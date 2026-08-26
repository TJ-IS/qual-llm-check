---
otero_id: 17176
otero_key: "B5GKY32J"
title: "What can we do with distributed discrete event simulation in design analysis of distributed database systems"
authors: "Ellen Konstantinova Stancheva"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90050-l"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# What can we do with distributed discrete event simulation in design analysis of distributed database systems

Ellen Konstantinova Stancheva
Computer Science Department, Institute of Mathematics,
Bulgarian Academy of Sciences, 1113 Sofia, Bulgaria

In designing distributed database systems, concurrency control and recovery mechanisms must be selected from a field of candidates. The crucial criterion for choosing a combination of particular algorithms is their individual and integrated performance. Instead of applying analytical and/or conventional simulation techniques, we suggest that distributed discrete event simulation be applied. The technology developed is based on subjecting to distributed simulation the distributed transaction management of the real system. It captures, in a distributed environment, the processing, storage and communication resources of the whole distributed database system. After introducing a methodological motivation, this technology is presented in the form of: a reference performance model of distributed database systems, corresponding distributed simulation model, and a distributed simulation algorithm based on Chandy-Misra-Bryant approach.

Keywords: Distributed database technology, Distributed transaction management, Concurrency control, Recovery, Distributed simulation, Chandy-Misra-Bryant approach.

![](/api/attachments/B5GKY32J/fulltext/images/fca207ca4208563e2f94c6b3444bf4087688b9ad7a0ff71b561f2d3d615c296e.jpg)

Ellen Stancheva received her M.Sc. and Ph.D. degrees in mathematics and computer science from Sofia University in 1975 and 1979, respectively. Her Ph.D. research concerned the area of software engineering technologies. Since 1983 she has been a research staff member of the Institute of Mathematics, Computer Science Department at the Bulgarian Academy of Sciences, Sofia. Since then she has also lectured at Sofia University, Department of Mathematics and Computer

Science. Presently she is with the Process Control and Instrumentation Group, Electrical and Controls Engineering Department at Ontario Hydro, Toronto, Ont., Canada. She is also an international associate member of the McLeod Institute, California State University, Chico, U.S.A. Her research interests include expert systems, distributed systems, distributed database systems, computer simulation. She is a member of the International Federation of Automatic Control (IFAC), the Society for Computer Simulation International (SCSI), and the Bulgarian Scientists Association.

## 1. Introduction

The technology of distributed database systems has already built to a great extent its theoretical foundations $[3,5]$ and has been used in a large number of applications. A part of the research literature in this field is dedicated to quantitative analysis and comparison of the performance of single transaction management approaches $[8,17,10,19,23]$ . These studies usually apply analytical modelling and/or simulation under limited operating conditions. Some of the authors comment on the difficulties of comparing such studies: different assumptions about system and application environments are used, different measures for system performance are applied. In most of the performance studies, the interference of the adopted algorithms is not considered, as it makes the models too complex to be workable. The evaluation of decisions associated with several design stages, is also avoided as it is not feasible by the conventional tools mentioned.

Within this scope, it is important to have an environment in which combination of the mentioned services are feasible. To provide such an environment for the process of analysis and design of distributed database systems, we propose that distributed discrete event simulation be applied. The essence of this approach is subjecting distributed transaction management to distributed simulation. The goals of distributed transaction management – efficient, reliable and concurrent execution of transactions – are strongly interrelated; moreover, there is a trade-off between them, because the effort which is required to implement the properties of transactions in a reliable way causes an obvious performance penalty. By subjecting distributed transaction management to distributed simulation we aim at providing an environment for envisioning the most appropriate, from the application viewpoint, combination of concurrency control, recovery techniques and utilisation of the resources. Such an environment can ensure the overall evaluation of decisions, concerning several database design stages simultaneously. The approach is also applicable to the different techniques which have been proposed in the research literature but have not been implemented in real systems. It is not clear in what way such techniques perform and affect each other; therefore, a performance evaluation could also be reasonable. Finally, the approach allows a cooperative design of distributed DBMSs, whether or not a computer conferencing system is set up or not.

Our notion of distributed simulation includes the Chandy–Misra–Bryant approach, although the technical considerations developed can be applied to some other distributed simulation methods of the same type. We consider it reasonable to embed this classical approach into our first model, realising that only detailed experimental studies in the next several years will prove which of the existing methods is the most viable [16].

For the purposes of building the technology of distributed simulation of distributed database systems, we need to distinguish between distributed discrete event simulation methods which entirely or partially transfer the parallelism of the system being simulated in the model, and methods which do not consider this parallelism. We call these groups of methods allocation-bound (AB) and allocation-free (AF) types of distributed discrete event simulation (DDS), respectively.

A major concern of the study is the more rereally considered DDS/AB (allocation-bound distributed simulation) and its potentiality to the analysis of distributed database systems with a high degree of site autonomy (i.e., degree of inherent parallelism high enough to benefit the simulation, if embedded into the simulation system). Insights into time synchronization, concurrency control, and deadlock protection problems are included. The exposition of the approach is based on the Basic distributed simulation algorithm of Chandy, Misra and Bryant with null messages for deadlock avoidance, although some other distributed simulation methods may also be applied to the technology presented. We introduce a combined distributed simulation algorithm (DDS/AB type) of some of the most well-known transaction management techniques, namely the basic 2-phase-commitment protocol (for recovery) and the basic timestamp mechanism with prewrites (for concurrency control). In the same way, distributed simulation mechanisms, corresponding to versions of the 2-phase-commitment protocol, and other concurrency control, and deadlock detection and resolution algorithms can be developed and easily introduced in the scheme developed (making use of software modules kept in a library).

Distributed DBMSs are used as reference systems, for the study. One may well ask why distributed DBMSs are chosen, rather than some other complex distributed systems, such as communication networks, traffic control, assembly line systems, etc., which typically exhibit a high degree of concurrency (large ratio of computation to communication). In our opinion, the establishment of the technology of the distributed simulation of distributed DBMSs will naturally result in a direct implementation to the rest of the distributed applications mentioned. One of the reasons is that such systems, more often than not, include distributed information services, themselves.

An early development of the technology, in which a simplified DBMS model is used, is presented in [20].

The organization of the paper is as follows: after some preliminaries and motivation for the application of distributed discrete event simulation in the second section, section 3.1 and 3.2 introduce: a reference performance model of distributed database systems, corresponding distributed simulation model, and distributed simulation algorithm. Section 4 is a discussion on the advantages and drawbacks of the approach. The example contained in section 5 enlightens the main ideas of the distributed simulation approach under discussion.

## 2. Methodological Preliminaries: Development and Motivation

With regard to the necessity to differentiate between two fundamentally different types of distributed simulation approaches on the basis of performance, in our investigation, we introduce some methodological preliminaries and developments.

The idea of distributed simulation was proposed by Chandy [6] and independently by Bryant [4]. These approaches advocate the process view of simulation - they control parallel processes without shared variables - and differ mainly in the memory requirements and the deadlock considerations. Later, there appeared distributed simulation techniques differing mainly in their approach to time management. The group of Peacock, Wong and Manning started to work in the field [14,15] with a taxonomy, which characterizes the different simulation methods. The taxonomy of Peacock et al. is extremely valuable and was developed early enough to incorporate all the incoming results into the building of the integrated technology of distributed simulation. But, in our opinion, it has not been referred to often enough.

Among the moderate number of existing methods, it is convenient to distinguish between two fundamentally different approaches: distributed simulation methods which involve a certain (complete or partial) mapping between the application allocation schemes of the physical and simulation systems, and methods which do not presuppose any application-oriented correspondence between these allocation schemes. We call the former allocation-bound distributed simulation and the latter, allocation-free distributed simulation. This distinction differs from some other very useful ones, such as those of Wyatt and Sheppard [24], based upon distribution of the model functions or simulation support functions; Reed and Malony [16], based upon static and dynamic node assignment, etc. In the allocation-bound cathegory of distributed simulation approaches, we include not only approaches with one-to-one application allocation mapping between the processes in the real and the simulation system, but approaches allowing the simulation model to be application-allocation-bound to a different degree (i.e., part of the processes be truly mapped, the rest combine - several processes on a site), as well.

The degree to which a simulation model is application-allocation-bound is concerned with the degree of parallelism of the real system, transferred to the simulation system. One simple way of expressing this degree is by the ratio of truly (one-to-one) assigned processes to nodes in the simulation system, to all processes in the real system.

With regard to this, we propose a specific level in the Peacock et al. classification (see fig. 1).

At the first level, it is determined whether there is a multiprocessor with a shared memory, or a network of processors available. The next level deals with the event-driven (discrete event) and the time-driven (continuous) nature of simulation. The third level presents tight and loose types of simulation (“loose” means that the simulation time in the component processes is different at any instant of the real time; “tight” means that it is the same). The next level is the newly proposed one, which differentiates between allocation-bound and allocation-free simulation methods. DDS/AB is appropriate for distributed systems whose inherent parallelism is significant enough to be considered in the simulation. The alternative form, DDS/AF, exhibits less parallelism of the physical system and gets benefit only from the extended computer power of a multiprocessor or a network environment.

![](/api/attachments/B5GKY32J/fulltext/images/78a18d162a1447d127e0ad1f21f91bc7dff5b5b7f1a43c66123779b2775b0be7.jpg)  
Fig. 1. Additional notations on the taxonomy tree of Peacock et al.

We are interested in distributed simulation tools appropriate for the simulation of distributed systems with a high degree of parallelism, and our investigation concerns mainly distributed event-driven loose type simulation. Not many studies in this field have appeared in literature. Most of them adopt the process view of simulation $[6,14,9,2]$ : a system being simulated is assumed to consist of a finite number of physical processes, which interact at discrete instants of time. The process interactions are called events and the time instants at which they occur, event times. Each physical process of the system is simulated by a logical process. Events appear to happen in a consistent order at all processes in the system, even though they may not physically be executed in that order.

We consider the basic cooperation schemes of DDS/AF and DDS/AB to be different mainly in: the presence of global control exercised by a process in the former, and in the realization of correspondence between the available hardware in the real and simulation systems without any global control, in the latter.

## 2.1. Allocation-Bound Distributed Simulation (DDS / AB)

As was already stated, DDS/AB involves some correspondence between the available hardware in the real and simulation systems, as one or several physical processes are simulated on the corresponding site. It was also declared that, such execution occurs using a distributed control algorithm, without any global control.

The simulation system consists of a finite number of processes and directed channels connecting some pairs of processes. Communication is permitted only by passing messages between processes; each process maintains its clock; different clocks are associated with channels and move forward in an asynchronous manner. The strict chronological sequence of events can be realized solely by messages in which the physical time and the event type are encoded. Most of the algorithms that have appeared in the literature employ this classical Chandy–Misra–Bryant scheme, and they differ mainly in the method of deadlock resolution.

As a representative of the DDS/AB methods, we have chosen to adopt and conform the Basic distributed simulation scheme $[6,12]$ , described below. The correctness proof of the algorithm and its variant with null messages for deadlock avoidance, are provided in $[12]$ . The proof that there is no deadlock in the situation is essentially contained in $[7]$ . The same results hold true if the buffers are not unbound. The buffer spaces can be decreased by introducing annihilation rules. The number of the sent null messages could be limited if null messages are transmitted after a proper time-out.

Basic distributed simulation algorithm: Consider n logical processes $p_{1}, p_{2}, \ldots, p_{n}$ simulating, respectively, the behaviour of n physical processes $P_{1}, P_{2}, \ldots, P_{n}$ . A channel $c_{ij}$ exists from $P_{i}$ to $P_{j}$ , if $P_{i}$ can send messages to $P_{j}$ . $p_{i}$ can simulate $P_{i}$ up to time t if it knows the initial state and all the messages that the $P_{i}$ is to receive up to time t. If message m is sent by $P_{i}$ to $P_{j}$ at time t, message (t, m) has to be sent by $p_{i}$ to $p_{j}$ at some point during simulation. If $p_{i}$ sends a sequence of messages to another $p_{j}$ , a requirement to increase the time component is stated. The channel clock value of a channel $c_{ij}$ is the t component of the last message received along that channel; the channel clock value is 0 if no message has been received along that channel. The clock value of $p_{i}$ is the value $T_{i} = \min_{j} \{t_{j}\}$ , where $t_{j}$ 's are the channel clock values of all incoming channels to $p_{i}$ . If $p_{i}$ has no incoming channels, it is the source process; if $p_{i}$ only receives messages without affecting the simulation, it is the sink process. Null message (t, null) is sent by $p_{i}$ to $p_{j}$ when $P_{i}$ sends no message to $P_{j}$ between the current $c_{ij}$ clock value and t.

The scheme is the following [12]: “Whenever $p_{i}$ receives a message, it properly updates $T_{i}$ ; if $T_{i}$ changes in value, then $p_{i}$ advances the simulation of $P_{i}$ up to $T_{i}$ . At this point $p_{i}$ predicts for each outgoing channel, a sequence of messages that the $P_{i}$ would have sent.”

## 2.2. Allocation-Free Distributed Simulation (DDS/AF)

We consider DDS/AF a minor issue for the stage of the study described and briefly present it for the sake of completeness.

Simulation of a system by a DDS/AF method can be adapted to the structure of the available hardware, and is executed in the presence of global control exercised by a main process.

The basic idea is to define a global time [9] common to all processes and local time for each simulation process. A process is considered to be anticipating when its local time is strictly greater than the global time. Messages deliver the value of the local time when the receiver is the main process, and the value of the global time, when it is an ordinary one. Each process is allowed to execute local actions whatever its local and global time might be. When a process starts another process, the starting time of the son process will be the local time of the father process, when the operation is performed (the initial process is only started by an external operator).

## 2.3. Comparison between DDS/AB and DDS/AF

A desired quality of distributed simulation possessed by both types of simulation, DDS/AF and DDS/AB, is transparency, i.e. a conventional simulation model does not need to be modified in order to be inserted in these two frameworks. It is interesting to note that DDS/AF has a greater degree of transparency in comparison with DDS/AB. In DDS/AB, the transparency is comparable to that in the physical system. For instance, if the physical system provides fragmentation transparency (i.e., the user is unaware of fragments and their allocation) the same type and degree of transparency can be simulated by a DDS/AB method.

DDS/AF is more conservative than DDS/AB and exhibits a lower degree of parallelism from a given simulation problem. On the other hand, its cost (memory and processing) is much lower.

Evaluation of advantages and drawbacks of DDS/AB and DDS/AF is an interesting, but difficult problem, since it involves the degree of inherent parallelism of the physical system. Which implementation is best for a particular simulation model depends on the relative costs of synchronization and the beneficial effects of load balancing. Therefore, corresponding cost and effectiveness measures, depending on the inherent parallelism of the application system and the degree to which the simulation system is application-allocation-bound, could be very helpful in making the right choice. An interesting approach to making a decision on whether to distribute the execution of a simulation is discussed in [11]; it is based on a well chosen quantitative measure of the inherent parallelism of the physical system, and could be expanded by including the above mentioned simulation model degree of being application-allocation-bound, but this is beyond the objectives of the present study.

## 3. Design Analysis of Distributed Database Management Systems

We consider the subject of distributed simulation of distributed DBMS performance. In the case of a high degree of site autonomy, i.e., a degree of inherent parallelism high enough to be embedded in the simulation model, we are interested in if the physical system performance would lend itself to DDS/AB.

To comprise the performance of different transaction management mechanisms and the overall functioning of a distributed DBMS with a high degree of site autonomy, we present a technology which applies DDS/AB methods.

## 3.1. Performance Model

A reference architecture of distributed DBMSs. Consider a distributed DBMS consisting of a collection of n sites, $S_{1}$ , $S_{2}$ , ..., $S_{n}$ , connected by a communication network and communicating by sending messages. Each site consists of a computer running either a Transaction Manager (TM) or a Data Manager (DM) or both, and a Communication Manager (CM). The Transaction Manager coordinates the execution of transactions; it is responsible for the concurrency control and query execution control. The Data Manager manages a local database; it provides the transactions with the possibilities to read data from the local database into local workspaces, and vice versa (according to a chosen concurrency control discipline); it also manipulates data in the workspaces. The delivery of messages, transaction control, and site monitoring are functions provided by the Communication Manager; it interconnects TMs and DMs. There is a finite number of transactions issued from the site terminals and run on the overall distributed database. A transaction presents a resource request to TM in the form of a sequence of read (retrieve) and write (update) operations and transmissions of intermediate results between sites. A resource request can be local, i.e., served by the local DM, or can refer to a resource at another site, in which case the transaction is distributed and the local TM is responsible for its distributed performance by communicating with the corresponding DMs. Neither TMs nor DMs intercommunicate.

The architecture of the system model resembles that of SDD-1 [18], and some other distributed DBMS models [23].

Concurrency control and recovery mechanisms. The synchronization of the operations among the sites, to avoid explicit conflicts between concurrent operations, may be performed by such techniques as: 2-phase-locking, timestamps, optimistic methods [5,13]. Consider having chosen the timestamp-mechanism with prewrites, controlling the concurrency of transactions, for the model under description. With this method a unique timestamp is assigned to each transaction at the time of its creation. Each data item carries the timestamps of the last transactions which read and wrote it. When a transaction attempts to read or write a data item, the DM, compares the timestamp of the data item with that of the transaction. We make use of “prewrites”, i.e., the write operations are buffered instead of directly applied to the database, before the transaction commitment. In the case of a read operation, the timestamp of the transaction must be greater than the write timestamp of the data item (otherwise the operation is rejected); and if it is, there must not be a prewrite operation pending on the same data item with smaller timestamps (otherwise the operation is buffered). In a prewrite operation, the timestamp of the transaction must be greater than the read timestamp of the data item and greater than the write timestamp (otherwise it is restarted). In a write operation, the operation is always buffered and it will be executed when all prewrites with smaller timestamps have been executed.

Thus the basic timestamp mechanism ensures the serializability of transactions; however, atomicity of transactions must also be ensured. It is not acceptable that a subtransaction be locally aborted because of a failure and the other subtransactions commit. For allowing a return to normal operation of a distributed system after a failure, different recovery algorithms have been proposed.

Consider the classical 2-phase-commitment protocol being chosen for the model, i.e., there is one process (a TM process in the model), which has a special role for the final commit or abort decision, called the coordinator, and other processes (DM processes in the model), which must commit together and are responsible for performing the write actions at its local database, called participants. The basic idea of the protocol is to determine a unique decision for all participants with respect to committing or aborting all local transactions. If a participant is unable to locally commit, then all participants must locally abort. The first phase of the protocol is reaching a common decision; the second phase is implementation of the decision.

We choose the mentioned mechanisms for the performance model under development, but it is possible to simulate different concurrency control mechanisms, as well as other versions of the two-phase commitment protocol, in a similar way. For instance, the operation of deadlock-resolution protocols or termination protocols (for operational participants) and restart protocols (for failed participants) can be simulated together with the commitment protocol.

Distributed transaction processing model. In the developed model, a centralized computational structure of transaction is considered. The processing model follows the timestamp mechanism with prewrites, to guarantee the serializability of the transactions and two-phase commitment, to make the execution recoverable. The distributed DBMS processes a transaction as follows:

If the operation is a read one, the TM begins the operations for the chosen copy of each logical data item at the various DMs. Each DM applies the timestamp mechanism, and depending on the results sends confirmation or rejection to the corresponding TM, or buffers the request (if prewrites with a smaller timestamp are pending on the same data unit).

If the operation is a prewrite one, it occurs in two stages following the two-phase commitment protocol. During the first stage, new values of data to be updated are stored in a protected workspace within the corresponding DM. The DM applies the timestamp mechanism, and depending on the results buffers the operation or sends a confirmation to the corresponding TM. During the second stage, the TM requests the DMs to transfer data from the protected workspaces to the local databases. In the real system, all the actions are accompanied by writing corresponding log records, which contain the required information for undoing or redoing the actions.

Model parameters. Typical groups of parameters which can be considered in the model are: transaction management parameters (concerned with the concurrency control, recovery mechanisms, and deadlock resolution); and application parameters (average interarrival time of transactions, transaction type, average local processing time, degree of interference, transaction size, maximum number of transactions running concurrently, database size, database content, database organization, average times of database operations, etc.).

## 3.2. The Distributed Simulation Model

In performing a distributed simulation of a distributed DBMS as the described one, we consider each site as a separate process, and tie these processes together as a set of co-operating parallel processes with message passing.

The physical processes inside the sites can be simulated by conventional discrete-event simulation techniques. For the site communication simulation we suggest that a DDS/AB method be applied.

A distributed DBMS can be modelled as a collection of n logical processes, $s_{1}, s_{2}, \ldots, s_{n}$ , running in parallel on the different sites and communicating through messages; each logical process $s_{i}$ , representing a site process $S_{i}$ , is considered consisting of such internal processes as: the input and output interface processes ( $ii_{i}$ and $oi_{i}$ ), responsible for converting the format of the messages from/to a standard format accepted by the network, and for the message time conversion from real to system simulation time; transaction manager process ( $tm_{i}$ ); data manager process ( $dm_{i}$ ); and communication manager process ( $cm_{i}$ ), simulating the functions of the corresponding managers from the reference architecture model; interactive work manager process ( $iwm_{i}$ ), controlling the interaction with the user, or if this interaction is simulated, communicating with transaction generation process ( $tg_{i}$ ) and transaction sink process ( $ts_{i}$ ) (fig. 2). The simulation of these internal processes can be performed by corresponding simulation modules. All of the modules may include statistics collection. Depending on the performance model developed, the requests issued from local terminals, or $tg_{i}$ (or received along channels), and directed to local and/or remote dms, are forwarded by the $iwm_{i}$ and ii (or only by ii) to local $dm_{i}$ or $tm_{i}$ .

As was already mentioned, to demonstrate how the environment described can be simulated, we choose to conform the basic distribution simulation algorithm with null messages for deadlock avoidance.

The scheme for the distributed simulation of distributed DBMSs processing, storage and communication could be presented as a distributed algorithm in the following way: Consider the simulation of the site process $S_{i}$ . At the initialization phase, the corresponding logical process $s_{i}$ inputs the simulation parameters, or creates and activates corotines for interactive work from local terminals. In the main simulation phase, $s_{i}$ prepares for each outgoing channel sequences of messages (at the beginning, null ones), that must be sent when their times come. After that, $s_{i}$ waits to obtain messages along all incoming channels; updates its clock value $T_{i}$ ; accepts a message; advances the simulation of $S_{i}$ up to $T_{i}$ . When the message comes from a coordinator process, $dm_{i}$ applies the timestamp mechanism and simulates rejection or application to the database. If $s_{i}$ is a coordinator process itself, $tm_{i}$ controls the execution of the subtransactions in two-phase commitment mode. When the message comes from $iwm_{i}$ , i.e., from tg process, or from a local terminal, the execution is controlled by $dm_{i}$ or $tm_{i}$ (for local and remote data processings, respectively). At the point when $T_{i}$ changes in value, for each outgoing channel a sequence of messages that $S_{i}$ would have sent is prepared, and the messages are sent at their respective times. When the simulation completion criterion met, a model validation test can be performed and all the results are printed out.

![](/api/attachments/B5GKY32J/fulltext/images/c34b5e7b71c288f950f7cdf1f13f6f03393141e2ad6cdb4a3e16232c0f6e2695.jpg)  
Fig. 2. Distributed DBMS process model.

DDS/AB distributed simulation algorithm for a subsystem process $S_{i}$ is presented (in a pseudocode) in fig. 3 and fig. 4.

To provide an environment of different sets of recovery and concurrency control mechanisms, and even different distributed simulation approaches, the corresponding software modules: data managers, transaction managers and communication managers are to be changed with appropriate ones, preliminary developed and kept in local software libraries. For introducing, in the model, different local application needs and politics, corresponding transaction generation modules must be prepared from the local application experts, or these needs are expressed interactively during the simulation.

It is possible that the internal processes mentioned be represented either by real software modules, which implement the processes, if already available, or by modules, which simulate their activities and gather statistics. This stands for the transaction manager modules and data manager modules, and not for the communication manager modules and the interface modules.

Several groups of decisions tackle the problems of time conversion and synchronization in the simulation system. The synchronization of the times between the site processes is achieved by an allocation-bound distributed algorithm. A set of procedures applied by the interface modules and based on properly devised scaling factors, convert the real time of the message passing, into the model simulation time.

In the environment designed, performance variables as the following ones may be considered: transaction response time, degree of interference, percentage of aborted transactions, queueing situations, etc.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
/* Site process  $S_{i}, i=1,2,\ldots,n$  */
/*  $s_{i}$ , corresponding logical process;  $T_{i}$ , clock value of  $s_{i}$  */
 $T_{i} := 0$ ;
prepare NULL messages to be sent along the output channels;
create and activate corotines for interactive work and/or input local simulation data;
while simulation completion criterion is not met do
begin /* simulation of  $S_{i}$  up to  $T_{i}$  */
    prepare for each outgoing channel a sequence of messages for sending;
    send the messages whose times have come;
/* receive messages and update  $T_{i}$  until it changes value */
 $T_{i}' := T_{i}$ ;
    while  $T_{i}' = T_{i}$  do
    begin
    wait to receive messages along all incoming channels into  $s_{i}$  buffers;
    update  $T_{i}$ , the minimum over all incoming channel clock values;
    upon accepting of a message, add it to the list of events;
/* in accordance with the kind of messages,  $dm_{i}$ ,  $tm_{i}$ ,  $cm_{i}$ , iwm; perform the necessary simulations */
• • •
    end
end
consider the model validation;
output the simulation results;
</div>

Fig. 3. DDS/AB algorithm for a site process $S_{i}$ .

/\* s; plays "participant" in the basic 2PC protocol \*/
if the message is READ then
    dm; applies the timestamp mechanism with prewrites and READY or ABORT messages are prepared to be sent, or the request is simulated buffered in dm; until the timestamp conditions allow READY message to be prepared to be sent in reply;
else if the message is PREPARE then
    dm; applies the timestamp mechanism with prewrites and according to the result the request is simulated rejected (ABORT message is prepared to be sent and writing "abort" record in the log is simulated), or buffered (READY message is prepared to be sent and writing subtransaction and ready records in the log are simulated);
else if the message is COMMIT command then
    dm; converts the buffered prewrite operation into a write operation, and application to the database is simulated (ACKNOWLEDGE message is prepared to be sent back), or the operation is kept on simulating buffered until the timestamp condition sets in and ACKNOWLEDGE message may be prepared to be sent, then writing "commit" record in the log is simulated;
else if the message is ABORT command then
    dm; simulates clearing up the buffer space from the corresponding operation and ACKNOWLEDGE message is prepared to be sent, next writing "abort" record in the log is simulated;
/\* si plays "coordinator" in the basic 2PC protocol \*/
else if the message is ABORT, or the coordinator's timeout expired then
    tm; asks ABORT command message to be prepared to be sent along all the participants' channels, next writing "global\_abort" record in the log is simulated;
else if the message is READY then
    according to the responses of the rest participants, tm; asks ABORT or COMMIT command messages to be prepared to be sent along the participants channels, next writing "global\_commit" record in the log is simulated;
else if the message is ACKNOWLEDGE then
    tm; considers the rest participants' responses and asks that COMPLETE or FAIL\_COMPLETE messages be prepared to be sent to ts, or to corresponding local terminal, writing "complete" record in the log is next simulated;
else if the message is from the tg, or local terminal then
    it is sent first to iwm, and then, either to tm, which asks PREPARE message to be formed to be sent along the participants' channels or to dm, which simulates the indicated local database processings;
else /\* the message is a NULL one \*/

Fig. 4. DDS/AB algorithm (part) when basic 2 PC protocol and basic timestamp mechanism chosen in $S_{t}$ .

## 3.3. Deadlock Considerations

The distributed simulation technique chosen to be embedded into the distributed simulation algorithm must be deadlock-free.

Nevertheless, deadlocks may occur, because of deadlocks in the simulated transaction management techniques. Usually, a specific deadlock-resolution technique accompanies the transaction management, and if so, it could be easily embedded into the simulation model in the form of another internal logical process, a deadlock manager process.

As far as the performance of not only deadlock-free mechanisms should have to be evaluated at times, the distributed simulation mechanism must be supplied with an additional deadlock resolution component, for instance a time-out mechanism.

## 4. Advantages and Drawbacks of the Approach

The described approach, presented by a distributed simulation model, makes the evaluation of distributed DBMS performance possible. It can be conformed to the distributed simulation of some other loosely coupled distributed systems [21,22]. On the principle of keeping problems of transaction management distinct, the approach permits performance measurement of different transaction management techniques together with the corresponding functioning and utilization of dynamic and static components. It can help different stages of the design analysis to be simultaneously considered (no other approach can provide such a possibility). For instance, by assigning to the transaction management process, $tm$ , such functions as query translation, access planning, etc., the range of model parameters could significantly be extended. The approach is not strictly bound to the distributed simulation method applied. Besides, the performance of different distributed simulation methods could be evaluated and compared in the same environment.

Notice, however, that the great amount of control messages raises the cost of the simulation, despite the convenience of having this amount evaluated. In such cases, one can use DDS/AF type of simulation. If the degree of “speedup” of simulation is important, DDS/AF type will also be more appropriate, because of the potentially faster execution of DDS/AF approaches. Unfortunately, we do not present corresponding technology considerations of DDS/AF type of simulation concerning the distributed DBMS design analysis.

In connection with the observations made, we advocate two particular approaches to the design analysis of distributed database systems with loosely coupled sites: (1) each component system connected with a computer site to be described by an expert on the local application, who has sufficiently precise knowledge of the application requirements, if necessary he can perform conventional simulation experiments; the expert, provides the distributed simulation with data such as: the frequency of the activation of the applications, the number, type, and the statistical distribution of accesses, made by each application to each required data object, and so forth, in the beginning of each simulation session; (2) the experts participate in the distributed simulation sessions interactively. In both cases, the interaction between the local experts (designers) on structure and numerical parameters improvement could be performed in the form of participant-concept reports, exchanged before and after the simulation sessions. Environment of a computer conferencing system with interactive tools could be especially useful in both cases.

![](/api/attachments/B5GKY32J/fulltext/images/f6a4eb73c51194a44cb20080fdbae51a65198419040709972f061b7fd6257566.jpg)  
Fig. 5. A site process performing four requests from time 15 to 35.

## 5. An Example

As an example of the distributed simulation approach to the design analysis of distributed DBMSs, a site process, simulating the performance of three global requests (i.e. issued from other sites) and one from a local interactive work manager (i.e., from the local transaction generation process, or from a local terminal) is considered (see fig. 5. and 6.). The requests are as follows: along the first channel, a request for a read operation; along the second – for a write operation (from a coordinator site); along the third – a message “abort” (from a participant site); and from the interactive work manager – a request for a read operation.

We use the 3-tuple $(t, m(x), tms)$ to denote that at time t a message with content m is sent; x is the data item involved; tms is the timestamp value generated for read (R) and write (W) operations for comparing with the timestamps (RTM and WTM) of the data items in the local databases. The clock value of the site, T, is initially 15; whenever a message is received, its value is updated. The simulation of the process is advanced to the new value. The site process obtains for the outgoing channels sequences of messages that the site simulated would have sent. They are kept in buffers, until the corresponding events are able to occur.

<table><tr><td>inputinterface(ii)(1 unit)</td><td>transactionmanager(lm)(2 units)</td><td>datamanager(dm)(3 units)</td><td>outputinterface(oi)</td></tr><tr><td>(15,R(x1),120)</td><td></td><td>(16,R(x1),120)</td><td>(19,data(x1))</td></tr><tr><td>(16,abort)</td><td>(17,abort)</td><td></td><td>(19,ABORT)</td></tr><tr><td>-</td><td></td><td></td><td></td></tr><tr><td>(29,R(x2),240)</td><td></td><td>(30,R(x2),240)</td><td>(33,data(x2))</td></tr><tr><td>(35,W(x1),115)</td><td></td><td>(36,W(x1),115)</td><td>(39,abort)</td></tr></table>

<table><tr><td>buffer</td><td>interactive work manager(iwm)(1 unit)</td><td>network</td><td>terminals or sink</td></tr><tr><td>(19,data(x1));A1</td><td></td><td>(A1*28,data(x1))</td><td></td></tr><tr><td>(19,ABORT);A3</td><td></td><td>(A3*28,ABORT)</td><td></td></tr><tr><td></td><td>(28,R(x2),240))</td><td></td><td></td></tr><tr><td>(33,data(x2));Ak</td><td>(35,data(x2));Ak</td><td></td><td>(Ak*36,data(x2))</td></tr><tr><td>(39,abort);A2</td><td></td><td>-</td><td></td></tr></table>

Fig. 6. Message transmission in the simulation of the example.

When the request (28, $\mathrm{R}(x_{2})$ , 240) is accepted and T becomes 28, the already buffered results will be sent, i.e., abort command ( $A_{3} \times 28$ , ABORT) along the third line (and along the rest lines leading to the “participants”); and ( $A_{1} \times 28$ , data( $x_{1}$ )) along the first line. The times are changed by corresponding scaling factors A. When the request (35, $\mathrm{W}(x_{1})$ , 115) is accepted and T becomes 35, the buffered command (33, data( $x_{2}$ )) will be sent as ((35, data( $x_{2}$ )); $A_{k}$ ) to the interactive work manager and after that to the corresponding terminal as ( $A_{k} \times 36$ , data( $x_{2}$ ))). The message ( $A_{2} \times 39$ , abort), will be sent along the second channel, when T becomes great enough for this.

## 6. Conclusions

We have suggested a development of the Peacock taxonomy with a new type of distinction of the methods on the level of performance. The AB (allocation-bound) type of simulation introduced has been applied to the design analysis of distributed database systems with an inherent parallelism high enough to be transferred to the simulation system. Performance and simulation models have been developed, as well as a distributed simulation algorithm, obtained by conformation of an existing AB simulation method. The same approach holds well if other deadlock free AB methods are embedded. It has been shown, for the purposes of distributed DBMS performance evaluation, how recovery and concurrency control techniques could be modelled together in a distributed environment, capturing the processing, storage, and communication resources of the whole system. Other transaction management mechanisms, as well as different local simulation conditions, can be embedded only by replacing process modules with new ones from the local software libraries and by describing corresponding transaction generation process modules (or simulate the environment interactively by terminals).

We do not consider the alternative approach, DDS/AF, in our study; this approach is far more often experimented with and discussed in the literature than the DDS/AB oriented methods; we only suppose that it is more appropriate for distributed systems with a negligible parallelism, such as distributed DBMSs with a small site autonomy. For the purpose of completeness, we plan to continue our study in direction of the potentiality of DDS/AF methods and their application to distributed DBMSs with a low site autonomy, and to regulate DDS/AB and DDS/AF application by a cost-effective analysis, based on quantitative measures for the inherent parallelism and the degree to which the simulation model is application-allocation bound.

The observations given in the paper can have practical importance in developing adequate tools in the performance measurement of different types of distributed applications [21]. Interesting results could be obtained by similar means, if different types of interconnections (communication interfaces) between the local subsystems of a complex distributed system are simultaneously considered in a reference model and simulated only by message communication [22].

## 7. Acknowledgements

The author thanks Ms. Erzsebet Csuhaj-Varju, Computer and Automation Institute, Hungarian Academy of Sciences, and Professor Dr. Ralph C. Huntsinger, California State University, Chico for their valuable consultations at different stages of the development of the work.

## References

[1] P. Bernstein, N. Goodman, V. Hadzilacos, Recovery Algorithms for Data Base Systems, in: R. Mason, Ed., Proc. of IFIP Conference, Paris (North-Holland Publ. Comp., Amsterdam, 1983) 799–807.

[2] J. Bezivin, Some Experiments in Object-Oriented Simulation, in: Proc. of OOPSLA'87 (North-Holland Publ. Comp., Amsterdam, 1987; ISDN: 0-897-91247-0) 394–405.

[3] O.H. Bray, Distributed Database Management Systems, Lexington Books (1982).

[4] R.E. Bryant, Simulation of Packet Communication Architecture Computer System, Technical Report MIT/LCS/TR-188, Massachusetts Tech, Cambridge, MA (Nov., 1977).

[5] S. Ceri, G. Pelagatti. Distributed Databases: Principles and Systems, (McGraw-Hill Book Company, 1984; ISBN: 0-07-010829-3).

[6] K.M. Chandy, V. Holmes; and J. Misra. Distributed Simulation of Networks, Computer Networks 3, Nr. 2 (Apr., 1979) 105–113.

[7] K.M. Chandy, J. Misra. Distributed Simulation: A Case Study in Design and Verification of Distributed Programs, IEEE Transactions on Software Engineering SF-5, Mr. 5 (Sep., 1977) 440–452.

[8] H. Garcia-Molina, Performanse Comparison of Two Update Algorithms for Distributed Databases, in: Proc. of the 3-rd Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, CA (1978).

[9] D. Jefferson, Virtual Time, ACM Transactions on Programming Languages and Systems 7, Nr. 3 (1985) 404–425.

[10] W. Lin, Performance Evaluation of Two Concurrency Control Mechanisms in a Distributed Database System, in ACM-SIGMOD International Conference on Management of Data, Ann Arbor, MI (1981).

[11] M. Livny, A Study of Methodology of Parallelism in Distributed Simulation, in: P. Reynolds, Ed., Distributed Simulation (Simulation Council, La Jolla, CA, 1985; ISDN: 0-735927-6) 94–98.

[12] J. Misra, Distributed Discrete-Event Simulation, Computing Surveys 18, Nr. 1 (Mar., 1986) 39–65.

[13] C. Papadimitriou, The Theory of Database Concurrency Control, Computer Science Press, Rockville, MD (1987).

[14] J.K. Peacock, J.W. Wong; and E. Manning. Distributed

Simulation Using a Network of Processors, Computer Network 3, Nr. 1 (Feb., 1973) 44–56.

[15] J. Peacock, E. Manning; J. Wong, Synchronization of Distributed Simulation Using Broadcast Algorithms. Computer Network 4, Nr. 2 (Apr, 1980) 3–10.

[16] A.D. Reed, A.D. Malony, An Evaluation Environment for Concurrent Object-Oriented Simulation, in: B. Unger and D. Jefferson, Eds., Proc. of the 1988 Distributed Simulation Conference (SCS, CA, 1988; ISBN: 0-911801-29-4) 149–153.

[17] D.R. Ries, The Effect of Concurrency Control in the Performance of a Distributed Management System, in: Proc. of 4-th Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, CA (1979).

[18] J.B. Rothnie, P.A. Bernstein, S. Fox, N. Goodman, M. Hammer, T.A. Landers, C. Reeve, D.W. Shipman and E. Wong. HSDD-1: A System for Distributed Databases, ACM TODS 5, Nr. 1, (1987) 1–17.

[19] K. Sevcik, Comparison of concurrency control methods using analytic models, in: R. Mason, Ed., Proc. of IFIP Conference, Paris (North-Holland Publ. Comp., Amsterdam, 1983) 847–857.

[20] E.K. Stancheva, Distributed Discrete Event Simulation to

Design Analysis of Distributed Database Systems, in: J. Clema, Ed., Proc. of the 1989 Summer Computer Simulation Conference (The Society for Computer Simulation (SCS), Austin, TX, 1989; ISBN: 0-911801-58-x) 477–482.

[21] E.K. Stancheva, J.K. Pavlov, “Computer Network Integrated Manufacturing: Performance Evaluation using Distributed Simulation.” in: Proc. of Advanced Information Processing in Automatic Control Conference, IFAC/IFORS/IMACS/IEEE, Nancy, France, (July, 1989) 84–89.

[22] E.K. Stancheva, R.C. Huntsinger, Allocation-Bound Distributed Simulation of Composite Distributed Systems, in: Proc. of the 1990 Summer Computer Simulation Conference, (The Society For Computer Simulation (SCS), Calgary, Canada, 1990)

[23] C. Thanos, E. Bertino and C. Carlesi, The Effects of Two-Phase Locking on the Performance of a Distributed Database Management System, Performance Evaluation Journal 8 (1988) 129–157.

[24] D. Wyatt and S. Sheppard, A Language-Directed Distributed Discrete Simulation System, in: S. Sheppard and Pegden, Eds., Proc. of the 1984 Winter Simulation Conference (The Society for Computer Simulation (SCS), San Diego, CA, 1984) 463–464.
