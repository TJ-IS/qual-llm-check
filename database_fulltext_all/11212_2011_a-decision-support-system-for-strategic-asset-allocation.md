---
otero_id: 11212
otero_key: "TDAXGE88"
title: "A decision support system for strategic asset allocation"
authors: "P. Beraldi; A. Violi; F. De Simone"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.02.017"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for strategic asset allocation<sup>☆</sup>

P. Beraldi <sup>a,</sup>⁎, A. Violi <sup>a,b</sup>, F. De Simone <sup>a,b</sup>

<sup>a</sup> Department of Electronics, Informatics and Systems, University of Calabria, Rende, Italy

<sup>b</sup> NEC-CESIC, Supercomputing Center for Computational Engineering, Rende, Italy

## a r t i c l e i n f o

Article history: Received 18 February 2010 Received in revised form 13 December 2010 Accepted 27 February 2011 Available online 11 March 2011

Keyword: Strategic asset allocation Risk management Stochastic programming

## a b s t r a c t

Strategic asset allocation is a crucial activity for any institutional or individual investor. Given a set of asset classes, the problem concerns the de<sup>fi</sup>nition and management over time of the best asset mix to achieve favorable returns subject to various uncertainties, policy and legal constraints, and other requirements. Although a considerable attention has been placed by the scienti<sup>fi</sup>c community to address this problem by proposing sophisticated optimization models, limited effort has been devoted to the design of integrated framework that can be systematically used by <sup>fi</sup>nancial operators. The paper presents a decision support system which integrates simulation techniques for forecasting future uncertain market conditions and sophisticated optimization models based on the stochastic programming paradigm. The system has been designed to be accessed via web and takes advantages of the increased computational power offered by high performance computing platforms. Real-world instances have been used to assess the performance of the decision support system also in comparison with more traditional portfolio optimization strategies.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Optimization-based decision support systems (DSS) provide a powerful tool in many industrial and operative contexts. By the formulation of optimization models it is possible to mathematically represent complex decision making problems and control, by the corresponding solutions, critical issues such as cost, risk, performance indexes and so forth. When encapsulated in decision support systems, the advantage related to the adoption of quantitative methodologies is further enhanced by the recent advances in computer science and information technology. The impact deriving from the adoption of DSS becomes even more evident in all those operative contexts characterized by a high level of complexity due, for example, to the presence of uncertainty, to the need to analyze huge amount of data and to operate in a short time. All these features are dominant in the <sup>fi</sup>eld of <sup>fi</sup>nancial management where the adoption of ef<sup>fi</sup>cient and effective DSS can assist the complex decision making process by improving the quality and the effectiveness of provided solutions. Nevertheless, recent global crisis and spectacular breakdowns have further emphasized the need to complement expertise and experience with the suggestions provided by advanced systems based on the integration of decision models and algorithms.

The paper contributes in this direction by proposing a system designed to support <sup>fi</sup>nancial operators in portfolio management activities. Different applications, from personal <sup>fi</sup>nancial planning, to pension fund management, to strategic and tactical asset allocation can be casted as Asset–Liability Management problems (ALM) (see the contributions in [12,14,33,38]). In this paper, the attention is focused on the strategic asset allocation problem (SAA, for short). Given a time horizon, the problem refers to the allocation and management of a portfolio of asset classes with the aim of maximizing the portfolio return while controlling the risk exposure.

SAA is a crucial problem that every investor (at individual or institutional level) has to deal with. Its practical relevance is the motivation behind the considerable attention devoted to this topic by the scienti<sup>fi</sup>c community. Starting from the Markowitz's seminal contribution [27] based on a static buy and hold portfolio strategy, other modeling frameworks [6,9,26,28,29,32] have been proposed and deeply investigated in the last decades. A special attention deserves the stochastic programming framework (SP, for short) [8,22] because of its high modeling power stemming from the integration of dynamic and uncertain aspects also accounting for the possibility to accommodate speci<sup>fi</sup>c requirements (policy restrictions, trading constraints, and so forth). On the other hand, the complexity of the SP methodology has limited its wide diffusion in the non-academic environment.

The considerations reported above represent the main motivation of the present contribution aimed at proposing a user-friendly DSS relying on the integration of SP as decision engine with simulation techniques for the generation of future uncertain market conditions and solution algorithms powered by the adoption of advanced computing platforms.

Other DSS designed for <sup>fi</sup>nancial management problems have been proposed in the last decade. A system which integrates multi-dimension databases, on-line analytical processing (OLAP) tools, procedural and declarative modeling languages has been proposed in [15]. In [30] the authors have proposed DSSALM, a tool to simulate interest rate risk and forecast the amounts of future assets and liabilities. Another contribution is [16], where the authors propose a web-based DSS which integrates portfolio management models with OLAP tools to handle multidimensional data structures and PVM network environment as high-performance computational framework.

The proposed DSS differs from other systems for the following features:

• the system core relies on innovative methodologies for the SAA problem and takes advantage of the computational power offered by high-performance computing environment. This last feature is particularly important for applications which are “space”-sensitive: a huge amount of data should be stored, managed and analyzed in order to get robust recommendations. In addition “time” can play a key role in terms of competitive advantage;

• the DSS provides a tool for risk management and allows benchmark analysis with other portfolio strategies;

• the system can be easily extended to other problems and functionalities, thanks to its modular structure;

• customers can access the system by a user-friendly interface and can easily modify parameters and settings;

• no investment or maintenance cost for <sup>fi</sup>nal users is required because of the web technology used.

The rest of the paper is organized as follows. Section 2 describes the SAA problem and provides a high level snapshot of the methodological framework. Section 3 presents the system architecture, by illustrating the main technical choices and the functional modules which implement the proposed methodological steps. Section 5 presents a system demo from an end-user perspective. Computational experiments are reported in Section 6: extensive numerical tests have been carried out in order to assess the performance of the proposed system also in comparison with other approaches. Some concluding remarks end the paper.

## 2. The SAA problem and proposed approach

The SAA problem concerns the de<sup>fi</sup>nition of a medium–long term allocation among a given set of “asset classes", i.e. macro-sets of <sup>fi</sup>nancial instruments identi<sup>fi</sup>ed by a common reference index. The goal is to achieve the maximum portfolio return within a user-de<sup>fi</sup>ned risk level and according to speci<sup>fi</sup>c requirements. This is a classical planning problem that <sup>fi</sup>nancial management typically faces at “strategic” level, since decisions concern classes of assets rather than single instruments whose choice is, on the contrary, performed at a tactical level, eventually according to some speci<sup>fi</sup>c policies of the <sup>fi</sup>nancial institute. The problem at hand belongs to the more general class of ALM problems and presents several critical features dif<sup>fi</sup>cult to deal with, even separately. The problem is dynamic since decisions (portfolio allocation) are taken all over the planning period and are strictly connected to market evolution. It is intrinsically stochastic since optimization should be carried out without the knowledge of the uncertain future evolution of market conditions. In addition, the problem is highly constrained, since a large number of regulatory, strategic and risk aversion constraints should be considered in order to mathematically represent end-user concerns. The SP framework allows to jointly accommodate all these features, providing more robust recommendations with respect to other modeling approaches [36]. This motivates the large stream of literature on SP for ALM problems [10,11,13,17,19,25,31,37]. Differently from other frameworks, within multistage SP the portfolio allocation problem is formulated so to consider the possibility to revise initial decisions concerning the portfolio composition. As time progresses and new information about market conditions become available, asset allocation can be revised by means of buying/selling decisions, also taking into account the possibility to have additional cash in<sup>fl</sup>ows. The complete mathematical model of the SAA problem formulated according to the multistage paradigm is introduced in Appendix B.

SP relies on the explicit accounting of the uncertainty surrounding the market conditions by the introduction of random variables de<sup>fi</sup>ned on a given probability space. In the case of discrete distributions, a scenario tree is used to represent the dynamic uncertain evolution of the random parameters. Fig. 1 shows a scenario tree for a planning horizon of length 3.

The root node (denoted by 0) represents the initial state. A scenario is a path from the root to a leaf node. Each intermediate node at a given level contains a realization of the uncertain parameters (assets values, risk-free rate, etc.) at that corresponding time stage. Probability is associated with each node so to satisfy the fundamental axioms of the probability theory.

The scenario tree provides the input parameters for multistage models. Here decisions are associated with each node. In the case of the SAA problem, <sup>fi</sup>rst stage decisions (associated with the root) concern the selection of the initial portfolio composition. At successive stages, according to the speci<sup>fi</sup>c scenario, portfolio is rebalanced in such a way to achieve maximum performance satisfying risk constraints and other requirements. Additional constraints, known as non anticipativity restrictions assure consistency of the decisions with the tree structure [8].

Our DSS has been designed according to the adopted methodological framework. Fig. 2 shows the main steps and their interactions. The decision approach is based on the availability of historical data related to asset class indexes, interest rates, macroeconomic variables and so forth. These data are stored in a consistent database and are statistically analyzed in order to determine parameters to use in the scenario generation step. According to the scenario tree and the user requirements and settings a dynamic optimization model, representing the SAA decision problem, is created and solved. Solutions are then analyzed and elaborated in order to provide the end-user with reports and statistics easily accessible. Re<sup>fi</sup>nements and further evaluations can be carried out by feed-back processes.

## 3. System design

A prototypal DSS has been designed to support the main steps of the framework introduced above. The resulting architecture presents a three-tier structure as illustrated in Fig. 3. The front-end exposes a user-friendly web-based interface that provides the access to applications and functionalities of the system. The middle layer is composed of modules and tools to ef<sup>fi</sup>ciently balance computational workload among available computing resources and to manage requests assignment. The third layer includes computing nodes, each one with an application kernel instance, a local resources manager and a

![](/api/attachments/TDAXGE88/fulltext/images/9967756aa6b9d51cfbe843a69bbd71de7f2acc913e9b5a1948ee24d760cd4844.jpg)  
Fig. 1. Four-stages scenario tree.

![](/api/attachments/TDAXGE88/fulltext/images/8e44aa24bab845d517e2914617fa0069033fa7619f40e471c9e371f6554dc7a5.jpg)  
Fig. 2. Decision approach steps.

data manager for handling <sup>fi</sup>nancial historical data and simulation and optimization results. The DSS kernel, implemented on each computing node of the platform, is composed by a set of independent functional modules, according to the methodological steps of the decision approach described in the previous section. The following Fig. 4 shows a high-level snapshot of the system kernel. The modules are strictly coordinated by sharing a common database which stores all the data related to a service request. The data <sup>fl</sup>ow among the modules is allowed by the unique identi<sup>fi</sup>cation code of each request, starting from which the user can access all related information. Each module is invoked by the request which identi<sup>fi</sup>es all the input data for the algorithms.

![](/api/attachments/TDAXGE88/fulltext/images/6c813024d96c87c2cd3d8a447f0209f8fcd992c002e2cd7c86f14a7705bcf7ff.jpg)  
Fig. 3. Overall architecture of the system.

The progress of the decision process can be monitored by the request status which is updated by each functional module according to a prede<sup>fi</sup>ned schema.

All the functional modules have been implemented in C++ and include some state-of-art scienti<sup>fi</sup>c and <sup>fi</sup>nancial libraries. A detailed description of the modules together with the methodological choices is reported below.

## 3.1. Data management

Data related to different entities involved in the decision process are stored in a unique database. More speci<sup>fi</sup>cally, data refer to historical information concerning prices of the <sup>fi</sup>nancial instruments, values of macroeconomic variables, generated scenarios and old portfolio compositions, together with user parameters and settings and solution analysis reports, that end-users may be willing to look at future time.

The DBMS has been implemented by using PostgreSQL,<sup>1</sup> an advanced open source object-relational database system. However, in order to maintain <sup>fl</sup>exibility and portability a C++ based API library for the communication between functional modules and database has been de<sup>fi</sup>ned and implemented.

## 3.2. Statistical analysis module

This module analyzes and elaborates the huge amount of data storing historical information for deriving some statistical measures (mean, variance, and covariance) and estimating the parameters of the models used in the scenario generation step. The module has been implemented in C++ and Matlab, and links some advanced scienti<sup>fi</sup>c libraries (GSL<sup>2</sup>). It is worthwhile noting that operations performed by this module can be considered off-line with the rest of the system, since they can be carried out just when the historical database is updated and not necessarily each time a request is submitted.

![](/api/attachments/TDAXGE88/fulltext/images/2ab0bcb451b03a02e2c7f6248a01da7b3f4865518631f44070f8bcf4c872ab1f.jpg)  
Fig. 4. High-level kernel architecture.

## 3.3. Scenario generator

Under the assumption of discrete probability space, the uncertain future evolution of market conditions is represented by means of a scenario tree. Scenario generation is a critical issue in any decision making problem under uncertainty. In the case of SP, scenarios provide the input parameters of the optimization model, thus “bad” scenarios translate in “bad” recommendations.

The relevance of this topic has motivated a rich and intense research activity in the last decades. Many different techniques have been proposed ranging from simulation to sampling and statistical methods [4,20,24,35]. The choice of the most appropriate technique typically depends on the speci<sup>fi</sup>c application at hand. For the SAA problem we have de<sup>fi</sup>ned a Monte Carlo procedure based on a global model, which integrates an economic model and a capital market model [2,14]. In particular, the model is based on the idea that asset classes of different currency areas can be clustered into a limited number of groups, each one represented by a relevant <sup>fi</sup>nancial index (for example, long term interest rate). The joint evolution of these indexes, also correlated with some macroeconomic variables (e.g., gross domestic product), is simulated for each currency area and thus the asset classes values are derived according to this dynamics. More details on the simulation model can be found in Appendix A.

Given a time horizon and a user-de<sup>fi</sup>ned time step, the tree generation is carried out level by level, specifying for each node a given number of children together with their probability of occurrence. Then, asset classes values at each node of the scenario tree are generated by a Monte Carlo procedure according to the economic and capital market model starting from the values at the ancestor node by extracting (correlated) values from a standard normal distribution. The scenario generation module has been implemented in C++ and links some <sup>fi</sup>nancial libraries (for example, Financial Numerical Recipes<sup>3</sup>) to perform speci<sup>fi</sup>c <sup>fi</sup>nancial calculations.

## 3.4. Model generator

The model generator builds a data representation of the speci<sup>fi</sup>c problem instance according to the mathematical paradigm adopted and on the basis of end-user parameters and generated scenarios. As described earlier, the multistage stochastic programming framework has been used to model the dynamic portfolio allocation problem. Here decisions are related to the amount invested in each asset class during the planning horizon under the different scenarios together with the amount eventually invested in a risk-free asset. Constraints are included to balance the monetary <sup>fl</sup>ow and to diversify portfolios according to speci<sup>fi</sup>c conditions imposed by the end user. The full description of the mathematical formulation is reported in Appendix B.

According to the evidence that the goal of an investor is usually twofold, i.e. pro<sup>fi</sup>t maximization and risk minimization, the model presents a classical mean–risk structure:

$$
\max (1 - \lambda) \overline {{{\mathbf {W}}}} - \lambda \mathbf {D}\tag{1}
$$

Here $\lambda \in ( 0 , 1 )$ is a user-de<sup>fi</sup>ned parameter accounting for risk aversion attitude, W denotes the expected value of the portfolio wealth at the end of the planning horizon, and D accounts for risk. In particular, Conditional Value at Risk (CVaR), has been used as risk measure. With respect to the well-known Value at Risk, CVaR allows a more accurate measure of tail losses and exhibits good computational and theoretical properties. It is a “coherent” measure [3], i.e. it satis<sup>fi</sup>es properties of monotonicity, sub-additivity, homogeneity, and translational invariance, and is also “convexity-preserving” in a mean–risk formulation [1].

By varying the value of λ different portfolios can be obtained accounting for different risk aversion attitudes.

The deterministic equivalent formulation of the problem has been generated by means of a C++ module which extends an open-source modern algebraic modeling language, FLOPC++ [21] of the COIN-OR project, which can be interfaced with many state-of-art solution solvers.

## 3.5. Solution kernel

Problem size is related to the number of asset classes, the length of the planning horizon and the scenarios number. This last element critically affects the solution process. If a larger number of scenarios allows a more faithful representation of the uncertain market conditions, on the contrary the huge size of the corresponding problem makes dif<sup>fi</sup>cult, the solution process, calling for the design of special-purpose algorithms, better if implemented on advanced computing systems. The solution kernel relies on a C++ module which links some state-of-art mathematical programming solvers, like CLP<sup>4</sup> (also in the COIN-OR project) and CPLEX<sup>5</sup> and implements also a special-purpose interior point method which exploits the particular model structure [5]. Moreover, in order to provide a trade-off analysis for the end-user the module performs multiple solution processes, taking advantage from the availability of a parallel computing framework. The module receives as input a coded version of the problem created by the model generator and, exploiting a parallel computing environment, solves several instances according to different values of the risk aversion parameter λ. Once the solution process is terminated, the module collects the results and stores solutions for subsequent analysis.

## 3.6. Solutions analysis module

Solution analysis is a very critical issue since recommendations provided by the model should be presented in a suitable form easily accessible also by non expert end-users. The DSS presents a module offering different functionalities. It performs a scenario based portfolio analysis, with evidence of the wealth evolution in the best and worst cases. Moreover, for each previously de<sup>fi</sup>ned solution it allows to calculate some statistical properties on the portfolio and the values of relevant risk measures. Also the robustness of the suggested <sup>fi</sup>nancial planning is evaluated by means of a sensitivity analysis. Finally, the solution is compared with other well-known decision approaches for portfolio management (static Markovitz model, <sup>fi</sup>x-mix, etc.). The module has been implemented in C++ and Matlab, and can be invoked also apart from the rest of the system for back-testing analysis or investment monitoring.

## 4. System implementation

The DSS described in the previous section represents the core of a service that can be offered to <sup>fi</sup>nancial operators according to the Application Service Providing (ASP) model. Operators can directly access the system via-web by means of user-friendly interfaces and work on their own requests simultaneously. In the last decades, webbased DSS are becoming more and more popular [7] in many applicative contexts. Decision makers can bene<sup>fi</sup>t from support for a complex decision process by simply using Web browser interfaces, which eventually integrate client side computation technologies like applets or Javascript.

The proposed DSS shares some features with the main categories of web-based DSS, data-driven and model-driven. On one hand the system allows to retrieve, organize and analyze a large amount of relevant data, on the other hand it provides a formal representation of a complex decision process and an analytic support by means of tools like simulation, optimization and statistics.

The choice of the web-based ASP model has been motivated by the relevant issues summarized as follows:

• reduction of operative costs: the use of internet as infrastructure for a web application allows to signi<sup>fi</sup>cantly reduce costs related to client management and software distribution;

• easy update: applications are run on remote servers, so a new version or an update will be immediately available for all the users;

• scalability: applications can be extended in terms of functionalities and users without particular problems of performance reduction by simply increasing hardware infrastructure.

The ASP model allows multiple users to concurrently access the system by an individual code and recover their own requests for monitoring, resubmitting and performance analysis. The concurrent use of the system has suggested the adoption of the high-performance computing. Each request is pre-processed by a resource balance module and is assigned to a computational node according to a load balance criterion. An additional the database stores data related to request users and their assignment to computing nodes, in order to guarantee each user to access his/her previous request.

Moreover, the adoption of high-performance computing systems may improve the ef<sup>fi</sup>ciency of the overall system. As previously observed, the solution process is typically computationally intensive for real applications and the adoption of parallel computing may lead to more robust solutions in a shorter time. Section 6 provides numerical evidence of the performance improvement achieved by the parallelization of the main steps.

## 5. System demo

Although implemented on a high-performance system, the powered platform is hidden to the decision maker, who can easily access the system by means of a login interface and can select the application he/she wants to use. Once the parameters of the speci<sup>fi</sup>c <sup>fi</sup>nancial planning application are set (Fig. 5), the request can be submitted and its status can be monitored by means of a request summary mask (Fig. 6). For the requests successfully completed, the <sup>fi</sup>nancial planning solution can be visualized, together with some statistics and relevant indexes. The system offers the possibility to perform different analysis, according to different decision levels. First of all, the system shows the so-called “ef<sup>fi</sup>cient frontier” (Fig. 7), that is the set of non dominated solutions (portfolios) obtained for different values of the risk aversion parameter λ. This information is very useful for a <sup>fi</sup>nancial operator, providing the tool for evaluating the best return/risk trade-off according to his/her requirements and strategies. Once the best solution according to the risk preference is chosen, (i.e. selected a particular value of λ) the end-

![](/api/attachments/TDAXGE88/fulltext/images/2e16227f741d1275934d96be7b362b630ff41bdc7af55c21834333de3283276e.jpg)

<table><tr><td>Request Submission</td><td>View Results</td><td>Welcome user2</td><td>logout</td></tr></table>

## Set Instruments

Strategic Asset Allocation >> Dynamic Stochastic Solution

<table><tr><td>☐</td><td>Code</td><td>Description</td><td>Invested Value</td><td>Market Area</td><td>Tipology</td></tr><tr><td>☑</td><td>UST5TR Index</td><td>BLOOMBERG/EFFAS BOND INDICES U</td><td>10000</td><td>DOLLAR</td><td>Bond</td></tr><tr><td>☐</td><td>UST4TR Index</td><td>BLOOMBERG/EFFAS BOND INDICES U</td><td>0.0</td><td>DOLLAR</td><td>Bond</td></tr><tr><td>☐</td><td>UST3TR Index</td><td>BLOOMBERG/EFFAS BOND INDICES U</td><td>0.0</td><td>DOLLAR</td><td>Bond</td></tr><tr><td>☐</td><td>UST2TR Index</td><td>BLOOMBERG/EFFAS BOND INDICES U</td><td>0.0</td><td>DOLLAR</td><td>Bond</td></tr><tr><td>☐</td><td>UST1TR Index</td><td>BLOOMBERG/EFFAS BOND INDICES U</td><td>0.0</td><td>DOLLAR</td><td>Bond</td></tr><tr><td>☑</td><td>SXXP Index</td><td>DJ STOXX 600 = PR</td><td>2000</td><td>DOLLAR</td><td>Stock</td></tr><tr><td>☑</td><td>INDU Index</td><td>DOW JONES INDUS. AVG</td><td>0.0</td><td>DOLLAR</td><td>Stock</td></tr><tr><td>☐</td><td>EE00 Index</td><td>EASTERN EUROPE GOVERNMENTS INDEX</td><td>0.0</td><td>DOLLAR</td><td>Bond</td></tr><tr><td>☐</td><td>EG09 Index</td><td>EMU DIRECT GOVERNMENTS 10+Y</td><td>0.0</td><td>EURO</td><td>Bond</td></tr><tr><td>☐</td><td>EURGBP Index</td><td>EUR-GBP X-RATE</td><td>0.0</td><td>EURO</td><td>Currency</td></tr><tr><td>☑</td><td>EURJPY Index</td><td>EUR-JPY X-RATE</td><td>0.0</td><td>EURO</td><td>Currency</td></tr></table>

## Set Parameters

Strategic Asset Allocation >> Dynamic Stochastic Solution >> Set Instruments

<table><tr><td colspan="3">Tipology Risk Constraint</td></tr><tr><td>Tipology Code</td><td>&#x27;Lower Bound %</td><td>&#x27;Upper Bound %</td></tr><tr><td>Bond</td><td>40</td><td>100.0</td></tr><tr><td>Stock</td><td>0.0</td><td>60</td></tr><tr><td>Currency</td><td>0.0</td><td>30</td></tr></table>

<table><tr><td colspan="3">Area Risk Constraint</td></tr><tr><td>Area Code</td><td>&#x27;Lower Bound %</td><td>&#x27;Upper Bound %</td></tr><tr><td>DOLLAR</td><td>0.0</td><td>100.0</td></tr><tr><td>EURO</td><td>0.0</td><td>100.0</td></tr></table>

<table><tr><td>Code</td><td>Description</td><td>Invested Value</td><td> $^{a}$ Lower Bound %</td><td> $^{a}$ Upper Bound %</td><td>Tipology</td><td>Market Area</td></tr><tr><td>UST5TR Index</td><td>BLOOMBERG/EFFAS BOND INDICES U</td><td>10000.0</td><td>0.0</td><td>100.0</td><td>Bond</td><td>DOLLAR</td></tr><tr><td>SXXP Index</td><td>DJ STOXX 600 = PR</td><td>2000.0</td><td>0.0</td><td>100.0</td><td>Stock</td><td>DOLLAR</td></tr><tr><td>INDU Index</td><td>DOW JONES INDUS. AVG</td><td>0.0</td><td>30</td><td>100.0</td><td>Stock</td><td>DOLLAR</td></tr></table>

Fig. 5. Request set-up.

user may access relevant statistics of the proposed <sup>fi</sup>nancial plan, from the best–worst case analysis to the wealth distribution over the scenarios set.

Finally, the end user can explore the proposed asset allocation along the planning horizon for each path of the scenario tree, together with wealth (and loss) evolution over time (Fig. 8).

![](/api/attachments/TDAXGE88/fulltext/images/cfc06d4ba5437e05ea474e97b535950f58baaf3829926034f36acefe0d1f2c7a.jpg)

Fig. 6. Request status check.  
![](/api/attachments/TDAXGE88/fulltext/images/1c323628fdc02e2ae0827cc6b731df41ea2c10b6a5dc69cbe4b0d025c5090473.jpg)  
Fig. 7. Ef<sup>fi</sup>cient frontier.

Such a detailed level of information, obtained through the elaboration of a huge amount of data, may provide a real advantage for the <sup>fi</sup>nancial operator who can integrate his/her experience and expertise by means of the support offered by the system.

## 6. Computational experience

The prototypal decision support system has been implemented on the high-performance computing system available at CESIC, a NEC supercomputing center at the University of Calabria. In particular, the computing platform is a NEC TX7 parallel supercomputer, with 32 Itanium-2 processors and 64 GB RAM.

As a test case, we have considered a horizon planning of one year with monthly rebalancing and a universe of 30 asset-classes of both Euro and US dollar currency areas. Historical values have been collected by DATASTREAM,<sup>6</sup> a large <sup>fi</sup>nancial statistical database.

Different instances have been generated by varying the number of scenarios. Table 1 reports problem size as function of the number of scenarios. In the same table, the last two columns report computational times required by the main modules, scenario generation and model formulation and solution.

The performance of the system has been fully investigated by a large set of numerical experiments aimed at evaluating the gain achieved both in terms of ef<sup>fi</sup>ciency and effectiveness. The following subsections present and comment the results.

## 6.1. Performance analysis

A <sup>fi</sup>rst set of computational experiments has been carried out to validate the proposed decision support system. For of all, we have evaluated the quality of the scenario generation technique by measuring the deviation of the underlying distribution moments from target values, computed on the basis of historical series. Fig. 9

## Scenarios

Reguest List >> Strategic Asset Allocation >> Dynamic Stochastic Solution

![](/api/attachments/TDAXGE88/fulltext/images/46bf5e24180ffca5fd91bc816018097a6cf68c3ce09aedee717b7313bdf353d2.jpg)

Month 2  
![](/api/attachments/TDAXGE88/fulltext/images/98f0ecf10b6ede1b27344106fe3abd8799569c574f20c341150a0c4e4c667757.jpg)  
Fig. 8. Solution statistics and scenario analysis.

shows the distance from targets for a portfolio with 5 asset classes. As evident, acceptable deviation values can be achieved with a limited number of scenarios. In addition, Fig. 10 shows the portfolio evolution along the scenario tree and real evolution, underlying how uncertainty in market conditions is well captured by the scenario tree representation.

Table 1 Test cases size.

<table><tr><td>Scenarios</td><td>Variables</td><td>Constraints</td><td>Non-zeros</td><td>Scenario generation (s)</td><td>CPLEX Solution (s)</td></tr><tr><td>27</td><td>3960</td><td>2631</td><td>15,123</td><td>19.8</td><td>57</td></tr><tr><td>64</td><td>8415</td><td>5556</td><td>36,444</td><td>35.2</td><td>81</td></tr><tr><td>125</td><td>15,444</td><td>10,171</td><td>82,205</td><td>63.8</td><td>106</td></tr><tr><td>216</td><td>25,641</td><td>16,866</td><td>176,904</td><td>101.2</td><td>180</td></tr><tr><td>343</td><td>39,600</td><td>26,031</td><td>363,279</td><td>147.4</td><td>310</td></tr><tr><td>512</td><td>57,915</td><td>38,056</td><td>710,228</td><td>182.6</td><td>597</td></tr><tr><td>729</td><td>81,180</td><td>53,331</td><td>1,322,169</td><td>292.6</td><td>1389</td></tr></table>

Other results have been collected to measure the so called “insample” stability [23], i.e. the sensitivity of the solutions provided by the model as function of the size of the scenario tree. In particular, for each size reported in Table 1 different trees have generated and the corresponding stochastic programming models have been solved. Fig. 11 shows for each instance the expected terminal wealth and the risk value. Here, the center of the circle represents the mean solution, while the radius measures the standard deviation. As expected, larger trees lead to more robust solutions, even though stable results can be obtained also for scenario trees of limited size.

Other experiments have been carried out to evaluate the effectiveness of the suggestions provided by the decision support system. To this aim a comparison with other portfolio optimization strategies has been performed. Fig. 12 reports ef<sup>fi</sup>cient frontiers (i.e. the set of non dominated portfolios) obtained by the SP approach and by the classical static Markovitz-like approach with the same risk measure, calculated on the same problem.

As expected, the SP strategy outperforms the buy and hold one providing more ef<sup>fi</sup>cient investment opportunities in terms of both pro<sup>fi</sup>tability and risk.

Furthermore, a back-testing analysis on real data has been carried out to evaluate the effectiveness of the allocation strategy suggested by the DSS with respect to other strategies. More speci<sup>fi</sup>cally, we have simulated the common behavior of a <sup>fi</sup>nancial operator consisting in periodic observations of real market evolution and the capital allocation among asset classes for the next period on the basis of new information available. Stochastic dynamic portfolio has been compared with the following policies:

• initial allocation without any optimization;

• “here&now” portfolio, that is the allocation at the initial stage suggested by our model;

![](/api/attachments/TDAXGE88/fulltext/images/9aaae9f1956f85a75dec872a799ed76a68f9e340a7ba346f2cd71b98b424ae26.jpg)  
Fig. 9. Simulations deviation from targets.

![](/api/attachments/TDAXGE88/fulltext/images/ad468b3a94c3022b2d4530ec3f00aa19981fc46527ce2234871004436c4c5b9b.jpg)  
Fig. 10. Scenario tree <sup>fi</sup>tting.

• “<sup>fi</sup>x-mix” strategy, which consists of periodic reallocation aimed at maintaining constant percentage on speci<sup>fi</sup>c asset classes;

• portfolio obtained with a myopic approach, which is de<sup>fi</sup>ned by means of the solution of a two-stage mathematical model for the entire planning horizon, based on the same scenario tree but without portfolio rebalancing.

Fig. 13 reports the portfolio's evolution in a <sup>fi</sup>nancial crisis period, from June 2008 to March 2009. The observation of real evolution of the initial portfolio (red line) clearly shows how static solutions can expose the investor to severe losses.

After the <sup>fi</sup>rst few months where the approaches show similar performance, it is clear how the dynamic stochastic approach (blue line) outperforms the other ones, allowing for substantial gains even in a <sup>fi</sup>nancial crisis context. The difference with the myopic strategy, the only one that as the proposed approach shows good performance, is due to the fact that the stochastic dynamic approach suggests initial decisions which not only take into account several market evolutions but also hedge against future adverse conditions.

## 6.2. Efficiency analysis

Final experiments have been carried out with the aim of evaluating the impact in terms of computational ef<sup>fi</sup>ciency deriving from the adoption of HPC systems. In particular, we have tested the performance of parallel versions of the most computational intensive modules of the system, i.e. the scenario generator and mathematical model generator and solver.

![](/api/attachments/TDAXGE88/fulltext/images/b0752186153a17bfa1c970fa1629559d0be8c47989fffe4cacf32e0e895c4e84.jpg)  
Fig. 11. Solutions stability.

![](/api/attachments/TDAXGE88/fulltext/images/b88cf1b8c5d4808af6cee7b7a2242eb75532e70f9d5ec0d5cca55cf39d2b390e.jpg)  
Fig. 12. Multistage stochastic approach vs Markovitz.

The scenario generation module has been parallelized considering a balanced partition of nodes of the scenario tree among available processors. This approach has been facilitated by the designed Monte-Carlo procedure which does not rely on the precedence relation among tree nodes. In fact, each processor computes asset returns for a subset of nodes and derives the corresponding asset prices by a log transformation. This parallelization approach requires a minimum level of communication among processors. Fig. 14 reports execution times for the scenario generator with a growing number of processors. As can be observed an almost linear speed-up can be achieved.

The parallelization of the model generator and solver relies on an embarrassing parallel approach: each parallel task consists of the same optimization model de<sup>fi</sup>ned for a given value of the risk aversion parameter λ, ranging from 0 to 1 with step 0.1. Fig. 15 depicts the model generator performance in terms of execution time as function of the number of processors.

Risk Neutral Out-of-Sample Ananlysis  
![](/api/attachments/TDAXGE88/fulltext/images/55e53dbe9b39668ed9d2e78e37641caa69446bc854fd2446dc6ba775d22ca325.jpg)  
Fig. 13. Strategies comparison.

![](/api/attachments/TDAXGE88/fulltext/images/c080c3e4bc765e16d9f8cd55b10de1164b6f0edaa32610efc3a448dd511e73fc.jpg)  
Fig. 14. Execution time of scenario generator.

It is worthwhile noting that further improvements can be obtained by implementing an ef<sup>fi</sup>cient (parallel) solution algorithm which can exploit both the particular structure of mathematical formulations and the potentialities of high performance computing. This aspect has not been addressed in the current version of the decision support system and it is the subject of ongoing research.

## 7. Conclusions

The paper presents an integrated approach to support <sup>fi</sup>nancial operators in the strategic asset allocation process. This is a crucial activity very dif<sup>fi</sup>cult to carry out because of the intrinsic stochastic and dynamic nature of the problem. In addition, the selection of a portfolio of <sup>fi</sup>nancial instruments has to generally satisfy a large number of constraints of different nature. Starting from the seminal contribution of Markowitz, a signi<sup>fi</sup>cant effort has been devoted by the scienti<sup>fi</sup>c community to propose sophisticated mathematical models able to encompass all the relevant features of the problem. Starting from static mathematical models based on the use of the variance as risk measure, dynamic and stochastic models based on the stochastic programming paradigm have been proposed. Particular attention has also been devoted to the choice of appropriate risk measures. However, the existing methodologies are not widely used in practice by <sup>fi</sup>nancial operators because they are too complex and require a lot of input data that should be preliminarily processed.

![](/api/attachments/TDAXGE88/fulltext/images/00cc0651925d78092677617508287e2be47c9c0023c7c4c67083c239ffe32fd6.jpg)  
Fig. 15. Execution time of model generator and solver.

The paper presents a DSS which implements sophisticated mathematical models and integrates simulation and optimization techniques. The complexities of the system core are hidden to the end-user that can access via web by a user-friendly interface. Comparison with other portfolio optimization strategies is also provided. This represents an important feature for a <sup>fi</sup>nancial operator who can capitalize his/her own expertise in the <sup>fi</sup>eld. In addition, the DSS has been designed to take advantage of the increased computational power offered by high-performance platforms. Besides a concurrent use of the system, the implementation on a HPC infrastructure allows to obtain more robust and reliable solutions in shorter times. Finally, the system can be easily modi<sup>fi</sup>ed to account for a wider class of decision problems of the ALM family and can be improved in terms of functionalities for a more general support to the investment planning activity.

## Appendix A. Economic and capital market model for scenario generation

The uncertainty related to the asset class indexes and interest rate evolution has been represented by means of a scenario tree as described in Section 3.3. In order to effectively model the correlated evolution among asset classes of different currency areas and the in<sup>fl</sup>uence of macroeconomic variables, a global capital markets model, originally proposed by Dempster et al. [2,14], has been adopted and customized.

It integrates two distinct models, one for the capital markets and one for the economic interaction. It is based on the de<sup>fi</sup>nition of the relation among a set of state variables for both the economic and the capital market model. In particular, the evolution of stock market index (S), short term interest rate (R), long term interest rate (L) and exchange rate (X), is modeled by means of simple diffusion equations:

$$
\frac {d S}{S} = (\alpha_ {s 1} + \alpha_ {s 2} S + \alpha_ {s 3} R + \alpha_ {s 4} L + \alpha_ {s 5} X) d t + \sigma_ {s} d Z _ {s}\tag{A.1}
$$

$$
\frac {d R}{R} = \left(\alpha_ {R 1} + \alpha_ {R 2} \frac {S}{R} + \frac {\alpha_ {R 3}}{R} + \alpha_ {R 4} \frac {L}{R} + \alpha_ {R 5} \frac {X}{R}\right) d t + \sigma_ {R} d Z _ {R}\tag{A.2}
$$

$$
\frac {d L}{L} = (\alpha_ {L 1} + \alpha_ {L 2} S + \alpha_ {L 3} R + \alpha_ {L 4} L + \alpha_ {L 5} X) d t + \sigma_ {L} d Z _ {L}\tag{A.3}
$$

$$
\frac {d X}{X} = \left(\alpha_ {X 1} + \alpha_ {X 2} \frac {S}{X} + \alpha_ {X 3} \frac {R ^ {F} - R}{X} + \alpha_ {X 4} \frac {L ^ {F} - L}{X} + \frac {\alpha_ {X 5}}{X}\right) d t + \sigma_ {X} d Z _ {X}\tag{A.4}
$$

where $\sigma _ { S } , \sigma _ { R } , \sigma _ { L }$ and $\sigma _ { X }$ are the standard deviations of the indexes at hand, the α coef<sup>fi</sup>cients are parameters which weight the dependence of each index from the other ones. In the exchange rate equation, $R ^ { F }$ and $L ^ { F }$ represent short and long term interest rates of the reference currency area.

The interaction of capital markets with the economy of major currency areas is represented by a model with four state variables, consumer price index (CPI), wages and salaries (WS), public sector borrowing requirement (PSB) and gross domestic product (GDP). These economic variables are supposed to in<sup>fl</sup>uence capital market variables according to a system of discrete time second-order autoregressive equations like the following:

$$
\begin{array}{l} \frac {S _ {t + 1} - S _ {t}}{S _ {t}} = \left(\alpha_ {S 1} + \alpha_ {S 2} S _ {t} + \alpha_ {S 3} R _ {t} + \alpha_ {S 4} L _ {t} + \alpha_ {S 5} X _ {t} + \beta_ {S 2} S _ {t - 1} \right. \\ \quad + \beta_ {S 3} R _ {t - 1} + \beta_ {S 4} L _ {t - 1} + \beta_ {S 5} X _ {t - 1} + \gamma_ {S 2} C P I _ {t} + \gamma_ {S 3} W S _ {t} \\ \quad + \gamma_ {S 4} G D P _ {t} + \gamma_ {S 5} P S B _ {t} + \delta_ {S 2} C P I _ {t - 1} + \delta_ {S 3} W S _ {t - 1} \\ \quad + \delta_ {S 4} G D P _ {t - 1} + \delta_ {S 5} P S B _ {t - 1}) + \sigma_ {S} Z _ {S} \end{array} \tag {A.}\tag{A.5}
$$

Here, β coef<sup>fi</sup>cients are similar to the α ones but related to the previous time period. Parameter γ and δ measure the in<sup>fl</sup>uence on the market index provided by macroeconomic variables, for current and previous time period respectively. Similar equations are de<sup>fi</sup>ned for the other state variables R, L, X for all currency areas. The overall equation system has linear parameters, which can be estimated using the seemingly unrelated regression (SUR) technique [18]. For a more accurate description we refer to the original contribution [14].

For the strategic asset allocation problem, this framework has been customized as follows. A model for a general set of asset classes has been de<sup>fi</sup>ned, by assigning each asset class to one of the relevant capital market indexes (S, R, L, X), according to the currency area it refers to. Speci<sup>fi</sup>c terms related to the correlations among the asset classes of the same group have been also included. For a “stock-like” asset class $i \in \varOmega _ { S } ,$ the evolution of its value $( V _ { i t } )$ can be modeled by means of the following equation, similar to A.5:

$$
\begin{array}{l} \frac {V _ {i , t + 1} ^ {S} - V _ {i , t} ^ {S}}{V _ {i , t} ^ {S}} = \left(\alpha_ {i 1} + \alpha_ {i 2} S _ {t} + \alpha_ {i 3} R _ {t} + \alpha_ {i 4} L _ {t} + \alpha_ {i 5} X _ {t} + \beta_ {i 2} S _ {t - 1} \right. \\ \qquad \qquad + \beta_ {i 3} R _ {t - 1} + \beta_ {i 4} L _ {t - 1} + \beta_ {i 5} X _ {t - 1} + \gamma_ {i 2} C P I _ {t} + \gamma_ {i 3} W S _ {t} \\ \qquad \qquad + \gamma_ {i 4} G D P _ {t} + \gamma_ {i 5} P S B _ {t} + \delta_ {i 2} C P I _ {t - 1} + \delta_ {i 3} W S _ {t - 1} \\ \qquad \qquad + \delta_ {i 4} G D P _ {t - 1} + \delta_ {i 5} P S B _ {t - 1} + \sum_ {j \in \Omega_ {S}} \eta_ {i j} (V _ {j, t}) + \sigma_ {i} Z _ {S} \end{array}\tag{A.6}
$$

Similar equations have been de<sup>fi</sup>ned for each asset class and allow simulation of the evolution of the entire asset class universe at each step of the scenario tree.

## Appendix B. Optimization model

As described earlier, a multistage stochastic programming model for the strategic asset allocation problem has been de<sup>fi</sup>ned. In order to limit the exposure to similar risk sources, each asset class has been included in one or more groups, or “families”, on the basis of main risk factors and speci<sup>fi</sup>c constraints have been de<sup>fi</sup>ned. In what follows the main features of this formulation are reported.

## Parameters

T planning horizon, articulated into elementary periods, $t { = } 0 , . . . , T { \ ; }$

N number of nodes of the scenario tree, $n { = } 0 , . . . , N ;$

M set of leaf nodes of the scenario tree;

I number of asset classes, $i = 1 , . . . , I ;$

J number of asset classes families, $j = 1 , . . . , J ;$

I<sub>j</sub> set of asset classes in family j;

$\pi _ { n }$ probability of occurrence of node n;

$\mathtt { a } _ { n }$ ancestor of node n;

C initial cash available;

$\overline { { z _ { i } } }$ initial holding in asset class i, at the beginning of the planning horizon;

$\Gamma _ { i n }$ simulated return of asset class i at node n;

$\Gamma _ { 0 n }$ simulated return of the risk free rate at node n;

$\mathrm { L } _ { i } , \mathrm { U } _ { i }$ lower and upper bound for the investment in asset class i;

${ \mathrm { H } } _ { j } ,$ B lower and upper bound for the investment in asset classes family j;

$\alpha _ { t }$ minimum return at period t;

λ risk aversion parameter.

## Decision variables

The model determines a sequence of investment decisions. In particular, rebalancing can be carried out at each node of the scenario tree by investment and disinvestment decisions. For each asset class i and each node n, the model includes the variables, $z _ { i n }$ representing the invested amount, and $x _ { i n }$ and $y _ { i n }$ denoting the amount added and disinvested, respectively. Furthermore, $f _ { n }$ denotes the amount invested in a risk-free asset at node n of the scenario tree.

## Objective function

The objective of the <sup>fi</sup>nancial planning is twofold: maximization of the expected wealth and minimization of the risk. In order to account for this con<sup>fl</sup>icting objectives, a mean–risk structure has been considered:

$$
\max (1 - \lambda) E _ {n \in M} [ W _ {n} ] - \lambda D _ {n \in M} [ W _ {n} ]\tag{B.1}
$$

where λ is a user-de<sup>fi</sup>ned parameter accounting for risk aversion attitude. The higher the value of λ the more conservative, but also the less pro<sup>fi</sup>table, the <sup>fi</sup>nancial planning.

The <sup>fi</sup>rst term of Eq. (B.1) is the expected value of <sup>fi</sup>nal wealth while the second one is a risk measure on the same quantity. The wealth associated to each node can be de<sup>fi</sup>ned as:

$$
W _ {n} = \sum_ {i = 1} ^ {I} z _ {i n} + f _ {n}\tag{B.2}
$$

As risk measure the Conditional Value at Risk (CVaR) for a certain con<sup>fi</sup>dence level $\beta$ (usually 95%) has been adopted. This is a modern formulation which w.r.t. the well-known Value at Risk allows a more accurate measure of tail losses and is a “coherent” measure [3], while maintaining good computational properties [1]. CVaR measures the expected value of losses exceeding VaR, as stated in formula B.3:

$$
\mathrm{CVaR} _ {\beta} = \xi_ {\beta} + \frac {1}{1 - \beta} \sum_ {n \in M} \pi_ {n} \left[ L _ {n} - \xi_ {\beta} \right] _ {+}\tag{B.3}
$$

where $\xi$ is the VaR at the same con<sup>fi</sup>dence level $\beta$ and $L _ { n }$ is the loss at leaf node n, which is computed as negative deviation of the portfolio wealth from the capitalized value of initial wealth $\widetilde { W } _ { n }$ (B.4).

$$
L _ {n} = \max \left[ 0, \widetilde {W} _ {n} - W _ {n} \right]\tag{B.4}
$$

This formulation is clearly non-linear. However, since the uncertainty within the model is represented by means of a <sup>fi</sup>nite set of realizations, the previous de<sup>fi</sup>nition can be easily linearized, using a set of auxiliary variables $\left( k _ { n } \right)$ and constraints (B.5–B.7), as following:

$$
\mathrm{CVaR} _ {\beta} = \xi_ {\beta} + \frac {1}{1 - \beta} \sum_ {n \in M} \pi_ {n} k _ {n}\tag{B.5}
$$

$$
k _ {n} \geq L _ {n} - \xi \quad \forall n \in M\tag{B.6}
$$

$$
k _ {n} \geq 0 \quad \forall n \in M\tag{B.7}
$$

For a detailed description of CVaR linearization we remind to [34].

## Constraints

Some constraints and requirements limit the <sup>fi</sup>nancial planning. First of all, a set of balance constraints on the amount invested in each asset-class, both at initial stage (B.8) and subsequent ones (B.9):

$$
z _ {i 0} = \bar {z} _ {i} + x _ {i 0} - y _ {i 0}
$$

$$
\forall i\tag{B.8}
$$

$$
z _ {i n} = z _ {i a _ {n}} (1 + r _ {i n}) + x _ {i n} - y _ {i n} \quad \forall i, \forall n\tag{B.9}
$$

Then, there is a set of <sup>fi</sup>nancial balance constraints, which impose the equilibrium between in<sup>fl</sup>ows and out<sup>fl</sup>ows (B.10), (B.11).

$$
\sum_ {i = 1} ^ {I} x _ {i 0} + f _ {0} = C + \sum_ {i = 1} ^ {I} y _ {i 0}\tag{B.10}
$$

$$
\sum_ {i = 1} ^ {I} x _ {i n} + f _ {n} = \sum_ {i = 1} ^ {I} y _ {i n} + f _ {a _ {n}} (1 + r _ {0 n}) \quad \forall n\tag{B.11}
$$

Furthermore, bound limits on the amount invested on each assetclass at each node of the scenario tree (B.12) have been included.

$$
L _ {i} W _ {n} \leq z _ {i n} \leq U _ {i} W _ {n} \quad \forall i, \forall n\tag{B.12}
$$

Similar conditions have been imposed on the amount invested on asset classes of the same family, in order to limit the exposure to the same risk factor (B.13).

$$
H _ {j} W _ {n} \leq \sum_ {i \in I _ {j}} z _ {i n} \leq B _ {j} W _ {n} \quad \forall j, \forall n\tag{B.13}
$$

Finally, classical nonnegative constraints limit the variable's values.

$$
\begin{array}{l} {z _ {i n}, x _ {i n}, y _ {i n} \geq 0} \\ {f _ {n} \geq 0} \end{array}
$$

∀i; ∀n

∀n

<sub>ð</sub>B:14<sub>Þ</sub>

<sub>ð</sub>B:15<sub>Þ</sub>

The overall model (B.1–B.15) belongs to the class of multistage stochastic programming problems with linear constraints and objective function. Real-life instances can be characterized by a very large size, so to require the adoption of ef<sup>fi</sup>cient solution methods, better if implemented on high-performance computing systems.

## References

[1] S. Ahmed, Convexity and decomposition of mean-risk stochastic programs, Mathematical Programming 106 (2006) 433–446.

[2] S. Arbeleche, M.A.H. Dempster, Econometric Modelling for Global Asset Liabilit Management, working paper 13/2003, University of Cambridge, 2003.

[3] P. Artzner, H. Delbaen, J.M. Eber, H. Heart, Coherent measures of risk, Mathematical Finance 9 (1999) 203–228.

[4] P. Beraldi, F. De Simone, A. Violi, Generating scenario trees: a parallel integrated simulation–optimization approach, Journal of Computational and Applied Mathematic 233 (9) (2010) 2322–2331.

[5] A. Berkelaar, J.A.S. Gromicho, R. Kouwenberg, S. Zhang, A primal-dual decomposition algorithm for multistage stochastic convex programming, Mathematical Programming: Series A and B.104 (1) (2000).153–177

[6] A. Berkelaar, R. Kouwenberg, Retirement saving with contribution payments and labor income as a benchmark for investments, Journal of Economic Dynamics and Control 27 (6) (2003) 1069–1097.

[7] H.K. Bhargava, D.J. Power, D. Sun, Progress in web-based decision support technologies, Decision Support Systems 43 (2007) 1083–1095.

[8] J.R. Birge, F. Louveaux, Introduction to Stochastic Programming, Springer, Heidelberg, 1997.

[9] G.C.E. Boender, A hybrid simulation/optimization scenario model for asset/liability management, European Journal of Operational Research 99 (1997) 126–135.

[10] D.R. Carino, T. Kent, D.H. Myers, C. Stacy, M. Sylvanus, A.L. Turner, K. Watanabe, W.T. Ziemba The Russell-Yasuda Kasai model: an asset/liability model for a Japanese insurance company using multistage stochastic programming, Interfaces 24 (1) (1994) 29–49.

[11] D.R. Carino, D.H. Myers, W.T. Ziemba, Concepts, technical issues and uses of Russell-Yasuda Kasai <sup>fi</sup>nancial planning model, Operations Research 46 (1994) 450–462.

[12] G. Consigli, Asset-Liability Management for Individual Investors, in: S.A. Zenios, W.T. Ziemba (Eds.), Handbook on Asset and Liability Management vol. B: Applications and Case Studies, North-Holland, Amsterdam, 2008.

[13] G. Consigli, M.A.H. Dempster, Stochastic programming for asset–liability management, Annals of Operation Research 81 (1998) 131–162.

[14] M.A.H. Dempster, M. Germano, E.A. Medova, M. Villaverde, Global asset–liability management, British Actuarial Journal 9 (2003) 137–216.

[15] N. Di Domenica, G. Mitra, P. Valente, G. Birbilis, Stochastic programming and scenario generation within a simulation framework: an information systems perspective, Decision Support Systems 42 (2007) 2197–2218.

[16] J. Dong, H.S. Du, S. Wang, K. Chen,X.Deng,A framework of web-based decision support systems for portfolio selection with OLAP and PVM, Decision Support Systems 37 (2004) 367–376.

[17] J. Gondzio, R. Kouwenberg, T. Vorst, Hedging options under transaction costs and stochastic volatility, Journal of Economic Dynamics and Control 27 (6) (2003) 1045–1068.

[18] J.D. Hamilton, Time Series Analysis, Princeton University Press, 1994.

[19] K. Høyland, S.W. Wallace, Using ALM in a Norwegian life insurance company, in: S.A. Zenios, W.T. Ziemba (Eds.), Handbook of Asset and Liability Management, North Holland, 2001.

[20] K. Hoyland, S.W. Wallace, Generating scenario trees for multistage decision problems, Management Science 47 (2) (2001) 295–307.

[21] T.H. Hultberg, FLOPC++ an algebraic modelling language embedded in C++, in: K.H. Waldmann, U.M. Stocker (Eds.), Operations Research Proceedings, Springer, Heidelberg, 2006.

[22] P. Kall, S. Wallace, Stochastic Programming, Wiley, Chichester, 1994.

[23] M. Kaut, S. Wallace, Evaluation of scenario generation methods for stochastic programming, Paci<sup>fi</sup>c Journal of Optimization 3 (2) (2007) 257–271.

[24] J. Kim, Event tree based sampling, Computers & Operations Research 33 (5) (2006) 1184–1199.

[25] R. Kouwenberg, S.A. Zenios, Stochastic programming models for asset liability management, in: S.A. Zenios, W.T. Ziemba (Eds.), Handbook of Asset and Liability Management, North Holland, 2001.

[26] C.D. Maranas, I.P. Androulakis, C.A. Floudas, A.J. Berger, J.M. Mulvey, Solving long-term <sup>fi</sup>nancial planning problems via global optimization, Journal of Economic Dynamics and Control 21 (1997) 1405–1425

[27] H.M. Markovitz, Portfolio selection, The Journal of Finance 7 (1952) 77–91.

[28] R.C. Merton, Lifetime portfolio selection under uncertainty: the continuous-time case, The Review of Economics and Statistics 51 (1969) 247–257

[29] J. Mossin, Optimal multiperiod portfolio policies, Journal of Business 41 (1987) 215–229.

[30] G.P. Moynihan, P. Purushothaman, R.W. McLeod, W.G. Nichols, DSSALM: a decision support system for asset and liability management, Decision Support Systems 33 (2002) 23–38.

[31] J.M. Mulvey, G. Gould, C. Morgan, An asset and liability management system for Towers Perrin-Tillinghast, Interfaces 30 (2000) 96–114.

[32] J.M. Mulvey, W.T. Ziemba, Worldwide Asset and Liability Modelling, Cambridge University Press, 1998.

[33] M. Pirbhai, G. Mitra, T. Kyriakis, Asset liability management using stochastic programming, in: B. Scherer (Ed.), Asset and Liability Management Tools. A Handbook for Best Practice, 2003, pp. 95–308.

[34] R. Rockafellar, S. Uryasev, Optimization of conditional value at risk, Journal of Risk 2 (2000) 21–41.

[35] B. Rustem, N. Gulpinar, R. Settergren, Simulation and optimization approaches to scenario tree generation, Journal of Economic Dynamics and Control 28 (2004) 1291–1315.

[36] S.W. Wallace, W.T. Ziemba (Eds.), Applications of Stochastic Programming, MPS-SIAM Series in Optimization, 2005.

[37] W.T. Ziemba, The Stochastic Programming Approach to Asset, Liability and Wealth Management, AIMR, Charlottesville Virginia, 2003.

[38] W.T. Ziemba, J.M. Mulvey (Eds.), Worldwide Asset and Liability Modeling, Cambridge University Press, Cambridge, 1998.

![](/api/attachments/TDAXGE88/fulltext/images/7c733ac687a9f7038b6027cb3cbbaf87512d3d3544a1066620e16718987fafa8.jpg)

Patrizia Beraldi was born in Cosenza, Italy, on March 7, 1969. She is an Associate Professor of Operations Research at the Faculty of Engineering, University of Calabria, Italy. She is the head of the research unit on quantitative <sup>fi</sup>nance at the Supercomputing Centre for Computational Engineer of the University of Calabria. Her research interests mainly concern the de<sup>fi</sup>nition of models and methods for speci<sup>fi</sup>c classes of mathematical programming problems with applications in <sup>fi</sup>nance, energy and health care. She is the author of more than 30 papers appeared on prestigious international journals.

![](/api/attachments/TDAXGE88/fulltext/images/da7d8974b47c5eee4d588b3bc7dbfe7ca19cfd8cf4eb6ad1aa78de12787ac739.jpg)

Antonio Violi was born in Reggio Calabria, Italy, on August 23, 1974. He received the degree in Management Engineering from University of Calabria in 2001 and the PhD in Operations Research in 2006 at the Electronic, Computer and Systems Science Department of University of Calabria, Italy. He is a senior engineer at the Supercomputing Centre for Computational Engineer at the University of Calabria. His current research interests concern the design of quantitative methods in <sup>fi</sup>nance and energy markets. He is the author of more than 10 papers published by international journals.

![](/api/attachments/TDAXGE88/fulltext/images/eb18ce169da35007a5936b29c4e3e52b65c7b68a69fb1ceff4d8aa3e90592342.jpg)

Francesco De Simone was born in Corigliano Calabro (CS), Italy, on May 31, 1980. He received the degree in Physics from University of Calabria in 2006 and a Master degree in Computer Science in 2008 at University of Calabria, Italy. He is currently a Ph.D. student in Operations Research at the Department of Electronics. Informatics and Systems of University of Calabria. His current research interests concern the design of models and algorithms for quantitative <sup>fi</sup>nance.
