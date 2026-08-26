---
otero_id: 26237
otero_key: "DEHJQYNE"
title: "Designing Information Technology Architectures: A Cost-Oriented Methodology"
authors: "Chiara Francalanci; Vincenzo Piuri"
year: "1999"
journal: "Journal of Information Technology"
doi: "10.1177/026839629901400207"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Designing information technology architectures: a cost-oriented methodology

CHIARA FRANCALANCI AND VINCENZO PIURI Politecnico di Milano, 20133 Milano, Italy

This paper proposes a design methodology of information technology architectures tying organizational requirements to technical choices and costs. The primary goal is to provide a structured support for the selection of the minimum-cost architecture satisfying given organizational requirements. Previous empirical studies have attempted absolute cost comparisons of different architectural solutions, primarily relying on the expertise of practitioners and a priori beliefs, but have rarely taken into account the impact of organizational requirements on costs. Requirements are modelled as information processes, composed of tasks exchanging information and characterized by varying levels of computational complexity. Different architectural distributions of presentation, computation and data management applications are compared. The cost implications of organizational requirements for processing intensity, communication intensity and networking are analysed. The results show a relationship between structural features of information processes and architectural costs and indicate how architectural design should be based on organizational as well as technology considerations.

## Introduction

Information systems (IS) design and optimum sizing is the result of a reconciliation of several con¯ icting requirements, including technical performance and costs, organization impact and user acceptance. Theoretical research and practitioners often focus on speci® c techniques for the optimization of individual design phases, usually leading to local technical optima, with little understanding of the relationships between different choices at different design stages.

This paper attempts the de® nition of a comprehensive design methodology that covers all phases of IS design in order to tie organizational requirements to technical choices and resulting costs. The main goal is the identi® cation of a sequence of design steps that track the cost implications of design choices from requirements analysis to physical implementation. Each step is modelled according to available techniques, borrowing (from the literature) the modelling tools to represent goals, constraints and the structure of the IS.

The focus is on architectural design tying the information requirements of an organization to the information technology (IT) components necessary to satisfy those requirements: costs are associated with these components (cf. Zachman, 1987; Sowa and Zachman, 1992). This process has many degrees of freedom, since different architectures can be built to satisfy a given set of requirements. The proposed methodology guides the system designer through a sequence of choices at different design steps in order to distinguish alternative solutions and evaluate their costs. The primary goal of the methodology is to help choose the architecture that minimizes the overall cost (including hardware, software, maintenance, management and training).

Organizational requirements have been modelled as processes, composed of tasks with a certain level of computational complexity, exchanging information between them and classi® ed as presentation, computation or data processing. At an organizational level, the main cost-differentiating factors in¯ uencing architectural choices are intensity of processing (measured by task complexity), intensity of communication (measured by the quantity of exchanged information) and extent of communication (measured by the level of networking in the process).

All these characteristics ± either directly or indirectly ± in¯ uence IT costs (cf. Willcocks, 1992; Smithson, 1994; Alter, 1996; Blyler and Ray, 1998). Intensity of processing mainly de® nes the computational capability and related technical features of the processing units. Intensity of communication typically affects the speed characteristics of the interconnection links. Group user interactions constrain the information and computation distribution in the IS. In turn, these requirements in¯ uence the choice of IT architecture in a wide range of possible solutions, from centralized to fully distributed. The optimal selection of the most cost-effective solution needs an accurate analysis and cost evaluation of all technical options satisfying given requirements, since, theoretically, all architectures can provide any high level of processing ability, although at markedly different costs (cf. Simpson, $^ { 1 9 9 7 { \mathrm { a , b ) } } }$ . The proposed methodology facilitates this choice by systematically analysing technical options and their costs against organizational requirements.

The next section reviews previous approaches and highlights the main organizational and technical variables of interest. The third section presents the phases of the design methodology and the corresponding architectural models. The fourth section discusses how architectural costs, including hardware, software, communication and management costs, change with different technical choices. The ® fth and sixth sections report and discuss experimental results from a comparative analysis of costs of different architectural choices with varying organizational requirements. Finally, the last section draws conclusions and suggests directions for future research.

## Research background and motivation

Cost analyses of technical choices have highlighted numerous design trade-offs primarily related to the appropriate sizing and location of computing resources within an IT architecture (Guengerich, 1992). One of the most widely discussed design trade-offs is described by Grosch’s law, recently reformulated as \`it is most effective to accomplish any task on the least powerful type of computer capable of performing it’ (Ein-Dor 1985:151). A traditionally lower cost of processing capabilities on smaller computers and a generally reduced software complexity have created the belief that a decentralized IT architecture will involve lower overall costs for an organization.

A number of technical factors would instead work against decentralization. First, communication costs can be signi® cantly higher in a decentralized architecture, due to more cumbersome data retrieval and consolidation in distributed transaction processing (Gavish and Pirkul, 1986; Lee et al., 1994). Dynamic ® le location and ® le migration techniques have been studied to reduce communication costs and improve transaction performance in decentralized environments (Liu Sheng, 1992). In practice, databases are duplicated to limit remote data access through geographical networks, while raising data consistency issues and causing additional communication load to align multiple copies of the same data. Decentralized architectures also increase the variability of processor load and reduce their utilization, which may raise costs particularly in real-time and fault-tolerant distributed systems (Distante and Piuri, 1989; Piuri, 1994). The most general technical model answering the research question of this paper is provided by Jain (1987), who studied the optimal sizing of a distributed system to minimize the costs of communication for remote transactions, processors and primary and secondary storage, while guaranteeing maximum ® le availability and minimum response time for queries. Other results concerning the optimum sizing of distributed architectures for special applications in real-time and faulttolerant distributed systems can be found in Distante and Piuri (1989) and Piuri (1994).

While pointing to the relevant technical cost tradeoffs, previous analyses have failed to consider management costs, which can be greatly dissimilar across different IT architectures. Ahituv et al. (1989) distinguished two separate distribution policies, technical and organizational, privileging technology and management considerations respectively. Management costs represent a relevant dimension of organizational policies for choosing an IT architecture and have been empirically found to shift the balance of technical trade-offs (Moad, 1994; Dec, 1996; Simpson, $^ { 1 9 9 7 { \mathrm { a , b ) } } }$ . Distributed architectures were in fact only extensively adopted in organizations only in the early 1990s and some of the expected cost reductions have been demonstrated to be elusive.

One of the claims for explaining these failures is that the overall cost of a distributed architecture depends on organizational requirements, which may or may not favour distribution (Guengerich, 1992). For example, the re-engineering literature has advocated the need for aligning organizational structure and technology and contributed to creating the belief that a ¯ atter, process-oriented and more networked organization would be best served by a distributed IT architecture (Hammer and Champy, 1993; Jarvenpaa and Stoddard, 1993; Venkatraman, 1994). However, the relationship between the overall costs of an IT architecture and the structural features of organizational processes has not been investigated. The few empirical results that have been published present absolute cost comparisons between centralized and client± server architectures and do not discuss the impact of process features on the ® ndings (Moad, 1994; Dec, 1996; Simpson, $^ { 1 9 9 7 { \mathrm { a , b ) } } }$ . Recently, practitioners have been considering the recentralization of data and application functionalities in order to decrease management effort and costs. This seems to indicate that the design of the IT architecture is often guided more by current beliefs and market offer than by an understanding of organizational requirements and technology costs.

Initial organizational requirements and resulting architectural costs are tied by design methodologies that incrementally translate requirements into technical choices (Aue and Breu, 1994). This paper proposes a

## Designing IT architectures

methodology that models such choices, accounting for technical as well as management trade-offs. The design phases are relatively consolidated (Aue and Breu, 1994), but each one of them has been primarily studied in isolation and often further partitioned into subphases (Alter, 1996). For example, requirements design has been addressed both in the IS and organizational literature. The latter typically views information processing capacity as a factor of organizational performance, with limited attention to the technology costs incurred to support different levels of information requirements (Galbraith, 1973, 1977; Lin and Carley, 1997). The IS literature deals with representational issues of organizational requirements, leaving costs as an issue for subsequent design phases more directly involved in technology choices (De Marco, $1 9 7 8 ;$ Coad and Yourdon, 1991). Aggregate perspectives evaluating the effect of structural properties of processes on costs have rarely been taken.

## Design methodology

The architectural design process ties the information requirements of an organization to the physical components necessary to satisfy those requirements. Acquisition and usage costs are associated with these physical components. The architectural design process offers many degrees of freedom, since in most cases different architectures can be built to satisfy a given set of requirements. These degrees of freedom involve choices at different stages of the architectural design (Aue and Breu, 1994). We consider four design phases, each producing a corresponding model of the IT architecture.

(1) Information requirements design, de® ning organizational requirements for information processing capacity.

(2) Technology requirements design, de® ning the IT resources necessary to satisfy given requirements for information processing capacity.

(3) Infrastructural design, allocating the required technology resources on to separate and interconnected computers.

(4) Physical design, associating computers and communication links with minimum-size commercially available devices.

Each model of the technology architecture is translated into the model produced in the subsequent design phase by a speci® cation activity (Figure 1). This speci® cation involves design choices which in turn affect architectural costs. The following subsections describe the design phases, the corresponding models and the design choices involved by speci® cation activities.

## The information requirements model

Organizational requirements for information processing capacity are modelled as information processes. Table 1 summarizes the complete set of elements constituting the model and their symbols.

An information process (referred to subsequently as a process) is described by a set of tasks $\{ T _ { i } \mid i = 1 \ldots n \}$ and the input± output interdependencies between them. We consider processes as information processing entities and limit interdependencies between tasks to information interdependencies. $T _ { i }$ is input interdependent with $T _ { j }$ if $T _ { j }$ produces information $I _ { j i }$ that is input to $T _ { i 5 }$ conversely, $T _ { j }$ will be output interdependent with $T _ { i } .$

We consider the information $I _ { i j }$ and $I _ { j i }$ exchanged between two interdependent tasks $T _ { i }$ and $T _ { j }$ to be measured as an information exchange rate, that is the mean average quantity of information exchanged in a time unit. Information quantities are de® ned as integer multiples of the smallest piece of information that can be exchanged in a given organization. Records or information objects are examples of information units that are used in this design phase. A task $T _ { i }$ can receive input information from multiple output interdependent tasks and convey output information to multiple input interdependent tasks. The overall input information of task $T _ { i }$ is $I _ { \mathrm { i n p u t } , i } = \Sigma _ { x } I _ { x i }$ and the overall output information is $I _ { \mathrm { o u t p u t } , i } ^ { \phantom { \dagger } \cdot \phantom { } } = \Sigma _ { y } I _ { \phantom { } _ { i } } y$

Each process has single entry and exit tasks called source and sink respectively. Information interdependencies with source and sink represent information exchanges with the world external to the process.

A task $T _ { i }$ can be repeatedly accomplished by $n _ { i }$ human executors working in parallel, each of them completing $k _ { i }$ activations of the task in a time unit. This keeps the decomposition of a process into tasks at a conceptual level, while separately representing the number of task instances by the same or different individuals. With these de® nitions, a task has $n _ { i } k _ { i }$ instances in each time unit.

Tasks are also associated with a factor $\mathbb { \chi } _ { i }$ measuring their complexity, de® ned as the number of high-level instructions procedurally describing the task. This de® nition assumes that a task corresponds to a software application, whose procedural high-level requirements are available at this stage of design. This oneto-one correspondence simpli® es the design process, but it does not affect the ® nal relationship between the structural features of information processes and architectural costs. Possible inaccuracies in the number of high-level instructions can be reduced if the assessment is obtained for all tasks, either from the same designer or by using the same evaluation techniques.

![](/api/attachments/DEHJQYNE/fulltext/images/45e3867e0b15ceb1faa7557993ad6a2aa250816fd132fc813a897cbc40b9eb93.jpg)  
Figure 1 Design models and speci® cation activities

Table 1 Elements and symbols of the information requirements model

<table><tr><td>Model element</td><td>Symbol</td></tr><tr><td>Task</td><td> $T_i$ </td></tr><tr><td>Total number of tasks</td><td> $n$ </td></tr><tr><td>Information interdependence</td><td> $I_{ij}$ </td></tr><tr><td>Number of executors of task  $T_i$ </td><td> $n_i$ </td></tr><tr><td>Number of activations of task  $T_i$  in a time unit by a single executor</td><td> $k_i$ </td></tr><tr><td>Task complexity</td><td> $\chi_i$ </td></tr><tr><td>Input information of task  $T_i$ </td><td> $I_{\text{input},i}$ </td></tr><tr><td>Output information of task  $T_i$ </td><td> $I_{\text{output},i}$ </td></tr><tr><td>Input information from external world</td><td> $I_{\text{source},i}$ </td></tr><tr><td>Output information to external world</td><td> $I_{i,\text{sink}}$ </td></tr></table>

The information requirements model does not make a distinction between different types of information, nor does it provide qualitative descriptions of information interdependencies. This orientation differs from the conceptual models of information requirements proposed in the IS literature, traditionally emphasizing descriptive representations of information (De Marco, 1978). Describing information is critical in guaranteeing the conceptual completeness and correctness of requirements design. Although maintaining many of the representational constructs from the IS literature (e.g. tasks, information interdependencies and complexity), we aim to produce the most parsimonious representation of cost-differential characteristics of information processes.

## The technology requirements model

Technology requirements design associates tasks and information interdependencies with required technology resources. Table 2 explains the speci® cation activities leading from the elements of the information requirements model to the corresponding elements of the technology requirements model.

Each task $T _ { i }$ corresponds to a software application $A _ { i } ,$ being the total number of applications equal to the total number of tasks. A one-to-one correspondence between tasks and applications also involves an equal number of executors $n _ { i }$ and activations $k _ { i }$ for tasks and corresponding applications in a time unit. Applications are associated with primary and secondary memory requirements, PM and $S M _ { i }$ respectively, for data, executable code and temporary structures supporting execution. Memory requirements are usually related to the application’s computational complexity, generally growing with it. However, they are not univocally determined by complexity, since different applications may create local data to varying degrees. Secondary memory requirements are assumed to include the storage of the application itself.

Information interdependencies are translated into quantities of data exchanged in a time unit by specifying a conversion factor a between information and data units (e.g. between records and bytes). Since information interdependencies have been de® ned as multiples of the same unit of information, a is constant across interdependencies, both between generic tasks $( I _ { i j } )$ and with the external world $( I _ { \mathrm { s o u r c e } , i ^ { 3 } } I _ { i , \mathrm { s i n k } } )$ . A label $M _ { i j }$ is also attached to data transfers to indicate the type of data transfer, either in primary (PM ) or secondary (SM ) memory. Task complexity is translated into computational complexity by specifying a conversion factor $\beta _ { i }$ from high-level to machine-level instructions. If complexity can be assumed to be homogeneous across tasks, $\beta _ { i }$ can be considered constant.

## The infrastructural design model

Infrastructural design allocates the technology resources required to perform the tasks speci® ed by the information requirements model on the computers composing the IT architecture. The three main resources to be allocated are processing capacity, memory, and communication load. A computer, to which a number of users $n _ { i } ^ { \prime }$ of an application $A _ { i }$ are assigned from the technology requirements model, should provide enough hardware features to support computation and communication requirements. In particular, it must guarantee the following.

(1) each activation of $A _ { i }$ is attributed $P M _ { i }$ and $S M _ { i }$ shares of primary and secondary memory

(2) $n _ { i } ^ { \prime } k _ { i }$ activations of $A _ { i }$ can be executed in a time unit.

In order for $n _ { i } k _ { i }$ activations of $A _ { i }$ to be executed in a time unit, a computer’s processing capacity should evaluate at least to $n _ { i } ^ { \prime } k _ { i } \chi _ { i }$ machine-level instructions per time unit. If $k _ { i }$ measures the number of activations per second, $n _ { i } ^ { \prime } k _ { i } \mathcal { X } _ { i }$ expresses processing capacity in MIPS (millions of machine-level instructions per second); MIPS can be translated into ${ \cal { M H z } } ,$ a common unit for the processing capacity of small computers, through the number of c.p.i. (cycles per instruction) (Patterson and Hennessy, 1994). If multiple applications $\{ A _ { 1 } , \dotsc A _ { k } \}$ are assigned to the same computer, the processing capacity must be at least $\begin{array} { r } { \sum _ { i = 1 \mathrm { ~ . ~ . ~ } k } n _ { i } ^ { \prime } k _ { i } \chi _ { i } } \end{array}$

Table 2 Elements and symbols of the technology requirements model

<table><tr><td>Element and symbol of the information requirements model</td><td>Specification activity</td><td>Element and symbol of the technology requirements model</td></tr><tr><td rowspan="3">Task,  $T_i$ </td><td>Mapping between tasks and software applications</td><td>Application,  $A_i$ </td></tr><tr><td>Classification of applications as presentation, computation or data management</td><td>Class of application, {P, C, D}Primary Memory,  $PM_i$ Secondary Memory,  $SM_i$ </td></tr><tr><td>Specification of primary and secondary memory requirements in bytes</td><td></td></tr><tr><td>Total number of tasks, n</td><td></td><td>Total number of applications, n</td></tr><tr><td>Number of executors of task  $T_i,n_i$ </td><td></td><td>Number of executors of application  $A_i$ ,  $n_i$ </td></tr><tr><td>Number of activations of task  $T_i$  in a time unit by a single executor,  $k_i$ </td><td></td><td>Number of activations of application  $A_i$  in a time unit by a single executor,  $k_i$ </td></tr><tr><td rowspan="2">Information interdependence,  $I_{ij}$ </td><td>Specification of conversion factor  $\alpha$  from organizational units of information to bytes</td><td>Data transfer,  $\alpha I_{ij}$ </td></tr><tr><td>Specification of the type of memory, primary or secondary, used for the data transfer</td><td>Class of data transfer $M_{ij} = [PM,SM]$ </td></tr><tr><td>Task Complexity,  $\chi_i$ </td><td>Specification of conversion factor  $\beta_i$  from high-level to machine-level instructions</td><td>Application computational complexity, $\beta_i\chi_i$ </td></tr><tr><td rowspan="2">Input information from external world,  $I_{source,i}$ </td><td>Specification of conversion factor  $\alpha$  from organizational units of information to bytes</td><td>Input data transfer,  $\alpha I_{source,i}$ </td></tr><tr><td>Specification of the type of memory, primary or secondary, used for the data transfer</td><td>Class of data transfer $M_{source,i} = [PM.SM]$ </td></tr><tr><td rowspan="2">Output information to external world,  $I_{i,sink}$ </td><td>Specification of conversion factor  $\alpha$  from organizational units of information to bytes</td><td>Output data transfer,  $\alpha I_{i,sink}$ </td></tr><tr><td>Specification of the type of memory, primary or secondary, used for data transfer</td><td>Class of data transfer $M_{i,sink} = [PM, SM]$ </td></tr></table>

Similarly, the total memory requirements are the summation of the primary and secondary memory requirements for all activations, that is $\begin{array} { r } { \sum _ { i = 1 \mathrm { ~ \dots ~ } k } n _ { i \ k i } ^ { \prime } P M _ { i } } \end{array}$ and $\begin{array} { r } { \sum _ { i = 1 \mathrm { ~ . ~ . ~ } k } n _ { i } ^ { \prime } k _ { i } S M _ { i } } \end{array}$ respectively. Secondary memory requirements are supposed to include an estimate of the data created by the application and, possibly, stored in a common database. By referring to data created as opposed to data accessed, the summation of secondary memory requirements for $\{ A _ { l } , \dotsc A _ { k } \}$ involves minimal redundancy among different applications.

We assume that an application is executed on a single machine, possibly multiprocessor, but never partitioned and remotely distributed for execution to separate machines. If the designer needs to model parallel and cooperative execution of subtasks within a given task, task partitioning must be explicitly represented in the information requirements model. The main types of cooperative processing can be modelled by classifying applications as presentation, computation and data management, i.e. as activities related to user interaction, data processing and data retrieval and storage, respectively.

Interactions among cooperative applications supporting a process are modelled as information exchanges. Applications $A _ { i }$ and $A _ { j }$ exchange data $\alpha I _ { i j }$ between each other. $\operatorname { I f } A _ { i }$ and $A _ { j }$ have been allocated to the same computer, the data transfer $\alpha I _ { i j }$ is local, while it is remote otherwise. Local and remote data transfers involve different memory requirements. A local data transfer in primary memory is supposed to take place in an area of memory of size $\alpha I _ { i j }$ shared between the two applications. A remote data transfer in primary memory would instead require a quantity of memory $\alpha I _ { i j }$ on both communicating computers. A remote data transfer in secondary memory is supposed to avoid the duplication of stored data, requiring a quantity of memory $\alpha I _ { i j }$ on only one of the communicating computers. Figure 2 shows the total amount of data transferred between computer $N ^ { t h }$ and $M ^ { t h }$ . The communication link between them should provide a communication capacity proportional to the total amount of transferred data, the physical distance between the two computers and response time requirements for each remote data transfer.

Similarly, data transfers $\mathsf { q } I _ { \mathrm { s o u r c e } , i }$ and $\mathbf { \Delta G } I _ { i , \mathrm { s i n k } }$ with the external world translate into memory requirements for the computer where $A _ { i }$ is allocated. The required memory is primary or secondary as speci® ed by the labels $M _ { \mathrm { s o u r c e } , i }$ and $M _ { i , \mathrm { s i n k } } .$ In addition, communication with the external world can be distinguished as local or remote.

## The Physical Model

Physical design associates physical components with the requirements speci® cations of the infrastructural model by identifying commercially available computers and communication links that offer at least the required capacity in terms of processing, memory and communication. This design phase is typically vendor dependent, since each manufacturer offers a different set of computers with distinct basic con® gurations and expansion components. To support physical design, vendors use computer applications, called con® gurators, which select and analyse the commercial components necessary to satisfy customers’ computing requirements.

![](/api/attachments/DEHJQYNE/fulltext/images/ccb95fbc7bf1dd44950eef3f191ff64674106b07231d0f3b8cdf8d6171e0e6ca.jpg)  
Figure 2 De® nition of a computer in the infrastructural model (dotted lines represent information exchange with other computers)

When requirements are imprecise or there exist multiple options, con® gurators may compare alternative solutions against cost and performance criteria by adopting optimization techniques to explore the range of possible solutions.

The simulation described in the ® fth section is based on a simpli® ed con® gurator operating on a vendorindependent component database. A limited number of basic computer con® gurations have been considered, selected as those common to the majority of commercial con® gurators. Additional components to expand basic con® gurations and obtain a higher capacity have also been included. Thirty-four basic con® gurations have been stored in the con® gurator, ranging from a 133 Mhz Pentium to a mainframe with 12 parallel 200 Mhz processors. The primary feature determining the choice of a basic con® guration is central processing unit (CPU) speed, which has to be equal to or greater than the processing capacity of the corresponding computer in the infrastructural design model. To satisfy memory requirements, it may be necessary to expand the selected basic con® guration. Particularly high memory requirements may drive the choice of the basic con® guration, given the practical limits to memory expansion.

Communication links are distinguished as remote or local, ranging from 14 kbit/s to 100 Mbit/s. The choice of a local versus remote communication link will depend on the physical location of the communicating computers and the sources of external information. In both cases, the discriminant feature of a physical communication link is capacity, most often measured in bits per second (b.p.s.). A physical link’s capacity should be equal to or greater than the capacity of the corresponding link between the computers in the infrastructural requirements model.

## Architectural costs

Technology resources involve different costs over their life cycle for purchase, installation, operation and maintenance. Costs are classi® ed into hardware, software, communication and management, by the de® nitions reported in Table 3. The literature documents numerous cost classi® cations, typically targeted at technology cost accounting (cf. Parker et $a l _ { \cdot s }$ 1988; Guengerich, 1992). A distinction between technology and management costs is common to most of these classi® cations. A further speci® cation of technology costs into hardware, software and communication allows a more precise association between the costs and physical components of IT architecture.

Each class of costs is associated with a different set of physical components of IT architecture. Hardware costs are associated with computers, expansion components and communication links. Software costs are associated with applications. Management costs are associated with computers, communication links and applications. Physical components may not incur all costs within a particular class. For example, the majority of expansion components do not involve any user training, nor do they require a speci® c operating system. Being associated with physical components, costs are unitary.

Table 3 Classi® cation of IT costs

<table><tr><td>Class of cost</td><td>Cost item included</td></tr><tr><td>Hardware and operating system</td><td>Hardware and operating system acquisitionHardware and operating system installationHardware and operating system testing</td></tr><tr><td>Application software</td><td>Requirements analysisAcquisition and customerization or development and verificationIntegration and installationTesting</td></tr><tr><td>Communication</td><td>Network lease (for wide area networks)Network installation (for local area networks)</td></tr><tr><td>Management</td><td>Hardware and operating system maintenance and upgradeSoftware maintenance and upgradeNetwork, managementUser training on operating systemUser training on software applicationsUser technical support (e.g. help desk)</td></tr></table>

In our experimental component database, hardware costs were obtained as a market mean of six different vendors, encompassing IBM, HP, Zenith, Digital, Compaq, and Olivetti. Communication costs were calculated as the mean among IBM, HP, Digital, Bull, Olivetti and Telecom. Cost data were collected from vendors’ web sites and from benchmarking sites, such as http://www.tpc.org. Software costs were gathered separately for software packages and in-house developed applications. The characteristics for the main software packages by Microsoft, Oracle, SAP, IBM, Digital, HP and Bull were obtained from vendors’ web pages; vendors’ web sites in fact provide thorough descriptions of software packages, including functionalities, size, hardware requirements and costs. The cost of in-house developed applications was calculated as a function of computational complexity. The site http://www.davidconsultinggroup.com/dcgindu.htm is an example of the relationship between software costs and size, as it has been adopted in this research. Management costs were obtained from benchmarking sites and triangulated with the empirical ® ndings of ® eld surveys (Moad, 1994; Dec, 1996; Simpson, 1997a,b).

The literature documents numerous cost classi® cations, typically targeted at technology cost accounting (Parker et al. 1988; Guengerich, 1992). A distinction between technology and management costs is common to most of these classi® cations. A further speci® cation of technology costs into hardware and software allows a more precise association between the costs and physical components of IT architecture.

## Experimental results

The proposed design methodology has been applied to compare the costs of different architectures with varying structural features of information processes in the information requirements model. In particular, the following structural features of processes have been studied.

(1) The intensity of processing, measured as tasks’ computational complexity $\mathbb { \chi } _ { i \dot { \mathfrak { s } } } ^ { \mathbf { \varrho } }$

(2) The intensity of communication, measured as the rate of information exchanges Iij, $I _ { i , s i n k } ,$ and $I _ { s o u r c e , i } .$

(3) The extent of communication, measured as the level of process networking.

Processes de® ned with the information requirements model can be considered generic graphs and analysed with graph analysis techniques (Harary, 1969; Foulds, 1992; Goutis, 1995). The mathematical de® nition of process networking was then borrowed from graph theory. For the purposes of this paper, it is suf® cient to know that networking is a number ranging between 0 and 1, measuring the number of tasks input or output interdependent with one another relative to the total number of tasks.

Several physical architectures have been considered, which are differentiated by the level of distribution of presentation, computation and data management applications among client and server computers. Figure 3 shows eight different architectures obtained with different allocations of applications. This view extends the discretization of the architectural choices commonly used in practice (Faye Borthick and Roth, 1994; Blyler and Ray, 1998). The distribution choice is practically useful, since it de® nes different levels of client± server architectures as processing migrates from the server to the client side (Blyler and Ray 1998). The central architectures in Figure 3 are in fact generically referred to as client± server, as opposed to the extreme centralized and stand-alone solutions.

![](/api/attachments/DEHJQYNE/fulltext/images/1a5be36400c0dfabc014731e61945c4af0a9c8ffd62aabc1864ec0804df631ff.jpg)  
Figure 3 Discretization of architectural choices based on the distribution of presentation, computation and data management applications

The cost analysis and comparison between these architectural choices was supported by an Excel-based tool developed in Visual Basic helping creation, modi-® cation, and versioning of projects according to the methodology explained in the third section.

Experimentation ranged between 50 and 250 tasks in the information requirements model. Networking was increased from 0.086 to 0.25 (obtained when, on average, each task is interdependent with approximately 25% of the total number of tasks). The order of magnitude of information interdependencies between task pairs was limited at between 100 and 10 000 b.p.s. Architectures with one, three and six servers were tested with different values of structural properties of processes.

Table 4 summarizes how cost trade-offs between different architectural choices vary with organizational requirements for the intensity of processing and the intensity and extent of communication. As an example, Figure 4 shows the minimum-cost solution with the distributed data and computation architecture at between 50 and 500 users. The required computational complexity and number of clients are reported on the horizontal and vertical axes respectively. Each area is labelled by the identi® ers of the chosen client and server, whose increasing value corresponds to greater computing capacity. Similar charts have been built for the distributed presentation and distributed application architectures. Figure 5 shows the minimum-cost architecture with varying requirements for computational complexity and number of users. The grey areas in Figure 5 represent values of organizational requirements for which the minimum-cost solution depends on the speci® c data point.

## Discussion

The ® ndings highlight a dependence of costs on the structural features of processes. Both networking and information interdependencies modify the overall costs of different architectural choices, changing the minimum-cost solution (® ndings 3± 8). On the contrary, computational complexity involves a growth of costs comparable across different architectures and does not affect the cost differences between them (® nding 2).

The most interesting ® nding from an organizational perspective is the impact of networking on costs. A client± server architecture seems to minimize IT costs for information processes with high levels of networking (® nding 5). This is basically due to the opportunity for exploiting parallelism in process execution with a limited amount of shared data. However, different client± server solutions show a high variance in their overall costs. While the distributed data and computation architecture has minimum costs, the remote data management would involve maximum costs, signi® cantly higher than a traditional centralized architecture. Variance is mostly related to communication costs that are minimized by local data management on client computers in distributed data and computation architectures.

Intuitively, high networking raises the need for direct communication between client computers. Low interaction between users’ activities suggests the decentralization of application functionalities (i.e. presentation and computation) and the centralization of data storage to facilitate information sharing. The decentralization of application functionalities reduces network traf® c, while splitting either computation or presentation between the client and the server would increase the amount of data to be transferred and, as a consequence, communication costs. Conversely, strong data dependencies between users’ activities suggests the centralization of application functionalities to reduce the amount of data to be exchanged over the network. The optimum solution consists of decentralizing computation and data management as long as the processes of different users do not involve frequent interactions and data sharing.

More speci® cally, maintaining presentation, computation and data management on centralized computing systems simpli® es the operation of IT architecture and reduces the number of system managers and operators and, thus, management costs. Moreover, the computational demand for supporting presentation for a high number of users requires high-performance architectures and, consequently, high technology acquisition and maintenance costs.

Distributing presentation over clients both reduces computational requirements on the server and enables

## Designing IT architectures

Table 4 Main ® ndings about the relationship between structural properties of processes and costs of different IT architectures

<table><tr><td>Finding 1</td><td>A higher number of servers increases the overall cost of architectures with all computation applications on the servers</td></tr><tr><td>Finding 2</td><td>Computational complexity does not represent a cost-differentiating factor across architectures</td></tr><tr><td>Finding 3</td><td>When networking and information interdependencies are low, the remote data management architecture has the lowest overall costs, while distributed computation has maximum costs</td></tr><tr><td>Finding 4</td><td>When networking is low and information interdependencies are high the centralized architecture has the lowest overall costs, while remote data management has maximum costs</td></tr><tr><td>Finding 5</td><td>When networking is high, the distributed data and computation architecture has the lowest overall cost, while remote data management has maximum costs</td></tr><tr><td>Finding 6</td><td>Centralized architectures have maximum hardware costs with low networking, with minimum hardware costs as networking increases. Among client–server architectures, hardware costs are maximum for the distributed presentation architecture and minimum for distributed data management with low networking. As networking increases, hardware costs become maximum for the distributed data management architecture and minimum for distributed computation</td></tr><tr><td>Finding 7</td><td>Software costs are always minimum in centralized architectures. Among client–server architectures, they are maximum for distributed computation and minimum for distributed presentation with low networking. As networking increases, they become maximum for distributed data management and remain minimum for distributed presentation</td></tr><tr><td>Finding 8</td><td>Management costs are always minimum in centralized architectures. They are equivalent for the different client–server solutions with low networking. As networking increases, they grow significantly only in distributed data management architectures</td></tr></table>

![](/api/attachments/DEHJQYNE/fulltext/images/a3f29b63dd27215898908cd97e9408a76dabd41f80ba357186739d8411efdea7.jpg)  
Figure 4 Client± server solutions with minimum cost for the distributed data and computation distributed architecture (pairs of numbers marking different zones in the ® gure indicate the number of client and server minimizing costs, e.g. \`7± 10; 22’ indicates a client between 7 and 10 and server 22)

![](/api/attachments/DEHJQYNE/fulltext/images/5f765d95667f0cd609eb0e42899015a063226d5111c3c8eae02acf47df045493.jpg)  
Figure 5 Comparative evaluation of client± server architecture with minimum cost for remote presentation (RP), remote computation (RC) and distributed date and computation (DDC); inside grey areas the actual choice of the optimum solution depends on speci® c requirements

the development of interactive and friendly user interfaces. Graphic interfaces can in fact be ef® ciently supported by local processing capacity on client computers, which is cheaper and more abundant than on servers. Transferring only the information to be presented and not the whole screen limits the quantity of data to be transmitted over the network, which may otherwise become a bottleneck for processing performance. Similarly, distributing either part or the whole computation over distributed machines is feasible when users’ activities are not closely interrelated and the computation moved on to clients uses a limited quantity of data from the server.

Data management can also be distributed if data subsets accessed by processes allocated to different clients have a limited overlap. The quantities of information that are exchanged through the network have been found to be a driver of cost, which is minimized with centralized architectures (® nding 4). Centralization reduces management and software costs by granting the IS function with scale economies primarily related to human resources (® ndings 7 and 8). These economies seem to offset the higher hardware costs of centralized computing. Distributed architectures require both additional management personnel and software, for example to deal with distributed software versioning, database consistency, network management and tuning.

As networking increases, higher communication requirements shift this trade-off towards client± server solutions with a distributed allocation of computation and data management (® ndings 5 and 6). Note that the number of servers has been found to be a purely technical choice independent of the structural features of information processes (® nding 1), as long as user activities can be split over different servers and servers can be connected by high-performance links.

Figure 5 shows how no IT architecture has absolute lowest costs, even if management costs are accounted for. Traditional technical variables modelling architectural choices remain cost discriminating and management costs shift technical trade-offs towards centralization, but have been found not to determine the minimum-cost solution. The grey areas in Figure 5 suggest signi® cant variations in the architectural solution minimizing costs even for small changes in organizational requirements. When design is limited to a particular type of IT architecture (e.g. the distributed data and computation in Figure 4), these variations seem to become particularly frequent for certain values of requirements. Furthermore, as the requirements increase along one of the axes in Figure 4, minimizing costs may require implementing and then rolling back architectural changes. For example, as the requirements for processing capacity increase from 9 to 10 MIPS, server 22 should be replaced by server 23 and then restored. On the one hand, these results con® rm that architectural design needs a systematic approach to be tied to organizational requirements. On the other hand, other considerations, such as the scalability of IT architecture, seem to be necessary to avoid local optima and frequent architectural changes.

## Conclusions

The main contribution of this paper is to show a relationship between the structural features of information processes and architectural costs. With respect to previous research, the ® ndings are interesting as they allow a ® ner comparison across different architectures by accounting for process requirements. Previous empirical studies attempted an absolute cost comparison across architectures and rarely discussed the impact of process features on their results. The optimum architectural choice from the point of view of costs and organizational requirements has been shown not to be unique but strongly dependent on the speci® c application requirements since hardware, software, maintenance, training and management costs have con¯ icting behaviours between the different structural solutions.

While the computer and cost database that supported experimentation is time dependent, the method for translating process requirements into physical choices is general. The results may partly depend on the high costs of centralized hardware in state-of-the-art technology, favouring client± server with respect to centralized architectures. As hardware and communication costs continue to decrease, the minimum-cost architecture may change. However, the same methodology and support tool would allow the amendment of cost analyses, once technical parameters are updated.

Future research and experimentation will be directed towards validating the proposed approach with practical large-scale cases. Additional testing for a broader range of process features will also be required in order to generalize the results. In this paper, we focused our attention on the costs and performance of the IT architecture supporting the IS. However, these aspects are not the only ones relevant when choosing the most suitable solution for the application environment and the organization. A few conceptual extensions would be required to measure scale effects on costs linked to the size of the IT architecture, currently captured only when related to software and data sharing among tasks. Scalability should also be considered since it might affect costs when ISs are evolving rapidly. Constraints on the IT components could be added to deal effectively with hardware and software legacies when their expected lifetime is not expired and their acquisition costs are still to be amortized. User acceptance and system usability should also be evaluated since they affect the actual productivity of the IS and, in turn, of the whole organization. Moreover, costs related to both organizational changes and IT organizational maturity should also be accounted for, although extremely dif® cult to quantify.

An interesting development would complete the architectural analysis by accompanying the analysis of costs with performance considerations. Notwithstanding the emphasis on costs in the professional literature, the lowest-cost solution does not necessarily represent the best alternative. Technical and organizational performance re¯ ections would improve the understanding of costs and bene® ts of long-term choices for the IT architecture.

## References

Ahituv, N., Neumann, S. and Zviran, M. (1989) Factors affecting the policy for distributing computing resources. MIS Quarterly, 13(4), 389± 400.

Alter, S. (1996) Information Systems: A Management Perspective (The Benjamin/Cummings Publishing Company, Inc., NY).

Aue, A. and Breu, M. (1994) Distributed information systems: an advanced methodology. IEEE Transactions on Software Engineering, 20(8), 594± 605.

Blyler, J.E. and Ray, G.A. (1998) What’s Size Got to Do With It? Understanding Computer Rightsizing (IEEE Press, NY).

Coad, P. and Yourdon, E. (1991) Object-oriented Analysis (Yourdon Press, NY).

Dec, K. (1996) Gartner view: client/server payoff. CIO, 9(13), 72± 6.

De Marco, T. (1978) Structured Analysis and Systems Speci® cation (Prentice Hall, Englewood Cliffs, NJ).

Distante, F. and Piuri, V. (1989) Hill-climbing heuristics for optimal hardware dimensioning and software allocation in fault-tolerant distributed systems. IEEE Transactions on Reliability, 38(1), 28± 39.

Ein-Dor, P. (1985) Grosch’s law revisited: CPU power and the cost of computation. Communications of the ACM, 28(2), 142± 51.

Faye Borthick, A. and Roth, H.P. (1994) Understanding client/server computing. Management Accounting, 76(2), 36± 41.

Foulds, L.R. (1992) Graph Theory Applications (Springer Verlag, NY, Inc, NY.).

Galbraith, J.R. (1973) Designing Complex Organizations (Addison-Wesley Publishing Company Inc., San Francisco).

Galbraith, J.R. (1977) Organization Design (Addison-Wesley Publishing Company Inc., San Francisco.).

Gavish, B. and Pirkul, H. (1986) Computer and database location in distributed computer systems. IEEE Transactions on Computers, 35(7), 583± 90.

Goutis, C. (1995) A graphical method for solving a decision analysis problem. IEEE Transactions on Systems, Man, and Cybernetics, 25(8), 1181± 93.

Guengerich, S. (1992) Downsizing Information Systems (SAMS-Prentice Hall Computer Publishing, Indiana).

Hammer, M. and Champy, J. (1993) Reengineering the Corporation (HarperCollins, New York).

Harary, F. (1969) Graph Theory (Addison-Wesley Publishing Company, NY).

Hayes, R.H., Wheelwright, S.C. and Clark, K.B. (1988) Dynamic Manufacturing: Creating the Learning Organization (Free Press, New York and Collier Macmillan, London).

Jain, H.K. (1987) A comprehensive model for the design of distributed computer systems. IEEE Transactions on Software Engineering, 13(10), 1092± 104.

Jarvenpaa, S. and Stoddard, D.B. (1993) Business Process Reengineering: Tactics for Managing Radical Change (Harvard Business School, Boston, MA).

Lee, H., Shi, Y. and Stolen, J. (1994) Allocating data ® les over a wide area network: goal setting and compromise design. Information & Management, 26, 85± 93.

Lin, Z. and Carley, K.M. (1997) Organizational response: the cost performance tradeoff. Management Science, 43(2), 217± 34.

Liu Sheng, O.R. (1992) Optimization of ® le migration policies in distributed computer systems. Computers Operations Research, 19(5), 335± 51.

Moad, J. (1994) Client/Server costs: don’ t get taken for a ride. Datamation, 40(4), 34± 41.

Parker, M.M., Benson, R.J. and Trainor, H.E. (1988) Information Economics. (Prentice-Hall International Editions, New Jersey).

Patterson, D.A. and Hennessy, J.L. (1994) Computer Organization and Design: The Hardware/Software Interface (Morgan Kaufmann, California).

Piuri, V. (1994) Design of fault-tolerant distributed control systems. IEEE Transactions on Instrumentation and Measurements, 43(2), 257± 64.

Simpson, D. (1997a) Cut desktop management costs! Datamation, 43(1), 102± 5.

Simpson, D. (1997b) Will NCs save you a bundle? Datamation, 43(5), 100± 5.

Smithson, S. (1994) Information retrieval evaluation in practice: a case study approach. Information Processing & Management, 30(2), 205± 23.

Sowa, J.F. and Zachman, J.A. (1992) Extending and formalizing the framework for information system architecture. IBM Systems Journal, 31(3), 590± 616.

Venkatraman, N. (1994) IT-enabled business transformation: from automation to business scope rede® nition. Sloan Management Review, 35(2), 73± 87.

Willcocks, L. (1992), \`Evaluating information technology investments: research, ® ndings, and reappraisal. Journal of Information Systems, 2, 243± 68.

Zachman, J.A. (1987) A framework for information system architecture. IBM Systems Journal, 26(3), 276± 92.

## Biographical notes

Chiara Francalanci is an Assistant Professor of Information Systems at Politecnico di Milano. She has a master’s degree in Electronic Engineering from Politecnico di Milano, where she has also completed her Ph.D. in Management Information Systems. As part of her post doctoral studies, she has worked for a year and a half at Harvard Business School as a Visiting Researcher. She has authored numerous articles on the economics of information technology, consulted on IT management, both in Europe and in the US, and published case studies on the impact of IT on performance.

Vincenzo Piuri has obtained a Ph.D. in Computer Engineering in 1989 at Politecnico di Milano. He is presently Associate Professor of Operating Systems at Politecnico di Milano. His research interests include distributed and parallel computing systems, computer arithmetic, neural networks, and fault tolerance. He is Associate Editor of the IEEE Transactions on Instrumentation and Measurement and a member of IEEE, IMACS and AEI.

Address for correspondence: Chiara Francalanci, Dipartimento di Elettronica e Informazione, Politecnico di Milano, piazza Leonardo da Vinci 32, 20133 Milano, Italy.
