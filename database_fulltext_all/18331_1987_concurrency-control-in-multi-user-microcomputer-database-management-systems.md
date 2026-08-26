---
otero_id: 18331
otero_key: "MZNU48P8"
title: "Concurrency control in multi-user microcomputer database management systems"
authors: "Jan L. Harrington"
year: "1987"
journal: "Information & Management"
doi: "10.1016/0378-7206(87)90046-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Concurrency Control in Multi-user Microcomputer Database Management Systems

Jan L. Harrington, Ph.D.

Bentley College, Department of Computer Information Systems, Beaver and Forest Streets, Waltham, MA 02154, U.S.A.

The past few years have seen a dramatic increase in the business use of centralized multi-user microcomputer DBMSS without a concomitant attention to the concurrency control mechanisms employed by those DBMSS to ensure the integrity of the data they manage. This paper examines the state-of-the-art, examines the types of work done previously on the performance of DBMS concurrency control, and proposes independent measures to be used in an empirical study to evaluate the efficiency and effectiveness of multi-user microcomputer DBMS concurrency control.

Keywords: Database management systems, Microcomputer database management, Concurrency control, Concurrency control performance, Database concurrency control, Microcomputer concurrency control, Locking, Locking performance.

## 1. Introduction

Over the past three years, a substantial number of corporate data management applications have migrated from mainframe and minicomputers to networked microcomputers. Like database management systems (DBMS) that run on larger machines, the multi-user microcomputer systems must, in some way, manage the problems that arise when more than one user interacts with a single database at the same time (concurrent use). The techniques for handling such use are known as concurrency control. Although valuable corporate data are being stored and managed with multi-user

![](/api/attachments/MZNU48P8/fulltext/images/e9069041fc6e11438069449122944a3b7998594fe3209e2f391af2d3d33d0298.jpg)

In addition to her work with DBMS concurrency control, Dr. Harrington is also engaged in a longitudinal study monitoring changes in the computer background with which freshmen enter college. Reports of the study (now in its fourth year) have been presented in a variety of forums, including the 1988 SIGSCE Conference in Atlanta, GA.

Dr. Harrington is the author of Relational Database Management for Microcomputers: Design and Implementation (Holt, Rinehart & Winston, 1988), a text book aimed at upper-division undergraduate students who are taking theoretically rigorous database management courses using microcomputers. She has also completed Database Management with Double Helix II for the Macintosh and VAX (Brady Books, 1988) for the trade market.

microcomputer DBMss, there has been no research reported in the literature that examines the efficiency and effectiveness of concurrency control as implemented in microcomputer software.

The purpose of this paper is to determine:

1. the concurrency control schemes used in some major multi-user DBMSS;

2. previous work in the evaluation of concurrency control performance; and

3. independent measures for an empirical study of concurrency control performance.

## 2. Underlying Concepts and Terminology

A database is a collection of data viewed as a logical whole. It may be located in a single place (centralized) or scattered across many systems (distributed). Concurrency control for distributed databases presents different demands than that for centralized databases and is beyond the scope of this paper.

A multi-user DBMS is one that can be used by more than one user at any given time. In a microcomputer environment, remote users gain access to a centralized database over a local area network (LAN). Activities against multi-user DMBSs are generally grouped into transactions. A transaction is a single unit of work presented to the DBMS. It may be limited to a single action (e.g. adding one record) or it may be an entire application program. Transactions end in one of two ways. If they end in an expected manner, then they are committed (all changes by the transaction are made permanent). If they end in an unexpected or undesirable manner, they are aborted and then possibly rolled back (all changes made by the transaction are undone and the database is restored to its state before the transaction began). In mainframe and minicomputer DBMss, rollback is usually performed by retrieving copies of the previous state of the database and details of changes made by a transaction from a log or audit trail consisting of a before-image file. Microcomputer DBMss, however, use a variety of techniques for transaction recovery, some of which require that the roll back be written into an application program.

Concurrent use of a database typically presents two types of problems:

1. Lost updates: These occur when a transaction eliminates an update made by a previous transaction before the previous transaction has been completed.

2. Deadlock: This is the result of attempts to control lost updates. Two transactions are deadlocked when they are blocked from gaining access to needed resources because each has control of a data object the other needs.

Ideally, concurrency control mechanisms should prevent lost updates and handle deadlock in some way (e.g. by either preventing it from occurring or detecting it and breaking it when it does occur).

There are three major concurrency control schemes used in DBMSS:

1. Optimistic: Concurrent transactions are allowed to run to completion, making updates in working storage instead of the database. When a transaction ends, the DBMS decides to allow it to commit if it will not interfere with another transaction. Transactions which interfere are not allowed to commit but instead are rolled back and then restarted.

2. Timestamping: Each time a transaction retrieves a data object, the transaction is timestamped. A transaction is not allowed to perform an update if another concurrently executing transaction has an earlier timestamp on the data object in question. This method is used most frequently in distributed database systems.

4. Locking: Transactions may obtain exclusive use of a portion of the database, preventing concurrently executing transactions from updating or retrieving locked data items. In some implementations, transactions may also obtain shared use of a portion of the database, preventing updates but allowing retrieval by concurrently executing transactions. (For an in-depth discussion of these concurrency control schemes and how they are used, see [2].)

Locking is the concurrency control method most commonly used for microcomputer DBMSS. Many DBMSS use some variation of Two Phase Locking (2PL). With 2PL, a transaction obtains locks on a data object as they are retrieved. Locks are held until the transaction either commits or is rolled back.

If the transaction has obtained an exclusive lock (also known as a write lock), no other transaction can obtain a lock on that object; the transaction has the exclusive right to view and/or update the data object. A transaction will be blocked if it attempts to obtain a lock on a data object on which an exclusive lock already exists. The lock request will be refused. The next operation varies from one DBMS to another. Some place transactions in an involuntary wait state, where they remain until either the lock on the data object is released or something else happens to abort the wait; others simply return a message to the user that the lock request was unsuccessful, in which case the user might either enter a voluntary wait state and continue to retry the lock request or abort the entire transaction.

If a transaction has obtained a shared, or read, lock, other transactions may also obtain shared locks but no transaction can obtain an exclusive lock; shared locks prevent updating but allow multiple transactions to view data. Transactions attempting to place exclusive locks on data objects held by shared locks will be blocked, while transactions attempting to place additional shared locks will succeed.

The size of the data that can be locked (e.g. table or record) is known as the granularity of the lock and varies from one DBMS to another. Regardless of the granularity, a lock may be placed either implicitly or explicitly. Implicit locks are those placed on a data object by the DBMS without direct user instructions. Explicit locks are placed in response to lock requests issued by a user. In either case, the user may be someone working interactively with a query language or an application program.

## 3. Some Microcomputer Concurrency Control Schemes

Six widely-used multi-user microcomputer relational DBMSS (Oracle, Informix-SQL, R:base System V, dBase III Plus, Revelation, and Progress) were examined to learn the details of their mechanisms for concurrency control. The first five were investigated in their MS-DOS implementations. Progress, however, will run under MS-DOS only in a single-user mode, and thus observations apply to its Unix implementation. All six DBMSS use some form of locking; they differ in the types and granularity of the locks, the agent that places the locks (e.g. application program, interactive command, or DBMS), and their ability to manage deadlock.

## 3.1. Revelation

Revelation [3] uses two dimensional tables termed files; rows are known as as rows. Revelation has no concept of a transaction. For concurrency control, it uses semaphore locks, similar in function to exclusive locks. They are placed on individual rows within a file. Once a user holds a semaphore lock, no other user can view or modify the row until the lock is released. Commands that affect the database structure (e.g. BUD, the database builder utility) or entire files (e.g. ENTER) obtain row locks as needed. These are released when the command terminates.

Application programs can place row locks explicitly with the LOCK command. Locks are not released automatically, however, when an application program terminates; they must be released explicitly with an UNLOCK command. The LOCK command returns a Boolean result to the application program reflecting the success of the locking attempt. If a lock cannot be placed, a program can either try to place the lock again (i.e. use an application program to enter a voluntary wait state) or abort the entire operation. Revelation does not place programs whose lock requests are unsuccessful in an involuntary wait state.

Deadlock can occur if concurrently executing programs continue unsuccessfully to try to obtain locks while retaining any locks they already hold. Revelation, however, has no provisions for detecting or breaking deadlock; its control must therefore be provided from within the application program. This generally takes the form of a counter within the program loop that retries a LOCK command. An attempt to place a lock is aborted if the counter reaches some arbitrary value, removing the program from the voluntary wait state it had entered when it was in the loop.

Revelation does no before-imaging. If a time-out is programmed into an application program, it is possible that a time-out will occur when some of the commands in the program have been completed and others not. It is then the responsibility of the program to manage rollback (i.e. explicitly undo every update it has made prior to the point when the time-out occurred).

## 3.2. dBase III Plus

dBase III Plus [1] is the most widely used microcomputer DBMS. It refers to tables as files and rows within those tables as records. Like Revelation, it has no concept of a transaction. It does, however, support both implicit and explicit file and record locking. Individual files within a dBase III Plus database may be used in shared or exclusive mode. An exclusive lock on a file (i.e. using the file in exclusive mode) can be obtained only if no other user has a lock on that file. Files used in shared mode are accessible by multiple users. Commands which open a file (e.g. USE), modify data (e.g. APPEND, BROWSE, UPDATE), or modify the structure of a file (e.g. CREATE, INDEX, JOIN TO, MODIFY COMMAND) automatically place the file in exclusive mode, implicitly placing an exclusive lock on the file. A few commands, in particular those which are limited to data retrieval (e.g. QUERY, REPORT FORM), default to shared mode.

While most commands default to exclusive mode, it can be overridden with a SET EXCLUSIVE OFF command. All files opened after that point will be opened in shared mode. In that case, explicit record and/or file locking will be needed to manage concurrent updates. Explicit file locks are placed with the command FLOCK(). This attempts to obtain the requested lock and returns a Boolean result based on its success. Explicit file locks can be placed from within an application program or with the DBMS's query language. Record locking is appropriate if an application program is processing single rows in a database file. Explicit record locks are placed with either the RLOCK() or LOCK() commands. Both work in the same way as FLOCK(), attempting to place the lock and returning a Boolean result. Implicit locks placed by commands such as APPEND or BROWSE are held only until that command terminates. Explicit locks, however, are held until the user or application program issues an UNLOCK command.

Like Revelation, dBase III Plus provides no deadlock detection or handling. If concurrent application programs contain loops which idle until FLOCK(), RLOCK() or LOCK() returns a value of true (i.e. the program places itself in an involuntary wait state when an attempt to obtain a lock fails), then deadlock can occur. Deadlock can also occur if an application program contains a RETRY command to execute a subprogram containing locking statements repeatedly until the subprogram succeeds. Deadlock must be broken explicitly, generally by coding a timer into the loop.

Since there is no before-imaging, application programs are also responsible for handling rollback.

## 3.3. R: base System V

R: base System V [7] refers to relations as tables. Though it has no concept of a transaction, it does have two features which address the problems of concurrent use. The first, termed “concurrency control”, is a mechanism that notifies users than an update they are about to perform will cause a lost update. There is no way to actually prevent the lost update (i.e. the user whose action would cause the lost update has the option to proceed).

The second feature which addresses the problems of concurrent use is locking. All locks are exclusive and can be placed either on tables or the entire database. Database locks are implicit. They are placed by the DBMS whenever a user issues a command that changes the database structure (e.g. the command modifies the definition of the columns which make up a table). Table locks are placed implicitly by those commands that update tables, but can also be placed explicitly by a user or an application program. Implicit locks are retained only for the duration of the command that placed them (i.e. an R:base transaction is limited to a single command). However, an application program can create the effect of larger transactions by using explicit table locks.

If a lock request cannot be satisfied, the user or application program issuing the request is placed in an involuntary wait state. R:base automatically continues to attempt to obtain the lock, but there is no list of which transactions are waiting for others. However, the DBMS breaks deadlock by limiting the amount of time a transaction can wait for a lock. The default wait time is about 4 seconds but this can be modified by the user or an application program.

Like Revelation, R: base does no before imaging. If a transaction is limited to a single command, then a time-out causes no harm. However, if an application program is used to extend the scope of a transaction, then in the event of a time-out, the program must manage its own rollback.

## 3.4. Progress

Progress [4] refers to tables as files and rows as rows; it is a DBMS that requires application programs to store and retrieve data. All programs have one or more transactions. Transaction boundaries are indicated in one of two ways. By default, blocks of code within programs that directly update the database are defined as complete transactions. Blocks are defined by looping constructs (e.g. FOR EACH blocks, REPEAT blocks) and by procedures that contain no looping. Each execution of a procedure without a loop or each iteration of a loop is a single transaction. The size of a transaction can be controlled explicitly, however, through use of the keyword TRANSACTION in looping statements or DO TRANSACTION at the beginning of a block that should constitute a single transaction.

Though Progress' documentation makes no mention of a before-image file, the DBMS would appear to be performing some transaction logging. If a transaction whose boundary has been marked implicitly (i.e. by Progress) fails, the DBMS will undo it. Transactions whose boundaries are marked explicitly can be undone by indicating (in an application program) that the DBMS should UNDO it if an error occurs. The application program need not provide undo code; thus the DBMS must be retaining a before-image.

In its multi-user implementation, Progress provides row locking. It will give a transaction a shared lock on a row whenever a row is retrieved or an exclusive lock whenever a row is updated. An application program can, however, override this locking and obtain an exclusive lock when a record is retrieved by appending EXCLUSIVE-LOCK to a retrieval command. All locks are held at least until the end of the transaction.

If a lock cannot be placed, Progress places the program in an involuntary wait state and returns a message to the user, who can continue to wait while DBMS repeatedly tries to obtain the lock or can abort the transaction by pressing the appropriate keyboard key. If the user aborts, Progress automatically rolls back the transaction. Note, the user must intervene to break a wait state, regardless of the type of application program (even in batch processing applications).

There is no deadlock prevention, detection, or resolution. In other words, the DBMS has no facility for detecting which concurrently executing program is waiting for rows locked by any other program or for breaking a deadlock when one occurs. Deadlocks therefore are broken only when a user explicitly aborts the transaction.

## 3.5. Oracle and Informix-SQL

Oracle [10] and Informix-SQL[11] are very similar in their terminology (tables are called tables and rows, rows) and concurrency control. Both use transactions and 2PL to manage concurrency control: locks are obtained as a transaction accesses data objects and all locks are held until the transaction finishes. Within an application program, Oracle transactions begin immediately after the end of a previous transaction; Informix-SQL transactions are started explicitly with a BEGIN WORK statement. Transactions end with either COMMIT WORK or ROLLBACK WORK. If neither COMMIT WORK nor ROLLBACK WORK statements appear in an application program, Oracle and Informix-SQL assume that the entire program is one transaction. When a user works from the SQL command interface, transactions are automatically defined to be a single command.

Both DBMss support table and row locks. There are, however, subtle differences in the agents that place the locks and the available locking. Both DBMss support shared locks (many users may retrieve data but none may update) and exclusive locks (only one transaction can view and/or update) which can be placed on either entire tables or rows within a table. Oracle also supports a shared update lock (an exclusive lock on rows within a table for a given transaction) which permits other users to obtain shared update locks on rows not locked by that transaction.

Informix-SQL table locks, regardless of whether they are shared or exclusive, can only be placed explicitly (i.e. a user or an application program must issue a command to place the lock). Oracle users can also place shared or exclusive table locks explicitly, but the DBMS itself will also implicitly lock an entire table whenever an UPDATE, INSERT, or DELETE command is issued.

Row locks are placed implicitly by both DBMSS. To obtain an Oracle row lock, an application program first explicitly locks the table in shared update mode and then opens a cursor as a row pointer. Thereafter, Oracle implicitly places a lock on each row to which the cursor points during the course of the transaction. Informix-SQL row locks are placed on groups of rows by UPDATE, INSERT, and DELETE commands. Locks on individual rows are placed as rows are retrieved in Informix-SQL's Update mode.

Table 1  
Summary of locking features of six multi-user microcomputer DBMSS

<table><tr><td></td><td>Granularity</td><td>Deadlock control in DBMS</td><td>Transaction control</td></tr><tr><td>Revelation</td><td>Row $^{1}$ </td><td>none</td><td>No concept of a transaction</td></tr><tr><td>dBase III Plus</td><td>Table $^{2}$ , Row $^{1,2}$ </td><td>none</td><td>No concept of a transaction</td></tr><tr><td>R : Base System V</td><td>Database $^{1}$ , Table $^{1,2}$ </td><td>time-out</td><td>No concept of a transaction</td></tr><tr><td>Progress</td><td>Row $^{1,2}$ </td><td>none $^{3}$ </td><td>Transactions with logging and rollback</td></tr><tr><td>Informix-SQL</td><td>Table $^{1,2}$ , Row $^{1}$ </td><td>detect &amp; break</td><td>Transactions with logging and rollback</td></tr><tr><td>Oracle</td><td>Table $^{1,2}$ , Row $^{2}$ </td><td>detect &amp; break</td><td>Transactions with logging and rollback</td></tr></table>

$^{1}$ Lock is explicit (placed by an application program or with the query language).  
$^{2}$ Lock is implicit (placed by the DBMS without user invention).  
$^{3}$ User is notified that a wait state exists; user must press key to explicitly terminate the wait.

By default, Oracle and Informix-SQL place transactions for which a lock request could not be satisfied into an involuntary wait state. Deadlock is detected by looking for a cycle in the transaction waiting list and is then broken by rolling back the youngest transaction (the one that has been executing the shortest time). Alternatively, users and application programs can request that transactions not be placed in a wait state, in which cause an unsatisfied lock request returns a message to that effect to the transaction.

The concurrency control features provided by these six DBMss are summarized in Table 1.

## 4. Previous Work in Locking Performance

Before attempting any empirical study of the performance of microcomputer DBMS concurrency control, it is important to look at previous work in the evaluation of concurrency control. This can give clues about behavior of the microcomputer DBMSSs and also help identify quantitative measures that might be adapted to the microcomputer environment. Because locking is the major method in microcomputer DBMS concurrency control, this investigation focused on its performance only, ignoring both the optimistic and timestamping methods.

Locking performance studies fall into two broad categories: simulations and mathematical models (analytical studies). Since there is a rather large body of work on locking performance, what follows is a discussion of some representative studies.

## 4.1. Simulation Studies

On of the earliest concurrency control simulation studies was reported by Munz & Krenz [9].

Using an IBM 370, they simulated the performance of a locking scheme that placed transactions in a wait state whenever a lock request could not be granted. Deadlock was allowed to occur, detected, and then broken. (This is the scheme used by Oracle and Informix-SQL.) Typical simulation runs involved 50 concurrent batch processes, each performing updates, and a database containing 100,000 lockable data objects. Their experimental measures included the total time that transactions spent waiting for locks, total CPU time, the number of deadlocks, and the average number of transactions involved in a deadlock. The bulk of Munz & Krenz's findings deals with the changes in parameters as the size of the database increased. For example, they discovered that, assuming a constant number of active transactions, the frequency of deadlocks increased until the size of the database became something greater than 100 lockable data objects, at which point it dropped off quickly and became very small as the database grew beyond 10,000 objects. This result is not surprising, since a larger database presents a larger pool of resources for which transactions can contend, reducing the amount of contention for any single data object.

Morris and Wong [8] used mathematical models to investigate transaction throughput (the number of transactions completed per unit time) with both locking and optimistic concurrency control. Their locking scheme assumed that transactions obtained all locks before beginning execution: a transaction had to indicate all data objects it might update. Since a transaction could not begin execution unless it held all required locks, deadlock could not occur. This pre-declaration type of locking is not used in any of the DBMSS surveyed here.

Morris and Wong discovered that, with their particular locking scheme, there was a greater transaction throughput than with the optimistic method. They did, however, realize that the pre-declaration type of locking was a somewhat simplistic scheme, that the model did not account for the overhead of the concurrency control mechanism, and that their results applied only to heavy transaction loads.

## 4.2. Analytical Studies

Shum and Spirakis [12] developed a mathematical model to investigate the rates of conflict (attempts to place exclusive locks on data objects already locked by another transaction) and deadlocks with 2PL. They discovered that the rate at which deadlocks occurred was directly proportional to the number of concurrently active transactions at any given time. The rate at which conflicts occurred was related to the product of the total number of concurrently active transactions and the number of concurrently active free transactions (those not holding any locks). As with other analytical studies, performance estimates were made from quantitative computations without reference to any existing DBMS implementations.

Galler [5] created a mathematical model that could be used to predict the average time a transaction would wait for locks. His locking scheme for centralized databases was similar to that employed by [8]: transactions were required to obtain all locks before beginning execution. In the initial model, a transaction that could not obtain the needed locks entered a wait queue (first in-first out), where it stayed until the locks were available. The modified model forced a transaction that was unable to obtain all required locks to release those it had already been granted and start again. From the average wait time produced by the model, Galler was able to predict transaction throughput and average response time for different levels of concurrent use and different granularities of locks. This study was not related to any particular DBMS or implementation; it was also designed only to predict locking performance under a specific set of circumstances.

Goodman et al's study [6] focused on a mathematical model which evaluated the performance of a locking scheme in which the transactions did not wait for locks. Instead, if a transaction was unable to obtain a lock, it was restarted. (This is similar to the method used in dBase III Plus and R:base System V). Among the measures they considered were the probability of transaction conflict (the probability that a transaction would be denied a lock and therefore be restarted), transaction throughput, and the ratio of the number of transactions aborted to the throughput. After evaluating their locking scheme, assuming constant transaction loads, they concluded that the relationship between the three parameters is linear for small numbers of concurrent transactions. When considering these data it is important to remember that they apply only to a concurrency control scheme where transactions do not wait for locks.

There are three major problems that arise when attempting to apply these modeling and simulation research results to a multi-user microcomputer DBMS. The first is that the studies are too specific to cover the range of techniques used in multi-user microcomputer DBMSS.

Second, while there has indeed been significant research done in evaluating the performance of a variety of locking schemes, those studies give little practical information; although they can predict the relative performance of locking techniques in an idealized, highly controlled setting, they do not measure the performance of actual implementations but are based on hypothetical mainframe environments. They are therefore not of much use in attempting to make a purchase decision.

Finally, the models and simulations can predict relative performance but cannot predict effectiveness. All the studies assume a perfect implementation, with no programming bugs (i.e. the concurrency control code is assumed to perform without error). Anecdotal evidence indicates that this is not the case. Therefore, it is not sufficient to analyze concurrency control methods by running simulations using existing algorithms. Instead, microcomputer DBMS concurrency control must be tested empirically on real networks using real DBMSS.

## 5. Independent Measures for an Empirical Study

The research studies used a number of different statistics to predict locking performance. Those which can be used to evaluate microcomputer DBMSS are:

1. Transaction throughput (the number of transactions completed in a given period of time). If microcomputer DMBss are subject to an identical number of transactions running off an identical database on identical hardware, then a comparative measure of transaction throughput can be obtained. Clearly, the transaction throughput will be affected by other implementation details, but since the purpose of the study is to measure performance within an actual operating environment, these implementation details must be considered as overhead, as is the effect of the locking mechanism itself.

2. Average wait time (the average time a blocked transaction waits before obtaining a requested lock or being rolled back). Depending on the DBMS, wait time is a measure of the level of concurrency and/or the effectiveness of deadlock control. This measures must be evaluated carefully for those DBMSS that permit the user or application program to control the wait time (e.g. R: base System V or dBase III Plus).

3. Ratio of aborted or restarted transactions to transaction throughput. Depending on its implementation of concurrency control, transactions for which a DBMS cannot place a lock or which become deadlocked may be either aborted (suspended without automatic restart) or restarted. The ratio of the number of roll backs and/or restarts is a measure of the level of concurrency and the effectiveness of deadlock control.

A concurrency control mechanism can be considered effective if it prevents the introduction of bad data into a database. This is a very different concept from the quantitative measures of performance, in that it says nothing about the speed with which the system operates or the number of concurrent transactions that the system will support without significant performance degradation; e.g. a locking scheme that hangs transactions in endless deadlock is perfectly effective, since it permits no undesirable data to be written to the database. Assuming that all DBMss in the empirical study start with an identical database, then the comparative effectiveness of the concurrency control can be measured by looking at the amount of incorrect data written to the database during the experimental executions.

## 6. Conclusions and Plans for Continued Research

Although there has been a great deal of research into the performance of various locking schemes, none provides practical information that can be used to evaluate the performance of concurrency control in existing commercial multi-user microcomputer DBMSs. This, however, is of vital importance to organizations placing valuable corporate data on networked microcomputer systems.

Our examination of existing commercial multi-user microcomputer DBMSS revealed that there are several different locking schemes being used. Oracle and Informix-SQL appear to have the most effective ones: they use Two Phase Locking, a before-image file for transaction recovery, and provide deadlock handling. Progress appears to manage its own rollback, but requires user intervention to break deadlock. R:base System V avoids deadlock with a time-out mechanism, but places the burden for transaction rollback on an application program. The remaining two DBMSS (Revelation and dBase III Plus), while providing locking capabilities, require intervention on the part of an application program to detect and/or break deadlock as well as to effect rollback.

Clearly, the performance of those DBMss that require program action for concurrency control will depend on the care with which those programs are written. Nonetheless, if we assume that application programs are written to provide the best possible concurrency control for all the DBMss, then the DBMss can be tested empirically to determine their relative effectiveness and efficiency, using the four independent measures. Data for the first three measures (transaction throughput, average wait time, restart/abort ratio) can be collected by the application programs performing experimental transactions. Data for the fourth (amount of bad data) can be obtained by examining the state of the database after experimental transactions have completed their execution.

## References

[1] Ashton-Tate, Inc. (1986) Using dBase III Plus. Torrence, CA: Ashton-Tate, Inc.

[2] Bernstein, P.A., V. Hadzilacos, N. Goodman (1987) Concurrency Control and Recovery in Database Systems. Reading, MA: Addison-Wesley.

[3] COSMOS, Inc. (1985) Revelation User's Guide. St. Joseph, MI: COSMOS, Inc.

[4] Data Language Corporation (1986) Progress Reference. Billerica, MA: Data Language Corporation.

[5] Galler, Bruce I. (1982) “Concurrency Control Performance Issues”. Technical Report CSRG-147. Computer Systems Research Group, University of Toronto.

[6] Goodman, N., R. Suri, Y.C. Tay (1983) "A Simple Analytic Model for Performance of Exclusive Locking in Database Systems". Proc. 2nd ACM SIGACT-SIGMOD Symp. on Principles of Database Systems. pp. 203–215. Atlanta, GA, March, 1983.

[7] Microrim, Inc. (1986) R: base System V User's Manual. Bellevue, WA: Microrim, Inc.

[8] Morris, R.J.T. and W.S. Wong (1985) “Performance Analysis of Locking and Optimistic Concurrency Control Algorithms”. In Performance Evaluation 5, pp. 105–118. North-Holland Publishing Company.

[9] Munz, R. and G. Krenz (1977) "Concurrency in Database Systems - A Simulation Study". Proc. ACM SIGMOD Int'l Conf. on Management of Data, pp. 111-120. Toronto, August, 1977.

[10] Oracle Corporation (1985) ORACLE Overview and Introduction to SQL. Menlo Park, CA: Oracle Corporation.

[11] Relational Database Systems, Inc. (1986) Informix-SQL Reference Manual. Menlo Park, CA: Relational Database System, Inc.

[12] Shum, Annie W. and Paul G. Spirakis (1981) "Performance Analysis of Concurrency Control Methods in Database Systems". In Performance '81, pp. 1-19. North-Holland Publishing Company.
