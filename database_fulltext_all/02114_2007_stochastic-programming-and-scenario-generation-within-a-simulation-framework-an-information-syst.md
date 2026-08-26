---
otero_id: 2114
otero_key: "MP8UXUNQ"
title: "Stochastic programming and scenario generation within a simulation framework: An information systems perspective"
authors: "Nico Di Domenica; Gautam Mitra; Patrick Valente; George Birbilis"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.06.013"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Stochastic programming and scenario generation within a simulation framework: An information systems perspective

Nico Di Domenica <sup>⁎</sup>, Gautam Mitra, Patrick Valente, George Birbilis

CARISMA, School of Information Systems, Computing and Mathematics, Brunel University, Uxbridge, UB8-3PH, UK

Received 19 July 2004; received in revised form 18 June 2006; accepted 21 June 2006 Available online 10 August 2006

## Abstract

Stochastic programming brings together models of optimum resource allocation and models of randomness to create a robust decision-making framework. The models of randomness with their finite, discrete realisations are called scenario generators. In this paper, we investigate the role of such a tool within the context of a combined information and decision support system. We explain how two well-developed modelling paradigms, decision models and simulation models can be combined to create “business analytics” which is based on ex-ante decision and ex-post evaluation. We also examine how these models can be integrated with data marts of analytic organisational data and decision data. Recent developments in on-line analytical processing (OLAP) tools and multidimensional data viewing are taken into consideration. We finally introduce illustrative examples of optimisation, simulation models and results analysis to explain our multifaceted view of modelling. In this paper, our main objective is to explain to the information systems (IS) community how advanced models and their software realisations can be integrated with advanced IS and DSS tools.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Scenario generation; Stochastic programming; DSS; OLAP; Business analytics; Simulation

## 1. Introduction and motivations

## 1.1. Role of business analytics within organisational IS

Two basic modelling paradigms come together in stochastic programming (SP). These are: (a) model of optimum resource allocation and (b) model of randomness respectively. It is well established that in the realm of OR/MS and its contribution to managerial decisionmaking four categories of models are of interest. For a detailed discussion, see Mitra [55]: (I) Descriptive models as defined by a set of mathematical relations, which simply predicts how a physical, industrial or a social system may behave. (II) Normative models constitute the basis for (quantitative) decision-making by a superhuman following an entirely rational that is, logically scrupulous set of arguments. Hence, quantitative decision problems and idealised decision-makers are postulated in order to define these models. (III) Prescriptive models involve systematic analysis of problems as carried out by normally intelligent persons who apply intuition and judgement. Two distinctive features of this approach are uncertainty analysis and preference (or value or utility) analysis. (IV) Decision models are in some sense a derived category as they combine the concept underlying the normative models and prescriptive models. Within the organisational context, the deployment of such models and their role in the IS infrastructure is recognised as “business analytics”. Optimisation-based decision support systems (DSS) are assuming an increasingly important role in many industries and public organisations. Optimisation modelling and solution techniques have seen sustained developments from the early sixties until now. The main achievements have come from the improvements in model conceptualisations, solution algorithms and software techniques. Optimisation models are considered as critical components of an organisation's analytical information technology (IT) systems, as they are used to analyse and control critical business measures such as cost, profit, quality and time. In the context of organisational information systems (IS) (Koutsoukis and Mitra [47]), quantitative models constitute an important component within the information value chain (IVC). Typically, transactional (operational) data, which is available in a firm, is analysed and synthesised to create analytic data or information, which is the first link of the information value chain. The analytic data is stored in data marts, which are subsets of the overall collection of data within a firm and is called data warehouse (Fig. 1).

In this context, optimisation models and the tools, which enable their formulation and solution, are considered to be inference engines, which support decisionmaking. They operate on the analytic data stored in the data marts to provide decision-makers with decision data, which is inferred from the models. Optimisation models can also be used within the more general framework of simulation, enabling decision-makers and analysts to take advantage of descriptive models as well as prescriptive models.

## 1.2. Optimum decision-making under uncertainty

Optimum decision-making concerns a class of problems where it is necessary to make decisions to optimise one or more given objectives, subject to appropriate restrictions. Mathematical programming (MP) models have made considerable contribution to optimum decision-making, as they enable the modeller to capture the structure of the problem and to quantify the effects of the decisions in terms of the objectives of the problem owner also known as the decision-maker. The future, due to its very nature, is naturally uncertain. When using LP or IP for optimum decision-making, modellers are required to analyse the available historical data in order to identify the parameters, which are to be considered in the model. Aggregation and estimation intervene in this important phase of the LP/IP modelling process. In many situations, the parameter values do not remain constant and are variable or “volatile”. The class of problems for which the assumption of a deterministic world (that is, model parameters are known exactly) is relaxed and often referred to as optimum decision-making under uncertainty, since some, if not all, the model parameters may be uncertain. In these cases, the modeller needs to take into account the effects induced by uncertainty into the underlying optimisation models. An early approach in the investigation of these effects was the use of sensitivity analysis. Unfortunately, as shown in Higle and Wallace [34], this approach shows a number of limitations, and may provide misleading conclusions in respect of the nature of the solutions. In general, sensitivity analysis is not a suitable approach for understanding the effects of random behaviour of the model parameters. In many real world problems, the uncertainty relating to one or more parameters can be modelled by means of probability distributions. In essence, every uncertain parameter is represented by a random variable over some canonical probability space; this in turn provides a representation of the uncertainty. Stochastic programming (SP) enables modellers to incorporate this quantifiable uncertainty into an underlying optimisation model. Stochastic programming models combine the paradigm of optimum resource allocation with modelling of random parameters, providing optimal decisions which hedge against future uncertainties (Fig. 2).

![](/api/attachments/MP8UXUNQ/fulltext/images/2499f81a5bdf6390e9073c6d9a7e32312d4ef983ba47ffe83f60a5cbeca55f82.jpg)  
Fig. 1. The information value chain.

![](/api/attachments/MP8UXUNQ/fulltext/images/67f4bfa907f01db76b2d5015b7febd2285237ccd38a8d0d918aa5db095633f9c.jpg)  
Fig. 2. Breakdown of stochastic programming.

## 1.3. Applications of stochastic programming

The successful application of linear [12] and integer programming models to decision problems in their turn have opened up the scope of applying SP models in decision-making where time and uncertainty affect the decisions. Moreover advances in hardware as well as software techniques and solution methods have made SP a viable optimisation tool for decision-making under uncertainty. Finance [51,52] and supply chain planning are typical areas where deterministic optimisation models have proven to be extremely inadequate since the model parameters are by their very nature uncertain. Financial planning [40,43,50], supply chain management [1,22], transportation logistics [28,29,62,63], telecommunications, network design [23], environmental planning and energy systems planning are the main application areas of SP. A detailed discussion of these applications is given in Di Domenica et al. [16].

## 1.4. Modelling systems, database and constituents

Whereas in Section 1.2, we have highlighted the importance of optimisation within an organisational IS here we consider a modelling perspective. In the different stages of the optimisation process, various constituents undertake different roles and interact with each other. These constituents and their interaction are set out in Fig. 3.

The technical experts (modelling experts, database experts, solver experts and domain experts, depending on their expertise) have access to all system components including the underlying models, databases and solver tools. The different technical experts collaborate to create a domain-specific application by integrating the different tools for the different stages of the process. The decisionmaker(s) are the constituents that utilise the (application) system. Typically, the decision-makers have access to the data and solution analysis routines available in the database, and use the underlying models and data as a black box. Thereafter, they analyse and report the results that are in the analytic database. Accordingly, there is a need to have integrated optimisation tools for all the constituents involved. The architecture is centred on the (algebraic) modelling systems, which process one or more algebraic models and the analytical data in order to generate a model instance. The instance is then passed onto the solvers (which implement one or more of solution algorithms). These optimise the model instance and return the values of the optimum decisions and objective (decision data) to the modelling system, which in turn stores them into the database. The components are typically controlled by a graphical user interface (GUI) [32].

![](/api/attachments/MP8UXUNQ/fulltext/images/9cb6c5735c07739fed9d64b0fa94a5ca2c9fe654aaecb1938b266a820b7640a9.jpg)  
Fig. 3. Optimisation process and constituents.

## 1.5. Guided tour

The rest of this paper is organised in the following way. We provide a short introduction to stochastic programming in Section 2, which also includes a list of the available software tools for SP. This section is complemented by an explanation of relevant model definitions and stochastic measures in Appendix A. In Section 3, we first give an overview of organisational information system and position the roles of analytic database and multidimensional database including online analytical processing (OLAP) views. The connection of IS to our decision modelling and description modelling methods is essential, as this enables the embedding of models within business analytics, business processes or business rules as appropriate. In Section 4, we provide a high level conceptual architecture of the integrated system. We consider the role of scenario generation and scenario trees and how these relate to the SP decision model. The use of algebraic modelling languages (AMLs) to formulate optimisation models and the extensions of AMLs to construct SP models are discussed and the integrated system is introduced in a summary form. In Section 5, we illustrate our combined modelling framework of decision-making followed by evaluation through simulation using an illustrative case study. We describe an asset liability management (ALM) model. For the purpose of generating scenarios, we outline a multistage extension of moment matching approximation. We then consider the results of the decision model obtained by computing the solutions of the expected value, here-and-now (for both two-stage and multistage) formulation of the ALM problem. These first stage decisions are then fixed to create simulation runs for the wait-and-see model and the frequency distribution of the objective solution values are computed. We discuss the in-sample stability of a scenario generation method, and present, stochastic measures and risk measures (VaR and

CVaR) are presented as obtained by the simulation. Our conclusions are presented and discussed in Section 6.

## 2. Stochastic programming

## 2.1. Background to $S P$

Stochastic programming is now a well-established mathematical programming paradigm [17], which explicitly incorporate uncertainty in the form of probability distributions of some parameters. These models can be further categorised taking into account the way in which such uncertainty is expressed and dealt with in the underlying linear optimisation model. The classification of stochastic programming problems leads to a working taxonomy shown in Fig. 4. We restrict our discussions to the linear case only although the taxonomy is equally applicable to non-linear programming (NLP) problems.

These problem classes can be illustrated by first considering the linear programming problem:

$$
\begin{array}{l} Z = \operatorname * {m i n c} x \\ \text { subject   to } A x = b \\ \qquad \qquad \qquad x \geq 0 \\ \qquad \text { where } A \in R ^ {m \times n}; c, x \in R ^ {n}; b \in R ^ {m} \end{array}
$$

Let (Ω, I, P) denote a (discrete) probability space where ξ(ω), ω ∈ Ω denote the realizations of the uncertain parameters. Let the realizations of A, b and c for a given event ω be defined as: ξ(ω) or $\xi _ { \omega } = ( A , b , c ) _ { \omega } .$ The associated probabilities of these realizations are often denoted as p(ξ(ω)) or $p _ { \xi ( \omega ) }$ . For notational convenience, these probabilities are denoted simply as p(ω).

## 2.1.1. Distribution problems

The optimisation problems, which provide the distribution of the objective function value for different realisations of the random parameters and also for the expected value of such parameters, are broadly known as the “distribution” problems. The terminology is based on the consideration that the statistical distribution(al) property of the objective value can be computed through these models.

![](/api/attachments/MP8UXUNQ/fulltext/images/b97cc6f2895c2f0873c9ead0e841e7b46c0da3f0c0bb371d754bbe953e21f250.jpg)  
Fig. 4. Taxonomy of SP problems.

2.1.1.1. Expected value problem. The expected value (EV) model is constructed by replacing the random parameters by their expected values. Such an EV model is thus a linear program, as the uncertainty is dealt with before it is introduced into the underlying linear optimisation model. It is common practice to formulate and solve the EV problem in order to gain some insight into the decision problem.

2.1.1.2. Wait-and-see problems. Wait-and-see (WS) problems assume that the decision-maker is somehow able to wait until the uncertainty is resolved before implementing the optimal decisions. This approach therefore relies upon perfect information about the future. Because of its very assumptions such solution cannot be implemented and is known as the “passive approach”. Wait-and-see models are often used to analyse the probability distribution of the objective value and consist of a family of LP models, each associated with an individual scenario.

## 2.1.2. Recourse problems

2.1.2.1. Here-and-now problems. Assuming Z as solution of the objective functions, simple (single stage) stochastic programming model can be formulated as follows:

$$
Z _ {H N} = \min E [ c (\omega) x ] \text {   where   } x \in F
$$

and $F = \bigcap _ { \omega \varepsilon \Omega } F ^ { \omega }$

The optimal objective function value $Z _ { H N }$ denotes the minimum expected costs of the stochastic optimisation problem. The optimal solution $x ^ { * } \in F$ hedges against all possible events $\omega { \in } \varOmega$ that may occur in the future.

A description of the here-and-now problems can be found in Appendix A, together with the uncertainty measures: value of the stochastic solution (VSS) and the expected value of perfect information (EVPI). For essential terminology and definitive SP models, the readers are referred to CARISMA SP workshop notes [8], Infanger [38] and Birge and Louveaux [3].

## 2.2. SP software tools

The algebraic modelling languages (AML) have played an important role in the acceptance of mathematical programming techniques as an aid to decisionmaking. AMLs are declarative languages, which enable practitioners to rapidly build structured, and scalable optimisation models. Modern systems based on algebraic modelling languages support the formulation and implementation of linear programming (LP), mixed integer programming (MIP), quadratic programming (QP) and to some extent non-linear programming (NLP) models. These systems are readily connected to linear or nonlinear optimisers for the solution of the models under investigation, and are able to interact with corporate data warehouses [45] and data marts stored in relational, object oriented or in other emerging standards. Until recently, however, the investigation of stochastic programming models could not take advantage of comparable tools. In fact, the practical exploitation of SP presents various difficulties, which affect the whole process of modelling, instantiation, solution and analysis of the results of SP problems. Recently, there has been considerable progress in the development and application of SP.

We have provided reference to a comprehensive list of working SP systems in Table 1, since there is an ongoing development we might have omitted some new systems; for up to date information, the readers are referenced to the excellent website hosted by the committee on stochastic programming (COSP: www.stoprog.org). Of the 12 systems set out in Table 1, only SPInE and its extensions, as described in this paper, provides the two phase modelling paradigm: through the connectivity with the data mart, we are able to store, extract and analyse both the decision data and the simulation data.

Table 1  
SP software tools

<table><tr><td>Name</td><td>Affiliation</td><td>System name</td><td>Type</td></tr><tr><td>JJ Bisshop et al. [5]</td><td>Paragon Decision Tech.</td><td>AIMMS</td><td>Modelling system</td></tr><tr><td>A Meeraus et al. [53]</td><td>GAMS</td><td>GAMS</td><td>Modelling system</td></tr><tr><td>B Kristjansson [49]</td><td>Maximal Software</td><td>MPL</td><td>Modelling system</td></tr><tr><td>R Fourer et al. [24]</td><td>Northwestern University</td><td>AMPL</td><td>Modelling system</td></tr><tr><td>MAH Dempster et al. [14]</td><td>Cambridge University</td><td>STOCHGEN</td><td>Modelling system</td></tr><tr><td>E Fragniere et al. [25]</td><td>University of Geneva</td><td>SETSTOCH</td><td>Modelling system</td></tr><tr><td>A King et al. [46]</td><td>COIN-OR</td><td>SMI</td><td>Solver</td></tr><tr><td>HI Gassmann et al. [27]</td><td>Dalhousie University</td><td>MSLiP</td><td>Solver</td></tr><tr><td>G Infanger et al. [37]</td><td>Stanford University</td><td>DECIS</td><td>Solver</td></tr><tr><td>P Kall et al. [41,42]</td><td>University of Zürich</td><td>SLP-IOR</td><td>Modelling system/solver</td></tr><tr><td>G Mitra et al. [67, 69]</td><td>Brunel University</td><td>SPInE</td><td>Modelling system/solver</td></tr><tr><td>R Daniel et al. [11]</td><td>Dash Optimisation</td><td>Dash/ XpressMP</td><td>Modelling system/solver</td></tr></table>

## 3. Information systems components

3.1. Transactional data, analytic data and information value chain

In an organisational context, the role of the information system has become well established. In general, data across the organisation is classified in two groups, namely transactional data and analytic data. Typically, the transactional database system is optimised for performance and efficiency rather than supporting analytical features. In contrast, the analytical database is carefully prepared for exploitation and decision support (Berson and Smith [2]). Analytic data is usually stored in data warehouses; these repositories of subject oriented integrated and non-volatile information is aimed at supporting the knowledge analyst to make better and faster decisions. The data in the warehouse are modelled as a multidimensional item; this approach facilitates the query engines to aggregate data across many dimensions in order to detect trends. We take a particular perspective of data and infrastructure in our modelling system. This view is called the information value chain (IVC) paradigm that commences with the analysis and synthesis of transactional data to create analytic data or information, which is the first step in the information value chain (Fig. 5).

Quantitative models constitute an important component within the IVC (Koutsoukis and Mitra [47]). Optimisation models are used within the framework of simulation, enabling the analysts to take advantage of descriptive models as well as prescriptive models. An important aspect of IVC is that the decision data, which is created by the optimisation models, is itself analytic data, and can therefore be fed into the chain again. As an example of the importance of IVC, we can observe the use of prescriptive (optimisation) models to obtain a set of optimum decisions, which are then used as input for a descriptive (simulation) model for risk analysis under alternative scenarios. The term decision database [39] denotes the collection of data repositories that are used for decision support applications. We use the term decision database to denote data marts [13] that are used to store the results of our model-driven investigations. For instance, a decision-maker or an end-user is typically interested in working with the optimisation results, in order to proceed with the decision-making process. In this case, it is easily seen that the decision-making process is very much related to the ‘new’ information, namely the optimisation results. Hence, a decision database requires some of form medium-term storage for the inferred information generated by the optimisation models. Data modelling, decision modelling and model investigation are logical steps, which play a leading role both in the interaction of information systems and decision technologies; taken together, they lead to business analytics. It is easily seen that data modelling and decision modelling closely interact with each other. The following list describes these logical constructs and their relationship to knowledge.

![](/api/attachments/MP8UXUNQ/fulltext/images/ff777bbf08c10f0214ce182bd94de953c0f36ca49f623f17a21092c966df9ae8.jpg)  
Fig. 5. Information value chain.

• Data modelling refers to the ‘structured’ internal representation and external presentation of recorded facts. Broadly speaking this provides the decisionmaker with information about their decision problem.

• Decision modelling is the development of a model, or a range of models that captures the structure as well as the decisions in respect of a given problem. These models are used to evaluate possible decisions (actions) in a given problem domain and the probable outcomes of these actions.

• Model analysis and investigation refers to the instantiation of the model with data, and the evaluation of the model parameters as well as the results in order to gain confidence and insight into the model.

Typically, data modelling involves defining relationships between data items leading to a relational data model, or identifying categories that are then used to define multidimensional tables, leading to a multidimensional data model. Decision modelling involves the development of models that are used for decision-making. Model analysis and investigation is often a descriptive analysis of the results obtained which is applied to gain insight, or knowledge with respect to a given decision problem.

## 3.1.1. The decision database

It is easily seen that for any given decision support system, data models, symbolic models and algorithmic tools interact. In many optimisation-based DSS, there exists an inherently strong coupling of data models, symbolic models and algorithms, also called an inference engine (Shapiro [66]). In general, one can consider the decision database as a data mart, in which the data models provide information about the problem at hand, decision models describe the decision problem, or the known relationships between the known information, and the algorithms generate the set of optimal, or near optimal “solutions” for the problem at hand. In stochastic programming applications, the decision database may consist of three main types of information: deterministic information (or information invariable to the uncertainty of the future), stochastic information (possible characteristics of future uncertainty and the information that is subject to that uncertainty), as well as the solutions (possible courses of action in the uncertain future). Further, it will include different solutions from different solving methods for a particular problem (output results, e.g., ‘wait-and-see’ scenario analysis and ‘here-and-now’ solutions). To summarise an optimisation-based DSS is an application-specific information systems, consisting of database tools, algebraic modelling tools and algorithmic (‘solving’) tools, with additional analytical tools, which are often used to provide further insight into the problem at hand. These additional analytical tools may consist, for example, of (relational) online analytical processing (R)OLAP tools which can help an analyst achieve a fast and descriptive overview of the data, in order to study the problem and make appropriate reports. In Section 4.4, we revisit some of these aspects to illustrate how this relates to our combined SP and simulation framework.

## 3.2. OLAP: multidimensional view and data cube

Since the inception of the term OLAP (Codd et al. [9]), the technology is recognized as a promising approach for the analysis and navigation of data warehouses and multidimensional data. OLAP systems enable powerful decision support based on multidimensional analysis of large amounts of summary data commonly drawn from a number of different transactional databases. OLAP's multidimensional data model and data aggregation techniques organize and summarize large amounts of data to facilitate quick evaluation using online analysis and graphical tools. In this section, we will discuss the data operators that we use to generate our set of numeric summary tables corresponding to a given aggregation hierarchy. The OLAP data are organized in multidimensional cubes containing measured values that are characterized by a number of hierarchical dimensions. The typical operations on data cubes include roll-up (increasing the level of aggregation), drill-down (decreasing the level of aggregation or increasing detail) along one or more dimension hierarchies, slice-and-dice (selection and projection) and pivot (re-orienting the multidimensional view of data). For a detail discussion on these operations, see Codd et al. [9] and Koutsoukis and Mitra [47]. Data warehouses and related OLAP technologies continue to receive strong interest from the research community as well as from industry, since OLAP tools present their users with a multidimensional perspective of the data and facilitate the writing of reports involving aggregations along the various dimensions of the data set. The multidimensional approach offers a number of advantages over traditional types of database management systems (DBMSs), including automatic application of the pre-specified aggregation functions (automatic aggregation) (Rafanelli and Shoshani, [64]), visual querying and good query performance due to the use of pre-aggregation (Gupta et al. [31] and Pedersen and Jensen [58]). Additionally, the multidimensional approach is a natural fit for data analysis problems. To be able to capture the complex data found, the data model for the OLAP system is able to handle irregular dimension hierarchies that do not fit the balanced-tree hierarchies (Pedersen and Jensen [58]). In general, OLAP cubes are a multidimensional representation of data, in which each attribute of a given data entity is considered as a separate dimension. For our purpose, an OLAP data cube consists of a lattice of cuboids each of which represents a certain level of hierarchy. The cube's aggregate functions compute statistics for a given set of values within each cuboid. Table 2 shows alternative aggregate functions, which can be grouped into three categories namely: distributive, algebraic and holistic (Gray [30]).

In a traditional SQL relational database, aggregate functions and the GROUP BY operator function only produce one out of N aggregates at a time. An OLAP data cube is an aggregate operator, which computes all $N ,$ aggregates in one shot. The ability of OLAP to support multidimensional data makes it naturally suitable as a viewing and analysis tool for decision support systems, which are based on multistage stochastic programming models. Indeed, as discussed in Section 2, the uncertain parameters of these models as well as the eventdependent optimum decisions are usually represented by at least two dimensions, namely the time and the scenarios. As an example, consider the problem of generating and representing a number of possible future prices of a set of assets [6,7,10] for a given number of time periods, Figs. 6, 7 and 8 also show how the input data used in the case study in Section 5 can be represented through OLAP technique. In Section 4, we describe how these values (analytic data) are computed by processing transactional (in our case: market) data using scenario generators. A relational table, which contains these data, should have at least the following fields, where the first three taken together define a primary key: asset, period, scenario and price. In other words, we have a price for each triplet (asset, period, scenario). Using an OLAP cube, the data can be aggregated (rolled-up) or disaggregated (drilled-down) to obtain progressively summarised information or increasing detailed information respectively. This is illustrated in Fig. 6.

Table 2  
Aggregate functions for OLAP data cube

<table><tr><td></td><td colspan="3">Aggregation function</td></tr><tr><td>Data type</td><td>Distributive function</td><td>Algebraic function</td><td>Holistic function</td></tr><tr><td>Set of numbers</td><td>Count, min, max, sum</td><td>Average, standard deviation</td><td>Median, rank, most frequent</td></tr></table>

The 0D cube is obtained by rolling up all three dimensions asset, period and scenario. Using average as the aggregate function, we obtain a single scalar, which is the “average price of all period, of all scenarios and for all assets”. By drilling down this cube along one dimension, we obtain 1D cubes (one per dimension) which in our example contain: (a) the average asset price for each asset calculated over all periods and scenarios, (b) the average asset price for each period calculated over all assets and scenarios, and (c) the average asset price for each scenario calculated over all assets and periods. By applying the drill-down procedure to a 1D cuboid, we obtain a 2D cuboid and so on, until we expand all dimensions and obtain the full detailed data (in this case, a 3D cuboid). Besides roll-up and drill-down, the slice and dice operations also enable OLAP users to create cuboids of smaller dimensions. Slicing into one dimension is very much like drilling one level down into that dimension but the number of entries displayed is limited to that specified in the slice command. A dice operation is like a slice on more than one dimension. Slicing and dicing therefore lead to a view in which only a subset of the data is shown. When the data is represented in 1D or 2D cuboids, it can also be visualised using 2D or 3D graphs. For instance, the 2D cuboid obtained by slicing into the asset dimension (selecting the data pertaining to one single asset) is shown in Fig. 7. The 3D graph represents the price for a given asset in all time periods and for all scenarios. Some of the scenario data paths are highlighted.

A 2D graph with multiple series can also be used to display a 2D cuboid. For instance, Fig. 8 shows the transactional (market) data used to generate the scenarios used in the previous examples.

## 4. Integrating scenario generation and SP software tools

## 4.1. Scenario trees

Two-stage stochastic programs with recourse (see Section 2) when stated explicitly take the form of large linear programs of a special structure, which capture the realisations of the random parameters. In the two-stage case, let represent $\xi$ the vector of all random parameters

3 - D Data Cube  
![](/api/attachments/MP8UXUNQ/fulltext/images/f7027498719adbbd08bfea2cf27b7818ae215d2999d2b08e9d9ec751bbdd88e1.jpg)

![](/api/attachments/MP8UXUNQ/fulltext/images/5e4acc46148f3a98a5ba6d72e4ee4fda73df0e693965b4ad84de26eadac78c66.jpg)  
0 - D Data Cube

![](/api/attachments/MP8UXUNQ/fulltext/images/73bba8ecea0629e6680b347fb1b10362fea3e1fba0ea19ee58e2d68a7a868fa0.jpg)  
1 - D Data Cube

2 - D Data Cube

![](/api/attachments/MP8UXUNQ/fulltext/images/fb58a8ec8adc118f99c9858dbd58a715c028b76ee4df33c8ff4016b0bcf6b1a1.jpg)  
Fig. 6. OLAP cuboids.

in a model. The probability distribution of $\xi$ is assumed to be discrete with a finite number of realisations $\xi _ { k } .$ . The probability of each realisation is defined as:

$$
p _ {k} = P \left(\xi_ {k}\right) \text {   for   } k = 1.. K \text {   where   } p _ {k} \geq 0 \text {   and   } \sum_ {k = 1} ^ {K} p _ {k} = 1
$$

For multistage stochastic programming, one assumes that the random vector $\xi$ follow a stochastic process $\xi _ { t }$ over the planning horizon. If the process is assumed to be discrete, with probability $P ( \xi _ { t } )$ , the uncertainty can be represented through a multilevel event tree, which defines the possible sequence of realizations, also known as data paths. In general, these are called scenarios over the whole planning horizon, see Fig. 10. Levels in the tree are associated to decision stages. In particular, if we denote $N _ { t }$ the set of nodes at the t the level, then each node $n \in N _ { t }$ represents a particular realization sequence of the data process and it can be thought as a particular state of the system at a given time. A probability $\pi _ { n }$ can be associated with each node n at level t such that:

<table><tr><td>Asset</td><td>Period</td><td>Scenario</td><td>Price</td></tr><tr><td>ALL</td><td>ALL</td><td>ALL</td><td>5.15</td></tr></table>

<table><tr><td>Asset</td><td>Period</td><td>Scenario</td><td>Price</td></tr><tr><td>1</td><td>ALL</td><td>ALL</td><td>0.24</td></tr><tr><td>2</td><td>ALL</td><td>ALL</td><td>10.162069</td></tr><tr><td>3</td><td>ALL</td><td>ALL</td><td>2.4108309</td></tr><tr><td>4</td><td>ALL</td><td>ALL</td><td>4.0341134</td></tr><tr><td>5</td><td>ALL</td><td>ALL</td><td>9.3705672</td></tr><tr><td>6</td><td>ALL</td><td>ALL</td><td>3.7087038</td></tr><tr><td>7</td><td>ALL</td><td>ALL</td><td>13.445068</td></tr><tr><td>8</td><td>ALL</td><td>ALL</td><td>6.0159124</td></tr><tr><td>9</td><td>ALL</td><td>ALL</td><td>1.4141097</td></tr><tr><td>10</td><td>ALL</td><td>ALL</td><td>0.6728426</td></tr></table>

<table><tr><td>Asset</td><td>Period</td><td>Scenario</td><td>Price</td></tr><tr><td>1</td><td>1</td><td>ALL</td><td>0.21</td></tr><tr><td>1</td><td>2</td><td>ALL</td><td>0.25</td></tr><tr><td>1</td><td>3</td><td>ALL</td><td>0.25</td></tr><tr><td>2</td><td>1</td><td>ALL</td><td>9.84</td></tr><tr><td>2</td><td>2</td><td>ALL</td><td>10.32</td></tr><tr><td>2</td><td>3</td><td>ALL</td><td>10.32</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>10</td><td>1</td><td>ALL</td><td>0.67</td></tr><tr><td>10</td><td>2</td><td>ALL</td><td>0.67</td></tr><tr><td>10</td><td>3</td><td>ALL</td><td>0.67</td></tr></table>

<table><tr><td>Asset</td><td>Period</td><td>Scenario</td><td>Value</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0.21</td></tr><tr><td>1</td><td>1</td><td>2</td><td>0.21</td></tr><tr><td>1</td><td>1</td><td>3</td><td>0.21</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>10</td><td>3</td><td>898</td><td>0.727029</td></tr><tr><td>10</td><td>3</td><td>899</td><td>0.665327</td></tr><tr><td>10</td><td>3</td><td>900</td><td>0.670015</td></tr></table>

![](/api/attachments/MP8UXUNQ/fulltext/images/69fadec34a88ab82568888494b0ccd24276792a0cd9e88aa710476c6b3cb0a7e.jpg)  
Fig. 7. OLAP data cube of asset price “datapaths”.

$$
\pi_ {n} = p \{\xi_ {t} | \xi_ {t - 1} | \dots | \xi_ {2} \} \sum_ {n \in N _ {t}} \pi_ {n} = 1, \pi_ {n} > 0, t = 2.. T
$$

Hence, arcs in the tree represent the probability distribution of $\xi _ { t } .$

The random data representing the uncertainty of the future are expressed in stochastic programming by a scenario tree. In the two-stage stochastic programmes, the structure of the tree encapsulates the first and second stage phases. The beginning of the planning horizon is represented by a sole root node and extends linearly to nodes until the end of the first stage. Each level in the first stage is represented by a single node since the states of the world during the first stage time periods are known with certainty. Moving to the second stage the tree branches into nodes only at level t = k + 1 as shown in Fig. 9. From each of these nodes, discrete flat scenarios commence with nodes at each time period an optimum decision has to be taken until level t = T. This means that the scenario tree is nothing else but a fan of individual scenarios $\omega _ { s } { = } \{ \omega _ { 1 , s } , ~ { \ldots } , ~ \omega _ { T , s } \}$ which occur with probabilities $p _ { s } { = } P ( \omega _ { k , s } ) \ \forall s .$

![](/api/attachments/MP8UXUNQ/fulltext/images/b6ecdf290dcb84deca8ead5384703fa8131916c72ca0617adc9fbb9a6bc2d3f4.jpg)  
Fig. 8. Time series view: 10 assets for the 65 time periods.

![](/api/attachments/MP8UXUNQ/fulltext/images/b3b26ec73a5ce14deb3f556c4fc9cd71c285edf03d07b482f3c2a0fad6ed8bbb.jpg)  
Fig. 9. Scenario tree for two-stage stochastic programming.

A representative scenario tree corresponding to the multistage stochastic programming formulation can be visualised as a tree starting similarly with the previous case with a sole root node at time 0 and branches into a finite number of nodes at level 1. This branching continues for all stages of the problem until level T. It is worth pointing out that although a node can have a finite number of descendants, a descendant could only have one immediate predecessor. A multistage scenario tree is considered to be balanced if the number of all descendants of the nodes at all stages $0 < t < T$ is equal (Fig. 10).

As a result in the two-stage stochastic program, the stages are fixed to two but the decision on the number of the time periods for the recourse actions can be two or more. In general, stages and time periods relate to points in time, that is (in the planning horizon) that are important for the decision-maker. The expiration date of an option contract or the dates a pension fund has to pay the contributions to the participants are examples of such situations. For a portfolio [18] manager who wishes to rebalance his portfolio quarterly and has a planning horizon of 12 months, the problem translates into a multistage stochastic program with four decision stages with three time periods.

![](/api/attachments/MP8UXUNQ/fulltext/images/94526d509bf7ea98b315246203ee87ff8624f1167697de9c53131efedb81ecb9.jpg)  
Fig. 10. Multistage tree.

## 4.2. Scenario generation

As discussed in the previous section, the data for a stochastic optimisation model is provided in the form of scenario trees; these are created using scenario generation methods, which may be very specific to the domain of application (see Section 2). A major focus of scenario generation is to create a tree structure of scenarios that “best” approximates a given underlying distribution of the random parameters. The criterion for choosing the “best” approximation is usually based on some measure, which quantifies the distance of the generated scenario tree from the underlying distribution. In general, a scenario generation procedure (for multistage problems) involves some or all the following steps: (a) assumption of a model, which explains the behaviour of the random parameters (for instance, econometric models for interest rates, etc.); (b) estimation/calibration of parameters for the chosen model, which uses historical data/subjective view; (c) generation of data trajectories paths according to the chosen model or discretisation of the distributions using approximation of statistical properties; (d) conditional sampling of the trajectories so that a scenario tree with the desired properties can be constructed. In many cases, practitioners also apply some reduction techniques to the resulting scenario tree to provide model instances, which can be realistically optimised by the available computational resources. Table 3 shows the most common techniques, which may be adopted for the different steps defined above.

As an alternative to generating scenarios, which are then used to instantiate large deterministic equivalent models, internal sampling techniques are methods for solving stochastic programming problems, which sample from the underlying distributions during the solution procedure.

## 4.3. Integrating scenarios and decision models

We introduced the concept of scenarios and noted that the scenario tree within SP serves two different purposes: (i) define the model uncertainty; (ii) specify the algebraic structure of the decision variables and constraints. A scenario generator $\varphi$ captures in a procedural form a domain-specific model of randomness. In particular, it uses historical information, an event tree structure and some other specification parameters. We can thus separate the main groups of parameters as H: history, τ: event tree and θ: remaining parameters. The set Ξ is then seen as the collection of scenarios, which are output, by the generation procedure: $\varphi ( H , \tau , \theta ) \Rightarrow \Xi .$ In the algebraic form of the SP model, we also need to specify the ‘variable and constraint’ tree structure, which we label as $\tau ^ { \prime } .$ . Thus, using the extended AML, we provide a specification of τ′ in the SP model through the tree declaration. For consistency, of course, we need the two trees to be congruent. In other words, we need to ensure that the event tree structure τ used by the special purpose scenario generator is ‘compatible’ with the $\tau ^ { \prime }$ specified in the SP model (Valente and Mitra [69]). The requirement for scenario generator parameter passing and tree consistency conditions are illustrated in Fig. 11. When a special purpose scenario generator is connected to SPInE, the two trees τ and $\tau ^ { \prime }$ are compared for consistency. The scenario generator then creates the set of scenarios and the associated probabilities p(ω). Alternatively, the modelling system can “import” the tree structure and allocate variables and constraints accordingly. This automatically avoids the problem of tree consistency.

Table 3  
Techniques used in scenario generation

<table><tr><td>Purpose</td><td>Methods</td></tr><tr><td>Generation of data trajectories</td><td>Econometric models and time series:Autoregressive models: AR(p)Moving average models: MA(q)Autoregressive moving average models:ARMA(p,q)Generalised autoregressive conditional heteroscedasticity: GARCH(p,q)Vector autoregressive models: VARBayesian VARReduced rank regressionDiffusion processes:Wiener processes (Brownian motion)Generalised Wiener processes (Brownian motion with drift)Other methods:Neural networks</td></tr><tr><td>Discretisation</td><td>Statistical approximationProperty matching (Høyland and Wallace [35])Moment matching (Høyland et al. [36])Non-parametric methodsSamplingRandom samplingStratified samplingBootstrapping</td></tr><tr><td>Tree construction and conditional sampling</td><td>Optimal discretisation (Pflug and Hochreiter [59])Barycentric approximation (Frauendorfer [26])Sequential clustering (Dupacova et al. [20])</td></tr><tr><td>Reduction</td><td>Scenario reduction (Dupacova et al. [21])</td></tr><tr><td>Internal sampling</td><td>Stochastic decomposition (Higle and Sen [33])Stochastic quasi-gradientEVPI-based importance sampling (Dempster and Thomson [15])</td></tr></table>

![](/api/attachments/MP8UXUNQ/fulltext/images/f770ef4df14874b62e32b1a418c43c024c632a1364cdaa73984284ec15358d78.jpg)  
Fig. 11. SG overview scheme.

The issues involved in the integration of scenario generators with a modelling system such as SPInE can be summarised as follows:

• Data consistency: The data exchange between SG and SP modelling system should be consistent and also should provide a well-defined structure of the data tree. The types and the dimension of the information contained should be compact and functional.

• Data communication: A common format for the representation of the data trees has to be defined. A standard method of generation and data flows between the objects has to be identified as well. Independently from the data used, the organisation of the information should keep the same format in a way that make the transmission easy and quick to analyse.

• Data viewing, modelling system and SG interoperability: The objects involved in the optimisation system should be independent, but at the same time should have a solid data communication interface: this enables for instance the interoperability of different SGs. Data viewing plays an important role in the solution process: data analysis and data reliability are the main objectives to achieve.

• Standard interface: The data interface for the presentation of the scenarios to the modelling system is based on ODBC connections. This allows the scenario generator to store the output in virtually any type of database (including text files). The flexible interface with scenario generators and the ability to create insample scenarios for SP model optimisation and out-ofsample scenarios for simulation make the connection to external generators a valuable feature of stochastic modelling systems.

Taking into account the above requirements, we are creating a library of scenario generators based on the techniques illustrated in Table 3. The availability of such a library makes it possible to formulate within the same modelling environment stochastic programming models, which cover different application domains (finance, supply chain, energy). A well-defined interface of SG library enables other practitioners to add their own scenario generators to the system, leading to a very versatile platform for the investigation of SP problems (see also Di Domenica et al. [16]).

## 4.4. System overview

We discuss the development of a modelling and analysis environment, which combines MDDB, OLAP, procedural languages and declarative modelling languages and supports the modeller in the automatic generation of multiperiod stochastic models and the browsing of data and solutions across different time stages and over different scenarios [57]. The system is designed to integrate databases, OLAP viewers, modelling systems, which include scenario generation, algebraic description of SPs and SP optimisation solvers and simulation within a single application system. The system components are also referred to objects, which are designed and specified to a common standard such that, where necessary, these can be replaced by alternative components. For example, we use FortSP solver but the solver object is defined in such a way that it can be easily replaced by stochastic extension to other leading industry solvers such as CPLEX or XPRESS (Fig. 12).

![](/api/attachments/MP8UXUNQ/fulltext/images/14adec02dc8ce3f7e48b2270debed4cf6b1359443b7de5de454a9b321e50ad47.jpg)  
Fig. 12. System overview.

Data flow through the system and interoperability present considerable design challenges. In the diagram above, the relations and data flows of the different objects in the system are illustrated. The database is organised in three main sections: transactional data, analytic model data and decision data (see Section 3). Scenario generator and the software tools (SP optimisation and OLAP) have all a specific role within the system. Initially, the transactional data are analysed to create analytic data, which can be viewed by the user through OLAP technology: a suitable interface is created to support the query and the analysis. The historical data is processed into an analytic data mart, which is used by the scenario generator. The resulting scenario tree data is combined with the algebraic model description to instantiate an SP decision model.

The SP solver processes the machine readable instance of the SP model created in external SMPS (stochastic mathematical programming system, see Birge et al. [4]) or in our internal SIR (stochastic internal representation) format and the results are then put back into the analytic decision database. This step is followed by the results evaluation through simulation runs or other diagnostic tests. SG is used to create scenarios for optimisation as well as to create scenarios for simulation. Simulation is very useful and can be displayed for different purposes including (a) evaluation of the stability (robustness) of a SP solution [65], (b) evaluation of the stability of the SG itself (Pflug and Hochreiter [59]), (c) quantification of the risk associated with a given decision. The system we developed shows that the integration between these objects is possible. In the next section a case study explains step by step the solution process and stability tests. There is another user perspective of the software environment, which comprises of four interacting functional modules and the resulting system architecture is displayed in Fig. 13. Also see Kutsoukis et al. [48].

The functionalities of the four modules are explained below.

## 4.4.1. External interface

This module enables the user to query the system.

## 4.4.2. Database system

It represents the repository of input data for the optimisation and evaluation models. The DB system also maintains and analyses the solutions of the SP models. More specifically, the DB system is split into two parts, as follows.

4.4.2.1. Data tables. These contain all the input data tables, which determine the instances of the problem generated by the modelling system. Similarly, the output data tables contain the solutions supplied by the SP optimisation system; all these tables can be viewed through OLAP technology in the IS system. In addition to model data, they include optimisation results and simulation results.

4.4.2.2. Procedures. In order to support SP modellers in defining the models and scenarios, tools such as nonlinear solver for parameter estimation and simulators for sampling are included. Furthermore, it contains the following procedures for the communication between different modules: (a) procedures for generating scenarios, (b) procedures for building the deterministic equivalent model, and (c) procedures for analysing, browsing and representing the results of the optimisation modules.

## 4.4.3. Modelling system

We use SPInE (Stochastic Programming Integrated Environment) (Messina and Mitra [54] and Valente et al. [69]) as modelling tool for SP. In SPInE, the user can build his own library of models, which can be used for studying and analysing different instances of the problem.

## 4.4.4. SP optimisation system

The system provides computational solution of the SP problems generated by the modelling system. It includes presolving procedures and optimisation algorithms for the solution of large-scale stochastic LP/ILP problems. The SP optimisation suite uses the embedded solver FortSP (Mitra et al. [56]) to process a range of SP models.

## 5. A case study

## 5.1. The experimental set up

We present a case study involving a small prototype model; the purpose of the case study is to illustrate the combined paradigm of data modelling, scenario generation, decision-making under uncertainty via SP modelling and result evaluation using SPInE. We consider the role of data modelling in Section 5.2 and describe an asset liability management (ALM) model in Section 5.3; in Section 5.4, we outline a multistage extension of moment matching approximation, which is used for generating scenarios for a two-stage and multistage SP model. We then consider the results of the decision model obtained by computing the solutions of the expected value, here-andnow (for both two-stage and multistage formulation of the ALM problem). These first stage decisions are then fixed to create simulation runs for the wait-and-see model and the frequency distribution of the objective solution values are computed. The analysis of results and the evaluation step through simulation cover the following aspects. In Section 5.5, we present the stochastic measures, in Section 5.6 we discuss the “in-sample stability” and in Section 5.7 the risk measures (VaR and CVaR) are presented.

![](/api/attachments/MP8UXUNQ/fulltext/images/c304899ceccadfed9afcee4ac2b010cc240ae0d8962734d471caa6e49c5d59b8.jpg)  
Fig. 13. DSS, software and user interaction.

## 5.2. Data model

In this illustrative example, the information regarding the asset prices comes from the market, whereas the current holdings and in particular liabilities are internal organizational data. The parameter values in the model $( \mathrm { s e e } \ p r i c e _ { i t s } , L _ { t } , \mathrm { H O } _ { i }$ in the next section) are instantiated by bringing together the market data and the organizational data (see Fig. 12 for a view of the two different data sources). We also observe that in addition to the input data the results are also put back in the data mart, which support the model instantiation as well as subsequent simulation.

## 5.3. The decision model

## 5.3.1. Algebraic formulation

The ALM problem: The formulation of the ALM problem is extensively discussed by Ziemba and Mulvey [70], We consider an illustrative example where an investor faces the problem of creating a portfolio allocating assets out of a universe of I assets [60]. Each asset is characterised by a price, which is (the only) random variable. The possible future prices are represented by an event tree. The goal of the investor is to maximise the portfolio wealth at the end of the time horizon T. He needs to take into account future obligations (liabilities). Asset buying and selling decisions are made, and each trade has an associated transaction cost. The deviation of the portfolio value from a predefined target is taken as measure of the risk. In each time stage, the investor can decide the amount of assets to buy, sell and hold in the portfolio. We formulate this problem as a two-stage as well as a multistage stochastic program with recourse (Messina et al. [54]):

Sets and indices:

T Denotes the number of time period in the time horizon

Assets Is the set of assets in our universe, where | $\mathbf { A s s e t s } | = I$ Scenarios Is the set of scenarios, where |Scenarios| = Sc $t { = } 1 . . . T$ Denotes time periods $i { = } 1 . . . I$ Denotes an asset $s { = } 1 . . . S { \mathrm { c } }$ Indicates a scenario

## Parameters:

price i ∈ Assets, t = 1…T, s ∈ Scenarios is the price of asset i in period t, for scenario s

$p _ { s }$ s ∈ Scenarios is the weight (probability) associated to scenario s

$L _ { t } { \geq } 0 \qquad t { = } 1 . . . T$ is the expected liability at time period t $F _ { t } { \geq } 0 \quad t { = } 1 . . . T$ is the funding available in time period t $A _ { t } { > } 0 \qquad t { = } 1 . . . T$ is the predefined target for time period t $\mathrm { H O } _ { i } { \geq } 0 ~ i { \in } \mathrm { A }$ ssets is the initial composition of the portfolio

$R \geq 0$ Is the maximum deviation from the target accepted by the investor (in fraction)

$g { \ge } 0$ Is the transaction cost rate

Decision variables:

$H _ { i t s } \geq 0$ i ∈ Assets t = 1..T, s ∈ Scenarios is the amount of assets of type i held in time period t under scenario s

$B _ { i t s } \geq 0 \mathrm { ~ i } \in A s s e t s t = 1 . . T , \mathrm { { s } \in }$ Scenarios is the amount of assets of type i bought in time period t under scenario s

$S _ { i t s } 2 0 \mathrm { i } \in \mathit { A s s e t s } , \mathrm { t } = 1 . . T , \mathrm { s } \in \mathit { S c }$ enarios is the amount of assets of type i sold in time period t under scenario s

Objective function: maximise the expected value of the final portfolio wealth:

$$
\max \sum_ {s = 1} ^ {S c} p _ {s} \sum_ {i = 1} ^ {I} \operatorname{price} _ {i T} H _ {i T}
$$

Subject to: asset holding constraints:

$$
H _ {i t s} = \mathrm{HO} _ {i} + B _ {i t s} S _ {i t s} \quad t = 1, i = 1.. I, s = 1.. \mathrm{Sc}
$$

$$
H _ {i t s} = H _ {i t - 1 s} + B _ {i t s} S _ {i t s} \quad t = 2.. T, i = 1.. I, s = 1.. \mathrm{Sc}
$$

Fund balance constraints:

$$
\begin{array}{l} (1 - g) \sum_ {i = 1} ^ {I} p r i c e _ {i t s} S _ {i t s} - L _ {t} + F _ {t} \\ = (1 + g) \sum_ {i = 1} ^ {I} p r i c e _ {i t s} B _ {i t s} \quad t = 1.. T, s = 1.. \mathrm{Sc} \end{array}
$$

Downside risk constraints:

$$
A _ {t} - \sum_ {i = 1} ^ {I} \operatorname{price} _ {i t s} H _ {i t s} \leq A _ {t} R \quad t = 2.. T, s = 1.. \mathrm{Sc}
$$

To complete the formulation, we add to this a set of non-anticipativity constraints, which depend on the event tree structure.

## 5.4. Scenario generation

Høyland et al. [36] have proposed the moment matching method, in which a discrete distribution is constructed to fit the first four marginal moments of the probability distribution of a given random vector, while maintaining the correlations between the vector's elements. The authors assume that the correlation matrix and the first four marginal moments (mean, variance, skewness, kurtosis) are supplied by the decision-maker. The structure of the algorithm is presented below in a summary form: (i) generate n discrete univariate random variables, each satisfying a specification for the first four moments; (ii) transform them so that the resulting random vector is consistent with the given correlation matrix. The transformation will distort the marginal moments of higher than second order. Hence, it is needed to start out with a different set of higher moments, so that the right ones can be obtained. The procedure would lead to the desired values for the correlations and the marginal moments if the generated univariate random variables were independent. This is, however, true only when the number of outcomes goes to infinity and all the scenarios are equally probable. With a limited number of outcomes, and possibly distinct probabilities, the marginal moments and the correlations will therefore not fully match the specifications.

## 5.5. Optimisation and stochastic measures

Given the ALM model and a set of 2500 scenarios for the asset prices generated using the method described in Section 5.3, we use SPInE to generate and solve the three related models here-and-now (HN), wait-and-see (WS) and expected value (EV). Using the decisions obtained for EV, SPInE also computes the expectation of the expected value (EEV) problem over all the scenarios. The optimum objective function values for these models are set out: WS: 67,189.4, HN: 61,354.4, EV: 54,846 and EEV: 60,567.2.

These are then used to compute the stochastic measures expected value of perfect information (EVPI)

and value of stochastic solution (VSS). These measures are designed to indicate whether or not randomness has much impact on the optimum decisions computed for the given problem: $\mathrm { E V P I } { = } ( \mathrm { W S } { \mathrm { - } } \mathrm { H N } ) { = } 5 8 3 4 . 9 1 7 7 4 1 7 2$ and $\mathrm { V S S } = ( \mathrm { H N } { \mathrm { - } } \mathrm { E E V } ) { = } 7 8 7 . 2 2 9 6 4 2 4 4 3$

These results, however, are based at the assumption that the scenario tree, which is used adequately and accurately, represents the model's uncertainty. Simulation is used to verify this assumption and test the reliability of the scenario generation method in terms of stability. Other approaches such as the contamination technique described in Dupacova et al. [19] are also used to perform an analysis of the robustness of the optimal value of a stochastic programming model.

## 5.6. Simulation: stability of the scenario generation

## 5.6.1. Stability

For a scenario-generation method, there are two desirable aspects, which need consideration. Since the first stage here-and-now decisions are influenced by the randomness of the parameter, the first aspect is in-sample stability; that is, if we generate several trees (with the same input) and solve the stochastic optimisation problem with these trees, we should get nearly the same optimal values. The second aspect is that the scenario tree should not introduce any bias, compared to the true solution (out-ofsample stability).

Table 4 Stability table

<table><tr><td>Stability measured by</td><td>Value</td></tr><tr><td>Min</td><td>57,344.52844</td></tr><tr><td>Max</td><td>60,055.20384</td></tr><tr><td>Range</td><td>2710.675393</td></tr><tr><td>Mean</td><td>59,419.04298</td></tr><tr><td>S.D.</td><td>492.7932547</td></tr><tr><td>Relative max deviation</td><td>4.56%</td></tr><tr><td>Relative mean deviation</td><td>0.83%</td></tr></table>

Min: min represents the minimum objective value of all the simulation runs (in our case 100).

Max: max represents the maximum objective value of all the simulation runs.

Range: the value “range” is the difference between max and min, and represents the maximum spread between all the runs.

Mean: we simply computed the mean of all the objective values. S.D. is the standard deviation of all the objective values.

Relative max deviation: this measure is expressed by the fraction between the range and the mean. In other words, ${ \mathrm { R M D } } = { \frac { \mathrm { R a n g e } } { \mathrm { M e a n } } } .$ Relative mean deviation: this measure is expressed by the fraction between the standard deviation and the mean. In other words, C ${ \mathrm { R M D } } = { \frac { \mathbf { 0 . p . } } { \mathbf { M e a n } } } .$

Table 5  
Simulation results

<table><tr><td></td><td>EV</td><td>HN(MS)</td><td>HN(TS)</td></tr><tr><td>Var</td><td>44,537.35</td><td>48,370.01</td><td>48,358.62</td></tr><tr><td>CvaR</td><td>41,419.95</td><td>45,054.09</td><td>45,065.22</td></tr><tr><td>Variance</td><td>113,806,893.41</td><td>52,421,392.19</td><td>52,374,316.20</td></tr><tr><td>Mean</td><td>60,798.51</td><td>61,413.73</td><td>61,413.96</td></tr></table>

EV: expected value problem.  
HN(MS): here-and-now problem multistage scenario tree.  
HN(TS): here-and-now problem two-stage scenario tree.

## 5.6.2. In-sample stability

In-sample stability (see Kaut and Wallace [44]) therefore assures the “relative robustness” of a scenario generation method. The main purpose of a scenario generator is to provide a discrete approximation of a given stochastic process (the model of randomness). If the number of scenarios is too small, however, the corresponding scenario tree may not be able to represent the underlying random process appropriately, and different scenario trees of the same size may lead to very different solutions. The in-sample stability is measured as the distance of the objective functions obtained by solving the same problem with different scenario trees (of the same size) generated with the same method. In other words, the scenario generation method is compared with itself. In our case study, we decided to adopt a three-stage tree with fifty scenarios in each stage. Subsequently, we carried out one hundred simulation runs in order to measure the stability. In each simulation, we generate a scenario tree and use SPInE to solve the relating model instance. The distribution of the objectives obtained by the simulation is used to extract the following measures of stability (Table 4).

We observe that the value given by the RMnD is less than 1%, therefore can assume that the scenario generation method used in this study is stable. Use of larger samples in the simulation runs will provide more reliable values of stability measures with a smaller error interval.

## 5.7. Simulation: computation of risk measures

Simulation is also used to evaluate the outcome of a given decision. Another set of simulation runs are therefore undertaken to analyse the risk profile (measured in terms of VaR, CVaR and variance) of three sets of decisions for our ALM model; these decisions are obtained by solving: (i) the HN optimum decision (multistage), (ii) the HN optimum decision (two-stage) and (iii) the EVoptimum decision. We use a scenario tree with 2500 scenarios to compute the three solutions above. Subsequently, we generate a larger tree with 10,000 scenarios to simulate their performance and obtain the distributions of the objective function values for each set of stage decisions. In Table 5, we set out the results obtained by the second set of simulations runs which use 10,000 scenarios.

Table 5 displays the summary of each run: The distribution of the objective function values for the three sets of decisions are shown in Fig. 14.

It is easily seen that the SP approach provides solutions which are much more robust than those obtained by deterministic EVapproach. Indeed, the variance is almost half, while in terms of VaR and CVaR; the HN solutions outperform the EV solution by about 10%.

## 6. Discussions and conclusions

The success of linear programming and mixed integer programming has in turn fuelled considerable interest in the study of stochastic programming and more recently stochastic mixed integer programming. (SMIP). SP has wide ranging applications in situations where uncertainty and risk are taken into consideration in the planning process. A natural evolution of the SP and SMIP models is to bring together (optimum) decision-making with simulation evaluation. Our future research focus is therefore to develop modelling and solution environments (Valente et al. [69] and Poojari et al. [61]) which enable the problem owners to apply a “decision engine” with which they can study “hedged” decisions and “risk” decisions under conditions of uncertainty. For instance, see Dempster [15] and Ziemba et al. [70]. There is thus considerable interest and growing adoption of SP as an important decisionmaking tool. In this paper, we have taken an integrated view of SP with data and information modelling as well as simulation modelling. Although we use wellestablished modelling and solution components in our system, our approach is highly innovative, since we bring a completely new perspective to the entire modelling process. Our case study is carefully chosen and underpins our belief that ex-ante decision modelling should be closely coupled with ex-post simulation modelling as this supports the decision-maker (problem owner) to gain more confidence in the modelling process. The connection to data and information modelling is equally important, since this enables the problem owner to extend systems into an embedded application of “business analytics”. The system architecture described in this paper is “desktop” oriented and uses welldefined internal system components which incorporates modelling language, scenario generation, data interchange. The emerging trend is towards open architecture of web services (Valente et al. [68,69]). The advantage of this approach is that “best of breed” established components developed by different researchers and developers can be connected together to rapidly create proof of concept quality applications.

![](/api/attachments/MP8UXUNQ/fulltext/images/fc7646e8ab31ea28dbfc7f978eac11b566ed677521a85780d72d9bc2d695bb7b.jpg)  
Fig. 14. EV, HN(MS) and HN(TS).

## Appendix A. SP model definition and stochastic measures

## A.1. Here-and-now problems

The formulation of the classical two-stage SP model with recourse is as follows:

$$
\begin{array}{l} Z = \min c x + Q (x) \text { subject   to } A x = b \text { and } x \geq 0 \text { where: } \\ \quad Q (x) = \min E _ {\omega} [ q (\omega) y (\omega) ] \text { subject   to } D (\omega) y (\omega) \\ \quad = h (\omega) + B (\omega) x \text { and } \begin{array}{c} y (\omega) \geq 0 \\ \omega \in \Omega \end{array} \end{array}
$$

The matrix A and the vector b are known with certainty. The function $Q ( x , \omega )$ is a non-linear term, which is referred to as the recourse function. The technology matrix B(ω), the recourse matrix D(ω), the right-hand side vector h(ω) and the vector of objective function coefficients q(ω) of this linear program may be random. For a given first stage decision x, the corresponding recourse actions y(ω) are obtained by solving the sub-problem associated with the recourse function Q(x). As the future unfolds in several sequential steps and subsequent recourse actions are taken, one deals with the generalisation of the twostage recourse problem, known as multistage stochastic programming problem with recourse. A decision made in stage t should take into account all future realisations of the random parameters and such decision only affects the remaining decisions in stages $t { + } 1 . . . T .$ In stochastic programming, this concept is known as non-anticipativity. The general formulation of a multistage recourse problem is set out in the equations below:

$$
\begin{array}{l} Z _ {H N} = \min _ {x _ {1}} \left\{c _ {1} x _ {1} + E _ {\xi 2} \left[ \min _ {x _ {2}} c _ {2} x _ {2} + E _ {\xi 3 | \xi 2} \left[ \min _ {x _ {3}} c _ {3} x _ {3} + \dots \right. \right. \right. \\ \left. \left. + E _ {\xi_ {T} | \xi_ {T - 1} | \cdot \cdot \cdot | \xi_ {2}} \min _ {x _ {T}} c _ {T} x _ {T} \right] \right] \Bigg \} \end{array}
$$

subject to:

$$
\begin{array}{c c c c c} A _ {1 1} X _ {1} & & & & = b _ {1} \\ A _ {2 1} x _ {1} + & A _ {2 2} x _ {2} & & & = b _ {2} \\ A _ {3 1} x _ {1} + & A _ {3 2} x _ {2} + & A _ {3 3} x _ {3} & & = b _ {3} \\ \vdots & & \ddots & & \vdots \\ A _ {T 1} x _ {1} + & A _ {T 2} x _ {2} + & A _ {T 3} x _ {3} + & \dots & + A _ {T T} x _ {T} = b _ {T} \\ \ell_ {t} \leq x _ {t} \leq u _ {t} \end{array}
$$

where: $t { = } 1 , . . . , T$ represents the stages in the planning horizon and the vectors: $\scriptstyle \zeta _ { t } = ( b _ { t } , c _ { t } , A _ { t I } , . . . , A _ { t T } ) \forall t \in [ 2$ $\ldots , T ]$ are random vectors on a probability space (Ω, I, P).

## A.2. Stochastic measures

It can be shown that the three objective function values $Z _ { E E V } , \ Z _ { H N }$ and $Z _ { W S }$ are connected by the following ordered relationship: $Z _ { W S } \leq Z _ { H N } \leq Z _ { E E V } .$ The inequality: $Z _ { H N } { \le } Z _ { E E V }$ can be argued in the following way: any feasible solution of the average value approximation is already considered in the here-andnow model; therefore, the optimal here-and-now objective must be better.

## A.3. The value of the stochastic solution (VSS)

The difference between these two solutions defines the value of the stochastic solution (VSS): $\mathrm { V S S } { = } Z _ { E E V } { - } Z _ { H N } .$ This is a measure of how much can be saved by implementing the (computationally expensive) here-andnow solution as opposed to the deterministic expected value solution. The practical computation of VSS is strictly related to the approach used in the computation of $Z _ { E E K }$

## A.4. The expected value of perfect information (EVPI)

Another important index is represented by the expected value of perfect information (EVPI): $\mathrm { E V P I } { = } Z _ { H N } { - }$ $Z _ { W S } .$ This property of stochastic optimisation problems is interpreted as the expected value of the amount the decision-maker is willing to pay to have perfect information (i.e. knowledge) about the future scenarios. A relatively small EVPI indicates that better forecasts will not lead to much improvement; a relatively large EVPI means that incomplete information about the future may prove costly.

## References

[1] A. Alonso-Ayuso, L.F. Escudero, A. Garín, M.T. Ortuño, G. Pérez, An approach for strategic supply chain planning under uncertainty based on stochastic 0-1 programming, Journal of Global Optimization 26 (2003) 97–124.

[2] A. Berson, S.J. Smith, Data Warehousing, Data Mining, and OLAP, McGraw-Hill, 1997.

[3] J.R. Birge, F. Louveaux, Introduction to Stochastic Programming, Springer Verlag, New York, 1997.

[4] J.R. Birge, M. Dempster, H. Gassman, A. King, S. Wallace, A standard input format for stochastic linear programs, COAL Newsletter 17 (1987) 1–20.

[5] J. Bisschop, AIMMS Manual, 2001 www.aimms.com.

[6] D.R. Cariño, A.L. Turner, Multistage planning for asset allocation, in: W.T. Ziemba, J.M. Mulvey (Eds.), World wide asset and liability modeling, Cambridge University Press, 1997.

[7] D.R. Carino, T. Kent, D.H. Myers, C. Stacy, M. Sylvanus, A.L. Turner, K. Watanabe, W.T. Ziemba, The Russell-Yasuda Model: An Asset/Liability Model for a Japanese Insurance Company Using Multistage Stochastic Programming, Interfaces, Vol. , January–February 1994.

[8] CARISMA Stochastic Programming Workshop Notes (2000). http://www.carisma.brunel.ac.uk.

[9] E.F. Codd, S.B. Codd, C.T. Salley, Providing On-line Analytical Processing to User-analysts: An IT Mandate, White Paper, E.F. Codd and Associates, 1993.

[10] G. Consigli, M. Dempster, The CALM stochastic programming model for dynamic asset/liability management, in: W.T. Ziemba, M.J. Mulvey (Eds.), Worldwide asset and liability modeling, Cambridge University Press, 1998.

[11] B. Daniel, Dash Modelling System and XpressMP Solver. www. dashoptimization.com.

[12] G. Dantzig, Linear programming under uncertainty, Management Science 1 (1955) 197–206.

[13] M. Demarest, Building the Data Mart, DBMS Magazine (1994) 44–53.

[14] Dempster, M. STOCHGEN Manual. http://www-cfr.jims.cam.ac.uk/ (1996).

[15] M. Dempster, R.T. Thompson, EVPI-based importance sampling solution procedures for multistage stochastic linear programmes on parallel MIMD architectures, Annals of Operation Research 90 (1) (1999) 161–184.

[16] N. Di Domenica, C. Lucas, G. Mitra, P. Valente, Scenario generation for stochastic programming (SP) and simulation: a modelling perspective, CARISMA Report CTR, vol. 31, 2005.

[17] B. Dominguez-Ballesteros, G. Mitra, Modelling and solving environments for mathematical programming (MP): a status review and new directions, Journal of the Operational Research Society 53 (10) (2002) 1072–1092.

[18] J. Dupacova, Portfolio optimization via stochastic programming: methods of output analysis, Mathematical Methods of Operations Research 50 (1999) 245–270.

[19] J. Dupacova, M. Bertocchi, V. Moriggia, Sensitivity of bond portfolio with respect to random movements in yield curve: a simulation study, Annals of Operation Research 99 (2000) 267–286.

[20] J. Dupacova, G. Consigli, S.W. Wallace, Scenarios for multistage stochastic programs, Annals of Operation Research 100 (2001) 25–53.

[21] J. Dupacova, N. Growe-Kuska, W. Romisch, Scenario reduction in stochastic programming: an approach using probability metrics, Mathematical Programming A95 (2003) 493–511.

[22] L. Escudero, E. Galindo, G. Garcia, E. Gomez, V. Sabau, Schumann modeling framework for supply chain management under uncertainty, European Journal of Operational Research 119 (1999) 14–34.

[23] F. Fantauzzi, A. Gaivoronski, E. Messina, Decomposition methods for network optimization problems in the presence of uncertainty. Lecture notes in economics and mathematical systems. 450: Network optimization. Red. Pardalos, Panos M.; Hearn, Donald W.; Hager, William W. Springer, ISBN 3-540-62541-0 ISSN 0075- 8442 0, pp. 234–248, (1997).

[24] R. Fourer, AMPL Manual. www.ampl.com.

[25] E. Fragniere, SETSTOCH. http://www.unige.ch/hec/logilab/ templeet/template/papiers/papier30spistoch.pdf.

[26] K. Frauendorfer, Barycentric scenario trees in convex multistage stochastic programming, Mathematical Programming 75 (1996) 277–293.

[27] H. Gassmann, MSLiP. http://www.mgmt.dal.ca/sba/profs/ hgassmann/.

[28] G. Godfrey, W.B. Powell, An adaptive, dynamic programming algorithm for stochastic resource allocation problems: I. Single period travel times, Transportation Science 36 (1) (2002) 21–39.

[29] G.A. Godfrey, W.B. Powell, An adaptive, distribution-free approximation for the news vendor problem with censored demands, with applications to inventory and distribution problems, Management Science 47 (8) (2001) 1101–1112.

[30] J. Gray, Data cube: a relational aggregation operator generalizing group-by, cross-tab, and sub-totals, MS Technical Report, (1995).

[31] A. Gupta, V. Harinarayan, D. Quass, Aggregate-query processing in data warehousing environments, Proceedings of 21st International Conference on Very Large Data Bases, 1995, pp. 358–369.

[32] M.A. Hearst, Modern Information Retrieval—Chapter 10: User Interfaces and Visualization, Addison Wesley Longman, 1999.

[33] J. Higle, S. Sen, Stochastic Decomposition: A Statistical Method for Large-scale Stochastic Linear Programming, Dordrecht, Boston, 1996.

[34] J. Higle, S. Wallace, Managing risk in the new power business—a sequel, IEEE Computer Applications in Power (April 2002) 12–19 (Vol.).

[35] K. Høyland, S.W. Wallace, Generating scenario trees for multistage decision problems, Management Science 47 (2001) 295–307.

[36] K. Høyland, M. Kaut, S. Wallace, A heuristic for momentmatching scenario generation, Computational Optimization and Applications 23 (2–3) (Feb/Mar 2003) 169–185.

[37] Infanger G. DECIS Manual. www.gams.com/solvers/decis.pdf.

[38] G. Infanger, Planning Under Uncertainty-solving Large Scale Stochastic Linear Programs, Boyd and Fraser Publishing company, 1994.

[39] W.H. Inmon, The operational data store, INFODB 9 (1) (1995).

[40] N. Jobst, M.H. Horniman, C. Lucas, G. Mitra, Computationa aspects of alternative portfolio selection models in the presence of discrete asset choice constraints, Quantitative Finance 1 (2001).

[41] P. Kall, SLP-IOR. http://www.unizh.ch/ior/Pages/Deutsch/Mitglieder/Kall/bib/ka-may-92a.pdf.

[42] P. Kall, S. Wallace, Stochastic Programming, Wiley, Chichester, 1994.

[43] J.G. Kallberg, R.W. White, W.T. Ziemba, Short term financial planning under uncertainty, Management Sciences 28 (1982) 670–682.

[44] M. Kaut, S. Wallace, Evaluation of Scenario-Generation Methods for Stochastic Programming, Posted as SPEPS 14- 2003, 2003.

[45] R. Kimball, The Data Warehouse Toolkit, Wiley, 1996.

[46] A. King, IBM OSL. http://www-306.ibm.com/software/data/bi/osl/.

[47] N. Koutsoukis, G. Mitra, Decision Modelling and Information Systems: The Information Value Chain, Kluwer Academic Pub, 2003.

[48] N. Koutsoukis, G. Mitra, C. Lucas, Adapting on-line analytica processing for decision modelling: the interaction of information and decision technologies, Decision Support Systems 26 (1999) 1–30.

[49] B. Kristjansson, MPL Manual. www.maximal-software.com.

[50] T. Kyriakis, A stochastic programming approach to asset and liability management, PhD Thesis (2001).

[51] D.G. Luenberger, Investment Science, Oxford University Press, New York, 1997.

[52] H.M. Markowitz, Portfolio selection, Journal of Finance 7 (1952) 77–91.

[53] A. Meeraus, GAMS Manual. www.gams.com.

[54] E. Messina, G. Mitra, Modelling and analysis of multistage stochastic programming problems: a software environment, European Journal of Operational Research 101 (1997) 343–359.

[55] G. Mitra, Models for decision making: an overview of problems, tools and major issues, in: G. Mitra (Ed.), Mathematical Models for Decision Support, NATO ASI Series, Springer, Verlag, 1988.

[56] G. Mitra, C. Poojari, S. Sen, Strategic and tactical planning models for supply chain: an application of stochastic mixed integer programming, in: H.P. Williams (Ed.), To appear in Handbook of Discrete Programming and Modelling, 2005.

[57] OSP Project. Optimisation Service Provider. EU CRAFT Project. http://www.osp-craft.com (2003).

[58] T.B. Pedersen, C.S. Jensen, Multidimensional data modelling for complex data, Proceedings of the Fifteenth International Conference on Data Engineering, 1999, pp. 336–345.

[59] G. Pflug, R. Hochreiter, Scenario generation for multi-stage decision models: an approach based on multidimensional facility location. Technical Report 2003-01, Department of Statistics and Decision Support Systems, University of Vienna, (2003).

[60] M. Pirbhai, G. Mitra, T. Kyriakis, Asset liability management using stochastic programming, in: B. Scherer (Ed.), Asset and Liability Management Tools. A Handbook for Best Practice, 2003, pp. 95–308.

[61] C. Poojari, G. Mitra, F. Ellison, S. Sen, Computational investigations of algorithms for processing two-stage stochastic linear programs. For publication INFORMS Journal of Computing (2005).

[62] W.B. Powell, A comparative review of alternative algorithms for the dynamic vehicle allocation problem, in: B. Golden, A. Assad (Eds.), Vehicle Routing: Methods and Studies, North Holland, Amsterdam, 1988, pp. 249–292.

[63] W.B. Powell, J.A. Shapiro, H.P. Simao, An adaptive dynamic programming algorithm for the heterogeneous resource allocation problem, Transportation Science 36 (2) (2002) 231–249.

[64] M. Rafanelli, A. Shoshani, STORM: a statistical object representation model, Proceedings of the Fifth Conference on Statistical and Scientific Database Management, 1990, pp. 14–29.

[65] W. Römisch, Stability of stochastic programming problems, in: A. Ruszczynski, A. Shapiro (Eds.), Stochastic programming, Handbooks in Operations Research and Management Science, vol. 10, 2003, pp. 483–554.

[66] J.F. Shapiro, The decision database, Sloan Working Paper WP#3570-93-MSA, (1993).

[67] P. Valente, G. Mitra, SPInE Manual. www.optirisk-systems.com.

[68] Valente, P. Mitra, G. The evolution of web-based optimisation: from ASP to e-Services, to appear in Decision Support System Journal, special issue on Web-based Decision Support, (2005).

[69] P. Valente, G. Mitra, C. Poojari, A stochastic programming integrated environment (SPInE), in: S.W. Wallace, W.T. Ziemba (Eds.), to appear in MPS/SIAM Series on Optimisation: Applications of Stochastic Programming, 2005.

[70] W.T. Ziemba, J.M. Mulvey (Eds.), Asset and liability management from a global perspective, Cambridge University Press, 1998, pp. 665.

![](/api/attachments/MP8UXUNQ/fulltext/images/90b9fe668af82721ecebe6c16b4559a02e7e89303934f49d070a3f1e257e9429.jpg)  
Nico Di Domenica. Research Interests: Optimisation software, Scenario Generation, Financial Planning, Stochastic Programming and Risk Management. BackGround: PhD in Optimisation and Modelling (Thesis Title: “Stochastic Programming and Scenario Generation, Decision Modelling Simulation and Information Systems”). CARISMA, The Centre for the Analysis of Risk and Optimisation Modelling Application, Brunel University. London. Socrates/Erasmus student

bursary. Courses attended in Madrid (Spain). Universidad Carlos III. Degree and BSc (100/110) in Computer Science, University of Milan Bicocca.

![](/api/attachments/MP8UXUNQ/fulltext/images/c013c926cb8eb161706e30d2cf3b853c394e21dad4d1c31bc9e79a138e43c1be.jpg)  
Professor Gautam Mitra. Research Interests: Stochastic programming, chance constrained programming, Quadratic programming. Risk modelling and optimum risk decisions. Portfo lio planning, asset and liability management. Decision modelling and information systems. Solution algorithms for large scale linear, integer and mixed integer programming problems. BackGround: BEE(JU), MSc(Lond), Phd(Lond), FBCS, FIMA, FRSA, He is the professor of computational optimisation and

modelling and a distinguished professor of Brunel University. In 2001 he set up The Centre for the Analysis of Risk and Optimisation Modelling Applications: CARISMA. He is the Director of CARISMA within the school of Information Systems and Mathematics, Brunel University.

![](/api/attachments/MP8UXUNQ/fulltext/images/d3f0314620651310c4faf38e1e19923645a460ddf1a78a1c503cd5171086c746.jpg)

Patrick Valente. Research Interests: Modelling and solution of Stochastic Programming problems, particularly in finance and supply chain, and development of software tools fo SP modelling, simulation and risk analysis. Use and design of algebraic modelling languages for stochastic programming problems and the implementation of web-based Decision Support Systems based on LP or SP optimisation methods. Background: Laurea in Scienze dell Informazione (Computer Science), University

of Milan (110/110 cum laude), Apr 1999; Ph.D. on Software tools for the investigation of stochastic programming problems, Department of Mathematical Sciences, Brunel University, 1999 - 2002.

![](/api/attachments/MP8UXUNQ/fulltext/images/f6b27767226e66ada8ad01074fac42327a7fb2b67a9b7328d3eb482fb45fb7fa.jpg)  
George Birbilis. Research Interests: Risk Management Modelling & Simulation, Object Oriented Framework for Decision & Risk Analysis, Operational Risk, Balance Scorecard, System Dynamics, Advanced strategies in risk management: Optimising Risk Management thorough Applied & Computational Mathematics. Background: Bachelor of Science (BSc) and Master of Science (MSc) Electrical Engineering, Pennsylvania USA, Master of Business Admin  
istration (MBA), London, UK, PricewaterhouseCoopers Management Consultant.
