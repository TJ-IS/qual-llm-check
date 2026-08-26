---
otero_id: 13742
otero_key: "UM3VF5VH"
title: "Controlling power systems with price signals"
authors: "Fernando L. Alvarado"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.05.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Controlling power systems with price signals

Fernando L. Alvarado

ECE Department, The University of Wisconsin, Madison, Wisconsin 53706, United States Christensen Associates, Madison, Wisconsin 53705, United States

Available online 27 July 2004

## Abstract

This paper revisits the possibility of controlling the power system entirely by means of price signals. It expands on notions introduced in an earlier paper and addresses several unresolved issues: problems with linear cost structures, response delays, varying costs, market power and stability problems caused by market/system interactions. The results suggest that control by price can, in fact, be made to work with some caveats. <sup>D</sup> 2004 Published by Elsevier B.V.

Keywords: Congestion management; Real time pricing; RTP; Stability; Optimal power flow; OPF

## 1. Introduction

Fred Schweppe and his co-workers [4,12–14] published a series of seminal papers on homeostatic control of a power system. These papers laid the foundation for the notion of using prices to control a power system. An important extension of the work of Schweppe was provided by William Hogan, who in 1992 introduced the concept of contract networks as a practical extension to these earlier notions because it permitted the establishment of property rights within networks and allowed (approximately) efficient prices to be determined from a dispatch that was influenced by the judgment of human operators [8]. More recently, Glavitsch and Alvarado [6] illustrated how (at least in principle) an operator could use prices to control congestion in the power system even under conditions where no information was explicitly shared by the generators with the system operator. The work by Glavitsch and Alvarado not only used prices (and prices alone) to resolve the problem of managing congestion, but further established in a theoretical setting that the system operator (who in this work was also in charge of <sup>b</sup>clearing<sup>Q</sup> a real time market) could <sup>b</sup>post<sup>Q</sup> prices for every node location that attained the desired objective of attaining optimal system dispatch without the need for any bids. Even after a serious disturbance, an operator could, in theory, post prices that would result in a new system equilibrium that would not only be optimal but also resolve the congestion. This was possible under the assumption that every generator would choose to operate anytime the price offered was above its marginal cost of production. Furthermore (and significantly) this work illustrated how the operator could infer and anticipate the behavior that any particular price pattern would elicit from generators prior to issuing and posting prices. This was, of course, subject to several clearly stated assumptions about the costs (there were assumed to be quadratic) and the behavior of the generators (costs were fixed over time and no market power was ever exercised). More recently, Alvarado described in detail how to resolve many of the problems associated with <sup>b</sup>control by price<sup>Q</sup> [2]. This chapter extends this work.

The chapter begins with a review of the main concepts from [6] and describes issues left unresolved by this earlier work and only partially covered in Ref. [2]:

<sup>!</sup> The requirement that cost functions be quadratic. Linear functions, although seemingly simpler, complicate the control problem because their allon all-off characteristics. Linear costs would render control by prices jumpy at best, seemingly erratic under more extreme conditions, and completely unfeasible in some cases.

<sup>!</sup> Response dynamics and delays. Even if we assume that posting a price elicits a response, attaining the new equilibrium takes time and the delays in achieving the transition can create serious operational difficulties which may include the excitation of unstable electromechanical system modes [1,3] as a result of the interaction between prices and system response characteristics. Anecdotal evidence has referred to this type of problem as <sup>b</sup>price chasing behavior<sup>Q</sup> that has apparently been observed in several systems.

<sup>!</sup> Non-stationary costs. This refers to the possibility that generator costs may change with time faster than the operator can track them. The assumption that an operator can infer marginal costs from observed behavior relies on the assumption that costs do not change over time. However, in energyconstrained situations (such as hydro systems) or in cases where fuel costs are volatile, such assumption may be invalid. Of particular interest is an understanding of how bidding behavior is affected by fixed costs, ramping constraints and the existence of multiple interacting markets for a given product (the output of a generator). For additional references on expected bidding behavior, refer to [10,11].

<sup>!</sup> The possibility that generators may attempt to exercise market power and fail to respond even when the price should ordinarily induce a desired behavior [7].

One additional topic addressed in this chapter is the possibility of using price signals for controlling all aspects of system operation, including such items as reactive power injection, reserve provision and other necessary system quantities. For example, real time prices may be posted for reactive power injection (and consumption), prices may also be posted in real type related to reserve requirements (although these would be a bit harder to monitor and measure than energy prices), and a price component associated with frequency (the original component in homeostatic control) may also be posted. These prices would not only vary over the course of a day depending on system conditions, but would vary by location based on system losses and congestion conditions.

## 2. Locational marginal pricing overview

A locational marginal price (LMP) at a given point in time and at a given system location is nothing more than the cheapest way by which one can deliver one MW of electricity to a particular node while from the available generators while respecting all the constraints and system limits in effect. The locational marginal prices themselves can be calculated in a variety of ways:

1. The system can be operated optimally <sup>b</sup>before<sup>Q</sup> the 1 MW increase and <sup>b</sup>after<sup>Q</sup> the 1 MW increase of demand at any given location. The additional cost of operating the system optimally after delivering the additional MW to the location in question is the LMP of that location at that time. This particular method of determining LMPs is, of course, highly impractical, but it is of great value to understand the meaning of LMPs and why they are the correct <sup>b</sup>price signal<sup>Q</sup> by which the system should be operated.

2. The LMPs can also be obtained from a knowledge of <sup>b</sup>sensitivity factors<sup>Q</sup> (sensitivity of constraining flows to injections) for each marginal generator and a simple calculation that establishes the cost of increasing 1 MW of production at a given location while holding the offending flow(s) unchanged. A set of two equations in two unknowns (for the case of a single constraining element) is solved for each desired LMP. It is necessary to know what elements have constrained and where the marginal generators are.

3. The LMPs can be obtained as the Lagrange multipliers associated with the nodal injection equations during the solution of the underlying optimization problem (the so-called optimal power flow, or OPF). This method has the virtue that it is not necessary to know where are the marginal units or which are the constraining elements ahead of time. Of course, this is not always the desired context in which to determine LMPs.

4. The LMPs can also be obtained from a <sup>b</sup>transposed Jacobian<sup>Q</sup> solution at a given operating point, with the limiting equations replacing the <sup>b</sup>original Jacobian<sup>Q</sup> rows and columns. This is, in effect, the <sup>b</sup>adjoint network<sup>Q</sup> approach for network analysis [5].

Regardless of how obtained, the LMPs create a pattern in the network that establishes the marginal cost of electricity at any system location. Although the prices may vary a great deal as a function of location, all four methods above should give the exact same LMP values provided the same conditions are used.

Once the LMPs are known, they can be used for a variety of purposes:

1. In calculations of price settlements for energy consumed or delivered, assuming that an LMP context is the agreed-upon market design.

2. For the purpose of establishing price differences between nodes in order to establish and settle transmission property rights and award payments to the holders of financial transmission rights (FTRs).

3. As a means for posting prices in the network for the purpose of influencing the operation of the system, by taking advantage of the natural business sense of all market participants, who will see it as advantageous to operate anytime the income from operating exceeds the costs of operation. This is the main topic of this paper.

## 3. Control by price—known costs

Control by price in our context means that to increase power production at a location, you do not send a <sup>b</sup>raise<sup>Q</sup> pulse to the generator. Instead, you increase the posted price—and wait for the generator(s) to respond. To increase production everywhere, you increase the price everywhere—and wait. To reduce production, you lower the price. In a more extended implementation of control by price, to get reactive power production and regulate voltage, you post a price for reactive power. To get <sup>b</sup>reserves<sup>Q</sup>, you post a price for the reserves. We assume, of course, that posting of a price at a node elicits a (nonmandatory) response on the part of every generator. Every generator (and every load, for that matter) will be free to choose whether to increase or decrease its output (or increase or decrease its consumption). If the price posted is the locational marginal price and every generator responds according to their cost, optimal operation should ensue.

While such price responsiveness may not be as simple and transparent as we assume it to be, there is sufficient evidence from actual systems (PJM and New York) to suggest that the system is, indeed, responsive to price.

In this section, we summarize the findings of Ref. [6]. Two situations are considered. If the costs of operation for each generator in the network are known to the system operator, then the optimal operating point can be readily obtained by solving an optimum power flow problem. This solution will, in fact, determine the prices that can be sent to the market to attain the desired optimum point under the assumption that the costs of every generator are not only know, but quadratic functions of production level.

The key concept of Ref. [6] is that we can convert a <sup>b</sup>congested optimization<sup>Q</sup> problem into an <sup>b</sup>uncongested optimization<sup>Q</sup> problem with an identical solution, and we can do so without having to know what the costs of the various generators are, provided we can assume that the costs of the generators are quadratic and invariant. The concept is best illustrated

![](/api/attachments/UM3VF5VH/fulltext/images/377e1282531ccbd5de050b2c6d951fe6d5f438f9d999fb3a29a3f351ed3c68ef.jpg)

Fig. 1. Solution as an unconstrained problem. The solution is unfeasible.

first considering a case where the costs are known. Let the generation costs for generator i be:

$$
C _ {i} = a _ {i} + b _ {i} P _ {i} + \frac {1}{2} c _ {i} P _ {i} ^ {2}\tag{1}
$$

For a lossless system with a given demand, the power balance equation is:

$$
P _ {1} + P _ {2} + \dots + P _ {n _ {\mathrm{g}}} = P _ {\mathrm{D}}\tag{2}
$$

The Lagrangian for this optimization problem is:

$$
\begin{array}{l} L = \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \left(a _ {i} + b _ {i} P _ {i} + \frac {1}{2} c _ {i} P _ {i} ^ {2}\right) \\ \quad + \lambda \big (P _ {1} + P _ {2} + \dots + P _ {n _ {\mathrm{g}}} - P _ {\mathrm{D}} \big) \end{array}\tag{3}
$$

And the optimality conditions are:

$$
\begin{array}{c} b _ {1} + c _ {1} P _ {1} = \lambda \\ b _ {2} + c _ {2} P _ {2} = \lambda \\ \vdots \\ b _ {n _ {\mathrm{g}}} + c _ {n _ {\mathrm{g}}} P _ {n _ {\mathrm{g}}} = \lambda \\ P _ {1} + P _ {2} + \dots + P _ {n _ {\mathrm{g}}} = P _ {\mathrm{D}} \end{array}\tag{4}
$$

Or, in matrix form:

$$
\left[ \begin{array}{c c c c c} c _ {1} & & & & - 1 \\ & c _ {2} & & & - 1 \\ & & \ddots & & \\ & & & c _ {n _ {\mathrm{g}}} & - 1 \\ \hline 1 & 1 & & 1 \end{array} \right] \left[ \begin{array}{c} P _ {1} \\ P _ {2} \\ \vdots \\ P _ {n _ {\mathrm{g}}} \\ \hline \lambda \end{array} \right] = \left[ \begin{array}{c} - b _ {1} \\ - b _ {2} \\ \vdots \\ - b _ {n _ {\mathrm{g}}} \\ \hline P _ {D} \end{array} \right]\tag{5}
$$

Using <sup>b</sup>Matlab notation<sup>Q</sup>, this becomes:

$$
\begin{array}{l} \operatorname{diag} (c) P - \operatorname{ones} (n _ {\mathrm{g}}, 1) \lambda = - b \\ \operatorname{ones} (1, n _ {\mathrm{g}}) P = P _ {\mathrm{D}} \end{array}\tag{6}
$$

If a line congests, the resulting congestion condition can be expressed as one more constraint, which in Matlab notation becomes:

$$
\boldsymbol {S P} = \boldsymbol {p} ^ {\max}\tag{7}
$$

This introduces an additional Lagrange multipliers, l. The new expanded equations at the solution point are:

$$
\begin{array}{l} \operatorname{diag} (\boldsymbol {c}) \boldsymbol {P} - \operatorname{ones} (n _ {\mathrm{g}}, 1) \lambda + \boldsymbol {S} ^ {T} \mu = - \boldsymbol {b} \\ \operatorname{ones} (1, n _ {\mathrm{g}}) \boldsymbol {P} = P _ {\mathrm{D}} \end{array}
$$

$$
\boldsymbol {S P} = \boldsymbol {p} ^ {\max}\tag{8}
$$

At the heart of the method is the premise that the same solution $P ^ { * }$ can be attained by price alone if a vector $\beta$ is added to the vector b. This <sup>b</sup>congestion price adjustment<sup>Q</sup> vector can be determined as follows:

$$
\boldsymbol {\beta} = - \operatorname{diag} (\boldsymbol {c}) \boldsymbol {P} ^ {*} + \operatorname{ones} (n _ {\mathrm{g}}, 1) \lambda - \boldsymbol {b}\tag{9}
$$

Once this vector is determined, it is used as a price signal that, in effect, modifies b. The result is an uncongested problem that has the same solution as the congested problem:

$$
\begin{array}{l} \operatorname{diag} (c) \boldsymbol {P} - \operatorname{ones} \left(n _ {\mathrm{g}}, 1\right) \lambda = - (\boldsymbol {b} + \boldsymbol {\beta}) \\ \operatorname{ones} \left(1, n _ {\mathrm{g}}\right) \boldsymbol {P} = P _ {\mathrm{D}} \end{array}\tag{10}
$$

We illustrate the process with a numeric example. Consider the system in Fig. 1. If this problem is solved ignoring the flow constraint, the solution obtained is as given.

Consider now the calculation and issuing of the price signal $\beta$ and the solution of the subsequent optimization problem (whether the solution is attained <sup>b</sup>centrally<sup>Q</sup> or by self-dispatch by the generators). The result is illustrated in Fig. 2.

The implication of this result is that market participants responding only to posted price signals would converge to an optimal dispatch without the need to be aware of any congestion relief efforts on the part of the system dispatcher.

![](/api/attachments/UM3VF5VH/fulltext/images/a82776831d1ff6e2a293ebf0259982a7fb815b3c7fcd26d8d2a58a33c15c851b.jpg)

Fig. 2. Unconstrained solution with locational price adjustments. The solution is feasible and optimal.

## 4. Control by price—unknown costs

The more interesting situation is when the costs of every generator are unknown to the system operator. If one can assume that the costs are not only quadratic, but also invariant with time, then it is possible to infer these costs from an observation of the response of generators to market prices. Ref. [6] illustrates how a sequence of market observations are sufficient to establish enough information about the behavior of generators to price signals to be able to predict their behavior under any other price signal sent to them. If this is true, it then becomes feasible to operate the system by issuing the <sup>b</sup>correct<sup>Q</sup> price signals necessary to induced the desired optimal behavior under any other set of conditions, including conditions that result in congestion of one or more lines. These price signals turn out to be none other than the locational marginal prices, although in the context used in the present paper these are not so much locational marginal prices as they are signals to control generator output.

In order to understand the process of estimating the cost parameters from a set of market observations, we make the following assumptions:

<sup>!</sup> The costs of all suppliers are indeed quadratic, characterized by (initially unknown) parameters $b _ { i }$ and $c _ { i } ,$ and there are no fixed costs of concern.

<sup>!</sup> The quadratic cost coefficients $c _ { i }$ are all nonzero and positive, and the linear cost coefficients $b _ { i }$ are positive (non-declining marginal costs).

<sup>!</sup> There are no ramping limits.

<sup>!</sup> The generators for which the estimate is done have reached neither their low limit nor their high limit during these observations.

<sup>!</sup> There are no startup and shutdown costs of concern.

<sup>!</sup> The cost parameters of all suppliers do not change from observation to observation.

<sup>!</sup> The same units participate in all rounds of observations.

<sup>!</sup> The observed behavior is steady-state, after any transients have settled.

The author admits up front that these assumptions are completely impractical. The purpose of this section is, however, to illustrate feasibility of cost inference even under these highly impractical conditions. Once the method is establish for these theoretical conditions, it can be adjusted for departures from (some) of these assumptions.

We will perform a number of <sup>b</sup>market observations<sup>Q</sup> from which we will infer the generator costs. The first set of observations corresponds to a case with no congestion. Under these conditions, the system settles into a solution determined from:

$$
\boldsymbol {b} + \operatorname{diag} (\boldsymbol {c}) \boldsymbol {P} ^ {0} = \operatorname{ones} \left(n _ {\mathrm{g}}, 1\right) \lambda_ {0}\tag{11}
$$

This is the first (or base case) observation. As system conditions change, the generation pattern will change and so will k. A later, second (still uncongested) system observation will result in a different pattern and a different price. This new point will be characterized by:

$$
\boldsymbol {b} + \operatorname{diag} (\boldsymbol {c}) \boldsymbol {P} ^ {1} = \operatorname{ones} \left(n _ {\mathrm{g}}, 1\right) \lambda_ {1}\tag{12}
$$

The difference between these two observations leads to the following equation:

$$
\operatorname{diag} (\boldsymbol {c}) \Delta \boldsymbol {P} = \Delta \lambda \text { ones } (n _ {\mathrm{g}}, 1)\tag{13}
$$

Based on this last equation, changes in power generation are in inverse proportion to the respective constants. In other words, we have that:

$$
c _ {1} \Delta P _ {1} = c _ {2} \Delta P _ {2} = \dots = c _ {n _ {\mathrm{g}}} \Delta P _ {n _ {\mathrm{g}}} = \Delta \lambda\tag{14}
$$

If we have access to the change in price $\Delta \lambda$ , then the constants $c _ { i }$ can be determined from these two observations alone. However, if more observations are available, the quadratic coefficients can be determined redundantly, leading to more robust estimates.

The linear cost coefficients can now be determined from $b _ { i } { = } { - } c _ { i } \cdot P _ { i } { + } \lambda _ { i }$

A more elaborate procedure can be set up if the case where the observations are made involves congestion. This is likely to be inevitable, because some generators will never operate unless congestion occurs and they are properly situated.

## 5. Piecewise-linear costs

When the cost characteristics of a given generator are purely linear (constant marginal costs), any response to a price above the marginal cost of the unit will tend to maximize the output of the unit.<sup>1</sup> For large units, this can result in situations where a steady-state solution simply cannot be attained by price alone.

![](/api/attachments/UM3VF5VH/fulltext/images/dee71d4aab6233b5ac62630ddfc895f8353b45839b546897841b3d39498a26d1.jpg)  
Fig. 3. Linear cost case, optimal solution.

We illustrate the nature of this problem with a simple example. Consider the system in Fig. 3. The optimal solution for this linear cost case is also illustrated.

If we attempt to reach this optimal operating point by price alone, we fail. Fig. 4 illustrates two possible situations, neither of which succeeds in the attempt.

## 6. Response dynamics

The analysis in Ref. [6] assumed only steadystate operation. The transition from any given operating state to an optimal operating state took place immediately. In practice, there are sometimes significant delays within the system. There are delays in determining and posting of prices. There are also delays due to ramping rate limitations of generators.

To illustrate the nature of the possible problems associated with delays, consider the example from Fig. 1, but where the load has just suddenly jumped from 100 to 200 MW (as a result, for example, of the loss of 100 MW of local generation, not shown). The pre-disturbance optimal dispatch corresponds to $P _ { \mathrm { g l } } { = } 1 0 0$ , no overload occurs and both prices are equal to US\$10/MW h. The ultimate optimal dispatch, attainable by pricing alone, is illustrated in Fig. 2. After the disturbance and before any pricing response is attained the generation/load balance is attained by the generator automatic frequency response (AGC) characteristics. Assume both generators have equal AGC characteristics. The response after the disturbance will be $P _ { \mathrm { g l } } { = } 1 5 0$ and $P _ { \mathrm { g } 2 } { = } 5 0$ . This results in an overload, which will hopefully be corrected by the response to prices. However, the occurrence of the overload may prompt the operator to post an even higher price in order to elicit the participation of some other generator that, although more expensive, may have better response characteristics. Of course, this will distort the eventual steady state and will require that prices once again be adjusted after the transitional period is over. The ultimate result can be a sequence of over and under-corrections to account for the slowness of some generating units.

An additional concern associated with response dynamics is the possibility the response delays will result in oscillations or, worse yet, instabilities.

## 7. Putting it together

On the surface, it would appear that control by price is doomed if either delays or linear (or worse yet, declining) marginal costs are the norm. However, the problem can be at least partially resolved as follows:

![](/api/attachments/UM3VF5VH/fulltext/images/c9a77afa0e70e1f817fd76d80b5c0f74920d1dd9dbad19209960a8c8d7d8957c.jpg)

![](/api/attachments/UM3VF5VH/fulltext/images/ab0df52e0ce4092566e5aa3516e0d099e809d9a2937fff3a94ac39b13f162b4b.jpg)  
Fig. 4. Neither price pattern leads to optimality. (a) Case 1: this dispatch is not feasible: the line overloads. (b) Case 2: this dispatch is feasible but not optimal.

<sup>!</sup> Losses have a tendency to vary as a quadratic function of any single injection. A price signal can be sent that reflects the quadratic nature of the losses and the (usually) diminishing marginal value of injection at any single location as a function of supply. Assume, for example, that the losses associated with injections at location 1 for Fig. 2 relative to the same injection at location 2 were losses $= 0 . 0 2 5 P _ { g 1 } ^ { 2 }$ , then a price signal that reflected the losses would include an additive price term equal to $\Delta \pi { = } 0 . 0 5 P _ { g 1 }$ , which would modify the corresponding value of b. This would transform the problem in Fig. 2 to the problem in Fig. 1 and eliminate the issues associated with linear cost structures.

<sup>!</sup> Assume that the response time capability of each unit is 10 MW/min (linear). A price signal above the cost would elicit a <sup>b</sup>ramp up<sup>Q</sup> response at this rate. A price signal below this rate would elicit a lowering of the output of a unit, at the same rate. If prices were to be adjusted every 2 min, it would be possible to attain a <sup>b</sup>near optimal<sup>Q</sup> limit cycle response by an alternating sequence of prices, as illustrated in Fig. 5.

(a)  
![](/api/attachments/UM3VF5VH/fulltext/images/39b90936f2dfc769c17f5a788f7b9282adbb040484c4e4ecceadc1410b369e5d.jpg)

(b)  
![](/api/attachments/UM3VF5VH/fulltext/images/a9ef45d028c595d7660e7f8e3f8a22db4474802e8bb437bc34fb24f09de8b0d6.jpg)  
Fig. 5. Quasi-steady state quasi-optimal response attained by timedomain price modulation. (a) Price as a function of time period. (b) Output of generators and line flow.

To formalize this analysis somewhat, assume that the response of each unit to a given price is linearly proportional to the price difference, but that price changes must be done discretely, in 1 MW increments. The use of discrete price changes is one way of attaining a certain <sup>b</sup>hysteresis<sup>Q</sup> in the loop, which will have the tendency to stabilize the system.

## 8. Non-stationary costs

Part of the way in which Ref. [6] established that the system could be steered to an optimal operating point was because the operator was able to infer generator marginal costs. That, coupled with the assumptions of a quadratic cost, no market power and an instantaneous response capability, leads to the ability to steer the system to almost any desired new condition. However, in many cases the costs of operation (whether they are actual fuel costs or opportunity costs) can vary over time. Such an effect would diminish the ability of an operator to properly predict response to a posted price and increase the difficulty associated with <sup>b</sup>control by price.<sup>Q</sup>

The solution to difficulties associated with nonstationary costs is two-fold:

<sup>!</sup> First, a more complete model of the generator cost structure can be established and parameters to this model can be fit by market observation. Parameters that may matter in the assessment of generator response include minimum up or down times, startup and shutdown costs, and status of the generator total energy or emissions limitations. A more complete assessment of generator parameters by market observation alone is beyond the intent of this paper.

<sup>!</sup> Second, the operator may rely on feedback observations. Anytime prices are issued, it is possible to ascertain who is responding to a price pattern change and take action according to the observed degree of response. In other words, an operator would not attempt to steer the system to a new optimal point, only steer the system in the direction of a better operating point. In a sense, this is precisely what locational marginal pricing is about.

## 9. Market power issues

In all the foregoing, there has been the implicit assumption that there is no market power either possible or being exercised by any generator. In a market where generators bid prices and the operator clears the market, the exercise of market power (or the attempt to exercise market power) could manifest itself as higher price bids on the part of generators or alternatively as the withholding of generators from production. In the present framework, where there are no bids, only posted prices, market power would manifest itself as the refusal of generators from participating in production, even under conditions where the prices posted are above the marginal costs of a generator.

Market power is difficult to detect. Market power refers to the ability to raise prices significantly above the efficient economic equilibrium by either raising prices (economic withholding) or by withholding quantity (capacity withholding). In the case of control by price, only capacity withholding makes sense, since there is no explicit <sup>b</sup>price bidding<sup>Q</sup> in effect.

To see how capacity withholding can benefit a generator, consider the case of an entity owning two generating units, and privy to the information that if one of its units were to be withheld this would most likely result in a significant increase in the market price associated with the other unit. This is illustrated in Fig. 6.

Detecting market power is not simple. There are essentially two approaches: (a) Simulate the system and try to predict what the price should be in the absence power, or (b) try to predict the behavior of profit-maximizing market participants that are pricetakers and verify if the behavior of actual participants is consistent with this behavior. Approach (a) is quite difficult to make work. Only approach (b) seems to be practical [9]. Thus, for purposes of market monitoring, it is essential to be able to anticipate optimal dispatch and bidding policy on the part of every generator. Such an effort needs to be an integral part of any <sup>b</sup>control by price<sup>Q</sup> system.

(a)  
![](/api/attachments/UM3VF5VH/fulltext/images/13dc086eb81c2f548d29faca8e4171fd55be544474cb42b5b1b675566b5b2295.jpg)

(b)  
![](/api/attachments/UM3VF5VH/fulltext/images/da23a6e886d135124209e65bbb8ca41919237f0e0c1309a1e130e670a9ad0645.jpg)  
Fig. 6. Prices rise and supplier surplus increases as a result of one supplier withholding output. (a) Initial clearing price, no profits (no surplus). (b) Clearing price if blue supplier withholds one unit.

## 10. Voltages, reserves and stability

Consider the extension of the notion of controlling a system by price alone to the control of quantities other than energy alone. We discuss two such quantities: voltage and reserves.

The control of voltage in the system is done primarily by means of reactive power injection. Under conditions where voltages are essentially within acceptable ranges, the only significant value of reactive power is as a means of reducing system losses. However, reactive power injections can have significant value under limiting conditions. The two features that distinguishes reactive power in a control by price system are (a) its volatility is likely to be quite high, (b) its time response characteristics are likely to be much faster and (c) it often is <sup>b</sup>lumpy<sup>Q</sup> rather than continuous (this is specially the case for switched shunt system elements).

Reserves correspond, by definition, to unused capacity in generating units that can be made available on short notice upon the occurrence of system events and outages. Creating a reserve market can be done exactly as the main market on energy (it can have locational components), but it also requires that speed of response be specified and that the manner in which the activation of these reserves is to take place (perhaps the only needed signal is a drop in system frequency, but more commonly it can be expected to be explicit signals sent to the reserve generators.

The final topic that deserves mention is stability. A perfectly stable system, when connected to a perfectly rational and stable market can give rise, under some conditions, to electromechanical stabilities. Thus, care must be exercised when including price as part of an electromechanical system feedback loop. Instabilities (including electromechanical instabilities) can develop. For further details, see Refs. [1,3].

## 11. Control by price in practice

One can say that an LMP system (such as the LMP system in effect in PJM or in New York) is accomplishing what this paper has described. Indeed, except for some aspects pertaining to the lack of signals for voltage support or the disregard of piecewise-linear effects or dynamic response issues, this is precisely what is being done. Real world operation seems to suggest that some of the concerns raised in this paper are not a major impediment to control by price. Both the PJM and the New York systems seem to be functioning relatively well. A different perspective on the same issue, however, would suggest that many of the present (albeit minor) problems and difficulties associated with the operation of these actual systems are, in fact, due to the very issues raised in this paper. A more thorough understanding of the nature of these problems (particularly market power issues) will eventually lead to better and smoother market designs and better operation of electricity markets.

## 12. Conclusions

Control by price can be viewed as a natural and logical extension of locational marginal pricing. In principle, it leads to the same optimal operating point, with the added advantage that control by price is more compatible with true free markets. Two of the main limitations of control by price (namely linear or declining marginal cost structures) can be addressed, at least in principle, with a proper design of the price signals that are sent to the market. Limitations associated with variability of costs will require better modeling of generator cost characteristics, a topic beyond the scope of this paper. Market power issues remain a large concern, but the issue is no different in a <sup>b</sup>control by price<sup>Q</sup> environment than it is in a more conventional market design. Finally, the entire market and electrical control system must be analyzed as a single joint system in order to establish the stability of the feedback controls. Failure to do so can lead to operational problems.

With respect to the possible extension of control by price, there seem to be no fundamental limitations about the possibility of extending control by price to also encompass voltage control and even reserves, provided appropriate signals are given in a timely manner. Market deployment of this concept will, however, require time and careful design of the precise requirements.

## Acknowledgment

This work was supported by the CERTS consortium under DOE Interagency Agreement DE-AI-99EE35075 with NSF. The author also gratefully acknowledges Rajesh Rajaraman for discussions that led to the improvement of the paper.

## References

[1] F.L. Alvarado, The stability of power system markets, IEEE Transactions on Power Systems 14 (2) (1999 May) 505–511.

[2] F.L. Alvarado, Is system control entirely by price feasible? Proceedings of 2003 HICSS, Waikoloa, Hawaii, 2003 January.

[3] F.L. Alvarado, J. Meng, C. DeMarco, W. Mota, Stability analysis of interconnected power systems coupled with market dynamics, IEEE Transactions on Power Systems 16 (4) (2001 November) 695– 701.

[4] M.C. Caramanis, R.E. Bohn, F.C. Schweppe, Optimal spot pricing, theory and practice, IEEE Transactions on Power Apparatus and Systems 109 (9) (1982 September) 3234– 3245.

[5] S.A. Director, R.A. Rohrer, The generalized adjoint network and network sensitivities, IEEE Transactions on Circuit Theory 16 (3) (1969 August) 317 – 323.

[6] H. Glavitsch, F.L. Alvarado, Management of multiple congested conditions in unbundled operation of a power system, IEEE Transactions on Power Systems 13 (3) (1998 August) 1013– 1019.

[7] S.M. Harvey, W.W. Hogan, Market power and withholding, December 2001, ksghome.harvard.edu/\~.whogan.

[8] W.W. Hogan, Contract networks for electric power transmission, Journal of Regulatory Economics 4 (1992) 211 – 242.

[9] R. Rajaraman, F.L. Alvarado, Testing for market power in hydro-dominant regions, VIII SEPOPE, Brasilia, Brazil, 2002 May.

[10] R. Rajaraman, F.L. Alvarado, (Dis)-Proving Market Power, PSerc publication 02–06, March 2002, www.pserc.wisc.edu, Revised September 2003.

[11] R. Rajaraman, F.L. Alvarado, Optimal bidding strategies in electricity markets under uncertain energy and reserve prices, PSERC Report 03–05, April 2003, www.pserc.wisc.edu.

[12] F.C. Schweppe, R.D. Tabors, J.L. Kirtley Jr., H.R. Outhred, F.H. Pickel, A.J. Cox, Homeostatic utility control, IEEE Transactions on Power Apparatus and Systems PAS-99 (3) (1980 May–June) 1151–1163.

[13] F.C. Schweppe, M.C. Caramanis, R.D. Tabors, Evaluation of spot price based electricity rates, IEEE Transactions on Power Apparatus and Systems PAS-104 (7) (1985 July) 1644– 1655.

[14] F. Schweppe, M. Caramanis, R. Tabors, R. Bohn, Spot Pricing of Electricity, Kluwer Academic, 1987.

Dr. Fernando L. Alvarado is Professor Emeritus, The University of Wisconsin, Madison, WI 53706. Also, he is Senior Consultant with Christensen Associates, Madison, WI 53705.
