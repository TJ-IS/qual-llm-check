---
otero_id: 17556
otero_key: "GM4P9VHW"
title: "Using multi-criteria analysis for tenant selection"
authors: "Chuk Yau; Tim Davis"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90007-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using multi-criteria analysis for tenant selection

Chuk Yau \*, Tim Davis

School of Computing and Information Technology, Griffith University, Nathan, Qld 4111, Australia

Tenant selection is an important strategic and operational problem for large property investment and management companies. This paper presents an evolutionary prototyping project developed in conjunction with a long term programme of establishing a property management information system for a known company. The project aims at developing a tenant selection decision support system (TSDSS) which employs a multi-criteria analysis technique as its evaluation tool. TSDSS also introduces a new method for determining the alternatives to be considered in the selection process, so that the values of some criteria, which represent the characteristics of the combinations of the chosen tenants, can be obtained. The alternative generation method has actually improved the practicality of using Multi-Criteria Analysis (MCA) techniques in some real life situations. However, from this development, some basic problems of using this technique have been revealed.

Keywords: Decision support systems; Multi-criteria analysis; Information system management; Property management

![](/api/attachments/GM4P9VHW/fulltext/images/8236eebfedc982da322288675aa2886e77cd2cf20650da5b82f98a750a50b6bf.jpg)

Dr. Chuk Yau is a Senior Lecturer in the School of Computing and Information Technology at Griffith University. He is a Member of the British Computer Society and the Operational Research Society and a Chartered Engineer. After completing a honours degree in computer science at London University in 1980, he worked as a software development consultant in Hong Kong and in 1985 he completed a Ph.D. at Lancaster University. Until 1991, he was teach-Science Department at the Chinese ing in the Computer Science Department at the Chinese University of Hong Kong while continuing as technical consultant to a number of large companies. His research interests include Project Management, Database Management, Decision Support Systems and Software Quality Assurance. He has published thirty papers in international journals and conferences.

Hong Kong being strategically located in South East Asia, has experienced a rapid economic growth over the past two decades. With there being more than 300,000 companies registered in a small city of only 400 square miles, the demand for commercial and industrial units is always at a premium. For this reason, the property business in Hong Kong is extremely active. Koon Wah, a large property investment and development company in Hong Kong, owns more than 1000 commercial units and has an expected annual business growth of more than 15%. The company's activities include developing commercial and industrial buildings on the properties it owns, selling developed units and renting and managing its own long term properties. The company, which is managed by a typical Chinese hierarchical structure with very strong family involvement, holds that its depends very much on the excellent leadership and the contribution of its loyal members. Although the company has operated in a healthy economic and management environment, the management is aware of the potential difficulties

## 1. Problems in property management

![](/api/attachments/GM4P9VHW/fulltext/images/c070a6562d7a69ea1f6c019917f160469fe3d027fad0da260e0408860617e95e.jpg)

Tim Davis is a Lecturer in the School of Computing and Information Technology at Griffith University. He is a Member of the Association of Computing Machinery, the Operational Research Society and the United Kingdom System Society. After completing his Master of Science degree at Florida Institute of Technology in 1985, he worked as an operations research and systems analyst for the Army's Deputy Chief of Staff for Personnel in Washington, D.C. Following his retirement from the United States Army in 1989, he took up his present position at Griffith University where he is also providing technical consultation to various public and private concerns. His research interests include Systems Theory, Systems Analysis and Design, Information Systems, Decision Support Systems and Systems Modelling and Simulation.

associated with its anticipated expansion. Some of the problems which have been recognised are:

(a) that the ever increasing volume and variety of data cause difficulties in the efficient and effective processing and maintenance by manual means. Figure 1 shows the complexity of the database (for notation see [11]);

(b) that timely and complete information is not always available to support management decisions, making objective identification and evaluation of opportunities difficult;

(c) that due to the nature of the business, the company has to deal with different types of individuals with varied backgrounds increasing the risk in the selection of adequate partners, investors and customers for the various projects; and

![](/api/attachments/GM4P9VHW/fulltext/images/45999209f51f44f35b976fb937af51efc4a34a41a30ea95920fbab529607aba1.jpg)  
Fig. 1. Data model of property management.

(d) that the changes in real estate regulations and law affect daily operations and require special attention at various levels of management.

Koon Wah recognised that the above problems had the potential to reduce the competitive nature of the company in the fast moving environment. In order to maintain the company's excellent performance, the top level of management decided to develop a property management information system with the objective of improving its daily operations as well as aiding the management decision processes.

## 2. Property management information system

In order to provide comprehensive support to all levels of the business, the Property Management Information System (PMIS) has to integrate the functions of Data Processing, Management Information Reporting and Decision Support. This project was planned to be completed in three years and was divided into three phases. The conceptual framework of Koon Wah's computerisation programme is shown in Figure 2.

The first phase of the project aimed at developing the core of the system through automation of the daily operations and management information reporting system. This phase was regarded as the initialisation stage $[4,7]$ of the overall project and as some staff already had experience in using micro-computers, it was felt that adaptation to this aspect of the proposed PMIS would occur in a relatively short period of time. This phase of automation was completed in 18 months and included the following major functions:

![](/api/attachments/GM4P9VHW/fulltext/images/6921d273a04258524117ffc3dd71db4e14cea92dc75cc6343a08462e4946e0a7.jpg)  
Fig. 2. The framework of computerisation.

(a) maintenance of information of associate companies, buildings, units and tenants;

(b) maintenance of the accounts of associate companies with the ability to generate financial reports;

(c) production of bills, reminders, debit notes and special statements to customers;

(d) facilities for tracking the status of tenancy agreements; and

(e) generation of managerial reports.

Subsequent analysis revealed that using the automated functions of PMIS actually reduced the clerical work load and increased the efficiency and accuracy in preparing monthly bills, reminders, statement of accounts, etc. The timeliness of management reports allowed managers to assess their business position at any point in time and provided the ability to identify potential problems early in their business activities.

## 3. Tenant selection decision support system (TSDSS)

With PMIS having developed support for the daily operations and regular management activities, the second phase, considered as a contagion stage $[4]$ , aims at establishing a generic platform for developing decision support systems for various types of business problems. The strategy employed in this phase was to develop a prototype DSS for a selected problem. With the knowledge and experience that was obtained from this process, it was felt that a good foundation would exist for further DSS development in the third phase.

From among the various business decision problems which included the determination of the pricing policy for sales and rental, and the selection of investment and development projects, the selection of tenants for new rental units was chosen for development. This choice was justified on the basis that:

(a) tenant selection is an independent operational management problem which had minimal effect on other functions within the organisation;

(b) the criteria for selecting tenants would be relatively easy to formulate;

(c) the required information would be readily accessible when required; and

(d) the performance of the system would be easier to measure.

During the one year process of developing the prototype system for tenant selection, a general decision model was developed for future usage. This paper presents the overall design of the prototype system and the concepts for using the more generic MCA model.

The major function of TSDSS is to evaluate the various combinations of tenants (alternatives) based on an established set of attributes (criteria). TSDSS has adopted an interactive MCA model which is regarded as a quantitative tool for evaluating alternatives that are characterised by multiple and conflicting criteria. TSDSS comprises four subsystems: the Criteria Identification Subsystem, the Utility Profile Construction Subsystem, the Alternative Generation Subsystem and the Evaluation Subsystem.

## 3.1. The tenant selection problem

Before discussing the subsystems further, it is essential to understand the problem of tenant selection which is an intricate task for property managers. This is particularly true for commercial and industrial buildings where tenants have generally been selected on a first-come, first-serve basis while other factors such as the nature of the business and goodwill also need to be considered before a final decision is made.

In the case study being presented, the problem is concerned with a newly constructed, unoccupied shopping centre for which the property management company will solicit proposals from potential tenants. Each of the proposals, to be submitted by a specified date, will be a standard application form consisting of the following types of information:

(a) Company directors: This is felt to be potentially useful in assessing the company's reliability.

(b) Business nature: Koon Wah attempts to maintain a reasonable

(d) Proposed units:

variety of business types for its shopping centre.

(c) Previous address:

(e) Proposed rental:

This is a source for collecting information on the potential tenant's past performance.

This provides information for unit allocation and occupancy rate consideration.

Although price lists are available before the proposals are collected, the potential tenants may propose prices which are lower than those listed. For example, a famous department store in Hong Kong always offers a very low rental at approximately 40% of the market rate for a large number of units in its selected location.

![](/api/attachments/GM4P9VHW/fulltext/images/77e29cadb576e0a3175c3e8cb43066754e6926b33d9503d441585c8510646559.jpg)  
Fig. 3. TSDSS operation process.

(f) Proposed length: Length of tenancy may be varied depending on the nature of the business.

Following the closing date, all the submitted proposals are evaluated on the basis of some pre-determined criteria with the overall objectives of the selection process being to maximise the rental income and obtain good tenants. Since each prospective tenant has his own background and requirements, the property manager must consider relevant tenant information such as past history, occupation, and pollution level acquired from various sources, and then evaluates them accordingly.

As might be expected, a large shopping centre with many units will normally attract a large number of prospective tenants. Although the property manager will have spent a significant period of time processing the enormous amount of data, the outcome may not result in the most satisfactory selections as the process will have involved a number of criteria on which the potential tenants would most likely have been weighed differently. Moreover, some criteria utilised in the process may not have been independent from other criteria resulting in confusion in the evaluation process. Taking these issues into account, TSDSS was designed to incorporate a methodology for guiding the selection process. The selection model of TSDSS is based on a MCA technique which has been successfully applied in many different areas. [2,5,6,9]

This project also suggests a new approach for determining the alternatives to be considered in the selection process. Traditionally, the alternatives of a MCA model would be the objects that the criteria are directly applied against. However, in this scenario we have to consider a combination of tenants rather than an individual tenant as an alternative. This allows for the determination of the percentage of occupancy and rental income for each of the possible combination of tenants. However, this approach introduces a combinatorial problem which significantly increases the number of alternatives generated. The large number of combinations to be evaluated may make the use of the MCA model impossible.

To resolve this problem, a special alternative generating system has been developed and will be presented in a later section of this paper. The methodology for tenant selection is depicted in Figure 3.

## 3.2. Criteria identification subsystem

Before proceeding, it is important to define some terms:

(a) Alternative: a possible solution to the decision problem;

(b) Criteria: a set of quantifiable characteristics that are inherent to all alternatives being considered by a decision maker so as to evaluate the quality of a solution; and

(c) Utility Function: a mathematical model constructed by certain mathematical hypothesis as well as information supplied by the decision maker [2]; usually, it integrates the relative preferences within the criteria set and works as an evaluation tool for the best solution

These terms can also be defined by the following mathematical notions which have been adopted in the paper.

Let $X_{i}$ be the domain of the i-th criterion,

$x_{i}$ be a particular value of $X_{i}$ ,

$x_{i}^{*}$ be the best value of $X_{i}$ ,

$x_{i}^{\circ}$ be the worst value of $X_{i}$ ,

$x_{\Omega i}$ be a particular value of $X_{i}$ of combination of tenants $\Omega$ ,

x be a specific combination of tenants having a particular value on each $X_{i}$ , denoted as $(x_{1}, x_{2}, \ldots, x_{n})$

X be the Cartesian product of $X_{i}$ 's, denoted as $(X_{1} \times X_{2} \times \ldots \times X_{n})$ ,

$\mathbf{X}_{i}$ be the Cartesian product of $X_{k}$ 's where $1 \leqslant k \leqslant n$ and $k \neq i$ , denoted as $(X_{1} \times X_{2} \times \ldots \times X_{i-1} \times X_{i+1} \times \ldots \times X_{n})$ ,

$\mathbf{X}_{\hat{i}\hat{j}}$ be the Cartesian product of $X_{k}$ 's where $1 \leqslant k \leqslant n$ and $k \neq i \neq j$ , denoted as $(X_{I} \times \ldots \times X_{i-1} \times X_{i+1} \times \ldots \times X_{j-1} \times X_{j+1} \times \ldots \times X_{n})$ .

Table 1

<table><tr><td>Criteria</td><td>Worst level</td><td>Best level</td></tr><tr><td>Percentage of Occupancy (OC)</td><td>60%</td><td>100%</td></tr><tr><td>Total Annual Income in Millions HK$ (TI)</td><td>16</td><td>24</td></tr><tr><td>Average Reliability (AR)</td><td>3</td><td>10</td></tr></table>

The first step of using TSDSS is to define a set of selection criteria. The criteria are then given a scale that will subsequently be used to determine the user's utility value between 0 and 1. Thus, the worst and best level of each criterion must be determined by the property manager. For example, in this case the property manager may decide to conduct the selection on the basis of three criteria with the worst and best levels as indicated in Table 1.

The MCA model is built on the concept of preference theory. When several criteria in a decision making process are considered, the decision maker may, in fact, conceive a preference order among these criteria. Nevertheless, the order may not be explicitly established in his mind, but may rather be clarified only when a preference under certain specific conditions has been made and the subsequent deductions have been derived. Preferential Independence (PI) and Utility Independence (UI) are the two fundamental assumptions $[2,8]$ for building an MCA model.

The ultimate gist of PI and UI is to verify the conditions that whenever a criterion or some criteria are considered, the decision maker can pay no attention to the effects on the considered criteria brought about by the remaining criteria. Following these concepts, the decision maker can consequently deduce the relative preference among the considered criteria or utility value of a particular criterion. The Utility Theory has been discussed in detail by many researchers $[1,2,8,9,10]$ . However, examples of verifying the Preferential Independence and Utility Independence in the context of tenant selection are given below.

## 3.2.1. Preferential independence

Presuming that there are a number of combinations of tenants which only differ from one another in the measures of two criteria.

IF the choice for the best combination remains unchanged even when the values of the remaining criteria are set to any other values, as long as they are the same for all the combinations,

THEN the two criteria are said to be Preferential Independent of the remaining criteria.

For instance, the selection of the best combination of tenants is based on three criteria, namely the percentage of occupancy (OC), the total annual income in millions of Hong Kong dollars (TI), and the average reliability (AR). The combinations A and B are the two alternatives in the selection process and their corresponding values with the set of criteria (OC, TI, AR) are (90%, 20, 8.3) and (95%, 18, 8.3), respectively. According to these measures, we have assumed that the property manager prefers combination A even knowing that these two combinations may differ from each other in OC and TI. In order to investigate the relationship between the average reliability and the other criteria, the value of AR is now altered to 9, or any other value as far as they are the same for both combinations. Now, suppose the property manager still prefers combination A, OC and TI can then be regarded to be preferential independent of AR in this case.

## 3.2.2. Utility independence

Suppose there are several combinations of tenants which only differ from one another in a single criterion, and the measure corresponding to that criterion is uncertain and involves a probability distribution.

IF the conditional preferences for lotteries on the considered criterion remains unchanged even when the values of the remaining criteria are set to any values, as long as they are the same for all combinations of tenants,

THEN that considered criterion is said to be Utility Independent of the remaining criteria.

For the example in the previous section, suppose combination A has a 50-50 chance of getting either (70%,20,8.3) or (95%,20,8.3), and combination B also has a 50-50 chance of getting either (75%,20,8.3) or (85%,20,8.3). Again, if the property manager considers only the criterion on percentage of occupancy when all the values of other criteria remain the same for both combinations. In this case, we again assume that the project manager prefers combination A. Now, suppose the measures of TI and AR are changed to 22 and 9 respectively for both combinations. Based on the condition that the probabilities of the measures remain unchanged, should the property manager still prefer combination A, then the percentage of occupancy can be claimed as Utility Independent of the remaining criteria.

## 3.3. Utility profile construction subsystem

To construct a utility profile for the property manager, the first step is to obtain his utility functions for the criteria. And then the scaling constants of the criteria in the multiplicative model must be assessed.

## 3.3.1. Determining the utility functions

Since the upper and lower bounds of the utility scale have been fixed at 1 and 0, respectively, all marginal utility functions are presumed either quadratic or linear. A third point on the utility curve can be determined by inquiring the property manager's preference for two choices, with one in a lottery and the other in a certainty situation. For example, the property manager is given a lottery of a half chance of full occupancy and a half chance of 70% occupancy, and another certain alternative of 80% occupancy. If the manager chooses the former, the system will shift the latter to a more favourable condition, say 85%, and will start to inquiry again. This process will be continued until the manager is indifferent to the two choices. At the end, the value of OC% of the choice will be given a utility value of 0.5 which is in the middle of the best and the worst levels. Having 3 points of a quadratic curve, the system is able to generate the manager's utility function of the percentage of occupancy which will be stored as part of the manager's utility profile. This procedure will be repeated until all utility functions have been obtained.

## 3.3.2. Assessing the scaling constants

Scaling constants are the relative weights of the criteria. The assessment is divided into two steps. The first step is to determine the weight of the first criterion, $k_{1}$ , by a probabilistic approach, and then based on $k_{1}$ , other $k_{i}$ 's can be deduced by applying another approach called trade-off resolution.

Assume that we consider three criteria to construct the utility profile and each of the corresponding utility functions has been completed in earlier stages. Primarily, a combination A, denoted as $(x_{A1}^{*}, x_{A2}^{0}, x_{A3}^{0})$ , is offered in which the percentage of occupancy is at the best level while the other criteria are at their worst levels. Then another combination B is offered and it is a lottery having a probability of p of getting all outcomes at their corresponding best levels and a probability of $(1-p)$ of getting all worst outcomes.

The system will acquire the value p from the property manager such that he will be indifferent to the two choices. Once p is found, $k_{1}$ can be determined.

Utility value of combination A

= Utility value of combination B

$$
\begin{array}{r l} & u (x _ {\mathrm{A1}} ^ {*}, x _ {\mathrm{A2}} ^ {\circ}, x _ {\mathrm{A3}} ^ {\circ}) = p \times u (x _ {\mathrm{B1}} ^ {*}, x _ {\mathrm{B2}} ^ {*}, x _ {\mathrm{B3}} ^ {*}) + (1 - p) \\ & \qquad \times u (x _ {\mathrm{B1}} ^ {\circ}, x _ {\mathrm{B2}} ^ {\circ}, x _ {\mathrm{B3}} ^ {\circ}) \\ & k _ {1} \times 1 + k _ {2} \times 0 + k _ {3} \times 0 = p \times 1 + (1 - p) \times 0 \\ & k _ {1} = p \end{array}
$$

Upon getting $k_{1}$ , TSDSS can proceed to assess $k_{2}$ which is the relative weight of total income by applying the trade-off resolution approach. The property manager is required to select two specific outcomes $x_{A1}$ and $x_{B2}$ , from the first and second criteria, respectively, such that he is indifferent to the combination $A = (x_{A1}, x_{A2}^{\circ}, x_{A3}^{\circ})$ and combination $B = (x_{B1}^{\circ}, x_{B2}, x_{B3}^{\circ})$ . In TSDSS, either $x_{Ai}$ or $x_{Bi}$ is fixed to a reference value so that the property manager may find it flexible for selecting the other outcome. For example, suppose the value of $x_{A1}$ is fixed at 80%, if the property manager is indifferent to combination $A = (80\%, 16, 3)$ and combination $B = (60\%, 20, 3)$ , then the value of $x_{B2}$ is 20. If it is really impossible to compare any 2 combinations, the system allows certain changes to be made to the reference value of the first attribute, i.e. lowering or raising the value of $x_{A1}$ in this case, so as to provide the property manager with new guidance for making the decision. From this process, the system obtains:

Utility value of combination A

= Utility value of combination B

$$
\begin{array}{l} {u (x _ {\mathrm{A1}}, x _ {2} ^ {\circ}, x _ {\mathrm{A3}} ^ {\circ}) = u (x _ {\mathrm{B1}} ^ {\circ}, x _ {\mathrm{B2}}, x _ {\mathrm{B3}} ^ {\circ})} \\ {k _ {1} \times u _ {1} (x _ {\mathrm{A1}}) = k _ {2} \times u _ {2} (x _ {\mathrm{B2}})} \\ {k _ {2} = k _ {1} \times u _ {1} (x _ {1} ^ {\prime}) / u _ {2} (x _ {2} ^ {\prime \prime})} \end{array}
$$

$k_{1}$ is a scalar constant between 0 and 1 which represents a weight of criterion i. As $k_{1}$ and all $u_{i}$ 's are determined, $k_{2}$ can be calculated. Similarly, repeating this process on all other criteria, all $k_{i}$ 's can be obtained.

The utility model adopted in TSDSS is known as the multiplicative function denoted as $u(x)$ which can be represented as follows:

$$
1 + k \cdot u (x) = \prod_ {i = 1} ^ {n} \left(1 + k \cdot k _ {i} \cdot u _ {i} (x _ {i})\right).
$$

In the multiplicative utility model, the constant k is interpreted as the synergistic effect and k > -1. It can be obtained by expanding the equation into polynomial of k [1,8]. The system has a module which is based on the Newton-Horner Method with deflation for finding the value of k.

Finally, all elements of the utility function model are stored in the property manager's utility profile for further use. The property manager's utility profile includes the 3 points of quadratic utility functions of the selection criteria and the weights of the criteria. An example of utility profile is shown in Table 2.

## 3.4. Alternative generation subsystem

Some important criteria, such as the percentage of occupancy and the total income, can not be assessed if tenants were selected independently. Using TSDSS, the property manager has to select tenants on a combinatorial basis. However, if the combinations of tenants were not generated with care, the total number of alternatives would be equal to $2^{n}-1$ , where n is number of tenants. If there are 30 potential tenants, the number of combinations would be 1,073,741,823. Obviously, it would be impractical to carry out a selection process even when a computer system is used. Thus, some rules must be introduced to delete unwanted combinations. The following two rules are adopted in TSDSS and the effect of applying these rules is presented in this section.

Table 2

<table><tr><td>Criteria</td><td>Worst level utility = 0</td><td>Best level utility = 1</td><td>Assessed level for utility = 0.5</td><td>Relative weight  $k_i$ </td></tr><tr><td>Percentage of Occupancy</td><td>60%</td><td>100%</td><td>80%</td><td>0.375</td></tr><tr><td>Total Annual Income</td><td>16</td><td>24</td><td>18</td><td>0.893</td></tr><tr><td>Average Reliability</td><td>3</td><td>10</td><td>6</td><td>0.469</td></tr></table>

The Synergistic effect, k = -0.799.

Table 3

<table><tr><td>Combination</td><td>Deleted by Rule 1</td><td>Deleted by Rule 2</td></tr><tr><td>A</td><td></td><td>Yes</td></tr><tr><td>B</td><td></td><td>Yes</td></tr><tr><td>C</td><td></td><td>Yes</td></tr><tr><td>D</td><td></td><td>Yes</td></tr><tr><td>AB</td><td></td><td>Yes</td></tr><tr><td>AC</td><td></td><td>Yes</td></tr><tr><td>AD</td><td></td><td>Yes</td></tr><tr><td>BC</td><td>Yes</td><td></td></tr><tr><td>BD</td><td></td><td>Yes</td></tr><tr><td>CD</td><td></td><td>Yes</td></tr><tr><td>ABC</td><td>Yes</td><td></td></tr><tr><td>ABD</td><td></td><td></td></tr><tr><td>ACD</td><td></td><td></td></tr><tr><td>BCD</td><td>Yes</td><td></td></tr><tr><td>ABCD</td><td>Yes</td><td></td></tr></table>

Rule 1 If there are some tenants whose proposed units are partially or wholly in common, they will not be included in the same combination. Therefore, any combination which contains conflicting tenants must be deleted.

Rule 2 If any combination is a subset of any other combination(s), the former combination must be deleted

For example, if we have 4 tenants identified as A, B, C and D; using the combinatorial formula $_{4}C_{1} + _{4}C_{2} + _{4}C_{3} + _{4}C_{4}$ , the number of possible combinations is set to 15. The possible combinations are indicated in the Combination column of Table 3.

Assuming that there are 10 units available for rental and that Tenant A wants units 1, 2 and 3, Tenant B wants units 4, 5 and 6, Tenant C wants units 6 and 7 and Tenant D wants units 8, 9 and 10, then a conflict exists between Tenants B and C.

Applying Rule 1 and deleting all combinations containing the conflicting tenants, 4 of the combinations will be deleted as indicated in the Rule 1 column of Table 3 with the remaining number of combinations being 11. Therefore, in applying Rule 1, the number of combinations becomes

$$
(2 ^ {n} - 1) + \sum_ {r = 1} ^ {m} (- 1) ^ {r} \binom {m} {r} \cdot 2 ^ {n - 2 r}
$$

Table 4

<table><tr><td>Combinations</td><td>n = 10</td><td>n = 20</td><td>n = 30</td></tr><tr><td>no conflict</td><td>1,023</td><td>1,048,575</td><td>1,073,741,823</td></tr><tr><td>m = 1</td><td>767</td><td>786,431</td><td>805,306,637</td></tr><tr><td>m = 2</td><td>575</td><td>589,823</td><td>603,379,775</td></tr><tr><td>m = 3</td><td>431</td><td>442,367</td><td>452,984,831</td></tr><tr><td>m = 4</td><td>323</td><td>331,775</td><td>333,738,623</td></tr><tr><td>m = 10</td><td>n / a</td><td>59,048</td><td>60,466,175</td></tr></table>

where n = number of tenants, m = number of conflicting tenants - 1.

The above reduction has been proved by Mathematical Induction. Table 4 further demonstrates the effect of applying the first rule in the alternative generation process.

Applying Rule 2 and deleting all combinations which are a subset of another combination, 9 additional combinations are deleted as indicted in the Rule 2 column of Table 3 leaving only 2 combinations to be considered as alternatives.

However, unlike Rule 1, the effect of Rule 2 is difficult to express mathematically as the occurrence of a particular subset is dependent on the  
Table 5

<table><tr><td></td><td># of units</td><td>Ten-ants</td><td>Original set size</td><td>Deleted</td><td>Remain-ing</td><td>% of original</td></tr><tr><td>Case 1</td><td>50</td><td>30</td><td>1,930</td><td>1,645</td><td>285</td><td>14.0%</td></tr><tr><td>Case 2</td><td>50</td><td>30</td><td>4,894</td><td>4,295</td><td>599</td><td>12.0%</td></tr><tr><td>Case 3</td><td>50</td><td>30</td><td>9,811</td><td>8,842</td><td>969</td><td>9.9%</td></tr><tr><td>Case 4</td><td>50</td><td>100</td><td>1,952</td><td>1,156</td><td>796</td><td>40.7%</td></tr><tr><td>Case 5</td><td>50</td><td>100</td><td>2,905</td><td>1,836</td><td>1,069</td><td>36.0%</td></tr></table>

actual requirements of the tenants in a specific application of the model and cannot be assumed by mathematical notions. Therefore, randomly generated cases have been used to illustrate some statistics for the purpose of evaluation in Table 5.

In order to observe the overall performance of applying the two rules, a case which has 30 potential tenants and 15 units was generated. The number of generated alternatives after applying Rule 1 and 2 are as shown in Table 6.

Table 6

<table><tr><td>Theoretical Set Size</td><td>After Rule 1</td><td>After Rule 2</td><td>% Remaining</td></tr><tr><td>1,073,741,823</td><td>3,336</td><td>152</td><td> $1.4 * 10^{-5}\%$ </td></tr></table>

<table><tr><td>Criteria</td><td>Combination 1</td><td>Combination 2</td><td>Combination 3</td></tr><tr><td>Percentage of Occupancy</td><td>88.27%</td><td>93.40%</td><td>82.5%</td></tr><tr><td>Total Annual Income</td><td>22.32</td><td>21.5</td><td>20.3</td></tr><tr><td>Average Reliability</td><td>7.2</td><td>8.32</td><td>9.2</td></tr><tr><td>Overall Score</td><td>0.975</td><td>0.968</td><td>0.93</td></tr></table>

<table><tr><td></td><td>Units</td><td>Tenants</td><td>Units</td><td>Tenants</td><td>Units</td><td>Tenants</td></tr><tr><td rowspan="20">Assignments</td><td>1</td><td>Starlink</td><td>1</td><td>Starlink</td><td>1</td><td>PDI</td></tr><tr><td>2</td><td>Starlink</td><td>2</td><td>Starlink</td><td>2</td><td>PDI</td></tr><tr><td>3</td><td>Starlink</td><td>3</td><td>Starlink</td><td>3</td><td>*</td></tr><tr><td>4</td><td>Champ Year</td><td>4</td><td>Champ Year</td><td>4</td><td>Champ Year</td></tr><tr><td>5</td><td>Crossland</td><td>5</td><td>Tempora</td><td>5</td><td>Tempora</td></tr><tr><td>6</td><td>*</td><td>6</td><td>Tempora</td><td>6</td><td>Tempora</td></tr><tr><td>7</td><td>Far East</td><td>7</td><td>Tempora</td><td>7</td><td>Tempora</td></tr><tr><td>8</td><td>Far East</td><td>8</td><td>Tempora</td><td>8</td><td>Tempora</td></tr><tr><td>9</td><td>Sun May</td><td>9</td><td>Tempora</td><td>9</td><td>Tempora</td></tr><tr><td>10</td><td>*</td><td>10</td><td>*</td><td>10</td><td>YASA</td></tr><tr><td>11</td><td>IIQ</td><td>11</td><td>IIQ</td><td>11</td><td>YASA</td></tr><tr><td>12</td><td>Dragon</td><td>12</td><td>Dragon</td><td>12</td><td>YASA</td></tr><tr><td>13</td><td>DAS-100</td><td>13</td><td>DAS-100</td><td>13</td><td>YASA</td></tr><tr><td>14</td><td>*</td><td>14</td><td>*</td><td>14</td><td>YASA</td></tr><tr><td>15</td><td>Formative</td><td>15</td><td>Formative</td><td>15</td><td>YASA</td></tr><tr><td>16</td><td>Four Sea</td><td>16</td><td>Four Sea</td><td>16</td><td>YASA</td></tr><tr><td>17</td><td>Four Sea</td><td>17</td><td>Four Sea</td><td>17</td><td>*</td></tr><tr><td>18</td><td>Four Sea</td><td>18</td><td>Four Sea</td><td>18</td><td>Hop Fat</td></tr><tr><td>19</td><td>Four Sea</td><td>19</td><td>Four Sea</td><td>19</td><td>Hop Fat</td></tr><tr><td>20</td><td>Four Sea</td><td>20</td><td>Four Sea</td><td>20</td><td>*</td></tr></table>

\* Unassigned Unit  
Fig. 4. Example report of some ranked combinations of tenants.

From this example, the result is promising as the two rules reduce a lot of original combinations so that the number of remaining combinations can be handled by TSDSS more efficiently.

## 3.5. Evaluation system

The evaluation system is a module which brings all relevant data together for final manipulation. This system will first calculate the values of the criteria of all short listed alternatives. In this application, the reliability level of an individual tenant is assessed by the manager based on his experience. For some tenants who are now renting other units of the company, the property manager may determine the reliability level according to the existing records stored in PMIS. Some good existing tenants can be given reliability level up to 10. Since the unassigned units can also be rented at a later time, the total annual income must include the possible income from the unassigned units with a discount factor to cover the potential losses. After the first round of unit assignment, the company will negotiate with some potential tenants for the rental of unassigned units. Normally tenants of the second round assignment will bargain for lower rentals for the units which may not satisfy all their requirements. The company always offers 5% discounts to some genuine tenants. Therefore the discount factor for the total income is normally set as 0.95. The criteria can be calculated as follows:

$$
\mathrm{OC} = \text { TOACT } / \text { TAA }
$$

where TOACT = Total Occupied Area of the Combination of Tenants, TAA = Total Available Area

$$
\mathrm{TI} = \mathrm{TRC} + (\mathrm{DF} \times \mathrm{PIUU})
$$

where TRC = Total Revenue of the Combination, DF = Discount Factor, PIUU = Projected Income of the Unassigned Units

$$
\mathrm{AR} = \sum \mathrm{R} _ {\mathrm{i}} \times \mathrm{OA} _ {\mathrm{i}} / \text { TOACT }
$$

where $R_{i} = \text{Reliability of Tenant}_{i}$ assessed by the manager, $AO_{i} = Occupied Area of Tenant_{i}$ .

The property manager's utility profile is also incorporated into the evaluation system. By applying the multiplicative model, an order of preference will be generated according to the aggregated utility values of the short listed alternatives. The information in Figure 4 is an example report of some ordered combinations of tenants. Normally, the management will re-consider some top-listed combinations by incorporating some intangible factors, such as the overall impression on the mixture of different types of business. Therefore, the generated reports are not regarded as the final decision but they will be able to support the property manager and other relevant staff to make the final decision.

## 4. Conclusion

The development of TSDSS is part of a pilot study of a long term computerisation programme. One of the most significant features of TSDSS is the alternative generation subsystem. Whereas traditionally alternatives have been inputs to the modelling process, this subsystem generates and subsequently selects the “most appropriate” alternatives through the application of two reduction rules. This significantly reduces the combinatorial problem generated by the identification of alternatives which are in themselves, combinations of options with identified attributes, thus improving the practicality of using Multi-Criteria Analysis. As well, the application of the rules in the alternative generation system will prevent the inclusion of alternatives with conflicting tenants which is a common problem in the manual selection process.

In this prototyping phase, the Multi-Criteria Analysis technique has been found effective for the tenant selection problem and is expected to be useful for other management decision problems which involve tradeoffs between some conflicting attributes. Since TSDSS is designed in a modular form, it provides for reusability of code for other DSS development. Moreover, the knowledge that the staff gained from this study will be valuable for tackling some strategic problems that require multiple modelling techniques $[6]$ .

An important issue to be mentioned resulting from experience with the TSDSS prototype is that of designing the user and system interfaces. It is recognised that the average decision maker has the need of a system that requires limited or no computing expertise. The current TSDSS prototype requires a level of familiarity inconsistent with the desired “ease of use”. This will require a redesign of the user interface and greater attention in the future design of other DSS systems. At the moment, TSDSS is a stand alone system which captures required data from the user without an automated connection to the main PMIS. Therefore, the user has to access the information of existing clients from a different computer system platform. Further development is needed to improve the system interfaces between PMIS and TSDSS so that data accessibility is enhanced.

With the development of the TSDSS prototype, some basic problems of applying Multi-Criteria Analysis techniques have been observed. The first difficulty is concerned with the utility assessment procedure, in which the property manager is asked to compare choices which are artificially generated by the computer. The measures of the choices presented may contain extreme values which would be rare in real life situations. Recognising that most staff in this type of decision-making capacity have a limited concept of probability or seldom think in such terms, the extreme values and the probability presented have the potential to make them feel the assessment procedure unrealistic. In the opinions of the users, it would be a long term benefit to develop a Utility Tutoring System which will be able to provide a number of examples and interactive training to staff to get familiar with the utility concept.

The last problem identified concerns the group decision-making practice which is commonly used in contemporary organisations. The users have indicated that the TSDSS prototype will need to be modified to handle utility aggregation for a group of decision makers.

## References

[1] Keeney, R.L., (1974), Multiplicative Utility Functions, Operations Research, 1974, P.22–34.

[2] Keeney, R.L. and Raiffa, H., (1976), Decisions with Multiple Objectives: Preference and Value Tradeoffs, John Wiley.

[3] Keeney, R.L. (1977), The Art of Assessing Multi-attribute Utility Functions, Organisational Behaviour and Human Performance, No. 19, P. 267–310.

[4] Nolan, R. (1979), Managing the Crisis in Data Processing, Harvard Business Review, March-April 1979, P. 115–126.

[5] Sage, A (1981), Behavioural and Organisational Considerations in Design of Information Systems and Process for Planning and Design Decision Support, IEEE Transactions on Systems, Man and Cybernetics SMC-11, No. 9, 1981, P. 640–678.

[6] Mich, R.P. and Burns, J.R., (1983), Conceptual Design of Decision Support Systems Utilizing Management Science Models, IEEE Transactions on Systems, Man Cybernetics. Vol. SMC-13, No. 4, P. 549–557.

[7] King, J.L. and Kraemer, K.L. (1984), Evolution of Organisational Information Systems: An Assessment of Nolan's Stage Model., CACM, May 1984, P. 466–475.

[8] Vira Changkong and Yacor, Y. Haimes, (1983), Multi-objective Decision Making: Theory and Methodology, North-Holland.

[9] Korhonen, P. and Wallenius, J., (1986), Some Theory and an Approach to Solving Sequential Multiple-Criteria Decision Problems, Journal of Operational Research Society, 1986, P. 501–508.

[10] Korhonen, P., Moskowitz, H. and Wallenius, J., (1986), A Progressive Algorithm for Modelling and Solving Multiple-Criteria Decision Problems, Operations Research, Vol. 34, No. 5, 1986, P. 724–731.

[11] Ashworth, C and Goodland, M, (1990), SSADM: A Practical Approach, McGraw-Hill.
