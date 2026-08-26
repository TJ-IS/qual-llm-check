---
otero_id: 17644
otero_key: "WZUZSDBT"
title: "Applying the service level criterion in a location-allocation problem"
authors: "C.P. Pappis; N.I. Karacapilidis"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90067-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Applying the service level criterion in a location-allocation problem

C.P. Pappis

University of Piraeus, Piraeus, Greece

N.I. Karacapilidis

University of Patras, Rio Patras, Greece

A DSS to help solve the location-allocation problem applying service level criterion is presented in this paper. The decisive parameters considered are the maximum allowable distance between a customer and the respective supplying center and the total number of such centers. A case study of a Greek bottling company with computational results is also included.

Keywords: Location; allocation; service level; decision support system.

Costas P. Pappis is currently an Associate Professor of Production/Operations Management at the University of Piraeus, Greece. He holds a BS degree in Production Engineering from the Technical University of Athens, a Diploma in Management Studies from the Polytechnic of Central London and a Ph.D. in Engineering from the University of London. Prior to joining the University in 1993, he worked as an operations analyst, as an Engineer in the Technical Services of the National Bank of Greece, as Director of the Offsets Department of the Ministry of National Economy of Greece, and as an Associate Professor at the University of Patras. He has been President of the Hellenic OR Society and has published papers in IEEE Systems, Man and Cybernetics, European Journal of Operational Research, Fuzzy Sets and Systems and Engineering Cost and Production Economics. Correspondence to: Costas P. Pappis, University of Piraeus, 80, Karaoli & Dimitrion Str., 18534 Piraeus, Greece.

## 1. Introduction

The location problem in general is connected with capacity decisions, as the issue of where to expand is almost always raised when the capacity expansion issue is raised. Capacity planning models are highly combinatorial in nature and are usually solved by using heuristics $[3]$ , $[4]$ , $[6]$ . The problem is also connected with routing decisions, that is decisions about fleet size and planned routes $[1]$ , $[8]$ , $[10]$ , $[12]$ .

The location and allocation problems take on considerable significance because the respective decisions represent the basic marketing strategy and may have serious impacts on revenue, costs and service levels $[11]$ . The basic criterion for the choice of location is usually the profit maximization. If all the prices and costs are independent of location, then the choice will be guided by the proximity to potential customers, to similar or competing organizations and to centers of economic activity in general $[2]$ , $[7]$ , $[9]$ .

Apart from profit maximization, service level criteria may also affect managers' decisions as to where to locate a plant or a warehouse. The method proposed here actually assumes the definition of a distance limit between supplying centers and customers. This limit is related to the service level of the company. Thus, the company would reject any solution which would imply that there is one customer located at a distance from all supplying centers greater than that limit.

## 2. Notation

dist = the distance limit between a customer and

the nearest supplying center

$\text{lolim} = \text{the lower limit of dist}$

uplim = the upper limit of dist

pace = the distance that will be added to the lolim repeatedly until the sum equals the uplim.

$$
\begin{array}{l} D C = \text { Distribution   center } \\ S _ {j} = \text { a   candidate   site   to   install   a } D C (j = 1, \dots , n) \\ C _ {i} = \text { a   customer } (i = 1, \dots , m) \\ a _ {i j} = \text { the   covering   coefficients,   where } \end{array}
$$

$$
a _ {i j} = \left\{ \begin{array}{l l} 1, & \text { if   customer } C _ {i} \text { is   covered   by   a } D C \\ & \text { situated   at   site } S _ {j} \text { such   that   the } \\ & \text { distance   between } C _ {i} \text { and } S _ {j} \text { is   less } \\ & \text { than   or   equal   to } d i s t \\ 0, & \text { otherwise } \end{array} \right.
$$

$$
x _ {j} = \left\{ \begin{array}{l l} 1, & \text { if   a } D C \text { is   located   at   site } S _ {j} \\ 0, & \text { otherwise } \end{array} \right.
$$

$c_{ij} =$ the total transportation cost of products from a $DC$ at $S_{j}$ to customer $C_i$ $f_{j} =$ the operational cost of a $DC$ at site $S_{j}$

## 3. The algorithm

The problem is formulated as follows:

“Given uplim, lolim, pace, $S_{j}$ , $C_{i}$ , $c_{ij}$ and $f_{j}$ produce the following decision aids:

(a) Tables showing for each service level (and a respective dist) the optimum location-allocation solution together with the implied cost.

(b) Tables showing the optimum alternative location-allocation solutions and their respective costs which fall within the dist range requiring the same number of DCs."

For the solution of the above problem the following algorithm has been constructed:

Step 1:

(i) Determine uplim, lolim and pace.

(ii) For dist = lolim to uplim with step pace

minimize $z = \sum_{j=1}^{n} x_j$

$$
\text { subject   to } \sum_ {j = 1} ^ {n} a _ {i j} x _ {j} \geqslant 1, \quad i = 1, \dots , m.
$$

Step 2:

For each dist and the respective solution, i.e. set of DC sites, found above, allocate the customers to these DCs, compute each time the respective transportation and operation cost, and (i) find the least of these costs, i.e. find

$$
\text { Min   Total   cost } = \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} a _ {i j} c _ {i j} + \sum_ {j = 1} ^ {n} f _ {j} x _ {j},\tag{1}
$$

(ii) define the respective optimum allocation of customers to DCs.

Step 3:

Determine dist range for which the optimum solutions included correspond to the same number of DCs and list these solutions together with the respective costs and customer allocation schemes.

## 4. Analysis

There are four basic approaches reported in the literature for solving covering problems, such as the one at Step 1. The first is an implicit enumeration approach, such as the branch and bound method. A second approach is to use cutting-plane methods and solve iteratively a number of linear programming problems. The third one is to employ reduction techniques, while the fourth approach involves the use of heuristic methods [5]. In this case study the cutting-plane method was adopted. At Step 1, dist forms an input data and the problem is to find, for each dist value, the least number and the sites of the required DCs so that each customer may be supplied by at least one DC situated at a distance smaller than the respective dist.

Sum (1) at Step 2 consists of two terms. The former depicts the transportation expenses. The expenses for the transportation of supplies from the company's factories to the DCs have not been included as the criterion used here is the customers service level. The second term of (1) refers to the operational expenses of DCs. Obviously, there is a trade-off between the customers' service and the operational cost of DCs, which is a function of the number of DCs.

Usually the results obtained at the previous step show that small deviations of dist are accompanied by large deviations in total cost. This is mainly due to the fact that different groups of DC sites are combined with different customer allocation schemes. At Step 3 the results produced are included in a Table which gives, for each dist range requiring the same number of

![](/api/attachments/WZUZSDBT/fulltext/images/ad14019de3e2f9815a492376501080e1138ac56e5ea372a8e8f87adadae8bc5d.jpg)

Table 1
Demand data

<table><tr><td>No.</td><td>Customer</td><td>Demand (boxes)</td></tr><tr><td>1</td><td>Patras</td><td>1,000,000</td></tr><tr><td>2</td><td>Kalamata</td><td>480,000</td></tr><tr><td>3</td><td>Corinth</td><td>600,000</td></tr><tr><td>4</td><td>Nafplio</td><td>520,000</td></tr><tr><td>5</td><td>Pyrgos</td><td>480,000</td></tr><tr><td>6</td><td>Sparti</td><td>280,000</td></tr><tr><td>7</td><td>Tripoli</td><td>260,000</td></tr></table>

Table 2  
Transportation expenses

<table><tr><td rowspan="2">packing size</td><td colspan="3">transport. expenses (GDR per box)</td><td rowspan="2">demand percent-age</td></tr><tr><td>up to 100 km</td><td>100–200 km</td><td>over 200 km</td></tr><tr><td>250 ml</td><td>16</td><td>34</td><td>41</td><td>43%</td></tr><tr><td>1/1.5 lit</td><td>24</td><td>51</td><td>62</td><td>30%</td></tr><tr><td>2 lit</td><td>15</td><td>32</td><td>39</td><td>2%</td></tr><tr><td>330/200 cc</td><td>8</td><td>18</td><td>22</td><td>25%</td></tr></table>

DCs, the set of the optimum location-allocation alternatives and their respective costs.

## 5. The case study

the installation of new distribution centers (DCs). The product routing currently in effect is described in Figure 1(a). The factory is also used as a DC. As shown in Figure 1 (b) the system proposed includes DCs between factory and customers.

This case study deals with the problem of locating distribution centers serving a given set of customers of a Greek bottling company. The main customer centers of the company are situated in the area of Peloponnese. Each center is the capital of the respective region. There are seven such regions (nomos) in Peloponnese, whose populations are considered in this study to be concentrated in their capital. Table 1 shows the respective demand.

The products of the company are classified in four categories according to packing size, i.e. 250, 1000/1500, 2000 and 200/330 ml. The transportation of the products has been undertaken by a transport agency. There is a classification in transportation expenses according to packing size and distance travelled (Table 2). For simplicity, a mean transportation cost per box is used, which is defined by:

In the present case of the bottling company the problem was to determine the best sites for

$$
C = \sum_ {j = 1} ^ {k} t _ {j} d _ {j},
$$

![](/api/attachments/WZUZSDBT/fulltext/images/80f9e21fb97033626113964639292e512beb5f559a375528504c4d67f4296a0e.jpg)

(a) existing  
![](/api/attachments/WZUZSDBT/fulltext/images/e49ba36ff24a3a13fe7099bb7c307e93ee3a1690a6414bbe38a288765f9d3ec3.jpg)  
(b) Proposed  
Fig. 1. Existing and proposed distribution systems.

Table 3  
Total covering problem results (Step 1)

<table><tr><td>dist (km)</td><td>least no. of warehouses</td><td>installation sites</td></tr><tr><td>55</td><td>7</td><td>1, 2, 3, 4, 5, 6, 7</td></tr><tr><td>60</td><td>5</td><td>1, 3, 4, 5, 6</td></tr><tr><td>65</td><td>4</td><td>1, 3, 5, 6</td></tr><tr><td>70</td><td>4</td><td>1, 3, 5, 6</td></tr><tr><td>75</td><td>4</td><td>1, 2, 4, 5</td></tr><tr><td>80</td><td>4</td><td>1, 2, 4, 5</td></tr><tr><td>85</td><td>4</td><td>1, 2, 4, 5</td></tr><tr><td>90</td><td>4</td><td>1, 2, 3, 5</td></tr><tr><td>95</td><td>3</td><td>1, 2, 3</td></tr><tr><td>100</td><td>3</td><td>1, 2, 3</td></tr><tr><td>105</td><td>3</td><td>1, 2, 3</td></tr><tr><td>110</td><td>2</td><td>1, 7</td></tr><tr><td>115</td><td>2</td><td>1, 7</td></tr><tr><td>120</td><td>2</td><td>1, 7</td></tr><tr><td>125</td><td>2</td><td>1, 7</td></tr><tr><td>130</td><td>2</td><td>1, 7</td></tr><tr><td>135</td><td>2</td><td>4, 5</td></tr><tr><td>140</td><td>2</td><td>1, 6</td></tr><tr><td>145</td><td>2</td><td>4, 5</td></tr><tr><td>150</td><td>2</td><td>4, 5</td></tr><tr><td>155</td><td>1</td><td>7</td></tr></table>

where $t_{j}$ are the transportation expences per box for packing size j, $d_{j}$ is the demand for each packing size (percentage of total demand), k is the number of packing sizes (=4).

Using the data of Table 2 we have:

\- for a distance up to 100 km: $C = 16.38$ GDR (Greek Drachmas)

\- between 100 and $200\mathrm{km}$ : $C = 35.06$ GDR

\- over 200 km: $C = 42.51$ GDR.

In this study $f_{j}$ is considered to be fixed, equal to f, for all possible installation sites (15 millions GDR).

Table 4  
Least total cost resulting from Step 2

<table><tr><td>installation sites</td><td>least total cost (GDR)</td></tr><tr><td>1, 2, 3, 4, 5, 6, 7</td><td>105000000</td></tr><tr><td>1, 3, 4, 5, 6</td><td>87121199</td></tr><tr><td>1, 3, 5, 6</td><td>80638798</td></tr><tr><td>1, 2, 4, 5</td><td>78673198</td></tr><tr><td>1, 2, 3, 5</td><td>77362800</td></tr><tr><td>1, 2, 3</td><td>70225200</td></tr><tr><td>1, 7</td><td>79864800</td></tr><tr><td>4, 5</td><td>87112400</td></tr><tr><td>1, 6</td><td>89250800</td></tr><tr><td>7</td><td>108891200</td></tr></table>

Table 5  
Dist ranges and corresponding sites

<table><tr><td>Service level (km)</td><td>no. of ware-houses</td><td>installation sites</td><td>annual total cost *</td></tr><tr><td>0 to 55</td><td>7</td><td>1, 2, 3, 4, 5, 6, 7</td><td>105.000</td></tr><tr><td>55 to 60</td><td>5</td><td>1, 3, 4, 5, 6</td><td>87.121</td></tr><tr><td>60 to 90</td><td>4</td><td>1, 3, 5, 6</td><td>80.638</td></tr><tr><td></td><td></td><td>1, 2, 4, 5</td><td>78.673</td></tr><tr><td></td><td></td><td>1, 2, 3, 5</td><td>77.362</td></tr><tr><td>90 to 105</td><td>3</td><td>1, 2, 3</td><td>70.225</td></tr><tr><td>105 to 150</td><td>2</td><td>1, 7</td><td>79.864</td></tr><tr><td></td><td></td><td>4, 5</td><td>87.112</td></tr><tr><td></td><td></td><td>1, 6</td><td>89.250</td></tr><tr><td>over 150</td><td>1</td><td>7</td><td>108.891</td></tr></table>

\* million GDR.

Table 6  
Allocation of customers for dist between 60 and 90 km

<table><tr><td colspan="2">Code numbers of proposed sites for distribution centers are:</td></tr><tr><td>1</td><td></td></tr><tr><td>3</td><td></td></tr><tr><td>5</td><td></td></tr><tr><td>6</td><td></td></tr><tr><td colspan="2">Allocation scheme</td></tr><tr><td>customer</td><td>supplier</td></tr><tr><td>1</td><td>1</td></tr><tr><td>3</td><td>3</td></tr><tr><td>5</td><td>5</td></tr><tr><td>6</td><td>6</td></tr><tr><td>2</td><td>6</td></tr><tr><td>4</td><td>3</td></tr><tr><td>7</td><td>6</td></tr><tr><td>Transportation cost (GDR) is:</td><td>20638798</td></tr><tr><td>Operational cost (GDR) is:</td><td>60000000</td></tr><tr><td>Total cost (GDR) is:</td><td>80638798</td></tr><tr><td colspan="2">Code numbers of proposed sites for distribution centers are:</td></tr><tr><td>1</td><td></td></tr><tr><td>2</td><td></td></tr><tr><td>4</td><td></td></tr><tr><td>5</td><td></td></tr><tr><td colspan="2">Allocation scheme</td></tr><tr><td>customer</td><td>supplier</td></tr><tr><td>1</td><td>1</td></tr><tr><td>2</td><td>2</td></tr><tr><td>4</td><td>4</td></tr><tr><td>5</td><td>5</td></tr><tr><td>3</td><td>4</td></tr><tr><td>6</td><td>2</td></tr><tr><td>7</td><td>4</td></tr><tr><td>Transportation cost (GDR) is:</td><td>18673198</td></tr><tr><td>Operational cost (GDR) is:</td><td>60000000</td></tr><tr><td>Total cost (GDR) is:</td><td>78673198</td></tr></table>

Results of Step 1 concerning the present case study are shown in Table 3. Step 2 calculates the least transportation cost for product distribution from DCs to customers, having the data of Table 3 as input. Results of that step are presented in Table 4. Table 5 shows dist ranges corresponding to the same number of DCs and the respective location-allocation cost. Finally Table 6 shows some customer allocation schemes corresponding to the data of Table 5.

Using the algorithm, the best (i.e. most economical) solution of the location–allocation problem is obtained, the decision parameter being the maximum allowable distance between a customer and the nearest supplying center. Thus, in our case study, for dist between 95 and 105 km, the least number of warehouses is 3, the respective sites for the warehouses to be installed are “1” (Patras), “2” (Kalamata) and “3” (Corinth), the least transportation cost is 25.2 m GDR and the total annual cost (including transportation and operational expenses) is 70.2 m GDR. The respective allocation scheme is as follows:

```csv
DC Customers
1 1, 5
2 2, 6, 7
3 3, 4
```

## 6. Conclusion

A DSS to help apply the service level criterion in a location-allocation decision situation has been presented. In this DSS the variable dist has been used as the basis for all formulations and calculations. This variable is very important in respect to the competitive posture of a company as it refers to the service level, which is highly essential for the marketing strategy, particularly in branches such as consumer goods. A case study dealing with the problem of locating distribution centers of a Greek bottling company was used to demonstrate the application of the DSS.

The DSS presented here, rather than providing the decision maker with an exact optimizing solution to the location-allocation problem, it produces a set of aids. These aids assist him in relating the values of the decision criteria that he uses as well as other parameters to the results of the implied decisions. Thus he may use his judgement in an environment of alternative solutions and make his choice on the basis of a cause-effect data set, which has been made explicit by means of the Tables produced by the algorithm.

## References

[1] E. Aarts, J. Korst, Boltzmann machines for travelling salesman problems, Eur. J. Oper. Res., 39, 1989, pp. 79–95.

[2] E.S. Buffa, R.K. Sarin, Modern Production/Operations Management, J. Wiley and Sons, N. York, 1987.

[3] L. Cooper, Heuristic Methods for Location-Allocation Problems, SIAM Review, Vol. 6, No 1, 1964, pp. 37–52.

[4] Erlenkotter D., A dual-based procedure for uncapacitated facility locations, Operational Research 26 (6), 1978, pp. 992–1009.

[5] R. Francis, J. White, Facility Layout and Location, Prentice-Hall, N. Jersey, 1974.

[6] J. Klincewisz, H. Luss, C.S. Yu, A large-scale multilocation capacity planning model, Eur. J. Oper. Res., 34, 1988, pp. 178–190.

[7] M. Korkel, On the exact solution of large-scale simple plant location problems, Eur. J. Oper. Res., 39, 1989, pp. 157–173.

[8] G. Laporte, F. Louveaux, H. Mercure, Models and exact solutions for a class of stochastic location-routing problems, Eur. J. Oper. Res., 39, 1989, pp. 71–78.

[9] D. Miller, J.W. Schmidt, Industrial Engineering and Operations Research, J. Wiley & Sons, New York, 1984.

[10] J. Nambiar, L. Gelders, L. Van Wassenhove, Plant Location and Vehicle Routing in the Malaysian rubber smallholder sector: A case study, Eur. J. Oper. Res., 38, 1989, pp. 14–26.

[11] C.P. Pappis, Production costs in the Periphery: the case of Greece, Eng. Costs & Prod. Econ., 20, 1990, pp. 285-294.

[12] S. Salhi, G.K. Rand, The effect of ignoring routes when locating depots, Eur. J. Oper. Res., 39, 1989, pp. 150–156.
