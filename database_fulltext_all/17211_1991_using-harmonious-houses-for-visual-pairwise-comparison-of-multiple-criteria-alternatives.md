---
otero_id: 17211
otero_key: "WTU6VNRA"
title: "Using harmonious houses for visual pairwise comparison of multiple criteria alternatives"
authors: "Pekka Korhonen"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90076-n"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using harmonious houses for visual pairwise comparison of multiple criteria alternatives

Pekka Korhonen \*

Helsinki School of Economics and Business Administration, 00100
Helsinki, Finland

In this paper, we consider the problem of evaluating decision alternatives, which are described by means of several criteria. Our aim is to develop an approach which enables a decision-maker to present value information on the basis of a visual representation. The underlying ideas used in the approach are based on the use of symmetry and harmony. These principles are operationalized by using “harmonious houses”. The theoretical approach is implemented as a decision support system, which makes pairwise comparisons possible between alternatives. To perform sensitivity analysis is also possible. In our pilot tests, the idea has proven very promising.

Keywords: Computer graphics, Multiple criteria, Multivariate analysis, Visualization, Interactive.

![](/api/attachments/WTU6VNRA/fulltext/images/23466ef80dd6004ed3c1fd2a2f61914574830fb41777aab7a3035e92a4b3fc78.jpg)

Pekka J. Korhonen is Professor of Statistics at the Helsinki School of Economics, Finland. He received a B.S. and M.S. in Mathematics and Ph.D. in Applied Mathematics, all from the University of Helsinki. His research interests are multiple criteria decision making, interactive computer graphics, computational statistics, the applications of such models to management problem solving. His articles have appeared in The Journal of the Operational Research Society, Management

Science, Computational Statistics & Data Analysis, Quarterly Publication of the International Research Institute of Management Sciences (MNIIPU), European Journal of Operational Research, Naval Research Logistics Quarterly, Fuzzy Sets and Systems, Interfaces, Operations Research, VNIISI Publications, Belgian Journal of Operations Research, Statistics and Computer Science, Mathematical Modelling.

## 1. Introduction

In this paper, we consider discrete multiple criteria problems, in which decision alternatives are evaluated using a large set of criteria. Since each alternative is presented as a vector having several elements, the amount of information required for comparisons is often quite large, which makes it very difficult for the decision maker (DM) to absorb it. Therefore, there is a need for a method, which helps the DM to compare such long vectors.

To evaluate decision alternatives, the DM needs both holistic and detailed information. A visual representation is a convenient and useful way to provide the DM with a holistic perception and to improve the quality of the user interface. Numerical information is a traditional way to represent detailed information.

In descriptive statistics, computer graphics is widely used to illustrate numerical information by producing standard visual representations (bar charts, line graphs, pie charts, etc.) or using some more advanced techniques, for example, Andrews' curves (Andrews, 1972) and Chernoff's faces (Chernoff, 1973). Especially, Andrews' curves and Chernoff's faces were developed to illustrate multivariate data; a problem closely related to ours. These techniques are suitable to problems, in which the alternatives are examined in a bid to identify clusters, outliers, etc. However, they do not provide the DM with enough information (value information) for articulating preferences, because it is difficult to find clear rules, for example, for associating "good values" with "beautiful faces".

Our aim is to develop an approach, which transforms a vector into a picture in the spirit of Chernoff's faces and Andrew's curves, but which also enables a DM to present value information on the basis of a visual representation. The underlying ideas are based on the use of two concepts: harmony and symmetry. For the type of the picture, we have chosen a simple “harmonious house”. The ideal (standard/normal) house is described in a harmonious (and symmetric) form. Deviations from this ideal are felt abnormal. The “degree” to which a house resembles the ideal one serves as the basis for evaluation.

The theoretical ideas are implemented in a decision support system called VICO (A VIsual Multiple Criteria CComparison), which makes pairwise comparisons between alternatives possible. A possibility to perform sensitivity analyses is also available. This feature is implemented in the spirit of visual interaction. By “visual interaction” we mean that the DM communicates with the system by using visual representation in an interactive way. He/she can pick up details in a picture for a closer examination, modify a picture, etc. For example, in the MCDM-procedures developed by Korhonen (1984, 1986), Korhonen and Laakso (1986), Korhonen and Wallenius (1988) visual interaction plays a central role.

This paper consists of four sections. In the next section we review the use of standard methods and discuss some advanced methods which may be useful to illustrate solutions in MCDM-procedures. In section 3 we describe our approach, its implementation, and preliminary experiences. Concluding remarks are presented in section 4.

## 2. Visualizing Numerical Data

Graphical techniques have been considered extremely useful by statisticians in analyzing data. They have developed a number of graphical methods. Standard graphical techniques, such as bar charts, value paths, line graphs, etc., have a common feature: There is a one-to-one correspondence between a graphical representation and numerical data. The graphical representation can be transformed back into numerical form (with a certain accuracy) and conversely.

Especially, the techniques used with multivariate data are of special interest for the researchers working on multiple criteria decision making (MCDM) problems, because of many similarities between these two problems. These techniques may also be used in MCDM-problems to provide the DM with holistic information and to obtain a quick overall view of the relevant information, and then proceed with a detailed examination, if necessary.

Many authors have proposed the use of standard graphical techniques (bar charts, value paths, line graphs, etc.) to illustrate alternative choices (see, e.g., Cohon 1978, Geoffrion et al. 1972, Grauer 1983, Grauer et al. 1984, Kok and Lootsma 1985, Korhonen and Laakso 1986, Schilling et al. 1983, Silverman et al. 1985 and Steuer 1986). In most situations, the amount of information to be presented to the DM for evaluation may be considerable. A visual representation improves the readability of such information.

Graphical techniques have also been implemented as part of some computer systems developed for solving MCDM-problems. Well known systems DIDASS (Dynamic Interactive Decision Analysis and Support Systems), Expert Choice, and PREFCALC are good examples. DIDASS has been developed by the System and Decision Sciences (SDS) research group at IIASA (Grauer, Lewandowski and Wierzbicki 1984). Expert Choice has been developed to implement the AHP (the Analytic Hierarchy Process) (see, e.g. Saaty 1980). PREFCALC has been developed by Jacquet-Lagreze (see, e.g. Jacquet-Lagreze and Siskos 1982) for assessing a set of additive utility functions. In addition, we would like to mention our system VIG (Korhonen 1987), in which a free search on the efficient frontier is implemented by using a dynamic graphical interface – called PARETO RACE (Korhonen and Wallenius 1988).

A visual representation is limited to two dimensions. Therefore, the main problem in visualizing multivariate data is to construct a two-dimensional representation, when the number of variables exceeds two. In statistics, two general principles are applied for this problem:

\- reduce the dimensionality of a problem or
- plot a multivariate observation as an object (an icon).

Principal component analysis and multidimensional scaling (MDS) are two well-known techniques for obtaining a low-dimensional (specially two-dimensional) representation of multivariate data, so that the data may be examined visually (see, e.g., Everitt 1978).

In addition to standard techniques, these techniques are also interesting from the point of view of MCDM-problems. However, to our knowledge the principal component analysis has not been used for graphical purposes - with an exception of the paper by Mareschal and Brans (1988), in which they showed how to describe criteria and alternatives in the same picture. Korhonen, Wallenius and Zionts (1980) used MDS to reduce a four criteria problem into two dimensions and then described their search procedure in terms of a planar graph.

In the early 1970's two promising techniques (Andrews 1972 and Chernoff 1973) were developed for visualizing multivariate data by using original variables. Andrews plotted the curve

$$
\begin{array}{r l} \mathrm {f_ {i} (t) = x_ {i1} / \sqrt {2} + x_ {i2} \sin t+ x_ {i3} \cos t+ x_ {i4} \sin 2t} \\ & + \dots \end{array}
$$

for each data point $x_{i} = [x_{i1}, x_{i2}, \ldots, x_{ip}]$ over the interval $-\pi \leq t \leq \pi$ . Thus, each observation will be a harmonic curve drawn in two dimensions. In this method the number of variables is unlimited. The harmonic curves depend on the order in which the variables are written down.

Chernoff used a human face to represent each observation graphically. The construction of Chernoff's faces consists of geometrically well-defined elements, such as arcs of circles, arcs of ellipses, and straight lines. The values of variables are used as the parameters of these elements. Chernoff's original proposal consisted of 18 face parameters (fig. 1).

The harmonic curves of Andrews and Chernoff's faces help the user to view similarities and dissimilarities between observations, to identify clusters, outliers etc., but they are not very suitable to describing “value-information”. For example, in Chernoff's face, it is easy to understand that a “smile” means something positive, but the length of a nose does not convey similar information. In addition, we have no knowledge about the joint-effects of the face parameters. Big eyes and a long nose may make the face look silly in some user's mind, although big eyes may usually be a positive feature.

![](/api/attachments/WTU6VNRA/fulltext/images/293e10fa5eac4d4225f3f5265e7479e937ac4b46ec96db7ff51e3f4170838268.jpg)  
Fig. 1. An example of Chernoff's face.

In spite of the preceding disadvantages, the techniques provide us with new directions developing visual techniques. Especially, there is a need for methods, which can convey value information, too. Flury and Riedwyl (1981) proposed the use of asymmetrical faces in the context of Chernoff's method for increasing the number of parameters. This technique includes one useful idea to convey value information. For instance, the face parameters of the right side may be determined by an ideal point solution and those of the left side may be determined by the values of the current solution. The idea is based on the thought that a very asymmetric face is “ugly”.

## 3. Harmonious Houses

## The Principle

When standard graphical techniques (e.g. bar charts, value paths, line graphs) are used to visualize alternative solutions, value information is included in the details. Long bars, lines with a positive slope, etc. stand for good values or improvements. However, to have a holistic perception of these pieces of value information, when there are a lot of details, is often impossible. On the other hand, advanced techniques, such as Chernoff's faces and Andrews' harmonic curves help the DM to obtain a holistic perception of the alternatives, but not of their value. Therefore, our aim is to develop a method similar to Chernoff's and Andrews' methods, but which is based on the idea making it possible to convey value information.

The first requirement for the icon we are looking for is that it is possible to be parametrized in such a way that by improving the value of a criterion the icon becomes “better” or more “positive” in some sense. To convey this positive-negative information we can apply the concepts of harmony and symmetry. We can use icons, with which the DM feels that the alternative gets “worse”, when the icon becomes more disharmonious and asymmetric. Of course, this idea is heavily dependent on the icon chosen. Therefore, it is important to choose an icon, which we are used to seeing in a very harmonious and symmetric form. For this reason, we propose the use of a house as such an icon.

It is possible to use “complex houses”, if needed, but we start with a very simple one (see fig. 2)

The structure of the house is controlled by varying the positions of the corner points. Fig. 2 illustrates a standard (basic) house, in which each corner point is in its default position and allowable moves of corner points are shown as squares. A criterion can now be associated with the x- or y-coordinate of any corner point in such a way that the ideal value of the criterion corresponds to the default value of the coordinate and the deviation from the ideal value is shown as a move in an x- or y-direction. The x- and y-coordinates of corner points are called house parameters. The idea becomes clear in the enlarged square of a corner point in fig. 3:

Let $V = [v_{L}, v_{I}] \cup [v_{I}, v_{U}]$ be the range of a criterion, in which $v_{L}$ is the lower bound, $v_{I}$ is the ideal value, and $v_{U}$ is the upper bound of the criterion. In many problems either $[v_{L}, v_{I}] = \phi$ or $[v_{I}, v_{U}] = \phi$ , because the criterion is either to be maximized or minimized. Then the values of the criterion can be transformed into the house parameters using a simple affine transformation f:

$$
\begin{array}{r l} & {\mathrm {f\colon [ v_ {L} , v_ {I} ]\to [ x_ {L} , x_ {I} ]}} \\ & {\mathrm {f\colon [ v_ {I} , v_ {U} ]\to [ x_ {I} , x_ {U} ]}} \\ & {\mathrm {f\colon [ v_ {L} , v_ {I} ]\to [ y_ {L} , y_ {I} ]}} \\ & {\mathrm {f\colon [ v_ {I} , v_ {U} ]\to [ y_ {I} , y_ {U} ]}.} \end{array}
$$

For instance, when $v \in [v_{L}, v_{I}]$ , function f is given as

$$
\mathrm{x} = \mathrm{x} _ {\mathrm{L}} + \frac {\mathrm{x} _ {\mathrm{I}} - \mathrm{x} _ {\mathrm{L}}}{\mathrm{v} _ {\mathrm{I}} - \mathrm{v} _ {\mathrm{L}}} (\mathrm{v} - \mathrm{v} _ {\mathrm{L}}).\tag{1}
$$

Note that formula (1) can also be applied, even though v lies outside the range, if desired.

![](/api/attachments/WTU6VNRA/fulltext/images/f862e8603b149875912c820330d0159939ef50277cc0734752cb3cf3cc4b063b.jpg)  
Fig. 2. An ideal harmonious house with the range of parameters.

![](/api/attachments/WTU6VNRA/fulltext/images/f58d8d9e081d40a9734f74c4afccf5118a0428eb80ada7aeb655b3f28d4efa4a.jpg)  
Fig. 3. Illustrating the moves of a corner point from its default position.

## Implementation

A preliminary version of an interactive microcomputer system by name VICO (A VIsual Multiple Criteria CComparison) is developed in the spirit of Decision Support Systems to implement the idea presented above. VICO is written in TURBO PASCAL and implemented on an IBM PC/1 microcomputer. The program consists of more than 3000 lines of code. Most of it is used to build up an attractive user/computer interface. The interface is based on one main menu, spreadsheets, and computer graphics. The key word is visual interaction. “Visual interaction” means that one communicates with the system using visual representation in an interactive manner. On the screen the user will see two houses simultaneously. With these houses he/she can make sensitivity analysis and thus to transform houses, when desired.

The VICO program has four main functions:

## Data Management Function

which allows a user to create new data, retrieve existing data, and save modified and restructured data.

## Data Operations Function

which allows a user to provide the attributes (columns) and the alternatives (rows) with names, to create new alternatives and attributes, to fill in or edit the attribute-alternative matrix, and to specify acceptable ranges for the attributes.

## House Building Function

which allows a user to select the criteria, to associate the criteria with house parameters, to draw the houses (two at a time), and to make sensitivity analysis in a visual form.

## Solution Output Function

which allows a user to examine solutions on the screen, and store intermediate results for later consideration and/or for report writing.

Each main function consists of one or more sub-functions, which are all chosen from the main menu (fig. 4). Using only one main menu makes it easy to keep the control of the program in the user's hands. Note that all functions are not available all the time. At each stage, available choices are colored light cyan, unavailable magenta. The user is welcome to choose anyone of the available functions without "running through the entire list" of choices. When a function is terminated by pressing the F10-key (Exit-key), the main menu is shown again. By moving the cursor up and down in the menu, we can find all available choices. When the menu is shown for the first time, only the first and last choices are available (the user can provide the model with a name or exit). Subsequently, other choices become available.

As a second example of the screens used in VICO we present the one obtained by choosing function “Specify House Parameters” from the main menu. The purpose of this screen is to provide the user with a convenient way to join the criteria into the house parameters. Any criterion may be associated with one or several house parameters. If no criterion stands for some house parameter, then the ideal position is used.

On the screen, the user will see two lists: the list of house parameters and the list of criteria. First he/she will move the cursor to point a house parameter to be defined, and then some certain criterion will be picked up and joined with the house parameter. The house parameters are shown also in a visual form in a window in a lower right corner. A thick line will indicate the house parameter under consideration (see fig. 5).

When all parameters are specified, the user can choose the function “Display Houses” from the main menu. Using function keys he/she can choose any two alternatives, simultaneously, and compare them as houses (see, fig. 6). The user can evaluate, which one is more harmonious and thus better. The system allows him/her to make sensitivity analysis with the values of the criteria. He/she can change the numerical value of a criterion and the system will draw the change into the picture. For example, this operation is made for one criterion of the alternative drawn as the rightmost house in fig. 6.

## Experimental tests

We have made some experimental tests with the preliminary version of VICO. For instance, in a simple pilot test we used as subjects a group of students (20) attending one of the basic courses for undergraduate students (Personal Computing)

![](/api/attachments/WTU6VNRA/fulltext/images/c5f326febe8d8bec0f76daa78add376925891d5476c37229cade3c0d95b6e7e4.jpg)  
Fig. 4. The main menu.

![](/api/attachments/WTU6VNRA/fulltext/images/59a8445202fc72c19a5394d5eaa95f12085a0e23b6363dbc2c11f951d9776d02.jpg)  
Fig. 5. House parameters.

at the Helsinki School of Economics. They had a little bit experience in using microcomputers, but no experience, e.g., in graphical presentation. The data consisted of 20 firms, and the purpose was to evaluate their performance. As performance indicators we used 11 criteria based on typical financial information. Identical information is given for two years (77 and 78). We a priori told the students the fact that three of these firms made a bankruptcy within the time period 79–80. Firm 19 (in fig. 6) is one of them. We asked the students to forecast which firms had gone into bankruptcy, based on the harmonious houses. The results are shown in table 1.

As we can see from table 1, the preliminary results are promising. Almost 75% recognized at least 2 bankruptcies, 3 persons recognized all of them; the mean is 1.95. A few years ago, we used the same firms for comparing the use of Chernoff's faces and that of numerical data for forecasting bankrupt companies. Then we found that the mean of right answers for the Chernoff's faces was 1.71 and for the numerical data 1.36. It is very encouraging that our new results are not poorer than our previous ones, even though the experiments are not quite comparable, because our previous test consisted of the data from 5 years 74–78, and the subjects were bank-managers.

![](/api/attachments/WTU6VNRA/fulltext/images/8b759fb06e96f57bc80df81bdcce3a235da22dd3774a7df2cef372902abe83ab.jpg)  
Fig. 6. A sample display of a two-house comparison.

Table 1  
The distribution of correct forecasts.

<table><tr><td>No. of Correct Forecasts</td><td>Frequency of Correct Answers</td></tr><tr><td>0</td><td>1</td></tr><tr><td>1</td><td>2</td></tr><tr><td>2</td><td>14</td></tr><tr><td>3</td><td>3</td></tr></table>

## 4. Discussion

In this paper we have proposed the use of a new method called harmonious houses – for visualizing numerical data. Our aim was to develop a decision support system which helps to convey value information to a DM by means of a visual representation. The idea is based on two principles: harmony and symmetry. When the values of criteria are very close to the ideal solution, our houses are quite harmonious and symmetric; and when they are far from that, the houses are very disharmonious and asymmetric. We have proposed the use of harmony and symmetry for conveying positive–negative feelings, because these concepts are easily parametrized.

We are aware that our method is heavily dependent on how the house parameters are specified. It is vital to associate important criteria with the house parameters that are essential to determining the structure of the house – thus influencing the degree of harmony. Of course, the directions of the changes plays an essential role, too. The method is subjective, and therefore it is important that a DM takes full benefit from this subjectivity and uses his/her knowledge of the problem and its interrelated relationships in the best possible way. In some cases, to associate criteria with house parameters may be obvious, but sometimes it requires many iterations and, perhaps, a pre-analysis of the relationships of the criteria. Anyway, this task always depends on the problem, and there exists no “shortcuts” or clear rules how to parametrize the problem. Each DM is free to choose any method he/she likes; he/she can group the criteria and associate the criteria in one group with the same structural house parameters, e.g., the roof, or he/she can use the left and right sides in a systematic way to describe development, etc. Fortunately, in our experience, the method does not seem to be very sensitive to poor specifications.

Our experience so far is very encouraging, motivating us to continue working in this direction. For instance, a large insurance company in Finland is willing to use our software for illustrating the performance of their company vis-a-vis the other companies in the same industry.

A simple house that we have used in this study, is only a prototype. We can construct houses with more windows, doors, floors, etc., or even use “skyscrapers”, and present as many parameters as needed. We can also enlarge details and zoom the picture as proposed by Wallenius. If the criteria have, e.g., a natural hierarchical structure, we can associate the criteria of lower levels with the details initially invisible, but which become visible by zooming. How to utilize these ideas is due to further research.

## References

Andrews, D. (1972), Plots of High Dimensional Data, Biometrics, Vol. 28, pp. 125–136.

Chernoff, H. (1973), Using Faces to Represent Points in k-Dimensional Space Graphically, J. Amer. Statist. Assoc., Vol. 68, pp. 361–368.

Cohon, J. L. (1978), Multiobjective Programming and Planning, Academic Press, New York.

Everitt, B. (1978), Graphical Techniques for Multivariate Data, Heinemann Educational Books, London.

Flury, B. and Riedwyl, H. (1981), Graphical Representation of Multivariate Data by Means of Asymmetrical Faces, J. Amer. Statist. Assoc., Vol. 76, pp. 757–765.

Geoffrion, A., Dyer, J. and Feinberg, A. (1972), An Interactive Approach for Multi-Criterion Optimization, with an Application to the Operation of an Academic Department, Management Science, Vol. 19, pp. 357–368.

Grauer, M. (1983), Reference Point Optimization - The Nonlinear Case, in Hansen, P. (ed.): Essays and Surveys on Multiple Criteria Decision Making, Springer-Verlag, Berlin, pp. 126-135.

Grauer, M., Lewandowski, A. and Wierzbicki, A. (1984), DIDASS – Theory, Implementation and Experiences, in Grauer, M., and Wierzbicki, A. (eds.): Interactive Decision Analysis, Springer-Verlag, Berlin, pp. 22–30.

Jacquet-Lagreze, E. and Siskos, J. (1982), Assessing a Set of Additive Utility Functions for Multicriteria Decision Making, the UTA method, European Journal of Operational Research, Vol. 10, pp. 151–164.

Kok, M. and Lootsma, F. (1985), Pairwise-Comparison Methods in Multiple Objective Programming, with Applications in a Long-Term Energy-Planning Model, European Journal of Operational Research, Vol. 22, pp. 44–55.

Korhonen, P. (1984), Subjective Principal Component Analysis, Computational Statistics and Data Analysis, Vol. 2, pp. 243–255.

Korhonen, P. (1986), A Hierarchical Interactive Method for Ranking Alternatives with Multiple Qualitative Criteria, European Journal of Operational Research, Vol. 24, pp. 265–276.

Korhonen, P. (1987): VIG - A Visual Interactive Support System for Multiple Criteria Decision Making, Belgian Journal of Operations Research, Statistics and Computer Science, Vol. 27, pp. 3–15.

Korhonen, P. and Laakso, J. (1986), A Visual Interactive Method for Solving the Multiple Criteria Problem, European Journal of Operational Research, Vol. 24, pp. 277–287.

Korhonen, P., Wallenius, J. and Zionts, S. (1980), A Bargaining Model for Solving the Multiple Criteria Problem, in Fandel, G. and Gal, T. (eds.): Multiple Criteria Decision Making Theory and Application, Springer-Verlag, Berlin, pp. 178–188.

Korhonen, P. and Wallenius, J. (1988), A Pareto Race, Naval Research Logistics, Vol. 35, No 6, pp. 615–623.

Mareschal, B. and Brans, J.-B. (1988), Geometrical Representations for MCDA, European Journal of Operational Research, Vol. 34, pp. 69–77.

Saaty, T. (1980), The Analytic Hierarchy Process, McGraw-Hill, New York.

Schilling, D., Revelle, C. and Cohon, J. (1983), An Approach to the Display and Analysis of Multiobjective Problems, Socio-Economic Planning Sciences, Vol. 17, pp. 57–63.

Silverman, J., Steuer, R. and Whisman, A. (1985), Computer Graphics at the Multicriterion Computer/User Interface, in Haimes, Y., and Chankong, V. (eds.): Decision Making with Multiple Objectives, Springer-Verlag, Berlin, pp. 201–213.

Steuer, R. (1986), Multiple Criteria Optimization: Theory, Computation, and Application, John Wiley and Sons, New York.
