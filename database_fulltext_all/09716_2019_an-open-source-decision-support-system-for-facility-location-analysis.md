---
otero_id: 9716
otero_key: "EHJ6U7U5"
title: "An open source decision support system for facility location analysis"
authors: "Güneş Erdoğan; Neophytos Stylianou; Christos Vasilakis"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113116"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An open source decision support system for facility location analysis

Güneş Erdoğan<sup>a,</sup>\*, Neophytos Stylianou<sup>a,b</sup>, Christos Vasilakis<sup>a</sup>

![](/api/attachments/EHJ6U7U5/fulltext/images/fd3cce0fd6dee491adec309776969136f40470f6ac935cb4cd629966b43b4e63.jpg)

<sup>a</sup> School of Management, University of Bath, BA1 7AY Bath, UK

<sup>b</sup> Medical School, University of Nicosia, Nicosia, Cyprus

## A R T I C L E I N F O

Keywords: Facility location analysis Spreadsheets Open source Health services

## A B S T R A C T

This paper introduces FLP Spreadsheet Solver, an open source spreadsheet based Decision Support System fo Facility Location Problems. Structure of the spreadsheets, interface of the solver, and a Tabu Search algorithm implemented within the solver are described. An integer programming formulation of the underlying facility location problem is provided. Computational tests show that FLP Spreadsheet Solver can solve benchmark pmedian and capacitated p-median instances to near optimality. The paper also includes a case study consisting of the application of FLP Spreadsheet Solver to a healthcare facility location problem.

## 1. Introduction

Facility Location Problems (FLPs) aim to select a subset of locations from a set of candidate locations, and to determine which customer locations will be served by which facility, to optimize an objective function that is based on the distances (or the costs) between the facilities and the demands of customer locations they serve. FLPs arise in both service and manufacturing industries, and in many diverse contexts, ranging from healthcare to commercial transportation and storage systems [1]. FLPs are considered to be strategical level management problems, the consequences of which reverberate for years and shape the environment around them, e.g. the location of a manufacturing facility may increase both the average income of the popu lation and the pollution in its vicinity. An exception to this rule is the set of operational level FLPs that involve mobile facilities such as ambulances.

Due to the advances in computer hardware and optimization software in the past two decades, basic FLPs and some of their variants can be solved to optimality for instances with up to a thousand locations [1]. However, solving an FLP arising in a real-world transporta tion network is still a challenging undertaking. Acquiring the geo graphical data is a preliminary yet non-trivial task. The highperformance computer codes developed by academics are usually not made available for public use, and even if they are, they require adaptation and compilation. The number of variables for mixed integer linear programming models for FLPs are in quadratic order of the number of locations, which exceeds the capacity of most freely avail able general purpose solvers, even for small instances.

In this paper, we introduce an Excel-based Decision Support System (DSS) for FLPs, named FLP Spreadsheet Solver [2]. Using a Tabu Search algorithm, it can provide near-optimal solutions for FLPs with up to 200 locations. FLP Spreadsheet Solver can be downloaded from https:// www.euro-online.org/websites/verolog/flp-spreadsheet-solver/ at zero cost, and it can work on multiple operating systems due to the portability of Excel. Through a link to a publicly available Geographical Information System (GIS) web service, FLP Spreadsheet Solver can retrieve coordinates of locations as well as driving distances (or durations), enabling decision makers to perform location analysis without the need for sophisticated know-how about using the GIS. It has been used for analyzing healthcare facility location decisions in the United Kingdom, and for teaching by academics in Canada, Germany, Spain, and Turkey.

Although large-scale organizations may find the time and money to invest into the development and deployment of specialized FLP models and tools, FLPs also arise when both money and time are in short supply. Typical examples include third sector organizations as well as practical problems arising in the area of disaster response/humanitarian logistics. With global warming and increasing political instability, natural and man-made disasters are becoming increasingly prevalent. To minimize the damage of a disaster and ensure timely response, it is imperative to find efective logistics solutions in a very short span of time. This need is recognized by Keenan and Jankowski [3], who state that “Emergency systems require rapid decision making, and the clarity of information display plays a huge role in their success.” In a similar vein, Schätter et al. [4] comment on the lack of decision support tools for disaster management, and the importance of precise yet comprehensible decision support for logistical operations. Consequently, we believe that FLP Spreadsheet Solver can be best utilized within the context of humanitarian logistics due to its ease of use, in addition to the ability to provide efective solutions in a short time on multiple platforms with zero cost, as well as its visualization capability. As an example, FLP Spreadsheet Solver may be used for deciding on the locations for provision distribution after a disaster.

The rest of the paper is organized as follows. In Section 2, we provide a brief review of the literature of FLPs and highlight our contributions. We provide the details of FLP Spreadsheet Solver in Section 3, including its interface and the structure of the spreadsheets. A formulation of the underlying unified FLP it solves, solution algo rithm, and performance on benchmark instances are provided in Section 4. In Section 5, we present a real-world application of the solver in a healthcare facility location problem. Finally, in Section 6, we provide our concluding remarks.

## 2. Related work

In this section, we first review the existing literature and software for FLPs, and then provide an outline of our contributions.

## 2.1. Literature

FLPs have been studied in depth for more than 50 years. Starting with the seminal paper of Hakimi [5], the study of FLPs has grown into one of the largest subfields of Operational Research (OR). We refer the reader to the recent book by Laporte et al. [1] and the references therein for an in-depth exposition to FLPs. Pick et al. [6] recently presented the state-of-the-art in terms of decision support systems for location analytics, in addition to current trends and future research directions. Finally, Ahmadi-Javid et al. [7] provided a comprehensive survey of healthcare facility location problems, which may benefit the readers that are particularly interested in the applications of FLPs. Many variants have been proposed through the introduction of extra features, including but not limited to the capacity of the facilities and the maximum allowed distance for service. In what follows, we will only describe the basic FLPs, for the sake of brevity.

The first ever FLPs to be studied are the fundamental problems of p centre and p-median [5], both of which aim to locate exactly p facilities on a network. The former aims to minimize the maximum distance between any customer location and the closest facility to it, focusing on equity. The latter minimizes the sum of the distances from each customer location to the closest facility, emphasizing performance. Toregas et al. [8] defined the concept of “coverage”, where a customer location is covered if an only if it is within a prespecified distance of the closest facility. The authors introduced the Set Covering Problem (SCP). which aims to minimize the number of facilities to be opened while ensuring all customers are covered. Church and ReVelle [9] studied the Max imum Coverage Location Problem (MCLP) to locate p facilities with the objective of maximizing total coverage, as a remedy to the high-cost solutions found by the SCP. Later studies also incorporated probabilistic coverage, e.g. the probability that an ambulance reaches a population centre within the preset time limit (e.g. Ref. [10]). Finally, Cornuejols et al. [11] presented the Uncapacitated Facility Location Problem (UFLP), which involves minimizing the sum of the cost of installation of facilities and the cost of transportation between facilities and customers. and the number of facilities is indeterminate.

We are aware of only three DSS for general FLPs. The first is named SITATION, provided for free by Daskin [12], which is capable of solving five classes of FLPs (p -centre, p-median, SCP, MCLP, and UFLP), to a maximum size of 150 locations. The second is an R package called or loca: Operations Research LOCational Analysis Models [13], which contains algorithms to solve the Fermat-Weber minisum location problem in the plane. The third and final solver is called Library of Location Algorithms (LoLA, [14]), which is capable of solving a much larger set of problem types.

Regarding applications of FLPs, Rakes et al. [15] have provided a

DSS for location analysis regarding the assignment of families to interim housing post-disaster. Karatas et al. [16] studied the problem of allocating helicopters to stations in order to minimize response time, provided an optimization model and a simulation model, and applied their results to the incident data from the Aegean coast of Turkey. KC et al. [17] used the MCLP to optimize the coverage provided by fire service in Brisbane, Australia. The authors determined a set of locations for potential fire stations based on population growth estimates. Fi nally, Smith et al. [18] applied a Relational-Algebraic Capacitated Location algorithm to a large-scale distance constrained UFLP to locate HIV/AIDS diagnostic equipment in South Africa. The problem instance analyzed by the authors consists of 1800 aggregated demand points and 60 facilities. The authors compared their results with data from a pilot study of four health districts, and concluded the validity of their method.

Spreadsheet based DSSs have been advocated by Seref and Ahuja [19] and have been gaining importance in the past few years. Erdogan [20] has provided an open-source spreadsheet solver for Vehicle Routing Problems (VRPs), named VRP Spreadsheet Solver, and provided two case studies of its application in healthcare and tourism. Bailey and Nowak [21] have presented a DSS to assign athletes to events of track-and-field. Finally, Bailey and Michaels [22] have provided a DSS to assign students to teachers, which has been successfully implemented in an elementary school in the United States, resulting in significant time savings.

## 2.2. Our contribution

FLP Spreadsheet Solver represents an improvement compared to existing available solvers through a number of added features and advantages. An immediate benefit of FLP Spreadsheet Solver is its access to a public GIS, which significantly decreases the overall decision support time for real-world problems, and facilitates the implementation and communication of the results due to better visualization. All three aforementioned software packages require the distance data for the network being analyzed to be input separately. Visualizing the solutions on a real map is also significantly harder for these solvers, which require a map of the region being analyzed to be acquired and incorporated. In addition, the executables of SITATION and LoLA are not compiled to run on Mac based systems, decreasing their accessibility.

FLP Spreadsheet Solver can solve many of the basic location problems consisting of capacitated and distance constrained versions of p -centre, p-median, MCLP, and UFLP, for up to 200 locations. We underline that the limit on the number of locations is primarily due to the limitations of the GIS service and can be manually lifted by the user. We demonstrate in Section 4 that the solver can find near-optimal solutions to FLPs with up to 600 locations, surpassing the location limit of SIT-ATION. In addition, FLP Spreadsheet Solver can handle multiple objectives simultaneously and can find solutions that balance equity and performance, a feature none of the existing solvers have.

Furthermore, all three existing solvers work in a procedural manner, i.e. the user executes the solvers on input data, and cannot easily change the optimal or near-optimal results returned by the solvers. A notable exception is SITATION that allows manual change of locations for facilities. FLP Spreadsheet Solver, on the other hand, provides the possibility of declarative programming provided by Excel. The end user may manually change the facilities or the allocation of customers to the facilities by simply clicking on the drop-down list of locations in appropriate cells (or cutting and pasting a list of customers from one facility to another), possibly resulting in mathematically sub-optimal solutions that better suit the managerial needs at hand. The decision maker may then instantaneously evaluate the diference in performance as computed by the spreadsheet. This improved user interface, coupled with a user function to check feasibility of the modified solution, provides the end user with an enhanced ability to perform what-if analysis.

In addition, we believe that the most significant contribution of our work is a maximally accessible and easy-to-use DSS. FLP Spreadsheet Solver owes its accessibility and ease-of-use to:

1. Being free to download, without necessitating registration by the end user.

2. Being multi-platform, working on both Windows and Mac versions of Excel.

3. Being installation-free, since Excel is already installed on most Windows and Mac computers.

4. Being open source, and thus being easily modifiable by an advanced user if needed.

5. Having integrated GIS functions that facilitate data acquisition and problem illustration.

6. Operating within the familiar Excel environment.

## 3. User interface

FLP Spreadsheet Solver is based on the same design principles as VRP Spreadsheet Solver [20], unavoidably resulting in similarities be tween the user interfaces. The data is kept in five spreadsheets: Console, Locations, Costs and Coverage, Solution, and Visualization. The spreadsheets are indexed in the order they should be generated, and the spreadsheets with the higher indices depend on the information stored in the spreadsheets with lower indices. All spreadsheets employ a colo coding scheme, where the green cells are the input from the user or the result of the solver, yellow cells are automatically computed by the spreadsheets, orange cells signal a warning, and red cells signal an error or violation of a constraint.

## 3.1. FLP solver console

This worksheet (Fig. 1) forms the basis for the rest of the worksheets and contains the number of locations and facilities, in addition to options regarding GIS functions, visualization parameters, and the CPU time limit for the solver. Users may select the primary objective function as minimization of the maximum service distance (p -centre), minimization of the total cost (p-median, UFLP), or maximization of total demand covered (MCLP). The worksheet employs data validation for all entries other than the GIS key, in order to avoid erroneous data

entry.

## 3.2. Locations

This worksheet contains the name, address, coordinates, and demand for every location (Fig. 2). It also stores which of the locations must be or may be facilities, and which ones cannot. For the locations that must or may be facilities, the user can also input the setup cost and capacity of a facility to be built at that location. The coordinates may be retrieved from the GIS web service if the user has a key, which may be generated at zero cost for research and educational purposes.

## 3.3. Costs and coverage

Costs and coverage worksheet (Fig. 3), as its name implies, stores the distance, cost, and coverage data for pairs of locations. In addition to the GIS web service, the distances may be computed using a spherical approximation for the shape of the Earth, which is useful if the problem data is based on flight distances. Users may opt to retrieve the travel time between locations (in minutes) from the GIS service to be used as distance. All data may be modified manually, e.g. the distance between two locations can be manually set to a high value to disallow service from one to the other. As a final note, although “demand covered” is computed as the product of the demand and coverage percentage, it can be manually edited by the user to apply diferent types of coverage functions based on the distance.

## 3.4. Solution

This worksheet is composed of six columns for each facility, locations served by the facility, their names and demand, amount of de mand covered, and the cost resulting from the service. Users can manually input solutions by selecting the names of the locations from the drop-down menu in each cell of the second column, e.g. columns B and L in Fig. 4. The three objective functions and their values are displayed on the top left, and facility specific information is generated on row 6.

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>1</td><td>Sequence</td><td>Parameter</td><td>Value</td><td>Remarks</td></tr><tr><td>2</td><td>0.Optional - GIS License</td><td>Bing Maps Key</td><td></td><td>You can get a free trial key at https://www.bingmapsportal.com/</td></tr><tr><td>3</td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>1.Locations</td><td>Number of locations</td><td>128</td><td>[5,200]</td></tr><tr><td>5</td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>2.Costs and Coverage</td><td>Distance computation</td><td>Bing Maps driving durations (min)</td><td></td></tr><tr><td>7</td><td></td><td>Bing Maps route type</td><td>Fastest / Car</td><td>Recommendation: use Fastest</td></tr><tr><td>8</td><td></td><td>Cost per unit distance</td><td>1</td><td>Positive</td></tr><tr><td>9</td><td></td><td>Costs scaled by demand</td><td>No</td><td></td></tr><tr><td>10</td><td></td><td>Service distance limit</td><td>200</td><td>Positive</td></tr><tr><td>11</td><td></td><td>Coverage distance limit</td><td>40</td><td>Positive</td></tr><tr><td>12</td><td></td><td>Coverage type</td><td>Linearly decreasing coverage</td><td></td></tr><tr><td>13</td><td></td><td></td><td></td><td></td></tr><tr><td>14</td><td>3.Solution</td><td>Number of facilities</td><td>5</td><td>[1,100]</td></tr><tr><td>15</td><td></td><td>Objective</td><td>Minimize total cost</td><td></td></tr><tr><td>16</td><td></td><td>All facilities must be located?</td><td>Yes</td><td></td></tr><tr><td>17</td><td></td><td></td><td></td><td></td></tr><tr><td>18</td><td>4.Optional - Visualization</td><td>Visualization background</td><td>Bing Maps</td><td></td></tr><tr><td>19</td><td></td><td>Location labels</td><td>Location IDs</td><td></td></tr><tr><td>20</td><td></td><td></td><td></td><td></td></tr><tr><td>21</td><td>5.Solver</td><td>Warm start?</td><td>Yes</td><td></td></tr><tr><td>22</td><td></td><td>Show progress on status bar?</td><td>No</td><td>May slow down the solution algorithm.</td></tr><tr><td>23</td><td></td><td>CPU time limit (seconds)</td><td>2400</td><td>Recommendation: At least 1260 seconds.</td></tr></table>

Fig. 1. Screenshot of FLP Solver Console worksheet.

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td></tr><tr><td>1</td><td>Location ID</td><td>Name</td><td>Address</td><td>Latitude (y)</td><td>Longitude (x)</td><td>Demand</td><td>May be a facility?</td><td>Capacity</td><td>Setup cost</td></tr><tr><td>2</td><td>1</td><td>RUH</td><td>Royal United Hospital Main Entrance, Bath BA1 3NH, UK</td><td>51.3908340</td><td>-2.3893830</td><td>0</td><td>Must be a facility</td><td>216382</td><td>0</td></tr><tr><td>3</td><td>2</td><td>Chippenham</td><td>St Francis Ave, Chippenham SN15 2SE, UK</td><td>51.4527290</td><td>-2.1253540</td><td>0</td><td>May be a facility</td><td>216382</td><td>0</td></tr><tr><td>4</td><td>3</td><td>Trowbridge</td><td>46 Seymour Rd, Trowbridge BA14 8LT, UK</td><td>51.3254280</td><td>-2.2110140</td><td>0</td><td>May be a facility</td><td>216382</td><td>0</td></tr><tr><td>5</td><td>4</td><td>Paulton</td><td>2 Salisbury Rd, Paulton, Bristol BS39 7SA, UK</td><td>51.3001070</td><td>-2.4943830</td><td>0</td><td>May be a facility</td><td>216382</td><td>0</td></tr><tr><td>6</td><td>5</td><td>Shepton Mallet</td><td>Bucklers Way, Shepton Mallet BA4 5GB, UK</td><td>51.1903180</td><td>-2.5615780</td><td>0</td><td>May be a facility</td><td>216382</td><td>0</td></tr><tr><td>7</td><td>6</td><td>Frome</td><td>48A Bath Rd, Frome BA11 2HH, UK</td><td>51.2388600</td><td>-2.3127930</td><td>0</td><td>May be a facility</td><td>216382</td><td>0</td></tr><tr><td>8</td><td>7</td><td>E02002985</td><td>14 Ashcroft Ave, Keynsham, Bristol BS31 2EX, UK</td><td>51.4136070</td><td>-2.5075280</td><td>737</td><td>Cannot be a facility</td><td>216382</td><td>0</td></tr><tr><td>9</td><td>8</td><td>E02002986</td><td>27 Berkeley Gardens, Keynsham, Bristol BS31 2PN, UK</td><td>51.4087670</td><td>-2.5040810</td><td>771</td><td>Cannot be a facility</td><td>216382</td><td>0</td></tr><tr><td>10</td><td>9</td><td>E02002987</td><td>4-5 Windrush Rd, Keynsham, Bristol BS31 1QL, UK</td><td>51.4069560</td><td>-2.4878730</td><td>451</td><td>Cannot be a facility</td><td>216382</td><td>0</td></tr><tr><td>11</td><td>10</td><td>E02002988</td><td>25 Larkhall PI, Bath BA1 6SF, UK</td><td>51.3985600</td><td>-2.3459080</td><td>2152</td><td>Cannot be a facility</td><td>216382</td><td>0</td></tr><tr><td>12</td><td>11</td><td>E02002989</td><td>61-77 Brookfield Park, Bath BA1, UK</td><td>51.3980789</td><td>-2.3928628</td><td>2986</td><td>Cannot be a facility</td><td>216382</td><td>0</td></tr><tr><td>13</td><td>12</td><td>E02002990</td><td>11 Brunswick St, Bath BA1 6PQ, UK</td><td>51.3924980</td><td>-2.3523450</td><td>2537</td><td>Cannot be a facility</td><td>216382</td><td>0</td></tr><tr><td>14</td><td>13</td><td>E02002991</td><td>18 Lansdown Rd, Bath BA1, UK</td><td>51.4041410</td><td>-2.3736740</td><td>2449</td><td>Cannot be a facility</td><td>216382</td><td>0</td></tr><tr><td>15</td><td>14</td><td>E02002992</td><td>117 Newbridge Hill, Bath BA1 3PT, UK</td><td>51.3876360</td><td>-2.3940120</td><td>2151</td><td>Cannot be a facility</td><td>216382</td><td>0</td></tr><tr><td>16</td><td>15</td><td>E02002993</td><td>5 Marlborough Ln, Bath BA1 2NQ, UK</td><td>51.3847080</td><td>-2.3709940</td><td>2064</td><td>Cannot be a facility</td><td>216382</td><td>0</td></tr><tr><td>17</td><td>16</td><td>E02002994</td><td>171 Dark Ln, Bathampton, Bath BA2 6SZ, UK</td><td>51.3954380</td><td>-2.3212350</td><td>2777</td><td>Cannot be a facility</td><td>216382</td><td>0</td></tr><tr><td>18</td><td>17</td><td>E02002995</td><td>171 North St, Bath BA1 6V, UK</td><td>51.3978191</td><td>-2.3105010</td><td>1810</td><td>Cannot be a facility</td><td>216382</td><td>0</td></tr></table>

Fig. 2. Screenshot of Locations worksheet.

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td></tr><tr><td>1</td><td>From</td><td>To</td><td>Time</td><td>Cost</td><td>Coverage</td><td>Demand covered</td><td>Method:</td><td>Bing Maps driving durations</td></tr><tr><td>2</td><td>RUH</td><td>RUH</td><td>0.00</td><td>0.00</td><td>100.00%</td><td>0.00</td><td></td><td></td></tr><tr><td>3</td><td>RUH</td><td>Chippenham</td><td>36.00</td><td>36.00</td><td>100.00%</td><td>0.00</td><td></td><td></td></tr><tr><td>4</td><td>RUH</td><td>Trowbridge</td><td>35.00</td><td>35.00</td><td>100.00%</td><td>0.00</td><td></td><td></td></tr><tr><td>5</td><td>RUH</td><td>Paulton</td><td>32.00</td><td>32.00</td><td>100.00%</td><td>0.00</td><td></td><td></td></tr><tr><td>6</td><td>RUH</td><td>Shepton Mallet</td><td>49.00</td><td>49.00</td><td>100.00%</td><td>0.00</td><td></td><td></td></tr><tr><td>7</td><td>RUH</td><td>Frome</td><td>38.00</td><td>38.00</td><td>100.00%</td><td>0.00</td><td></td><td></td></tr><tr><td>8</td><td>RUH</td><td>E02002985</td><td>22.00</td><td>22.00</td><td>100.00%</td><td>737.00</td><td></td><td></td></tr><tr><td>9</td><td>RUH</td><td>E02002986</td><td>24.00</td><td>24.00</td><td>100.00%</td><td>771.00</td><td></td><td></td></tr><tr><td>10</td><td>RUH</td><td>E02002987</td><td>20.00</td><td>20.00</td><td>100.00%</td><td>451.00</td><td></td><td></td></tr><tr><td>11</td><td>RUH</td><td>E02002988</td><td>13.00</td><td>13.00</td><td>100.00%</td><td>2152.00</td><td></td><td></td></tr><tr><td>12</td><td>RUH</td><td>E02002989</td><td>4.00</td><td>4.00</td><td>100.00%</td><td>2986.00</td><td></td><td></td></tr><tr><td>13</td><td>RUH</td><td>E02002990</td><td>10.00</td><td>10.00</td><td>100.00%</td><td>2537.00</td><td></td><td></td></tr><tr><td>14</td><td>RUH</td><td>E02002991</td><td>8.00</td><td>8.00</td><td>100.00%</td><td>2449.00</td><td></td><td></td></tr><tr><td>15</td><td>RUH</td><td>E02002992</td><td>3.00</td><td>3.00</td><td>100.00%</td><td>2151.00</td><td></td><td></td></tr><tr><td>16</td><td>RUH</td><td>E02002993</td><td>5.00</td><td>5.00</td><td>100.00%</td><td>2064.00</td><td></td><td></td></tr><tr><td>17</td><td>RUH</td><td>E02002994</td><td>18.00</td><td>18.00</td><td>100.00%</td><td>2777.00</td><td></td><td></td></tr></table>

Fig. 3. Screenshot of Costs and coverage worksheet.

## 3.5. Visualization

Visualization worksheet, depicted in Fig. 5, displays the data contained within Solution worksheet as a scatter plot on the backdrop of a map, obtained from a public GIS by our DSS. Users may manually change the size of the markers, width of the lines, colors of the markers, as well as adding extra information, to maximize the amount of in formation to display. Fig. 5 also depicts the data we will be using for our case study in Section 5.

## 3.6. Menu

The menu of FLP Spreadsheet Solver has a dedicated ribbon tab, as depicted in Fig. 6. Its design is aimed at increasing user friendliness through the use of buttons with icons. The buttons are numbered to match the number of the associated worksheet. In addition to setting up the worksheets to store the data and running the solver, users may issue commands to determine the coordinates of the locations, the driving distances or durations between the locations, and run a feasibility check to see if manual changes have resulted in an infeasible solution.

## 4. Model and algorithm

We now present an integer programming model of the problem solved by FLP Spreadsheet Solver, and the Tabu Search (TS) algorithm it employs, followed by the results of our computational experiments.

## 4.1. Model

Consider a directed graph $G = ( V { , } A )$ , where the vertex set consists of three disjoint subsets $V = V _ { 1 } \cup V _ { 2 } \cup V _ { 3 }$ . The first subset $V _ { 1 }$ contains the vertices that must be chosen as (or already are) facilities. The second subset $V _ { 2 }$ is composed of vertices that may be facilities. The third subset $V _ { 3 }$ consists of vertices that cannot be facilities. Each vertex i ∈ V has a demand $q _ { i } ,$ and each vertex i V V has a known (or estimated) setup cost $s _ { i }$ that is incurred if i is selected to host a facility, and a capacity $Q _ { i }$ . The arc set A contains all arcs connecting the vertices in V as well as self arcs (i,i) ∀i ∈ V. Associated with every arc $( i , j ) \in A ,$ there is a a cost $c _ { i j } ,$ distance $d _ { i j } ,$ and a probability $p _ { i j }$ of a facility in location i covering the demand in location j.

We denote the maximum number of facilities as m, and the binary parameter α, which is equal to 1 if all m facilities must be located and 0 otherwise. We also write δ to denote the service distance limit. Let us define $x _ { i j }$ to be equal to 1 if vertex i is served by a facility at vertex j, and 0 otherwise. In addition, let us define y to be equal to 1 if a facility is to be located at vertex $j ,$ and 0 otherwise. Finally, let us define w as the maximum distance between any location and the facility it is served by. The model is then:

<table><tr><td></td><td>A</td><td>B</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td></tr><tr><td>1</td><td>Total cost incurred:</td><td>8172.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>Total demand covered:</td><td>216382.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>Maximum service distance:</td><td>97.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>Facility 1</td><td>Facility location</td><td>Capacity</td><td>Demand allocated</td><td>Demand covered</td><td>Cost incurred</td><td></td><td>Facility 2</td><td>Facility location</td></tr><tr><td>6</td><td></td><td>RUH</td><td>216382.00</td><td>49012.00</td><td>49012.00</td><td>3224.00</td><td></td><td></td><td>Chippenham</td></tr><tr><td>7</td><td>Locations served</td><td>Location name</td><td>Distance</td><td>Demand</td><td>Covered</td><td>Cost</td><td></td><td>Locations served</td><td>Location name</td></tr><tr><td>8</td><td>1</td><td>RUH</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td></td><td>1</td><td>Chippenham</td></tr><tr><td>10</td><td>2</td><td>E02004667</td><td>70.00</td><td>41.00</td><td>41.00</td><td>70.00</td><td></td><td>2</td><td>E02004611</td></tr><tr><td>12</td><td>3</td><td>E02004608</td><td>66.00</td><td>32.00</td><td>32.00</td><td>66.00</td><td></td><td>3</td><td>E02006659</td></tr><tr><td>14</td><td>4</td><td>E02004646</td><td>63.00</td><td>27.00</td><td>27.00</td><td>63.00</td><td></td><td>4</td><td>E02006006</td></tr><tr><td>16</td><td>5</td><td>E02004652</td><td>63.00</td><td>45.00</td><td>45.00</td><td>63.00</td><td></td><td>5</td><td>E02006004</td></tr><tr><td>18</td><td>6</td><td>E02004643</td><td>62.00</td><td>37.00</td><td>37.00</td><td>62.00</td><td></td><td>6</td><td>E02004623</td></tr><tr><td>20</td><td>7</td><td>E02004672</td><td>62.00</td><td>38.00</td><td>38.00</td><td>62.00</td><td></td><td>7</td><td>E02003368</td></tr><tr><td>22</td><td>8</td><td>E02004609</td><td>62.00</td><td>50.00</td><td>50.00</td><td>62.00</td><td></td><td>8</td><td>E02006636</td></tr><tr><td>24</td><td>9</td><td>E02004639</td><td>62.00</td><td>63.00</td><td>63.00</td><td>62.00</td><td></td><td>9</td><td>E02006886</td></tr><tr><td>26</td><td>10</td><td>E02004641</td><td>61.00</td><td>50.00</td><td>50.00</td><td>61.00</td><td></td><td>10</td><td>E02003212</td></tr><tr><td>28</td><td>11</td><td>E02004634</td><td>58.00</td><td>43.00</td><td>43.00</td><td>58.00</td><td></td><td>11</td><td>E02004622</td></tr><tr><td>30</td><td>12</td><td>E02004650</td><td>55.00</td><td>25.00</td><td>25.00</td><td>55.00</td><td></td><td>12</td><td>E02006644</td></tr><tr><td>32</td><td>13</td><td>E02003079</td><td>55.00</td><td>41.00</td><td>41.00</td><td>55.00</td><td></td><td>13</td><td>E02004624</td></tr><tr><td>34</td><td>14</td><td>E02004651</td><td>52.00</td><td>17.00</td><td>17.00</td><td>52.00</td><td></td><td>14</td><td>E02006634</td></tr><tr><td>36</td><td>15</td><td>E02004661</td><td>50.00</td><td>36.00</td><td>36.00</td><td>50.00</td><td></td><td>15</td><td>E02006848</td></tr></table>

Fig. 4. Screenshot of Solution worksheet.

![](/api/attachments/EHJ6U7U5/fulltext/images/5de9157d3be222ab06bfefec63ea71c99d754eef95c3fd6c524c196b8dcd5b8e.jpg)  
Fig. 5. Screenshot of Visualization worksheet.

![](/api/attachments/EHJ6U7U5/fulltext/images/b09960d74d5d6abdbf32c32f8b21b41afab0d67a2253d805f94eb63e34bb2197.jpg)  
Fig. 6. The dedicated tab and menu for FLP Spreadsheet Solver.

$$
\text { lexmin } \left(\sum_ {(i, j) \in A} c _ {i j} x _ {i j} + \sum_ {j \in V} s _ {j} y _ {j}, w, - \sum_ {(i, j) \in A} q _ {i} p _ {i j} x _ {i j}\right)\tag{1}
$$

$$
\text { subject   to } \quad \sum_ {j \in V} x _ {i j} = 1, \quad \forall i \in V\tag{2}
$$

$$
x _ {i j} \leq y _ {j} \quad \forall (i, j) \in A,\tag{3}
$$

$$
\sum_ {i \in V} q _ {i} x _ {i j} \leq Q _ {j} y _ {j} \quad \forall j \in V _ {1} \cup V _ {2},\tag{4}
$$

$$
\sum_ {j \in V} y _ {j} \leq m,\tag{5}
$$

$$
\sum_ {j \in V} y _ {j} \geq m \times \alpha ,\tag{6}
$$

$$
w \geq \sum_ {j \in V} d _ {i j} x _ {i j} \quad \forall i \in V,\tag{7}
$$

$$
x _ {i j} = 0 \quad \forall (i, j) \in A: d _ {i j} > \delta ,\tag{8}
$$

$$
x _ {i j} \in \{0, 1 \} \quad \forall (i, j) \in A: d _ {i j} \leq \delta ,\tag{9}
$$

$$
y _ {j} = 1 \quad \forall j \in V _ {1},\tag{10}
$$

$$
y _ {j} \in \{0, 1 \} \quad \forall j \in V _ {2},\tag{11}
$$

$$
y _ {j} = 0 \quad \forall j \in V _ {3},\tag{12}
$$

$$
w \geq 0.\tag{13}
$$

The objective function Eq. (1) minimizes the total cost, the maximum distance between every location and the facility it is assigned to, and maximizes the coverage, in the given lexicographic order. We emphasize that the users may opt to change the order of objectives. Constraint (2) states that every location must be assigned to a facility. Constraint (3) requires a facility to be located at vertex j for any location i to receive service from it. The demand assigned to each facility is required to be less than or equal to its capacity by constraint (4). The maximum number of facilities is set by constraint (5), which is forced as an equality by constraint (6) if $\alpha = 1$ . Constraint (7) states that w must be greater than or equal to the distance between each location and the facility it is served by.

The rest of the constraints describe the nature of the variables, or rule out disallowed decisions, or enforce mandatory decisions. Constraint (8) forbids the assignment of any location to a facility at a distance of greater than δ, and Eq. (9) states the binary nature of the $x _ { i j }$ variables. Constraints (10), (11), and (12) state that the vertices in $V _ { 1 }$ must be facilities, whereas the vertices in $V _ { 2 }$ may be facilities, and the vertices in $V _ { 3 }$ are not allowed to host a facility. Finally, Eq. (13) is the nonnegativity constraint for w.

## 4.2. Solution algorithm

Two of the main components of a metaheuristic algorithm are intensification and diversification [23], where the former is aimed at improving the solution quality and the latter is aimed at escaping local optima. Intensification is usually achieved through local search, whereas diversification can be attained through multiple ways. Some common methods are random perturbations of a given solution as in Iterated Local Search, changing the order of neighborhoods as in Variable Neighbourhood Search, combining diferent solutions as in Genetic Algorithms, and memory structures that prohibit cycling as in TS. Design of a high performance heuristic requires the two components to be balanced.

FLP Spreadsheet Solver incorporates a TS algorithm that utilizes diferent components for the uncapacitated and capacitated instances, which we provide below. We start with the uncapacitated case, in which all locations are assigned to the closest facility for evaluating a solution. Hence, it sufices for the algorithm to keep the list of locations hosting a facility. The objective function value of each solution is penalized by a large constant for every missing location and violated distance constraint. The improvement operators return a candidate move that does not involve any locations in the tabu list unless the move improves the best known solution, in which case the tabu condition is ignored as per the aspiration criterion [23].

1. Greedy (uncapacitated): Starts with an empty solution and adds one facility at a time, based on the minimal increase of the objective value.

2. Exchange (uncapacitated): For every pair of locations $i , j \in V _ { 2 }$ that are not in the tabu list, where i hosts a facility and j does not host a facility in the current solution, evaluates the result of moving the facility from i to j and selects the move that results in the best improvement (or least deterioration) of the objective value.

3. Add: For every location $i \in V _ { 2 }$ that does not host a facility, evaluates the result of locating a facility at i and selects a location that results in the best improvement (or least deterioration) of the objective value.

4. Remove: For every location $i \in V _ { 2 }$ that hosts a facility, evaluates the result of removing the facility at i and selects a location that results in the best improvement (or least deterioration) of the objective value.

For the capacitated case, the algorithm stores the allocations of the locations to the facilities, and computes the objective function based on the allocations. The locations allocated to a facility are kept as an ordered list, with the first element of each list being the location that hosts the facility. Consequently, exchanging or relocating this first element changes the location of the facility. In addition to the penalization described above, each violation of the capacity constraint is penalized.

1. Greedy (capacitated): Starts with an empty solution of lists and adds one location to one list at a time, either to the beginning of the list (as a facility) or to the end (as a location assigned to the facility). The location and the position it is added to are selected based on the minimal increase of the objective value.

2. Exchange (capacitated): For all locations $i , j \in V ,$ evaluates the result of exchanging the positions of i and j on their lists and returns the move that results in the best improvement (or the least deterioration) of the objective value.

3. Relocate: For all locations i ∈ V, evaluates the result of relocating i from its position on to another position and returns the move that results in the best improvement (or the least deterioration) of the objective value.

The algorithm is then: Algorithm 1. Tabu search.

capacitated p-median instances from ORLib. The only diferent algo rithmic parameter we changed was the tabu tenure limit, for which we have used τ = |V |/3. In line with the uncapacitated computational tests, the solver was run 10 times for each instance. The average results are reported in Table 2. The solver found the optimal solution value in all runs for all instances with $| V \mid = 5 0 ,$ and three instances with |V | = 100. The average deviation for the instances with $\vert V \ \vert = 1 0 0$ is 0.7%, hence we observe that the solver can also find high quality solutions for capacitated instances of p-median.

1: $\begin{array} { r } { \mathbf { i f } \sum _ { i \in V } q _ { i } \le Q _ { j } \forall j \in V _ { 1 } \cup V _ { 2 } } \end{array}$ then // uncapacitated 2: Invoke Greedy (uncapacitated) to construct an initial solution. 3: else // capacitated 4: Invoke Greedy (capacitated) to construct an initial solution 5: end if 6: Set the current solution as the best known solution. 7: Initialize the tabu list as an empty list of locations. 8: while time limit is not exceeded 9: $\begin{array} { r } { \mathbf { i f } \sum _ { i \in V } q _ { i } \le Q _ { j } \forall j \in V _ { 1 } \cup V _ { 2 } } \end{array}$ then $/ /$ uncapacitated 10: Invoke Exchange (uncapacitated) for the current solution. 11: if α = 0 then 12: Invoke Add and Remove for the current solution. 13: end if 14: else // capacitated 15: Invoke Exchange (capacitated) and Relocate for the current solution. 16: end if 17: Choose the best move among the candidates and perform it on the current solution. 18: Update the best known solution if a better solution is found 19: Add the locations in the move in the tabu list, with a tenure of 0. 20: Increment the tabu tenure of all locations in the tabu list. 21: Remove locations in the tabu list with a tenure greater than τ. 22: With probability ρ, remove all locations in the tabu list. 23: end while

## 4.3. Computational performance

We have performed our computational experiments using Excel 2016 on a computer with a 3.60 GHz Intel Core i7-7700 CPU and 16 GB of RAM. Although FLP Spreadsheet Solver can solve more than 16 variants of the FLP, we have opted to use the p-median instances available in ORLib [24], which have been widely used as a benchmark. Due to the inherent limitations of Excel and its built-in programming language VBA, we have attempted to solve the instances with up to 600 vertices. The CPU time limit was set to $9 \times | V |$ . Algorithmic parameters were chosen to be τ = m and $\rho = 0 . 0 0 5$ , default values of the solver based on pilot experimentation.

The solver was run 10 times for each instance, and the average results are reported in Table 1. The TS algorithm successfully finds the optimal solution in all 10 runs for 14 instances out of 30, and the overall average deviation is 0.23%. Hence, we conclude that the TS algorithm is capable of solving instances with up to 600 vertices to near optimality.

Since the uncapacitated and the capacitated solvers difer in terms of their local search operators, we have also tested the solver on

## 5. Case study: location of maternity healthcare services

In this section, we provide the details of our case study in healthcare. We first present a statistical analysis of the demand, and then proceed to the results obtained using FLP Spreadsheet Solver.

## 5.1. Background

Decisions around the provision and allocation of care services within a regional health service are multifaceted and often require a delicate balancing across a number of objectives. Operational Research is thus very suitable in providing insights and quantitative support to those tasked with making such decisions [25]. The support can take diferent shapes, from providing a practical quantitative analysis of the problem, to deciding on the metrics the decisions should be based upon, to the development and use of more advanced techniques such as optimization.

In this real-life case study, we were commissioned by an National Health Service (NHS) Trust to look into the provision and allocation of maternity services within a region in England. The collaborating organisation asked us to evaluate the model of service provision currently in use and to support, through quantitative and geographical analysis, decisions about opening, closing, and relocating the maternity service facilities. In many ways, this was the ideal case study to both illustrate the capability of the FLP Spreadsheet Solver to tackle real-world facility location problems and to provide advanced analytics support to an important strategic-level decision making process.

Table 1  
Computational results on p-median instances from ORLib.

<table><tr><td>Instance</td><td>|V|</td><td>m</td><td>CPU time (seconds)</td><td>Average result</td><td>Optimal solution value</td><td>Average deviation (%)</td></tr><tr><td>pmed1</td><td>100</td><td>5</td><td>900</td><td>5819</td><td>5819</td><td>0.00</td></tr><tr><td>pmed2</td><td>100</td><td>10</td><td>900</td><td>4105</td><td>4093</td><td>0.29</td></tr><tr><td>pmed3</td><td>100</td><td>10</td><td>900</td><td>4250</td><td>4250</td><td>0.00</td></tr><tr><td>pmed4</td><td>100</td><td>20</td><td>900</td><td>3046</td><td>3034</td><td>0.40</td></tr><tr><td>pmed5</td><td>100</td><td>33</td><td>900</td><td>1355</td><td>1355</td><td>0.00</td></tr><tr><td>pmed6</td><td>200</td><td>5</td><td>1800</td><td>7824</td><td>7824</td><td>0.00</td></tr><tr><td>pmed7</td><td>200</td><td>10</td><td>1800</td><td>5639</td><td>5631</td><td>0.14</td></tr><tr><td>pmed8</td><td>200</td><td>20</td><td>1800</td><td>4454</td><td>4445</td><td>0.20</td></tr><tr><td>pmed9</td><td>200</td><td>40</td><td>1800</td><td>2753</td><td>2734</td><td>0.69</td></tr><tr><td>pmed10</td><td>200</td><td>67</td><td>1800</td><td>1261</td><td>1255</td><td>0.48</td></tr><tr><td>pmed11</td><td>300</td><td>5</td><td>2700</td><td>7696</td><td>7696</td><td>0.00</td></tr><tr><td>pmed12</td><td>300</td><td>10</td><td>2700</td><td>6634</td><td>6634</td><td>0.00</td></tr><tr><td>pmed13</td><td>300</td><td>30</td><td>2700</td><td>4374</td><td>4374</td><td>0.00</td></tr><tr><td>pmed14</td><td>300</td><td>60</td><td>2700</td><td>2971</td><td>2968</td><td>0.10</td></tr><tr><td>pmed15</td><td>300</td><td>100</td><td>2700</td><td>1736</td><td>1729</td><td>0.40</td></tr><tr><td>pmed16</td><td>400</td><td>5</td><td>3600</td><td>8162</td><td>8162</td><td>0.00</td></tr><tr><td>pmed17</td><td>400</td><td>10</td><td>3600</td><td>6999</td><td>6999</td><td>0.00</td></tr><tr><td>pmed18</td><td>400</td><td>40</td><td>3600</td><td>4811</td><td>4809</td><td>0.04</td></tr><tr><td>pmed19</td><td>400</td><td>80</td><td>3600</td><td>2859</td><td>2845</td><td>0.49</td></tr><tr><td>pmed20</td><td>400</td><td>133</td><td>3600</td><td>1804</td><td>1789</td><td>0.84</td></tr><tr><td>pmed21</td><td>500</td><td>5</td><td>4500</td><td>9138</td><td>9138</td><td>0.00</td></tr><tr><td>pmed22</td><td>500</td><td>10</td><td>4500</td><td>8579</td><td>8579</td><td>0.00</td></tr><tr><td>pmed23</td><td>500</td><td>50</td><td>4500</td><td>4619</td><td>4619</td><td>0.00</td></tr><tr><td>pmed24</td><td>500</td><td>100</td><td>4500</td><td>2967</td><td>2961</td><td>0.20</td></tr><tr><td>pmed25</td><td>500</td><td>167</td><td>4500</td><td>1845</td><td>1828</td><td>0.93</td></tr><tr><td>pmed26</td><td>600</td><td>5</td><td>5400</td><td>9917</td><td>9917</td><td>0.00</td></tr><tr><td>pmed27</td><td>600</td><td>10</td><td>5400</td><td>8307</td><td>8307</td><td>0.00</td></tr><tr><td>pmed28</td><td>600</td><td>60</td><td>5400</td><td>4504</td><td>4498</td><td>0.13</td></tr><tr><td>pmed29</td><td>600</td><td>120</td><td>5400</td><td>3039</td><td>3033</td><td>0.20</td></tr><tr><td>pmed30</td><td>600</td><td>200</td><td>5400</td><td>2013</td><td>1989</td><td>1.21</td></tr></table>

Table 2  
Computational results on capacitated p-median instances from ORLib.

<table><tr><td>Instance</td><td>|V|</td><td>m</td><td>CPU time (seconds)</td><td>Average result</td><td>Optimal solution value</td><td>Average deviation (%)</td></tr><tr><td>pmedcap1</td><td>50</td><td>5</td><td>900</td><td>713</td><td>713</td><td>0.00</td></tr><tr><td>pmedcap2</td><td>50</td><td>5</td><td>900</td><td>740</td><td>740</td><td>0.00</td></tr><tr><td>pmedcap3</td><td>50</td><td>5</td><td>900</td><td>751</td><td>751</td><td>0.00</td></tr><tr><td>pmedcap4</td><td>50</td><td>5</td><td>900</td><td>651</td><td>651</td><td>0.00</td></tr><tr><td>pmedcap5</td><td>50</td><td>5</td><td>900</td><td>664</td><td>664</td><td>0.00</td></tr><tr><td>pmedcap6</td><td>50</td><td>5</td><td>900</td><td>778</td><td>778</td><td>0.00</td></tr><tr><td>pmedcap7</td><td>50</td><td>5</td><td>900</td><td>787</td><td>787</td><td>0.00</td></tr><tr><td>pmedcap8</td><td>50</td><td>5</td><td>900</td><td>820</td><td>820</td><td>0.00</td></tr><tr><td>pmedcap9</td><td>50</td><td>5</td><td>900</td><td>715</td><td>715</td><td>0.00</td></tr><tr><td>pmedcap10</td><td>50</td><td>5</td><td>900</td><td>832.9</td><td>829</td><td>0.47</td></tr><tr><td>pmedcap11</td><td>100</td><td>10</td><td>1800</td><td>1013.3</td><td>1006</td><td>0.73</td></tr><tr><td>pmedcap12</td><td>100</td><td>10</td><td>1800</td><td>966</td><td>966</td><td>0.00</td></tr><tr><td>pmedcap13</td><td>100</td><td>10</td><td>1800</td><td>1026</td><td>1026</td><td>0.00</td></tr><tr><td>pmedcap14</td><td>100</td><td>10</td><td>1800</td><td>1026</td><td>1026</td><td>0.00</td></tr><tr><td>pmedcap15</td><td>100</td><td>10</td><td>1800</td><td>1112.7</td><td>1091</td><td>1.99</td></tr><tr><td>pmedcap16</td><td>100</td><td>10</td><td>1800</td><td>954.2</td><td>954</td><td>0.02</td></tr><tr><td>pmedcap17</td><td>100</td><td>10</td><td>1800</td><td>1040.3</td><td>1034</td><td>0.61</td></tr><tr><td>pmedcap18</td><td>100</td><td>10</td><td>1800</td><td>1071.7</td><td>1043</td><td>2.75</td></tr><tr><td>pmedcap19</td><td>100</td><td>10</td><td>1800</td><td>1039.8</td><td>1031</td><td>0.85</td></tr><tr><td>pmedcap20</td><td>100</td><td>10</td><td>1800</td><td>1008.2</td><td>1005</td><td>0.32</td></tr></table>

Table 3  
Delivery outcome based on risk of pregnancy.

<table><tr><td>Delivery outcome</td><td>High risk</td><td>Low risk</td><td>Total</td></tr><tr><td>Live birth</td><td>1404 (18%)</td><td>6267 (82%)</td><td>7671</td></tr><tr><td>Stillbirth</td><td>8 (25%)</td><td>24 (75%)</td><td>32</td></tr><tr><td>Neonatal death</td><td>1 (50%)</td><td>1 (50%)</td><td>2</td></tr><tr><td>Unknown</td><td>2 (33%)</td><td>4 (67%)</td><td>6</td></tr><tr><td>Total</td><td>1415 (18%)</td><td>6296 (82%)</td><td>7711</td></tr></table>

Table 4  
Location of delivery.

<table><tr><td>Location</td><td>High risk</td><td>Low risk</td><td>Total</td></tr><tr><td>RUH</td><td>1258 (20%)</td><td>4817 (80%)</td><td>6301</td></tr><tr><td>Chippenham</td><td>34 (9%)</td><td>354 (91%)</td><td>388</td></tr><tr><td>Trowbridge</td><td>42 (11%)</td><td>350 (89%)</td><td>392</td></tr><tr><td>Paulton</td><td>12 (6%)</td><td>184 (94%)</td><td>196</td></tr><tr><td>Shepton Mallet</td><td>30 (7%)</td><td>378 (93%)</td><td>408</td></tr><tr><td>Home Birth</td><td>31 (14%)</td><td>195 (86%)</td><td>226</td></tr><tr><td>Other</td><td>8 (31%)</td><td>18 (69%)</td><td>26</td></tr><tr><td>Total</td><td>1415 (18%)</td><td>6296 (82%)</td><td>7711</td></tr></table>

## 5.2. Setting

The collaborating NHS Trust had recently acquired a number of maternity services within the region to provide a more integrated approach in their provision. As a result, the maternity service currently comprises an in-house facility at the Royal United Hospital (RUH) in addition to five maternity facilities in the community (Chippenham, Trowbridge, Paulton, Shepton Mallet, and Frome) that ofer a combination of prenatal, birthing and antenatal services, with the exception of Frome that does not ofer birthing.

We acquired data regarding all six facilities for the financial years 2015/16 and 2016/17 (01/04/2015–30 /03/2017) on bookings, scans, outpatient appointment, admissions, and deliveries. Meticulous data cleaning was performed on all datasets before embarking on statistical descriptive analysis as well as location analysis. For the purposes of this paper, we focus our analysis on deliveries and outpatient appointments.

During the two financial years of the analysis there were 7711 deliveries performed by the maternity services. The vast majority (98.76%) was a delivery of a single baby and 1.24% had multiple births (twins and triplets). Average mother age at the time they booked the delivery appointment was 30.1, ranging between 15 and 49, with a standard deviation of 5.6. Of all deliveries, 18.35% were classified as high-risk pregnancies and the remaining 81.65% as low risk. Of those deliveries 99.48% resulted in a live birth, Table 3. Further analysis using the Fisher's exact test indicated that there is no statistically significant diference ( p = 0.185) between the outcomes of delivery and the risk classification. We note that the risk classification of the pregnancy, according to expert guidance. is allocated at the initial stages of the pregnancy and is not revised during the gestation period.

![](/api/attachments/EHJ6U7U5/fulltext/images/d35dbf96c5560458c44ee8dc9b76210f56a5dba8e734ff1c85c792b4bcd2f335.jpg)  
Fig. 7. Distribution of number of appointments per unique service users.

![](/api/attachments/EHJ6U7U5/fulltext/images/0c20d1343e8a00fd1dfacb059b33856b17182310bfc811154f20e61c2ab315e4.jpg)  
Fig. 8. Cumulative frequency distribution of number of appointments by ser vice user.

Table 5  
Maternity service location of outpatient's appointments.

<table><tr><td>Location</td><td>Frequency</td><td>Percent (%)</td></tr><tr><td>RUH</td><td>64,595</td><td>30.28</td></tr><tr><td>Chippenham</td><td>52,686</td><td>24.70</td></tr><tr><td>Trowbridge</td><td>22,561</td><td>10.58</td></tr><tr><td>Paulton</td><td>20,326</td><td>9.53</td></tr><tr><td>Shepton Mallet</td><td>46,357</td><td>21.73</td></tr><tr><td>Frome</td><td>6764</td><td>3.17</td></tr><tr><td>Other</td><td>53</td><td>0.02</td></tr><tr><td>Total</td><td>213,342</td><td>100.00</td></tr></table>

Table 4 indicates that most of high-risk pregnancies took place in RUH although many take place in birthing centres or even home births. It is clear that most babies were delivered at RUH and Paulton had the smallest number of deliveries. Approximately 3% of all deliveries were home births.

Although location of delivery is dominated by RUH, a diferent picture emerges when it comes to prenatal and antenatal appointments. Not only are there a lot more such appointments (and unique service users), but also the distribution of workload across the diferent facilities is more dispersed. Specifically, during the two financial years under investigation there were 213,342 outpatient appointments managed by the maternity services. The appointments were made by 13,943 unique service users. The mean appointment number per service user was 15.30, ranging between 1 and 93, with a standard deviation of 10.13. Around 7% of service users had one appointment, 25% had at most 6 appointments and 50% of service users had at most 16 outpatients appointments. The most frequent service users had 40 or more appointments during the 2 years of the data, corresponding to 1.4% of all service users, as depicted in Fig. 7.

Fig. 8 indicates the cumulative frequency distribution of appointments by service users. It can be observed that service users with 10 or more appointments within the two years of the dataset account for approximately 65% of all appointments booked, as indicated by the vertical dashed line.

Outpatient appointments took place in all six maternity service locations. The most common facility was again RUH with almost one in three appointments (30.28%), followed by Chippenham with 24.70%. Smallest number of appointments was to Frome with 3.17%, Table 5.

As the above data analysis demonstrates, the high volume of out patient appointments to a number of community facilities in addition to the main facility located in RUH, necessitated a careful consideration of their location. Although planners may not be able to change completely the geographical distribution of the facilities at their disposal, any suggested reduction in the number of facilities may have an adverse impact on patient access and experience, as well as increased levels of trafic and emissions (over 100,000 journeys per year only for outpatient appointments). As stated by Dantas et al. [26], socio-economically deprived populations are less likely to attend hospital appointments, so it is important for any location analysis to take account of such considerations.

## 5.3. Geographical data and scenarios

The United Kingdom holds a census every 10 years, and the results are summarised in terms of Output Areas (OAs), which are geographical regions which contain approximately equal number of residents. Based on the census of 2011, each OA contains between 100 and 625 people, corresponding to 40 to 250 households. The OAs are aggregated into Lower Layer Super Output Areas (LSOAs) with 1000 to 3000 residents and further aggregated into Middle Layer Super Output Areas (MSOAs) with 5000 to 15,000 residents [27].

The demand data was aggregated at the level of MSOAs, which have an average population of 7200 in England and Wales. This method not only keeps the problem size at a manageable level, but also protects patient confidentiality. The region being analyzed consists of 123 MSOAs, their centroids at a maximum driving duration of 2 h from RUH, with the associated number of service users ranging from 1 to 268 within the two-year period.

To account for socio-economical factors, we have utilized the Index of Multiple Deprivation (IMD), a measure of relative deprivation for geographical areas [28]. It is a combined measure of deprivation based on a total of 37 separate indicators that have been grouped into seven domains, each of which reflects a diferent aspect of deprivation ex perienced by individuals living in an area. A higher value of IMD implies worse standards of living. IMD has been calculated for all MSOAs and has been made publicly available by [29].

Table 6  
Agreed scenarios for investigation.

<table><tr><td>Scenario number</td><td>Demand type</td><td>Scenario description</td></tr><tr><td>1</td><td>Deliveries</td><td>All deliveries (low and high risk), all facilities (existing locations)</td></tr><tr><td>2</td><td></td><td>Low risk deliveries, all facilities (existing locations), baseline for scenarios 3–9</td></tr><tr><td>3</td><td></td><td>Low risk deliveries, RUH plus 3 community facilities (among existing locations)</td></tr><tr><td>4</td><td></td><td>Low risk deliveries, RUH plus 2 community facilities (among existing locations)</td></tr><tr><td>5</td><td></td><td>Low risk deliveries, RUH plus 1 community facility (among existing locations)</td></tr><tr><td>6</td><td></td><td>Low risk deliveries, RUH plus 3 community facilities anywhere</td></tr><tr><td>7</td><td></td><td>Low risk deliveries, RUH plus 2 community facilities anywhere</td></tr><tr><td>8</td><td></td><td>Low risk deliveries, RUH plus 1 community facility anywhere</td></tr><tr><td>9</td><td></td><td>Low risk deliveries, RUH plus 1 community facility within inner city limits</td></tr><tr><td>10</td><td>Outpatients</td><td>All facilities (existing locations), baseline for scenarios 11–13</td></tr><tr><td>11</td><td></td><td>RUH plus 3 community facilities (among existing locations)</td></tr><tr><td>12</td><td></td><td>RUH plus 2 community facilities (among existing locations)</td></tr><tr><td>13</td><td></td><td>RUH plus 1 community facilities (among existing locations)</td></tr></table>

Table 7  
Results of FLP Spreadsheet Solver for scenarios investigating delivery facilities.

<table><tr><td>Scenario</td><td>Number of facilities</td><td>Facilities excluded</td><td>Estimated difference</td><td>Baseline</td></tr><tr><td>1</td><td>5</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>2</td><td>5</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>3</td><td>4</td><td>Paulton</td><td>15%</td><td>Scenario 2</td></tr><tr><td>4</td><td>3</td><td>Paulton, Shepton Mallet</td><td>37%</td><td>Scenario 2</td></tr><tr><td>5</td><td>2</td><td>Chippenham, Trowbridge, Paulton</td><td>76%</td><td>Scenario 2</td></tr><tr><td>6</td><td>4</td><td> $N/A^1$ </td><td>9%</td><td>Scenario 2</td></tr><tr><td>7</td><td>3</td><td> $N/A^1$ </td><td>34%</td><td>Scenario 2</td></tr><tr><td>8</td><td>2</td><td> $N/A^1$ </td><td>64%</td><td>Scenario 2</td></tr><tr><td>9</td><td>2</td><td> $N/A^1$ </td><td>105%</td><td>Scenario 2</td></tr></table>

<sup>1</sup> No facility is excluded in this scenario since the solver is not constrained by the location of existing facilities.

The obiective of the model was chosen as the minimization of the sum of the driving times from each MSOA to the closest facility, weighted (multiplied) by the historical demand as well as the IMD of the MSOA. Clearly, this objective function favors solutions in which the facilities are closer to the MSOAs with higher demand and higher IMDs. The objectives, parameters and scenarios of the location analysis were discussed between the modelling team and the stakeholders. As a result of this discussion. 12 scenarios were agreed upon. to form the basis of the location analysis, (see Table 6).

To enable the computational analysis, the following simplifications and assumptions were made:

1. In all of the scenarios explored, RUH was the only service which is to be retained at its original location and was not to be removed from the solution

2. The duration of the fastest driving route in minutes was used as the distance between two locations.

3. Calculations do not include any capacity considerations associated with each facility.

4. Each service user will be referred and indeed attend the facility that they are allocated to.

Due to the objective function, constant number of facilities, and the lack of a capacity constraint, the underlying FLP was identified as a p median problem.

Table 8  
Results of optimization modelling for scenarios investigating outpatients facil ities.

<table><tr><td>Scenario</td><td>Number of facilities</td><td>Facilities excluded</td><td>Estimated difference</td><td>Baseline</td></tr><tr><td>10</td><td>6</td><td>N/A</td><td></td><td></td></tr><tr><td>11</td><td>4</td><td>Paulton, Frome</td><td>20%</td><td>Scenario 10</td></tr><tr><td>12</td><td>3</td><td>Paulton, Shepton Mallet, Frome</td><td>39%</td><td>Scenario 10</td></tr><tr><td>13</td><td>2</td><td>Chippenham, Trowbridge, Paulton, Shepton Mallet</td><td>83%</td><td>Scenario 10</td></tr></table>

## 5.4. Results

FLP Spreadsheet Solver was used for computing travel times between the MSOAs and the facility location, finding a solution for each scenario as per the computational setup described in the previous section, and displaying the results. Table 7 shows the results for the scenarios for deliveries, where the ‘Estimated diference’ is computed as the ratio of the diference of the objective function value of the scenario and the objective function value for its baseline scenario, divided by the objective function value for the baseline scenario. Therefore, a larger estimated diference implies a worse outcome.

Through the experiments, we observed that in every scenario in which the number of facilities was reduced, the objective function value as estimated by the optimization algorithm is expected to increase, pointing towards longer travel durations. This is to be expected as service users, on average, would have to travel farther to access fewer facilities.

In the case of having four birthing facilities in total, Paulton was not part of the best known solution since the efect of excluding this facility (15%) was the smallest. Excluding either Shepton Mallet or Trowbridge resulted in an estimated increase of 22% each and Chippenham with 26%. When considering four birthing facilities in total located anywhere within the region (Scenario 6), existing locations seem to be well positioned (RUH, Chippenham, Trowbridge and Shepton Mallet). The locations of all facilities are displayed in Fig. 5.

In Scenario 4 with three facilities in total (RUH and two other facilities), excluding Paulton and Shepton Mallet from the best known solution is preferable to any other combination. This is because the pair was associated with the smallest estimated increase in the results (37%), with next closest combination being Chippenham and Paulton (41%). In the case of three birthing facilities in total located anywhere within the region, there is a minor diference between existing locations and choosing entirely new hypothetical locations for the two community facilities (Scenarios 4 and 7, 37% compared to 34%) indicating that existing facilities are relatively well placed.

Table 8 shows the results for the scenarios investigating outpatients, with the estimated diference calculated as described above. In terms of outpatient services (Scenarios 11 to 13), we observed monotonic increases of the estimated diference with every reduction in the number of community facilities. In the case of three community outpatient centres in total. Paulton and Frome were not part of the best known solution. In a two community centre configuration, the best known solution included Chippenham and Trowbridge and in the one com munity centre scenario, the best found solution pointed to Frome.

## 5.5. Discussion

Our results showed that in all scenarios in which the total number of facilities was reduced, the total adjusted travelling duration along the optimal routes was longer. This was in line with expectations as fewer facilities should lead to longer overall travel distances. The key messages we communicated to our collaborators were as follows:

1. In the case of having four birthing facilities in total (RUH and three in the community), existing facility locations seem to be well positioned. In this particular scenario, excluding the existing facility in Paulton ofers the best solution.

2. In the case of three birthing facilities (RUH and two in the community), there is a minor diference between existing locations and hypothetically choosing new locations, indicating that existing facilities are well placed. The best found solution in this case is achieved by excluding Paulton and Shepton Mallet from the configuration.

3. In terms of outpatient services, we observed monotonic increases in the results with every reduction in the number of community facilities. In the case of three community outpatients centres, Paulton and Frome were not part of the best known solution. In a two community centre configuration, the best found solution included Chippenham and Trowbridge and in the one community centre scenario the best found solution pointed to Trowbridge.

As of early 2019 and as part of an initiative to transform maternity service in the entire region, the Trust has decided to recommend reducing the total number of birthing facilities from five to three and have taken on board our findings (key message 2) by putting forward a configuration which includes the main hospital maternity centre and two additional community facilities. The configuration was in line with the experimental results, specifically Scenario 4, thus excluding facil ities Paulton and Shepton Mallet. The changes are currently the subject of a public consultation exercise that is being conducted within the regional health economy [30].

## 6. Concluding remarks

In this paper, we have introduced an open source, spreadsheetbased DSS for FLPs, which is capable of solving capacitated and distance constrained versions of the four basic FLPs: p-median, p -centre, MCLP, and UFLP. It can retrieve GIS data from a web service, and display the solutions on the backdrop of a map. Due to its accessibility and platform independence, it can be used for teaching and decision making in practice. Our computational results indicate that it can solve p-median problems with up to 600 vertices and 200 facilities to near optimality, as well as capacitated p-median problems with up to 100 vertices and 10 facilities.

We have also provided the details of a real-life case study arising in healthcare, which demonstrates the capabilities of the solver and its usability in practice. The associated analysis consists of solving a series of p-median problems with the objective function coeficients are computed using travel durations and an index of deprivation. The solver is observed to be efective in quick yet detailed analysis, and the results have been utilized by the collaborating NHS Trust. We conclude that FLP Spreadsheet Solver can be used in practice for solving FLPs, particularly in the field of humanitarian logistics.

## Acknowledgments

This study has been partially supported by the collaborating NHS Trust. The authors gratefully acknowledge this support. We also thank the two anonymous reviewers for their constructive comments that improved the paper.

## References

[1] G. Laporte, S. Nickel, F.S. da Gama, Location Science, vol. 528, Springer, 2015.

[2] G. Erdoğan, FLP Spreadsheet Solver, EURO Working Group on Vehicle Routing and Logistics, 2014 https://www.euro-online.org/websites/verolog/flp-spreadsheetsolver/.

[3] P.B. Keenan, P. Jankowski, Spatial decision support systems: three decades on, Decision Support Systems 116 (2019) 64–76.

[4] F. Schätter, O. Hansen, M. Wiens, F. Schultmann, A decision support methodology for a disaster-caused business continuity management. Decision Support Systems 118 (2019) 10–20.

[5] S.L. Hakimi, Optimum locations of switching centers and the absolute centers and medians of a graph, Operations Research 12 (3) (1964) 450–459.

[6] J.B. Pick, Ö. Türetken, A.V. Deokar. A. Sarkar. Location analytics and decision support: reflections on recent advancements, a research framework, and the path ahead. Decision Support Systems 99 (2017) 1–8.

[7] A. Ahmadi-Javid, P. Seyedi, S.S. Syam, A survey of healthcare facility location, Computers & Operations Research 79 (2017) 223–263.

[8] C. Toregas, R. Swain, C. ReVelle, L. Bergman, The location of emergency service facilities, Operations Research 19 (6) (1971) 1363–1373.

[9] R. Church, C. ReVelle, The maximal covering location problem, Papers of the Regional Science Association 32 (1) (1974) 101–118.

[10] M.S. Daskin, A maximum expected covering location model: formulation, propertie and heuristic solution, Transportation Science 17 (1) (1983) 48–70.

[11] G. Cornuejols, M. Fisher, G.L. Nemhauser, On the uncapacitated location problem, Annals of Discrete Mathematics vol 1. Flsevier, 1977 pp 163–177

[12] M.S. Daskin, SITATION facility location software, Department of Industrial Engineering and Management Sciences, Northwestern University, USA, 2002https://daskin.engin.umich.edu/software/.

[13] M. Munoz-Márquez, orloca: Operations Research LOCational Analysis Models Departamento de Matematicas, Departamento de Estadistica e Investigacion Operativa, Universidad de Cadiz, Spain, 2008https://CRAN.R-project.org/ package=orloca.

[14] J. Kalcsics, A. Butsch, R. Jürgens, Library of Location Algorithms, Institute of Operations Research, Karlsruhe Institute of Technology, Germany, 2011http://lola. ior.kit.edu/english/index.php.

[15] T.R. Rakes, J.K. Deane, L.P. Rees, G.M. Fetter, A decision support system for postdisaster interim housing, Decision Support Systems 66 (2014) 160–169.

[16] M. Karataş, N. Razi, M.M. Gunal, An ILP and simulation model to optimize search and rescue helicopter operations, Journal of the Operational Research Society 68 (11) (2017) 1335–1351

[17] K. KC, J. Corcoran, P. Chhetri, Spatial optimisation of fire service coverage: a case study of Brisbane. Australia. Geographical Research 56 (3) (2018) 270–284.

[18] H.K. Smith, J.P. Smith, D.K. Glencross, N. Cassim, L.M. Coetzee, S. Carmona, W. Stevens, Siting of HIV/AIDS diagnostic equipment in South Africa: a case study in locational analysis, International Transactions in Operational Research 25 (1) (2018) 319–336.

[19] M.M.H. Şeref, R.K. Ahuja, Spreadsheet-Based Decision Support Systems, Springe Berlin Heidelberg, Berlin, Heidelberg, 2008, pp. 277–298.

[20] G. Erdoğan, An open source spreadsheet solver for vehicle routing problems, Computers & Operations Research 84 (2017) 62–72

[21] M.D. Bailey, M. Nowak, MeetOpt: A multi-event coaching decision support system, Decision Support Systems 112 (2018) 60–75.

[22] M.D. Bailey, D. Michaels, An optimization-based DSS for student-to-teacher as signment: classroom heterogeneity and teacher performance measures, Decision Support Systems 119 (2019) 60–71.

[23] C. Blum, A. Roli, Metaheuristics in combinatorial optimization: overview and conceptual comparison, ACM computing surveys (CSUR) 35 (3) (2003) 268–308

[24] J.E. Beasley, ORLib-Operations Research Library, Department of Mathematica Sciences, Brunel University, London, UK, 2005http://people.brunel.ac.uk \~mastjjb/jeb/info.html.

[25] M. Pitt, T. Monks, S. Crowe, C. Vasilakis, Systems modelling and simulation in health service design, delivery and decision making, BMJ Ouality & Safety 25 (1) (2016) 38–45.

[26] L.F. Dantas, J.J. Fleck, F.L.C. Oliveira, S. Hamacher, No-shows in appointmen scheduling — a systematic literature review. Health Policy 122 (4) (2018) 412–421

[27] UK Ofice for National Statistics, 2011 census: population and household estimates for small areas in England and Wales, march 2011, https://www.ons.gov.uk peoplepopulationandcommunity/populationandmigration/populationestimates bulletins

2011censuspopulationandhouseholdestimatesforsmallareasinenglandandwales/ 2012-11-23, (2018) [Accessed: October 2018].

[28] UK Ministry of Housing, English indices of deprivation, https://www.gov.uk/ government/statistics/english-indices-of-deprivation-2015, (2015) [Accessed: October 2018].

[29] Public Heath England, IMD 2015 scores for English middle layer super output areas, http://webarchive.nationalarchives.goy.uk/20170106083511/http://www.apho org,uk/resource/item,aspx?RID = 184831. (2015) [Accessed: October 2018].

[30] Bath & North East Somerset, Swindon & Wiltshire Local Maternity System, Transforming maternity services together, http://www.transformingmaternity.org. uk/documents/BSW\_LMS\_Pre\_consultation\_business\_case.pdf, (2019) [Accessed: March 2019].

Dr Güneş Erdoğan is a Reader at the University of Bath, School of Management has been doing research on the applications of combinatorial optimization in logistics and healthcare for more than ten vears. He worked as a Research Specialist in an international software company for two years, in which he developed decision support systems for transportation operations for government institutions and hospitals. He was employed as a Postdoctoral Scholar by the Interuniversity Research Center on Enterprise Networks Logistics, and Transportation (CIRRELT, Montreal, Canada) for two years, where he further developed his modelling and research skills. Güneş has since held permanent faculty positions at University of Bath, University of Southampton, and Ozyegin University, Istanbul (as founding faculty). In 2010. he received the Kuhn Award from the journal Naval Research Logistics, on his paper entitled “Ambulance Location for Maximum Survival". He is the Transportation Area Editor for the journal Computers & Operations Research. He is a member of the Bath Centre for Healthcare Innovation & Improvement (CHI2) and the EURO Working Group on Vehicle Routing and Logistics Optimization.

Dr Neophytos Stylianou is currently a researcher with the Medical School of the University of Nicosia. He holds a visiting researcher position with the Centre for Healthcare Innovation and Improvement (CHI2). School of Management. University of Bath. He is also a tutor for the distance learning programme of Masters in Public Health at UNICAF. Neophytos has a PhD from the University of Manchester on Health Service Research/Epidemiology/Public Health. His PhD was looking at ways of informing the improvement of the specialized burn injury health service utilizing data. Neophytos holds an MPH from Imperial College London and a BSc in Biomedical Science from the University of Essex. He has worked as a biomedical scientist in a clinical laboratory, he had held a Research Assistant position at the Cyprus University of Technology, where he investigated the burden of family carers of dementia patients. He has worked as a Public Health Intelligence Analyst with Public Health England. He has also worked as a

Researcher-in-Residence, a collaboration between University of Bath and the Royal United Hospitals NHS Foundation Trust in Bath trying to provide solutions to real lif problems found in the hospital. His main research interest lies in using data for the improvement of health services, focusing on clinical epidemiology, prediction modellin and health policy evaluation

Prof Christos Vasilakis is Chair of Management Science, Deputy Head (Research) of the IDO Division, School of Management and Director, Bath Centre for Healthcare Innovation and Improvement (CHI2). Christos has an academic background in management, decision sciences and computer science and has held positions at various universities including UCL in London, St. George's University of London and the University of British Columbi in Canada. Before embarking on his academic career, he spent four years in industry as a software engineer and systems analyst. His research focuses on developing and putting in place modelling methods and analytical tools for assisting those delivering and managing health services. Recent work includes the implementation of a computer system to monitor surgical site infections at UCLH, assisting pharmacists at Imperial Healthcar NHS Trust to simulate the impact of changes to the dispensary process and work with Moorfields Eye Hospital to develop methods for predicting future demand and the likely impact of introducing new service designs. At Bath he has set up CHI2 and a number of research projects with regional NHS Trusts through the Researchers-in-Residence mode of collaboration.
