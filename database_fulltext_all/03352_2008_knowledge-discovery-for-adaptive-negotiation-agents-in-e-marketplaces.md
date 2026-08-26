---
otero_id: 3352
otero_key: "TGVRQUXS"
title: "Knowledge discovery for adaptive negotiation agents in e-marketplaces"
authors: "Raymond Y.K. Lau; Yuefeng Li; Dawei Song; Ron Chi Wai Kwok"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.12.018"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Knowledge discovery for adaptive negotiation agents in e-marketplaces

Raymond Y.K. Lau <sup>a,⁎</sup>, Yuefeng Li <sup>b</sup>, Dawei Song <sup>c</sup>, Ron Chi Wai Kwok <sup>a</sup>

<sup>a</sup> Department of Information Systems, City University of Hong Kong, Tat Chee Avenue, Kowloon Hong Kong SAR, China <sup>b</sup> School of Software Engineering and Data Communications, Queensland University of Technology, GPO Box 2434, Brisbane, QLD 4001, Australia

<sup>c</sup> Knowledge Media Institute, The Open University, Walton Hall, Milton Keynes, MK7 6AA United Kingdom

Received 14 February 2007; received in revised form 30 November 2007; accepted 30 December 2007 Available online 15 January 2008

## Abstract

Intelligent software agents are promising in improving the effectiveness of e-marketplaces for e-commerce. Although a large amount of research has been conducted to develop negotiation protocols and mechanisms for e-marketplaces, existing negotiation mechanisms are weak in dealing with complex and dynamic negotiation spaces often found in e-commerce. This paper illustrates a novel knowledge discovery method and a probabilistic negotiation decision making mechanism to improve the performance of negotiation agents. Our preliminary experiments show that the probabilistic negotiation agents empowered by knowledge discovery mechanisms are more effective and efficient than the Pareto optimal negotiation agents in simulated e-marketplaces.

© 2008 Elsevier B.V. All rights reserved.

Keywords: Knowledge discovery; Bayesian learning; Adaptive negotiation agents; e-marketplaces

## 1. Introduction

The number of transactions conducted over e-marketplaces has grown rapidly in recent years. In the context of Business-to-Business (B2B) e-commerce, e-marketplaces are no longer operated in isolation but function as a series of interacting markets along an electronic supply chain (eChain) [33]. It is argued that software agents can provide high level of intelligence and autonomy for enhancing the effectiveness of e-marketplaces [6,15]. Software agents are encapsulated computer systems situated in some environments such as the Internet and are capable of flexible, autonomous actions in that environment to meet their design objectives [39]. These agents can incorporate experiential knowledge of past transactions to streamline the effects of volatile demand and supply conditions across multiple e-marketplaces in the electronic supply chain. Negotiation refers to the process by which group of agents (human or software) communicate with one another in order to reach a mutually acceptable agreement on resource allocation (distribution) [21,35,37]. This paper focuses on the development of a novel knowledge discovery mechanism to enhance negotiation agents' decision making processes in B2B e-marketplaces.

## 1.1. The problems

In typical B2B negotiation situations, a negotiator does not know the preferences of its opponents because each party wants to protect their own business interests. Nevertheless, knowing the preferences of the opponents (e.g., the reservation prices) may help improve the efficiency of the negotiation processes since negotiation agents (human or software) can avoid wasting their time to explore the non-fruitful negotiation options. For cooperative agents, having partial knowledge about their opponents may even help improve the negotiation effectiveness because it becomes easier for the agents to identify the “win–win” outcomes from among the set of feasible solutions. Unfortunately, classical negotiation models [5,32,36,40] do not address the learning issue essential for real-world negotiations. Instead, these models often assume that the preferences (e.g., the utility functions) of the opponents are available as public information. Such an assumption turns out to be invalid for typical e-commerce negotiation situations. Even though agent-based negotiation systems have been developed, these systems still suffer from the problems of supporting only limited types of negotiation scenarios (e.g., bi-lateral negotiations, price only negotiations, availability of opponents' payoff functions, or static negotiation spaces) [6,10,22,31]. One of the ways to alleviate the weakness of classical negotiation models and provide adequate support for realworld negotiations is to empower negotiation agents with a knowledge discovery mechanism so that they can continuously “mine” the preferences of the opponents based on the histories of negotiation dialogs among the participating agents.

## 1.2. Contributions

This paper illustrates the design and development of adaptive negotiation agents to enhance the degree of autonomy and the efficiency of e-marketplaces. In particular, the common weaknesses of the existing negotiation systems are addressed by introducing a novel knowledge discovery method and a Bayesian learning mechanism to improve the learning autonomy and adaptation power of negotiation agents. These adaptive probabilistic negotiation agents can discover crucial negotiation knowledge such as the opponents' changing preferences by mining the past negotiation histories and continuously monitoring the current negotiation dialogs with their opponents. Our preliminary experiments show that the probabilistic negotiation agents empowered by our novel knowledge discovery mechanism outperform a negotiation mechanism which guarantees Pareto optimum. Our research work opens the door to the development of practical intelligent systems to enhance the effectiveness and efficiency of modern e-marketplaces.

## 1.3. Outline of the paper

The remainder of the paper is organized as follows. A comparative study of previous research work is reported in Section 2. An introduction to the basic negotiation mechanism which guarantees Pareto optimum is given in Section 3. Section 4 illustrates the computational details of the probabilistic negotiation decision making mechanism and the associated knowledge discovery method for adaptive negotiation agents. Section 5 describes the quantitative evaluation of the adaptive negotiation agents and reports our experimental results. Finally, we offer concluding remarks and describe future direction of our research work.

## 2. Related work

Fuzzy logic has been applied to develop intelligent negotiation agents in e-marketplace [6]. Nine pre-defined fuzzy rules are used to generate trade-off for quantitative issues and another nine fuzzy rules are used to generate concession for qualitative issues separately [6]. The proposed negotiation model is somewhat limited since it is developed from the perspective of the supplier agents only. The main weakness of the fuzzy negotiation system is that it is not adaptive; for instance, the system cannot learn and refine the pre-defined fuzzy rules automatically. The probabilistic negotiation agents proposed in this paper are adaptive since they are empowered by a knowledge discovery mechanism to continuously mine the preference information of their opponents.

Non-linear regression has been applied to estimate the specific parameters (e.g., lower/upper bounds of the zone of acceptance of an attribute, negotiation deadline, weight of individual tactic, etc.) of the time-dependent and the behavior-dependent negotiation tactics [4]. It is assumed that agents' negotiation tactics are static and therefore it is possible to estimate these parameters based on the current negotiation dialogs. Instead of estimating the specific parameters of some pre-defined negotiation tactics, our proposed method adopts a nonparametric negotiation knowledge discovery approach where the opponents' negotiation tactics are not assumed static nor treated as public information. Our probabilistic negotiation agents are evaluated in multilateral dynamic negotiation scenarios.

Zeng and Sycara [40] have developed a sequential negotiation model called Bazaar. It was believed that an agent's belief about the opponent's true reservation price could be computed according to the posterior probability $\begin{array} { r } { \operatorname* { P r } ( H _ { i } | o ) = \frac { \operatorname* { P r } ( H _ { i } ) \operatorname* { P r } ( o | H _ { i } ) } { \sum _ { k = 1 } ^ { n } \operatorname* { P r } ( o | H _ { k } ) \operatorname* { P r } ( H _ { k } ) } } \end{array}$ , where Pr(H ) characterizes the <sup>¼</sup>probability distribution of the opponent's reservation prices and was assumed public information in the negotiation system. Moreover, domain knowledge in the form of conditional probabilities $\operatorname* { P r } ( o | H _ { i } )$ describing the chance of receiving an offering price $o$ given the opponent's true reservation price $H _ { i }$ was assumed available. Similar approach has also been applied to develop negotiation agents in the context of multi-agent co-ordination [5]. Nevertheless these approaches suffer from the problem of assuming the availability of the opponents' private information (e.g., the true reservation price). We illustrate an efficient data mining method of deriving the priori probabilities of offer acceptance without the assumption of the availability of the opponents' private information. Moreover, our proposed Bayesian learning mechanism is extended to deal with multiple negotiation issues.

Mining customers' transaction files to discover their shopping preferences has been conducted [16]. In particular, a Bayesian belief network (BBN) is constructed to capture the dependency among the preferred shopping items based on the mutual information derived from among these items. The recommender system generates a recommendation set by referring to the customer's current transactional actions and the trained BBN representing the shopping preferences of a particular customer. Our work is similar in the sense that we mine the negotiators' negotiation histories to discover their corresponding preferences. However, we use a computationally more efficient naive Bayesian approach since we would like the negotiation agents to conduct automated negotiations in real-time.

As a summary, there are variety of approaches of negotiation knowledge discovery such as case-based reasoning [3], fuzzy rules [6], time series approximation [24], Bayesian learning [5,40], Markov chain process [25], evolutionary learning [19], constraint satisfaction [38], etc. Generally speaking, these learning approaches can be classified into the broad categories of parametric [3,19,24] or non-parametric methods [5,25,40]. The negotiation knowledge discovery method illustrated in this paper is based on non-parametric approach since heterogeneous negotiation agents utilizing various tactics may be deployed to e-marketplaces. Our nonparametric negotiation learning method is unique in the sense that it can support multi-party multi-issue negotiation situations and it has been tested under dynamic negotiation environment.

## 3. A Pareto optimal negotiation model

A negotiation space $\mathrm { N e g } { = } { < P , A , D , U , T > }$ is a 5-tuple which consists of a finite set of negotiation parties (agents) $P ,$ a set of attributes (i.e., negotiation issues) A understood by all the parties $p \in P ,$ a set of attribute domains D for $A ,$ and a set of utility functions $U$ with each function $U _ { p } ^ { o } \in U$ for an agent $p \in P .$ An attribute domain is denoted $D _ { a _ { i } }$ where $D _ { a _ { i } } { \in } D$ and $a _ { i } \in A .$ . A utility function pertaining to an agent $p$ is defined by: $U _ { p } ^ { o } { : } D _ { a _ { 1 } } { \times } D _ { a _ { 2 } } { \times } { \ldots } { \times } D _ { a _ { n } } { \mapsto } [ 0 , 1 ]$ [17]. Each agent $p$ has a deadline $t _ { p } ^ { \bar { d } } \in T .$ It is assumed that information about $P , A , D$ is provided by the facilitator agents in an emarketplace. A multi-lateral negotiation situation can be modeled as many one-to-one bi-lateral negotiations where a negotiation agent $p$ maintains a separate negotiation dialog with each opponent. In a negotiation round, the agent will make an offer to each of its opponents in turn, and concentrate on the most favorable counter-offer from among the set of incoming offers evaluated according to its own payoff function $U _ { p } ^ { o }$

An offer $\overrightarrow { o } = < d _ { a _ { 1 } } , d _ { a _ { 2 } } , . . . , d _ { a _ { n } } >$ is a n-tuple of attribute values (intervals) pertaining to a finite set of attributes $A = \{ a _ { 1 } , a _ { 2 } , . . . a _ { n } \}$ . Generally speaking, a finite set of candidate offers $O _ { p }$ acceptable to an agent p $( \mathrm { i . e . , }$ , satisfying its hard constraints) is constructed via the Cartesian product $D _ { a _ { 1 } } { \times } D _ { a _ { 2 } } { \times } \cdots { \times } D _ { a _ { n } }$ . As human agents tend to specify their preferences in terms of a range of values, a more general representation of an offer is a tuple of attribute value intervals such as $\sigma _ { \mathrm { i } } { = } { < } 2 0 { - } 3 0 { , } 1 { - } 2 { , } 1 0 { - }$ 30,100–500N. The valuations of individual attributes and attribute values (intervals) are defined by the valuation functions $U _ { p } ^ { A } : A { \mapsto } [ 0 , 1 ]$ and $U _ { p } ^ { D _ { a i } } \colon D _ { a _ { i } } { \mapsto } [ 0 , 1 ]$ respectively, whereas $U _ { p } ^ { A }$ is an agent $p ^ { \star } { \bf s }$ valuation function for each attribute $a _ { i } { \in } A ,$ , and $U _ { p } ^ { D _ { a i } }$ is an agent $p ^ { \star }$ valuation function for each attribute value $d _ { a _ { i } } \in D _ { a _ { i } } .$ In addition, the valuations of attributes are assumed normalized, that is, $\textstyle { \sum _ { a _ { i } \in A } U _ { p } ^ { A } ( a _ { i } ) = 1 }$ . One common way to quantify an agent's preference $( \mathrm { i . e . }$ ., the utility function $U _ { p } ^ { o } )$ for an offer o is by a linear aggregation of the valuations [2,13,17,26]: $\begin{array} { r } { U _ { p } ^ { o } ( o ) = \sum _ { a _ { i } \in A , d a _ { i } \in O } U _ { p } ^ { A } ( a _ { i } ) \times } \end{array}$ $U _ { p } ^ { D _ { a i } } ( d _ { a _ { i } } ) _ { i }$ , where $d _ { a _ { i } }$ is the attribute value interval specified in an offer o.

If an agent's initial proposal is rejected by its opponent, it needs to propose an alternative offer with the least utility decrement $( \mathrm { i . e . , }$ computing a concession). An agent will maintain a set $O _ { p } ^ { \prime }$ which contains the offers it has proposed before (including the offer proposed in the current round). In a negotiation round, an alternative offer with a concession can be determined based on $\exists _ { o _ { \mathrm { c o u n t e r } } \in \{ O _ { p } - O _ { p ^ { \downarrow } } ^ { ' } \} } \forall _ { o _ { x } \in \{ O _ { p } - O _ { p ^ { \downarrow } } ^ { ' } \} } \colon [ o _ { x } \preceq _ { p } o _ { \mathrm { c o u n t e r } } ] ,$ where $O _ { x } { \preceq } _ { p } O _ { y }$ denotes that an offer $o _ { y }$ is more preferable than another offer $o _ { x }$ . The preference relation $\preceq _ { p }$ is a total ordering induced by an agent $p ^ { \star }$ s utility function $U _ { p } ^ { o }$ over the set of feasible offers $O _ { p } .$ . The concession mechanism works by picking an offer from the top of the list ranked by $( \preceq _ { p } , \{ O _ { p } - O _ { p } ^ { \prime } \} )$ in each negotiation round.

The term o<sub>≃</sub> represents agent $p ^ { \star }$ interpretation about the opponent's proposal o. Once $O _ { \simeq }$ is computed, acceptance of the incoming offer o can be determined with respect to $p ^ { \star }$ own preference $( \preceq _ { p } , O _ { p } )$ . An offer $o _ { \simeq } \in O _ { p }$ is equivalent to o iff every attribute interval of $O _ { z }$ <sub>≃</sub> intersects each corresponding attribute interval of o. The acceptance criteria for an incoming offer o (i.e., the equivalent o ) is defined by:

1. If $\forall _ { o _ { x } \in O p } O _ { x } \preceq _ { p } o _ { \simeq } ,$ an agent $p$ should accept o since it produces the maximal payoff.

2. If $\mathop { o _ { \simeq } } \in O _ { p } ^ { \prime }$ is true, an agent p should accept o because $O _ { \simeq }$ is one of proposals it makes before.

It is shown that if each participating agent $p { \in } P$ employs their preference ordering $( \preceq _ { p } , O _ { p } )$ to compute concessions and uses the offer acceptability criteria described above to evaluate incoming offers, Pareto optimal [29] result is always found if it does exist in a negotiation space [2].

## 4. The probabilistic negotiation agents

The development of the probabilistic negotiation mechanism for adaptive negotiation agents is driven by the basic intuition that rational negotiators strive for two possibly contradictory objectives [10,19]: (1) maximizing self payoffs, and (2) maximizing the chance of reaching an agreement. The former can be computed according to a negotiator's private utility function as discussed in Section 3, and the latter can be estimated based on Bayesian learning [8]. The proposed adaptive negotiation agents can refer to the negotiation history files to discover the negotiation preferences of their opponents. Moreover, these agents can monitor the current negotiation dialog with their opponents to identify the possible preferential changes of their opponents.

## 4.1. Probabilistic negotiation decision making

Our probabilistic negotiation agents' decision mak ing mechanisms are underpinned by a ranking function; this function produces a ranked list of offers according to the potential of individual offers for maximizing self payoff and the chance of offer acceptance by the opponent. In particular, the preference relation $\preceq _ { p }$ of a probabilistic negotiation agent is a total ordering induced by the product of the agent's private utility function $U _ { p } ^ { o }$ and the probability function Pr(accept|o) which characterizes the probability of acceptance of an offer o by the opponent. In other words, the feasible offers of an agent $p$ are ranked in descending order according to:

$$
\operatorname{Rank} (o) = \left[ U _ {p} ^ {o} (o) \right] ^ {\frac {1}{\alpha}} \times [ \operatorname * {P r} (\text { accept } | o) ] ^ {\frac {1}{(1 - \alpha)}}\tag{1}
$$

where ${ \boldsymbol { \alpha } } \in [ 0 , 1 ]$ is a trade-off factor for maximizing one's own payoff or maximizing the chance of the offer being accepted by the opponent. According to our current implementation, when $\scriptstyle { \alpha = 0 }$ is specified by the human negotiator, the fraction $\textstyle { \frac { 1 } { \alpha } }$ will not be computed and a default value of zero will be returned; this results in instantiating a benevolent agent which only considers the opponent's benefits. On the other hand, if $\mathsf { \alpha } \mathsf { \alpha } \mathsf { \alpha } \mathsf { \alpha } \mathsf { \alpha } \mathsf { \beta } \mathsf { \alpha } \mathsf { \alpha }$ is specified, the fraction $\frac { 1 } { 1 - \alpha }$ will return zero instead of an undefined value; this results in instantiating a strictly self-interest agent. Moreover, a system wide default of 0.5 will be assumed if the α value is not provided by the human negotiator initially. It should be noted that the absolute numerical value of Rank(o) is not important, but the relative rank of an offer o.

A counter-offer with the least amount of concession (in terms of the least decrement of own payoff and the minimal reduction of offer acceptability) is selected from the top of the list $( \preceq _ { p } , \{ O _ { p } - O _ { p } ^ { \prime } \} )$ ranked by an agent $p$ in each negotiation round. Once the counteroffer is determined, it will be added to the set $O _ { p } ^ { \prime } .$ The revised $O _ { p } ^ { \prime }$ forms the basis to evaluate the incoming offers. The probability of acceptance of an offer o can be computed according to Bayes theorem [8]:

$$
\operatorname * {P r} \left(c _ {j} | o\right) = \frac {\operatorname* {P r} \left(o \mid c _ {j}\right) \times \operatorname* {P r} \left(c _ {j}\right)}{\operatorname* {P r} (o)}\tag{2}
$$

where $c _ { j } \in \{ \mathrm { a c c e p t } , \ \mathrm { r e j e c t } \}$ and $j$ is the index of a particular class. If the naive assumption of feature $( \mathrm { i . e . } ,$ negotiation issue) independency is made, the prior probability $\operatorname* { P r } ( o | c _ { j } )$ can be approximated by [23,27]:

$$
\operatorname * {P r} \bigl (o | c _ {j} \bigr) = \prod_ {i = 1} ^ {| A |} P r \bigl (d _ {a _ {i}} | c _ {j} \bigr)\tag{3}
$$

where $d _ { a _ { i } }$ is one of the attribute values of an offer o. By the addition rule of probability theory, $\Pr ( o ) =$ ${ \boldsymbol { \Sigma } } _ { j = 1 } ^ { n } { \mathrm { P r } } ( o | c _ { j } ) \times { \mathrm { P r } } ( c _ { j } )$ is held. Therefore, the probability of acceptance of an offer o by the opponent can be estimated according to:

$$
\begin{array}{l} \operatorname * {P r} (\text { accept } | o) = \left(\operatorname * {P r} (\text { accept }) \times \prod_ {i = 1} ^ {| A |} \operatorname * {P r} (d _ {a _ {i}} | \text { accept })\right) \\ \quad \div \left[ \operatorname * {P r} (\text { accept }) \times \prod_ {i = 1} ^ {| A |} \operatorname * {P r} (d _ {a _ {i}} | \text { accept }) \right. \\ \quad \left. + \operatorname * {P r} (\text { reject }) \times \prod_ {i = 1} ^ {| A |} \operatorname * {P r} (d _ {a _ {i}} | \text { reject }) \right] \end{array}\tag{4}
$$

It should be noted that if only a partial counter-offer (i.e., some attributes are missing in an offer) is evaluated, the corresponding terms such as $\operatorname* { P r } ( d _ { a _ { i } } | \mathrm { a c c e p t } )$ and $\mathrm { P r } ( d _ { a _ { i } } |$ reject) are treated as 1 because these negotiation issues are considered not relevant by an agent. As a result, the probability of offer acceptance is determined by other attribute values. Currently, there are two operating modes of our probabilistic negotiation agents, namely adaptive and nonadaptive. For the non-adaptive mode, the probability negotiation agents estimate the opponents' preferences based on the past negotiation histories only. They operate based on the negotiation mechanism described in Section 3 except that the offer ranking is established according to Eq. (1) instead of based on an agent's own utility function. After a negotiation session begins, the preferences of an agent and its opponents are assumed unchanged.

On the other hand, for the adaptive probabilistic agents, the probability function Pr(accept|o) is revised in each negotiation round based on the most recent negotiation dialog. Therefore, the adaptive probabilistic negotiation agents are sensitive to the opponents' recent preferential changes. After updating the priori probabilities based on the current negotiation dialog, the set of feasible offers $O _ { p }$ for the agen $p { \in } P$ will be re-ranked again according to Eq. (1). As a result, more sensible negotiation decision making can be conducted from time to time according to the most recent preferences of agent $p$ and its opponents. As the time dimension is always an important issue for practical negotiations [21], our probabilistic negotiation agents are extended to take into account the time pressure:

$$
\operatorname{Rank} (o) = \left[ U _ {p} ^ {o} (o) \right] ^ {\frac {1}{\alpha \times \mathrm{TP} (t)}} \times [ \operatorname * {P r} (\text { accept } | o) ] ^ {\frac {1}{(1 - \alpha \times \mathrm{TP} (t))}}\tag{5}
$$

The term TP(t) represents the time pressure function. The basic intuition is that when the negotiation deadline is approaching, an agent is more likely to concede in order to make a deal [14,30]. However, different agents may have different attitudes towards deadlines. An agent may be eager to reach a deal and so it will concede quickly (Conceder agent). On the other hand, an agent may not give ground easily during negotiation (Boulware agent) [28]. Therefore, a time pressure function $\begin{array} { r } { \mathrm { T P } ( t ) = 1 - \bigg ( \frac { t } { t _ { p } ^ { d } } \bigg ) ^ { \frac { 1 } { e _ { p } } } } \end{array}$ is developed to approximate a wide spectrum of agents' concession attitude. Our TP function is similar to the negotiation decision function referred to in the literature [9,11]. The term $t _ { p } ^ { d }$ indicates the deadline for an agent $^ { p , }$ and $e _ { p }$ is used to model the “concession attitude” of the agent $p .$

## 4.2. Mining negotiation knowledge

Data mining refers to the non-trivial process of identifying valid, novel, potentially useful, and ultimately understandable patterns in data [12]. In the context of knowledge discovery for automated negotiations, the novel patterns are the negotiation preferences (i.e., the frequently requested issues and their values). This kind of patterns is ultimately understandable and potentially useful because they can be applied to improve both negotiation effectiveness (e.g., joint payoffs) and negotiation efficiency (e.g., reducing the amount of time to reach agreements). In association rule mining, the measures of rule support and rule confidence are used to evaluate the quality of the association rules extracted from frequent item-sets [1]. In fact, rule support and rule confidence correspond to the joint probability and the conditional probability of the appearance of items (e.g., consumer products) in transactions. Our approach of discovering the preferences of negotiators is also based on computing the priori probabilities of the frequently requested items (negotiation options) appearing in some offers. The prior probabilities such as Pr(accept), Pr (reject), $\Pr ( d _ { a _ { i } }$ |accept), and $\mathrm { P r } ( d _ { a _ { i } } | \mathrm { r e j e c t } )$ can be estimated based on the negotiation histories. Fig. 1 depicts a segment of a negotiation history file.

The basic assumption of our negotiation knowledge discovery method is that each counter-offer from the opponent is considered an acceptable offer (i.e., a positive training example). Moreover, if an agent proposes an offer and it is rejected by the opponent, it is treated as a negative training example. As agents' preferences may change in real-world negotiation situations, the most recently archived negotiation sessions are more useful than the sessions archived long time ago in terms of estimating the opponent's current preferences. Moreover, a negotiation agent will maintain a separate history for the negotiation processes it conducted with each of its partners. A negotiation session refers to a particular negotiation process. The negotiation process ends when an agreement could be reached or all the parties decide to quit. For each negotiation process (session), a negotiation agent will make series of offers (i.e., entries). Based on the above assumptions, the training examples generated from the past negotiation sessions and the current negotiation dialog should be weighted. The weight factor $w _ { i } ^ { S }$ is computed and assigned to a negotiation session i according to a linear function:

$$
w _ {i} ^ {S} = w _ {\max} - \text { step } \times \frac {w _ {\max} - w _ {\min}}{| \text { session } | - 1}\tag{6}
$$

where $w _ { i } ^ { S }$ is the highest weight assigned to a particular negotiation session $i ;$ the terms $w _ { \mathrm { m a x } } { > } 0$ and $w _ { \mathrm { m i n } } > 0$ represent the maximal and the minimal weights assigned to valuate all the negotiation sessions. The term |session| is the total number of archived negotiation sessions including the current negotiation session for knowledge discovery purpose. The term $\mathrm { s t e p } { = } < 0 , 1 , . . . , | \mathrm { s e s s i o n } | - 1 >$ represents the sequence of negotiation sessions. For example, the step value of the most current negotiation session is 0, and the second most current session is 1, so on so forth.

![](/api/attachments/TGVRQUXS/fulltext/images/9b5c46e7cad14d0afb4f84c09b18ce45ded4e4f3e98858b15977b1e51c01ff6e.jpg)  
Fig. 1. A segment of negotiation history.

In addition, the weight of each offer (or counter-offer) within a negotiation session i varies. For instance, a counter-offer proposed by the opponent at the earlier stage is more preferable (for the opponent) than the one proposed at a later stage. Therefore, each entry in a negotiation session i is also weighted in chronological order. The second weight factor $w _ { i j } ^ { \breve { E } }$ for the jth negotiation entry (i.e., an event) in the ith archived negotiation session is computed according to:

$$
w _ {i j} ^ {E} = w _ {i} ^ {S} - (j - 1) \times \frac {w _ {i} ^ {S} - w _ {i + 1} ^ {S}}{| E |}\tag{7}
$$

where E is the total number of entries of an archived negotiation session $i . ~ w _ { i } ^ { S }$ and $\mathbf { w } _ { i + 1 } ^ { S }$ are the highest session weights assigned to the i session and the session immediately preceding it respectively. For the oldest session (i.e., $( i + 1 ) >$ |session|) in a negotiation history file, the value of $\mathbf { w } _ { i + 1 } ^ { S }$ is assumed zero.

Table 1 shows an example of the sample space which consists of 3 past negotiation sessions and 1 current negotiation session. The maximal weigh $w _ { \mathrm { m a x } } { = } 5 0 0$ and the minimal weight $w _ { \mathrm { m i n } } { = } 2 0 0$ are set. The entry depicted at the bottom of Table 1 represents the current negotiation session between an agent and its opponent. The weight of the second most current negotiation session is computed according to Eq. (6), that is $\begin{array} { r } { w _ { 2 } ^ { S } = 5 0 0 - 1 \times \frac { 5 0 0 - 2 0 0 } { 4 - 1 } = 4 0 0 } \end{array}$ . In addition, the weight of the second negotiation entry in this session is computed according to Eq. (7), that is $w _ { 2 2 } ^ { E } = 4 0 0 -$ $( 2 - 1 ) \times \frac { 4 0 0 - 3 0 0 } { 4 } = 3 7 5$ . In fact, the weights can be interpreted as the additional sample points attached to each event (i.e., a training example). According to

A weighted sample space

<table><tr><td>Session</td><td>Offers</td><td>Price $(d_{a_1})$ </td><td>Shipmenttime  $(d_{a_2})$ </td><td>Qty $(d_{a_3})$ </td><td>Opponentaccept  $(c_j)$ </td><td>Weights</td></tr><tr><td rowspan="4">4</td><td> $o_1$ </td><td>5–10</td><td>1–2</td><td>20–30</td><td>N</td><td>200</td></tr><tr><td> $o_2$ </td><td>15–20</td><td>3–4</td><td>50–50</td><td>Y</td><td>175</td></tr><tr><td> $o_3$ </td><td>1–2</td><td>2–2</td><td>10–20</td><td>N</td><td>150</td></tr><tr><td> $o_4$ </td><td>25–30</td><td>5–8</td><td>60–100</td><td>Y</td><td>125</td></tr><tr><td rowspan="4">3</td><td> $o_1$ </td><td>5–10</td><td>1–2</td><td>20–30</td><td>N</td><td>300</td></tr><tr><td> $o_2$ </td><td>15–20</td><td>3–4</td><td>50–50</td><td>Y</td><td>275</td></tr><tr><td> $o_3$ </td><td>1–2</td><td>2–2</td><td>10–20</td><td>N</td><td>250</td></tr><tr><td> $o_4$ </td><td>25–30</td><td>5–8</td><td>60–100</td><td>Y</td><td>225</td></tr><tr><td rowspan="4">2</td><td> $o_1$ </td><td>5–10</td><td>1–2</td><td>20–30</td><td>N</td><td>400</td></tr><tr><td> $o_2$ </td><td>15–20</td><td>3–4</td><td>50–50</td><td>Y</td><td>375</td></tr><tr><td> $o_3$ </td><td>1–2</td><td>2–2</td><td>10–20</td><td>N</td><td>350</td></tr><tr><td> $o_4$ </td><td>25–30</td><td>5–8</td><td>60–100</td><td>Y</td><td>325</td></tr><tr><td>1</td><td> $o_1$ </td><td>5–10</td><td>1–2</td><td>20–30</td><td>N</td><td>500</td></tr></table>

Table 1, there are 3650 sample points in the sample space, and $\begin{array} { r } { \mathrm { P r } ( \mathrm { a c c e p t } ) = \frac { 1 5 0 0 } { 3 6 5 0 } = 0 . 4 1 } \end{array}$ is estimated. Similarly, $\begin{array} { r } { \operatorname* { P r } ( \mathrm { r e j e c t } ) = \frac { 2 1 5 0 } { 3 6 5 0 } = 0 . 5 9 , \operatorname* { P r } ( \mathrm { p r i c e } = 2 5 - 3 0 | \mathrm { a c c e p t } ) = } \end{array}$ $\begin{array} { r } { \frac { 6 7 5 } { 1 5 0 0 } = 0 . 4 5 , \check { \mathrm { P r } } ( \mathrm { q t y } = 5 0 - 5 0 | \mathrm { a c c e p t } ) = \frac { 8 2 5 } { 1 5 0 0 } = 0 . 5 5 } \end{array}$

## 5. The experiments

## 5.1. General procedure

The simulated e-marketplaces were characterized by multi-lateral negotiations among some buyer agents $( B 1 , . . . , B n )$ and some seller agents $( S 1 , . . . , S n )$ . These agents negotiated over some virtual services or products described by five attributes $( \mathrm { i } . { \mathsf { e } } . , \ \left| A \right| = 5 )$ with each attribute domain containing five discrete values $D _ { a _ { i } } { = }$ $\{ 1 , 2 , 3 , 4 , 5 \}$ . For each agent $p ,$ the size of the feasible offer set is: $| O _ { p } | = 5 ^ { 5 } = 3 1 2 5$ . The valuation of an attribute or a discrete attribute value fell in the unit interval of (0,1). For each negotiation case, an agreement zone always existed since the difference between the buyers and the sellers only lay on their valuations against the same set of negotiation issues (e.g., attributes and attribute values). The simulated e-marketplaces were symmetric where the same number of buyers and sellers participated.

At the beginning of every negotiation round, each agent would invoke its own decision making mechanism to generate an offer for that round. The order of deliberation of out-going offers among the agents was randomly chosen by the facilitator agent. At the message exchange phase, each agent sent the offer messages to all the opponents (e.g., S1→B1, S1→B2, S1→ B3, etc. for the seller S1). After the message exchange phase, the facilitator agent randomly selected a sequence of agents such as $< B 2 , B 1 , S 1 , S 2 , . . . , S n >$ for incoming offer evaluation. For instance, with reference to the above sequence, agent B2 would evaluate its incoming offers first, then agent B1 would evaluate its incoming offers, etc. If agreements could be made, an agent always selected the best deal (evaluated according to its private utility function). If there was a tie, an opponent would be randomly selected by an agent. Once an agreement was made between a pair, they would be removed from the e-marketplace immediately by the facilitator agent, and the remaining agents would continue their negotiations until either agreement was made or the negotiation deadline was due. Our e-marketplaces were implemented as Web services [7,18,34] and instantiated on a Server with a Pentium-4 2.2 GHz single processor and 1 GB main memory. To avoid the communication overheads, all the experiments were conducted under our Intranet environment. All the agents were developed using Java SDK 1.5.0.

## 5.2. Evaluation measures

Both the effectiveness (in terms of average joint payoff) and the efficiency (in terms of average number of negotiation rounds) of the negotiation processes were evaluated. We adopt the relative measure of “negotiation rounds” to assess the negotiation time involved in a negotiation process (and indirectly measuring the computational/communication costs) so that it becomes easier to compare our results with others which may be conducted in different computational environments. Moreover, average weighted Euclidean distance [8] was also used to measure how far away the solutions obtained by our probabilistic agents from the Pareto optimum:

$$
\operatorname{AvgDist} = \frac {\sum_ {j = 1} ^ {| \mathrm{PS} |} \sum_ {i = 1} ^ {| \mathrm{PA} |} \operatorname{dist} \left(\overrightarrow {o _ {i}} , \overrightarrow {o _ {j}}\right)}{| \mathrm{PA} | \times | \mathrm{PS} |}\tag{8}
$$

$$
\operatorname{dist} \left(\overrightarrow {o _ {x}}, \overrightarrow {o _ {y}}\right) = \sqrt {\sum_ {i = 1} ^ {| A |} w _ {i} \left(d _ {a _ {i}} ^ {x} - d _ {a _ {i}} ^ {y}\right) ^ {2}}\tag{9}
$$

where $\mathrm { P A } \subseteq P$ is the set of agents reaching an agreement in an e-marketplace, and PS is the set of Pareto optimal solutions. As each agent has its own preference $w _ { i }$ for an attribute $a _ { i } ,$ the average distance is computed among the agents PA by Eq. (8). Since the Pareto optimum set PS may contain more than one optimal solution, the mean distance between the agents' solution and every Pareto optimal solution is computed. The weight factor $w _ { i } { = } U _ { p } ^ { A } ( a _ { i } )$ in Eq. (9) is an agent's valuation for a particular attribute $a _ { i } { \in } A$ . An offer vector $\stackrel { \longrightarrow } { o _ { x } }$ contains an attribute value $d _ { a _ { i } } ^ { x }$ along the ith dimension (issue) in a negotiation space. If an attribute interval instead of a single value is specified for an offer, the mid-point of an attribute interval is first computed.

## 5.3. Experiment 1

Hypothesis 1. The probabilistic negotiation agents empowered by the knowledge discovery mechanisms are more efficient than the Pareto optimal agents which are not equipped with the knowledge discovery mechanisms.

## 5.3.1. The experimental procedures

The first experiment aimed at developing a basic test to see if the proposed negotiation knowledge mining method could improve the negotiation processes. Two buyer agents and two seller agents were involved $( \mathrm { i } . { \mathsf { e } } . , \ | P | = 4 )$ in this experiment. There were six negotiation groups which are characterized by various levels

Table 3  
Table 2  
The utility functions of two agents

<table><tr><td colspan="5">Agent Buyer:  $p_1$ </td></tr><tr><td> $U_{p_1}^{A} (price)=0.3$ </td><td> $U_{p_1}^{A} (qty)=0.3$ </td><td> $U_{p_1}^{A} (size)=0.2$ </td><td> $U_{p_1}^{A} (delivery)=0.1$ </td><td> $U_{p_1}^{A} (warranty)=0.1$ </td></tr><tr><td> $U_{p_1}^{D_{price}}(1)=0.9$ </td><td> $U_{p_1}^{D_{qty}}(1)=0.9$ </td><td> $U_{p_1}^{D_{size}}(1)=0.9$ </td><td> $U_{p_1}^{D_{delivery}}(1)=0.9$ </td><td> $U_{p_1}^{D_{warranty}}(1)=0.9$ </td></tr><tr><td> $U_{p_1}^{D_{price}}(2)=0.8$ </td><td> $U_{p_1}^{D_{qty}}(2)=0.8$ </td><td> $U_{p_1}^{D_{size}}(2)=0.8$ </td><td> $U_{p_1}^{D_{delivery}}(2)=0.8$ </td><td> $U_{p_1}^{D_{warranty}}(2)=0.8$ </td></tr><tr><td> $U_{p_1}^{D_{price}}(3)=0.6$ </td><td> $U_{p_1}^{D_{qty}}(3)=0.6$ </td><td> $U_{p_1}^{D_{size}}(3)=0.6$ </td><td> $U_{p_1}^{D_{delivery}}(3)=0.6$ </td><td> $U_{p_1}^{D_{warranty}}(3)=0.6$ </td></tr><tr><td> $U_{p_1}^{D_{price}}(4)=0.2$ </td><td> $U_{p_1}^{D_{qty}}(4)=0.2$ </td><td> $U_{p_1}^{D_{size}}(4)=0.2$ </td><td> $U_{p_1}^{D_{delivery}}(4)=0.2$ </td><td> $U_{p_1}^{D_{warranty}}(4)=0.2$ </td></tr><tr><td> $U_{p_1}^{D_{price}}(5)=0.1$ </td><td> $U_{p_1}^{D_{qty}}(5)=0.1$ </td><td> $U_{p_1}^{D_{size}}(5)=0.1$ </td><td> $U_{p_1}^{D_{delivery}}(5)=0.1$ </td><td> $U_{p_1}^{D_{warranty}}(5)=0.1$ </td></tr></table>

$$
\text { Agent   Seller: } p _ {2}
$$

$$
U _ {p _ {2}} ^ {A} (\text { price }) = 0. 3
$$

$$
U _ {p _ {2}} ^ {A} (\mathrm{qty}) = 0. 3
$$

$$
U _ {p _ {2}} ^ {D _ {\mathrm{qty}}} (1) = 0. 1
$$

$$
U _ {p _ {2}} ^ {D _ {\text { price }}} (1) = 0. 1
$$

$$
U _ {p _ {2}} ^ {\bar {D} _ {\mathrm{qty}}} (2) = 0. 2
$$

$$
U _ {p _ {2}} ^ {A} (\text { size }) = 0. 2
$$

$$
U _ {p _ {2}} ^ {\bar {D} _ {\text { price }}} (2) = 0. 2
$$

$$
U _ {p _ {2}} ^ {\hat {D} _ {\mathrm{qty}}} (3) = 0. 5
$$

$$
U _ {p _ {2}} ^ {D _ {\text { size }}} (1) = 0. 1
$$

$$
U _ {p _ {2}} ^ {\tilde {D} _ {\text { price }}} (3) = 0. 5
$$

$$
\dot {U} _ {p _ {2}} ^ {\mathcal {D} _ {\mathrm{qty}}} (4) = 0. 8
$$

$$
U _ {p _ {2}} ^ {\tilde {D} _ {\mathrm{qty}}} (5) = 0. 9
$$

$$
U _ {p _ {2}} ^ {\bar {D} _ {\text { size }}} (2) = 0. 2
$$

$$
U _ {p _ {2}} ^ {\tilde {D} _ {\text { price }}} (4) = 0. 8
$$

$$
U _ {p _ {2}} ^ {\tilde {D} _ {\text { size }}} (3) = 0. 5
$$

$$
U _ {p _ {2}} ^ {\tilde {D} _ {\text { price }}} (5) = 0. 9
$$

$$
U _ {p _ {2}} ^ {D _ {\text { size }}} (4) = 0. 8
$$

$$
U _ {p _ {2}} ^ {\tilde {D} _ {\text { size }}} (5) = 0. 9
$$

$$
U _ {p _ {2}} ^ {A} (\text { warranty }) = 0. 1
$$

$$
U _ {p _ {2}} ^ {A} (\text { delivery }) = 0. 1
$$

$$
U _ {p _ {2}} ^ {D _ {\text { delivery }}} (1) = 0. 1
$$

$$
U _ {p _ {2}} ^ {\bar {D} _ {\text { delivery }}} (2) = 0. 2
$$

$$
U _ {p _ {2}} ^ {D _ {\text { warranty }}} (1) = 0. 1
$$

$$
U _ {p _ {2}} ^ {\hat {D} _ {\text { delivery }}} (3) = 0. 5
$$

$$
U _ {p _ {2}} ^ {\bar {D} _ {\text { warranty }}} (2) = 0. 2
$$

$$
U _ {p _ {2}} ^ {\tilde {D} _ {\text { delivery }}} (4) = 0. 8
$$

$$
U _ {p _ {2}} ^ {\tilde {D} _ {\text { delivery }}} (5) = 0. 9
$$

$$
U _ {p _ {2}} ^ {\tilde {D} _ {\text { warranty }}} (3) = 0. 5
$$

$$
U _ {p _ {2}} ^ {\tilde {D} _ {\text { warranty }}} (4) = 0. 8
$$

$$
U _ {p _ {2}} ^ {\tilde {D} _ {\text { warranty }}} (5) = 0. 9
$$

of conflict among the buyers and the sellers. Each group contained ten negotiation cases (i.e., totally $6 \times 1 0 { = } 6 0$ simulated e-marketplaces). For the first negotiation group, buyers and sellers had exactly the same utility functions (i.e., no conflict). Two utility functions are the same if both the valuation of the attributes and the valuation of the corresponding attribute values are the same. Table 2 shows an example of the utility functions for a buyer agent $p _ { 1 }$ and a seller agent $p _ { 2 }$ used in this experiment.

For each succeeding negotiation group, buyers and sellers were characterized by having common weighting from one (small conflict group) to five attributes (highest conflict group) respectively [26]. For these negotiation groups, opposing valuations of the attribute values were created between the buying side and the selling side. In this experiment, no negotiation deadline was imposed in the e-marketplaces. The control group consisted of the Pareto optimal negotiation agents developed according to the negotiation mechanism described in Section 3. These agents could found Pareto optimal solutions when time constraint was not present. After running a simulated e-marketplace, the average joint payoffs and the average negotiation time were recorded.

60% of the entries captured in a negotiation session were used to train the probabilistic agents. We employed a heuristic $w _ { \mathrm { m i n } } \mathrm { > = } | E | _ { \mathrm { M A X } }$ and $w _ { \mathrm { m a x } } 2$ |session $\times w _ { \mathrm { m i n } }$ to derive various combinations of $w _ { \mathrm { m a x } }$ and $w _ { \mathrm { m i n } } ,$ whereas $| E | _ { \mathrm { M A X } }$ is the number of entries of the largest archived session, and |session| is the number of sessions archived in the negotiation history file. Based on the empirical testing for typical negotiation scenarios, we found that the parameters $w _ { \mathrm { m a x } } = 2 0 , 0 0 0 , ~ w _ { \mathrm { m i n } } = 2 0 0 0 , ~ \alpha = 0 . 6$ produced good performance and so they were adopted in this experiment. After a negotiation process began, a probabilistic agent could estimate the posteriori probability Pr(accept|o) for each of its opponent based on the training data. In this experiment, the preference of each agent remained static.

The experimental group comprised of the same number of non-adaptive (i.e., the priori probabilitie about the opponents' preferences were not updated) probabilistic negotiation agents as defined in Section 4. The same set of negotiation cases attempted by the Pareto optimal agents were applied to the probabilistic agents. The negotiation histories of the Pareto optimal agents were made available to the probabilistic agents as the training set. As a result, each probabilistic agent had some knowledge about its opponents before the negotiation process began. In particular, only the first

## 5.3.2. The experimental results

According to the experimental results depicted in Table 3, the Pareto optimal agents achieved an overall average joint utility of 2.31 by using 938.25 negotiation rounds on average. On the other hand, the probabilistic agents achieved an overall average joint utility of 2.23 in 724.75 negotiation rounds on average. There was a $\textstyle { \frac { 2 . 3 1 - 2 . 2 3 } { 2 . 3 1 } } \times 1 0 0 = 3 . 2 \%$ decrement of the overall average joint utility when the probabilistic agents were engaged in the same negotiation situations as the Pareto optimal agents. The overall average distance from the solutions found by the probabilistic agents to the Pareto optimum is 0.16 which is considered a small distance. However, the improvement in terms of reduced average negotiation time of the probabilistic agents was $\begin{array} { r } { \frac { 9 3 \bar { 8 . } 2 5 - 7 2 \bar { 4 } . 7 5 } { 9 3 8 . 2 5 } \times } \end{array}$ $1 0 0 = 2 2 . 8 \%$ . Except the first negotiation group, the probabilistic agents consistently consumed less negotiation time than that of the Pareto optimal agents. For each test case in the first negotiation group, both buyers and sellers had exactly the same utility function. Therefore, an agreement could always be found in the first negotiation round. According to paired one tail t-test, the average negotiation time consumed by probabilistic agents is significantly less than that of the Pareto optimal agents, $t ( 5 ) = - 3 . 4 8 , p < 0 . 0 1$ . Therefore, we conclude that the probabilistic negotiation agents empowered by knowledge discovery mechanisms can identify negotiation solutions faster than the Pareto optimal agents do. Hypothesis 1 is supported according to our experiment.

The impact of Bayesian learning on negotiations

<table><tr><td rowspan="2">Group</td><td colspan="2">Pareto optimal</td><td colspan="3">Probabilistic</td></tr><tr><td>Avg. joint-util.</td><td>Avg. time</td><td>Avg. joint-util.</td><td>Avg. time</td><td>Avg. dist.</td></tr><tr><td>1</td><td>2.74</td><td>1.0</td><td>2.74</td><td>1.0</td><td>0.00</td></tr><tr><td>2</td><td>2.41</td><td>562.0</td><td>2.35</td><td>459.0</td><td>0.15</td></tr><tr><td>3</td><td>2.38</td><td>813.0</td><td>2.31</td><td>622.5</td><td>0.18</td></tr><tr><td>4</td><td>2.29</td><td>1036.0</td><td>2.23</td><td>804.0</td><td>0.17</td></tr><tr><td>5</td><td>2.15</td><td>1483.5</td><td>2.04</td><td>1110.0</td><td>0.22</td></tr><tr><td>6</td><td>1.87</td><td>1734.0</td><td>1.73</td><td>1352.0</td><td>0.26</td></tr><tr><td>Mean</td><td>2.31</td><td>938.25</td><td>2.23</td><td>724.75</td><td>0.16</td></tr></table>

![](/api/attachments/TGVRQUXS/fulltext/images/9b7368f78fe15fbfe1b934234d9333fa5a6b8978190d29ec71efe9e4b7ef81d1.jpg)  
Fig. 2. The impact of α on agent's performance.

## 5.3.3. The impact of the trade-off factor

The impact of the trade-off factor α on the performance of our probabilistic negotiation agents was evaluated. In particular, we would like to observe how the various levels of α affect the quality of the solutions (e.g., average distance from the Pareto optimum) and the time required to search for those solutions. Fig. 2 plots the overall average distance between the solutions found by the probabilistic agents and that produced by the Pareto optimal agents over the six negotiation groups listed in Table 3. It should be noted that the overall average distances plotted in Fig. 2 was scaled up by a factor of one thousand. It is shown that a lower rate of decrement of the overall average distance occurs beyond $\alpha { = } 0 . 6 ,$ , and at the same time a higher rate of increment of the overall average negotiation time (e.g., a larger angle of the slop) occurs. Therefore, we set the trade-off factor to $\alpha { = } 0 . 6$ to strive for a better balance between the quality of the negotiation solutions and the time required to identify those solutions. According to our testing, the average joint payoffs of the agents do not vary with respect to the choices of different $w _ { \mathrm { m a x } }$ and $w _ { \mathrm { m i n } }$ as long as our heuristic of how to estimate these parameters was followed.

## 5.3.4. The impact of the negotiation history

In addition, we examined the impact of the availability of various amount of negotiation history data (i.e., the training set) on the effectiveness of the probabilistic negotiation agents. The negotiation histories were obtained by repeatedly invoking the Pareto optimal agents to attempt the 60 negotiation cases we developed before. Each negotiation history file contained certain number of recorded sessions (i.e., negotiation processes) and each session contained certain number of entries (i.e., offers and counter-offers). In particular, we made the first x percentage of the negotiation entries in a session and the first y percentage of negotiation sessions in a history file available to train the probabilistic agents in each run. After the training process, the probabilistic agents would start to negotiate as before.

Fig. 3 highlights the overall average joint payoff achieved by the probabilistic negotiation agents when various number of entries and sessions are used to train them. It is shown that using more than 60% of the top entries and more than 2 negotiation sessions to train the probabilistic agents cannot improve the maximal average joint utility. In fact, employing a large number of sessions (e.g., 10 sessions) and all the entries (100%) of a negotiation session to train a probabilistic agent may even lead to slightly degraded performance because the final offers do not represent the actual preference of the opponent due to the concession making process. According to our empirical testing, it only took 6.1 s to train an agent (i.e., computing all the priori probabilities) with a negotiation history file containing 10 sessions and each session containing 500 entries on average. This shows a positive sign for the computational efficiency of our negotiation knowledge discovery method.

![](/api/attachments/TGVRQUXS/fulltext/images/b2b5f8f10bfa8a6722a16cac02200f188d4effb1f7c1431662c536a770f3fda1.jpg)  
Fig. 3. The impact of negotiation history on agent's performance.

## 5.3.5. Discussion

As a summary, this experiment confirms that the probabilistic negotiation agents empowered by the knowledge discovery mechanism can make use of the knowledge about their opponents to find agreements faster. With better knowledge about their opponents, the probabilistic negotiation agents can by-pass some of the non-fruitful offers (e.g., chance of acceptance is low) from the set of feasible offers. Even though the probabilistic agents are not fully self-interested, they can achieve near optimal joint payoffs. This represents a win–win negotiation strategy. Such a strategy is desirable for negotiations in B2B e-commerce because it helps maintain long-term relationships among business partners.

## 5.4. Experiment 2

Hypothesis 2. Under time pressure, the probabilistic negotiation agents outperform the Pareto optimal agents in terms of negotiation effectiveness.

## 5.4.1. The experimental procedures

The second experiment tries to evaluate the effectiveness of our probabilistic agents under realistic negotiation condition such as the presence of time pressure. In addition, we would like to test the agents' time adjustment mechanisms defined according to Eq. (5). The same set of negotiation cases employed in experiment one was reused with a negotiation deadline of 500 rounds. This experiment was still based on a control group vs. experimental group design. The first simulation run involved the Pareto optimal agents, and then the non-adaptive probabilistic agents participated in the second simulation run. The third simulation run involved the non-adaptive probabilistic agents with the time adjustment mechanisms Eq. (5) activated. The concession attitude $e _ { p } { = } 0 . 4$ was set for all the time sensitive probabilistic agents. If an agent could not find a deal before the negotiation deadline, its payoff would be zero.

## 5.4.2. The experimental results

The average joint payoffs obtained by different types of agents from six negotiation groups are tabulated in Table 4. The overall average joint payoffs achieved by the Pareto optimal agents, the probabilistic agents, and the time sensitive probabilistic agents are 1.42, 1.58, and

Table 4  
Agent performance under time pressure

<table><tr><td>Group</td><td>Pareto optimal</td><td>Probabilistic Eq. (1)</td><td>Probabilistic Eq. (5)</td></tr><tr><td>1</td><td>2.74</td><td>2.74</td><td>2.74</td></tr><tr><td>2</td><td>1.93</td><td>2.16</td><td>2.31</td></tr><tr><td>3</td><td>1.66</td><td>1.81</td><td>2.02</td></tr><tr><td>4</td><td>1.15</td><td>1.34</td><td>1.95</td></tr><tr><td>5</td><td>0.86</td><td>1.05</td><td>1.88</td></tr><tr><td>6</td><td>0.19</td><td>0.36</td><td>1.63</td></tr><tr><td>Mean</td><td>1.42</td><td>1.58</td><td>2.09</td></tr></table>

2.09 respectively. Except the first negotiation group where agents could always find the best agreements in the first negotiation round, the probabilistic agents consistently performed better than the Pareto optimal agents, and the time sensitive probabilistic agents also performed better than their non time sensitive counterparts. According to paired one tail t-test, the average joint payoffs achieved by probabilistic agents are significantly higher than that of the Pareto optimal agents $( \mathrm { e } . \mathrm { g } . , t ( 5 ) { = } 4 . 7 2 $ $p { < } 0 . 1$ for the non time sensitive probabilistic agents and $t ( 5 ) = 3 . 1 3 , p = 0 . 0 1$ for the time sensitive probabilistic agents). Therefore, we can conclude that our proposed probabilistic agents are more effective than the Pareto optimal agents under time pressure. Hypothesis 2 is supported according to our experiment. The reason for such a difference is that the Pareto optimal agents could not be able to find solutions before the deadline in many cases where negotiation conflicts existed. On the other hand, the probabilistic agents were able to carry out the search faster (e.g., by ignoring some less promising deals). As a result, they were able to seal some deals even though a tough deadline was imposed.

## 5.4.3. The difference of agents' concession behavior

Fig. 4 shows the difference of the concession making processes conducted by a Pareto optimal agent (PO), a probabilistic agent (PR), and a time sensitive probabilistic agent (PRT) respectively. There was a significant performance boost of the probabilistic agents who were empowered by the time adjustment mechanism because these agents were sensitive to the negotiation deadlines. When the deadline was approaching, these agents tended to propose offers which were more likely to be accepted by their opponents (e.g., the α value drop to a very low value). As a consequence, the time sensitive probabilistic agents could find agreements for all the negotiation cases in this experiment. The Y axis in Fig. 4 represents the potential utility value brought to an agent if the corresponding offer is really accepted by the opponent. The comparison is based on one of the negotiation cases from negotiation group 4, and the potential payoffs of the offers are computed from the perspective of the sellers. It is not difficult to find that the concession making behavior of the time sensitive probabilistic agent is different from the other two agents. For instance, there was a bigger drop of the utility values of the agent's offers when the deadline was approaching. In this case, the time sensitive probabilistic agent found an agreement at the 486th negotiation round, whereas the other two agents could not find solution before the deadline of the 500th negotiation rounds. According to paired one tail t-test, the average payoffs of the time sensitive probabilistic agents is significantly higher than that of their non time sensitive counterparts, $t ( 5 ) = 2 . 5 9 , p = 0 . 0 2$ . As can be seen, the proposed time adjustment mechanism for probabilistic agents is effective since it can improve negotiation outcomes in general.

![](/api/attachments/TGVRQUXS/fulltext/images/ad79883c39a496e6776135fd9cfb11fd7002a24240ce21f9d2278b88e47364e9.jpg)  
Fig. 4. Comparative concession behavior among three types of agents.

## 5.4.4. The impact of the agents' concession attitude

We further tested the concession attitude of the time sensitive probabilistic negotiation agents by varying the parameter value $e _ { p } { = } 0 . 1$ (extreme Boulware agents) and $e _ { p } = 1 0$ (Conceder agents) while keeping the other experimental conditions unchanged. For the extreme Boulware agents, the overall average joint payoff achieved is 2.06. For the Conceder agents, the overall average joint payoff achieved is 1.95. The extreme Boulware agents actually failed to reach an agreement in one case with high conflict and so their performance was not as good as the little Boulware agents. On the other hand, the conceder agents conceded too quickly even for the neutral negotiation situations, and therefore their performance was not as good as the little Boulware agents either.

## 5.5. Experiment 3

Hypothesis 3. Under dynamic negotiation environment (e.g., the presence of preferential changes of the negotiators), the adaptive probabilistic negotiation agents can achieve near Pareto optimal negotiation results.

## 5.5.1. The experimental procedures

Under realistic negotiation situations, the preferences of negotiation agents may change over time. This experiment tries to test if the adaptive probabilistic negotiation agents (i.e., their priori probabilities were updated after every negotiation round) can achieve good negotiation outcomes given the preferential changes of themselves and their opponents. At the beginning of the simulations, we employed the same set of negotiation cases used in experiment one. However, the utility functions of the agents would be modified n times after the negotiation processes started. As a result, the utility functions of these agents may not be the same as that examined in experiment one when the negotiation processes completed. The final outcomes in terms of average joint payoffs and the average distances from the Pareto optimum would be recorded. The final negotiation outcomes were computed according to the last modified utility functions of the agents. For instance, after 100 rounds of negotiations, the valuation values of m attributes pertaining to each agent would be randomly selected and modified. After another 100 rounds of negotiations, the agents' valuation functions would be changed again $( \mathrm { i } . { \mathrm { e } } . , \ n { = } 2 )$ . To ensure the required number of preferential changes could be injected into each agent, these agents were forced not to accept a deal until the last change was injected. No negotiation deadline was imposed in this experiment.

To evaluate the adaptiveness of the probabilistic agents, we invoked the adaptive evolutionary negotiation agents [20] under the same conditions (e.g., the same utility function and the same preferential changes of the agents). The evolutionary agents were developed based on a genetic algorithm (a heuristic search approach) and they were not equipped with a knowledge discovery mechanism. The negotiation agents discussed in this paper were empowered by a knowledge discovery mechanism underpinned by Bayesian learning. For this experiment, the parameters $n { = } 2$ and $m = 2$ were used, whereas n and m stand for the frequency of changes and the number of attributes modified respectively. It should be noted that the first negotiation group was a reference group where no preferential changes was injected to the agents. As the preferences of the buyers and the sellers were the same for this negotiation group, an agreement was always reached in the first negotiation round in each case.

## 5.5.2. The experimental results

The comparison between the performance of the evolutionary agents and that of the adaptive probabilistic agents is tabulated in Table 5. By ignoring the reference group (negotiation group 1), the overall average distance of the solutions found by the adaptive probabilistic agents from the Pareto optimum is $\textstyle { \frac { 0 . 1 4 + { \dot { 0 . } } 2 2 + 0 . 1 9 + 0 . 2 3 + 0 . 2 5 } { 5 } } = 0 . 2 1$ , which is close to that (i.e., 0.19) achieved by the non-adaptive probabilistic agents in experiment one. This demonstrates that the average performance of our adaptive probabilistic agents can be maintained even though they operate under a more challenging dynamic negotiation environment.

Table 5  
Performance of adaptive negotiation agents

<table><tr><td rowspan="2">Group</td><td colspan="2">Evolutionary agents</td><td colspan="2">Probabilistic agents</td></tr><tr><td>Avg. joint utility</td><td>Avg. dist.</td><td>Avg. joint utility</td><td>Avg. dist.</td></tr><tr><td>1</td><td>2.74</td><td>0.00</td><td>2.74</td><td>0.00</td></tr><tr><td>2</td><td>2.41</td><td>0.15</td><td>2.42</td><td>0.14</td></tr><tr><td>3</td><td>2.16</td><td>0.21</td><td>2.14</td><td>0.22</td></tr><tr><td>4</td><td>2.12</td><td>0.18</td><td>2.11</td><td>0.19</td></tr><tr><td>5</td><td>1.96</td><td>0.23</td><td>1.96</td><td>0.23</td></tr><tr><td>6</td><td>1.79</td><td>0.25</td><td>1.78</td><td>0.25</td></tr></table>

Based on our simulations, the difference between the average joint payoff of the evolutionary agents and that of the adaptive probabilistic agents is only marginal (by paired one tail t-test, $t ( 5 ) = 1 . 1 7 , p { = } 0 . 1 5 )$ . On the other hand, significant difference of the average weighted Euclidean distances between the evolutionary agents and the probabilistic agents was not found (by paired one tail t-test, $t ( 5 ) = - 0 . 5 4 , \ p = 0 . 3 1 )$ . Therefore, we conclude that the adaptive probabilistic agents are able to adapt to the dynamic negotiation environment, and the performance of these agents is comparable to that achieved by the adaptive evolutionary agents whose effectiveness was tested in a previous study [20]. The adaptive probabilistic agents can produce negotiation outcomes close to the Pareto optimum (e.g., 0.21 point away from the optimum). In general, Hypothesis 3 is supported according to our study.

Fig. 5 plots the overall average distances from the Pareto optimum given the various values of n and m. The overall average distances shown in Fig. 5 excluded the negotiation group 1 since no preferential change was injected to the agents in this group. It is not difficult to observe that the agents can adapt to the preferential changes presented in the negotiation environment. As a result, the overall average distances from the Pareto optimum do not vary much given more frequent changes and greater extent of changes. However, if the changes occurred more frequently, the negotiation efficiency will be affected. Fig. 6 shows that more frequent preferential changes of the agents will generally increase the overall average negotiation time. The reason is that the agents need to take time to learn the opponents' new preferences and adapt to these preferences. Nevertheless, the probabilistic negotiation agents seem robust enough in responding to the frequent changes because the negotiation time is only increased linearly with respect to the number of preferential changes as shown in Fig. 6.

![](/api/attachments/TGVRQUXS/fulltext/images/bcc1d73e7e217ff1d208f913fe19c9c9dda5126588c33a77780412d49ad1c1c4.jpg)  
Fig. 5. The impact of preferential changes on average distance from Pareto optimum.

## 6. Conclusions and future work

Intelligent software agents are promising for supporting business negotiations in e-marketplaces. Since real-world negotiation spaces are complex and dynamic, it is desirable to empower negotiation agents with effective knowledge discovery mechanisms so that these agents can automatically uncover essential negotiation knowledge to improve negotiation outcomes. A novel knowledge discovery method and the corresponding probabilistic negotiation decision making mechanism are developed for adaptive negotiation agents. These agents can continuously learn the preferences of their opponents based on the negotiation dialogs recorded in history files. Our preliminary experiments show that the probabilistic negotiation agents empowered by knowledge discovery mechanisms can make a better balance between maximizing self payoff and improving offer acceptability, and therefore they are more effective and efficient than the Pareto optimal agents under realistic negotiation conditions. Our research opens the door to the development of intelligent software tools to enhance the autonomy and effectiveness of e-marketplaces. As naive Bayesian learning is adopted in our negotiation knowledge discovery framework, dependencies among negotiation issues cannot be taken into account. Future research will explore Bayesian belief network to model the dependency of negotiation issues in complex negotiation spaces. Since our current probabilistic negotiation decision making mechanism only takes into account the opponent agents' concession patterns, an extended decision making mechanism which also considers the opponents' reputation will be examined in the future.

![](/api/attachments/TGVRQUXS/fulltext/images/61925a7d201bc55a52df70d5cb3cf4639c3e3d0458ca6702444e0abe2e422414.jpg)  
Fig. 6. The impact of preferential changes on average negotiation time.

## Acknowledgments

The work reported in this paper has been funded in part by the Australian Research Council (ARC) Discovery grant, grant number DP0556455. This work is also funded in part by the UK's Engineering and Physical Sciences Research Council (EPSRC), grant number EP/E002145/1. The authors would like to thank three anonymous reviewers for their insightful comments and suggestions that help a lot in improving the quality of the paper.

## References

[1] R. Agrawal, R. Srikant, Fast algorithms for mining association rules in large databases, in: Jorge B. Bocca, Matthias Jarke, Carlo Zaniolo (Eds.), VLDB'94, Proceedings of 20th International Conference on Very Large Data Bases, Morgan Kaufmann Publishers, Santiago de Chile, Chile, September 12–15 1994, pp. 487–499.

[2] M. Barbuceanu, W.-K. Lo, Multi-attribute utility theoretic negotiation for electronic commerce, in: Frank Dignum, Ulises Cortés (Eds.), Agent-mediated Electronic Commerce III — Current Issues in Agent Based Electronic Commerce Systems, number 2003 in Lecture Notes in Artificial Intelligence, Springer-Verlag, Heidelberg, Germany, 2001, pp. 15–30.

[3] J. Brzostowski, R. Kowalczyk, On possibilistic case-based reasoning for selecting partners in multi-agent negotiation, in: Geoffrey I. Webb, Xinghuo Yu (Eds.), Proceedings of the 17th Australian Joint Conference on Artificial Intelligence, volume 3339 of Lecture Notes in Computer Science, Springer, Cairns, Australia, December 4–6 2004, pp. 694–705.

[4] J. Brzostowski, R. Kowalczyk, Adaptive negotiation with on-line prediction of opponent behaviour in agent-based negotiations, Proceedings of the 2006 IEEE/WIC International Conference on Intelligent Agent Technology, IEEE Computer Society, 2006, pp. 263–269.

[5] H.H. Bui, S. Venkatesh, D. Kieronska, Learning other agents preferences in multiagent negotiation using the Bayesian classifier, International Journal of Cooperative Information Systems 8 (4) (1999) 275–293.

[6] C.-B. Cheng, C.-C.H. Chan, K.-C. Lin, Intelligent agents for emarketplace: negotiation with issue trade-offs by fuzzy inference systems, Decision Support Systems 42 (2) (2006) 626–638.

[7] D. Chiu, S. Cheung, P. Hung, S. Chiu, A. Chung, Developing enegotiation support with a meta-modeling approach in a web services environment, Decision Support Systems 40 (1) (2005) 51–69.

[8] R. Duda, P. Hart, Pattern Classification and Scene Analysis, John Wiley & Sons, New York, New York, 1973.

[9] P. Faratin, C. Sierra, N.R. Jennings, Negotiation decision functions for autonomous agents, Journal of Robotics and Autonomous Systems 24 (3–4) (1998) 159–182.

[10] P. Faratin, C. Sierra, N.R. Jennings, Using similarity criteria to make issue trade-offs in automated negotiations, Artificial Intelligence 142 (2) (2002) 205–237.

[11] S. Fatima, M. Wooldridge, N.R. Jennings, An agenda based framework for multi-issues negotiation, Artificial Intelligence 152 (1) (2004) 1–45.

[12] U.M. Fayyad, G. Piatetsky-Shapiro, P. Smyth, From data mining to knowledge discovery: an overview, in: U.M. Fayyad, G. Piatetsky-Shapiro, P. Smyth, R. Uthurusamy (Eds.), Advances in Knowledge Discovery and Data Mining, The MIT Press, 1996, pp. 1–34.

[13] E. Gerding, D. van Bragt, H. La Poutré, Multi-issue negotiation processes by evolutionary simulation, validation and social extensions, Computational Economics 22 (2003) 39–63.

[14] F. Harinck, C. De Dreu, Negotiating interests or values and reaching integrative agreements: the importance of time pressure and temporary impasses, European Journal of Social Psychology 34 (5) (2004) 595–611.

[15] M. He, N.R. Jennings, H. Leung, On agent-mediated electronic commerce, IEEE Transactions on Knowledge and Data Engineering 15 (4) (2003) 985–1003.

[16] J. Ji, C. Liu, J. Yan, N. Zhong, Bayesian networks structure learning and its application to personalized recommendation in B2C portal, Proceedings of the 3rd IEEE/WIC International Conference on Web Intelligence, IEEE Computer Society, Beijing, China, September 20–24 2004, pp. 179–183.

[17] R. Keeney, H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Tradeoffs, Cambridge University Press, Cambridge, UK, 1993.

[18] J. Kim, A. Segev, A web services-enabled marketplace architecture for negotiation process management, Decision Support Systems 40 (1) (2005) 71–87.

[19] R. Krovi, A. Graesser, W. Pracht, Agent behaviors in virtual negotiation environments, IEEE Transactions on Systems, Man, and Cybernetics 29 (1) (1999) 15–25.

[20] R.Y.K. Lau, M. Tang, O. Wong, S. Milliner, Y. Chen, An evolutionary learning approach for adaptive negotiation agents, International Journal of Intelligent Systems 21 (1) (2006) 41–72.

[21] A.R. Lomuscio, N.R. Jennings, A classification scheme for negotiation in electronic commerce, Journal of Group Decision and Negotiation 12 (1) (2003) 31–56.

[22] P. Maes, R. Guttman, A. Moukas, Agents that buy and sell, Communications of the ACM 42 (3) (March 1999) 81–91.

[23] T. Mitchell, Machine Learning, McGraw Hill, New York, New York, 1996.

[24] W.W.H. Mok, R.P. Sundarraj, Learning algorithms for single-instance electronic negotiations using the time-dependent behavioral tactic, ACM Transactions on Internet Technology 5 (1) (2005) 195–230.

[25] V. Narayanan, N.R. Jennings, An adaptive bilateral negotiation model for E-commerce settings, Proceedings of the Seventh IEEE International Conference on E-Commerce Technology (CEC'05), 2005, pp. 34–41.

[26] J.R. Oliver, A machine learning approach to automated negotiation and prospects for electronic commerce, Journal of Management Information Systems 13 (3) (1996) 82–112.

[27] M.J. Pazzani, D. Billsus, Learning and revising user profiles: the identification of interesting web sites, Machine Learning 27 (3) (1997) 313–331.

[28] H. Raiffa, The Art and Science of Negotiation, Harvard University Press, 1982.

[29] J. Rosenschein, G. Zlotkin, Task oriented domains, Rules of Encounter: Designing Conventions for Automated Negotiation among Computers, MIT Press, Cambridge, Massachusetts, 1994, pp. 29–52.

[30] A. Roth, J. Murnighan, F. Schoumaker, The deadline effect in bargaining: some experimental evidence, American Economic Review 78 (4) (1988) 806–823.

[31] B. Rubenstein-Montano, R.A. Malaga, A weighted sum genetic algorithm to support multiple-party multi-objective negotiations, IEEE Transactions on Evolutionary Computation 6 (4) (August 2002) 366–377.

[32] A. Rubinstein, Perfect equilibrium in a bargaining model, Econometrica 50 (1) (1982) 97–109.

[33] R. Singh, A.F. Salam, L. Iyer, Agents in e-supply chains, Communications of the ACM 48 (6) (2005) 108–115.

[34] P. Tremblett. Java and UDDI registries. Dr. Dobb's Journal of Software Tools, 27(9):34, 37–40, September 2002.

[35] R. Vetschera, Preference structures and negotiator behavior in electronic negotiations, Decision Support Systems 44 (1) (2007) 135–146.

[36] J. von Neumann, O. Morgenstern, The Theory of Games and Economic Behaviour, Princeton University Press, 1994.

[37] J. Wainer, P.R. Ferreira Jr., E.R. Constantino, Scheduling meetings through multi-agent negotiations, Decision Support Systems 44 (1) (2007) 285–297.

[38] H. Wang, S. Liao, L. Liao, Modeling constraint-based negotiating agents, Decision Support Systems 33 (2) (2002) 201–217.

[39] M. Wooldridge, N. Jennings, Intelligent agents: theory and practice, Knowledge Engineering Review 10 (2) (1995) 115–152.

[40] D. Zeng, K. Sycara, Bayesian learning in negotiation, International Journal of Human-Computer Studies 48 (1) (1998) 125–141.

![](/api/attachments/TGVRQUXS/fulltext/images/f0977f67ab90a14eab2524e6eedf6960918a309f46bac2aa187dc5e85dcfdb48.jpg)  
Dr. Raymond Lau, is the Programme Director of the Bachelor of Business Administration (Honors) in Electronic Commerce degree programme offered by the Department of Information Systems at City University of Hong Kong. He is the author of more than 60 refereed international journals and conference papers. His research work is published in renowned journals such as ACM Transactions on Information Systems, Decision Support Systems, Electronic Commerce Research and

Applications, International Journal of Cooperative Information Systems, Journal of Applied Non-Classical Logic, International Journal of Intelligent Systems, Web Intelligence and Agent Systems, etc. His research interests include Information Retrieval, Text Mining, and Agent-Mediated e-Commerce. He is the technical editor of the Journal of Asian Information Management.

![](/api/attachments/TGVRQUXS/fulltext/images/b33f847b4b2e0d576220e82d453e303d2263279976acd4d00c3c4906e916be81.jpg)

Yuefeng Li is an Associate Professor of Information Technology at the Faculty of Information Technology, Queensland University of Technology, Australia. He received a B.S degree in Mathematics and a M.S. degree in Computer Science from Jilin University, China, a Ph.D. in Computer Science from Deakin University, Australia. His current research interests include ontology and web mining, web intelligence, data mining and knowledge-based systems. He has published

more than 70 refereed papers and three books. His research work is published in renowned journals such as IEEE Transactions on Knowledge and Data Engineering, Knowledge-Based Systems, Applied Artificial Intelligence, International Journal of Intelligent Information and Database Systems, etc. He is an Associate Editor of the International Journal of Pattern Recognition and Artificial Intelligence, and an Associate Editor of the IEEE Intelligent Informatics Bulletin.

Dr. Dawei Song has been a Senior Lecturer at the Knowledge Media Institute, the Open University, United Kingdom, since 2005. He obtained his Ph.D. in information systems from the Chinese University of Hong Kong in 2000. From 2000 to 2005, he worked in the Distributed Systems Technology Centre at the University of Queensland, Australia. His research interests include various theoretical and practical aspects of context-sensitive information retrieval, such as applied logic and language modelling for query expansion and relevance feedback. His research work has been published in renowned journals and conferences, including ACM Transactions on Information Systems, Journal of American Society for Information Science and Technology, ACM SIGIR and ACM CIKM conferences.

![](/api/attachments/TGVRQUXS/fulltext/images/6b5fd59e2cb01de00ba5448b57712964eb4c06d1121f9e14569492fc63959bb4.jpg)

Dr. Ron Chi Wai Kwok, is an Associate Professor in the Department of Information Systems at the City University of Hong Kong. He received his Ph.D. in Information Systems from the City University of Hong Kong. He was an Assistant Professor in the School of management at the State University of New York at Binghamton before joining City University of Hong Kong in 2002. His research interests lie in the areas of technology mediated learning, fuzzy GSS, knowl-

edge integration, and leadership. His prior publications have appeared in Journal of Management Information Systems, Journal of Association for Information Systems, Communications of ACM, Communications of AIS, IEEE Transactions on Systems, Man, and Cybernetics, Decision Support Systems, European Journal of Information Systems, Information & Management, Group Decision and Negotiation, among others.
