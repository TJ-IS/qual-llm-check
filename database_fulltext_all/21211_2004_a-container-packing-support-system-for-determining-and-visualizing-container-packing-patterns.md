---
otero_id: 21211
otero_key: "YC96BEKC"
title: "A container packing support system for determining and visualizing container packing patterns"
authors: "Chen-Fu Chien; Jing-Feng Deng"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00192-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A container packing support system for determining and visualizing container packing patterns

Chen-Fu Chien\*<sup>,1</sup>, Jing-Feng Deng

Department of Industrial Engineering and Engineering Management, National Tsing Hua University, 101 Section 2 Kuang Fu Road, Hsinchu 30043, Taiwan, ROC

Accepted 30 September 2002

## Abstract

Relatively few approaches have been developed to solve the container-packing problem despite its important industrial and commercial applications. This study constructs a container packing support system capable of incorporating the computational algorithm, graphic user interface (GUI) input/output interface, and a simulation program for illustrating the container packing process in steps. A numerical example is used to illustrate the proposed container packing support system. We use real data to compare the solutions derived by the proposed algorithm with those of a greedy algorithm and the original solutions of a local transportation company. The results demonstrate the effectiveness and practical viability of this approach. <sup>D</sup> 2002 Elsevier B.V. All rights reserved.

Keywords: Container packing; Decision support system; Cutting and packing; Knapsack; Heuristics; Combinatorial optimization

## 1. Introduction

This paper describes the development of a computational procedure and container packing support system to determine and visualize the container packing pattern. Packing pooled shipment in containers is a complex procedure that heavily relies on workers’ experience. It often takes several days to allocate the pooled goods into a number of containers and then pack the allocated goods into the containers. Occasionally, workers must unload some containers and then reload them in different patterns to pack more goods in the containers. Thus, a container packing support system capable of flexibly determining the container packing patterns is needed.

Container packing [2,10,11,17] and related problems, e.g., knapsack [12,13], cutting and packing [6,7], and pallet loading [16], have received considerable attention. Related studies attempt to effectively optimize the allocation of limited resources (e.g., space). Knapsack problems aim to pack a number of objects that have different profits into a knapsack with limited volume. Cutting and packing problems involve different dimensions, i.e., one-dimensional cutting [12], twodimensional cutting [1,8], three-dimensional cutting [3,4], and others [5]. Related studies thoroughly examine one-dimensional cutting and two-dimensional cutting problems by extending their methods to higher dimensional cutting stock problems if possible. Among their approaches, heuristic methods have been developed based on expert knowledge and operation rules [2,10]. On the other hand, exact methods exist based on dynamic programming, linear programming, and integer programming [14,15]. In addition, hybrid approaches including genetic algorithm have been applied to the container packing problem. For example, Gehring and Bortgeldt [9] first used a greedy algorithm to generate a number of disjunctive vertical box strips and then applied genetic algorithm to arrange the box strips on the container floor according to a given optimization criteria. However, straddling across adjacent strips is not allowed and the arrangement of the box strips is a two-dimensional optimization through genetic algorithm.

Notably, a container packing support system capable of assisting users is seldom constructed since most studies focus on developing or improving the algorithms, heuristics, and mathematical models. This study develops a computer-based procedure for determining container-packing patterns (i.e., the packing order, the orientation and location of each box). A container packing support system is also constructed to increase not only the efficiency of determining container packing patterns, but also the space utility. Based on acquired knowledge from domain experts, this study also derives a computational algorithm rather than developing an exact mathematical model. A near-optimal solution within a reasonable time is often adequate for practical applications. In terms of decision support, the scope of this paper is the description of the computer-based tool to effectively determine the packing pattern and graphically present the results. We select Matlab, a programming language dedicated to technical computing, to implement the proposed algorithm and create a unique GUI to facilitate container packing processes in steps.

## 2. The approach

## 2.1. Problem structuring

This study considers a problem in which a specific number of rectangular boxes of known dimensions are packed into a fixed dimensional container to maximize the space utilization. We restrict the problem to the 20- and 40-ft dry cargo containers that are commonly used in shipments. The goods are viewed as rectangular boxes whose base axes can rotate (i.e., length and width can be interchanged) and whose height axis remains the ‘‘up’’ direction. Only the geometric factors, i.e., the sizes of containers and boxes, are considered. Boxes can be packed in any location in the container and with any other boxes. The center of gravity is assumed to be in the center of the box. For each kind of box, there are a specific number of boxes to be loaded. The boxes have the same destination. Other factors, e.g., profits of different goods and weights, are not considered, though they can be easily incorporated into the proposed system.

## 2.2. Computational procedure

A computational procedure is developed to determine the container packing patterns that consist of the packing orientation (i.e., the x–y–z dimensions) of each box and corresponding location (i.e., the reference point of packing space). The proposed computational procedure uses the wall-building concept that mirrors the actual container packing process and requires solving a series of knapsack-type sub-problems that involve complex combinatorial optimizations. In practice, the boxes are loaded into the container by building walls that are the container sections across the full height and width (length). The derived algorithm generates a set of vertical strips, combining them into lateral walls, and then combining the walls to determine the container packing patterns. The final solution is the best one among the alternative packing patterns. Fig. 1 schematically depicts the proposed procedure. Alternatively, in addition to building vertical walls, the user may also load the container by horizontal layers. However, keeping the bottom flat with a horizontal layer-bylayer approach could be difficult. In practice, loading the container by horizontal layers may lead to problems (e.g., the worker can barely enter the container to load or adjust the boxes).

Before the process begins, the dimensions of the usable space in the container are compared with those of the boxes to be packed. If the dimensions of the usable space in the container are smaller than those of the smallest box, then the container cannot pack any more boxes. Otherwise, when a usable space is found, the proposed procedure searches the box that is appropriate for the available location. In particular, the container packing procedure consists of the following steps.

![](/api/attachments/YC96BEKC/fulltext/images/159594c540f4e592178764755344599bd3b6384f7cfa3278db199f40f25e9781.jpg)  
Fig. 1. Computational procedure.

## 2.2.1. Step 1: initialization

The users input the required data by select a data file of specific shipment (e.g., goods<sup>\_</sup>1.txt) that consists of the box length, width, height, Type, and the numbers of same-size boxes. The algorithm then ranks the boxes in the order based on the following five ranking criteria:

Rank 1. Select the box with larger base dimensions (i.e., the length and the width).

Rank 2. Select the box with a larger base area.

Rank 3. Select the box with a larger x-dimension (i.e., length).

Rank 4. Select the box with a larger y-dimension (i.e., width).

Rank 5. Select the box with a larger z-dimension (i.e., height).

The above criteria are used to prioritize the boxes since the box with larger base dimensions, i.e., the length and the width, should be selected earlier and packed in a lower place. Since this procedure stacks boxes in order, the lower box should have a larger base so that the strip is stable. The boxes can be rotated to different orientations.

## 2.2.2. Step 2: select a box in the ranking order

A box to be packed is selected according to the ranking order. The initially packed box determines the length and width of the corresponding strip. As some boxes are packed, loading the larger boxes of goods becomes increasingly difficult because the empty space of the container becomes smaller and fragmented.

## 2.2.3. Step 3: summarize the empty spaces

This step summarizes the available rectangular spaces in the container. Initially, no box is loaded into the container so that the whole container is treated as a whole space. The initial spatial matrix representation [17] is created according to the container dimensions, For example, the initial spatial matrix representation of a 20-ft container of the dimensions (length, width, height)=(590, 230, 240) is as follows.

$$
\left[ \begin{array}{c c} 2 4 0 & 5 9 0 \\ 2 3 0 & 0 \end{array} \right]\tag{1}
$$

When a box is loaded into the container, the space is cut into sections. Fig. 2 illustrates the spatial representations showing that a box of Type #10 is packed into the empty 20-ft container. The reference point (0, 0, 0) of a rectangular space is denoted by the X, Y, and Z axes (i.e., the inner-left-bottom corner) as shown in Fig. 2. Thus, the container space is horizontally cut into two sections including the container space from Z = 0 to Z = 120 and the container space from Z = 120 to Z = 240 as shown in Fig. 2(a) and (b), respectively. The initial spatial matrix representation of container space is thus updated as matrices (a) and (b) as follows.

$$
\left[ \begin{array}{c c c} 1 2 0 & 2 0 0 & 5 9 0 \\ 1 0 0 & - 1 0 & 0 \\ 2 3 0 & 0 & 0 \end{array} \right]\tag{2a}
$$

$$
\left[ \begin{array}{c c c} 2 4 0 & 2 0 0 & 5 9 0 \\ 1 0 0 & 0 & 0 \\ 2 3 0 & 0 & 0 \end{array} \right]\tag{2b}
$$

Empty space is represented by matrix cells with value 0. Herein, ‘‘-10’’ is used to denote the box of Type #10 that is packed into the space of the dimensions (length, width, height)=(200, 100, 120) represented as a submatrix of matrix (2a).

![](/api/attachments/YC96BEKC/fulltext/images/fa4834bcb1c53046edbf55bce90a9ba711bf22ed007c29dad29d697af10d682c.jpg)  
Fig. 2. Illustration of spatial matrix representation.

As more goods are loaded into the container, the container space is continuously cut into more small spaces. First, the proposed algorithm searches the empty spaces that are denoted as ‘‘0’’ in the spatial representation matrices. Second, it merges the fragmented spaces that belong to the same strips, i.e., the reference points of the spaces that have the same xaxis and y-axis coordinates, into a large rectangular space. In other words, spaces are collected upward and then merged. Then, the spaces that belong to the same lateral (or longitudinal) wall, i.e., the reference points of the spaces that have the same x-axis (or yaxis) and z-axis coordinates, are merged again. Restated, the small spaces that are next to each other and belong to the same strip or wall are collected and then merged into a large rectangular space iteratively to accommodate the unallocated boxes to reduce the wastage of pieced spaces.

Then, we check whether there are suitable empty spaces for the considered box. If yes, the procedure continues to STEP 4. If all the empty spaces are compared and none of them can accommodate the considered box, it goes back to STEP 2 and selects the next box in the order until all the boxes are considered.

## 2.2.4. Step 4: match the box with the suitable empty spaces

The suitable spaces for packing the considered box are searched by comparing the dimensions of the box and the dimensions of the empty spaces summarized in STEP 2. We rank the suitable spaces, by checking their referencing points, that the inner and lower spaces have higher priorities. That is, the algorithm prioritizes the suitable spaces based on the following criteria:

Rank 1. Select the space whose reference point has the smallest x-axis coordinate.

Rank 2. Select the space whose reference point has the smallest y-axis coordinate.

Rank 3. Select the space whose reference point has the smallest z-axis coordinate.

The boxes are packed and the empty spaces are matched according to the ranking criteria. Thus, a vertical strip is built by stacking the boxes into the spaces with the same x-axis and y-axis coordinates. When the empty space in the strip is inappropriate for the chosen box, the box is packed in the next strip. We combine the strips in the same section into a lateral wall as illustrated in Fig. 3. When the wall has been completely built, we begin to build the next wall. Also, we pack the box in the next section to build another lateral wall if there are no suitable boxes to complete the existing walls.

## 2.2.5. Step 5: pack the box, update the data, and update the spatial representations

We pack the box into the corresponding location of the fittest space and update the spatial representations. Also, we update the data by removing the packed box from the list of unpacked boxes.

Then, we determine whether any boxes can be packed into the empty space. If so, the containerpacking process is continued to select the next box; otherwise, the packing process is finished and goes to STEP 6.

## 2.2.6. Step 6: stop the packing process and generate the output

The packing processes stop when all the empty spaces are smaller than the unpacked boxes or all the boxes are packed. The coordinates of the reference points of the packed boxes (i.e., filled spaces) and the empty spaces are recorded and tracked by spatial representation matrices.

Certainly, the box is packed in the lowest possible location of a particular strip. Nevertheless, boxes loaded in the same strip can be vertically interchanged to accommodate additional placement restriction. That is, the heavier box is packed in the lower location. Vertical strips are combined into various lateral walls and the walls are combined into the container. Also, the walls can be interchanged to accommodate the placement restriction, e.g., weight stability. The spare spaces are generated to the top of the packed goods and to the front and the right sides of the wall. Transportation companies typically squeeze goods such as clothing in these spaces in Taiwan.

## 2.3. Container packing support system

Based on the proposed computational procedure, this study develops a container packing support system to determine the packing pattern and visualize the result. Matlab is used to perform the matrix computation involved in searching and merging the spaces through the spatial matrix representation. This system consists of a database, the proposed algorithm, and graphic input/output interfaces. A graphic user interface (GUI) is used for the user to input the data and visualize the packing pattern. The user can observe the 3D graph of the packing pattern (from any perspective) step-by-step or continuously. The output report details the specific packing location of each box (i.e., the coordinates of the corresponding reference points) and its orientation (i.e., the x–y–z dimensions). The container-packing pattern can be illustrated through dynamic graphic simulation.

![](/api/attachments/YC96BEKC/fulltext/images/536f11ad2297e64f0e29543ab3b71bd3137b32dab925957e692fb0aea8b8b22a.jpg)  
Fig. 3. Illustration of lateral wall-building in 3D graph.

## 3. Validation

## 3.1. Illustrative example

The following example demonstrates the proposed algorithm and container packing support system. The proposed algorithm was successfully implemented in the Matlab programming language version 6.1 on a

Windows 2000 platform running with a Pentium II processor with 350 MHz clock speed and 256MB RAM.

STEP 1: A 20-ft dry container is considered, having a length, width, and height of 590, 230, and 240 cm, respectively. Based on the ranking criteria, the boxes of goods are sorted as given in Table 1.

Table 1  
Characteristics of sorted boxes

<table><tr><td colspan="2">Base length</td><td>Height</td><td>Number of boxes</td><td>Type</td></tr><tr><td>200</td><td>100</td><td>120</td><td>4</td><td>#10</td></tr><tr><td>200</td><td>100</td><td>100</td><td>3</td><td>#9</td></tr><tr><td>100</td><td>100</td><td>120</td><td>3</td><td>#6</td></tr><tr><td>100</td><td>100</td><td>50</td><td>2</td><td>#7</td></tr><tr><td>100</td><td>80</td><td>100</td><td>3</td><td>#5</td></tr><tr><td>100</td><td>80</td><td>50</td><td>2</td><td>#8</td></tr><tr><td>100</td><td>70</td><td>50</td><td>5</td><td>#3</td></tr><tr><td>100</td><td>70</td><td>40</td><td>5</td><td>#2</td></tr><tr><td>80</td><td>80</td><td>80</td><td>3</td><td>#4</td></tr><tr><td>50</td><td>40</td><td>50</td><td>10</td><td>#1</td></tr></table>

STEP 2: Packing is started from selecting the first box (i.e., a box of Type #10) in Table 1.

STEP 3: A search is made for the available space based on the spatial representation and, in doing so, the space of the dimensions (length, width, height)= (590, 230, 240) is found.

STEP 4: The box of Type #10 is matched with the only available space since it is smaller than the container.

STEP 5: The box of Type #10 is packed into the empty container. The whole container space is cut into sections after packing the first box and the spatial representations are updated as illustrated in Fig. 2. In addition, we update the data by deducting one from the total number of Type #10 boxes. We determine whether there are unpacked boxes. Since there are unpacked boxes, the packing process is continued by going back to STEP 2.

STEP 2: The second box (i.e., the second box of Type #10) selected from Table 1 is considered.

STEP 3: We summarize all the empty spaces in the container by first searching the spatial representation matrices and possibly merge the small spaces into lager ones. If there is no space larger than the selected box, another type of box with smaller dimensions is chosen according to the ranking criteria.

STEP 4: We match the considered box with the empty space on the top of the first box according to the ranking criteria.

STEP 5: We pack the second box into the space of the dimensions (length, width, height)=(200, 100, 120) with the reference point (x, y, z)=(0, 0, 120). The spatial representation matrices become as follows.

$$
\left[ \begin{array}{c c c} 1 2 0 & 2 0 0 & 5 9 0 \\ 1 0 0 & - 1 0 & 0 \\ 2 3 0 & 0 & 0 \end{array} \right]\tag{3a}
$$

$$
\left[ \begin{array}{c c c} 2 4 0 & 2 0 0 & 5 9 0 \\ 1 0 0 & - 1 0 & 0 \\ 2 3 0 & 0 & 0 \end{array} \right]\tag{3b}
$$

Thus, a strip is built. Next, we determine whether there are unpacked boxes. Since there are unpacked boxes, the packing process is continued by going back to STEP 2 and selecting the next box. STEP 3 summarizes all the empty spaces in the container by searching the spatial representations. Spaces are cut into more sections as more boxes have been packed into the container. We merge the spaces upward for packing boxes into strips and merge the spaces next to each other in order to build lateral walls. If there is no space larger than the selected box, another type of box, i.e., smaller (as shown in Table 1), is selected to match the empty spaces. The selected box is packed by matching the fittest space in STEP 4. Thus, the space of dimensions (length, width, height)=(200, 130, 240) with the reference point $( x , y , z ) { = } ( 0 , 1 0 0$ 0) is chosen to pack the third box of Type #10. STEP 5 updates the spatial representation matrices as follows.

$$
\left[ \begin{array}{c c c} 1 2 0 & 2 0 0 & 5 9 0 \\ 1 0 0 & - 1 0 & 0 \\ 2 0 0 & - 1 0 & 0 \\ 2 3 0 & 0 & 0 \end{array} \right]\tag{4a}
$$

$$
\left[ \begin{array}{c c c} 2 4 0 & 2 0 0 & 5 9 0 \\ 1 0 0 & - 1 0 & 0 \\ 2 0 0 & 0 & 0 \\ 2 3 0 & 0 & 0 \end{array} \right]\tag{4b}
$$

Following similar processes, the algorithm stops when no box is remaining to be packed or no available empty space is sufficiently large to accommodate the unallocated boxes. Table 2 summarizes the solution of the packed boxes in the packing order, including specific dimensions and coordinates of the reference points of the packing locations.

Table 2 Results

<table><tr><td rowspan="2">Type</td><td colspan="3">Box dimensions</td><td colspan="3">Coordinates of reference point of packed location</td></tr><tr><td>Length</td><td>Width</td><td>Height</td><td>x</td><td>y</td><td>z</td></tr><tr><td>#10</td><td>200</td><td>100</td><td>120</td><td>0</td><td>0</td><td>0</td></tr><tr><td>#10</td><td>200</td><td>100</td><td>120</td><td>0</td><td>0</td><td>120</td></tr><tr><td>#10</td><td>200</td><td>100</td><td>120</td><td>0</td><td>100</td><td>0</td></tr><tr><td>#10</td><td>200</td><td>100</td><td>120</td><td>0</td><td>100</td><td>120</td></tr><tr><td>#9</td><td>200</td><td>100</td><td>100</td><td>200</td><td>0</td><td>0</td></tr><tr><td>#9</td><td>200</td><td>100</td><td>100</td><td>200</td><td>0</td><td>100</td></tr><tr><td>#9</td><td>200</td><td>100</td><td>100</td><td>200</td><td>100</td><td>0</td></tr><tr><td>#6</td><td>100</td><td>100</td><td>120</td><td>200</td><td>100</td><td>100</td></tr><tr><td>#6</td><td>100</td><td>100</td><td>120</td><td>300</td><td>100</td><td>100</td></tr><tr><td>#6</td><td>100</td><td>100</td><td>120</td><td>400</td><td>0</td><td>0</td></tr><tr><td>#7</td><td>100</td><td>100</td><td>50</td><td>400</td><td>0</td><td>120</td></tr><tr><td>#7</td><td>100</td><td>100</td><td>50</td><td>400</td><td>0</td><td>170</td></tr><tr><td>#5</td><td>100</td><td>80</td><td>100</td><td>400</td><td>100</td><td>0</td></tr><tr><td>#5</td><td>100</td><td>80</td><td>100</td><td>400</td><td>100</td><td>100</td></tr><tr><td>#5</td><td>80</td><td>100</td><td>100</td><td>500</td><td>0</td><td>0</td></tr><tr><td>#8</td><td>80</td><td>100</td><td>50</td><td>500</td><td>0</td><td>100</td></tr><tr><td>#8</td><td>80</td><td>100</td><td>50</td><td>500</td><td>0</td><td>150</td></tr><tr><td>#3</td><td>70</td><td>100</td><td>50</td><td>500</td><td>100</td><td>0</td></tr><tr><td>#3</td><td>70</td><td>100</td><td>50</td><td>500</td><td>100</td><td>50</td></tr><tr><td>#3</td><td>70</td><td>100</td><td>50</td><td>500</td><td>100</td><td>100</td></tr><tr><td>#3</td><td>70</td><td>100</td><td>50</td><td>500</td><td>100</td><td>150</td></tr><tr><td>#2</td><td>100</td><td>70</td><td>40</td><td>200</td><td>0</td><td>200</td></tr><tr><td>#2</td><td>100</td><td>70</td><td>40</td><td>300</td><td>0</td><td>200</td></tr><tr><td>#2</td><td>100</td><td>70</td><td>40</td><td>400</td><td>100</td><td>200</td></tr><tr><td>#2</td><td>70</td><td>100</td><td>40</td><td>500</td><td>0</td><td>200</td></tr><tr><td>#2</td><td>70</td><td>100</td><td>40</td><td>500</td><td>100</td><td>200</td></tr><tr><td>#1</td><td>50</td><td>40</td><td>50</td><td>400</td><td>180</td><td>0</td></tr><tr><td>#1</td><td>50</td><td>40</td><td>50</td><td>400</td><td>180</td><td>50</td></tr><tr><td>#1</td><td>50</td><td>40</td><td>50</td><td>400</td><td>180</td><td>100</td></tr><tr><td>#1</td><td>50</td><td>40</td><td>50</td><td>400</td><td>180</td><td>150</td></tr><tr><td>#1</td><td>50</td><td>40</td><td>50</td><td>450</td><td>180</td><td>0</td></tr><tr><td>#1</td><td>50</td><td>40</td><td>50</td><td>450</td><td>180</td><td>50</td></tr><tr><td>#1</td><td>50</td><td>40</td><td>50</td><td>450</td><td>180</td><td>100</td></tr><tr><td>#1</td><td>50</td><td>40</td><td>50</td><td>450</td><td>180</td><td>150</td></tr></table>

A three-dimensional graph of the container packing support system is used to illustrate the results. As illustrated in Fig. 4, users can use the ‘‘Input Cargo Group #’’ popup\_menu on the GUI to select specific shipment data files. Also, users use ‘‘Container Type’’ popup\_menu to select available containers (e.g., 20-ft standard dry container, 40-ft standard dry container, and 40-ft extra large dry container) for loading. Then, press the ‘‘Execute’’ button to execute the computational procedure. The system can show each packing step according to the embedded algorithm and specify the dimensions and reference point of the packed box, respectively. For instance, Fig. 3 illustrates the fourth step in the packing pattern. The loaded box is shown with different colors and marked with the number of box Type (e.g., see Figs. 3 and 4). Fig. 4 illustrates the final solution of container packing pattern with detailed results in the listbox. The container space utilization rate is 83.0754%. The elapsed computing time is 5.6580 s. The developed system allows the user to rotate the figure and view the loading pattern from different angles as illustrated in Fig. 5.

## 3.2. Validation

We used actual data from a local shipping company to compare our proposed algorithm with the greedy algorithm. Table 3 summarized the results of packing 11 different containers with 49 non-identical boxes. Indeed, the example given in Section 3.1 is the first container in Table 3. Both algorithms apply the same criteria to prioritize the boxes, but the greedy algorithm’s space utilization (which does not merge fragmented spaces) was consistently less than or equal to our proposed algorithm. Our space utilization rates were better than the local shipping company’s solution (last column of Table 3) about half the time. CPU time was highly variable, but the greedy algorithm was faster only about half the time.

Experienced workers in local shipping companies often require several days to allocate and pack the pooled goods into containers. They must occasionally unload some containers and then reload them in different patterns. Because our system reduces trialand-error, domain users have reacted favorably to our system, especially the GUI that allows them to visualize the results in steps, as illustrated in Figs. 3 – 6. Fig. 6 illustrates the results of the 11th container (a 40-ft container) in which 717 boxes are loaded as given in Table 3. The container space utilization rate is 92.02% and the elapsed computing time is 370.483 s. We expect that our system, which can handle more than 1000 boxes, will help Taiwanese transportation companies improve their competitive advantage which has been eroded by rising labor cost and aging experienced workers. The sample codes and test instances will be provided upon request.

![](/api/attachments/YC96BEKC/fulltext/images/42d6900b152bdcce4b091f3598506943cde3b12ae471d39768834825af91f43d.jpg)  
Fig. 4. Input/output screen of 20-ft container packing pattern in 3D graph.

![](/api/attachments/YC96BEKC/fulltext/images/623b1cc43c65f130fe82880c63724c4dd9538ea0548172a4506767ebb94ec39a.jpg)  
Fig. 5. Input/output screen of 20-ft container packing pattern in 3D graph (rotated).

Table 3  
Comparison of greedy algorithm and proposed algorithm

<table><tr><td rowspan="2">No.</td><td colspan="3">Container dimension</td><td colspan="4">Boxes</td><td colspan="3">Greedy algorithm</td><td colspan="3">Proposed algorithm</td><td rowspan="2">Current utilization rate</td></tr><tr><td>Length</td><td>Width</td><td>Height</td><td>Length</td><td>Width</td><td>Height</td><td>Total number</td><td>Packed number</td><td>Utilization rate</td><td>CPU time (s)</td><td>Packed number</td><td>Utilization rate</td><td>CPU time (s)</td></tr><tr><td rowspan="10">1</td><td rowspan="10">590</td><td rowspan="10">230</td><td rowspan="10">240</td><td>40</td><td>50</td><td>50</td><td>10</td><td>6</td><td>0.7411</td><td>9.4240</td><td>10</td><td>0.8308</td><td>5.6580</td><td>0.8290</td></tr><tr><td>100</td><td>70</td><td>40</td><td>5</td><td>0</td><td></td><td></td><td>10</td><td></td><td></td><td></td></tr><tr><td>100</td><td>70</td><td>50</td><td>5</td><td>0</td><td></td><td></td><td>0</td><td></td><td></td><td></td></tr><tr><td>80</td><td>80</td><td>80</td><td>3</td><td>3</td><td></td><td></td><td>3</td><td></td><td></td><td></td></tr><tr><td>80</td><td>100</td><td>100</td><td>3</td><td>3</td><td></td><td></td><td>6</td><td></td><td></td><td></td></tr><tr><td>100</td><td>100</td><td>120</td><td>3</td><td>3</td><td></td><td></td><td>3</td><td></td><td></td><td></td></tr><tr><td>100</td><td>100</td><td>50</td><td>2</td><td>0</td><td></td><td></td><td>2</td><td></td><td></td><td></td></tr><tr><td>100</td><td>80</td><td>50</td><td>2</td><td>1</td><td></td><td></td><td>2</td><td></td><td></td><td></td></tr><tr><td>200</td><td>100</td><td>100</td><td>3</td><td>3</td><td></td><td></td><td>3</td><td></td><td></td><td></td></tr><tr><td>200</td><td>100</td><td>120</td><td>4</td><td>4</td><td></td><td></td><td>4</td><td></td><td></td><td></td></tr><tr><td rowspan="8">2</td><td rowspan="8">1210</td><td rowspan="8">230</td><td rowspan="8">240</td><td>30</td><td>50</td><td>50</td><td>100</td><td>0</td><td>0.8025</td><td>12.03</td><td>96</td><td>0.9522</td><td>19.55</td><td>0.8025</td></tr><tr><td>100</td><td>70</td><td>40</td><td>20</td><td>0</td><td></td><td></td><td>10</td><td></td><td></td><td></td></tr><tr><td>100</td><td>70</td><td>50</td><td>10</td><td>0</td><td></td><td></td><td>0</td><td></td><td></td><td></td></tr><tr><td>80</td><td>100</td><td>100</td><td>10</td><td>0</td><td></td><td></td><td>0</td><td></td><td></td><td></td></tr><tr><td>100</td><td>100</td><td>120</td><td>20</td><td>8</td><td></td><td></td><td>8</td><td></td><td></td><td></td></tr><tr><td>100</td><td>100</td><td>50</td><td>10</td><td>0</td><td></td><td></td><td>0</td><td></td><td></td><td></td></tr><tr><td>200</td><td>100</td><td>100</td><td>10</td><td>10</td><td></td><td></td><td>10</td><td></td><td></td><td></td></tr><tr><td>200</td><td>100</td><td>120</td><td>10</td><td>10</td><td></td><td></td><td>10</td><td></td><td></td><td></td></tr><tr><td rowspan="2">3</td><td rowspan="2">1360</td><td rowspan="2">230</td><td rowspan="2">270</td><td>80</td><td>30</td><td>40</td><td>400</td><td>234</td><td>0.8343</td><td>1134.55</td><td>234</td><td>0.8343</td><td>221.79</td><td>0.8891</td></tr><tr><td>80</td><td>30</td><td>50</td><td>400</td><td>400</td><td></td><td></td><td>400</td><td></td><td></td><td></td></tr><tr><td rowspan="5">4</td><td rowspan="5">1210</td><td rowspan="5">230</td><td rowspan="5">240</td><td>80</td><td>30</td><td>40</td><td>300</td><td>300</td><td>0.6626</td><td>1122.63</td><td>300</td><td>0.8768</td><td>234.14</td><td>0.7986</td></tr><tr><td>80</td><td>30</td><td>30</td><td>100</td><td>0</td><td></td><td></td><td>100</td><td></td><td></td><td></td></tr><tr><td>40</td><td>40</td><td>60</td><td>100</td><td>26</td><td></td><td></td><td>26</td><td></td><td></td><td></td></tr><tr><td>50</td><td>30</td><td>60</td><td>100</td><td>4</td><td></td><td></td><td>83</td><td></td><td></td><td></td></tr><tr><td>60</td><td>30</td><td>70</td><td>100</td><td>100</td><td></td><td></td><td>100</td><td></td><td></td><td></td></tr><tr><td>5</td><td>1210</td><td>230</td><td>270</td><td>80</td><td>30</td><td>40</td><td>650</td><td>630</td><td>0.8049</td><td>154.07</td><td>630</td><td>0.8049</td><td>154.07</td><td>0.8893</td></tr><tr><td>6</td><td>1360</td><td>230</td><td>270</td><td>80</td><td>30</td><td>40</td><td>750</td><td>714</td><td>0.8116</td><td>1199.50</td><td>714</td><td>0.8116</td><td>242.66</td><td>0.8642</td></tr><tr><td rowspan="2">7</td><td rowspan="2">1360</td><td rowspan="2">230</td><td rowspan="2">270</td><td>80</td><td>30</td><td>40</td><td>600</td><td>600</td><td>0.8116</td><td>1384.43</td><td>600</td><td>0.9130</td><td>255.62</td><td>0.8562</td></tr><tr><td>80</td><td>30</td><td>30</td><td>600</td><td>152</td><td></td><td></td><td>271</td><td></td><td></td><td></td></tr><tr><td>8</td><td>1210</td><td>230</td><td>280</td><td>80</td><td>30</td><td>40</td><td>750</td><td>735</td><td>0.9055</td><td>124.619</td><td>735</td><td>0.9055</td><td>141.66</td><td>0.9055</td></tr><tr><td rowspan="7">9</td><td rowspan="7">1360</td><td rowspan="7">230</td><td rowspan="7">270</td><td>60</td><td>30</td><td>30</td><td>250</td><td>0</td><td>0.4703</td><td>10.235</td><td>250</td><td>0.9555</td><td>765.44</td><td>0.8885</td></tr><tr><td>60</td><td>40</td><td>40</td><td>100</td><td>20</td><td></td><td></td><td>100</td><td></td><td></td><td></td></tr><tr><td>60</td><td>40</td><td>20</td><td>200</td><td>0</td><td></td><td></td><td>200</td><td></td><td></td><td></td></tr><tr><td>140</td><td>120</td><td>50</td><td>50</td><td>45</td><td></td><td></td><td>50</td><td></td><td></td><td></td></tr><tr><td>50</td><td>40</td><td>30</td><td>50</td><td>0</td><td></td><td></td><td>50</td><td></td><td></td><td></td></tr><tr><td>60</td><td>40</td><td>30</td><td>100</td><td>0</td><td></td><td></td><td>100</td><td></td><td></td><td></td></tr><tr><td>80</td><td>30</td><td>50</td><td>400</td><td>400</td><td></td><td></td><td>400</td><td></td><td></td><td></td></tr><tr><td rowspan="5">10</td><td rowspan="5">1210</td><td rowspan="5">230</td><td rowspan="5">240</td><td>80</td><td>30</td><td>40</td><td>200</td><td>200</td><td>0.5783</td><td>69.149</td><td>200</td><td>0.9308</td><td>438.03</td><td>0.9765</td></tr><tr><td>80</td><td>50</td><td>20</td><td>200</td><td>16</td><td></td><td></td><td>200</td><td></td><td></td><td></td></tr><tr><td>50</td><td>30</td><td>60</td><td>200</td><td>200</td><td></td><td></td><td>33</td><td></td><td></td><td></td></tr><tr><td>80</td><td>30</td><td>30</td><td>200</td><td>2</td><td></td><td></td><td>200</td><td></td><td></td><td></td></tr><tr><td>80</td><td>30</td><td>20</td><td>200</td><td>0</td><td></td><td></td><td>200</td><td></td><td></td><td></td></tr><tr><td rowspan="7">11</td><td rowspan="7">1360</td><td rowspan="7">230</td><td rowspan="7">270</td><td>60</td><td>40</td><td>30</td><td>150</td><td>0</td><td>0.3081</td><td>13.9</td><td>150</td><td>0.9202</td><td>370.483</td><td>0.5705</td></tr><tr><td>80</td><td>30</td><td>40</td><td>150</td><td>2</td><td></td><td></td><td>150</td><td></td><td></td><td></td></tr><tr><td>50</td><td>50</td><td>40</td><td>100</td><td>10</td><td></td><td></td><td>56</td><td></td><td></td><td></td></tr><tr><td>160</td><td>120</td><td>160</td><td>10</td><td>8</td><td></td><td></td><td>8</td><td></td><td></td><td></td></tr><tr><td>60</td><td>40</td><td>40</td><td>150</td><td>0</td><td></td><td></td><td>150</td><td></td><td></td><td></td></tr><tr><td>40</td><td>40</td><td>30</td><td>100</td><td>0</td><td></td><td></td><td>53</td><td></td><td></td><td></td></tr><tr><td>40</td><td>30</td><td>30</td><td>150</td><td>7</td><td></td><td></td><td>150</td><td></td><td></td><td></td></tr></table>

![](/api/attachments/YC96BEKC/fulltext/images/896a0d05a2ee733775b0b7ec88eeedcc4ab07eb81c8b755c6a91ef2e981d1fa0.jpg)  
Fig. 6. Illustration of 40-ft container packing pattern with 717 boxes.

## 4. Concluding remarks

This study proposes a computational procedure and a container packing support system to determine the container packing patterns efficiently and visualize the results. A numerical example is used to illustrate the computational procedures of the derived algorithm and demonstrate the developed system. A computer programming language for technical computing, i.e., Matlab, is used to perform the involved matrix computation. With the graphical simulation developed herein, the packing process can be shown in a sequential manner. In a typical problem using actual data, our solutions compare well both with the greedy algorithm and with the original solution by the shipping company, suggesting that our system has practical utility. Wastage of fragmented spaces is generally inevitable to load goods with different shapes and sizes into a container. Straddling across adjacent strips and walls is not allowed in the existing multistage cutting approaches to packing boxes into the container [3,9]. The proposed algorithm incorporates a procedure to continuously search and merge fragmented spaces to reduce the wasted space. The near-optimal solution of the proposed algorithm may be good enough in the tradeoffs of the required time and labor. Further research has to be done to implement the container packing support system in various domains. As a partial goal, we are planning to make the system accessible through Internet to exchange ideas with researchers and practitioners to improve the system features.

## Acknowledgements

This research is partially supported by National Science Council, ROC (NSC89-2213-E-007-029). Dr. Chen-Fu Chien is also under Fulbright Program to be a Visiting Professor in the Department of Industrial Engineering and Operations Research, UC-Berkeley, from 2002 to 2003. Special thanks go to the Worldwide Freight Terminals, in particular to Mr. Yu-Jen Yu for his kind assistance. The authors also wish to thank the referees who provide invaluable suggestions.

## References

[1] J.E. Beasley, Algorithms for unconstrained two-dimensional guillotine cutting, Journal of the Operational Research Society 36 (4) (1985) 297– 306.

[2] E.E. Bischoff, M.D. Marriott, A comparative evaluation of heuristics for container-loading, European Journal of Operational Research 44 (1990) 267– 276.

[3] C. Chien, W. Wu, A recursive computational procedure for container loading, Computers & Industrial Engineering 35 (1998) 319–322.

[4] C. Chien, W. Wu, A framework of modularized heuristics for determining the container loading patterns, Computers & Industrial Engineering 37 (1999) 339 – 342.

[5] C. Chien, S. Hsu, C. Chen, An iterative cutting procedure for determining the optimal wafer exposure pattern, IEEE Transactions on Semiconductor Manufacturing 12 (3) (1999) 375–377.

[6] K.A. Dowsland, W.B. Dowsland, Packing problems, European Journal of Operational Research 56 (1992) 2 – 14.

[7] H. Dyckhoff, A typology of cutting and packing problems, European Journal of Operational Research 44 (1990) 145 – 159.

[8] D. Fayard, V. Zissimopoulos, An approximation algorithm for solving unconstrained two-dimensional knapsack problems, European Journal of Operational Research 84 (1995) 618 – 632.

[9] H. Gehring, A. Bortgeldt, A genetic algorithm for solving the container loading problem, International Transactions in Operational Research 3 (5/6) (1997) 401 – 418.

[10] H. Gehring, K. Menschner, M. Meyer, A computer-based heuristic for packing pooled shipment containers, European Journal of Operational Research 44 (1990) 277 – 288.

[11] J.A. George, D.F. Robinson, A heuristic for packing boxes into a container, Computers & Operations Research 7 (1980) 147–156.

[12] P.C. Gilmore, R.E. Gomory, A linear programming approach to the cutting-stock problem, Operations Research 9 (1961) 849– 859.

[13] P.C. Gilmore, R.E. Gomory, The theory and computation of knapsack functions, Operations Research 14 (1966) 1045 – 1074.

[14] J.C. Herz, Recursive computational procedure for two-dimensional stock cutting, IBM Journal of Research and Develop ment 16 (5) (1972) 462–469.

[15] M. Hifi, V. Zissimopoulos, A recursive exact algorithm for

weighted two-dimensional cutting, European Journal of Operational Research 91 (1996) 553–564.

[16] F.H. Liu, C.J. Hsiao, A three-dimensional pallet loading method for single-size boxes, Journal of the Operational Research Society 48 (6) (1997) 726– 735.

[17] B.K.A. Ngoi, M.L. Tay, E.S. Chua, Applying spatial representation techniques to the container packing problem, International Journal of Production Research 32 (1) (1994) 111 – 123.

![](/api/attachments/YC96BEKC/fulltext/images/854420c03c43f5c43a38772e5c24415c53777e84bd07f12c486a075c201a5b98.jpg)

Chen-Fu Chien received his BS degree with double majors in Industrial Engineering and Electrical Engineering from the National Tsing Hua University in 1990. He received his MS and PhD degrees in Industrial Engineering, with two minors in Statistics and Business, from the University of Wisconsin-Madison, USA in 1994 and 1996, respectively. Dr. Chien is an Associate Professor in the Department of Industrial Engineering and

Engineering Management, National Tsing Hua University. He is a member of the Phi Tao Phi Honor Society, INFORMS, CIIE, and CIDS. His research works appear in Computers and I.E., IEEE Trans. on Power Delivery, IEEE Trans. on Power Systems, IEEE Trans. on Semiconductor Manufacturing, Int. J. of CIM, Int. Trans. in OR, J. of MCDA, R and D Management, and JCIIE. He received the Distinguished Young Faculty Research Award from National Tsing Hua University, Best Paper Award from Chinese Institute of Industrial Engineers, Best Research Awards from the National Science Council, Distinguished Industrial Collaboration Award from the Ministry of Education, and Best Engineering Paper Award by Chinese Institute of Engineers, Taiwan. His research and development efforts center on multi-criteria decision analysis, decision support systems, data mining, and statistical decision making.

![](/api/attachments/YC96BEKC/fulltext/images/28ba7d5701d1431078724279b4a162eeafb7e2f5a11e88078987e912922eac5d.jpg)

Jing-Feng Deng is a PhD student in the Department of Industrial Engineering and Engineering Management at National Tsing Hua University, Taiwan. He received his MS degree in Industrial Engineering and Engineering Management from National Tsing Hua University in 2000. His research works appear in IEEE Trans. on Semiconductor Manufacturing and Int. Trans. in OR. His current research interests include decision support system, combinatorial optimization, and scheduling.
