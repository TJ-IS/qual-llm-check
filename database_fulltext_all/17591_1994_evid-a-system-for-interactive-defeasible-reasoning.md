---
otero_id: 17591
otero_key: "2BJF56MP"
title: "EVID: A system for interactive defeasible reasoning"
authors: "Robert L. Causey"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90028-0"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# EVID: A system for interactive defeasible reasoning

Robert L. Causey

The University of Texas, Austin, TX, USA

I describe a system for interactive, automated defeasible reasoning. An application program using this system can infer a conclusion defeasibly from a conjunction of supporting facts together with an appropriate general rule. This particular inference of the conclusion might be defeated by additional facts, although other independent evidence could still support the conclusion on the basis of other rules. The system has been implemented in Prolog, and includes an extensive logical interface that permits the user to interact with and override an application program's defeasible conclusions, subject to certain constraints on the user's consistency. Applications to decision support systems are described.

Keywords: Defeasible reasoning; Default reasoning; Non-monotonic reasoning; Decision support systems; Logic programming.

![](/api/attachments/2BJF56MP/fulltext/images/037278fb4306719948fd4b4887688510f751f85f79f483cdce0568181ed98bf2.jpg)

Robert L. Causey is Professor of Philosophy and a member of the Artificial Intelligence Laboratory at the University of Texas at Austin. He received a B.S. in Mathematics from the California Institute of Technology, and a Ph.D. in Logic and the Methodology of Science from the University of California at Berkeley. Causey has taught at the University of Texas since 1967, including eight years as Chairman of the Philosophy Department. He has investigated the logical foundations of measurement and of scientific explanations, is the author of Unity of Science (Reidel, 1977) and of numerous articles in philosophical and scientific journals, and is a co-author of the video-course Introduction to Artificial Intelligence and Expert Systems (Morgan-Kaufmann, 1988). His current research interests include knowledge representation in artificial intelligence, the logical structure of scientific theories, and automated reasoning.

Correspondence to: Robert L. Causey, Department of Philosophy, Waggener Hall 316, University of Texas, Austin, Texas 78712-1180 USA. E-mail: rlc@cs.utexas.edu.

## 1. Introduction to defeasible reasoning

1.1. Practical decision making often depends on information that is not directly available to us, but which can be inferred from other information that is available. For instance, while driving we may not directly experience the feel of a slick street, but infer that the street is slick from the visible evidence that it has just begun to rain. This inference is based on the rule-of-thumb that, in typical situations, if rain has begun to fall on a previously dry street, then that street is slick. There usually will be additional rules-of-thumb linking other kinds of evidence (e.g., an oil spill) to a given conclusion (e.g., slick street). Such rules may have exceptions; for instance, a special kind of road building material may prevent the onset of rain from causing slickness. Thus, the additional information that the particular street in question is made of this material will defeat (block) the inference of slickness from the evidence that it has just begun to rain.

In recent years there has been much interest in what is called “default”, or “defeasible”, or “nonmonotonic” reasoning. The first two terms have been used in a variety of ways by different writers, but it is generally the case that “default” reasoning is related to “defeasible” reasoning, and both of these are special types of “nonmonotonic reasoning”. Many articles on the latter subject are reprinted in [4], and Chapter 6 of [3] is a useful exposition. In connection with decision support systems, defeasible reasoning is considered in [7], [5], and [1], where many other references to the literature are cited. Some comparisons with this literature will be made in Section 6.

1.2. To avoid confusion with other terminology in the literature, I will use the following general characterization: A defeasible rule is a special form of conditional (if-then) sentence $^{1}$ that permits one to infer a conclusion sentence (corresponding to the consequent of the rule) from a conjunction of supporting evidential sentences (corresponding to the antecedent), provided that this inference is not blocked (defeated) by other statements of defeating conditions. A conjunction of defeating conditions is called a defeater. There may be many defeasible rules with the same consequent following from various antecedents (conjunctions of different kinds of supporting evidence). In general, there will also be a variety of defeaters that block inferences of instances of the consequent from one or more of the conjunctions of supporting evidence. Notice that a defeater does not defeat the rule; it blocks an inference that would otherwise be based on that rule together with supporting evidence. This characterization is still vague in some respects; the following simple, fictional example will illustrate the key ideas involved. It is assumed that the reader is familiar with first order predicate logic; some familiarity with Prolog programming will be helpful. In Prolog, predicate and individual constants are written in lower case, and variables in upper case. I will follow those conventions. In later sections, I will use bold face for Prolog code. The following examples are presented informally, but are also in bold face because I will later show how they can be implemented in Prolog.

Suppose that we are interested in whether or not a person uses a computer in his or her work. We introduce a predicate, $\mathbf{ucw}(\mathbf{P})$ , which is true of any person P, if P personally interacts with a computer as a part of P's job. Such information might be of interest to a salesperson representing a computer manufacturing company. A person's occupation, together with certain other facts regarding that person, will serve as evidence that $\mathbf{ucw}(\mathbf{P})$ . For a simple example, we assume the following fictional, but not implausible, rules:

ucw(P) if (defeasibly) (engineer(P))

and can \_type(P) .

$$
\operatorname{ucw} (\mathbf {P}) \text {if (defeasibly)} (\operatorname{professor} (\mathbf {P})\tag{1}
$$

and can \_type(P) ).

(2)

The term if(defeasibly) will be given an exact interpretation in a later section, but its intended meaning, in the case of (1), can be roughly described as follows: The condition (engineer(P) and can\_type(P)) constitutes one piece of prima facie evidence for the conclusion ucw(P). Thus, for a typical person P, who satisfies this prima facie evidence, we may infer ucw(P). By “typical” I mean that we do not have any defeating conditions that would defeat (override) the evidential support of (engineer(P) and can\_type(P)) for the conclusion ucw(P), and hence block the inference of the conclusion. If such a defeating condition (a defeater) becomes available, then it will defeat this conclusion for this evidence. It is important to understand that such a defeat does not imply that this conclusion is false, for it might still follow from some other, independent evidence. But if no other supporting evidence is available, and the evidence (engineer(P) and can\_type(P)) is defeated, then we are not warranted in making a defeasible inference that ucw(P). Yet, as will be seen later, we may still choose to believe that it is true in particular circumstances where we have other, special reasons for this belief. It should already be clear that the exact meaning of if(defeasibly) is rather complex and subtle; this meaning will be explicated further in Section 3.

Defeaters (conjunctions of defeating conditions) are components of defeater rules. Here are three examples:

ucw(P) is defeated \_for (engineer(P))

and can \_type(P) if

company\_president (P).

(3)

ucw(P) is defeated \_for (professor(P))

and can \_type(P) if

art \_professor(P).

(4)

ucw(P) is defeated if fears \_computers(P). (5)

The relationship, defeated\_for, occurs in (3) and (4), so these rules state conditions for relative defeats. Thus, (3) asserts that the additional information, company\_president(P), defeats the evidential support of (engineer(P) and can\_type(P)) for the conclusion ucw(P). In this case, company\_president(P) is a “conjunction” of one statement; company\_president(P) is the defeater corresponding to the defeater rule (3). Similarly, if we know that bob, say, is a professor who can type, then by (2) we may defeasibly infer that ucw(bob), but if we find out that bob is also an art professor, then this inference is defeated by (4). It is important to understand that it may still be the case that ucw(bob), but we are no longer entitled to infer this by means of (2) when (2) has been relatively defeated. The conditions, company\_president(P) and art\_professor(P), are relative defeaters because each of them defeats (blocks) an inference based on (relative to) some piece of evidence. If bob is an engineer, can type, and is also a professor, then an inference from either (1) or (2) might be relatively defeated by either (3) or (4) together with the corresponding relative defeater, respectively, while the other inference is still allowable.

The condition, fears \_computers(P), in (5), is an absolute defeater. If fears \_computers(bob) is true, then we are not allowed to infer that ucw(bob) from any evidence. In other words, fears \_computers defeats any supporting evidence corresponding to the antecedent of any defeasible rule with the conclusion ucw(bob). Yet, as will be seen in Section 4.2, we may still choose to believe that ucw(bob) in special circumstances where we have other, special reasons for this belief.

1.3. In order to summarize the ideas introduced above, let concl, $ev_{1}, ev_{2}, \ldots, ev_{k}$ , be predicates followed by zero or more free variables or individual constants. (If there are no variables or constants, the predicate is treated as a propositional constant.) Then a defeasible rule will usually have the form given by this schema:

concl if (defeasibly)

$$
\left(\mathrm{ev} _ {1} \text {   and   } \mathrm{ev} _ {2} \text {   and   } \dots \text {   and   } \mathrm{ev} _ {k}\right).\tag{6}
$$

Later we will also allow negations of the $ev_{i}$ , using Prolog's negation by failure. As mentioned previously, the exact interpretation of if(defeasibly) will also be given later. I am not suggesting that it must be a new kind of if-then logical connective.

Now let $d_{1},\ldots,d_{n}$ , also be predicates followed by zero or more free variables or individual constants. Then a relative defeater rule has the form: concl is defeated \_for

$$
\begin{array}{l} \left(\mathrm{ev} _ {1} \text { and   ev} _ {2} \text { and...and   ev} _ {\mathbf {k}}\right) \text { if } \\ \left(\mathrm{d} _ {1} \text { and...and   d} _ {\mathbf {n}}\right). \end{array}\tag{7}
$$

An absolute defeater rule has the form: concl is defeated if $(\mathbf{d}_{1}$ and ... and $d_{n})$ .

(8)

The conjunctions in the antecedents of (7) and (8) are relative and absolute defeaters respectively. The relative defeater rule schema (7) uses the 2-ary metapredicate defeated\_for, whereas (8) uses the 1-ary metapredicate defeated. All of these characterizations will be refined later.

Defeasible rules, defeater rules, and both relative and absolute defeaters, are used in practical reasoning, including the reasoning required for decision making. Some might insist that such rules should be replaced by assertions of conditional probability. I would agree that probabilistic decision models are often useful, when suitable probability values can be obtained. But suitable values are often not available. In fact, most of our practical reasoning does not involve probability calculations; rather, it is based on nonprobabilistic, defeasible reasoning. Moreover, as pointed out in [7], pp. 98–99, a decision support system (DSS) that relies on probability values can be very difficult to expand and maintain.

It should be noted that many previous investigations of defeasible and default reasoning do not make use of the distinction between relative and absolute defeaters. In these investigations, and in the reasoning systems based on them, one usually finds a facility for handling only those cases approximately corresponding to our absolute defeaters. Pollock's work is one exception to this; see [10], which distinguishes "rebutting" from "undercutting" defeaters. Although there are significant differences between Pollock's approach and the present one, his distinction seems to have a motivation similar to that behind the current distinction between absolute and relative defeaters. The above example and the further discussion below should make it very clear that such a distinction is needed for adequate representation of practical, defeasible, evidence-based reasoning.

## 2. Functional requirements for an interactive defeasible reasoning system

2.1. Statements (1)-(5) in the previous section are examples of "domain knowledge" because they make assertions about a particular application domain. Let us call such knowledge "longterm” if it is stored in a computer program and we do not expect that it will require revision very often. An interactive defeasible reasoning program (IDRP) is an interactive program containing long-term knowledge that is used together with user-entered “current data” to provide advice to the user. For instance, a user query might ask whether ucw(bob), and the response will be inferred from the long-term knowledge of the IDRP together with user-supplied, current information about bob. Although the general concept of a DSS is broader (including probability based systems), it should be clear that an IDRP could be used as a DSS or as part of one.

This article will not present a general theory of defeasible reasoning, but it will describe some of the most important features of an IDRP that are required to assist with practical decision making. In particular, we will be concerned with IDRP's that are able to perform evidence-based reasoning, and are designed so that the user has the ability, subject to consistency of his own inputs, to defeat (block) the defeasible inferences of the program. A number of other highly desirable features of an IDRP will also be described. These conditions will first be summarized in general terms below; later I will show how these features can be realized within the backward chaining deduction environment of Prolog.

Of course, one does not want to program from scratch each particular IDRP for each application of interest. It is more convenient to have a general “shell” that interprets domain knowledge and assists user interaction. Such a shell will be called an interactive defeasible reasoning system (IDRS). For the discussion in the remainder of this section, let us give the name EVID to an idealized IDRS. I will describe some of the main functional characteristics which EVID should have. In some cases it will be convenient to use descriptions that directly refer to features of EVID; in other cases, it will be more convenient to describe how an IDRP interpreted by EVID should behave. In the latter case, however, this behavior will still largely be the result of the general functionality of EVID.

2.2. Before we proceed, it is important to note that an IDRP will usually contain some nondefeasible rules in addition to its defeasible ones. For example, we might have

professor(P) if art \_ professor(P).

(9)

The next few paragraphs describe desirable functional requirements of the ideal EVID.

2.2.1. If the user enters the information, art\_professor(bob), the IDRP will be able to infer professor(bob) from (9). Thus, some of the system's conclusions will hold positively (as in this case), and some will only hold defeasibly, as we have already seen. EVID should be able to tell the user how each of the IDRP's conclusions holds, whether positively, defeasibly, or in some other mode. Holds will be discussed in more detail in Subsections 4.1 and 5.2. Also, note that the actions of entering or removing facts are subject to various constraints; see 2.2.8 below.

2.2.2. If the IDRP can infer a conclusion from one or more pieces of evidence, for instance ucw(bob) from (engineer(bob) and can\_type(bob)), the system should be able to justify this conclusion by citing all of the supporting evidence. In most applications this should not be very burdensome since there will usually only be a few pieces of supporting evidence. Moreover, the user will typically want to know what all of this evidence is, in order to facilitate the types of interactions described below.

2.2.3. Sometimes the user will expect the IDRP to infer a conclusion, but it does not. Often this will happen because all available supporting evidence has been defeated. The system should be able to report these defeats to the user.

2.2.4. The user, and more often the “knowledge engineer” programming the IDRP, may want a complete deduction of one of the system’s conclusions. EVID should contain a proof-trace facility for displaying such proofs.

2.2.5. In some (perhaps most) applications there will be times when the user wants to know what additional user-input data would enable the IDRP to infer a conclusion which it currently cannot. For instance, suppose the IDRP does not yet have any information about bob, but the user wants to know what would enable it to infer ucw(bob). EVID should be able to analyze the domain rules and tell the user what pieces of evidence (if entered) would lead to the conclusion ucw(bob). It is not necessary for the program to perform an exhaustive, and computationally expensive, search through all possible ancestor premises of the desired conclusion. Experimental tests have indicated that such a search can produce more information than the user typically wants or needs. Instead, it is useful to tell the user what conjunctions of evidence occur in the bodies of rules that have the desired conclusion as their head. If desired, the user can then do a manual, recursive search for possible facts that would support some of this evidence.

2.2.6. There will be times when the system infers a defeasible conclusion which the user doubts. In some cases of this type the user may suspect that there is additional defeating information available to him that has not been entered into the system, but he may not know exactly what additional information is relevant in this manner. EVID should be able to tell the user what additional data would serve as either relative or absolute defeaters. As in the previous paragraph, an exhaustive search is not required, but the program should find all of the possible facts that would serve as immediate defeaters.

2.2.7. Suppose that the IDRP infers from appropriate evidence that, defeasibly, ucw(bob). Suppose further that the user does not have available any additional data that would defeat this inference. Still, the user may have good reasons for believing that, in this particular situation, the available evidence is not sufficient to conclude that ucw(bob). Indeed, the user may have good reason for believing that there is no evidence of any kind to warrant the conclusion that ucw(bob). Regardless of how thoroughly the long-term knowledge of the IDRP has been developed, there will be atypical situations that are not covered by suitable defeater conditions. Thus, occasionally the IDRP may defeasibly infer some conclusion with which the user disagrees, and such that the user cannot defeat this conclusion simply by the input of additional information known to the user. EVID should allow the user to defeat this conclusion, either relative to particular supporting evidence, or absolutely, provided that the user does not contradict himself in so doing. Thus, subject to self-consistency, EVID should permit the user to have the “last word” on defeasible conclusions. Such a user-entered override of an IDRP conclusion is called a “user defeat”. Although I use the phrase “defeat a conclusion”, all that is really happening is that one or more inferences are being blocked. Thus, a user defeat, as with any other defeat, only blocks inferences, either relatively or absolutely.

2.2.8. The user is permitted to add new information and to defeat some of the system's conclusions. EVID should also allow the user to remove data previously added by the user and to undefeated conclusions that the user has previously defeated (either relatively or absolutely). Naturally, there is the risk that the user may, in performing various combinations of such actions, either generate a logical contradiction from his inputs, or create a conflict that arises from specific domain knowledge. Also, the user may introduce certain kinds of redundancies which, although not logically harmful, may create deductive inefficiencies. EVID should be designed to prevent, as far as is practical, the user from performing such undesirable actions, while still leaving the user “reasonable freedom” in “having the last word.” It is difficult to characterize this general aim precisely and, because of computational limitations of logic, impossible to check for all inconsistencies. Therefore, these constraints on user interactions must be largely formulated as particular implementation features (which will be described in a later section).

The previous paragraphs describe, very generally, the functionality desired in our idealized EVID, an interactive defeasible reasoning system. Of course, many details still need to be explicated, and there are other, special features that either are intrinsically desirable, or are useful in achieving the general functionality we desire. The following sections give more detail in the context of a particular Prolog implementation.

## 3. Implementation of EVID-style defeasible rules

3.1. This section presents a simple application program that is interpreted by my interactive defeasible reasoning system EVID. Recall that EVID is the “shell” program that is used to interpret various application programs. The example application program will introduce some key metapredicates and show how they are used to formulate defeasible rules and defeater rules. The next section will describe EVID itself in more detail.

EVID has been under development since late 1988, and experimentation and further development are continuing, so some details of the following description are subject to change. Because of the experimental nature of this work, it would be unwise to present a precise characterization of an IDRS, since some details would likely become obsolete as a result of future developments. When describing EVID it is also difficult to say exactly which of its features are special implementation details, and which are “essential” features of an IDRS. Nevertheless, I do believe that most of what is described below should at least be considered highly important features of any Hornclause, backward chaining IDRS.

The current EVID is implemented in Prolog and makes essential use of the standard Prolog negation by failure. Although the unrestricted use of negation by failure can lead to contradictions, when used only with Horn clauses it preserves consistency; see [3], pp. 119–120. It is also important to observe that reliance on negation by failure constitutes an epistemological assumption that we know all of the relevant laws and positive atomic sentences about an application domain $^{2}$ . Indeed, I wish to emphasize that not(concl), in the sense of negation by failure, merely means that concl cannot be proved on the basis of the current knowledge of a program. In such a situation, the user should be permitted (subject to certain restrictions) to add concl to the current body of facts of the program.

EVID's design is motivated by epistemological considerations and a desire not to introduce new kinds of logical connectives, modalities, or inference rules. I am in general agreement with most of the criticisms, presented in [5], of general nonmonotonic logics. Fortunately, those criticisms do not apply to EVID, at least in any damaging way that I can see, since it uses standard Prolog deductions, supplemented with some metapredicates and negation by failure.

3.2. The current Version 0.9 EVID contains about 90 internal predicates and over 1300 lines of Prolog. The most important of these EVID predicates are metapredicates. This program is too complex to describe in detail; instead, L will use a very simple application example to explain what EVID does and how it works. This example program is related to the ucw example that was described in general terms in Section 1. The program is given in the following listing $^{3}$ :

```prolog
% Domain predicate declarations....
definite(engineer(_)).
definite(professor(_)).
definite(company_president(_)).
definite(art_professor(_)).
definite(computer_artist(_)).
defeasible(ucw(_)).
defeasible(can_type(_)).
defeasible(fears_computers(_)).
% A nondefeasible rule....
professor(P):-art_professor(P).
% Defeasible rules....
can_type(P):-
    professor(P),
    not(defeated_for(professor(P), can_type(P))). 
ucw(P):-
    engineer(P),
    can_type(P),
    not(defeated_for((engineer(P), can_type(P)), ucw(P))). 
ucw(P):-
    professor(P),
    can_type(P),
    not(defeated_for((professor(P), can_type(P)), ucw(P))). 
ucw(P):-
    computer_artist(P),
    not(defeated_for(computer_artist(P), ucw(P))). 
% Relative defeater rules....
defeated_for((engineer(P), can_type(P)), ucw(P)):-
    engineer(P),
    can_type(P),
    company_president(P).
```

```prolog
defeated _for((professor(P), can _type(P)),
    ucw(P)):
    professor(P),
    can _type(P),
    art _professor(P).

% Absolute defeater rule....
defeated(ucw(P)):- fears _computers(P).
```

First of all, notice that some of the predicates in the example are declared to be definite and others defeasible. EVID's own internal predicates are declared (within EVID) to be evid\_predicates; any predicate in an application program (such as the above example) that is neither an evidPredicate nor a built-in Prolog system predicate must be declared as definite or defeasible. EVID makes extensive use of these declarations on frequent occasions of runtime predicate type checking. Although runtime checking uses extra computations, the EVID declarations enhance program efficiency and error checking in other ways. In the following, a predicate that is either definite or defeasible is called a domain predicate.

EVID declarations were actually invented, however, for epistemological reasons. It is assumed that some predicates are used to represent “basic facts” while others are used to represent “defeasible conclusions” that are (usually) inferred from the basic facts. “Defeasible conclusions” are subject to direct user overrides; the “basic facts” are not. The knowledge engineer who develops the application program is given complete freedom to decide which predicates are definite and which are defeasible, and these declarations will depend on the features of the particular application domain under consideration. In extreme situations, all predicates might be defeasible or all definite (although in the latter case, the knowledge base (KB) will not have any defeasible rules). It would be out of place here to attempt a detailed epistemological justification for the EVID declarations. It will be seen below how these declarations impose constraints on the knowledge representation style of EVID-based IDRP’s, and how they determine which of the program’s conclusions can be directly blocked by the user (user defeated). It should become clear that the declarations have a natural motivation, and are useful in developing KB’s and for program efficiency.

In the case of the above example, we assume that information such as art\_professor(jim) is basic in the sense that it either must be supplied to the program as an externally obtained fact, or it must be derivable within the program in such a way that the user cannot directly defeat the conclusion of this derivation. $^{4}$ Hence, art\_professor is declared to be definite. The predicate professor is also declared definite for the same reason. Note that a fact such as professor(jim) can be inferred by the program from art\_professor(jim) by a nondefeasible rule, as shown in the program. On the other hand, ucw is declared defeasible since the program will be able to use one or more defeasible rules to infer facts such as ucw(jane) from other, current information in the program. In general, atomic facts stated in terms of defeasible predicates (such as ucw(jane)) are those which an IDRP can infer from prima facie evidence by inferences that can be blocked when additional, defeating information is obtained. Yet, the definite/defeasible distinction is not based on any general, a priori principles, but is relative to the context of an application and determined by the designer of the KB.

To simplify the terminology, an atomic formula or the negation of an atomic formula (using Prolog's not, negation by failure) will be called a literal. If an atomic formula uses a definite or defeasible predicate, then that formula will also be called definite or defeasible, accordingly. The sample application program contains a nondefeasible rule and several defeasible rules. A nondefeasible rule always has the form of a standard Prolog rule, with a definite formula in the head of the rule. The body of such a rule is always a conjunction of one or more literals. These literals can be formed from domain predicates or Prolog system predicates (such as those corresponding to numerical operations).

A defeasible rule must have a defeasible atomic formula in its head, and there are only two allowable forms of defeasible rules:

concl:-

$$
\begin{array}{l} \mathbf {e v} _ {1}, \mathbf {e v} _ {2}, \dots , \mathbf {e v} _ {\mathbf {k}}, \\ \text { not } (\text { defeated\_for } ((\mathbf {e v} _ {1}, \mathbf {e v} _ {2}, \dots , \mathbf {e v} _ {\mathbf {k}}), \text { concl })). \end{array}\tag{10}
$$

concl:-

not (defeated (concl)).

(11)

In (10) and (11), concl and the $ev_{i}$ may have zero or more free variables or individual constants. The head, concl, is a defeasible atomic formula. The $ev_{i}$ may be any literals using domain predicates or Prolog system predicates. Important distinguishing features of these two rule forms are the required uses of the EVID predicates, defeated\_for and defeated. The reader should notice that the general form of (6) is implemented by (10) and interpreted by EVID in the form of (10). It is important to observe that both (10) and (11) are standard Prolog rules; they simply have special forms using the defeated\_for and defeated metapredicates, and are further constrained by the types of predicates allowed to occur in particular parts of the rules. A rule of form (10) enables the program to infer concl from the evidence ( $ev_{1}, ev_{2}, \ldots, ev_{k}$ ) provided that this inference of the conclusion is not defeated\_for this particular evidence. Rules of form (11) are rare, but can be used to infer that concl holds prima facie without any special evidence to support it, unless this conclusion is absolutely defeated.

Finally, the little sample program contains some relative defeater rules and an absolute defeater rule. Rules of these types have the forms: defeated \_for((ev $_{1}$ , ev $_{2}$ , ..., ev $_{k}$ ), concl):-

$$
\begin{array}{l} \mathbf {e v _ {1}}, \mathbf {e v _ {2}}, \ldots , \mathbf {e v _ {k}}, \\ \mathbf {d _ {1}}, \mathbf {d _ {2}}, \ldots , \mathbf {d _ {n}}. \end{array}\tag{12}
$$

defeated (concl) :-

$$
\mathbf {d} _ {1}, \mathbf {d} _ {2}, \dots , \mathbf {d} _ {n}.\tag{13}
$$

Rule forms (12) and (13) are the EVID-style implementations of (7) and (8), respectively. In (12) and (13), the $d_{i}$ are the conjuncts of the relative and absolute defeaters, respectively; they may be literals formed from domain predicates or Prolog system predicates. In Section 5 below, (12) and (13) will be augmented with another type of defeater rule which I call a contra-defeater.

3.3. At this point a few additional remarks may help to avoid some misunderstandings. First note that in (12) the evidential conditions, $ev_{i}$ , are restated in the body of the rule so that Prolog will apply the relative defeat only to domain objects that satisfy these evidential conditions. Thus, the syntax of (12) is a little cumbersome. But this is a minor inconvenience. It is easy (if one desires) to write the rules in something like the forms of (6)–(8), and then have a simple re-write program convert them into the Prolog forms (10), (12), (13).

Relative and absolute defeats are conceptually related, and EVID represents this relationship. EVID has an internal rule that says: a conclusion is defeated for any evidence whatsoever, if that conclusion is (absolutely) defeated. In other words, defeated\_for(\_, concl) follows from defeated(concl), where \_ is a variable that can be instantiated by any evidential statement. It must be emphasized that defeated\_for is a 2-ary predicate, and hence is more general than defeated. The fact that defeated\_for is 2-ary is what enables EVID to defeat a prima facie conclusion relative to some evidence, while that conclusion may still be supported by other evidence. The 1-ary defeated predicate will not provide this flexibility, since it is intended to represent absolute defeats. Internally, EVID insures that, once defeated(concl) is derived, then concl is not supported by any evidence whatsoever that is in the KB. It will only be true by a direct user addition of concl. The two defeater rules in the sample program illustrate how defeated\_for and defeated are used.

In order to clarify these ideas further, let ev abbreviate some conjunction of evidential conditions. Note that defeated\_for(ev,concl) can be true while concl is also true, because there may be other, undefeated evidence that supports concl. If all currently true supporting evidence for concl is defeated, and concl has not been explicitly asserted as a fact, then a query of concl will return “no”, but this only means that Prolog cannot currently infer the conclusion. Additional, new evidence might result in concl again being inferable. If defeated(concl) results from current facts plus the IDRP’s internal rules, then concl is absolutely defeated, so there can be no additional evidence that would enable the IDRP to infer concl. Yet, even in this case EVID will permit the user to add concl to the current body of facts (as the next section will show). In other words, concl is logically consistent with defeated(concl), since the latter only blocks the IDRP from using defeasible rules to infer concl. (Section 4.2 will describe some additional restrictions in the case of user overrides.)

It might be suggested that $\phi$ if (defeasibly) $\psi$ and $\phi$ is defeated for $\psi$ if $\rho$ are in some sense equivalent to the Prolog rule, $\phi : -\psi$ , $not(\rho)$ . From this, one then might suggest that we can simply replace the EVID rules,

concl \_a :- ev\_a,

$$
\text { not } (\text { defeated\_for } (\text { ev\_a }, \text { concl\_a }))  .\tag{14}
$$

$$
\text { defeated\_for } (\text { ev\_a }, \text { concl\_a}): - \text { ev\_a }, \text { d\_a }.\tag{15}
$$

with the simpler

$$
\text { concl\_a }: - \text { ev\_a }, \text { not } (\text { d\_a }).\tag{16}
$$

However, such a replacement would destroy most of the unique and valuable functionality of EVID. Recall that an IDRP may use both defeasible and nondefeasible rules. The nondefeasible rules have been described above, and such a rule will behave logically just as it would without the EVID environment. Thus, in an EVID-interpreted IDRP, a rule like (16) would behave just as an ordinary Prolog rule, and concl\_a would need to be declared as a definite predicate.

To get a sharper focus on the differences, assume that concl\_a, ev\_a, and d\_a are all definite predicates. Also assume that concl\_b is defeasible, and that ev\_b is definite. Let us compare (16) with

concl\_b :- ev\_b,

$$
\text { not } (\text { defeated\_for } (\text { ev\_b }, \text { concl\_b })).\tag{17}
$$

First note that (16) contains a specific overriding condition, d\_a, whereas (17) contains no defeating condition at all. If we tried to do away with defeated\_for by using rules of the form of (16), each defeating condition (or conjunction of defeating conditions) would need to be referenced (either alone or in a disjunction with others) in some rule like (16). This is not only awkward, but causes a major loss of EVID's functionality. Using EVID we can state a defeasible rule like (17) even if the knowledge base contains no defeater rules for concl\_b at all. Such general defeasible rules cannot be stated if we are restricted to rules like (16), which require a specific condition like d\_a.

Recall that, by Functional Requirement 2.2.7, EVID should allow the user to perform a manual, direct user defeat of any defeasible conclusion an IDRP infers. As previously explained, defeats are really cases of inferences being blocked, but it is also convenient to speak loosely of defeating or overriding conclusions. Support of such user overrides is a primary design goal of EVID. Such user overrides (illustrated below in Section 4.2) do not depend on any specific defeating conditions, such as d\_a. In fact, direct user defeats can be applied to any defeasible inference made within an EVID-interpreted IDRP, even if, as in the case of (17), there are no associated defeater rules in the knowledge base. Thus, EVID's capability of handling rules like (17), without specific defeating conditions, and with no associated defeater rules at all, is a most important prerequisite for EVID's functionality. If we restricted ourselves to the use of rules of the form of (16), we would lose this functionality. Of course, for semantical reasons, I am assuming here that the Prolog implementation does not permit the user to assert not(F), where F is some formula and not is negation by failure. It should also be noticed that EVID permits the user to defeat relative to specified evidence. The assertion of a negation predicate, which is 1-ary, would not substitute for such relative user defeats.

EVID also makes an important conceptual distinction between rules like (16) and rules like (17). In the case of (16), not(d\_a) is considered by EVID to be part of the supporting evidence, along with ev\_a, for concl\_a. Recall that evidential conditions are conjunctions of literals, which include negated conjuncts like not(d\_a). On the other hand, in (17) not(defeated\_for(ev\_b, concl\_b)) is not a piece of supporting evidence, but rather a metatheoretical statement that there is no information which defeats the evidential support of ev\_b for concl\_b. Of course, this evidential support can be defeated by either the firing of a defeater rule, or by a direct user defeat.

Although a rule of the form of (16), using negation by failure, is one type of “default rule”, it is still considered to be a nondefeasible rule within the EVID conceptual framework. One may wonder why there is a need for default rules like (16) as well as EVID-style defeasible rules like (17). A simple example should show why. Suppose that a large corporation hires many types of employees and has strictly formulated employee policies. One company rule may say that an employee is paid hourly if he (or she) is classified as a welder. This rule also allows only one, very rare exception, namely if the welder has been put on an annual salary by special action of the company president. Then a knowledge base about this corporation might reasonably include a rule,

paid \_hourly(Emp) :- welder(Emp),

$$
\text { not } (\text { presidential\_exception } (\text { Emp }))  .\tag{18}
$$

in which the predicates are all definite.

It is assumed that, if an employee is a presidential exception, then this fact will be in the KB. Clearly, (18) has the form of (16), and if all that the KB knows about bob is that he is a welder, by (18) the IDRP will conclude by default that paid \_hourly(bob). In this type of situation we do not want the user to be able to make a direct assertion of a defeat or of any kind of negation of this conclusion. When the user interacts within the EVID shell, such assertions are blocked. In fact, this conclusion should only go away if there is specific information in (or added to) the KB that presidential \_exception(bob). Yet, there are many other situations in which we do want the user of a Decision Support System to be able to make a direct override of the system's inferences. A good example is an interactive, revisable planning program that not only makes initial plans, but also assists the user in making interactive plan revisions as new, and unexpected, contingencies arise. Having served as the “expert” in the design of such a program (see [8]), I am convinced that it is usually not feasible to write rules covering the breadth of real-world contingencies, and that there will be times when the user should override the program's advice. For these types of situations EVID provides defeasible rules like (17), and an interface for making such overrides. For the more restricted situations, EVID allows default rules like (16) and (18), or even more restricted rules that use no negation by failure at all.

Thus, EVID makes an important conceptual distinction between a nondefeasible (but default)

rule with some negative evidence (like (16)) and a “genuine” defeasible rule (like (17)). This conceptual distinction greatly enhances the representational capabilities of EVID compared to a program that merely uses rules like (16). Also, by means of the metapredicates, defeated\_for and defeated, plus some others pertaining to user defeats and other conditions, EVID keeps track of the status of evidential support, user overrides, current defeating data, etc. This “book keeping” is required for some of EVID’s functionality, and it helps in the operation of an efficient, effective interface. The examples in the following sections will illustrate some of these features.

## 4. What EVID does

## 4.1. Introduction to EVID's operations

As previously mentioned, EVID is a large program with many predicates. In this article, I will only mention a few of the main EVID predicates that are primarily for user interactions. In order to use EVID, it is loaded into Prolog along with one or more application files. Suppose that EVID is loaded together with the sample application program listed in the previous section. One important EVID predicate is addit; it allows the user to assert new facts as current data for the application IDRP. However, addit checks that several conditions are satisfied (some of which will be mentioned later) before it permits a new fact to be asserted. Initially, if we do addit(engineer(bob)) and addit(professor(bob)), EVID will permit these facts to be asserted and will also cause them to be remembered by the system as user added facts.

EVID has a predicate, holds, such that holds(How,Sent) informs us How a true sentence holds. Sent is either a definite or defeasible atomic formula constructed from a domain predicate followed by individual constants and variables. As is customary, free variables are assumed to be universally quantified, so a formula with free variables is actually a sentence. There are several possible values for how a sentence can hold. If the sentence is defeasible (i.e., is atomic with a defeasible predicate), then it always holds defeasibly. If the sentence is definite (is atomic with a definite predicate), and all derivations of this sentence use nondefeasible rules with no negation by failure, then the sentence holds positively. Currently, EVID also distinguishes two other values for holds that are intermediate between these cases. These modes apply to atomic formulas with definite predicates. A sentence of this form may have several derivations. Some of these derivations may depend on an ancestor premise that holds defeasibly. The holds predicate indicates such cases. In other cases, there may be no defeasible ancestors, but there may be a derivation with an ancestor premise using Prolog's not, and hence using negation by failure. For instance, if an IDRP uses (18) of the previous section to conclude by default that paid\_hourly(bob) because bob is a welder, then this conclusion holds by at least one negation by failure proof. The holds predicate so indicates. Returning to the current example about professors, computer users, etc., if we ask the system, holds(How,professor(bob)), it replies "How = positively". If we ask, holds(How,ucw(bob)), it replies "How = defeasibly".

EVID includes a predicate why, which returns a special type of justification for conclusions. Since $\mathbf{ucw}(\mathbf{bob})$ is now true, we can ask why. With the output in a slightly revised format, here is what we obtain $^{5}$ :

?-why(ucw(bob)).

ucw(bob)

HOLDS defeasibly.

IT IS CURRENTLY SUPPORTED BY THE FOLLOWING EVIDENCE:

[engineer(bob),can\_type(bob)]

[professor(bob),can\_type(bob)]

AND ALSO THE:
[SUPPORTING EVIDENCE = =>]
[ IS DEFEATED BY = => ]

Notice that currently there is no evidence for $\mathbf{ucw}(\mathbf{bob})$ that is defeated, as is indicated by the blanks after the arrows. However, we might want to know what additional facts would defeat this conclusion if these facts were true. EVID has a predicate, howdefeatit, which tells us the following:

?-howdefeatit(ucw(bob)).

CAN BE DEFEATED BY ADDITION OF ANY OF THESE ABSOLUTE DEFEATERS [fears \_computers(bob)]

IT CAN BE DEFEATED BY ADDITION OF ALL OF THESE RELATIVE DEFEATERS

[SUPPORTING EVIDENCE == >, engineer-
(bob), can \_type(bob)]

[ BY THE DEFEATER == >, company\_president(bob)]

[SUPPORTING EVIDENCE == >, professor (bob), can \_type(bob)]

[ BY THE DEFEATER == >, art \_ professor (bob)]

CURRENTLY THE
[SUPPORTING EVIDENCE == >]
[ IS DEFEATED BY == > ]

Notice that howdefeatit gives the user considerable information. It first lists all of the absolute defeaters. It then lists all relative defeaters that are not presently true, but which would affect the current supporting evidence if they were. Finally, like why, it lists all current defeaters, if any. If it had been the case that bob were only a typing engineer, then howdefeatit would not have listed the art \_professor(bob) defeater case.

Suppose that we now do addit(company\_pre-sident(bob)). This will relatively defeat the supporting evidence (engineer(bob), can\_type(bob)). But this is only a defeat of the inference from this evidence, so this evidence no longer supports the conclusion. But a defeat does not imply that it is false that ucw(bob). In EVID we only get a negative result by a total failure of Prolog to derive the conclusion. In this case, the other supporting evidence, (professor(bob), can\_type(bob)), will still be undefeated, so ucw(bob) will still follow defeasibly from this other evidence. Thus, after adding that bob is a company president, howdefeatit responds with:

?- howdefeatit(ucw(bob)).

ucw(bob)

CAN BE DEFEATED BY ADDITION OF ANY OF THESE ABSOLUTE DEFEATERS [fears \_computers(bob)]

IT CAN BE DEFEATED BY ADDITION OF ALL OF THESE RELATIVE DEFEATERS

[SUPPORTING EVIDENCE = => ,professor (bob),can\_type(bob)]

[ BY THE DEFEATER = = >, art \_ professor (bob)]

CURRENTLY THE

[SUPPORTING EVIDENCE = = >, engineer (bob), can \_type(bob)]

[ IS DEFEATED BY == >, company\_president (bob)]

Notice that the now defeated supporting evidence engineer(bob), can\_type(bob), together with its currently true relative defeater company\_president(bob) have been moved from above to below the dashed line in the display. If we also addit(fears\_computers(bob)), then we will obtain:

?- howdefeatit(ucw(bob)).

ucw(bob)

IS NOT TRUE, AND CURRENTLY THE

[SUPPORTING EVIDENCE == >, \*all\_evidence\*]

[ IS DEFEATED BY == >,fears \_computers(bob)]

[SUPPORTING EVIDENCE = => ,engineer-
(bob),can\_type(bob)]

[ IS DEFEATED BY == >, company\_president (bob)]

Notice that howdefeatit now says that ucw(bob) is not true (in the sense of negation by failure, as usual). We now have both a relative and an absolute defeater active. The absolute defeat is represented by \*all\_evidence\*, which is an EVID propositional constant which is declared to be definite and always holds positively. If a conclusion (such as ucw(bob)) is defeated for \*all\_evidence\*, then EVID will insure that no evidence together with defeasible rules in the IDRP will support an inference of this conclusion. If we ask why(ucw(bob)), we will be told that ucw(bob) is not true and be advised to try whynot. The latter will give us the same information that howdefeatit shows here.

Suppose that someone had not seen the above displays, but queried the system, in its current state, about ucw(bob). He would receive the response “no”. Suppose this person wants to learn how this conclusion might be obtained. He could use the howgetit predicate as follows:

?- howgetit(ucw(bob)).

ucw(bob)

IS DEFEASIBLE, AND IS CURRENTLY NOT TRUE. WHEN TRUE AND UNDEFEATED, THE FOLLOWING SETS OF EVIDENCE SUPPORT OR DENY IT

[computer\_artist(bob)]

[engineer(bob),can\_type(bob)]

[professor(bob),can\_type(bob)]

CURRENTLY THE

[SUPPORTING EVIDENCE == >, \*all \_evidence\*]

[ IS DEFEATED BY == >,fears \_computers (bob)]

[SUPPORTING EVIDENCE == >, engineer (bob), can \_type(bob)]

[ IS DEFEATED BY == >, company\_president (bob)]

Although not previously mentioned, there are occasions when one uses a rule that supports the failure of a conclusion, rather than its truth. The response of howgetit reflects this possibility without specifying which evidence supports affirmatively or negatively. Evidence for a denial of a conclusion normally contains the Prolog propositional constant fail, so it is fairly easy for the user to use other EVID predicates in order to distinguish the affirmative from the denying evidence.

## 4.2. User overrides

The above examples show some of the basic ways in which EVID interprets an application program and acts as an informative interface between this program and the user. The examples show that the user can add additional facts to the application program and thereby (nonmonotonically) affect the conclusions this program can infer with EVID's assistance. Yet, when the user merely adds new factual in formation, he (or she) at most indirectly affects the system's inferences. In addition to such indirect effects, EVID also provides for direct user overrides of most of the program's defeasible conclusions and of its defeats of conclusions.

The latter type of override is simpler. Suppose that our example program was given only the following facts about bob: engineer(bob), can\_type(bob), company\_president(bob). Then ucw(bob) does not hold because the inference of this conclusion is defeated by the information that bob is a company president. Presumably the user who entered these facts believes that they are all true. Also, we assume that the rules in the system are correct in the sense that they represent good information about engineer, ucw, etc. Yet, in this particular instance the user has other good, external reasons for believing that ucw(bob) is true even though bob is also a company president, and this user also wants the program “to share this belief” with him. In such a situation the user simply uses addit to assert that ucw(bob). Then this fact will be both relatively defeated and also true, as shown here:

?- why(ucw(bob)).

ucw(bob)

HOLDS defeasibly.

IT IS CURRENTLY SUPPORTED BY THE FOLLOWING EVIDENCE:

[it\_is\_a\_defeasible\_user\_added\_fact]

AND ALSO THE:

[SUPPORTING EVIDENCE == >, engineer (bob), can \_type(bob)]

[ IS DEFEATED BY == >, company \_ president (bob)]

The reader should notice that howgetit and howdefeatit did not include the cases of direct user additions or overrides in their displays, since it is assumed that the user will know that these cases are almost always allowable. Note that holds considers that a user added fact holds defeasibly if it is built from a defeasible predicate, in this case ucw. Also, note that the only “evidence” applicable in this situation is that shown above (a user added fact). This affects the operation of howdefeatit; a query of howdefeatit(ucw(bob)) will now remind the user that ucw(bob) is user added (so cannot be defeated), but that it may be removed. Any user added fact can be removed by using the removeit EVID predicate. Finally, a user addition (using addit) would be allowed whenever ucw(bob) is not currently true, provided that it is not true because either there is no evidence in the system for it, or because any available evidence has been defeated by one or more relative or absolute defeats as a result of the program's internal rules and data. However, addit does not permit the user addition of a fact that is already true, regardless of how it happens to hold. As will be seen below, addit has other restrictions in the cases of user defeats.

Not only can the user override a program defeat by the addition of a fact (as just shown), he can also override a program defeasible inference by a manual defeat. EVID has two predicates, defeatit\_for and defeatit, for this purpose. Suppose that the example program was given only the following facts about bob: engineer(bob), professor(bob). Then ucw(bob) holds defeasibly on the basis of two different sets of supporting evidence, and, as was shown previously, a query of how defeatit(ucw(bob)) will display one absolute and two relative defeaters. Yet, the user will know about direct user overrides, and one possibility is a relative defeat such as defeatit\_for((engineer(bob), can\_type(bob)), ucw(bob)). After this is done, we can observe this:

?- howdefeatit(ucw(bob)).

ucw(bob)

CAN BE DEFEATED BY ADDITION OF ANY OF THESE ABSOLUTE DEFEATERS [fears \_computers(bob)]

IT CAN BE DEFEATED BY ADDITION OF ALL OF THESE RELATIVE DEFEATERS

[SUPPORTING EVIDENCE == >, engineer (bob), can \_type(bob)]

[ BY THE DEFEATER == >, company\_president(bob)]

[SUPPORTING EVIDENCE == >, professor (bob), can \_type(bob)]

[ BY THE DEFEATER == >, art \_ professor (bob)]

CURRENTLY THE

[SUPPORTING EVIDENCE == >, engineer (bob), can \_type(bob)]

[ IS DEFEATED BY == >,user\_defeated\_for ((engineer(bob),can\_type(bob)),ucw(bob))]

A relative user defeat of this kind would be appropriate if the user has good, external reasons for believing that, in this particular instance, the fact that bob is an engineer who can type is not sufficient evidence for inferring that ucw(bob). In effect, the user is telling the program to ignore, in the case of bob, this particular supporting evidence, while letting the program make inferences based on other, nondefeated evidence. If the user is really convinced that he knows bob so well that there is no defeasible evidence whatsoever that would convince him that ucw(bob), then the user can do defeatit(ucw(bob)), which defeats the conclusion for all evidence, and can only be overridden by the user doing undefeatit(ucw(bob)). If the user does perform defeatit(ucw(bob)), then howdefeatit(ucw(bob)) will report that ucw(bob) is not true and has been user defeated for \*all\_evidence\*. The query whynot(ucw(bob)) returns a similar report.

It was mentioned above that one may use addit to add a fact to the system if that fact is not currently true in the KB because there is no undefeated supporting evidence for it, as a result of the program's internal rules and data. However, if the fact is not currently true as a result of the use of defeatit, then it has been defeated by the user for all evidence. In such a situation, addit will not permit the user to add in this fact. If the user wants it to be true again, he must first use the undefeatit predicate. This restriction on addit does not apply if the user has only made relative user defeats.

## 5. Discussion of EVID's design

## 5.1. EVID's Logical Interface

Sections 3 and 4 describe how defeasible rules are formulated in an application program and how EVID interprets these rules and provides a user interface to the application program. This description shows many ways in which the current EVID program satisfies the general functional requirements that are specified in Section 2. I will now present more detailed motivation for some of these functional requirements, and then Section 5.2 will give summary descriptions of the main interactive EVID predicates that satisfy the functional requirements.

By “user interface” I am not referring to such things as windows, icons, and menus, but rather to what might be called a logical interface. EVID predicates such as holds, why, whynot, howgetit, and howdefeat give the user information about various logical relationships between evidence, conclusions, and defeating conditions. EVID contains other predicates that provide additional information about possible defeaters and possible evidence, and about all currently true evidence and defeaters in the system, etc. Furthermore, predicates such as addit, removeit, defeatit \_for, and undefeatit \_for permit the user to make interactive changes in the epistemological state of the system while they perform certain logical checks and impose some logical constraints on these interactive changes. Thus, it is appropriate to say that EVID provides a logical interface between the application program and the user.

This logical interface is considerably more complex than the above simple examples indicate. The complexity results largely from the major design decision to give the user “the last word,” subject to the user’s own “self-consistency,” when the user disagrees with either a defeasible conclusion or a defeat of a conclusion inferred from the application program. “Self-consistency” as used here does not merely mean strict logical consistency, but refers more broadly to the avoidance of epistemically irrational actions. Developing a general and rigorous characterization of the latter concept would be a large project, and is not attempted here. However, some relevant remarks are given at the end of this subsection.

In addition, some other constraints are imposed in order to avoid useless redundancies and for the sake of efficiency. The extent of these interface complexities is clear from an examination of the program. For instance, in the current implementation, the specification of the defeatit \_for predicate uses eighteen Prolog clauses, many of which call other complex predicates. I will not attempt to describe the interface in detail, but will instead mention some of its additional, salient features.

One design feature prevents the user from asserting “irrelevant facts”, to which no program rule would apply. Thus, addit does predicate type checking and will not allow the user to add a fact that is neither definite nor defeasible. Also, it will not allow the addition of any fact that is already true in the program, either as a direct assertion or indirectly by inference. This restriction has several advantages, including program efficiency, but its primary motivation is the following: an application program is intended to be a kind of friendly, knowledgeable adviser to the user, with EVID as their interface. The user gives the program some external facts (perhaps about a particular decision problem) that the program does not have, and then the program infers conclusions from these facts for the user's information. These external facts supplied by the user are of two main kinds: facts that the program is unable to infer even without any relevant defeating conditions being true, or conclusions for which the program has only defeated evidence. In either situation, the fact the user wishes to add is not currently true in the program. Hence, there is no need to allow the user to add facts that are already true, and concern for efficiency motivates blocking such additions.

Suppose that the program has defeasibly inferred concl, but the user is convinced that no evidence should be allowed to support this particular conclusion. Then, she can do defeatit(concl) and thereby defeat this conclusion for all possible evidence. As previously mentioned, in such a case addit will not permit her to assert concl back into the current state of the program's KB. Unlike the cases just mentioned, in this one the fact, concl, is not true in the program, but the reason for this is the user's own action of defeating it. Thus, the user believes that there is no possible evidence to support concl, so if she asserted it, she would be asserting something for which she already believes there can be no evidential justification. The addit predicate prevents her from doing this.

The defeatit \_for predicate is 2-ary and needs to check for more potential problems than the addit predicate. Suppose that the user enters defeatit \_for(ev,concl), where ev is a conjunction of one or more atomic formulas. Then concl must be a defeasible atomic sentence, and the entire conjunction ev must be of the appropriate form to be a possible piece of evidence for concl. The latter condition implies that the program must have at least one rule of the proper form relating concl to ev. This requires checking a number of aspects of these formulas. Also, additional checks apply in the special case where ev is \*all\_evidence\*. This case arises automatically in EVID when using the defeatit predicate for absolute user defeats.

Application programs sometimes have rules that lead to a more complicated situation than has previously been mentioned. Suppose that we have an application program that recommends how a person is likely to travel from location A to location B under certain conditions. Such a program might be useful, for instance, in military intelligence contexts. If the travel is over an island, say, there might be options of travel by land (by means of various roads), travel by air, or travel by sea. This program could have a rule that states that a person travels by air on a date if (defeasibly) that person flies something (jet, balloon, etc.) on that date. Let us assume that travels \_by (land, air, sea) and flies are defeasible and occur in other rules. Yet, in this case, the connection between these predicates is assumed to be very strong in the sense that one cannot both fly and not travel by air. We want the user to be able to defeat the program's defeasible conclusions but, because of this strong connection, a defeat of "travels by air" should also imply a defeat of "flies". In abstract form, here is a more extended example of these ideas:

definite(ev(\_)).

defeasible(concl0(\_) ).

```prolog
concl0(X):-  
ev(X),  
not(defeated _for(ev(X), concl0(X))).
```

concl1(X):-  
concl0(X), not (defeated \_for(concl0(X), concl1(X))).

concl2(X):- 
    concl1(X),
    not(defeated\_for(concl1(X),concl2(X))).

concl3(X):-  
concl2(X),  
not(defeated\_for(concl2(X), concl3(X))).

% Contra-defeaters ...
defeated(concl0(X)):- defeated(concl1(X)).
defeated(concl1(X)):- defeated(concl2(X)).
defeated(concl2(X)):- defeated(concl3(X)).

ev(bob).

The last three rules are contra-defeaters, which can hold when the evidence for one defeasible conclusion (e.g., $\text{concl1}(X)$ ) is another defeasible formula (e.g., $\text{concl0}(X)$ ). Note that contra-defeaters are syntactically quite different from the defeater rule forms (12) and (13) in Section 3. In (12) and (13) the defeating conditions, $d_{i}$ , are literals formed from domain predicates or Prolog system predicates, whereas the defeating condition in a contra-defeater has the form defeated(C) for some defeasible conclusion formula C.

Contra-defeaters are used when we want to guarantee that an absolute defeat of a conclusion also leads to an absolute defeat of an evidential formula supporting this conclusion, as in the example of travels by air and flies. There can also be extended chains of contra-defeaters, as the above little program illustrates. If this program is interpreted by EVID, initially concl0(bob), concl1(bob), concl2(bob), concl3(bob) all hold defeasibly. If the user does not accept the last conclusion, she may do defeatit(concl3(bob)), which produces a user defeat of this conclusion for \*all\_evidence\*. In addition, because of the contra-defeater rules, concl0(bob), concl1(bob), concl2(bob) are also defeated. It was explained above that, since concl3(bob) is user defeated, addit will not permit the user to add this conclusion back into the program. But concl0(bob), concl1(bob), concl2(bob) are also defeated for all evidence by the user, indirectly, because of the contra-defeater chain. Thus, addit will also not permit the user to add any of these back into the program's current KB. If the user does addit(concl0(diane)) then, because of the contra-defeater chain, she is similarly not permitted by EVID to apply defeatit to any of the other numbered conclusions that follow from it. As might be guessed, checking for contra-defeater chains is computationally rather expensive but, fortunately, long chains seem to be uncommon in practical applications. Predicates in EVID's logical interface, including addit and defeatit\_for, also check for other situations, but these are more specialized and will not be discussed here.

I believe that user interaction will be very important in many DSS's. There has already been much investigation of nonmonotonic reasoning systems, but little attention has been given to user interaction. Although still somewhat sketchy, I hope that the above description has persuaded the reader that the goal of effective user interaction leads to important and difficult problems regarding the design and implementation of a logical interface. In particular, when the user is permitted to defeat evidential support for conclusions and also add new facts to the program, it becomes difficult to characterize exactly what we should mean by “user self-consistency.” When a number of pragmatic and epistemological issues are considered, such as the complications of contra-defeater chains, this characterization problem becomes even more complex. I indicated near the beginning of this subsection that we should really be interested in trying to prevent the user from performing epistemically irrational actions. This discussion of EVID’s logical interface should throw some light on what this involves, but perhaps some additional emphasis will be helpful.

Obviously, we would not want the user to addit both p and not(p), and EVID certainly prevents this. But recall that in EVID, concl is consistent with defeated\_for(ev, concl) and also with defeated(concl). If all supporting evidence for concl is defeated within the IDRP, the user may still do addit(concl), for the user may still have good reasons for believing that concl is true. But, on any plausible definition of “rational”, it would be irrational for the user to do addit(concl) and then follow this later with defeatit(concl). I would consider this to be an example of an epistemically irrational action, for the user is saying both that he believes the defeasible conclusion concl, and also that he believes that it has been defeated for \*all\_evidence\* in the strongest possible sense. Note that there is a difference between (i) the situation in which all evidence in the IDRP has been defeated by other facts in the IDRP, and (ii) the situation in which concl is user defeated. In case (ii) it is not just KB rules that lead to the defeat, but rather the user’s own authority that provides the defeat.

Now there is no logical contradiction in having both concl and user\_defeated(concl), but I consider this situation to be epistemically irrational. In order to enforce user epistemic rationality, addit will not add a fact that is already user defeated, as was mentioned earlier in this section. Also, if concl is a user added fact, then defeatit will not permit the user to defeat this conclusion. The above discussion of contra-defeaters provides another example of how EVID attempts to prevent epistemically irrational actions by the user. If an IDRP contains a contradefeater chain as previously described, then EVID also constrains the user's application of additions and defeats in a similar, but more general manner.

It is important to appreciate that EVID is a very complex system because it not only applies defeasible reasoning to a KB, but also permits the user to interact in such a way that the user becomes a special type of authority figure that can override some of the IDRP's conclusions. Thus, it is quite difficult to characterize what we should mean by “epistemic rationality” of the user. So far my research on this has been experimental. Clearly, one guiding heuristic principle is this: If concl is defeasible, then the user should not both say that he believes concl and that there is no evidence whatsoever for believing concl. The above constraints on mutual use of addit and defeatit prevent the user from doing this.

However, the general situation is more complex, as illustrated by contra-defeater chains. Here the user is not directly acting irrationally. Instead, assuming that the user accepts the rules of a contra-defeater chain, he might indirectly act irrationally, so EVID prevents this also. I am convinced that this constraint is not ad hoc and is well justified, but it is not clear how far EVID should try to prevent various (and sometimes rare) types of “questionable” user actions that are indirectly mediated through rules in a KB. Also, to what extent should EVID prevent the user from doing merely silly things? For instance, currently, if the user attempts defeatit\_for(ev, concl), but there is no rule in the KB stating that ev is evidence for concl, then the attempted relative defeat is aborted with a message to the user about the lack of an appropriate rule. This check in defeated\_for certainly helps to save memory usage and promotes later program efficiency. Yet, its epistemic status is perhaps arguable. At least this much can be said: although the user is an “authority” with special powers over an IDRP, the user is constrained to work within the KB of rules in the IDRP. In this working context, we might not want to say that it is “irrational” for the user to defeat for data that is not possible evidence for a conclusion (according to KB). Yet, we can say that it is “arational”, and have EVID block such actions for this reason.

In the design of EVID I have been guided by experimental testing of a number of different types of logical problems and application programs (see Section 7). EVID does work well with many applications, but it will undergo further development. Clearly, the interactive nature of EVID, as specified in its functional requirements, raises many interesting questions for further research. In particular, perhaps some general criteria for an appropriate sense of “epistemic rationality” can be developed. Such criteria would be theoretically illuminating, although their practical applicability will be limited by implementation issues.

## 5.2. Summary of some important EVID predicates

As previously mentioned, EVID currently has about 90 predicates. Most of these are primarily for internal use by EVID, or for the knowledge engineer to use in debugging rules during construction of the KB of an IDRP. Although some of these “internal” predicates could occasionally be helpful in supplying special information to the (end) user of a DSS, normally such a user will use only about twenty EVID predicates in interactions with an IDRP. Most of these predicates have been introduced in particular examples earlier in this article. At this point, I will give summary descriptions of the main interactive predicates in order to provide a more general overview of how EVID-based DSS’s can be used. These summary descriptions only mention the primary function performed by the predicate being described. Most of these predicates have complex characterizations using many Prolog clauses. Many of these clauses are used to trap for inappropriate user actions, such as trying to add an assertion that is not stated using the IDRP’s declared domain predicates. Such error traps block the action and return an informative message to the user. In general, the following summaries omit such details. Also, I use the Prolog convention of writing an n-ary pred in the form pred/n, when it is desired to show the arity. The predicates are listed in a functional order, rather than alphabetically. Numbers in parentheses refer to the Functional Requirements in Subsections 2.2.1–2.2.8. These numbers will help to relate a given predicate to the descriptions of functional requirements, or to other remarks made in these descriptions. However, in general there is not a one-to-one relationship between particular predicates and particular functional requirements.

definite /1 and defeasible /1: these are used by the knowledge engineer to declare the application domain predicates. Where S is a variable, the user can do definite(S) or defeasible(S) to find all definite or defeasible domain predicates. S can also be a particular atomic sentence.

predtype/2: predtype(S,T) returns every predicate S (including EVID predicates) with its type T. If S is not a variable, it must be a particular predicate name.

holds /2: If How is a variable and sent is instantiated as some particular sentence, then holds(How,sent) returns the value of How that says how the sentence holds. If sent is definite, there are three possibilities: Normally with a defeasible ancestor premise, when there is at least one derivation with a defeasible ancestor or the negation of one; normally with a negative ancestor premise, when the previous case does not hold, but there is at least one negation by failure proof; or positively, when sent is true, but neither of the previous cases obtain. All of these cases are considered nondefeasible truths in the system (since they are not subject to user defeats), but it can be helpful to the user to have the detailed information described. If sent is defeasible and true, then How always has the value defeasibly. (2.2.1)

addit /1: The EVID user is not supposed to use Prolog's built in assertion predicates, but rather addit. If sent is an “allowable” atomic sentence, addit(sent) will assert sent as a new fact in the IDRP. What is “allowable” involves many error checks. One of the most important is that sent must not be a defeasible conclusion of the IDRP which has been directly defeated by the user (see defeatit /1). (2.2.1, 2.2.8)

user \_added / 1: If addit(sent) succeeds, then user \_added(sent) is true. If S is a variable, user \_added(S) returns all user added sentences currently true in the system.

removeit/1: The EVID user is not supposed to use Prolog's retract. Instead, removeit(sent) can be used to retract a user added sentence. (2.2.1, 2.2.8)

why/1: If sent is a true domain sentence, why(sent) tells how the sentence holds, lists all currently undefeated supporting evidence, and (if any) all currently defeated true “supporting” evidence. Supporting evidence typically consists of other facts in the system used in derivations of sent. In special cases sent may be a user added fact or a fact in the KB, and why so indicates, in lieu of supporting evidence. An example of the former is near the beginning of Section 4. (2.2.2)

whynot / 1: A sentence, sent, can fail to be true in two ways: (i) there is not sufficient evidence in the KB to imply it or (ii) there is supporting evidence, but all such evidence has been defeated by one or more means. In case (i) whynot(sent) reports that there is no supporting evidence. In case (ii) it lists all of the defeated supporting evidence with the corresponding defeaters (including user defeats, if any). (2.2.3)

proveit / 1: If sent is true, proveit(sent) returns a detailed trace of a proof of sent. This trace is rather inelegant, and is mainly used by the knowledge engineer as an aid in rule debugging. The user of an EVID DSS would only need proveit rarely, since why is usually more helpful. (2.2.4)

howgetit / 1: If sent is a domain sentence, howgetit(sent) says whether or not sent is true, and then lists all possible directly supporting evidence for sent, i.e., howgetit only looks as far as the body of rules with sent as the head. In the case of (10) for instance, it returns the evi in the body of the rule. It performs the corresponding operation on nondefeasible rules. Thus, howgetit does not attempt an exhaustive search throughout all possible ancestor premises of sent. This would be computationally expensive, and also would probably not be very helpful for the user, who can manually recurse with howgetit if desired. In cases where there already is defeated supporting evidence in the program, howgetit also reports this information, which can be helpful to the user. Finally, an IDRP may occasionally use rules with the cut-fail combination as part of the “supporting evidence” in order to guarantee the failure (denial) of a goal. If such rules exist, howgetit also returns their denying “evidence”. (2.2.5)

howdefeatit/1: This predicate was illustrated several times in Section 4. Its primary function is as follows. If sent holds defeasibly, then howdefeatit lists all possible absolute defeaters. In addition, for any currently true supporting evidence that is not defeated by the firing of defeater rules, it lists the corresponding possible relative defeaters. Finally, it lists all currently true, but defeated evidence, along with the correlative defeaters. If sent is defeasible, has some true supporting evidence, but all such supporting evidence for it is currently defeated, then howdefeatit reports that sent is not true and lists all of the currently defeated evidence along with the correlative defeaters. In cases of absolute defeats, the supporting evidence is named \*all\_evidence\*. If sent is true and user added, howdefeatit reports this and says that the sentence should just be removed. The howdefeatit predicate also checks for many other special situations regarding sent and returns useful information, but these details will not be described here. (2.2.6)

defeatit \_for/2: Like howdefeatit, this predicate also checks for many special situations and returns special reports. It is perhaps the most complicated predicate in EVID because of its numerous error traps and other features designed to help implement EVID's logical interface. Its primary function is as follows. Evidence is defeatable \_for/2 a conclusion if there is a defeasible rule formulated in terms of this evidence and conclusion. Suppose that concl holds defeasibly and that defeatable \_for(ev,concl), where ev may be a conjunction of supporting literals, and is true. Then the user may do defeatit \_for(ev,concl), which accomplishes a user relative defeat of this particular evidential relationship. Since this is a relative defeat, other evidential relationships are not affected. Note that one may not do a repeated defeatit \_for(ev,concl) if this has already been accomplished. There are many other constraints on the operation of this predicate. (2.2.7)

user\_defeated\_for / 2: user\_defeated\_for(ev, concl) is true after a successful application of defeatit\_for(ev, concl).

undefeatit \_for /2: This undoes, and is the only way to undo, a user relative defeat accomplished by defeatit \_for. (2.2.8)

defeatit / 1: If the user does defeatit(concl), this calls defeatit\_for(\*all\_evidence\*',concl). If the latter is successful, the program acquires user\_defeated\_for(\*all\_evidence\*',concl). The defeatit prdicate will not defeat a fact that the user has added (see addit / 1). Other restrictions also apply to user defeats. There is also an undefeatit / 1 with behavior similar to that of undefeatit\_for / 2. (2.2.7, 2.2.8)

defeated\_for / 2: defeated\_for(ev,concl) holds whenever EVID can deduce it. This typically happens as the result of the firing of relative defeater rules. It also follows from user\_defeated\_for(ev,concl) by an internal EVID rule. By another EVID rule, defeated\_for(\_,concl) follows from defeated(concl) (see below). Thus, if a conclusion is absolutely defeated, then it is relatively defeated for any evidence whatsoever. Defeated\_for / 2 is the more general predicate, and defeated / 1 implies defeated\_for, for all possible evidence (except user additions).

defeated / 1: defeated(concl) is true whenever EVID can deduce it. This typically happens as the result of the firing of an absolute defeater rule. It also follows from user\_defeated\_for 用户\_all\_evidence\*',concl), which results from a user defeat.

The above predicates are those most often used in interactive runs of EVID DSS's. There are others that are occasionally helpful to the user. For instance, current \_defeaters(Concl, Ev, Defeater), where Concl, Ev, Defeater are variables, returns all triples <Concl, Ev, Defeater> in which true supporting evidence, Ev for Concl, is currently defeated by Defeater. It would not be appropriate to go into further details about EVID predicates here, but the above list should provide a fair understanding of how the user interacts with an EVID-based IDRP.

## 6. Some Comparisons

Although I want to avoid extended comparative discussions, a few points are worth noting here. First of all, as far as I know, no previous theoretical discussion or practical implementation of any nonmonotonic reasoning system has included any detailed investigation of the logical interface requirements for safe and effective user interactions. From the perspective of pure, logical investigations, perhaps the interface is not so important. Yet, it must play a prominent role in any practical, interactive defeasible reasoning system, including Decision Support Systems. The EVID program appears to embody the first serious attempt to characterize and implement a suitable logical interface for such systems.

Another feature of EVID that seems to be unique is the requirement that all application predicates be typed as either definite or defeasible, and that definite and defeasible rules have syntactic forms associated with these typings. This “strong typing” is based on the epistemological roles of the predicates, not on features that would typically be used for data typing in a programming language. EVID’s typing requirements impose constraints on the form of knowledge representation used in an EVID-style application program. Yet, I do not believe that these constraints are oppressive, and it could be argued that they encourage the knowledge engineer to practice careful thinking in the design of knowledge based systems. The typing requirements certainly require one to consider carefully which kinds of KB facts should be treated as “epistemologically basic” and which should be “defeasibly inferred”. Yet, I suspect that EVID typings will be considered unimportant by some researchers; it would be an interesting project to attempt to emulate EVID’s functionality without these typings.

If one reviews the literature on nonmonotonic reasoning, e.g., in [4], one finds many attempts to develop theoretical systems of nonmonotonic logic, which are usually extensions of the first-order predicate calculus. Aside from the internal problems with such systems, they are very difficult (if not impossible) to implement with any satisfactory degree of efficiency. Indeed, Ginsberg writes ([4], p. 11), “...implementations of nonmonotonic reasoning systems (and there are very few) tend to be excruciatingly slow because of the repeated need for consistency checking.” The approach taken with EVID is modest; rather than attempt to implement an entire first-order system, EVID merely interprets and interacts with a normal Prolog program which uses some metapredicates. Of course, an EVID-based application program uses negation by failure, most often together with defeated-for and defeated, but Prolog can efficiently handle queries of such predicates.

One of the best known systems of nonmonotonic reasoning is Reiter's default logic; see [12] (reprinted in [4], to which the following page references apply). Reiter's system augments first-order predicate calculus with so-called "default rules" of inference, so it is an extension of a full standard logic. A default inference involves assuming a proposition “...in the absence of any information to the contrary...” (p. 68). There are several forms of default rules, but a very simple example is this (restated from the one Reiter has on p. 68): ‘If bird(X) and it is consistent to assume that flies(X), then infer flies(X).' As Reiter points out (p. 69), it is difficult to provide a suitable formal characterization of this consistency requirement, and he devotes much effort to doing so. An obvious inconsistency can result from ‘penguin(X) → ¬ flies(X)’, where ¬ is the standard “classical”, first-order logic negation. Now, regardless of the formal characterization details, inconsistency in a Reiter system always seems to depend on the use of ¬, so any defeater must be absolute in an even stronger form than is given by EVID's defeated predicate. Furthermore, there does not seem to be any simple way of expressing relative defeats in a Reiter system. If a program has more than one default rule for concl, and one of these rules is defeated, then the inference is blocked from all of them. In my judgment Reiter's default logic suffers from a fundamental conceptual error of interpreting “absence of contrary information” in terms of logical consistency requirements on the sentences of a theory. It appears that defeasible reasoning cannot be adequately explicated in terms of simple consistency requirements, and the design of EVID avoids this particular error.

If the above is a correct interpretation of Reiter's default logic, then that system will be severely limited in its ability to provide convenient treatment of relative defeaters. The simple example program using ucw should demonstrate the importance of representing multiple kinds of evidential conditions and relative defeaters for these. Another system that has similar difficulties is "d-Prolog", described in [7]. Since its syntax is somewhat different from that used by EVID, it is not immediately clear how best to formulate the ucw example in d-Prolog. Yet, there is no direct way to express relative defeater rules in it, and trying to follow the standard d-Prolog program styles always leads to rule systems which contain only absolute defeaters. Hence, if ucw(bob) follows defeasibly from two sets of evidence, and only one of them is defeated, then the program behaves as if they both were.

As mentioned in Section 1, Pollock has previously distinguished “rebutting” from “undercutting" defeaters. In [9], p. 37, without going into details, he generally criticizes the A.I. literature on nonmonotonic reasoning for not making this distinction. Although Pollock's work is related to mine, I will not attempt a highly detailed comparison, since I do not have enough information about the implementation details of Pollock's system. It does appear from [10] that his system (if implemented as described) would have a much more complex logic than an EVID system. Pollock's definition of "undercutting defeater" relies on a conditional that he states ([10], p. 485) as "P wouldn't be true unless Q were true.". He says this is not a material conditional, but does not commit himself to a particular analysis of it. It certainly seems to rely on some logical conceptions that go beyond those used in EVID.

In addition, a Pollock “rebutting defeater”, R, for Q, is a reason for believing $\neg Q$ . This seems stronger than an EVID absolute defeat. In an EVID IDRP, if concl has been absolutely defeated by means of facts and a KB defeater rule, then the IDRP cannot infer concl. Thus, one might say that there is no reason in the KB to believe concl. But this is not as strong as saying that there is a reason for believing $\neg$ concl. In fact, the user can still add concl if she (or he) thinks that this is justified. Moreover, as shown in Section 5.2, an EVID absolute defeat is a relative defeat for all possible evidence (except user additions). It does not appear that there is an analogous relationship between Pollock’s rebutting defeaters and his undercutting defeaters. Thus, Pollock’s rebutting defeaters do not appear to be equivalent to EVID’s absolute defeaters.

Finally, [9], p. 39, says that “defeaters” (defeating conditions) may be prima facie reasons for other propositions such as $\neg Q$ or the denial of “P would not be true unless Q were true”. Thus his defeaters may be defeated by other “defeater defeaters”, etc., and he is led into some complicated discussions about ultimately undefeated arguments. I am not sure exactly how to compare all of this with EVID, but at least the following should be noted. The defeating conditions, $d_{1}$ , in (12) and (13) may themselves be defeasible. Thus, if concl is defeated by some defeating condition, say $d_{1}$ , and this condition is itself defeasible, then it may be defeated by some further defeating condition, say $d_{2}$ . One could say that $d_{2}$ is an EVID “defeater defeater”, but I would prefer not to introduce such terminology because it might be misunderstood. The important point to note is that whether or not concl will be inferable in an IDRP will, in general, depend on a set of interacting defeasible and nondefeasible rules, together with defeater rules.

One system that appears capable of handling relative defeats is described in [2]. Brewka's approach uses some aspects of Reiter's work and also of some earlier modal logic nonmonotonic systems. The basic idea is to state default rules and to name these rules, e.g., $r_{1}$ , $r_{2}$ , etc. The rules are formulated as sentences, rather than as rules of inference. Brewka introduces a metapredicate, appl, such that $appl(r_{1}, X)$ means that the rule $r_{1}$ applies to the object X. (Actually, there must be several such predicates of different arities corresponding to the number of free variables in the rule.) Finally, in addition to default rules (stated as sentences), Brewka uses “exceptions” such as ‘penguin(X) → ¬ appl(r₁, X)’, where $r_{1}$ might be the default rule that says that birds fly. This work was motivated by a concern for handling interacting defaults, and Brewka does not explicitly discuss evidential support and blocks of such support. Instead, his approach is to block the application of a rule. However, it would appear that this system could handle relative defeats. $^{6}$ A recently developed system that also “names” default rules with special predicates is described in [11]. This program (like Brewka's) allows explicit blocking of an application of a default rule by a (named) reference to that rule. The manner of naming rules and its use in deductive procedures is unusual, but does yield considerable flexibility. It is difficult to see a natural, intuitive interpretation for the special predicates that are introduced to name or refer to the default rules.

Many other comparisons can be made, but most of them pertain to specific problems and issues. Also, in this article I will avoid any detailed comparisons with Circumscription approaches. At present there are a number of different theoretical approaches to Circumscription, see $[4]$ and $[3]$ , but few implementations. It is difficult to know where to begin a systematic comparison. However, one point is worth noting. In the Circumscription literature, a special predicate, ab (or abnormal) is usually employed in the representation of “common sense reasoning”. In [6], reprinted in [4], this 1-ary predicate is applied to various “aspects” of things. For instance, the following might be a rule about birds, with respect to some special aspect, say, aspect2: if bird(X) and not ab(aspect2(X)), then flies(X). Also, assume that there are rules which say that ostriches and penguins are abnormal with respect to aspect2. McCarthy shows how Circumscription can be used to handle some types of default reasoning using his ab and a large variety of special “aspects”. Yet, even McCarthy admits that “The aspects themselves are abstract entities, and their unintuitiveness is somewhat a blemish on the theory” (p. 155 in the Ginsberg anthology, [4]).

The basic problem, it seems to me, is that McCarthy's approach uses ad hoc "aspects" together with the 1-ary ab, whereas what is really needed is a way to represent relationships between evidence and defeasible conclusions. The latter is exactly what the 2-ary defeated \_for predicate does. For instance, one should view bird as evidence for flies, but evidence that can be defeated by certain other conditions, such as penguin. In contrast, using ab together with aspects is awkward and seems to distract one from seeing the fundamental structure of the defeasible, common sense reasoning. It is also more limited in representational power since ab is only 1-ary. Among other things, this prevents us from having any simple, straightforward way to state rules corresponding to EVID's absolute defeater rules. I am currently studying these comparisons in more detail, but it would be premature to say more about this at this time.

To be fair, it should be pointed out that a prime motivation of many investigators has been to develop systems that automatically infer certain kinds of defeasible conclusions in situations where it would appear that the KB has conflicting conclusions. The conflicts often arise because of the use of $\neg$ . For example, suppose that we have the rules: 'flies(X) if(defeasibly) bird(X)', ' $\neg$ flies(X) if(defeasibly) penguin(X)', and 'bird(X) if penguin(X)'. If penguin(peggy), what should be inferred about her flying ability? One reasonable approach, which has a long history in scientific methodology, is to use the most specific information available, namely, that peggy is a penguin, and to infer that she does not fly. The d-Prolog system of [7] is one that uses such an approach. Internally, the program compares degrees of specificity of predicates in order to decide which of the competing rules to use.

EVID could perhaps be augmented with specificity comparison mechanisms, and they might be useful in some applications. Fortunately, however, such comparisons will often not be required because they will be an automatic result of EVID-style knowledge representations. To see this, note that the above example would be represented in EVID by the following rules:

flies(X):-

bird(X),

not(defeated \_for(bird(X), flies(X))).

defeated \_for(bird(X), flies(X)):-

bird(X),

penguin(X).

bird(X):-

penguin(X).

In these rules, bird and penguin are definite, and flies is defeasible. Although this representation does not mean precisely the same as the preceding, it automatically keeps penguins from flying, and it is useful for applications. Moreover, in EVID if penguin(peggy), then whynot(flies (peggy)) explains that the evidential support bird (peggy) is relatively defeated by penguin(peggy). $^{7}$

## 7. Intended applications

## 7.1. Inheritance hierarchies

The literature on nonmonotonic reasoning contains a number of standard test cases for reasoning systems. These cases consist of small puzzle-like problems to check whether a program draws the allegedly correct defeasible inferences from specified assumptions. EVID-style programs have been written for all of the major types of standard test cases. When these examples are translated into appropriate representations for EVID, the behavior of the programs is very reasonable. These little programs will not be described here because it is more interesting to consider some possible practical applications.

Another kind of standard test is to build a KB which has a hierarchical arrangement of many “classes” of things, say, species of animals. Subclasses are to inherit properties of their superclasses, but this inheritance is usually defeasible, in the sense that an inherited property can be overridden by a more specific property of the subclass. For instance, most kinds of birds will inherit “can fly” from the general class of birds, but this inheritance will be blocked for penguins, ostriches, and some others. A hierarchy of this kind may, in addition to classes, have nodes that represent individuals, such as Leo, a particular lion. Finally, it is possible that a given class or individual may have more than one superclass, giving rise to the possibility of a conflict over which superclass should transmit the value of a particular inheritable property. This is sometimes called “the problem of multiple inheritance.”

An inheritance hierarchy with all of the above features has been implemented as an EVID application program. The basic approach is straightforward, although the details can be tedious to program. Inheritance from a superclass is handled by letting membership in the superclass serve as evidence (usually defeasible) for the inherited property. This representation requires no special treatment to obtain multiple inheritance, one merely writes two or more such inheritance rules. Inheritance conflicts are obvious because a query for the value of the inherited property will yield more than one answer. It is then the responsibility of the knowledge engineer to write suitable defeated \_for rules to block the inheritance of the inappropriate answers. This form of representation can lead to many rules, so programs of this type will not be as efficient as those using a directly procedural approach (such as semantic nets and frame systems). On the other hand, an inheritance hierarchy interpreted by EVID offers many additional features, including explanations and explicit user overrides by means of addit, defeatit \_for, etc. Also, special forms of rules permit the knowledge engineer to represent different ways in which an individual may be an exception to a default rule. Overall, EVID programs offer extensive representational flexibility.

Inheritance hierarchies are interesting, but I do not consider them, per se, to be application programs. Rather, they are a convenient knowledge representation for possible applications. Suffice it to say that EVID can handle such hierarchical representations when needed, although large programs may (as always) run into computational efficiency problems. In the remainder of this section, I will briefly describe two small experimental application programs that have been successfully run in the EVID environment. These examples are selected because they demonstrate two general types of applications for which EVID may be especially useful. The first type can very roughly be described as user directed because the user specifies the kinds of conclusions that interest him, and he enters data appropriate to obtaining these conclusions or at least some inferences relevant to them. The second type is program directed because the program is designed to seek a certain kind of conclusion goal and it queries the user for information leading to this goal. Well known expert system programs for classification and diagnosis fall into this second category.

## 7.2. A user directed application

The first example program is a fictional military intelligence adviser. EVID was originally designed specifically in order to implement this kind of intelligence adviser, which in turn is a model for many types of DSS's. Suppose there is a primitive mountainous island and a spy is expected to travel from point A on one side to point B on the other side. The application program's KB comprises many rules, both definite and defeasible, about possible modes of travel from A to B depending on the traveler, weather conditions, and other factors. To use the program, we enter various current facts, and then it advises us about how the spy is expected to travel. Naturally, this advice is based on defeasible inferences that the program makes and these inferences may change with new information. This program continues to grow in size as new and more complex rules are added to it. I will only give an informal description of some of its features, but will try to convey an accurate impression of its functionality.

There are only three general ways the spy can travel from A to B; these are specified by travels \_by(Person,X,Date), where X can take the values land, air, or sea. The only way to travel by land is to take one of three roads: highroad, lowroad, or midroad, expressed by takes(Person,X,Date) in which X is the road. The only way he can travel by air is to fly something, specified by: flies(Person,X,Date), where X can have many values such as single \_prop, jet, balloon, etc. Finally, it is assumed that the only way he can travel by sea is if he rides a boat, rides(Person,boat,Date). These four predicates are the only defeasible predicates in the program, which also has about a dozen definite predicates pertaining to such things as weather conditions, what types of air craft the spy can fly, whether or not he has tire chains, is acrophobic, gets seasick, etc. There is also a predicate that specifies that he prefers some modes of travel over others, and a predicate that specifies that certain information about him is uncertain (i.e., based on questionable intelligence sources). $^{8}$ The program currently has 24 rules. Of these, two are definite, and nine are defeasible rules, while thirteen are defeaters (including three contra-defeaters).

We begin a dialogue with the program by telling it, say, that travels(spy,oct31), where spy is a generic name for an unidentified spy. If this is all that it is given (other than the fact that spy is a person), then it defeasibly infers that he takes the highroad. If we then tell it that there is mountain snow on October 31, it infers that he takes the lowroad. But if we also tell it that he has tire chains, then he takes the highroad in spite of snow. There are other conditions that defeat his taking the highroad. Suppose that the program infers that he takes the lowroad, and then we give the program new information that there is a coastal storm, then it will infer that he takes the midroad. At any point, we can use howgetit and howdefeatit to help us decide what additional, external information would be relevant to different conclusions. Also, why and whynot yield the program's reasons for currently inferring or not inferring certain conclusions.

Now suppose that the user is an experienced intelligence officer. Such a person may notice a special nuance of the situation that is not covered by the program's KB. For example, this could be some peculiarity of the sea's condition, or some particular information about who the spy is and what his dispositions are, etc. A detailed, reliable KB is very difficult to construct, and an experienced human expert, working in a real world context, will almost always be able to draw defeasible inferences, and make defeats of such inferences, in ways that go beyond the capabilities of an automated system. The automated system can be very helpful, but it should only be treated as a smart, friendly adviser. EVID gives the user the "last word" subject to the constraints of its logical interface. Thus, if the program has defeated a certain conclusion, the user can override this and add that fact back into the system. If the program has drawn a conclusion, the user can defeat it, again subject to the constraints of EVID's logical interface. A wise user will only perform such actions with great care. Whether he ultimately agrees with the program, or overrides it in some respects, he will have responsibility for the decisions that are made.

To take a specific example, suppose that the user has information that the spy in question is bob and this user knows that bob prefers flying over taking any road. Also, suppose that there is mountain snow, and that bob can fly a single prop plane. When all this information is entered, one might expect the program to infer that bob flies, but this is not the case because of a rule that has mountain snow defeating the flying of a single prop, so bob rides a boat and travels by sea. If we subsequently get and enter new information that bob has had new training and can now fly a jet, then the program infers that he flies it and that he travels by air. Finally, suppose that the user also knows that bob has reason to believe that the user knows about bob's new training, so bob is likely to expect anti-air travel preparations from the user. Thus, the user concludes that, at least in these special conditions that go beyond the program's KB, bob will avoid air travel after all. Then the user can use defeatit to overrule the air travel, and the program will conclude that bob rides a boat.

The current implementation of this test program uses a standard command line interface, but this program is part of a larger project to investigate possible designs for logical spreadsheets. Several possibilities suggest themselves, but here is one sketch that easily comes to mind. In a typical application, there will be a set of data that is externally obtained and supplied to the program. This data will usually be expressed in terms of definite predicates, such as the ones mentioned above. There will also be other facts that the program infers, either positively or defeasibly, from the input data and its KB. One could set up a kind of tabular spreadsheet, with cells (or windows) for the input data, and other cells for displaying the output conclusions. Some user actions, like defeatit, could be performed with the help of menu selections. As new information is fed into the spreadsheet, it would be updated to show how the program's inferences change. A separate window would be useful for display of the program's "explanations" (responses to why, etc.). A spreadsheet of this sort would be convenient for answering logical "what if" questions.

## 7.3. A program directed application

There is no standardized definition for “expert system,” but typical examples of such systems help to solve diagnosis and classification problems. In fact, many diagnostic expert systems do little more than classification: they have a KB that includes a classification of different types of functional abnormalities (diseases, breakdowns, poor performance, etc.). The classification system is largely based on observational data (symptoms, laboratory test results, case histories, etc.). The expert system includes a large number of heuristic rules that lead from entered observational data towards the formulation of classification hypotheses. Because of the classificational nature of such programs, it is common to write experimental prototypes for the identification of an animal specimen's species in terms of the observed data about the specimen. Such a program typically includes an interface that prompts the user to enter certain observational data in response to the program's questioning. This data then fires internal rules that lead to partial identifications and to additional questioning. When successful, this process eventually leads to a few (often one) identificatory hypotheses which are sometimes associated with probabilities or certainty factors.

One of the commonly heard complaints about such programs is that they are not sufficiently flexible to satisfy a well-informed user. For instance, often the user can justifiably exclude many possibilities himself, but the program will nevertheless question him with many tedious and seemingly useless questions pertaining to these possibilities. In other words, many expert systems follow a fairly standard pattern of questioning and do not let the user “guide” the system more quickly towards the desired goal. Also, typical expert systems do not use defeasible reasoning, at least not in a fashion that is guided by an overall conception of what the role of such reasoning should be in an expert system. It would seem that effective use of defeasible reasoning could lead to more flexible and efficient expert systems.

EVID was not originally designed for building expert systems, but I have been experimenting with a simple animal classification system that runs in EVID. There are two general motivations for these experiments: (i) to study how defeasible rules can be used in the system to increase its flexibility and efficiency, and (ii) to give the user the full benefits of EVID's logical interface, in particular, so that he will be able to use addit to enter information directly and thus avoid having the program ask him questions to elicit this information or questions about conclusions that follow from it (usually defeasibly). My experimental expert system has four main parts:

\- The EVID shell (used without any modifications)

\- The expert system's control mechanisms for querying the user

\- The defeasible domain rules for generating classificatory hypotheses

\- Other domain rules for making internal defeasible inferences

When achieved, the final identifications are in terms of specific animal kinds such as tiger, bald eagle, platypus, etc. Intermediate classifications include larger categories such as mammal, bird, carnivore, etc. The rules for generating hypotheses are fairly standard in one way – they use entered data to infer intermediate kinds (like mammal), and then use additional, more specific entered data to move towards a final goal (like tiger). Yet, these rules are unusual in that they are defeasible, and hence their conclusions are subject to both user defeats and defeats by program defeater rules.

As indicated in the above list, the program uses another set of rules for making internal defeasible inferences. These are similar to the rules one would expect in an inheritance hierarchy. For example, described in a simplified form, there are rules that say that the property of reproducing by live birth applies to an animal if there is direct information that it is a mammal. But this defeasible inference about the reproduction method is relatively defeated if there is other substantial evidence that the animal in question is a platypus. As one might expect, it takes great care to formulate the defeasible rules in such a way that they work correctly. My experimental program uses a limited set of rules that apply primarily to warm-blooded animals, and these rules are not highly accurate from the perspective of biology. Yet, they work fairly well, with very interesting results.

My experimental expert system has two operational modes: a query mode and a discuss mode. When in the query mode, the program asks the user questions about properties of the subject or thing to be identified, just as any standard expert system would do. However, in addition to answering such questions with values of attributes, the user can respond to any of these questions by entering discuss, and then the program moves into the (user directed) discuss mode. The discuss mode uses the standard EVID interface to allow the user to interact with the expert system's rules and the current data in the program. The user can add facts and defeat conclusions just as in the traveling-spy program previously described. He can also ask for help with howgetit and howdefeatit, and get explanations in the usual ways. When in the discuss mode the user can, at any time, choose to return to the query mode. If an identification succeeds, the program automatically returns to the discuss mode, where the user can ask for explanations, defeat conclusions, or revise his previous inputs as desired.

This type of expert system is very flexible. One especially useful feature is this: while in the discuss mode (which is where the program starts), the user can enter any relevant information that he remembers is available to him. For instance, if he already knows that his specimen is a mammal, he can enter this information. The program has an internal rule that says that, defeasibly, a mammal reproduces by live birth (rather than by hatched eggs, as do birds). Now, if the program does not already know whether the specimen is a mammal or bird, it would (in the query mode) ask for the method of reproduction. However, if the user has already added the data that the specimen is a mammal, this question is skipped initially because the program defeasibly infers the information that it reproduces by live birth. If additional answers to the program's questions lead to an identification, this is all that is required and the process comes to a relatively fast end. If additional answers do not yield a solution, eventually the program checks for the possibility of a platypus (which is a mammal that reproduces by hatched eggs). If the user gives the appropriate answers to the program's questions, the previous defeasible conclusion of reproduction by live birth is defeated, and the animal can be identified as a platypus.

It can be seen that several things are going on here. First, the user can add information during the discuss mode. The program is then able to make defeasible inferences from this information. Such additions then greatly reduce the number of questions the program asks of the user. Yet, if the program cannot achieve its goal, it will eventually ask the user questions relevant to the defeat of some of its previous defeasible conclusions. At this point, some of the previously skipped questions may be asked. All of this is handled through the combination of the EVID logical interface together with the expert system's control mechanisms for querying the user. At the present time, this program is still very experimental. Its operations are very complex and not as efficient as I would like, but it demonstrates an interesting and potentially useful type of application of the EVID defeasible reasoning system.

## 8. Concluding remarks and acknowledgments

8.1. The key idea in the defeasible reasoning machinery of EVID is the use of the defeated \_for metapredicate. This predicate is used in the characterization of defeated, defeatit \_for, and others, and it is used in the formulation of defeasible rules, relative and absolute defeater rules, and contra-defeater rules (indirectly, through defeated). All of the defeasible reasoning is done in standard Prolog, although some essential conceptual relationships between important metapredicates are implemented within the EVID shell. The key idea in the logical interface of EVID is to allow the user to “have the last word,” as previously described. This feature makes the interface very powerful, and also is responsible for most of its design and implementation complexities.

In recent years a number of approaches to defeasible reasoning have been proposed or developed, but there is not yet any consensus regarding what should be the adequacy requirements for a defeasible reasoning system. Some investigators present new logical formalizations for default, defeasible, or more general non-monotonic logics. Others develop implementations of reasoning systems; EVID is an example of this approach. Persons working on the formal approaches tend to focus on standard logical questions such as soundness and completeness. As previously mentioned, [5] discusses some of the fundamental difficulties with these formal approaches. Perhaps some of these formal issues will be clarified in the future.

Besides the issues about formalizations, there are other important questions about the nature of practical defeasible reasoning and how it can be represented in a computational logic system. Unfortunately, much of the current literature, both formalistic and computational, is guided by a body of simple and eclectic examples about birds, penguins, etc. These test cases are useful, but I do not believe that they provide very good understanding of the typical uses of defeasible reasoning in practical contexts. EVID's design was motivated by the types of Decision Support Systems described in the previous section, including the user interaction functional requirements described in Section 2. Let us briefly review some of the features that an EVID-based IDRP does and does not have.

Recall that EVID does not use the standard, classical negation ( $\neg$ ), but only negation by failure. All of the defeasible conclusions inferred in such an IDRP are positive atomic sentences formulated in terms of domain predicates. Thus, the IDRP cannot infer new defeasible rules. Of course, the IDRP will also have other limitations of knowledge representations in Prolog. Although such limitations are considerable, much can still be accomplished with clever use of Prolog; see [13] for an extended discussion.

In order to adhere to standard conventions about formalizations, most formal approaches to defeasible reasoning would include classical negation, as well as derivations of new defeasible rules from previous assumptions. If one is implementing a “complete” defeasible reasoning theorem prover, perhaps such features should be included, to the extent (if any) that they can, while maintaining consistency and adequate defeasible reasoning representations. Yet, are such features really required for most practical applications of defeasible reasoning? I believe they are not, at least not for most DSS’s.

Default reasoning began to receive serious attention in the Artificial Intelligence literature around the middle 1970's. At that time, this attention was focused on the inheritance of properties from “prototype classes” in semantic networks and frame representation systems. In these systems, property inheritance is implemented by a procedural search of the hierarchical network, which emulates the deduction of simple default properties. The search procedure also allows for “exceptional cases”, in which the default property does not apply. This “prototype plus exception model” only permits rather simple types of situations to be represented. It was elaborated to permit “multiple inheritance”, but such elaborations lead to increasingly complex specifications of the search procedures to be used. Some of these complications are discussed in [14]. Although the “prototype plus exception model” is useful for rather simple classification hierarchies, it is clearly too limited to serve as a general system for representing defeasible reasoning.

EVID uses a model of defeasible reasoning based on the ideas of prima facie evidence plus defeating conditions. “Prototype plus exception” representations are a simple special case of EVID’s more general conceptual framework, and we would certainly require that any adequate defeasible reasoning system be able to handle such special cases. What more should be required of the defeasible reasoning capabilities of a DSS? I do not believe that it is necessary, or even desirable, for such a system to infer new rules from those already programmed by the knowledge engineer. The knowledge engineer might occasionally find such capability to be of use, but the user of an IDRP should only be interested in the program’s advice and explanations based on the explicit KB rules plus current data. It might still be argued that there is a need for classical negation, and some defeasible reasoning systems include this. However, the presence of classical negation will greatly increase the likelihood of self contradiction in a highly interactive system that permits extensive user defeats and user additions. The fact that EVID only uses negation by failure actually helped in the task of implementing its logical interface.

Aside from implementation issues, what does the user of an IDRP need? Basically, the user needs to know what new positive atomic sentences follow from the data that has been entered into the system, why certain sentences either hold or not, how they hold, how they can be defeated, etc. I assume that the user understands negation by failure, so that he will also understand that a “no” response by the IDRP indicates either the total lack of evidence, or at least the lack of undefeated supporting evidence. It seems to me that this type of negation should be adequate for most DSS applications. I cannot prove these opinions, but I hope that they will at least lead to serious discussion and further investigation of these issues.

8.2. EVID Version 0.9 is still undergoing further development and testing. This current version exists in two slightly different variants, one for the Arity $^{TM}$ Prolog Interpreter (5.1) and one for Quintus $^{TM}$ Prolog (2.0). The former runs on an 80286 MS-DOS $^{TM}$ personal computer and the latter on a SUN-3 $^{TM}$ UNIX $^{TM}$ Workstation. All of the programs described in this paper run at acceptable speeds in both systems. For portability, the present code is almost entirely compatible with the de facto standard Edinburgh Prolog. Developing a logical spreadsheet, as described in the previous section, would presently require much extra, system-dependent code.

Some of the equipment and software for this research has been supported by U.S. Army Research Office Grant ARO-DAAG29-84-K-0060 to the University of Texas Artificial Intelligence Laboratory (UT AIL). I wish to thank Bruce Porter and Fletcher Mattox for assistance with setting up the Quintus Prolog, and Donald Nute for supplying his d-Prolog with sample programs and documentation. I also thank Steven Kimbrough, Donald Nute, Vladimir Lifschitz, and three anonymous referees for their comments on an earlier draft. The implementation of the Arity version of EVID was independently supported and performed by the author. Some of this work has been previously described in a UT AIL technical report.

## References

[1] M. Belzer and B. Loewer. A Conditional Logic for Defeasible Beliefs. Decision Support Systems 4, (No. 1): (1988), 129–142.

[2] G. Brewka. Tweety – Still Flying: Some Remarks on Abnormal Birds, Applicable Rules, and a Default Prover. In Proceedings of AAAI-86, Vol. I, pages 8–12. (Morgan Kaufmann, San Mateo, California, 1986; ISBN: 0-934613-13-3).

[3] M.R. Genesereth and N.J. Nilsson. Logical Foundations of Artificial Intelligence. (Morgan Kaufmann, San Mateo, California, 1987; ISBN: 0-934613-31-1).

[4] M.L. Ginsberg (editor). Readings in Nonmonotonic Reasoning (Morgan Kaufmann, San Mateo, California, 1987; ISBN: 0-934613-45-1).

[5] S.O. Kimbrough and F. Adams. Why Nonmonotonic Logic? Decision Support Systems 4, (No. 1): (1988), 111–127.

[6] John McCarthy. Applications of Circumscription to Formalizing Common-Sense Knowledge. Artificial Intelligence 28, (No. 1): (1986), 89–116.

[7] D. Nute. Defeasible Reasoning and Decision Support Systems. Decision Support Systems 4, (No. 1): (1988), 97–110.

[8] C.J. Petrie, R.L. Causey, et al.. A Planning Problem: Revisable Academic Course Scheduling. MCC Technical Report No. ACT-AI-020-89 (1989), Microelectronics and Computer Technology Corp., 3500 West Balcones Center Dr., Austin, TX 78759, 97 pp.

[9] J.L. Pollock. Contemporary Theories of Knowledge. (Rowman & Littlefield, Totowa, New Jersey, 1987; ISBN: 0-8476-7452-5).

[10] J.L. Pollock. Defeasible Reasoning. Cognitive Science 11, (no. 4): (1987), 481–518.

[11] D. Poole. A logical Framework for Default Reasoning. Artificial Intelligence 36, (No. 1): (1988), 27–47.

[12] R. Reiter. A Logic for Default Reasoning. Artificial Intelligence 13, (No. 1–2): (1980), 81–132.

[13] M.J. Sergot, F. Sadri, et al.. The British Nationality Act As a Logic Program. Communications of the ACM 29, (No. 5): (1986), 370–386.

[14] D.S. Touretzky. The Mathematics of Inheritance Systems. (Morgan Kaufmann, San Mateo, CA, 1986; ISBN: 0-273-08765-7).

[15] L. Wittgenstein. Tractatus Logico-Philosophicus. (Routledge & Kegan Paul, London, 1922).
