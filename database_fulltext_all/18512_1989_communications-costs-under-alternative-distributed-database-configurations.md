---
otero_id: 18512
otero_key: "YERHCMUC"
title: "Communications costs under alternative distributed database configurations"
authors: "Max E. Jerrell; James N. Morgan"
year: "1989"
journal: "Information & Management"
doi: "10.1016/0378-7206(89)90024-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Communications Costs under Alternative Distributed Database Configurations

Max E. Jerrell and James N. Morgan
Northern Arizona University, College of Business Administration,
Box 15066, Flagstaff, AZ 86011, USA

Distributed database management systems (DDBMSs) can be configured in a variety of ways. Full or partial replication of data may be utilized, and even within systems not allowing replication a variety of directory configurations might be used, including fully replicated, centrally replicated and distributed directory systems. Alternative DDBMS configurations may lead to very different communications costs in a distributed network, and changes in database usage patterns are likely to affect different configurations in different ways. This paper models the communications costs associated with several alternative DDBMS configurations and examines the impact of changing database usage patterns on those costs. Changes in usage are found to have a substantial impact on relative communications costs of the alternative configurations.

Keywords: Distributed database management systems, Distributed processing, Database management, Communications cost.

![](/api/attachments/YERHCMUC/fulltext/images/d7458f9dd043c1610eb019a118b7dbd7c23f6d8f3be2e6fc8220e87e33075af1.jpg)

Max Jerrell is an Associate Professor of Economics and Statistics at Northern Arizona University. He holds a Ph.D. in Economics from Arizona State University. He has published articles in economics, statistics, numerical methods, and physics. He is currently a member of economic forecasting panels which forecast economic activity for the state of Arizona, the Southwest, and the metropolitan Phoenix area. He holds the rank of Major in the U.S. Air Force Reserve.

## 1. Introduction

This paper contains an examination and comparison of communication costs under alternative types of data distribution. Distributed systems with limited data distribution and management capabilities are already in widespread use $[2,3,4,10,13,14]$ ; prototype distributed database management systems (DDBMSs) supporting full access to all system data without the user knowing its storage location have been developed and tested $[6,16,18]$ ; and commercial database products with varying degrees of DDBMS capabilities are becoming available $[8,12,19]$ . In the literature addressing DDBMSs, little attention has been devoted to measurement and comparison of the volumes of data communications required to support alternative DDBMS configurations. Reduction in data communications cost is seen as an important factor motivating the move to distributed systems $[4,17,20]$ , but few attempts have been made to model communications costs under DDBMS configurations.

Several alternative DDBMS configurations have been proposed. Some involve fully partitioning the system database, while others allow full or partial replication of data. Aschim [1] developed an early taxonomy of possible distribution schemes for distributed networks not allowing replication. Schemes for configuring DDBMSs allowing replication have been proposed by various researchers, and are summarized in [15]. Fully partitioned systems can use a variety of directory systems. The full system directory can be copied at each node (replicated directory), a central node can contain the full system directory with each noncentral node containing a directory only for the fragment of the database held locally (central directory), or there may be no system directory (a distributed directory) so that the system is either searched node by node or a request is broadcast to all nodes to find remotely held data. The distribution methods are not mutually exclusive. Systems allowing partial replication use the directory systems described above to locate nonreplicated or nonfully replicated data, and it is at least conceptually possible to provide a DDBMS which supports all of the types of directory described above plus full or partial replication. Communication and other processing costs may vary markedly under these alternative distribution methods; thus exploration of cost tradeoffs under alternative distribution methods is appropriate.

![](/api/attachments/YERHCMUC/fulltext/images/2b1f97bdc55216f125cda79ab4a3e56f6fa4ca3e0823087410265be78828fb21.jpg)

Aspects of this problem have been explored in the literature. It has been known since the early 1970's that replication of data imposes lower communications costs when transactions are predominantly queries, than when many transactions are modifications requiring posting to all copies. In addition, a number of studies have addressed the "file allocation" problem. These studies have derived equations designed to determine the optimal allocation of data within a system allowing data to be distributed. Most have treated the case in which replication of data is allowed, but not required. However, virtually all of these studies have either assumed a specific type of directory system, or specified directory update costs in a very abstract form consistent with a variety of directory systems [7,9,21]. Such models treat the optimal allocation of data between replicated and nonreplicated configurations, but do not provide a systematic evaluation of all reasonable DDBMS configurations.

An early paper by Chu [5], compared costs of alternative file directory systems under various patterns of transactions. Directory systems corresponding to the central directory, fully replicated directory, and distributed directory were used.

![](/api/attachments/YERHCMUC/fulltext/images/bc7f4eb8ef46a9b7d7fcb454bc945c33d2e4035f2b67f774318818c81a0182ef.jpg)  
Fig. 1. Six Alternative DDBMS Configurations.

Cost comparisons were made varying the query rate and the ratio of update to query transactions. Chu found that the replicated directory tended to provide the lowest operating costs when the ratio of updates to query transactions was very low, that the distributed directory system was most advantageous when the update rate was high relative to the query rate, and that the central directory tended to have lower costs than the other two over most of the range of values he used in simulating performance. An important limitation of Chu's work is that he assumed updates could be initiated only by the node containing the file to be updated.

This paper provides a model of the communication costs associated with alternative DDBMS configurations and presents comparisons of the costs associated with these alternative configurations under various patterns of data usage. The model is oriented toward the choice of the type of DDBMS configuration to be used for a particular database. The question of data allocation is not addressed - the storage location for each data element under a given DDBMS configuration is assumed to be predetermined based upon expected access patterns. However, it is recognized that usage patterns may vary considerably across the data entities of a database. Given estimates of the usage pattern of a data entity, the model presented here could be used to determine the appropriate DDBMS configuration for that entity. Systematic application of this procedure to all entities of a database could be used to determine the optimal allocation of data among DDBMS configurations in systems supporting multiple configurations, and to suggest the types of DDBMS configurations which need to be available to provide efficient processing of a given database.

Six alternative systems are evaluated here. These configurations are depicted for the case of a three node system in Figure 1. In Figure 1 DB represents the data of a database, DIR represents a database directory, the subscript s indicates that the full system database or directory is present at the specified location, and the subscript x designates the central node of a system. The first alternative treated uses a central computer containing the full database and its directory with no database or directory fragments distributed (CDD). Three alternative fully partitioned systems are presented. The first places a full directory copy at each node and is referred to as a fully replicated directory (FRD) system; the second, the centrally replicated directory (CRD) system, places a full directory copy at a central node and local directories at the local nodes; and finally, the distributed directory (DD) system places only a local directory at each node. Under each of these systems it is assumed that nonredundant fragments of the database are stored at each of the nodes of the systems and that each node has a directory of its locally stored database fragment. Two systems allowing data replication are also included; a fully replicated system (FR) in which each node has a full copy of the database and its directory, and a centrally replicated (CR) system in which a central node has a complete copy of the database and directory, while other nodes contain database fragments and local directories with no data fragment stored at more than one noncentral node.

## 2. A Model of Communications Costs under Alternative DDBMS Configurations

A number of assumptions have been made in order to simplify the analysis and focus it on the choice of the type of data distribution methodology to be used. It is assumed that:

— In systems which allow distribution of data base fragments, the home node of each data element is predetermined and is invariant across all such systems.

— Each pair of nodes is connected by a communication link (thus star or ring communication patterns can be supported).

— Communications charges are proportional to usage; and the unit communication cost between a pair of nodes is a positive function of distance and is independent of the direction of transmission.

— Costs associated with failure and recovery and costs associated with transactions not successfully completed (such as attempts to add existing data, delete, modify or query nonexisting data) are not treated.

The system consists of N nodes where N is a positive integer. Where ring communications linkages are used, nodes are so situated that minimum communication costs can be achieved by a search procedure traversing the ring from node i to node $i+1$ and so on with node N connecting to node 1. Communication costs are measured per unit of message length between a pair of system nodes. For instance, $C_{ij}$ represents the cost of transmitting a message of unit length between nodes i and j.

Four types of transactions are treated here, queries $(Q)$ , adds $(U^{a})$ , modifications $(U^{m})$ , and deletes $(U^{d})$ . The three types of updates are treated separately because updates which add or delete an item listed in a nonlocal directory require that the nonlocal directory be updated, while modifications do not. For the purposes of this analysis additions or deletions of items which would not appear in nonlocal directories are treated as modifications. For example, assuming that orders are not assigned a unique order number which is used for retrieval, orders placed by a given customer might be found in a network database by first finding the appropriate customer number and then walking a chain of order records to find a given order. A similar relational database would have an order table with customer number appearing as a foreign key, and multiple occurrences of a given customer number occurring in the table. In either case the addition of a new order would not require the update of nonlocal directories and thus, for our purposes, would be treated as a modification transaction.

Query and update transactions rates per unit of time are measured. Thus $U^{m}$ represents the total number of modification transactions occur over a unit of time. Query and update transactions may be identified by their node of origin. For instance, $U_{i}^{a}$ refers to all add transactions originating at node i. Where a second subscript is used to identify transactions, it refers to the home node of the transaction data entity. Thus $Q_{ij}$ refers to all queries originating at node i on data whose home node is j.

Four basic message types of potentially varying lengths are assumed to be transmitted among nodes. Queries on nonlocal data require that a search message $(M^{s})$ be sent to the appropriate node to find the desired data. Once the appropriate data has been found, it must be retrieved $(M^{r})$ to the node which originated the request. These messages are treated as separate components because, in some systems, $M^{s}$ may be sent to more than one node in order to find the appropriate data. Update transactions on remotely held data will usually require an initial query (search and retrieval) to verify that the proposed update is appropriate. After it has been determined that an update is appropriate, a set of messages $M^{u}$ is required to update the database. This set of messages consists of transmission of the new or updated unit of data to the node where it is to be stored, and transmission of a return verification message to the node originating the update. A fourth type of internodal message is the set of transmissions required to update a nonlocal data directory $M^{du}$ . Here a message is transmitted from the node containing the data to the node containing the nonlocal data directory and a confirming message is returned from that node.

Some queries will be compound; that is, a single query may request retrieval of several data entities which meet a given criteria. In this case a single $M^{s}$ may be associated with several $M^{r}$ . The unit of measurement for queries is a single data entity retrieved. To adjust for compound queries a parameter $\beta$ is specified; this represents the average proportion of a search message required for each data entity retrieved across all queries. The parameter is expected to fall in the unit interval.

Central Database/Directory. By a central database/directory system, CDD, we mean a system where a central computer contains a complete copy of the system database and its directory. The noncentral nodes are assumed to process data to produce reports as needed, but they do not have any portion of the system database or directory.

The communications costs of such a system, $CDD^{c}$ , are presented in the equation below. For query transactions originating at any noncentral node i, a search

$$
\begin{array}{r}CDD^{c} = \sum_{\substack{i = 1\\ i\neq x}}^{N}C_{ix}\bigl [Q_{i}\bigl (\beta M^{s} + M^{r}\bigr) \\ +U_{i}\bigl (M^{s} + M^{r} + M^{u}\bigr)\bigr ] \end{array}
$$

message, $\beta M^{s}$ , must be sent to the central node $(x)$ . The appropriate data is then retrieved and sent from the central node back to node i, in a message $M^{r}$ . All updates originating at a non-central node $(U_{i}$ where $i \neq x)$ require a search message to the central node $(M^{s})$ , retrieval of the existing data to the originating node $(M^{r})$ , and finally, a set of update messages $(M^{\mu})$ . All internodal communications under this sytem occur between node i and the central node x. Thus communications cost per unit message length is always $C_{ix}$ .

Fully Replicated Directory. A fully replicated directory system is one in which the database is fully partitioned, but a directory for all data in the system is retained at every node. This directory indicates which remote node contains each nonlocally held data entity.

The following equation presents the communication costs associated with a fully replicated directory system, $FRD^{c}$ . The first term of this equation specifies

$$
\begin{array}{l}F R D^{c} = \sum_{i = 1}^{N}\sum_{\substack{j = 1\\ j\neq i}}^{N}\left\{C_{ij}\Big[C_{ij}\big(\beta M^{s} + M^{r}\big) \right.\\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad +\left(U_{ij}^{m} + U_{ij}^{d}\right)\\ \qquad \qquad \times (M^{s} + M^{r} + M^{u})\\ \qquad +U_{ij}^{a}M^{u}\Big]\\ \qquad \qquad +\sum_{\substack{k = 1\\ k\neq j}}^{N}\left(U_{ij}^{a} + U_{ij}^{d}\right)M^{du}C_{jk}\Bigg\} \\ \qquad +\sum_{i = 1}^{N}\sum_{\substack{j = 1\\ j\neq i}}^{N}\left(U_{ii}^{a} + U_{ii}^{d}\right)M^{du}C_{ij}\\ \end{array}
$$

communications costs associated with queries and updates on data stored at some remote node. Once the local directory at i has been searched to determine that the requested data is not held at i, the directory copy at i is searched to determine the location of the data, node j. For queries, the standard search and retrieval messages are then exchanged between nodes i and j. For all updates except adds, the search, retrieval and update messages are required. Valid add transactions require only an update message, because the search of the directory copy at i indicates that the identified unit of data does not currently exist in the system. Adds and deletes require that the system directory copies at each node be updated as well; this is accomplished by the last component of the first term. Adds and deletes to locally held data, $U_{ii}^{a}$ and $U_{ii}^{d}$ , still require that the system directory copies at the other nodes be updated. These costs are specified by the second term of the equation.

Centrally Replicated Directory. The centrally replicated directory system, $CRD^{c}$ , places a full copy of the system database directory at a central node. The database itself is fully partitioned. Each node contains a unique database fragment and a directory for that local fragment. All transactions on nonlocal data are routed through the central node which finds the node containing the desired data. It is assumed that once this node has been located direct communications can be established between it and the originating node.

The communications costs of a centrally replicated directory system are presented below. All queries on data not stored at the local node are routed to the central node (x). If the central node is neither the originating nor

$$
\begin{array}{l}C R D^{c} = \sum_{\substack{i = 1\\ i\neq x}}^{N}\sum_{\substack{j = 1\\ j\neq i\\ j\neq x}}^{N}Q_{ij}\Big[(C_{ix} + C_{xj})\beta M^{s} + C_{ij}M^{r}\Big]\\ \\ \quad +\sum_{\substack{i = 1\\ i\neq x}}^{N}C_{ix}(Q_{ix} + Q_{xi})(\beta M^{s} + M^{r})\\ \\ \quad +\sum_{\substack{i = 1\\ 1\neq x}}^{N}\sum_{\substack{j = 1\\ j\neq i\\ j\neq x}}^{N}\Big(\big(U_{ij}^{m} + U_{ij}^{d}\big)\\ \\ \quad \times \Big[\big(C_{ix} + C_{xj}\big)M^{s}\\ \quad +C_{ij}(M^{r} + M^{u})\Big]\\ \\ \quad +U_{ij}^{a}\big(2C_{ix}M^{s} + C_{ij}M^{u}\big)\\ \quad +C_{jx}\big(U_{ij}^{a} + U_{ij}^{d}\big)M^{du}\Big\} \\ \\ \quad +\sum_{\substack{i = 1\\ i\neq x}}^{N}C_{ix}\Big[(U_{ix} + U_{xi})(M^{s} + M^{r} + M^{u})\\ \\ \quad +\big(U_{ii}^{a} + U_{ii}^{d}\big)M^{du}\Big]\end{array}
$$

the destination node of a query, an indirect find operation is performed. A search message is first sent to the central node, which determines the location of the requested data and forwards the message to the appropriate node; the node containing the requested data then transmits the data directly to the originating node. The second term of the equation treats remote queries which involve the central node as the originating or destination node. For these queries, an indirect search message is not required.

The message patterns required to support updates tend to parallel those for queries. Remote modifies and deletes where the central node is neither the originating or destination node require an indirect find operation followed by retrieval and update messages. Forwarding a search message is not required for adds if the add is valid since there is no data to be retrieved. Adds and deletes which do not involve the central node as the originating or destination node also require that the directory at the central node be updated. The communications costs of these operations are indicated in the third term of the equation. Updates involving the central node as originating or destination node do not require the indirect find operation. In addition, it is assumed that the updating of the central directory can be accomplished for these transactions as a part of the database update process without additional transmission. Communications costs for these transactions are represented by the fourth term. The final term of the equation indicates that local adds or deletes at a noncentral node require that the directory copy at the central node be updated as well.

Distributed Directory. The distributed directory system, $DD^{c}$ , is one in which fragments of the system database are distributed to a set of nodes, none of which takes on any central functions. Each node contains only a local directory. The only information a node has about remotely held data is an indication that data of a given type does exist at other nodes, and an indication of which node is to be searched first in seeking remotely held data. If the desired data is not found at the first remote node, the request is sent to the next node etc. Thus find and fetch requests are assumed to traverse the ring of nodes until the requested data has been found or all nodes have been searched. Once data has been found at some node j to satisfy a request generated at node i, it is assumed that the two nodes communicate directly with each other, rather than following a ring communications pattern.

For the purposes of this paper, it will be assumed that communications are always routed to the next numbered node when traversing the ring. Thus node 1 would first route find and fetch operations to node 2, etc. Node N is assumed to route its find and fetch operations to node 1 completing the ring.

Communications costs for the distributed directory system are indicated in the following equation. All queries on remotely held data, $Q_{ij}$ , require a ring search

$$
\begin{array}{l} DD^{c} = \sum_{i = 1}^{N}\sum_{\substack{j = 1\\ j\neq i}}^{N}\Big\{Q_{ij}\big(\beta \Gamma_{ij} + C_{ij}M^{r}\big) + \big(U_{ij}^{d} + U_{ij}^{m}\big)\\ \\ \times \Big[\Gamma_{ij} + (M^{r} + M^{u})C_{ij}\Big]\\ \\ +U_{ij}^{a}\big(\tau_{i} + M^{u}C_{ij}\big)\Big\} \end{array}
$$

$$
+ \sum_ {i = 1} ^ {N} U _ {i i} ^ {a} \tau_ {i}, \quad \text { where }
$$

$$
\Gamma_ {i j} = \left\{ \begin{array}{l l} \sum_ {k = i + 1} ^ {j} M ^ {s} C _ {k - 1, k} & \text { if } \quad j > i \\ \sum_ {k = i + 1} ^ {N} M ^ {s} C _ {k - 1, k} + M ^ {s} C _ {N 1} + \sum_ {k = 2} ^ {j} M ^ {s} C _ {k - 1, k} \\ \text { if } \quad j <   i, \quad \text { and } \end{array} \right.
$$

$$
\tau_ {i} = \sum_ {k = i + 1} ^ {N} M ^ {s} C _ {k - 1, k} + M ^ {s} C _ {N 1} + \sum_ {k = 2} ^ {i} M ^ {s} C _ {k - 1, k}
$$

procedure to find the node containing the data. A search message is sent to node $i + 1$ , which would forward it to node $i + 2$ until the node containing the data is found. The term $T_{ii}$ measures the communications costs of this ring search. Once the data is found it is transmitted directly to the originating node. Remote modifications and deletes require the same ring search, followed by a direct retrieval and update process between the originating and destination nodes. Add transactions require a search of the entire ring, $\tau_{i}$ , to verify that the identified unit of data does not already exist in the system. This full ring search is required for any directory identified unit of data, even if the data is to be added to the locally held database fragment. Remote adds require additional update transmissions once the search has been completed. Communications costs to support adds are shown in the last two components of the equation.

Fully Replicated Data. A distributed system with fully replicated data requires that a full copy of the system database be stored at each node. Under this type of system remote communications are never required for query processing but each node must be notified to update its data when any add, delete or modify transaction occurs.

Where timely update of data is important, the maintenance of concurrency among the multiple copies of each data item becomes a major concern. Systems designed to guarantee strong concurrency, in which all copies of a unit of data must be identical at the time that any transaction on that data unit is initiated, require locking or time stamp procedures. These procedures may impose heavy communications overhead in order to guarantee the strong concurrency condition, and the amount of communications overhead required varies widely across alternative proposed procedures.

In this paper we assume a system guaranteeing only weak concurrency. That is, there is one node containing the master copy of any data item; all updates must originate through that master node which then transmits appropriate updates to all other copies of the data until receiving confirmation that all copies have been updated. Queries from nodes not containing the master copy of requested data normally obtain it from their local copy with the attendant risk that the local copy is not fully up to date. Queries requiring absolute accuracy can be routed to the node containing the master copy. In this paper we assume that the accuracy of local copy data is adequate for all queries.

The equation below presents the communication costs of a fully replicated system. All queries are handled locally, so that communications costs arise only for update transactions. Modify and delete transactions on data whose master copy

$$
\begin{aligned} FR^{c} & = \sum_{i = 1}^{N}\sum_{\substack{j = 1\\ j\neq i}}^{N}\left\{C_{ij}\Bigl [\big(U_{ij}^{m} + U_{ij}^{d}\Bigr)\big(M^{s} + M^{r} + M^{u}\bigr) \right.\\ & \quad \left. + U_{ij}^{a}M^{u}\Bigr ] + \sum_{\substack{k = 1\\ k\neq j}}^{N}C_{jk}U_{ij}M^{u}\right\} \\ & \quad +\sum_{i = 1}^{N}\sum_{\substack{j = 1\\ j\neq i}}^{N}C_{ij}U_{ii}M^{u} \end{aligned}
$$

is remotely held require that the master copy be found, retrieved, and updated. Adds to a remotely held master copy do not require search and retrieval messages, but do require that the master copy be updated. Once the update to the master copy has been accomplished, message sets are transmitted between the node holding the master copy and every other node of the system to update each copy of the data. These activities are summarized in the first set of terms of the equation.

Updates to a unit of data whose master copy is (or will be) locally held do not require remote communications to find and retrieve the master copy. They do require that the update be posted to each of the remaining nodes, however, and this is indicated by the last term.

Centrally Replicated Data. A variety of schemes for partial replication (more than one but less than N copies of units of data) are possible. It is not possible to treat such variations systematically. However, one particular form of partial replication deserves treatment here because of its wide applicability. This system is one in which a complete copy of the system database and directory is maintained at the central node, while database fragments and local directories are maintained at noncentral nodes. An item may appear in the central database only or may also appear in one noncentral node. The central node is further assumed to contain the master copy of all data, with the noncentral copy being updated following the procedures for maintaining weak consistency described for the fully replicated system.

The following equation indicates the communication costs associated with the centrally replicated system just described. The first term deals with

$$
\begin{aligned} CR^{c} & = \sum_{\substack{i = 1\\ i\neq x}}^{N}\sum_{\substack{j = 1\\ j\neq i}}^{N}Q_{ij}\big(\beta M^{s} + M^{r}\big)C_{ix}\\ & \quad +\sum_{\substack{i = 1\\ i\neq x}}^{N}C_{ix}U_{tx}\big(M^{s} + M^{r} + M^{u}\big)\\ & \quad +\sum_{\substack{i = 1\\ i\neq x}}^{N}\sum_{\substack{j = 1\\ j\neq i\\ j\neq x}}^{N}U_{ij}\Big[C_{ix}\big(M^{s} + M^{r} + M^{u}\big)\\ & \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \\ & \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \\ & \quad \quad \quad \quad \quad \quad \quad +C_{xj}M^{u}\Big]\\ & \quad +\sum_{\substack{i = 1\\ i\neq x}}^{N}C_{xi}\Big[U_{xi}M^{u} + U_{ii}\big(M^{s} + M^{r} + M^{u}\big)\Big] \\ & \end{aligned}
$$

costs associated with queries. Queries on remotely held data give rise to communications costs. All such transactions are accommodated through the copy of the data held at the central node, which is searched with the appropriate data being retrieved to the originating node.

Treatment of updates is rather complex. Remote updates to data held only at the central node require search, retrieval, and update messages between the originating and central nodes, as shown in the second term. Remote updates originating at a noncentral node on data which is copied at a noncentral node require that we first find retrieve and update the master copy of the data at the central node. Then the copy of the data held at the noncentral node j is updated. Updates originating at the central node on data which is copied at a noncentral node i require no remote communication to update the master copy, but do require that the copy at node i be updated, as indicated by the first part of the last term in the equation. The last portion of this term specifies the communications costs, at a noncentral node, of updating data which is copied locally. The master copy at the central node must be searched, the appropriate data retrieved, and the update posted to the master. However it is assumed that the local copy can be updated without further remote communication.

## 3. Simulations under Alternative Patterns of Database Usage

The communications cost equations are complex ones involving several parameters. Comparisons of the communications costs of alternative DDBMS configurations can be achieved by simulation. Because the number of parameters involved is large, an arbitrary base case is selected and simulation runs are developed varying one parameter at a time from its base case value. The parameters of the model are listed below and base case values for these parameters are indicated in parentheses.

(1) The proportion of all transactions $(T)$ which are queries $(Q = 0.75T, U = 0.25T)$ .

(2) The proportion of all updates $(U)$ which are modifications $(U^{m} = 0.75 U, U^{a} + U^{d} = 0.25 U)$ .

(3) The ratio of adds to deletes $(U^{a} = U^{d})$ .

(4) The number of nodes $(N = 5)$ .

(5) The volume of local data held and transactions originated at the central node (equal to the volume of local data held and transactions originating at each noncentral node).

(6) Local usage ratio $(L)$ , which is the ratio of the probability of accessing a local data element to the probability of accessing a nonlocal data element $(L = 2)$ .

(7) The lengths of the search, retrieval and update messages, and the value of $\beta(T^{s}=1, T^{r}=3, T^{u}=4, T^{du}=2, \text{and } \beta=1)$ .

In addition to the parameter specifications, several additional assumptions have been used for all of the simulation runs. The nodes of the system are assumed to be spaced at uniform intervals on the perimeter of a circle with a radius of 1; communication cost between any two nodes is assumed to be equal to the straight line distance between them. All noncentral nodes are assumed to contain data base fragments of equal size and to originate equal numbers of transactions. The probability of accessing a data element is unaffected by its home node location, except as indicated by parameter 6 above. The simulations are performed over a period which is assumed to encompass 500 transactions.

An exhaustive elaboration of parameter value combinations is not practical. However, analysis of the impact of changing an individual parameter while holding all other parameters at base case level are presented. The levels of costs of alternative DDBMS configurations are strongly influenced by the arbitrary combination of base case values chosen, but changes in costs as a parameter is changed give key insights into the effects of data usage patterns on the performance of alternative DDBMS configurations.

Distributed databases are intended for use when there is a large volume of local processing, but remote access to data is still desired. Thus increases in the local usage ratio would be expected to improve the performance of configurations which distribute database fragments. Figure 2 shows that this is in fact the case. Communications costs for the three fully partitioned DDBMS configurations decline markedly as the localized usage ratio is increased from 2 to 20. Costs for the CR configuration decline less rapidly reflecting the fact that the costs of maintaining the central node's copy of the database do not decline as specificity increases. The CDD configuration is unaffected by changes in the localized usage ratio. The modest decline in costs shown for the FR

Local Usage Ratio

![](/api/attachments/YERHCMUC/fulltext/images/0616d29ee6b0c19ef310f64851abfa0d4434506ee5a8689c5e51807e8f2930d7.jpg)  
Fig. 2. Communications Costs versus Local Usage Ratio.

configuration is due entirely to a reduction in the need to find the master copy of a data entity before initiating an update.

Increases in the query proportion tend to cause communications costs to fall in all DDBMS configurations, as shown in Figure 3. However, the decline is really rapid in the case of the FR configuration. For this configuration there is no communication cost associated with queries, while there is a great deal of cost associated with posting update transactions to all nodes. The CR configuration experiences cost declines somewhat sharper than those for the three fully partitioned configurations; while the CDD configuration is the least affected by increases in the query proportion.

The effect of variations in the proportion of updates which are modifications are shown in Figure 4. Variations in this parameter primarily affect the relative performance of the fully partitioned configurations. Add and delete transactions require changes to nonlocal directories while modifications do not. The communications required to update all directory copies under the FRD configuration can be quite heavy, so, as the modification proportion increases and the number of adds and deletes correspondingly declines, costs associated with the FRD configuration fall sharply. The FRD configuration becomes the least costly configuration when the modification proportion is sufficiently high. The same phenomenon applies to the CRD configuration, but to a lesser degree, since only the central node contains nonlocal directory information. Increases in the modification proportion cause a slight increase in $FR^{c}$ and a slight decrease in $DD^{c}$ because of idiosyncracies in the treatment of adds.

![](/api/attachments/YERHCMUC/fulltext/images/71237c9ee71b10fea16eb71a3d30664e35e99035d30cd6372f314d37a89c1b37.jpg)  
Query Proportion  
Fig. 3. Communications Costs versus Query Proportion.

![](/api/attachments/YERHCMUC/fulltext/images/9f3de5607e805b0d411f872a06fe991c0913e61249d59972c6dae663e487112a.jpg)  
Modifies as a Proportion of Updates  
Fig. 4. Communications Costs versus Modify Proportion.

The impact of changes in the number of nodes is shown in Figure 5. Costs of the FR configuration rise most sharply as the number of nodes increases, due to the costs of maintaining copies of all data entities at a larger number of nodes. $FRD^{c}$ also rises sharply with the number of nodes due to added cost of maintaining a nonlocal directory at each node. $DD^{c}$ also rises with increases in the number of nodes, due to increases in the expected number of nodes - searched in order to find a nonlocal data element. $CR^{c}$ and $CRD^{c}$ rise less rapidly than other configurations allowing distribution of data, since they allow some DDBMS functions to be performed by a central node. The CDD configuration has the smallest communications cost increase of all with cost increasing only to the extent that the proportion of transactions originating at the central node shrinks as the number of nodes increases.

![](/api/attachments/YERHCMUC/fulltext/images/8544d0856b77b0c0cde2c4e5ec779b053b78f2bd1f0a6ba6ef2f456bfcc46d2f.jpg)  
Fig. 5. Communications Costs versus Number of Nodes.

Changes in other parameters cause relatively straightforward changes in relative performance. Graphs are not presented for these parameters. Increases in central node size, allowing for a central facility of greater size than the individual non-central nodes, reduces $CDD^{c}$ most sharply and also causes substantial declines in $CR^{c}$ . This is not surprising, since these configurations are the ones which place the greatest reliance on the central node.

Increases in the ratio of adds to deletes cause increased communication costs for the DD system since all nodes must be contacted to ensure that the data entity does not already exist prior to executing an add. Increasing the proportion of adds slightly reduces costs for the FR system since deletes require one to find and retrieve the master copy of the data prior to updating, while adds do not.

As the average length of search messages decreases relative to the average length of data units transferred between nodes (changing parameter 7 above), the communications costs of the fully partitioned configurations fall relative to other configurations. This is reasonable, since the fully partitioned configurations use directory search procedures to minimize the need to transfer data among nodes.

## 4. Summary and Conclusions

This paper has explored communications costs under alternative DDBMS configurations. It has extended previous work by making a more detailed examination of alternative transaction types and by systematically comparing the communication costs of a wide variety of DDBMS configurations. Results under alternative access patterns have been simulated in order to examine their effects on the relative performance of alternative configurations.

Previous studies have suggested that the proportion of transactions which are queries affects the relative performance of DDBMS configurations. Specifically, a high rate of queries relative to updates is expected to improve the relative performance of the FR configuration. The simulation results presented here support that expected result. Increasing the query proportion causes the sharpest decline in costs for the FR configuration, while the fully partitioned configurations experience modest declines with the smallest occurring under the DD configuration.

In addition to treating the query proportion, this paper examines the composition of updates, the proportion of adds versus deletes versus modifications. The mathematical models derived and the simulation results indicate that changes in the composition of updates do have sharply differential effects on alternative DDBMS configurations. Specifically, increases in the proportions of modifications versus adds and deletes tend to improve the relative performance of the configurations with fully partitioned data and replicated directories. The improvement is most profound in the case of the FRD system, where there is a heavy overhead of directory update messages associated with adds and deletes, and these are avoided for modifications. Horizontally partitioned databases can be treated as having all updates in the form of modifications, since individual occurrences of a table do not need to be identified in master directories. Thus FRD configurations are particularly advantageous for horizontally partitioned systems. However, communications costs of FRD configurations can be quite high for vertically partitioned databases with a high volume of adds and deletes. Increases in the proportion of adds relative to deletes, raise the relative communication costs of the distributed directory system since it is necessary to contact all nodes to ensure that the data does not already exist.

Other usage parameters also have significant impact on relative communications costs. All data distributing configurations experience cost savings as the local usage ratio increases, but the decline is by far the sharpest for the fully partitioned configurations. Increases in the number of nodes cause cost increases under all configurations. However, costs are least affected for the configurations (CDD, CRD, and CR) using a central node and most affected for configurations replicating data (FR) or directory information (FRD) across all nodes.

The simulations presented here suggest that each of the configurations can be shown to minimize communications costs under plausible sets of alternative usage patterns. Thus expected usage must be considered in selecting a DDBMS configuration or combination of allowed configurations to be used for a given distributed database application. In addition, in systems allowing multiple configurations and control of configuration selection, usage patterns of various database fragments should be considered in order to determine the best configuration for each type of data. The robustness of alternative configurations under changing usage patterns is also an important design consideration.

## References

[1] Aschim, F., "Data Base Networks - An Overview", Management Informatics, Vol. 3, No. 1, 1974.

[2] Banatre, J. M. Banatre, G. Lapalme and F. Ployette, “The Design and Building of Enchere a Distributed Electron Marketing System”, Communications of the ACM, Vol. 29, No. 1, 1986, pp. 19–27.

[3] Buchanan, J., R. Fennell, and H. Samet, "A Database Management System for the Federal Courts", ACM Transactions on Database Systems, Vol. 9, No. 1, 1984, pp. 72–88.

[4] Champine, G., "Six Approaches to Distributed Databases, Datamation, May, 1977.

[5] Chu, W., "Performance of File Directory Systems for Data Bases in Star and Distributed Networks", Proceedings of the National Computer Conference, 1976, pp. 577–587.

[6] Deen, S., R. Amin, G. Ofori-Dwumfuo, and M. Taylor, "The Architecture of a Generalised Distributed Database System – PRECI", The Computer Journal, Vol. 28, No. 3, 1985, pp. 282–290.

[7] Dutta, A., "Modeling of Multiple Copy Updata Costs for File Allocation in Distributed Databases", International Journal of Computer and Information Sciences, Vol. 14, No. 1, 1985, pp. 29–34.

[8] Fuerst, I., “Close to the Edge”, Datamation, Sept. 1, 1985, pp. 44–50.

[9] Gavish, B., "Models for Configuring Large-Scale Distributed Computing Systems", AT&T Technical Journal, Vol. 64, No. 2, 1985, pp. 491-531.

[10] Gifford, D. and A. Spector, "The TWA Reservation System", Communications of the ACM, Vol. 27, No. 7, 1984, pp. 650–665.

[11] Kohler, W., "A Survey of Techniques for Synchronizations and Recovery in Decentralized Computer Systems", Computing Surveys, Vol. 13, No. 2, 1981, pp. 149–83.

[12] Myers, E., "No DBMS is an Island", Datamation, June 1, 1986, pp. 32–34.

[13] Online Conferences, “Distributed Systems in Practice”, in Distributed Processing, Online Publications, London, 1977.

[14] Phillips, C., "Automated Hotel Systems", Data Processing, Vol. 26, No. 3, 1984, pp. 33–35.

[15] Rothnie, J. and N. Goodman, "A survey of Research and Development in Distributed Database Management", Proceedings of IEEE Third International Conference on Very Large Data Bases, 1977, pp. 48–62.

[16] Rowe, L. and K. Birman, "Network Support for a Distributed Database System", Proceedings of the Fourth Berkely Conference on Distributed Database Management and Computing Networks, 1979, pp. 337–52.

[17] Slonim, J., D. Schmidt, and P. Fisher, "Considerations for Determining the Degrees of Centralization of Decentralization in the Computing Environment", Information and Management, Vol. 2, No. 1, 1979, pp. 15–29.

[18] Spaccapietra, S., “Distributed DBMS Architectures”, in Distributed Data Sharing Systems, North Holland, Amsterdam, 1982, pp. 3–15.

[19] Suyders, J., "Those Belated Distributed DBMSs", Computer Decisions, February, 1981, pp. 77–96.

[20] Taylor, F., “Why Distribute”, in Distributed Database, Online Publications, Northwood, England, 1981, pp. 3–22.

[21] Wah, B., "File Placement on Distributed Computer Systems", Computer, Jan., 1984, pp. 23-32.
