---
otero_id: 16908
otero_key: "4MUHXUNX"
title: "A logic programming framework for planning and simulation"
authors: "Ronald M Lee; Louis W Miller"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90117-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Logic Programming Framework for Planning and Simulation

Ronald M. LEE \* and Louis W. MILLER \*\*
\* University of Texas, Graduate School of Business, Information Systems Group, Austin, TX 78712, USA and \*\* RAND Corporation

Planning and simulation models share the characteristic that they involve reasoning about hypothetical sequences of activities. These may be naturally described in a graph structure, e.g., a state transition diagram or a Petri net. A logic programming framework is proposed for describing the problem domain ('model base') of planning and simulation problems in logical form, separate from the inferencing mechanisms applied to them. Applications are to dynamic programming, decision trees, PERT networks, and discrete event simulation.

Keywords: Logic Programming; Planning; Simulation; Dynamic Programming; Decision Trees; PERT; Petri Nets

![](/api/attachments/4MUHXUNX/fulltext/images/c56995fd4af4786db032c6ed30368d710650ca7c5f16a434aa855fbc30b188cd.jpg)

Louis Miller heads the Rand Corporation's Information Sciences Department. The work reported here was done as a member of the faculty of the Decision Sciences Department at the Wharton School of the University of Pennsylvania. With interests in operations research and decision support systems, he has had extensive experience in policy analyses related to logistics systems and natural disasters. Dr. Miller is coauthor of Theory of Scheduling (Addison-Wesley, 1967)

and Disaster Insurance Insurance Protection: Public Policy Lessons (Wiley, 1978).

![](/api/attachments/4MUHXUNX/fulltext/images/e29c03c4fb295b028e48fea1c9b325de2fce20978938fe400644fdbb6e85bb8d.jpg)

Ronald M. Lee is presently a member of the Information Systems Group at the Graduate School of Business, University of Texas, Austin, TX 78712, USA. Formerly, he held a research position at the International Institute of Applied Systems Analysis (IIASA), Laxenburg, Austria. He has also held faculty positions at the New University of Lisbon, Portugal, and at Washington University, St. Louis, MO. Doctoral work was at the Department of Decision Sciences, The Wharton

School, University of Pennsylvania.

## 1. Introduction

Logic programming, including languages like Prolog and its variants, is becoming popular for AI applications such as database inferencing, natural language processing, expert systems, and a variety of others $[1,2,3,4]$ . Here we explore the use of logic programming in building models for management decision aiding; specifically, in building planning and simulation models.

A key advantage of the declarative orientation in logic programming is the ease in separating the problem specification (the ‘knowledge’ or ‘model base’) from the inference machinery to process it. Thus, the role of semantic modeling constructs is emphasized.

Planning and simulation models share the characteristic that they involve reasoning about hypothetical sequences of activities. Activities take time (i.e., they have a temporal duration) and they transform the world from one state to another. In doing so, they may consume resources, e.g., incur costs, require the usage of a machine or labor, etc.

A simple form of planning model might therefore be described as a state transition diagram, with transitions corresponding to activities. The output of the model is a sequence of states (or activities) from a given start state to a certain goal state.

A simulation model may also be described as a state transition diagram, again with activities corresponding to states. In a simulation; however, there is a transition back from the goal state to the start state, so that the processing of the model may cycle through repeated iterations.

More sophisticated planning and simulation models differ from this basic structure in several ways:

\- Choice of activities: A planning model may be directed to simply find a sequence of activities to reach the desired goal. This is a satisficing model. Alternatively, if activities are marked with some metric of performance, e.g. cost, the model can find an optimum (least cost) plan.

```prolog
/* model base */
/* goat alone with cabbage */
infeasible(s(1,0,0,_)).
infeasible(s(0,1,1,_)).
/* goat alone with wolf */
infeasible(s,(1,0,_0)).
infeasible(s(0,1,_1)).
```

\- Concurrency: In many situations, activities may be undertaken concurrently. Examples of models that reflect this characteristic are PERT and discrete event simulations. In this case, the nodes of the diagram are re-interpreted as transitions between sets of activities: A PERT diagram is a partial ordering of activities.

\- Choice of concurrency combined:

A representation that includes both choice and concurrency is a Petri net (e.g., [6]). Two types of nodes are involved:

a. Choice nodes, which indicate an exclusive choice between activities; and

b. ‘Transition’ nodes, which mark the termination and beginning of concurrent activities.

\- Role of probability

a. Probability on choices: In some situations: certain choices are determined exogenously, e.g., the behavior of a competitor, or the reaction of the marketplace. This may be indicated by marking the transitions from a choice node with the estimated probability that it will be taken. Decision trees are examples of state transition diagrams including probabilistic choice.

b. Stochastic aspects of activities: Generally, the motivation for modeling a situation using simulation is that the characteristics of the activities themselves are uncertain. Most commonly, the duration of the activity is taken to be a random variable, e.g., drawn from an exponential distribution.

These various aspects are consolidated in Table 1. While the model in each box might be either a planning or a simulation model, planning models seem more appropriate where choice is the dominant characteristic, whereas simulation seems more appropriate when stochastic concurrency dominates.

Table 1

<table><tr><td rowspan="2">Choice</td><td colspan="3">Concurrency</td></tr><tr><td>None</td><td>Deterministic duration</td><td>Probabilistic duration</td></tr><tr><td>None</td><td>Linear sequence</td><td>PERT</td><td>Discrete event simulation</td></tr><tr><td>Deterministic</td><td>State transition diagram</td><td>Petri net</td><td>Simulation with choice</td></tr><tr><td>Probabilistic</td><td>Decision tree</td><td>and/or Decision tree</td><td>Simulation with probabilistic choice</td></tr></table>

## 2. Searching a State Transition Graph - Example

A farmer needs to ferry a goat, a (very large) cabbage and his pet wolf across a river. The only available boat holds only the farmer and one passenger (the cabbage counts as a passenger). The goat cannot be left alone with the cabbage, and the wolf cannot be left alone with the goat. The problem is to devise a plan for transporting all four across the river [4].

This is a simple planning problem that can be easily modeled as a sequence of states and transitions. A state might be described by four binary variables for example:

s(F, G, C, W).

indicating whether each of the individuals is on the near side (0) or far side (1). There are thus 16 possible states. However, some states are not allowed. We indicate this in the form of explicit infeasibility assertions:

```txt
/* possible transitions between states */
```

trans(s(0,G,C,W),s(1,G,C,W), 'farmer goes alone'). trans(s(0,0,C,W),s(1,1,C,W), 'farmer takes goat'). trans(s(0,G,0,W),s(1,G,1,W), 'farmer takes cabbage').

```prolog
trans(s(0,G,C,0),s(1,G,C,1), 'farmer takes wolf').
```

These transitions are bi-directional, i.e., one can go from the first state to the second state or vice versa.

These assertions constitute the ‘model base’ for this problem. This essence of this problem type is that it involves a search through a state space, with choices available as to which transition to take. A solution amounts to finding a sequence (list) of states with no repetitions (a state is never re-visited), and not traversing any infeasible states. The additional Prolog rules needed to do this are as follows:

(farmer takes goat,to far side),
(farmer goes alone,to near side),
(farmer takes wolf,to far side),
(farmer takes goat,to near side),
(farmer takes cabbage,to far side),
(farmer goes alone,to near side),
(farmer takes goat,to far side)];

## 3. Dynamic Programming

In the above example, there was no metric of goodness for a particular solution. Any solution would do. By adding a cost factor to the transitions, the problem becomes a candidate for optimization, e.g. by a dynamic programming algorithm. For example, suppose the state space is given by the (directed) graph in Figure 1.

This state transition diagram is represented by the following assertions:

/\* model base \*/

trans(a,b,1).

![](/api/attachments/4MUHXUNX/fulltext/images/a4c011cdd46b484b1dcb5428982560423f76a7a6ed61880135c1fe34e046fa85.jpg)  
Figure 1

```prolog
trans(a,c,3).
trans(b,d,5).
trans(b,e,2).
trans(c,e,7).
trans(c,f,4).
trans(d,g,1).
trans(e,g,4).
trans(e,h,1).
trans(f,h,2).
trans(g,i,3).
trans(h,i,2).
```

A recursive search through such a state space is as follows:

```prolog
/* logic program */
dynamic(X, Z, [X | L], Cost) :- 
dynamlan(X, Z, L, Cost).
dynamlan(X, X, [], 0).
dynamlan(X, Z, LL, TC) :- 
    setof((K, [Y | L]), (C, CC)^(trans(X, Y, C), dynamlan(Y, Z, L, CC), K is C + CC), SS), minof(SS, (TC, LL)).
```

Comments: ‘setof’ is a built-in predicate that returns a list of tuples selected from the database; ‘minof’ is an auxiliary predicate that finds the minimum element in a list.

## 4. Decision Trees

A decision tree is another form of state space search solvable in dynamic programming fashion.

In this case, there are two types of nodes: choice nodes (drawn as circles) and 'outcome' nodes (drawn as diamonds). Choice nodes indicate choices to be made by the decision maker of planning algorithm; each arc emerging from a choice node has an associated cost for that alternative. Outcome nodes indicate choices made external to the model, represented as probabilities on the transitions. A simple decision tree (graph) is presented in Figure 2.

```prolog
/* model base */
/* transitions from choice nodes */
xtrans(a,b,20).
xtrans(a,c,40).
xtrans(d,g,10).
xtrans(d,h,30).
xtrans(e,h,25).
xtrans(e,i,50).
```

![](/api/attachments/4MUHXUNX/fulltext/images/9302646e2ec000d157ff07aefcc09059f8cbfa8ea70ecf7e67be842925fe5767.jpg)  
Figure 2

```prolog
xtrans(f,i,25).
xtrans(f,j,15).

/* transitions from outcome nodes */

ptrans(b,d,.5).
ptrans(b,e,.5).
ptrans(c,e,.3).
ptrans(c,f,.7).
ptrans(g,k,.2).
ptrans(g,1,.8).
ptrans(h,1,.1).
ptrans(h,m,.9).
ptrans(i,m,.4).
ptrans(i,n,.6).
ptrans(j,n,.5).
ptrans(j,o,.5).

/* values of final 'result' nodes */

result(k,100).
result(1,200).
result(m,300).
result(n,250).
result(o,150).

The expected value of a given node can be found by the following recursive predicate:

/* logic program */

val(X,V) :- result (X,V).

val(X,V) :-
bagof(M, (Y,P,K)^(ptrans(X,Y,P), val(Y,K), M is K*P),L),
sumof(L,V).

val(X,V) :- bestchoice(X,Z,V).

bestchoice(X,Z,V) :-
bagof((M,Y), choice(X,Y,M), L),
maxof(L, (V,Z)).

choice(X,Y,M) :- xtrans(X,Y,C), val(Y,K), M is K - C.

Alternatives and their expected values at a give choice node are given by the predicate, 'choice', for example:

/* sample execution */

?- choice(a,Y,M).

Y = b M = 25;
Y = c M = 23

The best alternative at a given choice node is given
```

by 'bestchoice', e.g., ?- bestchoice(A,Z,V).

## 5. State Space Simulation

State transition diagrams may also provide the knowledge base for a simulation model. In this case, the final state in the graph has a transition cycling back to the start state. Such simulations are usually only interesting, however, when there are stochastic aspects involved, for instance, exponentially distributed activity times.

For example, consider a simple case where the system has only two states, s0 and s1, having two activities, (s0,s1) and (s1,s0), whose durations are exponentially distributed with means 10 and 20 respectively. The system is diagrammed in Figure 3.

This system is described by the following transition assertions:

```prolog
/* model base */
trans(s0,s1,X) :- eran(X,10).
trans(s1,s0,X) :- eran(X,20).
```

Here, ‘eran(X,M)’ is a built-in predicate returning exponential variates, X, having a mean of M. The basic logic for a simulation of this system is as follows:

```prolog
/* logic program */
cycle(T0,X) :-
    trans(X,Y,DT),
    T1 is T0 + DT,
    cycle(T1,Y).
```

This program merely follows the state transition graph, updating the current time after each transition. Using the Prolog 'spy' for tracing, its behav-

![](/api/attachments/4MUHXUNX/fulltext/images/2ff603b71b8893f763932846a2a84a5abc874a5379a1503630d33ee3b9b34d57.jpg)  
Figure 3

```txt
ior is as follows:
/* sample execution */
?- cycle(0,s0).
** 0 Call : cycle(0,s0)
** 1 Call : cycle(16,s1)
** 2 Call : cycle(22,s0)
** 3 Call : cycle(26,s1)
** 4 Call : cycle(48,s0)
** 5 Call : cycle(70,s1)
```

Note that the ‘cycle’ predicate does not do any data collection, nor does it have a termination condition. A more sophisticated version with these features added is the following:

```prolog
/* logic program */
go(L) :- sim(s0,100,0,[],L).
sim(X,Q,T,L,L) :- T >= Q,!. 
sim(X,Q,T0,L,LL) :- trans(X,Y,DT),
    update(Y,DT,L,W),
    T1 is T0 + DT,
    sim(Y,Q,T1,W,LL).
update(Y,DT,[(Y,T0)|L],[(Y,T1)|L]) :- T1 is T0 + DT, !.
update(Y,DT,[],[(Y,DT)]) :- !.
update(Y,DT,[Z|L],[Z|W]) :- update (Y,DT,L,W).
/* sample execution */
?- go(L).
L = [(s1,34),(s0,66)];
?-go(L).
~L = [(s1,31),(s0,103)];
etc.
```

An implementation consideration: doing the iterations of the simulation using recursive logic will eventually cause an overflow in the stack space using the Prolog interpreter. However, most compilers now support 'tail recursion optimization', which recognizes deterministic uses of recursion (where there are no backtracking alternatives) and does not accumulate stack space. Thus, in compiled form, the above logic programs run efficiently for an arbitrary number of iterations.

A slightly more elaborate situation might involve choice between the transitions to be taken, for instance the least cost activity. An example is the state transition diagram in Figure 4.

This is incorporated into the previous structure if we call the basic transitions, e.g., 'xtrans', adding a cost parameter, and re-code the 'trans' assertions to pick the minimum cost alternative (assume all times are exponentially distributed with a mean of 10):

/\* model base \*/

xtrans(s0,s1,3,X) :- eran(X,10).

xtrans(s0,s2,4,X) :- eran(X,10).

xtrans(s1,s0,2,X) :- eran(X,10).

xtrans(s2,s0,1,X) :- eran(X,10).

trans(X,YY,TT) :-

setof((C,Y,T),xtrans(X,Y,C,T),L),

minof(L, (CC,YY,TT)).

Elaborating the States

In the farmer example earlier, states were not given individual names (s0,s1,...), but rather were identified in terms of more elementary components, e.g., the position of the farmer, the goat, etc.. The same approach can be applied to simulation modeling. For example, suppose a simple case of two machines in sequence, controlled by a single operator. Thus, each machine must wait while the other is processing. A sketch of the system is presented in Figure 5.

This is described in ‘trans’ assertions like the following:

/\* model base \*/

trans(s([(m1,busy),(m2,wait)]),

s([(m1,wait),(m2,busy)]), X) :- eran(X,5).

trans(s([(m1, wait), (m2, busy)]).

s([(m1,busy),(m2,wait)]), X) :- eran (X,3).

![](/api/attachments/4MUHXUNX/fulltext/images/e1b99a95e4e3c118a4d0f2d2f6ac0d7d3f5c5c1efbadb0e4321804731cbefb9e.jpg)  
Figure 4

![](/api/attachments/4MUHXUNX/fulltext/images/66630ada9c30ec7d05b8c0a5bd526b8d46379b15c02518a34411d1fd77860c49.jpg)

![](/api/attachments/4MUHXUNX/fulltext/images/769cba3df76b8d8eec512bdd016068fb541e95a8308f3c456909e59e45184ec4.jpg)

![](/api/attachments/4MUHXUNX/fulltext/images/a57861820b2c8715606c4997b229f5988f6a62d8ec01984f5f19f7c63456a398.jpg)  
Figure 5

![](/api/attachments/4MUHXUNX/fulltext/images/d561cb3de634d7049c4531916d4fb57e7a44859e9d68f71dbd29c379af2d58f9.jpg)

go(L) :- sim(s([(m1,busy), (m2,wait)]), 100,0,[],L).

/\* sample execution \*/

?- go (L).

$L = [(s[(m1, wait),(m2,busy)]),66),(s[(m1,busy),(m2,wait)]),36)]$

?- go(L).

$L = [(s([(m1,wait),(m2,busy)]),67),(s([(m1,busy),(m2,wait)]),37)]$

?- go(L).

$L = [(s[(m1,wait),(m2,busy)]),64),(s[(m1,busy),(m2,wait)]),39)]$

## 6. Concurrency of Activities - PERT

In many, indeed most, situations, activities occur concurrently. A planning model often used in these cases is a PERT diagram. A simple example is the plan for building a house in Figure 6.

In a PERT diagram, multiple arcs emanating from a node indicate not choice but rather concurrency of the indicated activities. Thus, work on the walls and the plumbing can proceed in parallel, once the foundation has been laid. Likewise, both the ceiling and electrical work can be done in parallel once the walls are done. All these must be completed before painting can begin.

Note that the nodes in a PERT diagram no longer represent states of the entire system (e.g., the construction of the house). Rather, they represent 'sub-states', indicating a momentary status of only part of the system. More commonly, the nodes are viewed as instantaneous transitions between two or more activities. The total state of the system is therefore given as the set of activities that are currently being performed. The above diagram is described by the following Prolog

![](/api/attachments/4MUHXUNX/fulltext/images/97abceb59be6dd6e97e7219bb46ea23f02e26f652a4bd8cefe881bced56be720.jpg)  
Figure 6

The critical path is found as the maximum length path of activities between two nodes:

## 7. Discrete Event Simulation

Concurrency of activities is also an important feature of many simulation models. A discrete event simulation may be characterized as a PERT diagram having cycles, that is, where sequences of activities repeat. For example, consider the PERT diagram in Figure 7.

As with other PERT diagrams, we note that the nodes in this graph no longer represent states. Rather, a state in this system is given by the set of

busy
walt-unload

![](/api/attachments/4MUHXUNX/fulltext/images/fc3857efeaaf189494d1e1c44fcdcdd14531a0220c62b95cc4d8a5abe567f223.jpg)  
Figure 7

activities currently active. Thus, it is the nodes, rather than the arcs, that mark transitions in the system. (PERT diagrams, more generally called 'marked graphs', are sometimes regarded as the graphical dual of state transition diagrams – see e.g. [6] p. 204.)

Representing the set of currently active activities as a list of pairs giving the activity and its scheduled completion time, the 'trans' assertions are as follows:

```prolog
/* model base */
start([(_,0,d)]).
/* node i */
trans(T,[(T, _,d)],[(Ta,T,a),(Tb,T,b)]) :- Ta is T + 5,
Tb is T + 2.
/* node j */
trans(T,[(T, _,b)],[(Tc,T,c)]) :- Tc is T + 1.
/* node k */
trans(T,[(T, _,a),(T, _c)],[(Td,T,d)]) :-Td is T + 3.
A logic program that performs the simulation
iterations is as follows:
/* logic program */
go :- start(L), bump(0,L).
bump(T0,L0) :-
    transit(T0,L0,T1,L1),
    bump(T1,L1).
transit(T,L0,T,L1) :-
    trans(T,WW,AA),
    remove(WW,L0,MM),
    append(AA,MM,L1).
transit(T0,L0,T1,[(_,T,A)|LL]) :-
    qsort(L0,[(T1,T,A)|LL]).
```

```javascript
/* sample execution */
?- go.
** 1 Call : bump(0,[(44,0,d)])
** 2 Call : bump(0,[(5,0,a),(2,0,b)])
** 3 Call : bump(2,[(_206,0,b),(5,0,a)])
** 4 Call : bump(2,[(3,2,c),(5,0,a)])
** 5 Call : bump(3,[(_556,2,c),(5,0,a)])
** 6 Call : bump(5,[(_683,0,a),(-556,2,c)])
** 7 Call : bump(5,[(8,5,d)])
** 8 Call : bump(8,[(_1071,5,d)])
** 9 Call : bump(8,[(13.8,a),(10,8,b)])
** 10 Call : bump(10,[(_1082,8,b),(13,8,a)])
** 11 Call : bump(10,[(11,10,c),(13,8,a)])
```

etc.

The addition of concurrency into the simulation introduces the problem of waiting: among concurrent activities, some will finish earlier, hence must wait for the others to complete. In the above program, when an activity is waiting, its scheduled completion time is left as an uninstantiated variable (noted in the spy trace as an underscore followed by an integer). Thus, there are actually two types of transitions ('transit') of the system – those given by the 'trans' assertions, and the completion of the next scheduled activity. (Note: 'qsort' orders the activity list from earliest to latest, with waiting activities sorted last.)

In the above example, waiting was represented implicitly as the time between the completion of one activity and the start of the next. However, often we would like to represent waiting explicitly, as a distinct arc type. A revised form of the program to do this is as follows:

```prolog
/* logic program */
go :- start(L), bump(0,L).
bump(T0,L0) :-
    write('.'),
    transit(T0,L0,T1,L1),
    bump(T1,L1).
transit(T,L0,T,L1) :-
    atrans(T,WW,AA),
    remove(WW,L0,MM),!,
    append(AA,MM,!,1).
transit(T,L0,T1,L1) :-
    qsort(L0,[(T1,T0,A)|LL]), 
    xtrans(T,[(T1,T0,A)],AA),
    append(LL,AA,L1).
```

Note that this version recognizes two types of transitions, ‘atrans’ and ‘xtrans’. An ‘atrans’ describes the node transitions between substates. An ‘xtrans’ permits the representation of waiting times as explicit activities. Here we assume that certain types of activities are ‘busy’, i.e., involving a definite action and with a scheduled completion time. Other activities are ‘waiting’, and their completion time is left as an uninstantiated variable. An ‘atrans’, corresponding to the previous ‘trans’ assertions, marks a transition from waiting to busy, whereas an ‘xtrans’ marks the completion of a busy activity, and the beginning of waiting. (Actually, the two are distinguished by their preconditions only: ‘atrans’ marks the end of waiting; ‘xtrans’ marks the end of busy. The post-conditions can be anything.)

The following example serves to illustrate. Again, there are two machines, m1 and m2, that operate in sequence. However, m2 can now operate concurrently with m1. As before, m1 is fed continuously, and m2 unloads its job with no delay. However, m2 must wait to be fed by the output of m1. The activities of m1 are thus busy or waiting to unload. The activities of m2 are busy and waiting to load. The configuration of the system is sketched in Figure 8.

This can be described by the PERT diagram in Figure 9.

This system is described by the following model base:

```prolog
/* model base */
start([_,0,act(m1,wu)), (_,0,act(m2,w1))]).
/* node a */
atrans(T, [(_,_,act(m1,wu)),(_,_,act(m2,w1))],
[(T1,T,act(m1,b)),(T2,T,act(m2,b))])
:- eran(X1,5), eran(X2,3),
T1 is X1 + T, T2 is X2 + T.
```

![](/api/attachments/4MUHXUNX/fulltext/images/b4207f5c13cda32034bd801ce542c10d1f8040e6d093eec24761d236e97ea286.jpg)  
Figure 8

![](/api/attachments/4MUHXUNX/fulltext/images/aa0a5a349af85a0b223aefd014a5f598bf3745ccc4bfa27d22f5967cebdb2123.jpg)  
Figure 9

/\* node b \*/

/\* node c \*/

xtrans(T, [(\_, \_, act(m1,b))], [(\_, T, act(m1,wu))]).

xtrans(T, [(\_, \_, act(m2,b))], [(\_, T, act(m2,w1))]).

Using the Prolog 'spy', the execution behavior of this system is as follows:

?- go.

\*\* 1 Call : bump(0,[(\_44,0,act(m1,wu)),(\_45,0,act(m2,w1))])
\*\* 2 Call : bump(0,[(8,0,act(m1,b)),(0,0,act(m2,b))])
\*\* 3 Call : bump(0,[(8,0,act(m1,b)),(\_558,0,act(m2,w1))])
\*\* 4 Call : bump(8,[(\_558,0,act(m2,w1)),(\_719,0,act(m1,wv))])
\*\* 5 Call : bump(8,[(21,8,act(m1,b)),(9,8,act(m2,b)])
\*\* 6 Call : bump(9,[(21,8,act(m1,b)),(\_1260,8,act(m2,w1))])
\*\* 7 Call : bump(21,[(\_643,8,act(m2,w1)),(\_804,9,act(m1,wv))])
\*\* 8 Call : bump(21,[(25,21,act(m1,b)),(22,21,act(m2,b))])
\*\* 9 Call : bump(22,[(25,21,act(m1,b)),(\_1345,21,act(m2,w1))])
\*\* 10 Call : bump(25,[(\_1345,21,act(m2,w1)),(\_1506,22,act(m1,wu))])
\*\* 11 Call : bump(25,[(44,25,act(m1,b)),(31,25,act(m2,b))])

## 8. Petri Nets

A PERT diagram conveys concurrency of activities, but does not indicate choice between alternative courses of action. A state transition diagram, by contrast, indicates choice, but not concurrency. A Petri net is a combination of these two. Two types of node are included: choice nodes (drawn as circles), analogous to the nodes in S-T graphs; and transition nodes (drawn as boxes), analogous to nodes in PERT graphs.

In drawing a Petri net diagram, activities are indicated as labels on choice nodes (circles). As before, transition nodes (boxes) represent an instantaneous transition between activities. The previous PERT diagram is re-drawn in Petri net notation in Figure 10.

To exemplify the modeling of choice in a Petri net, consider the following elaboration of the machine shop example. Assume there are now three machines, m1, m2 and m3. Again there are two phases to the processing: the first phase is done by machine m1; the second phase is done by either m2 or m3, depending on which is available first. Assume that processing times are exponentially distributed with means of 10, 30 and 15, respectively. The configuration of the system and activities of each machine is sketched in Figure 11. A Petri net diagram of the processing is presented in Figure 12.

The flow of processing in a Petri net is described by means of ‘tokens’ that flow through the network. Tokens may reside at choice nodes, also called ‘places’. A transition node ‘fires’ by removing a token from each of its input places and depositing a (new) token on each of its output places. The state of the system is given by the location of tokens at each of the various places. (We assume that a place can have at most one token; this assumption is sometimes relaxed.)

The previous simulation program remains essentially the same for simulating Petri nets. Transition nodes in the Petri net become 'trans' assertions in the logic program. As before, 'atrans' is used where the pre-conditions (here, input places) are waiting activities; 'xtrans' is used where the pre-conditions are busy activities. The above system is thus programmed as follows:

![](/api/attachments/4MUHXUNX/fulltext/images/bc19ef9aa862cbe0aae398834a1387bbb9c52255de176dd0c04549d245b8b759.jpg)  
Figure 10

![](/api/attachments/4MUHXUNX/fulltext/images/d946fe33c3109414fe3d5dfa9f9a2bf783ec9b90669c2f391d97c709863c8ddb.jpg)  
Figure 11

/\* model base \*/
start([0,0,act(m1,b)), (\_,0,act(m2,w1)), (\_,0,act(m3,w1))]).

/\* node a \*/

xtrans(T, [(\_, \_, act(m2,b))], [(\_, T, act(m2,w1))]).

/\* node b \*/

![](/api/attachments/4MUHXUNX/fulltext/images/56093c866bd11bd1a1cbe0dd5f5e45780957a4e6cf3ba55c4c3d388f8848054b.jpg)  
Figure 12

atrans(T, [(\_,\_,act(m1,wu)), (\_,\_,act(m2,w1))],
[(T1,T,act(m1,b)), (T₂,T,act(m2,b))])
:- eran(X1,10), eran(X2,30),
T1 is T + X1, T2 is T + X2.

/\* node c \*/

xtrans(T, [(\_-, \_, act(m1,b))], [(\_-, T, act(m1,wu))]).

/\* node d\*/

atrans(T, [(\_,\_,act(m1,wu)), (\_,\_act(m3,w1))],
[(T1,T,act(m1,b)), (T₃,T,act(m3,b))])
:- eran(X1,10), eran(X3,15),
T1 is T + X1, T3 is T + X3.

/\* node e \*/

xtrans(T, [(\_-, -,act(m3,b))], [(\_-, T, act(m3,21))]).

/\* sample execution \*/

?- go.

\*\* 1 Call : bump(0,
[(0,0,act(m1,b)),(\_44,0,act(m2,w1)),
(\_45,0,act(m3,w1))])

\*\* 2 Call : bump(0,
    [(\_44,0,act(m2,w1)),(\_45,0,act(m3,w1)),
    (\_251,0,act(m1,wu))])

\*\* 3 Call : bump(0,
[(22,0,act(m1,b)),(50,0,act(m2,b)),
(\_45,0,act(m3,w1))])

\*\* 4 Call : bump(22,
[(50,0,act(m2,b)),(\_45,0,act(m3,w1)),
(\_789,0,act(m1,wu))])

\*\* 5 Call : bump(22,
[(31,22,act(m1,b)),(31,22,act(m3,b)),
(50,0,act(m2,b))])

\*\* 6 Call : bump(31,
[(31,22,act(m3,b)),(50,0,act(m2,b)),
(\_805,22,act(m1,wu))])

\*\* 7 Call : bump(31,
[(50,0,act(m2,b)),(\_805,22,act(m1,wu)),
(\_1044,31,act(m3,w1))])

\*\* 8 Call : bump(31,
[(41,31,act(m1,b)),(60,31,act(m3,b)),
(50,0,act(m2,b))])

\*\* 9 Call : bump(41,
[(50,0,act(m2,b)),(60,31,act(m3,b)),
(\_1687,31,act(m1,wu))])

\*\* 10 Call : bump(50,
[(60,31,act(m3,b)),(\_1687,31,act(n1,wu)),
(\_1926,41,act(m2,w1))]

\*\* 11 Call : bump(50,
[(82,50,act(m1,b)),(72,50,act(m2,b)),
(60,31,act(m3,b))]

etc.

In this example, if both m2 and m3 are waiting, the choice defaults to m2, by the ordering of the rules.

## 9. Concluding Remarks

The preceding text contains seven logic programs. For expository reasons, these have ignored such necessary features as data collection and boundary conditions on the simulations. However, they are complete and operational in their basic inferential structure. This terseness and elegance is one of the most attractive features of logic programming. Another major attraction is its declarative form, which enables the separation of problem dependent assertions ('model base') from the inferencing structure ('logic program'). Thus the same problem domain may be analyzed using a variety of inferential techniques.

## Acknowledgements

We thank William Maxwell for many stimulating discussions about modeling automated factories, and Michael Zisman for introducing us to the usefulness of Petri nets as a modeling tool. We also gratefully acknowledge the Department of Decision Sciences, Wharton School, University of Pennsylvania, which provided the setting for the initial phases of this work.

## References

[1] Coelho, H., J.C. Cotta and L.M. Periera, How to Solve it in Prolog, 2nd Edn., Laboratorio Nacional de Engenharia Civil, Lisbon, Portugal (1980).

[2] Clark, K.L. and F.G. McCabe, Micro-Prolog: Programming in Logic, Prentice-Hall, Englewood Cliffs, NJ (1984).

[3] Clocksin, W.F. and C.S. Mellish, Programming in Prolog, 2nd edn., Springer-Verlag, New York (1985).

[4] Kowalski, R.A., Logic for Problem Solving, Elsevier/North Holland, Amsterdam (1979).

[5] Lee, R.M., Database Inferencing for Decision Support, Decision Support Systems, 1 (1985).

[6] Peterson, J.L., Petri Net Theory and the Modeling of Systems, Prentice-Hall, Englewood Cliffs, NJ (1981).
