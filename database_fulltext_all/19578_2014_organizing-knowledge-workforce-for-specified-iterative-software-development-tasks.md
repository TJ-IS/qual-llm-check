---
otero_id: 19578
otero_key: "B8YJFWYF"
title: "Organizing knowledge workforce for specified iterative software development tasks"
authors: "Benjamin B.M. Shao; Peng-Yeng Yin; Andrew N.K. Chen"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.10.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Organizing knowledge workforce for speci<sup>fi</sup>ed iterative software development tasks

Benjamin B.M. Shao <sup>a</sup>, Peng-Yeng Yin <sup>b</sup>, Andrew N.K. Chen <sup>c,</sup>⁎

<sup>a</sup> W. P. Carey School of Business, Arizona State University, Tempe, AZ 85287, United States

<sup>b</sup> College of Management, National Chi Nan University, Nantou, Taiwan

<sup>c</sup> School of Business, University of Kansas, Lawrence, KS 66045, United States

## a r t i c l e i n f o

Article history: Received 26 November 2012 Received in revised form 20 August 2013 Accepted 3 October 2013 Available online 11 October 2013

Keywords: Iterative software development Workforce management Task assignment Knowledge management Simulations Particle swarm optimization

## a b s t r a c t

Organizing knowledge workers for speci<sup>fi</sup>c tasks in a software development process is critical for the success of software projects. Assigning workforce in software projects represents a dynamic and complex problem that concerns the utilization of cross-trained knowledge workers who possess different productivities and error tendencies in coding and defect correction. This complexity is further compounded when the development process follows a software release life cycle and involves major releases of alpha, beta, and <sup>fi</sup>nal versions in the context of iterative software development. We study this knowledge workforce problem from three essential project management perspectives: (1) timeliness — obtaining shortest development time; (2) effectiveness — satisfying budget constraint; and (3) ef<sup>fi</sup>ciency — achieving high workforce utilization. We explore ideal workforce composites with two strategic focuses on productivity and quality and with different scenarios of workload ratios. An analytical model is formulated and a meta-heuristic approach based on particle swarm optimization is used to derive solutions in a simulation experiment. Our <sup>fi</sup>ndings suggest that forming an ideal workforce composite is a non-trivial task and task assignments with divergent focuses for software projects under different workload scenarios require different planning strategies. Practical implications are drawn from our <sup>fi</sup>ndings to provide insight on effectively planning workforce for software projects with speci<sup>fi</sup>c goals and considerations.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Software projects require extensive development efforts and can be quite a challenging undertaking for planning and execution. To cope with complexity, large software projects are typically divided into multiple modules, each of which is individually developed and then tested and corrected through iterations for incremental development and quality improvement [11]. An important aspect in software development is resources that include budget and workforce. The productivities of knowledge workers for different types of tasks are not identical; neither is the cost of employing these people. How to effectively manage knowledge workers (e.g., software developers and testers) for various tasks in the software development process is thus a critical issue for the success of software projects. Workforce management in software projects is a dynamic and complex problem that is concerned with the utilization of cross-trained knowledge workers who possess different productivities and error tendencies in coding and defect correction. This complexity is further compounded when the development process follows a software release life cycle and involves major releases of alpha, beta, and <sup>fi</sup>nal versions in the context of iterative software development.

Following the “design evaluation” guideline for a design-science study [30,40], we tackle this software project management problem through an experimental paradigm from three essential project management perspectives: (1) timeliness — obtaining shortest development time; (2) effectiveness — satisfying budget constraint; and (3) ef<sup>fi</sup>ciency — achieving high workforce utilization. We explore ideal workforce composites with two strategic focuses on productivity and quality and with different scenarios of workload ratios. On the workforce management front, we examine how software project managers assemble and allocate workers with different pro<sup>fi</sup>ciencies in development and testing skills to various tasks in the context of iterative software development (i.e., alpha, beta, and <sup>fi</sup>nal releases of the software release life cycle) to achieve the shortest total development time, maximize workforce utilization, satisfy budgetary constraint, and meet quality requirements. An analytical model is formulated and a metaheuristic approach based on particle swarm optimization is used to derive solutions in a simulation experiment.

We explore whether organizations can strike a desired balance by evaluating the tradeoff among abovementioned project management perspectives with appropriate assignment of diverse workers under different strategic focuses and workload scenarios. In doing so, we take the <sup>fi</sup>rst step to tackle this complicated problem with the belief that effective software project management involves more than deploying workers to tasks by availability but requires a holistic and systematic guideline. Practical implications drawn from our <sup>fi</sup>ndings can provide insight on effectively planning workforce for software projects with speci<sup>fi</sup>c goals and considerations.

The intended contributions of this study are as follows. First, while most previous studies look at speci<sup>fi</sup>c aspects of iterative software development, we consider multiple key factors affecting different metrics of software development performance. We do so by formally modeling a software development problem associated with both project and workforce management. Speci<sup>fi</sup>cally, our model seeks to minimize the completion time while satisfying budget constraint, meeting quality requirement, and managing worker assignment in the context of iterative software development. Second, we uncover valuable insights of project and workforce management using a contemporary particle swarm optimization (PSO) algorithm. The ef<sup>fi</sup>cacy of both the proposed model and the PSO algorithm is demonstrated through an extensive simulation. Third, in a larger sense, our endeavor also responds to a recent call for more holistic, multidisciplinary, business-centric, and “macrodesign science” information systems (IS) research that can carry potential high visibility and high impact to organizations and society [16].

The rest of the paper is organized as follows. Section 2 provides background descriptions of iterative software development, project and workforce management, and key factors and perspectives associated with software development. Section 3 explains the context of software development process and our model formulation. Section 4 introduces the particle swarm optimization approach as well as our experiment and simulation settings. Section 5 presents our <sup>fi</sup>ndings and corresponding implications. Finally, concluding remarks, limitations, and future research directions are offered in Section 6.

## 2. Background

It is useful to <sup>fi</sup>rst clearly de<sup>fi</sup>ne some key concepts and terms to delineate the speci<sup>fi</sup>c context of our study. A software development process starts with selecting, designing, and initiating a software project. This process proceeds to the construction and re<sup>fi</sup>ning iterations and then reaches the release of the <sup>fi</sup>nal product. In this study, we focus on the phase of “construction and re<sup>fi</sup>ning iterations” where coding and defect correction occur. A software development project encompasses different scales and types that range from a large system development involving conceptual, logical, and physical designs of many interdependent components to producing software modules requiring mostly programming and debugging efforts only. In this study, we refer a software development project to the latter. For example, in the offshore IT outsourcing context, a software project completed by a subcontractor can be only involved in coding and debugging efforts. Another example can be a turn-key application or module which is developed by a consulting company.

In the context of software development, knowledge workers refer to developers with different pro<sup>fi</sup>ciency levels of coding and debugging computer programs. That is, knowledge workers possess different levels of productivities and error tendencies in coding and defect correction, respectively. Therefore, the context of this study lies in knowledge workforce management and project management for software development. Knowledge workers to be assigned are software code producers who follow pre-de<sup>fi</sup>ned software speci<sup>fi</sup>cations and instructions to perform speci<sup>fi</sup>c software development and quality improvement tasks. We examine how software project managers can assemble and allocate workers with different pro<sup>fi</sup>ciencies in coding and testing skills to a software development project in order to achieve objectives such as the shortest total development time, maximum workforce utilization, satisfying budgetary constraint, and meeting quality requirements.

## 2.1. Iterative software development

Most modern large-scale software projects are carried out in an incremental and iterative fashion termed the software release life cycle.

That is, the incremental construction of software projects proceeds in a series of iterations. Each of the iterations consists of a development phase, followed by a testing–debugging phase [11]. In the development phase, developers work on their assigned modules and perform such tasks as detailed design and coding. In the follow-up testing–debugging phase, developers try to enhance the quality of modules by evaluating the actual output against the expected output and taking corrective actions if any discrepancy occurs in such evaluation. Such an iteration of adding functionalities, inspecting and testing components, and releasing a sequential number of working versions usually repeats for several times before the complete product is <sup>fi</sup>nally delivered to the customer or made available on the market [36]. Additionally, Keil [32] emphasized the importance of matching appropriate project management systems to the stages of software projects.

Many technical and managerial challenges exist in developing largescale software projects that follow the iterative development process. Complexity, innovativeness, and criticality of software systems all contribute to technical challenges [44]. The literature of software engineering and information systems has strongly promoted the use of incremental and iterative development for software projects, as the effectiveness of such development methods has been consistently demonstrated. Practical development paradigms such as iterative process [11], the risk-driven spiral model [10], and rational uni<sup>fi</sup>ed process [38] have been proposed and employed in the industry. Incremental and iterative development facilitates the development of software systems as it reduces the propagation impacts of defective code and produces comparatively stable products in progress that subsequent development can improve upon [44]. On the other hand, managerial challenges arise from the need to coordinate the efforts of project members who possess different skill levels for different tasks. Incremental process models and spiral models based on iterative enhancement have been proposed to manage software development in practice. However, these models provide little guidance for decision makers to effectively manage project and knowledge workforce.

## 2.2. Software project management and workforce management

Project management refers to the planning and control activities associated with the making of a product or service to ensure that the production process be carried out smoothly to meet certain goals. Managing software projects is a complex undertaking as it involves both technical problems (e.g., data structures, algorithms, program ef<sup>fi</sup>ciency) and managerial challenges related to workforce, resource allocations, and other administrative aspects [49]. While many new innovative development tools and methods (e.g., agile, object-oriented programming languages, reusable code) have been proposed and employed to enhance the quality and productivity of software development, it is argued that a management-focused approach to improving the practice of software development process is also warranted [4].

Several attributes separate software projects from other types of projects, causing IS practitioners to struggle with effective software project management. First, the dynamics of software construction typically involve iterative and incremental development. These build and test phases can repeat several times, thus complicating its planning and controlling efforts. Second, the lack of effective planning and controlling tools as well as the paucity of accurate timely information exacerbate the dilemma of promoting creativity and exercising disciplined management in software projects. Finally, knowledge workers are oftentimes cross-trained and possess varied levels of skill, knowledge, and experience [15]. Thus, workforce is likely to show different productivity and error tendency in completing different tasks. These productivity and error factors have to be taken into account by project managers, making the planning decisions even more dif<sup>fi</sup>cult.

Workforce management stems from the human resource management (HRM) literature which encompasses the aspects of practices and strategies for creating, utilizing, and maintaining workforce to increase company value or achieve project goals. Common theoretical HRM strategies include cost strategy (e.g., reducing workforce cost), quality strategy (e.g., improving the depth of workforce competency), and <sup>fl</sup>exibility strategy (e.g., increasing the breadth of workforce competency). One important implication of the <sup>fl</sup>exibility strategy is “workforce alignment” which generally refers to the <sup>fi</sup>t between workforce attributes and intended strategic goals [14]. Many researchers referred the resource-based view (RBV) for the importance of workforce alignment since knowledge workers are considered a scarce and critical resource of a <sup>fi</sup>rm. For example, Dyer and Ericksen [20] noted that greater performance accrues to <sup>fi</sup>rms that have the right types of people in the right places at the right times, doing things which result in the organization receiving maximum bene<sup>fi</sup>ts. However, despite its conceptual importance and appeal, workforce alignment has rarely been examined directly. Campbell [13] demonstrated the ef<sup>fi</sup>cacy of analytical modeling with experiments in allocating and utilizing cross-trained knowledge workers in an organization.

In the context of iterative software development, we intend to explore what an ideal workforce composite should be and how various tasks should be assigned to knowledge workers with diverse capabilities. We seek to answer the research question: how can we form and manage an ideal workforce composite to complete the software project within budget constraints and meet quality requirements in a timely and ef<sup>fi</sup>cient fashion?

## 2.3. Software project performance

It is argued that software project performance ought to be measured along two dimensions: (1) process performance, which speci<sup>fi</sup>es how well the software development process has been undertaken, and (2) product performance, which indicates how well the <sup>fi</sup>nal software system actually meets the speci<sup>fi</sup>cations [46]. Taking both aspects into account is essential for evaluating the performance of a software project. For instance, a software project may provide a high-quality product, but the project itself may have taken much more time or money than initially estimated. By the same token, a well-managed project that is completed on time and under budget may deliver a product of poor quality that fails to satisfy user requirements. In other words, the performance of software projects should be measured by targets met and quality achieved [2]. Meeting targets indicates that a successful project should be completed on time and on budget [48]. Software quality, in turn, refers to whether software product satis<sup>fi</sup>es the pre-speci<sup>fi</sup>ed requirements.

Several studies have focused on software project performance. Nidumolu and Subramani [47] argued that one aspect of outcome control in software development activities is setting performance criteria such as productivity standards, budgets, and schedules. Deephouse et al. [19] studied software project performance by examining if a project meets its schedule/budget targets. Marciniak [41] also urged the use of software development methods to improve product quality and limit costs, duration, and delays. Abdel-Hamid et al. [1] measured software project performance by <sup>fi</sup>nal cost, completion time, and remaining undetected defects. In this study, we analyze the process performance of software development projects from the perspective of timeliness, effectiveness, and efficiency as well as the product performance of the <sup>fi</sup>nal software quality in the context of software release life cycle.

Timeliness is an essential factor in measuring the performance of software development process because project delays can cause serious damages to the developing and adopting organizations [9]. Customers expect a software system to be delivered on time without delay. Despite the unequivocal importance of meeting the schedule requirements, many software projects have failed in this regard and suffered long delay in completion time [33]. These “runaway” projects can result in deadline pressures for both project managers and members, and such pressures likely lead to defective products with low reliability and poor quality as developers are tempted to take shortcuts when faced with approaching deadline [5]. Interestingly, Harter et al. [28] found software product development time to be negatively associated with software product quality (i.e., reduced development time is associated with higher quality). Therefore, we argue that timeliness (speed) is a critical process performance criterion for successful software development. In this study, we attempt to address this timeliness issue by <sup>fi</sup>nding what workforce composite and strategic focus is likely to result in timely completion of software development.

In a general term, effectiveness refers to the extent of an actual outcome compared with the targeted goal. Barker and Verma [8] pointed out that in a resource constrained development environment the ability to assess system engineering effectiveness has been receiving increased emphasis. One important aspect of software project management is a reliable plan of budget and schedules where effectiveness can have a direct impact on the quality of decisions made to manage a software project. The accuracy of software project estimates can reduce unnecessary expenses and improve a system's effectiveness [45]. Furthermore, Maxwell et al. [42] conducted an analysis of software development effort estimation and found that effort predictions made for software projects are more accurate using a company speci<sup>fi</sup>c model than a general model. Hamilton and Chervany [27] proposed a goalcentered view on effectiveness that is determined by comparing performance with objectives (i.e., effectiveness can be measured by comparing actual costs and bene<sup>fi</sup>ts with budgeted costs and expected bene<sup>fi</sup>ts). In this study, we take on this view and de<sup>fi</sup>ne effectiveness of a software development as the extent of satisfying a budget constraint.

Ravichandran and Rai [48] noted that aside from product quality, IS development quality also encompasses process efficiency which covers resource utilization and elimination of non-value-adding activities in the process. For human resources like workforce, Faraj and Sproull [22] suggested that expertise in software development teams must be managed and coordinated in order to leverage its potential, and knowledge workforce needs to be ef<sup>fi</sup>ciently utilized in order to achieve desired team performance. As a result, excess or under-utilized workforce is usually regarded as a loss to an organization [35]. In this study, we investigate ef<sup>fi</sup>ciency in terms of workforce utilization during the software project development as another process performance measurement.

## 2.4. Productivity and quality

Workforce issues in software project management have gained special awareness over the last two decades, especially as labor costs surpassed hardware costs for an information system. These issues are further complicated by the dynamics of iterative software development processes [50]. Since software development is knowledge work, the most critical resource for software projects is expertise (i.e., specialized skills and knowledge) of team members. Therefore, software project staf<sup>fi</sup>ng is one of the major problems that today's project managers have to address with care. Knowledge workers have to be conscientiously allocated to both development activities (e.g., design and coding) and quality enhancement activities (e.g., testing, structured walkthroughs, and inspection).

Productivity and quality are two major performance metrics of software projects. Software development effort estimation models have been developed and used in practice to facilitate schedule, size/ complexity measurement, cost reduction, productivity improvement, and quality control. Among them, the Constructive Cost Model (COCOMO) series of models proposed by Boehm [10] have been widely used. Using the source lines of code (SLOC) as input, the COCOMO models and its descendant Constructive Systems Engineering Cost Model (COSYSMO) have shown good predictive power. Other models that also rely on regression-based algorithms and SLOC include the Putnam Model, PRICE system, and SEER-SEM. Function points represent an alternative way to measure the amount of software functionality provided to the users. Using a different estimation method based on user requirements, function points are found highly correlated to source lines of code [3]. Additionally, function points cannot be automatically measured. As a result, the COCOMO models have been incorporated in more software development effort estimation software.

Aladwani [2] found that the productivity of project members plays a critical role in deciding the performance of software projects. His <sup>fi</sup>ndings con<sup>fi</sup>rm the importance of recruiting quali<sup>fi</sup>ed staff with suf<sup>fi</sup>cient technical skills in the design, coding, and testing methods to be employed. However, having capable workforce with high productivity comes with high costs in the form of high compensation. Therefore, we conjecture that project managers who pay special attention to schedules and costs associated with productivity of knowledge workers typically can have better administrative control over their software development processes and in turn can derive better performance.

On the other hand, Haag et al. [26] noted that the quality of software is emerging as a more critical issue than productivity. They further suggested that quality improvement techniques for the software development process can lead to “increased programmer productivity, fewer design changes, a reduction in the number of errors passed from one phase to the next, and quality software systems that satisfy customer requirements.” Krishnan et al. [37] found that quality improvements in software products increase productivity and save costs. In software development, it is estimated that about half of developers' time is spent on the discovery and correction of defects [24]. Quality assurance techniques, such as testing and inspection, are indispensable means to assure quality and reduce defects in software products. Testing refers to the simulated execution of completed software modules to see if their outcomes meet the anticipated speci<sup>fi</sup>cations. Inspection is the examination of source code for the purpose of defect exposure. It is believed that source code inspection can supplement testing efforts. Harter et al. [28] investigated the relationships between process maturity, product quality, cycle time, and costs for 30 software projects, and their <sup>fi</sup>ndings suggested that quality improvement, cycle time reduction, and cost decrease can be simultaneously achieved by reducing defects and rework in software production. Babu and Suresh [7] proposed a model to optimize the software quality subject to budget constraint. In this study, we investigate the iterative software development process along with workforce management issues in order to achieve the two aforementioned strategic objectives of productivity and quality.

## 3. Model formulation

## 3.1. Model basics

Software metrics can help link the development progress and software quality to the efforts of development and testing. Boehm [10] through the COCOMO models provided a solid foundation for software engineering economics and suggested two useful measurement constructs. The scale of software can be measured by the number of thousand lines of code, and the defect density of software can be represented by the number of errors per thousand lines of code. With these software metrics, we can understand better the relationship between the scale of software, the defect density of different releases of a software product, and the effort allocation. The ideal allocation is achieved when we minimize the time span of development and testing subject to budgetary constraints.

The assignment optimization is a mixed integer-programming problem by considering an assignment function that maps each task in the entire software development process to a knowledge worker. Mixed integer programming problems are NP-hard, which implies that exact methods pursuing optimal solutions of such problems are computationally prohibitive. Heuristics optimization has been frequently utilized to solve such combinatorial optimization problems. Genetic algorithm (GA) is one of the popular heuristics proposed, and it imitates the evolving of nature to select the best solution from the solution space [43]. Particle swarm optimization (PSO) algorithm proposed by Kennedy and Eberhart [34] is another useful technique. The PSO algorithm facilitates simple rules simulating bird <sup>fl</sup>ocking and has become a popular and effective optimization tool in business and engineering applications [21,51]. In this study, we adopt the PSO algorithm as the solution method for obtaining near-optimal solutions of our formulated model. More detailed descriptions about the background of and the rationale for using the PSO algorithm are provided in the online Appendix A.

In accordance with the industry practice, the iterative software development process is modeled to consist of three iterative releases, namely alpha, beta and <sup>fi</sup>nal. A common pool of knowledge workers is available for both development and testing tasks. Fig. 1 illustrates the iterative software development process to be modeled.

There are two types of <sup>fl</sup>ow in the software development model: code and defects <sup>fl</sup>ow, and workforce <sup>fl</sup>ow. The code and defects <sup>fl</sup>ow includes both <sup>fl</sup>ows of software code and its accompanying defects. In the iterative development process, the code <sup>fl</sup>ow starts with the requirement document, evolves in the iterative builds by adding functional features, and ends with the <sup>fi</sup>nal release with the speci<sup>fi</sup>ed and fully implemented function points. The knowledge workers allocated to each development build moderate the number of features added in each iteration. The size of software can be measured by thousands of delivered source instructions (KDSI).

The defects <sup>fl</sup>ow indicates the <sup>fl</sup>ow of defects introduced in the software. All the defects go through a testing procedure in the testing phase of the development process and, jointly with the effort allocated in the testing phase, decide the percentage of the defects discovered through the testing procedures. Subsequently, the bug-<sup>fi</sup>xing effort decides how many coding errors are removed from the code and how many of them remain residual defects and go into the next iteration. Moreover, the newly added features will also introduce their own defects. The defects in the software can be represented by defects per thousands of delivered source instructions.

It is noted that there can be different types of software errors, including fatal errors, incorrect-result errors, and non-robust errors. We also note that a single coding error may cause the crash of a software system, a logical error may cause malfunction of the software system, and a coding or logical error may cause any one of the three types of software error. In this study, we assume that the debugging process in any testing phase encompasses detections of any type of errors. That is, while inventing lines of codes, knowledge workers may detect simple coding errors or other logical errors.

The workforce <sup>fl</sup>ow indicates the knowledge worker assignment. The knowledge workers allocated to the development and testing tasks moderate the speed of development and error <sup>fi</sup>xing. Evidently, workforce is limited and subject to constraint, which is usually represented by budget or man-month in software projects. In this study, we use budget as the resource constraint. Knowledge workers (i.e., developers/testers) possess different productivities in coding and bug <sup>fi</sup>xing, and they receive speci<sup>fi</sup>c wage rates proportional to their skill levels.

## 3.2. Proposed model

In this study, we make the following assumptions. First, software is made up of classes or modules, and one developer or tester is assigned to the development or testing of each class. This is the case in practice when each class is well de<sup>fi</sup>ned, and this assumption holds when the system design is complete and the interface between classes is clearly speci<sup>fi</sup>ed. This approach of solo programming is appropriate when the system is large or the project has a tight deadline [18]. Second, the progress of development and testing within a software class is proportional to the time allocated and the productivity of developer or tester who takes on the task. Third, an error rate in a class is proportional to the scale of module and the error rate of the developer. Fourth, errors removed from a module depend on the testing time spent and the debugging productivity of the tester. Finally, knowledge workers are compensated based on their wage rates and total time they put into all the assigned tasks in the whole development process. The parameters and their de<sup>fi</sup>nitions are given in Table 1.

![](/api/attachments/B8YJFWYF/fulltext/images/af98018eb9f41f20fa89b9627a534b7cd5d6c6a5da8414e1854c04e094a4e492.jpg)  
Fig. 1. Software development process composed of alpha, beta and <sup>fi</sup>nal releases.

We de<sup>fi</sup>ne a task assignment matrix X as a matrix of $M \times W$ of the decision variables $x _ { i k } ,$ , where $x _ { i k } = 1$ if worker i is assigned to task k, and $x _ { i k } = 0$ otherwise $( 1 \leq i \leq M , 1 \leq k \leq W )$ and $\sum _ { i = 1 } ^ { M } x _ { i k } = 1$ indicating each task k is assigned to one and only one knowledge worker.

According to Fig. 1, there are six stages in the iterative software development cycle: alpha development, alpha testing, beta development, beta testing, <sup>fi</sup>nal development, and <sup>fi</sup>nal testing. Each stage has a certain number of tasks to complete (see Fig. 2), and it takes its own development or testing time and incurs its own development or testing cost.

<table><tr><td>Symbol</td><td>Meaning</td></tr><tr><td>M</td><td>The number of the knowledge workers</td></tr><tr><td>di</td><td>The coding development productivity of knowledge worker i (=1, 2, ..., M) in software development, measured by thousands of instructions coded per time unit (e.g., a day, a week)</td></tr><tr><td>ri</td><td>The error rate of knowledge worker i (=1, 2, ..., M) in software development, measured by the number of errors introduced per thousand of instructions coded per time unit</td></tr><tr><td>bi</td><td>The debugging productivity of knowledge worker i (=1, 2, ..., M) in software testing, measured by the percentage of errors removed per thousand of instructions per time unit</td></tr><tr><td>ci</td><td>The cost of knowledge worker i (=1, 2, ..., M) per time unit</td></tr><tr><td>Nα</td><td>The number of the modules in the alpha release</td></tr><tr><td>Nβ</td><td>The number of incremental modules added in the beta release</td></tr><tr><td>Nf</td><td>The number of incremental modules added in the final release</td></tr><tr><td>N</td><td>The total number of modules in the final release: N = Nα + Nβ + Nf</td></tr><tr><td>W</td><td>The total number of tasks: W = Nα + Nα + Nβ + (Nα + Nβ) + Nf + (Nα + Nβ + Nf)</td></tr><tr><td>sj</td><td>The size of software module j (=1, 2, ..., N) in thousands of instructions</td></tr><tr><td>ej</td><td>The error rate in module j (=1, 2, ..., N) per thousand of instructions</td></tr><tr><td>ej*</td><td>The final error rate in module j (=1, 2, ..., N) per thousand of instructions after the final testing</td></tr><tr><td>Eα</td><td>The maximum acceptable error rate in the modules of the alpha release</td></tr><tr><td>Eβ</td><td>The maximum acceptable error rate in modules of the beta release, Eα ≥ Eβ</td></tr><tr><td>Ef</td><td>The maximum acceptable error rate in modules of the final release, Eα ≥ Eβ ≥ Ef</td></tr><tr><td>B</td><td>The available budget</td></tr></table>

![](/api/attachments/B8YJFWYF/fulltext/images/5a42b93b5a1592f3d6712f39e239bf3974233c07e8eba759faa9a05493ebafc8.jpg)  
Fig. 2. Iterative software development cycle.

(I) Time of alpha phase development is the longest time of any worker among all workers spends in this phase:

$$
T _ {d \alpha} = \max \left(\sum_ {j = 1} ^ {N _ {\alpha}} x _ {1 k} s _ {j} / d _ {1}, \dots , \sum_ {j = 1} ^ {N _ {\alpha}} x _ {i k} s _ {j} / d _ {i}, \dots , \sum_ {j = 1} ^ {N _ {\alpha}} x _ {M k} s _ {j} / d _ {M}\right).\tag{1}
$$

The cost for alpha phase development is:

$$
C _ {d \alpha} = \sum_ {i = 1} ^ {M} c _ {i} \left(\sum_ {j = 1} ^ {N _ {\alpha}} x _ {i k} s _ {j} / d _ {i}\right).\tag{2}
$$

The error rate in module k after alpha phase development and before alpha phase testing is:

$$
e _ {j} = \sum_ {i = 1} ^ {M} r _ {i} x _ {i k}, 1 \leq k \leq N _ {\alpha}.\tag{3}
$$

We have $k = j$ in Eqs. (1), (2) and (3) above.

(II) Time of alpha phase testing is:

$$
T _ {t \alpha} = \max \left(\sum_ {j = 1} ^ {N _ {\alpha}} x _ {1 k} s _ {j} \left(e _ {j} - E _ {\alpha}\right) / b _ {1}, \dots , \sum_ {j = 1} ^ {N _ {\alpha}} x _ {M k} s _ {j} \left(e _ {j} - E _ {\alpha}\right) / b _ {M}\right).\tag{4}
$$

The cost for alpha phase testing is:

$$
C _ {t \alpha} = \sum_ {i = 1} ^ {M} c _ {i} \left(\sum_ {j = 1} ^ {N _ {\alpha}} x _ {i k} s _ {j} \left(e _ {j} - E _ {\alpha}\right) / b _ {i}\right).\tag{5}
$$

We have $k = j + N _ { \alpha }$ in Eqs. (4) and (5) above.

(III) Time of beta phase development is:

$$
T _ {d \beta} = \max \left(\sum_ {j = N _ {\alpha} + 1} ^ {N _ {\alpha} + N _ {\beta}} x _ {1 k} s _ {j} / d _ {1}, \dots , \sum_ {j = N _ {\alpha} + 1} ^ {N _ {\alpha} + N _ {\beta}} x _ {i k} s _ {j} / d _ {i}, \dots , \sum_ {j = N _ {\alpha} + 1} ^ {N _ {\alpha} + N _ {\beta}} x _ {M k} s _ {j} / d _ {M}\right).\tag{6}
$$

The cost for beta phase development is:

$$
C _ {d \beta} = \sum_ {i = 1} ^ {M} c _ {i} \left(\sum_ {j = N _ {\alpha} + 1} ^ {N _ {\alpha} + N _ {\beta}} x _ {i k} s _ {j} / d _ {i}\right).\tag{7}
$$

The error rate in module k after beta phase development and before beta phase testing is:

$$
e _ {j} = \left\{ \begin{array}{l l} E _ {\alpha}, & \text { if } 1 \leq j \leq N _ {\alpha} \\ \sum_ {i = 1} ^ {M} r _ {i} x _ {i k}, & \text { if } N _ {\alpha} + 1 \leq j \leq N _ {\alpha} + N _ {\beta} \end{array} \right..\tag{8}
$$

We have $k = j + N _ { \alpha }$ in Eqs. (6), (7) and (8) above.

(IV) Time of beta phase testing is:

$$
T _ {t \beta} = \max \left(\sum_ {j = 1} ^ {N _ {\alpha} + N _ {\beta}} x _ {1 k} s _ {j} \left(e _ {j} - E _ {\beta}\right) / b _ {1}, \dots , \sum_ {j = 1} ^ {N _ {\alpha} + N _ {\beta}} x _ {M k} s _ {j} \left(e _ {j} - E _ {\beta}\right) / b _ {M}\right).\tag{9}
$$

The cost for beta phase testing is:

$$
C _ {t \beta} = \sum_ {i = 1} ^ {M} c _ {i} \left(\sum_ {j = 1} ^ {N _ {\alpha} + N _ {\beta}} x _ {i k} s _ {j} \left(e _ {j} - E _ {\beta}\right) / b _ {i}\right).\tag{10}
$$

We have $k = j + 2 N _ { \alpha } + N _ { \beta }$ in Eqs. (9) and (10) above.

(V) Time of <sup>fi</sup>nal phase development is:

$$
T _ {d f} = \max \left(\sum_ {j = N _ {\alpha} + N _ {\beta} + 1} ^ {N _ {\alpha} + N _ {\beta} + N _ {f}} x _ {1 k} s _ {j} / d _ {1}, \dots , \sum_ {j = N _ {\alpha} + N _ {\beta} + 1} ^ {N _ {\alpha} + N _ {\beta} + N _ {f}} x _ {i k} s _ {j} / d _ {i}, \dots , \sum_ {j = N _ {\alpha} + N _ {\beta} + 1} ^ {N _ {\alpha} + N _ {\beta} + N _ {f}} x _ {M k} s _ {j} / d _ {M}\right).\tag{11}
$$

The cost for <sup>fi</sup>nal phase development is:

$$
C _ {d f} = \sum_ {i = 1} ^ {M} c _ {i} \left(\sum_ {j = N _ {\alpha} + N _ {\beta} + 1} ^ {N _ {\alpha} + N _ {\beta} + N _ {f}} x _ {i k} s _ {j} / d _ {i}\right).\tag{12}
$$

The error rate in module k after <sup>fi</sup>nal phase development and before <sup>fi</sup>nal phase testing is:

$$
e _ {j} = \left\{ \begin{array}{l l} E _ {\beta}, & \text { if } 1 \leq j \leq N _ {\alpha} + N _ {\beta} \\ \sum_ {i = 1} ^ {M} r _ {i} x _ {i k}, & \text { if } N _ {\alpha} + N _ {\beta} + 1 \leq j \leq N _ {\alpha} + N _ {\beta} + N _ {f} \end{array} \right..\tag{13}
$$

We have $k = j + 2 N _ { \alpha } + N _ { \beta }$ in Eqs. (11), (12) and (13) above. (VI) The time of <sup>fi</sup>nal phase testing is:

$$
T _ {t f} = \max \left(\sum_ {j = 1} ^ {N _ {\alpha} + N _ {\beta} + N _ {f}} x _ {1 k} s _ {j} \left(e _ {j} - E _ {f}\right) / b _ {1}, \dots , \sum_ {j = 1} ^ {N _ {\alpha} + N _ {\beta} + N _ {f}} x _ {M k} s _ {j} \left(e _ {j} - E _ {f}\right) / b _ {M}\right).\tag{14}
$$

The cost for <sup>fi</sup>nal phase testing is:

$$
C _ {t f} = \sum_ {i = 1} ^ {M} c _ {i} \left(\sum_ {j = 1} ^ {N _ {\alpha} + N _ {\beta} + N _ {f}} x _ {i k} s _ {j} \left(e _ {j} - E _ {f}\right) / b _ {i}\right).\tag{15}
$$

We have $k = j + 3 N _ { \alpha } + 2 N _ { \beta } + N _ { f }$ in Eqs. (14) and (15) above.Finally, the full optimization model is formulated as follows:

$$
\text { Minimize } T ^ {*} = T _ {d \alpha} + T _ {t \alpha} + T _ {d \beta} + T _ {t \beta} + T _ {d f} + T _ {t f}\tag{16}
$$

subject to

$$
C _ {d \alpha} + C _ {t \alpha} + C _ {d \beta} + C _ {t \beta} + C _ {d f} + C _ {t f} \leq B\tag{17}
$$

$$
e _ {j} ^ {*} \leq E _ {f}, \forall j = 1, \dots , N\tag{18}
$$

$$
\sum_ {i = 1} ^ {M} x _ {i k} = 1, 1 \leq k \leq W \quad (x _ {i k} = 0 \text { or } 1).\tag{19}
$$

The objective function minimizes the total development time of the software project. Constraint (17) ensures the optimal solution with shortest development time satisfy budget constraint B. That is, collective costs incurred during the software development process will not exceed the available <sup>fi</sup>nancial resource. Constraint (18) ensures the <sup>fi</sup>nal software product is within the speci<sup>fi</sup>ed quality requirement (i.e., the <sup>fi</sup>nal defect rate has to be within the maximum acceptable threshold E ). Finally, Constraint (19) makes sure that each task in the software development process be assigned to and completed by one knowledge worker.

## 4. Experiments

## 4.1. Particle swarm optimization

Particle swarm optimization (PSO) is motivated by the social behaviors of organisms such as bird <sup>fl</sup>ocking and <sup>fi</sup>sh schooling [34]. PSO is tied to evolutionary computation like genetic algorithms and evolutionary programming [39]. It combines local search methods for “neighborhood bests” with global search methods for the “global best.” PSO provides a population-based search procedure where individual particles change their positions with speed over time in a multidimensional search space. Through each <sup>fl</sup>ight, each particle adjusts its position according to its own experience as well as the experience of a neighboring particle for the quest of the best position (i.e., with the smallest objective value). We propose a meta-heuristic based on particle swarm optimization to derive solutions to the formulated problems (16)–(19).

A potential solution to the problem can be represented by a set of parameters that are joined together to form a particle as structured in Fig. 2. The length of a particle is

$$
W = N _ {\alpha} + N _ {\alpha} + N _ {\beta} + \left(N _ {\alpha} + N _ {\beta}\right) + N _ {f} + \left(N _ {\alpha} + N _ {\beta} + N _ {f}\right).
$$

In this study, we adopt a hybrid strategy for particle generations of the PSO. We conduct a pilot experiment for the proposed model using the PSO algorithm and a heuristic algorithm. In general, it is observed that the PSO algorithm performs better than the heuristic algorithm on the testing problems for both project duration and budget satisfaction. This implies that the PSO does a better job of substituting costs for duration time reduction. On the other hand, the heuristic algorithm is more computationally ef<sup>fi</sup>cient. In the pilot run, we also identify the variations of the derived optimal solutions from PSO. The result meets a priori expectation with small variations and this <sup>fi</sup>nding is critical since we can ensure not only the quality but also the stability of PSO optimal solutions.

## 4.2. Experimental setting

In this subsection, we describe the details of our simulation experiment. Simulation means driving a model of a real-world system with suitable inputs and observing the corresponding outputs [12]. The simulation approach is often used in social science when people have complex problems that cannot be solved by other means such as optimization, survey, and case study. Simulation allows social scientists to experiment with “arti<sup>fi</sup>cial society” and explore the implications of theories in ways not otherwise possible [23]. In our study, we mainly utilize the simulation approach for the purposes of discovery and formalization. That is, we use simulation to discover important relationships and principles from model [6]. More speci<sup>fi</sup>cally, with many possible variations of workforce composite, strategic focuses and workload ratios, we are keen on how these factors together impact completion time, budget consumption, and workforce utilization in the context of iterative software development. In the experiment, we consider the following experimental factors.

## 4.2.1. Workforce composite

Project managers cannot form a project team with a random pool of knowledge workers and then expect to complete the project timely and effectively. In our experiment, we test ten different types of workforce composite as an attempt to identify which type of composite can produce ideal results from a speci<sup>fi</sup>c perspective (i.e., timeliness, effectiveness, or ef<sup>fi</sup>ciency) with a speci<sup>fi</sup>c focus (i.e., productivity or quality). These composites are set based on different percentages of knowledge workers in a project team that possess a speci<sup>fi</sup>c combination of productivity level and error rate level. For example, in Composite 1, a project team has 30% of knowledge workers who have high coding productivity and low error rate, 20% of knowledge workers who have high coding productivity and medium error rate, 10% of knowledge workers who have high coding productivity and high error rate, and so on. Evidently, these composites are not exhaustive but used for our exploratory simulation for this study. Table 2 lists all ten workforce composites used in our experiment.

Note that for the combination of three levels of productivity (i.e., high, medium, and low) and three levels of error level (i.e., low, medium, and high), there should have been nine possible types of knowledge workers (see Table 3). However, we only consider six types of knowledge workers in Table 2 in forming workforce composites because it is reasonable to assume that <sup>fi</sup>rms will not recruit or retain the other three types (i.e., high error level with low productivity, high error level with medium productivity, and medium error level with low productivity) of knowledge workers.

## 4.2.2. Productivity and error rate level

Different knowledge workers possess different levels of competence in performing a speci<sup>fi</sup>c task. For software development, we conjecture that a knowledge worker i has a certain productivity level of coding $d _ { i } ,$ a certain error rate level $r _ { i } ,$ and a certain productivity level of debugging $b _ { i \cdot }$ In our experiment, we categorize these competencies into three levels — high, medium, and low (see Table 4). For example, a worker with high coding productivity, low coding error rate, and medium debugging productivity can code 8 to 10 thousand software instructions per time unit, incur only 2 to 4 errors per thousand of coded instructions, and detect and correct 50 to 70% of errors per thousand of coded instructions per time unit.

## 4.2.3. Strategic focus

It is reasonable to justify that different knowledge workers will be compensated differently based on their competency (i.e., productivity of coding and debugging in the context of software development). It will also cost a software project differently when knowledge workers incur different levels of errors. Therefore, we conjecture that the cost $c _ { i }$ of hiring a knowledge worker per time unit is determined by compensating her for her productivity of coding/debugging and by penalizing her for her coding error rate (i.e., $c _ { i } = a _ { 1 } d _ { i } - a _ { 2 } r _ { i } + a _ { 3 } b _ { i } )$ . The three coef<sup>fi</sup>cients $a _ { 1 } , a _ { 2 } ,$ , and $a _ { 3 }$ can be set as different weights to represent different strategic focuses on productivity or quality for a software project. For example, by setting $a _ { 1 }$ higher, the focus is on productivity (i.e., promoting coding development productivity). On the other hand, by setting $a _ { 2 }$ and $a _ { 3 }$ higher, the focus is on quality (i.e., penalizing errors and promoting debugging productivity).

Workforce composite.

<table><tr><td></td><td> $Hd_{i}-Lr_{i}$ </td><td> $Hd_{i}-Mr_{i}$ </td><td> $Hd_{i}-Hr_{i}$ </td><td> $Md_{i}-Lr_{i}$ </td><td> $Md_{i}-Mr_{i}$ </td><td> $Ld_{i}-Lr_{i}$ </td></tr><tr><td>Composite 1</td><td>30%</td><td>20%</td><td>10%</td><td>20%</td><td>10%</td><td>10%</td></tr><tr><td>Composite 2</td><td>10%</td><td>10%</td><td>10%</td><td>20%</td><td>20%</td><td>30%</td></tr><tr><td>Composite 3</td><td>10%</td><td>20%</td><td>30%</td><td>10%</td><td>20%</td><td>10%</td></tr><tr><td>Composite 4</td><td>30%</td><td>30%</td><td>10%</td><td>10%</td><td>10%</td><td>10%</td></tr><tr><td>Composite 5</td><td>30%</td><td>10%</td><td>10%</td><td>30%</td><td>10%</td><td>10%</td></tr><tr><td>Composite 6</td><td>10%</td><td>10%</td><td>30%</td><td>10%</td><td>10%</td><td>30%</td></tr><tr><td>Composite 7</td><td>10%</td><td>30%</td><td>10%</td><td>30%</td><td>10%</td><td>10%</td></tr><tr><td>Composite 8</td><td>20%</td><td>20%</td><td>10%</td><td>20%</td><td>20%</td><td>10%</td></tr><tr><td>Composite 9</td><td>10%</td><td>20%</td><td>10%</td><td>20%</td><td>20%</td><td>20%</td></tr><tr><td>Composite 10</td><td>10%</td><td>20%</td><td>20%</td><td>20%</td><td>20%</td><td>10%</td></tr></table>

Table 3  
Possible types of workforce competence combination.

<table><tr><td rowspan="2"></td><td colspan="4"> $d_i$  (development productivity)</td></tr><tr><td></td><td>H</td><td>M</td><td>L</td></tr><tr><td rowspan="3"> $r_i$  (error rate)</td><td>L</td><td>O</td><td>O</td><td>O</td></tr><tr><td>M</td><td>O</td><td>O</td><td>X</td></tr><tr><td>H</td><td>O</td><td>X</td><td>X</td></tr></table>

O: Six types considered in this study; X: Three types are not considered in this study.

In our experiment, we simulate eight strategies with focus on productivity, quality, or both (see Table 5).

For example, Strategy 1 has high coef<sup>fi</sup>cient $a _ { 1 }$ on d<sub>i</sub> (coding productivity) and we term this strategy high-productivity focused (Hp). Strategy 2 also has high coef<sup>fi</sup>cient $a _ { 1 }$ on $d _ { i }$ (coding productivity) but at the same time has extra weight $a _ { 2 }$ on $r _ { i }$ (error rate). We therefore call Strategy 2 high-productivity and moderate-quality focused (Hp–Mq). Strategy 3 has a relatively lower weight $a _ { 1 }$ on $d _ { i }$ than Strategy 1, and hence it is termed moderate-productivity focused (Mp). Strategy 5 has high coef<sup>fi</sup>- cient $a _ { 2 }$ on r (error rate) and has extra weight $a _ { 3 }$ on $b _ { i }$ (debugging productivity). We term Strategy 5 high-quality focused (Hq). Strategies 6 and 7 both have medium coef<sup>fi</sup>cient $a _ { 2 }$ on $r _ { i }$ (error rate) and have extra weight $a _ { 3 }$ on $b _ { i }$ (debugging productivity). We term Strategies 6 and 7 moderate-quality focused $\mathrm { M q } - 1$ 1 and Mq-2, respectively. Strategy 4 has both medium coef<sup>fi</sup>cient a<sub>1</sub> on d<sub>i</sub> (coding productivity) and medium coef<sup>fi</sup>cient $a _ { 2 }$ on $r _ { i }$ (error rate). We therefore term Strategy 4 moderateproductivity and moderate-quality focused (Mp–Mq), and we list it in both productivity focus and quality focus categories. Finally, Strategy 8 has equal weights a , a and a for $d _ { i } ,$ r and $b _ { i } ,$ and it is termed equal focus.

## 4.2.4. Workload ratio

Workload ratio indicates the number of tasks that a knowledge worker needs to complete through all three phases during the software development process. The larger the ratio is, the heavier the burden is put on a knowledge worker for performing tasks and hence the higher the worker utilization will be. In this sense, workload ratio is related to “workforce slack” and “workforce utilization.” Usually excess workforce is regarded as a loss to an organization [35]. However, unlike other capital investments, slack of workforce can have a positive externality effect on organization in the future. Workforce slack (or unused human resource capacity) can offer opportunities to further train employees for anticipated or new knowledge set [15]. Slack can thus transform the excess resources to knowledge acquisition activities of workers, improve future worker productivity, and provide <sup>fl</sup>exibility for an organization. In this study, we de<sup>fi</sup>ne the term workload ratio (WLR) as the average number of tasks assigned to one knowledge worker and is equivalent to W/M (where W is the number of tasks and M is the number of workers). We explore whether workload ratio impacts software development process and outcome while interacting it with previously mentioned factors. In the experiment, we simulate three different workload ratios: 10, 20, and 30 (i.e., W/M = 1000/100, 2000/100, and 3000/100).

Productivity and error rate of knowledge workers.

<table><tr><td></td><td>Low</td><td>Medium</td><td>High</td></tr><tr><td> $d_{i}$ (coding productivity – number of KDSI)</td><td> $2 < d_{i} <= 4$ </td><td> $5 < d_{i} <= 7$ </td><td> $8 < d_{i} <= 10$ </td></tr><tr><td> $r_{i}$ (error rate – number of errors in KDSI)</td><td> $2 < r_{i} <= 4$ </td><td> $5 < r_{i} <= 7$ </td><td> $8 < r_{i} <= 10$ </td></tr><tr><td> $b_{i}$ (debugging productivity – percentageof errors that are detected and corrected)</td><td> $2 < b_{i} <= 4$ </td><td> $5 < b_{i} <= 7$ </td><td> $8 < b_{i} <= 10$ </td></tr></table>

Table 5  
Strategic focuses by assigning coef<sup>fi</sup>cients/weights on worker compensation.

<table><tr><td>Coefficients</td><td></td><td> $a_{1}$ </td><td> $a_{2}$ </td><td> $a_{3}$ </td></tr><tr><td rowspan="4">Productivity focus</td><td>Strategy 1 (Hp)</td><td>100</td><td>10</td><td>10</td></tr><tr><td>Strategy 2 (Hp-Mq)</td><td>100</td><td>20</td><td>10</td></tr><tr><td>Strategy 3 (Mp)</td><td>30</td><td>10</td><td>10</td></tr><tr><td>Strategy 4 (Mp-Mq)</td><td>30</td><td>20</td><td>10</td></tr><tr><td rowspan="4">Quality focus</td><td>Strategy 5 (Hq)</td><td>10</td><td>30</td><td>20</td></tr><tr><td>Strategy 6 (Mq-1)</td><td>10</td><td>20</td><td>20</td></tr><tr><td>Strategy 7 (Mq-2)</td><td>10</td><td>20</td><td>30</td></tr><tr><td>Strategy 4 (Mp-Mq)</td><td>30</td><td>20</td><td>10</td></tr><tr><td>Equal focus</td><td>Strategy 8</td><td>10</td><td>10</td><td>10</td></tr></table>

## 4.2.5. PSO parameters

PSO involves a few parameters which may affect the performance of the algorithm being implemented. These parameters include swarm size, inertia weight, and acceleration constants. The ideal swarm size is the optimal number of particles that can work together to <sup>fi</sup>nd a quality-accepted solution most ef<sup>fi</sup>ciently (i.e., consuming the least computational efforts). We refer to this optimal number of particles as the maximum synergism. Various numbers of particles have been speci<sup>fi</sup>ed for the proposed PSO method on a set of testing problems in order to obtain the optimal setting. The inertia weight indicates the momentum that moves the current particle to the same direction as the previous <sup>fl</sup>ight of the particle. The philosophy of this progressive design resembles the classic direct search method such as the pattern move by Hooke and Jeeves [31]. The two acceleration constants control the cognition degrees to which the individual best and the global best experience, respectively. They are usually set to the same value or different values proportional to the <sup>fi</sup>tness of the respective experiences. The inertia weight and the acceleration constants should hold a mathematical relation in order to avoid explosion of the <sup>fl</sup>ight distance. Clerc and Kennedy [17] proposed a mathematical formula for these parameters that guarantees the convergence of the search trajectory. In this study, we employ their settings for conducting our experiments. A generic simulation program of the PSO-based algorithm was developed in C++. The simulation platform of the experiments is a personal computer equipped with a 2.4 GHz CPU and 248 MB RAM.

## 5. Results and discussions

Before presenting the simulation results, we <sup>fi</sup>rst describe the steps taken to ensure internal validity of the simulation model. First, the simulation program was coded and veri<sup>fi</sup>ed by the authors, and code walkthroughs were performed to ensure correctness. Second, simple base cases with known answers were tested for validation purposes. We also recorded and observed intermediate output values to verify that the program executed as anticipated. Finally, we conducted a pilot experiment to test the properties of our PSO algorithm with a hybrid strategy.

We also address external validity issues with additional procedures. First, we referred to extant IS literature to set the value ranges for parameters used in our simulation. When de<sup>fi</sup>nitive guidelines from the IS literature were not available, we then looked for and used practitioner and academic literature from other related disciplines such as computer science and project management. Second, to ensure robustness, numerous parameter ranges which are different from the ones used for the main simulation were adopted and tested for sensitivity analyses. These additional results showed that our model is robust to variations in parameter values and the relative performance of the workforce composites and strategies remains stable. Finally, we compared our <sup>fi</sup>ndings with those from studies in other contexts to check for abnormal outcomes.

## 5.1. Development time — Timeliness

We <sup>fi</sup>rst present and discuss the results from the timeliness perspective. Tables 6 and 7 show the outcomes associated with the best and worst timeliness, respectively, for software project completion. In general, Composite 4 (which has 70% of workers with high productivity) is the best composite to achieve timeliness (or shortest software development time) when a <sup>fi</sup>rm focuses on either development productivity or quality across different workload ratios. In other words, when a <sup>fi</sup>rm builds its workforce with the majority of workers “championing” coding productivity and at the same time having low or moderate error rates, the <sup>fi</sup>rm can achieve best timeliness of software development.

Best timeliness — Shortest development time.

<table><tr><td colspan="5">Development productivity focusBest timeliness — Shortest development time</td><td rowspan="2">Equal focus</td></tr><tr><td>Strategy</td><td>(Hp)</td><td>(Hp–Mq)</td><td>(Mp)</td><td>(Mp–Mq)</td></tr><tr><td>WLR: 10</td><td>Comp 4</td><td>Comp 4, 1</td><td>Comp 4</td><td>Comp 4</td><td>Comp 4</td></tr><tr><td>WLR: 20</td><td>Comp 4</td><td>Comp 4</td><td>Comp 4, 1</td><td>Comp 4</td><td>Comp 4</td></tr><tr><td>WLR: 30</td><td>Comp 4</td><td>Comp 4</td><td>Comp 4, 1</td><td>Comp 4</td><td>Comp 4</td></tr><tr><td colspan="5">Quality (error rate) focusBest timeliness — Shortest development time</td><td rowspan="2">Equal focus</td></tr><tr><td>Strategy</td><td>(Hq)</td><td>(Mq-1)</td><td>(Mq-2)</td><td>(Mp–Mq)</td></tr><tr><td>WLR: 10</td><td>Comp 4</td><td>Comp 4</td><td>Comp 4, 1</td><td>Comp 4</td><td>Comp 4</td></tr><tr><td>WLR: 20</td><td>Comp 4</td><td>Comp 4</td><td>Comp 4</td><td>Comp 4</td><td>Comp 4</td></tr><tr><td>WLR: 30</td><td>Comp 4</td><td>Comp 4</td><td>Comp 4</td><td>Comp 4</td><td>Comp 4</td></tr></table>

It is not tautological that Composite 4 in general results in not only best timeliness but also best workforce utilization (see Table 8). That is, a <sup>fi</sup>rm which develops software projects in shortest time usually demonstrates best utilization of its workforce; this is the case across different workload ratios. This <sup>fi</sup>nding implies that a <sup>fi</sup>rm should hire enough best workers (champions) in software development but not try to build as large a workforce as possible. In other words, the quality of workforce should take precedence over the quantity of workforce.

It is also not surprising that Composite 4 does not result in worst effectiveness in terms of incurring high development costs (see Table 11). This implies that when possible, a <sup>fi</sup>rm should hire enough best workers (champions) in software development even though the <sup>fi</sup>rm needs to compensate these workers individually more.

Table 7 shows that when workload ratio is low and a <sup>fi</sup>rm is focusing on development productivity, Composite 2 results in the longest development time (worst timeliness). This result is expected since Composite 2 has a relatively low percentage of workers who have high productivity (30%). When workload ratio is low and the focus is on development productivity, a <sup>fi</sup>rm without suf<sup>fi</sup>cient “champions” in the workforce is likely to incur longer development time. On the other hand, when workload ratio is low and a <sup>fi</sup>rm is focusing on quality control (reducing error rate), Composite 6 bears the longest development time (worst timeliness). This result is also expected since Composite 6 has a relatively low percentage of workers (20%) who have high productivity and low or moderate error rates, and it has a relatively high percentage of workers who have low productivity with low error rates. When workload ratio is low and a <sup>fi</sup>rm is focusing on quality control, a <sup>fi</sup>rm tends to utilize workers who have low or moderate error rates. Under Composite 6, these workers possess lower productivity and hence cause timeliness issues. Lastly, when workload ratio is low and a <sup>fi</sup>rm is focusing on neither development productivity nor quality control, Composite 6 again results in the longest development time (worst timeliness). This is because under Composite 6, a <sup>fi</sup>rm has a high tendency to utilize workers who either have high productivity with high error rate or have low productivity with low error rate. In either case, the <sup>fi</sup>rm is likely to suffer from long development time.

Worst timeliness — Longest development time.

<table><tr><td colspan="5">Development productivity focusWorst timeliness — Longest development time</td><td rowspan="2">Equal focus</td></tr><tr><td>Strategy</td><td>(Hp)</td><td>(Hp–Mq)</td><td>(Mp)</td><td>(Mp–Mq)</td></tr><tr><td>WLR: 10</td><td>Comp 2, 6, 10</td><td>Comp 6</td><td>Comp 2</td><td>Comp 2</td><td>Comp 6</td></tr><tr><td>WLR: 20</td><td>Comp 10, 2</td><td>Comp 10</td><td>Comp 2, 10, 6</td><td>Comp 10</td><td>Comp 10</td></tr><tr><td>WLR: 30</td><td>Comp 2</td><td>Comp 2, 10</td><td>Comp 2</td><td>Comp 2</td><td>Comp 2</td></tr><tr><td colspan="5">Quality (error rate) focusWorst timeliness — Longest development time</td><td rowspan="2">Equal focus</td></tr><tr><td>Strategy</td><td>(Hq)</td><td>(Mq-1)</td><td>(Mq-2)</td><td>(Mp–Mq)</td></tr><tr><td>WLR: 10</td><td>Comp 6</td><td>Comp 6</td><td>Comp 6, 10</td><td>Comp 2</td><td>Comp 6</td></tr><tr><td>WLR: 20</td><td>Comp 2</td><td>Comp 10</td><td>Comp 10</td><td>Comp 10</td><td>Comp 10</td></tr><tr><td>WLR: 30</td><td>Comp 2</td><td>Comp 2, 10</td><td>Comp 2</td><td>Comp 2</td><td>Comp 2</td></tr></table>

When workload ratio is high, Composite 2 in general causes the longest development time. When workload ratio is high, a <sup>fi</sup>rm is almost certain to assign most, if not all, workers to tasks. Under Composite 2, a <sup>fi</sup>rm has a relatively low percentage of workers who have high productivity (i.e., a <sup>fi</sup>rm with few “champions” in the workforce) and is likely to incur longer development time when many “marginal workers” are assigned to tasks. This result holds true across different strategies (i.e., development productivity focus, quality focus, or equal focus).

When workload ratio is medium, Composite 10 in general causes the longest development time. This is an interesting observation and deserves scrutiny. Composite 10 comprises the workforce where there is no clear concentration on “champions” or “marginal workers.” Under this composite, a <sup>fi</sup>rm does not have the luxury of assigning “champions” to tasks or not assigning “marginal workers” to tasks. Therefore, when workload ratio is medium, a <sup>fi</sup>rm is likely to “randomly” assign most, if not all, workers to tasks. As a result, this composite ends up having the worst timeliness.

## 5.2. Idle time — Workforce utilization

We next present and discuss the results from the ef<sup>fi</sup>ciency perspective. Tables 8 and 9 show the outcomes associated with the best and worst workforce utilization, respectively, in terms of average idle time.

The results concerning the average idle time of workers (i.e., workforce utilization) generally indicate that Composite 4 is among the composites which incur shortest average idle time (i.e., best workforce utilization) for different strategies and across different workload ratios. That is, a <sup>fi</sup>rm which has a higher percentage of workforce with high productivity is likely to have fewer workers idle. This result implies that a <sup>fi</sup>rm can better utilize its workforce by assigning more tasks to those “champions.” While these champions are completing more tasks in an ef<sup>fi</sup>cient way, other workers can perform other assigned tasks in a slower pace. As a result, the <sup>fi</sup>rm has fewer idle workers during the software development process.

Other composites that show best workforce utilization are Composites 1, 5, 7, and 8. The common con<sup>fi</sup>guration for these composites is that at least 40% of workforce is made up of developers with high productivity and low to moderate error rate (champions). Therefore, the analogy presented above also holds true for them.

In general, the patterns of composites that have worst workforce utilization (i.e., longest idle time) re<sup>fl</sup>ect the patterns of composites that have worst timeliness (i.e., longest development time). Composite 6 again seems to have poor workforce utilization for different <sup>fi</sup>rm's strategies and across all workload ratios. Composite 6 has a relatively low percentage of workers with high productivity and low or moderate error rates, and thus it is likely for this <sup>fi</sup>rm to have a higher percentage of workers with low productivity not assigned to any tasks. On the other hand, Composite 6 also has a relatively high percentage of workers with low productivity and low error rates. When a <sup>fi</sup>rm focuses on quality, this type of workers will be assigned to work <sup>fi</sup>rst, leaving little room for workers with high error rate to be assigned. All these factors lead to poor workforce utilization.

Table 8  
Best workforce utilization — Shortest idle time.

<table><tr><td colspan="5">Development productivity focusBest workforce utilization - Shortest idle time</td><td rowspan="2">Equal focus</td></tr><tr><td>Strategy</td><td>(Hp)</td><td>(Hp-Mq)</td><td>(Mp)</td><td>(Mp-Mq)</td></tr><tr><td>WLR: 10</td><td>Comp 4</td><td>Comp 1, 4</td><td>Comp 4</td><td>Comp 4</td><td>Comp 4, 1</td></tr><tr><td>WLR: 20</td><td>Comp 1, 4, 8</td><td>Comp 5, 8</td><td>Comp 4, 1, 8, 7</td><td>Comp 4</td><td>Comp 5, 4, 1</td></tr><tr><td>WLR: 30</td><td>Comp 5</td><td>Comp 7, 4, 1, 8, 5</td><td>Comp 8, 4, 5, 1</td><td>Comp 1, 4, 5</td><td>Comp 4, 3</td></tr><tr><td colspan="5">Quality (error rate) focusBest workforce utilization - Shortest idle time</td><td rowspan="2">Equal focus</td></tr><tr><td>Strategy</td><td>(Hq)</td><td>(Mq-1)f</td><td>(Mq-2)</td><td>(Mp-Mq)</td></tr><tr><td>WLR: 10</td><td>Comp 4</td><td>Comp 4, 7, 1</td><td>Comp 1, 4, 5, 7</td><td>Comp 4</td><td>Comp 4, 1</td></tr><tr><td>WLR: 20</td><td>Comp 4, 5, 7</td><td>Comp 4, 5, 7</td><td>Comp 5, 1, 7, 3, 8</td><td>Comp 4</td><td>Comp 5, 4, 1</td></tr><tr><td>WLR: 30</td><td>Comp 5, 1, 4</td><td>Comp 4, 7, 1</td><td>Comp 4</td><td>Comp 1, 4, 5</td><td>Comp 4, 3</td></tr></table>

## 5.3. Development cost — Effectiveness

Next we present and discuss the results from the effectiveness perspective. Tables 10 and 11 show the outcomes associated with the best and worst effectiveness, respectively, in terms of development cost.

It is interesting to note that in Table 10 all composites incur similar development cost when a <sup>fi</sup>rm focuses on development productivity. The reason may be that with tight budget limit, there is not much opportunity to realize signi<sup>fi</sup>cant cost savings while still paying for high productivity compensation. For other <sup>fi</sup>rm's strategies (i.e., quality focus and equal focus), Composites 3, 6, and 10 are the ones that incur relatively low development costs and hence achieve better effectiveness. For Composites 3 and 10, they have the two highest percentages of workers with high or medium error rates and at the same time don't have “champions.” This indicates that a <sup>fi</sup>rm might try to avoid these error-prone workers by assigning other workers who are not only less productive but also less expensive. As a result, a <sup>fi</sup>rm will actually incur less development costs. On the other hand, Composite 6 has a relatively high percentage of workers with high productivity and high error rates, and it also has a relatively high percentage of workers with low productivity and low error rates. Under this composite, it is likely that more workers with low error rates and low productivity who are hence less expensive will be assigned to tasks.

By the same token, in Table 11, all composites incur similar development cost when a <sup>fi</sup>rm focuses on development productivity. The reason again may be that with tight budget limit, there is little room for cost improvement while still paying for high productivity compensation. For other strategies (i.e., quality focus and equal focus), Composite 5 seems to stand out as the least effective one with high development costs. Composite 5 not only has high percentage of “champions” who has high productivity but also has high percentage of workers who has medium productivity and low error rate. Therefore, under Composite 5, workers who are champions or have medium productivity are more likely to be assigned to tasks, resulting in higher development cost due to higher workers' compensation.

Worst workforce utilization — Longest idle time.

<table><tr><td colspan="5">Development productivity focusWorst workforce utilization — Longest idle time</td><td rowspan="2">Equal focus</td></tr><tr><td>Strategy</td><td>(Hp)</td><td>(Hp-Mq)</td><td>(Mp)</td><td>(Mp-Mq)</td></tr><tr><td>WLR: 10</td><td>Comp 6</td><td>Comp 6</td><td>Comp 2</td><td>Comp 2, 6</td><td>Comp 6</td></tr><tr><td>WLR: 20</td><td>Comp 6</td><td>Comp 10, 9, 6</td><td>Comp 6</td><td>Comp 6, 10</td><td>Comp 9, 10</td></tr><tr><td>WLR: 30</td><td>Comp 2</td><td>Comp 6</td><td>Comp 2, 6</td><td>Comp 2</td><td>Comp 6</td></tr><tr><td colspan="5">Quality (error rate) focusWorst workforce utilization — Longest idle time</td><td rowspan="2">Equal focus</td></tr><tr><td>Strategy</td><td>(Hq)</td><td>(Mq-1)</td><td>(Mq-2)</td><td>(Mp-Mq)</td></tr><tr><td>WLR: 10</td><td>Comp 6</td><td>Comp 6</td><td>Comp 6</td><td>Comp 2, 6</td><td>Comp 6</td></tr><tr><td>WLR: 20</td><td>Comp 6</td><td>Comp 6, 10</td><td>Comp 6</td><td>Comp 6, 10</td><td>Comp 9, 10</td></tr><tr><td>WLR: 30</td><td>Comp 6</td><td>Comp 6, 10</td><td>Comp 6</td><td>Comp 2</td><td>Comp 6</td></tr></table>

## 5.4. Other observations

In all composites, when workload ratios increase, software development time becomes longer. This result is expected since it takes longer to develop software when there are more tasks. It is interesting to observe that the increase of workload and the increase of development time are not proportional. For example, when there are three times more workload, it approximately only leads to twice more development time. This implies that development timeliness tends to be a more serious problem when workload is light for a <sup>fi</sup>rm. It also suggests that a <sup>fi</sup>rm should impose higher workload ratio to achieve better development timeliness instead of through hiring more workers.

On the other hand, in all composites, when workload ratios increase, workers' average idle time decreases. This result is expected because when there are more tasks needed to be completed, even less competent workers will be assigned to work on tasks. When workload ratio is low, a <sup>fi</sup>rm tends to allocate the workers who are more competent in an attempt to accelerate the software development process. Less competent workers will be likely left out to do other tasks or receive training, thus causing high average idle time of the workforce. It is also interesting to note that the relationship between the increase in workload ratio and the decrease in idle time is approximately linear.

## 5.5. Cross-strategy analysis

We further investigate how a speci<sup>fi</sup>c workforce composite fares across different strategic focuses under three different workload scenarios. We use Composite 4 and Composite 5 for this analysis since they are the ones that perform better in most cases that we discussed above. Our simulation results point to interesting implications (see Tables 12 and 13).

Table 10  
Best effectiveness — Least development cost.

<table><tr><td colspan="5">Development productivity focusBest effectiveness – Least development cost</td><td rowspan="2">Equal focus</td></tr><tr><td>Strategy</td><td>(Hp)</td><td>(Hp–Mq)</td><td>(Mp)</td><td>(Mp–Mq)</td></tr><tr><td>WLR: 10</td><td>Comp 3(All Similar)</td><td>Comp 3(All Similar)</td><td>Comp 3</td><td>Comp 3</td><td>Comp 3, 10</td></tr><tr><td>WLR: 20</td><td>Comp 4(All Similar)</td><td>Comp 3(All Similar)</td><td>Comp 3, 10, 9, 8</td><td>Comp 6</td><td>Comp 6, 3</td></tr><tr><td>WLR: 30</td><td>Comp 3(All Similar)</td><td>Comp 3(All Similar)</td><td>Comp 3</td><td>Comp 3</td><td>Comp 10</td></tr><tr><td colspan="5">Quality (error rate) focusBest effectiveness – Least development cost</td><td rowspan="2">Equal focus</td></tr><tr><td>Strategy</td><td>(Hq)</td><td>(Mq-1)</td><td>(Mq-2)</td><td>(Mp–Mq)</td></tr><tr><td>WLR: 10</td><td>Comp 3</td><td>Comp 3</td><td>Comp 3</td><td>Comp 3</td><td>Comp 3, 10</td></tr><tr><td>WLR: 20</td><td>Comp 6, 3</td><td>Comp 6</td><td>Comp 6, 3</td><td>Comp 6</td><td>Comp 6, 3</td></tr><tr><td>WLR: 30</td><td>Comp 3</td><td>Comp 10</td><td>Comp 10</td><td>Comp 3</td><td>Comp 10</td></tr></table>

Table 13  
Table 11  
Worst effectiveness — Most development cost.

<table><tr><td colspan="5">Development productivity focusWorst effectiveness – Most development cost</td><td rowspan="2">Equal focus</td></tr><tr><td>Strategy</td><td>(Hp)</td><td>(Hp–Mq)</td><td>(Mp)</td><td>(Mp–Mq)</td></tr><tr><td>WLR: 10</td><td>Comp 2 (all similar)</td><td>Comp 6 (all similar)</td><td>Comp 2</td><td>Comp 5</td><td>Comp 5</td></tr><tr><td>WLR: 20</td><td>Comp 6 (all similar)</td><td>Comp 10 (all similar)</td><td>Comp 5, 1, 2</td><td>Comp 1, 5</td><td>Comp 5, 10, 4, 1, 9</td></tr><tr><td>WLR: 30</td><td>Comp 2 (all similar)</td><td>Comp 5 (all similar)</td><td>Comp 5</td><td>Comp 5</td><td>Comp 5, 1</td></tr><tr><td colspan="5">Quality (error rate) focusWorst effectiveness – Most development cost</td><td rowspan="2">Equal focus</td></tr><tr><td>Strategy</td><td>(Hq)</td><td>(Mq-1)</td><td>(Mq-2)</td><td>(Mp–Mq)</td></tr><tr><td>WLR: 10</td><td>Comp 5, 1</td><td>Comp 5</td><td>Comp 5</td><td>Comp 5</td><td>Comp 5</td></tr><tr><td>WLR: 20</td><td>Comp 5</td><td>Comp 5, 4</td><td>Comp 5, 4, 1</td><td>Comp 1, 5</td><td>Comp 5, 10, 4, 1, 9</td></tr><tr><td>WLR: 30</td><td>Comp 5, 1</td><td>Comp 5</td><td>Comp 5</td><td>Comp 5</td><td>Comp 5, 1</td></tr></table>

First, strategies focused on productivity do not necessarily yield shorter development time as expected. Instead, strategies focused on quality perform better from all three perspectives of software development on time, cost, and idle ratio. In particular, Strategy 5 with high quality focus actually yields shortest development time, lowest development cost, and highest workforce utilization when workload ratio is low. Even when workload ratio is high, Strategy 5 still outperforms strategies with productivity focus on total time and total cost. This <sup>fi</sup>nding echoes the conclusion of Harter and Slaughter [29] that quality improvement in software development not only reduces development costs but also helps with infrastructure activities like data integration and con<sup>fi</sup>guration management which can save development time. Our results imply that project managers should emphasize quality <sup>fi</sup>rst for software development instead of productivity. That is, higher

## Table 12

Cross-strategy performance comparison with workforce Composite 4.

<table><tr><td colspan="2"></td><td>Total time</td><td>Total cost</td><td>Idle ratio</td></tr><tr><td colspan="5">Composite 4 (WLR = 10)</td></tr><tr><td rowspan="4">Productivity focus</td><td>Strategy 1 (Hp)</td><td>18.86</td><td>1,130,488</td><td>0.416379</td></tr><tr><td>Strategy 2 (Hp-Mq)</td><td>20.05</td><td>1,067,046</td><td>0.424724</td></tr><tr><td>Strategy 3 (Mp)</td><td>18.99</td><td>370,280</td><td>0.417276</td></tr><tr><td>Strategy 4 (Mp-Mq)</td><td>18.79</td><td>292,957</td><td>0.409779</td></tr><tr><td rowspan="4">Quality focus</td><td>Strategy 5 (Hq)</td><td>18.71</td><td>118,984</td><td>0.402154</td></tr><tr><td>Strategy 6 (Mq-1)</td><td>19.76</td><td>176,162</td><td>0.421260</td></tr><tr><td>Strategy 7 (Mq-2)</td><td>20.44</td><td>289,595</td><td>0.434702</td></tr><tr><td>Strategy 4 (Mp-Mq)</td><td>18.79</td><td>292,957</td><td>0.409779</td></tr><tr><td>Equal focus</td><td>Strategy 8</td><td>19.77</td><td>144,182</td><td>0.422543</td></tr><tr><td colspan="5">Composite 4 (WLR = 20)</td></tr><tr><td rowspan="4">Productivity focus</td><td>Strategy 1 (Hp)</td><td>27.46</td><td>1,873,360</td><td>0.236507</td></tr><tr><td>Strategy 2 (Hp-Mq)</td><td>29.15</td><td>1,836,797</td><td>0.231583</td></tr><tr><td>Strategy 3 (Mp)</td><td>27.63</td><td>608,912</td><td>0.240673</td></tr><tr><td>Strategy 4 (Mp-Mq)</td><td>27.10</td><td>483,033</td><td>0.225959</td></tr><tr><td rowspan="4">Quality focus</td><td>Strategy 5 (Hq)</td><td>29.19</td><td>223,267</td><td>0.210420</td></tr><tr><td>Strategy 6 (Mq-1)</td><td>28.40</td><td>321,714</td><td>0.216026</td></tr><tr><td>Strategy 7 (Mq-2)</td><td>29.50</td><td>517,501</td><td>0.242375</td></tr><tr><td>Strategy 4 (Mp-Mq)</td><td>27.10</td><td>483,033</td><td>0.225959</td></tr><tr><td>Equal focus</td><td>Strategy 8</td><td>28.94</td><td>256,420</td><td>0.229733</td></tr><tr><td colspan="5">Composite 4 (WLR = 30)</td></tr><tr><td rowspan="4">Productivity focus</td><td>Strategy 1 (Hp)</td><td>38.85</td><td>2,833,113</td><td>0.146107</td></tr><tr><td>Strategy 2 (Hp-Mq)</td><td>41.01</td><td>2,836,932</td><td>0.133773</td></tr><tr><td>Strategy 3 (Mp)</td><td>39.15</td><td>923,127</td><td>0.153482</td></tr><tr><td>Strategy 4 (Mp-Mq)</td><td>38.94</td><td>746,297</td><td>0.147374</td></tr><tr><td rowspan="4">Quality focus</td><td>Strategy 5 (Hq)</td><td>37.45</td><td>319,629</td><td>0.150944</td></tr><tr><td>Strategy 6 (Mq-1)</td><td>40.66</td><td>502,257</td><td>0.124957</td></tr><tr><td>Strategy 7 (Mq-2)</td><td>40.33</td><td>791,886</td><td>0.119185</td></tr><tr><td>Strategy 4 (Mp-Mq)</td><td>38.94</td><td>746,297</td><td>0.147374</td></tr><tr><td>Equal focus</td><td>Strategy 8</td><td>40.93</td><td>397,013</td><td>0.130046</td></tr></table>

priority with higher incentive should be placed on reducing errors over producing codes so that software project can be completed in shorter time, with lower cost, and with better workforce utilization.

Second, compensating workers for higher coding productivity does not result in ideal software development outcomes. These strategies actually incur higher cost but not-so-ideal completion time and workforce utilization. Therefore, companies should not solely pursue highly productive (i.e., fast coding) workers without considering their error tendency. Striking a balance between productivity and quality of workers' output or focusing more on quality will deliver better software development performance.

Third, Strategies 6 and 7 do not perform better than Strategies 4 and 5 in most cases. That is, rewarding debugging efforts does not result in ideal outcomes unless it is combined with high error penalty. This result con<sup>fi</sup>rms the general belief in practice that preventing errors in the <sup>fi</sup>rst place during software development is more bene<sup>fi</sup>cial than allowing their introduction and then trying to detect and correct them later [11].

Cross-strategy performance comparison with workforce composite 5.

<table><tr><td colspan="2"></td><td>Total time</td><td>Total cost</td><td>Idle ratio</td></tr><tr><td colspan="5">Composite 5 (WLR = 10)</td></tr><tr><td rowspan="4">Productivity focus</td><td>Strategy 1 (Hp)</td><td>21.87</td><td>1,222,347</td><td>0.440630</td></tr><tr><td>Strategy 2 (Hp-Mq)</td><td>23.08</td><td>1,116,823</td><td>0.453745</td></tr><tr><td>Strategy 3 (Mp)</td><td>21.93</td><td>392,446</td><td>0.441322</td></tr><tr><td>Strategy 4 (Mp-Mq)</td><td>21.96</td><td>307,962</td><td>0.441768</td></tr><tr><td rowspan="4">Quality focus</td><td>Strategy 5 (Hq)</td><td>21.51</td><td>135,569</td><td>0.426122</td></tr><tr><td>Strategy 6 (Mq-1)</td><td>22.54</td><td>198,049</td><td>0.445305</td></tr><tr><td>Strategy 7 (Mq-2)</td><td>22.29</td><td>313,369</td><td>0.437164</td></tr><tr><td>Strategy 4 (Mp-Mq)</td><td>21.96</td><td>307,962</td><td>0.441768</td></tr><tr><td>Equal focus</td><td>Strategy 8</td><td>22.64</td><td>161,495</td><td>0.445592</td></tr><tr><td colspan="5">Composite 5 (WLR = 20)</td></tr><tr><td rowspan="4">Productivity focus</td><td>Strategy 1 (Hp)</td><td>30.65</td><td>1,917,351</td><td>0.250388</td></tr><tr><td>Strategy 2 (Hp-Mq)</td><td>31.11</td><td>1,847,554</td><td>0.216058</td></tr><tr><td>Strategy 3 (Mp)</td><td>30.55</td><td>623,224</td><td>0.250590</td></tr><tr><td>Strategy 4 (Mp-Mq)</td><td>30.41</td><td>501,579</td><td>0.249073</td></tr><tr><td rowspan="4">Quality focus</td><td>Strategy 5 (Hq)</td><td>31.82</td><td>260,369</td><td>0.212606</td></tr><tr><td>Strategy 6 (Mq-1)</td><td>31.31</td><td>330,440</td><td>0.219763</td></tr><tr><td>Strategy 7 (Mq-2)</td><td>31.72</td><td>525,721</td><td>0.230486</td></tr><tr><td>Strategy 4 (Mp-Mq)</td><td>30.41</td><td>501,579</td><td>0.249073</td></tr><tr><td>Equal focus</td><td>Strategy 8</td><td>31.36</td><td>260,621</td><td>0.220445</td></tr><tr><td colspan="5">Composite 5 (WLR = 30)</td></tr><tr><td rowspan="4">Productivity focus</td><td>Strategy 1 (Hp)</td><td>41.30</td><td>2,845,696</td><td>0.135558</td></tr><tr><td>Strategy 2 (Hp-Mq)</td><td>45.04</td><td>2,859,374</td><td>0.137846</td></tr><tr><td>Strategy 3 (Mp)</td><td>42.36</td><td>937,404</td><td>0.154346</td></tr><tr><td>Strategy 4 (Mp-Mq)</td><td>42.13</td><td>767,448</td><td>0.152427</td></tr><tr><td rowspan="4">Quality focus</td><td>Strategy 5 (Hq)</td><td>40.57</td><td>339,751</td><td>0.149014</td></tr><tr><td>Strategy 6 (Mq-1)</td><td>44.83</td><td>526,358</td><td>0.134397</td></tr><tr><td>Strategy 7 (Mq-2)</td><td>45.56</td><td>824,103</td><td>0.147345</td></tr><tr><td>Strategy 4 (Mp-Mq)</td><td>42.13</td><td>767,448</td><td>0.152427</td></tr><tr><td>Equal focus</td><td>Strategy 8</td><td>45.17</td><td>410,510</td><td>0.141958</td></tr></table>

Finally, Strategy 8 with equal focus usually does not perform the best from any of the three perspectives of software development. The equalfocus strategy may work <sup>fi</sup>ne in general from the three perspectives; however, this strategy will not yield the best outcomes. Therefore, speci<sup>fi</sup>c incentives like penalty on errors and reward on debugging efforts should be implemented in order to achieve the best results.

## 6. Conclusions

In this study, we investigated important issues of project management and workforce management commonly encountered in largescale iterative software development. Project managers constantly face the challenge of adequately composing and assigning workforce who have different pro<sup>fi</sup>ciency for performing different tasks to development and testing activities in an iterative software development project, so as to minimize total time required and still meet the budget and quality constraints. Our focus on knowledge worker productivity and development team makeup re<sup>fl</sup>ects the <sup>fi</sup>ndings of Guinan et al. [25] that team skill, managerial planning, and consistency in team experience and knowledge levels are more effective than development tools and methods in enabling effective development processes. In compliance with the software industry practice, we consider three major development version releases in a software release life cycle: alpha, beta and <sup>fi</sup>nal. A discrete optimization model is formulated to represent the problem. In general, our simulation <sup>fi</sup>ndings shed light on identifying speci<sup>fi</sup>c workforce composites for satisfying speci<sup>fi</sup>c software development goals under organizational constraints.

Our results provide insightful implications. First, if timeliness of software development is the top priority, we con<sup>fi</sup>rm the conventional belief that a workforce composite consisting mainly of workers with high coding productivity can achieve shorter software development time. Therefore, when budget allows and highly productive workers are available, a project manager should seek to recruit and assign more workers with high productivity to software development tasks. Second, a higher workload ratio (i.e., a greater average number of tasks to be assigned to a worker) results in not only better worker utilization but also relatively less increase in development time. Therefore, if possible, we should consider utilizing existing employees more (i.e., assigning more tasks) instead of acquiring additional workers (which in fact could result in even longer development time). Third. between the two strategic focuses on productivity and quality, quality focus tends to yield better software development outcomes. Incorporating a higher penalty on error, a software project can actually be completed relatively faster and cheaper as well as with higher worker utilization. As a result, project managers and company executives should emphasize more on, and provide stronger incentive for, coding quality of workers than on their coding productivity or debugging capability. Finally, managing software development without a clear strategic focus will not derive desirable outcomes. Therefore, we should provide speci<sup>fi</sup>c incentives or guidelines for workers to focus on either quality or productivity in order to achieve better software development results.

As with all research, this study has some limitations that should be acknowledged. First, our model considers workers' skill levels and productivities that remain unchanged during the project period. To extend from this study, these factors can be adjusted based on training and observations over time [15] or for different types of projects and contexts. Second, our model does not take intangibles of workers and some environmental factors into account. For example, factors such as positive or negative synergy of co-workers on a project, past experience of workers on speci<sup>fi</sup>c projects and modules, learning on the <sup>fl</sup>y of workers during a project phase, integration efforts and effects of different software modules, and moral hazard of workers are not modeled or simulated in this study. Third, there can be other measurements of knowledge workers' productivities as well as error tendency for software development. We believe that our model can adapt to other quanti<sup>fi</sup>able measurements deemed appropriate. Fourth, to avoid further complexity of our model, we do not explicitly consider the possibility that workers will help other workers or be assigned to more tasks if they encounter idle time. Moreover, we assume minimal dependency among modules (tasks) within the same development and testing phase but, if necessary, dependency can also be incorporated into our model between additional subsequent development and testing phases. As a result, in our study, the critical path method (CPM) can be applied at the activity (or phase) level, not at the task (or module) level within each phase. Future research can thus consider dependency at the module level. Fifth, in our model, we do imply the reuse of codes from the previous phase and therefore only “additional” codes need to be developed for the current phase. On the other hand, we do acknowledge that even some additional codes might be duplicates of certain portion from the previous phase. Also, we do not consider the possibility of code reuse from earlier phase to later phase in such forms as shared library of procedures and functions. Sixth, in current model, we treat the relationship between module size and cost/time as linear. In future study, potential nonlinear functions can be considered in an attempt to capture the complexity and coordination effect on cost and time needed for larger project modules. Seventh, we assume a worker's compensation is proportional to her productivity. It is arguable that a good human resource practice can <sup>fi</sup>nd high quality workers with low compensation in an ideal situation. Finally, we give equal weight to the time and budget assigned for all three phases. It might be possible that managers would like to focus on or allocate resources in each phase differently. Our model can be modi<sup>fi</sup>ed to assign a weight coef<sup>fi</sup>- cient for each phase to take this aspect into account.

Our study provides a base framework for investigations into various aspects of project management and workforce management in the context of iterative software development. While there are limitations as mentioned above, this study utilizes the simulation approach mainly for the purposes of discovery and exploration. Future studies can be further pursued to extend our <sup>fi</sup>ndings. While our endeavor embodies the <sup>fi</sup>rst step to investigate complicated issues associated with workforce and project management in the context of iterative software development, our model can be modi<sup>fi</sup>ed for different project contexts such as pair programming and extreme programming. Other perspectives of project management, in addition to timeliness, effectiveness and utilization, can be explored. Additional strategic focuses on workforce beyond quality and productivity can also be investigated. On the methodology front, empirical data from real-world settings can be used to verify our simulation <sup>fi</sup>ndings. In addition, in this study we propose a metaheuristic algorithm based on particle swarm optimization (PSO) to derive solutions to the formulated problem. The advantage of this pro posed algorithm consists of the inherent parallelism, stochastic process, adaptability, and positive feedback. The experimental results manifest that our proposed PSO algorithm is more effective than a heuristic algorithm in producing a task assignment that requires a short duration time with the allowable budgets. Our results also suggest that the PSO algorithm can generate attractive alternatives for evaluation purposes. Nonetheless, a comprehensive decision support system incorporating the proposed task assignment model and the PSO algorithm can be built to help project managers further identify useful alternatives.

## Acknowledgments

The authors thank the reviewers and the editor for their constructive comments and insightful suggestions. Any errors that remain are the sole responsibility of the authors.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at http://dx. doi.org/10.1016/j.dss.2013.10.002.

## References

[1] T.K. Abdel-Hamid, K. Sengupta, C. Swett, The impact of goals on software project management: an experimental investigation, MIS Quarterly 23 (4) (1999) 531–555.

[2] A.M. Aladwani, An integrated performance model of information systems projects Journal of Management Information Systems 19 (1) (2002) 185–210.

[3] A.J. Albrecht, J.E. Gaffney, Software function, source lines of code, and development effort estimation: a software science validation, IEEE Transactions on Software Engineering 9 (6) (1983) 639–648.

[4] H.P. Andres, R.W. Zmud, A contingency approach to software project coordination, Journal of Management Information Systems 18 (3) (2001) 41–70.

[5] Robert D. Austin, The effects of time pressure on quality in software development: an agency model, Information Systems Research 12 (2) (2001) 195–207.

[6] R. Axelrod, Advancing the art of simulation in the social sciences, in: Conte, Hegselmann, Terna (Eds.), Simulating Social Phenomena, Springer, Berlin, 1997, pp. 21–40.

[7] A.J.G. Babu, N. Suresh, Project management with time, cost, and quality considerations, European Journal of Operational Research 88 (2) (1996) 320–327.

[8] B.G. Barker, D. Verma, System engineering effectiveness: a complexity point paradigm for software intensive systems in the information technology sector, Engineering Management Journal 15 (3) (2003) 29–38.

[9] J.D. Blackburn, G.D. Scudder, L.N. Van Wassenhove, Improving speed and productivity of software development: a global survey of software developers, IEEE Transactions on Software Engineering 22 (12) (1996) 875–885.

[10] B.W. Boehm, Software Engineering Economics, Prentice-Hall, Englewood Cliffs, N.J., 1981

[11] K. Bittner, I. Spence, Managing Iterative Software Development Project, Addison Wesley Longman, Massachusetts, 2006.

[12] P. Bratley, B. Fox, L. Schrge, A Guide to Simulation, Second edition Springer-Verlag, NY, 1987.

[13] G.M. Campbell, Cross-utilization of workers whose capabilities differ, Management Science 45 (5) (1999) 722–732

[14] A. Chen, T. Edgington, Assessing value in organizational knowledge creation: considerations for knowledge workers, MIS Quarterly 29 (2) (2005) 279–309.

[15] A. Chen, Y. Hwang, T.S. Raghu, Knowledge life cycle, knowledge inventory, and knowledge acquisition strategies, Decision Sciences 41 (1) (2010) 21–47.

[16] H. Chen, Editorial: design science, grand challenges, and societal impacts, ACM Transactions on Management, Information Systems 2 (1) (2011) 1–10.

[17] M. Clerc, J. Kennedy, The particle swarm explosion, stability, and convergence in a multidimensional complex space, IEEE Transaction on, Evolutionary Computation 6 (1) (2002) 58–73.

[18] M. Dawande, M. Johar, S. Kumar, V.S. Mookerjee, A comparison of pair versus solo programming under different objectives: an analytical approach, Information Systems Research 19 (1) (2008) 71–92.

[19] C. Deephouse, T. Mukhopadhyay, D.R. Goldenson, M.I. Kellner, Software process and project performance, Journal of Management Information Systems 12 (3) (1996) 187-205

[20] L. Dyer, J. Ericksen, In pursuit of marketplace agility: applying precepts of self-organizing systems to optimize human resource scalability, Human Resource Management 44 (2005) 183–189.

[21] R.C. Eberhart, Y. Shi, Particle Swarm Optimization: Developments, Applications and Resources, Proceedings of the 2001 Congress on Evolutionary Computation, 1, 2001, pp. 81–86.

[22] S. Faraj, L. Sproull, Coordinating expertise in software development teams, Management Science 46 (12) (2000).1554-1568

[23] N. Gilbert, K.G. Troitzsch, Simulation for the Social Scientist, Open University Press, 1999.

[24] P. Grunbacher, M. Halling, S. Bif<sup>fl</sup>, H. Kitapci, B.W. Boehm, Integrating collaborative processes and quality assurance techniques: experiences from requirements negotiation, Journal of Management Information Systems 20 (4) (2004) 9–29.

[25] P.J. Guinan, J.G. Cooprider, S. Faraj, Enabling software development team performance during requirements de<sup>fi</sup>nition: a behavioral versus technical approach, Information Systems Research 9 (2) (1998) 101–125.

[26] S. Haag, M.K. Raja, L.L. Schkade, Quality function deployment usage in software de velopment, Communications of the ACM 39 (1) (1996) 39–49.

[27] S. Hamilton, N.L. Chervany, Evaluating information system effectiveness — part I: comparing evaluation approaches, MIS Quarterly 5 (3) (1981) 55–69.

[28] D.E. Harter, M.S. Krishnan, S.A. Slaughter, Effects of process maturity on quality, cycle time, and effort in software product development, Management Science 46 (4) (2000) 451–466.

[29] D.E. Harter, S.A. Slaughter, Quality improvement and infrastructure activity costs in software development: a longitudinal analysis, Management Science 49 (6) (2003) 784–800.

[30] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Ouarterly 28 (1) (2004) 75–105

[31] R. Hooke, T.A. Jeeves, Direct search solution of numerical and statistical problems Journal of the Association for Computing Machinery 8 (1961) 212–229

[32] M. Keil, Pulling the plug: software project management and the problem of project escalation, MIS Ouarterly 19 (4) (1995) 421–447.

[33] M. Keil, J. Mann, A. Rai, Why software projects escalate: an empirical analysis and test of four theoretical models, MIS Quarterly 24 (4) (2000) 631–664

[34] J. Kennedy, R.C. Eberhart, Particle Swarm Optimization, Proceedings IEEE International Conference on Neural Networks, IV, 1995, pp. 1942–1948.

[35] J.Y. Kim, K. Altinkemer, A. Bisi, Yield management of workforce for it service providers, Decision Support Systems 53 (1) (2012) 23–33.

[36] M. Koushik, V.S. Mookerjee, Modeling coordination in software construction: an analytical approach, Information Systems Research 6 (3) (1995) 220–254.

[37] M.S. Krishnan, C.H. Kriebel, S. Kekre, T. Mukhopadhyay, An empirical analysis of productivity and quality in software products, Management Science 46 (6) (2000) 745–759.

[38] P. Kruchten, The Rational Uni<sup>fi</sup>ed Process: An Introduction, 3rd ed. Addison-Wesley, Inc., Reading, MA, 2004.

[39] R.J. Kuo, L.M. Lin, Application of a hybrid of genetic algorithm and particle swarm optimization algorithm for order clustering, Decision Support Systems 49 (4) (2011) 451–462.

[40] S.T. March, V. Storey, Design science in the information systems discipline, MIS Quarterly 32 (4) (2008) 725–730.

[41] R. Marciniak, Effectiveness measures for software development interests: design and validation American Association of Cost Engineers Transactions 2 (1992) 1–9

[42] K. Maxwell, L. Van Wassenhove, S. Dutta, Performance evaluation of general and company speci<sup>fi</sup>c models in software development effort estimation, Management Science 45 (6) (1999) 787–803.

[43] Z. Michalewicz, Genetic Algorithms + Data Structure = Evolution Programs, 3rd ed. Springer-Verlag, New York, NY, 1996.

[44] V.S. Mookerjee, I.R. Chiang, A dynamic coordination for software system construction, IEEE Transactions on Software Engineering 28 (6) (2002) 684–694.

[45] T. Mukhopadhyay, S.S. Vicinanza, M.J. Prietula, Examining the feasibility of a case-based reasoning model for software effort estimation, MIS Quarterly 16 (2) (1992) 155–171.

[46] S. Nidumolu, The effect of coordination and uncertainty on software project performance: residual performance risk as an intervening variable, Information Systems Research 6 (3) (1995) 191–219.

[47] S.R. Nidumolu, M.R. Subramani, The matrix of control: combining process and structure approaches to managing software development, Journal of Management Information Systems 20 (3) (2003) 159–196.

[48] T. Ravichandran, A. Rai, Total quality management in information systems development: key constructs and relationships, Journal of Management Information Systems 16 (3) (1999) 119–155.

[49] R.A. Ribeiro, A.M. Moreira, P. van den Broek, A. Pimentel, Hybrid assessment method for software engineering decisions, Decision Support Systems 51 (1) (2011) 208–219.

[50] K. Sengupta, T.K. Abdel-Hamid, M. Bosley, Coping with staf<sup>fi</sup>ng delays in software project management: an experimental investigation, IEEE Transactions on Systems, Man, and Cybernetics Part A — Systems and Humans 29 (1) (1999) 77–91.

[51] Z.H. Zhan, J. Zhang, Y. Li, Y.H. Shi, Orthogonal learning particle swarm optimization, IEEE Transactions on Evolutionary Computation 15 (6) (2011) 832–847.

Benjamin B. M. Shao is an Associate Professor of Information Systems in the W. P. Carey School of Business at Arizona State University. He received his B.S, and MS. from National Chiao Tung University, Taiwan, and Ph.D. from the State University of New York at Buffalo. His research interests are in the areas of IT impacts IS security healthcare IT distributed collaborative systems, and software project management. He has published more than 60 refereed papers in leading journals and conference proceedings across the <sup>fi</sup>elds of Information Systems, Computer Science, Production and Operations Management, Operations Research, and Healthcare Management. He has been serving on the editorial boards of six IS journals. In the W. P. Carey School, he was recognized for teaching excellence as the DISC Professor of the Year and the <sup>fi</sup>nalist for the John W. Teets Outstanding Teaching Award.

Peng-Yeng Yin received his B.S., M.S. and Ph.D. degrees in Computer Science from National Chiao Tung University, Hsinchu, Taiwan. From 1993 to 1994, he was a visiting scholar at the University of Maryland, College Park. In 2000, he was a visiting Professor at the University of California, Riverside (UCR). From 2006 to 2007, he was a visiting Professor at the University of Colorado. He is currently a Professor of the Department of Information Management, National Chi Nan University, Taiwan, and he was the department head during 2004 and 2006, and the Dean of the of<sup>fi</sup>ce of R&D for the university from 2008 to 2012. Dr. Yin is a member of the Phi Tau Phi Scholastic Honor Society and listed in Who’s Who in the World, Who’s Who in Science and Engineering, and Who’s Who in Asia. He is the Editor-in-Chief of the International Journal of Applied Metaheuristic Computing and is on the Editorial Board of several other journals. He has published more than 120 articles and edited four books in pattern recognition and metaheuristic computing. His current research interests include wind energy, evolutionary computation, metaheuristics, pattern recognition, machine learning, computational intelligence, and operations research.

Andrew Chen is an Associate Professor of Information Systems at the School of Business at the University of Kansas. His current teaching and research interests include knowledge management, IT business value, human computer interaction design, database management, and business and web programming applications. His research work appears in Decision Sciences, Decision Support Systems, European Journal of Operational Research, Journal of Electronic Commerce Research, Journal of Management Information Systems, and MIS Quarterly
