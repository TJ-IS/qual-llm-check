---
otero_id: 364
otero_key: "AVNG86RF"
title: "A decision support system for sustainable energy supply combining multi-objective and multi-attribute analysis: An Australian case study"
authors: "Alessandro Mattiussi; Michele Rosano; Patrizia Simeoni"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.08.013"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for sustainable energy supply combining multi-objective and multi-attribute analysis: An Australian case study

Alessandro Mattiussi <sup>a</sup>, Michele Rosano <sup>b</sup>, Patrizia Simeoni <sup>a,</sup>⁎

<sup>a</sup> Dipartimento di Ingegneria Elettrica, Gestionale e Meccanica, University of Udine, via Delle Scienze 208, Udine, Italy <sup>b</sup> Sustainable Engineering Group, Curtin University, Sarich Road, Bentley, Perth Western Australia, Australia

## a r t i c l e i n f o

Article history: Received 8 March 2013 Received in revised form 23 August 2013 Accepted 23 August 2013 Available online 31 August 2013

Keywords: Eco-industrial park MCDA AHP CHP

## a b s t r a c t

A framework for an energy supply decision support system (DSS) for sustainable plant design and production is presented in this paper, utilising an innovative use of multi-objective and multi-attribute decision-making (MODM, MADM) modelling together with impact assessment (IA) of the emission outputs. The mathematica model has been applied within an eco-industrial park (EIP) setting and includes three steps. First, an assessment of the total EIP emissions' inventory and impacts is conducted; the second step, focusing on the sustainability bene<sup>fi</sup>ts of combined heating and power (CHP) plants and photovoltaic technologies, developed a multiobjective mathematical model including both economic and environmental objectives in a Pareto-frontier optimisation analysis. Four different scenarios involving combinations of CHP plants (internal combustion engine, gas turbine, micro-turbines and fuel cells) and two types of PV plant (monocrystalline and polycrystalline) were evaluated. The third step utilises a MADM methodology – the analytic hierarchy process (AHP) – for selecting the best alternative among the Pareto-frontier ef<sup>fi</sup>cient solutions. This model has been applied to a case study of an EIP located in Perth (Kwinana Industrial Area—KIA), Western Australia.

© 2013 Elsevier B.V. All rights reserved

## 1. Introduction

Day-to-day decision making requires both objective and subjective perspectives, utilising the former for rational, constrained modelling and the latter for adapting speci<sup>fi</sup>c problem issues to the decision-making process. The combination of both formal and informal information in the decision-making process is the main focus of this paper, referring to typical multi-criteria issues such as energy production. A decision support system (DSS) is de<sup>fi</sup>ned as a softwarebased tool assisting in the decision-making process by interacting with both internal/external users and databases while utilising standardised or speci<sup>fi</sup>c algorithms for problem solving [5].

Power, D. [21] identi<sup>fi</sup>ed four main types of DSSs, depending on the main drivers guiding the decisional process:

\- Model-driven DSSs: such DSSs require a limited amount of data because of the intrinsic composition of the system, used to evaluate quantitative data in a tailor-made structure that can be adapted to other external requirements. Initially developed for <sup>fi</sup>nancial planning, this category of DSS was later used for multi-criteria decision making and spatially driven decisions such as logistics or distribution modelling.

\- Data-driven DSSs: the database structure behind the DSS is emphasised, and the operations of data-warehousing and manipulation are the most relevant for such DSSs. Online – meaning interactive (such as the OLAP) – and of<sup>fl</sup>ine applications can be found, and webbased data-driven DSSs currently represent the natural evolutions of such models.

\- Communication-driven DSSs are used for exploiting the network and communicating capabilities of the system, which includes the use of groupware, conferencing or other computer-based communications. This category is directly related to group DSSs, developed to promote a participatory approach to the decision process, and their relation with model-driven DSSs has been studied, aiming to include the shared approach of the former with the structured modelling of the latter.

\- Document-driven DSSs, also called “text-oriented DSSs”, are used for document retrieval, especially in large groups/organisations, to support the decision-making process. The advent of a Web-based system increased the possibility of such DSSs, allowing rapid access of documents distributed in worldwide databases.

\- Knowledge-driven DSSs: these are speci<sup>fi</sup>c, tailor-made systems used in a particular domain and developed for a particular person or group of people. Power [21] acknowledged the relationship with Arti<sup>fi</sup>cial Intelligence systems, in which the DSS follows a series of rules to evaluate and eventually make decisions on the problem to be analysed.

Arnott & Pervan [2] reported a framework for DSS classi<sup>fi</sup>cation and sub-classi<sup>fi</sup>cation, identifying personal DSSs, group support systems, executive information systems, intelligent DSSs and knowledgemanagement-based DSSs. Each of such DSSs presents sub-branches depending on their speci<sup>fi</sup>c features and temporal evolution. In particular, model-driven DSS represents the focus of this study. The modellisation stage, focusing on multi-criteria modelling, will be investigated in the following paragraphs.

Multi-criteria, multi-attribute and multi-objective analyses – while similar in their ultimate purpose of assisting with the <sup>fi</sup>nal decisionmaking process [18] – differ in their de<sup>fi</sup>ning concepts. Multi-criteria decision-making (MCDM) “deals with a general class of problems that involves multiple attributes, objectives and goals” [32]. Although MCDM represents the major class in decision-making support systems, multi-attribute (MA) and multi-objective decision-making (MODM) represent their subclasses, [20] related to more speci<sup>fi</sup>c approaches in the decision-making model. Life cycle assessment (LCA) and impact assessment (IA) are tools used in industrial ecology [3] to quantify and evaluate the emissions (air, water and soil) from various parts of a production process and then evaluate their impacts on different elements of the ecological system (e.g., human health, ecosystem damage and resources) depending on the IA methodology chosen.

Optimisation with multiple con<sup>fl</sup>icting objectives has no single best solution, but a set of solutions, named the “Pareto-set” for Villfred Pareto (1848–1923), who <sup>fi</sup>rst studied them, which can be applied to social science, economy and game theory. Multi-objective optimisation techniques therefore identify a set of non-dominated solutions which represent the optimums for a given problem. The concept of domination can be illustrated as follows: an alternative a is non-dominated by b if a is better than b for at least one objective while not being worse than b for all of them.

Identifying the Pareto-frontier means also satisfying the following requisites for the solutions identi<sup>fi</sup>ed while minimising the total elaboration time, as reported in [1]:

• Spread: To <sup>fi</sup>nd a set of solutions that “capture the whole spectrum” of the true Pareto front;

• Accuracy: To <sup>fi</sup>nd a set of solutions as close to the real Pareto front as possible;

• Diversity: To <sup>fi</sup>nd a set of solutions as diverse as possible.

Weise [30] provided a broad taxonomy of evolutionary algorithms, de<sup>fi</sup>ned as “population based metaheuristic optimization algorithms that use biology-inspired mechanisms like mutation, crossover, natural selection and survival of the fittest in order to refine a set of solution candidates iteratively”. First, metaheuristics is de<sup>fi</sup>ned as a “method for solving general problems, combining objective functions in an abstract way, treating problems as a black box”.

According to [30], the <sup>fi</sup>ve main stages of evolutionary algorithms involve the following:

• Initial population, which allows the initial sample for analysis to be created from the possible set of candidate solutions;

• Design evaluation, which computes the objective value from the candidate solution;

• Fitness assignment, which, depending on the objective, determines the <sup>fi</sup>tness of the candidate solution relative to a <sup>fi</sup>tness criterion (weighed sum of objective values, Pareto ranking, etc.) which evaluates the suitability of the candidates to the optimisation required;

• Selection: based on the <sup>fi</sup>tness of the candidate solution, at this stage the population (the group of candidate solutions) to be maintained is selected, while the remaining solutions are discarded.

• Reproduction: selected candidate solutions are reproduced by different mechanisms such as partial mutation, crossovers, or complete change.

As a class of MO techniques, the family of evolutionary algorithms includes, among others, evolution strategies (ES), genetic algorithms (GA), genetic programming (GP) and learning classi<sup>fi</sup>er systems (LCS) [30]. Among GA techniques, the non-dominated sorting algorithm (NSGA) represents an increasingly used method for the design stage. NSGA and its variant NSGA-II, <sup>fi</sup>rst developed by Srinivas and

Deb [25][26], are population-based metaheuristics encompassing seven steps for design optimisation [30], i.e., population initialisation, non-dominated sorting, crowding distance, selection, genetic operators, recombination and selection. Having de<sup>fi</sup>ned the initial population based on problem constraints or user design of experiments (DOE), sorting is performed by assigning a priority value (“rank”) to non-dominated designs, selecting designs for further explorations based on rank and crowding distance, i.e., higher <sup>fi</sup>tness is assigned to individuals located on a sparsely populated part of the front [16]. Genetic operators, mainly “recombination”, “crossover” and “mutation”, are used for exploring the design space, which is then selected, maintaining a range of best-performing designs (“elitism”) for the next <sup>fi</sup>tness assessment, until the last generation of designs is assessed or the end criterion is reached.

To overcome the shortenings of lateral diversity in Pareto front determination of NSGA-II, Jeyadevi et al. [12] developed a modi<sup>fi</sup>ed NSGA (MNSGA-II) including a controlled version of elitism for improving the exploration stage and the lateral distribution of the Pareto Front, used in reactive power dispatch modelling. Guo et al. [10] used a modi<sup>fi</sup>ed version of NSGA-II to solve scheduling issues in production planning, relating scheduler utilisation to a production process simulator. Panda [19] used NSGA-II for electrical noise reduction in controller designs.

Yusoff et al. [31] reviewed the application of NSGA-II in machining design, concluding that such an algorithm represents a reliable and popular tool in MO machining setup, allowing the inclusion of multiple performances and variables. There are numerous published applications of MCDM in plant design. Multi-objective (MO) analysis has been broadly used in designing product components, but limited research has considered the environmental impacts of the process. Vince et al. [29] assessed the design installation of a Reverse Osmosis plant for desalinated water production, including both economic and environmental criteria. However, in this analysis, the environmental impact was limited to a quantitative environmental assessment of water discharges, considering electricity production and the water recovery rate as the environmental criteria. Mirzaesmaeeli et al. [15] treated environmental emissions as a constraint in a mixed integer linear programming (MILP) optimisation of a Canadian power producer, while the optimisation model proposed in [22] included environmental emissions considered as externalities, i.e., those externally generated but unaccounted for in the costs. Harkin et al. [11] used MO optimisation to design CO capture systems retro<sup>fi</sup>tted in coal power stations. They took into account the percentage of CO captured (maximised) and the energy input to the process (minimised), evaluating results as a function of the input parameters. Guillén-Gosálbez [9] applied MO optimisation, discussing its validity when assessing multiple objectives such as environmental outcomes, and introduced a mixed MILP-MO model, which they then applied to heat exchanger designs and petro-chemical supply chains. Environmental impacts within LCA typically include acidi<sup>fi</sup>cation, eutrophication, global warming and eco-toxicity. Bernier, Maréchal, & Samson [4] used both thermo-economic and environmental objectives for a carbon dioxide capture plant design, integrating LCA (in terms of global warming potential) into the optimisation model. Applied evolutionary algorithms were used in [7] for power plant capacity estimation, considering only technical (maximise exergy ef<sup>fi</sup>ciency) and economic (minimising total costs) criteria in identifying Pareto-optimal solutions.

Most MCDM methodologies provide a unique utilisation of MO or MA analysis. This paper aims to establish a framework for including both MO and MA decision-making modelling and introduces a general methodology for DSS in sustainable energy plant design (§ Section 2.x). The proposed framework has been developed to assess both individual companies and EIPs, in which the summations of each individual company's emissions can be aggregated to provide an emissions <sup>fi</sup>gure for the entire EIP. Such a framework has then been applied to a speci<sup>fi</sup>c case study in the Kwinana Industrial Area (KIA, Perth, Western Australia): the three speci<sup>fi</sup>c stages of data assessment (§ 3.1) are related to the whole industrial park, and the two stages of energy alternatives identi<sup>fi</sup>cation (§ 3.2) and choice (§ 3.3), refer to a speci<sup>fi</sup>c case study of a company in the industrial area.

## 2. Objective and methodology

The major objective of this work is to develop a DSS aimed at helping the decision maker in identifying and choosing the better energy generation options among a range of many feasible solutions. The starting point for building this model was initially identi<sup>fi</sup>ed by Simon [25], as shown in Fig. 1. It consisted of a general DSS structure and three major decision-making steps: a) problem classi<sup>fi</sup>cation/de<sup>fi</sup>nition (“intelligence phase”), b) alternative generation/evaluation (“design phase”) and c) alternatives negotiation/selection and action determination (“choice phase”). The proposed methodology uses the tools of LCA, MODM and MADM in each of these stages of the DSS.

In the proposed methodology, attributes are used in “ex-post” decision making – i.e., referring to a known situation – while objectives are antecedent to the decision-making process. In other words, attributes are used to analyse a goal towards which the objectives have been chosen. Considering the three-step decision-making approach previously described in Fig. 1, the following can be stated:

\- MODM provides support for the decision maker in identifying a range of alternatives.

\- Multi-attribute decision making (MADM) supports the decision maker in the latter stages (the “Choice Phase”) of selecting from a range of feasible alternatives.

The three stages of the research methodology are noted in Fig. 1 and are discussed below.

## 2.1. Stage I: Impact assessment of an industrial area's emissions

The data-intensive stage of life cycle inventory (LCI) was used for problem identi<sup>fi</sup>cation, focusing on an assessment of emissions from three main contributors to air, water and soil impacts in the industrial park. A two-step approach has been used. The <sup>fi</sup>rst step ranks the companies in the industrial park for macro-toxicants – toxicants whose main impacts are associated with the volumes emitted – such as $\mathrm { N O } _ { \mathrm { x } } ,$ $\mathrm { S O } _ { \mathrm { x } } ,$ PMs and NMVOCs. The LCI is then followed by an IA (LCIA) to evaluate the micro-toxicant impacts – i.e., toxicants whose impact is due to the quality of the toxicant itself. The LCIA methodology chosen for the study was ‘Eco-Indicator 99’, a damage-oriented method for LCIA [8] that takes into account human health, eco-system and land use impacts. Two main impacts have been considered for the following LCIA stage, namely Human Health and Eco-system Damage. In Eco-Indicator 99, ‘human health impacts’ are measured in ‘Disability Adjusted Life Years’ (DALY), a variable that measures the number of ‘life’ years lost due to the inhalation/ingestion of pollutants p via different sources (e.g., air, food, water); ‘eco-system impacts’, are measured by the ‘Potentially Disappeared Fraction’ (PDF) of animal and natural species per square metre per day. Human health impacts (HHIs) and ecosystem impacts (ESIs) Impacts have been calculated according to Eq. (1) and Eq. (2):

$$
H H I = \sum_ {c} \sum_ {p} I E _ {p, c} H H I _ {p, c}\tag{1}
$$

$$
E S I = \sum_ {c} \sum_ {p} I E _ {p, c} E S I _ {p, c}\tag{2}
$$

thus summing up the emissions of each pollutant $\mathsf { p }$ to each compartment c $( \mathrm { I E } _ { \mathrm { p , c ) } } ,$ multiplied for its impact factor $\mathrm { ( H H I _ { p , c } , }$ ESIp,c) on the two considered impact categories of human health $\mathrm { ( H H I _ { p , c } ) }$ and ecosystem damage $\left( \mathrm { E S l } _ { \mathrm { p , c } } \right)$

## 2.2. Stage II: MODM for combined heat and power plant design

Having assessed the outputs and impacts of the EIP, the focus is then shifted to single companies inside the EIP. An MO model has been developed for the design of a gas-<sup>fi</sup>red CHP plant integrated with PV (photovoltaic) solutions. The model accounts for both economic and environmental impacts. The Economic assessment indicator is a Net Present Value (NPV) cash <sup>fl</sup>ow assessment, while the environmental analysis considered local impacting pollutants such as $\mathsf { N O } _ { \mathrm { x } } , \mathsf C 0 , \mathsf S 0 _ { 2 } ,$ NMVOCs and PMs. The optimisation process relies on a number of factors including the following:

\- There is a discrete choice among plants. The four different types of CHP technologies being assessed (internal combustion engines, turbines, micro-turbines and fuel cells) have been selected from the most relevant manufacturers worldwide, with technical performance (e.g., power conversion ef<sup>fi</sup>ciency) data taken from manufacturers' catalogues and implemented in a Microsoft Excel spreadsheet. Similarly, data were collected from PV manufacturers. Environmental performance measures including emission rates have been taken from [27] and [28].

![](/api/attachments/AVNG86RF/fulltext/images/4561247bec0d18a19da959153273f56576a6bf96f5a2f148483f85a07cb2dcda.jpg)  
Fig. 1. DSS integrated with LCA and MCDM (adapted from [24]).

\- Life cycle assessment has been used for assessing the environmental impact of the life cycle emissions, and the impact area considered is an algebraic sum of the emission outputs from the CHP plants and the emissions avoided from the heating and power produced. Human health impacts, as de<sup>fi</sup>ned in the previous section, have also been considered to evaluate and quantify the damage produced by each pollutant, resulting in the calculation of the human health impact reduction (HHIR) coef<sup>fi</sup>cient considered in the MO assessment.

\- Technical constraints have been used to avoid excessive waste heat while still satisfying at least 70% of company's power needs on a monthly basis.

\- The economic analysis relies on a traditional cash <sup>fl</sup>ow analysis but also considers the current trends in power and fossil fuel prices in all revenues and costs, resulting in both revenue and cost adjustments during the medium-term investment.

The two MO objectives are to maximise the Net Present Value (NPV) and the HHIR of the combined solutions (CHP + PV). The simulations combined a Microsoft Excel worksheet for <sup>fl</sup>exible modelling and simulation and ModeFrontier software (developer: Esteco, Trieste, Italy) for advanced scheduling and optimisation; the programs were then run in an iterative process to identify the Pareto-frontier, i.e., the group of non-dominated solutions, de<sup>fi</sup>ned as the group of alternatives which cannot be improved in one of the two objectives without reducing the other. The design space of the optimisation model – the total number of candidates solutions to be assessed – consisted of 256 CHP plants, 48 PV module types, four variables (0.7 to 1, step 0.1) assessing the percentage of heat and four parallel variables for the percentage of power to be covered by the plant, four variables assessing the number n of similar CHP plants to be considered (1 to 4, step 1) and 11 variables (0 to 1, step 0.1) assessing the percentage of total available roof area covered by the PV plants.

The procedure for the optimisation process is summarised in Fig. 2.

The identi<sup>fi</sup>cation of the initial set of candidate solutions, DOE, i.e., the combination of variables to be simulated by Microsoft Excel, represents a major stage in the whole optimisation process. Among the advantages of a consistent DOE, the rapidity of the optimisation process for rapidly converging to optimal solutions is most likely the most relevant.

The design space is de<sup>fi</sup>ned by the number of variables multiplied by the number of variable levels (i.e., the allowed values for each variable). Given a problem with <sup>fi</sup>ve variables, each with three possible levels, the maximum number of design combinations is $5 ^ { 3 } = 1 2 5$ designs. Obviously, increasing the number of variables and levels increases the complexity of the problem. Over the hypercube de<sup>fi</sup>ned as the polyhedron with a number of dimensions equal to the number of variables (e.g., three variables with equal level size are represented by a cube), the initial design space can be selected in various ways.

The software used for the optimisation process (Esteco Mode Frontier 7.0) allows the following DOE algorithms: user-de<sup>fi</sup>ned sequences, random DOE, Sobol sequences, constraint satisfaction problem (CSP) models, Latin HyperCube/Montecarlo, full factorial DOE, reduced factorial DOE, cubic face centred DOE and Box-Behnken DOE.

Having <sup>fi</sup>xed the initial set of solutions for which the output values have been assessed, the optimiser has to decide how to move from one set of candidates to the next, to identify best-performing candidates. This process, known as scheduling, depends on many variables, such as the following:

\- Variable type: continuous vs. discrete;

\- Search operators: mutation/selection/crossover;

\- Relation among generations (keeping best solutions, i.e., elitism, or completely changing the generation set);

\- Computing capabilities: varying the number of contemporary assessed variables.

<table><tr><td>STAGES</td><td>OBJECTIVE</td><td>TOOLS</td><td>DONE BY</td></tr><tr><td>DOE – Initial Set of Variables</td><td>Define the initial generation of candidate solutions to be assessed</td><td>DOE Algorithms</td><td>Mode Frontier/User</td></tr><tr><td>Output Calculation</td><td>Calculate the results from the single simulation of each generation of candidate solutions</td><td>Mathematical Model</td><td>Microsoft Excel</td></tr><tr><td>Scheduling</td><td>Variates the candidates solutions depending on simulation results</td><td>Scheduling Algorithm</td><td>Mode Frontier</td></tr><tr><td>Pareto Front</td><td>Identifies the non-dominated solutions</td><td>Optimizer</td><td>Mode Frontier</td></tr></table>

Fig. 2. Optimisation procedure followed.

## 2.2.1. The mathematical model

The mathematical optimisation model considers the following objective functions:

$$
\operatorname{Max} (N P V) = \sum_ {y} (A C F) _ {y} - I _ {o}\tag{3}
$$

$$
\operatorname{Max} (H H I R) = A E I - C E I\tag{4}
$$

NPV, as expressed in Eq. (5), represents the sum of the cash <sup>fl</sup>ows (ACF) actualised and considered throughout the whole duration (y) of the initial investment (I ) on a monthly basis (m) for each of the technologies assessed (t). ACF is equal to the difference between the actualised revenues (TAR) and costs (TAC), in turn depending on the revenues from selling excess power $( \mathbb { R } ^ { \mathrm { e x c } } )$ , the avoided purchasing of electricity and heat $( \mathbb { R } ^ { \mathrm { a v } } )$ , incentives (I) and associated variable costs such as fuel consumption (C<sup>f</sup>), maintenance (C<sup>m</sup>), heat and power integration $( \mathsf { C } ^ { \mathrm { i n t } } )$ and excessive heat disposal $( { \cal C } ^ { \mathrm { e x c } } )$

$$
\begin{array}{l} N P V + I _ {o} = \sum_ {y = 0} ^ {1 5} \overline {{A C F}} _ {y} = \sum_ {y = 0} ^ {1 5} \left(\overline {{T A R}} _ {y} - \overline {{T A C}} _ {y}\right) = \sum_ {y} \sum_ {m} \sum_ {t} \left(\overline {{R}} _ {e l} ^ {e x c} + \overline {{R}} _ {e l} ^ {a v} + \overline {{R}} _ {h} ^ {a v} + \overline {{I}}\right) \\ - \sum_ {y} \sum_ {m} \sum_ {t} \left(C ^ {f} + C ^ {m} + C _ {e l} ^ {\text { int }} + C _ {h} ^ {\text { int }} + C _ {h} ^ {\text { exc }}\right) _ {y, m, t} \end{array}\tag{y,m,t}
$$

ð<sup>5</sup>Þ

The HHIR, as reported in Eq. (6), has been calculated as the sum of the impacts from the avoided emissions from electricity generation $( \mathsf { A E I } _ { \mathrm { e } } ,$ positive), heat $( \mathsf { A E I } _ { \mathrm { h } }$ positive) production and current emissions (CEI, negative) from the simulated design.

$$
\begin{array}{l} H H I R = A E I _ {e} + A E I _ {h} - C E I = \\ \sum_ {p = 1} ^ {5} E L \cdot E R _ {p} ^ {e l} \cdot I F _ {p} + \sum_ {p = 1} ^ {5} E _ {h} \cdot E R _ {p} ^ {h} \cdot I F _ {p} - \sum_ {p = 1} ^ {5} \sum_ {t = 1} ^ {7} F C _ {t} \cdot E R _ {t, p} \cdot I F _ {p} \end{array}\tag{6}
$$

AEI is calculated by multiplying the total electricity production (EL) by the emission rates of each pollutant p from the national power system and the relative speci<sup>fi</sup>c impact factor (IF) of each pollutant in terms of speci<sup>fi</sup>c human health impact; the latter is expressed in DALY/kg, using the LCIA Eco-Indicator methodology described in § 2.1. Emission Rates (ER) for each pollutant p were used to calculate the avoided power production and associated emissions; these rates were taken from the IPPC/Corinair Emission Factor database, taking into consideration the energy mix of the speci<sup>fi</sup>c country. Similarly, $\mathtt { A E I } _ { \mathrm { h } }$ depends on the heat saved by the company $\left( \operatorname { E } _ { \mathrm { h } } \right)$ multiplied by the pollutants emitted by traditional natural-gas boilers – again from the Corinair database – and the pollutant-related impact factor of LCIA Eco-Indicator methodology. Eventually the CEI considered plant-speci<sup>fi</sup>c emission rates, expressed in kg per input MJ, fuel consumption (FC) of the simulated design considering each CHP technology t and the relevant impact factor.

Each simulation has been subjected to constraints to promote the following:

\- Correct plant sizing (avoiding excessive heat waste), considering the LT index (Eq. (7)), stating that at least one third of the thermal output must be exploited;

$$
\mathrm{LT} = \mathrm{E} ^ {\mathrm{th}} / \left(\mathrm{E} ^ {\mathrm{th}} + \mathrm{E} ^ {\mathrm{e}}\right) > 0. 3 3\tag{7}
$$

\- Satisfy a percentage (PC) of the heating and power needs of the company c on a monthly basis m;

$$
\mathrm{E} _ {\mathrm{m}, \mathrm{t}} ^ {\mathrm{ee}} > \mathrm{PC} _ {\mathrm{c}, \mathrm{m}} ^ {\mathrm{ee}} \mathrm{E} _ {\mathrm{c}, \mathrm{m}} ^ {\mathrm{ee}}\tag{8}
$$

$$
\mathrm{E} _ {\mathrm{m}, \mathrm{t}} ^ {\mathrm{h}} > \mathrm{PC} _ {\mathrm{c}, \mathrm{m}} ^ {\mathrm{h}} E _ {\mathrm{c}, \mathrm{m}} ^ {\mathrm{h}}\tag{9}
$$

\- Respect site-speci<sup>fi</sup>c limits: the occupied area of PV plants $( S _ { \mathrm { P V } } )$ has to be inferior to the available roof area $\left( { \mathsf { A } } _ { \mathrm { R A } } \right)$ for PV plants multiplied by the percentage of covered area $( \mathsf { P C } ^ { \mathsf { P V } } )$ .

$$
S _ {\mathrm{PV}} <   \mathrm{PC} ^ {\mathrm{PV}} A _ {\mathrm{RA}}\tag{10}
$$

## 2.3. Stage III: MADM

Having identi<sup>fi</sup>ed the technical feasible solutions from both an economic and environmental perspective, the last step of the methodology involves the development of a decision-making model to assist with the <sup>fi</sup>nal choice among the identi<sup>fi</sup>ed solution sets. AHP methodology, proposed by [23], has been selected for this purpose. AHP has been widely used for MADM, particularly for correlated sustainability issues, as reported by [6,13] and [17]. The method allows the inclusion of both quantitative and qualitative criteria in the assessment and involves three stages: problem structuring: pairwise comparison, aggregation and results, as outlined in Fig. 3.

## 3. The case study: Kwinana Industrial Area

The Kwinana Industrial Area (KIA) is approximately 40 km from the city of Perth (Western Australia) and is characterised by a signi<sup>fi</sup>cant presence of heavy industries such as re<sup>fi</sup>neries (crude oil, alumina, titanium dioxide, nickel) and chemical production, together with regional utility plants for power production and water treatment. Over 50 companies are present in the Kwinana Industrial area (KIA). The KIA was assessed during the period January to June 2011, by directly visiting the companies, interviewing personnel and collecting data.

## 3.1. Life cycle impact and life cycle impact assessment

LCI was <sup>fi</sup>rst performed using data from the Australian National Pollutant Inventory (NPI) database, using a 1% cut-off percentage – therefore considering only relevant emitters in the Area (C1 to C27) – and allowing the ranking of companies regarding their NOx, PM, SOx and NMVOC emissions, as shown in Fig. 4.

The micro-toxicant IA considered the wide range of impacts in the Eco-Indicator 99 methodology, but was limited to Eco-System and Human Health Impacts, due to the lack of Australian-speci<sup>fi</sup>c impact factors for the other impact categories. The human health and ecosystemspeci<sup>fi</sup>c impacts (per unit of pollutant emitted/discharged) – were computed by [14] and have been used in this study. The results shown in Fig. 5 allow us to identify the most signi<sup>fi</sup>cant companies in the area regarding the two impact categories considered.

## 3.2. MODM for a selected case study company

While the <sup>fi</sup>rst stage of the research addressed the entire EIP (Kwinana Industrial Area), in this next analysis we focus on a speci<sup>fi</sup>c company within the KIA. This company is a chemicals producer and has speci<sup>fi</sup>c energy requirements in its productive cycle of both hot water and electricity generation. The MO methodology has been used at this stage. A combination CHP and PV plant was selected as the energy source for the individual company given the requirement for continuous loads of both hot water and electricity and the availability of high solar radiation in the immediate region, which averages some 19.6 MJ/m2 (Australian Bureau of Meteorology). The company's monthly energy and water consumption data have been collected via direct interviews with company personnel to gather the necessary information regarding the productive cycle, power and natural gas consumption and the costs to be used in the mathematical model in the MO model mentioned in Section 2.3. An initial set of 100 feasible designs – randomly generated with feasible solutions manually inserted – constituted the <sup>fi</sup>rst generation of modelled runs.

![](/api/attachments/AVNG86RF/fulltext/images/e05ad81de7b6a933a6da877d92619950fc37a5aead2990b9ef31793892cb9c16.jpg)  
Fig. 3. AHP methodology.

An NSGA-II algorithm was then selected for the scheduling and optimisation of these 100 generations, thus covering approximately 10,000 potential solutions, which is extremely limited compared to the size of the design stage.

Simulation results are shown in Fig. 6, showing the value of economic pro<sup>fi</sup>tability (to be maximised) on the y-axis and the best environmental performing solutions (reducing the impact of its emissions) on the x-axis. As shown, the simulator assesses the feasible points, which in this case study are related to combinations of gas-fuelled-ICEs or fuel cells, as well as PV plants. Other solutions (gas and micro turbines) could not conform to the current limit on excess waste heat output while simultaneously satisfying at least 70% of company's power needs. The top left corner of Fig. 6, represents the most pro<sup>fi</sup>table solution for the optimisation results but presents a NPV that is barely positive (AU\$113,000) and an environmental impact reduction that is negative (more pollutants are emitted than the effective emission savings). In the top right corner, the most environmental impactreducing solution presented has an HHIR of 19.7 DALY (the unit of measurement for human health impact) and an economic pro<sup>fi</sup>tability of AU \$110,000, while in the bottom right corner the Pareto-frontier presents a comparable value of HHIR, but at a reduced pro<sup>fi</sup>tability.

The Pareto-frontier is therefore made up of two main groups of solutions: <sup>fi</sup>rst, a combination of gas-fuelled ICE and PV plant, located in the top left of Fig. 6 above, and second, a fuel cell coupled with a PV plant (top-right and bottom right, respectively). The selected solutions have been oversized due to an expressed request by the company, which is expecting to increase production output and therefore the required heat and power loads in the near future. The technical details associated with these two alternatives, exported from the simulator outputs, are reported in Table 1.

## 3.3. AHP analysis of selected alternatives

The previous stage involved only two-objective functions to identify trade-off ranges, but given the various issues involved in the decisionmaking process, a more detailed problem-solving structure is considered here for the more complex AHP analysis. A business-as-usual (BAU, i.e., continuing current plant management) option has also been considered, and its economic/environmental performances have been calculated. Speci<sup>fi</sup>cally, four categories of criteria have been used, considering environmental, economic, technical and social criteria. The hierarchical model for the AHP analysis is represented in Fig. 7, together with the criteria's associated priorities to selected Equal Weights (EW), Environmental (En), Decision Maker (DM) and Technical (Te) scenarios.

The criteria used in the decision-making assessment involved both quantitative (ef<sup>fi</sup>ciencies, emissions and IRR) and qualitative (reliability, commercial viability and the decision makers' attitudes) criteria. Quantitative criteria were directly translated into the 1–9 Saaty Scale for pairwise comparison using the AHP reference software SuperDecisions 2.08, while the qualitative criteria indicating the decision makers

![](/api/attachments/AVNG86RF/fulltext/images/e0662d96729b8403259ac2adb323f5d5bf3300008aecdc01eb389418c831dff8.jpg)  
Fig. 4. Life cycle inventory of KIA macro-toxicants.

Most significant emitter of Toxicants impacting on Human Health and Eco-System  
![](/api/attachments/AVNG86RF/fulltext/images/27aa244a18671cc59f0d23ea0dc307908054c7b755bac5128edc042eeb7f9a62.jpg)  
Fig. 5. Impact assessment of KIA's micro-toxicant emissions.

attitude towards the solutions have been considered by interviewing company personnel and identifying their preferences among the selected alternatives. When assessing the weight of the four main groups of criteria in terms of the main objectives (maximising NPV and maximising HHIR), three scenarios were considered, i.e., the technical/economic perspective, the environmental perspective and the DMs' viewpoint. The evaluation of these three criteria was performed by assigning maximum weight (9 in the Saaty Scale) to the respective criteria in the three scenarios assessed, i.e., Technical/Economic in Scenario 1, decision maker (social criteria) in Scenario 2 and Environmental criteria in Scenario 3, while assigning equal weight to intra-criteria assessment (e.g., environmental and social criteria) in Scenario 1. Furthermore, a scenario with equal weights for all four criteria has also been considered.

Results are shown in Fig. 8. The combination of the internal combustion engine and PV plants was the most preferred alternative in terms of both the Techno-Economic assessment and the decision makers' point of view, largely due to its economic performance (NPV, IRR and PB) and the commercial/technological reliability of the CHP solution. From the environmental viewpoint, FC and PV plants were the mostpreferred solution, due to the low environmental impact of the FC plant and its higher power conversion ef<sup>fi</sup>ciency, hence lowering fossil fuel consumption and increasing ${ \mathrm { C O } } _ { 2 }$ emission reduction.

![](/api/attachments/AVNG86RF/fulltext/images/35b27fee38725600452e3a5736caa12e7423e97aa3b95d0f209a1e1308b9077f.jpg)  
Fig. 6. MO optimisation design space assessed.

Table 1 Pareto-frontier alternatives: Details.

<table><tr><td colspan="2"></td><td>UM</td><td>Solution 1</td><td>Solution 2</td></tr><tr><td rowspan="12">Technical criteria</td><td>CHP plant type</td><td></td><td>ICE</td><td>FC</td></tr><tr><td>Power</td><td>kW</td><td>370</td><td>300</td></tr><tr><td>Power efficiency</td><td>%</td><td>39%</td><td>54%</td></tr><tr><td>Thermal efficiency</td><td>%</td><td>45%</td><td>41%</td></tr><tr><td>PV peak power</td><td> $kW_p$ </td><td>120</td><td>190</td></tr><tr><td>PV efficiency</td><td>%</td><td>14%</td><td>20%</td></tr><tr><td>PV occupied area</td><td>m2</td><td>1050</td><td>1050</td></tr><tr><td>Power produced by PV</td><td>kWh</td><td>161,663</td><td>234,965</td></tr><tr><td>Total power produced</td><td>kWh</td><td>1,255,568</td><td>1,138,810</td></tr><tr><td>Percentage</td><td>%</td><td>100%</td><td>91%</td></tr><tr><td>Total heat produced</td><td>kWh</td><td>1,259,469</td><td>685,431</td></tr><tr><td>Percentage</td><td>%</td><td>230%</td><td>125%</td></tr><tr><td rowspan="6">Economic criteria</td><td>Capital costs</td><td>AU$</td><td>1,108,486</td><td>2,152,555</td></tr><tr><td>Operating costs at y = 0</td><td>AU$</td><td>270,561</td><td>219,113</td></tr><tr><td>Operating revenues at y = 0</td><td>AU$</td><td>284,708</td><td>266,533</td></tr><tr><td>Payback</td><td>Years</td><td>19</td><td>19</td></tr><tr><td>NPV</td><td>AU$</td><td>161,020</td><td>228,839</td></tr><tr><td>IRR</td><td>%</td><td>15%</td><td>11%</td></tr><tr><td rowspan="6">Environmental criteria(avoided emissions)</td><td> $CO_2$  emissions</td><td>t</td><td>193.82</td><td>365.8</td></tr><tr><td>CO emissions</td><td>t</td><td>-15.51</td><td>0.64</td></tr><tr><td> $SO_x$  emissions</td><td>t</td><td>3.06</td><td>2.78</td></tr><tr><td>PM emissions</td><td>t</td><td>0.05</td><td>0.08</td></tr><tr><td>NMVOC emissions</td><td>t</td><td>-0.11</td><td>0.00</td></tr><tr><td>NOx emissions</td><td>t</td><td>-7.95</td><td>1.52</td></tr></table>

From the Environmental viewpoint, the ‘business as usual’ (BAU) scenario – i.e., maintaining the current operation – represents the second-preferred solution, given its poor environmental performance of ICE (internal combustion engine) solutions, which feature high emissions of $\mathsf { N O } _ { \mathrm { x } }$ and CO – higher than the base-case scenario. Considering the DMs' viewpoint, an almost identical priority has been assigned to the BAU and ICE scenarios, with a small preference for the latter, with higher preference given to the absence of capital investment – a priority perhaps from the decision makers' perspective.

The equal-weights scenario presented similar results for ICE and FC plants – with a slightly higher performance for the former – whereas the BAU scenario ranked considerably behind the CHP technologies. The solutions presented for the various scenarios have been tested for rank reversal problems, as suggested by Schenkerman [24]. This has been done by deleting the poorest-performing solution for each scenario (BAU in Scenario 1, 2 and $4 , \mathsf { F C } + \mathsf { P V }$ in Scenario 2) and re-assessing the rankings. The results are shown in Fig. 9.

As illustrated in Fig. 9, no rank reversal occurred when testing the solutions. For each scenario, the rank among the alternatives has been maintained, with variations in the raw priority values due to the removal of the poorest-performing solution, which contributed to their original calculation.

Sensitivity tests have been conducted to evaluate the robustness of the “Equal Weights” scenarios. The results show that a relevant variation in BAU priorities is required (+57%) suggesting that the alternative solutions are signi<sup>fi</sup>cantly more valuable than the BAU option. Similar computations with analogous results were also found for the FC and ICE solutions. A slight increase in the FC raw priority or a minimal decrease in the ICE solution (±4%) leads to a Pareto ef<sup>fi</sup>ciency intersection, resulting in a non-optimal solution set.

![](/api/attachments/AVNG86RF/fulltext/images/b9be86ff3a9c5472fd81c585936fcf97b24b6bda0c6571f4856f16b3f6916e7f.jpg)  
Fig. 7. AHP hierarchy for MADM of selected alternatives

Normal Priorities for selected Scenarios  
![](/api/attachments/AVNG86RF/fulltext/images/5155a1d24327492c30890a11c59740a9954bcfa2b2a1bce64ae98a6458af9271.jpg)  
Fig. 8. Normal priorities for selected scenarios.

## 4. Discussion and conclusions

This paper developed a DSS for addressing energy optimisation decisions in energy plant designs. The potential value of this analysis is that it provides a DSS framework for assessing and benchmarking the sustainability of energy production systems, considering both objective and subjective criteria throughout the analysis by exploiting the advantages of both MODM and MADM.

Following the traditional frameworks of DSS (problem identi<sup>fi</sup>cation, alternatives generation and alternatives selection), the developed DSS consisted of a three-step approach:

Problem identi<sup>fi</sup>cation has been conducted by emissions assessment, considering both the volumes and impacts of emitted substances. Particular emphasis has been given to the “Eco-Indicator '99” methodology, which calculates the environmental impacts (damage done) from a range of emission variables. Next, an MO optimisation was conducted to determine the possible energy alternatives by developing a mathematical model considering economic and environmental objectives at the very beginning of the energy plant design, involving mixed renewable/non renewable CHP (internal combustion engines, gas turbines, fuel cells) and PV technologies. The third and last step of the DSS involved using the input results of the optimisation process (step 2), which included MADM in the selection of the best alternatives among the candidate solutions from the Pareto-Frontier.

While traditional energy ef<sup>fi</sup>ciency ‘trade-off studies’ relate to energy use, ef<sup>fi</sup>ciency and cost, in this paper two additional impacts are included – environmental impacts and an allowance for ‘conventional wisdom’ in decision making.

The methodology followed potentially aids in decision-making processes and the planning process for energy plant designs that are both more eco-ef<sup>fi</sup>cient and sustainable. This is particularly relevant for energy investment in large industrial and manufacturing companies and increasingly important for those involved in eco-industrial parks and the energy-intensive mining and resources sectors.

A more holistic DSS has been presented that assists in reviewing the emission footprint and environmental impacts of energy production investment. The days of assessing energy production solely in terms of NPV are coming to a close. Increasing regulatory pressures and community concerns about GHG production also suggest a need to review plant energy design in terms of environmental impact and other emissions criteria.

Further research could also use this methodology in worldwide industrial park benchmarking assessments, to promote lower emissions and higher industrial emission standards. The full methodology detailed in this paper could also be extended to other types of industrial plants, including water treatment plants and energy plants integrated with enhanced pollution abatement technologies.

Normal Priorities for selected Scenarios - Rank Reversal Test  
![](/api/attachments/AVNG86RF/fulltext/images/8ff47dc19afe0728e0ef23d57b65d03bd4daa68070e40e3f35e2caedfcbeb8ec.jpg)  
Fig. 9. Normal priorities for selected scenarios — Rank reversal test.

## References

[1] A. Alarcon-Rodriguez, G. Ault, S. Galloway, Multi-objective planning of distributed energy resources: a review of the state of the art, Renewable and Sustainable Energy Reviews (2010) 1353–1366.

[2] D. Arnott, G. Pervan, A critical analysis of Decision Support Systems research, Journa of Information Technology (2005) 67–87.

[3] R. Ayres, A Handbook of Industrial Ecology, Edward Elgar, 1994.

[4] E. Bernier, F. Maréchal, R. Samson, Multi-objective design optimization of a natural gas-combined cycle with carbon dioxide capture in a life cycle perspective, Energy (2010) 1121–1128.

[5] F. Burstein, C.W. Holsapple, Handbook on Decision Support System 1, Springer, 2008. [6] A.I. Chatzimouratidis, P.A. Pilavachi, Environmental, technologic and economic criteria are used for evaluating different power plants, Energy Policy (2009) 778–787.

[7] J. Dipama, A. Teyssedou, F. Aubé, L. Lizon-A-Lugrin, A grid based multi-objective evolutionary algorithm for the optimization of power plants, Applied Thermal Engineering (2010) 807–816.

[8] M. Goedkoop, R. Spriensma, The Eco-Indicator 99: A Damage Oriented Method for Life Cycle Impact Assessment, Prè Consultants, 2011.

[9] G. Guillén-Gosálbez, A novel MILP-based objective reduction method for multiobjective optimization: application to environmental problems, Computers and Chemical Engineering (2011) 1469–1477.

[10] Z.X. Guo, W.K. Wong, Zhi Li, Peiyu Ren, Modeling and Pareto optimization of multi-objective order scheduling problems in production planning, Computers and Industrial Engineering 64 (2013) 972–986.

[11] T. Harkin, A. Hoadley, B. Hooper, Using multi-objective optimisation in the design of CO capture systems for retro<sup>fi</sup>t to coal power stations, Energy 41 (2010) (2011) 228–235.

[12] S. Jeyadevi, S. Baskar, C.K. Babulal, M. Willjuice Iruthayarajan, Solving multiobjective optimal reactive power dispatch using modi<sup>fi</sup>ed NSGA-II, Electrical Power & Energy Systems 33 (2011) 219–228.

[13] D. Krajnc, P. Glavič, A model for integrated assessment of sustainable development, Resources, Conservation and Recycling (2005) 189–208.

[14] S. Lundie, M.A. Huijbregts, H.V. Rowley, Australian characterisation factors and normalisation <sup>fi</sup>gures for human toxicity and ecotoxicity, Journal of Cleaner Production (2007) 819–832.

[15] H. Mirzaesmaeeli, A. Elkamel, P. Douglas, E. Croiset, M. Gup, A multi-period optimization model for energy planning with CO emission consideration, Journal of Environmental Management (2010).1063–1070.

[16] P. Murugan, S. Kannan, S. Baskar, NSGA-II algorithm for multi-objective generation expansion planning problem Electric Power Systems Research 79 (2009) 622-628

[17] N. Nagesha, P. Balachandra, Barriers to energy ef<sup>fi</sup>ciency in small industry clusters: multi-criteria-based prioritization using the analytic hierarchy process, Energy (2006) 1969–1983.

[18] D. Olson, Multi-criteria decision support, in: Burstein, Holsapple (Eds.), A Handbook on Decision Support System, 1, Springer, 2008, p. 299.

[19] Sidhartha Panda, Narendra Kumar Yegireddy, Automatic generation control of multi-area power system using multi-objective non-dominated sorting genetic algorithm-II, Electrical Power & Energy Systems 53 (2013) 54–63.

[20] S. Pohekar, M. Ramachandran, Application of multi-criteria decision making to sustainable energy planning, Renewable and Sustainable Energy Reviews 365–381 (2004).

[21] Power, Decision Support Systems: a historical overview, in: Burstein, Holsapple (Eds.), Handbook on Decision Support System 1, Springer, 2008, pp. 121–140.

[22] A. Rong, R. Lahdelma, CO emissions trading planning in combined heat and power production via multi-period stochastic optimization, European Journal of Operational Research 1874–1895 (2005).

[23] T. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[24] S. Schenkerman, Avoiding rank reversal in AHP decision-support models, European Journal of Operational Research 74 (3) (1994) 407–419(5 May).

[25] H.A. Simon, The New Science of Management Decision, Harper & Row, New York, 1960.

[26] N. Srinivas, K. Deb, Multi-objective optimization using non-dominated sorting in genetic algorithms, IEEE Transactions on Evolutionary Computation 2 (1994) 221–248.

[27] US-EPA, Technology Characterization: Reciprocating Engines, Gas Turbines, Micro-Turbines and Fuel Cells, , 2008.

[28] US-EPA, Emissions Factors & AP 42, Compilation of Air Pollutant Emission Factors, http://www.epa.gov/ttnchie1/ap42/2011.

[29] F. Vince, F. Marechal, E. Aoustin, P. Bréant, Multi-objective optimization of RO desalination plants, Desalination 222 (2008) 96–118.

[30] T. Weise, Global Optimization Algorithms. da Global Optimization Algorithms, http://www.it-weise.de/2009.

[31] Yusliza Yusoff, Mohd Salihin Ngadiman, Azlan Mohd Zain, Overview of NSGA-II for optimizing machining process parameters, Procedia Engineering 15 (2011) 3978–3983.

[32] M. Zeleny, Multiple Criteria Decision Making, McGraw-Hill, 1982.

Dr. Patrizia Simeoni graduated in Industrial Technology Engineering and got a Ph.D. in Energetics (2005) at the University of Udine (Italy). From 2006 she's an adjoint professor of Waste Treatment Plants and Environmental Compatibility of Industrial Plants. From 2010 she is a researcher of Mechanical Plants at the University of Udine. Her main areas of research concerns Decision Support Systems (DSS) for energy and Environmental planning, Life Cycle Assessment (LCA), Multi-Criteria Analysis (MCA), Risk management, Industrial ecology. She's actively involved in research project of national relevance and works as a technical-scienti<sup>fi</sup>c consultant in the areas of waste management and soil remediation, developing and implementing decision support systems for enterprises and public bodies.

Alessandro Mattiussi graduated (2008) in Industrial Engineering at the University of Udine (Italy) and where he got the Ph.D. (2012) after a visiting period at Curtin University (Perth, Western Australia), with a thesis on “Decision Support Systems (DSS) for sustainable plant design”. Currently working for the Italian Industrial Association, he's researching on the Electricity and Gas Markets and Multi-Criteria Analysis in Energy Planning focusing on Life Cycle Assessments (LCA) of energy-converting technologies, and energy recovery in industrial contexts.

Michele Rosano. Ph.D., Director of Centre of Excellence in Cleaner Production (University of Western Australia, Perth), researching on Resource Economics, Sustainability Manage: ment, Life Cycle Assessment and Waste Management. She leads the Industrial Ecology Group within the Centre of Sustainable Resource Processing (CSRP). She worked internationally in the mining industry in a number of senior executive positions, and as a Lecturer and Researcher in Australia. She is currently assisting with the establishment of Australia's <sup>fi</sup>rst Industrial Ecology Networking organisation.
