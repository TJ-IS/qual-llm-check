---
otero_id: 5748
otero_key: "FWKFBDDD"
title: "A DSS for bicriteria location problems"
authors: "Sérgio Fernandes; M. Eugénia Captivo; João Clímaco"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.09.014"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A DSS for bicriteria location problems

Sérgio Fernandes <sup>a,b,</sup>⁎, M. Eugénia Captivo <sup>c,b</sup>, João Clímaco <sup>d,e</sup>

<sup>a</sup> Escola Superior de Tecnologia — Instituto Politécnico de Setúbal, Campus do IPS, Estefanilha, 2910-761 Setúbal, Portugal

<sup>b</sup> Centro de Investigação Operacional, Faculdade de Ciências — Universidade de Lisboa, Bloco C6, Piso 4, Campo Grande, 1749-016 Lisboa, Portugal

<sup>c</sup> Faculdade de Ciências — Universidade de Lisboa, Campo Grande, 1749-016 Lisboa, Portugal

<sup>d</sup> Faculdade de Economia — Universidade de Coimbra, Av. Dias da Silva, 165, 3004-512 Coimbra, Portugal

<sup>e</sup> Instituto de Engenharia de Sistemas e Computadores de Coimbra, Rua Antero de Quental, 199, 3000-033 Coimbra, Portugal

## a r t i c l e i n f o

Article history: Received 14 February 2013 Received in revised form 9 September 2013 Accepted 10 September 2013 Available online xxxx

Keywords: Bicriteria location models GIS Multiattribute analysis Waste transfer station siting

## a b s t r a c t

In this paper, we present a new interactive decision support system (DSS) – named SABILOC – in action. The DSS is aimed at supporting decision-making concerning bicriteria location models and it was specially designed to deal with problems in which the facilities to be located have environmental impacts. We point out three advantages of SABILOC when compared with other DSS for location problems available in the literature. Firstly, an interactive procedure is used allowing the decision-maker to obtain non-dominated solutions for bicriteria location models. Secondly, a multiattribute analysis module allows the decision-maker to proceed with a more detailed analysis of a subset of solutions selected from the <sup>fi</sup>rst interactive phase. Finally, the embedment of a Geographic Information System into SABILOC makes the system much more useful in real world location problems. In order to better describe and validate the potentialities and functionalities of SABILOC, we present a case study of a real world problem applied to waste transfer station siting.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

In traditional location problems, the aim is to obtain the best way to satisfy multiple stakeholders by assigning facilities with known locations. This implies the need to determine the number and location of facilities to be installed, and the allocation of the demand points to the installed facilities in order to maximize their effectiveness and ef<sup>fi</sup>ciency. In case the facilities to be located have environmental implications, then it is also intended to minimize their negative impact on the communities. Depending on the problem, it is possible that we have also to decide about other characteristics, like the size or capacity of each facility and the type of facilities regarding single/multicommodities.

The type of optimality criterion depends on the nature of the activities or of the equipment to be installed. Considering desirable facilities, such as warehouses, service and transportation centers, and emergency services, the typical objectives are based on the minimization of distances between facilities and populations. However, there is another kind of situation in which the population desires services far away, but keeping accessibility, in order to preserve the area's quality of life. Examples of such services are sanitary land<sup>fi</sup>lls, waste transfer stations, incinerators, airports, prisons or chemical plants. In general, any type of facility with environmental impacts falls into this category. The growing interest in environmental issues is due in part to concerns highlighted by people who naturally are more aware of possible negative effects that installing certain services can bring to their lives than the possible positive effects. As a result, population usually represented by several environmental organizations requires certain environmental actions by the government, giving rise to new legislation that imposes minimum levels of quality, maximum levels of acceptable degradation and certain prohibition directives.

A location model to be applicable in a real world problem, particularly for location of undesirable facilities, must take into account many types of location constraints. As already mentioned before, regional planning rules for land-use and laws just allow such facilities in speci<sup>fi</sup>c areas, even forbidding their location in the vicinity of some places. The morphology of the potential locations and/or meteorological conditions may rule out other areas. Another consideration to take into account, that can in<sup>fl</sup>uence the choice of the site to install an undesirable facility, is the negative impact of transporting hazardous materials to or from these places in populated or environmentally sensitive areas, whether by the risk of accident or simply by the increase in traf<sup>fi</sup>c. Because of the generic features of Geographic Information Systems (GIS), including the visual potentialities and the easy way of manipulating different kinds of data from various sources, like business data and geographic data (road networks, land use information, census data, etc.), GIS may be a signi<sup>fi</sup>cant aid in assisting traditional Operational Research (OR) location models. In particular, when the facilities to be located have environmental impacts, usually depending on several meteorological and geomorphologic factors, a previous organization of model input data could be more easily evaluated with a GIS. According to literature reviews found in Church [7], Malczewski [30] and Murray [33], we can con<sup>fi</sup>rm that despite all the advantages that a GIS may offer to traditional OR location problems, in particular when it is intended to locate undesirable facilities, it is not usual to <sup>fi</sup>nd papers that combine both subjects.

S. Fernandes et al. / Decision Support Systems xxx (2013) xxx–xxx  
![](/api/attachments/FWKFBDDD/fulltext/images/c524baba19788ff6f6396a7bd894d2801b4deea61846739713b210c79175237f.jpg)  
Fig. 1. GIS page of SABILOC.

In the past, the environmental issues on the approaches to locate undesirable facilities were formulated as constraints or addressed by a surrogate criterion (like distance) on a single objective framework. However, single objective models cannot be expected to accurately represent problems of this type (Erkut and Neuman [13]). The modeling of relevant environmental issues as criteria, instead of constraints, with the use of appropriate techniques (for example interactive methods) generates certainly more information for decision-makers, providing a better understanding of the problem characteristics. Nowadays, it is well accepted that most location problems, particularly those that deal with undesirable facilities, are inherently multicriteria. This trend is due to the fact that reality is multi-dimensional and therefore, realworld problems are naturally formulated using multiple criteria, in general con<sup>fl</sup>icting.

Rarely there is a feasible solution which optimizes all the criteria simultaneously. If such solution exists, then there is no con<sup>fl</sup>ict between the criteria and the solution is optimal. On the other hand, if there is con<sup>fl</sup>ict then the concept of non-dominated or Pareto optimal solution (Pareto [34]) in multicriteria theory, is essential. The concept of dominance is important since the decision-maker intends to choose just one <sup>fi</sup>nal compromise solution, which should be ef<sup>fi</sup>cient taking into account the criteria considered. Thus, it is necessary that the decisionmaker's preferences somehow intervene in the search process for a <sup>fi</sup>nal solution, enabling decision-making.

The methods and procedures by which multiple criteria can be formally incorporated into a decision-making process are part of the general <sup>fi</sup>eld of knowledge Multiple Criteria Decision Making (MCDM).<sup>1</sup> Interactive methods are, in general, the best choice, especially if they are designed as learning oriented, improving the knowledge about the problem. These methods have been developed to deal with multiobjective problems considering, on one hand, different ways to interact with the decision-maker and to guide the decision process and moreover, different methodologies for obtaining solutions. Interactive methods should allow that the decision-maker's preferences might be partially modi<sup>fi</sup>ed and contradictory; being the decision-maker the responsible for <sup>fi</sup>nishing the interactive process when he/she feels satis<sup>fi</sup>ed with one of the solutions found. While in some situations an interactive process for multiobjective optimization problems makes possible to opt for one alternative, in many others, it just enables the elimination of a great part of the feasible solutions thence reducing the <sup>fi</sup>nal choice to a small number of the non-dominated ones. In this case, the reduced set of alternatives (known explicitly) should be analyzed through a multiattribute a posteriori decision analysis tool.

In this paper, we present a new interactive DSS, named SABILOC, developed to support decision-making concerning bicriteria location models (some preliminary and partial versions can be found in Fernandes et al. [16–18], Captivo et al. [5]). As we will see, the system was specially designed to deal with problems in which the facilities to be located have environmental impacts. The advantages of the SABILOC DSS, comparatively with others existent in the literature, can be pointed out as:

![](/api/attachments/FWKFBDDD/fulltext/images/973a636f402c3ffe3665d20141c6356e9bfa4acab6a8592b3a5d97cc6c90033b.jpg)  
Fig. 2. Flowchart of the general framework of the interactive method.

1) The direct embedment of a GIS into SABILOC makes the system much more useful in real world location problems. The embedment has, at least, two obvious advantages in this type of problems. First, by manipulating the GIS tools, it is possible to select initial potential sites to locate the service(s). After this <sup>fi</sup>rst analysis, the candidate sites can be used at a later stage of the DSS. Another advantage corresponds to the possibility of obtaining relevant data for the location models, especially those considering environmental concerns. Because a GIS provides ef<sup>fi</sup>cient manipulation and presentation of data, this embedment turns SABILOC into a powerful tool at supporting decision-making in location problems.

2) A <sup>fi</sup>rst interactive phase, based on a combinatorial optimization procedure, allows the decision-maker to obtain, in a progressive and participatory way, any non-dominated solution of the implemented bicriteria location models. The bicriteria model in general, due to its special structure, is an important particular case in multicriteria optimization, presenting some advantages either graphical or computational. The methods proposed for problems with two objective functions are sometimes referred to as limited. They only address two criteria when often the real problems are characterized by multiple criteria due to the multidimensionality of reality. But actually we may ask if these problems should be faced with complicated modeling, in which several criteria try to accurately represent reality. Moreover, often the decision-maker's goals are not well de<sup>fi</sup>ned, not allowing an appropriate formulation of the model to be used in the decision process. According to Bana e Costa [4], simplicity and interactivity should be the thrust of supporting decision-making, in order to open doors to participation and learning. In the context of multicriteria optimization and in a <sup>fi</sup>rst phase, considering models with only two objective functions enables the simplicity and interactivity required at decision-making. For example, the case study we will present corresponds to a location problem for selecting the sites to locate waste transfer stations, and this one can have advantages if it is approached as a bicriteria location model. The two con<sup>fl</sup>icting criteria can be the maximization of facilities' ef<sup>fi</sup>ciency and effectiveness, and the minimization of their negative impact on the communities.

3) An interactive multiattribute analysis module of SABILOC allows the decision-maker to proceed with a more detailed analysis of a subset of compromise alternatives selected from the <sup>fi</sup>rst interactive phase. The analysis is based on the evaluation of each of those alternatives regarding now a set of additional criteria. These last ones are subdivided into four groups representative of obnoxious effects, accessibility, costs and equity. Thus, this second phase allows the procedure to bridge a possible limitation of the <sup>fi</sup>rst interactive phase, due to the fact that we have considered only the two most important criteria. The multiattribute analysis module basically stands for an interactive implementation of a version of the conjunctive method making use of a radar chart. Several tools are available in the module.

![](/api/attachments/FWKFBDDD/fulltext/images/bb4e792d16630cc6d11d8a5ab2b184851fb5629628c1cb0e97b2c460be1d2b50.jpg)  
Fig. 3. Graphical representation of the objective space considering two criteria of minimization.

Please cite this article as: S. Fernandes, et al., A DSS for bicriteria location problems, Decision Support Systems (2013), http://dx.doi.org/10.1016/ j.dss.2013.09.014

In the next section, we present the bicriteria location models already implemented in SABILOC. In Section 3, we review relevant literature, with special emphasis on multiobjective location problems concerning environmental impacts and regarding GIS technology. In Sections 4, 5 and 6, we detail the advantages of SABILOC, which we just pointed out in the Introduction. In Section 7, we present a case study in which it is intended to locate waste transfer stations in part of Setúbal district in Portugal. Section 7 is subdivided into three subsections: Preprocessing data and First and Second interactive phases. In Section 8, some conclusions are presented.

## 2. Implemented bicriteria location models

The basic bicriteria location model that is the object of this study can be formulated as: BSPLP (Bicriteria Simple Facility Location Problem)

$$
\min F _ {1} = \sum_ {j \in J} \sum_ {i \in I} l _ {i j} x _ {i j} + \sum_ {j \in J} h _ {j} y _ {j}\tag{1}
$$

$$
\min F _ {2} = \sum_ {j \in J} \sum_ {i \in I} r _ {i j} x _ {i j} + \sum_ {j \in J} g _ {j} y _ {j}\tag{2}
$$

$$
s. t.: \sum_ {j \in J} x _ {i j} = 1 \quad \forall i \in I\tag{3}
$$

$$
y _ {j} \geq x _ {i j} \quad \forall i \in I, \forall j \in J\tag{4}
$$

$$
y _ {j} \in \{0, 1 \} \quad \forall j \in J\tag{5}
$$

$$
x _ {i j} \in \{0, 1 \} \quad \forall i \in I, \forall j \in J\tag{6}
$$

where I is the set of clients or communities to be served; J is the set of potential service locations; h and g are the costs or representative values of opening service at site $j ; l _ { i j }$ and $r _ { i j }$ are the costs or representative values from assigning service at site j to client i; the decision variables are de<sup>fi</sup>ned as: $y _ { j } = 1$ if service at site j is opened and 0 otherwise; $x _ { i j } = 1$ if client/ community i is assigned to service at site j and 0 otherwise. Constraint (3) assures that every client or community is assigned to some service, whereas constraint (4) prevents assignments to closed services.

The structure of the objective function (1) or (2) is simple and <sup>fl</sup>exible enough to be easily understood by the users and to give it different meanings depending on the intentions. For example, the objective function could represent total costs, total risk or environmental impact resulting from open services and transportation between communities and services. There are several examples in the literature (Hultz et al. [24], Revelle and Laporte [36], Ross and Soland [37]) where we can <sup>fi</sup>nd different meanings for this objective function structure.

![](/api/attachments/FWKFBDDD/fulltext/images/d15083d169291f128e92466304269d32eb67caff1f0e4bc7bf75fbb8538a5621.jpg)  
Fig. 4. Dialog box that allows the decision-maker to de<sup>fi</sup>ne the parameters of the search.

![](/api/attachments/FWKFBDDD/fulltext/images/4162a478bd2ef95c61c34dc37efb50d823688d93568b98b0a39117615d346bc8.jpg)  
Fig. 5. Objective space displaying the two lexicographic optima, the ideal point and two non-dominated solutions. Eliminated areas.

Nowadays, the bicriteria location models implemented in SABILOC are four: the simple facility location (Krarup and Pruzan [28]), the p-facility location (Cornuejols et al. [8]), the capacitated location

List of criteria included in the multiattribute a posteriori analysis module of SABILOC to describe the performance of the alternatives.

<table><tr><td> $\sum_{j\in S}\sum_{i\in I}\frac{1}{d_{ij}}a_i$ </td><td>Obnoxious effect produced on communities by the installed equipments (inversely proportional to the Euclidian distance).</td><td>Crit. 1</td></tr><tr><td> $\sum_{j\in S}\sum_{i\in I}\frac{1}{d_{ij}^2}a_i$ </td><td>Obnoxious effect produced on communities by the installed equipments (inversely proportional to the square of the Euclidian distance).</td><td>Crit. 2</td></tr><tr><td> $\max_{i\in I}\sum_{j\in S}\frac{1}{d_{ij}}a_i$ </td><td>Maximum obnoxious effect produced on any community by the transfer stations and the existing landfills.</td><td>Crit. 3</td></tr><tr><td> $\max_{j\in S}\sum_{i\in I}\frac{1}{d_{ij}}a_i$ </td><td>Maximum obnoxious effect produced by some transfer station or some landfill on all communities.</td><td>Crit. 4</td></tr><tr><td> $\min_{i\in I,j\in S}d_{ij}$ </td><td>Minimum (Euclidean) distance between any community and any transfer station or landfill.</td><td>Crit. 5</td></tr><tr><td> $\sum_{j\in S}\sum_{i\in I}a_ic_{ij}x_{ij}$ </td><td>Total sum of distances (shortest path) between transfer stations or landfills, and the communities assigned to each equipment.</td><td>Crit. 6</td></tr><tr><td> $\max_{i\in I,j\in S}c_{ij}x_{ij}$ </td><td>Maximum distance (shortest path) between transfer stations or landfills and the communities assigned to each equipment.</td><td>Crit. 7</td></tr><tr><td> $\sum_{j\in S}h_j$ </td><td>Total sum of fixed costs (for opening or maintenance) of the installed equipments (objective function 1).</td><td>Crit. 8</td></tr><tr><td> $\sum_{j\in S}g_j$ </td><td>Total sum of fixed costs (for opening or maintenance) of the installed equipments (objective function 2).</td><td>Crit. 9</td></tr><tr><td> $\sum_{j\in S}\sum_{i\in I}l_{ij}x_{ij}$ </td><td>Total sum of assignment/transportation costs of communities to the installed equipments (objective function 1).</td><td>Crit. 10</td></tr><tr><td> $\sum_{j\in S}\sum_{i\in I}r_{ij}x_{ij}$ </td><td>Total sum of assignment/transportation costs of communities to the installed equipments (objective function 2).</td><td>Crit. 11</td></tr><tr><td> $\sum_{j\in S}\sum_{i\in I}q_if_jx_{ij}$ </td><td>Total sum of service costs of the installed equipments.</td><td>Crit. 12</td></tr><tr><td> $\frac{\sum_{i\in I}\sum_{h\in I}|E_{i(x)}-E_{h(x)}|}{2N^2\overline{E}_{(x)}}$ </td><td>Gini coefficient relative to total obnoxious effect.</td><td>Crit. 13</td></tr><tr><td> $\frac{1}{2N}\sum_{i\in I}\left|\frac{E_{i(x)}}{\overline{E}_{(x)}}-\frac{a_i}{\overline{a}}\right|$ </td><td>Hoover coefficient relative to total obnoxious effect.</td><td>Crit. 14</td></tr><tr><td> $\frac{\sum_{i\in I}\sum_{h\in I}|E_{i(x)}-E_{h(x)}|}{2N^2\overline{E}_{(x)}}$ </td><td>Gini coefficient relative to total accessibility.</td><td>Crit. 15</td></tr><tr><td> $\frac{1}{2N}\sum_{i\in I}\left|\frac{E_{i(x)}}{\overline{E}_{(x)}}-\frac{a_i}{\overline{a}}\right|$ </td><td>Hoover coefficient relative to total accessibility.</td><td>Crit. 16</td></tr></table>

Please cite this article as: S. Fernandes, et al., A DSS for bicriteria location problems, Decision Support Systems (2013), http://dx.doi.org/10.1016/ j.dss.2013.09.014

S. Fernandes et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/FWKFBDDD/fulltext/images/58cbf7da7e7aa7b9e6cfe2f35c401ea7c3cda21779dc8ba38df9c210cfbb5be5.jpg)  
Fig. 6. Adding a new criterion.

![](/api/attachments/FWKFBDDD/fulltext/images/7faae33fd43aa1c0cdebbea11af5c6806c83776542e0632346a9ece421d83530.jpg)  
Fig. 8. Inactivating alternatives and criteria.

(Guignard and Spielberg [22]) and the modular location (Correia and Captivo [9]). All of them keep a similar structure of objective functions (1) and (2). Note that, due to the fact that the system was developed in a modular way, the insertion of more models and/or procedures to solve them, is simple.

![](/api/attachments/FWKFBDDD/fulltext/images/6ceb52ca13cc9745b5f6f510d9b4821ad651134ba12d8581d5f3ca18e66a8e89.jpg)  
Fig. 7. Multiattribute analysis page of SABILOC.

![](/api/attachments/FWKFBDDD/fulltext/images/377ec253e7679a3ba147816121ecae7871ce0fbe4cff87e2aa8a4da06dcf881c.jpg)  
Fig. 9. Intervention areas and infrastructures of AMARSUL. Legend: (1) recycling collection center; (2) sanitary land<sup>fi</sup>ll; (3) waste transfer station; (4) biogas recovery plant; (5) mechanical treatment unit; (6) refuse derived fuel production unit; (7) sorting center; (8) aerobic mechanical biological treatment center; (9) anaerobic digestion mechanical biological treatment center.

## 3. Literature review

The literature review presented below is based on the conjugation of the following topics, which were considered relevant to this study: location science, environmental concerns, multicriteria and GIS.

Many of the recent papers using GIS to analyze the most suitable site, usually do it in a raster<sup>2</sup> environment. Roughly speaking, the map layers<sup>3</sup> serve as criteria (all of them must be in a common scale); they are weighted according to a value of in<sup>fl</sup>uence, and combined to produce a <sup>fi</sup>nal map displaying suitable locations. For example, Wang et al. [45] and Sener et al. [38,39] use this type of procedure to site sanitary land<sup>fi</sup>lls. The raster data usually used on location analysis include the distance to points of interest (like other facilities already established, roads and clients/suppliers) and, meteorological and geomorphologic characteristics (e.g. slope of the terrain, land-use and wind). Some studies on competitive location problems use attraction functions, for example based on Huff [23] model (Suárez-Vega et al. [42]).

The process of combining data layers, in general raster graphics, each weighted by some factor, in an adequate way was one critical barrier on these studies in the past. Nowadays, it can be easily accomplished in some GIS applications, as integrant part or as external module. However, as noted by Malczewski [30], the simplicity of the weighted sum and related methods makes them often used without full understanding of the assumptions underlying the approach. Furthermore, the method is often applied without full insight into the meanings of two critical elements of the weighted sum model: the weights assigned to attribute maps and the procedures for deriving commensurate attribute maps. As it is known, the results of analysis can dramatically change depending on the used weights and the standardization methods applied to map layers. Many references to existing works that form the interface between GIS and Location Science can be found in the complete Church [7] review and, in the more recent review, by Murray [33]. The capability of a GIS to analyze raster data can be used to <sup>fi</sup>lter unacceptable places to install services. However, to determine the best locations, besides the manipulation of raster data, other operational tools must be taken into account. As mentioned by Church [7], some siting studies tend to present their results as optimal, under the assumption that the optimal sites are those that have the highest value of the suitability index. That is, they present their results as ‘optimal’ even though there is no ‘formal’ optimization model. Such misconceptions are somewhat common in the GIS literature. In order to make the multicriteria techniques more accessible to GIS users, analysts and researchers, and ultimately experts and decision-makers in many <sup>fi</sup>elds, Greene et al. [21] provide a complete and simple overview of the background and methods of multicriteria decision analysis and its spatial extension using GIS.

Using multiobjective mixed-integer programming, Wyman and Kuby [46,47] present a model for the location of hazardous material facilities with three objective functions (cost, risk and equity). To represent process-related risk accurately, Gaussian atmospheric dispersion techniques were used to plot a pollution plume for projected facility capacities. Falit-Baiamonte and Osleeb [15] develop a biobjective integer location model to locate environmentally hazardous facilities where risk and equity are considered. The equity objective explicitly considers both the existing distribution of undesirable facilities as well as new facilities that are to be located and. for that, a GIS is used to obtain relevant data. Alçada-Almeida et al. [2] present a multiobjective approach to locate emergency shelters and identify evacuation routes in urban areas. The multiobjective model is incorporated into a GIS-based decision support system. Using the same GIS-based interactive decision support system, Alçada-Almeida et al. [1] propose a multiobjective mixed-integer programming approach to identify the locations and capacities of hazardous material incineration facilities. The approach incorporates a Gaussian dispersion model to determine the geographical distribution of the impacts resulting from an accident or <sup>fi</sup>lter malfunction at each of the potential locations. Also based on the previous decision support system, Tralhão et al. [43] present a multiobjective approach to locate multi-compartment containers for urban-sorted waste.

Without using GIS technology, Kirca and Erkip [27], Gil and Kellerman [20] and, Rahman and Kuby [35] intend to locate waste transfer stations. Kirca and Erkip [27] propose a general mathematical programming approach with four stages to determine the locations of transfer stations. The main motivation for having multiple stages is to allow the decisionmaker(s) to participate in the process. The <sup>fi</sup>rst two stages correspond to the validation and preparation of the available data. The third stage intends to obtain the solution of a capacitated location model, where the objective function corresponds to the minimization of transportation costs (proportional to the Euclidean distance and amount transported). The last stage corresponds to the implementation of the results of the static location problem over the time horizon. Gil and Kellerman [20] present a very simple multicriteria model for the location of waste transfer stations. Each of the <sup>fi</sup>ve sets of criteria and each speci<sup>fi</sup>c criterion are ranked ordinally and then the potential sites are rated according to each criterion. According to the authors, adding up all the criteria grades for all the sites reveals the best site. In Rahman and Kuby [35], a multiobjective model examines the tradeoffs between minimizing costs and public opposition. The cost objective function combines the transshipment and the <sup>fi</sup>xed-charge problems, while expected public opposition is modeled as a decreasing function (derived empirically from opinion survey data) of distance from the waste transfer station.

![](/api/attachments/FWKFBDDD/fulltext/images/be976cfc72bab2d4f7440a62607bda0a483ab73f44a7dd16b7dfed1d6d37a7e2.jpg)

<table><tr><td colspan="2"></td><td>1996</td><td>1997</td><td>1998</td><td>1999</td><td>2000</td><td>2001</td><td>2002</td><td>2003</td><td>2004</td><td>2005</td></tr><tr><td>(1)</td><td>Estações de Transferência</td><td>1</td><td>2</td><td>13</td><td>23</td><td>41</td><td>54</td><td>67</td><td>75</td><td>75</td><td>78</td></tr><tr><td>(2)</td><td>Centrais de Triagem</td><td>1</td><td>1</td><td>4</td><td>11</td><td>14</td><td>18</td><td>22</td><td>23</td><td>25</td><td>26</td></tr><tr><td>(3)</td><td>Aterros</td><td>13</td><td>18</td><td>28</td><td>32</td><td>34</td><td>38</td><td>37</td><td>35</td><td>34</td><td>33</td></tr><tr><td>(4)</td><td>Unidades de Incineração com Recuperação de Energia</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>(5)</td><td>Unidades de Valorização Orgânica</td><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td><td>5</td><td>5</td><td>6</td><td>7</td><td>8</td></tr></table>

Fig. 10. Number of waste management infrastructures in Portugal between 1996 and 2005. Legend: (1) waste transfer stations; (2) sorting centers; (3) land<sup>fi</sup>lls; (4) incineration units with energy recovery; (5) anaerobic digestion mechanical biological treatment units.

Chatzouridis and Komilis [6] present a methodology to optimally site and design municipal solid waste transfer stations using a GIS and single objective binary programming. First, the proposed methodology designates the location of all candidate waste transfer stations using GISbased siting approaches. Next, a single objective model minimizing total solid waste collection cost is developed in an Excel spreadsheet.

Lotov et al. [29] present a different approach from those presented above. The authors present a visualization technique for the Pareto frontier, so-called interactive decision maps technique, in the case of more than two objective functions. This technique intends to generate a representation of the Pareto frontier, using several decision maps, and to present it to the decision-maker. This one only has to specify a preferred

![](/api/attachments/FWKFBDDD/fulltext/images/e0b79fb0b479350fca7bad0e74053737a4a35b89aae97574e94abaedcdddcb50.jpg)  
Fig. 11. Mask prepared for a previous selection of potential sites to locate waste transfer stations. (For interpretation of the references to color in this <sup>fi</sup>gure, the reader is referred to the web version of this article.)

Please cite this article as: S. Fernandes, et al., A DSS for bicriteria location problems, Decision Support Systems (2013), http://dx.doi.org/10.1016/ j.dss.2013.09.014

combination of objective values (goal) directly on one of the decision maps. Then, the information is used to determine one or a small number of solutions that are in line with the identi<sup>fi</sup>ed goal. A GIS displays the selected solutions.

## 4. Embedment of a GIS into SABILOC

Nowadays, there is a vast offer of GIS desktop applications on the market. A common feature to all of them is the possibility of manipulating map layers in order to partially describe the world. By displaying a set of logic map layers with the ability to manage the overlays of layers on top of each other, a GIS gives us a map view that geographically characterizes any place of the world. An added-value of a GIS application consists in offering distinct and particular modules which allow users to extend the software analysis capabilities through special data handling. Usually, but not necessarily, these modules are grouped by areas of analysis, such as space, networks and statistics.

Due to the advantages already mentioned in the Introduction, we decided to embed a GIS into SABILOC. We used ArcGIS Engine platform (version 9.3.1) by ESRI — Environmental Systems Research Institute [14], and the developer API (Application Programming Interface) adopted was Microsoft COM (Component Object Model) technology. The basic structure of SABILOC corresponds to a folder with several pages, which can vary depending on the model chosen. All of them have the GIS page (Fig. 1). This page allows us to open an ArcMap document or to add dataset and layers data, just like the ArcMap software.

We are especially interested in two ArcGIS application extensions: Spatial Analyst and Network Analyst. The Spatial Analyst extension provides a broad range of spatial modeling and analysis features. This extension (version 9.3.1 of ArcGIS) allows users to: analyze surfaces (Slope, Aspect, Contour, Cut/Fill, Hillshade, Viewshed), analyze distances (Euclidean Distance, Euclidean Allocation, Euclidean Direction, Cost Distance, Cost Allocation, Cost Back Link, Cost Path), convert data, apply conditional operations, predict density (Point Density, Line Density, Kernel Density), extract data, interpolate data, reclassify data and operate raster data (Map Algebra). Map Algebra is the analysis language for Spatial Analyst. It is extremely important, since it allows most of the features listed above to be executed. Operations can be done by applying the functions listed above and elementary mathematical functions (e.g. sine, power, and logarithm) on cell's values, and combine the results through arithmetical, bitwise, combinatorial, logical and relational operators. Map Algebra operations can be performed by using the Raster Calculator tool. The Network Analyst extension provides a framework for networkbased spatial analysis, including routing, travel directions, closest facilities, service area and origin–destination cost matrix considering several restrictions. For a more complete and detailed study of all these extensions' capabilities, please refer to the ArcGIS Desktop help website [14].

In this way, we can use the embedded GIS to obtain relevant data for the location models, especially those considering environmental concerns. Fernandes et al. [17] give an example to illustrate the advantages of using the Spatial Analyst extension. The Gaussian plume model was adopted to map potential concentrations of nonreactive pollutants, resulting from the potential installation of an industrial plant. Using the adequate parameters, a variant of this model can also be used to predict the level of odor downwind from the odor source. For example, multiplying model results by the number of inhabitants in the area, we obtain a good indicator of the obnoxious effect of odor on communities. Both Spatial Analyst and Network Analyst extensions have also been important to analyze the potentially negative impacts of transporting unwelcome materials in populated or environmentally sensitive areas. The increasing number of publications using this technology for decision-making in hazardous material transportation problems

![](/api/attachments/FWKFBDDD/fulltext/images/bfb57640a1d74161c5b09988532e552818dad3b70c904a2d2f5daeddfb1631a4.jpg)  
Fig. 12. GIS page with the shortest path example.

Please cite this article as: S. Fernandes, et al., A DSS for bicriteria location problems, Decision Support Systems (2013), http://dx.doi.org/10.1016/ j.dss.2013.09.014

shows it (Zografos and Androutsopoulos [49], Zhang et al. [48], Kim et al. [26]).

With the embedded GIS, SABILOC also allows us to preprocess data in order to obtain initial candidate sites for using in location models. For example, as we will see in the case study, by combining raster layers, each weighted by some factor, and choosing the sites with maximum value of suitability and total area not less than a certain value, we can obtain the set of potential sites to install the facilities.

## 5. Combinatorial optimization interactive procedure

To deal with the bicriteria location models implemented in SABILOC, we believe that learning oriented interactive methods are the best choice. The number of non-dominated solutions of such models can grow signi<sup>fi</sup>cantly given the problem size. In case of a real problem, the characterization of the set of ef<sup>fi</sup>cient solutions can generate excessive amounts of information dif<sup>fi</sup>cult to be analyzed by a decisionmaker. The learning oriented interactive methods are especially important in these problems because, as mentioned, determining all ef<sup>fi</sup>cient solutions does not seem to be practicable nor an easy task.

The interactive process intrinsic to SABILOC is based on Ferreira et al. [19]. In this interactive method, the decision-maker has an active rule in the process for calculating new non-dominated solutions. However, it is not too demanding regarding the information required from him/her. There are no irrevocable decisions throughout the interactive process and it only stops when the decision-maker <sup>fi</sup>nds one satisfactory solution or feels, at least, satis<sup>fi</sup>ed with the knowledge obtained about the problem. The general framework of the interactive method is presented as a <sup>fl</sup>owchart in Fig. 2.

Initially, SABILOC computes the two lexicographic optima $\mathsf { S } _ { 1 } =$ $( \mathsf { F } _ { 1 } ^ { \operatorname* { m i n } } , \mathsf { F } _ { 2 } ^ { \operatorname* { m a x } } )$ and ${ \sf S } _ { 2 } = ( { \sf F } _ { 1 } ^ { \mathrm { m a x } } , { \sf F } _ { 2 } ^ { \mathrm { m i n } } ) ( { \sf F } _ { i } ^ { \mathrm { m i n } }$ is the optimal value of objective function i and $\mathrm { F } _ { i } ^ { \mathrm { m a x } }$ is the best value of objective function i when the other objective function is optimized), and the ideal point $( \mathsf { F } _ { 1 } ^ { \mathrm { m i n } } , \mathsf { F } _ { 2 } ^ { \mathrm { m i n } } )$ assuming the criteria are con<sup>fl</sup>icting. These three points are presented to the decision-maker through a two axis graphical display of the objective space. Next, the interactive phase starts. During the dialog phase, the decision-maker is asked to give indications about the sub-region in the objective space to carry on the search for a new non-dominated solution. The indications can be expressed in two different ways: by choosing a pair of non-dominated solutions already known and candidate to be adjacent or by indicating upper bounds on both objective functions. Based on this information, the system starts the search for a new non-dominated solution using a procedure based on Soland [40] that enables the determination of any non-dominated solution of the model.

As presented by Soland [40], to obtain all non-dominated solutions of a bicriteria integer or mixed-integer linear model like min $\mathrm { F } _ { 1 } ( \mathbf { x } )$

<sup>ð Þ</sup>min F x a parametric constrained problem of the type <sup>ð Þ</sup>s:t: : x∈S

min $\lambda _ { 1 } \mathsf { F } _ { 1 } ( \mathbf { x } ) + \lambda _ { 2 } \mathsf { F } _ { 2 } ( \mathbf { x } )$

s:t: : $\mathrm { F } _ { 1 } ( \mathbf { x } ) \leq \phi _ { 1 }$ should be solved for different values of $\phi _ { 1 }$ <sup>ð Þ</sup>F<sub>2</sub>  x ≤ϕ<sub>2</sub> <sup>ð</sup>x∈S

and $\phi _ { 2 } ,$ and with $\lambda _ { 1 } , \lambda _ { 2 }$ such that $\lambda _ { 1 } + \lambda _ { 2 } = 1$ and $\lambda _ { 1 } > 0 , \lambda _ { 2 } > 0 .$

In discrete problems, the simple optimization of weighted sums of the different objective functions only generates part of the nondominated solution set, named the supported solutions. These are the non-dominated solutions located on the frontier of the convex hull (see Fig. 3). Unsupported non-dominated solutions are those located in the interior of the triangles de<sup>fi</sup>ned by the orthogonal lines passing through adjacent extreme supported non-dominated solutions (i.e.

![](/api/attachments/FWKFBDDD/fulltext/images/07cf987d51d85cecb472e950186d56fbf40d49917be322acdde213fdb1f7b9d4.jpg)  
Fig. 13. GIS page with a Euclidean distance example.

Please cite this article as: S. Fernandes, et al., A DSS for bicriteria location problems, Decision Support Systems (2013), http://dx.doi.org/10.1016/ j.dss.2013.09.014

those dominated by some convex combination of other non-dominated solutions). The number of unsupported non-dominated solutions is, in general, much higher than the number of supported ones. Obviously, some unsupported non-dominated solutions can be most interesting for the decision-maker. So, this subset of non-dominated solutions must be considered.

In this way, in the computation phase, a single criterion problem representing a weighted sum of both objective functions is optimized, imposing limits on their values $( \phi _ { 1 }$ and $\phi _ { 2 } )$ accordingly to the preferences expressed by the decision-maker during the dialog phase. The weights are just operational parameters that can be <sup>fi</sup>xed by the analyst or even by default using equal weights. They do not have an important role in this interactive procedure. Because the structure of the single criterion problem remains almost unchanged, compared with the initial model, it is possible to take computational advantage of algorithms specially developed, and hence more ef<sup>fi</sup>cient, to solve the problem. To optimize the single criterion problem, SABILOC allows the decision-maker to choose between two general solvers — CPLEX [25] and MATLAB [32] and, in case of the simple facility location model and the p-facility location model, a special purpose procedure intended speci<sup>fi</sup>cally for these models — DUALOC adaptation (Dias et al. [11]) (Fig. 4).

As a result of the computation phase, the method always provides some information to the decision-maker. If there is no non-dominated solution in the studied sub-region, then the corresponding area in the objective space is eliminated (shaded). On the other hand, if a nondominated solution is obtained, it is displayed in the objective space and two sub-areas, where we can ensure there are no other nondominated solutions, are eliminated. Below and to the left of a found non-dominated solution there are no feasible solutions (otherwise, the found solution would be dominated). Moreover, any solution above and to the right of a non-dominated solution is dominated by it (Fig. 5). This information, together with the graphic information obtained when solutions are not found in a particular region, could be very useful to the decision-maker. Knowing the regions where there are no non-dominated solutions and therefore avoiding them, the decisionmaker searches for new solutions in a selective way improving the knowledge of the non-dominated solution set in a progressive way. As already mentioned, the interactive process goes on until the decisionmaker considers having suf<sup>fi</sup>cient knowledge about the set of nondominated solutions.

In conclusion, this constitutes a general-purpose linear integer programming learning oriented biobjective interactive package inspired on a proposal of Ferreira et al. [19]. In this paper, it is customized to several location models. It aims a progressive and selective learning of the ef<sup>fi</sup>cient solutions, not only avoiding the excessive computational effort of the generating techniques, but also refusing the use of aggregation procedures (based on weights or distance metrics) in order to converge to the optimum of some virtual utility function. In these circumstances, we avoid the most common aggregation problems due to distortions related to the estimation of weights and the use of normalization procedures. The base of our approach is just asking the decision maker, taking into account the previous obtained solutions, to update bounds for the objective functions values, in order to progress the search in his most interesting sub-areas of the objective functions space. Note that in psychological terms a dialog based on the progressive updating of reservation levels for the objective functions is much more reliable than putting questions, for instance, on weights. We intend to get a reduced number of potentially interesting ef<sup>fi</sup>cient solutions, which will be analyzed in more detail using the multiattribute module described in the next section.

![](/api/attachments/FWKFBDDD/fulltext/images/4a8e949b9d1164918870e97048a5683faf2c50db3dde90b777fee17225e1e77b.jpg)  
Fig. 14. Fixed costs page of SABILOC.

Please cite this article as: S. Fernandes, et al., A DSS for bicriteria location problems, Decision Support Systems (2013), http://dx.doi.org/10.1016/ j.dss.2013.09.014

The only reference describing an approach related to ours is Lotov et al. [29]. The authors propose a nice learning oriented use of tradeoff curves between pairs of criteria, parameterizing the values of the remaining ones. Although interesting it deserves a remark. Before the use of open search procedures, the methodology is based on heavy calculations because it requires the generation of the whole set of ef<sup>fi</sup>- cient solutions concerning each tradeoff curve. Its philosophy is very different from ours, mostly because we intended to design a procedure not only with a psychologically reasonable dialog phase, but also avoiding computational burden. So, we opted by delimitating progressively the search area, trying to avoid the calculation of ef<sup>fi</sup>cient solutions not interesting for the decision maker. Moreover, our methodology is organized into two phases. In the <sup>fi</sup>rst, we use a biobjective linear integer location model looking for the search of an interesting subset of ef<sup>fi</sup>cient solutions. The second one analyzes these solutions in more detail using a multiattribute model usually involving a much greater set of criteria.

## 6. Multiattribute a posteriori analysis module

After concluding the <sup>fi</sup>rst interactive phase, where a set of alternatives is known and apparently satisfactory for the decision-maker, a second phase procedure, consisting in a multiattribute a posteriori analysis, should be carried out. In this second phase, it is intended to execute a more detailed analysis of a subset of compromise alternatives, obtained from the <sup>fi</sup>rst phase, based on a large and coherent set of criteria/ attributes. Because we will consider additional attributes in this analysis, some dominated solutions eliminated in the <sup>fi</sup>rst interactive phase (in terms of the two criteria considered on that phase) may now be interesting for the decision-maker. In this way, in many cases, it is justi<sup>fi</sup>ed to extend the analysis to slightly dominated solutions around the acceptable solutions selected in the <sup>fi</sup>rst phase. This extension can be done through SABILOC and for that purpose, the decision-maker only has to select the preferable regions of the objective space and the system calculates all feasible (dominated and non-dominated) solutions on those regions.

The next step is to select a set of criteria that describes the performance of the alternatives. The criteria will be the performance measures by which the alternatives will be judged. SABILOC allows the decisionmaker to choose from a wide range of criteria (sixteen in total), helpfully subdivided into four groups representative of obnoxious effects, accessibility, costs and equity, as presented in Table 1. The choice of criteria to implement for the multiattribute analysis took into account the most usual criteria found in the literature (for details about the criteria see Fernandes et al. [18]). Although we have implemented these criteria, any other interesting and relevant criteria can be easily included in the system.

In Table 1, S corresponds to the set of installed services. I is the set of clients or communities to be served; a is the population of community located at site $i \epsilon I ; d _ { i j }$ is the Euclidean distance between community i - I and site j $\epsilon S ; c _ { i j }$ is the length of the shortest path between community i - I and the equipment installed at site $j \in S ; N$ is the number of communities; a is the average population; $E _ { i ( x ) }$ is a value representative of total obnoxious effect or accessibility related to the community located at site i- I and $\overline { { E _ { ( x ) } } }$ is the correspondent average value. Note that all criteria are <sup>ð Þ</sup>of minimization except Crit. 5 which is to be maximized.

At this stage of the procedure, it could be important to involve the decision-makers and the interest groups (e.g. municipality and civil parish representatives, resident committees, and environmental organizations) in order to derive a coherent and representative set of new

![](/api/attachments/FWKFBDDD/fulltext/images/3694714acf89db7d6ad7ae03698466614a720ef2c278e72f9fbd205c68420cc4.jpg)  
Fig. 15. Assignment costs page of SABILOC

S. Fernandes et al. / Decision Support Systems xxx (2013) xxx–xxx  
![](/api/attachments/FWKFBDDD/fulltext/images/90f4aa1b8bae854e9513ca4b06fc1d9d5989ed53f3f0e9c5715bab8e042450bb.jpg)  
Fig. 16. Fixed variables page of SABILOC.

criteria, which re<sup>fl</sup>ects their concerns and goals. SABILOC also allows the analyst to add new criteria, quantitative or qualitative type (Fig. 6), and new alternatives.

To help encourage the decision-maker(s) to think about all the information contained in the performance matrix, we think it is worth considering the use of supplementary presentations, such as graphs, and additional summaries of the data. The presentation of the performance of alternatives through the so-called radar chart can be very helpful to the decision-maker for a better understanding of the data. The radar chart will enable to easily visualize the peculiar differences between alternatives when facing all the criteria and will be a key part of our procedure. On this radar, each axis represents an active criterion and the performances of active alternatives are plotted along the axes. Each alternative is represented in the chart through a ring, <sup>fi</sup>lled or not, in which the vertices lie on the axes. The center point of the radar chart corresponds to the anti-ideal point and the outer ring to the ideal point. Additionally, to complement the radar chart information, it is also presented, in tabular way, the distance of each alternative, considering only quantitative criteria, to the ideal point using three types of metric: $L _ { 1 } , L _ { 2 }$ and L (Fig. 7).

Furthermore, although SABILOC initially provides a large set of criteria, the decision-maker, based on the evaluation of alternatives, may wish to select a more restrict subset of the criteria to analyze. It may happen that all the available alternatives are likely to achieve the same, or very similar, level of performance when assessed against a certain criterion initially chosen. A criterion like this one can be considered redundant to the multiattribute analysis and consequently removed or inactivated. SABILOC allows the analyst to achieve the selection of criteria by inactivating those that have exactly the same or similar (considering a positive small tolerance ) performance values.

Moreover, the decision-maker, in relation to the criteria considered, could be interested in inactivating dominated, or even quasidominated<sup>4</sup>, alternatives. The implemented decision support system may help the decision-maker in selecting only alternatives that are not (quasi-)dominated by any other alternative (Fig. 8).

Once the dominance analysis and the elimination of redundant criteria have been concluded, and if the decision-maker is not able of opting yet for one <sup>fi</sup>nal solution, then multiattribute analysis methods should be used. The additive model, despite being the most commonly used to aggregate preferences in multiattribute problems, has raised several criticisms regarding the requirement of additive independence of criteria and its full compensatory nature. The method proposed here is intended to circumvent the problem of compensation, avoiding aggregation inter-criteria. As it is known, the available non-compensatory techniques are very simple and hardly used. However, we believe that if the techniques are well implemented, with good interactivity and the help of additional tools, then they may be an added value in supporting decision-making. The method proposed here can be seen as an interactive implementation of the conjunctive method, which consists in eliminating alternatives that do not reach speci<sup>fi</sup>c performance levels for the considered criteria. The developed tool is non-compensatory thence avoiding the problem that a weak performance in one attribute may always be compensated by a strong performance in another attribute, as in an additive model. The tool also avoids the need to assume additive independence among the various attributes. In certain situations, such assumption is a requirement too strong. Thus, with the multiattribute analysis module of SABILOC, the main limitations of the additive method are surpassed.

To put into practice the interactive conjunctive method tool, we consider, for each criterion, a number of performance levels, allowing the classi<sup>fi</sup>cation of the alternatives in classes de<sup>fi</sup>ned by these thresholds. We use the representation in a radar chart, and an appealing color scheme, providing a direct and interactive process to modify the thresholds on the graphic and an immediate visualization of the changes in the results. The decision-maker can consider three performance levels at the most – ‘Reservation Level’, ‘Level 1’ and ‘Level 2’ – and the de<sup>fi</sup>nition of performance level values for each one of them can be done directly through edits, slider controls or the radar chart.

Initially, only the level values of ‘Reservation Level’ are de<sup>fi</sup>ned and, by default, they correspond to the worst value of all active alternatives for each criterion. Obviously, these values can be changed by user's choice. Also note that crossing the levels is not allowed. So, the level's values must comply with a non-increasing or non-decreasing ordering, depending on whether the criterion is of minimization or maximization, respectively. By default, the representation of levels in the radar chart is made by a dashed ring, colorful and not <sup>fi</sup>lled. The colors associated with the levels ‘Reservation Level’, ‘Level 1’ and ‘Level 2’ are red, orange and yellow, respectively. The user can change all these properties.

By setting the level's values, the program automatically tells, through different colors, which alternatives do not satisfy the levels giving an immediate feedback to the decision-maker about his/her choices. The manipulation of the controls allows the users to gradually gain consciousness of the problem at hand and a thorough understanding of the alternatives' behavior when dealing with the required levels for the criteria.

In Subsection 7.3 concerning the case study, we will illustrate this second interactive procedure.

Summarizing, this module is also a learning oriented one, here combining the avoidance of the concerns related to weights and normalizations, with sensitivity analysis capacities and enabling holistic comparison of the alternatives.

## 7. Waste transfer station siting case study

The district of Setúbal is located in the south-west of Portugal and the district capital is the city of Setúbal. It has a population of approximately 852 thousand inhabitants (Census, 2011) and an area of 5064 km<sup>2</sup>. Thirteen municipalities compose the district.

AMARSUL is the company responsible for the treatment, recovery and disposal of urban solid waste produced in nine of the thirteen municipalities of Setúbal district, which correspond to 58 civil parishes, approximately 780 thousand inhabitants (Census, 2011) and an area of 1522 km<sup>2</sup>. According to the data provided by the company (AMARSUL [3]), the active waste management infrastructures are: two sanitary land<sup>fi</sup>lls, one aerobic mechanical biological treatment plant, one sorting center, two biogas recovery installations, seven recycling collection centers and one waste transfer station. And still under construction: an anaerobic digestion mechanical biological treatment unit, with a mechanical treatment to produce refuse derived fuel (Fig. 9 — retrieved from AMARSUL website).

The de<sup>fi</sup>nition of a waste transfer station (by Portuguese Decree-Law nr 239/97 of September 9) is a facility where waste is unloaded in order to prepare it to be transported to another place of treatment, recovery or disposal. As it is known, the primary reason for using a transfer station is to reduce the cost of transporting waste to <sup>fi</sup>nal facilities. Additional advantages are: the possibility of siting the infrastructures of treatment, recovery and disposal of urban solid waste at greater distances from urban centers; the possibility of a greater use of collection vehicles by reducing the distances traveled and allowing the use of smaller vehicles in urban centers. Despite the obvious economic and environmental bene<sup>fi</sup>ts associated with the use of waste transfer stations, they also present some environmental concerns (for instance, the noise caused by the use of heavy-duty equipment at the facilities, the unpleasant odor, insects, the increased traf<sup>fi</sup>c congestion in the vicinity of transfer stations and the consequent noise resulting from that circumstance).

![](/api/attachments/FWKFBDDD/fulltext/images/d5d7e9deb76fc141e575326f8d6154d860bdb182b42b69ba64b7ab5f18c9afcf.jpg)  
Fig. 17. Results page displaying the <sup>fi</sup>rst lexicographical minimum.

In this case study, we assume that the company AMARSUL is assessing the possibility of building at least one waste transfer station in its area of action. The waste discharged in these stations would be transferred later to the nearest land<sup>fi</sup>ll (located in the municipalities of Palmela and Seixal). Some previous studies pointed out that the installation of a transfer station would be economically advantageous when the distance, from the centroid of waste collection routes to the disposal site, exceeds more or less 25 km. This break-even distance is only indicative, and certainly outdated, since it still does not consider the recent sharp increases in fuel prices. As it can be seen in Fig. 10 (MAOT [31]), AMARSUL has not matched the national growth in the number of transfer stations, somehow validating the intentions of the company to assess the building of such infrastructures, while keeping operational the existing one in the municipality of Sesimbra. Moreover, the building of more waste transfer stations meets the guidelines for action plan (MAOT [31]), designed by the Portuguese Ministry of Environment, Spatial Planning and Regional Development, which points out the strategy, de<sup>fi</sup>nes priorities and sets goals to achieve for the period 2007 to 2016 on urban solid waste management.

Identifying a suitable site for a waste transfer station can be a challenging process. Site suitability depends on numerous technical, environmental, economic, social, and political criteria. When selecting a site, a balance needs to be achieved among the multiple criteria that might have con<sup>fl</sup>icting objectives. For example, a site centrally located in the area where waste is generated would be economically better but it would disturb the wellbeing of people living or working near the site, causing public concerns and opposition. Less than ideal sites may still present the best option due to transportation, environmental, and economic considerations. The relative importance given to each criterion used in selecting a suitable site will vary by the community's needs and concerns (EPA [12]).

In the next three subsections we will explore the case study here described in order to show in action the potentialities and functionalities of SABILOC.

## 7.1. Preprocessing data

We will now show how we can use the embedded GIS to preprocess data in order to obtain initial candidate sites for using in the <sup>fi</sup>rst interactive phase of our case study.

Besides the Of<sup>fi</sup>cial Administrative Map of Portugal, eleven input map layers (protected areas, special protection areas for avifauna and biotopes; natural resources; water; parks; land use and land cover; land feasibility; street roads; railways; city limits; sanitary land<sup>fi</sup>lls and waste transfer station) are evaluated to be used in the embedded GIS. For the purpose of verifying the safe distances, we used the values indicated in Table A1 (in Appendix A) to determine the buffer zones for each layer. Several operations were made in SABILOC using the Spatial Analyst and the Network Analyst extensions. With the Spatial Analyst extension, we converted vector data to raster data, calculated Euclidean distances and, using the Map Algebra syntax, we performed operations and conditional statements among and within raster datasets. Next, using the Network Analyst extension, we found the regions that

![](/api/attachments/FWKFBDDD/fulltext/images/1102eef0a93dd81aa193766a688f80ba0e8f9a1b648e81e8020ebd42c4f8a767.jpg)  
Fig. 18. Results page displaying the second lexicographical minimum and the ideal point.

Please cite this article as: S. Fernandes, et al., A DSS for bicriteria location problems, Decision Support Systems (2013), http://dx.doi.org/10.1016/ j.dss.2013.09.014

encompass all accessibility streets within 15 and 25 km of the existing land<sup>fi</sup>lls and the existing waste transfer station, via the road network.

Fig. 11 shows the result of the operations mentioned before. All initially obtained raster layers were multiplied by each other so that if any pixel was equal to 0, coming from any layer, then the pixel value resulting from the multiplication will become 0, which means that the pixel is completely unsuitable as a waste transfer station site. More dark colors in the <sup>fi</sup>gure represent more unsuitable sites where black represents an excluded area. Red color represents the sites which have the highest value of the suitability index regarding the considered layers. The polygons dark and light pink are the regions respectively within 15 and 25 km of land<sup>fi</sup>lls and the waste transfer station.

Choosing the sites with maximum value of suitability and total area not less than 10,000 m<sup>2</sup>, we obtain 94 potential sites to install waste transfer stations.

## 7.2. First interactive phase

Given previously obtained potential sites, we can go on now to the <sup>fi</sup>rst interactive phase. In this case study, we use the bicriteria simple facility location model where J corresponds to the set of potential sites to locate waste transfer stations (centroid of areas obtained in Subsection 7.1) plus the sites of existing land<sup>fi</sup>lls and the existing waste transfer station. Set I corresponds to the set of centroids of the population area of the civil parishes (58 points).

The objective functions used were (1) and (2), where $h _ { j }$ is the waste transfer station <sup>fi</sup>xed cost (cost to build, own and operate the transfer station) for selecting site j- J plus the transfer truck hauling cost from the transfer station at site j- J to the closest land<sup>fi</sup>ll; $l _ { i j }$ is the assignment cost of the civil parish centroid located at site i - I to the waste transfer station or to an existing land<sup>fi</sup>ll at site $j \in J ; g _ { j }$ is a measure of the obnoxious effect (for example, the odor or the noise) in a certain area de-<sup>fi</sup>ned around a transfer station located at site $j \epsilon J$ and around the shortest path from site j- J to the closest land<sup>fi</sup>ll, multiplied by an impact factor (in this case the number of inhabitants); and $d _ { i j } ,$ in this instance, is null.

At the outset, it should be noted that this case study is intended to demonstrate in a simple way, the modus operandi of the various modules of the DSS. The case study does not address with too much detail all the features that a real problem of this sort would require. Detailed information about the costs (land deployment, maintenance of transfer stations, maintenance and fuel consumption of different vehicles used in this type of service, manpower, etc.) and about the environmental impact (measurements of noise and odor, emissions and fuel consumption of vehicles taking into account the inclinations of the paths, etc.) would be needed. The amount of waste collected and transported from collection points to transfer stations and then to land<sup>fi</sup>ll, or directly to land<sup>fi</sup>lls, would also be an important indicator that would certainly in<sup>fl</sup>uence the decision process, particularly with regard to the capabilities and the sizes of the waste transfer stations to deploy.

For dealing with this instance of the problem, we can take advantage of the GIS potentialities in order to obtain some of the required values. To obtain the transfer truck hauling cost from the transfer station at site j- J to the closest land<sup>fi</sup>ll we used the Closest Facility tool of the Network Analyst extension, which calculates the shortest path, considering the potential sites to install a waste transfer station as origins and the existing land<sup>fi</sup>lls as destinations. The attribute considered to minimize while determining the route was the distance. The result was then multiplied by the corresponding unitary cost.

Fig. 12 shows the output of another Closest Facility tool computation corresponding to the shortest path from the civil parish centroids to each of the 94 potential sites to locate transfer stations plus the two existing land<sup>fi</sup>lls and the existing waste transfer station. After the shortest path computation, it is possible to visualize a table with all the solution's information. Multiplying these results by the collection truck fuel consumption and dividing by the collection truck average payload we obtain the $l _ { i j }$ mentioned before.

![](/api/attachments/FWKFBDDD/fulltext/images/b8ba1091e881e7402d4b5db1a39a81f8b7969b925d965ee51e30576302c345cf.jpg)  
Fig. 19. Results page displaying the non-dominated solutions 1, 2 and 3. Assignments of solution 3.

To obtain the second objective function coef<sup>fi</sup>cients, we used some tools of the Spatial Analyst extension. First, we calculated a Euclidean distance raster (considering the maximum distance equal to 1000 m) around the potential sites to install the transfer stations and around the roads that de<sup>fi</sup>ne the shortest paths from these potential sites to existing land<sup>fi</sup>lls. Next, in order to obtain a measure of negative impact on communities, we multiplied the number of inhabitants in the buffer areas by the inverse of the Euclidean distances obtained before. Therefore, the second objective function represents a measure of the obnoxious effects on communities caused by the installed facilities (in this case, the main inconveniences are the odor and the noise resulting of the heavy-duty facility equipment) and by the heavy truck traf<sup>fi</sup>c, hauling shipment to the <sup>fi</sup>nal disposal site. Fig. 13 shows part of the map resulting from these operations.

All the obtained coef<sup>fi</sup>cients of objective functions can be seen in the Fixed Costs page (Fig. 14) and the Assignment Costs page (Fig. 15).

In real situations, often certain services must necessarily be installed in places de<sup>fi</sup>ned at the outset, due to social, economic and/or policy reasons. Likewise, some communities have to be assigned to speci<sup>fi</sup>c services or, alternatively, they cannot be assigned to some services. So, to cope with this situation, SABILOC allows us to <sup>fi</sup>x some variables of the models through the Fixed Variables page (Fig. 16). That is, we can de<sup>fi</sup>ne a potential site to install a service as an obligatory choice for opening a service. After a reassessment of the problem at hand, a potential site could also be considered no longer valid. Likewise, we could deal with the assignments between the communities and the installed services, and de<sup>fi</sup>ne them as active or inactive. To set variables $x _ { i j }$ and y as intended, we have to <sup>fi</sup>ll in the corresponding grids on the Fixed Variables page. This software feature is very useful for our instance because it allows us to <sup>fi</sup>x the existing waste transfer station in Sesimbra as open, since it was decided to keep this transfer station in operation. The two land<sup>fi</sup>lls (Palmela and Seixal) are also <sup>fi</sup>xed as open. As Fig. 16 shows, the icons associated with the open services are now different in order to highlight the fact they have been opened by the user setting.

After de<sup>fi</sup>ning all the parameters of the model, the interactive search for ef<sup>fi</sup>cient solutions through the Results page can start. Initially the system computes the two lexicographic optima and the ideal point. In our instance, the lexicographical minimum obtained for objective function $\mathrm { F } _ { 1 }$ was $\mathsf { S } _ { 1 } = ( 7 5 5 . 5 , 2 0 0 0 . 4 )$ (Fig. 17). In the second iteration is shown the non-dominated solution that minimizes objective function $\mathrm { F } _ { 2 } ,$ which is equal to $\mathrm { S } _ { 2 } = ( 1 0 1 3 . 9 , 2 0 3 )$ ). In this iteration the ideal point is also presented (Fig. 18).

Looking at Figs. 17 and 18, we can see that while solution 1 corresponds to opening 3 new transfer stations at potential sites 26, 49 and 86 (maintaining the current transfer station in Sesimbra in operation as required before), solution 2 maintains the current situation of a single transfer station. Note that all <sup>fi</sup>xed variables are respected in both solutions that ${ \mathrm { i } } s ,$ the existing transfer station and both land<sup>fi</sup>lls are open.

Now, to carry on the search for a new non-dominated solution, the decision-maker has to give indications about the sub-region in the objective space where to search. To do so, one possibility is mouse clicking at some point of the rectangle de<sup>fi</sup>ned by the lexicographic minima, which corresponds to the region of the objective space where more non-dominated solutions may exist. Let us try to calculate a new nondominated close to the ideal point. To this end, we mouse click within the objective space in a point close to the ideal point. A dialog box (see Fig. 4) opens and we accept the parameters de<sup>fi</sup>ned by default. As intended, the chosen upper limits are given for the objective functions.

![](/api/attachments/FWKFBDDD/fulltext/images/f567dff726e9fb434b47ffa80fc2abc4a2917bde294fbfaebe066de47b79c0a2.jpg)  
Fig. 20. Results page displaying the non-dominated solutions 2, 3, 4, 6 and 7. Assignments of solution 7.

Please cite this article as: S. Fernandes, et al., A DSS for bicriteria location problems, Decision Support Systems (2013), http://dx.doi.org/10.1016/ j.dss.2013.09.014

The weight λ<sub>1</sub> (mentioned in Section 5) is automatically calculated taking into account the upper limits considered. We should remember that the speci<sup>fi</sup>c choice of the positive weight $\aleph _ { 1 }$ is not important in our interactive method. To optimize the single criterion problem, by default, the selected software is the DUALOC adaptation. In this case, we were too demanding with the objective function limits and thus, the DSS output was that there are no non-dominated solutions in that region.

Figs. 19 and 20 represent two different steps of the interactive process.

Note that the scales of the objective space in Fig. 20 were changed in order to facilitate their viewing, since the image was confused due to the proximity of the solutions. The third solution obtained by searching the region between the lexicographic optima, compared with the <sup>fi</sup>rst, worsens 92.1 units in the value of objective function F<sub>1</sub> (representing cost) and improves 1786.4 units in the value of objective function $\mathrm { F } _ { 2 }$ (representing environmental impact). Compared with solution number 2, it improves 166.3 units in the cost and worsens 11 units in the environmental impact.

## 7.3. Second interactive phase

Considering solution 7 as the preferable one for the decision-maker, let us execute a more detailed analysis of this alternative. As already mentioned before, because we will consider additional attributes in this analysis, some dominated solutions eliminated in the <sup>fi</sup>rst interactive phase (in terms of the two criteria considered on that phase) may now be interesting for the decision-maker. Therefore, we will search for solutions similar to solution 7. We will make a search in a square, with side-length of 4 units, centered on solution 7, that is, we will consider as search limits $8 2 5 . 5 \le \mathrm { F } _ { 1 } \le 8 2 9 . 5$ and $2 4 6 . 3 \le \mathrm { F } _ { 2 } \le 2 5 0 . 3$ (Fig. 21). The result of the search performed in the speci<sup>fi</sup>ed area is presented in a dialog box (Fig. 22) and 12 solutions were obtained.

![](/api/attachments/FWKFBDDD/fulltext/images/db55da281e8c519de6b0509f5ecd7a7f813fe58ab40715558ff6cdc3fb010cd0.jpg)  
Fig. 22. Displaying the results of a search performed in a particular area of the objective space.

Through this last window and selecting some or all the solutions, we can create the data to carry out a multiattribute a posteriori analysis.

Next, the decision-maker has to select a set of criteria that will describe the performance of the alternatives. Intending to address the location of waste transfer stations, we selected (from Table 1) criteria 2, 3, 4 and 5 from the group of criteria representing the obnoxious effect, criteria 6 and 7 representing accessibility, criteria 8 and 10 representing the costs and criteria 13 to 16 as equity measures. In our case study, S corresponds to the set of installed waste transfer stations plus the existing land<sup>fi</sup>lls and the existing waste transfer station. And set I corresponds to the set of centroids of the population area of the civil parishes.

In this concrete problem, where it is intended to build waste transfer stations, the interest group perspectives may be particularly important in order to derive a representative set of new criteria, which re<sup>fl</sup>ects their concerns and goals. To illustrate the SABILOC functionality, which allows us to insert new criteria, quantitative or qualitative type (see Fig. 6), we added a new qualitative criterion with four classes (poor, average, good, excellent), which could be interpreted as a personal appreciation of alternatives by a company manager.

![](/api/attachments/FWKFBDDD/fulltext/images/47a1914671583dff7f5b5a47aacc2ab815e1c49dc5b4d398b0c236080e0f7e75.jpg)  
Fig. 21. Finding all solutions in a particular area of the objective space.

![](/api/attachments/FWKFBDDD/fulltext/images/3a8b9fee00467a3f5019550fb6d1d0dcace8f1725fb097fe6adb63b7dc3b1a20.jpg)  
Fig. 23. De<sup>fi</sup>ning performance levels. (For interpretation of the references to color in this <sup>fi</sup>gure, the reader is referred to the web version of this article.)

In short, our performance matrix has now 13 attributes (one of them is qualitative) and 12 alternatives (see Table A2 in Appendix A). To help the decision-makers for a better understanding of all the information contained in the matrix, we present them the performance of alternatives through the radar chart. Moreover, to complement the radar chart information, we also present the distance of each alternative to the ideal solution using the metrics $L _ { 1 } , L _ { 2 }$ and $L _ { \infty } .$ On the left-hand side of Fig. 7, we presented part of the performance matrix and on the right-hand side, the radar chart and the distances mentioned before.

Next, using SABILOC (see Fig. 8), we inactivated the criteria of the <sup>fi</sup>rst three groups (obnoxious effect, accessibility and cost) in which all the alternatives have the same performance values. For the fourth group of criteria, representative of equity, we assumed the coef<sup>fi</sup>cient measures with a difference of one percentage point are redundant for our analysis. We also inactivated the dominated alternatives.

Finally, for obtaining a <sup>fi</sup>nal solution of the studied instance, we simulated the choices of performance's thresholds for the criteria by a decision-maker. First, we only accepted an alternative if the level of performance of the qualitative criterion was at least good. With this option, four alternatives were inactivated (1, 3, 5 and 8). Then we gave priority to the cost criteria. De<sup>fi</sup>ning the threshold value of Crit. 10 equal to 731 we inactivated one more alternative. After some more interactions, the result of the manipulation of levels is presented in Figs. 23 and 24.

Alternative 4 is the only one active (green), alternative 2 has orange color, alternative 6 has yellow color and all the others are red. Selecting alternative 4, the <sup>fi</sup>nal resolution of the real problem addressed here involves the opening of two new waste transfer stations in potential sites 26 and 64. Transfer station 26 would serve as a point of unload of 7 civil parishes (Fig. 25) and station 64 of 6 parishes. The waste unloaded in the waste transfer stations 26 and 64 is then prepared and transported to the closest land<sup>fi</sup>ll located at Palmela (Fig. 26).

Note that this alternative is a dominated solution regarding the two objective functions considered in the <sup>fi</sup>rst interactive phase. Compared with the non-dominated solution 7 selected in the <sup>fi</sup>rst phase, in terms of the two objective function values initially considered, alternative 4 has the same environmental impact but has a higher cost value. What led to the choice of alternative 4 instead of the solution 7 (alternative 1 in the second phase) was the above referred qualitative criterion, corresponding to the simulation of a personal appreciation of alternatives by a company manager, who evaluated solution 4 as being excellent and solution 7 (alternative 1) as being average. Thus, the <sup>fi</sup>nal resolution provides great part of the continuity of the current management for collecting waste. In particular, the continuity of the current waste transfer station in Sesimbra to satisfy the municipality of Sesimbra and the

![](/api/attachments/FWKFBDDD/fulltext/images/3746f8b6681dd04a48187046f11d03067318e9d71ba876b16c543efade81bf9f.jpg)  
Fig. 24. Radar chart.

Please cite this article as: S. Fernandes, et al., A DSS for bicriteria location problems, Decision Support Systems (2013), http://dx.doi.org/10.1016/ j.dss.2013.09.014

![](/api/attachments/FWKFBDDD/fulltext/images/657fe57c714dc8f5ec3471b0201bd99e09dd0ea3288913b31a913a70b0e24a1f.jpg)  
Fig. 25. Civil parishes allocated to waste transfer station 26.

waste collected in the most parishes will continue to be directly unloaded in the land<sup>fi</sup>lls located in Seixal and Palmela.

## 8. Conclusions

In this paper, we presented SABILOC, a new DSS developed to support the decision-making concerning bicriteria location problems. As described, the system was specially designed to deal with problems in which the facilities to be located have environmental impacts.

Three advantages of the implemented DSS, when compared with the approaches found in the literature, were detailed and highlighted: the initial interactive phase (based on a combinatorial optimization procedure), the multiattribute a posteriori analysis module and the embedment of a GIS into SABILOC.

In order to validate the potentialities and functionalities of SABILOC. we presented a case study of a real world problem. First, we used the GIS embedded into SABILOC to preprocess data for the case study. After preprocessing data, we used the interactive procedure provided by SABILOC, to obtain non-dominated solutions of the Bicriteria Simple Facility Location model. The model parameters were obtained using the embedded GIS. The solutions are presented in a graphically appealing way, through the objective space display, and its calculation is quite fast. We searched in certain regions of the objective space in order to <sup>fi</sup>nd non-dominated solutions that would meet our preferences. A small set of satisfactory alternatives was chosen in this interactive phase. Then, the second phase procedure, consisting in the multiattribute a posteriori analysis, was carried out. To proceed with the detailed analysis of the small set of alternatives, we used several tools and the interactive implementation of the conjunctive method, eliminating alternatives which did not reach speci<sup>fi</sup>c performance levels for the criteria considered. To help in de<sup>fi</sup>ning the adequate thresholds of performance for the criteria we used the radar chart and the appealing color scheme provided by the DSS.

<table><tr><td colspan="2">[~] Route: Location 26 - Palmela</td><td>18,2 km</td><td>18 min</td><td></td></tr><tr><td colspan="2">1: Start at Location 26</td><td></td><td></td><td>Map</td></tr><tr><td colspan="2">2: Go southeast</td><td>&lt;0,1 km</td><td>&lt;1 min</td><td>Map</td></tr><tr><td colspan="2">3: Take roundabout and proceed southeast</td><td>0,3 km</td><td>&lt;1 min</td><td>Map</td></tr><tr><td colspan="2">4: Take roundabout and proceed southeast on N119</td><td>0,6 km</td><td>&lt;1 min</td><td>Map</td></tr><tr><td colspan="2">5: Take roundabout and proceed south on N119</td><td>0,2 km</td><td>&lt;1 min</td><td>Map</td></tr><tr><td colspan="2">6: Take ramp and go south on IC3</td><td>3,5 km</td><td>3 min</td><td>Map</td></tr><tr><td colspan="2">7: Go on IC32</td><td>8,6 km</td><td>7 min</td><td>Map</td></tr><tr><td colspan="2">8: Bear left onto ramp to N379-2</td><td>0,3 km</td><td>&lt;1 min</td><td>Map</td></tr><tr><td colspan="2">9: Bear left on N379-2 (Estrada EN379-2)</td><td>0,9 km</td><td>&lt;1 min</td><td>Map</td></tr><tr><td colspan="2">10: Bear right onto ramp</td><td>0,6 km</td><td>&lt;1 min</td><td>Map</td></tr><tr><td colspan="2">11: Turn left</td><td>0,5 km</td><td>&lt;1 min</td><td>Map</td></tr><tr><td colspan="2">12: Bear left on Estrada das Formas</td><td>2,4 km</td><td>4 min</td><td>Map</td></tr><tr><td colspan="2">13: Turn left</td><td>&lt;0,1 km</td><td>&lt;1 min</td><td>Map</td></tr><tr><td colspan="2">14: Turn right</td><td>0,1 km</td><td>&lt;1 min</td><td>Map</td></tr><tr><td colspan="2">15: Finish at Palmela</td><td></td><td></td><td>Map</td></tr><tr><td colspan="2">Total time: 18 min</td><td></td><td></td><td></td></tr><tr><td colspan="2">Total distance: 18,2 km</td><td></td><td></td><td></td></tr></table>

Fig. 26. Directions from the waste transfer station 26 to land<sup>fi</sup>ll in Palmela.

Although the resolution of the real world problem had not used all the information required to solve a complex problem like this one, the proposed <sup>fi</sup>nal solution was analyzed in the general context and it seems a plausible solution to be implemented.

Finally, we highlight that SABILOC is totally free of charge. The software runs on Windows, from Vista onwards. After registering at http:// ltodi.est.ips.pt/sergiof/SABILOC/, you can download the last version of SABILOC. As for the external tools: DUALOC Adaptation is free and is an integrant part of SABILOC; the use of MATLAB requires the installation of a MATLAB Compiler Runtime; and the use of CPLEX requires a license that can be free of charge for educational purposes. To run SABILOC and make use of the embedded GIS, an ArcGIS 9.3 Engine Runtime singleuser license or an ArcGIS 9.3 Desktop license, for example the ArcView, is needed.

## Acknowledgments

This work was partially supported by the FCT Portuguese Foundation of Science and Technology (Fundação para a Ciência e a Tecnologia) under research projects Pest-OE/MAT/UI0152 and POSC/U308/1.3/NRE/04.

## Appendix A

## Table A1

Summary of the input layers used in the analysis.

<table><tr><td>Layer name</td><td>Buffer zone</td><td>Ranking</td></tr><tr><td rowspan="2">Protected areas, special protection areas for avifauna and biotopes</td><td>Not suitable</td><td>0</td></tr><tr><td>Suitable</td><td>1</td></tr><tr><td rowspan="2">Natural resources</td><td>Not suitable</td><td>0</td></tr><tr><td>Suitable</td><td>1</td></tr><tr><td rowspan="2">Water</td><td>Not suitable</td><td>0</td></tr><tr><td>Suitable</td><td>1</td></tr><tr><td rowspan="2">Parks</td><td>Not suitable</td><td>0</td></tr><tr><td>Suitable</td><td>1</td></tr><tr><td>Land use and land cover</td><td>CUF, A, RRNAL, CS, GUA, RF, V, OG, ACAPC, IM, SM, SAL, IF, WC, WB, CL, E, SO DUF, SLF, NIAL, PIL, FTBP, ANV, NG, BDS PA, PAST, CCP, AFA, BLF, CF, MF, BA ICU, MES, DS, MH, SV, TWS, BR</td><td>0</td></tr><tr><td rowspan="4">Land feasibility</td><td>S, SA, R</td><td>0</td></tr><tr><td>A</td><td>2</td></tr><tr><td>B</td><td>5</td></tr><tr><td>C, D, E, A or B + C, A or B + D or E, C + D or E</td><td>10</td></tr><tr><td>Street roads</td><td>≤20 m</td><td>0</td></tr><tr><td>Including major and highway roads</td><td>&gt;20 m and ≤250 m</td><td>10</td></tr><tr><td rowspan="2">(Euclidean distances)</td><td>&gt;250 m and ≤500 m</td><td>5</td></tr><tr><td>&gt;500 m</td><td>2</td></tr><tr><td>Railways</td><td>≤20 m</td><td>0</td></tr><tr><td>(Euclidean distances)</td><td>&gt;20 m</td><td>1</td></tr><tr><td>City limits</td><td>≤150 m</td><td>0</td></tr><tr><td>(Euclidean distances)</td><td>&gt;150 m</td><td>1</td></tr><tr><td>Landfills</td><td>≤10 km</td><td>0</td></tr><tr><td>(Euclidean distances)</td><td>&gt;10 km</td><td>1</td></tr><tr><td>Waste transfer station</td><td>≤10 km</td><td>0</td></tr><tr><td>(Euclidean distances)</td><td>&gt;10 km</td><td>1</td></tr></table>

Please cite this article as: S. Fernandes, et al., A DSS for bicriteria location problems, Decision Support Systems (2013), http://dx.doi.org/10.1016/ j.dss.2013.09.014

Performance matrix. <sub>ble</sub> A<sup>2</sup>

Legend:

$$
\mathrm{D}
$$

$$
\mathrm{AorB+C}
$$

<table><tr><td></td><td>Crit. 2</td><td>Crit. 3</td><td>Crit. 4</td><td>Crit. 5</td><td>Crit. 6</td><td>Crit. 7</td><td>Crit. 8</td><td>Crit. 10</td><td>Crit. 13</td><td>Crit. 14</td><td>Crit. 15</td><td>Crit. 16</td><td>Manag. appr.</td></tr><tr><td>Alt. 1</td><td>0.0436</td><td>26.5917</td><td>103.314</td><td>1992.1152</td><td>7,557,274.451</td><td>25.023</td><td>98.2</td><td>729.3</td><td>0.4915</td><td>0.0995</td><td>0.2527</td><td>0.4114</td><td>Average</td></tr><tr><td>Alt. 2</td><td>0.0436</td><td>26.5917</td><td>103.314</td><td>1992.1152</td><td>7,558,915.409</td><td>25.023</td><td>98.2</td><td>729.5</td><td>0.4915</td><td>0.0995</td><td>0.2526</td><td>0.4114</td><td>Good</td></tr><tr><td>Alt. 3</td><td>0.0438</td><td>26.5896</td><td>103.314</td><td>1992.1152</td><td>7,565,007.410</td><td>25.023</td><td>98.0</td><td>729.9</td><td>0.4908</td><td>0.1000</td><td>0.2524</td><td>0.4112</td><td>Average</td></tr><tr><td>Alt. 4</td><td>0.0438</td><td>26.5896</td><td>103.314</td><td>1992.1152</td><td>7,566,648.368</td><td>25.023</td><td>98.0</td><td>730.1</td><td>0.4908</td><td>0.1000</td><td>0.2524</td><td>0.4112</td><td>Excellent</td></tr><tr><td>Alt. 5</td><td>0.0436</td><td>26.5849</td><td>103.314</td><td>1992.1152</td><td>7,558,863.133</td><td>25.023</td><td>98.2</td><td>730.0</td><td>0.4917</td><td>0.0996</td><td>0.2527</td><td>0.4114</td><td>Average</td></tr><tr><td>Alt. 6</td><td>0.0436</td><td>26.5849</td><td>103.314</td><td>1992.1152</td><td>7,560,504.091</td><td>25.023</td><td>98.2</td><td>730.2</td><td>0.4917</td><td>0.0996</td><td>0.2527</td><td>0.4114</td><td>Good</td></tr><tr><td>Alt. 7</td><td>0.0436</td><td>26.5917</td><td>103.314</td><td>1992.1152</td><td>7,569,418.779</td><td>25.023</td><td>98.2</td><td>730.4</td><td>0.4915</td><td>0.0995</td><td>0.2528</td><td>0.4114</td><td>Poor</td></tr><tr><td>Alt. 8</td><td>0.0443</td><td>26.5888</td><td>103.314</td><td>1543.5095</td><td>7,582,278.770</td><td>25.023</td><td>97.4</td><td>731.4</td><td>0.4894</td><td>0.1016</td><td>0.2518</td><td>0.4109</td><td>Average</td></tr><tr><td>Alt. 9</td><td>0.0443</td><td>26.5888</td><td>103.314</td><td>1543.5095</td><td>7,583,919.728</td><td>25.023</td><td>97.4</td><td>731.6</td><td>0.4894</td><td>0.1016</td><td>0.2518</td><td>0.4109</td><td>Excellent</td></tr><tr><td>Alt. 10</td><td>0.0438</td><td>26.5896</td><td>103.314</td><td>1992.1152</td><td>7,578,792.696</td><td>25.023</td><td>98.0</td><td>731.2</td><td>0.4908</td><td>0.1000</td><td>0.2524</td><td>0.4113</td><td>Average</td></tr><tr><td>Alt. 11</td><td>0.0436</td><td>26.5849</td><td>103.314</td><td>1992.1152</td><td>7,571,007.461</td><td>25.023</td><td>98.2</td><td>731.1</td><td>0.4917</td><td>0.0996</td><td>0.2528</td><td>0.4115</td><td>Poor</td></tr><tr><td>Alt. 12</td><td>0.0436</td><td>26.5849</td><td>103.310</td><td>1992.1152</td><td>7,572,648.419</td><td>25.023</td><td>98.2</td><td>731.3</td><td>0.4917</td><td>0.0996</td><td>0.2527</td><td>0.4114</td><td>Average</td></tr></table>

Please cite this article as: S. Fernandes, et al., A DSS for bicriteria location problems, Decision Support Systems (2013), http://dx.doi.org/10.1016/ j.dss.2013.09.014

## References

[1] L. Alçada-Almeida, J. Coutinho-Rodrigues, J. Current, A multiobjective modeling approach to locating incinerators, Socio-Economic Planning Sciences 43 (2009) 111-120.

[2] L. Alçada-Almeida, L. Tralhão, L. Santos, J. Coutinho-Rodrigues, A multiobjective approach to locate emergency shelters and identify evacuation routes in urban areas, Geographical Analysis 41 (2009) 9–29.

[3] AMARSUL, Relatório e Contas 2011, 2012(Accessed 27 July 2012, Retrieved from URL: http://www.amarsul.pt/public/documents/relatorio\_de\_contas\_2011.pdf).

[4] A. Bana e Costa, Três convicções Fundamentais na Prática do Apoio à Decisão, Pesquisa Operacional 13-1 (1993) 9–20(in Portuguese).

[5] M.E. Captivo, J. Clímaco, S. Fernandes, A bicriteria DSS dedicated to location problems, in: F. Adam, P. Humphreys (Eds.), Encyclopedia of Decision Making and Decision Support Technologies I, Information Science Reference, 2008, pp. 53–60.

[6] C. Chatzouridis, D. Komilis, A methodology to optimally site and design municipal solid waste transfer stations using binary programming, Resources, Conservation and Recycling 60 (2012) 89–98.

[7] R. Church, Geographical information systems and location science, Computers and Operations Research 29 (2002) 541–562.

[8] G. Cornuejols, M.L. Fisher, G.L. Nemhauser, Location of bank accounts to optimize <sup>fl</sup>oat: an analytic study of exact and approximate algorithms, Management Science 23 (1977).789-810

[9] I. Correia, M.E. Captivo, A Lagrangian heuristic for a modular capacitated location problem, Annals of Operations Research 122 (2003) 141–161.

[10] L. Dias, J. Clímaco, Additive aggregation with variable interdependent parameters: the VIP analysis software, Journal of the Operational Research Society 51-9 (2000) 1070–1082.

[11] J. Dias, M.E. Captivo, J. Clímaco, An interactive procedure dedicated to a bicriteria plant location problem, Computers and Operations Research 30 (2003) 1977–2002.

[12] EPA, United States Environmental Protection Agency, Waste Transfer Stations: a manual for decision-making, 2002, (Accessed 20 July 2012. Retrieved from URL: http://www.epa.gov/osw/nonhaz/municipal/pubs/r02002.pdf).

[13] E. Erkut, S. Neuman, A multiobjective model for locating undesirable facilities, Annals of Operations Research 40 (1992) 209–227.

[14] ESRI, ArcGIS Desktop 9.3 Help, 2012(Accessed 20 July 2012, Retrieved from URL: http://webhelp.esri.com/arcgisdesktop/9.3/index.cfm?TopicName=welcome).

[15] A. Falit-Baiamonte, J. Osleeb, An equity model for locating environmentally hazardous facilities, Geographical Analysis 32-4 (2000) 351–368.

[16] S. Fernandes, M.E. Captivo, J. Clímaco, SABILOC — Um Sistema de Apoio à Decisão para Análise de Problemas de Localização Bicritério, Pesquisa Operacional 27 (2007) 607–628(in Portuguese).

[17] S. Fernandes, M.E. Captivo, J. Clímaco, A GIS embedded decision support system for bicriteria location problems, in: A. Respício, F. Adam, G. Philips-Wren, C. Teixeira, J. Telhada (Eds.), Bridging the Socio-technical Gap in Decision Support Systems — Challenges for the Next Decade, IOS Press, 2010, pp. 271–281.

[18] S. Fernandes, M.E. Captivo, J. Clímaco, A multi-attribute analysis module for SABILOC — a DSS for location problems, in: A. Respício, F. Burstein (Eds.), Fusing DSS Into the Fabric of the Context, IOS Press, 2012, pp. 197–208.

[19] C. Ferreira, J. Clímaco, J. Paixão, The location-covering problem: a bicriterion interactive approach, Investigación Operativa 4 (1994) 119–139.

[20] Y. Gil, A. Kellerman, A multicriteria model for the location of solid waste transfer stations: the case of Ashdod Israel, GeoJournal 29-4 (1993) 377–384.

[21] R. Greene, R. Devillers, J. Luther, B. Eddy, GIS-based multiple-criteria decision analysis Geography Compass 5–6 (2011) 412–432

[22] M. Guignard, K. Spielberg, A direct dual method for the mixed plant location problem with some side constraints, Mathematical Programming 17 (1979) 198–228.

[23] D. Huff, De<sup>fi</sup>ning and estimating a trading area, Journal of Marketing 28-3 (1964) 34-38

[24] J. Hultz, D. Klingman, G. Ross, R. Soland, An interactive computer system for multicriteria facility location, Computers and Operations Research 8-4 (1981) 249 261.

[25] ILOG CPLEX Callable Library C API 11.0 Reference Manual, ILOG, 2007.

[26] M. Kim, E. Miller-Hooks, R. Nair, A geographic information system-based real-time decision support framework for routing vehicles carrying hazardous materials, Journal of Intelligent Transportation Systems 15-1 (2011) 28–41

[27] Ö. Kirca, N. Erkip, Selecting transfer station locations for large solid waste systems, European Journal of Operational Research 35 (1988) 339–349.

[28] J. Krarup, P.M. Pruzan, The simple plant location problem: survey and synthesis European Journal of Operational Research 12 (1983) 36–81.

[29] A. Lotov, V. Bushenkov, G. Kamenev, Interactive Decision Maps, Approximation and Visualization of Pareto Frontier Kluwer Academic Publishers, Boston, 2004.

[30] J. Malczewski, GIS-based multicriteria decision analysis: a survey of the literature, International Journal of Geographical Information Science 20-7 (2006) 703–726.

[31] MAOT, in: Ministério do Ambiente, do Ordenamento do Território e do Desenvolvimento Regional (Ed.), PERSU II — Plano Estratégico para os Resíduos Sólidos Urbanos 2007–2016, 2007, (Accessed 20 July 2012, Retrieved from URL: http://www.maotdr.goy.pt/Admin/Files/Documents/PERSU.pdf (in Portuguese)).

[32] MATHWORKS, MathWorks Documentation Center, 2013, (Accessed 28 June 2013, Retrieved from URL: http://www.mathworks.com/help).

[33] A. Murray, Advances in location modeling: GIS linkages and contributions, Journal of Geographical Systems 12-3 (2010) 335–354.

[34] V. Pareto, Manuale di Economia Politica, Societa Editrice, 1906.

[35] M. Rahman, M. Kuby, A multi-objective model for locating solid waste transfer facilities using an empirical opposition function, Information Systems and Operational Research 33 (1995) 34–49.

[36] C. Revelle, G. Laporte, The plant location problem: new models and research prospects, Operations Research 44-6 (1996) 864–873.

[37] G. Ross, R. Soland, A multicriteria approach to the location of public facilities, European Journal of Operational Research 4 (1980) 307–321.

[38] S. Sener, E. Sener, B. Nas, R. Karagüzel, Combining AHP with GIS for land<sup>fi</sup>ll site selection: a case study in the Lake Beysehir catchment area (Konya, Turkey), Waste Management 30-11 (2010) 2037–2046.

[39] S. Sener, E. Sener, R. Karagüzel, Solid waste disposal site selection with GIS and AHP methodology: a case study in Senirkent–Uluborlu (Isparta) Basin, Turkey, Environmental Monitoring and Assessment 173-1 (2011) 533–554.

[40] R. Soland, Multicriteria optimization: a general characterization of ef<sup>fi</sup>cient solutions, Decision Sciences 10 (1979) 26–38.

[41] R. Steuer, Multiple Criteria Optimization: Theory, Computation and Application, John Wiley & Sons, 1986

[42] R. Suárez-Vega, D.R. Santos-Penate, P. Dorta-González, M. Rodríguez-Díaz, A multi-criteria GIS based procedure to solve a network competitive location problem, Applied Geography (2011) 282–291.

[43] L. Tralhão, J. Coutinho-Rodrigues, L. Alçada-Almeida, A multiobjective modelling approach to locate multi-compartment containers for urban-sorted waste, Waste Management 30 (2010) 2418–2429.

[44] P. Vincke, Decision-Aid, Wiley, 1989.

[45] G. Wang, L. Qin, G. Li, L. Chen, Land<sup>fi</sup>ll site selection using spatial information technologies and AHP: a case study in Beijing China, Journal of Environmental Management 90-8 (2009) 2414–2421.

[46] M. Wyman, M. Kuby, A multiobjective location–allocation model for assessing toxic waste processing technologies, Studies in Locational Analysis 4 (1993) 193–196.

[47] M. Wyman, M. Kuby, Proactive optimization of toxic waste transportation, location and technology, Location Science 3-3 (1995) 167–185.

[48] J. Zhang, J. Hodgson, E. Erkut, Using GIS to assess the risks of hazardous materials transport in networks, European Journal of Operational Research 121 (2000) 316-329

[49] K. Zografos, K. Androutsopoulos, A decision support system for integrated hazardous materials routing and emergency response decisions Transportation Research Part C.16 (2008).684-703

Sérgio Flores Fernandes is a Professor at the Department of Mathematics, Polytechnic Institute of Setúbal — Higher School of Engineering and Technology, and a researcher collaborator at the Operations Research Center. He received his M.Sc. degree in Operations Research from the University of Lisbon in 2000. Currently, he is preparing his Ph.D. degree in System Analysis. His research interests include multicriteria location problems, decision support systems and geographical information systems.

Maria Eugénia Captivo is an Associate Professor of Operations Research at the Faculty of Sciences, University of Lisbon, and a researcher at the Operations Research Center. She obtained her Ph.D. in Operations Research in 1988 and the title of “Agregação” in 2005, both at the University of Lisbon. Her current research interests are in multicriteria location problems, combinatorial optimization, network optimization, production planning, cutting and packing. Her works have been published by journals such as Computers & Operations Research, European Journal of Operational Research, 4OR — A Quarterly Journal of Operations Research, Annals of Operations Research, Journal of Decision Systems, Journal of Global Optimization, CEJOR, OR Spectrum, TOP, IMA Journal of Management Mathematics, Location Science, Operational Research, JORBEL, Investigação Operacional, Pesquisa Operacional Computación y Sistemas and Portugaliae Mathematica.

João Carlos Namorado Clímaco is a retired Full Professor at the Faculty of Economics of the University of Coimbra. Actually he is a researcher and Member of Conselho Geral of INESC-Coimbra (the research unit in which he is integrated). He obtained a Master of Science Degree in “Control Systems” at the Imperial College of Science and Technology “, University of London (1978): the “Diploma of Membership of the Imperial College of Science and Technology" (1978): the Ph.D. in Optimization and Systems Theory. Electrical Engineering Department University of Coimbra (1982): and the title of “Agregação" at the University of Coimbra (1989), He was awarded with: “Conference Chairman Award" 1995, and “The Georg Cantor Award”, 2013, by the International Society on Multiple Criteria Decision Making and Grande O<sup>fi</sup>cial da Ordem do Rio Branco, Brazil — 1996. He is Past Vice-President of ALIO — Latin Ibero American OR Association, Past Vice-President of the Portuguese OR Society, and Past Member of the International Executive Committee of the International Society on Multiple Criteria Decision Making. He is a member of the IFIP-WG 8.3-Decision Support Systems. He belongs to the Editorial Board of the following Scienti<sup>fi</sup>c Journals: “Group Decision and Negotiation”, “International Transactions in Operational Research”, and “International Journal of Decision Support Systems”. He is also a member of the Editorial Board of the University of Coimbra Press
