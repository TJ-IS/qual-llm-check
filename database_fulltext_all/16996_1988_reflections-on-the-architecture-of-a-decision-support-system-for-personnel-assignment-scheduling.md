---
otero_id: 16996
otero_key: "YQTZQ46J"
title: "Reflections on the architecture of a decision support system for personnel assignment scheduling in production cell technology"
authors: "Rolf Bühner; Peter Kleinschmidt"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90010-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Reflections on the Architecture of a Decision Support System for Personnel Assignment Scheduling in Production Cell Technology

Rolf BÜHNER, Peter KLEINSCHMIDT
University of Passau, D-8390 Passau, FRG

Within the range of new technology applications ‘flexible manufacturing systems’ are expected to give a productivity edge in market competition. Their function is based on a decentralized manufacturing organisation in form of semi-autonomous workgroups. These workgroups, consisting of a small number of workers, form so-called production cells. In this paper we want to present considerations on the architecture of a decision support system for personnel assignment scheduling within production cell organisation. Beside this, social, organisational, and qualificational aspects and requirements for the use of such systems are discussed.

Keywords: New Technologies, Production Cells, Decision Support Systems, Personnel Information Systems, Transport- and Allocation (Assignment) Problems, Group Assignments, Up-Qualification.

![](/api/attachments/YQTZQ46J/fulltext/images/ab485eb3fdab67459b1681e148ea79b1253044b668de536c6e738945b9f5bb42.jpg)

![](/api/attachments/YQTZQ46J/fulltext/images/8abdc6af0fbf642a1c0f91a732d6bd0fba78cf1a239cb430114ce2fa36b2a1a9.jpg)

Rolf Bühner is Professor of Business Administration at the University of Passau, FRG. He received his MBA at the University of Munich and his Ph.D. at the University of Augsburg. His teaching and research interests are in the fields of personnel management, new technologies and strategy. In collaboration with large German companies he has examined the personnel and organizational impacts of new technology. He has also lectured in Japan and the United States.

Peter Kleinschmidt is on the faculty of the department of mathematics and computer science at the University of Passau (F.R.G.). He was formerly a Professor at the University of Bochum (F.R.G.) and he had visiting positions at the University of Siegen (F.R.G.) and the University of Washington, Seattle. His teaching and research interests are in the areas of polyhedral theory, combinatorics, network flow algorithms and their applications in Operations Research. His research articles have appeared in numerous journals including, Mathematical Programming, Mathematics of Operations Research, Journal of Discrete and Computational Geometry, Journal of Combinatorial Theory, Mathematische Zeitschrift.

## 1. Introduction

The demand for decision support is steadily increasing as far as new technology and its implementation are concerned. This applies among other things, especially, to work organization forms such as production cells where supervisors or foremen typically serve as personnel assignment disposers and decision makers.

This paper aims at contributing to an appropriate design of architectures for decision support systems to be used in production cells. In this way it will concentrate on the treatment of specific basic aspects. A concrete transformation into a full-system realization, as followed by researchers at the University of Passau, is intended. $^{1}$

Concentrating on basic considerations, two main targets will be pursued. The first one is to demonstrate ameliorations in working conditions and staff-qualification going with the use of decision support systems in this context. The second one is to show that even on the lowest management level (supervisor level) decision problems become highly specific and therefore require efficient algorithmic tools using very specific elements (such as 'sparsity' of certain matrices). It will be demonstrated how these advantages can be systematically exploited by using suitable architectures and model-management components.

## 2. New Technologies and Work Organization

Increases in efficiency in industrial manufacturing by means of new technologies represent a substantial challenge for personnel management. New technologies in this area may offer strategic competitive advantages such as shorter throughput time or customer orientation by means of product variety and high quality. Manufacturing strategy therefore becomes a crucial part in corporate strategy.

Such strategy reorientation and repositioning of the company in the marketplace will not be successful unless it is accompanied by a consistent personnel management. Unfortunately this is not always the case in practice. Most often, decisions on the installation of technical innovations are made without previously evaluating quantitative and qualitative consequences for the employees [3]. This is especially true for so-called production cells. This specific form of work organisation is more and more commonly used for flexible manufacturing in order to meet changing market conditions [2].

Production cells are characterized by the fact of putting together on one spot all components, machines and workers necessary for the manufacturing of one family of parts. The worker's job, besides the primary task of manufacturing the parts, equally contains work scheduling and time planning as well as quality control and quality assurance. One production cell usually consists of five to twelve men. Its efficient functioning depends on the versatility of its members, their motivation and their willingness to cooperate. Several production cells are directed by one single supervisor. Group-oriented work organisation calls for up-qualification of workers. Their flexible placement in production cells represents an excellent way of acquiring missing qualifications. Subsequently we will make the following assumptions, all based upon practical experience [3]:

\- Human resource structure is determined by equally qualified workers who may cross-substitute one another.

\- Up-qualification of the workers is necessary for production cell productivity.

\- Workers can be assigned to different workplaces and to different production cells.

\- Training within the scope of the group is favourable because of mutual assistance between workers and high self-determination of the production cell.

\- Flexible personnel assignment with changing tasks increases the worker's contentment and motivation.

As part of the process of increasing labour division more and more management tasks, especially in the field of personnel management, have been taken out of the supervisor's scope and assigned to higher management levels. Supervisors in their turn tend to compensate this loss of esteem by the illegal use of power which may prevent innovations from being implemented. Thus, redelegation of responsibility towards the supervisor level may have two positive aspects. On the one hand it may encourage a supervisor's acceptance of innovations, on the other hand it is supposed to make supervisors the organisational unit to implement personnel strategy on the shopfloor. A supervisor has to take care of the worker's daily problems and therefore represents an important intermediary in a personnel management system. Especially when working in production cells a supervisor often has to make personnel assignment decisions on the spot. According to his personal preference appraisal a supervisor will assign workers to production cells and thus determine manpower capacity for each production cell. Doing this, he has to take into account a certain absentism rate which ranges in average from five to ten per cent. In case that the manpower deficit is substantial, it is up to him to decide whether or not production cells are to be temporarily closed down and which ones this will be.

The importance of these decisions and the complexity of their determining factors will make a decision support system for prompt personnel assignment a useful instrument for supervisors. The typical decision problem may be characterized as follows: What is the optimal assignment of individual workers to certain groups (production cells) under the restrictions of specific qualifications, orders situation and absentism.

In the next chapter we will present some reflections on the architecture of such decision support systems.

## 3. The components of a decision support system for personnel assignment scheduling in production cell technology

In the last section we argued that the main components of our decision support system should be designed for the use on the hierarchy level of a supervisor. For a higher management level we will also develop some components which we will describe later.

Even today, the supervisors of a production cell dispose of a personal computer workstation which is connected to a mainframe and a printer [2].

The main components of the system will be realized on such a workstation, e.g. a PC with a graphics screen. We can profit from the fact that the PC's are linked to a Personnel information system. It would also be desirable to have an interface to a data base which contains the qualification and achievement profiles of the workers. These personnel data are converted into a format which is needed by our system.

We conclude that the technical requirements for an installation of our system are fulfilled in most production cell environments. The main components of the decision support system for the supervisor level and the tasks are as follows:

## 1. Staff attendance survey

\- An survey of reliable teams;

\- A graphics oriented representation of the qualification profiles of the workers.

## 2. Placement

\- A-priori assignment of workers or teams to certain production cells;

\- A-priori interdiction of assignments.

## 3. Generating feasibility

\- Assessment of the actual demand for workers per production cell;

\- Algorithms which compute a feasible personal assignment

or which indicate bottlenecks causing infeasibility;

\- Elimination of bottlenecks by closing certain production cells or by relaxing interdictions of assignments (by reactivating the placement component).

## 4. Optimization

\- Mathematical algorithms which compute an optimal personnel assignment;

\- Presentation of optimal solutions on a graphics screen or on a printer.

## 5. Analysis

\- Computation of alternative solutions by

![](/api/attachments/YQTZQ46J/fulltext/images/343eb3c522f36e47f1f38d096b3656c3fde2efa6ea6b01b4c52b93c23d4880af.jpg)  
Fig. 1

changing parameters;

\- Proposals of parameter changes;

\- Predictions of the solution efficiency in comparison with previous decisions.

## 6. Evaluation

\- Storing of decision parameters;

\- Storing of the efficiency obtained by the decision;

\- Statistical processing of the data;

\- Storing of the data in a statistical data base.

The interactions between the components are illustrated in Fig. 1. The arrows also represent the possible course of a session with the system.

The evaluation component is an interface to a higher level of decision makers.

On this level, a system will be developed which processes the data of the evaluation component. This system illustrates the qualification deficits which caused infeasibility and may initiate additional training programs.

Discrepancies between the results of the evaluation component and the original evaluation of the workers are analyzed in cooperation with the supervisors and lead to corrections in the evaluation of the workers qualification.

These corrections lead to a man-machine interaction which dynamically optimizes the data of the system. This process could be partially automated with methods of artificial intelligence. Such an enhancement of the system has not been planned so far, as we concentrate on the basic decision level. However, following the general concept of constructing decision support systems as pursued at the University of Passau, we plan to design our system in a way which allows the integration of AI-components (e.g. as described in [1]) at a later point.

We will now describe the components in a more detailed form. The optimization component which plays a central role in the system will be described in a separate section.

## Staff attendance survey

The direct interface to a Personnel information system provides fast access to the current list of present workers at the time of decision (e.g. at the beginning of a shift).

The workers present which are to be assigned to production cells are listed on the screen, reliable teams are graphically emphasized.

The qualification features of the workers can be directly accessed via a personnel data base (personnel information system), can be graphically represented and equipped with ranking orders. The qualification profiles of workers can be compared to the requested profiles of the production cells on the graphics screen (for example as overlayed curves). These screen representations have to be restricted to essential issues because we require decisions on the supervisor level to be made very fast.

## Placement

With special conditions in the production environment it will be necessary for the supervisors to fix or forbid assignments of workers or teams to certain production cells. This can be done using a 'mouse' on the screen provided by the staff attendance survey. Fixed or forbidden assignments are marked with arrows of different colors. As an additional decision aid further elements of the staff attendance survey can be shown in 'windows'.

After the use of the feasibility or analysis component, these fixed or forbidden assignments can be altered.

## Generation of feasibility

Based on the actual production goal the supervisor fixes the number of workers required for each production. This number may also be provided by an interface to an existing PPS-system. Using fast max-flow algorithms and the data provided by the placement component, the following is achieved:

(i) a feasible assignment is constructed or

(ii) those workers which cannot be assigned to a production cell and those production cells which cannot be optimally filled are identified.

In the first case, the optimization component is activated. In the second case, the supervisor can act as follows: Certain production cells can be closed down. This can be done with respect to a preference structure depending on the production goal (this structure can be extracted from a PPS-system).

Certain bottlenecks which cause infeasibility can be eliminated relaxing the decisions that were made in the placement phase.

In both cases there will be an interaction between the placement and the feasibility component until the existence of a feasible solution is guaranteed.

## Optimization

Based on mathematical assignment algorithms which are provided by an algorithm data base, one or several optimal assignments are computed and presented on the graphics screen or on the printer.

## Analysis

Based on the results of the optimization component the system proposes changes of parameters (e.g. capacities of production cells, relaxations of conditions fixed in the placement component)

![](/api/attachments/YQTZQ46J/fulltext/images/0bea1ec4228b35cc8ba63163a2fd85f9b6bbb2eb4ec79cf01d64cb32afbbba97.jpg)  
Fig. 2

which lead to significant improvements. These proposals are generated by reoptimization algorithms and parametric methods based on the algorithm in [7] and by branching heuristics. By the use of the placement component the suggested changes can be performed.

Independently, the supervisor can change parameters if he does not agree with the optimal solutions.

Based on the data of the statistical data base the efficiency (e.g. the output of each production cell) of the solutions can be predicted. This may lead to a change of assignments.

The decision is made after possibly several uses of the analysis component.

## Evaluation

After a decision has been made, the personal assignment is stored. Also the reasons which lead to the decision (absentisms, closing certain production cells, fixed assignments) are stored.

The efficiency of the solution is evaluated (e.g. after a shift) by the output of the production cells. These evaluation figures are stored, too.

The stored data are processed and integrated in the statistical data base. This data base can contain the following data which should be presentable in a user-friendly form:

\- How often does a worker cause infeasibility (qualification deficits)?

\- How do the assignments of workers and teams correlate with the output of the production cells?

\- How often does a production cell have to be closed down?

\- How do the qualification profiles of the workers correlate with the productivity of the production cells?

\- What is the average discrepancy between the qualification profiles of the workers and the required profiles of the production cells?

\- What is the degree of satisfaction of the workers with the assignments?

In Fig. 2 we present a sketch of the architecture of our system which describes the hardware components, the data accesses and system interfaces.

## 4. Optimizing personal assignments

The design of our system is basically deterministic.

However, we plan a future integration of stochastic concepts via Markov chains which take account of long-term effects (compare [8]).

The optimization component heavily depends on the definition of a reasonable function which quantifies the utility of a worker (or team) for each production cell. For this, several concepts are possible.

The utility can be defined by a simple ranking. However, this does not take account of the different components of the qualification profile. It is more common [2], [10], to associate with each worker a vector $q_{i}$ whose components are measures for certain qualification attributes. Analogously, for each production cell j a vector $d_{j}$ is defined whose components are corresponding measures for the required qualification attributes.

The use of the worker i for the production cell j is measured by a suitable vector norm $c_{ij}$ of the vector $q_{i}-d_{j}$ .

For example the euclidean or supremum norm could be chosen. The smaller the quantity $c_{ij}$ , the more useful will worker i be for production cell j. Of course, there will be qualification attributes that don't have a corresponding requirement attribute and vice versa. When computing $q_{i}-d_{j}$ , we really only consider the restriction of $q_{i}$ and $d_{j}$ to elements which are comparable. The structure of the profile vectors highly depends on the actual environment where the system is used. In general, the vectors $q_{i}$ and $d_{j}$ will be transformations of the existing qualification and requirement profiles. For example, the vector $d_{j}$ for a production cell can consist of all the requirement profiles for the single jobs that have to be performed on the cell. In this case, $q_{i}$ should consist of several identical copies of a qualification profile, one for each job.

This evaluation of the utility is a simplifying model, too, because the components of the qualification and required profiles are combined into one number. However, this model has proved useful in many models for manpower planning ([9], [10]) and it allows the use of linear assignment models. It reflects our flexibility requirement mentioned in section 2: the worker has to be able to perform different (ideally all) jobs within a production cell. Hence, we are mainly interested in the qualification of a worker for a cell rather than his qualification for a single job within the cell.

If all qualification and requirement profiles are taken into account we have a typical situation of multiattributive decision theory. We plan to experimentally integrate a multiattributive component into our system. For example programs like MAUD [4] or Prefcalc [5] could be useful for our purpose. However, such programs cause relatively long dialogues before an acceptable solution is found. This would have a bad effect on the acceptance of our system as it is designed for shortterm decisions. Nevertheless, for the planned system for a higher decision level multiattributive methods will be provided.

To take the multiattributive situation into account within a linear model the components of the vectors $q_{i}$ and $d_{j}$ can at least be equipped with weight factors [10]. For the normal use of our system we chose a flexible linear basic model which is based on the quantities $c_{ij}$ . It relies on the classical assignment or transportation model which has proved useful in many manpower planning applications. In most of these applications, optimal assignments of single persons to single jobs are computed with algorithms for the assignment problem. Or, in the case of assignments of single persons to groups, general transportation algorithms are used which are originally designed for assignments of group-members to groups. These latter algorithms are really unnecessarily general and hence too slow for our purpose.

We use an algorithm which we developed in [7] and which is tailored for our situation of assignments of single persons to groups.

So far, assignment algorithms in manpower planning have been used mainly for large-scale problems (e.g. in military applications [9]). In our situation the dimensions are much smaller (nevertheless the problems are quite complex) and the hierarchy level of the decision maker is lower.

Our basic linear model is as follows:

Let the workers be numbered by $i=1,\ldots,n$ , the production cells by $j=1,\ldots,m$ and let $c_{ij}$ denote the cost coefficients as defined above. Let $x_{ij}$ be 1 or 0 if the worker i is assigned to the production cell j or if he is not, respectively.

Let the numbers $b_{j}$ denote the number of workers required for production cells $j = 1, \ldots, m$ .

Under the assumption that each worker is assigned to exactly one production cell and that each production cell gets exactly the required amount of workers the model can be expressed as

follows:

Minimize $\sum_{i,j}c_{ij}x_{ij}$ , where

$$
\sum_ {j = 1} ^ {m} x _ {i j} = 1, i = 1, \dots , n,
$$

$$
\sum_ {i = 1} ^ {n} x _ {i j} = b _ {j}, j = 1, \dots , m, x _ {i j} \geqslant 0.
$$

This is a special case of the transportation problem, and it contains the classical assignment problem as a special case. For this problem we have developed a very efficient algorithm [7] whose advantages for the concept of our system will be described in the sequel.

\- The algorithm is a special dual simplex algorithm.

This fact allows its integration is more complex linear systems and a handling of additional constraints.

\- The algorithm admits an efficient parametric analysis.

This is useful for the applications in the analysis component, for changes of the production cell capacities and changes of the qualification profiles.

\- The algorithm terminates in time $O(mn^2)$ in the worst case and in time $O(mn \log n)$ in the average case.

These theoretical performance properties are the best which are currently known and they have been verified in various implementations. The codes compare favorably to other published codes [7].

Problems of the size required by our system are solved on 16-bit PC's in fractions of a second. For the same problems a commercial PC-code for transportation problems needs about 3 minutes. The speed of our algorithm is very important for the following reasons:

Fast algorithms improve the acceptance of the system when short-term decisions have to be made. Variants of the problem can be solved by enumerative methods. For example the assignments of reliable teams can all be compared by optimizing the remaining assignments with the basic algorithm.

Branch and bound methods are supported.

\- We have developed an even more efficient variant of the algorithm which takes advantage of sparsity of the matrix $c_{ij}$ . If only $k$ assignments are feasible the worst case running time of the algorithm is $O(nk + mn \log m)$ .

This is very important in our system, as we typically fix or forbid certain assignments (either a-priori or in the placement phase). For the treatment of absentism the variant can be used as well. Vacant positions can internally be represented by 'dummies'. If a production cell must be completely filled, this will be achieved by forbidding assignments of dummies to this cell.

Beside the basic algorithm, we will provide an algorithm bank which allows automatic changes of models if the situation is more complex. This corresponds to the concept pursued at the University of Passau, namely that model-management should have a central function in decision support systems (compare [6]).

If many additional constraints have to be taken into account, LP-algorithms or non-linear optimization algorithms provided by the algorithm bank have to be used. If there are many incompatible assignments, linear complementarity algorithms are necessary. As mentioned before, multi-attributive methods shall only be provided for the higher decision level.

We will, however, pursue the general strategy to use the basic algorithm most of the time, perhaps also in enumerative applications, because it is tailored for the general problem and so fast that its running time is much smaller than the loading time for more complicated optimization software.

## 5. References

[1] R. Bardens, D. Karagiannis: Knowledge-based manpower planning, Annals of Operations Research, forthcoming.

[2] R. Bühner: Betriebswirtschaftliche Organisationslehre, Oldenbourg Verlag, München, Wien, 1986.

[3] R. Bühner: Strategisches Personalmanagement für neue Produktionstechnologien, Betriebswirtschaftliche Forschung and Praxis, Heft 3/1987.

[4] P.C. Humphreys, A. Wisuda: MAUD 4, Technical Report 83-5, Decision analysis unit, London School of Economics and Political Science, 83 (1983) 5.

[5] E. Jaquet-Lagreze, J. Siskos: Assessing a set of additive utility functions for multicriteria decision making – the UTA method, European J. Operational Res. 10 (2) 1982.

[6] M. Jarke: Kopplung qualitativer und quantitativer Theorien in der Entscheidungsunterstützung, Proceedings des 2. Internationalen GI-Kongresses '87 Wissensbasierte Systeme, München 1987.

[7] P. Kleinschmidt, C.W. Lee, H. Schannath: Transportation problems which can be solved by the use of Hirsch-paths for the dual problems, Mathematical Programming 27 (1987), 153–168.

[8] C.J. Verhoeven, J. Wessels, J. Wijngaard: Computer-aided design of manpower policies, Manpower Planning Reports 16, Technological University Eindhoven, 1979.

[9] G.A. Zölzer: On the application of analytic models in personnel planning in the Bundeswehr, in: Manpower planning and organization design, Proceedings of the NATO conference on manpower planning and organization design at Stresa 1977 (D.T. Bryant, R.J. Niehaus, eds.) 1977.

[10] G. Zülch: Verallgemeinerung and Lösung de Zuordnungsproblems von Hildebrandt, in: Arbeitsorganisation und neue Technologien, hrsg. von R. Hackstein, F.-J. Herg, F. von Below, Springer Verlag, Berlin etc. 1986, 695–718.
