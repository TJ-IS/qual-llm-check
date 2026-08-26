---
otero_id: 20905
otero_key: "AXQ5B8WU"
title: "Market monitoring and control of ancillary services"
authors: "Ali Keyhani; Ashkan Kian; Jose Cruz; Marwan A. Simaan"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00103-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Market monitoring and control of ancillary services

Ali Keyhani <sup>a,)</sup>, Ashkan Kian <sup>a</sup>, Jose Cruz Jr. <sup>a</sup>, Marwan A. Simaan <sup>b</sup>

<sup>a</sup> Department of Electrical Engineering, 205 Dreese Laboratory, Ohio State UniÕersity, 2015 Neil AÕenue, Columbus, OH 43210, USA UniÕersity of Pittsburgh, Pittsburgh, PA, USA

## Abstract

In this paper, the problems of market monitoring and control of ancillary services of future energy systems are presented. We envision that future system operation of electric power systems will evolve into completely unbundled ancillary service markets that are governed by spot price signals. The grid operators need to acquire ancillary services through competitive markets for control of the system operation. With the above vision of the future, this paper presents the control of ancillary services based on a frequency regulation<sup>r</sup>load following LFC market, a load regulating RL market, and a base load BLŽ . Ž . Ž . market. In the LFC market, the units dispatched for generation must have specific response characteristics as determined by the nature of system loads. These units will be controlled by the grid operator. It is envisioned that LFC will be multi-time scale and decentralized. In the RL market, the units dispatched for generation will not participate in LFC. These units are dispatched for specific period of time for regulating system load. The BL units are dispatched daily to satisfy the BL of the day on a weekly or monthly basis. The locational market power associated with generators participating in LFC and in RL is even more critical than that for generators participating in satisfying the BL, since these units are required for frequency regulation, voltage support and relief of overload conditions. To create an efficient market for these services, we will propose and formulate the use of incentive strategies for the BL, RL and the LFC markets. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Ancillary services; Market monitoring; Incentive control; Optimization; Game theory; Strategic bidding

## 1. Introduction

The future energy systems will be controlled by multi-lateral markets and ancillary services markets. The multi-lateral markets will provide fixed energy over specified period of time and these energy sources cannot be controlled for matching the load demand to generation 1,13–17 . The primary function of the <sup>w</sup> <sup>x</sup> ancillary services is to provide generation control and the capability to respond to dynamic system conditions. The market monitoring and decentralized control of future energy systems will be impacted by the following technological development.

## 1.1. Impact of generation technology

In the 21st century, deregulation of the power industry will become a reality and a competitive market will determine the efficient production of electric energy. In the deregulated market, there will be many new power producers and market makers. In addition, if fuel cell technology is established as a viable technology in power generation, then every consumer has the potential to become a power producer. Although these changes may take many years to become reality for small users, one would expect that the large industrial and commercial users would move to establish their own generation using the new established micro turbine and combined-cycles gas technologies. Many complex problems need to be studied. With a highly distributed generation system, how should the base load BL , regulating load andŽ . ancillary services be provided? How should the market be monitored for anti competitive behaviors?

## 1.2. Impact of communication and computer technology

Greatly expanded computer instrumentation, control, sensing, and communications capabilities will be utilized in all levels of power system network from generating stations, transmission system substations, distribution systems and customer sites. The distributed network of computer systems are required for interactive, real-time control of generation and bus voltages, over the highly interconnected, geographically dispersed generation and load. To effectively utilize the power of distributed computer instrumentation, the computational algorithms based on distributed models will be necessary to achieve decentralized computer control of the network operations.

## 1.3. Impact of enÕironmental issues

The impact of pollution on mankind and the planet will continue to be a social issue for the next century. To reduce the smog and pollution in the cities, the use of electric vehicles will become a reality with large impact on power usage. As the demand for electric energy grows, more power producers and power marketers will enter the energy market. The need for efficient market monitoring to deal with anti-competitive behavior should be addressed. The solution of this problem will assure the efficient production of electric energy and stable operation of the power network.

## 1.4. Impact of the spot pricing market

With implementation of emerging metering technology, the spot price of energy can be send to the customer 6,11,12,19,20,22,27,29 . The metering sys-<sup>w</sup> <sup>x</sup> tem can control various loads at the customer sites. The customer can be offered a number of variable price schedules based on the time of usage. With the customer in the loop of energy usage and reacting to the spot price market, control of the ancillary services will need to be investigated.

## 1.5. Impact of the control technology

The rapid expansion of computer, sensing, and communication systems has revolutionized the development of multi-agent controllers using neural network<sup>r</sup>fuzzy logic- and rule-based systems for control of large-scale, uncertain, nonlinear, and time-dependent systems. The vertically integrated power companies have relied on central control of system frequency and power flows on the transmission tie lines to neighboring systems for stable operation. The vulnerabilities of centralized control systems have been demonstrated by blackouts of 1967, 1977, 1978, and 1996. Is it feasible to decompose the power system and identify a number of control areas based on on-line measurement? What is needed is decentralized on-line modeling. For decentralized control of generation, on-line modeling techniques in presence of noise and measurement errors are needed. Algorithms for real-time processing large data set, pattern extractions, correlating information from separate data sets and knowledge acquisition for the development of on-line adaptive models are essential. The on-line models will facilitate the development of decentralized control agents and decision support with partial input and output observations. Therefore, what is needed is the development of decentralized multi-time scale, multi agent generation control systems for stable operation of the future restructured power system with dispersed generation sources. This is an essential technology for dealing with emergency conditions and orderly break up of the systems with a priori defined control areas that are still viable for stable operation.

## 1.6. Impact of the software technology

As the cost of memory and storage systems has rapidly decreased, there has been explosion in the development of new programming languages. These languages are based on object oriented programming techniques using many platforms. The $\mathrm { C } + +$ language allows for the design and implementation of the testbed system using a true object-oriented approach. The object-oriented approach allows for better system partitioning and visualization in solving complex system. Moreover, C<sup>qq</sup> code is relatively easy to maintain, re-use, modify, and allow for a group of programmers to work on separate parts of the code, without the errors multiplying in proportion to the length of the code. Programs written in $\mathrm { C } + +$ can be maintained and extended more easily and addition of functionality to the code is relatively straightforward with fewer risks of introducing errors. By using object-oriented features such as inheritance, re-using already written code is made more practical and codes comparable to Fortran in efficiency can in fact be written in $\mathrm { C } + +$ , along with the added benefits of saving valuable implementation time due to ease of code re-usability and maintenance.

Nowadays, visual programming packages for C<sup>q</sup> <sup>q</sup> are widely available that can save considerable amount of time in designing and implementing graphical user interface for the testbed. The Javabased object-oriented programming is a natural way of designing multi-agent simulation systems. The object-oriented programming is also a convenient technology for building libraries of re-usable software that will facilitate the exchange of agent com-Ž ponent ..

The power system consists of thousands of buses, power consumption of which, needs to be modeled on-line for use in security analysis. The object-oriented programming technology is a natural approach for development visualization models. Furthermore, this technology will be used to develop a virtual Java-based simulation testbed for study of market monitoring of ancillary services.

The main objective of the testbed is to develop the conceptual framework for using the grid operator Ž Ž .. independent system operator ISO in providing incentives to the multiple providers in an ancillary services market Fig. 1 . We assume that the gridŽ . operator buys energy for frequency regulation and load following from one or more energy providers in the ancillary services market. The grid operator provides transmission capacity rights to the energy providers. To allow the grid operator to influence the price, we assume that the transmission rights can be made function of the generation of the energy providers. The functions will be chosen in such a way that the resulting price for the ancillary services will be close to the full competition price. The methodology will be applied to the ancillary services market wherein the grid operator purchases energy for the purpose of regulating frequency and load following.

![](/api/attachments/AXQ5B8WU/fulltext/images/1e38cdd593056cefb9b349332db0da8ff6c8e4143820162319e77f15679ccdc7.jpg)  
Fig. 1. A deregulated power system operation schematic.

## 1.7. A new philosophy of future automatic generation control

We envision that future system operation of electric power systems will evolve into completely unbundled ancillary service markets that are governed by spot price signals. The grid operators need to acquire ancillary services through competitive markets for control of the system operation. The unbundled ancillary services will include frequency regulation<sup>r</sup>load following LFC and operating reserves.Ž . The power associated with ancillary services is critical, since the grid operators must be able to control specific resources for secure and stable operation. For example, when a grid operator loses a 1300 MW unit, the control system needs to react immediately to control the system for stable operation and then the operator needs to adjust the generator set points according to spot price signals. The reaction of energy users to spot price signals will have great impact on ancillary service markets. With the above vision of the future, we propose an LFC market, a load regulating market RL and a BL market. In theŽ . LFC market, the units dispatched for generation must have specific response characteristics as determined

by the nature of system loads. These components of load data sampled on 1-min interval and 5-min interval are shown in Fig. 2. These units will be controlled by the grid operator. It is envisioned that LFC will be multi-time scale and decentralized. In the RL, the units dispatched for generation will not participate in LFC. These units are dispatched for specific period of time for regulating system load. The BL units are dispatched daily to satisfy the BL of the day on a weekly or monthly basis. The locational market power associated with generators participating in LFC and in RL is even more critical than that for generators participating in satisfying the BL, since these units are required for frequency regulation, voltage support and relief of overload conditions. To create an efficient market for these services, the use of incentive strategies for the RL and the LFC markets is proposed that will be discussed later. Fig. 3 presents the proposed decentralized generation control. The sub-grid operators will function in the same manner for the subsystems as the grid operator does for the entire system. Refs. 1,13–<sup>w</sup> 18,28 present the modeling and control problems<sup>x</sup> related to these concepts.

## 2. Detailed technical rationale

## 2.1. Diffusing horizontal market power

Recent Federal law mandates the separation of the functions of generation, transmission, and distribution where there is an interstate power flow. There is supposed to be competition in generation but transmission and distribution remain regulated. Federal law mandates equal access to the transmission system for all generation providers. The open access in itself does not insure full competition. Hogan 7,8<sup>w</sup> <sup>x</sup>

![](/api/attachments/AXQ5B8WU/fulltext/images/a9d94ddb3dc2bd9b404ea2ab4313b27088371632f2bace19aa69891fe718016d.jpg)  
Fig. 2. Public service Indiana, load data on 1-min interval top figure , 5-min interval bottom figure. Ž . Ž .

![](/api/attachments/AXQ5B8WU/fulltext/images/4f12f518812bae590fa1cd028ddcdd8ca68a9cca93f828da17d2cae367bbdf73.jpg)  
Fig. 3. Future decentralized generation control.

demonstrates through several examples that when there are transmission constraints, it is possible to have an incremental generation of 1 MW at one bus to block generation of more than 1 MW at another bus. Thus, an increase in use of the network in one portion of the network can cause a reduction of capacity in another portion of the network. In this situation, there is a possibility of exploiting network interactions to restrict competition and manipulate prices. Furthermore, Ilic, et al. 9,10 , through sev-<sup>w</sup> <sup>x</sup> eral examples, show that a line created a localized sub-market of three buses in a 24-bus network, although the sub-market was still connected to the rest of the network by four unconstrained lines. They also showed how loop flows aggravate the problem. One approach to moving to a greater participation by small entrants to the market is to allow the grid operator, such as the ISO, to exercise greater authority and provide incentives to the various energy providers connected to the power systems. This can be cast in the framework of games where the grid operator is the ISO 2,4,5,23–25 . For example, an incentive model of duopoly with government coordination is presented in Refs. 23–25 . It is shown that<sup>w</sup> <sup>x</sup> the government, acting as ISO, can induce two companies to achieve perfect competition price while behaving as duopolists in a Cournot fashion. This concept can be adapted for dynamic systems.

## 2.2. A principle of incentiÕes in strategies [ ] 2,4,5,21,23–25

As mentioned earlier, our main objective is to develop a framework within which an ISO uses incentive controls in its interactions with multiple providers Gencos in an ancillary services market soŽ . as to achieve optimum performance and market monitoring of the entire grid operation. Ideally, this may include, among other things, the attainment of perfect market competition prices of ancillary services. To illustrate conceptually how this can be achieved, let us first consider a simple grid with one ISO and only one Genco. Let us assume that the ISO has a scalar decision variable x and the Genco has a scalar decision variable y. The ISO wishes to minimize an objective function that is influenced not only by its decision variable but also by the decision variable of the Genco. Denote this objective function by I xŽ , y.. Similarly, the Genco has an objective function denoted by $G ( x , y )$ . For simplicity, these functions are assumed to be convex. Finally, suppose that the choices of x and y must satisfy $C ( x , \ y ) = 0 .$ , also assumed to be convex. The relationship $C ( x , y ) = 0$ may represent various constraints that are imposed by the grid on the variables x and y.

In general, it is not possible to simultaneously minimize $I ( x , y )$ and $G ( x , y )$ with respect to both variables. The combination of x and y that minimizes $I ( x , y )$ may not be the same combination that minimizes $G ( x , y )$ . Furthermore, the ISO can only choose x and the Genco can only choose y. In spite of these limitations, the ISO wonders what would happen if it had complete control over the choices of both variables x and y, and if these could be chosen to minimize $I ( x , y )$ and satisfy the constraint $C ( x ,$ $y ) = 0$ . Suppose that the unique answer to this minimization problem is given by $x = X , y = Y$ , and $p = P .$ , where p is the Lagrange multiplier in the ISO’s Lagrangian function:

$$
L _ {I} (x, y, p) = I (x, y) + p C (x, y)
$$

From the ISO’s perspective, optimum operation of the grid can be achieved only if the Genco chooses, or is induced to choose, y<sup>s</sup>Y. Clearly, however, the Genco has no incentive to choose $y = Y$ unless it is induced to do so. With this result, the ISO wonders how it could induce the Genco to choose y<sup>s</sup>Y.

Suppose that the ISO decides to implement a sophisticated strategy whereby its decision variable x is allowed to be a function of the Genco’s choice of y, i.e., $x = h ( y )$ , where the function h is to be determined by the ISO. By doing so, the ISO is giving the Genco an incentive to influence his final choice of x. The question that still needs to be answered is how does the ISO select this function to induce the Genco to choose $y = Y ?$ In order to illustrate how this can be done, let us consider a simple example of such an incentive function. Let

$$
x = X + A (y - Y)
$$

where A is a constant yet to be determined, and Y is the Genco’s control, desired by the ISO, obtained as explained earlier. We will demonstrate that under some reasonable conditions, this strategy will induce the Genco to choose y<sup>s</sup>Y. We proceed to examine the Genco’s optimization problem. Knowing that x will depend on y through the above expression, the Genco proceeds to minimize its objective function: $G ( x , y )$ , subject to the two constraints: $x = X + A \left( { \mathrm { ~ y ~ } } \right)$ $- Y )$ and $C ( x , \ y ) = 0$ . The Genco’s Lagrangian function is:

$$
\begin{array}{r l} L _ {G} (x, y, p _ {1}, p _ {2}) & = G (x, y) \\ & + p _ {1} \{x - X - A (y - Y) \} \\ & + p _ {2} C (x, y) \end{array}
$$

where $p _ { 1 }$ and $p _ { 2 }$ are Lagrange multipliers. Assuming that G and C are differentiable, the differential of $L _ { G } ( x , \ y , \ p _ { 1 } , \ p _ { 2 } )$ can be determined as:

$$
\begin{array}{r l} \mathrm{d} L _ {G} (x, y, p _ {1}, p _ {2}) & = \left\{R (x, y) + p _ {1} \right\} \mathrm{d} x \\ & + \left\{S (x, y) - A p _ {1} \right\} \mathrm{d} y \\ & + \left\{x - X - A (y - Y) \right\} \mathrm{d} p _ {1} \\ & + C (x, y) \mathrm{d} p _ {2} \end{array}
$$

where

$$
\begin{array}{l} R (x, y) = \frac {\partial (G + p _ {2} C)}{\partial x} \quad \text { and } \\ S (x, y) = \frac {\partial (G + p _ {2} C)}{\partial y} \end{array}
$$

Now, since $x - X - A \left( y - Y \right) = 0 .$ , and $C ( x , \ y )$ <sup>s</sup>0, we have,

$$
\begin{array}{r l} \mathrm{d} L _ {G} (x, y, p _ {1}, p _ {2}) & = \left\{R (x, y) + p _ {1} \right\} \mathrm{d} x \\ & + \left\{S (x, y) - A p _ {1} \right\} \mathrm{d} y \end{array}
$$

The ISO calculates the values of $R ( x , \ y )$ and $S ( x , y )$ at $x = X , \ y = Y ,$ and $p _ { 2 } = P .$ . If $R \neq 0$ , the ISO chooses the following equation.

$$
A = - \frac {S}{R}
$$

With this choice of A by the ISO, the resulting differential of the Genco’s Lagrangian function evaluated at $x = X , \ y = Y , \ p _ { 1 } = - R$ , and $p _ { 2 } = P$ yields zero! Since G and C are convex, this first-order condition is sufficient to guarantee that is the unique solution for the minimization of G subject to the constraint of C <sup>s</sup> 0. If R <sup>s</sup> 0, the $\mathrm { I S O ^ { \circ } s }$ decision variable does not affect the Genco’s Lagrangian function at the ISO’s desired operating point and the incentive strategy cannot induce the Genco to choose $y = Y .$ . Thus, except for the AgenericB case where $R = 0 ;$ , the incentive strategy of the ISO is effective.

The concept of incentive strategies can be extended to situations that involve more than one Genco. However, in this case, an important question that needs to be answered as a part of the optimization process is the nature of interaction among the various Gencos. For example, the Gencos may choose to cooperate among themselves and implement a Pareto-type non-inferior solution. Or they may elect Ž . not to cooperate among themselves and implement a Nash-type solution. This issue is very important from the $\mathrm { I S O ^ { \circ } s }$ perspective whenever it has to deal with a multitude of Gencos. As mentioned earlier, an important objective for the ISO may be to reduce the chance of gaming among the Gencos. The main purpose of using incentive strategies in this case would be to induce the Gencos to agree to cooperate in order to achieve an overall optimal operation of the grid.

Let us, for illustration purposes, assume that there are N Gencos in the incentive problem discussed earlier. Let the decision variable of the ISO be a scalar x as before and let $y _ { 1 } , ~ y _ { 2 } , \ldots , ~ y _ { N }$ denote the decision variables of the Gencos, respectively. The objective function of the ISO is now $I ( x , y _ { 1 } , y _ { 2 } , . . . ,$ $y _ { N } )$ and the objective functions of the Gencos are $G _ { n } ( x , \ y _ { 1 } , \ y _ { 2 } , . . . , \ y _ { N } )$ for $n = 1 , \ldots , \ N .$ . The final choice of variables must satisfy the grid constraints $C ( x , \ y _ { 1 } , \ y _ { 2 } , . . . , \ y _ { N } ) = 0 $ As before, let $x = X , \{ y _ { n }$ $= Y _ { n } , n = 1 , \ldots , N \}$ and $p = P$ be the unique set of variables that minimize the ISO’s Lagrangian function $L _ { I } ( x , y _ { 1 } , y _ { 2 } , . . . , y _ { N } )$ . It is this solution that the ISO now wishes to induce the Gencos to choose. However, inducing a multitude of Gencos is more difficult than inducing one Genco! Following an analysis similar to the one-Genco problem, a possible simple incentive function in this case would be,

$$
x = X + \sum_ {n = 1} ^ {N} A _ {n} (y _ {n} - Y _ {n})
$$

where, as before, the $A _ { n } ^ { \phantom { \dagger } } \mathbf { s }$ are constants to be determined by the ISO.

Let us first consider the case where the Gencos wish to implement a Pareto solution among themselves. This would necessitate minimizing an objective function that is a convex combination of the individual objective functions, appended with the grid constraint and the above incentive function. That is:

$$
\begin{array}{l} L _ {G} \big (x, y _ {1}, y _ {2}, \dots , y _ {N} \big) \\ = \sum_ {n = 1} ^ {N} \alpha_ {n} G _ {n} \big (x, y _ {1}, y _ {2}, \dots , y _ {N} \big) \\ + p _ {1} \Bigg \{x - X - \sum_ {n = 1} ^ {N} A _ {n} \big (y _ {n} - Y _ {n} \big) \Bigg \} \\ + p _ {2} C \big (x, y _ {1}, y _ {2}, \dots , y _ {N} \big) \end{array}
$$

In the above expression, the scalars $\alpha _ { n }$ must satisfy $\textstyle \sum _ { n = 1 } ^ { N } \alpha _ { n }$ and $\alpha _ { n } \geq 0$ . For each choice of these $\alpha _ { n }$ scalars, the proper choice of the constants $A _ { n }$ by the ISO can be easily determined to be,

$$
A _ {n} = - \frac {S _ {n}}{R}
$$

where

$$
\begin{array}{l} R = \frac {\partial \left(\sum_ {i = 0} ^ {N} \alpha_ {i} G _ {i} + p _ {2} C\right)}{\partial x} \quad \text { and } \\ S _ {n} = \frac {\partial \left(\sum_ {i = 0} ^ {N} \alpha_ {i} G _ {i} + p _ {2} C\right)}{\partial y _ {n}} \end{array}
$$

All these expressions must be evaluated at the ISO’s desired solution. It is interesting to observe that in this case, each $A _ { n }$ will be a function of the $\alpha _ { n }$ scalars. By leaving the choice of these scalars to the end, the ISO has the capability of inducing the Gencos to implement a Pareto solution of its own choosing. In other words, the ISO is able to coordinate the nature of cooperation among the Genco’s in the best way that benefits the operation of the entire system.

The other, and less desirable, situation is when the Gencos are in a competitive environment and end up implementing a Nash-type solution among themselves. In this case, each Genco will pursue a strategy of protecting itself against possible cheating by the other Gencos. A Nash solution $\{ y _ { I } ^ { * } , y _ { 2 } ^ { * } , \ldots , y _ { N } ^ { * } \}$ must satisfy the inequalities:

$$
\begin{array}{l} G _ {n} \big (  x, y _ {1} ^ {*}, y _ {2} ^ {*}, \ldots , y _ {n} ^ {*}, \ldots , y _ {N} ^ {*}   \big) \\ \leq G _ {n} \big (  x, y _ {1} ^ {*}, y _ {2} ^ {*}, \ldots , y _ {n}, \ldots , y _ {N} ^ {*}   \big) \end{array}
$$

for $n = 1 , \ 2 , \ldots , \ N ;$ where x is governed by the incentive function described above. The proper choice of $A _ { n }$ by the ISO in this case can be shown to be,

$$
A _ {n} = \frac {S _ {n}}{R _ {n}}
$$

where $R _ { n }$ and $S _ { n }$ are given by the expressions:

$$
R _ {n} = \frac {\partial (G _ {n} + p _ {2} C)}{\partial x} \quad \text { and } \quad S _ {n} = \frac {\partial (G _ {n} + p _ {2} C)}{\partial y _ {n}}.
$$

As before, these expressions must be evaluated at the ISO’s desired solution. Note that in this case, the ISO has less flexibility in its ability to influence the Gencos’ behavior. The ISO has no parameters, such as the $\alpha _ { n }$ scalars, that it can manipulate to influence the final outcome. We should mention that in the case where the ISO is using incentive controls, this solution would not have much appeal for the Gencos. One of the main advantages of the Nash solution is in its ability to protect each Genco against cheating by the other Gencos. However, the ISO can easily provide such a guarantee by properly using its incentive controls as has been demonstrated earlier. In fact, gaming among the Gencos can be reduced to a minimum.

In a realistic grid model, market conditions and the ISO’s and Gencos’ ability to influence the system will vary as a function of time. Dynamic decision making, in this case, typically would require a mathematical model to characterize the evolution of the entire power grid as a function of time. If x tŽ . is used to denote the state vector of the system, it then would evolve according to a differential equation that is controlled simultaneously by the ISO and Gencos. That is:

$$
\frac {\mathrm{d} x}{\mathrm{d} t} = f \big (x, u, v _ {1}, v _ {2}, \ldots , v _ {N}, t \big)
$$

where $u ( t )$ and $v _ { 1 } ( t ) , \ldots , v _ { N } ( t )$ are the control variables of the ISO and Gencos, respectively, and t is time. The ISO and Gencos typically have integrated objective functions defined over a finite time horizon <sup>w</sup> <sup>x</sup> 0, T that they wish to minimize:

$$
J _ {I} (u, v _ {1}, \dots , v _ {N}) = \int_ {0} ^ {T} I (x, u, v _ {1}, \dots , v _ {N}, t) d t
$$

and

$$
J _ {G _ {n}} \big (u, v _ {1}, \dots , v _ {N} \big) = \int_ {0} ^ {T} G _ {n} \big (x, u, v _ {1}, \dots , v _ {N}, t \big) \mathrm{d} t
$$

$$
f o r \quad n = 1, \ldots , N
$$

Following a similar analysis as in the static case, the ISO first minimizes $J _ { I } ( u , v _ { 1 } , \ldots , v _ { N } )$ as if it has complete control over the choices of u and $v _ { 1 } , \ldots ,$ $v _ { N }$ . This would be solved using standard optimal control theory. Let U and $v _ { 1 } , \ldots , v _ { N }$ be the unique functions that minimize $J _ { I } ( u , \ v _ { 1 } , \ldots , \ v _ { N } )$ . Now the ISO wants to induce the Gencos to choose $v _ { n } = V _ { n }$ for $n = 1 , \ldots , \ N .$ To achieve this, the ISO will implement a strategy $u = h ( v _ { 1 } , \ldots , \ v _ { N } )$ where the incentive function h is to be determined by the ISO in such a way that the minimization of $J _ { G _ { n } } ( h ( v _ { 1 } , \ldots , v _ { N } ) , v _ { 1 } , \ldots , v _ { N } )$ by the Gencos will yield $v _ { n } = V _ { n }$ . Since the objective function for each Genco depends on the control choices of all Gencos, the ISO has to take into consideration the resulting interaction among all the Gencos. As in the static case, an objective for the ISO would be to induce the Gencos to cooperate and achieve a non-conflicting solution. An example of a simple incentive function h is $\begin{array} { r } { u = U + \sum _ { n = 1 } ^ { N } A _ { n } ( v _ { n } - V n ) } \end{array}$ where $A _ { 1 } , \ldots , ~ A _ { N }$ are appropriate functions to be determined by the ISO. In the dynamic case, however, open-loop and feedback strategies need to be considered and the functions $A _ { n }$ will be different in each of these cases. In the open loop case, the controls u and $v _ { 1 } , \ldots , v _ { N }$ and the functions $A _ { n }$ will all be functions of time only, whereby in the feedback case, these will be functions of time and the state x tŽ ..

## 2.3. Diffusing horizontal market power

In the literature, it has been pointed out that although there is equal access to the transmission network, there remains substantial opportunity to exercise horizontal market power. Individual transmission line constraints can prevent additional generation from some buses and thus prevent free competition to prevail. Under the present rules of the grid operation, generation providers may purchase transmission capacity rights as transmission congestion contracts TCC . Thus a provider that holds a TCCŽ . on a specific transmission line may receive revenues corresponding to the capacity associated with the TCC times the price differential between the buses connected to the transmission line. In the process of optimizing its total profits, an energy provider may cause some transmission lines to be congested.

Hogan 7,8 has modeled this bulk power market,<sup>w</sup> <sup>x</sup> without leadership of the grid operator, as an oligopoly. The resulting market price is higher than the competitive benchmark price. A goal of the grid operator is to design incentives so that the resulting market prices correspond to perfect competition prices in the ideal case. If the perfect competition prices cannot be achieved, the market prices should be as close to the perfect competition prices as possible.

The market power model proposed here seeks to define the strategy that a grid operator should implement for achieving a virtually perfect competition market. If each energy provider uses the same optimization procedure while assuming that the other energy providers have fixed strategies, the equilibrium market price will be a Cournot equilibrium. The challenge for the grid operator is to design the incentives so that the Cournot equilibrium prices are equal to the perfect competition prices.

A simplified model of two energy providers will be considered. One energy provider will be assumed to be a dominant provider DP which owns a larger share of the generating units of the assumed power market with two providers, and another provider IP representing other power producers. Let us assume the power market model has $" n "$ buses and $" m "$ lines.

$P _ { \mathrm { D P } }$ and $P _ { \mathrm { I P } }$ are the n-vectors of loads at each of the n buses.

$P G _ { \mathrm { D P } }$ and $P G _ { \mathrm { \tiny { I P } } }$ are the n-vectors of generators at each of the n buses.

Y denotes the n-vector of net injections at each of the n buses.

$P _ { \mathrm { i j } } ( \mathrm { m i n } )$ and $P _ { \mathrm { i j } } ( \mathrm { m a x } )$ are the lower and upper bounds on the real power line flows.

BŽ . Ž . . and C . are the benefit and cost functions for load and generation.

The benefit function BŽ .. depends on the energy sold and on the price of the energy. It is the area under the demand curves. The cost function CŽ .. represents the area under the supply curves. TD is a contract on transmission capacity rights that defines a vector of net loads and pays $p ^ { \prime } \mathrm { T D }$ for DP. TI is similarly defined for IP.

The grid operator will be considered as the ISO and the two energy providers will be the Gencos in a formulation. The control variables for the grid operator are TD and TI. The control variables for the energy providers are their generations and loads. A powerful type of control for the grid operator is to allow TD and TI to be incentive functions of the generations and the loads of the energy providers. Affine functions will be considered for simplicity, i.e., TD and TI will be linear combinations of constants and Genco control variables with proportionality constants.

The optimization problem for DP is to maximize

$$
\left(B _ {\mathrm{DP}} \left(\boldsymbol {P} _ {\mathrm{DP}}\right) - C _ {\mathrm{DP}} \left(\boldsymbol {P} \boldsymbol {G} _ {\mathrm{DP}}\right)\right) + \boldsymbol {p} ^ {\prime} \mathrm{TD}
$$

with respect to $P _ { \mathrm { D P } } , P G _ { \mathrm { D P } }$ . This maximization is subject to the assumption that the strategy of IP is fixed and that the grid operator provides the value of TD or its functional dependence on $\mathrm { D P ^ { \bullet } s }$ control variables. Furthermore, the maximization is subject to power flow problem 7–10,15,17,18,28 :<sup>w</sup> <sup>x</sup>

$$
\left[ \mathbf {Y} \right] - \left[ \mathbf {A} ^ {T} \right] \left[ P _ {\mathrm{lineflow}} \right] = 0
$$

$$
\Sigma \left(\boldsymbol {P} _ {\mathrm{DP}} - \boldsymbol {P G} _ {\mathrm{DP}}\right) + \Sigma \left(\boldsymbol {P} _ {\mathrm{IP}} - \boldsymbol {P G} _ {\mathrm{IP}}\right) = \boldsymbol {Y}
$$

Ž . Net input balance equation

where A denotes the Ž . m by n incidence matrix.

There is a similar optimization formulation for the IP player, under the assumption that the control strategy of DP is fixed, and the grid operator provides TI.

The above two problems need to be solved simultaneously for the scheduled transmission systems conditions. The equilibrium solution provides the optimum amount of power to be generated by DP and IP to share in meeting the total load. It also provides the resulting market prices at the n buses. The ISO’s challenge is to design TD and TI so that the resulting price vector is as close to the perfect competition price vector.

The DP and IP optimizations can be carried out using nonlinear programming. The first step is to form Lagrangian functions, where p is the Lagrange multiplier vector for the net input balance equality constraint. Thus, p appears linearly in two places in each of the Lagrangian functions. One is in $p ^ { \prime } \mathrm { T D }$ orŽ $\pmb { p } ^ { \prime } \mathrm { T I } )$ and another is in the appended equality constraint. The Kuhn–Tucker conditions for the simultaneous maximization of the two Lagrangian functions will contain the parameters in the design of TD and TI. The grid operator will choose the parameters in such a way that the Kuhn–Tucker conditions both for DP and for IP are satisfied when the price vector equals the ideal perfect competition price vector.

## 3. Incentive control of ancillary services

Ancillary services could be categorized as following:

1. regulation or AGC,

2. spinning reserve SR , Ž .

3. non-spinning reserve NSR , Ž .

4. replacement reserve RR .Ž .

ISO runs markets for ancillary services in order to assure the power system security and reliability with respect to FERC standards. ISO wants to make sure that there are always sufficient generation resources to dispatch in case of generator, line or transformer outages or other contingencies, as well as imbalances caused by forecast errors. The reserve contracts are done using a two-part pricing system. First, the accepted generators for the ancillary market are paid a fixed fee for keeping part of their capacity available for dispatch. Second, if this available capacity is used, then they will receive a second payment corresponding to the ancillary market-clearing price 3,26 .<sup>w</sup> <sup>x</sup>

The definition and conditions constrains , for the Ž . four categories mentioned above, in order to bid into the ancillary service market are as follows.

AGC is the regulating capability, under automatic generation control, that responds in an effort to continuously balance the ISO control area’s supply resources with minute-to-minute load variations in order to meet the NERC control performance standards.

SR is a resource capacity synchronized to the system, which is able to immediately begin to supply energy or reduce demand, fully available within 10 min, and able to be sustained for a period of at least 30 min to provide first contingency protection.

NSR is a resource capacity non-synchronized to the system, which is able to supply energy or reduce demand, fully available within 10 min, and able to be sustained for a period of at least 30 min to provide first contingency protection.

Transmission loss is an inherent, unavoidable consequence of delivering electric energy. The transmission losses are usually paid by the load distribution entities Disco based on their contribution toŽ . the system losses. The uncompensated transmission losses will depress the system frequency, because they represent the mismatch between generation and total effective load. Therefore, transmission loss compensation could be bid in the AGC market in a similar way 3,26 .<sup>w</sup> <sup>x</sup>

To reduce the chance of gaming the market, ISO has imposed cost-based cap price CBCP for Gen- Ž . cos who bid into the ancillary reserve markets. Gencos are not permitted to bid above the capped levels, and if the market-clearing price is higher than CBCP, the Gencos will only receive compensation up to the CBCP level. This creates a situation where the Gencos benefit from driving their bids down to their marginal costs 26 .<sup>w</sup> <sup>x</sup>

By estimating the zonal market clearing prices of energy and ancillary services shadow prices of en-Ž ergy and ancillary services , the ISO could solve the. following optimization problem to minimize the expected costs of energy and ancillary reserves for the power consumers:

$$
\min _ {p, r, u} \left\{\sum_ {k = 1} ^ {2 4} \sum_ {n = 1} ^ {m} \operatorname{mcpe} (k) p _ {n} (k) u _ {n} ^ {e} (k) \right.
$$

$$
\left. + \operatorname{mcpr} (k) r _ {n} (k) u _ {n} ^ {r} (k) \right\}
$$

Subject to:

$$
\sum_ {n = 1} ^ {m} p _ {n} (k) u _ {n} ^ {e} (k) = P _ {t} (k), \quad \text { for } \quad k = 1, \dots , 2 4
$$

$$
\begin{array}{l} \sum_ {n = 1} ^ {m} r _ {n} (k) u _ {n} ^ {r} (k) \geq R _ {t} (k), \quad \text { for } \quad k = 1, \dots , 2 4 \\ p _ {n} ^ {\min} \leq p _ {n} (k) \leq p _ {n} ^ {\max} \\ 0 \leq r _ {n} (k) \leq \min \left\{r _ {n} ^ {\max}, p _ {n} ^ {\max} - p _ {n} (k) \right\} \\ u _ {n} ^ {\mathrm{e}} (k) = \left\{ \begin{array}{l l} 0 & \text { if } \operatorname{Bid} _ {n} ^ {\mathrm{e}} (k) > \operatorname{mcpe} (k) \\ 1 & \text { if } \operatorname{Bid} _ {n} ^ {\mathrm{e}} (k) \leq \operatorname{mcpe} (k) \end{array} \right. \\ u _ {n} ^ {\mathrm{r}} (k) = \left\{ \begin{array}{l l} 0 & \text { if } \operatorname{Bid} _ {n} ^ {\mathrm{r}} (k) > \operatorname{mcpr} (k) \\ 1 & \text { if } \operatorname{Bid} _ {\mathrm{n}} ^ {r} (k) \leq \operatorname{mcpr} (k) \end{array} \right. \end{array}
$$

Where, $u _ { n } ^ { \mathrm { e } } ( k ) = \mathrm { u n i t }$ commitment of generator-n in the energy market; $u _ { n } ^ { \mathrm { r } } ( k ) = \mathrm { u n i t }$ commitment of generator-n in the ancillary reserve market; $m =$ number of generators who participant in the energy and reserve markets; $P _ { t } ( k ) =$ estimated power system demand at hour k; R kŽ .<sup>s</sup>estimated power system ancillary reserve requirement at hour k; mcpeŽ . k <sup>s</sup> expected clearing price of energy; mcprŽ . k <sup>s</sup>expected clearing price of ancillary reserve; $\mathbf { B i d } _ { n } ^ { \mathrm { e } } = \mathbf { G e n c o } { - n }$ energy bid at hour $k ; { \mathrm { B i d } } _ { n } ^ { \mathrm { r } } =$ Genco-n ancillary reserve bid at hour $k ; ~ p _ { n } ( k ) =$ Genco-n energy schedule for hour k; $r _ { n } ( k ) = \mathrm { G e n c o - }$ n ancillary reserve schedule for hour k.

The ISO should solve the above Kuhn–Tucker optimization problem over a 24-period load cycle in order to minimize the power consumer costs. After finding the optimal energy and ancillary reserve schedules for the next 24-h, the ISO could propose economic incentive functions EIF to all day-aheadŽ . energy and ancillary reserve market participants Ž . Gencos . The market participants could use these incentive functions to maximize their expected benefit functions payoff functions in dynamic games Ž . such as deregulated energy and ancillary reserve markets.

A proposed EIF is as follows:

$$
\begin{array}{l} S (k) = \operatorname{mcpe} (k) \big [ p (k) - p ^ {*} (k) \big ] u ^ {\mathrm{e}} (k) \\ \qquad + \operatorname{mcpr} (k) \big [ r (k) - r ^ {*} (k) \big ] u ^ {\mathrm{r}} (k), \end{array}
$$

for $k = 1 , \ldots , 2 4$

where, $p ^ { \ast } ( k ) = \mathrm { o p t i m a l }$ energy schedule at hour k from ISO optimization process; $r ^ { * } ( k ) = \mathrm { o p t i }$ mal ancillary reserve schedule at hour k from ISO optimization process; $u ^ { \mathrm { e } } ( k ) = \mathrm { o p t i m a l }$ energy unit commitment at hour k from ISO optimization process; <sup>r</sup> u kŽ . <sup>s</sup> optimal ancillary reserve unit commitment at hour k from ISO optimization process.

If each Genco uses the proposed EIF in order to define its optimal bids and schedules for the dayahead energy and ancillary reserve markets, then the difference between the Genco’s and ISO’s optimal solutions will be negligible. The proposed method for incentive control of energy and ancillary services in deregulated energy markets is known as the Stackelberg strategy in dynamic game theory. In the proposed method of controlling ancillary services, ISO Ž . the market maker sets the optimal schedules and market clearing prices, and Gencos the price takersŽ . will define their optimal bids and schedules with respect to the ISO’s EIF. The proposed incentive control method could increase the efficiency of the deregulated energy and ancillary reserve markets by giving important economic signals to the market participants at each trading hour.

## 4. Conclusion

This paper presents a proposed framework for market monitoring and incentive control of ancillary services. The proposed control formulated based on developing a frequency LFC market, a RL market and a BL market. The above market will be controlled by the ISO with a predefined incentive function that all market players must use to compute the cost of their energy to be offered to the respective markets. The EIF, such as the one proposed in this paper, will give economic signals to the market participants. If they include these functions in their bid<sup>r</sup>schedule optimization process for the day-ahead markets, the optimal performance of the power system and maximum efficiency of the energy and ancillary reserve markets are guaranteed by the ISO.

## References

1 A. Abur, A. Keyhani, H. Bakhtiari, Autoregressive filters for the identification and replacement of bad data in power system state estimation, IEEE Transactions on Power Systems 2.3 1987 552–560, Aug. .Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 Basar, Tamer and Jose B. Cruz, Jr. AConcepts and methods in multi-person coordination and control.B Optimization and Control of Dynamic Operational Research Models. Ed. S.G.

<sup>w</sup> <sup>x</sup> 3 K.W. Cheung, P. Shamsollahi, S. Asteriadis, Functional requirements of energy and ancillary service dispatch for the interim ISO New England electricity market, IEEE–PES Annual Conference, NY, Feb., 1999.

<sup>w</sup> <sup>x</sup> 4 J.B. Cruz Jr., Survey of concepts in hierarchical decisionmaking, Proc. Fourth International Conf. on Analysis and Optimization of Systems, Le Chesnay, France, December, 1980, pp. 384–396, Invited .Ž .

<sup>w</sup> <sup>x</sup> 5 J.B. Cruz Jr., Stackelberg strategies for hierarchical control of large scale systems, Proc. Second Workshop on Hierarchical Control, Warsaw, Poland, June, 1978, pp. 341–355, Ž .Invited .

<sup>w</sup> <sup>x</sup> 6 G. Gross, D.J. Finlay, G. Deltas, Strategic bidding in electricity generation supply markets, IEEE–PES Annual Conference, NY, Feb., 1999.

<sup>w</sup> <sup>x</sup> 7 William W. Hogan, A market power model with strategic interaction in electricity networks, The Energy Journal 18.4 Ž . 1997 .

<sup>w</sup> <sup>x</sup> 8 William W. Hogan, Contract networks for electric power transmission, Journal of Regulatory Economics 4.3 1992 Ž . 211–242.

<sup>w</sup> <sup>x</sup> 9 M.D. Ilic, Performance-based value of transmission services for competitive energy management, Proc. 26th North American Power Symposium NAPS , Kansas State Univ., Man-Ž . hattan, KS, 26–27 Sept. 1994.

<sup>w</sup> <sup>x</sup> 10 M. Ilic, E.H. Allen, Z. Younes, Transmission scarcity: who pays? The Electricity Journal 1997 38–49, July. Ž .

<sup>w</sup> <sup>x</sup> 11 H.R. Kassaei, A. Keyhani, T. Woung, A hybrid fuzzy, neural network bus load modeling and predication, IEEE Transactions on Power Systems PE 021-PWRS-0-06 1998 inŽ . Ž press ..

<sup>w</sup> <sup>x</sup> 12 A. Keyhani, Development of an interactive power system research simulator, IEEE Transactions on Power Apparatus and Systems 103.3 1984 MarchŽ . Ž . <sup>r</sup>April .

<sup>w</sup> <sup>x</sup> 13 A. Keyhani, Dynamic system load generation control using variable pressure steam generators, IEEE Transactions on Power Apparatus and Systems 75.2 1975 Nov.Ž . Ž . <sup>r</sup>Dec. .

<sup>w</sup> <sup>x</sup> 14 A. Keyhani, One-step-ahead load forecasting for on-line application, IEEE Power Apparatus and Systems 75.1 1975Ž . Ž . July<sup>r</sup>Aug. .

<sup>w</sup> <sup>x</sup> 15 A. Keyhani, A. Abur, S. Hao, Evaluation of power flow techniques for personal computers, IEEE Transactions on Power Systems 4.2 1989 Aug. .Ž . Ž .

<sup>w</sup> <sup>x</sup> 16 A. Keyhani, El-Abiad, A real-time modeling techniques for application to automatic generation control, IEEE Transactions on Power Apparatus and Systems 95.1 1976Ž . Ž .Nov.<sup>r</sup>Dec. .

<sup>w</sup> <sup>x</sup>17 A. Keyhani, S. Hao, W.R. Wagner, A rule based approach for construction a local network model for decentralized voltage control, Electric Power Systems Research Journal 16 Ž . 1989 .

<sup>w</sup> <sup>x</sup> 18 A. Keyhani, S.M. Mir, On-line weather-sensitive and industrial group bus load forecasting for microprocessor-based applications, IEEE Transactions on Power Apparatus and Systems 102.12 1983 3868–3876, Dec. . Ž . Ž .

<sup>w</sup> <sup>x</sup> 19 A. Keyhani, A.B. Proca, A virtual testbed for instruction and design of permanent magnet machines, IEEE Transactions on Power Systems PE-273-PWRS-0-07 1998 .Ž .

<sup>w</sup> <sup>x</sup> 20 F.C. Schweppe, R. Bohn, R. Tabors, M. Caramanis, Spot Pricing of Electricity, Kluwer Academic Publishing, Boston, 1988.

<sup>w</sup> <sup>x</sup> 21 F.C. Schweppe, M.C. Caramanis, R.D. Tabors, Evaluation of spot price based electricity rates, IEEE Transaction of Power Apparatus and Systems PAS-104.7 1985 July .Ž . Ž .

<sup>w</sup> <sup>x</sup> 22 F.C. Schweppe, R.D. Tabors, J.L. Kirtley, Homeostatic control for electric power usage, IEEE Spectrum 1982 July.Ž .

<sup>w</sup> <sup>x</sup> 23 M. Simaan, J.B. Cruz Jr., A Stackleberg solution for games with many players, IEEE Trans. on Automatic Control AC-18 Ž . Ž . 1973 June .

<sup>w</sup> <sup>x</sup> 24 M. Simaan, J.B. Cruz Jr., Additional aspects of the Stackelberg strategy in nonzero-sum games, Journal of Optimization Theory and Applications 11.6 1973 June .Ž . Ž .

<sup>w</sup> <sup>x</sup> 25 M. Simaan, J.B. Cruz Jr., On the Stackelberg strategy in nonzero-sum games, Journal of Optimization Theory and Applications 11.5 1973 May .Ž . Ž .

<sup>w</sup> <sup>x</sup> 26 P. Skantze, J. Chapman, Price dynamics in the deregulated California energy market, IEEE–PES Annual Conference, NY, Feb., 1999.

<sup>w</sup> <sup>x</sup>27 C-Li Tseng, S.S. Oren, A.J. Svoboda, R.B. Johnson, Pricebased spinning reserve requirements in power system scheduling, PSERC 1998 .Ž .

<sup>w</sup> <sup>x</sup>28 W.R. Wagner, A. Keyhani, S. Hao, T.C. Wong, A rule-based approach to decentralized voltage control, IEEE Transactions on Power Systems 5.2 1990 643–651, May .Ž . Ž .

<sup>w</sup> <sup>x</sup> 29 A. Zobian, M.D. Ilic, Unbundling of transmission and ancillary services: Part II. Cost-based pricing framework, IEEE Transactions on Power Systems 12 2 1997 549–556, Ž . Ž . May.

![](/api/attachments/AXQ5B8WU/fulltext/images/b12e3e2ad40bf3d46611da68f21b1c168b785fce4069a0d989b22f837cf19afb.jpg)

Ali Keyhani is a fellow of IEEE and a recipient of the Ohio State University College of Engineering Research Award for 1989 and 1999. He established the Ohio State University Mechatronic graduate program in 1995, and he is the director of the Department of Electrical Engineering Mechatronic Systems Laboratory. His research interests are in the areas of electromechanical systems, power systems control and operation, power electronics, design of electric ma-

chines and parameter estimation. Dr Keyhani is the Chairman of the Electric Machinery Committee and the past Editor of IEEE Transactions on Energy Conversion. He has been a consultant to Accuray, Combustion Engineering, Asea Brown Boveri, TRW Controls, Harris Controls, Liebert, Delphi Automotive Systems, Mahab Engineering, IRD, and Foster Wheeler Engineering. He has authored many papers in the IEEE Transactions on control of power systems, machine modeling, parameter estimation, power electronic systems, design of virtual and testbeds for variable speed drive systems.

![](/api/attachments/AXQ5B8WU/fulltext/images/3453afcd360ebfd42917314ad00f56e2ed81bcbcc6f66c5b76e0339eae762bc9.jpg)

Jose B. Cruz, Jr. is the Howard D. Winbigler Chair in Engineering, and Professor of Electrical Engineering at the Ohio State University OSU . HeŽ . received his BS summa cum laude from the University of the Philippines in 1953, SM from the Massachusetts Institute of Technology in 1956 and the PhD from the University of Illinois in 1959, all in electrical engineering. He served as Dean of the College of Engineering at OSU from 1992 to 1997, Professor of

![](/api/attachments/AXQ5B8WU/fulltext/images/9f60f8a70f7205512f6de499760704af935ed3f56852ebc6a50c8b58633a8066.jpg)

Marwan A. Simaan received the Ph.D. degree in Electrical Engineering from the University of Illinois at Urbana-Champaign in 1972 and did postdoctoral work at the Coordinated Science Laboratory at the University of Illinois until 1974. In 1976 he joined the Department of Electrical Engineering at the University of Pittsburgh where he is currently the Bell of PA<sup>r</sup>Bell Atlantic Professor. He served as chair of the department from 1991 to 1998. He has held research

Electrical and Computer Engineering at the University of California in Irvine UCI from 1986 to 1992, and at the University ofŽ . Illinois from 1965 to 1986. Dr Cruz was elected as a member of the National Academy of Engineering in 1980. He is also a Fellow of the Institute of Electrical and Electronics Engineers; recipient, Curtis W. McGraw Research Award of the American Society for Engineering Education 1972; recipient, Halliburton Engineering Education Leadership Award, 1981; distinguished member, IEEE Control Systems Society, designated in 1983; recipient, IEEE Centennial Medal, 1984; recipient, IEEE Richard M. Emberson Award, 1989; Fellow, American Association for the Advancement of Science elected 1989; recipient, ASEE Centennial Medal, 1993; and recipient, Richard E. Bellman Control Heritage Award, American Automatic Control Council in 1994.

and consulting positions in industry including the English Electric Leo-Marconi Computers Ltd.; Bell Telephone Laboratories; Shell Development Company; Gulf R&D Company; and ALCOA Laboratories. His research interests are mainly in the areas of control and signal processing. He has edited four books and written more than 225 articles in journals, books, conference proceedings and technical reports.

Dr. Simaan is a member of the US National Academy of Engineering and a Fellow of the AAAS and IEEE. He is coeditor of the Journal of Multidimensional Systems and Signal Processing Ž . Kluwer . He currently serves on the editorial boards of a number of journals including the IEEE Proceedings and the Journal of Optimization Theory and Applications Ž . Plenum .

Dr. Simaan received three Best Paper Awards 1985, 1988, andŽ 1999 and a Distinguished Alumnus Award from the department. of Electrical and Computer Engineering at the University of Illinois at Urbana-Champaign 1995 . He is a member of AAAI,Ž . ASEE and SEG. He is a registered Professional Engineer in Pennsylvania and he serves as an Electrical Engineering program Evaluator for the Accreditation Board for Engineering and Technology ABET .Ž .
