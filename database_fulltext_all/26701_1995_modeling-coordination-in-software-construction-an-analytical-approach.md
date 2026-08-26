---
otero_id: 26701
otero_key: "97WTVHTU"
title: "Modeling Coordination in Software Construction: An Analytical Approach"
authors: "Murlidhar V. Koushik; Vijay S. Mookerjee"
year: "1995"
journal: "Information Systems Research"
doi: "10.1287/isre.6.3.220"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## H4R

![](/api/attachments/97WTVHTU/fulltext/images/d204a9868c763f21d54ab6af5b42039e8e5178da10a6d2676c3897518160a0c0.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Modeling Coordination in Software Construction: An Analytical Approach

Murlidhar V. Koushik, Vijay S. Mookerjee,

## To cite this article:

Murlidhar V. Koushik, Vijay S. Mookerjee, (1995) Modeling Coordination in Software Construction: An Analytical Approach. Information Systems Research 6(3):220-254. http://dx.doi.org/10.1287/isre.6.3.220

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1995 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/97WTVHTU/fulltext/images/f1830f603243dbce40827d2d466aac0aee235fa4a938bffebc9d0635f7ace43e.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Modeling Coordination in Software Construction: An Analytical Approach

Murlidhar V. Koushik

Department of Management Science, DJ-10

School of Business Administration

University of Washington

Seattle, Washington 98195

Vijay S. Mookerjee

Department of Management Science, DJ-10

School of Business Administration

University of Washington

Seattle, Washington 98195

Software development projects are typically team efforts, wherein groups of specialists work toward the common goal of building a software system. The individual efforts of team members need to be coordinated to ensure product quality and effectiveness of the team. In this paper we model the process of coordination in the construction phase of incrementally developed, modular software systems. The analytical model proposed here supports macro-level decisions regarding the development team size and the coordination policy, based upon micro-level interactions between the modules in a system. The objective in this model is to minimize the effort spent on coordination activities subject to the requirement that the system must be completed within a specified period.

Results from the model are used to examine coordination related trade-offs. We show that: (1) more complex systems need a higher level of coordination than simpler ones, (2) if the time available for construction reduces, it is optimal to reduce the level of coordination, and (3) marginal productive output is a diminishing function of team size. The sensitivity of the analytical model with respect to its assumptions is studied by constructing a set of simulation experiments where these assumptions are relaxed. The results of these experiments provide support in establishing the robustness of the analytical model.

Software construction—Economic model—Tradeoffs-Coordination policy--Team size

## 1. Introduction

oftware systems are among the most complex artifacts produced by humans. This Dcomplexity arises not only due to the inherent complexities of the product, but also due to the difficulties in managing the software development process. The team responsible for software development has the complex task of developing and integrating the various system components from specification to acceptance testing Since there are typically many system components and developers, coordination is required during all phases of the software project. Here we focus on the coordination effort required during the construction phase of a software system.

Software systems are often constructed incrementally. Functionality is added to the components of an existing system, the components are assembled and tested, and if found consistent, a working configuration of the system is produced. This cycle of adding functionality, integrating the system components, and producing a working configuration may repeat several times before the final system is released. Software construction can be conceptually viewed as repeated occurrences of a sequence consisting of a development phase and a coordination phase. The development phase involves effort needed to enhance and test system modules. The coordination phase consists of activities necessary to remove intermodule inconsistencies that may have arisen during the development phase.

Software project managers are typically faced with the problem of choosing the best approach to coordinate the efforts of the construction team. A key concern is to construct the system at minimum cost without sacrificing the quality and consistency of the product, and also meeting the project schedule. The cost of constructing a system is the sum of the development and coordination costs incurred in the period used for constructing the system. These costs depend on a variety of factors including the functionalities required of the system, the development environment being used, the complexity of the system modules, the size and structure of the software team, and the coordination policy.

We develop a model that highlights the economic aspects of team coordination during the construction phase of incrementally built software projects. The following setting characterizes the essentials of the construction process:

1. The system to be constructed consists of a set of modules (programs, objects, or functions) described by design specifications. Module specifications are assigned to a development team for coding, unit testing and integration. Each module is the responsibility of exactly one developer.

2. Individual developers add functionality to their modules through coding and unit testing. A module is released when enough functional elements have been added

3. After some number of modules have been released, the project manager schedules a coordination phase to identify and remove inconsistencies between modules in the system. After this phase is completed, further development of the modules resumes as in (2) above.

Given the above setting, our objective is to minimize the coordination effort subject to the constraint that the system is constructed in a specified time. A key decision variable affecting coordination effort is the coordination policy. A coordination policy is operationalized as the number of modules that must be released before a coordi nation phase is initiated. Performing coordination when only a few modules have been released can be costly and disruptive to the flow of individual effort. On the other hand, allowing the development phase to extend beyond a point may be undesirable since modules could have drifted too far apart and the resulting coordination costs in this state could be very high. The size of the construction team is another important decision variable. As team size increases, more coordination effort is required. Thus, the size of the team should be chosen as the smallest value necessary to construct the system without exceeding the time available.

The most novel aspect of this study is that it emphasizes a quantitative approach to modeling the coordination problem. The analytical model helps us to understand several important phenomena that have hitherto only been empirically observed. It shows that more complex systems optimally require a higher level of coordination than simpler systems.¹ The model also enables us to conclude that if the time available for software construction decreases, the level of coordination should also be decreased. Results from the model also appear to support a widely held observation in the field: adding more members to late projects makes them later, the so-called Brook's law (Brooks 1982). We present and discuss these and other findings in the context of a variety of software projects and compare our results with previously reported research.

We present references from two cases of large software development projects that highlight both the importance and the difficulty of coordinating large software projects. These cases have helped motivate this study.

The first case is the OS/360 system software project undertaken by IBM in the 1970s (Belady and Lehman 1976). In the classic work by Brooks (1982), the author describes the coordination problem in this project as that of “quantizing updates," and notes that:

Each team building another component has been using the most recent tested version of the integrated system as a test bed for debugging its piece. Their work will be set back by having that test bed change under them. Of course it must. But the changes need to be quantized. Then each user has periods of productive stability, interrupted by bursts of test bed change This seems to be much less disruptive than a constant rippling and trembling." (Page 1 50)

More recently, Zachary (1993) describes the coordination agonies of releasing Microsoft's new product, Windows NT. Zachary (1993) notes that:

In most software-development programs, the various pieces under development are stitched together only once in a while. By contrast, [management] insisted on a fresh build practically every day, meaning that each piece of NT, some containıng hundreds of changes, had to be reassembled into a whole, which was then subjected to a new round of testing. This scramble for a fresh build led to more skirmishes, these pitting programmers against builders. (Wall Street Journal, Page A6, May 26, 1993)

The rest of this paper is organized as follows. In §2, we briefly review background literature that addresses coordination related problems. In §3, we describe an abstraction of the software construction process and develop the analytical model. This model is based on the concepts of pairwise coefficient of interaction and connectivity between system modules. We introduce and describe these concepts here. In §4, we present numerical and qualitative results. In §5, we report on a set of experiments carried out to examine the sensitivity and robustness of the analytical model. Section 6 summarizes and concludes the paper.

## 2. Coordination in Software Projects

Software development costs have been estimated to account for a large portion of the total cost of a system. Hence many approaches have sought to improve various performance criteria through efficient management of the development process. Improved coordination has appeared as a common thread in the literature on software development. Here, we restrict our attention to literature that has emphasized coordination during system construction, namely, (i) team structure and size effects, (ii) system testing and integration strategies, and (ii) development environments.

There is general agreement that team size and structure could influence coordination costs during system construction (Safoutin and Thurston 1993, Tamai 1992). The team approach and the chief programmer team approach (Baker 1972) are typical of the methods that emphasize structural aspects of the software team. Swanson and Beath (1990) examine departmentalization of the software maintenance function. While recommending a separate department for maintenance, they recognize that this may lead to increased coordination costs between the development and the maintenance staffs.

Other researchers have emphasized structural aspects of the software system (Brooks 1982, Parnas 1972, Paulson and Wand 1992). These studies have focused on the role of modularization in system construction, especially its impact on the cost and complexity of construction. Research in this area has also attempted to identify software structures that could reduce the effort needed to resolve intermodule inconsistencies that typically occur during system construction. Walker (1981) emphasizes an organic system structure based on the premise that module interdependence needs to be coordinated through mutual adjustment rather than standards or plans.

Research emphasizing coordination during system construction has attempted to determine an optimal strategy for system testing and integration. A vital part of a programmer's task during system integration is to understand the functions and behavior of a module from its code (Robson et al. 1991). Solheim and Rowland (1993) conduct a simulation experiment to study how big bang versus incremental testing affects system reliability. It is observed that a testing and integration strategy favoring fewer system integrations could produce more reliable systems. However, this study does not deal with economic aspects. For example, for a given project, it is not clear whether coordination costs will be increased or reduced by delaying system integration.

There has also been an attempt to better coordinate system construction through a focus on development environments. Among other things, development environments deal with coordination aspects during large system construction, for example, maintenance of software libraries, configuration management, change request notices, and so on (Katz and Lehman 1984, Ramamoorthy et al. 1986, Dittrich and Lorie 1988, Hudson and King 1988, Ramanathan and Sarkar 1988, Katz 1990).

## 3. Model Development

In the first subsection, we describe details of the setting used to characterize the software construction process. Next we analytically describe the various activities involved in the construction process. We then present the coordination model and briefly discuss its properties. A simple numerical example is used to illustrate the model in the last subsection.

## 3.1. Preliminaries

A schematic high-level view of the system development process is shown in Figure 1. The process begins with a functional specification of the system. The design subprocess transforms the functional specifications into technical descriptions of the modules in the system. This is followed by module development (including individual module testing) and coordination. As shown in Figure 1, system construction is iterative. In particular, it may be noted that the coordination subprocess does not necessarily lead to the release of a new version of the system. A new version is released only after it meets the functional specifications.²

![](/api/attachments/97WTVHTU/fulltext/images/e44e8f7ca15fe639cb4d24a17603cce7dadc3561b61dd7a16159646b74a9688e.jpg)  
FiGURE 1. Schematic Representation of Development and Coordination Activities in the System Construction Process

² Although not of interest in this study, a higher level of iteration may occur. The release of a version may be followed by the preparation of functional specifications for the next version of the system.

![](/api/attachments/97WTVHTU/fulltext/images/8ab88284f029d3bea81bea4fef7dc96a2a11292010ebfbc2a7c88477da3ec7f4.jpg)  
FiGURE 2. Different Stages in Development and Coordination Shown on a Time Axis.

Development consists of module coding and unit testing. Modules are released if the planned functional requirements have been incorporated and unit tests are successful. These modules belong to the released set. Other modules on which planned development is incomplete, or unit testing has not been done, are not released. These modules belong to the unreleased set.

Coordination consists of system integration and module rework. The system integration process resolves inconsistencies among modules in the released set and the remaining modules in the system. It is a process of reciprocal adaptation involving the newly released modules and consistent versions of unreleased modules. The rework process reconciles differences between two different versions of a module in the unreleased set: a version created by partial development, and a version created during system integration. This is a unidirectional adaptation process wherein only the current versions of the modules in the unreleased set are modified. At the end of the rework phase, all modules are consistent with one another in their current states.

We describe an example of the above development and coordination process involving a small system with six modules. Figure 2 tracks the state of a module at different stages of the process.

1. At time $t _ { 0 } ,$ the six modules designated $a _ { 0 } , b _ { 0 } , c _ { 0 } , d _ { 0 } , e _ { 0 }$ and $f _ { 0 }$ are assumed to be compatible with one another, that is, they form a mutually consistent version of the system with respect to the functional elements currently included.

2. Development work on some of these modules starts from time $t _ { 0 }$ . Modules are released after some functional elements have been added and unit testing has been done. The released set comprises modules $a _ { 0 } ^ { \mathrm { r e l } } , \ : c _ { 0 } ^ { \mathrm { r e l } }$ and $e _ { 0 } ^ { \tt r e l }$ . Note that modules $d _ { 0 } ^ { \mathrm { d e v } }$ and $f _ { 0 } ^ { \mathrm { d e v } }$ are not considered to be in the released set, either because the planned development is not yet complete, or because the development is complete but the modules have not been unit tested. This is consistent with standard practice where a partially complete and/or untested module is not used for system integration (Beizer 1987). Instead, the last consistent version of such a module is used.

![](/api/attachments/97WTVHTU/fulltext/images/5a7be1083279d5fd62268dcee9b9fff618b3d331f42606bcfa2f3116f03c9347.jpg)  
FiGURE 3. Components of Cycle Time

3. We assume in this example that the policy requires a coordination to be scheduled when three modules have been released. Thus, at time $t _ { 1 }$ , the three released modules $a _ { 0 } ^ { \mathrm { r e l } } , c _ { 0 } ^ { \mathrm { r e l } }$ and $e _ { 0 } ^ { \mathrm { r e l } }$ are integrated with consistent versions of the remaining modules, that is, $b _ { 0 } , d _ { 0 }$ , and $f _ { 0 }$ . Inconsistencies detected during integration testing may require that all these modules be adapted.

4. At the end of integration, modules $d _ { 0 }$ and $f _ { 0 }$ each have two changed versions: a partially developed, unreleased version $( d _ { 0 } ^ { \mathrm { d e v } }$ and $f _ { 0 } ^ { \mathrm { d e v } } )$ , and a version resulting from the integration process. These differing versions of each module are reconciled during the rework process. Specifically, the changes incorporated in these modules during integration are applied to the partially developed versions.

5. After coordination is completed, the six modules are again consistent with respect to one another in their current states. The next cycle of development and coordination begins with the six modules in states described by $a _ { 1 } , b _ { 1 } , c _ { 1 } , d _ { 1 } , e _ { 1 }$ and $f _ { 1 }$

The example above assumed that coordination is performed after the release of three modules. It is not clear if this is the optimal strategy. We next develop an analytical model that will determine the coordination strategy that minimizes coordination costs.

## 3.2. Construction Activities

Here we develop analytical expressions for the time spent on each of the activities in the system construction process. Figure 3 displays these activities in the form of a construction cycle. Note that we have divided system integration into two activities: changeover and adaptation. These activities are discussed in this section. Notation introduced here is summarized in Table 1.

We consider a software project consisting of homogeneous modules being developed by a team of developers. Homogeneous is used to mean that: (i) modules in the system are (approximately) of the same size and complexity, (ii) the level of interaction between any pair of modules in the system is the same, and (iii) each module is connected to the same number of other modules.³

Modeling Coordination in Software Construction

<table><tr><td colspan="2">TABLE 1Symbols Used</td></tr><tr><td colspan="2">Project Parameters</td></tr><tr><td> $N$ </td><td>total number of modules in the system</td></tr><tr><td> $p$ </td><td>pairwise coefficient of interaction between modules in the system</td></tr><tr><td> $r$ </td><td>number of modules connected to each module in the system</td></tr><tr><td> $L$ </td><td>estimated development effort to construct the system</td></tr><tr><td> $T$ </td><td>time available for system construction</td></tr><tr><td> $\Lambda$ </td><td>mean of Poisson process describing the release of modules by developers</td></tr><tr><td colspan="2">Decision Variables</td></tr><tr><td> $S$ </td><td>number of developers in the group</td></tr><tr><td> $m$ </td><td>number of modules representing the coordination policy</td></tr><tr><td colspan="2">Variables Representing Time Within a Cycle</td></tr><tr><td> $\tilde{D}, \tilde{D}_{m}$ </td><td>development time, or equivalently, the time until the release of the  $m^{th}$  module</td></tr><tr><td> $K$ </td><td>changeover time, that is time spent by team on communication and program comprehension during the integration process</td></tr><tr><td> $\tilde{A}$ </td><td>adaptation time, that is time spent to adapt the  $m$  released modules with consistent versions of remaining modules</td></tr><tr><td> $\tilde{R}$ </td><td>rework time, that is time spent on reworking the  $(N - m)$  partially developed but not released modules to make them consistent with the  $m$  integrated modules</td></tr><tr><td> $\tilde{C}$ </td><td>time spent on coordination activities,  $\tilde{C} = K + \tilde{A} + \tilde{R}$ </td></tr><tr><td> $\tilde{\tau}$ </td><td>cycle time,  $\tilde{\tau} = \tilde{D} + \tilde{C}$ </td></tr><tr><td colspan="2">Objective Function</td></tr><tr><td> $E(\tilde{C}/\tilde{D})$ </td><td>the expected coordination time per unit development time, representing the quantity to be minimized</td></tr></table>

Development Time. Assume that N system modules are assigned to a team of S developers in such a way that each module is the responsibility of exactly one developer. We assume that the team of developers releases modules at a rate described by a Poisson process with mean denoted by $\Lambda .$ . The Poisson distribution is appropriate in our setting since, (i) the release process is typically a continuous one and hence the probability of two or more modules being released in a small time interval is low, and (ii) individual modules are released independently of one another. These properties map well to the requirements for a Poisson process (Ross 1970).

Let m denote the coordination policy followed for the project. This means that coordination is scheduled immediately after the release of the $m ^ { \mathrm { t h } }$ module by the group. Let $y _ { 1 }$ denote the time from 0 to the time of the release of the first module, and for $1 < n \leq m ,$ let $y _ { n }$ denote the time from the release of module $( n - 1 )$ to the release of module n. Since the release of modules follows a Poisson process with rate Λ, it is known that $y _ { n } .$ for $n = 1 , 2 , \ldots , m ,$ , are independent, identically distributed exponential random variables having mean $1 / \Lambda$ , and that $\tilde { D _ { m } } ;$ the time until the arrival of the $m ^ { \mathfrak { n } }$ module, $\begin{array} { r } { \tilde { D } _ { m } = \sum _ { \imath = 1 } ^ { m } y _ { \imath } } \end{array}$ , is distributed as an Erlang variable with parameters m and Λ (Ross 1970). Its probability density function is given by:

$$
f _ {\dot {D} _ {m}} (x) = \Lambda e ^ {- \Lambda x} \frac {(\Lambda x) ^ {m - 1}}{(m - 1) !}, \quad x \geq 0.\tag{1}
$$

The expected time spent on development, $E ( \tilde { D _ { m } } )$ , i.e., the expected time until the arrival of the $m ^ { \mathrm { t h } }$ module is given by:

$$
E (\tilde {D} _ {m}) = \int_ {0} ^ {\infty} x f _ {\tilde {D} _ {m}} (x) d x = \frac {\Lambda^ {m}}{(m - 1) !} \int_ {0} ^ {\infty} e ^ {- \Lambda x} x ^ {m} d x = \frac {\Lambda^ {m}}{(m - 1) !} \frac {m !}{\Lambda^ {m + 1}} = \frac {m}{\Lambda}.\tag{2}
$$

For simplicity, in the rest of this paper we use $\tilde { D }$ rather than $\tilde { D _ { m } }$ , to denote the time spent on development by each developer during one construction cycle.

Changeover Time. The time required for changeover is the time spent after the release of m modules and before the adaptation process starts. There are two types of activities that occur during changeover. The first is the communication required among members of the team. Communication includes time spent answering questions generated by team members. Communication may also involve negotiation, and in some situations, mediation between members, to resolve issues relating to the responsibility for removing inconsistencies between modules. Members often present their work to the team to prevent lapses in communication (Bhandari et al. 1993). The other important variable influencing changeover time is program comprehension. Program comprehension is required to analyze how changes in modules affect one another (Robson et al. 1991; Yau and Colofello 1980, 1985).

We model the changeover time as depending on: (i) the square of the number of members in the team, and (ii) the number of modules released, as described below:

$$
K = k _ {1} S ^ {2} + k _ {2} m, \quad \text { where } k _ {1} \text { and } k _ {2} \text { are   constants. }\tag{3}
$$

The first term on the right-hand side of (3) considers the impact of team size and structure on the changeover time. The effect of team size is expressed as the square of the number of developers. Interviews with programmers and system engineers reveal that as the size of the team is increased beyond a point communication overhead in a project can get out of hand (Curtis et al. 1988). This supports the hypothesis that communication overhead might increase nonlinearly with team size. In addition, previous research suggests that the amount of communication overhead in a team depends upon the number of communication links (each link connects two members) that need to be established (Malone 1987, Brooks 1982, Pressman 1987). We introduce the constant $k _ { 1 }$ to account for team structure effects. A flat, homogeneous team may require a higher value for $k _ { 1 }$ , whereas a lower value for $k _ { 1 }$ would be more appropriate for a hierarchically organized team, since every member of the team would not need to communicate with every other member.

The second term on the right-hand side of (3) models the impact of program comprehension during the adaptation process. Since changes in these released modules must be understood before other modules in the system can be made consistent, we expect the effort spent on program comprehension to depend on the number of released modules (m). The value of $k _ { 2 }$ will depend upon the ease of program comprehension. Specifically, $k _ { 2 }$ should decrease as programs become easier to comprehend. This constant may be influenced by factors such as the size and complexity of the system modules, the use of program comprehension techniques, standards followed for documentation, characteristics of the development environment, and so on

Adaptation Time. We begin with a simple instance of the problem of determining an appropriate functional form for estimating the time required for adaptation, ${ \check { A } } ,$ as a function of the team size (S) and the coordination policy (m). Consider a homogeneous system with three modules: a, b, and $c .$ To begin, let us assume that these three modules are consistent with respect to one another. Let $t _ { a }$ units of time be spent on modifying module a during development. We need to estimate the time spent on adaptation so that the three modules again form a consistent system. To do this, we introduce the notion of the pairwise coefficient of interaction (PCI). We note here that PCI is a parameter that characterizes the level of interaction between the different pairs of modules in a system. It concerns the question: how much time do we need to spend on system adaptation if a specified amount of time is spent on revising one of its modules? For a homogeneous system of modules, the value of PCI between any pair of modules is a nonzero constant if any one module in the pair calls the other; otherwise, this value is zero.

The value of PCI may depend, among other things, on: (i) the import and export interfaces of the two modules, (ii) the parameters passed between the two modules, and (iii) the pre- and post- condition describing the interaction (i.e., under what conditions does one module call the other? how does the other module respond?), etc. We note that previous research has described measures similar to the pairwise coefficient of interaction. For example, see Yau and Colofello (1980), Schneidewind (1987), and Lejter et al. (1992) for a discussion of the “ripple effect." and the discussion of module coupling by Stevens et al. (1974).

In a relatively homogeneous system, several samples of module pairs may be taken and an average value of PCI computed across these samples may be used as the value of PCI for any two modules in the system. In a more heterogeneous system, it may be necessary to use a different value of PCI for each pair of modules. Here, we consider a homogeneous system and use a constant value of PCI (denoted by $p )$ between any pair of connected modules.

Using this notion of PCI, we model the time required for adaptation as an infinite sequence of adaptations between modules in the system. The origination for these adaptations may be at any module that is either revised and released during the development process or revised during the adaptation process. Using the example in Figure 4, we posit that the time $t _ { a }$ spent on module a generates an initial amount of adaptation time of magnitude $p$ times $t _ { a }$ for each of the two modules b and $c ,$ as shown in Figure 4(a). This means that it is necessary to spend an amount of time $p t _ { a }$ on each of modules b and c to accommodate the changes made to module a. We refer to the initial adaptation as “first-order adaptation."

The total effort due to first-order adaptation is therefore $( p t _ { a } + p t _ { a } ) = 2 p t _ { a }$ . Now the ${ p t } _ { a }$ units of time spent on modules b and c will in turn generate its own need for adaptation, referred to as second-order adaptation in Figure 4(b). The magnitude of each second-order adaptation is $p ( p t _ { a } )$ or $p ^ { 2 } t _ { a }$ . The sum of the second-order adaptations is $( 2 p ^ { 2 } t _ { a } + 2 p ^ { 2 } t _ { a } ) = 4 p ^ { 2 } t _ { a }$ . Continuing in this manner, the third-order adaptations sum to $8 p ^ { 3 } t _ { a }$ (see Figure 4(c)), the fourth-order adaptations to $1 6 p ^ { 4 } t _ { a }$ , and in general, the $n ^ { \mathrm { t h } } .$ -order adaptations to $2 ^ { n } p ^ { n } t _ { a }$

![](/api/attachments/97WTVHTU/fulltext/images/a0869c710689c143f7f6b9578eaf57fe386b16e42d0bdf206af0ee2e0a11e9bf.jpg)  
(a) first-order adaptations

![](/api/attachments/97WTVHTU/fulltext/images/e43378f4c444b603c5907f2408d52fd9917ef261d75d1a98ab9b4a12ed31a2a2.jpg)

![](/api/attachments/97WTVHTU/fulltext/images/f2440dac00393c30fd7e37f6952879a4dd90229b2905b3bd859daed73f537dc9.jpg)  
(b) second-order adaptations

![](/api/attachments/97WTVHTU/fulltext/images/400785ebc85839f22020fc950486e524d05d6e1fc998349435737dec1e95148b.jpg)

![](/api/attachments/97WTVHTU/fulltext/images/36c97fdf1de20b4c507e652e0d4d08cfe362b1592a5ae8f70c6a84689c4db325.jpg)  
(c) third-order adaptations

![](/api/attachments/97WTVHTU/fulltext/images/83f5e1fac3f0655fc8a9695f64a697b338fad30c151a89c07789feb418e52b5a.jpg)  
FiGURE 4. Illustration of the Adaptation Process Having Spent $t _ { a }$ Time Units on Module a.

The time required for integrating modules $a , b ,$ , and c as a result of spending $t _ { a }$ units of development time on module a is therefore obtained as:

$$
\tilde {A} = \frac {2 p t _ {a} + 4 p ^ {2} t _ {a} + 8 p ^ {3} t _ {a} + \cdots}{S} = \frac {2 p t _ {a}}{S} \sum_ {\iota = 0} ^ {\infty} (2 p) ^ {\iota} = \frac {2 p t _ {a}}{S (1 - 2 p)}, \quad p <   0. 5.\tag{4}
$$

In (4) we have used an infinite sequence of adaptations but in reality this will typically be finite. Upon examining the geometric series for the work flows, it is easy to see that the contribution of most higher order terms is small. Thus, for simplicity we use infinite terms. Note also that we divide the right-hand side of Equation (4) by S to convert effort units to time units.

The analysis thus far assumed that only module a changed during the development phase. If now, in addition, $t _ { b }$ and $t _ { c }$ units of time had been spent on developing modules b and c then the adaptation time for the three modules in the system would be:

$$
\tilde {A} = \frac {2 p (t _ {a} + t _ {b} + t _ {c})}{S (1 - 2 p)}, \quad p <   0. 5.\tag{5}
$$

In general, if there are $N$ modules in a system and if m of these moduies are released such that $t _ { i }$ units of time $( i = 1 , 2 , \dotsm m )$ are spent on these modules then the adaptation time will be given by:

$$
\tilde {A} = \frac {(N - 1) p \sum_ {i = 1} ^ {m} t _ {i}}{S (1 - (N - 1) p)}, \quad p <   \frac {1}{(N - 1)}.\tag{6}
$$

The multiplier $( N - 1 )$ for $p$ in the numerator and denominator arises if there are $( N - 1 )$ modules directly connected to any module in the system, i.e., each module is connected to all other modules. Instead, if there are r modules directly connected to each module in the system (referred to here as connectivity), the expression for adaptation time is given by:

$$
\tilde {A} = \frac {r p \sum_ {i = 1} ^ {m} t _ {i}}{S (1 - r p)}, \quad p <   \frac {1}{r}.\tag{7}
$$

The summation $\sum _ { i = 1 } ^ { m } t _ { i }$ in Equation (7) represents the development effort expended on the m released modules. To evaluate this summation, recall first that $\hat { D }$ units of time are spent on development by each developer, and each developer is responsible for $N / S$ modules. Some modules on which development is done may be released while others may not. We assume that a developer equally distributes development time on the $N / S$ modules, i.e., each module is developed for $\mathcal { S } \tilde { D _ { \mathbf { \lambda } } } / \mathbf { \tilde { \Lambda } }$ units of time. Therefore, the development effort expended by the group on the m modules in the released set is $m ( S { \tilde { D } } / N )$ and that on the $( N - m )$ modules in the unreleased set is $( N - m ) ( S { \tilde { D } } / N )$

From the above discussion, the expected time required for adaptation can be expressed as:

$$
E (\tilde {A}) = E \left(\frac {r p}{S (1 - r p)} \frac {m S \tilde {D}}{N}\right) = \frac {m ^ {2} r p}{N \Lambda (1 - r p)}, \quad p <   \frac {1}{r}.\tag{8}
$$

In the above analysis, we require that the pairwise coefficient of interaction be limited to $1 / r ,$ , where r is the connectivity. This is necessary to ensure that the geometric series representing the adaptation time converges to a finite value. $1 \mathrm { f } p \ge 1 / r ,$ the sum of the infinite series will clearly be unbounded, suggesting that system adaptation is a never-ending sequence of module adaptations. Note that this restriction is required only if infinite adaptation flows occur. Note also that $p$ will typically be positive, since allowing $p$ to be zero would cause adaptation time to be zero, implying that modules in the system are independent of each other.

Rework Ttme. Rework is done on the modules that were partially developed but not released at the start of the last integration process. Rework is a unidirectional adaptive process where work flows from a released module to each unreleased module that is connected to it. An unreleased module requires rework before it can be developed further.

Consider a system with two modules a and b. Let $m \simeq 1$ for this system. Suppose that a was released first and integration was done immediately upon its release. Let $t _ { a }$ and $t _ { b }$ units of time be spent on modules a and b respectively. We model the effort required to rework module b as:

$$
\tilde {R} = \frac {p (t _ {a} t _ {b})}{t _ {a} + t _ {b}}, \quad t _ {a} + t _ {b} > 0.\tag{9}
$$

We expect that rework effort on module b should depend upon the product of $t _ { a }$ and $t _ { b } .$ . The product form is consistent with the fact that rework effort is zero if either $t _ { a }$ or $t _ { b }$ is zero. In (9) we divide by the total time spent on the two modules to ensure dimensional consistency.

In general, if there are $( N - m )$ modules that need rework and there are m modules that were released in the last integration the total rework time is given by:

$$
\tilde {R} = \frac {1}{S} \sum_ {i = 1} ^ {m r / (N - 1)} \sum_ {j = 1} ^ {(N - m)} \frac {p t _ {i} t _ {j}}{\left(t _ {i} + t _ {j}\right)}, \quad t _ {i} + t _ {j} > 0,\tag{10}
$$

where the subscripts i and j refer to modules in the released and unreleased sets respectively. The upper limit for i is the estimated number of modules in the released set that are connected to a module in the unreleased set. Since every module is connected to r other modules in the system, an average of $m r / ( N - 1 )$ modules in the released set are connected to a module in the unreleased set. The upper limit for / is the total number of unreleased modules. Note that the right-hand side of (10) is divided by S to convert rework effort to rework time. Our assumption regarding equal allocation of time on released and unreleased modules allows us to write: $t _ { \iota } = t _ { \jmath } = S \tilde { D } / N$

Thus,

$$
\tilde {R} = \frac {m r p (N - m)}{2 (N - 1) N} \tilde {D}.\tag{11}
$$

Hence, the expected time required for rework is given by:

$$
E (\tilde {R}) = \frac {m ^ {2} r p (N - m)}{2 (N - 1) N \Lambda}.\tag{12}
$$

Construction Cycle. We have developed functional forms for the times spent by developers on the different activities of system construction. Let ĩ denote the cycle time. The expected cycle time is given by:

$$
\begin{array}{r l} E (\tilde {\tau}) & = E (\tilde {D}) + K + E (\tilde {A}) + E (\tilde {R}) \\ & = \frac {m}{\Lambda} + k _ {1} S ^ {2} + k _ {2} m + \frac {m ^ {2} r p}{N \Lambda (1 - r p)} + \frac {m ^ {2} r p (N - m)}{2 (N - 1) N \Lambda}. \end{array}\tag{13}
$$

Note that the expected cycle time in (13) is a function of the two decision variables, m and S.

## 3.3. Problem Formulation

We are now able to formulate the coordination model. We assume that the design specifications for the modules are known, and that the total development effort to construct the system has been estimated to be L person-months. We also assume that the clock time available for system construction, denoted by $T ,$ is available as an organizational constraint. The decision variables in the model are the coordination policy (m) and the team size (S). The objective is to minimize the total effort spent on coordination, subject to the constraint that the system must be constructed within T' months.

The coordination effort per cycle by the team is $S \tilde { C } .$ where $\dot { C } = K + \dot { A } + \dot { R }$ , the time spent per cycle on coordination activities. The number of cycles required to construct the system is given by $L / S \tilde { D }$ since $S \tilde { D }$ units of development work are completed in one cycle. Hence the total coordination effort expended by the team is $\tilde { S C } ( L / S \tilde { D } )$ $= L ( \tilde { C } / \tilde { D } )$ .Since $L$ is a constant for a given project, to minimize the total coordination effort it is sufficient to minimize the ratio of time spent per cycle on coordination to that spent on development. Since $\tilde { C }$ and $\hat { D }$ are both random variables, the objective function is specified in terms of the expected value of this ratio.

We have $\tilde { C } = K + \tilde { A } + \tilde { R } .$ and therefore:

$$
\begin{array}{r l} E \left(\frac {\tilde {C}}{\tilde {D}}\right) & = E \left(\frac {K + \tilde {A} + \tilde {R}}{\tilde {D}}\right) = E \left(\frac {K}{\tilde {D}}\right) + \frac {m r p}{N (1 - r p)} + \frac {m r p (N - m)}{2 (N - 1) N} \\ & = K E \left(\frac {1}{\tilde {D}}\right) + \frac {m r p}{N (1 - r p)} + \frac {m r p (N - m)}{2 (N - 1) N}. \end{array}\tag{14}
$$

The expectation of the reciprocal of $\dot { D }$ can be evaluated as:

$$
\begin{array}{r l} E \left(\frac {1}{\tilde {D}}\right) & = \int_ {0} ^ {\infty} \frac {1}{x} f _ {\tilde {D}} (x) d x = \frac {\Lambda^ {m}}{(m - 1) !} \int_ {0} ^ {\infty} e ^ {- \Lambda x} x ^ {m - 2} d x \\ & = \frac {\Lambda^ {m}}{(m - 1) !} \frac {(m - 2) !}{\Lambda^ {m - 1}} = \frac {\Lambda}{(m - 1)} \end{array}\tag{15}
$$

where the integration result in the last step is valid for $m > 2$

Using the functional form for $K ,$ together with Equations (14) and (15) the model can be formulated as shown below.

Problem $C P$

$$
\underset {S, m} {\text { Min }} Z _ {h m} (S, m) = E \left(\frac {\tilde {C}}{\tilde {D}}\right) = \frac {(k _ {1} S ^ {2} + k _ {2} m) \Lambda}{(m - 1)} + \frac {m r p}{N (1 - r p)} + \frac {m r p (N - m)}{2 (N - 1) N}
$$

Subject to

$$
\frac {L}{S} E \left(\frac {\tilde {\tau}}{\tilde {D}}\right) \leq T,\tag{C1}
$$

$$
\frac {m L \Lambda}{S (m - 1)} \geq N,\tag{C2}
$$

$$
E (\tilde {\tau}) \leq T,\tag{C3}
$$

$$
m > 2,\tag{C4}
$$

$$
m \leq N,\tag{C5}
$$

$$
m \text {   and   } S \text {   are   integers.   }\tag{C6}
$$

Constraint (C1) is the time restriction expressed in terms of the development work $L$ required to be completed in T units of time. This can be derived as follows. Since $\tilde { D }$ units of development occur in ĩ units of time, the expected time for one developer to complete L units of work will be given by $L E ( \tilde { \tau } / \tilde { D } )$ . Since there are a total of S developers it follows that at least $( L / S ) E ( \tilde { \tau } / \tilde { D } )$ units of time must be available for system construction. Constraint (C2) is required to ensure that each module is released at least once in the period utilized for system construction (i.e., some period less than or equal to T). This can be derived as follows. Since m releases occur in one cycle the total expected number of releases is m times the expected number of cycles given by $E ( m L / S \tilde { D } ) = m L \Lambda / S ( m - 1 )$ . The third constraint (C3) ensures that at least one cycle is completed during the scheduled period. Constraints (C4) and (C5), (C6) are self-explanatory.

Comment 1. For a system with $p = 0$ , the objective function is minimized by choosing $m = N$ . This becomes apparent upon setting $p = 0$ in the objective function:

$$
\underset {S, m} {\text { Min }} E \left(\frac {\tilde {C}}{\tilde {D}}\right) = \frac {(k _ {1} S ^ {2} + k _ {2} m) \Lambda}{(m - 1)}
$$

which is clearly minimized by maximizing $m , \mathrm { i . e . , } m = N .$

Comment 2. In this section we have assumed that development time is spent on all $N$ modules. The model, however, can be easily applied to maintenance scenarios as well, where only some of the N modules may need development. Let $N = N _ { c } + N _ { u }$ where $N _ { c }$ and $N _ { u }$ denote the number of changed and unchanged modules respectively. To modify the model for maintenance scenarios we replace $N$ by $N _ { c }$ in Equation (8) for adaptation. The revised expression for rework (replacing Equation 12) is E(R) $= m ^ { 2 } r p ( N _ { c } - m ) / 2 ( N - 1 ) N _ { c } \Lambda$ . The rest of the problem is unchanged. Note that the values of r and $p$ apply to the entire system since modules in $N _ { u }$ will also require adaptation.

## 3.4. Example

Assume that a team consisting of 5 persons is assigned the task of constructing a system consisting of $N = 1 0 0$ modules. The total development effort is estimated to be 15 person-months, and the system is to be constructed within 4.5 months.

Assuming a connectivity of $5 \left( r = 5 \right)$ , we use a system with low PCI $( p = 2 0 \%$ of the maximum permissible value; $0 . 2 \times ( 1 / 5 ) = 0 . 0 4 )$ . To estimate the constant $k _ { 1 }$ , let us assume that 5 hours are spent by the team for every integration meeting. Assuming 8 hours per day and 25 days per month, the number of months spent per meeting is equal to $5 / ( 8 \times 2 5 )$ . Hence, $0 . 0 2 5 = k _ { \mathrm { l } } \times ( S ^ { 2 } )$ or $k _ { 1 } = 0 . 0 0 1$ months per person squared. In addition, assume that it takes about 4 hours to analyze the effects of changes made on a given module. Hence, $k _ { 2 } = 2 / ( 8 \times 2 5 ) = 0 . 0 1$ months per module, To estimate the mean release rate for the team (Λ), we assume that a module is released at least once during its development. The rate of release of modules may be approximated by (100 modules) times (5 persons)/[15 person-months] = 33.33 modules per month.

In Figure 5, we plot the objective function as a function of the coordination policy m. The best coordination policy for this team $( S = 5 )$ is $m ^ { * } = 2 1$ and the time taken to construct the system is 4.38 months. For this coordination policy, the expected coordination effort per unit development is 0.46. This implies that approximately 31% of the total effort spent on construction is due to coordination.ª

![](/api/attachments/97WTVHTU/fulltext/images/ad8947945e3904ac22caf3216d3987b6fdd2813eee5bc85847cae24dc73e4688.jpg)  
FiGURE 5. Expected Coordination per Unit Development vs. Coordınation Policy

In this example, we find that if the team size is reduced to 4, the svstem cannot be completed in the budgeted time (time required = 5.12 months). We also find that values of S greater than 5 lead to more coordination effort. Hence, it is optimal to construct the given system using a five person team that integrates whenever 21 modules have been released.

In the next section, we present extensive numerical results obtained from optimally solving problem CP. These results provide interesting insights into the trade-off between the time for completion and the coordination required to achieve it.

## 4. Numerical Results

In this section, we investigate numerical properties of the optimization model developed in the previous section. A certain parameter is varied holding the others constant. The impact of the varying parameter is observed on the coordination policy, team size and the coordination per unit development. Three parameters are varied: (i) the value of ${ \dot { p } } ,$ (ii) system size (M) and, (iii) the time available for construction (T). We assume that values for the changeover parameters for the given development environment are estimated to be $k _ { 1 } = 0 . 0 0 1$ and $k _ { 2 } = 0 . 0 1$

Since system size is increased with L kept constant (i.e., the productive output is fixed), the average size and/or complexity of an individual module can be expected to decrease. Other things being equal, a decrease in average module size and/or complexity should increase the mean rate of module release. Furthermore, this rate should increase with the size of the team. To permit comparison across different system and team sizes, we use the relationship below for the mean release rate. In practice, of course, the mean release rate may be directly estimated by:

$$
\Lambda = \left(\frac {S}{L / N}\right) = \frac {N S}{L}.\tag{16}
$$

## 4.1. Solution Procedure

With the mean release rate (Λ) specified by Equation (16) two of the model's constraints, namely, C2 and C3 drop out, i.e., these constraints are trivially met. This simplifies the model considerably and the problem can be easily reduced to a single variable optimization problem. Upon examining the objective function of problem CP, it is clear that the decision variable S should be chosen as the minimum value that satisfies the model's constraints.

For a given value of S the objective function is convex with respect to m if:

$$
m ^ {3} - m - \alpha <   0, \quad \text { where } \quad \alpha = \frac {2 N (N - 1) N S (k _ {1} S ^ {2} + k _ {2})}{L r p}.\tag{17}
$$

The condition in (17) is satisfied for all problems reported in this section. In addition, solving the above cubic as an equation in m we find that the convexity condition is far from stringent, i.e., it is typically satisfied for values of m in the range [3, N] for a variety of parameter values. Assuming convexity, it is possible to solve the coordination problem as one involving a single decision variable m. A procedure to do so is outlined below.

## SOLUTION PROCEDURE

INITIALIZE

$Y = M ,$ where M is a very large positive number

DoUNTIL{A solution is found or the problem is determined to be infeasible}

$$
m ^ {*} = \underset {m \in \{3, 4, N \}} {\text {Min}} \frac {(k _ {1} S ^ {2} + k _ {2} m) N S}{(m - 1) L} + \frac {m r p}{N (1 - r p)} + \frac {m r p (N - m)}{2 (N - 1) N}
$$

$\mathrm { I f } \quad \frac { L } { S } E \biggl ( \frac { \tilde { \tau } } { \tilde { D } } \biggr ) \geq T$ an optimal solution has been found

ELSE

$$
X = \frac {L}{S} E \left(\frac {\tilde {\tau}}{\tilde {D}}\right)
$$

IF X > Y the problem is infeasible

$$
Y = X
$$

$$
S = S + 1
$$

![](/api/attachments/97WTVHTU/fulltext/images/e5847b2b51625ff737790dc516041ff34622a04283d31a18d2eaec870ba14f69.jpg)  
FiGURE 6. Effect of Module Interaction on Coordination Policy.

For a given value of S, the optimal value of m in the above algorithm can be determined as follows. Differentiate the objective function with respect to m and set the result to zero. The following cubic equation in m is obtained:

$$
m ^ {3} + a _ {2} m ^ {2} + a _ {1} m + a _ {0} = 0, \quad \text { where }
$$

![](/api/attachments/97WTVHTU/fulltext/images/0d71f61375821186da1fdeb1518ab693b79ce000b36b3e69aacd67945212f1a1.jpg)  
FiGURE 7. Effect of Module Interaction on Coordination Required

![](/api/attachments/97WTVHTU/fulltext/images/ac368e7319db33f4f70bf51a92a2843e809a161ddb9c057dee5d796ed77eb50f.jpg)  
FiGURE 8. Effect of Module Interaction on Team Size.

$$
a _ {2} = - \left(\frac {N - 1}{1 - r p} + \frac {N}{2} + 2\right), \quad a _ {1} = - \left(\frac {2 (N - 1)}{1 - r p} + N + 1\right), \quad \text { and }
$$

$$
a _ {0} = \frac {k _ {1} N ^ {2} S ^ {3}}{L r p} + \frac {k _ {2} N ^ {2} S}{L r p} - \frac {N - 1}{1 - r p} - \frac {N}{2}.
$$

![](/api/attachments/97WTVHTU/fulltext/images/c6ccfaa8ef653a800b64e4dce08a78733504d54cb57ad74ea0541f38147d5af2.jpg)  
FiGURE 9. Effect of System Sıze on Coordination Required.

![](/api/attachments/97WTVHTU/fulltext/images/7d134829fc34f0005c9f2c390620c7cb4c5a9c619d2148e9605a1c5e99efe65a.jpg)  
FiGURE 10. Effect of System Size on Coordınation Policy.

Solve the above cubic to obtain three roots for m (Abramowitz and Stegun 1970) Depending on the value of the coefficients, a cubic equation in the above form has one real root and a pair of complex conjugate roots or three real roots. Ignore imaginary roots (if any). If a root is greater than N replace it by N. If a root is less than 3 replace it by 3. If a root is in the range [3, M] round it off to the closest integer. The optimal value of m is found by evaluating the objective function at each of the roots obtained through the above process.

In the above algorithm, the variable X represents the expected time taken to construct the system with the current values of $m ^ { * }$ and S. A project is infeasible if: (i) values below a particular value of S are not sufficient to construct the system in a specified period, and (ii) it is found that increasing S increases the time taken to construct the system. When conditions (i) and (ii) are detected, there is no need to explore higher values of S. Using the above algorithm, it is easy to optimally solve problem CP for various parameter values.

## 4.2. Pairwise Coefficient of Interaction

Here we study the effects of changing the intermodule interaction (expressed as a proportion of the maximum allowable, i.e., 1/r) on the coordination policy, expected coordination per unit development and the team size. Figure 6 shows that if p increases, it is better to integrate when fewer modules have been released. At high levels of P, the effort required for adaptation and rework increases rapidly. Because the cost of delaying integration increases, it is attractive to integrate more frequently (i.e., choose a lower value for m, the number of modules released before integration).

Figure 7 shows that the optimal coordination per unit development increases as the value of p increases. As p increases, more time is spent on adaptation and rework activities. Hence, the coordination per unit development increases. Figure 8 follows directly from Figure 7. Note that a small increase in p does not typically require a larger team size; however, increasing p beyond a point requires additional members to construct the system. The discontinuous behavior exhibited by the curve in Figure 8 is due to the integrality constraint on the value of S.

![](/api/attachments/97WTVHTU/fulltext/images/0e5af5fdbd7968398fb233985ab87bf829c06359a53ba81094950b50afe89a12.jpg)  
FiGURE 11. Effect of Crashing on Team Size.

![](/api/attachments/97WTVHTU/fulltext/images/2664e48ecda86a284472c616affd6112330ed422d8365e45c795e5096be89cf5.jpg)  
FiGURE 12. Effect of Crashing on Coordination Required.

![](/api/attachments/97WTVHTU/fulltext/images/9e0380cda1196a8ffb318f52dfb87a2aacde831fac6c8f54887ba32cd592488f.jpg)  
FiGURE 13. Effect of Crashing on Coordınation Policy.

## 4.3. System Size

Here we study the impact of changing the system size (M) on the coordination required per unit development and the coordination policy. In Figure 9, we find that as system size increases, the amount of coordination required per unit development also increases. Pressman (1987) observes that as the size of a module decreases (i.e., for a given system the number of modules increase), more interfaces are needed leading to an increase in construction cost. Thus Figure 9 may be interpreted as an increase in construction cost resulting from an increase in the number of system interfaces.

![](/api/attachments/97WTVHTU/fulltext/images/85d73e86ff295f9d85454ca14ef2cb7787efde6f028a14d77a4de4aaa917d1af.jpg)  
FiGURE 14. Effect of Team Sıze on Maximum Productive Output

<table><tr><td rowspan="3" colspan="2"></td><td colspan="3">TABLE 2Summary of Results</td></tr><tr><td colspan="2">Optimal response</td><td>Impact of change</td></tr><tr><td>Coordination Policy</td><td>Team Size</td><td>Coordination Per Unit Development</td></tr><tr><td rowspan="3">Change in parameter</td><td>Pairwise coeff. of interaction increases</td><td>Increase level of coordination</td><td>Increase team size</td><td>Increase in the coordination required</td></tr><tr><td>System size increases</td><td>Reduce level of coordination</td><td>Increase team size</td><td>Increase in the coordination required</td></tr><tr><td>Time available reduces</td><td>Reduce level of coordination</td><td>Increase team size</td><td>Increase in the coordination required</td></tr></table>

As system size increases, the optimal coordination policy should be relaxed, i.e., it is optimal to integrate when more modules are released. This relationship is displayed in Figure 10. Note the nonlinear nature of the curve in Figure 10. Although not shown here, the optimal coordination policy expressed as a percentage of the system size also increases as N increases (the optimal m is approximately 5% at N = 125, approximately 12% at N = 5,000). The results in Figure 10 can be interpreted as follows. Since an increase in system size tends to increase the number of persons required, the communication cost during team meetings increases sharply with an increase in system size. Given the increase in communication cost, it is optimal to have fewer system integrations, i.e., delay system integration to a certain extent.

## 4.4. Crashing

We refer to crashing as the act of reducing the time available for system construction keeping everything else about the project the same. The graph in figure 11 shows that as the time available for construction reduces, more persons are required to construct the system. There are two effects occurring here. As the available time is reduced, clearly more persons are required to do the same amount of work. This is a direct effect of crashing. The other effect is indirect. Since more persons are required more coordination effort results, i.e., the team becomes less productive (see Figure 12). Because the team is less productive, a further increase in team size is required. The increase in team size resulting from crashing causes the optimal coordination policy to prescribe fewer integrations (see Figure 13).

While the above results are not surprising, we note that the relationship between available time and team size is nonlinear. Reducing time available is initially possible with a small increase in team size, but as the schedule is continuously tightened, the impact on team size becomes more significant. This appears to be consistent with experience gathered in the field (Brooks 1982)

## 4.5. Team Size

The graph in Figure 14 displays the effect of increasing the size of the team on the productive output obtained in 100 time units, i.e., the total development output in T = 100. This graph shows that adding extra team members beyond a point will reduce the team's productive output. Note that for a given project there is a lower limit for the time required to complete construction activities. Thus, a system may be infeasible to construct in a certain period irrespective of the number of personnel available.

These results also show that a lower level of intermodule interaction increases the amount of productive output from a team. The curves in Figure 14 may be interpreted as production functions corresponding to different technologies. A superior design (for example, a lower value of p obtained through object based technology) could lead to a higher level of productive output. In Figure 13 we find that the curves fall more steeply beyond the peak value as the value of p decreases. For lower values of p it is optimal to integrate more frequently. Thus the negative impact of increasing team size beyond a point is higher when the value of p is lower.

## 4.6. Discussion

The results reported in this section should not interpreted in a strict numeric sense For example, these results should not be used to predict the time to completion for system construction. On the other hand, it is reasonable to use these results to predict the impact of changing a particular system parameter on the direction of an outcome variable. For instance, these results can be used to predict that time needed for construction will increase with an increase in intermodule interaction, everything else held constant.

In Table 2, qualitative conclusions of this study are depicted in two dimensions Each row of this table prescribes the project manager's optimal response to a change in a particular project parameter (other parameters are held constant). The impact on the manager's objective function, namely, the coordination required per unit development, is displayed in the last column.

The first row in Table 2 summarizes the effects of increasing intermodule interaction. Thus, the optimal response to an increase in p is to increase the level of coordination, i.e., managers should call for an integration when fewer modules have been released. A larger team size will be required to accomplish completion. As expected the coordination required per unit development increases. System development methodologies often recommend that intermodule interaction should be controlled for example, through high cohesion and low coupling, by making module interfaces more explicit, by using a message passing mechanism to share module resources, etc. (Yau and Colofello 1980; 1985). Clearly, the design effort to reduce p incurs extra cost. This cost, however, may be compensated by a reduction in the resources required to construct the system. Although, trading-off design and construction effort may be attempted in practice, system development methodologies seldom make this trade-off explicitly (Paulson and Wand 1992). The analytical model developed in this paper could support managers in making superior trade-offs between design and construction effort

The second row in Table 2 prescribes that the coordination policy should be relaxed for larger systems. In the last column this row, we find that an increase in system size increases the coordination per unit development, perhaps in part, due to more system interfaces. Thus, to reduce coordination per unit development, system size should be as small as possible (for example, choose N equal to S). However, such a strategy to partition a system will likely make the individual modules more complex. This may not be desirable for several reasons.

The cost of constructing a module typically increases nonlinearly with the size of the module (Pressman 1987). Thus the cost of constructing modules must be tradedoff with the cost of constructing interfaces. Making individual modules more complex may also be undesirable because the maintenance effort required in the life of a module could increase, especially if the maintenance is performed by someone who did not develop the module. The extent of modularization (i.e., an appropriate value for M), is clearly an issue that requires considerable judgment (Parnas 1972). However. the model presented here makes it possible for a designer to examine the different implications of selecting a particular system size.

The third row in Table 2 prescribes that as the available time reduces, the level of coordination should also be reduced. This in sharp contrast to the Windows NT experience (presumably a project with a very tight schedule) where the team integrated daily. Of course, to properly evaluate such a coordination policy, many other factors need to be considered (for example, p and r for the system, the total development effort required, etc.). In a slightly different context, Brooks has observed that managers typically react to schedule slippage by adding more personnel, sometimes causing the project to slip even further (Brooks 1982). It would be interesting to collect data to study whether managers increase the level of coordination in response to a project that appears to be slipping. Our model, of course, tells us that they must do exactly the opposite!

The results concerning crashing may be valuable for proposal managers while bidding for projects, say, in a consulting environment. The promise of an earlier delivery date will likely make a proposal more attractive to the customer. However, a tighter schedule will expend more resources to construct the same system (development effort stays the same, but coordination effort increases). These results could help proposal managers include marketing, economic and personnel considerations while bidding for software contracts.

## 5. Coordination in Heterogeneous Systems

In this section we relax the homogeneity assumptions and examine the robustness of the results reported in the previous sections by comparing the performance of a heterogeneous system with an equivalent homogeneous system⁵. We report on three experiments carried out for this purpose. The first two experiments were designed to study the impact on coordination costs of variability in (1) module connectivity, and (2) pairwise coefficient of interaction. The third experiment was designed to compare different coordination policies in heterogeneous and homogeneous systems given variability in both the above factors. The performance of heterogeneous systems in these experiments was determined using a simulation model.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
TABLE 3
Parameters Used for Analyzing the Performance of Heterogeneous Projects

Project Parameters
System size (N) = 500 modules
Team size (S) = 20 team members
Development effort (L) = 1000 person-months
Time available (T) = 75 months
Module release rate ( $\Lambda$ ) = 10 modules/month
Changeover Time Parameters
Team structure ( $k_{1}$ ) = 0.001
Program comprehension ( $k_{2}$ ) = 0.010
Distribution Parameters
Module connectivity ( $|r^{(i)}|$ ) ~ Uniform (mean =  $\mu_{r}$ , variance =  $\sigma_{r}^{2}$ )
Coefficient of interaction ( $p_{ij}$ ) ~ Uniform (mean =  $\mu_{p}$ , variance =  $\sigma_{p}^{2}$ )
Development time in a cycle ( $\tilde{D}$ ) ~ Erlang (mean = m/ $\Lambda$ , variance = m/ $\Lambda^{2}$ )
</div>

We describe the approach used for modeling heterogeneity and coordination costs in the simulation study. The parameter values used for the heterogeneous system in the experiments are summarized in Table 3.

## 5.1. Modeling System Heterogeneity

The three types of heterogeneity considered in the simulation experiments are described below. We begin with models for representing heterogeneity in software systems. Next we describe distribution assumptions made in the experimental study. Finally, we indicate the method used for constructing equivalent homogeneous systems.

Connectivity. One characteristic of software systems is the presence of variance in connectivity. In particular, for hierarchically designed systems, certain modules may call many different modules and combine the results obtained. Modules lower in the hierarchy may not directly interact with many other modules. Hence it is important to determine the sensitivity of our results concerning the homogeneous assumption of uniform module connectivity.

Let $i \in \{ 1 , 2 , \ldots , N \}$ and $j \in \{ 1 , 2 , . . . , N \}$ denote particular modules in the system. The connectivity between modules i and j is defined as:

$$
r _ {i j} = \left\{ \begin{array}{l l} 1 & \text { if   modules } i \text { and } j \text { are   connected   modules }, \\ & \text { i.e.,   module } i \text { calls   module } j \text { or   module } j \text { calls   module } i. \\ 0 & \text { otherwise }. \end{array} \right.
$$

Note that $r _ { \imath \jmath } = r _ { \jmath \imath }$ for all $i , j \in \{ 1 , 2 , \ldots , N \}$ . The set of modules connected to module i is denoted by ${ \overset { \cdot } { r } } ^ { ( \iota ) } = \left\{ j | r _ { \iota \ j } = 1 \right\}$ . The connectivity of module i, that is, the number of modules connected to module $t ,$ is denoted by $\big \vert r ^ { ( i ) } \big \vert$

In the experiments described below, variation in module connectivity was modeled assuming that $| r ^ { ( t ) } |$ is a uniformly distributed random variable with mean $\mu _ { r }$ and coefficient of variation $k _ { r } = \sigma _ { r } / \mu _ { r }$ , where $\sigma _ { r }$ is the standard deviation of the random variable. Values for $\mu _ { r }$ and $k _ { r }$ were specified at the beginning of each experiment. The procedure used for constructing a connected system of modules was as follows. In the first step, for each $i \in \{ 1 , 2 , \ldots , N \}$ , uniform random deviates were generated in the range [0, 1]. Values for $| r ^ { ( i ) } |$ were then obtained by scaling these deviates to the range $\{ \mu _ { r } - \sqrt { 0 . 3 } \sigma _ { r } , \mu _ { r } + \sqrt { 0 . 3 } \sigma _ { r } \}$ . In the second step, pairs of module numbers $i , j$ $\in \{ 1 , 2 , \ldots \land N \}$ were independently generated, and the values of $\cdot _ { r _ { \iota \ j } }$ and $r _ { \mu }$ were set to 1 if the following conditions were satisfied: $( \mathrm { i } ) \ i \neq j , ( \mathrm { i i } )$ the modules were not already connected, i.e., the current value of $r _ { t } ) = r _ { t } = 0$ , and (iii) the module connectivities were not exceeded, i.e., $\begin{array} { r } { \sum _ { k = 1 } ^ { N } r _ { \iota k } < \bar { \vert } r ^ { ( \iota ) } \vert } \end{array}$ for module i, and $\begin{array} { r } { \sum _ { k = 1 } ^ { N } r _ { \jmath k } < | r ^ { ( \jmath ) } | } \end{array}$ for module j.

The connectivity r in the equivalent homogeneous system is represented by the average number of modules connected to an individual module:

$$
\overline {{{r}}} = \frac {1}{N} \sum_ {i = 1} ^ {N} | r ^ {(i)} | = \frac {1}{N} \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} r _ {i j}.\tag{18}
$$

Pairwise Coefficient of Interaction. A second aspect common to many software systems is that modules do not interact with one another to the same extent. This may arise due to differences in the number and nature of parameters exchanged and consequently the type of coupling between them. Modules that are tightly coupled will have a higher PCI than modules that are loosely coupled.

Let $p _ { y }$ denote the PCI between modules i and j. If modules i and j are not connected, then $p _ { \imath \jmath } = 0 ;$ ; otherwise $0 < p _ { \iota \jmath } < 1$ . Note that $p _ { \imath \jmath } = p _ { \jmath \imath }$ for all $i , j \in \{ 1 , 2 ,$ $\dots , N \}$ . In the experiments described below, variation in PCI was introduced by assuming that $p _ { \imath \jmath }$ is a uniformly distributed random variable with mean μ and $\mu _ { p }$ coefficient of variation $k _ { p } = \sigma _ { p } / \mu _ { p }$ , where $\sigma _ { p }$ denotes the standard deviation of the random variable. Values for $p _ { i j }$ were generated from this distribution (using a procedure similar to that described above for connectivity), for each pair of modules $i , j \in \{ 1 , 2 , \ldots , N \}$ where $r _ { \scriptscriptstyle { l j } } = 1$ . It was then verified for each i that $\begin{array} { r } { \sum _ { J = 1 } ^ { N } p _ { \imath \jmath } } \end{array}$ $< 1$ . This condition is required to ensure that the adaptation time in successive stages of the adaptation process constitutes a convergent sequence. We note that this is a sufficient condition for ensuring that the condition $\bar { p } < 1 / \bar { r }$ holds for the equivalent homogeneous system⁶.

$$
\bar {p} = \frac {1}{N r} \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} p _ {i j} <   \frac {1}{r}.
$$

Since the total connectivity in the system is $N { \overline { { r } } } ,$ PCI in the equivalent homogeneous system, $p ,$ is represented by the average value:

$$
\bar {p} = \frac {1}{N \bar {r}} \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} p _ {i j}.\tag{19}
$$

Development Time. Software projects are typically characterized by varying amounts of time spent on different modules. This may arise due to differences in module size and complexity. Thus, modules that are larger or more complex might need increased development and testing time in comparison to other modules. In addition, modules that have previously been developed and tested may experience less additional development work in comparison to other modules for which new functionality has yet to be added. The development time spent on different modules within a cycle therefore varies.

In the experiments described here, $\tilde { D } ,$ , the development time within a cycle, is modeled as an Erlang random variable with mean $m / \Lambda$ , where Λ is the rate at which modules are released by the development team. Since the Erlang deviate with mean $m / \Lambda$ is the sum of m identically distributed exponential variables having mean $1 / \Lambda$ , values for $\tilde { D }$ were sampled using the composition method (Phillips et al. 1976, Pritsker and Pegden 1979). Thus, if $y _ { 1 } , y _ { 2 } , \dotsc , y _ { m }$ represent m independent uniform deviates in [0, 1] then the Erlang deviate $\dot { D }$ is expressed by the inverse transformation $\begin{array} { r } { \dot { D } = \left( - 1 / \Lambda \right) \sum _ { t = } ^ { m } } \end{array}$ ln $y _ { \iota }$ :

Since $\check { D }$ is the time until the release of the $m ^ { \mathfrak { h } }$ module, it follows that the total effort on the $N$ modules is SD. Uniform random deviates in [0, 1] were therefore used to distribute $\tilde { S D }$ over the $N$ modules in the system. Thus, $\mathrm { i f } \ \tilde { t } _ { t }$ denotes the development time spent on module $i ,$ then $\begin{array} { r } { \sum _ { \iota = 1 } ^ { N } \widetilde { l } _ { \iota } = S \tilde { D } } \end{array}$ . Development time within a cycle in the equivalent homogeneous system is represented by the mean of the Erlang distribution, $m / \Lambda$

## 5.2. Coordination Time

We denote the sets of released and unreleased modules as {released set} and {unreleased set} respectively. In the experiment, {released set} was constructed by randomly selecting m modules from the $N$ system modules. The remaining $( N - m )$ modules constituted the {unreleased set}.

The changeover time (K) is a function of S and $m ,$ and can therefore be directly calculated using Equation (3). The expression for adaptation time $( \check { A } )$ can be derived as follows. Let $\tilde { A } _ { i } ^ { ( n ) }$ denote the time required for adapting module i during the $n ^ { \mathfrak { t h } }$ adaptation stage. When $n = 1$ , the adaptation time required for module i depends on the development time spent on connected modules in {released set }. Hence,

$$
\tilde {A} _ {i} ^ {(1)} = \sum_ {j \in r ^ {(i)} \cap \{\text { released   set } \}} p _ {i j} \tilde {t} _ {i}.\tag{20}
$$

For any subsequent stage $n ,$ the adaptation time for module i depends on the time spent on all connected modules which were modified during the previous stage, and therefore:

$$
\tilde {A} _ {i} ^ {(n)} = \sum_ {j \in r ^ {(i)}} p _ {i j} \tilde {A} _ {j} ^ {(n - 1)}.\tag{21}
$$

The total adaptation time over all N modules during the cycle is therefore given by:

$$
\tilde {A} = \sum_ {i = 1} ^ {N} \sum_ {k = 1} ^ {n} \tilde {A} _ {i} ^ {(k)}.\tag{22}
$$

In the simulation experiments, adaptation time for heterogeneous projects was calculated as a fifth-order adaptation process $( \mathrm { i } . \mathrm { e } . , n = 5 )$

Next consider the time spent on rework (R) for modules in the {unreleased set }. Let ${ \tilde { R _ { J } } }$ denote the rework time on module $j \in$ {unreleased set}. Then,

$$
\tilde {R} _ {j} = \sum_ {i \in r ^ {(j)} \cap \{\text { released   set } \}} \frac {p _ {i j} \tilde {t} _ {i} \tilde {t} _ {j}}{(\tilde {t} _ {i} + \tilde {t} _ {j})}\tag{23}
$$

and the total time spent on rework during the cycle is:

$$
\tilde {R} = \sum_ {j \in \{\text {unreleased set} \}} \tilde {R} _ {j}.\tag{24}
$$

The performance of the heterogeneous system in one cycle is measured by the ratio:

$$
\tilde {Z} _ {h l} (S, m) = \frac {\tilde {C}}{\tilde {D}} = \frac {K + \tilde {A} + \tilde {R}}{\tilde {D}}.\tag{25}
$$

## 5.3. Experimental Results

Before conducting the experiments described here we confirmed the correctness of the simulation model. To do this, we compared the objective function values calculated using the analytical model with the simulation model that was forced to operate under conditions of strict homogeneity. To ensure strict homogeneity in the simulation model all sources of variation were eliminated by setting $k _ { r } = k _ { p } = 0$ and distributing $\tilde { D }$ equally over the N modules. In addition the homogeneous model used average values for connectivity, PCI and development time as the heterogeneous model. The objective function values for the two models differed by less than a third of a percentage point for a variety of parameter values. These differences completely vanished (i.e., the results of the two models became identical) when a finite homogeneous model with fifth order adaptation flows was used. Thus under strict homogeneity, the simulation model is identical to the homogeneous model.

The three experiments described below compare the infinite version of the homogeneous model with a heterogeneous model that accumulates up to fifth-order adaptation flows.

EXPERIMENT 1: EFFECT OF VARIABILITY IN MODULE CONNECTIVITY. The effect of variation in module connectivity on coordination time was studied for the heterogeneous system described in Table 3. Two coordination policies $( m = 5 0$ and 100), three levels of mean connectivity $\{ \mu _ { r } = 3 0$ , 50 and 70), and three coefficients of variation $( k _ { r } = 0 . 1 0 , 0 . 3 0$ , and 0.50) were considered. Since the experiment was designed to isolate the effects of variability in $\mid \boldsymbol { r } ^ { ( i ) } \mid$ , the pairwise coefficient of interaction was set at ${ \pmb \mu } _ { p } = ( 0 . 5 0 / \mu _ { r } )$ with coefficient of variation $k _ { p } = 0$ . Thus, in this experiment, $p _ { \imath \jmath }$ $= { \pmb { \mu } } _ { p }$ , for all i, j where $r _ { \imath \jmath } = 1$

Four projects were studied for each combination of these parameters. Table 4 compares average performance for the heterogeneous projects with the equivalent homogeneous projects. Values reported here are percentage differences calculated as

$$
\% \text {difference} = \frac {\bar {Z} _ {h t} (S , m) - \bar {Z} _ {h m} (S , m)}{\bar {Z} _ {h m} (S , m)} \times 100.\tag{26}
$$

Coordination costs in Table 4 are seen to be higher for the equivalent homogeneous systems at low levels of variation. However, coordination costs for heterogeneous systems rise with increasing variability in $\{ r ^ { ( \iota ) } \}$ . Furthermore, as $\pmb { \mu } _ { r }$ increases, the effects of increasing variability begin to dominate, resulting in increased coordination time for the heterogeneous projects. Homogeneity assumptions thus tend to overestimate coordination time at low levels of variability and underestimate at high levels of variability. In general, heterogeneous projects with average connectivity r as high as 14% of system size and coefficient of variation up to about 30% can be modeled as if they were homogeneous; the error in the objective function value due to this approximation is less than about 3%.

EXPERIMENT 2: EFFECT OF VARIABILITY IN THE PAIRWISE COEFFICIENT OF IN-TERACTION. This experiment was designed to investigate the effect of variation in PCI on coordination time. The overall structure of the experiment is similar to Experiment 1, and so we mention only those parameter settings that differ. Since this experiment was designed to measure the effect of variability in $p _ { \imath \jmath }$ , the value of $\mu _ { r }$ was kept fixed at 50 in this experiment by setting coefficient $k _ { r } = 0$ . The three values of $\mu _ { p }$ examined here are 30%, 50%, and 70% of $( 1 / \mu _ { r } )$ . Three levels for coefficient $k _ { p }$ were used: $k _ { p } = 0 . 1 0 , 0 . 3 0$ , and 0.50.

The results of this experiment, shown in Table 5, represent percentage differences calculated using Equation (26). Coordination costs in the heterogeneous projects are consistently lower than in the homogeneous equivalents. For a given value of $\mu _ { p } ,$ increasing variability has an almost negligible effect on the difference in coordination costs. As $\mu _ { p }$ increases, the difference in coordination costs rises very slowly at low values and quite rapidly subsequently. In general, the experiment indicates that the mean of the distribution is a more significant contributor than the variability in determining coordination costs.

EXPERIMENT 3: OPTIMAL COORDINATION POLICY. This experiment was designed to compare different coordination policies for projects in the presence of heterogeneity in $\mid r ^ { ( \iota ) } \mid$ and $p _ { \imath \jmath }$ . Different policies were simulated by varying $m ,$ the number of modules released before a system integration is performed. A number of independent simulation runs were performed for each value of m in the range $m = 2 0$ to $m = 1 0 0$ with step size 5. The remaining parameters were set as follows: mean connectivity $\pmb { \mu } _ { r }$ $= 5 0 .$ , coefficient of variation $k _ { r } = 0 . 3 0$ , mean pairwise coefficient of interaction $\mu _ { p }$ = 50% of $( 1 / \mu _ { r } )$ , and coefficient of variation $k _ { p } = 0 . 3 0$ . The choice of these values for $k _ { r }$ and $k _ { p }$ was influenced by the results of the first two experiments. When considered independently, they led to coordination costs that were within about $3 \%$ of the equivalent homogeneous projects. Here we were interested in seeing the combined effect these levels of variation had on coordination costs.

The experiment was set up so that the project was terminated when either of the following conditions became true at the end of a cycle:

TABLE 4  
Effect of Variation in Module Connectivity on Average C/D in Heterogeneous Systems

<table><tr><td rowspan="2">Coordination Policy (m)</td><td rowspan="2">Mean Connectivity (μr)</td><td colspan="3">Coefficient of Variation (kr)</td></tr><tr><td>0.10</td><td>0.30</td><td>0.50</td></tr><tr><td rowspan="3">50</td><td>30</td><td>-2.48</td><td>-0.53</td><td>+4.30</td></tr><tr><td>50</td><td>-2.94</td><td>-1.06</td><td>+3.67</td></tr><tr><td>70</td><td>-2.98</td><td>+1.39</td><td>+6.41</td></tr><tr><td rowspan="3">100</td><td>30</td><td>-2.89</td><td>+0.39</td><td>+8.47</td></tr><tr><td>50</td><td>-3.58</td><td>-0.42</td><td>+7.37</td></tr><tr><td>70</td><td>-1.97</td><td>+1.55</td><td>+9.71</td></tr></table>

(i) the required development effort (L) was completed (indicating a successfully completed project), or

(ii) the time available (T) was used up (indicating infeasibility for the chosen coordination policy).'

A comparison of the objective function values obtained from the several simulation runs in the heterogeneous project with an equivalent homogeneous project is shown in Figure 15. Two versions of the equivalent homogeneous model are shown in Figure 15—one based on an infinite sequence of flows, and another based on fifthorder flows. The optimal coordination policy with S = 20 is m = 40 in all three cases. The coordination time is slightly larger for homogeneous projects than for heterogeneous projects over most values of m. The differences are very small at low values of m (<35) and increase slightly at larger values of m.

In summary, these three experiments provide compelling validation of the homogeneity assumptions made in §3 and the numerous results described in §4. The sources of variation do not appear to matter much, although the impact due to variation in connectivity appears to be larger. Because heterogeneous systems are difficult to model analytically. it is encouraging to find that mapping a heterogeneous system to an equivalent homogeneous system has a very small effect on the optimal coordination policy over a wide range of parameter values. The main benefit of this finding is that project managers may not need to resort to time consuming numerical techniques to determine efficient policies for coordinating software systems. The analytical insights obtained through modeling homogeneous systems are hence quite robust,

## 6. Summary and Conclusions

In this paper, we develop an analytical model to examine problems concerning coordinating a team that develops a software system. We use two decision variables: (i) the level of coordination that should be applied (operationally, the number of modules released before integration), and (ii) the size of the team required to complete the project. The objective is to minimize the coordination effort subject to the constraint that the project is completed within a specified period.

TABLE 5  
Effect of Variation in Pairwise Coefficient of Interaction on Average C/D in Heterogeneous Systems

<table><tr><td rowspan="2">Coordination Policy (m)</td><td rowspan="2">Mean pairwise Coefficient of Interaction $\left( {\mu }_{p}\right)$ </td><td colspan="3">Coefficient of Variation  $\left( {k}_{p}\right)$ </td></tr><tr><td>0.10</td><td>0.30</td><td>0.50</td></tr><tr><td rowspan="3">50</td><td> ${0.30}/{\mu }_{r}$ </td><td>-1.82</td><td>-1.82</td><td>-1.82</td></tr><tr><td> ${0.50}/{\mu }_{r}$ </td><td>-2.45</td><td>-2.45</td><td>-2.38</td></tr><tr><td> ${0.70}/{\mu }_{r}$ </td><td>-9.31</td><td>-9.26</td><td>-9.15</td></tr><tr><td rowspan="3">100</td><td> ${0.30}/{\mu }_{r}$ </td><td>-2.04</td><td>-2.04</td><td>-2.00</td></tr><tr><td> ${0.50}/{\mu }_{r}$ </td><td>-2.89</td><td>-2.87</td><td>-2.79</td></tr><tr><td> ${0.70}/{\mu }_{r}$ </td><td>-11.84</td><td>-11.77</td><td>-11.57</td></tr></table>

The construction of a software system is perceived to be an alternating sequence of two kinds of activities: (i) uncoordinated activities in which development takes place, and, (ii) coordination activities in which inconsistencies that occur during the development phase are corrected (coordination activities consist of system integration and rework). We develop a micro model to estimate the coordination time required for a given amount of uncoordinated development. To do this, we use the notions of the pairwise coefficient of intermodule interaction (PCI) and connectivity. The PCI estimates the adaptation time required to make a pair of modules consistent, given that a certain amount of uncoordinated development is performed on the modules. Connectivity is the number of modules directly connected to a given module. For the analytical treatment, we assume that the system is homogeneous (modules are equally complex and PCI and connectivity are constants). Another micro model is developed to estimate the rework component in a construction cycle. Rework also depends upon PCI and connectivity.

The micro model developed for estimating coordination time (integration plus rework time) is used to derive the objective function employed in the macro model that attempts to minimize the coordination time per unit development time. The model is numerically solved and several results are obtained. Two important results are summarized here. One result concerns the effect of crashing a project's schedule on team size and productivity. Proposal managers could use the insight provided here to trade-off the chances of winning a contract by promising an early delivery date, with the fall in productivity and increase in personnel requirement. The other important conclusion of this study is that as the time available for construction is reduced, the level of coordination should also be reduced.

The significance of the homogeneity assumption is investigated in some detail. It is found that the expected behavior of a heterogeneous system can be closely approximated by treating it as a homogeneous one in which the actual values for PCI, connectivity and development time spent on a module are replaced by average values.

![](/api/attachments/97WTVHTU/fulltext/images/531916314e01585e2a3e0510a8d247ae7a9af914c4c38c139cb45c2626bc87e1.jpg)  
FiGURE 15. Objective Function Values for Heterogeneous and Homogeneous Projects for Various Coordination Policies

This result leads us to believe that the homogeneous model is robust and the results obtained through it are quite general.

Further research on this problem could examine other more sophisticated coordination policies, for example, a policy that depends not only on the number of modules released, but also on the individual times spent on the released modules. Of course, it would be extremely difficult to analytically evaluate the objective function with such a policy, let alone find the optimal parameters for the policy. However, more sophisticated policies may be considered in a decision support environment where the project manager may investigate the implications of a decision to integrate using an approximate numerical procedure. Such coordination related aspects could be included in existing software engineering environments.

The model developed in this paper may apply to other coordination problems that arise in team efforts. Product development typically operates this way. In the development of a photocopier for example, independent units develop the various subsystems of the copier, such as optics, mechanical paper handling, power supply and so on (Hammer 1990). Having people develop simultaneously saves time, but at the integration and testing phase, the pieces often fail to work together. Then costly redesign begins. In a product development environment, of course, different functional forms for integration and rework may have to be derived. Considerable research, however, will be needed to investigate the applicability of the coordination model in this paper to other problem domains.\*

## References

Abramowitz, M. and I. Stegun (Ed.), Handbook ofMathemattcal Functions, Dover Publications Inc., 1970.

Baker, F.. “Chief Programmer Team Management of Production Programming," 1BM Systems Journal 11, 1 (1972), 56–73.

Banker, R., S. Datar, C. Kemerer and D. Zweig, “Software Complexity and Maintenance Costs," Commu nications of the ACM, 36, 11 (1993), 81–94.

Beizer, B., Software System Testıng and Qualıty Assurance, Van Nostrand Reinhold Company, New York 1987.

Belady, L. A. and M. M. Lehman, "A Model of Large Program Development," IBM Systems Journal, 15 (1976), 225-252.

Bhandari, I., M. Hallıday, E. Traver, D. Brown, J. Chaar and R. Chillarege, "A Case Study of Software Process Improvement During Development," IEEE Transacttons on Software Engineering, 19, 12 (1993),1157-1170.

Boehm, B. W., Software Engineering Economics, Prentice-Hall Inc., Inglewood Cliffs, NJ, 1981.

-, “A Spiral Model of Software Development and Enhancement,"IEEE Computer, 21, 5 (1988), 61-72.

Brooks, F. P., The Mythical Man-Month—Essays on Software Engineerıng, Addison-Wesley, Readıng, MA, 1982.

Curtis, B., H. Krasner and N. Iscoe, “A Field Study of the Software Design Process for Large Systems," Communications ofthe ACM, 31, 11 (1988), 1268–1287

Dittrich, K. R. and R. A. Lorie, “Version Support for Engineering Database Svstems," IEEE Transactions on Software Engineering, 14 (1988), 429–437.

Hammer, M., “Reengineering Work: Don't Automate, Obliterate," Harvard Bustness Revıew, July-August (1990), 104–112

Hudson, S A. and R. Kıng, “The Cactıs Project: Database Support for Software Environments," IEEE Transactions on Software Engincering, 14 (1988), 709–719

Katz, R.. “Toward a Unified Framework for Version Modelıng in Engineering Databases," ACM Computing Surveys, 22 (1990), 375–408.

and T. J. Lehman, “Database Support for Versions and Alternatives of Large Design Files,"IEEE Transactions on Software Engıneering, SE-10 (1984), 191–200

Lejter, M., S. Meyers and S. P Reiss, “Support for Maintaining Object-Oriented Programs," IEEE Transactions on Software Engineering, 18 (1992), 1045–1052

Malone, T. W., “Modelıng Coordination in Organızations and Markets," Management Sctence, 33, 10 (1987).1317-1332

Parnas, D., “On the Criteria for Decomposing Programs into Modules," Communicattons of the ACM December (1972)

Paulson, D. and Y. Wand, “An Automatic Approach to Information Systems Decomposition," IEEE Transactions on Software Engineering, 18, 3 (1992), 174–189.

Phillips, D., A. Ravındran and J. Solberg, Operattons Research. Princıples and Practıce, John Wiley & Sons, New York, 1976

Pressman, R , Software Engineerıng A Practitioner's Approach, Second Edition. McGraw Hill, 1987.

Pritsker, A. and C. Pegden, Introduction to Sımulation and SLAM, Halstead Press, 1979.

Ramanathan, J. and S. Sarkar, “Provıding Customized Assistance for Software Lifecycle Approaches." IEEE Transactions on Software Engineering, 14 (1988), 749–757

Ramamoorthy, C. V., V. Garg and A Prakash, “Programming in the Large," IEEE Transactions on Software Engineering, SE-12 (1986), 769–783.

Robson, D. J., K. H. Bennett, B. J. Cornelius and M. Munro, “Approaches to Program Comprehension," The Journal of Systems and Softw are, 14, 2 (1991), 79–84.

Ross, S., Applted Probability Models wuh Optimizatton Appltcattons, Holden-Day, 197).

Safoutin, M. J. and D. L. Thruston, “A Communications Based Technıque for Interdısciplinary Design Team Management," 1EEE Transactions on Engineerıng Management, 40, 4 (1993), 360–372.

Schneidewind, N. F., “The State of Software Maintenance," IEEE Transactions on Software Engineering, SE-13 (1987), 303-310

Solheim, J. A. and J. H. Rowland, “An Empirical Study of Testing and Integration Strategies Using Arti ficial Software Systems," IEEE Transactions on Software Engineering, 19, 10 (1993), 941–949.

Stevens, W., G. Myers and L. Constantine, “Structured Design," IBM Systems Journal, 13 (1974), 115– 139.

Swanson, E. B. and C. M. Beath, “Departmentalization in Software Development and Maintenance," Communications of the ACM, 33 (1990), 658–667.

Tamai, T., “Experıment on Coordination within Software Development Teams," Informatton and Soft ware Technology, 34, 7 (1992), 437–442.

Walker, M. Managing Software Reltabılity The Paradıgmatic Approach, North-Holland, New York 1981.

Yau, S. S. and J. S. Colofello, “Design Stability Measures for Software Maintenance," IEEE Transactons on Software Engineering, SE-11 (1985), 849–856.

- and —, "Stability Measures for Software Maintenance," IEEE Transactions on Software Engineering, SE-6 (1980), 545–552.

Zachary, G. P., "Climbing the Peak—Agony and Ecstasy of 200 Code Writers Beget Windows NT," Wall Street Journal, May 26, 1993, A1, A6
