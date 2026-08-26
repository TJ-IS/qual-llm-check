---
otero_id: 18035
otero_key: "X62EPTFE"
title: "Functional requirements for the development and use of a software-cost database"
authors: "G.J. Dekker; F.J. van den Bosch"
year: "1983"
journal: "Information & Management"
doi: "10.1016/0378-7206(83)90009-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Functional Requirements for the Development and Use of a Software-Cost Database \*

G.J. Dekker and F.J. van den Bosch
National Aerospace Laboratory NLR, P.O. Box 90502, 1006 BM
Amsterdam, The Netherlands

Cost estimation of software development and control of the cost during the development are difficult, due to a lack of useful cost history figures. This paper describes the results of the first phase of a study to develop a software-cost database. This database will be used to develop an accurate cost estimation method and to support cost management. The study has been performed for the Netherlands Agency for Aerospace Programs (NIVR). The database is in use since the end of 1982. During the first phase, a literature survey, together with experience available at NLR, has led to a proposal for a cost estimation method based on 8 classes with in total 47 well-defined cost factors. The clear definition of these cost factors is important for the effective use of the method.

Keywords: Computer systems programs; cost control; cost estimates; design-to-cost; life cycle costing; software development.

![](/api/attachments/X62EPTFE/fulltext/images/414c358c94a2219a11d95cff504268e6d0fef09ce161c762979c8bcb9d19da91.jpg)

Geert Jan Dekker is a research engineer at the National Aerospace Laboratory NLR (Amsterdam, the Netherlands). He graduated in 1974 in applied mathematics and physics at the Utrecht University. As principal analyst, he has contributed to several medium and large scientific/technical information processing systems. His current research interests are software engineering, with emphasis on cost control and quality assurance.

## 1. Introduction

The management of software development faces two problems: cost estimation and cost control. Cost estimation occurs before a software project is started, when either the cost of the project must be estimated from the project description (Life Cycle Costing) or the scope of the project must be determined, given the available project budget (Design-to-Cost).

Cost control occurs during the project and includes monitoring the effort and making corrections when deviations from the plan are observed.

In spite of the enormous investment in software today, it is generally impossible to give realistic cost estimates, let alone control the development cost effectively. Two reasons can be identified [18]:

1. Not enough qualitative and quantitative information is available about the cost estimation process.

2. Virtually no cost figures are available from previous projects.

There is a clear need for a software-cost database, containing clearly defined cost data from actual projects, together with cost factors, such as application field, techniques and terminology used, and changes during the project life cycle [15].

![](/api/attachments/X62EPTFE/fulltext/images/38093aece11bf50f41cdc580beac328584e2ed1688550e58c6fda3144aaccae6.jpg)  
Frank J. van den Bosch is a research engineer at the National Aerospace Laboratory NLR (Amsterdam, the Netherlands). He graduated in numerical mathematics at the University of Amsterdam. As senior system designer he has contributed to various medium and large scientific/technical information processing systems. His current research interests are directed towards the application of data communication, and computers in an organization.

This article presents the results of the first phase of a study to define and implement such a database regarding aerospace projects. An overview is given of available cost estimation methods (section 2) and sources of cost data (section 3). The estimation methods are evaluated with respect to their use for Life Cycle Costing, Design-to-Cost and Cost Control and an optimum combination is proposed (section 4). The contents of the cost database are then specified in such a way that the proposed cost estimation method can be calibrated with the collected data (section 5). Finally the current status of the study is given, together with the plans for the use of the already developed cost database system.

## 2. An Overview of Cost Estimation Techniques

A survey of the literature reveals a large number of different cost estimation methods [1,4,10,17]. There are, however, three basic techniques that we term: (1) the analogy technique; (2) the parametric technique; and (3) the decomposition technique (Fig. 1). All known methods can be shown to be a combination of these three or a variant of one of them.

![](/api/attachments/X62EPTFE/fulltext/images/03c4b1757f676d58aa10a3007f7368c80fd3ed82f0a2e1fc0a7510ac5f472900.jpg)  
Fig 1 Cost Estimation Techniques.

## 2.1. The Analogy Technique

For the analogy technique the estimator relies on the cost of similar systems or compares large modules with similar modules from previous projects. The cost of these projects are stored in a kind of database (most of the time in the brains of the estimator). Adjustments are made for differences between modules and between development methods. However, it is difficult to estimate the effect of certain differences; e.g., a faster response time. The accuracy of this technique is thus highly dependent of the estimators' ability and experience.

## 2.2. The Parametric Technique

For the parametric technique the estimator has to characterize the new project by a number of figures, such as the estimated number of lines of code; the complexity of the project; the experience of the developers; etc. The cost of the project is obtained by feeding these figures into some formula, which is based on the cost data of previous projects. Examples of methods using this technique are the COCOMO method [4], the SLIM method [19], the PRICE-S method [11] and the TRW SCEP method [5]. A closer look at the various parametric methods reveals a number of problems.

First of all, there is no “best” formula relating the size of a project to the necessary effort. Two basic formulae are:

$$
\mathbf {M M} = a I + b,\tag{1}
$$

$$
\mathbf {M M} = c I ^ {d},\tag{2}
$$

where

MM = number of manmonths of effort needed.
I = number of thousands of statements.

a, b, c and d are constants, depending on the type and/or difficulty of the software.

Formula (1) assumes that the cost per instruction is independent of the size of the project, where formula (2) assumes the contrary.

If $d < 1.0$ in (2), single instructions become cheaper as the projects becomes larger; i.e. “economies of scale” are assumed to apply. The case where d > 1.0 expresses the opinion that larger projects have more internal interfaces and thus need more communication between the designers, making single instructions more expensive [6]. Values for d have been reported from 0.404 [14] to 1.83 [20], but most of them are close to 1 [4].

Secondly, the definitions of the terms used are often vague, or not given at all. For instance, it is almost never stated whether the number of statements should include comment lines, not-delivered test statements, data areas, etc., or not. This makes an accurate application of the formulae difficult.

Finally, the data samples on which the various formulae are based are always too small to gain statistical significance. It is therefore not surprising that it can be shown that none of the published parametric methods is reliable when applied on actual data [17].

## 2.3. The Decomposition Technique

In the decomposition technique, the total project is broken into small jobs which allow a reasonably reliable estimate. Each job in the so obtained Work Breakdown Structure (WBS) should take about one manmonth. In order to decompose the project, the estimator must have a deep insight into the project. In fact, the WBS should contain a good part of the design; but the preparation of the design takes approximately 40% of the total cost. Also, the integration effort may be costly and difficult to estimate.

## 3. An Inventory of Cost Databases

All estimation methods rely upon data gathered in previous projects. However, such data is scarcely available, probably because cost figures are company-confidential. Furthermore, the collection of detailed project information is most of the time for accounting purposes only and accounting data is not sufficient for cost estimation purposes [18]. A survey of the literature reveals the following cost databases:

Wolverton [22] describes a TRW in-house cost database. He has presented results in scatter diagrams, but only relative data is given.

Black [3] used experimental cost data to derive a cost estimation method, but the data are not published.

Putnam [19] claims that his method compares very well with data from 50 projects of the U.S. Army Computer System Command. He does not publish this data.

Graver [12] mentions the existence of an automated system (PARMIS) within the Air Force Data Systems Design Center. This contains figures from over 2000 projects. However, no software characteristics are available and most of the projects are business oriented. Herd [13] mentions this database but regards it as unreliable (over 85% of the included projects did not exceed budget estimates and there is no indication whether a project was completed or not when the actual costs were less than half those anticipated).

Walston and Felix [21] present the results of analysis of 60 completed projects at IBM: they present only scatter diagrams and summaries.

Herd [13] uses a published database from SDC (the System Development Corporation). This database contains 169 projects, and data is recorded on 94 variables per project. However, this data was published in 1966, and cannot be regarded as up-to-date.

The Rome Air Development Center of the U.S. Air Force operates the "Data and Analysis Center for Software, DACS". One of the functions of DACS is to collect software cost data for general research [9]. However, their data is not made available outside the U.S.

Some data from 18 NASA projects can be found in [2]. The size of these projects is expressed in lines of High Order code, inclusive comments.

Recently, data from 63 projects, including 23 cost factors per project was published by Boehm [4]. This dataset is the most complete, freely accessible database today.

Thus, except for Boehm's data, the data is generally vague, unreliable, or very old. Furthermore, the published data has often been collected after completion of the projects, and not during them [18], relying on human memory.

## 4. Proposal for a Cost Estimation Method

The main requirement for a software-cost database is that its contents can be used for the calibration of a cost estimation and control method. Thus, before these contents can be specified, it is necessary to define this method. A useful cost estimation method has to support both life cycle costing and design-to-cost. The latter becomes more and more important due to the ever continuing increase of software cost.

This section presents an evaluation of the techniques, described in section 2 with respect to their applicability for: life cycle costing, design-to-cost and cost control. This evaluation leads to a combination of the technique, which promises to be the best applicable.

## 4.1. Evaluation of Cost Estimation Techniques

All three techniques are of value for life cycle costing. The analogy technique and the decomposition technique supply cost figures directly from the specifications. They do not account automatically for the used production process; this is, however, a significant cost factor [13]. The parametric technique makes restrictive use of analogy and decomposition when the size of the software is to be estimated. It accounts separately for the production process. Thus, the parametric technique is conceptually better for the estimation of the life cycle costs. However, today there is no accurate software estimation formula. Most of the formulae have not been validated in current or new projects [14,17]. Thus the results of a parametric method must be scrutinized by an experienced estimator and compared to costs that have been estimated with other methods.

Design-to-cost implies a funding limit and that the scope of the project should be adapted down to this [13]. This involves a trade-off between software and hardware costs. Normally, this is an iterative process in which ever more functions or constraints are removed until the estimated costs are at or below the maximum. At each step, the designer needs a quick way to obtain an accurate estimate and an indication of the cost impact of each function or constraint.

For the analogy technique it must be expected that the projects used for the estimation process differ significantly from the project under consideration. This is particularly true of aerospace and other scientific projects. The sensitivity of the analogy technique to changes in the specifications makes it inaccurate for the design-to-cost process.

The decomposition technique can only be used for design-to-cost if complete functions or modules can be removed. The effects of removal or relaxation of overall design constraints, such as portability or testing requirements, can not be estimated effectively with this technique.

The parametric technique is suitable for design-to-cost, if the adaptation of the requirements is a removal, or relaxation, of design constraints, and if these constraints are separately estimated cost factors. It is even possible to estimate the relative impact of these factors individually by computing the gradient of the cost estimation formula. Thus, the designer can concentrate his attention on those constraints which have the most impact. On the other hand, it is not possible to see the effect of removing complete functions from the system. This can only be estimated when the impact of these functions on the system's size can be estimated.

![](/api/attachments/X62EPTFE/fulltext/images/63a5b3b809d2ec3d0f290adb1c09874405951ab936ffc1d1fb77fcf31c8f907f.jpg)  
Fig. 2. Software development Phases and their Products.

It appears that a combination of the decomposition technique (to obtain the estimated size of the system) and the parametric technique promises to be the best approach for design-to-cost. Analogy can be used for the estimation of the size of individual software modules.

In order to control the cost, the costs must be allocated to the different phases of the life cycle. Each phase ends with delivery of some products, see Fig. 2. Furthermore, the plan must be updated when the project requirements or its environment change. Then the project manager is able to monitor the effort and take corrective action in time, by early detecting a possible cost overrun.

All three techniques allow cost allocation to the phases of a project. However, the analogy technique is not well suited to estimate changes in environment and requirements, and thus should not be used here. The same is true for the decomposition technique, because its plan consists of a summation of estimates of parts; thus if the overall constraints change (e.g., a larger part of the system is to use interactive I/O processing), it will be difficult to update the plan; all jobs will have to be re-estimated. With the parametric technique it is relatively simple to update the plan to incorporate changes. The changes must be translated to changes in the related parameters, after which a new cost estimate can be obtained.

## 4.2. Proposed Cost Estimation and Control Method

It can be concluded that no single cost estimation technique can be reliably used in all three areas. However, a combination can support all of them. The proposed method uses decomposition of the software and analogy to obtain an estimate of only the size of the delivered code, and this will be one of the parameters for the cost estimation formulae. Such a combination is useful in the estimation of the life cycle costs of a software product. It can be extended to design-to-cost if the decomposition takes place to the level of independent functions or modules, and if the parametric formulae contain sufficient independent cost factors. In order to be suitable for cost control, the method must give separate independent cost figures for each project phase. Furthermore, sufficient independent cost factors must be included in the parametric formulae in order to accommodate change during the project.

Both design-to-cost and cost control dictate that a large number of cost factors should be included. However, it is not feasible to estimate detailed project factors when an initial estimate of the life cycle costs is to be made. Therefore, the cost factors have been classified into a small number of groups, each of which corresponds to one main cost factor. In this way, it will be possible to estimate the main factors when little detailed information about the project is available and to improve these estimates when more detailed information becomes available.

The proposed method consists of two sets of formulae. The first set relates 8 main cost factors with a total of 47 subfactors (see Fig. 3):

$$
F _ {j} = h _ {j} \left(b _ {j 1} f _ {j 1}, \dots , b _ {j k} f _ {j k}\right),\tag{3}
$$

where:

$$
F _ {j} = \text { main   factor } j (j = 1, \dots , 8),
$$

$h_{j} = \text{a function to relate } F_{j}$ with its subfactors $f_{jk}$ ,

$$
b _ {j k} = \text { weight   for   subfactor } f _ {j k},
$$

$f_{jk} = \text{subfactor } k \text{ of main factor } F_j$ . (The number of subfactors varies with $j$ ).

An explanation of the factors and their subfactors is given in section 5.

The functions $h_{j}( )$ and the weight factors $b_{jk}$ have to be determined from experience and the literature.

The second set of formulae relates the main cost factors to the cost of each phase:

$$
\begin{array}{l} \text { Cost } _ {i} = C _ {i} (a _ {1} F _ {1}, \dots , a _ {j} F _ {j}), \\ \text { where } \\ \text { Cost } _ {i} = \text { project   cost   in   phase } i, \\ C _ {i} = \text { a   function   to   relate   Cost } _ {i} \text { with   the   main } \\ \text { factors } F _ {j}, \\ a _ {j} = \text { weight   for   main   factor } F _ {j}, \end{array} \tag {4}
$$

![](/api/attachments/X62EPTFE/fulltext/images/84f680a97a8d8adf52c0a6f038179bc87d779c9a8864c91126532ca726063a61.jpg)  
Fig. 3. Classification of Cost Factors.

$F_{j} = \text{main factor } j.$

The function C, must be derived from theoretical considerations, and the weight factors a, must be estimated from data of completed projects.

## 5. Contents of the Cost Database

In Table 1, the 47 cost factors are listed together with an indication when they can be obtained during the life cycle of a software project. A detailed definition, together with a description of their possible influence on development cost can be found in [7].

The cost factors have been structured into 8 groups:

1. Project size (work to be done).

2. Project difficulty (unique project conditions).

3. Reliability requirements (leading to more testing, etc.).

Table 1
Cost factors per project phase

<table><tr><td rowspan="2">Cost factor</td><td colspan="7">Registration after phase (see fig. 2)</td></tr><tr><td>Prel. stud.</td><td>Conc. phase</td><td>Defi-nition</td><td>Det. Design</td><td>Impl.</td><td>Integr. &amp; Valid.</td><td>Ops. &amp; maint.</td></tr><tr><td>1 Project size</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Number of input message types</td><td></td><td></td><td></td><td></td><td></td><td>×</td><td></td></tr><tr><td>Number of output message types</td><td></td><td></td><td></td><td></td><td></td><td>×</td><td></td></tr><tr><td>Number of data elements</td><td></td><td></td><td></td><td></td><td></td><td>×</td><td></td></tr><tr><td>Number of words in the database</td><td></td><td></td><td></td><td></td><td></td><td>×</td><td></td></tr><tr><td>Number of product/project pages</td><td></td><td></td><td></td><td></td><td></td><td>×</td><td></td></tr><tr><td>Number of delivered statements</td><td></td><td></td><td></td><td></td><td></td><td>×</td><td></td></tr><tr><td>2 Project difficulty</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Quality of requirements</td><td></td><td></td><td>×</td><td>×</td><td>×</td><td>×</td><td></td></tr><tr><td>Frequency of change of requirements</td><td></td><td></td><td>×</td><td>×</td><td>×</td><td>×</td><td></td></tr><tr><td>Acquisition of hardware and software packages</td><td></td><td></td><td>×</td><td></td><td></td><td></td><td></td></tr><tr><td>Concurrent development of hardware</td><td></td><td></td><td></td><td>×</td><td></td><td></td><td></td></tr><tr><td>Overdue time at which the hardware and system software is specified</td><td></td><td></td><td></td><td>×</td><td></td><td></td><td></td></tr><tr><td>Overdue time at which the hardware and system software is available</td><td></td><td></td><td></td><td></td><td>×</td><td></td><td></td></tr><tr><td>Language requirements</td><td></td><td>×</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Security requirements</td><td></td><td>×</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Development schedule</td><td></td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td></td></tr><tr><td>Number of personnel involved in development</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td></td></tr><tr><td>Personnel turnover rate</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td></td></tr><tr><td>Participation of programming organization in the conceptual phase</td><td></td><td></td><td>×</td><td>×</td><td>×</td><td>×</td><td></td></tr><tr><td>3 Project reliability requirements</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Required reliability</td><td></td><td>&lt;</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Testing, verification and validation requirements</td><td></td><td>×</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Portability</td><td></td><td>×</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Maintenance and change requirements</td><td></td><td>×</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Multiple software utilization sites</td><td></td><td>×</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Resilience</td><td></td><td>×</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4 Utilization</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Time constraints</td><td></td><td></td><td></td><td></td><td>×</td><td></td><td></td></tr><tr><td>Memory constraints</td><td></td><td></td><td></td><td></td><td>×</td><td></td><td></td></tr><tr><td>5 Percentage of new design and code use of existing documentation</td><td></td><td></td><td></td><td>×</td><td></td><td></td><td></td></tr><tr><td>Use of existing software</td><td></td><td></td><td></td><td></td><td>×</td><td></td><td></td></tr><tr><td>6 Development environment</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Communications with the purchaser</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td></td></tr><tr><td>Average turn-around time of the development computer</td><td></td><td></td><td></td><td></td><td>×</td><td></td><td></td></tr><tr><td>Timesharing versus batch</td><td></td><td></td><td></td><td>×</td><td></td><td></td><td></td></tr><tr><td>Programmer access to computer</td><td></td><td></td><td></td><td>×</td><td></td><td></td><td></td></tr><tr><td>Difference between the development computer and the target computer</td><td></td><td></td><td></td><td></td><td>×</td><td></td><td></td></tr><tr><td>Number of development locations</td><td></td><td>×</td><td></td><td></td><td>×</td><td></td><td></td></tr><tr><td>Available tools and their use</td><td></td><td></td><td></td><td></td><td>×</td><td></td><td></td></tr><tr><td>Reliability of the development computer and its software</td><td></td><td></td><td></td><td></td><td>×</td><td></td><td></td></tr><tr><td>Travel requirements</td><td></td><td></td><td></td><td></td><td></td><td>×</td><td></td></tr><tr><td>Use of modern programming and design techniques</td><td></td><td></td><td></td><td></td><td>×</td><td></td><td></td></tr><tr><td>7. Application</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Routine mix</td><td></td><td></td><td></td><td></td><td></td><td>×</td><td></td></tr><tr><td>8. Resources</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Purchaser experience with electronic data processing</td><td>×</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Experience with the used language</td><td></td><td></td><td></td><td>×</td><td></td><td></td><td></td></tr><tr><td>Experience with application</td><td>×</td><td>×</td><td>×</td><td>×</td><td></td><td></td><td></td></tr><tr><td>Experience with hardware and system software</td><td></td><td></td><td></td><td>×</td><td></td><td></td><td></td></tr><tr><td>Experience with peripherals</td><td></td><td></td><td></td><td>×</td><td>×</td><td></td><td></td></tr><tr><td>Overall experience</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td></td></tr><tr><td>Man-hours per personnel category</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>Secondary resources</td><td></td><td></td><td></td><td></td><td></td><td>×</td><td></td></tr></table>

4. Utilization (load conditions relative to the hardware).

5. Percentage of new design and code (existing software that can be re-used).

6. Development environment (and productivity considerations).

7. Application (the degree of complexity of the product).

8. Resources (experience, skills, know-how, and costs of the software staff).

Next, a subset of cost factors has been selected for each group and the cost factors have been defined so that:

\- the selected cost factors are distinct;

\- the set of cost factors is complete;

\- each factor is unambiguously measurable.

Having defined the cost factors, the database can be built. Using the collected data it will be possible to estimate the weight factors using an estimation technique. However, estimating the weight of 47 factors requires a substantial volume of data, therefore the weight factors $b_{jk}$ will initially be based on literature and prior experience. Using these weight factors a measure for the “weight” ( $F_{j}$ ) of each group is found. The weight factors for the eight groups ( $a_{j}$ ) must then be estimated from the collected data.

## 6. Current status and Future Work

In the first phase of the study (described here) we found a lack of sufficient readily available, and interpretable cost data. Furthermore, we have defined the contents of a software-cost database which can be used for the calibration of a generally applicable cost estimation method.

Our next activities have been the development of a data collection system, including cost reporting forms and procedures; and the technical implementation of the database. A description of these activities will be published soon [8].

Currently, the database is in use as a cost control tool for running projects. It is available for use by other parties performing technical/scientific software development.

Our future plans involve the gathering of as much as possible cost data from actual projects. The data will first be used for an evaluation of existing parametric methods. When sufficient data has been gathered our proposed estimation method will be calibrated using this data. In order to provide this method as soon as possible, most of its weight factors will be generated using the literature and our experience. These provisional weight factors will be improved when more data becomes available.

## References

[1] JD Aron. Estimating Resources for Large Programming Systems, FSC-69-5013 (IBM-FSC, Gaithersburg, MD, 1969)

[2] J.W. Bailey and V.R. Basih, A meta-model for software development resource expenditures, in Proceedings, Fifth International Conference on Software Engineering (IEEE/ACM/NBS, 1981) 107-116.

[3] R K E. Black c.s., B.C.S. Software Production Data, RADC-TR-77-116 (Boeing Computer Services, Inc., 1977) NTIS No. AD-A039852.

[4] B.W. Boehm, Software Engineering Economics (Prentice Hall, Inc., Englewood Cliffs, New Jersey, 1981).

[5] B W Boehm and R.W. Wolverton, Software Cost Modelling: Some Lessons Learned, Journal of Systems and Software, 1 (1980) 195–201.

[6] F P. Brooks Jr., The mythical man-month, Datamation 20 (1974) 44-52.

[7] G J Dekker, M v.d. Wilt and F.J. v.d. Bosch, Functional requirements for a software cost database, NLR TR 81017 (National Aerospace Laboratory NLR, Amsterdam, 1981).

GJ Dekker. A software cost database for the develop-

ment of aerospace software, in: E.A. Warman, ed., Proceedings of the First International Conference on Computer Applications in Production and Engineering, CAPE'83 (North-Holland Publ. Cy., Amsterdam, 1983; ISBN: 0-444-86614-0).

[9] L.M. Duvall, S.A. Gloss-Soler and J. Martens, Data and Analysis Center for Software, RADC-TR-80-204 (IIT Research Inst., Rome, NY, 1980).

[10] M.C. Finfer and R.K. Mish, Software Acquisition Management Guidebook: Software Cost Estimation and Management, SDC-TM-5772/007/02 (System Development Corp., Santa Monica, Calif., 1978).

[11] F.R. Freiman and R.E. Park, PRICE Software Cost Model, in: Proceedings of the National Conference on Aerospace and Electronics, NAECON'79 (IEEE, 1979) 280–288.

[12] C.A. Graver, c.s., Cost Reporting Elements and Activity Trade-offs for Defense System Software, Vol. 2: Executive Summary, ESD-TR-77-262-Vol. 2 (General Research Corp., Santa Barbara, Calif., 1977).

[13] J.R. Herd, c.s., Software Cost Estimation Study, Vol. 1: Study Results, RADC-TR-77-220 (Doty Associates, Inc., Rockville, MD, 1977).

[14] T.G. James, Jr., Software Cost Estimating Methodology, in: Proceedings of the National Conference on Aerospace and Electronics, NAECON'77 (IEEE, 1977) 22–28.

[15] D.R. Jeffrey and I. Vessey, Models, Metrics, and Management of IS Development, Information & Management 3 (1980) 89–93.

[16] W. Meyers, A Statistical Approach to Scheduling Software Development, Computer, 11 (1978) 23–35.

[17] S.N. Mohanti, Software Cost Estimation: Present and Future, Software-Practice and Experience 11 (1981) 103–121.

[18] U. Posthuma de Boer, Cost Estimation and Management Control of Software Development in Scientific/Technical Projects, NLR TR 78056 U (National Aerospace Laboratory NLR, Amsterdam, 1978).

[19] L.H. Putnam, A General Empirical Solution to the Macro Software Sizing and Estimating Problem, IEEE Tr. on Software Eng., SE-4 (1978) 345–361.

[20] V. Schneider, Prediction of Software Effort and Project Duration: Four New Formulas, ACM SIGPLAN notes 13 (1978) 49–59.

[21] C.E. Walston and C.P. Felix, A Method of Programming Measurement and Estimation, IBM Syst. J. 16 (1977) 54–73.

[22] R.W. Wolverton, The Cost of Developing Large-Scale Software, IEEE Trans. on Computers C-23 (1974) 615–636.
