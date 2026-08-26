---
otero_id: 17187
otero_key: "C3DJYRZG"
title: "Information structuring and its implementations on a research decision support system"
authors: "Mitsuhiko Toda; Kunihiko Hiraishi; Toramatsu Shintani; Yoshinori Katayama"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90055-g"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information structuring and its implementations on a Research Decision Support System

Mitsuhiko Toda, Kunihiko Hiraishi, Toramatsu Shintani and Yoshinori Katayama

International Institute for Advanced Study of Social Information Science, Fujitsu Limited, Numazu-shi, Shizuoka 410-03, Japan

We discuss decision making processes from the viewpoint of information structuring. We consider the processes in a wide sense, and argue the need for advanced decision support systems which aid decision makers' information structuring throughout the processes. We propose a Research Decision Support System (RDSS), which is a prototype for such systems and supports decision making on research and development (R&D). In RDSS, pieces of information for a particular R&D field are classified as needs and seeds for the field, and are related and stored in databases. Their relations are summarized by R&D maps which present holistic models of the field and support selection of strategic paths of R&D. We describe our implementations of RDSS, and present the results of experiments. The functions of RDSS are general ones for information structuring, and can be used for constructing advanced decision support systems for areas other than R&D.

Keywords: Information structuring, Advanced decision support systems, R&D, Research Decision Support System.

![](/api/attachments/C3DJYRZG/fulltext/images/64f28ccfa5037f8e0ad01a5b5adb1e87b07b973ce3cb11e796fc23c55e72d16a.jpg)

Mitsuhiko Toda received the B.E. degree from the University of Tokyo in 1965, and the M.S. and Ph.D. degrees from the University of California, Los Angeles, in 1971 and 1974, respectively. From 1974 to 1977 he was with NASA's Ames Research Center. In 1977 he joined the International Institute for Advanced Study of Social Information Science (IIAS-SIS), Fujitsu Ltd., where he is currently the manager of Planning Department and a Research Laboratory. He has been doing research on applications of systems analysis to social systems and decision research. His current research interests include decision making, decision support systems and research on research.

## 1. Introduction

The importance of aids for decision making (DM) is widely recognized due to ubiquity of DM in business and societal activities. Although various kinds of computer-based decision support systems (DSS) and software are presently available in market, the scope of their support is quite limited. The limitation is inevitable due to the fact that DM requires high level intelligent activities of human decision makers and that the present state

![](/api/attachments/C3DJYRZG/fulltext/images/b9834e351b2fdc2a18cb58c96ea7a2b7f7bc7bcf57f7a3b06cb53cc427fb5eff.jpg)

Kunihiko Hiraishi received the B.E. degree from the Tokyo Institute of Technology in 1983, and the M.S. degree in 1985. In 1985 he joined the IIAS-SIS, Fujitsu Ltd. His current research interests focus on problem-solving by modeling. He is also interested in analysis of discrete event systems using Petri nets and computational learning theory.

Toramatsu Shintani received the B.E. and M.S. degrees from the Science University of Tokyo in 1980 and 1982, respectively. Since 1982 he has been an Associate Research Staff at the IIAS-SIS, Fujitsu Ltd. His current research interests include parallel logic programming, nonmonotonic reasoning, and decision support systems.

Yoshinori Katayama received the B.E. and the M.S. degree from the Science University of Tokyo in 1985. In 1985 he joined the IIAS-SIS, Fujitsu Ltd. His current research interests are in the areas of object-oriented model, object-oriented database programming systems, and applications of artificial intelligence techniques to designing decision support systems.

of art of computer technology is not advanced enough to replace essential parts of the activities.

The concept of DSS was initiated by Gorry and Morton in 1971 [4], and research has been conducted on the kinds of supported DM activities, conceptual frameworks for systems, and pioneering systems. Serious efforts of research aiming at advanced DSS have recently been started as a multidisciplinary field of research [6], and the number of research-oriented articles has been increasing, as compared with application-oriented ones [3]. The advancement of artificial intelligence tools and their applicability to advanced DSS have a significant impact on such efforts. Applications of these tools have recently been actively proposed for constructing DSS together with conventional tools; database management tools and modeling methods of management science/operations research. We will discuss the details of this trend in section 5 based on the concrete models we have developed.

The purpose of this paper is to argue the need for supporting functions of DSS in structuring information throughout DM processes, and to propose a prototype system which demonstrates such capabilities. We consider a DM process in a wide sense, and interpret it as a process of information structuring. An advanced DSS is required to support through the process in a unified manner. We propose a system called RDSS, Research Decision Support System, which provides such supporting functions. It is a “Specific DSS” [10, Ch. 1] for generating an advanced “DSS Generator” [10, Ch. 1]. We have implemented it and have conducted experiments to clarify directions of R & D for advanced DSS, using the aid of its functions.

The area of DM processes supported by RDSS is research and development (R&D). We consider the processes as a part of the activities of problem solving. Creation of new scientific knowledge and technological know-how requires highly intelligent activities of researchers and engineers. R&D is a problem solving activity that requires advanced knowledge information processing such as concept formation and all sorts of inferences, including deduction, induction and abduction. RDSS supports DM of researchers for such activities by providing functions for information structuring; classifying, systematizing, integrating and assessing knowledge and information on a particular field of R&D. With the aid of RDSS, researchers can classify pieces of information from the viewpoint of needs/seeds, relate them, store them in databases, integrate them to generate R&D maps which illustrate the field of their interest, and assess strategic paths of the R&D on the maps.

This paper consists of six sections. In section 2 we discuss information structuring activities of DM processes. In section 3 we discuss DM on R&D from the viewpoint of problem solving. In section 4 we propose and describe RDSS. In section 5 we discuss the findings obtained from experiments on RDSS. Section 6 concludes the paper with remarks concerning future topics of research.

## 2. Decision Making Processes and Information Structuring

## 2.1. Decision Making Processes

Currently available DSS provide only piecemeal support for a wide range of DM processes. We need to design and implement DSS that can support throughout the processes. The well-known model of DM processes proposed by Simon [8, Ch. 2] provides a basic framework for designing such DSS. He characterizes the processes by the following four phases:

(A) Intelligence phase; (B) Design phase;

(C) Choice phase; and (D) Review phase.

(1)

Advanced DSS should support DM activities throughout these phases in a unified manner. The need to support all these phases has been discussed (e.g. by Sprague [9]), but the unified support has not been emphasized. It will be discussed in the next section from the viewpoint of structuring information.

## 2.2. Decision Support Systems for Information Structuring

Based on the definition in Ref. [2], we define DSS as follows:

A decision support system is a computer-based system which supports a decision maker in making decisions for solving an ill-structured problem by utilizing knowledge and information of the areas related to the problem.

In this definition we consider “an ill-structured problem” as a problem for which a solution procedure is not specified completely. The description “supports a decision maker in making decisions for solving an ill-structured problem” implies that DSS supports him in structuring the problem, in other words, in completely specifying a solution procedure for the problem. The “knowledge and information of the areas related to the problem” are either stored in a DSS or supplied by the decision maker. In either case, not all the available knowledge and information are relevant or directly usable for solving the problem. Therefore, when the DSS supports in structuring the problem, it is most important that it supports in structuring information. The information structuring is integrating and transforming pieces of collected information into the one appropriate for solving the problem. This process of integration and transformation can only be performed by trials and errors due to the ill-structuredness of the problem. The “knowledge of the areas related to the problem” is utilized to guide the trials and errors. It must be supplied by the decision maker under the present state of art of technology, but will be partially stored in knowledge bases of advanced DSS to enhance the functions for unified support of information structuring.

The four phases classified by (1) can be considered as the phases of information structuring processes. A part of information collected during (A) Intelligence phase is related to the purpose of solving the problem concerned, and it can be applied to (B) Design phase only when it is integrally transformed. Based on the transformation decision alternatives are developed in this phase. In (C) Choice phase it needs to be further transformed, and additional information for assessing the alternatives needs to be integrated. As DM proceeds these phases, more specific information is required to clarify and solve the problem.

Conventional DSS only support the above process piece-wise, and a user must either process information by himself or generate programs (in many cases supported by DSS specialists) to supplement those provided by the DSS. Advanced DSS should aim at supporting decision makers throughout the above process of information structuring in a unified manner. The support enables to store information of the three phases in DSS, and to make it readily available for (D) Review phase, during which decisions made by previous phases are reassessed.

## 3. Decision Support for Research and Development

## 3.1. R & D Cycles and Decision Making

Phases of R&D cycles are properly corresponded to those in (1), and the correspondence is illustrated in fig. 1. In the Intelligence phase a researcher (decision maker) collects information concerning a field of his interest, gradually recognizes issues and problems requiring R&D, and clarifies them. This clarification eventually enables him to establish topics for R&D in the Design phase. The Choice phase encompasses the planning phase and the implementation phase of R&D activities. During the planning phase, he tries to select a topic and a course of action. After actual R&D efforts are initiated, various means for solving the topic and its subtopics are selected and pursued to attain the targeted results and intermediate ones along the planned course. The results are reexamined in the Review phase, and trigger subsequent cycles of R&D efforts. In the everlasting cycle, feedback of information occurs in various levels as shown by the arrows in fig. 1.

![](/api/attachments/C3DJYRZG/fulltext/images/04ab2b421324b743c22568d5baebc6c01bf6a5d8e233143cd49159565dbbd24b.jpg)  
Fig. 1. Correspondence of R&D Cycles and DM Phases.

![](/api/attachments/C3DJYRZG/fulltext/images/13f91c1df9570f556ac55f4f1f5d0970a8fe021073299a2de699b2bd5027ca95.jpg)

## 3.2. R&D as Solving Target Setting Problems

Sato defines problem solving as follows [5, Ch. 1].

(a) A problem is a gap between a target and the corresponding state, and requires a solution.

(b) Problem solving is resolving the gap.

(c) There are two types of problems (see fig. 2). Type I is the derailing problem in which a state has derailed in keeping track of a constant target. Solving activities for this problem involve diagnosis of finding causes of the derailment, and resolving the gap between the target and the present state by removing the causes. Type II is the target setting problem in which a present target is intentionally reset to aim at a higher level target, and a gap is generated. Its solving activities involve developing the state to resolve the gap, thus aim at a higher level state.

Fig. 2. Two Types of Problems.  
![](/api/attachments/C3DJYRZG/fulltext/images/91c222f5016c7edc0310ab6f23344248939b6f07f542386ae95b963bbcaf667e.jpg)  
Fig. 3. Elements of Original Papers.

In general, innovative R&D requires solving efforts for a target setting problem, because it is intended to create new dimensions to societies. Information for such R&D can be analyzed from this viewpoint of problem solving. Consider information contained in original scientific/technical papers, which are major sources of information for R&D activities. They contain descriptions on four elements as shown in fig. 3; motivation for R&D, existing R&D results, new results, and necessary future R&D topics/areas.

Motivation for R&D in a paper may be social demands or desire to find unknown facts, and induces setting the target of the R&D. Existing research results show the present state of art as compared with the target. Recognition and clarification of the gap between these two states enable the paper's author(s) to specify the topic of the R&D. This process can be considered as earlier phases of a DM process, which we have discussed in section 3.1. The topic is the problem to be solved by the R&D activities. This problem can be rephrased as the need for the R&D. The new results usually constitute the main body of the paper, and offer solutions for the problem. The solutions, however, are usually partial ones for the problem, and necessary future research topics/areas are discussed or suggested for its future solution. Therefore, the new results can be considered as seeds for solving the problem completely.

The emphasis on each of the above elements varies, depending on papers. There are papers solely discussing research opportunities by concentrating on the target and existing research results as the present state of art. Nonetheless, the framework in fig. 3 provides a basis for obtaining and classifying information in the papers in terms of needs and seeds for R&D. Other types of R&D information can also be classified by this framework. For example, market information is classified as information on needs, and mathematical tools are classified as seeds.

## 4. Research Decision Support System

## 4.1. Overview

We propose RDSS which supports researchers in structuring information and making decisions on their R&D. It provides supporting functions for each of the DM phases discussed in section 2, and information obtained in one phase is easily transferred to the supporting function in the subsequent phase. Researchers can integrate and transform information to structure it in a unified manner. The functions provided by RDSS are illustrated in fig. 4.

The supporting functions shown in fig. 4 are (1) functions to construct structured R&D databases for Intelligence activities;

![](/api/attachments/C3DJYRZG/fulltext/images/1996ac0baa1bd89cbdd650b2605bea81ce92ca2d59b0c7d05504fc8a20a3e694.jpg)  
Fig. 4. DM Support by RDSS.

(2) functions to generate and illustrate R&D maps for Design activities;

(3) functions to select optimal strategic paths of R&D for Choice activities.

Pieces of information on an R&D field of interest collected by Intelligence activities are sequentially structured to plan strategy for the R&D as shown in fig. 4. Each of these functions will be described in the following by taking original papers as an example of an information source. RDSS has been implemented in Quintus-Prolog on a SUN workstation with a color graphic terminal for displaying and editing R&D maps.

4.2. Functions to Construct Structured R&D Databases

RDSS provides a researcher with capabilities to construct databases as shown in fig. 5. The pieces of information extracted from collected sources like papers are stored in three kinds of relational databases (DB); needs-seeds DB, classification framework DB, and source attributes DB. Processing of these DB is managed as a group by the subsystem of RDSS, which is implemented on KORE/DB, a database management subsystem of Knowledge Oriented Reasoning Environment (KORE) [7]. The information stored in needs-seeds DB and classification framework DB is extracted from the sources and constructed through the filter of researcher's knowledge concerning his specialized R&D field as described below. Therefore, although these DB are called as databases, they should be considered as knowledge-bases, because user knowledge is incorporated in them.

## 4.2.1. Needs-Seeds Databases

The information extracted from a source is specified by keywords expressing needs and seeds for an R&D field. They are analyzed from the viewpoint discussed in section 3. In particular, when the source is an original paper, fig.3 can be applied to obtain the information. Furthermore, the needs and seeds are related by the source in the following form, and stored in the needs-seeds DB.

$$
(\text { need   keyword   n }) - [ \text { information   source   i } ]
$$

$$
- (\text { seed   keyword   s }).\tag{2}
$$

Relation (2) means that source i deals with information on need n and seed s, and furthermore, seed s is applicable to meet the demand of need n. There can be more than one need/seed related by a source, and relation (2) is modified accordingly.

A researcher's evaluations on relationships in (2) are also stored in the needs-seeds DB. The degree of relationship between need n (or seed s) and source i is evaluated by the researcher in terms of five rankings; from “most closely related” to “a little related”. These data are stored to indicate whether need n/seed s is the main subject in source i or a sub-subject of differing degrees. These data will be used when we want to generate an R&D map that focuses on important needs-seeds relations, by picking up a subset of information stored in needs-seeds DB.

## 4.2.2. Classification Framework Databases

The keywords stored in needs-seeds DB are selected from classification framework DB. The thesaurus of the keywords is classified and hierarchically structured to represent the framework of an R&D field from the viewpoint of needs and seeds.

![](/api/attachments/C3DJYRZG/fulltext/images/5d90f2b8cce5dfb8831596cf42b4cbe79e473983a4e7bf500773c50262743126.jpg)  
Fig. 5. Construction of Structured R&D Databases.

Large scale bibliographic DB generally provide keywords selected from categorized thesauri, which are fixed for a certain period. When keywords are freely selected to represent information sources, it is difficult to classify and structure them. The R&D fields intended to be supported by RDSS are growing ones, and classification framework for

![](/api/attachments/C3DJYRZG/fulltext/images/76565a509ef6a2ad9fae9f84aebfda6b56717259c8f44a2e01b7cd3770913d97.jpg)

![](/api/attachments/C3DJYRZG/fulltext/images/e84994c070c8fe6bf50314a0584df299971b45f8daab1a7dc589f16b9a4d4708.jpg)

Fig. 6. Framework of DSS Keywords.

the fields does not necessarily exist when R&D efforts are started. When a framework exists, it is tentative and is gradually structured as R&D of the field grows. Therefore, it must be flexible, and needs to be growingly restructured as information of new R&D results are added to DB. At the same time it should provide a reasonable framework to classify collected information.

RDSS provides supporting functions to meet these requirements as follows.

(1) Keywords for needs-seeds DB are selected from classification framework DB.

(2) It is possible to add and modify keywords and to restructure existing classification framework DB, when need/seed keywords for a new source of information are added to needs-seeds DB.

A thesaurus of keywords is hierarchically structured by trees, as exemplified in fig. 6, and stored in classification framework DB. The framework in fig. 6 is a part of the framework obtained from an experiment on RDSS, which is intended to support R&D on DSS and will be described in section 5. Keywords of the framework must be divided in two categories; needs and seeds. As shown in fig. 6, the trees are categorized as need trees and seed trees. This categorization will be taken into account in the functions for generating R&D maps in the next phase. For each tree, keywords are hierarchically broken down to express more specific concepts in the form of category, sub-category 1, sub-category 2,..., sub-category m, depending on the specificity required.

When a framework and keywords are updated in the classification framework DB, the information already stored in needs-seeds DB must be modified accordingly, so that it is consistent with the updated classification framework DB. This requirement is largely processed automatically by the system, by making use of trigger functions provided by KORE/DB (the dotted line in fig. 5 indicates this function). Modification in a database triggers related modification in other databases of RDSS. Some modifications in classification framework DB, however, do not automatically trigger change in needs-seeds DB. For example, when a keyword is broken down by two keywords, each of which expresses a part of the former's concept, existing information in needs-seeds DB represented by the keyword cannot be automatically broken down. Instead it is shown on an interface display so that researchers can reclassify it.

## 4.2.3. Source Attributes Databases

Basic functions of source attributes DB are the same as those of bibliographic DB; they contain information such as title, authors, etc. for the case of papers. An identification (ID) number is assigned to each source of information, and this ID number is taken as the key when the DB are manipulated together with needs-seeds DB. An additional function of source attributes DB is storing evaluation data on information sources. Each source of information is evaluated by researchers in terms of importance/significance in three categories; important, average, and irrelevant for the present interest. The evaluated data are also stored in source attributes DB.

These evaluation data of source attributes DB, in addition to bibliographic data, enable a researcher to generate subsets of information for the following phases. He can generate subsets of needs-seeds DB that focus on specific aspects of the whole DB and hence those of resulting R&D maps. For example, the following maps can be easily generated by RDSS.

(1) R&D maps generated by information of important sources

(2) R&D maps of specific areas by restricting journals of papers

(3) R&D maps representing a historical accumulation of R&D results by generating a sequence of DB in the order of publication of papers

## 4.3. Functions to Generate R&D Maps

The information stored in needs-seeds DB is transferred to the subsystem of RDSS that generates R&D maps. An R&D map represents a holistic model of a field of interest, and is displayed on a color graphic terminal. Relations of R&D needs and seeds are integrated to obtain the map, which is displayed in the form of a hierarchical graph. It visually presents correlations of the needs and the degree of the seeds' contributions to the needs. Therefore, it provides functions to assist researchers in visually grasping the trend of the R&D field and finding alternative courses of actions. These activities for planning R&D are important in the Design phase.

![](/api/attachments/C3DJYRZG/fulltext/images/65087d72fe5b7573f3fbe94cc3df7fddceaa6deac7a0823587796c8abdef7d0c.jpg)  
Fig. 7. Procedure of Visual Q-Analysis.

![](/api/attachments/C3DJYRZG/fulltext/images/6885060780e9359c08770e8eeaeeb2acb57b15cf986f84632cc81d67aedd8c06.jpg)  
zFig. 8. Needs-Seeds Relations.

![](/api/attachments/C3DJYRZG/fulltext/images/664552c2f9c648eb85b8f17bc5e96c3c5bae618cd72e1d07f574ad14c13cac24.jpg)  
Fig. 9 and 10. R&D Map I and II.

The method of Visual Q-Analysis (VQA) [11,12] is applied to obtain R&D maps in the form of F-Hierarchy and Q-Hierarchy. It accepts relational data between two sets of items, such as needs and seeds for R&D, and draws the hierarchies in the form of visually understandable maps on a display. The procedure of VQA is shown in fig. 7.

Fig. 8 illustrates an example of input to VQA, an integration of needs-seeds relations expressed by (2) with information source i deleted. The keywords in fig. 8 are abbreviations of those in fig. 6 (the attached numbers correspond to those in fig. 6). The obtained map of F-Hierarchy and that of Q-Hierarchy for this input are called R&D Map I (fig. 9) and R&D Map II (fig. 10), respectively. In section 5 more detailed maps will be shown, and their implications will be discussed as the results of experiments (figs. 11 and 12). In the following we describe briefly what we intend to represent with these maps. Readers are referred to [11] for the details represented by these maps.

In R&D Map I, needs for R&D are represented by one type of nodes (need-nodes; displayed by solid line rectangles in fig. 9). They are connected with each other and to the other type of nodes (seed-nodes; displayed by broken line rectangles in fig. 9) which represent a seed or a combination of seeds. A node is located in the hierarchy at a level, which shows the number of applicable seeds for the represented need (for a need-node) or the number of seeds represented by the node (for a seed-node). For example, need-node 3.4.6 in fig. 9 represents need 3.4.6 (DSS, Components, Inference Engine as shown in fig. 6) and is located at level 1. This means that one applicable seed is related, which we can find in fig. 8 as seed 4.6 by tracing the edge going out of node 3.4.6 (broken-lined edge). Another need-node 3.4.5 (DSS, Components, Model Base Management Systems) is located at level 6, which means that six seeds are related as applicable.

![](/api/attachments/C3DJYRZG/fulltext/images/321d4e264467935d87951c8b8445de5816e29adef6e01544208a9ea441b53023.jpg)  
Fig. 11. R&D Map I of DSS.

Connection of a need-node to a seed-node means that the seed(s) represented by the seed-node is applicable to meet the demand of the need represented by the need-node. Therefore, we can easily find needs to which the same seeds are applicable, and conversely, seeds that are applicable to multiple of needs. For example, need-node 3.4.2 of level 2 is connected to seed-node 4.8 (Theory/Methodology, Artificial Intelligence/Knowledge Engineering) of level 1 and need-node 3.4.6 which also represents seed 4.6. Need-nodes 3.2.4 and 1.6.2 are jointly connected to seed-node (4.4 and 4.8) of level 2 (by broken-lined edges). This means that these two needs share the two seeds, 4.4 (Management Science/Operations Research) and 4.8, as applicable seeds.

The R&D Map II in fig. 10 simplifies the R&D Map I in fig. 9, and represents the correlational structure of the needs in a form of tree graphs, where the correlation is specified by a chain of the above joint applicability of seeds (this chain is obtained as q-connectivity of Q-Analysis [1]). The greater the degree of q-connectivity, the more closely related the needs are in the sense that more seeds are commonly applicable to them. R&D Map II is particularly useful when we analyze a large set of needs and seeds, since it simplifies and summarizes R&D Map I, and hence we can easily observe holistic correlational structures.

R&D Maps I and II integrate and structure collected information in Needs-Seeds DB. They illustrate alternative needs for R&D, and assist researchers in finding strategic plans in the Choice phase that focus the R&D on particular needs.

## 4.4. Color Graphic Displays for R & D Maps

RDSS automatically draws R&D maps on a color graphic terminal in the form of visually understandable graphs whose nodes and edges are so arranged that there are less crossings of lines and that nodes are located to maintain balance (figs. 9 and 10 show the examples).

![](/api/attachments/C3DJYRZG/fulltext/images/93f8a96dc64eacb7d1a6a10671faa05771a20944b4e283c58b6741bf6cee2a51.jpg)  
Fig. 12. R&D Map II of DSS.

Its displaying functions are menu-driven, and provides researchers with the following capabilities, so that they can easily conduct experiments on the maps to structure their thoughts and build up concepts of the R&D field.

(1) multiwindow display functions for the analysis using multiple of maps;

(2) functions for enlargement (partial enlargement), reduction and rotation of maps;

(3) functions for editing maps on a display and storing them;

(a) addition and deletion of nodes and edges;

(b) relocation of nodes and edges;

(c) selection of color and shape of nodes;

(d) selection of types of lines for edges;

(e) modification of keywords of nodes;

(f) writing comments;

(g) storing edited maps in a file;

(4) functions for displaying focused parts of a map.

When certain weights are attached to the nodes of a map, parts of the map can be displayed for the nodes whose weights are more (or less) than a specified threshold value. As an application of this function, parts of a map can be sequentially displayed in the order of a specified sequence of threshold values for the weights specified by utility indicators, which will be described in section 4.5. This function is particularly useful when an RDSS user wants to display the most significant part of a map to focus his attention, and then gradually enlarges the map according to the significance. Another purpose of this function is to display a growing path on a map, which shows a strategic path of R&D determined during the Choice phase (see section 4.5).

It is important that keywords of maps are readily readable on a display, because they convey important notions for R&D. This requirement cannot easily be met on a limited area of CRT display, especially for large scale maps. RDSS provides selectable means to meet the requirement, which are a short form representation, a coded table form representation, and a pop-up display of keywords.

## 4.5. Functions to Select Optimal R & D Paths

Strategic analysis for R&D can be investigated on R&D Map I with an aid for selecting optimal paths on the model. The paths are determined on the map to select topics of R&D for meeting needs by developing relevant seeds and integrating them, where the seeds are selected in the order of importance. The method for finding the paths has been proposed in [11], and is called STI Analysis, the analysis on Strategies for Technology Integration. In the following we outline procedures of STI analysis, which focus on the effects of particular R&D efforts for all the needs considered in the map.

STI Analysis first computes the importance of a need-node on the map in the sense how much effects R&D for the need has on other needs. The measure Con(n), called concentricity of need n, expresses its importance and is computed by

$$
\sum_ {i = 1} ^ {m} (\text { number   of   needs   to   which }
$$

$$
\operatorname{Con} (n) = \frac {\text { seeds } s _ {i} \text { is   applicable)}}{\text {(number of seeds appli- cable to need n)}},\tag{3}
$$

where $s_{1},\ldots,s_{m}$ are seeds applicable to need n. The greater $\mathrm{Con}(n)$ is, the more effective the R&D for n is in the sense that the developed seeds can be applied to more of the other needs of the map.

STI Analysis then computes utility indicators for all the nodes of the map. First, it assigns Con(n) as the utility indicator of need-node n. The indicators are computed from the top level and go downward on the map, because need-nodes are located in upper levels and seed-nodes are connected to these (see fig. 9). The indicator of a need-node is distributed to connected seed-nodes according to their contribution to the need. The distributed utility indicators from multiple of need-nodes to a seed node are summed to compute the indicator of the seed-node.

Finally, STI Analysis determines the optimal path(s) for R&D to meet a target need (or needs) on the map by an algorithm that searches for the nodes of greatest indicators, thus determining the order of developing relevant seeds. A researcher can determine the target need(s) by considering their concentricity and additional information on his R&D. For example, he can determine the target by integrally judging the concentricity of need-nodes and other factors of his R&D, such as cost-benefit ratios and resource constraints.

He can modify the second and final steps of STI Analysis by assigning a judgmental indicator to need-nodes, instead of concentricity, on the map. RDSS will generate more realistic optimal paths if he provides the indicator which expresses his overall judgment of the importance of the needs including cost and other factors of R&D.

Thus STI Analysis supports researchers in judging macroscopic directions of R&D, or in determining microscopic choice of R&D paths, depending on the scope of the model represented by an R&D Map I and the specificity of keywords assigned to its nodes.

## 5. Experiments in the Field of DSS

We have implemented the RDSS described in section 4 and have conducted experiments to examine feasibility of the proposed approach. One of the motivations for the experiments is the need to clarify the directions of R&D for DSS, since future advanced DSS need to be contributed from multidisciplinary fields and are still open to our efforts of R&D, as we have discussed in section 1.

## 5.1. Outline

As the first step of the experiments, we selected the papers in the “Decision Support Systems” journal as the source of information. We sampled the original papers in Vol. 2 (1986) and Vol. 3 (1987), totaling 44 papers (We omitted the papers in No. 3 of Vol. 3, because all of them are either reviews or expository papers).

The authors played the role of an RDSS user, and interactively created a framework of 116 keywords and stored them in a classification framework DB, of which 56 keywords represent needs and the rest (60 keywords) represent seeds of R&D for DSS. The framework, which we have created from the papers and other information sources and experiences, sufficiently encompasses the field relevant to R&D for advanced DSS.

The keywords dealt in the papers are those listed in fig. 6. We obtained 25 needs and 28 seeds to generate needs-seeds relations like those in fig. 8. Their keywords are listed as leaf categories (lowest level categories) of the trees in fig. 6. Applying VQA to the relations, we obtained R&D Map I in fig. 11 and R&D Map II in fig. 12. We computed utility indicators to assess importance of nodes by the procedures described in section 4.5. Fig. 11 illustrates the importance of the nodes by the darkness of their backgrounds; the darker a node is, the greater its utility indicator is.

Figs. 8 and 9 were obtained by aggregating the DB for figs. 11 and 12. For example, need-node 3.4.5 in fig. 9, representing Model Based Management Systems (MBMS) of DSS, aggregately represents need-nodes 3.4.5.2, 3.4.5.3, 3.4.5.4, and 3.4.5.5 in fig. 11, each of which describes different aspects of MBMS as shown in fig. 6.

## 5.2. Findings of Experiments

Observing figs. 11 and 12, we can obtain the following findings from the collected and structured information.

(1) Supporting capability for modeling is the central topic of needs for DSS. It has been actively approached from the viewpoint of DSS functions, because we can observe in fig. 11 that need-node 3.2.4 (DSS, Function, Modeling) is located at level 7, indicating that seven seeds have been proposed for the need. From the viewpoint of DSS components, four need-nodes 3.4.5.2 (level 4), 3.4.5.3 (level 6), 3.4.5.4 (level 1), and 3.4.5.5 (level 4), which are drawn by double line rectangles, represent various aspects of the needs for constructing MBMS components. These aspects are Framework, Model Representation, Model Building, and User Model Interface, as shown in fig. 6. In particular, Model Representation aspect represented by node 3.4.5.3, located at level 6, is considered as the most important one for constructing MBMS.

We should note that one of the issues of the “Decision Support Systems” journal (Vol. 2, No. 1: 10 original papers) is a special issue on model management systems. This issue significantly contributes to the above observations on the importance of modeling. Nonetheless, the maps reflect the trend contained in the sample information sources, and clearly illustrate its details and relationship with the other needs.

(2) It is quite natural that many seeds are proposed for management DM, which is represented by need-node 1.5 at level 4. Another related need is represented by node 1.6.2 at level 5, which indicates the DM need for strategic planning. The fact that these needs require modeling support is clearly shown by the broken-lined edges in fig. 11 connecting these nodes with the nodes we have discussed in (1). For example, nodes 1.5 and 3.2.4 are jointly connected to seed-node (4.4.2 and 4.8.5.1) at level 2, which indicates that seeds 4.4.2 (Mathematical Programming) and 4.8.5.1 (Knowledge Representation) are jointly applicable to these needs. Although we have to check the details of the seeds proposed for these needs, by going back to needs-seeds DB, we can clearly see correlations of the needs in the sense that they share the seeds as applicable. This supporting function of visually displaying correlations of needs is one of the advantages provided by RDSS.

(3) Need-node 1.2 (level 4) representing the need of group DM has need-node 1.3 (organizational DM; level 3) as its child (the relationship shown by dotted-lined edge connecting them). This parent-child relationship means that the set of seeds applicable to need 1.2 contains those for need 1.3 as its subset. Another child of node 1.2 is need-node 1.8.4 (Multi-criteria DM; level 1), which is also shown by a dotted-lined edge. These correlations explicitly show that the need of group DM encompasses a wider scope than the other needs in terms of applicable seeds.

(4) From the viewpoint of seeds, we first focus our attention on the nodes at level 1, and then trace connected edges to the nodes of upper levels. The nodes represent seeds or combinations of seeds, which are applicable to multiple of needs. At level 1 we can find three important categories of seeds, which are Artificial Intelligence/Knowledge Engineering (AI/KE) seeds, Data Base

Management Systems (DBMS) seeds, and those of Management Science/ Operations Research/ Decision Analysis (MS/OR/DA). Important AI/KE seeds are those concerning Knowledge Representations: 4.8.5.2 (Frames and Scripts), 4.8.5.6 (Multiple Agent/Actor; represented by need-node 3.4.4.1), and 4.8.5.1 (represented by need-node 3.4.4.2). Important DBMS seeds are relational ones (6.2.2; represented by need-node 3.2.1). Important MS/OR/DA seeds are 4.4.2 (Mathematical Programming), 4.3.4 (Multi-objective DA; represented by need-nodes 1.8.4 and 3.3.1). Also Logics (4.6.4; represented by need-nodes 3.4.2.2 and 3.4.6) are considered as important seeds for DSS.

(5) Another important category of seed is 4.2.3 (Concept, Framework; represented by need-node 3.3.3), which represents the results of efforts for establishing conceptual frameworks for DSS. A similar finding has been reported in Ref. [3]. This category is the seed specific to DSS field. The authors believe that more R&D should be directed toward this area so that the DSS discipline develops to a well established one, which provides guidelines and methodology by integrating the seeds of other disciplines discussed in (4).

We can quantitatively confirm the observations in (1)-(5) by the utility indicators shown in fig. 11 by the darkness of the need-nodes and seed-nodes.

In order to investigate the trend study based on R&D Maps, we generated the maps for a subset of the information source. The comparison between figs. 11 and 12 and corresponding R&D Maps generated from 25 papers of Vol. 2 (1986) revealed that the above findings hold for the latter, except those in (3). The importance of the need for group DM (1.2) is not observed on the subset maps.

(6) The above observations can be summarized by fig. 9, which is obtained by aggregating the needs and seeds obtained for figs. 11 and 12. It illustrates that in order to meet the important DSS needs of modeling support for various types of DM, seeds in the new emerging area of AI/KE have been actively proposed to be utilized together with those in the conventional area of R&D for DSS, which are MS/OR/DA and DBMS.

Figs. 9–12 provide us with concrete models in illustrating recent R&D efforts for DSS. We only have collected information from papers in two volumes of a journal, but the above findings clearly show the trend of R&D we would capture by reading through the papers. The R&D Maps in the figures are models of different degree of aggregation for solidifying such efforts of collecting and structuring R&D information. Furthermore, RDSS supports us in accumulating our knowledge in the field and dynamically directing our R&D efforts by enabling to construct adaptably growing databases.

With diversified sources of information, we can obtain models of a wider scope, and plan macroscopic directions of R&D for DSS with the aid of STI Analysis. With a more specific framework of keywords, we can determine microscopic choice of R&D paths by using the method.

## 6. Concluding Remarks

We have argued the need for advanced DSS which support information structuring throughout DM processes in a unified manner. Then we have proposed RDSS as a prototype for such systems. After discussing major functions of the system, we have described our implementations and presented the results of experiments for the purpose of supporting R&D for advanced DSS.

Although the area of DM supported by RDSS is R&D, its functions are general ones for information structuring. They can be used for constructing advanced DSS for other areas. For example, DM for strategic business planning would require such functions during its process.

Integrating and structuring pieces of information on RDSS requires that each piece concretely and reliably specify some need or seed of an R&D field. Therefore, it is necessary to establish a thesaurus of keywords and a classifying framework for specifying the information. We have to enhance the functions of RDSS for supporting such activities. One of the necessary future R&D topics is the methodology to support in establishing classification frameworks like that in fig. 6, based on a set of keywords obtained from information sources. Another topic related to this is a method for flexible keyword matching that can account for semantic synonyms and keywords describing related concepts. The method will substantially enhance the functions for supporting the use of the classification framework DB and needs-seeds DB. The area of wider scope requiring future research is integration of information on other aspects of R&D into RDSS, such as cost, risk and schedule. In particular, we need to extend STI Analysis so that we can quantitatively consider resource constraints when we investigate optimal R&D paths. Future research is envisaged in these directions.

This is a part of the work in the major R&D of the Fifth Generation Computer Project, conducted under the program set up by MITI.

## References

[1] R.H. Atkin, From Cohomology in Physics to q-connectivity in Social Science, Int'l J. Man-Machine Studies 4, Nr. 2 (1972) 139–167.

[2] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Developments in Decision Support Systems, in: M.C. Yovits, Ed., Advances in Computers, Vol. 23 (Academic Press, New York, 1984).

[3] J.J. Elam, G.P. Huber and M.E. Hurt, An Examination of the DSS Literature (1975–1985), in: E.R. McLean and H.G. Sol, Eds., Decision Support Systems: A Decade in Perspective (Elsevier, Amsterdam, 1986).

[4] G.A. Gorry and M.S.S. Morton, A Framework for Management Information Systems, Sloan Management Review 13, Nr. 1 (1971) 55–70.

[5] I. Sato, Mondai no Kouzougaku (A Structural Study of Problems) (Diamond, Tokyo, 1977) (in Japanese).

[6] H.J. Schneider and A.B. Whinston, Editorial, Decision Support Systems 1, Nr. 1 (1985) 1–4.

[7] T. Shintani, Y. Katayama, K. Hiraishi, and M. Toda, KORE: A Hybrid Knowledge Programming Environment for Decision Support Based on a Logic Programming Language, in E. Wada, Ed., Logic Programming '86 (Lecture Notes in Computer Science, No. 264) (Springer, Berlin, 1987).

[8] H.A. Simon, The New Science of Management Decision, revised ed. (Prentice Hall, Englewood Cliffs, 1977).

[9] R.H. Sprague Jr., A Framework for the Development of Decision Support Systems, MIS Quarterly 4, Nr. 4 (1980)1–26.

[10] R.H. Sprague Jr. and E.D. Carlson, Building Effective Decision Support Systems (Prentice-Hall, Englewood Cliffs, 1982).

[11] K. Sugiyama and M. Toda, Visual Q-Analysis (I) and (II), Cybernetics and Systems 14, Nr. 2 (1983) 185–251.

[12] K. Sugiyama and M. Toda, Structuring Information for Understanding Complex Systems: A Basis for Decision Making, FUJITSU Scientific and Technical J. 21, Nr. 2 (1985) 144–164.
