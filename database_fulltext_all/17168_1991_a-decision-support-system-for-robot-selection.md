---
otero_id: 17168
otero_key: "HRVBARZQ"
title: "A decision support system for robot selection"
authors: "Mao-Jiun J. Wang; Haymwantee P. Singh; Wilfred V. Huang"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90044-c"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for robot selection

Mao-Jiun J. Wang

National Tsin Hua University, Hsin Chu, Taiwan, ROC

Haymwantee P. Singh and Wilfred V. Huang

Alfred University, Alfred, NY 14802, USA

This paper presents a decision support robot selection system which applies the fuzzy set method to this multicriteria decision making problem. The objective robot attributes are evaluated via marginal value functions while the subjective robot attributes are evaluated via fuzzy set membership function. Data from both evaluations are finally processed such that a fuzzy set decision vector is obtained. Viewpoints of several members of a decision making body are integrated. Sensitivity analysis has shown that final choices can be varied when the weight assignments are changed.

Keywords: Robot selection, Decision support system, Fuzzy set membership function, Marginal value function, Multiple criteria decision making.

## 1. Introduction

![](/api/attachments/HRVBARZQ/fulltext/images/452be2cefb05d78bf0e31f7f28194f2be10605abd6a7229ac1c1862871d92cee.jpg)

The robot's significant contribution to productivity in manufacturing has gained outstanding recognition. There is even a greater future ahead for robots as engineers begin to unwind the application spiral. According to Critchlow [4], more than 100,000 robots will be installed in the United States by 1990. The widespread applications and the increasing growth of the robot industry are now creating problems in new directions. The selection mechanism for robots is becoming more and more complex as the number of robot vendors increases. More than 90 robot manufacturers and distributors and some 200 different robot styles has been reported in USA [15]. Prospective robot buyers are now faced with a situation of having to make a choice from among several robots which are all capable of performing a similar task.

Mao-Jium J. Wang is an associate professor of Industrial Engineering at National Tsin Hua University, Taiwan, R.O.C.. Prior to that he was an assistant professor in Industrial Engineering at Alfred University. He received his Ph.D. in Industrial Engineering from the SUNY-Buffalo in 1986. His research interests include industrial ergonomics, decision support system, and industrial inspection. He is a senior member of IIE.

There are over 50 potential robot attributes that may have to be considered for the selection of a particular robot application [10]. These robot attributes can be classified into two categories: (1) Objective attributes – these attributes are defined numerically, e.g. cost, repeatability, position accuracy and load capacity. (2) Subjective attributes – these attributes have qualitative definitions, e.g. vender's service contract, training, programming flexibility, and man-machine interface. Lists of robot attributes can be accessed from existing literature on robotics (e.g. [5] and [12]).

![](/api/attachments/HRVBARZQ/fulltext/images/8012ad1f20a28374485d4a3303f4498961201f2fb9a712f9f2313e5c4a2bbe4b.jpg)

Haymwantee P. Singh is presently head of Information Department, Institute of Applied Science and Technology, Georgetown, Guyana, South America. She received a B.A. degree in Mathematics from University of Guyana in 1985 and a M.S. in Industrial Engineering from Alfred University in 1988. Her research interests include mathematical modelling and operation research.

![](/api/attachments/HRVBARZQ/fulltext/images/1aea9471a49f732a0004bfe08fb562653b635877877cd786f05f3b650bb4404a.jpg)  
Wilfred V. Huang is an associate professor in Industrial Engineering at Alfred University, N.Y.. He has a B.S. degree in I.E. from Purdue University, and a M.S. and Ph.D. degree from SUNY-Buffalo. His research interests include applied operation research, manufacturing system, and computer simulation. Dr. Huang is a senior member of IIE.

Since robot selection is a rather new field for researchers, only a few selection methods are reported. One of the earlier robot selection methods was developed by Knott and Getto [9]. The methodology of this model is based on an economic evaluation through which a final choice of a robot system is made from several alternatives which can be used in the same production process. The cost factors to be considered are: (a) investment, (b) overhead, and (c) labor. Therefore, the strict robot attributes which entered the decision making model were costs. Subsequently, Huang and Ghandfourish [7] introduced a method whereby the robot selection criteria were categorized into 3 main groups: (a) critical factors, (b) objective factors, (c) subjective factors. The objective category was considered as 'total costs'. This category was given a different treatment from the subjective category since cost can be assigned numerical values. The factors in the subjective group were defined in linguistic terms. Each factor was either defined as excellent/good/average/poor or yes/no. In the case of a yes/no answer, the problem is that the decision maker has to make an exact response to a situation where there can be a degree of availability or non-availability of the factor which is neither maximum nor minimum (i.e. not exactly equal to one or zero). The fact is that any degree of availability which lies between 0 and 1 is not accounted for by the model. Another article by Jones et al. [8] introduced more technicality into the idea of robot selection. This is a computerized robot selection system which engages the user in a type of interrogation procedure. This research highlighted that robot attributes could be classified into two groups namely numeric and discrete. However, the discrete attributes, e.g. vendor's reputation, service contract, programming flexibility had to be evaluated as available or unavailable, and there is no scale between the two extreme points.

More recently, a robot selection procedure was developed which outlined the development of a coding and classification system which issued to code and store robot characteristic properties in a database. The coding system is used to select the robots that can perform a specified task $[10]$ . This methodology first seeks to help the user to make a selection of a number of robots which are capable of performing in the same production process. Then after a selection is made economic modeling is applied whereby the final choice of the most cost effective robot from among all the alternatives is made.

The main issue of concern is the subjective robot attributes. In the cases where these attributes were considered in the decision making process, there is a restriction on the description and evaluation of the attributes. Thus numerical assignments by the members of the decision making team for attributes vs. alternatives may not be expressions of the true feelings of those members. In actual fact, a decision maker is not allowed to further quantify the given linguistic descriptions even if the case so demands from his point of view. Therefore this is a limitation imposed on these fuzzy or imprecise quantifications. In order to compensate this limitation, fuzzy set concept introduced by Zadeh [14] is proposed. By definition, a fuzzy set is a class of objects with a continuum of grades of membership. Such a set is characterised by a membership function which assigns to each object a grade of membership ranging between 0 and 1 [14]. This concept of fuzzy sets has also been applied to the evaluation of a multicriteria decision making problem ([1], [2], [3], and [6]). Hipel's fuzzy set multicriteria modeling approach is applied here to evaluate the subjective attributes and to process all the robot attributes [6]. Through fuzzy set multicriteria decision making process, a final decision vector of alternative is determined. The alternative robot with the highest value in the vector is the best choice being recommended.

## 2. Robot Selection Model

The proposed decision support robot selection procedure using fuzzy set multicriteria decision making approach is shown in fig. 1.

In robot selection, as mentioned earlier, one is faced with the problem of making a choice from among several vendor alternatives associated with several robot attributes. The complexity of this task can be reduced if the number of attributes and alternatives can be reduced. This can be done by performing a task analysis in the absence of the robot. Task analysis is to evaluate all the functions and subtasks that will be performed by the robot, then to specify a profile of robot attributes needed to meet the process requirements. Through task analysis it will enable the prospective robot buyer to become aware of the essential and maybe additional attributes that this expected robot should have for it to meet the specific process requirements. It will also be possible to isolate a subset from the selected set of prospective robot vendors. This robot selection model requires that decision makers compare each robot attribute against the alternative robot in order to make a final choice. A report in [13] indicated that an individual cannot simultaneously compare more than $7 \pm 2$ objects without becoming confused. It is recommended for this robot selection model that at most nine robots be identified for the final evaluation.

![](/api/attachments/HRVBARZQ/fulltext/images/ef2310a9b6a34f3bc84441d48a07e58957b7950ab169ac164307f75a9c3040b7.jpg)  
Fig. 1. Flow diagram of robot selection procedure.

As per processing of robot attributes, it can first be divided into the objective and subjective categories. The objective attributes are evaluated using marginal value function in terms of direct and inverse linear relationship. In direct linear relationship, the preference for an attribute rises as attribute value rises. On the other hand, in inverse linear relationship, preference value rises as attribute value lowers. The marginal value functions for calculating scaled value of direct and inverse relationship are presented in the following:

For direct relationship:

$$
x = \left(x ^ {*} - x _ {i}\right) / \left(x ^ {*} - x ^ {0}\right),\tag{1}
$$

For inverse relationship:

$$
x = \left(x _ {i} - x ^ {0}\right) / \left(x ^ {*} - x ^ {0}\right),\tag{2}
$$

where $x^{0}$ is the lowest attribute value, $x^{*}$ is the highest attribute value, $x_{i}$ is the attribute value of alternative i. Scaled values which lie in the interval [0,1] are computed for each attribute with respect to each alternative robot. Therefore, a scaled value matrix can be obtained.

For subjective attributes, since members of the decision making team will be aware of the robot attributes associated with the prospective vendors, it will be required of them to rate each attribute against the alternative robots in the interval $[0,1]$ . This can be done via a simple rating questionnaire (fig. 2). The rating obtained from each member of the decision team can be considered as grade of membership $[6]$ . For K rating questionnaires, a modified pessimistic aggregated rating matrix R can be obtained by aggregating fuzzy set membership function together. For modified pessimistic aggregation:

$$
R _ {i j} = 1 / 2 \left[ \operatorname{Min} \left(r _ {i j} ^ {1}, r _ {i j} ^ {2}, \dots , r _ {i j} ^ {k}\right) + \left(1 / k \sum_ {k = 1} ^ {k} r _ {i j} ^ {k}\right) \right],\tag{3}
$$

where $r_{ij}$ is the rating of attribute i vs. alternative j, k is the number of decision makers involved.

The reason for using this modified pessimistic aggregation is that, not only will conservative opinions (expressed in the first term) be accounted for, but also a better estimate of overall opinions (expressed in the second term) will be considered since there will be a certain amount of deviation away from the purely pessimistic viewpoints.

Instructions: You are requested to rate an attribute with respect to an alternative in the domain [0,1], and the interval of 0.1.

1. Rate vender's service contract for robot 1.

$$
\begin{array}{c c c c c c c c c c c} \text {I - - - I - - - I - - - I - - - I - - - I - - - I - - - I - - - I - - - I - - - I - - - I - - - I} \\ 0. 0 & 0. 1 & 0. 2 & 0. 3 & 0. 4 & 0. 5 & 0. 6 & 0. 7 & 0. 8 & 0. 9 & 1. 0 \end{array}
$$

2. Rate vender's service contract for robot 2.

$$
\begin{array}{c c c c c c c c c c c} \text {I - - - - I - - - - I - - - - I - - - - I - - - - I - - - - I - - - - I - - - - I - - - - I - - - - I - - - - I} \\ 0. 0 & 0. 1 & 0. 2 & 0. 3 & 0. 4 & 0. 5 & 0. 6 & 0. 7 & 0. 8 & 0. 9 & 1. 0 \end{array}
$$

3. Rate vender's service contract for robot 3.

```txt
I----I----I----I----I----I----I----I----I----I
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
```

4. Rate vender's service contract for robot 4.

I----I----I----I----I----I----I----I----I----I
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0

5. Rate programming flexibility for robot 1.

I----I----I----I----I----I----I----I----I----I
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0

6. Rate programming flexibility for robot 2.

I----I----I----I----I----I----I----I----I----I
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0

7. Rate programming flexibility for robot 3.

I----I----I----I----I----I----I----I----I----I
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0

8. Rate programming flexibility for robot 4.

```txt
I----I----I----I----I----I----I----I----I----I
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
```  
Fig. 2. Rating questionnaire.

Further, since both objective and subjective attributes are independent and having the same domain range $(0, 1)$ , the values associated with both subjective and objective attributes can be put together to form a new matrix C of n alternatives and m robots. Thus, weightings associated with both subjective and objective attributes can be evaluated simultaneously.

The individual weighting vectors can be developed by asking each member to weigh the attributes through questionnaire (fig. 3). The K weighting column vectors of weighted attributes (objective and subjective) can be processed in a similar manner as the K rating matrices to obtain a modified pessimistic aggregated weighting vector, W. Like matrix C, the values in vector W are independent and having the same domain range $(0, 1)$ . It is admissible that the transpose $W^{T}$ of column vector W is multiplied by the matrix C to give the vector V.

$$
W _ {(1 \times n)} ^ {T} * C _ {(n \times m)} = V _ {(1 \times m)}.\tag{4}
$$

This vector V is a decision vector of values for alternatives 1, 2, ..., m. Again the alternatives can be ranked in descending order of magnitude so that the best can be chosen, i.e., the alternative with the highest value. This is the vector on which the final choice will be made. This vector V has

Instructions: You are requested to weight the attributes in

the domain [0,1], and the interval of 0.1.

1. Assign a weight to purchase cost.

```txt
I----I----I----I----I----I----I----I----I----I
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
```

2. Assign a weight to load capacity.

```txt
I----I----I----I----I----I----I----I----I----I
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
```

3. Assign a weight to repeatability.

```csv
I----I----I----I----I----I----I----I----I----I----I
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
```

4. Assign a weight to vender's contract.

```txt
I----I----I----I----I----I----I----I----I----I
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
```

5. Assign a weight to programming flexibility.

```txt
I----I----I----I----I----I----I----I----I----I
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
```

Fig. 3. Weighting questionnaire.

This section of the program deals with the objective

attributes. Order the attributes in any chosen way.

Input the number of objective attributes:

example: 3

Input the number of identified robots:

example: 4

Input the value of attribute #, \_\_, for robot, \_\_:

example:

Input the value of attribute #, \_\_, for robot, 1 :

> 3500.00

1 2

•

•

•

n m

Fig. 4. Screen format for inputing objective attributes.

This section of the program deals with the subjective

attributes. Order the attributes in any chosen way.

How many rating questionnaires do you have:

example:

> 5

Input the number of subjective attributes:

example:

> 2

This is rating matrix # \_.

example:

This is rating matrix # 1:

Type in the rating value of attribute, \_\_, robot, \_\_,:

example:

Type in the rating value of attribute, 1, robot, 1 :

> 0.8

Type in the rating value of attribute, 1, robot, 2 :

> 0.5

Fig. 5. Screen format for inputing subjective attributes.

been computed on the grounds that the attributes are weighted in order of preference by the decision making body. An algorithm which summarizes the robot selection multiple-criteria decision making procedure is shown in table 1. A computer software was developed on the IBMPC which accounts for the entire decision making model. The demonstration of the first screen for objective and subjective attributes processing is illustrated in figs. 4 and 5 respectively.

most \$65,000. After a task analysis, it has been identified that the desired load capacity should be at least 25 pounds, and the repeatability should be within 0.1 inch. In addition, programming flexibility and vendor's service are also considered as important decision attributes. Four robots that are capable to perform this machine loading task and meet the constraints were chosen from the American Machinist Special Report 745 [11]. Five attributes identified for this prospective robot are as follows:

## 3. A Hypothetical Example

(1) Purchase cost.

An example is illustrated following the procedure in table 1.

(2) Load capacity.

(3) Repeatability.

(4) Vendor's service contract.

(5) Programming flexibility.

Step 1

It is assumed that there is need for a robot to perform a machine loading task, and that the prospective robot buyer can afford to spend at

Step 2

These attributes were divided into 2 groups as shown in table 2. The objective attributes include purchase cost, load capacity and repeatability. The

1. Perform a task analysis, then select the desired attributes for the robot to be purchased and identify the prospective robot vendors.

2. Place the robot attributes into the subjective and objective categories.

3. Identify the appropriate preference value function and its associated marginal value function for each objective attribute.

4. Tabulate the value of each objective attribute for each alternative.

5. Compute the scaled value using the marginal value function for each objective attribute with respect to each alternative. Tabulate the results in matrix form - attributes vs. alternatives.

6. Obtain fuzzy set membership function by requesting each member of the decision making body to rate each subjective attribute against each alternative robot.

7. Develop a modified pessimistic aggregated rating matrix from the K decision makers' rating matrices of attributes vs. alternatives.

8. Combine the scaled values of objective attributes and the aggregated ratings of subjective attributes to form a matrix C.

9. Request each member of the decision making body to assign a weight to each attribute such that there will be K weighting vectors for K members.

10. Develop a Modified Pessimistic Aggregated Weighting Vector W from the K weighting vectors.

11. Multiply the transpose of W by the C matrix to obtain the decision vector V. Identify the alternative with the highest numerical value.

Table 2  
Categorized Robot Attributes.

<table><tr><td>Objective Attributes</td><td>Subjective Attributes</td></tr><tr><td>Purchase Cost</td><td>Vendor&#x27;s Service Contract</td></tr><tr><td>Load Capacity</td><td>Programming Flexibility</td></tr><tr><td>Repeatability</td><td></td></tr></table>

Table 1
Stepwise Description of Robot Selection Algorithm.  
Table 3  
Objective Attribute with Associated Marginal Value Function.

<table><tr><td>Attribute</td><td>Marginal Value Functiona</td></tr><tr><td>Purchase Cost</td><td> $(x^{*} - x_{i})/(x^{*} - x^{0})$ </td></tr><tr><td>Load Capacity</td><td> $(x_{i} - x^{0})/(x^{*} - x^{0})$ </td></tr><tr><td>Repeatability</td><td> $(x^{*} - x_{i})/(x^{*} - x^{0})$ </td></tr></table>

$^{a}x^{0}$ is the lowest attribute value, $x^{*}$ is the highest attribute value, $x_{i}$ is the attribute value of alternative i.

subjective attributes include vendor's service contract and programming flexibility.

## Step 3

The marginal value function for each objective attribute was identified and presented in table 3. For cost, a lower value is often preferred by purchasers. There is also a very strong preference for this attribute. For an increase in attribute value there is a significant decrease in preference value. The same reason is also true for repeatability. Therefore, both attributes are represented by an inverse marginal value function. However, for load capacity, a higher attribute value is preferred. As this attribute value increases, the preference value increases linearly. Therefore, this attribute is represented by the direct marginal value function.

## Step 4

The information regarding the objective attribute value for each robot is shown in table 4. The highest and the lowest value for each attribute is also determined. They are listed beneath table 4.

## Step 5

Using the attribute values from table 4 and the marginal value functions from table 3, the scaled values for an attribute with respect to each alternative can be calculated. Thus for the attribute cost and the robot 1, the scaled value is computed as follows:

Table 4  
Objective Attribute Value for Each Robot $^{4}$

<table><tr><td rowspan="2">Objective Attributes</td><td colspan="4">Alternative Robots</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>(1) Purchase Cost ($)</td><td>35,000</td><td>60,000</td><td>50,000</td><td>55,000</td></tr><tr><td>(2) Load Capacity (lbs.)</td><td>50</td><td>55</td><td>100</td><td>150</td></tr><tr><td>(3) Repeatability (ins.)</td><td>0.008</td><td>0.02</td><td>0.03</td><td>0.06</td></tr></table>

$^{a}x^{0}=$ lowest attribute value $\Rightarrow$ (1) purchase cost = 35,000,  
(2) load capacity = 50,  
(3) repeatability = 0.008.  
$x^{*} =$ highest attribute value $\Rightarrow$ (1) purchase cost $= 60,000$  
(2) load capacity = 150,  
(3) repeatability = 0.06.

Table 5  
Scaled Values for Objective Attributes.

<table><tr><td rowspan="2">Attributes</td><td colspan="4">Alternatives</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Purchase Cost</td><td>1.0</td><td>0.0</td><td>0.4</td><td>0.2</td></tr><tr><td>Load Capacity</td><td>0.0</td><td>0.05</td><td>0.5</td><td>1.0</td></tr><tr><td>Repeatability</td><td>1.0</td><td>0.769</td><td>0.577</td><td>0.0</td></tr></table>

$$
\begin{array}{r l} \left(x ^ {*} - x _ {i}\right) / \left(x ^ {*} - x ^ {0}\right) & = (6 0 - 3 5) / (6 0 - 3 5) \\ & = 1. 0. \end{array}\tag{5}
$$

The computed scaled values are tabulated in table 5.

## Step 6

It is a requirement that each member of the decision making body rate each subjective attribute against the alternative robots. Questionnaire scaled from 0 to 1 are used by decision makers to do the ratings. It is assumed that a 3-member decision making body completed the rating questionnaire. These individual ratings are summarized in table 6.

## Step 7

Through fuzzy set aggregation procedure, a modified pessimistic aggregated rating matrix R (shown in table 7) is calculated by applying:

$$
R _ {i j} = 1 / 2 \left[ \operatorname{Min} \left(r _ {i j} ^ {1}, r _ {i j} ^ {2}, r _ {i j} ^ {3}\right) + 1 / 3 \sum_ {k = 1} ^ {3} r _ {i j} ^ {k} \right],\tag{6}
$$

where $r_{ij}$ is the aggregated rating of attribute i vs. alternative j.

Table 6  
A Combination of Three Decision Maker's Rating Matrix.

<table><tr><td rowspan="2">Attribute</td><td colspan="4">Alternative</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td colspan="5">Vendor&#x27;s Service Contract</td></tr><tr><td>DM1</td><td>0.8</td><td>0.5</td><td>0.9</td><td>0.7</td></tr><tr><td>DM2</td><td>0.8</td><td>0.6</td><td>0.8</td><td>0.65</td></tr><tr><td>DM3</td><td>0.75</td><td>0.45</td><td>0.7</td><td>0.6</td></tr><tr><td colspan="5">Programming Flexibility</td></tr><tr><td>DM1</td><td>0.6</td><td>0.85</td><td>0.8</td><td>0.9</td></tr><tr><td>DM2</td><td>0.5</td><td>0.65</td><td>0.6</td><td>0.7</td></tr><tr><td>DM3</td><td>0.4</td><td>0.6</td><td>0.4</td><td>0.6</td></tr></table>

Table 7  
Modified Pessimistic Aggregated Rating Matrix R.

<table><tr><td rowspan="2">Attributes</td><td colspan="4">Alternatives</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Vendor&#x27;s Service Contract</td><td>0.766</td><td>0.485</td><td>0.75</td><td>0.625</td></tr><tr><td>Programming Flexibility</td><td>0.45</td><td>0.65</td><td>0.5</td><td>0.665</td></tr></table>

Table 8  
The Formation of Matrix C by Puting Objective and Subjective Attributes Values Together.

<table><tr><td rowspan="2">Attributes</td><td colspan="4">Alternatives</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Purchase Cost</td><td>1.0</td><td>0.0</td><td>0.632</td><td>0.447</td></tr><tr><td>Load Capacity</td><td>0.0</td><td>0.05</td><td>0.5</td><td>1.0</td></tr><tr><td>Repeatability</td><td>1.0</td><td>0.769</td><td>0.577</td><td>0.0</td></tr><tr><td>Vendor&#x27;s Service Contract</td><td>0.766</td><td>0.485</td><td>0.75</td><td>0.625</td></tr><tr><td>Programming Flexibility</td><td>0.45</td><td>0.65</td><td>0.5</td><td>0.665</td></tr></table>

## Step 8

The scaled values of the objective attributes and the aggregated ratings of subjective attributes were put together to form the C matrix as shown in table 8.

## Step 9

At this point, the three assumed decision makers assigned weights to the attributes. Again a questionnaire can be provided for this task. In this case three weighting vectors were obtained from the decision makers as in table 9.

## Step 10

From table 9, a modified pessimistic aggregated weighting vector W was calculated using a similar approach to the R matrix. The transpose $W^{T}$ of this vector W is

$$
W ^ {T} = (0. 8 5, 0. 7 1, 0. 8 4, 0. 6 1 5, 0. 5 1 5).\tag{7}
$$

Table 9  
Individual Weighting Vectors.

<table><tr><td rowspan="2">Attributes</td><td colspan="3">Weighting Vector</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>Purchase Cost</td><td>0.9</td><td>0.85</td><td>0.85</td></tr><tr><td>Load Capacity</td><td>0.7</td><td>0.75</td><td>0.7</td></tr><tr><td>Repeatability</td><td>0.85</td><td>0.9</td><td>0.8</td></tr><tr><td>Vendor&#x27;s Service Contract</td><td>0.7</td><td>0.6</td><td>0.6</td></tr><tr><td>Programming Flexibility</td><td>0.5</td><td>0.55</td><td>0.55</td></tr></table>

Step 11

This row vector $W^{T}$ was multiplied by the C matrix to obtain a row vector V which is a decision vector of alternative values after the attributes have been weighted. This vector is

$$
V = (2. 3 9 2 8, 1. 3 1 4 4, 2. 0 9, 1. 8 1 6).\tag{8}
$$

According to the order of magnitude in decision vector V, the final ranking for alternatives in descending order is: robot 1, robot 3, robot 4, and robot 2. Therefore, the best choice is robot 1 and the second best choice is robot 3.

## 4. Sensitivity Analysis

The main purpose of sensitivity analysis is to see how the final results are affected by changes in the input data and method of analysis [6]. Sensitivity analysis also serves to increase the decision maker's confidence in the results obtained after applying a specific method. In this study, the aim is to give the decision makers an idea about how the weighting assignment changes can affect the outcome of the robot selection.

The decision maker may raise the question, "What will the vector $V$ be like if changes in the vector $W$ of weighted attributes are made?" Since there exist many solutions to this, the question is restated as, "What will be the least changes in the vector $W$ of weighted attributes should a specific robot $k$ be chosen instead of the one identified as the 'best choice' from the vector $V$ ?"

Two models were proposed, linear and non-linear programming models, to answer the above questions. The objective function was to minimize the differences between the original weights and the newly assigned weights if any, such that robot k be selected.

## Model 1: Linear Programming Model

Given: $m$ robots

$n$ attributes

Let $w_{i}$ be the current weight of the attribute. $x_{i}$ be the new weight of the attribute.

$c_{ij}$ be the element $(i,j)$ of the combined matrix $C$ of ratings.

$y_{j}$ be the new value for robot $j$ .

Assume robot k is the best robot.

Since the objective function is to minimize the deviation of any weight, it is expressed as

$$
\text { Minimize } \sum_ {i = 1} ^ {n} \left(x _ {i} - w _ {i}\right) \text { subject   to }\tag{9a}
$$

$$
\sum_ {i = 1} ^ {n} x _ {i} c _ {i j} = y _ {j}, \quad j = 1, 2, \dots , m,\tag{9b}
$$

$$
y _ {k} > y _ {j}, \quad V j, j \neq k,\tag{9c}
$$

$$
1 > x _ {i} > 0 \quad \text { for } \quad i = 1, 2, \dots , n,
$$

$$
y _ {j} > 0 \quad \text { for } \quad j = 1, 2, \dots , m.\tag{9d}
$$

(9e)

## Model 2: Non-linear Programming Model

Same as in model 1 except that the objective function is the sum of squares instead of the sum of absolute terms:

$$
\text { Minimize } \sum_ {i = 1} ^ {n} (x _ {i} - w _ {i}) ^ {2}.\tag{10}
$$

The non-linear model was emphasized here due to its reasonableness to penalize heavier the higher deviations for any weights. A linear approach however may introduce a large change for certain weights, leaving the rest of the weights unchanged.

To solve Model 2, the reduced gradient method was used. It can be shown that the function,

$$
f (x) = \sum_ {i = 1} ^ {n} \left(x _ {i} - w _ {i}\right) ^ {2}\tag{11}
$$

is convex. Therefore a global minimum exists.

The example was continued by solving the non-linear programming problem, and the results in table 10 was obtained. In column 1, robot 1 was assigned the status of “best” robot. Note the values computed for $x_{i}$ (new weights) are exactly the same as $w_{i}$ values (current weights). This can be compared with the weighting vector W.

Table 10  
Results from Non-linear Model.

<table><tr><td></td><td>Robot 1</td><td>Robot 2</td><td>Robot 3</td><td>Robot 4</td></tr><tr><td colspan="5"> $x_{i}$  (new weights,  $i = 1,\dots,5$ )</td></tr><tr><td>1.</td><td>0.85</td><td>0</td><td>0.61</td><td>0.72</td></tr><tr><td>2.</td><td>0.71</td><td>0.50</td><td>0.97</td><td>0.95</td></tr><tr><td>3.</td><td>0.84</td><td>0.64</td><td>0.66</td><td>0.60</td></tr><tr><td>4.</td><td>0.62</td><td>0.12</td><td>0.63</td><td>0.58</td></tr><tr><td>5.</td><td>0.52</td><td>0.84</td><td>0.51</td><td>0.57</td></tr><tr><td colspan="5"> $Y_{j}$  (value of each robot,  $j = 1,\dots,4$ )</td></tr><tr><td>1.</td><td>2.392</td><td>1.158</td><td>1.982</td><td>2.013</td></tr><tr><td>2.</td><td>1.315</td><td>1.158</td><td>1.942</td><td>1.572</td></tr><tr><td>3.</td><td>2.090</td><td>1.158</td><td>1.982</td><td>1.993</td></tr><tr><td>4.</td><td>1.810</td><td>1.114</td><td>1.982</td><td>2.013</td></tr><tr><td colspan="5"> $f$  (objective function value)</td></tr><tr><td></td><td>0</td><td>1.1379</td><td>0.1612</td><td>0.1399</td></tr></table>

$$
W = (0. 8 5, 0. 7 1, 0. 8 4, 0. 6 2, 0. 5 2).\tag{12}
$$

Thus the deviation between $x_{i}$ and $w_{i}$ in each case is zero. The objective function value is also zero. However, for comparison sake it can be observed in column 2 where robot 2 is selected as the “best” robot, that the new weights of all the attributes have changed significantly. The objective function value is the largest since the robot with the lowest rank was elevated to number 1. It should also be noted that this decision was made under the assumption that the difference between $y_{2}$ (robot 2) and $y_{i}$ (robot i), $i \neq 2$ , is greater than zero (example $y_{2} - y_{1} > 0$ ).

The output in column 2 of table 10 gives information that even though robot 2 is restricted as the “best” choice, values for robots 1 and 3 are similar to the robot 2. Therefore a small value epsilon $\epsilon$ was introduced such that

$$
y _ {2} - y _ {1} > \epsilon ,\tag{13}
$$

$$
y _ {2} - y _ {3} > \epsilon ,\tag{14}
$$

$$
y _ {2} - y _ {4} > \epsilon .\tag{15}
$$

It can be shown that there is a relationship between $\epsilon$ and the objective function values.

Finally, it should now be clear to the decision maker(s) that the choice of a robot will be partially dependent on the vector of weights W for the attributes.

## 5. Discussion and Conclusions

This paper highlights the idea that robot selection will become a very complex task for prospective robot buyers in the future, if not already. Existing literature on robot selection methods has been discussed and the limitations with respect to the subjective attributes were reviewed. Robot attributes which were classified as objective and subjective were not listed since much of this information is available in current literature on robotics. This model presented, processed the subjective attributes in a formalized manner. It can be applied by any decision making team whose intention is to consider subjective attributes when selecting a robot. An idea was expressed that a decision making team including technical experts be considered whenever this method will be used to make a selection of a robot.

The concept of task analysis was introduced to help those involved in decision making to become more formal and objective in their approach to robot selection. Through task analysis the decision makers will be forced to evaluate the proposed robot task such that awareness of needs becomes an important issue. As such specific attributes and vendors can be identified at a minimum level.

The main focus of this research was to use the concepts of the fuzzy set method to evaluate the subjective robot attributes in such a manner that the viewpoints of an entire decision making body can be expressed without any constraints. By applying the fuzzy set concepts, the subjective attributes can be evaluated by assigning numerical values in the domain range of $(0, 1)$ with increment interval of 0.1. Then numbers from different decision makers can be aggregated together by using fuzzy set modified pessimistic aggregation method. Thus these imprecise terms are allowed to assume exact values. The model was described and a simplified hypothetical example was presented. A computer software was developed on the basis of the decision making algorithm described.

A form of sensitivity analysis was developed to explain to the user that the viewpoints of the entire decision making body is expressed in the final decision making vector V. Should viewpoints vary in another application, then the final decision vector V, can also be changed. This conclusion is supported through the results obtained from the non-linear model discussed.

## References

[1] S.M. Baas and H. Kwakernaak, Rating and Ranking of Multiple-Aspect Alternatives Using Fuzzy Sets, Automatica 13 (1977) 47–58.

[2] J-M. Blin, Fuzzy Sets in Multiple Criteria Decision Making, TIMS Studies in the Management Sciences 6 (1977) 129–146.

[3] J.J. Buckley, The Multiple Judge, Multiple Criteria Ranking Problem: A Fuzzy Set Approach, Fuzzy Sets and Systems 13 (1984) 25–37.

[4] A.J. Critchlow, Introduction to Robotics (Macmillan Publ. Comp., New York, 1985).

[5] R.C. Dorf, Robotics and Automated Manufacturing (Reston Publ. Comp., 1983).

[6] K.W. Hipel, Fuzzy Set Methodologies in Multicriteria Modeling, in: M.N. Gupta and E. Sanchez, Eds., Information and Decision Process (North-Holland Publ. Comp., Amsterdam, 1985).

[7] P.Y. Huang, and P. Ghandforoush, Procedures Designed for Evaluating and Selecting Robots, Industrial Engineering 19, No. 4 (1985) 44–48.

[8] M.S. Jones, C.J. Malmborg, and M.H. Agee, Robotics: Decision Support System for Selecting a Robot, Industrial Engineering 17, No. 9 (1984) 66–73.

[9] K. Knott, and R.D. Gretto, A Model for Evaluating Alternative Robot Systems under Uncertainty, International Journal of Production Research 20, No. 2 (1982) 155–165.

[10] O.F. Offodile, B.K. Lambert, and R.A. Dudek, Develop-

ment of a Computer Aided Robot Selection Procedure (CARSP), International Journal of Production Research 25, No. 8 (1987) 1109–1121.

[11] American Machinist, Robots: Looking for the Specifications, Special Report 745, May 1982.

[12] R.J. Sanderson, J.A. Campbell, and J.D. Meyer, Industrial Robots: A Summary and Forecast for Manufacturing Managers (Tech Tran Co., 1982).

[13] T.L. Satty, A Scaling Method for Priorities in Hierarchical Structures, Journal of Mathematical Psychology, 15 (1977) 234–281.

[14] L.A. Zadeh, Fuzzy Sets, Information and Control, 8 (1965) 338–353.

[15] M.I. Zeldman, What Every Engineer Should Know about Robots (Marcel Dekker, Inc., 1984).
