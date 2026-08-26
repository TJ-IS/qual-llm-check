---
otero_id: 1058
otero_key: "QSPPBZB6"
title: "Decision support in hierarchical planning systems: The case of procurement planning in oil refining industries"
authors: "Kasper Bislev Kallestrup; Lasse Hadberg Lynge; Renzo Akkerman; Thordis Anna Oddsdottir"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.09.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support in hierarchical planning systems: The case of procurement planning in oil re<sup>fi</sup>ning industries

Kasper Bislev Kallestrup <sup>a</sup>, Lasse Hadberg Lynge <sup>a</sup>, Renzo Akkerman <sup>b,</sup>⁎, Thordis Anna Oddsdottir <sup>a</sup>

<sup>a</sup> Department of Management Engineering, Technical University of Denmark, Produktionstorvet 424, 2800 Kgs. Lyngby, Copenhagen, Denmark

<sup>b</sup> TUM School of Management, Technische Universität München, Arcisstr. 21, 80333 Munich, Germany

## a r t i c l e i n f o

Article history: Received 3 October 2013 Received in revised form 11 August 2014 Accepted 13 September 2014 Available online xxxx

Keywords: Advanced planning systems Hierarchical planning Crude oil operations Procurement planning

## a b s t r a c t

In this paper, we discuss the development of decision support systems for hierarchically structured planning approaches, such as commercially available advanced planning systems. We develop a framework to show how such a decision support system can be designed with the existing organization in mind, and how a decision process and corresponding software can be developed from this basis. Building on well-known hierarchical planning concepts, we include the typical anticipation mechanisms used in such systems to be able to decompose planning problems, both from the perspective of the planning problem and from the perspective of the organizational aspects involved. To exemplify and develop our framework, we use a case study of crude oil procurement planning in the re<sup>fi</sup>ning industry. The results of the case study indicate an improved organizational embedding of the DSS, leading to signi<sup>fi</sup>cant savings in terms of planning efforts and procurement costs. In general, our framework aims to support the continuous improvement of advanced planning systems, increasing planning quality in complex supply chain settings.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Managing supply chains is a complex task and is often done with hierarchically structured advanced planning systems (APSs) [47]. Due to the complexity and uncertainty in supply chains, it is normally not possible or desirable to create fully automated decision systems that rapidly identify and execute optimal decisions. Even if it were, it is likely that managers would not trust such a system blindly, due to the very high potential costs of erroneous decisions. Instead, managers turn to decision support systems (DSSs), which support planning processes as good as possible.

A DSS involves a human–computer interaction and the software part usually provides a range of information that managers use to decide on an action. Literature on DSSs in relation to APSs focuses primarily on modeling or data structure aspects. As documented by Zoryk-Schalla et al. [51], focusing on modeling aspects early in the development of DSSs for APSs, without properly de<sup>fi</sup>ning the planning process and its characteristics, can lead to signi<sup>fi</sup>cant implementation problems. This calls for research on the development process of APSs, especially related to the planning process complexities, information requirements, as well as the organizational embedding [20].

The planning processes covered in APSs normally span different functional domains (e.g. production, distribution, sales) and include decision problems with different time horizons and granularity (from strategic to operational). This range of planning processes is often also re<sup>fl</sup>ected in organizational structures, which increases the need for coordination between the different processes. It is exactly this coordination in the hierarchical structure and the related information <sup>fl</sup>ows that are key factors in the development and implementation of APSs [48], and often the reason to implement an APS in the <sup>fi</sup>rst place [20]. Even though there is an increasing body of work on APSs and other hierarchical planning systems, how to develop additional decision support in a structured way remains a challenge, especially when taking into account the existing planning infrastructure and its organizational embedding.

In this paper, we address this problem by developing a framework to support DSS design, considering organizational aspects and process design early in the development process. More speci<sup>fi</sup>cally, we contribute to the decision support literature by answering (i) how a DSS for an APS can be designed with the existing organization in mind?, (ii) how a decision process can be developed from this basis? and (iii) how the information obtained from the <sup>fi</sup>rst two steps eases and directs the development of the enabling software? As we base our work on wellknown hierarchical planning concepts, we also contribute by providing insights on the anticipation mechanisms used in such systems to be able to decompose planning problems. Since we propose methods for creating DSSs in commonly used APS settings, we also ensure professional relevance [4]. Throughout the paper, we will use a case study of procurement planning in the re<sup>fi</sup>ning industry, an industry where advanced planning systems have traditionally seen extensive use [14,40]. However, the procurement planning problem has been an underdeveloped aspect within APSs [33], and previous research has often not managed to capture the decision problem properly [35], and it is therefore a good environment for the discussion of the DSS development process.

In the following section, we <sup>fi</sup>rst discuss the main literature streams related to our study. Based on this, Section 3 develops an initial development framework for model-based DSSs for APSs. In Section 4, we then outline the general structure of procurement planning in the re<sup>fi</sup>nery industry, followed by the application of our development framework to create a DSS in Section 5. In Section 6, we further re<sup>fi</sup>ne our framework based on the case results, followed by conclusions and further research directions in Section 7.

## 2. Related literature

## 2.1. Decision support systems

Creating DSSs is a way for organizations to improve the ef<sup>fi</sup>ciency and effectiveness of their decision processes. Power [38] argues that how to improve a decision process depends on how ill-structured the decision problem is. Ill-structured problems are de<sup>fi</sup>ned by what they are not, namely well-structured problems. A well-structured problem is a problem that is routinely carried through, where the solution can be checked and where the end goal can be met in a reasonable amount of time [46]. According to Power [38], problems that are well-structured can normally be automated in a decision system, while ill-structured problems need special decision studies. Problems that lie in-between these extremes (semi-ill-structured problems) can normally bene<sup>fi</sup>t from a DSS.

Conceptually, a DSS is a formalization of the knowledge and experience held by employees involved in the process, structured in a way that enhances the decision maker's ability to choose the best solution to a complex problem [25]. According to Holsapple and Whinston [16], a DSS is a human–computer interaction, where the computer consists of four elements, illustrated in Fig. 1.

A DSS may use a database analysis system to create metadata that can give new insights for managers or provide a mathematical model of the problem domain that greatly reduces a problem's solution domain. Early descriptions of management information systems used for decision support focused on the analysis of the decision system and condensation of data [1] as a means to ensure that software systems would provide only information that was relevant to the decision maker. Courbon et al. [8] described the design of such systems as evolutionary, a concept that was expanded and popularized by Keen [23]. Keen argued that a DSS can only exist if it is a product of an adaptive process between the system and the user, where the system encourages the user to take new approaches, which in turn lead the user to request more features from the system. Both Keen and Courbon et al. focused on the software engineering aspects of DSSs, assuming that a good decision process would evolve naturally. Other authors, including Blanning [6] and Linger and Burstein [31] used the analysis of the decision making process to identify what functions a DSS should have. Blanning also mapped modules of the DSS to the different departments in an organization.

Gachet and Haettenschwiler [12] reviewed nine different DSS development methodologies and advocated for those that combine system engineering aspects and decision making process aspects. These integrated approaches include Keen and Scott-Morton's [22] widely accepted “Design Cycle” and Saxena's [41] “Decision Support Engineering”, both of which place the decision analysis task or process development task as an antecedent of the software development task. Saxena's approach also includes a range of interactions that challenge the sequential structure, in order to allow for the evolutionary characteristics of DSSs.

![](/api/attachments/QSPPBZB6/fulltext/images/f066603cc82e996ac4a047ea9b1c0f6b5ca3390acbc631515f3ad3c7e27cd5b4.jpg)  
Fig. 1. Structure of DSSs according to Holsapple and Whinston [16].

## 2.2. Hierarchical planning structures

Hierarchical planning is important if one seeks to optimize systems where scheduling is critical and non-trivial tactical decisions, such as procurement and network planning, have a larger horizon than it is possible to optimize scheduling problems for. Planners usually solve this problem by splitting the system into at least two planning levels, an aggregate level and a detailed level. One of the earliest approaches to structure a planning system hierarchically was presented by Hax and Meal [15]. They proposed a hierarchical system that can “make decisions in sequence, with each set of decisions at an aggregate level providing constraints within which more detailed decisions must be made”. Bitran et al. [5] also argued that hierarchical planning models can replace dif<sup>fi</sup>cult-to-solve stochastic planning models when demand for individual products is stochastic but deterministic for aggregated product families. A robust aggregate plan is de<sup>fi</sup>ned by Lasserre and Mercé [29] as a plan for which a feasible disaggregation policy can be formulated. Gfrerer and Zäpfel [13] subsequently discussed how robust aggregate plans can be enforced through topdown coordination.

A conceptual framework for describing hierarchical structures, like those in hierarchical planning systems, was proposed by Schneeweiss [42]. In a hierarchical structure, there will be a top level (aggregate level) and a base level (detailed level). The top level can instruct the base level and the base level can react to these instructions. In topdown hierarchical structures like APSs, the base level cannot present a reaction before the decision is implemented in the object system (production system), but instead, the top level anticipates how the base level will react. The anticipation in the top level can then be updated/re<sup>fi</sup>ned based on ex-post feedback from the object system. In subsequent work, Schneeweiss [43] distinguishes three categories of anticipation: (i) considering characteristics of the base level directly (perfect anticipation), (ii) considering approximations of base-level characteristics (approximate anticipation), or (iii) considering part of the base-level characteristics (implicit anticipations). For non-perfect anticipation, which is normally the case in practice, the reaction from the object system can be quite different from the anticipations. Decision-makers can reduce the problem by increasing the quality of the anticipation, which is often a key aspect in the design and operation of hierarchical planning systems.

Hierarchical models can in some simple cases be autonomous, but in practice, a hierarchical planning system takes the form of an APS that combines autonomous decision modules with DSS modules [47]. The use of DSS modules is necessitated by the complexity of supply chains and, to some extent, the capacity of modern algorithms and computers. APS modules are either technically integrated or integrated through organizational processes. Most of the DSSs in APSs are model-based optimization tools (using Alter's [2] taxonomy), simply because planning and scheduling have traditionally been areas that heavily utilize operations research methodology.

Researchers report that APSs are widely used in the industry, but it has been argued that this is not re<sup>fl</sup>ected in DSS research [32]. As a consequence, DSS literature does not always describe the task of positioning a DSS, which determines the users, their objective and their organization. In a single-level planning process, this may be straightforward but for APSs, where multiple planning levels exist and many organizational units are involved, positioning a DSS is not straightforward.

Please cite this article as: K.B. Kallestrup, et al., Decision support in hierarchical planning systems: The case of procurement planning in oil re<sup>fi</sup>ning industries, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.09.003

K.B. Kallestrup et al. / Decision Support Systems xxx (2014) xxx–xxx

## 2.3. Crude oil procurement planning

In this paper, we consider the case study of crude oil procurement planning for re<sup>fi</sup>ning industries. Fig. 2 shows a typical APS for petroleum supply chains. Positioning a DSS for procurement planning within this structure is a non-trivial task. Related planning tasks include the crude supply scheduling level, the production and master planning level, and the strategic planning level. This positioning determines what information, generated in one of the other functional columns (production, distribution, sales) or in the market, is available to the DSS, and what information the DSS generates for the system.

The problem processing system in a DSS normally builds on formalized models of the problem domain. Decision support models for procurement planning have not received much attention in the quantitative operations management literature. Most work on procurement concerns the qualitative evaluation of different suppliers [7,10], sometimes followed by a quantitative model to support the selection process [19]. This is then typically the basis for contract negotiation and the actual ordering processes that are often based on classical inventory control. As an alternative to these supplier-focused approaches, we also see procurement of raw material on spot markets [17], often used in dual sourcing strategies as a supplement to a supplier base to be able to deal with demand uncertainty [18]. Approaches that try to capture the decision of procuring raw materials from different sources, including discrete short-term opportunities for sourcing, are however less common. Speci<sup>fi</sup>c work on the procurement of crude oils is also rather limited. As is the case for a lot of natural resources, quality variations in the raw material often lead to blending problems, complicating procurement decisions. Kingsman [24] already identi<sup>fi</sup>ed this problem, and it has often been included in production scheduling (especially in the re<sup>fi</sup>ning industry), but it has not seen much attention in decision support for procurement planning. Some previous work does however exist. Julka et al. [21] and Pitty et al. [37] investigate different forms of simulation-based decision support systems for managing supply chains in the petroleum industry. Julka et al. [21] propose an agent-based system that models third-party logistics providers, the procurement department and the internal logistics department as separate entities. Between these, offers and deals are made automatically based on a static sequence, de<sup>fi</sup>ning the procurement process. Pitty et al. [37] describe a similar dynamic simulation system. It models suppliers, the procurement process, crude operations, product operations, and customers. In a subsequent paper [26], they propose that the system can be connected to a search heuristic and, through many subsequent simulations, optimize against an objective.

None of them, however, consider the blending of crude oils, but rely on a strict pre-quali<sup>fi</sup>cation, which is too restrictive in a lot of practical settings. Other researchers approach procurement from a risk management perspective and use stochastic programming or linear programming models to identify the optimum product slates for a re<sup>fi</sup>nery [27,37]. They do, however, not consider a limited availability of speci<sup>fi</sup>c procurement opportunities, but rather assume the utopian situation that crude oil procurements are pro<sup>fi</sup>tably available so the mix of crude oils at the re<sup>fi</sup>nery can be kept constant during the planning horizon.

To address this lack of approaches that are able to deal with realistic situations, Oddsdottir et al. [35] recently developed a solution approach to solve a non-linear procurement planning problem that includes most relevant practical problem characteristics. The formulation is a mixedinteger non-linear programming (MINLP) model that is solved using a two-stage solution approach involving a linearized version of the original MINLP model, and a reduced MINLP model that represents the nonlinear problem with all procurement decisions <sup>fi</sup>xed. In our case study, the problem processing system of our DSS will be based on this work.

## 3. Developing model-based DSSs for APSs

DSS design methodologies (e.g. [16,25,38]) tend to assume that the computer in a DSS will automatically have a user. This assumption fails whenever a DSS is to be used in an APS, where many actors are involved and many decision processes are interconnected. In hierarchically structured systems, we need explicit focus on the organization. Some authors that develop decision systems for hierarchical systems, do consider the organization of work as they de<sup>fi</sup>ne planning levels [11,36,50], but they concentrate on the issue of de<sup>fi</sup>ning the correct mathematical models, and aggregation/disaggregation rules, so they only consider the organization within the software aspect of a DSS.

![](/api/attachments/QSPPBZB6/fulltext/images/0343754dee5c7b778a0d1745fff29fbf97f716c01accc3524eba7f25dfb0a3d1.jpg)  
Fig. 2. An ‘ideal’ downstream petroleum supply chain planning system Adapted from Roitsch and Meyr [40]

Please cite this article as: K.B. Kallestrup, et al., Decision support in hierarchical planning systems: The case of procurement planning in oil re<sup>fi</sup>ning industries, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.09.003

They fail to describe how the system will interface with the real organization and its work systems. This focus will, as was also pointed out by Alter [3], lead designers to create DSSs that have little or no impact on reality.

In our view, users for a DSS only come into existence once the designer de<sup>fi</sup>nes how the DSS is positioned within the hierarchical structure of the APS and the organization. To ensure that the user(s) will be able to use the DSS effectively, the designer must further design the interaction between human and computer, a new decision process that utilizes DSS software. When developing a DSS for an APS, there are consequently three aspects to consider: Organization, process, and software. The supersystem of these three will always be the organization, as the organization de<sup>fi</sup>nes the purpose. Subsequently, business processes structure elements and their relations to support this purpose. Finally, software is an element that can enable these processes.

These antecedence relationships imply a certain sequence that should be re<sup>fl</sup>ected in DSS development. The relationship between process and software is recognized by most integrated DSS development methodologies, as they develop the process before the software [22,41]. The relationship between organization and process has however not received much attention.

If developers start by modeling the software/planning model, they will likely start by prototyping a model for a simpli<sup>fi</sup>ed problem and then expand on this until the requirements of the project are met. The simple problem might be found at the most aggregated level, while the DSS naturally <sup>fi</sup>ts with the least aggregated level. The data structures used initially will then be dramatically different from what is necessary in the end.

Disregarding the organization aspect will consequently lead to higher project costs and longer delivery times, as also documented by [51]. Fig. 3 illustrates our initial framework for the continuous process of developing DSSs for APSs. When it becomes obvious that a decision process in an APS is <sup>fl</sup>awed and that it can be improved by a DSS (the root-cause is a semi-ill-structured problem), designers should start by investigating the inadequacy. This provides the requirements for a DSS development process. The development process should consider all three aspects of the future DSS in accordance with the logical sequence between them.

The primary contribution of our approach to DSS development is that we extend our DSS model to explicitly include the organization in an integrated framework that also considers the decision making support (process) and the system engineering (software) aspects.

![](/api/attachments/QSPPBZB6/fulltext/images/a71d6ee777d47fce39cbede8256b7bfd4a20aaf1bda59d9d6b87bbb678661669.jpg)  
Fig. 3. Initial conceptual framework on the development of DSSs for APS.

In the case study presented in Section 5, we apply this conceptual framework. From an analysis of the decision inadequacy, we start the development process by positioning the DSS within the existing organization. We then design the business process aspects of the DSS. This helps in identifying the users of the system and their interactions with the system. Once the target process is determined, we use the information gathered from the <sup>fi</sup>rst two steps to develop the elements of the software. We use the case study as an illustrative example of a company with a hierarchical planning structure, embedded in an organization with various functional areas involved in one or more planning tasks. In developing the detailed planning model, and the required anticipation mechanisms, we needed to consider some more industry-speci<sup>fi</sup>c aspects, such as the complex connections between the availability of raw materials and the feasibility of production plans. This aspect is however common for the process industry, as argued by Crama et al. [9], and might therefore not only be case-speci<sup>fi</sup>c. Furthermore, for the sake of generalizability of the results, the important aspect is that there is some kind of anticipation mechanism that links the planning problem at hand to another planning problem it in<sup>fl</sup>uences. Here, the anticipation of how the procured materials are actually used on the more detailed production planning level is a typical example of anticipation in a supply chain context.

Before we present the case study, we brie<sup>fl</sup>y introduce the oil re<sup>fi</sup>ning industry and the concepts of crude oil procurement planning. After the case study we revisit our framework in Section 6 and re<sup>fi</sup>ne its details, based on the experiences from the case study, to develop the <sup>fi</sup>nal version of our DSS development methodology, applicable to hierarchically structured APSs.

## 4. Crude oil procurement planning

At the most general level, oil re<sup>fi</sup>neries distil a <sup>fl</sup>ow of many hydrocarbons, crude oil, into many <sup>fl</sup>ows of single or few hydrocarbons, product cracks. This is done in the re<sup>fi</sup>nery's Crude Distillation Units (CDUs). Product cracks can then be further re<sup>fi</sup>ned to useable petrochemical products, which are used by airline companies, everyday motorists, road surfacing companies, and as input to other petrochemical industries. Crudes differ in hydrocarbon composition and in amount of nonhydrocarbon contents. They are often categorized according to sulfur contents (sweet and sour crudes), density (condensates, light, and heavy crudes), and acidity (indicated by the total acid number, TAN). Relevant data on crude contents and characteristics are collectively called crude assay data. The heterogeneous nature of crudes leads to uneven demand and relative differences in crude prices.

A critical determinant for re<sup>fi</sup>ning pro<sup>fi</sup>ts is the re<sup>fi</sup>nery's ability to procure crudes that can be re<sup>fi</sup>ned into end products at the highest margin, in the largest amounts. Selecting crude procurement opportunities in a way that optimizes re<sup>fi</sup>nery pro<sup>fi</sup>tability is the core element of crude oil procurement planning. The object system, which planners seek to control, is the front-end of a re<sup>fi</sup>nery, the crude operations system, illustrated in Fig. 4. The external constraints on the system are primarily the market and the end-product operations that lie after the CDU. Planners would ideally consider the re<sup>fi</sup>ning system as one entity, but complexity forces them to split the systems into crude operations and re<sup>fi</sup>ning operations. The end-product operations are traditionally optimized with approximate linear programming models, and the solutions to these models pull the crude oil operations planning process via CDU feed requirements on volumetric <sup>fl</sup>ow rates and the required quality of crude mix (sulfur, density, TAN, etc.).

Once production plans and CDU requirements are established, planners choose crude procurements that can be imported and blended to adhere to these CDU feed constraints. But the product of the planning process has to comprise of more than an import plan. Schedules for the speci<sup>fi</sup>c crude <sup>fl</sup>ow are equally important, due to the fact that crude imports are blended in storage tanks and CDUs are fed by multiple storage tanks simultaneously.

Please cite this article as: K.B. Kallestrup, et al., Decision support in hierarchical planning systems: The case of procurement planning in oil re<sup>fi</sup>ning industries, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.09.003

![](/api/attachments/QSPPBZB6/fulltext/images/ae7296f52908660bb8f9c821e6135f190686112552a364dfdd2559505b01dfbf.jpg)  
Fig. 4. The object system of the crude oil procurement planning system.

The crude procurement planning process is naturally only one component of the total supply planning system. Fig. 5 details the supply column in hierarchically structured APSs that is typical for re<sup>fi</sup>ning businesses. The <sup>fi</sup>gure is based on a variety of publications related to petroleum supply chains [28,34,40,45] as well as the authors' experience. It shows information on managerial responsibilities, levels of planning, available information and time horizons. Most importantly, it also depicts the interdependencies between the different planning levels. For example, when the long-term planning department plans maintenance for one of the CDUs, they do not only affect the object system, but also impose some capacity limitations on the mid-term planning process (a top-down instruction). The long-term planning could e.g. anticipate that capacity utilization will be low for the next months. If this anticipation turns out to be wrong, it will naturally affect the performance of the object system and a key concern in a hierarchical planning process is thus the quality of the top level's anticipation.

![](/api/attachments/QSPPBZB6/fulltext/images/c50c21135f5cb82fb1e5436d23afe8945df097151bd4865cca860bafddbba045.jpg)

Fig. 5. A generic hierarchically structured planning process for supply planning in the downstream petroleum industry.

<table><tr><td>Please cite this article as: K.B. Kallestrup, et al., Decision support in hierarchical planning systems: The case of procurement planning in oil refining industries, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.09.003</td></tr></table>

Procurement planning is a process that spans multiple planning levels and thus in many cases multiple departments. Fig. 6 shows the typical process of creating an import plan. The speci<sup>fi</sup>c sequence and departmental responsibilities will differ for different companies, but the general structure corresponds to the literature [21,37,40]. The procurement process consists of several parallel processes. The longterm planning department (usually split into logistics department, procurement department, crude assay department, etc.) continuously works to improve the raw material supply by pre-qualifying new crudes for their re<sup>fi</sup>neries and update crude assay data. They are also responsible for forecasting end-product prices and estimate what margin can be achieved from re<sup>fi</sup>ning the pre-quali<sup>fi</sup>ed crudes, usually referred to as crude re<sup>fi</sup>ned netbacks or re<sup>fi</sup>ning margins [21,37]. To do this they need the trading department to identify or estimate crude procurement availability and prices. They also need the planning department of the individual re<sup>fi</sup>neries to estimate what their crude stock slate will be at the start of the planning horizon and their production forecasts. Once this data is collected, and netbacks have been de<sup>fi</sup>ned, traders begin to look for speci<sup>fi</sup>c procurement opportunities in the market.

The mid-term planners then try to select crudes to form an import plan that will be feasible with respect to the CDU feed requirements calculated within the production column of the APS. This is a scheduling task that is mathematically extremely dif<sup>fi</sup>cult. If the ratio between inventory capacity and production capacity is low, the scheduling department will need to be included in the process to try to forecast what the crude stock slate will be at a speci<sup>fi</sup>c point-in-time, to estimate if a given procurement can feasibly be added to the stock slate, at that time, without causing an infeasible CDU feed.

Going back to the problem classi<sup>fi</sup>cations presented in Section 2, crude oil procurement planning can clearly be classi<sup>fi</sup>ed as a semi-illstructured problem, as some aspects, such as selecting the most promising crudes, are very dif<sup>fi</sup>cult, while other aspects, such as evaluating whether a solution is technically feasible, are relatively straightforward. It therefore follows that the procurement process could bene<sup>fi</sup>t from a DSS.

## 5. Case study: development of a DSS

For a period of one year, we have been working with Statoil to develop a DSS for their procurement process. Earlier attempts with a commercial APS provider were unsuccessful, as it was aiming for perfect anticipation, which turned out to be impossible. We will use this DSS development experience to illustrate the framework outlined in this paper, and exemplify the consequences of considering the organizational, process and software aspects of DSS to an equal degree. To develop each of the DSS aspects, we used interviews and observations to lay the basis for the process analysis and establishment of our understanding of the existing organization.

Statoil's procurement process is organized with a central re<sup>fi</sup>nery optimization department in Stavanger, Norway and separate planning

![](/api/attachments/QSPPBZB6/fulltext/images/d866f71fc8b8a555f0714f161761c8907bcd4de3c4880c9d897da1280a3cabcc.jpg)  
Fig. 6. Elements of the crude oil procurement process.

Please cite this article as: K.B. Kallestrup, et al., Decision support in hierarchical planning systems: The case of procurement planning in oil re<sup>fi</sup>ning industries, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.09.003

departments at each of their facilities. In this study, we include one of these facilities: the re<sup>fi</sup>nery in Kalundborg, Denmark. The procurement process at Statoil is similar to the generic case described in the previous section. The Stavanger-based employees in the Planning & Economics department calculate netbacks for each crude and facility. In collaboration with the Kalundborg-based employees of the Planning & Economics department, they then try to select between the procurement opportunities identi<sup>fi</sup>ed by the Trading department. The Trading department has of<sup>fi</sup>ces in Stavanger, London, Stamford (Connecticut), and Singapore. For the Kalundborg re<sup>fi</sup>nery, the crude oil supply is mainly handled by the Stavanger and London of<sup>fi</sup>ces. Table 1 shows how the responsibilities concerning different planning levels at Statoil compare to the generic case. The time horizons and information <sup>fl</sup>ows are similar to the generic case.

As in the generic case, the task “Select among procurement opportunities” is the most challenging. The task is performed using a (manual) heuristic procedure, where crudes on the netbacks list are considered in a prioritized manner, starting with the highest margin crudes. The Kalundborg planners and the crude oil Scheduling department at Kalundborg manually <sup>fi</sup>t possible crudes into the import plan and crude <sup>fl</sup>ow charts to meet the production plans for the planning horizon. The planning horizon is typically 2–3 months and <sup>fl</sup>ows are described per day. If a procurement opportunity vanishes from the market, planners will have to reschedule. They often discover that the crude arrival date will ideally have to be moved slightly in time. This is then reported to the traders, who subsequently investigate the options in the market. They perhaps <sup>fi</sup>nd a solution that almost <sup>fi</sup>ts the wishes of the planners and report this back to Kalundborg, where planners then reschedule to evaluate feasibility. This iterative process continues until feasibility seems reasonable, and the traders can close the procurement deal. This whole process has a long lead time (up to 14 days), and is time-consuming, due to a number of reasons:

• Manually creating crude <sup>fl</sup>ow schedules is extremely complex due to its combinatorial nature.

• Infeasible plans can be extremely costly once the consequences of decisions materialize and many scenarios with slight alterations are therefore considered to ensure the robustness of the decisions.

• Planners and schedulers at Kalundborg work in different hours than the traders and the crude oil market, which means that otherwise quick con<sup>fi</sup>rmations from planners are sometimes postponed until the next morning.

This slow and iterative process can result in the loss of pro<sup>fi</sup>table contracts or engagement in non-pro<sup>fi</sup>table contracts, when traders, in an effort to secure a good deal, sometimes have to buy before they have a <sup>fi</sup>nal con<sup>fi</sup>rmation.

Another problem with the process is the con<sup>fl</sup>icting objectives of the Trading department, and the Planning & Economics and Scheduling departments. Traders are concerned with maximizing the margin, while planners and schedulers are more concerned with maximizing the pro<sup>fi</sup>t. To avoid situations where operators are forced to reduce facility throughput, because of problematic feedstock, planners often reject crudes that they are unfamiliar with. These are typically the cheap crudes with problematic qualities. They are referred to as “exotic crudes”, and often represent signi<sup>fi</sup>cant re<sup>fi</sup>ning margins if they can be integrated in the procurement plan.

Table 1  
Comparison between generic planning systems and system at Statoil.

<table><tr><td rowspan="2">Planning level</td><td colspan="2">Responsibility</td></tr><tr><td>The generic planning system</td><td>Statoil</td></tr><tr><td>Long-term</td><td>Long-term planning department</td><td>Planning &amp; Economics (NO) Trading department (NO/UK) Crude Risk Assessment Team (DK)</td></tr><tr><td>Mid-term</td><td>Planning department</td><td>Planning &amp; Economics (DK) Trading department (NO/UK)</td></tr><tr><td>Short-term</td><td>Scheduling department</td><td>Scheduling department (DK)</td></tr></table>

Comparing the organization at Statoil with the generic planning organization, a main characteristic is that the mid-term and long-term planning levels are geographically distributed between Norway, Denmark and the UK, as well as spread out over <sup>fi</sup>ve departments: Planning & Economics (2 locations), Trading, Crude Risk Assessment Team, and Scheduling.

In summary, Table 2 lists the key issues and requirements for the new DSS. These were then represented by a series of metrics, for which the current performance was measured or estimated and quantitative targets were established. The key metrics are the re<sup>fi</sup>ning pro<sup>fi</sup>t, the resources spent on procurement planning, and the time required to create a plan.

## 5.1. The organization

All of the problems found at Statoil are directly (problems 1, 3, 4) or indirectly (problems 2, 5) related to the selection process “Select among procurement opportunities”. This is possibly due to the fact that this is a scheduling task, which is as mentioned extremely hard to solve to feasibility. Problem number 4 also speci<sup>fi</sup>ed the process “check feasibility of import plan” to be problematic. There are two ways of dealing with a troublesome task, you can either rede<sup>fi</sup>ne the process to eliminate the task, or you mitigate the problem related to the task.

## 5.1.1. Eliminate target tasks

To eliminate the task, we need to remove the object system's sensitivity to the choice of crudes. Excluding non-procurement related options such as inventory expansion and facility upgrading (both strategic level decision), the only way to do this is by being more intelligent in the pre-quali<sup>fi</sup>cation of crudes. A DSS could be positioned at the longterm planning, focusing on the evaluation of which crudes are feasible for all possible blend ratios with the other pre-quali<sup>fi</sup>ed crudes. This would potentially increase the ef<sup>fi</sup>ciency of the procurement process, as crude oil procurement will then just be added to the import plan according to their re<sup>fi</sup>ning margin and only inventory limits will have to be considered. As such a pre-quali<sup>fi</sup>cation process would limit the pro<sup>fi</sup>tability of the re<sup>fi</sup>nery by limiting the potential crude oil procurements, this was not considered a feasible direction for further development.

## 5.1.2. Mitigate problems related to target tasks

The dif<sup>fi</sup>culty in selection of crudes is that feasibility evaluation requires detailed scheduling of a long time-horizon (2–3 months) where a variety of uncertainties exist. There are basically two ways of dealing with this: (i) reduce the time horizon, or (ii) improve the ability to perform the detailed scheduling and deal with the stochasticity.

The <sup>fi</sup>rst option requires that traders can secure crude deliveries at a short notice. This will make the data deterministic and feasible to schedule with existing processes. This could be achieved by creating a DSS that spans the mid-term and the short-term planning, which can coordinate operation of multiple facilities. If the portfolio contains enough heterogeneous facilities, crudes can be bought long-term without considering feasibility. On the mid-term and the short-term horizon the DSS then distributes the procurements between the different re<sup>fi</sup>neries in a way that ensures feasibility and maximizes pro<sup>fi</sup>t. As this study focuses on the Kalundborg re<sup>fi</sup>nery, this network perspective would be out of the scope of this study, and this direction was not pursued, as the product portfolio at a single re<sup>fi</sup>nery is too small to ensure feasibility.

The second option involves the introduction of a DSS to support the selection task based on an improved anticipation of the detailed planning, which should reduce the time required to select crudes and improve the ability to choose the right crudes. Such a DSS would span the mid-term planning level. In our study, this option was selected as (i) it involves a relative generic decision problem with a hierarchical anticipation dimension, which increases the relevance of our study in the literature, and (ii) it can build on a signi<sup>fi</sup>cant body of industrial experience and academic literature available on detailed scheduling. In Fig. 7 we have placed the DSS in the hierarchical planning system according to this option and shown the performance criteria for each of the actors responsible for the respective planning levels, as well as decision aggregation level and organizational scope of the planning processes.

Table 2 Requirements for new DSS.

<table><tr><td>Key issues</td><td>DSS requirements</td></tr><tr><td>1 Deciding upon an import plan is a time-consuming process for the traders and the planners, because of the many iterations and lengthy feasibility studies necessary to select the right procurements.</td><td>Reduce resources spent on procurement planning</td></tr><tr><td>2 It is not possible to assess how good an import plan is in absolute terms. As only a few alternatives can be assessed, the chosen solution might be far from the, not-considered, best solution.</td><td>Enable assessment of opportunity cost</td></tr><tr><td>3 The complexity of the selection problem encourages the planners to stick with the well-known crude oils, even though they could be less profitable than “exotic” crudes with more complicating component contents.</td><td>Increase refining profits</td></tr><tr><td>4 The selection and validation processes depend on the experience and insight of a few key employees.</td><td>Reduce dependency on tacit knowledge</td></tr><tr><td>5 It is difficult to react to suddenly available procurements, as a new schedule cannot be created in time.</td><td>Reduce response time to market opportunities</td></tr></table>

Our choice of organizing the DSS at the mid-term planning level, focusing on handling the task “Select among procurement opportunities”, adds a series of requirements to the DSS. From Fig. 7 we can deduce the following:

1. The aggregation level of the decisions taken by the DSS must be in the magnitude of days.

2. The system will be instructed on crude netbacks and production targets and must instruct the short-term planners on the import plan and the corresponding target aggregated <sup>fl</sup>ow schedule. To do this it will need to make anticipations regarding the short-term planning level (e.g. actual CDU feed requirements, exact crude delivery dates).

3. Decisions taken will concern only the re<sup>fi</sup>nery in Kalundborg. This means that the support system will consider details of the re<sup>fi</sup>nery, including equipment capacities and operation times.

4. The users of the software will likely be the Planning & Economics or the Trading department.

5. Import plans (and <sup>fl</sup>ow schedules) must be optimized against the re<sup>fi</sup>ning pro<sup>fi</sup>ts of Kalundborg.

To decide if the system should be used by the Trading department or the Planning & Economics department, we will evaluate the degree of automation and characteristics of the left-over tasks of the crude selection subproblem, as suggested by van Wezel et al. [49]. The main distinction is whether the user will simply have to provide input data, or will be an active participant in the decision process.

## 5.2. The process

Fig. 8 shows all the information we have on the DSS at this stage of the development process. It receives instructions regarding crude netbacks and the volumetric production targets, and it instructs the short-term planning with import and crude <sup>fl</sup>ow plans. The system requires a range of static information (re<sup>fi</sup>nery setup, crude assays, etc.) and is subject to constraints based on a set of exogenous variables (information). The aggregation level of the DSS will be the highest temporal granularity of the exogenous variables. In our case study, details on the equipment availability are on a daily basis and procurement contracts are negotiated for three-day delivery windows. The temporal granularity of any data produced by the DSS will therefore be at least three days.

The system will have to anticipate the short-term planning level, when evaluating if the instructions will be feasible on that level. It will thus have to anticipate the mechanics of the detailed crude <sup>fl</sup>ow in the

![](/api/attachments/QSPPBZB6/fulltext/images/d22475d1c57f00780dca5aeada2daaa6876361efc4f53c51f2dd25687939a8f3.jpg)  
Fig. 7. For Statoil's case, the DSS will have to span the medium term planning level.

Please cite this article as: K.B. Kallestrup, et al., Decision support in hierarchical planning systems: The case of procurement planning in oil re<sup>fi</sup>ning industries, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.09.003

K.B. Kallestrup et al. / Decision Support Systems xxx (2014) xxx–xxx

![](/api/attachments/QSPPBZB6/fulltext/images/6fc7dfe688f4d129c79cd5dc21abfb7a2bf23923f9702de08a6cf70deaec47df.jpg)  
Fig. 8. Depiction of the information <sup>fl</sup>ows to and from the DSS.

crude operations system. It is important that the anticipation of the short-term planning level is as precise as practically possible, to ease disaggregation of the solution. Even if we were able to perfectly forecast the data, the combinatorial nature of the scheduling task (that is central in the base level) renders it practically impossible to solve a perfect anticipation. Instead we use implicit anticipations, and design the process so that these are continuously updated and improved. When using implicit anticipations, the left-over tasks of the selection subproblem are non-trivial; the user must be able to identify potential <sup>fl</sup>aws and make adjustments to guide the DSS in another direction.

Since the Trading department has no prior experience with planning and scheduling, it becomes natural that the Planning & Economics

![](/api/attachments/QSPPBZB6/fulltext/images/bf604627338802a2c24d79e176ba2e1fc0be9826a61dd2785ee85cc3263fb2df.jpg)  
Fig. 9. Proposed new procurement process. Calculations of netbacks and related tasks, which lie within long-term planning, are omitted

Please cite this article as: K.B. Kallestrup, et al., Decision support in hierarchical planning systems: The case of procurement planning in oil re<sup>fi</sup>ning industries, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.09.003

department should be the primary user of the system. Fig. 9 shows the proposed new procurement process, where the software component of the DSS is a central part in the selection task.

## 5.3. The software

The overall architecture of the DSS software can be derived from the target process in Fig. 9. First, we note that the software will need to store two types of information, dynamic case-speci<sup>fi</sup>c data, and more static knowledge-base data. The dynamic data includes all information regularly <sup>fl</sup>owing into the system, e.g. production targets and initial inventory. The static data includes the re<sup>fi</sup>nery setup information and the implicit anticipation model (although the model de<sup>fi</sup>nition is de<sup>fi</sup>ned by the problem processing system). Since no data is completely static, the software will also need a knowledge editor. Traders, planners and schedulers have a series of existing systems that the software will have to interface with and it thus needs an integration system and/or a report generator, depending of the nature of the interface. Fig. 10 shows the architecture that, besides the mentioned elements of the representation system, also needs a problem processing system to deal with the scheduling task.

## 5.3.1. Problem processing system

When we chose to position the DSS at the mid-term planning level, and not change pre-quali<sup>fi</sup>cation of other long-term planning processes, we retained the CDU feed's dependency on crude oil blending, and the DSS thus needs to consider scheduling explicitly. The algorithm used to solve the problem in our DSS is based on Oddsdottir et al. [35] and uses scheduling algorithms based on the crude scheduling literature [30,39] to solve the reduced MINLP model. A detailed discussion of this modeling approach is out of the scope of this paper, and interested readers are referred to the mentioned references.

## 5.3.2. The anticipation model

Because we chose to use an imperfect anticipation it will be necessary to note how data is aggregated and what measures are taken to make the aggregation robust. First of all, the primary output of the system is the import plan. The choice of a discrete-time scheduling model means that we will aggregate data to represent the 3-day periods that make up the total planning horizon, which is 3 months. In reality we only need to model the second and the third month (20 periods), due to the fact that procurement agreements for the <sup>fi</sup>rst month cannot be changed anymore. In Statoil's detailed scheduling process, all aspects of technical feasibility, roughly 290 parameters, are evaluated to ensure that the facility can run without interruption. Some parameters are critical, while other parameters almost always have acceptable values when some “key” parameters are within their limits. It is not computationally feasible to handle an MINLP model that covers 20 periods and all 290 parameters. In collaboration with Statoil, we therefore selected 11 key parameters that presented an acceptable balance between model complexity and anticipation quality:

• 2 volumetric <sup>fl</sup>ow parameters

• 3 crude blend components or characteristics, measured for 2 CDUs and for the total system: sulfur (wt.%), TAN (ppm), and density (g/cm<sup>3</sup>).

Component limits to the total system (sum of CDUs) and the volumetric <sup>fl</sup>ow limits are critical to ensure feasible operation of the downstream system, the end-product operations. The component limits speci<sup>fi</sup>c to each CDU are necessary because each CDU has its own feedstock range.

Following the terminology of Schneeweiss [43], this classi<sup>fi</sup>es as implicit anticipation since we choose parameters that indicate the dynamics of the base-level system. The speci<sup>fi</sup>c limits on each of the parameters are some of the controls available to improve the anticipation model: enlarging, shrinking or moving the accepted intervals. Once the optimization module has found an optimal solution, the DSS can easily calculate and present all the 290 parameters to the user. As solution algorithms and CPU power improve, model managers could also choose to add more key parameters, to further improve the anticipation quality.

The reduction of the problem complexity may lead to discrepancy between the anticipated base level and the actual base level, and can even prevent the aggregated solution from being feasibly disaggregated. The DSS uses two strategies to improve the likelihood of <sup>fi</sup>nding a solution that is robust to disaggregation.

First, the DSS software lets planners dedicate groups of storage tanks to each of the CDUs, meaning that the average key component level of each group will meet the limitations of the related CDU. This prevents solutions that are just narrowly acceptable, meaning solutions where component limits can only be met from the <sup>fi</sup>nal blend in the manifold between storage tanks and CDU — where small changes to equipment availability will render the plan infeasible. Instead, multiple tanks will now hold crude blends that can be accepted by the CDUs.

![](/api/attachments/QSPPBZB6/fulltext/images/8e26db4985f618820a823669d20dab811d75047864bcb2b377e78902140e87b0.jpg)  
Fig. 10. General architecture of the DSS software

Please cite this article as: K.B. Kallestrup, et al., Decision support in hierarchical planning systems: The case of procurement planning in oil re<sup>fi</sup>ning industries, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.09.003

K.B. Kallestrup et al. / Decision Support Systems xxx (2014) xxx–xxx

![](/api/attachments/QSPPBZB6/fulltext/images/797d9ab28a77b424f18f78e07b30013c2fa91e0cd635a6db8c510d6b1e09f0a7.jpg)  
Fig. 11. Realization of DSS software architecture with the indication of information streams and direction of interaction.

Second, we expanded the crude assay data for each crude and let it be dependent on which CDU a speci<sup>fi</sup>c crude <sup>fl</sup>owed to in each period. The reason for maintaining data separate for each CDU is to control the key component levels of the end products when blending heavy crudes with light crudes. A large fraction of heavy crudes is distilled into heavy end products. If the TAN level of these products is too high, one might want to reduce this by blending the heavy crude with a condensate that is low on TAN. The problem is that condensates distil

Please cite this article as: K.B. Kallestrup, et al., Decision support in hierarchical planning systems: The case of procurement planning in oil re<sup>fi</sup>ning industries, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.09.003

to very small amounts of heavy end products and blending is thus not linear to the volume <sup>fl</sup>ow of the crude. The additional implicit anticipations used to counter this is to add bonus values or punishment to the crude assay data dependent on which CDU the crude goes into. For example, in the current anticipation model, the TAN level for condensates with densities under 0.77 g/cm<sup>3</sup>, is set to 0.45 ppm when going into the non-condensate CDU and the original 0.01 ppm when going into the condensate CDU. In this way, we can prohibit or decrease the usage of condensates to arti<sup>fi</sup>cially lighten or dilute heavier crudes, and vice versa. This increases the likelihood that a solution can be feasibly disaggregated.

In conclusion, the likelihood of <sup>fi</sup>nding a feasible solution can be increased by (i) making the parameter limits for the aggregated model tighter to create room for “nudging” the plan when disaggregating, or (ii) using one of the two strategies described above.

## 5.3.3. Representation systems

From Fig. 9, we know that the different users of the system will be interested in different aspects of the software:

• The Trading department holds the task of <sup>fi</sup>nding speci<sup>fi</sup>c procurements in the market and will regularly need to update information, as up-to-date information is critical to the process.

• The Scheduling department needs to validate the solution and thus needs access to the generated <sup>fl</sup>ow schedule and detailed metadata to assist disaggregation and validation.

• Planning & Economics is interested in <sup>fi</sup>nding import plans, based on input regarding already agreed procurements, the base stock slate, and the procurement opportunities. They will also need access to the implicit anticipation model, so they can update key component limits, tank dedication limits, and crude assay bonus levels. Finally, they will need a solution report from the system with metadata that can guide them in assessing the feasibility of the solution.

We have split the user interface into compartments that support the structure of the procurement process. This ensures that the user interface can be customized to each user's own work stream. It thus allows the individual user to go through the system-user adaptive process that is essential for a DSS and is in line with the request for better user interface personalization put forth by Shim et al. [44].

To illustrate the resulting DSS architecture, Fig. 11 shows, through a collection of connected screenshots, the elements of the developed DSS. It indicates how different users have their separate interface, and it shows how they can use the system without having to worry about the layer with mathematical and algorithmic details.

The fact that such a layer exists, however, means that Statoil will need a model manager that can maintain it. This is a clear example of how the DSS affects the organization, as Keen [23] predicted. The specific interface between the model manager and the algorithmic layer depends on how Statoil chooses to organize themselves and is therefore outside of the scope of this paper. The General Algebraic Modeling System, GAMS, was used to implement the heuristic. In the case study, we acted as model managers and interfaced with the source code, written in GAMS syntax, directly.

The proposed DSS contains another layer, the commercial solver, which could be any available and viable solution. For our prototype, we have used IBM's MIP solver CPLEX. This is also a consequence of the chosen heuristic that breaks the problem into a sequence of MIPs.

The user interface laver was implemented in Microsoft Excel, as it is the environment that many other planning tools at Statoil utilize. Seamless integration with the detailed scheduling tools and netback calculators is ensured simply by reusing data structures. To optimize the problem processing system, data structures are in some cases altered before being sent to the commercial solver. The choice of Microsoft Excel also allowed us to use Excel's data visualization system, integration system, and user interface platform, rather than developing them ourselves.

## 5.4. Case study results

A comprehensive numerical study of the planning model is not within the scope of this paper. For more details on the algorithmic performance, we refer to Oddsdottir et al. [35]. Here, we will however brie<sup>fl</sup>y discuss some results related to the DSS requirements set out in Table 2.

The DSS has been tested with Statoil staff and the DSS software aspects have been tested against historic data. A total of 91 tests were performed, based on 6 base cases and 4 use case scenarios (adding holding cost, rolling horizon planning setup, rescheduling in response to dif<sup>fi</sup>culties, and reschedule to take advantage of suddenly appearing procurement opportunities). Based on these tests, we expect the following changes in the key metrics introduced earlier:

• An increase in the re<sup>fi</sup>ning pro<sup>fi</sup>t by at least 10%, due to an increased ability to assess pro<sup>fi</sup>table procurement opportunities.

• A reduction of about 60% in procurement process resource usage, as many time-consuming, computationally dif<sup>fi</sup>cult tasks have been implemented in the software.

• A reduction from 14 days to just 1 day for the import plan lead time, mainly due to a signi<sup>fi</sup>cant decrease in iterative communication between different departments in the organization. Combined, we estimate that the improved procurement process allows the organization to improve its local re<sup>fi</sup>ning pro<sup>fi</sup>t by 10%.

Next to these more quantitative results, the DSS has also reduced the dependence on tacit knowledge, which reduces the training of new staff signi<sup>fi</sup>cantly, as well as increased the possibilities to compare alternative plans, which was too time-consuming before.

## 6. DSS development methodology

Based on experiences from the case study, we are able to further specify our initial conceptual framework to propose a DSS development methodology, applicable when developing for hierarchically structured APSs.

A design task, at its most basic level, tries to ful<sup>fi</sup>ll a set of requirements by realizing a performance of something or someone. These requirements are typically identi<sup>fi</sup>ed through an analysis task and the performance is a characteristic of the creation. With DSSs, we design in sequential stages (disregarding naturally occurring iterations). First we design the organization aspect of the DSS, then the process, and lastly the software aspect. So DSS development can be seen as a process that continuously transforms required performance to realized performance, while continuously updating the requirements so they <sup>fi</sup>t the realized parts of the DSS.

Fig. 12 shows the resulting DSS development methodology. A set of requirements may be considered and relevant for the development of a speci<sup>fi</sup>c aspect, but not possible to realize within that aspect of the DSS. Instead, such requirements are updated with the knowledge generated in the task and passed back to the pool of requirements.

The full process is as follows. Before the development commences, the designer analyzes the current decision process. The output of this is the base requirements for the DSS, on which the development is initiated.

First, the designer extracts a part of the base requirements and realizes some of them by creating the decision organization (positioning the DSS within the APS and its organizational embedding). The requirements that are not realized are further speci<sup>fi</sup>ed to <sup>fi</sup>t the chosen decision organization and used in the next stage. This also holds for the knowledge regarding the decision characteristics and planning interactions, which cover:

• Decision characteristics: Decision objectives, organizational scope of decision, decision aggregation level, and required performance of decision process.

K.B. Kallestrup et al. / Decision Support Systems xxx (2014) xxx–xxx

![](/api/attachments/QSPPBZB6/fulltext/images/46def879148afac2a1a197a00c03a247818e7b115eaf971f3ecbf540492e91ef.jpg)  
Fig. 12. Illustration of proposed method for designing DSS systems for a hierarchically structured planning system

• Planning interactions: Involved organizational units (departments), instructions received from higher planning levels, instructions presented to lower planning levels, necessary anticipations, and information available to the process.

Second, the designer develops the process aspect of the DSS, based on the updated requirements as well as the base requirements for the future process. The product of the process development task is the new decision process structure and, as before, a set of further speci<sup>fi</sup>ed requirements, namely the necessary model characteristics and user interactions, which cover:

• Model characteristics: Model objectives, scope of model, model aggregation level, and required model performance.

• User interactions: Users, input to software, output from software, speci<sup>fi</sup>c applications of software.

Third, this information is used, together with requirements from the overall performance requirements, to develop the software aspect of the DSS and thereby “<sup>fi</sup>nalizing” the DSS development with the creation of a software system. Because software development has no descendants, it will need to realize all the requirements that are left. When the software development task is done, we conclude the DSS development. This approach would be repeated when another or new decision inadequacy is identi<sup>fi</sup>ed.

## 7. Conclusions

In this paper, we develop a design framework for decision support in hierarchical planning systems. Building on a case study on the development of a DSS for procurement planning within a typical hierarchically structured APS, we illustrated (i) how DSS practitioners can use analysis of organized decision systems to propose new decision processes that utilize model-based DSS software, and (ii) how process and organization design can direct the development of such software. Finally, we condensed our experiences into a three-stage DSS development process. The results of the case study indicate signi<sup>fi</sup>cant savings in terms of planning efforts and procurement costs, improving the procurement planning aspects in APSs for re<sup>fi</sup>ning industries. More generally, our framework should be able to support the continuous improvement of advanced planning systems, adding planning functionalities or improving existing functionalities, with a focus on the organizational embedding of the different planning tasks, thereby increasing overall planning quality in complex supply chains.

In this paper, the re<sup>fi</sup>ning industry is used as the speci<sup>fi</sup>c context, and the identi<sup>fi</sup>ed organization, process, and software, as well as the resulting savings are of course dependent on case speci<sup>fi</sup>cs. Nevertheless, it is important to realize that the hierarchical planning structure that is at the core of this research is commonly found in industry. It is re<sup>fl</sup>ected in most organizational structures of medium and large sized companies, as well as in commercially available APSs, by large vendors such as SAP or AspenTech [47]. It is furthermore used as a decomposition method in the development of planning tools in many industries, ranging from typical manufacturing situations in which aggregate planning strategies based on product families are followed by detailed planning for individual products, to more industry-speci<sup>fi</sup>c applications where some kind of decoupling between planning problems with different granularities can be identi<sup>fi</sup>ed. It should be noted that the development of anticipation mechanisms connecting the different planning levels is usually problemspeci<sup>fi</sup>c and requires good domain knowledge. The anticipation mechanisms developed in the case study cover aspects that are typical for process industries, and could for instance also be applicable in other industries where varying raw material quality is a key factor, such as the food industry, the chemical industry, or the paper industry. For this paper, the key is that the anticipation is representative for the type of connections that are needed between planning problems in hierarchical planning structures. In general, the case provides an example of a typical hierarchical planning situation, supporting the general applicability of the framework in the development of decision support in hierarchical planning systems.

Throughout the software development task, the anticipation model, especially the crude-tank group dedication and bonus crude assay data, has been continuously updated as we tested the system against the speci<sup>fi</sup>c procurement issues encountered at Statoil. This has brought the DSS software to a point, where disaggregation of the solution can be done feasibly and the prototype DSS software can be tested on reliability and robustness. If successful, the next step will be to create a “professional grade” system, with adequate linkage in to the IT infrastructure and maintenance features. A crucial ability in this effort is to be able to measure and ensure the performance of the DSS. How do we validate the robustness of the aggregation rules applied? How can we identify causes of decision effectiveness issues when discrepancies between reality and the DSS software are only accessible through the planner's mental model of both realities?

The abovementioned questions are interesting directions for further research as well. Also, even though we trust the proposed development methodology to be relatively generic, it would be useful to test it in other APS development projects. An important aspect of our work is the anticipation functions in hierarchical settings, even though the developed methodology might also be used outside of hierarchical planning settings. Related to our case study, another interesting direction for further research stems from our focus on a single production facility. Extending the DSS to include a production network with multiple facilities would create additional opportunities to improve re<sup>fi</sup>ning margins, but the organizational embedding of the DSS would also require additional attention.

## Acknowledgments

We gratefully acknowledge our collaboration partners at Statoil A/S for providing useful information and support regarding this work.

## References

[1] R.L. Ackoff, Management misinformation systems, Management Science 14 (1967) B-147-B-156.

[2] S. Alter, A taxonomy of decision support systems, Sloan Management Review 19 (1977) 39–56.

[3] S. Alter, A work system view of DSS in its fourth decade, Decision Support System 38 (2004) 319–327

[4] D. Arnott, G. Pervan, Eight key issues for the decision support systems discipline, Decision Support Systems 44 (2008) 657-672.

[5] G.R. Bitran, E.A. Haas, H. Matsuo, Production planning of style goods with high setup costs and forecast revisions, Operations Research 34 (1986) 226–236.

[6] R.W. Blanning, The functions of a decision support system, Information & Management 2 (1979) 87–93.

[7] J.S. Bonser, S.D. Wu, Procurement planning to maintain both short-term adaptiveness and long-term perspective, Management Science 47 (2001) 769-786.

[8] J.C. Courbon, J. Grajew, J. Tolovi, Design and Implementation of Interactive Decision Support Systems: An Evolutive Approach, Institute d'Administration des Enterprises, Grenoble, France, 1978.

[9] Y. Crama, R. Pascual, J.A. Torres, Optimal procurement decisions in the presence of total quantity discounts and alternative product recipes, European Journal of Operational Research 159 (2004) 364–378.

[10] L. De Boer, E. Labro, P. Morlacchi, A review of methods supporting supplier selection, European Journal of Purchasing & Supply Management 7 (2001) 75–89.

[11] G. Fontan, C. Merce, J.-C. Hennet, J. Lasserre, Hierarchical scheduling for decision support, Journal of Intelligent Manufacturing 16 (2005) 235–242.

[12] A. Gachet, P. Haettenschwiler, Development processes of intelligent decisionmaking support systems: review and perspective, in: J.N.D. Gupta, G.A. Forgionne, T.M. Mora (Eds.), Intelligent Decision-making Support Systems: Foundations, Applications and Challenges, Springer, 2006, pp. 97–121.

[13] H. Gfrerer, G. Zäpfel, Hierarchical model for production planning in the case of uncertain demand Furopean Journal of Operational Research 86 (1995) 142-161

[14] I.E. Grossmann, Advances in mathematical programming models for enterprisewide optimization, Computers & Chemical Engineering 47 (2012) 2–18.

[15] A.C. Hax, H.C. Meal, Hierarchical integration of production planning and scheduling, in: M. Geisler (Ed.), TIMS Studies in Management Science, North-Holland, Amsterdam, 1973, pp. 53–69.

[16] C.W. Holsapple, A.B. Whinston, Decision Support Systems: A Knowledge-based Approach, West Publishing Company, St. Paul, MN, USA, 1996.

[17] Z. Hong, C.K.M. Lee, A decision support system for procurement risk management in the presence of spot market, Decision Support Systems 55 (2013) 1–36.

[18] K. Inderfurth, P. Kelle, R. Kleber, Dual sourcing using capacity reservation and spot market: optimal procurement policy and heuristic parameter determination, European Journal of Operational Research 225 (2013) 298–309.

[19] V. Jayaraman, R. Srivastava, W.C. Benton, Supplier selection and order quantity allocation: a comprehensive model, Journal of Supply Chain Management 35 (1999) 50–58.

[20] P. Jonsson, L. Kjellsdotter, M. Rudberg, Applying advanced planning systems for supply chain planning: three case studies, International Journal of Physical Distribution & Logistics Management 37 (2007) 816–834

[21] N. Julka, I. Karimi, R. Srinivasan, Agent-based supply chain management—2: a re<sup>fi</sup>nery application, Computers & Chemical Engineering 26 (2002) 1771–1781.

[22] P.G. Keen, M.S. Scott-Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, Massachusetts, 1978.

[23] P.G.W. Keen, Adaptive design for decision support systems, SIGOA Newsletter 1 (1980) 15–25.

[24] B.G. Kingsman, Purchasing raw materials with uncertain <sup>fl</sup>uctuating prices, European Journal of Operational Research 25 (1986) 358–372.

[25] M.R. Klein, L.B. Methlie, Knowledge Based Decision Support Systems: With Applications in Business, 2nd ed. John Wiley & Sons Inc., West Sussex, England, 1995.

[26] L.Y. Koo, A. Adhitya, R. Srinivasan, I.A. Karimi, Decision support for integrated re<sup>fi</sup>nery supply chains — part 2, Design and operation, Computers & Chemical Engineering 32 (2008) 2787–2800.

[27] H. Lakkhanawat, M.J. Bagajewicz, Financial risk management with product pricing in the planning of re<sup>fi</sup>nery operations, Industrial & Engineering Chemistry Research 47 (2008) 6622–6639.

[28] W. Lasschuit, N. Thijssen, Supporting supply chain planning and scheduling decisions in the oil and chemical industry, Computers & Chemical Engineering 28 (2004) 863–870.

[29] J.B. Lasserre, C. Mercé, Robust hierarchical production planning under uncertainty, Annals of Operations Research 26 (1990) 73–87.

[30] J. Li, W. Li, I.A. Karimi, R. Srinivasan, Improving the robustness and ef<sup>fi</sup>ciency of crude scheduling algorithms, AIChE Journal 53 (2007) 2659–2680.

[31] H. Linger, F. Burstein, Intelligent decision support in the context of the modern organisation, Proceedings of the 4th Conference of the International Society for Decision Support Systems — ISDSS'97, July 21–22, Lausanne, Switzerland, 1997.

[32] K.N. McKay, V.C.S. Wiers, Integrated decision support for planning, scheduling, and dispatching tasks in a focused factory, Computers in Industry 50 (2003) 5–14.

[33] H. Meyr, H. Rosic, C. Seipl, M. Wagner, U. Wetterauer, Architecture of selected APS, in: H. Stadtler, C. Kilger (Eds.), Supply Chain Management and Advanced Planning, 4 ed.Springer, Berlin, 2008.

[34] S.M.S. Neiro, J.M. Pinto, A general modeling framework for the operational planning of petroleum supply chains, Computers & Chemical Engineering 28 (2004) 871–896.

[35] T.A. Oddsdottir, M. Grunow, R. Akkerman, Procurement planning in oil re<sup>fi</sup>ning industries considering blending operations, Computers & Chemical Engineering 58 (2013) 1–13.

[36] L. Özdamar, M.A. Bozyel, S.I. Birbil, A hierarchical decision support system for production planning (with case study), European Journal of Operational Research 104 (1998) 403–422.

[37] S.S. Pitty, W. Li, A. Adhitya, R. Srinivasan, I.A. Karimi, Decision support for integrated re<sup>fi</sup>nery supply chains — part 1. Dynamic simulation, Computers & Chemical Engineering 32 (2008) 2767–2786.

[38] D.J. Power, Decision Support Systems: Concepts and Resources for Managers, Ouorum Book Westport CT USA 2002

[39] P.C.P. Reddy, I.A. Karimi, R. Srinivasan, Novel solution approach for optimizing crude oil operations, AIChE Journal 50 (2004) 1177–1197.

[40] M. Roitsch, H. Meyr, Oil industry, in: H. Stadtler, C. Kilger (Eds.), Supply Chain Management and Advanced Planning, 4 ed.Springer, Berlin, 2008, pp. 1–16.

[41] K. Saxena, Decision support engineering: a DSS development methodology, Proceedings of the Twenty-fourth Annual Hawaii International Conference on System Sciences, IEEE, 1991, pp. 98–107.

[42] C. Schneeweiss, Hierarchical structures in organisations: a conceptual framework, European Journal of Operational Research 86 (1995) 4–31.

[43] C. Schneeweiss, Distributed decision making — a uni<sup>fi</sup>ed approach, European Journal of Operational Research 150 (2003) 237–252.

[44] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2002) 111–126.

[45] D.E. Shobrys, D.C. White, Planning, scheduling and control systems: why can they not work together, Computers & Chemical Engineering 24 (2000) 163–173.

[46] H.A. Simon, The structure of ill structured problems, Arti<sup>fi</sup>cial Intelligence 4 (1974) 181–201.

[47] H. Stadtler, C. Kilger (Eds.), Supply Chain Management and Advanced Planning, 4 ed. Springer, Berlin Germany. 2008

[48] H. Stadtler, B. Fleischmann, M. Grunow, H. Meyr, C. Sürie, Advanced Planning in Supply Chains, Springer, Berlin, Germany, 2012.

[49] W. van Wezel, J. Cegarra, J.-M. Hoc, Allocating functions to human and algorithm in scheduling, in: IC. Fransoo T. Wäfler LR. Wilson (Eds.) Behavioral Operations in Planning and Scheduling, Springer, Berlin Heidelberg, 2011 pp. 339–370

[50] E. Vicens, M.E. Alemany, C. Andres, J.J. Guarch, A design and application methodology for hierarchical production planning decision support systems in an enterprise integration context, International Journal of Production Economics 74 (2001) 5–20.

[51] A.J. Zoryk-Schalla, J.C. Fransoo, T.G. de de Kok, Modeling the planning process in advanced planning systems, Information & Management 42 (2004) 75–87.

Kasper Bislev Kallestrup received an M.Sc. in Engineering Management from the Technical University of Denmark, where he subsequently also worked in research positions in the Department of Management Engineering and the Department of Chemical Engineering.

Lasse Hadberg Lynge received an M.Sc. in Engineering Management and a B.Sc. in Mechanical Engineering from the Technical University of Denmark. After holding positions at IBM and Victoria Properties, he is currently working as a Consultant at Bain & Company.

Renzo Akkerman is Professor of Operations Management and Technology at the School of Management of the Technische Universität München in Munich, Germany. He previously held positions at the Technical University of Denmark and the University of Groningen. He has a Ph.D. in Operations Management, as well as an M.Sc. in Econometrics and Operations Research, both from the University of Groningen. His research and teaching mainly focuses on operations management in the process industries, ranging from supply chain management issues to detailed production planning and control

Thordis Anna Oddsdottir is a Ph.D. student in the Department of Management Engineering at the Technical University of Denmark. She holds an M.Sc. in Industrial Engineering from the Georgia Institute of Technology, as well as a B.Sc. in Mechanical Engineering from the University of Iceland. Her research interest lies within the <sup>fi</sup>eld of operations management, with special focus on supply chain management and optimization.
