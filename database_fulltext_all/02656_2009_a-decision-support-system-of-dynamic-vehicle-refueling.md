---
otero_id: 2656
otero_key: "8SQG3HW5"
title: "A decision support system of dynamic vehicle refueling"
authors: "Yoshinori Suzuki"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.09.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system of dynamic vehicle refueling

Yoshinori Suzuki ⁎

Department of Logistics, Operations, and Management Information Systems, College of Business, Iowa State University, 2340 Gerdin Business Building, Ames, Iowa 50011-1350, USA

a r t i c l e i n f o

Article history: Received 22 February 2008 Received in revised form 10 September 2008 Accepted 23 September 2008 Available online 9 October 2008

Keywords: Decision support systems Transportation Motor carriers Fuel cost Models and algorithms

## a b s t r a c t

Fuel optimizers are software products that reduce the fuel cost of motor carriers at the “point of purchase” by optimally determining: (i) which truck stop(s) to use, and (ii) how much fuel to buy at the chosen truck stop(s). These products, however, upset many truck drivers by “con<sup>fi</sup>scating” their freedom to choose truck stops. Consequently, users are suffering from limited actual cost savings due to low driver compliance rates. We develop a decision support system that reduces the fuel cost of motor carriers at the point of purchase without con<sup>fi</sup>scating the drivers' freedom to choose truck stops, so that higher driver compliance rates are expected.

© 2008 Elsevier B.V. All rights reserved

## 1. Introduction

Given the dramatic increase of fuel prices during the past few years, ef<sup>fi</sup>cient management of fuel cost has become a critical issue in today's motor-carrier industry. One method of managing fuel cost, which is increasingly recognized by the U.S. truckload (TL) carriers, is the use of software products called “fuel optimizers”. Fuel optimizers are decisionsupport models that reduce motor carrier fuel costs at the point of purchase. These models <sup>fi</sup>rst download the latest price data of nearly all the truck stops in the U.S. and Canada (updated daily), and then compute the optimal fueling schedule for each route that indicates: (i) which truck stop(s) to use, and (ii) how much fuel to buy at the chosen truck stop(s) to minimize the cost of refueling. The models typically work in conjunction with the truck-routing software, so that users can <sup>fi</sup>rst compute the shortest route for a given origin-destination, and then optimize fueling operations along this route. Famous fuel optimizer product names include: (i) ProMiles, (ii) Expert Fuel, and (iii) Fuel & Route. Vendors of these software products claim that, typically, cost savings range from 4 to 11 cents per gal of fuel, which convert to an average saving of \$1200 per truck per year.

Despite the cost saving capability of these software products, many TL carriers are still reluctant to adopt them for two reasons. First, fuel optimizers upset many truck drivers by “con<sup>fi</sup>scating” their freedom to choose truck stops (many drivers have strong preferences on which truck stops to use). Thus, in general, it is dif<sup>fi</sup>cult for users to attain high driver compliance rates (proportion of fueling occasions in which truck drivers comply with the fueling instructions). This condition suggests that users may suffer from limited actual cost savings. Second, the use of fuel optimizers can increase (worsen) truck driver turnover rates. For over two decades, TL carriers have suffered from extremely-high driver turnover rates ([1,7,12]), especially from the high cost of driver replacements ([10,13]). It is generally believed that the use of fuel optimizers will increase the already-high driver turnover rates of TL carriers by upsetting many truck drivers (by con<sup>fi</sup>scating their freedom to choose truck stops) [11].

The above conditions imply that the bene<sup>fi</sup>t of using fuel optimizers, after adjusting for driver compliance rates and replacement costs, may be small. It appears that: (i) the models can give limited actual cost savings, and (ii) their use may increase driver turnover rates. These issues, especially the latter, constitute the main reasons why many carriers are hesitant to adopt fuel optimizers. Since TL carriers have already made substantial investments in the past few years to reduce driver turnover rates (e.g., raise driver pays, provide good fringe bene<sup>fi</sup>ts, etc., — see, e.g., [1,7,6]), they are reluctant to do anything that can possibly increase driver turnover rates even slightly. This pattern suggests that TL carriers do want to reduce fuel costs, but not at the expense of increased driver turnover.

In this paper, we present a new method of managing fuel cost at the “point of purchase” that does not confiscate the freedom of truck drivers to choose truck stops, so that carriers can expect (i) high driver compliance rates, and (ii) minimal increase of driver turnover rates. This method was recently developed by us (research team led by the author) as a decision support system for a medium-sized TL carrier in the U.S., which (like many other carriers) was reluctant to adopt the standard fuel optimizers because of the possible impact on driver turnover rates (this carrier is denoted as carrier X from now on). We show, by performing a series of simulation experiments, that our method (i) allows carriers to reduce fuel cost considerably at the point of purchase without con<sup>fi</sup>scating the drivers' freedom to choose truck stops, and (ii) attains lower costs (higher cost savings) than standard fuel optimizers under certain realistic conditions, if the cost is adjusted properly by driver compliance rates and driver replacement costs.

## 2. Review of fuel optimizers

In this section we review the literature on vehicle refueling and, based on the literature review, derive a mathematical model that mimics standard (commercial) fuel optimizers (the mathematical model derived in this section will later be used in our simulation experiments). Since the literature on vehicle refueling is rather limited, we obtained missing information by performing a series of interviews with four TL carriers, three over-the-road truck drivers, two fuel-optimizer vendors, and two truck-stop chains.

## 2.1. Literature review

Research on vehicle refueling has been conducted by both academic researchers and practitioners. Most of the early works were conducted by practitioners (fuel-optimizer vendors) in early 1990s during the software development phase. These studies developed several mathematical models, and examined the cost-saving potentials of these models. The basic concept of these models is to take advantage of price variance that exists across truck stops in order to reduce the cost of refueling. The models' goal is to buy more gallons at truck stops where the fuel is cheap, and buy fewer gallons at truck stops where the fuel is expensive. Most of the commercial fuel optimizers that exist today have their roots in these studies.

Despite the proliferation of actual software products in the <sup>fi</sup>eld, academic researchers did not study the type of vehicle refueling problems mentioned above until recently. Perhaps the <sup>fi</sup>rst scholarly work that considered the “where-to-buy” vehicle refueling problem is Lin et al. [5]. They considered the <sup>fi</sup>xed-route vehicle refueling problem similar to that addressed by the commercial fuel optimizers, and developed a linear-time greedy algorithm for <sup>fi</sup>nding optimal fueling policies. Other scholarly works that investigated vehicle refueling problems include Lin [4], Khuller et al. [2], and Suzuki [11]. Lin [4] extended the work of Lin et al. [5] by developing an algorithm that jointly determines the optimal path (route) from origin to destination, and the optimal fueling decisions along the path. Khuller et al. [2] considered optimal fueling policies for traveling-salesman problems, and developed several polynomial time approximation algorithms. Suzuki [11] proposed a “generic” approach to the vehicle refueling problems by considering not only fuel cost, but also several other costs of vehicle operations.

Our review of literature indicates that past vehicle-refueling studies face two types of common limitations. First, all of the proposed models con<sup>fi</sup>scate the freedom of truck drivers to choose truck stops. This condition implies that these models may suffer from limited actual cost savings due to low driver compliance rates, and from increased driver turnover rates. Second, all the proposed models are static models that do not consider the dynamic (i.e., day to day) movement of fuel prices (they calculate the optimal fueling schedule based on the latest price data available at the time of dispatch). This pattern suggests that, if the models are used to calculate fueling schedules for those routes that require multiple trip days (which are common in the TL industry), the solutions may not be truly optimal.

## 2.2. Mathematical form of standard fuel optimizers

Basically, commercial fuel optimizers are mathematical programming models that minimize the cost of buying fuel in a given route by selecting optimal fueling locations (truck stops) and quantities (gallons). The following factors are considered by the models: (i) truck's tank capacity, (ii) trip starting fuel, (iii) trip ending fuel, (iv) minimum purchase quantity (to control the frequency of fuel stops), (v) fuel consumption rate, (vi) minimum fuel to be maintained at all times, and (vii) out-of-route distance to each candidate truck stop (extent to which a truck must deviate from the optimal route to reach the truck stop).

Let Ω be the set of all the truck stops along the (shortest) route from origin o to destination d, and $i ( i { = } 1 , 2 , . . . . , n )$ be the elements of Ω (see Fig. 1). Also let (the following are required model inputs):

C<sub>i</sub> = retail diesel price (per gallon) at truck stop i,

a = amount of miles that a driver must go out-of-route to reach truck stop i,

m<sub>i</sub>= distance (miles) from truck stop i − 1 (o if i = 1) to truck stop i (not including a or a ),

m<sub>d</sub>= distance (miles) from truck stop n to destination d (not including a ),

θ = amount of fuel (gallons) in tank at origin o (starting fuel),

σ = average fuel consumption rate (miles per gallon) for the whole trip,

Q = vehicle tank capacity (e.g., 200 gal),

ρ = minimum amount of fuel to be maintained in tank at all times (lower bound fuel),

l = minimum gallons to purchase at truck stops $( \mathsf { e } . \mathsf { g } . , 5 0 \ \mathsf { g } \mathsf { a } ] )$

ε = required amount of fuel in tank at the <sup>fi</sup>nal destination d (ending fuel).

![](/api/attachments/8SQG3HW5/fulltext/images/ec8dbc084d86e34cc4f88cbff79c9107ba5577d82ff604fa252165a543639225.jpg)  
Fig. 1. A sample route.

Given these inputs, the vehicle refueling problem addressed by standard fuel optimizers can be written as a mixed-integer LP model of the following form (this formulation is based on the work of Suzuki [11]):

$$
\min _ {\delta_ {i}, \phi_ {i}} \sum_ {i \in \Omega} \phi_ {i} C _ {i},\tag{1}
$$

Subject to:

$$
\delta_ {i} \in \{0, 1 \} \quad \forall i \in \Omega ,\tag{2}
$$

$$
r _ {i} \geq \rho \quad \forall i \in \Omega ,\tag{3}
$$

$$
r _ {d} \geq \varepsilon ,\tag{4}
$$

$$
\phi_ {i} \geq \delta_ {i} l \quad \forall i \in \Omega\tag{5}
$$

$$
\phi_ {i} \leq \delta_ {i} Q \quad \forall i \in \Omega ,\tag{6}
$$

$$
r _ {i} + \phi_ {i} \leq Q \quad \forall i \in \Omega .\tag{7}
$$

$$
r _ {i} = \left\{ \begin{array}{l l} \theta - (m _ {i} + \delta_ {i} a _ {i}) / \sigma , & \text { if   } i = 1 \\ r _ {i - 1} + \phi_ {i - 1} - (\delta_ {i - 1} a _ {i - 1} + m _ {i} + \delta_ {i} a _ {i}) / \sigma , & \text { if   } i \neq 1. \end{array} \right.\tag{8}
$$

$$
r _ {d} = r _ {n} + \phi_ {n} - (\delta_ {n} a _ {n} + m _ {d}) / \sigma .\tag{9}
$$

where:

$\delta _ { i } =$ 1 if truck stop i is selected as a refueling point, 0 otherwise $\phi _ { i } = $ nonnegative amount of fuel (gallons) to purchase at truck stop i

$r _ { i } =$ nonnegative amount of fuel in tank either at truck stop i before buying fuel (if δ =1) or at the point nearest to i along the route $( \mathrm { i f } \ \delta _ { i } { = } 0 )$ (see Fig. 1)

$r _ { d } =$ remaining fuel at the <sup>fi</sup>nal destination (d).

Note that the above model minimizes the cost of buying fuel between o and d while ensuring that: (i) the remaining fuel does not fall below ρ at any point in the route (constraint 3), (ii) the ending fuel is larger than or equal to ε (constraint 4), (iii) the minimum purchase quantity is l at any truck stop (constraints 5 and 6), and (iv) the sum of remaining fuel in the tank (before buying fuel) and the amount of purchased fuel does not exceed the tank capacity at any truck stop (constraint $7 ) .$ . We veri<sup>fi</sup>ed that the above model, when solved using the simplex algorithm in conjunction with the branch-and-bound method, generally gives the same solution as ProMiles (one of the most-widely used fuel optimizers in the <sup>fi</sup>eld).

## 3. Proposed method

## 3.1. Basic framework

We argued in the previous section that the major limitations of the existing fuel optimizers are: (i) they upset truck drivers by con<sup>fi</sup>scating their freedom to choose truck stops, and (ii) they do not consider dynamic <sup>fl</sup>uctuations of fuel prices. Our basic approach is to overcome these limitations by: (i) allowing drivers to choose truck stops, and (ii) taking advantage of dynamic price <sup>fl</sup>uctuations. To use our method, a carrier must satisfy the following two conditions. First, all trucks must be equipped with both GPS and satellite-communication systems. Second, a carrier must have access to the fuel-price database from OPIS (Oil Price Information Service), which updates the price of each truck stop daily (U.S. and Canada).

Simply stated, our method allows drivers to freely choose a truck stop in every fueling occasion, but requires them to follow instructions on: (i) how much fuel to buy, and (ii) when to buy fuel (before or after rest). Notice that this approach con<sup>fi</sup>scates the drivers' freedom to choose the fueling amount, but not the freedom to choose truck stops. We employ this approach because our interviews with TL carriers and truck drivers suggest that, while con<sup>fi</sup>scating their freedom to choose truck stops tends to upset drivers, con<sup>fi</sup>scating their freedom to choose the fueling quantity or the timing of fueling (before or after rest) does not upset drivers. Our method consists of two parts; Before– After method and Min–Max method.

## 3.2. Before–After method

The basic idea of this method is to take advantage of fuel price changes that may take place during the time a driver is taking an overnight rest at a truck stop. In the U.S., truck drivers' driving and resting times are strictly regulated by the hours-of-service (HOS) rule. Roughly speaking, the HOS rule states that, after a driver is on duty for 14 hours (or 11 hours h of truck driving, whichever comes <sup>fi</sup>rst), the driver must rest for 10 consecutive hours (i.e., overnight rest, which usually takes place at the parking area of truck stops — see [15]). Since truck stops change fuel prices everyday, it is possible for a driver to observe a change of fuel price at a truck stop while he or she is taking an overnight rest. Our approach is to take advantage of such dynamic price changes. Speci<sup>fi</sup>cally, when a driver takes an overnight rest at a truck stop and buys fuel at the same time (overnight rest is typically combined with refueling), the driver is instructed to: (i) buy fuel after the rest if the fuel price is expected to change during the rest time such that the price after the rest is lower than that before the rest, or (ii) buy fuel before the rest otherwise.

## 3.3. Min–Max method

Truck drivers often buy fuel more than once during a trip. In this case drivers will face different fuel prices between the <sup>fi</sup>rst and the second (or third, etc.) fuel stops, because the location and time (date) of fuel stops are different. The basic idea of the Min–Max method is to take advantage of such dynamic and cross-section price variances that exist between consecutive fuel stops. Speci<sup>fi</sup>cally, once a driver stops at a truck stop (T ), our method compares the latest price at this truck stop (current price) and the expected fuel price at subsequent fuel stops, and decides whether the driver should “top off” at $T _ { s } ,$ or buy only the minimum amount (l). A driver is instructed to top-off if the expected future price is higher than the current price, but is instructed to buy the minimum amount otherwise (therefore the driver buys the maximum amount of fuel when the price is low, and buys the minimum amount when the price is high).

Readers should note that, although in theory the Min–Max method can only be used for long trips that involve two or more fuel stops, it can often be used for short trips that involve only one fuel stop. Speci<sup>fi</sup>cally, the method may be applied to a “one-stop” trip if the destination (route) of the subsequent trip is known in advance (prior to the dispatch time of the “current” trip). Notice that if the route of the next trip is known in advance (our interviews with carriers indicate that this condition is true in most TL trips), one can combine the “current” and the “subsequent” trips to form a longer trip, so that the resulting trip will most likely involve more than one fuel stop (which is now suitable for the Min–Max method).

## 3.4. Dynamic programming formulation

Our method can be formulated as a stochastic dynamic programming model, where each stage is de<sup>fi</sup>ned by the fueling occasion, and the state is de<sup>fi</sup>ned by the amount of fuel yet to be purchased before reaching the destination. Let $\lambda _ { s }$ and $\phi _ { s }$ be the decision variables indicating the timing (before or after rest) and the quantity (min or max) of refueling at stage s (stages are numbered backwards as S, S−1, …, 3, 2, 1, where S is the <sup>fi</sup>rst fueling occasion), and $f _ { s } { * } ( G _ { s } )$ be the cost expected from the use of the optimal policy at stage s and onward. Our objective is to minimize the following $f _ { s } ^ { * } ( \bar { G } _ { s } )$ function at each stage s:

$$
f _ {s} ^ {*} (G _ {s}) = \min _ {\lambda_ {s}, \phi_ {s}} \left\{\left[ \lambda_ {s} C _ {s} + (1 - \lambda_ {s}) \int_ {0} ^ {\infty} C _ {s} ^ {+} g \left(C _ {s} ^ {+}\right) d C _ {s} ^ {+} \right] \phi_ {s} + \sum_ {i \in \Psi_ {s}} p (i | \phi_ {s}) f _ {s - 1} ^ {*} \left(G _ {s} - \phi_ {s} + \frac {2 a _ {i}}{\sigma}\right) \right\}\tag{10}
$$

Subject to:

$$
\lambda_ {s} \in \{0, 1 \} \quad \forall s\tag{11}
$$

$$
\phi_ {s} \in \{l, Q - r _ {s} \} \quad \forall s\tag{12}
$$

$$
G _ {s} = \varepsilon - r _ {s} + R _ {s} / \sigma \quad \forall s\tag{13}
$$

where

$G _ { s } =$ state variable for stage s (total gallons yet to be purchased during the trip),

$\lambda _ { s } =$ 1 if buying fuel before the rest at stage s (truck stop s), 0 otherwise,

$C _ { s } =$ fuel price per gallon at truck stop s before the rest (assumed to be known from OPIS data),

$C _ { s } ^ { + } =$ fuel price per gallon at truck stop s after the rest (stochastic), $g ( C _ { s } ^ { + } ) =$ probability density function (PDF) of $C _ { s } ^ { + } ,$

$p ( i | \phi _ { s } ) \ d t$ probability that truck stop i will be chosen for the next (s−1) fueling occasion given $\phi _ { s } ,$

$\boldsymbol { \Psi } _ { s } =$ set of candidate truck stops located in between truck stop s and the <sup>fi</sup>nal destination,

$R _ { s } =$ remaining distance to destination d from $T _ { s }$ (truck stop used in stage $\textstyle s \to a _ { s } + \sum _ { i \in \Psi _ { s } } m _ { i } + m _ { d }$

The above dynamic program, however, is dif<sup>fi</sup>cult to solve for multiple reasons. First, it is dif<sup>fi</sup>cult to accurately calculate $r _ { s }$ (remaining fuel) in each stage s, so that the state variable $\left( G _ { s } \right)$ in each stage s (i.e., current state) is unknown. Although in theory it is possible to obtain the value of $r _ { s }$ in every stage by asking truck drivers to report $r _ { s }$ via the satellite communication system (or by using a remote engine monitoring system), carrier X believes that it is not practical to do so for the following reasons: (i) fuel indicators of heavy-duty trucks (including those of remote monitoring systems) are not accurate, and (ii), drivers may not honestly report $r _ { s }$ values (some drivers prefer to top off at every fuel stop, so that they may be tempted to undervalue $r _ { s } ) .$ Second, the above model requires that the expected fuel prices of all future stages be known in advance, but in practice it is dif<sup>fi</sup>cult to accurately forecast future fuel prices beyond those of the immediate-next fuel stop (s−1) (we will discuss this issue later). Given these conditions, we decompose the problem into two parts, i.e., the timing (before or after) and the quantity (min or max) problems, and solve each part (problem) independently by using a simple heuristic.

## 3.5. Heuristic: The Before–After problem

The before–after (i.e., timing) problem can be expressed as follows (to be solved at each stage s):

$$
\min _ {\lambda_ {s} \in \{0, 1 \}} \left\{\lambda_ {s} C _ {s} + (1 - \lambda_ {s}) \int_ {0} ^ {\infty} C _ {s} ^ {+} g \left(C _ {s} ^ {+}\right) d C _ {s} ^ {+} \right\}\tag{14}
$$

Given the expected value of $C _ { s } ^ { + } ,$ the solution to this problem can be obtained by using the following logic:

$$
\lambda_ {s} = \left\{ \begin{array}{l} 1 \text {   if   } C _ {s} \leq \int_ {0} ^ {\infty} C _ {s} ^ {+} g (C _ {s} ^ {+}) d C _ {s} ^ {+} \\ 0 \text {   otherwise   } \end{array} \right.\tag{15}
$$

We obtain (forecast) the expected value of $C _ { s } ^ { + }$ by using a timeseries econometric model that is calibrated (trained) with the OPIS data. We will discuss the detailed speci<sup>fi</sup>cations of this econometric model later.

## 3.6. Heuristic: The Min–Max problem

Given the lack of information on $G _ { s }$ and the problem with predicting fuel prices beyond the (immediate) next stage $( s - 1 ) ,$ it is dif<sup>fi</sup>cult to solve the Min–Max problem. Thus, we determine the value of $\phi _ { s }$ in each stage s by a heuristic method that considers only the fuel price of the current stage (s) and the immediate next stage $( s - 1 )$ Let $\pmb { \Lambda } _ { s - 1 } ^ { l } \in \Psi _ { s }$ and ${  { \Lambda } } _ { s - 1 } ^ { h } \in \varPsi _ { s }$ be the set of candidate truck stops for the next fueling occasion $( s - 1 )$ given $\phi _ { s } = l$ and $\phi _ { s } { = } Q { - } r _ { s }$ respectively (such that $p ( i | { \phi _ { s } } = l ) > 0 \forall i \in { \Lambda } _ { s - 1 } ^ { l } ; p ( i | { \phi _ { s } } = Q - r _ { s } ) > 0 \forall i \in { \Lambda } _ { s - 1 } ^ { h } ) ,$ . Also let $C _ { s - 1 } ^ { l }$ and $C _ { s - 1 } ^ { h }$ be the expected fuel price of the next stage $( s - 1 )$ given $\phi _ { s } = l$ and that given $\phi _ { s } = Q - r _ { s } ,$ respectively. $C _ { s } ^ { l } .$ and $C _ { s - } ^ { h }$ can be obtained by the following formulas:

$$
C _ {s - 1} ^ {l} = \sum_ {i \in \Lambda_ {s - 1} ^ {l}} p (i | \phi_ {s} = l) \int_ {0} ^ {\infty} C _ {i} ^ {+} q \left(C _ {i} ^ {+}\right) d C _ {i} ^ {+},\tag{16}
$$

$$
C _ {s - 1} ^ {h} = \sum_ {i \in \Lambda_ {s - 1} ^ {h}} p (i | \phi_ {s} = Q - r _ {s}) \int_ {0} ^ {\omega} C _ {i} ^ {+} q \left(C _ {i} ^ {+}\right) d C _ {i} ^ {+}
$$

where $C _ { i } ^ { + }$ is the fuel price of i at stage $s \mathrm { - } 1$ before the rest (next day price at $i ) ,$ and $q ( C _ { i } ^ { + } )$ is the PDF of $C _ { i } ^ { + }$ .

Our objective is to contrast the prices $C _ { s } , C _ { s - 1 } ^ { l } , C _ { s - 1 } ^ { h }$ , and choose $\phi _ { s }$ such that we utilize the lowest price as much as possible and avoid the highest price to the extent possible. We perform this task by using a two-step procedure. First, we determine the price to utilize $( C ^ { u } )$ and the price to avoid $( C ^ { - u } )$ as:

$$
C ^ {u} = \min \left(C _ {s}, C _ {s - 1} ^ {l}, C _ {s - 1} ^ {h}\right), \quad C ^ {- u} = \max \left(C _ {s}, C _ {s - 1} ^ {l}, C _ {s - 1} ^ {h}\right)\tag{17}
$$

Second, the result of the <sup>fi</sup>rst step is applied to the logic shown in Table 1 to derive $\phi _ { s } .$ (Notice that this logic attempts to maximize the amount of fuel purchased at $C ^ { u } ,$ , and avoid or minimize the fuel purchased at $C ^ { - u } ) .$ . As before, we obtain the expected $C _ { i } ^ { + \cdot } s$ from the econometric model trained with the OPIS data.

## 4. Decision support system

In this section we discuss the decision support system designed to utilize the proposed decision support model. Since the critical factor of a decision support system is the quality of information infrastructure $[ 8 ] ,$ , we focus on discussing how the system generates and utilizes the data needed to operate the decision support model. We also discuss advantages and disadvantages of the system.

## 4.1. The system procedure

The system performs the following four tasks sequentially (see Fig. 2 for the system overview). The <sup>fi</sup>rst task is to identify the “current” truck stop location. Once a truck stops at a given truck stop (T ) for refueling, the driver sends the following information to the company (carrier X) via the satellite communication system: (i) name of $T _ { s }$ (chain name only; e.g., Pilot, Flying-J), and (ii) how long the driver intends to stay at $T _ { s } .$ The system uses the <sup>fi</sup>rst driver input $( T _ { s }$ name) and the truck's current position given by the GPS locator (this data is readily available at the company headquarters) to identify the exact location of $T _ { s } .$ Notice that, although our system works in conjunction with the GPS, the driver input on truck-stop name is still needed to identify the exact location of $T _ { s } ,$ because when $T _ { s }$ is located adjacent to another truck stop (which happens occasionally) the GPS cannot distinguish between the two truck stops.

Proper fueling quantity at stage s

<table><tr><td colspan="2">If (possible scenarios)</td><td>Then (solution)</td><td rowspan="2">Because (reasons) $^a$ </td></tr><tr><td> $C^u=$ </td><td> $C^{-u}=$ </td><td> $\phi_s=$ </td></tr><tr><td> $C_s$ </td><td> $C_{s-1}^l$ </td><td> $Q-r_s$ </td><td> $C_s$  is least expensive</td></tr><tr><td> $C_s$ </td><td> $C_{s-1}^h$ </td><td> $Q-r_s$ </td><td> $C_s$  is least expensive</td></tr><tr><td> $C_{s-1}^l$ </td><td> $C_{s-1}^h$ </td><td>l</td><td>Buy fuel at  $C^u$ </td></tr><tr><td> $C_{s-1}^h$ </td><td> $C_{s-1}^l$ </td><td> $Q-r_s$ </td><td>Avoid buying fuel at  $C^{-u}$ </td></tr><tr><td> $C_{s-1}^l$ </td><td> $C_s$ </td><td>l</td><td> $C_s$  is most expensive</td></tr><tr><td> $C_{s-1}^h$ </td><td> $C_s$ </td><td>l</td><td> $C_s$  is most expensive</td></tr></table>

<sup>a</sup> We assume, without the loss of generality, that the expected $R _ { s - 1 }$ (remaining route distance from the truck stop chosen for stage s−1) given $\phi _ { s } = l \mathrm { i } s$ greater that the given $\phi _ { s } = Q - r _ { s } .$

![](/api/attachments/8SQG3HW5/fulltext/images/b8eaea3c0965c0393daf64106b94b916755ad57a271cc20c855416eb1dd411d0.jpg)  
Fig. 2. Decision support system overview.

The second task is to apply the Before–After method as follows. First, the judgment on whether the price of $T _ { s }$ will change while the driver stays at $T _ { s }$ is made by: (i) using the driver input on expected duration of stay at $T _ { s }$ (second driver input obtained during the <sup>fi</sup>rst task), and (ii) assuming that $T _ { s }$ price will change precisely at 12 am. Second, if the system <sup>fi</sup>nds that the price is not expected to change during the rest, it will omit the rest of the procedure and chooses to buy fuel before the rest. Third, if the system <sup>fi</sup>nds that the price is expected to change during the rest, it extracts the latest (current) price of $T _ { s }$ from the OPIS data and forecasts (using the econometric model) whether this price will increase or decrease after the rest. The system then determines when to buy fuel using the Before–After procedure discussed earlier.

The third task is to apply the Min–Max method as follows. First, the system identi<sup>fi</sup>es $\Lambda _ { s - 1 } ^ { l }$ and $\Lambda _ { s - 1 } ^ { h }$ by: (i) <sup>fi</sup>nding the “con<sup>fi</sup>dence intervals” of the distance between two consecutive fuel stops given $\phi _ { s } = l$ and $\phi _ { s } { = } Q { - } r _ { s }$ respectively (using the carrier's historical data), and (ii) pooling truck stops that are located within these con<sup>fi</sup>dence intervals. Second, the system uses the econometric model discussed earlier to forecast future (stage s − 1) fuel prices of all the truck stops in $\Lambda _ { s } ^ { l }$ and $\Lambda _ { s } ^ { h } .$ . Third, the system then: (i) computes the expected future fuel prices $C _ { s - 1 } ^ { l }$ and $C _ { s - 1 } ^ { h } ,$ and (ii) determines the refueling quantity $\phi _ { s }$ by using the Min–Max procedure discussed earlier. (We assume, based on the inputs given by carrie ${ \mathrm { X } } ,$ that truck drivers buy fuel exactly once everyday; i.e., a “stage” represents a “day” in our system.)

The <sup>fi</sup>nal task is to transmit the model solution. Once the driver instruction that indicates both the timing and quantity of fueling is generated by the above procedure (e.g., top-off after rest, buy 50 gal before rest, etc.), the system sends the instruction to the driver via the satellite communication system. Our experiments indicate that, once the system is automated (no human work is needed at the company side), it takes less than 15 s for a driver to get the instruction after sending the initial information.

## 4.2. Advantages and disadvantages

Our decision support system has two advantages over the standard fuel optimizers. First, our system does not con<sup>fi</sup>scate the drivers' freedom to choose truck stops, so that it should not upset drivers. This condition implies that: (i) our method is expected to attain higher driver compliance rates than standard fuel optimizers, and (ii) our method should not increase driver turnover rates of carriers. Second, our system may be more robust (than standard fuel optimizers) to the violation of the assumption that trucks always follow the shortest routes. Notice that if trucks do not follow the shortest routes (which happens occasionally), standard fuel optimizers may not work at all, as they require that trucks strictly follow the shortest routes. In contrast, our system may still work (partially) under such circumstances, because the Before–After method works perfectly even when trucks are not following the shortest routes.

One disadvantage of our system is that it employs a “passive” approach. Notice that our system uses a “reactive” decision model that reduces the cost of fuel after a driver has chosen the truck stop, while the fuel optimizers use “proactive” models that aggressively seek truck stops with the lowest fuel prices. This condition suggests that our model may face stricter constraints (smaller feasible regions) than standard fuel optimizers. Commercial fuel optimizers, therefore, may outperform our system in terms of the “gross bene<sup>fi</sup>t” realized by carriers (cost savings before adjusting for driver compliance rates, etc.).

## 5. Econometric model

The previous section indicated that econometric price forecasting is an integral part of our system. In this section we describe our econometric model and empirically test its forecasting accuracy.

## 5.1. Basic approach

Our basic approach is to predict future fuel price at each truck stop by using an exogenous variable that is readily available from the OPIS data. This exogenous variable, which is called “truck stop cost” (denoted C(T)), basically represents the total cost a truck stop has paid to acquire a gallon of diesel fuel on a given day (i.e., “the cost of goods sold”). Typically, C(T) includes the following cost items: (i) purchase price of diesel fuel at the nearest pipeline terminal (rack price), (ii) freight cost (for transporting the purchased fuel from the pipeline to the truck stop), and (iii) federal and state taxes. The OPIS data of day t contains the (estimated) C(T) of day t (as of 8 am) for every truck stop in the database.

It should be noted that, as a general rule, truck stops determine their retail prices every day by referring to C(T) of the previous day. This pattern implies that C(T) of day t is a good predictor of the retail price of day t+1 (next day). Given this condition, we employ a forecasting approach where C(T) of a truck stop (i) on day t is used as a predictor of the retail fuel price at i on day t+1. Our experience indicates that this approach provides substantially better forecasting results than the standard auto-regressive type models. Notice that this approach allows us to forecast only future prices for the next day (for the next stage s − 1). While it is possible to forecast future prices beyond the next day by using auto-regressive models, we do not use this approach as it will substantially reduce the forecasting accuracy.

## 5.2. Model specification

Let $C _ { i t }$ be the fuel price (per gallon) at truck stop i on day t, and $C ( T ) _ { i t }$ be the truck stop cost of i on day t. We use the following fixed-effect specification to model the relationship between C(T) and $C _ { i t } \mathrm { : }$

$$
C _ {i t} = \sum_ {i} (\alpha_ {i} T _ {i}) + \beta_ {0} C (T) _ {i t - 1} + \gamma_ {i t}\tag{18}
$$

where $T _ { i }$ is a dummy (0/1) variable representing the $i ^ { \mathrm { { t h } } }$ truck stop, α 's and $\beta _ { 0 }$ are model parameters to be derived empirically, and $\gamma _ { i t } \mathbf { \dot { s } }$ are stochastic regression residuals (assumed to follow a normal distribution whose mean is zero). We also tested (empirically by using the OPIS data obtained from carrier X) a variety of other functional forms to model the relationship between $C ( T ) _ { i t }$ and $C _ { i t }$ (including several non-linear and random-effects speci<sup>fi</sup>cations), but the above speci<sup>fi</sup>- cation almost always provided the best <sup>fi</sup>t.

Sample empirical results of our econometric model are shown in Table 2. The model was calibrated with the OPIS data that contain price and cost information of 351 truck stops over 175 days. We used the data from the <sup>fi</sup>rst 173 days (60,423 records) to calibrate the model, and reserved the data from the last 2 days (702 records) to forecast future prices. Results indicate that: (i) the model gives a good <sup>fi</sup>t to the calibration sample $\scriptstyle \left( R ^ { 2 } = 0 . 9 4 0 \right)$ and (ii) the model does a reasonably good job of forecasting future prices $\scriptstyle ( R ^ { 2 } = 0 . 8 5 2 ;$ i.e., the model can explain over 85% of tomorrow's price variances). Results also show that the model attains the hit rate of 0.821 in the forecasting sample, which implies that the model can correctly predict the direction of future price movement (whether the price will go up or go down) roughly 82.1% of the time. Notice that this <sup>fi</sup>gure is substantially better than 50% (random pick).

Table 2 Regression results

<table><tr><td colspan="2"></td><td>Calibration samplea</td><td>Forecasting sample</td></tr><tr><td rowspan="2">Sample size</td><td>Number of truck stops</td><td>351</td><td>351</td></tr><tr><td>Total records for calibration</td><td>60,423</td><td>702</td></tr><tr><td rowspan="2">Coefficients</td><td> $\alpha_i$ </td><td>_b</td><td>-</td></tr><tr><td> $\beta_0$ </td><td>1.0606*</td><td>-</td></tr><tr><td rowspan="6">Fit statistics</td><td>SSRc</td><td>453.264</td><td>7.004</td></tr><tr><td> $R^2$ </td><td>0.940</td><td>0.852</td></tr><tr><td>Parameters estimated</td><td>352</td><td>-</td></tr><tr><td>MSEd</td><td>0.008</td><td>-</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.940</td><td>-</td></tr><tr><td>Hit ratee</td><td>-</td><td>0.821</td></tr></table>

⁎p-valueb0.0001.  
Model is calibrated by the ordinary least squares method.  
<sup>b</sup> Individual (truck stop) constants are not reported for space limitations.  
<sup>c</sup> Sum of squared residuals.  
<sup>d</sup> Mean squared error.  
<sup>e</sup> Proportion of sample observations for which the model correctly predicted the future price movement (up or down).

## 6. Simulation experiment

In this section we perform a series of simulation experiments to investigate how well the proposed method works under practical conditions. The goal is to compare the performance of our model with that of standard fuel optimizers. To obtain realistic results, the simulation parameters are speci<sup>fi</sup>ed mainly by using the actual data obtained from a variety of reliable sources. Most of the data are obtained from carrier X (we worked jointly with carrier X to design the experiments). Other data sources include the following: (i) OPIS data, (ii) U.S. government publications, (iii) regression results of Table 2, (iv) ProMiles, and (v) interviews with four TL carriers (including carrier X), three truck drivers, two fuel-optimizer vendors, and two truck-stop chains. Selected simulation parameters are shown in Table 3.

## 6.1. Experiment

We randomly generate numerous hypothetical (yet realistic) truck refueling problems, and solve each problem by using the following three methods: benchmark, proposed, and fuel-optimizer methods. The benchmark method calculates the refueling cost for each problem by using the logic that mimics actual (random) refueling behavior of truck drivers; i.e., it gives the upper-bound cost for each problem (cost without the use of any cost-saving method). The fuel-optimizer method and the proposed method calculate the cost for each problem by applying the procedures discussed in Sections 2 and 3, respectively.

Our experiments are performed as follows. First, for each problem (load), the problem details such as: (i) route characteristics (e.g., route distance, dispatch time, number of truck stops along the route), (ii) vehicle characteristics (e.g., tank capacity, starting fuel, fuel consumption rate at various points along the route), and (iii) driver characteristics (e.g., daily mileage, driver preference on overnight rest locations) are determined randomly (see Table 3 for probability distributions of random variables). Second, for each truck stop along the route, detailed store characteristics, such as the miles from the previous truck stop, out-of-route distance, and “actual” diesel prices (from day 1 to day k, where k denotes the number of days required to complete the route), as well as the exact time of price change (e.g.,12 am) are again determined randomly. Third (for the proposed method only), the “forecasted” (next day) fuel price of each truck stop along the route is created by adding a stochastic error term (forecast error term) to the “actual” fuel price determined in the previous step (day 1 to day k). Fourth, once all the problem details are speci<sup>fi</sup>ed by the above procedure, the problem is solved by using the three methods discussed earlier.

We perform the above problem-solving task 25 times to complete a simulation trial. The 25 problems solved in each trial are “consecutive” problems, such that the conditions observed at the end of one problem (trip) are used as the starting conditions for the next problem (trip). Each time a simulation trial is completed, the cumulative cost of vehicle refueling (25 trips) is calculated for each method. This cumulative cost will be used as the performance measure. We repeat the trial 1000 times to complete an experiment. Thus, in each experiment, we generate and solve 25,000 vehicle refueling problems. To obtain robust simulation results, we perform three experiments (generate and solve 75,000 problems).

## 6.2. Modeling drivers' stochastic fueling behavior

A challenging part of our experiment is to mimic the stochastic fueling behavior of truck drivers (benchmark and proposed methods). We model drivers' fueling behavior as follows. First, based on our interviews with carrier managers and truck drivers, we create several ways (logics) of emulating drivers' fueling behaviors (time, place, and quantity of fuel purchases). Second, we test each logic by conducting small simulation experiments. Speci<sup>fi</sup>cally, we (i) apply each logic to a variety of (randomly generated) vehicle-refueling problems to simulate drivers' fueling behaviors under each logic, (ii) collect summary statistics for each logic (e.g., purchase quantity per fuel stop), and (iii) compare the collected data with the summary statistics derived from the actual fueling data (over 6000 fueling records) provided by carrier X. Third, we choose the <sup>fi</sup>nal logic based on: (i) the similarity of summary statistics between simulated and actual data, and (ii) the degree to which the logic does not con<sup>fl</sup>ict with fueling habits reported by drivers.

Table 3  
Selected simulation parameters

<table><tr><td></td><td>Distributiona</td><td>Parameters</td><td>Data sourceb</td><td>Sample</td></tr><tr><td colspan="5">Random Variables</td></tr><tr><td>Variance of avg. price across regionsc</td><td>Normal</td><td>Std=0.0826</td><td>US DOE [14]</td><td>900</td></tr><tr><td>Diesel price within region (excl. tax)</td><td>Normal</td><td>Mean=2.416, Std=0.362</td><td>OPIS data</td><td>61,125</td></tr><tr><td>Price movement (from day to day)</td><td>Normal</td><td>Mean=0, Std=0.1617</td><td>OPIS data</td><td>61,126</td></tr><tr><td>Price forecast errord</td><td>Normal</td><td>Mean=0, Std=0.09996</td><td>OPIS regression</td><td>61,125</td></tr><tr><td>TS (truck stop) price change time</td><td>Uniform</td><td>Min=9:00 pm, Max=3:00 am</td><td>(TS), (D)</td><td>-</td></tr><tr><td>Total trip miles (actual miles)e</td><td>Weibullf</td><td>-</td><td>Carrier X</td><td>5157</td></tr><tr><td>Tank capacity (200 or 240 gal)e</td><td>Bernoulli</td><td>-</td><td>Carrier X</td><td>&gt;500</td></tr><tr><td>Starting fuel (% of tank filled)</td><td>Uniform</td><td>Min=20%, Max=100%</td><td>Carrier X</td><td>-</td></tr><tr><td>Daily mile (excluding out-of-route)e</td><td>Normalg</td><td>-</td><td>Carrier X</td><td>1258</td></tr><tr><td>Daily on-duty time</td><td>Normalg</td><td>Mean=12.5, Std=0.5 (max=14)</td><td>HOS regulation</td><td>-</td></tr><tr><td>Miles from one TS to another</td><td>Gamma</td><td>Loc=-0.05, scale=80.5, shape=0.5</td><td>ProMiles</td><td>532</td></tr><tr><td>Out-of-route miles to TS (one way)</td><td>Exponential</td><td>1/mean=2.46</td><td>ProMiles</td><td>1177</td></tr><tr><td>Miles per gallon (TS to TS)e</td><td>Normal</td><td>-</td><td>Carrier X</td><td>1260</td></tr><tr><td>Prob. that subsequent route is known</td><td>Bernoulli</td><td>Prob (known)=0.65</td><td>Carrier X</td><td>-</td></tr><tr><td>Prob. that a driver sleeps at TS</td><td>Bernoulli</td><td>Prob (TS sleep)=0.85</td><td>US DOT [15]</td><td>2046</td></tr><tr><td>Prob that driver refuels before sleep</td><td>Bernoulli</td><td>Prob (before sleep)=0.5</td><td>Carrier X, (D)</td><td>-</td></tr><tr><td colspan="5">Fixed Parameters</td></tr><tr><td>OPIS data available time</td><td>-</td><td>11:00 am</td><td>Carrier X</td><td>-</td></tr><tr><td>Min fuel to be maintained at all times</td><td>-</td><td>20% of tank capacity</td><td>Carrier X</td><td>-</td></tr><tr><td>Min gal. to refuel</td><td>-</td><td>70 gal</td><td>Carrier X, (SV)</td><td>-</td></tr><tr><td>Min ending fuel (% of tank capacity)h</td><td>-</td><td>0.5 (0.8 if price of next route is higher)</td><td>Carrier X, (SV)</td><td>-</td></tr><tr><td>Candidate TS for next stage ( $\Lambda_{s-1}^{l}$ )</td><td>-</td><td>Truck stops within 300–500 miles</td><td>Carrier X, (D)</td><td>6072</td></tr><tr><td>Candidate TS for next stage ( $\Lambda_{s-1}^{h}$ )</td><td>-</td><td>Truck stops within 640–840 miles</td><td>Carrier X, (D)</td><td>6072</td></tr><tr><td>Prob. of using TS i ( $p(i)\phi_s=l$ )</td><td>-</td><td>Uniformly distributed within ( $\Lambda_{s-1}^{l}$ )</td><td>Carrier X, (D)</td><td>-</td></tr><tr><td>Prob. of using TS i ( $p(i)\phi_s=Q-r_s$ )</td><td>-</td><td>Uniformly distributed within ( $\lambda_{s-1}^{h}$ )</td><td>Carrier X, (D)</td><td>-</td></tr><tr><td>Prob. driver follows shortest route</td><td>-</td><td>Prob (follow)=1.00</td><td>-</td><td>-</td></tr><tr><td>Prob. comply with fueling instruction</td><td>-</td><td>Prob (comply)=1.00</td><td>-</td><td>-</td></tr></table>

<sup>a</sup> When data are available, distributions are determined mainly by the goodness of <sup>fi</sup>t.  
<sup>b</sup> Descriptions of data sources: (D) = interviews with truck drivers, (TS) = interviews with truck stop chains, (SV)=interviews with fuel-optimizer vendors.  
<sup>c</sup> Following the U.S. DOE practice, we assume that there are nine regions in the U.S. (a truck moves from one region to another roughly every 500 miles).  
<sup>d</sup> Applies only to the proposed method. This error term is added to the simulated “actual” fuel prices to create the price forecasts (this error term follows the forecasting-error distribution obtained from the OPIS regression results of Table 2)  
<sup>e</sup> Parameters of these variables cannot be reported for con<sup>fi</sup>dentiality reasons.  
<sup>f</sup> This distribution is truncated such that the minimum distance is 500 miles (because the majority of business for Carrier X are loads with more than 500 miles).  
<sup>g</sup> These distributions are truncated because of the upper bounds implied by the hours of service (HOS) rule.  
<sup>h</sup> This constraint applies only to the fuel optimizer method.

## 6.3. Performance measure

As mentioned previously, we measure the performance of each method by the cumulative cost of refueling (over 25 consecutive trips). This cost, however, does not accurately measure the performance of each method unless an adjustment is made to account for the remaining (residual) fuel. Notice that the remaining fuel at the end of a trial may be different from one method to another, because in each method the location (where), quantity (how much), and time (when) of fuel purchases are (most likely) different. Since the cost of buying the “residual” fuel is included in the cumulative cost, we must exclude this particular portion of the cost from the performance measure to compare the three methods appropriately.

We measure the performance of each method (in each trial) by using the following cost formula:

$$
\frac {C _ {\mathrm{cum}}}{G _ {\mathrm{cum}}} (G _ {\mathrm{cum}} - r _ {\mathrm{fin}})\tag{19}
$$

where $C _ { \mathrm { c u m } }$ is the cumulative cost of buying fuel during the trial (25 trips), G is the total fuel (gallons) purchased during the trial, and $r _ { \mathrm { f i n } }$ is the remaining fuel at the end of the trial. Note that the above formula measures the cost of fuel purchased and consumed during the trial. Also note that we ignore the cost of starting fuel (gallons given at the start of a trial). This is because: (i) it is a sunk cost, and (ii) it equally affects the costs of all the methods (the starting fuel is identical across all the three methods in each trial).

## 6.4. Assumptions

We employ the following assumptions during our experiments. Given space constraints, we discuss only selected assumptions here. Further details of our assumptions are available upon request.

## 6.4.1. OPIS data available time

Each day, OPIS data become available to subscribers sometime between 10am and noon. This condition implies that, during the morning of day t (before OPIS data are received), a carrier has no means of knowing the “latest” (day t) fuel price at truck stops. This issue (data receiving time) can possibly impact the performance of both the fueloptimizer and our methods, because both methods create fueling instructions by using the latest OPIS data. In our experiments, we assume the following: (i) a carrier receives OPIS data precisely at 11 am every day, and (ii) before 11 am the carrier uses OPIS data from the previous day to create fueling instructions (proposed or fuel-optimizer method).

6.4.2. Minimum ending fuel (this parameter applies to the fuel-optimizer method only)

Many fuel-optimizer users prefer to set the ending fuel (ε) such that: (i) ε=large value, if the average fuel price of the subsequent route is higher than that of the current route (so that the truck may avoid buying expensive fuel in the next trip), and (ii) ε=small value, if the average fuel price of the subsequent route is lower than that of the current route (so that the truck will buy cheap fuel in the next trip). To incorporate such user preferences, we assume the following: (i) ε=80% of tank capacity if the subsequent route is known in advance and the average fuel price of this subsequent route is higher than that of the current route (average fuel prices are calculated from the latest OPIS data), and (ii) ε=50% of tank capacity otherwise.

Table 4 Simulation results

<table><tr><td></td><td>Benchmark method</td><td>Prop. method (before-after)</td><td>Prop. method (combined)</td><td>Fuel-optimizer  $method^a$ </td></tr><tr><td colspan="5">Experiment 1. (n=1000)</td></tr><tr><td>Average fuel cost ($)</td><td>7386.6</td><td>7340.1</td><td>7242.6</td><td>7053.8</td></tr><tr><td>Std. deviation</td><td>713.5</td><td>709.1</td><td>702.8</td><td>666.0</td></tr><tr><td>% saving (vs. benchmark)</td><td>0.00</td><td>0.63</td><td>1.95</td><td>4.51</td></tr><tr><td> $t-test (paired t-values)^b$ </td><td>-</td><td>41.845*</td><td>40.684*</td><td>50.216*</td></tr><tr><td colspan="5">Experiment 2. (n=1000)</td></tr><tr><td>Average fuel cost ($)</td><td>7383.8</td><td>7340.6</td><td>7236.4</td><td>7059.5</td></tr><tr><td>Std. deviation</td><td>698.6</td><td>692.3</td><td>688.1</td><td>685.7</td></tr><tr><td>% saving (vs. benchmark)</td><td>0.00</td><td>0.58</td><td>2.00</td><td>4.39</td></tr><tr><td> $t-test (paired t-values)^b$ </td><td>-</td><td>39.011*</td><td>43.694*</td><td>45.148*</td></tr><tr><td colspan="5">Experiment 3. (n=1000)</td></tr><tr><td>Average fuel cost ($)</td><td>7425.6</td><td>7381.4</td><td>7279.2</td><td>7095.3</td></tr><tr><td>Std. deviation</td><td>692.8</td><td>686.8</td><td>683.5</td><td>673.7</td></tr><tr><td>% saving (vs. benchmark)</td><td>0.00</td><td>0.59</td><td>1.97</td><td>4.45</td></tr><tr><td> $t-test (paired t-values)^b$ </td><td>-</td><td>39.328*</td><td>39.533*</td><td>53.915*</td></tr></table>

⁎p-valueb0.001.  
<sup>a</sup> For this method, solutions are obtained by using the simplex algorithm, in conjunction with the branch-and-bound method.  
<sup>b</sup> Paired t-tests comparing the cost of the method in the column and that of the benchmark method.

## 7. Simulation results and implications

Simulation results are shown in Table 4. To simplify our discussions, we report only selected statistics. Observe that two results are reported for the proposed method; i.e., the “Before–After” and the “Combined” results. The former re<sup>fl</sup>ect the cost of the proposed method if only the Before–After method is used, while the latter re<sup>fl</sup>ect the cost if both the Before–After and the Min–Max methods are used (i.e., the latter re<sup>fl</sup>ect the true cost of our method). Notice that, by separately calculating these two costs, we can distinguish the costsaving capability of the Before–After method and that of the Min–Max method.

Cost comparisons under selected scenarios

<table><tr><td rowspan="2"></td><td colspan="6">Possible scenarios (number of trucks = 500 under all scenarios) $^a$ </td></tr><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td></tr><tr><td colspan="7">Scenario descriptions</td></tr><tr><td colspan="7">(a) Route compliance rate (\%)b</td></tr><tr><td>Fuel-optimizer method</td><td>0.90</td><td>0.90</td><td>0.90</td><td>0.95</td><td>0.95</td><td>0.95</td></tr><tr><td>Proposed method</td><td>0.90</td><td>0.90</td><td>0.90</td><td>0.95</td><td>0.95</td><td>0.95</td></tr><tr><td colspan="7">(b) Fueling-schedule compliance rate (\%)c</td></tr><tr><td>Fuel-optimizer methodd</td><td>0.50</td><td>0.55</td><td>0.60</td><td>0.50</td><td>0.55</td><td>0.60</td></tr><tr><td>Proposed method</td><td>0.80</td><td>0.90</td><td>0.90</td><td>0.80</td><td>0.90</td><td>0.90</td></tr><tr><td colspan="7">(c) Driver turnover rate increase (\%)e</td></tr><tr><td>Fuel-optimizer method</td><td>0.05</td><td>0.10</td><td>0.10</td><td>0.05</td><td>0.10</td><td>0.10</td></tr><tr><td>Proposed method</td><td>0.01</td><td>0.01</td><td>0.02</td><td>0.01</td><td>0.01</td><td>0.02</td></tr><tr><td colspan="7">(d) Driver replacement cost ($ per driver)f</td></tr><tr><td>Fuel-optimizer method</td><td>5000</td><td>5000</td><td>5000</td><td>5000</td><td>5000</td><td>5000</td></tr><tr><td>Proposed method</td><td>5000</td><td>5000</td><td>5000</td><td>5000</td><td>5000</td><td>5000</td></tr><tr><td colspan="7">Cost estimates ($,000)</td></tr><tr><td colspan="7">(1) Gross annual cost (unadjusted cost)g</td></tr><tr><td>Fuel-optimizer method</td><td>18,381</td><td>18,381</td><td>18,381</td><td>18,381</td><td>18,381</td><td>18,381</td></tr><tr><td>Proposed method</td><td>18,857</td><td>18,857</td><td>18,857</td><td>18,857</td><td>18,857</td><td>18,857</td></tr><tr><td colspan="7">(2) Costs adjusted for compliance rates</td></tr><tr><td>Fuel-optimizer methodh</td><td>18,851</td><td>18,813</td><td>18,774</td><td>18,830</td><td>18,789</td><td>18,749</td></tr><tr><td>Proposed methodi</td><td>18,954</td><td>18,919</td><td>18,919</td><td>18,944</td><td>18,907</td><td>18,907</td></tr><tr><td colspan="7">(3) Annual driver replacement costsj</td></tr><tr><td>Fuel-optimizer method</td><td>125.0</td><td>250.0</td><td>250.0</td><td>125.0</td><td>250.0</td><td>250.0</td></tr><tr><td>Proposed method</td><td>25.0</td><td>25.0</td><td>50.0</td><td>25.0</td><td>25.0</td><td>50.0</td></tr><tr><td colspan="7">(4) Net annual cost = (2) + (3)</td></tr><tr><td>Fuel-optimizer method</td><td>18,976</td><td>19,063</td><td>19,024</td><td>18,955</td><td>19,039</td><td>18,999</td></tr><tr><td>Proposed method</td><td>18,979</td><td>18,944</td><td>18,969</td><td>18,969</td><td>18,932</td><td>18,957</td></tr><tr><td colspan="7">Cost saving per gallon of fuel (cents)k</td></tr><tr><td>Fuel-optimizer method</td><td>3.27</td><td>2.18</td><td>2.66</td><td>3.53</td><td>2.48</td><td>2.99</td></tr><tr><td>Proposed method</td><td>3.23</td><td>3.68</td><td>3.36</td><td>3.37</td><td>3.83</td><td>3.51</td></tr></table>

<sup>a</sup> Carrier size of 500 trucks is used in our analyses, as this size is similar to that of carrier X.  
<sup>b</sup> Proportion of trip occasions in which drivers strictly follow the shortest route.  
<sup>c</sup> Proportion of fueling occasions in which drivers comply with fueling schedules.  
<sup>d</sup> According to our interviews with fuel-optimizer vendors, the compliance rate typically ranges between 50% and 60%.  
<sup>e</sup> Increase in turnover rate due to the adoption of the method (turnover rate of 100% is assumed before the adoption which roughly re<sup>fl</sup>ects the current turnover rate of carrier X).  
<sup>f</sup> Driver replacement cost (per replacement) is typically \$5000–\$8000 (see, e.g., [1] and [10]).  
<sup>g</sup> This cost is obtained by multiplying the simulation results by: (i) number of trucks, and (ii) number of annual trips/25.  
<sup>h</sup> Cost = (a) ×(b) ×A + (1− (a) ×(b)) ×B (where A = cost of fuel-optimizer method, B = cost of benchmark method).  
<sup>i</sup> Cost=(a)×(b)×J+(1−(a))×(b)×W+(1−(b))×B (where J = cost of our method, W = cost of Before–After method).  
<sup>j</sup> Cost=500×(c)×(d) (for both methods).  
<sup>k</sup> Savings over the benchmark method.

Results of the proposed method indicate that the majority of the cost savings come from the Min–Max method, rather than from the Before–After method. On average, over 70% of the cost savings are attained by the Min–Max method, while less than 30% are attained by the Before–After method. Two possible reasons might explain this phenomenon. First, the Min–Max method takes advantage of the larger price variance than the Before–After method. Recall that the Before–After method takes advantage of only the dynamic price variance, while the Min–Max method takes advantage of both the geographic and dynamic price variances. This pattern implies that the former may face smaller cost-saving opportunities than the latter. Second, as described in Table 3, we considered only the medium and long-distance routes (500 miles or longer) in our experiments (because they constitute the majority of business for carrier X). Since the Min–Max method is designed primarily for those routes with multiple fuel stops (i.e., long-distance routes), its cost savings may become larger as route distances increase.

With regard to the cost-saving potentials, Table 4 indicates that the lowest cost (highest cost saving) is attained by the fuel-optimizer method, followed by the proposed method (combined), the Before– After method, and the benchmark method. This pattern is found consistently across all the three experiments. Roughly speaking, the fuel-optimizer method saves about 4.4% of fuel cost, while our method saves about 2.0% of fuel cost. Given the average fuel price of \$2.416 (see Table 3), these <sup>fi</sup>gures convert to an average saving of 10.7 cents/gal of fuel for the fuel-optimizer method, and an average saving of 4.8 cents/ gal of fuel for our method. (Notice that the former <sup>fi</sup>gure is close to those claimed by fuel-optimizer vendors, which are typically 4 to 11 cents/gal). This condition implies that the cost-saving potential of the fuel-optimizer method may be higher than that of our method.

The above results, however, do not necessarily indicate that the fueloptimizer method always outperforms the proposed method, because the <sup>fi</sup>gures shown in Table 4 merely represent the “gross” costs, which can be attained only if certain “desirable” conditions are satis<sup>fi</sup>ed (e.g., 100% driver compliance rate — see Table 3). To compare the two methods properly, we must evaluate the “net” cost of each method by discounting the gross cost by such factors as driver compliance rates and driver replacement costs. Table 5 compares the net costs of the two methods under selected scenarios. (These scenarios re<sup>fl</sup>ect the “most likely” scenarios and are selected from the many scenarios which we and carrier X analyzed jointly.) The table indicates that, after making the appropriate adjustments, the cost of our method may become lower than that of the fuel-optimizer method under certain (realistic) conditions. We see from the table that, depending on situations, our method may outperform the fuel-optimizer method by more than \$100,000 per year for carriers with 500 trucks. These <sup>fi</sup>gures convert to possible cost savings (of using our method over the standard fuel optimizers) of more than \$1 million for large carriers that have over 10,000 trucks (such as J.B. Hunt Transport and Schneider National).

In short, our simulation results imply two things. First, our method allows carriers to reduce fuel cost considerably (up to 2%) at the point of purchase without con<sup>fi</sup>scating the freedom of truck drivers to choose truck stops. This condition implies that those carriers which do not wish to upset truck drivers by con<sup>fi</sup>scating their freedom may still enjoy up to 2% cost savings by using our method. Second, while the commercial fuel optimizers may outperform our method in terms of “gross” cost savings, the latter may outperform the former in terms of the “net” cost savings. Our analyses indicate that, depending on situations, the cost of our method may become noticeably lower than that of standard fuel optimizers, if the costs are adjusted properly by driver compliance rates and driver replacement costs.

## 8. Conclusions and limitations

Today, the ef<sup>fi</sup>cient management of fuel cost is a critical issue for motor carriers. We have proposed a decision support system that takes advantage of the dynamic movement of fuel prices to reduce motorcarrier fuel cost at the point of purchase. A unique aspect of our method is that, unlike the commercial fuel optimizers, it allows carriers to save costs without con<sup>fi</sup>scating the freedom of truck drivers to choose trucks stops. Thus, our method is expected to: (i) attain high driver compliance rates, and (ii) reduce fuel costs with little or no added driver replacement costs. Our method should work particularly well if carriers are facing the following problems: (i) drivers are reluctant to give up their freedom to choose truck stops, (ii) driver turnover rate is expected to increase considerably if drivers are forced to give up the freedom, or (iii) the cost of driver replacement (per replacement) is high. Current or potential users of fuel optimizers, who are facing these problems, may bene<sup>fi</sup>t from the use of our method.

Readers should note the following study limitations. First, our method may not be suitable for small carriers. To use our method, a carrier must satisfy the following conditions: (i) equip its trucks with GPS and satellite communication systems, and (ii) have access to OPIS data. While these conditions are generally satis<sup>fi</sup>ed by large and medium carriers, they may not apply to small carriers. Carriers that do not meet these conditions may wish to use commercial fuel optimizers. Second, our method may not be appropriate for carriers that focus on short routes (some carriers avoid long routes to ensure that their drivers stay home at night.) Recall that the majority of our model's cost savings come from the Min–Max method, which is primarily designed to work in medium and long-distance routes that have multiple fuel stops. This condition implies that carriers focusing on short routes may not receive full bene<sup>fi</sup>ts from our method. Third, our method assumes a constant rate of fuel consumption (mpg) throughout the trip (route), while in practice the vehicle mpg can vary from one route segment to the next depending on such factors as the road condition (e.g., highway or non-highway) and the amount of fuel in the tank (i.e., vehicle weight). An interesting extension of this study, therefore, is to improve the proposed method by: (i) linking the decision model with a GIS database that captures the road condition [9], and (ii) creating an algorithm that adjusts the mpg by the vehicle weight [3]. We leave this topic for future research.

## Acknowledgments

This research was funded, in part, by the Iowa State University College of Business Mini-Scholarship Grant. The author thanks Carrier X for providing many useful data. Thanks also go to three truck-load carriers, three over-the-road truck drivers, two fuel-optimizer vendors, two truck-stop chains, and one satellite-communication vendor for kindly participating in the author's interviews. The author appreciates Danny Johnson, Kevin Scheibe, and Bobby Martens for providing many helpful comments to earlier versions of this paper.

## References

[1] S.B. Keller, J. Ozment, Managing driver retention: effects of the dispatcher, Journal of Business Logistics 20 (1999) 97–120.

[2] S. Khuller, A. Malekian, J. Mestre, To <sup>fi</sup>ll or not to <sup>fi</sup>ll: the gas station problem, Proceedings of the 15th Annual European Symposium on Algorithms, 4698, 2008, pp. 534–545.

[3] D. Kodjak, Heavy-duty truck fuel economy, National commission on energy policy available at: http://www1.eere.energy.gov/vehiclesandfuels/pdfs/deer\_2004/session6/ 2004\_deer\_kodjak.pdf.

[4] S.H. Lin, Finding optimal refueling policies in transportation networks, Proceed ings of the 4th International Conference on Algorithmic Aspects in Information and Management, 5034, 2008, pp. 280–291.

[5] S.H. Lin, R. Gertsch, J.R. Russell, A linear-time algorithm for <sup>fi</sup>nding optimal vehicle refueling policies, Operations Research Letters 35 (2007) 290–296

[6] H. Min, T. Lambert, Truck driver shortage revisited, Transportation Journal 42 (2002).5-17

[7] H. Min, A. Emam, Developing the pro<sup>fi</sup>les for truck drivers for successful recruitment and retention, International Journal of Physical Distribution & Logistic Management 33 (2003) 149–163.

[8] K.G. Murty, J. Liu, Y. Wan, R. Linn, A decision support system for operations in a container terminal, Decision Support Systems 39 (2005) 309–332.

[9] J.J. Ray, A web-based spatial decision support system optimizes routes for oversize overweight vehicles in Delaware, Decision Support Systems 43 (2007) 1171–1185.

[10] J. Rodriguez, M. Kosir, B. Lantz, G. Griffen, J. Glatt, The Costs of Truckload Driver Turnover,UpperGreatPlainsTransportationInstitute,NorthDakotaStateUniversity, 2000.

[11] Y. Suzuki, A generic model of motor-carrier fuel optimization, Naval Research Logistics, forthcoming

[13] Truckload Carriers Association, How to recruit and retain drivers (2007), available at: http://www.smallcarrieruniversity.com/ccu\_driver\_recruitment.shtml.

[12] [12] Transport Topics Driver churn sets record, April 4 (2005) 1, 26.

[14] U.S. Department of Energy, Gasoline and Diesel Fuel Update, available at: http:// www.eia.doe.gov.

[15] U.S. Department of Transportation Federal Motor Carrier Safety Administration, Intelligent Transportation Systems and Truck Parking, Washington, DC, 2005.

Yoshinori Suzuki is Associate Professor of Logistics and Supply Chain Management and Jacobson Company Fellow in Transportation and Logistics at the College of Business, Iowa State University. He holds a Bachelor of Science degree in Business and Economics from Sophia University (Tokyo Japan), a Master of Business Administration degree in Marketing from New York University, and a Doctor of Philosophy degree in Business Logistics from The Pennsylvania State University. He has several years of industry experience. His work experiences include sales, logistics management, and transportation management. He has participated in many publicly and privately funded research projects, and has published over 20 research papers in such journals as Transportation Research, Journal of Transportation Engineering, Naval Research Logistics, and Journal of Business Logistics. His research interest centers on airline and motor-carrier management issues.
