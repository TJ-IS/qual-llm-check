---
otero_id: 17148
otero_key: "3E6H3MPG"
title: "Decision support by rapid simulation using simulation nets"
authors: "Aimo A. Törn"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90025-m"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision Support by Rapid Simulation Using Simulation Nets

Aimo A. TÖRN

Åbo Akademi, Department of Computer Science, SF-20520 Åbo, Finland

The working of a tool, Simulation Nets, for designing and executing models for simulation of systems is presented. The tool is an extension of the theoretically attractive Petri Nets, whose suitability in general simulation modeling has largely been overlooked in the simulation community. Simulation Nets helps in obtaining a correct simulation model because of their good graphical properties, their strength in describing concurrent processes, and because of the possibility in proving correctness for some parts of the model by applying the well known reachability tree technique. The resulting graphical model consists of a number of submodels. The submodels are exact enough to permit simulation experiments to be performed without the need of programming. This permits easy incremental validation of the model, i.e., validation of the submodels and a hierarchy of coupled submodels. Simulation nets thus facilitates rapid modeling and experimentation and thus supports the decision maker in obtaining the data needed for him to make his decision. Experiences with a working prototype are presented.

Keywords: Simulation, Simulator, Modeling, Petri Net, Validation.

## 1. Introduction

Simulation may be regarded as a general-purpose method of obtaining knowledge about the working of a system; i.e., in the absence of applicable mathematical formulae or equations, the working of important parts of the system under consideration may be mimicked, and values of the entities of the system can be obtained by collecting data during a simulation run. Because simulation models are often complicated and because their use requires extensive calculations, they are normally realized as computer programs.

When designing computer programs, some design tools (such as program flowcharts) must be used. One drawback of most existing programming tools for simulation is the lack of a convenient technique for modeling concurrent interacting processes. Because concurrent interacting processes are essential features of simulation models and because much of the complexity of such models arises from the existence of those concurrent processes, the ordinary design tools (such as program flowcharts, which describe a single process) are not adequate for use in designing simulation programs.

The course taken to overcome this difficulty has been to provide special design tools with particular simulation languages. GPSS (see for instance [Schriber 1974]) is one example of a language with its own flowcharting technique, and SLAM [Pritsker and Pedgen 1979] with its network graphs is another. In some activity-based simulation languages, i.e., SIMON [Hills 1976] and GSP [Tocher and Owen 1969], so-called activity diagrams are used. Similar activity diagrams are also used by Birtwistle for outlining the structure of the program prior to coding in DEMOS [Birtwistle 1979]. Because of the absence of a generally applicable formal tool, ad hoc schemes if any for describing the interaction of concurrent processes have been used.

As a remedy for this lack of a generally applicable tool for simulation modeling Simulation Nets [Törn 1981] was suggested. Simulation Nets are based on the well known Petri Nets which were designed to describe asynchronous concurrent processes. Simulation Nets are extensions of Petri Nets permitting general simulation modeling. The extensions include inhibitor arcs, test arcs, time, queues and entities, i.e., coloured tokens. The hierarchical modeling capabilities by refinement of transitions and places are demonstrated and the advantage of hierarchical manual validation is stressed. It is also demonstrated how the validated simulation graph could be turned into a correct Simula program.

In [Törn 1985] an automated tool for processing a simulation graph was presented. Using the tool it is possible to execute Simulation Nets represented as a single net with the extensions inhibitor arcs and time distributions for the delay in firing transitions. The result of the simulation must be deduced from the standard output automatically produced and containing statistical data for places and transitions. A trace facility is provided, which makes it possible to get detailed information on the steps in the execution. A non-Petri Net modeling technique for the first steps in the model construction is introduced.

In [Törn 1986] the use of Petri Net analysis for aiding the validation of simulation graphs is suggested. By evaluating the reachability tree, questions regarding liveness and boundedness may be answered for suitable parts of the design.

[Törn 1988] is a brief description of Simulation Nets.

In this paper the detailed working of a tool, SimNet for entering, editing, refining, tracing and executing simulation nets is presented by modeling a small simulation problem using Simulation Nets and by implementing the resulting design using this tool. SimNet permits the model to be composed of submodels that may be separately executed and tested before coupling them together to form the total model. The use of the reachability tree and the printout from the automatic statistics collector in validating the design is also demonstrated.

## 1.1. Simulation Nets

For simulation purposes the Petri Net constructs, places and transitions, will be interpreted as conditions and events (activities, processes). An event can occur if certain preconditions are fulfilled and, after the occurrence, certain postconditions hold. Tokens may be interpreted as entities traversing the net.

Simulation Nets are extensions to Petri Nets including the following: An entity belongs to a class of system entities such as customers, cars and normally have attributes that make the entities into individuals. A queue of entities is noted as a place with a horizontal bar across the circle. The time concept is introduced by assigning time distributions to the transitions. The concept is an extension of the Timed Petri Nets of Ramchandani [Ramchandani 1974]. When a transition t is enabled it may fire. Firing means removing the required number of tokens from each of t's input places. These tokens remain in the transition t for the "firing time", and then the firing terminates by adding the required number of tokens to each of t's output places. Each of the firings is initiated in the same instant of time in which it is enabled. If a transition is enabled while it fires, a new independent firing can be initiated. If a net contains conflicts, and there are several different enable functions for the same marking, an arbitrary choice will be made. If the order is important, the conflict should be resolved by the modeller (for instance by introducing inhibitor arcs).

The high-level nets used in the first design steps are not Simulation Nets but is a net showing the relation between a choice of conceptually important high-level activities and places. The use is illustrated in section 2.1.

## 1.2. Validating Simulation Nets

It is hoped that validation of Simulation Nets could be enhanced by using Petri Net analysis techniques. One possible approach is to use the ordinary reachability tree technique augmented by time inscriptions, i.e., for each marking the corresponding time function is also given. At least for some nets this technique is powerful enough to support correctness proofs, for an example see section 2.2.

Some data important for the validation can be collected during the execution of the net. Some questions (negative) regarding liveness and boundedness may be answered in this way. This will be demonstrated in the treatment of the sample problem.

## 1.3. Implementation

A tool for entering, editing, refining and executing a restricted class of simulation nets is working. The tool makes it possible to couple nets, and subnets may therefore be analyzed and tested before being incorporated into a larger model. Several “languages” for the interface with the user have been presented [Nelson et al 1985; Cumani 1985; Törn 1986], our approach will be demonstrated in section 2.3. An important question to be solved is how to enter the procedures to be evaluated when firing transitions. Nelson solves this problem by producing a skeleton simulation program that is then completed by the user. This was one of the approaches suggested in [Törn 1986]. The other possibility is to enter the procedures together with the simulation nets. In its present state our tool cannot read and evaluate user provided procedures.

## 2. An Illustrative Example

The example used to demonstrate the use of simulation nets in modeling simulation designs is the following [O'Donavan 1979]:

A ship can be prepared for departure from a port A every $15 \pm 10$ hours. However, if one ship is unable to sail, it delays the departure of the next. A ship will not sail unless there is a high tide. During the 12 hours between high tide and low tide, ships can set sail, but during the next 12 hours between low tide and high tide, they may not.

![](/api/attachments/3E6H3MPG/fulltext/images/dd246888cf2f645669dac2c6f9d06eb24964dc83c6d72af9e24bf1eae382614d.jpg)  
Fig. 1. Crude System Model.

![](/api/attachments/3E6H3MPG/fulltext/images/7e55c7a25d9bcd87c3ec842a0d33a575cbf2316c52c76944c3a38fc5791a4f7f.jpg)  
Fig. 2. Tide Model.

When a ship does set sail, it travels $6 \pm 2$ hours before selecting a route. It prefers to go to port B, if there is a free berth there at the time (B has 5 berths), and the journey to this destination takes $40 \pm 10$ hours. Unloading at port B takes $65 \pm 30$ hours. Otherwise, the ships go to port C.

## 2.1. Simulation Net for the Sample Problem

In fig. 1–fig 5 the development of a model for the sample problem is illustrated. In fig. 1 the corresponding crude design, i.e. the high-level net is shown. The building blocks of this net are detailed and presented as simulation nets in figs. 2–5. The nets with their inscriptions should be easy to understand and we do not further comment on them.

![](/api/attachments/3E6H3MPG/fulltext/images/e3d97f75c1c21ab7d7f0c4a5a162223945ead775f88cae9da6ef8ba540dc7b2a.jpg)  
Fig. 3. Departures Model.

![](/api/attachments/3E6H3MPG/fulltext/images/a2506fbd8e3080f6b79d505dad0bdcf35322ea96c4e42324f694a6708e0f4a18.jpg)  
Fig. 4. Ship Movement Model.

## 2.2. An Analysis Tool

In fig. 6 the use of a generalized reachability tree i shown. The changing content of the three places Low-tide, High-tide-starts and Low-tide-starts in the model Tide-management can be traced through firings of transitions. Also given is the duration of a given state. We see that the tree implies a 24-hour cyclic behaviour with 12-hour duration of High-tide (content 0 for Low-tide) followed by a 12-hour duration of Low-tide (content 1 for Low-tide). This is obviously exactly the intended behaviour of the Tide-model. By the aid of the extended reachability three we have thus been able to prove the correct behaviour of the Tide-model.

![](/api/attachments/3E6H3MPG/fulltext/images/28b6a875b31328591ede4d5bfee7303a3ff85e2acbbde748fbde05257ab148c8.jpg)  
Fig. 5. Model of Ship-to-B from Fig. 4.

![](/api/attachments/3E6H3MPG/fulltext/images/b2610eb4946dce556711125527e64f5b4b608e9072148de7879629fe415a9b14.jpg)  
Fig. 6. Reachability Tree for Tide-Management.

## 2.3. SimNet, a Tool for Validation

In figs. 7–9 the use of the a tool, SimNet, for validating the design is demonstrated using the sample problem modeled in section 2.1. In fig. 7 the functions available are listed.

In fig. 8–9 validation of the net Tide is shown. First the prompted input of Tide is presented. Then the net is initialized i.e., initial tokens are placed in Low-tide and High-tide-starts. After that it is shown how the net Tide is prepared for a trace run, and then the printout from such a run is given. From this printout it can be seen that the

![](/api/attachments/3E6H3MPG/fulltext/images/e3c621ea520fa9eb70ee40d431c91764e58eeeec4ab22b3138ff80461dba6fe4.jpg)  
Fig. 7. Functions of SimNet.

```yaml
=>create
    Netname : Tide
Trans & Func : HighToLow cnst 12
Inplaces : LowTide 1
HighTideStarts 1
Outplaces : LowTide 1
LowTideStarts 1
Trans & Func : LowToHigh cnst 12
Inplaces : LowTideStarts 1
Outplaces : HighTideStarts 1
Trans & Func :
=>init
    Give netname : Tide
    Give place : LowTide 1
    Give place : HighTideStarts
    Give initial occupancy : 1
    Give place :
    Give netname :
=>set
    Statistics for : Tide
    Statistics set for TIDE
    Statistics for :
=>trace
    Give netname : Tide
    Trace set for TIDE
    Give netname :
    Start trace at time : 0
    Time to trace : 60
=>run
    Give time to run : 2400
---- TRACE ----
0.00 HIGHTOLOW starts (ends: 12.00)
12.00 HIGHTOLOW finished (used: 12.00)
LOWTOHIGH starts (ends: 24.00)
24.00 LOWTOHIGH finished (used: 12.00)
HIGHTOLOW starts (ends: 36.00)
36.00 HIGHTOLOW finished (used: 12.00)
LOWTOHIGH starts (ends: 48.00)
48.00 LOWTOHIGH finished (used: 12.00)
HIGHTOLOW starts (ends: 60.00)
60.00 HIGHTOLOW finished (used: 12.00)
LOWTOHIGH starts (ends: 72.00)
```  
Fig. 8. Input of and Trace with Tide.

working of the net Tide is an alternation between firings of the transitions High-to-low Low-to-high with a 12 h duration for each. The printout of the automatically collected statistics is then given in fig. 9. From the first part, transition statistics, it can be seen that both High-to-low and Low-to-high have continued to fire up till the run time limit 2400, that the time between firings is 24 h, and that time between the start and the completion of a firing action is 12 h. From the second part, place statistics it can be seen that the entity mean time for Low-tide is 12 h, which means that the duration of low tide is 12 h. These facts are obviously sufficient for Tide to behave correctly. We can therefore say that we have validated Tide experimentally. Finally the net Tide is stored on disk.

<table><tr><td>TRAN SITION</td><td colspan="2">FIRINGS COMPL GOING</td><td>LAST FIRED</td><td>TIME MEAN</td><td>BETWEEN MIN</td><td>FIRINGS MAX</td><td></td></tr><tr><td>HIGHTOLOW</td><td>100</td><td>0</td><td>2376.00</td><td>24.00</td><td>24.00</td><td>24.00</td><td></td></tr><tr><td>LOWTOHIGH</td><td>100</td><td>0</td><td>2388.00</td><td>24.00</td><td>24.00</td><td>24.00</td><td></td></tr><tr><td colspan="8">FIRING TIME</td></tr><tr><td></td><td>MEAN</td><td>MIN</td><td>MAX</td><td></td><td></td><td></td><td></td></tr><tr><td>HIGHTOLOW</td><td>12.00</td><td>12.00</td><td>12.00</td><td></td><td></td><td></td><td></td></tr><tr><td>LOWTOHIGH</td><td>12.00</td><td>12.00</td><td>12.00</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="8">---- PLACE STATISTICS----</td></tr><tr><td colspan="8">For net TIDE</td></tr><tr><td rowspan="2">PLACE NAME</td><td rowspan="2">NO OF VISITS</td><td rowspan="2">LATEST CH</td><td rowspan="2">O</td><td colspan="4">----CONTENT----</td></tr><tr><td>INI FIN</td><td>MEAN</td><td>MIN</td><td>MAX %O</td></tr><tr><td>LOWTIDE</td><td>100</td><td>2388</td><td>2376</td><td>1</td><td>1</td><td>0.5</td><td>0 1 50.0</td></tr><tr><td>HIGHTIDESTARTS</td><td>100</td><td>2400</td><td>2376</td><td>1</td><td>1</td><td>0.0</td><td>0 1 100.0</td></tr><tr><td>LOWTIDESTARTS</td><td>100</td><td>2388</td><td>2388</td><td>0</td><td>0</td><td>0.0</td><td>0 1 100.0</td></tr><tr><td colspan="8">ENTITY AVERAGE MEANTIME UTIL.</td></tr><tr><td>LOWTIDE</td><td>12.00</td><td>50.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>HIGHTIDESTARTS</td><td>0.00</td><td>100.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>LOWTIDESTARTS</td><td>0.00</td><td>UDEF</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="8">=&gt;save Give filename for saving : fipo.tid</td></tr></table>

Fig. 9. Statistics from Run with Tide.

All the other models given in figs. 3–5 may be independently validated in the same way as Tide. In order to be able to validate the behaviour of aggregate models, the models must be coupled to form aggregates.

In fig. 10 all the separate models (see figs 2–5) are loaded and coupled together. Tide and Ship-movement should be coupled so that the place Low-tide is common to both. In the terminology of SimNet we expand the place Low-tide of the net Tide so that the place after the expansion will be the net Ship-movement. In the same way Departure-generation is coupled to Ship-movement. The aggregation is completed by expanding the transition Ship-to-B in the net Ship-movement to be the net Ship-to-B shown in fig. 5. It should be clear that the aggregated models may be validated in the same way as simple models (e.g. like Tide). The aggregated models may be stored and can therefore be used later without the need to repeat the coupling actions.

```txt
=>load
    Give infilename : fipo.tid
=>load
    Give infilename : fipo.mov
=>plexpand
    Net within to expand place : Tide
    Place name : LowTide
    Expanding net : Move
=>load
    Give infilename : fipo.gen
=>plexpand
    Net within to expand place : Gen
    Place name : ShipToLeave
    Expanding net : Move
=>load
    Give infilename : fipo.msu
=>trnexpand
    Expand transition : ShipToB
    Expanding net is : ShipToB
=>save
    Give filename for saving : fipo.all
Fig. 10. Coupling Submodels.
```

<table><tr><td colspan="10">=&gt;load</td></tr><tr><td colspan="10">Give infilename : fipo.all</td></tr><tr><td colspan="10">=&gt;set</td></tr><tr><td colspan="10">Statistics for : Move</td></tr><tr><td colspan="10">Statistics set for MOVE</td></tr><tr><td colspan="10">Statistics for : Gen</td></tr><tr><td colspan="10">Statistics set for GEM</td></tr><tr><td colspan="10">Statistics for :</td></tr><tr><td colspan="10">=&gt;run</td></tr><tr><td colspan="10">Give time to run : 10000</td></tr><tr><td colspan="10">=&gt;stat</td></tr><tr><td colspan="10">---- TRANSITION STATISTICS----</td></tr><tr><td colspan="10">--- --</td></tr><tr><td colspan="10">---- PLACE STATISTICS----</td></tr><tr><td colspan="10">For net MOVE</td></tr><tr><td rowspan="2">PLACE NAME</td><td colspan="3">NO OF LATEST</td><td colspan="6">----CONTENT----</td></tr><tr><td>VISITS</td><td>CH</td><td>O</td><td>INIT FINAL</td><td>MEAN</td><td>MIN</td><td>MAX</td><td>%O</td><td></td></tr><tr><td>LOWTIDE</td><td>417</td><td>9996</td><td>9984</td><td>1</td><td>1</td><td>0.5</td><td>0</td><td>1</td><td>50.1</td></tr><tr><td>SHIPTOLEAVE</td><td>551</td><td>9988</td><td>9988</td><td>0</td><td>0</td><td>0.2</td><td>0</td><td>1</td><td>82.2</td></tr><tr><td>SHIPTOSELECT</td><td>551</td><td>9993</td><td>9993</td><td>0</td><td>0</td><td>0.0</td><td>0</td><td>1</td><td>100.0</td></tr><tr><td>FREEBERTHS</td><td>401</td><td>9993</td><td>9972</td><td>5</td><td>2</td><td>0.8</td><td>0</td><td>5</td><td>42.8</td></tr><tr><td>SHIPTOC</td><td>147</td><td>9954</td><td>0</td><td>0</td><td>147</td><td>74.6</td><td>0</td><td>147</td><td>1.7</td></tr><tr><td>SHIPTOLEAVEB</td><td>401</td><td>9980</td><td>0</td><td>0</td><td>401</td><td>198.0</td><td>0</td><td>401</td><td>1.1</td></tr><tr><td></td><td colspan="3">ENTITY MEANTIME AVERAGE UTIL.</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>LOWTIDE</td><td>11.97</td><td>50.06</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SHIPTOLEAVE</td><td>3.13</td><td>UNDEF</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SHIPTOSELECT</td><td>0.00</td><td>UNDEF</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>FREEBERTHS</td><td>19.49</td><td>84.36</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SHIPTOC</td><td>5070.02</td><td>UNDEF</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SHIPTOLEAVEB</td><td>4936.80</td><td>UNDEF</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="10">----</td></tr><tr><td colspan="10">For net GEM</td></tr><tr><td rowspan="2">PLACE NAME</td><td colspan="3">NO OF LATEST</td><td colspan="6">----CONTENT----</td></tr><tr><td>VISITS</td><td>CH</td><td>O</td><td>INIT FINAL</td><td>MEAN</td><td>MIN</td><td>MAX</td><td>%O</td><td></td></tr><tr><td>GEMTOKEN</td><td>551</td><td>9988</td><td>9988</td><td>1</td><td>0</td><td>0.2</td><td>0</td><td>1</td><td>82.6</td></tr><tr><td>SHIPTOLEAVE</td><td>551</td><td>9988</td><td>9988</td><td>0</td><td>0</td><td>0.2</td><td>0</td><td>1</td><td>82.5</td></tr><tr><td></td><td colspan="3">ENTITY MEANTIME AVERAGE UTIL.</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GEMTOKEN</td><td>3.16</td><td>82.56</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SHIPTOLEAVE</td><td>3.16</td><td>UNDEF</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 11. Place Statistics of a Run with the Complete Model.

## 2.4. Experimenting

Fig. 11 describes one experiment made with the complete model. From the place statistics it can be seen that out of a total of 551 ships that sailed from port A (Shiptoselect, no of visits), 3 are at port B (see Freeberths, final content), 401 have visited port B (see Shiptoleave B, final content)

and 147 have sailed to port C (see ShiptoC, final content). The average utilization of the berths at port B is 84% (see Freeberths, average utilization). Also some other interesting facts may be found by reading the statistical data.

## 3. Conclusions

Simulation nets have proved easy to use in modeling simulation designs. This is because simulation nets allow a representation showing both overview and sufficient detail for correct modeling of interactions.

The model of a given system, consisting of a number of submodels, is easily implemented with the aid of a tool, SimNet, capable of reading the design and helping in independent validation of submodels and aggregates of submodels. Given the design, SiNet can automatically perform a simulation of the working of the model. As a result of the simulation, statistical information about the simulated system is automatically produced. Parameters of the system can easily be changed, allowing convenient optimization and experimentation.

## 4. References

[Birtwistle 1979] G.M. Birtwistle, Discrete Event Modeling on Simula, (Macmillan, London) 214 pp.

[Cumani 1985] A. Cumani, ESP - a package for the evaluation of Stochastic Petri Nets with phase-type distributed transition times, in [Marsan et al 1985] 144-151.

[Hills 1976] P.R. Hills, SIMON - a computer simulation language in ALGOL, in S.H. Holindall (ed.), Digital Simulation in Operations Research (American Elsevier, New York).

[Marsan et al 1985] M.A. Marsan, G. Balbo and K. Trivedi, (eds.), Proceedings of the International Workshop on Timed Petri Nets, Torino Italy July 1–3, 1985 (IEEE Computer Society Press, Silver Spring) 307 pp.

[Nelson et al 1985] R.A. Nelson, L.M. Haibt and P.B. Sheridan, Casting Petri nets into programs, IEEE Trans. on Software Engineering, Vol. SE-9, No 5, 590–602.

[O'Donovan 1979] T.M. O'Donovan, GPSS - Simulation made simple (Wiley, N.Y.) 127 pp.

[Pritsker and Pedgen 1979] A.A.B. Pritsker and C.D. Pedgen, Introduction to simulation and SLAM (Wiley, New York) 588 pp.

Ramchandani 1974] C. Ramchandani, Analysis of asynchronous concurrent systems by Petri nets, Project MAC TR-120 Massachusetts Institute of Technology (Cambridge, Massachusetts).

[Schriber 1974] T.J. Schriber, Simulation using GPSS (Wiley, New York) 533 pp.

[Tocher and Owen 1969] K.D. Tocher and D.C. Owen, The automatic programming of simulations, Proceedings Second International Conference on Operations Research, 50–68.

[Törn 1981] A.A. Törn, Simulation graphs: a general tool for modeling simulation designs, Simulation 37:6, 187–194.

[Törn 1985] A.A. Törn, Simulation nets, a simulation modeling and validation tool, Simulation 45:2, 71–75.

[Törn 1986] A.A. Törn, Simulation nets – an application of Petri nets to system simulation, In: Ruschizka, M. (ed.), Transactions on Scientific Computing–'85, Vol. 2., Computer Systems: Performance and Simulation (Elsevier) 213–218.

[Törn 1988] A.A. Törn, Simulation modeling formalism: Extended Petri net graphs, In: Singh M.G. (ed.), Encyclopedia of Systems and Control (Pergamon Press, Oxford) 4348–4350.
