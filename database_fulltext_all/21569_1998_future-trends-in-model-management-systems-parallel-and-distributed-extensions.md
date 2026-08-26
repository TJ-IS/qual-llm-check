---
otero_id: 21569
otero_key: "RKVPNAP5"
title: "Future trends in model management systems: parallel and distributed extensions"
authors: "Margaret K Mayer"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00025-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Future trends in model management systems: parallel and distributed extensions

Margaret K. Mayer

Department of Systems Engineering, Thornton Hall, UniÕersity of Virginia, CharlottesÕille, VA 22903, USA

## Abstract

A model management system MMS is a computer system which aids in the organization, utilization, and execution ofŽ . models for decision makers. Currently, MMS frameworks do not provide an estimate of computer resource consumption rates for solvers, or permit alternate computational models. Without an estimate of computer resource consumption rates, the decision maker is unable to evaluate alternative solution approaches to select the most efficient. Even with such an estimate, MMS may fail the analyst if all strategies require computation time which exceeds the deadline. This is largely due to the fact the MMS only permits sequential computation. MMS prototypes limit execution of solvers to sequential, so alternative computational models such as Single Program Multiple Datastream and Multiple Input Multiple Datastream, cannot be used. MMS frameworks should be extended to provide algorithmic complexity of solvers as an evaluation measure and to incorporate parallel computational models. Networks of workstations connected by an Ethernet are an attractive low cost means of providing concurrent execution, and suit the flexible processing needs of MMS. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Model Management Systems; Parallel and distributed computing

## 1. Introduction

A model management system MMS is a com-Ž . puter based system which aids in the creation, storage, retrieval, manipulation, and utilization of models for decision makers 29 . The aim of MMS is to<sup>w</sup> <sup>x</sup> facilitate problem solving by relieving the decision maker of coding algorithms and specifying models in procedural syntax. This is made possible by decoupling the solvers from the models, specifying standardized input<sup>r</sup>output specifications, and accessing models and data in non-procedural syntax. An analogous example is a database system. Database architecture is divided into three levels—the internal, conceptual, and external 10 . The user interacts with<sup>w</sup> <sup>x</sup> the external level aware only of the information necessary for his application, while the conceptual level provides the abstract picture of the entire system. The internal level is concerned with the physical representation of the data in storage. If the database is relational, the user can utilize a non-procedural language called SQL that specifies what information to manipulate, not how to do perform the operations. Researchers 23,22,29,17 have created MMS prototypes which implement a tiered MMS architecture and provide a non-procedural modeling language.

A complete MMS framework assists in the selection, linking, and execution of models. Prior researchers 4,6,29 have specified desired features of <sup>w</sup> <sup>x</sup> MMS: a general framework for conceptualization of models, an executable modeling language, and software integration model linkage . Through IŽ . <sup>r</sup>O standardization and model rules, an analyst can link different models together to solve a problem. Some <sup>w</sup> <sup>x</sup> 18,29 identify the need for a measure to compare existing versions of models, but do not suggest what measures to use. One such measure this research proposes is the algorithmic complexity of the linked model solvers an executable capable of solving aŽ model associated with a dataset and parameters . In. fact, MMS frameworks have completely ignored the performance issue despite the existence of complexity theory 32 . <sup>w</sup> <sup>x</sup>

Why does algorithm complexity matter in the MMS framework? For organizations to benefit from an MMS implementation, MMS must provide accurate results in a timely manner. Although development time can be reduced through the MMS framework, MMS minimally manages the execution of the linked model solvers, by providing compiling, linking and execution services. The solution of large scale problems often require either large amounts of memory or computational time, or both due to their complexity. It is realistic to assume that the linked models, each of which requires an amount of memory and computational time for a given set of inputs, may exceed the available resources on a machine. Without an estimate of the consumption of these resources, the decision maker is unable to evaluate alternative solution strategies.

Although a formal complexity measure specification in MMS aids the evaluation of alternative solution strategies, it does not address the problem of ensuring results in a timely manner. All solution strategies available to the analyst via MMS may require a solution time which exceeds a deadline. In this regard, the MMS has failed to aid the decision maker since she cannot solve her problem in a timely manner. This is largely due to the fact that the only computational model implemented in the MMS framework is single instruction single datastream Ž . SISD .

This paper proposes the extension of MMS to include parallel models of computation such as single program multiple datastream SPMD and multi-Ž . ple instruction multiple datastream MIMD 1,21 .Ž . <sup>w</sup> <sup>x</sup> The MIMD model is the execution of a set of instructions on multiple processors on different sets of data. Each processor can execute a different set of instructions. SPMD is the execution of a large instruction set, or complete program, on multiple processors using different sets of data. By incorporating alternative computational models into MMS which permit parallel instruction execution, a solution strategy solved by computational models other than SISD may return a solution in a timely manner. By including memory and complexity performance measures, each computational model as applied to the linked solvers can also be evaluated. Models can be parallelized on two levels within the MMS perspective: distribution of model solvers and parallelization of model solvers. Solver distribution is the placement of individual models on different machines, while solver parallelization refers to the distribution of a solver across multiple machines.

Since ease of use, model reuse and flexibility are main tenets of MMS, the hardware chosen to execute a parallel or distributed approach must also adhere to this. Parallel and distributed extensions to MMS will be useless if analysts are restricted to running on special purpose parallel hardware. Networks of workstations are an attractive low cost alternative to such hardware, and their excess computational cycles can be harnessed as needed 25 . Software already<sup>w</sup> <sup>x</sup> exists which utilizes networks of workstations as a virtual parallel machine 19,25,26,34,35,40 .<sup>w</sup> <sup>x</sup>

This extension to include parallelization and distribution introduces issues to the MMS that are either non-existent in the SISD computational model or trivial.

<table><tr><td>Machine selection</td><td>Select machines using a selection criteria.</td></tr><tr><td>Start up</td><td>Initiate remote execution of parallel/distributed models.</td></tr><tr><td>Communication</td><td>Communicating data and results among distributed solvers, within parallelized solvers, or parallelized solver results to other solvers.</td></tr><tr><td>Fault tolerance</td><td>Continued execution or clean termination despite the occurrence of an abnormal event, such as machine failure.</td></tr><tr><td>Termination</td><td>Detect termination of distributed/parallelized models.</td></tr></table>

These issues are not unique to the extended MMS; any parallel<sup>r</sup>distributed software must address these issues 25,26 . In fact, the various parallel software<sup>w</sup> <sup>x</sup> identified earlier address these issues to varying degrees. Since a goal of MMS is to aid in execution, the extended MMS must resolve these issues in a manner which is easy to understand for the analyst.

These extensions are motivated by the need of companies to have tools which permit flexible solution and computational strategies. A report published by the New Zealand Ministry of Commerce 9<sup>w</sup> <sup>x</sup> reported the recommendations of a study which explored alternatives for developing and maintaining models for their energy sector. Three strategies were proposed: laissez faire, full systems, and linked submodels. Laissez faire policy stated that models could developed without restriction in style or assumptions; full systems designated one large model that would model all subsectors, and linked submodels permitted development of models tailored to subsectors which could be linked when necessary. Although the submodels strategy was recommended, they noted that a disadvantage was the possibility of excessive solution times. The extensions proposed in this paper intend to eliminate this disadvantage.

## 2. Related research

To date, little research has been performed on parallel and distributed extensions in MMS. This section will present that research, general MMS research, and a brief background on parallel software available for networked workstations. The background on parallel software is included as reference for the methods proposed in Section 3.

## 2.1. Parallel and distributed MMS

Only one researcher has explored distributed extensions to MMS. In a 1993 working paper, Muhanna <sup>w</sup> <sup>x</sup> 28 discussed possible extensions of his SYMMS model to distribution. The basic non-distributedŽ . SYMMS architecture is shown in Fig. 1 29 . The<sup>w</sup> <sup>x</sup> Model Knowledge Base is similar to a database in that methods for storage, retrieval, integrity, and relationships of models are stored. The Model Consultation component MCS provides model selectionŽ . support, and the Model Execution component MESŽ . manages the linking, compiling, and execution of the selected models. The Dialogue Management Subsystem DMS is the interface of the system to the Ž . analyst. Included in SYMMS is a non-procedural language, MDL, which specify what models the decision maker wishes to use.

![](/api/attachments/RKVPNAP5/fulltext/images/b8f7644a1fc181d206a44bd3075bf24b650221a18a7e65549761d2924a2ff830.jpg)  
Fig. 1. SYMMS architecture.

Muhanna 28 examined the issues surrounding <sup>w</sup> <sup>x</sup> the physical distribution of the model base, and the applicability of client<sup>r</sup>server computational models to the management of the distributed model base. He also examined extensions to the MES system so that parallel and distributed computation can occur. By representing the linked solvers as applied to model instances as nodes on a network with input<sup>r</sup>outputs as edges, the problem becomes one of exploiting parallelism apparent in the graph and scheduling the solvers on appropriate processors. He identifies two other issues: implementation and heterogeneous machines. While SYMMS is a working MMS prototype, the distributed extensions proposed by Muhanna have not been implemented.

Although the parallel and distributed extensions proposed by Muhanna are similar to the ones proposed in this paper, several differences are apparent. The inclusion of the complexity measure component in this research is an extension critical to model<sup>r</sup>solver selection in the serial as well as parallel cases. Resource selection is targeted in this research, as cannot be assumed that machines that are equally available. Finally, the extension to the MES kernel to accomplish parallelization and distribution of solvers across machines is not stated. This research specifically addresses that issue, using SYMMS as an example.

## 2.2. Model management systems

Early researchers at first focused on MMS as part of a decision support system 3,12,14,22,31,<sup>w</sup> 36,41,42 . This view is limiting because parts of one<sup>x</sup> decision support system may also be applicable to another decision support system. Although MMS research has not halted in this direction, a wider perspective has been taken by most to rectify this limitation 11,16,24,27,29,37 . Several excellent sur-<sup>w</sup> <sup>x</sup> veys 4,39 exist which detail the evolution of the <sup>w</sup> <sup>x</sup> various approaches taken in MMS research, which for the sake of brevity will not be re-stated.

Because of the parallels of DBMS and MMS, some MMS models and prototypes tightly integrate the database and models 7,8,15,37 . This causes the<sup>w</sup> <sup>x</sup> models to be dependent on the origin of the data, which limits the reusability of the model for other datasets. Geoffrion 16 also holds that data and <sup>w</sup> <sup>x</sup> models should be tightly integrated, although the model formulation, not data representation, is of prime importance in his work on structured modeling. Artificial intelligence approaches have been applied to MMS regarding the representation of the knowledge. These approaches include use of formal logic 7 , semantic networks 13 , graphs 22 , and <sup>w x</sup> <sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> frames 11 .<sup>w</sup> <sup>x</sup>

Researchers in MMS tend to fall into one of two modeling categories: modeling-in-the-small, or modeling-in-the-large 29 . Modeling-in-the-small ad- <sup>w</sup> <sup>x</sup> dresses model conceptualization and formulation for a particular model. Examples of modeling-in-thesmall include spreadsheets, linear programming languages, and statistical packages which provide a language to solve a specific domain of problems. A much broader and problem independent view of modeling-in-the-small is taken by Geoffrion who developed structured modeling 17 :

. . . it uses a hierarchically organized, partitioned, and attributed acyclic graph to represent a model instance or a class of model instances, with particular attention given to representing semantic as well as mathematical structure . . .

In contrast, modeling-in-the-large considers the issues of administering a model base, model linkage to models and data, and presentation of information cohesively to the analyst 29 . The MMS framework<sup>w</sup> <sup>x</sup> differentiates between model types, model versions, and solvers. Several versions of one model may exist, and there are different types of models. For example, Model Types could be Forecast, Production Planning, Inzentory <sup>w</sup> <sup>x</sup> 29 . Model versions of type Forecast that may exist are: MoÕing AÕerage, Exponential Smoothing, and Simple Regression. Revisions of models versions are recorded for compatibility to existing linked model structures just as software versions exist simultaneously for compatibility. Solvers are the computer code associated with a particular model. The MCS alerts the analyst to the existence of these different model versions and aids in selection 29 . There are limitations to both ap- <sup>w</sup> <sup>x</sup> proaches. It can be argued that modeling-in-the-small must be accounted for in the larger scheme, since standardized development of model versions<sup>r</sup>solvers are necessary to ensure proper linkage to other models and data. However, modeling-in-the-small does not address the broad systems issues, which modeling-in-the-large targets.

## 2.3. Parallel software

Software which permits the use of networked workstations is currently available commercially or through public domain. This software is further categorized by being either based on procedures or objects. Selected software models will be reviewed here; a more complete survey is located in Ref. 25 .<sup>w</sup> <sup>x</sup>

Linda is a distributed data structures language where virtual shared memory is created so that data structures, called tuples, may be placed and accessed by a group of networked workstations. Exact location of a tuple in tuple space is unknown to the user, although it must physically reside on at least one of the workstations. Parallel virtual machine PVM is aŽ . public domain software library which was developed at Oak Ridge National Laboratory to execute large parallel applications that run on heterogeneous machines 40 . The PVM software permits an applica- <sup>w</sup> <sup>x</sup> tion to use a collection of different machines concurrently, allowing communication. Other parallel software uses PVM for its communication primitives with goals of efficient resource management 30 and<sup>w</sup> <sup>x</sup> parallelization by graphical display 34 .<sup>w</sup> <sup>x</sup>

XENOOPS is an object oriented approach to parallel software 20 which contains a generic abstract<sup>w</sup> <sup>x</sup> base class, Work Unit, to specify work to be performed. Although a design was presented, results of an implementation were not discussed. Mentat 19 is<sup>w</sup> <sup>x</sup> an object oriented parallel system consisting of a language and a compiler. It runs on several platforms, including networked workstations. The tasks of scheduling, communication, and synchronization among processes are automatically performed, while the decomposition of the problem is left to the programmer. Extensions to C<sup>qq</sup> permit specification of objects which are complex enough to be parallelized, without detailing communication.

An object oriented approach to the management of optimization problems across networked workstations has been created 25,26 . Unlike Mentat, paral- <sup>w</sup> <sup>x</sup> lelization is currently limited to the SPMD level which is particularly advantageous for combinatorial problems which have a large solution space to search for the optimal value. The user is in complete control of the frequency and type of communication through explicit message passing of Message objects which permits the user to compare communication frequency as a performance measure. The algorithm manager coordinates the startup, termination, and communication among processes across network. A statistics manager which ranks workstations according to workload aids in the selection of available workstations. Currently, the management of the communication and administrative details is performed through a centralized master. Planned extensions include other managerial configurations, such as peer to peer, and MIMD computational models.

## 3. Proposed extensions

The purpose of this research is to extend the MMS framework to compare performance of model solvers and permit their parallel and distribution execution. Through a careful review of the literature, the SYMMS architecture 29 is an ideal existing<sup>w</sup> <sup>x</sup> MMS framework that can be used as a base to showcase and eventually implement these extensions. Fig. 2 presents the proposed extensions to the SYMMS architecture, which can be compared to Fig. 1.

![](/api/attachments/RKVPNAP5/fulltext/images/bfd6e8a45ca3691262b0588757815c852803df808b3c5100dadba1ca4f1569c3.jpg)  
Fig. 2. SYMMS architecture with proposed extension.

## 3.1. Model consultation subsystem extension

Since the purpose of the MCS is to aid in model selection, the extension concerning algorithmic complexity belongs as an enhancement to the MCS, not an added module. Note that in Fig. 2, provisions for storage of the solver’s complexity must be made in the knowledge base, just as other attributes concerning a model or solver are stored. An established notation for stating the complexity of algorithms, such as Big-Oh Notation 1 , is proposed to represent <sup>w</sup> <sup>x</sup> the complexity of algorithms in MMS. It measures the growth rate of a algorithm, as it relates to the size of the input. Readers interested in the process of calculating the complexity of an algorithm should refer to 1,32 .<sup>w</sup> <sup>x</sup>

The importance of algorithmic complexity in MMS cannot be underestimated. For example, suppose two solvers, S1 and S2, are available to solve an instance of a model. S1 is an exact algorithm, in that it returns the optimal value, whereas S2 is a heuristic which does not guarantee optimal values. S2 may indeed return the optimal value for problems of a certain size or structure, but it cannot be guaranteed in the general case. S2 does return a near-optimal answer, which may be acceptable under certain conditions. In addition, suppose S1 has an exponential growth rate while S2 grows at a cubic rate. Without algorithmic complexity, the analyst cannot compare S1 and S2 in terms of expected computation time, without actually executing them both.

The use of algorithmic complexity can also serve as justification for the selection of S2 over S1. Under time constraints and using algorithmic complexity, the analyst may choose the heuristic S2 over S1 to solve large problems, sacrificing optimality but guaranteeing an answer before the deadline. Fig. 3 illustrates the comparison of complexity of three solvers: S1, S2, and S3. S1 and S2 are the exponential exact solver and cubic rate heuristic solver, respectively, while S3 is a cubic rate heuristic with a very large constant. For small input sizes, the exact solver S1 returns the solution in less time than S3 and about the same as S2. However, being an exponential algorithm, it quickly becomes costly to run, as shown in Fig. 3. If time to solution is limited, S2 or S3 is the better choice.

Although it appears that S3 would never be selected over S2, the algorithmic complexity graph does not indicate the quality of the solution returned. Since S2 and S3 are heuristics and only guarantee near-optimal values, it is likely that in terms of solution quality, there are solution quality differences under different input sets. The MCS, which provides information about suitability of models and solvers for problems, can provide that information to make the proper choice between S2 and S3.

![](/api/attachments/RKVPNAP5/fulltext/images/294f884cf1bc891797678a0becfada62c567654a6b14f84e41ed79caf85cf59b.jpg)  
Fig. 3. Chart of function growth.

## 3.2. Model distribution subsystem deÕelopment

Parallel and distributed selection and evaluation is performed by a new module called Model Distribution Subsystem MDS . The connections from MCSŽ . to the dialogue system are noted differently in Fig. 2, since the use of this module is optional to the analyst. The MDS is invoked directly by the analyst, or by the analyst’s selection of a model type version via MCS that requires distributed<sup>r</sup>parallel computation.

## 3.2.1. Distribution of solÕers

Once invoked, the MDS evaluates the potential for distribution of solvers across networked workstations, which can be performed by analyzing a graph of the dependencies among the linked solvers. Analysis is necessary since it is possible that distribution of the linked solvers may not result in a reduction in solution time. Distribution of the solvers introduces communication among them. The time to accomplish the communication is normally offset by the concurrent execution of solvers. It is possible that communication time cannot be offset if the percent of concurrent execution is minimal. For example, if the input to a solver S2 requires the complete output of a predecessor solver S1, concurrent execution of these solvers is not feasible. Placing these solvers on separate machines will only increase total execution time, due to the addition of communication time.

In order to distribute the solvers properly, the network of solvers must be classified and analyzed as to its divisibility. Processing loads can be classified as either indivisible or divisible. If a load is divisible, it can further be broken down into modularly divisible or arbitrarily divisible 2,5 . Indivisible<sup>w</sup> <sup>x</sup> loads must be run as one process on one machine, while divisible loads can be broken down. An arbitrarily divisible load can be distributed among any number of processors, while a modularly divisible load can only be broken down into a certain number of components due to its processing structure.

For a set of solvers, $\mathbf { S } = \{ \mathbf { s } _ { 1 } , \mathbf { s } _ { 2 } , \ldots , \mathbf { s } _ { n } \}$ , that are combined to solve a problem, P, with a given dataset, D, the relationships between the solvers must be determined. Because the one solver will provide its output as input to another solver, the solvers must be executed in a certain order. If some of solvers must be executed in a certain order, then the relationships are said to have precedence. A PERT<sup>r</sup>CPM raph <sup>w</sup> <sup>x</sup> 43 is constructed to display the relationships between solvers. Because each solver ${ \bf s } _ { i }$ in S is to be executed in its entirety on one processor and the solvers will exchange information, S can be classified as modularly divisible. A PERT<sup>r</sup>CPM graph will be composed by the MDS, to determine how much distribution is possible.

Once the PERT<sup>r</sup>CPM graph is constructed, the MDS must next consider whether distribution of the solvers will minimize solution time over a purely sequential execution. This can be accomplished by looking at the total processing time for the execution of S in two cases: 1 the sequential execution of S, Ž . and 2 the distributed execution of S.Ž .

3.2.1.1. Sequential execution of S. Let S be the set of Solvers, $\mathbf { s } = \mathbf { S } \{ \mathbf { s } _ { 1 } , \mathbf { s } _ { 2 } , \ldots , \mathbf { s } _ { n } \} .$ , and T be set of processing times, $\mathrm { T } = \{ t _ { 1 } , t _ { 2 } , \ldots , t _ { n } \}$ , associated with each $\mathbf { S } _ { i } . .$ For sequential execution of S, the total processing time, P, is:

$$
P _ {\mathrm{S}} = \sum_ {i = 1} ^ {n} t _ {i}
$$

3.2.1.2. Distributed execution of S. Let S be the set of Solvers, $\mathbf { s } = \mathbf { S } \{ \mathbf { s } _ { 1 } , \mathbf { s } _ { 2 } , \ldots , \mathbf { s } _ { n } \}$ , and T be set of processing times, $\mathrm { T } = \{ t _ { 1 } , t _ { 2 } , \ldots , t _ { n } \}$ , associated with each $\mathrm { ~ s ~ } _ { i } .$ In addition, let $c _ { i j }$ be the cost of communication between two solvers, and M be the set of machines, $M = \{ \mathbf { m } _ { 1 } , \mathbf { m } _ { 2 } , \dots , \mathbf { m } _ { k } \}$ , available to execute the distributed process. This problem is a task scheduling problem, specifically resource-constrained task scheduling 33 . In Ref. 33 , several heuristics are<sup>w x</sup> <sup>w x</sup> discussed for solving this NP-hard scheduling problem specifically for multi-processor task scheduling. In the case where $M = 2 .$ , it is possible to utilize maximum network flow algorithms efficiently to schedule tasks on processors 38 .<sup>w</sup> <sup>x</sup>

## 3.2.2. Parallelization of solÕers

The proposed MDS will also handle the selection of a specific solver to run in parallel. Since the

SYMMS architecture has the capability to store different model version types, the parallel solver code can be stored as a version of the sequential solver. Typically, an algorithm may be decomposed in several ways to execute in parallel. The choice of decomposition partly depends on the type of computer used to execute the parallel code. In the case of using networked workstations as a parallel machine, the choice is also dependent upon the amount of communication that results. Communication is a factor since the workstations and the network which connects them are not dedicated as a parallel machine, but rather manage multiple tasks and users. Frequent communication or waits for responses increase overall execution time, and erode the advantage of parallel execution.

Rather than specify that the MDS should automatically decompose and parallelize the problems, it is proposed that the MDS use a parallel solver version which is stored with the sequential version. The background section includes a brief survey of several parallel software environments which could be used to aid the process of parallelization. The solver can be parallelized with one of these software environments, using the appropriate communication primitives. To maintain the flexibility of MMS, a specific software environment can not be expected to be used in every case. This is analogous to permitting sequential solvers to be coded in different languages such as FORTRAN, C, or C<sup>qq</sup>. Caution must be used, however, in permitting alternate software environments if parallel solvers coded in different environments are to be linked together. This issue is to be handled by the MES.

## 3.3. Model execution subsystem enhancement

The MES module is to be enhanced to manage the administrative functions of the parallel<sup>r</sup>distributed linked solvers in execution. The administrative functions address the issues listed in Section 1: startup, termination, communication, and fault tolerance. Because the enhanced MES will handle these issues for a variety of solvers and computing environments, it needs to be flexible in its addressing of the issues. For example, suppose the network of workstations that are available to use vary widely in their computing workload. The MES should distribute the solver tasks to appropriate workstations based on current workload, so as not to overload already busy workstations. A resource selection algorithm which always selects the same set of workstations, independent of workload, would be a bad choice for two reasons: 1 solvers are computationally intensive, Ž . and 2 additional tasks will only add to the currentŽ . workload. Once the machines have been selected, startup consists of placing the decomposed solver asŽ specified by its parallel solver version onto those. machines. For the distributed case, entire solvers are placed different machines.

Now that the solvers have been placed on machines and have begun to execute as separate computer processes, the MES must handle the communication that results from the distribution<sup>r</sup>parallelization. Communication patterns for the distributed solvers is the passing of one solver’s output to another solver for input. In some cases, the distributed solvers may run independently, and then their results sent to another solver. Distributed solver communication is predictable due to this output–input pattern. Although communication patterns have been specified by the solver version used in the parallel case, frequency and type of communication will vary from solver to solver. In either the distributed or parallel case, the communication patterns could be synchronous or asynchronous. In synchronous communication, a solver may wait for communication reply before continuing, while in asynchronous communication, a solver continues its task without waiting for a reply. Due to the type of communication and frequency, the MES must allow for flexible communication.

Once the distributed and<sup>r</sup>or parallel solvers have finished executing, the MES must recognize this event and return the results to the analyst. If the MES does not detect that all remote processes have terminated, the system will wait. This unnecessary waiting adds time to solution execution and erodes performance gains made by distribution and parallelization. Termination detection of remote solvers must be addressed to avoid this scenario.

Finally, the MES must be fault tolerant, which is the ability to continue execution or terminate regularly despite the occurrence of an abnormal event <sup>w</sup> <sup>x</sup> 25,26 . For the MES, an abnormal event is the loss of a process which is associated with a solver. This loss can occur for several reasons, which include machine failure and program failure. At a minimum, the MES must recognize the loss of the process. At this point three options are available: 1 TerminateŽ . the entire effort, 2 Restart the lost process, 3Ž . Ž . Continue without the process. The selection of which alternative is problem-solver dependent, especially in the case of option 3 . Using the scenario of paral-Ž . lelizing one solver, suppose the decomposition consisted of executing the same solver on multiple machines using different data sets which represent different areas of the solution space. The loss of one process in this case may not be disastrous if the lost solver was returning intermediate results that were much poorer than the other processes. However, if the solver was guaranteed to return an optimal result, that lost process may have been searching the space which would ultimately return that value. Without its continued execution, incorrect results would be returned. This case illustrates how the selection of a fault tolerant policy is problem-solver dependent. The MES should handle all three cases, which can be specified either by the analyst or by information stored with the parallel solver version, in the case of parallel solver execution.

It is proposed that the enhanced MES should contain an algorithm manager which coordinates the startup, termination, and communication of the solvers, both in distributed and parallel sequences. Such an algorithm manager has been created 25,26<sup>w</sup> <sup>x</sup> to handle the SPMD parallel execution of optimization problems. This algorithm manager can easily be extended to include MIMD parallel execution, and the execution of distributed solvers. Since the algorithm manager has encapsulated the communication protocols, it is possible to utilize alternate software for communication such as PVM 40 or Linda 35 .<sup>w x</sup> <sup>w x</sup> This would require writing of new methods which use PVM or Linda communication calls, but it would not change the interface to the MES or the functionality of the algorithm manager. This capability permits the use of parallel solver versions which were developed using not only algorithm manager communication calls, but also Linda or PVM. With these enhancements, the MES will truly aid in the compilation and execution of solvers so that results can be returned efficiently.

## 4. Summary

This paper has presented parallel and distributed extensions to MMS which are necessary to achieve its goals of flexibility and reuse. The incorporation of computational complexity of solvers gives an analyst a comparative measure of the various solvers’ computational time for a given set of inputs. Without extensions to the model of execution, the analyst using any MMS framework will be unable to select alternative computational strategies as part of the model solving process. This ultimately prevents the analyst from solving problems in a timely manner, rendering the SISD MMS useless. The author has demonstrated how to incorporate these extensions into an existing prototype MMS architecture, SYMMS. The consultation subsystem and knowledge base is extended to incorporate the calculation and storage of computational complexity. Extensions to include parallelism are located in the execution and consultation subsystems. A new subsystem which handles the evaluation of potential parallelism in a set of solvers is proposed. Other MMS prototypes can similarly be extended, providing they have an extensible architecture design.

Issues regarding the selection of what software environment to use for parallelism were raised, and it is suggested that until there is a standard, alternate models be allowed for use. It is necessary, though, within the enhanced MES to ensure that different solver environments can operate concurrently so that parallel solvers can be linked just as sequential solvers are linked by input–output. Since this paper has only discussed extensions to MMS frameworks, it would be inappropriate to suggest whether any parallel software environment is incompatible without the extensions in a working prototype.

MMS is a decision aiding tool in that it aids in the creation, use, storage, selection, and execution of models. While several MMS frameworks have been developed, none have yet transitioned from research into industry use. For MMS to become commonplace in industry, the frameworks must address alternate models of execution and computational complexity as a performance measure. These extensions will create a decision tool that aids in the selection and execution of models<sup>r</sup>solvers, producing a framework that promotes reuse and flexibility.

## 5. Acronyms

DMS Dialogue Management Subsystem MMS Model Management System SISD Single Instruction Single Datastream MIMD Multiple Instruction Multiple Datastream MES Model Execution Subsystem MDS Model Distribution Subsystem MCS Model Consultation Subsystem SYMMS Prototype of an MMS 27,29<sup>w</sup> <sup>x</sup>

## Acknowledgements

I would like to thank Waleed Muhanna of Ohio State University, author of several Model Management Papers and developer of SYMMS, for his support towards these extensions and permission to use the SYMMS architecture as an example in this paper. I would also like to thank George Wilson of Lehigh University for introducing me to Model Management theory, and for his comments regarding these proposed extensions.

## References

<sup>w</sup> <sup>x</sup> 1 A. Aho, J. Hopcroft, J. Ullman, Data Structures and Algorithms, Addison-Wesley, Reading, MA, 1983.

<sup>w</sup> <sup>x</sup> 2 S. Akl, The Design and Analysis of Parallel Algorithms, Prentice-Hall, Englewood Cliffs, NJ, 1989.

<sup>w</sup> <sup>x</sup> 3 L.M. Applegate, B.R. Konsynski, J.F. Nunamaker, Model management systems: designs for decision support, Decision Support Syst. 2 1 1986 81–91.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 A.A. Baldwin, D. Baldwin, T.K. Sen, The evolution and problems of model management research, OMEGA-Int. J. Manage. Sci. 19 6 1991 511–528.Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 V. Bharadwaj, D. Ghose, M. Venkataraman, T. Robertazzi, Scheduling Divisible Loads in Parallel and Distributed Systems, IEEE Computer Society Press, Los Alamitos, CA, 1996.

<sup>w</sup> <sup>x</sup> 6 M. Binbasiolglu, Key features for model building decision support systems, Eur. J. Operational Res. 82 1995 422–437.Ž .

<sup>w</sup> <sup>x</sup> 7 R.H. Bonczek, C.W. Holsapple, A.B. Whinston, Mathematical programming within the context of a generalized data base management system, R.A.I.R.O. Recherche Operationnelle<sup>r</sup>Operations Res. 12 2 1978 117–139.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 R.H. Bonczek, C.W. Holsapple, A.B. Whinston, A generalized decision support system using predicate calculus and network database management, Operations Res. 29 1981Ž . 263–281.

<sup>w</sup> <sup>x</sup> 9 J.G. Culy, S.J. Gale, The Prospects for Energy Modeling: Volume I Review and Recommendations, New Zealand Ministry of Commerce Report, NZIER Contract 341, 1991.

<sup>w</sup> <sup>x</sup> 10 C.J. Date, An Introduction to Database Systems, 6th edn., Addison-Wesley Publishing, Reading, MA, 1995.

<sup>w</sup> <sup>x</sup> 11 D.R. Dolk, B.R. Konsynski, Knowledge representation for model management systems, IEEE Trans. Software Eng. SE–10 6 1984 619–628.Ž . Ž .

12 A. Dutta, A. Basu, An artificial intelligence approach to model management in decision support systems, IEEE Comput. 17 9 1984 89–97.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 J.J. Elam, J.C. Henderson, L.W. Miller, Model management systems: an approach to decision support in complex organizations, Proceedings of the First International Conference on Information Systems, December 1980, pp. 98–110.

<sup>w</sup> <sup>x</sup> 14 J. Fedorowicz, G.B. William, Representing modeling knowledge in an intelligent decision support system, Decision Support Syst. 2 1 1986 3–14.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 R. Fourer, Database structures for a class of mathematical programming models, Proceedings of the 24th Annual Hawaii International Conference on System Sciences, January 1991, pp. 306–316.

<sup>w</sup> <sup>x</sup> 16 A.M. Geoffrion, An introduction to structured modeling, Manage. Sci. 33 5 1987 547–588.Ž . Ž .

<sup>w</sup> <sup>x</sup> 17 A.M. Geoffrion, The formal aspects of structured modeling, Operations Res. 37 1 1989 30–50.Ž . Ž .

<sup>w</sup> <sup>x</sup> 18 A.M. Geoffrion, Computer-based modeling environments, Eur. J. Operational Res. 41 1989 33–43. Ž .

<sup>w</sup> <sup>x</sup> 19 A. Grimshaw, Easy-to-use object-oriented parallel processing with Mentat, Computer, May 1993, pp. 39–51.

<sup>w</sup> <sup>x</sup> 20 W. Jossen, S. Binjens, P. Verbaeten, Object parallelism in XENOOPS, Proceedings of the First Annual Object Oriented Numerics Conference, 1993, pp. 42–54.

21 A.H. Karp, Programming for parallelism, Computer 20 5Ž . Ž . 1987 43–57.

<sup>w</sup> <sup>x</sup> 22 T.-P. Liang, Development of a knowledge-based model management system, Operations Res. 36 6 1988 849–863.Ž . Ž .

<sup>w</sup> <sup>x</sup> 23 T.-P. Liang, C.V. Jones, Meta-design considerations in developing model management systems, Decision Sci. 19 1Ž . Ž . 1988 72–92.

<sup>w</sup> <sup>x</sup> 24 M.V. Mannino, B.S. Greenberg, S.N. Hong, Model libraries: knowledge representation and reasoning, ORSA J. Computing 2 3 1990 287–301.Ž . Ž .

<sup>w</sup> <sup>x</sup> 25 M. Mayer, Management of Networked Workstations as a Parallel Machine for the solution of Optimization Problems, PhD Thesis Industrial Engineering, Lehigh University, Bethlehem, PA, 1995.

<sup>w</sup> <sup>x</sup> 26 M. Mayer, L.J. Plebani, A parallel algorithm manager for networked workstations, Annals of Operations Research Special issue in OR<sup>r</sup>IS interface, in press, 1997.

<sup>w</sup> <sup>x</sup> 27 L.W. Miller, N. Katz, Model management systems to support policy analysis, Decision Support Syst. 2 1 1986 55–63.Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 W.A. Muhanna, Distributed model management systems: organizational considerations and implementation issues, Working Paper Series WPS93-52, The College of Business, The Ohio State University, September 1993, p. 39.

<sup>w</sup> <sup>x</sup> 29 W. Muhanna, R.A. Pick, Meta-modeling concepts and tools

for model management: a systems approach, Manage. Sci. 40 Ž . Ž .9 1994 1093–1113.

<sup>w</sup> <sup>x</sup> 30 B. Neumann, R. Rao, The Prospero resource manager: a scalable framework for processor allocation in distributed systems, Concurrency: Practice and Experience 6 4 1994Ž . Ž . 339–355.

<sup>w</sup> <sup>x</sup> 31 S.-S. Pan, R.A. Pick, A.B. Whinston, A formal approach to decision support, in: S.K. Change Ed. , Management andŽ . Office Information Systems, Plenum, New York, 1984.

<sup>w</sup> <sup>x</sup> 32 C.H. Papadimitriou, K. Steiglitz, Combinatorial Optimization: Algorithms and Complexity, Prentice-Hall, Englewood Cliffs, NJ, 1982.

<sup>w</sup> <sup>x</sup> 33 D.-T. Peng, K.G. Shin, Optimal scheduling of cooperative tasks in a distributed system using an enumerative method, IEEE Trans. Software Eng. 19 3 1993 253–267.Ž . Ž .

<sup>w</sup> <sup>x</sup> 34 J. Schaeffer, D. Szafron, et al., The enterprise model for developing distributed applications, IEEE Parallel and Distributed Technology, August 1993, 85–95.

<sup>w</sup> <sup>x</sup> 35 Scientific Computing Associates, C-Linda User’s Guide and Reference Manual, New Haven, CT, 1992.

<sup>w</sup> <sup>x</sup> 36 R.H. Sprague, H.J. Watson, MIS concepts: I., J. Syst. Manage., January 1975, pp. 34–37.

<sup>w</sup> <sup>x</sup> 37 E.A. Stohr, M. Tanniru, A database for operations research models, Int. J. Policy Anal. Inform. Syst. 4 1 1980Ž . Ž . 105–121.

<sup>w</sup> <sup>x</sup> 38 H.S. Stone, Multiprocessor scheduling with the aid of network flow algorithms, IEEE Trans. Software Eng. SE–3 1Ž . Ž . 1977 85–93.

<sup>w</sup> <sup>x</sup> 39 C.-K. Suh, E.-H. Suh, D.-M. Lee, Artificial intelligence

approaches in model management systems: a survey, Comput. Ind. Eng. 28 2 1995 291–299.Ž . Ž .

<sup>w</sup> <sup>x</sup> 40 V. Sunderam, PVM: A framework for parallel distributed computing, Concurrency: Practice and Experience 2 4Ž . Ž . 1990 315–339.

41 E. Turban, Decision Support and Expert Systems: Management Support Systems, Macmillan, New York, NY, 1988.

<sup>w</sup> <sup>x</sup> 42 H.J. Will, Model management systems, Information Systems and Organization Structure, Walter de Gruyter, Berlin, Germany, 1975.

<sup>w</sup> <sup>x</sup> 43 W.L. Winston, Operations Research: Applications and Algorithms, PWS-Kent Publishing, Boston, MA, 1991.

![](/api/attachments/RKVPNAP5/fulltext/images/8aae549e5374060d4427bff6021d4f6476334c377c95a3063cf5fdfcec643ee6.jpg)

Margaret K. Mayer is an Assistant Professor in the Department of Systems Engineering at the University of Virginia. She received her PhD in Industria Engineering from Lehigh University. She holds a BS from the School of Operations Research and Industrial Engineering at Cornell University and MS in Industrial Engineering from Lehigh University. She is currently an Associate Editor for INFORMS On-line, IN-FORMS’ electronic information source,

and is an Associate Editor for International Abstracts in Operations Research. Her research interests are in the areas of information technology, artificial intelligence, model management systems, and parallel algorithm development.
