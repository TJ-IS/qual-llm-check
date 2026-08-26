---
otero_id: 10014
otero_key: "SUPF2JJ3"
title: "A probabilistic model of integration"
authors: "Stephan Olariu; Jeffrey V. Nickerson"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.12.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# A probabilistic model of integration

Stephan Olariu <sup>a,⁎</sup>, Jeffrey V. Nickerson

Old Dominion University, Norfolk, VA 23529-0162, United States b Stevens Institute of Technology, Hoboken, NJ 07030, United States

Available online 23 December 2007

## Abstract

We propose a probabilistic model of integration where decisions about integration are made based on the perceived ensuing benefit. Integration proceeds in a pairwise manner. This model provides a way to think formally about the integration processes in networks. The model considers information decay over time, and relates decisions to integrate to the value of the information the nodes possess. A sensor network designed to detect intruders is used as an illustrative example. Other applications of the model are suggested: information systems integration, as well as the merger of corporations. © 2008 Published by Elsevier B.V.

Keywords: Integration; Preferential attachment; Information economics; Network design; Sensor networks; Social network

## 1. Introduction

Information is a good that can be traded, or exchanged, and hence has value. There are many aspects of information that may increase or decrease its value: timeliness is an important one; accuracy is another. Assessing the value of information and understanding the dynamics of its change over time has been a topic of research in economics [5,11,25,26], information systems [1,38], psychology [3,4], and political science [10,21,37], among many others.

Arrow [5] attempted to bridge the gap between information theory and information value. In a review assessing different approaches to valuing information, Ahituv [1] criticized past economic work in information systems as fruitless. He observed that information value is linked to the value of the surrounding information system: this latter value has been studied empirically, and appears difficult to assess, as the opinions of stakeholders differ according to circumstance. More recent work of Raban and Rafaeli [38] on valuation has agreed, claiming that corporate stakeholder valuation is subjective and not fully rational.

But in some domains, the value of information may be clearer. We consider in this paper one such domain, that of sensor networks. We use as a working scenario the following example: a set of sensors, which can communicate with other sensors in their neighborhood, are monitoring an area for intruders. Experience shows that there exists a strong spatial correlation of sensor data — indeed, the sensors in the vicinity of the intruder are likely to detect its presence, others do not. In our working scenario, it is imperative for the sensors to integrate information in order to corroborate the intrusion event and to aggregate information in order to pinpoint the type of intrusion. If the sensors do not integrate information, the sensor field will not be able to easily determine an intruder's presence, direction, and velocity. However, if the sensors over-communicate with each other, they run the risk of depleting their batteries. Thus, the sensors need to make individual decisions about integration with their fellow sensors.

We build a model based on the following assumptions:

• Information value decreases over time and, consequently, the sensors need to take into account decaying value when deciding whether or not to integrate;

• The decay function of information is universal within the network and occurs at the same rate;

• Global integration is the result of a cascading set of pairwise integrations between neighboring sensors.

Thus, in our model, one entity makes a decision about whether or not to integrate with another entity. There is a benefit to integration: both entities gain the value of the other.

Our assumptions, stated above, allow us to build a probabilistic model of integration. Deductively, we look at what derives from our initial assumptions. Later in the paper, we discuss the limits of our model, and how different assumptions may change our conclusions. We also discuss the implications of the model for the examination of social and information systems networks: such networks often involve decision makers who also make tradeoffs between integrating and not integrating in the face of resource constraints.

The remainder of this article is organized as follows: in Section 2 we review related work. Section 3 is of an introductory nature since it discusses the assumed dynamics of the type of integration investigated in the paper. Section 4 investigates analytical properties of two related information decay functions. Section 5 proves time-independence results that hold in our model of integration. A closer look at various scenarios of integration is taken in Section 6. Section 7 puts our work in perspective: in Subsection 7.1 we discuss the limitations of the model; Subsections 7.2 and 7.3 discuss the implication of our results and avenues for future research. Finally, Section 8 offers concluding remarks.

## 2. Related work

Information is more valuable new than old. For example, real time stock quotes are more valuable than quotes which are delayed 20 min. We see evidence of this in the tiered pricing offered by exchanges for pricing information based on the delay: the less delay, the more expensive the service. In everyday situations, we recognize that today's newspaper is more important than yesterday's. This deterioration of information value is discussed in a general way in the literature of the economics of information [5,25,26]. We discount past information in favor of present information. Discount functions have also been discussed in relationship to the psychology of individual decision making [11].

In psychology, information integration [3,4] studies how humans handle data. New information flows into a human mind and is merged into already processed information. Our ability to perceptually integrate information is an indicator of our overall thinking abilities [20]. Research shows that some forms of human memory decay exponentially [22].

At the social level, economists discuss the half-life of an academic field or even of a scientific paper. Recently, the Web has provided us empirical evidence for information decay in academia. Researchers in physics post their articles online in standard venues: the citation rates decay exponentially starting from the time of posting [8].

Deutsch [10] has modeled integration in the context of politics, investigating the way coalitions form and dissolve. This kind of merger – when states form coalitions – is analogous, at a higher scale, to the integration we describe between nodes in a sensor network. Work on preferential attachment [6] has suggested that a tendency to attach to the node in a network that already has more connections will create realistic networks. Work in this area has focused on the purely formal properties of the network: once a vertex has many edges, more vertices will attach to it. In our model, once a vertex has established value, many other vertices will attempt to attach in order to share the value. But our most soughtafter nodes will sometimes refuse these connections.

Lawrence and Lorsch [21], proposed a model of integration in which individuals – ambassadors – carry information back and forth between culturally distinct parts of the corporation. Porter's [37] ideas on how organizational units specialize and, as a result, create boundaries underlying the justifications offered for most integration technologies [40].

In work on coordination science [9,23,24], patterns of behaviors are classified with respect to producers and consumers of resources. Integration, then, can be seen as a linking between places. We will use these integration ideas — that integration happens in shared places and that it is facilitated by ambassadors.

In a series of papers, Jones et al. [12–18] have investigated a particular instance of information integration in sensor networks, namely that of reaching a consensus. While their model of a sensor network is similar to ours, their approach is not explicitly probabilistic.

In our previous work we have focused on latency as a key aspect of modern communication networks [29], and have investigated its implications in the context of sensor networks [34,32,34]. In [31,30] we have proposed metrics for measuring integration. Recently, we introduced the idea of couriers — moving entities which visit sensors and integrate the information between sensors or sensor clusters [28].

In [31] we proposed a model of integration and introduced a discount function (e.g. [11]) effectively reducing the value of a network when latency delays communication.

Our measure did not address how integration is likely to be built over time. In other words, we assume that, if there is a path in the graph, then the path will be used and integration will occur as quickly as possible. In real situations, this is often not the case: the resources to integrate are limited, and thus integration takes place more slowly, as a set of cascading smaller integrations, first between neighbors, and then recursively, between clusters of already integrated nodes. We now turn to analyzing the dynamics of such integration.

## 3. Assumptions about integration dynamics

We assume a set of actors associated with particular pieces of information. We will consider the sensors to be our major actors — later, we will discuss generalization to other types of networks. Situations with actors communicating in parallel are complex, with new and emerging external inputs, and feedback loops.

Here, we simplify by considering a situation in which nodes have values, which are deteriorating, and must decide to integrate or not with others. In accord with other researchers [2], we envision a collection of sensors deployed in large numbers over an area of interest. In our working scenario, the sensors are dropped uniformly at random from an aircraft to detect intruders in a large territory. In addition to the sensors, a set of couriers are also deployed — these are robots, one assigned to each sensor (see [28,33,43] for more on the concept of couriers). The sensors in our model can transmit very far, but only a little information, sufficient to announce the value of the information they possess and their location. Thus, the sensors possess vectors of information:

public data value :8; location 10:00; 20:00; 3:00 ;

sensed data timestamp 07:34:00; signal energy 34:00 ;

timestamp 07:34:10; signal energy 37:00 ; N :

The quantity of public data is small, and the quantity of sensed data is large, as such data may include time series information on signals. For example, a sensor may record video. Consequently, we envision the sensors sending and receiving public data from their neighbors, and then making the decision to send a courier to meet with them and exchange the sensed data.

How can sensors determine the value of the information they have? Such a value is in relation to the objective of the sensor field, which will be determined before deployment. For example, sensors that have detected a high signal strength target will advertise higher value than a sensor that has seen no intruder. This valuation process may be as simple as looking up a statistic in a pre-defined table.

Once an agreement to integrate is reached, the sensors will send their couriers to meet each other and exchange detailed information. This information may include information on all potential targets seen, including location and trajectory information, as well as other sensory information — for example, photographs, seismographs, etc. In our model, the couriers each proceed from their corresponding node and meet half-way. There are other possible schemes: one courier can handle communication between two nodes [30] or one courier can traverse a path over several nodes [43]. But for the purposes of integrating quickly, meeting half-way ensures that within the time it takes to reach the half-way point and return, both nodes will know each other's information.

The overall state of such a network is polled by yet another sensor. In realistic environments, this is something that flies over the sensor field. These are called flying sinks, and are discussed in more detail in [30]. Consistent with our scheme, such a flying sink would fly over the field, listen for nodes with high information value, and receive their data. Thus, the process of integration is one in which information aggregates to the point where a small sampling of the field will reveal the state of world as understood by the network.

This model is general enough to represent networks which contain both electronic and transportation components. Such hybrid networks have received increasing attention of late–recent studies have looked at this conjunction of robotics and sensor networks [39,30,43]. This model also can be used to model social networks such as diplomacy, in which electronic communication is used to set up face-to-face meetings, at which time integration takes place.

A courier model can also be used in fully electronic networks. In such cases, the couriers should be thought of as virtual, a conceptualization of a channel. If communication is streamlined in an electronic network, communication is at the speed of light and therefore we can consider the distance to be 0. But in electronic networks, there are often multiple hops, and queue delays associated with the transmission and parsing of data. In such cases distance can be considered topological, derived from the routing structure of the network, or it can be inferred as a correlate of network latency.

With that as the backdrop, we proceed with the formal analysis.

In what follows, $\mathbf { R } ^ { + }$ denotes the set of positive reals. The graphs used are all undirected with no self-loops or multiple edges. An edge e of endpoints x and y will be denoted by $e = \{ x , y \}$ . For a vertex x of a graph $G = ( V ,$ $E ) _ { : }$ , we let $N _ { G } ( x )$ denote the set $\{ y \in V \ \{ x , y \} \in E \}$ . In words, $N _ { G }$ (x) is the set of neighbors of x in $G ,$ namely the set of all the vertices in V that are adjacent to x. To simplify the notation, whenever the graph $G$ is understood, we shall write $N ( x )$ instead of $N _ { G } ( x )$

Consider an arbitrary graph $G { = } ( V , E )$ along with

• a map v: $V \to \mathbf { R } ^ { + }$ that associates with every vertex x of the graph G its “value” v(x). It is useful to think of the value of a vertex as a quantification of some useful attribute it possesses. Often, we think of the value as representing an encoded form of the information stored by the vertex;

• a map d: $E \to \mathbf { R } ^ { + }$ that associates with each edge e of the graph G its “length”, d(e).

The phenomena we address occur in time. We assume that the time axis starts at 0 and is partitioned into unit intervals referred to as slots as illustrated in Fig. 1. For the analysis that follows, the exact size of a time slot is immaterial; naturally, in the real world, the size of time slots is application-dependent. All transactions discussed in this paper occur at slot boundaries. The values associated with vertices are assumed to be constant during a given time slot. These values change (often abruptly) as we transit from the current time slot to the next one. As time slots become smaller and smaller, in the limit, we find our familiar continuous world.

For an arbitrary vertex x of G, we let $\nu _ { 0 } ( x )$ , stand for its initial value v(x). As we noted above, the value of x remains constant during a given time slot. Referring again to Fig. 1, the initial value $\nu _ { 0 } ( x )$ of vertex x remains constant during time slot 0. Similarly, the discounted value $\nu _ { 1 } ( x )$ of x stays the same through time slot 1, and so on.

Vertices use their values to make decisions: the larger the value, the better (i.e. more informed) the decision. In every time slot, vertices have the choice of making a decision or else to defer decision to a later time. However, values decay with time. To give mathematical expression to this idea, we define a decay function

$$
\rho : \mathbf {R} ^ {+} \times \mathbf {N} \rightarrow \mathbf {R} ^ {+}
$$

![](/api/attachments/SUPF2JJ3/fulltext/images/cba20c12f5121849e20bcc94edc8470c3a77248b049e81b80fb8724787376c64.jpg)  
Fig. 1. Illustrating time slots and the corresponding discounted values.

and define the discounted value $\nu _ { t } ( x )$ of vertex x during the t-th time slot to be

$$
v _ {t} (x) = \rho (v _ {0} (x), t)\tag{1}
$$

where, by convention,

$\nu ( x ) { = } \nu _ { 0 } ( x ) { = } \rho ~ ( \nu _ { 0 } ( x ) , 0 ) ,$ , and

• for all $t \geq 1 , \nu _ { t } ( x ) < \nu _ { 0 } ( x )$

Eq. (1) shows that the penalty of waiting for t time slots is that the value of the vertex decreases. To counterbalance time decay, we define an algebraic graph operation that we call vertex integration or, simply, integration. Formally, given a graph $G { = } ( V , E )$ along with the maps v and $d ,$ the integration of adjacent vertices x and y results in a new graph $G ^ { \prime } { = } ( V ^ { \prime } { , } E ^ { \prime } )$ , where $V ^ { \prime }$ and $E ^ { \prime }$ are defined as follows:

$V ^ { \prime } { = } ( V \backslash \{ x , y \} ) \cup$ {z}. In words, $V ^ { \prime }$ is obtained from V by first removing vertices x and y and then by adding a new vertex labeled $z ^ { 1 }$ ;

$E ^ { \prime } { = } ( E \backslash E _ { 1 } ) \cup E _ { 2 }$ where

$\begin{array} { r } { -   E _ { 1 } = ( \bigcup _ { u \in N ( x ) } x u ) \bigcup ( \bigcup _ { w \in N ( y ) } y w ) \bigcup \{ x ,  y \} } \end{array}$ , that is the set of edges of G adjacent to one of the vertices x or y, and

$E _ { 2 } { = } \bigcup _ { u \in N ( x ) \cup N ( y ) , \ u \neq x , \ u \neq y } \ z u ,$ , that is, the set of edges joining the new vertex z to the neighbors of x and y in the original graph, x and y excluded.

In words, $E ^ { \prime }$ is obtained from E by first removing all the edges belonging to $E _ { 1 }$ and then by adding the edges in $E _ { 2 } ;$

$\nu ( z ) { = } \nu ( x ) \circ ( y )$ , where ◦ is an application-dependent binary operation. Natural instances of ◦ include +, max, min, XOR (the exclusive of v(x) and v(y)), OR (the logical or of v(x) and v(y)), among many others [2,35,36,33]. In this paper, we take v(z) to be $\nu ( x ) +$ v(y);

• for all vertices u in $N ( x ) \cup N ( y ) \backslash \{ x , y \}$ , set $d ( z u ) =$ min $\{ d ( x u ) , d ( y u ) \}$

We refer the reader to Fig. 2 for an illustration. In Fig. 2(a) vertices A and F are integrated and, after integration, are replaced in the new graph in Fig. 2(b) by a vertex labeled AF. Notice that the old edge between vertices A and $F$ is removed; the new vertex $A F$ is adjacent to all the vertices that were adjacent, in the original graph, to either A or F or both. The value of the new vertex $A F$ is the sum of the values of A and F. Also, it is worthwhile to note that since both A and F were adjacent to B, after integration the vertex AF is connected to B by an edge of weight 1, the minimum of 1 and 4.

The above formalism is useful to define, in abstract terms, the concept of integration. However, instead of thinking of z as a new vertex, it is often useful to view z as a composite vertex consisting of vertices x and $y ,$ combined.<sup>2</sup>

Vertices that are not composite are said to be simple. In particular, all the vertices of the original graph G are simple.

In our model, integration is the only way in which the value of a vertex can increase over time. Our main interest lies in investigating conditions under which it is mutually beneficial for integration to occur.

## 4. Properties of the decay function

The main goal of this subsection is to further investigate properties of the generic decay function defined in (1), which will be instantiated in several ways in the subsections of this section. Our motivation is to discuss, in some detail, several natural ways in which one can think, and reason, about a decay function.

However, before we instantiate the decay function, and in order make the decay conform to our intuition, we insist on the following generic properties that any decay function should satisfy:

Commutativity: For arbitrary natural numbers k, m,

$$
v _ {m} (v _ {k} (x)) = v _ {k} (v _ {m} (x)).\tag{2}
$$

To simplify the notation, we write

$$
v _ {m + k} (x) = v _ {m} (v _ {k} (x))
$$

and, similarly,

$$
v _ {k + m} (x) = v _ {k} \left(v _ {m} (x)\right).
$$

In this new notation, (2) becomes

$$
v _ {m + k} (x) = v _ {k + m} (x).\tag{3}
$$

Eqs. (2) and (3) capture our intuitive idea that the final value at the end of two discount periods should not depend on the order in which the discounts are applied.

Consistency: For arbitrary natural numbers k, m, n such that $n { = } k { + } m$ 3

$$
v _ {n} (v _ {0} (x)) = v _ {m} (v _ {k} (v _ {0} (x))) = v _ {k} (v _ {m} (v _ {0} (x)))\tag{4}
$$

which can also be expressed in the equivalent form

$$
v _ {n} (x) = v _ {m + k} (x) = v _ {k + m} (x)\tag{5}
$$

Eq. (5) expresses our intuitive idea that the discounted value $\nu _ { n } ( x )$ of x at the end of n time slots should equal the discounted value $\nu _ { k } ( x )$ at the end of k time slots, further discounted by the effect of waiting an additional m time slots, to a value of $\nu _ { m } ( \nu _ { k } ( x ) )$ which we write as $\nu _ { m + k } ( x )$ . Incidentally, the order in which the discounts are applied is irrelevant, and so $\nu _ { n } ( x )$ also matches $\nu _ { k } ( \nu _ { m } ( x ) )$ , that is $\nu _ { k + m } ( x )$

Associativity: For arbitrary natural numbers k, l, m,

$$
v _ {k} [ v _ {l} (v _ {m} (v _ {0} (x))) ] = v _ {m} [ (v _ {l} (v _ {k} (v _ {0} (x))) ],\tag{6}
$$

which can also be expressed in the equivalent form

$$
v _ {k + (l + m)} (x) = v _ {(k + l) + m} (x).\tag{7}
$$

In other words, Eqs. (6) and (7) give mathematical expression to the idea that the discounted value at the end of three discount periods does not depend in the order in which the discounts are applied.

Idempotence: For all natural numbers $k ,$

$$
v _ {k + 0} (x) = v _ {k} (x).\tag{8}
$$

Eq. (8) captures the idea that discounts only apply at time-slot boundaries. In other words, as already mentioned, values are constant within a time slot.

Note: The observant reader must have noticed that the properties of the decay function stated above are reminiscent of the axioms of an Abelian semigroup in abstract algebra. Indeed, it is very easy to verify that the decay function induces a semigroup on the set of positive real values with respect to the operation of composition of discounts (or decays). This is a promising topic for future research.

![](/api/attachments/SUPF2JJ3/fulltext/images/0c1ed71f24e6a0769ea392c25db1f3e0e9e96e010651e402222b03b28c109f61.jpg)  
(a)

![](/api/attachments/SUPF2JJ3/fulltext/images/eb87fa46510df78f22ff382725c6cf8f738896e5047b1b3461e1d968335d9e57.jpg)  
(b)  
Fig. 2. Illustrating the integration of two vertices.

To set the stage for the next subsections, we define a decay function δ as

$$
\delta : \mathbf {N} \rightarrow (0, 1 ].
$$

In Subsection 4.1 we concern ourselves with decay functions of the “multiplicative” type. Later, in Subsection 4.2 we look at “additive” decay functions. As it turns out, although the defining properties of these decay functions are quite different, they share numerous important properties.

## 4.1. Multiplicative decay

There are applications, especially in data aggregation in sensor networks, where the discounted value $\nu _ { n } ( x )$ of a vertex at the end of n time slots is expressed as

$$
v _ {n} (x) = v _ {0} (x) \cdot \delta (n).\tag{9}
$$

Now, the consistency property of the decay function implies that, under these conditions,

$$
\delta (n) = \delta (k) \cdot \delta (m),\tag{10}
$$

where $n { = } k { + } m$

Second, by virtue of (4), we can first evaluate the discounted value $\nu _ { k } ( x )$ at the end of k time slots and then discount this value further at the end of m subsequent time slots. Consequently, we must have

$$
\begin{array}{c} v _ {n} (x) = (v _ {0} (x) \cdot \delta (k)) \cdot \delta (m) \\ = v _ {0} (x) \cdot (\delta (k) \cdot \delta (m)). \end{array}\tag{11}
$$

Now, (9) and (11), combined, show that (10) must hold, as desired.Also, note that (8) translates into

$$
\delta (0) = 1.\tag{12}
$$

Intuition tells us that the solution of the functional Eq. (10) must be an exponential. The following result confirms our intuition.

Theorem 4.1. Let $a = \delta ~ ( l )$ . Then, for an arbitrary natural number n,

$$
\delta (n) = a ^ {n}.\tag{13}
$$

Proof. We proceed by induction. By (12), the conclusion is immediate for $n { = } 0$ . We shall, therefore, assume that $n \geq 1$ . The consistency property of the decay function allows us to write

$$
\begin{array}{l} \delta (n) = \delta (n - 1) \cdot \delta (1) \\ \qquad = \delta (n - 2) \cdot (\delta (1)) ^ {2} \\ \qquad \dots \\ \qquad = \delta (n - i) \cdot (\delta (1)) ^ {i} \\ \qquad \dots \\ \qquad = \delta (0) \cdot (\delta (1)) ^ {n} \\ \qquad = \delta (1) ^ {n} [ \text { by   virtue   of   (12) } ] \\ \qquad = a ^ {n}, \end{array}
$$

Completing the proof of the theorem.

The case a = 1 corresponds, essentially, to the situation where there is no value decay, portrayed in Fig. 2. While interesting and worthwhile in its own right, we dismiss this case in the sequel of this work and focus on the more interesting case where

$$
0 <   a <   1.\tag{14}
$$

Although we were conditioned to think of exponential functions as growing or decreasing very fast, in practice this is not always the case. Indeed, for $a = { \frac { 9 9 } { 1 0 0 } }$ we have $a ^ { 1 0 } = 0 . 9 0 4 3 8 . . . , \ a ^ { 2 0 } = 0 . 8 1 7 9 0 . . .$ , and $a ^ { 1 0 0 } = 0 . 3 6 6 0 3$

This shows that at the end of 10 time slots a vertex of unit value has lost roughly 10% or its original value; at the end of 20 time slots, the same vertex has lost only about 18.3% of its value. Even after a long delay of 100 time slots the vertex still has about 36.6% of its initial value.

## 4.2. Additive decay

Occasionally, one is interested in defining the decay function differently. Specifically, for every integer $m ,$ we define the discounted value of x at the end of m time slots by writing

$$
v _ {m} (x) = v _ {0} (x) - v _ {0} (x) \cdot \delta (m).\tag{15}
$$

Observe that (15) can also be written as

$$
v _ {m} (x) = v _ {0} (x) \cdot [ 1 - \delta (m) ].\tag{16}
$$

By virtue of (16), and the consistency property (4) of the decay function we write

$$
\begin{array}{c} v _ {m + k} (x) = v _ {0} (x) \cdot [ 1 - \delta (m) ] - v _ {0} (x) \cdot [ 1 - \delta (m) ] \cdot \delta (k) \\ = v _ {0} (x) \cdot [ 1 - \delta (m) ] \cdot [ 1 - \delta (k) ] \end{array}\tag{17}
$$

Since the discounted value of x at the end of $m + k$ time slots is $\nu _ { 0 } ( x ) \cdot [ 1 - \delta ( m + k ) ]$ , (17) implies that

$$
v _ {0} (x) \cdot [ 1 - \delta (m + k) ] = v _ {0} (x) \cdot [ 1 - \delta (m) ] \cdot [ 1 - \delta (k) ].
$$

After a bit of algebra, we obtain the following interesting property of the additive decay function that justifies its name:

$$
\delta (m + k) = \delta (m) + \delta (k) - \delta (m) \cdot \delta (k)\tag{18}
$$

It is instructive to explore the expression of the associativity property in the context of the additive decay function. Indeed, it is quite easy to prove that for arbitrary natural numbers $k , l , m$ , the following equation is satisfied:

$$
\begin{array}{r l} \delta ((k + l) + m) & = \delta (k + (l + m)) \\ & = \delta (k) + \delta (l) + \delta (m) - \delta (k) \delta (l) \\ & \quad - \delta (k) \delta (m) - \delta (l) \delta (m) \\ & \quad + \delta (k) \delta (l) \delta (m). \end{array}\tag{19}
$$

Note: It is interesting to note the similarity between the expressions in (18) and (19) and the expression of the probability of the union of non-necessarily disjoint events.<sup>3</sup>

Now that we have a better understanding of the additive decay function, a natural thing to do is to obtain a closed form for δ (n) as a function of δ (1) (and not $\delta \left( 0 \right)$ which must be 0). It may come as a surprise that in this case, too, the expression is almost an exponential. The following theorem spells out the technical details.

Theorem 4.2. Write $a = \delta ~ ( l )$ . For an arbitrary natural number n,

$$
\delta (n) = 1 - (1 - a) ^ {n}.\tag{20}
$$

Proof. We proceed by induction on n. The result is certainly true for $n { = } 0$ , since in this case $\delta ( 0 ) =$ $1 - ( 1 - \stackrel { \cdot } { a } ) ^ { 0 } = 0 .$

Choose an arbitrary $n , ( n \geq 1 )$ , and assume that $\delta ( n ) =$ $1 - ( 1 - a ) ^ { n }$ holds for this particular value of n. With this assumption, we need to prove that $\delta ( n + 1 ) { = } 1 - ( 1 - a ) ^ { n + 1 }$

For this purpose, using (19), we write

$$
\begin{array}{l} \delta (n + 1) = \delta (1) + \delta (n) - \delta (1) \cdot \delta (n) \\ \quad = a + (1 - (1 - a) ^ {n}) \\ \quad \quad - a (1 - (1 - a) ^ {n}) [ \text { by   the   induction   hypothesis } ] \\ \quad = a + 1 - (1 - a) ^ {n} - a + a (1 - a) ^ {n} \\ \quad = 1 - (1 - a) ^ {n + 1}, \end{array}
$$

as desired.

Theorem 4.2 has a very interesting corollary that we state and prove next.

Corollary 4.3. For all natural numbers n, the discounted value $\nu _ { n } ( x )$ of vertex x at the end of n time slots is given by

$$
v _ {n} (x) = v _ {0} (x) \cdot (1 - a) ^ {n}.
$$

Proof. To see that the expression of $\nu _ { n }$ above is correct, write

$$
\begin{array}{l} v _ {n} (x) = v _ {0} (x) - v _ {0} (x) \cdot \delta (n) \\ \quad = v _ {0} \cdot (1 - \delta (n)) \\ \quad = v _ {0} \cdot (1 - 1 - (1 - a) ^ {n}) [ \text { by   Theorem   4.2 } ] \\ \quad = v _ {0} (x) \cdot (1 - a) ^ {n}, \\ \text { completing   the   proof. } \end{array}
$$

$$
\operatorname * {P r} [ A \cup B ] = \operatorname * {P r} [ A ] + \operatorname * {P r} [ B ] - \operatorname * {P r} [ A ] \operatorname * {P r} [ B ]
$$

and

$$
\begin{array}{c} \operatorname * {P r} [ A \cup B \cup C ] = \operatorname * {P r} [ A ] + \operatorname * {P r} [ B ] + \operatorname * {P r} [ C ] - \operatorname * {P r} [ A ] \operatorname * {P r} [ B ] - \operatorname * {P r} [ A ] \operatorname * {P r} [ C ] \\ - \operatorname * {P r} [ B ] \operatorname * {P r} [ C ] + \operatorname * {P r} [ A ] \operatorname * {P r} [ B ] \operatorname * {P r} [ C ]. \end{array}
$$

As Corollary 4.3 shows, even the additive decay function has, in the end, an exponential effect. Thus, there is no significant difference between the multiplicative and the additive decay function. With this observation in mind, in the remainder of this work, we adopt the multiplicative delay in all our derivations. Similar expressions can be obtained if the additive decay function is used instead of the multiplicative one.

There are still other functional combinations possible. For example, in some cases information has value up until a deadline, and then no value after the deadline, as illustrated in Fig. 3. As such functions have been explored in the scheduling literature [27], we will instead focus on situations in which decay is continuous.

## 5. Time-independence results

In sensor networks integration is a instance of information aggregation [35]. Indeed, in keeping with typical mission semantics, a sensor has the choice to report the sensed value it stores or to wait some more in the hope that, by integrating with a neighboring sensor, it can report a better value.<sup>4</sup> To give the presentation a more general favor, in the remainder of this section we shall talk about vertices and not sensors and of decision making and not of reporting.

Since the value of the information stored by a vertex decays over time, delaying decision making only makes sense if the expected value after integration exceeds the current one. Otherwise it is better to make a decision right away, since the quality of this decision will not improve after integration.<sup>5</sup>

Integration takes time and, in sensor networks, energy as well. To model the cost of integration, we imagine that each vertex has a courier which may be dispatched to a neighboring vertex with an integration offer.<sup>6</sup> We assume that all couriers move at unit speed: thus, traversing the edge $e = \{ x , ~ y \}$ connecting vertices x and y requires $d ( x , \ y )$ time slots.<sup>7</sup>

![](/api/attachments/SUPF2JJ3/fulltext/images/e0cc66f1ca658b90694579ae7046cdee0c28fa90eb8adb616a3c7ba91f011416.jpg)  
Fig. 3. Illustrating discounted values with deadline.

From an optimization standpoint, the individual node only wants to expend its energy on transactions which will result in an increase in utility. Intuition tells us that, in most cases, vertices storing a higher value are reluctant to integrate with vertices storing less valuable information. In the limit, of course, a vertex will never integrate with a vertex that contains no information. On the other hand, vertices containing less valuable information are eager to integrate with vertices of higher value. Merging with a highervalue node – a node with valuable and recent information, and/or a node that has already integrated with many other nodes – will be desirable, but lower value nodes may sap power for little benefit.<sup>8</sup>

Consider an arbitrary time slot, t, and two vertices x and y with values v (x) and v (y), respectively and refer to Fig. 4. In time slot t vertex x makes an integration offer to vertex y with probability

$$
p _ {t} (x, y) = \frac {v _ {t} (y)}{v _ {t} (x) + v _ {t} (y)}.\tag{21}
$$

![](/api/attachments/SUPF2JJ3/fulltext/images/4dbcffea3fa10df9caba4a66bcd860dd8d64f26203ad28e01c599e2879de606c.jpg)  
Fig. 4. Illustrating asymmetric integration probabilities.

We warn the reader that since the time quantas are discrete, an integration offer (if any) made in time slot t will go out to the corresponding party at the edge between time slots t and t + 1.

Similarly, in the same time slot, vertex y makes an integration offer to x with probability

$$
p _ {t} (y, x) = \frac {v _ {t} (x)}{v _ {t} (x) + v _ {t} (y)}.\tag{22}
$$

A bit of explanation is in order at this time. Eq. (21) is intended to capture the idea that the probability of integrating with a vertex of zero value should be zero and, likewise, the probability of integrating with an omniscient vertex, i.e., one of infinite value, should be one. In fact, (21) is an attempt to interpolate between these two extremes. Similarly for (22).

We now state and prove a simple but, at first blush, somewhat counter-intuitive result that indicates that the probability of integration of two simple vertices is timeinvariant.

Lemma 5.1. If both x and y are simple vertices then $\begin{array} { r } { p _ { t } ( x , y ) = \frac { \nu _ { 0 } ( y ) } { \nu _ { 0 } ( x ) + \nu _ { 0 } ( y ) } \mathrm { ~ a n d ~ } p _ { t } ( y , x ) = \frac { \nu _ { 0 } ( x ) } { \nu _ { 0 } ( x ) + \nu _ { 0 } ( y ) } . } \end{array}$

Proof. Notice that we can write

$$
\begin{array}{l} p _ {t} (x, y) = \frac {v _ {t} (y)}{v _ {t} (x) + v _ {t} (y)} \\ \quad = \frac {v _ {0} (y) \cdot a ^ {t}}{v _ {0} (y) \cdot a ^ {t} + v _ {0} (y) \cdot a ^ {t}} [ \text { by   (10) } ] \\ \quad = \frac {v _ {0} (y) \cdot a ^ {t}}{(v _ {0} (x) + v _ {0} (y)) \cdot a ^ {t}} \\ \quad = \frac {v _ {0} (y)}{v _ {0} (x) + v _ {0} (y)}. \end{array}
$$

The fact that $\begin{array} { r } { p _ { t } ( y , x ) = \frac { \nu _ { 0 } ( x ) } { \nu _ { 0 } ( x ) + \nu _ { 0 } ( y ) } } \end{array}$ is proved similarly. □

Lemma 5.1 indicates that, as long as x and y remain simple vertices, the probability that x (resp. y) makes an integration offer to y (resp. x) is time-independent. The best intuitive justification we can offer is that decay affects all simple vertices in equal measure and, in relative terms, they remain equally desirable or undesirable to each other.<sup>9</sup> It is interesting to note that although stated in the context of multiplicative delay, Lemma 5.1 holds for additive delay as well.

It is interesting, and somewhat surprising, that Lemma 5.1 can be extended to composite vertices. Indeed, suppose that the composite vertices x and y were obtained, over time, by the integration, in some order, of vertices $\{ x _ { 1 } , x _ { 2 } , . . . , x _ { r } \}$ and $\{ y _ { 1 } , y _ { 2 } , . . . , y _ { s } \}$ , respectively.

Lemma 5.2. In slot t, vertex x (resp. y) makes an integration offer to vertex y (resp. x) with probability

$$
p _ {t} (x, y) = \frac {\sum_ {i = 1} ^ {s} v _ {0} (y _ {i})}{\sum_ {j = 1} ^ {r} v _ {0} (x _ {j}) + \sum_ {i = 1} ^ {s} v _ {0} (y _ {i})}
$$

and

$$
p _ {t} (y, x) = \frac {\sum_ {j = 1} ^ {r} v _ {0} \left(x _ {j}\right)}{\sum_ {j = 1} ^ {r} v _ {0} \left(x _ {j}\right) + \sum_ {i = 1} ^ {s} v _ {0} \left(y _ {i}\right)}
$$

respectively.

Proof. We begin by showing that

$$
v _ {t} (x) = \left(\sum_ {j = 1} ^ {r} v _ {0} \left(x _ {j}\right)\right) \cdot a ^ {t}.\tag{23}
$$

The proof of (23) is by induction on t. The basis is easy: if t = 1, then the integration must have involved two vertices and the conclusion follows from Lemma 5.1.

For the inductive step, let t be arbitrary and assume that (23) holds for all composite vertices obtained by integration in fewer than t time slots. We may assume that the integration operation that generated x occurred in time slot t and involved two vertices $x ^ { \prime }$ and $x ^ { \prime \prime }$ consisting respectively, of the integration (in some order) of vertices $\{ x _ { 1 } ^ { \prime } , ~ x _ { 2 } ^ { \prime } , . . . , ~ x _ { r _ { 1 } } ^ { \prime } \}$ and $\{ x _ { 1 } ^ { \prime \prime } , ~ x _ { 2 } ^ { \prime \prime } , . . . , ~ x _ { r , } ^ { \prime \prime } \}$ respectively, where $x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } . . . , x _ { r _ { 1 } } ^ { \prime } , x _ { 1 } ^ { \prime \prime } , x _ { 2 } ^ { \prime \prime } . . . , x _ { r _ { 2 } } ^ { \prime \prime }$ is some permutation of $x _ { 1 } , x _ { 2 } , . . . , x _ { r }$

We assume, without loss of generality, that vertices $x ^ { \prime }$ and $x ^ { \prime \prime }$ were obtained in time slots $t ^ { \prime }$ and $t ^ { \prime \prime } { } _ { ; }$ , both preceding t. By the inductive hypothesis, we have

$$
v _ {t ^ {\prime}} (x ^ {\prime}) = \left(\sum_ {i = 1} ^ {r _ {1}} v _ {0} (x _ {i} ^ {\prime})\right) \cdot a ^ {t ^ {\prime}}
$$

and

$$
v _ {t ^ {\prime \prime}} (x ^ {\prime \prime}) = \left(\sum_ {j = 1} ^ {r _ {2}} v _ {0} \big (x _ {j} ^ {\prime \prime} \big)\right) \cdot a ^ {t ^ {\prime \prime}}.
$$

In the time span between $t ^ { \prime }$ and t the value of $x ^ { \prime }$ has decayed in such a way that

$$
\begin{array}{c} v _ {t} (x ^ {\prime}) = \left(\sum_ {i = 1} ^ {r _ {1}} v _ {0} (x _ {i} ^ {\prime})\right) \cdot a ^ {t ^ {\prime}} \cdot a ^ {t - t ^ {\prime}} \\ = \left(\sum_ {i = 1} ^ {r _ {1}} v _ {0} (x _ {i} ^ {\prime})\right) \cdot a ^ {t}. \end{array}
$$

Similarly, in the time interval between $t ^ { \prime \prime }$ and $t ,$ the value of $x ^ { \prime \prime }$ has decayed to reach

$$
v _ {t} (x ^ {\prime \prime}) = \left(\sum_ {j = 1} ^ {r _ {2}} v _ {0} \big (x _ {j} ^ {\prime \prime} \big)\right) \cdot a ^ {t}.
$$

Thus, the integration in time slot t produces a combined value of

$$
\begin{array}{l} v _ {t} (x) = v _ {t} \left(x ^ {\prime}\right) + v _ {t} \left(x ^ {\prime \prime}\right) = \left(\sum_ {i = 1} ^ {r _ {1}} v _ {0} \left(x _ {i} ^ {\prime}\right)\right) \cdot a ^ {t} \\ \quad + \left(\sum_ {j = 1} ^ {r _ {2}} v _ {0} \left(x _ {j} ^ {\prime \prime}\right)\right) \cdot a ^ {t} = \left(\sum_ {j = 1} ^ {r} v _ {0} \left(x _ {j}\right)\right) \cdot a ^ {t} \end{array}
$$

as claimed. This completes the proof of (23).

We now return to the proof of Lemma 5.2. By virtue of (21), vertex x makes an integration offer to $y$ with probability

$$
\begin{array}{l} p _ {t} (x, y) = \frac {v _ {t} (y)}{v _ {t} (x) + v _ {t} (y)} \\ = \frac {\left(\sum_ {i = 1} ^ {s} v _ {0} (y _ {i})\right) \cdot a ^ {t}}{\left(\sum_ {j = 1} ^ {r} v _ {0} (x _ {j})\right) \cdot a ^ {t} + \left(\sum_ {i = 1} ^ {s} v _ {0} (y _ {i})\right) \cdot a ^ {t}} \\ = \frac {\sum_ {i = 1} ^ {s} v _ {0} (y _ {i})}{\sum_ {j = 1} ^ {r} v _ {0} (x _ {j}) + \sum_ {i = 1} ^ {s} v _ {0} (y _ {i})} \end{array}
$$

completing the proof of the lemma.

Lemma 5.2 tells us that all integration decisions, as reflected by the integration offer probabilities, are timeindependent and only depend on the original value of the sets of vertices involved.

## 6. To integrate or not to integrate?

For reasons of simplicity we assume that integration offers are synchronous. While this assumption may not hold in some applications, it is certainly true in sensor networks [35].

Eqs. (21) and (22) express probabilities for various vertices to initiate an integration offer, assuming that integration is considered to be beneficial for the vertex. How is this determined?

The obvious answer to this question is that integration with vertex $y$ is advantageous to x only if

$$
v _ {t} (x) <   \tilde {v} _ {t + \Delta} (x)\tag{24}
$$

where

$\nu _ { t } ( x )$ is the current value of $x ,$ and

$\tilde { \nu } _ { t + \varDelta } \left( x \right)$ is the expected value of x after integration,<sup>10</sup> assuming that integration takes Δ time.

Intuitively, if x has a lesser value than $y$ then it is always better for x to integrate. How about if x has a larger value than that of $y \mathrm { ? }$

In this section we will identify a threshold λ such that integration with y is beneficial provided that

$$
\frac {v (y)}{v (x) + v (y)} > \lambda .
$$

It is clear that the integration of x and y may occur in exactly one of the following three scenarios:

Scenario 1: In time slot t both x and y send a courier towards each other as illustrated in Fig. 5. Evidently, in this case, the two couriers meet half-way between x and y, at which point integration occurs. Thus, in this scenario, the integration process will be completed at the end of time slot $t + { \frac { d ( x , y ) } { \gamma } }$

Scenario $2 \vdots$ In time slot $t , x$ dispatches a courier towards $y$ but y does not send a courier towards $x ,$ as illustrated in Fig. 6. In this case, y accepts the integration offer with probability $\frac { \nu ( x ) } { \nu ( x ) + \nu ( y ) } .$ If x's integration offer is accepted, integration occurs at the end of time slot $ t + d ( x , y ) ;$

Scenario $3 \colon$ In slot $t , y$ sends a courier towards x but x does not send a courier towards $y ,$ as illustrated in Fig. 7. Upon receipt, x accepts the integration offer with probability $\frac { \nu ( x ) } { \nu ( x ) + \nu ( y ) } .$ . If such is the case, integration occurs at time slot $t + d ( x , y )$

## 6.1. A closer look at Scenario 1

We assume that the decisions of x and y to send couriers are independent events. By (21) and (22) the probability, $p _ { 1 }$ , of the event that both x and y send a courier towards each other can be expressed as

![](/api/attachments/SUPF2JJ3/fulltext/images/e6a3c10177cfda12790b35d745a8b4530d60ea65e7a8616cfc2e54e3e8a78c6f.jpg)  
Fig. 5. Illustrating the first integration scenario.

![](/api/attachments/SUPF2JJ3/fulltext/images/40ff1bf990c9592f6335f201fc6c6d38077ac0b740be2da35223ab45b0f86f1b.jpg)  
Fig. 6. Illustrating the second integration scenario.

![](/api/attachments/SUPF2JJ3/fulltext/images/bab7a53903e84a4379cdcd75f96407a95ae0498ddeeb0ce15dfac0af2f5ff87c.jpg)  
Fig. 7. Illustrating the third integration scenario

$$
\begin{array}{l} p _ {1} = \frac {v _ {t} (y)}{v _ {t} (x) + v _ {t} (y)} \cdot \frac {v _ {t} (x)}{v _ {t} (x) + v _ {t} (y)} = \frac {v _ {t} (x) v _ {t} (y)}{\left[ v _ {t} (x) + v _ {t} (y) \right] ^ {2}} \\ = \frac {v _ {0} (x) v _ {0} (y)}{\left[ v _ {0} (x) + v _ {0} (y) \right] ^ {2}} [ \text { by   Lemmas   5.1   and   5.2 } ] \\ = \frac {v (x) v (y)}{\left[ v (x) + v (y) \right] ^ {2}}. \end{array}\tag{25}
$$

Consequently, the expected value, $\tilde { \nu } _ { t + \frac { d ( x , y ) } { 2 } } ( x )$ , of x at time $t + { \frac { d ( x , y ) } { 2 } }$ is

$$
\begin{array}{l} \tilde {v} _ {t + \frac {d (x , y)}{2}} (x) = (1 - p _ {1}) \cdot v _ {t + \frac {d (x , y)}{2}} (x) \\ \qquad + p _ {1} \cdot (v _ {t} (x) + v _ {t} (y)) \cdot a ^ {\frac {d (x , y)}{2}} \\ \qquad = v (x) \cdot \left(1 - \frac {v (x) v (y)}{\left[ v (x) + v (y) \right] ^ {2}}\right) \cdot a ^ {t + \frac {d (x , y)}{2}} \\ \qquad + \frac {(v (x) + v (y)) \cdot v (x) v (y) \cdot a ^ {t + \frac {d (x , y)}{2}}}{\left[ v (x) + v (y) \right] ^ {2}} \\ \qquad = v (x) \cdot a ^ {t + \frac {d (x , y)}{2}} \\ \qquad \times \left[ 1 - \frac {v (x) v (y)}{\left[ v (x) + v (y) \right] ^ {2}} + \frac {v (y) \cdot [ v (x) + v (y) ]}{\left[ v (x) + v (y) \right] ^ {2}} \right] \\ \qquad = v (x) \cdot a ^ {t + \frac {d (x , y)}{2}} \cdot \left[ 1 + \left(\frac {v (y)}{v (x) + v (y)}\right) ^ {2} \right]. \end{array}
$$

Vertex x will find it beneficial to integrate with y (and, thus, to extend an integration offer to it) only if $\nu _ { t } ( x )$ is strictly smaller than $\tilde { \nu } _ { t + \frac { d ( x , y ) } { 2 } } ( x )$ . This observation allows us to write

$$
v _ {t} (x) = v (x) \cdot a ^ {t} <   v (x) \cdot a ^ {t + \frac {d (x , y)}{2}} \cdot \left[ 1 + \left(\frac {v (y)}{v (x) + v (y)}\right) ^ {2} \right]
$$

which, after simple algebra, yields to following equivalent inequality

$$
1 <   a ^ {\frac {d (x , y)}{2}} \cdot \left[ 1 + \left(\frac {v (y)}{v (x) + v (y)}\right) ^ {2} \right]
$$

which, in turn, is equivalent to

$$
\left(\frac {v (y)}{v (x) + v (y)}\right) ^ {2} > a ^ {- \frac {d (x , y)}{2}} - 1.\tag{26}
$$

Observe that (14) implies

$$
a ^ {- \frac {d (x , y)}{2}} \geq 1.
$$

Therefore, inequality (26) is equivalent to:

$$
\frac {v (y)}{v (x) + v (y)} > \sqrt {a ^ {- \frac {d (x , y)}{2}} - 1}.\tag{27}
$$

Eq. (27) spells out the desired condition for integration. By writing

$$
\lambda = \sqrt {a ^ {- \frac {d (x , y)}{2}} - 1}
$$

it becomes clear that in order for vertex x to consider integration with y, the ratio $\frac { \nu ( y ) } { \nu ( x ) + \nu ( y ) }$ must exceed λ. With this, we obtain an amended form of (21):

$$
p _ {t} (x, y) = \left\{ \begin{array}{l l} 0 & \text { if } \frac {v (y)}{v (x) + v (y)} \leq \sqrt {a ^ {- \frac {d (x , y)}{2}} - 1} \\ \frac {v (y)}{v (x) + v (y)} & \text { otherwise. } \end{array} \right.\tag{28}
$$

Up to this point we have looked at integration from x's perspective. What does y think? Intuitively, we expect y to be even more inclined to integrate, especially with a vertex of a larger value. This intuition is borne out by the following simple computation that mimics the reasoning of vertex x. Indeed, y finds it profitable to integrate with x as soon as its expected value after integration exceeds it current value.

The expected value of y at time $t + { \frac { d ( x , y ) } { 2 } }$ is

$$
\begin{array}{l} \tilde {v} _ {t + \frac {d (x , y)}{2}} (y) = (1 - p _ {1}) \cdot v _ {t + \frac {d (x , y)}{2}} (y) \\ \qquad + p _ {1} \cdot (v _ {t} (x) + v _ {t} (y)) \cdot a ^ {\frac {d (x , y)}{2}} \\ \qquad = v (y) \cdot \left(1 - \frac {v (x) v (y)}{\left[ v (x) + v (y) \right] ^ {2}}\right) \cdot a ^ {t + \frac {d (x , y)}{2}} \\ \qquad + \frac {(v (x) + v (y)) \cdot v (x) v (y) \cdot a ^ {t + \frac {d (x , y)}{2}}}{\left[ v (x) + v (y) \right] ^ {2}} \\ \qquad = v (y) \cdot a ^ {t + \frac {d (x , y)}{2}} \cdot [ 1 - \frac {v (x) v (y)}{\left[ v (x) + v (y) \right] ^ {2}} \\ \qquad + \frac {v (x) \cdot [ v (x) + v (y) ]}{\left[ v (x) + v (y) \right] ^ {2}} ] \\ \qquad = v (y) \cdot a ^ {t + \frac {d (x , y)}{2}} \cdot \left[ 1 + \left(\frac {v (x)}{v (x) + v (y)}\right) ^ {2} \right]. \end{array}
$$

Thus, y favors integration as soon as

$$
v _ {t} (y) = v (y) \cdot a ^ {t} <   v (y) \cdot a ^ {t + \frac {d (x , y)}{2}} \cdot \left[ 1 + \left(\frac {v (x)}{v (x) + v (y)}\right) ^ {2} \right].
$$

After simple algebra this yields the following equivalent inequality

$$
1 <   a ^ {\frac {d (x , y)}{2}} \cdot \left[ 1 + \left(\frac {v (x)}{v (x) + v (y)}\right) ^ {2} \right]
$$

which can be written as

$$
\left(\frac {v (x)}{v (x) + v (y)}\right) ^ {2} > a ^ {- \frac {d (x , y)}{2}} - 1.\tag{29}
$$

Since, by (14), $a ^ { - { \frac { d ( x , y ) } { 2 } } } \geq 1$ , (29) is equivalent to:

$$
\frac {v (x)}{v (x) + v (y)} > \sqrt {a ^ {- \frac {d (x , y)}{2}} - 1}.\tag{30}
$$

Observe that the assumption $\nu ( x ) > \nu ( y )$ implies that (30) is less stringent than (27). Consequently, y will find it advantageous to integrate with x even when x does not wish to integrate with y. In any case, our analysis leads to an amended form of (22):

$$
p _ {t} (y, x) = \left\{ \begin{array}{l l} 0 & \text { if } \frac {v (x)}{v (x) + v (y)} \leq \sqrt {a ^ {- \frac {d (x , y)}{2}} - 1}, \\ \frac {v (x)}{v (x) + v (y)} & \text { otherwise. } \end{array} \right.\tag{31}
$$

## 6.2. What happens in Scenario 2?

Let $p _ { 2 }$ denote the probability of integration under the conditions of Scenario 2. The corresponding event occurs only if the following events occur simultaneously:

• x sends a courier towards y,

• y does not send a courier towards x, and

• upon receipt, y accepts the integration offer.

Assuming that all the events mentioned are independent, $p _ { 2 }$ can be expressed as:

$$
\begin{array}{l} p _ {2} = \frac {v _ {t} (y)}{v _ {t} (x) + v _ {t} (y)} \cdot \left(1 - \frac {v _ {t} (x)}{v _ {t} (x) + v _ {t} (y)}\right) \cdot \frac {v _ {t} (x)}{v _ {t} (x) + v _ {t} (y)} \\ = \frac {v _ {t} (x) v _ {t} ^ {2} (y)}{\left[ v _ {t} (x) + v _ {t} (y) \right] ^ {3}} \left[ \text { where   we   write } v _ {t} ^ {2} (y) \text { for } (v (t)) ^ {2} \right] \\ = \frac {v _ {t} (x) v _ {t} ^ {2} (y)}{\left[ v _ {t} (x) + v _ {t} (y) \right] ^ {3}} \left[ \text { where   we   write } v _ {t} ^ {2} (y) \text { for } (v (t)) ^ {2} \right] \\ = \frac {v_ {0} (x) v _ {0} ^ {2} (y)}{\left[ v _ {0} (x) + v _ {0} (y) \right] ^ {3}} [ \text { by   Lemmas   5.1   and   5.2 } ] \\ = \frac {v (x) v ^ {2} (y)}{\left[ v (x) + v (y) \right] ^ {3}} [ \text { by   writing } v (x) \text { and } \\ v (y) \text { for } v _ {0} (x) \text { and } v _ {0} (y), \text { respectively. } ] \end{array}\tag{32}
$$

With this, it is easy to compute the expected value, $\tilde { \nu } _ { t + d ( x , \ y ) } ( x )$ , of x in time slot $t + d ( x , y )$

$$
\begin{array}{l} \tilde {v} _ {t + d (x, y)} (x) = (1 - p _ {2}) \cdot v _ {t + d (x, y)} (x) \\ \qquad + p _ {2} \cdot (v _ {t} (x) + v _ {t} (y)) \cdot a ^ {d (x, y)} \\ \qquad = v (x) \cdot \left(1 - \frac {v (x) v ^ {2} (y)}{\left[ v (x) + v (y) \right] ^ {3}}\right) \cdot a ^ {t + d (x, y)} \\ \qquad + \frac {(v (x) + v (y)) \cdot v (x) v ^ {2} (y) \cdot a ^ {t + d (x , y)}}{\left[ v (x) + v (y) \right] ^ {3}} \\ \qquad = v (x) \cdot a ^ {t + d (x, y)} \cdot \left[ 1 - \frac {v (x) v ^ {2} (y)}{\left[ v (x) + v (y) \right] ^ {3}} \right. \\ \qquad \left. + \frac {v ^ {2} (y) \cdot [ v (x) + v (y) ]}{[ v (x) + v (y) ] ^ {3}} \right] \\ \qquad = v (x) \cdot a ^ {t + d (x, y)} \cdot \left[ 1 + \left(\frac {v (y)}{v (x) + v (y)}\right) ^ {3} \right] \\ \qquad = v _ {t + d (x, y)} (x) \cdot \left[ 1 + \left(\frac {v (y)}{v (x) + v (y)}\right) ^ {3} \right]. \end{array}
$$

Naturally, x will find it beneficial to integrate with $y ,$ only if $\nu _ { t } ( x )$ is strictly smaller than $\tilde { \nu } _ { t + d ( x , \ y ) } ( x )$ . This observation allows us to write

$$
v _ {t} (x) = v (x) \cdot a ^ {t} <   v (x) \cdot a ^ {t + d (x, y)} \cdot \left[ 1 + \left(\frac {v (y)}{v (x) + v (y)}\right) ^ {3} \right]
$$

which, after simple algebra, yields to following equivalent inequality

$$
1 <   a ^ {d (x, y)} \cdot \left[ 1 + \left(\frac {v (y)}{v (x) + v (y)}\right) ^ {3} \right]
$$

which boils down to

$$
\left(\frac {v (y)}{v (x) + v (y)}\right) ^ {3} > a ^ {- d (x, y)} - 1.\tag{33}
$$

By (14), we have $a ^ { - d ( x , y ) } \geq 1$ . Therefore, the inequality (33) is equivalent to:

$$
\frac {v (y)}{v (x) + v (y)} > \left(a ^ {- d (x, y)} - 1\right) ^ {\frac {1}{3}}.\tag{34}
$$

By Lemma A.1 in the Appendix, the condition captured by (34) is more stringent than the one in (27). This, in turn, suggests the following strategy of vertex x (the one with the larger value):

• If condition (27) holds, x sends a courier towards vertex y with probability $\textstyle { \frac { \nu ( y ) } { \nu ( x ) + \nu ( y ) } } ;$

• If the courier does not meet the courier from y at the mid-point, then $x ' s$ courier is instructed to march on to y only if (34) holds;

• Otherwise, the courier returns to x and the integration attempt fails.

## 6.3. What happens in Scenario 3?

Let $p _ { 3 }$ denote the probability of integration under the conditions of Scenario 3. Assuming all events involved to be independent, $p _ { 3 }$ can be expressed as:

$$
\begin{array}{l} p _ {3} = \left(1 - \frac {v _ {t} (y)}{v _ {t} (x) + v _ {t} (y)}\right) \cdot \frac {v _ {t} (x)}{v _ {t} (x) + v _ {t} (y)} \cdot \frac {v _ {t} (y)}{v _ {t} (x) + v _ {t} (y)} \\ = \frac {v _ {t} (y) v _ {t} ^ {2} (x)}{\left[ v _ {t} (x) + v _ {t} (y) \right] ^ {3}} \left[ \text { where   we   write } v _ {t} ^ {2} (y) \text { for } (v (t)) ^ {2} \right] \\ = \frac {v _ {0} (y) v _ {0} ^ {2} (x)}{\left[ v _ {0} (x) + v _ {0} (y) \right] ^ {3}} [ \text { by   Lemmas   5.1   and   5.2 } ] \\ = \frac {v ^ {2} (x) v (y)}{\left[ v (x) + v (y) \right] ^ {3}} [ \text { by   writing } v (x) \text { and } v (y) \text { for } \\ v _ {0} (x) \text { and } v _ {0} (y), \text { respectively. } ] \end{array} \tag {35}
$$

With this, the expected value, $\tilde { \nu } _ { t + d ( x , y ) } ( x )$ , of x at time $t + d ( x , y )$ becomes

$$
\begin{array}{l} \tilde {v} _ {t + d (x, y)} (x) = (1 - p _ {3}) \cdot v _ {t + d (x, y)} (x) + p _ {3} \cdot (v _ {t} (x) + v _ {t} (y)) \cdot a ^ {d (x, y)} \\ \qquad = v (x) \cdot \left(1 - \frac {v ^ {2} (x) v (y)}{\left[ v (x) + v (y) \right] ^ {3}}\right) \cdot a ^ {t + d (x, y)} \\ \qquad + \frac {(v (x) + v (y)) \cdot v ^ {2} (x) v (y) \cdot a ^ {t + d (x , y)}}{\left[ v (x) + v (y) \right] ^ {3}} \\ \qquad = v (x) \cdot a ^ {t + d (x, y)} \\ \qquad \times \left[ 1 - \frac {v ^ {2} (x) v (y)}{\left[ v (x) + v (y) \right] ^ {3}} + \frac {v (x) v (y) \cdot [ v (x) + v (y) ]}{[ v (x) + v (y) ] ^ {3}} \right] \\ \qquad = v (x) \cdot a ^ {t + d (x, y)} \cdot \left[ 1 + \frac {v (x) v ^ {2} (y)}{\left[ v (x) + v (y) \right] ^ {3}} \right] \\ \qquad = v _ {t + d (x, y)} (x) \cdot \left[ 1 + \frac {v (x) v ^ {2} (y)}{\left[ v (x) + v (y) \right] ^ {3}} \right]. \end{array}
$$

As before, x will be interested to integrate with $y ,$ only if $\nu _ { t } ( x )$ is strictly smaller than $\tilde { \nu } _ { t + d ( x , \ y ) } ( x )$ . This observation allows us to write

$$
v _ {t} (x) = v (x) \cdot a ^ {t} <   v (x) \cdot a ^ {t + d (x, y)} \cdot \left[ 1 + \frac {v (x) v ^ {2} (y)}{\left[ v (x) + v (y) \right] ^ {3}} \right]
$$

which, after simple algebra, yields to following equivalent inequality

$$
1 <   a ^ {d (x, y)} \cdot \left[ 1 + \frac {v (x) v ^ {2} (y)}{\left[ v (x) + v (y) \right] ^ {3}} \right]
$$

which yields

$$
\frac {v (x) v ^ {2} (y)}{\left[ v (x) + v (y) \right] ^ {3}} > a ^ {- d (x, y)} - 1.\tag{36}
$$

Assuming, as we did, that $\nu ( x ) > \nu ( y )$ , it turns out that (36) is less stringent than (33). It follows that integration under Scenario 3 is likelier to happen than under Scenario 2. This is not entirely unexpected since $p _ { 3 }$ is larger than $p _ { 2 }$

It is also interesting that, in Scenario 3, vertex y has a strategy that mirrors that of vertex x in Scenario 2: namely, if its courier does not meet at half-point the courier of x it then continues only if a certain condition, that mirrors (34) holds.

## 6.4. What is the probability of integration?

It is perhaps appropriate to take a final look at the probability of integration, as discussed in the previous subsections of this section. More specifically, assume that some two vertices x and y possessing values v(x)

and $\nu ( \nu )$ , respectively, are involved in an integration attempt that begins, at the end of time slot t.

What is the probability that, at the end of $d ( x , y )$ time slots the two vertices will be integrated?

This question is better dealt with by evaluating the probability of the complementary event, namely that the two vertices will still not be integrated at the end of $\cdot d ( x , y )$ time slots. For this purpose, we note that

• by (25), the probability that the integration occurs at the end of $\frac { \cdot d ( x , y ) } { 2 }$ time slots is $\begin{array} { r } { \frac { \nu ( x ) \nu ( y ) ^ { - } } { [ \nu ( x ) + \nu ( y ) ] ^ { 2 } } , } \end{array}$

<sup>½</sup> <sup></sup>  <sup>ð</sup> <sup>Þþ</sup> <sup>ð</sup> <sup>Þ</sup> • by (32) and (35), combined, the probability that integration occurs precisely at the end of $d ( x , y )$ time slots (and not $\frac { d ( x , y ) } { 2 }$ time slots) is

$$
\begin{array}{c} \frac {v (x) v ^ {2} (y)}{\left[ v (x) + v (y) \right] ^ {3}} + \frac {v ^ {2} (x) v (y)}{\left[ v (x) + v (y) \right] ^ {3}} \\ = \frac {v (x) v (y) [ v (x) + v (y) ]}{\left[ v (x) + v (y) \right] ^ {3}} = \frac {v (x) v (y)}{\left[ v (x) + v (y) \right] ^ {2}} \end{array}\tag{37}
$$

Now, (25) and (37), combined, imply that the probability of no integration at the end o $\mathbf { \chi } ) d ( x , y )$ time slots is

$$
\begin{array}{c} 1 - \frac {v (x) v (y)}{\left[ v (x) + v (y) \right] ^ {2}} - \frac {v (x) v (y)}{\left[ v (x) + v (y) \right] ^ {2}} = 1 - \frac {2 v (x) v (y)}{\left[ v (x) + v (y) \right] ^ {2}} \\ = \frac {v ^ {2} (x) + v ^ {2} (y)}{\left[ v (x) + v (y) \right] ^ {2}} = \frac {\left[ v (x) - v (y) \right] ^ {2} + 2 v (x) v (y)}{\left[ v (x) + v (y) \right] ^ {2}} \end{array}\tag{38}
$$

In addition, (38) shows that the probability of no integration is minimized when $\nu ( x ) - \nu ( y ) { = } 0$ . This is to say that vertices x and y stand the best chance of integrating if they are of equal (or similar) value. Fig. 8 illustrates various values of the integration probability of vertices x and y where v(x) and v(y) vary in the range [0.1–20.0]. The figure provides an empirical confirmation of (38).

![](/api/attachments/SUPF2JJ3/fulltext/images/8cf589a6da0b8f92c558464a3f7045a0b001eb965fdaf1a8019365bd7dfa4e6f.jpg)  
Fig. 8. Illustrating the integration probability.

Also, (38) shows and Fig. 9 confirms that the larger the imbalance between v(x) and v(y), i.e. the larger the difference $| \nu ( x ) - \nu ( y ) |$ |, the larger the probability of no integration. Why is this ${ \bf s o } \mathrm { ? }$

In the context of sensor networks, the explanation is very simple. Sensors that have detected that an event has occurred carry a much larger value than those who have not. Consequently, it makes sense for the neighboring sensors that have detected the occurrence of the event to integrate thus corroborating the information and, perhaps, pinpointing the type of the event. For example, in sensor networks deployed with the mission of detecting intruders, two sensors that have identified an intruder will benefit from integrating their findings not only for the purpose of reinforcing the information collected but also in order to pinpoint the location and type of intruder detected. Conversely, the sensors that have not detected an event are discouraged from integration with other sensors that have not detected an intruder — they simply carry no information.

## 7. Putting our work in perspective

## 7.1. Limitations

We assumed that information deteriorates at a constant rate throughout the network. In a sensor network, we think this assumption is fair: the sensors have a common goal, and the information is all related to a single goal. In social networks, things may be more complex. For example, the freshness of information may be more valuable to a company on the verge of bankruptcy than to a company flush with money. There is an additional complication: the company on the verge of bankruptcy may want to disguise the urgency of its information needs, and may also want to inflate the value of the information they hold, in the hopes of merging prior to collapsing. Thus, in adversarial situations, there is uncertainty relating to the decay value of information to the participants. Also, participants may inflate the value of their information in the hopes of encouraging integration.

Such assumptions about the uncertainty of information functions and value will lead to more complex models. But such additional assumptions don't negate the primary idea explored here: both sides have different decision thresholds, with the less valuable player more likely to want to integrate.

We assumed a simple physical model of integration based on physical distance. In reality, the model is complex. Some communication is instant, and some is delayed through electronic queues, and others still through transportation queues. These different assumptions in heterogeneous networks will yield more complex models.

![](/api/attachments/SUPF2JJ3/fulltext/images/0627e484ef5ec40ac0d7d8c7a10167912940723c8e2180ee7b8f7f2d57305b39.jpg)  
Fig. 9. Illustrating the no integration probability.

We also have assumed a local decision model. This is realistic in the case of sensors. But in organizations, it may be possible to also reason at a global level. We can ask: how much worse is local decision making from global decision making? Another way of putting this: how far from optimal is a set of simple pairwise decisions? Our pairwise decisions are a kind of parallel greedy algorithm. We know that sometimes greedy algorithms can fail, but often they are good approximations.

We also assumed that information from the sensors is independent. This is generally true in geographic sensor networks. Sometimes there is overlap. Particularly in social networks, there are bound to be dependencies. In such cases, we cannot simply add values, but must determine the overlap and subtract that overlap from the sum. This may lead to a faster diminishment of returns from integrating: information may become progressively less novel to the higher-value nodes.

The size of data to integrate will effect the time to integrate. In fully electronic networks, the throughput of a link and the message size together affect overall latency (see [29] for a discussion on this topic related to mobile computing). Thus, in a more complex model, the size of the message and the electronic throughput may be important to include.

In our decision model shown here, we looked at the integration of a particular event – an intrusion – across a set of sensors. We did not model the continuous monitoring of a stream of events. In such cases, the decay of information becomes important: it will not make sense to integrate old, lower value information in comparison to newer, higher-value information. When there is an event stream, it becomes possible for the sensors to learn something about the environment, and about their fellow sensors' behaviors. Therefore, over time, sensors might make more effective decisions about who to integrate with, based on past experiences, using reinforcement learning techniques [19].

## 7.2. Sensor networks

In the realm of sensor networks, our model has its most direct application. Sensors with information in the environment might pair off with neighbors, integrate, and the composite neighbors formed through this operation could repeat the process until there is one composite node, indicating all nodes have received the relevant information.

This is different from traditional sensor integration techniques, and it can be compared to other techniques with respect to time to integrate, as well as energy usage. In order to shorten the time to integrate, additional constraints on integration might be placed to encourage stable marriage situations, with the goal of pairing up nodes in a way that would be collectively optimal.

Our model of time-based decay provides a way of marrying electronic communication, which is almost instant, with transportation, which is orders of magnitude slower. Clusters of sensors (or clusters of electronic networks) might be joined through couriers, as in [30,28].

## 7.3. Computer and social networks

Sensor networks share many characteristics with computer networks: sensors are themselves computers that differ from other computers with respect to size and energy consumption. Thus, models of sensor networks might also apply to larger networks, especially those that are resource constrained.

Sensor networks also share characteristics with social networks: the sensors are active integrators and decision makers, who have global goals, incomplete information, limited communication, and need to conserve their energy. Thus, such studies of sensor networks might yield insights into more complex social networks.

Even in situations where energy expenditure is not critical, human attention often is. In other words, it may be that not everything can be monitored all the time, and therefore human participation in the network needs to minimized. Thus the integration problem for any form of network is often a multi-attribute one: trying to detect events with minimal delay and integrate detection with minimal delay, while at the same time trying to minimize the use of energy — electrical energy in the case of sensor networks, and cognitive energy in the case of social networks.

The first implication of our work is that integration asymmetries might explain the general background of resistance to both technical and social integration in corporate settings. It may be that players have rational reasons not to share, and that those espousing sharing have to clearly understand the extent of the disincentives to doing so.

Second, the asymmetries in mergers might be studied by looking at the behavior of companies looking to acquire others and those looking to be acquired. Our model predicts that time will be important: that urgency relating to information may drive the deal. Also the size (and value) of a company may play an important role in terms of who controls the negotiation surrounding integration.

Third, the history of the integration of information systems in companies may follow the pattern of the model. Several departments consider pairwise whether or not to consolidate and share data; those pairs possessing data with equal value may choose to do so, but departments with high value data may choose not to share with smaller departments. Even though the imposition of a unified framework might eventually serve all, the pairwise, local decisions lead to fragmented information systems. Thus, what might in retrospect look like a series of bad decisions may in fact have been locally optimal for those involved. This, in turn, suggests that incentives to share data should in turn be asymmetrical, and be constructed to make cooperation more likely. For example, many companies meet resistance when installing enterprise application integration systems; this resistance may be entirely logical from a local perspective given the long time frames such installations take and the relative lack of benefit to those who already control valuable data. Incentives to such owners of data may need to be quite strong.

## 7.4. Directions for future work

In this paper we have provided an incentive-based probabilistic model for pairwise integration and have shown that the model finds applications to sensor networks, social networks and business applications such as merging between companies and departments. There are a number of natural ways in which the current work can be extended.

First, it would be of interest to see to what extent our incentive-based local integration has an “optimal” global effect after many pairs have had the chance to integrate. In order to do so we will need to build a model for the net benefits and costs of such a network. There is a multi-attribute decision problem at the root of such optimization. On the one hand, the network should aggregate values. On the other hand, the network should conserve energy. When energy conservation is important, there might be a point beyond which network nodes would find it undesirable to integrate further. Checking the optimality of our model is easy on small examples. We can consider the integration trees formed through the repeated application of probabilistic rules, and derive mean and variance statistics for these runs. Then we can evaluate all possible integration trees, and compare the energy savings and maximum value of all possible trees to the mean value of the probabilistic integration. We can then say how much worse the greedy probabilistic algorithm is from the optimal algorithm. We can go further and evaluate the optimal integration at each time step: as we pointed out before, this model does allow regions of a sensor network to gain local information before a global integration takes place.

Second, our model is similar to the preferential attachment model. But we predict that, at some point, nodes will start refusing integration from lower value nodes. Is our model more or less accurate than preferential attachment? We might test it through social network game experiments — for example [7].

Third, it would be interesting to investigate a few of the ramifications of our model. For example, what is the relationship of our integration to the classic Stable Marriage Problem.

Fourth, in our model we have assumed that information decays uniformly across the networks and the set of actors. However, it is unclear whether the decision process would change significantly if the value decay rate is nonuniform. In addition, the introduction of a stream of events may change the dynamics of the network by encouraging the processing of new information at the expense of old information.

## 8. Concluding remarks

This paper laid the foundations of a probabilistic perspective on integration. The crux of the paper is that the various players consider integration as a viable solution as soon as the expected benefit of integration out-weighs the status-quo. The decay of information value may push such negotiations to a conclusion, but those possessing high-valued information are not likely to pair up with those possessing low-valued information. The decay of information value with respect to time increases the pressure to integrate quickly. We have provided a model for how integration may occur over time, in a series of proposals, rejections and acceptances which can lead to consolidation and eventually full integration. Such integration can provide the shared awareness that cooperating actors in a network need to interpret their environment.

## Acknowledgments

The authors gratefully acknowledge the constructive comments and suggestions of three anonymous referees as well as those of the guest editors of the special issue.

J. Nickerson's research was supported in part by the Office of Naval Research under grant N00014-05-1- 00632. S. Olariu acknowledges National Science Foundation grants CNS-0721563 and CNS-0721586.

## Appendix A

The purpose of this appendix is to prove the following technical result.

Lemma A.1. For all real numbers a with $a \in ( 0 , 1 )$ and $d ( x , y ) > 0$ , the following inequality holds

$$
\left(a ^ {- \frac {d (x , y)}{2}} - 1\right) ^ {\frac {1}{2}} <   \left(a ^ {- d (x, y)} - 1\right) ^ {\frac {1}{3}}
$$

Proof. Write

$$
z = a ^ {- \frac {d (x , y)}{2}}
$$

and observe that $z > 1$ . With this substitution, the desired inequality is equivalent to

$$
(z - 1) ^ {\frac {1}{2}} <   (z ^ {2} - 1) ^ {\frac {1}{3}}
$$

which, in turn, reduces to

$$
(z - 1) ^ {3} <   (z ^ {2} - 1) ^ {2}.
$$

Simple algebra reduces this latter inequality to the tautology

$$
z - 1 <   (z + 1) ^ {2}
$$

completing the proof of the lemma.

## References

[1] N. Ahituv, A systematic approach toward assessing the value of an information system, MISQ 4 (4) (1980) 61–75.

[2] F. Akyildiz, W. Su, Y. Sankarasubramanian, E. Cayirci, Wireless sensor networks: a survey, Computer Networks 38 (4) (2002) 393–422.

[3] N.H. Anderson, Foundations of information integration theory, Academic Press, New York, 1981.

[4] N.H. Anderson, Contributions to information integration theory, L. Erlbaum Associates, Hillsdale, N.J., 1991

[5] K.J. Arrow, The value and the demand for information, in: C.B. McGuire, R. Radner (Eds.), Decision and organization. A volume in honor of Jacob Marschak, North-Holland Pub. Co., Amsterdam, 1972, pp. 131–140, (Edited by C. B. McGuire and Roy Radner. Contributors Kenneth J. Arrow, et. Al).

[6] A.-L. Barabási, R. Albert, Emergence of scaling in random netowks, Science 286 (1999) 509–512.

[7] T. Ben-Zvi, Corporate positioning: A business game perspective, Developments in Business Simulation and Experimental Exercises 32 (2007).

[8] T. Brody, S. Harnad, L. Carr, Earlier web usage statistics as predictors of later citation impact, Journal of the American Society for Information Science and Technology 57 (8) (2006) 1060–1072.

[9] K. Crowston, A taxonomy of organizational dependencies and coordination mechanisms, in: T.W. Malone, K. Crowston, G.A. Herman (Eds.), Organizing Business Knowledge: The MIT Process Handbook, MIT Press, 2003, pp. 85–108.

[10] K. Deutsch, Communication theory and political integration, in: P.E. Jacob, J.V. Toscano (Eds.), The integration of political communities. Lippincott, Philadelphia, 1964.

[11] S. Frederick, G. Leowenstein, T. O'Donoghue, Time discounting and time preference: a critical review, Journal of Economic Literature XL (2005) 351–401.

[12] K.H. Jones, K.N. Lodding, A. Wadaa, S. Olariu, L. Wilson, M. Eltoweissy, Biomimetic models for sensor networks — towards a social sensor network, Handbook of Bio-Inspired Algorithmic Techniques, CRC Press, Boca Raton, ISBN: 1-58488-475-4, 2005.

[13] K.H. Jones, K.N. Lodding, S. Olariu, L. Wilson, C. Xin, Biologyinspired distributed consensus in massively-deployed sensor networks, Proc. 4th International Conference on AD-HOC Networks, Cancun, Mexico, October 2005.

[14] K.H. Jones, K.N. Lodding, S. Olariu, L. Wilson, C. Xin, Energy usage in biomimetic models for massively-deployed sensor networks, Proc. 1-st IEEE Workshop on Mobile Ad-hoc and Uniquitous Sensor Networks, Ninjin, China, November 2005.

[15] K.H. Jones, K.N. Lodding, S. Olariu, L. Wilson, C. Xin, Sensor networks for situation management: a biomimetic model, Proc. IEEE MILCOM, Philadelphia, PA, October 2005.

[16] K.H. Jones, K.N. Lodding, S. Olariu, L. Wilson, C. Xin, Biologic-inspired architecture fro situation management, Prc 2nd Workshop on Situation Management (SIMA 2006) at IEEE MILCOM 2006, Washington, DC, October 2006.

[17] K.H. Jones, K. Lodding, S. Olariu, L. Wilson, C. Xin, Communal cooperation in sensor networks for situation management, Proc 9th International Conference for Information Fusion, (Fusion 2006), Florence, Italy, July 10–13, 2006.

[18] K.H. Jones, K. Lodding, S. Olariu, L. Wilson, C. Xin, Biologyinspired approach for ammunal behavior in sensor networks, Proc. 39thHawaii International Conference on System Sciences, (HICSS-39), Kauai, Hawaii, January 4–7, 2006.

[19] L.P. Kaebling, M.L. Littman, A.W. Moore, Reinforcement learning: a survey, Journal of Artificial Intelligence Research 4 (1996) 237–285.

[20] P. Kozma-Wiebe, S.M. Silverstein, A. Feher, I. Kovacs, P. Ulhaas, S.M. Wilkmiss, Development of a world-wide web based contour integration test, Computers in Human Behavior 22 (6) (2006) 971–980.

[21] P.R. Lawrence, J.W. Lorsch, Organization and environment; managing differentiation and integration, Harvard University, Boston, 1967.

[22] J.L. Lu, S.J. Williams, L. Kaufman, Behavioral lifetime of human auditory sensory memory predicted by physiological measures, Science 258 (1992) 1668–1670.

[23] T.W. Malone, K. Crowston, Interdisciplinary study of coordination, ACM Computing Surveys 26 (1) (1994) 87–119.

[24] T.W. Malone, K. Crowston, J. Lee, B. Pentland, C. Dellarocas, G. Wyner, J. Quinby, C.S. Osborn, A. Bernstein, G. Herman, M. Klein, E. O'Donnell, Tools for inventing organizations: toward a handbook of organizational processes, Management Science 45 (3) (1999) 435–443.

[25] J. Marschak, Economics of information systems, in: M.D. Intriligator (Ed.), Frontiers of quantitative economics: papers invented for presentation at the Econometric Society winter meetings, New York, 1969, North Holland Pub. Co., Amsterdam New York, 1971, pp. 32–108.

[26] J. Marschak, R. Radner, Economic theory of teams, Yale University Press, New Haven, 1972.

[27] R. McNaughton, Scheduling with deadlines and loss functions, Management Science 6 (1) (1959) 1–12.

[28] J. Nickerson, S. Olariu, Courier assignment in social networks, Proceedings of the 40th Annual Hawai'i International Conference on System Sciences, 2007.

[29] J.V. Nickerson, A concept of communication distance and its application to six situations in mobile environments, IEEE Transactions on Mobile Computing 5 (4) (2005) 409–419.

[30] J.V. Nickerson, Flying sinks: heuristics for movement in sensor networks, Proceedings the 39th Annual Hawaii International Conference on System Sciences, 2006.

[31] J.V. Nickerson, S. Olariu, A measure of integration and its application to sensor network, Workshop on Information Technology and Systems (WITS), 2005.

[32] J.V. Nickerson, S. Olariu, Protecting with sensor networks: attention and response, Proceedings of the 40th Annual Hawaii's International Conference on System Sciences, 2007.

[33] S. Olariu, M. Eltoweissy, M. Younis, ANSWER. Autonomous networked sensor systems, Journal of Parallel and Distributed Computing 63 (1) (2007).

[34] S. Olariu, J.V. Nickerson, Protecting with sensor networks: perimeters and axes, MILCOM, 2005.

[35] S. Olariu, A. Wadaa, W. L., M. Wltoweissy, Wireless sensor networks: leveraging the virtual infrastructure, IEEE Network 18 (4) (2004) 51–56.

[36] S. Olariu, Q. Xu, A simple robust virtual infrastructure for massively deployed wireless sensor networks, Computer Communications 28 (2005) 1505–1516.

[37] M.E. Porter, Competitive strategy: techniques for analyzing industries and competitors, Free Press, New York, 1980.

[38] D.R. Raban, S. Rafaelie, The effect of source nature and status on the subjective value of information, JASIST 57 (3) (2006) 321–329.

[39] W. Sheng, G. Tewolde, Y. Guo, Distributed robot-assisted node localization in active sensor networks, Proceedings of IEEE International Conference on Mechatronics and Automation, 2006.

[40] E.A. Stohr, J.V. Nickerson, Intra enterprise integration, in: J. Luftman (Ed.), Competing in the Information Age: Align in the Sand, Oxford University Press, New York, 2002, pp. 227–251.

[41] C.-P. Teo, J. Sethuraman, W.-P. Tan, Gale-shapely stable marriage problem revisited: Strategic issues and applications, Management Science 47 (9) (2007) 1252–1267.

[42] A. Wadaa, S. Olariu, L. Wilson, K. Jones, E. M, Training a sensor network, Journal of Mobile Networks and Applications 10 (1) (2005) 151–167.

[43] B. Yuan, M. Orlowaska, S. Sadiq, On the optimal robot routing problem in wireless sensor networks, IEEE Transactions on Knowledge and Data Engineering 19 (9) (2007).

![](/api/attachments/SUPF2JJ3/fulltext/images/86d986a8d40854d754dbb55d931c8edabcbf877aeccd88bb167c89348f841eaa.jpg)

Professor Olariu has obtained his BSc., MSc, and PhD degrees from McGill University in Montreal, Canada. During the years, he has held many different roles and responsibilities as a member of numerous organizations and teams. Much of his experience has been with the design and implementation of robust protocols for wireless networks and in particular sensor networks and their applications. He is applying mathematical modeling and analytical frameworks to the resolution of problems

ranging from securing communications, to predicting the behavior of complex systems, to evaluating performance of wireless networks. His research interests are in the area of complex systems enabled by largescale deployments of sensors and more specifically in securing systems of systems.

Professor Olariu is an Associate Editor of IEEE Transactions on Computers, IEEE Transactions on Parallel and Distributed Systems and Networks, and serves on the editorial board of Journal of Parallel and Distributed Computing, Journal of Ad hoc and Sensor Networks, and Parallel, Emergent and Distributed Systems.

![](/api/attachments/SUPF2JJ3/fulltext/images/d02f35fb2523c2732287aabb16f919471203bddb656e1bfc8f677878e95f7907.jpg)

Jeffrey V. Nickerson is Associate Professor and Director of the Center for Decision Technologies at Stevens Institute of Technology. Mr. Nickerson's research interests include social network analysis, sensor network design, and diagram use in system design. He holds a B.A. from UC Berkeley, an M.F.A from Rhode Island School of Design, and an M.S. and Ph.D. in Computer Science from New York University.
