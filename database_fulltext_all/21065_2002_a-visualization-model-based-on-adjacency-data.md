---
otero_id: 21065
otero_key: "8MTEVFSG"
title: "A visualization model based on adjacency data"
authors: "Edward Condon; Bruce Golden; Shreevardhan Lele; S. Raghavan; Edward Wasil"
year: "2002"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00003-9"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A visualization model based on adjacency data

Edward Condon <sup>a</sup>, Bruce Golden <sup>b,</sup>\*, Shreevardhan Lele <sup>b</sup>, S. Raghavan <sup>b</sup>, Edward Wasil <sup>c</sup>

<sup>a</sup>Institute for Research in Electronics and Applied Physics, University of Maryland, College Park, MD 20742, USA <sup>b</sup>R.H. Smith School of Business, University of Maryland, College Park, MD 20742, USA <sup>c</sup>Kogod School of Business, American University, Washington, DC 20016, USA

Accepted 1 December 2001

## Abstract

In this paper, we describe a model whose focus is on data visualization. We assume the data are provided in adjacency format, as is frequently the case in practice. As an example, individuals who buy item a are likely to buy or consider buying items b, c, and d, also. We present a simple technique for obtaining distance measures between data points. Armed with the resulting distance matrix, we show how Sammon maps can be used to visualize the data points. An application to the college selection process is discussed in detail. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Visualization; Sammon map; Multidimensional scaling

## 1. Introduction

Relationships among various alternatives in a decision space can often be obtained in the form of adjacency data. For example, consider the output of an association rule analysis or a market basket analysis [1]. If item i and item j are found to be co-purchased, then they can be considered to be adjacent to each other. As another example, consider the output of a recommender system [7]. If the purchase of item i results in the recommendation of item j, then item j is adjacent to item i. Furthermore, if the purchase of item j results in the recommendation of item i, then items i and j are adjacent to each other. Thus, adjacency of two items suggests a significant degree of either cooccurrence or substitutability. Adjacency data for n alternatives can be summarized in the form of an $n \times n$ adjacency matrix, $A = ( a _ { i j } )$ , where $a _ { i j } = 1$ if item j is adjacent to item i, and 0 otherwise.

It should be noted that the adjacency matrix is typically derived from the observed demand for the n items. This is significantly different from measuring proximities between items based on product characteristics such as physical features, price, and quality. For several managerial decisions, adjacency data that are derived from observed demand provide more convincing evidence than proximity measures that are not based on observed demand.

In this paper, we consider the following problem. Given an adjacency matrix for a decision space consisting of n alternatives, we wish to obtain a twodimensional map of the n alternatives that enables the visualization of the given decision space. In this twodimensional visualization, the distance between points provides a measure of their relationship.

Representing the decision space in a two-dimensional map has several benefits over the adjacency matrix representation. Consider the case where two items are not directly adjacent to each other but can be linked via another item or a chain of items. It is difficult and impractical to obtain information on such linkages from the adjacency matrix; however, a twodimensional map can easily exhibit such longer linkages. Additionally, a good two-dimensional representation can enable a decision maker to visually detect clusters and other patterns that may be present in the data. Such patterns are difficult to detect in the adjacency matrix.

In order to obtain a two-dimensional map of a set of n items, it is necessary to first obtain a symmetric $n \times n$ distance matrix, $\pmb { D } \mathrm { = } ( d _ { i j } )$ , where $d _ { i j }$ represents the distance between items i and j. Such distances are usually obtained from a high dimensional representation of the items (for example, in a space of product characteristics) or elicited directly from the decision maker. In this study, we develop a graph-theoretic approach to convert the given asymmetric adjacency matrix into a symmetric distance matrix.

Given a distance matrix, we can create a twodimensional map using multidimensional scaling (e.g., see Ref. [2]). In particular, we use the scaling technique known as Sammon mapping. This technique has been shown to be superior to the classical methods of multidimensional scaling (MDS) when the map is used to detect clusters (e.g., see Ref. [5]). The Sammon mapping technique [6] takes the given distance matrix $\pmb { D } \mathrm { = } ( d _ { i j } )$ as the input distance matrix and creates an output configuration in a low dimensional space (typically two-dimensional) with output distance matrix $F { = } ( f _ { i j } )$ by minimizing the error $\sum _ { i < j } { [ ( d _ { i j } - f _ { i j } ) ^ { 2 } / d _ { i j } ] } .$ In this paper, the output distance matrix F represents the distances between points in two-dimensional space and the error provides an indication of how the placement of points is doing with respect to the original distances D. If the error is zero, then we can locate the points in two-dimensional space and capture the relationships specified in D exactly.

The rest of this paper is organized as follows. Section 2 describes a graph-theoretic procedure using the all-pairs shortest path method for converting the given asymmetric adjacency matrix into a symmetric distance matrix. In Section 3, we provide a detailed example containing adjacency data for undergraduate college programs in the United States. A distance matrix is obtained using the procedure outlined in Section 2 and, in turn, this distance matrix is used to create a Sammon map of the colleges. In Section 4, we analyze various patterns in the Sammon map that lead to several useful insights about the demands for various colleges. Section 5 concludes the paper and provides directions for extensions of this work.

## 2. Methodology

In this section, we describe a simple technique to get distance measures from adjacency data. This allows for use of MDS variants such as Sammon maps to map the data.

Our technique to obtain distance measures consists of the following steps.

(1) Create the $n \times n ~ 0 { - } 1$ asymmetric adjacency matrix A. Entry $a _ { i j } = 1$ , in row i and column j of A, represents that item j is in the list of items adjacent to item i. Note that, even if $a _ { i j } = 1$ item i may not be in the list of items adjacent to item j. In other words, $a _ { j i }$ could be 0.

(2) Next, convert the adjacency matrix to a directed graph as follows. Create a node for each item (for a total of n nodes). Next, create a directed arc for each nonzero entry in A. If $a _ { i j } = 1$ , create a directed arc from node i to node j.

(3) Compute distance measures. Let the distance of an arc in this directed graph be equal to 1. Compute the all-pairs shortest path distance matrix D of this directed graph. Entry $d _ { i j }$ in matrix D represents the distance from node i to node j in the directed graph.

(4) Modify the distance matrix D, to obtain a final distance matrix X, to account for disconnected components, and the need for symmetry.

A critical issue deals with the fact that techniques like Sammon maps and MDS expect a symmetric distance matrix. However, due to the asymmetric nature of the adjacency relationships, the distances obtained from our technique can be asymmetric. We now describe how to convert adjacency data to a format that can be used by Sammon maps. We take a convex combination of the larger and smaller distance measures, amax $( d _ { i j } , d _ { j i } ) + ( 1 - \alpha ) \mathrm { m i n } ( d _ { i j } , d _ { j i } )$ where $0 \leq \alpha \leq 1$ , to obtain a symmetric measure between nodes i and j. In selecting a, one option would be to take the maximum distance (i.e., a = 1), another is to take the minimum distance (i.e., a = 0), and a third possibility is to take the average (i.e., a = 0.5). Taking the average appears more reasonable since it gives equal weight to the relationships on the i to j path and the relationships on the j to i path. We use the average in the computational experiments presented in the next section.

We illustrate our procedure on the adjacency matrix and the network representation shown in Fig. 1. We compute the all-pairs shortest path using the Floyd – Warshall method (see Ref. [4]). This gives the distance matrix D. We make the distance matrix D symmetric by averaging the distances to get the final distance matrix X. The two matrices are shown in Fig. 2.

We now consider the situation where there is no path from a node to another in the directed graph. In this case, we may view the shortest distance as being infinity. However, in order to visualize the data, a finite symmetric distance measure is required between every pair of data points. One way to get around this problem is to replace all infinite entries in D with a suitably large finite value, L.

It is now useful to introduce two standard graphtheoretic concepts concerning directed graphs and connectivity. A strongly connected component of a directed graph is a maximal set of nodes such that there is a directed path from every node in the component to every other node in the component. A directed graph is strongly connected if it consists of a single strongly connected component.

![](/api/attachments/8MTEVFSG/fulltext/images/211662f5fd689e972558f95fe5262cacdd10e8b1c1b3877a88e6da95b50f21f9.jpg)  
Fig. 1. Adjacency matrix and associated directed graph.

![](/api/attachments/8MTEVFSG/fulltext/images/a9ce029c8449b7eadea909c9cec493f93efdba9ce94dfb06f38f8c026a4e0486.jpg)  
Fig. 2. Distance matrices D and X.

A weakly connected component of a directed graph is a maximal set of nodes such that there is a path, disregarding orientation of the arcs, from every node in the component to every other node in the component. A directed graph is weakly connected if it consists of a single weakly connected component.

Some caution needs to be taken in choosing L, the large value that represents infinity. If it is too large, then the points within a strongly connected component will be pushed closer together in the visualization and it will be difficult to ascertain within-component relationships from the visualization. On the other hand, choosing a value for L that is too small may result in a visualization that merges distinct components.

We further refine our procedure of replacing infinite distances in order to better represent the relationships within the data. To explain our idea, consider the directed graph representing the adjacency data shown in Fig. 3. There are two strongly connected components, A and B. Recall that within each strongly connected component, there is a path from every node to every other node. In Fig. 3, we see that there are paths from component A to component B, and no paths from component B to component A. Notice that there is a single arc from a node in component A to a node in component B. This represents the relationship linking (or weakly connecting) the two components. Rather than replacing all B to A distances by infinity, our procedure makes use of linkages between components. For each arc from one strongly connected component to another, we create a reverse arc with a suitably large distance value, R. Now a computation of the all-pairs shortest path method provides distance measures from B to A as well. Again, care must be taken in choosing a value for R. Our computational experiments (see Section 3) indicate that a good choice of a value for R is the average of the maximum shortest path distances in each of the strongly connected components of the graph.

![](/api/attachments/8MTEVFSG/fulltext/images/8f8ce932c6c7409c94cf28a656d8a9bce9b0788a17c95265d5e79484f6636d48.jpg)  
Fig. 3. Strongly connected components A and B. There are paths from A to B, but none from B to A.

If the graph representing adjacency relationships is not weakly connected, then even after the above refinement, it is possible that there is no path from one strongly connected component to another. In this case, we may use L as the distance measure between nodes that do not have a directed path between them. However, in general, it is better to separately visualize each weakly connected component since there is no relationship between weakly connected components.

We can now summarize Step (4) of the modification procedure.

(4.1) Identify arcs from one strongly connected component to another. Add reverse arcs for each of them with a distance value of R.

(4.2) Recalculate distance matrix D using the allpairs shortest path method.

(4.3) If the graph is not weakly connected, then there are still no paths between some pairs of nodes. Make these distances L in the distance matrix D.

(4.4) Symmetrize distance matrix D to obtain final distance matrix X (where $\scriptstyle x _ { i j } = x _ { j i } = ( d _ { i j } + d _ { j i } ) / 2 )$ to be used as input to a Sammon map procedure or MDS procedure.

The running time for the procedure is dominated by the all-pairs shortest path calculation that can be done in O(n<sup>3</sup>) time.

## 3. Application: college selection

In this section, we apply our technique to help visualize data from a college selection problem. We describe the data set, the code we use to generate our Sammon maps, and how we set the values of parameters in our code. Finally, we present maps based on geographical location, type of college, cost, and academic quality.

The Fiske Guide to Colleges [3] is a well-respected publication that has been used by students and their parents for nearly 20 years to help select the right college. The 2000 edition of The Fiske Guide contains information on more than 300 colleges and universities in the United States. It provides statistics on items such as cost and SAT score, and ratings based on academics, social life, and quality of life. In addition, The Fiske Guide lists a school’s biggest overlaps, that is, ‘‘the colleges and universities to which its applicants are also applying in greatest numbers and which thus represent its major competitors.’’ Furthermore, The Fiske Guide points out (p. xxvi):

‘‘Once you have decided on the type of school you think you want. . .we hope you will thumb through the book looking for similar institutions

Table 1  
Entries in the adjacency matrix for a sample of eight schools

<table><tr><td>School</td><td>Brown</td><td>Cornell U.</td><td>Harvard</td><td>MIT</td><td>Penn</td><td>Princeton</td><td>Stanford</td><td>Yale</td></tr><tr><td>Brown</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Cornell U.</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>Harvard</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td>MIT</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Penn</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td>Princeton</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Stanford</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td>Yale</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td></tr></table>

Table 2  
One hundred schools from The Fiske Guide that form our analysis set

<table><tr><td>Component</td><td>School</td><td>State</td><td>Type</td><td>Cost</td><td>Academics</td></tr><tr><td>A1</td><td>Arizona State University</td><td>AZ</td><td>Public</td><td>$$</td><td>★★★</td></tr><tr><td>A2</td><td>Arizona, University of</td><td>AZ</td><td>Public</td><td>$</td><td>★★★</td></tr><tr><td>A3</td><td>Barnard College (Columbia University)</td><td>NY</td><td>Private</td><td>$$$$</td><td>★★★★★</td></tr><tr><td>A4</td><td>Bates College</td><td>ME</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A5</td><td>Boston College</td><td>MA</td><td>Private</td><td>$$$$</td><td>★★★</td></tr><tr><td>A6</td><td>Boston University</td><td>MA</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A7</td><td>Bowdoin College</td><td>ME</td><td>Private</td><td>$$$$</td><td>★★★★★</td></tr><tr><td>A8</td><td>Bryn Mawr College</td><td>PA</td><td>Private</td><td>$$$$</td><td>★★★★★</td></tr><tr><td>A9</td><td>Bucknell University</td><td>PA</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A10</td><td>Carleton College</td><td>MN</td><td>Private</td><td>$$$$</td><td>★★★★★</td></tr><tr><td>A11</td><td>Carnegie Mellon University</td><td>PA</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A12</td><td>Colby College</td><td>ME</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A13</td><td>Colgate University</td><td>NY</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A14</td><td>Colorado College</td><td>CO</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A15</td><td>Colorado, University of—Boulder</td><td>CO</td><td>Public</td><td>$$</td><td>★★★★</td></tr><tr><td>A16</td><td>Connecticut, University of</td><td>CT</td><td>Public</td><td>$$</td><td>★★★★</td></tr><tr><td>A17</td><td>Delaware, University of</td><td>DE</td><td>Public</td><td>$$</td><td>★★★</td></tr><tr><td>A18</td><td>Denver, University of</td><td>CO</td><td>Private</td><td>$$$</td><td>★★★</td></tr><tr><td>A19</td><td>Emory University</td><td>GA</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A20</td><td>George Mason University</td><td>VA</td><td>Public</td><td>$$</td><td>★★★</td></tr><tr><td>A21</td><td>Georgetown University</td><td>DC</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A22</td><td>Grinnell College</td><td>IA</td><td>Private</td><td>$$$</td><td>★★★★</td></tr><tr><td>A23</td><td>Illinois, University of—Urbana-Champaign</td><td>IL</td><td>Public</td><td>$$</td><td>★★★★★</td></tr><tr><td>A24</td><td>Indiana University</td><td>IN</td><td>Public</td><td>$$</td><td>★★★★</td></tr><tr><td>A25</td><td>Iowa State University</td><td>IA</td><td>Public</td><td>$</td><td>★★★</td></tr><tr><td>A26</td><td>Iowa, University of</td><td>IA</td><td>Public</td><td>$$</td><td>★★★★</td></tr><tr><td>A27</td><td>James Madison University</td><td>VA</td><td>Public</td><td>$</td><td>★★★</td></tr><tr><td>A28</td><td>Lafayette College</td><td>PA</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A29</td><td>Lehigh University</td><td>PA</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A30</td><td>Lewis and Clark College</td><td>OR</td><td>Private</td><td>$$$$</td><td>★★★</td></tr><tr><td>A31</td><td>Macalester College</td><td>MN</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A32</td><td>Marquette University</td><td>WI</td><td>Private</td><td>$$</td><td>★★★</td></tr><tr><td>A33</td><td>Mary Washington College</td><td>VA</td><td>Public</td><td>$</td><td>★★★★</td></tr><tr><td>A34</td><td>Maryland, University of—College Park</td><td>MD</td><td>Public</td><td>$$</td><td>★★★</td></tr><tr><td>A35</td><td>Massachusetts, University of—Amherst</td><td>MA</td><td>Public</td><td>$$</td><td>★★★</td></tr><tr><td>A36</td><td>Michigan State University</td><td>MI</td><td>Public</td><td>$$</td><td>★★★</td></tr><tr><td>A37</td><td>Michigan, University of</td><td>MI</td><td>Public</td><td>$$$$</td><td>★★★★★</td></tr><tr><td>A38</td><td>Middlebury College</td><td>VT</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A39</td><td>Minnesota, University of—Twin Cities</td><td>MN</td><td>Public</td><td>$$</td><td>★★★★</td></tr><tr><td>A40</td><td>Mount Holyoke College</td><td>MA</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A41</td><td>New Hampshire, University of</td><td>NH</td><td>Public</td><td>$$$$</td><td>★★★</td></tr><tr><td>A42</td><td>New Jersey, The College of</td><td>NJ</td><td>Public</td><td>$</td><td>★★★</td></tr><tr><td>A43</td><td>New York University</td><td>NY</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A44</td><td>North Carolina State University</td><td>NC</td><td>Public</td><td>$</td><td>★★★</td></tr><tr><td>A45</td><td>North Carolina, University of—Chapel Hill</td><td>NC</td><td>Public</td><td>$</td><td>★★★★★</td></tr><tr><td>A46</td><td>Northeastern University</td><td>MA</td><td>Private</td><td>$$$$</td><td>★★</td></tr><tr><td>A47</td><td>Northwestern University</td><td>IL</td><td>Private</td><td>$$$$</td><td>★★★★★</td></tr><tr><td>A48</td><td>Notre Dame, University of</td><td>IN</td><td>Private</td><td>$$$</td><td>★★★★</td></tr><tr><td>A49</td><td>Oberlin College</td><td>OH</td><td>Private</td><td>$$$$</td><td>★★★★★</td></tr><tr><td>A50</td><td>Oregon State University</td><td>OR</td><td>Public</td><td>$$</td><td>★★★</td></tr><tr><td>A51</td><td>Oregon, University of</td><td>OR</td><td>Public</td><td>$</td><td>★★★</td></tr><tr><td>A52</td><td>Pennsylvania State University</td><td>PA</td><td>Public</td><td>$$</td><td>★★★</td></tr></table>

(continued on next page)

Table 2 (continued )

<table><tr><td>Component</td><td>School</td><td>State</td><td>Type</td><td>Cost</td><td>Academics</td></tr><tr><td>A53</td><td>Pittsburgh, University of</td><td>PA</td><td>Public</td><td>$$$</td><td>★★★</td></tr><tr><td>A54</td><td>Puget Sound, University of</td><td>WA</td><td>Private</td><td>$$$$</td><td>★★★</td></tr><tr><td>A55</td><td>Purdue University</td><td>IN</td><td>Public</td><td>$</td><td>★★★</td></tr><tr><td>A56</td><td>Reed College</td><td>OR</td><td>Private</td><td>$$$$</td><td>★★★★★</td></tr><tr><td>A57</td><td>Richmond, University of</td><td>VA</td><td>Private</td><td>$$$</td><td>★★★</td></tr><tr><td>A58</td><td>Rutgers University</td><td>NJ</td><td>Public</td><td>$$</td><td>★★★★</td></tr><tr><td>A59</td><td>Smith College</td><td>MA</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A60</td><td>Tufts University</td><td>MA</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A61</td><td>Vanderbilt University</td><td>TN</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A62</td><td>Vassar College</td><td>NY</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A63</td><td>Vermont, University of</td><td>VT</td><td>Public</td><td>$$$</td><td>★★★</td></tr><tr><td>A64</td><td>Villanova University</td><td>PA</td><td>Private</td><td>$$$$</td><td>★★★</td></tr><tr><td>A65</td><td>Virginia Polytechnic Institute</td><td>VA</td><td>Public</td><td>$</td><td>★★★</td></tr><tr><td>A66</td><td>Virginia, University of</td><td>VA</td><td>Public</td><td>$$</td><td>★★★★★</td></tr><tr><td>A67</td><td>Wake Forest University</td><td>NC</td><td>Private</td><td>$$$$</td><td>★★★</td></tr><tr><td>A68</td><td>Washington University in St. Louis</td><td>MO</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A69</td><td>Washington, University of</td><td>WA</td><td>Public</td><td>$</td><td>★★★★</td></tr><tr><td>A70</td><td>Wellsley College</td><td>MA</td><td>Private</td><td>$$$$</td><td>★★★★★</td></tr><tr><td>A71</td><td>Whitman College</td><td>WA</td><td>Private</td><td>$$$$</td><td>★★★★</td></tr><tr><td>A72</td><td>Willamette University</td><td>OR</td><td>Private</td><td>$$$$</td><td>★★★</td></tr><tr><td>A73</td><td>William and Mary, College of</td><td>VA</td><td>Public</td><td>$</td><td>★★★★★</td></tr><tr><td>A74</td><td>Wisconsin, University of—Madison</td><td>WI</td><td>Public</td><td>$</td><td>★★★★★</td></tr><tr><td>B1</td><td>Alabama, University of —Tuscaloosa</td><td>AL</td><td>Public</td><td>$</td><td>★★★</td></tr><tr><td>B2</td><td>Auburn University</td><td>AL</td><td>Public</td><td>$</td><td>★★</td></tr><tr><td>B3</td><td>Charleston, College of</td><td>SC</td><td>Public</td><td>$</td><td>★★★</td></tr><tr><td>B4</td><td>Clemson University</td><td>SC</td><td>Public</td><td>$</td><td>★★★</td></tr><tr><td>B5</td><td>Florida State University</td><td>FL</td><td>Public</td><td>$</td><td>★★★</td></tr><tr><td>B6</td><td>Florida, University of</td><td>FL</td><td>Public</td><td>$</td><td>★★★★</td></tr><tr><td>B7</td><td>Georgia Institute of Technology</td><td>GA</td><td>Public</td><td>$$</td><td>★★★★</td></tr><tr><td>B8</td><td>Georgia, University of</td><td>GA</td><td>Public</td><td>$</td><td>★★★</td></tr><tr><td>B9</td><td>Miami, University of</td><td>FL</td><td>Private</td><td>$$$$</td><td>★★★</td></tr><tr><td>B10</td><td>South Carolina, University of</td><td>SC</td><td>Public</td><td>$$</td><td>★★★</td></tr><tr><td>B11</td><td>Tennessee, University of—Knoxville</td><td>TN</td><td>Public</td><td>$</td><td>★★★</td></tr><tr><td>C1</td><td>Brown University</td><td>RI</td><td>Private</td><td>$$$$</td><td>★★★★★</td></tr><tr><td>C2</td><td>Cornell University</td><td>NY</td><td>Private</td><td>$$$$</td><td>★★★★★</td></tr><tr><td>C3</td><td>Harvard University</td><td>MA</td><td>Private</td><td>$$$$</td><td>★★★★★</td></tr><tr><td>C4</td><td>Massachusetts Institute of Technology</td><td>MA</td><td>Private</td><td>$$$$</td><td>★★★★★</td></tr><tr><td>C5</td><td>Pennsylvania, University of</td><td>PA</td><td>Private</td><td>$$$$</td><td>★★★★★</td></tr><tr><td>C6</td><td>Princeton University</td><td>NJ</td><td>Private</td><td>$$$$</td><td>★★★★★</td></tr><tr><td>C7</td><td>Stanford University</td><td>CA</td><td>Private</td><td>$$$$</td><td>★★★★★</td></tr><tr><td>C8</td><td>Yale University</td><td>CT</td><td>Private</td><td>$$$$</td><td>★★★★★</td></tr><tr><td>D1</td><td>California, University of—Berkeley</td><td>CA</td><td>Public</td><td>$$$$</td><td>★★★★★</td></tr><tr><td>D2</td><td>California, University of—Davis</td><td>CA</td><td>Public</td><td>$$$</td><td>★★★★</td></tr><tr><td>D3</td><td>California, University of—Irvine</td><td>CA</td><td>Public</td><td>$$$$</td><td>★★★</td></tr><tr><td>D4</td><td>California, University of—Los Angeles</td><td>CA</td><td>Public</td><td>$$$</td><td>★★★★</td></tr><tr><td>D5</td><td>California, University of—San Diego</td><td>CA</td><td>Public</td><td>$$$</td><td>★★★★</td></tr><tr><td>D6</td><td>California, University of—Santa Barbara</td><td>CA</td><td>Public</td><td>$$$$</td><td>★★★</td></tr><tr><td>D7</td><td>Southern California, University of</td><td>CA</td><td>Private</td><td>$$$$</td><td>★★★</td></tr></table>

that might not have occurred to you. One way to do this is to look at the ‘‘Overlaps’’ of schools you like and then check out those schools’ overlaps. Many students have found this worthwhile, and quite frankly, we view the widening of students’ horizons about American higher education as one of the most important purposes of this book.’’

To illustrate, the overlaps of the University of Pennsylvania are Harvard, Princeton, Yale, Cornell, and Brown. Overlaps are not necessarily symmetric. For example, the University of Pennsylvania is not among Harvard’s overlaps (Princeton, Yale, Stanford, MIT, and Brown). The Fiske Guide points out that the lack of symmetry is ‘‘especially true in the case of institutions that are considered ‘‘safety’’ schools by students who also apply to more selective colleges and universities.’’ We use the overlap information given in The Fiske Guide to generate an adjacency matrix, build a directed graph, compute distance measures, and modify the distance matrix for input to our Sammon map procedure.

Before we generate the adjacency matrix, we need to prepare the overlap data. The Fiske Guide lists 300 colleges and universities. There is one listing and one set of overlaps for St. John’s College (it has two campuses—one in Annapolis, MD and one in Santa

Fe, NM) and for the joint university of St. John’s University and College of St. Benedict (both located in Minnesota). Thus, the actual number of schools is 298 and, of these, we did not include Alverno College (located in Milwaukee, WI) in our analysis since its four overlap schools are not given in The Fiske Guide.

For some of the 297 schools that we propose to analyze, overlaps are not always clearly defined. For example, The Fiske Guide gives UCLA and other UC campuses as part of the overlaps for the University of California-Berkeley. We include the UC campuses of Santa Barbara, San Diego, and Santa Cruz as part of Berkeley’s overlaps.

The data preparation phase provides us with a clean data set of 297 colleges and universities with each school having one to eight overlaps that are listed in The Fiske Guide. Using this data set, we now construct an adjacency matrix for all 297 schools. To illustrate this, in Table 1, we show the entries in the adjacency matrix for a sample of eight schools. We see that these entries are not symmetric.

![](/api/attachments/8MTEVFSG/fulltext/images/b3b54cf30ef9ad2910d1bf7fac98cc79be53c4d6d514240285c8e57b38093884.jpg)  
Fig. 4. Sammon map of the 100 schools with each school labeled by its component identifier.

Next, we convert the adjacency matrix for all 297 schools to a directed graph following the instructions given in Step (2) of our technique (see Section 2). Based on this directed graph, several strongly connected components emerge and we select the four largest for analysis: component A with 74 schools, component B with 11 schools from the southern U.S., component C with 8 schools of which 6 are from the Ivy League, and component D with 7 schools from California. The 100 schools that make up these four strongly connected components are listed in Table 2. The first column of Table 2 shows the component to which each school belongs. The 74 schools belonging to component A are given first, so that the first school listed is Arizona State University which carries the identifier A1; the 11 schools from component B are given next, and so on for the rest of the schools. The table also lists the state in which each school is located, the type of school (public or private), the cost (inexpensive (\$) to very expensive (\$\$\$\$)), and the academic quality (fair (11) to outstanding (11111)) as defined in The Fiske Guide. We will apply our visualization technique to these 100 schools.

We now apply Step (3) and compute the all-pairs shortest path distance matrix (D) of the directed graph formed by the 100 schools given in Table 2. To generate D, we use the shortest path routine found in the package Combinatorica (for more details, consult the Web page at http://www.cs.sunysb.edu/ <sup>f</sup> skiena/ combinatorica/index.html). The largest distance from the all-pairs shortest path computations is 18, so we set the value of L equal to 20 (if needed in the next step).

We now apply the modified form of Step (4) which requires us to add reverse arcs of length R from one strongly connected component to another (when there is a forward arc representing an adjacency relationship from one strongly connected component to another). We experimented with several values (e.g., 10, 15, and 20) and found that setting the value of R equal to the average of the maximum shortest distances within the four components worked well for this data set (that is, the specified value of R provided clear relationships within and between components and the orientations of the components were similar to how they were connected). The maximum shortest distances were 18, 5, 2, and 3 within the four components A, B, C, and D, respectively, so we set the value of R equal to $( 1 8 + 5 + 2 + 3 ) / 4 = 7$ With this value, we recalculated D (this matrix did not have any infinite distances), and then symmetrized D to obtain the final distance matrix (X) for input to our Sammon map procedure. We point out that the Sammon maps created with different random starts and $R = 7$ were visually similar, that is, the four components were aligned in roughly the same way in each map.

![](/api/attachments/8MTEVFSG/fulltext/images/827846511e6303a974af112c48b2faba8f2206978792f2d25c155a5a99e9c4b7.jpg)  
Fig. 5. Sammon map of the 100 schools with each school labeled by its geographical location (state).

We wrote code in Mathematica 4.0 for Windows 95/98/NT to generate a Sammon map. Our code reads in a symmetric n  n distance matrix as input. A set of n random coordinates (one for each data point) in two dimensions is generated. A second distance matrix is calculated from this random set of starting coordinates. We use the error measure given in Ref. [6] and iteratively adjust the coordinates (corresponding to the data points) as given in Ref. [6] to minimize the error measure. The error measure computation and coordinate adjustments are repeated until a stopping criterion is satisfied and the final coordinates are then plotted in two dimensions. We point out that the algorithm essentially keeps the coordinates of all points fixed except one. This point is moved until the objective function is minimized. Then another point is selected and all other points are fixed. This point is moved until the objective function is minimized. This continues until there is no further improvement.

![](/api/attachments/8MTEVFSG/fulltext/images/ea7e273c2be2f93ca3b88ff00a00a37ca7058bd991a385ff3911a9946c83ed91.jpg)  
Fig. 6. Sammon map of the 100 schools with each school labeled by its designation (public (U) or private (R)).

Our Sammon map of the 100 schools is shown in Fig. 4. Each school is labeled by its component identifier (e.g., A1). Four maps (Figs. 5 – 8) show each school’s location (state), designation (public or private), cost, and academic quality. These five maps are discussed in the next section.

## 4. Discussion of results

The Fiske Guide recommends taking full advantage of the adjacency (overlap) data provided in its pages. However, this is not as easy as it sounds. The reader can glean some local information (e.g., which schools are Harvard’s overlaps), but global information is much more difficult to collect (e.g., suppose one wants a list of all the overlaps of Harvard’s overlaps). One of the benefits of data visualization, especially where appropriate symbols and colors are used, is that this global information becomes immediately available. Patterns and relationships among the schools become clear with visualization.

Using the key from Table 2, Fig. 4 reveals that the University of Delaware (A17), George Mason University (A20), James Madison University (A27), Virginia Polytechnic Institute (A65), Penn State University (A52), The College of New Jersey (A42), and the University of North Carolina (A45) are the schools most similar (in an overlapping sense) to the University of Maryland (A34), since they are nearest neighbors on the Sammon map (the schools are visually close together on the map). It should be clear that geography probably plays a large role here. For confirmation, see Fig. 5. On the other hand, Fig. 4 indicates that Washington University (A68), Emory University (A19), and Georgetown University (A21) are similar to each other and yet each pair is at least 500 miles apart.

![](/api/attachments/8MTEVFSG/fulltext/images/4ee631e61436f9e977c8bea3352cf4114d3afb75057e7336a161b390e4161095.jpg)  
Fig. 7. Sammon map of the 100 schools with each school labeled by its cost (inexpensive (\$) to very expensive (\$\$\$\$)).

In this example, all of the University of Maryland’s Sammon map neighbors are public schools (see Fig. 6). On the other hand, Washington University (A68) has, mainly, other private schools as Sammon map neighbors. Of the public schools, the University of Michigan (A37) seems to be most similar. Fig. 6 enables us to observe how the public schools and private schools cluster separately. Given an interest in a particular private school, it is easy to identify similar public schools, and vice versa.

Given an interest in a particular school, a student (or parent) may want to know if there are less expensive, Sammon map neighbors. Fig. 7 helps us to answer such a question. For example, we can use Table 2 and Fig. 7 to observe that the University of Notre Dame (A48) is a less expensive, Sammon map neighbor of Washington University (A68).

Given an interest in a particular school, say, the University of Maryland (A34), a student or parent might be interested in applying to a Sammon map neighbor of higher academic quality as a ‘‘reach’’ school. A reach school is one that the applicant has a small chance of getting into, but it is far from a sure thing. Fig. 8 could be used, in this case, to identify the University of North Carolina (A45) as such a school.

In Fig. 9, we attempt to pull all the pieces together by zooming in on a particular school, Tufts (A60), in order to more carefully explore our visualizations. From the school identifier in panel (a), we obtain the school name in panel (f). From panel (b), we can see that most of the Sammon map neighbors of Tufts are on the East Coast. From panel (c), we learn that only a few of these are public schools. As expected, panel (d) indicates that these public schools are less-

![](/api/attachments/8MTEVFSG/fulltext/images/1bdfd8d5249b295ccca776ee4dab00f7b127314ac750989548ea9b8ebe9eaaad.jpg)  
Fig. 8. Sammon map of the 100 schools with each school labeled by its academic quality (fair (11) to outstanding (11111)).

![](/api/attachments/8MTEVFSG/fulltext/images/073eaf9e286ecee2b1e082501daa646179aae6f193878ce0f8783417a87fe3d9.jpg)  
(a) Identifier

![](/api/attachments/8MTEVFSG/fulltext/images/2bf3698c9b81aeded6e502e29da0d0cece8834404afe6f5c9a802833f105b568.jpg)  
(b) State

![](/api/attachments/8MTEVFSG/fulltext/images/00cf9fc269edce3d51413c367a8eadfde4e35d913bfe091c01906f16030a9642.jpg)  
(c) Public or private

![](/api/attachments/8MTEVFSG/fulltext/images/b86f6d89c3bfa836b84ade52d147b4aaddfd71154b2cd4e3abc5bbc278111b70.jpg)  
(d) Cost

![](/api/attachments/8MTEVFSG/fulltext/images/82b18a95981df966fbf6c9dd24d72a177517db7c6f3dccbf6a48fec7412344bb.jpg)  
(e) Academics

![](/api/attachments/8MTEVFSG/fulltext/images/8d52c77466a8c8e5de68781f4dab01dc8120c007ccc794548fbbde91abf2d4a4.jpg)  
(f) School name  
Fig. 9. Six panels showing zoomed views of schools that are neighbors of Tufts University.

expensive alternatives. Panel (e) reveals that several of these less-expensive, public schools (e.g., William and Mary, University of Virginia, and University of North Carolina) actually have higher-quality academics than Tufts. Fig. 9 and the above discussion reveal a richness of information not available to someone who merely looks up Tufts in The Fiske Guide and finds that Brown, Cornell, Harvard, University of Pennsylvania, and Georgetown are overlaps. This is a key motivation for our work.

It is easy to imagine a wide variety of other figures embedded in a visually based decision support system (DSS) for college selection. Each of these figures would enable the user to pose and answer relevant questions such as: Which Sammon map neighbors of a particular school have a large (or small or mediumsize) undergraduate population? Which Sammon map neighbors of a particular school have campuses that are urban (or rural or suburban)? Which Sammon map neighbors of a particular school have a sizeable African –American (or Hispanic or Jewish) population? All of these data are readily available, either in The Fiske Guide or elsewhere.

A fully functional DSS might allow the user to suppress those schools, in which there is no interest, from the Sammon map. Some potential examples are: only show those schools with low or moderate costs; only show those schools with outstanding academic programs; only show those schools in urban environments; only show those schools with at least 10,000 undergraduates; only show those schools within nearby states.

Furthermore, it is expected that making a transition from one figure to another on the computer screen would be simple and, with respect to any such figure, by pointing to a particular label and clicking, the user could easily access all available data relating to that particular school.

The visually based DSS that we envision would be simple, powerful, and very useful to students and parents alike. As far as we know (and we have looked), no comparable decision support tool for college selection exists.

## 5. Conclusions and future work

In this paper, we have focused on adjacency data. We have developed a technique (based on shortest paths) to convert adjacency data to a format that can be used by Sammon maps to obtain a meaningful visualization of the data. Each step is relatively easy to perform. An application to the college selection process was discussed in detail. In this application, a single Sammon map was used to describe the information for 100 schools contained in a large, well-known collegeselection guide.

Alternatively, U.S. News & World Report publishes a college ranking each spring based on multidimensional numerical data. These columns of numerical data can also be used to build Sammon maps (using the concept of Euclidean distance). In fact, this is the traditional way in which Sammon maps are constructed. In future work, we would like to explore this alternative approach and compare a Sammon map constructed from adjacency data to one constructed from multidimensional numerical data. We might examine whether the merger of two maps creates a more informative visual display. It may be possible to use the multidimensional numerical data to fill in missing entries in the adjacency data (or vice versa). We might also examine whether it is possible to display directed arcs on a Sammon map so that a user could tell the direction of the relationship (overlap) between two schools.

Along other lines, we would hope to investigate whether the visually based DSS, sketched in this paper, can be applied to Web-based recommender systems for products such as books, music CDs, and movies. It may be possible to use co-citation of references or keywords to construct adjacency data and appeal to Sammon maps for the purposes of finding similar or closely related journal articles or scholarly books. Many potential applications of this work seem to exist.

## References

[1] M. Berry, G. Linoff, Data Mining Techniques, Wiley, New York, 1997.

[2] T. Cox, M. Cox, Multidimensional Scaling, Chapman & Hall, London, 1994.

[3] E. Fiske, The Fiske Guide to Colleges 2000, Times Books, New York, 1999.

[4] E. Lawler, Combinatorial Optimization: Networks and Matroids, Holt, Rinehart, and Winston, New York, 1976.

[5] B. Ripley, Pattern Recognition and Neural Networks, Cambridge Univ. Press, Cambridge, 1996.

[6] J. Sammon, A nonlinear mapping for data structure analysis, IEEE Transactions on Computers C-18 (5) (1969) 401 – 409.

[7] J. Schafer, J. Konstan, J. Riedl, E-commerce recommendation applications, Data Mining and Knowledge Discovery 5 (1/2) (2001) 115 – 153.

![](/api/attachments/8MTEVFSG/fulltext/images/cbfcc7a10b6cf95b510c428b1c2c860f2f05728c5e0777ccf8270cf780e7f6b6.jpg)  
Edward Condon is a faculty research assistant at the Institute for Research in Electronics and Applied Physics at the University of Maryland. His current research interests are data visualization and its application to operations research problems, Sammon maps and group decision making, and neural networks. Mr. Condon received his MS in Systems Engineering from the University of Maryland.

![](/api/attachments/8MTEVFSG/fulltext/images/8fba3736ab23f9459e6d73c34b4eac2e0e45480b25c8137e0b3dafac04f84141.jpg)

![](/api/attachments/8MTEVFSG/fulltext/images/356e3aba347cc01980c226f1eba48c0ab4e68a062df1ed0edf11172f9e986e2f.jpg)  
Bruce Golden is the France-Merrick Chair in Management Science at the University of Maryland’s Robert H. Smith School of Business. He is Editor-in-Chief of Networks and previously served as Editor-in-Chief of the INFORMS Journal on Computing. Both of his daughters attend highly regarded colleges in the mid-west.

Shreevardhan Lele is Assistant Professor of Decision and Information Technologies at the Robert H. Smith School of Business, University of Maryland, College Park. He obtained his PhD in Statistics and Management Science from the University of Michigan Business School, Ann Arbor. He works in the area of data mining for managerial applications.

![](/api/attachments/8MTEVFSG/fulltext/images/3123ea9bb92a5a57905417685b651605824ba9ce527067e4a891c82edcf808f8.jpg)

S. Raghavan’s research interests are in optimization techniques and their applications to e-markets, supply chain management, and telecommunications. His recent research and teaching has centered around network planning, design, and optimization, data mining, auctions, and internet pricing. Dr. Raghavan is an associate editor of Networks, and holds two U.S. patents. He received the 1996 George B. Dantzig Disserta-

tion Award from INFORMS. Prior to joining the faculty at the University of Maryland, he led the Optimization Group at U.S. WEST Advanced Technologies. He received his PhD in Operations Research from the Massachusetts Institute of Technology.

![](/api/attachments/8MTEVFSG/fulltext/images/e8b0511a0bd70aea852b7da870774a72d053ea6f5f4f35d7638a0fa2579ecaba.jpg)  
Edward Wasil is a Professor of Management Science in the Kogod School of Business at American University where he has taught courses in managerial statistics, production and operations management, and operations research for 16 years. He serves as the Feature Article Editor of the INFORMS Journal on Computing and conducts research in applied data mining and network optimization.
