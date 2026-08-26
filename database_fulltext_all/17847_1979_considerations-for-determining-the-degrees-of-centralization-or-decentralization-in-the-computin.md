---
otero_id: 17847
otero_key: "CV3V6SYV"
title: "Considerations for determining the degrees of centralization or decentralization in the computing environment"
authors: "Jacob Slonim; Dave Schmidt; Paul Fisher"
year: "1979"
journal: "Information & Management"
doi: "10.1016/0378-7206(79)90016-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Considerations for Determining the Degrees of Centralization or Decentralization in the Computing Environment

Jacob Slonim, Dave Schmidt, and Paul Fisher
Department of Computer Science, Kansas State University,
Manhattan, Kansas 66506. USA

The advent of distributed data base systems has introduced a bewildering assortment of terms, measurements, and descriptions for managers and users. The complexity which a distributed system introduces in hardware, software, and data allocation provides the major source of misunderstanding and confusion that is reflected in current jargon. This paper proposes a method of definition and measurement which alleviates the terminology and measurement problem. The methodology provides a standardized view of distributed systems and promotes an objective, quantified approach to the classification and selection of such a system.

Keywords: Database, operational, performance, update, retrieval economic, distribution.

![](/api/attachments/CV3V6SYV/fulltext/images/21db0c712d41eab76443ea962dd8d1acb1c0128864342685a832e0bd98a89890.jpg)

Jacob Slonim received a B.S. in Computer Science and Mathematics from the University of Western Ontario in 1971, an M.S. in Computer Science in 1973, and a Ph.D. in the same field was awarded him by Kansas State University in 1978. His professional experience includes the following: system designer, programmer, and project manager for Canadian Jurimetrics Limited; international project manager for the National Center of

Scientific and Technological Information, Israel; and research assistant and instructor at Kansas State University. He is a member of the ACM, SIGMINI, and SIGIR honorary professional societies, and his current research field is data base management. He has authored over sixteen publications since 1975 and has two patents registered with the U.S. government—one for the method for identifying the components of a file and the other for a system and method of updating automatically textual data.

![](/api/attachments/CV3V6SYV/fulltext/images/d09be822843b76ace5ad4e63d7cce5680995a84d81441cae606e723c131618d3.jpg)

Paul S. Fisher received a B.A. in Mathematics from the University of Utah in 1963, an M.A. in the same field in 1964, and a Ph.D. in Computer Science was awarded him by Arizona State University in 1967. From 1967 to 1972, he worked as an Assistant Professor in the Department of Computer Science at Kansas University and was thereafter advanced to the position of Associate Professor. His current position as

Head of that Department was presented him in 1973, and he was awarded a full professorship in July, 1978. Dr. Fisher has served as a reviewer for Computer Reviews ACM, CACM-Programming Systems Section, Wiley, and McGraw-Hill. He is currently serving as consultant to the Computer Systems Command, U.S. Army. He has authored over fourteen publications since 1970 and in that time has also received over a dozen research grants, most notably one each for software portability issues (£195K) and a back-end DBMS communication system (£10K). Dr. Fisher is a member of the ACM, SIGMINI, SIGPLAN, and SIGACT honorary professionals' societies, and is presently on sabbatical in Israel, where he is a Visiting Professor at the University of Tel-Aviv and working as a research consultant to ELBIT.

![](/api/attachments/CV3V6SYV/fulltext/images/9b7a4fb55611dfb89e80fb00f43b1c4665f1dd877be50644d376a3aca57526ed.jpg)

David A. Schmidt was born in Colby, Kansas on May 10, 1953. He received the B.A. degree (Mathematics) from Fort Hays (Kansas) State University in 1975 and the M.S. degree (Computer Science) from Kansas State University in 1977, where he is currently working towards the Ph.D. degree. His research interests include denotational semantics and computational complexity. Mr. Schmidt is a member of the IEEE Computer

Society and the Association for Computing Machinery.

## 1. Introduction

There has long been a need for a standard for defining and comparing distributed organizations. Since there are now a large variety of organizational options in terms of geography, hardware and software, this need becomes crucial. The methodology presented for filling this need assists in selection as well as measurement of a system; managers need assistance in deciding, based on factors important to them, which alternatives of a distributed system are best for their implementation. In addition, communication between technicians and managers is educed. Technicians view a system in terms of performance while management sees a system through economy factors; the proposed tool reconciles these views by providing a common meeting ground for determining priorities and trade-offs. Such a unifying approach is crucial in reducing future communication gaps.

## 2. Composition of the tool

Presently, the largest problem in comparing and rating distributed systems lies in the large number of characteristic features to be considered. The proposed tool organizes these factors into seven groups of the system consideration. They are as follows:

1. Operational Characteristics

2. Performance Characteristics

3. Update Characteristics

4. Retrieval Characteristics

5. Economic Characteristics

6. Data Base Size

7. Number and Distribution of Users

Each group contains a number of subitems which, as a whole, constitute the essence of the property under consideration. As some subitems may carry more weight than others in influencing the overall rating of the group, a five-point weighting system is introduced to balance their relative importance. The subitems for each group will be discussed later.

With the distributed system's characteristic features organized as indicated, objective ratings may now be stated for a given system architecture in each area. This allows different distribution alternatives to be compared in the light of their overall ratings.

## 3. Types of distributed systems

The basic forms of distributed systems are described, where each will be rated against the seven groups. These alternatives represent a current view of what distributed systems can become. The reader who desires more information on these is referred to [7].

## 3.1. Centralization (C)

This organization maintains the entire data base at a single, central location. This organization is utilized in most systems today and is particularly well-suited for application where requests are alike from all nodes.

## 3.2. Decentralization

Decentralization, Partitioned (DP). A partitioned data base is often described as multiple logical data bases; i.e., the formerly centralized data is divided across several computers. Data bases are typically partitioned according to required accessibility; that is, files are positioned on the machine where they are likely to receive heaviest usage.

Decentralization, Partitioned, Heterogeneous Software (DPHS). Here a number of different systems are employed in the network. The fundamental issue then becomes the development of a control structure. The integration of different DBMS's involving different data models, data definition languages (DDL), data manipulation languages (DML), and data formats requires a large effort in cross data systems translation technologies. Schemes for global control of the system (to achieve transparency) and global addressing techniques (master directories, schemas) are also needed components.

Decentralization, Partitioned, Heterogeneous Hardware (DPHH). One may use the same data base management system on different computer architectures, usually those of different hardware manufacturers.

Decentralization, Partitioned, Homogeneous Software, Heterogeneous Hardware and Data Compatibility (PHI(DC)). Mixed vendors may present one problem not otherwise encountered, that is, compatibility differences between one machine and another involving the basic codes used for representation of information. Fortunately, the commonly used information codes for internal representation (i.e., ASCII) allow code conversion at this basic level to be feasible and possible, and the frequent use of code conversion tables involves little use of storage and processing power.

Decentralization, Partitioned, Heterogeneous Software/Hardware and Data Compatibility (PHSDC). This configuration presents a very complex situation, as the distributed system embodies a truly distributed data base. Some doubt has been expressed whether organizations need such systems, but there is clearly interest. One insurance company interviewed by P.J. Down [12] is contemplating a distributed system in which each branch office will have its own computer, software, and data. The majority of the transaction processing will thus be made in each specific office, which will be linked to others so that transactions for data not held at that office can be routed to the appropriate location.

Decentralization, Replication (DR). A distributed data base may be primarily based upon the duplication of certain files at some or all the information processors. Duplication may be needed to increase access to the file by providing more paths to it; to provide rapid backup in case of the failure of a device, channel, or information processors accessing the file; or to decrease communications volume and/or dependencies on the communications facilities between information processors. A distributed system in which there is duplication of data between different locations raises the problem of maintaining consistency of the duplicated data, particularly after a system failure. No available software package covers this situation.

Decentralization, Replication, Heterogeneous Software (DRHS). A replicated data base could be supervised by different DBMS software (based upon different data models; i.e., network, hierarchical, relational). This approach involves very complex updating procedures.

Decentralization, Replication, Heterogeneous Hardware (DRHH). Such configurations have different machines, and thus physical data independence becomes extremely important; i.e., the data and the application programs which use it must remain unaffected (except for performance) by changes made to the physical storage structure. Cost/benefit tradeoffs might make certain types of physical independence very expensive.

Decentralization, Replication, Heterogeneous Hardware and Data Compatibility (RHHDC). The problem that faces the designer of a distributed DBMS composed of multiple software and hardware systems on a heterogeneous network is data incompatibility. The problem of disparate internal data representation is complicated by different physical sites running different data base management machines.

Decentralization, Replication, Heterogeneous Software/Hardware and Data Compatibility (RHSHDC). Here data is replicated at multiple heterogeneous sites in order to minimize hardware and transmission costs. Such a system must cope with multiple copies of the same data in one or more logical and/or physical formats. Data compatibility is concerned with translating data from one format (logical or physical) to another. This issue must be addressed when transferring data from one DBMS to another. With different sites running different data base systems, effective data translation becomes critically important.

## 4. Construction and use of the tool

The system configurations are now evaluated against each of the seven characteristic categories. As each category contains many subitems, a tabular format is used. Each subitem is represented as a row in the table; system configurations appear as the columns. A five-point rating scale is used to rank each system on each specific subitem. A five-point weighting factor is then introduced to balance the subitems in proportion to their importance to the group as a whole. The results for each system configuration are totaled, and an overall rating results for each characteristic.

As discussion of system characteristics follows, the reader should remember that the table includes many subitems which may be of little or no consideration to a specific situation. The manager may therefore include only items that are relevant to the environment. The tables can therefore be used as a guide; hardware and software options can be easily compared for performance and economic improvement.

The ratings for each characteristic subitem/system configuration are subjective. Information for the ratings stems from the authors referenced on each of the subitems. The reader may disagree with ratings on several of the items and is welcome to do so. Due to the large number of subitems, the error on each subitem is minimized. Overall evaluation is therefore insensitive to smaller points.

## 5. System evaluation characteristics

The subitems that constitute the seven categories of the distributed system evaluation are:

1. Operational Characteristics - Those factors which encourage easy access, flexibility, and expansion of the system

2. Performance Characteristics - Those factors at the hardware level that influence throughput

3. Update Characteristics - Approaches to the updating of data and how they affect system performance

4. Retrieval Characteristics - The types and distribution of user queries which affect system performance

5. Economic Characteristics -- Elements of present and future cost benefits

6. Data Base Size - The number of schemas and the size of each data base

7. User Characteristics - The geographic distribution of users of the system

The subitems of these seven categories must now be considered.

## 5.1. Operational

Data locality [10,11]. At a single site, data may be spread across multiple storage units to improve load leveling. Multiple sites may allocate data among the sites, with each subset of data being allocated to the site which uses it most. This latter subdivision makes remote access methods essential.

Data distributed by machines [28]. Data may be divided among multiple machines with each subset of data kept locally while summarized data is held at remote machines. This method of distributing data must be enforced managerially within the organization in large enterprises.

Data standards [7]. To manage the data consistently, standards must be developed and implemented throughout the company. Such standards will include the specification of data names and their descriptions. These can be monitored and enforced by the data administrator.

Expertise [12]. People within the data administration function must become expert in using the DBMS and its associated software for solving physical layout problems and extracting logical data.

Available data [30]. The ability to reach many different data bases can provide a terminal user with a rich array of capabilities. To provide high data availability, the system designer must store vital data in duplicate in more than one machine (to allow access during partial system failure).

Resource-sharing [3]. Resource-sharing encompasses a myriad of operational issues that directly affect the operation of distributed data bases. The configuration and homogeneity of the system determine, to a large degree, the technology required. Homogeneous systems will naturally require less effort than heterogeneous systems.

Machine independence [31]. Machine independence is concerned with the change from one set of hardware to another, usually of another manufacturer. Such a change constitutes a radical, painful transformation in most environments.

Evolutionary growth of the data base [23]. The most obvious form of data base growth is the increase in the volume of data of a “horizontal expansion.” Such growth leads to a need to spread the data across machines or storage devices.

Diverse requirements of users [23]. Disregarding the changes to the data base, the addition of new users usually means that they need to see their unique subset. New access paths may need to be established. Additional users may impose more stringent performance or timeliness requirements.

Security [29]. The best configuration is one in which the DBMS is the only system executing on the hardware. Where that is not possible, the DBA should review all hardware and software configurations to determine the threat which might be applied for the specific environment.

Concurrency [16]. The sharing of data among concurrent processes can adversely affect data base integrity and consistency. A large data base must usually allow concurrent processing. The user should not be concerned with other processes that are executing simultaneously.

Localized management [20,12]. A factory or district office may desire to keep its own data. The data are nevertheless used elsewhere, possibly by means of telecommunication links. Localized management and control of data can have advantages; the local organization is fully responsible for accuracy and safekeeping and cannot blame malfunctions on some far distant group.

## 5.2. System performance

Integration [34]. Among homogeneous data base systems, the level of integration effort is small in relation to that of heterogeneous ones. The integration of different DBMS's involving different data models, data definition languages, and data formats requires a large effort in data translation.

System complexity [25]. In general, data base software becomes more complex when it permits logical files to be split. Little software is available to help.

Overlap execution [22]. Simulation studies show that a backend computer can overlap its execution with the host machine, allowing more throughput in the larger computer.

System maturity [15]. A fairly complete analysis of distributed file system designs has been made but actual implementation is dependent upon technological advances in the area of computer networking. On the other hand, the centralized DBMS is mature and this promotes easier implementation and usage.

System overhead [24]. Overhead is defined as non-production effort when the system and its programs are performing administrative (i.e., non-user related) tasks.

Program compatibility [20]. Centralized control is needed to ensure that transfer of applications will be possible without burdensome reprogramming. The data item formats should be centrally controlled, and the same data dictionary should be used everywhere. Only one data description language (DDL) must be used and all schemas reviewed centrally. Only with centralized control is it possible to avoid the crippling problems resulting from piecemeal development.

Data redundancy [32]. Some redundancy exists in order to give improved access, reduced transmission, simple addressing methods, and better recovery from accidental loss of data. Uncontrolled redundancy involves the extra cost of storing multiple copies, serious problems in updating, and probable inconsistencies.

System throughput [18]. In distributed systems, application programs will generally execute faster due to the reduction in traffic. On the other hand, the overhead of the network can reduce the response time for programs initiated across nodes or requesting data from several locations.

Reorganization of data [26]. The process of rearranging the relative physical placement of data units in the data base constitutes reorganization. The reorganization of data in distributed networks is much more difficult than in a centralized DBMS application.

Translation of data [21,24,33]. One of the problems that faces the distributed system is data incompatibility. The problem of disparate internal data representations is complicated by the different logical structures of the data base system. Since differences are a fact of life in data processing, a method of data base translation is necessary for the case of distributed networking.

Response time overhead [8]. Overhead due to the backend approach with respect to response time consists of transmission time of the command to the backend, task queueing delay, possible conversion overhead associated with character sets and data format, and transmission time of the result back to the host.

## 5.3. Economics

Cost [20]. If a system stores its data close to the locations where they originate or are used, there is less transmission of data with a subsequent reduction in telecommunication cost. On the other hand, economics of scale often favor the use of large centralized data storage facilities. There is a cost trade-off between these factors, but the cost of small localized data storage facilities is dropping much faster than the cost of data transmission.

System development [20]. The problems associated with excessively large system development can be alleviated if local organizations develop local data bases and make them work, albeit under centralized constraints, such as data definitions, formats, and schemas.

Hardware cost [6]. Local development and storage of local files has gained popularity and economic viability with the spread of minicomputers with data transmission capability.

Improved utilization of resources [12]. By carefully dividing the data between sites, one improves the utilization of system resources. However, overhead is incurred when remote access is necessary.

Data communication cost [12]. In distributed data bases, a new cost factor is communication, e.g., tariffs. Such tariffs may increase in the future rather than decrease.

Software cost [12]. The cost of distributed network DBMS software is increasing with time as a result of the rising cost of software development personnel and the increasing complexity of network software. There has been little success in providing better software engineering methodology to compensate for higher personnel cost.

Hardware cost [12]. The cost/performance ratio of hardware changes rapidly; mini- and microprocessors have been developed to be used in distributed data environments.

## 5.4. Update

Update from different locations [10,11]. If data is to be updated by transactions from different locations, it should remain in one place so that the updating process with its potential conflicts and deadlocks can be controlled. It is undesirable to have more than one copy of data being updated in different places at the same time.

Dynamic update versus static update [14]. When an elaborate search of the data is necessary in order to respond to spontaneous queries, the data must be structured to facilitate searching. With such structures, it is complex and expensive to update or insert new records. It is sometimes, however, difficult to avoid this complexity. Sometimes it is possible to carry out the updating later on off-line operations.

Redundancy [13,5]. In a replicated data system, multiple updating operations are necessary. Redundancy is therefore expensive for volatile files. Also, because different copies may be in different stages of updating, the system may give inconsistent information.

Deadlock [1]. The possibility of a deadlock in distributed networks is greater than in centralized systems.

## 5.5. Retrieval

Batch query. A batch is a collection of transactions taken over a period of time which are retained for later sequential processing.

On-line query. In an on-line operation, a user has direct and immediate access to the computer system via terminal devices.

On-line query for more than one file. Multiple file capabilities allow direct and immediate access to more than one schema.

On-line query from DEMS distributed geographically. The user has direct and immediate access to a data base management system which connects geographically separated computers together via transmission lines.

Restricted query. The retrieval of the data is pre-defined by the DBMS.

Unrestricted query. In a system that permits spontaneous queries or allows a nonprogrammer user to explore the data base and produce reports, unrestricted queries may be said to occur.

On-line query from homogeneous DBMS. This form presents direct and immediate access to more than one data base management system from the same type.

On-line query from heterogeneous DBMS. Similar to above, this class cf query permits direct and immediate access to more than one DBMS with different sites running different DBMS's.

## 5.6. Data base size

Data base size [27] is the total number of characters required for a representation of the data. This can influence the choice of the data base organization. An organizational method that requires a large amount of overhead per entity would be an unlikely candidate for a large data base. The size also affects the type and number of backend machines selected. We shall divide the data base into four categories:

1. Small: up to 1 M byte

2. Medium: 1 M to 50 M bytes

3. Large: 50 M to 100 M bytes

4. Very large: over 100 M bytes

The most important consideration in defining the need for expansion of data processing and data accessibility is the number of users. The following is our categorization of number of users:

1. Small number locally: 2–16

Small number distributed: 1–8

2. Medium number locally: 16–32
Medium number distributed: 8–16

3. Large number locally: 32–128
Large number distributed: 16–64

4. Very large number locally: 128 and up

Very large number distributed: 64 and up
The tables for each of the seven categories are displayed in Tables 1 through 7. The “Description” column contains abbreviations. “W” denotes the weighting factor. The weighted evaluation of a subitem for a particular configuration is the product of the rating shown multiplied by the weighting factor (as given at the left of the row). The sums of the weighted results are presented in the "total" row of each table. The final row gives the evaluation index - the total weighted score divided by the sum of the subitems' weights. An overall evaluation of each configuration is exhibited in Figure 8, where the seven characteristic factors are themselves weighted and summed.

## 6. Evaluation

The operational table i shows that good results occur in systems with homogeneous hardware and software. Such an effort is seen due to the maturity of the system's development in those areas; heterogeneous networks are still in their infancy. Also note that the centralized system fails to show good results due to the lack of data locality and machine independence in its singular configuration. Data replication versus partitioning has no effect upon the scores. It should be noted that even in centralized systems the need to "distribute" data over several files may be

Table 1

<table><tr><td>Description</td><td>W</td><td>C</td><td>DP</td><td>DPHS</td><td>DPIHH</td><td>PHHDC</td><td>PHSHDC</td><td>DR</td><td>DRHS</td><td>DRHH</td><td>RHSHDC</td></tr><tr><td>Data Locality</td><td>2</td><td>5</td><td>5</td><td>2</td><td>4</td><td>2</td><td>0+</td><td>4</td><td>3</td><td>2</td><td>1</td></tr><tr><td>Data Distributed By Machines</td><td>3</td><td>0</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>5</td><td>4</td><td>3</td><td>1</td></tr><tr><td>Data Standards</td><td>5</td><td>5</td><td>5</td><td>1</td><td>2</td><td>1</td><td>0+</td><td>5</td><td>2</td><td>3</td><td>0+</td></tr><tr><td>Expertise</td><td>4</td><td>5</td><td>3</td><td>2</td><td>2</td><td>1</td><td>1</td><td>3</td><td>2</td><td>2</td><td>1</td></tr><tr><td>Available Data</td><td>5</td><td>5</td><td>4</td><td>2</td><td>2</td><td>1</td><td>1</td><td>5</td><td>3</td><td>2</td><td>1</td></tr><tr><td>Resource-Sharing</td><td>3</td><td>1</td><td>4</td><td>3</td><td>2</td><td>0+</td><td>0+</td><td>4</td><td>2</td><td>1</td><td>0+</td></tr><tr><td>Machine Independence</td><td>5</td><td>5</td><td>3</td><td>1</td><td>0+</td><td>0+</td><td>0+</td><td>3</td><td>1</td><td>0+</td><td>0+</td></tr><tr><td>Evolutionary Growth of DB</td><td>4</td><td>1</td><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>Diverse Requirements of Multiple User&#x27;s</td><td>3</td><td>3</td><td>5</td><td>4</td><td>4</td><td>2</td><td>2</td><td>5</td><td>3</td><td>3</td><td>3</td></tr><tr><td>Security</td><td>4</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0+</td><td>4</td><td>3</td><td>3</td><td>0+</td></tr><tr><td>Concurrency in DBMS</td><td>3</td><td>4</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>Localized Management</td><td>1</td><td>0</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>Index</td><td>42</td><td>153</td><td>180</td><td>123</td><td>107</td><td>68</td><td>54</td><td>179</td><td>119</td><td>106</td><td>59</td></tr><tr><td>Mean</td><td></td><td>3.64</td><td>4.28</td><td>2.92</td><td>2.54</td><td>1.62</td><td>1.28</td><td>4.26</td><td>2.83</td><td>2.52</td><td>1.40</td></tr></table>

Table 2

<table><tr><td>Description</td><td>W</td><td>C</td><td>DP</td><td>DPHS</td><td>DPHH</td><td>PHHDC</td><td>PHSHDC</td><td>DR</td><td>DRHS</td><td>DRHH</td><td>RHHDC</td><td>RHSHDC</td></tr><tr><td>Integration</td><td>3</td><td>3</td><td>4</td><td>2</td><td>2</td><td>1</td><td>0+</td><td>5</td><td>3</td><td>3</td><td>1</td><td>0+</td></tr><tr><td>System Complexity</td><td>2</td><td>5</td><td>4</td><td>2</td><td>2</td><td>1</td><td>0+</td><td>2</td><td>2</td><td>2</td><td>0+</td><td>0+</td></tr><tr><td>Execution Overhead</td><td>1</td><td>1</td><td>4</td><td>3</td><td>3</td><td>1</td><td>0+</td><td>5</td><td>4</td><td>4</td><td>2</td><td>1</td></tr><tr><td>Overlap Execution</td><td>3</td><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>System Maturity</td><td>4</td><td>5</td><td>3</td><td>2</td><td>2</td><td>0+</td><td>0+</td><td>4</td><td>3</td><td>3</td><td>0+</td><td>0+</td></tr><tr><td>System Overhead</td><td>2</td><td>5</td><td>3</td><td>2</td><td>2</td><td>1</td><td>0+</td><td>2</td><td></td><td>1</td><td>0+</td><td>0+</td></tr><tr><td>Program Compatibility</td><td>5</td><td>5</td><td>4</td><td>2</td><td>1</td><td>0+</td><td>0+</td><td>5</td><td>3</td><td>2</td><td>0+</td><td>0+</td></tr><tr><td>Data Redundancy</td><td>4</td><td>4</td><td>5</td><td>5</td><td>5</td><td>2</td><td>2</td><td>5</td><td>5</td><td>4</td><td>2</td><td>2</td></tr><tr><td>System Throughput</td><td>1</td><td>2</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>Reorganization of Data</td><td>3</td><td>5</td><td>4</td><td>4</td><td>2</td><td>0+</td><td>0+</td><td>5</td><td>4</td><td>2</td><td>0+</td><td>0+</td></tr><tr><td>Restructure of Data</td><td>3</td><td>5</td><td>4</td><td>3</td><td>2</td><td>0+</td><td>0+</td><td>3</td><td>2</td><td>1</td><td>0+</td><td>0+</td></tr><tr><td>Translation of Data</td><td>4</td><td>5</td><td>5</td><td>3</td><td>2</td><td>0+</td><td>0+</td><td>5</td><td>3</td><td>2</td><td>0+</td><td>0+</td></tr><tr><td>Response Time Overhead</td><td>1</td><td>3</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0+</td><td>5</td><td>4</td><td>3</td><td>1</td><td>0+</td></tr><tr><td>Total</td><td>36</td><td>161</td><td>147</td><td>110</td><td>89</td><td>34</td><td>25</td><td>154</td><td>116</td><td>93</td><td>30</td><td>25</td></tr><tr><td>Mean</td><td></td><td>4.47</td><td>4.08</td><td>3.05</td><td>2.47</td><td>.94</td><td>.69</td><td>4.28</td><td>3.22</td><td>2.58</td><td>.83</td><td>.69</td></tr></table>

needed to improve reliability and timing, etc. One implication drawn from these results is that from a purely operational point of view, a homogeneous distributed partitioned system presents a definite step up from a centralized system.

Totals from the system performance table 2 show that centralized systems score well due to the total lack of compatibility problems. In contrast, distributed systems suffer due to the lack of maturity – data translation and program compatibility problems are as yet unsolved. Note that replication provides better performance than data partitioning due to the locality of data, an implementation which is truly an extension of the centralized philosophy.

Update considerations in table 3 show that centralizing versus partitioning gives almost the same results.

Table 3

<table><tr><td>Description</td><td>W</td><td>C</td><td>DP</td><td>DPHS</td><td>DPHH</td><td>PHHDC</td><td>PHSHDC</td><td>DR</td><td>DRHS</td><td>LFHH</td><td>RHHDC</td><td>RMSHDC</td></tr><tr><td>Update From Different Location</td><td>4</td><td>4</td><td>5</td><td>3</td><td>2</td><td>0+</td><td>0+</td><td>3</td><td>2</td><td>1</td><td>0+</td><td>0+</td></tr><tr><td>Dynamic Update</td><td>4</td><td>5</td><td>5</td><td>3</td><td>2</td><td>0+</td><td>0+</td><td>2</td><td>1</td><td>1</td><td>0+</td><td>0+</td></tr><tr><td>Static Update</td><td>4</td><td>5</td><td>4</td><td>3</td><td>2</td><td>0+</td><td>0+</td><td>2</td><td>1</td><td>1</td><td>0+</td><td>0+</td></tr><tr><td>Redundancy of Data</td><td>5</td><td>3</td><td>3</td><td>2</td><td>2</td><td>0+</td><td>0+</td><td>5</td><td>5</td><td>5</td><td>0+</td><td>0+</td></tr><tr><td>Deadlock</td><td>1</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>Total</td><td>18</td><td>75</td><td>75</td><td>50</td><td>38</td><td>6</td><td>4</td><td>58</td><td>46</td><td>42</td><td>5</td><td>5</td></tr><tr><td>Mean</td><td></td><td>4.17</td><td>4.17</td><td>2.78</td><td>2.11</td><td>.22</td><td>.22</td><td>3.22</td><td>2.56</td><td>2.33</td><td>.28</td><td>.28</td></tr></table>

Table 4

<table><tr><td>Description</td><td>W</td><td>C</td><td>DP</td><td>DPHS</td><td>DPHH</td><td>PHHDC</td><td>PHSHDC</td><td>DR</td><td>DRHS</td><td>DRHH</td><td>RHHDC</td><td>RHSHDC</td></tr><tr><td>Batch Query</td><td>3</td><td>5</td><td>3</td><td>2</td><td>2</td><td>0+</td><td>0+</td><td>3</td><td>2</td><td>2</td><td>0+</td><td>0+</td></tr><tr><td>On-Line Query</td><td>5</td><td>3</td><td>5</td><td>2</td><td>2</td><td>0+</td><td>0+</td><td>5</td><td>4</td><td>4</td><td>0+</td><td>0+</td></tr><tr><td>On-Line Query For More Than One File</td><td>3</td><td>3</td><td>4</td><td>2</td><td>2</td><td>0+</td><td>0+</td><td>5</td><td>4</td><td>4</td><td>0+</td><td>0+</td></tr><tr><td>On-Line Query From DB Distributed Geographically</td><td>4</td><td>1</td><td>4</td><td>2</td><td>2</td><td>1</td><td>1</td><td>5</td><td>4</td><td>4</td><td>1</td><td>1</td></tr><tr><td>Restricted Query</td><td>4</td><td>5</td><td>3</td><td>1</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>Unrestricted Query</td><td>1</td><td>5</td><td>4</td><td>3</td><td>3</td><td>2</td><td>2</td><td>5</td><td>3</td><td>3</td><td>2</td><td>2</td></tr><tr><td>Query From Homogenous DB</td><td>2</td><td>5</td><td>5</td><td>5</td><td>5</td><td>2</td><td>1</td><td>5</td><td>5</td><td>5</td><td>2</td><td>1</td></tr><tr><td>Query From Heterogenous DB</td><td>2</td><td>1</td><td>4</td><td>4</td><td>4</td><td>1</td><td>1</td><td>5</td><td>5</td><td>5</td><td>1</td><td>1</td></tr><tr><td>Total</td><td>24</td><td>80</td><td>86</td><td>55</td><td>55</td><td>16</td><td>14</td><td>102</td><td>85</td><td>85</td><td>20</td><td>18</td></tr><tr><td>Mean</td><td></td><td>3.30</td><td>3.58</td><td>2.29</td><td>2.29</td><td>.67</td><td>.58</td><td>4.25</td><td>3.54</td><td>3.54</td><td>.83</td><td>.75</td></tr></table>

Replication of data requires more update overhead and consequently such systems do poorly. Note also that performance is reduced significantly when there are hardware/software incompatibilities.

The other end of data access, retrieval, in table 4, shows that the replicated distributed system provides an excellent query environment. Centralization fares poorly, due to the absence of data locality. Tables 3 are 4 are really complementary views; a comparison of the tables shows that some form of a partitioned system gives good balance between data retrieval and update. Keplication should only be considered when retrievals constitute a large portion of the user requests.

Table 5

<table><tr><td>Description</td><td>W</td><td>C</td><td>DP</td><td>DPHS</td><td>DPHH</td><td>PHHDC</td><td>PHSHDC</td><td>DR</td><td>DRHS</td><td>DRHH</td><td>RHHDC</td><td>RHSHDC</td></tr><tr><td>Personnel Cost</td><td>5</td><td>5</td><td>3</td><td>2</td><td>2</td><td>1</td><td>0+</td><td>2</td><td>1</td><td>1</td><td>0+</td><td>0+</td></tr><tr><td>System Development</td><td>4</td><td>5</td><td>4</td><td>2</td><td>2</td><td>1</td><td>0+</td><td>2</td><td>1</td><td>0+</td><td>0+</td><td>0+</td></tr><tr><td>Hardware Cost</td><td>5</td><td>3</td><td>4</td><td>4</td><td>5</td><td>4</td><td>4</td><td>5</td><td>4</td><td>5</td><td>4</td><td>4</td></tr><tr><td>Improved Utilization of Resources</td><td>3</td><td>2</td><td>5</td><td>4</td><td>5</td><td>4</td><td>4</td><td>4</td><td>3</td><td>4</td><td>3</td><td>4</td></tr><tr><td>Data Communication Cost</td><td>4</td><td>5</td><td>3</td><td>2</td><td>3</td><td>1</td><td>0+</td><td>4</td><td>3</td><td>3</td><td>2</td><td>1</td></tr><tr><td>Software Cost</td><td>5</td><td>5</td><td>4</td><td>2</td><td>1</td><td>0+</td><td>0+</td><td>3</td><td>1</td><td>1</td><td>0+</td><td>0+</td></tr><tr><td>Cost/Performance</td><td>2</td><td>3</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0+</td><td>5</td><td>4</td><td>4</td><td>3</td><td>2</td></tr><tr><td>R &amp; D Cost</td><td>5</td><td>5</td><td>4</td><td>2</td><td>2</td><td>0+</td><td>0+</td><td>3</td><td>1</td><td>1</td><td>0+</td><td>0+</td></tr><tr><td>Expansion Costs</td><td>5</td><td>2</td><td>4</td><td>3</td><td>5</td><td>5</td><td>5</td><td>4</td><td>4</td><td>4</td><td>5</td><td>5</td></tr><tr><td>Update Cost (Per Unit)</td><td>1</td><td>5</td><td>5</td><td>3</td><td>4</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0+</td></tr><tr><td>Retrieval Cost (Per Unit)</td><td>1</td><td>4</td><td>4</td><td>3</td><td>3</td><td>1</td><td>1</td><td>5</td><td>4</td><td>4</td><td>3</td><td>2</td></tr><tr><td>Total</td><td>40</td><td>161</td><td>159</td><td>105</td><td>121</td><td>72</td><td>75</td><td>137</td><td>93</td><td>97</td><td>72</td><td>67</td></tr><tr><td>Mean</td><td></td><td>4.02</td><td>3.97</td><td>2.62</td><td>3.02</td><td>1.80</td><td>1.85</td><td>3.42</td><td>2.32</td><td>2.42</td><td>1.80</td><td>1.67</td></tr></table>

Table 5 shows the totals for the economic factors, which suggest that the replicated systems are not economical—extra copies of the data mean extra cost for storage and maintenance. Note also that usage of heterogeneous hardware and software plays a positive role, in that one may obtain a better price on a system configuration by choosing different vendors; however, one "pays" for this in other categories.

Table 6

<table><tr><td>Description</td><td>W</td><td>C</td><td>DP</td><td>DPHS</td><td>DPHH</td><td>PHHDC</td><td>PHSHDC</td><td>DR</td><td>DRHS</td><td>DRHH</td><td>RHHDC</td><td>RHSHDC</td></tr><tr><td>a. Small Data Base Up To 1 MBytes</td><td>1</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>b. Medium Size DB Up To 50 MBytes</td><td>1</td><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>c. Large DB Up To 100 MBytes</td><td>3</td><td>5</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>d. Very Large DB Above 100 MBytes</td><td>5</td><td>4</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>e. Small Number of Schemas</td><td>1</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>f. Medium Number of Schemas</td><td>2</td><td>4</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>g. Large Number of Schemas</td><td>3</td><td>3</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>h. Very Large Number of Schemas</td><td>5</td><td>2</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>i. Combination of e &amp; a</td><td>1</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>j. Combination of e &amp; b</td><td>1</td><td>4</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>k. Combination of e &amp; c</td><td>2</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>l. Combination of e &amp; d</td><td>3</td><td>4</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>m. Combination of f &amp; a</td><td>2</td><td>3</td><td>4</td><td>5</td><td>3</td><td>2</td><td>1</td><td>4</td><td>3</td><td>3</td><td>1</td><td>1</td></tr><tr><td>n. Combination of f &amp; b</td><td>2</td><td>3</td><td>4</td><td>3</td><td>3</td><td>2</td><td>1</td><td>3</td><td>3</td><td>3</td><td>1</td><td>1</td></tr><tr><td>o. Combination of f &amp; c</td><td>2</td><td>3</td><td>4</td><td>3</td><td>3</td><td>2</td><td>1</td><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>p. Combination of f &amp; d</td><td>4</td><td>3</td><td>4</td><td>3</td><td>3</td><td>2</td><td>1</td><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>q. Combination of g &amp; a</td><td>1</td><td>2</td><td>4</td><td>3</td><td>3</td><td>2</td><td>1</td><td>4</td><td>2</td><td>2</td><td>1</td><td>0+</td></tr><tr><td>r. Combination of g &amp; b</td><td>2</td><td>2</td><td>4</td><td>3</td><td>3</td><td>2</td><td>1</td><td>3</td><td>2</td><td>2</td><td>1</td><td>0+</td></tr><tr><td>s. Combination of g &amp; c</td><td>3</td><td>2</td><td>4</td><td>3</td><td>3</td><td>2</td><td>1</td><td>3</td><td>2</td><td>2</td><td>1</td><td>0+</td></tr><tr><td>t. Combination of g &amp; d</td><td>4</td><td>2</td><td>4</td><td>3</td><td>3</td><td>2</td><td>1</td><td>2</td><td>2</td><td>2</td><td>1</td><td>0+</td></tr><tr><td>u. Combination of h &amp; a</td><td>2</td><td>1</td><td>4</td><td>3</td><td>3</td><td>2</td><td>1</td><td>4</td><td>3</td><td>3</td><td>2</td><td>1</td></tr><tr><td>v. Combination of h &amp; b</td><td>3</td><td>1</td><td>4</td><td>3</td><td>3</td><td>2</td><td>1</td><td>3</td><td>2</td><td>2</td><td>0+</td><td>0+</td></tr><tr><td>w. Combination of h &amp; c</td><td>4</td><td>1</td><td>4</td><td>2</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td><td>1</td><td>0+</td><td>0+</td></tr><tr><td>x. Combination of h &amp; d</td><td>5</td><td>1</td><td>4</td><td>2</td><td>2</td><td>1</td><td>1</td><td>1</td><td>0+</td><td>0+</td><td>0+</td><td>0+</td></tr><tr><td>Total</td><td>62</td><td>167</td><td>237</td><td>198</td><td>198</td><td>164</td><td>129</td><td>143</td><td>114</td><td>114</td><td>86</td><td>74</td></tr><tr><td>Mean</td><td></td><td>2.69</td><td>3.82</td><td>3.19</td><td>3.19</td><td>2.64</td><td>2.08</td><td>2.31</td><td>1.84</td><td>1.84</td><td>1.39</td><td>1.19</td></tr></table>

The effect of size of the data base and number of schemas is shown in table 6. Only a partitioned system performs well when the size and number of users increase. The choice of replication ruins any hope of reasonable expansion, and a centralized configuration simply cannot cope with growth.

Table 7 shows that as the consideration of the users' needs increase, a replicated system appears to be best. A replicated system is responsive because data can be located wherever there is a demand. The use of homogeneous versus heterogeneous hardware/software is thus minimized.

Table 7

<table><tr><td>Description</td><td>W</td><td>C</td><td>DP</td><td>DPHS</td><td>DPHH</td><td>PHHDC</td><td>PHSHDC</td><td>DR</td><td>DRHS</td><td>DRHH</td><td>RHHDC</td><td>RHSHDC</td></tr><tr><td>a. Small Number Locally 2-16</td><td>1</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>b. Medium Number Locally 16-32</td><td>2</td><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>c. Large Number Locally 32-128</td><td>3</td><td>4</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>d. Very Large Number Locally 128 and Up</td><td>5</td><td>3</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>e. Small Distributed Geographically 1-8</td><td>1</td><td>3</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>f. Medium Distributed Geographically 16-32</td><td>2</td><td>2</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>g. Large Distributed Geographically 16-64</td><td>3</td><td>1</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>h. Very Large Distributed Geographically 64 and Up</td><td>5</td><td>0+</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>4</td><td>4</td><td>4</td><td>4</td><td>3</td></tr><tr><td>i. Combination of a &amp; e</td><td>1</td><td>3</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>j. Combination of a &amp; e</td><td>1</td><td>3</td><td>5</td><td>5</td><td>4</td><td>4</td><td>4</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>k. Combination of a &amp; g</td><td>3</td><td>2</td><td>5</td><td>5</td><td>4</td><td>4</td><td>4</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>l. Combination of a &amp; h</td><td>5</td><td>1</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>4</td><td>4</td><td>4</td><td>4</td><td>3</td></tr><tr><td>m. Combination of b &amp; e</td><td>1</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>3</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>n. Combination of b &amp; f</td><td>2</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>3</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>o. Combination of b &amp; g</td><td>3</td><td>3</td><td>4</td><td>4</td><td>4</td><td>4</td><td>3</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>p. Combination of b &amp; h</td><td>4</td><td>1</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>5</td><td>5</td><td>5</td><td>5</td><td>3</td></tr><tr><td>q. Combination of c &amp; e</td><td>4</td><td>3</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>r. Combination of c &amp; f</td><td>4</td><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>s. Combination of c &amp; g</td><td>4</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>t. Combination of c &amp; h</td><td>4</td><td>2</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>u. Combination of d &amp; e</td><td>5</td><td>3</td><td></td><td>3</td><td>3</td><td>3</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td></tr><tr><td>v. Combination of d &amp; f</td><td>5</td><td>3</td><td></td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>w. Combination of d &amp; g</td><td>5</td><td>2</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>x. Combination of d &amp; h</td><td>5</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>Total</td><td>78</td><td>196</td><td>266</td><td>256</td><td>253</td><td>253</td><td>237</td><td>300</td><td>300</td><td>300</td><td>300</td><td>277</td></tr><tr><td>Mean</td><td></td><td>2.50</td><td>3.41</td><td>3.28</td><td>3.24</td><td>3.24</td><td>3.03</td><td>3.85</td><td>3.85</td><td>3.85</td><td>3.85</td><td>3.55</td></tr></table>

As a general aid in considering the categories together, a trade off summary is presented in table 8. One notes that the partitioned system presents the best overall balance, primarily due to its strong performance in the areas of operations, economics, user considerations, and update features. Replicated systems make up the next general group. The centralized system falls to the bottom primarily because it is not flexible to growth, i.e., it is not cost effective. This becomes apparent when one considers the economic factors of expansion.

Figure 1 gives a graphical comparison of the system configurations in the general performance areas, viz., performance, retrieval, and update. One notes that the performance graph alone provides a good measure of a balanced retrieval versus based system. One must also conclude that there are other important factors which contribute to performance characteristics, hence, the discrepancy in the curves. There definitely is room for improvement in the retrieval and update areas. Results similar to the performance ratings must be realized to produce a truly well-rounded system.

A grouping of major “trade-off” areas is shown in figure 2. The effect of performance on economics is especially noticeable. Although it might appear that a system should be selected which minimizes these discrepancies in the graphs (and thus eliminates the trade-off decision), the better solution is to choose a scheme which presents high scores for all important areas. The simple partitioned configuration then becomes a good choice.

Replication is definitely the most volatile – the distributed replicated heterogeneous hardware system eliminates the trade-off factor. This oddity occurs because the balance between performance and cost is maintained by the amount of duplicated data in the system. However, one can see that such a configuration is definitely not generally the “best” choice.

The user and size factors are compared in figure 3; apparently no matter how good the performance, a replicated system is a potential disaster if the data base has a possibility for extensive growth. Only the partitioned system presents a safe choice when the

Table 8

<table><tr><td>Description</td><td>Average</td><td>W</td><td>C</td><td>DP</td><td>DPHS</td><td>DPHH</td><td>PHHDC</td><td>PHSHDC</td><td>DR</td><td>DRHS</td><td>DRHH</td><td>RHHDC</td><td>RHSHDC</td></tr><tr><td>Operational</td><td>143.4513.04</td><td>5</td><td>3.6418.2</td><td>4.2821.4</td><td>2.9214.6</td><td>2.5412.2</td><td>1.628.1</td><td>1.286.4</td><td>4.2621.3</td><td>2.8314.15</td><td>2.5212.6</td><td>1.407.0</td><td>1.407.0</td></tr><tr><td>System Performance</td><td>109.29.93</td><td>4</td><td>4.4717.88</td><td>4.0816.32</td><td>3.0512.2</td><td>2.479.88</td><td>.943.76</td><td>.692.76</td><td>4.2817.12</td><td>3.2212.88</td><td>2.5810.32</td><td>.833.32</td><td>.692.76</td></tr><tr><td>Economically</td><td>144.5513.14</td><td>5</td><td>4.0220.1</td><td>3.9719.85</td><td>2.6213.1</td><td>3.0215.1</td><td>1.809.00</td><td>1.859.25</td><td>3.4217.1</td><td>2.3211.6</td><td>2.4212.1</td><td>1.809.00</td><td>1.678.35</td></tr><tr><td>Update</td><td>45.684.15</td><td>2</td><td>4.178.34</td><td>4.178.34</td><td>2.785.56</td><td>2.114.22</td><td>.721.44</td><td>.22.44</td><td>3.226.44</td><td>2.565.12</td><td>2.334.66</td><td>.78.51</td><td>.28.56</td></tr><tr><td>Query</td><td>76.956.99</td><td>3</td><td>3.359.99</td><td>3.5810.74</td><td>2.296.87</td><td>2.296.87</td><td>.672.01</td><td>.581.74</td><td>4.2512.75</td><td>3.5410.62</td><td>3.5410.62</td><td>.832.49</td><td>.752.25</td></tr><tr><td>DB Size and No. Schema</td><td>26.182.38</td><td>1</td><td>2.692.69</td><td>3.823.82</td><td>3.193.19</td><td>3.193.19</td><td>2.642.64</td><td>2.082.08</td><td>2.312.31</td><td>1.841.84</td><td>1.841.84</td><td>1.391.39</td><td>1.191.19</td></tr><tr><td>User&#x27;s</td><td>112.9610.27</td><td>3</td><td>2.507.50</td><td>3.4110.23</td><td>3.289.84</td><td>3.249.72</td><td>3.249.72</td><td>3.039.09</td><td>3.8511.55</td><td>3.8511.55</td><td>3.8511.55</td><td>3.8511.55</td><td>3.5510.66</td></tr><tr><td>Total</td><td>28.69</td><td>23</td><td>84.7</td><td>91.7</td><td>65.36</td><td>61.78</td><td>36.69</td><td>31.76</td><td>88.57</td><td>67.76</td><td>63.69</td><td>35.31</td><td>32.77</td></tr><tr><td>Mean</td><td>2.61</td><td></td><td>3.68</td><td>3.99</td><td>2.84</td><td>2.69</td><td>1.59</td><td>1.38</td><td>3.85</td><td>2.95</td><td>2.72</td><td>1.53</td><td>1.42</td></tr></table>

![](/api/attachments/CV3V6SYV/fulltext/images/7208a60363128f3d19b201d6bbe543465b57fe511495f69b4da26d920606291e.jpg)  
Fig. 1

![](/api/attachments/CV3V6SYV/fulltext/images/734ea1d938f484ebadf752856649f73279c59ce24807215f25f9b24bf263a03d.jpg)  
Fig. 2

![](/api/attachments/CV3V6SYV/fulltext/images/97c2d69e803c78cc8a52001a01e4e99987b1c50b3b3d1a76bafbfeab0f01ac79.jpg)  
Fig. 3  
data base size is volatile - one negative factor has a definite influence over all others.

Finally, we can validate our results by looking at other relevant work. Most current and earlier research papers have asked: "What is the optimal data file allocation scheme (in terms of cost) for a system with a given degree of replication?" These papers consider the factors of system node distribution, communication lines speeds, data storage costs, level of data sharing, and behavior of access patterns. Mathematical models for answering this question for a given system have been developed [17,19]. However, only [10,11] and [9] present generalized results. They conclude that simple partitioning is recommended for systems whose traffic consists of a majority of updates. Centralization is also an acceptable alternative. A replicated system becomes viable only when updates drop below the ten percent level. Tables 3 and 4 of this paper agree with these results. When updates become a primary consideration, table 3 indicates that the centralized or partitioned schemes provide good results. However, when retrievals provide the primary traffic, the replicated system performs better, as shown in table 4.

## 7. Conclusion

The evaluation tool presented in this paper has proved to be easy to use and an effective device for comparing data base system configurations. One can measure trade-off factors in developing a system and use them to view progress in the improvement of the state-of-the-art.

One must obviously ask what conclusions can be drawn from the tables and graphs in terms of a "best" configuration. First, a partitioned system has become a realizable, attractive replacement for existing centralized systems. There no longer need be fear about building and using such a configuration. Second, distributed systems which replicate data should be considered for use only in specialized situations, e.g., exclusive on-line retrieval with batch updating. The potential for ruin in a replicated system directly increases with the amount of growth projected. Finally, problems still exist in the use of heterogeneous hardware and software in a system. The lack of maturity and use of such systems remains the culprit. Hopefully, research in this area will bring their use up to the level of success currently enjoyed by heterogeneous systems.

## References

[1] P.A. Alsberg and J.D. Day, "A Principle for Resilient Sharing of Distributed Resources," Report from the Center for Advanced Computation, University of Illinois at Urbana-Champagne, Urbana, IL, 1976.

[2] P.A. Alberg, G.G. Belford, S.R. Bunch, J.D. Day, E. Grapa, D.C. Healy, E.J. McCauley, and D.A. Willcox, "Synchronization and Deadlock," PAC Document Number 185, CCTC-WAD 6503, Center For Advanced Computation, University of Illinois at Urbana-Champagne, Urbana, IL, March 1, 1976.

[3] J.L. Berg, Editor. "Data Base Directions, The Next Steps," Proceedings of the Workshop of the National Bureau of Standards, Pub. 451 and ACM held at Ft. Lauderdale, FL, October 29-31, 1975.

[4] P.A. Bernstein, N. Goodman, J.B. Rothnie, C.A. Papadimitrious, "Analysis of Serializability in SDD-1: A System for Distributed Data Base (The Fully Distributed Case)," Proceedings First International Conference on Computer Software and Application, IEEE Computer Society, Chicago, IL, November 1977. (Also available from Computer Corporation of America, 575 Technology Square, Cambridge, MA 02139 as Technical Report No. CCA-77-05.)

[5] P.A. Bernstein, N. Goodman, J.B. Rothnie, D.W. Shipman, "The SDD-I Redundant Update Algorithm: The General Case," Computer Corporation of America, 575 Technology Square, Cambridge, MA 02139, Technical Report No. CCA-77-09, August 1, 1977.

[6] P.B. Berra, "Data Base Machines," ACM SIGIR Forum, Volume XII, Number 3, Winter 1977, pp. 4–23.

[7] G.M. Booth, "Distributed Data Bases: Their Structure and Use," Infotech State of the Art Report, Distributed Systems, pp. 201–213, 1976.

[8] R.E. Canaday, et al., "A Back-end Computer for Data Base Management," CACM, Volume 17, Number 10, October 1974, pp. 575–582.

[9] R.G. Casey, "Allocation of Copies of a File in an Information Network," Proceedings AFIPS SJCC, Volume 40, 1972, pp. 618–623.

[10] W.W. Chu, "Optimal File Allocation in Computer Networks," In Computer Communication Networks, Kuo, F.F., Editor, Prentice-Hall, Computer Applications in Electrical Engineering Series, Prentice-Hall, Inc., Englewood Cliffs, NJ, 1973.

[11] W.W. Chu, "Performance of File Directory Systems for Data Bases in Star and Distributed Networks," Proceedings AFIPS NCC. Volume 45, June 1976, pp. 585–593.

[12] P.J. Down and F.E. Taylor, "Why Distributed Computing," Published by NCC Publication, 1978.

[13] C.A. Ellis, "A Robust Algorithm for Updating Duplicate Data Bases," Proceeding 1977 Berkeley Workshop on Distributed Data Management and Computer Networks, Lawrence Berkeley Laboratory, University of California, Berkeley, CA, May 1977, pp. 146–158.

[14] K.P. Eswaran, J.N. Graph, R.A. Lorie and I.L. Traiger, "The Notions of Consistency and Predicate Locks in a Data Base System," CACM, Volume 19, Number 11, November 1976, pp. 624–633.

[15] J.P. Fry and E.H. Sibley, "Evolution of Data Base Management Systems," Computing Surveys, Volume 8, Number 1, March 1976, pp. 7–42.

[16] P.F. King and A.J. Collmeyer, "Data Base Sharing – An Efficient Mechanism For Supporting Concurrent Processes," Data Base Management, B. Schneiderman, (Ed), 1978, pp. 110.

[17] K.D. Levin and H.M. Morgan, "Optimizing Distributed Data Bases - A Framework for Research," Proceedings AFIPS NCC, Volume 44, June 1975, pp. 472-478.

[18] M.S. Loomis and G.J. Popek, "A Module for Data Base Distribution," Symposium on Trends and Application, 1976 Computer Networks, IEEE, pp. 162–169, 1976.

[19] S. Mahmoud and J.S. Riordon, "Optimal Allocation of Resources in Distributed Information Networks," ACM Trans. on Database Systems, 1: 1, pp. 65–83.

[20] J. Martin, "Principles of Data Base Management," Prentice-Hall, Inc., Englewood Cliffs, NJ, 1975.

[21] F.J. Maryanski, "A Survey of Developments in Distributed Data Base Management Systems," Computer, Volume 11, Number 2, February 1978, pp. 28–38.

[22] F.J. Maryanski and V.E. Wallentine, "A Simulation Model of a Backend Data Base Management System,"

Proceedings Pittsburgh Modeling and Simulation Conference, April 1976, pp. 252–257.

[23] H.S. Meltzer, "Data Base Concept and an Architecture for a Data Base System," Proceedings of SHARE, XXXIII, Boston, August 1969, pp. 315–470.

[24] A.G. Merten and J.P. Fry, "A Data Description Language Approach to File Translation," Proceedings ACM SIGMOD Workshop, May 1974, pp. 191–205.

[25] R.L. Nolan, "Computer Data Base: The Future is Now," Harvard Business Review, September-October 1975, pp. 101.

[26] I. Palmer, "Data Base Systems: A Practical Reference," Q.E.D. Information Sciences, Inc., Wellesley, MA, 1976.

[27] N.S. Prywes, "Structure and Organization of Very Large Data Bases," Critical Factors in Data Management, ed., F. Gruenberger, Prentice-Hall, Inc., Englewood Cliffs, NJ, 1969.

[28] C.V. Ramamoorthy, G.S. Ho, T. Krishnarao and B.W. Wah, "Architectural Issues in Distribution Data Base Systems," Proceedings Very Large Data Bases, Third

International Conference, October 1977, pp. 121–126.

[29] B. Ruder, "Security Mechanisms for Protecting Data in a DBMS Environment," Auerbach Information Management Series, Auerbach Publishers Inc., 22-03-11, 1976.

[30] V.L. Shatz, "Computer Network for Retail Stores," Computer, 1973, pp. 21–25.

[31] L.B. Smith, "Data Independence in DBMS," Auerbach Publishers, Inc., Auerbach Information Management Series 22-03-08, 1976.

[32] M. Stonebraker and E. Neuhold, "A Distribution Data Base Version of Ingres," 1977 Berkeley Workshop on Distributed Data Management and Computer Networks, Lawrence Berkeley Laboratory, University of California, Berkeley, CA, May 1977, pp. 10–36.

[33] S.U.W. Su and H. Lam, "A Semi-Automatic Data Translation Scheme for Achieving Data Sharing in a Network Environment," Proceedings ACM SIGMOD Workshop, May 1974, pp. 227–247.

[34] D. Tsichritzis, "Features for a Conceptual Schema," CSRG Report 56, University of Toronto, 1975.
