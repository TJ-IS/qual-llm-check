---
otero_id: 14270
otero_key: "895BF3GW"
title: "Matching observed behavior and modeled behavior: An approach based on Petri nets and integer programming"
authors: "Wil M.P. van der Aalst"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.03.013"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Matching observed behavior and modeled behavior: An approach based on Petri nets and integer programming

Wil M.P. van der Aalst

Department of Technology Management, Eindhoven University of Technology, P.O.Box 513, NL-5600 MB Eindhoven, The Netherlands

Received 7 January 2005; received in revised form 23 March 2006; accepted 26 March 2006 Available online 15 May 2006

## Abstract

Inspired by the way SAP R/3 and other transactional information systems log events, we focus on the problem to decide whether a process model and a frequency profile “fit” together. The problem is formulated in terms of Petri nets and an approach based on integer programming is proposed to tackle the problem. The integer program provides necessary conditions and, as shown in this paper, for relevant subclasses these conditions are sufficient. Unlike traditional approaches, the approach allows for labeled Petri nets with “hidden transitions”, noise, etc. © 2006 Elsevier B.V. All rights reserved.

Keywords: Process mining; Reference models; Petri nets; Integer programming; SAP R/3; Marking equation; Conformance testing

## 1. Introduction

For many processes in practice there exist models. These models are descriptive or prescriptive, i.e., they are used to describe a process or they are used to control or guide the system. Typical examples are the so-called reference models in the context of Enterprise Resource Planning (ERP) systems like SAP [15]. The SAP reference models are expressed in terms of so-called Event-driven Process Chains (EPCs) [14] describing how people should/could use the SAP R/3 system. Similar models are used in the workflow domain [25], and also in many other domains ranging from flexible manufacturing and telecommunication to operating systems and software components [17]. In some domains these models are referred to as specifications or blueprints. In reality, the real process may deviate from the modeled process, e.g., the implementation is not consistent with the specification or people use SAP R/3 in a way not modeled in any of the EPCs.

Clearly, the problem of checking whether the modeled behavior and the observed behavior match is not new. However, when we applied our process mining techniques [28] to SAP R/3 we were confronted with the following interesting problem: The logs of SAP do not allow for monitoring individual cases (e.g., purchase orders). Instead SAP only logs the fact that a specific transaction has been executed (without referring to the corresponding case). Hence, tools like the SAP Reverse Business Engineer (RBE) report on the frequencies of transaction types and not on the cases themselves. These transactions can be linked to functions in the EPCs, but, as indicated, not to individual cases. Moreover, some functions in the EPC do not correspond to a transaction code, and therefore, are not logged at all. This raises the following interesting question: Do the modeled behavior (i.e., the EPC) and the observed behavior (i.e., the transaction frequencies) match?

![](/api/attachments/895BF3GW/fulltext/images/053919200f33d95fc54a795fd7031b6a5cef84ecb23c8da7097bba6ea8708e76.jpg)  
Fig. 1. A Petri net.

The problem of checking whether the modeled behavior and the observed behavior match is not only relevant in the context of SAP. In a wide variety of applications only frequencies are being recorded and/or it is impossible to link events to specific cases. Therefore, we consider an abstraction of the problem. Consider a Petri net with some initial marking [18,19] and a frequency profile which is a partial function indicating how many times certain transitions fired. Consider for example the marked Petri net shown Fig. 1. A frequency profile fp could be fp(a) = 3, fp(b) = 2, fp(c) = 2, fp(d) = 2, and fp(e) = 3, thus indicating the number of times each transition occurred. However, the modeled behavior (i.e., the marked Petri net) and the observed behavior (the frequency profile fp) do not match. It is easy to see that fp(b) + fp(c) cannot exceed fp(a) since b and c depend on the tokens produced by a. Now consider another frequency profile fp: fp(a) = 3, fp(b) = 2, fp(d) = 2, and fp(e) = 3, i.e., the number of times c occurred is unknown. Now the modeled behavior and the observed behavior match, i.e., the observed transition frequencies are consistent with the Petri net model. Moreover, it is clear that in this situation c occurred precisely once.

In the remainder we will focus on this problem and propose an approach based on Integer Programming (IP) [23,35]. Using a marked Petri net and a frequency profile, an IP problem is formulated to check whether the modeled behavior and the observed behavior match and, if so, the frequencies of transitions not recorded in the profile are determined. First, we introduce some preliminaries, i.e., process mining, Petri nets, and integer programming, and discuss related work. Then we focus on the core problem and formulate the IP problem. We demonstrate the applicability of our approach using an example. Moreover, we show in more detail why the problem is relevant in the context of SAP and apply the approach to a SAP process model.

Finally, we conclude the paper by summarizing the results and discussing future work.

## 2. Preliminaries

This section presents some preliminaries needed in the remainder of the paper. We first discuss the concept of process mining and then introduce the two techniques used in this paper: Petri nets and Integer Programming. Finally, we present some related work.

## 2.1. Process mining

The research reported in this paper is part of our work on process mining [28–30,34]. The goal of process mining is to extract information about processes from transaction logs [28]. We typically assume that it is possible to record events such that (i) each event refers to an activity (i.e., a well-defined step in the process), (ii) each event refers to a case (i.e., a process instance), (iii) each event can have a performer also referred to as originator (the person executing or initiating the activity), and (iv) events have a timestamp and are totally ordered.<sup>1</sup> Table 1 shows an example of a log involving 19 events, 5 activities, and 6 originators. In addition to the information shown in this table, some event logs contain more information on the case itself, i.e., data elements referring to properties of the case.

Event logs such as the one shown in Table 1 are used as the starting point for mining. We distinguish three different perspectives: (1) the process perspective, (2) the organizational perspective and (3) the case perspective. The process perspective focuses on the controlflow, i.e., the ordering of activities. The goal of mining in this perspective is to find a good characterization of all possible paths, e.g., expressed in terms of a Petri net or Event-driven Process Chain (EPC). The organizational perspective focuses on the originator field, i.e., which performers are involved and how are they related. The goal is to either structure the organization by classifying people in terms of roles and organizational units or to show relation between individual performers (i.e., build a social network). The case perspective focuses on properties of cases. Cases can be characterized by their path in the process or by the originators working on a case. However, cases can also be characterized by the values of the corresponding data elements. For example, if a case represents a replenishment order it is interesting to know the supplier or the number of products ordered.

<table><tr><td colspan="4">An event log</td></tr><tr><td>Case id</td><td>Activity id</td><td>Originator</td><td>Timestamp</td></tr><tr><td>Case 1</td><td>Activity A</td><td>John</td><td>9-3-2004:15.01</td></tr><tr><td>Case 2</td><td>Activity A</td><td>John</td><td>9-3-2004:15.12</td></tr><tr><td>Case 3</td><td>Activity A</td><td>Sue</td><td>9-3-2004:16.03</td></tr><tr><td>Case 3</td><td>Activity B</td><td>Carol</td><td>9-3-2004:16.07</td></tr><tr><td>Case 1</td><td>Activity B</td><td>Mike</td><td>9-3-2004:18.25</td></tr><tr><td>Case 1</td><td>Activity C</td><td>John</td><td>10-3-2004:9.23</td></tr><tr><td>Case 2</td><td>Activity C</td><td>Mike</td><td>10-3-2004:10.34</td></tr><tr><td>Case 4</td><td>Activity A</td><td>Sue</td><td>10-3-2004:10.35</td></tr><tr><td>Case 2</td><td>Activity B</td><td>John</td><td>10-3-2004:12.34</td></tr><tr><td>Case 2</td><td>Activity D</td><td>Pete</td><td>10-3-2004:12.50</td></tr><tr><td>Case 5</td><td>Activity A</td><td>Sue</td><td>10-3-2004:13.05</td></tr><tr><td>Case 4</td><td>Activity C</td><td>Carol</td><td>11-3-2004:10.12</td></tr><tr><td>Case 1</td><td>Activity D</td><td>Pete</td><td>11-3-2004:10.14</td></tr><tr><td>Case 3</td><td>Activity C</td><td>Sue</td><td>11-3-2004:10.44</td></tr><tr><td>Case 3</td><td>Activity D</td><td>Pete</td><td>11-3-2004:11.03</td></tr><tr><td>Case 4</td><td>Activity B</td><td>Sue</td><td>11-3-2004:11.18</td></tr><tr><td>Case 5</td><td>Activity E</td><td>Clare</td><td>11-3-2004:12.22</td></tr><tr><td>Case 5</td><td>Activity D</td><td>Clare</td><td>11-3-2004:14.34</td></tr><tr><td>Case 4</td><td>Activity D</td><td>Pete</td><td>11-3-2004:15.56</td></tr></table>

The ProM framework [28–30] has been developed to extract information from event logs.<sup>2</sup> It offers wide varieties of the so-called “plug-ins”. There are mining plug-ins for each of the three perspectives. Fig. 2 shows a screenshot of the ProM tool while analyzing the event log shown in Table 1.

The Petri net [8] shown on the right-hand side in Fig. 2 is the result of applying the α algorithm plug-in to the event log shown in Table 1. This is one of the five mining plug-ins focussing on the process perspective. Note that the event log contains information about five cases (i.e., process instances). The log shows that for four cases (1, 2, 3, and 4) the activities A, B, C, and D have been executed. For the fifth case only three activities are executed: activities A, E, and D. Each case starts with the execution of A and ends with the execution of D. If activity B is executed, then also activity C is executed. However, in some cases activity C is executed before activity B. The α algorithm [29] translates this information into causal dependencies and generates the Petri shown in Fig. 2. It is easy to see that this is indeed the most likely process model explaining the behavior observed in the log. The Petri net starts with activity A and finishes with activity D. These activities are represented by transitions. After executing A there is a choice between either executing B and C in parallel or just executing activity E.

ProM also has plug-ins to analyze the organizational perspective. An example is shown on the left-hand side in Fig. 2. Using the social network mining plug-in [27] a so-called social network is generated. The social network shown in Fig. 2 is based on the transfer of work from one individual to another, i.e., the focus is on relations among individuals (or groups of individuals) based on how work flows through the organization. Consider again Table 1. Although Carol and Mike can execute the same activities (B and C), Mike is always working with John (cases 1 and 2) and Carol is always working with Sue (cases 3 and 4). Probably Carol and Mike have the same role but based on the small sample shown in Table 1 it seems that John is not working with Carol and Sue is not working with Carol. These examples show that the event log can be used to derive relations between performers of activities, thus resulting in a sociogram as shown in Fig. 2. The sociogram shows that work is transferred to Pete but not vice versa. Mike only interacts with John and Carol only interacts with Sue. Clare is the only person transferring work to herself.

Besides the “How?” and “Who?” question (i.e., the process and organization perspectives), there is the case perspective that is concerned with the “What?” question. The case perspective looks at the case as a whole and tries to establish relations between the various properties (i.e., data) of a case. ProM also allows for the analysis of this perspective (e.g., through the LTL checker plug-in). However, Table 1 does not show any data elements. Therefore, we do not elaborate on this and simply refer to Refs. [28,30].

As Fig. 2 shows, an event log such as the one shown in Table 1 can be the starting point of a wide variety of analysis techniques. Unfortunately, these classical forms of process mining only work if the identities of individual cases are logged. In reality, like in SAP, only frequencies of activities are often known or the first column in Table 1 is missing (case id's). Therefore, we would like to extend our work on process mining to situations where only frequencies are known as described in the introduction.

![](/api/attachments/895BF3GW/fulltext/images/80c37c98bf443aa8b52b5293cd198fecf37d34e7974d948d49009e819559b4d6.jpg)  
Fig. 2. Some mining results obtained using our ProM tool (see http://www.processmining.org). The results shown are based on the event log shown in Table 1.

## 2.2. Petri nets

This section introduces the basic Petri net terminology and notations (cf. [19,7]). Readers familiar with Petri nets can skip this section.

The classical Petri net is a directed bipartite graph with two node types called places and transitions. The nodes are connected via directed arcs. Connections between two nodes of the same type are not allowed. Places are represented by circles and transitions by rectangles.

Definition 1. (Petri net). A Petri net is a triple (P, T, F):

\- P is a finite set of places,

\- T is a finite set of transitions $( P \cap T { = } \phi )$

$\bullet \ F { \subseteq } ( P \times T ) \cup ( T \times P )$ is a set of arcs (flow relation)

A place p is called an input place of a transition t iff there exists a directed arc from p to t. Place p is called an output place of transition t iff there exists a directed arc from t to p. We use •t to denote the set of input places for a transition t. The notations $t ^ { \bullet } , \bullet p$ and $p ^ { \bullet }$ have similar meanings, $\mathrm { e . g . , } p ^ { \bullet }$ is the set of transitions sharing p as an input place. In this paper, we do not consider multiple arcs from one node to another. However, all results can be extended to Petri nets with arcs weights.

Fig. 1 shows a Petri net with 5 transitions (a, b, c, d, and e) and 6 places $( p 1 , \ldots p 6 )$ .

At any time a place contains zero or more tokens, drawn as black dots. The state, often referred to as marking, is the distribution of tokens over places, i.e., $\scriptstyle M \in P \to \mathbb { N }$ . We will represent the marking as follows: $1 ^ { \prime } p 1 + 2 ^ { \prime } p 2 + 1 ^ { \prime } p 3 + 0 ^ { \prime } p 4$ is the marking with one token in place $p 1$ , two tokens in $p 2$ , one token in $p 3$ and no tokens in p4. We can also represent this marking as follows: $p 1 + 2 ^ { \prime } p 2 + p 3$ . The marking shown in Fig. 1 is $p 1$ . (Note the overloading of notation.) To compare markings we define a partial ordering. For any two markings $M _ { 1 }$ and $M _ { 2 } , M _ { 1 } \leq M _ { 2 }$ iff for all $p \in P ; M _ { 1 }$ $( p ) \leq M _ { 2 } ( p )$

The number of tokens may change during the execution of the net. Transitions are the active components in a Petri net: they change the marking of the net according to the following firing rule:

(1) A transition t is said to be enabled iff each input place p of t contains at least one token.

(2) An enabled transition may fire. If transition t fires, then t consumes one token from each input place p of t and produces one token for each output place p of t.

In Fig. 1 transition a is enabled. Firing a results in marking $2 ^ { \prime } p 1 + p 2 + p 3$ . In this marking, three additional transitions (besides a) are enabled $( b , \ c , \ d )$ Any of these transitions may fire. However, firing one of these transitions will disable one or two other transitions, e.g., firing $c$ will disable both $b$ and $d .$

Given a Petri net $( P , T , F )$ and a marking $M _ { 1 } ,$ , we have the following notations:

$M _ { 1 } { \stackrel { t } { \longrightarrow } } M _ { 2 } \colon$ transition t is enabled in marking $M _ { 1 }$ and firing t in $M _ { 1 }$ results in marking $M _ { 2 }$

$M _ { 1 } { \longrightarrow } M _ { 2 } \mathrm { . }$ : there is a transition t such that $M _ { 1 } \xrightarrow { t } M _ { 2 }$

$M _ { 1 } \stackrel { \sigma } {  } M _ { n }$ : the firing sequence $\sigma { = } t _ { 1 } t _ { 2 } t _ { 3 } { \ldots } t _ { n - 1 }$ leads from marking $M _ { 1 }$ to marking $M _ { n }$ via a (possibly empty) set of intermediate markings $M _ { 2 } , . . . M _ { n - 1 }$ , i.e., $M _ { 1 } { \stackrel { \cdot } { \longrightarrow } } M _ { 2 } { \stackrel { t _ { 2 } } { \longrightarrow } } \dots { \stackrel { t _ { n - 1 } } { \longrightarrow } } M _ { n }$

A marking $M _ { n }$ is called reachable from $M _ { 1 }$ (notation $M _ { 1 } { \stackrel { * } { \longrightarrow } } M _ { n } )$ iff there is a firing sequence $\sigma$ such that $M _ { 1 } { \stackrel { \sigma } { \to } } M _ { n }$ . Note that the empty firing sequence is also allowed, $\operatorname { i . e . , } M _ { 1 } \mathrel { \mathop { \leq } } M _ { 1 }$

To manipulate firing sequences, we introduce the Parikh vector $\pi _ { \sigma } \in T { \overset { } { \to } } I N$ , where ${ \pmb { \pi } } _ { \sigma } ( t )$ denotes the number of occurrences of transition t in σ.

We use (PN, M) to denote a Petri net PN with an initial marking M. A marking $M ^ { \prime }$ is a reachable marking of (PN, M) iff $M { \stackrel { * } { \to } } M ^ { \prime } .$ Consider the Petri net shown in Fig. 1 with only one token in p1. For this initial marking there are 6 reachable markings.

## 2.3. Integer Programming

Besides Petri nets we use Integer Programming (IP) to address the problem of checking whether the modeled behavior and the observed behavior match. An IP problem can be seen as a variant of the classical Linear Programming (LP) problem [23,35]. Therefore, before introducing the IP problem, we briefly introduce the basic idea of an LP problem. First, we define the LP problem. The standard form of an LP problem is:

$$
\begin{array}{l} \min (\boldsymbol {c} _ {1}, \boldsymbol {c} _ {2}, \dots , \boldsymbol {c} _ {n}) (\boldsymbol {x} _ {1}, \boldsymbol {x} _ {2}, \dots , \boldsymbol {x} _ {n}) \quad \text { s.t. } \mathbf {A} (\boldsymbol {x} _ {1}, \boldsymbol {x} _ {2}, \dots , \boldsymbol {x} _ {n}) \\ = (\boldsymbol {b} _ {1}, \boldsymbol {b} _ {2}, \dots , \boldsymbol {b} _ {m}) \quad \boldsymbol {x} _ {i} \geq 0 \quad \text { for   all } 1 \leq i \leq n \end{array}
$$

where $x _ { 1 } , x _ { 2 } , . . . , x _ { n }$ are n variables forming a (unknown) vector $( \pmb { x } _ { 1 } , \pmb { x } _ { 2 } . . . , \pmb { x } _ { n } ) .$ , A is a matrix of known coefficients, and $( \pmb { c } _ { 1 } , \pmb { c } _ { 2 } . . . , \pmb { c } _ { n } )$ and $( \pmb { b } _ { 1 } , \pmb { b } _ { 2 } . . . , \pmb { b } _ { m } )$ are vectors of known coefficients. The expression $( \pmb { c } _ { 1 } , \ c _ { 2 } . . . , \pmb { c } _ { n } ) ( \pmb { x } _ { 1 } , \ \pmb { x } _ { 2 } . . . , \pmb { x } _ { n } )$ takes the product of two vectors and is called the objective function. The equations formed by $\mathbf { A } ( x _ { 1 } , x _ { 2 } . . . ,$ $\pmb { x } _ { n } ) = ( \pmb { b } _ { 1 } , \pmb { b } _ { 2 } . . . , \pmb { b } _ { m } )$ are called the constraints. All these entities must have consistent dimensions.<sup>3</sup> Note that n is the number of variables and $m$ is the number of constraints. The goal is to minimize the objective function while respecting the constraints.

Although all linear programs can be put into the standard form, in practice it may not be necessary to do so. For example, although the standard form requires all variables to be non-negative it is possible to rewrite $k \leq x _ { i } \leq l$ into the standard form by using two new variables ${ x } _ { k } { = } { x } _ { i } { - } k$ and $x _ { l } { = } l { - } x _ { i }$ and require $x _ { k } \ge 0$ and $x _ { l } \ge 0$ . Similarly, inequalities in the constraints can be replaced by equalities by introducing explicit slack variables. The simplex method was the first method developed to solve LP problems. A much more efficient (polynomial time) algorithm was found by Karmarkar in 1984 [13].

For many applications the assumption that the variables are continuous is unrealistic. In many practical applications, some variables will denote decisions, $\mathrm { e . g . , } x _ { i } { = } 0 \ \mathrm { o r } x _ { i } { = } 1$ rather than any value between 0 and 1. In an Integer Programming (IP) problem the variables are integers, i.e., it is like an LP problem but now $x _ { i }$ should be integer for all $1 \leq i \leq n$ . Unfortunately, the IP problem can no longer be solved in polynomial time and one needs to resort to computationally expensive methods like branch and bound [23,35].

In some cases it is useful to consider the LP relaxation of an IP problem. In this case the objective function and constraints are the same but the integer variables are replaced by appropriate continuous variables and constraints. For example ${ x _ { i } } \mathrm { { = } } 0 \ \mathrm { { o r } } \ x _ { i } \mathrm { { = } } 1$ is then replaced by $0 \leq x _ { i } \leq 1$ . The LP solution might turn out to have all variables taking integer values at the LP optimal solution. In this case we obtain an optimal integer solution. If we have variables taking fractional values at the LP optimal solution, then we can round these off to the nearest integer value. However, in many cases the rounded LP relaxation solution either violates a constraint or yields a non-optimal solution, i.e., LP relaxation is fast (polynomial time) but may be inaccurate to some degree. Nevertheless, IP problems are typically easier to solve than methods requiring the construction of the full state space.

## 2.4. Related work

The starting point of this work is the literature on process mining [28,29,1,3,9,11,36,22,34]. The idea of applying process mining in the context of workflow management was first introduced in Ref. [1]. Since then several researchers have been working on this topic and we refer to Ref. [28] for a survey on process mining. ProM [30] is an example of a tool for process mining. An example of a commercial tool is the ARIS Process Performance Manager (PPM) [11]. Some of the ideas developed in the context on the ProM tool have been adopted in tools like PPM (e.g., the OrgAnalyzer in version 4).

Although not explicitly addressed in this paper, our work is related to reference modeling [2,20]. One of the most comprehensive models is the SAP reference model [4,15]. Its data model includes more than 4000 entity types and the reference process models cover more than 1000 business processes and inter-organizational business scenarios. Most of the other dominant ERP vendors have similar or alternative approaches towards reference models. We have developed a new reference modeling language: Configurable EPCs [21], i.e., an extension of the EPC language [14] used by SAP and ARIS. Using classical process mining techniques we have developed an approach to discover the configuration [12].

In a technical sense, the work presented is most related to the “Marking Equation” known from Petri net theory [17,6,24] and this paper builds on some of these results. However, the approach presented differs in at least two ways. First of all, the marking equation considers the initial and resulting marking while we only consider the initial marking. Second, we allow for transition frequencies that are unknown, i.e., the frequency profile may be incomplete. Moreover, the approach allows for the extensions described in Section

5 while the marking equation does not. Clearly there are also relations with the classical results on place and transition invariants [7,24,18]. However, these are less direct.

## 3. Matching a marked Petri net and a frequency profile

As indicated in the introduction, we use Petri nets to model processes. However, other types of models, e.g., the EPCs used by the SAP reference model, can be mapped onto Petri nets.<sup>4</sup> Petri nets may be used to model a wide variety of processes. A Petri net can model what we think the process is (i.e., a descriptive model) but it can also model what the process should be (i.e., a prescriptive model). In both cases, the real process may deviate from what is modeled in the Petri net. In this section, we investigate whether the modeled behavior (i.e., Petri net) and the observed behavior match. Since in reality we often cannot inspect the state and just observe events, it is realistic to assume that we can only monitor the firing of transitions. Moreover, we assume that we cannot link transition occurrences to specific tokens or exploit their ordering in time, i.e., we only know the frequency profile.

To illustrate the problem, we again show the Petri net used in the introduction. Fig. 3, shows a Petri net and two frequency profiles. Both the graphical and textual representation of the marked Petri net are given in Fig. 3(a). For a Petri net with transitions T, the frequency profile refers to a subset of T, i.e., frequency profile $f p \in T { \not \to } \mathbb { N }$ is a partial function. For t ∈ dom (fp), fp(t) is the number of times t occurred/fired. For t∉dom(fp) this is unknown. If dom $( \mathit { f p } ) { = } T ,$ the frequency profile is complete. Fig. 3(b) shows a complete frequency profile. The frequency profile shown in Fig. 3(c) is incomplete because fp(c) is not given (i.e., c ∉ dom (fp)).

The marked Petri net shown in Fig. 3(a) and frequency profile given in Fig. 3(b) do not “match”, because there is no firing sequence starting from the initial marking resulting in the $f p$ shown $( f p ( b ) + f p ( c )$ cannot exceed fp(a) since b and c depend on the tokens produced by a, but it does). However, a match with the frequency profile given in Fig. 3(c) is possible. The firing sequence $( a , b , d , e , a , b , d , e , a , c , e )$ fires a and e three times, b and d two times, and c once, i.e., it is consistent with the $f \dot { p }$ shown in Fig. 3(c).

Both for complete and incomplete frequency profiles we define the predicate match (PN, M, fp) to formalize the notions just introduced.

![](/api/attachments/895BF3GW/fulltext/images/3238f08526ece08f78d88b221a632c235fd56108d25fae5026b07d2fdfe9df23.jpg)  
Fig. 3. A process model with two frequency profiles.

Definition 2. (Match). Let (PN, M) be a marked Petri net with $P N { = } ( P , ~ T , ~ F )$ and $f p \in P \not \to \mathbb { N }$ a frequency profile. (PN, M) and fp match if there exists a firing sequence σ enabled in M $( \mathrm { i . e . , } M \xrightarrow { \sigma } )$ such that for all $t \in d o m ( { \boldsymbol { f } } p ) \colon f p ( t ) = \pi _ { \sigma } ( t )$ . (Notation: match(PN, M, fp).)

Clearly, match(PN, M, fp) = false for Fig. 3(b) and match(PN, M, fp) = true for Fig. 3(b). Note that for any marked Petri net there is a trivial matching profile $f \bar { p }$ with $d o m ( \it { f p } ) = 0$

Definition 2 refers to the existence of one firing sequence σ. This firing sequence may refer to multiple process instances (called “cases” in workflow jargon) as shown in the example. $( a , b , d , e , a , b , d , e , a , c , e )$ symbolizes the complete processing of the three cases in place p1. In Fig. 3(a) the initial marking determines the number of cases. However, it is also possible to add source transitions (i.e., transitions without any input places) and sink transitions (i.e., transitions without any output places). In the example of Fig. 3 we could have started with an empty initial marking (no tokens) and a source transition $t _ { s t a r t }$ with $\bullet t _ { s t a r t } { = } \phi ;$ and $t _ { s t a r t } \bullet = \{ p 1 \}$ In this case, Fig. 3(b) still does not match while Fig. 3 (c) does. This example shows that match(PN, M, fp) can be applied to “open nets” (source and sink transitions and no initial tokens), “closed nets” (no source and sink transitions and initially some places are marked), and mixtures of the latter two.

Even for moderate examples, the number of firing sequences may be too large to check match(PN, M, fp). Therefore, in the spirit of Refs. [6,17], we can try to formulate a linear algebraic representation. Given the discrete nature of firing transitions, we propose an Integer Programming (IP) problem rather than a Linear Programming (LP) problem [23,35]. In other words, we consider the function match(PN, M, fp) and try to formulate it in terms of an IP problem.

Definition 3. (Integer programming problem). Let (PN, M) be a marked Petri net with $P N { = } ( P , ~ T , ~ F )$ and $f p \in T { \not \to } \mathbb { N }$ a frequency profile. IP(PN, M, fp) is the corresponding Integer Programming (IP) problem:

$$
\begin{array}{l l} \min \sum_ {t \in T} f _ {t} \\ \text { s.t. } f _ {t} = f p (t) & \text { for   all } t \in d o m (f p) \\ f _ {(t, p)} = f _ {t} & \text { for   all } (t, p) \in F \cap (T \times P) \\ f _ {(p, t)} = f _ {t} & \text { for   all } (p, t) \in F \cap (P \times T) \\ M (p) + \sum_ {t \in \bullet p} f _ {(t, p)} - \sum_ {t \in p ^ {\bullet}} f _ {(p, t)} \geq 0 & \text { for   all } p \in P \\ f _ {t} \geq 0 & \text { for   all } t \in T \\ f _ {t} \quad \text { integer } & \text { for   all } t \in T \\ f _ {(x, y)} \quad \text { integer } & \text { for   all } (x, y) \in F \end{array}
$$

There are two types of positive integer variables: $f _ { t }$ for transition frequencies and $f ( x , y )$ for arc frequencies. The first constraint specifies that the transition frequencies should match the frequency profile. Note that for some transitions there may not be a frequency in the frequency profile. The second and third constraints refer to the fact that transition frequencies and arc frequencies need to be aligned. The fourth type of constraint is the most interesting one. For each place, there should be a balance between the inflow of tokens and the outflow of tokens, i.e., it is not possible to consume more tokens than the initial ones plus the produced ones. The objective function minimizes the number of firings. Given the nature of the problem this is of less importance and alternative objective functions can be defined, e.g., an objective function maximizing or minimizing the number of tokens in the net.

Before we discuss the relation between match(PN, M, fp) and IP(PN, M, fp), let us return to the Petri net shown in Fig. 3(a). Assuming some initial marking M

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
and some frequency profile $fp$, $IP(PN, M, fp)$ is formulated as follows.

$\min f_a + f_b + f_c + f_d + f_e$

s.t. $f_a = fp(a)$ $\cdots$ $f_{(a,p2)} = f_a$ $\cdots$ $f_{(p1,a)} = f_a$ $\cdots$ $M(p1) - f_{(p1,a)} \geq 0$ $M(p2) + f_{(a,p2)} - f_{(p2,b)} - f_{(p2,c)} \geq 0$ $M(p3) + f_{(a,p3)} - f_{(p3,c)} - f_{(p3,d)} \geq 0$ $M(p4) + f_{(b,p4)} + f_{(c,p4)} - f_{(p4,e)} \geq 0$ $M(p5) + f_{(c,p5)} + f_{(d,p5)} - f_{(p5,e)} \geq 0$ $M(p6) + f_{(e,p6)} \geq 0$ $f_a \geq 0$ $\cdots$ $f_a \quad \text{integer}$ $\cdots$ $f_{(p1,a)} \quad \text{integer}$ $\cdots$
</div>

Applying this to the initial marking shown in Fig. 3 (a) and the frequency profile $f p ( a ) = 3 , f p ( b ) = 2 , f p ( c ) = 2 ,$ $f p ( d ) = 2$ , and $f p ( e ) = 3$ indeed results in an IP problem without a solution. While applying it to the second frequency profile fp(a) = 3, fp(b) = 2, fp(d) = 2, and $f p ( e ) = 3$ yields the solution where fc = 1. In the latter case the value of the objective function is 11.

In the remainder of this section we investigate the relation between match(PN, M, fp) and $I P ( P N , M , f p )$ 6 i.e., “Can the IP problem be used to determine whether the modeled and observed behavior match?”. It is important to establish this relation because, IP(PN, $M ,$ $f ( \boldsymbol { p } )$ can be solved more efficiently than determining match(PN, M, fp) on the basis of constructing and traversing the coverability graph [7,17,19].

The following theorem shows that, as expected, the IP problem indeed provides necessary requirements.

Theorem 1. Let (PN, M) be a marked Petri net with $P N = \left( P \right)$ T, F) and $f p \in T { \not \to } I N$ a frequency profile. If match(PN, M, fp), then IP(PN, M, fp) has a solution.

Proof. If match(PN, M, fp), then there exists a firing sequence σ enabled in M $( \mathrm { i . e . , } M \xrightarrow { \sigma } )$ such that for all $t \in T \colon f p ( t ) = \pi _ { \sigma } ( t )$ . Let $M ^ { \prime }$ be the resulting marking. Now consider the IP problem. The only constraint that could be violated is $\begin{array} { r } { M ( p ) + \sum _ { t \in \bullet p } f _ { ( t , p ) } - \sum _ { t \in p \bullet } f _ { ( p , t ) } { \geq } 0 } \end{array}$ for some $p \in P .$ However, this constraint follows directly from the firing rule. In fact, $\begin{array} { r } { M ( p ) + \sum _ { t \in \bullet p } f _ { ( t , p ) } - } \end{array}$ $\begin{array} { r } { \sum _ { t \in p \bullet } f _ { ( p , t ) } = M ^ { \prime } ( p ) } \end{array}$ □

![](/api/attachments/895BF3GW/fulltext/images/252c0b9e81657c11c782b94307cc60223e2ffbb5f29c0ec58410ccdbf2482066.jpg)  
Fig. 4. Counter example.

The theorem shows that, if $I P ( P N , M , f p )$ does not have a solution, match(PN, M, fp) does not hold. This allows for the quick detection of mismatches between the model and the observed behavior.

Unfortunately, the result does not hold in the opposite direction, as can be shown by an example taken from [7]. Fig. 4 shows a marked Petri net. Let $f p ( t ) = 1$ for all transitions t except for $t { = } g$ which occurs twice $( \mathrm { i } . \mathrm { e } . , f p ( g )$ $= 2 )$ . It is easy to verify that IP(PN, $M , f p )$ has a solution. However, the marked Petri net and the frequency profile do not match because there is no firing sequence (starting in the initial marking shown in Fig. 4) that fires $g$ twice and all other transitions once. (Note that it is impossible to return to the initial marking.) Fortunately, for certain subclasses the result does hold in the opposite direction. In the remainder we will explore some of these subclasses for which match(PN, M, fp) if and only if IP(PN, M, fp) has a solution. The following theorem, shows that this is the case for all acyclic processes.

Theorem 2. Let (PN, M) be an acyclic marked Petri net with $P N = \left( P \right)$ T, F) and $f p \in T { \not \to } I N$ a frequency profile such that IP(PN, M, fp) has a solution. There exists a firing sequence σ enabled in M such that for all t ∈ dom $( f p ) \colon f p ( t ) = \pi _ { \sigma } ( t )$ , i.e., match(PN, M, fp).

Proof. In the solution of IP(PN, $M , f p )$ each transition $t \in T$ fires $f _ { t }$ times. Let $\begin{array} { r } { n = \sum _ { t \in T } f _ { t } . } \end{array}$ . If n = 0, the empty sequence is enabled and the theorem holds. If $n { > } 0$ remove all transitions t for which $f _ { t } { = } 0$ . Moreover, remove all places and arcs not connected to a transition t for which $f _ { t } { > } 0 .$ . Let $P N ^ { \prime }$ be the resulting net and $M ^ { \prime }$ the resulting marking. Clearly, $P N ^ { \prime }$ is acyclic. At least one transition is enabled in (PN′, M′). (If not, the fact that $P N ^ { \prime }$ is acyclic would imply that there is an empty source place $p$ with some output transition $t ^ { \prime } .$ . However, $M ( p ) +$ $\begin{array} { r } { \sum _ { t \in \bullet p } f _ { ( t , p ) } - \sum _ { t \in p \bullet } \ f _ { ( p , t ) } = \ M ^ { \prime } ( p ) + 0 \ – f _ { p , t ^ { \prime } } \ – \dots = 0 + } \end{array}$ $0 { - } f _ { t ^ { \prime } } { - } _ { \cdots } { \geq } 0$ . Clearly, this leads to a contradiction.) Fire this enabled transition $t ^ { * }$ and let $M ^ { * }$ be the resulting marking and $f ( p *$ such that $f p ^ { * } ( t ^ { * } ) { = } f p ( t ^ { * } ) - 1$ and for all other $t \in \mathrm { d o m } ( f p ) { : } f p ^ { * } ( t ) { = } f p ( t )$ . Clearly, $I P ( P N , M ^ { * } , f p ^ { * } )$ has a solution. Repeat the above process until $n { = } 0 .$ . In each step, a transition $t ^ { * }$ is fired thus forming a sequence σ enabled in M. □

Note that the Proof of this theorem is similar to Theorem 16 in [17]. Consider Fig. 4 with the arc from $g$ to $p 1$ removed and a new place $p 8$ added as an output place of $\cdot _ { g . }$ . Now for any marking M and any frequency profile $f \bar { p }$ such that IP(PN, M, fp) has a solution, there exists a corresponding firing sequence, i.e., match(PN, $M , f p )$ . For example, given the marking shown in Fig. 4 and the acyclic variant of the net, the IP problem has a solution for the following frequency profile $f p \colon f p ( a ) { = } f p$ $\scriptstyle ( b ) = f p ( d ) = f p ( e ) = 0 , \ f p ( c ) = f p ( f ) = f p ( g ) = 1$ . Indeed, as suggested by Theorem 2, there is a firing sequence firing $c , f$ and $g \left( { \mathrm { e . g . , } c f g } \right)$

The counter example shown in Fig. 4 is free-choice [7]. Therefore, one could consider to prove Theorem 2 for subclasses of free-choice nets (i.e., replace the requirement that the net is acyclic with some other structural requirement). Two well-known subclasses are the class of marked graphs and the class of state machines [7,17,19].

A marked graph is a Petri net with for each place $p \in P ; \ | \bullet p | = | p \bullet | = 1$ (i.e., places cannot have multiple input or output transitions). A circuit is a circular path in the Petri net such that no element (i.e., place or transition) occurs more than once. It is easy to see that in a marked graph the number of tokens in a circuit is constant. Therefore, a circuit remains (un)marked if it is (un)marked in the initial marking. Using existing results it is easy to prove that Theorem 2 applies to (cyclic) marked graphs where each circuit is marked.

Theorem 3. Let (PN, M) be a marked graph with $P N =$ (P, T, F) and $f p \in T { \not \to } I N$ a frequency profile. If each circuit is initially marked, then IP(PN, M, fp) has a solution if and only if match(PN, M, fp).

Proof. As shown in Theorem 1, match(PN, M, fp) implies that IP(PN, M, fp) has a solution. Remains to prove that IP(PN, M, fp) has a solution also implies match(PN, M, fp). Consider a solution assigning values to each $f _ { t }$ and $f _ { ( x , y ) } .$ Let $M ^ { \prime }$ be a marking defined as follows: $\begin{array} { r } { M ( p ) + \sum _ { t \in \bullet p } f ( t , p ) - \sum _ { t \in p \bullet } f ( p , t ) = M ^ { \prime } ( p ) } \end{array}$ for all $p \in P .$ Note that M′ is indeed a marking, i.e., for each $p \in P , M ^ { \prime } ( p )$ is a non-negative integer. This implies that the marking equation $M ^ { + } \mathbf { N } . X ^ { = } M ^ { \prime }$ has a solution (N is the incidence matrix and X is a vector.). This solution is given by the values assigned to $f _ { t } .$ Because there is a solution, M and $M ^ { \prime }$ agree on all place invariants. For live marked graphs a marking $M ^ { \prime }$ is reachable from M if and only if both agree on all place invariants (cf. Theorem 3.21 in [7]). A marked graph where each circuit is initially marked is live (cf. Theorem 3.15 in [7]). Therefore, $M ^ { \prime }$ is reachable from M and match(PN, M, fp). □

Fig. 5 shows a marked graph. For any initial marking $M ,$ the IP problem has a solution if and only if match (PN, M, fp) (provided that every circuit is initially marked).

A Petri net is a state machine iff transitions cannot have more than one input or output place, i.e., for each transition $t \in T ; | \bullet t | = | \bullet t | = 1$ . It is easy to prove that Theorem 3 also holds for state machines as long as the the net is strongly connected $( \mathrm { i . e . }$ , there is a directed path from any node to any other node in the net) and initially there is at least one token.

Theorem 4. Let (PN, M) be a strongly connected state machine with $P N { = } ( P , ~ T , ~ F )$ and a non-empty initial marking $f p \in T { \not \to } I N$ a frequency profile. IP(PN, M, fp) has a solution if and only if match(PN, M, fp).

Proof. As shown in Theorem 1, match(PN, M, fp) implies that IP(PN, M, fp) has a solution. Remains to prove that the reverse also holds. Consider a solution assigning values to each $f _ { t }$ and $f _ { ( x , y ) }$ . Let $M ^ { \prime }$ be a marking defined as follows: $\begin{array} { r } { M ( p ) + \sum _ { t \in \bullet p } f _ { ( t , p ) } - \sum _ { t \in p \bullet } f _ { ( p , t ) } = } \end{array}$ $M ^ { \prime } ( p )$ for all $p \in P .$ Note that $M ^ { \prime }$ is indeed a marking, i.e., for each $p \in P , M ^ { \prime } ( p )$ is a non-negative integer. The number of tokens in M equals the number of tokens in $M ^ { \prime } ,$ , in fact M and $M ^ { \prime }$ agree on all place invariants. Moreover, the marked state machine is live because PN is a strongly connected state machine and M is nonempty (cf. Theorem 3.3 in [7]). Using the second reachability theorem (cf. Theorem 3.8 in [7]), it follows that M′ is reachable from M and match(PN, M, fp). □

![](/api/attachments/895BF3GW/fulltext/images/0851ba228f0d4d4478dddbc7cb13bd477361a6558cbecba36f3793c45856a716.jpg)  
Fig. 5. Marked graph.

![](/api/attachments/895BF3GW/fulltext/images/58f6e62eb4fd6133fc26289acaf0948bb44f8a1dfbd23fda286344f977093b1a.jpg)  
Fig. 6. State machine.

Fig. 6 shows a strongly connected state machine. For any non-empty initial marking M IP(PN, M, fp) has a solution if and only if match(PN, M, fp).

In this section, we explored the relation between match(PN, M, fp) (i.e., the predicate indicating that a process model and observed transition frequencies fit together) and IP(PN, M, fp) (i.e., an integer programming problem). In the remainder, we consider a larger example, possible extensions, and the application of the results in the SAP context.

## 4. Example

After showing a number of abstract examples, we now use the more realistic example shown in Fig. 7. It describes the workflow [25] of handling orders. The upper half models the logistical subprocess while the lower half models the financial subprocess. Most of the workflow should be self-explanatory except perhaps for the construct involving c7 and t10 (reminder): A reminder can only be sent if the goods have been shipped.

Unlike the other two Petri nets, the initial marking is empty. Instead a source and a sink transition have been added. Transition t0 (create) creates the order while t13 (destroy) marks the end of the order. This pattern is often used to model an unknown number of cases.

Suppose that only the steps t1 (register ), t6 (replenish), t8 (ship\_goods), t9 (send\_bill), t11 (receive\_payment), and t12 (archive) are recorded. Fig. 7 shows four frequency profiles $( f p _ { 1 } , ~ f p _ { 2 } , ~ f p _ { 3 }$ , and $f ( p _ { 4 } )$ . The IP problems corresponding to the first two profiles $( f p _ { 1 }$ and $f ( p _ { 2 } )$ , both have a solution. It is also easy to see that $f { \boldsymbol { p } } _ { 1 }$ and $f { \ ' } p _ { 2 }$ both indeed match with the Petri net. Note that in the first profile there are no replenishment orders and no reminders, i.e., t4, t6 and t10 do not fire. It is also interesting to note that the number of times t3 and $t 7$ fire is not constrained by $f { \boldsymbol { p } } _ { 1 }$ , however, by the objective function their frequencies are set to 0. In the second profile there are 10 replenishment orders and 5 reminders. The IP problems corresponding to the last two profiles $( f p _ { 3 }$ and $f ( p _ { 4 } )$ , both do not have a solution and, indeed, $f { \ ' } p _ { 3 }$ and $f p _ { 4 }$ do not match with the Petri net. In $f { \ ' } p _ { 3 }$ there are not enough bills (70) to justify the number of payments (80). In $f p _ { 4 }$ there are not enough shipments.

## 5. Extensions

A Linear Programming (LP) problem can be solved in polynomial time while an IP problem is NP complete [23,35]. Therefore, it may be interesting to consider the

![](/api/attachments/895BF3GW/fulltext/images/66ea424ed400567e3c46be417d30db16705b8b7c61d52941b45cee3c166a983f.jpg)  
Fig. 7. A Petri net modeling the processing of customer orders and four frequency profiles.

LP relaxation of $I P ( P N , M , f p )$ . We expect that in some cases this will provide good results. Note that often the rounded LP relaxation provides a feasible but nonoptimal solution (but not always, cf. the example net shown on page 269 in [6]). Since the objective function is of less interest, this is not a problem. Also note that if the IP problem has a solution the LP problem will also have a solution. Therefore, Theorem 1 also holds for the LP relaxation. As a result the LP problem can be used to quickly point out discrepancies between the process model and the frequency profile.

The LP relaxation is also interesting if the frequency profile is not exact or if we want to abstract from exceptions, i.e., if we consider noise we are not interested in the exact number of firings but in an approximate number. Suppose we want to allow a margin of 10 percent. To specify this we replace the first constraint in Definition 3 $( f _ { t } { = } f p ( t ) )$ by two weaker constraints: $f _ { t } { \ge } 0 . 9 f p ( t )$ and $f _ { t } \leq 1 . 1 f p ( t )$ . Such approximations are also needed if we collect data for a limited period with an unknown number of tokens in the initial marking.

Definition 4. Let (PN, M) be a marked Petri net with $P N { = } ( P , T , F ) , f p { \in } T { \not  } \mathrm { I N }$ a frequency profile, and α the noise level $( 0 \leq \alpha \leq 1 )$ . The corresponding LP (IP) problem allowing for α noise:

$$
\begin{array}{l l} \min \sum_ {t \in T} f _ {t} \\ \text {s.t.} f _ {t} \geq (1 - \alpha) f p (t) & \text {for all} t \in d o m (f p) \\ f _ {t} \leq (1 + \alpha) f p (t) & \text {for all} t \in d o m (f p) \\ f _ {(t, p)} = f _ {t} & \text {for all} (t, p) \in F \cap (T \times P) \\ f _ {(p, t)} = f _ {t} & \text {for all} (p, t) \in F \cap (P \times T) \\ M (p) + \sum_ {t \in p} f _ {(t, p)} - \sum_ {t \in p} f _ {(p, t)} \geq 0 & \text {for all} p \in P \\ f _ {t} \geq 0 & \text {for all} t \in T \\ f _ {t} \quad (\text {integer}) & \text {for all} t \in T \\ f _ {(x, y)} \quad (\text {integer}) & \text {for all} (x, y) \in F \end{array}
$$

Note that Definition 4 defines both an LP and and IP problem. The only difference is that for the LP problem the variables do not need to be integers.

Definition 4 allows for the application of our approach in the context of noise. Moreover, it can also resolve issues such as partial or inaccurate knowledge of the initial marking. However, we would also like to point at the fact that the addition of source and sink transitions can be used to make the whole approach more robust (cf. beginning of Section 3).

Another extension is the situation where multiple transitions refer to the same event, e.g., in SAP multiple functions in the EPC may generate the same transaction. This corresponds to a labeled Petri net with multiple transitions having the same label. Again this is easy to incorporate in the IP problem. The frequency profile is no longer a mapping from transitions to frequencies but from transition labels to frequencies and the first constraint should be replaced as indicated below.

Definition 5. Let (PN, M) be a marked Petri net with $P N { = } ( P , T , F )$ , L a set of labels, $l a b \in T \not \to L$ a labeling function, and $f p \in L \not \to \mathrm { I N }$ a frequency profile. The corresponding IP problem is:

$$
\begin{array}{l l} \min \sum_ {t \in T} f _ {t} \\ \text { s.t. } \quad \sum_ {t \in \operatorname{dom} (l a b) \mid l a b (t) = l} f _ {t} = f p (l) & \text { for   all } l \in L \\ f _ {(t, p)} = f _ {t} & \text { for   all } (t, p) \in F \cap (T \times P) \\ f _ {(p, t)} = f _ {t} & \text { for   all } (p, t) \in F \cap (P \times T) \\ M (p) + \sum_ {t \in p} f _ {(t, p)} - \sum_ {t \in p} f _ {(p, t)} \geq 0 & \text { for   all } p \in P \\ f _ {t} \geq 0 & \text { for   all } t \in T \\ f _ {t} \quad \text { integer } & \text { for   all } t \in T \\ f _ {(x, y)} \quad \text { integer } & \text { for   all } (x, y) \in F \end{array}
$$

All results given in Section 3 can be extended to labeled Petri nets.

Note that Definitions 4 and 5 can be combined. These extensions show that the formulation in terms of an LP/ IP problem is easy to refine or extend.

## 6. Application in the context of SAP

The problem addressed in this paper applies to a wide variety of systems. However, the first time we were confronted with this phenomenon was when we started to apply process mining in the context of SAP R/3 [10,15]. Given the widespread use of SAP, this has been the main motivation for the research reported in this paper. Based on a detailed analysis of the various SAP logs we discovered that there is no event log that allows for the type of log as shown in Table 1 [32]. There are two reasons why we have been unable to obtain references to case identifiers in SAP R/3. First of all, most logs only cover a small part of the SAP system, e.g., just the workflow module. Second, the logging facilities in SAP R/3 at a system-wide scope can be linked to transaction codes but not to individual cases.

This section will show that the approach described in this paper can be applied in the context of SAP R/3. We will show this in two steps. First, we show that the SAP logs allow for the discovery of a frequency profile $f ( p .$ Second, we show that it is possible to obtain predefined process models (i.e., models of a descriptive or prescriptive nature) and map them onto Petri nets.

![](/api/attachments/895BF3GW/fulltext/images/4c6ea3fb8e25a2dfb3557eeac9fe5b41605f984270735cad8d753ec862d58a30.jpg)  
Fig. 8. A screenshot of the SAP R/3 transaction monitor (ST03).

## 6.1. Obtaining a frequency profile in SAP

If we look at a logging facility in SAP R/3 with a system-wide scope, then the so-called transaction monitor<sup>5</sup> is the most obvious candidate to start. Every transaction that is executed is stored in the transaction monitor together with some basic information as is shown in Fig. 8. Transaction codes can be linked to concrete activities and also information such a timestamp, originator, etc. are supplied. As indicated, there is no way to link transactions in the transaction monitor to cases. Therefore, classical process mining techniques do not apply. Fortunately, it is possible to obtain a frequency profile as shown in Fig. 8. The first column on the right gives the transaction code (Tcode) and the second column gives the frequency (Dialog steps). As shown it is possible to refine the frequency into a frequency for every user (see smaller window).

Instead of directly using the ST03 transaction monitor, one can also use the Reverse Business Engineer (RBE). RBE is a tool for analyzing run-time SAP R/3 data. RBE is based on transaction frequencies and provides a more convenient way to obtain the information needed.

We also tried to use a completely different approach using the so-called document flows. SAP R/3 contains thousands of tables and an activity in some process often generates a record in a specific table. The problem is that these tables are linked and a-priori knowledge about the relations between these tables is needed to link the addition of a record to a concrete case. For example, when a purchase requisition is entered into SAP R/3 (via transaction code ME51), a new record is added to the purchase requisition table EBAN. The purchase requisition is uniquely identified by the purchase requisition number (BANFN). However, if for the same case a purchase order is created (via transaction code ME21), this purchase order results in the addition of a record in the purchasing table EKKO without a link to the purchase requisition number (BANFN). However, the record in the EBAN will get a pointer to the corresponding record in the EKKO table. An approach based on document flows requires knowledge of the underlying database. Therefore, it can only be supported for specific processes [32]. In fact, the ARIS PPM tool [11] of IDS Scheer provides a kind of process mining for some of the (hard-coded) SAP processes.

To summarize: it is possible to derive the transaction frequencies for fp but there is no way to link transactions to cases in a generic manner.

## 6.2. Obtaining a process model in SAP

The approach presented in this paper not only requires a frequency profile fp, it also needs an explicit process model PN expressed in terms of a Petri net. Fortunately, SAP has a comprehensive reference model including more than 4000 entity types and more than 1000 business processes and inter-organizational business scenarios [4,15]. These models describe the functionality of SAP and can be used to understand and/or configure the system. Given the nature of this paper, we focus on the reference models expressed in the so-called Event-driven Process Chains (EPCs) [14,15]. Fig. 9 shows a screenshot of ARIS showing a fragment of a reference model.

An EPC consists of three main elements. Combined, these elements define the flow of a business process as a chain of events. The elements used are:

\- Functions, which are the basic building blocks. A function corresponds to an activity (task, process step) which needs to be executed. A function is drawn as a box with rounded corners.

\- Events, which describe the situation before and/or after a function is executed. Functions are linked by events. An event may correspond to the position of one function and act as a precondition of another function. Events are drawn as hexagons.

\- Connectors, which can be used to connect functions and events. This way, the flow of control is specified. There are three types of connectors: ∧ (and), × (xor) and ∨ (or). Connectors are drawn as circles, showing the type in the center of the circle.

Functions, events and connectors can be connected with edges in such a way that (i) events have at most one incoming edge and at most one outgoing edge, but at least one incident edge (i.e. an incoming or an outgoing edge), (ii) functions have precisely one incoming edge and precisely one outgoing edge, (iii)

![](/api/attachments/895BF3GW/fulltext/images/c960ab6126b4d08d01d35ddbad3e92382fe23abe059271b8a891a4d5367ebeef.jpg)  
Fig. 9. A screenshot of a SAP reference model in ARIS for mySAP. The purchase requisition EPC is shown on the left and right half is used to navigate this EPC and other SAP reference models.

![](/api/attachments/895BF3GW/fulltext/images/dbaf4e69c5e7d001829dfd486d204a46ecb245bfdfe6815d626cd5d9f72b598f.jpg)  
Fig. 10. The application of the approach in the context of SAP.

connectors have either one incoming edge and multiple outgoing edges, or multiple incoming edges and one outgoing edge, and (iv) in every path, functions and events alternate.

Fig. 9 shows part of a bigger EPC. The left window shows four events, three functions, and one connector. The connector is a xor-split (denoted by the × symbol). The three functions are non-atomic, i.e., they can be further decomposed. There are several approaches to map an EPC onto a Petri net. In this paper we will not elaborate on this, because this is far from trivial and, depending on the EPC, this can only be partly automated. Instead we refer to only a few of the many papers on this topic [26,5,31,16]. Moreover, we would like to emphasize that in the context of the ProM framework there is a plug-in to translate an EPC into a Petri net [31].

Functions in the SAP reference model can be linked to the SAP transaction codes. For example, ARIS for mySAP shows the transaction codes of functions that can be directly linked to SAP. This mapping is partial, but our approach does not require a full mapping. (Note that $f p \in T { \not \to }  { \mathbb { N } }$ is a partial function.)

Using the SAP reference model and the transaction monitor (or RBE) we can deduce in a number of steps the frequency profile fp and process model PN. However, we cannot deduce the initial marking without more knowledge of the SAP system. Fortunately, as shown in Section 5, there are ways to work around the problem. By observing the process over a longer period of time and allowing for a noise level, the initial marking becomes of less importance.

## 6.3. SAP example

Let us consider the fragment of the invoice verification process to illustrate the overall approach in SAP. Fig. 10 shows a fragment of the process in terms of an EPC. We focus on the four functions in this EPC fragment. For convenience these functions have been renamed to $a , b , c ,$ and d. Using the transaction monitor (ST03) or RBE we can obtain the frequencies of the corresponding transactions. The upper half of the diagram refers to the information obtained from SAP and ARIS for mySAP. The lower half shows the translation into the notations used in this paper, i.e., the frequency profile fp and process model PN. Both can be translated into an IP problem using Definition 4, i.e., fp $( a ) = 5 6 , f p ( b ) = 8 7 6 , f p ( c ) = 3 2 3 , f p ( d ) = 1 2 7 8 ,$ , and PN as shown in Fig. 10. The initial marking of the place connecting a, b, c, and d can be assumed to be zero (of some better guess). If $\alpha { = } 0 . 0 5 $ , then $I P ( P N , M , f p )$ has a solution because $f p ( a ) + f p ( b ) + f p ( c ) = 1 2 4 6 \geq ( 1 - 0 . 0 5 )$ $f p ( d ) = 1 2 1 4 . 1$ . This suggests that the reference model and the frequency profile match. However, if fp(d) would have been substantially larger, e.g., 1500, the IP problem would not have had a solution thus indicating that both do not match.

## 7. Conclusion

Inspired by a problem encountered when applying process mining techniques to SAP transaction logs, the paper tackled the problem of checking whether a Petri net and a frequency profile match. An IP problem was proposed to efficiently implement a necessary but not sufficient condition. The approach allows for extensions not possible in the traditional linear algebraic approaches [17,6,24]. Clearly, the application is not limited to SAP transaction logs but is applicable in any situation where processes are only monitored at an aggregate level, i.e., frequency profiles rather than event traces.

Future research is aiming at a better characterization of the class of nets for which IP(PN, M, fp) has a solution if and only if match(PN, M, fp). In this paper, it was shown that for acyclic nets, marked graphs, and state machines this is the case. It seems that the characterizations given in [33] and the class of ST-nets (nets obtained by composing marked graphs and state machines) are a good starting point for a better understanding when solutions of the IP problem are actually realizable.

## Acknowledgments

The author would like to thank Eric Verbeek for proof-reading an early version of the paper and Monique Jansen-Vullers and Michael Rosemann for their joint work on mining SAP and configurable process models which uncovered the problem addressed in this paper. Moreover, Martijn van Giessel contributed with his Master thesis on mining SAP logs.

## References

[1] R. Agrawal, D. Gunopulos, F. Leymann, Mining Process Models from Workflow Logs, Sixth International Conference on Extending Database Technology, 1998, pp. 469–483.

[2] J. Becker, M. Kugeler, M. Rosemann (Eds.), Process Management: A Guide for the Design of Business Processes, Springer-Verlag, Berlin, 2003.

[3] J.E. Cook, A.L. Wolf, Discovering models of software processes from event-based data, ACM Transactions on Software Engineering and Methodology 7 (3) (1998) 215–249.

[4] T. Curran, G. Keller, SAP R/3 Business Blueprint: Understanding the Business Process Reference Model, Upper Saddle River, 1997.

[5] J. Dehnert, W.M.P. van der Aalst, Bridging the gap between business models and workflow specifications, International Journal of Cooperative Information Systems 13 (3) (2004) 289–332.

[6] J. Desel, Basic Linear Algebraic Techniques of Place/Transition Nets, in: W. Reisig, G. Rozenberg (Eds.), Lectures on Petri Nets I: Basic Models, Volume 1491 of Lecture Notes in Computer Science, SpringerVerlag, Berlin, 1998, pp. 257–308.

[7] J. Desel, J. Esparza, Free Choice Petri Nets, Volume 40 of Cambridge Tracts in Theoretical Computer Science, Cambridge University Press, Cambridge, UK, 1995.

[8] J. Desel, W. Reisig, G. Rozenberg (Eds.), Lectures on Concurrency and Petri Nets, Volume 3098 of Lecture Notes in Computer Science, Springer-Verlag, Berlin, 2004.

[9] J. Herbst, A Machine Learning Approach to Workflow Management, Proceedings 11th European Conference on Machine Learning, Volume 1810 of Lecture Notes in Compute Science, Springer-Verlag, Berlin, 2000, pp. 183–194.

[10] J. Hernandez, The SAP R/3 Handbook, 1997.

[11] IDS Scheer, ARIS Process Performance Manager (ARIS PPM): Measure, Analyze and Optimize Your Business Process Performance (whitepaper), IDS Scheer, Saarbruecken, Gemany, 2002, http://www.ids-scheer.com.

[12] M.H. Jansen-Vullers, W.M.P. van der Aalst, M. Rosemann, Mining Configurable Enterprise Information Systems, Data and Knowledge Engineering 56 (3) (2006) 195–244.

[13] N. Karmarkar, A new polynomial-time algorithm for linear programming, Combinatorica 4 (4) (1984) 373–396.

[14] G. Keller, M. Nüttgens, A.W. Scheer, Semantische Processmo dellierung auf der Grundlage Ereignisgesteuerter Processketten (EPK), Veröffentlichungen des Instituts für Wirtschaftsinforma tik, Heft 89 (in German), University of Saarland, Saarbrücken, 1992.

[15] G. Keller, T. Teufel, SAP R/3 Process Oriented Implementation, Addison-Wesley, Reading MA, 1998.

[16] E. Kindler, On the Semantics of EPCs: A Framework for Resolving the Vicious Circle, in: J. Desel, B. Pernici, M. Weske (Eds.), International Conference on Business Process Management (BPM 2004), Volume 3080 of Lecture Notes in Computer Science, Springer-Verlag, Berlin, 2004, pp. 82–97.

[17] T. Murata, Petri nets: Properties, analysis and applications, Proceedings of the IEEE 77 (4) (April 1989) 541–580.

[18] W. Reisig, Petri Nets: An Introduction, Volume 4 of EATCS Monographs in Theoretical Computer Science, Springer-Verlag, Berlin, 1985.

[19] W. Reisig, G. Rozenberg (Eds.), Lectures on Petri Nets I: Basic Models, Volume 1491 of Lecture Notes in Computer Science, Springer-Verlag, Berlin, 1998.

[20] M. Rosemann, Application Reference Models and Building Blocks for Management and Control (ERP Systems), in: P. Bernus, L. Nemes, G. Schmidt (Eds.), Handbook on Enterprise Architecture, Springer-Verlag, Berlin, 2003, pp. 596–616.

[21] M. Rosemann, W.M.P. van der Aalst. A Configurable Reference Modelling Language. QUT Technical report, FIT-TR-2003-05, Queensland University of Technology, Brisbane (In press in Information Systems).

[22] M. Sayal, F. Casati, U. Dayal, M.C. Shan, Business Process Cockpit, Proceedings of 28th International Conference on

Very Large Data Bases (VLDB'02), Morgan Kaufmann, 2002, pp. 880–883.

[23] A. Schrijver, Theory of Linear and Integer Programming, John Wiley & Sons, New York, 1998.

[24] M. Silva, E. Teruel, J.M. Colom, Linear Algebraic and Linear Programming Techniques for the Analysis of Place/ Transition Net Systems, in: W. Reisig, G. Rozenberg (Eds.), Lectures on Petri Nets I: Basic Models, Volume 1491 of Lecture Notes in Computer Science, Springer-Verlag, Berlin, 1998, pp. 309–373.

[25] W.M.P. van der Aalst, The application of Petri nets to workflow management, The Journal of Circuits, Systems and Computers 8 (1) (1998) 21–66.

[26] W.M.P. van der Aalst, Formalization and verification of eventdriven process chains, Information and Software Technology 41 (10) (1999) 639–650.

[27] W.M.P. van der Aalst, M. Song, Mining Social Networks: Uncovering Interaction Patterns in Business Processes, in: J. Desel, B. Pernici, M. Weske (Eds.), International Conference on Business Process Management (BPM 2004), Volume 3080 of Lecture Notes in Computer Science, Springer-Verlag, Berlin, 2004, pp. 244–260.

[28] W.M.P. van der Aalst, B.F. van Dongen, J. Herbst, L. Maruster, G. Schimm, A.J.M.M. Weijters, Workflow mining: A survey of issues and approaches, Data and Knowledge Engineering 47 (2) (2003) 237–267.

[29] W.M.P. van der Aalst, A.J.M.M. Weijters, L. Maruster, Workflow mining: discovering process models from event logs, IEEE Transactions on Knowledge and Data Engineering 16 (9) (2004) 1128–1142.

[30] B. van Dongen, A.K. Alves de Medeiros, H.M.W. Verbeek, A.J. M.M. Weijters, W.M.P. van der Aalst, The ProM framework: A New Era in Process Mining Tool Support, in: G. Ciardo, P. Darondeau (Eds.), Application and Theory of Petri Nets 2005, Volume 3536 of Lecture Notes in Computer Science, Springer-Verlag, Berlin, 2005, pp. 444–454.

[31] B.F. van Dongen, W.M.P. van der Aalst, H.M.W. Verbeek, Verification of EPCs: Using Reduction Rules and Petri Nets, in: O. Pastor, J. Falcao e Cunha (Eds.), Proceedings of the 17th Conference on Advanced Information Systems Engineering (CAiSE'05), Volume 3520 of Lecture Notes in Computer Science, Springer-Verlag, Berlin, 2005, pp. 372–386.

[32] M. van Giessel. Process Mining in SAP R/3. Master's thesis, Eindhoven University of Technology, Eindhoven, 2004.

[33] K. van Hee, N. Sidorova, M. Voorhoeve, Soundness and Separability of Workflow Nets in the Stepwise Refinement Approach, in: W.M.P. van der Aalst, E. Best (Eds.), Application and Theory of Petri Nets 2003, Volume 2679 of Lecture Notes in Computer Science, Springer-Verlag, Berlin, 2003, pp. 335–354.

[34] A.J.M.M. Weijters, W.M.P. van der Aalst, Rediscovering workflow models from event-based data using Little Thumb, Integrated Computer-Aided Engineering 10 (2) (2003) 151–162.

[35] L.A. Wolsey, Integer Programming, John Wiley & Sons, New York, 1998.

[36] M. zur Mühlen, M. Rosemann, Workflow-based Process Monitoring and Controlling-Technical and Organizational Issues, in: R. Sprague (Ed.), Proceedings of the 33rd Hawaii International Conference on System Science (HICSS-33), IEEE Computer Society Press, Los Alamitos, California, 2000, pp. 1–10.

![](/api/attachments/895BF3GW/fulltext/images/41588bce3206bc2f4065d6cedd7dfd0a86cf1ae0f137d82a1321cf36c051cbd8.jpg)

Wil van der Aalst is a full professor of Information Systems and head of the Information Systems department of the Faculty of Technology Management at Eindhoven University of Technology. Currently he is also an adjunct professor at Queensland University of Technology (QUT) working within the Centre for Information Technology Innovation (CITI). His research interests include information systems, simulation, process mining, Petri nets, process models, workflow manage-

ment systems, verification techniques, enterprise resource planning systems, computer supported cooperative work, and interorganizational business processes.
