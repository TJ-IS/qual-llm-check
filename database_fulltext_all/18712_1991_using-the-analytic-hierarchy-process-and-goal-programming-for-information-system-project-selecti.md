---
otero_id: 18712
otero_key: "JHRBM9E8"
title: "Using the analytic hierarchy process and goal programming for information system project selection"
authors: "Marc J. Schniederjans; Rick L. Wilson"
year: "1991"
journal: "Information & Management"
doi: "10.1016/0378-7206(91)90032-w"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Techniques

# Using the analytic hierarchy process and goal programming for information system project selection

Marc J. Schniederjans and Rick L. Wilson
University of Nebraska-Lincoln, Lincoln, NE 68588-0491, USA

One of the basic information system (IS) management activities is the planning of IS projects. Specifically, such planning requires the selection of IS projects and allocation of resources to complete them. This paper presents an improved IS project selection methodology that combines the recently applied IS project selection methodologies of the analytic hierarchy process (AHP) within a goal programming (GP) model framework. This new combination of the AHP and GP methodologies helps to overcome the weaknesses observed when either methodology is used separately. The combined AHP and GP methodology is illustrated through an example.

Keywords: IS planning, IS project selection, Goal programming, Analytic hierarchy process.

## 1. Introduction

In a recent paper researchers proposed the use of the analytic hierarchy process (AHP) as a means of establishing a priority system for the systematic selection of information system (IS) projects $[4]$ . This study explained how AHP mathematically determines a priority structure and demonstrated how this is applied in the selection of IS projects. While the AHP provides an ideal ranking process for the selection of IS projects, it does not consider relevant constraints that exist in the decision environment. Indeed, the AHP ranking of IS projects does not always determine which ones will actually be completed. Factors (such as budgetary limitations, available management, and staff resources) are real world constraints that should and often do alter which IS projects are selected regardless of the sophistication of any ranking method.

Recent, IS project selection methodologies have been proposed that consider budgetary and resource constraints in the decision process. Muralidhar, Santhanam and Schniederjans [3] proposed

![](/api/attachments/JHRBM9E8/fulltext/images/b594c09601e739e7939387b3cbffe9d1f1a0fc54c52b261405eb8ce2a5c43719.jpg)  
Mark J. Schniederjans is currently a professor of management in the College of Business Administration at the University of Nebraska-Lincoln. He is the author of several books including Case Studies in Decision Support Systems, and numerous articles. Dr. Schniederjans serves on the editorial advisory boards of Computers & Operations Research and Production and Operations Management. His research and consulting interests include the introduction of computer based tech-

nology in production and operations facilities and the development of mathematical programming based decision support systems.

![](/api/attachments/JHRBM9E8/fulltext/images/89b6f12a564b2c7f944550a25682a0472b37d75b3b79d8e167117ad74d91f9fb.jpg)  
Rick L. Wilson is an assistant professor of management science and information systems at Oklahoma State University. He is currently finishing his Ph.D. in management information systems from the University of Nebraska-Lincoln. His work experience includes several positions with U.S. West. He has previously published papers in Information and Management, as well as presenting numerous papers at national and international meetings. His research in  
terests include decision support systems, neural networks and advanced technology management.

the use of a zero-one linear programming (ZOLP) model for IS project selection. In their model, they sought a single objective of minimizing budgetary costs that were constrained by resource limitations including management, analyst, and programmer hours. Extending this model, the same researchers developed a zero-one goal programming (ZOGP) model to consider the more realistic multiple and conflicting objectives that exist when limited resources constrain the decision problem of IS project selection [7]. In their ZOGP model, goal constraints were used to model “obligatory goals”, such as mandated projects and maximum resource limitations, that must be used to constrain the IS project selection process. They also demonstrated how other more flexible goals could be modeled as goal constraints, and considered in order of their ranked importance. While the ZOGP model’s multiple ranked objective represents an improvement over the ZOLP model, the means by which the ranks were determined was not defined in their paper. Considering the fact that the ranking of the goal constraints has a tremendous impact on determining the solution, great care must be given in their establishment.

The purpose of this paper is to demonstrate how the AHP can be used to establish a priority structure for use within a ZOGP model. Specifically, we will demonstrate how a combined AHP and ZOGP model can be used to aid in IS project selection by generating a solution that recognizes the real world resource limitations while considering AHP ranked goals.

## 2. Methodology

To understand the combined AHP and ZOGP model, we must determine how AHP can be used to generate the IS project priorities and then decide how ZOGP may use those priorities within its modeling structure.

## 2.1. AHP procedure and use in ranking IS projects

The Analytic Hierarchy Process, introduced by Saaty [5], addresses how to determine the relative importance of a set of activities in a multi-criteria decision problem. A comprehensive list of major applications of the AHP can be found in Zahedi [14] and Shim [12]. AHP makes it possible to incorporate judgments on intangible qualitative criteria alongside tangible quantitative criteria [6]. The process utilizes pairwise comparisons of the project alternatives as well as pairwise comparisons of the multiple criteria. The use of such comparisons to collect data from the decision maker offers significant advantages. It allows the decision maker to focus on the comparison of just two objects, making the observation as free as possible from extraneous influences. Additionally, pairwise comparisons generate meaningful information about the decision problem, improving consistency in the decision making process [2].

The attributes of the AHP satisfy the requirements of a good IS project prioritization methodology. It allows both tangible and intangible factors to be specified in a multi-criteria setting, provides the ability to express the relative importance of the multiple criteria being considered, uses pairwise comparisons in extracting information when determining the project prioritizations, and is easy to use and implement.

As with any methodology, the first step in using the AHP for prioritizing a set of IS projects is to identify the multiple criteria which merit consideration. The next step is to evaluate how well each project addresses each criterion by comparing the projects in pairs for all possible project combinations for a given criteria. The process is repeated for each criterion under evaluation in the project prioritization problem.

When comparing the alternatives for each criterion, the decision maker will respond to questions such as: “In comparing Project 1 and Project 2, on the basis of cost reduction, which project is preferred?” The responses are represented numerically, scaled on the basis of Saaty’s proposed 1–9 scale with reciprocals, in a project comparison matrix. Large numerical values in the comparison matrix indicate a greater degree of preference of one project over another in the given comparison. The comparison matrix will be reciprocal in nature (i.e., when a comparison is made, the exact ‘reciprocal’ response is then coded for the corresponding entry in the matrix where the order of the comparison is reversed), halving the required number of comparisons. Further details on the scale and properties of the matrix can be found in Saaty.

After all project comparisons are made for each criterion, their relative importance are elicited from the decision maker using the same pairwise comparison process. When comparing the importance of the individual criteria, the typical question asked of the decision maker would be: "In comparing the benefits obtained by cost reduction and the benefits obtained by increased productivity, which is more important to the organization?" As before, all possible pairwise comparisons are made and coded numerically in another comparison matrix. Once comparison matrices for both project and criteria comparisons are constructed, the final step is to determine the overall prioritization of the IS projects.

Establishing this prioritization involves three steps. The first is to determine the relative importance of the criteria using the criteria comparison matrix. The largest eigenvalue and the corresponding principle eigenvector of this matrix are calculated. The principle eigenvector is normalized such that its entries sum to one. The normalized eigenvector represents the relative importance of the criteria.

The second step is to determine the relative importance of the projects with respect to each criterion. The project comparison matrices are used to establish the relative importance of the projects. As in the previous step, the normalized principle eigenvector of the project comparison matrix for a given criterion represents the priority of the projects for that criterion. The process is repeated for every criterion, each resulting in a distinct prioritization of projects.

Finally, the relative importance of the projects for each criterion and the relative importance of the criteria themselves are used to determine the overall ranking of the projects. Assume that the relative importance of n projects are to be established using \_ criteria. Let $C_i$ (for $i = 1, 2, \ldots, \_)$ represent the relative importance of criteria i and let $D_{ij}$ (for $j = 1, 2, \ldots, n$ ) represent the relative importance of Project j with respect to criteria i. The overall relative importance of Project j ( $w_j$ ) is determined as:

$$
\mathrm{w} _ {\mathrm{j}} = \sum_ {\mathrm{i} = 1} ^ {-} \mathrm{C} _ {\mathrm{i}} \cdot \mathrm{D} _ {\mathrm{ij}}
$$

The larger the value of $w_{j}$ , the higher the relative importance of Project j. Thus, the composite values of $w_{j}$ represent the relative ranking of the projects under evaluation [13].

## 2.2. The ZOGP model for IS project selection

A ZOGP model is an ideal decision making methodology that can be used to make an optimal selection, consistent with AHP IS project rankings and resource constraints $[8]$ . Zero-one goal programming has been applied in a variety of ranked resource selection schemes, including the selection of corporate acquisition candidates $[9]$ , library journal acquisition candidates $[11]$ , and faculty course assignments $[10]$ . ZOGP permits the consideration of resource limitations (e.g., budgetary limitations or limited human resource hours of labor) and other selection limitations (e.g., mandated projects) that must be rigidly observed in the IS project selection decision. ZOGP also permits the ranked inclusion of IS projects so their selection is based, in part, on the AHP ranking system previously discussed. The ZOGP model for IS project selection can be stated as follows:

Min $Z = \mathrm{P_k(w_jd_i^+, w_jd_i^-)}$

$$
\begin{array}{r l} & \left(\text { for } k = 1, 2, \dots , K; i = 1, 2, \dots , m; \right. \\ & \quad \left. j = 1, 2, \dots , n\right) \end{array}\tag{1}
$$

subject to

$$
\begin{array}{r l} \mathrm {a_ {ij} x_ {j} - d_ {i} ^ {+} + d_ {i} ^ {-} = b_ {i}} \\ & (\text { for   i = 1,2,\ldots,m; j = 1,2,\ldots,n}) \end{array}\tag{2}
$$

$$
\begin{array}{r l} & \mathrm {x_ {j} + d_ {i} ^ {-} = 1 (for i = m+ 1, m+ 2,\dots,m + n;} \\ & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \mathrm{j=1,2,...,n)} \\ & \text { and } \mathrm {x_ {j} = 0 or 1 (for j = 1,2,...,n)}, \end{array}\tag{3}
$$

where m = the number of IS project goals to be considered in the model, n = the pool of IS projects from which the optimal set will be selected, $w_{j}$ = the AHP mathematical weight on the j = 1, 2, ..., n IS projects, $P_{k}$ = some K priority lexicographic rankings where $P_{1} > P_{2} \gg P_{K}$ , for i = 1, 2, ..., m IS project goals, $d_{i}^{+}$ , $d_{i}^{-}$ = the ith positive and negative deviation variables for i = 1, 2, ..., m IS project goals, $x_{j}$ = a zero-one variable, where j = 1, 2, ..., n possible projects to choose from and when $x_{j}$ = 1, then select the jth IS project or when $x_{j}$ = 0, then do not select the jth IS project, $a_{ij}$ = the jth IS project usage parameter of the ith resource, and $b_{i}$ = the ith available resource or limitation factors that must be considered in the selection decision.

In this model, eq. (1) is the objective function which seeks to minimize deviation from desired IS project goals consistent with the AHP ranking of the projects. The $w_{j}$ are attached to the deviational variable $d^{-}$ for the n number of IS projects represented by the goal constraints in eq. (3). The lexicographic nature of goal programming treats the AHP weights as a sub-ranking of the IS projects within their specific $P_{k}$ . The greater the $w_{j}$ , the more desirable the selection of project in the decision process. The goal (right-hand side value) for each of the constraints in eq. (3) will always be set at one, since a value of one for a particular $x_{j}$ variable indicates the selection of that project. All other goal constraints used to model obligatory goals and flexible goals are formulated using eq. (2). An “obligatory goal” constraint is one that does not permit any deviation from the targeted value; in other words, the deviational variable used to express this goal in the objective function must be equal to zero. A “flexible goal” constraint permits the possibility of either positive $d^{+}$ or negative $d^{-}$ deviation occurring from a stated $b_{i}$ . The positioning of the obligatory goals in the objective function priority scheme is at the highest priority level (i.e., $P_{1}$ ) in order to insure zero deviation. In most real world problems, obligatory goals, such as a resources’ maximum capacity, tend to establish boundaries but not an exact solution. It is usually when the ranking of the individual projects are considered that a specific set of projects will be determined by the model. This model solution behavior is one of the reasons why it is so important that a comprehensive method like AHP be used to establish the ranks for the individual project variable constraints. Because of the importance of these goals, we recommend that the set of goal constraints used to model the individual IS projects (i.e., eq. (2) constraints) be positioned at the next highest priority (i.e., $P_{2}$ ) after the obligatory goals. To rank the individual projects at the $P_{2}$ priority level, the AHP mathematical weight should be attached to the respective IS projects’ deviation variables in the objective function. The AHP weighting within the $P_{2}$ priority level has the effect of ranking the importance of the individual IS projects. The ZOGP model bases the selection of the IS projects $x_{j}$ on the AHP determined weights of $w_{j}$ for corresponding $d_{i}^{-}$ . The larger the $w_{j}$ , the more likely the corresponding IS project will be selected.

If other more flexible goals are to be considered, they may be ranked together or individually at subsequent priority levels. (For a review of basic GP model formulation procedures, see Schniederjans).

## 3. Toward application: A hypothetical example revisited

## 3.1. AHP development

To illustrate the use and advantages of the combined AHP and ZOGP model in IS project selection, the hypothetical example used by Muralidhar, Santhanam and Wilson will be revisited. Their problem consisted of prioritizing six IS projects on the basis of four criteria deemed to be important for a hypothetical organization. The criteria used were (1) Increased accuracy in clerical operations, (2) Information processing efficiency, (3) Promotion of organizational learning, and (4) Cost of implementation.

Pairwise comparison matrices were developed indicating the results when evaluating the relative importance of the criteria as well as matrices indicating the pairwise evaluation of how the projects address each criterion. By calculating the normalized eigenvector using the project comparison matrices for accuracy, efficiency, organizational learning and implementation costs, the relative importance of the projects for each criterion type can be determined. Calculating the normalized eigenvector of the criteria comparison matrix indicates the relative importance of the criteria. To obtain the overall composite relative importance of the six projects (the project prioritization), $w_{j}$ , the sum of the products of the relative importance of a specific criterion multiplied by the relative importance of a project considered under the specific criterion, is calculated for each project.

For the revisited example, the $w_{j}$ values calculated for the six IS projects were as follows: $x_{1}=0.226$ , $w_{2}=0.208$ , $w_{3}=0.044$ , $w_{4}=0.167$ , $w_{5}=0.183$ , and $w_{6}=0.171$ . Thus, the priority order of the projects could be established as Project 1, Project 2, Project 5, Project 6, Project 4, and Project 3, using their calculated composite relative importance values.

## 3.2. ZOGP model formulation

As previously stated, the AHP method of IS project selection establishes only a ranked order in which the projects should be completed and does not consider any resource constraints. Suppose that in this hypothetical example there exists several obligatory and flexible goals that must be considered in the selection from the available pool of the six IS projects. If there are four obligatory goals: (1) a total yearly maximum of 15,000 hours of programmer time is available to complete all of the IS projects selected, (2) a total yearly maximum of 6,500 hours of analyst time is available to complete all of the IS projects selected, (3) a total yearly maximum budget of \$200,000 is available to complete all of the IS projects selected, and (4) project 2 is a necessary maintenance activity and therefore is a mandated project that must be one of the set of IS projects selected. In addition to the goal of selecting the IS projects, there are two other flexible goals, stated in order of their importance: (1) an initial yearly allocation of budgeted dollars is set at \$180,000 but can vary up to but not beyond the total maximum value of \$200,000 and (2) an initial allocation goal of clerical hours of labor is set at 3,700 hours but deviation from this allocation is possible. In Table 1, the yearly cost and human resource usage information for each of the six projects is presented.

Based on this data and the previously computed AHP values, we can structure the goal constraints for this hypothetical example as presented in Table 2. As shown in the ZOGP model in Table 2, the first four goal constraints represent the “obligatory goals” defined in the problem. The appropriate deviation variables for these four goals constraints are placed at the $P_{1}$ priority level to insure the maximum resource levels are not exceeded and that the mandated project is selected. If, for any reason, deviations exist in these goals in a resulting solution, such a solution to the IS project selection problem would be infeasible or unworkable given the obligatory limitations. The next six goal constraints set at the $P_{2}$ priority level are designed to allow the projects to be selected in accordance to the AHP ranked order. As previously stated, the ZOGP model selects the IS projects on the basis of the AHP determined weights $w_{j}$ . The larger the weight, the more likely the corresponding IS project will be selected. At the $P_{3}$ priority, the goal of not over or under achieving a budget of 180,000 is modeled. Finally, at the $P_{4}$ level, the goal of not over or under utilizing 3,700 clerical hours is modeled.

The solution for this problem was generated using a University of Nebraska FORTRAN program based on a zero-one enumeration method for goal programming proposed by Bitran [1]. As shown in Table 3, the optimal selection for the example included IS projects $\mathbf{x}_2$ , $\mathbf{x}_4$ , $\mathbf{x}_5$ , and $\mathbf{x}_6$ . The other two projects where not chosen because of the limitations posed by resource limitations. For the priority analysis in Table 3 we can see that the obligatory goals were achieved (thereby a workable or feasible solution is guaranteed) and no more than the desired \$180,000 budget goal is needed to accomplish the IS projects selected. The goal deviation at $\mathbf{P}_2$ is expected since there will always be some deviation at this goal level unless all of the IS projects are selected.

## 3.3. Solution and interpretation

What makes the AHP and ZOGP model solution superior to using either method separately lies in the strengths and weaknesses of both methods. If only the AHP method is utilized to make the IS

Yearly cost and human resource usage information on IS projects  
Table 1

<table><tr><td rowspan="2">Item</td><td colspan="6">IS project yearly resource usage ( $a_{ij}$ )</td><td rowspan="2">Total yearly maximum available Resources ( $b_i$ )</td></tr><tr><td> $x_1$ </td><td> $x_2$ </td><td> $x_3$ </td><td> $x_4$ </td><td> $x_5$ </td><td> $x_6$ </td></tr><tr><td>Programmer hours</td><td>6,000</td><td>10,000</td><td>1,000</td><td>750</td><td>2,250</td><td>2,000</td><td>15,000 Hours</td></tr><tr><td>Analyst hours</td><td>1,300</td><td>1,250</td><td>1,800</td><td>2,000</td><td>1,500</td><td>1,750</td><td>6,500 Hours</td></tr><tr><td>Budgeted costs (000)</td><td>$80</td><td>$25</td><td>$55</td><td>$40</td><td>$65</td><td>$50</td><td>$200</td></tr><tr><td>Clerical labor hours</td><td>1,000</td><td>800</td><td>500</td><td>1,200</td><td>900</td><td>1,100</td><td>3,700 Hours *</td></tr></table>

\* The possibility of clerical overtime permits the usage of more than 3,700 hours if necessary.

Table 2
ZOGP model formulation

<table><tr><td colspan="8">ZOGP model formulation</td><td>Goals</td></tr><tr><td colspan="8">Minimize  $Z = P_1$  ( $d_1^+ + d_2^+ + d_3^+ + d^{-4}$ )</td><td>[Satisfy all obligatory goals]</td></tr><tr><td colspan="8"> $P_2$  ( $0.226d_5^- + 0.208d_6^- + 0.044d_7^- + 0.167d_8^- + 0.183d_9^- + 0.171d_{10}^-$ )</td><td>[Select highest AHP weighted IS projects]</td></tr><tr><td colspan="8"> $P_3$  ( $d_{11}^- + d_{11}^+$ )</td><td>[Use $180,000 for all IS projects selected]</td></tr><tr><td colspan="8"> $P_4$  ( $d^{-12} + d_{12}^+$ )</td><td>[Use 3,700 hours clerical help for all IS projects]</td></tr><tr><td colspan="8">subject to  $6,000 \times_1 + 10,000x_2 + 1,000x_3 + 750x_4 + 2,250x_5 + 2,000x_6 + d_1^- - d_1^- = 15,000$ </td><td>[Avoid over utilizing max. programmer hours]</td></tr><tr><td colspan="8"> $1,300x_2 + 1,250x_2 + 1,800x_3 + 2,000x_4 + 1,500x_5 + 1,750x_6 + d_2^- - d_2^+ = 6,500$ </td><td>[Avoid over utilizing max. analyst hours]</td></tr><tr><td colspan="8"> $80x_1 + 25x_2 + 55x_3 + 40x_4 + 65x_5 + 50x_6 + d_3^- - d_3^+ = 200$ </td><td>[Avoid over utilizing max. budgeted dollars]</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td> $x_2 + d_4^- = 1$ </td><td></td><td></td><td>[Select obligatory project 2]</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td> $x_1 + d_5^- = 1$ </td><td></td><td></td><td>[Select project 1]</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td> $x_2 + d_6^- = 1$ </td><td></td><td></td><td>[Select project 2]</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td> $x_3 + d_7^- = 1$ </td><td></td><td></td><td>[Select project 3]</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td> $x_4 + d_8^- = 1$ </td><td></td><td></td><td>[Select project 4]</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td> $x_5 + d_9^- = 1$ </td><td></td><td></td><td>[Select project 5]</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td> $x_6 + d_{10}^- = 1$ </td><td></td><td></td><td>[Select project 6]</td></tr><tr><td rowspan="3">and</td><td colspan="7"> $80x_2 + 25x_2 + 55x_3 + 40x_4 + 65x_5 + 50x_6 + d_{11}^- - d_{11}^+ = 180$ </td><td>[Avoid over or under utilizing expected budget]</td></tr><tr><td colspan="7"> $1,000x_1 + 800x_2 + 500x_3 + 1,200x_4 + 900x_5 + 1,100x_6 + d_{12}^- - d_{12}^+ = 3,700$ </td><td>[Avoid over or under utilizing clerical hours]</td></tr><tr><td colspan="7"> $x_j = 0 \text{ or } 1$ </td><td></td></tr></table>

Table 3  
ZOGP model solution for hypothetical example

<table><tr><td colspan="2">Decision variables</td><td>Interpretation</td></tr><tr><td colspan="2"> $x_{2} = x_{4} = x_{5} = x_{6} = 1$ </td><td>[Select projects 2, 4, 5, and 6]</td></tr><tr><td colspan="2"> $x_{1} = x_{3} = 0$ </td><td>[Do not select projects 1 and 3]</td></tr><tr><td colspan="2">Deviation variables</td><td></td></tr><tr><td colspan="2"> $d_{1}^{-} = d_{1}^{+} = 0$ </td><td>[We will use exactly 15,000 hours of programmer time]</td></tr><tr><td colspan="2"> $d_{2}^{-} = d_{2}^{+} = 0$ </td><td>[We will use exactly 6,500 hours of analyst time]</td></tr><tr><td colspan="2"> $d_{3}^{-} = 20, d_{3}^{+} = 0$ </td><td>[We will use $20,000 ($200,000–$180,000) less than the maximum budgeted dollars]</td></tr><tr><td colspan="2"> $d_{4}^{-} = 0$ </td><td>[We will select mandated project 2]</td></tr><tr><td colspan="2"> $d_{5}^{-} = 1$ </td><td>[We will not select project 1]</td></tr><tr><td colspan="2"> $d_{6}^{-} = 0$ </td><td>[We will select project 2]</td></tr><tr><td colspan="2"> $d_{7}^{-} = 1$ </td><td>[We will not select project 3]</td></tr><tr><td colspan="2"> $d_{8}^{-} = 0$ </td><td>[We will select project 4]</td></tr><tr><td colspan="2"> $d_{9}^{-} = 0$ </td><td>[We will select project 5]</td></tr><tr><td colspan="2"> $d_{10}^{-} = 0$ </td><td>[We will select project 6]</td></tr><tr><td colspan="2"> $d_{11}^{-} = d_{11}^{+} = 0$ </td><td>[We will use exactly the $180,000 budgeted amount]</td></tr><tr><td colspan="2"> $d_{12}^{-} = 0, d_{12}^{+} = 500$ </td><td>[We will use 500 (4,200–3,700) more hours of clerical help than the initial 3,700 hours]</td></tr><tr><td colspan="2">Priority analysis</td><td></td></tr><tr><td>Priority</td><td>Goal deviation</td><td></td></tr><tr><td> $P_{1}$ </td><td>0</td><td>[All obligatory goals achieved]</td></tr><tr><td> $P_{2}$ </td><td>0.27</td><td>[Two projects not selected]</td></tr><tr><td> $P_{3}$ </td><td>0</td><td>[No over or under achievement in the desired goal of using $180,000]</td></tr><tr><td> $P_{4}$ </td><td>500</td><td>[We will over utilize clerical labor by 500 hours]</td></tr></table>

project selection, the prescribed project rankings, as previously stated, generated an implementation order of projects 1, 2, 5, 6, 4, and 3. In Table 4 we present a comparison of using the AHP ranking order and the resulting combined AHP and ZOGP approach. As we can see in Table 4, regardless of the assumption used in applying the AHP method, the combined solution generated by using the

Table 4  
Original AHP solution and ZOGP solution comparison

<table><tr><td rowspan="2"></td><td rowspan="2">Resulting projects completed</td><td colspan="4">Resulting unused resources</td></tr><tr><td>Programmer hours</td><td>Analyst hours</td><td>Dollars</td><td>Clerical hours</td></tr><tr><td colspan="6">Original AHP solution</td></tr><tr><td>Assuming the projects would have to be completed in the ranked order given in the prior study but with the new resource limitations.</td><td>Only project 1, as programmer hours prevents project 2 from being completed</td><td>9,000</td><td>5,200</td><td>120,000</td><td>2,700</td></tr><tr><td colspan="6">Original AHP solution</td></tr><tr><td>Assuming the AHP ranking order is used but project order can be violated (i.e., projects can be stopped) in order to permit multiple projects to be completed.</td><td>Only projects 1, 5, and 6, as analyst hours prevents project 4 from being selected</td><td>4,750</td><td>1,950</td><td>9,000</td><td>700</td></tr><tr><td colspan="6">AHP and ZOGP model solution</td></tr><tr><td>Assumes we use the solution given by the model.</td><td>Projects 2, 4, 5, and 6</td><td>0</td><td>0</td><td>20,000</td><td>0</td></tr></table>

ZOGP model results in more projects being completed with less unused resources. While the issue of the AHP selecting a higher ranked project (i.e., project 1) can be raised, we feel the ZOGP model solution does a better job in selection by choosing more projects and making better use of available resources. Had we tried to use just a ZOGP model without the AHP weighting, only pure chance could generate the same solution that the combined AHP-ZOGP model derived. That is, no preferential ranking of the projects is possible without a weighting system which recognizes project “relative” importance as with the AHP. The simple ranking of priorities of the resource constraints presented in prior research does not begin to consider relative importance of the individual IS projects that the AHP weights incorporate into the ZOGP model. Indeed, the solution obtained when the AHP weighted constraints were left out of the model was entirely different (i.e., the solution resulted in selecting some of the lowest AHP ranked projects). It appears, then, the combined AHP and ZOGP model uses the preferential information provided by AHP and generates a feasible solution that best satisfies the IS project ranking by using the ZOGP methodology. The combined approach does not suffer the AHP shortcoming of ignoring resource constraints nor ZOGP’s weakness of ignoring the relative significance of IS project preferences.

## 4. Toward implementation: A case study

To examine some of the implementation issues related to the adoption of the proposed combined AHP and ZOGP modeling approach, data were collected for a case study at a regional utility company. Data were collected on IS project planning at the Lincoln Telephone and Telegraph (LT & T) Company of Lincoln, Nebraska. The purpose of the case study was to compare LT & T's current IS project ranking procedure with the proposed AHP-ZOGP method. Specifically this case study sought to observe possible benefits and limitations in implementing the AHP-ZOGP method when compared on a retrospective basis with prior IS project decision making.

Research on prior LT&T's IS project planning revealed they used a ranking/scoring method during the 1988–90 planning periods. From this period, a single year's data were incorporated into a AHP-ZOGP model. While the proprietary nature of the LT&L data prohibits its publication (by request of the utility company), its basic size and scope is similar in nature to the previous hypothetical example. Comparing the solutions generated and the effort necessary to obtain the solutions by both methods (i.e., their prior ranking method and the newly generated solution using the proposed AHP-ZOGP method) a number of comparative implementation observations were expressed by those members who took part in the study.

These observations can be grouped into implementation benefits and limitations in using the proposed AHP-ZOGP method. The reported benefits of using the AHP-ZOGP method included:

1. A more realistic solution: The AHP-ZOGP solution could have saved IS resources by recognizing necessary constrained resources that the ranking method did not.

2. Time savings: While determining AHP weights were time consuming, the time saved by avoiding political issues in the selection of projects more than compensated to help reduce the total time required to obtain a final selection.

3. A more thorough decision process: The completeness and non-political, non-bias nature of the pairwise comparisons in the AHP method was viewed as a more thorough means of weighting IS projects in the decision process than the ranking methods currently employed at LT&T.

4. Additional decision making information: Using a mathematical programming method like ZOGP allows for additional trade-off information (i.e., referred to as the “dual solution”) that permits decision makers to see dollar trade-offs between different projects, and the trade-offs in cost criteria used in the selection process. (While this type of additional analysis was not the focus of this paper, information on how it works in a ZOGP model is presented in Schniederjans and Fowler [9].)

The observed limitations of using the AHP-ZOGP method included:

1. Required AHP and ZOGP software: While the pairwise comparisons are manually performed, the computational effort to develop the AHP weighting necessitates some software to compute the normalized eigenvector. Likewise, the ZOGP software system is also a necessity is this approach is to be used. Without the software, this method is not practical to implement.

2. AHP limits application: As observed by Saaty [6], AHP chiefly limits the use of this AHP-ZOGP method to situations of 20 or less projects.

In defense of the observed limitations it should be mentioned AHP and ZOGP software is inexpensive and has been around for over ten years $[1,14]$ . While the software is of a special nature, its potential for improving decisions and saving constrained resources (such as in the LT&T study) could return software investment costs many times over in its first application. As to the 20 or less project limitation on the model, this may not really represent such a limitation. In the case of LT&T, less than ten IS projects were actually being examined. For IS department with more than 20 projects, they might consider dropping the AHP portion of the model and just use ZOGP to obtain a solution. Also, cutting any “obligatory” projects (and their resources) from the analysis that would be selected anyway might be another way of making the model fit the situation. IS departments might also overcome this limitation by performing their planning efforts more frequently, but with a smaller number of projects.

While this retrospect case study is a historic in nature, the observations do seem to support the contention that the combined AHP-ZOGP method can do a better job of selectioning IS projects than when using a single selection method, like ranking. While the AHP-ZOGP method was observed to have some limitations, these may not be applicable or can be overcome by many organizations.

## 5. Summary and conclusion

One of the basic management activities in IS planning deals with the selection of IS projects and the allocation of resources to complete these projects. This paper has presented an improved methodology to address such an IS management planning scenario. The approach offered here combines the recently applied analytic hierarchy process (AHP) within the framework of a zero-one goal programming model (ZOGP). The AHP is first used to prioritize the set of IS projects under consideration on the basis of the pertinent criteria of the organization. The resulting prioritization information is then used as a ranking scheme within the framework of a ZOGP model. The ZOGP model explicitly considers not only the relative importance of the IS projects but also considers important resource availability constraints faced by the organization when determining the proper selection of the projects which should be implemented.

The combined AHP-ZOGP method offers a systematic, easy-to-use approach to the IS project selection decision problem. It extends previous research in the area by incorporating a comprehensive prioritization system within an optimizing resource allocation process. Because of the synergy in the combined AHP-ZOGP approach, the new methodology is an excellent alternative to previous methodologies dealing with IS project selection.

## References

[1] Bitran, G., “Linear Multiple Objective Programs with Zero-one Variables”, Math. Programming, Vol. 23, No. 10, (1977), 121–139.

[2] David, H.A., The Method of Paired Comparisons, New York: Hafner Publishing, 1963.

[3] Muralidhar, K., Santhanam, R. and Schniederjans, M.J., "An Optimization Model for Information System Project Selection", Management Science and Policy Analysis, Vol. 6, No. 1, (1988), 53–62.

[4] Muralidhar, K., Santhanam, R. and Wilson, R.L., “Using the Analytic Hierarchy for Information System Project Selection”, Information and Management, January 1990, 1–9.

[5] Saaty, T.L., “A Scaling Method for Priorities in Hierarchical Structures”, Journal of Mathematical Psychology, Vol. 15, (1977), 234–281.

[6] Saaty, T.L., The Analytic Hierarchy Process, New York: McGraw-Hill, 1980.

[7] Santhanam, R., Muralidhar, K. and Schniederjans, M.J., "A Zero-One Goal Programming Approach for Information System Project Selection", OMEGA, Vol. 17, No. 6, (1989), 583–594.

[8] Schniederjans, M.J., Linear Goal Programming, Princeton, NJ: Petrocelli Books, Inc., 1984.

[9] Schniederjans, M.J. and Fowler, K., “Strategic Acquisition Analysis: A Multi-Objective Approach”, Journal of

the Operational Research Society, Vol. 40, No. 4, (1989), 333–345.

[10] Schniederjans, M.J. and Kim, G.Y., “A Goal Programming Model to Optimize Departmental Preferences in Course Assignment”, Computers and Operations Research, Vol. 14, No. 2, (1987), 87–96.

[11] Schniederjans, M.J. and Santhanam, R., “A Zero-One Goal Programming Approach for Journal Selection and Cancellation”, Computers and Operations Research, Vol. 16, No. 6, (1989), 557–566.

[12] Shim, J.P., “Bibliographical Research on Analytic Hierarchy Process (AHP)” ORSA/TIMS Joint National Meeting, Denver, CO, October 24, 1988.

[13] Wind, Y. and Saaty, T.L., “Marketing Applications of the Analytic Hierarchy Process”, Management Science, Vol. 26, No. 7 (1980), 641–658.

[14] Zahedi, F., “The Analytic Hierarchy Process – A Survey of the Method and Its Applications”, Interfaces, Vol. 16, No. 4, (1986), 96–108.
