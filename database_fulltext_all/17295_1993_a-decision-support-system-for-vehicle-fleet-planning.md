---
otero_id: 17295
otero_key: "CQ36VJEM"
title: "A decision support system for vehicle fleet planning"
authors: "Jean Couillard"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90009-r"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for vehicle fleet planning

Jean Couillard

University of Ottawa, Ottawa, Ont., Canada

A decision support system (DSS) is developed to solve the fleet planning problem. The system can be used by fleet managers to plan fleet size and mix. The decision support system was designed to assist managers in every step of the planning process: (i) To forecast demand; (ii) to determine relevant criteria; (iii) to generate alternative plans; (iv) to assess alternative plans with respect to the criteria determined in ii); and (v) to choose 'the best' plan. Emphasis of the decision support system is on flexibility. Another important feature of the decision support system is that it uses both a multicriteria approach to evaluate alternative plans and a stochastic programming model to generate plans. The system can be used to answer a wide variety of 'What if' questions with potentially significant cost impacts. The example provided shows how the DSS can be useful to improve vehicle fleet planning.

Keywords: Decision support system, Vehicle fleet planning, Stochastic programming

## 1. Introduction

Following gradual deregulation of the trucking industry in the province of Québec in Canada, productivity improvement has become a major concern for many trucking companies. It was felt that vehicle fleet productivity could further be improved by better adjusting fleet size to demand. In the province of Québec, vehicle fleet planning is done rather informally. General planning guidelines developed through experience are used. For example, fleet size is adjusted to previous year demand to reduce the uncertainty related to demand forecasting. It is also largely believed that 10% of the vehicles should be replaced each year to keep the mean age of the fleet constant. These guidelines do not explicitly consider the trend of the demand nor the effect of new improved vehicles (in terms of fuel and maintenance efficiency). A more formal approach to fleet planning is needed to take into account the many factors that can impact fleet productivity such as the trend of the demand and new vehicles performance.

Fleet planning is a complex management process which aims at adjusting fleet size and composition to meet the demand in a cost-effective way. It affects both short term and long term operations. For example, enough vehicles should be available daily to meet the demand. In the long run, if vehicle replacement is not carefully planned, substantial costs could be incurred later to update a fleet that is getting too old and obsolete. Uncertainty of demand, future maintenance cost, vehicle residual values, and new vehicle availability are important issues to study.

![](/api/attachments/CQ36VJEM/fulltext/images/37d881d8fc0847d7af3a04e13c103da4aec3a0043af11e305f0fc6e9afdca4b2.jpg)

In order to help managers with fleet planning, a decision support system (DSS) was developed. The DSS was designed to assist the manager in every step of the fleet planning process: (i) To forecast demand; (ii) to determine relevant criteria; (iii) to generate alternative plans; (iv) to evaluate alternative plans with respect to the criteria determined in ii); and (v) to choose ‘the best’ plan.

In the first part of the paper, a conceptual model of the vehicle fleet planning process is presented and a short literature review is given. In the second part, a DSS is developed to formalize each activity of the fleet planning process of the conceptual model. Finally, an example of how the DSS can be used to improve vehicle fleet planning is provided.

## 2. Vehicle fleet planning

A conceptual model of vehicle fleet planning is illustrated in fig. 1. The fleet planning process is divided into five activities. In demand forecasting, the first activity of the fleet planning conceptual model, two sources of data can be used; past sales (ton-miles of merchandise carried) and future service needs, expressed by actual and potential customers. The second activity aims at generating alternative plans to meet the forecasted demand subject to budget constraints and new vehicle availability. A plan is defined for each period by the number of vehicles kept or sold in each different group to meet the demand. A group is composed of vehicles of same make and age at a given period.

The selection of relevant criteria is a third activity of the fleet planning process. Criteria are chosen according to corporate objectives: Profitability, productivity, customer satisfaction, driver satisfaction, etc.. The plans are then evaluated with respect to the criteria selected, this is the fourth management activity. The data can be presented in an evaluation grid, a matrix in which lines represent alternatives,

![](/api/attachments/CQ36VJEM/fulltext/images/91afd4c0bc3e9c358e58ad831ce90472e54a2a0a43e0d5f85b274f87092f191a.jpg)  
Fig. 1. A conceptual model of vehicle fleet planning.

Table 1
Fleet planning models.

<table><tr><td>Authors</td><td>Fleet composition</td><td>Demand</td><td>Expansion policy</td><td>Outside hiring</td><td>Allocation to routes</td><td>Model used</td><td>Solution algorithm</td></tr><tr><td>[9] Kirby [1959]</td><td>No</td><td> $Det^a$ </td><td>No</td><td>Yes</td><td>No</td><td>Algebraic formula</td><td>Optimal</td></tr><tr><td>[19] Wyatt [1961]</td><td>No</td><td>Det</td><td>No</td><td>Yes</td><td>No</td><td>Algebraic formula</td><td>Optimal</td></tr><tr><td>[8] Gould [1975]</td><td>Yes</td><td>Det</td><td>No</td><td>Yes</td><td>No</td><td>Linear programming</td><td>Optimal</td></tr><tr><td>[13] New [1975]</td><td>Yes</td><td>Det</td><td>Yes</td><td>Yes</td><td>No</td><td>Linear programming</td><td>Optimal</td></tr><tr><td>[12] Mole [1975]</td><td>No</td><td>Det</td><td>Yes</td><td>Yes</td><td>No</td><td>Dynamic programming</td><td>Optimal</td></tr><tr><td>[14] Parikh [1977]</td><td>Yes</td><td> $Sto^b$ </td><td>No</td><td>No</td><td>Yes</td><td>Queuing model</td><td>Mathematical approximation</td></tr><tr><td>[10] Levy Golden and Assad [1980]</td><td>Yes</td><td>Det</td><td>No</td><td>No</td><td>Yes</td><td>Integer programming</td><td>Heuristic</td></tr><tr><td>[18] Williams and Fowler [1980]</td><td>No</td><td>Sto</td><td>Yes</td><td>No</td><td>No</td><td>Simulation model</td><td>Simulation</td></tr><tr><td>[1] Avramovich, Cook, Langston and Sutherland</td><td>Yes</td><td>Det</td><td>No</td><td>No</td><td>No</td><td>Linear programming</td><td>Optimal</td></tr><tr><td>[6] Etezadi and Beasley [1983]</td><td>Yes</td><td>Det</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Mixed-integer programming</td><td>Simulation</td></tr><tr><td>[4] Couillard and Martel [1990]</td><td>Yes</td><td>Sto</td><td>Yes</td><td>Yes</td><td>No</td><td>Stochastic programming</td><td>Optimal</td></tr></table>

$^{a}$ Det: Deterministic  
$^{b}$ Sto: Stochastic

columns, criteria, and elements are evaluations. Finally, the fifth activity is the selection of the 'best' plan from the evaluation grid.

The process is complex because it involves dealing with short term and long term operations, and uncertainty (demand, maintenance costs, vehicle residual values, and new vehicle availability). Consequently, in order to formalize the fleet planning process, to allow easy data processing and to provide a tool to answer a wide variety of ‘what if’ questions, a decision support system was designed.

Since the original work of Kirby [9] and Wyatt [19], the fleet sizing and composition problem has been analyzed from different points of view. Models were proposed based on different assumptions such as: (i) the fleet composition (homogeneous or non homogeneous);

(ii) the demand (deterministic or stochastic, stationary or non stationary);

(iii) outside hiring to meet demand (allowed or not allowed).

Table 1 summarizes the models found in the literature on fleet planning according to their basic assumptions, and type of model used.

The DSS developed uses the model described in $[4]$ . The model is much more comprehensive than the others proposed in the literature. It takes into account tax allowances, non homogeneous fleet, the demand as a non stationary stochastic seasonal process, vehicle rental or leasing, replacement/expansion policy. The model generates a minimal discounted cost plan covering the purchase, replacement, sale and/or rental of the vehicles necessary to deal with a seasonal stochastic demand. A stochastic programming model is used to address the problem and can be solved efficiently due to its separability properties.

The DSS can automatically generate the model using basic information from the user and/or a data base, solve the model without the intervention of the user and print the solution of the model in a way that could easily be understood by managers who do not necessarily have knowledge of mathematical programming. Because managers are often reluctant to use the solution of a model they do not understand, it was proposed that the system allow users to input alternative plans that would be validated by the system and then compared to the optimal solution of the model.

![](/api/attachments/CQ36VJEM/fulltext/images/912f1a55459f58ee527440b8c12ecf2e4719a22b0bac8fa13a5b508a5f3eeae6.jpg)  
Fig. 2. The DSS architecture.

## 3. A decision support system for vehicle fleet planning

The DSS is composed of five modules: FORECASTING; CRITERIA; PLANS; EVALUATION; and SELECTION, each one corresponding to an activity of the conceptual model, and a DATA BASE MANAGEMENT System. The DSS architecture is illustrated in fig. 2.

A menu-based approach gives access to the modules. Each module includes a secondary menu of procedures. All procedures are independent and can be used in any order. All data can easily be stored for further processing. A short description of the modules and their procedures follows.

The FORECASTING module helps to forecast the number of ton-miles of merchandise to be carried in each of the planning periods and to determine the number of vehicles required to carry the forecasted volume of merchandise. The module contains five procedures:

(i) SUBJECTIVE allows the manager to input subjective forecasts according to the methodology proposed in [7];

(ii) OBJECTIVE generates objective forecasts from past data using a multiplicative decomposition model;

(iii) COMBINE does a weighted linear combination of the objective and subjective forecasts using a minimum variance criterion to determine the weights [2]. A lognormal distribution is then fitted to the resulting forecasts [3];

(iv) MODIFY allows the manager to change any specific forecast;

(v) TRANSFORM transforms the forecasted volume (ton-miles) of merchandise to be carried into the number of vehicles required to carry it.

The demand can be assumed deterministic or stochastic. If the demand is stochastic, a lognormal distribution is fitted to the forecast errors and confidence intervals are provided together with the forecasts.

The CRITERIA module assists the user in defining a set of relevant criteria. Two procedures are available:

(i) LIST allows the manager to choose from the most frequently used

criteria set, the criteria deemed relevant to the problem on hand;

(ii) INPUT allows the user to define any other criteria for specific application.

Qualitative and quantitative criteria can be selected. According to Vargas and Saaty [17], intangible factors can account for more than 50 percent of vehicle buying decisions.

The PLAN module, which helps the manager to determine alternative plans, is composed of six procedures:

(i) FLEET allows the manager to input data on the existing fleet (type of

vehicles, number, costs, etc.);

(ii) NEW allows the manager to input data on new vehicles;

Actual fleet composition and new vehicles  
Table 2  
Demand forecast and fleet composition.

<table><tr><td rowspan="3">Year</td><td rowspan="3">Period</td><td colspan="6">Forecasts, number of tractors required</td></tr><tr><td colspan="2">Pessimistic value</td><td colspan="2">Most likely value</td><td colspan="2">Optimistic value</td></tr><tr><td> $1^a$ </td><td> $2^b$ </td><td>1</td><td>2</td><td>1</td><td>2</td></tr><tr><td rowspan="4">1988</td><td>1</td><td>8</td><td>39</td><td>9</td><td>41</td><td>10</td><td>43</td></tr><tr><td>2</td><td>7</td><td>37</td><td>8</td><td>39</td><td>9</td><td>41</td></tr><tr><td>3</td><td>7</td><td>40</td><td>8</td><td>42</td><td>9</td><td>44</td></tr><tr><td>4</td><td>5</td><td>31</td><td>6</td><td>33</td><td>7</td><td>35</td></tr><tr><td rowspan="4">1989</td><td>1</td><td>9</td><td>43</td><td>10</td><td>45</td><td>11</td><td>47</td></tr><tr><td>2</td><td>7</td><td>41</td><td>8</td><td>43</td><td>9</td><td>45</td></tr><tr><td>3</td><td>8</td><td>44</td><td>9</td><td>46</td><td>10</td><td>48</td></tr><tr><td>4</td><td>6</td><td>34</td><td>7</td><td>36</td><td>8</td><td>38</td></tr></table>

<table><tr><td>Vehicle type</td><td>Vehicle group</td><td>Mean age (months)</td><td>Average mileage (miles)</td><td>Miles per gallon</td><td> $Capacity^c$ </td><td>Actual number</td><td>Price/ unit ($)</td></tr><tr><td>MACK 84</td><td>C0001</td><td>36</td><td>296 731</td><td>4.2</td><td>2</td><td>4</td><td>57 000.00</td></tr><tr><td>MACK 85</td><td>C0002</td><td>24</td><td>197 072</td><td>4.5</td><td>2</td><td>10</td><td>62 000.00</td></tr><tr><td>MACK 86</td><td>C0003</td><td>12</td><td>97 412</td><td>4.5</td><td>2</td><td>20</td><td>68 000.00</td></tr><tr><td>MACKLT 85</td><td>D0001</td><td>24</td><td>197 022</td><td>5.5</td><td>1</td><td>7</td><td>55 800.00</td></tr><tr><td colspan="8">New vehicles</td></tr><tr><td>MACK 87</td><td>N0001</td><td>0</td><td>0</td><td>5.0</td><td>2</td><td>0</td><td>78 500.00</td></tr><tr><td>MACKLT 87</td><td>N0002</td><td>0</td><td>0</td><td>6.0</td><td>1</td><td>0</td><td>72 150.00</td></tr></table>

$^{a}$ 1: load of less than 50 000 pounds.  
$^{b}$ 2: load of more than 50 000 pounds.  
$^{c}$ Capacity 1 corresponds to vehicles that can only carry loads of less than 50 tons, and 2 any loads.

helps the manager to develop alternative plans; the manager first chooses the different vehicle groups to include in the plan and then specifies the number of vehicle in each group kept and sold at each period;

(iv) GENERATE this procedure generates a stochastic/deterministic fleet planning model [4];

(v) MODIFY modifies any data of a Plan;

(vi) CONSTRAINT allows for the introduction of additional constraints such as capital availability or vehicle availability.

The EVALUATION module assists the manager in evaluating each alternative plan with respect to the criteria selected. The three procedures of this module are:

Table 3
Fleet size and mix plans.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="8">Vehicles kept and sold () each period</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td rowspan="6">Plan #1 codes</td><td>C0001</td><td>4(0)</td><td>4(0)</td><td>4(0)</td><td>4(0)</td><td>0(4)</td><td>0(0)</td><td>0(0)</td><td>0(0)</td></tr><tr><td>C0002 10</td><td>10(0)</td><td>10(0)</td><td>10(0)</td><td>10(0)</td><td>10(0)</td><td>10(0)</td><td>10(0)</td><td>(0)</td></tr><tr><td>C0003</td><td>20(0)</td><td>20(0)</td><td>20(0)</td><td>20(0)</td><td>20(0)</td><td>20(0)</td><td>20(0)</td><td>20(0)</td></tr><tr><td>D0001</td><td>7(0)</td><td>7(0)</td><td>7(0)</td><td>7(0)</td><td>7(0)</td><td>7(0)</td><td>7(0)</td><td>7(0)</td></tr><tr><td>N0001</td><td>8(0)</td><td>8(0)</td><td>8(0)</td><td>8(0)</td><td>8(0)</td><td>8(0)</td><td>8(0)</td><td>8(0)</td></tr><tr><td>N0002</td><td>2(0)</td><td>2(0)</td><td>2(0)</td><td>2(0)</td><td>2(0)</td><td>2(0)</td><td>2(0)</td><td>2(0)</td></tr><tr><td rowspan="6">Plan #2 codes</td><td>C001</td><td>4(0)</td><td>4(0)</td><td>4(0)</td><td>4(0)</td><td>0(0)</td><td>0(0)</td><td>0(0)</td><td>0(0)</td></tr><tr><td>C0002 10</td><td>10(0)</td><td>10(0)</td><td>10(0)</td><td>10(0)</td><td>10(0)</td><td>10(0)</td><td>10(0)</td><td>(0)</td></tr><tr><td>C0003</td><td>20(0)</td><td>20(0)</td><td>20(1)</td><td>20(0)</td><td>20(0)</td><td>20(0)</td><td>20(0)</td><td>20(0)</td></tr><tr><td>D0001</td><td>7(0)</td><td>7(0)</td><td>7(0)</td><td>7(0)</td><td>7(0)</td><td>7(0)</td><td>7(0)</td><td>7(0)</td></tr><tr><td>N0001</td><td>4(0)</td><td>4(0)</td><td>4(0)</td><td>4(0)</td><td>12(0)</td><td>12(0)</td><td>12(0)</td><td>12(0)</td></tr><tr><td>N0002</td><td>1(0)</td><td>1(0)</td><td>1(0)</td><td>1(0)</td><td>2(0)</td><td>2(0)</td><td>2(0)</td><td>2(0)</td></tr><tr><td rowspan="6">Plan #3 codes</td><td>C0001</td><td>4(0)</td><td>4(0)</td><td>4(0)</td><td>0(4)</td><td>0(4)</td><td>0(0)</td><td>0(0)</td><td>0(0)</td></tr><tr><td>C0002</td><td>10(0)</td><td>10(0)</td><td>10(0)</td><td>7(3)</td><td>7(0)</td><td>7(0)</td><td>7(0)</td><td>7(7)</td></tr><tr><td>C0003</td><td>20(0)</td><td>20(0)</td><td>20(0)</td><td>20(0)</td><td>20(0)</td><td>20(0)</td><td>20(0)</td><td>20(0)</td></tr><tr><td>D0001</td><td>2(5)</td><td>2(0)</td><td>2(0)</td><td>2(0)</td><td>2(0)</td><td>2(0)</td><td>2(0)</td><td>2(0)</td></tr><tr><td>N0001</td><td>7(0)</td><td>7(0)</td><td>8(0)</td><td>8(0)</td><td>17(0)</td><td>17(0)</td><td>18(0)</td><td>18(0)</td></tr><tr><td>N0002</td><td>0(0)</td><td>0(0)</td><td>0(0)</td><td>0(0)</td><td>0(0)</td><td>0(0)</td><td>0(0)</td><td>0(0)</td></tr></table>

(i) INPUT allows the user to directly input evaluations;

(ii) CALCULATION this procedure performs all calculations (estimated ownership costs,

(iii) MODIFY to modify any data of the evaluation grid.

Finally, SELECTION module, helps the manager to choose the ‘best’ plan. Three procedures are proposed:

(i) TOTAL does the sum of all costs and the weighted average of qualitative criteria,

(ii) WEIGHT does a weighted sum of quantitative and qualitative criteria,

(iii) ELECTRE 2 applies the ELECTRE 2 method [15].

The proposed DSS includes all of the characteristics of an effective DSS from the generic DSS framework of Sprague and Carlson [16]:

(i) it supports a semi-structured decision;

(ii) it supports all phases of decision making (intelligence, design, choice and implementation);

(iii) it combines modelling techniques with data base and data presentation techniques;

(iv) it emphasizes ease of use and flexibility/adaptability;

(v) it interacts with transaction processing (EDP).

It can be categorized in the Specific DSS (SDSS) group (see Sprague and Carlson [16] for a complete nomenclature of DSS). It is divided into three components: The Dialogue Component, the Modelling

Table 4

Sample interaction with the DSS. $^{a}$

ENTER THE NAME OF THE MODULE TO BE ACCESSED:

FORECASTING

CRITERIA

PLANS

EVALUATION

SELECTION

$\Rightarrow$ EVALUATION b

DATABASE MANAGEMENT

ENTER THE NAME OF THE PROCEDURE TO BE ACCESSED:

INPUT

CALCULATION

MODIFY

$\Rightarrow$ CALCULATION

ENTER THE RENTING COST PER VEHICLE PER PERIOD (3 MONTHS):

⇒ \$12,000

ENTER THE DEPRECIATION METHOD:

1. LINEAR DEPRECIATION

2. DECLINING BALANCE METHOD

$\Rightarrow 2$

ENTER THE DEPRECIATION RATE:

⇒.30

ENTER THE INTEREST RATE:

$\Rightarrow .18$

ENTER THE MARGINAL TAX RATE:

$\Rightarrow .40$

$^{a}$ Translated from French

$^{b}$ Data input by user are in bold

<table><tr><td>DATE</td><td>Mileage</td><td>Age</td><td>Serv.</td><td>Owning cost</td><td>Interest</td><td>Maint. cost</td><td>Fuel cost</td><td>Rental cost</td><td>Tax allocation</td><td>Total cost</td></tr><tr><td colspan="11">Plan #1</td></tr><tr><td>1/7/87</td><td>158 180</td><td>19</td><td>0.00</td><td>1 990 099.63</td><td>532 666.06</td><td>664 537.88</td><td>1 784 293.50</td><td>0.00</td><td>1 988 639.00</td><td>2 982 958.50</td></tr><tr><td colspan="11">Estimation</td></tr><tr><td>1/1/88</td><td>176 988</td><td>21</td><td>1.00</td><td>2 538 071.50</td><td>665 239.56</td><td>995 743.88</td><td>2 297 640.75</td><td>0.03</td><td>2 598 678.50</td><td>3 898 017.50</td></tr><tr><td>1/7/88</td><td>226 812</td><td>27</td><td>1.00</td><td>2 954 858.75</td><td>760 953.25</td><td>1 384 546.75</td><td>2 694 887.25</td><td>183.71</td><td>3 118 172.00</td><td>4 677 258.00</td></tr><tr><td>1/1/89</td><td>228 067</td><td>27</td><td>1.00</td><td>3 420 452.25</td><td>868 063.63</td><td>1 778 481.63</td><td>3 245 425.50</td><td>183.71</td><td>3 725 042.75</td><td>5 587 564.50</td></tr><tr><td>1/7/89</td><td>277 887</td><td>33</td><td>1.00</td><td>3 708 057.25</td><td>940 349.06</td><td>2 216 440.00</td><td>3 665 755.25</td><td>230.00</td><td>4 212 332.50</td><td>6 318 499.50</td></tr><tr><td colspan="11">Plan #2</td></tr><tr><td>1/7/87</td><td>158 100</td><td>19</td><td>0.00</td><td>1 990 099.63</td><td>532 666.06</td><td>664 537.88</td><td>1 784 293.50</td><td>0.00</td><td>1 988 639.00</td><td>2 982 958.50</td></tr><tr><td>1/1/88</td><td>190 813</td><td>23</td><td>0.90</td><td>2 445 854.50</td><td>642 464.06</td><td>978 148.25</td><td>2 308 208.00</td><td>43 572.88</td><td>2 567 299.25</td><td>3 850 948.75</td></tr><tr><td>1/7/88</td><td>240 640</td><td>29</td><td>1.00</td><td>2 792 501.50</td><td>720 326.25</td><td>1 334 456.50</td><td>2 710 097.75</td><td>97 092.89</td><td>3 061 790.25</td><td>4 592 685.50</td></tr><tr><td>1/1/89</td><td>235 779</td><td>28</td><td>0.90</td><td>3 204 746.50</td><td>813 802.06</td><td>1 688 149.75</td><td>3 278 871.50</td><td>137 425.80</td><td>3 649 198.50</td><td>5 473 797.50</td></tr><tr><td>1/7/89</td><td>285 601</td><td>34</td><td>1.00</td><td>3 451 774.50</td><td>876 050.75</td><td>2 081 306.88</td><td>3 703 806.25</td><td>188 305.81</td><td>4 120 497.75</td><td>6 180 747.50</td></tr><tr><td colspan="11">Plan #3</td></tr><tr><td>1/7/87</td><td>158 180</td><td>19</td><td>0.00</td><td>1 990 099.63</td><td>532 666.06</td><td>664 537.88</td><td>1 784 293.59</td><td>0.00</td><td>1 988 639.00</td><td>2 982 958.50</td></tr><tr><td>1/1/88</td><td>177 732</td><td>21</td><td>0.90</td><td>2 453 297.50</td><td>644 958.69</td><td>949 202.50</td><td>2 274 935.75</td><td>114 239.98</td><td>2 574 653.75</td><td>3 861 980.75</td></tr><tr><td>1/7/88</td><td>198 892</td><td>24</td><td>0.96</td><td>2 818 696.75</td><td>729 344.75</td><td>1 248 169.50</td><td>2 693 698.00</td><td>209 400.11</td><td>3 079 723.75</td><td>4 619 585.50</td></tr><tr><td>1/1/89</td><td>209 797</td><td>25</td><td>0.90</td><td>3 230 812.25</td><td>829 022.81</td><td>1 560 053.13</td><td>3 205 685.50</td><td>364 440.13</td><td>3 676 005.50</td><td>5 514 008.50</td></tr><tr><td>1/7/89</td><td>230 435</td><td>27</td><td>0.90</td><td>3 490 707.50</td><td>902 740.06</td><td>1 886 966.75</td><td>3 644 304.00</td><td>487 800.13</td><td>4 165 007.50</td><td>6 247 511.50</td></tr></table>

Component and the Data Base Component. The integration of the three components of the DSS is achieved through a sandwich architecture (see the terminology proposed by Sprague and Carlson [16], pp. 285–287). The DSS was developed in FORTRAN77 and includes the mathematical programming software XMP developed by R.E. Marsten [11].

## 3. Illustration of the decision support system

In this section an example is given to illustrate the utilization of the DSS. Let us suppose that quarterly forecasts of the number of tractors required for the next two years, beginning as of January 1988, were obtained. For each forecast, 99% confidence intervals were calculated assuming that the demand is normally distributed. Table 2 gives the forecasted demand with the 99% confidence intervals, the current fleet size and composition, and the new vehicles available.

<table><tr><td colspan="7">Table 6Illustration of the ‘WHAT IF’ capability of the system.</td></tr><tr><td colspan="7">⇒ CALCULATIONENTER THE RENTING COST PER VEHICLE PER PERIOD (3 MONTHS):⇒ $12,000ENTER THE DEPRECIATION METHOD:1. LINEAR DEPRECIATION2. DECLINING BALANCE METHOD⇒ 2ENTER THE DEPRECIATION RATE:⇒ .40ENTER THE INTEREST RATE:⇒ .18ENTER THE MARGINAL TAX RATE:⇒ .40Plan #1</td></tr><tr><td>DATE</td><td>MILEAGE</td><td>AGE</td><td>SERV.</td><td>OWNING COST</td><td>TAX ALLOCATION</td><td>TOTAL COST</td></tr><tr><td>1/7/87</td><td>158 180</td><td>19</td><td>0.00</td><td>2 284 612.75</td><td>2 106 444.08</td><td>3 159 666.11</td></tr><tr><td colspan="7">ESTIMATION</td></tr><tr><td>1/1/88</td><td>176 988</td><td>21</td><td>1.00</td><td>2 874 605.75</td><td>2 733 292.99</td><td>4 099 937.98</td></tr><tr><td>1/7/88</td><td>226 812</td><td>27</td><td>1.00</td><td>3 290 066.25</td><td>3 252 255.88</td><td>4 878 382.33</td></tr><tr><td>1/1/89</td><td>228 067</td><td>27</td><td>1.00</td><td>3 772 387.50</td><td>3 865 817.79</td><td>5 798 725.18</td></tr><tr><td>1/7/89</td><td>277 887</td><td>33</td><td>1.00</td><td>4 042 471.75</td><td>4 346 098.42</td><td>6 519 147.64</td></tr><tr><td colspan="7">PLAN #2</td></tr><tr><td>DATE</td><td>MILEAGE</td><td>AGE</td><td>SERV.</td><td>OWNING COST</td><td>TAX ALLOCATION</td><td>TOTAL COST</td></tr><tr><td>1/7/87</td><td>158 180</td><td>19</td><td>0.00</td><td>2 284 612.75</td><td>2 106 444.08</td><td>3 159 666.11</td></tr><tr><td colspan="7">STIMATION</td></tr><tr><td>1/1/88</td><td>190 813</td><td>23</td><td>0.90</td><td>2 760 655.25</td><td>2 693 219.38</td><td>4 039 829.06</td></tr><tr><td>1/7/88</td><td>240 640</td><td>29</td><td>1.00</td><td>3 095 874.50</td><td>3 183 139.16</td><td>4 774 709.73</td></tr><tr><td>1/1/89</td><td>235 779</td><td>28</td><td>0.90</td><td>3 521 691.50</td><td>3 775 976.24</td><td>5 663 964.37</td></tr><tr><td>1/7/89</td><td>285 601</td><td>34</td><td>1.00</td><td>3 751 986.75</td><td>4 240 583.58</td><td>6 360 874.86</td></tr><tr><td colspan="7">PLAN #3</td></tr><tr><td>DATE</td><td>MILEAGE</td><td>AGE</td><td>SERV.</td><td>OWNING COST</td><td>TAX ALLOCATION</td><td>TOTAL COST</td></tr><tr><td>1/7/87</td><td>158 180</td><td>19</td><td>0.00</td><td>2 284 612.75</td><td>2 106 444.08</td><td>3 159 666.11</td></tr><tr><td colspan="7">EstIMATION</td></tr><tr><td>1/1/88</td><td>177 732</td><td>21</td><td>0.90</td><td>2 780 197.25</td><td>2 705 413.67</td><td>4 058 120.50</td></tr><tr><td>1/7/88</td><td>198 892</td><td>24</td><td>0.96</td><td>3 148 449.75</td><td>3 211 625.84</td><td>4 817 437.27</td></tr><tr><td>1/1/89</td><td>209 797</td><td>25</td><td>0.90</td><td>3 584 440.50</td><td>3 817 457.83</td><td>5 726 185.24</td></tr><tr><td>1/7/89</td><td>230 435</td><td>27</td><td>0.90</td><td>3 840 332.75</td><td>4 304 857.48</td><td>6 457 286.21</td></tr></table>

Three plans, given in table 3, are analyzed. According to the first plan, vehicles are replaced when they reach their economic life (the economic life of a vehicle is obtained by minimizing the maintenance and ownership costs functions, see [5]). Plan 2 minimizes the maintenance and ownership costs over the two years period, and the last plan was generated by the stochastic model.

Table 4 gives a sample interaction with the DSS to obtain the evaluation grid using the CALCULATION procedure.

Table 5 gives the estimated costs for the next two years on a 6 month basis. The last column gives the total cost minus tax allocations for each period. For the given situation, replacing vehicles when they reach their economic life (Plan 1) not only increases total operating cost, but also the average fleet age. Plan 2 yields the lowest total operating cost but the average fleet age is significantly higher than in Plan 3, postponing more expenses for a later date. The choice between Plan 2 and Plan 3 then becomes a matter of long-term and short-term objectives.

Because cost estimates are rapidly generated by the DSS, a wide variety of 'what if' questions can be dealt with. For example, what happens if residual value goes down 10% (i.e. the depreciation rate goes from 30% to 40%). Table 6 illustrates the 'what if' capability of the DSS on the current plans (note that Plan 3 is no longer optimal and the GENERATE module should be used to obtain the optimal solution; however, only the effect on the current plans will be examined here). The depreciation rate is changed using the EVALUATION module. The evaluation grid is automatically up-dated. In table 6, only the columns of the previous evaluation grid which are affected by the modification are given.

All estimates and parameters can be modified, one or many at a time, for sensitivity analysis. This is a very important feature of the DSS, making it a useful tool for this rapidly changing environment.

## 4. Conclusion

A DSS was developed to improve vehicle fleet planning. It was designed to assist managers in every step of the process. The DSS does not automate the decision-making process but helps the manager at every step of the process by providing powerful tools to forecast the demand, to choose relevant criteria, to generate alternative plans, to assess alternative plans with respect to the criteria and to choose the ‘best’ plan.

The example provided shows that the determination of fleet size and composition is a complex management process involving trade-offs between short-term and long-term objectives, and uncertainty (demand, maintenance costs, owning costs, etc.). A decision support system therefore becomes a useful tool to deal with such a complex problem.

## References

[1] D. Avramovich, and D, T.T. Cook, G.D. Langston and F. Sutherland, A Decision Support System for Fleet Management: A Linear Programming Approach, Interfaces 12, No. 3 (1982).

[2] J.M. Bates, and C.W. Granger, The Combination of Forecasts. Opl. Res. Q. 20, pp. 451–468 (1969).

[3] J. Couillard, and G.R. d'Avignon, The Combination of Forecasts in Road Transportation Industry, Seventh International Symposium on Forecasting, May 26–29, Boston, Massachusetts, 20 p. (1987).

[4] J. Couillard, and A. Martel, Vehicle Fleet Planning in the Road Transportation Industry, IEEE Transactions on Engineering Management 37, No. 1, pp. 31–36 (1990).

[5] d'Avignon, and J. Couillard, Politique de remplacement de tracteurs, DS-80-21 F.S.A. (U. Laval, Québec, 1980).

[6] T. Etezadi, and J.E. Beasley, Vehicle Fleet Composition, Journal of Operational Research Society 34, pp. 87–91 (1983).

[7] A. Gascon, Subjective Estimation of an Effectiveness Distribution: The Lognormal, Rapport de recherche RR-8, GREP, Faculté des sciences de l'administration, Université Laval (1979).

[8] J. Gould, The Size and Composition of a Road Transportation fleet, Operational Research Quarterly 20, pp. 81–92 (1969).

[9] P. Kirby, Is Your Fleet the Right Size?, Operational Research Quarterly 10, p. 252 (1959).

[10] L. Levy, B. Goldon, and A. Assad, The Fleet Size and Mix Vehicle Routing Problem, Management Science and Statistics Working Paper, No. 80-001. College of Business and Management, University of Maryland.

[11] R.E. Marsten, Introduction to XMP, College of Business and Public Administration, University of Arizona (1982).

[12] R.H. Mole, Dynamic Optimization of Vehicle Fleet Size, Operational Research Quarterly 26, pp. 25–34 (1975).

[13] C.C. New, Transport Fleet Planning for Multi-Period Operations, Operational Research Quarterly 26, pp. 151–166 (1975).

[14] S.C. Parikh, On a Fleet Sizing and Allocation Problem, Management Science 23, No. 9, pp. 972–977 (1975).

[15] B. Roy, La Méthode ELECTRE R, METRA, Direction scientifique, note de travail, No. 142 (1971).

[16] R.H. Sprague Jr., and E.D. Carlson, Building Effective Decision Support Systems, p. 239 (Prentice Hall. New Jersey, 1982).

[17] L.G. Vargas, and T.L. Saaty, Financial and Intangible Factors in Fleet Lease or Buy Decision, Industrial Marketing Management 10, pp. 1–10 (1981).

[18] W.W. Williams, and O.S. Fowler, Minimum Cost Fleet Sizing for a University Motor Pool, Interfaces 10, No. 3, pp. 21–29 (1980).

[19] J.K. Wyatt, Optimal Fleet Size, Operational Research Quarterly 12, p. 186 (1961).
