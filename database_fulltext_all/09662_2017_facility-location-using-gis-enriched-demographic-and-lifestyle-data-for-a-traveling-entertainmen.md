---
otero_id: 9662
otero_key: "BCKEWSH3"
title: "Facility location using GIS enriched demographic and lifestyle data for a traveling entertainment troupe in Bavaria, Germany"
authors: "Jeremy North; Fred L. Miller"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.05.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Facility location using GIS enriched demographic and lifestyle data for a traveling entertainment troupe in Bavaria, Germany

ELSEVIER Decision Support Systems

Jeremy W. North, Fred L. Miller

![](/api/attachments/BCKEWSH3/fulltext/images/21fea2de2fc7c962e89b2147793da46a033f8b211448376ca0e37111fe22911d.jpg)

PII: S0167-9236(17)30085-4

DOI: doi: 10.1016/j.dss.2017.05.007

Reference: DECSUP 12842

To appear in: Decision Support Systems

Received date: 19 September 2016

Revised date: 16 April 2017

Accepted date: 4 May 2017

Please cite this article as: Jeremy W. North, Fred L. Miller , Facility location using GIS enriched demographic and lifestyle data for a traveling entertainment troupe in Bavaria, Germany, Decision Support Systems (2016), doi: 10.1016/j.dss.2017.05.007

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# ACCEPTED MANUSCRIPT

# Facility Location Using GIS Enriched Demographic and Lifestyle Data for a Traveling Entertainment

Troupe in Bavaria, Germany

Jeremy W. North<sup>1</sup>, Fred L. Miller<sup>2</sup> College of Business Murray State University Murray, KY 42071 Phone: 314-809-6196 Fax: 314-809-3740 <sup>1</sup>jnorth@murraystate.edu, <sup>2</sup>fmiller@murraystate.edu

## ABSTRACT

This paper presents the development and subsequent application of a facility location methodology for selecting good show locations for a traveling entertainment troupe in Bavaria, Germany. The troupe is headquartered at a theater in Munich and wishes to expand its audience by offering traveling shows to select sites across Bavaria. A spatial analysis of the region is completed via classic location theory modeling techniques, leading to the development of a multi-criteria facility location approach for application. Additionally, we use location analytics techniques on demographic and consumer spending data extracted from the Business Analyst Web App (BAWA) system for each of the 95 districts in Bavaria. This data is integrated into a decision support system to weight consumer demand values with district lifestyle population patterns aggregated at the postal code level. Lifestyle-weighted demand is then used to identify locations that maximize the amount of customers within a given travel distance to a show while maintaining dispersion of selected facilities.

Keywords: Maximal Covering, Multi-criteria Facility Location; Dispersion; GIS

Facility Location Using GIS Enriched Demographic and Lifestyle Data for a Traveling Entertainment Troupe in Bavaria, Germany

## 1. Introduction

In Europe, entertainment troupes can usually be found conducting shows for the general public at a fee. These groups often cater exclusively to a cultural sub-region, providing spectacle with a local flair. Selecting where to play is the key decision required by traveling entertainment troupes. In this work, we develop a decision support system integrating location analytics and optimization modeling to select good show locations for a traveling entertainment troupe in Bavaria, Germany. The complexity and difficulty of these problems often necessitate the development of a decision support system, as seen in [3, 16, 21, 26, 27, 28, 29].

Facility location consists of selecting a subset of candidate sites and allocating demand to chosen locations. Optimization modeling techniques have been developed to address a wide variety of locationallocation problems [18]. The criteria pursued in these models can typically be categorized as being minisum, minimax, or covering [12]. In minisum problems, the objective is to minimize the weighted sum of customer to assigned facility distance. Minimax models seek to find a solution that minimizes the furthest distance between a customer and their assigned facility. In covering problems however, a maximum travel distance is defined, and location-allocation decisions are contingent upon the customers being within this “service level”. An in-depth coverage of this thriving research field can be found in the books by [8], [12], and [18].

Customers must travel to selected locations in the problem considered here. This important distinction necessitates direct consideration in our modeling approach. Since the entertainment troupe desires a high level of attendance, the primary goal sought in this work will be to maximize the amount of demand within a set travel distance, or covering. Coverage was also the criterion pursued in [9], a locationallocation approach to siting professional European football teams in Belgium. To the authors’ knowledge, this is the only other application of facility location modeling to select entertainment venues.

# ACCEPTED MANUSCRIPT

There are two general approaches in coverage modeling. Formalized in the seminal contribution by [31] in the context of facility location, the set covering location problem seeks to find the minimum amount of facilities required for a complete coverage of all customers. [6] established an alternative approach to coverage, where the objective is to maximize the amount of covered demand given a fixed number of facilities to locate (p). A key difference between these problems is that set covering doesn’t account for the magnitude of demand amongst customer regions. Population levels vary widely among the 95 districts in Bavaria, and a fixed number of show locations is to be selected. Therefore, we will seek to maximize the amount covered demand in our modeling approach. See [24] for a recent overview on the maximal covering facility location problem (MCLP), and [15] for a review of covering in location modeling.

Another important consideration in the problem given here is the potential cannibalization of demand amongst the selected show locations themselves. For this reason, troupe organizers do not want to schedule performances that are close together spatially. This establishes a secondary criterion in our problem, where we utilize the techniques of dispersion modeling in facility location [20]. The seminal work in [31] defines the problem as siting p facilities such that the distance between the two closest selected locations is maximized. An improved formulation for the problem was recently given in [30].

To estimate customer demand, [9] utilizes historical season ticket holder and attendance data in order to calculate a set of indices, from which covered demand sub-regions are partitioned into monopoly, monopolistic, and low attendance categories. In this work, we estimate potential attendance through location analytics techniques using the ESRI Business Analyst Web App (BAWA) [13] and a proprietary data set provided to the authors by Michael Bauer Research (MBR) [22] for the purposes of this study. Using these resources, demographic and consumer spending data for each district in Bavaria is extracted from information at postal code level. This data is integrated into a decision support system in order to weight consumer demand values according to lifestyle spending patterns at the district level. Lifestyleweighted demand is then used in the modeling methodology put forth here.

There are three contributions in this work. Firstly, we provide a decision support system applying location analytics and facility location modeling for regional entertainment site selection. Secondly, we develop and implement a multi-criteria optimization modeling approach for application on this problem. Lastly, we show a new way to estimate demand values for use in facility location modeling by incorporating real-world spending, demographic and lifestyle data. The next section gives our approach to followed by computational exercises in a spatial analysis, a case study application, and the conclusion with a discussion of future research.

## 2. Estimation of potential attendance

There is a wide variance of willingness to spend for live entertainment amongst diverse population segments. This important consideration is the impetus behind the application of location analytics technology to develop an accurate estimate of demand throughout all districts in Bavaria. Using information from BAWA, data concerning population and total and per capita recreational spending from each of Bavaria’s 95 districts was extracted. Additionally, in order to refine the accuracy of potential demand estimates, we utilize “International Consumers Styles” data furnished from MBR at the postal code level, which we aggregated to the district level. The lifestyle segments in the MBR system are given in Table 1 below.

## Table 1

Example percentage attendance by lifestyle segmentation

<table><tr><td>Lifestyle Type</td><td>Percent Attending</td></tr><tr><td>Type A: High Earning Urban Professionals</td><td>.9</td></tr><tr><td>Type B: Comfortable</td><td>.8</td></tr><tr><td>Type C: Modern and Pragmatic Over-50s</td><td>.65</td></tr><tr><td>Type D: Well Informed Modern Consumers</td><td>.7</td></tr><tr><td>Type E: Affluent Highly Educated Urban Families</td><td>.6</td></tr><tr><td>Type F: Security-oriented Seniors</td><td>.5</td></tr><tr><td>Type G: Orientation Seeking Lower and Middle Class Consumers</td><td>.4</td></tr><tr><td>Type H: Younger Lower and Middle Class Consumers</td><td>.45</td></tr><tr><td>Type I: Modern Younger Families</td><td>.35</td></tr><tr><td>Type J: Low-Income Younger Consumers</td><td>.5</td></tr></table>

Table 1 includes a column labelled “Percent Attending”. This value is based on an analysis of internal audience cultural spending data. This percent attending value is the proportion of each segment’s population apt to seek the type of live theatrical entertainment offered by this troupe, and can vary from district to district. Using these weights, lifestyle-segmented weighted population values are calculated $( h _ { i } )$ and used as estimates of potential demand per district in our optimization models. With lifestyle segments indexed by $k \in k$ and districts indexed by $i \in I ,$ , this is calculated as follows:

$$
h _ {i} = \sum_ {k} s _ {k i} a _ {k i} \quad \forall i \in I
$$

where $s _ { k i }$ and $a _ { k i }$ are the percent attending and the population estimations of lifestyle segment in district respectively.

It is important to note that this estimation can and will vary amongst all lifestyle segments based on the type of live entertainment in question. For example, Type J consumers are going to be much more likely than Type A consumers to attend live popular music performances due to lifestyle differences. Our approach implicitly incorporates these lifestyle-based preferences amongst sects of a population. Additionally, the size of these lifestyle subpopulations differ from region to region, a fact that our approach incorporates as well.

## 3. Model Formulations

In our optimizations, we use travel distances given by our geographic information system (GIS), with the centroid of each district modeled as both candidate facility locations $( j \in J )$ and customer regions or points of demand $( i \in I )$ . Using these sets, we define the following additional notation: $t _ { i j } =$ travel time between demand point $i \in I$ and candidate facility location $j \in J$ $a _ { i j } = \left\{ { \begin{array} { l l } { 1 { \mathrm { ~ i f ~ } } t _ { i j } \leq t _ { c } } \\ { 0 { \mathrm { ~ o t h e r w i s e } } } \end{array} } \right.$ , where $t _ { c }$ is the maximum travel time for coverage

p = number of facilities to open

$$
X _ {j} = \left\{ \begin{array}{l} 1 \text {if a facility is opened at candidate site j} \\ 0 \text {otherwise} \end{array} \right.
$$

$$
Y _ {i} = \left\{ \begin{array}{l} 1 \text {if demand i is covered} \\ 0 \text {otherwise} \end{array} \right.
$$

With this notation, the MCLP $( P _ { 1 } )$ is formulated below.

$$
\left(P _ {1}\right) \text {Maximize} Z _ {1} = \sum_ {i \in I} h _ {i} Y _ {i}\tag{1}
$$

s.t.

$$
Y _ {i} \leq \sum_ {j \in J} a _ {i j} X _ {j}
$$

$$
\forall i \in I\tag{2}
$$

$$
\sum_ {j \in J} X _ {j} = p\tag{3}
$$

$$
X _ {j} \in \{0, 1 \}
$$

$$
\forall j \in J\tag{4}
$$

$$
Y _ {i} \in \{0, 1 \}
$$

$$
\forall i \in I\tag{5}
$$

The objective of $P _ { 1 }$ is to maximize the total amount of covered demand (1), given a coverage travel time $( t _ { c } )$ and amount of facilities to locate (3). Constraints (2) disallow coverage $( Y _ { i } = 1 )$ ) of demand $i \in I$ when a selected facility is not close enough. Binary restrictions on the decision variables are given by (4) and (5). To conduct a spatial analysis of Bavaria (section 4), we solve $P _ { 1 }$ with several configurations of coverage distance and number of facilities to locate. It was given by the entertainment troupe that the maximum travel time for a customer to attend a show should be no more than one hour. In this work, we examine coverage travel times of 30, 45, and 60 minutes, as provided by GIS-estimated road travel distances in the region.

Before presenting the modeling approach created for application in this paper, we give the classic formulation for the p-dispersion facility location problem $( P _ { 2 } )$ .

We define the following additional notation to formulate problem $P _ { 2 }$ :

$$
M = \max _ {i \in I, j \in J} \{d _ {i j} \}
$$

## D = minimum distance between two selected facilities

With this additional notation, the p-dispersion problem $( P _ { 2 } )$ is formulated below.

(P2) Maximize $Z _ { 2 } = D$

(6)

s.t.

$$
D \leq d _ {i j} + (M - d _ {i j}) (1 - X _ {i}) + (M - d _ {i j}) (1 - X _ {j}) \quad \forall i, j \in J, i <   j\tag{7}
$$

$$
\sum_ {j \in J} X _ {j} = p\tag{3}
$$

$$
X _ {j} \in \{0, 1 \}
$$

$$
\forall j \in J\tag{4}
$$

$$
0 \leq D \leq M\tag{8}
$$

The objective of $P _ { 2 }$ is to maximize the distance between the two closest selected facilities (6).

Constraints (7) set the dispersion variable ( ) to the distance between the two nearest open facilities, with bounds on this decision variable set by (8).

In addition to examining coverage versus the amount of facilities to locate $( t _ { c } , p )$ , our spatial analysis must include the performance of facility dispersion across the service region. As a result of this effort, it became clear that multiple optimal solutions exist in our problem for many configurations of $( t _ { c } , p )$ . This is not an unexpected finding, as it is well known that multiple optimality is a common characteristic of many applications of coverage modeling, as pointed out relatively recently in [32]. The presence of multiple optimal solutions led to the development of a multi-criteria modeling approach for this problem, where we consider both maximal covering (given $t _ { c }$ and ) and dispersion when selecting show locations.

Ours isn’t the first approach to take advantage of the presence of multiple optimality in coverage facility location modeling. [7] present the MCLP with mandatory closeness constraints, where a maximal covering is sought for coverage distance $d _ { c }$ , and complete coverage is enforced at coverage level $( d _ { c } ^ { \prime } > d _ { c } )$ . In [1], the authors capitalize on the presence of multiple optimal solutions in the MCLP by employing optimization-based approaches to find a set of solutions for application in a nature reserve site selection problem, from which the decision makers select the most preferred.

There are some key works in the literature that should also be mentioned here that explore the incorporation of dispersion or distance restrictions within coverage-based and/or minisum models. [25] give the -median impact problem (PMIP), which considers population impact in undesirable facility location by preventing more than one facility to be located within a specified distance of any population center. The minimum weighted covering location problem (MCLPDC) is provided in [4]. In the MCLPDC, the amount of demand covered is minimized with additional restrictions disallowing open facilities to be closer than a specified distance. [2] et al. evaluate the -median objective performance when dispersion, population, and/or equity criteria are pursued. They show that good performance on a median objective can be obtained in these models. [23] provides a thorough examination of distancebased restrictions in location modeling, and a recent survey of multi-criteria facility location is given in [14].

In the problem presented in this paper, maximal covering takes precedence over dispersion of show locations. However, the traveling entertainment troupe desires consideration of both criteria. See figure 1 for an example illustration of the effects of multiple optimality in this scenario.

Maximal Covering  
![](/api/attachments/BCKEWSH3/fulltext/images/f36e4910f68dca6326f534c5266bb431180ada277bdc309170add160041623f8.jpg)  
Figure 1: Multiple Optimality in Maximal Covering

Maximal Covering → Max Dispersion  
![](/api/attachments/BCKEWSH3/fulltext/images/e7420381cef37c141e0fd0fc650c7181053d9de12ef8cb74cdf2fb58f241bb35.jpg)

# ACCEPTED MANUSCRIPT

A myopic pursuit of maximal covering resulted in the outcome on the left in figure 1. However, a better solution exists, as depicted in the illustration on the right in figure 1, where the $p = 6$ selected facilities are more dispersed $( D _ { 2 } > D _ { 1 } )$ . We exploit the presence of multiple optimal solutions to the MCLP in our problem by formulating and solving a bi-objective optimization model $( P _ { 3 } )$ . To formulate $P _ { 3 } ,$ , we define an additional slack variable $( s _ { i } )$ and a penalty parameter $\left( \mu _ { i } \right)$ . With this notation, a location problem (PDMCLP) is given below.

(P3) Maximize $\begin{array} { r } { Z _ { 3 } = D + \sum _ { i \in I } \mu _ { i } s _ { i } } \end{array}$

(9)

s.t.

$$
\sum_ {i \in I} h _ {i} Y _ {i} + s _ {i} \geq Z _ {1} ^ {*}\tag{10}
$$

$$
D \leq d _ {i j} + (M - d _ {i j}) (1 - X _ {i}) + (M - d _ {i j}) (1 - X _ {j}) \quad \forall i, j \in J, i <   j\tag{7}
$$

$$
Y _ {i} \leq \sum_ {j \in J} a _ {i j} X _ {j}
$$

$$
\forall i \in I\tag{2}
$$

$$
\sum_ {j \in J} X _ {j} = p\tag{3}
$$

$$
0 \leq D \leq M\tag{8}
$$

$$
X _ {j} \in \{0, 1 \}
$$

$$
\forall j \in J\tag{4}
$$

$$
Y _ {i} \in \{0, 1 \}
$$

$$
\forall i \in I\tag{5}
$$

In $P _ { 3 }$ , we are maximizing the dispersion of selected facilities (9) as in $P _ { 2 }$ . However, we do so subject to a minimum performance on maximal covering (10), with constraint sets (2) – (5), (7), and (8) enforcing their previously described restrictions.

In this problem, we are seeking a maximal value for given a required performance level of maximal covering $( P _ { 1 } )$ , as dictated by $Z _ { 1 } ^ { * }$ . The method of elastic constraints is a premier solution method for multicriteria optimization problems as it combines the strengths of the well-known ɛ-constraint and weighted sum solution methods. In other words, it is relatively easier to solve (weighted sum) and can be deployed to discover the entire set of non-dominated points (ɛ-constraint). The incorporation of slack variables in this fashion allows upper bounds violations on constrained objectives at a penalty [11]. In our implementation, the Pareto frontier is discovered in a re-optimization procedure, iteratively perturbing from a starting value equaling the coverage performance found in the solution to $P _ { 2 }$ , up to the value found in the solution to $P _ { 1 }$

We discovered in computational testing that a slight degradation of performance in covering can result in a significant improvement in dispersion for our problem. This finding ultimately led to the abandonment of a purely lexicographic optimization $\left( \operatorname* { m a x } _ { D } \left\{ \operatorname* { m a x } _ { X _ { j } , Y _ { i } } { P _ { 1 } } \right\} \right)$ in favor of the employment of multi-criteria decision making techniques for a solution approach. Section 4 details this discovery through the employment of $( P _ { 3 } ^ { \prime } )$ , a simplification of $P _ { 3 }$ where (9) and (10) are replaced as follows:

$( P _ { 3 } ^ { \prime } )$ Maximize $Z _ { 3 } = D$

(11)

s.t. (2)-(5), (7), (8)

$$
\sum_ {i \in I} h _ {i} Y _ {i} \geq \lambda Z _ {1} ^ {*}\tag{12}
$$

Other potential applications of the PDMCLP could be in the area of military defense or security. For example, one might explore its application in the siting of quick reactionary forces in a hostile combat zone or missile defense systems. Another area where this modeling approach could prove useful is in the siting of a set of brick-and-mortar retail locations or stores throughout a city, where it is desired to be within close proximity to customer regions while dispersing open facilities.

## 4. Spatial Analysis

Computational experiments were done on a 3.2 GHz PC with 8.00 GB of RAM using the Gurobi 6.5 solver for MILPs [17]. The Julia programming language was used to code our optimizations [19].

# ACCEPTED MANUSCRIPT

A spatial analysis of the 95 districts in Bavaria was conducted by solving $P _ { 1 }$ and $P _ { 3 } ^ { \prime }$ with varying coverage distances (travel times) and amounts of facilities to locate. In this analysis, we consider values of 30, 45, and 60 for coverage travel times $( t _ { c } )$ in minutes. In each scenario, the number of facilities to locate will vary from 2 up to 10, which is the amount of facilities needed to attain complete coverage at a maximum travel time of 60 minutes. Additionally, the location variable for Munich was fixed at one $( X _ { M u n i c h } = 1 )$ for this analysis. For the purposes of results discussion, an instance will henceforth be referred to with the tuple $\left( t _ { c } , p \right)$ . Table 2 below show the results employing models $P _ { 1 }$ and $P _ { 3 } ^ { \prime }$ with a covering travel time of 30 minutes.

Table 2: Spatial Analysis Results: Coverage = 30 Minutes Travel Time

<table><tr><td> $(t_c,p)$ </td><td>Covered  $(P_1,P_3')$ </td><td>Dispersion  $(P_3',\lambda = 1)$ </td><td>Covered  $(P_3',\lambda = .99)$ </td><td>Dispersion  $(P_3',\lambda = .99)$ </td></tr><tr><td>(30,2)</td><td>27.04%</td><td>107</td><td>26.93%</td><td>119</td></tr><tr><td>(30,3)*</td><td>32.20%</td><td>53</td><td>32.20%</td><td>53</td></tr><tr><td>(30,4)*</td><td>35.40%</td><td>53</td><td>35.40%</td><td>53</td></tr><tr><td>(30,5)*</td><td>38.37%</td><td>53</td><td>38.37%</td><td>53</td></tr><tr><td>(30,6)*</td><td>41.33%</td><td>53</td><td>41.33%</td><td>53</td></tr><tr><td>(30,7)</td><td>44.09%</td><td>48</td><td>43.88%</td><td>53</td></tr><tr><td>(30,8)</td><td>46.74%</td><td>48</td><td>46.40%</td><td>53</td></tr><tr><td>(30,9)*</td><td>49.16%</td><td>48</td><td>49.16%</td><td>48</td></tr><tr><td>(30,10)</td><td>51.34%</td><td>26</td><td>51.10%</td><td>48</td></tr></table>

With 30 minutes travel time establishing the coverage radius, it takes 55 facilities to effect a complete coverage of the 95 districts in Bavaria. In table 2, the “Covered $( P _ { 1 } , P _ { 3 } ^ { \prime } ) ^ { \ ' }$ and Covered $( P _ { 3 } ^ { \prime } , \lambda = . 9 9 )$ columns gives the maximal covering values expressed as a percentage of total demand in Bavaria. The “Dispersion $( P _ { 3 } ^ { \prime } , \lambda = \# ) ^ { : }$ ” columns give the performance on the dispersion metric across both models. We notice that when $\lambda = . 9 9$ , significant improvements occur at a negligible decrease in coverage on the dispersion metric throughout the region in four out of nine instances.

The traveling entertainment troupe desires the consideration of five or six show locations, which provides coverage of roughly 38% to 41% of the potential customers in the region, as seen in table 2. A maximum reasonable travel time of 1 hour was given by troupe organizers, so coverage contingent upon travel times of both 45 and 60 minutes were evaluated as well. See table 3 for the spatial analysis results using a coverage of 45 minutes.

Table 3: Spatial Analysis Results: Coverage = 45 Minutes Travel Time

<table><tr><td> $(t_c, p)$ </td><td>Covered  $(P_1, P_3')$ </td><td>Dispersion  $(P_3', \lambda = 1)$ </td><td>Covered  $(P_3', \lambda = .99)$ </td><td>Dispersion  $(P_3', \lambda = .99)$ </td></tr><tr><td>(45, 2)</td><td>39.76%</td><td>119</td><td>39.43%</td><td>122</td></tr><tr><td>(45, 3)*</td><td>47.45%</td><td>97</td><td>47.45%</td><td>97</td></tr><tr><td>(45, 4)*</td><td>55.11%</td><td>64</td><td>55.11%</td><td>64</td></tr><tr><td>(45, 5)*</td><td>61.85%</td><td>64</td><td>61.85%</td><td>64</td></tr><tr><td>(45, 6)</td><td>66.94%</td><td>64</td><td>66.61%</td><td>76</td></tr><tr><td>(45, 7)</td><td>71.79%</td><td>64</td><td>71.70%</td><td>76</td></tr><tr><td>(45, 8)</td><td>76.28%</td><td>64</td><td>76.19%</td><td>76</td></tr><tr><td>(45, 9)</td><td>80.39%</td><td>64</td><td>79.60%</td><td>76</td></tr><tr><td>(45, 9)</td><td>84.27%</td><td>61</td><td>83.53%</td><td>76</td></tr></table>

In table 3, it is shown that significant improvements in the dispersion metric can be seen at negligible decreases in coverage. This holds for all configurations except for (45, 3), (45, 4), and (45, 5). Additionally, slight improvements in dispersion were occasionally discovered throughout our computational testing with zero degradation of coverage performance due to the presence of multiple optimal solutions in this problem (as suggested in figure 1). Interestingly, this property didn’t manifest until examinations of covering travel times of at least 45 minutes. The results for coverage based upon a maximum travel time of one hour is given in table 4.

Table 4: Spatial Analysis Results: Coverage = 60 Minutes Travel Time

<table><tr><td> $(t_c, p)$ </td><td>Covered  $(P_1, P_3')$ </td><td>Dispersion  $(P_3', \lambda = 1)$ </td><td>Covered  $(P_3', \lambda = .99)$ </td><td>Dispersion  $(P_3', \lambda = .99)$ </td></tr><tr><td>(60, 2)*</td><td>58.56%</td><td>122</td><td>58.56%</td><td>122</td></tr><tr><td>(60, 3)*</td><td>68.73%</td><td>95</td><td>68.73%</td><td>95</td></tr><tr><td>(60, 4)*</td><td>76.40%</td><td>95</td><td>76.40%</td><td>95</td></tr><tr><td>(60, 5)*</td><td>83.73%</td><td>92</td><td>83.02%</td><td>92</td></tr><tr><td>(60, 6)</td><td>89.34%</td><td>84</td><td>88.56%</td><td>92</td></tr><tr><td>(60, 7)</td><td>94.56%</td><td>63</td><td>93.64%</td><td>84</td></tr><tr><td>(60, 8)</td><td>97.16%</td><td>77</td><td>96.75%</td><td>84</td></tr><tr><td>(60, 9)</td><td>99.44%</td><td>71</td><td>98.66%</td><td>77</td></tr><tr><td>(60, 10)</td><td>100.00%</td><td>76</td><td>99.28%</td><td>77</td></tr></table>

Table 4 shows once again that significant improvements in dispersion is attainable at a negligible decrease in coverage. When coverage travel time is 60 minutes, the instances where this wasn’t the case are (60, 2), (60, 3), (60, 4), (60, 5). Objective performance as the number of facilities change can be seen in figures 2 & 3 for a coverage travel time of 60 minutes.

![](/api/attachments/BCKEWSH3/fulltext/images/507c1d8d2169a5d32b4f5750583804f77ba35bd7b16f8eabe5631b2ab3c7b576.jpg)  
Figure 2: Decreasing Marginal Improvement of Coverage

Figure 2 shows an expected decreasing marginal improvement of coverage as the number of facilities located increases.

![](/api/attachments/BCKEWSH3/fulltext/images/fdd56310c1b441d0fb31a7e19fe9b161977c56c56d66bf84416fbf85c14c3641.jpg)  
Figure 3: Change in Dispersion as Facilities Located Increase

Dispersion generally decreases as the number of facilities located increases in our problem, as depicted in figure 3. However, dispersion is not monotonically decreasing as the number of facilities increase in our models. This is due in part to a heavy focus on maximal covering in our modeling approach. The properties shown in figure 2 and figure 3 are present at all coverage travel times considered in this analysis.

When examining these results across all coverage distances evaluated, we conclude that improvements in dispersion tend to get larger as the number of facilities to locate increases, and an improvement dispersion is often possible at a slight “cost” of performance in maximal co vering. Additionally, alternate optimal solutions are often present, favoring the pursuit of secondary, additional criteria. Our multi-criteria application is given next in section 5.

## 5. Application

In the spatial analysis of this problem, it was discovered that roughly 90% of Bavaria can be within a 60 minute drive time of a show if the number of locations to select (p) is six. Additionally, the closest distance between any two shows would be approximately 84 miles. Based upon these findings, it was decided that the traveling entertainment troupe would host six shows a week across Bavaria. Table 5 below show the lexicographic optimization approach $( P _ { 3 } ^ { \prime } , \lambda = 1 )$ with a coverage distance given by a 60 minute drive time and $p = 6$

<table><tr><td colspan="3">Table 5:  $P_{3}^{\prime}$ , Coverage = 60 Minutes Travel Time, p = 6</td></tr><tr><td> $(t_{c}, p)$ </td><td>Covered ( $P_{3}^{\prime}$ )</td><td>Dispersion ( $P_{3}^{\prime}, \lambda = 1$ )</td></tr><tr><td>(60, 6)</td><td>89.34%</td><td>84</td></tr></table>

The selected districts to host shows for this solution are Munich, Traunstein, Straubing-Bogen, Roth, Schweinfurt, and Neu-Ulm. Figure 4 is a representation of this solution using ESRI software.

# ACCEPTED MANUSCRIPT

![](/api/attachments/BCKEWSH3/fulltext/images/3c572e0e1bfd51669003547e569d589370aa10489df6c165edd28659d1aa6698.jpg)  
Figure 4: Selected Locations and Coverage of the 95 Districts of Bavaria using $( P _ { 3 } ^ { \prime } , \lambda = 1 )$

In figure 4 above, the proposed show locations are represented with blue diamonds, and the coverage borders for each selected district accurately capture road travel distance. Table 6 below show the multicriteria application results of our PDMCLP model $( P _ { 3 } )$

Table 6: $P _ { 3 } ,$ Coverage = 60 Minutes Travel Time, $p = 6$

<table><tr><td>Solution Number</td><td>Coverage</td><td>Dispersion</td></tr><tr><td>1</td><td>69.31%</td><td>116</td></tr><tr><td>2</td><td>71.77%</td><td>115</td></tr><tr><td>3</td><td>73.51%</td><td>113</td></tr><tr><td>4</td><td>74.61%</td><td>111</td></tr><tr><td>5</td><td>75.10%</td><td>110</td></tr><tr><td>6</td><td>75.52%</td><td>108</td></tr><tr><td>7</td><td>75.92%</td><td>107</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td>8</td><td>76.02%</td><td>106</td></tr><tr><td>9</td><td>76.63%</td><td>105</td></tr><tr><td>10</td><td>76.71%</td><td>104</td></tr><tr><td>11</td><td>76.91%</td><td>103</td></tr><tr><td>12</td><td>80.68%</td><td>101</td></tr><tr><td>13</td><td>83.97%</td><td>100</td></tr><tr><td>14</td><td>84.18%</td><td>96</td></tr><tr><td>15</td><td>87.56%</td><td>95</td></tr><tr><td>16</td><td>88.56%</td><td>92</td></tr><tr><td>17</td><td>88.58%</td><td>88</td></tr><tr><td>18</td><td>89.34%</td><td>84</td></tr></table>

Table 6 shows the non-dominated set when p = 6 and covering travel time is 60 minutes. Solution number 16 was selected as the chosen solution because a 9.52% improvement in dispersion is attainable at less than 1% decrease in performance of coverage from the maximal covering value of 89.34%. The Pareto frontier for this application can be seen in figure 5.

![](/api/attachments/BCKEWSH3/fulltext/images/bea7b03a7c2e2daa5a6b52b4acabb21356256838daba6dc6fb0a204f19f92164.jpg)  
Figure 5: Pareto Efficient Solutions (Coverage = 60 Minutes Travel Time, p = 6)

The selected districts to host shows for the chosen solution are Munich, Tirschenreuth, Straubing-Bogen, Roth, Schweinfurt, and Neu-Ulm. This solution is depicted in Figure 6 below.

![](/api/attachments/BCKEWSH3/fulltext/images/ef92bd07565f25d45a541a7078d3ee9aa3daa4c947834d59034f3ec84843c5a6.jpg)  
Figure 6: Selected Locations and Coverage of the 95 Districts of Bavaria using $P _ { 3 }$

When comparing figures 5 and 6, it is apparent that the key difference is that the show offered in the southeast section of Bavaria (Traunstein in figure 5) is instead moved to the northeast section of Bavaria (Tirschenreuth in figure 6) for better dispersion.

Lastly, with these six districts chosen, a final site selection process must be completed. Each of the 95 districts of Bavaria, to include the ones selected by troupe organizers, feature multiple venues. Troupe organizers will consider the appeal each venue has comparatively at the five districts to host entertainment shows outside of Munich. Negotiations between troupe organizers and city officials and/or venue owners ultimately determine the site within these districts that shows will take place.

# ACCEPTED MANUSCRIPT

## 6. Conclusion

This paper presents the development and subsequent application of a facility location methodology for selecting good show locations for a traveling entertainment troupe in Bavaria, Germany. A spatial analysis of the region was completed via classic location theory modeling techniques, leading to the development and application of a multi-criteria facility location model we call the p-dispersed maximal covering facility location problem (PDMCLP). Location analytics techniques were also applied in the stimations of potential demand for a traveling, theatrical entertainment troupe in Bavaria, Germany. This data was incorporated into a decision support system that maximizes the amount of demand within a given travel distance to a show, while maintaining dispersion of selected show locations.

The methodology derived and implemented in this paper presents an integration of the vast amount of data available in GIS software like ESRI into an operations research-based approach to facility location. We believe that this is a largely unexplored area in the field, and that much work is left to be done on both private and public sector applications. In today’s “big data” world, application-specific decision support systems for facility location problems should incorporate as much pertinent information as possible. Only through the incorporation and utilization of data repositories available from organizations like MBR can this be achieved.

Another area of future research is to further explore the characteristics of the PDMCLP and its potential application in other decision areas. These decision areas can include but are not limited those that are security and/or military in nature, or retail location problems. Potential military applications include QRF or quick reactionary forces site selection in combat zones, missile defense location, or region districting for unmanned aerial vehicle deployment. In retail location problems, we believe that the data available in software like BAWA can be utilized with great success in conjunction with more sophisticated facility location methodologies from the management sciences/operations research disciplines.

## References

## ACCEPTED MANUSCRIPT

[1] J.L. Arthur, M. Hachey, K. Sahr, M. Huso, A.R. Kiester, Finding all optimal solutions to the reserve site selection problem: formulation and computational analysis, Environmental and Ecological Statistics 4 (1997) 153-165.

[2] R. Batta, M. Lejeune, S. Prasad, Public facility location using dispersion, population, and equity criteria, European Journal of Operational Research 234 (2014) 819-829.

[3] J. Belien,, L. De Boeck, J. Colpaert, S. Devesse, F. Van den Bossche, Optimizing the facility location design of organ transplant centers, Decision Support Systems 54 (2013) 1568-1579.

[4] O. Berman, R. Huang, The minimum weighted covering location problem with distance constraints, Computers & Operations Research 35 (2008) 356-372.

[5] J. Bezanson, S. Karpinski, V.B. Shah, A. Edelman, Julia: a fast dynamic language for technical computing, 2012, http://arxiv.org/abs/1209.5145 accessed June 20, 2016.

[6] R. Church, C. ReVelle, The maximal covering location problem, Papers in Regional Science 32 (1974) 101-118.

[7] R. Church, C. ReVelle, Theoretical and computational links between the p-median, location setcovering, and the maximal covering location problem, Geographical Analysis 8 (1976) 406-415.

[8] M.S. Daskin, Network and Discrete Location: Models, Algorithms and Applications, 2<sup>nd</sup> edn., Wiley, 2013.

[9] T. Dejonghe, Restructuring the Belgian professional football league: a location-allocation solution, in Tijdschrift voor Economische en Sociale Geografie, Royal Dutch Geographical Society KNAG 95 (2004) 73-88.

[10] M. Ehrgott, Multicriteria Optimization, 2<sup>nd</sup> edn., Springer 2005.

[11] M. Ehrgott, A discussion of scalarization techniques for multiple objective integer programming, Annals of Operations Research 147 (2006) 343-360.

[12] H.A. Eiselt, V. Marianov (Eds.), Foundations of Location Analysis, Springer, 2011.

[13] ESRI 2016, Business analyst online, ArcGIS Desktop: Release 10. Redlands, CA: Environmental Systems Research Institute.

[14] R.Z. Farahani, M. SteadieSeifi, N. Asgari, Multiple criteria facility location problems: A survey, Applied Mathematical Modeling 34 (2010) 1689-1709.

[15] R.Z. Farahani, N. Asgari, N. Heidari, M. Hosseininia, M. Goh, Covering problems in facility location: a review, Computers & industrial engineering 62 (2012) 368-407.

[16] S. Fernandes, M.E. Captivo, J. Climaco, A DSS for bicriteria location problems, Decision Support Systems 57 (2014) 224-244.

[17] Gurobi Optimizer Version 6.5. Houston, Texas: Gurobi Optimization, Inc., July 2016.

[18] G. Laporte, S. Nickel, F.S. da Gama (Eds.), Location Science, Springer, 2015.

[19] M. Lubin, I. Dunning, Computing in operations research using julia, INFORMS Journal on Computing 27 (2015) 238-248.

[20] M.J. Kuby, Programming models for facility dispersion: the p-dispersion and maxisum dispersion problems, Geographical Analysis 19 (1987) 315-329.

[21] V. Maniezzo, I. Mendes, M. Paruccini, Decision support for siting problems, Decision Support Systems 23 (1999) 273-284.

[22] Micheal Bauer Research, International consumer styles database, Nürnberg, Germany, http://www.english.mb-research.de/market-data-europe/consumer-styles.html accessed Jun 22, 2016.

[23] I.D. Moon, S.S. Chaudry, An anlalysis of network location problems with distance constraints, Management Science 30 (1984) 290-307.

[24] A.T. Murray, Maximal coverage location problem: impacts, significance, and evolution, International Regional Science Review 39 (2016) 5-27.

[25] A.T. Murray, R.L. Church, Impact models for siting undesirable facilities, Papers in Regional Science 77 (1998) 19-36.

[26] V. Maniezzo, I. Mendes, M. Paruccini, Decision support for siting problems, Decision Support Systems 23 (1999) 273-284.

## ACCEPTED MANUSCRIPT

[27] A. Oztekin, F.M. Pajouh, D. Delen, L.K. Swim, An RFID network design methodology for asset tracking in healthcare, Decision Support Systems 49 (2010) 100-109.

[28] C.P. Pappis, N.I. Karacapilidis, Applying the service level criterion in a location-allocation problem, Decision Support Systems 11 (1994) 77-81.

[29] H. Pirkul, R. Gupta, E. Rolland, VisOpt: a visual interactive optimization tool for P-median problems, Decision Support Systems 26 (1999) 209-223.

[30] D. Sayah, S. Irnich, A new compact formulation for the discrete p-dispersion problem, European Journal of Operational Research 256 (2017) 62-67.

[31] D.R. Shier, A min-max theorem for p-center problems on a tree, Transportation Science 11 (1977), 243-252.

[32] L.V. Snyder, Covering problems, in H.A. Eiselt,V. Marianov (Eds.), Foundations of Location Analysis, Springer, 2011, 109-135.

[33] C. Toregas, R. Swain, C. ReVelle, L. Bergman, The location of emergency service facilities, Operations Research 9 (1971) 1363-1373.

# ACCEPTED MANUSCRIPT

## Biographical Note

Jeremy William North is an Assistant Professor of Logistics at Murray State University. He received his Ph.D. in Business Administration – Logistics and Supply Chain Management from the University of Missouri – St. Louis in 2014. His research interests include facility location, heuristic algorithm development, and vehicle routing and scheduling.

Fred Luther Miller is a Hutchins Distinguished Professor emeritus of Marketing and Location Analytics at Murray State University. His teaching and research interests include location analytics, e-commerce, and global marketing.

# ACCEPTED MANUSCRIPT

## Highlights

 We develop and implement a multi-criteria optimization model called the p-dispersed maximal covering location problem.

The modeling approach is contingent upon and justified by the presence of multiple optimality in the maximal covering facility location problem.

 Using proprietary demographic and consumer spending data given to us for the purposes of this research, we integrate GIS location analytics techniques into our decision support system via the application the ESRI Business Analyst Web App.

An application of our methodology on a facility location problem in the region of Bavaria, Germany is given for an entertainment site selection problem.
