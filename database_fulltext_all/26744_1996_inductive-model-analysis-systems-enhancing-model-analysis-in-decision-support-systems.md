---
otero_id: 26744
otero_key: "2NA3H2C9"
title: "Inductive Model Analysis Systems: Enhancing Model Analysis in Decision Support Systems"
authors: "Ramesh Sharda; David M. Steiger"
year: "1996"
journal: "Information Systems Research"
doi: "10.1287/isre.7.3.328"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR Information Systems Research

![](/api/attachments/2NA3H2C9/fulltext/images/43fbae24ad598445b854cccc20692fb9915018a5daecfc1ae1dfa0949d5b9b7a.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Inductive Model Analysis Systems: Enhancing Model Analysis in Decision Support Systems

Ramesh Sharda, David M. Steiger,

To cite this article:

Ramesh Sharda, David M. Steiger, (1996) Inductive Model Analysis Systems: Enhancing Model Analysis in Decision Support Systems. Information Systems Research 7(3):328-341. http://dx.doi.org/10.1287/isre.7.3.328

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article's accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1996 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/2NA3H2C9/fulltext/images/097bc8778d591d6f6eca69abd6362937261f5d5b41bdba950be8a4f7104c97ee.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Inductive Model Analysis Systems: Enhancing Model Analysis in Decision Support Systems

Ramesh Sharda • David M. Steiger

College of Business Administration, Oklahoma State University, Stillwater, Oklahoma 74078

sharda@orcs.bus.okstate.edu

Bryan School of Business and Economics, University of North Carolina at Greensboro, Greensboro, North Carolina 27412 steigerd@iris.uncg.edu

After building and validating a decision support model, the decision maker frequently solves (often many times) different instances of the model. That is, by changing various input parameters and rerunning different model instances, the decision maker develops insight(s) into the workings and tradeoffs of the complex system represented by the model.

The purpose of this paper is to explore inductive model analysis as a means of enhancing the decision maker's capabilities to develop insight(s) into the business environment represented by the model. The justification and foundation for inductive model analysis is based on three distinct literatures: 1) the cognitive science (theory of learning) literature, 2) the decision support system literature, and 3) the model management system literature. We also propose the integration of several technologies that might help the modeler gain insight(s) from the analysis of multiple model instances. Then we report on preliminary tests of a prototype built using the architecture proposed in this paper. The paper concludes with a discussion of several research questions.

Much of the previous MIS/DSS and management science research has focused on model formulation and solution. This paper posits that it is time to give more attention to enhancing model analysis.

(Decision Support Systems; Model Management; Cognitive Science; Inductive Model Analysis; Insight)

## 1. Introduction

In a decision support system (DSS), mathematical modeling consists of three processes: model formulation, solution, and analysis. Historically, most of the research and development efforts in DSS and operations research/management science have focused on model solution, specifically solution algorithms. Only recently have we seen research efforts which are devoted to developing model formulation aids such as modeling languages, graphical user interfaces, and knowledge-based tools intended to simplify the formulation process. Significantly less effort has been dedicated to post-solution analysis. (See §2 for notable exceptions to this general trend, i.e., for efforts directed toward post-solution analysis.)

In this paper, we focus on model analysis, specifically, the computer-aided analysis of multiple model instances representing the historical situations and/or what-if cases posed by the decision maker. The importance of such analysis is undeniable. Geoffrion states that “the true purpose . . . (of modeling) . . . is to develop insights into system behavior which in turn can be used to guide the development of effective plans and decisions. Such insights are seldom evident from the output of a single (model) run. One must know not only what the optimal solution is for a given set of input data, but also why" (Geoffrion 1976). That is, the true purpose of modeling, both during model building and during output analysis, is the process of understanding the system being modeled; e.g., which controllable variables interact with each other to affect the performance of the system.

To this, Jones adds that “developing insight into model behavior is ultimately a process of discovery, of finding trends, surprising behaviors, and comparing the behavior of the model to what is expected or observed in the real system. How well does it match? Where does it differ? Do those changes correspond to what is expected? If yes, why? If not, why not? In one sense, developing insight involves recognizing patterns: How does the model respond to changes in parameters? What trends can be detected? How do the trends compare?” (Jones 1992).

The common element in each of these statements is the development of insight, i.e., perceiving the inner nature of the tradeoffs inherent in any complex business situation. Yet understanding the problem is not always easily accomplished, especially when several, if not many, components of the situation interact and cause a combinatorial explosion of what-if possibilities, each of which by itself is difficult to analyze.

While some individual researchers have tried to focus on developing insights into the problem, the IS research community has devoted very little attention to insight development. Swanson and Ramiller (1993) analyzed the themes of papers submitted to Information Systems Research from 1987–1992. Their subject classification scheme does not include phrases such as “insight” or “analysis with models”, even though the basic purpose of information systems and DSS modeling is “insight, not numbers” (Hamming 1962, Geoffrion 1976). Admittedly, this evidence is from only one leading IS journal; however, it does show the dearth of emphasis placed on insightful analysis and understanding from information systems and DSS models. Without speculating on the causes of this inattention, we suggest that the information technologies have evolved to a point where IS should develop research concentrations in these areas.

The purpose of this paper is to explore inductive model analysis as a means of enhancing the decision maker's capabilities to develop insight(s) into the business environment represented by a DSS model. The paper is organized as follows. In the next section we identify the various types of analysis systems that have been developed thus far. In §3, we provide the justification and foundation for inductive model analysis systems, basing them on three widely diverse literatures: 1) the cognitive science (theory of learning) literature, 2) the DSS literature, and 3) the model management system literature. In §4, we develop an architecture for inductive model analysis systems, including components for the generation, storage and manipulation of multiple model instances. We also propose using several available technologies that are potentially productive in the development of insights via inductive model analysis. In §5, we describe a prototype implementation of an inductive model analysis system, called INSIGHT, and its application to a standard business analysis problem. In §6, we discuss several research areas for further development of insightful model analysis.

This research makes several contributions to the information systems/decision support system literature. First, it develops a framework for insightful model analysis by combining the theory of learning, DSS, and model management literatures. We are not aware of any previous attempts in using the theory of learning literature to identify the attributes of insight in model analysis. Second, it proposes a class of inductive model analysis systems based on the multiple model instances generated by a decision maker. Our proposal includes an architecture and a potential set of inductive technologies which could enhance model analysis. Our limited development and testing efforts lead us to conclude that there is promise in applying the inductive technologies for model analysis.

## 2. Model Analysis Systems

Current model analysis systems can be grouped into three categories based on the inherent type of processing logic employed: deductive analysis systems, statistical inference systems, and inductive analysis systems.

Deductive model analysis systems typically apply paradigm- or model-specific knowledge to a specific instance of the model, addressing such questions as "Why is this the solution?" or, in the case of linear programming (LP) models, "Why is this instance infeasible?" For example, ANALYZE (Greenberg 1990, 1993, 1994) is a computer-assisted deductive analysis system for linear programming (LP) models, and provides interactive query of the LP matrix and the solution values to 1) document and verify the model, 2) trace causation via network path analysis, 3) analyze causes of infeasibility, and 4) simplify the model via substructure elimination or imbedded network identification. ANALYZE provides "an artificially intelligent environment, with English translation of results automatically obtained" which is "well suited for the nonexpert of linear programming" (Greenberg 1994). Other deductive analysis systems include PERUSE (Kurator and O'Niell 1980) for LP models; I-KBS (Reddy 1985) and several domain-specific scheduling models (Donohue and Spearman 1993, Koltai et al. 1993) for stochastic models; and ROME/ERGO (Kosy and Wise 1984, 1986; Wise and Kosy 1986) and IFPS/PLUS (EXECUCOM 1992) for spreadsheet models. Each of these deductive model analysis systems is, by design, limited to analyzing one (or two, in the case of ROME/ERGO and IFPS/PLUS) model instance at a time. Further, these systems are limited to a single modeling paradigm or problem domain.

Statistical inference systems compute standard summary statistics of the model's output variable(s) based on a set of randomly generated model instances, displaying the results in numerical and/or graphical form. This allows risk and uncertainty to be included explicitly or implicitly in a model. For example, @RISK (Palisade 1991), an add-in to spreadsheet software, calculates the mean and standard deviation of an output variable (e.g., a corporation's profits) from instances generated by a Monte Carlo simulation applied to stochastic distributions of one or more input variables (e.g., sales and cost-of-good-sold). In addition to @RISK, statistical inference systems include general simulation models. These modeling systems are limited, by design, to producing summary statistics and do not address other analysis questions, such as "Which stochastic parameter has the greatest impact on the model's output?" or "Does some subset of stochastic parameters interact to influence the model's output?"

Inductive model analysis systems (IMAS) operate on a set of related model instances which represent historical situations familiar to the decision maker and/or what-if cases generated by him/her. The goal of these analysis operations is to provide the decision maker with assistance in analyzing the model instances s/he has generated—specifically, to enhance the development of insight(s) into the decision making environment based on the set of model instances.

Inductive model analysis systems are distinguished from deductive analysis systems by both the required input and the type of processing logic employed. That is, deductive analysis systems operate on one or two model instances and apply existing model- or paradigm-specific knowledge to the specific model instance, whereas IMAS operate on many user-specified solved instances and apply inductive analysis technologies to generate new knowledge. Also, IMAS provide results which are independent of the modeling paradigm, matching the generality and analysis requirements of state-of-the-art modeling languages such as Structured Modeling (Geoffrion 1987, 1989).

Furthermore, IMAS are distinguished from statistical inference systems by the scope of their functionality. That is, statistical inference systems deal only with determining the distribution of the stochastic output variables, whereas the scope of IMAS is much broader. IMAS include insightful analysis tasks such as identifying key parameters, finding and explaining the primary differences between multiple model instances, developing causal relations between input parameters and output variables, planning which what-if model instance(s) should be solved to complete an interesting study or sequence of instances, estimating impacts of incremental and nonincremental changes in parameters and model structure, recognizing patterns in model behavior, etc. (see Steiger and Sharda (1995) for a technical description of these analysis tasks, the questions they address and potential implementation technologies which are applicable).

This is not to say that research on deductive and statistical inferential systems should be abandoned, but that inductive analysis systems can provide additional analysis capabilities based on the application of a different set of (inductive) technologies.

There are currently three systems which can be classified primarily as IMAS. One is LISA (Saltelli and Homma 1992 Saltelli and Marivoet 1990), a system which uses standardized rank regression coefficients and partial rank correlation coefficients to determine the key parameters in a probabilistic model, i.e., those input parameters which are most important in determining variations in the output variable. However, LISA does not address the other insight-generating analysis tasks. Further, LISA assumes a large (>1000) number of model instances based on known distributions of input parameters, both of which are often unavailable in many decision making analyses.

A second approach that can be classified as an IMAS is Global Sensitivity Analysis (Wagner 1993). The goal of this analysis is to provide sensitivity analyses based on the analysis of a set of solved model instances. The input to Global Sensitivity Analysis consists of: 1) the marginal distributions of up to ten stochastic model parameters or groups of parameters, where a parameter might be an objective function coefficient, a right-hand side value, or a matrix coefficient, if the model is a linear programming model, 2) a prespecified set of nonlinear, multinomial terms involving the stochastic parameters, with the set of terms based on a priori human knowledge or model-specific expertise, and 3) a large set of (perhaps 2,000) solved model instances obtained by repeatedly varying (via Monte Carlo simulation) one or more of the stochastic parameters and resolving the model. Processing consists of using backward, stepwise, least-squares regression to find the “best fit” between some subset of multinomial terms and the set of instance solutions. The output is the best fit polynomial (consisting of an additive model of 20–40 or more multinomial terms) and the associated regression coefficients, along with the coefficient of determination, $R^{2}$ . This output is then used to determine the sensitivity of the original model to changes in a given parameter and to determine which stochastic parameter(s) are most influential in the model solution. The primary advantages of Global Sensitivity Analysis include the following: 1) least-squares fits using multinomial terms can be used to provide good approximations for “explaining” the variations in solutions to many complex linear programming and decision analysis models, and 2) all software used in this system is commercially available as add-ins to standard spreadsheet packages.

A third system which can be classified as an IMAS is the prototype system named INSIGHT described further in §5. The goal of this system is to generate, using artificial intelligence, a simplified auxiliary model which helps the decision maker develop insight(s) into the business environment being modeled. The input to INSIGHT consists of a small set of solved model instances generated either by the decision maker through a series of what-if instances or by Monte Carlo simulation, if the marginal distributions of the stochastic parameters are known or estimated. Processing consists of two sequential steps: first, using the Group Method of Data Handling (GMDH) algorithm (Ivakhnenko 1971, Farlow 1984) to generate an additive model of multinomial terms which explain variations in the solutions to the model instances specified above, and second, using stepwise regression to find a "best fit" simplified auxiliary model between some subset of the GMDH-produced multinomials and the set of instance solutions. The output is the closed-form, simplified auxiliary model which helps the decision maker develop insight(s) into the interactions and tradeoffs between model parameters, as well as the sensitivity of model solutions to changes in parameter values. We suggest that such simplified meta-models, consisting of additive multinomial terms, are conducive to insight generation (see §3) by the decision maker since: 1) they focus attention on the key model parameters, 2) they give priority, as much as possible, to simple relations and tradeoffs, 3) they recognize and highlight patterns, 4) they are based on instances which the decision maker has specified and is familiar with, and 5) multinomials can approximate virtually any linear or nonlinear relationship (response surface) between dependent and independent variables.

The advantages of using GMDH in these applications include the following: 1) no prior knowledge or preestablished set of multinomials is required, 2) a smaller set of samples (i.e., solved model instances) is required as compared to standard regression, 3) no assumptions with respect to linearity or continuity of the solution values (e.g., objective function values in the case of LP models) or normality of residuals are required, and 4) chances of overfitting are reduced (Prager 1988, Barron 1984, Barron et al. 1984).

It must be noted that one post-analysis approach, named Candle-Lighting (Kimbrough and Oliver 1994; Kimbrough et al. 1990, 1992, 1993), is unique in that it spans our deductive-statistical-inductive taxonomy, having analysis components in each. That is, Candle-Lighting has a deductive analysis component (which provides submodel and surrogate model analysis), a statistical analysis component (which applies simulation for exploring the impact of changing different parameter values), and an inductive analysis component (which creates, analyzes, and orders/summarizes model instances via genetic algorithms).

## 3. Justification and Foundations for Inductive Analysis Systems

Three distinct literatures form the justification for, and the foundation of, inductive model analysis systems. These include: 1) the DSS literature, especially as it relates to the decision maker's use of a model, 2) the cognitive science (theory of learning) literature, especially as it relates to the decision maker learning from a model via insight generation, and 3) the model management system literature, especially as it relates to knowledge discovery and paradigm independence. Each of these is discussed individually below.

## DSS Literature

Once a model is built and run, the decision maker's job has just begun. He develops his understanding of the problem and the model solution by iteratively analyzing several, if not many, model instances, formulating and testing hypothesized interrelationships between model parameters and the model solutions (Little 1970). That is, he uses the model to develop insights into his decision making environment (Geoffrion 1976). However, developing insight(s) from the manual analysis of multiple instances is not elementary, especially when the number of instances increases, say to five or more. Thus, there is a need, based on the practitioners' use of a model, for computer-assisted analysis of model instances.

Insights can be the product of any of the several model analysis tasks performed by the decision maker. We divide these analysis tasks into two broad categories: model validation and what-if analysis. (Other researchers have opted for more detailed classification schemes (Brennan and Elam 1986, Elam and Konsynski 1987).)

Model validation consists of selecting historical situations familiar to the decision maker, constraining the mathematical model to represent these situations, running the model, and comparing the model's output with the decision maker's expectation to determine whether there is a high correlation between the results predicted by the model and what would actually happen in the real world or what the decision maker would expect to happen (Hillier and Lieberman 1990). High correlation for a number of such instances establishes confidence in the model's validity. Low correlation may lead to finding and correcting an error in the model, and subsequent retesting and validation of the corrected model. If no syntactical or semantical error is found in the mathematical model, the decision maker may question the validity of his own mental model of the situation. This may, in turn, lead to insightful learning by the decision maker, i.e., the revision of his mental model.

What-if analysis consists of running several, and perhaps many, what-if cases (i.e., model instances) to generate and test hypotheses concerning the decision making environment. The purposes of these what-if analyses include identifying key parameters, determining relative sensitivities of various parameters, developing causal relationships between key parameters and the model's solutions, evaluating the effects of uncertainty in one or more parameters, estimating the impact of relaxed/tightened constraints, etc. Each of these what-if analyses, and the associated model instances, may be used by the decision maker to generate insight(s) into the business environment.

If the decision maker is one of several members in a group, he may have additional analysis tasks. For example, in group decision making, where all members are capable of understanding the problem as a whole (Rasmussen et al. 1991), the decision maker may want to classify the cumulative what-if cases into clusters of related instances, and analyze a specific cluster, even though some of these instances were originally generated by other group members. Alternatively, in distributed decision making, where each group member has expertise in only a limited part of the whole problem (Rasmussen et al. 1991), a decision maker might want to analyze the impact of his decision alternatives on the model as a whole.

Each of these analysis tasks may require from two to some large number (perhaps 200 or more) model instances from which the decision maker attempts to develop generalization(s) and insight(s) (Geoffrion 1975). Manual analysis of these cases becomes increasingly difficult for more than a handful of instances. An inductive model analysis system is appropriate since the basis of analysis is a set of specific model instances from which the decision maker attempts to develop generalization(s) and insight(s), perhaps in the form of mathematical relationships between the parameters which are varied and the model solutions.

Table 1 Characteristics of Insight and Insight-generating Models

<table><tr><td>Characteristics of Insight from the Theory of Learning</td><td>Characteristics of Insight-generating DSS Analysis Tools</td></tr><tr><td>Subject organizes field into figure and ground, figure is analyzed and ground is ignored</td><td>Simplified auxiliary models and metamodels focus on key parameters, ignoring insignificant details</td></tr><tr><td>Subject looks for simplicity, regularity.</td><td>Inductive tools determine linear and nonlinear relationships between key parameters, with simple relations given priority</td></tr><tr><td>Subject organizes his/her own patterns</td><td>Inductive technologies include pattern recognition, pattern generation and pattern comparison capabilities. Alternative technologies can be used to generate possibly different patterns from same data</td></tr><tr><td>Tendency to perceive incomplete material as complete</td><td>Generated patterns are generalizable</td></tr><tr><td>Former experience forms a frame of reference.</td><td>Requires a comprehensive database of patterns and what-if instances, also an instance generator</td></tr></table>

Thus, the practitioner's modus operandi in using a DSS strongly suggests the need for a computer-assisted inductive analysis system to enhance his generation of insight(s) into the decision making environment. It also implies a need for 1) an instance generator (to help generate a set of instances over some range of parameter values), 2) a database of model instances (to store and retrieve instances), 3) a set of multiple instance analysis tools (featuring several inductive analysis technologies to address the different analysis tasks), and 4) a user-seductive interface (to interpret the results of analysis and present them in a form conducive to insight development by the decision maker).

## Cognitive Science (Theory of Learning) Literature

The study of insight was popularized by the Gestalt psychologists in the early 1900's and forms one of the bases of their theory of learning. In this literature, insight is defined as the sudden, clear and holistic understanding of the essential relationships of the problem, frequently involving the combination of previously learned facts or responses into new and novel patterns and combinations of patterns; a quality of perception (Hilgard 1956; Logan and Ferraro 1978; Kohler 1925, 1969; Lee 1965).

According to the theory of learning literature, insight has five basic characteristics (Lee 1965). Applying these five characteristics to the decision making, insightful decision making includes the following: 1) the decision maker organizes his environment into the "figure" (the thing on which s/he focuses all attention) and the "ground" (everything else in the environment, which is subsequently ignored)—like a seasoned hunter who focuses all his attention on the target (i.e., the "figure") and ignores the surrounding trees, grass, and other animals (i.e., the "ground"), 2) the decision maker tends to look for simple and regular relations in the situation presented to him, 3) there is a tendency to perceive incomplete material as complete, 4) the decision maker organizes patterns from the data presented to him, and after using a pattern to solve one problem, can use it directly, and in generalized form, to solve the same and similar problems presented to him later on, and 5) the decision maker works within a frame of reference consisting mainly of former patterns and situations from his experience (Lee 1965, Lonergan 1958, Hilgard 1956).

These five characteristics of insight from the theory of learning suggest several corresponding desired characteristics for insight-generating Inductive Model Analysis Systems (IMAS) (see Table 1). Specifically, the organization of the environment into “figure” and “ground” corresponds to the desired characteristic of the IMAS to determine key parameters and variables in the mathematical decision model, i.e., to determine a minimum set of key factors which are necessary and sufficient to explain variations in the model's behavior over a specified set of circumstances or model instances. Likewise, the search for simple, regular relations corresponds to the desired characteristic of the IMAS to determine linear and nonlinear relationships among the minimum set of key factors which sufficiently and insightfully explain the model's behavior. Kohler states that this is one of the most basic characteristics of insight in that "all problems with which we may be confronted, and also the solutions of such problems, are matters of relations; not only does our understanding of the problem demand our awareness of certain relations, we cannot solve the problem without discovering certain new relations" (Kohler 1969, 143–144).

The insightful organization of patterns suggests that the IMAS should provide a significant pattern recognition capability. In decision making, such patterns may be generated by the analysis of multiple, related what-if instances posed by the decision maker while trying to validate the model or understand the effects of parameter perturbations. In addition, the IMAS should incorporate multiple methods and technologies which generate several different patterns for the same data, since insight frequently comes from rearranging old patterns, as well as generating new patterns (Kohler 1969, Hilgard 1956, Logan and Ferraro 1978).

The tendency to perceive incomplete material as complete implies a generalization requirement for the IMAS. That is, the key factors, relationships, and patterns generated from a specified set of model instances should be applicable to similar situations for which they have not been explicitly designed, thus enabling the IMAS to provide valid insights and conclusions when presented with a new decision situation or input pattern that is different from those on which it was based (Dayoff 1990).

The importance of former experience forming the frame of reference for insights suggests that the IMAS should provide a comprehensive database of stored model instances which reflect historical situations familiar to the decision maker and what-if situations posed by him. The need for many model instances, in turn, implies a requirement for a user interface specialized in specifying model instances.

## Model Management Systems Literature

Model management systems (MMS), one of the three primary components of a DSS, are operating systems for models whose purpose is to support the general description, manipulation (solution, integration, analysis and presentation) and control (access authorization, integrity, security and privacy) of models (Chang et al. 1993, Dolk 1986, Blanning 1993). In general, the goal of MMS is to do for models what database management systems (DBMS) do for data. Thus, research directions and priorities of MMS should parallel those of DBMS.

One of the highest priority research topics for the 1990's in DBMS is the exploitation of machine learning and knowledge discovery as an aid to assembling knowledge (data)bases. Knowledge discovery is the nontrivial extraction of implicit, previously unknown, and potentially useful information from data, i.e., the discovery of patterns that are both interesting and certain enough to be of value to the decision makers (Frawley et al. 1992). Technologies incorporated in knowledge discovery include ID3 (for expert systems shells), inductive methods, neural networks and genetic algorithms, to mention a few.

If we think of multiple instances in a MMS as a relational database of model instances, with each model instance represented as an entity consisting of parameter values and its model solution as attributes, then knowledge discovery is directly applicable to model analysis. That is, knowledge discovery could extract the interesting patterns and trends from a specified set of model instances, thus enhancing the decision maker's insight generating capabilities.

Thus, knowledge discovery in intelligent DBMS strongly suggests inductive analysis as an appropriate methodology when analyzing multiple model instances in an MMS. It further suggests self-learning technologies (e.g., neural networks, genetic algorithms and inductive statistics), a database of model instances and an intelligent interface to translate mathematical equations into more understandable logical rules.

Another current research area in MMS is structured modeling, a framework and computer-based environment for conceiving, representing and manipulating a wide variety of models (Geoffrion 1987, 1989). One of the primary features of structured modeling is its paradigm-independent generality, i.e., its ability to encompass most of the modeling paradigms (Geoffrion 1987). This implies the need for a matching paradigm-independent generality in model analysis systems, which, in turn, implies the use of inductive analysis technologies since deductive knowledge would inherently force paradigm dependence. For example, the knowledge used in ANALYZE (Greenberg 1990) is deduced from the MPS input matrix, linear programming solution tableau and LP-specific rules, and is thus limited to LP-based models. IMAS, on the other hand, could be used in other modeling paradigms as well.

Table 2 Summary of Implied/Required Inductive Analysis Capabilities

<table><tr><td>Views</td><td>Implied/Required Inductive Analysis Capabilities</td></tr><tr><td>DSS View- Validation and What-if Analysis</td><td>Inductive analysis of many instancesSet of analysis toolsInstance generatorDatabase of model instancesUser-seductive interface</td></tr><tr><td>GDSS</td><td>Clustering of instancesPerturbation analysis</td></tr><tr><td>Theory of Learning View</td><td>Key factor determinationSufficiency measureLinear and nonlinear relation generatorExplanatory measure(s)Multiple pattern recognition technologiesDatabase of instancesInterface for specifying instancesComputer-assisted instance generator</td></tr><tr><td>Model Management View</td><td>Database of instancesKnowledge discovery using self-learning,inductive technologiesIntelligent interfaceParadigm-independent generality</td></tr></table>

## Summary of Inductive (and Other) Analysis Capabilities

A summary of the analysis capabilities required or implied by the three literatures discussed above is provided in Table 2. This literature survey forms the framework for IMAS in general, and the foundation for the proposed inductive model analysis architecture.

## 4. Inductive Model Analysis Systems: An Architecture

Based on the requirements and characteristics dictated by the three literatures discussed above, we propose an inductive model analysis system architecture consisting of four major components: 1) a model instance database, 2) an analysis toolkit consisting of several tools using various inductive technologies, 3) an instance generator to support the creation of multiple model instances under decision maker control, and 4) a user interface module. Each of these four components, along with their respective interactions, is depicted in Figure 1 and described briefly. This logical design of IMAS is derived from the functional requirements summarized in Table 2, and is independent of any specific hardware or software specifications. Note that the direction of the arrows in Figure 1 indicate the direction of communication or information flow, e.g., the decision maker communicates, via the user interface, the specific parameters and model instances to be used in an analysis, and the results are then communicated, via the user interface, back to the decision maker.

## Instance Database

The instance database can be thought of as a relational database with at least two types of model instances: what-if instances and historical situations both stored in the form of tuples. Each tuple has multiple attributes, one attribute for each model input parameter value, one for each (solved) decision variable value, one for the overall solution level (e.g., objective function value) and one for each solver specific parameter value. That is, each tuple contains all the information required to identify and recreate the solution for a specific model instance, as well as the solution itself.

Figure 1 Logical Design of an Inductive Model Analysis System (IMAS)  
![](/api/attachments/2NA3H2C9/fulltext/images/040e19ec430fcfa9eada9baaa3da46102f35d1802530203ce8e57c90e45d0368.jpg)

## Instance Generator

What-if scenarios may be created manually by the decision maker/analyst, or may be generated under computer control. In the latter mode, the Instance Generator creates a set of n instances based on the user-specified ranges of one or more model parameters. If the parameter is stochastic in nature and the user specifies the appropriate distribution characteristics, a Monte Carlo simulation is implemented. If the user specifies only ranges over which several parameters, decision variables and/or solution values are reasonable, the instance generator insures the generated instances cover, to the extent possible, the entire potential solution space. For example, in a warehouse location model with a maximum of 13 locations possible, if the user specifies the valid ranges of several interacting parameters (without the associated distributions), then the instance generator will vary the parameter values so that the created set of instances will represent each input parameter throughout its valid range, as well as the output variable (optimal number of warehouses) throughout its valid range (1–13).

## User Interface Module

The user interface is a loosely-coupled system which passes requests, data and results between the decision maker and the other IMAS components, i.e., the analysis toolkit, the instance generator and the instance database. For example, the decision maker may specify a certain tool to analyze a given range of instances, providing a tolerance or quality measure. Alternatively, the decision maker may request the generation of a set of instances based on a specified range of values for a given model parameter.

## Analysis Toolkit

The analysis toolkit is a repository for tools or modules designed to analyze multiple model instances and help the decision maker generate insight(s) into the complex situation being modeled. In general, these tools address the several fundamental model analysis tasks described in §3, applying both classical and state-of-the-art technologies to the analyses. Whereas our prototype system (INSIGHT, described in §5) included only GMDH and classical statistics in the analysis toolkit, other potentially applicable toolkit technologies include neural networks, statistical cluster analysis, rank regression and correlation coefficients, the group method of data handling (GMDH) with coefficients of determination, and perturbation analysis, each of which is discussed briefly in the following paragraphs. Note that this is an illustrative (not definitive or exhaustive) list of applicable technologies.

Kohonen networks (Dayoff 1990, Wasserman 1989) and statistical cluster analysis are potentially applicable technologies for preprocessing model instances generated from Group DSS into groups of related model instances. Kohonen networks are self-organizing neural networks that accept instance tuples (representing values of model parameters and variables) and produce a two-dimensional “similarity” feature map in which distances between two groups of instances are approximately proportional to the dissimilarity of parameter values in different model instances. Once instances have been so grouped, the decision maker can analyze each group individually for insights germane to the instance similarities.

Rank regression coefficients and rank correlation coefficients have been used to help identify key parameters in stochastic models, i.e., those stochastic parameters which have the largest influence on the value of the output variable. This is sometimes referred to as Sensitivity Analysis in the risk and analysis literature (Saltelli and Marivoet 1990, Saltelli and Homma 1992). However, such techniques “can lead to misinterpretation of the results, … particularly when the output under consideration is a time dependent function of the input parameters” (Saltelli and Homma 1992, p. 92).

Group method of data handling (GMDH) algorithms (Prager 1988, Farlow 1984) are potentially useful in developing insight-generating relations between input parameters and the output variable of interest, as well as identifying the key parameters of a DSS model. GMDH are self-organizing, nonparametric methods which accept, as input, the instance tuples. They typically generate, as output, a proposed mathematical model, represented as a multilayered, cascading network of second- or third-degree polynomial equations whose parameters are optimized to minimize the error between the proposed model and the training data. GMDH has at least two basic advantages over classical statistical techniques: 1) GMDH requires no a priori knowledge of the model structure, i.e., of the linearity or nonlinearity, the degree of any term, or the interactions of any two or more input variables, and 2) GMDH can construct a high degree polynomial (say of degree 8 in 20 variables) with as few as 100 tuples (data points), as opposed to the millions of tuples required for such a task in classical statistical techniques (Prager 1988, Barron 1984, Barron et al. 1984). However, GMDH models do tend to be quite complex, with many multinomials in each model, potentially hiding important insights. This potential problem can be alleviated by generating a simplified submodel via stepwise regression (Prager 1988, Sharda and Steiger 1995).

Perturbation analysis can be used to evaluate the impacts of changes in one parameter on the model as a whole, as is required in distributed decision making. Perturbation analysis involves finding the gradient of some performance measure and using this gradient to calculate effects of changes in a parameter on the performance measure or model. It has been applied to discrete event dynamic systems (Ho and Cao 1991), to the design of stochastic production lines (Donohue and Spearman 1993) and to operation scheduling (Koltai et al. 1993).

These represent only a few potential applications of new and classical technologies to the development of insights in a modeled business environment. Others, as developed, will represent candidates for addition to the analysis toolkit of IMAS.

## 5. Prototype Implementation of an Inductive Model Analysis System: Insight

We have developed a prototype implementation of an IMAS with some of the functionality proposed earlier. Our software, named INSIGHT, is essentially a relation generator. INSIGHT, which would be one of several tools in the IMAS Analysis Toolkit (Figure 1), analyzes multiple model instances to: 1) generate one or more insightful relations between key parameters and the model's behavior, and 2) identify the critical model parameters. A general description of INSIGHT was provided in §2.

## Implementation Technologies

INSIGHT is implemented in the spreadsheet environment of Excel (version 4.0) (Microsoft 1992). Excel was chosen because it provides 1) an instance storage capability, Scenario Manager, 2) add-in capabilities for a multitude of model solvers, and 3) an extensive macro programming capability for data handling and user interface control.

To determine the critical factors and key relations, INSIGHT incorporates 1) the inductive Group Method of Data Handling (GMDH) (Prager 1988, Barron et al. 1984, Farlow 1984), of AIM, (AbTech 1990) a commercially available, self-learning analysis package which produces an nth order, cascading, multiple-termed polynomial relation between parameter values and model solutions, 2) Excel's statistical analysis capabilities to determine the correlation coefficients and coefficients of determination for each term in the GMDH polynomial relation, and 3) an Excel macro to select the simplest relation which explains a high proportion, say $80\%$ , of the variation in the model's behavior. (For a complete description of the INSIGHT software, see Sharda and Steiger (1995).)

## Preliminary Testing

To illustrate the INSIGHT software, we formulated a facility location model for a test case. Geoffrion (1976) used a similar model to illustrate the development of insight-generating simplified auxiliary models. The general facility location model, formulated using mixed integer linear programming, is as follows:

$$
\text { Min } \quad \Sigma_ {i} \Sigma_ {j} t _ {i j} * x _ {i j} + \Sigma_ {j} f * y _ {i}
$$

s.t. $\Sigma_{i}x_{ij} = p_{j}$ for every $j$ ,

$$
\Sigma_ {i} x _ {i j} - M * y _ {i} \leq 0 \quad \text { for   every } i,
$$

$$
y _ {i} = 0, 1 \quad \text { for   every } i,
$$

$$
x _ {i j} \geq 0 \quad \text { for   every } i, \text { for   every } j, \quad \text { where }
$$

$x_{i,j} =$ product shipped from the warehouse located in city $i$ to satisfy demand in city $j$ ,

$t_{i,j}$ = transportation cost (\$/unit shipped) from warehouse i to demand point j,

$f_{i} =$ fixed costs associated with building a warehouse in city $i$ ,

$p_{i} =$ product demand in city $j$ , and

$y_{i}$ = a binary variable which is 1 if a warehouse is acquired/opened in city i, and 0 otherwise.

To this formulation, Geoffrion (1976) added seven simplifying assumptions, namely:

1. Demand is uniformly distributed on the plane with a density of $p\left(\mathrm{CWT}/\mathrm{mi}^{2}\right)$ where CWT is hundred weight of product shipped.

2. All warehouses are identical and arbitrarily relocatable.

3. The supply cost for each warehouse is s (\$/CWT) regardless of its location.

4. The fixed cost of each warehouse is f (\$).

5. The variable throughput cost of each warehouse is v (\$/CWT).

6. The outbound freight rate for each warehouse is t (\$/CWT-mi).

7. There are no throughput limits for the warehouse.

He then used human expertise and mathematical manipulation to generate the following insight-generating simplified auxiliary model for the optimal number of warehouses, $n^{*}$ , for an area having A square miles of area:

$$
n ^ {*} = A / 3. 0 5 * (p * t / f) ^ {2 / 3}.
$$

Our illustrative model incorporates approximately the same set of assumptions used by Geoffrion. However, in our model, demand is evenly distributed among the 13 potential cities instead of being uniformly distributed throughout the plane. Thus, our model represents lumpy demand located in 13 fairly centrally located (but not exactly equidistant) cities, where distances between cities are actual highway mileages. Our model depicts the cities in Central Texas, an arbitrary locale chosen simply because a map showing city-to-city driving distances was handy at the time.

The facility location model was formulated as a $13 \times 13$ city mixed integer linear programming model using the What's Best! (Savage 1992) software package to solve specific instances. As an illustration of the IN-SIGHT software, we generated and solved a set of 24 model instances, each with a different value of one or more of the following variables: total demand, p, warehouse-to-customer transportation rate, t, and/or warehouse fixed costs, f.

Any instance which resulted in an optimal number of warehouses greater than one and less than 13 was accepted as one of the instances to be analyzed by IN-SIGHT. In addition, we ensured that there were at least two model instances which depicted different values for each of the three model variables mentioned above. Both of these restrictions, concerning the selection of model instances to be used in the analysis, could easily be implemented in an expert system module within IN-SIGHT.

GMDH algorithms cannot generate simple models for common terms such as 1/x, sqrt(x) and cos(x). For example, cos(x) would be approximated by an 18th order polynomial, patently unsuitable for our simplified auxiliary model. To address this potential problem, we included in INSIGHT a routine to automatically add 1/x and sqrt(x) for each of the independent input variables specified in Scenario Manager since these are common terms which might be potential components of any simplified auxiliary model. (A future enhancement to INSIGHT will include the capability for the user to specify such terms at his discretion.)

Based on these 24 model instances, the INSIGHT tool generated the following simplified auxiliary model:

$$
n ^ {*} = 7 0 0 * (p * t / f)
$$

using the same three key variables as used in the Geoffrion model in an even more simplified form. This single term explained 92% of the total variation from average of the optimal number of warehouses; i.e., $R^{2} = 0.92$ . A side-by-side comparison of Geoffrion's results and those of INSIGHT is shown in Table 3.

Table 3 Test Problem Results and Comparison

<table><tr><td>Geoffrion</td><td>Insight</td></tr><tr><td>Method</td><td>Method</td></tr><tr><td>Human expertise</td><td>Artificial intelligence</td></tr><tr><td>Mathematical knowledge</td><td>Statistical software</td></tr><tr><td>Mathematical simplification</td><td>More realistic assumptions</td></tr><tr><td>Mathematical manipulation</td><td>Multiple instances</td></tr><tr><td>Relation generated</td><td>Relation generated</td></tr><tr><td> $n^{*} \approx (p*t/f)^{2/3}$ </td><td> $n^{*} \approx p*t/f$ </td></tr></table>

INFORMATION SYSTEMS RESEARCH
Vol. 7, No. 3, September 1996

Table 4 gives an indication of the robustness of the INSIGHT results to the number of instances analyzed. In this model, at least, the INSIGHT results degrade gracefully (with respect to $R^{2}$ ) down to the 10–15 instance range. This indicates that only a modest number of rationally selected instances were required to generate the insightful results shown. Actual results in other models would depend on the model, modeling paradigm, specific instances, complexity of relationship, etc.

Thus, the INSIGHT software, using inductive analysis technologies as applied to the analysis of multiple model instances, was able to duplicate the insight-generating simplified auxiliary model produced by Geoffrion without using human expertise or mathematical manipulations based on simplifying assumptions. This provides a preliminary illustration (but not a proof) of the concepts of IMAS and the concepts and implementation of the INSIGHT software.

Note that this relation between p, t, f and $n^{*}$ is valid when all other model parameters are held constant. If other parameter values were varied, those additional parameters, their values and the associated model solutions could be added to the set of instances included in the INSIGHT analysis. Then, if they had a significant impact on the output parameters, they would be included as key factors and included in a (new) relation; else, they would be ruled out as key factors and would not enter into the key relation. In some models, knowing that a parameter, varied over an appropriate range of values, would not affect the output might be very valuable information indeed.

## 6. Research Directions

There are several major research areas which have potentially significant contributions to the insightful analysis of model solutions. The first of these concerns the research and development of additional links between the theory of learning literature and decision support systems. Given that insight is a form of learning, a major purpose of modeling is learning from the analysis of model solutions, not just implementing the solution a model produces. Insightful learning may occur from both deductive systems, such as from rule-based knowledge, and inductive systems, as from multiple instance analysis. In either case, we need to know more about the characteristics of insight, what triggers it, how it differs from decision maker to decision maker, what prerequisites it depends on, when in the analysis process it is most likely to occur, and what types of relations and presentations of those relations are most likely to encourage it. Given that “insight” does not appear as a keyword in an Information Systems Research summary (Swanson and Ramiller 1993), we propose that more research is needed to identify and define the concept of insight as a function of IS use.

<table><tr><td colspan="2">Table 4 Sensitivity of the Insight Model to Number of Instances Analyzed</td></tr><tr><td># Instances</td><td> $R^{2}$  for Relation</td></tr><tr><td>15</td><td>0.88</td></tr><tr><td>24</td><td>0.92</td></tr><tr><td>48</td><td>0.94</td></tr></table>

In the DSS literature, especially the management science aspects of it, the focus of research has been modeling and solution techniques. It is time now to give analysis of solutions the importance it deserves. An early task in this regard is to articulate the purpose of model analysis. Several DSS researchers (Brennan and Elam 1986, Elam and Konsynski 1987) have attempted to develop some theory in this vein, but it is still an area needing further refinement. We need to identify a “minimal spanning set” of tasks that leads to successful model analysis and validate these tasks through experimentation.

While we have proposed a logical design for IMAS, specific implementations would entail the use of various technologies. We need to explore and evaluate those technologies which are potentially applicable to insightful model analysis. This might include both commercially available software packages and research systems which implement one or more of these technologies. Initial evaluation could match the input, processing, output and feedback characteristics of the technologies against the corresponding characteristics of the prime analysis tasks mentioned above. The results could provide a research agenda for the application of the technologies to the analysis tasks, and if successful, the addition of that technology to the IMAS analysis toolkit.

The sampling of research tasks identified above include potential applications of field research as well as laboratory methods. We need to begin with an understanding of the insight related tasks of IS use, develop and test IMAS in laboratory experiments, and then test the applicability of such systems in practice. For example, we might design a laboratory experiment to test the ability of the INSIGHT-generated relations ( $§4$ ) to enhance a subject's insight generation capability. For this, we might adapt the basic design and insight measurement criteria (differences in “warmth ratings” as a function of time-to-solution) proposed by Metcalfe (Metcalfe 1986a, 1986b; Metcalfe and Wiebe 1987).

In addition, we need to further refine and develop the overall architecture conducive to model analysis, in general, and inductive model analysis, in particular. We also need to address the critical issues related to instance management within the model management systems (MMS) context.

## 7. Conclusions

In this paper we have argued that model analysis needs to receive more attention from the IS researchers. We have made a first attempt (we believe) to synthesize the literature from the theory of learning perspective (especially with respect to insight generation) with the DSS modeling literature to develop a framework for various approaches to model analysis to enhance insight into the decision problem. We have proposed that analysis systems based on inductive analyses of multiple model instances (IMAS) are appropriate for developing some insight into the problem. We proposed an architecture for such systems, and described a prototype built along this architecture. Preliminary tests of this prototype using a seminal case analysis suggests that the inductive model analysis systems are worthy of further development and investigation.

## References

AbTech, Abductory Inductive Models—User's Manual, AbTech, Inc., Charlottesville, VA, 1990

Barron, A. R., "Predicted Squared Error. A Criterion for Automatic Model Selection," in S. J. Farlow (Ed.), Self-Organizing Methods in Modeling. GMDH Type Algorithms, Marcel Dekker, New York, 1984, 97–103.

Barron, R. L., A N Mucciardi, F J. Cook, A R Barron and J N Craig, "Adaptive Learning in Networks Development and Applications in the U S of Algorithms related to GMDH," in S. J Farlow (Ed.), Self-Organizing Methods in Modeling GMDH Type Algorithms, Marcel Dekker, New York, 1984, 25–66

Blanning, R. W., "Model Management Systems: An Overview," Decision Support Systems, 9 (1993), 9–18

Brennan, J J and J. J Elam, "Understanding and Validating Results in Model-Based Decision Support Systems," Decision Support Systems, 2 (1986), 49–54

Chang, A, C W Holsapple, and A B Whinston, "Model Management Issues and Directions," Decision Support Systems, 9 (1993), 19–37

Dayoff, F., Neural Network Architectures, Van Nostrand Reinhold, NY, 1990

Dolk, D R., "A Generalized Model Management System for Mathematical Programming," ACM Trans Math. Software, i2, 2 (1986), 92–126

Donohue, R. L. and M. I. Spearman, "Improving the Design of Stochastic Production Lines: An Approach Using Perturbation Analysis," International J Production Research, 31, 12 (1993), 2789-2806

Elam, J J and B Konsynski, "Using Artificial Intelligence Techniques to Enhance the Capabilities of Model Management Systems," Decision Sciences, 18, 3 (Summer 1987), 487–501

EXECUCOM, Interactive Financial Planning System: User's Manual, EXECUCOM, Austin, TX, 1992

Farlow, S J (Ed.), Self-Organizing Methods in Modeling: GMDH type Algorithms, Marcel Dekker, New York, 1984

Frawley, W J, G Piatetsky-Shapiro and C J Matheus, "Knowledge Discovery in Databases: An Overview," AJ Magazine, Fall (1992), 57–70

Geoffrion, A M, "The Purpose of Mathematical Programming is Insight, Not Numbers," Interfaces, 7, 1 (1976), 81–92

——, “An Introduction to Structured Modeling,” Management Sci, 33, 5 (1987), 547–588

---, "The Formal Aspects of Structured Modeling," Oper. Res., 5 (1989), 30-51

Greenberg, H J, "A Primer of ANALYZE," Working Paper, University of Colorado at Denver, Denver, CO, June 1, 1990

——, "Enhancements of ANALYZE: A Computer-Assisted Analysis System for Linear Programming," ACM Trans Math Software, 19, 2 (1993), 223–256

——, "Syntax-directed Report Writing in Linear Programming Using ANALYZE," European J Oper Res, 72 (1994), 300–311

Hamming, R W., Numerical Methods for Scientists and Engineers, McGraw-Hill, New York, 1962

Hilgard, E R, Theories of Learning, (2nd Ed), Appleton-Century-Crofts, Inc, New York, 1956

Hillier, F S and G J Lieberman, Introduction to Operations Research (5th Ed), McGraw-Hill, New York, 1990, 20–23

Ho, Y C and X R Cao, Perturbation Analysis of Discrete Event Dynamic Systems, Kluwer, Boston, MA, 1991

Ivakhnenko, A G, Polynomial Theory of Complex Systems, IEEE Trans Systems, Man and Cybernetics, 4 (1971), 364–384

Jones, C. V., "User Interfaces and Operations Research," in E. G. Coffman, J. K. Lenstra and A. Y. Kan (Eds.), Handbook of Operations Research, Vol. 13, North-Holland/Elsevier, Amsterdam, 1992, 603–668

Kimbrough, S. O., S. A. Moore, C. W. Pritchett and C. A. Sherman, "On DSS Support for Candle-Lighting Analysis," Transactions of DSS-92, The Institute of Management Sciences, Providence, RI, 1992, 118–135.

— and J. R. Oliver, "On Automating Candle Lighting Analysis: Insight from Search with Genetic Algorithms and Approximate Models," Proc. Twenty-Seventh Annual Hawaii International Conf. System Sciences, 1994, 536–544.

——, —— and C. W. Pritchett, "On Post-Evaluation Analysis: Candle-Lighting and Surrogate Models," Interfaces, 23, 3 (1993), 17–28.

—, C. W. Pritchett, M. P.I Bieber and H. K. Bhargava, "The Coast Guard's KSS Project," Interfaces, 20, 6 (1990), 5–16

Kohler, W., The Mentality of Apes (English translation by E. Winter), Harcourt, Brace and Co., New York, 1925

——, The Task of Gestalt Psychology, Princeton University Press, Princeton, NJ, 1969

Koltai, T, J. Larraneta and L. Onieva, "Examination of the Sensitivity of an Operation Schedule with Perturbation Analysis," International J. Production Research, 31, 12 (1993), 2777–2787.

Kosy, D W. and B. P. Wise, "Self-explanatory Financial Planning Models," Proc National Conf. Artificial Intelligence, August 1984, 176–181

— and —, "Overview of Rome: A Reason-Oriented Modeling Environment," in L. F. Psu (Ed.), Artificial Intelligence in Economics and Management, Elsevier Science Publishers, North-Holland, 1986, 21–30.

Kurator, W. G. and R. P. O'Neill, "PERUSE: An Interactive System for Mathematical Programs," ACM Trans. Math. Software, 6, 4 (1980), 489–509.

Lee, D. L., "Perception, Intuition and Insight," in W. R. Niblett (Ed.), How and Why Do We Learn, Faber and Gaber, London, 1965.

Little, J. D. C., "Models and Managers: Concept of a Decision," Management Sci., 16, 8 (1970), B466–B489

Logan, F. A. and D. P. Ferraro, Systematic Analyses of Learning and Motivation, John Wiley & Sons, New York, 1978.

Lonergan, B J. F., Insight, A Study of Human Understanding, Harper & Row, San Francisco, CA, 1958.

Metcalfe, J, "Feeling of Knowing in Memory and Problem Solving," J. Experimental Psychology: Learning, Memory and Cognition, 12 (1986a), 288–294.

——, "Premonitions of Insight Predict Impending Error," J. Experimental Psychology: Learning, Memory and Cognition, 12 (1986b), 623–634.

— and D. Wiebe, "Intuition in Insight and Noninsight Problem Solving," Memory and Cognition, 15 (1987), 238–246

Microsoft, Microsoft Excel User's Guide 2 (Version 4.0), Microsoft Corporation, 1992

Palisade Corporation, Risk Analysis and Simulation Add-In for Lotus 1-2-3 Version 2.0 Users Guide, Palisade Corporation, New York, 1991.

Prager, M. H., "Group Method of Data Handling: A New Method for Stock Identification," Trans. American Fishery Society, 117 (1988), 290–296

Rasmussen, J., B. Brehmer and J. Leplat, Distributed Decision Making Cognitive Models for Cooperative Work, John Wiley & Sons, New York, 1991.

Reddy, Y. V., "The Role of Introspective Simulation in Managerial Decision Making," DSS-85 Transactions, IADSS, University of Texas at Austin, Austin, TX, 18–32

Saltelli, A and T. Homma, "Sensitivity Analysis for Model Output," Computational Statistics and Data Analysis, 13 (1992), 73–94.

— and J. Marivoet, "Non-parametric Statistics in Sensitivity Analysis for Model Output: A Comparison of Selected Techniques," Reliability Engineering and Systems Safety, 28 (1990), 229–253.

Savage, Sam L., The ABC's of Optimization Using What's Best!, LINDO Systems Inc., Chicago, IL, 1992.

Sharda, R and D. M Steiger, "Using Artificial Intelligence to Enhance Model Analysis," in S. G Nash and A Sofer (Ed.), The Impact of Emerging Technologies on Computer Science and Operations Research, Kluwer Academic Publishers, Boston, 1995, 263–279.

Steiger, D. M. and R. Sharda, "Inductive Model Analysis: A Taxonomy of Tasks and the Role of AI Technologies in Addressing These Tasks," Working Paper Series: ISOM 950501, University of North Carolina at Greensboro, Greensboro, NC 27412, 1995

Swanson, E. B and N C Ramiller, "Information Systems Research Thematics Submissions to a New Journal, 1987–1992, Information Systems Res., 4, 4 (1993), 299–330.

Wagner, H. M., "Global Sensitivity Analysis," Oper. Res., (1995), 948-969.

Wasserman, P. D., Neural Computing: Theory and Practice, Van Nostrand Reinhold, New York, 1989

Wise, B. P. and D. W. Kosy, "Model-Based Evaluation of Long-Range Resource Allocation Plans," in L. F. Pau (Ed.), Artificial Intelligence in Economics and Management, Elsevier Science Publishers, North-Holland, 1986, 93–102

Steven O. Kimbrough, Associate Editor. This paper was received on May 27, 1994 and has been with the authors 5 months for 1 revision.
