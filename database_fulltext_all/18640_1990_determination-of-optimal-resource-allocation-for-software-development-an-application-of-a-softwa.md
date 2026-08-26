---
otero_id: 18640
otero_key: "GG47HGSE"
title: "Determination of optimal resource allocation for software development — An application of a software equation"
authors: "Yaw-Chin Ho; Carl D. McDevitt"
year: "1990"
journal: "Information & Management"
doi: "10.1016/0378-7206(90)90054-l"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Determination of Optimal Resource Allocation for Software Development – An Application of A Software Equation

Yaw-Chin Ho and Carl D. McDevitt

Department of Information Systems, School of Business, Auburn University at Montgomery, Montgomery, Alabama 36117-3596, USA

In every development project, software development managers face the problem of efficiently and effectively allocating scare resources to meet organizational needs. Previous work by Putnam and Boehm focused on the development of software cost models that measured the amount of development effort and the development time committed for a particular project. However, neither model provides a clear mechanism for determining whether a particular combination of development effort and development time are at the maximum productivity level or at the minimum cost. The purpose of this article is extend previous work by proposing a process that allows the software manager to determine the trade off between development effort and development time that will maximize productivity or minimize cost for a given software system.

Keywords: Software Cost Estimation, Software Development Cost Function, Software Equations, Software Economics.

## 1. Introduction

Software development managers begin each project with the following questions: Can I do it? How much will it cost? How long will it take? How many people are needed? What are the risks? What are the resource trade offs? To assist managers in making decisions on software development, a great deal of effort has been devoted to the development of software cost-estimating models. Significant work in the area of cost estimation has been done by Putnam [6] and by Boehm [1].

The Putnam Model is based on an analysis of the software life-cycle in terms of the Rayleigh distribution of project personnel level versus time. Differing in detail, but alike in generic concept, Boehm provided a conceptualization that is gener-

![](/api/attachments/GG47HGSE/fulltext/images/e1ba35d2820876fbfafcca35da2342311e0763a08e65ca8b977be9f7018c4e3e.jpg)

![](/api/attachments/GG47HGSE/fulltext/images/c4f400d742a6a6d4927cf45c15aaf73ba22ceec5496dbc71f31e969e340a202e.jpg)  
Yaw-Chin Ho is an Associate Professor of Information Systems at Auburn University at Montgomery. He received his Ph.D. in Mathematics from the Peabody College of Vanderbilt University. His major research interests focus on software development and economics, and programming techniques. Dr. Ho is an active consultant to both public corporations and governmental organizations regarding a variety of information processing areas.

Carl McDevitt is Associate Professor and Chairman of the Department of Information Systems and Decision Science, Auburn University at Montgomery. Dr. McDevitt holds the Ph.D. from the University of Georgia. In addition to research in information systems and project management, Dr. McDevitt has been active in professional societies, serving as an officer in the Montgomery Chapter of DPMA, the Central Alabama Chapter of APICS, and Southeast DSI.

ally consistent with Putnam's estimation procedure for software costs. The Boehm model provides two equations. One estimates the number of person-months required to develop the most common type of software product in terms of thousands of delivered source instructions; the other estimates the development schedule in months.

To determine the trade off for different combinations of development effort and time, Putnam employed a “Size-Effort-Time Trade-Off Chart”. This is used to derive a combination of development time and effort that may produce a given software product in the ‘fastest time’ [5]. Boehm’s model does not directly address the trade off question, but does provide an equation relating person-months to development times. Neither model provides a clear mechanism for determining whether or not a particular combination of person-months (or person-years) and development time are at the maximum productivity level or at the minimum cost. The objective of this article is, therefore, to demonstrate how such maximum productivity or minimum cost solutions may be derived by extending these concepts.

## 2. Putnam's Model

Putnam's model is expressed by the following equation:

$$
\mathrm{S} _ {\mathrm{s}} = \mathrm{C} _ {\mathrm{k}} \mathrm{K} ^ {1 / 3} \mathrm{t} _ {\mathrm{d}} ^ {4 / 3},
$$

where

$S_{s}$ = number of end-product delivered source lines-of-code;

$C_{k}=$ a constant representing the state of technology;

$$
\mathbf {K} = \text { life   cycle   effort,   in   person   years };
$$

$$
\mathrm{t} _ {\mathrm{d}} = \text { development   time,   in   years. }
$$

In an example based upon an actual case history, Putnam derived a software equation for the SAVE system [5]

$$
\mathrm{S} _ {\mathrm{s}} = 1 0 4 0 0 \mathrm{K} ^ {1 / 3} \mathrm{t} _ {\mathrm{d}} ^ {4 / 3}.
$$

In this example, Putnam demonstrated that, in order to produce 98,475 source statements in two years, a nominal development effort of 23.59 person-years would be required. Assuming a cost of \$50,000 per person-year, this system would cost \$1.18 million. If the development time is reduced to 1.81 years, development effort required increases to 35.4 person-years at a cost of \$1.77 million. An increase of \$0.59 million in cost is incurred by trading 0.19 years for 11.81 person-years development effort. However, if development time is increased to 2.2 years, only 14.50 person-years and 0.73 million in cost would be expected. A reduction of \$0.45 million could be realized by substituting 0.2 years for 9.09 person-years development effort.

## 3. Boehm's Model

In his Basic COCOMO (Constructive Cost Model), Boehm derived nominal equations relating development effort in person-months and development time in months. The equations are as follows:

$$
\mathrm{MM} = 2. 4 (\mathrm{KDSI}) ^ {1. 0 5},\tag{1}
$$

$$
\mathrm{TDEV} = 2. 5 (\mathrm{MM}) ^ {0. 3 8},\tag{2}
$$

where

MM = number of person-months required to develop a given software product;

TDEV = development schedule in months;

KDSI = thousands of delivered source instructions.

Since Boehm's equations do not directly measure the impact of development time on the desired number of source instructions, the equations cannot be used to analyze the trade off between development time and effort. However, the equations can be combined to produce another model.

Different combinations of TDEV and MM for 20 KDSI Per Boehm/COCOMO.

<table><tr><td>TDEV (month)</td><td>MM</td></tr><tr><td>12</td><td>52.2</td></tr><tr><td>14</td><td>40.7</td></tr><tr><td>16</td><td>32.8</td></tr><tr><td>18</td><td>27.2</td></tr><tr><td>20</td><td>22.9</td></tr><tr><td>22</td><td>19.7</td></tr><tr><td>24</td><td>17.1</td></tr><tr><td>26</td><td>15.0</td></tr><tr><td>28</td><td>13.3</td></tr><tr><td>30</td><td>11.9</td></tr></table>

By multiplying equations (1) and (2) and solving for KDSI, the following equation can be derived: $KDSI = 0.1815 \left( MM \right)^{0.5909} \left( TDEV \right)^{0.9523}$ .

This equation has the same general form as Putnam's and can be used to describe the trade off between effort and time. Table 1 illustrates various combinations of development time and effort that might be used to produce a software system of 20,000 delivered source instructions (DSI).

## 4. Manager's Concern

Generally, the questions facing software managers may be reduced to the following:

1. What resources are required to produce a given software system?

2. What is the best combination of resources in terms of highest productivity or minimum cost?

While software cost estimating models focus on the first question, managers need to know how to determine a cost minimizing combination of resources. Previous efforts have approached the cost equation primarily by placing a cost on the direct labor associated with development effort and given little, if any, attention to the cost of development time.

By looking at the software equation as a production function and studying the rates of substitution between resources, and considering the cost of both inputs, the 'best' combination can be developed.

## 5. Rate of Substitution Between Time and Effort

As shown in Table 1, if development times stretch out for a given size of software product, fewer person-months are needed. Correspondingly, reducing development time will increase cost. However, the rate of trade-off varies. More person-months units are required to trade for a reduction of a development month when the development time becomes shorter. In other words, the rate of substitution of person-months for development months is decreasing as shown in Table 2.

Figure 1, an Isoquant Curve, depicts the numerical example shown in Table 2. A movement along the isoquant indicates how person-months must be substituted for TDEV in order to maintain production of 20 KDSI.

Table 2  
Rate of substitution of Man-Months for Development Months for 20-KDSI Software Systems.

<table><tr><td>TDEV</td><td>MM</td><td>d[MM]</td><td>d[MM]/d[TDEV]</td></tr><tr><td>12</td><td>52.2</td><td></td><td></td></tr><tr><td>14</td><td>40.7</td><td>11.5</td><td>5.75</td></tr><tr><td>16</td><td>32.8</td><td>7.9</td><td>3.95</td></tr><tr><td>18</td><td>27.2</td><td>5.6</td><td>2.80</td></tr><tr><td>20</td><td>22.9</td><td>4.3</td><td>2.15</td></tr><tr><td>22</td><td>19.7</td><td>3.2</td><td>1.60</td></tr><tr><td>24</td><td>17.1</td><td>2.6</td><td>1.30</td></tr><tr><td>26</td><td>15.0</td><td>2.1</td><td>1.05</td></tr><tr><td>28</td><td>13.3</td><td>1.7</td><td>0.85</td></tr><tr><td>30</td><td>11.9</td><td>1.4</td><td>0.70</td></tr></table>

The numerical examples provided in Table 2 demonstrate that when TDEV is 30 months, 1.4 person-months can be used to trade for 2 months development time, etc. The rate of substitution of person-months for development months changes from 0.7 person-months to 5.75 person-months; approximately a 720% increase. Again, the real question to DP managers is how they can determine the most economical combination to produce a given software system.

The experience of IBM in developing OS/360 is an example of this phenomenon. The IBM experience was summarized by Frederick P.

![](/api/attachments/GG47HGSE/fulltext/images/52b6493e716401b1c904df294b835366b6a1f8c774a1c6a81dc19ee2f9189440.jpg)  
Fig. 1. Isoquant for 20 KDSI.

Brooks, Jr. in his book, The Mythical Man-Month as follows:

“Adding manpower to a late software project makes it later.”

"One can derive schedules using fewer men and more months, ... one cannot, however, get workable schedules using more men and fewer months." [2]

Putnam also indicated that:

“Clearly, time is not a ‘free good’ and while you can trade people for time within narrow limits, it is a most unfavorable trade and is only justified by comparable benefits or other external factors.” [6]

## 6. A Theoretical Solution

Either of the software equations discussed above may be regarded as a software systems “production function” [3]. These production functions describe the relationship between the amount of resources (person-months and development time) used and the amount of product produced (KDSI). The relationship between product and resources may be one of constant, increasing, or diminishing returns. Therefore, a production function can assist DP managers in determining a technologically feasible combination of specific value of resources and product.

This is demonstrated in Figure 2, which was constructed using the software equation as a production function. The vertical axis measures output per unit of “PERSON” (MM/TDEV) for the average and marginal physical product curves, and total output for the total physical product curve. The horizontal axis measures the input of “person-months” divided by the constant input of “months”. Reading this axis from left to right, the ratio of “person-months” to “months” is increasing. The total product rises at an increasing rate up to D ( $K_{2}$ units of people) and at a decreasing rate to its maximum value at point A ( $K_{4}$ units of people) and declines beyond that point.

Average physical products (APP) and marginal physical products (MPP) curves are derived from the total physical products (TPP) curve. Up to $K_{3}$ units of persons, the slope of APP is increasing.

![](/api/attachments/GG47HGSE/fulltext/images/ef87d63361f2490341a9fed598ebfe0a31b87a51e2c8208dcf37749d33abfa18.jpg)  
Fig. 2. The Relationship of total, Marginal and Average Productivity.

The APP curve reaches its maximum at point E where MPP = APP and declines after that. The MPP curve represents the slope of the TPP curve at each point. Point A, for instance, represents the point where the slope of TPP or the MPP is zero and TPP is at its maximum. To the left of point A, an additional unit of “person” has a positive MPP and hence will increase output, if employed. To the right, an additional unit produces a decline in output. The MPP reaches its maximum value at point C, which corresponds on the TPP curve to inflection point D. The law of diminishing marginal returns therefore is evident after points C and D, associated with $K_{2}$ units.

From an operational perspective, DP managers should employ input combinations in Region II. Region I operations would be inefficient, because throughout this region adding units of “person” generates a higher average output and therefore a lower average cost per unit. Operation in Region III is uneconomical: additional units actually reduce output.

This approach may be difficult to implement. For practical purposes, an optimum combination of MM and TDEV for a given KDSI can be more easily determined by examining cost.

## 7. A Cost Related Solution - An Optimum Combination of Inputs

To determine the economically most efficient combination of development time and effort, a cost value must be assigned to both development time and person-months of effort. Associated with the software equation, a total cost equation may be expressed as:

$$
\mathrm{C} = \mathrm{P} _ {\mathrm{m}} (\mathrm{MM}) + \mathrm{P} _ {\mathrm{t}} (\mathrm{TDEV}),
$$

where

$$
\begin{array}{l} \mathrm {P_ {m}} = \text { cost   of   MM }; \\ \mathrm {P_ {t}} = \text { cost   of   TDEV }. \end{array}
$$

To demonstrate, assume $P_{m} = \$5K$ per person-month and $P_{t} = \$5K$ per month. Using the 20 KDSI example, Table 3 gives the cost associated with the alternative combinations developed in Table 2.

The minimum cost in column 6 is found with 15 person-months development effort and 26 months development time. If the manager changes the development time to 24 months, the increment cost penalty will be \$0.5K. On the other hand, if management decides to reallocate manpower and increase development time to 28 months, a penalty of \$1.5K is incurred.

![](/api/attachments/GG47HGSE/fulltext/images/2564adbf4d2f96d2c33d6707e2ae4f122c8de2b92f98faa6a66fc372c3cac504.jpg)  
Fig. 3. Isoquant and Price Curve for 20 KDSI.

Figure 3 depicts the data given in columns 1, 2, 3, and 4 of Table 3. The tangent point between the trade off curve (or isoquant) and the cost equation represents the most economical combination of TDEV and MM. It is clear that moving away from the tangent point in either direction will increase the total cost of development.

## 8. Cost of Time and Effort - Issues and Methods of Determination

In one article, Putnam stated that “... the important point is that the software equation gives us the linkage between system size, technological tools, effort, and schedule. Effort and time are coupled. You cannot change one without changing the other.” [6] Unfortunately, when estimating the dollar cost of software development, the current software cost models all focus on the dollar cost of labor in terms of person-months. Is the cost of development time a significant factor of the total dollar development cost? Putnam had an answer. He stated that:

Total Cost for 20 KDSI = 0.1815 \* MM $^{0.5905}$ \* TDEV $^{0.9523}$ at Various Unit Cost of MM and TDEV.

<table><tr><td>TDEV(1)</td><td>MM(2)</td><td>$5K * TDEV.(3)</td><td>$5K * MM(4)</td><td>$10K * TDEV(5)</td><td>$(6) =(3) + (4)</td><td>$(7) =(4) + (5)</td></tr><tr><td>30</td><td>11.9</td><td>150</td><td>59.5</td><td>300</td><td>209.5</td><td>359.5</td></tr><tr><td>28</td><td>13.3</td><td>140</td><td>66.5</td><td>280</td><td>206.5</td><td>346.5</td></tr><tr><td>26</td><td>15.0</td><td>130</td><td>75.0</td><td>260</td><td>205.0 *</td><td>335.0</td></tr><tr><td>24</td><td>17.1</td><td>120</td><td>85.5</td><td>240</td><td>205.5</td><td>325.5</td></tr><tr><td>22</td><td>19.7</td><td>110</td><td>98.5</td><td>220</td><td>208.5</td><td>318.5</td></tr><tr><td>20</td><td>22.9</td><td>100</td><td>114.5</td><td>200</td><td>214.5</td><td>314.5 *</td></tr><tr><td>18</td><td>27.2</td><td>90</td><td>136.0</td><td>180</td><td>226.0</td><td>316.0</td></tr><tr><td>16</td><td>32.8</td><td>80</td><td>164.0</td><td>160</td><td>244.0</td><td>324.0</td></tr><tr><td>14</td><td>40.7</td><td>70</td><td>203.5</td><td>140</td><td>273.5</td><td>343.5</td></tr><tr><td>12</td><td>52.2</td><td>60</td><td>261.0</td><td>120</td><td>321.0</td><td>381.0</td></tr></table>

“Clearly, time is not a ‘free good’, and it is a dangerous parameter to set arbitrary on this basis of external factors such as meeting the date of a trade show.”

“Schedule is the most critical problem in software development … if the development time is arbitrarily specified by managerial fiat, there is a high chance the system bandwidth will shape the input manpower and work profile to match as best it can.”

"The manager can only justify such a trade if the resulting benefits are comparable to the enormous cost incurred." [6] The substitutability of effort for time is the other issue.

## Brooks' law states that

“manpower and time are not interchangeable, that productivity rates are highly variable, and that there is no nice industry standard that can be modified slightly to give acceptable results for a specific job or software house.” [2]

Brooks' law may be explained in terms of the marginal rates of substitution of effort for time.

The above issues strongly imply that the cost of development time can not be ignored, but must be addressed during the determination of the total cost of software development. For example, based on Putnam and Boehm models, if the dollar cost of a unit of person-month is \$5,000, then 11.9 MM will cost \$59,500 which is the total dollar cost of the system. This approach for estimating the total development cost has two shortcomings:

1. The total cost increases as the units of MM are increased, but there is no indication as to which units of MM may have the highest productivity.

2. The approach apparently underestimates the total cost, since it ignores the cost of development time. For example, if the cost of the development time is \$5,000, then the total cost of producing 20 KDSI using 11.9 person-months in 30 months is \$209.5K. If the unit cost of the development time is higher (\$10K), the total cost will be higher. Furthermore, by considering the development time and development effort together, the highest productivity of development time and effort can be clearly identified.

Although there are few previous studies that have directly discussed the estimation of the cost of development time, the basis for this cost estimation may be found in the concepts of opportunity and production cost. In his COCOMO model, Boehm suggested that when the required development schedule shifts away from its nominal level, the total cost could be increased as much as 23%. [1] The following factors may be considered as significant determinants of schedule cost:

1. Base costs include the opportunity cost of “buying” rather than developing the system. If the firm decides to contract the software development with a software house instead of developing in-house in order to “buy time” for other projects, the cost paid to the software house can be used as the basis of the development time cost. Normally, this would be higher than the cost of in-house development.

2. Setup costs include preparing the “production line” for the job, plus the cost of testing and any spoilage that is expected during the test period. These will be incurred regardless of whether the system is developed internally or not. But when the system is developed externally, these costs will be included in the “price” of the system.

3. Delay costs may be incurred when the system cannot be completed on time. They may include out-of-pocket costs of making special attempts to retain the “project” schedule. Project retention efforts are not always successful and any lost revenue must also be included in the delay costs. Perhaps the project revenue (or customer’s business) will be lost only on this project, but there is a chance of losing support or business on a continuing basis. Conceptually, then, the opportunity cost should be measured as the present value of the expected losses resulting from the delay. For a software house, the “delay cost” may occur at “a fixed-price, fixed-delivery contract with penalties for nonperformance!” [4]

4. Costs for hiring, relocation and training during the development due to the following causes:

a. Personnel attrition during development: The U.S. average voluntary turn over of programmers per year has been from 12% to 65%.

b. Unreasonable/unachievable schedule constraints: When the schedule for a project is totally unreasonable and unrealistic, morale drops. As a result, the employees with the most experience and skill tend to quit and are replaced by new personnel with less skill and experience.

This cost is quite high. Indeed it would not be “impossible for an enterprise to spend \$100,000 to fill a senior position: half for moving costs and half for training costs.” [4]

5. Holding costs, including insurance, deterioration, interest and the opportunity costs of investing funds in software development activities. The longer the development time, the higher the holding costs.

## 9. Conclusion

One of the important properties of Putnam's and Boehm's models is that software product, in terms of source instructions (or lines of code), is directly dependent on the two input factors: person-months and development time. This means that different combinations of input can produce a given level of output or one input can be substituted for another so as to maintain a constant level of output. However, productivity is still governed by the law of diminishing returns and diminishing marginal rate of substitution. Even if person-months and development time are interchangeable, DP managers still need to know how output can be maximized for a given cost, or cost can be minimized for a given output to obtain the best trade off ratio between person-months and development time.

Unfortunately, the current software cost estimation models all focus on the cost of person-months without considering the cost of development time. One possible reason seems to be that no mechanism has yet been developed to price development time. This article suggests using a cost equation of all input factors and its associated software equation to determine the best combination of input factors for a given software product.

## References

[1] Barry W. Boehm, Software Engineering Economics, New Jersey: Prentice-Hall, 1981.

[2] Frederick P. Brooks, Jr., The Mythical Man-Month: Eassys on Software Engineering, Reading: Addison-Wesley Publishing Company, 1975.

[3] P. Ein-Dor & C.R. Jones, Information Systems Management: Analytical Tools and Techniques. New York: Elsevier Science, 1985.

[4] C. Jones, Programming Productivity, New York: McGraw-Hill, 1986.

[5] Larry H. Putnam, “Example of an early sizing, cost and schedule estimate for an application software system,” Tutorial Software Cost Estimating and Life-Cycle Control: Getting the Software Numbers, 102. New York: IEEE Computer Society Press, 1980.

[6] Larry H. Putnam, Tutorial Software Cost Estimating and Life-Cycle Control: Getting the Software Numbers, New York: IEEE Computer Society Press, 1980.

[7] Edwards Yourdon & L.L. Constantine, Structure-Design Fundamentals of a Discipline of Computer Program and Systems Design. New Jersey: Prentice-Hall, 1979.
