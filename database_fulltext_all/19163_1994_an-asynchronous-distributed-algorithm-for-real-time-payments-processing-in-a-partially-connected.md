---
otero_id: 19163
otero_key: "2DC6YVGX"
title: "An asynchronous distributed algorithm for real-time payments-processing in a partially-connected network of banks"
authors: "Tony Lee; Sumit Ghosh"
year: "1994"
journal: "Information & Management"
doi: "10.1016/0378-7206(94)90093-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# An asynchronous distributed algorithm for real-time payments-processing in a partially-connected network of banks

Tony Lee and Sumit Ghosh \*

Division of Engineering, Brown University, Providence, RI 02912, USA

Keywords: Banking; Payments-processing; Broadband-ISDN; Communication networks; Simulation; Loosely-coupled parallel processors; Distributed algorithm; Modeling; Network of workstations; Financial institutions

The payment-processing system in the banking industry consists of deposits, withdrawals, and transfers of monies through the use of cash, checks, magnetic tapes, and electronic transactions. Of these, nearly all of the check processing through the United States Federal Reserve System, most of the check processing in the private networks, and a part of the electronic transactions are realized through the utilization of the principles of batch-mode processing. This is a conservative and secure means of transaction processing wherein operations, initiated by users, are stored within the system for a certain length of time, typically a few hours to a day or a week, and completed during off-hours i.e.; when the bank is closed to users. Batch-mode processing suffers from many limitations, the principal ones being that: (i) users are denied real-time access to their money, and that (ii) a user's banking privileges cannot be extended – a facility that is increasingly being demanded by users. A centralized banking algorithm, similar to the Swiss Interbank Clearing System (SIC), is inadequate for the United States of America with nearly 12,700 financial institutions and which is extremely vulnerable to a natural calamity or an act of terrorism. This paper proposes a new, distributed architecture for payments processing within a network of major banks as an alternative to the Federal Reserve System. This approach distributes the processing operations to multiple, concurrent, cooperating geographically distributed computers i.e., at many sites, to achieve real-time transaction processing. In essence, a user's most recent account balance and the banking privileges of withdrawal, deposit and, transfer are available to a user, transparently, anywhere i.e., at any of the major banks constituting the network. The accuracy of every transaction is guaranteed and, as a result, (i) banks are not exposed to the risk of fraudulent or bad credits, and (ii) users are not denied complete access to their most recent balances.

![](/api/attachments/2DC6YVGX/fulltext/images/2b092df6678de477ffbe8e28f473ef606264223ef571a0715f6f3bfdb7022bf4.jpg)

![](/api/attachments/2DC6YVGX/fulltext/images/7c627b9fed990792a82246638eaa12f32e441ce2422527de5be030d5619ab09c.jpg)

Tony Lee received his Sc.B. (Honors) in electrical engineering from the Division of Engineering and the A.B. degree from the Political Science department at Brown University in 1992. Currently, Tony is a PhD student in the Division of Engineering at Brown University. His research interests include parallel processing, distributed simulation, broadband-ISDN networks, and decision-making algorithms.

Sumit Ghosh received the B. Tech degree in electrical engineering from the Indian Institute of Technology, Kanpur in 1980. He received the M.S., and Ph.D. degrees from the Computer Systems Laboratory of the electrical engineering department at Stanford University in 1981 and 1984. He then served as a Principal Investigator - Member of Technical Staff at Bell Laboratories Research, Holmdel, New Jersey. Since January 1, 1989 he has been with the Division of Engi neering at Brown University, Providence, Rhode Island as an Assistant Professor. His research interests include asynchronous distributed decisionmaking algorithms for military command and control, integration of geographically-dispersed databases, integration of patient medical records, approximate reasoning for self-healing broadband-ISDN network control, behavior simulation, fault simulation, test generation, distributed real-time payments processing, railway networks, intelligent vehicle highway system, inventory management, and hardware description languages/environments for distributed execution on parallel processors. Additional interests include dynamic debugging environments for distributed algorithms executing on loosely-coupled parallel processors and adaptive, reconfigurable machine architectures.

## 1. Introduction

The payment-processing system in the banking industry utilizes the basic operations of deposit, withdrawal, and transfer of money. In general, for the check-processing subsystem, these operations involve two distinct accounts which in turn may be associated with two distinct banks. Thus, a deposit of a check, in the amount of M dollars, into an account $A^{X}$ associated with bank X, where the check is drawn on another account $B^{Y}$ associated with another bank, Y, implies: Where possible, $B^{Y}$ must be debited by and $A^{X}$ must be credited with M dollars. The transaction, in general, succeeds when $B^{Y}$ has a total balance exceeding M dollars, and fails otherwise. Where $X \equiv Y$ i.e., both accounts $A^{X}$ and $B^{Y = X}$ are associated with the same bank, the transaction will be executed by a central computer, $C^{X = Y}$ owned by bank X. In general, such transactions may be executed instantaneously i.e., $A^{X}$ is debited and $B^{X}$ is credited, simultaneously and in real-time. The instantaneous nature of this operation is made possible primarily due to the fact that $C^{X = Y}$ has complete access to both accounts. Even where bank X maintains multiple branches, the accounts may ultimately reside on the single, centralized computer.

This process may be mathematically modeled as a discrete-event simulation system with feedback loops. When a transaction, say a deposit of a check, is initiated, an electronic stimulus is created and introduced into the system. The stimulus is characterized by the unique identifier of the originating (payee) bank, the distinct identifier of the payer bank i.e., on which the check is drawn, the dollar amount involved, and the time at which the transaction is initiated. Evidently, the stimulus is first propagated by the network to the destination bank. Then, the stimulus is processed. That is, if the unrestricted balance of the payer account exceeds the amount of the check, the account is debited and a return acknowledgement is created. The acknowledgement is characterized by an approval or denial, the dollar amount, and the payee bank identifier. This stimulus is then routed back to the originating bank by the network. In this process, the stimuli are constituted by discrete pieces of data namely, deposit, withdrawal, or transfer of a dollar amount. Furthermore, the stimuli are asynchronous; i.e., they are introduced into the system at irregular time intervals.

At present, the check-processing subsystem of the U.S. Federal Reserve System is primarily batch-mode [1]. Much of the check-processing through the private networks also utilize the batch-mode operational techniques. In this, where a transaction initiated by a user in a region I (as determined by the Federal Reserve) pertains to a payer bank that is included in a different region, II, the transaction is queued at the originating bank. Then, later, when the banking system is “off-line” (i.e., it is closed to the users), the queued transactions are propagated to the appropriate payer banks and are processed.

![](/api/attachments/2DC6YVGX/fulltext/images/c34e68dc1db184108cfa8328118dcdc05ea56456740cd27a2611f222abfcae1a.jpg)  
Fig. 1. A partial organizational layout of the United States federal reserve system.

Figure 1 shows a partial organizational layout of the System; it divides the entire country into twelve regions and permits each of the twelve Federal Reserve Banks (FRBs) to extend their jurisdiction over the appropriate regions. The FRB in San Francisco serves the banks in California, Utah, Oregon, Washington, and Hawaii while the FRB in New York serves the banks in the state of New York. Thus the FRB in San Francisco services Wells-Fargo Bank and Bank of America in California while the FRB in Philadelphia caters to the Merridian Bank, Mellon Bank, and Continental Bank, etc. The solid lines interconnecting the FRBs represent the lines through which transactions are propagated. Let us assume that a user of account $A_{1}$ at Wells Fargo Bank deposits a check, $C_{1}$ , in the amount of M dollars, drawn on an account $B_{1}$ at Citibank. The stimulus $T_{1}$ , created as a result of the deposit, is propagated to FRB in San Francisco for “settlement”. The FRB in San Francisco does not maintain an accurate balance for the account $B_{1}$ of Citibank and, as a result, it is unable to resolve the issue of settlement immediately. However, to ensure the continuation of the nation’s financial system, the FRB in San Francisco advances a credit to Wells Fargo Bank for M dollars and queues up the transaction in a special queue to be mailed to the FRB in New York. Thus, the Federal Reserve System issues a daylight overdraft in the lieu of Citibank and expects Citibank to repay the amount between the time when the banks close for business for the current day and re-opens the following business day. Other transactions initiated at all of the other FRBs that transcend the jurisdiction of the regional FRB may similarly cause the creation of daylight overdrafts and the appropriate queuing of the transactions. At the “end of the banking day” i.e., when the banking system is off-line, the queued transactions are routed to the destination banks for processing. Thus, the transaction $T_{1}$ is propagated to Citibank via FRB in New York where account $B_{1}$ is debited by M dollars and this money is propagated by Citibank to repay for the overdraft issued earlier by the Federal Reserve System. Since no new transactions are introduced into the system at the end of the day and as each and every transaction introduced into the system during the daytime is guaranteed to be routed by the network to the appropriate bank, the sum total of all transactions will execute accurately. For instance, if transactions $T_{1}, T_{2}, \ldots, T_{N}$ , pertaining to the same account $B_{1}$ (originating or destination) at Citibank are initiated at N distinct banks at increasing times $t = t_{1}, t_{2}, \ldots, t_{N}$ respectively, during the current day, the network guarantees that the each and every $T_{i} \forall i \in \{1, N\}$ will be routed to Citibank. Even if $T_{i}$ arrives at Citibank prior to $T_{i+1}$ , although $T_{i}$ was initiated first, the net result, R, given by $R = \sum_{i=1}^{N} T_{i}$ , is guaranteed to be consistent by the commutative and associative laws of mathematics. It may be noted that a $T_{i}$ may be a deposit in the favor of $B_{i}$ (i.e., $T_{i}$ is positive) or a check drawn on $B_{i}$ (i.e., $T_{i}$ is negative) in the favor of another account. If the balance of $B_{i}$ and the net result, R, is such that all transactions succeed i.e., none of the transactions fail, then the order of arrival of the $T_{i}s \forall i \in \{1, N\}$ is unimportant. Where the transitions are, hypothetically, processed in real-time, the following scenario may occur. At some time, due to repeated withdrawals, the account balance for $B_{1}$ has reduced to zero. Consequently, subsequent withdrawal transactions fail. At a later time, a large sum is credited to $B_{1}$ and subsequent withdrawal transactions are honoured. Furthermore, let us suppose that the net dollar amount of the failed transactions is less than the final account balance of $B_{1}$ . Such a scenario will not be observed today, given the benevolent nature of the daylight overdraft system supported by the Federal Reserve System and therefore the people of the United States of America.

A benefit of the daylight overdraft system is the possibility of reduced risk to the participating institutions in the event of failure by one of them to “settle” at the end of the day. However, a limitation of the daylight overdraft system is that, often, the total credit extended by the Federal Reserve System exceeds tens of billions of dollars and occasional problems (e.g. power failures)

compound to create extreme financial risks, such as the Bank of New York incident that led to the largest \$22.6 billion Discount Loan window [3]. Perhaps, the most notable limitation of the current Federal Reserve System is that it is unable to deliver real-time processing. This manifests in a delay, often arbitrarily imposed by the banks and the network, in the processing of a check. The delay may vary anywhere from 1–2 days for an intra-region check to a high of 6 months for international checks. Furthermore, since the FRB in San Francisco maintains account balances for only those banks within its jurisdiction, a difficulty is created when a user of Bank of America tries to access the banking privileges through Midlantic Bank during a business trip to New Jersey. This paper does not consider the issues of check cashing facilities provided by credit cards to a privileged few. These are based strictly on trust and credit worthiness and not the actual bank balance of the user.

In addition to these limitations, the Federal Reserve System's concern with the present network is amplified by the following possible scenarios. First, while the transaction volume of ACH electronic payments is expected to increase by a factor of 10 over the next 5 years [7], checks transactions are expected to increase by $4\%$ a year and there is fear that the current system may be incapable of addressing the increase. Second, the US Congress, under increasing pressure from users whose businesses experience negative impact due to the payments processing delays, may pass laws mandating real-time performance [6]. Third, presently, banks located within a State in the US, are subject to strong State regulations that have been carried forward from the days when the Union was first established. For instance, until a few years ago, banks in Florida were prohibited from crossing county lines [10]. Thus, mergers of interstate banks are infrequent and, where mergers have occurred, the individual banks have maintained unique identities. There is an increasing possibility that the US Congress may revise the banking rules with the result that it permits potential mergers between large interstate banks, say Citibank and Bank of America [4]. Under such circumstances, it is highly likely that a user of Bank of America may demand all of the usual banking facilities through Citibank during a business trip to New York and a user of

Citibank may demand similar privileges through Bank of America while vacationing in California. The recent merger of Manufacturers Hanover Trust and Chemical Bank is pointed out in this context. In essence, there may be strong incentives for the banking network to offer a unified transparent view of the entire banking network to the US public and perhaps to the international community. Finally, the Federal Reserve System is acutely aware that a single, centralized FRB that maintains the most recent balances of the banks that it services is highly vulnerable to natural disasters and artificial catastrophes. The total or even the partial loss of data is simply unacceptable, given its linkage to the world financial markets and the economies of other nations of the world.

A centralized, uniprocessor-based approach to payment-processing may offer the potential of real-time performance with a limited scope. The Swiss Interbank Clearing (SIC) system $[2]$ eliminates the need for daylight overdrafts through real-time processing and achieves this objective through the utilization of a centralized algorithm. Large multi-national companies (such as General Motors with business units located in USA, Australia, and Europe) enjoy real-time performance through dedicated networks – wholly owned or leased, and special banking privileges $[5]$ . Conceivably, a local subset of automated teller machines (ATMs) pertaining to a single bank can potentially offer real-time performance to its local customers. Obviously, under these circumstance, the performance is limited to cash and checks drawn only on the local bank. A principal limitation of this approach is its lack of scalability; i.e., as the size of the system increases, the performance degrades. As a result, the approach is unsuitable for large countries and communities such as the USA, China, India, and the EEC and a country with many large financial institutions, such as Japan. This paper presents a novel approach through the use of multiple concurrent processors that cooperate synergistically through a distributed algorithm.

## 2. A centralized, uniprocessor-based algorithm for real-time payment-processing

In the centralized approach, the most recent balance of every bank must be stored and ac-

cessed by a single computational engine. This is termed the reserve account in the Federal Reserve System. Thus, unlike the current US Federal Reserve network, each bank must communicate directly with a single entity. The single, centralized, computer (SCC) may be located near the center of the country, say Omaha, Nebraska such that it offers uniform link delays to all of the nation's banks. SCC must execute each and every inter-bank transaction. Consider that a user of an account at Wells-Fargo Bank deposits a check for settlement that is drawn on the Bank of Boston. The computer at the Wells-Fargo Bank intercepts the transaction and recognizes that the instrument must be forwarded to the SCC for "settlement". When the SCC receives the transaction, $T_{1}$ , it extracts the identifier of the bank that deposited the check and that on which the check is drawn, the dollar amount (M) of the check and the time at which the check is received. The transaction is first queued for processing, in the correct order, at a later time. When $T_{1}$ appears at the head of the queue, it is processed by the SCC. First, the authenticity of the instrument is verified. Then, the account balance of the Bank of Boston ( $BoB^{bal}$ ) is examined with respect to M. When $BoB^{bal}$ exceeds M, SCC debits the account of the Bank of Boston and credits that of Wells-Fargo by M dollars. Thereafter, an acknowledgement is propagated to the depositing bank (Wells-Fargo). In the event that $BoB^{bal}$ is less than M, the transaction fails immediately and one of two strategies may be adopted: The transaction is queued in a waiting queue to be processed at a later time when new deposits are added to the balance of the Bank of Boston or a failure message is generated and the transaction is dropped.

Since the SCC has complete access to the account balances for each and every bank within its jurisdiction and as all inter-bank transactions are routed to the SCC for settlement, the accuracy of all transactions are ensured. However, the ability to deliver real-time performance is contingent on timely transaction processing. Assume that each of the N banks generate an average of T transactions per unit time destined for the SCC. Assume further that each transaction requires an average of S computer instructions. Thus, the SCC must be capable of processing $N \times T \times S$ instructions per unit time failing which, real-time performance is not ensured. For the USA, N is approximately 12,700 [3] and the Federal Reserve estimates that T is a monotonically increasing function of time. As a result, this approach is unsuitable. Furthermore, while the scalar speed of expensive and high-performance supercomputers, such as CRAY and CDC Cyber, have increased steadily over the past decade, the improvement is extremely modest compared to the magnitude of N and the projected increase in T.

```txt
Individual Client Bank:

receive a user initiated transaction by check
authenticate the transaction

if (check is drawn on the same bank) {
    process the transaction locally
}
elseif (check constitutes an inter-bank transaction) {
    propagate the transaction to SCC
}

Single, Centralized Computer (SCC):

receive a transaction from a client bank
authenticate the transaction and queue it for processing in future
extract the transaction at the head of the queue
extract identifier of depositing bank (A)
extract identifier of bank on which the check is drawn (B)
extract the dollar amount (M)

if (balance of B is equal to or exceeds M) {
    debit the account B and credit the account A
    propagate an acknowledgement to A
}
else if (balance of B is less than M) {
    transaction fails immediately
    either insert transaction in a waiting queue or
    drop the failed transaction
}

advance the head of the queue to the subsequent entry
```  
Fig. 2. A centralized, uniprocessor-based approach for payment-processing.

The SIC [2] system, fully operational by January 1989, was designed to settle over 90,000 payments per hour. The settlement rate was derived from an assumption of a maximum of 400,000 payment transactions on peak days. Although SIC operates on a 24-hour basis for most transactions, ones that are entered into the system after 3pm on a bank working day have their value dates modified to reflect the following day. SIC caters to a total of 156 participating financial institutions in contrast to the Federal Reserve System that services nearly 12,700 institutions.

Figure 2 presents the uniprocessor-based algorithm, expressed in pseudo-code.

## 3. A distributed approach to payments-processing

As an alternative to the Federal Reserve System, the major banks could constitute a partially connected network and realize payments-processing directly, without the need of the Federal Reserve Banks. This approach assumes that a significant fraction of transactions are local, i.e. confined to limited geographical areas about their origins. Every banking node combines the functions of routing and processing transactions. Only a banking node owns exclusive access to and maintains the most recent balances for all of its accounts. Any transaction introduced into the system is routed to the appropriate target bank.

Following its execution, an acknowledgement is returned to the originating bank. In addition, every banking node is assumed to possess complete topological knowledge of the network and computes “virtual paths” to every other node in the network. The notion of “virtual paths” is similar to that in B-ISDN [8].

A banking transaction initiated at a node of the network and requiring processing, may be viewed as a discrete event in the network. In discrete-event simulation, an event is executed at a node and the execution may trigger the propagation of a piece of information to a subsequent node where it is manifested as a new event. For the case of banking, a transaction initiated at a bank, termed the depositing bank, may be propagated to a different bank, termed the payer bank, on which the instrument of payment is drawn. The information to be propagated is encapsulated as a packet, and given the partially connected nature of the network, a packet may be routed by one or more nodes to the ultimate destination. Following the completion of processing at the payer bank, a new event in the form of an acknowledgement is propagated to the payee bank, which may or may not be identical to the depositing bank. The message may either state that the transaction succeeded or that it failed. Thus, information may flow in a cycle and, consequently, the banking system corresponds to a discrete-event simulation system with feedback loops. Given the fact that (i) the banking network is characterized by geographically distributed, processing nodes, (ii) multiple, concurrent computational engines, and (iii) the fact that transactions are asynchronous i.e., they are introduced at irregular time instants, this approach utilizes a variation of the discrete event simulation algorithm [11] to achieve success.

In the Pseudo-Transaction Algorithm (PTA), whenever a banking node processes a transaction represented through a packet - either from the stimulus-queue (i.e., from the users at a corresponding node) or incoming-queues (i.e., originated at other nodes and routed by the network), an outgoing real-packet may or may not be generated. Under normal circumstances, it is generated with an assertion-time value that exceeds the current time value at the node and is propagated to the appropriate destination node. Simultaneously, pseudo-packets containing the new assertion-time value are propagated on all other outgoing paths from the node. In the event of congestion, the incoming transaction may need to be delayed (requued) and, thus, a real-packet is not generated. Under these conditions, pseudopackets with assertion-times equal to the current time value of the node plus the corresponding link propagation delay are propagated on every outgoing link. A natural requirement for PTA is that an actual event, defined at t=0, must be asserted at every node to signify the start of transaction processing. The proof of correctness for this approach is straightforward and is not presented here.

```scss
search, one at a time, over the stimulus-queue and all incoming-queues;
label 1: if (head-event corresponds to a pseudo-transaction) {
    if (next-entry is NULL) {
    use the assertion-time associated with the head-event;
    }
    else {
    advance head-pointer to the subsequent entry;
    go to label 1;
    }
}
else {
    use the assertion-time associated with the head-event;
}
```  
Fig. 3. Algorithm for determining the execution of events in PTA.

![](/api/attachments/2DC6YVGX/fulltext/images/715cb42d0a7ce713e266fde5e1b138499ee18edd2cee0e71549b57f6a9fd2bea.jpg)  
Fig. 4. An example distributed banking simulation.

## 3.1. Execution of events in PTA

The strategy for selecting an event to be executed from among many candidates is based on determining the smallest of the assertion times for all incoming packets. The corresponding packet in the appropriate queue is selected by PTA for processing. This mechanism ensures that the correct order of execution of events, and therefore causality, is consistently honoured. Where $q_{st}$ represents the assertion-time of the head event associated with the stimulus-queue and $q_{i}$ through $q_{n}$ represent the corresponding times for the n incoming-queues, the time up to which the node is processed, $\tau$ , is given by:

$$
\tau = \text { minimum } \left\{q _ {s t}, q _ {i}, \dots , q _ {n} \right\}.
$$

Each of the queues are arranged in order of increasing assertion-times. The basic algorithm of PTA is shown in Figure 3.

In addition, where two competing events are characterized by the same value of assertion-time, a real-packet will always assume precedence over a pseudo-packet. Where two or more events with identical assertion-times are all genuine or all pseudo, the one that is encountered first assumes precedence. Furthermore, where a real-packet associated with one of its receiving queues is the event with the least value of time as well as the only event in that queue, it is processed and thereafter replaced by a pseudo-packet with the same assertion-time.

As an example, consider the simple network shown in Figure 4 where three nodes - A, B, and C, are connected by six unidirectional links $L_{AB}$ , $L_{BA}$ , $L_{AC}$ , etc. Assume that the propagation plus the processing delays for all links are 1 time unit. A real-packet i.e., one that is actually sent in the network, is represented by “XR” and a pseudopacket is expressed in the form “XP”, where X denotes the assertion-time of the packet. The body of the packets containing account and bank identifiers, nature and amount of transaction, etc. are not shown.

For each of the concurrent banking nodes, a real-packet 0R, asserted at t = 0, is shown in the three stimulus queues of A, B, and C. When the model A executes for t = 0, a real-packet 1R is propagated to B and a pseudo-packet 1P is sent to C. These packets are incorporated in the receiving queues – AB and AC respectively. The packets in AB must be subsequently routed to C as per the virtual path. Similarly, when B is executed at t = 0, it sends a real-packet 1R to C and a pseudo-packet 1P to A. Upon execution at t = 0, the node C propagates a real-packet, 1R, to B and a pseudo-packet 1P to A. At this time instant i.e., t = 0, all of the real-packets in the stimulus queues at t = 0 are utilized and, therefore, they are deleted. The deletions are represented through the symbols, X-1, placed under the corresponding real-packets. Each of A, B, and C have packets defined at t = 0 at all of their incoming queues. The packets in the stimulus queues are defined up to t = 10. When A is executed at t = 1, it propagates a 2R to node B and 2P to node C. Upon execution at t = 1, node B propagates two real-packets (2R) to A and C. Both of these packets have reached their destinations and, thus, their virtual path information is nil. When node C executes at t = 1, it sends a 2R to A and a 2P to B. At t = 2, all of the incoming queues of A, B, and C have packets – either real or pseudo, defined at t = 2. The real-packets, asserted at t = 1, that are processed are deleted as identified by the symbols, X-2, placed immediately beneath them. As a result, the nodes will execute and generate more packets. The process continues until the contents of the stimulus queues are completely depleted.

## 3.2. A model of the asynchronous, distributed banking architecture

The distributed banking network architecture is similar to that of the CCITT proposed broadband-ISDNetwork (B-ISDN) except that every packet represents a unique banking transactions and that packets may not be dropped, regardless of the severity of congestion in the network. A banking node, however, may chose to cluster a set of packets, corresponding to a few transactions, all of which are destined for the same target node, and assert it into the network.

The routing mechanism is unique and similar to that proposed for BISDN. It differs from that used for existing wide-area packet-switched networks in that it incorporates a few of the principles of circuit-switching. The network can therefore provide a measure of its performance in propagating the packets. This, in turn, may prove essential towards imposing a fair, tiered charge system on customers for the use of the network. The routing algorithm is based on the concept of virtual paths (route through the network) that connects two end points. For the transmission of a packet representing a transaction, a route is determined, based on available bandwidth, cost, desired performance, etc. A route must be established prior to propagating packets. In our model, a number of standard routes are precomputed during initialization and at discrete points in time during the operation of the network and the allocation of a route to a message is achieved dynamically. Every virtual path is associated with a “service-type”: a combination of the performance and timing characteristics that the network attempts to guarantee for the packets propagating on the path. When packets, representing transactions, are introduced into the network, they are assigned virtual paths by the node. They are then routed, through the banking nodes, from the origin to the destination nodes. The intermediate banking nodes on a virtual path are aware of the existence of the virtual path information within a packet and use this information for routing.

For all possible pairs of nodes of a given banking network, virtual paths are computed based on the “weighted shortest-path spanning tree” [9,12]. Every node is assumed to possess complete knowledge of the network topology and computes the virtual paths to every other node. In this scheme, for a given originating node, other nodes are added to a tree structure in order of their increasing distances from the originating node. Thus, when a new node is encountered in the course of traversing through the network for the first time, the algorithm guarantees that the path from the originating to the node in question is the shortest path. For the banking network, the nodes of the tree correspond to the banking nodes and the weighted paths refer to the links between the corresponding nodes with the appropriate propagation delays. To determine the next-shortest path, one may continue to develop the tree until the node is encountered for the second time. Successive next-shortest paths may be obtained by continuing this process. It may be pointed out that in addition to the propagation delay resulting from the limited speed of electromagnetic propagation over fibres, other parameters such as the processing delay at a banking node may be included to influence the choice paths. The determination and selection of shortest-paths in the context of routing is integral to many networks, including TYMNET, TRANSPAC, IBM SNA, and DEC DNA.

![](/api/attachments/2DC6YVGX/fulltext/images/fb3b7c8b4740b904b042245f2079b6f4d99c733317b08985bd8562026a70adcb.jpg)  
Fig. 5. A graphical representation of a banking node.

## 4. Architecture of the banking simulation program

The simulation program is designed to reflect the functions of each banking node. Figure 5 shows the node with input packets, generated stochastically, asserted at the input ports, and stored in the input buffers. The packets may be either generated at the node reflecting user-asserted transactions at the bank or propagated from other nodes. The node examines the destinations of these packets and, under normal circumstances, propagates them to their destinations. Under exceptional circumstances, such as unavailability of channel bandwidth due to heavy traffic, congestion, or link failures, a few packets, may be requued at the node.

The basic algorithm for modeling the banking node is straightforward. Associated with every node is the notion of the current local time (the minimum of the times up to which all incoming data lines are defined). The model periodically checks for updates. When a new minimum time is computed, a check is made; if it exceeds the current local time, the program then executes the required number of timesteps until the current local time equals the new minimum time. The algorithm and the node-programs in the simulation guarantee that the timestamps associated with the packets, propagated on each and every outgoing link, will increase monotonically. That is, for two consecutive packets on a link, $C_{1}$ and $C_{2}$ with timestamps $t_{1}$ and $t_{2}$ respectively, $t_{2}$ must be either greater than or equal to $t_{1}$ .

The algorithm that defines the simulation of a node-program corresponding to a timestep $t = t_{1}$ , is as follows. At local time, $t = t_{1}$ ,

\- 1. Check all links for incoming packets. The node blocks until at least a single packet has been received at a link. Input packets are stored in the input buffers corresponding to the link identifier. For every new entry into a buffer, the assertion time is guaranteed to exceed that of the most recent entry in the buffer.

\- 2. The input buffers including the file that stores input packets asserted at this node (link number 0), are examined and the minimum assertion time over all of the packets is determined. This minimum value is be either equal to or greater than the current simulation time at the node. When the value of the new minimum time exceeds the current simulation time, the latter is updated to reflect the new minimum time value.

\- 3. For every incoming link, extract from the corresponding simulation buffers all packets with timestamps equal to the current simulation time. These must be processed immediately. For each packet, there are four possible scenarios.

\- i. If the packet is a real-packet and is destined for this node, the corresponding transaction is executed, updating the balance, where possible, and generating an acknowledgement. The acknowledgement may indicate a success or a failure and is placed on the output buffer with an assertion time equal to the current time plus the node delay.

\- ii. If it is a real-packet or an acknowledgement not destined for this node, its assertion time is updated by the node delay and it is included in the output buffer for subsequent propagation. The exact output link at which the packet is asserted is determined based on the virtual path associated with it.

\- iii. If the packet is a pseudo-packet, representing an update of the simulation time, it is utilized in step 2 and does not cause any output to be placed in the buffers.

\- iv. If the packet is a real-packet, originating at this node, the node computes the most appropriate virtual path based on the destination. This virtual path is embedded in the appropriate fields of the packet and it is placed in the output buffer.

\- 4. The output buffer is evaluated; i.e., the packets in the buffers are examined. For each packet, the following two scenarios are possible:

\- i. If the packet is successfully propagated, prior to sending it, its timestamp is updated with the propagation delay of the link.

\- ii. If the capacity of the link on which the packet must be sent (based on the predetermined virtual path) is exceeded, the packet is requued in the output buffer and its assertion time is incremented. The capacity of a link, Y, implies that a packet may be propagated every Y timesteps. When a packet is propagated at time $t_1$ , the subsequent packet on the same output link may be sent at $t_1 + Y$ , the next packet at $t_1 + 2 \times Y$ , and so on. Therefore, for a packet that is requued in the output buffer with N packets ahead of itself, the assertion time must be incremented by $N \times Y$ .

The node-program consists of three conceptual parts that are described as follows: Buffering and Processing of Input Packets

The primary need to buffer incoming packets stems from the fact that the simulation proceeds at different speeds on different nodes, depending on the load at the individual nodes. When a packet with a timestamp $t = t_{x}$ arrives at a node where the current local time, $t = t_{y}$ , is less than $t_{x}$ , the packet may not be processed immediately. Such packets have arrived “too soon” i.e., they have arrived sooner than they would in reality. As a result, they are buffered until the current local time increases to a value $t \geqslant t_{x}$ . Then, the packet is extracted from the buffer for processing by the banking node. It may be noted that the notion of buffering is an artifact of the simulation. In reality, the phenomenon of packets characterized as “arrived too soon” is non-existent in reality.

The common principle of polling the input links was not utilized for two reasons. First, the continuous use of polling is expected to consume significant CPU time. Second, as control is surrendered to the operating system less frequently in the event of polling, it contradicts the authors' desire to execute the simulation as a background job on the workstation without seriously affecting other users. Instead, a mechanism is utilized wherein, for a specified maximum time interval, the system call listens for incoming packets only for the specified time. Thereafter, the operating system returns control to the node-program. Where a packet arrives at the link within the specified time interval, the operating system immediately returns control to the node-program. This approach was observed to be highly efficient. That is, under normal conditions, the node-program executed at normal priority, consuming less than 20% of the available CPU time, and the normal interactive usage by others was hardly affected.

## Switching Packets through the Node

Presently, packets that are deemed executable are extracted individually from the pool in any random order. Thus, except for their timestamp values, the packets are not prioritized. A packet is forwarded to the proper send queue and the process continues until the pool is empty. The send queues are accessed by the packet transmission routines on a first in first out (FIFO) basis. Transmission and Buffering of Outgoing Packets

As permitted, any one of the multiple ready packets is selected at random, extracted from the appropriate send queue, and transmitted over the proper link. When multiple packets compete for transmission, one or more may need to be re-queued.

## 5. Implementation issues

The distributed simulator was written in C and consists of approximately 2100 lines of code. It was compiled utilizing the Sun ANSI standard C compiler, acc without optimization. The simulator is executed on a network of 50 + Sun Sparcstation1 (Sun 4/60) workstations, each with 16MB of main memory and CPU's rated at 12.5MIPs. All the workstations are connected through Ethernet, with most of the file systems mounted remotely off two Sun 4/490 file servers using Sun's Network File System (NFS).

The simulations are run in background at low priority while the workstations are in regular use by other users. The priority is adjusted such that the CPU usage by a node-program at any of the workstations is limited to approximately 20%.

The input stimulus is realized through packets that are generated by stochastic means, i.e. through the use of pseudo-random generators. For each packet, its type - debit or credit, the amount, and the payer and payee account identifiers are all stochastic quantities. Inter-packet timings are also stochastic quantities.

![](/api/attachments/2DC6YVGX/fulltext/images/dd2e15284017e94f92076e8cf50cd131ad0eac2a1a3a5732bc9ed2d6056ba93b.jpg)  
Fig. 6. A 20 node banking network.

## 6. Performance of banking network simulation

## 6.1. Experimental banking networks

Simulation utilizing three banking networks consisting of 10, 20, and 50 nodes with a total of 50000, 100000, and 250000 input packets, respectively, were employed. Only the 20 node network is shown here. In Figure 6, the node names are arbitrary. Associated with every link is the value of the propagation delay, computed from dividing the length of the link by the speed of electromagnetic transmission in optical fibres. The second quantity, associated with every link, refers to its capacity as a fraction of the basic 155.52 Mbits/sec (B-ISDN) link. Thus, since the capacity of a link is “6”, the link is six times slower than the basic link.

Simulation execution times as a function of input transactions and network size

<table><tr><td>No. of banking nodes (No. of processors)</td><td>Transactions asserted</td><td>Elapsed time (sec)</td><td>CPU time (ms) per transaction</td></tr><tr><td>10</td><td>50000</td><td>203.49</td><td>4.07</td></tr><tr><td>20</td><td>100000</td><td>520.54</td><td>5.21</td></tr><tr><td>50</td><td>250000</td><td>1237.05</td><td>4.95</td></tr></table>

## 6.2. Results

Execution Times

Table 1 presents the total simulation times for the different networks, using appropriate number of workstations, as a function of the input pack-

![](/api/attachments/2DC6YVGX/fulltext/images/c11efef5d24b8fcde723a94d3ba88b1ea86d2ff219c6b0c385b9bbbe72bcceef.jpg)  
Fig. 7. CPU time (ms) per transaction (real) as a function of network size.

ets. The data is obtained for the case of 50% "transaction-volume." At each node, packets were generated and asserted at every timestep. This corresponds to the case of 100% transaction-volume. Where transactions are asserted at the average rate of M (0 ≤ M ≤ 100) per 100 timesteps, the transaction-volume is defined as M%. Given that multiple workstations execute simultaneously, the total simulation time is computed as the maximum of the CPU times of all participating workstations. The last column presents the average time required for processing a transaction for each of the three networks and is shown in Figure 7. Since increased transaction-volume is likely to imply slower processing speed, the average transaction time is likely to be lower for lower transaction-volume values. The nature of the graph reveals that, even as the size of the network increases fivefold, the average time to process a transaction increases only by 26%. While the increase reflects the increased average node processing, link delays, and overhead, the size of the increase attests to the algorithm's scalability. That is, as the banking network grows in size, the number of available processors in the system also increases and, as a result, the total system throughput increases without adversely affecting the processing time of individual transactions.

The reported performance of the distributed simulation is pessimistic, since pseudo-packets will be completely absent in an actual banking network. Furthermore, given that a significant fraction of the transactions are likely to be confined to a limited geographical area (for efficiency), the overall network may be structured hierarchically.

![](/api/attachments/2DC6YVGX/fulltext/images/2401de638f713a58844fc73121bbc0483bc12022c3cf04eb3897cadcad4586e4.jpg)  
Fig. 8. CPU time ( $\mu$ s) per transaction (real and pseudo) as a function of network size.

At the lowest level, a limited number of banking nodes, say 50 to 100, are organized into groups where the nodes are connected through intra-group networks and deliver fast performance. High performance is essential at this level, since most transactions are local to their respective groups. At the next higher level, groups are interconnected through an inter-group network that offers slightly reduced but acceptable performance, since relatively few transactions cross group boundaries.

The evidence of scalability is observed across different values for the transaction-volume factor, as shown in Figure 8, where the elapsed time is divided by the total number of transactions that includes both real- and pseudo-packets. While the size of the network increases fivefold, the average time to process a transaction increases by

86%, 48%, and 36% corresponding to the transaction-volume values of 10%, 30%, and 50% respectively. The values along the Y-axis are expressed in the units of microseconds.

Figure 9 presents the average size of the output queues of node 1 for the 20-node banking network, obtained from dividing the cumulative sizes of all the queues of node 1 divided by the total number of output queues. The data is computed every timestep and is plotted against the transaction assertion time, for different values of transaction-volume. At relatively high values for transaction-volume, namely 40% and 50%, the queue size increases linearly with time, implying that transactions are queued faster than they are serviced by the network. For lower values of transaction-volume namely, below 35%, the size of the queue is constant with time implying that the transactions are processed as fast as they are added to the system.

![](/api/attachments/2DC6YVGX/fulltext/images/b0a20ee4c4577d56791c6fd89900d71ec809541b82c7a74edabfbb6b364b2439.jpg)  
Fig. 9. Average output queue size between nodes 1 and 13 for a 20 node banking network, as a function of transaction assertion time.

The graphs in Figure 10 present the completion times of the transactions, for the 20 node banking network, as a function of the transaction-volume. The graphs correspond to the transactions between nodes 1 and 5. The choice of the node pair $\{1, 5\}$ is based on the fact that it corresponds to the worst-case scenario: the completion times of the transactions are the highest among all other possible pairs of nodes. A transaction is complete when it has been routed to its destination by the network, executed at the destination bank, and an acknowledgement has been returned to the originating banking node. A total of five scenarios are considered corresponding to 5%, 10%, 11%, 12%, and 15% transaction-volume values. The x-coordinate of a transaction refers to the simulation time, in timesteps, at which it is asserted into the network. The y-coordinate refers to the simulation time required for the transaction to complete. Transactions are asserted into the system, between 0 and 10000 timesteps. However, given that they are produced stochastically, the assertion of transactions for a case may terminate prior to the simulation time being equal to 10000 timesteps. All of the transactions, asserted into the system, are verified to execute to completion. The values for the mean, standard deviation, minimum, and maximum completion times are presented in Table 2.

Table 2  
Transaction propagation measures as a function of transaction-volume for 20 node banking network

<table><tr><td>Congestion Level</td><td>5%</td><td>10%</td><td>11%</td><td>12%</td><td>15%</td></tr><tr><td>Mean completion time (timesteps)</td><td>95.9</td><td>76.4</td><td>269.4</td><td>288.0</td><td>1260.2</td></tr><tr><td>Standard deviation (timesteps)</td><td>174.3</td><td>83.8</td><td>243.9</td><td>250.6</td><td>720.0</td></tr><tr><td>Minimum completion time (Ideal)</td><td>16</td><td>16</td><td>16</td><td>16</td><td>85</td></tr><tr><td>Maximum completion time (timesteps)</td><td>859</td><td>368</td><td>761</td><td>819</td><td>2608</td></tr></table>

![](/api/attachments/2DC6YVGX/fulltext/images/c79b6bdb66867c38c1c5764f2357ba79a001ae056fe1b4c9596b95eb8da970c0.jpg)  
Fig. 10. Transaction completion times as a function of the transaction-volume.

For the given link delays in the network, the minimum time that a transaction may require between nodes 1 and 5, is 16 timesteps. In the course of the simulation, a few transactions are actually observed to require 16 timesteps. However, the minimum completion time for the 15% transaction-volume scenario is a high of 85 timesteps. On the other hand, in the event of high transaction-volume, a few transactions are observed to require significant completion time. In general, as the value of the transaction-volume increases (i.e., as more and more transactions are asserted into the system), the mean and standard deviation increase, with one exception. For the 5% transaction-volume case, a few transactions are delayed significantly due to excessively low capacity of an intermediate link; this contributes to high values for the mean and standard deviation.

In a banking network, one of the major concerns is likely to be the value of the factor, F, defined as the ratio of the maximum completion time to the lowest possible completion time. The values of F are observed to be 53.7, 23, 47.5, 51.2, and 163 for the 5%, 10%, 11%, 12%, and 15% cases respectively. The value of F reflects the degradation of performance, compared to the ideal, due to the high volume of transaction traffic and the consequent congestion. The exact value of F may depend on many factors – economic, political, etc.

![](/api/attachments/2DC6YVGX/fulltext/images/4423fcd56d32c94dc23829e20b4d09f946d59183eb70992f14bcaad6132576eb.jpg)  
Fig. 11. Transaction completion times as a function of increased values of transaction-volume.

Figure 11 presents the completion times of the transactions for high levels of transaction-volumes. While transactions require significantly larger completion times, it may be noted that the slopes of all of the curves are modestly positive, with one exception. For the 10% scenario, the slope is nearly zero implying that as transactions continue to be asserted to the system, they are continuously and promptly completed. Under this scenario, transactions are rarely accumulated at different nodes due to congestion and the system may be sustained, relatively, on a continuous basis. In contrast, for increasing levels of congestion - 30% to 70%, more and more transactions are requued locally and the time for completion increases, even when the assertion of transactions into the system is discontinued. The different curves serve as a model for different qualities of banking service with appropriately tiered charges. Furthermore, although the assertion of transactions into the system is discontinued at t = 3000 timesteps, the graphs for the 10% and 70% cases do not extend up to 3000 timesteps, implying that the input traffic is discontinued even sooner. The simulation continues to run for an additional 8000 timesteps, without any input stimulus, to allow the completion of all transactions.

## 7. Conclusions

This paper has proposed an asynchronous, distributed architecture for banking within a network of major banks as an alternative to the Federal Reserve System. This approach has distributed the processing operations to multiple, concurrent, cooperating geographically distributed computers to achieve real-time transaction processing. It utilizes the principles of a asynchronous, distributed, discrete-event simulation algorithm utilizing pseudo-transactions (timestamps), and guarantees the accuracy of every transaction. Given that the major banks are geographically distributed throughout the entire country, the distributed nature of the algorithm, proposed in this paper, is extremely appropriate. It offers the hope of a banking system that is available, transparently, to a user anywhere within the coverage area of the network. In essence, a user's most recent account balance and the banking privileges of withdrawal, deposit, and transfer are available to a user, transparently, anywhere i.e., at any of the major banks constituting the network. Moreover, the facility to initiate multiple transactions corresponding to a single account, simultaneously in time, at different geographical points, is permitted. The accuracy of every transaction is guaranteed and, as a result, (i) banks are not exposed to the risk of fraudulent or bad credits, and (ii) users are not denied complete access to their most recent balances. In addition, while the balances of accounts at each of the major banks are owned exclusively by the respective banks, thereby implying privacy and security for them, any transaction inserted anywhere in the system is correctly routed to the target bank for execution. This paper has also reported an implementation of such a model of a network of banking nodes on a network of SUN workstations, configured as a loosely-coupled parallel processor, at Brown University. Performance analysis indicates that this approach achieves a very high throughput for transaction processing.

## References

[1] Collin Canright, “Will Real-Time Systems Spell the End for Batch Processing,” Bank Administration, Vol. 64, No. 9, September 1988, pp. 42–46, Rolling Meadows, Illinois.

[2] Christian Vital and David Mengle, "SIC: Switzerland's New Electronic Interbank Payment System," Economic Review, Vol. 74, No. 6, Nov/Dec 1988, Federal Reserve Bank of Richmond, pp. 12–27.

[3] David B. Humphrey, “Payments System, Risk, Market Failure, and Public Policy,” in Electronic Funds Transfers and Payments: The Public Policy Issues, Ed. by Elinor H. Solomon, Kluwer Publishers, Boston, 1987, pp. 83–110.

[4] Private Communications with David Humphrey, Federal Reserve Bank of Richmond, Virginia, December 1989.

[5] Private Communications with George McGovern and Kuldeep Tuteja, The Chase Manhattan Bank, New York, New York 10038, December 1990.

[6] Private Communications with Niels Larsen, Federal Reserve Bank of Boston, Massachusetts, March 1989.

[7] Electronic Payments Processor, Pilot Project: Request for Proposal, Federal Reserve Bank of Philadelphia, PA 19106, August 1988.

[8] Anna Hac and Hasan B. Mutlu, "Synchronous Optical Network and Broadband ISDN Protocols," IEEE Computer, Vol. 22, No. 11, November 1989, pp. 26–34.

[9] Sedgewick, Robert. Algorithms, Addison-Wesley Publishing Company, Reading, Massachusetts, 1988.

[10] William M. Randle, "Banks," Proceedings of the Conference on Payments in the Financial Services Industry of the 1980s, Quorom Books Publishers, Westport, Connecticut, 1984, pp. 61–68.

[11] Sumit Ghosh and Meng-Lin Yu, "An Asynchronous Distributed Approach for the Simulation of Behavior-Level Models on Parallel Processors," Proceedings of the 1988 International Conference on Parallel Processing, August 15–19, 1988, St. Charles, Illinois.

[12] Schwartz, M. and Stern, T.E., “Routing Techniques Used in Computer Communications Networks,” IEEE Transactions on Communications, Vol. COM-28, No. 4, April 1980, pp. 539–552.
