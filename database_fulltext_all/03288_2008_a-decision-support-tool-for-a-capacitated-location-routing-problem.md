---
otero_id: 3288
otero_key: "SGYG2EEE"
title: "A decision-support tool for a capacitated location-routing problem"
authors: "Rui Borges Lopes; Sérgio Barreto; Carlos Ferreira; Beatriz Sousa Santos"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.07.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision-support tool for a capacitated location-routing problem

Rui Borges Lopes <sup>a,</sup>⁎, Sérgio Barreto <sup>b</sup>, Carlos Ferreira <sup>a</sup>, Beatriz Sousa Santos <sup>c</sup>

<sup>a</sup> Department of Economics, Management and Industrial Engineering/CIO, University of Aveiro, Campus Universitário de Santiago, 3810-193 Aveiro, Portugal

<sup>b</sup> ISCA-Higher Institute of Accounting and Administration/CIO, University of Aveiro, R. Associação Humanitária dos Bombeiros de Aveiro, 3811-902 Aveiro, Portugal

<sup>c</sup> Department of Electronics, Telecommunications and Informatics/IEETA, University of Aveiro, Campus Universitário de Santiago, 3810-193 Aveiro, Portugal

## a r t i c l e i n f o

Article history: Received 16 November 2007 Received in revised form 12 June 2008 Accepted 9 July 2008 Available online 18 July 2008

Keywords: Decision-support too Location-routing Web map servers

## a b s t r a c t

In this paper we present a decision-support tool (DST) that implements a capacitated location-routing problem (CLRP) with two levels (depots and customers) and a capacitated and homogeneous vehicle <sup>fl</sup>eet. It allows the exploration of the solution <sup>fi</sup>nding process in a way easily understandable by the user, and enables access to online geographic data through web map servers (WMS). This tool was developed for Windows platforms having an architecture that easily allows the integration of new functionality.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Location and routing have been some of the major concerns in logistics, having implications on the complete supply chain [7]. It is generally accepted that the success of many enterprises may depend on the location-distribution decisions [3,11] and that, nowadays, many managers tend to support their decisions on acquired experience [10]. This attitude may be caused by both the overall complexity of the problem and the speci<sup>fi</sup>cities of different cases [22,25]. The development of an effective tool to support this kind of decisions is similarly complex due to the same reasons. Moreover, in the case of a tool to support decisions for location-routing problems (LRP), there are other key aspects beyond optimization issues; one such aspect is the presentation of the solution and the exploration of the process in a way easily understandable by the decision-maker, allowing better judgments.

One can <sup>fi</sup>nd in the literature a signi<sup>fi</sup>cant number of contributions concerning LRPs [16,22,25], as well as contributions regarding decisionsupport systems (DSS) [2,13,14,28]. On the other hand there is a lack of studies involving both areas.

For that reason, an integrated approach to location and routing, and an application that can support the decision, may represent an important competitive advantage. With this paper we will try to help <sup>fi</sup>lling that gap, presenting a decision tool for a LRP integrating the essential features of this type of problem.

## 2. A capacitated location-routing problem (CLRP)

The location-routing problem (LRP) appears as a combination of two (dif<sup>fi</sup>cult) problems: the facility location problem (FLP) and the vehicle routing problem (VRP); both of them can be shown to be NPhard. Moreover, the multiplicity of characteristics of those models also leads to a wide diversity of LRPs [22,25].

The LRP is a better model in contexts involving the simultaneous location of facilities and the design of distribution routes between the facilities and the users, given that solving separately these two aspects will most likely produce a suboptimal solution [27].

In this paper we consider a discrete capacitated location-routing problem (CLRP) with two layers (depots and customers) and a capacitated and homogeneous vehicle <sup>fl</sup>eet. Each customer has a certain demand and the potential facilities (depots) have a certain capacity; the location cost of each depot is known, as well as the unitary cost of distribution (function of covered distance). Euclidean distances are considered.

The model seeks to determine which depots must be opened (established) and to draw the distribution routes from these depots to the customers (vehicles start and end their routes at the same depot) minimizing the total cost (location and distribution costs) [6].

While the multiplicity of real cases and the integration of their characteristics in LRP models lead to a great diversity of problems [22,25], the above described CLRP integrates the essential LRP features and considers appropriate constraints to guarantee routes and depots with balanced capacity.

## 3. Solving the capacitated location-routing problem

The capacitated location-routing problem (CLRP) is NP-hard; thus, most practical (large dimension) problems call for heuristic algorithms in order to obtain “good solutions” in reasonable time [1,17];

![](/api/attachments/SGYG2EEE/fulltext/images/720318b42f1247c8ca05b7344e81db30102f71423ccf73195152fb45e6e38345.jpg)  
Fig. 1. Input and output data concerning each phase of the sequential heuristic for the CLRP.

moreover, heuristic algorithms are (usually) easy to understand, modify and implement, providing several solutions allowing the user the <sup>fl</sup>exibility to choose the preferred one.

Heuristic methods for LRPs included sequential [23], iterative [26] and hierarchical [24] approaches. Recently, metaheuristics such as tabu search, simulated annealing and genetic algorithms were proposed [19,30]. Due to the characteristics of our model (vehicles with small capacity and signi<sup>fi</sup>cant <sup>fi</sup>xed costs for the facilities), we used a sequential method as it has some advantages from a computational point of view [21,29]. More precisely we used a sequential distribution-<sup>fi</sup>rst location-second heuristic [5], consisting of four main steps: (i) construct groups of customers with a capacity limit; (ii) determine the distribution in each customer group; (iii) improve the routes and (iv) locate the depots and assign the routes to them. Fig. 1 illustrates the schema of the heuristic and some details of the steps are presented in this section.

This heuristic has been submitted to several computational tests with promising results, validating its use in a DSS (Fig. 2). The interested reader is referred to the work of [5] for a complete presentation and evaluation of this heuristic. The instances presented in Fig. 2 are available from [4].

## 3.1. Cluster analysis

Several authors have integrated cluster analysis procedures in heuristics for LRPs [9,21]. A detailed description of the clustering phase used in this heuristic can be found in [6].

The <sup>fi</sup>rst step of the heuristic groups clients based on the capacity of the used vehicles. For this purpose, twenty different possibilities are used, combining four clustering methods (two hierarchical and two non-hierarchical) with six proximity measures (single linkage or nearest neighbour, complete linkage or farthest neighbour, group average, centroid, ward and saving) [15].

## 3.2. Travelling salesman problem

After the de<sup>fi</sup>nition of the different groups of clients, an optimal distribution route for each cluster is determined, solving a travelling salesman problem (TSP). The method is based on the relaxation of the sub-routes constraints, in a two-index integer linear programming

<table><tr><td colspan="2">Instance</td><td>Vehicle Capacity</td><td>CLRP Cost (Lower Bound)</td><td>CLRP Cost (Upper Bound)</td><td>GAP (%)</td></tr><tr><td>1</td><td>Gaskell67-21x5</td><td>6000</td><td>424.9</td><td>435.9</td><td>2.59</td></tr><tr><td>2</td><td>Gaskell67-22x5</td><td>4500</td><td>585.1</td><td>591.5</td><td>1.09</td></tr><tr><td>3</td><td>Gaskell67-29x5</td><td>4500</td><td>512.1</td><td>512.1</td><td>0.00</td></tr><tr><td>4</td><td>Gaskell67-32x5</td><td>8000</td><td>556.5</td><td>571.7</td><td>2.73</td></tr><tr><td>5</td><td>Gaskell67-32x5</td><td>11000</td><td>504.3</td><td>511.4</td><td>1.41</td></tr><tr><td>6</td><td>Gaskell67-36x5</td><td>250</td><td>460.4</td><td>470.7</td><td>2.24</td></tr><tr><td>7</td><td>Christofides69-50x5</td><td>160</td><td>549.4</td><td>582.7</td><td>6.06</td></tr><tr><td>8</td><td>Christofides69-75x10</td><td>140</td><td>744.7</td><td>886.3</td><td>19.01</td></tr><tr><td>9</td><td>Christofides69-100x10</td><td>200</td><td>788.6</td><td>889.4</td><td>12.78</td></tr><tr><td>10</td><td>Or76-117x14</td><td>150</td><td>12048.4</td><td>12474.2</td><td>3.53</td></tr><tr><td>11</td><td>Perl83-12x2</td><td>140</td><td>204.0</td><td>204.0</td><td>0.00</td></tr><tr><td>12</td><td>Perl83-55x15</td><td>120</td><td>1074.8</td><td>1136.2</td><td>5.71</td></tr><tr><td>13</td><td>Perl83-85x7</td><td>160</td><td>1568.1</td><td>1656.9</td><td>5.66</td></tr><tr><td>14</td><td>Perl83-318x4</td><td>25000</td><td>---</td><td>580680.2</td><td>---</td></tr><tr><td>15</td><td>Perl83-318x4</td><td>8000</td><td>---</td><td>747619.0</td><td>---</td></tr><tr><td>16</td><td>Min92-27x5</td><td>2500</td><td>3062.0</td><td>3062.0</td><td>0.00</td></tr><tr><td>17</td><td>Min92-134x8</td><td>850</td><td>---</td><td>6238.0</td><td>---</td></tr><tr><td>18</td><td>Daskin95-88x8</td><td>9000000</td><td>356.4</td><td>384.9</td><td>8.00</td></tr><tr><td>19</td><td>Daskin95-150x10</td><td>8000000</td><td>43938.6</td><td>46642.7</td><td>6.15</td></tr><tr><td rowspan="2"></td><td colspan="3">- Optimal solution</td><td>Average</td><td>4.81</td></tr><tr><td colspan="3">- Could not be found</td><td>Median</td><td>3.13</td></tr></table>

Fig. 2. Some instances and corresponding results of the sequential heuristic for the CLRP.

TSP formulation, whenever the group has 40 customers or less. The obtained integer problem is solved using the CPLEX<sup>®</sup> software package. Whenever sub-routes are detected, adequate constraints are introduced and the iterative process continues until the determination of the TSP optimal solution. If the group integrates more than 40 customers, a two-step heuristic is used for solving the TSP. In the <sup>fi</sup>rst step, a feasible TSP route is obtained using the farthesttype neighbourhood criteria, to choose the next client to be included in the route, and saving criteria, to determine where to include it. In the second step, the feasible TSP solution is improved through a 3- optimal local search procedure.

## 3.3. Improvement of client routes

This step provides an improvement of the routes found so far, using a 3-optimal local search as the one proposed by [8] for the Hamiltonian p-median problem. Besides providing a decrease of the routes cost, this step contributes to the elimination of the disagreeable biased effect, which emerges when the capacitated groups are formed. This phase provides the <sup>fi</sup>nal routes, their capacity and the distance covered by them.

## 3.4. Capacitated location-allocation problem

In the last step of the heuristic a capacitated location-allocation problem (CLAP) is solved. In this problem the heuristic allocates the routes to the depots (if it is advisable to install the depot). The routes are collapsed into a single client with an associated cost of allocation (to each depot) obtained by a saving function. The resulting single source CLAP is solved exactly using the CPLEX<sup>®</sup> software package.

## 4. A decision-support tool for the CLRP

A very important issue of this tool is the target audience; we do not expect users (decision-makers) to have any background on modelling and optimization aspects concerning LRPs. Thus, the information provided to users is neither technical data regarding the heuristic nor its validation; we focused instead on providing a usable interface. To implement the application, we used an object-oriented (OO) methodology (uni<sup>fi</sup>ed modelling language—UML) and Visual Basic<sup>®</sup>, version 6.0.

The developed application is organized around a main window, with all the functionalities accessible in this window, through the toolbar, or the menu (in a way easily understandable by users). In this context, the target user of this application is typically a decisionmaker, with higher education and moderate computer literacy, but having much experience in the subject (professional experience in real installations of depots and designing logistic systems) and that will use the tool infrequently. This user pro<sup>fi</sup>le suggests that the main usability goal should be ease of learning; therefore, the user interface should be extremely intuitive. The pro<sup>fi</sup>le of the end-users, as well as the task they intend to perform using this DST, and the usability principles (e.g. consistency, compatibility, familiarity, feedback, robustness, etc.) [12] were taken into consideration during the design of the tool.

The tool offers the following possibilities:

• Input (or edit) new (or existing) data in order to de<sup>fi</sup>ne the problem;

• Obtain solutions for the CLRP;

• Visualize the results either through numeric or graphical representation;

• Export the data to other applications;

• Export the graphical solution.

The developed tool incorporates two main parts: the solution algorithms (previously presented) and the graphical user interface (GUI). It was implemented for Windows platforms and has an open architecture which allows an easy integration of new functionality.

The DST can also incorporate any other solution method for the CLRP that uses commercial software, due to its integration with the CPLEX<sup>®</sup> which allows solving the provided formulation.

![](/api/attachments/SGYG2EEE/fulltext/images/c8f0d212c09b1a1ae7caddd996ba02a49d01bc71ca5b0f6f4402755f64754b75.jpg)  
Fig. 3. The GUI and the four different visualization areas.

![](/api/attachments/SGYG2EEE/fulltext/images/f7ee16447081e2fd351cf95bc5d825db62827c6f5340ae3b8f563c612c04ad2d.jpg)  
Fig. 4. Clients data with the Import and Export options.

## 4.1. Graphical user interface (GUI)

The main purpose of the GUI was to allow an easy and ef<sup>fi</sup>cient access to solutions for the CLRP. Thus, according to [18], the following characteristics are fundamental:

• Easy to learn: allowing the intuitive use of the tool by any user;

• Robustness: allowing the user to recover from unintended situations;

• Interactivity: allowing the information to effectively <sup>fl</sup>ow between the user and the system;

• Based on events: allowing the user to always be aware of the tasks he is performing.

The GUI comprises four distinct sections as shown in Fig. 3:

• A toolbar with buttons allowing a quick access to the functionalities (Area A);

• An alphanumerical component to display all the information regarding the problem (clients and depots data, vehicle capacity) (Area B);

• A visualization area displaying the information regarding the maps (Area C);

• A status bar showing the used hierarchic method and proximity measure (clustering phase), an icon indicating if the location of the objects in the map is provided by the application (Yes: ; No: ) and if the obtained solution is exact or approximate (Area D).

Regarding the toolbar, there is a set of buttons corresponding to different functionalities, besides the standard ones (New, Open, Save, Print, etc.):

A Language: allows changing the language of the tool (currently supports English, Portuguese and Spanish);

Import Map: allows importing an image to the map (bmp, jpg or gif format <sup>fi</sup>les);

Import Client/Depot Picture: allows importing an image (standard format: ico, bmp, jpg, etc.) to represent the client/depot;

Client/Depot/Route Colour: allows modifying the client/depot/ route icons colour in order to easily highlight the objects and identify the different routes on the map;

Display Labels/Pictures: allows activating or deactivating the visualization of icons corresponding to clients and depots;

View Demand: allows visualizing the clients based on their demand; Recalculate Scale: allows recalculating scale, hence adjusting the objects to the visualization area;

Zoom In: allows zooming in on a speci<sup>fi</sup>c area of the map. The interaction with web map servers (WMS) provides new imagery and detailed data of the selected region;

Move Map: allows moving the map inside the visualization area. Through this option it is possible to adjust the map image to the remaining objects;

Lock Relation: allows maintaining the relation between the map and the objects. This enables the use of different visualization scales for the map and the objects;

Hide Map: allows hiding the image inserted in the map area, allowing a better view of the objects;

Import Solution: allows importing a solution <sup>fi</sup>le obtained with other software;

Save Map: allows saving to an image <sup>fi</sup>le all the data in the map area (map, clients, depots and routes).

Most of these options are also available through the main menu, allowing a greater <sup>fl</sup>exibility to the user.

## 4.2. Information flow

In this section the information <sup>fl</sup>ow of the proposed DST will be presented. Firstly, the data input options, needed to insert the necessary information for characterizing and solving the problem, are presented.

After the data input it is possible to obtain online geographic data from the web map servers (WMS). It is also possible to proceed to a set of changes, from a graphical point of view, namely associating maps and images, changing the visualization scale, etc., thus making the interpretation of the information easier. Further on, users can choose several ways to run the algorithm, enabling them to visualize and analyse the obtained solution. Finally, users may export the obtained solution as well as the inserted data.

The following subsections describe in more detail how to work with the proposed DST, as well as its main functionalities.

![](/api/attachments/SGYG2EEE/fulltext/images/e33f75929abaf900d80c4aa6ab67b4a0bdd0a273ddec7a13d2db7263cbd17391.jpg)  
Fig. 5. Graphical data input (directly into the map area).

![](/api/attachments/SGYG2EEE/fulltext/images/77681663b8a78b24ccd01c5a83e834af54301ecf94dcf42b233d47f6437a0945.jpg)  
Fig. 6. Currently featured server integration (Demis® and Google Maps®)

## 4.2.1. Data input

The information needed to obtain the solution using the tool is the following:

• Clients location;

• Demand associated with each client;

• Possible locations for the depots;

• Capacity associated with each depot;

• Vehicles capacity.

Our tool allows the required data to be inserted either globally or one client or depot at a time. In order to insert the data globally, there is an Open <sup>fi</sup>le option (allowing the user to recover all data regarding a problem previously saved) as well as an Import data option (allowing to import several clients and depots, even if they where originally inserted in other applications). Through this set of options the user can quickly import a large quantity of data. The input (or update) of new (or existing) data individually can be done either numerically (as shown in Fig. 4) or graphically (directly on the map).

![](/api/attachments/SGYG2EEE/fulltext/images/c68629e0217c43baa716e42a4b562b7758ad6a557df97eb0512d8d4bfcf71678.jpg)  
Fig. 7. Objects graphical representation according to their position on the map.

The option to insert the data directly on the map area makes easier the identi<sup>fi</sup>cation of the location on the map (X and Y coordinates) where the user intends to insert the client and/or depot (Fig. 5). In order to edit the inserted data it is possible to drag the clients and/or depots across the map area (allowing the corresponding update of its coordinates).

Finally, the capacity of the <sup>fl</sup>eet is inserted, thus fully characterizing the capacitated location-routing problem (CLRP).

## 4.2.2. Web map server integration

The OpenGIS web map server (WMS) protocol de<sup>fi</sup>nes an interface for web based mapping applications; it is based on a query syntax for posting a request for the desired layers and zoom window to the server, which returns a map as a standard picture.

Our decision-support tool enables the user to obtain real online geographic information using WMS. Currently, the application supports the integration with the following servers (Fig. 6):

• Demis<sup>®</sup>;

• Google Maps<sup>®</sup>.

When these options are enabled the user can zoom in on any point of the world map, thus obtaining real online geographic information on the selected area. All the options regarding the layers of both servers are fully integrated in the application.

Demis<sup>®</sup> is an online server that complies with the OpenGIS WMS protocol.

Google Maps<sup>®</sup> is an online server that provides the same satellite imagery than Google Earth<sup>®</sup>, although using a different projection.

## 4.2.3. Graphical representation

Most of the graphical representation functionalities are concerned with the map and its interaction with the remaining objects (clients, depots and routes). In the map area there is a set of options that allow the introduction, editing and visualization of the inserted data.

In order to ensure that the objects (clients and depots) and associated information are always visible, different icons were used according to the objects location on the map and the distance to the border (Fig. 7) [20].

There are different ways to de<sup>fi</sup>ne the map scale, and the user has the possibility to change the representation scale. The application allows the user to zoom in or out (by increasing or decreasing the representation scale) on a speci<sup>fi</sup>c area of the map, in order to have a better view of the data in that area (Fig. 8). There is also the possibility to lock the relation between both representation scales (map and objects); moreover, combined with the “Move map” option, allows the user to easily adjust the map to the remaining objects (clients and depots).

When working with the WMS the zoom option provides new imagery and geographic data regarding the selected area.

It is also possible to visualize the map based on the clients demand. A circle where the radius represents the demand is drawn (clients with higher demand values correspond to circles with bigger radius). Through this option the user can easily identify clients with higher demand values, thus providing a useful view of the map (Fig. 9).

Finally, regarding the routes, they are displayed when the user obtains or imports the solution. When one of these options is used, the application draws a line connecting the clients to the depots (or to other clients). A different colour is associated to each route, allowing a better identi<sup>fi</sup>cation of the solution proposed.

Information regarding the used grouping method can be visualized in the status bar; there is also an indication about the solution: optimal or approximate.

## 4.2.4. Visualization of the solution

In order to obtain the solution, the user can choose one of the following options:

• Import the solution <sup>fi</sup>le;

• Run the algorithm, choosing a speci<sup>fi</sup>c grouping method;

• Run the algorithm for all the grouping methods;

• Run the algorithm step-by-step.

By allowing to import a solution <sup>fi</sup>le, it becomes possible to easily interact with other applications. With this option it is also possible to get solutions from algorithms currently not included in this tool; the user only has to guarantee the solution <sup>fi</sup>le follows a speci<sup>fi</sup>c structure.

![](/api/attachments/SGYG2EEE/fulltext/images/5d8f3f4072234df54753e69f8eb8da7d6dc7b881456c5f1e6181f71024564e68.jpg)  
Fig. 8. Changing the map scale (from 1:1098 to 1:612).

If the user runs the algorithm for all the grouping methods [6], the application displays a window where the user can visualize the different grouping methods. The total cost of the solution associated to each method, a bar indicating the percentage of improvement (as compared to the worst obtained result) as well as an image where the user can easily identify the best solutions found (Fig. 10). Afterwards, the user must choose the solution to visualize, either graphically on the map or numerically. In the former case, routes are displayed using different colours and the depots that will not be installed will have a new graphical representation, making it easier to understand the solution (Fig. 11).

All the information regarding the solution can also be visualized numerically (Fig. 12). The user can see the total cost of the solution, the depots to be installed, and the data of the different routes (capacity, path and cost).

![](/api/attachments/SGYG2EEE/fulltext/images/8028ec26b8eade610107983a98281fd588338d0d6f0f8e55de5643b309794907.jpg)  
Fig. 9. Visualization of clients demand.

Finally, it is also possible to run the algorithm step-by-step, which provides the application with a strong pedagogical component, allowing the user to have a detailed view of the development of the algorithm. This option enables the user to additionally handle the vehicle routing problem (VRP) and the capacitated location-allocation problem (CLAP) by running only a subset of the original heuristic (the <sup>fi</sup>rst, second and third steps to obtain the VRP solution and the fourth step for the CLAP), as shown in Fig. 13.

![](/api/attachments/SGYG2EEE/fulltext/images/721c1ba6ae258b7c969ae5835d6a6abb5e562dc3b2e45d806119bd518c760e30.jpg)  
Fig. 10. Control panel displaying the results associated to each grouping method.

![](/api/attachments/SGYG2EEE/fulltext/images/718566bdbb35cc8a070b7ae58e0755106740a9d566ba08dc0bc1d2eab002a0b6.jpg)  
Fig. 11. Graphical representation of the solution.

## 4.2.5. Data output

Regarding the data output the following options are available:

• Data export;

• Save the data in a <sup>fi</sup>le;

• Save the map image (containing all the information).

In order to export data, there is the possibility of exporting the clients and the depots data to text format <sup>fi</sup>les, facilitating the integration with other software. There is also the possibility of saving the data in a <sup>fi</sup>le. Through this option the user can save all the data into a single <sup>fi</sup>le, with a speci<sup>fi</sup>c format. Finally, there is the “Save Map” option, which allows the user to save the map he is currently visualizing to an image <sup>fi</sup>le.

## Solution: Problem 1

```txt
Solution: Problem 1
Total Cost= 422.3 m.u.
Route 1
Capacity= 6300
Depot 2 -> 10 -> 9 -> 7 -> 5 -> 2 -> 1 -> 6 -> 8
Cost= 86.4 m.u.
Route 2
Capacity= 2200
Depot 2 -> 4 -> 3
Cost= 45.4 m.u.
Route 3
Capacity= 7100
Depot 4 -> 16 -> 14 -> 15 -> 12 -> 11 -> 13
Cost= 101 m.u.
Route 4
Capacity= 6900
Depot 4 -> 17 -> 18 -> 20 -> 21 -> 19
Cost= 89.4 m.u.
```  
Fig. 12. Data window with the numerical information of the solution.

![](/api/attachments/SGYG2EEE/fulltext/images/1444c5479288ae5994ae1995ead8bb7b7c34a122298f7c9af63b8a80afb4f70a.jpg)  
Fig. 13. Visualization of the VRP (after the third step of the heuristic) on the DST.

## 4.2.6. Other characteristics

Besides the previously mentioned options, there is a set of characteristics that have been added to the application in order to improve its usefulness. For instance: an option to change the language; a help <sup>fi</sup>le and a set of options regarding the map, the visualization scale and the algorithm used.

The integration of other algorithms is made through the “Solver Options”, available in the menu.

## 5. Conclusion

A decision-support tool that implements a capacitated locationrouting problem (CLRP) with two levels (depots and customers) and a capacitated and homogeneous vehicle <sup>fl</sup>eet was presented. It allows the exploration of the solution <sup>fi</sup>nding process in a way easily understandable by the user, and enables access to online geographic data through web map servers (WMS).

A usable user interface was a great concern throughout the development of this tool, which was designed to allow decisionmakers with a moderate computer literacy to be able to obtain good quality solutions without much learning effort.

Although the best decision may not be the most cost ef<sup>fi</sup>cient, this type of tool can help managers make a more scienti<sup>fi</sup>cally supported decision, by providing the total estimated costs of a set of different solutions. From this point it is up to the manager to make the decision, taking into consideration the estimated cost, the service level or even the company strategy and motivation.

A decision-support tool assists, but does not replace, the decisionmaker. It does not try to provide the ‘answer’, nor does it impose a prede<sup>fi</sup>ned sequence of analysis. It supports semi-structured decisions where parts of the analysis can be systematized by the tool, improving the decision-maker's insight and judgement.

Although this decision-support tool has been developed for the CLRP, due to its modular architecture, it could also include, Network CLRP, LRP with paths and even more speci<sup>fi</sup>c cases such as the CLAP and the VRP. Moreover, future developments could lead to further integration with other WMS or geographic information systems (GIS).

## References

[1] M. Albareda-Sambola, J.A. Díaz, E. Fernández, A compact model and tight bounds for a combined location-routing problem, Computers & Operations Research 32 (2005) 407–428.

[2] S. Alter, A work system view of DSS in its fourth decade, Decision Support Systems 38 (2004) 319–327.

[3] D. Ambrosino, M.G. Scutellà, Distribution network design: new problems and related models, European Journal of Operational Research 165 (2005) 610–624.

[4] S.S. Barreto, http://sweet.ua.pt/\~iscf143/, 2003.

[5] S.S. Barreto, Análise e Modelização de Problemas de Localização-Distribuição [Analysis and Modelization of Location-Routing Problems] (Ph.D. dissertation, University of Aveiro, 2004) (in Portuguese).

[6] S. Barreto, C. Ferreira, J. Paixão, B.S. Santos, Using clustering analysis in a capacitated location-routing problem, European Journal of Operational Research 179 (2007) 968–977.

[7] J.H. Bookbinder, Global Logistics, Transportation Research E 41 (2005) 461–466.

[8] I.M. Branco, J.D. Coelho, The Hamiltonian p-median problem, European Journal of Operational Research 47 (1990) 86–95.

[9] A. Bruns, A. Klose, An iterative heuristic for location-routing problems based on clustering, Proceedings of the Second International Workshop on Distribution Logistics, 1995, pp. 1–6.

[10] C. Carlsson, E. Turban, DSS: directions for the next decade, Decision Support Systems 33 (2002) 105–110.

[11] Commission of the European Communities, European transport policy for 2010: time to decide, COM (2001) 370, Brussels, White Paper, 2001.

[12] A. Dix, J. Finlay, G. Abowd, R. Beale, Human–Computer Interaction, 3rd ed.Prentice Hall, New Jersey, 2004.

[13] H.B. Eom, S.M. Lee, Decision support systems applications research: a bibliography (1971–1988), European Journal of Operational Research 46 (3) (1990) 333–342.

[14] S.B. Eom, S.M. Lee, C. Somarajan, E.B. Kim, Decision support systems applications — a bibliography (1988–1994), OR Insight 10 (2) (1997) 18–32.

[15] B.S. Everitt, Cluster Analysis, 3rd ed.Arnold, London, 1993

[16] G. Laporte, Location-routing problems, in: B.L. Golden, A.A. Assad (Eds.), Vehicle Routing: Methods and Studies, North-Holland, Amsterdam, 1988, pp. 163–197.

[17] C. Lin, C. Kwok, Multi-objective metaheuristics for a location-routing problem with multiple use of vehicles on real data and simulated data, European Journal of Operational Research 175 (2006) 1833–1849.

[18] J. Malczewski, GIS and Multicriteria Decision Analysis, John Wiley and Sons, New York, 1999.

[19] J. Melechovský, C. Prins, C.R. Wol<sup>fl</sup>er-Calvo, A metaheuristic to solve a locationrouting problem with non-linear costs, Journal of Heuristics 11 (2005) 375–391.

[20] A. Melo, B.S. Santos, C. Ferreira, J.S. Pinto, Software application for data visualization and interaction in a location routing problem, Revista do Departamento de Electrónica e Telecomunicações da Universidade de Aveiro 2 (4) (1999) 471–476.

[21] H. Min, Consolidation terminal location-allocation and consolidated routing problems, Journal of Business Logistics 17 (2) (1996) 259–288.

[22] H. Min, V. Jayaraman, R. Srivastava, Combined location-routing problems: a synthesis and future research directions, European Journal of Operational Research 108 (1998) 1–15.

[23] K.G. Murty, P.A. Djang, The U.S. army national guard’s mobile training simulators location and routing problem, Operations Research 47 (1999) 175–182.

[24] G. Nagy, S. Salhi, Nested heuristic methods for the location-routing problem, Journal of the Operational Research Society 47 (1996) 1166– 74.

[25] G. Nagy, S. Salhi, Location-routing: issues, models and methods, European Journal of Operational Research 177 (2007) 649–672.

[26] J. Perl, M.S. Daskin, A warehouse location-routing problem, Transportation Research 19B (5) (1985) 381-396

[27] S. Salhi, G.K. Rand, The effect of ignoring routes when locating depots, European Journal of Operational Research 39 (1989) 150–156.

[28] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2002) 111–126.

[29] R. Srivastava, W.C. Benton, The location-routing problem: considerations in physical distribution system design, Computers & Operations Research 17 (5) (1990) 427–435.

[30] D. Tuzun, L.I. Burke, A two-phase tabu search approach to the location routing problem, European Journal of operational Research 116 (1999) 87–99.

Rui Borges Lopes received his MSc degree in Operations Management from the University of Aveiro in 2005. He teaches at the Department of Economics, Management and Industrial Engineering of the University of Aveiro and is a researcher in the R&D unit CIO of the University of Lisbon. His current research interests lie primarily in Operations Research (location-routing models), Spatial Decision-Support Systems and Multiple Criteria Programming.

Sérgio Barreto is an Associate Professor at the Accounting and Administration Institute of the University of Aveiro where he is a member of the Marketing and Data Analysis Research Center and teacher of the Mathematics group. He has a PhD in Industrial Management from the University of Aveiro. He is also a researcher of the CIO (Operations Research Center) of the University of Lisbon and author and co-author of several scienti<sup>fi</sup>c papers presented at conferences and published in journals. His research area is related with combinatorial optimization with a special interest in location and routing problems.

Carlos Ferreira received a MSc degree in Statistics and Operational Research from the University of Lisbon and a PhD in Mathematics from the University of Aveiro in 1998. He currently is an Associate Professor with the Department of Economics, Management and Industrial Engineering at the University of Aveiro, Portugal, where he is director of the Information Management MSc. His teaching and research interests are in Operations Research, Data Analysis and Information Management.

Beatriz Sousa Santos received her PhD in Electrical Engineering in 1989 and is currently Associate Professor with the Department of Electronics, Telecommunications and Informatics, University of Aveiro, Portugal. She lectures Human–Computer Interaction and Computer Graphics and her main research interests are in the areas of Data and Information Visualization.
