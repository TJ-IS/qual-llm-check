---
otero_id: 19527
otero_key: "8UF56Q2J"
title: "A DSS for planning of soil-sensitive field operations"
authors: "Dionysis D. Bochtis; Claus G. Sørensen; Ole Green"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.12.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A DSS for planning of soil-sensitive <sup>fi</sup>eld operations

Dionysis D. Bochtis ⁎, Claus G. Sørensen, Ole Green

University of Aarhus, Faculty of Science and Technology, Department of Engineering, Blichers Allé 20, 8830 Tjele, Denmark

## a r t i c l e i n f o

Article history: Received 19 May 2011 Received in revised form 18 December 2011 Accepted 22 December 2011 Available online 30 December 2011

Keywords: Route planning B-patterns Agricultural vehicles Operations planning Navigation

## a b s t r a c t

The current increased size of agricultural vehicles aggravates the problem of soil compaction causing increased energy requirements, increased ${ \mathrm { C O } } _ { 2 }$ emissions, and reduced yields. The aim of this paper was to develop a DSS for optimize route planning in terms of minimized risk for soil compaction for agricultural vehicles carrying time-depended loads. The developed system uses as input <sup>fi</sup>eld and operational characteristics, including a potential risk indicator map based on speci<sup>fi</sup>c measure of distributed soil physical–chemical properties. It provides the optimal <sup>fi</sup>eld-work tracks traversal sequence which can be executed using state-ofthe-art auto-steering and navigation-aiding systems available on modern agricultural vehicles. The system has been demonstrated and tested for heavy application units used for organic fertilizer. The risk factor was reduced up to 61% by using the corresponding optimal plans instead of the non-optimal conventional ones that an operator would follow

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

The structural development within agriculture, as well as the external demands imposed on agriculture, requires that new knowledge intensive technology including knowledge management become an integral part of environmental-friendly. Therefore, there is a need for innovation and technological development, which can contribute to an ef<sup>fi</sup>cient utilization of applied resources while at the same maintain the overall sustainability of agriculture. In the current situation, the focus is improved resource utilization and environmental impact and this requires improved process control and other aspects of automation. At the same time, the biology has to be fully integrated in the new technology.

A number of technological foresights have recommended multidisciplinary efforts matching the technical potentials with the prevailing production challenges and user requirements. The research efforts is aimed at a system perspective, where the development and implementation of automation is looked upon from multiple perspectives like energy, environment, management, mechanization system, etc. as well as a clear understanding that the industrial automation process and the biological bio-production are distinctly different. In this regard, it becomes important to de<sup>fi</sup>ne the production challenges which the new technology must meet. A number of decision support systems aimed at supporting the manager meeting the challenges facing agriculture including demands for reduced resource inputs, cleaner production methods, reduced environmental impact, maintaining quality products, etc. [16,18].

One of the main speci<sup>fi</sup>c challenges is to sustain the soil as growth medium. Soil compaction is one factor that deteriorates soil quality as a growth medium [22]. With the continued increase of size of farm machinery, the problem of soil compaction is aggravated causing increased power and energy requirements, increased $\mathrm { C O } _ { 2 }$ emissions, dif<sup>fi</sup>culties in seedbed preparation, plants emergence, plants growth during the growing season, and reduced yields. Topsoil compaction is mainly in<sup>fl</sup>uenced by the magnitude of contact stresses and without any mechanical tillage, topsoil compaction effects may last for up to 5 years [15]. Subsoil compaction, on the other hand, is mostly related to the magnitude of wheel load. In the upper subsoil (25–40 cm), the natural recovery from compaction is very slow if it occurs, while the compaction below 40 cm is considered as persistent [1] leading to long-term yield reduction [12].

The continuous increase in the weight of <sup>fi</sup>eld machines and the necessity to use these machines in un-favorable soil conditions due to timeliness related cost have increased the potential for soil compaction. Combine harvesters of more than 30 Mg and organic fertilizing tankers of 35 Mg is a common occurrence in <sup>fi</sup>eld operations. Fully loaded, the weight of two-axle sugar beet harvesters is about 35–40 Mg and the weight of three-axle harvester up to 50 Mg. Fig. 1 shows an illustrative example of a damaged <sup>fi</sup>eld area caused by a heavy agricultural vehicle travelled over an area sensitive to soil compaction.

Current research studies indicate that it is important to effectively control the mechanical impacts of agricultural machinery on soil structure in order to reduce the risk of soil compaction [14]. A number of preventive strategies have been reported [7,22] involving, for example, the control of wheel/track loads and the use of low tire in<sup>fl</sup>ation pressures in order to adjust the machines and equipment used in critical conditions to be aligned with the actual strength of the subsoil. Other measures have included the establishment of recommendations for wheel load-ground contact pressure combinations in different soil conditions, guidelines for working at the most appropriate soil moisture content, targeted loosening of both topsoil and subsoil, the use of low ground pressure equipment, etc. Nevertheless, these measures are often compromised by inherent cost constraints. As for example, the alignment of the machinery size with the soil strength capability might require the use of a small-sized, and consequently low capacity, machine which results in increased timeliness and labor cost, as well as increased unit machinery cost.

![](/api/attachments/8UF56Q2J/fulltext/images/36d61f613bf8c74d2dfc77b0d6f8c73952ba85beef2fd73034d4a0e54f5bf820.jpg)  
Fig. 1. Damaged soil as a result of unsuitable combination of traf<sup>fi</sup>cked track and vehicle load.

In order to extend the current preventing measures to integrate and comply with the cost constraints mentioned above, there is a need for researching planning tools involving optimization of the <sup>fi</sup>eld traf<sup>fi</sup>c, in terms of route planning, under the criterion of the minimization of risk on soil compaction.

Field traf<sup>fi</sup>c planning for agricultural vehicles has to be addressed as two distinct problems. The <sup>fi</sup>rst problem regards the generation of the traf<sup>fi</sup>c lines (<sup>fi</sup>eld-work tracks) and is related to the representation of the <sup>fi</sup>eld as a geometrical entity. A number of methods dealing with this problem have been developed recently (e.g., [9,11,13,17]). The second problem regards the optimization of the routing or motion of the vehicles within this geometrically de<sup>fi</sup>ned world. In relation to this problem, advanced methods based on combinatorial optimization have recently been introduced. A new type of algorithmically-computed optimal <sup>fi</sup>eldwork patterns, the Bpatterns, has been recently introduced [2] providing the optimal <sup>fi</sup>eld-work track sequencing according to one or more criterions. B-patterns are based on an approach according to which the <sup>fi</sup>eld coverage is expressed as the traversal of a weighted graph, and the problem of <sup>fi</sup>nding optimal traversal sequences of <sup>fi</sup>eld-work tracks is equivalent to <sup>fi</sup>nding the shortest tours in the graph. The weight of the graph arcs could be based on any relative optimization criterion, such as, total or non-working travelled distance, total or non-productive operational time, a soil compaction measure, etc. Contrary to any traditional <sup>fi</sup>eld-work pattern, B-patterns do not follow the repetition of standard motifs but they are the unique result of the optimization approach on the speci<sup>fi</sup>c combination of the mobile unit kinematics and dimensions, the operating width, the <sup>fi</sup>eld shape, and the optimization/s criterion/s. The implementation of B-patterns for autonomous [5] and conventional agricultural machines supported by auto-steering systems [4] showed that, under the criterion of the minimized non-working distance, this distance can be reduced signi<sup>fi</sup>cantly reaching up to 50%. B-patterns can be implemented in the majority of <sup>fi</sup>eld operations, involving different machinery systems (single or multiple-machinery system) and different operational characteristics (deterministic, stochastic, and dynamic). These patterns can be generated from the implementation of the well-known combinatorial optimization problem, the vehicle routing problem (VRP), after the appropriate abstractive representations of the corresponding routing problems [3].

As mentioned, the pursued approach involve that the resulting optimal traf<sup>fi</sup>c pattern consists of sequences of <sup>fi</sup>eld-work tracks that do not follow any pre-determined standard motif. In contrast, the track sequence is a result of an optimization under a minimization criterion, which makes it feasible to extend and introduce as a criterion the risk for soil compaction for speci<sup>fi</sup>c types of <sup>fi</sup>eld operations. These speci<sup>fi</sup>c <sup>fi</sup>eld operations are characterized by varying vehicle weight over time during operation execution, e.g. harvesting and tanker application of fertilizer.

The aim of this paper is to present a decision support system for the route planning for agricultural vehicles carrying time-depended loads with the objective of reducing the risk of soil compaction. The principle relies on the basic hypothesis that an area to be worked which has low soil strength, and therefore is more sensitive to compaction, should be worked with a corresponding low vehicle load.

## 2. System description

The proposed system is targeted toward input material <sup>fl</sup>ow <sup>fi</sup>eld operations where a speci<sup>fi</sup>c quantity of a material is transported by the agricultural vehicle and is subsequently distributed over the <sup>fi</sup>eld area (e.g., seeding, spraying, and fertilizing). Speci<sup>fi</sup>cally, the system will be useful for planning the application of organic fertilizer. This speci<sup>fi</sup>c operation incur a high risk for soil compaction due to relatively heavy machinery used (e.g. tankers up to 35 Mg) for the application of organic fertilizer in various crops [1].

The devised system regards the most common area coverage practice aimed at <sup>fi</sup>eld operations according to which the complete covering, in a geometrical sense, of the <sup>fi</sup>eld area involves a set of parallel <sup>fi</sup>eld-work tracks, or trips, which starts at one boundary of the <sup>fi</sup>eld and terminates at the opposite boundary. An overview of the system components as well as their inter-connections in terms of input, output and related processes is presented in Fig. 2. The program was developed using the MATLAB technical programming language (The MathWorks, Inc., Natwick, Mass).

## 2.1. Input

## 2.1.1. Field-specific data

These data are associated with the direct <sup>fi</sup>eld attributes and include:

• The <sup>fi</sup>eld boundary. The <sup>fi</sup>eld boundary is represented by an ordered set of points, e.g. in UTM coordinates, where their sequential, e.g. pair-wise, connections constitute the polygon that embraces the <sup>fi</sup>eld area

• The driving direction. This regards the direction of the parallel <sup>fi</sup>eldwork tracks

• Potential risk indicator measurements. This indicator is a result of the interpretation of a number of individual spatial distributed soil physical–chemical properties (or a combination of them).

## 2.1.2. Operation-specific data

These data include the working width, that is the width of the applicator and also representing the width of the <sup>fi</sup>eld-work tracks, the tanker capacity, that is the maximum load that vehicle can carry, and the dosage rate, that is the amount of the applied material (e.g. organic fertiliser) per unit area.

## 2.2. Spatial risk representation

## 2.2.1. Geometrical field representation

Initially, a 2-dimensional coordinate system is assigned to the <sup>fi</sup>eld (e.g., the transformation of the UTM system), having the yaxis parallel to the driving direction. As mentioned above, <sup>fi</sup>eld coverage involves a set of parallel <sup>fi</sup>eld-work tracks. In this stage, the parameters for the description of these tracks are generated. These parameters regard the coordinates of the points which de<sup>fi</sup>ne each individual track. The starting and ending points of the <sup>fi</sup>eld-work tracks are located on the internal <sup>fi</sup>eld boundary, that is the offset of the <sup>fi</sup>eld boundary equaling a width, comprising a number of sequential passes that the agricultural vehicle has to perform peripheral to the main <sup>fi</sup>eld area before or after (depending on the operation) the execution of the operation con<sup>fi</sup>ned to the main <sup>fi</sup>eld area. An illustrative example is presented in Fig. 3.

## 2.2.2. Reference grid generation

In a next step, a reference orthogonal grid is generated. Each cell of the grid is a square with vertex equal to the operating width. Fig. 4 presents two different grids (corresponding to the same driving direction but for different machine used) as a function of the operating width.

![](/api/attachments/8UF56Q2J/fulltext/images/74374fff5ca637f1464837ba4e46edcba013b96c24e4df305e34169ab0b9568b.jpg)  
Fig. 2. Overview of the system components and related inter-connections.

![](/api/attachments/8UF56Q2J/fulltext/images/baba5777d3991e9c2ec138825d16a55597928521e97e19db350fa47da85c0087.jpg)  
Fig. 3. An example of a geometrical <sup>fi</sup>eld representation for two different driving directions.

## 2.2.3. Interpolation

The relative risk map is the result of a spatial interpolation derived from the basic distributed risk indicator measurements and superimposed on the reference grid of the <sup>fi</sup>eld. The interpolation method estimates un-sampled sites within the <sup>fi</sup>eld. The followed method is the reverse distance method plus a weight factor correlated to the number of the distributed measurements expressing the reliability of the mean value.

## 2.3. Planning

## 2.3.1. Sorting of tracks

The sequential sorting of the tracks according to a soil compaction measure is based on the derived relative risk map. In a <sup>fi</sup>rst step, a threshold value between 0 and 1 is de<sup>fi</sup>ned as an indicator of the distinction between low and high risk of soil compaction. For each track, a value is allocated depicting the relative number of cells where the normalized value of the risk indicator is higher than the threshold value. The tracks are sorted according to this estimated value and subsequently, a permutation of the tracks is generated.

## 2.3.2. Estimation of number of routes

An organic fertilizing operation, as any material input operation, has to comply with capacity constraints since a full load carried by the vehicle is generally not suf<sup>fi</sup>cient for full area coverage of a normal-sized <sup>fi</sup>eld, and thus, a number of routes are required. A “route” is designated as the work operation composed of a number of part operations carried out by the vehicle: <sup>fi</sup>lling the tanker at the facility unit, driving from the facility to the position where the application is commence or resumed, applying the dedicated material to the <sup>fi</sup>eld and driving to the location of the facility unit for renewed <sup>fi</sup>lling. The number of routes is given by:

$$
n = \frac {a \cdot A}{C}
$$

where, a is the application rate, A is the <sup>fi</sup>eld area, C is the tank capacity, and the symbol ⌈⌉ denotes the ceiling function in order to return an integer number of routes.

## 2.3.3. Allocation of tracks to routes

![](/api/attachments/8UF56Q2J/fulltext/images/c58cbc6ee967dc7ae91923e655ca0cfe9732ff39eb9107ecfb63f9973cf55dde.jpg)  
Fig. 4. The reference grid for two different operating widths.

In this stage, the tracks are assigned to the routes following the sorted permutation. The devised process involves that the permutation is divided into sequential sets equaling the number of routes (n). Then the <sup>fi</sup>rst n tracks of the <sup>fi</sup>rst set are assigned one by one to the <sup>fi</sup>rst track of each of the n routes, the n tracks of the second set are assigned one by one to the second track of each route, and so on. The output from the procedure is n permutations of <sup>fi</sup>eld-work tracks where the traversal of each permutation corresponds to a route of the vehicle (Fig. 5).

As mentioned, the resulting optimal traf<sup>fi</sup>c pattern consists of sequences of <sup>fi</sup>eld-work tracks that do not follow any predetermined standard motif, but in contrast, the track sequence is a result of an optimization under a minimization criterion. In that sense the resulted patterns belong to the family of B-patterns and will be denoted as $\mathsf { B _ { c o m } } ^ { * }$ -patterns in correspondence to $\mathrm { B _ { d i s } } ^ { * }$ -patterns which are the B-patterns resulting under the optimization criterion of minimizing the non-working travelled distance. Using the terminology adopted in auto-steering systems for agricultural vehicles, the conventional <sup>fi</sup>eld-work pattern will be symbolized as AB-pattern.

## 2.4. Measure of goodness

In order to compare the potential soil compaction risk as derived from the system route plan and a conventional standard route plan (e.g. AB-pattern), a measure of goodness (denoted “risk factor”) is introduced. The risk factor is derived from the following process based on the logic that the pass of a vehicle with high load should be avoided in areas corresponding to grid cells designated with high values of the risk indicator. Two threshold values between 0 and 1 are de<sup>fi</sup>ned, one for the normalized value of the risk indicator and one for the normalized value of the vehicle load. If the risk indicator in a cell is below the predetermined threshold value, then the risk factor for this cell equals zero, meaning that the cell can be subjected to both (low and high) vehicle loads. If the normalized value of the risk indicator in a cell is higher than the threshold value then two options occur; if the normalized value of the load is also lower than the corresponding load threshold value, then the risk factor equals zero; in the opposite case where the normalized value of the load is higher than its threshold value, the risk factor is the normalized value (in order to be expressed between 0 and 1) equaling the difference between the normalized load and the threshold in order to express the quantitative risk. The total value of the risk factor results from the mean value of the risk factors within its cell.

## 3. Case study

## 3.1. Experimental field

The case study is based on an experimental <sup>fi</sup>eld located at the Organic Research Station Rugballegaard, Horsens, Denmark [55.864067° N 9.800732° E] (Fig. 6a). The experimental <sup>fi</sup>eld has a total area of 145,000 m<sup>2</sup>. Based on 17 samples, the soil texture of the <sup>fi</sup>eld for the depths of 0–100 cm contained 2.1% soil organic matter (SOM), 17.7% clay (b2 μm), 14.7% silt (2–20 μm), 40% <sup>fi</sup>ne sand (20–200 μm) and 25.4% coarse sand (>200 μm). As it can be seen for the soil texture, the sand content is high. In comparison with a soil with high clay content and under the same moisture content conditions the former soil is less susceptible to soil compaction. Nevertheless, regardless of soil texture higher moisture content will imply higher risk for soil compaction. Furthermore, as described earlier, the system provides a relative measure for the risk for soil compaction which is translated to higher absolute risk in the case of higher moisture content.

As part of an already con<sup>fi</sup>gured experimental platform, the <sup>fi</sup>eld is divided in 739 plots of dimensions 9×1.5 m (Fig. 6b) [10]. The plots are placed in pairs where the distance between the two plots centre was 3 m. For each plot an $\mathrm { E C _ { a } }$ measurement located in the centre of the plot (c.f. to the next section) has been carried out recorded and was used as the potential risk indicator for the system.

![](/api/attachments/8UF56Q2J/fulltext/images/c13376f9bf9fcfc5f489c4ac53627b494c3cfc57d14634dba5e95e89590cf31b.jpg)  
Fig. 5. The process of allocation of tracks to routes.

For illustrating the effect of different risk indicator quanti<sup>fi</sup>cations on the resulting optimal routes, two sub-<sup>fi</sup>elds (referred to as “<sup>fi</sup>eld $\mathsf { A } ^ { \prime \prime }$ and “<sup>fi</sup>eld B”) with the same area were selected (Fig. 4b) and contained within the total experimental <sup>fi</sup>eld area. The area of each sub-<sup>fi</sup>eld was 46,656 m<sup>2</sup>.

a)  
![](/api/attachments/8UF56Q2J/fulltext/images/0ac3e58de0c7e89224b4d2afa71c6e982600117a954592896bbdab3d6419dbe6.jpg)

b)  
![](/api/attachments/8UF56Q2J/fulltext/images/3a4ceb9879e62c163732a691ce8c0c57a9ee034f24d55d84f10c8bc85279b575.jpg)  
Fig. 6. The experimental <sup>fi</sup>eld and the plot framing the measurements of the EM38 measurements.

## 3.2. Risk indicator measurements

In the presented case study, the soil compaction risk indicator for the planning system is the electromagnetic induction (EMI) measurements. EMI scanning is a rapid, non-invasive method for collecting soil apparent electrical conductivity $\left( \mathrm { E C _ { a } } \right)$ information, which in turn can provide information on soil moisture which is directly connected to the risk of the soil compaction. Soil moisture is considered to be the single most important edaphic factor among all others that in<sup>fl</sup>uence $\mathrm { E C _ { a } }$ determination [6]. Reedy and Scanlon [19] found that the $\mathrm { E C } _ { \mathrm { a } }$ could explain 80% and 99% of the moisture content variance when moisture contents were averaged vertically and spatially (i.e. across the surface of the soil volume), respectively, in all depths of the soil pro<sup>fi</sup>le.

The selection of the EMI as the risk indicator stems both from the proven correlation between the EMI value and the potential risk for compaction, as well as from the fact that $\mathrm { E C _ { a } }$ is among the most frequently used tools by farmers in precision agriculture measurements for the spatio-temporal characterization of edaphic and anthropogenic properties that in<sup>fl</sup>uence crop yield [8], since it can be determined relatively easily using appropriate measuring devices, such as the Geonics EM38 instrument (Geonics Limited, Canada).

![](/api/attachments/8UF56Q2J/fulltext/images/cdd24c3fb8b1c66e54f49d35dfb61f21a9b631e03836cc03ade7b9338e8f4188.jpg)  
Fig. 7. The iTecPRO interface

## 3.3. Navigation system

The navigation system that has been selected for the automated execution of the route plans generated by the planning system was the pro-module iTEC Pro® (Intelligent Total Equipment Control) (Deere & Company, Moline, Illinois) combined with the GreenStar<sup>TM</sup> 3 System (Deere & Company, Moline, Illinois) and installed on a 7730 John Deere tractor (Deere & Company, Moline, Illinois). The selection of this system was based on the available advanced capability of the iTEC Pro® of traversing irregular sequences of <sup>fi</sup>eld-work tracks (as the ones resulting from the planning system). Furthermore, iTEC Pro® is currently the only commercially available auto-steering system that can execute automated turnings between tracks in order to reach the planned subsequent one. Fig. 7 presents the interface during the execution of the plans.

![](/api/attachments/8UF56Q2J/fulltext/images/124e0644664adfffa65bd93e7b2236c7ce4fe514bda9bd9f4261a8092db0268a.jpg)

## 3.4. The operational characteristics

The operating width of the application unit was 9 m, resulting in 24 <sup>fi</sup>eld-work tracks on each one of the sub-<sup>fi</sup>elds. The tanker capacity was 25 m<sup>3</sup> of organic fertilizer, while the application rate was $0 . 0 0 1 6 \mathrm { m } ^ { 3 } / \mathrm { m } ^ { 2 }$ (volume of organic fertilizer per unit <sup>fi</sup>eld area). The combination of the total area of each sub-<sup>fi</sup>eld, the application rate, and the tanker capacity, resulted in three routes (or equivalently, in three loadings) required for the total area coverage. The working speed during execution was set in the navigation system to be 2 m/s.

## 3.5. Results from case study

The results on the conventional and optimal plans in combination with the risk indicator map of the <sup>fi</sup>eld and the resulting potential

![](/api/attachments/8UF56Q2J/fulltext/images/194be4f2d68d1a28d1f20ab13f50a2c303bcbc7c6627c145b2ea3c45aad0afec.jpg)

![](/api/attachments/8UF56Q2J/fulltext/images/868867e396976f687abff37f2b9a15058b5633995034b02e2fe6a06b51e8c2e9.jpg)

![](/api/attachments/8UF56Q2J/fulltext/images/738b01941ca72d1deeacc298dcde075e598edcff1a2c80632ba94c46ac396a75.jpg)

![](/api/attachments/8UF56Q2J/fulltext/images/bf526e13def8824b96dea83b6086d354bd4090384b723fe6c5ffbc5c1ad8b871.jpg)  
Fig. 8. Field A; the tanker load distribution on the <sup>fi</sup>eld area for the conventional (a) and optimal (b) patterns, the electrical conductivity map of the <sup>fi</sup>eld (c) and the distribution of the risk factor across the <sup>fi</sup>eld for the conventional (d) and optimal (e) patterns.

![](/api/attachments/8UF56Q2J/fulltext/images/786a352b272b9d3d48dd1df5a789fa7de83bebe7ccf9a7d05a0a122de860cb8e.jpg)

![](/api/attachments/8UF56Q2J/fulltext/images/175bdeee5a18080e65d40e9622eb604f2de0342b5e9a6e2caf428b787571682f.jpg)

Field B  
![](/api/attachments/8UF56Q2J/fulltext/images/1ce768a9b3ef6ef13ca529b2dc15ccfa06fab12a30267095feae998e00ddb442.jpg)  
Field B $1 B ^ { \prime } _ { c o m }$ -pattern

Field B / AB-pattern  
![](/api/attachments/8UF56Q2J/fulltext/images/6bc294edc2f7995ae39bb991112013081fddabe7e724b3814bbbc09f9ce028f6.jpg)

![](/api/attachments/8UF56Q2J/fulltext/images/9432b9b43007ef4415057f7e698ed88ea4b270e39a19bfbaa9e3c16f2044022e.jpg)  
Fig. 9. Field B; the tanker load distribution on the <sup>fi</sup>eld area for the conventional (a) and optimal (b) patterns, the electrical conductivity map of the <sup>fi</sup>eld (c) and the distribution of the risk factor across the <sup>fi</sup>eld for the conventional (d) and optimal (e) patterns.

risk are presented in Figs. 8 and 9 for the cases of <sup>fi</sup>eld A and <sup>fi</sup>eld B, respectively. Speci<sup>fi</sup>cally, Figs. 8a and 9a show the distribution of the volume of the remaining tanker load across the areas of <sup>fi</sup>elds A and <sup>fi</sup>eld B, respectively, as a result of the continued emptying of the tanker while the application unit is moving on the <sup>fi</sup>eld according to the conventional and optimal patterns. The conventional pattern involves a simpli<sup>fi</sup>ed track-by-track traversal sequence as can be seen for the equal and repeated load distribution for each route. In contrast, in the case of the optimal pattern, there is no uniform and repeated load distribution but instead different load distributions for each route. Both conventional and resulted optimal patterns are given in Table 1. Fig. 8c presents the risk indicator map for the <sup>fi</sup>eld area and comprising of the interpolation of the electrical conductivity measurements. Finally, Fig. 8d and e presents the distribution of the risk factor on the <sup>fi</sup>eld area as resulting from the conventional and optima patterns, respectively. The mean of the risk factor, as de<sup>fi</sup>ned above and representing the measure of goodness for a speci<sup>fi</sup>c <sup>fi</sup>eld-work pattern, is given in Table 1 for the all of the followed plans. Similarly, Fig. 9 presents the corresponding results for <sup>fi</sup>eld B.

The derived route plans and the associated risk factors.

<table><tr><td rowspan="2"></td><td colspan="2">Optimal (Bcom*)</td><td colspan="2">Conventional (AB)</td></tr><tr><td>Plan</td><td>Risk factor</td><td>Plan</td><td>Risk factor</td></tr><tr><td rowspan="3">Field A</td><td>R1=&lt;1 4 5 19 8 9 10 24&gt;</td><td rowspan="3">0.058</td><td>R1=&lt;1 2 3 ...&gt;</td><td rowspan="3">0.075</td></tr><tr><td>R2=&lt;2 7 17 18 14 15 12 22&gt;</td><td>R2=&lt;9 10 11 ...&gt;</td></tr><tr><td>R3=&lt;3 6 16 20 23 13 21 11&gt;</td><td>R3=&lt;17 18 19 ...&gt;</td></tr><tr><td rowspan="3">Field B</td><td>R1=&lt;11 16 17 6 18 14 19 1&gt;</td><td rowspan="3">0.011</td><td>R1=&lt;1 2 3 ...&gt;</td><td rowspan="3">0.028</td></tr><tr><td>R2=&lt;10 13 23 20 8 22 5 2&gt;</td><td>R2=&lt;9 10 11 ...&gt;</td></tr><tr><td>R3=&lt;24 12 9 21 7 15 4 3&gt;</td><td>R3=&lt;17 18 19 ...&gt;</td></tr></table>

Table 2  
Operational measures for different <sup>fi</sup>eld-work patterns.

<table><tr><td>Pattern</td><td>Non-working distance (m)</td><td>In-field operational time (s)</td><td>In-field productivity (m2/s)</td><td>Deviation from AB-pattern productivity</td></tr><tr><td>AB/fields A&amp;B</td><td>1468</td><td>11,285</td><td>4.13</td><td></td></tr><tr><td> $B_{dis}^{*}/fields$  A&amp;B)</td><td>1132</td><td>10,934</td><td>4.27</td><td>+3.2%</td></tr><tr><td> $B_{com}^{*}/field$  A</td><td>2024</td><td>11,492</td><td>4.06</td><td>-1.8%</td></tr><tr><td> $B_{com}^{*}/field$  B</td><td>2390</td><td>11,695</td><td>3.99</td><td>-3.5%</td></tr></table>

From the above described <sup>fi</sup>gures, it is clearly shown how the resulting optimal plans allocate high remaining tanker loads to areas with low risk indicator values $( \mathrm { E C _ { a } }$ in this case), in contrast to the conventional plans which ignore any soil compaction risk indications. As a result the risk factor is reduced 23% and 61% for <sup>fi</sup>eld A and <sup>fi</sup>eld B, respectively, by using the corresponding optimal route plans instead of the non-optimal conventional ones.

As it can be seen from the resulting track sequences for the individual routes in the case of the optimal patterns (Table 1), the application unit has to execute extended turnings in order to traverse these sequences. For example, in <sup>fi</sup>eld A in the <sup>fi</sup>rst route the application has to travel from track 5 to track 19. The distance between the two tracks equals to 14 times the working width, which is 126 m. In the case of the conventional pattern the distance between any two sequential tracks equals 9 m (a single working width). The result of this is that the optimal patterns, in terms of minimized soil compaction, compromise the non-productive time allocated to turnings and consequently, the operation's productivity is reduced.

Table 2 presents the non-working travelled distances, the total in-<sup>fi</sup>eld operational time (with the re-loading time excluded), and the in-<sup>fi</sup>eld productivity for all of the followed patterns in both <sup>fi</sup>elds, as well as the perceptual change in the productivity compared to the conventional patterns. For comparison purposes, the corresponding results for the case of the optimal patterns in terms of minimized non-working distances are also presented. The traversal sequence of tracks for this case was the same for the two <sup>fi</sup>elds, since their dimensions and the application unit characteristics (operating width and turning radius) are equal, and was as follows: ${ B _ { d i s } } ^ { * }$ -pattern: $\mathrm { R } 1 = < 1$ $3 5 7 8 6 4 2 >$ , R2=b9 11 13 15 16 14 12 10>, R3=b17 19 21 23 24 22 20 18>.

The results of the optimizing under the criterion of the nonworking distance show that productivity was increased by 3.2%, while the corresponding optimization under the criterion of minimizing soil compaction risk show that productivity was reduced by 1.8% and 3.5%, respectively for <sup>fi</sup>elds A and B.

## 4. System con<sup>fi</sup>gurations

In the presented case study, the driving direction as related to the geometry of the <sup>fi</sup>eld was pre-determined and was given as an input to the system. Nevertheless, different alternative and potential driving directions could be allowed in normal farming practices depending on the layout of the <sup>fi</sup>eld (geometry, topography, operations history, etc.). Such user preferences can be easily handled by the system providing potentially even improved solutions in terms of soil compaction risk. In the case of <sup>fi</sup>eld B, for example, selecting the perpendicular driving direction to the initial one (Fig. 10) will have implications in terms of reducing the risk factor from 0.058 to 0.042. The model gives the potential for evaluating the optimal patterns for all possible driving directions in the range from 0° to 360°.

As it has been shown, a sole consideration of the soil compaction implications can have a negative effect on other operational parameters. One such other parameter is the operations productivity which in the case of minimized soil compaction risk is reduced due to the increased in-<sup>fi</sup>eld non-working travelled distance during turnings. This indicates that a multiple-objective criteria optimization should be pursued. However, such a multi-criteria approach requires that the individual factors can be expressed in a comparable way. Although the non-working distance can be easily translated into cost stemming from increased fuel, time, etc., there is currently no an explicit connection between the degree of the soil compaction and the incurred cost, in terms of reduced yield as well as the cost for the amelioration of the soil compaction.

Field B / $\boldsymbol { \mathsf { B } } _ { \mathrm { r m m } } ^ { \bullet }$ -pattern /alternative driving direction  
![](/api/attachments/8UF56Q2J/fulltext/images/16140c565b6efd29bca4cc13b953946b834ace639d0f6a4ec4e4fea94d5edb60.jpg)

Field B  
![](/api/attachments/8UF56Q2J/fulltext/images/90a7cf9df4b05c10de34bd15c950ee240dc1b82622450bd662948d2ee2cdd9c5.jpg)

![](/api/attachments/8UF56Q2J/fulltext/images/b5426533c4152b8c460799ddac575ef5522cc079a61c8000bfcd1b3263dc7e79.jpg)  
Fig. 10. Field B; The altered driving direction (a), the electrical conductivity map (b) and the initial driving direction (c) (b and c are presented in Fig. 8 and are reproduced here for comparison reasons).

Nevertheless, simple heuristics can improve the solution in terms of reduced non-working travelling distance while keeping the compaction risk at the same level. As for example, applying simple “swap” heuristic operations in the initial solution in the case of <sup>fi</sup>eld

<table><tr><td>Route 1= &lt; 11</td><td>16</td><td>17</td><td>6</td><td>18</td><td>14</td><td>19</td><td>1&gt;</td></tr><tr><td>Route 2= &lt; 10</td><td>13</td><td>23</td><td>20</td><td>8</td><td>22</td><td>5</td><td>2&gt;</td></tr><tr><td>Route 3= &lt; 24</td><td>12</td><td>9</td><td>21</td><td>7</td><td>15</td><td>4</td><td>3&gt;</td></tr></table>

Fig. 11. Two “swap” operations between the routes of the initial solution for <sup>fi</sup>eld B.

B, as depicted in Fig. 11 (i.e., interchanging track 6 of route 1 with track 21 of route 3, and track 14 of route 1 with track 22 of route 2), the non-working distance (2390 m — Table 2) is reduced by 22% (1867 m in the improved solution) leading to an increase in the productivity even exceeding the productivity of the conventional AB pattern. At the same time, the risk factor is maintained at the same level since the involved interchanging tracks in each “swap” operation have comparable risk indicator levels.

As it was mentioned in the System description section, the development of the system was targeted toward input material <sup>fl</sup>ow <sup>fi</sup>eld operations where a speci<sup>fi</sup>c quantity of a material is transported by the agricultural vehicle and distributed in the <sup>fi</sup>eld area. The case of the output material <sup>fl</sup>ow operations, such as grain or forage harvesting, can also be analyzed in a similar way where the course of the volume of the remaining load is reversed. In the case of the input material <sup>fl</sup>ow operations and counting form the beginning of a route, the load at a given time expressed as part of the initial load is progressively reduced from 100% to 0%, while in the case of the material output operations the load at a given time is progressively increased from 0% to 100%. The main difference between these two cases, is that planning for input material <sup>fl</sup>ow is deterministic, while planning for output material <sup>fl</sup>ow is stochastic. The stochasticy in the latter case is caused by the uncertainty of the realized yield which implies that the load distribution cannot be predicted with certainty but can only rely on an expected probability derived from historical yield data. This will put increased demand on the planning system in terms of on-line monitoring and continuously up-dating and revising of the plans based on the latest yield information. However, that fact that such on-line monitoring sensor systems are currently being developed [20,21] and combined with the fact that the signi<sup>fi</sup>cantly low computational time requirements of the presented algorithmic approach (in the level of ms) allow for its implementation within a real-time system, make it feasible, in principle, to expand the proposed system to the case of the output material <sup>fl</sup>ow operations, and this constitutes a target of future experimental research.

## 5. Conclusions

A decision support system for the route planning for agricultural vehicles carrying time-depended loads with the objective to reduce the risk of soil compaction has been developed. The system has been demonstrated and tested for the case of material input operations, and speci<sup>fi</sup>cally for heavy application units used for organic fertilizer. It has been proved that the hypothesis that an area to be worked which is more sensitive to compaction should be worked with a corresponding low vehicle load and this principle forms the engine for producing optimal routes in terms of minimized risk for soil compaction. According to the results from the system implementation in two experimental <sup>fi</sup>elds the risk factor was reduced by 23% and 61%, respectively, by using the corresponding optimal plans instead of the non-optimal conventional ones that an operator would follow.

The implementation of the system requires feasible technologies providing information on the soil sensitivity to compaction, as well as navigation means for the actual execution of the resulting optimal routes. Regarding the former, the electrical conductivity map of the <sup>fi</sup>eld in the presented case study was used as indicator it is among the most frequently used tools by farmers in precision agriculture applications. However, any other means of measuring soil sensitivity already existed or developed in the future can be implemented. Regarding the latter, the presented system is fully operational using existing state-of-the-art auto-steering and navigation-aiding systems available on modern agricultural vehicles.

The system can be extended to include multi-criteria optimization aspects, such as minimized non-working travelled in-<sup>fi</sup>eld distance, as well as optimal routes in terms of both track sequence traversal and driving direction. Finally, the low computational time requirements of the underlying algorithmic approach allow for the implementation of the system as a real-time decision support system integrating the uncertainty inherent in output material <sup>fl</sup>ow operations, such as harvesting.

## Acknowledgments

The authors would like to thank Deere & Company, Moline Technology Innovation Center, One John Deere Place, Moline, USA for providing supplemental equipment used as part of the machine advanced navigation and guidance in the project.

## References

[1] L. Alakukku, P. Weisskopf, W.C.T. Chamen, F.G.J. Tijink, J.P. van der Linden, S. Pires, G. Spoor, Prevention strategies for <sup>fi</sup>eld traf<sup>fi</sup>c-induced subsoil compaction: a review Part 1. Machine/soil interaction, Soil and Tillage Research 73 (2003) 145–160.

[2] D.D. Bochtis, Planning and control of a <sup>fl</sup>eet of agricultural machines for optimal management of <sup>fi</sup>eld operations, Ph.D. Thesis. Aristotle University, Greece, 2008.

[3] D.D. Bochtis, C.G. Sørensen, The vehicle routing problem in <sup>fi</sup>eld logistics part I, Biosystems Engineering 104 (2009) 447–457.

[4] D.D. Bochtis, S.G. Vougioukas, Minimising the nonworking distance travelled by machines operating in a headland <sup>fi</sup>eld pattern, Biosystems Engineering 101 (2008) 1–12.

[5] D.D. Bochtis, S.G. Vougioukas, H.W. Griepentrog, A mission planner for an autonomous tractor, T, ASABE 52 (2009) 1429–1440.

[6] E. Brevik, T. Fenton, A. Lazari, Soil electrical conductivity as a function of soil water content and implications for soil mapping, Precision Agriculture 7 (2006) 393–404.

[7] T. Chamen, L. Alakukku, S. Pires, C. Sommer, G. Spoor, F. Tijink, P. Weisskopf, Prevention strategies for field traffic-induced subsoil compaction: a review: Part 2. Equipment and <sup>fi</sup>eld practices, Soil and Tillage Research 73 (2003) 161–174.

[8] D.L. Corwin, S.M. Lesch, Apparent soil electrical conductivity measurements in ag riculture, Computers and Electronics in Agriculture 46 (2005) 11–43

[9] S. de Bruin, P. Lerink, A. Klompe, T. van der Wal, S. Heijting, Spatial optimisation of cropped swaths and <sup>fi</sup>eld margins using GIS, Computers and Electronics in Agriculture 68 (2009) 185–190.

[10] O. Green, M. Lamande, P. Schjønning, C.G. Sørensen, D.D. Bochtis, Reducing the risk of soil compaction by applying ‘Jordværn Online’® when performing slurry distribution, Acta Agriculturae Scandinavica Section B-Soil and Plant Science 61 (2011) 209–213.

[11] I.A. Hameed, D.D. Bochtis, C.G. Sørensen, M. Nøremark, Automated generation of guidance lines for operational <sup>fi</sup>eld planning, Biosystems Engineering 107 (2010) 294–306.

[12] M.A. Hamza, W.K. Anderson, Soil compaction in cropping systems, a review of the nature, causes and possible solutions, Soil and Tillage Research 82 (2005) 121–145.

[13] J.W. Hofstee, L.E.E.M. Spatjens, H. Ijken, Optimal path planning for <sup>fi</sup>eld operations, in: E.J. Van Henten, D. Goense, C. Lokhorst (Eds.), Proc. Joint International Agricultural Conference, JIAC 2009, Precision Agriculture 09, Wageningen, Netherlands, 2009, pp. 521–529.

[14] T. Keller, P. Defossez, P. Weisskopf, J. Arvidsson, G. Richard, SoilFlex: A model for prediction of soil stresses and soil compaction due to agricultural <sup>fi</sup>eld traf<sup>fi</sup>c including a synthesis of analytical approaches, Soil and Tillage Research 93 (2007) 391–411.

[15] M. Lamandé, P. Schjønning, The ability of agricultural tyres to distribute the wheel load at the soil–tyre interface, Journal of Terramechanics 45 (2008) 109–120.

[16] D. Mackrell, D. Kerr, L. von Hellens, A qualitative case study of the adoption and use of an agricultural decision support system in the Australian cotton industry: the socio-technical view, Decision Support Systems 47 (2009) 143–153.

[17] T. Oksanen, A. Visala, Coverage path planning algorithms for agricultural <sup>fi</sup>eld machines Journal of Field Robotics 26 (2009) 651–668

[18] B. Recio, F. Rubio, J.A. Criado, A decision support system for farm planning using AgriSupport II, Decision Support Systems 36 (2003) 189–203.

[19] R.C. Reedy, B.R. Scanlon, Soil water content monitoring using electromagnetic induction, Journal of Geotechnical and Geoenvironmental 129 (2011) 1028–1039.

[20] C.G. Sørensen, L. Pesonen, S. Fountas, P. Suomi, D. Bochtis, P. Bildsøe, S.M. Pedersen, A user-centric approach for information modelling in arable farming, Computers and Electronics in Agriculture 73 (2010) 44-55

[21] N. Wang, N. Zhang, M. Wang, Wireless sensors in agriculture and food industry — recent development and future perspective, Computers and Electronics in Agri culture 50 (2006) 1–14.

[22] P. Weisskopf, R. Reiser, J. Rek, H.R. Oberholzer, Effect of different compaction impacts and varying subsequent management practices on soil structure, air regime and microbiological parameters, Soil and Tillage Research 111 (2010) 65–74.

Dionysis D. Bochtis is an Associate Professor in the Engineering Department of the Faculty of Science and Technology at Aarhus University, Denmark. He holds a Ph.D. in Fleet management in bio-production systems, a M.Sc. in Automation Control, and a B.Sc. in Exact Sciences (Physics). His primary research is industrial engineering focused on bio-production and related provision systems including activities related to <sup>fl</sup>eet management (for conventional and autonomous <sup>fi</sup>eld machinery), <sup>fi</sup>eld robots (high level control aspects: mission planning, path planning, task allocation), supply chain management for bio-energy bio-recourses, <sup>fi</sup>eld logistics (scheduling, area coverage planning, routing), automation, and Decision Support Systems. He is the author of more than 120 articles in peer reviewed Journals and conference proceedings.

Claus G. Sørensen is an Associate Professor in the Engineering Department of the Faculty of Science and Technology at Aarhus University, Denmark, and he holds a

Ph.D. in Production and Operations Management. He has 20 year experience in production and operations management, information modelling in terms of decision processes, type of information, system analysis, and simulation and modelling of technology use in agriculture. Research topics have included resource analyses and optimisations, integration of technical management evaluations for whole farm analyses and optimisations, the feasibility of introducing robotic systems in agriculture and the development of management information systems. He is the chairman in Section V (systems management) of CIGR (international commission of agricultural and biosystems engineering) and author or co-author of more than 300 articles in peer reviewed Journals conference proceedings, and scienti<sup>fi</sup>c reports.

Ole Green is an Associate Professor in the Engineering Department of the Faculty of Science and Technology at Aarhus University, Denmark. He holds a Ph.D. in Sensors Technology and a M.Sc. in agricultural engineering. He run the company Green Agro from 2004 to 2008, from 2004 to 2006 he was employed at Danish Agricultural Advisory Service and from 2006 at Aarhus University. He is the author of more than 100 articles in peer reviewed Journals and conference proceedings, and 5 patent applications. His research is focused on developing, analyzing, and evaluating new technological solutions in biological environment.
