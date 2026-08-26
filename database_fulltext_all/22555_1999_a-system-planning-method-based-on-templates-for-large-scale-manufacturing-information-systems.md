---
otero_id: 22555
otero_key: "RBWMDF6Y"
title: "A system planning method based on templates for large-scale manufacturing information systems"
authors: "H Morihisa; R Oshita; H Furukawa; J Kanda"
year: "1999"
journal: "Information & Management"
doi: "10.1016/s0378-7206(99)00003-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# A system planning method based on templates for large-scale manufacturing information systems

H. Morihisa $^{*}$ , R. Oshita, H. Furukawa, J. Kanda

Nippon Steel Information and Communication Systems Inc. (ENICOM), 1 Fuji, Hirohata, Himeji Hyogo 671-1188, Japan

Accepted 19 August 1998

## Abstract

In the field of manufacturing, there is a need to develop large-scale manufacturing information systems. This is especially true in the Japanese steel manufacturing industry where CIM is the core management technology. But developing such systems requires large amounts of time and manpower, and furthermore, these type of projects are very difficult to manage. Therefore, in order to ease the process of analysis and design, we propose procedures based on a two-dimensional template with specific criteria for large-scale manufacturing IS architectures. In each manufacturing system, there are two important elements that correspond to the two dimensions of the template. One is a functional category and the other is a management structure. We show here the effectiveness of applying this method to system planning of large-scale IS in one representative steel manufacturing plant. © 1999 Elsevier Science B.V. All rights reserved.

Keywords: IS planning; Evaluation of planning system; Planning system model; CIM; Steel plant

## 1. Introduction

In the field of manufacturing, there is a great need for the development of large-scale systems. For example, in the Japanese steel industry, computer integrated manufacturing (CIM) has become the core management technology since the latter half of the 1980s [4]. CIM depends mainly on large-scale manufacturing information systems (IS). Therefore, high-quality efficient system analysis, design and development are required in the field of manufacturing. Furthermore, it is difficult to manage large-scale manufacturing IS and such systems demand large resources, particularly of manpower and development time. Therefore, it is important to have an effective method with which we can analyze, design, develop and manage large-scale manufacturing IS.

In large-scale system development, common concepts concerning system methodology and system architecture are very important. A system development methodology using templates of specific manufacturing system architecture is one example.

However, current methodologies for required and structured analysis have some problems in the process of transformation from the logical to the physical model because of the lack of precise modeling criteria. To cope with this problem, we have analyzed the entities in the manufacturing process at steel plants and the management structure in the field of manufacturing. As a result of this investigation, we propose an analysis and design method based on a two-dimensional template that is effective in the implementation of large-scale manufacturing ISs. Also, we illustrate the effectiveness of this model by applying it to the development of an actual information system for one steel manufacturing plant in Japan.

## 2. Outline of the problem

## 2.1. Scope

Characteristics of the system for this steel manufacturing plant are as follows [2, 5]:

1. System type: multistage process production;

2. Constraints: nonstop operation;

3. Evaluation criteria: quality, cost, delivery and customer satisfaction; and

4. Control elements: working schedule and production lot size.

Additionally, characteristics of the IS for this steel manufacturing plant are as follows.

1. The IS have the following hierarchical structures: the process control layer, operation on-line layer and production management batch layer.

2. The IS have the function of planning company-wide optimal management strategies in order to assure quantity, delivery and quality of the products to customers, and, above all, to improve service quality so as to strengthen competitiveness in areas other than price.

## 2.2. Current methodology and their problems

We have been making use of the revised Demarco's integrated requirement and structured analysis methodologies which are shown in Fig. 1 [1, 2, 3].

Structured analysis consists of four phases: preparation of the present physical model; preparation of the present logical model; preparation of a future and extended future logical model; and preparation of a future physical model. The structured analysis methodology gradually results in detailed design through the expansion possible through the use of data flow diagrams, entity-relation diagrams and state-transition diagrams. The preparation of a future logical model from the present logical model calls for a requirement definition, and this may be performed through requirement analysis, output of which provides the expanded needs.

![](/api/attachments/RBWMDF6Y/fulltext/images/5308facb7922b6ff6d91ed0432440644baae9cc0fcfc8f88305fce3a6edac3c3.jpg)  
Fig. 1. Requirement and structured analysis methodologies.

However, such a total development methodology has certain problems that must be overcome, especially in logical modeling. These problems are:

1. Analysis of a large-scale system requires a lot of time and effort.

2. It takes a lot of time to transform a logical model into a physical model, because the process of analysis for both the models are separate from one another.

3. There are no precise guiding principles for system architecture and database design.

Therefore, we need modified procedures and guiding principles that are useful in system analysis and design. In this paper, we propose a system planning method based on templates as a guideline for the logical system architecture.

## 3. Template guidelines for large-scale systems

First, we investigate manufacturing systems and show their characteristic functions and management structures.

## 3.1. Management cycle

In the field of manufacturing, the management cycle is very important and is referred to as PDCA cycle or Demming circle. P, D, C and A denote ‘plan’, ‘do’, ‘check’ and ‘action’, respectively. Fig. 2 shows the function of the PDCA cycle in the field of the manufacturing [2].

![](/api/attachments/RBWMDF6Y/fulltext/images/4b25267d4d6b92da48e0929af4bc6ccf81372d08fd5cd3a0979171d1d7805f79.jpg)  
Fig. 2. Configuration of the manufacturing management.

In this management cycle, there are three major elements in the field of manufacturing: functions; management cycle; and management elements. We make use of these elements for the improvement of system analysis and design methods $[5]$ .

## 3.2. Function category and management structure

In our method of systems analysis, we use entity-relation diagrams. By analyzing various manufacturing IS, we realized that there are some critically important entities: these are the critical success factors (CSF). In the field of manufacturing plant management, CSF are quality, material, ordering and scheduling and each of them is orthogonal to the others. Therefore, we adopt this function category as one axis of the logical system architecture.

We categorize production business activity into the four business layers required in the business management cycle containing a Demming or PDCA cycle: planning; progress control; operation control; and plant control. We adopt these management layers as another axis of the logical system architecture. Features of each management layer are shown in Fig. 3.

## 3.3. Two-dimensional templates for manufacturing information logical models

During the first stage of system planning, guidelines for the information logical model, which are easily transformed to the physical model, are important. Thus, we propose two-dimensional templates for the logical models; their axes are the function categories and management layers. Fig. 4 shows the schema of templates for logical manufacturing models.

The manufacturing information system (MIS) is expressed in the following equation:

$$
\mathrm{MIS} = \sum \text { Subsystems } (l, m)
$$

where l represents planning, progress control, operation control and plant control and m represents quality, material, order and scheduling functions.

This logical model is easily transformed to the physical model. Both the logical and physical models have three structural axes and these structures of the logical and physical model axes resemble one another. Fig. 5 shows how the three axes of both logical and physical models correspond.

## 3.4. Evaluation of planning and modification

It is difficult to decide on the best system architecture by using only one procedure. It is necessary to modify the first architecture when evaluating the system architecture. The items to be evaluated in the IS architecture are listed below:

1. Suitability for PDCA system structure;

2. Partitioning of ‘Definition of Problems’, ‘Algorithm for Solution’, ‘Policy Making’;

3. Consistency and degree of loose coupling of the function category; and

4. Validity and degree of loose coupling of the business layers.

This leads us to modify and refine the system planning. Fig. 6 shows the iterative system planning procedures of the improved method for manufacturing IS planning.

Walston and Felix show that the elapsed time in IS development can be estimated by the equation [7]:

$$
D = 4. 1 \times L ^ {0. 3 6},
$$

where D is the duration of the project and L the estimated number of source lines (in thousands). This equation shows that we can decrease the time required in developing a project if we can divide the system into sub-systems, since we can then develop sub-systems parallel to each other.

<table><tr><td>Business layers</td><td>Features</td><td>Management cycle</td></tr><tr><td>Strategy</td><td>Decision Making of Enterprise Management StrategyDevelopment and Improvement of Planing Model by Analyzing historical dataStrong and Weak Point AnalysisProduction Forecast Using Models</td><td>Quarter-Year</td></tr><tr><td>Planning</td><td>Little Universality of Planning LogicProcessing Large Volumes of DataDepending Greatly on Environmental ConstraintSelecting the Most Profitable Strategic Solution from two or more SolutionsLarge Degree of Freedom and Wide Range of Solutions</td><td>Day-Week - Month</td></tr><tr><td>Progress Control</td><td>Multiple Manufacturing lines Control and CoordinationQuick reaction in Abnormal StatusDepending on Plant Facilities</td><td>Minutes-Hour</td></tr><tr><td>Operation Control</td><td>Depending on Plant FacilitiesRestricted and Fixed FunctionAssuring Response Time</td><td>Second</td></tr><tr><td>Plant Control</td><td>Modeling of Physical Phenomenon</td><td>Millisecond</td></tr></table>

Fig. 3. Features of management layers.

Furthermore, Putnam developed the following equation for estimation of development effort [6].

$$
K = L ^ {3} / (C _ {\mathrm{k}} ^ {3} t _ {\mathrm{d}} ^ {4}),
$$

where K is development effort, L the number of source lines (in thousands), $C_{k}$ a state-of-technology constant, and $t_{d}$ the development time. This equation shows that we can also save development effort if we can divide the system into sub-systems.

## 4. Results of applying this method to a real system

We applied this method based on templates to one of the manufacturing information systems of a steel production plant in Hirohata works in Nippon Steel. This is the total production management system of one steel plant. The estimated number of source lines of the system was 500 000 steps in PL/I language. The time available for system development was limited to ca. 20 months because of the time required for plant construction.

<table><tr><td></td><td>Quality</td><td>Material</td><td>Order</td><td>Scheduling</td></tr><tr><td>Planning</td><td></td><td></td><td></td><td></td></tr><tr><td>Progress control</td><td></td><td></td><td></td><td></td></tr><tr><td>Operation control</td><td></td><td></td><td></td><td></td></tr><tr><td>Plant control</td><td></td><td></td><td></td><td></td></tr></table>

Fig. 4. Two-dimensional templates schema for logical manufacturing systems.

![](/api/attachments/RBWMDF6Y/fulltext/images/1c644c2efeb8fd2726904f9cecaae52b9ffb608cd667bd8c931b011f16ef4bbf.jpg)  
Fig. 5. Mapping of the logical model and the physical model.

According to Walston and Felix's equation, system development duration is estimated at 38 months where as by the Putnam's equation, the development effort is estimated at 934 person-months, where $C_k$ is 11000 (an excellent environment) and the duration is 38 months. But the estimated duration is over the allowable limit. On the other hand, if we could develop the system within 20 months, the development effort is estimated at 12171 person-months, over the allowable limit.

![](/api/attachments/RBWMDF6Y/fulltext/images/55c92bd20dc9f3015d283b983e9727387cad1b948e6d71a6a3ead1625ce593f4.jpg)  
Fig. 6. Iterative system planning procedure.

Therefore, we divide the total production management system into some sub-systems by using this template model in order to solve a problem which has contradictory constraints. Fig. 7 shows the outline of our two-dimensional template for the steel manufacturing plant. In this figure, there are two hierarchical PDCA cycles. One is the management cycle at the level of entire Hirohata Works while the other is the management cycle at the plant level, corresponding to the 'Do' section at the Works level. The 'Do' section contains some PDCA cycles. Each box denotes the function of the manufacturing plant and each arrow denotes data flow. The results of applying this model are shown in Table 1.

By using the estimated number of source lines of sub-systems, the duration and development effort can be estimated by using the Walston and Felix and Putnam's equation, where $C_{\mathrm{k}}$ is 8000 (a good software development environment). Results are shown in Table 2.

Estimated number of source lines (in thousands) of the sub-system

<table><tr><td></td><td>Quality</td><td>Material</td><td>Order</td><td>Scheduling</td></tr><tr><td>Planning</td><td>111</td><td>22</td><td>0</td><td>0</td></tr><tr><td>Progress control</td><td>36</td><td>18</td><td>71</td><td>32</td></tr><tr><td>Operation control</td><td>131</td><td>10</td><td>25</td><td>44</td></tr><tr><td>Plant control</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

![](/api/attachments/RBWMDF6Y/fulltext/images/1a8dd6db57b209c8b9c64d1442ff45b30ef502274caaa17d96b5f36bf14cb44d.jpg)  
Fig. 7. Outline of the two-dimensional template for steel manufacturing plans.

Table 2  
Estimated duration (in months: upper) and the development effort (in person-months: lower) of the sub-systems

<table><tr><td></td><td>Quality</td><td>Material</td><td>Order</td><td>Scheduling</td></tr><tr><td rowspan="2">Planning</td><td>22.3</td><td>12.5</td><td>0</td><td>0</td></tr><tr><td>222</td><td>18</td><td></td><td></td></tr><tr><td rowspan="2">Progress control</td><td>13.2</td><td>11.6</td><td>19.0</td><td>14.3</td></tr><tr><td>62</td><td>13</td><td>111</td><td>32</td></tr><tr><td rowspan="2">Operation control</td><td>23.7</td><td>9.4</td><td>13.1</td><td>16.0</td></tr><tr><td>289</td><td>5</td><td>22</td><td>53</td></tr><tr><td>Plant control</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

According to our model, the duration is estimated to be 23.7 months (maximum estimated duration) and the total development effort to be 824 person-months.

In reality, this total production management system for one of the steel plant was developed in 22 months with 724 person-months and the number of source lines of the system was 585000.

## 5. Conclusions

This paper has proposed the use of templates for large-scale manufacturing management system planning. Through the use of these templates, we have accomplished comparatively high productivity results in planning steel manufacturing plant systems.

## Acknowledgements

We appreciate the useful suggestions by Prof. Norihisa Komoda in the Department of Information Systems Engineering, Osaka University in writing this paper.

## References

[1] T. DeMarco, Structured analysis and System Specification, Prentice-Hall, 1979.

[2] H. Furukawa, Systems integration of business systems, Nippon Steel Technical Report 51, 1991, pp. 53–59.

[3] M. Haga, Development technology for business information systems, Systems, Control And Information, 37(3) (1993) 160–167 (in Japanese).

[4] M. Ito, H. Furukawa, Current status and future trends of CIM in the Japanese steel industry, Journal of Systems Integration 2(1), 1992, pp. 91–114.

[5] I. Okinaka, Problems in the Production Management System of the Steel Industry – An Approach to the Problem of Multi-Purpose Decision-Making, in Preprint of $\ddagger$ Z-th International Conference on Multiple Criteria Decision Making – Toward Interactive and Intelligent Decision Support Systems, 2 (1986) 551–560.

[6] L. Putnam, A General Empirical Solution to the Macro Software Sizing and Estimating Problem, IEEE Trans. Software Engineering, SE-4(4) (1987) 345–361.

[7] C. Walston, C. Felix, A method for programming measurement and estimation, IBM Systems Journal 16(1), 1977, pp. 54–73.

![](/api/attachments/RBWMDF6Y/fulltext/images/c059fb2e3a8dbea741ade03d85fdaa2b26f0738ca1e7ee23f9a219023313c70c.jpg)  
Hiroshi Morihisa received his BE and ME degrees from Tokyo University in 1978 and 1980, respectively. Since 1980, he has been a system engineer at Nippon Steel Corporation and Nippon Steel Information and Communication Systems Inc. (ENICOM). Currently, he is also a Ph.D student at the Department of Information Systems Engineering, Faculty of Engineering, Osaka University. His research interest

is business information systems planning. He is a member of the Institute of Electrical Engineers in Japan and Information Processing Society of Japan.

![](/api/attachments/RBWMDF6Y/fulltext/images/87b5c5ede5b6de525084c48d05bd98b7c5229c6685aa8f6fe87feabc0cdc8173.jpg)

Ryota Oshita received his BE and ME degrees from Kobe University in 1981 and 1983, respectively. Since 1980, he has been engaged in planning and developing systems at Nippon Steel Corporation and Nippon Steel Information and Communication Systems Inc. (ENICOM). His research interest is business information systems planning. He is a member of Information Processing Society of Japan.

![](/api/attachments/RBWMDF6Y/fulltext/images/03265697377778e85b7498b13dbfedb3b32d0487a749800a4203dcb1e6b3770a.jpg)

for Management Information.

Hiroshi Furukawa received his BE from Tokyo Institute of Technology in 1971. Since 1971, he has been engaged in planning and developing systems at Nippon Steel Corporation and Nippon Steel Information and Communication Systems Inc. (ENICOM). He is now General Manager of System Division 1 in Osaka Regional Office. His research interest is business management system. He is a member of The Japan Society

![](/api/attachments/RBWMDF6Y/fulltext/images/42ba86a6eb7e0ec209d968c4ce9b0197f45bf2cf25fb0dacb1295bfe72d1e919.jpg)

Jun Kanda received his BE from Keio University in 1963. Since 1963, he has been engaged in the field of Industrial Engineering, Production Management and System Planning at Nippon Steel Corporation and Nippon Steel Information and Communication Systems Inc. (ENICOM). He had been a system consultant in a Steel Company in the USA. He is now the General Manager of Project Audit Department. His current

research interest is Project Management.
