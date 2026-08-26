---
otero_id: 21403
otero_key: "AJAQHAZM"
title: "Distributed decision support systems under limited degrees of competence: A simulation study"
authors: "Aldo Franco Dragoni"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00073-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Distributed decision support systems under limited degrees of competence: A simulation study

Aldo Franco Dragoni \*

University of Ancona, Computer Sciences Institute, via Brecce Bianche, 60131 Ancona, Italy

## Abstract

We report the results of a simulation experiment inspired by a popular board game. Nine agents are wandering, searching for clues to fill the three slots of a detective case. They have a limited perceptive capacity so that they can discern a clue badly. On meeting each others, agents exchange their current results. They can be insincere, i.e., they can provide false information to divert the others' investigations. Each agent is equipped with a same belief revision mechanism that makes them able to recognize and solve contradictions, assign a degree of credibility to each piece of information and assign a degree of reliability to each agent (itself included). The purpose of the experiment is that of evaluating the performances of the entire agency on the varying of the local strategies for belief revision and communication. © 1997 Elsevier Science B.V.

Keywords: Belief revision; Distributed cognition; Distributed decision making; Distributed artificial intelligence

## 1. Introduction

As the importance of computer networking increases, some tasks traditionally performed by a single workstation are being conceived as performable in a distributed manner by networks of interacting information systems. Even the task of supporting decisions could be regarded in such a way. The scenario we have in mind is that of a network of workstations, each running a Decision Support System (DSS) for its own user. The software on a single workstation cannot always accomplish its task without the contribution of the other DSSs. Sometimes this contribution could be harmful rather than helpful. Information coming from other DSSs could be damaging, for instance because:

1. local data available at the other DSSs may not be updated or truthful;

2. there can be some hardware faults at the other workstations;

3. there can be some mistakes in the architecture or software implementation of the other DSSs;

4. some nodes could join the network with non-co-operative intentions (may be destructive ones) and could supply incorrect information in order to induce wrong decisions;

5. even if the DSSs adopt standard protocol and syntax to exchange information, there can still be some semantic differences or ambiguities;

6. there can be noises on the communication channels.

We define as incompetent a DSS that is unreliable because of 1, 2 and 3, and we define as insincere a DSS that is unreliable because of 4. Items 5 and 6 regard communication. In this paper we will concentrate on the kinds of mistakes $1 \div 4$ , which can be ascribed to a single software/hardware agent. A symptom that some degree of incompetence and/or insincerity is insinuated into the network is the appearance of contradictions in the knowledge base of some DSSs. The ability of detecting contradictions, identifying the pieces of information that originated them, and readjusting the knowledge base to remove them, are important features to embed in a DSS. The complex of these operations is normally called 'Belief Revision'. However, in such a scenario, it is also very important to make the network able to detect the culprits for the wrong information, i.e., its unreliable member agents.

Belief Revision is a long standing debated argument in the community of Artificial Intelligence. Since the influential and seminal works of Gärdenfors et al. [1,17], the ideas have been progressively refined [18] and ameliorated toward normative, effective and computable paradigms [2,30,35]. However, in this Distributed Decision Support System (DDSS) scenario, nodes exchange knowledge and then make inferences based both on locally found and exchanged knowledge, so the belief revision task becomes especially problematic since agents must compute their beliefs locally, based also on beliefs communicated and justified externally. According to us, it becomes necessary to ‘enlarge’ the idea of belief revision in two directions.

1. For detecting contradictions and identifying the pieces of information from which they originated it is sufficient to maintain information about what has been told; but to properly 'solve' a contradiction it is necessary to keep information about who said it or, in general, about from where that information came! It could also come from certain or hypothetical information local to the reasoning agent [9]. The belief revision module in a DSS cannot leave the sources of the information out of the picture because of their relevance in giving the additional notion of 'strength of belief' [16]. In fact, the reliability of the source affects the credibility of the information and vice-versa.

It is necessary to develop systems that deal with couples $\langle piece of information, informant \rangle$ rather than with information alone.

2. In order to make practical the belief revision process, it is necessary, to not only make the system able to discard pieces of information after that new evidence contradicts it (non-monotonicity of belief revision [19]), but to also make the system able to recover previously discarded pieces of information after new evidence redeems it [12].

We have developed a tentative model for belief revision that tries to overcome these limitations, and we have incorporated it into a prototypical system for supporting detective inquiries $[10]$ . However, as the experiment that we report in this paper shows, a model for belief revision that behaves reasonably in a single-agent domain does not necessarily do the same in a distributed environment. We define ‘Distributed Belief Revision’ the study of how the adoption of a local model of belief revision and of local policies of communication affects each node’s opinions regarding what is more credible (among the various pieces of information) and who is more reliable (among the nodes with whom it got in touch) $[11]$ . In Distributed Belief Revision special questions arise that regard the global emergent epistemic behavior of the overall network; for instance:

\- Does the proposed (local) strategies for belief revision and communication assure the various nodes to converge gradually toward the same knowledge space?

\- If this global beliefs convergence is assured, how long will it take to achieve it?

\- Is it possible for the various nodes to detect those among themselves which are particularly unreliable?

\- If that is possible to what extent?; i.e., what happens if most of the nodes are largely unreliable?

\- Is the overall global network reliable?; i.e., does it converge to the most credible knowledge or not?,

\- Is it possible that a node realizes that it itself is unreliable? etc.

There have already been presented many different formalisms and algorithms to perform belief revision [1,2,4,5,7,8,10,14,17,18,21,22,24,25,27–32,35,39] and the problem of correlating the uncertainty of information to the reliability of its source is afforded in various ways [3,13,15,23,36–40]. Furthermore, we can adopt disparate reasonable policies of communication in order to make the nodes able to exchange information. A policy of communication should define when the communication takes place, what is communicated and to whom the communication is sent. There can also be various choices regarding the structure of the network: should all the nodes be equals or should there be some hierarchical structure; what kind of power have the superiors, should the structure be fixed or could it dynamically change (may be on a voting base), etc. Each of these choices will deeply affect the global performances of the network. The kind and the importance of these emergent effects can be evaluated only on a simulation basis. To compare the global features of different local strategies, we have developed CLUE, a testbed based on MICE [28], a specific tool for multiagent applications in which we can define various agents able to communicate with each other, perceive the environment, move in it and modify it. Inspiration for our specific testbed has come from CLUEDO $^{™}$ , a board game based on a detective story metaphor.

In this paper we report on the first experiment which lasted four months. We equipped each agent with the assumption based belief revision system derived from the one that we adopted for our Inquiry Support System $[10]$ . We assumed the network was not structured and we adopted some specific rules for communication. We also made two fundamental working assumptions.

1. Nodes do not communicate to the others the sources from which they received the pieces of information; they present themselves as completely responsible for the knowledge they are passing onto the others. In this way, the receiving nodes consider the sending nodes as the sources of the information they are receiving.

2. Nodes exchange opinions regarding the credibility of the information they are giving to the others, but they do not exchange opinions regarding the reliability of the other nodes with whom they got in touch.

With the first assumption we extend the scope of responsibility: a node is responsible not only for the information that it provides to the network as the original source, but also for the information that it receives from some nodes and, retaining it credible, passes on to other nodes. With the second assumption we limit the range of useful information: a node's opinion regarding the other's (and its own) reliability is drawn out from pure information regarding the knowledge domain under consideration, not from indirect opinions.

The structure of the paper is as follows. In Section 2 we present the belief revision model embedded in the nodes of the network. In Section 3 we present the simulation testbed and the nature of the experiment made. Finally, we present the (unfortunately rather unsatisfactory) results of the experiment.

## 2. A model for belief revision in a multiagent environment

In this section we present a belief revision model for a single DSS that receives information from various sources. This model is close to those presented in $[2,30,35]$ but it disconceives the principle of ‘priority to the incoming information’ $[17]$ according to which newcoming information is always part of the rearranged knowledge base. In place of it, we propose the following: ‘store and recover principle’: every piece of incoming information has to be stored to be eventually recovered by a revision process whenever possible. The model brings together assumption-based reasoning and uncertainty management. ATMS-based algorithms $[6]$ guarantee:

\- the knowledge base's ‘stability’; each element that has a valid justification is believed, while each element that lacks a valid justification is disbelieved;

\- the knowledge base's ‘well-foundedness’; there are no mutually dependent elements;

\- the knowledge base's 'logical consistency' (as far as it is currently known to be inconsistent).

Uncertainty management techniques will be applied to choose the most plausible set of beliefs to reason with. We present the model's basic architecture with reference to the diagram in Fig. 1.

![](/api/attachments/AJAQHAZM/fulltext/images/836da54cb5a425fb78bb7ee7367328116f364c40d4b7b37091d372a7e3c1f01a.jpg)  
Fig. 1. The basic architecture of the Belief Revision system.

All the pieces of information received are treated as revisable ‘assumptions’. A piece of information extracted from a private local database is regarded as an information sent by the node to the node itself (a node estimates its own reliability in the same way in which it estimates the others'). There are two kinds of data: that introduced as an assumption and that deductively derived by the Problem Solver as a logical consequence of other data. We call Knowledge Base (KB) the set of all the pieces of information currently received (or acquired); KB grows monotonically since no assumption is ever erased from the memory. We call Knowledge Space (KS) the set of data currently inferred from those in KB; even KS grows monotonically since no derived sentence will ever be removed from KS. Each datum’s Origin Set (OS) [27] records the assumptions upon which it really ultimately depends. The OS of an assumption contains only the identifier of the assumption itself. A same sentence can appear in more than a datum with different OSs. In particular, a same piece of information can appear in assumption and in derived nodes at the same time. The ATMS detects and stores in tables the nogoods; these nogoods are minimally inconsistent subsets of KB. Every superset of a nogood is inconsistent too. A good is a subset of KB that:

1. is consistent (it is not a superset of a nogood),

2. if augmented with whatever else assumption in KB it becomes inconsistent.

Given KB, there is a bijective mapping between sets of nogoods and sets of goods. Finding all the maximally consistent subsets of KB can be very hard [33]. Any good is the complement with respect to

KB of a minimal hitting set for the collection of all the nogoods. We compute the goods and the nogoods with the algorithm to calculate minimal hitting sets presented in [34]. For the purpose of our experiment the algorithm behaves very well, but to be implemented in real DSSs this model needs to be approximated by techniques that trade completeness (of the ATMS that searches the nogoods and of the algorithm that finds their minimal hitting sets) for efficiency (for instance by calculating only the more important goods or by computing only the most credible pieces of information in each good). Each good has a corresponding context, which is the subset of KS made of the inferred data whose OS is subset of the good. A same datum can belong to multiple contexts. This ability to manage multiple contexts is very appealing for belief revision because it makes possible to compare the credibility of different maximally consistent sets of beliefs as a whole than different single beliefs.

A main problem with this model of belief revision is that of defining criteria to select the best context to reason with among the many possible outcomes of the ATMS. It is not the case to select which belief is to be thrown away to remove the contradiction, but, more generally, to choose which is the new preferred good among them in KB; this is the task of the Chooser. In a multi-agent environment, to choose the preferred good CG (and, consequently, the preferred context CC) it will be necessary to develop systems that deal with couples $\langle information, informant\rangle$ , evaluating in the same time the reliability of the source and the credibility of the information. As it interacts with the others, a DSS learns about its partners' reliability and it should refine its opinions regarding the various pieces of information that it received from the others and from its own private database. It also should be able to assign a degree of reliability to itself, i.e. to its own local database.

In assumption-based reasoning the emphasis is placed on assumptions, i.e. on received (not desumed) information, so we do not care about the credibilities of derived data. However, the credibility of a derived sentence could be defined that of the least credible assumption in its OS. The Chooser selects the most plausible contexts by comparing the credibilities of all the goods in KB. We need adequate functions to model these relationships. To cope with the complexity of the matter we introduce three dynamically related parameters:

Table 2  
Table 1  
Representation of epistemic attitudes as data available to a DSS

<table><tr><td></td><td>Statement</td><td>Modal representation</td><td>Node</td></tr><tr><td>1</td><td>A believes that the credibility of  $a$  is  $c_{a}$ </td><td> $\text{Bel}_{A}(\text{cred}(a) = c_{a})$ </td><td> $\langle \_, a, \_, \_, c_{a}, \_\rangle$ </td></tr><tr><td>2</td><td>A believes that the credibility of  $\neg a$  is  $c_{\neg a}$ </td><td> $\text{Bel}_{A}(\text{cred}(\neg a) = c_{\neg a})$ </td><td> $\langle \_, \neg a, \_, \_, c_{\neg a}, \_\rangle$ </td></tr><tr><td>3</td><td>A does not believe that the credibility of  $a$  is  $c_{a}$ </td><td> $\neg \text{Bel}_{A}(\text{cred}(a) = c_{a})$ </td><td>-</td></tr><tr><td>4</td><td>A does not believe that the credibility of  $\neg a$  is  $c_{\neg a}$ </td><td> $\neg \text{Bel}_{A}(\text{cred}(\neg a) = c_{\neg a})$ </td><td>-</td></tr></table>

1. $r_s$ , reliability of the source $s$ estimated by the receiving node,

2. $c_{\alpha}$ , credibility of the assumption $\alpha$ estimated by the receiving node,

3. $c_{\alpha,s}$ , source credibility (s-credibility) of the assumption $\alpha$ estimated by the source s.

These parameters range from -1 to +1:

\- $r_s = -1$ , source absolutely mendacious;

\- $r_{s} = 0$ , source unreliable;

\- $r_{s} = 1$ , source absolutely reliable;

\- $c_{\alpha} = -1$ , assumption absolutely incredible;

\- $c_{\alpha} = 0$ , assumption uncertain;

\- $c_{\alpha} = 1$ , assumption certain.

$c_{\alpha}=0.3\ (r_{s}=0.3)$ means that one should be inclined to bet 0.3 on the veracity of $\alpha$ (on the reliability of s); $c_{\alpha}=-0.3\ (r_{s}=-0.3)$ means that one should be inclined to bet 0.3 on the falsity of $\alpha$ (on the reliability of s).

A datum has the following structure:

## $\langle$ Identifier, Sentence, OS, Source, Credibility $\rangle$ .

The sources' current reliabilities and the assumptions's s-credibilities are collected in two global tables. A same piece of information can appear in multiple nodes with different credibilities. In particular, a same source can provide the same piece of information at different times with different credibilities. The credibility of a good is defined to be the average of the credibilities of the assumptions in it. The preferred context CC is chosen as the one associated to the most credible good. The intended meaning for CC is to be the maximal and globally most believable piece of knowledge currently available to the DSS. A datum is believed if and only if it appears in CC with a positive credibility. There are no relationships between the credibility of an assumption and that of its negated. Actually we could distinguish four kinds of statements (Table 1):

The 3rd and the 4th statements cannot be explicitly expressed as data for these DSS. These sentences simply follow from the 1st and the 2nd for every $c_{\alpha}' \neq c_{\alpha}$ and every $c_{\neg \alpha}' \neq c_{\neg \alpha}$ . There should be a complementary relationship between the credibilities of the 1st and the 3rd, or between the 2nd and the 4th ones but not necessarily between the 1st and the 2nd. However, although the contradictory set {1,2} is not incredible (its internal credibility is generally different from -1) the ATMS removes it; the 1st and the 2nd will never appear in the same good even if they have, reasonably, credibilities with opposite signs. Generally, given an assumption $\alpha$ , $c_{\alpha,s}$ and $c_{\alpha}$ are different because each receiving agent judges $c_{\alpha}$ from its point of view, that is from, at least, the following items:

(a) Currently locally estimated reliability $r_{s}$ of the source. In our intuition, the initial valuation of the credibility $c_{\alpha}$ of a piece of information $\alpha$ is a function:

$$
c _ {\alpha} = f ^ {\prime} \left(r _ {s}, c _ {\alpha , s}\right).
$$

Table 2 shows what we think the qualitative behaviour of this function should be. Whether the information is given as credible or not ( $c_{\alpha,s}$ positive

Qualitative behaviour of the function $f'$

<table><tr><td> $r_s$ </td><td> $c_{\alpha,s}$ </td><td> $c_\alpha$ </td></tr><tr><td>+</td><td>++</td><td>+</td></tr><tr><td>0</td><td>++</td><td>0</td></tr><tr><td>-</td><td>++</td><td>-</td></tr><tr><td>+/0/-</td><td>0</td><td>0</td></tr><tr><td>+</td><td>--</td><td>-</td></tr><tr><td>0</td><td>--</td><td>0</td></tr><tr><td>-</td><td>--</td><td>+</td></tr></table>

Table 3

or negative), it will be as more uncertain as more unreliable is considered the source. If $s$ is considered mendacious then $c_{\alpha}$ and $c_{\alpha,s}$ have different signs. If $s$ is considered reliable then $c_{\alpha}$ and $c_{\alpha,s}$ have the same sign. In our model, we chose for $f'$ the product: when a node receives a piece of information with a s-credibility $c_{\alpha,s}$ from a node whose reliability is $r_s$ , initially it simply estimates the information's credibility by multiplying them:

$$
c _ {\alpha} = r _ {s} \times c _ {\alpha , s}.
$$

(b) Local consistency with all the other assumptions in its KB. The discovery of a nogood affects the internal credibilities of its assumptions. Consider the nogood $\{\alpha,\neg\alpha\}$ . In our intuition, the new credibility $c_{\alpha}^{\prime}$ should be a function of the previous credibilities of $\alpha$ and $\neg\alpha$ , that is:

$$
\begin{array}{l} c _ {\alpha} ^ {\prime} = f ^ {\prime \prime} \left(c _ {\alpha}, c _ {\neg \alpha}\right), \\ c _ {\neg \alpha} ^ {\prime} = f ^ {\prime \prime} \left(c _ {\neg \alpha}, c _ {\alpha}\right). \end{array}
$$

We think that if $c_{\alpha}$ and $c_{\neg\alpha}$ have different signs then their absolute values should increase, since the difference of the signs sounds as a confirmation of the epistemic attitudes toward $\alpha$ and $\neg\alpha$ ; if they have the same sign, then their absolute values should decrease, because one cannot bet much on the veracity and much on the falsity of $\alpha$ ; if they have the same sign and very different absolute values then the minor one could change the sign of its credibility, meaning that one is rather convinced regarding the veracity or the falsity of $\alpha$ . In Table 3 we summarize what we expect it should be the qualitative behaviour of $f''$ ; $c_{\alpha}$ and $c'_{\alpha}$ are the credibilities of $\alpha$ before and after the discovery of the nogood.

A function that reasonably approximates this qualitative behaviour is:

$$
c _ {\alpha} ^ {\prime} = c _ {\alpha} - \frac {c _ {\alpha} + c _ {\neg \alpha}}{2}.
$$

However, in the model adopted in the experiment, we adopted the function:

$$
c _ {a} ^ {\prime} = c _ {a} - \rho \frac {c _ {\neg a}}{| c _ {a} | + | c _ {\neg a} |},
$$

Qualitative behaviour of the function $f''$

<table><tr><td> $c_{\alpha}$ </td><td> $c_{\neg \alpha}$ </td><td> $c'_{\alpha}$ </td><td> $c'_{\neg \alpha}$ </td></tr><tr><td>--</td><td>++</td><td>-- --</td><td>+++</td></tr><tr><td>++</td><td>--</td><td>+++</td><td>-- --</td></tr><tr><td>++</td><td>++</td><td>+</td><td>+</td></tr><tr><td>--</td><td>--</td><td>-</td><td>-</td></tr><tr><td>++</td><td>+</td><td>+</td><td>-</td></tr><tr><td>--</td><td>-</td><td>-</td><td>+</td></tr></table>

where $c_{\alpha}^{\prime}$ was truncated into the range $-1 \leq c_{\alpha}^{\prime} \leq 1$ . The parameter $\rho (0 < \rho \leq 1)$ will be estimated experimentally.

Generally, a nogood involves more than two assumptions and the same assumption can be involved in more than one nogood. In this case the new credibility of an assumption depends on the credibilities of all the other assumptions in the nogood for all the nogoods. The following function generalizes the preceding one:

$$
c _ {\alpha} ^ {\prime} = c _ {\alpha} - \rho \cdot \sum_ {\mathrm{ng} \in \mathrm{NG}} \frac {C _ {\mathrm{ng}}}{P | c _ {\alpha} | + | C _ {\mathrm{ng}} |},
$$

where:

$$
C _ {\mathrm{ng}} = \frac {\sum_ {(k \in \mathrm{ng}) \wedge (k \neq a)} c _ {k}}{| \mathrm{ng} | - 1},
$$

where NG is the set of nogoods to which $\alpha$ belongs and $|ng|$ is the cardinality of ng. This function treats all the nogoods as they were detected simultaneously.

## 2.1. Example

Let us illustrate the preceding formula with an example. Suppose that $KB = \{\alpha, \beta, \chi, \delta, \epsilon, \phi\}$ with $c_{\alpha} = c_{\beta} = c_{\chi} = c_{\delta} = c_{\epsilon} = c_{\phi} = 0.5$ and $\rho = 0.5$ . Let the following be the goods and the nogoods:

$$
\begin{array}{l l} \text {goods:} & \{\alpha , \beta , \chi , \delta \}, \{\chi , \delta , \epsilon , \phi \}, \{\alpha , \chi , \delta , \epsilon \}, \\ & \{\beta , \chi , \delta , \epsilon \} \\ \text {nogoods:} & \{\alpha , \phi \}, \{\beta , \phi \}, \{\alpha , \beta , \epsilon \} \end{array}
$$

The new credibility of $\alpha$ is:

$$
\begin{array}{r l} & c _ {\alpha} ^ {\prime} = c _ {\alpha} - \rho \cdot \left[ \frac {c _ {\phi}}{| c _ {\alpha} | + | c _ {\phi} |} + \frac {(c _ {\beta} + c _ {\epsilon}) / 2}{| c _ {\alpha} | + | (c _ {\beta} + c _ {\epsilon}) / 2 |} \right] \\ & \quad = 0, \\ & c _ {\beta} ^ {\prime} = c _ {\beta} - \rho \cdot \left[ \frac {c _ {\phi}}{| c _ {\beta} | + | c _ {\phi} |} + \frac {(c _ {\alpha} + c _ {\epsilon}) / 2}{| c _ {\beta} | + | (c _ {\alpha} + c _ {\epsilon}) / 2 |} \right] \\ & \quad = 0, \\ & c _ {\chi} ^ {\prime} = c _ {\chi} = 0. 5, \\ & c _ {\delta} ^ {\prime} = c _ {\delta} = 0. 5, \\ & c _ {\epsilon} ^ {\prime} = c _ {\epsilon} - \rho \cdot \left[ \frac {(c _ {\alpha} + c _ {\beta}) / 2}{| c _ {\epsilon} | + | (c _ {\alpha} + c _ {\beta}) / 2 |} \right] = 0. 2 5, \\ & c _ {\phi} ^ {\prime} = c _ {\phi} - \rho \cdot \left[ \frac {c _ {\alpha}}{| c _ {\phi} | + | c _ {\alpha} |} + \frac {c _ {\beta}}{| c _ {\phi} | + | c _ {\beta} |} \right] = 0. \end{array}
$$

These changes in the internal credibilities of the assumptions will affect their respective current source's reliability. This new reliability will be used to calculate the credibilities of the next information coming from that agent. In our intuition, the reliability $r_{s}$ of an agent s that gave an information with s-credibility $c_{\alpha,s}$ should depend on $c_{\alpha}$ and $c_{\alpha,s}$ :

$$
r _ {s} = f ^ {\prime \prime \prime} \left(c _ {\alpha}, c _ {\alpha , s}\right).
$$

Our idea is simply that an information source's reliability should decrease with the distance between the information's credibility and s-credibility. This is an acceptable correspondence:

$$
r _ {s} = 1 - | c _ {\alpha} - c _ {\alpha , s} |.
$$

Given the set $R$ of all the assumptions come from that source, the actual current source's reliability is the average of all the reliabilities for each assumption:

$$
r _ {s} = \frac {\sum_ {\alpha \in R} 1 - \left| c _ {\alpha} - c _ {\alpha , s} \right|}{\left| R \right|}.
$$

In this model we assume that an agent estimates his own reliability in the same way (with the same function) in which he calculates the others' reliability.

## 3. The experiment

We are going to simulate an organization of DSSs. It is expected that any single DSS could take, in some way, advantage of its being part of the group even if it could be able to accomplice its task by itself. We would like to investigate, on a statistical basis, which combinations of:

1. configurations of the organization,

2. modelling of the single nodes,

3. rules of interaction,

assure the best synergistic results. The group we considered in our simulation was unstructured and compound of a few elements. However, the node's model is prepared to implement hierarchical organizations. Regarding the points 2 and 3, the focus of our experiment has been studying how local strategies of belief revision and locally implemented rules of communication affect the global performances of the DDSS. In our view, it is unreasonable and intuitively wrong to try to ensure that all the nodes' views are globally consistent (as in distributed TMS [Huhns 90]). It is better to let agents stand by their beliefs based on their own view of the evidence. This permits the realistic possibility that nobody has uncompromised evidence or information. This is what Mason and Johnson [26] call “Liberal Belief Revision Policy.” In fact, in real world networks of DSSs, nodes are not necessarily always benevolent nor regularly competent, so they can lie, deliberately or not. As far as DDSSs will spread over the world, we'll need local policies of belief revision which resist the defilement of the information. We agree with Mason and Johnson [26] that there is no satisfactory answer to the question “How do we determine which agent is right?”, but we can try to answer the questions “How do we determine the most reliable agents?” and “How do we determine the most credible pieces of information?”

To reduce the risks of information pollution and/or monopoly, along with good local strategies of belief revision we will need also good local communication policies.

In our experimental session we made the following working assumptions:

1. The nodes transmit only the pieces of information contained in their preferred context CC (partially or totally).

2. The nodes do not communicate the sources from which they received the various pieces of information, but they present themselves as completely responsible for the knowledge they are passing on. The receiving nodes consider the sending nodes as the sources of all the pieces of information they are receiving.

3. The nodes communicate their personal estimations regarding the credibility of the pieces of information they are passing, but they do not supply their opinions regarding the others' (and their own) reliability.

4. All nodes use the same representation language (syntax and semantic) for beliefs.

5. Communicating nodes ‘know’ what they are talking about, and they have a common ‘understanding’ of the propositions they exchange.

6. All the nodes have the common notion of logical inconsistency.

7. There are no noises on the communication channels.

8. The general mechanism for decision is a mostly subconscious task to the DSS (but nothing prevents us to consider DSSs aware of it so that they can conceive strategies to influence the others by means of communication).

## 3.1. The simulation testbed

Adopting the model for belief revision presented in this paper as a local mechanism to manage and solve contradictions in a Distributed Decision Support Systems, we hope to achieve:

![](/api/attachments/AJAQHAZM/fulltext/images/289042a3fb50644752dfec3d023b1388f08c1b9778b26691b186ec5d48c6f5e1.jpg)  
Fig. 2. The scenario of the simulation testbed, with agents wandering around searching for clues and exchanging their current results. Each agent represents a DSS.

Table 4  
Internal representation of the items of the game

<table><tr><td>A</td><td>B</td><td>C</td><td></td><td></td><td></td><td></td></tr><tr><td>Col. Mustard</td><td>Dagger</td><td>Anteroom</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Miss Rosa</td><td>Candlestick</td><td>Veranda</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Prof. Plum</td><td>Pistol</td><td>Dining Room</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>Rev. Green</td><td>Rope</td><td>Kitchen</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>Cap. Brown</td><td>Bar</td><td>Dance Hall</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>Mrs Pavone</td><td>Monkey Wrench</td><td>Sitting Room</td><td>11</td><td>12</td><td>13</td><td>14</td></tr><tr><td>Miss Scarlett</td><td>Carabine</td><td>Billiard Room</td><td>13</td><td>14</td><td>15</td><td>16</td></tr><tr><td>Mrs White</td><td>Hatchet</td><td>Library</td><td>15</td><td>16</td><td>17</td><td>18</td></tr><tr><td>Serg. Gray</td><td>Poison</td><td>Study</td><td>17</td><td>18</td><td>1</td><td>2</td></tr></table>

## 1. the convergence of:

(a) the nodes' opinions regarding the credibility of the various pieces of information that are running through the network,

(b) the nodes' opinions regarding the reliability of all the members of the organization;

2. the stability of these convergences: the agreement should not be subsequently broken groundless;

3. the correctness of these convergences: the set of beliefs on which the nodes reached the consensus should contain as much truthful knowledge as possible and the concordant opinions regarding the various nodes' reliability should reflect the real competence (and sincerity) of the DSSs;

4. the robustness of these convergences: down to what degree of reliability of the members and up to what percentage of unreliable agents the organization is still able to reach these convergences?

To evaluate these features we have developed CLUE, a testbed based on MICE [28], a specific tool for multiagent applications by means of which we can define various agents with different capabilities, able to communicate each other, perceive the environment, move in it and modify it. Inspiration for our specific testbed has come from CLUEDO $^{™}$ , a board game based on detective stories metaphor. In the following we sketch the CLUE testbed.

Table 5  
Example of possible clues

<table><tr><td>A, 7</td><td>Prof. Plum, Rev. Green</td></tr><tr><td>B, 2</td><td>Dagger, Poison</td></tr><tr><td>C, 4</td><td>Anteroom, Veranda</td></tr></table>

In the nine rooms of the Tudor house move nine characters, each able to use any of the nine weapons available in the house. It is commonly known that the householder is dead. Any character must detect which of his companions (maybe himself) is the killer, which weapon he used and in which room he murdered the householder. The clues are randomly placed in the house (Fig. 2).

Each agent investigates by himself wandering around following simple strategies to find out the clues. Each of the 27 (9 + 9 + 9) items of the game are univocally characterized by a letter ('A' for the characters, 'B' for the rooms and 'C' for the weapons) and a tuple of four integers (from 1 to 18) as reported in Table 4.

A clue is a couple $\langle letter, integer\rangle$ . For instance, the clues $\langle A,1\rangle$ and $\langle A,2\rangle$ rouse suspicion that the killer is 'Serg. Gray' or 'Col. Mustard'. In addition there are some special 'exculpating' clues of the form $\langle\neg character\rangle$ or $\langle\neg room\rangle$ or $\langle\neg weapon\rangle$ . A case consists in 12 clues (four for each item). A set of clue maps on a set of candidate solutions (one killer, one weapon, one room), that are all the terns of items compatible with the collected clues. A void set of clue maps on the set of all 93 possible solutions. The more clues in the set, the less the candidate solutions. For instance, let $\langle A,7\rangle$ , $\langle B,2\rangle$ , $\langle C,4\rangle$ be the collected clues. They correspond to the items listed in Table 5: which identify the eight possible solutions listed in Table 6. After the discovery of the (exculpating) clues $\langle\neg Rev. Green\rangle$ , $\langle\neg Anteroom\rangle$ the set of possible solutions collapses to the one listed in Table 7.

Table 6  
Candidate solutions

<table><tr><td>1</td><td>Prof. Plum</td><td>Dagger</td><td>Anteroom</td></tr><tr><td>2</td><td>Prof. Plum</td><td>Dagger</td><td>Veranda</td></tr><tr><td>3</td><td>Prof. Plum</td><td>Poison</td><td>Anteroom</td></tr><tr><td>4</td><td>Prof. Plum</td><td>Poison</td><td>Veranda</td></tr><tr><td>5</td><td>Rev. Green</td><td>Dagger</td><td>Anteroom</td></tr><tr><td>6</td><td>Rev. Green</td><td>Dagger</td><td>Veranda</td></tr><tr><td>7</td><td>Rev. Green</td><td>Poison</td><td>Anteroom</td></tr><tr><td>8</td><td>Rev. Green</td><td>Poison</td><td>Veranda</td></tr></table>

Table 7  
Remaining candidate solutions

<table><tr><td>2</td><td>Prof. Plum</td><td>Dagger</td><td>Veranda</td></tr><tr><td>4</td><td>Prof. Plum</td><td>Poison</td><td>Veranda</td></tr></table>

All agents have a limited visibility. An agent finds a clue if he is sufficiently close so that he can view it. Each agent has an ‘a priori’ fixed perceptive capacity. Even if they see a clue, agents can perceive it badly. The probability of a right perception is proportional to the agent’s capacity. When an agent erroneously detects a clue, he does not assume an absurd datum but he assumes a datum that individuates items among the 24 ones not involved in the case.

On meeting each other, agents exchange their current results. So, the when and the who parts of the communication policy are carried out randomly. Regarding the what part, we had many choices, from communicating the entire set of clues in the database to communicating selected pieces of information depending on the reliability of the receiving agent. As a compromise we chose the communication of the entire preferred good, regardless to the estimated reliability of the receiving agent. If agent A passes its preferred good to agent B and subsequently changes its preferred good or his opinion regarding the credibility of the pieces of information contained in it, this change will not affect the preceding communication made to B until they meet again.

Each agent has also a certain degree of sincerity: an agent is ‘sincere’ if he communicates the context that it considers the most credible one; an agent is ‘insincere’ if he communicates a context in which he does not believe; an agent is ‘pernicious’ if he communicates a context in which he does not believe and changes the degrees of credibility of the pieces of information that he passes to the others. In the experiment, if the database of an agent with a degree of sincerity s (-1 < s < 1) contains n goods, ordered from the most to the least credible one, he communicates the good in the position

$$
p = \operatorname{int} \left(\frac {n}{2} + s \frac {n}{2}\right).
$$

Furthermore, if he estimates that $c_{a}$ is the credibility of a piece of information a, he gives for it the credibility $c_{a}^{\prime}=c_{a}^{\prime}s$ . This modelling of insincerity is very rough and does not reflect the complexity and the meaning that this term has in the real world. Indeed, this is the weakest point in the model of these agents; however, we are not really directly interested in a realistic shaping of this negative ability, since we do not aim at building insincere agents but at building sincere agents and an agency able to recognize them.

There are two kinds of agents: the detective and the accomplice ones. When a detective agent finds a clue, he calculates its credibility by multiplying his own (auto)reliability with the given (objective) credibility of the clue (we set this credibility to '1' for all the clues in all the simulations made), then he records it in his database. When an accomplice agent finds a clue he does the same that the innocent one does but he also cancels the clue to prevent the others from finding it (just for the fun of it, he does not cancel a clue if there is a detective agent that can see him!). By doing so we aim at studying the effects of the introduction of private databases inaccessible to most of the other agents.

When agents communicate their results they do not specify who found the clues. They act as the clues were personally discovered. In general, in the database of an agent there will be many copies of a clue (one for each agent that communicated it) so that it will be necessary to establish a degree of credibility that expresses the agent's opinion regarding that clue. That is the value that will be communicated to the others. Let the representative credibility be that value. There can be many ways to calculate the representative credibility of a 'replicated' clue: min and max could be reasonable functions but we initially chose the average. Any receiving agent considers the sending agent as the source of the information; he calculates the credibility of each received piece of information by multiplying the reliability of the sending agent with the credibility of the clue supplied by the source, then he records it in his database along with the source and the internal and the external credibilities of the clue. Any agent's database can become inconsistent for two reasons:

1. observing a clue, the agent can perceive it badly,
2. the agent receives incorrect information from in-
sincere, mendacious or incapable agents.

On detecting a contradiction in its own database any agent starts a belief revision process. In the CLUE testbed there are no derived sentences (all the clues are treated as assumptions), so that KS collapses to KB and the context associated to a given good coincides with the good itself. The agent will:

1. list all the nogoods and goods,

2. calculate the reliability of the other agents and the credibilities of all the clues in its KB,

3. select the most credible good.

A nogood is a minimally incompatible set of clues, i.e., a set of clues all of the same kind (character, weapon or room) that do not identify any item and that, if it is reduced of any of its clues then it individuates one or more items. Conversely, a good is a subset of the clues in KB (not necessarily all of the same kind) that does not contain a nogood, but it will become a superset of a nogood if expanded by any other clue in KB. The credibility of a good is defined to be the average of the credibility of all the clues in it. In this way we take into account all the pieces of information in the good but we ignore its cardinality. Clues that have been communicated by different sources are replicated with (normally) different credibilities. Obviously they will be linked together since they will always be contained in the same goods. The effects of the changes in the credibility of each of them on the overall belief revision process will be weighted by the others. If a same source gives the same clues more than once, then we have two choices: (a) replace the old datum with the new one with the newly calculated internal credibility, (b) retain all the data doing as if the sources were different (but with the same current reliability). We chose the first solution as the least conservative one, but we were not very convinced about it. Since this event is very frequent, this choice will be influential on the results of the simulations. When an agent's preferred good contains enough clues to single out a solution then the agent proposes it. Since an agent can change his preferred good, he can change his mind and abjure the proposed solution by adopting another one or by simply returning confused (because his new good does not contain a number of clues sufficient to individuate a single solution). The simulation does not stop when an agent proposes a solution, but after a predetermined number of 'cycles'. This because often, after having presented a solution, agents change their minds, rejecting previously held pieces of knowledge and adopting the point of view of some other agents. During a cycle all the agents change their position.

To make possible experiments with structured organizations we modelled the agents with a degree of authority (from 1 to 5). We used this parameter just to solve trajectory conflicts and deadlocks in the locomotion of the agents, but the purpose is that of leading simulations of hierarchical structures to see how the global performances vary when incapacity and/or insincerity distributes over various levels of the organization. The nature of the power could be simply that of conditioning the stream of information (from low to high levels but not vice versa), or, more effectively, that of forcing the subalterns to adopt the superior's cognitive state. The acquisition of power could be established by the scientists (predetermined and fixed) or could be performed dynamically by means of general elections.

## 3.2. Refining the model for belief revision

The first step of a simulation is the setting of the 'initial conditions', that are:

1. the case ( $\langle$ killer, weapon, room $\rangle$ ).

2. the number of agents (it has always been set at 9 – just to simulate the board game),

3. the spatial disposition of the clues,

4. the spatial disposition of the agents.

We then set some technical parameters of the simulation (some of them regarding the locomotory abilities of the agents), among which:

\- length of the simulation (that has always been 4000 cycles; this number of cycles has often been sufficient for a corrupt agent to cancel all the clues),

\- snapshots' interval (number of cycles among two subsequent samples; this interval has always been 100 cycles).

## Three important initial settings are:

1. the agents' opinions regarding their own and the others' degree of reliability,

2. the 'source' credibility of the directly perceived clues,

3. the value of the parameter r.

In all the simulations made, we set at '0' each agent's auto-reliability and each agent's opinion regarding each other's reliability; in this way we reduced the risk of being influenced by groundless prejudices. The source credibility of the perceived clues was always set at '1', so that their internal credibility was equal to the auto-reliability of the agent.

The independent variables in our experiment were:

1. the distribution of the agents' degrees of capacity,  
2. the distribution of the agents' degrees of sincerity.

At each sample, for each agent we stored the following data:

\- current distribution of the estimates regarding the others' and his own reliability,

• currently preferred good,

\- credibility of the preferred good,

\- currently proposed solution (if the preferred good contains enough clues),

• number of different solutions proposed,

• number of communications performed.

For each instantiation of the independent variables we started a series of simulations varying the initial conditions. We computed the average of each datum, for each sample over all the simulations.

In the easiest case (datum-point) in which all the agents were competent and sincere, the convergence to the (obviously) correct solution was reached within 600 cycles. The convergence was reached earlier if they communicated more. The credibility of the preferred good was the same for all the agents.

We then examined the case in which all the agents were sincere and competent, apart from the one that had a limited degree of competence. We tried five degrees of capacity: 0.8, 0.6, 0.4, 0.2, 0. For each of these values we started various series of simulations varying not only the initial conditions but also the initial settings: (1) (\{1,0.75,0.5,0.25,0\}), (2) (\{1,0.75,0.5,0.25\}), and (3) (\{1,0.75,0.5,0.25\}). We defined degree of correctness as the number of agents with the correct solutions (the others may be proposing a wrong solution or none). The diagram in Fig. 3 summarizes the behaviour of the degree of correctness for all these simulations.

![](/api/attachments/AJAQHAZM/fulltext/images/e285663dacddccf4e0610d69531ff9a9ed37916264b882f59e87209f7b30ed80.jpg)  
Fig. 3. Number of agents with the correct solutions in the case that there is an incompetent agent.

We observed that:

\- All the agents (even the incompetent one) almost always found the correct solution (a little bit slower) but subsequently they were systematically misled by the incapable agent (instability probably due to the ‘credulous’ nature of these agents).

\- After 2000 cycles the credibilities of the different goods of any agent were very close to each other so that rather insignificant changes in the credibility of some clues caused the change of the preferred good (flattening and instability due to the abuse of the average function).

\- When agents with similar cognitive states exchange their preferred good, they do not increase the credibility of their beliefs nor the estimates regarding each others' reliability (as it seems reasonable it should be)

\- The global behaviour of the agency was too much dependent on the initial conditions (we were not able to explain this behaviour and we were forced to carry on more experiments than expected to yield well founded statistics).

\- A reduction in the value of $r$ cuts down the effects of communication with respect to the directly perceived clues.

A main problem with our modelling was that the credibility of a piece of information increases only after conflict with a piece of information with negative credibility. Probably, a belief with positive credibility should be confirmed even by the concurrence of the same data with positive credibility from a different independent source. So, we introduced the idea of giving a 'prize' to the consensus. Let the degree of consensus G be the percentage of received data already belonging to the preferred good with the same sign of credibility. Let r be the auto-reliability, $r_{s}$ the reliability of the sending agent and $d = |r - r_{s}|$ . We modified the way an agent recalculates its and the other's own reliability:

$$
\begin{array}{l l} \cdot & r _ {s} ^ {\prime} = r _ {s} + d \times G \text {   if   } r _ {s} <   r, \\ \cdot & r ^ {\prime} = r + d \times G \text {   if   } r <   r _ {s}. \end{array}
$$

Hoping to limit the flattening of the goods' credibility we changed the function that calculates the representative credibility of a replicated clue: instead of the average we chose the maximum. After repeating the simulations, with the same settings as before, we observed that.

\- the agents were only a bit more conservative regarding their opinions,

\- under high degrees of consensus, the credibility of the preferred goods increased,

\- the flattening of the degrees of credibility of the goods lightly reduced.

However, we noticed also the following negative behaviour:

\- under high degrees of consensus, the reliability and the auto-reliability of the agents involved in the communication did not increase,

and, more seriously:

\- the estimates of the reliability of the agents (92 values) did not reflect their real degrees of competence (only one incapable agent).

We tried to make the agents still more conservative regarding their opinions. The idea was that of differentiating the calculus of the auto-reliability: instead of the (8) we adopt a function that computes the average of the old and the new auto-reliability:

$$
r ^ {\prime} = \left(r + \frac {\sum_ {a \in R} 1 - | c _ {\alpha} - c _ {\alpha , s} |}{| R |}\right) / 2.
$$

![](/api/attachments/AJAQHAZM/fulltext/images/7c7911f554dbca2dce6d533f3d54bbcf9b04fe8f1be6335ee669bea65fbc9774.jpg)  
Fig. 4. Reduction in the number of proposed solutions.

We observed a drastic reduction in the number of proposed solutions (Fig. 4). This means that the agents were not favorably disposed toward changes of mind. We also obtained some further reduction of the flattening, but the reliabilities estimated by the agents were still absolutely unrelated with the real competences of the agents themselves. We then realized that our definition of degree of consensus was rather insignificant since two agents highly concordant regarding the clues could be proposing totally different solutions of the case. We realized that the degree of consensus should be calculated based on the shared solutions (associated to the preferred good) not based on the shared clues. However, neither this change produced significant improvements in the global performance of the agency.

In our modelling we did not take into account the numbers of repetitions of a piece of information, i.e., the number of times a clue has been perceived or received from communication. As a consequence, few clues with high credibility dominate many clues with slower credibility. A wrong piece of information with a high degree of credibility that comes after many right clues provokes disastrous effects since it will become part of a good with fewer pieces of information and its contribution to the credibility of the good itself (which is the average of the credibilities of its clues) will be very high. It is not infrequent that a wrong clue causes changes of the preferred good, so it is explained why the incompetent agent, although it realizes that it is unreliable and gives to the others clues with low credibility, it is able to perturb the global cognitive state to the point that all the agents lose the correct solution. From Eq. (4) we see that the change of the credibility of a piece of information is proportional to $\rho$ . This suggests to make $\rho$ dependent on the cardinality of the goods and of the nogood to which the piece of information belongs. $\rho$ is no more fixed but it varies with the function:

$$
\rho = \frac {N _ {c}}{N _ {c} + N _ {n c}}, \quad (0 <   \rho \leq 1),
$$

where $N_{c}$ is the number of assumptions into the biggest good to which $\alpha$ belongs ('confirmations'), and $N_{nc}$ is the number of assumptions into the biggest nogood to which $\alpha$ belongs ('counter-checks').

In the case of conflicting clues with comparable credibilities it will be punished the clue with fewer confirmations and more counter-checks.

## 3.3. Results with the last version of the model

Almost 700 hours of simulation on a 'SPARK-STATION 2' showed that the model we adopted in the experiment does not assure convergency when more than one agent (among nine) is unreliable. For each instance of the independent variables (distributions of capacity and sincerity) we made three simulations varying the initial conditions. All the graphs for each simulation are reported in [20]. We began with all agents being sincere and with the following distributions of capacity listed in Table 8.

The agents converged twice to the correct solution and once to a wrong one. The reliabilities estimated by the incapable agent were the lowest of the group, and he found himself as the least reliable agent of the agency. The other agents at first averagely recognized the incapable agent as the least reliable one, but subsequently their opinions changed and they saw him as the most affordable source of the group. It should be noted that the incapable agent here is the same that cancels the clues after finding them, i.e., he is in a unique position regarding the accessibility to the information.

Table 8  
Only one agent is incompetent (the accomplice one)

<table><tr><td>Agent</td><td>Type</td><td>Capacity</td></tr><tr><td>1</td><td>Accomplice</td><td>0.8</td></tr><tr><td>2</td><td>Detective</td><td>1</td></tr><tr><td>3</td><td>Detective</td><td>1</td></tr><tr><td>4</td><td>Detective</td><td>1</td></tr><tr><td>5</td><td>Detective</td><td>1</td></tr><tr><td>6</td><td>Detective</td><td>1</td></tr><tr><td>7</td><td>Detective</td><td>1</td></tr><tr><td>8</td><td>Detective</td><td>1</td></tr><tr><td>9</td><td>Detective</td><td>1</td></tr></table>

We reduced the reliability of the capacity of the incompetent agent to 0.5. At first the agents converged to the correct solution but after that they chose the wrong solution twice. The reliabilities estimated were lower than in the preceding case (the agents were more suspicious of each other). The incapable agent was not recognized either in the initial phase. These trends were confirmed when we further reduced, at 0.3 and at 0, the capacity of the incapable agent. In the latter case the agents were not able to gain convergency on any solution (in the maximum amount of time of 4000 cycles).

![](/api/attachments/AJAQHAZM/fulltext/images/f575bcd135670978b54c048e7cc53b33cd40945706d98f89eddd08e1132b902f.jpg)  
Fig. 5. Average of the reliability estimated by eight agents toward the ninth one. Agent 1 is the accomplice while agent 2 is the incapable one.

Table 9  
The incompetent agent is a detective

<table><tr><td>Agent</td><td>Type</td><td>Capacity</td></tr><tr><td>1</td><td>Accomplice</td><td>1</td></tr><tr><td>2</td><td>Detective</td><td>0.8</td></tr><tr><td>3</td><td>Detective</td><td>1</td></tr><tr><td>4</td><td>Detective</td><td>1</td></tr><tr><td>5</td><td>Detective</td><td>1</td></tr><tr><td>6</td><td>Detective</td><td>1</td></tr><tr><td>7</td><td>Detective</td><td>1</td></tr><tr><td>8</td><td>Detective</td><td>1</td></tr><tr><td>9</td><td>Detective</td><td>1</td></tr></table>

We then modelled as incapable a detective agent (Table 9).

Rather strangely, the degree of convergence (number of agents proposing the same solution, not necessarily the correct one) was lower than in the analogous preceding case. However, the incapable agent was not regarded as the most reliable one, but he was neither recognized as the least reliable one.

We then set at 0 the capacity of the incompetent agent (agent 2). The graph in Fig. 5 refers to this case. The lowest reliability is ascribed to the incapable agent while the highest to the accomplice agent.

From these simulations with only one incapable agent we can summarize the following results:

1. the degree of convergence of the agents to a same solution is ‘guaranteed’ only if the incapable agent has a capacity greater than 0.5 (less than 25% of errors);

2. the degree of correctness decreases with the capacity of the incapable agent and is rather dependent on the initial conditions;

3. at the end of the simulation, the most reliable agent is considered the accomplice one;

4. if the incapable agent is a detective one, then he is normally recognized by the others (and by himself).

We tried to increase the number of incapable agents (Table 10). The degrees of convergence and correctness drastically decreased and they did not reach a stable value. Only the incapable detective agent was recognized. We then increased the number of incompetent agents, to 4 and then to 7. The degrees of correctness and convergence decreased in the former case and were annulled in the latter case. However, in the case of four incapable agents we saw that the convergence was more stable than in the case of two incapable agents. We think that this result was due to the initial conditions. It is difficult to establish the threshold for the acceptable performances of the agency.

Table 10  
Two agents are incompetent

<table><tr><td>Agent</td><td>Type</td><td>Capacity</td></tr><tr><td>1</td><td>Accomplice</td><td>0.8</td></tr><tr><td>2</td><td>Detective</td><td>0.8</td></tr><tr><td>3</td><td>Detective</td><td>1</td></tr><tr><td>4</td><td>Detective</td><td>1</td></tr><tr><td>5</td><td>Detective</td><td>1</td></tr><tr><td>6</td><td>Detective</td><td>1</td></tr><tr><td>7</td><td>Detective</td><td>1</td></tr><tr><td>8</td><td>Detective</td><td>1</td></tr><tr><td>9</td><td>Detective</td><td>1</td></tr></table>

The simulations with insincere agents (Table 11) were more difficult to understand. We think that the results were too dependent on the initial conditions.

The degree of correctness was high only in the initial phase of the simulation; in the final part it was practically reduced to '0'. The insincere agent was not recognized, while the incapable agent (which was the accomplice) was assigned with the highest degree of reliability. With two insincere agents we obtained better results regarding the correctness, the stability of the convergence and regarding the estimates of the reliabilities (which were higher than before, but the insincere agents were not recognized).

Table 11  
One agent is incompetent and another one is insincere

<table><tr><td>Agent</td><td>Type</td><td>Capacity</td><td>Sincerity</td></tr><tr><td>1</td><td>Accomplice</td><td>0.8</td><td>1</td></tr><tr><td>2</td><td>Detective</td><td>1</td><td>0</td></tr><tr><td>3</td><td>Detective</td><td>1</td><td>1</td></tr><tr><td>4</td><td>Detective</td><td>1</td><td>1</td></tr><tr><td>5</td><td>Detective</td><td>1</td><td>1</td></tr><tr><td>6</td><td>Detective</td><td>1</td><td>1</td></tr><tr><td>7</td><td>Detective</td><td>1</td><td>1</td></tr><tr><td>8</td><td>Detective</td><td>1</td><td>1</td></tr><tr><td>9</td><td>Detective</td><td>1</td><td>1</td></tr></table>

We obtained the same results with four insincere agents. With a fifth highly incompetent agent, the agency was totally unable to reach a correct solution but the insincere agents were recognized! With seven insincere agents all the nine agents were estimated unreliable (almost at '0') by the others.

During all the experiment we detected an anomaly in the behaviour of the agent's belief revision system; when the agent's preferred good has negative credibility (a very rare case) the system crashes down: both the agents' reliabilities and the credibilities of the preferred goods tend to $-1$ . This event depends on the number of communications that an incapable agent is able to make before being recognized. Perhaps, a way to deal with such cases of emergence could be that of making the agents believe only directly perceived clues until their preferred good's credibility grownups to the positive range.

## 4. Conclusion

Almost 700 hours of simulation on a 'SPARK-STATION 2' (and 14 MB of produced data) with the multi-agent simulation testbed CLUE, confirm that it is possible to find model for belief revision to embed in each DSS of a distributed system that favours the stable convergency and correctness of the opinions regarding what is more credible and who is more reliable. This result can be reached without the agents exchanging information concerning reliability judgements and without their keeping trace of the original sources of the information. However, adopting our model for belief revision and our policies of communication, this result was reached only in the easy case in which just one among nine DSSs is rather incompetent. Furthermore, the results are not very significant since the simulation testbed was a highly idealized and simplified representation of a real Distributed Decision Support System.

## 5. Future developments

To begin with, we need a simulator specially designed for the Distributed Decision Support Systems scenario. The one adopted in the experiment was designed also for Distributed Robotics so that:

\- it wastes much of the time in simulating the wandering of the agents around the world,

\- it is able to coordinate the activity of too few agents.

For future experiments we plan to modify the DSS's model in several ways. Some ideas are:

\- Adopt the Dempster–Shafer approach to combine corroborating/conflicting evidences.

\- Allow the agents to communicate different pieces of information to different agents, depending on the estimated reliability of these agents. This could preserve a high quality information from being ruined.

\- Simulate hierarchical structures where information flows only from the bottom up, and study the effects of incapacity or insincerity over different levels of the structure.

\- Simulate hierarchical structures where the superiors are able to force in some ways their subalterns to adopt their cognitive state, whether the opinions are regarding the credibility of the pieces of information or the reliability of the various agents.

\- Simulate dynamic hierarchical structures where the power can be gained or lost depending on: (a) objective characteristics of the agents, as their capacity or their being close to the real solution of the case (however, objective properties are valuable only from outside the network so that these ways are rather infeasible in real systems), and (b) characteristics of the agents estimated by the others (typically their degree of reliability averagely estimated by the others).

\- Allow the agents to have exclusive access to their own pieces of information and study the global performances of the agency with different shares between private and public information accessibility.

## Acknowledgements

Paolo Giorgini worked hard in his master thesis to build and drive the simulator CLUEDO, adopted in the experiment. We would like to thank Andrea Brown for her correction of many spelling mistakes and grammatical errors in English, and an anonymous referee for his helpful comments.

## References

[1] C.E. Alchourrón, P. Gärdenfors and D. Makinson, On the Logic of Theory Change: Partial meet Contraction and Revision Functions, The Journal of Simbolic Logic, No. 50 (1985) 510–530.

[2] S. Benferhat, C. Cayrol, D. Dubois, J. Lang and H. Prade, Inconsistency Management and Prioritized Syntax-Based Entailment, in: Proc. of the 13th Inter. Joint Conf. on Artificial Intelligence (IJCAI'93) (1993) 640–645.

[3] R. K. Bhatnagare and L.N. Kanal, Handling Uncertain Information: A Review of Numeric and Non-numeric Methods, in: Kanal and Lemmer, Eds., Uncertainty in Artificial Intelligence (1986).

[4] G. Brewka, Preferred Subtheories: An Extended Logical Framework for Default Reasoning, in: Proc. of the 11th Inter. Joint Conf. on Artificial Intelligence (IJCAI'89) (1989) 1043–1048.

[5] M. Dalal, Investigations Into a Theory of Knowledge Base Revision: Preliminary Report, in: Proc. of the American Conf. on Artificial Intelligence (AAAI'88) (1988).

[6] J. de Kleer, An Assumption Based Truth Maintenance System, Artificial Intelligence 28, (1986) 127–162.

[7] S. Dixon and N. Foo, Connections Between the ATMS and AGM Belief Revision, in: Proc. of the 13th Inter. Joint Conf. on Artificial Intelligence (IJCAI'93) (1993) 534–539.

[8] J. Doyle, Reason Maintenance and Belief Revision: Foundation versus Coherence Theories, in: P.Gärdenfors, Ed., Belief Revision (Cambridge University Press, 1992).

[9] A.F. Dragoni, A Model for Belief Revision in a Multi-Agent Environment, in: E. Werner and Y. Demazeau, Eds., Decentralized A.I.3. (Elsevier Science Publisher, Amsterdam, 1992).

[10] A.F. Dragoni and M. Di Manzo, Supporting Complex Inquiries, International Journal of Intelligent Systems 10, (1995).

[11] A.F. Dragoni and P. Puliti, Distributed Belief Revision versus Distributed Truth Maintenance, In: Proc. 6th IEEE Int. Conf. on Tools with A.I., New Orleans (IEEE Press, 1994).

[12] A.F. Dragoni, F. Mascaretti, P. Puliti, A Generalized Approach to Consistency Based Belief Revision, Proceedings of the 4th Conference of the Italian Association for Artificial Intelligence, Lectur Notes in Artificial Intelligence, LNAI 992 (Springer-Verlag, 1995).

[13] D. Dubois and H. Prade, A Survey of Belief Revision and Update Rules in Various Uncertainty Models, International Journal of Intelligence Systems 9, (1994) 61–100.

[14] D. Dubois and H. Prade, Belief Change and Possibility Theory, in: P. Gärdenfors, Ed., Belief Revision (Cambridge University Press, 1992).

[15] J. Fox, Knowledge, Decision Making, and Uncertainty, in: A. Gale, Ed., Artificial Intelligence and Statistics (1986).

[16] J.R. Galliers, Modelling Autonomous Belief Revision in Dialogue, Tech Report, Cambridge University Comp. Lab., Cambridge England (1989).

[17] P. Gärdenfors, Knowledge in Flux: Modeling the Dynamics of Epistemic States (MIT Press, Cambridge, MA, 1988).

[18] P. Gärdenfors, Belief Revision: An Introduction, in: P. Gärdenfors, Ed., Belief Revision (Cambridge University Press, 1992).

[19] P. Gärdenfors, Belief Revision and Non Monotonic Logic: Two Sides of the Same Coin?, in: Proc. of the 9th European Conference on Artificial Intelligence (ECAI 90) (1990) 768–773.

[20] P. Giorgini, Un modello di Revisione delle Conoscenze per Sistemi Distribuiti, Ph.D. Thesis in Electronic Engineering, University of Ancona, A.A. 1992–93 (April 1994).

[21] G. Harman, Change in View: Principles of Reasoning (MIT Press, Cambridge, MA, 1986).

[22] X. Huang, G.I. McCalla, E. Neufeld, Using Attention in Belief Revision, in: Proc. of the American Conf. on Artificial Intelligence (AAAI 91) (1991).

[23] K.B. Laskey and P.E. Lehner, Belief Maintenance: An Integrated Approach to Uncertainty Management, in: J. Pearl and G. Shafer, Eds., Readings in Uncertain Reasoning (Morgan Kaufmann, 1990).

[24] Léa Sombé, A Glance at Revision and Updating in Knowledge Bases, International Journal of Intelligence Systems 9, (1994) 1–27.

[25] F. Lévy, A Survey of Belief Revision and Updating in Classical Logic, International Journal of Intelligence Systems 9, (1994) 29–59.

[26] C.L. Mason and R.R. Johnson, DATMS: A Framework for Distributed Assumption Based Reasoning, in: L. Gasser and M.N. Huhns, Eds., Distributed Artificial Intelligence 2 (Pitman/Morgan Kaufmann, London, 1989) 293–318.

[27] J.P. Martins and S.C. Shapiro, A Model for Belief Revision, Artificial Intelligence 35, No. 1 (1988) 25–79.

[28] T.A. Montgomery, J. Lee, D.J. Musliner, D.E. Damouth, Y. So and E.H. Durfee, MICE Users Guide, Artificial Intelligence Laboratory, Dept. of Electrical Engineering and Computer Science, University of Michigan, Ann Arbor, Michigan (Feb. 1992).

[29] B. Nebel, A Knowledge Level Analysis of Belief Revision, KR 1989.

[30] B. Nebel, Base Revision Operations and Schemes: Semantics, Representation, and Complexity, in: Proc. of the 11th European Conference on Artificial Intelligence (Wiley and Sons, 1994).

[31] B. Nebel, Belief Revision and Default Reasoning: Syntax-Based Approaches, KR 1991.

[32] B. Nebel, Syntax Based Approaches to Belief Revision, in: P. Gärdenfors, Ed., Belief Revision (Cambridge University Press, 1992).

[33] G.M. Provan, A Complexity Analysis of Assumption-Based Truth Maintenance Systems, in: B. Smith and G. Kelleher, Eds., Reason Maintenance Systems and Their Applications (Ellis Horwood Series in Artificial Intelligence, 1988).

[34] R. Reiter, A Theory of Diagnosis from First Principles, Artificial Intelligence, (1987).

[35] N. Roos, A Logic for Reasoning with Inconsistent Knowledge, Artificial Intelligence 57, (1992).

[36] G. Shafer, Belief Functions, in: J. Pearl and G. Shafer, Eds., Readings in Uncertain Reasoning (Morgan Kaufmann, 1990).

[37] G. Shafer and R. Srivastava, The Bayesian and Belief-Function Formalisms a General Perpective for Auditing, in: J. Pearl and G. Shafer, Eds., Readings in Uncertain Reasoning (Morgan Kaufmann, 1990).

[38] D.J. Spiegelhalter, A Statistical View of Uncertainty in Expert Systems, In: A. Gale, Ed., Artificial Intelligence and Statistics (1986).

[39] L. Willard and L.Y. Yuan, The Revised Gärdenfors Postulates and Update Semantics, Lectures Notes in Computer Science, in: Goos and Hartmanis, Eds., da ICDT '90.

[40] Q. Zhu and E.S. Lee, Dempster–Shafer Approach in Propositional Logic, International Journal of Intelligent Systems 8, (1993).

![](/api/attachments/AJAQHAZM/fulltext/images/a160fa5bf4ddc0a247e40468569f6575e893fc15db2fee70bbe52702c7c57678.jpg)

Aldo Franco Dragoni received a degree in Electronics Engineering from the University of Ancona (Italy). He has been a member of the Program Committee of two International Conferences on Artificial Intelligence (ICTAI '95 and MAAMAW '96), and reviewer for Journals and International Conferences. He participated in two National Research Projects (of Robotics and Building). He is member of the AAAI, IEEE and AI\* IA (Italian Association for Artificial

Intelligence). Since 1989 he works as Technical Collaborator at the Computer Science Institute of the University of Ancona, where he lectures Logic Programming and Artificial Intelligence and has tutored 16 Master Theses in the field of Artificial Intelligence. His current research interests include Distributed Cognition, Belief Revision and Reasoning under Uncertainty.
