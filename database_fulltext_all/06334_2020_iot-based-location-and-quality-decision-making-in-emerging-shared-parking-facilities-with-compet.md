---
otero_id: 6334
otero_key: "B2PZDGA3"
title: "IoT-based location and quality decision-making in emerging shared parking facilities with competition"
authors: "Peng Wu; Feng Chu; Nasreddine Saidani; Haoxun Chen; Wei Zhou"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113301"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# IoT-based location and quality decision-making in emerging shared parking facilities with competition

Peng Wu<sup>a</sup>, Feng Chu<sup>a,b,⁎</sup>, Nasreddine Saidani<sup>c</sup>, Haoxun Chen<sup>d</sup>, Wei Zhou<sup>e,f</sup>

<sup>a</sup> School of Economics & Management, Fuzhou University, 350116 Fuzhou, China

<sup>b</sup> Laboratory IBISC, Univ Evry, University of Paris-Saclay, 91025 Evry, France

<sup>c</sup> Company AZAP, 75008 Paris, France

<sup>d</sup> Laboratory LOSI, University of Technology of Troyes, 10300 Troyes, France

<sup>e</sup> Information & Operations Management, ESCP Europe, Paris, France

<sup>f</sup> Transportation Engineering, School of Naval Architecture, Ocean & Civil Engineering, Shanghai Jiaotong University, Shanghai, China

## A R T I C L E I N F O

Keywords: Sharing economy Shared parking Electric vehicle Sharing decision support

## A B S T R A C T

Shared parking firms ofer a double-sided platform for parking space sharing. Many of these firms provide diferentiated service levels to both suppliers and buyers. This new phenomenon in the parking industry materialized thanks to recent innovations in IoT-enabled automation and electric vehicle charging technologies. We study shared parking firms. Specifically, we formulate the firm's location and quality decision problem by using a multiplicative interaction model with competition. A non-cooperative game renders the optimized quality levels and location selections at Nash equilibrium in the presence of competition. We illustrate managerial insights with a small-sized problem. For industry practitioners, we propose a tailored branch and bound based exact algorithm and a problem-specific genetic algorithm for large-sized problems. Simulated computational results confirm the effectiveness and efficiency of the proposed shared-parking decision support model.

## 1. Introduction

New transportation business models have emerged in recent years, thanks in part to increasing popularity of sharing economy and related enabling technologies. Companies that provide shared transportation and parking services such as Uber, Lyft, Onepark, and Pavemint have greatly reshaped the transportation economy and civil infrastructure development in many countries. Moreover, an increasing number of property owners have started sharing their parking spaces or membership-exclusive parking facilities to the public via shared parking platforms. The benefits of sharing parking spaces include reduction in the overall parking space requirement and increased revenue for the property owners. With competition from existing public parking providers, emerging shared parking service providers face two strategic decisions that include (1) location selection and (2) service quality choice.

The first decision on location selection is an important classical problem for shared parking firms [1]. Facing competition, companies such as Onepark and Pavemint must consider where to add new shared parking spaces and/or build parking facilities along with an incentive policy and diferentiated service levels. The main business model involves incentivizing property owners to share their parking resources on the platform. At the same time, the platform owner also invests in these shared parking properties by providing automated equipment on site (e.g., check-in-out facilities, automated mechanics, video surveillance, sensors and EV charging devices). Unlike classical sharing economy platforms such as Uber or airBnb, there is a substantial (initial) investment requirement for shared parking platform to operate and grow.

The second decision on service quality level has not been considered in published literature on parking marketplace management, to the best of our knowledge. Indeed, it is not until recently that parking service quality has become an important decision because of advances in IoT and electric vehicle technologies. Most shared parking companies not only provide the platform that bridges buyers and suppliers, but also install check-point facilities, EV charging devices, sensors and surveillance equipments upon agreement with the parking space owner. This practice enables the shared parking company to diferentiate its service quality. This new phenomenon related to parking service quality choice raises many questions that largely remain unanswered, including its impact on the classical location problem, service quality decision problem, and pricing and competition strategy problems.

We study both the decision problems for a shared parking firm as a competitive location problem (CLP). The set of available parking facility locations is formed from shared private parking spaces. Service quality diferentiation is enabled by the installation of onsite equip ments/devices that are connected via an IoT-based sensor system in frastructure. This IoT-based system allows for tracking and tracing vehicles as well as provide information on connected parking facilities such as charging stations and various mechanical devices. It enables the service provider to design and diferentiate the quality levels of the parking facilities. On-site electric charging devices ofer various levels of charging speed/time. Video and sensor based surveillance of parking facility improves service quality in terms of parking security. Automated checkpoints with RFID and mobile payment facilities im prove convenience and help reduce customer wait time.

Existing studies on CLP for parking marketplace management mainly focus on the location decision. However, it is important to simultaneously consider service quality and facility location as both impact a firm's long-term market share. Considering only location may lead to sub-optimality, especially when service quality is measurable and can be controlled. Over the past few years, a number of articles on other industries (e.g., [2–8]) have addressed competitive facility location and design problems in a continuous space by taking into account the service quality decisions of facilities. The quality of a facility is usually determined by the facility size, variety, convenience, maintenance efort, technology level, and other case-specific factors. We consider parking service quality with similar factors. For example, with additional electric charging devices, service can be diferentiated by charging speed and quality. In addition, [9–11] considered competitive facility location and design in discrete space. The above studies generalize previous work on competitive facility location by simply assuming that the quality of the existing facilities as given. Although more realistic, response from existing competitors is not considered by any of these studies. As mentioned in [12], considering the response from competitors is a natural extension of CLP. Furthermore, we assume that the probability of a customer choosing a parking site is proportional to the utility of patronizing it. We then adopt a multiplicative interaction (MCI) model [13] to express the probability of a customer patronizing either a new parking site or an existing one.

The contributions of this study are summarized below.

i) We consider a new shared parking facility location and quality decision problem.

ii) We present a novel decision model for a shared parking firm that faces competition, competitors' reactions, and limited budget, by adopting the MCI model. The problem is shown to be NP-hard.

iii) We propose an iterative solution framework composed of two main phases (parking location and quality determination) to solve the proposed model. Given a set of new open parking facilities, the competitive decision process occurring among new and existing parking facilities is modeled as a non-cooperative game. The service quality of new and existing parking facilities is determined by the Nash equilibrium.

iv) We develop a tailored B&B algorithm and problem-specific genetic algorithm (GA)-based method to obtain the best set of open parking facilities. Computational results on 320 randomly generated in stances under different structures show the effectiveness and effi. ciency of the proposed approaches.

The remainder of the paper is structured as follows. We introduce and formulate the model in Section 2. In Section 3, we first present an iterative solution framework to solve the proposed problem. Two tailored iterative framework-based approaches: B&B algorithm and GA based method are developed. Numerical experiments are provided to draw managerial insights and to validate the efectiveness and eficiency of the proposed approaches in Section 4. We conclude and identify future research directions in Section 5.

## 2. The model

Although advanced technologies and decision support tools have been developed, today it is still considered analytically challenging to optimize location decision in a competitive environment. Competitive location problems may involve not only location decisions, but also other decisions such as quality design and/or pricing. Hotelling's pioneering work on duopoly in a linear market [14] provides an important foundation for today's research on competitive location. The competitive location problems can be categorized as in a continuous space or in a discrete space setting according to whether facilities are located on a plane or on a network (a set of discrete points). For competitive location in a continuous space, [15] studied a single facility location problem that considers competition from another facility. Later, finding the optimal location of a single new facility with the analysis of the market share function was discussed in [16,17]. [18] presented a geographic information system (GIS) based competitive location model for a single facility to be located in continuous space. [19] extended this by considering multiple competitive facilities and developed several heuristic algorithms. The earliest contributions to competitive location in discrete space were made by [20,21]. Following the work of [22,23], a number of studies have addressed discrete multi-facility location problems in the retail industry (e.g., [24], [25–27], [28–30]). Many highlighted competitive location models are available in the literature. We refer to the survey papers [31–34] for an overview.

A few published research articles consider competitors' responses in CLP. [35] is the first to consider a firm that chooses to build facilities in a network of either competitive or oligopolistic environment. An economic equilibrium model was developed to describe the competition on the network in terms of equilibrium prices, demands, production levels and shipments. A variational inequality was proposed to specify its equilibrium. [36] considered the location decision and quality design of a new facility in continuous space with the objective of maximizing facility profit. An interval Branch and Bound (B&B) based two-stage algorithm was developed as a solution. Later, [37] developed a game theoretic model to analyze a market situation with two firms entering a new market where customers consider one of the suppliers according to travel distance and service quality. Both firms maximize market share by deciding on the location on a plane and service quality. Recently, [38] established a bi-level programming model to deal with a Huf-like competitive location and design problem where the leader desires to locate a facility such that its profit is maximized after the competitor locates its facility. It is assumed that the follower also considers maximizing its own profit. These studies mainly focus on optimally locating a single or two new facilities and assume that the budget for opening facilities and improving service quality is unlimited. While none of the published CLP research address the parking facility and quality problem, we fill the void by considering CLP for solving the emerging shared parking problem.

In summary, we consider that a shared parking firm is to locate new parking facilities in a network and simultaneously determine the service quality of each parking site to maximize its total profit. In the network, there are existing parking facilities that belong to other parking service firms that may or may not be shared. We assume that these existing parking facilities can improve their quality to compete for market share with new ones but their locations are given and fixed because relocation is expensive. Both the entrant and the existing firm have limited budget. A customer is free to choose any parking to patronize, and two utility factors that include parking quality and travel cost afect her/his location decision. The probability of a customer choosing a parking site is proportional to the patronizing utility. We adopt a multiplicative interaction (MCI) model [13] to express the probability of a customer patronizing either a new parking site or an existing one. Note that parking owners/members do not pay for using his/her own parking facilities.

![](/api/attachments/B2PZDGA3/fulltext/images/b2d4acd4428e2a5042a6e10da5f17cf733739235bb3f512b1a76729743696ed9.jpg)  
Fig. 1. Shared parking location selection with discrete demand points.

## 2.1. Problem description

Let $\ G \ = \ ( N , A )$ be a network that includes a set of nodes $N = P \cup C \cup D$ and a set of arcs A. The nodes in sets P, C and D respectively represent the potential sites for opening new shared Parking service facilities, Competing parking service facilities, and Demand points (Fig. 1). The shortest distance between the two nodes, $i , j \in N ,$ represented by an arc in A is denoted by $d _ { i j } .$

We consider a general framework that models a set of available parking candidates and decides which to include in the service network and at what quality level. Typical candidates can be a level or a block of parking spaces from a multiple level parking complex. Fig. 1 illustrates the mechanism of shared parking services. In the figure, the size of P and C show that the density of available shared parking space may vary from area to area. The grey circle linking square P implies usage of private parking and the circle linking any two diferent nodes implies the usage of shared parking from a demand spot. The availability of parking spaces for sharing could be an issue because it directly afects the supply.

Suppose that a shared parking service firm has a limited budget B and is attempting to open one or more new parking facilities from a finite set of potential candidate locations P that are previously privately owned. The fixed cost for constructing/renovating the parking facility at site j is denoted by $f _ { j } , j \in P .$ There is a set of existing parking facilities $C \subset N ( | C | = m )$ that belongs to other parking service firms with service quality $\alpha _ { j }$ at parking $j \in C .$ . For simplicity, we assume that m existing parking facilities belong to m diferent competitors respectively. However, the proposed model and algorithms given later can be easily extended to the case where some competitors have multiple facilities. The potential parking service demand at demand zone $i \in D$ is denoted by $w _ { i } .$ When entering the market, the entrant firm also needs to decide the service quality at each site, denoted by $y _ { j } , j \in P ,$ , and carefully take into account possible responses from existing competitors.

We assume that the service quality level of each new parking or the quality improvement level of each existing parking is taken from a discrete set. This assumption does not lead to a loss of generality but simplifies the solution to the studied problem. The entrant firm needs to decide the service quality at each site ${ \mathfrak { i } } \in P ,$ denoted by $y _ { j } ,$ and carefully take into account the responses from existing competitors. Each existing parking facility $j \in C$ can improve its service quality to compete for market share subiect to a limited budget $B _ { j } .$ Let $z _ { j }$ be the increased service quality, $j \in C .$ Note that reallocating existing facilities is not allowed because it is expensive. We also assume that the service quality of both new and existing parking facilities are bounded and the maximum service quality is denoted as $q _ { m } , m \in P \cup D$

We assume that a potential customer whose destination is zone i, $\forall i \in D$ is free to decide where to purchase parking service, and her/his decision is mainly afected by two factors: the service quality at facility ${ \ u { \ u { \ u { \ u { \ u { \ u { \ u { \ u { \ u { \ v { \ v { \ v { \ v { \ v { \ v { \ v { \ v { \ v { \ v { \ v { \ v { \ v { \ v } { \ v { \ v { \ v { \ v } { c } } } } } } } } } } } } } } } } } } } } } } } } } } , \ { \ v { \ v { \ v { \ v { \ v { { \ v { \ v { \ v { \ v { \ v { \ v { \ v { \ v { \ v { c } } } } } } } } } } } } } } } } \forall j \in P \cup { \ v { \ v { \ v { \ v { { \ v { c } } } } } } }$ denoting its service level and the travel distance from node i to facility $j , \mathrm { i } . e . , d _ { i j }$ . The market share of each parking is determined by the utility its customers gain from purchasing the service provided by the parking facility. The utility of a customer whose destination is demand zone i patronizing parking facility $j ,$ denoted by $u _ { i j } ,$ increases in the service quality and decreases in the travel distance. Nevertheless, for facility j, $\forall j \in P \cup C ,$ the higher the service quality provided, the more the cost required. For simplicity, it is assumed that customers with the destination zone i ∈ D perceive the same utility [12]. According to [9], the following utility expressions (1) and (2) for new and existing parking facilities are defined:

$$
u _ {i j} = y _ {j} ^ {\beta_ {1}} d _ {i j} ^ {- \beta_ {2}}, i \in D, j \in P\tag{1}
$$

$$
u _ {i j} = (\alpha_ {j} + z _ {j}) ^ {\beta_ {1}} d _ {i j} ^ {- \beta_ {2}}, i \in D, j \in C\tag{2}
$$

where $\beta _ { 1 }$ and $\beta _ { 2 }$ are non-negative values, respectively representing the sensitivity of customers to quality and travel distance. For practical applications, these are estimated based on available real data. As defined above, $y _ { j }$ and $z _ { j }$ are decision variables for the service quality of new and existing parking, respectively. We note that $d _ { i j }$ in (1) is a variable for the new parking's location, while that in (2) is a parameter since the location of an existing parking is known.

Let $s \subseteq P$ denote the set of selected sites for locating new parking facilities. Then, the probability of a customer i ∈ D to patronize facility $j \in S \cup C _ { : }$ , denoted by $p _ { i j } ,$ is proposed according to an MCI-type model [13] as follows:

$$
p _ {i j} = \frac {u _ {i j}}{\sum_ {l \in C} u _ {i l} + \sum_ {k \in S} u _ {i k}}, i \in D, j \in S\tag{3}
$$

$$
p _ {i j} = \frac {u _ {i j}}{\sum_ {l \in C} u _ {i l} + \sum_ {k \in S} u _ {i k}}, i \in D, j \in C\tag{4}
$$

The market share or customer flow whose destination is demand zone $i , i \in D ,$ , captured by a parking $j , j \in S \cup C ,$ , is thus written as

follows:

$$
M _ {i j} = w _ {i} p _ {i j}, i \in D, j \in S \cup C\tag{5}
$$

Then, the profit obtained by parking $j , j \in S \cup C$ can be defined as follows:

$$
\pi_ {j} = F \left(\sum_ {i \in D} M _ {i j}\right) - (f _ {j} + \phi (y _ {j})), j \in S\tag{6}
$$

$$
\pi_ {j} = F \left(\sum_ {i \in D} M _ {i j}\right) - \phi (z _ {j}), j \in C\tag{7}
$$

where F is a strictly increasing function which transforms the market share into expected sales. Following [2], F is taken as a linear function, $\mathrm { i . e . , } \ F ( \Sigma _ { i \in D } M _ { i j } ) \ = \ \rho \Sigma _ { i \in D } M _ { i j } ,$ where $\rho$ is the unit profit obtained. $\phi ( y _ { j } )$ $j \in S$ and $\phi ( z _ { j } ) , j \in C$ are functions computing the cost of operating a new parking with quality level $y _ { j }$ and that of increasing an existing parking in quality level $z _ { j } ,$ respectively. In this paper, we consider a linear service quality cost function, $\mathbf { i . e . , } \phi ( y _ { j } ) = q ^ { c } y _ { j }$ and $\begin{array} { r } { \phi ( z _ { j } ) = q ^ { c } z _ { j } , } \end{array}$ where $q ^ { c }$ is the cost of increasing one level of service quality.

The problem consists of optimally deciding the location of new entrant parking facilities ${ \boldsymbol { s } } \subseteq P$ and determining their service quality by taking into account the reactions of competitors' parking facilities and limited budget, so as to maximize the total profit of the entrant firm. Specifically, m competitors' parking service facilities that are already in the market can maximize their own profit by optimally improving their service quality.

## 2.2. Notations

The notations to be used for the formulation are summarized as follows.

Indices:

i: index of demand zone.

j: index of existing parking facilities and potential sites.

Parameters:

N: set of nodes in the network, $i , j \in N .$

A: set of arcs in the network.

P: set of potential locations for opening new parking facilities, $P \subset N .$

C: set of existing parking ${ \mathrm { f a c i l i t i e s , } } C \subset N .$

D: set of demand zones, $D \subset N .$

w : demand per unit time at zone $i \in D .$

$d _ { i j } .$ shortest distance from node i to j, $( i , j ) \in A .$

$\alpha _ { j } \cdot$ current quality level of existing facility $j , j \in C .$

$\beta _ { 1 } \colon$ customer service quality sensitivity parameter, $\beta _ { 1 } \geq 0$

$\beta _ { 2 } \mathrm { : }$ customer travel distance sensitivity parameter, $\beta _ { 2 } \geq 0$

$f _ { j } { \mathrm { : } }$ fixed cost associated with the opening of a parking facility at site $j \in P .$

ϕ(y ): cost of operating a new parking j with quality level $y _ { j } , j \in P .$ ϕ(z ): cost of increasing an existing parking j at quality leve $z _ { j } , j \in C$

B: budget of the entrant firm available for opening new parking facilities.

ρ: income from a single customer from sharing.

$B _ { j } \colon$ budget of existing parking $j \in C$ available for improving its quality level.

$q _ { m } \mathrm { : }$ maximum quality level for each parking facility. Note that $q _ { m } \geq a _ { j } { \mathrm { f o r } } j \in C .$

$q ^ { c } \colon$ cost of increasing one level of service quality.

Decision variables:

$x _ { j } { \mathrm { : } }$ equal to 1 if a parking is open at site j $\forall j \in P ,$ and 0 otherwise. y : quality level of new parking $j , \forall j \in P ,$ , and $y _ { j } \in Q _ { j } = \{ q _ { 1 } ^ { ~ j } , q _ { 2 } ^ { ~ j } \}$ $\ldots , q _ { m _ { i } ^ { j } } \}$ , where $q _ { k } ^ { \ j } , k \ = \ 1 , \ 2 , \ . . . , m _ { j }$ is the k-th quality level of new parking $j , 0 \in Q _ { j } ,$ . Note that $y _ { j } = 0$ means that site j is not open.

z : quality improvement level of parking $j , \forall j \in C ,$ already in the market, and $z _ { j } \in Q _ { j } = \{ q _ { 1 } { } ^ { j } , q _ { 2 } { } ^ { j } , . . . , q _ { m _ { i } } { } ^ { j } \}$ , where $q _ { k } ^ { \ j } , k { = } 1 , 2 , . . . , m _ { j }$ is the kth quality level of new parking facility ${ \ u { j } } , 0 \in Q _ { j } .$

Intermediate variables:

u<sub>ij</sub>: utility of a customer whose destination is demand zone $i , i \in D$ who patronizes parking facility $j \in P \cup C .$

p : probability of a customer $i \in D$ to patronize parking facility $j \in S \cup C$

$M _ { i j } { \mathrm { : } }$ market share or customer flow at demand zone $i , i \in D ,$ captured by a parking facility $j , j \in S \cup C .$

π : profit obtained by parking facility $j , j \in S \cup C .$

## 2.3. Formulation

Based on the above discussion, the considered problem can be formulated as the following integer non-linear program.

Model <sub>n</sub>:

$$
\begin{array}{l} \max \sum_ {j \in P} \pi_ {j} = \sum_ {j \in P} \left(\rho \sum_ {i \in D} M _ {i j} - \phi (y _ {j}) - f _ {j} x _ {j}\right) \\ = \sum_ {j \in P} \left(\sum_ {i \in D} \frac {\rho w _ {i} y _ {j} ^ {\beta_ {1}} d _ {i j} ^ {- \beta_ {2}}}{\sum_ {l \in C} (\alpha_ {l} + z _ {l}) ^ {\beta_ {1}} d _ {i l} ^ {- \beta_ {2}} + \sum_ {k \in P} y _ {k} ^ {\beta_ {1}} d _ {i k} ^ {- \beta_ {2}}} - q ^ {c} y _ {j} - f _ {j} x _ {j}\right) \end{array}
$$

$$
\text { s.   t. } \quad \sum_ {j \in P} (q ^ {c} y _ {j} + f _ {j} x _ {j}) \leq B,\tag{8}
$$

$$
y _ {j} \leq q _ {m} x _ {j}, \forall j \in P,\tag{9}
$$

$$
q ^ {c} z _ {j} \leq B _ {j}, \forall j \in C,\tag{10}
$$

(11)

$$
z _ {j} + a _ {j} \leq q _ {m}, \forall j \in C,\tag{12}
$$

$$
x _ {j} \in \{0, 1 \}, \forall j \in P,\tag{13}
$$

$$
y _ {j}, z _ {j} \in Q _ {j}, \forall j \in P \cup C.\tag{14}
$$

Objective (8) is to maximize the profit obtained by all new parking facilities for the entrant firm. Constraint (9) ensures that the available budget of the entrant firm cannot be exceeded. Constraint (10) restricts that the value of service quality $y _ { j }$ is equal to 0 if site j is not selected and the service quality $y _ { j }$ is bounded by $q _ { m } \mathrm { i f }$ site j is open. Constraint (11) ensures that the cost of each new parking $j \in P$ for setting its service quality should not exceed its available budget $B _ { j } .$ Constraint (12) means that the maximum quality level of each existing parking $j \in C$ should not exceed $q _ { m } .$ . Constraints (13) and (14) enforce the re strictions on decision variables.

As mentioned above, each existing facility $j , j \in C$ in the market would react to maximize its profit obtained by improving its service quality. Then, for any $j \in C ,$ , the corresponding optimization problem can be also formulated as the following integer non-linear program.

Model <sub>j</sub>:

$$
\max \pi_ {j} = \sum_ {i \in D} \frac {\rho w _ {i} (\alpha_ {j} + z _ {j}) ^ {\beta_ {1}} d _ {i j} ^ {- \beta_ {2}}}{\sum_ {l \in C} (\alpha_ {l} + z _ {l}) ^ {\beta_ {1}} d _ {i l} ^ {- \beta_ {2}} + \sum_ {k \in P} y _ {k} ^ {\beta_ {1}} d _ {i k} ^ {- \beta_ {2}}} - q ^ {c} z _ {j},\tag{15}
$$

subject to constraints (9)–(14).

Note that the entrant shared parking facilities and the existing ones would compete with each other for market share such that their own profits are maximized. Such a competitive process can be modeled as a non-cooperative game that will be detailed later. Since a discrete facility location problem in a competitive environment without considering quality decisions and competitors' reactions is shown to be NPhard [39], the considered shared parking service facility location and quality design problem in a competitive environment considering the competitors' reactions is also NP-hard.

To solve the proposed model presents several challenges; in particular: (i) the incorporation of quality design and competitors' reactions makes it harder to solve; and (ii) the objectives of the model is nonconvex and discontinuous $( \mathrm { i . e . , }$ , non-smooth and non-linear). Existing methodologies cannot be directly used to solve the proposed model, thus we develop novel solution methodologies next.

## 3. Solution methodology

In this section, a solution framework is suggested to solve the considered problem. Its core idea is to decompose the studied problem into two main phases: Quality determination and Location.

Quality determination: Given a set of opened new parking facilities $s ,$ determining the service quality at each parking as well as the improved service quality level at each existing parking;

Location: Determining an optimal set of locations S.

In the framework, the former phase serves as sub-routine for the latter.

## 3.1. Quality determination

Given an optimal set of locations $S \subseteq P ,$ the optimization problem $\mathcal { P } _ { n }$ reduces to the following non-linear integer program:

Model ${ \mathcal { P } } _ { n } ^ { \prime } \colon$

$$
\max \sum_ {j \in S} \sum_ {i \in D} \frac {\rho w _ {i} y _ {j} ^ {\beta_ {1}} d _ {i j} ^ {- \beta_ {2}}}{\sum_ {l \in C} (\alpha_ {l} + z _ {l}) ^ {\beta_ {1}} d _ {i l} ^ {- \beta_ {2}} + \sum_ {k \in S} y _ {k} ^ {\beta_ {1}} d _ {i k} ^ {- \beta_ {2}}} - \sum_ {j \in S} q ^ {c} y _ {j}\tag{16}
$$

$$
\text { s.   t. } \quad \sum_ {j \in S} q ^ {c} y _ {j} \leq B - \sum_ {j \in S} f _ {j}\tag{17}
$$

$$
q ^ {c} z _ {j} \leq B _ {j}, \forall j \in C\tag{18}
$$

$$
y _ {j} \leq q _ {m}, \forall j \in S\tag{19}
$$

$$
z _ {j} \leq q _ {m} - \alpha_ {j}, \forall j \in C\tag{20}
$$

$$
y _ {j}, z _ {j} \in Q _ {j}, \forall j \in S \cup C,\tag{21}
$$

and for any $j \in C ,$ its corresponding problem also reduces to the fol lowing non-linear program:

Model $\mathcal { P } _ { j } ^ { \prime } \colon$

$$
\max \sum_ {i \in D} \frac {\rho w _ {i} (\alpha_ {j} + z _ {j}) ^ {\beta_ {1}} d _ {i j} ^ {- \beta_ {2}}}{\sum_ {l \in C} (\alpha_ {l} + z _ {l}) ^ {\beta_ {1}} d _ {i l} ^ {- \beta_ {2}} + \sum_ {k \in S} y _ {l} ^ {\beta_ {k}} d _ {i l} ^ {- \beta_ {2}}} - q ^ {c} z _ {j},\tag{22}
$$

subject to constraints (17)–(21).

In the quality level determination phase, each parking $j , j \in S \cup C$ seeks for its best service quality as the best response to the other parking facilities' quality decisions. The determination of the best service quality of both new and existing parking facilities lies in finding an optimal quality combination $\mathbf { \sigma } ( \mathbf { y } ,$ z) such that objectives (16) and (22) are maximized while satisfying constraints (17)–(21). To derive the best quality, we model the competitive quality decision process occurring among all parking facilities as a non-cooperative multi-player game in which a parking and a possible set of quality (or a possible set of quality improvements) are considered as a player j and a set of strategies $Q _ { j } ,$ respectively, $j \in S \cup C .$ Moreover, any feasible strategy of each parking must satisfy its budget constraint. The game's non-cooperative nature motivates us to choose Nash equilibrium as its solution. In Nash equi librium, the set of quality choices made by the parking facilities are their best responses to the choices of the competitors' parking facilities.

As previously assumed, $Q _ { j } , \ \forall \ j \in S \cup C$ is a finite discrete set, thus the game's solutions are finite. Since in reality either the entrant firm or the competitors usually cannot know the complete market information, a mixed-strategy is adopted to ensure the existence of Nash equilibrium for the game. [40] proved that a finite game has a Nash equilibrium as stated by the following theorem.

Theorem 1. If a game G is finite, then there is a mixed-strategy Nash Equilibrium for G [40].

The considered non-cooperative n-player game can be represented

by the following tuple:

$$
\Gamma = \left(S \cup C, \{Q _ {j} \} _ {j \in S \cup C}, \{\pi_ {j} \} _ {j \in S \cup C}\right)\tag{23}
$$

According to Theorem 1 in [41], the problem of computing the Nash equilibrium of game Γ can be formulated as an equivalent non-linear minimization program, shown as follows:

Model $\mathcal { P } _ { { T } } \colon$

$$
\min \sum_ {r \in S \cup C} (\pi_ {r} ^ {*} - \pi_ {r} (\sigma))\tag{24}
$$

$$
\mathrm{s.t.} \quad \pi_ {\mathrm{r}} (\sigma_ {- r}, s _ {r} ^ {k}) - \pi_ {r} ^ {*} \leq 0, \forall r \in S \cup C, \forall k = 1, 2, \dots , l _ {r}\tag{25}
$$

$$
\sum_ {k = 1} ^ {l _ {r}} \sigma_ {r} ^ {k} = 1, \forall r \in S \cup C\tag{26}
$$

$$
\sigma_ {r} ^ {k} \geq 0, \forall r \in S \cup C\tag{27}
$$

where σ is the decision vector denoting the mixed strategy combination; $\sigma .$ and $s _ { r } ^ { k }$ denote the mixed strategy vector formed by all players except player r and k-th pure strategy of player r, respectively; and $\sigma _ { r } ^ { k }$ represents the probability assigned to pure strategy $s _ { r } ^ { k } .$ . Note that the optimal value of $\mathcal { P } _ { T }$ is 0. The value of $\pi _ { r } ^ { * }$ at the optimal point gives the expected payof of player r. For more details on the above formulation, we refer to [41].

In this study, we adopt the sequential quadratic programming based quasi-Newton algorithm to solve $\mathcal { P } _ { T }$ such that the Nash equilibrium is identified. For more details on this method, interested readers can refer to [41,42].

## 3.2. Location

In this section, we develop tailored B&B and GA for locating parking facilities. In general, although a B&B algorithm can find the optimal location, it is often computationally hard for large-sized NP-hard problems. Thus, we also develop a meta-heuristic algorithm to solve largesized instances more eficiently.

## 3.2.1. Branch and bound method

In this section, we focus on designing an exact method: branch and bound algorithm to find an optimal solution. The B&B method is an iterative method that exploits a tree structure (generally called tree search). The main part of the algorithm is composed of two basic op erations: branching and bounding. They can be simply explained as follows.

At n-th iteration $( n \geq 1 )$ , a node $o _ { n }$ at the current tree representing a partial solution with its associated total fixed cost $f _ { o _ { n } }$ is selected according to a specified search strategy (for the first iteration, the root node corresponding to the original solution space is considered), and then is branched into two child nodes ${ { o _ { n } } ^ { 1 } }$ and ${ { o _ { n } } ^ { 2 } }$ , which describes deciding to add a new potential parking site j or not, respectively. For each node ${ o _ { n } } ^ { i } ,$ $i = 1 , 2 ,$ , we update $f _ { o _ { n } ^ { i } } = f _ { o _ { n } } + f _ { j } . \mathrm { I f } f _ { o _ { n } ^ { i } } > B _ { }$ , which indicates that it does not contain a feasible solution, then node ${ { o _ { n } } ^ { i } }$ is pruned. If node ${ { o _ { n } } ^ { i } }$ is located at the ∣P∣-th level detailed later, which means that all potential parking sites are considered, then we compute a lower bound $L B _ { o _ { n } ^ { \dagger } }$ by determining the quality of both new and existing parking facilities, and update the best lower bound found so far $L B _ { b }$ if $L B _ { o _ { n } ^ { \ i } } > L B _ { b } .$ . Otherwise, we define problem $U B ( o _ { n } ^ { ~ i } )$ representing a relaxation problem of the corresponding subproblem that is then solved to obtain a corresponding upper bound (if it exists), denoted by $U B _ { o _ { n } ^ { i \bullet } }$ If $U B _ { o _ { n } ^ { i } }$ is less than or equa to $L B _ { b } ,$ which implies that it does not contain a global optimal solution, then node ${ { o _ { n } } ^ { i } }$ is closed and the search for ${ { o _ { n } } ^ { i } }$ is terminated. If there exist unexplored nodes, a new iteration repeats; otherwise, the current lower bound is considered as the optimal solution of the problem and the search is terminated. In what follows, the main components of the proposed branch and bound algorithm including branching rule, lower and upper bounds computation, search strategy and pruning schemes are detailed, followed by a summarization of the overall algorithm.

A. Branching rule: In a traditional B&B method, the branching procedure usually considers all decision variables of an optimization problem. However, for complex optimization problems with multiple sets of variables like the considered problem containing three sets of variables, $\mathrm { i . e . , } x _ { j } , y _ { j } ,$ , and $z _ { j } ,$ a branching procedure taking into account all sets of variables usually requires excessive memory, which may result in slow convergence of a B&B method. To accelerate the speed of the B& B method, we propose a branching procedure based on partial vari ables, which is given in detail next.

For the studied problem, we can find that the location decision of new parking x would greatly afect the values of $y _ { j }$ and z as once locations of new parking facilities are determined, the optimal quality of both new and existing parking facilities can be subsequently determined by computing the Nash equilibrium. Such an observation leads us to design a branching procedure depending on variables $x _ { j }$ instead of all sets of variables.

In our B&B method, the potential parking sites in set P are sequentially considered through the branching procedure. Two branches are generated for each node. Each node at level k represents a partial location scheme $s \prime ,$ in which k potential parking sites are already determined, and the remaining $| P \ | \ - \ k$ potential sites are in the unconsidered set and sequentially considered next. At each node, two child nodes are created by considering a new potential site j selected from the un-considered set. In one child node, the new potential site is considered to be opened, i.e., $x _ { j } = 1$ , while in the other node the new potential site is considered not to be opened, $\mathrm { i } . \mathrm { e } . , x _ { j } { = } 0$ . Note that the selected parking site for each branching node is the one with the highest fixed cost among the remaining unexplored ones, which aims to eliminate the leaf nodes violating the budget constraint as soon as possible in the B&B tree, thereby accelerating the convergence speed.

B. Lower bound computation: To achieve rapid pruning for our B&B algorithm, thereby accelerating its solution speed, we design a constructive heuristic to compute a lower bound of solutions (i.e., a feasible solution). The basic idea of the heuristic is to open as many new parking facilities as possible while respecting limited budget B to compete for more market share. The proposed heuristic first finds a good feasible set of open locations ${ \cal S } _ { 0 } ,$ then determines the quality of all parking facilities by computing the Nash equilibrium for new opened and existing parking facilities, and finally calculating the objective function value $\pi _ { S _ { 0 } }$ . Note that the heuristic can also be used as a standalone method. The procedure of the heuristic for computing a lower bound is outlined in Algorithm 1.

C. Upper bound computation: To accelerate the convergence of the B& B method, an upper bounding scheme is proposed to prune part of branches in the search tree that are not necessary to be explored further. Each node o in the B&B tree corresponds to a partial solution where the values of some variables $x _ { j } ^ { \prime } s$ are determined. Let Ω(o) be these $j \mathbf { s } .$ . To calculate an upper bound of the total profit of all new parking facilities corresponding to node $^ { o , }$ for each existing parking $j \in C ,$ we first fix the quality level to its initial one $\alpha _ { j } , \mathrm { i } . \mathrm { e } . , z _ { j } = 0 ;$ and for each new parking $j \in P ,$ we set its service level as the maximum level $q _ { m }$ if it is considered to be opened. Thus, the market share captured by the new parking facilities would be maximal.

Algorithm 1. Heuristic procedure for computing a lower bound.

In addition, we also relax the budget constraints for existing and new entrant parking facilities and only ensure that the total fixed cost of new entrant parking facilities is equal to or less than the available budget. However, the obtained relaxed model is still non-linear. To make the problem more tractable, we consider the attractions of the existing parking facilities and the sites at which we decide to open a parking only, which is the denominator part of the objective function. Thus, we obtain a linear objective function. Based on the above ana lysis, an upper bound of the total profit of all new parking facilities corresponding to node o can be obtained by solving the following ILP: Model UB(o): Model UB(o)

$$
U B _ {o} = \max \quad \rho \sum_ {i \in D} w _ {i} \frac {\sum_ {j \in P} q _ {m} ^ {\beta_ {1}} d _ {i j} ^ {- \beta_ {2}} x _ {j}}{\sum_ {j \in C} \alpha_ {j} ^ {\beta_ {1}} d _ {i j} ^ {- \beta_ {2}}} - \sum_ {j \in P} f _ {j} x _ {j}\tag{28}
$$

$$
\mathrm{s.t.} \quad \sum_ {j \in P \backslash \Omega} f _ {j} x _ {j} \leq B - \sum_ {j \in \Omega} f _ {j} x _ {j} ^ {o}\tag{29}
$$

$$
x _ {j} = x _ {j} ^ {o}, \forall j \in \Omega\tag{30}
$$

$$
x _ {j} \in \{0, 1 \}, \forall j \in P \backslash \Omega\tag{31}
$$

where $x _ { j } ^ { o }$ are those values determined in node o. Note that the above ILP can be eficiently solved by any optimization solver such as CPLEX.

If there is no solution to UB(o), then node o cannot lead to a feasible solution, and thus can be eliminated from the search tree. Otherwise, the optimal objective function value $U B _ { o }$ provides an upper bound corresponding to node o.

D. Search strategy and pruning schemes: The selection of a good search strategy is important for a B&B algorithm in terms of its eficiency as measured by computational time and memory requirement. Diferent search strategies exist in the literature, such as depth-first search, best-

1: Initialize $S _ { 0 }  \emptyset$ , and $T C \gets 0 ;$

2: Sort all the potential sites in set $P$ in the increasing order of their fixed cost, and let

$$
j = 1;
$$

3: while $T C \le B$ do

4: Open the j-th sorted potential site. $\mathrm { i } . \mathrm { e } . , x _ { j } = 1$ , and set $S _ { 0 } = S _ { 0 } \cup j \colon$

5: Let $T C = T C + f _ { i }$

6: end while

7: Determine the quality of both new and existing parking facilities $\mathbf { \Psi } ( \mathbf { y } , \mathbf { z } )$ based on $S _ { 0 }$ by computing the Nash equilibrium of game Γ;

8: Let $\begin{array} { r } { T C = T C + \sum _ { i \in S _ { 0 } } q ^ { c } y _ { j } ; } \end{array}$

9: if $T C \le B$ then

10: Output the objective function value $\pi _ { S _ { 0 } }$ as the lower bound LB and stop

11: else

12: $\begin{array} { r } { T C = T C - \sum _ { j \in S _ { 0 } } q ^ { c } y _ { j } ; } \end{array}$

13: Close the latest-opened parking $j ^ { \prime }$ and let $S _ { 0 } = S _ { 0 } \backslash \{ j ^ { \prime } \}$

14: $T C = T C - f _ { j } $ and $\mathrm { g o }$ to Step $7 ;$

15: end if

bound-search, and breadth-first search [43]. In our B&B algorithm, we use the depth-first-search strategy plus backtracking rule to select a node for the next branching in the search tree because it performs better than the others.

The search procedure in a branch is terminated when each of the following conditions is satisfied:

i) The current selected node is a leaf or belongs to the ∣P∣-th level; in other words, all potential parking sites are added.

ii) The corresponding total fixed cost is greater than the budget B.

iii) The corresponding upper bound of the current node is less than or equal to the best lower bound found so far.

E. Overall algorithm: The B&B algorithm to solve the addressed competitive shared parking facility location and quality design problem is outlined in Algorithm 2.

chromosomes is produced following the operations of crossover, mutation, evaluation, and selection. The GA stops once a stopping criterion is reached. Detailed procedure for solving the proposed problem with a GA-based method is described next.

A. Solution representation: In a traditional GA, a chromosome is encoded to represent a solution to the original problem. To efectively and eficiently solve the proposed problem by GA, we propose to first use a chromosome to represent a partial solution and then to obtain a complete solution by determining the remaining variables depending on the derived partial solution. For this reason, we consider first encoding new parking facilities' location variables x by a chromosome.

Thus, we define a chromosome $\boldsymbol { c } = \{ c _ { j } \ | \ j = 1 , 2 , . . . , \ | \ P \ | \ \}$ , where ∣P∣ denotes the number of potential locations for opening new parking facilities, to represent the set of decision variables $x = \{ x _ { j } | j { = } 1 , 2 , { \ldots } , | P | \}$ . Each gene $c _ { j }$ in chromosome c represents the

## Algorithm 2. Branch and bound algorithm.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1: Construct an initial feasible location configuration  $S_{0}$  of the new parking facilities and compute the corresponding objective function value  $\pi_{S_{0}}$  with Algorithm 1, and set the current best lower bound  $LB_{b}$  as  $\pi_{S_{0}}$ ;
2: Sort all the potential sites in set P in increasing order of their fixed cost;
3: Select an unexplored node in the B&amp;B search tree according to the depth-first-search strategy plus backtracking rule;
4: Split the selected node into two children branches:  $x_{j} = 1$  and  $x_{j} = 0$ , where j denotes the potential site with the largest fixed cost among the un-considered sites;
5: for  $k = 1; k \leq 2; k++$  do
6: if  $\sum_{i=1}^{j} f_{i}x_{i} &gt; B$  then
7: Node o is eliminated;
8: else if  $j = |P|$  then
9: Determine the quality of both new and existing parking facilities y, z, which ensures the Nash equilibrium, and update the best lower bound  $\pi_{b}$  as  $\pi(\mathbf{x},\mathbf{y},\mathbf{z})$  if  $\pi(\mathbf{x},\mathbf{y},\mathbf{z}) &gt; LB_{b}$ ;
10: else
11: Compute an upper bound  $UB_{o}$  for each branch by solving  $UB(o)$  defined in (28)-(31) with CPLEX and obtain its corresponding location solution x;
12: if there is no solution or  $UB_{o} \leq LB_{b}$  then
13: Node o is eliminated;
14: end if
15: end if
16: end for
17: if there is an unexplored node then
18: Go to Step 3;
19: else
20: Output the best solution (x, y, z) and the corresponding objective function value  $LB_{b}$  and stop.
21: end if
</div>

## 3.2.2. Genetic algorithm based method

As the problem is NP-hard, determining optimal solutions is computationally dificult, especially for large-scale problems. Thus, in addition to the B&B based method developed in the previous section, we propose a GA-based method to tackle large-scale problems. GA is a nature-inspired meta-heuristic method introduced by [44] for solving complex optimization problems. Due to its practical applicability and extensive generality, GA has been successfully applied to many dif ferent optimization problems including workforce stafing and assignment [45], credit scoring [46], and order clustering [47].

A GA is usually driven by an initial “population” of feasible solutions, each of which is encoded as a chromosome. A new population of value of a decision variable $x _ { j } .$ Then, based on the partial solution specified by a chromosome, we obtain a complete solution by determining the quality of all parking facilities (i.e., (y, z)) identified by the Nash equilibrium of game Γ.

B. Initial population generation: The performance of a GA is afected by the choice of its initial population of chromosomes. Thus, a population initialization procedure tailored for the proposed problem is designed here.

To improve the quality of the initial set of individuals and reduce the search space for an optimal solution, we first propose an upper bound on the number of new parking facilities, denoted by S . Let $q _ { m i n } ^ { j }$ denote the lowest quality among set $Q _ { j }$ of parking, $j \in P .$ Then, S is derived via Algorithm 3 whose core idea is to open the potential parking facilities of the lowest fixed cost with consideration of the lowest service quality while respecting the budget limit. Obviously, S is less than or equal to ∣P∣ which helps shrink the solution space.

$( q ^ { c } y _ { j } + f _ { j } x _ { j } ) - B \}$ . If BFT of a solution is greater than $^ { 0 , }$ a penalty value will be added to the fitness function. Thus, the fitness value of a chromosome c is calculated as follows:

Algorithm 3. Computing an upper bound on the number of new parking facilities.

$$
F i t (c) = P r o f i t (x, y, z) - \eta \times \mathrm{BFT}\tag{32}
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input:  $f_{j}$ ,  $q_{min}^{j}$ ,  $q^{c}$ , and B
1: Initialize total cost  $TC \leftarrow 0$  and  $\overline{|S|} \leftarrow 0$ 
2: Sort all potential sites in set P in the non-decreasing order of their fixed cost  $f_{j}$ 
3: Set j=1 and  $TC = TC + f_{j} + q_{min}^{j}q^{c}$ .
4: while  $TC \leq B$  do
5:  $\overline{|S|} = \overline{|S|} + 1$ ,  $j = j + 1$ 
6:  $TC = TC + f_{j} + q_{min}^{j}q^{c}$ 
7: end while
8: Output  $\overline{|S|}$ .
</div>

Then, we set the size of the population as PopSize. For a chromosome $c ,$ we first randomly generate an integer $| S | \in [ 1 , | \overline { { S } } | ]$ , then ran domly select ∣S∣ potential sites from set P and set their corresponding genes c with the value of 1 and the remaining genes c with the value of $^ { 0 , }$ respectively. Thus, we obtain an initial chromosome $c \ = \ ( c _ { 1 } , c _ { 2 } ,$ $\ldots , c _ { | P | } )$ . We check whether this chromosome satisfies budget constraint (9) by considering a minimum quality level $q _ { m i n } ^ { j }$ for each new opened parking. If so, this chromosome is feasible. Otherwise, it is deleted and a new one is regenerated. In the same way, PopSize chromosomes are generated as the initial population $\{ c ^ { 1 } , \stackrel {  } { c ^ { 2 } } , . . . , c ^ { P o p S i z e } \}$ . The detailed procedure for the initial population generation is outlined in Algorithm 4.

where Profit() calculates the total profit of all new entrant parking facilities via (8); and η denotes a penalty factor. The larger the fitness function value, the better the corresponding individual.

D. Section operation: The selection of chromosomes is done using roulette wheel section. It is a fitness-proportional-based selection in which chromosomes with higher fitness have larger probability to be selected. For each chromosome $c ^ { l } ,$ its probability of being selected is defined as $\begin{array} { r } { p _ { l } = \frac { F i t ( c ^ { l } ) } { \sum _ { l } F i t ( c ^ { l } ) } } \end{array}$ . The selection process is done by spinning the roulette wheel PopSize times. Each time one chromosome is chosen for a new population with probability $p _ { l } .$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 4. Initial population generation.

Input: PopSize,  $\overline{|S|}$ , and B

1: Initialize  $l \leftarrow 1$ 

2: while  $l \leq PopSize$  do

3: Set  $c_{j}^{l} \leftarrow 0$  for  $\forall j \in \{1, 2, ..., |P|\}$ 

4: Randomly generate an integer number  $|S| \in [1, \overline{|S|}]$ 

5: Randomly select  $|S|$  potential sites from set P and set their corresponding genes  $c_{j}^{l}$  with the value of 1

6: if  $\sum_{j \in P}(q^{c} q_{min}^{j} + f_{j}) c_{j}^{l} &gt; B$  then

7: Go to Step 3

8: else

9:  $c^{l}$  is found and set  $l = l + 1$ 

10: end if

11: end while

12: Output  $\{c^{1}, c^{2}, ..., c^{PopSize}\}$ .
</div>

C. Fitness computation: For a chromosome c in the population, the objective function of its decoded solution $( x , y , z )$ is used to define the fitness function. First, we obtain $x _ { j } = c _ { j } \mathrm { f o r } j = 1 , 2 , . . . , \vert P \vert .$ . Then, the quality of new and existing parking facilities $( y , z )$ are determined by calculating the Nash equilibrium of game $T .$

As the decoded solution may violate the budget constraint (9), we thus transform the budget constraint into a soft constraint based on a budget feasibility test (BFT) function. BFT is defined as $\operatorname* { m a x } \{ 0 , \Sigma _ { j \in P }$

E. Crossover operation: First, we define a probability $p _ { c }$ for crossover operation. Then, we randomly generate a real number $r \in [ 0 , 1 ] .$ . If $\begin{array} { r l } { p _ { c } } & { { } > \ ~ r , } \\ { \cdot } & { { } > \ ~ \cdot } \end{array}$ two parent chromosomes $\begin{array} { l l l } { { c ^ { l } } } & { { = } } & { { ( c _ { 1 } { } ^ { l } , c _ { 2 } { } ^ { l } , . . . , c _ { | P | } { } ^ { l } ) } } \end{array}$ and $\bar { c } ^ { k } \ = \ ( { c _ { 1 } } ^ { k } , { c _ { 2 } } ^ { k } , . . . , \bar { c _ { | P | } } ^ { k } )$ and an integer $\lambda \in [ 2 , | P | - 1 ]$ are randomly generated. Thus, two ofsprings $( { c _ { 1 } } ^ { l } , . . . , { c _ { \lambda } } ^ { l } , { c _ { \lambda + 1 } } ^ { k } , . . . , { c _ { | P | } } ^ { k } )$ and $( c _ { 1 } ^ { ~ k } ,$ $\dots , { c _ { k } } ^ { k } , { c _ { \lambda + 1 } } ^ { l } , . . . , { c _ { | P | } } ^ { l } )$ are produced.

F. Mutation operation: First, we define a probability $p _ { m }$ for mutation operation. Then, for each gene of the selected parent chromosome, randomly generate a real number s ∈ [0,1] and update the gene's value from 0 to 1 or 1 to 0 if p > s. Thus, a mutated child chromosome is generated. G. Termination criterion: The GA-based algorithm is terminated when a maximum number of generations MaxGen is reached. H. Overall algorithm:Algorithm 5 presents the GA-based method.

## Algorithm 5. GA-based method.

## 4. Numerical experiments & managerial insights

In this section, we first use a small example for illustration and to draw managerial insights. We then test a large-sized problem with 320 randomly generated instances to verify the performance of the proposed algorithms.

1: Initialize the population size PopSize, crossover probability $p _ { c } ,$ mutation probability $p _ { m } ,$ , and maximum number of generations MaxGen. Set generation index $i \gets 1 ;$ 2: Initialize PopSize chromosomes as the initial population calling Algorithm 4; 3: Calculate the fitness value of each new chromosome c; 4: Set $x _ { j } = c _ { j }$ for $j = 1 , 2 , . . . , | P | ;$ 5: Derive the quality of both new and existing parking facilities $\mathbf { \Psi } ( \mathbf { y } , \mathbf { z } )$ by computing the Nash equilibrium of game Γ; 6: Calculate the fitness value $F i t ( c )$ via (32); 7: Select chromosomes by spinning the roulette wheel if $i > 1 ;$ 8: Produce new chromosomes via crossover and mutation operations; 9: if i = MaxGen then 10: Output the best found solution $\left( \mathbf { x } , \mathbf { y } , \mathbf { z } \right)$ , then stop. 11: else 12:Set $i = i + 1$ and go to Step 3; 13: end if

![](/api/attachments/B2PZDGA3/fulltext/images/9ea7b68906ac45c58dba67b261791d48d06c036a2f0ad62c01ea2f9de6eebf8e.jpg)  
Fig. 2. Basic setup.

## 4.1. Simple example & managerial insights

A simple simulated example with a five by five customer demand zone (Fig. 2) is conducted. We consider 25 demand zones and 6 potential shared parking sites P1–P6. The red zone indicates a high-demand area where an existing competitor C is located. The parameters are set as follows: the current quality level of the competitor is set at 5, the maximum quality level for any parking facility is 15, the cost for increasing one level of service quality is 50, the income from a single customer from sharing is 50. The fixed costs of selecting P1, P2, P3, P4, P5, and P6 are 300, 500, 300, 700, 600, and 500, respectively. The customer demand is set to be 10 from zone 1–25, except the red zones 12, 13, 17, and 18, where demand is set to be 100. The distances matrix between potential and existing parking and demand zones are listed in Table 1.

We consider three scenarios (1 monopoly, 2 duopoly, 3 duopoly with service diferentiation) and investigate the optimal location and quality decisions. For the monopoly case, there is no competition so minimizing the weighted travel distance to achieve a high service coverage of demand is simply optimal for the firm. For a fair comparison among three scenarios, the initial quality level of new shared parking facilities for the first two scenarios are set at 5, which is the same as that of the competitor.

The computational results are summarized in Table 2 and illustrated in Figs. 2–5. Fig. 2 shows the basic model setup with zones of regular parking demand, high demand zones, potential parking facilities and a

The distances between potential and existing parking and demand zones.

<table><tr><td> $\begin{array}{c}d_{ji}\text{D}\\P\end{array}$ </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td></tr><tr><td>P1</td><td>0.1</td><td>5</td><td>10</td><td>15</td><td>20</td><td>5</td><td>7</td><td>11</td><td>16</td><td>21</td><td>10</td><td>11</td><td>14</td><td>18</td><td>22</td><td>15</td><td>16</td><td>18</td><td>21</td><td>25</td><td>20</td><td>21</td><td>23</td><td>25</td><td>28</td></tr><tr><td>P2</td><td>10</td><td>5</td><td>0.1</td><td>5</td><td>10</td><td>11</td><td>7</td><td>5</td><td>7</td><td>11</td><td>14</td><td>11</td><td>10</td><td>11</td><td>14</td><td>18</td><td>16</td><td>15</td><td>16</td><td>18</td><td>23</td><td>21</td><td>20</td><td>21</td><td>23</td></tr><tr><td>P3</td><td>20</td><td>15</td><td>10</td><td>5</td><td>0.1</td><td>21</td><td>16</td><td>11</td><td>7</td><td>5</td><td>22</td><td>18</td><td>14</td><td>11</td><td>10</td><td>25</td><td>21</td><td>18</td><td>16</td><td>15</td><td>28</td><td>25</td><td>23</td><td>21</td><td>20</td></tr><tr><td>P4</td><td>10</td><td>7</td><td>8</td><td>11</td><td>15</td><td>7</td><td>3</td><td>4</td><td>8</td><td>13</td><td>8</td><td>4</td><td>4</td><td>8</td><td>13</td><td>11</td><td>8</td><td>9</td><td>11</td><td>15</td><td>15</td><td>13</td><td>13</td><td>15</td><td>18</td></tr><tr><td>P5</td><td>21</td><td>18</td><td>16</td><td>15</td><td>16</td><td>18</td><td>14</td><td>11</td><td>10</td><td>11</td><td>16</td><td>11</td><td>7</td><td>5</td><td>7</td><td>15</td><td>10</td><td>5</td><td>0.1</td><td>5</td><td>16</td><td>11</td><td>7</td><td>5</td><td>7</td></tr><tr><td>P6</td><td>18</td><td>18</td><td>20</td><td>22</td><td>25</td><td>13</td><td>13</td><td>15</td><td>18</td><td>22</td><td>8</td><td>9</td><td>11</td><td>15</td><td>20</td><td>4</td><td>4</td><td>9</td><td>13</td><td>18</td><td>3</td><td>4</td><td>8</td><td>13</td><td>18</td></tr><tr><td>C</td><td>20</td><td>18</td><td>18</td><td>19</td><td>22</td><td>15</td><td>13</td><td>13</td><td>15</td><td>18</td><td>11</td><td>9</td><td>8</td><td>11</td><td>14</td><td>9</td><td>4</td><td>4</td><td>8</td><td>12</td><td>8</td><td>4</td><td>2</td><td>8</td><td>12</td></tr></table>

Table 2  
Computational results for the case study.

<table><tr><td rowspan="2">Scenarios</td><td colspan="4">New entrant firm</td><td colspan="3">The competitor</td></tr><tr><td>Profit</td><td>Cost</td><td>Location</td><td>Quality</td><td>Profit</td><td>Cost</td><td>Quality improvement</td></tr><tr><td>Scenario 1</td><td>29,650</td><td>850</td><td>P4</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Scenario 2</td><td>18,335.98</td><td>1800</td><td>P4, P5</td><td>-</td><td>10,364.02</td><td>0</td><td>-</td></tr><tr><td>Scenario 3</td><td>14,809.73</td><td>2000</td><td>P3, P4</td><td>5, 15</td><td>13,190.27</td><td>500</td><td>10</td></tr></table>

![](/api/attachments/B2PZDGA3/fulltext/images/2be4f4f3c737c943eacda57979cf8d39dcea2195b842d052204ee93c8bd9da78.jpg)  
Fig. 3. Location decision without competition.

competitor. Fig. 3 shows that without competition. The best solution for the firm is to select facility P4, which is located closest to the high demand zone. When there is a competitor, as shown in Fig. 4, the optimal locations include both P4 and P5. One explanation is that the competitor changes the demand distribution for the firm, especially in the red zones. To react, the firm includes a new parking facility that is less afected by the competitor. We include diferentiated (higher) service ofering in Fig. 5. The firm's location selection becomes P4 and P3. Higher service ofering (such as fast EV charging) gives the customer more incentive to use such parking facilities even if they are farther away. Higher service level expands the maximum travel distance limit between the demand and the facility location. Traditionally if we consider only location, P3 would not be included because it is the most remote site with low coverage rate. With high service level offerings and with competition, P3 now appears in the list of optimal parking locations when the competitor also increases its service level.

![](/api/attachments/B2PZDGA3/fulltext/images/1dd73a6e72623b421e27a7053e374a037a9e8fdb59f6a71411620d7436ef00f3.jpg)  
Fig. 4. Location decision with competition.

![](/api/attachments/B2PZDGA3/fulltext/images/bed9b18771fc7496eebe3d3a76dcd010780c26e064fc7f080f42bf253a2cd8ea.jpg)  
Fig. 5. Location + quality decision with competition.

From Table 2, we see that the total profits of the new entrant shared parking firm without competition, with competition, and with quality diferentiation are 29,650, 18,335.98, and 14,809.73 respectively. The investment cost increases from 850, 1800, to 2000. For the case without competition, only one facility is established, while two facilities are opened for the cases with competition. Moreover, the area with max imum travel distance is enlarged when the service quality is increased. For the first two cases without quality competition, the center parking points with high demands are considered. With quality diferentiation, the firm's profit decreases because of the additional cost to improve quality and because of competitor's reaction by improving its service quality. In this case, the firm's decision includes a very remote parking point P3, which is counter-intuitive if we don't consider parking service competition. Such results are clearly shown in Figs. 2–5. The competitor's total profit increases from 10,364.02 to 13,190.27 when service quality improvement is considered.

## 4.2. Larger-sized randomly generated instance

For the large sized problems, diferent cities/areas have their unique setups in terms of shared parking availability, parking demand pattern, and competition. Each scenario (e.g., map of parking facilities in a city) renders a unique problem setup for the decision maker. The solution algorithms perform diferently when the problem size difers. Regarding solvability and solution optimality, we therefore conduct a series of analysis to investigate the suitable solution methods from small to large sized problems.

We evaluate the performance of the proposed algorithms with 32 groups of randomly generated instances under diferent structures with 10 instances for each group, thus leading to 320 instances in total. Each item for each group in the computational result table is the average value of the 10 instances. The proposed algorithms are coded in ${ \mathrm { C } } + + ,$ with which the sequential quadratic programming based quasi Newton method [41] and IBM ILOG CPLEX 12.2 are combined to compute the Nash equilibrium of game Γ and exactly solve UB(o), respectively. CPLEX is run in default options. We set PopSize and MaxGen to 50 and 200 by rules of thumb. To select a better crossover and mutation probability combination $( p _ { c } , p _ { m } ) _ { : }$ , various combinations of crossover probabilities {0.7, 0.8, 0.9} and mutation probabilities {0.05, 0.10, 0.15} are compared in the preliminary experiments. The combination (0.9, 0.15) generally performs better than the others and is then adopted for the GA-based method in the remaining experiments. In addition, for each instance, we test the GA-based method through 10 independent runs and compute the average value for analysis. The computational time for both methods of each instance is limited to 36,000 s. All tests are carried out on a PC equipped with a 2.4 GHz processor and 2 GB of memory.

The data for each test instance is randomly generated in the following way. The customer demand per unit time at each zone $w _ { i } , i \in D ,$ is randomly generated in the interval [10,50]. The locations of demand zones, existing and candidate parking facilities are randomly distributed in a $[ 0 , 5 0 ] \ \times \ [ 0 ,$ 50] Euclidean plane. The shortest distance between each zone and each parking $d _ { i j } , i \in D , j \in P \cup C ,$ is calculated accordingly. The service quality of each existing parking j is randomly generated in the interval $[ 1 , 1 0 ] , j \in C .$ . Each new parking j is assumed to have three levels of service quality, i.e., $Q _ { j } = \{ 5 , 1 0 , 1 5 \} , j \in P ;$ and each existing parking j is assumed to have two levels of service quality improvement, $Q _ { j } \ = \ \{ 5 , 1 0 \} , j \in C .$ The cost for increasing one level of service quality $q ^ { c }$ and the fixed cost of opening a potential parking $f _ { j } ,$ $j \in P$ are randomly generated in the interval [50, 100] and [200, 500], respectively. Both sensitivity parameters $\beta _ { 1 }$ and $\beta _ { 2 }$ are set to 1. The available budget of the entrant firm B is set to 2000. The available budget of the existing parking is set as: $B _ { j } = 1 0 0 0 , j \in C$ . The income from a single customer from sharing ρ is set to 50.

In the experiments, the results obtained by the B&B algorithm are compared with those obtained by the GA-based method in terms of two performance measures: (i) deviation $\begin{array} { r } { \left( \% \right) \ = \ \frac { L B _ { G A } - O p t . } { O p t . } \ * } \end{array}$ 100% where Opt. and $L B _ { G A }$ denote the objective function value obtained by the B&B algorithm and GA-based method, respectively; and (ii) computational time ratio $\begin{array} { r } { \mathbf { \Sigma } = \frac { C T _ { B \& B } } { C T _ { G A } } } \end{array}$ where $C T _ { B 8 : B }$ and $C T _ { G A }$ denote the computational time (CPU seconds) spent by the B&B algorithm and GA-based method, respectively. The comparison results of both methods are summarized in Tables 3–6.

Table 3 reports the computational results for instances with ∣P∣ fixed at $3 , | C | = 3 , 5 , 7$ and $\vert D \vert = 2 0 , 5 0 , 1 0 0$ . From Table 1, we observe that: i) The proposed B&B algorithm can find optimal solution for all the instances within about 2 min, which indicates its efectiveness and efi ciency in obtaining optimal solutions. The deviations of the solutions found by the GA-based method are 0, implying that an optimal solution is obtained for each instance. This shows that the proposed GA-based method is able to find high-quality solutions; ii) The CPU time for the B &B algorithm (resp. the GA-based method) varies from 8.5 (resp. 35.20) to 120.82 s (resp. 404 s) with its average value 38.4 s (resp. 136.68 s). The B&B algorithm spends less time than the GA-based algorithm over all groups, and the former spends 28% time of the latter on average. This shows that the B&B algorithm is more eficient than the GA-based

Table 3  
Computational results for instances with $\left| P \right| = 3 .$

<table><tr><td rowspan="2">Group</td><td rowspan="2">|C|</td><td rowspan="2">|D|</td><td>B&amp;B algorithm</td><td colspan="2">GA based method</td><td rowspan="2">Ratio</td></tr><tr><td>CPU time (s)</td><td>Deviation (%)</td><td>CPU time (s)</td></tr><tr><td>1</td><td>3</td><td>20</td><td>8.50</td><td>0.00</td><td>35.20</td><td>0.24</td></tr><tr><td>2</td><td></td><td>50</td><td>8.84</td><td>0.00</td><td>35.30</td><td>0.25</td></tr><tr><td>3</td><td></td><td>100</td><td>8.88</td><td>0.00</td><td>38.30</td><td>0.23</td></tr><tr><td>4</td><td>5</td><td>20</td><td>13.19</td><td>0.00</td><td>54.60</td><td>0.24</td></tr><tr><td>5</td><td></td><td>50</td><td>16.92</td><td>0.00</td><td>62.50</td><td>0.27</td></tr><tr><td>6</td><td></td><td>100</td><td>18.01</td><td>0.00</td><td>87.50</td><td>0.21</td></tr><tr><td>7</td><td>7</td><td>20</td><td>64.12</td><td>0.00</td><td>173.20</td><td>0.37</td></tr><tr><td>8</td><td></td><td>50</td><td>86.29</td><td>0.00</td><td>339.50</td><td>0.25</td></tr><tr><td>9</td><td></td><td>100</td><td>120.82</td><td>0.00</td><td>404.00</td><td>0.30</td></tr><tr><td>Average</td><td></td><td></td><td>38.40</td><td>0.00</td><td>136.68</td><td>0.28</td></tr></table>

Table 4  
Computational results for instances with $\left| P \right| = 5 .$

<table><tr><td rowspan="2">Group</td><td rowspan="2">|C|</td><td rowspan="2">|D|</td><td>B&amp;B algorithm</td><td colspan="2">GA based method</td><td rowspan="2">Ratio</td></tr><tr><td>CPU time (s)</td><td>Deviation (%)</td><td>CPU time (s)</td></tr><tr><td>10</td><td>3</td><td>20</td><td>33.47</td><td>0.00</td><td>150.00</td><td>0.22</td></tr><tr><td>11</td><td></td><td>50</td><td>36.75</td><td>0.00</td><td>159.60</td><td>0.23</td></tr><tr><td>12</td><td></td><td>100</td><td>48.19</td><td>0.00</td><td>201.60</td><td>0.24</td></tr><tr><td>13</td><td>5</td><td>20</td><td>92.40</td><td>0.00</td><td>349.20</td><td>0.26</td></tr><tr><td>14</td><td></td><td>50</td><td>100.97</td><td>0.00</td><td>391.20</td><td>0.26</td></tr><tr><td>15</td><td></td><td>100</td><td>131.30</td><td>0.01</td><td>465.80</td><td>0.28</td></tr><tr><td>16</td><td>7</td><td>20</td><td>220.23</td><td>0.00</td><td>783.10</td><td>0.28</td></tr><tr><td>17</td><td></td><td>50</td><td>249.01</td><td>0.00</td><td>1489.37</td><td>0.17</td></tr><tr><td>18</td><td></td><td>100</td><td>909.29</td><td>0.00</td><td>3888.42</td><td>0.23</td></tr><tr><td>Average</td><td></td><td></td><td>202.40</td><td>0.00</td><td>875.37</td><td>0.23</td></tr></table>

Table 5  
Computational results for instances with $\left| P \right| = 1 0 .$

<table><tr><td rowspan="2">Group</td><td rowspan="2">|C|</td><td rowspan="2">|D|</td><td>B&amp;B algorithm</td><td colspan="2">GA based method</td><td rowspan="2">Ratio</td></tr><tr><td>CPU time (s)</td><td>Deviation (%)</td><td>CPU time (s)</td></tr><tr><td>19</td><td>3</td><td>20</td><td>299.17</td><td>0.01</td><td>390.00</td><td>0.77</td></tr><tr><td>20</td><td></td><td>50</td><td>321.84</td><td>0.00</td><td>366.00</td><td>0.88</td></tr><tr><td>21</td><td></td><td>100</td><td>400.71</td><td>0.00</td><td>488.00</td><td>0.82</td></tr><tr><td>22</td><td>5</td><td>20</td><td>645.84</td><td>0.01</td><td>737.10</td><td>0.88</td></tr><tr><td>23</td><td></td><td>50</td><td>697.79</td><td>0.18</td><td>862.00</td><td>0.81</td></tr><tr><td>24</td><td></td><td>100</td><td>840.97</td><td>0.04</td><td>814.50</td><td>1.03</td></tr><tr><td>25</td><td>7</td><td>20</td><td>3268.02</td><td>0.00</td><td>3356.50</td><td>0.97</td></tr><tr><td>26</td><td></td><td>50</td><td>4660.38</td><td>0.00</td><td>5127.20</td><td>0.91</td></tr><tr><td>27</td><td></td><td>100</td><td>6900.77</td><td>0.00</td><td>7437.60</td><td>0.93</td></tr><tr><td>Average</td><td></td><td></td><td>2003.94</td><td>0.03</td><td>2175.43</td><td>0.92</td></tr></table>

## Table 6

Computational results for large-sized instances with ∣P∣ = 5, 10, 20, 50 and 100.

<table><tr><td rowspan="2">Group</td><td rowspan="2">|P|</td><td>B&amp;B algorithm</td><td colspan="2">GA based method</td><td rowspan="2">Ratio</td></tr><tr><td>CPU time (s)</td><td>Deviation (%)</td><td>CPU time (s)</td></tr><tr><td>28</td><td>5</td><td>35.46</td><td>0.00</td><td>140.40</td><td>0.25</td></tr><tr><td>29</td><td>10</td><td>280.60</td><td>0.00</td><td>377.20</td><td>0.74</td></tr><tr><td>30</td><td>20</td><td>4347.98</td><td>0.01</td><td>964.00</td><td>4.51</td></tr><tr><td>31</td><td>50</td><td>18,260.30</td><td>0.10</td><td>2256.00</td><td>8.09</td></tr><tr><td>32</td><td>100</td><td>35,223.54</td><td>0.05</td><td>9822.62</td><td>3.59</td></tr><tr><td>Average</td><td></td><td>11,699.58</td><td>0.03</td><td>2712.04</td><td>4.29</td></tr></table>

method; and iii) The CPU times for both the proposed methods show an increasing trend as the problem size increases. Moreover, for each given ∣C∣ (resp. ∣D∣), the CPU time for the B&B algorithm increases with ∣D∣ (resp. ∣C∣), which implies that the problem's complexity increases with

∣C∣ and ∣D∣.

Table 4 presents the computational results for 9 groups of instances with ∣P∣ increased to 5, ∣C ∣ =3,5,7 and $| D | = 2 0 , 5 0 , 1 0 0$ , from which we can also conclude that: i) the proposed B&B algorithm can find optimal solutions for all the tested instances within a short time (i.e., 910 s), which confirms its eficiency in optimally solving the studied problem; ii) the average deviation varies from 0.00 to 0.01% with its average value being about 0.00, and its value is 0.00 for 8 out of 9 groups, which again shows that the proposed GA-based method is able to find high-quality near-optimal solutions; and iii) the CPU time spent by the B&B algorithm increases from 33.47 to 909.29 s with its average value being 202.40 s, while that of GA-based method varies from 150 to 3888.42 s with its average value being 875.37 s. Moreover, the former is less than the latter over all groups and increases more moderately than the latter with the problem size. These results indicate that the proposed B&B algorithm is superior to the GA-based method in solving the instances with a larger ∣P∣ = 5.

Table 5 summarizes the computational results for the instances with ∣P∣ increasing to 10, from which we can further find that: i) the computational time for the B&B algorithm increase as ∣P∣ increases from 3 to 10 for each given ∣C∣ and ∣D∣. Take groups 9, 18 and 27 as an example, all groups are with ∣C∣ = 7 and $| D | = 1 0 0$ , but ∣P∣ are 3, 5 and 10, respectively, the CPU times are 102.82 s, 909.29 s, and 6900.77 s, respectively. This indicates that the complexity of the problem also increases with ∣P∣; ii) the GA-based method can obtain close to optimal solution as the deviation varies between 0 and 0.18% with its average value being 0.03%; and iii) the CPU times for both the proposed methods have similar increasing trends as the size of the problem increases.

By comparing all the results in Tables 3–5, we summarize the con clusions below.

i) The computational time spent by the proposed B&B algorithm increases more rapidly with the number of potential parking facilities (i.e., ∣P∣) compared with that with the number of existing parking facilities ∣C∣ and demand zones ∣D∣. This may be because the branching procedure of the B&B algorithm is determined by the number of potential location sites and most computational time of the algorithm is spent on solving the integer linear program for computing an upper bound at each explored node; and,

ii) The computational time spent by the GA-based method is more than that of the B&B algorithm over all groups which may be because the CPU time for the GA-based method depends considerably on the number of existing parking facilities and demand zones, while the B &B algorithm depends relatively slightly on them. However, note that the value of the “Ratio” has an increasing trend as ∣P∣ increases. For example, on average, the ratio is 0.28 for ∣P∣ = 3 while it is 0.92 for ∣P∣ = 10. These results imply that the GA-based method performs more stably than the B&B algorithm as the problem size increases.

In order to further explore the influence of the number of potentia parking sites ∣P∣ on the performance of both the proposed algorithms, we also conduct a series of computational experiments that vary the potential number of sites for the location of new parking facilities from 5, 10, 20, 50 to 100, with the number of demand zones fixed at 50 and the number of existing parking facilities fixed at 3. The computational results are summarized in Table 6.

From Table 6, we can conclude that: i) the proposed B&B algorithm is able to obtain optimal solutions for instances with up to 100 potential parking facilities within the given time. The deviation varies between 0.00 and 0.1% with its average value being 0.03%, which again indicates the high quality of the solutions obtained by the GA-based method; and ii) the CPU time for the B&B algorithm increases from 35.46 to 35,223.54 s with its average value being 11,629.58 s, while that for the proposed GA-based method varies between 140.40 and 9822.62 s. On average, the former is 4.29 times the latter. Moreover, the CPU time for the B&B algorithm increases sharply with the number of potential parking facilities, while that of the GA-based method increases moderately and remains acceptable even for instances with a large number of potential parking sites ∣P∣ = 100. This shows that the GA-based method is superior to the B&B algorithm in terms of computational eficiency for solving large-scale instances with a large number of potential parking sites.

To sum up, the B&B algorithm is quite eficient and suitable for solving small- and medium-sized problems, while the GA-based method is more eficient for solving large-sized problems. The GA-based method is therefore the preferred method (vs. B&B method) to solve practical sized problems.

## 5. Conclusions

This paper investigates an emerging research problem of optimal facility location and associated quality design for a new-entrant shared parking firm when facing competition from existing service providers. The service quality is diferentiated by emerging technologies such as IoT, sensor system, charging system, and RFID parking facility surveillance system. These technologies ofer vehicle tracking and tracing capability as well as information on connected parking facilities. Onsite electric charging devices can be designed to ofer various levels of charging speed/time that is considered as one of the key quality indicators for electric vehicles. Parking facility surveillance based on video and sensor improves parking security service quality. Automated checkpoints with RFID and facilitated mobile payments improve convenience and help reduce customer wait time.

We then introduce a new discrete competitive facility location and design that incorporates the responses of the facilities that are already in the market and limited budget constraints and formulates its decision model. To solve this problem, an iterative solution framework consisting of quality determination and location is developed. In the quality determination phase, the competitive decision process occurring among facilities is modeled as a non-corporative game and the best qualities of the new facilities and existing ones are identified through Nash equilibrium. A B&B algorithm and a GA are developed to de termine the locations of new shared parking facilities. Computational results on 320 randomly generated instances show that the proposed B& B algorithm is able to find optimal solutions in reasonable time for small-sized problems with relatively fewer number of potential parking sites, while the proposed GA-based approach is more eficient and suitable for solving large-sized problems with a large number of po tential parking sites.

In this paper, we consider a model of available shared parking spaces at the macro level without considering the flow of patrons at the microscopic level where each patron needs to make decisions based on availability (such as choosing the second-best choice). Integrating the consumers' route decision at the micro level is another future research question to extend this work. The pricing of parking services can be designed in the model to further explain the dynamics of competition in the shared parking market. Few articles on parking facility decision models have considered pricing. Our literature review also shows a void in research on parking pricing that is related to parking distance, capacity, and quality. An immediate future research can be directed at investigating shared-parking pricing as an extension of this work. In this paper, we also assume that the new shared parking firm must possess facilities from the market while the competitors may also enter the market. Consequently, a future extension of this research is to take into account the actions of competitor's new facility decision. From another point of view, shared parking could lead to a reduction in pollution. Thus, future research of green issues in shared parking is practically important [48]. The development of efective methods for the proposed and extended problems [46,49–55] is another future research topic.

## Author contribution statement

Authors: Peng Wu, Feng Chu, Nasreddine Saidani, Haoxun Chen, Wei Zhou.

Contribution: All the authors contribute and are actively engaged in every step of publishing this paper, including conceptualization, methodology, software, validation, formal analysis, investigation, data curation, writing original, writing review& editing, visualization, and funding acquisition.

## Acknowledgement

This work was supported in part by the National Natural Science Foundation of China under Grants 71701049 and 71571061, in part by the Natural Science Foundation of Fujian Province, China under Grant 2018J05120.

## References

[1] L. Chen, J. Olhager, O. Tang, Manufacturing facility location and sustainability: a literature review and research agenda, Int. J. Prod. Econ. 149 (2014) 154–163.

[2] J. Fernández, B. Pelegr, F. Plastria, B. Tóth, et al., Solving a huf-like competitive location and design model for profit maximization in the plane, Eur. J. Oper. Res. 179 (3) (2007) 1274–1287

[3] B. Tóth, J. Fernández, B. Pelegrn, F. Plastria, Sequential versus simultaneous approach in the location and design of two new facilities using planar huf-like models, Comput. Oper. Res. 36 (5) (2009) 1393–1405.

[4] J. Redondo, J. Fernández, I. Garca, P. Ortigosa, Sensitivity analysis of a continuous multifacility competitive location and design problem. Top 17 (2) (2009) 347–365

[5] J.L. Redondo, A. Arrondo, J. Fernández, I. Garca, P.M. Ortigosa, A two-level evolutionary algorithm for solving the facility location and design (1|1)-centroid pro blem on the plane with variable demand, J. Glob. Optim. 56 (3) (2013) 983.

[6] J. Fernández, S. Salhi, G. Boglárka, et al., Location equilibria for a continuous competitive facility location problem under delivered pricing, Comput, Oper. Res 41 (2014) 185–195.

[7] J.L. Redondo, J. Fernández, J.D.Á. Hervás, A.G. Arrondo, P.M. Ortigosa, Approximating the pareto-front of a planar bi-objective competitive facility location and design problem, Comput. Oper. Res. 62 (2015) 337–349.

[8] J. Fernández, G. Boglárka, J.L. Redondo, P.M. Ortigosa, A.G. Arrondo, et al., A planar single-facility competitive location and design problem under the multideterministic choice rule, Comput. Oper. Res. 78 (2017) 305–315.

[9] R. Aboolian, O. Berman, D. Krass, Competitive facility location and design problem, Eur, J. Oper, Res. 182 (1) (2007) 40–62.

[10] M.G. Ashtiani, A. Makui, R. Ramezanian, A robust model for a leader–follower competitive facility location problem in a discrete space, Appl. Math. Model. 37 (1) (2013) 62–71.

[11] W. Shan, Q. Yan, C. Chen, M. Zhang, B. Yao, X. Fu, Optimization of competitive facility location for chain stores, Ann. Oper. Res. (2017) 1–19.

[12] Y. Zhang, Designing a retail store network with strategic pricing in a competitive environment. Int. J. Prod. Econ. 159 (2015) 265–273

[13] M. Nakanishi. L.G. Cooper. Parameter estimation for a multiplicative competitive interaction model: least squares approach J Mark Res, (1974) 303–311

[14] H. Hotelling, Stability in competition, Econ. J. 39 (153) (1929) 41–57.

[15] Z. Drezner, Competitive location strategies for two facilities, Reg. Sci. Urban Econ. 12 (4) (1982) 485–493.

[16] F. Plastria, Gbsss: the generalized big square small square method for planar singlefacility location, Eur. J. Oper. Res. 62 (2) (1992) 163–174.

[17] T. Drezner, Optimal continuous location of a retail facility, facility attractiveness, and market share: an interactive model., J. Retail. 70 (1) (1994) 49–64

[18] R. Suárez-Vega. D.R. Santos-Peñate. P. Dorta-González. Location models and gis tools for retail site location, Appl. Geogr. 35 (1) (2012) 12–22.

[20] S.L. Hakimi, On locating new facilities in a competitive environment, Eur. J. Oper. Res, 12 (1) (1983) 29–35.

[21] S. Hakimi, p-Median theorems for competitive locations, Ann. Oper. Res. 6 (4) (1986) 75–98.

[22] D.L. Huf, Defining and estimating a trading area, J. Mark. (1964) 34–38.

[23] D.L. Huf, A programmed solution for approximating an optimum retail location, Land Econ, 42 (3) (1966) 293–303.

[24] D. Achabal, Multiloc: a multiple store location model, J. Retail. 58 (1982) 5–25

[25] A. Ghosh, C.S. Craig, A location allocation model for facility planning in a competitive environment, Geogr, Anal, 16 (1) (1984) 39–51.

[26] A. Ghosh, C.S. Craig, Fransys: a franchise distribution system location model, J. Retail, 67 (4) (1991) 466.

[27] A. Ghosh, S.L. MacLaferty, Location Strategies for Retail and Service Firms,

Lexington Books, 1987.

[28] H. Küçükaydn, N. Aras, İ.K. Altnel, A discrete competitive facility location model with variable attractiveness, J. Oper. Res. Soc, 62 (9) (2011) 1726–1741

[29] D. Konur, J. Geunes, Competitive multi-facility location games with non-identical firms and convex trafic congestion costs, Transportation Research Part E: Logistics and Transportation Review 48 (1) (2012) 373–385

[30] A. Lančinskas, P. Fernández, B. Pelegn, J. Žilinskas, Improving solution of discrete competitive facility location problems, Optim. Lett. 11 (2) (2017) 259–270.

[31] H.A. Eiselt, G. Laporte, Sequential location problems, Eur. J. Oper. Res. 96 (2) (1997) 217–231.

[32] H.A. Eiselt, G. Laporte, J.-F. Thisse, Competitive location models: a framework and bibliography, Transp. Sci. 27 (1) (1993) 44–54.

[33] T. Drezner, A review of competitive facility location in the plane, Logist. Res. 7 (1) (2014) 114.

[34] M. Ashtiani, Competitive location: a state-of-art review, Int. J. Ind. Eng. Comput. 7 (1) (2016) 1–18.

[35] R.L. Tobin, T. Miller, T.L. Friesz, Incorporating competitors’ reactions in facility location decisions: a market equilibrium approach, Locat. Sci. 3 (4) (1995) 239–253.

[36] N. Saidani, F. Chu, H. Chen, Competitive facility location and design with reactions of competitors already in the market, Eur. J. Oper. Res. 219 (1) (2012) 9–17.

[37] E.M. Hendrix, On competition in a stackelberg location-design model with deterministic supplier choice, Ann. Oper. Res. 246 (1–2) (2016) 19–30.

[38] B.G. Tóth, K. Kovács, Solving a huf-like stackelberg location problem on networks, J. Glob. Optim. 64 (2) (2016) 233–247.

[39] S. Benati, P. Hansen, The maximum capture problem with random utilities: problem formulation and algorithms. Eur. J. Oper. Res, 143 (3) (2002) 518–530.

[40] J.F. Nash, Equilibrium points in n-person games, Proc. Natl. Acad. Sci. U. S. A. 36 (1) (1950) 48.

[41] B. Chatterjee, An optimization formulation to compute Nash equilibrium in finite games, Proceeding of International Conference on Methods and MODELS in Computer Science, 2010, pp. 1–5.

[42] R. Fletcher, Practical Methods of Optimization, John Wiley & Sons, 2013.

[43] T. Ibaraki, Theoretical comparisons of search strategies in branch-and-bound algorithms, International Journal of Computer & Information Sciences 5 (4) (1976) 315-344.

[44] J.H. Holland, Adaptation in Natural and Artificial Systems: An Introductor Analysis With Applications to Biology, Control, and Artificial Intelligence, University of Michigan. Ann Arbor. ML. 1975

[45] N. Ilk, M. Brusco, P. Goes, Workforce management in omnichannel service centers with heterogeneous channel response urgencies, Decis. Support. Syst. 105 (2018) 13–23.

[46] N. Kozodoi, S. Lessmann, K. Papakonstantinou, Y. Gatsoulis, B. Baesens, A multi objective approach for profit-driven feature selection in credit scoring, Decis. Support. Syst. 120 (2019) 106–117.

[47] R. Kuo, L. Lin, Application of a hybrid of genetic algorithm and particle swarm optimization algorithm for order clustering, Decis. Support. Syst. 49 (4) (2010) 451–462.

[48] I. Bose, R. Pal, Do green supply chain management initiatives impact stock prices of firms? Decis. Support. Syst. 52 (3) (2012) 624–634.

[49] I. Bose, K. Altinkemer, Design of a web site for guaranteed delay and blocking probability bounds, Decis, Support, Syst, 38 (1) (2004) 131–140.

[50] I. Bose, E. Eryarsoy, L. He, Multi-period design of survivable wireless access net works under capacity constraints, Decis, Support, Syst. 38 (4) (2005) 529–538

[51]. P. Ravisankar. V. Ravi, G.R. Rao. L. Bose, Detection of financial statement fraud and feature selection using data mining techniques, Decis. Support. Syst. 50 (2) (2011) 491–500.

[52] F. Wang, X. Lai, N. Shi, A multi-objective optimization for green supply chain network design. Decis. Support, Syst. 51 (2) (2011) 262–269.

[53] X. Chen, I. Bose, A.C.M. Leung, C. Guo, Assessing the severity of phishing attacks: a hybrid data mining approach, Decis. Support. Syst. 50 (4) (2011) 662–672

[54] L. Zhang, K. Mistry, C.P. Lim, S.C. Neoh, Feature selection using firefly optimization for classification and regression models. Decis, Support, Syst. 106 (2018) 64–85.

[55] L. Meng, Q. Kang, C. Han, M. Zhou, Determining the optimal location of terror response facilities under the risk of disruption, IEEE Trans. Intell. Transp. Syst. 19 (2) (2018) 476–486

Peng Wu is an Assistant Professor in the School of Economics & Management in Fuzhou University, China.

Feng Chu is a professor in the Laboratory IBISC, University of Evry, University of Paris Saclay, France.

Nasreddine Saidani is a senior research in AZAP research institute, Paris, France.

Haoxun Chen is a professor in the Laboratory LOSI, University of Technology of Troyes, France.

Wei Zhou is a professor of Information Systems & Operations management at the ESCP Europe business school in Paris, France.
