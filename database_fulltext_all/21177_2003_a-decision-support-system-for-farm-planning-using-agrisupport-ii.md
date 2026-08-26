---
otero_id: 21177
otero_key: "YP5SXM2J"
title: "A decision support system for farm planning using AgriSupport II"
authors: "B. Recio; F. Rubio; J.A. Criado"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00134-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# A decision support system for farm planning using AgriSupport II

B. Recio \*, F. Rubio, J.A. Criado

Departamento de Matema´tica Aplicada a la Ingenierı´a Agrono´mica, Escuela Te´cnica Superior de Ingenieros Agro´nomos, Universidad Polite´cnica de Madrid, Avenida de la Complutense s/n, Madrid 28040, Spain

Accepted 3 July 2002

## Abstract

The farm planning problem is a critical aspect in the design of decision support systems (DSSs) for complex farm advising. Traditionally, the approaches to this problem have been very simple and unable to manage the complexity of the problem, which involves scheduling of field tasks, investment analysis, machinery selection, cost/benefit analysis, and other aspect of the agricultural production process. A new approach to this problem is presented for medium – large farms and integrated in a more general framework to build DSSs in agriculture. The system have been validated for the technicians of Albacete Provincial Technical Agricultural Institute (ITAP) and accepted as the core of future broad DSSs for their use. This is overall objective of the AgriSupport II project.

<sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Agricultural farm planning; Integer programming; Decision support system

## 1. Introduction

Farmers today face economic and environmental pressures. Product prices are falling, forcing farmers to lower their production costs and evaluate new production alternatives and crops in order to make farming profitable. This makes planning, aimed at achieving biologically and economically optimal levels for the crop production system, even more important than it was before.

Crop production is a complex enterprise involving many decision-making processes that depend on a host of factors. Some factors, like climatic conditions, land characteristics, etc., are inherent to the farm and cannot be altered or controlled. Other farm properties, like the current structure of the machinery stock and personnel, the irrigation infrastructure in place, etc., are factors possibly to be taken into account. These factors can be modified for the purposes of achieving maximum profitability.

The above factors are what constitute the farm’s options. These options cover a wide variety of alternatives on which decisions have to be made, such as the choice of which crops to grow, which field operations to perform, how and when to complete these operations, using which machinery, which fertilisers and other chemical substances are to be applied, etc. This is what is known as field operation planning.

Therefore, the field operation planning problem is inseparable from any analysis involving activity scheduling and cost control. Indeed, the development of methods to support the selection and planning of field operations has been the subject of research at technological and research centres all over the world (see Refs. [3,9,10] for some pioneering work and Refs. [1,2] for more recent work). These farm planning and technical advice systems help farmers to optimise their resources according to business prospects and manage the production risk in the manner best suited to their interests. These systems are called Decision Support Systems for Planning Field Operations. Their main functions are as follows: provision of strategic advice about the crops to be planted, etc., resource (machinery and personnel) sizing and acquisition planning, specialised advice on particular points (markets, treatments, and fertilisers), and task identification and scheduling. Fig. 1 shows the importance of field operation planning in agriculture advising.

The structure of the farm or farms interested in planning their operations varies, and there are different levels of complexity. These structures can be classified by level of complexity as follows:

. A farm with a single plot. There are no conflicts between resources in this case, and the problem is confined to suitable resource sizing and the provision of the respective specialised advice. This is not a realistic problem nowadays and is not representative of real-world production.

. A farm with several plots. A crop is grown on each plot, which is actually an independent unit of production. The farm owns the global resources for application, and the conflicts concerning resource use arise depending on the number of resources, the characteristics of the plots, and the complexity of the operations to be performed. This is the scenario for most farming businesses.

. Many coordinated farms. This occurs when resources are shared at a higher level than the farm (shared machinery, coordination of activities with a processing plant, etc.). The conflicts concerning resource use are generalised, leading to a wide range of possibilities that make these scenarios difficult to resolve. This is the case of agricultural cooperatives, and advice must be oriented to the whole cooperative rather than to individual producers.

A lot of models of field operations planning have been developed either based in operational research as in heuristic search and other AI techniques. None of them have obtained full success. The three options that have had results closest to a global solution are the:

 linear programming approach,

 dynamic programming approach, and

 simulation approach.

The three of them are operational research-based. Among them, dynamic programming is the method less used due to its model and copulation-inherent problems.

Problems groups in agriculture advising  
![](/api/attachments/YP5SXM2J/fulltext/images/bce78e4468adcc701def9664e85a9dfdb515a37cec36f97f57fcc14f9bbd0e30.jpg)  
Fig. 1. Importance of the field operation planning problem.

Planning models often have probabilistic elements when the impact of certain facts do not have a deterministic impact in the result. In spite of this, probabilistic models have several disadvantages when applied to this kind of problems, normally making its application not feasible. For this reason, it is usual to apply deterministic models, approaching the unknown parameters to fixed values using statistic methods. The reasons for this approach are these:

. The probabilistic structure of a model have an important impact over its behavior. For example, when considering in a climate model the impact of exceptional years (years with a low level of probability), it cannot be contemplated using statistical average values.

. Models, mainly linear programming and simulation, are based on a deterministic orientation. Therefore, the probabilistic approach is an extension of the basic model [14]. Therefore, if we want to consider probabilistic factors without restrictions, we have to use other methods different from linear programming, which, in its probabilistic version, is too heavy for most of the DSSs. We can consider dynamic probabilistic programming.

. Actually, most of the models applied in field operation planning are of deterministic nature.

In Table 1, the general advantages and disadvantages of each model are shown according to Refs. [11,13,14].

We have designed a new approach to this problem, trying to represent the problem complexity yet assuming as few compromises as possible and, after that, looking for the methodology that can manage the problem. We have tried three approaches, choosing two of them to be implemented in the system.

Comparison among classical approaches to the farm planning problem

<table><tr><td>Characteristics</td><td>Simulation</td><td>Dynamic programming</td><td>Linear programming</td></tr><tr><td>Reality description</td><td>short</td><td>short</td><td>depends of problem</td></tr><tr><td>Computation effort</td><td>low</td><td>high</td><td>high</td></tr><tr><td>Operation sequence</td><td>correct</td><td>correct</td><td>unknown</td></tr><tr><td>Feasibility in real DSSs</td><td>not used</td><td>fair</td><td>fair</td></tr><tr><td>Result type</td><td>suboptimal</td><td>optimal</td><td>optimal</td></tr><tr><td>Complexity</td><td>-</td><td>simple</td><td>depends of problem</td></tr><tr><td>Software availability</td><td>?</td><td>?</td><td>available</td></tr></table>

This effort is for the global AgriSupport II project that aims to develop tools and schemes to implement DSSs for agricultural advising.

## 2. The AgriSupport II project

The design and implementation of DSSs for agricultural advising have particular problems that make the application of this technology in the agroalimentary field difficult. The difficulty arises from the application of a generalist solution using a unique technology (see Refs. [6,8] for a full analysis).

From 1992, the Information Technology and Agriculture Group of the Universidad Polite´cnica de Madrid have been working to identify the origin of the relative failure of DSSs and to design the methods and tools to solve these in order to successfully implement DSSs in the agricultural sector.

The AgriSupport II project’s overall objective is to translate the latest advances in intelligent DSSs, adapting them to fit into the needs of the agricultural sector.

Basically, it is the implementation of a family of tools to design and build DSSs for agricultural advising, including some sort of field operation planning that solves the traditional limits of the methods to perform it.

The so-called AgriSupport system have three elements:

. A model that is composed of a series of abstractions to structure agriculture productive process elements and specialised algorithms that, working over them, perform the planning and the analysis of a farm using different calculation paths in function of the freedom of the problem variables. Fig. 2 shows the main elements of this model.

. A system that is composed of a series of software tools to assist in the development of DSSs using the above models and algorithms.

. A methodology to guide in the analysis of a problem in agriculture advising and the design of DSSs to support it.

![](/api/attachments/YP5SXM2J/fulltext/images/ace6073cb537be65252f516b4d460ff38d46035cca4a0d6738e77cfaa2f7e8f0.jpg)  
Fig. 2. Elements of the AgriSupport model.

In this general framework, the farm planning model algorithm is the key element in the system.

## 3. The planning model

Planning must take into account all the agricultural activities of the farm to decide on the minimum requirements in terms of machinery, labour, etc., for viable operation. The activities carried out on farms are determined by two higher level concepts that are structured hierarchically as follows:

. Field work: all the work carried out in connection with a crop for the purposes of preparing and improving the soil and the crop, with the ultimate aim of getting a good harvest.

. Field operation: all field work has a specific goal, which is attained by carrying out activities (tasks) that are grouped under a particular operation. The operations have different ways of achieving a goal. This means that an operation comprises several activities that have a common aim, which is the aim set by the field work of which the operation is part of.

Field work is completed by performing one of the possible operations available for achieving the goal in question. The choice of operation depends on the crop type, the soil type, and the climatic zone, where the operation that best achieves the goal set by the field work is chosen. The decision on which operation to select to perform the field work is part of the expert knowledge in agronomics and takes into account the structural characteristics of the farm and the crop in question. Supported by the knowledge available in the system, the engineer makes this decision before running the planning model.

A technical path for a crop is defined as the specific sequence of operations to be performed. The field operations of the farm are planned on the basis of one or more technical paths of tasks to be performed (as many paths as crops or plots are considered) and of the available resources for performing these tasks. The technical paths include all the tasks to be performed on the farm and their relationships of precedence.

Resources are either material, including machinery, implements, etc., or human, including permanent or temporary workers employed on the farm. Each resource has an associated variable and fixed cost. The variable cost is how much it costs to use the resource and this will be included in the estimated cost of performing the tasks for which the resource is used.

The fixed cost is not proportional to either the length of time or the number of times it is used. This cost includes the costs of storage, depreciation, insurance, etc. for keeping the resource on the farm.

The purchase of new farm implements at the start of the farming season is a usual rather than an exceptional occurrence. This means that the resources considered have to account for existing and hypothetical items, the acquisition of which is one of the decisions to the made as part of the problem. If this property was not included, the system would not respond to one of the most important decision-making factors in this environment: the policy of machinery purchase and personnel hiring. This would lead to overly static circumstances and is unlikely to represent real or optimum situations. Therefore, a resource that is not really present on the farm is considered. The fixed cost also includes the costs of purchase, hire, etc., depending on how the resource is to be acquired.

Having defined the available resources for planning, these resources are divided into different work units, normally composed of a tractor, an implement, and a series of human operators.

The next step is to identify which work units are suitable for performing each task. We call each of the possible variants for performing a task mode.

An execution time and a cost is estimated for each mode, depending on the characteristics of the land, the climate, the resources employed, etc. The cost of a mode includes the variable cost of the resources used, after estimating the time it will take to perform the task according to this mode.

The data required for planning and which will be needed in the optimisation model can be summarised as follows:

Technical path, which implies knowing: Tasks to be performed Precedence among tasks About each task: Precedence with other tasks (established by the technical path including the task) Time window Modes for performance About each mode: Resources used (established by the definition of the mode)

Length Cost About each resource: Variable cost (used to estimate the cost of the mode using the resource) Fixed cost

These data raise a mixed-integer linear programming problem for decision-making on annual planning, that is, when to perform each task and using what resources, or, alternatively, by what mode.

The goal is to minimise the cost, which is the sum of the costs of the selected modes and the fixed cost of the resources used.

Of course, all the problem-solving constraints must be included, such as allocating a mode for each task, assuring that the relationships of precedence are respected, assuring that each task is performed within its time window, and assuring that resource allocation is workable. When we formulated the problem, we encountered several difficulties that forced us to develop new mathematical models for this sort of problems.

The first difficulty, which ultimately determines the selected model, is the size of the problem. The path defined to get the model input data (resources ! work units ! modes) produces a wide variety of modes. A simple example would be 3 tractors, 4 implements, 2 operators, and 12 tasks. In this case, we will have 24 work units and around 200 modes (taking into account that not all the work units are applicable to all the tasks). If the farm has 7 tractors, 12 implements, and 5 operators to perform 40 tasks, there will be 420 work units and around 10,000 modes.

Another factor to be taken into account was how to manage time. An agricultural year lasts between 8 and 12 months, depending on the crops. Although there are long periods between tasks, bottlenecks lasting 1– 2 weeks tend to arise at critical times (harvesting etc.). At these points, several tasks have to be performed in a very short period and call for work units that are very similar in structure. In addition, a delay of one or more days in performance causes a significant loss of production. Accuracy to a day (or half a day) is required to study the feasibility of a work plan and overlapping tasks in these periods.

It was the time factor, together with the possibility of generating a huge number of modes, that led us to discard the models that we had originally developed, which considered time discretely, that is, divided into periods. Instead, we opted for a continuous variable that represents when a task is to be started (see Ref. [4] for some alternative models).

However, we were obliged to set a series of conditions for feasible resource allocation in this continuous time approach. We termed these conditions incompatibilities. They ensure that no two tasks whose modes have a resource in common are carried out at the same time. One weakness of this model is that the number of incompatibility conditions grows very quickly if there is a wide variety of crops. This growth is not initially proportional to the number of tasks, as their paths are parallel and a lot of incompatibilities have to be defined. However, the results obtained for real problems show that the problemsolving time is very short in all these cases (see next section). This provides user interactivity, and users can define new crop or resource scenarios for evaluation as and when considered necessary.

The model is shown in Appendix B and explained in detail in Ref. [12].

## 4. Implementation and computational experience

The system described was experimentally implemented in a program connected to an Excel spreadsheet. The characteristics of the farm, crops, number of plots, etc. and the resources under consideration were entered in the spreadsheet. The spreadsheet output the respective modes for these parameters, calculating the cost and time for performing each mode. These data were then sent to the program (in which the model formulation is programmed in C++, connected to the CPLEX optimiser), which runs the developed model. The solution, if any, travels the inverse path to return to the spreadsheet for analysis. The major drawback of this first implementation was that the modes were calculated automatically without including expert knowledge, which could be used to discard some modes in given scenarios.

As the results obtained were very satisfactory, a full DSS was designed and implemented using this technology. The program is implemented in C++ (again linked to CPLEX as an optimiser) and makes use of all the objects and facilities of the AgriSupport environment. In this case, every time the model is executed, the respective modes are generated, and modes that are not advisable on technical grounds or make no substantial contribution to the existing ones are deleted. Because of this feature, it was possible to reduce the modes’ final input into the optimiser by about a third. The application can be run on a range of platforms, including PCs running Windows 95/98. Of course, performance depends on the specifications of the environment. The results presented here were obtained on a Sun Enterprise 450 with CPU Ultra-SPARC II 300 MHz, using the default strategies of the CPLEX 6.6 optimiser.

The AgriSupport system was applied at ITAP experimental farms in Albacete (Spain), where different combinations of crops were proposed and experimented with.

The computational experiment reported covers 25 case studies using different resources and crops. The objective was to plan the production in an area of approximately 300 ha. The cases are divided into five blocks, depending on the number of crops involved.

Table 2  
Problem data

<table><tr><td>Code</td><td>Tasks</td><td>Modes</td><td>Resources</td><td>Precedence</td><td>Incompatibilities</td></tr><tr><td>A1</td><td>11</td><td>21</td><td>18</td><td>6</td><td>11</td></tr><tr><td>A2</td><td>11</td><td>58</td><td>22</td><td>6</td><td>16</td></tr><tr><td>A3</td><td>11</td><td>169</td><td>26</td><td>6</td><td>21</td></tr><tr><td>A4</td><td>11</td><td>480</td><td>30</td><td>6</td><td>26</td></tr><tr><td>A5</td><td>11</td><td>760</td><td>36</td><td>6</td><td>30</td></tr><tr><td>B1</td><td>24</td><td>45</td><td>18</td><td>14</td><td>71</td></tr><tr><td>B2</td><td>24</td><td>127</td><td>22</td><td>14</td><td>106</td></tr><tr><td>B3</td><td>24</td><td>355</td><td>26</td><td>14</td><td>141</td></tr><tr><td>B4</td><td>24</td><td>984</td><td>30</td><td>14</td><td>176</td></tr><tr><td>B5</td><td>24</td><td>1552</td><td>36</td><td>14</td><td>206</td></tr><tr><td>C1</td><td>33</td><td>60</td><td>18</td><td>18</td><td>164</td></tr><tr><td>C2</td><td>33</td><td>166</td><td>22</td><td>18</td><td>241</td></tr><tr><td>C3</td><td>33</td><td>457</td><td>26</td><td>18</td><td>318</td></tr><tr><td>C4</td><td>33</td><td>1250</td><td>30</td><td>18</td><td>395</td></tr><tr><td>C5</td><td>34</td><td>1986</td><td>36</td><td>18</td><td>471</td></tr><tr><td>D1</td><td>45</td><td>82</td><td>18</td><td>25</td><td>308</td></tr><tr><td>D2</td><td>45</td><td>220</td><td>22</td><td>25</td><td>458</td></tr><tr><td>D3</td><td>45</td><td>599</td><td>26</td><td>25</td><td>608</td></tr><tr><td>D4</td><td>45</td><td>1630</td><td>30</td><td>25</td><td>758</td></tr><tr><td>D5</td><td>46</td><td>2671</td><td>36</td><td>25</td><td>898</td></tr><tr><td>E1</td><td>54</td><td>100</td><td>18</td><td>30</td><td>474</td></tr><tr><td>E2</td><td>54</td><td>265</td><td>22</td><td>30</td><td>705</td></tr><tr><td>E3</td><td>54</td><td>725</td><td>26</td><td>30</td><td>936</td></tr><tr><td>E4</td><td>54</td><td>1986</td><td>30</td><td>30</td><td>1167</td></tr><tr><td>E5</td><td>55</td><td>3237</td><td>36</td><td>30</td><td>1382</td></tr></table>

```txt
Group A: grain  
Group B: grain + corn  
Group C: grain + corn + beet  
Group D: grain + corn + beet + lucerne  
Group E: grain + corn + beet + lucerne + legumes
```

Table 2 shows the characteristics of each case. The tasks for each crop are constant (save for three cases where a new task is added), and the number of resources that are available on the farm are continually increased.

Table 3 shows the model dimensions (after preprocessing) and the computational results. The headings are as follows: m, number of constraints; nc, number of continuous variables; n01, number of 0–1 variables; $Z _ { \mathrm { I P } } ,$ value of the optimal integer solution; nn, number of branch-and-cut nodes; GAP, relative increment of the optimal integer solution value; and T, elapsed time (s).

Table 3  
Computational experiment

<table><tr><td>Code</td><td>m</td><td>nc</td><td>n01</td><td> $Z_{\text{IP}}$ </td><td>nn</td><td>GAP</td><td>T (s)</td></tr><tr><td>A1</td><td>50</td><td>11</td><td>37</td><td>3,392,701</td><td>0</td><td>0.00</td><td>0.00</td></tr><tr><td>A2</td><td>73</td><td>11</td><td>83</td><td>3,249,801</td><td>0</td><td>8.38</td><td>0.04</td></tr><tr><td>A3</td><td>89</td><td>11</td><td>198</td><td>3,155,267</td><td>0</td><td>8.05</td><td>0.11</td></tr><tr><td>A4</td><td>103</td><td>11</td><td>513</td><td>3,142,205</td><td>0</td><td>7.72</td><td>0.36</td></tr><tr><td>A5</td><td>113</td><td>11</td><td>799</td><td>3,137,620</td><td>0</td><td>7.74</td><td>0.69</td></tr><tr><td>B1</td><td>163</td><td>24</td><td>86</td><td>4,979,892</td><td>0</td><td>0.00</td><td>0.04</td></tr><tr><td>B2</td><td>247</td><td>24</td><td>178</td><td>4,789,661</td><td>0</td><td>5.52</td><td>0.16</td></tr><tr><td>B3</td><td>331</td><td>24</td><td>410</td><td>4,656,508</td><td>0</td><td>5.36</td><td>0.81</td></tr><tr><td>B4</td><td>401</td><td>24</td><td>1043</td><td>4,642,074</td><td>4</td><td>5.15</td><td>1.57</td></tr><tr><td>B5</td><td>461</td><td>24</td><td>1617</td><td>4,637,489</td><td>4</td><td>5.15</td><td>3.20</td></tr><tr><td>C1</td><td>286</td><td>33</td><td>140</td><td>5,347,631</td><td>0</td><td>0.00</td><td>0.09</td></tr><tr><td>C2</td><td>445</td><td>33</td><td>255</td><td>5,141,251</td><td>0</td><td>4.79</td><td>0.28</td></tr><tr><td>C3</td><td>599</td><td>33</td><td>550</td><td>4,996,486</td><td>0</td><td>4.69</td><td>1.00</td></tr><tr><td>C4</td><td>733</td><td>33</td><td>1347</td><td>4,981,023</td><td>3</td><td>4.50</td><td>5.49</td></tr><tr><td>C5</td><td>837</td><td>34</td><td>2090</td><td>6,614,765</td><td>0</td><td>3.59</td><td>12.13</td></tr><tr><td>D1</td><td>494</td><td>45</td><td>225</td><td>5,961,335</td><td>0</td><td>0.00</td><td>0.15</td></tr><tr><td>D2</td><td>790</td><td>45</td><td>373</td><td>5,731,854</td><td>11</td><td>4.33</td><td>0.67</td></tr><tr><td>D3</td><td>1106</td><td>45</td><td>756</td><td>5,571,273</td><td>11</td><td>4.25</td><td>4.78</td></tr><tr><td>D4</td><td>1382</td><td>45</td><td>1791</td><td>5,554,095</td><td>15</td><td>4.08</td><td>43.49</td></tr><tr><td>D5</td><td>1516</td><td>46</td><td>2839</td><td>7,179,611</td><td>88</td><td>3.14</td><td>79.49</td></tr><tr><td>E1</td><td>761</td><td>54</td><td>318</td><td>6,319,232</td><td>0</td><td>0.00</td><td>0.27</td></tr><tr><td>E2</td><td>1267</td><td>54</td><td>493</td><td>6,082,104</td><td>57</td><td>4.26</td><td>6.22</td></tr><tr><td>E3</td><td>1681</td><td>54</td><td>957</td><td>5,912,598</td><td>60</td><td>4.16</td><td>16.93</td></tr><tr><td>E4</td><td>2089</td><td>54</td><td>2222</td><td>5,895,420</td><td>83</td><td>3.99</td><td>88.86</td></tr><tr><td>E5</td><td>2341</td><td>55</td><td>3480</td><td>7,520,466</td><td>80</td><td>3.12</td><td>161.35</td></tr></table>

The first observation concerning the results shown in Table 3 is that the GAP is very small, which means that the model developed is very tight. The number of nodes that are required for the cases with enlarged LP fractional solution is also very small. Taken together, this means that the elapsed time is very short. Note that a total of only 2.5 min of CPU time is required on a 300-MHz machine to get and prove the optimal integer solution of case E5, whose dimensions are m = 2341 constraints and n01 = 3480 0–1 variables.

A graph containing the planning of the tasks for case C presented above is shown in Fig. 3.

## 5. Development environment and goals

This research have been supported and validated by ITAP, one of the most advanced Extension Services entity in Spain.

ITAP is a public sector company set up by Albacete Provincial Council (Spain) for the purpose of providing Extension Services in the province. Its activities include the management and use of the land owned by the provincial council, the provision of technical advice for arable and livestock farmers in the province, and agricultural research, especially concerning farming techniques for the most important species of provincial interest.

The ITAP’s activities have gained in importance recently, as the use of the second largest water resource in Spain has promoted the growth of the agricultural sector in the province of Albacete. This has led to a move from extensive farming on large agricultural holdings to intensive farming, bringing with it major changes from both the agronomic and business viewpoint. From the agricultural viewpoint, the appearance of new crops and new production processes is noteworthy. From the business viewpoint, we have a new investment and adaptation to a new farming system.

Operation planning is one of the most important activities performed by the ITAP with regard to both the provision of advice and research concerning the management and running of its own farms.

Farming is now intensive, new-fashioned, and very dynamic. Crops are usually produced on an annual basis. All these mean that new crops and varieties are often introduced every season. This raises questions for farmers: ‘‘Do I have the necessary resources on my farm to perform the operations required to grow the crops that I would like to introduce?’’ ‘‘Do I have enough resources to plant the areas I want to with each crop?’’ If I do not have a resource, should I buy it or is it better to rent it?’’ ‘‘If I buy the resource, what size do I need?’’ ‘‘What profit can I expect?’’

Crops: Casa del Pozo  
![](/api/attachments/YP5SXM2J/fulltext/images/d9247312749f83494f01ea1f998346d5931de15bed9e3414cdb88647692003fb.jpg)  
Fig. 3. Graph containing the planning of the tasks for case C.

As farmers make the decision on what crops to grow and what areas to plant every year, they often approach ITAP for advice on what are the best-suited operations for a crop in view of the characteristics of their farms, the resources required for alternative crops (analysing the programmed tasks), and the costs and benefits associated with these alternatives.

Moreover, as the comparisons between one crop and another are a very important part of the research on new alternative crops conducted by the ITAP at its farms, planning is required so as to get the maximum profitability of the crops for comparison.

The ITAP asked us to develop a decision support system to improve these difficult advisory and research tasks. This was by no means straightforward and called for the knowledge of experts in agriculture (see Refs. [5 –7]), the development of new mathematical models, and an efficient software implementation.

The DSS was designed for use by ITAP engineers. When farmers require advice of any kind, they turn to the centre, where they are attended by engineers individually. Therefore, the tool has to have an interface for inputting and modifying the particulars supplied by the farmer seeking advice. Once these data had been collected and entered, the system had to give a response in a reasonable time, where ‘‘reasonable’’ was defined as the ‘‘time it takes an engineer and a farmer to have a cup of coffee.’’

The system input data are the particulars supplied by the farmer and others provided by the expert engineer depending on the particulars of the farm. These are data about the plots, such as soil type, surface area, crop to be planted; general data about the farm, such as the stock of machinery and available labour force; and a crop plan, including the time windows for each operation and the equipment that can be used for each operation.

The system should first evaluate the cost and the time it takes to perform each operation, depending on the alternatives open depending on farm structure. The goal is to output the resource allocation for each field operation on each plot, as well as the starting and finishing date for each operation, ensuring that the production plan is viable and providing the lowest overall cost. If a resource is missing or the available resources are insufficient for all the operations, they have to be sized and the system should accept different resource compositions to determine which is the optimum policy to be followed.

These are the features of the system we developed: AgriSupport. Appendix A shows part of the data input interface and Appendix C presents a graph showing the results of the planned operations.

The next section focuses on the model developed in AgriSupport, a model enabling medium-term farm planning, i.e., the farm planning to be decided at the beginning of each agricultural year.

## 6. Conclusions and results obtained

The results obtained by developing this system have different implications for the management of the ITAP’s own plots, its advisory tasks, and its research work.

With regard to plot management, the ITAP was pleased to have a tool by means of which to undertake the management of its farms at the start of each season and be able to plan crops every year. One open question, which could lead to cooperation in the future, is the development of a tool that the ITAP could use to deal with the incidents arising in day-to-day operations carried out according to the plan proposed at the start of the season, that is, programming rather than a planning-focused tool.

The ITAP is also very satisfied with the improvement in its advisory service and its image (always excellent) now that it is able to provide a service that farmers were asking for, also giving them the chance to discuss a variety of points concerning the production process and examine the farm’s cost/benefit analysis in detail.

The most popular features of the system are the graphical interface for both entering the data and outputting the report generated and system execution times. As the output is generated in less time than it takes to have a cup of coffee, the system can be run again inputting different configurations.

Appendices A and C show the graphical interface displaying the data input and results presentation. These results include a diagram of the plan output.

As mentioned above, we developed the tool with the idea of providing technical support to the extension services. Now that the ITAP has a website that is often consulted by its clients, the possibility of providing support via Internet is being studied.

At the scientific level, the system provides a model around which all planning revolves and which is the starting point for raising other highly important agronomic research issues, such as integrated planning with irrigation and fertilisation.

## Appendix A. Input data format

The graphical interface displays a screen containing seven main points or sections. The first three points—general data, farm plots, and work schedule—are for entering the input data. The last four points—machinery analysis, task programming, economic analysis and recommendations, and diagnoses—include the results of the analysis after outputting the planning.

Description of the input data and format:

General data:

 Farmer particulars: name, surname, and locality.

 Machinery: the data on tractors and equipment or tools are entered separately. These are data concerning their technical specifications, uses, and costs (Fig. 4).

 Personnel: the characteristics of farm workers, divided into tractor drivers and hands. The input data are the number of each type and their unit cost per hour.

 Others: the other data required in executing the model, including diesel cost and tractor maintenance cost.

Farm plots: the number of plots on the farm, and for each of which the following data should be entered.

 Plot: the basic data of each plot (area, soil composition, and other technical data, such as texture, workability, and depth; Fig. 5).

 Crop: after selecting the crop type for the plot, all the activities that can be performed for this crop appear. Task selection is optional, while the time window and necessary personnel (tractor drivers and hands) have to be inputted for each selected task (Fig. 6).

![](/api/attachments/YP5SXM2J/fulltext/images/af2e44e2533e3ee48849b89bda94259ff84a38e1beff45db1be28d52c5c17bec.jpg)  
Fig. 4. General farm data. Input data screen.

![](/api/attachments/YP5SXM2J/fulltext/images/4f8bb3b50bd78270bffee4c6f1abce2fc29092457c34417c47eab211a04af607.jpg)  
Fig. 5. Plots data. Input data screen.

![](/api/attachments/YP5SXM2J/fulltext/images/d4d480cb7a8e222b79f9249b2a3f6590435eec86e53574731418e6fefd233d9d.jpg)  
Fig. 6. Crops and task operation selections. Input data screen.

Work schedule: the expected number of hours of work per day of the agricultural year is specified in this. These values are loaded automatically (estimated for the climatic conditions of the region), but can be modified if desired.

## Appendix B. Mathematical model

Present below are the parameters, the decision variables, and the mathematical model.

Index sets

I set of tasks, i<sup>a</sup>I

$J _ { i }$ set of modes associated with task $i , j { \in } J _ { i }$

$K$ set of resources, k<sup>a</sup>K

Problem data

$[ r _ { i } , d _ { i } ]$ time window of task i

$l _ { i j }$ length of mode j for performing task i

$c _ { i j }$ cost of mode j for performing task i (it includes the variable cost of using the required resources)

$K _ { i j }$ set of resources assigned to mode j for performing task i

$J _ { i } ^ { k }$ set of modes related to task i that needs resource $k ( j { \in } J _ { i } ^ { k } { \Leftrightarrow } k { \in } K _ { i j } )$

$f _ { k }$ fixed cost of resource k

$G { = } ( I , P )$ graph of direct precedence

$P$ set of arcs $( i _ { 1 } , i _ { 2 } ) ,$ , such that task $i _ { 2 }$ cannot begin before task $i _ { 1 }$ is finished if $( i _ { 1 } , i _ { 2 } ) { \in } P$

Decision variables

$T _ { i }$ date for starting task i

1 if task i is performed under alternative j<sub><</sub> x<sub>ij</sub> ¼ 0 otherwise

$$
y _ {k} = \left\{ \begin{array}{l l} 1 & \text { if   resource   } k \text {   is   used } \\ 0 & \text { otherwise } \end{array} \right.
$$

Incompatibility conditions:

The following conditions, when verified simultaneously, define the incompatibility between tasks $i _ { 1 }$ and $i _ { 2 }$ in the use of resource k:

(I-1) The intersection between the time windows of tasks $i _ { 1 }$ and $i _ { 2 }$ is not empty

(I-2) There are no precedence relationships between tasks $i _ { 1 }$ and $i _ { 2 }$

(I-3) The mode sets $J _ { i _ { 1 } } { } ^ { k }$ and $J _ { i _ { 2 } } ^ { \ k }$ are both nonempty.

The mathematical model is:

$$
\min \sum_ {i \in I} \sum_ {j \in J _ {i}} c _ {i j} x _ {i j} + \sum_ {k \in K} f _ {k} y _ {k}\tag{1}
$$

subject to

$$
\sum_ {j \in J _ {i}} x _ {i j} = 1 \quad \forall i \in I\tag{2}
$$

$$
T _ {i _ {1}} + \sum_ {j \in J _ {i _ {1}}} l _ {i _ {1} j} x _ {i _ {1} j} \leq T _ {i _ {2}} \quad \forall (i _ {1}, i _ {2}) \in P\tag{3}
$$

$$
\sum_ {j \in J _ {i} ^ {k}} x _ {i j} \leq y _ {k} \quad \forall i \in I, k \in K\tag{4}
$$

$$
T _ {i} + \sum_ {j \in J _ {i}} l _ {i j} x _ {i j} \leq d _ {i} \quad \forall i \in I\tag{5}
$$

$$
T _ {i} \geq r _ {i} \quad \forall i \in I\tag{6}
$$

$$
x _ {i j} \in \{0, 1 \} \quad \forall i \in I, j \in J _ {i}\tag{7}
$$

$$
y _ {k} \in \{0, 1 \} \quad \forall k \in K\tag{8}
$$

and the incompatibility constraints for each pair of tasks $( i _ { 1 } , i _ { 2 } )$ and each resource k verifying incompatibility conditions (I-1), (I-2), and (I-3)

$$
\begin{array}{l} T _ {i _ {1}} + \sum_ {j \in J _ {i _ {1}} ^ {k}} l _ {i _ {1} j} x _ {i _ {1} j} - T _ {i _ {2}} \leq (d _ {i _ {1}} - r _ {i _ {2}}) \\ \times \left(3 - \sum_ {j \in J _ {i _ {1}} ^ {k}} x _ {i _ {1} j} - \sum_ {j \in J _ {i _ {2}} ^ {k}} x _ {i _ {2} j} - \delta_ {i _ {1} i _ {2} k}\right) \end{array}\tag{9}
$$

![](/api/attachments/YP5SXM2J/fulltext/images/5ce683d1bf596482ff8251a24b0361b1b58d65910e8e8c2e52abd6c828ad369c.jpg)  
Fig. 7. Task programming. Output data screen.

![](/api/attachments/YP5SXM2J/fulltext/images/65fd8cbd7aea0f5b7fb933ef7416d678419d67c9eea22245c55191876fcafaa5.jpg)  
Fig. 8. Financial analysis. Output data screen.

$$
\begin{array}{l} T _ {i _ {2}} + \sum_ {j \in J _ {i _ {2}} ^ {k}} l _ {i _ {2} j} x _ {i _ {2} j} - T _ {i _ {1}} \leq (d _ {i _ {2}} - r _ {i _ {1}}) \\ \times \left(2 - \sum_ {j \in J _ {i _ {1}} ^ {k}} x _ {i _ {1} j} - \sum_ {j \in J _ {i _ {2}} ^ {k}} x _ {i _ {2} j} - \delta_ {i _ {1} i _ {2} k}\right) \end{array}\tag{10}
$$

$$
\delta_ {i _ {1} i _ {2} k} \in \{0, 1 \}.\tag{11}
$$

The objective function (1) minimises the total cost, which includes the variable cost of performing a task in a certain way and the fixed cost of the resources considered. Condition (2) ensures that each task is performed in a unique way. Condition (3) ensures that the precedence conditions are satisfied. Condition (4) ensures that the fixed cost of all resources used in planning is considered. Conditions (5) and (6) guarantee that each task is completed within its time window. Variables $\delta i _ { 1 } i _ { 2 } k$ are auxiliary and are used to model logical incompatibility constraints like conditions (9) and (10): the incompatibility conditions that prevent tasks using the same resource in the chosen mode from being carried out at the same time.

## Appendix C. Output data format

## 1. Machinery analysis

. Analysis of obsoleteness: the results of the analysis of farm machinery obsoleteness performed by the program are displayed.

. Sizing of replacement machinery: this is the equipment required to cover the field operations that is not available on the farm, because the existing equipment is either insufficient or considered obsolete.

## 2. Task programming

. Plot: The same number of plots as included in the Farm plots will appear (see Appendix A). Each plot includes (a) time diagram: this shows the minimum starting and maximum finishing dates and the starting and finishing dates with the equipment sized by the program; (ii) field operations: these include, for each task, the maximum and minimum execution dates, the real dates with the sized equipment, the equipment necessary for performance, the hours of work required for performance, and the costs of the operation (in terms of personnel and machinery) associated with each work unit (Fig. 7).

3. Financial analysis: this includes an analysis of the costs and a summary for the whole farm (Fig. 8).

## References

[1] K. Darby-Dowman, S. Barker, E. Audsley, D. Parsons, A twostage stochastic programming with recourse model for determining robust planting plans in horticulture, Journal of the Operational Research Society 51 (2000) 83 – 89.

[2] J.B. Dent, G. Edwards-Jones, M.J. McGregor, Simulation of ecological, social and economic factors in agricultural systems, Agricultural Systems 49 (4) (1995) 337 – 351.

[3] G. Fokkens, R.J. Puylaert, A linear programming model for daily harvesting operations at the large-scale grain farm of the Ijsselmeerpolders Development Authority, Journal of the Operational Research Society 32 (1981) 535 – 547.

[4] M.T. Ortun˜ o, B. Recio, B. Vitoriano, Modelizacio´ n del Problema de Planificacio´n y Asignacio´n de Recursos para una explotacio´ n agraria, Investigacio´n Operacional 19 (1998) 116– 127.

[5] B. Recio, Sistema de Soporte a la Decisio´n para la Planificacio´n de Operaciones de Cultivo, Aplicacio´n al cultivo del trigo en Navarra, PhD thesis, ETSI Agro´nomos, Universidad Polite´cnica de Madrid, 1992.

[6] B. Recio, F. Rubio, AgriSupport: a knowledge based decision support system for farm planning, Proceedings of AIFA Conference, 1993, pp. 349 – 358.

[7] B. Recio, F. Rubio, L. Marquez, AgriSupport II: a decision tool to support the extension services, European CIGR Congress, 1994, pp. 114 – 122.

[8] F. Rubio, Paradigma de planificacio´n avanzada empleando te´cnicas de propagacio´n de restricciones: aplicacio´n al sector agrario/agroalimentario, PhD thesis, ETSI Telecomunicaciones, Universidad Polite´cnica de Madrid, 2000.

[9] J. Van Elderen, Heuristic Strategy for Scheduling Farm Operations, Centre for Agricultural Publishing and Documentation, PUDOC, Wageningen, 1977.

[10] J. Van Elderen, Scheduling of Field Operations, Bayer, Landwirtsch, 1981.

[11] J. Van Elderen, Scheduling Farm Operations: A Simulation Model, PUDOC, Wageningen, 1987.

[12] B. Vitoriano, M.T. Ortun˜ o, B. Recio, F. Rubio, A. Alonso, Two alternative models for farm management: discrete versus continuous time horizon, European Journal of Operation Research. Accepted Nov. 2001.

[13] P.J.M. Wijngaard, A comparison of operational research techniques for scheduling problem, XXIInd Congress of International Committee of Work Study and Labour Management in Agriculture (CIOSTA/CIGR V), BRD, Stuttgart, 1986, pp. 152 – 158.

[14] P.J.M. Wijngaard, Scheduling Models in Farm Management: A New Approach, 1998, Wageningen.

![](/api/attachments/YP5SXM2J/fulltext/images/f83d244a7cc19affd3359600ab8af0e95bd30eb32b62227c22fbc49ad398012b.jpg)  
Beatriz Recio is a professor in the Department of Mathematics and Information Technology applied to Agricultural Engineering at Universidad Polite´cnica de Madrid. Her research interests include farm management, management information systems, and decision support systems.

![](/api/attachments/YP5SXM2J/fulltext/images/ee2a060cdcbe2636873cd601cc4d89eb89aaadfeca393ed33fbfbe8aeceead4a.jpg)  
Jose Antonio Criado is now finishing his PhD in intelligence decision support system for farm planning. His primary scientific interest lies in the application of the Internet to support decision support systems in agriculture.

![](/api/attachments/YP5SXM2J/fulltext/images/9ab84d12c603f0710658b766c65e539bff215aab8a5a2e2608ba6331d306e6cb.jpg)  
interests include e-commerce and decision support systems.

Fernando Rubio has PhD in Computer Science and he is involved in advanced system implementations in such areas as transportation, industry, and business. He has been working as a manager for the EEC and provides advanced technology solutions to firms such as Texas Instruments and Andersen Consulting. Currently, he teaches business and computing and maintains a fruitful research line in the Universidad Polite´cnica de Madrid. His research
