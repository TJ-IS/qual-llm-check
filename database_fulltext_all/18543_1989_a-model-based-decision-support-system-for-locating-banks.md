---
otero_id: 18543
otero_key: "G4JVJYV5"
title: "A model-based decision support system for locating banks"
authors: "Hokey Min"
year: "1989"
journal: "Information & Management"
doi: "10.1016/0378-7206(89)90044-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Model-Based Decision Support System for Locating Banks

Hokey Min

College of Business Administration, University of New Orleans, New Orleans, LA 70148, USA

The proper location of branch-banks is critical to the success of the banking business. The major ingredients for deciding where to locate branch-banks are: growth rates of deposits and loans; degree of competition; easy accessibility, and operating costs of potential sites. These are often highly sensitive to socio-economic, demographic, and behavioral factors that are ill-defined and fuzzy in nature. Accordingly, the traditional normative approach alone cannot analyze the excessive location-related data associated with the external factors and cannot appropriately evaluate behavioral criteria for branch-bank sites. In order to overcome these difficulties, this paper develops an interactive fuzzy goal programming model embedded within a locational decision support system for branch-banks. To demonstrate the practicality of the proposed model-based DSS, it has been applied to establish real-world-like location scenarios for commercial branch-banks in Columbus, Ohio.

Keywords: Retail location, Fuzzy multicriteria decision making, Decision support systems.

![](/api/attachments/G4JVJYV5/fulltext/images/dbf9e1c48455b419f3feb19d6c75bf11dd575996d6744a5bee61c532b4e2e39e.jpg)

Hokey Min is an Assistant Professor of Production/Operations Management in the Department of Management at the University of New Orleans. In September of 1989, he will join the faculty of Operations Management at the Northwestern University. He received his M.B.A. (Production Management) degree from Yonsei University, Seoul, Korea and M.S.B.A. (Management Science) from the University of South Carolina, Columbia, and obtained the M.A. and Ph.D. de-

grees in Management Science from the Ohio State University, Columbus. His research interests are in Logistics, Multiple Criteria Decision Making (MCDM), Decision Support System, Group Decision Making, and Purchasing and Materials Management. His research works appeared in professional journals such as Euro. J. Opl. Res., Socio-Econ. Plan. Sci., OMEGA, Computers & Opns Res., and Transportation Research A.

## 1. Introduction

In order to maintain the continued growth of banking organizations, a bank manager must determine the best location of new branch-banks. As most banking institutions in the USA provide banking services to their customers through franchised branch-bank networks, the key to successful banking operations depends mainly on the branch-bank business potential, which is greatly influenced by the site selection of branch-banks.

This selection plays an important role in the bank's profitability in at least three ways. First, a new branch-bank, located more conveniently than existing offices, may be sufficient reason for another branch's clients to switch banks (Kramer [13]). As such, a more convenient location may attract a large number of clients, thereby providing a large influx of deposits and increasing bank loans. Second, the proper location of branch offices may prevent overlapped banking services within the trading area of potential competitors, thereby increasing future market share. Third, a good decision may ease financial pressure on the banking operation, because the proper location of a new branch-bank may reduce capital investment costs, such as leasing costs or property taxes.

Given the significance of these decisions, very little effort has been directed toward this area. The paucity of existing studies has generally forced bank managers to deal with bank location problems in an intuitive manner. Consequently, they have lost opportunities to improve efficiency and effectiveness in banking operations.

In this respect, a better decision-making tool is needed to help bank managers investigate possible locations that are influenced by complex, ill-defined, and fuzzy factors. These encompass socioeconomic, demographic and behavioral aspects, such as trading area population, average household income, propensity for savings (saving habits), capital costs, competitor density, and location convenience. Although most socio-economic and demographic factors are quantifiable, behavioral factors such as customers' saving habits and location convenience are usually not quantifiable.

Thus, most bank location decisions include a few fuzzy goals; e.g., selecting a “more convenient” site in terms of public accessibility, and generating an “acceptable” level of revenues by increasing market shares in given trading area and by minimizing capital costs. A bank may aim for “acceptable” or “satisfying” revenues rather than at maximizing them in order to thwart potential competition. Since the conventional Operations Research (OR) techniques such as linear programming (LP) and standard goal programming (GP) cannot properly deal with the behavioral factors and fuzzy goals, we propose a fuzzy GP model that allows the decision maker (DM) to be linguistic or imprecise in the articulation of locational goals. Additionally, an interactive scheme is used to permit a dialogue between the DM and the model. But a good dialogue cannot be developed without an interface between the model and its related data: the model parameters.

## 2. Literature Review of Previous Bank Location Research

Due to the complex and uncertain nature of the long-term and strategic bank location problem, only a few analytical studies have been reported in the literature. Carter and Cohen [3] first analyzed the branch-bank location problem as a capital budgeting problem using risk analysis. They adopted a simulation approach, which aimed to reduce the uncertainty in the expected rate of return from a proposed branch-bank site by experimenting with location alternatives. Due to large data requirements and lengthy computer programs, their simulation approach tends to be extremely inefficient and time-consuming when comparing all potential branch-bank sites with respect to their profitability. On the other hand, Soenen [20] introduced a gravity model to define a trading area for the proposed bank office and eventually to determine the appropriate bank site. He also identified, using a regression analysis, various factors which influence customers' bank selection patterns. Similarly, Clawson [4] determined the significant factors affecting "net savings gain" of each branch using a stepwise multiple linear regression analysis. Later, Doyle et al. [5] extended the works of Soenen [20] and Clawson [4] to develop a stochastic model for multivariate determination of the main exogenous variables influencing the deposit and loan potential of a branch. Bell and Zabriskie [2] employed a unique technique called "computer-aided mapping (CAM)" that generated location-related data on a map. The CAM visually produced data concerning population density, breakdowns of population by ethnic group, crime rate, zoning, market potential, etc. in varied color patterns or shadings. The CAM would be an effective means of communicating data with a bank manager; however, it might be an expensive one-time technique, for once there is a change in data, the map must be redrawn.

In general, previous studies focused on the identification of the most important variables in branch-bank location; they generally employed stochastic models to estimate the profitability of the proposed branch offices. Accordingly, these studies deal only with the diagnosis of the bank location problem, i.e., the intelligence stage of a three-part decision-making paradigm: intelligence, design, and choice (see, e.g., Simon [19] for the three-part classification).

Meanwhile, Bandyopadhyay [1], in a work synthesizing applications of OR in banking, attempted to build a “flow-chart” (conceptual) model of rural branch-bank location. However, no rigorous mathematical model was presented in his research. Sweeny et al. [22] developed a deterministic Minimum Location Covering (MLS) model. They attempted to minimize the number of counties in which a principal place of business should be located in order to serve the entire state population with branch-banks. They, however, were mainly concerned with the allocation or “districting” decision of branch-banks rather than the specific location, per se. In fact, these previous studies that oversimplified the location decision procedure have yet to provide the DM with the specific location choice among competing alternatives. In other words, although they provide a basis for developing a model-based DSS, there was no multi-criteria model-based DSS that could absorb complex location-related information and establish multiple, conflicting, and fuzzy locational goals.

## 3. An Architecture of the Locational DSS

To extract appropriate information and to facilitate a dialogue between the manager and the model, we first construct an architecture of the locational DSS. The architecture consists of three basic components: data management, model management, and dialogue management, as suggested by Sprague and Carlson [21].

## 3.1. Data Management Subsystem

Although the core of a model-based DSS is undoubtedly its model subsystem, the bank location model cannot be executed without providing it with a database. This contains the location-related data sources which constitute the model parameters. To avoid data redundancy, these data sources are broken down into (1) external, (2) internal and (3) government sources. External ones may include data files obtainable from local census bureau, chambers of commerce, and regional planning agencies. Internal sources are available from the bank's internal marketing, accounting data files, and "Retail Banking Service Potentials," the guide provided by American Bankers Association. Government sources include legal documents and reports issued by federal and state governments. Based on the studies of Soenen [20] and Robertson and Bellenger [16], the three broad source categories are further subclassified in Table 1.

With the sets of input data classified in Table 1, our database can prevent the modeler from using redundant data sources and allow direct and convenient access to data in a user-oriented way. The location database will be more useful if data can be statistically analyzed. Statistical analyses can be used to transform raw input into meaningful, interpretable information.

## 3.1.1. Multivariate Analysis

A multiple regression analysis may be used to investigate the relationships between bank profitability and input data. Bank profitability (net savings gained by a potential branch) is regarded as a dependent variable. Examples of independent

Table 1
Input data classification.

1. Demographic data - area population, rate of population change, percentage of married couples, percentage of seniors (over 65 years old).

2. Socio-economic data - total family income, median family income, bank-robbery rate.

3. Bank market data – existing bank to population ratio, bank deposits per capita, propensity for savings, business characteristics of market segments, i.e., residential versus commercial districts.

4. Comparative data - proximity of the existing banks to the new site, type of bank services provided by competitors, number of the existing banks.

5. Public utility data – public transit systems, major transportation arteries including highways, parking facilities, nearness to shopping centers, universities, and colleges.

6. Investment data – rate of returns, capital cost, property taxes, depreciation, insurances, and investment budgets.

7. Policy data – strategic bank business policies, local and federal government laws and regulation.

variables are population characteristics, degree of competition, and cost of bank services. In addition, a step-wise regression analysis or factor analysis may be used to identify a smaller number of underlying factors influencing a location decision. Either one of these technique would help determine the relevancy of the data; for example, a factor analysis has been considered a data reduction technique (Kim and Mueller [12]).

## 3.1.2. Forecasting Technique

Considering that external (census and economic) data are changing over time, the use of a forecasting technique is necessary to predict growth rates of bank deposits and loans that are crucial to the bank location decision.

## 3.1.3. Simulation Model

A decision on bank location can be considered a capital budgeting problem (Carter and Cohen [3]). This includes risk analysis to evaluate expected returns. The simulation model can be used to evaluate alternative investment opportunities under various realistic circumstances. It eventually helps a bank manager analyze the portfolio effect of introducing a new bank into an area.

## 3.1.4. Computer Aided Mapping (CAM)

To provide a DM with visual summaries of input data, CAM may be utilized. Maps generated by CAM help identify population growth patterns, competitor density, crime rate, etc. Consequently, CAM can be an important visual aid.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1. Decision Variable
 $x_{j}=1$  if a branch-bank j is “opened,”
=0 if a branch-bank j is “closed.”
</div>

## 3.2. Model Management Subsystem

The main focus of the model management subsystem is the design of a normative model to allow the DM to structure various locational goals, constraints, and variables. Although the model can be treated as a “black-box” whose algorithm and solution procedures need not be understood by the bank manager, it should generate and compare alternative scenarios in fairly simple and transparent terms. In other words, the specific choice of a bank location model heavily depends on the degree of user-friendliness. To increase user-friendliness, we integrated a GADS (Geodata Analysis and Display System) into the model-base. Consequently, the model management subsystem consists of two basic components: (1) GADS and (2) MCDM (Multiple Criteria Decision Making) model.

## 3.2.1. GADS

GADS was originally developed in the early 1970's by the IBM Research Division for the analysis of geographic data by non-technicians. Due to its flexibility and simplicity through an interactive graphical display it was widely applicable to many geographical planning problems, such as the urban analysis and school zoning (Keen and Scott-Morton [11]). Considering its capability in defining zoning boundaries, the GADS can be used to identify potential bank market boundaries that determine a limited number of potential bank sites and measure future market share.

## 3.2.2. MCDM Model

In selecting an appropriate location model (a critical component of the model-base), we consider its ability to capture realistic aspects of bank location decisions as well as its usability. Among many available OR techniques, we chose a fuzzy GP approach $[8,15]$ .

First, such a technique allows simultaneous analysis of multiple quantifiable (e.g., generating large amount of bank deposits) and nonquantifiable criteria (e.g., providing good public service). According to Jelassi et al. [10], ability to consider both quantifiable and nonquantifiable objectives is one of the most important ingredients of a multicriteria DSS.

Second, some objectives involve imprecise or linguistic goals which cannot be defined clearly by bank managers. For instance, the bank manager may desire a “substantial increase” of bank deposits and/or “more convenient” parking facilities for clients. To deal with these goals, inherent in bank location situations, we employ a fuzzy GP technique. Minch and Sanders [14, p. 406] said, “an important addition to a data-management system for MCDM purposes is the capability to handle linguistic variables.” Therefore, in the context of MCDM-DSS, the use of a fuzzy GP technique is further justified.

Third, a fuzzy GP model has a relatively simple structure, easily understood by nontechnical users, e.g., bank managers, because the fuzzy GP model can be formulated within a traditional LP framework $[24]$ . A survey by Fabozzi and Trovato $[7]$ revealed that LP has gained wider acceptance by the banking community as a decision-making tool. Accordingly, the fuzzy GP model can be successfully implemented by bank managers using large-scale commercial computer codes such as the packages of MPSX $[9]$ and SCICONIC/VM $[23]$ . In addition, the fuzzy GP model can be solved using LINDO $[18]$ , which has been commercially available as a microcomputer software package at a relatively low price: thus the fuzzy GP model can substantially enhance the user-friendliness of our DSS.

Finally, since bank managers may be reluctant to identify a priori a lexicographic importance of competing locational goals, the fuzzy GP model may be relevant because it treats all goals with equal or comparable importance. Moreover, the computer runs can be carried out in an interactive mode by changing the parameters, and the potential leeway of fuzzy goals. Thus, the fuzzy GP model can strengthen the communication link between the model and the DM.

The general formulation for the bank location problem is presented in the following.

Notations

## 2. Parameters

$\rho = \text{the degree of “agglomeration” (Note: The higher the value of } \rho, \text{ the more opportunities a branch-bank location has of attracting a large number of clients.)}$

$r_{j}^{\rho}=$ the relative distance from the potential branch-bank site j to its nearest competitive (homogeneous) existing branch-bank site,

$a_{j} =$ the population in the trading area of potential branch-bank $j$ ,

$b_{j}$ = the per capita income in the trading area of potential branch-bank j,

$c_{j}=$ the average propensity for savings per person in the trading area where the potential branch-bank j is sited,

$q_{j}$ = the number of existing competitive (homogeneous) banks in the trading area where the potential branch-bank j is sited,

$W_{j}=$ the weighting scale for the commercial deposit potential of the merchants and professional practices located within the trading area of the proposed branch-site j; this is:

0.5: pure residential area

1.0: partially residential and commercial area

2.0: pure commercial area

$F_{j}=$ the fixed cost such as initial investment cost to establish a branch-bank at potential site j.

$V_{j}=$ the operating cost such as rental and depreciation to maintain a branch-bank at potential site j,

$U_{j} =$ the public utilities at potential branch-bank site $j$ (Note: this is a scale ranging from 1 to 10), $P =$ the number of new branch-banks to be opened,

$d_{j} =$ the average distance traveled by clients expected to bank at branch site $j$ ,

$S^{\rho}$ = the relative distance beyond which the attractiveness of the branch-bank is considered dramatically “declines.” The value of $S^{\rho}$ is presumed to be constant, regardless of the trading area,

$M =$ the maximally achievable public utilities,

$R =$ the acceptable amount of expected return,

H = the threshold weighted travel distance beyond which banking services for any trading area fall to zero,

## 3. Indices

$I =$ the set of bank trading area $(i = 1,2,\dots,m)$ , $J =$ the set of potential branch-bank sites $(j = 1,2,\dots,n)$ ,

$T_{i}=$ the set of potential branch-bank sites in the given trading area i.

## Fuzzy GP Formulation

max $\lambda$

(1)

Subject to

$$
\sum_ {j \in J} r _ {j} ^ {\rho} x _ {j} / \alpha + d ^ {-} - d ^ {+} = S ^ {\rho} \cdot P / \alpha ,\tag{2}
$$

$$
\sum_ {j \in J} \left\{\left[ W _ {j} a _ {j} b _ {j} c _ {j} / (q _ {j} + 1) \right] - \left[ F _ {j} + V _ {j} \right] \right\} x _ {j} / \beta
$$

$$
+ e ^ {-} - e ^ {+} = R \cdot P / \beta ,\tag{3}
$$

$$
\sum_ {j \in J} U _ {j} x _ {j} / \gamma + f ^ {-} - f ^ {+} = M \cdot P / \gamma ,\tag{4}
$$

$$
\sum_ {j \in J} a _ {j} d _ {j} / \delta + g ^ {-} - g ^ {+} = H \cdot P / \delta ,\tag{5}
$$

$$
\sum_ {j \in T _ {i}} x _ {j} \leq 1, \quad i \in I,\tag{6}
$$

$$
\sum_ {j \in J} x _ {j} = P,\tag{7}
$$

$$
\lambda + \alpha^ {+} \leq \phi ,\tag{8}
$$

$$
\lambda + e ^ {-} \leq \psi ,\tag{9}
$$

$$
\lambda + f ^ {-} \leq \theta ,\tag{10}
$$

$$
\lambda + g ^ {+} \leq \nu .\tag{11}
$$

$$
\lambda , d ^ {-}, d ^ {+}, e ^ {-}, e ^ {+}, f ^ {-}, f ^ {+}, g ^ {-}, g ^ {+} \geq 0,
$$

where $\alpha, \beta, \gamma, \delta, \phi, \psi, \theta, \nu$ 's are subjectively chosen constants.

Objective function (1) maximizes the minimum fuzzy membership function, i.e., minimizes the maximum deviation from the fuzzy goal. Constraints (2), (3), (4), (5) are fuzzy locational goal constraints. To elaborate, constraints (2) minimizes the relative distance of the potential branch site to its nearest existing homogeneous bank sites. Constraint (3) insures sufficient amount of expected return; here, the expected return is computed using the retail revenue-generating function: expected return = estimated total deposit potential - facility cost = (weighted average per capita deposit) × (population of the trading area) - (investment and operating cost for the bank).

Constraint (4) assures the easiest accessibility to public utilities. Since the public utilities are usually more accessible in the area of colleges, universities, shopping malls, and office buildings,

the utility measures implicitly consider the nearness to those facilities. Also, in our model, public utilities include low crime rates, such as bank-robbery rates. Constraint (5) minimizes the weighted travel distances from the center of the trading area to the potential site, presuming that most bank customers have a tendency to bank at the branch office nearest to their home or place of work. Constraints (6), (7) are system constraints. Constraint (6) states that no two new branch-banks are located in the same trading area. This is not a strict equality constraint, for it allows the possibility of locating one branch or not locating a branch in a particular trading area at all. Constraint (7) limits a number of multiple branch-banks that may be simultaneously located in all potential sites. In fact, legislative regulation on the establishment of new branch-banks may determine the maximum number of new branches added in a given period. Constraints (8), (9), (10), (11) are associated with objective function (1).

![](/api/attachments/G4JVJYV5/fulltext/images/f7aba4a0011efd42fa14544f7cfce98a6abceafab78de5c7aedb59a74c419b86.jpg)  
Fig. 1. A Conceptual Architecture for the Bank Locational DSS.

## 3.3. Dialog Management Subsystem

"As a model becomes more approximate and sacrifices reality in order to gain information and computation and computational advantages, generally the model must be run more times in order to gain insights equivalent to those that would be obtained from a single solution of the more realistic alternative model." (Dyer and Mulvey [6, p.103]) In view of this, the dialog management subsystem focuses attention on the user-model interface to enable the end-user (bank manager) to recognize and enumerate the trade-offs as a means to evaluate alternative location scenarios. Through the trade-off analysis the end-user may choose the best bank site, but it cannot be efficiently used without standardized output-display mechanisms that bridge the communication gap between the model and its non-technical user. Such standardized output-display mechanisms consist of two visual representations: (1) tables that give an initial list of candidate bank sites generated by the model-base, and (2) value paths which pictorially summarize the pros and cons of locating a bank on each candidate site. These visual mechanisms will also help the user by responding to "what-if" queries because they facilitate close interaction and feedback between the model and its user.

To recapitulate, Figure 1 depicts the three-way linkages among the data, model, and dialog management.

It also schematically demonstrates the development process of the bank locational DSS. The development process is comprised of six main steps: (1) creation of the locational data base, (2) analysis, display, and transformation of the location-related data, (3) construction of location models, (4) modification and revision of location models, (5) final recommendations and reports for the locational configurations of multiple branchbanks, and (6) sensitivity or parametric analysis of location models.

Because many previous studies have concentrated on the steps 1 and 2, the major emphasis in our study has been upon steps 3, 4, 5, and 6, i.e., the design and choice stages of the decision process.

## 4. An Illustrative Example

To demonstrate the applicability of the model-based DSS, we consider the hypothetical case of simultaneously opening two new branch-banks of equal size (15,000 square feet), which are franchised by a large commercial Ohio bank system, in the northern part of Columbus, Ohio. For illustrative purpose, we make the following assumptions:

(1) The real competitors of new branch-banks are illustrated by the franchised branch offices of Banc One National Bank, Bank One of Columbus, Franklin Bank, Huntington National Bank, Ohio State Bank, Society Bank, and State Savings Bank. We do not include savings and loan associations, investment banks, auto banks, and other financial institutions as real competitors.

(2) The trading area boundary of banking services is tantamount to the boundary of census tracts defined by the 1980 Census of Population and Housing [25]. For simplicity, we assume that trading areas do not overlap, although this may not be the case in large metropolitan areas.

Under the above assumptions, the proposed DSS has been implemented to solve the hypothetical location problem with 20 potential sites as portrayed in Figure 2.

Although the successful application of the DSS to the sample problem relies on the close linkage and integration of three subsystems, we treat the fuzzy GP model as a central and coordinating component of our model-based DSS. Consequently, the final location strategy was chosen by solving the fuzzy GP model in an interactive mode. The actual model formulation contains 29 constraints and 28 decision variables, which include 20 binary integer variables. The model was tested using a SCICONIC/VM computer package on a PRIME 9955 super-minicomputer system at the Ohio State University. The integer programming agenda, GLOBAL, along with BOUNDS section that enoubles us to specify some binary variables, of the SCICONIC/VM package was employed to solve the integer problem.

![](/api/attachments/G4JVJYV5/fulltext/images/5313b63aba77a1d607f1117ca9e178b153229f253f57ab651c8d42bad5dd1e8a.jpg)  
Fig. 2. Spatial Distribution of Trading Area Boundaries and Existing Branch-bank Locations.

After obtaining the initial configuration, we carried out the interactive test runs by modifying parameters, constraints, and degradation allowances of fuzzy goals. The three interactive results given in Table 2 may illustrate alternative location strategies.

While this paper reports only the interactive results of three computer runs, interested users certainly can utilize the model for more interaction with DM. In addition, to improve the interpretability of our interactive test results that produce different location strategies, we employ the value path approach proposed by Schilling et al. [17]. The value paths of our interactive test results are graphically displayed in Figure 3.

Summary of the interactive test runs.

<table><tr><td>Solution</td><td>Run1</td><td>Run2</td><td>Run3</td></tr><tr><td>Alternative</td><td>Site 7</td><td>Site 7</td><td>Site 13</td></tr><tr><td>Location</td><td>Site 13</td><td>Site 15</td><td>Site 20</td></tr><tr><td>Configuration</td><td></td><td></td><td></td></tr><tr><td colspan="4">Fuzzy Goal Achievement</td></tr><tr><td>1. Relative Location</td><td>Satisfied</td><td>Satisfied</td><td>Satisfied</td></tr><tr><td>2. Revenue</td><td>Satisfied</td><td>Unsatisfied</td><td>Satisfied</td></tr><tr><td>3. Utility</td><td>Satisfied</td><td>Satisfied</td><td>Satisfied</td></tr><tr><td>4. Distance</td><td>Unsatisfied</td><td>Unsatisfied</td><td>Unsatisfied</td></tr><tr><td>Number of iterations</td><td>25</td><td>32</td><td>38</td></tr><tr><td>Prime 9955 CPU Time (Sec.)</td><td>3</td><td>4</td><td>4</td></tr></table>

![](/api/attachments/G4JVJYV5/fulltext/images/dc1c5c3f7f05215d2d9e3b3dcabb7baf8ceb69354bfdb2bbd846fc4eb2919e36.jpg)  
Fig. 3. Value Paths of Three Interactive Runs.

These value paths help the DM to compare the alternative location strategies because the DM can easily perform trade-offs analysis. For example, as shown in Figure 3, the location scenario based on the second run creates the largest public utilities among three sample scenarios; however, it generates the lowest projected revenue. More importantly, the value paths enable the DM not only to handle multiple location scenarios at once, but also to measure the opportunity costs that the DM should pay for the improvement of other fuzzy goals.

## 5. Summary and Conclusions

Due to the complexity and uncertainty involved in banking environments, the location decision normally requires large quantities of input data, as well as a sophisticated model design. Although the major focus of our attention here is to build the DSS based on an elegant location model, the successful execution of this DSS relies on the quality of location-related information. Accordingly, the traditional “stand-alone” location model, which largely neglected data-management functions can no longer absorb large quantities of data critical to the bank location choice. Also, from a practical standpoint, an actual decision usually requires the bank manager to modify the model according to dynamically changing environments and to evaluate trade-offs for alternative locations. Here, an attempt has been made to facilitate the dialog between the user and the model.

In light of these discussions, one of the most important themes that emerges from this study is the integration of the normative location model within a MCDM DSS. Through the integration, we are able to improve the technical elegance and flexibility of the model, while increasing the user-friendliness and accessibility to the DM. In our specific bank location situations, an interactive fuzzy GP technique and a value path analysis are major vehicles that enable us to move in this direction.

## Acknowledgment:

The author would like to thank Professor Edgar H. Sibley and anonymous referees for helpful comments for improving the presentation.

## References

[1] R. Bandyopadhyay, “Operational Research in Development Banking in India.” European Journal of Operational Research, 2(1), 1978, pp. 8–25.

[2] R.R. Bell and N.B. Zabriskie, "Assisting Marketing Decisions by Computer Mapping: A Branch Banking Application." Journal of Marketing Research, 15, 1978, pp. 122–128.

[3] E.E. Carter and K.J. Cohen, “The Use of Simulation in Selecting Branch Banks.” Industrial Management Review, 8(2), 1967, pp. 55–69.

[4] C.J. Clawson, “Fitting Branch Locations, Performance Standards, and Marketing Strategies to Local Conditions.” Journal of Marketing, 38, 1974, pp. 8–14.

[5] P. Doyle, I. Fenwick and G.P. Savage, “Model for Evaluating Branch Location and Performance.” Journal of Bank Research, 12, 1981, pp. 90–95.

[6] J.S. Dyer and J.M. Mulvey, "Integrating Optimization

Models with Information Systems for Decision Support." In J.L. Bennett (Eds), Building Decision Support Systems. Reading, MA, Addison-Wesley, 1983.

[7] F.J. Fabozzi and S. Trovato, “The Use of Quantitative Techniques in Commercial Banks,” Journal of Bank Research, 6, 1976, pp. 173–178.

[8] E.L. Hannan, “On Fuzzy Goal Programming.” Decision Sciences, 12, 1981, pp. 522–531.

[9] IBM Mathematical Programming System Extended/370 Program Reference Manual (4th ed.), 1979.

[10] M.T. Jelassi, M. Jarke, and E.A. Stohr, “Designing a Generalized Multicriteria Decision Support System.” Journal of Management Information Systems, 1(4), 1985, pp. 24–43.

[11] P.G.W. Keen and M.S. Scott-Morton, Decision Support Systems: An Organizational Perspective, Reading, MA, Addison-Wesley, 1978.

[12] J. Kim and C.W. Mueller, Factor Analysis: Statistical Methods and Practical Issues, Beverly Hills, CA., Sage Publications, Inc., 1\*978.

[13] R.L. Kramer, “Forecasting Branch Bank Growth Patterns.” Journal of Bank Research 1(4), 1971, pp. 17–24.

[14] R.P. Minch and G.L. Sanders, “Computerized Information Systems Supporting Multicriteria Decision Making.” Decision Sciences, 17(3), 1986, pp. 395–423.

[15] R. Narasimhan, “Goal Programming in a Fuzzy Environment.” Decision Sciences, 11, 980, 325–336.

[16] D.H. Robertson and D.N. Bellenger, “Identifying Bank Market Segments.” Journal of Bank Research, 7, 1977, pp. 276–283.

[17] D.A. Schilling, C. Revelle and J.L. Cohon, “An Approach to the Display and Analysis of Multiobjective Problems.” Socio-Econ. Plan Sci., 17(2), 1983, pp. 57–63.

[18] L. Schrage, Linear, Integer and Quadratic Programming with LINDO: Users Manual. Palo Alto, CA, The Scientific Press, 1984.

[19] H.A. Simon, The New Science of Management Decision, New York: Harper and Row, 19960.

[20] L.A. Soenen, “Locating Bank Branches.” Industrial Marketing Management, 3, 1974, pp. 211–228.

[21] R.H. Sprague and E.D. Carlson, Building Effective Decision Support Systems. Englewood Cliffs, NJ, Prentice-Hall, 1982.

[22] D.J. Sweeny, R.L., Mairose, and K. Martin, “Strategic Planning in Bank Location.” Proceedings. Atlanta, GA, Decision Sciences Institute, 1979.

[23] Users Guide to SCICONIC/VM (Version 1.30). Milton Keynes, U.K., Scicon Computer Services, 1983.

[24] H.J. Zimmermann, “Fuzzy Programming and Linear Programming with Several Objective Functions,” Fuzzy Sets Systems, (1), 1978, pp. 45–55.

[25] 1980 Census of Population and Housing. Columbus, OH, U.S. Dept. of Commerce, Bureau of the Census, 1983.
