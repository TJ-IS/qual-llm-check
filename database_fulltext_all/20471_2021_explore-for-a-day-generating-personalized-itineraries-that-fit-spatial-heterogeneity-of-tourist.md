---
otero_id: 20471
otero_key: "AQR4GCCP"
title: "Explore for a day? Generating personalized itineraries that fit spatial heterogeneity of tourist attractions"
authors: "Haipeng Ji; Weimin Zheng; Xinyi Zhuang; Zhibin Lin"
year: "2021"
journal: "Information & Management"
doi: "10.1016/j.im.2021.103557"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Explore for a day? Generating personalized itineraries that fit spatial heterogeneity of tourist attractions

![](/api/attachments/AQR4GCCP/fulltext/images/e3602944ee2fc8f90de94877286aa9795104dfe4bc4fe0006e75f3b9f20a6e65.jpg)

Haipeng Ji <sup>a</sup>, Weimin Zheng <sup>a,\*</sup>, Xinyi Zhuang <sup>a</sup>, Zhibin Lin <sup>b</sup>

<sup>a</sup> School of Management, Xiamen University, 422 South Siming Road, 361005, Xiamen, China

<sup>b</sup> Durham University Business School, Mill Hill Lane, Durham DH1 3LB, United Kingdom

## A R T I C L E I N F O

Keywords: Recommender system Tourist trip design problem Heuristic approach Personalization Spatial structure Tourism attraction

## A B S T R A C T

Recommender systems are widely adopted by firms as an innovative personalization tool across various in dustries. Most of the existing tour recommender systems treat the spatial structure of tourist attractions as a single type, which neglects the spatial heterogeneity among these attractions. This study attempts to address this problem by modeling the spatial heterogeneity in the design of personalized trips. We propose a two-phase heuristic approach, which involves an improved artificial bee colony algorithm and a differential evolution al gorithm. The results of a field experiment confirm that our new model outperforms the benchmark models in maximizing customer utilities.

## 1. Introduction

Planning a one-day exploration in various places of interest at an unfamiliar destination is time-consuming. A tour recommender system can help users plan a dream holiday exploration by automatically generating a personalized travel plan that suits their needs and prefer ences. A recommender system generally uses content-based and/or collaborative filtering algorithms by considering the attributes of a product that a consumer liked or purchased in the past (content-based) or the similarity between a consumer and others according to their historical like or purchase data (collaborative filtering) [23]. The design of a tour recommendation is more complex than that of a product recommendation, as it involves recommending the attractions or point of interest (POIs) and a travel route that connects the POIs [21].

Developers of a tour recommendation have to consider numerou real-life constraints, among which are the temporal and spatial con straints [25]. In terms of the spatial structure, there are two basic types of attractions, namely the node- and line-shaped attractions, which often exist simultaneously in a tourism destination. For line-shape attractions, such as greenway, coastline, river, and street, the profits (or utility) for tourists are associated with arcs, rather than vertices and their spatial position changes when they finish visiting the attractions. Despite the advances in tour recommender systems, most studies treat all attractions as the same in terms of spatial structure and ignore the multiple entrances/exits of attractions, thereby restricting the modeling of vertices or arcs. As a result, these systems may fail to capture the practical properties of attractions with large areas and multiple entrances/exits. For example, Yellowstone National Park has five entrance stations, each of which is far from the others. Therefore, choosing appropriate stations to enter and leave the park while planning the trip is essential. Moreover, previous studies put relatively little emphasis on optimizing the time for exploration or enjoyment at each attraction, which is a pivotal part of tourist experiences and must not be ignored in the recommender system design [46].

This study aims to tackle the above problems by considering tourist attractions’ spatial structure and the time spent at each attraction for generating a personalized travel itinerary. Specifically, we consider the heterogeneity of attractions’ spatial structure, that is, the in homogeneity and complexity of spatial structure, and categorized it into three types: (a) POI (node-shape attraction with a unique and identical entrance and exit, b) line of interest (LOI, line-shape attraction with only one entrance/exit at both ends), and (c) area of interest (AOI, large area with multiple entrances/exits). In addition, the time spent at attractions is considered an optimization variable. The complexity of such a prob lem results from the correlation among attraction selection, sequencing determination, choice of entrances/exits and time allocation, and mul tiple constraints. We tackle this mixed tourist trip design problem by developing a two-phase heuristic approach (HA), which involves an improved artificial bee colony (ABC) algorithm and a differential evo lution algorithm (DEA). Our approach differs from existing trip design methods in several ways. First, our proposed approach applies a variantform nectar with four pheromones to code the solution. Second, it de signs a cell array embedded in different dimension matrices for improved storing and managing of the relationship among vertices. Third, it improves the search ability and optimization performance of the algorithm by adjusting the evolution structure of ABC and adding a new group of bees. Finally, it also improves the evolution structure by introducing an adaptive evolutionary parameter to reach an equilibrium of the solution quality and algorithm efficiency.

This study makes three major contributions to information systems literature. First, this study advances recommender system design by offering an improved approach that integrates spatial heterogeneity with other features and influencing factors, whereas most previous recommender system studies mainly focus on recommending POIs, without considering the unique spatial features of each POI. Second, our system design incorporates the actual available entrances and exits of each attraction; thus, it avoids unnecessary detours and allows more time for the users to explore and enjoy their visit. Third, our design further considers the access order, access time, and visitors’ personal preferences. As a result, the recommendations generated from our approach can closely match users’ preferences while meeting their time budgets, which outperform those generated from the baseline methods.

The remaining sections of this paper are organized as follows. Sec tion 2 reviews the design of recommender systems and, specifically, tourist trip design. Section 3 formalizes a high-efficient mathematical model to address the mixed tourist trip design problem. Section 4 pre sents our proposed HA framework. Section 5 examines the effectiveness of our method through a field experiment. Finally, Section 6 discusses the results and offers directions for further studies.

## 2. Literature review

## 2.1. Tourism recommender system

The design of a recommender system is usually based on one or both of the two basic modeling approaches: content-based and collaborative filtering algorithms [23]. Content-based systems focus on the attributes of a product that a consumer liked or purchased in the past, whereas collaborative filtering recommenders are based on the similarity be tween a consumer and others according to their historical like or pur chase data. Many recommender systems use a combination of both approaches. Research on the POI recommender system has explored four major techniques, including the collaborative filtering-based, matrix factorization-based, probabilistic, and link-based models [36]. First, both user-based and friend-based collaborative filtering have been adapted for recommending POIs. Second, various matrix factorization models have been leveraged, together with a combination of multiple latent factors. Third, probabilistic models have been used to capture the different influencing factors, including social, sequential, geographical, and temporal influences on user preferences to generate recommenda tions. Fourth, link-based models have been used to present graphs of the links between users and POIs for recommendations. Integrating the various factors with algorithmic techniques improves the tour recom mendations [36].

The design of a tour recommendation should consider numerous real-life constraints, in addition to that of a product or POI recommen dation. The temporal and spatial constraints are the key influencing factors that should be integrated into the design [25]. In a typical day-trip excursion at a destination, a day reflects the constraint of time, and the destination offers the space for tourist exploration. The temporal constraints include the limit of time allocated for the tour including time at attractions and travel between attractions. The design thus needs to incorporate various factors, such as crowdedness and time for queuing at the attractions, transport modes used, traffic congestion, and uncer tainty in time for travel [9, 44]. Moreover, the tour recommender system has to consider factors such as user demographics [4], traveling group size [3], real-time location, and user’s personal interests [40]. Contex tual factors such as the day, time, season, and weather should also be taken into account [29].

## 2.2. Spatial constraints for a tourist trip design

The spatial constraints for a tourist trip design include the need for the start and end at certain locations, including the location of the hotel the tourist stays, stations, attractions, and specifically the entrance and exit of an attraction. Most studies abstract tourist attractions as vertices and assume that tourists enter and leave attractions at the same location (see a summary in Table 1). These works are sufficient for designing routes at attractions with single entrance/exit, such as museums,

## Table 1

Studies on personalized tour design.

<table><tr><td>Authors</td><td>Contributions</td><td>Models</td><td>Factors</td></tr><tr><td>Lee, et al. [22]</td><td>An ontological recommendation multi-agent.</td><td>Ant colony optimization</td><td>Context information; Tourists&#x27; requirements; Tainan City travel ontology.</td></tr><tr><td>Rodriguez et al. [34]</td><td>A tool that formalizes a mathematical model and interactive multi-criteria technique.</td><td>Tabu search</td><td>Multiple tourists&#x27; objectives; Interactive process with the tourist.</td></tr><tr><td>Hsu et al. [16]</td><td>An intelligent recommender system for tour decision-making.</td><td>None (Based on Google API)</td><td>Tourist preference prediction.</td></tr><tr><td>Tsai and Chung [41]</td><td>A route recommender system based on tourist behavior and real-time information.</td><td>Route generation algorithm</td><td>Tourist behaviors similarity; Current facility queuing situation.</td></tr><tr><td>Liu, et al. [26]</td><td>A recommender system that focuses on real-time personalized tour design.</td><td>Route generated algorithm</td><td>Real-time traffic information.</td></tr><tr><td>Cenamor, et al. [2]</td><td>A system based on information gathered from social networks.</td><td>Automated planning approach</td><td>User expectations for POIs; POIs popularity.</td></tr><tr><td>Kotiloglu, et al. [21]</td><td>A framework named “Filter-first, Tour-second”.</td><td>Iterated tabu search</td><td>Mandatory points; Optional points.</td></tr><tr><td>Sun and Lee [38]</td><td>A four-phase framework based on contents gathered from photo-sharing social networks.</td><td>Tour recommendations by sharing photos approach</td><td>Landmark topics; User characterization.</td></tr><tr><td>Zheng, et al. [48]</td><td>A combination of difference evolution algorithm and a genetic algorithm</td><td>Genetic algorithm and differential evolution</td><td>esthetic fatigue; Variable sightseeing value.</td></tr><tr><td>Liao and Zheng [24]</td><td>A stochastic environment that is time-dependent in the tourist trip design problem.</td><td>Heuristic algorithm based on random simulation</td><td>Time-dependent stochastic environment like travel times and wait times.</td></tr><tr><td>Zheng and Liao [46]</td><td>A heuristic approach using Pareto optimality to meet group member preferences.</td><td>Nondominated sorting heuristic algorithm</td><td>Heterogeneous preferences of group members.</td></tr><tr><td>Zheng, et al. [45]</td><td>A two-level heuristic approach with consideration of hotel selection.</td><td>Memetic algorithm</td><td>Hotel selection.</td></tr><tr><td>Zheng, et al. [47]</td><td>A model that considers transport mode choice in the day itinerary design</td><td>Nondominated sorting heuristic algorithm</td><td>Transport mode.</td></tr></table>

galleries, small squares, or parks. However, the practical properties of other types of attractions, such as greenway, coastline, river, and street, are not mined. When tourists visit such attractions, the profits are associated with arcs, rather than vertices [27, 28], and their spatial position changes when they finish visiting the attractions [37]. Given these differences, abstracting attractions as vertices may not be feasible or ideal in practice [6].

Several recent studies treat attractions as arcs and regard tourist trip design problem as a variant of arc orienteering problem. For example, Souffriau et al. [37] formulated the cycle route planning and proposed a heuristic solution approach and presented a mathematical optimization model. Verbeeck et al. [43] extend the arc orienteering problem, consider the different profits of various direction arcs, and introduce a branch cutting method to solve the bicycle journey design problem with the same end and starting points. Lu and Shahabi [28] introduce a variant of arc orienteering problem and used a set of meta-heuristic algorithms to tackle the problem in search of the optimal travel path in large-scale road networks. Lu et al. [27] proposed a two-time-dependent arc orienteering problem, under which the travel time and benefit value depend on time.

The two types of attractions (node- and line-shape) may exist simultaneously in tourism destinations, which make the tour itinerary design a typical combination of orienteering problem and arc orien teering problem [42, 45]. Gavalas et al. [8] abstract the multiple-day itinerary design problem with node- and line-shape attractions and proposed the first metaheuristic approaches to tackle it. Mrazovic et al. [31] also model this issue and introduce a variable neighborhood search to deal with this problem.

Despite the progress made in the recommender system research, existing studies continue to ignore the discussion and solution of spatial heterogeneity. First, prior literature focuses on the information at the tourist and attraction levels to recommend tours $\left[ 2 , \ 1 6 , \ 3 8 \right]$ . Most studies assume that all the attractions have the same spatial structure and that tourists enter and leave attractions at predefined locations $[ 2 ,$ $1 6 , 2 4 , 3 8 , 4 5 , 4 8 ]$ . This situation is impractical in many cases, especially for attractions with large areas and multiple entrances/exits $( \boldsymbol { \mathrm { e . } } \boldsymbol { \mathrm { g . } } ,$ , Yellowstone National Park). Considering that the paths (travel distance) from different exits of an attraction to different entrances of another attraction are completely different [17], which further affects tourist behavior, ignoring the choice of attractions’ entrances/exits may lead to potentially infeasible or suboptimal solutions (travel time increased and travel experience decreased). For example, although Liu et al. [26] and Liao and Zheng [24] take traffic/travel time into account when modeling, ignoring the spatial heterogeneity of attractions results in the underperformance of their approach in solving our problem. Second, existing studies on the mixed orienteering problem and the mixed tourist trip design problem assign a fixed value to the time spent on the vertex [8, 31]. However, in reality, the lengths of time that each tourist wishes to take at a vertex may vary. Hence, vertex time allocation should also be optimized in line with tourists’ characteristics [45, 46].

Moreover, space variables, such as attraction, sequencing, and the entrances/exits of an attraction) are discrete variables, whereas time is a continuous one as the simultaneous optimization of spatial and temporal structure factors present additional modeling challenges. Consequently, we consider the following improvements. First, we fully consider the heterogeneity of tourist attractions’ spatial structure and the duration spent at each vertex by proposing a two-phase HA to design additional reasonable trips. Second, with the recognition of the complexity of the mixed tourist trip design problem, we use multiple methods to reach an equilibrium of the solution quality and algorithm efficiency.

## 3. Mathematical model

A mathematical model can be developed to introduce the research problem. Table 2 lists the description of variables used. Let V be the set of vertices, including attractions $( V _ { A } = \{ a _ { 1 } , ~ a _ { 2 } , ~ . . . , ~ a _ { N 2 } \} )$ , departing locations $( V _ { I } ) _ { i }$ , and ending locations $( V _ { F } ) .$ . As previously stated, three types of attractions are involved in this study: POI, LOI, and AOI. POI and LOI can be regarded as specific forms of AOI. A feasible solution of the problem consists of M stages $\varLambda _ { 1 } , \varLambda _ { 2 } , . . . ,$ Λ<sub>M</sub> with $\Lambda _ { j } \in V$ such that $\Lambda _ { I } \in V _ { I } , \Lambda _ { M } \in V _ { F } , \left\{ \Lambda _ { 2 } , \cdots , \Lambda _ { M - 1 } \right\} \subset V _ { A } ,$ the arrival time at $\varLambda _ { 1 }$ is set to $\tau .$ . For the attractions visited at each stage $\varLambda _ { j } ,$ , its actual visit time $t _ { j } ^ { s }$ should not take place outside its time window $[ t o _ { i } , t c _ { i } ]$ where to is the opening time and $t c _ { i }$ is the closing time. However, the earlier or the later arrival time $t _ { j } ^ { a }$ will cause unnecessary waiting time or miss the favorite attraction. The time budget for the trip equals to $T _ { m a x } ,$ which contains the duration of $\varLambda _ { j }$ and the travel time between $\varLambda _ { j - 1 }$ and $\varLambda _ { j }$ . For clarity, an example of a fivestage route $\left( M = 5 \right)$ is shown in Fig. 1, where the solid red lines and dots represent a visit to a vertex (a stage), the dotted lines represent the road between each stage. Compared with the models built, when we consider the impact of attractions’ heterogeneity on tourist trip design, our model introduces the number of entrances and exits of vertices and the influ ence of the selected entrances and exits on the travel time between two adjacent stages.

Table 2  
Mathematical variables

<table><tr><td>Variable</td><td>Description</td></tr><tr><td> $V_I$ </td><td>Set of the initial starting locations of the destination,  $i = 1, 2, ..., N_1$ </td></tr><tr><td> $V_A$ </td><td>Set of the attractions of the destination,  $i = 1, 2, ..., N_2$ </td></tr><tr><td> $V_F$ </td><td>Set of the final ending locations of the destination,  $i = 1, 2, ..., N_3$ </td></tr><tr><td> $V$ </td><td>Set of vertices,  $V = V_I \cup V_A \cup V_F$ </td></tr><tr><td> $N$ </td><td>Number of vertices,  $N = N_1 + N_2 + N_3$ </td></tr><tr><td> $EN_i^k$ </td><td>kth entrance of  $v_i$ </td></tr><tr><td> $EX_i^k$ </td><td>kth exit of  $v_i$ </td></tr><tr><td> $K_i^{EN}$ </td><td>Number of entrances for  $v_i$ </td></tr><tr><td> $K_i^{EX}$ </td><td>Number of exits for  $v_i$ </td></tr><tr><td> $T_{max}$ </td><td>Budgeted time available for the tourist</td></tr><tr><td> $\tau$ </td><td>Arrival time at the destination</td></tr><tr><td> $n_i$ </td><td>Number of discrete visits to vertex  $v_i$ </td></tr><tr><td> $M$ </td><td>Number of total stages in the trip (i.e., the sum of ni,  $M = \sum n_i$ ,  $i = 1, 2, ..., N$ )</td></tr><tr><td> $\Lambda_j$ </td><td>Vertex visited at the  $j$ th stage,  $j = 1, 2, ..., M$ </td></tr><tr><td> $[to_i,tc_i]$ </td><td>Time windows of  $v_i$ </td></tr><tr><td> $t(\Lambda_j, \Lambda_{j+1})$ </td><td>Travel time between  $\Lambda_j$  and  $\Lambda_{j+1}$ </td></tr><tr><td> $t_j^a$ </td><td>Arrival time at vertex  $\Lambda_j$ </td></tr><tr><td> $t_j^s$ </td><td>Actual start time visiting vertex  $\Lambda_j$ </td></tr><tr><td> $t_j^e$ </td><td>Departure time from vertex  $\Lambda_j$ </td></tr><tr><td> $p_i$ </td><td>Tourist&#x27;s preference value for  $v_i$ ,  $p_i \in [0,1]$ </td></tr><tr><td> $t_i$ </td><td>Average time spent at  $v_i$  by previous tourists</td></tr><tr><td> $x_{ij}$ </td><td>If the tourist visits vi at the  $j$ th stage, set  $x_{ij} = 1$ ; otherwise, 0</td></tr><tr><td> $y_{ij}$ </td><td>If a visit to  $v_i$  is followed by a visit to  $v_j$ , set  $y_{ij} = 1$ ; otherwise, 0</td></tr></table>

## 3.1. Model objective

The model’s objective is to maximize the utility of tourists under numerous constraints. Considering that tourists may repeatedly visit a landmark attraction during their tour [41], let n represent the number of discrete visits to vertex $\nu _ { i \cdot }$ In Eq. (1), integer M denotes the number of the stages, and N represents the number of vertices at the attraction:

$$
M = \sum_ {i = 1} ^ {N} n _ {i}\tag{1}
$$

The utility at each stage obtained by an individual tourist is mainly determined by the vertex visited at that stage $( \varLambda _ { j } )$ . It is closely related to the length of time spent at the corresponding vertex and $p _ { i }$ for $\varLambda _ { j } .$ . In tourist destinations, a unit time stay in an attraction is regarded as a commodity [35]. According to the law of diminishing marginal utility, marginal satisfaction decreases as consumers purchase more of the same product [1]. Owing to the esthetic fatigue of tourists in a similar way, as the duration a tourist stays at the same vertex increases, the marginal utility decreases [24]. Under this consideration, the utility gained by the tourist at jth stage can be calculated by Eq. (2) according to the duration that needs to be optimized and the preference value provided by tourists. In this equation, $M S _ { i } ( t )$ denotes the marginal sensation acquired by the tourist from v<sub>i</sub> at moment $t ,$ a non-negative decreasing function of time. We set x as a 0–1 discrete variable: if the tourist visits v at the jth stage, $x _ { i j } = 1 ;$ otherwise, 0. t<sup>s</sup> indicates the start time at vertex $\Lambda _ { j } ,$ whereas $t _ { j } ^ { a }$ is arrival time at $\varLambda _ { j } .$ . These two values are usually unequal because the time windows of the vertices may result in waiting time. Thus, $t _ { j } ^ { s }$ can be obtained as follows (see Eq. (3)):

![](/api/attachments/AQR4GCCP/fulltext/images/2a81e7eab491cf7458c0559dad1f9ae65e3f44a653b66e0e06c3935426cb1b7b.jpg)  
Fig. 1. Illustration of a tourist route.

$$
u _ {j} = \int_ {t _ {j} ^ {s}} ^ {t _ {j} ^ {e}} \left\{\sum_ {i = 1} ^ {N} \left[ M S _ {i} (t) \cdot p _ {i} \cdot x _ {i j} \right] \right\} d t\tag{2}
$$

$$
t _ {j} ^ {s} = \max \left[ t _ {j} ^ {a}, t o _ {i} \right]\tag{3}
$$

We suppose that tourists obtain zero utility while waiting and during traffic. Thus, the utility can be obtained as follows:

$$
u = \sum_ {j = 1} ^ {M} u _ {j}\tag{4}
$$

## 3.2. Model constraints

A tour route design has personalized and permanent technical con straints. Implementing permanent technical constraints ensures the validity and real meaning of the designed routes, as shown in Eqs. (5)– (10), whereas implementing personalized constraints to ensure the trip is within the time budget limit is the premise to meet an individual’s needs and preferences [34], as illustrated in Eq. (11). Specifically, Eqs. (5) and (6) set a limit that a tourist starts her/his trip at one of the initial starting locations and ends the trip at one of the final arrival locations. Eq. (7) guarantees that only one attraction can be visited per stage, from the second one to the M− 1th stages of the entire trip:

$$
\sum_ {v _ {i} \in V _ {I}} x _ {i 1} = \sum_ {v _ {j} \in V _ {F}} x _ {j M} = 1\tag{5}
$$

$$
\sum_ {j = 1} ^ {M} \sum_ {v _ {i} \in V _ {I}} x _ {i j} = \sum_ {j = 1} ^ {M} \sum_ {v _ {i} \in V _ {F}} x _ {i j} = 1\tag{6}
$$

$$
\sum_ {v _ {i} \in V _ {A}} x _ {i j} = 1, j = 2, 3, \dots , M - 1\tag{7}
$$

Eqs. (8)–(9) ensure the connectivity of time and path, where $y _ { i j }$ is a 0–1 discrete variable. If a visit to v is followed by a visit to $\nu _ { j } ,$ then we se $y _ { i j }$ to 1; 0, otherwise. If a tourist visits $\nu _ { i }$ at the jth stage and enters $\nu _ { i }$ from the kth entrance. then we set 0–1 discrete variable $g _ { i j k } = 1 ;$ otherwise, $g _ { i j k } = 0$ . Similarly, if a tourist visits $\nu _ { i }$ at the jth stage and leaves $\nu _ { i }$ from the kth exit, then we set 0–1 discrete variable $h _ { i j k } = 1$ ; otherwise, $h _ { i j k } =$ 0. Eq. (10) restricts that a tourist enters through one of the entrances to visit the vertex and then leaves through one of the exits. $\operatorname { E q . } \left( 1 1 \right)$ limits the total visit time of the trip to a maximum time budget $T _ { m a x } ,$ , where $t _ { M } ^ { a }$ is the arrival time at $\varLambda _ { M }$ and τ is the time that the tourist starts the trip:

$$
t _ {j} ^ {e} + t \left(\Lambda_ {j}, \Lambda_ {j + 1}\right) = t _ {j + 1} ^ {a}, (\forall j = 1, 2, \dots , M - 1)\tag{8}
$$

$$
\sum_ {v _ {i} \in \boldsymbol {V} _ {I} \cup \boldsymbol {V} _ {A}} y _ {i j} - \sum_ {v _ {k} \in \boldsymbol {V} _ {A} \cup \boldsymbol {V} _ {F}} y _ {j k} = 0, \forall v _ {j} \in \boldsymbol {V} _ {\boldsymbol {A}}; v _ {i} \neq v _ {j}, v _ {j} \neq v _ {k}\tag{9}
$$

$$
\sum_ {k = 1} ^ {K _ {i} ^ {E N}} g _ {i j k} = \sum_ {k = 1} ^ {K _ {i} ^ {E X}} h _ {i j k} = x _ {i j}\tag{10}
$$

$$
t _ {M} ^ {a} \leq \tau + T _ {\max}\tag{11}
$$

## 4. Solution approach

The problem proposed in this study is a generalization of the orien teering problem, which has been proven to be NP-hard (class of prob lems that are at least as hard as the hardest problems in NP) [13]. This implies that deriving the optimal solution of the model in a limited time is difficult. Moreover, our model considers the influence of spatial het erogeneity on tour recommendation, which makes it more complex and increases the risk of falling into local optimum. Therefore, we propose a two-phase HA that combines improved ABC and DEA, including the preprocessing and evolution phases. ABC algorithm, first introduced by Karaboga [18]. DEA is specifically applicable to solving continuous optimization problems. The comprehensive framework of HA is illus trated in Fig. 2. The details of each phase are presented in Sections 4.1 and 4.2.

## 4.1. Preprocessing phase

In the preprocessing phase, four tasks are conducted: attraction characterization, information cell array construction, solution coding, and initial solution set (ISS) generation.

As previously mentioned, a tour route may contain attractions with different spatial structures: POI, LOI, and AOI. For example, the route as shown in Fig. 3(a) means that the tourist starts her/his trip from the initial start location (v ) and then successively visits v , v , v , v , and v . Finally, the trip ends at the final end location (v ). For the visited at tractions, v<sub>3</sub> and v<sub>7</sub> are POIs, v<sub>5</sub> is an AOI, and v<sub>6</sub> and v<sub>2</sub> are LOIs. To facilitate the subsequent processing of the approach, each entrance and exit of vertices should also be characterized. Therefore, the information of attractions in Fig. 3(a) is transformed to Fig. 3(b).

Certain vertices contain multiple entrances and exits. This leads to multiple paths between a pair of vertices. For example, six paths exist between the pair $( \nu _ { 5 } , \nu _ { 6 } )$ (as shown in red lines in Fig. 3(a)). Choosing different entrances/exits indicates that different path selections are available, which may correspond to different travel times. This infor mation can significantly affect trip optimization. Most previous studies use a regular matrix to store information without considering the mul tiple entrances/exits of attractions. Given that the existing methods are incapable of solving the problem concerned, we design a cell array embedded in different dimension matrices, which denote a distance matrix between two vertices. For clarity, we provide a specific example to illustrate such a structure, as shown in Fig. 4(a). The structure con tains the distance information among vertices $( \nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { 7 } )$ . As dis played in Fig. $^ { 3 , }$ six paths exist between the pair (v , v ) and two paths between the pair $( \nu _ { 6 } , \nu _ { 2 } )$ . Thus, two cell arrays $( \nu _ { 5 } \to \nu _ { 6 } ,$ , shown in the red grid; $\nu _ { 6 } {  } \nu _ { 2 } ,$ presented in the blue grid) denote two matrices with different dimensions, as illustrated in Fig. 4(b).

After characterizing the attractions and constructing the information cell array, we must code the solutions. Most evolution algorithms require an advanced determination of solution dimensions [11], which cannot be applied to the present problem owing to possible variations in the vertices that a tourist visits. To code the solutions, Zheng et al. [48] design a double-layer, variable-length chromosome that involves vertex selection, sequencing, and time allocation. In addition to these three elements, our study must determine the entrances/exits of the chosen vertices. Thus, we introduce a variable-form nectar with four phero mones to code the solutions. The two upper pheromones are the vertex selection of the route and the time spent at each chosen vertex, whereas the two lower pheromones indicate the entrances and exits of the chosen vertices. This solution coding is illustrated with an example in Fig. $^ { 5 , }$ which depicts that the tourist starts the trip at $\nu _ { 1 } ,$ then successively visits v , v , v , v , $\nu _ { 2 } ,$ and $\nu _ { 4 } ,$ where the trip ends. At v , v , v , $\nu _ { 6 } ,$ and $\nu _ { 2 } ,$ the time spent are 69, 18, 6, 43, and 26 min, respectively. The entrance and exit for each chosen vertex are $( E N _ { 1 } ^ { 1 } , E X _ { 1 } ^ { 1 } ) , ( E N _ { 3 } ^ { 1 } , E X _ { 3 } ^ { 1 } ) , ( E N _ { 7 } ^ { 1 } , E X _ { 7 } ^ { 1 } )$ , (EN<sup>3</sup>, $E X _ { 5 } ^ { 2 } ) . . . , ( E N _ { 4 } ^ { 1 } , E X _ { 4 } ^ { 1 } )$ , as shown in the red lines in Fig. 5(a).

Each employed bee (EB) corresponds to a food source (solution). The quality of ISS strongly influences the performance of our approach. To ensure the diversity of solutions, SN (population size) solutions are generated based on the constraints as presented in Section 3.2, and they are randomly assigned to the EBs.

## 4.2. Evolution process

The goal of the evolution process is to obtain solutions with greater utility, matching an individual tourist’s needs. As described in Section 4.1, a solution is coded as a variable-form nectar with four pheromones, including the selection and sequencing of vertices, the length of time at each vertex, and the choice of vertices’ entrances and exits. We use an improved ABC algorithm and a DEA to evolve these four variables. The improved ABC algorithm optimization includes three discrete variables: selection of vertices, sequencing of vertices, and the choice of vertices entrances and exits. The DEA is applied to optimize the visit time for the corresponding vertices.

![](/api/attachments/AQR4GCCP/fulltext/images/8bdeffb95ac225fe9b0f7fb57997d03ce8849a5a0d0f9e377aed8f9026f95a47.jpg)  
Fig. 2. Procedure of the proposed method.

![](/api/attachments/AQR4GCCP/fulltext/images/810bc8b193d91b832966944a1ab6592be80cbefca1977deeec4cf3e4bf68cf5e.jpg)  
Fig. 3. Example of attraction characterization.

![](/api/attachments/AQR4GCCP/fulltext/images/3c67f6e3b6f000aef11c4a6d3ea091f18badf37221d33894659ea1c148e33f8b.jpg)  
(a)

![](/api/attachments/AQR4GCCP/fulltext/images/8dd22402723a36f4d8917dcb9e6460068f63cd4209a38e6905cff0fa94dbdec9.jpg)

Fig. 4. Cell array embedded in different dimension matrices.  
![](/api/attachments/AQR4GCCP/fulltext/images/b1101476c27225bf7152689b5b74fcdadb079b1eade94ab57e85c6eeb5b954e4.jpg)  
Fig. 5. Examples of solution coding.

The ABC algorithm is developed by Karaboga [18] based on hon eybees’ behavior. In the ABC system, EBs and onlooker bees (OBs) select food sources based on their experiences and nestmates and then adjust their positions. Scout bees (SBs) fly and randomly select food sources without using experiences. The ABC system combines local and global search methods. Local search methods are used by EBs and OBs, whereas global search methods are used by SBs. Given the simplicity, flexibility, and robustness of the ABC algorithm, it has been extensively used in optimization problems with multiple variables [5, 19, 20, 30, 32, 33, 39]. Realizing that our study involves interacting elements, we improve ABC in two ways. (1) Four neighborhood structures are embedded in ABC to enhance the local search ability. (2) A new group of bees named “employed scout bee (e-SB)” is designed to further optimize the choice of entrances/exits of attractions.

## 4.2.1. EB process

A solution is denoted as a variable-form nectar with four phero mones. In this study, the EBs focus on the optimization of the first pheromone, that is, the selection and sequencing of vertices. Each EB is linked with a particular food source (solution). At each iteration, EBs search for new food sources and assess their fitness (the utility of the solution). When the food source position cannot be improved further, ABC algorithm abandons the food source after a predetermined number of iterations limit [18]. However, to solve the mixed tourist trip design problem, we suggest the extract-insert search strategy to allow the al gorithm a greater opportunity to escape from a local optimum. All four applied neighborhood structures are introduced: insertion (select a vertex and then insert it into the optimal location), inversion (reverse the sequence between two vertices), swap (select two vertices and then exchange their positions), and extract-insert (exclude a random number of vertices and insert non-included vertices). For the detailed illustration of these neighborhood structures, we refer to Cura [5].

We suppose that the solution loaded on an EB is the current solution (CS), and the fitness value of CS (f(CS)) represents the utility of the corresponding solution, which can be obtained through Eq. (4). First, the EB randomly selects one of the above neighborhood structures to search for a new solution (NS). The fitness value of NS (f(NS)) is also calculated based on Eq. (4). If $( f ( N S ) > f ( C S ) )$ , then a good solution is found. Subsequently, the CS of the EB is replaced with the NS, and the number of trials (t(EB)) is reset to 0; otherwise, the EB keeps the current solution, and t(EB) is added by 1 $\mathbf { \nabla } ( \mathrm { i } . \mathrm { e } . , t ( E B ) = t ( E B ) + 1 )$

## 4.2.2. OB process

After the EB searching behavior is completed, EBs return to the hive with information about the food sources (solutions) and head to the dance area to share the information. OBs waiting in the nest selects a food source according to such information. Specifically, an OB chooses a solution based on the probability values, which can be obtained by using the fitness values that EBs provided. In view of this purpose, the roulette wheel selection method can be adopted. This fitness-based selection technique is proposed by Goldberg [12]. Hence, many onlookers are attracted to rich sources, resulting in positive feedback behavior. The probability value $p _ { m }$ with which EB is selected by an OB can be calcu lated using Eq. $( 1 2 )$ , where $C S _ { m }$ means the solution loaded on $E B _ { m } ,$ and SN denotes the population size:

$$
P _ {m} = \frac {f (C S _ {m})}{\sum_ {m = 1} ^ {S N} f (C S _ {m})}.\tag{12}
$$

After an OB selects an EB and its corresponding solution, a neigh borhood solution is determined by randomly using one of the above neighborhood structures again. Its fitness value is computed using Eq. (4). Following the EB process, a greedy selection is used between the originally selected solution $( C S _ { m } )$ and the neighborhood solution. If the neighborhood solution dominates $C S _ { m } ,$ , then $C S _ { m }$ is replaced by the neighborhood solution.

## 4.2.3. SB process

In the general ABC algorithm, unemployed bees who randomly select their food sources are named scout bees. In addition to general SBs (g-SBs), a new group named e-SB is designed to further optimize the choice of entrances/exits of attractions. The details of both groups are pre sented in the following:

(1) g-SBs. As mentioned earlier, if the solution to an EB is unable to be improved through a predetermined number of trials (named abandon ment criteria, limit), that is t(EB) = limit, then the EB becomes g-SB, and its solution is abandoned. The converted g-SB begins to randomly seek a new solution, which can be assigned to the corresponding EB, whose solution has been abandoned. Hence, poor solutions are discarded, and negative and positive feedbacks are balanced.

(2) e-SBs. e-SBs are special bees that are designed to optimize the entrances and exits of attractions. Such entrances and exits are repre sented as the two lower pheromones in the variable-form nectar (as shown in Section 4.1). Each e-SB only corresponds to a single EB in the whole evolution process, and its optimization is based on the solution of the EB. Specifically, e-SBs optimize the route whose vertex selection and sequencing have been optimized by EBs and OBs. e-SBs seek good so lutions according to the following steps. First, the paths set between each pair of adjacent vertices $( \varLambda _ { 1 } , \ \varLambda _ { 2 } ) , \ ( \varLambda _ { 2 } , \ \varLambda _ { 3 } ) , \ . . . , \ ( \varLambda _ { M { - } l } , \ \varLambda _ { M } )$ are determined, and the path sets are denoted as $s _ { 1 } , s _ { 2 } , . . . , s _ { M - 1 }$ . Second, the shortest path $\left( \boldsymbol { p } _ { i } ^ { * } \right)$ ) of the ith path set $( S _ { i } )$ is found. Finally, the starting and ending points of $\dot { \boldsymbol { p } } _ { i } ^ { * }$ are marked as the exit and entrance vertices Λi and $\varLambda _ { i + 1 } ,$ , respectively. For clarity, the pair (v , v ) shown in Fig. 3 is taken to illustrate this process. Six paths are observed between pair $( \nu _ { 5 } , \nu _ { 6 } ) _ { : }$ , and the travel time of the path between $E X _ { 5 } ^ { 3 }$ and $E X _ { 6 } ^ { 1 }$ is the shortest among the six paths. Thus, $E X _ { 5 } ^ { 3 }$ and $E X _ { 6 } ^ { 1 }$ are selected as the exit of $\nu _ { 5 }$ and the entrance of $\nu _ { 6 } ,$ respectively $( { \mathrm { F i g . ~ } } 6 )$

## 4.2.4. DEA process

Typically, each iteration involves all four processes: EBs, OBs, SBs, and DEA. The optimization of vertex entrance/exit and time allocation is based on that of vertex selection and sequencing. In addition, in the early stage of evolution, the optimization intensity of vertex selection and sequencing is strong. Thus, the optimization of vertex entrance/exit and time allocation in the early stage of evolution cannot effectively improve the quality of final solutions but can reduce the efficiency of the algorithm. To reach an equilibrium of solution quality and algorithm efficiency, we improve the evolution structure by introducing the adaptive evolutionary parameter $( p _ { e } ) _ { : }$ , which can be calculated using Eq. (13). In this equation, G is the iteration times of the algorithm, and Iter refers to the current iterations. $p _ { e }$ increases as the number of iterations increases, indicating that the optimization intensity of vertex entrance/ exit and time allocation increases gradually:

$$
p _ {e} = \frac {1}{G - I t e r + 1}\tag{13}
$$

<table><tr><td> $v_1$ </td><td> $v_3$ </td><td> $v_7$ </td><td> $v_5$ </td><td> $v_6$ </td><td> $v_2$ </td><td> $v_4$ </td></tr><tr><td>0</td><td>69</td><td>18</td><td>6</td><td>43</td><td>26</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>3</td><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td><td>3</td><td>2</td><td>1</td><td>1</td></tr></table>

![](/api/attachments/AQR4GCCP/fulltext/images/91f7a889d56bfd4b56dad184f2e1b871cba0b16971563fa47650de5ff9546ea8.jpg)  
Fig. 6. Example of an e-SB

![](/api/attachments/AQR4GCCP/fulltext/images/c72eb3e7aa16e8f46aa519cc73ae3efb5f83b238f3a5b3b1c9f6774af052ad6e.jpg)  
Fig. 7. Map of Kulangsu Island.

## 5. Field experiment

## 5.1. Field

The field selected for the experiment is Kulangsu (or Gulangyu), a tiny island of merely 1.88 km<sup>2</sup> located southwest of Xiamen City in China (Fig. 7). The island is a UNESCO World Cultural Heritage Site, surrounded by various attractions such as heritage buildings, beaches, gardens, rugged terrain, and historical sites. The only access to the island is two dedicated ferries for tourists, operating between Kulangsu and Xiamen, with the third one open only to local residents (shown as red dots in Fig. 7). The island is car-free, walking is the only way for tourists to tour around the island. Approximately 90% of the tourists visiting the island chose the one-day tour option, according to official statistics [46]. A dilemma exists between the number of attractions in Kulangsu and the limited time tourists have for their tour, which makes it an ideal case for our study.

## 5.1.1. Basic information about the attractions

Kulangsu is dotted with plenty of attractions. This study selects 39 of the most popular ones for the study. Locations of the 39 attractions are indicated in Fig. 7. The number of entrances and exits for each attraction can significantly affect route planning. The information is listed in the fifth column of Table 3. Note that certain attractions are open areas (e.g., Gangzaihou Seaside Resort). Thus, tourists can enter and leave from anywhere. For these attractions, the number of entrances and exits can be considered infinite. In addition, the average time spent by earlier tourists (t ) at each attraction can influence the development of the initial solution in the preprocessing phase. The responses from a survey with tourists and Kulangsu tourism service staff members serve as data on t . We randomly conducted several interviews with tourists leaving Kulangsu. They wrote down two kinds of information: (1) the attractions they had visited, and (2) the time they had used at each attraction. We deleted the values that are too large or too small to calculate the average time spent at each attraction. The sixth column in Table 3 presents the results.

## 5.1.2. Basic information of the participants

We recruited 100 tourists to participate in our survey at Sanqiutian and Neicuoao Ferry Terminals on August 11, 19, and 27, 2019. We conducted a simple oral interview with the participants. We described to the participants the 39 attractions using pictures and collected the willingness respondents rated to visit each attraction based on a scale from ${ } ^ { 6 6 } 0 ^ { \prime \prime }$ (no interest to visit the attraction) $\tan ^ { 6 6 } 1 ^ { \prime \prime }$ (the highest interest to visit the attraction). Subsequently, the respondents recorded their time budget. Respondents’ demographic information was requested, too. Among all our participants, 37 were male, and 63 were female; 45 were recruited at Sanqiutian Ferry Terminal, whereas 55 were gathered at Neicuoao Ferry Terminal; 39 were recruited for the first survey, 34 during the second, and the remaining 27 were invited for the final survey. Table 4 lists the aforementioned tourist information.

Table 3  
Attractions in Kulangsu.

<table><tr><td>No</td><td>Name</td><td>Spatial structure</td><td>Time window</td><td>Number of entrances/ exits</td><td>tj (min)</td></tr><tr><td> $v_1$ </td><td>Shuzhuang Garden</td><td>AOI</td><td>[05:00–21:30]</td><td>2, 2</td><td>60</td></tr><tr><td> $v_2$ </td><td>Gangzaihou Seaside Resort</td><td>AOI</td><td>[00:00–24:00]</td><td>Infinite, Infinite</td><td>10</td></tr><tr><td> $v_3$ </td><td>International Calligraphy and Carving Gallery</td><td>POI</td><td>[08:15–18:15]</td><td>1, 1</td><td>15</td></tr><tr><td>....</td><td>....</td><td>....</td><td>....</td><td>....</td><td>....</td></tr><tr><td> $v_{36}$ </td><td>Gulang Rock</td><td>POI</td><td>[00:00–24:00]</td><td>1, 1</td><td>10</td></tr><tr><td> $v_{37}$ </td><td>Merihua Beach</td><td>AOI</td><td>[00:00–24:00]</td><td>Infinite, Infinite</td><td>10</td></tr><tr><td> $v_{38}$ </td><td>Shell Museum</td><td>AOI</td><td>[08:00–18:00]</td><td>1, 1</td><td>60</td></tr><tr><td> $v_{39}$ </td><td>Gusheng Tunnel</td><td>LOI</td><td>[00:00–24:00]</td><td>2, 2</td><td>5</td></tr><tr><td> $v_{40}$ </td><td>Sanqiutian Ferry Terminal</td><td>Ferry Terminal</td><td>[00:00–24:00]</td><td>1, 1</td><td>-</td></tr><tr><td> $v_{41}$ </td><td>Neicuoao Ferry Terminal</td><td>Ferry Terminal</td><td>[07:20–18:40]</td><td>1, 1</td><td>-</td></tr></table>

Table 4  
Sample tourist preferences and time budget.

<table><tr><td>Tourist</td><td>Gender</td><td>Preferred attractions</td><td>Time budget</td></tr><tr><td>1</td><td>M</td><td>[0.50, 0.36, 0.29, ..., 0.20, 0.23, 0.29]</td><td>5 h, [8:00–13:00]</td></tr><tr><td>2</td><td>F</td><td>[1.0, 0.40, 0.28, ..., 0.94, 1.0, 0.90]</td><td>5 h, [8:00–13:00]</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>100</td><td>M</td><td>[.63, 0.88, 0.64, ..., 1.0, 0.74, 0.81]</td><td>12 h, [8:00–20:00]</td></tr></table>

## 5.2. Algorithm parameters

The performance of our approach can be considerably affected by algorithm parameters, including SN, G, the numbers of EBs $( N _ { e b } )$ , OBs $( N _ { o b } ) , g { \ - } S B s \ : ( N _ { g - s b } )$ , and $e { - } S B s \left( N _ { e { - } s b } \right)$ in the colony, abandonment criteria (limit), and differential evolution rate (F<sub>s</sub>). Inappropriate SN and G values may reduce the performance of the approach: too small SN and G may increase the risk of reaching a local optimum, whereas too large values may cause computational inefficiency. In general, $N _ { e b }$ and $N _ { o b }$ are the same and equal to SN, that is, $N _ { e b } = N _ { o b } = S N _ { \cdot }$ . Moreover, $N _ { s b }$ is usually set to 1 [15, 20]. In this study, a new group of bees called e-SBs is designed to optimize the choice of entrances/exits of attractions. $N _ { e - s b }$ equals to $N _ { e b } ,$ as e-SB is mapped one-to-one with EB. The parameter limit is set to $S N \times D ,$ where D is the dimension of the solution and equals to the number of vertices (N). The parameters of our algorithm are pre sented in Table 5.

## 5.3. Model performance evaluation

Considering the personal characteristics. preferences. and con. straints of the 100 participants (Table 4), the essential information of Kulangsu (Table 3), and algorithm parameters (Table 5), we designed tour routes using our method along with four baseline methods, namely, iteration local search (ILS), standard genetic algorithm (sGA), particle swarm optimization (PSO), and ant colony optimization (ACO). To prevent random errors, each algorithm creates the route for each tourist 30 times and averages the total utility of results 30 times [18]. Fig. 8 shows the average utility obtained by each tourist through these five methods.

Several paired sample t-tests were run to examine whether any sta tistical differences exist among the utility achieved by the five methods of HA, ILS, sGA, PSO, and ACO. Table 6 lists the means and standard deviations of the utility generated from the five methods. Table 7 shows the results of the paired t-tests. For the first pair (HA–ILS), the gap mean was 2.442, and HA reached a significantly higher utility (M = 40.811, SD = 19.352) than ILS (M = 38.369, SD = 17.887) (t(100) = 10.222, p < 0.05). Analogously, the second (HA–sGA), third (HA–PSO), and fourth pairs (HA–ACO) showed an obvious advantage of our proposed method over sGA, PSO, and ACO in improved utility.

## 5.4. Model efficiency evaluation

We now compared our proposed approach with the above four al gorithms (ILS, GA, PSO, and ACO) to analyze the efficiency of HA. The two tourists from each group with a time budget of 4, 8, and 12 h were selected as the test samples, and we ran each algorithm 30 times. To depict the relationship between the result and iterations, the optimiza tion history of HA is provided in Fig. 9. As our approach pays attention to the optimization of discrete and continuous variables and provides more opportunities to escape from local optimality, the efficiency of the al gorithm may be limited. Therefore, we flexibly adjusted the number of iterations to 2000 (denoted as LHA) and kept other parameters of the algorithm unchanged, to achieve a better trade-off between efficiency and performance.

Table 5  
Algorithm parameters.

<table><tr><td></td><td>SN</td><td>G</td><td> $N_{eb}$ </td><td> $N_{ob}$ </td><td> $N_{g-sb}$ </td><td> $N_{e-sb}$ </td><td>Limt</td><td> $F_s$ </td></tr><tr><td>Value</td><td>15</td><td>10,000</td><td>15</td><td>15</td><td>1</td><td>15</td><td>615</td><td>0.1</td></tr></table>

![](/api/attachments/AQR4GCCP/fulltext/images/dd435ff3f609556e61beb26aa0981ab5bf34cb83986de1c61ed3c0ec57df6b8a.jpg)  
Fig. 8. Average utility by methods (HA, ILS, sGA, PSO, and ACO).

Table 6  
Basic statistics of paired samples.

<table><tr><td colspan="2"></td><td>Mean</td><td>N</td><td>Standard deviation</td><td>Standard error mean</td></tr><tr><td rowspan="2">Pair 1</td><td>HA</td><td>40.811</td><td>100</td><td>19.352</td><td>1.935</td></tr><tr><td>ILS</td><td>38.369</td><td>100</td><td>17.887</td><td>1.789</td></tr><tr><td rowspan="2">Pair 2</td><td>HA</td><td>40.811</td><td>100</td><td>19.352</td><td>1.935</td></tr><tr><td>sGA</td><td>35.006</td><td>100</td><td>17.301</td><td>1.730</td></tr><tr><td rowspan="2">Pair 3</td><td>HA</td><td>40.811</td><td>100</td><td>19.352</td><td>1.935</td></tr><tr><td>PSO</td><td>36.847</td><td>100</td><td>17.675</td><td>1.768</td></tr><tr><td rowspan="2">Pair 4</td><td>HA</td><td>40.811</td><td>100</td><td>19.352</td><td>1.935</td></tr><tr><td>ACO</td><td>35.416</td><td>100</td><td>16.449</td><td>1.645</td></tr></table>

Table 8 shows the results of five methods for various time budgets $T _ { m a x }$ and the corresponding number of tourists where the average utility U and the average computational time T are reported. The performance of HA and LHA is optimal for all the runs, especially in optimizing the route for a longer time budget, whereas ILS shows great advantages in computational time. The structure of our approach, which focuses on finding the best choice of entrance and exit and the duration at attrac tions, becomes very time consuming to calculate.

## 5.5. Case demonstration

The results indicate the advantage of our approach in accumulating more utility for the tourist over the other four methods, indicating that it can help improve the effectiveness of the tour recommender system by considering the heterogeneity of tourist attractions’ spatial structure and the time spent at each attraction. By contrast, most previous studies abstract attractions as pure vertices or pure arcs, ignoring the multiple entrances/exits of attractions, leading to unnecessary detours or addi tional time en route between attractions. In general, longer time at attraction and less time en route provide greater utility [45]. Our approach reflects the actual situation of attractions’ spatial structure and incorporates time optimization, thus helping tourists avoid unnecessary detours or extra time en route between attractions.

For validation, we performed a comparative test to make a distinc tion between our approach and ILS presented by Gavalas, et al. [10]. For example, the first tourist in Table 4 plans to visit Kulangsu for 5 h (from 8:00 to 13:00). We employed HA and ILS to create routes for this tourist, as shown in Fig. 10 (the left shows our proposed HA, whereas the right indicates ILS). As displayed in the figures, compared with ILS, HA designs routes that reduce the amount of time spent on the road, thereby increasing the number and time of visits to attractions for achieving additional utility, as presented in Table 9.

Table 7  
Results of paired sample t-tests.

<table><tr><td rowspan="3" colspan="2"></td><td colspan="5">Paired differences</td><td rowspan="3">t</td><td rowspan="3">df</td><td rowspan="3">Sig. (2-tailed)</td></tr><tr><td rowspan="2">Mean</td><td rowspan="2">Standard deviation</td><td rowspan="2">Standard error mean</td><td colspan="2">95% Confidence interval of the difference</td></tr><tr><td>Lower</td><td>Upper</td></tr><tr><td>Pair 1</td><td>HA-ILS</td><td>2.442</td><td>2.389</td><td>0.239</td><td>1.968</td><td>2.916</td><td>10.222</td><td>99</td><td>0.000***</td></tr><tr><td>Pair 2</td><td>HA-Sga</td><td>5.805</td><td>3.655</td><td>0.365</td><td>5.080</td><td>6.530</td><td>15.883</td><td>99</td><td>0.000***</td></tr><tr><td>Pair 2</td><td>HA-PSO</td><td>3.964</td><td>2.751</td><td>0.275</td><td>3.418</td><td>4.510</td><td>14.407</td><td>99</td><td>0.000***</td></tr><tr><td>Pair 3</td><td>HA-ACO</td><td>5.395</td><td>3.690</td><td>0.369</td><td>4.663</td><td>6.127</td><td>14.621</td><td>99</td><td>0.000***</td></tr></table>

\*p < 0.05.  
\*\*p < 0.01.  
p < 0.001.

![](/api/attachments/AQR4GCCP/fulltext/images/5187381443a8b8f8016de76faba2c46f33fbcfa130e82099b8b42a1a68c76690.jpg)  
Fig. 9. Optimization history of HA.

Table 8  
Comparison of efficiency between different methods.

<table><tr><td rowspan="2">Tmax</td><td rowspan="2">No.</td><td colspan="2">HA</td><td colspan="2">LHA</td><td colspan="2">ILS</td><td colspan="2">GA</td><td colspan="2">PSO</td><td colspan="2">ACO</td></tr><tr><td>U</td><td>T</td><td>U</td><td>T</td><td>U</td><td>T</td><td>U</td><td>T</td><td>U</td><td>T</td><td>U</td><td>T</td></tr><tr><td>4H</td><td>28</td><td>23.53</td><td>10.93</td><td>23.21</td><td>2.54</td><td>20.83</td><td>0.09</td><td>18.09</td><td>3.20</td><td>18.02</td><td>2.75</td><td>19.35</td><td>3.37</td></tr><tr><td>4H</td><td>77</td><td>21.87</td><td>11.42</td><td>21.56</td><td>2.54</td><td>21.44</td><td>0.06</td><td>17.69</td><td>3.16</td><td>20.87</td><td>2.67</td><td>20.34</td><td>3.37</td></tr><tr><td>8H</td><td>16</td><td>44.00</td><td>13.67</td><td>43.11</td><td>3.39</td><td>38.39</td><td>0.05</td><td>38.86</td><td>3.55</td><td>39.30</td><td>3.41</td><td>35.00</td><td>3.70</td></tr><tr><td>8H</td><td>58</td><td>47.71</td><td>15.60</td><td>46.64</td><td>3.17</td><td>42.73</td><td>0.12</td><td>40.29</td><td>3.53</td><td>41.63</td><td>3.34</td><td>43.14</td><td>3.38</td></tr><tr><td>12H</td><td>22</td><td>72.86</td><td>13.46</td><td>71.53</td><td>3.47</td><td>61.38</td><td>0.09</td><td>58.28</td><td>3.97</td><td>58.18</td><td>4.25</td><td>62.55</td><td>3.55</td></tr><tr><td>12H</td><td>35</td><td>82.77</td><td>13.79</td><td>82.17</td><td>3.60</td><td>72.13</td><td>0.10</td><td>65.53</td><td>4.03</td><td>65.52</td><td>4.29</td><td>72.04</td><td>4.39</td></tr></table>

![](/api/attachments/AQR4GCCP/fulltext/images/09560c968de30b332f53f0abebbdd25eb60b4865167ebe0c56f858f63734a980.jpg)  
Fig. 10. Tour routes designed by HA and ILS.

Table 9  
Information about tour routes designed by HA and ILS.

<table><tr><td>Method</td><td>Number of attractions visited</td><td>Time spent in the attractions</td><td>Time spent on the road</td><td>Utility</td></tr><tr><td>HA</td><td>21</td><td>243</td><td>57</td><td>25.49</td></tr><tr><td>ILS</td><td>13</td><td>225</td><td>75</td><td>24.26</td></tr></table>

Given the full consideration of the attractions’ spatial structure, the route designed by our approach can avoid “backtracks” as much as possible. These so-called “backtracks” refer to repeating the route taken to reduce the marginal utility of tourists or cause additional traffic time consumption. For example, both the routes designed by HA and ILS (Fig. 10) include the sub-route “The Bagua Building (Organ Museum) (v ) → Longshan Tunnel $( \nu _ { 3 2 } ) $ Epigraphy on Restoration of the Sanhe Taoist Temple $( \nu _ { 3 3 } ) . \ '$ Our approach considers that Longshan Tunnel $( \nu _ { 3 2 } )$ is a line-shape attraction and avoids “backtrack” by optimizing the choice of $\nu _ { 3 2 } \cdot s$ entrance and exit. By contrast, the route designed by ILS has a “backtrack,” which may reduce the marginal utility of the tourist. Fig. 11 illustrates the comparison of these two approaches (the left shows our proposed HA, whereas the right indicates ILS). The dotted line in the right figure represents that the tourist walked twice in Longshan Tunnel.

In addition. certain tourist attractions contain multiple entrances/ exits. Therefore, choosing appropriate stations to enter and leave at tractions is important in planning trips. Our approach considers the multiple entrances and exits of attractions to avoid unnecessary detours. For example, both the routes designed by HA and ILS (Fig. 10) contain the sub-route $\mathrm { ^ { \circ } Y u }$ Garden (v ) → Xiamen Music School $( \nu _ { 8 } ) . \mathrm { ^ { , , } Y u }$ Garden (v ) has three entrances $\left( E N _ { 9 } ^ { 1 } , E N _ { 9 } ^ { 2 } , \right.$ and $E N _ { 9 } ^ { 3 } )$ ) and three exits $( E X _ { 9 } ^ { 1 } , E X _ { 9 } ^ { 2 }$ and EX<sup>3</sup>) (Fig. 12). Our approach optimizes the choice of entrances/exits of attractions. The tourist enters $\nu _ { 9 }$ from $E N _ { 9 } ^ { 3 }$ and leaves the attraction from $E N _ { 9 } ^ { 1 } ;$ , which is the nearest exit from $\nu _ { 8 }$ (left of Fig. 12). In the route designed by ILS, the tourist enters $\nu _ { 9 }$ from EN<sup>2</sup> and leaves the attraction from the same station, adding an unnecessary detour (the yellow curves in the right of Fig. 12). Detours can undoubtedly increase the travel time between attractions. For example, the traffic time between v and $\nu _ { 8 }$ is 1 min in the route designed by HA, but 4 min in the route presented by ILS.

## 6. Discussion and conclusions

Providing information services such as fit-for-purpose recommen dations is essential for firms to successfully compete in today’s market environment [7, 14]. One of the neglected issues in the tour recom mender research is the heterogeneity of attractions’ spatial structure. Failing to consider it may lead to potentially infeasible or suboptimal recommendations for the users. This study proposes a novel model with solutions coded using a variant-form nectar with four pheromones, optimized with variables combining improved ABC and DEA. Our pro posed model adopts various measures to reach an equilibrium of solu tion quality and algorithm efficiency (e.g., improving the evolution structure, embedding neighborhood search structure, and adding a new group of bees in the ABC algorithm). We test our new model along with four benchmark models using a field experiment that verifies the supe rior performance of our model.

This study offers an improved model of tourist trip design that in tegrates spatial heterogeneity. The design provides significant improvement for tour recommender systems that optimize tourism experience; thus, our model can help tourism organizations provide more enjoyable trips. This is important because system design should be user-centered, and user well-being is of paramount importance. Service providers can integrate our proposed model to improve their existing recommender systems. In addition, our model can be further integrated with other intelligent systems, such as tourist personal conversational agents, which can be applied across multiple channels such as websites, smartphones, kiosks, and service robots to enhance tourist experience, satisfaction, and loyalty.

There are some limitations in this study, which are worth considering in future research. First, although we provided the evidence that the time spent in an attraction can be regarded as a commodity, the utility of stay with time requires further exploration, based on different tourist characteristics and destination characteristics. Second, for island desti nations that have multiple ferry terminals, the choices of terminals affect the route structure, thereby increasing the complexity of the design problem. Future studies should take into consideration the choices of ferry terminals in the trip design for island destinations. Finally, as tourists may change their minds owing to the changes in the weather condition, traffic condition, personal issues, tiredness, or mood, future researchers may consider the development of a dynamic tour recom mender system that can adjust in real time to the changes of the contexts and tourist preferences.

![](/api/attachments/AQR4GCCP/fulltext/images/e03d3cb8201ccd21a7f7f0e44da23d999ee862295ffe6a7bc87867c52a23a579.jpg)  
Fig. 11. Tour routes designed by HA and ILS (backtracks).

![](/api/attachments/AQR4GCCP/fulltext/images/83d18af8ff0d7665171ea295cc211161444a857b6a4ba57be73e7d56306102cb.jpg)  
Fig. 12. Tour routes designed by HA and ILS (detours).

## Funding

This work was supported by the National Natural Science Foundation of China (No. 71971179, No. 71601164) and Natural Science Founda tion of Fujian Province, China (No. 2020J01033).

## CRediT authorship contribution statement

Haipeng Ji: Writing- Original draft preparation, Methodology; Weimin Zheng: Project administration, Conceptualization; Xinyi Zhuang: Writing- Original draft preparation; Zhibin Lin: Writing Reviewing and Editing

## References

[1] P. Brewer, S. Venaik, GLOBE practices and values: a case of diminishing marginal utility? J. Int. Bus. Stud. 41 (2010) 1316–1324.

[2] I. Cenamor, T. de la Rosa, S. Núnez, ˜ D. Borrajo, Planning for tourism routes using social networks, Expert Syst. Appl. 69 (2017) 1–9.

[3] Y.-.Y. Chen, A.-.J. Cheng, W.H. Hsu, Travel recommendation by mining people attributes and travel group types from community-contributed photos, IEEE Trans. Multimedia 15 (2013) 1283–1295.

[4] Cheng, A.-.J., Chen, Y.-.Y., Huang, Y.-.T., Hsu, W.H., & Liao, H.-Y.M. (2011). Personalized travel recommendation by mining people attributes from communitycontributed photos. In Proceedings of the 19th ACM international conference on Multimedia (pp. 83-92): ACM.

[5] T. Cura, An artificial bee colony algorithm approach for the team orienteering problem with time windows. Comput. Ind. Eng. 74 (2014) 270–290.

[6] D.W. Eby, L.J. Molnar, Importance of scenic byways in route choice: a survey of driving tourists in the United States, Transp. Res. Part A: Policy Pract. 36 (2002) 95–106.

[7] H. Feng, J. Tian, H.J. Wang, M. Li, Personalized recommendations based on timeweighted overlapping community detection. Inf, Manag, 52 (2015) 789–800.

[8] D. Gavalas, V. Kasapakis, C. Konstantopoulos, G. Pantziou, N. Vathis, Scenic route planning for tourists, Pers. Ubiquitous Comput. 21 (2017) 137–155

[9] D. Gavalas, V. Kasapakis, C. Konstantopoulos, G. Pantziou, N. Vathis, C. Zaroliagis, The eCOMPASS multimodal tourist tour planner, Expert Syst. Appl. 42 (2015) 7303–7316.

[10] D. Gavalas, C. Konstantopoulos. K. Mastakas, G. Pantziou, N. Vathis. Efficient metaheuristics for the mixed team orienteering problem with time windows

[11] C.D. Geiger, H. Eskandari, A fast Pareto genetic algorithm approach for solving expensive multiobjective optimization problems, J. Heuristics 14 (2008) 203–241.

[12] D. Goldberg, Genetic Algorithms in Search, Optimization, and Machine Learning. Inc, Addison-Wesley Longman Publishing Co, Boston, MA, USA, 1989.

[13] B.L. Golden, L. Levy, R. Vohra, The orienteering problem, Nay. Res. Logist. 34 (1987) 307–318.

[14] M. Gorgoglione, U. Panniello, A. Tuzhilin, Recommendation strategies in

[15] K. Guo, Q. Zhang, A discrete artificial bee colony algorithm for the reverse logistics location and routing problem. Int. J. Inf. Technol. Decis. Mak. 16 (2017) 1339–1357.

[16] F.-.M. Hsu, Y.-.T. Lin, T.-.K. Ho, Design and implementation of an intelligent recommendation system for tourist attractions: the integration of EBM model Bayesian network and google maps, Expert. Syst. Appl. 39 (2012) 3257–3264.

[17] X. Huang, M. Li, J. Zhang, L. Zhang, H. Zhang, S. Yan, Tourists’ spatial-tempora behavior patterns in theme parks: a case study of Ocean Park Hong Kong, Jo. Dest. Mark. Manag. Sci. 15 (2020), 100411.

[18] Karaboga, D. (2005). An idea based on honey bee swarm for numerical optimization. In: technical report TR06, Erciyes University, Engineering Faculty, Computer Engineering Department.

[19] D. Karaboga, B. Gorkemli, C. Ozturk, N. Karaboga, A comprehensive survey: artificial bee colony (ABC) algorithm and applications, Artif. Intell. Rev. 42 (2014)

[20] M.S. Kıran, H. <sup>˙</sup>Is¸can, M. Gündüz, The analysis of discrete artificial bee colony algorithm with neighborhood operator on traveling salesman problem, Neural Comput. Appl. 23 (2013) 9–21.

[21] S. Kotiloglu. T. Lappas., K. Pelechrinis. P.P. Repoussis. Personalized multi-perioo tour recommendations. Tour, Manag, 62 (2017) 76–88

[22] C.-.S. Lee, Y.-.C. Chang, M.-.H. Wang, Ontological recommendation multi-agent for Tainan City travel, Expert. Syst. Appl. 36 (2009) 6740–6753.

[23] D. Lee, K. Hosanagar, How do recommender systems affect sales diversity? A crosscategory investigation via randomized field experiment, Inf. Syst. Res. 30 (2019) 239–259.

[24] Z. Liao, W. Zheng, Using a heuristic algorithm to design a personalized day tour route in a time-dependent stochastic environment, Tour. Manag. 68 (2018) 284-300.

[25] K.H. Lim, J. Chan, S. Karunasekera, C. Leckie, Tour recommendation and trip planning using location-based social media: a survey, Knowl. Inf. Syst. 60 (2019) 1247-1275.

[26] L. Liu, J. Xu, S.S. Liao, H. Chen, A real-time personalized route recommendation system for self-drive tourists based on vehicle to vehicle communication. Expert Syst, Appl, 41 (2014) 3409–3417.

[27] Lu, Y., Joss´e, G., Emrich, T., Demiryurek, U., Renz, M., Shahabi, C., & Schubert, M. (2017). Scenic routes now: efficiently solving the time-dependent arc orienteering problem. I n Proceedings of the 2017 ACM on Conference on Information and Knowledge Managemen t (pp. 487–496): ACM.

[28] Lu. Y., & Shahabi, C. (2015). An arc orienteering algorithm to find the most scenic path on a large-scale road network. In Proceedings of the 23rd SIGSPATIAI International Conference on Advances in Geographic Information Systems (pp. 46): ACM.

[29] A. Majid, L. Chen, H.T. Mirza, I. Hussain, G. Chen, A system for mining interesting tourist locations and travel sequences from public geo-tagged photos, Data Knowl. Eng. 95 (2015) 66–86.

[30] R. Martín-Moreno, M.A. Vega-Rodríguez, Multi-objective artificial bee colony algorithm applied to the bi-objective orienteering problem, Knowl. Based Syst. 154 (2018) 93-101.

[31] Mrazovic, P., Larriba-Pey, J.L., & Matskin, M. (2017). Improving mobility in smart cities with intelligent tourist trip planning. In 2017 IEEE 41st Annual Compute Software and Applications Conference (COMPSAC) (Vol. 1, pp. 897-907): IEEE.

[32] S. Omkar, J. Senthilnath, R. Khandelwal, G.N. Naik, S. Gopalakrishnan, Artificia bee colony (ABC) for multi-objective design optimization of composite structures, Appl, Soft Comput, 11. (2011) 489–499.

[33] Q.-.K. Pan, M.F. Tasgetiren, P.N. Suganthan, T.J. Chua, A discrete artificial bee colony algorithm for the lot-streaming flow shop scheduling problem, Inf. Sci. (Ny) 181 (2011) 2455–2468.

[34] B. Rodriguez, J. Molina, F. Perez, R. Caballero, Interactive design of personalised tourism routes, Tour, Manag, 33 (2012) 926–940.

[35] D. Rugg, The choice of journey destination: a theoretical and empirical analysis, Rev. Econ, Stat. (1973) 64–72.

[36] Y. Si, F. Zhang, W. Liu, An adaptive point-of-interest recommendation method for location-based social networks based on user activity and spatial features. Knowl Based Syst, 163 (2019) 267–282.

[37] W. Souffriau, P. Vansteenwegen, G.V. Berghe, D.V. Oudheusden, The planning of cycle trips in the province of East Flanders, Omega (Westport) 39 (2011) 209–213.

[38] C.Y. Sun, A.J.T Lee, Tour recommendations by mining photo sharing social media, Decis. Support Syst. 101 (2017) 28–39.

[39] W.Y. Szeto, Y. Wu, S.C. Ho, An artificial bee colony algorithm for the capacitated vehicle routing problem, Eur. J. Oper. Res. 215 (2011) 126–135.

[40] Taylor, K., Lim, K.H., & Chan, J. (2018). Travel itinerary recommendations with must-see points-of-interest. In Companion Proceedings of the The Web Conference 2018 (pp. 1198-1205): International World Wide Web Conferences Steering Committee.

[41] C.-.Y. Tsai, S.-.H. Chung, A personalized route recommendation service for theme parks using RFID information and tourist behavior, Decis. Support Syst. 52 (2012) 514–527.

[42] P. Vansteenwegen, W. Souffriau, D. Van Oudheusden, The orienteering problem: a survey, Eur. J. Oper. Res. 209 (2011) 1–10.

[43] C. Verbeeck, P. Vansteenwegen, E.H. Aghezzaf, An extension of the arc orienteering problem and its application to cycle trip planning, Transp. Res. Part E 68 (2014) 64–78.

[44] C.Y. Zhang, H.W. Liang, K. Wang, Trip recommendation meets real-world constraints: POI availability, diversity, and traveling time uncertainty, ACM Trans. Inf, Syst, 35 (2016) 1–28

[45] W. Zheng, H. Ji, C. Lin, W. Wang, B. Yu, Using a heuristic approach to design personalized urban tourism itineraries with hotel selection, Tour. Manag. 76 (2020), 103956.

[46] W. Zheng, Z. Liao, Using a heuristic approach to design personalized tour routes for heterogeneous tourist groups, Tour. Manag. 72 (2019) 313–325.

[47] W. Zheng, Z. Liao, Z. Lin, Navigating through the complex transport system: a heuristic approach for city tourism recommendation, Tour. Manag. 81 (2020), 104162.

[48] W. Zheng, Z. Liao, J. Qin, Using a four-step heuristic algorithm to design personalized day tour route within a tourist attraction, Tour. Manag. 62 (2017) 335–349.

Haipeng Ji is a master student of tourism management, at School of Management, Xiamen University, China.

Weimin Zheng is an Associate Professor of tourism management at Xiamen University. His current research interests focus on tourism management related topics, such as tourist mobility, tourist behavior analysis and tourist trip design problem, using the theories and methods of operational research. His-work has appeared in European Journal of Opera tional Research, Computers & Industrial Engineering, Tourism Management, Annals of Tourism Research, and Information Sciences, etc.

Xinyi Zhuang is a master student of tourism management, School of Management, Xiamen University, China.

Zhibin Lin is Associate Professor at Durham University Business School, UK. His-interests focus on technology and innovation marketing; transport, travel and tourism manage ment. He is a regular contributor to several international leading journals, such as Infor mation & Management, Computers in Human Behaviour, Annals of Tourism Research, Tourism Management, Journal of Travel Research. Journal of Business Research, and others.
