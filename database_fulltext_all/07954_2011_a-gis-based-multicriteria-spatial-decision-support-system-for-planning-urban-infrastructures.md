---
otero_id: 7954
otero_key: "HAJSRNXV"
title: "A GIS-based multicriteria spatial decision support system for planning urban infrastructures"
authors: "João Coutinho-Rodrigues; Ana Simão; Carlos Henggeler Antunes"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.02.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A GIS-based multicriteria spatial decision support system for planning urban infrastructures

João Coutinho-Rodrigues <sup>a,b,</sup>⁎, Ana Simão <sup>a</sup>, Carlos Henggeler Antunes <sup>a,c</sup>

<sup>a</sup> INESC-Coimbra, R. Antero Quental, 199, 3000–033 Coimbra, Portugal

<sup>b</sup> Department of Civil Engineering, Faculty of Sciences and Technology, Polo II, University of Coimbra, 3030–788 Coimbra, Portugal

<sup>c</sup> Department of Electrical Engineering and Computers, Faculty of Sciences and Technology, Polo II, University of Coimbra, 3030–290 Coimbra, Portugal

## a r t i c l e i n f o

Article history: Received 18 December 2009 Received in revised form 23 December 2010 Accepted 3 February 2011 Available online 9 April 2011

Keywords: Spatial Decision Support Systems Geographical Information Systems Multicriteria Analysis Urban Infrastructures

## a b s t r a c t

The planning of urban infrastructures has important spatial implications. The evaluation of alternative courses of action in this setting requires the explicit consideration of multiple criteria as they have important social, economic, and environmental effects. This paper presents a decision support system aimed at offering the users (e.g., government or municipal agencies) a <sup>fl</sup>exible and user-friendly environment to provide decision aid in urban infrastructure planning. The visualization of available alternatives on maps provides a valueadded for decision support processes in urban infrastructure evaluation problems. The development of this system has been motivated by a real world urban case study.

© 2011 Elsevier B.V. All rights reserved

## 1. Introduction

Urban areas are constantly changing as they expand into new territory or existing areas are re-developed. Infrastructure investments are key components for successfully implementing these changes. However, the planning and analysis of such investments is complex. Typically, they are strategic and long-term in nature as they involve large capital expenditures designed for many years of service. The evaluation of these investments requires the explicit consideration of multiple, con<sup>fl</sup>icting and incommensurate criteria as they have important social, economic, and environmental effects that impact various stakeholders differently. These decisions also have important spatial implications as many of their costs and bene<sup>fi</sup>ts are distributed spatially. Consequently, they have differing impacts on several stakeholders depending upon the type and location of the investments, and upon the citizen groups affected.

The appraisal of alternative urban plans involves the analytical and systemic determination of all the factors in<sup>fl</sup>uencing the multidimensional value of courses of action, supported in clear principles and using well-de<sup>fi</sup>ned criteria. The process of evaluation should be scienti<sup>fi</sup>cally sound, and its adequate application depends not just on the quality and amount of the information gathered but also on the features offered to the user. In order to analyze decision problems, the need to integrate spatial data with algorithmic techniques has been recognized and gave rise to a research stream in the context of decision support systems (DSS) related to the so-called Spatial Decision Support Systems (SDSS). As mentioned by Maniezzo et al. [12], these systems are concerned with how to integrate spatially referenced information in a decision making environment in order to positively affect the performance of decision makers, showing how spatially integrated DSS can be used to bridge the gap between policy makers and complex computerized models.

In the context of urban and regional planning, where the “the complexity of the decision problem is obvious” [22], DSS are used to assist governments and communities, aiding urban planners in organizing, analyzing, modifying, and re-evaluating existing or needed spatial information within land-use planning activities [21].

The integrated information/decision support system presented in this paper is aimed at offering the users (e.g., government or municipal agencies, promoters, etc.) a <sup>fl</sup>exible and user-friendly environment based on formal multiple criteria methodologies to assist them in keeping and structuring information, obtaining historical and statistical analysis, and providing decision aid by enabling a detailed comparative analysis of the alternatives in urban plans evaluation, both for experts and other people with no technical knowledge.

The visualization of available alternatives on a map, assisting the user to locate the spatial elements in their actual environment, and the possibility of automatic representation of alternatives in the criterion space, provides a value-added for the decision analysis and support processes in urban infrastructure problems where usually several options must be compared.

We present a SDSS prototype developed to plan and analyze a large-scale urban infrastructure investment decision in Coimbra, Portugal. The underlying decision is to select “the best” water supply system investment option to satisfy the new demand created by a proposed urban development/expansion project. As proposed, the project will cover 77 hectares and includes 2,200 housing units, as well as a church, pre-primary school, senior citizen home, health club, hotel, equestrian center, and shops, among other facilities. Although the SDSS prototype was developed to analyze a speci<sup>fi</sup>c investment, it was designed to be applicable to other infrastructure decisions and urban areas.

Given the spatial, multicriteria nature of urban infrastructure planning and investment decisions, the system developed for Coimbra is a Multicriteria Spatial Decision Support System (MC-SDSS) [1,9,10,19]. The system prototype is called MCPUIS (Multicriteria Planning of Urban Infrastructure Systems). MCPUIS integrates methodologies from three areas of research: geographical information systems (GIS), data base management systems (DBMS), and multicriteria decision analysis (MCDA) in a user-friendly, menu-driven SDSS.

MCPUIS was designed to assist decision makers (DMs) in the evaluation and comparison of various infrastructure investment options. Consequently, it assumes that a discrete set of investment alternatives has been identi<sup>fi</sup>ed and characterized, and that the problem is to provide decision support in the selection of the “best” of these alternatives according to multiple evaluation criteria. In the implementation of MCPUIS special attention has been paid to aspects such as the identi<sup>fi</sup>cation and structuring of the various criteria, the selection of multicriteria methods, the support of qualitative and quantitative information to assess the criterion scores, and the development of a userfriendly interface. The integration of all these aspects, which may involve the use of large amounts of inter-related alphanumeric and spatial data, was accomplished by using a relational data base management system incorporating a high-level programming language for model and interface development [14].

## 2. Architecture and capabilities of MCPUIS

## 2.1. General overview

The MCPUIS architecture is comprised of the four modules displayed in Fig. 1, integrating a set of multiple criteria decision aid (MCDA) methods, a GIS, a relational DBMS (RDBMS), and an adequate human-computer interface aimed at minimizing the cognitive effort required from users.

The MCDA module includes distinct methods such as:

\- SAW, the Simple Additive Weighting [3,11,23];

\- TOPSIS, Technique for Order Preference by Similarity to Ideal Solution [13,23];

\- ELECTRE I [17,18], which belongs to the ELECTRE (Elimination and Choice Translating Reality) family of methods based on outranking relations [5].

The GIS module supports storage and visualization of maps and spatial data, and provides functions for spatial analysis. This module is supported on ESRI ArcView® [16], which was selected due to several reasons. It can perform the geographical data storage and visualization requirements of MCPUIS and can be programmed to perform the spatial analysis. Also, it includes built-in spatial analysis functions used by MCPUIS. For example, it can be used in the computation of the construction costs (or economic bene<sup>fi</sup>ts) associated with a particular infrastructure investment. In addition, it is a popular and readily available commercial GIS. MCPUIS is “cohesive” [8] in the sense that the decision support methods and visualization methods are encoded into the GIS.

The database module is implemented with a RDBMS. This module is used to store and manipulate alphanumeric data. Data in the RDBMS is typically non-spatial in nature (e.g., the cost and <sup>fl</sup>ow capacity of a particular type of pipe or valve). The RDBMS used for the development of this work is 4th Dimension (4D) - www.4d.com. It includes a high-level programming language, consisting of several commands and components (data types, variables, operators, expressions, commands and methods) that help to perform tasks and manage the data, allowing a full integration of data manipulation with models through graphical interfaces.

![](/api/attachments/HAJSRNXV/fulltext/images/ce1629e057bc9e8e238dbe7f6d681d8173347d8068e16c02463f716f0d5e4011.jpg)  
Fig. 1. MCPUIS Architecture.

MCPUIS is provided with an interface designed to be user-friendly and intuitive for the user, allowing the easy introduction of all the parameters required by the methods and the experimentation with the decision support methods implemented (e.g., to facilitate sensitivity analysis with different sets of parameters and with the results provided by distinct methods).

Those modules support the 4 basic functions:

1. SRDD, storage, retrieval, and display of data;

2. IOE, investment option evaluation;

3. IOCS, investment option comparison and selection;

4. CISA, communication/interaction with the system and sensitivity analysis.

Some of the capabilities associated with these functions are described below.

## 2.2. The SRDD function

The SRDD function encompasses the storage, retrieval, and display of data, and it integrates the GIS and the RDBMS module". Spatial data is stored in the GIS module (e.g., city maps, geological maps, roads network, physical location of pipelines and water supply system clients). Non-spatial alphanumeric data (e.g., the capacity or cost of a particular pump, discount rate) and various relationships among the data (e.g., clients served by each water tank, the type of client served by any speci<sup>fi</sup>c pipe, electricity consumption per day by pump) are stored in the RDBMS. The database management capabilities (e.g., data import, editing, classi<sup>fi</sup>cation, search, manipulation, and export)

and the visualization capabilities (e.g., maps of the existing system or of a speci<sup>fi</sup>c alternative) are accomplished via pull-down menus, dialogue boxes, spreadsheets, tables, and graphics. The display of spatially referenced data via maps and other <sup>fi</sup>gures is a basic feature of a GIS such as ESRI ArcView®.

## 2.3. The IOE function

The IOE function carries out the global assessment of investment options, which must take into account their performances on the various evaluation criteria at stake. This requires the determination of various economic, social, and environmental costs and bene<sup>fi</sup>ts associated with each alternative. These scores for the criteria are often dif<sup>fi</sup>cult to determine as they involve data that vary spatially. Examples include the age/diameter/depth of existing and/or proposed pipelines, increased road congestion caused by the construction works, and/or the impacts on existing infrastructures such as gas pipelines, electricity lines and telecommunications cables. The IOE function of MCPUIS facilitates these evaluations by ensuring that they are based upon the same technical formulae and data. This saves time and effort and ensures that the comparisons are based upon evaluations using similar databases and techniques. The IOE function provides important data/information needed for these evaluations. For example, this data can be used to calculate <sup>fi</sup>xed infrastructure investment costs (e.g., pipeline installation based upon the depth of the installation and the capacity of the pipe among other factors) or social costs (e.g., population with improved and/or degraded service) associated with a particular investment option.

## 2.4. The IOCS function

Complex decision problems are frequently encountered in urban and land-use planning, typically involving the consideration of a wide range of incommensurable and con<sup>fl</sup>icting criteria. The IOCS function performs the comparison of the various alternatives according to the multiple criteria at stake in urban investment decisions. As is generally recognized, no multiple criteria decision analysis (MCDA) technique is the “best” for all problems and the various methods often produce different results for the same problem (e.g., [5,7]). Typically the differences are greater when there are more alternatives and when the alternatives have similar values for the criteria [15]. Therefore, the application of distinct MCDA methods, with different underlying assumptions, is likely to generate more con<sup>fi</sup>dence in the results obtained with distinct approaches. Since it has been recognized that DSS incorporating complex models and methods have been “underutilized” [2] and DMs reveal reluctant to use potentially bene<sup>fi</sup>cial tools due to their perceived complexity, MCPUIS incorporates simple methods based on distinct underlying principles which are easy to be explained having in mind not just the system acceptance but also reliance on the results. However, as this is an independent module (external to the GIS, RDBMS and human-computer interface), it may accommodate additional methods to be implemented in a future phase of development. The MCDA methods component offers a set of techniques that provide guidance and coherence to the decision making process. These techniques (SAW/TOPSIS and ELECTRE methods) can be broadly categorized as compensatory and noncompensatory, being also different regarding the preference information required from the DM and the type of output provided. A full description of the MCDA methods and implementation details utilized by MCPUIS are beyond the scope of this paper. The interested reader is referred to Yoon and Hwang [23] or Triantaphyllou [20] for an introduction/overview of these techniques.

The three MCDA methods presently included require the DM to assign weights to the various criteria, to be carried out using a meaningful methodology for weights elicitation, and that the performances of each alternative according to each criterion are in numerical and comparable values (i.e. normalized). SAW and TOPSIS belong to the group of complete aggregation methods that compute an aggregate performance for each alternative. TOPSIS ranks the alternatives based upon DM determined weights on the criteria, and each alternative's performance vis a vis two reference points: “ideal solution” and “anti-ideal solution” (e.g., see [4,6,14]) – this particular feature distinguishes this method from the other two methods. Both SAW and TOPSIS allow for compensation between criteria and are based on simple and intuitive principles, yet disputable ones mainly regarding the role of weights. However, in many situations (and especially when it concerns urban planning), a very good performance in one criterion may not compensate a low score in another criterion. The methods of the ELECTRE family rely upon the construction and the exploitation of an outranking relation in face of the problem to be tackled (selection, ranking or sorting). The main feature of ELECTRE methods, which is relevant in the context of our study, is their possible non-compensatory nature. That is, a very bad performance on a given evaluation aspect (criterion) may not be compensated by good scores on other criteria. Furthermore, some ELECTRE methods accommodate in a natural way the imprecision and uncertainty inherent to human decision processes by relying on the use of thresholds. Weights in the framework of ELECTRE methods do not depend on the nature of the criterion scales. Therefore, these weights possess the true meaning of relative importance given to the distinct criteria. In this way, weights in the framework of ELECTRE are different from weights used in SAW and TOPSIS, which in these cases can be interpreted as rates of transformation into a common utility/ value unit. The technical parameters required by the methods, such as criteria weights or the thresholds of concordance and discordance of ELECTRE I, are freely de<sup>fi</sup>ned by the user via user friendly menus, slide bars, etc. implemented in MCPUIS, thus giving him/her full control of the decision process.

The SDSS enables the results to be visualised in the space of criteria using windows (Figs. 3 and 4), which can overlap on map windows (Fig. 2) where the alternatives under evaluation are displayed. This feature is useful, in several contexts, for grasping the spatial implications associated with each alternative solution. The outranking graph generated by ELECTRE I method [17,18] can also be displayed.

The multicriteria capabilities of MCPUIS include the elicitation of the required DM inputs (e.g., the de<sup>fi</sup>nition of decision criteria, the assignment of weights) and the generation and presentation of the outputs according to the characteristics of the different MCDA techniques. MCPUIS can also perform sensitivity analysis on various parameters used by the MCDA methods and DM's inputs.

## 2.5. The CISA function

The communication/interaction aspects are very relevant in the context of a SDSS also to enable sensitivity analysis studies. For this purpose the MCDA methods (SAW, TOPSIS, ELECTRE I), the RDBMS structure and the graphical interface to receive parameters and comparison of the alternatives in the criterion space have been developed from scratch and incorporated into the ESRI ArcView® GIS platform. This was done to facilitate the user/system interaction and allows MCPUIS to be utilized in other infrastructure system planning applications in other settings.

The overall purpose of MCPUIS is to assist the DM in the assessment and selection of the investment option to be implemented. The DM supplied inputs (e.g., weights and threshold values, etc.) used by the MCDM techniques in<sup>fl</sup>uence the results obtained using the different MCDA methods. Since these inputs parameters are “subjective” (i.e., they depend on the DM who may be not absolutely con-<sup>fi</sup>dent about the preferences he/she expresses in this setting) MCPUIS includes also a “sensitivity analysis” function to assess the stability (robustness) of the conclusions in face of distinct sets of input parameters. This is an empirical (ad-hoc) analysis to provide insights on how robust the “preferred alternative” is regarding the inputs provided by the DM. An example is presented in the next section.

![](/api/attachments/HAJSRNXV/fulltext/images/c97e29964959fd9d84f7c64fcf09da72db4a1ee5947f2895cd1b0d3a77789a05.jpg)  
Alternative 1

![](/api/attachments/HAJSRNXV/fulltext/images/b4861d00c9376c05073e4a45e905cfa51d0a6e32ab3268d72561f16617507a75.jpg)

![](/api/attachments/HAJSRNXV/fulltext/images/de335ac2e73e9de9aa973d7501810f38aa8a1a1dc5fbe746b3e869437136c767.jpg)  
Alternative 2

Alternative 3  
![](/api/attachments/HAJSRNXV/fulltext/images/4439132ad457825100e4b48ae58e4a0576f81b2ebf9488ed6f0b66bd7589e557.jpg)  
Alternative 4  
Fig. 2. Four Infrastructure Investment Options.

The MCPUIS system interface has been designed to minimize not just the computer programming tasks, but also the skills on multicriteria analysis, RDBMS, and GIS required. Also the cognitive effort is made easy through the extensive use of database management (e.g., data import, editing, classi<sup>fi</sup>cation, search, manipulation, and export) and visualization capabilities (e.g., maps of the system or of a speci<sup>fi</sup>c alternative, graphics comparing various alternatives).

## 3. MCPUIS application to a real world case study

MCPUIS was developed to analyze a proposed expansion of the water supply system of Coimbra, the larger city in the central region of Portugal. The expansion is necessary to meet the increased demand (estimated at approximately 2,650 cubic meters or about 700,000 gallons per day) resulting from a new urban development on 77 hectares (about 190 acres) on the southern edge of the city, near the technological campus of the University of Coimbra. This represents an increase of about 5% in total water supplied by Coimbra's water and sanitation department. Four investment options, shown in Fig. 2, were identi<sup>fi</sup>ed to serve this additional demand.

The content of Fig. 2 was generated by the GIS component of MCPUIS. This <sup>fi</sup>gure demonstrates the importance of GIS in the MCPUIS architecture as well as its use in the storage/retrieval/display of data (i.e., the SRDD function). The GIS component can generate a 3-D model of the terrain enhancing the impacts of the altitude difference (ranging from 20 m to 132 m), which are an important parameter for any water supply problem. Fig. 2 shows how MCPUIS can represent the infrastructure changes associated with each alternative. For example, existing pipelines are represented by solid lines (pipelines are also color-coded to show diameter), and “dashed” lines represent the proposed pipelines. This <sup>fi</sup>gure also demonstrates how various infrastructure data can be highlighted and displayed. The selection of data to be displayed is made by the user by selecting the “data layers” to be shown by “checking” them on a list next to the map.

Fig. 2 also illustrates the role of the GIS component in the evaluation of alternatives (the IOE function). Interaction with the planners identi<sup>fi</sup>ed 10 criteria to evaluate the four investment alternatives, which where organized in 4 families as follows:

A. four types of infrastructure (pipeline, excavation/pavement restore, creation of new streets, construction of new water storage tank) costs;

B. operating and maintenance costs;

C. two water system bene<sup>fi</sup>ts (improvements in total network reliability, increase of ef<sup>fi</sup>ciency in water supply along the new links created to supply the new zone).

D. three social costs associated with construction impacts (impacts over the road users, impacts over residents, interference with other existing infrastructures as gas, electricity, cable TV networks);

The 10 criteria considered are enumerated with more detail in Table 1.

The evaluation of these criteria for the various alternatives has important spatial variations. For example, Coimbra is very hilly, and its topography (and water pressure) can vary greatly over short distances. These differences in<sup>fl</sup>uence <sup>fi</sup>xed and variable water supply infrastructure costs. Consequently, the planners have established three water pressure categories for planning and cost estimation purposes. Fig. 2 shows these three water pressure categories for the region under study. This GIS-based information is then used by MCPUIS to generate various criteria scores (e.g., <sup>fi</sup>xed and operating network costs) for the various investment options. For example, costs of road pavement and excavation depend on the areas affected and volumes of excavation in each type of soil and rock. The areas of road pavements were automatically evaluated as a function of the diameters of pipes using the GIS function buffer; a 3-D digital model of the terrain with the geotechnical characteristics of the soil was developed in the GIS allowing the automatic evaluation of volumes to be excavated in soil, soft rock and hard rock. The impacts over residents living near the zones affected by construction works were evaluated by using maps of soil usage (city urban plan of Coimbra). All this information gathered with the GIS is utilized in the comparison of alternatives – IOCS function of MCPUIS.

Table 1  
The criteria considered in the case study.

<table><tr><td>Family A:</td><td>Costs of infrastructure (acquisition, installation and construction)</td></tr><tr><td>A.1</td><td>Costs of conduits (pipes and accessories need for the installation)</td></tr><tr><td>A.2</td><td>Costs of installation (pavement removal, opening ditch, close ditch, pavement restore)</td></tr><tr><td>A.3</td><td>Creation of new streets (according to Portuguese laws the conduits should be located along streets)</td></tr><tr><td>A.4</td><td>Costs of new reservoirs and reinforcement of water elevation stations</td></tr><tr><td>Family B:</td><td>Operating and maintenance costs</td></tr><tr><td>B.1</td><td>Costs of operating during the life of the project (e. g. energy)</td></tr><tr><td>Family C:</td><td>Profitability of the investment</td></tr><tr><td>C.1</td><td>Increase of robustness to the overall water supply system (e. g. increase of reliability)</td></tr><tr><td>C.2</td><td>Increase of capacity of the water supply system (e. g. increase of storage capacity and water transportation)</td></tr><tr><td>Family D:</td><td>Impacts during the building of the new infrastructures</td></tr><tr><td>D.1</td><td>Impacts over the road users (social costs incurred over the users of the affected roads during construction works)</td></tr><tr><td>D.2</td><td>Impacts over neighbor zones (it goes beyond D.1 concerning the citizens living near the zones affected by construction works)</td></tr><tr><td>D.3</td><td>Interference with other existing infrastructures (other infrastructures exist in the underground, as gas, electricity, cable TV, that can be affected by the construction works; there is, at least, an associated risk of damage of other infrastructures when opening the ditch).</td></tr></table>

MCPUIS incorporates additional graphic capabilities to facilitate the DM's comparison of the various alternatives (IOCS function). Fig. 3 shows two MCPUIS generated graphs comparing the performance of the four alternatives according to the SAW and TOPSIS techniques. This <sup>fi</sup>gure displays the performance of the alternatives vis-à-vis the various criteria as weighted by the municipal planning department (the DM). The required weights were elicited from the DM by MCPUIS, being automatically re-scaled so that they sum to 100 to facilitate the analysis. Using this weight information, those two methods ranked the top two alternatives similarly.

The comparison of the alternatives with the ELECTRE I method is represented by means of an oriented “outranking graph” displaying the outranking relationships established. These relationships do not need to be neither transitive nor complete. In our problem, alternative 3 “outranks” alternatives 1 and 2, while alternative 4 is incomparable with any other alternative according to the information and parameters provided.

MCPUIS displays like that in Fig. 3 compare the alternatives via their “aggregated” performance as appraised by one or more of the MCDA methods. MCPUIS also includes graphical displays to help the DM assessing the alternatives via their performance on the individual criteria. Fig. 4 shows two displays for aiding a direct comparison of alternatives in the criterion space - columns graph and BAGAL [4].

BAGAL has an axis radiating out from the origin like the spokes of a wheel for each of the 10 criteria. The interior and exterior boundaries of the BAGAL are determined by the “ideal” and “anti-ideal” solutions (used in TOPSIS). The criterion values for each solution are plotted and connected by color-coded lines. With the BAGAL graphic, the DM can readily compare the alternatives to each other as well as to the “ideal” and “anti-ideal” solutions via their performances on the individual criteria.

The results provided by the three MCDA methods incorporated into MCPUIS are greatly in<sup>fl</sup>uenced by the technical parameters supplied by the DM (e.g., weights and threshold values). In order to cope with the subjective nature of most of these inputs, MCPUIS includes a “sensitivity analysis” function to determine how stable (robust) the results are regarding these inputs. This capability combined with the ease by which the DM enters the various parameters allows him/her to experiment with distinct sets of values to help specify them via a progressive learning process.

An example of this type of analysis is shown in Fig. 5 for the SAW ranking of the alternatives. Given the criterion weights provided by the members of the local planning department (the DM), SAW and TOPSIS ranked the investment alternatives in the following order: $a _ { 3 } ,$ $a _ { 1 } , a _ { 2 } , a _ { 4 }$ (a designates “Alternative i”). This is referred to as the “Base solution” (S<sub>B</sub>) in Fig. 5. However, SAW scored alternatives 2 and 4 about equally while TOPSIS showed a strong preference for alternative 2 over alternative 4 (Fig. 3).

Each row in Fig. 5 displays the weights assigned to each criterion A.1 to D.3. The minimum and maximum values on each row (shaded areas) represent the range of the DM's acceptable values for the weight on the criterion. The bold vertical line represents the weight assigned by the DM in the analysis that resulted in the current ranking (S ). The darker shaded area of each rectangle shows the range for which the DM assigned weight on a particular criterion may vary and the corresponding ranking determined by SAW ( $\mathrm { i . e . , } S _ { \mathrm { B } } \colon a _ { 3 } , a _ { 1 } , a _ { 2 } , a _ { 4 } )$ does not change. Changing any of the criterion weights to a value in the lighter shaded area of any of these rectangles will result in a different ranking of the four alternative courses of action: $S _ { \mathrm { A } } \left( \mathrm { i } . \mathrm { e } . , a _ { 3 } , \right.$ $a _ { 1 } , ~ a _ { 4 } , ~ a _ { 2 } )$ . In the case study, the sensitivity analysis on the SAW criterion weights indicates that the ranking is quite stable. For example, Fig. 5 shows that the SAW ranking will not change regardless of the weights assigned to criteria A3, D1 and D3. The ranking is most sensitive to the weight assigned to criterion C2. An important <sup>fi</sup>nding of this sensitivity analysis is that the top two SAW ranked alternatives $( a _ { 3 } , a _ { 1 } )$ do not vary regardless of the weights assigned to the criteria in the SAW method (assuming that they remain within the DM provided ranges shown in Fig. 5). The required weights were elicited from the DM by MCPUIS, being automatically re-scaled so that they sum to 100 to facilitate the analysis.

![](/api/attachments/HAJSRNXV/fulltext/images/010230271d655410fc6deda83cadc0670e5c0b2c0f7366d6c045883a27bd59c5.jpg)

![](/api/attachments/HAJSRNXV/fulltext/images/b74f0deab88dfda0fbfc90b469460eb403cc2499d9c00aca8e59d250694c3dd5.jpg)  
Fig. 3. Graphic Representation of SAW and TOPSIS Rankings

![](/api/attachments/HAJSRNXV/fulltext/images/e988dbdeb919de9f73507c8ace71942e36b8ce42e6e10f817973d9c303f3454a.jpg)  
Fig. 4. Comparison of alternatives in the criterion space - columns and BAGAL

As already mentioned for ELECTRE I, “alternative a outranks alternative $b "$ is veri<sup>fi</sup>ed using the concordance (a majority of criteria supports it) and non-discordance (no criterion is strongly opposed to it) principles. The user-de<sup>fi</sup>ned thresholds of concordance and discordance of ELECTRE I play an important role and may in<sup>fl</sup>uence the <sup>fi</sup>nal outranking relations. The variation of those parameters was performed and the results obtained are presented in Fig. 6, where the set of not outranked alternatives is represented for several pairs of threshold values located in the 4 regions of the <sup>fi</sup>gure. It can be observed that alternative $a _ { 3 }$ is never outranked by any other alternative for any pair of values of those thresholds. However, $a _ { 1 }$ is always outranked by, at least, one other alternative. This conclusion also remains valid for weight changes (not presented here due to space limitations).

As there is no “best” MCDA method [7], MCPUIS includes three methods with distinct underlying assumptions. MCPUIS can then be used to determine how sensitive the results are with respect to the MCDA method instantiated with different sets of preference information and technical parameters.

## 4. Conclusion

Urban infrastructure investments are typically strategic and longterm in nature. The bene<sup>fi</sup>ts and costs of such investments are distributed spatially; therefore, they affect various stakeholders differently. Moreover, multiple, often con<sup>fl</sup>icting and incommensurate, evaluation aspects are at stake for assessing the merits of the potential alternatives. A prototype GIS-based, Multicriteria Spatial Decision Support System (MC-SDSS) called MCPUIS (Multicriteria Planning of Urban Infrastructure Systems) has been developed for providing assistance to planners in the evaluation process. The primary functions of MCPUIS are: SRDD (storage, retrieval, and display of data); IOE (investment option evaluation); IOCS (investment option comparison and selection); and CISA (communication/interaction with the system and sensitivity analysis). The various capabilities of MCPUIS were demonstrated with a case study from the City of Coimbra, Portugal, which motivated the development of this system. MCPUIS was used to evaluate and compare four investment options to expand the water supply network to serve a proposed 77 hectare development on the city's edge. Ten different criteria were explicitly considered to compare and evaluate the 4 alternative courses of action. This evaluation process is facilitated by the GIS component of MCPUIS. MCPUIS incorporates three MCDA methods (SAW, TOPSIS, and ELECTRE I) to help the DMs to compare and evaluate the alternatives. The sensitivity analysis function of MCPUIS revealed that the results obtained in the Coimbra case study were rather robust.

![](/api/attachments/HAJSRNXV/fulltext/images/e347dcac4a770f810b3d6786aa63cd250e649493878aa360c95a06dc9a71160f.jpg)  
Fig. 5. Sensitivity Analysis on SAW Criterion Weights.

![](/api/attachments/HAJSRNXV/fulltext/images/938e08e0d90ee7490b85f9c9be67a720ae6dbfacc6daf78afd72354ef26fadb7.jpg)  
Fig. 6. Sensitivity Analysis on ELECTRE I concordance and discordance thresholds

## References

[1] S. Chakhar, V. Mousseau, GIS-based Multicriteria Spatial Modeling Generic Framework, International Journal of Geographical Information Science 22 (11–12) (2008) 1159–1196.

[2] T. Chenoweth, K.L. Dowling, R.D. St. Louis, Convincing DSS Users that Complex Models are Worth the Effort, Decision Support Systems 37 (1) (2004) 71–82.

[3] C.W. Churchman, R.L. Ackoff, An Appropriate Measure of Value, Journal of Operations Research Society of America 2 (2) (1954) 172–187.

[4] J. Coutinho-Rodrigues, J. Current, J. Climaco, S. Ratick, An Interactive Spatial Decision Support System for Multiobjective HAZMAT Location-Routing Problems, Transportation Research Record 1602 (1997) 101–109.

[5] J. Figueira, V. Mousseau, B. Roy, ELECTRE Methods, in: J. Figueira, S. Greco, M. Ehrgott (Eds.), Multiple Criteria Decision Analysis: State of the Art Surveys, Springer, 2005, pp. 133–153.

[6] T. Hanne, Intelligent Strategies for Meta Multiple Criteria Decision Making, Kluwer Academic Publishers. Boston. 2001

[7] B.F. Hobbs, P. Meier, Energy Decisions and the Environment: A Guide to the Use of Multicriteria Methods, 1st editionKluwer Academic Publishers, Boston, 2000.

[8] P. Jankowski, Integrating Geographical Information Systems and Multiple Criteria Decision-making Methods, International Journal of Geographical Information Systems 9 (1995) 251–273.

[9] P. Jankowski, A. Zielinska, M. Swobodzinski, Choice Modeler: a Web-based Spatial Multiple Criteria Evaluation Tool, Transactions in GIS 12 (4) (2008) 541–561.

[10] H. Karnatak, S. Saran, K. Bhatia, P. Roy, Multicriteria Spatial Decision Analysis in Web GIS Environment, Geoinformatica 11 (2007) 407–429.

[11] R.L. Keeney, H. Raiffa, Decisions with Multiple Objectives, John Wiley and Sons, New York, 1976.

[12] V. Maniezzo, I. Mendes, M. Paruccini, Decision Support for Siting problems, Decision Support Systems 23 (1998) 273–284.

[13] B.H. Massam, Muti-criteria Decision Making (MCDM) Techniques in Planning, Progress in Planning 30 (1) (1988) 1–84.

[14] E. Natividade-Jesus, J. Coutinho-Rodrigues, C. Antunes, A Multicriteria Decision Support System for Housing Evaluation, Decision Support Systems 43 (3) (2007) 779–790.

[15] D.L. Olson, H.M. Moshkovich, R. Schellenberger, A.I. Mechitov, Consistency and Accuracy in Decision Aids: Experiments with four Multiattribute Systems, Decision Sciences 26 (1995) 723–748.

[16] T. Ormsby, E. Napoleon, R. Burke, C. Groessl, L. Bowden, Getting to Know ArcGIS Desktop, 2nd EditionESRI Press, 2008.

[17] B. Roy, The Outranking Approach and the Foundations of ELECTRE Methods, in: C. Bana e Costa (Ed.), Readings in Multiple Criteria Decision Aid, Springer-Verlag, 1990, pp. 155–183.

[18] B. Roy, D. Bouyssou, Aide Multicritère à la Décision: Méthodes et Cas, Economica, Paris, 1993.

[19] A. Simão, P. Densham, M. Haklay, Web-based GIS for Collaborative Planning and Public Participation: An Application to the Strategic Planning of Wind Farm Sites, Journal of Environmental Management 90 (6) (2009) 2027–2040.

[20] E. Triantaphyllou, Multi-Criteria Decision Making Methods: A Comparative Study, Applied Optimization Series 44, Kluwer Academic Publishers, Boston, 2000.

[21] D.A. Tsamboulas, G.K. Mikroudis, TRANS-POL: A Mediator Between Transportation Models and Decision Makers’ Policies, Decision Support Systems 42 (2) (2006) 879–897.

[22] F. Witlox, M. Antrop, P. Bogaert, P. Maeyer, B. Derudder, T. Neutens, V. Acker, N. Wegh, Introducing Functional Classi<sup>fi</sup>cation Theory to Land use Planning by Means of Decision Tables, Decision Support Systems 46 (4) (2009) 875–881.

[23] K.P. Yoon, C.L. Hwang, Multiple Attribute Decision-Making: An Introduction, Sage Publications, London, 1995

João Coutinho-Rodrigues is currently Professor at the Department of Civil Engineering, Faculty of Sciences and Technology, University of Coimbra (where he has been since 1980), and senior researcher in the Decision Support in Systems Engineering group at INESC-Coimbra. He received his Degree in Civil Eng., his MSc in Computer Science and PhD in Civil Eng. from the University of Coimbra. Research interests include: decision support systems, multicriteria analysis, networks, GIS, and applications in urban/environmental/transportation engineering. He has published, among other journals, in: Computers & Operations Research, Decision Support Systems, International Journal of Computer Applications in Technology, Journal of Business Logistics, Journal of Infrastructure Systems - American Society of Civil Engineers, Municipal Engineer, Transportation Research (Part A and Part B), Transportation Research Record, Geographical Analysis, Socio-Economic Planning Sciences, Waste Management, Water Power & Dam Construction.

Ana Simao is currently a researcher in the Decision Support in Systems Engineering group at INESC-Coimbra. She received her Degree in Civil Engineering from the Technical University of Lisbon, her MSc in Civil Engineering from the University of Coimbra and her PhD in Geography from the University College London. She has been a lecturer at the Dept. of Civil Engineering, University of Coimbra, from 1998 until 2007. Research interests include: GIS, decision support systems, multicriteria analysis

Carlos Henggeler Antunes received the Ph.D. degree in electrical engineering (optimization and systems theory) from the University of Coimbra, Coimbra, Portugal, in 1992.He is a Professor with the Department of Electrical Engineering and Computers, University of Coimbra, and Director of the R&D Unit INESC Coimbra. His research interests include multiple objective programming, decision support systems, and energy planning
