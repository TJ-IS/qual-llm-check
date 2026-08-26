---
otero_id: 19880
otero_key: "94ASNZP4"
title: "Authority and consensus in group decision making with fallible individuals"
authors: "Carlos Sáenz-Royo; Vicente Salas-Fumás; Álvaro Lozano-Rojo"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113670"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Authority and consensus in group decision making with fallible individuals

![](/api/attachments/94ASNZP4/fulltext/images/e555191e9b554cd2bedcfb531136ed89a0560fba65ff7839c901670c675bbda7.jpg)

Carlos Saenz-Royo´ <sup>a,\*</sup>, Vicente Salas-Fum´as <sup>b</sup>, Alvaro <sup>´</sup> Lozano-Rojo <sup>c</sup>

<sup>a</sup> Centro Universitario de la Defensa, Spain

<sup>b</sup> University of Zaragoza, Spain

<sup>c</sup> Centro Universitario de la Defensa - IUMA - University of Zaragoza, Spain

## A R T I C L E I N F O

Keywords: Group decision-making Hierarchy Consensus Omission and commission errors Agent-based modeling

## A B S T R A C T

This paper compares the performance, in terms of expected opportunity loss of mistakes, of group decision making with fallible members, under different organization structures. These structures result from combining the decision mechanisms of authority and consensus with the communication networks of star, tree, and full network. Simulation results from Agent Based Modeling show that the authority (consensus) is preferred when the time to reach a group decision matters (not matters), and in organizational environments of high (low) risk and high (low) prospects of growth. Additionally, the results of the paper recommend that organizations that want to migrate from authority to consensus decision making, as defined here, should switch from the lowdensity tree like connecting network, common in hierarchical structures, to a high-density full network.

## 1. Introduction

A well-accepted hypothesis in organization theory is that individual behavior is intended but bounded rational [1], i.e. cognitive limits of the brain lead decision-makers to commit judgment errors. Organizational design may then proceed with the criterion of minimizing the collective negative consequences of individual mistakes [2–5]. This study exam ines the under researched question of how the choice of “organization”, understood as the “patterns of communications and relations among a group of people, including the processes of making and implementing decisions” [1], affects collective performance in groups comprising in dividuals whose bounded rationality led them to make omission and commission errors in the valuation of projects that challenge the status quo. The organization choice determines how individual errors are aggregated into commission and omission errors at the group level that, together, determine the group's performance, measured here by the expected opportunity loss (EOL) from mistakes [6,7].

The physical set up includes a set of nodes joint through communi cation lines, with one or more intended but bounded rational persons occupying each node. Each person-node processes information, either coming from outside, when she detects an innovation opportunity that is potentially adoptable by the organization, or from inside, when a con nected organization member shares information about a project under evaluation. The organization set up includes a communication network, from three possible ones, start, tree and full network, together with a decision-making mechanism, either a hierarchical-formal, or a consensus-informal one. In the hierarchy-formal mechanism there is a node in the network with authority to make a final decision on the project, and operates wither in a centralized (the node with authority is the only one with decision power and the others only communicate the relevant information about the detected project), or decentralized way (all nodes of the network have the power to filter out the evaluated projects that will finally reach for final decision). In the informalconsensus mechanism, after information exchanges, the group con verges to the unanimous support or rejection of the evaluated innova tion project as follows: (i) there is no qualified authority, (ii) the communications among members are undirected, and (iii) the organi zation only implements those projects backed unanimously.

Authority-formal decision making with a tree communication network is the dominant organization structure among business firms Consensus-informal can be considered a challenging-decision making mechanism, with full communication networks progressively replacing tree ones. In the authority mechanism individual members execute what they are ordered to do, without participating in the decision process. With consensus, members implement the decisions that support indi vidually. The implementation of the decisions will then likely be faster and more efficient with consensus than with authority. However, the time for decision-making is longer in consensus than in authority. Much less is known about the comparative performance of authority and consensus in the decision-making process (pre-implementation stage), when group members make judgment errors in the evaluation of inno vation projects that challenge the status quo, as modeled here. The aim of this paper is to provide evidence from simulations about estimated performance, measured by expected opportunity losses of mistakes, of authority and consensus implemented in different communication net works. The results will indicate whether there may be other reasons, beyond the advantages in the decision implementation stage, to prefer consensus over authority in group decision making, as modeled here.

The rest of this paper is organized as follows. Section 2 presents the literature review on group decision-making with fallible individual and highlights the contributions of the paper. Section 3 describes the ele ments of the organizational design problem and the general set up of the collective actions. Section 4 explains the simulation methodology (agent-based modeling) and presents the main results. Section 5 shows comparative static exercises and robustness. Section 6 illustrates the practical relevance of the research. Finally, the conclusions summarize this study and its main results.

## 2. Literature review

Sah and Stiglitz [8,9] first demonstrated the relevance of “architec ture” (e.g., how decision-making units are arranged, who makes which decision, how information is shared) for the performance of economic systems where fallible individuals make decisions and choices with implications for collective performance. They show that, for similar fallibility of individuals, the architecture of polyarchy, where decision units operate independently, accept proportionately more projects that should had been rejected than hierarchy, where the decision-making authority is more concentrated; whereas hierarchies reject proportion ately higher number of good projects. The choice between the two ar chitectures will depend on the priority about which mistakes to avoid.

Our study also quantifies the losses from omission and commission errors, although with the difference that polyarchy and hierarchy as sume that flows in the network are directed while we compare structures with directed (authority) and undirected (consensus) flows. With directed flows the decision units have one chance for deciding about support adoption of a project or not, while in undirected flows they can have several chances to make the decision, and change their mind from one to the next. Furthermore, this study considers the opportunity cost of the decision-making time in each organization structure, and pro poses the EOL as a measure of performance for group decision making, novel in the literature.

This study is also related to the literature on information and deci sion sciences applied to the formation of consensus in groups' decision making, wherein individual members have diversity of opinions, expertise of knowledge, and/or diversity of preferences (see P´erez et al. [10] for a review). The consensus process was modeled using different representations of utility values [11], fuzzy preference relations [12], linguistic preference relations [13], and pairwise comparison matrices [14]. In the paper, process involves feedback through iterative negoti ations and information exchanges that either happen automatically or are externally guided, as in Salas-Fumas, ´ S´aenz-Royo, and Lozano-Rojo [15], with the differences that the fallibility of individuals is represented in a way that allows for heterogeneity among members, and with per formance measured in expected opportunity loses.

Organization theory has also investigated the relationship between organization design and type I and/or type II decision errors in group decision-making, both theoretically [15–19] and in real group decision making situations [20–24]. Our study resembles those of Knudsen and Levinthal [19] and Csaszar [18] where each member of a group of ho mogeneously fallible individuals makes uncorrelated probabilistic de cisions. The difference is that here the fallibility of individuals is expressed in intended rationality terms (errors of judgment are not purely random), as in Salas-Fumas, ´ Saenz-Royo, ´ and Lozano-Rojo [15]; moreover, the proposed EOL as performance measure combines the probability of error and the respective payoffs, discounted to adjust fo the cost of the time in making a decision.

Finally, this study is motivated by the research opportunities offered by the evolution towards what Raab and Kenis [25] call a “society of networks,” spurred by the advances in the information and communi cation technologies [26,27]. The network organization in this study responds to what Van Alstyne [27] called the “network as a computer,” where “firms are modeled as decision processes dependent on managers capabilities, communication paths, utilization rates, and decision errors while minimizing the costs of decision resources” (page 84). The first communication networks were designed with the minimum communi cation lines needed to connect all the nodes with the one that centralized the decision power (tree network), in response to the high communi cation costs. In these tree-like networks the decision-making mechanism consisted on all organization members communicating the disperse in formation to the authority node for a centralized decision, and the au thority node communicating the decision to the rest of the group for proper execution.

We explore the performance of group decision making in full net works where information exchanges and mutual adaptation can create a spontaneous consensus on change among all nodes-members. The combination of full network and consensus creates an environment of informal organization, where shocks (in the form of new ideas, oppor tunities, values, or social norms) generate opportunities to change and, somehow randomly owing to the fallibility of the members, the change may ultimately get materialized or not.

## 3. Proposed model

The general background is an organization where individuals occupy nodes joint by communication lines. The elements for the analysis include the fallible individuals, the communication network, the group decision making mechanism and the collective outcomes.

## 3.1. Intended but bounded rational individuals

The capacity to process information and the complexity of the in formation processed by individual that decides supporting the adoption of a project with value V when the economic value of the status quo is $V _ { 0 }$ or not are combined in a probability function of supporting adoption, as follows<sup>1</sup>:

$$
p (V) = \frac {1}{1 + e ^ {- \beta \left(\frac {V - V _ {0}}{V _ {0}}\right)}}\tag{1}
$$

The complement, $1 - p ( V )$ , is the probability that the individual will reject the new project. The difference between the value of the new project and the value in the status quo $V - V _ { 0 }$ represents the quantity of information processed, in an inverse way. The complexity of the choice diminishes as the quantity of information processed decreases. Param eter $\beta ,$ generally non-negative, is a measure of the information pro cessing skills of the individual. Its value increases with the general skill of the person and with the specific knowledge and expertise that she has about the tasks performed in the job position. A higher value of $\dot { \beta }$ in creases or decreases the probability of the project being accepted when the net payoff is positive and negative, respectively. An unbounded rational individual would only support projects with $V > V _ { 0 } ,$ and reject the rest. Therefore, when $V < V _ { 0 } ,$ p(V) is the probability of committing the mistake of accepting a project that with unbounded rationality would be rejected (commission or type II error); then, $1 - p ( V )$ is the probability of committing the mistake of rejecting a project with $V > V _ { 0 }$ (omission or type I error), see Fig. 1.

## 3.1.1. Communication networks

There are three possible communication networks considered: star, tree, and full network, each represented in Fig. 2 with number of nodes N $= 1 3 .$

## 3.1.2. Star tree full network

Each node of the network is a decision unit that accepts or rejects certain projects generated in the node with the probability (1). The or ganization structure determines how the information flows through the network and how the decision of the node is processed.<sup>2</sup>

## 3.2. Group decision-making and organization structures

The combination of a decision mechanism (authority and consensus) and communication network is termed as organization structure, s. Furthermore, $p ( V | s )$ represents the probability that the group with structure s will adopt a project of value V

## 3.2.1. Authority

In the authority mechanism, one node in the network has the power to make the decision whether to adopt the project or not and terminate decision process. In centralized authority, the node with the decision power is directly connected to all other nodes in the organization (star network). If the new project randomly emerges in the node with au thority, the project is accepted or rejected with the probability function (1) and the authority decisions becomes the group decision. If the new project randomly appears in any other node, the information is communicated without cost to the node with authority for the final decision. Hence for s = centralized authority, $p ( V | s ) = p ( V )$

Authority can be decentralized in two ways: hierarchy and polyarchy; Fig. 3. In decentralized hierarchy, the network has one node with the power to adopt the project for the group or not (authority); all the other nodes have power only to reject adoption. In decentralized polyarchy, each node has power only to accept. If the node rejects the project, it communicates the decision to its neighbor node and the process con tinues until the node with authority who makes the final decision.

In decentralized hierarchy, adoption of the project by the group re quires that all people that intervene in the decision, including the node with authority, accept the project. For the group rejection of the project, it is sufficient that one node rejects the project. In decentralized poly archy, for group adoption it is sufficient that one node accepts the project; for group rejection, it is necessary that all nodes reject the project.

In decentralized hierarchy and polyarchy, the probability that the group accepts or rejects the project of value V will be a closed function of $p ( V ) .$ . Consider, for example, the decentralized hierarchy in star network with $N = 1 3$ in Fig. 2. If the new project can appear with equal proba bility in all nodes of the network, then 12 out of 13 projects would appear in a periphery node and for s = decentralized hierarchy and star,

$$
p (V s) = \frac {1 2}{1 3} p (V) ^ {2} + \frac {1}{1 3} p (V)
$$

In the tree network with a span of control equal to three of Fig. 2, the probability of group adoption is (for s = decentralized hierarchy and tree),

$$
p (V s) = \frac {1}{1 3} p (V) + \frac {3}{1 3} p (V) ^ {2} + \frac {9}{1 3} p (V) ^ {3}.
$$

## 3.2.2. Consensus

The consensus mechanism is a non-directed process, wherein any node of the network (star, tree, or full network) can interact with any of the nodes it is directly connected to. A project of value V reaches a randomly chosen node that either supports or rejects the project with probability in (1). If the choice is support then it chooses randomly one neighbor node and communicates the information on the project; the outcome of the interaction between the two nodes can be that both support or reject the project, with probability function (1). If the deci sion is rejection the process ends and the group decision is rejection. If the decision is to accept the project, then two nodes that interact with a randomly selected neighbor. The process continues as long as there is one node that supports the project. Technically, the process can be described as an absorbing Markov chain with two absorbing states: all the nodes in the network unanimously accept or reject the project. The probability that structure s adopts the project with value $V , p ( V | s ) ;$ , with s = consensus star, consensus tree, and consensus full network is calcu lated through simulation.

## 3.3. Time until the group decision is made

The time required for the group decision will be measured by the total number of iterations between pairs of nodes in the process towards the collective acceptance. The random variable $\widetilde { T } _ { V | s }$ represents the un certain time, in number of iterations between pairs of nodes, till the group accepts the project, for organization structure s and a project of value V. The expected value of this random variable will be denoted by $T _ { V | s } .$

In the centralized authority mechanism with one node with full au thority the expected decision time is $T _ { V | s } = 1$ by assumption. With decentralized hierarchy in star, the number of interactions necessary for adoption is maximum two (the agent-node where the project appears decides whether to accept or reject; if the project is accepted then the node interacts with the full authority node for the final decision). With $N ~ = ~ 1 3$ , the expected time is $\begin{array} { r } { T _ { V | s } = 1 { \cdot } \frac { 1 } { 1 3 } + 2 { \cdot } \frac { 1 2 } { 1 3 } = \frac { 2 5 } { 1 3 } . } \end{array}$ . For the tree network, $\begin{array} { r } { T _ { V | s } = 1 { \cdot } { \frac { 1 } { 1 3 } } + 2 { \cdot } { \frac { 3 } { 1 3 } } + 3 { \cdot } { \frac { 9 } { 1 3 } } = { \frac { 3 4 } { 1 3 } } . } \end{array}$

In the consensus mechanism, $T _ { V | s }$ is calculated by counting the average number of iterations in the simulation process to reach a group adoption decision in each communication network: star, tree, and full network.

## 3.4. Performance measure: expected opportunity loss (EOL)

The performance of organization structures will be evaluated by the expected opportunity loss, EOL, from group erroneous decisions, used in statistics and decision theory [34–36].

In the simulation, the economic value V of a project that appears in a node of the network is a realization of a random variable V <sup>̃</sup> with known distribution. Therefore, the ex ante expected opportunity loss $E O L \Big ( \widetilde { V } \Big )$ is a random variable whose distribution depends on both, the distribution of $\widetilde { V }$ and the probability of adoption of a particular project. The calculation of the distribution of $E O L \Big ( \widetilde { V } \Big )$ requires first estimate $E O L ( V )$ for values of the project above, below, or equal to the value of the status quo:

![](/api/attachments/94ASNZP4/fulltext/images/9d6a799a60c930e42cc99f4c3a11cb4173321d1c8676bab0e68cdc1af2b6728f.jpg)  
Fig. 1. Probability of accepting (1) and rejecting a project of value V: $\beta = 1$ and $V _ { 0 } = 1$

![](/api/attachments/94ASNZP4/fulltext/images/0ad19b94797f7be91629d608127cd7b4b0d053671b278a0e5372d16f517c9c68.jpg)  
Fig. 2. Communication networks: $N = 1 3 .$

$$
\begin{array}{r l} E O L (V | V > V _ {0}) & = V - (p (V | s) V + (1 - p (V | s)) V _ {0}) = \\ & = (V - V _ {0}) (1 - p (V | s)) \end{array}\tag{2}
$$

$$
E O L (V | V <   V _ {0}) = (V _ {0} - V) p (V | s)\tag{3}
$$

EOL $( V | V = V _ { 0 } ) = 0 .$

When time matters, the payoffs of the organization structure are expressed in present value terms calculated with a positive discounting interest rate, r. During the time spent in arriving at the decision, the group continues to operate in the status quo and earns a payoff $V _ { 0 } .$ . With discounting, (2) and (3) change to:

$$
\begin{array}{r l} E O L (V | V > V _ {0}) & = V - \left(p (V | s) V e ^ {- r T _ {V | s}} + (1 - p (V | s)) V _ {0}\right) = \\ & = (V - V _ {0}) \left(1 - p (V | s) \frac {V e ^ {- r T _ {V | s}} - V _ {0}}{V - V _ {0}}\right) \end{array}\tag{4}
$$

$$
E O L (V | V <   V _ {0}) = p (V | s) \left(V _ {0} - V e ^ {- r T _ {V | s}}\right)\tag{5}
$$

The EOL of a project with $V > V _ { 0 }$ increases with the time spent in reaching a collective decision because more time passes before the group collects the benefits of a more profitable project (status quo). For the projects with $V < V _ { 0 }$ the EOL decreases with the time of adoption because the commission error is delayed.

## 3.5. Asymmetry between costs of omission and commission errors

In economically relevant situations, commission errors tend to have graver consequences than omission errors [18,37,38]. For example, if a firm commits a mistake and adopts a project that results in significant losses, its reputation will be negatively affected, and it could even close down. If the firm commits an omission mistake of not investing in a project that would eventually turn profitable, the loss is in the form of opportunity loss, which is not observable by third parties; therefore, it has no effect on the firm's reputation. Eq. (5) can be modified with a penalty g of commission errors as follows.

$$
\begin{array}{c} E O L (V | V <   V _ {0}) = \\ = (V _ {0} - V) (1 + g) p (V s) \frac {V _ {0} - V e ^ {- r T _ {s}}}{V _ {0} - V}. \end{array}
$$

## 3.6. Expected payoff from the distribution of projects

By Assumption, V is a uniform distributed with lower and upper bounds $V _ { m }$ and $V _ { M } .$ The mean value of the evaluated projects is $\begin{array} { r } { \overline { { V } } = \frac { V _ { m } + V _ { M } } { 2 } } \end{array}$ and the difference $V _ { M } - \mathrm { ~ } V _ { m }$ is a proxy of the level of risk. With unbounded rationality and no mistakes, the group will reject all the projects with value V less than or equal to value $V _ { 0 } ,$ and will adopt all the projects with value V greater than $V _ { 0 } .$ . When $V _ { m } < V _ { 0 } < V _ { M } ,$ the expected payoff for the group decision-making under unbounded rationality is given by:

$$
\left(\frac {V _ {0} - V _ {m}}{V _ {M} - V _ {m}}\right) V _ {0} + \left(\frac {V _ {M} - V _ {0}}{V _ {M} - V _ {m}}\right) \left(\frac {V _ {0} + V _ {M}}{2}\right)\tag{6}
$$

In general, the cumulative distribution function of $E O L \Big ( \widetilde { V } \Big )$ is written as:

$$
\begin{array}{l} \mathbf {P} \left[ E O L (\widetilde {V}) \leq \ell \right] = \int_ {V _ {0}} ^ {V _ {0} + \ell} (1 - p (V s)) f _ {\widetilde {V}} (V) d V \\ \quad + \int_ {V _ {0} - \ell} ^ {V _ {0}} p (V s) f _ {\widetilde {V}} (V) d V + \\ \quad + \int_ {- \infty} ^ {V _ {0}} (1 - p (V s)) f _ {\widetilde {V}} (V) d V + \int_ {V _ {0}} ^ {+ \infty} p (V s) f _ {\widetilde {V}} (V) d V \end{array}
$$

where $f _ { \widetilde { v } }$ denotes the probability density function of ${ \widetilde { V } } .$ The first sum mand is related to the loss by omission error, whereas the second one to that by commission error. The last two summands are the probability of no error (i.e., electing the right option). Rearranging:

$$
\begin{array}{c} \mathbf {P} \Big [ E O L \Big (\widetilde {\mathrm{V}} \Big) \leq \ell \Big ] = \mathbf {P} \Big [ \widetilde {V} \leq V _ {0} + \ell \Big ] + \int_ {V _ {0} + \ell} ^ {+ \infty} p (V s) f _ {\widetilde {V}} (V) d V - \\ - \int_ {- \infty} ^ {\mathrm{V} _ {0} - \ell} p (V s) f _ {\widetilde {V}} (V) d V \end{array}\tag{7}
$$

In the particular case of $\ell = 0 ,$

$$
\begin{array}{c} \mathbf {P} \Big [ E O L \Big (\widetilde {V} \Big) \leq 0 \Big ] = \mathbf {P} \Big [ E O L \Big (\widetilde {V} \Big) = 0 \Big ] = \\ = \int_ {- \infty} ^ {V _ {0}} (1 - p (V s)) f _ {\widetilde {V}} (V) d V + \int_ {V _ {0}} ^ {+ \infty} p (V s) f _ {\widetilde {V}} (V) d V. \end{array}
$$

![](/api/attachments/94ASNZP4/fulltext/images/cdb6c6464e7dfbebe06fc3cca0ee431d84665bb47013d7bcbb016a620980e08d.jpg)  
Fig. 3. Decentralized hierarchy and polyarchy.

EOL cannot be negative because it is calculated from the difference between the value under the right decision and the value under the wrong decision. Although EOL(V) is a continuous function on the real parameter $V , E O L { \big ( } { \widetilde { V } } { \big ) }$ is neither a continuous nor a discrete random variable since $\mathbf { P } \Big [ E O L \Big ( \widetilde { V } \Big ) = 0 \Big ] > 0 .$ Therefore, the reasonable confi dence interval for those distributions is of the form, $[ 0 , a ) ,$ , where $\mathbf { P } \Big [ E O L \Big ( \widetilde { V } \Big ) \le a \Big ] = \theta ,$ and θ is the selected confidence level (Fig. 4). Given the probability distribution of the random variable, $E O L \Big ( \widetilde { V } \Big )$ , the expected value of the random variable is.

$$
E _ {\widetilde {V}} = \mathbf {E} \left[ E O L (\widetilde {V}) \right] = \int_ {- \infty} ^ {\infty} E O L (V) f _ {\widetilde {V}} (V) d V\tag{8}
$$

## 4. Computation of EOLs for different organization structures

Computation of (8) requires, the probability that the group adopts projects of value $V ,$ and the time spend in making the decision, for each organization structure. For the authority mechanism $p ( V | s )$ and $T _ { V | s }$ have closed forms. For consensus, $p ( V | s )$ and $T _ { V | s }$ are calculated using Monte Carlo simulation as in Agent Based Modeling $[ \ [ 1 5 , 3 9 - 4 2 ]$ . For a fix value of $V ,$ we randomly choose (with probability $\textstyle { \frac { 1 } { N } } )$ a node of the network where the described process starts. The simulation ends with adoption or rejection and the outcome is stored, together with the number of iterations needed to reach it. The process is repeated 200,000 to compute the proportion of adoptions and the average number of it erations needed for the final decision. The process is repeated for a sample of values of V so its range is adequate covered (for more detail see Salas-Fumas, ´ Saenz-Royo, ´ and Lozano-Rojo [15]).

The base case for the simulation considers: $N = 1 3$ nodes, $\widetilde { V }$ uni formly distributed between $V _ { m } = - \ 8$ and $V _ { M } = 1 0 _ { : }$ , a status quo value $V _ { 0 }$ $^ { \textrm { \scriptsize = 1 } }$ , and $\beta = 1$ . Since the decentralized hierarchy and the decentralized polyarchy give opposite but symmetric results (ignoring the time effects) to save space we only report the results of decentralized hierarchy. With consensus the probability of adopting or rejecting a project of economic value V is the same in all communication networks (Markov transition matrix with two absorbing values) but the time needed to reach a consensus is different across networks and the EOL of consensus will vary with the type of network.

## 4.1. Probability distribution of commission and omission errors

Fig. 4 shows the estimated probabilities of group's commission and omission errors in the range of V<sup>̃</sup>.Recall that with consensus the prob ability of mistakes is the same in all the networks. The discontinuity in $V / V _ { 0 } = 1$ occurs since when $V = V _ { 0 }$ there are no costs from mistakes. In general, left and right limits in the value of probability of making a mistake around $V / V _ { 0 } = 1$ would be different, but for centralized au thority where the probabilities of commission and omission errors are symmetric both converging to $\textstyle { \frac { 1 } { 2 } }$ when $V / V _ { 0 } = 1$

Relatively to the centralized authority, the decentralized hierarchy lowers the probability of commission errors while increasing that of omission errors, consistent with the result of Sah and Stiglitz [8]. The consensus mechanism has lower and higher probability of commission and omission errors, respectively, especially for values of $V / V _ { 0 }$ marginally above 1.

For values of V higher than $V _ { 0 } ,$ the probability of omission errors decreases with V in all organization structures but faster under consensus than under authority. Consensus initially has high probability of omission errors, but the probability decreases rapidly as V increase. Subsequently, when $V / V _ { 0 } > 1 . 2 6 \ ( 1 . 4 7 )$ , the probability of omission errors with consensus is lower than the one in the decentralized hierarchy in star (tree) networks. The probability of omission errors in consensus and in the centralized authority converge for high $V / V _ { 0 } ,$

## 4.2. Time until the group decides adoption

The mean time needed to reach an adoption decision by the group is shown in Fig. 5. This time is relatively small when $V < V _ { 0 }$ for all orga nization structures. The explanation of this result is that the only orga nization structure that adopts a significant number of projects when $V <$ $V _ { 0 }$ is the central authority (zero iterations). The rest of organization structures practically reject all the projects with $V < V _ { 0 } .$

For $V > 0 ,$ the time to group adoption decision is considerably small for all variations of the authority mechanism, but relatively high in the case of consensus, especially for the values of V relatively close to $V _ { 0 } .$ With consensus, the network with the shortest time to adoption is the full network, followed by the tree and the star; higher density of the connecting lines in the network shortens the expected adoption time.

## 4.3. Calculation of EOL for a project of value V, EOL(V)

The performance measure EOL, Eq. (8), weights the losses of both commission and omission errors. The results of the calculation of EOL(V) from ABM simulations are presented in Fig. 6 for $r = 0$ and in Fig. 7 for r $> 0 .$

Function EOL(V) is concave for $V < V _ { 0 }$ and $V > V _ { 0 } ,$ whereas its value is 0 for $V = V _ { 0 } .$ . It has an interior maximum for a value of V in the ranges between $V _ { m }$ and $V _ { 0 }$ and $V _ { 0 }$ and $V _ { M } .$ . Different values of V affect the EOL with two opposite effects: when the difference between V and $V _ { 0 }$ increases (decreases) in absolute value, the probability of a wrong decision by the group decreases (increases); however, simultaneously, as the difference in the values of the projects increases (decreases), the op portunity loss from the wrong decision increases (decreases). In the maximum EOL, the two marginal effects are equal in absolute value.

From $\mathrm { F i g . } ~ 6 , ~ E O L ( V )$ for centralized authority commission and omission errors are symmetric around $V _ { 0 } .$ In the other organization structures EOL(V) is asymmetric, lower when $V ~ < ~ V _ { 0 }$ (losses from commission errors), and higher when $V > V _ { 0 }$ (losses from omission er rors). The EOL(V) of consensus in full network is practically 0 for the values of $V < V _ { 0 } ,$ and is always lower than the EOL of the other orga nization structures. The $E O L ( V )$ from omission errors (for values of $V >$ $V _ { 0 } )$ are lower with the centralized authority than in the rest; for suffi ciently high values of V the EOLs with the consensus and authority mechanisms are practically the same.

When $r > 0$ the comparative results are different, Fig. 7. With $\pmb { r } = 0 . 3 ,$ EOL(V) is always greater (lower) than or equal to that when $r = 0$ for all $V > V _ { 0 } ( V < V _ { 0 } )$ . The differences are higher with consensus than with authority because in consensus the group spends more time to reach a decision. When $V < V _ { 0 } ,$ , the EOLs of commission errors are practically null with consensus and positive with authority. Decentralized authority reduces the EOL compared to that of centralized authority in the star and tree structures. When $V > V _ { 0 } ,$ decentralized hierarchy increases the EOL of the omission errors compared to that with centralized authority, but for higher values of V the differences disappear. The penalty in terms of the higher EOL of consensus in full network compared to that with centralized authority is practically constant for all V.

For the values of $V < V _ { 0 } ,$ and of $V > V _ { 0 } ,$ the EOL(V) functions are concave with an interior maximum in all the organization structures, similar to what happen when $r = 0 _ { \mathrm { { i } } }$ , Fig. 6. With consensus, when $V > V _ { 0 }$ the EOL functions have a maximum and a minimum in all networks. This means that when time counts there is a value of V beyond which the marginal increase in EOL from the opportunity cost of the wrong decision dominates the marginal increase in EOL from the lower prob ability of the error. The lower EOL of consensus in full networks is explained by the fact the time to reach consensus is lower in full net works than in the other communication structures.

![](/api/attachments/94ASNZP4/fulltext/images/f8e31fede8b252c3836ac688aec56504b081996401faa294261986bfebed1465.jpg)  
Fig. 4. Simulated probability of commission $( V < V _ { 0 } )$ and omission $( V > V _ { 0 } )$ errors for different organization structures $( N = 1 3 , r = 0 ,$ and range of V: − 8 to 10).

![](/api/attachments/94ASNZP4/fulltext/images/b012d99ef918375c900d3e7fe51de26fc99df53594b717f4a608fcfc78827341.jpg)  
Fig. 5. Expected number of time periods for group acceptance of the project of value V (N = 13 and range of V: − 8 to 10).

![](/api/attachments/94ASNZP4/fulltext/images/beaee68317da8c9f5531d251b023fee8ef0d2841c339b9f0e7a1eec8eb4edcf3.jpg)  
Fig. 6. The EOL(V) when interest rate is 0 $( r = 0 ) .$

![](/api/attachments/94ASNZP4/fulltext/images/46de4e3a796e49a1628c1f7dabcea9accec89175e1b33be7eaa8a86a9b2790e7.jpg)  
Fig. 7. EOL(V) with interest rate $r = 0 . 3 \%$

## 4.4. Calculation of $\mathrm { E } _ { \widetilde { \mathrm { v } } }$

In the simulation, the values of V are realizations of a random vari able uniformly distributed on the interval [− 8, 10]. The Fig. 8 shows the estimated EOL, $E _ { \widetilde { v } } ,$ from (8) for the uniformly distributed random var iable $\widetilde { V }$ and interest rates between 0 and 1%. In the calculation of $E _ { \widetilde { v } }$ the values of EOL for $V < V _ { 0 }$ and $V > V _ { 0 }$ are added and the sum is divided by the probability from the uniform distribution, $( V _ { M } - \ V _ { m } ) ^ { - 1 }$ , which is equal to <sup>1</sup> in this case.

The $E _ { \widetilde { v } }$ functions increase with the interest rate because the penalties from the time spent in the decision-making also increase; the function is linear because the range of interest values is relatively small. The slope of the loss function is higher in consensus than in authority because of higher time to reach a decision in the former than in the latter. In fact, in the structures with centralized authority $E _ { _ V }$ is practically flat with the interest rate because it requires only one period to reach the decision. The $E _ { _ V }$ with the centralized authority dominates that of the decentral ized hierarchy for all the interest rates. Furthermore, the $E _ { \widetilde { v } }$ of consensus in full network dominates that of consensus in star and tree structures. The choice of the organization structures is then reduced to the choice between the centralized authority and consensus in full network. Under the criterion of $E _ { \widetilde { v } }$ from the distribution of $\widetilde { V } ,$ the consensus mechanism would be preferred for relatively low values of interest rates, i.e., $r <$ 0.3%, whereas centralized authority would be preferred for interest rates higher than 0.3%. “Impatience” is then determinant for the choice of the structure.

## 5. Comparative static analysis

We now examine the sensitivity of $E _ { _ V }$ under different organization structures to the moments (expected value and dispersion) of the dis tribution of $\widetilde { V } ,$ and interest rate; Table 1.

With $r = 0 ,$ the higher $E _ { _ V }$ occur with lower values of dispersion, $\mathrm { i . e . , }$ [0,2]: as dispersion increases, the $E _ { \widetilde { v } }$ decreases. Since the mean of $\widetilde { V }$ is 1 (equal to $V _ { 0 } = 1 )$ lower variance implies that most values of the new projects concentrate around the value of the status quo where the probability of mistakes is higher. When the dispersion of $\widetilde { V }$ increases there will be values of V higher and lower than $V _ { 0 } = 1$ with low prob ability of mistakes but with high losses resulting from the mistakes. From Table 1, as the variance of the distribution of projects increases, the reduction in the contribution to lower the $E _ { \widetilde { v } }$ from a reduction in $p ( V$ ∣ s) more than compensates for the increase in the contribution from a higher $\vert V - V _ { 0 } \vert$

The $E _ { \widetilde { v } }$ with the consensus is the same in all communication struc tures because when $r = 0$ the time to reach a decision does not matter. Consensus has lower expected losses than authority, and the relative differences increase with the dispersion of the random variable. The opportunity losses from the commission errors while moving from au thority to consensus, more than compensates for the increase in the opportunity losses from committing more omission errors with consensus than with authority, and the difference increases with the dispersion of the random variable.

With authority, $E _ { \widetilde { v } }$ is higher for the decentralized hierarchy in tree structure. Centralized authority and decentralized hierarchy in star structures provide the same $E _ { \widetilde { v } }$ that is independent of the dispersion of the value of the random variable ${ \widetilde { V } } .$ In a tree network the losses from commission (omission) errors are higher (lower) than those in a star; however, the total expected loss is lower in a star than in a tree. This indicates that the lower losses from commission errors do not compen sate the higher ones from omission errors. Compared to the structures with centralized authority, the decentralized hierarchy in star reduces the commission errors but increases the omission ones; however, these differences compensate.

When the time matters, $r > 0 ,$ the pattern of results from the comparative static analysis is less clear. For example, the expected loss monotony decreases with dispersion of the random variable only in the centralized authority. Now, the $E _ { \widetilde { v } }$ with consensus increases, whereas that with centralized authority and that of decentralized hierarchy with star practically do not change. This is the consequence of the higher time required to reach a consensus decision. With a moderate interest rate r $= 0 . 5 \%$ and a small variance of the random variable, the $E _ { \widetilde { v } }$ with consensus is still lower than the $E _ { \widetilde { v } }$ with centralized authority. When the interest rate is high, i.e., $r = 1 \% ,$ the lower $E _ { \widetilde { v } }$ of consensus in full network compared to that with centralized authority holds only for the random variables with small variance. The advantage, in terms of lower $E _ { \widetilde { v } } .$ , of centralized authority over that with consensus as the interest rate goes up is higher for high than for low dispersion of the random variable.

In Table $^ { 2 , }$ the comparative static analysis is extended to scenarios of moderate positive interest rate and distributions of the random variable V<sup>̃</sup> with different mean and different dispersion. The first part of the Table presents the estimated $E _ { \widetilde { v } }$ when the expected value of $\widetilde { V }$ is $^ { 2 , }$ and when is 0. When the distribution of economic values of the projects is centered above, $E \Big ( \widetilde V \Big ) = 2 ,$ the status ${ \bf q u o , }$ centralized authority pro vides lower $E _ { \widetilde { v } }$ than the consensus in full network, for all the dispersions of the $\widetilde { V }$ variable considered. On the contrary, when the distribution is centered below, $E \Big ( \widetilde V \Big ) = 0 ,$ , consensus in the full network provides the lowest $E _ { \widetilde { v } } .$ . When the distribution of the economic values shifts upwards the higher number of omission errors with consensus compared to the omission errors with centralized authority, penalizes the former organization structure with respect to the latter. On the contrary, when the shift is downwards, then the lower number of commission errors with consensus make this organizational solution preferred to centralized authority. One remarkable result seen in Table 2 is that with high dispersion of the random variable value, the $E _ { \widetilde { v } }$ with authority in its different versions, and that of consensus in full network all tend to be very similar.

It can be assumed that in most organization environments higher expected returns will go together with higher risk. Subsequently, two economically relevant contexts to be compared are [− 4,8], high return and high risk, and [− 1, 1], low return and low risk. In the first case the $E _ { \widetilde { v } }$ with centralized authority and that of consensus in full network are quite similar, i.e., the choice of the organization structure would not be that relevant. However, in the second case the $E _ { \widetilde { v } }$ with consensus is considerably lower than that with authority. Consequently, in this sce nario, the choice of the organization structure could be very relevant, with the consensus mechanism clearly preferred over authority.<sup>4</sup>

The information in Tables 1 and 2 on expected values of the expected loss of the variable $E O L \Big ( \widetilde { V } \Big )$ , is complemented with Fig. 9 A and 9 B that show the probability distribution of the random variable, $\mathbf { P } \Big [ E O L \big ( \widetilde { V } \big ) \le$ $\ell \rceil$ from $( 7 ) ,$ , for centralized authority and consensus with full network, and selected parameter values (first row of Tables 1 and 2).

![](/api/attachments/94ASNZP4/fulltext/images/bca33b027e8c255275b026b51c2399e5592c29460e8e2b1051e59fa4dab375c0.jpg)  
Fig. 8. Mean opportunity loss $E _ { \widetilde { V } } \Big [ E O L \big ( \widetilde { V } \big ) \Big ]$ as a function of the interest rates for different organization structures when $\widetilde { V }$ is uniformly distributed between − 8 and 10.

Table 1  
Sensitivity of $E _ { \widetilde { v } }$ to changes in the dispersion of random variable $\widetilde { V }$ with $E \Big ( \widetilde { V } \Big ) = V _ { 0 } = 1$ constant, and to changes in interest rate

<table><tr><td rowspan="2"></td><td rowspan="2">Authority</td><td colspan="2"></td><td rowspan="2">Consensus</td><td rowspan="2"></td><td rowspan="2"></td></tr><tr><td colspan="2">Decentralization: Hierarchy</td></tr><tr><td></td><td>r=0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $[V_m, V_M]$ </td><td>Centralization</td><td>Star</td><td>Tree</td><td>Full network</td><td>Star</td><td>Tree</td></tr><tr><td>[0,2]</td><td>0.1694</td><td>0.1690</td><td>0.1807</td><td>0.1308</td><td>0.1306</td><td>0.1309</td></tr><tr><td>[-4,6]</td><td>0.1583</td><td>0.1583</td><td>0.1907</td><td>0.0969</td><td>0.0970</td><td>0.0968</td></tr><tr><td>[-8,10]</td><td>0.0913</td><td>0.0913</td><td>0.1105</td><td>0.0555</td><td>0.0555</td><td>0.0553</td></tr><tr><td></td><td>r=0.005</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[0,2]</td><td>0.1722</td><td>0.1723</td><td>0.1839</td><td>0.1496</td><td>0.1762</td><td>0.1651</td></tr><tr><td>[-4,6]</td><td>0.1671</td><td>0.1744</td><td>0.2116</td><td>0.1504</td><td>0.2147</td><td>0.1799</td></tr><tr><td>[-8,10]</td><td>0.1046</td><td>0.1162</td><td>0.1438</td><td>0.1306</td><td>0.2184</td><td>0.1688</td></tr><tr><td></td><td>r=0.01</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[0,2]</td><td>0.1750</td><td>0.1756</td><td>0.1870</td><td>0.1671</td><td>0.2145</td><td>0.1953</td></tr><tr><td>[-4,6]</td><td>0.1760</td><td>0.1904</td><td>0.2322</td><td>0.2022</td><td>0.3239</td><td>0.2588</td></tr><tr><td>[-8,10]</td><td>0.1177</td><td>0.1409</td><td>0.1766</td><td>0.2035</td><td>0.3708</td><td>0.2771</td></tr></table>

Table 2  
$E _ { \widetilde { v } }$ for distributions of $\widetilde { V }$ with different mean and dispersion values

<table><tr><td colspan="7"> $r = 0.005$ </td></tr><tr><td rowspan="2"></td><td rowspan="2">Authority</td><td colspan="2"></td><td rowspan="2">Consensus</td><td rowspan="2" colspan="2"></td></tr><tr><td colspan="2">Decentralization: Hierarchy</td></tr><tr><td> $[V_m, V_M]$ Expected  $V = 2$ </td><td>Centralization</td><td>Star</td><td>Tree</td><td>Full network</td><td>Star</td><td>Tree</td></tr><tr><td>[1,3]</td><td>0.2456</td><td>0.4163</td><td>0.5144</td><td>0.3793</td><td>0.4606</td><td>0.4229</td></tr><tr><td>[0,4]</td><td>0.2064</td><td>0.3008</td><td>0.3671</td><td>0.2513</td><td>0.3165</td><td>0.2845</td></tr><tr><td>[-4,8]</td><td>0.1470</td><td>0.1584</td><td>0.1941</td><td>0.1537</td><td>0.2375</td><td>0.1908</td></tr><tr><td>Expected  $V = 0$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[-1,1]</td><td>0.2407</td><td>0.0760</td><td>0.0482</td><td>0.0077</td><td>0.0095</td><td>0.0088</td></tr><tr><td>[-2,2]</td><td>0.1993</td><td>0.1100</td><td>0.1064</td><td>0.0748</td><td>0.0881</td><td>0.0826</td></tr><tr><td>[-6,6]</td><td>0.1388</td><td>0.1409</td><td>0.1703</td><td>0.1177</td><td>0.1638</td><td>0.1392</td></tr></table>

In the two figs. (9.A and 9.B), the cumulative probability distribution is discontinuous at EOL of 0, i.e., there is a positive probability of 0 EOL. When $r = 0 , \mathrm { F i g } . 9 . \mathrm { A } ,$ the probability of positive EOL starts at 0.6 for structures with the centralized authority mechanism. and at 0.7 for the consensus in full network. The cumulative probability of the positive EOLs with consensus dominates that of those with authority, and the mean value of EOL with consensus is lower than that with authority. With a confidence of 95%, the EOL with authority (consensus) will be lower than 0.8255 (0.7596). These results are consistent with those in the same scenario in Table 1. When $r = 0 . 0 1 , \mathrm { F i g . 9 . B }$ , the average EOL is also lower in consensus than in authority but the two are closer now. The mean value of EOL is higher with authority than with consensus, though the probability distribution with consensus only dominates that with authority at 0 and for $E O L \Big ( \widetilde { V } \Big ) \ge 0 . 2$

## 5.1. Other robustness results

The $E _ { _ V }$ with the centralized authority is determined in a balanced way of losses attributed to omission and to commission errors, while with consensus the $E _ { \widetilde { v } }$ is mainly determined by losses from the omission errors and hardly of losses from commission errors. Organizations that bear more penalties from the commission errors than from the omission ones would prefer the consensus mechanism to authority. In fact, when the priority is to avoid commission errors decentralized hierarchy mechanism would be preferred to centralized authority, in terms of lower $E _ { \widetilde { v } } .$ The $E _ { _ V }$ of decentralized hierarchy and consensus will be close but lower with consensus than with authority.

![](/api/attachments/94ASNZP4/fulltext/images/30f769b0fd250731648a3072bf95f7735227e32f824e64a722cd1c1dfbe43d49.jpg)  
A. N=13, r=0, and V ∈ U [0,2]

![](/api/attachments/94ASNZP4/fulltext/images/3dccde2fd15620814ffe565699ee9ccf2e9dea1b5b050bf5683432d12060c6bb.jpg)  
B. N=13, r=0.01, V ∈ U[0,2]  
Fig. 9. Cumulative probability distribution of random variable EOL V<sup>̃</sup> with centralized authority and consensus in full network.

Simulation results (not included in this paper) confirm the intuition that higher values of parameter β (less bounding rationality) result in a lower $E _ { _ V }$ in all organization structures. Moreover, the reduction in the average EOL is proportionally similar across organization structures and distributions of the random variable value of the project. If individuals differ in capacity to process information the performance of collective decisions improves placing those individuals with higher capacity in the authority position. With consensus, individuals with different informa tion processing capacity can be randomly assigned in the nodes of the network. With heterogeneous individuals the structures with authority, especially with centralized authority, will have an additional advantage over consensus. Consensus with full network will then be preferred when individuals in organization have all similar skills.

The simulated values of the probability of mistakes, time to reach a decision, and the EOL for different network sizes N (1, 6, 13, 50, 100, and 500), show that the probability of mistakes varies with the size of the network up to $N = 1 3 ;$ for values higher than 13 the probability of mistakes to higher values of N varies very little, for a given V. As ex pected from the results of Sah and Stiglitz [8], for relatively small initial values of N, higher N implies lower (higher) probability of the com mission (omission) errors.

The time to reach a group decision with the consensus mechanism increases substantially with N, especially for values of the new project that are not too different from the value of the status quo. With decen tralized hierarchy a network with N = 100 and span of control of 3 would need a maximum number of 4 iterations to reach a decision, which means that the sensitivity of time to reach a decision to the size of the network is much lower in authority than in consensus. When time to reach a consensus matters larger networks penalize consensus over centralized authority.

## 6. Practical relevance of the research

This study must be viewed as an attempt to learn about the de terminants of the quality of the decision process at the preimplementation stage, particularly the effect of bounded rationality of humans in the mistakes that people make in processing the information available (random factors that result in project risks that cannot be altered through the choice of organization structure are ignored). This stage of the decision process is non-observable by the researchers and we propose to learn about it through simulation. One important side product of the study of the quality of the decisions with measures of performance that include opportunity losses from commission and omission errors. Obviously, the observation of success and failure of actual decisions informs only about possible commission errors, and in an imperfect way because success and failure also depend on luck and implementation effectiveness. Omission errors are totally opaque for external observers. The simulation approach allows us to study the de terminants of commission errors free from the interference of nature and implementation failures.

Understanding the determinants of success and failure of organiza tional innovations is of practical importance considering the high rate of reported failures by business firms. One report on failures in the implementation of big data projects by business firms [46] says that “85% of the big data projects that firms undertake end up with failure”. Consultants in this area claim that the reason of failure is not so much the technology but, “integrating (the big data projects) with existing business processes and applications; management (and organizational) resistance; internal politics; lack of skills; and security and governance challenges”. Proposed solutions to reduce failure rates include “build out small, departmental successes into holistic, company-wide initiatives” and “seed these projects in a more bottom-up fashion, driven by de velopers”. But they have drawbacks too because “a company's culture may not be able to keep pace with attempts to quickly scale out projects, and the very DNA that made the small-scale project successful would likely prove insufficient to carry the broader project to a successful conclusion”.

What the theoretical results reported here tell us about the high rate of failure in big data projects, and about the approaches to the organi zation innovation adoption decision proposed by consultants, a bottom up, muddling through, culture driven one, and a top down, authoritydriven approach? In the framework of this paper, the reported failures would be classified as commission errors (projects adopted and imple mented that should had been rejected), but nothing is said on omission errors (projects that were rejected and that could have been a success). Therefore, with the published information, the diagnosis about inno vation performance is limited. Commission errors should be evaluated jointly with omission errors, and it would be interesting to assess the growth potential and the risk of the high data projects, and use the re sults of the comparative static analysis above to see which organization structure would be more appropriate given the projects' characteristics. The consultants recommend the bottom-up decision mechanisms to reduce implementation failures related with resistance to change, organizational politics, culture and alike. The research reported here recommends considering also the performance in the preimplementation stage when choosing between bottom-up or top-down decision-making mechanisms. Moreover, to take full advantage of changing from top-down (authority) to bottom-up (consensus), the simulation results recommends replacing the tree-like communication structure of centralized authority by full networks.<sup>5</sup>

Table 3  
Summary of calculations. Best values are highlighted in bold.

<table><tr><td rowspan="2">Project</td><td colspan="2">Probability accept (reject)</td><td colspan="2">Expected return</td><td colspan="2">EOL</td><td>EOL</td><td>Time to decision</td><td>EOL with discount (r)</td></tr><tr><td>A</td><td>B</td><td>A</td><td>B</td><td>A</td><td>B</td><td>A and B</td><td>A and B</td><td>A and B</td></tr><tr><td>CA</td><td>0.52 (0.48)</td><td>0.48 (0.52)</td><td>1.042</td><td>0.962</td><td>0.038</td><td>0.038</td><td>0.0384</td><td>1</td><td> $0.54–0.5016e^{r}$ </td></tr><tr><td>DAS</td><td>0.29 (0.71)</td><td>0.25 (0.75)</td><td>1.023</td><td>0.980</td><td>0.057</td><td>0.020</td><td>0.0384</td><td>1.8</td><td></td></tr><tr><td>DAT</td><td>0.20 (0.80)</td><td>0.17 (0.99)</td><td>1.016</td><td>0.987</td><td>0.064</td><td>0.013</td><td>0.0386</td><td>2.2</td><td></td></tr><tr><td>C</td><td>0.12 (0.88)</td><td>0.05 (0.95)</td><td>1.001</td><td>0.996</td><td>0.071</td><td>0.004</td><td>0.0372</td><td>20.3</td><td> $0.123–0.086e^{20.3r}$ </td></tr></table>

## 6.1. Illustrative example

The following is an illustrative example of application of the ABM approach to the evaluation of organization structures. A Research Institute operates a supercomputer that is used in projects that require complex and numerous calculations. One of the research teams has the duty of coming out with innovation projects that will potentially improve the computation power of the supercomputer. The team is composed of a principal investigator, PI, three seniors, and nine junior researchers. The Institute considers the following organization struc tures for the evaluation and decision on proposals about improving the working of the supercomputer.

Centralized authority (CA): the PI centralizes proposals and decisions.

Decentralized authority and star (DAS): the three senior researchers and the nine junior ones can directly communicate with the PI. Each person decides whether a project is worth presenting to the PI for approval or not. If presented, the PI makes the final decision.

Decentralized authority and tree (DAT): three junior researchers communicate with one senior and the senior communicates directly with the PI. Seniors can present proposals directly to the PI who decides on it. Juniors decide on their proposals to present them to the respective senior or not; the senior will decide to present it to the PI for final decision.

Consensus (C): All researchers have the same decision power, and all are directly connected as in a full network communication structure; projects for improvement can appear at any node of the network. The researcher with a proposal to make would randomly choose another member of the team to share the information on the proposal and make the decision: either the two agree in supporting the project, or the two agree on rejecting it. The process continues as long as there is one researcher supporting the adoption of the innovation project or all agree on supporting the innovation and implement it.

In all cases, during the decision time the supercomputer operates with the current level of performance, $V _ { 0 } = 1 6 { , } 3 8 4$ spins/ns. There are two possible innovation projects that can appear at any node of the organization with equal probability: Project $\mathsf { A } \colon V = 1 7 , 6 9 4 . 7 2$ spins/ns, or $V / V _ { 0 } = 1 . 0 8 ;$ Project B: $V = 1 5 , 0 7 3 . 2 8$ spins/ns, or $V / V _ { 0 } = 0 . 9 2$ . With full rationality A would always be accepted and B rejected. With bounded rationality, the probability of accepting (Eq. (1)), expected return, EOL with $r = 0 ( \mathrm { E q }$ . (8) from (2) and (3)), and EOL with $r \neq 0 ( \mathrm { E q } .$ (8) from (4) and (5)), appear in Table 3.

The comparisons are restricted to centralized authority and consensus, the two with expected opportunity loss, EOL. If time does not matter (r = 0) Consensus is preferred. When time matters $( r \neq 0 )$ the preferred organizational structure depends on the value of r. Solving the equation $0 . 5 4 \textrm { -- } 0 . 5 0 1 6 \mathrm { e } ^ { r } = 0 . 1 2 3 2 \textrm { -- } 0 . 0 8 6 0 \mathrm { e } ^ { 2 0 . 3 r }$ , the interest rate at which the two structures are indifferent is $r = 0 . 0 0 1$ . With higher (lower) values centralized authority (consensus) will be preferred.

## 7. Conclusion

How to transform individually fallible elements into a reliable sys tem is a relevant question in physical [47] and social domains [8,9]. This study evaluates the effect of organization structure decisions on the performance of groups of fallible individuals joint through communi cation lines that decide about the acceptance or rejection of projects whose value is a realization of a random variable of known distribution that appears at random in any node. The structures combine two design variables, the communication network (star, tree, or full network), and the group decision mechanism (authority and consensus).

Two polar organization structures for group decision making emerge from the analysis, centralized authority in tree networks, and consensus in full network. The combination of authority decision making (directed flows) and a tree like communication network (minimal communication lines) represents the more traditional organization structure. Consensus in full network emerges as a potential alternative in a time of denser and cheaper communications. Traditional (hierarchical) and emerging (network-consensus) structures appear as competing outcomes from efficiency driven choices by firms and organizations in general. The results of the paper point out to the comparative disadvantage of consensus-based decisions in trees, compared with the performance of consensus in full networks. Therefore, maintaining the tree network dominating in many firms it is unlikely that consensus will replace au thority. For consensus having a chance in replacing authority, the full network must be extended among firms, replacing the tree.

From a managerial perspective, the results of this study indicate that the expected opportunity loss of consensus tends to be lower in: i) organizational environments of low interest rates that do not severely penalize the time needed to reach a consensus; ii) environments of low costs communications that ease the implantation of full networks; iii) when the risks owing to the environmental shocks around the status quo are moderately low (low dispersion of the probability distribution of the values of the projects that challenge the status quo); and iv) in organi zational environments that expect worst results relative to the status quo (the mean of the distribution of the projects' economic values is lower than the economic value under the status quo). On the contrary, the authority mechanism is preferred in opposite conditions to the aforementioned, but particularly when organizations anticipate flows of innovation projects from a distribution of values with mean higher than the value in the status quo and high variance. The consensus mechanism better handles the costs of the errors when the external environment of the organization worsens relative to the status quo. Inversely, authority is more effective in reducing the costs from errors owing to not leveraging the advantage of the new opportunities of more favorable external environments of the organization. These predictions open empirical research opportunities to test them.

The paper is motivated by the practical relevance of improving the quality of individual and group decisions, and the difficulty of properly identifying the reasons of success and failure in decision making by just observing the organization innovation projects that fail and succeed. We argue that the bounded rationality of individuals in organizations, conditions the final outcome in the adoption of innovations already in the pre-execution stage of processing the information available for de cision. This stage of the decision-making process is rarely directly observable by researchers so we propose to study it with the help of simulation in the spirit of agent-based modeling. In the paper we use the evidence on the high number of big data innovation projects that fail in practice (an issue that raises concerns for many years [48]), to assess the practical relevance of the research methodology and results. We show the relevance of accounting for opportunity losses from omission errors in decision-making (unobservable for the external observer) to explain the observed rates of commission errors, and the power of consensus compared with authority to lower ex ante expected opportunity losses and to unlock organization change by facilitating the implementation of innovations [49]. The methodology proposed here complements well with the increasing use of internet-based tools for crowd participation by companies in idea generation, idea evaluation, and problem solving processes that traditionally were reserved for experts, i.e., “wisdom of the crowd” versus use of experts in the evaluation of innovation projects and business models (Hienerth and Riar [50], for a review).

Future research could examine its connections with the choice of organization structures when individuals make decisions under “imprecise and vague information”, as assumed in the fuzzy decision theory. The probability of choice that captures the intended but boun ded rationality of individuals has several similarities with the cases of fuzzy preference relations formulated in Chiclana et al. [51]. The ABM simulation considers that the randomness in the outcomes from group decisions result only from the bounded rationality of group members (omission and commission errors); we could study situations where the value of the innovation projects is uncertain because of uncontrollable exogenous random factors, the quality of group decision-making in human-automata interaction environments, such in artificial intelli gence scenarios, and the choice of organization structures in competitive situations where the payoffs from that choice by one firm depends on the choices of other firms in the same market.

## Acknowledgment

This work was supported by the Spanish Ministerio de Economía y Competitividad, [ECO2013-48496-C4-3-R and MTM2016-77642-C2-2- P], the Diputacion ´ General de Aragon ´ (DGA) and the European Social Fund [CREVALOR and Grants E22\_17R], and the Centro Universitario de la Defensa [UZCUD2017-SOC-04].

## References

[1] H.A. Simon, Administrative Behavior: A Study of Decision-Making Processes in Administrative Organizations, 4th ed., Simon & Schuster, 1997.

[2] R.M. Burton, B. Obel, Strategic Organizational Diagnosis and Design: The Dynamics of Fit, 3rd ed., Kluwer, 2004.

[3] R.M. Cyert, J.G. March, A Behavioral Theory of the Firm, 2nd ed., Blackwell, 1992.

[4] R.L. Daft, R.H. Lengel, Organizational information requirements, media richness and structural design, Manag. Sci. 32 (1986) 554–571, https://doi.org/10.1287/ mnsc.32.5.554.

[5] J.G. March, H.A. Simon, H.S. Guetzkow, Organizations, 2nd ed., Blackwell, 1993.

[6] X.-B. Jin, G.-G. Geng, G.-S. Xie, K. Huang, Approximately optimizing NDCG using pair-wise loss, Inf. Sci. 453 (2018) 50–65, https://doi.org/10.1016/j. ins,2018.04.033.

[7] S. Suresh, N. Sundararajan, P. Saratchandran, Risk-sensitive loss functions for sparse multi-category classification problems, Inf. Sci. 178 (2008) 2621–2638, https://doi.org/10.1016/i.ins.2008.02.009.

[8] R.K. Sah, J.E. Stiglitz, The architecture of economic systems: hierarchies and polyarchies, Am. Econ. Rev. (1986) 716–727.

[9]. R.K. Sah. JE. Stiglitz. Committees. hierarchies and polvarchies, Econ, J. 98 (1988) 451, https://doi,org/10.2307/2233377.

[10] I.J. P´erez, F.J. Cabrerizo, S. Alonso, Y.C. Dong, F. Chiclana, E. Herrera-Viedma, On dynamic consensus processes in group decision making problems, Inf. Sci. 459 (2018) 20–35, https://doi.org/10.1016/j.ins.2018.05.017.

[11] E. Herrera-Viedma, F. Herrera, F. Chiclana, A consensus model for multiperson decision making with different preference structures, JEEE Trans. Syst., Man. Cybern. A 32 (2002) 394–402, https://doi.org/10.1109/TSMCA.2002.802821.

[12] M. Fedrizzi, J. Kacprzyk, S. Zadrozny, ˙ An interactive multi-user decision support system for consensus reaching processes using fuzzy logic with linguistic quantifiers, Decis, Support. Syst. 4 (1988) 313–327. https://doi,org/10.1016/ 0167-9236(88)90019-X

[13] F. Herrera, E. Herrera-Viedma, J.L. Verdegay, A model of consensus in group decision making under linguistic assessments, Fuzzy Sets Syst. 78 (1996) 73–87, https://doi.org/10.1016/0165-0114(95)00107-7.

[14] T.L. Saaty, Decision making with the analytic hierarchy process, Int. J. Serv. Sci. 1 (2008) 83–98, https://doi.org/10.1504/IJSSci.2008.01759.

[15] V. Salas-Fum´as, C. S´aenz-Royo, A. <sup>´</sup> Lozano-Rojo, Organisational structure and performance of consensus decisions through mutual influences: a computer simulation approach, Decis. Support. Syst. 86 (2016) 61–72, https://doi.org/ 10.1016/i.dss.2016.03.008.

[16] M. Christensen, T. Knudsen, The Architecture of Economic Organization: Toward a General Framework. Frederiksberg: The Link Program. 2002.

[17] M. Christensen, T. Knudsen, Design of decision-making organizations, Manag. Sci. 56 (2010) 71–89, https://doi.org/10.1287/mnsc.1090.1096.

[18] F.A. Csaszar, An efficient frontier in organization design: organizational structure as a determinant of exploration and exploitation, Organ. Sci. 24 (2013) 1083–1101, https://doi.org/10.1287/orsc.1120.0784.

[19] T. Knudsen, D.A. Levinthal, Two faces of search: alternative generation and alternative evaluation, Organ. Sci. 18 (2007) 39–54, https://doi.org/10.1287/ orsc.1060.0216.

[20] F.A. Csaszar, Organizational structure as a determinant of performance: evidence from mutual funds, Strateg. Manag. J. 33 (2012) 611–632, https://doi.org 10.1002/smj.1969.

[21] R. Garud, P. Nayyar, Z. Shapira, Technological choices and the inevitability of errors, in: R. Garud, P.R. Nayyar, Z.B. Shapira (Eds.), Technological Innovation, Cambridge University Press, 1997, pp. 20–40, https://doi.org/10.1017/ CBO9780511896613.005.

[22] R. Gulati, M.C. Higgins, Which ties matter when? The contingent effects of interorganizational partnerships on IPO success, Strateg. Manag. J. 24 (2003) 127–144, https://doi.org/10.1002/smj.287.

[23] J. Lerner, The syndication of venture capital investments, Financ. Manag. 23 (1994) 16, https://doi.org/10.2307/3665618.

[24] P. Puranam, B.C. Powell, H. Singh, Due diligence failure as a signal detection problem, Strateg. Organ. 4 (2006) 319–348, https://doi.org/10.1177 1476127006069426

[25] J. Raab, P. Kenis, Heading toward a society of networks: empirical developments and theoretical challenges, J. Manag. Inq. 18 (2009) 198–210, https://doi.org 10.1177/1056492609337493

[26] M. Castells, The Rise of the Network Society: The Information Age: Economy, Society, and Culture, 2nd ed., Wiley John & Sons, 2009.

[27] M. Van Alstyne, The state of network organization: a survey in three frameworks, J. Organ. Comput. Electron. Commer. 7 (1997) 83–151, https://doi.org/10.1080 10919392.1997.9681069

[28] R.D. Luce, Semiorders and a theory of utility discrimination, Econometrica 24 (1956) 178, https://doi.org/10.2307/1905751

[29] T. Pachur, R.S. Suter, R. Hertwig, How the twain can meet: prospect theory and models of heuristics in risky choice. Cogn. Psychol. 93 (2017) 44–73. https://doi org/10.1016/i.cogpsych.2017.01.001.

[30] B. Scheibehenne, T. Pachur, Using Bayesian hierarchical parameter estimation to assess the generalizability of cognitive models of choice, Psychon. Bull. Rey. 22 (2015) 391–407, https://doi.org/10.3758/s13423-014-0684-4

[31] R.S. Sutton, A.G. Barto, Reinforcement Learning: An Introduction, 2nd ed., MIT, 1998.

[32] P. Puranam, N. Stieglitz, M. Osman, M.M. Pillutla, Modelling bounded rationality in organizations: progress and prospects, ANNALS 9 (2015) 337–392, https://doi. org/10.5465/19416520.2015.1024498.

[33] J. Pearl, Bayesianism and causality, or, why I am only a half-bayesian, in: D. Corfield. J. Williamson (Eds.). Foundations of Bavesianism. Springer. 2001 pp. 19–36, https://doi.org/10.1007/978-94-017-1586-7\_2.

[34] A. Aznar Grasa, Econometric Model Selection: A New Approach, Springer, 1989, https://doi org/10.1007/978-94-017-1358-0

[35] J.O. Berger, Statistical Decision Theory and Bayesian Analysis, Springer, 1985.

[36] J.M. Bernardo, A.F.M. Smith, Bayesian Theory, John Wiley & Sons, 1994, https:/ doi.org/10.1002/9780470316870.

[37] M.S. Catalani, G.F. Clerico, How and when unanimity is a superior decision rule, in: Decision Making Structures, Physica-Verlag HD, 1996, pp. 15–29, https://doi.org 10.1007/978-3-642-50138-8 2

[38] L. Yu, K.K. Lai, A distance-based group decision-making methodology for multi person multi-criteria emergency decision support, Decis. Support. Syst. 51 (2011) 307–315, https://doi.org/10.1016/j.dss.2010.11.024.

[39] G. Fioretti, Agent-based simulation models in organization science, Organ. Res. Methods 16 (2013) 227–242, https://doi,org/10.1177/1094428112470006.

[40] M.W. Macy, R. Willer, From factors to actors: computational sociology and agentbased modeling, Annu. Rev. Sociol. 28 (2002) 143–166, https://doi.org/10.1146 annurev.soc.28.110601.141117

[41] I. Moya, M. Chica, O. <sup>´</sup> Cordon, ´ A multicriteria integral framework for agent-based model calibration using evolutionary multiobjective optimization and network based visualization, Decis. Support. Syst. 124 (2019) 113111, https://doi.org/ 10.1016/i.dss.2019.113111

[42] M.A. Zaffar, R.L. Kumar, K. Zhao, Using agent-based modelling to investigate diffusion of mobile-based branchless banking services in a developing country, Decis. Support. Syst. 117 (2019) 62–74, https://doi.org/10.1016/j. dss.2018.10.015.

[43] Y. Dong, H. Zhang, E. Herrera-Viedma, Integrating experts' weights generated dynamically into the consensus reaching process and its applications in managing non-cooperative behaviors, Decis. Support. Syst. 84 (2016) 1–15, https://doi.org 10.1016/i.dss.2016.01.002.

[44] Z. Gong, X. Xu, H. Zhang, U. Aytun Ozturk, E. Herrera-Viedma, C. Xu, The consensus models with interval preference opinions and their economic

interpretation, Omega 55 (2015) 81–90, https://doi.org/10.1016/j. omega.2015.03.003.

[45] H. Zhang, I. Palomares, Y. Dong, W. Wang, Managing non-cooperative behaviors in consensus-based multiple attribute group decision making: an approach based on social network analysis, Knowl.-Based Syst. 162 (2018) 29–45, https://doi.org 10.1016/i.knosys.2018.06.008

[46] M. Asay, 85% of Big Data Projects Fail, but your Developers Can Help Yours Succeed, TechRepublic. https://www.techrepublic.com/article/85-of-big-data projects-fail-but-your-developers-can-help-yours-succeed/, 2017.

[47] E.F. Moore. C.E. Shannon. Reliable circuits using less reliable relays, J. Franklin Inst. 262 (1956) 191–208, https://doi.org/10.1016/0016-0032(56)90559-2.

[48] J.I. Porras, P.J. Robertson, Organizational Development: Theory, Practice, and Research., Consulting, Psychologists Press, 1992.

[49] M. Choi, W.E.A. Ruona, Individual readiness for organizational change and its implications for human resource and organization development, Hum. Resour. Dev. Rev. 10 (2011) 46–73. https://doi.org/10.1177/1534484310384957

[50] C. Hienerth, F. Riar, The wisdom of the crowd vs. expert evaluation: A conceptualization of evaluation validity, in: 35<sup>th</sup> DRUID Celebration Conference, 2013, pp. 17–19.

[51] F. Chiclana, F. Herrera, E. Herrera-Viedma, Integrating three representation models in fuzzy multipurpose decision making based on fuzzy preference relations, Fuzzy Sets Syst. 97 (1998) 33–48.
