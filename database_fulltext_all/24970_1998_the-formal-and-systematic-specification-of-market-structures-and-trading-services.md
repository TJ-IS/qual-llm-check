---
otero_id: 24970
otero_key: "AZ9QV9G9"
title: "The Formal and Systematic Specification of Market Structures and Trading Services"
authors: "Martin Reck"
year: "1998"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1998.11518206"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Formal and Systematic Specification of Market Structures and Trading Services

Martin Reck

To cite this article: Martin Reck (1998) The Formal and Systematic Specification of Market Structures and Trading Services, Journal of Management Information Systems, 15:2, 9-21, DOI: 10.1080/07421222.1998.11518206

To link to this article: http://dx.doi.org/10.1080/07421222.1998.11518206

![](/api/attachments/AZ9QV9G9/fulltext/images/c932223361b0fe63f8930c80e50a73cea07c0c983e0253f9362b95494355587e.jpg)

Published online: 07 Dec 2015.

![](/api/attachments/AZ9QV9G9/fulltext/images/1513b5f249adfc2c5cc4bd01fe36a894d5c4d8ed8befc1e2760da20048c4107f.jpg)

Submit your article to this journal

![](/api/attachments/AZ9QV9G9/fulltext/images/ed50405b7ef0dba16e7fc018a783e7d8124208f4122737fab2887f4def17c1be.jpg)

View related articles

# The Formal and Systematic Specification of Market Structures and Trading Services

MARTIN RECK

MARTIN RECK is Head of Market Design and Functionality of Deutsche 80rse AG, Frankfurt, Germany. In this function he is responsible for the design of market structures and the functionial concepts of Deutsche 8orse's trading systems, among them Xetra and the floor systems of the Frankfurt stock exchange. Martin Reck holds a degree in computer science from the University of Dortmund, Germany and is currently completing a Ph.D. in business administration at St. Gallen University, Switzerland.

ABSTRACT: This paper supplies methodological support for trading system development. It provides a formal framework for the systematic definition of market structures and the specification of trading services. Market structure describes the interaction among traders, and trading services identifies the trading system interface and the description of the system behavior. The framework provides guidance in applying "trace specifications" as a formal description technique for both market structure and trading services. It also details how to formally assess market structure and trading service properties. Moreover, the framework introduces concepts for building market structure taxonomies that support the systematic search and development of alternative forms of markets. The taxonomies are collections of trace specifications for market structures with specialization and extension relationships defined between them. Improvements in market quality and efficiency should result from such a disciplined and systematic approach to market structure and trading services definition and implementation.

KEY WORDS AND PHRASES: electronic trading, financial markets, market structure, specification languages.

## Motivation

INFORMATION TECHNOLOGY IS THE MAIN DRIVER FOR TODA Y'S market innovations. Advances in information technology have made electronic trading systems technically feasible, and the lower costs of computing and communication make their development and operation economically reasonable. Competitive pressure arising from trading service innovators can make the transition to electronic trading for established exchanges and other market providers unavoidable. For example, exchanges in Frankfurt, Paris, and Stockholm implemented reforms and developed new market systems in the early 1990s in response to the growing volume of trading that had migrated to London after the London Stock Exchange rolled out its SEAQ International market in 1985.

Markets increasingly need to use systems to remain efficient, yet trading system construction is a complex, multistep process. It starts from a market structure definition and leads to a trading service specification, a trading system design, and, finally to system implementation.

A market structure definition describes the exchange of messages between traders as they seek to reallocate assets among themselves. The definition determines the range of messages available to traders and restricts the set of message sequences they may cause. It also defines how certain message sequences translate into trades. The next step, trading service specification, describes functional characteristics of the trading system. It identifies the trading system's interface, distinguishes input and output messages, and specifies the trading system's "behavior," which denotes the way it transforms a sequence of input messages into a sequence of output messages. Then, system design takes the interface specification and decomposes the system described as a single component into a number of communicating subcomponents. The result is a network of subcomponents connected by data channels with an external operation that should fulfill the behavior specification of the previous level.

Typically, electronic trading systems comprise components for order routing, order management, and trade generation, as well as for order and trade information dissemination. In the final development step, for each component and communication channel some specific hardware and software implementation has to be developed and rolled out. Assuming that an electronic trading system is the only interaction medium for a specific group of traders, its behavior completely determines the way traders may interact. Thus, it constitutes a specific market structure, and traders choose it as their trading platform if they find that the system constitutes a market that serves theirneeds.

Obviously, the match of the market structure implemented and the market structure demanded is most critical for the success of an electronic trading system. The market structure definition and the subsequent development of a trading service specification appear to be the two critical development steps for establishing the match of demand and the implemented system. In brief, the requirements for a specific market structure must be captured and transferred into some market structure design. Because of its complexity, this task has to be carried out systematically and iteratively. A market structure definition may start from scratch or with a market model description already given. In either case, alternative market forms have to be considered, market structure similarities and differences need to be identified, and several adjustments lead to definitions of new market structures. The whole process has to be carried out carefully, and the result needs to be validated thoroughly, since market structure design is the first description of traders' wishes and the starting point of the entire development process. The transition to a trading service specification has to carry over the previously stated market structure requirements into a behavioral specification of the trading system. That specification effort progresses from the global view taken in the market structure definition to a component-oriented view that captures the trading system's behavior. At that stage of the specification, the trading system, together with components in its environment, build a "network," and the sequence of messages observable in that network should reflect the interaction of the market structure definition. If control of market interaction is not described as being completely shifted to the trading system component, then the behavior of market components located in the trading system's environment need to be specified, too. Assuming that an electronic trading system takes complete control of market interaction, such that the trading system with the interface and input/output behavior it provides to traders is the only interaction medium, then all restrictions imposed on the interaction should at some stage of the trading service specification be completely reflected in the trading system's specification. Still, the specified interaction should equal that of the market structure design, although it is under the control of a single component in the center of interaction, the trading system.

## Specifying Market Structures and Trading Services

THIS SECTION EXPLAINS HOW TO APPLY "TRACE SPECIFICATIONS," a concept presented in [2] and [3], for the description of market structures and trading services. For both market structures and trading services, respective system models from institutional economics and computer science will be sketched. Both the market institution part in the model of a microeconomic system and models of distributed systems as employed in computer science describe the structure as a network of communicating agents. Thus, requirements for an adequate modeling technique are the same for both. We will exploit that and show how the formalism of trace specifications can be applied to the description of market structures and trading system behaviors.

## Models of Markets and Distributed Systems

First, we illustrate the requirements for a description technique for market structures to be derived from the model of micro economic systems as employed in institutional economics [10]. A microeconomic system, according to Smith, consists of two components, an "environment" and an "institution." Of interest for our purposes is the institution part. An institution defines the rules of property under which agents are allowed to communicate and exchange commodities with the purpose of modifying initial allocations. In general, the institution defines rights of ownership, the right to demand payment or delivery, and the rules of communication.

The institution also specifies a language of messages and denotes the messages that an agent is allowed to send. It prescribes a set of allocation rules that determine the distribution of commodities between agents. The result defines the final allocation of commodities to agents as a function of the sequence of all messages sent. An institution further defines the payments to be made by each agent as a function of messages sent. Finally, it specifies a set of process rules. They are starting rules, stopping rules, and transition rules, which define the sequence of messages that an agent may send. The central point of the model is the assumption that the final allocation of resources through an institution is determined through the exchange of messages by participating agents. "Agents choose messages, and institutions determine allocations via the rules that carry messages into allocations. There is a social process that culminates in exchange" [10].

## Messages and Components in a Distributed System

The concept of message exchange between agents is also used in models of distributed computer systems [1]. Originally, computer systems were understood as recipients of input values that sequentially compute output as the result of evaluating a function. For example, technology and advanced application demands have led to the use of computers as components in systems of interactive humans, computers, machines, or other artificial and natural components. For these systems, the term "distributed system" is now widely used. It denotes a family of interacting and conceptually or spatially distributed components. A computer can be an integrated part of such a distributed system but can itsdf also be built of interacting distributed components.

Markets as described by Smith can be thought of as distributed systems. Computer science provides a range of models to describe distributed systems. We want to look at the models developed in [2] and [3], where global and component-oriented models of distributed systems are distinguished. In a global view, the system under consideration is described as a whole without any structure provided for its components. The focus of the global description is on the behavior of the system. At this level, it is described through the set of all allowed system runs. System runs in the case of a distributed system are finite or infinite sequences of actions. These runs are called "traces." A trace can be thought of as produced by an observer with a notebook who watches the process and write:s down the name of each event as it occurs [6].

Traces represent the history of actions the system may perform. Actions in a trace are regarded as being atomic and instantaneous (for sequential models of organizational processes, also see [8]). Following this trace scheme, we can also imagine a global observer who records the exchange of messages in a market. That way, the market structure observed would lead to a model that comprises the set of traces that can be recorded. A specification that describes the set of all traces in a market can be used to determine the structure of that market.

## Specifications

The next section proposes dt:finitions of market structures by trace specifications. From a global viewpoint, they prescribe the sequences of messages that may occur in the envisaged market structure. We call such a description a "market structure definition." Trace specifications that are component oriented [3] describe distributed systems as networks of components that exchange messages asynchronously across directed communication links. A single component is connected to one or more other components by input and output channels. The direction of a channel determines whether it is for input to or output from the attached components. Messages are assigned to each channel and constitute input and output actions for the components linked. Input and output actions constitute the "syntax" of a component. Then, a component is determined by its input/output behavior, its "interface." Again, the interface of a component can be determined through a trace specification on input and output actions.

This paper applies the component-oriented specification style for outlining trading services. We assume that a single component, the envisaged trading system, in this case forms the component to be further developed. It is located at the center of a trader network. Traders are exclusively linked to the trading system component to use it for their interaction. We call the description ofthat component a "trading service specification."

## Trace Specifications of Market Structures and Trading Services

## Terminology

This section presents the application of trace specifications [3] for the definition of market structures and trading services. "Traces" are finite or infinite sequences or "streams" of actions. Given a set of items S, the set of streams over S is denoted by Sro. It is defined as the union of the finite and infinite sequences over S: $S \omega = S ^ { * } \cup S .$

The basic operations and relations defined on streams are the following. Let s, t, U be streams and $a , b , c$ be items,

E denotes the empty stream.

$< s _ { 1 } , \ldots , s _ { n } >$ denotes the stream that contains the elements $s _ { 1 } , \ldots , s _ { n } .$

${ \mathcal { f } } t ( s )$ returns the first element of s, if s is not empty;ft(E) delivers $\perp ( \mathrm { " u n d e f i n e d " } )$ rt(s) returns the stream in which the first element of s is deleted.

a&s denotes the stream where a is prefixed to s. If a is defined, that is, $a \perp , f t \left( a \& s \right)$ $= a \ \mathrm { a n d } \ r t ( a \& s ) = s .$

s . t denotes the concatenation of the streams sand t. If s is an infinite stream, s . t is equal to s.

s pre t denotes that s is a prefix of t, that is, :3 u: s . u = t.

a in s yields true if a occurs in s.

#s delivers the length of s, if s is infinite.

$a \circledast s ,$ a filter operation, results in a substream of s that only consists of a-elements, such as a $\mathbb { C } < a \cdot c \cdot b \cdot c \cdot a > = < a \cdot a >$ . The operation may be extended so that the first operand is a set of items.

Formally, traces over an action set Act can now be regarded as streams over Act. They are denoted by:

$\mathbf { A c t } \mathbf { \omega } = \mathbf { A c t ^ { * } } \cup \mathbf { A c t } .$ , where $\mathsf { A c t } ^ { * }$ refers to the set of finite traces, Act to the set of infinite traces over Act.

A trace specification is defined as a pair $( \mathsf { A c t } , P )$ . Act denotes a set of actions, P is a predicate P: Actro\~{true, false}. When trace specifications are used for defining systems, Act denotes the set of actions the system is expected to perform, andP defines those traces that represent the system behavior. P is a formula of predicate logic with a free variable of sort Actro.

## Examples

The following example illustrates the concept. The system under consideration is that ofa simple market; it is based on the action set $\mathsf { A c t } _ { A } = \{ \mathsf { e n t e r } . b ,$ ente $f ,$ trad $\cdot ( b , f ) \mid b$ $\in \mathrm { B i d } , f \in \mathrm { O f f e r } \}$ . enter.b and enter $\cdot f$ denote actions by which bids $b \in$ Bid and offers $f \in$ ffer are submitted to the market. $\mathtt { T r a d e } ( b , f )$ denotes the action by which a trade with constituent parts b andfis formed. We define the sets Bid and Offer as Bid = $\mathrm { O f f e r } = \{ ( a , t , p ) \mid a \in \mathrm { A s s e t }$ , t E Trader, $p \in \mathtt { P r i c e } \}$ . Asset and Trader are elementary sets of names,p is equal to the set of decimal numbers with an ordering relation defined upon it (for an example of a trading system specification that includes quantity as an attribute of orders, see [9]). We now want to describe a market that should exhibit the following simple behavior:

• Only bids and offers submitted may occur as constituent parts of trades.

• Each bid and offer is uniquely identified and may be submitted only once.

• Each bid and offer submitted may occur in a trade only once.

• Once entered, all bids and offers submitted eventually occur in a trade.

The predicates listed below define that behavior. The first requirement is captured by predicate $S _ { \imath }$ (let t denote a trace over $\operatorname { A c t } _ { A } )$

$$
S _ {1} (t) \equiv \forall b \in \text { Bid }, f \in \text { Offer }, t ^ {\prime} \in \operatorname{Act} _ {A} ^ {*}:
$$

t' . trade (bj) pre t \~ enter.b in $t ^ { \prime } \wedge$ enterfin $t ^ { \prime }$ .

The second requirement is expressed by $S _ { 2 } \mathrm { : }$

$$
S _ {2} (t) \equiv \forall b \in \text { Bid }, f \in \text { Offer }, t ^ {\prime} \in \operatorname{Act} _ {A} ^ {*} \colon t ^ {\prime} \text { pre } t \Rightarrow
$$

$$
\# (\text { enter }. b \circledcirc t ^ {\prime}) 1 \wedge \# (\text { enter }. f \circledcirc t ^ {\prime}) 1.
$$

$S _ { 3 }$ formalizes the third requirement:

$$
S _ {3} (t) \equiv \forall b \in \text { Bid }, f \in \text { Offer }, t ^ {\prime} \in \operatorname{Act} _ {A} ^ {*}: t ^ {\prime} \text { pre } t \Rightarrow
$$

$$
\# (\{\text { trade } (b ^ {\prime}, f) | b ^ {\prime} \in \text { Bid } \} Ⓒ t ^ {\prime}) \quad 1.
$$

The fourth requirement is fonnalized by $L _ { 1 }$ and $L _ { 2 } \mathrm { . }$

$$
L _ {1} (t) \equiv \forall t ^ {\prime} \in \operatorname{Act} _ {A} ^ {*}, b \in \text { Bid }: t ^ {\prime} \text {   pre   } t \wedge \text {   enter }. b \text {   in   } t ^ {\prime} \Rightarrow
$$

$$
\exists t ^ {\prime \prime} \in \operatorname{Act} A ^ {*}, f \in \text { Offer: } t ^ {\prime} \cdot t ^ {\prime \prime} \text { pre } t \wedge \operatorname{trade} (b, f) \text { in } t ^ {\prime \prime}.
$$

$$
L _ {2} (t) \equiv \forall t ^ {\prime} \in \operatorname{Act} A ^ {*}, f \in \text { Offer: } t ^ {\prime} \text { pre } t \wedge \text { enter }. f \text { in } t ^ {\prime} \Rightarrow
$$

$$
\exists t ^ {\prime \prime} \in \operatorname{Act} A ^ {*}, b \in \text { Bid }: t ^ {\prime} \cdot t ^ {\prime \prime} \text {   pre   } t \wedge \text { trade } (b, f) \text {   in   } t ^ {\prime \prime}.
$$

The conjunction of the predicate $S _ { 1 } , S _ { 2 } , S _ { 3 } , L _ { 1 }$ , and $L _ { 2 }$ forms $A ( t ) \equiv S _ { 1 } ( t ) \land S _ { 2 } ( t ) \land S _ { 3 } ( t )$ $\setminus L _ { 1 } ( t ) \land L _ { 2 } ( t )$ defining the set $T = \{ t \in \operatorname { A c t } _ { A } \omega | \operatorname { A u c t } ( t ) \}$ of traces the market is allowed to perform. The specification we get has the form $M _ { A } = ( \mathsf { A c t } _ { A } , A )$

The specification example illustrates two different kinds of system properties, so-called safety and liveness properties [3]. $S _ { 1 } , S _ { 2 }$ ' and $S _ { 3 }$ are examples of predicates that define safety properties. They express that "nothing bad does happen" and refer to all finite prefixes of traces. Their violation can be detected after a finite amount of time, by examining a sufficiently large prefix of a trace.

Let us look at $S _ { 2 }$ as an example of a safety predicate. If the entry of a bid b or an offe $f$ would occur more than once in trace $t ,$ then this failure could be detected by analyzing t step by step from the beginning. In other words, the safety predicate $S _ { 2 }$ holds for t if it is valid for all finite prefixes of t.

Predicates $L _ { 1 }$ and $L _ { 2 }$ are examples of live ness predicates in the specification above. They demand that bids and offers entered are eventually matched. Liveness properties demand that "eventually something good does happen" in a system run. The violation of a liveness property can only be detected after a complete, possibly infinite, observation.

Trace specifications as introduced above do not account for a structuration of a system into components; requirements stated address the system as a whole. The step toward a component-oriented system specification is conducted by identifying and specifying system components [3].

Each component can be specified by a tuple $( I , O { , } C )$ with $I \cap O = \emptyset$ and $C \colon ( I \cup$ $O ) { \mathfrak { o } } \to$ {true, false}. $( I , O { , } C )$ is called component specification. A set of input actions I and output actions a constitute the system component's interface. C specifies the component's interface behavior. Sets I and a are required to be disjoint so that input actions and output actions can be distinguished in traces.

A system can now be considered as a structure of separate components, each given by a component specification $( I _ { 1 } , O _ { 1 } , C _ { 1 } ) , ( I _ { 2 } , O _ { 2 } , C _ { 2 } ) , \dots , ( I _ { n } , O _ { n } , C _ { n } )$ where $O _ { i } \cap O _ { i } = \emptyset$ for $i \neq j$ Output action sets are required to be disjoint so that outputs can uniquely be assigned to one component. Components are understood as being connected, if an output action of one component is the input action of the other.

$S \colon ( I 1 \cup . . . \cup I _ { n } \cup O _ { 1 } \cup . . . \cup O _ { n } ) \omega $ {true, false} as defined by $S ( t ) \equiv \forall i \in \left\{ 1 , \ldots , n \right\}$ $C _ { i } ( ( I _ { i } \cup O _ { i } ) \circledcirc t )$ determines system behavior as the result of the interplay of individual system components.

Let us now apply this framework to the market previously specified by $M _ { A } = ( \mathbf { A c t } _ { A }$ A). The global specification is further developed by transforming it into a componentoriented specification (see figure I).

Within the trading system specification, the same method of the specified market structure can be applied to the specification of elements of the trading system. The two components identified are a trading system and an environment component. The component specification for the system takes the form $M _ { T S } = ( I _ { T S } , O _ { T S } , T S )$ with trace predicate TS: $I _ { T S } \cup O _ { T S } $ {true,false} defining the system's interface behavior.

The environment takes the form $M _ { E } = ( I _ { E } , O _ { E } , E )$ ' accordingly. Sets of input and output actions are defined as $I _ { T S } = O _ { E } = \{ \mathrm { e n t e r } . b , \mathrm { e n t e r } . f | b \in \mathrm { B i d } , f \in \mathrm { O f f e r } \}$ and $O _ { T S }$ $= I _ { E } = \{ { \mathrm { t r a d e } } ( b , f ) | b \in { \mathrm { B i d } } , f \in { \mathrm { O f f e r } } \}$

The conjunction of the four predicates below defines the trading system's behavior:

$$
T S (t) \equiv T S _ {1} (t) \wedge T S _ {2} (t) \wedge T S _ {3} (t) \wedge T S _ {4} (t),
$$

where $t \in \mathsf { A c t } _ { A } = I _ { T S } \cup O _ { T S }$

$$
T S _ {1} (t) \equiv \forall b \in \text { Bid }, f \in \text { Offer }, t ^ {\prime} \in \text { Act } A ^ {*}:
$$

![](/api/attachments/AZ9QV9G9/fulltext/images/6a9cc8c929ed8aa868c5b4df2c3bccae17b9c4af09f277eee1e7aaca935ae7e6.jpg)  
Figure 1. Trading System and Environment

I' . trade (b,j) pre $t \Rightarrow { \mathrm { e n t e r } } . b$ in $t ^ { \prime } \wedge$ enterfin $t ^ { \prime }$ .

$$
T S _ {2} (t) \equiv \forall b \in \text { Bid }, f \in \text { Offer }, t ^ {\prime} \in \text { Act } A ^ {*}: t ^ {\prime} \text { pre } t \Rightarrow
$$

$$
\# (\{\text { trade } (b, f ^ {\prime}) \mid f ^ {\prime} \in \text { Offer } \} Ⓒ t ^ {\prime}) \quad 1 \wedge
$$

$$
\# (\{\text { trade } (b ^ {\prime}, f) \mid b ^ {\prime} \in \text { Bid } \} Ⓒ t ^ {\prime}) \quad 1.
$$

$$
T S _ {3} (t) \equiv \forall b \in \text { Bid }, f \in \text { Offer }, t ^ {\prime}, t ^ {\prime \prime} \in \text { Act } A ^ {*}:
$$

$$
t ^ {\prime} \cdot \text { enter. } b \cdot t ^ {\prime \prime} \cdot \text { enter. } f \text {   pre   } t \wedge \text { matching   } (b, f) \Rightarrow
$$

$$
t ^ {\prime} \cdot \text { enter. } b \cdot t ^ {\prime \prime} \cdot \text { enter. } f \cdot \text { trade } (b, f) \text { pre } t
$$

$$
T S _ {4} (t) \equiv \forall b \in \text { Bid }, f \in \text { Offer }, t ^ {\prime}, t ^ {\prime \prime} \in \operatorname{Act} _ {A} ^ {*}:
$$

$$
t ^ {\prime} \cdot \text { enter } f \cdot t ^ {\prime \prime} \cdot \text { enter }. b \text {   pre   } t \wedge \text { matching   } (b, f) \Rightarrow
$$

$$
t ^ {\prime} \cdot \text { enter } f \cdot t ^ {\prime \prime} \cdot \text { enter } b \cdot \text { trade } (b, f) \text { pre } t
$$

Predicates $T S _ { 1 }$ and $T S _ { 2 }$ are equal to $S _ { 1 }$ and $S _ { 2 } . T S _ { 3 }$ expresses that a trade occurs as the next action if the offer matches the standing bid. $T S _ { 4 }$ formalizes the same property with an offer entered first.

Predicate matching: Bid $\times \mathrm { O f f e r }  \{ \mathrm { t r u e , f a l s e } \}$ determines the conditions for a trade to occur\~hat is, when a bid and offer match: matching $( [ a , b , p ] , [ a ^ { \prime } , b ^ { \prime } , p ^ { \prime } ] ) \Leftrightarrow$ $a = a ^ { \prime } \wedge b b ^ { \prime } \wedge p p ^ { \prime }$ . Behavior of the environment has to satisfy predicates:

$$
E _ {1} (t) \equiv \forall b \in \text { Bid }, f \in \text { Offer }, t ^ {\prime} \in \operatorname{Act} _ {A} ^ {*}: t ^ {\prime} \text { pre } t \Rightarrow
$$

$$
\# (\text { enter }. b \circledcirc t \in) \quad 1 \wedge \# (\text { enter }. f \circledcirc t ^ {\prime}) \quad 1.
$$

$$
E _ {2} (t) \equiv \forall t ^ {\prime} \in \operatorname{Act} _ {A} ^ {*} b \in \text { Bid: } t \in \cdot \text { enter. } b \text { pre } t \Rightarrow
$$

$$
\exists t ^ {\prime \prime} \in \operatorname{Act} _ {A} ^ {*}, f \in \text { Offer: }
$$

$$
t ^ {\prime} \cdot \text { enter. } b \cdot t ^ {\prime \prime} \cdot \text { enter. } f \text { pre } t \wedge \text { matching } (b, f) .
$$

$$
E _ {3} (t) \equiv \forall t ^ {\prime} \in \operatorname{Act} A ^ {*}, f \in \text { Offer: } t ^ {\prime} \cdot \text { enter. } f \text { pre } t \Rightarrow
$$

$$
\exists t ^ {\prime \prime} \in \operatorname{Act} _ {A} ^ {*}, b \in \operatorname{Bid}:
$$

$$
t ^ {\prime} \cdot \text { enter. } f \cdot t ^ {\prime \prime} \cdot \text { enter. } b \text {   pre   } t \wedge \text { matching } (b, f)  .
$$

Predicate $E _ { 1 }$ is equal to $S _ { 2 } .$ ' Predicate $E _ { 2 }$ expresses that an offer f eventually follows to match a bid b previously entered. $E _ { 3 }$ defines the same condition for an offer submitted.

The three predicates above constitute $E ( t )$ as follows: $E ( t ) \equiv E _ { 1 } ( t ) \land E _ { 2 } ( t ) \land E _ { 3 } ( t )$ . In order to show correctness of the split into a system component specification and a specification of the environment proof of $T S ( t ) \land E ( t ) \Rightarrow A ( t )$ must be carried out.

## The Specification of Time

The behavior of markets and trading systems can be bound to certain time conditions that, for instance, define the starting time, the duration of the market process, termination time, or the required response time of a trading system. We follow the concept as presented in [3].

Time is represented by the "ticking" of a global clock introduced into specifications. Technically, an additional action $A ( ^ { \circ } \mathfrak { t i c k } ^ { \prime \prime } )$ is introduced, which occurs in traces. It can be assumed to occur in traces when no other action takes place at the same time. "Ticks" occur after intervals of real time that have constant length. Formally, timed traces are elements of $( \mathbf { A c t } \cup \{ \} ) ^ { * } ,$ ; they are infinite, since the clock is assumed not to stop. The set of timed traces as defined above is denoted by $\mathsf { A c t } _ { A } \mathsf { \omega }$ . Timed traces with a finite number of actions are denoted by $\mathsf { A c t } _ { A } ^ { * }$

We extend the specification of the market given in the previous sections by the requirement that each bid and offer should be acknowledged not later than N units after entry:

$$
\begin{array}{l} T 1 (t) \equiv \forall b \in \text { Bid }, t ^ {\prime} \in \operatorname{Act} _ {A} ^ {*}: t ^ {\prime} \cdot \text { enter }. b \text { pre } t \Rightarrow \\ t ^ {\prime \prime} \in \operatorname{Act} _ {A} ^ {*}: t ^ {\prime} \cdot \text { enter }. b \cdot t ^ {\prime \prime} \cdot \text { ack }. b \text { pre } t \wedge \\ \# (\quad ⓒ t ^ {\prime \prime}) \quad N. \end{array}
$$

Action ack.b denotes the market's confirmation of a bid b. $T _ { 2 } ( t )$ requires the same condition to hold for offers.

$$
\begin{array}{l} T _ {2} (t) \equiv \forall f \in \text { Offer }, t ^ {\prime} \in \text { Act } _ {A} ^ {*} \colon t ^ {\prime} \cdot \text { enter }. f \text { pre } t \Rightarrow \\ \exists t ^ {\prime \prime} \in \text { Act } _ {A} ^ {*} \colon t ^ {\prime} \cdot \text { enter }. f \cdot t ^ {\prime \prime} \cdot \text { ack }. f \text { pre } t \wedge \\ \# (\quad Ⓞ t ^ {\prime \prime}) \quad N. \end{array}
$$

The predicate specifying the new behavior is given through: $A ( t ) \equiv A ( t ) \land T _ { 1 } ( t ) \land T _ { 2 } ( t )$ and the new specification is $M _ { A } = ( \operatorname { \bf A c t } _ { A } , A )$ where ${ \mathrm { A c t } } _ { \mathit { A } } = { \mathrm { A c t } } { \mathit { A } } \cup \{ { A , \mathrm { a c k . } } { b , \mathrm { a c k . } } { f } \}$

## Market Structure Taxonomies

THIS SECTION INTRODUCES THE CONCEPT OF SYSTEM TAXONOMIES, which are built of trace specifications (for further approaches for establishing systematics of processes, see [7, 12]. Domowitz [4] presents a nonformal taxonomy of trading systems).

We show the application of a stepwise construction of market structures and illustrate its use by giving an example of a market that facilitates continuous trading. Formally, a system taxonomy, is a triple (S, Res, Ext) where S is a finite set of trace specifications. ${ \mathsf { R e s } } \subseteq S \times S ,$ is the restriction relation, which for specifications $( A _ { i } { \mathcal { P } } _ { i } )$ $\in S$ and $( A _ { j } , P _ { j } ) \in S$ is defined as:

$$
\begin{array}{l} (A _ {i}, P _ {i}) \operatorname{Res} (A _ {j}, P _ {j}) \Leftrightarrow \mathrm{U} \\ (A \mathrm{i} = A \mathrm{j} \wedge \forall t \in A _ {j} \omega : P _ {j} (t) \Rightarrow P _ {i} (t)), \text { we   say: } \end{array}
$$

$( A _ { j } , P _ { j } )$ restricts $( A _ { i } , P _ { i } )$ Ext $\notin S \times S ,$ is the extension relation, which for $( A _ { i } , P _ { i } ) \in S$ and $( { \dot { A } } _ { j } , { P } _ { j } ) \in { \cal S }$ is defined through:

$$
\begin{array}{l} (A _ {i}, P _ {i}) \operatorname{Ext} (A _ {j}, P _ {j}) \Leftrightarrow \\ (A _ {i} \in A _ {j} \land \forall t \in A _ {j} \omega : P _ {j} (t) \land P _ {i} (A _ {i} ⓒ t)), \text { we   say } \\ (A _ {j}, P _ {j}) \text { extends } (A _ {i}, P _ {i}). \end{array}
$$

For illustration of both concepts, we extend the market structure specification introduced earlier. We start with a new predicate $A \equiv S _ { 1 } ( t ) \land S _ { 2 } ( t ) \land S _ { 3 } ( t )$ and extend $\mathsf { A c t } _ { A }$ by the action publish. $. b ,$ which refers to the publication of bid b. Action publishf denotes the publication of an offer $f .$ Publication makes bids and offers submitted known to the rest of the market. The action set we gain has the form $\mathsf { A c t } _ { B } = \mathsf { A c t } _ { A } \cup$ {publish.b, publishjf $b \in \mathrm { B i d } , f \in \mathrm { O f f e r } \}$

So far, market behavior with the newly introduced publishing operations is not restricted. Let us impose a restriction on the publication of bids and offers demanding that no bid is published <sub>unlc\~ss</sub> all bids submitted earlier were published before; the same should hold for offers. The formalization of that requirement is given through safety predicate,

$$
S _ {4} \equiv \forall t ^ {\prime} \in \operatorname{Act} _ {B} ^ {*}, b \in \operatorname{Bid} b, f \in \text { Offer }: t ^ {\prime} \text { pre } t \Rightarrow
$$

(Bids © Publish © t) pre (Bids © Enter © t) A

(Offers © Publish © I') pre (Offers © Enter © t').

Note: Publish = {publish.b,publis $f | b \in \mathrm { B i d } , f \in \mathrm { O f f e r } \}$ . Function bids applied to a trace of publish operations deliver the finite sequence of arguments $b ^ { * } \in \mathbb { B i d } ^ { * }$ . Offers deliver the same for offers as arguments in a trace of publish operations. In addition, we require that before a bid and offer appear as constituent parts of a trade, both must have been published before. Safety predicate $S _ { 5 }$ expresses that property:

$$
S _ {5} (t) \equiv \forall b \in \text { Bid }, f \in \text { Offer }, t ^ {\prime} \in \operatorname{Act} _ {B} ^ {*}:
$$

t' . trade (bj) pre t \~ publish.b in $t ^ { \prime } \wedge$ publishfin $t ^ { \prime }$

The restricted market behavior can now be defined by

$$
B (t) \equiv A (t) \wedge S _ {4} (t) \wedge S _ {5} (t) \text {   for   all   } t \in \operatorname{Act} _ {B} \omega .
$$

Predicates $S _ { 4 } ( t ) \land S _ { 5 } ( t )$ do not violate any other predicate in $\mathbf { } A ( t )$ . Being consistent with

A(/), predicate $S _ { 4 } ( t ) \wedge S _ { 5 } ( t )$ imposes additional restriction on the market's behavior concerning the publishing of bids and offers submitted to the market.

We get a new market structure specification by $M _ { B } = ( \mathsf { A c t } _ { B } , B )$ with $B ( t ) \Rightarrow A \left( \mathbf { A c t } _ { A } \odot t \right)$ We further restrict the behavior $M _ { B }$ and demand that bids and offers that constitute a trade should match. Safety predicate $S _ { 6 }$ expresses that requirement:

$$
S _ {6} (t) \equiv \forall b \in \text { Bid }, f \in \text { Offer }, t ^ {\prime} \in \operatorname{Act} _ {B} ^ {*}:
$$

$$
t ^ {\prime} \cdot \operatorname{trade} (b, f) \text {   pre   } t \Rightarrow \operatorname{matching} (b, f).
$$

Matching of a bid and an offer is defined by matching(bJ), as previously given. But matching only requires that the price of a bid is higher than that of an offer.

The predicate following imposes a requirement on the sequence in which bids and offers should be executed. We demand that price priority holds for the execution of bids and offers. Safety predicate $s _ { \tau }$ expresses that property of the market by:

$$
\begin{array}{l} S _ {7} (t) \equiv \forall b, b ^ {\prime} \in \text { Bid }, f, f ^ {\prime} \in \text { Offer }, t ^ {\prime}, t ^ {\prime \prime} \in \text { Act } _ {B} ^ {*} \colon \\ t ^ {\prime} \cdot \text { trade } (b, f) \cdot t ^ {\prime \prime} \cdot \text { trade } (b ^ {\prime}, f ^ {\prime}) \text { pre } t \Rightarrow \\ (b ^ {\prime} \text { in } t ^ {\prime} \Rightarrow \text { price }. b \quad \text { price }. b ^ {\prime}) \wedge \\ (f ^ {\prime} \text { in } t ^ {\prime} \Rightarrow \text { price }. f \quad \text { price }. f ^ {\prime}) \end{array}
$$

${ \cal { S } } _ { 7 } ( t )$ gives priority to bids with higher prices and to offers with lower prices, accordingly. Bids and offers at the same price are matched according to the sequence of their placement [5, II]. Orders submitted first receive precedence. The formalization of that property provides predicate $S _ { 8 }$

$$
S _ {8} (t) \equiv \forall d \in \text { Trade }, p \in \text { Price }, s \in \text { Act } ^ {*}: s \Rightarrow t \Rightarrow
$$

$$
(\text { bids.Trades. } p \circledast S) \text { pre } (\text { Bids. } p \circledast s) \wedge
$$

$$
(\text { offers.Trades. } p \circledast s) \text { pre } (\text { Offers. } p \circledast s).
$$

We use a couple of auxiliary functions and sets for expressing $S _ { 8 } .$ Set Trades $p =$ {trade.d IdE Trade, price.bid. $\scriptstyle d = p \}$ includes trades that have price p as the matching price and for which p is equal to the price of the bid that constitutes one part of the trade. Auxiliary set Bids $p = \{ { \tt b i d } . b \mid b \in { \tt B i d }$ , price $\boldsymbol { \mathbf { \mathit { b } } } = \boldsymbol { \mathbf { \mathit { p } } } \boldsymbol  \}$ contains all bids having price $p , \mathsf { O f f e r s . } p = \{ \mathsf { o f f e r . } f | f \in \mathsf { O f f e r . }$ pric $\scriptstyle f = p \}$ includes all offers at price $p .$ Auxiliary operation bids delivers a trace of bids, all those bids that occur as constituent components in a trace of trades. Operation offers returns all offers in those trades.

Finally, we impose a restriction on the market behavior concerning the production of trades when orders match. It is demanded that the market eventually produce at least one trade when a bid and an offer match. Liveness predicate $L _ { 1 }$ formalizes that requirement:

$$
L _ {1} (t) \equiv \forall t ^ {\prime} \in \operatorname{Act} _ {B} ^ {*}, b \in \operatorname{Bid}, f \in \text { Offer: }
$$

$$
t ^ {\prime} \text {   pre   } t \wedge \text {   enter.   } b \text {   in   } t ^ {\prime} \wedge \text {   enter.   } f \text {   in   } t ^ {\prime} \wedge \text {   matching   } (b, f) \Rightarrow
$$

$$
\exists t ^ {\prime \prime} \in \operatorname{Act} _ {B} ^ {*}: t ^ {\prime} \cdot t ^ {\prime \prime} \text {   pre   } t \wedge \# (\text { Trades   } \mathbb {C} t ^ {\prime \prime}) \quad 1.
$$

We get the new market structure specification, where $M _ { C } = ( \mathbf { A c t } _ { C } , C ) , \mathbf { A c t } _ { C } = \mathbf { A c t } _ { B } .$

![](/api/attachments/AZ9QV9G9/fulltext/images/565d7a1e2b59e6e779d7398cb16fa9cac5e13a69c2be80a69f2a1589c9457341.jpg)

Figure 2. Taxonomy

and $C ( t ) \equiv B ( t ) \land S _ { 6 } ( t ) \land S _ { 7 } ( t ) \land S _ { 8 } ( t ) \land L _ { 1 } ( t )$ for all $T \in \mathsf { A c t } _ { C } \mathsf { \omega } _ { C }$

The examples illustrate the stepwise development of new market forms. We extended a version of the specification $M _ { A } = ( \operatorname { \mathbf { A c t } } _ { A } ^ { \phantom { A } \mathbf { A } } )$ (we took the liveness predicates out) by publishing operations and restricted the behavior connected to these operations. The new market form $M _ { B } = ( \operatorname { \mathrm { \bf A c t } } _ { B } , B )$ was then transformed to $M _ { C } = ( \mathbf { A c t } _ { C } , C )$ which further restricted the matching behavior of $M _ { B }$ and models continuous trading with price-time priority. Market $M _ { A A } = ( \operatorname { \bf A c t } _ { A A } , A )$ also extended $M _ { A }$ by "ticks" and an accept operation. Again, for both actions the behavior was restricted, and $M _ { A } , M _ { B } , M _ { C } ,$ and $M _ { A A }$ form a taxonomy of market structures (figure 2).

## Conclusion

THIS PAPER PRESENTED AN APPROACH THAT AIMS AT THE SUPPORT of trading system construction in its early phase. It suggests separating market structure definition and trading service specification as the two first steps and shows how to apply trace specifications as a formal description technique on both levels. Carrying out both steps formally allows descriptions to be related to one another, supports the systematic exploration of market structures and trading service alternatives, and enables more rigorous treatment of market system development, leading to more efficient financial exchanges.

## REFERENCES

1. Brauer, W. The new paradigm of informatics, In H. Maurer (ed.), New Results and New Trends in Computer Science. Lecture Notes in Computer Science 555. Berlin: Springer, 1991.

2. Broy, M. Mathematical system models as a basis for software development. In 1. v. Leeuwen, Computer Science Today: Recent Trends and Developments. Lecture Notes in Computer Science 1000. Berlin: Springer, 1995.

3. Broy, M.; Dederichs, F.; Dendorfer, C.; Fuchs, M.; Gritzner, T.; and Weber, R. The design of distributed systems. Department for Informatics, Technical University Munich, 1993.

4. Domowitz, I. A taxonomy of trade execution systems. Department of Economics, Northwestern University, 1992.

5. Harris, L.E. Liquidity trading rules, and electronic trading systems. Monograph Series in Finance and Economics. New York: New York University, 1990.

6. Hoare, C.A.R. Communicating Sequential Processes. Englewood Cliffs, NJ: Prentice-Hall, 1985.

7. Malone, T.; Crowston, K.; Lee, J.; Pentland, B.; Dellarocas, c.; Wyner, G.; Quimby, J.; Osborne, C.; and Bernstein, A. Tools for inventing organizations: towards a handbook of organizational processes. MIT-CCS, Report 198, 1997.

8. Pentland, B. Grammatical models of organizational processes. Organization Science, 6, 5 (1995), 541-556.

9. Reck, M. Formally specifying an automated trade execution system. Journal of Systems and Software, 21 (1993), 245-252.

10. Smith, V.L. Microeconomic systems as experimental science. American Economics Review, 72 (1982), 923-955.

II. Schwartz, R.A. Reshaping the Equity Markets-A Guide for the 1990s. New York: Harper Business, 1991.

12. Wyner, G., and Lee, J. Applying specialization to process models. Proceedings of the Conference on Organizational Computing Systems, Milpitas, California, 1995.
