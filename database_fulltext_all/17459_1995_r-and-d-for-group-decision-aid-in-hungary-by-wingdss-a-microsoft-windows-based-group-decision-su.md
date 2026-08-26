---
otero_id: 17459
otero_key: "B7QAE2VX"
title: "R and D for group decision aid in Hungary by WINGDSS, a Microsoft Windows based Group Decision Support System"
authors: "Péter Csáki; Tamás Rapcsák; Piroska Turchányi; Mátyás Vermes"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00017-m"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# R and D for group decision aid in Hungary by WINGDSS, a Microsoft Windows based Group Decision Support System

Péter Csáki, Tamás Rapcsák, Piroska Turchányi \*, Mátyás Vermes

Department of Operations Research and Decision Systems, Computer and Automation Institute, Hungarian Academy of Sciences, H-1518, P.O. Box 63, Budapest, Hungary

## Abstract

A flexible and complex Group Decision Support System for PC-s in Microsoft Windows environment is presented. Several real-life applications have been carried out with WINGDSS. The Multi-Attribute Decision Aid type system reflects the logical structure of the problem as well as the preferences and the expertise of decision makers. We assume a heterogeneous group in a soft negotiation situation. Both factual data and subjective factors will be taken into account when qualifying the alternatives. Arrival at a group ranking satisfactory to all members is supported by a series of possibilities to use WINGDSS interactively, and by integrating feedbacks from individuals. The interface to relational databases, the tree handling 'AROMA' modul for problem structuring, the dialog box editor, the built-in interpreter for evaluating the alternatives ensure the applicability of WINGDSS in various decision situations. Experiences with real life decision problems are reported.

Keywords: Multi-Attribute utility decomposition; Group Decision Support System

## 1. History

The main activities of our department have been modeling, methodological research and software development for single decision support systems with applications in the field of electrical energy optimization or production control for more than a decade.

Research on group decision support began at the end of 1989 only, in a period when our country had rather limited possibilities for obtaining up-to-date computer hardware and software.

Due to technological and social burdens, convincing managers about coordinating their decision activities by a computerized process was nothing else but a nice dream.

A small group started the research and development of a GDSS [1]. Our aims were to create a system which

\- is flexible and adjustable to different types of decision situations at several institutions and organizations,

\- has an attractive user interface,

\- can integrate other algorithms, decision support systems developed at our department or in other institutions,

and last but not least,

\- whose performance is comparable to that of similar Hungarian or international systems.

Completed in 1992, WINGDSS 2.1 is being used at the Tender Bureau of the Hungarian Telecommunications Company. An experimental model for the appraisal of hotels has been worked out for the State Property Agency. The allocation process at the Ministry of Welfare of social budgets was supported by WINGDSS. A joint research project for possible applications of the system in environment monitoring and environment impact assessment (EIA) processes is being carried out with the Ministry of Environment and Regional Policy. Due to the efforts in exploring the fields of real life application, we have been gathering a lot of useful experience that also define the directions for further research and development: The newly designed, recoded WINGDSS 3.0 arrived at its testing phase in 1993.

## 2. Summary of WINGDSS features

## 2.1. Hardware requirements

WINGDSS has been developed on PC, under Microsoft WINDOWS. This feature improves the user-friendliness of the system but at the same time, as the complexity of WINGDSS increases, the hardware requirements widen. The early versions of WINGDSS [1], [2] and even Version 2.1 run on PC AT 286, as well. The latest version, WINGDSS 3.0 just being developed [3], requires a PC 386 with at least 4MB RAM.

## 2.2. Outline of the system

The class of (group or single) decision problem which is supported by WINGDSS is as follows:

One or more decision makers from different fields but with a common interest have the task of ranking certain alternatives that have been previously given and characterized by a finite set of criteria or attributes.

There exist systems for preference modelling [7], i.e. where the aim is to verify the ranking what decision makers have already in their mind.

The concept in WINGDSS is different. WINGDSS provides a final evaluation for every alternative ensuring a ranking according to the final scores. Moreover, the modul for sensitivity analysis can provide help to achieve the desired ranking of the alternatives.

The attributes of alternatives can be factual data evaluated equally by decision makers, and subjective factors to which each DM may give different scores.

Idea organization is a key issue in a decision process. In WINGDSS the hierarchy of criteria is a tree, which is most helpful in many cases for problem structuring. We plan to handle, however, net type structures, as well.

Decision makers define the set of criteria which is not necessarily identical to the set of alternative attributes. The root of the tree can be the problem itself which will be gradually decomposed into less complex subproblems or criteria. The nondecomposable criteria are called the leaves of the criterion tree.

A leaf criterion is the smallest unit to be evaluated, and it is generally not a single alternative attribute. WINGDSS has a built-in function editor and compiler to define functions or rather small procedures to evaluate an alternative at each leaf criterion. These procedures may access several attributes, factual and subjective ones. Consequently, the score belonging to a leaf criterion will be the result of a more or less complicated calculation involving some attributes.

Decision makers express the importance of any leaf or higher level criterion by assigning preference weights to them. No method for determining these weights has been included into WINGDSS yet, but the variations of the weights can be taken into account by assigning intervals in which the weights may vary, and it is possible to examine the effect of the changes on the final ranking.

Starting from the lowest level of the criterion tree, the combination of the preference weights and scores at the leaves results in scores at higher level nodes. The latter nodes are also associated with preference weights, consequently, the calculation can proceed toward the root where the final score to each alternative is determined.

Thus, this procedure provides for each decision maker the individual cardinal ranking which reflects both the alternatives' characteristics and the DM's individual preferences. In a group decision situation, however, group ranking should incorporate the different priorities and the expertise of decision makers as well. This is achieved by assigning voting powers to each DM at each criterion, i.e. at each node of the criterion tree.

The present version runs on a single PC (with a system facilitator or supervisor) but also provides the atmosphere of a decision room with networked computers: task formulation, idea generation, and team building are supported in many ways, but at the same time, the individuals' privacy is also ensured. The new WINGDSS 3.0 will be completed as a multiuser system by the end of 1993.

## 2.3. Flexibilities from problem modeling to group ranking

We view the group decision process as a three-phase event:

\- task preparation,

\- individual ranking,

\- group ranking.

This concept defines three subtasks for a virtual separation of the activities. The subtasks do not describe the sequence of actions in an obligatory way: switching from one phase to another is possible at any stage.

A group decision system is not allowed to be problem specific. Within organizations groups are formed to work on decision problems, but they are disbanded when the problems are solved. Consequently, the types of decision problems, the composition of the group, the characteristics of the decision makers, the set of alternatives, the set of criteria, the methods for evaluation would vary from problem to problem.

In the preparation phase of the decision task WINGDSS 2.1 provides operations for

\- selecting the alternatives from an outer database by a filtering mechanism,

\- creating and modifying the set of alternatives connected to the system's inner database,

\- creating and modifying the tree of criteria, - defining or modifying the name, the authorities and the classification of decision makers.

More features will be present in the new WINGDSS 3.0, in which

\- any data of the alternatives and that of the decision makers, furthermore, any kind of results will be stored in outer (WINDOWS compatible) databases,

\- the dynamic linkage to these databases will be provided (i.e. any modification carried out by the user from the WINGDSS system will be recorded in the outer databases),

\- the criteria tree will be stored also separately in order to be reused by other decision models.

WINGDSS shows a lot of potential in the phases of individual and group ranking. The built-in compiler in WINGDSS ensures the creation or modification of the appropriate functions or procedures for individual evaluations. A list of built-in functions is also available. The necessary modifications can be carried out with or without the help of a system facilitator.

The arrival at a group ranking satisfactory to all members is supported by a series of possibilities using WINGDSS interactively. Preference weights and voting powers can be updated by any authorized user. In addition, sensitivity analysis can be carried out for

– studying the effect of the variations of the main decision parameters (individual preferences, voting powers of decision makers, scores given by decision makers),

– investigating the stability of the final ranking of the alternatives,

\- examining the possible dominance of a criterion,

\- calculating the possibility of moving an alternative to its desired place.

## 3. Mathematical formulation

Consider a decision problem with l group members $D_{1}\ldots D_{l}$ , n alternatives $A_{1}\ldots A_{n}$ and m criteria $C_{1}\ldots C_{m}$ .

As described earlier, the criteria are arranged hierarchically into a directed tree. One starts, for example, with the problem that will be the root of the tree. Then, two or more general criteria are defined, and each of them will be decomposed into even more specific criteria. The endpoints of the tree, the simplest criteria, are called leaf criteria. Proceeding from the root toward the leaves, the subsequent criteria define subtrees with one father node and two or more child nodes.

The simple subtrees consisting of some leaves and their father nodes are the starting places in the evaluation process. Denote the leaf criteria belonging to a simple subtree by $N'$ .

## 3.1. Individual ranking

A procedure is attached at each leaf $C_{i}$ to evaluate one or more alternative attributes, belonging to the same leaf. In case of factual data, the return value i.e. the result of the evaluation at a leaf criterion must be identical for any decision maker, while subjective attributes can be evaluated differently by each DM. Denote the result of the evaluation of decision maker $D_{k}$ for alternative $A_{j}$ on the leaf criterion $C_{i}$ by $a_{i,j}^{k}$ . Assume that the problem arising from the differences in the dimension of the attributes has already been settled, and the $a_{i,j}^{k}$ values are the results of the proper transformation.

The individual preferences on the criteria are expressed as weights at each branching of the tree. Let the weights $w_{i}^{k} \geqslant 0$ be assigned by $D_{k}$ at $C_{i}, i = 1 \ldots m; k = 1 \ldots l$ . Note that the preference weights are independent of the alternatives.

To begin with, the normalized linear combination is calculated at each simple subtree $N'$

$$
\mu_ {j} ^ {k} = \frac {\sum_ {i \in N ^ {\prime}} w _ {i} ^ {k} a _ {i , j} ^ {k}}{\sum_ {i \in N ^ {\prime}} w _ {i} ^ {k}}, \quad j = 1 \dots n; k = 1 \dots l.\tag{1}
$$

The $\mu_{j}^{k}$ value is assigned to the root of this simple subtree, i.e. at the father node of the appropriate set of leaf criteria. If that node is not the root of the whole tree, then, there are at least two nodes at that level with normalized weights and with $\mu_{j}^{k}$ values resulted from (1). While proceeding on the tree toward the root, weights on the higher level criteria are combined with values obtained from one level below. The final individual score by $D_{k}$ for $A_{j}$ will be the value assigned to the root, and the alternatives will be ranked in descending order.

Note that an additive multi-attribute model is applicable only to decision problems when the additive independence of the criteria can be proved. [5,8]. Therefore, the decision problem should be carefully analysed with respect to additive independence.

The new WINGDSS 3.0 has the option of calculating the arithmetical or the geometrical mean of scores and weights.

## 3.2. Group ranking

WINGDSS has its special way for calculating the group result. The different knowledge and priority of a group member are expressed by voting powers both for weighing and qualifying. For factual data only the preference weights given by the decision makers will be revised at each criterion by the voting power for weighing. However, in case of subjective attributes, not only the weights but also the $a_{i,j}^{k}$ values will be modified at the corresponding leaf criteria by the voting powers for qualifying.

Let $V(w)_{i}^{k}$ denote the voting powers assigned to $D_{k}$ for his/her weighing on any criterion $C_{i}$ , and $V(q)_{i}^{k}$ the voting powers assigned to $D_{k}$ for his/her qualifying on the leaf criteria $C_{i}$ , $j = 1 \ldots n$ ; $k = 1 \ldots l$ .

Now, the method of calculating the group utility of the alternative $A_{j}$ is as follows:

The preference weights will be aggregated into group weights $W_{i}$ at each criteria $C_{i}$ :

$$
W _ {i} = \frac {\sum_ {k = 1} ^ {l} V (w) _ {i} ^ {k} w _ {i} ^ {k}}{\sum_ {k = 1} ^ {l} V (w) _ {i} ^ {k}}, \quad i = 1 \dots m.\tag{2}
$$

The group qualification $Q_{i,j}$ at each leaf criterion $C_{i}$ for each alternative $A_{j}$ is:

$$
Q _ {i, j} = \frac {\sum_ {k = 1} ^ {l} V (q) _ {i} ^ {k} a _ {i , j} ^ {k}}{\sum_ {k = 1} ^ {l} V (q) _ {i} ^ {k}}, \quad i \in N ^ {\prime}; j = 1 \dots n.\tag{3}
$$

The group utility of $A_{j}$ is the result of the normalized linear combination of the aggregated qualification values with the aggregated weights:

$$
U _ {j} = \frac {\sum_ {i} W _ {i} Q _ {i , j}}{\sum_ {i} W _ {i}}, \quad j = 1 \dots n\tag{4}
$$

proceeding from the leaf level toward the root.

Similarly to the individual evaluation process, the new WINGDSS 3.0 also offers the geometrical mean.

The best group alternative is the one associated with the highest group utility. A correct group utility function for cardinal ranking must satisfy the axioms given in [9]. Function (4) is appropriate in this respect.

4. Activities with WINGDSS during the decision process

This part is illustrated with the screen prints of a simple DEMO program of WINGDSS 2.1. The three main menu groups correspond to the three phases of the decision process. Moving back and forth, however, is always possible with reasonable limitation (e.g. without defining certain parameters in the preparational phase, it is impossible to work in the other phases).

## 4.1. Task preparation phase - Decision task menu

A system facilitator or supervisor composes the decision group (with on-screen operations), defines the individuals' authorities, gives the passwords and assigns the voting powers. The authorities (see Figure 1) include the right to construct and modify the set of criteria, the set of alternatives, the data of group members, the right to define the evaluation procedures, and the right to review the individual evaluations and to process the aggregation. Menu items during the session will be activated or disabled accordingly.

![](/api/attachments/B7QAE2VX/fulltext/images/150f236b41399c1f023595eb9d78ece9a61bc876a66c89f5e1233c3e31f4155d.jpg)  
Fig. 1.

The tree of criteria will be constructed by the supervisor or by an authorized decision maker.

Creating and modifying this tree with on-screen operations are technically possible due to the AggRegated Object MAnagement (AROMA)

module of WINGDSS. AROMA, developed by our team, is also applicable to several types of graph handling tasks separately from the WINGDSS system: nodes and subtrees can be constructed, moved, copied, deleted, renamed and arranged in several ways (see Figure 2).

Decision makers and alternatives are also formally arranged into simple trees in WINGDSS 2.1, and the creation and modification of these sets are also done by AROMA. The data of alternatives can be entered directly or they can also be selected from a relational (dBASE compatible) database. A methodology for selecting records from the outer database can also be defined from the WINGDSS, providing a screening on the alternatives. One can simply append the criteria set with a leaf node for selection, and connect a procedure including the selection parameters, as it is shown in Figure 3.

![](/api/attachments/B7QAE2VX/fulltext/images/3a0d2b1f650077fedea3a89c0339a7a8bf16ef3eb439c5b714fed5cc77889059.jpg)  
Fig. 2.

By prescribing a threshold value, one simply browses in the database for the records on which the value of that particular selection function will achieve the threshold. The browsing process will stop at each appropriate record, and the system offers this record to be included as an alternative into the inner database.

The language for writing the above procedures is easy to learn and, in addition, all the standard functions of the C library can be applied. Figure 4. illustrates how the dialog box and the procedures for a particular leaf criteria should be created and tested. The evaluation procedures can be saved to the system database for immediate use, but they can also be stored separately for later use (with minor modifications if necessary) in a different decision task.

In the file menu it is possible to create a new procedure (with its dialog box), to load a procedure created before, to save it to the system and to store it as a separate file. The edit menu contains the usual text editing functions (copy, cut, paste, ...). The control menu is for creating static-, edit-, checkboxes and radio buttons. In the options menu one can switch from edit mode to test mode and vice versa.

## 4.2. Individual decision phase - Individual decision menu

After a successful login (name and password), a decision maker can start his/her individual evaluation process. When weighing the criteria (see Figure 5.), one does not have to care about normalizing the weights, since the system will perform this task.

![](/api/attachments/B7QAE2VX/fulltext/images/bf9c54a7965bc2a05e60c61542b93be2f9d5b0dbb8ad8d5a7a97f2577e7984bc.jpg)  
Fig. 3.

When qualifying the alternatives, one selects an alternative and works with the leaf criteria. The result immediately appears on the screen, as it is illustrated in Figure 6. Working with problems involving a large number of alternatives, the users complained about the time consuming effects of this process. Consequently, in Version 3.0 the evaluation will be carried out automatically by the system.

## 4.3. Group ranking phase - Group decision menu

The group score of an alternative will be processed as described in Part 3.2.

The opinions of other group members will often cause one member to reconsider and modify his/her evaluation. Such feedbacks can be taken into account in the following manner: any decision maker is allowed to activate the Individual decision menu again for performing modifications in the evaluation of the subjective criteria or for changing his/her preferences. If changes are required in the structure of the decision task, and/or in the form of the evaluation procedure, then they can be performed in the Decision task menu.

The algorithm for sensitivity analysis can be used for answering the following questions:

\- What are the intervals in which the weights can vary without effecting the ranking of the alternatives?

![](/api/attachments/B7QAE2VX/fulltext/images/eb52d8f837f9bc278def3fe34b3799c31e206a798004f3a07b55f75512da04c8.jpg)  
Fig. 4.

\- If the weights are allowed to vary in given intervals, how will the value and position of the alternatives be changed?

\- What kind of transformations are needed to change the position of one particular alternative (to move one low ranked alternative to a better place, for example)?

\- If the scores are allowed to vary (within given intervals) for a certain set of alternatives, how will this phenomenon effect the values (consequently, the position) of the remaining alternatives?

\- Are there criteria dominating the ranking?

The method applied at this phase is described in [11] and will be integrated into Version 3.0. Two different approaches of this theme are reported in [12] and [13].

One more characteristic of group ranking in WINGDSS should be pointed out here: the possibility of defining a threshold for the score at each criterion is provided. Alternatives having a score below the critical value at one or more criteria are excluded. They are listed with the size of the exclusion; see Figure 7.

Group results again, can be reviewed in several ways, by tracing back to the scores given individually by the decision makers; see Figure 8.

## 5. Applications

The institutions where WINGDSS has been applied are the Tender Bureau of the Hungarian Telecommunications Company (bid evaluation, product and technology selection), the Ministry of Welfare (allocating budgets among social institutions), and the Ministry of Environment and Regional Policy.

![](/api/attachments/B7QAE2VX/fulltext/images/52c1f65722d14032d31288d541e91a033342e7bf647dc1cb2d45e7c8a1fa5e88.jpg)  
Fig. 5.

In the Ministry of Welfare more than 250 applications had to be evaluated and ranked. Fortunately, the problem could be decomposed into subproblems where three or four decision makers evaluated 40-50 alternatives. A lot of time and effort had been devoted to setting up the criterion tree and the appropriate evaluation procedures. This problem inspired the interface to outer databases and the creation of a possibility for screening the alternatives. The screening procedure has been used for rejecting applications not conforming to the rules and for creating the subproblems. Criteria were categorized as financial, professional, functional. Among the financial criteria there were subjective and objective ones: the decision makers were asked, for example, to score certain aspects of the financial plan worked out by the applicant, and, at the same time, economic factors were calculated and scored independently from the decision makers' individual opinion. The professional and functional criteria were further decomposed, as well, and evaluated similarly to the way described at the financial criteria.

An experiment with appraising hotels has been carried out for the State Property Agency. Fifteen hotels were evaluated and ranked. Criteria were grouped into three groups, namely: economic, market and others. The economic criteria were decomposed into condition, income revenue- and goodwill analysis. The market criterion reflected the fair market value. The others criteria were decomposed into the quality of staff's work, occupancy, services and similar subcriteria. To evaluate the income revenue, the goodwill and the fair market value functions suggested by experts in hotel appraisal were applied. Certain parameters (discount factor, capitalizable rate of interest, modernization factor, etc.) could have been varied. The evaluation of the remaining criteria was totally subjective.

![](/api/attachments/B7QAE2VX/fulltext/images/59718c72430cd1eb364b2efc994d90da7c4af297087aa35ed8aef020f25ae739.jpg)  
Fig. 6.

Our recent project with the Ministry for Environment and Regional Policy includes assistance in several complex decision problems. In order to avoid the undesirable environmental impacts of human activities, a careful analysis must be carried out before starting new construction projects, modifying technologies, or introducing new ones, stopping current industrial or agricultural activities. The project includes the integration of a Geographic Information System into WIN-GDSS.

At present we are conducting a mission with our WINGDSS system in the really difficult process of convincing people to use computers for supporting their decision problems. Hopefully, the real life applications of WINGDSS will convince the possible users about its higher efficiency.

## 6. Summary, conclusions and experiences

Due to the fact that WINGDSS is a quantitative system, qualitative information must be

![](/api/attachments/B7QAE2VX/fulltext/images/b749b0b4c05216ebe474d35cb602d5596de5725e6c0bfe25771745bd9bf2e15d.jpg)  
Fig. 7.

scored, i.e. transformed also into numbers. Factual data are often used in problem specific, well defined functions (e.g. determining the revenue of a hotel or a company). The subjective attributes are usually rated by the decision makers with values from a predefined list of scores. Logical attributes are mostly associated with zero - one values. Attributes are often measured in different dimensions, that is why the software system must ensure that the values resulting from the evaluation procedures vary in the same range for each evaluated criteria. This can be done with a proper mapping. The evaluation procedures can be defined with the built-in language. The dynamic linkage with WINDOWS compatible databases has already been worked out. The system has a lot of interactive features. The new version of WINGDSS will be able to integrate program solvers, as well.

WINGDSS is capable to handle several hundred criteria or alternatives. In practice, to follow a tree of hundred nodes by scrolling the screen is not an attractive activity and the speed of evaluation also depends on the problem size. To grasp the decision situation well, the decomposition of large problems into subproblems (10–20 criterion nodes, 5–20 alternatives) is strongly recommended.

Various types of algorithms are reported in the literature on preference structure determination, on finding the correct preference function [6]. The weights in WINGDSS must be given explicitly by the users. Fortunately, our partners were able to cope with this task. In addition, using the sensitivity algorithm, validation or correction of the weights can be done effectively.

![](/api/attachments/B7QAE2VX/fulltext/images/090a54e9dfb255eb9d5e39a11650c93d1ace1391ee371585ae68df43885ff9bd.jpg)  
Fig. 8.

## Acknowledgement

This research was supported in part by the Hungarian National Committee for Technical Research and Development through Grant G1-16-138/88. Another support is given in part by the Hungarian National Research Foundation, OTKA No.2568.

## References

[1] M. Bíró, P. Turchányi and M. Vermes, CONDOR: Consensus Development and Operations Research tools in Group Decision Support Systems, Research Report CAI HAS 23/1989 (December 1989).

[2] M. Bíró, P. Csáki, M. Vermes, WINGDSS Group Decision Support under MS-Windows, in: Proceedings of the Second Conference on Artificial Intelligence, Von Neumann Society, (January 1991) Budapest, Hungary.

[3] P. Csáki, L. Csiszár, F. Fölsz, K. Keller, Cs. Mészáros, T. Rapcsák, P. Turchányi, A flexible framework for hierarchical decision support: WINGDSS 3.0, Research Report CAI HAS (April 1993).

[4] S. Dyer and K. Sarin, Measurable Multi-attribute Value Functions, Operations Research 27, No. 4 (July–August 1979).

[5] P.C. Fishburn, Utility Theory for Decision Making, John Wiley and Sons, New York, 1970.

[6] E. Jacquet Lagrez and J. Siskos, Assessing a Set of Additive Utility Functions for Multicriteria Decision Making, the UTA Method, European Journal of Operational Research 10, No. 2 (June 1982).

[7] T. Kämpke, F.J. Radermacher and P. Wolf, Supporting preference elicitation – The FAW preference elicitation tool, Decision Support System 9 (July 1993).

[8] R.L. Keeney, Multiplicative Utility Functions, Operations Research 22, No. 1 (January–February 1974).

[9] R.L. Keeney, Group Preference Axiomatization with Cardinal Utility, Management Science 23, No. 2 (October 1976).

[10] R.L. Keeney, Building Models of Values, European Journal of Operational Research 37, No. 2 (November 1988).

[11] Cs. Mészáros and T. Rapcsák, Sensitivity Analysis on Decision Problems, Research Report CAI HAS (Aug. 1992), accepted in Decision Support Systems.

[12] S. Soofi and J. Retzer, Adjustment of Importance Weights in Multi-attribute Value Models by Minimum Discrimination Information, European Journal of Operational Research 60, No. 1 (July 1992).

[13] R. Vetschera, Integrating Databases and Preference Evaluations in Group Decision Support, Decision Support Systems 7, No. 1 (January 1991).

[14] M.J. Wang, H.P. Singh and W.V. Huang, A Decision Support System for Robot Selection, Decision Support Systems 7, No. 3 (August 1991).

Péter Csáki is on the staff of the Department of Operations Research and Decision Systems, Computer and Automation Institute, Hungarian Academy of Sciences. He graduated in applied mathematics at the Eötvös Loránd University Budapest, Hungary. His recent interests include object oriented system analysis research, design and development. Previously, he carried out biometrical and statistical research. He was involved in the simulation of biological and ecological systems, in a joint project with IIASA on shallow lake modelling (the lake Balaton in Hungary).

Tamás Rapcsák is the head of the Department of Operations Research and Decision Systems, Computer and Automation Institute, Hungarian Academy of Sciences and the leader of the Group Decision Project. He graduated in mathematics at the Kossuth Lajos University, Debrecen, Hungary. He holds a Candidate Degree of Sciences and a Ph.D. in Operations Research. His research interests are in the areas of nonlinear programming, classical and modern differential geometry. He carried out numerous modelling activities on practical problems such as minimum weight design of the lateral walls of buses, design of terrain correction works, sewerage networks as well as irrigation and drink water networks. He has been the supervisor of several Ph.D. students. His current research field is the description of the structural properties of decision models with differential geometrical and tensor optimization tools. He published in several professional journals on operations research such as Jota, Ejor, Optimization, Zamm and Global Optimization. He is the president of the Hungarian Operations Research Society.

Piroska Turchányi is on the staff of the Department of Operations Research and Decision Systems, Computer and Automation Institute, Hungarian Academy of Sciences. She holds a Ph.D. in Operations Research. She graduated at the Eötvös Loránd University Budapest, Hungary. Her interests include research and modelling of computer supported collaborative systems. She has been carried out a lot of scientific organizational activities.

Mátyás Vermes was previously on the staff of the Department of Operations Research and Decision Systems, Computer and Automation Institute, Hungarian Academy of Sciences. He holds a Ph.D. on Geophysics, he recieved M.S. degrees both in Geophysics and Applied Mathematics at the Eötvös Loránd University Budapest, Hungary. He has been carried out various software developments in Fortran, C and database handling systems. He was engaged in the development of the WINGDSS system.
