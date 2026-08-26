---
otero_id: 26711
otero_key: "5RKBJCSW"
title: "Using Treemaps to Visualize the Analytic Hierarchy Process"
authors: "Toshiyuki Asahi; David Turo; Ben Shneiderman"
year: "1995"
journal: "Information Systems Research"
doi: "10.1287/isre.6.4.357"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [129.105.215.146] On: 18 September 2016, At: 12:36 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## H4R

![](/api/attachments/5RKBJCSW/fulltext/images/4510118e510d712c83c5e2da15c256db35cc8f88edac0510ee42270b729046f7.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Using Treemaps to Visualize the Analytic Hierarchy Process

Toshiyuki Asahi, David Turo, Ben Shneiderman,

To cite this article:

Toshiyuki Asahi, David Turo, Ben Shneiderman, (1995) Using Treemaps to Visualize the Analytic Hierarchy Process. Information Systems Research 6(4):357-375. http://dx.doi.org/10.1287/isre.6.4.357

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1995 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/5RKBJCSW/fulltext/images/548072b2ae5b9b0f4bd94edf13f3242618e7371079b78a7621eefe7c96159580.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Using Treemaps to Visualize the Analytic Hierarchy Process

Toshiyuki Asahi\*

Human-Computer Interaction Laboratory

University of Maryland

David Turo\*

College Park, Maryland 20740

Human-Computer Interaction Laboratory and

Department of Computer Science

University of Maryland

Ben

Shneiderman

College Park, Maryland 20740

Department of Computer Science,

Human-Computer Interaction Laboratory and

Institute for Systems Research

AV Williams Building

University of Maryland

College Park, Maryland 20740

Treemaps, a visualization method for large hierarchical data spaces, are used to augment the capabilities of the Analytic Hierarchy Process (AHP) for decision-making. Two direct manipulation tools, presented metaphorically as a "pump" and a "hook," were developed and applied to the treemap to support AHP sensitivity analysis. Users can change the importance of criteria dynamically on the two-dimensional treemap and immediately see the impact on the outcome of the decision. This fluid process dramatically speeds up exploration and provides a better understanding of the relative impact of the component criteria. A usability study with six subjects using a prototype AHP application showed that treemap representation was acceptable from a visualization and data operation standpoint.

Visualization—Treemap—Analytic Hierarchy Process, AHP-Decision support—User interfaces

## Introduction

Tisualizing information to promote ease of comprehension and dissection is a primary goal of user interface research. Information—often very abstract must be transformed into coherent visual representations. These visualizations are customarily read-only; amplification of information-based work processes can be obtained, however, by allowing direct manipulation of the visualization itself.

Treemaps graphically represent hierarchical information via a two-dimensional

1047-7047/95/0604/0357/\$01.25 Copyright © 1995, Institute for Operations Research and the Management Sciences rectangular map, providing compact visual representations of complex data spaces through both area and color (Shneiderman 1992). Their efficiency for particular data searching tasks has been tested through controlled studies (Turo and Johnson 1992, Turo 1993) with primary benefits seen for two types of tasks: location of outliers in large hierarchies and identification of cause-effect relationships within hierarchies. By extending the treemap into a “read/write"graphic through direct manipulation tools, the user is given the capability to massage the data and perform the outlier and cause-effect tasks much more effectively. AHP, given its decision tree hierarchy and inherent need for large-scale data visualization and user manipulation, is an appropriate choice for treemap visualization.

Within this paper, the AHP is introduced more formally. Treemap applicability to AHP is then discussed; two new direct manipulation tools are added to the treemap to produce a total AHP solution. Three distinct real-world examples and a preliminary usability study demonstrate the treemap's viability in the AHP arena. Future research avenues are then considered.

## Analytic Hierarchy Process

AHP was developed to promote improved decision making for a specific class of problems that involve prioritization of potential alternate solutions through evaluation of a set of criteria elements. These elements may be divided into subelements and so on, thus forming a hierarchical decision tree. Once the hierarchical problem definition has been established, these criteria are weighted individually at every level relative to each other; prioritization of the alternate solutions can then be obtained via evaluation of these weights (Saaty 1980, 1982).

As an example, a problem might be "What car to buy?"The potential solutions are all of the car models available for purchase in the nearby geographic area. The major criteria at the first-level of the decision tree are price, quality, customer support and road handling (there are undoubtedly others). Price can be broken down further into list price, rebates, dealer incentives and financing. Quality can be broken down into consumer reports from previous years, recalls for similar models and miles-pergallon estimates. This process of refining criteria is what forms the decision tree.

AHP suits a wide range of applications including transport study, technological choice, resource allocation and organization planning (Saaty and Vargas 1991). The method has been gaining popularity as a viable decision-support tool in a number of fields such as economics, politics, marketing, sociology, and management (Finnie et al. 1983, Zahedi, 1986). A description of the procedure is given here in five stages:

1. Criteria are identified from the problem space. A hierarchical structure is formed by using the overall goal as a root of the decision tree and making each “major" criterion a child. Each criterion in turn is detailed to provide additional descendants. Once the decision tree is completely formed, all n alternatives are assigned to every leaf node in the tree. (Assuming m leaves (subcriteria) prior to this action, the new tree will have m\*n leaves with each alternative appearing m times.)

2. Relative importance (or preference) for each criterion is rated among those which have same parent node (the goal or the parent criteria), i.e., siblings. Rating is done using the scaled one-pair comparison method. That is, for all distinct pair of subcriteria under a criteria, a single rating from 1 to 9 is assigned corresponding to the verbal expressions in Figure 1.

A square matrix is formed when every two criteria are compared. The matrix has the property that element $a _ { i j } = 1 / a _ { j i }$ (if item i is 2 times as important as item $j ,$ then item j is  as important as item i). The relative importances are given as a normalized eigenvector of the pairwise comparison matrix, guaranteeing that the sum of relative importances of siblings always equals one.

Using Treemaps to Visualize the AHF

<table><tr><td>Intensity of Importance</td><td>Definition</td></tr><tr><td>1</td><td>Equal importance of both elements</td></tr><tr><td>3</td><td>Weak importance of one element over another</td></tr><tr><td>5</td><td>Essential or strong importance of one element over another</td></tr><tr><td>7</td><td>Demonstrated importance of one element over another</td></tr><tr><td>9</td><td>Absolute importance of one element over another</td></tr><tr><td>2, 4, 6, 8</td><td>Intermediate values between two adjacent judgements</td></tr></table>

FIGURE 1. The Pairwise Comparison Scale (Saaty and Vargas 1991).

3. Relative importance for each alternative is rated in the same way as for criteria—all n alternatives are judged against each of the m subcriteria.

4. Absolute importance for all criteria and alternatives are calculated. The absolute importance of the root node (the “goal") is set to 1. The absolute importance of all other nodes (criteria or alternatives) is calculated by multiplying a node's relative importance by its parent node's absolute importance.

5. For each alternative, all of its m absolute importances are summed; this value equals the total number of preference points. Alternatives with greater amounts of points are preferable to alternatives with lesser amounts of points.

Figure 2 shows an example of a decision tree used by AHP to solve the problem of “software package selection."Stage 1 involves identification and subdivision of problem-space criteria: service, specification, price and usability are major criteria, and these are further subdivided into 13 minor criteria to form a four-level decision tree. Three alternatives, "soft A," "soft B,"“soft C," are assigned to all 13 leaf nodes as child nodes that, for convenience, are simply represented on only the “Service" criteria.

Stage 2 assigns relative values to each of the nodes (on Figure 2, values are attached to each node using a “relative importance/absolute importance"format). Relative importances are produced through a pairwise-comparison method. For example, the criteria of“warranty,"“instruction" and “maintenance" are compared in three pairwise comparisons and rated with respect to their parent criterion “service." An example matrix of relative comparisons is given in Figure 3. The relative importances are ascertained by calculating the eigenvector of the matrix. They are 0.4, 0.2 and 0.4 respectively in this simple case.

Stage 3 evaluates relative importances for every alternative. In Figure 1, these are 0.1. 0.4 and 0.5 for packages A, B and C for the “Warranty"; other subcriteria have different weights

In Stage 4, absolute importance is calculated by multiplying relative importance by the parent node's absolute importance. For the second-level criteria, this simply means absolute importance is set equal to relative importance, as the root node's absolute importance is 1. For a third-level criterion such as "Warranty," the absolute importance equals its relative importance of 0.4 multiplied by “service"'s absolute importance of 0.2—this equals 0.08. At the alternative level, the same multiplicative process occurs, and results are established for each alternative under each low-level criterion.

Asahi • Turo · Shneiderman  
![](/api/attachments/5RKBJCSW/fulltext/images/ecec1abe4c28be0cf9a6ba0850a1f5026944364b7e8a4595db02d310b391b663.jpg)  
FIGURE 2. A Hierarchical Structure for AHP

Stage 5 sums 13 separate results for each alternative to produce preference points, which are then used for prioritization purposes. In this case, the sums for software packages A, B, and C under “Service" are 0.048, 0.080 and 0.072, respectively. If their totals are 0.252, 0.220 and 0.328 under all the remaining criteria, total final preference points will equal 0.300, 0.300 and 0.400. Package C is thus more preferable than the other two packages.

![](/api/attachments/5RKBJCSW/fulltext/images/eec29ade0e8b50379a6e8b976434e4857ec38c58b2d1cf1d9a48f02fb46dab32.jpg)  
FIGURE 3. Pairwise Comparison Matrix

For practical use, though, a one-time rating result is not reliable enough. “Sensitivity analysis" is the process which examines how strongly the rating of a particular criterion or alternative affects the total amount of preference points (Tone 1990). It is clear that if a criteria has large absolute importance, the change of the relative importance of the child nodes can strongly influence the result. Processes and tools which allow experimentation with and examination of the structure of the AHP decision-making process model to ascertain causes and stability of particular results are therefore indispensable to sensitivity analysis.

A PC software product called “Expert Choice" is one of several available (others include HIPRE and Criterium) to facilitate AHP (Forman 1989). It supports the various stages of the AHP procedure: the data input of criteria and alternatives and rating via the pairwise comparison method to the ranking via preference points. For sensitivity analysis, three graphic types are provided which enable users to examine how the change of certain criteria's relative importance will affect total preference points. For example, users may directlý alter a criterion's importance by changing the length of its representative bar in a graph. However, it is still difficult for users to guess or grasp the reason why the overall result changes as displayed during the operation, because the entire tree structure and each element's value cannot be displayed simultaneously. Users are required to switch the display by means of a mode selection or scroll function when they need to refer to both hierarchical structure and an element's value. At the sensitivity analysis stage, users must maintain the decision tree structure in their mind because it cannot be displayed simultaneously with the graph display modes. Treemaps are seen as a mechanism to simultaneously utilize the screen space more effectively, reduce user mental load and still enable sensitivity analysis to be performed.

## Treemap Representation for AHP

The treemap can represent both hierarchical structure and each elements' quantitative information simultaneously in a two-dimensional rectangular space; 100% of the designated screen area is utilized. Application arenas for treemaps have included computer directory browsing, stock market portfolio visualizations, an NBA player statistical browser and a budget viewer (Jungmeister and Turo 1992, Turo and Johnson 1992).

Treemaps are generated using a straightforward algorithm known as “slice-anddice." The root node of a hierarchy is represented by the entire screen area. For the root node's children, the screen area is sliced (either horizontally or vertically) to create smaller rectangles with area dependent upon the value of a particular weighting attribute (Shneiderman 1992). Each node is then processed recursively, with the direction of the slicing switched by 90 degrees for each level.

Since the decision-making processes are represented by hierarchical trees in AHP, these trees translate directly to the treemap visualization method. Figure 4 is an example of a treemap generated with a prototype AHP application for the same decision-making problem that was shown in Figure 2. A base rectangle representing the goal of decision-making is divided into small rectangular areas proportional to their relative importances. Users can identify any criterion by labels displayed in the offset areas (offset areas are also helpful for users to recognize the hierarchical structure).

![](/api/attachments/5RKBJCSW/fulltext/images/c9dd30da1b036c7fabaeb538ab65884e9201929c7a0ecdb82dab654e4e8b5f9e.jpg)  
FIGURE 4. Screen Image of the AHP Prototype.

The drawing algorithm is graphically shown in Figure 5. First, the base rectangle (the “root," software package selection) is partitioned for level 2 criteria according to their relative importances, leaving the upper and left side areas for the offset (Figure 5a). Each Level 2 criterion is divided further by its child criteria proportional to their relative importances; Figure 5b displays this process for the Level 2 criterion of “service"; Figure 5c displays the resultant treemap when all Level 2 criteria have been processed. Finally, every level 3 criterion is partitioned by the three alternative solutions (Figure 5d). Since all nodes are created by partitioning their parent node rectangles by their relative importances, size of each area comes to represent its absolute importance.

A unique feature of the AHP hierarchy is that the leaves of every branch always consist of the same set of alternatives. In the prototype system, distinctive colors are assigned to each alternative so that users can easily identify it. (Color information has been used to represent another attribute in other treemap prototypes.) A key is provided to allow the user to identify corresponding alternatives or modify the color of individual alternatives.

A bar graph for showing the total preference points of each alternative is separately displayed just below the completed treemap in the prototype application (Figure 4), because such values cannot be displayed plainly on the treemap itself. The actual numerical value of any of the bars is temporarily displayed while it is “selected" with the mouse cursor. The prototype also allows any of the nodes (a goal, a criterion or an alternative) to be set as the “current node" by clicking the mouse. Current node relative and absolute importances are displayed numerically at the right side of the screen at all times. Additionally, a zooming capability is provided to allow any node in the tree to become the root node, thus obtaining more screen area for that node's descendants.

![](/api/attachments/5RKBJCSW/fulltext/images/5190e3596c7ab55d67ee8d7a1479d05bed31d03605e586031ad39af248824a18.jpg)

Using Treemaps to Visualize the AHF  
![](/api/attachments/5RKBJCSW/fulltext/images/6815cb8e9bc582748042a3a05d74a37f004667299ee863489d6f0d6766e8a630.jpg)

![](/api/attachments/5RKBJCSW/fulltext/images/dd5172f7a85b4bf84aa830e5fa65ed35caf62914d1bc0a6d7909f8805db2b2ad.jpg)

![](/api/attachments/5RKBJCSW/fulltext/images/f92913b49721684abe0ffac454c0026864c605bfb2379f26257417a3601731d7.jpg)  
FIGURE 5. Treemap Drawing for an AHP Hierarchy.

Treemaps were originally developed for visualizing hierarchical data containing large numbers of nodes that are difficult to grasp with any other representation. The resolution of the available display directly correlates to the amount of information that can be presented. Practical limits of criteria or alternatives at each tree level are estimated to be between seven and nine in order to keep the results of pairwise comparisons consistent and reliable (Saaty 1980). A survey paper of AHP applications, (Zahedi 1986), found that the number of hierarchy levels did not exceed seven and the alternatives were limited to avoid excessive input requirements. Given these factors, the prototype was developed on a VGA screen supporting 640 × 480 pixel resolution.

A decision tree can contain as many nodes as practically possible given human tolerance and processing limitations. For example, the decision-making model of site selection (Figure 12) might have another level: factors in the hierarchy that represent groups of people having different viewpoints (Tone and Yanagisawa 1989). (These factors are called “actor" (Saaty 1980).) Simply adding this one level, though, 'multiplies the number of nodes, making it difficult for users to digest the entire structure. In such cases, the treemap approach is advantageous because it can display the entire model in a screen no matter how big the hierarchy is. (Figure 6 gives the treemap representation of the example of site selection problem with the actor elements.)

![](/api/attachments/5RKBJCSW/fulltext/images/7c40c147ded9d17f3a280d31004391a3fc0a29c680829ca428cc2844557ff3fe.jpg)  
FiGURE 6. A Decision-making Model of Site Selection with Actors.

The primary advantage in representing the AHP decision tree with a treemap is that the entire display space is shown at once, simultaneously showing cause-effect relationships for the number of preference points while eliminating the need for mental gymnastics to piece together the entire tree. If tools to directly manipulate values represented in the treemap are developed, the goal of providing a viable sensitivity analysis environment will be realized.

## Data Manipulation Tools

## Hook: Altering Sibling Weights

What is the most direct and intuitive way for a mouse-driven user interface to manipulate the information represented by the treemap's rectangles? One possibility is to grab boundary lines and drag them. In the prototype system, the “hook"tool is introduced for this purpose. The mouse cursor changes its shape to a hook when a user selects the “hook" icon in Figure 4 so that the cursor's current function is clearly identified. Figure 7 shows this tool at work: the user can grab any boundary line and move it (a horizontal line moves in a vertical direction and vice versa).

All hierarchical relations are maintained during hook manipulation. All relative proportions are maintained as well, with the exception of the two sibling "hook nodes" involyed in the hook operation. The children of these hook nodes are either reduced or expanded proportionally dependent upon the direction of the hook. The siblings of the hook nodes are not changed in absolute size. A hook operation for the second level criteria of “specification" and “price" is shown in Figure 7—the children of these two hook nodes expand or reduce proportionally (e.g., “specification"'s area grows larger, so its children expand), but first-level siblings “service" and “usability" are not affected. A ruler is displayed temporarily during the hook operation to aid in evaluating the relative sizes amorig all sibling components. The ruler pops up next to the siblings of the hook node; its orientation (horizontal or vertical) is dependent upon the slice direction of the hooked boundary (e.g., hooking a vertical slice results in a horizontal ruler).

![](/api/attachments/5RKBJCSW/fulltext/images/b6461e79db81aff6fb5c275756ca47e763da90394119fa9c00173daa79a8175c.jpg)  
FIGURE 7. Data Manipulation with the Hook Tool.

When applied to the AHP, the hook tool is thought to be useful when a user has a certain ratio of two or more criteria or alternatives in mind and wants to adjust the decision tree to reflect this. If there is a need, for example, to set criterion A. B. C and D to the ratio 1:2:1:1, this can be accomplished by sliding three boundary lines to desired positions one by one (the ruler displayed during the hook operation is used for fine adjustments).

## Pump: Altering Criteria Importance

The hook tool is useful for altering sibling weights on a particular level. However. suppose an individual wants to only change the weight of one criterion while keeping the proportions of its siblings constant. We introduce a tool called a “pump" for this task. The pump is activated by clicking upon the pump icon illustrated in Figure 4, which changes the cursor to a pump. Users can increase or decrease any rectangle's area gradually by placing the “pump" cursor into the area and pushing the mouse button (the left button inflates an area, the right button deflates). As a rectangle is inflating/deflating, other sibling rectangles that have the same parent will also deflate/ inflate and maintain their relative size ratio.

Figure 8 is an example of the pump operation. Suppose the first-level criteria have relative importances 0.1, 0.4, 0.2 and 0.3 when read from left to right in Figure 8a. When the “specification" is pumped up to 0.7, "service," "price," and "usability" decrease to 0.05, 0.1 and 0.15, respectively (Figure 8b). If “specification" is deflated to 0.1, its three siblings inflate to 0.15, 0.3 and 0.45, keeping their relative ratio of 1:2:3 (Figure 8c). Pumping speed, which actually means the amount of relative importance that changes when the mouse button is pushed one time, can also be adjusted by users. Usually, the speed is set small enough to produce continuous motion.

This kind of operation is required for sensitivity analysis when examining the influence of an individual criterion as described in the following section. The hook tool is inappropriate for such tasks as the relative weights of other nodes are impacted.

Any change of the treemap as a result of user's operation with these tools is displayed rapidly. The final result displayed with the prototype's bar graph also reflects the change of the treemap without delay. The visual feedback is given via fluid animation. Pumps can be applied to alternatives in the same manner to change its importance relative to its siblings.

## Reverse Pumping

Additional functionality is provided to support “reverse analysis" of decision-making models by regarding the total preference graph (seen at the bottom of Figure 4) as an object for manipulation. When a user pumps up one of the bars of the graph, the bar extends (the others shrink), and the treemap changes its partitioning to meet this condition. Different algorithms are possible for redrawing the treemap; the procedure implemented in the prototype is illustrated in Figure 9.

The criterion C1 contains five child criteria and each has two alternatives “A" and “B". When alternative B's graph bar is pumped up, the algorithm searches among all children of the currently selected node (C1) to locate the child which has the largest area ratio for B. This child is then pumped in tandem with the pumping action on B's bar (either inflation or deflation). The effect is the same as if the pump had been used on the child directly. This functionality is helpful for locating the criteria containing the highest ratio for an alternative especially when they contain descendant criteria.

Both the hook and pump tools provide the benefits of direct manipulation (Shneiderman 1992). Effects of these tools can be seen instantaneously at the screen location where the tool is operating. Users can store up to ten sets of relative weights and recall them at any point during the interaction.

## Prototype Examples

## Dam Construction

Sensitivity analysis can be executed visually and intuitively with a treemap. At a glance users can ascertain which element influences the result because every element's importance is shown as the area of a rectangle. It is clear that the change occurring in the larger area is more influential to the final result. Figure 10 shows a treemap for a decision-making problem that has a goal as “whether to construct the dam" (taken from the examples of“Expert Choice"). In this case, the decision-making model has a four-level decision tree with two alternatives of “build" and “not build." As the result of the rating procedure, the importance of “not build" exceeds that of“build" by about 0.03 points.

![](/api/attachments/5RKBJCSW/fulltext/images/3cc8dfafcffd51064ee7b3f2b046cac42a580044d673cc0157045f4b59611449.jpg)  
FIGURE 8. Data Manipulation with the Pump Tool.

![](/api/attachments/5RKBJCSW/fulltext/images/5ab8186157fb799f727ce8d6467f2be58ec7e716a30e435c0c6be1a7fbedd3dc.jpg)  
FIGURE 9. Graph Manipulation with the Pump Tool. C1 is the Currently Selected Node.

The criterion “effects of dam failure" is seen to influence the outcome of “not build" greatly given the large area of the “not build" alternative—this is an outlier. The dam failure criterion propagates up the decision tree through “Safety"—indicating a cause-effect relationship. The outcome favoring “not build" is not strong because the counter-effects of“power consideration" support a “build" decision, a fact easily seen with the treemap.

The “pump" tool allows users to manipulate the size of a criterion (rectangle) and examine the change of the total preference points on the outcome. This functionality aids in sensitivity analysis as the sibling criteria maintain their relative size relation. In the case of an example shown in Figure 10, a decision maker would find that the result reverses when the criterion “power consideration" increases by 0.06 points; the "build" bar becomes longer. If the decision maker is the person who would like to promote the dam construction, this information is of potential use in designing proposals.

Alternatively, if a decision maker pumped up the "build" bar while the goal is selected as a current node, the result would be that the criterion “employment factor" is pumped up. This criterion is thus seen to have the highest “build" alternative ratio and indicates dam construction would be positive from a jobs point of view.

## Site Selection

The hook tool is also useful for sensitivity analysis. It is sometimes difficult to judge which criterion would produce a more dramatic change in the result, especially when rectangular aspect-ratios are dissimilar. Figure 11 shows such an example; it is difficult to say which criterion—C1 or C2—has more impact on alternative A's preference point total. In this case, actual manipulation of each criterion's area with the hook is helpful. If A's preference increases as C1 increases and C2 decreases when manipulating their joint boundary, then the answer for the question is C1. If A does not change, C1 and C2 are assumed to be equally effective. The ordering of the criteria can be changed in the case where two criteria do not share a joint boundary. Direct manipulation actions (such as dragging and dropping) to swap regions would be a solution; this and many other features could be added in a commercial version.

![](/api/attachments/5RKBJCSW/fulltext/images/fb283249a1435778f9fda204eb0e505e757eaa11f330740ab84b5f49635d8d16.jpg)  
FIGURE 10. A Treemap for Dam Construction.

Figure 12 displays two treemaps for the selection of the site for a newly planned branch factory (Tone 1990). Four alternatives (sites A, B, C, D) are evaluated with a three-level decision tree. The graph in Figure 10a shows “site A" having the highest point total (0.27) followed by “B," "D" and “C." “Social factor" and "economical factor" are given much more importance than “technical factor" among the firstlevel criteria.

Suppose a decision maker wishes to examine the sites in the context of these two predominant factors. When their joint boundary line is moved to the left with the hook (thereby increasing the importance of “economical factor" at the expense of “social factor"), the preference points of “site A" and “site B" increase and those of “site D" decrease. “Site C" does not change its point total. When the joint boundary is hooked to the right, an opposite tendency is observed. From these observations, the decision maker can extract the fact that “site A"and “site B"are influenced advantageously with “economical factor" and “Site D" has an advantage with “social factor". “Site C" is neutral for these criteria.

![](/api/attachments/5RKBJCSW/fulltext/images/e2f48585f15835643a382b3e665f045ba1b6908b0e562c36ba69296d564dba94.jpg)  
FiGURE 11. An Example of Treemap Manipulation for Examining the Influence of Two Criterial on the Final Decision.

## Patent Application

A patent management section of a company has established the decision tree shown in Figure 13 for applying for a patent (the data is taken from an “Expert Choice" example). When a patent document is submitted to this section from one of the product development sections, it is tested through the AHP procedure and judged as viable or nonviable.

The importance of the subcriteria of “Probability of Success" is sometimes changed in accordance with revised organization policy. The hook tool allows for this change as the user can adjust the ratios of all subcriteria by manipulating their five joint boundaries. Note that the ruler pops up vertically adjacent to all six subcriteria allowing for finer adjustments in ratio.

## Usability Study

## Description

In addition to comments from many visitors, a usability study was conducted to evaluate the effectiveness of the prototype via more structured subjective preference data. Six student volunteers, all business or management majors, participated in the study. All of them were familiar with AHP as well as skilled in operating a computer with a mouse input device. For the subjective evaluation, a modified Questionnaire for User Interface Satisfaction (QUIS) with 9 point scale rating was employed after task completion (Chin et al. 1988). Five questions were selected from the original QUIS along with seven additional questions specifically related to the prototype.

Using Treemaps to Visualize the AHP  
![](/api/attachments/5RKBJCSW/fulltext/images/d0fa79b7785771981ee1dba020b80ac115b77a48bc6551518e4c1101430fa373.jpg)  
FIGURE 12a. Site Selection, the Original Decision-making Model.

The subjects were asked to give their subjective impression by filling out the questionnaire immediately after executing tasks from the below list (two tasks involve data searching; the remaining three involve data operation):

1. List out three criterion where X has fewer relative importance points than B.

2. Check the most influential criterion in the final result among those listed above.

3. How much should we change the relative importance point of the criterion found in task 2 to reverse the result?

4. Suppose we can eliminate “price" as a criterion. What would the result be in such a case?

5. If importance of “service," “specification," “price" and “usability" are in the ratio of 1:1:1:2 (i.e., relative importance points are 0.2, 0.2, 0.2, 0.4 respectively), how will the result change?

Even though tasks 3 and 4 were designed for testing the pump tool and task 5 was for the hook tool, any suggestion to do so was not given to the subjects; they were encouraged to find the correct method themselves. The same decision making model shown in Figure 2 with two alternatives (“Soft X" and “Soft B") was used in the study. Before attempting the tasks, subjects were given an explanation of the prototype and asked to perform three sample tasks: reading relative importances from a treemap, and manipulating them by the hook and pump tools.

![](/api/attachments/5RKBJCSW/fulltext/images/5104ca008adb39d8760f52a1673620e59195e5721bee84f95a2b4a13b7220b09.jpg)  
FIGURE 12b. Site Selection, the Result of the Hook Operation

## Results

Since all subjects gave more than five points (the midpoint) on every item, the prototype created a positive impression in these subjects for the given data and tasks (Figure 14). Moreover, the means exceed 7 in the 10 of 12 items. These facts suggest the treemap method has potential as an effective tool for AHP data visualization and operations. A few subjects reported that the numerical data display with all nodes would help data search and operation processes (relative/absolute ratios are displayed when the node is selected).

Although there was no suggestion to do so, five of six subjects made use of both the pump and hook tools properly for completing tasks 3–5 (one subject used only the hook tool for completing all tasks). All subjects who used the pump tool gave 8 or 9 points for its usability. The hook tool also received over 7 average points. These facts indicate that the functions and representations of both tools are acceptable. Further experimental study would be useful with larger sets of data and with more involved AHP tasks.

![](/api/attachments/5RKBJCSW/fulltext/images/2835f43d8bd4d856024185146f93b17d700d48fc2be5eee7003bed13c7ba6e00.jpg)  
FIGURE 13. Patent Application with Vertical Pop-up Ruler to the Right of “Probability of Success" Children.

## Future Research

The transformation of the treemap and the outcome bar graph of alternatives is rapid and incremental. However, "undo" commands and history logging allowing users to reverse their most recent operations could be added in a commercial version. Such functions are important in a system that provides full “what if" analysis.

When the prototype was developed, hierarchical structures and rating results were assumed to have been provided in advance through existing packages such as Expert Choice. The user interface could be expanded to allow users to slice and dice the base rectangle in order to input a hierarchical structure directly. A facility to rearrange positions for criteria would be useful

Rating involves more difficult issues. The AHP applies a pairwise comparison method with a scale for giving relative importances to criteria and alternatives. A visual process could be developed to accomplish this.

Additional usability studies with professional subjects carrying out a wider variety of tasks drawn from their own projects would provide further insights. Integration of the treemap visualization into existing decision-making tools would be another important step towards widespread dissemination.

![](/api/attachments/5RKBJCSW/fulltext/images/49425836ad9970a7e6d5b790b3fb9e34817331a6f2d249028a23e0e08076d139.jpg)  
FiGURE 14. Subjective Preference Results. Each Circle Represents an Actual Rating; Each Triangle Represents the Mean Rating

## Conclusion

Techniques for expanding treemaps into decision-support tools have been proposed. A prototype for the AHP method incorporating direct manipulation tools has been implemented on a personal computer, and its usability has been tested.

Information visualization is a dynamic field. In many cases, a good deal of computing horsepower is required for the effective display of information in simulations, detailed 3-D representations or animations. Treemaps and their manipulation methods can be realized with simple algorithms. Even though the prototype was implemented on a personal computer with a standard graphics library (Borland's C library), it runs fast enough for practical use—thus opening the door to visualization support for the average user.

A detailed video description is available: T. Asahi, B. Shneiderman, and D. Turo, Visual Decision-Making: Using Treemaps for the Analytic Hierarchy Process, ACM

SIGGRAPH Video Review (April 1995). Also appeared in the Univ. of Maryland Human-Computer Interaction Laboratory Video Reports 1994 (ordering information at http://www.cs.umd.edu/projects/hcil).\*

Acknowledgments. We want to thank Professor Saul Gass of College of Business and Management at University of Maryland for giving us useful information about the AHP including the “Expert Choice" software package, Professor Ernest Forman and students of School of Business and Public Management at the George Washington University for their cooperation in the usability study, the members of the Human-Computer Interaction Lab at the University of Maryland, College Park for their comments, and Mrs. Maysa Assis for proofreading this article.

\* Jonathan Grudin, Associate Editor. This paper was received on October 30, 1994, and has been with the authors 1 month for 1 revision.

## References

Chin, J. P., V. A. Diehl, and K. Norman, "Development of an Instrument Measuring User Satisfaction of the Human-computer Interface." Proceedings ofCHI '88 Human Factors in Computing Systems, ACM Press, 1988, 213–218.

Finnie, G. R., G. E. Wittig, and D. I. Petkov, “Prioritizing Software Development Productivity Factors Using the Analytic Hierarchy Process," The Journal of Systems and Software, 22 (1983), 129–137.

Forman, E. H., Expert Choice Software Version 7.0 and Manual, Decision Support Software Company, Pittsburgh, PA, 1989.

Jungmeister, W, and D. Turo, “Adapting Treemaps to Stock Portfolio Visualization," Technical Report Dept. of Computer Science, University of Maryland, CAR-TR-648, CS-TR-2996, SRC-TR-92-120, 1992.

Saaty, T. L., The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

, Decision-making for Leaders, Wadsworth, Belmont, CA, 1982.

, and L. Vargas, The Logic of Priorities, RWS Publications, Pittsburgh, PA, 1991.

Shneiderman, B., Designing the User Interface, Strategies for Effective Human-computer Interaction, 2nd Edition. Addison-Wesley, Reading, MA, 1992.

-. “Tree Visualization with Tree-maps: A 2-D Space-filling Approach,"ACM Transactions on Graphics 11, 1 (Jan. 1992), 92–99.

Tone. K, and S. Yanagisawa, “Site Selection for a Large Scale Integrated Circuit Factory," in The Analytic Hierarchy Process, B. L. Golden, E. A. Wasil, and P. T. Harker, Eds., Springer-Verlag, Berlin, 1989, 242-250.

—, A Game-like Decision-making Method (in Japanese), Nikkagiren, Tokyo, 1990.

Turo. D, and B. Johnson, “Improving the Visualization with Treemaps: Design Issues and Experimentation," Proceedings of Visualization '92, IEEE Computer Society Press, 1992, 124–131.

-, "Enhancing Treemap Displays via Distortion and Animation: Algorithms and Experimental Evaluation, "Unpublished Masters Thesis, Department of Computer Science, University of Maryland, 1993.

Zahedi, F., “The Analytic Hierarchy Process—A Survey of the Method and its Applications," Interfaces, 16(1986),96-108
