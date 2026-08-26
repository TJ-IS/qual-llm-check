---
otero_id: 16847
otero_key: "NCD927BS"
title: "A decision support system for the planning of the workload on a grain terminal"
authors: "W.P.A. van der Heyden; J.A. Ottjes"
year: "1985"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(85)90169-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Decision Support System for the Planning of the Workload on a Grain Terminal

W.P.A. van der HEYDEN \* and J.A. OTTJES \*\* \* Delft University of Technology, Department of Mathematics and Informatics, Delft, The Netherlands, and \*\* Delft University of Technology, Department of Mechanical Engineering, Delft, The Netherlands

Ships, loaded with agricultural products, are handled by GEM at three different terminals in the port of Rotterdam. Each terminal consists of several berths and has both floating equipment and shore equipment. This paper describes the terminal system, the planning process and a menu driven computer planning model of the system. The planning model is split up into a first phase, in which berths are allocated, and a second phase, in which unloading equipment is assigned. The user of the model has the opportunity to manipulate several penalties and assign preferences to berths.

Keywords: Decision support system; Grain terminal;

![](/api/attachments/NCD927BS/fulltext/images/0559d366815cc91caa32accbe349ff7bb8f55b7013099c1ea356e8262dca334d.jpg)

![](/api/attachments/NCD927BS/fulltext/images/b79047fc608f371967a260ee3cd056c1ad83e2f222fedb2df19f5afe9b71c79d.jpg)

W.P.A. van der Heyden graduated in 1970 at the Technological University of Delft in Mathematics (specialization, Operations Research); until 1984 Senior Staff member of the Department of Mathematics and Informatics of the Technological University Delft; at present, Senior Staff Member Department Industrial Organisation and Management, Department of Mechanical Engineering at the same university.

J.A. Ottjes Graduated 1970 at the Technological University of Delft in Physics; at present Senior Staff member Section for Transport Engineering of the Department of Mechanical Engineering of the Technological University Delft.

## 1. Introduction

The Graan Elevator Maatschappij (GEM) is a large stevedoring company situated in the port of Rotterdam. Some 1000 sea-going vessels, varying from dry cargo ships to bulkcarriers up to 200000 ton DWT are handled annually. The cargo of these ships consists of agricultural products destined for the West-European hinterland, Great Britain and the East-European countries.

Transhipment involves some 45 000 river vessels and 1500 coasters which are loaded either directly from the supplying sea-going or indirectly via interim storage. For this purpose some 125 000 tons storage capacity is available.

Terminals equipped in the main with pneumatic elevators have been established at three different locations in the port of Rotterdam. Part of the equipment is situated on shore while in addition some 20 floating pneumatic elevators are available. The unloading capacity of the elevators at each location varies and amounts to 1000 ton/hour per elevator. The total effective capacity of the GEM is estimated to be 27 to 28 million ton/year.

## 2. Planning

Each ship is scheduled according to a plan set up by the central planning section in close cooperation with the local planning authorities at each location. For service purposes the GEM publishes a weekly schedule in which for each ship which is expected to arrive within ten days, the planned location, berth and expected time of departure is given. These data are the result of a careful planning process involving a large number of parameters of the system. Two planning-levels are to be considered:

\- Location and berth allocation,

\- Equipment allocation on the locations.

In order to obtain realistic data on the first level planning, it appears to be necessary to carry out the equipment planning in some detail too.

This gives an initial level-2 planning. The daily 'floor' planning is carried out at the locations, the basis of this being the initial level-2 planning. In fact the planning has the character of a continuous process. Every time an unexpected change takes place as a result of bad weather, incorrect cargo specification, extra arrivals, etc., the planning or a part of it has to be reconsidered. Especially in busy periods, this is a time-consuming practice and the consequent lack of time prevents the planner from taking into account – possibly better – alternative schedules.

Use of a computer may improve planning results, because the bulk of the planning routine can be performed in a relative short time, giving the planner the opportunity to use his skill and experience to compare several alternative plans. For this purpose a computer-aided planning system has been developed at the Delft University of Technology. This system is in use by the GEM and has been fully accepted and is integrated in the planning section of the company.

The most important aspects of this planning-system will be elucidated in the following sections.

## 3. Description of the System

Two important elements are to be considered in the system:

\- the ships;

\- the location with equipment.

A location can be considered to be composed of a number of single berths and a common set of elevators which are used for these berths. Both ship and berths possess characteristic features. The planning has to match these features in such a way that certain objectives are achieved. Such an objective might be minimal demurrage cost. In general, however, a number of interests are brought to bear in the defining of the objective.

The main characteristic features of ships and berths are:

SHIP

\- Expected Time of Arrival (ETA);

\- Cargo information;

\- Ship's workload per location;

\- Type of the ship;

\- DWT;

\- Permitted berths;

\- Maximum number of elevators;

\- Expected Time of Depart (ETD).

## BERTH

\- Equipment information;

\- Availability of equipment;

\- Maximum permitted length;

\- Maximum permitted draught;

\- Maximum permitted DWT.

The ETA and the cargo information are generally known some ten days before the actual arrival of the ship. The workload is calculated from the cargo information, particularly from the plan of stowage. For the same ship the workload may differ according to the location, because each location may have its own standard elevator capacity. Furthermore the ship's workload depends on the type of the ship, the type of cargo and the number of separations between the layers of different materials in the same hold (see Fig. 1).

For each location a scheme must be available giving the effective unloading capacity of the elevators as a function of the type of cargo and type of vessel.

Type, length draught and DWT determine in the first instance whether or not a ship may be handled on a certain berth. However, the planner may have his own reasons for preferring or excluding certain berths. Therefore, he must be free to further reduce the set of permitted berths.

Each ship has a maximum number of elevators. This is an arbitrary number, which may be set by the planner. It depends, for instance, on physical restrictions like the number of holds and whether or not there are barges aside to be loaded directly.

The availability of equipment depends on the availability of elevator crews and also upon delays resulting from stoppages for maintenance and equipment failure. For each planning period an ‘availability scheme’ must be set up in which the crew’s work schedules, weekends, public holidays, etc. are taken into account. An example is shown in Fig. 2.

A very important variable is the ETD. In most cases a contractual ETD will exist, to be considered as deadline. However, in general it will be profitable for a client to have his ETD as early as possible. On the other hand, it may happen that, for commercial reasons a client may wish the unloading to be delayed for some time. The planner has to take account of this. The planner must further ensure that different clients, who may competitors, are treated fairly. In order to cope with these problems, the planner must have the possibility to manipulate the ETD data and to survey the consequences of this in his planning. A computer aided planning system is pre-eminently suitable to meet to these requirements.

<table><tr><td colspan="4">mean capacity at &#x27;EUROPOORT VAST&#x27; (tons/shift)</td></tr><tr><td>kind</td><td>type 1</td><td>type 2</td><td>type 3</td></tr><tr><td>grains</td><td>1150</td><td>3750</td><td>1150</td></tr><tr><td>good flowing pellets</td><td>750</td><td>3000</td><td>750</td></tr><tr><td>bad flowing pellets</td><td>700</td><td>1750</td><td>700</td></tr><tr><td>tapioca</td><td>650</td><td>1450</td><td>650</td></tr><tr><td>good flowing flour</td><td>700</td><td>2250</td><td>700</td></tr><tr><td>bad flowing flour</td><td>600</td><td>1500</td><td>600</td></tr><tr><td>separations * 10</td><td>10</td><td>10</td><td>10</td></tr></table>

Fig. 1. Effective unloading capacity of a location for different types of vessel and cargo.

<table><tr><td colspan="4">availability elevators at &#x27;EUROPOORT VAST&#x27;</td></tr><tr><td>day/shift</td><td>00-08</td><td>08-16</td><td>16-24</td></tr><tr><td>Monday</td><td>0</td><td>4</td><td>4</td></tr><tr><td>Tuesday</td><td>4</td><td>4</td><td>4</td></tr><tr><td>Wednesday</td><td>4</td><td>4</td><td>4</td></tr><tr><td>Thursday</td><td>4</td><td>4</td><td>4</td></tr><tr><td>Friday</td><td>4</td><td>4</td><td>4</td></tr><tr><td>Saturday</td><td>3</td><td>2</td><td>0</td></tr><tr><td>Sunday</td><td>0</td><td>0</td><td>0</td></tr></table>

Fig. 2. Sample availability scheme.

## 4. Solution of the Planning Problem

The planning problem can be formulated as a Machine Scheduling Problem with scarce resources. The translation from the GEM problem to a Machine Scheduling Problem is as follows:

ships → jobs;

berths → machines;

equipment → resources.

A two phase method is used to find a solution of the problem:

Phase 1: find a good allocation of the jobs to the machines;

Phase 2: find a good allocation of the resources to the jobs.

Prior to the first phase of the methods, it is necessary to make an estimate of the job duration. This is the number of lay-days of the ships on the various berths. It is calculated as the quotient of the workload and the maximum of items of equipment permitted, multiplied by a factor (mostly 2). This method gives satisfactory results in practice. A detailed description of the algorithm used in given in the appendix.

## 5. Use of the System

The system is built for use by people who are not experienced computer users. Therefore the system is interactive, user-friendly and menu-driven. It runs on an IBM mainframe and the users have a display unit and a printer at their disposal.

The method for the solution of the planning problem gives a good approximation of the optimum solution with the objective minimal sum of weighted delay and tardiness. The allocation of equipment can give rise to a situation where a ship 'lays over the weekend' while only a few units of workload remain to be processed in the next week. It is also possible that the plan assigns a berth to a certain vessel but that for some specific reason the planner does not wish this to be done.

```txt
GRAAN ELEVATOR MAATSCHAPPY BV
DATE 04/10/01 TIME 11.53
RELEASE 2
SELECT APPLICATION --->
1 ADD,DELETE OR CHANGE SHIP INFORMATION
2 CHANGE DEFAULT VALUES
3 PERFORMANCE OF A PLANNING
4 CHANGE ETA OR ETD AND PLANNINGRUN
5 UPDATING OF DAILY PROGRESS
6 CHANGE ACTUAL AVAILIBILITY ON LOCATIONS
7 BACKUP TO BACKGROUND MEMORY
8 BACKUP FROM BACKGROUND MEMORY
9 PRINT FUNCTIONS
USE PFIS TO QUIT
```  
Fig. 3. Main menu.

The planner has some means available for adjusting these situations. For the first situation he can manipulate the penalties on delay and tardiness to steer a ship into a more favourable position. The effect will be that decreasing the delay or tardiness of one ship will increase the delay and/or tardiness of other ships. By excluding the assigned berth in the second situation he can study the effect of this action.

The method normally used is as follows:

\- Run a planning with no penalties and all berths allowed;

\- Study the results;

\- If there are ships in an unfavourable position try to improve this planning by manipulation of penalties and excluding berths;

\- Repeat until the planning is satisfactory.

As seen from this description, the computer system is a support system for the planner. In all cases the planner retains his responsibility.

## 6. Implementation

The prototype of the system was developed at the University of Delft according to the specifications given by the company. This prototype was transferred to the company's computer. After installation, two months were required to complete the system. This was done in close cooperation with the users. In this process the planners learned to use the system. Some new features were added, errors were removed and securities for misuse were built in. After two months the system was fully operational and the planners could use it without problems. With this system it was also possible by means of simulation to study the effect of several unloading strategies.

## 7. Future Developments

In the near future a modified version of the planning system will be build. In this version there will be direct links with the administration system of the company. This will make it possible to base the planning also on cost and/or profits for both company and client. In the new system it will be also possible to use temporary berths and equipment.

## APPENDIX: Detailed description of the algorithm.

## Phase 1: Allocation of the jobs

We define:

$l(i,j)$ = the amount of processing time required by ship j on verth i;

$r(j) = \text{the point in time at which ship } j \text{ is available for unloading;}$

$d(j) =$ the point in time at which unloading of ship $j$ is due to be completed;

$s(j) =$ the point in time at which ship $j$ is planned to start unloading;

$c(j) = \text{the point in time at which unloading of ship } j \text{ is planned to be completed;}$

$x(j) =$ delay in start of ship $j$ , $x(j) = \max (0, s(j) - r(j))$ ;

$y(j) = \text{tardiness of ship } j, y(j) = \max (0, c(j) - d(j)).$

The allocation of the ships to the berths is done by a method based on simulation.

Let $T(i)$ be the point in time at which the first berth becomes available. For each ship $j$ with $t(i, j) > 0$ can be calculated the values $x(j)$ and $y(j)$ . These two values are weighted by penalty factors $ws(j)$ and $we(j)$ and the weight $w(j) = ws(j) * x(j) + we(j) * y(i)$ is calculated.

Ship m, with maximum weight, is assigned to berth i. The moment at which berth i is again available for processing is given by $T'(k) = \max(T(i) + t(i, j), r(j) + t(i, j))$ .

The algorithm starts with all $T(i)=0$ and proceeds until all ships are scheduled. The scheduling is characterised by $W = \sum ws(j) * x(j) + we(j) * y(j)$ ; W is the weighted sum of delay and tardiness of all ships. At each decision moment $T(i)$ the best choice is made, but nevertheless the final result is generally not the best. Therefore a simple interchanging routine is used in which the effect of interchanging two ships in time and place is studied. If the result of the interchange of two ships gives a better solution this interchange is applied. It is evident that the performance of this algorithm depends on the quality of the estimate of the unloading times of the ships.

<table><tr><td>location</td><td>elevators</td><td>to be used on berth</td></tr><tr><td>1</td><td>4 fixed5 floating</td><td>1,21,2 and 3</td></tr><tr><td>2</td><td>5 fixed5 floating</td><td>4,54,5 and 6</td></tr><tr><td>3</td><td>2 fixed</td><td>7</td></tr></table>

Fig. 4.

## Phase 2: Assignment of equipment

The result of the Phase 1 is an allocation of ships to berths. The next step is the assignment of equipment to the ships. For each location fixed floating equipment is available, as given in Fig. 4.

The equipment is assigned to a ship for fixed periods of time called shifts (normally 8 hours). The distribution in a shift is carried out according to certain rules. These rules applied to the berths in location 1 are as follows:

Let $wI(i), wI(j), wI(k) = \text{total workload of the ships};$

let $u(i), u(j), u(k)$ = be part of the workload already completed;
let $p(i), p(j), p(k)$ = planned number of lay-days;
let $s(i), s(j), s(k)$ = already used number of time-units

then the weight of the ships is calculated by:

$$
w ^ {\prime} (l) = \frac {s (l)}{p (l)} / \frac {u (l)}{W 1 (l)} * f (l) * v (l) l = i, j, k
$$

with $f(1)$ penalty for exceeding due date ( $f(1)=1$ if t < due date, else $f(1)>1$ ) and $v(1)$ appraisal factor of the ship.

The unloading of a ship is on schedule if $w'(1) = 1$ . The weights $w'(i)$ , $w'(j)$ and $w'(k)$ are normalized to $w(i)$ , $w(j)$ and $w(k)$ . The number of items of equipment to be used is calculated by:

$$
\begin{array}{l} n (i) = w (i) * (4 + 5), n (j) = w (j) * (4 + 5) \\ \text { and } n (k) = w. k) * 5. \end{array}
$$

These numbers are balanced and corrected for fixed and floating equipment. The same method is used for the other locations.
