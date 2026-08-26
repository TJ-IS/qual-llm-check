---
otero_id: 9748
otero_key: "CU7W7GM9"
title: "Visual interactive support for selecting scenarios from time-series ensembles"
authors: "Guilherme G. Schardong; Ariane M.B. Rodrigues; Simone D.J. Barbosa; Hélio Lopes"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.08.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Visual interactive support for selecting scenarios from time-series ensembles

Guilherme G. Schardong<sup>\*</sup>, Ariane M.B. Rodrigues, Simone D.J. Barbosa, Hélio Lopes

![](/api/attachments/CU7W7GM9/fulltext/images/023517e402f779d432d6850f6bbb493fa86e415663232e1e8cd6029fb8b6672c.jpg)

Departamento de Informática, PUC-Rio, Rua Marquês de São Vicente 225, Gávea, Rio de Janeiro, RJ 22451-900, Brazil

## A R T I C L E I N F O

Keywords: Scenario reduction User interaction Time series Multidimensional projection Ensemble data

## A B S T R A C T

Stochastic programming approaches to solve the scenario reduction problem have become invaluable in the analysis and behavior prediction of dynamic systems. However, such techniques often fail to take advantage of the user's own expertise about the problem domain. This work provides visual interactive support to assist users in solving the scenario reduction problem with time-series data. We employ a series of time-based visualization techniques linked together to perform the task. By adapting a multidimensional projection algorithm to handle temporal data, we can graphically present the evolution of the ensemble. We also propose to use cumulative bump charts to visually compare the ranks of distances between the ensemble time series and a baseline series. To evaluate our approach, we developed a prototype application and conducted observation studies with volunteer users of varying backgrounds and levels of expertise. Our results indicate that a graphical approach to scenario reduction may result in a good subset of scenarios and provides a valuable tool for data exploration in this context. The users liked the interaction mechanisms provided and judged the task to be easy to perform with the tools provided.

## 1. Introduction

Recent developments in simulation techniques have helped researchers to better understand and predict several naturally occurring phenomena, ranging from weather forecast [1] to circuit calibration [2] and <sup>fl</sup>uid dynamics [3]. These simulations produce a huge amount of data, due to the availability of computing power and simulation model re<sup>fi</sup>nements. To extract meaningful information from all those data, researchers have been developing an array of approaches in diverse areas: data mining [4], machine learning [5], visualization [6], and optimization [7]. Such approaches typically use statistical measures to summarize the results or to reduce the dimensionality of data and select the most probable outcomes of the simulation.

In simulation analysis, scenario reduction is particularly useful, since its goal is to reduce the number of simulation outcomes (i.e., scenarios) to a more manageable size, with minimal loss of variability. Existing approaches are usually modeled as stochastic programming problems [8,9], in which a probability is associated to each possible scenario, and the goal is to select a subset of scenarios whose prob ability is closest to that of the original set (henceforth called ensemble). However, none of those approaches actively engages the users and their knowledge about the problem domain. Visualization-based approaches, conversely, allow for interactive exploration of the data through visual tools and interaction mechanisms. Visual analytics supports decision making by integrating the best of computational processing power and human cognitive prowess [10-13]. For time-based ensembles, Cheng et al. [14] provide a comprehensive survey on time-series and timebased visualization techniques and interaction mechanisms, from which we draw in our proposal.

The main goal of our work is to provide visual interactive support for solving the scenario reduction problem with time-series data. We employ a series of time-based visualization techniques linked together, allowing the user to draw from the strengths of each technique. To the best of our knowledge, no one has proposed a similar way of approaching this problem.

We also propose adaptations to two known visualization algorithms: (i) the Local A<sup>fi</sup>ne Multidimensional Projection (LAMP) algorithm [15], in order to produce a time-based representation of the data; and (ii) Bump charts, also known as Slope graphs [16], in order to view a transformed version of our time-series ensemble. Multidimensional projections are evolving, especially in the works of Alencar et al. [17] and Wong et al. [18]. By using a di<sup>f</sup>erent base technique, with a strong mathematical foundation [15], we aim to provide a more robust representation of the similarity between the series over time. We have also made some adaptations to Bump charts [16]. As our data is not ordinal, we transform them by ranking the distance between each series and a baseline. Moreover, we do not treat each time step as isolated from the others, but as an accumulated rank from all previous time steps.

As proof of concept, we built a prototype software using the brushing and linking framework, proposed by Becker et al. [19], Buja et al. [20], as basis for the user interaction with the di<sup>f</sup>erent visuali zations. We chose four visualization mechanisms: (i) a Fanchart, proposed by Britton et al. [21]; (ii) the Distance scatterplot; (iii) a cumulative Bump chart; and (iv) a scatterplot with the results of our proposed multidimensional projection (MP) approach. To evaluate our approach, we conducted an empirical study involving experts and non experts in the scenario reduction area.

In summary, our contributions are:

A visual interactive approach to assist the user in selecting a subset of meaningful scenarios from a time-series ensemble dataset, thus solving an instance of the scenario reduction problem;

• An adaption of a multidimensional projection algorithm to generate a visual representation of time-varying data, taking into account the time component of the data;

A transformation of a time-series ensemble dataset into a cumula tive, ranked version, in order to support a visual assessment of its evolution.

The remainder of this paper is organized as follows: Section 2 presents related works on Scenario Reduction and Multidimensional Projection. In Section 3 we describe our approach and explain the visualization techniques employed. Section 4 presents the user study plan. Section 5 presents the results of our study and discusses its implications. Finally, Section 6 presents some concluding remarks and directions for future work.

## 2. Related work

This section describes two groups of related works, on: (i) scenario reduction (i.e., the problem we address); and (ii) multidimensional projections, which are the type of algorithm we have adapted to help us with scenario reduction. Table 1 presents some of the main works and their contributions compared to ours. Details about these works are presented below.

## 2.1. Scenario reduction

As the number of objects in an ensemble grows, it becomes in creasingly di<sup>fi</sup>cult to analyze or visualize it adequately, even when using dimensionality reduction techniques. In many cases, it becomes

## Table 1

Overview of the literature in scenario reduction and multidimensional projections.

<table><tr><td>Work</td><td>Scenario reduction</td><td>Multidimensional projections</td><td>Brushing &amp; linking</td></tr><tr><td>Armstrong et al. [22]</td><td>X</td><td></td><td></td></tr><tr><td>Gröwe-Kuska et al. [23]</td><td>X</td><td></td><td></td></tr><tr><td>Meira et al. [24]</td><td>X</td><td></td><td></td></tr><tr><td>Lee et al. [2]</td><td>X</td><td></td><td></td></tr><tr><td>Heitsch and Römisch [25]</td><td>X</td><td></td><td></td></tr><tr><td>Domenica et al. [26]</td><td>X</td><td></td><td></td></tr><tr><td>Kawas et al. [27]</td><td>X</td><td></td><td></td></tr><tr><td>Park et al. [28]</td><td></td><td></td><td>X</td></tr><tr><td>Demir et al. [29]</td><td></td><td></td><td>X</td></tr><tr><td>Scheidt and Caers [30]</td><td>X</td><td>X</td><td></td></tr><tr><td>Sahaf et al. [31]</td><td>X</td><td></td><td>X</td></tr><tr><td>Waser et al. [32]</td><td>X</td><td></td><td>X</td></tr><tr><td>Our approach</td><td>X</td><td>X</td><td>X</td></tr></table>

necessary to select a representative subset of the ensemble for further processing, in a process known as scenario reduction, which has increasingly attracted researchers' interest, especially in areas such as power production [9,23] and geostatistics [2,8,22,30,33-35]. A number of researchers have proposed to use stochastic programming as an approach to tackle this problem. Dupačová et al. [9] stated that the Fortet-Mourier family of probability metrics may be used as canonical metrics to <sup>fi</sup>nd a subset of scenarios with probability distributions closest to the original set. They reduced the number of possible scenarios by 50% while keeping 90% relative accuracy in the remaining scenarios. More recently, Armstrong et al. [8] proposed a metric for the distance between conditional simulated realizations of ore deposits, along with a random search procedure to <sup>fi</sup>nd an approximation of the ideal subset of scenarios. They followed the approach proposed by Heitsch and Römisch [34] to calculate the distance between a subset of scenarios and the full ensemble. In their experiments, the best subset found was 1% o<sup>f</sup> the expected value for their objective function, which indicates that the number of possible scenarios can be strongly reduced without signi<sup>fi</sup>cant loss in variability.

In the petroleum <sup>fi</sup>eld, Scheidt and Caers [30] have used dimensionality reduction and kernel methods to quantify the uncertainty in an ensemble of geological facies realizations. Their approach involved mapping the realizations onto a lower dimensional space using a multidimensional scaling (MDS) algorithm [36] and <sup>fl</sup>ow-related distance metrics, such as the Hausdor<sup>f</sup> distance [37] or time-of-<sup>fl</sup>ightbased metrics [38]. They have also used kernel methods to transform the projected points from a non-linear space onto a linear one, thus facilitating the application of grouping approaches, such as clustering algorithms and Principal Component Analysis. After de<sup>fi</sup>ning the realization groups, a few elements of each group are chosen for the actual <sup>fl</sup>ow simulation. The <sup>fl</sup>ow simulation statistics they obtained with a reduced number of realizations were very similar to those with the full ensemble.

Di<sup>f</sup>erent from most of the scenario reduction approaches presented so far, our main goal is to allow users to input their own knowledge of the problem domain into the process through graphical tools, therefore leading to a more <sup>fl</sup>exible process overall. To the best of our knowledge, there is little work on visual analytics and scenario reduction. Sahaf et al. [31] proposed a scenario reduction approach based on randomly sampling scenarios after clustering them using a mutual information similarity metric. They implemented this approach in a visual analytics framework, where it is possible to visualize the spatial contribution of each model to the similarity of scenarios and run a clustering algorithm in an area speci<sup>fi</sup>ed by the user. Kawas et al. [27] proposed an uncertainty-aware framework for decision optimization, in which they employed classic stochastic programming to perform the scenario reduction and used visual analytics only to evaluate the resulting models.

On a decision support systems context we found no works that involve both scenario reduction and visual analytics. Waser et al. [32] come close, by proposing a scenario generation and interactive visualization approach applied to <sup>fl</sup>ooding management. Their approach can simulate <sup>fl</sup>ooding scenarios in real time, but their visualization tool is not scalable and the plans generated are suboptimal. Domenica et al. [26] incorporate stochastic programming and scenario generation techniques into established decision support and information systems. They successfully argue that decision and simulation models can be combined in order to create business analytics, therefore creating uncertainty-aware decision and information systems. Park et al. [28] proposed a visual analytics approach for managing supply chain networks. They modeled these networks as directed graphs and implemented a series of interactive visualizations for them, including: force-directed layout, treemap layout, substrate-based visualization, chord diagrams and matrix layout. However, their views are not connected to each other, therefore lacking an important pattern-discovery mechanism.

## 2.2. Multidimensional projection

Multidimensional Projection (MP) techniques help us explore complex datasets. Using adequate distance metrics and dimensionality, patterns in the data may stand out, allowing users to quickly identify them. Their usefulness motivated the development of new MP techni ques and the adaptation of existing techniques to speci<sup>fi</sup>c kinds of data and application domains.

Wong et al. [18] used MP techniques to explore time-varying volume data. They adapted two algorithms: Fastmap [39] and Part-Linear Projection [40], in order to preserve temporal coherence between data volumes at di<sup>f</sup>erent time steps. The new algorithms, named Time-Co herent Fastmap (TC-Fastmap) and Time-Coherent Part-Linear Projection (TC-PLP), achieved an equivalent or lower con<sup>fi</sup>guration stress when compared to other time-varying projection techniques. They also proposed a scatter projection for attribute-space data exploration and for correlating selections to the object-space model.

Alencar et al. [17] adapted the Least Squares Projection (LSP) algorithm proposed by Paulovich et al. [41] to show the temporal evolution of groups of data. They applied their Time-based LSP algorithm to visualize the evolution of articles written by a researcher between the years 1995 and 2010. They plotted the results as a graph, with edges representing references between two articles, vertex color showing the publication age, and vertex size indicating the count of citations to each paper by 2010. They also employed a DBSCAN clustering algorithm [42] to identify groups of similar papers and extracted the topics of each group using the approach presented by Eler et al. [43]. In scienti<sup>fi</sup>c paper collections, this is especially useful to assess the evolution of research topics of a knowledge area, and may help to identify and predict research trends.

The <sup>fi</sup>rst part of our work draws on Alencar et al. [17]: we propose an adaptation of the Local A<sup>fi</sup>ne Multidimensional Projection (LAMP) algorithm [15] to generate a sequence of mappings of our time series ensemble. Each time step results in a new projection of the data until then. By merging the results of those projections in a single view, we provide a graphical approach to assess the evolution and behavior of the ensemble.

## 3. Proposed approach

Aiming to provide a framework for users to visually inspect and select representative subsets in a univariate time series ensemble, we have developed a series of graphical views, connected using brushing and linking [29,44].

When solving scenario reduction tasks, the general goal is to select the smallest number of scenarios while keeping the loss of variability minimal. Decisions made using the reduced set should be similar to those made using the full set of scenarios. However, both the number of scenarios in the reduced set and the way to select them is heavily problem and data dependent. Each pair of problem and type of data may require a di<sup>f</sup>erent scenario reduction approach in order to yield satisfactory results.

Di<sup>f</sup>erent from the usual approaches with stochastic programming, we allow the user to decide what constitutes a representative subset fo their use case. In the petroleum <sup>fi</sup>eld, for example, several approaches [24,45,46] propose the choice of percentile models as representatives of the ensemble, usually the scenarios $\mathrm { P _ { 1 0 } , P _ { 5 0 } }$ and $\mathrm { P } _ { 9 0 } .$ This is motivated by the subsequent risk analysis that is performed on the selected scenarios. These reference models also ensure that a number of scenario near the distribution's extrema and median values are selected, thus ensuring some variability in the reduced set of scenarios. We opted to follow this approach as a starting step for our proposal; however, it is straightforward to adapt it to other targets.

We initially implemented four time series visualization techniques: the Fanchart [21], the Distance chart, the Bump chart [16], and the

Time-Lapse Local A<sup>fi</sup>ne Multidimensional Projection chart. These charts are all connected using the brushing and linking framework [19,20] to provide interaction mechanisms for the user. The following subsections detail the charts and interaction mechanisms.

## 3.1. Fanchart

The <sup>fi</sup>rst graphical view used in our approach is the Fanchart [21], used to visualize a distribution of time-based data. The Fanchart is commonly used to graph observed past data together with forecasts of future data. The observed data is represented as a line chart, since their values are known, while the forecasts are represented as an increasingly wide cloud of possibilities. Since the values around the mean are, usually, more likely to happen, they are represented in stronger colors. As the values stray further to the extremities, their color gets fainter, a re<sup>fl</sup>ection of the smaller likelihood of their occurrence.

Fancharts are useful in uncertainty analysis, since a wide fan of forecasts represents more uncertainty about the future, while a narrower fan represents less uncertainty. Compared to line charts, a Fanchart is less cluttered visually, and thus a good choice for assessing a large ensemble of time-series. In our approach, Fancharts are the closest view a user has of the raw data. When analyzing scenarios, analysts can use the Fanchart to check whether the behavior shown in the other views is consistent. Fig. 1a shows an example of a Fanchart of a synthetic time-series ensemble.

## 3.2. Distance chart

The second graphical view is the Distance chart. As its name implies, the Distance chart graphs the distances, or similarities between a set of objects and a baseline. Selecting the scenarios closest to a reference may provide a reasonable starting set of solutions to scenario reduction. Fig. 1b shows an example of a Distance chart of a synthetic time-series ensemble.

In a Distance chart, the X axis is the series' identi<sup>fi</sup>er, and the Y axis is the distance between each series and a baseline. Each series is treated as a multidimensional point when calculating the distance. We use the Euclidean distance, instead of a correlation measure or a dynamic time warping technique, to maintain coherence with the Bump chart and Time-lapsed LAMP chart. Also, it is computationally light to calculate, even though it becomes increasingly unstable as the data dimension ality increases.

## 3.3. Bump chart

The third graphical view, the Bump chart, was proposed by Tufte [16] in order to visualize rankings of objects in time, e.g, cyclists' positions at the end of each day of a Tour de France. Our proposal di<sup>f</sup>ers from the original approach in two main aspects: <sup>fi</sup>rst, we graph a distance-based ranking built from an ensemble of time-series and a reference time-series; second, the ranking on time step T is calculated by taking into consideration information from time steps [0,T − 1], thus, making it a cumulative measure.

A ranking measure is built by comparing a set of elements as they achieve a goal, e.g. athletes <sup>fi</sup>nishing a race. However, when dealing with time-series data, the goal may not be clearly de<sup>fi</sup>ned. Here we de<sup>fi</sup>ned the goal as proximity of the ensemble's series to a baseline time-series, using the Euclidean distance. A rank by time measure may be used to assess the adherence of a scenario to the baseline. Depending on the analysis being made, a more adherent scenario may be desirable. However, it may not necessarily be the closest one, in a raw distance sense.

Fig. 1c shows an example of Bump chart built from a synthetic timeseries ensemble. It presents a scale-independent view of the ensemble compared to the baseline. It can also be modi<sup>fi</sup>ed to simply present an ordering of the time-series values at each time step, dismissing the need for a baseline series and presenting the data more closely to the original values.

![](/api/attachments/CU7W7GM9/fulltext/images/3a9ba3d9a99a70efdc9e66e9069f70dd5175f83a02d01a0b8f54d675e38553fa.jpg)  
(a) A sample Fanchart.

![](/api/attachments/CU7W7GM9/fulltext/images/22878f1f397566e9d2a611f930d53ad3d0dda920f2df00740d42610cac7705f6.jpg)  
(b) A sample Distance chart.

![](/api/attachments/CU7W7GM9/fulltext/images/512d6446867e84139113398d8223b7312b9daf664612c51ebf27e7d3510d7ac7.jpg)  
(c) A sample Bump chart.  
Fig. 1. The charts of a randomly generated, cumulative time-series dataset. The green triangle refers to the $\mathrm { \bf p } _ { 9 0 } ,$ blue to $\mathrm { \bf P } _ { 5 0 } ,$ and red to $\mathrm { \bf P } _ { 1 0 } .$ . For the Distance and Bump charts (1b and 1c), the baseline is the calculated $\mathrm { P } _ { 5 0 }$ scenario.

## 3.4. Time-lapsed LAMP

The <sup>fi</sup>nal view is a modi<sup>fi</sup>ed version of the LAMP algorithm proposed by Joia et al. [15]. LAMP is a <sup>fl</sup>exible technique with focus on user interaction during the input stage. It uses orthogonal mapping theory as a basis to build local mappings of high-dimensional data. The main focus of LAMP is to let the users input their knowledge about the similarity of data instances into the mapping process. To project the data, LAMP requires a subset of the input data to act as control points. These points are located in the projection space, either through user input or by using other techniques. They are used to build a series of orthogonal a<sup>fi</sup>ne mappings, one for each data instance. Each mapping is built by solving an Orthogonal Procrustes Problem [47]. This allows building accurate mappings, and has competitive computational times when compared to other MP techniques [15].

We propose an adaptation of LAMP in which we add a time attribute to the process. Given an ensemble S of time series with T time steps each, we build T − 1 mappings. Each mapping t ∈ [2,T] is composed of the projected data from times [1,t], and is independent from the others. However, when merged in a single view, the result is a series of |S paths, as shown in Fig. 2b. Each path traces the evolution of a single time series, allowing its comparison to the |S|− 1 others.

This approach can be used to <sup>fi</sup>nd features which are not easily veri<sup>fi</sup>able using ordinary MP approaches. Fig. 2 shows an example of four synthetic curves projected using MDS (2a) and our Time-lapsed LAMP (2b).

The main advantages of LAMP over other MP approaches are its robust mathematical basis, computational speed and, mainly, axis stability. Unlike multidimensional scaling techniques, LAMP does not su<sup>f</sup>er from axis rotations and scaling, so it does not require post-processing the maps to conform to the same orientation.

The original LAMP algorithm requires three parameters: $X \in \mathbb { R } ^ { T }$ as the data to be mapped, $X _ { s } \in \mathbb { R } ^ { T }$ as the control points in the original space $\mathbb { R } ^ { T } ,$ , and $Y _ { \textrm { i } }$ as the mapping of $X _ { s }$ onto the projected space, in our case $\mathbb { R } ^ { 2 } .$ . The <sup>fi</sup>rst step in our approach is to build the control points set. We opted to use the whole set S as control points; therefore, they must be positioned in the projection space before the main mapping step. For this task, we employed an MDS algorithm [36], using the |S| series and T time steps as input. We also opted to use a Euclidean distance between each time series as metric for this step. The resulting projected points are then used as the $Y _ { \mathrm { ~ , ~ } }$ parameter for LAMP, while the original series S is used as the $X _ { s }$ parameter. The X parameter, however, needs special processing. Since X constitutes the data to be mapped, and we build one mapping for each time step t, X must be adapted to contain only the data to be projected up to time step t. This adaptation is done by replacing the data of S outside the time step range [1,t] with zeros; this e<sup>f</sup>ectively removes that range from consideration for the mapping. An outline of the procedure is as follows:

1. Build the control points mappings $Y _ { s ; }$

Use an MDS algorithm with the T time steps of all S time series; 2. For each time step t ∈ [2,T], map the time series using their whole data as the $X _ { s }$ parameter and their mappings as the $Y$ parameter; • To build X, use only the values in the time step range [1,t]; • Replace the remaining values [t + 1,T] with zeros.

3. Merge the resulting mappings and plot them.

Contrary to most MP algorithms, this approach results in a sequence of mappings for each time series. Each mapping presents the behavior of that single series, allowing to compare it to all others in the set. This feature may be useful to detect patterns in the behaviors of sets of scenarios, so that the user may select them for further analysis.

## 3.5. Interaction mechanisms and prototype details

To evaluate the e<sup>f</sup>ectiveness of our approach, we developed a prototype application<sup>1</sup> implementing the views presented in this section as well as the brushing and linking technique to add interactivity to our prototype. We implemented the prototype using the Python programming language (version 3)<sup>2</sup>. We used Matplotlib 2.0 [48] as a graphical plot library, Qt $5 . 7 ^ { 3 }$ as the user interface API, NumPy [49], Scipy [50] and Scikit Learn [51] for the high performance, numerically heavy computations.

Fig. 3 shows the main window of our software prototype. We implemented brushing and linking in two ways: click-to-select and mousehover to highlight. In click-to-select, if the user clicks on a scenario in a graphical view, that scenario is highlighted in all other views, by reducing the opacity of all non-selected scenarios. In the mouse-hover to highlight feature, the representation of the scenario under the cursor is thickened on all views, making it easier to distinguish it from the others.

![](/api/attachments/CU7W7GM9/fulltext/images/1ffefde9b2081474203083dea3ab4378d36894e77270398a470846330cdb58d1.jpg)  
(a) MDS plot sample.

![](/api/attachments/CU7W7GM9/fulltext/images/b595e8dc0b76100d9d46dd57c0b587a689d375c356c0c1cd664035656dbf3276.jpg)  
(b) Time-lapsed LAMP plot sample.

Fig. 2. Comparison between the MDS and Time-lapsed LAMP projections of a randomly generated dataset of 4 time-series  
![](/api/attachments/CU7W7GM9/fulltext/images/371baa214f04c1a0a396d5a546df5e8ed8e3a27160ace897124424bf82943aff.jpg)

![](/api/attachments/CU7W7GM9/fulltext/images/7b010678ced2bd317310c3a9bcea4cd53ac235873e822f83e61bcf2d2c4781ad.jpg)

![](/api/attachments/CU7W7GM9/fulltext/images/67bb752948a2d50f347aedd03614837b2891c5bd069ea3068930bc8d76c507cf.jpg)

![](/api/attachments/CU7W7GM9/fulltext/images/7cab9557aea1587f6c01fece682bfe017637aeaa0d92bd2568be0b90f71201f9.jpg)  
Fig. 3. Main window of our prototype application. The main area contains the four graphical views: Fanchart (upper-left), Time-lapsed LAMP chart (upper-right), Bump chart (lower-left), and Distance chart (lower-right). An options panel at the right-hand side presents more generic options nearer the top and view-speci<sup>fi</sup>c options below.

## 4. Evaluation

## 4.1. Test ensemble

The ensemble we used in our tests comes from a synthetic model called UNISIM-I, created for testing algorithms and methodologies related to reservoir management. This model was built using real publicly available data from the Namorado Field located in the Campos Basin, Brazil. It comprises high-quality geological and production data to ensure that any derived models honor the original data [52]. The base model contains a set of four exploratory perforations used to estimate the initial values of the reservoir's production and petrophysical properties. Based on this initial model, a production strategy was de<sup>fi</sup>ned by adding a number of wells and preparing an ensemble of 200 realization for reservoir simulation using the IMEX simulator. The resulting si mulations have a high degree of uncertainty, which was reduced by performing a history matching process using an ensemble-based method (ensemble smoother with multiple data assimilation [53]). The history matching considered oil and water production rate (QO and QW, respectively) and gas-oil ratio at producing wells, and bottom-hole pressure at production and water injection wells, for a period of 10 years. The uncertainty parameters correspond to porosity, net-togross ratio, horizontal and vertical permeability at every reservoir gridblock, end-points of water relative permeability curve, rock compressibility, and water-oil contact. This resulted in another ensemble with lower uncertainty, thus more appropriate for production forecasting.

![](/api/attachments/CU7W7GM9/fulltext/images/7f3c7811b9735f29c241693564a79be2143cf7d57758e5daf8f6dbc70360ace3.jpg)  
Fig. 4. UNISIM-I-H geometry with the producer wells in red and injector wells in blue. The grid property shown is the <sup>fi</sup>eld porosity. Images produced using Geresim. Available at: http://webserver2.tecgraf.puc-rio.br/\~celes/projects.html.

The resulting simulations contain a set of 25 wells, the 4 exploratory ones, plus 21 added by the engineers who de<sup>fi</sup>ned the production strategy. Each well can be classi<sup>fi</sup>ed as either injector or producer. The models used in our tests are composed of 14 producer and 11 injector wells. The focus of our analysis lied on the cumulative oil and water production wells (NP and WP, respectively). Each simulated model contains 30 years of data: 10 years of observed data and 20 years of production forecasts; the data is sampled monthly for the historic data, and every 6 months for the forecasts. Fig. 4 shows the reservoir geometry and the location of the selected wells.

For the study, we imported oil and water cumulative production data, as well as their production rates of the producer wells, saving data from each well and property in a comma-separated-values (CSV) <sup>fi</sup>le. For each scenario, we summed the productions of all wells, in order to obtain a single time series for each property of each scenario. The <sup>fi</sup>rst 10 years of historical data were removed, since the goal was to perform the analysis using only forecast production data.

## 4.2. Evaluation method

To evaluate our proposal, we performed an observational study according to the following procedure: Each participant was given an overview of the prototype and its features, and a series of tasks related to scenario reduction. The evaluators observed and recorded the par ticipants interacting with the prototype to perform the proposed tasks. Throughout the session, the evaluators asked participants to give feedback on the prototype, aiming to identify interaction <sup>fl</sup>aws and opportunities for improvement.

The study was divided in three rounds. At each round, the researchers ranked the problems and suggestions of the last cycle, and made the corresponding corrections and improvements in a new version of the prototype, incrementally enhancing the user-system inter action before a <sup>fi</sup>nal evaluation round, which involved experts in sce nario reduction. Before each session, the researchers assessed the participants' knowledge by means of a questionnaire <sup>4</sup>. The questionnaire asked about the users' background and professional areas, as well as speci<sup>fi</sup>c knowledge about the graphical views, the de<sup>fi</sup>nition of a percentile series, and time-series analysis. Answers to these questions were ranked on a <sup>fi</sup>ve-point scale, ranging from 1 (no knowledge) to 5

(expert knowledge).

## 5. Results and discussion

A total of 29 people participated in the study: 11 on the <sup>fi</sup>rst round, 8 on the second, and 10 on the third round.

The <sup>fi</sup>rst round was considered a preliminary study, and was conducted in order to assess the feasibility of our approach for scenario reduction and to help plan a more detailed study. The 11 participants of this study are all laboratory colleagues of the researchers, all of them with science and technology backgrounds, comprising 8 graduate and 3 undergraduate students, with varying levels of education: 1 D.Sc., 6 M.Sc., 1 B.Sc., and 3 undergraduate students in Electronics Engineering. None of them had prior knowledge of the scenario reduction problem before the evaluation sessions.

We asked participants to <sup>fi</sup>nd 3 to 5 scenarios closest to the $\mathrm { P } _ { 5 0 }$ scenario calculated from the ensemble, using the Cumulative Water Production (WP) property. Most users had no problems in <sup>fi</sup>nding a set of scenarios. Most of the issues raised by them were related to the usersystem interaction. Some users commented on the cluttering of the Bump chart, which is a problem the researchers had somewhat anticipated during the development phase of the prototype. They also reported some confusion regarding the Time-lapsed LAMP chart. Most users found it hard to interpret, since it has no direct connection to the original data, but it is rather a representation of the distances between the scenarios at each time step.

The second evaluation round was composed exclusively of undergraduate students with no prior knowledge of the scenario reduction problem. These students were recruited from Human-Computer Interaction classes of the Department of Informatics of PUC-Rio. All participants of this round work on information technology related areas and have a varying level of experience, ranging from the <sup>fi</sup>rst to the last semester in their courses.

For this round, we opted for participants that had little probability of knowing the target area. This allowed us to assess the di<sup>fi</sup>culty of the task, as well as any user interface issues that could interfere with the study. Since little or no previous knowledge could be an obstacle for the study, we prepared a small tutorial in order to explain the concept of percentiles, and to present the prototype, its graphical views and interaction mechanisms. This tutorial was given after the pre-session questionnaire. The participants were also given an opportunity to use the prototype at will for a few minutes, in order to clarify any doubts about the concepts presented in the tutorial. We noticed that, since these participants were not used to this area, they paid more attention to the interaction mechanisms, and made several comments that helped us re<sup>fi</sup>ne the prototype even further.

In this round, most of the participants claimed to have little or no knowledge of the graphical views, or time-series analysis, as expected. Fig. 5 (Round 2) shows their answers to the questionnaire.

![](/api/attachments/CU7W7GM9/fulltext/images/505971af45868aae5c663e8ebb601b604ac69e78778574a934cdb82abb3f8548.jpg)  
Fig. 5. Second and third round participants' answers to the knowledge-based questions of the pre-session questionnaire.

Most users claimed to not know about the concepts, while no user claimed to know them well, or to be an expert at any of them. Regarding the percentile and time-series concepts, the number of users who had seen these concepts before was higher; however, at least half of them still claimed to have no knowledge of these concepts.

After the <sup>fi</sup>rst 4 evaluation sessions for this round, we noticed that participants were confused by the bump chart's ranking concept. They seemed to associate a higher numerical rank with better adherence to the reference scenario, which was not the case. Coincidentally, these participants were all from the <sup>fi</sup>rst half of the course periods. In order to further evaluate this issue, the bump chart was changed for the last 4 sessions, in order to present a better adherence with a higher numerical rank. Some participants understood this ranking concept more naturally after the change. However, more studies must be performed in order to investigate whether previous knowledge is necessary to properly interpret this chart.

The main issues found during this evaluation round were: (i) confusion between rank and score with the Bump chart; and (ii) confusion between time steps and scenario IDs with the Distance chart.

And the main improvements suggested by the participants in the second round were: (i) “undo” option for the selection; (ii) band-based group selection for the Bump and/or Distance charts; (iii) <sup>fi</sup>lter out the time steps of the Fan and Bump chart using an X-axis zoom feature; (iv) <sup>fi</sup>lter out scenarios using the Distance chart group selection feature (remove the scenarios above the threshold line); and (v) adopt similar behavior for the Bump Chart.

Before the experiment started, we expected the users to rely heavily on the Distance chart, because the task was to <sup>fi</sup>nd the scenarios closest to a pre-de<sup>fi</sup>ned baseline. Such task naturally invites the user to rely upon the Distance chart, while using the other views as guides for the selection. We also expected some confusion regarding the Bump and Time-lapsed LAMP charts, since the information presented by them is much denser compared to the other charts. However, most users of the second round used the Bump and Distance charts as their main drivers, while the Fanchart was used more as a reference, which partly conforms to our expectations. Also, some users did not use the selection mechanism provided, relying only on the tooltips and highlights between the views. The users who did use the selection mechanism, used the group selection to <sup>fi</sup>nd an initial set of answers, and then analyzed those in order to make their choice, which is what we expected.

For the third evaluation round, the participants were 8 PhD

Professors, 1 Post-doctoral researcher working in di<sup>f</sup>erent departments of PUC-Rio, and 1 Software Engineer working outside the University. They all work with – or have extensive academic experience on – sce nario reduction and its applications (see Fig. 5, Round 3). As expected, most of them claimed to have good knowledge or expertise in the percentile and time-series analysis areas, i.e., their knowledge of the related subjects was much higher, compared to the participants of the second round. Therefore, the tutorial made for the second round par ticipants was not administered to these users.

As for the graphical views, their knowledge tended more to the negative side. Some users claimed to know the views, but the percentage of users who claimed expertise was lower. We gave the participants an overview of the prototype and its features, but an explanation about percentiles, time-series, and scenario reduction was not necessary. Of the 10 participants of this round, only 8 solved all tasks proposed; the other 2 provided an extremely rich discussion but, unfortunately, their available time ran out after more than 2 h of discussions and little usage of the prototype.

During the observation sessions, the participants did not pay too much attention to the user interface, but rather focused on the scenario reduction task. All participants made extensive use of the mouse-hover to highlight features, while only a few used the click-to-select feature.

During the post-task interviews, all participants commented on the di<sup>fi</sup>culty of scenario reduction problems, especially considering that a crucial and potentially costly decision must be made based on the results of this task. They appreciated the possibility of visually exploring the ensemble, mainly because any visual patterns can then be easily identi<sup>fi</sup>ed. When asked about the existence of other visual approaches, the participants claimed to not know any similar approaches to ours for this particular problem. We also asked about other areas besides oil & gas that they thought would bene<sup>fi</sup>t from this approach. Four partici pants mentioned their own research area, energy resource management, since it involves similar data and problems, but instead of oil/ water production they deal with solar, wind, and water-based electric energy resources and scenarios where sunlight, wind, and rainfall may not be enough to sustain the energy generation demand during the whole year, thus requiring the more expensive thermoelectric plants to be activated. Another participant mentioned stock management and distribution on big chain-stores involving varying demands for certain items based on region, seasonality, and managing uncertain market conditions. Their feedback gives us con<sup>fi</sup>dence on the novelty and general applicability of our work. When asked about the most helpful graphical views, all participants answered either the Bump or Distance charts. However, none of them extracted meaningful information from the Time-lapsed LAMP chart.

## 6. Conclusions

In this paper, we presented a novel graphical approach to scenario reduction on time series ensemble data. Our approach proved to be useful on an exploratory analysis of such data on the same context of scenario reduction. We evaluated the feasibility of our approach by performing an empirical study with a series of users, both experienced in the scenario reduction area and not. By observing their interactions and interviewing them afterwards, we obtained invaluable insights on the usefulness of our approach. Our contributions are threefold: (i) a visual interactive approach to assist the user in selecting a subset of meaningful scenarios from a time-series ensemble dataset, thus solving an instance of the scenario reduction problem; (ii) an adaptation of a multidimensional projection algorithm to generate a visual representation of the time component of a dataset; and (iii) an approach to create a ranked, cumulative version of a time-based dataset in orde to perform a visual assessment by using Bump charts.

According to the participants of our study, the most useful views are the Bump and Distance charts. Both charts convey the distance between the scenarios and a reference, which is useful for the kind of task proposed. However, some of the inexperienced users seemed to be confused by the ranking measure used in the Bump chart. They associated rank with score, meaning that a higher rank meant a better scenario, which is exactly the opposite of the information conveyed by the chart itself. In order to test this, we altered the Bump chart to present better ranked scenarios with higher numerical ranks. The results showed that some users seemed more comfortable with this alteration. We reverted this alteration for the experts' evaluation round, and none of them seemed to be confused by the ranking/score concept. More studies must be performed, but, so far, we may a<sup>fi</sup>rm that the Bump chart requires some knowledge of rankings to be used properly.

As for the Time-lapsed LAMP chart, almost every user found it confusing. This can be explained by the fact that it does not represent the data directly, but through a series of projections of data at each time step. The axes caused some confusion as well, some users did not un derstand that they are akin of Principal Components, and not attributes contained in the dataset. Another serious issue with this chart is that some of the scenarios, while close to the reference in the other views, seemed to be further apart when viewed in this chart. This may be due to a high stress in the projected con<sup>fi</sup>guration. A higher stress means that the projection failed to <sup>fi</sup>nd an accurate, low dimensional representation for the data.

All participants of the third evaluation round, who were experts in the domain, agreed that the proposed approach <sup>fi</sup>lls a gap in the data exploration phase during decision making. However, there are some issues to overcome. The Bump chart tends to become very cluttered as the number of scenarios increase. Some performance issues also inter fered during the tests; however, those are related to the prototype implementation, and can be mitigated by a proper implementation of the approach. The color palettes can also confuse the user. On the positive side, the same experts agreed on the general applicability of our approach on other <sup>fi</sup>elds, such as hydroelectric, wind and thermal energy resource production/allocation, while a couple of them have shown great interest in already implementing a re<sup>fi</sup>ned version of our ap proach on their decision-making processes. One participant also raised the possibility of application to the evaluation process of oil well formation.

The issues and feedback collected raise the opportunity for continuing our work. We aim to use the latest feedback to further re<sup>fi</sup>ne our prototype and implement it in a real decision making process by some of the interviewed experts. Such <sup>fi</sup>eld testing will help us validate the results obtained so far. One expert asked if it was possible to infer a stochastic program for scenario reduction from a user's decision. When we presented this question to some of the other experts, they too were interested in an answer, so we intend to pursue it further. In general, other multidimensional projection techniques, as well as time-series distance metrics, can also be explored.

## Acknowledgments

We thank PETROBRAS, CNPq, and CAPES for partially supporting this research. We also thank Regis Romeu, Alexandre Emerick, and Luciano Reis for providing the ensemble used in the tests; and Prof. Waldemar Celes Filho and Tecgraf/PUC-Rio for the use of Geresim. Finally, we thank the colleagues and students who participated in the study, and the reviewers, for their valuable feedback on our work.

## References

[1] J. Sanyal, Song Zhang, J. Dyer, A. Mercer, P. Amburn, R.J. Moorhead, Noodles: a tool for visualization of numerical weather model ensemble uncertainty, IEEE Transactions on Visualization and Computer Graphics 1077-2626, 16 (6) (2010) 1421 1430.

[2] H.K.H. Lee, M. Taddy, G.A. Gray, Selection of a representative sample, Journal of Classi<sup>fi</sup>cation 0176-4268, 27 (1) (2010) 41–53.

[3] M. Hummel, H. Obermaier, C. Garth, K.I. Joy, Comparative visual analysis of la grangian transport in cfd ensembles, IEEE Transactions on Visualization and Computer Graphics 19 (12) (2013) 2743 2752.

[4] Y. Wang, S. Tang, Y.-D. Zhang, J.-T. Li, D. Wang, Representative selection based on sparse modeling, Neurocomputing 139 (2014) 423 431.

[5] Y. Yang, G.I. Webb, J. Cerquides, K.B. Korb, J. Boughton, K.M. Ting, To select or to weigh: a comparative study of linear combination schemes for superparent-one dependence estimators, IEEE Transactions on Knowledge and Data Engineering 19 (12) (2007) 1652–1665.

[6] M.N. Phadke, L. Pinto, O. Alabi, J. Harter, R.M. Taylor II, X. Wu, H. Petersen, S.A. Bass, C.G. Healey, Exploring ensemble visualization, IS&T/SPIE Electronic Imaging, International Society for Optics and Photonics, 201282940B–82940B.

[7] M.H. Alrefaei, M. Almomani, Subset selection of best simulated systems, Journal of the Franklin Institute 344 (5) (2007) 495–506.

[8] M. Armstrong, A. Ndiaye, R. Razanatsimba, A. Galli, Scenario reduction applied to geostatistical simulations, Mathematical Geosciences 1874-8961, 45 (2) (2013) 165–182.

[9] J. Dupačová, N. Gröwe-Kuska, W. Römisch, Scenario reduction in stochastic pro gramming, Mathematical Programming 1436-4646. 95 (3) (2003) 493–511.

[10] W. Aigner, A. Bertone, S. Miksch, C. Tominski, H. Schumann, Towards a conceptual framework for visual analytics of time and time-oriented data. Simulation Conference, 2007 Winter, 2007, pp. 721–729.

[11] G. Andrienko, N. Andrienko, D. Keim, A.M. MacEachren, S. Wrobel, Editorial: challenging problems of geospatial visual analytics, Journal of Visual Languages and Computing 22 (4) (2011) 251–256.

[12] D.A. Keim, F. Mansmann, D. Oelke, H. Ziegler, Visual Analytics: combining automated discovery with interactive visualizations, Proceedings of the 11<sup>th</sup> International Conference on Discovery Science, Springer-Verlag, Berlin, Heidelberg, 2008, pp. 2–14.

[13] J. Kohlhammer, D. Keim, M. Pohl, G. Santucci, G. Andrienko, Solving problem with visual analytics, Procedia Computer Science 1877-0509, 7 (0) (2011) 117 120 http://www.sciencedirect.com/science/article/pii/S1877050911007009 proceed. ings of the 2<sup>nd</sup> European Future Technologies Conference and Exhibition 2011 (FET 11).

[14] X. Cheng, D. Cook, H. Hofmann, Enabling interactivity on displays of multivariate time series and longitudinal data, Journal of Computational and Graphical Statistics 25 (4) (2016).1057–1076

[15] P. Joia, F.V. Paulovich, D. Coimbra, J.A. Cuminato, L.G. Nonato, Local a<sup>fi</sup>ne multidimensional projection, IEEE Transactions on Visualization and Computer Graphics 17 (12) (2011) 2563–2571 JSSN 10772626.

[16] E. Tufte, Envisioning Information, Graphics Press, 1990.

[17] A.B. Alencar, K. Börner, F.V. Paulovich, M.C.F. de Oliveira, Time-aware visualization of document collections, Proceedings of the 27th Annual ACM Symposium on Applied Computing - SAC ’12, SAC ’12, ACM Press, New York, New York, USA, 2012, pp. 997–1004 ISBN 9781450308571.

[18] C. Wong, M.C.F. Oliveira, R. Minghim, Multidimensional projections to explore time-varying multivariate volume data, Graphics, Patterns and Images (SIBGRAPI), 2013 26th Conference on, 2013, pp. 107–114.

[19] R. a. Becker, W.S. Cleveland, M. Hill, Brushing scatterplots, Technometrics 0040- 1706, 29 (2) (1987) 127–142

[20] A. Buja, J. McDonald, J. Michalak, W. Stuetzle, Interactive data visualization using focusing and linking, Proceeding Visualization ’91, IEEE Comput. Soc. Press, 1991, pp. 156–163 ISBN 0-8186-2245-8.

[21] E. Britton, P. Fisher, J. Whitley, The In<sup>fl</sup>ation Report projections: understanding the fan chart, Bank of England Ouarterly Bulletin (Feb) (1998) 30–37.

[22] M. Armstrong. A. Vincent. A. Galli, C. Meheut, Genetic algorithms and scenaric

reduction, Journal of the Southern African Institute of Mining and Metallurgy 114 (3) (2014) 237–244 ISSN 22256253.

[23] N. Gröwe-Kuska, H. Heitsch, W. Römisch, Scenario reduction and scenario tree construction for power management problems, 2003 IEEE Bologna PowerTech - Conf, Proceedings, vol, 3. 2003, pp. 152–158 ISBN 0780379675.

[24] L.A. Meira, G.P. Coelho, A.A.S. Santos, D.J. Schiozer, Selection of representative models for decision analysis under uncertainty, Computers & Geosciences 88 (2016) 67–82 ISSN 00983004.

[25] H. Heitsch, W. Römisch, Scenario reduction algorithms in stochastic programming, Computational Optimization and Applications 24 (2-3) (2003) 187–206 ISSN 09266003.

[26] N.D. Domenica, G. Mitra, P. Valente, G. Birbilis, Stochastic programming and sce nario generation within a simulation framework: an information systems perspective, Decision Support Systems 0167-9236, 42 (4) (2007) 2197–2218 decision Support Systems in Emerging Economies.

[27] B. Kawas, A. Koc, M. Laumanns, C. Lee, R. Marinescu, M. Mevissen, N. Taheri S. Van Den Heever, R. Verago, Uni<sup>fi</sup>ed framework and toolkit for commerce opti mization under uncertainty, IBM Journal of Research and Development 58 (5/6) (2014) 12–1.

[28] H. Park, M.A. Bellamy, R.C. Basole, Visual analytics for supply network management: system design and evaluation, Decision Support Systems 0167-9236, 91 (2016) 89–102.

[29] I. Demir, C. Dick, R. Westermann, Multi-charts for comparative 3D ensemble vi sualization, IEEE Transactions on Visualization and Computer Graphics 20 (12) (2014) 2694 2703 ISSN 10772626.

[30] C. Scheidt, J. Caers, Uncertainty quanti<sup>fi</sup>cation in reservoir performance using distances and kernel methods-application to a West Africa deepwater turbidite re servoir, SPE Journal 1086-055X, 14 (04) (2009) 680 692.

[31] Z. Sahaf, H. Hamdi, F. Maurer, L. Nghiem, M.C. Sousa, Clustering of geological models for reservoir simulation studies in a visual analytics framework, 78th EAGE Conference and Exhibition 2016, 2016.

[32] J. Waser, A. Konev, B. Sadransky, Z. Horváth, H. Ribičiç, R. Carnecky, P. Kluding, B. Schindler, Many plans: multidimensional ensembles for visual decision support in <sup>fl</sup>ood management, Computer Graphics Forum 33 (3) (2014) 281–290 ISSN 14678659.

[33] C. Scheidt, J. Caers, Representing spatial uncertainty using distances and kernels, Mathematical Geosciences 41 (4) (2009) 397 419 ISSN 18748961.

[34] H. Heitsch, W. Römisch, Scenario tree modeling for multistage stochastic programs, Mathematical Programming 0025-5610. 118 (2) (2009) 371–406

[35] P. Sarma, W.H. Chen, J. Xie, Selecting representative models from a large set of models, SPE Reservoir Simulation Symposium, Society of Petroleum Engineers, 2013ISBN 9781627480246

[36] J.B. Kruskal, M. Wish, Multidimensional Scaling, vol. 31, (1978), p. 93 ISBN 0- 8039-0940-3

[37] S. Suzuki, J.K. Caers, History matching with an uncertain geological scenario, SPE Annual Technical Conference and Exhibition, Society of Petroleum Engineers, 2006ISBN 978-1-55563-149-9

[38] K. Park, J. Caers, History matching in low-dimensional connectivity-vector space, EAGE Conference on Petroleum Geostatistics, September 2007, 2007, pp. 10–14 JSBN 9073781485.

[39] C. Faloutsos. K.-I. Lin. FastMap: a fast algorithm for indexing, data-mining and visualization of traditional and multimedia datasets. Proceedings of the 1995 ACM SIGMOD international conference on Management of data, vol. 24, 1995, pp. 163–174 JSBN 0897917316. ISSN 0163-5808.

[40] F.V. Paulovich, C.T. Silva, L.G. Nonato, Two-phase mapping for projecting massive data sets, IEEE Transactions on Visualization and Computer Graphics 1077-2626, 16 (6) (2010) 1281–1290.

[41] F.V. Paulovich, L.G. Nonato, R. Minghim, H. Levkowitz, Least square projection: a fast high-precision multidimensional projection technique and its application to document mapping, IEEE Transactions on Visualization and Computer Graphics 1077-2626, 14 (3) (2008) 564 575.

[42] M. Ester, H.P. Kriegel, J. Sander, X. Xu, A density-based algorithm for discovering clusters in large spatial databases with noise, Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining, 1996, pp. 226–231 ISBN 1577350049, ISSN 09758887.

[43] D.M. Eler, F.V. Paulovich, M.C.F. De Oliveira, R. Minghim, Topic-based coordina tion for visual analysis of evolving document collections, Proceedings of the International Conference on Information Visualisation, 2009, pp. 149 155 ISBN 978-0-7695-3733-7, ISSN 10939547.

[44] K. Potter, A. Wilson, P.T. Bremer, D. Williams, C. Doutriaux, V. Pascucci, C.R. Johnson, Ensemble-vis: a framework for the statistical visualization of ensemble data, ICDM Workshops 2009 - IEEE International Conference on Data Mining, 2009, pp. 233 240 ISBN 9780769539027.

[45] D. Steagall, D. Schiozer, Uncertainty analysis in reservoir production forecasts during appraisal and pilot production phases, SPE Reservoir Simulation Symposium. 2001.

[46] D.J Schiozer,. E.L.. Ligero, S.B. Suslick. A.P.A. Costa. J.A.M. Santos. Use of re presentative models in the integration of risk analysis and production strategy definition. Journal of Petroleum Science and Engineering 44 (1-2) (2004) 131–141 JSSN 09204105

[47] J.C. Gower, G.B. Dijksterhuis, Procrustes Problems, 30 Oxford University Press on

Demand, 2004.

[48] J.D. Hunter, Matplotlib: A 2D graphics environment, Computing in Science & Engineering 1521-9615, 9 (3) (2007) 90 95.

[49] S. van der Walt, S.C. Colbert, G. Varoquaux, The NumPy array: a structure for ef-<sup>fi</sup>cient numerical computation, Computing in Science & Engineering 1521-9615, 13 (2) (2011) 22–30.

[50] E. Jones, T. Oliphant, P. PetersonOthers, SciPy: Open Source Scienti<sup>fi</sup>c Tools for Python, (2001) http://www.scipy.org/.

[51] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, G. Louppe, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, É. Duchesnay, Scikit-learn: machine learning in Python, Journal of Machine Learning Research 12 (2012).

[52] G.D. Avansi, D.J. Schiozer, UNISIM-I: synthetic model for reservoir development and management applications, International Journal of Modeling and Simulation for the Petroleum Industry 9 (1) (2015).

[53] A.A. Emerick, A.C. Reynolds, Ensemble smoother with multiple data assimilation, Computers & Geosciences 0098-3004. 55 (2013) 3–15.

![](/api/attachments/CU7W7GM9/fulltext/images/90065ed7537509c04e5c95ba3be7c15705d7816d3fc5cef056c88e9f6b0851ac.jpg)

Guilherme Schardong is a Doctoral Candidate at the Informatics Department of the Ponti<sup>fi</sup>cal Catholic University of Rio de Janeiro (PUC-Rio). He has a Master's degree in Informatics (2014) and a Bachelor of Computer Science (2011), both obtained at the Federal University of Santa Maria (UFSM). His research area is Computer Graphics, with strong focus in Scienti<sup>fi</sup>c Visualization and, more recently, Decision Making. He likes to develop and apply computational techniques to obtain information and knowledge from raw data.

![](/api/attachments/CU7W7GM9/fulltext/images/9a4def71a155a56c816b96d8d99a2685f68c42b4909a09dd1a28f393ef98cf91.jpg)

Ariane Moraes Bueno Rodrigues is a PhD student at the Informatics Department of PUC-Rio in the field of Human Computer Interaction. In the last vear. she has been a lec turer in HCI classes of the undergraduate Computer Science course at PUC-Rio. She was the winner of the BPI Challenge 2017, along with other colleagues, in the academic category. Her current research interests involve: increasing the quality of use of interactive systems; data science and visual analytics.

![](/api/attachments/CU7W7GM9/fulltext/images/531ba0e30d5154a36b91821d2d75a795d797a200cc107ce995a38a3db59676a5.jpg)

Simone Diniz Junqueira Barbosa is an Associate Professor at the Informatics Department of the Ponti<sup>fi</sup>cal Catholic University of Rio de Janeiro (PUC-Rio), where she teaches, advises and conducts research in the <sup>fi</sup>eld of Human-Computer Interaction (HCI). Her current research interests involve: model-based interactive systems design; multimodal user interaction; data science and visual analytics; digital storytelling, increasing the quality of use (e.g. usability, communicability, accessibility) of interactive systems in diverse domains, by means of adaptation, analogymaking mechanisms, and other arti<sup>fi</sup>cial intelligence techniques.

![](/api/attachments/CU7W7GM9/fulltext/images/9e4df103dad6ed6e297dce0f3d0955165eda593dc7ce6a3a73ca46048c96a296.jpg)

Hélio Lopes is an Associate Professor in the Department of Informatics at PUC-Rio. He has a Doctoral degree in Mathematics (1996), a Master's degree in Informatics (1992) and a Bachelor degree in Computer Engineering (1990). All of these degrees were obtained at PUC-Rio, His research is mainly in the fields of Computer Graphics and Computational Modeling. He likes to develop and to apply advanced mathematical and computational techniques to solve realworld problems that have engineering, scienti<sup>fi</sup>c and industrial relevance.
