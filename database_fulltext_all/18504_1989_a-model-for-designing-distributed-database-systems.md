---
otero_id: 18504
otero_key: "E6M3HCYA"
title: "A model for designing distributed database systems"
authors: "Sudha Ram"
year: "1989"
journal: "Information & Management"
doi: "10.1016/0378-7206(89)90018-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Model for Designing Distributed Database Systems

Sudha Ram

Department of Management Information Systems, Karl Eller Graduate School of Management, University of Arizona, Tucson, AZ 85721, USA

In designing distributed database systems, an important issue is the location of various copies of each database. This is known as the File Allocation Problem (FAP). This paper examines the impact of incorporating a specific concurrency control mechanism (CCM) into the FAP. Several mechanisms can be used, and, depending on the choice, the communication flows in the network will vary. In order to allocate data optimally, one must identify the exact communication flows. It is this that has been ignored in past research. Here a non-linear integer programming model has been formulated for the FAP. It incorporates the Central Node Locking mechanism for concurrency control. The model has been solved using an algorithm called ZOOM/XMP. Detailed analysis has been carried out for various configurations. Assumed values have been used for the various non-decision parameters that need to be entered.

Keywords: Distributed Database Systems, File Allocation, Concurrency Control, Communication Networks, Integer Programming, Two Phase Locking.

![](/api/attachments/E6M3HCYA/fulltext/images/0efd2de2924cd5efbfddb804ccca0fc0a9170d64d5cc19e8f16b66ed644d4149.jpg)

Sudha Ram is Assistant Professor at the Department of Management Information Systems, University of Arizona, Tucson. She received her PhD. in MIS from the University of Illinois at Urbana-Champaign in 1985. She has worked on several research projects dealing with database design for organizations such as IBM, NCR, US Army Corp. of Engineers, and the US department of Agriculture. Her teaching and research emphasis are in distributed database systems, automated tools for database design and expert systems applications in business. She has published several papers in these areas.

## 1. The Importance of Distributed Databases

A Distributed Database System (DDS) is a collection of data that are spread across different computers connected together using a communications network [7]. Each site of the network has autonomous processing capability and can perform local applications. Each site also participates in the execution of one or more global applications, which require accessing data at several sites using the network. A user is unaware of the distribution since the system is managed by a single Distributed Database Management System (DDBMS) [2]. The most important feature of distributed data bases is the concept of “cooperation among autonomous sites”.

DDS are used in applications requiring access to an integrated database from geographically dispersed locations. Such applications include banking, military command and control, and inventory control. In addition to the advantage of distributing a single database, advanced communication technology allows the integration of existing distinct, and perhaps radically different, databases for the purpose of sharing valuable information [24]. Such heterogeneous systems are also called DDS. However, the potential advantages of DDS cannot be had without considerable effort. The complexity of such systems is due mainly to the requirement for interaction which poses several design problems.

In this paper we attempt to provide guidelines for designing distributed data base systems by simultaneously considering several of the design issues. Specifically this research addresses the issue of allocating databases across the sites of a computer network, taking into account a concurrency control mechanism. In order to allocate databases, the exact communication flows in the network need to be identified. These, in turn, depend on the pattern of queries (read and write) and the concurrency control mechanism.

## 2. Issues in the Design of Distributed Databases

The main decisions in the design of distributed databases concern:

1. Data Distribution: the question of how to distribute the data among the various sites and what degree of data duplication to allow.

2. Function Distribution: the placement of system-level data management functions. They are clustered to build the user-level functions, such as retrieve, modify, add, and delete.

3. Concurrency Control Mechanisms: the issue of how to maintain consistency among the different copies of the data items, while allowing concurrent accesses to the data.

4. Request Decomposition: transforming high-level non-procedural request into low-level, procedural ones.

Each of these issues has been fairly well researched [5], [15]. However, most has focused on only one aspect, assuming that everything else was held constant. Initially this was acceptable and probably even necessary in developing a basic understanding of these facets. A second mode of research must now focus on the combined effect and the interactions among these issues. Here we address the integration of the first and third issues, demonstrating the distribution of data in a network after incorporating a specific concurrency control mechanism.

## 2.1. Data Placement Alternatives

Three approaches can be identified in data placement:

1. Centralized: The entire database is stored at one node. This approach minimizes storage costs; however reliability of the system is suspect. If there are several remote users, retrievals are expensive, both in terms of high communication costs as well as time delays. Updates are relatively cheap, since only one copy of each data item needs to be updated.

2. Replicated or Fully Redundant: A complete copy of each database is stored at every node. This method has high storage costs but high reliability. Retrieval costs are low, since all requests can be satisfied locally. The complexity of the update synchronization procedures will however increase the total cost.

3. Partitioned: In certain cases, due to high locality of reference, the database can be divided into non-overlapping segments that can be distributed across the various nodes. The reliability is more in this case than in the centralized case. Locality of reference lowers retrieval costs. Further, updates are cheaper, since multiple copies do not exist.

A mixture of methods (the last two) can lead to a hybrid system where certain databases are replicated while others are partitioned.

## 2.2. Concurrency Control Mechanisms (CCM)

One of the main objectives of a Database Management System (DBMS) is to enable multiple users to access the data concurrently [3]. This can be achieved without problems provided that the user is only retrieving data. However, if two or more users update the same data item at the same time, all but the last update may be lost, thus impairing the integrity of the database. In some cases, when one user is updating a particular piece of data, no other user is allowed to read that same piece of data – in order to avoid the wrong value being read. However, this may be a less significant problem compared to the previous case. The cost of reading a value that is only a few seconds old may be less than the waiting time imposed on a transaction. In a centralized database, consistency has to be maintained among various parts of one database. In a distributed database, the problem is magnified, because each copy of a database may need to reflect the same accurate information at the same point of time. As mentioned earlier, there is a tradeoff between this requirement and making the data available as soon as possible. In certain cases, users may be satisfied with values other than the most recent ones.

There are several methods available for concurrency control in distributed database systems. A careful study of these has revealed that they are composed of only a few subalgorithms. These are variations of two basic techniques: two-phase locking (2PL) and timestamp ordering (T/O). An exhaustive survey of all the methods is available in [18].

The model for file allocation that is described here takes into account the Central Locking Mechanism [27] based on 2PL. The CCM utilized has two disadvantages. First, most of the traffic is to or from one node, creating a potential bottleneck. Second, this method is vulnerable to loss of the central node. This can be obviated by designating a backup node to take over the functions of the central node in case of a crash. Our model allows the determination of the back up node. Further, under certain types of loads in the system, there is an advantage to be had by bundling messages to and from the central site. The mechanism is also simple and easy to implement.

## 3. The File Allocation Problem

One of the design issues is the allocation of the databases over the network in an optimal manner: the File Allocation Problem (FAP) [25]. The optimum can be computed in terms of either performance or operating costs. In order to minimize operating costs, it may be better to store fewer copies of a database. However, the penalty this may impose is that of longer response time. Several models have been proposed to solve the FAP starting with Chu's pioneering effort in 1969 [9]. Whitney [29] extended this work by considering jointly the allocation of files and network topology design. A detailed review of the various FAP models can be found in [10]. Most of the models are in the form of mathematical programming problems with a variety of constraints [1], [4], [6], [8], [11], [12], [13], [14], [16], [17], [19], [20], [21], [26] [28]. The objective function to be minimized is total cost, consisting of storage and operating costs. However, a major shortcoming in all the models is that they have ignored the consequences of incorporating a CCM. It is our contention that communication costs form a major part of the operating costs of a DDS and that the communication flow depends entirely on the CCM [23]. Hence specific CCM have to be incorporated into the FAP.

## 3.1. Formulating the Model

The DDS considered in our model consists of several nodes. At each node is located computer hardware (mainframe, minicomputer, intelligent terminal, etc.). The hardware need not be the same at each node, which can communicate at a certain cost per unit of data transmitted. Users have access to databases that can be stored at any of the nodes.

Transactions are of two types: read-only queries (retrievals) and updates. Each query may consist of a series of instructions to extract the data and present them in a suitable format to the person making the request. Similarly, each update could consist of a sequence of steps designed to extract the data values and write them back after updating them. Each query or update can be considered to be a program. For instance, in an airlines reservations system one program might answer the question: "How many seats are available for flight number "X" from "Y" to "Z" on a given date. Similarly, a program for a bank might calculate the balances for each account and then update the database. Thus there would be separate programs to handle each transaction type and these programs may be stored at different nodes. Read-only queries would read information from a single copy of a database via a particular copy of a program. Updates would write information into all copies of a database via any one copy of an update program. The model described in this paper does not consider the allocation of programs.

## 3.2. Communication Flows in the Network

For a read-only query the following steps may be executed when the Central Node Locking Mechanism is used (see Figure 1). The query is initiated at a site (site A), which may or may not contain a database. The originating site may be just a remote terminal.

In processing queries, a program at site A will first decompose any queries which need more than one value into single-item queries directed towards a single database. The resulting subqueries for only one item will each be directed toward a database. Site A will then request the central node for a lock on the item(s). This is just one of many different protocols that may be used. The central node maintains information about the locations of databases. The central node will grant a lock on the requested item(s) if they are not already locked. Assuming a lock is granted, the central node will send a message to one of the sites (site B) having the relevant database(s), instructing it to ship the item(s) to site A, which can now use them to generate a report, if necessary.

![](/api/attachments/E6M3HCYA/fulltext/images/5f817247f7590da5027860db6f53725221bc6737d1f3ba2ec4e8b703de318c6f.jpg)  
Fig. 1. Communication Flows Read-Only Queries (note: The sequence of messages is indicated by the number parentheses).

These steps are initiated in the case of a read-only query. In the case of an update originating at site A, there will be additional messages flowing in the network (see Figure 2). The flow will be identical till the point when site A receives the items from the relevant databases. Site A will then update each of these items and give the updated values to the user. Subsequently the updated values will be sent to the central node, which will transfer them to each copy of the relevant databases in the network. Site B (which supplied the data) will be one of the recipients of the updated value(s) from the central node. Finally in the case of both types of transactions, site A will request the central node to release the locks. This request is transmitted by site A immediately after sending the updated value to the central node. The central node will release the lock when it receives an acknowledgment from all the recipients of the updated values. Typically, acknowledgments are piggybacked onto other requests flowing from a node to the central node. Note that the order of messages (6) and (7) in Figure 2 can be interchanged without any loss of information.

![](/api/attachments/E6M3HCYA/fulltext/images/02652c29b94838c53d3a7efc9b9b333832733679dd9abbc2f94006555b3429b2.jpg)  
Fig. 2. Communication Flows Updates (note: The sequence of messages is indicated by the number in parentheses).

In order to allocate the various databases, it is necessary to consider the cost of all the information flows in the network. If we were using the primary copy or the majority consensus method [27] for concurrency control, the message flows would be different; it is this aspect of the FAP that has been ignored in past research. The model in this paper demonstrates the results of incorporating a central node locking mechanism into the FAP. The communication flows have been translated into mathematical terms, yielding the nonlinear integer programming model shown in Appendix 1. The model accepts a number of input parameters from the designer of a DDS (see Appendix 2).

## 3.3. Decision Variables

There are three decision variables:

1. $X_{kd}=1$ if a copy of database d is stored at node k; 0 otherwise.

2. $y_{m} = 1$ if $m$ is the central node; 0 otherwise.

3. $Y_{jmkd}=1$ if node k is instructed by the central node m to supply the processing node j with data item values out of database d; 0 otherwise. This means that node j always consults the same copy of database d (that at k) for all updates and queries originating at node j.

It should be noted that programs that process updates are different from those processing (readonly) queries. All programs are assumed to be allocated at the nodes where they are required. No decision variable corresponding to the allocation of programs is incorporated into the model.

## 3.4. Constraints in the Model

There are several constraints in the model; the most important of these is the capacity constraint. It is based on the fact that - in order to prevent a bottleneck at any node - each one is limited in the total number of queries and updates that it can process per unit time.

## 3.5. Solving the Model

The solution algorithm used is the ZOOM/XMP algorithm, as described in [22]. ZOOM/XMP is a computer code for solving zero/one mixed integer programming problems. ZOOM begins by solving the problem as a linear program, and then uses the Pivot and Complement heuristic to find an initial integer feasible solution. It then uses a branch and bound search to find improved solutions and to verify optimality. The B&B procedure uses linear programming to compute bounds. It also has several novel features, such as fixed-order branching, the select and expand strategy, the resource space tour, and cheating.

In order to convert the non-linear model to a linear version, it was assumed that all the nodes are homogeneous: the non-decision parameters for all nodes are identical. This implies that any node can be designated as the central node. Hence for purposes of analysis, node 1 was designated as the central node: variable $y_{1}$ was given a value of 1, while $y_{2}$ , $y_{3}$ etc. were given a value of 0. However, even if all nodes are not identical, the same algorithm can be used by trying each node in turn as the central node and choosing the one that yields the lowest total cost.

## 3.6. Analysis using the Model

The objective of the analysis was to determine a pattern, if any, in the allocation of databases for various query and update patterns. The impact of different amounts of total traffic in the network was also to be noted. Subsequently, the effects of changing the number of nodes in the network were to be studied.

The communication cost between any two nodes was assumed to be identical. This assumption is valid for certain types of packet switched networks that base their charges, not on the distance, but on the size of the message. This is due to the fact that a message is typically broken into several packets, and each packet may travel along a different route to reach the destination. However, in many networks, costs are based on the distance between the communicating nodes. This is especially true of networks that connect widely dispersed sites, as in the case of a world-wide organization. Hence the model does allow for communication costs based on the distance between nodes or some other metric. Further, the communication cost per packet for updates and queries was assumed to be the same (the model does allow for differing costs).

Table 2  
Values for Non-decision Parameters that were Fixed During the Analysis.

<table><tr><td>Variable</td><td>Value</td></tr><tr><td> $S_{kd}$ </td><td>$1.00</td></tr><tr><td> $C_{ij}$ </td><td>$0.01 per packet</td></tr><tr><td> $U_{ij}$ </td><td>$0.01 per packet</td></tr><tr><td> $f_{id}$ </td><td>0.33</td></tr><tr><td> $g_{id}$ </td><td>0.33</td></tr><tr><td> $n_i$ </td><td>50 packets</td></tr><tr><td> $m_i$ </td><td>50 packets</td></tr><tr><td> $\alpha, \alpha'$ </td><td>1.0</td></tr><tr><td> $\beta, \beta'$ </td><td>1.2</td></tr><tr><td> $\gamma$ </td><td>1.3</td></tr></table>

Next, nodes were assumed to have identical traffic. The number and size of queries and updates originating at each node were the same. The expansion factors $\alpha$ , $\beta$ , $\gamma$ , etc. were held constant throughout the analysis. The storage cost of each database at every node was also the same: $S_{kd}$ was always constant “S”. The unit of time was a day. The values for the non-decision parameters that were not varied during the analysis are shown in Table 1. All these would be specified by the designer of the database system. It is to be noted that the values of the parameters can be changed and the ones presented here are for purposes of illustration. Experimentation with different values has enabled us to specify general guidelines for the design of DDS.

Allocation of Databases (result from ZOOM/XMP) Three Nodes, Three Databases (Node 1 is Central Node).

<table><tr><td rowspan="2">No.</td><td rowspan="2"># of queries</td><td rowspan="2"># of updates</td><td rowspan="2">ratio of queries/updates</td><td colspan="3">Processing Capacity at nodes</td><td colspan="3">Allocation of databases at nodes</td></tr><tr><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td></tr><tr><td>1.</td><td>100</td><td>100</td><td>1</td><td>300</td><td>300</td><td>300</td><td>2,3</td><td>1</td><td>2</td></tr><tr><td>2.</td><td>100</td><td>100</td><td>1</td><td>200</td><td>300</td><td>300</td><td>1,2,3</td><td>2</td><td>1,3</td></tr><tr><td>3.</td><td>100</td><td>100</td><td>1</td><td>200</td><td>200</td><td>300</td><td>1,2,3</td><td>2</td><td>1,3</td></tr><tr><td>4.</td><td>100</td><td>100</td><td>1</td><td>200</td><td>300</td><td>300</td><td>1,2,3</td><td>1,2</td><td>1</td></tr><tr><td>5.</td><td>100</td><td>100</td><td>1</td><td>200</td><td>200</td><td>200</td><td>1,2,3</td><td>2,3</td><td>1,3</td></tr><tr><td>6.</td><td>100</td><td>100</td><td>1</td><td>0</td><td>350</td><td>350</td><td>-</td><td>1,2</td><td>1,3</td></tr><tr><td>7.</td><td>100</td><td>100</td><td>1</td><td>600</td><td>300</td><td>300</td><td>1,2,3</td><td>-</td><td>-</td></tr><tr><td>8.</td><td>100</td><td>0</td><td>100</td><td>600</td><td>300</td><td>300</td><td>1,2,3</td><td>1,2,3</td><td>1,2,3</td></tr><tr><td>9.</td><td>100</td><td>50</td><td>2</td><td>600</td><td>300</td><td>300</td><td>1,2,3</td><td>-</td><td>-</td></tr><tr><td>10.</td><td>630</td><td>50</td><td>12.6 *</td><td>3600</td><td>3600</td><td>3600</td><td>1,2,3</td><td>-</td><td>-</td></tr><tr><td>11.</td><td>631</td><td>50</td><td>12.62</td><td>3600</td><td>3600</td><td>3600</td><td>1,2,3</td><td>1,2,3</td><td>1,2,3</td></tr><tr><td>12.</td><td>1230</td><td>100</td><td>12.30 *</td><td>5000</td><td>5000</td><td>5000</td><td>1,2,3</td><td>-</td><td>-</td></tr><tr><td>13.</td><td>1231</td><td>100</td><td>12.31</td><td>5000</td><td>5000</td><td>5000</td><td>1,2,3</td><td>1,2,3</td><td>1,2,3</td></tr><tr><td>14.</td><td>2420</td><td>200</td><td>12.10</td><td>9000</td><td>9000</td><td>9000</td><td>1,2,3</td><td>-</td><td>-</td></tr><tr><td>15.</td><td>2430</td><td>200</td><td>12.15 *</td><td>9000</td><td>9000</td><td>9000</td><td>1,2,3</td><td>-</td><td>-</td></tr><tr><td>16.</td><td>2431</td><td>200</td><td>12.155</td><td>9000</td><td>9000</td><td>9000</td><td>1,2,3</td><td>1,2,3</td><td>1,2,3</td></tr><tr><td>17.</td><td>3610</td><td>300</td><td>12.03</td><td>12000</td><td>12000</td><td>12000</td><td>1,2,3</td><td>-</td><td>-</td></tr><tr><td>18.</td><td>3630</td><td>300</td><td>12.10 *</td><td>12000</td><td>12000</td><td>12000</td><td>1,2,3</td><td>-</td><td>-</td></tr><tr><td>19.</td><td>3631</td><td>300</td><td>12.103</td><td>12000</td><td>12000</td><td>12000</td><td>1,2,3</td><td>1,2,3</td><td>1,2,3</td></tr><tr><td>20.</td><td>4830</td><td>400</td><td>12.07 *</td><td>16500</td><td>16500</td><td>12500</td><td>1,2,3</td><td>-</td><td>-</td></tr><tr><td>21.</td><td>4831</td><td>400</td><td>12.07</td><td>16500</td><td>16500</td><td>16500</td><td>1,2,3</td><td>1,2,3</td><td>1,2,3</td></tr></table>

Notes: \* denotes Threshold Ratio. In all the situations where there is a redundant allocation of databases, each node has surplus capacity and all data items are obtained locally.

Table 3  
Allocation of Databases (result from ZOOM/XMP) Five Nodes, Three Databases (Node 1 is Central Node).

<table><tr><td rowspan="2">No.</td><td rowspan="2"># of queries</td><td rowspan="2"># of updates</td><td rowspan="2">ratio of queries/updates</td><td rowspan="2">Processing Capacity at each node</td><td colspan="5">Allocation of databases at nodes</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>1.</td><td>100</td><td>100</td><td>1</td><td>100</td><td>all</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>2.</td><td>50</td><td>50</td><td>1</td><td>1000</td><td>all</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>3.</td><td>700</td><td>50</td><td>14.0</td><td>4000</td><td>all</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>4.</td><td>1200</td><td>50</td><td>24.0</td><td>10,000</td><td>all</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>5.</td><td>1280</td><td>50</td><td>25.6 *</td><td>10,000</td><td>all</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>6.</td><td>1281</td><td>50</td><td>25.62</td><td>10,000</td><td>all</td><td>all</td><td>all</td><td>all</td><td>all</td></tr><tr><td>7.</td><td>2530</td><td>100</td><td>25.30 *</td><td>20,000</td><td>all</td><td></td><td>-</td><td>-</td><td>-</td></tr><tr><td>8.</td><td>2531</td><td>100</td><td>25.31</td><td>20,000</td><td>all</td><td>all</td><td>all</td><td>all</td><td>all</td></tr><tr><td>9.</td><td>5030</td><td>200</td><td>25.15 *</td><td>40,000</td><td>all</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>10.</td><td>5031</td><td>200</td><td>25.155</td><td>40,000</td><td>all</td><td>all</td><td>all</td><td>all</td><td>all</td></tr><tr><td>11.</td><td>7530</td><td>300</td><td>25.10 *</td><td>80,000</td><td>all</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>12.</td><td>7531</td><td>300</td><td>25.103</td><td>80,000</td><td>all</td><td>all</td><td>all</td><td>all</td><td>all</td></tr><tr><td>13.</td><td>10030</td><td>400</td><td>25.07 *</td><td>80,000</td><td>all</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>14.</td><td>10031</td><td>400</td><td>25.077</td><td>80,000</td><td>all</td><td>all</td><td>all</td><td>all</td><td>all</td></tr><tr><td>15.</td><td>12530</td><td>500</td><td>25.06 *</td><td>100,000</td><td>all</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>16.</td><td>12531</td><td>500</td><td>25.062</td><td>100,000</td><td>all</td><td>all</td><td>all</td><td>all</td><td>all</td></tr></table>

Notes: \* denotes Threshold Ratio; 'all' indicates databases 1, 2, and 3.

The analysis started with three nodes and three databases in the network. The number of programs is irrelevant, since we assumed it is fully redundant at each node, with a traffic of 100 queries and 100 updates. Thus there were a total of 600 transactions per day in the entire system initially. The capacity constraint was set at this to allow enough capacity at the central node to process all the queries and updates originating in the entire system. Under this condition, the algorithm showed that only one copy of each database was to be allocated. When the capacity of the central node was reduced there was a partially redundant allocation of databases. This can be seen in Table 2, where the allocation of databases is indicated for various capacities at each node. Increasing the number of queries and updates to 200 each at each node resulted in the same allocation of just one copy of each database, no matter how high the total traffic, as long as the number of queries and updates in the system was the same. Just one copy of each database got allocated, as long as the central node had enough capacity to process all the traffic.

The next logical step was to examine the impact of having more updates than queries. Again, the number of copies of each database remained at one as long as the number of updates was more than the number of queries. Next the situation was reversed to study the allocation of databases when the number of queries were more than the number of updates. In all these cases, each node had enough capacity to process all the queries and updates arising in the entire network. We started with 50 updates at each node and increased the number of queries from 50 to 100, 200, etc. Now a change in the allocation of databases was observed. Above a certain ratio of queries to updates, we found a fully replicated allocation of databases. Specifically, for 50 updates originating at each node when the ratio of queries to updates was more than 12.6, a copy of each database was allocated at each node. Below this value only one copy of each database got allocated in the entire network. Next, the number of updates in the system was doubled to 100 at each node. This time the ratio of queries to updates for a fully redundant allocation was slightly lower at 12.3. A partitioned allocation was found at a ratio below this value. On increasing the number of updates to 200, we found that the transition took place at a still lower ratio of queries to updates. The same pattern was observed for higher levels of updates. The reason for this could be that at higher levels of updates the total traffic in the system is much higher, hence there are more transactions making demands for data values. Hence it is necessary to allocate an extra copy of each database even though the disparity between the number of queries and updates is lower.

Allocation of Databases (result from ZOOM/XMP) Ten Nodes, Three Databases (Node 1 is Central Node).

<table><tr><td rowspan="2">No.</td><td rowspan="2"># of queries</td><td rowspan="2"># of updates</td><td rowspan="2">ratio of queries/updates</td><td rowspan="2">Processing Capacity at each node</td><td colspan="2">Allocation of databases at</td></tr><tr><td>node 1</td><td>all other nodes</td></tr><tr><td>1.</td><td>5780</td><td>100</td><td>57.8 *</td><td>80,000</td><td>1,2,3</td><td>-</td></tr><tr><td>2.</td><td>5781</td><td>100</td><td>57.81</td><td>80,000</td><td>1,2,3</td><td>1,2,3</td></tr><tr><td>3.</td><td>11530</td><td>200</td><td>57.65 *</td><td>300,000</td><td>1,2,3</td><td>-</td></tr><tr><td>4.</td><td>11531</td><td>200</td><td>57.655</td><td>300,000</td><td>1,2,3</td><td>1,2,3</td></tr><tr><td>5.</td><td>17280</td><td>300</td><td>57.60 *</td><td>300,000</td><td>1,2,3</td><td>-</td></tr><tr><td>6.</td><td>17281</td><td>300</td><td>57.603</td><td>300,000</td><td>1,2,3</td><td>1,2,3</td></tr><tr><td>7.</td><td>23030</td><td>400</td><td>57.57 *</td><td>400,000</td><td>1,2,3</td><td>-</td></tr><tr><td>8.</td><td>23031</td><td>400</td><td>57.57</td><td>400,000</td><td>1,2,3</td><td>1,2,3</td></tr><tr><td>9.</td><td>28780</td><td>500</td><td>57.56 *</td><td>400,000</td><td>1,2,3</td><td>-</td></tr><tr><td>10.</td><td>28781</td><td>500</td><td>57.56</td><td>400,000</td><td>1,2,3</td><td>1,2,3</td></tr></table>

Note: \* denotes Threshold Ratio.

At this point we introduce the term Threshold Ratio (TR): the highest value of the ratio of queries to updates, at which only one copy of a database is allocated in the system for a given level of updates.

The TR is different for different levels of updates. Further, as the level of updates in the system increases, the TR decreases. Thus there is an inverse relationship between the number of updates in the system and the threshold ratio. A similar analysis was carried out by increasing the total number of nodes in the network to 5, while the total number of databases remained at 3. It was noticed that when there were 50 updates at each node, the TR had a value of 25.6 which is much higher than for three nodes. On increasing the number of updates to 100, the TR decreased to 25.3. Table 3 indicates the trend in the value of the TR for various levels of updates. Similar results were obtained when the total number of nodes was increased to 10, while the number of databases remained at three; see Table 4.

Thus the TR varies directly with the total number of nodes in the network; as the total number of nodes in the network increases, so does the total traffic. This is due to the fact that each node has the same amount of originating traffic. Hence, in order to justify an extra copy of a database, a larger number of queries are required. An interesting observation is that after a certain level of updates is reached in the system, the value of the TR starts leveling out. The difference between the TR values for a level of updates of 400 is 25.07, while that for a level of updates of 500 is 25.06 (see Table 3). Figure 3 shows the trend of the TR values for a network consisting of five nodes with three databases to be allocated. The TR represents a frontier for moving from a partitioned allocation to a redundant allocation or vice versa. Similar graphs can be plotted for various number of nodes and databases in a network.

![](/api/attachments/E6M3HCYA/fulltext/images/7a043e0932f7155a9399c81f45456dedcb12937fcfb2357d03d6ed72a7a673ac.jpg)  
TOTAL QUERIES AND UPDATES IN THE SYSTEM  
Fig. 3. Threshold Ratios for Database Allocation (five nodes, three databases).

Whenever the ratio of queries to updates is below the TR, the processing capacity of the central node determines whether there is a partitioned or a hybrid allocation of databases. A hybrid allocation is obtained only if the central node does not have enough capacity to process all requests for data and the ratio of queries to updates is below the TR. This pattern is illustrated by the first six entries of Table 2. In each of these cases, the central node does not have sufficient processing capacity and the ratio of queries to updates is below the TR. Hence, there is a hybrid allocation; some databases are duplicated, while others are not. Entry 7 shows that there is a partitioned allocation of databases, once the central node is given enough capacity to process all data requests and the ratio of queries to updates is below the TR.

In all cases, the nodes were homogeneous. Hence it did not matter which was chosen as the central node. However in case all nodes are not identical, the algorithm can be used iteratively to select the central node: the one that yields the lowest overall cost can be designated as the central node. The backup node can be the one that yields the second lowest overall cost. As expected, the total cost of the system is lowest whenever a partitioned allocation of databases is obtained. However, this is at the expense of increased response time and vulnerability to failures. The cost of a redundant allocation is much greater; however, the response time in each case is expected to be better, since all requests are handled locally. The total cost of the system is between these two values, in the case of a hybrid allocation. The response time is not expected to be as good as that of a fully redundant system, but better than a partitioned system.

It is therefore clear that the allocation of a database at a particular node depends on:

1. The ratio of queries to updates at that node.

2. The total traffic for that database arising at all other nodes.

3. The capacity of the node under consideration.

## 4. Practical Implications

1. For an application with much more update traffic than query traffic, one copy of each database seems to be the best option when the central node locking mechanism is used for concurrency control. Further, in such a case the best option is to store the databases at the central node. The choice of the central node is crucial, since this node would not only act as a controller for maintaining lock information, but would also manage the data in the network.

2. For networks that have equal query and update traffic, (number and size) the best option is to store a copy of each database at the central node.

3. We find that the transition from single to multiple copies of a database takes place within a very narrow range of traffic. This occurs only if the query traffic is greater than the update traffic. The same holds true whatever the storage or communication cost per packet. Hence the FAP is considerably simplified for practical applications. The designer of a DDS can determine the frontiers for a specific range of parameters of the system and decide on either a partitioned or fully replicated allocation, depending on the range of traffic.

4. For a system with fairly heavy traffic, any increase in total traffic maintaining the query/update ratio constant will not cause a major change in database allocation. Hence the designer does not have to expend extra resources in reorganizing the entire system. This is because the threshold ratios level out after a certain level of traffic is reached.

5. A major reorganization in the system would be advisable in certain situations. If the ratio of queries to updates were to change drastically while the total traffic remained the same, then the best allocation would change from a fully redundant to a partitioned one or vice versa. Similarly, if the level of traffic in the system increased drastically from very low to very high while maintaining the same ratio of queries to updates, the system would require reorganization. Lowering of communication costs might also be a cause for reorganization of the system. Thus it is essential for the designer to project future levels of traffic and query/update ratio. This would help make an evaluation of the degree of reorganization needed and planning for it. For instance, if a very rapid growth in traffic is predicted but the ratio of queries to updates is expected to remain fairly constant, then the designer would know that a change from a partitioned allocation to a fully redundant allocation will be imperative in the near future. In such a situation, the designer would need to calculate that total cost of the reorganization and compare it with the cost of starting with a fully redundant allocation. If it turns out that the cost of reorganization is more than the cost of maintaining a non-optimal allocation for a short period of time, the user can go ahead with the decision to have a fully redundant allocation from the outset.

## 5. Conclusions

This paper addressed the task of looking at the FAP from a new perspective and demonstrated the implications of incorporating CCM into the FAP. There is still considerable potential for research. Some of the enhancements were described here.

Here only one concurrency control mechanism has been incorporated into the FAP; a set of models is being formulated to include other CCM. We are also developing special heuristics to solve larger models. Our intention is to build a decision support system containing a set of models that will facilitate File Allocation; this will help in setting parameters and in carrying out a sensitivity analysis on them.

## Appendix 1

Objective function

Minimize:

Storage cost of databases +

Communication cost for read-only queries + Communication cost for updates (See Appendix 2 for explanation of notation)

Storage cost of databases

$$
\sum_ {k} \sum_ {d} S _ {k d} * X _ {k d}.
$$

Communication cost for read-only queries

1. Request for lock

$$
\sum_ {m} \sum_ {i} C _ {i m} * n _ {i} * f _ {i d} * \lambda_ {i} * y _ {m}.
$$

2. Same as 1 (granting of lock)

3. Request for data item from site B

$$
\sum_ {i} \sum_ {d} \sum_ {k} \sum_ {m} C _ {m k} * n _ {i} * f _ {i d} * \alpha * \lambda_ {i} * y _ {m} * Y _ {i m k d}.
$$

4. Data item sent from site B to site A $\sum_{i}\sum_{d}\sum_{k}\sum_{m}C_{ki}*n_{i}*f_{id}*\beta*\lambda_{i}*y_{m}*Y_{imkd}.$

5. Same as 1 (Release of lock).

Communication cost for updates

1. Request for lock

$$
\sum_ {i} \sum_ {m} U _ {i m} * m _ {i} * g _ {i d} * \lambda_ {i} * y _ {m}.
$$

2. Same as 1 (granting of lock)

3. Request for data item from site B

$$
\sum_ {i} \sum_ {d} \sum_ {k} \sum_ {m} U _ {m k} * m _ {i} * g _ {i d} * \alpha^ {\prime} * \lambda_ {i} ^ {\prime} * y _ {m} * Y _ {i m k d}.
$$

4. Data item value sent from site B to site A $\sum_{i}\sum_{d}\sum_{k}\sum_{m}U_{ki}*m_{i}*g_{id}*\beta^{\prime}*\lambda_{i}^{\prime}*y_{m}*Y_{imkd}.$

5. Updated value sent from site A to central node

$$
\sum_ {d} \sum_ {i} \sum_ {m} U _ {i m} * m _ {i} * g _ {i d} * \gamma * \lambda_ {i} ^ {\prime} * y _ {m}.
$$

6. Updated value from central node to all relevant sites

$$
\sum_ {i} \sum_ {d} \sum_ {m} \sum_ {l} U _ {m l} * m _ {i} * g _ {i d} * \gamma * \lambda_ {i} ^ {\prime} * y _ {m} * X _ {l d}.
$$

7. Same as 1 (release of lock).

Constraints

1. Single central node

$$
\sum_ {m} y _ {m} = 1.
$$

2. At least one copy of each database $\sum_{k} X_{kd} \geq 1$ .

3. Site B should send data item value to site A only if relevant database is allocated at B

$$
X _ {k d} \geq Y _ {i m k d}.
$$

4. Only one node needs to furnish the desired data item value

$$
\sum_ {k} Y _ {i m k d} = 1.
$$

5. Processing capacity constraint

$$
\sum_ {i} \sum_ {d} n _ {i} * f _ {i d} * Y _ {i m k d} + \sum_ {i} \sum_ {d} m _ {i} * g _ {i d} * Y _ {i m k d} \leq C P _ {i}.
$$

$CP_{i}$ is the total capacity of node i. It is the maximum number of requests for data item values that node i can satisfy per unit time.

6. Binary constraints

$$
\begin{array}{l l l} \text {(a)} X _ {k d} = 0 & \text {or} & 1, \\ \text {(b)} y _ {m} = 0 & \text {or} & 1, \\ \text {(c)} Y _ {i m k d} = 0 & \text {or} & 1. \end{array}
$$

## Appendix 2

## Input parameters

1. $S_{kd} =$ Storage cost of database $d$ at node $k$

2. $C_{ij}$ ( $U_{ij}$ ) = Communication cost per unit for read-only queries (updates) from node i to node j

3. $n_i$ ( $m_i$ ) = number of read-only queries (updates) originating at node $i$ per unit time

4. $f_{id}(g_{id}) = \text{fraction of total number of read-only queries (updates) originating at node } i \text{ requiring data item values from database } d.$

5. $\lambda_{i}(\lambda_{i}^{\prime}) =$ average size of read-only queries (updates) originating at node $i$ (in number of packets)

6. $\alpha, \beta, \gamma (\alpha', \beta', \gamma') =$ expansion factors for size of queries (updates).

## References

[1] J. Akoka and P.P.S. Chen, "Optimal Design of Distributed Information Systems", IEEE Transactions on Computers, Vol C-29, No. 12, Dec 1980, pp. 1068-1090.

[2] G.G. Belford, "Distributed Database Techniques: An Assessment", in Current Directions in Database Management development, Auerbach Publishers Inc., 1984, pp. 1–12.

[3] P.A. Bernstein and N. Goodman, "Concurrency Control in Distributed Database Systems", ACM Computing Surveys, Vol 13, No. 2, June 1981, pp. 185-221.

[4] G. Casey, "Allocation of Copies of a File in an Information Network", Proceedings AFIPS, 1972 Spring Joint Conference, Vol. 40, 1972, pp. 617-625.

[5] S. Ceri, B. Pernici and G. Wiederhold, "An Overview of Research in the Design of Distributed Databases", Database Engineering, 1984, pp. 46–51.

[6] S. Ceri, G. Martella and G. Pelagatti, "Optimal File Allocation in a Computer Network: A Solution Method Based on the Knapsack Problem", Computer Networks, Vol. 6, 1982, pp. 345-357.

[7] S. Ceri and G. Pelagatti, "Distributed Databases: Principles and Systems", McGraw-Hill Publishing Co., New York, 1984.

[8] M. Chandy, “Models of Distributed Systems”, Proceedings of the Third International Conference on Very Large Databases, 1977, pp. 105–120.

[9] W.W. Chu, "Multiple File Allocation in a Multiple Computer System", IEEE Transactions on Computers, Vol. C-18, No. 10, Oct. 1969, pp. 885–889.

[10] LW. Dowdy and D.V. Foster, "Comparative Models of the File Assignment Problem". ACM Computing Surveys, 1982, Vol. 14, No. 2, June 1982, pp. 287-313.

[11] J. Elam and M. Fisher, "The use of Mathematical Models in Distributed Database Design", Distributed Databases II, Infotech State-of-the-Art report, 1979, pp. 115-125.

[12] K.P. Eswaran, "Placement of records in a file and file allocation in a computer network", Information Processing 74, 1974, pp. 304–307.

[13] M.L. Fisher and D.S. Hochbaum, "Database location in Computer Networks", Journal of ACM, Vol 27, No. 4, Oct 1980, pp. 718–735.

[14] B. Gavish and H. Pirkul, "Computer and Database Location in Distributed Computer Systems", IEEE Transactions on Computers, Vol. C-35, No. 7, July 1986,

[15] N. Goodman and J.B. Rothnie, "A Survey of Research and Development in Distributed Database Management", Proceedings of the Third International Conference on Very Large Databases, 1977, pp. 10–27.

[16] K.B. Irani and N.G. Khabbaz, "A Methodology for the design of Communication networks and distribution of data in Distributed Supercomputer Systems", IEEE Transactions on Computers, Vol. C-31, No. 5, May 1982.

[17] H.K. Jain, "A Comprehensive Model for the Design of Distributed Computer Systems". IEEE Transactions on Software Engineering, Oct. 1987, Vol SF-13, No. 10, pp. 1092–1104.

[18] W.H. Kohler, "Overview of Synchronization and Recovery Problems in Distributed Databases", Proceedings COMPCON80, Fall 1980, pp. 433-441.

[19] L.J. Laning and M.S. Leonard, "File Allocation in a Distributed Computer Communication Network", IEEE Transactions on Computers, Vol. C-32, No. 3, Mat. 1983, pp. 232–244.

[20] K.D. Levin and H.L. Morgan, "Optimal Program and Data Location in Computer Networks", Communications of ACM, Vol. 20, No. 5, May 1977, pp. 315-322.

[21] S. Mahmoud and J.S. Riordon, "Optimal Allocation of Resources in Distributed Information Networks", ACM Transactions on Database Systems, Vol. 1, No. 1, March 1976, pp. 66–78.

[22] R. Marsten, "User's manual for ZOOM/XMP", Department of MIS, University of Arizona, Tucson, AZ 85721.

[23] S. Ram, "A Model for the design of distributed databases", Unpublished PhD Dissertation, University of Illinois at Urbana Champaign, Department of MIS, Sept. 1985.

[24] S. Ram and C. Chastain, "Distributed Database Management Systems: An Architectural Survey", forthcoming, Journal of Systems and Software, 1989.

[25] C.V. Ramamoorthy and B.W. Wah, "Data management in Distributed databases", Proceedings AFIPS, 1979, pp. 667-680.

[26] C.V. Ramamoorthy and B.W. Wah, "The Isomorphism of Simple File Allocation", IEEE Transactions on Computers, Vol. C-32, No. 3, Mar 1983, pp. 221–232.

[27] J.D. Ullman, "Principles of Database Systems", Computer Science Press, Rockville, Md., 1982.

[28] B.W. Wah, "File Placement on Distributed Computer Systems", IEEE Computer, Jan 1984, pp. 23-32.

[29] V.K.M. Whitney, "A Study of Optimal File Assignment and Communication Network Configuration in Remote Access Computer Message Processing and Communication Systems", Unpublished PhD dissertation, University of Michigan, Department of Electrical Engineering, Sept. 1970.
