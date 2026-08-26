---
otero_id: 17620
otero_key: "HAYYXBP5"
title: "A decision support system dedicated to discrete multiple criteria problems"
authors: "C. Henggeler Antunes; Luís A. Almeida; Virgínia Lopes; Joãc N. Clímaco"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90050-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system dedicated to discrete multiple criteria problems

C. Henggeler Antunes $^{a,c,1}$ , Luís A.
Almeida $^{b,c}$ , Virgínia Lopes $^{b}$ and João N. Clímaco $^{b,c}$

$^{a}$ Department of Electrical Engineering, University of Coimbra, Coimbra, Portugal

$^{b}$ Faculty of Economics, University of Coimbra, Coimbra, Portugal

$^{c}$ INESC, Núcleo de Coimbra, Rua Antero de Quental 231 ca. 3000 Coimbra, Portugal

In most real world contexts, decisions must be made in presence of multiple, conflicting, incommensurate criteria. This paper presents a computational tool aimed at providing decision aid in the evaluation of a finite and explicitly known set of alternatives over several criteria. The system has been designed as an experimentation framework for helping analysts in the practice of decision aid, and it can be customized to specific decision situations. This decision support system (DSS) consists of a problem editor, a problem compiler, a set of multiple criteria decision aid (MCDA) methods, a dialogue base and a data management module. The DSS intends to make the most of a user-friendly computer interface in order to minimize the cognitive effort required from decision makers (DMs). The set of methods includes some representative discrete alternative MCDA methods, underlying different philosophies and strategies for selecting, clustering or ranking the alternatives. Some features of this DSS will be illustrated by considering a case study of evaluation of alternative power generation expansion policies.

Keywords: Decision support systems; Multiple criteria decision making; Human-computer interaction; Computer graphics; Interactivity; Decision theory

![](/api/attachments/HAYYXBP5/fulltext/images/4530bea2a5b9db454fd26664ebd9dc0c903d25ed46f45e38af44827adcf244c0.jpg)

Carlos Henggeler Antunes is an Assistant Professor at the Department of Electrical Engineering, University of Coimbra, and a researcher at INESC. He holds a Ph.D. in Electrical Engineering (Optimisation and System Theory) from the University of Coimbra. His current research interests include multiple criteria decision aid, design of interactive Human-computer environments, combining operational research and expert system techniques in the framework of deci sion support systems, and telecommunications network modernization planning. He has published articles in Foundations of Control Engineering, Mathematical and Computer Modelling, Engineering Optimisation, European Journal of Operational Research, Computers and Operations Research and Operations Research Letters, among others.

![](/api/attachments/HAYYXBP5/fulltext/images/b7aa61e6ef2b9d96ca8652ddc35ee634e37ba57012a2e00201fba8180dea924c.jpg)

Luís Alçada Almeida is an assistant lecturer at the Faculty of Economics, University of Coimbra, and a researcher at INESC. He holds a computer science engineer degree from the University of Coimbra and he is currently preparing a M.Sc. dissertation. His research interests are interactive computer graphics and multiple criteria decision aid.

![](/api/attachments/HAYYXBP5/fulltext/images/66d20fc717a2ac3979d711c1fbab09b9f09565a5556116ebaf6ef4b075b854f6.jpg)  
Virgínia Lopes received a computer science engineer degree from the University of Coimbra. She is currently working at the Legal Medical Institute in Coimbra.

## 1. Introduction

In most real world contexts, decisions must be made in presence of multiple, conflicting, incommensurate criteria. This paper deals with decisions where the universe of alternatives corresponding to different courses of action is discrete (finite and explicitly known a priori). A level of achievement for the different criteria (which may not necessarily be quantifiable) is associated with the various alternatives.

Several methods exist to deal with discrete multiple criteria decision problems. However, these methods are difficult to classify, evaluate and compare since they are based on distinct assumptions about the DM's preferences and require different types of preference information. Nevertheless, two main broad “schools” are generally distinguished: the so-called “american” and “french schools”. In the first one we may include the methods based on the multiattribute utility theory (MAUT) and AHP, which aggregate the different criteria in a sole function to be optimized. In the second one, we may include the methods based on an outranking relation which represents the DM's preferences. The first category of methods assumes that an implicit utility function exists and that the information given by the DM about his/her preferences is consistent with this function. The second category of meth-

![](/api/attachments/HAYYXBP5/fulltext/images/8ff8b4edc928444cbcdbc6800137dbad167f114c45615da99a83761d13991cd5.jpg)

João Namorado Clímaco is a Professor at the Faculty of Economics, University of Coimbra, and he is the Director of the Coimbra branch of INESC. He holds a M.Sc. in Control Systems from the Imperial College of Science and Technology (University of London) and a Ph.D. in Electrical Engineering from the University of Coimbra. His current research interests include multiple criteria decision aid, mathematical programming techniques, Human-computer interaction, decision support systems and energy planning. He has published articles in IEEE Transactions on Power, Apparatus and Systems, Foundations of Control Engineering, JORBEL, Mathematical and Computer Modelling, Engineering Optimization, European Journal of Operational Research, Computers and Operations Research and Operations Research Letters, among others.

ods aims at constructing and exploring the out-ranking relation in order to aid the DM in the decision process. The frontiers between these “schools” are sometimes fuzzy ones, namely when the interactivity with the DM plays a key role throughout the decision process (combining computation phases with dialogue phases involving the DM).

Other characteristics may be used for classifying discrete MCDA methods. For instance, these may be categorized according to the different levels of preference information required from the DM: no information, information on criteria, and information on alternatives [4].

The selection of the most appropriate MCDA method from the several alternative methods is a multiple criteria problem in itself [5]. So, the need arises to have the possibility of making comparative evaluations of the application of different MCDA methods and/or to profit from the potentialities of each method in certain phases of the decision process (for instance, in reducing the universe of alternatives). These possibilities can contribute to improving the DM's cognitive representation of the decision situation and minimize the cognitive effort required from him/her.

A DSS has been developed which integrates some representative discrete alternative MCDA methods in the operational framework of a flexible and user-friendly computational tool. The system has been designed as an experimentation framework for helping analysts (with previous experience and theoretical knowledge of the methods) in the practice of decision aid. The aim is to provide the analysts a powerful and flexible tool, in which experiments can be carried out in order to acquire further insights into the working of the methods as well as their adequacy to distinct types of problems and DMs. The DSS can be customized to specific decision situations, by considering only the most adequate methods and developing dedicated meaningful interfaces in order to be used directly by DMs, though the mediation of an analyst with methodological knowledge is advisable.

The possibility of performing experiments is a key issue in multiple criteria decision aid. The need and usefulness of performing experiments is emphasized in [3], because (i) some knowledge is better than none; (ii) experiments are a way of recording the history of methodological issues;

(iii) experimental results discourage useless metaphysical speculation and help to define new theoretical and empirical questions; (iv) experiments have an important effect on practice by showing what works. This is in close relation with the importance of exploring the effect of the lack of determination of the parameters with respect to the robustness of the conclusions of MCDA studies [7].

In the context of a specific decision situation, the possibility of combining the methods can be of interest. The knowledge about the problem acquired with the application of a method can contribute, for instance, to the elimination of some alternatives thus reducing the universe where a compromise alternative which most corresponds to the (evolving) DM's preferences must be chosen. This computational tool aims at taking into account the evolutionary nature of the decision process, by enabling a previous stage of exploration of the problem where the DM can gather knowledge about it and/or to revise his/her a-priori preferences (mostly related to past similar problems he/she dealt with). This structure accommodates the “erratic” component inherent to a decision making process, trying to make the most of its creative nature in order to gain new insights into the problem that will be useful in the next stages of the decision process.

The man-machine interaction is a fundamental component of the DSS, having in mind to amplify the DM's capabilities of information processing and decision making and facilitate the processes of the system's acceptability and learning [1]. The system aims at obtaining a balance between the potentialities that are offered to the user (system's functionality) and the ease of learning and use (system's usability). Special attention must be paid to the main limits of people (memory, accurate calculating, and patience) and their main strengths (visual scanning, learning highly integrated and complex material) must be potentialized. Although the ease of learning is a key issue in the success of MCDA computational tools, we have tried to avoid the tendency towards the development of computer applications which may be easy to learn, but which are not sufficiently powerful to accomplish the task they are intended to perform [6].

Some features of this DSS will be illustrated by means of a case study dealing with the evaluation of alternative power generation expansion policies based on economic and welfare criteria.

The motivation and the interest of the study have been provided in the introduction. In section 2 a computer implementation of a DSS dedicated to discrete multiple criteria problems is described. A problem of evaluation of power generation expansion alternatives is briefly reviewed in 3. In section 4 some features of the system are illustrated using this case study. Some conclusions are drawn in 5.

## 2. A computer implementation of a DSS for discrete multiple criteria problems

## 2.1. The global architecture of the system

The DSS consists of five main components: a problem editor, a problem compiler, a set of MCDA methods, a dialogue base and a data management module.

Firstly, the user describes the problem in terms of criteria, alternatives and scales (qualitative or quantitative) in an almost natural language according to a problem-oriented grammar. The syntax rules are kept to a minimum in order to facilitate the user tasks. In this phase the user has at his/her disposal a built-in “dictionary”, offered by the problem editor, containing the reserved words that he/she can visualize on a separate window and simply copy and paste into his/her problem description on another window. The user has the option of writing this “source code” in english or in portuguese, which are both supported by the dictionary. Furthermore, the raw data can be split among different files enabling its use in different problems (some of the criteria and scales of one problem can be used in another decision problem).

The different components (criteria, alternatives and scales) of the problem are then compiled by the problem compiler generating a compact code that is used by the methods. This mechanism provides independence between the description of the problems (in their various components) and the computational operations required by the application of the methods. All the relevant information (of cardinal or ordinal type)

needed by a particular method and (for the sake of generality) not included in the problem description is later required from the user through the dialogue base, when it is needed to perform any computation.

The code generated by the compiler (object code) is composed of independent code units which can be: a scale, a criterion, all the criteria of a given problem, the alternatives or the whole problem. The level of achievement of each alternative for each criterion can be measured on a ratio, interval, ordinal or nominal scale. The independent code units can be obtained recurring to pre-definitions (code units previously compiled) instead of repeating the same entities in the description of the problem made with the editor (source code).

The set of methods includes some of the most well known discrete MCDA methods, which are representative of different “schools”, having distinct prior assumptions, and differing in the types of preference information required from and results presented to the user (see section 2.2). This DSS is an experimentation framework where the discrete MCDA methods can be used in a flexible manner so that their potentialities and limitations can be better understood. The aim is to provide the analysts an user-friendly, yet powerful, tool in which experiments can be freely carried out in order to acquire further insights into the working of the methods as well as their adequacy to types of problems and DMs. This seems an essential step towards laying the foundations for the development of guiding mechanisms aimed at supporting the user through the analysis of the decision situation (selecting the most appropriate method or sequence of methods).

The possibility of evaluating in a flexible way the results produced by the same method with different preference information or by different methods allows for a kind of sensitivity analysis. On one hand, the user can make experiments using different preference information corresponding to distinct scenarios in terms of the context of the problem and observe interactively the changes in the results. This enables to evaluate in an interactive manner the robustness of the conclusions in relation to the lack of determination of the input parameters, which Roy [7] considers to be an important issue in MCDA studies. On the other hand, the DSS enables the evaluation of the results produced by different methods requiring distinct preference information (weights, pairwise comparisons between alternatives, thresholds, etc.). This enables to enhance the comprehension of the methods potentialities as well as the recognition of the judgements which reveal to have more influence on the conclusions of the studies. The possibility of performing experiments in an interactive manner plays thus a key role in gathering knowledge not just about the problem and the methods, but also about the structure of the preferences.

For the sake of modularity and uniformity the problem description can be saved in different data files that are integrated and handled by the data management module.

In order to enhance the user's capabilities in processing the information, the dialogue base makes extensive use of graphical displays, offering the user a flexible and user-friendly environment consisting of menu handling, mouse operation, overlapping windows, pictorial controls and dialogue boxes, always keeping the user in control over the solution search process (see section 2.3).

Another fundamental characteristic of this system is the tolerance to user errors. All the dialogue boxes used to require additional information from the user are validated only when the user presses the mouse on a OK button and the data are then verified before being transmitted to the computational component. Usually, the errors are reported by an alert dialogue box indicating the error type. Most of the actions can be reversed enabling to try something out at a very “low cost”.

The system also offers the user an on-line help, accessible from a menu, where he/she can read a short information about the available actions.

In Fig. 1 a simplified block diagram of the DSS is presented.

The software has been developed in Pascal on a Macintosh II microcomputer. The size of the executable code is 243 KBytes for the present version. The program has been written in a modular way such that new methodologies and types of graphical interface can be easily added, and the DSS is currently being extended in both directions. Further work will include the study of using expert system techniques to implement guiding mechanisms aimed at supporting the user in the selection of the most appropriate method or sequence of methods in the analysis of a particular decision situation.

![](/api/attachments/HAYYXBP5/fulltext/images/dc389f8005f6269ae89e932ea93046c5bb7fd728a7b6509305023bc29f57b472.jpg)  
Fig. 1. DSS block diagram.

## 2.2. The set of MCDA methods

The set of discrete alternative MCDA methods integrates some noncompensatory procedures (where no tradeoffs occur) such as dominance test, conjunctive, disjunctive, minimax, maximax, lexicographic, elimination by the least attractive aspect, choice by the most attractive aspect, as well as some of the “classical” methods: simple additive weighting, ELECTRE methods (I, Is, III and IV), TOPSIS and AHP.

In the simple additive weighting (SAW) method the DM assigns importance weights to each criterion. A figure of merit for each alternative is obtained by multiplying the scale rating for each criterion value by the weight assigned to the criterion and then summing these products over all criteria $[4]$ .

In the analytic hierarchy process (AHP) the DM is asked to establish priorities for the criteria by judging them in pairs to evaluate their relative importance. A matrix of pairwise comparisons is constructed by reference to a fundamental semantic scale associated to a ratio scale [9].

The basic concept underlying the family of ELECTRE methods is the outranking relation between alternatives, although this relation may be formalized in different ways in different methods. An alternative A1 outranks another alternative A2 according to the whole set of criteria if the value of the performances gives a sufficiently strong argument for considering that A1 is globally as good as A2 with respect to the criteria in the DM preference model $[8,10]$ . The outranking relation does not need to be neither complete nor transitive.

The TOPSIS method is based on the concept that the chosen alternative should have the shortest Euclidean distance to the ideal solution and the furthest to the anti-ideal solution [4].

Furthermore, the user has access to a “procedure toolbox”, which includes, for example, the possibility of eliminating alternatives manually (those considered inefficient) or conditionally (those not satisfying additional constraints he/she imposes).

## 2.3. The man-machine interface

The user controls the program's behaviour just by clicking the mouse or typing the keyboard. These actions are viewed by the system as input events which are recorded for later processing in an event queue, which in turn feeds them to the program to be processed in an orderly way. The computer interface is mainly based on:

\- A menu bar at the top of the screen lists the titles of the available pulldown menus, grouping the actions available to the user, thus not occupying screen space and not requiring command memorization. However, most of the menu available actions have their equivalent in keyboard commands (something that becomes more important as the users become more acquainted with the system).

\- Overlapping windows are used by the program for displaying tabular and graphical information to the user.

\- Pictorial controls provide the user a intuitive way for specifying his/her preferences (slide bar controls have a moving indicator that displays the current setting and can be manipulated with the mouse).

\- Dialogue boxes are used whenever some further information is needed before a given command can be carried out, being also useful for conveying status information to the user or obtaining the user permission for potentially “dangerous” operations.

The use of visually appealing graphical displays (including the use of colours) greatly contributes to minimize the cognitive effort required from the user. However, if he/she does not feel comfortable with graphs (or prefers more exact numerical information), then he/she can freely switch to tabular presentations. Graphs enhance the comprehension of the problem and the decision making speed can be increased, mainly due to the human ability of learning highly integrated and complex material through visual scanning. Tables, providing exact values, may become less complex and more suited for the later stages of the interactive decision process.

## 3. A problem of evaluation of power generation expansion alternatives

Power generation expansion planning is intrinsically a multiple criteria problem, in which several conflicting aspects must be explicitly taken into account. As an illustrative example we will consider a problem of evaluation of alternative power generation expansion policies. A multiple objective linear programming model has been developed, which considers three objective functions quantifying the total system cost, the reliability of the supply system, and the environmental impacts associated with the expansion policies. These objectives are optimized subject to load, operational and budget constraints. A set of alternatives (considered good compromise solutions) was selected to be further evaluated considering new issues related to the impact of demand-side management (DSM) techniques (aimed at influencing the customer use of electricity in ways that produce desired changes in the utility's load shape). Some of the DSM techniques are: direct load control (DLC, which means end-use equipment control), dynamic pricing (DP, a type of incentive rate) and co-generation (CG, a type of dispersed generation). For further details on the problem see [2].

Three solutions were selected by means of an interactive three-objective linear programming package. Then 9 mixed strategies have been added to these 3 basic solution by incorporating the DSM techniques (DLC, DP and CG). Five criteria were considered to evaluate this set of alternative power generation expansion policies: cost of the KWh (measured in a ratio scale, unit \$/KWh), impact on the balance of payments (ratio scale, unit \$/KWh), creation of jobs (measured in an ordinal scale), reduction of the rate of investment in new power plants (ordinal scale) and benefits of the shifted KW to off-peak hours (ratio scale, unit \$/KW).

## 4. An illustrative example

This section aims to illustrate some features of the DSS, and it is not intended to make an analysis of the case study. The data corresponding to the power expansion planning problem, as it was edited by the user, is displayed on one or more overlapping windows which can be dragged on the screen. In Fig. 2 the windows corresponding to the scales Order and \$/KWh, the set of criteria Energy, and the whole problem PowerExpansion are displayed as they appear on the screen. Note that the pre-defined scales Order and \$/KWh are then used in the definition of the criteria, and the set of criteria are pre-defined with respect to the entity Problem. The description of the problem (source code) looks like a very simple and intuitive use of a dedicated “programming language”.

<table><tr><td colspan="6">Criteria Energy</td></tr><tr><td colspan="6">Criteria Energy;</td></tr><tr><td colspan="6">Minimize CostKWh : Scale Predef $/KWh;</td></tr><tr><td colspan="6">Minimize ImpactBP : Scale Predef $/KWh;</td></tr><tr><td colspan="6">Maximize CrJobs : Scale Predef Order;</td></tr><tr><td colspan="6">Maximize RedRateInv : Scale Predef Order;</td></tr><tr><td colspan="6">Maximize BenefitShiftKWh : Scale Predef $/KWh*</td></tr></table>

Fig. 2. Problem data.

The set of alternatives consists of 3 basic alternatives (S1, S2 and S3) and 9 mixed alternatives incorporating different DSM techniques. This initial information is always available to be brought to the frontmost screen plane.

After editing and compiling the source code describing the different components of the problem, the user can switch to the environment of method execution.

Let us suppose that the DM/analyst wants to know the alternatives which do not satisfy the requirements: cost of the KWh lower than 0.063 \$/KWh, and benefits of the shifted KW to off-peak hours greater than 1100 \$/KW. The user chooses the conjunctive method and he/she is offered a pictorial control where he/she can set the “cutting” values in an interactive way (see Fig. 3). The alternatives which do not satisfy these additional constraints are dynamically displayed in a different pattern (or colour).

Let us suppose that the DM/analyst then decided to use the TOPSIS method (not eliminating the alternatives which did not satisfy the additional constraints). A control panel consisting of slide bars for specifying the weights is shown in Fig. 4 (the signs + and - indicate whether it is a benefit or a cost criteria). The value of the weights is dynamically presented (in percentage) as the user moves any of the indicators with the mouse, the other weights being automatically scaled so that they add up to 100. It is also possible to fix some of the weights by means of the checkbox (acting as a toggle) at the right hand side of each slide bar control (in Fig. 4 the weight of the criterion benefits of the shifted KW to off-peak hours is fixed).

![](/api/attachments/HAYYXBP5/fulltext/images/b67f275345df5b938c78df9e6a8a62c9e591e2f8bf008cd9e827444088dee303.jpg)  
Fig. 3. “Filtering” the alternatives by imposing additional constraints.

![](/api/attachments/HAYYXBP5/fulltext/images/e2c82d05a9934a0a006588ccd6c47300143b5dab1afb5a1ab2f1cbf6db5bd727.jpg)  
Fig. 4. Using the TOPSIS method.

The figure of merit of each alternative is dynamically displayed in a bar graph (or in a table, according to the user specifications), as the user varies the weights.

Let us now suppose that the DM/analyst wants to make a comparative evaluation of these results with the results produced by the ELECTRE IV method, because he/she does not feel comfortable indicating weights for the criteria. The main characteristics of ELECTRE IV method which are of interest to the study of this problem are: this method does not require a prior specification of weights for the criteria and it takes into account the uncertainty associated to the data.

The user is offered a control panel consisting of slide bars for specifying his/her preference and indifference threshold levels (by clicking the checkbox the user can switch between absolute and percentage values). The final graph obtained by the application of ELECTRE IV method is displayed dynamically, showing the preference (outranking) relations in the universe of the alternatives (Fig. 5). The nodes of the outranking graph may be rearranged on the screen by the user.

![](/api/attachments/HAYYXBP5/fulltext/images/0af443a05b05def128d1b1e59ad875902dc9277121e473536113fff5eb2eb264.jpg)  
Fig. 5. Using the ELECTRE IV method.

This DSS aims to be an experimentation framework where the user can try the different methodologies and/or freely change his/her preferences in order to evaluate different scenarios, in an interactive manner. Due to its modular structure this DSS can easily integrate new methods and types of graphical interfaces. The regularities found by means of experimentation must contribute to customize the DSS to specific decision situations, by offering the most adequate methods and dedicated meaningful interfaces in order to be used directly by DMs.

This is an essential step towards laying the foundations for the development of guiding mechanisms aimed at supporting DMs through the analysis of the decision situation, namely in the selection of the most appropriate method or sequence of methods to deal with a particular type of problems.

## Acknowledgement

The authors are grateful to two anonymous referees for the comments made on a earlier version of the paper.

## 5. Conclusions

A DSS designed as an experimentation framework for helping analysts in the evaluation of a set of alternatives over several criteria has been presented. The DSS consists of a problem editor, a problem compiler, a set of discrete alternative MCDA methods, a dialogue base and a data management module. The system offers the user some representative MCDA methods, underlying different philosophies, enabling to make a comparative analysis of the results produced by different methods in order to gain new insights not just into the problem, but also into the working of the methods as well as their adequacy to types of problems and DMs. Special emphasis has been placed on the development of a flexible and intuitive man-machine interface, in order to facilitate the user tasks and increase the system's acceptability.

## References

[1] C.H. Antunes, L. Almeida, V. Lopes and J. Clímaco (1990), A user-friendly man-machine interface for a discrete multiple criteria decision support system, Proc. XI IFAC World Congress, V. Utkin and U. Jaaksoo (eds.), Tallinn, vol. 10, 165–169.

[2] J. Clímaco, A. Martins and A. Almeida (1990), On the use of multicriteria optimization for energy planning, International Journal Global Energy Issues, vol. 2, no. 3, 194–203.

[3] B. Hobbs (1986). What can we learn from experiments in multiobjective decision analysis?, IEEE Transactions on Systems, Man and Cybernetics, vol. 16, no. 3, 384–394.

[4] C. Hwang and K. Yoon (1981), Multiple Attribute Decision Making, Methods and Applications - A State of the Art Survey, Springer-Verlag.

[5] M. Jelassi and V. Ozernoy (1988), A framework for building an expert system for MCDM models selection, Presented at the VIIIth International Conference on MCDM, Manchester, 1988.

[6] J. Kammersgaard (1988), Four different perspectives on human-computer interaction, International Journal Man-Machine Studies, vol. 28, 343–362.

[7] B. Roy (1990), The outranking approach and the foundations of ELECTRE methods, Readings in Multiple Criteria Decision Aid, C. Bana e Costa (ed.), Springer-Verlag, 155–183.

[8] B. Roy and Ph. Vincke (1981), Multicriteria analysis: survey and new directions, European Journal Operational Research, vol. 8, 207–218.

[9] T. Saaty (1980), The Analytic Hierarchy Process. McGraw-Hill.

[10] Ph. Vincke (1989), L'Aide Multicritère à la Décision. Éditions de l'Université de Bruxelles.
