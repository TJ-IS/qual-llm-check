---
otero_id: 10794
otero_key: "VTT9AA7N"
title: "DSS of vehicle refueling: A new enhanced approach with fuel weight considerations"
authors: "Yoshinori Suzuki; Frank Montabon; Shih-Hao Lu"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.10.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DSS of vehicle refueling: A new enhanced approach with fuel weight considerations

Yoshinori Suzuki ⁎, Frank Montabon, Shih-Hao Lu

Department of Supply Chain & Information Systems, College of Business, Iowa State University, 2340 Gerdin Business Building, Ames, IA 50011-1350, USA

## a r t i c l e i n f o

Article history: Received 11 February 2014 Received in revised form 11 August 2014 Accepted 18 October 2014 Available online 24 October 2014

Keywords: Decision support systems Trucks Fuel cost Fuel consumption Optimization

## a b s t r a c t

The <sup>fi</sup>xed-route vehicle-refueling problem (FRVRP) is a mathematical problem widely used in the U.S. trucking industry. The FRVRP seeks the best refueling policy (sequence of fuel stations to use, along with the fueling quantity at each station) for a given (<sup>fi</sup>xed) origin–destination route that minimizes a vehicle's refueling cost. While effective, the current FRVRP methods need not produce optimal solutions, as they ignore the negative impacts that carrying excessive amounts of fuel in the tank can have on fuel consumption rates. This paper proposes a new approach to the FRVRP that takes into account the bene<sup>fi</sup>t of retaining some empty space in the fuel tank at all times, which enhances fuel economy. We show by conducting computational testing that our approach attains not only cheaper refueling costs, but also lower fuel burns, than other approaches. Our approach is simple, yet its implementation may save millions of gallons of diesel fuel and billions of dollars of fuel cost for the U.S. trucking industry per year.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Given the dramatic increase of fuel prices observed during the last few years, the ef<sup>fi</sup>cient management of fuel cost has become a critical issue in today's motor-carrier (trucking) industry. The importance of this issue cannot be overstated as fuel prices affect not only the operating cost of carriers but also the logistics cost of shippers. One method of managing the motor-carrier fuel cost, which is increasingly adopted by U.S. truckload (TL) carriers, is the use of software products called fuel optimizers. Fuel optimizers are decision support systems designed to solve the fixed-route vehicle-refueling problem (FRVRP), a mathematical problem that seeks the best refueling policy (sequence of fuel stations to use, along with the fueling quantity at each station) for a given (<sup>fi</sup>xed) origin–destination route that minimizes a vehicle's refueling cost. These products typically work in conjunction with the fuel-price databases which are updated daily, so that carriers can always create refueling policies based on the latest price data.

To date, several FRVRP solution techniques have been developed. These include the heuristics developed by software (fuel optimizer) vendors, as well as the exact methods proposed by academicians. It is worth noting that virtually all of these methods produce solutions that buy as many gallons at cheap fuel stations (truck stops) as possible and buy fewer (or no) gallons at expensive truck stops (i.e., top off at a limited number of cheap truck stops to minimize the per-unit price of buying fuel). Here the rationale is that: (i) when the route is <sup>fi</sup>xed the amount of fuel needed by a vehicle to move along the route (which is equivalent to the required refueling quantity along the route) is also <sup>fi</sup>xed, so that (ii) the refueling cost, which is given by the product of refueling quantity (gallons) and the unit price of purchased fuel (dollars per gallon), can be minimized by minimizing the latter. This rationale, however, may not hold in practice.

Evidences indicate that a truck's fuel economy is affected by its payload (total loaded weight of a vehicle, including fuel weight, less its empty weight), such that the heavier the payload the worse the fuel economy (see, e.g., U.K. Department for Transport [16]). This means that the amount of fuel needed by a vehicle (whose cargo weight is <sup>fi</sup>xed) to move along a given route is not constant. Rather, it is a function of the amount of the fuel carried by the vehicle when it is moving along the route, such that the heavier the fuel the more the fuel needed. Consequently, the amount of fuel burned by a vehicle in a given route can be affected by the refueling pattern (policy) which the vehicle follows while moving along the route.

The above paragraph implies that the assumption used by all the traditional FRVRP methods, that a vehicle's fuel burn in a given route is always <sup>fi</sup>xed, may not be valid. Consequently, it is questionable if, after considering the possible negative impact of fuel weight on fuel consumption rates, the “optimal” FRVRP solutions given by the existing methods are truly optimal. Recall that these solutions tend to “over<sup>fi</sup>ll” a vehicle's fuel tank at cheap truck stops, possibly to the extent that the vehicle's fuel weight after refueling would be too heavy to achieve a good fuel economy. This pattern implies that these solutions may suffer from higher fuel burns and thus higher refueling requirements for the vehicle along the route. We suspect that existing FRVRP methods may merely be minimizing the per-unit cost of buying fuel at the expense of increased refueling requirements, which can result in higher refueling costs.

This paper describes a study being carried out by the authors to enhance the performance of fuel-optimizer products in which a new FRVRP method is proposed that allows carriers to achieve lower refueling costs than other (existing) methods. This new method is based on the idea that if a truck possesses more fuel than necessary in its fuel tank (e.g., beyond that needed to reach the next refueling location), it must burn additional fuel to carry this “extra” or “unnecessary” fuel to the next station, so that such surplus fuel should be either eliminated or minimized to lower fuel consumption. Note that this type of method allows carriers not only to lower refueling costs, but also to perform more environmentally friendly (greener) vehicle operations, as it requires less fuel than other methods (fuel consumption is an important metric of environmental friendliness; see, e.g., Shrivastava [7]). This latter point is increasingly recognized as an important issue in the trucking industry because, with the growing public awareness of global warming, many shippers (e.g., Wal-Mart, Target, Johnson & Johnson, and Coca Cola) are now asking motor carriers to reduce their fuel consumptions considerably (Coyle et al. [3]).

In the paragraphs that follow we <sup>fi</sup>rst propose a new FRVRP form that considers the possible trade-off between (i) maximizing the amount of fuel purchase (top off) at cheap stations (which reduces per-unit cost of buying fuel), and (ii) avoiding excessive fuel purchases at any station so as to retain some empty space in the fuel tank at all times (which enhances fuel economy), and then develop a heuristic for this form. We show by solving the real-world FRVRP instances obtained from ProMiles, a widely-used fuel optimizer, that the solutions given by our method outperform the standard FRVRP solutions in both the refueling cost and fuel consumption. Our method is simple, yet its implementation can possibly save millions of gallons of diesel fuel and billions of dollars of fuel cost for the U.S. trucking industry per year.

## 2. State of the art: current FRVRP approaches

To date, several FRVRP forms and solution techniques have been developed in the literature. Perhaps the earliest work that considered the vehicle refueling problem is Stroup and Wollmer [8], which modeled the aircraft refueling problem for commercial airliners. They considered the problem of how many gallons of fuel to purchase at each landing airport to minimize the cost of refueling, subject to certain constraints such as the maximum refueling quantity at each airport implied by the tank capacity and the remaining fuel in the tank. This study formulated the FRVRP as a network problem and showed that the problem can be easily solved to optimality by using the standard linear-programming techniques.

Recently, the vehicle-refueling concept was applied to the trucking industry by Lin et al. [5]. This study considered the refueling problem for commercial trucks, which seeks the best sequence of fuel stations to use for a given origin–destination route. An interesting aspect of this study is that it considered the FRVRP as a special case of the capacitated lot-sizing problem (CLSP), which is widely used in the production literature, and developed an ef<sup>fi</sup>cient optimal algorithm by modifying the existing CLSP methods. A similar (essentially identical) FRVRP form was considered by Khuller et al. [4]. This study formulated the FRVRP as a dynamic program in which the problem is divided into n sub-problems, where n is the number of fueling stations available along the route, and developed an ef<sup>fi</sup>cient optimal algorithm.

An extended version of the above FRVRP was proposed by Suzuki [9], in which two additional factors are considered, namely: minimum refueling quantity and truck-stop out-of-route (OOR) miles. The former re<sup>fl</sup>ects the lower-bound refueling quantity at any truck stop, which is used to control the refueling frequency (forbids frequent stops with small purchases). The latter re<sup>fl</sup>ects the distance a truck must divert from the main route to reach a fuel station, which is used to discount the value of truck stops that are located far from the main route. Suzuki [9] showed that this extended FRVRP can be formulated as a mixedinteger linear program, so that the optimal solution can be obtained by using standard LP methods. Suzuki [10] considered a vehicle-refueling problem in which a truck driver is allowed to freely choose refueling locations (which makes the problem more complex) and proposed a heuristic method.

The vehicle-refueling problem is also considered by practitioners, especially by software vendors and transportation consulting companies that developed commercial fuel optimizers. It is not clear how the FRVRP is solved by commercial fuel optimizers, as many fueloptimizer vendors are reluctant to provide details of their solution techniques (we tried, but they all refused). We, however, know that all fuel optimizers use heuristics to solve the FRVRP (Suzuki [9]). We suspect that these software products may be using a simple method in which they <sup>fi</sup>rst identify the set of cheapest truck stops along the route, and then choose a few truck stops from this set as refueling points by using a construction-type heuristic.

There are several variants of the FRVRP that jointly address the vehicle-routing and vehicle-refueling problems. Studies that considered these variants, which are called the variable-route vehicle-refueling problems (VRVRPs), include Bousonville et al. [1], Khuller et al. [4], Suzuki [11], Suzuki and Dai [12], and Sweda and Klabjan [14]. From the perspective of researchers studying VRVRPs, the FRVRP is a sub-problem of their focal problems (e.g., as part of the “route <sup>fi</sup>rst, refueling-policy second” solution approaches), which implies that the FRVRP studies can be of great utility to these researchers too.

## 3. Standard FRVRP formulation

In this section we describe the standard FRVRP formulation that is widely used by transportation researchers and practitioners, and then point out its limitations. In the next section we propose a new FRVRP form and discuss how it can alleviate the limitations of the standard form. The form discussed in this section is based on the work of Suzuki [9], which is perhaps the most widely-used form in practice.

## 3.1. The model

Consider a route shown in Fig. 1. Let $\Omega = \{ 1 , 2 , . . . , i , . . . , n \}$ be the set of truck stops found along the (shortest) route from origin o to destination z. Characteristics of each truck stop $i \in \Omega$ are given by: (i) p (fuel price per gallon), (ii) e (OOR miles, or the extent to which a vehicle must divert from the main route to reach truck stop i), and (iii) $d _ { i \cdot }$ 1,i (miles between truck stops i 1 and i, excluding $e _ { i - 1 }$ and e ). The vehicle has a <sup>fi</sup>xed fuel-tank capacity of Q gallons and an average fuel consumption rate of λ (gallons per mile or GPM). The vehicle must make one or more fuel stops to maintain the minimum fuel (reserve fuel) $\mathbf { 0 } \mathbf { f } l \geq 0$ gal in the tank at all times, subject to the minimum purchase quantity of $\rho \ge 0$ gal in every refueling occasion. The vehicle may not choose those truck stops whose OOR miles (e ) exceed $u \geq 0$ miles (we assume that the elements of Ω are pre-screened such that $e _ { i } \leq u \forall i \in \Omega \}$ . Given the initial fuel level at origin (θ) and the required fuel level at destination (ε), we seek the minimal-cost refueling policy $\Phi = \langle \phi _ { 1 } , \phi _ { 2 } , . . . ,$ $\phi _ { i } , . . . , \phi _ { n } \rangle$ 〉, where $\phi _ { i } \ge 0$ is the amount of fuel (gallons) to purchase truck stop i. Following the standard practice, we assume that a vehicle's cargo weight is <sup>fi</sup>xed throughout the route.

Let δ be a 0/1 binary decision variable indicating the refueling location (1 if refueling at truck stop i, 0 otherwise). The standard FRVRP can be expressed as a mixed-integer linear program as follows:

$$
\text { P1 }: \quad \min _ {\delta_ {i}, \phi_ {i}} \sum_ {i \in \Omega} p _ {i} \phi_ {i}\tag{1}
$$

$$
\text { Subject   to: } \quad \delta_ {i} \in \{0, 1 \} \quad \forall i \in \Omega\tag{2}
$$

$$
r _ {i} \geq l \quad \forall i \in \Omega\tag{3}
$$

![](/api/attachments/VTT9AA7N/fulltext/images/4b679fd4bba6f939b45ba36fc6394dc71fb3378163b7ba3071897a766df5fa91.jpg)  
Fig. 1. A sample refueling problem (source: Suzuki [9]).

$$
r _ {z} \geq \varepsilon\tag{4}
$$

$$
\phi_ {i} \geq \delta_ {i} \rho \quad \forall i \in \Omega\tag{5}
$$

$$
\phi_ {i} \leq \delta_ {i} Q \quad \forall i \in \Omega\tag{6}
$$

$$
r _ {i} + \phi_ {i} \leq Q \quad \forall i \in \Omega\tag{7}
$$

$$
r _ {i} = \left\{ \begin{array}{l} \theta - \lambda \Big (d _ {o, 1} + \delta_ {1} e _ {1} \Big), \quad \text { if } i = 1 \\ r _ {i - 1} + \phi_ {i - 1} - \lambda \Big (\delta_ {i - 1} e _ {i - 1} + d _ {i - 1, i} + \delta_ {i} e _ {i} \Big), \quad \text { if } i > 1 \end{array} \right.\tag{8}
$$

$$
r _ {z} = r _ {n} + \phi_ {n} - \lambda \left(\delta_ {n} e _ {n} + d _ {n, z}\right)\tag{9}
$$

where r is the vehicle's fuel level either at truck stop i before buying fuel $( \mathrm { i f } \delta _ { i } = 1 )$ or at the diversion point to $\dot { l } ( \mathrm { i f } \delta _ { i } = 0 ;$ see Fig. 1) and $r _ { z }$ is the vehicle's fuel level when arriving at destination z. The objective is to minimize the refueling cost. The model constraints ensure the following: (i) the minimum purchase quantity is ρ at any truck stop (constraints 2, 5, 6), (ii) the fuel level does not exceed the tank capacity after refueling at any truck stop (constraint 7), (iii) the fuel level does not fall below l at any point in the route (constraints 3, 8), and (iv) the ending fuel level is at least ε (constraints 4, 9). P1 above can be solved to optimality by using the standard mixed-integer linear programming methods (Suzuki [9]).

Note that, when necessary, the length of each road segment in P1 $( d _ { i - 1 , i } )$ can be adjusted by the road-speci<sup>fi</sup>c factors (e.g., gradient and average vehicle speed) to account for the possible variance of fuel consumption rate across segments. If, for example, a segment $d _ { i - 1 , i }$ has a positive gradient (uphill) such that it requires 20% more fuel burn than normal segments with zero gradients (<sup>fl</sup>at terrain), $d _ { i - 1 , i }$ can be multiplied by 1.2. Similar adjustments can be made to incorporate the effect of vehicle speed on fuel burn.

## 3.2. Two limitations of P1

First, P1 uses only one value of λ; i.e., it assumes that λ is <sup>fi</sup>xed regardless of the amount of fuel in the tank (note that λ can be changed freely by users from one instance to another, but its value must be <sup>fi</sup>xed within a given instance). This means that P1 ignores the possible loss of fuel economy that is caused by the possession of excessive amount of fuel. Thus, as discussed earlier, the solutions obtained by solving P1 may tend to over<sup>fi</sup>ll (top off) a vehicle's fuel tank at cheap truck stops (to minimize the per-unit price of refueling), which can worsen the fuel consumption rate. Hence, P1 solutions may require more fuel burns to move a vehicle from o to z than other solutions (that do not top off at cheap truck stops) and thus require more fuel to be purchased along the route, which may result in higher refueling costs.

Second, P1 uses only one value of reserve fuel l (again, l can be changed freely from one instance to another, but its value must be <sup>fi</sup>xed within a given instance). Using this “one-size <sup>fi</sup>ts all” l value, however, is not desirable from the fuel ef<sup>fi</sup>ciency standpoint. Note that the reserve fuel re<sup>fl</sup>ects the minimum amount of fuel that must be kept in the fuel tank at all times to avoid the “out of fuel” incidents on the road. Hence, it is typically interpreted as the amount of fuel needed by a vehicle to reach an alternate truck stop(s) in an unlikely event that the intended truck stop cannot be used for reasons such as temporary closure. This means that, ideally, the value of l should vary from one segment to the next along the route. Speci<sup>fi</sup>cally, l should be small when a vehicle is traveling the region with many truck stops (high truck-stop density area), because the distance between truck stops is small in this region, whereas l should be large when the vehicle is traveling the region with limited truck stops (low truck-stop density area). In P1, however, because it accepts only one value of l, it is inevitable that we set l such that it will be suf<sup>fi</sup>cient to avoid the out-of-fuel incidents in all regions, including the low truck-stop density areas (e.g., 40 gal). This implies that in P1 a vehicle must carry an excessive amount of unnecessary safety fuel when it is traveling high truck-stop density areas, which worsens the fuel consumption rate.

## 4. Proposed formulation

## 4.1. Framework

Our FRVRP form is based on the following logic. First, our model must incorporate the negative effect of fuel weight on GPM. This means that our model must adjust GPM (λ) dynamically throughout the route (updated every mile) based on the fuel weight. Second, our model must <sup>fl</sup>exibly adjust the reserve-fuel (l) at various points along the route such that the minimum fuel a vehicle must carry when arriving at truck stop i, or when passing through the diversion point to i, is determined by the truck-stop density around i. This reserve fuel, which is determined uniquely for each i, is denoted hereafter as $\tau _ { i \cdot }$

## 4.2. The new formulation

The proposed new FRVRP formulation, which is denoted as P2 from now on, can be expressed as:

$$
\text { P2 }: \quad \min _ {\delta_ {i}, \phi_ {i}} \sum_ {i \in \Omega} p _ {i} \phi_ {i}\tag{10}
$$

$$
\text { Subject   to }: \quad \delta_ {i} \in \{0, 1 \} \quad \forall i \in \Omega\tag{11}
$$

$$
r _ {i} \geq \tau_ {i} \quad \forall i \in \Omega\tag{12}
$$

$$
r _ {z} \geq \varepsilon\tag{13}
$$

$$
\phi_ {i} \geq \delta_ {i} \rho \quad \forall i \in \Omega\tag{14}
$$

$$
\phi_ {i} \leq \delta_ {i} Q \quad \forall i \in \Omega\tag{15}
$$

$$
r _ {i} + \phi_ {i} \leq Q \quad \forall i \in \Omega\tag{16}
$$

$$
r _ {i} = \left\{ \begin{array}{l} \theta - f \Big (\theta , d _ {o, 1} + \delta_ {1} e _ {1} \Big), \quad \text { if } i = 1 \\ r _ {i - 1} + \phi_ {i - 1} - f \Big (r _ {i - 1} + \phi_ {i - 1}, \delta_ {i - 1} e _ {i - 1} + d _ {i - 1, i} + \delta_ {i} e _ {i} \Big), \quad \text { if } i > 1 \end{array} \right.\tag{17}
$$

$$
r _ {z} = r _ {n} + \phi_ {n} - f \left(r _ {n} + \phi_ {n}, \delta_ {n} e _ {n} + d _ {n, z}\right)\tag{18}
$$

$$
\tau_ {i} = \left\{ \begin{array}{l l} f \Big (Q, e _ {i} + d _ {i, i + 1} + 2 e _ {i + 1} + d _ {i + 1, i + 2} + e _ {i + 2} \Big) \times S, & \text { if } i \leq n - 2 \\ l, \quad \text { if } i > n - 2 \end{array} \right.\tag{19}
$$

where τ is the dynamic reserve-fuel parameter indicating the minimum fuel to be maintained by a vehicle when arriving at truck stop i (if refueling at i) or when passing through the diversion point to i (otherwise), l is the standard (static) reserve fuel (e.g., 40 gal), S ≥ 1 is the user-speci<sup>fi</sup>ed “safety-margin” multiplier for reserve fuel $( \mathbf { e . g . } , S = 1 . 1 )$ , and $f ( a , b )$ is the formula that computes the amount of fuel needed to travel a road segment whose length is b miles by a vehicle that has a gallons of fuel in the tank at the starting point of the segment. The actual functional form of f (a, b) can be found in Appendix A.

## 4.3. Features of new formulation

P2 has three advantages over P1. First, unlike P1, P2 incorporates the negative impact of fuel weight on GPM. Note that P2 expresses a vehicle's fuel consumption in a given segment as a function of the vehicle's initial fuel level (at the starting point of the segment) and the segment's length. This means that GPM is non-stationary in P2; i.e., a vehicle's GPM varies from one segment to the next throughout the route based on the fuel weight. In theory, therefore, P2 should produce better solutions than P1 by considering the trade-off between: (i) maximizing refueling quantity (top off) at a limited number of cheap truck stops (which lowers the per-unit cost of refueling), and (ii) avoiding excessive fuel purchases at any truck stop so as to retain some empty space in the fuel tank at all times (which enhances fuel burn).

Second, P2 minimizes the “unnecessary” reserve fuel to be held by a vehicle. Note that, unlike P1, P2 assigns a unique value of l for each truck stop i (τ ) by considering the truck-stop density around i (i.e., how far away other truck stops are from i). Speci<sup>fi</sup>cally, P2 de<sup>fi</sup>nes τ as the amount of fuel needed by a vehicle to move from i to the next two truck stops along the route (i + 1 and i + 2) without running out of fuel (this ensures that the vehicle always has enough fuel to reach at least two alternate fuel stations even when the intended truck stop i is closed). This means that P2 should achieve a better (lower) GPM than P1 by reducing a vehicle's reserve-fuel requirement when it is traveling high truck-stop density areas.

Third, P2 allows a vehicle to buy larger amounts of fuel (than P1) in high truck-stop density areas, where the fuel price is expected to be low for competitive reasons. To see this point, recall that P2 uses small τ values $( \tau _ { i } \ll l )$ for all i that are located in high truck-stop density areas. This implies that a truck's fuel level when arriving at these “cheap” truck stops will, in general, be lower under P2 than under P1. As such, when desirable, P2 allows trucks to buy more fuel than P1 at cheap truck stops, while also keeping larger empty space in the fuel tank than P1 after refueling (see Fig. 2 for an example). This makes it possible for P2 to outperform P1 in terms of both the fuel burn and the per-unit cost of refueling.

## 5. Solving the proposed model

## 5.1. Approach

Solving P2 above is challenging for several reasons. First, given the functional form of f (a, b) (Appendix A), P2 is a mixed-integer program with nonlinear step functions, which makes it dif<sup>fi</sup>cult to solve P2 via the conventional linear or nonlinear programming techniques. Second, while in theory P2 can be solved to optimality by using a dynamic programming method, it is dif<sup>fi</sup>cult to do so in practice (partly because the state variable, which re<sup>fl</sup>ects a vehicle's fuel level at various points along the route, is not discrete; see Suzuki [10]). Third, although it is possible to develop a metaheuristic that solves P2 to near optimality, this requires rather long solution time, especially for large instances (solving FRVRPs quickly is crucial for many carriers, as they must solve thousands of FRVRPs each day; see Suzuki [13]).

Given these conditions we solve P2 by using a simple heuristic ap proach. Speci<sup>fi</sup>cally, we <sup>fi</sup>rst create a “relaxed”, or simpli<sup>fi</sup>ed, version of P2 by eradicating both the nonlinearity and discontinuity of the problem and then solve the resulting problem by using a standard linearprogramming method. While seemingly naive, this approach, which attempts to produce quality P2 solutions by solving a simpli<sup>fi</sup>ed version of P2 to optimality rather than solving the exact P2 formulation to near optimality, can be of great utility to practitioners for two reasons. First, it allows users to obtain solutions by using standard simplex solvers. This means that carriers may be able to use our method conveniently without performing technical programming tasks, and that commercial fuel optimizers (many of which may be using a simplex-like method to solve P1) can possibly adopt our method quickly without drastically modifying the software speci<sup>fi</sup>cation. Second, it allows users to generate solutions quickly. Given the availability of many powerful commercial solvers today that can solve large mixed-integer programs quickly, the time required to generate a solution under the proposed approach is very small, usually well under one second.

## 5.2. Relaxed model: concepts

Our relaxed model mixes the features of P1 and P2; i.e., the form that is as tractable as P1 but incorporates the following attributes of P2: (i) the ability to consider the trade-off between reducing unit cost of buying fuel (top off at cheap truck stops) and reducing fuel burns (always keep empty space in the fuel tank), and (ii) the ability to change the reserve fuel quantity from one point to the next along the route.

Let M Q be a non-integer decision variable indicating the “virtual” tank capacity (maximum permissible fuel level at any point along the route). This means that Q − M represents that portion of the fuel tank which will never be used (empty space). From the fuel ef<sup>fi</sup>ciency standpoint it is clear that the larger the $Q - M$ the better the solution. Our idea is to create a formula that converts the fuel ef<sup>fi</sup>ciency gain attained by having $Q - M$ gallons of empty tank space into dollar values and add this formula to the objective function as a penalty (incentive) function to incorporate the bene<sup>fi</sup>t of having empty tank space.

![](/api/attachments/VTT9AA7N/fulltext/images/cc4d19030b685030f2bfa1e8a62ed9ec607a51d2ed8392b57cb08ed90e9ae812.jpg)  
Fig. 2. Hypothetical refueling patterns at high truck-stop density area

Let α be a constant measuring the average, or expected, dollar saving that can be attained by reducing M (increasing empty tank space) by one gallon. In other words, α measures the expected saving in fuel consumption (of moving a vehicle from o to z), expressed in dollar value, which can be attained by increasing the empty tank space by one gallon. Speci<sup>fi</sup>cally, the value of α can be expressed as follows:

$$
\alpha = \pi \kappa \beta_ {1} \left(d _ {o, 1} + \sum_ {i = 1} ^ {n - 1} d _ {i, i + 1} + d _ {n, z}\right) \frac {\sum_ {i = 1} ^ {n} p _ {i}}{n},\tag{20}
$$

where π is the expected reduction in average fuel level (gallons) which a vehicle can achieve by reducing M by one unit,<sup>1</sup> κ is a multiplier that converts the fuel quantity (gallons) into weight (metric tons), and $\beta _ { 1 } \geq 0$ is the parameter indicating the decrease in GPM that can be achieved by reducing the vehicle payload by one metric ton (see Appendix A for further details). Observe that Eq. (20) <sup>fi</sup>rst computes the average improvement in GPM (average fuel saving attained per mile) that is caused by a one-unit reduction of M $( \pi \times \kappa \times \beta _ { 1 } )$ , and then multiplies the resulting <sup>fi</sup>gure by the route length (to obtain the overall fuel saving) as well as by the average fuel price (to convert the saving into dollar value). We do not include OOR miles when calculating the route length in Eq. (20), as this practice provides conservative estimates of α.

Once α is determined by $\operatorname { E q . } \left( 2 0 \right)$ , we can compute the total monetary bene<sup>fi</sup>t that can be realized by using the virtual tank capacity of $M < Q \mathrm { a s } \colon \alpha ( Q - M )$ . We add this formula to the objective function to incentivize solutions that always retain some empty space in the fuel tank (solutions with small M values), and penalize those that top off at cheap truck stops (solutions with large M values). It is to be noted that to determine α we must know the value of π. This issue (how to compute π) is discussed later.

## 5.3. Relaxed model: functional form

The relaxed model we propose, which is denoted hereafter as P3, can be expressed as follows:

$$
\text { P3 }: \quad \min _ {\delta_ {i}, \phi_ {i}, M} \sum_ {i \in \Omega} p _ {i} \phi_ {i} - \alpha (Q - M)\tag{21}
$$

$$
\text { Subject   to }: \quad \delta_ {i} \in \{0, 1 \} \quad \forall i \in \Omega\tag{22}
$$

$$
r _ {i} \geq \tau_ {i} \quad \forall i \in \Omega\tag{23}
$$

$$
r _ {z} \geq \varepsilon\tag{24}
$$

$$
\phi_ {i} \geq \delta_ {i} \rho \quad \forall i \in \Omega\tag{25}
$$

$$
\phi_ {i} \leq \delta_ {i} Q \quad \forall i \in \Omega\tag{26}
$$

$$
r _ {i} + \phi_ {i} \leq M \quad \forall i \in \Omega\tag{27}
$$

$$
M \leq Q\tag{28}
$$

$$
r _ {i} = \left\{ \begin{array}{l} \theta - \lambda \left(d _ {o, 1} + \delta_ {1} e _ {1}\right), \quad \text { if } i = 1 \\ r _ {i - 1} + \phi_ {i - 1} - \lambda \left(\delta_ {i - 1} e _ {i - 1} + d _ {i - 1, i} + \delta_ {i} e _ {i}\right), \quad \text { if } i > 1 \end{array} \right.\tag{29}
$$

$$
r _ {z} = r _ {n} + \phi_ {n} - \lambda \left(\delta_ {n} e _ {n} + d _ {n, z}\right)
$$

30

Table 1 Route characteristics.

<table><tr><td>Route ID</td><td>Route distance (miles)</td><td>Number of truck stops</td><td>Average miles between TS</td><td>Average fuel price (no tax)a</td><td>Average out-of-route miles</td></tr><tr><td>1</td><td>716</td><td>47</td><td>14.93</td><td>2.633</td><td>0.766</td></tr><tr><td>2</td><td>783</td><td>82</td><td>9.43</td><td>2.704</td><td>0.620</td></tr><tr><td>3</td><td>998</td><td>66</td><td>14.89</td><td>2.688</td><td>0.402</td></tr><tr><td>4</td><td>1162</td><td>78</td><td>14.71</td><td>2.629</td><td>0.588</td></tr><tr><td>5</td><td>1194</td><td>98</td><td>12.06</td><td>2.830</td><td>0.344</td></tr><tr><td>6</td><td>1248</td><td>84</td><td>14.68</td><td>2.680</td><td>0.432</td></tr><tr><td>7</td><td>1350</td><td>119</td><td>11.25</td><td>2.791</td><td>0.497</td></tr><tr><td>8</td><td>1417</td><td>112</td><td>12.54</td><td>2.835</td><td>0.623</td></tr><tr><td>9</td><td>1486</td><td>98</td><td>15.01</td><td>2.667</td><td>0.329</td></tr><tr><td>10</td><td>1829</td><td>97</td><td>18.67</td><td>2.675</td><td>0.397</td></tr><tr><td>11</td><td>2137</td><td>106</td><td>19.97</td><td>2.853</td><td>0.363</td></tr><tr><td>12</td><td>2630</td><td>177</td><td>14.78</td><td>2.619</td><td>0.424</td></tr><tr><td>13</td><td>2848</td><td>182</td><td>15.56</td><td>2.835</td><td>0.322</td></tr><tr><td>14</td><td>3284</td><td>179</td><td>18.25</td><td>2.848</td><td>0.504</td></tr><tr><td>15</td><td>3379</td><td>199</td><td>16.90</td><td>2.852</td><td>0.380</td></tr><tr><td>16</td><td>3616</td><td>192</td><td>18.73</td><td>2.836</td><td>0.334</td></tr><tr><td>17</td><td>1023</td><td>45</td><td>22.25</td><td>3.793</td><td>0.180</td></tr><tr><td>18</td><td>1110</td><td>57</td><td>19.14</td><td>4.001</td><td>0.360</td></tr><tr><td>19</td><td>989</td><td>69</td><td>14.13</td><td>3.683</td><td>0.317</td></tr><tr><td>20</td><td>755</td><td>90</td><td>8.29</td><td>3.683</td><td>0.489</td></tr><tr><td>21</td><td>885</td><td>99</td><td>8.85</td><td>3.852</td><td>0.461</td></tr><tr><td>22</td><td>821</td><td>78</td><td>10.39</td><td>3.840</td><td>0.528</td></tr><tr><td>23</td><td>1067</td><td>129</td><td>8.21</td><td>3.805</td><td>0.319</td></tr><tr><td>24</td><td>635</td><td>95</td><td>6.61</td><td>3.799</td><td>0.378</td></tr></table>

<sup>a</sup> Following the standard practice, we exclude state taxes from fuel prices (see Suzuki [9] for details).

$$
\tau_ {i} = \left\{ \begin{array}{l l} \lambda \Big (e _ {i} + d _ {i, i + 1} + 2 e _ {i + 1} + d _ {i + 1, i + 2} + e _ {i + 2} \Big) \times S, & \text { if } i \leq n - 2 \\ l, & \text { if } i > n - 2 \end{array} \right..\tag{31}
$$

Note that P3 computes a vehicle's fuel consumption in each segment of the route by using a <sup>fi</sup>xed value of λ (as in the case of P1), instead of using f (a, b) formula (which is the case in P2). This is because the negative effect of fuel weight on GPM is no longer measured by the exact fuel consumption formula (f (a, b)), but is now approximated by the penalty term in the objective function. Also note that P3 is a mixed-integer linear program that uses only one more decision variable and one more constraint than P1. This implies that P3 can be solved to optimality in a straightforward fashion by using a standard (commercial) simplex solver, and that the CPU time needed to solve P3 should be similar to that needed to solve P1.

## 6. Computational testing

In this section we empirically investigate the advantage of our approach over the existing approach by performing numerical experiments with real-world FRVRP instances. Our goal is to examine the extent to which our approach can lower the refueling costs and fuel consumptions of trucks over the existing approach in realistic settings. Our testing uses 24 FRVRP instances generated by ProMiles. These instances re<sup>fl</sup>ect the real-world refueling problems found among the most popular truck routes in the U.S. Table 1 shows the characteristics of these routes. Table 2 reports the parameters used in our testing. These parameters are chosen based on either: (i) the data available from the past empirical studies on truck routing/refueling, or (ii) inputs obtained from practitioners (we interviewed four TL carriers for this study). The vehicle considered in our experiments is the U.S. class-8 truck. Like many fuel optimizers, we assume that a truck is fully loaded with the total payload of 45,000 lb (excluding fuel). In the discussions that follow we denote the FRVRP solutions obtained from the conventional approach (P1) as standard solutions and those obtained from our approach (P3) as proposed solutions.

## 6.1. Design of experiment

In our experiment we perform the following procedure for each individual test instance. First, we obtain problem details, such as the shortest-route distance between origin and destination, available truck stops along this route, and their characteristics including fuel prices, from ProMiles. Second, we obtain the standard solution for the instance by solving P1 to optimality by using a commercial solver. Third, we compute the proposed solution for the instance by solving P3 to optimality, again using a commercial solver. Fourth, since neither P1 nor P3 considers the negative impact of fuel weight on fuel economy when calculating the truck's fuel consumption, we use formulas (17) and (18) of P2 to compute for both the standard and the proposed solutions the “actual” amount of fuel burned by the truck in the route, as well as the “actual” amount of fuel left in the truck's tank at the end of the route (residual fuel). Fifth, we compare the above two FRVRP solutions (standard and proposed) by using several performance measures.

Table 2 Selected parameters.

<table><tr><td>Parameter</td><td>Symbol</td><td>Value</td><td>Unit</td><td>Remarks</td></tr><tr><td colspan="5">Parameters used in experiments</td></tr><tr><td>Weight regression intercept</td><td> $\beta_0$ </td><td>0.10097</td><td>-</td><td>Source: U.K. DFT [16]</td></tr><tr><td>Weight regression slope</td><td> $\beta_1$ </td><td>0.00297</td><td>-</td><td>Source: U.K. DFT [16]</td></tr><tr><td>Maximum out-of-route</td><td>u</td><td>3.00</td><td>Miles</td><td>Default value of ProMiles</td></tr><tr><td>Minimum refueling quantity</td><td>ρ</td><td>70</td><td>Gallons</td><td>Source: Suzuki [10]</td></tr><tr><td>Tank capacity</td><td>Q</td><td>200/250</td><td>Gallons</td><td>Experimental factor</td></tr><tr><td>Minimum fuel (standard) $^a$ </td><td>l</td><td>40</td><td>Gallons</td><td>Default value of ProMiles</td></tr><tr><td>Available fuel at origin</td><td>θ</td><td>70/100</td><td>Gallons</td><td>Experimental factor</td></tr><tr><td>Required fuel at destination</td><td>ε</td><td>70/100</td><td>Gallons</td><td>Experimental factor</td></tr><tr><td>Fuel weight multiplier $^b$ </td><td>κ</td><td>0.00325</td><td>-</td><td>-</td></tr><tr><td colspan="5">Parameters used in cost estimates</td></tr><tr><td>Maintenance cost per mile</td><td> $C^m$ </td><td>0.048</td><td>Dollars</td><td>Source: Suzuki [9]</td></tr><tr><td>Depreciation cost per mile</td><td> $C^d$ </td><td>0.260</td><td>Dollars</td><td>Source: Suzuki [9]</td></tr><tr><td>Driver wage per mile</td><td> $C^w$ </td><td>0.344</td><td>Dollars</td><td>Source: Suzuki [9]</td></tr><tr><td>Fuel cost per mile</td><td> $C^f$ </td><td>0.430</td><td>Dollars</td><td>Source: Suzuki [9]</td></tr><tr><td>Revenue per mile</td><td>R</td><td>1.900</td><td>Dollars</td><td>Source: Suzuki [9]</td></tr><tr><td>Fixed time per fuel stop</td><td>χ</td><td>10</td><td>Minutes</td><td>Source: Suzuki [9]</td></tr><tr><td>Pumping rate (gal. per min)</td><td>ω</td><td>60</td><td>Gallons</td><td>Source: TL carrier</td></tr><tr><td>% increase in GPM in OOR</td><td>Δ</td><td>40.99</td><td>Percent</td><td>Source: Suzuki [9]</td></tr><tr><td>Average travel speed (highway)</td><td>v</td><td>65</td><td>MPH</td><td>Source: Suzuki [9]</td></tr></table>

<sup>a</sup> 20% of tank capacity (200 gal).  
<sup>b</sup> 1 gal of diesel fuel = 7.15 lb; 1 lb = 0.454 kg; 1 kg = 0.001 metric ton.

To gain insights into the conditions under which our approach works most effectively, we perform four experiments by adopting a two-factor $( 2 \times 2 )$ experimental design with two levels of Q (200, 250) and two levels of (θ, ε) combinations ((70, 70), (100, 100)). This design allows us to test the impact of tank capacity (Q) and the beginning and ending fuel levels (θ, ε) on the effectiveness of our method. The experiments are executed by using CPLEX software (12.5) on a 2.66 GHz quad-core PC. Following Suzuki [9], we set the CPLEX parameters such that the software uses the simplex algorithm, branch-and-bound method, and zero integer tolerance, when solving the mixed-integer programs P1 and P3. In every instance tested in our experiments, the CPU time needed to solve P1 or P3 was well under 1 s.

## 6.2. Performance measures

We use <sup>fi</sup>ve metrics to contrast the standard and proposed solutions. The <sup>fi</sup>rst is the fuel consumption. This is measured by the (aforementioned) “actual fuel consumption”, or the actual amount of fuel burned while traveling the route (obtained by P2 formulas). The second is the fuel consumption rate (GPM). This metric is obtained by dividing the <sup>fi</sup>rst metric above (actual fuel consumption) by the total route distance (including OOR miles). The third is the refueling cost. This metric re-<sup>fl</sup>ects the “net” refueling cost, which is computed by adjusting the actual cost of refueling along the route by the residual fuel (the speci<sup>fi</sup>c formula used to calculate this metric is given later). The fourth is the average fuel level in the route. This metric is obtained by <sup>fi</sup>rst calculating the truck's “actual” fuel level (mile by mile) along the route by using P2 formulas, and then taking the average of all the values. The <sup>fi</sup>fth is the maximum fuel level observed in the route. This metric is equivalent to M of P3, and is obtained by <sup>fi</sup>nding the largest value of r + ϕ (where $r _ { i }$ is computed by P2 formulas) across all the truck stops i ∈ Ω.

We calculate the “net” refueling cost (third metric mentioned above) using the following formula:

$$
\sum_ {i \in \Omega} p _ {i} \phi_ {i} + (\varepsilon - r _ {z} ^ {a}) \frac {\sum_ {i = 1} ^ {n} p _ {i}}{n},\tag{32}
$$

where $r _ { z } ^ { a }$ is the “actual” residual fuel retained in the tank when arriving at the destination (computed by P2 formulas). Formula (32) indicates that we measure the refueling cost by adjusting the purchase cost $\textstyle { \bigl ( } \sum _ { i \in \Omega } p _ { i } \phi _ { i } { \bigr ) }$ by the residual fuel, such that the difference between ε (required residual fuel) and r <sup>a</sup> (actual residual fuel), as expressed in dollar value, is added to the purchase cost. This means that if $r _ { z } ^ { a } > \varepsilon$ the difference between the two values (fuel surplus in dollars) is subtracted from the purchase cost, whereas if $r _ { z } ^ { a } < \varepsilon$ the difference (fuel de<sup>fi</sup>ciency in dollars) is added to the purchase cost. This type of adjustment, which is widely used in the FRVRP literature (e.g., Suzuki [10]), is necessary to compare the refueling costs of the standard and proposed solutions (which can have different residual fuels) on the same footing.

## 6.3. Choosing π

As mentioned earlier, we must know the value of π to solve P3. Since π measures the average reduction in fuel level which we can attain by decreasing M by one gallon, π can be expressed as: $( \sum _ { j \in J } \pi _ { j } / | J | )$ where $\pi _ { j }$ is the decrease in fuel-level that can be attained by a unit reduction of M for a speci<sup>fi</sup>c condition j, and J is the universal set of conditions. Here the term “condition” refers not only to each individual FRVRP instance, but also to each possible scenario within the same instance. This means that, for example, a unit reduction of M from 200 to 199 gal for a given instance re<sup>fl</sup>ects a different condition than the unit reduction of M from 199 to 198 gal for the same instance. Since it is dif<sup>fi</sup>cult to identify the universal set J, it follows that it is dif<sup>fi</sup>cult to compute π precisely. We can, however, estimate π by <sup>fi</sup>rst identifying its possible range by computing the worst-case and the best-case values (lower and upper bounds), and then selecting the most logical (most reasonable) value within this range.

It can be shown that the lower bound of π is 0. This is because in some cases (conditions) a unit reduction of M has no impact on the average fuel level at all. This happens, for example, in a small (shortdistance) instance where the fuel-purchase requirement is so small relative to Q that a certain part of the fuel tank would never be utilized under any solution.<sup>2</sup> It can also be shown that the upper bound of π is 1. Note that the maximum fuel-level reduction which a vehicle can attain via a unit reduction of M at any point along the route is one gallon. Hence it follows that the maximum reduction in average fuel level (in the entire route) a vehicle can achieve by reducing the virtual tank capacity (M) by one unit (the amount by which the average fuel level of a vehicle decreases in an idealistic condition where its fuel level at every point along the route diminishes by the maximum amount of one gallon) is also one gallon.

Given these bounds, we can determine the value of π pragmatically. Speci<sup>fi</sup>cally, we determine π by conducting a preliminary computational testing that examines how the performance of P3 solutions, as measured by the “net” refueling cost mentioned above, is affected by the value of π within the possible range [0, 1]. This test allows us to determine the best value of π to use in P3 based on solid empirical evidence. In this testing we adjust π from 0 to 1 in an increment of 0.05. Results of this computational testing (not reported here) indicate that π values between 0.4 and 0.5, inclusive, generally provide promising results. Based on this <sup>fi</sup>nding, we set $\pi = 0 . 4 5$ in our “full-scale” experiments discussed below.

## 6.4. Results of experiments

Results are shown in Table 3. For space limitations we report only the summary statistics of the <sup>fi</sup>ve performance measures (averages of all 24 instances). Detailed results of our experiments (instance by instance result) can be found in Appendix C (online supplement). The most important <sup>fi</sup>ndings follow.

First, the proposed solution outperforms the standard solution in terms of refueling cost. Results show that in all the experiments the proposed solution attains lower refueling cost than the standard solution. The average cost saving attained by the proposed solution over the standard solution ranges from \$6.12 (1.23%) to \$11.37 (1.74%) with an overall average of \$8.68 (1.40%). This suggests that, as expected, our approach produces “cheaper” solutions than the standard approach, which requires less fuel costs to move a vehicle from origin to destination. This also suggests that if the negative impact of fuel weight on GPM is considered, the “seemingly” optimal standard (P1) solutions may no longer be optimal.

Second, the proposed solution outperforms the standard solution in terms of fuel consumption. Results show that, as expected, the amount of fuel needed to move a truck from origin to destination is lower for the proposed solution than for the standard solution in all the experiments. The average fuel saving attained by the proposed solution over the standard solution ranges between 0.15% and 0.25%, with an overall average of 0.187% (0.52 gal). Values of other performance metrics are consistent (in agreement) with this <sup>fi</sup>nding. Observe that the proposed solution achieves better (lower) GPM, average fuel level, and maximum fuel level than the standard solution in all of the experiments. This condition implies that the proposed solution achieves lower fuel burns than the standard solution by retaining larger empty tank space (maintaining lighter fuel weight) relative to the standard solution throughout the route.

Table 3  
Computational results (summary statistics).

<table><tr><td></td><td>Refueling cost (adj.)</td><td>Fuel consumed</td><td>Fuel econ. (GPM)</td><td>Average fuel level</td><td>Maximum fuel level</td></tr><tr><td colspan="6">Experiment 1a</td></tr><tr><td>Standard solutions</td><td>732.17</td><td>253.80</td><td>0.1627</td><td>113.96</td><td>181.24</td></tr><tr><td>Proposed solutions</td><td>722.25</td><td>253.31</td><td>0.1625</td><td>87.11</td><td>160.26</td></tr><tr><td>Improvements (%)</td><td>1.48</td><td>0.15</td><td>0.16</td><td>23.30</td><td>11.66</td></tr><tr><td colspan="6">Experiment 2b</td></tr><tr><td>Standard solutions</td><td>727.52</td><td>253.72</td><td>0.1627</td><td>113.84</td><td>180.21</td></tr><tr><td>Proposed solutions</td><td>721.40</td><td>253.23</td><td>0.1625</td><td>91.82</td><td>161.75</td></tr><tr><td>Improvements (%)</td><td>1.12</td><td>0.18</td><td>0.13</td><td>19.67</td><td>10.37</td></tr><tr><td colspan="6">Experiment 3c</td></tr><tr><td>Standard solutions</td><td>732.62</td><td>253.86</td><td>0.1628</td><td>123.70</td><td>198.12</td></tr><tr><td>Proposed solutions</td><td>721.25</td><td>253.41</td><td>0.1625</td><td>91.21</td><td>172.19</td></tr><tr><td>Improvements (%)</td><td>1.74</td><td>0.16</td><td>0.19</td><td>26.27</td><td>13.38</td></tr><tr><td colspan="6">Experiment 4d</td></tr><tr><td>Standard solutions</td><td>727.81</td><td>253.95</td><td>0.1629</td><td>131.57</td><td>208.77</td></tr><tr><td>Proposed solutions</td><td>720.49</td><td>253.28</td><td>0.1626</td><td>96.59</td><td>174.01</td></tr><tr><td>Improvements (%)</td><td>1.25</td><td>0.25</td><td>0.21</td><td>26.55</td><td>16.65</td></tr></table>

<sup>a</sup> Q = 200, θ = 70, ε = 70.  
b $Q = 2 0 0 , \theta = 1 0 0 , \varepsilon = 1 0 0 .$  
<sup>c</sup> Q = 250, θ = 70, ε = 70.  
d $Q = 2 5 0 , \theta = 1 0 0 , \varepsilon = 1 0 0 .$

Third, the degree to which the proposed approach outperforms the standard approach is larger for the refueling-cost metric (1.23% to 1.74%) than for the fuel-consumption metric (0.15% to 0.25%). This pattern suggests that most of the cost savings attained by our approach over the standard approach (1.23% to 1.74%) come from the reductions of per-unit cost (price) of purchased fuel (0.94% to 1.58%), rather than from the reductions of fuel burn (0.15% to 0.25%). This <sup>fi</sup>nding was somewhat surprising to us, as we had expected the opposite pattern (most savings come from the reductions of fuel consumption). This might suggest that, after considering the trade-off between (i) maximizing fuel purchases at cheap truck stops and (ii) retaining empty space in the fuel tank at all times, our approach often chooses to pursue the former strategy (more aggressively so than the standard approach) to lower the total cost of refueling.

Fourth, the performance of the proposed approach seems to be affected by the value of Q (tank size), such that the effectiveness of our approach improves as Q increases. Table 3 shows that both the cost and fuel savings attained by our approach over the standard approach are larger when Q = 250 (1.74% for $\theta = \varepsilon = 7 0$ and 1.25% for $\theta = \varepsilon = 1 0 0 _ { \cdot } ^ { \cdot }$ than when Q = 200 (1.48% for $\theta = \varepsilon = 7 0$ and 1.12% for $\theta = \varepsilon = 1 0 0 )$ . This pattern suggests that the bene<sup>fi</sup>t of our approach may be an increasing function of Q; i.e., the proposed approach may give higher cost and fuel savings to trucks with larger fuel tanks.

Fifth, mixed results were found for the effect of θ and ε parameters (initial and ending fuel levels) on the performance of our approach. Table 3 shows that, as θ and ε parameters increase from 70 to 100 gal, the fuel saving attained by our approach over the standard approach improves (from 0.15% to 0.18% when Q = 200, and from 0.16% to 0.25% when $Q = 2 5 0 )$ , while the cost saving attained by our approach over the standard approach worsens (from 1.48% to 1.12% when $Q = 2 0 0$ and from 1.74% to 1.25% when $Q = 2 5 0 )$ . This implies that, as θ and ε are adjusted, the effectiveness of our approach can increase or decrease depending on the type of metric we choose to measure the performance. Given such mixed results, we could not draw any de<sup>fi</sup>nitive conclusion regarding the effect of θ and ε parameters.

## 7. Model validation

In order for a model to be valid, it must (i) provide truly meaningful bene<sup>fi</sup>ts to end users, and (ii) work effectively under most practical settings. This section investigates these two issues by performing two additional experiments. First, we examine how the use of our approach would affect other costs (than refueling) of motor carriers. Our goal here is to study the negative impacts, if any, of using our approach on carriers costs other than fuel, so that we can assess the overall, or net, impact of our approach on carrier performance. Second, we test the robustness of our numerical results to the changes in $\beta _ { 1 }$ value. Our goal here is to investigate if, and to what extent, the amount of fuel saving given by our approach diminishes when the impact of fuel weight on fuel consumption rate (β ) decreases by a certain degree.

## 7.1. Impact on other cost

Suzuki [9] argues that the FRVRP solutions affect not only the refueling cost of carriers, but also many other costs of vehicle operations (because many operating costs are functions of OOR miles and refueling frequencies, both of which are determined by the refueling policy). These other (non-refueling) costs include the vehicle maintenance and depreciation costs, the loss of fuel ef<sup>fi</sup>ciency due to reduced vehicle speed before and after making refueling stops, and the opportunity costs (loss of time) associated with making fuel stops and traveling OOR miles. We calculate all of these costs for every solution generated in our numerical testing performed in $\ S 6$ (standard and proposed), and examine the extent to which our approach outperforms, or underperforms, the standard approach in terms of these costs. Following Suzuki [9], we exclude the driver cost (wage) from our cost analyses because TL drivers are paid by the “billed miles” (shortest-route miles from o to z), rather than by the actual odometer miles, so that the driver cost is <sup>fi</sup>xed within each route, regardless of the OOR miles or the frequency of fuel stops.

We cluster non-refueling costs into three types, namely: (i) direct cost associated with OOR miles (denoted $\kappa ^ { 1 } )$ , (ii) opportunity cost associated with OOR miles $\textstyle ( \kappa ^ { 2 } )$ , and (iii) opportunity cost associated with refueling stops $( \kappa ^ { 3 } ) .$ . (We do not consider the costs incurred in the main route, as they are identical between the standard and proposed approaches.) $\kappa ^ { 1 }$ includes the per-mile costs of vehicle maintenance and depreciation incurred in OOR segments, as well as the cost of extra fuel burns experienced in OOR segments (loss of fuel ef<sup>fi</sup>ciency before and after making fuel stops that is caused by the reduced vehicle speed). $\kappa ^ { 2 }$ measures the cost of driver and vehicle times that are spent for traveling OOR miles (i.e., the opportunity cost of traveling “extra” miles beyond the minimum required miles, which is given by the shortest distance from o to $z ) . \kappa ^ { 3 }$ measures the cost of driver and vehicle times that are spent for making “extra” fuel stops beyond the minimum required fuel stops, as well as those spend for pumping “extra” fuel beyond the minimum required amount. For details on how $\kappa ^ { 1 } , \kappa ^ { 2 } ,$ , and $\kappa ^ { 3 }$ are actually computed, see Appendix B. The cost parameters used for computing $\kappa ^ { 1 } , \kappa ^ { 2 } ,$ , and $\kappa ^ { 3 }$ are reported in Table 2 (lower part).

Non-refueling cost comparisons (averages).

<table><tr><td rowspan="2"></td><td rowspan="2">OOR miles</td><td rowspan="2">Fuel stops</td><td colspan="4">Computed costs ($)</td></tr><tr><td> $\kappa^1$ </td><td> $\kappa^2$ </td><td> $\kappa^3$ </td><td>Total</td></tr><tr><td colspan="7">Experiment 1a</td></tr><tr><td>Standard solutions</td><td>2.863</td><td>2.708</td><td>1.434</td><td>2.226</td><td>4.940</td><td>8.600</td></tr><tr><td>Proposed solutions</td><td>2.377</td><td>2.625</td><td>1.202</td><td>1.822</td><td>4.215</td><td>7.239</td></tr><tr><td>Improvement (diff.)</td><td>0.486</td><td>0.083</td><td>0.233</td><td>0.404</td><td>0.724</td><td>1.361</td></tr><tr><td colspan="7">Experiment 2b</td></tr><tr><td>Standard solutions</td><td>2.452</td><td>2.708</td><td>1.239</td><td>1.880</td><td>4.964</td><td>8.084</td></tr><tr><td>Proposed solutions</td><td>1.511</td><td>2.542</td><td>0.762</td><td>1.162</td><td>3.507</td><td>5.431</td></tr><tr><td>Improvement (diff.)</td><td>0.942</td><td>0.167</td><td>0.478</td><td>0.717</td><td>1.457</td><td>2.652</td></tr><tr><td colspan="7">Experiment 3c</td></tr><tr><td>Standard solutions</td><td>2.226</td><td>2.583</td><td>1.118</td><td>1.723</td><td>7.264</td><td>10.105</td></tr><tr><td>Proposed solutions</td><td>2.346</td><td>2.375</td><td>1.186</td><td>1.798</td><td>5.425</td><td>8.409</td></tr><tr><td>Improvement (diff.)</td><td>-0.121</td><td>0.208</td><td>-0.068</td><td>-0.075</td><td>1.839</td><td>1.696</td></tr><tr><td colspan="7">Experiment 4d</td></tr><tr><td>Standard solutions</td><td>2.287</td><td>2.583</td><td>1.148</td><td>1.774</td><td>7.229</td><td>10.151</td></tr><tr><td>Proposed solutions</td><td>1.305</td><td>2.417</td><td>0.660</td><td>0.997</td><td>5.684</td><td>7.342</td></tr><tr><td>Improvement (diff.)</td><td>0.983</td><td>0.167</td><td>0.487</td><td>0.776</td><td>1.545</td><td>2.809</td></tr></table>

<sup>a</sup> Q = 200, θ = 70, ε = 70.  
Q = 200, θ = 100, ε = 100.  
<sup>c</sup> Q = 250, θ = 70, ε = 70.  
Q = 250, θ = 100, ε = 100.

Computed costs are shown in Table 4. Results indicate that, in all the experiments, the proposed solution attains lower non-refueling costs than the standard solution. Note that the proposed solution achieves lower $\kappa ^ { 3 }$ values than the standard solution in all the experiments, and achieves lower $\kappa ^ { 1 }$ and $\kappa ^ { 2 }$ values in three out of four experiments (1, 2, and 4). This is because our approach achieves both lower refueling frequency and lower OOR miles than the standard approach in nearly all the experiments. This <sup>fi</sup>nding is not surprising because, as discussed earlier, our approach reduces both Q (maximum fuel level) and l (minimum fuel level) of a vehicle (it reduces l by a larger amount than Q), so that it should allow us not only to lower the average fuel level throughout the trip (which improves fuel economy), but also to buy more fuel at cheap truck stops, when necessary, than the standard approach (which lowers the per-unit cost of buying fuel). Our approach, therefore, seems to provide not only lower refueling costs, but also lower non-refueling costs, to carriers. This means that, after considering the savings realized in these non-refueling cost items, the bene<sup>fi</sup>ts of our approach may become larger than those reported in Table 3.

Sensitivity analyses (adjusted refueling cost).

<table><tr><td rowspan="2"></td><td colspan="4"> $\beta_1$  value adjustments</td></tr><tr><td>Base case</td><td>10% less</td><td>20% less</td><td>30% less</td></tr><tr><td colspan="5">Experiment 1a</td></tr><tr><td>Standard solutions</td><td>732.17</td><td>703.51</td><td>674.85</td><td>646.18</td></tr><tr><td>Proposed solutions</td><td>722.25</td><td>693.69</td><td>665.19</td><td>636.64</td></tr><tr><td>Improvements ($)</td><td>9.92</td><td>9.82</td><td>9.66</td><td>9.54</td></tr><tr><td>Improvements (%)</td><td>1.48%</td><td>1.52%</td><td>1.57%</td><td>1.62%</td></tr><tr><td colspan="5">Experiment 2b</td></tr><tr><td>Standard solutions</td><td>727.52</td><td>698.87</td><td>670.24</td><td>641.59</td></tr><tr><td>Proposed solutions</td><td>721.40</td><td>692.86</td><td>664.33</td><td>635.79</td></tr><tr><td>Improvements ($)</td><td>6.12</td><td>6.01</td><td>5.91</td><td>5.80</td></tr><tr><td>Improvements (%)</td><td>1.12%</td><td>1.15%</td><td>1.18%</td><td>1.22%</td></tr><tr><td colspan="5">Experiment 3c</td></tr><tr><td>Standard solutions</td><td>732.62</td><td>703.91</td><td>675.22</td><td>646.52</td></tr><tr><td>Proposed solutions</td><td>721.25</td><td>692.69</td><td>664.06</td><td>635.50</td></tr><tr><td>Improvements ($)</td><td>11.37</td><td>11.22</td><td>11.15</td><td>11.02</td></tr><tr><td>Improvements (%)</td><td>1.74%</td><td>1.79%</td><td>1.85%</td><td>1.91%</td></tr><tr><td colspan="5">Experiment 4d</td></tr><tr><td>Standard solutions</td><td>727.81</td><td>699.08</td><td>670.36</td><td>641.64</td></tr><tr><td>Proposed solutions</td><td>720.49</td><td>691.89</td><td>663.32</td><td>634.70</td></tr><tr><td>Improvements ($)</td><td>7.32</td><td>7.19</td><td>7.04</td><td>6.94</td></tr><tr><td>Improvements (%)</td><td>1.25%</td><td>1.27%</td><td>1.31%</td><td>1.35%</td></tr></table>

<sup>a</sup> Q = 200, θ = 70, ε = 70.  
<sup>b</sup> Q = 200, θ = 100, ε = 100.  
<sup>d</sup> Q = 250, θ = 100, ε = 100.  
<sup>c</sup> Q = 250, θ = 70, ε = 70.

## 7.2. Sensitivity to changes in $\beta _ { I }$

In our experiments (§6) we <sup>fi</sup>xed the value of $\beta _ { 1 }$ to that which was derived from U.K. Department for Transport [16]. Although we believe that [16] is the most reliable data source for estimating $\beta _ { 1 }$ (as this is the only study we know which estimated the pure effect of vehicle payload on fuel consumption rate for heavy-duty trucks after controlling for vehicle make, vehicle gross weight, axel load, road conditions, etc.), there exist other studies that provide different estimates o ${ \mathrm { : } } \beta _ { 1 }$ . For this reason we conduct a series of sensitivity analyses here, in which several different $\beta _ { 1 }$ values are tested, to examine the robustness of our computational results reported in Table 3. Our analyses repeat the experiments conducted in §6 with three different $\beta _ { 1 }$ values; namely, 90%, 80%, and 70% of the original $\beta _ { 1 }$ value (i.e., 10%, 20%, and 30% less than that of the original $\beta _ { 1 }$ value). We use only the reduced (lower) values of $\rho _ { 1 }$ in our sensitivity analyses because higher $\beta _ { 1 }$ values will only strengthen the performance of our approach.

Results are shown in Table 5. The table shows that, as the value of $\beta _ { 1 }$ diminishes, the dollar saving attained by our approach over the standard approach decreases slightly, while the percentage saving attained by the former over the latter increases slightly. It seems that, while the reduction of $\beta _ { 1 }$ value decreases both the cost saving attained by our method and the total refueling costs of the two methods (proposed and standard) simultaneously, it decreases the cost saving of our method to a lesser extent than it decreases the total refueling costs of the two methods. This condition (that the dollar saving of our method diminishes only slightly while the percentage saving of our method increases slightly with the reduction o ${ \mathrm { \dot { \rho } } } _ { 1 }$ value) suggests that the performance of our approach may be affected trivially by the changes in $\beta _ { 1 }$ values; i.e., our approach seems to attain noticeable cost saving over the standard approach regardless of the $\beta _ { 1 }$ value. The most plausible explanation to this phenomenon is that: (i) when $\beta _ { 1 }$ is large our approach aggressively lowers a vehicle's average fuel level to enhance the fuel economy, but (ii) when $\beta _ { 1 }$ becomes smaller our approach switches strategy such that it buys large amounts of fuel at cheap truck stops (more aggressively so than the standard approach) to lower the per-unit cost of buying fuel.

## 8. Practical implications

Readers should keep the following points in mind when assessing the merit of using the proposed approach in the <sup>fi</sup>eld. First, since our approach tends to produce solutions that require less OOR miles and fuel stops than the standard approach (as shown in Table 4), the use of our approach may be desirable from the drivers' perspective. It is known that drivers: (i) do not want OOR miles (as these miles are “unpaid” miles), and (ii) do not want frequent fuel stops (as they want to reach destinations quickly to reduce the risk of missing the next load) (Suzuki [9]). This means that our approach, which is less likely to upset drivers than other methods, may give implicit cost savings to carriers in terms of higher driver compliance rates to refueling policies and lower driver turnover rates (see Suzuki [10] for similar claims).

Second, since our model (P3) does not change the basic nature of the standard problem P1 (P3 merely adds a penalty function to P1 and adjusts the reserve fuel and tank capacity), our approach can be used in conjunction with many FRVRP techniques and concepts developed in the past. Our approach, for example, can be combined with the preprocessing technique proposed by Suzuki [13] to cut the CPU time of solving large instances. Our approach can also be used jointly with the “total cost minimization” concept developed by Suzuki [9] by slightly modifying the functional forms of the objective function and selected constraints. This allows us to consider many vehicle-operating costs that are not included in P3.

Third, the proposed FRVRP approach may compare favorably with other fuel-saving methods widely used in the trucking industry, which require physical changes to trucks. These methods, which include trailer and cab roof fairings, trailer side skirts, and aerodynamic side mirrors, typically give 1% to 6% savings in fuel cost, which are comparable to, or slightly better than, those given by our approach. These methods, however, involve initial investments, meaning that carriers cannot realize positive returns during the payback periods, which are estimated to be between one and eight years (Council of Energy Ministers [2]). This condition implies that for many for-hire TL carriers, whose acceptable payback period is less than two years (Roeth et al. [6]), the use of these methods may not be desirable. Our approach, in contrast, does not require any capital investment by carriers, effectively making the payback period zero. This means that once our method is adopted by fuel-optimizer products carriers can start saving fuel costs immediately (possibly with a small incremental fee for improved software performance).

Fourth, our approach can give considerable bene<sup>fi</sup>ts to the trucking industry as a whole. Our experiments indicate that the proposed approach may attain up to 1.74% savings in fuel cost and up to 0.25% savings in fuel consumption over the conventional approach. While seemingly trivial, these <sup>fi</sup>gures convert to large cost and fuel savings for the trucking industry as a whole. Assuming, for example, the total fuel burns of 36.4 billion gallons per year for the U.S. trucking industry (Transport Topics [15]) and the average fuel price of \$3.00 per gallon (a conservative estimate), our results suggest that the proposed approach can possibly save up to 1.9 billion dollars of fuel cost and up to 91 million gallons of diesel fuel for the industry per year. If the fuel price continues to increase into the future (a likely scenario), the bene<sup>fi</sup>t of using our approach becomes even larger. It can be shown that, if the fuel price goes beyond \$6.00 per gallon (which re<sup>fl</sup>ects the current pricing conditions of many non-U.S. countries), the cost-saving potential of our approach reaches nearly \$4 billion per year for the U.S. trucking industry.

## 9. Conclusions and future research

This paper has proposed a new FRVRP approach that takes into account the bene<sup>fi</sup>t of retaining some empty space in the fuel tank at all times, which enhances fuel economy. Our approach seems to produce FRVRP solutions that are more environmentally friendly and more cost ef<sup>fi</sup>cient than the traditional FRVRP methods. If implemented in the <sup>fi</sup>eld, the approach may help TL carriers save millions of gallons of diesel fuel and billions of dollars of fuel cost. Our approach is simple and practical, as it merely requires one to solve a mixed-integer linear program by using a standard simplex solver, whose problem complexity (number of variables and constraints) is very similar to that of conventional FRVRP. This means that our approach may be adopted immediately by many commercial fuel-optimizer products.

This study has its limitations, which may need to be addressed by future research. First, our approach does not directly solve the proposed FRVRP form P2 (instead, it solves a simpli<sup>fi</sup>ed version of P2). Although we believe that this is a reasonable approach, given that the quick solution time is crucial in many practical settings, there may be a way to directly solve P2 ef<sup>fi</sup>ciently by developing a special algorithm. Future studies may wish to explore this issue. Second, like many other FRVRP studies, we assumed that the time spent at each refueling stop is <sup>fi</sup>xed, which may not be practical. An interesting extension of our study, therefore, is to allow the stopping time to vary from one station to another by considering such truck-stop attributes as the location, capacity, and engineering design (conditional on the availability of such data). Third, our approach reduces the effective range of trucks by always keeping some empty space in the fuel tank. While our approach does ensure that each vehicle has suf<sup>fi</sup>cient safety fuel at all times and locations, some drivers may feel uncomfortable reducing the vehicle range (as it may decrease the “peace of mind”), which might negatively affect their compliance rates to refueling policies.

## Appendix A. Computing fuel consumption

We estimate the impact of fuel weight on GPM by referring to U.K. Department for Transport [16], which empirically studied the effect of truck payload on GPM. Based on this study, we express the relationship between GPM and vehicle payload as: $\mathrm { G P M } = \beta _ { 0 } + \beta _ { 1 } L$ , where L is the payload (measured in metric tons), $\beta _ { 0 } \ge 0$ is the GPM of a vehicle when it is empty, and $\beta _ { 1 } \geq 0$ is the increase (loss) in GPM that is caused by an additional ton of payload. In this study we assume that the value of L is non-stationary, because L includes not only the cargo weight, but also the fuel weight (which diminishes with trip miles).

Let w<sub>0</sub> be the cargo weight (non-fuel payload) and κ be the constant (multiplier) that converts fuel quantity (gallons) into weight (tons). We can then express a vehicle's payload as: ${ \cal L } = w _ { 0 } + \kappa A ,$ , where A is the amount of fuel in the vehicle's tank. If we let a be the amount of fuel a vehicle has in its tank at the starting point of a road segment, then the value of A when the vehicle is traveling the jth mile of the road segment (between miles j and $j + 1 )$ can be expressed as: $a - ( \lambda _ { 0 } + \lambda _ { 1 } +$ $\lambda _ { 2 } + \ldots + \lambda _ { j - 1 } ) ,$ , where $\lambda _ { j }$ is the GPM of the vehicle when it is traveling the jth mile. We can then express GPM of the vehicle when it is traveling the jth mile of the road segment as follows: $\lambda _ { j } = \beta _ { 0 } + \beta _ { 1 } [ w _ { 0 } + \kappa ( a -$ $( \lambda _ { 0 } + \lambda _ { 1 } + \lambda _ { 2 } + . . . + \lambda _ { j - 1 } ) ) ] .$

We can generalize the above arguments by expressing the fuel consumption function f (a, b) as:

$$
f (a, b) = \sum_ {j = 0} ^ {b *} \lambda_ {j},\tag{A.1}
$$

$$
\lambda_ {j} = \left\{ \begin{array}{l l} \beta_ {0} + \beta_ {1} (w _ {0} + \kappa a) & \text { if } j = 0 \\ \beta_ {0} + \beta_ {1} \Big (w _ {0} + \kappa \Big (a - \sum_ {q = 0} ^ {j - 1} \lambda_ {q} \Big) \Big) & \text { if } 0 <   j <   b ^ {*} \\ \Big (\beta_ {0} + \beta_ {1} \Big (w _ {0} + \kappa \Big (a - \sum_ {q = 0} ^ {b ^ {*} - 1} \lambda_ {q} \Big) \Big) \Big) (b - b ^ {*}) & \text { if } j = b ^ {*} \end{array} \right.\tag{A.2}
$$

where $b ^ { * } = \left\lfloor b \right\rfloor \mathrm { a n d } j \in \left\{ 0 , 1 , 2 , 3 , . . . , b ^ { * } \right\}$ . Note that if b is an integer, then $b ^ { * } = b ,$ , so that the third line of Eq. (A.2) disappears. Also note that we adjust GPM by using a step-function, i.e., by dividing the road segment into $b ^ { * } + 1$ (or $b ^ { * }$ if b is integer) intervals and assuming that GPM stays constant in each interval.

## Appendix B. Computing non-refueling costs

We calculate the non-refueling costs $\kappa ^ { 1 } , \kappa ^ { 2 } ,$ , and $\kappa ^ { 3 }$ by using the formulas proposed by Suzuki [9], which is based on the concept of “opportunity costs”. For interpretations of the formulas, see Suzuki [9].

κ<sup>1</sup> is computed by adding the costs directly incurred by a carrier for each “extra mile” which the vehicle actually traversed (miles traveled beyond the minimum distance between o and z; i.e., OOR miles).

$$
\kappa^ {1} = \sum_ {i \in \Omega} 2 \delta_ {i} e _ {i} \left[ C ^ {m} + C ^ {d} + \Delta \overline {{\lambda}} \left(\frac {\sum_ {i = 1} ^ {n} p _ {i}}{n}\right) \right],\tag{B.1}
$$

where $C ^ { m }$ is the vehicle maintenance cost (per mile), $C ^ { d }$ is the vehicle depreciation cost (per mile), Δ is the percentage increase in GPM which a vehicle experiences when it makes fuel stops (i.e., loss of fuel ef<sup>fi</sup>ciency before and after making fuel stops due to reduced vehicle speed), and λ is the overall average GPM in the entire route (λ is computed uniquely for each instance and method based on the result of our numerical experiment performed in $\ S 6 ;$ online Appendix C reports the instance-by-instance λ value).

To compute $\kappa ^ { 2 } ,$ , we must <sup>fi</sup>rst calculate the opportunity cost associated with each “extra mile” (denoted $O _ { p m } )$ . We calculate $O _ { p m }$ by <sup>fi</sup>rst estimating the amount of vehicle time that is saved by reducing the “extra mile” by one unit (one mile), and then computing the expected pro<sup>fi</sup>t that can be generated by using the saved time in the best alternative way (i.e., hauling another load on highways). Speci<sup>fi</sup>cally,

$$
O _ {p m} = R - \left(C ^ {m} + C ^ {d} + C ^ {w} + C ^ {f}\right),\tag{B.2}
$$

where $R$ is the average revenue per loaded highway mile and $C ^ { w }$ and $\mathcal { C }$ are the driver wage and fuel cost (per mile) respectively $( C ^ { m }$ and $C ^ { d }$ are de<sup>fi</sup>ned the same as before). Given $O _ { p m } , \kappa ^ { 2 }$ is computed as follows:

$$
\kappa^ {2} = \sum_ {i \in \Omega} 2 \delta_ {i} e _ {i} O _ {p m}.\tag{B.3}
$$

$\kappa ^ { 3 }$ is obtained by <sup>fi</sup>rst calculating the expected vehicle time that is saved by eliminating one “extra” fuel stop (stops made beyond the minimum required stops), as well as the time which is saved by eliminating one “extra” gallon of refueling (gallons purchased beyond the minimum required refueling), and then evaluating the pro<sup>fi</sup>t that can be generated by using the saved time in the best alternative way.

$$
\kappa^ {3} = \left[ \left(\sum_ {i \in \Omega} \delta_ {i} - R ^ {s}\right) \chi + \left(\sum_ {i \in \Omega} \phi_ {i} - R ^ {r}\right) \frac {1}{\varpi} \right] \frac {v}{6 0} O _ {p m},\tag{B.4}
$$

where $R ^ { s }$ and $R ^ { r }$ are the minimum required fuel stops and refueling quantity respectively (R<sup>s</sup> and $R ^ { r }$ are computed uniquely for each instance by solving the modi<sup>fi</sup>ed versions of P1 in which the total fuel stops and the total refueling quantity, respectively, are minimized), $\chi$ is the <sup>fi</sup>xed (non-pumping) time per fuel stop, ϖ is the pumping rate (gallons per minute), and υ is the average vehicle speed on highways (mph).

## Appendix C. Supplementary data

Supplementary data to this article can be found online at http://dx. doi.org/10.1016/j.dss.2014.10.005.

## References

[1] T. Bousonville, A. Hartmann, T. Melo, H. Kopfer, Vehicle routing and refueling: the impact of price variations on tour length, in: E. Sucky, B. Asdecker, A. Dobhan, A. Haas, J. Wiese (Eds.), Logistikmanagement Herausforderungen, Chancen & Lösungen, University of Bamberg Press, Bamberg, Germany, 2011, pp. 104–106.

[2] Council of Energy Ministers, On the road to a fuel-ef<sup>fi</sup>cient truck, http://<sup>fl</sup>eetsmart. nrcan.gc.ca/documents/PDF/trucking.pdf2009 (accessed 27 Jan 2014).

[3] J.C. Coyle, R.A. Novack, B.J. Gibson, E.J. Bardi, Transportation: A Supply Chain Perspective, South-Western Cengage Learning, Mason, OH, 2011.

[4] S. Khuller, A. Malekian, J. Mestre, To Fill or Not to Fill: The Gas Station Problem, Proceedings of the 15th Annual European Symposium on Algorithms, 4698, 2008, pp. 534–545.

[5] S.H. Lin, R. Gertsch, J.R. Russell, A linear-time algorithm for <sup>fi</sup>nding optimal vehicle refueling policies, Operations Research Letters 35 (2007) 290–296.

[6] M. Roeth, D. Kircher, J. Smith, R. Swim, Barriers to the increased adoption of fuel efficiency technologies in North American on-road freight sector, International Council for Clean Transportation, http://www.theicct.org/sites/default/<sup>fi</sup>les/publications/ ICCT-NACFE-CSS\_Barriers\_Report\_Final\_20130722.pdf2013 (accessed 27 Jan 2014).

[7] P. Shrivastava, The role of corporations in achieving ecological sustainability, Academy of Management, The Academy of Management Review 20 (1995) 936–960.

[8] J. Stroup, R. Wollmer, A fuel management model for the airline industry, Operations Research 40 (1992) 229–237.

[9] Y. Suzuki, A generic model of motor-carrier fuel optimization, Naval Research Logistics 55 (2008) 737–746.

[10] Y. Suzuki, A decision support system of dynamic vehicle refueling, Decision Support Systems 46 (2009) 522–532.

[11] Y. Suzuki, A decision support system of vehicle routing and refueling for motor carriers with time-sensitive demands, Decision Support Systems 54 (2012) 758–767.

[12] Y. Suzuki, J. Dai, Decision support system of truck routing and refueling: a dual-objective approach, Decision Sciences 44 (5) (2013) 817–842.

[13] Y. Suzuki, A variable-reduction technique for the <sup>fi</sup>xed-route vehicle-refueling problem, Computers & Industrial Engineering 67 (2014) 204–215.

[14] T.M. Sweda, D. Klabjan, Finding minimum-cost paths for electric vehicles, Electric Vehicle Conference (IEVC) 2012 IEEE International (2012) 1–4.

[15] Transport Topics, Last Year's Diesel-Price Nightmare Teaches Fleets to Diversify Options in Buying Strategies to Cut Costs, July 27 2009. 1–2.

[16] U.K. Department for Transport, Effects of Payload on the Fuel Consumption of Trucks, London, U.K. 2007.

Yoshinori Suzuki is a Professor of Supply Chain Management and Sturgeon Faculty Fellow in Business at the College of Business, Iowa State University. He holds a Bachelor of Science in Business and Economics from Sophia University (Tokyo Japan), a Master of Business Administration in Marketing from New York University, and a Doctor of Philosophy in Business Logistics from The Pennsylvania State University. He has participated in many publicly and privately funded research projects, and has published over 30 research papers in such journals as Decision Sciences, Decision Support Systems, Journal of Business Logistics, Journal of Transportation Engineering, Naval Research Logistics, and Transportation Research (various parts). His research interest centers on freight logistics and motorcarrier management issues.

Frank Montabon is an Associate Professor of Supply Chain Management at Iowa State University. His PhD in Operations and Sourcing Management is from Michigan State University. He has earned the following certi<sup>fi</sup>cations from APICS: Certi<sup>fi</sup>ed in Production and Inventory Management, Certi<sup>fi</sup>ed in Integrated Resource Management, and Certi<sup>fi</sup>ed Supply Chain Professional. He has earned Certi<sup>fi</sup>ed Professional in Supply Management from the Institute for Supply Management. Dr. Montabon's research focuses on issues of environmental management. He has done large scale surveys on ISO 14000 and published research on the ef<sup>fi</sup>cacy of environmental approaches. His current research projects involve the effect of proactive environmental efforts on innovation, factors correlating to successful environmental management system implementation, and food supply chains.

Shih-Hao Lu is a Supply Chain Management doctoral student at the College of Business, Iowa State University. He holds a Bachelor of Science in MIS degree from National Central University (Taiwan), and a MBA degree from National Taiwan University of Science and Technology. His research interests include logistics, operations research, and green supply chains.
