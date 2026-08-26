---
otero_id: 17238
otero_key: "9Y3ZUNSA"
title: "Diagnosis and correction of office system communication"
authors: "F. Cazzola; M. Galli; B. Pernici"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90017-j"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Diagnosis and correction of office system communication

F. Cazzola, M. Galli
Politecnico di Milano, Milano, Italy

B. Pernici

University of Udine, Udine, Italy

Automatic support to Office Information System (OIS) design is needed to improve the quality of the design and to make it more efficient. An important part of OIS is represented by communication aspects. Messages of different types are exchanged between agents according to the office protocol for a given procedure. A tool to support automatic detection of office protocol specification errors and their correction is presented. The tool is able to propose solutions to the errors, based on a generalized protocol analysis theory.

Keywords: Office information systems, Communication analysis, D.2.1 Requirements specification, D.2.10 Design – methodologies, representation, H.4 Information systems applications.

![](/api/attachments/9Y3ZUNSA/fulltext/images/e0f5cc77b84d62ebe4bcfdbec41526e36dd437e2b4a91a73d19ebe276ed19d82.jpg)

Francesco Cazzola was born in Milan on Oct. 28, 1963. He graduated in Electronics Engineering at Politecnico di Milano in 1988, with a thesis on the analysis of communication problems for the design of office procedures. Presently, he is with the “Unità specialistica per l'informatica” of ENEL, where he works on distributed systems and on the development of applications based on client-server architectures.

![](/api/attachments/9Y3ZUNSA/fulltext/images/957fdc7645682ff0c63b0ebc4b3318df2e5ed55b8a40d5241e6f132c9d4b13f7.jpg)

Massimiliano Galli, born in Ancona (Italy) on Oct. 13, 1963, graduated in Electronics Engineering at Politecnico di Milano in 1988, with a thesis on the analysis of communication problems for the design of office procedures. Presently, he is a research associate at the “Centro di Ricerca sui Sistemi di Gestione della Produzione” of the Consorzio Universitario MIP-Politecnico di Milano, where he works on the organizational impact of methodologies and technology innovation on production.

Correspondence to: B. Pernici, Università di Udine, Dip. di Matem. e Informatica, via Zanon 6, I-33100 Udine UD, Italy. e-mail: pernici@uduniv.cineca.it, Tel: +39/432/297169 ext. 206, Fax: 510755.

## 1. Introduction and motivation

The problem of developing Information Systems (IS), Databases, and software packages has been studied for years. Many methods and techniques have been proposed to support the different phases of the design life cycle. However, manual methods and techniques are not sufficient to master the complexity of big software development projects.

Recent research is focusing on developing computer based tools to support the design of complex projects [Fre 85, DaE 84, Was 82, Cer86b].

The potential benefits of using computer aided development are on productivity, design quality, and product quality. However, many existing computer based tools are still based on concepts required by manual activities, i.e., on an old system development paradigm, therefore a great part of the potential benefits of using them during design is thus lost. For instance, many software and IS development tools based on the concepts of Structured Analysis [DeM 79] are mainly centered on the goal of providing a computer based support to the production of Data Flow Diagrams and Data Dictionary, and therefore they often provide only little more than a good graphical editor and documentation management tools.

Recent research is moving in the direction of providing tools that do not just support manual activities, but also perform, with the aid of the designer, some design decisions. This new generation of tools, to provide effective support, must be specialised in performing a specific design activity, e.g., in the database (DB) area, normalizing relations [Cer 86a, Bou 85], or, in software engineering, producing source code corresponding to the specifications.

A growing sector in the Information System area is the sector of Office Information Systems (OIS). Peculiar aspects characterize the office environment, and specialized tools can be useful to help the designer of Office Information Systems in his task.

Several methods and models to support OIS design have been proposed in the literature [Bra 84]. The aim of these methods and models is to construct upon existing IS and software (sw) design techniques, adding the consideration of characteristics which are peculiar of the office environments.

As in the case of IS, DB, and sw development, also in the OIS area recently some efforts have been devoted to develop automatic tools for supporting office information system design in all its phases [Per 86, Per 88, Loc 88].

An important aspect in OIS design is the modelization of office structure and its behaviour: this is usually called “conceptual design” [Bra 84]. In this phase it is very important to product a correct modelization and this implies consistency and correctness verification of the office schema obtained during the design process.

The purpose of this paper is to show how the analysis of the modelization of office procedures, concerning the aspects relative to the correct exchange of information, can be supported by computer based tools. First, we illustrate a technique of verification of office procedures, then we present an intelligent system for suggesting solutions to the designer to solve an incorrect office schema.

In section 2 an overview on the problems inherent to Office Information System design is presented. In section 3 we illustrate the office communication analysis technique.

In section 4 we show the functional aspects of the analysis and diagnosis system, then in section 5 we present the intelligent tool to support correction of design errors. In section 6 we show an example using our tool.

## 2. Modeling in office environment

The office environment is characterized by some peculiar aspects which assume a relevant role in Office Information System design.

The original features of the office environment lead to a different design process for an office information system versus the design of a conventional information system [Bra 84].

We summarize here some of the differences which proved to be important in our work.

Office data: the types of data used in conventional information systems, such as characters, strings, and numeric data, are not sufficient in the office environment, other types of data, such as unstructured data contained in messages, letters, texts, annotations, graphics, and oral communications are currently employed and must be supported.

Office activities: activities may be unstructured in office information systems [Pan 84]. These activities are performed following instructions which are usually incomplete. Flexibility in performing activities is essential for achieving office goals, due to the high number of possible exception situations and anomalies.

Interconnection of elements: complexity in office information system design is higher than in a conventional information system design, because of the large number of elements in each office related through several connections. The elements are distributed among several office workers in the same or in different departments and can also be located externally to the office environment.

Integration of functions: in office information systems the office goal is achieved by an integration of different functions based on cooperation among the elements in the office.

These original features of OIS are particularly relevant in the early phases of the design process, commonly called the “conceptual” or “logical” phases.

The conceptual design of an Office Information System is a complex task where it is necessary to define office and business goals, to locate those functions in office work that are only loosely related to the goals of the enterprise and to give a guide in providing some technical solution suitable to the office under study, taking into consideration the set of analyzed problems.

In this paper, we focus on communication problems during office activities.

Some solutions have been proposed in the literature to handle the particular characteristics of OIS mentioned above. Office models allow to describe the structure of the data being exchanged between office workers. Several types of models have been proposed [Bra 84] and, among them, office Document Architecture (ODA) and Office Document Interchange Format (ODIF) [Hor 85] have been proposed to describe both the logical structure and the layout of documents.

Office activities have been classified by [Pan 84] in two broad classes. Type I activities follow well defined procedures, while Type II activities represent creative and variable work which does not follow a precise procedure. Models for describing office procedures have been proposed for Type I activities, in which it is possible to describe control and data flows, the document types and archives being accessed and communication patterns. The first model of this type was proposed by [Zis 78] and was based on augmented Petri Nets to model office activities. Information Control Nets (ICN), proposed in [Ell 79], allow to describe office procedures in terms both of data and of control flows. In this model, however, data are not described in detail with their characteristics, and communication aspects are embedded in the procedure description and not made explicit.

Communication between workers has been examined in the past mainly from two different perspectives: the first takes into consideration the semantics of communication, while in the second conversations are analyzed independently of their semantics, to guarantee their correct synchronization and termination.

The meaning of the communication acts has been analyzed in detail by [Flo 80]. Each speech act is classified according to its type: assertive, directive, commissive, declarative, and expressive. In this framework, offices and organizations are considered primarily as networks of directives (including orders, requests, consultations or offers) and commissives (including promises, acceptances, denial and so on). Some systems based on these concepts have been developed [e.g., Flo 80], providing an agenda for managers in a telecommunication environment in which different types of speech acts can be manipulated and recorded.

A technique for analyzing conversational systems is proposed in [Woe 88]. A generic conversation can be analyzed, based on Predicate/Transition Nets, in order to determine whether a conversation has been correctly terminated on both sides, and that it is not blocked due to a faulty synchronization between the participants. A tool for analysis of conversations has been proposed, based on simulation of Predicate/Transition Nets.

An approach leading to the development of a complete methodology for office system design, involving not only the conceptual design phase, is represented by the TODOS project (Automatic TOols for Designing Office Information Systems), whose goal is to develop tools to support various aspects of the design. We developed our tool for supporting the design of office communication protocols starting from the TODOS environment. In TODOS, the approach taken in modeling communication between agents takes partially into consideration the semantics of exchanged messages.

## 3. TODOS: An example of a complete methodology for office information system design supported by automatic tools

TODOS is a three year multinational project started in 1986, supported by the Commission of the European Communities within the ESPRIT Programme under Project N. 813 [Per 90].

Partners in TODOS are Dornier GmbH (D), Oce' (NL), Italtel (I), Sema-Metra (F), Thomson (F), and Politecnico di Milano (I).

The work on developing models and tools for conceptual design is performed at Politecnico di Milano (by the authors, M. G. Fugini, and S. Pozzi), Thomson Informatique Services (J.R. Rames), and its subcontractor Univ. of Paris (Prof. C. Rolland). The work presented in this paper was initiated starting from concepts developed for office conceptual modeling in TODOS.

The goal of the TODOS project is making Office Information Systems development easier, quicker, and more reliable by providing analysts, designers and users with a set of design tools [Per 86].

Techniques for collecting design data, conceptual modeling, office system rapid prototyping, and architecture selection are studied in the project. The project is divided in four Work Packages, corresponding to the four phases of the TODOS method:

1. requirement collection and analysis

2. conceptual design

3. rapid prototyping of office systems

4. architecture design.

For each of these phases a modeling language and a development environment based on this language are being realized.

The conceptual design phase has the task of organizing the information, collected in the requirement collection phase, in a formal way by means of a conceptual model.

The TODOS Conceptual Model (TCM) is a semantic model of office static and dynamic elements [Per 87].

Static elements describe data structures in the office and include documents, messages, agents, and objects.

## Document

This concept allows to model office real world documents, such as forms, letters, memos and so on.

TCL DB database containing office

## C - TODOS

![](/api/attachments/9Y3ZUNSA/fulltext/images/d8a0e89ddd63a27d3852e58f15d7eb31a2a022d9b6841b2979bf0c84574317c9.jpg)

TSL TODOS Specification Language

TQL TODOS Query Language

Fig. 1. Architecture of C-TODOS.

## Object

An object represents information that is needed by the office system or by users for performing the office work.

## Agent

An agent defines the role played by an office worker or a group of workers in office environment.

## Message

Messages model office communication, i.e., phone calls, electronic mail messages, and so on. It is important to underline that messages are used to model temporary information within the system: if such information is needed in a more permanent way for performing activities in the office system, message information has to be stored as documents or objects.

Dynamic elements describe procedural aspects of the information system in terms of events and actions.

Event

An event models a system state change, such as message arrival or a temporal event (e.g., end of the month). One event entity is always associated with one static entity; the event ascertains a state change of the static entity.

Action

An action represents an activity performed in the office (e.g., copying a document, sending a message). One action entity is always associated with one static entity, called the modified entity.

A dynamic transition models the relationship between events and actions. It allows to model the relationship between a system state change (event) and its consequences (transition elements).

A transition element is composed by an action and (optionally) of a condition and a triggering factor associated to it.

C-TODOS is the tool being developed to support conceptual modeling. The architecture of C-TODOS is represented in Fig. 1. C-TODOS consists of the following components:

\- the specification database, which stores the formal description of the office being designed (TCL DB);

\- the specification module, which supports the analyst in writing specifications into the specification database and in retrieving information from it; it is composed of two modules:

\- the modeling module, which supports the analyst in creating and modifying specification database data;

\- the query module which supports queries against the specification database;

\- the analysis module, which allows the analyst to check the consistency of the specification DB, highlighting the presence of undesired features in the specifications; the analysis module allows also to produce reports as documentation for the project.

In the work presented in this paper we focus on consistency checking on the dynamic submodel about information exchanges in the office.

In the following section, we present the theoretical basis for analyzing information exchanges. We based our work on that of proposed by Shi-Kuo Chang [Cha 81, Cha 82, Cha 84, Cha 85], extending it to be able to consider complex messages involving more than two agents. The most important aspect of our work is the realization of an analysis and diagnosis tool, based on this theory, which allows to help the designer in correcting erroneous specifications of message exchanges in the office.

## 4. Verification of office procedures

Shi-Kuo Chang developed a methodology for verification of office procedures [Cha 85].

Among the aspects involved in this methodology (management of office data and office activities, study of information exchange), we are interested in the study and modeling of information exchange processes among interacting agents.

Chang defines an agent as an information processor (a person, an organizational unit, a computer program, and so on), which is capable of manipulating data and assuming different states [Cha 82].

The process of information exchange between two agents is called conversation or interaction; the unit of information exchange is called a message.

It is necessary to specify the rules which govern message exchanges among agents; this can be done by specifying a protocol.

We adopt the following definition of protocol [Cha 82]: “the set of rules which govern the exchange of messages”.

The models of computer communication protocols can be classified into three major categories:

(1) finite state automata models

(2) Petri Nets and related models

(3) programming languages.

These protocol models have been developed for computer communication in general.

Petri Nets are a powerful tool for modeling concurrent and asynchronous systems [Pet 77].

Particular primitives have been developed in programming languages for handling synchronization of processes [Mer 79].

![](/api/attachments/9Y3ZUNSA/fulltext/images/08a27967f1376c3de56a487e936f0ef4aeafd33de5d489da2f126c6c41703607.jpg)  
Fig. 2. Pay office agents.

The first two types of model have also been extended for office modeling. We have seen in section 2. that extended Petri Nets have been used to model office procedures [Ell 79, Zis 78].

Finite state automata have been adopted among others by Chang to model office procedures.

As office environments not only involve message exchanges, but also activity management and database updates, Chang developed a technique for modeling and analysis of protocols, based on automata theory, and called protocol analysis.

## 4.1. Modeling a protocol with finite state automata theory

Each agent in the office is represented by a finite state automaton called protocol agent [Cha 82, Cha 85].

A protocol agent $M_{i}$ is a 5-tuple ( $K_{i}$ , $S_{i}$ , $g_{i}$ , $s_{0}$ , $F_{i}$ ), where:

1. $\mathbf{K}_{\mathrm{i}}$ is the finite nonempty set of messages exchanged by agent $\mathbf{M}_{\mathrm{i}}$ .

$K_{i} \subseteq X$ where X is the universal message space; X contains all the messages exchanged among the protocol agents, including the empty message “e”.

2. $S_{i}$ is a finite nonempty set of states $\{s_{0}, s_{1}, s_{2}, \ldots, s_{m}\}$ .

3. $\mathbf{g}_{\mathrm{i}}\colon \mathbf{S}_{\mathrm{i}}\times \mathbf{K}_{\mathrm{i}}\times \mathbf{D}_{\mathrm{i}}\to \mathbf{S}_{\mathrm{i}}$ is the state transition function.

$D_{i}=\{+, -\}$ , where + denotes that the message is received by $M_{i}$ and - denotes that the message is sent by $M_{i}$ .

4. $\mathbf{s}_0\in \mathbf{S}_{\mathrm{i}}$ is the initial state.

5. $F_{i} \subseteq S_{i}$ is the set of final states.

As an example of a protocol modeled with automata theory, we can see the protocol agents represented in Fig. 2. We have two agents, an employee and a pay office: the employee may ask for a loan sending a request to the pay office.

```txt
Employee
    preparing loan request
    waiting for reply
    loan pending

Pay office
    waiting for a request
    request examining
    loan pending

The set of messages is the same for the agents because we have in this example only two agents:
    loan request (a)
    request deny (d)
    request acceptance (g)
    payback (p)
```

The request may be accepted or refused, and the decision is communicated to the employee by a message.

The pay office will ignore other requests by the employee until the employee has reimbursed the loan. We have the following sets of states:

The final states are represented by a double circle, while the initial states are marked with an arrow.

## 4.2. Protocol analysis

Protocol analysis lets us examine a protocol in order to detect whether it is correct or it has deadlock or unspecified reception problem.

Protocol analysis consists in building a protocol machine. Given N agents modeled with the 5-tuples $\mathbf{M}_{\mathrm{i}} = (\mathbf{K}_{\mathrm{i}},\mathbf{S}_{\mathrm{i}},\mathbf{g}_{\mathrm{i}},\mathbf{s}_{0\mathrm{i}},\mathbf{F}_{\mathrm{i}})$ with $\mathrm{i} = 1\dots \mathrm{N}$ , a protocol machine M is a 5-tuple (K, S, g, $s_0$ , F) where:

1. $\mathbf{K} = \{(x_1, \ldots, x_N) | \text{there exist } i, j \text{ such that } x_i \in K_i, x_j \in K_j, x_i = -x_j \text{ and } x_k = e \text{ for all } k \text{ not equal to } i \text{ or } j\}$ .

2. $S = \{ (s_{i1}, s_{i2}, \dots, s_{iN}) | s_{ik} \in S_k, 1 \leqslant k \geqslant N \}$ is the set of states of $M$ .

It is important to underline that $S$ is a subset of the cartesian product of the sets of states $S_{i}$ of agents $M_{i}$ . Generally not all the possible states are reachable.

A state $s$ is reachable if a message sequence $w$ exists, such that $g(s_0, w) = s$ .

3. $g((s_{i1}, \ldots, s_{iN}), (x_{1}, \ldots, x_{N})) = (f_{1}(s_{i1}, x_{1}), \ldots, f_{N}(s_{iN}, x_{N}))$ where

$$
f _ {k} \left(s _ {i k}, x _ {k}\right) = \left\{ \begin{array}{l l} s _ {i k} & \text {if} x _ {k} = e \\ “ - ” & \text {if} g _ {k} \left(s _ {i k}, x _ {k}\right) \\ & \text {is unspecified in} M _ {k} \\ g _ {k} \left(s _ {i k}, x _ {k}\right) & \text {otherwise} \end{array} \right.
$$

4. $s_{0}=(s_{01},s_{0,\ldots},s_{0N})$ .

5. $F = \{ (s_{i1}, s_{i2}, \ldots, s_{iN}) | s_{ik} \in F_k \}.$

The protocol machine shows the joint evolution of all the agents of the protocol.

Chang makes the following assumptions about message exchanges:

(1) simultaneous exchanges of more than one message are not allowed: the protocol machine can change state only after exchanging a single message

(2) each message exchange involves a pair of agents: one of the agents sends the message, the other receives it.

All the other agents do not evolve.

We show how to remove these constraints later, when we introduce generalized protocol analysis.

For each reachable state, it is necessary to examine how the agents can evolve for each possible message exchange.

In this way it is possible to classify all the state transitions of the protocol machine.

After classifying the state transitions it is possible to classify the states of the protocol machine. This classification will allow us to detect possible errors in the protocol.

For a state $(s_{i1},\ldots,s_{iN})$ of the protocol machine M, given a message, there are four types of state transitions:

1. if $\mathbf{g}((\mathbf{s}_{\mathrm{i}1},\ldots,\mathbf{s}_{\mathrm{i}\mathrm{N}}),(\mathbf{x}_{1},\ldots,\mathbf{x}_{\mathrm{N}}))=(\mathbf{s}_{\mathrm{j}1},\ldots,\mathbf{s}_{\mathrm{j}\mathrm{N}})$ with $s_{jk}$ not equal to “-” for $1\leqslant k\geqslant N$ , the transition is a normal transition (NT); it means that the next state is specified for each agent;

2. if the next state is unspecified for the agent which sends the message, but the next state is specified for the agent which receives the message, the transition is a send-unspecified transition (ST);

3. if the next state is unspecified for the agent which receives the message, but the next state is specified for the agent which sends the message, the transition is a receive-unspecified transition (RT);

4. if the next state is unspecified for both the agents exchanging the message, the transition is a unspecified transition (UT).

The presence of a receive-unspecified transition (RT) denotes that the agent sending the message is in a state which allows the message to be sent, while the agent receiving the message is in a state in which receiving the message is not allowed. The presence of a receive-unspecified transition (RT) denotes a protocol error; the problem is called unspecified reception and it occurs whenever one agent is in a state incapable of receiving a message sent by the other agent.

A send-unspecified transition (ST) means that the agent receiving the message is in a correct state to do it, but the agent sending the message is in an uncorrect state; in this state of the protocol machine the message can not be sent.

An unspecified transition (UT) means that neither of the two agents exchanging the message is able to evolve.

Given a state of the protocol machine, while the presence of receive-unspecified transitions (RT) denotes a protocol error, the presence of send-unspecified transitions (ST) and/or unspecified transitions (UT) is not a problem. Such transitions (UT and/or ST) are a problem only if a correct way to evolve does not exist in that state of the machine (i.e., none of the transitions of that state is a normal transition).

According to these criteria a state of a protocol machine can be classified as follows:

1. if there is at least one receive-unspecified transition (RT), it is a receive-unspecified state (RUS).

2. if there are neither receive-unspecified transitions (RT) nor normal transitions (NT), and there is at least a send-unspecified transition (ST), it is a deadlock state (DLS).

3. if all the transitions are unspecified (UT), it is a dead-end state (DES).

4. otherwise it is a normal state (NS).

We have noted above that for receive-unspecified states (RUS) we have a problem which has been called unspecified reception.

Deadlock states (DLS) and dead-end states (DES) are states of the protocol machine from which it is impossible to evolve towards another state; the only difference between DLS and DES is that in the case of deadlock states some agents are in a correct state to receive messages (which however cannot be sent), while in the case of dead-end states there are not even agents waiting for a message.

According to these arguments, we define correct a protocol when all the states of the protocol machine are classified as normal states (NS), except for those states which are final states: in this case they may be dead-end states.

We solved the problem of determining the set of reachable states of protocol analysis by developing an algorithm to build a reachability graph; the set of nodes in the graph coincides with the set of reachable states of the protocol machine and the set of arcs is built up with all the normal transitions of the machine.

The reachability graph for our example is shown in Fig. 3. We can see that the set of states of the machine is a subset of the cartesian product of the states of the agents, and represents the reachability set $\{(s_{0}, s_{0}), (s_{1}, s_{1}), (s_{2}, s_{2})\}$ .

![](/api/attachments/9Y3ZUNSA/fulltext/images/bced6aa757d545635e91c6389edb4711ce6ee2662cc10f813bad601f9abfa9bb.jpg)  
Fig. 3. Reachability graph.

Fig. 4. shows the table of states and transitions for the protocol formed by the agents employee and pay office.

Each row corresponds to a reachable state of the machine, while columns correspond to all the possible message exchanges.

The table contains all the possible transitions, with their classification, and a classification of the states of the protocol machine: in our example there is a receive-unspecified state (RUS), so the protocol is not correct: in fact, when the employee sends a request for an additional loan from state $s_{2}$ , the pay office is not ready to handle such a message (it can only receive a payback message in its state $s_{2}$ )

## 4.3. Generalized protocol analysis

We extended Chang's protocol analysis in order to have a more powerful and general analysis technique.

We extended Chang's protocol analysis in the sense that we allow an agent to send more than one message simultaneously, involving more than two agents in a message exchange.

This multiple exchange can be modeled introducing also the concept of multiple message: the message is sent by a single agent, but it is made up of a n-ple of messages, each of which is received by a different agent.

Therefore, in general, the agent sending the message sends n messages (n instances of the same message or n different messages) to n different agents.

The main consequence of this generalization is:

<table><tr><td colspan="6">TABLE OF TRANSITIONS AND STATES OF PROTOCOL MACHINE</td></tr><tr><td></td><td>(+g,-g)</td><td>(+d,-d)</td><td>(-p,+p)</td><td>(-a,+a)</td><td></td></tr><tr><td>(S0,S0)</td><td>(_,_)UT</td><td>(_,_)UT</td><td>(_,_)UT</td><td>(S1,S1)NT</td><td>NS</td></tr><tr><td>(S1,S1)</td><td>(S2,S2)NT</td><td>(S0,S0)NT</td><td>(_,_)UT</td><td>(_,_)UT</td><td>NS</td></tr><tr><td>(S2,S2)</td><td>(_,_)UT</td><td>(_,_)UT</td><td>(S0,S0)NT</td><td>(S2,_)RT</td><td>RUS</td></tr></table>

Fig. 4. Table of transitions and states.

a message exchange can cause the evolution of more than two agents.

If all the messages of the protocol are n-ples with $n = 1$ (simple messages), Chang's protocol analysis is enough to study the protocol; so protocol analysis is a special case of generalized protocol analysis.

In order to show better purposes and consequences of this extension let us examine an example.

In Fig. 5, we can see a three agent protocol, in which the first agent (meeting organizer) sends an invitation message to the other two agents (managing director, president) and waits for their replies.

The messages of the protocol are:

c managing director's reply

d president's reply

x invitation

Multiple message x is composed of two messages:

a invitation to managing director

b invitation to president

We are interested in multiple message x, which is made up by messages a and b.

In the case of multiple messages, to classify state transitions of the protocol machine is more complex that in the case of simple messages.

In fact, when a multiple message is sent, there are several agents receiving the message; so it is possible that only some of them are in a correct state to receive their component of the message, but not the others.

In the example, all the possible transitions for multiple message x are the following (states are ordered as follows: meeting organizer, managing director, president)

$$
\begin{array}{l l} \hline (- x, + a, + b) \\ \hline (- -, -, -) U T \\ (s _ {i}, s _ {j}, s _ {k}) N T \\ (s _ {h}, -, -) R T \\ (-, s _ {w}, s _ {v}) S T \\ (s _ {h}, s _ {w}, -) \\ (s _ {j}, -, s _ {k}) \\ (-, s _ {j}, -) \\ (-, -, s _ {1}) \end{array} \quad \text {cases classified by Chang}
$$

where “—” means that the next state is unspecified.

We classify the new cases as follows:

New case 1: some of the agents receiving the message have an unspecified next state, while the next state is specified for the other agents receiving the message and for the agent sending the message.

Even if some of the agents could receive their component of message correctly, the transition is classified as receive-unspecified transition (RT).

This choice is due to the fact that the multiple message is viewed as an atomic entity in the analysis: it must be correctly received by each agent, otherwise it causes a problem of unspecified reception.

New case 2: some of the agents receiving the message have a specified next state, while the next state is unspecified for the other agents receiving the message and for the agent sending the message.

Possible classifications for this kind of transition could be unspecified transition (UT) or send-unspecified transition (ST).

As some agents have a specified next state it seems to be correct to classify this case as send-unspecified transition (ST).

The classification of the states of the protocol machine in generalized protocol analysis given the state transitions is the same as in Chang's protocol analysis.

![](/api/attachments/9Y3ZUNSA/fulltext/images/29543dd5049893ece19f526d091bdb7110d7c454b0f5ac603a2aa306ba833bc8.jpg)  
Fig. 5. Invitation three agent protocol.

## 5. Analysis and diagnosis of office protocols

As our system goal is to support the designer of office procedures with an automatic tool which detects communication problems, we felt it was extremely useful to develop not only an analysis technique, but also to look for criteria which can guide the user in finding the solution to detected problems.

Semantic evaluations on the protocol are not considered by the system, which asks the user to decide if the proposed solutions are semantically significant.

This is due to the fact that the criteria on which the search of solutions is based do not take in account the meaning of the messages.

## 5.1. Modules organization

The system is composed of five modules, organized as in Fig. 6.

The manager is at the top of module hierarchy because it has the task to coordinate and control the execution of the other modules in the following order:

(1) preliminary checks

(2) reachability graph construction

(3) table of transitions and states classification

(4) diagnosis

![](/api/attachments/9Y3ZUNSA/fulltext/images/70ffdb848b7d1f96bcaa9e4fe36311bf9d96d874c9befe66486b8d4d9d953ced.jpg)  
Fig. 6. System architecture.

## Manager

The first task of this module is to load the specifications of the protocol in the database. It has also to load the other modules, enabling their execution in the order previously specified.

## Preliminary checks

The purpose of this module is to perform some consistency checks on protocol specifications: these checks capture some errors in the protocol which can be identified before performing protocol analysis. - to verify the existence of at least one final state for each agent

\- to verify that, in case of simple messages, the message exchange happens between two agents (one sending the message and the other receiving it)

\- for all the messages declared as multiple messages, to verify that an agent sending the message exists and that for each component of the message there is an agent receiving it

\- to control that each agent is a deterministic automa.

When it is verified that the protocol being examined is not consistent according to the preliminary checks, the system assists the user in modifying it.

These preliminary checks have the only purpose of verifying the consistency of the model, but they do not control the protocol correctness.

It is however necessary to make these checks before protocol analysis; in fact it would be completely useless to analyze an inconsistent protocol.

## Reachability graph construction

This module constructs the reachability graph.

## Table of transitions and states classification

The task of this module is the costruction of the table of transitions and states.

For each state of the protocol machine (node of the reachability graph), for each possible message exchange, the transitions are classified according to the criteria explained in generalized protocol analysis.

After classifying all the transitions, the states of the machine are classified.

## Diagnosis

This module evaluates if the protocol is correct, i.e., if all the states of the machine are normal states (or dead-end states if they are final states).

If the protocol is not correct the system undertakes the following actions:

\- listing receive-unspecified states, deadlock states and dead-end states found in the analysis,

\- suggesting possible solutions to the problems, in the following order:

(1) receive-unspecified states with a single receive-unspecified transition,

![](/api/attachments/9Y3ZUNSA/fulltext/images/0bf9db713155f83290c1644eab4a060333d466dcbfde522be5cee6c10d329fa6.jpg)  
Fig. 7. General view of system organization.

(2) receive-unspecified states with more than one receive-unspecified transition,

(3) deadlock states,

(4) dead-end states.

Only the user (i.e., the office designer) can evaluate if the proposed solution is semantically meaningful. For this reason the module is highly interactive and each solution must be accepted or refused by the user.

If the user refuses the proposed solution, the system looks for another one; if he accepts the solution the system modifies the protocol model and updates the classification of transitions and states in the table.

A general view of system organization is shown in Fig. 7.

## 5.2. Diagnosis and correction of uncorrect message exchange models

An uncorrect protocol can present three kinds of problems:

\- receive-unspecified states (RUS)

\- deadlock states (DLS)

\- dead-end states (DES).

In order to make the protocol correct, it is necessary to transform all receive-unspecified states, deadlock states, dead-end states (unless then are final states) into normal states.

We adopt the following solution strategy:

(1) only messages already present in the protocol are considered

(2) protocol agents are modified only by adding arcs in the respect of the following reachability constraint: changes in the modelization must not modify the set of reachable states.

If new states were introduced, we could know nothing about their classification; so we could introduce new problems in the protocol when trying to solve a single protocol error.

Adding/removing states to the agents or removing arcs does not respect the reachability constraint; so these actions are not taken into account during diagnosis and correction. However, if the designer decides so, he can always decide to modify the specifications of the protocol and the whole process can be reiterated.

## Receive-unspecified states (RUS)

To solve the receive-unspecified states we must consider four cases.

A first classification is between receive-unspecified states with at least one normal transition and receive-unspecified states without normal transitions.

The states belonging to the first class have a possibility of evolution, given by the existence of the normal transition: so it is sufficient to solve the receive-unspecified problem, transforming the receive-unspecified transition (RT) into one of the other kinds of transitions (NT, ST or UT).

The states belonging to the second class do not have a possibility of evolution because of the absence of a normal transition. For these states, it is not sufficient to solve the receive-unspecified problem: we must give to the protocol a possibility of evolution not to transform the state into a deadlock state. It is therefore necessary to transform the receive-unspecified transition (RT) into a normal transition (NT).

The second level of classification deals with the presence of more than one receive-unspecified transition: this implies that all receive-unspecified transitions have to be transformed into another kind of transition (NT, ST or UT).

## Transformation $RT\to NT$

Transforming a receive-unspecified transition into a normal transition means to make the next state specified for the agents receiving the message.

This can be done by adding an arc, corresponding to the message received, in the agent which has the next state unspecified.

The state where the arc starts is determined by the state of the machine, while the state where the arc arrives is chosen according to the reachability constraint.

To add an arc to a protocol agent, in the respect of the reachability constraint, has the following effects:

\- the set of reachable states does not change; the only change in the reachability graph is the appearance of some new arcs.

\- the next states of other transitions can become specified, with the possible change of classification of transitions themselves and of states.

## Transformation $RT\to ST$

Transforming a receive-unspecified transition into a send-unspecified transition means to make the next state unspecified for the agent sending the message.

To make a next state unspecified, it would be necessary to delete an arc from the protocol agent. To delete an arc from a protocol agent has the following effects:

\- one or more arcs are removed from the reachability graph; in this way some states which were reachable could become unreachable.

\- the next states of other transitions can become unspecified with the possible change of classification of transitions themselves and of states.

Since deleting an arc the reachability set could change, the algorithm we propose here does not make use of transformation RT → ST.

Adding an arc, the reachability set does not change and the protocol can only improve.

## Transformation $RT\to UT$

As it would be necessary to make the next state unspecified for the agents sending the message, this case is similar to transformation RT → ST. For the same reasons discussed above, our algorithm does not make use of transformations RT → UT.

![](/api/attachments/9Y3ZUNSA/fulltext/images/d90c06b538602a4b5c73ac39cb533ffd35d65f422b201184c7072efdb84b9972.jpg)  
Fig. 8. Modification to the protocol.

According to the previous considerations, the algorithm always attempts to transform receive-unspecified transitions into normal transitions; transformations RT → ST and RT → UT are not used in the algorithm, which is based on the rule to transform a receive-unspecified state into a normal state: all the receive-unspecified transitions of the state must be transformed into normal transitions.

We can see an example of solution of a receive-unspecified state in the protocol formed by the employee and the pay office.

In the state of machine $(s_{2}, s_{2})$ , where both agents are in state loan pending, the employee may send another loan request without the pay office being able to receive it.

It is necessary to allow the pay office to receive the message loan request, in the state loan pending. We must add an arc to the agent pay office, which starts from the state $s_{2}$ (loan pending), and arrives in another of its states, without modifying the reachability set of the protocol.

A possible solution is adding a self-loop in the state loan pending (S2), marked with the message +loan request.

This modification does not alter the reachability set (new states are not introduced in the protocol machine), and allows the pay office to receive a loan request in the state $s_{2}$ .

The modification can be seen in Fig. 8, and the new table of states and transitions is shown in Fig. 9. Now the protocol is correct because all its states are normal.

## Deadlock states (DLS)

A deadlock state is a state in which at least one agent can receive a message which is not sent by any other agent (send-unspecified transition ST). Moreover, the transition may not be specified for all agents exchanging the message (UT), and is neither a receive-unspecified (RT) nor a normal (NT) transition.

A deadlock state can be transformed into a normal state by transforming send-unspecified transitions (ST) or unspecified transitions (UT) into normal transitions.

TABLE OF TRANSITIONS AND STATES OF PROTOCOL MACHINE

<table><tr><td></td><td>(+g,-g)</td><td>(+d,-d)</td><td>(-p,+p)</td><td>(-a,+a)</td><td></td></tr><tr><td>(S0,S0)</td><td>(_,_)UT</td><td>(_,_)UT</td><td>(_,_)UT</td><td>(S1,S1)NT</td><td>NS</td></tr><tr><td>(S1,S1)</td><td>(S2,S2)NT</td><td>(S0,S0)NT</td><td>(_,_)UT</td><td>(_,_)UT</td><td>NS</td></tr><tr><td>(S2,S2)</td><td>(_,_)UT</td><td>(_,_)UT</td><td>(S0,S0)NT</td><td>(S2,S2)NT</td><td>NS</td></tr></table>

Fig. 9. Modified table of states and transitions.

## Transformation $ST\to NT$

The transformation technique is analogous to that described for transformation RT → NT; the only difference is that the next state is unspecified also for the agent sending the message, besides for some agents receiving the message.

## Transformation $ST\to UT$

The transformation technique is analogous to that described for transformation RT $\rightarrow$ NT; the only difference is that the next state is unspecified for all the agents exchanging the message.

## Transformation UT → NT

An unspecified transition UT is transformed into a normal transition with a technique similar to that adopted in the case of the transformation RT → NT. Arcs have to be added, corresponding to the message received (or sent), in the agents which have the next state unspecified.

## Dead-end states (DES)

In a dead-end state, all transitions are unspecified (UT).

A dead-end state can be transformed into a normal state by transforming one of the unspecified transitions UT into a normal transition NT.

Thus, the transformation will be of the type UT → NT, already discussed above.

## Discussion

It is important to underline that for the transformations $ST \rightarrow NT$ and $UT \rightarrow NT$ the property that the protocol can only improve it is not warranted (differently from the case of the transformation $RT \rightarrow NT$ ).

In fact, to add an arc relative to a message sending may make some transitions unspecified in the next state for the agent sending the message.

So, for states of the machine different from the one being considered, the following transformations may happen:

## ST → RT

## $\mathrm{UT}\rightarrow \mathrm{RT}$

As the introduction of even a single receive-unspecified transition (RT) changes the classification of the state in receive-unspecified state (RUS), it is obvious that the improvement of the protocol is not warranted. However, the correction algorithm converges, since the correction procedure may be iterated several times, and RUS can be only transformed into normal states NS, and not again into DLS or DES.

The effect of transformation from receive-unspecified transition to normal transition (RT → NT) is completely different; in fact, the transformation requires to add arcs relative to a message receiving. In states different from the one being considered the following transformations may happen:

$\mathrm{UT}\rightarrow \mathrm{ST}$

$\mathrm{RT}\rightarrow \mathrm{NT}$

The second kind of transformation is quite positive, of course. The first kind is not noxious, as a single send-unspecified transition (ST) is not a problem; the only change which may happen in states classification is that some dead-end states (DES) eventually become deadlock states, but this would not be a new problem. So the protocol can only improve.

The algorithm starts examining protocol correctness.

If the protocol is not correct, the algorithm tries to find solutions to the problems detected by attempting to transform each state into a normal state.

The criteria to transform states classified as RUS, DES or DLS into normal states have just been explained.

The user is asked to accept or refuse each solution found by the system.

When a solution is accepted, the system updates the columns of the table of states and transitions relative to the messages for which arcs have been added to the protocol agents.

After re-classifying the columns, the states of the protocol must be re-classified; at this point the algorithm starts again reconsidering protocol correctness.

It is important to underline that it is not sure that a correct solution for the protocol will be found.

In fact, it is possible that for some states no solution can be found with the criteria on which the algorithm is based, or that the user considers semantically meaningless all the solutions proposed for such states.

In these cases, finding a semantically correct solution to the errors in the protocol is outside of the scope of the algorithm and it is left to the user.

## 6. An example of verification of an office procedure

In this section, we present a complete example of modelization, analysis and modification of an office procedure.

The first step is to translate office procedure specifications into a protocol.

In particular, we refer to specifications expressed according the TCM (TODOS Conceptual Model) and using the TODOS Specification Language (TSL) [Per 87], developed within the TODOS project.

We consider the behaviour of a recruitment office. We translated TODOS specifications into a five agents protocol, as shown in Fig. 10:

(1) system

(2) chief

(3) interviewer

(4) secretary

(5) user

The user sends a request for a job to the recruitment office; the secretary receives the request and sends to the system (the system being designed, an automatic support for the recruitment office) a message posletter (position\_requested\_letter).

The system informs the chief there is a request by the message applh (application\_to\_handle).

The chief may immediately refuse the request by sending the message refdec (refusal\_decision) to the system, or may temporarily accept it by the message tempacc (temporary\_acceptance).

If a tempacc is sent the system schedules an interview between the user and an interviewer, sending the message not to the secretary.

The secretary informs the user and the interviewer with the multiple message notifica, formed by the components intnot and intconf, in order to communicate the date for the interview.

```txt
{ aggregation-of
    { envelope: aggregation-of
    { from: SYSTEM;
    to: secretary};
    contents: aggregation-of
    { c: copy-of acceptance_letter withall }
    }
}
```

After the interview, a report is sent to the system by the interviewer and the system informs the chief with the message reph (report\_to\_handle).

The chief must decide about the request, communicating his decision to the system with the messages refdec or accdec (acceptance \_decision).

The system informs the secretary of the chief's decision with the messages refmes (refusal\_message) and accmes (acceptance\_message); the secretary communicates the decision to the user with the messages refusal and acceptance.

We shortly discuss here how to transform TODOS specifications into a protocol; this can be done by abstracting information about message exchanges among office agents from the specifications.

For instance, the TODOS specification of message accmes (acceptance\_message) could be the following:

<acceptance\_message> is-a message;

![](/api/attachments/9Y3ZUNSA/fulltext/images/b01fd3c84d2189cde2d3301d75b3ae123290298c2b8bf3cc1f3e769b19114b3a.jpg)  
Fig. 10. Recruitment office.

![](/api/attachments/9Y3ZUNSA/fulltext/images/1a2f10ac79d1425cb9e9a3c9435a6099f700c370e8cb3885797c6370501057b4.jpg)  
Fig. 10. Recruitment office (cont'd).

From this specification we learn that the message is sent by the system and it is received by the secretary.

Through the concept of aggregation, the structure of this message is specified, and it can be graphically represented as follows:

![](/api/attachments/9Y3ZUNSA/fulltext/images/4167ce1ad89d61bc96d38beb73e0085295ee04b00ac91883849b66f3970e6512.jpg)

But in order to construct a protocol, this information is not sufficient: we need information about precedence relationships among messages.

In the TODOS Specification Language there is an optional field “follows” by which the designer can specify which messages precede the one being specified.

So in order to build a protocol the user must collect these specifications (if they are present); however, in order to perform protocol analysis, it is necessary to have a complete specification of the precedence relationships between messages. If this cannot be derived entirely from TODOS specifications, these must be completed with the help of the designer.

![](/api/attachments/9Y3ZUNSA/fulltext/images/5e85c8ebaeaaab2a43e1451f5fe0b193facd2337eda5a168c75c2bf7493efb28.jpg)  
N.B. notifica = (intconf, intnot)  
Fig. 11. Global precedence graph.

This part of the system is a first help to the designer in verifying the completeness of given specifications.

Complete information on precedence relationships can be graphically represented with a global precedence graph; the global precedence graph for our example is shown in Fig. 11.

We call this graph global because it represents precedence relationships among all the messages in the protocol.

From this graph, it is possible to obtain a precedence graph for each agent of the protocol; this can be done by ignoring all the messages in the global graph which are neither sent nor received from the agent being considered.

For example, the precedence graph for the agent user is shown in Fig. 12.

It is interesting to underline that in the graph of agent user message intnot appears instead of notifica; this is due to the fact that notifica is a multiple message and so the agent sending it (secretary) "sees" it with its global name (notifica), while the agents receiving it "see" it with the name of the received component (intnot for user and intconf for interviewer).

The use multiple messages in TODOS is exemplified in Fig. 13; event int triggers two different actions (ictx and intx), each of them sends a message (intconf and intnot). As these message sendings are simultaneous, intconf and intnot are treated as a multiple message, named notifica.

From each precedence graph we are able to build the protocol agent for the corresponding office agent.

![](/api/attachments/9Y3ZUNSA/fulltext/images/2767213384955fab46e463b6615bbc01c06f2637abe0384270a513764ca2ff78.jpg)  
Fig. 12. Precedence graph for agent user.

![](/api/attachments/9Y3ZUNSA/fulltext/images/f20b171d9a6e0186019dff862457347687a1cc3ee04317c0914e16219ed8592f.jpg)  
Fig. 13. Multiple message sending.

Exploring the graph from the root to the leaves and starting from the initial state $s_{0}$ of the protocol agent, for each message in the graph we must add an arc labeled with this message (preceded by + if the agent receives the message, and by – otherwise); this arc starts from the current state and arrives at a new state.

In case of messages related by an XOR, we must add a new arc for each message in XOR; each of this new arcs starts from the current state and arrives at new state which is different for each of them.

Messages which are leaves in precedence graph origin arcs starting from the current state and arriving at the initial state $s_{0}$ .

The protocol agent shown in Fig. 10.4 for agent user is shown in Fig. 12; it has been built from the precedence graph of agent user following the criteria explained above.

Protocol agents for the other office agents can be built in a similar way.

It is important to underline that in TODOS specifications the agent user is not explicitly modelized; as we intend to study message exchanges, it has been necessary to make an explicit modelization of this agent, while the agent user is implicit in TODOS, since he does not interact directly with the system.

The protocol we have presented is correct.

We will modify it taking away an arc, in order to show how our system reacts in the case of an incorrect protocol.

We can take away the arc +refusal from the agent user, which connects the states $s_{0}$ and $s_{1}$ . With this change we introduce a receive-unspecified problem in the machine's state formed by:

agent system in state $s_{0}$

agent chief in state $\mathbf{s}_0$

agent interviewer in state $s_{0}$

agent secretary in state $s_{3}$

agent user in state $s_{1}$ .

In fact in this reachable machine's state the secretary (in state $s_3$ ) is able to send the message refusal, while the user (in state $s_1$ ) is unable to receive it.

The analysis and diagnosis system informs the office designer of the problem in the protocol with a display message like the following one:

A RUS has been identified.

A RUS is a receive-unspecified state, i.e. a state where one or more messages may be sent without the receiver being in a correct state to receive them.

List of RUS states.

The following state is a RUS.
agent system is in state 0
agent chief is in state 0
agent interviewer is in state 0
agent secretary is in state 3
agent user is in state 1

The message refusal is responsible of a rt between the agent secretary in state 3 and the agent user in state 1.

Do you want solution proposals? (y/n)

If we want to examine system's proposals, we must reply y (yes) to the system's query. So it proposes the following solution:

Solution proposal for the RUS
agent system in state 0
agent chief in state 0
agent interviewer in state 0
agent secretary in state 3
agent user in state 1

Add an arc + refusal for the agent user from the state 1 to the state 0.

Do you accept the solution? (y/n)

The proposal suggests us to add an arc, marked with the message refusal, from the state $s_{1}$ to the state $s_{0}$ , for the agent user.

So the user becomes able to receive the message refusal when it is in the state $s_{1}$ , and the message it not lost.

The arrival state $s_{0}$ has been chosen by the system according to the reachability constraint and the reachability set is not changed.

We can see that the arc added is the same which we removed to make the protocol uncorrect, and the system has restored the initial situation.

In this modification we removed an arc + refusal, but there was another arc + refusal in the protocol, so that the preliminary checks detect nothing anomalous.

If we had removed the arc -accmes from the agent system, it would had not been necessary to go through protocol analysis to show this protocol is uncorrect. The preliminary checks warn the office designer with the message:

The message accmes, received by the agent secretary when it is in state 5, is not sent by any agent.

This check prevents an unsuccessful analysis when the protocol shows evident inconsistent features.

## 7. Concluding remarks

In this paper we presented a theoretical approach to generalized office protocol analysis. The protocol model is based on finite state automata theory and allows simultaneous exchange of complex messages among different office workers.

Based on this approach, a system has been built, which is able to identify protocol errors and to propose possible solutions to the designer to eliminate the errors. The theory underlying error correction is presented in the paper.

A system for analysis and diagnosis has been implemented in Prolog.

Diagnosis requires an interactive language in order to permit user's approval of the solutions presented by the system and a flexible structure for easy modifications of office protocols.

Prolog has been chosen as programming language because of its structure in facts and rules. The algorithms on which analysis is based have been easily translated into Prolog rules because of the peculiar nature of the problem. Prolog as a language with good interactive capability and with a database of facts showed itself a good choice.

Future work will be the integration of the message analyzer into the TODOS tool environment, enriching some of its support features.

## Acknowledgements

This work has been partially supported by the Commission of European Communities under ESPRIT Programme, Project N. 813 TODOS (TOols for Designing Office Systems)

## References

[Bou 85] Bouzeghoub, M., Gardarin, G., and Metais, E., “Database design tools: an expert system approach”, Proc. 11th Int. Conf. on Very Large Databases, Stockholm (1985).

[Bra 84] Bracchi, G. and Pernici, B., “The design requirements of office systems”, ACM Trans. on Office Information Systems, Vol. 2, No. 2, pp. 151–170 (April 1984).

[Caz 88] Cazzola, F. and Galli, M., “Analisi e diagnostica per la verifica degli scambi di messaggi nelle procedure d’ufficio”, Graduation Thesis, Dept. of Electronics, Politecnico di Milano, in Italian (1988).

[Cer 83] Ceri, S. (Ed.), Methodology and Tools for Database Design, North Holland (1983).

[Cer 86a] Ceri, S. and Gottlob, G., “Normalization of relations and Prolog”, Comm. of the ACM, Vol. 29, No., 6 (June, 1986).

[Cer 86b] Ceri, S., “Requirements collection and analysis in information systems design”, Information Processing '86, Elsevier Science Publ., North Holland (1986).

[Cha 81] Chang, S.K., “A model for information exchange”, International Journal of Policy Analysis and Information Systems, Vol. 5, No. 2 (1981).

[Cha 82] Chang, S.K., “Protocol Analysis for Information Exchange”, International Journal of Policy Analysis and Information Systems, Vol. 6, No. 1 (1982).

[Cha 84] Chang, S.K., “Office Information System design”, in: Management and Office Information Systems, Edited by Shi-Kuo Chang, Plenum Publishing, Corporation (1984).

[Cha 85] Chang, S.K. and Chan, W.L., “Transformation and verification of office procedures”, IEEE Transactions on Software Engineering, Vol. SE-11, No. 8, pp. 724–734 (August 1985).

[DaE 84] Database Engineering Journal, Special Issue on Database Design Aids, Methods, and Environments Vol. 7, No. 4 (Dec. 1984).

[DeM 79] De Marco, T., "Structured Analysis and System Specification", Prentice Hall, Englewood Cliffs, New Jersey (1979).

[Ell 79] Ellis, C.A., “Information control nets: a mathematical model of office information flow”, Conference on Simulation, Measurement and Modeling of Computer Systems, pp. 225–239 (1979).

[Flo 80] Flores, F. and Ludlow, J.J., “Doing and speaking in the office”, In Decision Support Systems: Issues and Challenges, G. Fich and R. Sprague Eds., Pergamon Press (1980).

[Fre 85] Frenkel, C.A., "Toward automating the software development cycle", CACM, Vol. 28, No. 6 (June 1985).

[Hor 85] Horak, W., “Office Document Architecture and office Document Interchange Formats: current status of international standardization”, Computer, pp. 50–60 (Oct. 1985).

[Kon 82] Konsynski, B.R., Bracker, L.C., and Bracker, W., “A model for specification of office communications”, IEEE Transactions on Communications, Vol. COM-30, No. 1 (January 1982).

[Loc 88] Lochovsky, F.H., Hogg, J.S., Weiser, S.P., and Mendelzon, A.O., "OTM: Specifying office tasks", Conf. on Office Information Systems, Palo Alto, CA (March 1988).

[Mer 79] Merlin, P.M., “Specification and validation of protocols”, E.E. Publication No. 34, Faculty of Electrical Engineering, Technion, Haifa, Israel (January 1979).

[Pan 84] Panko, R.R., “38 offices: analyzing the needs in individual offices”. ACM Trans. on Office Information Systems. Vol. 2, No. 3 (July 1984).

[Per 86] Pernici, B. and Vogel, W., “An integrated approach to OIS development”, ESPRIT Technical Week '86. North-Holland (September 1986).

[Per 87] Pernici, B., Barbic, F., Fugini, M.G., Maiocchi, R., Rames, J.R., and Rolland, C., “C-TODOS: an automatic tool for office system conceptual design”, ACM Trans. on Information Systems, Vol. 7, No. 4, pp. 378–419 (1989).

[Per 88] Pernici, B. and Verrijn Stuart, A. (eds.), “Office Information Systems the Design Process”, Proc. of IFIP WG 8.4 Working Conference, Linz (Aug. 1988).

[Pet 77] Peterson, J.L., "Petri Nets", Computing Surveys, Vol. 9, No. 3 (September 1977).

[Per 90] Pernici, B. and Rolland, C. (Eds.), “Automatic Tools for Designing Office Information Systems. The TODOS Approach”, ESPRIT Research Report Series, Springer Verlag (1990).

[Rol 86] Rolland, C. and Proix, C., “An expert system approach to information system design”, Information Processing '86, Elsevier Science Publ., North Holland (1986).

[Was 82] Schneider, H.-J. and Wasserman, A.I. (Eds), “Automated Tools for Information System Design”, North Holland (Jan. 1982).

[Zis 78] Zisman, M., “Use of production systems for modeling asynchronous, concurrent processes”, In Pattern Directed Inference Systems, Waterman and Hayes-Roth, Eds., Academic Press, New York, pp. 53–68 (1978).
