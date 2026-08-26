---
otero_id: 21666
otero_key: "JGTKJPMJ"
title: "Error analysis in electric power system available transfer capability computation"
authors: "Peter W Sauer; Santiago Grijalva"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00074-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Error analysis in electric power system available transfer capability computation

Peter W. Sauer <sup>)</sup>, Santiago Grijalva

Department of Electrical and Computer Engineering, 1406 W. Green St., UniÕersity of Illinois at Urbana-Champaign, Urbana, IL, USA

## Abstract

A key concept in the restructuring of the electric power industry is the ability to accurately and rapidly quantify the capabilities of the transmission system. Transmission transfer capability is limited by a number of different mechanisms, including thermal, voltage, and stability constraints. This paper discusses the available transfer capability ATC definitionsŽ . and determination guidelines approved by the North American Electric Reliability Council NERC and presents severalŽ . concepts for dealing with the potential errors and technical challenges of computation. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Available transfer capability ATC ; Power system loadabilityŽ .

## 1. Introduction

This paper revises and expands the two conference papers referenced in Refs. 12,13 . It summarizes recent results on the approximations of available transfer capability ATC computations and theŽ . analytical treatment of errors.

There has been interest in quantifying the transmission transfer capabilities of power systems for many years. When systems were isolated and largely radial, these capabilities were fairly easy to determine and consisted mainly of a combination of thermal ratings and voltage drop limitations. In most cases, these two limitations were easily combined into a single power limitation either MW, MVA, or Ž SIL . As such, ATC for a given transmission line at.

a given time could be interpreted as the difference between the power limitation and the existing power flow. The North American Electric Reliability Council NERC has been careful to distinguish the word Ž . ‘capacity’ from the word ‘capability’. Capacity is normally a specific device rating i.e., thermal ,Ž . whereas capability refers to a limitation which is highly dependent on system conditions. Another interpretation is that capacity refers to the ability of a system to serve native load and engage in transfers while capability is solely the ability to engage in transfers.

As isolated systems became interconnected for economic and reliability reasons, looped networks introduced technical issues with the definition and calculation of ATC. In addition, the differences between contract path and actual power-flow path introduced additional complexity to the quantification of ATC. System stability became an important constraint for some areas of the interconnected network and this required the consideration of a third limiting phenomena. The introduction of St. Clair curves were one of the first attempts to include thermal, voltage, and stability constraints into a single transmission line loading limitation 17 . These results<sup>w</sup> <sup>x</sup> were later verified and extended from a more theoretical basis in Ref. 5 . This ‘single rating’ concept<sup>w</sup> <sup>x</sup> is extremely valuable from a computational point of view. Linear load flow and linear programming solutions made transmission transfer capability determination relatively fast and easy 10,9,18,6,11 . They <sup>w</sup> <sup>x</sup> focused on both the ‘Simultaneous Interchange Capability SIC ’ and the ‘Non-Simultaneous Inter- Ž . change Capability NSIC ’. Many extensions to thisŽ . work have appeared including economic dispatch and nonlinear considerations such as VAR limits and transient stability constraints 1,8,14–16 .<sup>w</sup> <sup>x</sup>

## 2. Documentation and definitions

In May 1995, NERC revised its earlier reference documents on transfer capability to provide additional clarifications and examples 19 . This 1995<sup>w</sup> <sup>x</sup> document recommends two NERC transfer capability measures: ‘First Contingency Incremental Transfer Capability FCITC ’ and ‘First Contingency To- Ž . tal Transfer Capability FCTTC ’. The FCITC wasŽ . defined to be the amount of electric power, incremental above normal base power transfers, that can be transferred over the interconnected transmission systems so that the following conditions are met.

Ž .a From a given system configuration with precontingency operating procedures in effect, all facility loadings are within normal ratings and all voltages are within normal limits.

Ž . b The given system remains stable following a disturbance that results in the loss of any single element line, transformer, generating unit, etc. .Ž .

Ž . Ž c The post-contingency system after operation of any automatic operating systems, but before any post-contingency operator-initiated adjustments has . all facility loadings within emergency ratings and all voltages within emergency limits.

The concept of voltage collapse can be considered to be included either in the voltage limit or the stability limit. The concept of bifurcation can be considered to be included in the stability limit. The time frame for stability is considered to be between milliseconds and several minutes. The FCTTC was defined to be the total amount of electric power Ž . normal base power transfers plus FCITC that can be transferred between two areas satisfying the above criteria.

The issue of ‘before any post-contingency operator-initiated adjustments’ in c above attempts toŽ . define the range of contingency cases and specific scenarios which must be considered. Unfortunately, this does not specifically address the many ‘operator guidelines’ which can potentially change the necessary contingency scenario and case outcome.

The terminologies SIC and NSIC originally referred primarily to the ability of an area to import from more than one other area. If this import capability was from only one other area, it was the NSIC for that area. If the import capability was from two or more areas simultaneously, it was the SIC for those areas. Today the term ‘Simultaneous’ refers primarily to the notion of more than one transaction and ‘Non-simultaneous’ refers to a single transaction.

The movement towards open-access transmission and associated recent rulings of the Federal Energy Regulatory Commission FERC have added consid-Ž . erable emphasis to the interest in quantifying electric power system transmission capabilities. This interest has led to new definitions and recommended methods of determination by NERC 20 . Through this<sup>w</sup> <sup>x</sup> document, virtually all players in the U.S. interconnected electric power system agree on the six ATC principles which are paraphrased as follows.

ATC calculations must:

Ž .a give a reasonable and dependable indication of transfer capabilities.

Ž . b recognize time-variant conditions, simultaneous transfers, and parallel flows.

Ž .c recognize the dependence on points of injection<sup>r</sup>extraction.

Ž . d reflect regional coordination to include the interconnected network.

Ž .e conform to NERC and other organizational system reliability criteria and guides.

Ž .f accommodate reasonable uncertainties in system conditions and provide flexibility.

This 1996 document introduces several new terms which refine the concepts of the 1995 documents and specifically identify quantities associated with uncertainty in modeling and system conditions. The ‘Total Transfer Capability TTC ’ is essentially the same asŽ . the FCTTC discussed above with the following clarification. If the maximum transfer capability of the pre-contingency system using normal limits is less than that of all first-contingency cases considering emergency limits, the TTC is the more restrictive number. If an area considers multiple contingencies to ensure reliability, and these transfer capabilities are more restrictive, then the TTC is this more restrictive number. As such, the word ‘Contingency’ does not explicitly appear in the new term. The ‘Transmission Reliability Margin TRM ’ is the Ž . amount of transmission capability necessary to ensure that the interconnected network is secure under a reasonable range of uncertainties in system conditions. The ‘Capacity Benefit Margin CBM ’ is the Ž . amount of transmission transfer capability reserved by load serving entities to ensure access to generation from interconnected systems to meet generation reliability requirements. With these two terms added, ATC is equal to:

## ATC<sup>s</sup>TTC<sup>y</sup>TRM<sup>y</sup>ETC<sup>y</sup>CBM

where ETC is the sum of ‘Existing Transmission Commitments which includes retail customers ’.Ž . This ETC term essentially includes all normal pre-Ž transfer transmission flows included in the given. case. The ETC and CBM quantities can be further described in terms of their contractual firmness using terminology such as ‘Recallable’, ‘Non-recallable Ž . or ‘Firm’ and ‘Non-Firm’ , ‘Scheduled’, and ‘Reserved’ transfers. The contractual nature of the transaction could influence the level of assurance needed to ensure a transfer can take place. This means that more contingencies may be studied for the more firm transactions. Since the full impact of these terms on the computational burden of ATC calculations is not clear at this time, they are not discussed further. Instead, this paper focuses on the TTC and TRM calculations.

## 3. Dealing with the technical challenges

A possible scenario for the computation of TTC proceeds as follows.

Ž .a Definition of a base case. This may be a current or forecasted condition, existing or planned configuration and must specify what is meant by areas. An ‘area’ may include one or more generators. If it is one generator, the increase or decrease of power out is easily specified. If it is more than one generator, the appropriate unit allocation dispatch Ž . must be specified both for the increase and decrease in outputs.

Ž . b Specification of contingencies. The exact list of contingencies could vary from single outages such as a loss of a line or generator, to complex fault<sup>r</sup>switching scenarios. The number of contingencies to be considered could vary from a very small number to thousands.

Ž .c Determination of network response. A computer simulation is done to determine how the specified generation changes impact transmission line flows, system voltages, and stability margins. This must be done for the base case with normal limits enforced plus all specified contingencies with emergency limits enforced.

Ž . d Finding the maximum transfer. It is possible that the base case condition and configuration does not satisfy the normal constraints on line flows, voltage and stability. In this case, the TTC could be considered zero or perhaps negative. In either event, it should be considered degenerate and some modification of parameters or conditions should be obtained to make the base case secure as a starting point. From this point, a systematic procedure to increase the specified transfer must be used to determine the maximum transfer that satisfies the above criteria. While repeated incremental analysis could be used, the concept of sensitivities gives a fast estimate of this maximum. For example, power transfer distribution factors give a linear prediction of power flow distribution in response to change in generation changes. These linear factors can be used to predict the maximum generation change which can be allowed. Similar distribution factors for voltage levels and stability margins are less reliable, but may be a useful alternative to repeated full nonlinear simulation.

Ž .e Interpretation of results. In the Network Response NR method of TTC computation, the trans-Ž . fer capability from area A to area B is the maximum amount of real power that can be transferred from area A to area B by all physical paths. In the Rated System Path RSP method of TTC computation, theŽ . transfer capability from area A to area B is the amount of real power which flows over the physical paths directly connecting areas A and B under system-wide limiting conditions. As such, the computational requirements in both cases are similar, and mathematical solutions may even be the same, but the designation of capabilities is different. The RSP method includes a further allocation of capability to each physical line connecting areas A and B.

Ž . Ž . Ž . f Repeat for alternate cases. Steps a – e above must be repeated for all possible cases which may be in affect at the time the TTC number will be used. Since the TRM is designed to account for uncertainty in the model configuration and operating conditions, the alternate cases could be used to compute the TRM. The available capability for a given transfer can become smaller as more alternate but notŽ necessarily likely cases are considered. If appropri-. ately weighted by the likelihood of occurrence, this could be used to determine the TRM for this base case. This is illustrated in Fig. 1. below for the most likely base case and four less likely alternate cases. The TRM associated with the base case is determined from the most limiting TTC of the alternate cases in this case alternate 4 .Ž .

Alternatives to this systematic approach to TRM calculation could include fixed MW amounts 50Ž MW , or fixed percentages 5% . A reduction of line. Ž . ratings by some fixed percentage 2% will normallyŽ . lower the TTC. This reduction in TTC from a reduction of individual element ratings could also be used to specify the TRM.

![](/api/attachments/JGTKJPMJ/fulltext/images/014161925c7e10274565c5af272d3ba198872c932f14556b9da1695092c1096d.jpg)  
Fig. 1. Determining TRM from alternate cases.

From an engineering perspective, the challenges of ATC computation lie in the need to consider all likely base cases, all likely contingencies, and systematically compute the maximum transfer capability. In an operations environment where ATC numbers are posted on a short-term several hours basis,Ž . the number of base cases needed should be smaller than for a planning environment. However, when a given transaction is made, this transaction must be considered in the base case for future ATC calculations. This means that the ATC numbers must be updated after every transaction. A systematic method to rapidly update the ATC number after a transaction is needed. Current computation times for full ATC calculations of large systems 15,000 buses consid-Ž . ering up to 7000 contingencies for 500 different transaction directions could take up to 24 h even when linear methods are used. This means that considerable reduction in computation time is still needed. The new TRACE program which is being tested by EPRI may provide a significant new tool for these computations. This program was originally developed to compute SIC numbers 21 .<sup>w</sup> <sup>x</sup>

Sensitivity analysis may provide a useful solution to this challenge. Since the system is very likely to be in a very nonlinear region at each maximum, it is important that these sensitivities be of the ‘largechange’ type. For example, we now have largechange sensitivities to predict the impact of line outages Line Outage Distribution Factors . A simi-Ž . lar large-change sensitivity may be computable from the information obtained in the repeated alternate cases. If sensitivities of ATC to likely transactions could be computed at the same time that the ATC number itself is computed, rapid estimates could be obtained and utilized in a real-time basis. For example, when repeated alternate cases are computed to ensure all possible conditions are considered, their information could be used to estimate changes in the TTC when similar transactions actually occur.

The use of probabilistic methods to consider the impact of uncertainty has been used extensively in power systems 7,2 . These concepts may prove use- <sup>w</sup> <sup>x</sup> ful in quantifying TRM from a probabilistic approach. Expected values of ATC numbers could be used for TTC with variances used to compute TRM.

Most viable probabilistic approaches to uncertainties in parameters rely on linear approximations and zero-mean normal distributions. With this, the mean value of most quantity deviations remains at zero— providing little improvement in expectations. The computed variance does however provide an indication of a likely range of values for the deviation. If TRM is to be a ‘reduction-only’ concept, then something like 3 standard deviations from Normal might be a viable approach to computing a component of TRM.

The concept of ‘most limiting phenomenon’ may offer another approach to the reduction in computation time. Depending on the properties of the given system, it may be clear that the most limiting constraints are found in only one of the three—thermal, voltage and stability. In this case, there may be no need to consider constraints which will never be enforced. The results by Dobson and Lu 4 and <sup>w</sup> <sup>x</sup> Chiang 3 offer potentially useful tools to rapidly <sup>w</sup> <sup>x</sup> quantify distances to instability and thereby constraints for TTC calculations.

Traditional load flow and stability programs must be revised to properly enforce system limits. For example, the reactive power limit of a generator should be variable and dependent on the real power output. This should reflect the limitations of the unit capability curve.

## 4. An example

A three-area system was used to explore the various options for computing TRM. Each area consists of a single bus with generation and load as shown in Fig. 2. Each area is connected by a single line. The areas were numbered 1, 2 and 3. The base case data for the system are as follows.

Base power is 100 MVA.

Bus 1 was the swing bus with 1500 MW load

Bus 2 had 600 MW generation and 600 MW load

Bus 3 had 800 MW generation and 800 MW load

Bus 1 had a voltage set point of 1.00 pu

Bus 2 had a voltage set point of 1.00 pu

Bus 3 had a voltage set point of 1.04 pu

All line resistances were zero and there were no shunt elements.

Line 2–1 had a reactance of 0.90 pu

Line 2–3 had a reactance of 0.28 pu

Line 3–1 had a reactance of 0.37 pu

Line 2–1 had a rating of 100 MVA

Line 2–3 had a rating of 140 MVA

Line 3–1 had a rating of 130 MVA

## 4.1. Maximum transfer 2–1

The transfer under study was from bus 2 to bus 1. This was implemented by an increase in generation at bus 2, with the real power being reduced automatically by the swing generator at bus 1. The base case had zero real power flow on all lines in the initial operating point. When the generation at bus 2 was increased by 10 MW causing a 10 MW transferŽ from 2 to 1 , the real power flow on the lines became. Ž . see Fig. 3 :

![](/api/attachments/JGTKJPMJ/fulltext/images/117c833602143a2c93b092a0445879605e04bb681e6514a1d68a81dea133c0e6.jpg)  
Fig. 2. Base case.

$$
P _ {2 - 1} = 4. 1 \mathrm{MW}
$$

$$
P _ {2 - 3} = 5. 9 \mathrm{MW}
$$

$$
P _ {3 - 1} = 5. 9 \mathrm{MW}
$$

These flows provide one set of values for the realpower distribution factors for each line as 41% on 2–1, 59% on 2–3, and 59% on 3–1. From the ratings of the lines, extrapolation of the transfer using real power distribution factors to the line limits gave three transfer limits:

Limiting line 2–1: 100<sup>r</sup>0.41<sup>s</sup>244 MW transfer 1 to 2

Limiting line 2–3: 140<sup>r</sup>0.59<sup>s</sup>237 MW transfer 1 to 2

Limiting line 3–1: 130<sup>r</sup>0.59<sup>s</sup>220 MW transfer 1 to 2

The smallest of these was 220, making this the linear estimate of the Total Transfer Capability TTC fromŽ . bus 2 to bus 1. When the generation at bus 2 was increased to simulate the transfer, an increase of 203 MW brought line 3–1 to its 130 MVA limit Fig. 4 .Ž . This means that the TTC under these conditions was

203 MW rather than the predicted 220 MW. This <sup>q</sup>8.4% error is due to two things. First, the prediction assumed linear flow distribution. Second, the prediction was based only on MW flows. This implies that a TRM of up to 8.4% may be justified because of these modeling<sup>r</sup>computational errors.

## 4.2. ReactiÕe power considerations

Since the transmission line rating is an apparent power MVA limit, it is interesting to analyze how Ž . including VARs in the calculation modifies the previous ATC results for the base case.

The initial base case loading has $S _ { 3 - 1 } ^ { \mathrm { o } }$ 11 MVA Ž . see Fig. 2 in line 3–1. The line 3–1 loading limit is $S _ { 3 - 1 } ^ { \mathrm { m a x } } = 1 3 0$ MVA. Using a simplistic view of the loading margin, the available line MVA capacity can be taken to be:

$$
\Delta S _ {3 - 1} = S _ {3 - 1} ^ {\max} - S _ {3 - 1} ^ {0} = 1 3 0 - 1 1 = 1 1 9 \mathrm{MVA}\tag{4.1}
$$

Let $S _ { 2 } ^ { \mathrm { o } }$ be the initial apparent power produced by Area 2,

$$
S _ {2} ^ {\mathrm{o}} = | 6 0 0 \mathrm{MW} - j 1 4. 2 8 \mathrm{MVAR} | = 6 0 0. 2 \mathrm{MVA}
$$

Let $S _ { 2 } ^ { \mathrm { m a x } }$ be the apparent power that Area 2 needs to generate so that line 3–1 reaches its MVA limit.

![](/api/attachments/JGTKJPMJ/fulltext/images/32dfd17acb86984c1dc9aa620cbbba6e054494417ec21859a431a50a07636d75.jpg)  
Fig. 3. Ten MW changed case.

![](/api/attachments/JGTKJPMJ/fulltext/images/6dc5870bb5663d1c98d251104d8f5be72f97f3bbc80e2dc78bba3708d878981e.jpg)  
Fig. 4. Maximum transfer 2–1.

Furthermore, let $\varDelta S _ { 2 }$ be the required variation of apparent power injection in Area 2:

$$
\Delta S _ {2} = S _ {2} ^ {\mathrm{max}} - S _ {2} ^ {\mathrm{o}}\tag{4.2}
$$

Using the real-power distribution factor to predict the required apparent power injection to fully load line 3–1,

$$
\Delta S _ {2} = \Delta S _ {3 - 1} / 0. 5 9 = 1 1 9 / 0. 5 9 = 2 0 1. 7 \mathrm{MVA}.
$$

Using this with Eq. 4.2 , Ž .

$$
S _ {2} ^ {\max} = S _ {2} ^ {0} + \Delta S _ {2} = 6 0 0. 2 + 2 0 1. 7 = 8 0 1. 9 \mathrm{MVA}
$$

This means that Area 2 must generate 801.9 MVA increase its generation by 201.7 MVA forŽ . line 3–1 to reach its 130 MVA rated limit. This value is important, but is not sufficient to complete a power transaction, which is defined in terms of MWs. The active power component of $S _ { 2 } ^ { \mathrm { m a x } }$ must be found to complete the TTC calculation. To do this, the reactive power injection at a bus must be represented as a function of its corresponding active power injection. It is known that the $P { - } Q$ relation at a voltage controlled bus connected to an infinite bus through a transmission system is the one of a circle. This claim is here generalized and it will be assumed in the following calculation that the reactive power support in Area 2 is related to its active power injection as in a circle equation,

$$
\left(P _ {2} - P _ {0 \mathrm{g} 2}\right) ^ {2} + \left(Q _ {2} - Q _ {0 \mathrm{g} 2}\right) ^ {2} = S _ {0 \mathrm{g} 2} ^ {2}\tag{4.3}
$$

where $P _ { 2 }$ and $Q _ { 2 }$ are the active and reactive power generated by Area 2, and $P _ { 0 \mathrm { g } 2 } , Q _ { 0 \mathrm { g } 2 }$ and $S _ { 0 \mathrm { g } 2 }$ represent the center coordinates of the circle and its radius, respectively. The unknown parameters can be found by solving a system of three equations each corresponding to a different operating point. For the generator in Area 2, the following operating points resulting from the power flow solution were used:

$$
\begin{array}{l} P _ {2} = 6 0 0, Q _ {2} = - 1 4. 2 8 \\ P _ {2} = 6 1 0, Q _ {2} = - 1 4. 1 6 \\ P _ {2} = 6 2 0, Q _ {2} = - 1 3. 7 9 \end{array}
$$

Substituting these into Eq. 4.3 and solving theŽ . resulting three equations for the parameters,

$$
\begin{array}{l} P _ {0 \mathrm{g} 2} = 6 0 0. 1 9 \\ Q _ {0 \mathrm{g} 2} = 3 8 6. 1 4 \\ S _ {0 \mathrm{g} 2} = 4 0 0. 4 2 \end{array}
$$

Therefore, every P–Q operating point of the generator in Area 2 is assumed to satisfy:

$$
\left(P _ {2} - 6 0 0. 1 9\right) ^ {2} + \left(Q _ {2} - 3 8 6. 1 4\right) ^ {2} = 4 0 0. 4 2 ^ {2}\tag{4.4}
$$

The limit in line 3–1 will be reached when,

$$
P _ {2} ^ {2} + Q _ {2} ^ {2} = 8 0 1. 9\tag{4.5}
$$

Solving Eqs. 4.4 and 4.5 gives the injection whichŽ . Ž . fully loads line 3–1. These two equations have two solutions. In this case, one solution is unfeasible because it corresponds to an operating point beyond the steady state stability limit of generator 2. The feasible solution is $P _ { 2 } = 8 0 1 . 6 ~ \mathrm { M W }$ and $Q _ { 2 } = 3 9 . 5$ MVAR. Consequently, the corresponding variation in $P _ { 2 }$ , which stands for the TTC for Area 2, equals: 801.6<sup>y</sup>600<sup>s</sup>201.6 MW.

Similar calculations were performed for interconnections 2–1 and 2–3. The results are summarized in Table 1, and are compared to those found in the calculation without taking into account the reactive power component.

Table 1 shows the following results:

Ž .a Line 3–1 is determined as the limiting interconnection in both methods.

Ž . b When VARs are included in the calculation, the error decreases in all cases.

Ž .c For the limiting line, the inclusion of VARs reduces the error from 8.4 to <sup>y</sup>0.6%.

We therefore conclude that including the reactive power in the calculation of TTC has an effect that is not negligible and that taking into account the reactive power could be a key issue to enhance TTC calculations.

Notice that the computation of TTC including VARs is performed using two approximations: active-power constant distribution factors, and the P–Q circle relation. The total error Ž .<sup>y</sup>0.6% must therefore be assigned to each of these two components.

The accuracy of the P–Q circle approximation can be evaluated by comparing the values of $Q _ { 2 }$ using Eqs. 4.4 and 4.5 with those from the ACŽ . Ž . power flow, for different $P _ { 2 }$ operating points. This comparison is presented in the following table for the values of $P _ { 2 }$ that saturates each one of the interconnections.

The results in Table 2 show that the approximation of the relation P–Q using a circle equation is very precise, with an error less than 2%. Therefore, we conclude that the circle equation efficiently allows VARs inclusion in this case.

Table 1  
TTC calculation

<table><tr><td rowspan="3">Limit line no.</td><td colspan="5">ATC</td></tr><tr><td>Actual value</td><td colspan="2">VARs not included</td><td colspan="2">VARs included</td></tr><tr><td> $\Delta P_2$ </td><td> $\Delta P_2$ </td><td>Error (%)</td><td> $\Delta P_2$ </td><td>Error (%)</td></tr><tr><td>2-1</td><td>233</td><td>244</td><td>4.7</td><td>241.4</td><td>3.6</td></tr><tr><td>2-3</td><td>218</td><td>237</td><td>8.7</td><td>211.0</td><td>-3.2</td></tr><tr><td>3-1</td><td>203</td><td>220</td><td>8.4</td><td>201.6</td><td>-0.6</td></tr></table>

Table 2  
Evaluation of VAR–circle approximation

<table><tr><td rowspan="2">Line no.</td><td colspan="2">Actual values</td><td colspan="2">Estimated values</td></tr><tr><td> $P_2$ </td><td> $Q_2$ </td><td> $Q_2$ </td><td>Error (%)</td></tr><tr><td>2-1</td><td>833.0</td><td>59.56</td><td>60.35</td><td>1.32</td></tr><tr><td>2-3</td><td>818.0</td><td>49.44</td><td>50.13</td><td>1.41</td></tr><tr><td>3-1</td><td>803.0</td><td>40.22</td><td>40.87</td><td>1.63</td></tr></table>

## 4.3. Error in line reactance

To investigate uncertainty in the data, consider the reactance of the following lines.

Ž .a A 10% increase in the line 2–1 reactance from 0.90 to 0.99 decreased the TTC to 196 MW 3.4%Ž decrease , while a 10% decrease in the line 2–1. reactance from 0.9 to 0.81 resulted in a TTC of 212 MW 4.4% increase .Ž .

Ž . b A 10% increase in the line 2–3 reactance from 0.28 to 0.308 increased the TTC to 206 MW 1.5%Ž increase , while a 10% decrease in the line 2–3. reactance from 0.28 to 0.252 resulted in a TTC of 200 MW 1.5% decrease .Ž .

Ž .c A 10% increase in the line 3–1 reactance from 0.37 to 0.407 increased the TTC to 206 MW 1.5%Ž increase , while a 10% decrease in that reactance. from 0.37 to 0.333 decreased the TTC to 200 MW Ž . 1.5% decrease .

Taking the worst case decrease, this means that a TRM of up to 3.4% may be justified to account for these data errors.

It may be possible to analytically predict this by examining the impact of 10% error on the analytical expression for the real-power distribution factors 11 .<sup>w</sup> <sup>x</sup> Or, to formulate the sensitivities of the distribution factors to small changes in line impedance. When the reactance of line 2–1 was increased by 10%, the power distribution factors changed from 0.41 to 0.387 Ž . Ž . 5% decrease and from 0.59 to 0.613 4% increase . This 4% increase in the 3–1 distribution factor would have predicted a TTC of 212 MW 130Ž . <sup>r</sup>0.613 rather than the 220 MW 130Ž . <sup>r</sup>0.59 which was originally predicted by the original line reactance, giving a 3.6% decrease. This is very close to the 3.4% reduction in TTC actually observed with a 10% increase in the line 2–1 reactance. This implies that it may be useful to further investigate analytical sensitivities of distribution factors to small changes in reactances for the purpose of computing a TRM component to account for model error.

## 4.4. Reduction in line ratings

When the above TTC was computed using a 3% reduction in all line ratings, the TTC was found to be 197 MW 3.0% decrease . This implies that there isŽ . a very close correlation between reduction of line ratings and reduction of TTC. This heuristic approach needs to be investigated further to establish a stronger theoretical basis for use as a TRM component.

## 5. Summary and conclusions

The computation of TTC and TRM presents a major challenge for power system engineers. While the NERC definitions and methods for determination provide considerable guidance for these calculations, there are still many major issues associated with their practical implementation. One of the main issues is related to the question of what to study. The concept of Available Transfer Capability requires the determination of what is available from a particular condition. If the exact condition were known in advance and a specific transaction was in question, the burden would be significantly less than that encountered in the attempt to predict what will be available at a future time. This paper has presented several of the issues associated with these computations and offered possible concepts for dealing with the challenges of the ATC calculation.

## Acknowledgements

The authors thank Ian Dobson, Hsiao-Dong Chiang, Ray Klump and David Takach for comments provided in the preparation of this paper. This work was supported in part by funds from National Science Foundation Grant NSF EEC 96-15792, the

University of Illinois Power Affiliates Program, the Grainger endowments to the University of Illinois, Power Engineering Research Center PSERC sub-Ž . contracts from Cornell University, and The Fulbright Scholarship Board.

## References

<sup>w</sup> <sup>x</sup> 1 S. Ahmed-Zaid, P.W. Sauer, Optimal system loadability, Proc. 1981 Midwest Power Symposium, University of Illinois at Urbana-Champaign, Urbana, IL, Sec. 3.1, 15–16 October 1981 , pp. 1–10.Ž .

<sup>w</sup> <sup>x</sup> 2 P.M. Andersen, A. Bose, A probabilistic approach to power system stability analysis, IEEE Transactions on Power Apparatus and Systems August 1983 2430–2439.Ž .

<sup>w</sup> <sup>x</sup> 3 H.D. Chiang, The BCU method for direct stability analysis of electric power systems: theory and applications, IMA Series, Vol. 64, Systems and Control Theory for Power Systems, Springer-Verlag 1995 , pp. 39–94. Ž .

<sup>w</sup> <sup>x</sup> 4 I. Dobson, L. Lu, Computing an optimum direction in control space to avoid saddle node bifurcation and voltage collapse in electric power systems, IEEE Transactions on Automatic Control 37 10 1992 1616–1620.Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 R.D. Dunlop, R. Gutman, P.P. Marchenko, Analytical development of loadability characteristics for EHV and UHV transmission lines, IEEE Transactions on Power Apparatus and Systems PAS 98 2 1979 606–617.Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 L.L. Garver, P.R. Van Horne, K.A. Wirgau, Load supplying capability of generation-transmission networks, IEEE Transactions on Power Apparatus and Systems PAS 98 3 1979Ž . Ž . 957–962.

<sup>w</sup> <sup>x</sup>7 G.T. Heydt, B.M. Katz, A stochastic model in simultaneous interchange capacity calculations, IEEE Transactions on Power Apparatus and Systems PAS 94 2 1975 350–359.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 T.W. Kay, P.W. Sauer, R.D. Shultz, R.A. Smith, EHV and UHV loadability dependence on VAR supply capability, IEEE Transactions on Power Apparatus and Systems PAS 101 9 1982 3568–3575.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 G.L. Landgren, S.W. Anderson, Simultaneous power interchange capability analysis, IEEE Transactions on Power Apparatus and Systems PAS 92 6 1973 1973–1986.Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 G.L. Landgren, H.L. Terhune, R.K. Angel, Transmission interchange capability-analysis by computer, IEEE Transactions on Power Apparatus and Systems PAS 91 6 1972Ž . Ž . 2405–2414.

<sup>w</sup> <sup>x</sup> 11 P.W. Sauer, On the formulation of power distribution factors for linear load flow methods, IEEE Transactions on Power Apparatus and Systems PAS 100 2 1981 764–770.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 P.W. Sauer, Technical challenges of computing available transfer capability ATC in electric power systems, Proceed-Ž . ings of the Thirtieth Annual 1997 Hawaii InternationalŽ . Conference on System Sciences, Vol. V, Maui, HI, 7–10 January 1997 , pp. 589–593. Ž .

<sup>w</sup> <sup>x</sup> 13 P.W. Sauer, Alternatives for calculating transmission reliability margin TRM in available transfer capability ATC , Ž . Ž . Proceedings of the Thirty-First Annual 1998 Hawaii Inter-Ž . national Conference on System Sciences, Vol. III, Kona, HI, 6–9 January 1998 , p. 89.Ž .

14 P.W. Sauer, K.D. Demaree, M.A. Pai, Stability limited load supply and interchange capability, IEEE Transactions on Power Apparatus and Systems PAS 102 11 1983 3637–Ž . Ž . 3643.

<sup>w</sup> <sup>x</sup> 15 P.W. Sauer, R.J. Evans Jr., M.A. Pai, Maximum unconstrained loadability of power systems, Proceedings 1990 IEEE International Symposium on Circuits and Systems, 90 CH 2868-8, New Orleans, LA, 1–3 May 1990 , pp. 1818–Ž . 1821.

<sup>w</sup> <sup>x</sup>16 P.W. Sauer, B.C. Lesieutre, M.A. Pai, Maximum loadability and voltage stability in power systems, International Journal of Electrical Power and Energy Systems 15 3 1993Ž . Ž . 145–154.

<sup>w</sup> <sup>x</sup> 17 H.P. St. Clair, Practical Concepts in Capability and Performance of Transmission Lines, AIEE Transactions 72 1953Ž . 1152–1157, Part III.

<sup>w</sup> <sup>x</sup> 18 B. Stott, J.L. Marinho, Linear programming for power system network security applications, IEEE Transactions on Power Apparatus and Systems PAS 98 3 1979 837–848.Ž . Ž .

<sup>w</sup> <sup>x</sup> 19 Transmission Transfer Capability Task Force, Transmission Transfer Capability, North American Electric Reliability Council, Princeton, NJ May 1995 .Ž .

<sup>w</sup> <sup>x</sup> 20 Transmission Transfer Capability Task Force, Available Transfer Capability Definitions and Determination, North American Electric Reliability Council, Princeton, NJ JuneŽ 1996 ..

<sup>w</sup> <sup>x</sup> 21 Union Electric, Simultaneous Transfer Capability: Direction for Software Development, EPRI Report EL-7351, Project 3140-1, Electric Power Research Institute, Palo Alto, CA Ž . August 1991 .

Peter W. Sauer obtained his Bachelor of Science degree in Electrical Engineering from the University of Missouri at Rolla in 1969, the Master of Science and PhD degrees in Electrical Engineering from Purdue University in 1974 and 1977, respectively. From 1969 to 1973, he was the electrical engineer on a design assistance team for the Tactical Air Command at Langley Air Force Base, Virginia, working on design and construction of airfield lighting and electrical distribution systems. He has been on the faculty at Illinois since 1977 where he teaches courses and directs research on power systems and electric machines. His main interests are in modeling and simulation of power system dynamics with applications to steady-state and transient stability analysis. From August 1991 to August 1992 he served as the Program Director for Power Systems in the Electrical and Communication Systems Division of the National Science Foundation in Washington DC. He is the Chairman of the IEEE Power Engineering Society PES Working Group on Dynamic Security Assessment, Ž . and Chairman of the IEEE Central Illinois Chapter of PES. He is a registered Professional Engineer in Virginia and Illinois and a Fellow of the IEEE.

Santiago Grijalva was born in Quito, Ecuador in November 1970. He received the Engineer Degree from the National Polytechnic University—Ecuador in 1994, and the MS Diploma from the Army Polytechnic University—Ecuador in 1997, in Electrical Engineering and Information Systems, respectively. Since 1995 he worked as EMS Engineer and then as Head of the Software Department in the Ecuadorian National Center of Energy Control, on maintenance and development of real-time SCADA-EMS systems. By means of a Fulbright Fellowship, he is currently a Graduate Student and a Research Assistant at the University of Illinois at Urbana-Champaign. His interests are concentrated in power system control and operation, real-time power applications, and information systems.
