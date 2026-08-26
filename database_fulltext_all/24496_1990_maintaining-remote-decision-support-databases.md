---
otero_id: 24496
otero_key: "6EP92EBK"
title: "Maintaining Remote Decision Support Databases"
authors: "George Diehr; Aditya Saharia; David Chao"
year: "1990"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1990.11517892"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Maintaining Remote Decision Support Databases

George Diehr, Aditya Saharia & David Chao

To cite this article: George Diehr, Aditya Saharia & David Chao (1990) Maintaining Remote Decision Support Databases, Journal of Management Information Systems, 7:2, 111-138, DOI: 10.1080/07421222.1990.11517892

To link to this article: http://dx.doi.org/10.1080/07421222.1990.11517892

![](/api/attachments/6EP92EBK/fulltext/images/9637d76ccb8eb280f27492de9022203aa827de10d6c3a4c1b2126a5c27bf7ec4.jpg)

Published online: 21 Dec 2015.

![](/api/attachments/6EP92EBK/fulltext/images/59b099d1fe2c59543b260b03ddaa557ac1800493030cfa6e4464f5b6cdb7f2a9.jpg)

Submit your article to this journal ↗

![](/api/attachments/6EP92EBK/fulltext/images/a7cd816593f738309aca4c7f10aa555856d1e760ba330620e69266d144657a89.jpg)

View related articles ↗

![](/api/attachments/6EP92EBK/fulltext/images/0f8c52b0fa84c47138eca12ce9e8011577d5cb4a69ee79dcfa7be8780162428f.jpg)

Citing articles: 1 View citing articles ↗

# Maintaining Remote Decision Support Databases

GEORGE DIEHR, ADITYA SAHARIA, and DAVID CHAO

GEORGE DIEHR is Professor of Information Systems at California State University–San Marcos. He was previously at the University of Washington. His primary interest is in database management, specifically physical structure and design. He is currently working on single-access hashing schemes. He has published in Communications of the ACM, SIAM: Journal on Scientific and Statistical Computing, and Information Systems Research.

ADITYA N. SAHARIA is Assistant Professor of Information Systems at the University of Washington. He received his Ph.D. in Physics from Carnegie-Mellon University and his M.B.A. from the University of Rochester. His research interests include information economics, distributed databases, and artificial intelligence. His work has appeared in Physics Letters, Physical Review, Nuclear Physics, ACM Transactions on Database Systems, SIAM: Journal on Scientific and Statistical Computing, and Information Systems Research. He is a member of the ACM and TIMS.

DAVID CHAO is Associate Professor of Business Analysis and Computing Systems at San Francisco State University. He received his Ph.D. in Information Systems from the University of Washington. His primary interest is in database management.

ABSTRACT: This research describes and analyzes schemes for managing decision support databases that are extracted from a central database and “downloaded” to personal workstations. Unlike a (true) distributed database system, where updates are propagated to maintain consistency, these remote “snapshots” are updated only periodically (“refreshed”) upon command of the remote workstation user. This approach to data management has many of the same advantages of a distributed database over a centralized database (e.g., reduced communication costs, improved response time for retrievals, and reduction in contention), but it avoids the high overhead for concurrency control associated with updating in a distributed database. The added cost is in reduced data consistency.

The schemes analyzed include full regeneration, the scheme used by System $R^{*}$ , and two new schemes. One new scheme—called modified regeneration—is a variation on simple full regeneration of the snapshot, but transmits only relevant changes to the snapshot. The other new scheme uses a difference table of relevant updates. Algorithm descriptions, models of processing and communication costs, analytical and numerical comparison of performance, and qualitative evaluation are included.

Our conclusions are that the difference-table approach is the most robust scheme; the System $R^{*}$ scheme has lowest cost for only rather limited environments; and the modified-regeneration scheme is attractive due to its simplicity and flexibility. The results and models presented here could be used by a DBMS “refresh optimizer” to determine the best scheme to employ as a function of refresh frequency, update rate, and various processing and communication cost parameters.

KEY WORDS AND PHRASES: decision support systems, distributed databases, database snapshots, consistency in distributed databases.

## 1. Introduction

A CONVENTIONAL DATABASE RECORDS OPERATIONAL DATA about the organization. As various events in the organization take place, the corresponding transactions modify the database on a continual basis. Old data are deleted and new data inserted. Such systems typically allow users access to the current information, reflecting the current state of the organization. However, for some applications, users may require or will tolerate access to an obsolete version of data. For example, Gorry and Scott-Morton [7] suggest that, for many decision activities of a planning nature, the users prefer past aggregate information to current detailed information. Sprague and Carlson [18] and Inmon [9, 10] claim that in decision support systems users may either not prefer, or should not be allowed to use, real-time data. For example, many budget and financial applications call for end-of-period data. Similarly, in production planning or workforce analysis, it may be more convenient to work with static data rather than with a time-varying version.

Adiba and Lindsay [2] proposed supporting such users through “snapshots,” which are read-only copies of a selected portion of the database representing a state of the organization at a fixed point in time. This approach also has the advantage of minimizing contention between transaction processing and decision support queries [11].

Since a snapshot represents a past database state, as transactions updating the database arrive, it will diverge from the snapshot. As this divergence increases, the cost to the user for working with stale data will increase. At some point this cost will exceed acceptable levels and the user will issue a refresh request to bring the snapshot to a state consistent with the current database.

In most decision support systems, the commonly followed scheme for refreshing snapshots is full regeneration. At refresh time, the user submits a query defining the snapshot; the central database management system recreates the snapshot and transmits it to the user's workstation, replacing the old snapshot. Full regeneration does not take advantage of the fact that, although there may have been numerous updates to the database, only a few entries in the snapshot may need to be updated. The widespread use of full regeneration stems from the fact that it is very simple to use—it does not require any additional data structures or algorithms. In many cases, the snapshot-relevant portion of the database changes only minimally between refreshes. For such cases, it will usually be more economical to perform a differential refresh of the snapshot—that is, only relevant updates are applied to the snapshot to restore it to a consistent state.

Snapshots bear close resemblance to “views” in relational databases. Views differ from snapshots in two ways. First, while a snapshot exists physically, it is commonly considered that a view does not exist in a physical sense—rather, the view is a definition stated in the form of a relational query on base tables. When a query is executed that references a view, the view definition is used to modify the query, creating an equivalent query directly on the base tables. This approach to processing views is called “query modification.” The second difference is that the snapshot is not maintained in a state consistent with the database. Since the view is a definition on the database, any changes to the database are, of course, realized in the view.

Recently, several authors have suggested an alternative approach, called “materialized” views $[3, 14]$ . A materialized view exists physically and is maintained in a state consistent with the database, or is brought to a consistent state whenever the view is referenced. Blakeley and Tompa $[3]$ propose an immediate update scheme in which base-table updates are examined for relevance as they occur. Relevant updates are then applied to the materialized view in real time. Hanson $[8]$ proposes and analyzes both immediate- and deferred-view update schemes. The deferred scheme buffers the relevant updates until a query on the view occurs, at which time the materialized view is updated. The proposed algorithms and analyses demonstrate that, depending on operating characteristics, a materialized-view approach may be more efficient than traditional query modification.

Roussopolous [15] discusses the deferred-view update scheme implemented in ADMS, an experimental DBMS being developed at the University of Maryland. In ADMS, pointers identifying changes to the database are maintained. When a query requesting data from the view occurs, the view is brought to a state consistent with the database using this pointer system. Clearly, the deferred-view update schemes of Roussopolous and Hanson are adaptable to differential snapshot maintenance.

With the widespread availability of personal computers and their powerful and friendly decision support tools, most snapshots will be maintained on a PC. Thus, snapshot refresh involves additional costs for data communication. A differential refresh approach, as opposed to full regeneration, becomes even more attractive because of the potential for substantial reduction in communication costs.

Recently, a number of authors $[12, 14, 16]$ have proposed architectures for differential refresh of remote snapshots. In these schemes, only the changes since the last refresh are transmitted to the remote site. Thus, they provide substantial savings in communication cost over full regeneration, especially if the number of updates to the database between two refreshes is low. These schemes, however, require additional data structures and algorithms to create the refresh messages. To determine the best approach, both the communication costs and the additional CPU and I/O costs associated with these data structures and processes must be considered.

We note that the snapshot approach is quite different from the approach commonly assumed in research on distributed databases. In a distributed database system, the emphasis is on assuring that replicated fragments are consistent with each other $[4]$ . In contrast, with a snapshot the user accepts that his data is “stale” (either because of the application requirements or because of the high cost associated with accessing current data). Thus, the snapshot is, at best, consistent with the database only just after refresh. Additionally, in distributed systems it is assumed that different sites are in constant communication with each other (except for possible node or link failure), whereas with remote snapshots communication must be established only to request and transfer the refresh messages. For these reasons, the algorithms developed to maintain a distributed database are not easily adaptable for remote snapshots.

The research presented here adapts some of the techniques and analyses presented by these authors, but differs in several important ways. While the difference-table scheme uses several of the techniques and data structures of the Roussopolous and Hanson schemes, Roussopolous does not provide any detailed performance measures. While Hanson presents numeric estimates of the costs for refreshing materialized views, he assumes that the materialized views are stored at the central site, and, therefore, communication costs are not incorporated. In addition, the cost analysis of Lindsay et al. [12] deals only with communication costs and does not provide cost expressions. This research is specific to remote snapshots and explicitly includes communication and message generation costs as factors in evaluating the schemes.

The remainder of this paper is organized as follows. Section 2 presents the following differential refresh schemes: modified regeneration, which maintains a copy of the "old" snapshot at the central site and transmits only the difference between the new and old snapshots; the scheme used in System $R^*$ , in which updated base-table records are time-stamped; and a scheme recently proposed by Saharia and Diehr [16], which maintains a difference table of relevant updates.

In section 3, costs for generating and transmitting refresh messages are modeled for these schemes and for the full-regeneration scheme. Using these models, we identify which scheme is “best” as a function of various operating characteristics (e.g., the update rate, frequency of snapshot refresh, and fraction of records qualified for the snapshot). Section 4 suggests extensions, and section 5 is a conclusion.

## 2. Differential Refresh Schemes

THIS SECTION DESCRIBES SEVERAL SCHEMES FOR DIFFERENTIAL REFRESH of remote snapshots. The refresh process is initiated by a user when he perceives that the cost of using stale data has exceeded acceptable levels. Upon receiving a refresh request, the central site generates and transmits the refresh messages to the remote site. Following Lindsay et al. [12], a refresh scheme should meet the following objectives:

(C1) It should assure that the snapshots are consistent with the database just after refresh.

(C2) It should cause minimal interruption of the normal database activities.

(C3) The number of refresh messages should be as small as possible. Thus, if a database entry has gone through multiple updates, only the last version should be included in the refresh request.

(C4) The scheme should be able to support multiple, different snapshot definitions over the same database table.

From the perspective of a database administrator or software developer, there is an additional “software” complexity/cost criteria, specifically,

(C5) Does the scheme require redefinition of the database itself and modification of, or “hooks” into, the DBMS and the teleprocessing software (e.g., IBM’s DB/DC software).

One reason for the popularity of full regeneration is that it is essentially the only scheme that does not require new features to be added to the DBMS itself. Thus, for many installations, full regeneration is the only practical alternative.

Criterion C1, “consistency,” merits clarification. We define “point consistency” between snapshot and database to mean that the snapshot represents the state of relevant records in the database at a single point in time. To illustrate, assume that a snapshot is defined as a selection of records from a single base table. Then, point consistency precludes schemes that determine the refresh messages by scanning the base table without locking (essentially) the entire table. If only individual records are locked, updates could occur to a record after it was scanned, but before the table scan is completed. Similarly, if point consistency is not enforced, a transaction that updates a number of records in the base table may be only reflected in some of the records in the snapshot, thereby causing such a snapshot to be internally inconsistent.

As Lindsay et al. [12] note, to assure point consistency requires that, on the average, half the table will be locked. For example, to guarantee that the snapshot is consistent with the base table just after the scan ends, a page-level lock is acquired just before the page is scanned. However, once the page is locked, it remains locked until the entire scan is complete. Thus, the refresh activity need not hold locks on those pages not yet scanned. Alternatively, to assure that the snapshot is consistent with the base table immediately before the scan begins, page-level locks for all the pages are acquired before scanning. However, as soon as a page is scanned, its lock may be released.

There are alternatives to point consistency. For example, during message generation, a scheme might lock a record (or its page) only as it is scanned. Of course, with this level of locking, the snapshot will not be point consistent (in general) with the base table.

With these objectives in mind, the following sections outline several differential refresh schemes. The focus is on snapshots that are defined over a single file in the database (as opposed to snapshots that involve, say, joins). Each scheme is explained using a running example (given in Figure 1) that describes a database file at two refresh instances—the transactions posted against it, and the snapshot just after refresh.

The refresh schemes described here fall into two categories: (1) schemes that require scanning the base table to generate refresh messages, and (2) schemes that maintain a history of updates to the database for generating the refresh message. The “scanning” schemes include full regeneration, modified regeneration, and System $R^{*}$ . The difference-table scheme of Saharia and Diehr [16] is representative of “history” methods.

## 2.1. Modified-Regeneration Scheme

Modified regeneration maintains a copy of the snapshot at the central site. When a refresh request arrives, a new version of the snapshot is created by a scan of the database. Such a scan may be sequential, in which case each and every record in the base table is read, or records may be randomly accessed using appropriate indexes as determined by the query optimizer. The new version is compared to the old version to determine the relevant changes since the last refresh. Added and modified records are transmitted to the snapshot site. If the snapshot records include keys, keys of deleted records are also transmitted. If the snapshot records do not include unique identifiers, then all attributes of deleted records are sent. While this modified-regeneration scheme is “obvious” and may even be used in practice, we are not aware of any publication that has described the scheme or analyzed its performance.

<table><tr><td>CLIENT</td><td>CONSULTANT</td><td>HOURS</td></tr><tr><td>NICOLAI SERV.</td><td>SAHARIA</td><td>15</td></tr><tr><td>JR PROD.</td><td>SMITH</td><td>20</td></tr><tr><td>NW PIPE DIST.</td><td>DAIGLE</td><td>18</td></tr><tr><td>KELLY&#x27;S</td><td>DIEHR</td><td>17</td></tr><tr><td>BIOTECH. INC.</td><td>DIEHR</td><td>23</td></tr></table>

<table><tr><td rowspan="2">(iii) MODIFYTO</td><td rowspan="2"></td><td colspan="3">ASSIGNMENTS</td></tr><tr><td>CLIENT</td><td>CONSULTANT</td><td>HOURS</td></tr><tr><td rowspan="2">(iv) MODIFYTO</td><td rowspan="2"></td><td>ABLE &amp;CO.</td><td>PRIZZI</td><td>12</td></tr><tr><td>NICOLAI SERV.</td><td>SAHARIA</td><td>15</td></tr><tr><td rowspan="2">(v) MODIFYTO</td><td rowspan="2"></td><td>JR PROD.</td><td>SMITH</td><td>20</td></tr><tr><td>NW PIPE DIST.</td><td>DAIGLE</td><td>18</td></tr><tr><td rowspan="3">(vi) MODIFYTO</td><td rowspan="3"></td><td>MASON &amp; CO.</td><td>SAHARIA</td><td>9</td></tr><tr><td>KELLY&#x27;S</td><td>DIEHR</td><td>17</td></tr><tr><td>BIOTECH. INC.</td><td>DIEHR</td><td>23</td></tr></table>

A very attractive feature of this scheme is that (as with full regeneration) it can be implemented without modification of either central- or remote-site DBMS software. For example, consider a system that supports SQL and has a stored copy of the current (or "old") snapshot called OLD. Upon receipt of a refresh command, the new (central site) snapshot is created by executing an SQL command to load a table (say) NEW. Next, the OLD table is subtracted from NEW to give the entries to be added to the snapshot. Subtraction of NEW from OLD gives the entries to be deleted from the snapshot. The old snapshot, the new snapshot, and the refresh messages generated for this scheme are shown in Figure 2.

The following shows how SQL can be used to create the “add” messages and “delete” messages and update the remote snapshot. The add messages are created by:

INSERT INTO ADD\_MSG

SELECT \* FROM NEW

MINUS

SELECT \* FROM OLD

Assuming that the snapshot includes a key, the delete messages are created by:

INSERT INTO DEL\_MSG
SELECT KEY FROM OLD
WHERE KEY NOT IN
(SELECT KEY FROM NEW)

The remote site can also use SQL to update its snapshot once it has received ADD\_MSG and DEL\_MSG. It first deletes all records that have either been deleted or updated using the following:

DELETE FROM SNAPSHOT
WHERE KEY IN
(SELECT KEY FROM ADD\_MSG
UNION SELECT KEY FROM DEL\_MSG)

It then inserts all records from ADD\_MSG:

INSERT INTO SNAPSHOT
SELECT \* FROM ADD\_MSG
Modified regeneration transmits no redundant messages. Each message results in a required update to the snapshot—i.e., either a record insertion, modification, or deletion.

![](/api/attachments/6EP92EBK/fulltext/images/e858a08126305ccb785ebfbf73b5748eecfb496a203a4ab9a012281549ece498.jpg)  
Refresh request (Definition: SELECT \* FROM ASSIGNMENTS WHERE HOURS ≥ 15; Current Snapshot = OLD)  
Figure 2. Refresh Message Generation in the Modified-Regeneration Scheme. The snapshot definition and the table to be used as the copy of the old snapshot are explicitly identified as part of the refresh request.

The disadvantage of modified regeneration is the necessity to create a complete new version of the snapshot. Thus, if few relevant changes have occurred to the database between refreshes, the cost of creating the new snapshot and determining the add and delete messages may have a significant impact on normal database processing. If the snapshot is to be consistent with the base table at refresh time (criterion C1), the base table must be locked during creation of the new snapshot. The impact on normal processing (the extent to which the scheme satisfies criterion C2) will depend, to a great extent, on whether point consistency is required, and on whether the refresh must take place during periods of heavy processing or if it can be deferred to off-hours.

The cost of a new snapshot will also depend on the existence of cost-effective indexes. If, for example, an index exists that is relevant to the snapshot definition and has “selectivity” (proportion of records that must be retrieved) of (typically) 10 percent or less, or, if a clustering index exists, a substantial savings over the cost of a full file scan may be realized.

The characteristics of modified regeneration can be summarized as follows:

(C1) It requires locking the full base table during refresh if a point-consistent snapshot is to be created.

(C2) It requires recreation of the full snapshot via file scan or use of indexes and two differencing operations on the old and new snapshots to generate the refresh messages. Thus, the impact on normal operations is independent of the update rate; it depends on whether point consistency is required, the number of updates between consecutive refreshes, the proportion of qualified records, and the presence of cost-effective indexes.

(C3) Ignoring the possibility of compressing multiple deletion keys into a single message (e.g., see System $R^{*}$ scheme), it transmits the minimum possible number of messages.

(C4) It supports multiple views either by separate operations for each view refresh or by a single scan to extract records satisfying the union of the snapshots (into separate NEW snapshot tables).

(C5) It requires no modification of database or DBMS software. It can be implemented with high-level SQL commands.

## 2.2. Time-Stamping Database Records

The changes required to refresh a snapshot are represented by those qualified records in the database that have been modified, inserted, or deleted since the last refresh. These records can be identified by adding a time-stamp field to each record, giving the last time a record was modified. Each record also includes a flag to indicate insertion, modification, or deletion. The database entries that have changed since the last refresh are determined by comparing the time-stamp field for each record against the time of last refresh. Insertions, deletions, and modifications are then handled as follows:

Insertions are straightforward—if the record is qualified, it is transmitted to the snapshot. Modifications are more complex, since a record may be modified from (say) a qualified to a nonqualified state. Thus, modified records that remain qualified are transmitted to the snapshot to replace earlier versions. Keys of modified records that are nonqualified now (or the full records if the snapshot does not include a key) are transmitted with a deletion indication. If the record exists in the snapshot, it is deleted; otherwise, the message is ignored (it is redundant).

Deletions require additional special handling, since the refresh activity requires that we identify records that were represented in the snapshot but have to be deleted from the snapshot. A possible approach is to mark records as deleted rather than physically deleting them at refresh time (a delete message is sent for each such record). Note again that, even if the record is nonqualified at the time of deletion, there exists the possibility that it was qualified at the time of last refresh (hence exists in the snapshot), was modified to become nonqualified, and subsequently deleted. Records that are marked deleted may be physically removed after all snapshots have been refreshed.

Lindsay et al. [12] report a time-stamping mechanism implemented in system $R^{*}$ , the experimental distributed database management system being developed at IBM. In addition to using a time-stamp to identify insertions and modifications, boundaries of empty regions are maintained to identify deletions. This can be efficiently done by extending each base-table record to include a pointer called previous-address, which gives the address of the previous record. The scheme thus requires either a unique key or a fixed address for each record in an ordered address space. These record identifiers are also stored in the snapshot.

As we discuss in the following, a deletion or an insertion causes one or both of these fields for the next record to be updated. These fields could be set at the time of each insertion or deletion; however, since the only purpose of the fields is to support a refresh, it is less expensive to set the field values using a batch process immediately before the next refresh. At that time, the two fields for the affected records are revised during the scan performed to generate the refresh messages.

The time-stamp and previous-address fields may also be set to value NULL, as described in the following example. When comparing a record's time-stamp value with the time of previous refresh (called snap-time in the sequel), a high time-stamp (a NULL time-stamp is assumed to be higher than any other time) signifies that either the record itself has been updated or that the record is the upper boundary of a region from which one or more records have been deleted. The scheme thus allows for multiple snapshots, since for each snapshot all such regions from which deletions have occurred (since the last refresh for this snapshot) can be identified, irrespective of how many other snapshots have been refreshed in the intervening period.

At the time of an update, the previous-address and time-stamp fields are set in the record being updated or inserted using the following rules: a modified record has its previous-address field set to NULL, an inserted record has both fields set to NULL. At the time of base-table fixup, a record with NULL value in either of these fields is "fixed." In addition, a record whose value of previous-address does not match the address of the preceding record is also fixed. An insertion will cause only the previous-address of the subsequent record to be fixed, whereas a deletion will cause both the previous-address and the time-stamp to be fixed.

Figure 3 illustrates the example database file with time-stamp and previous-address fields at times of last and current refresh, the snapshot at these two times, and the refresh message. Unoccupied addresses (empty slots in the figure) are available for record additions. Handling of the time-stamp and previous-address fields for several updates is described below to illustrate the algorithm.

A value-modifying update (as opposed to a record insertion or deletion) simply sets the time-stamp to NULL. For example, the update of the record at location 1, the multiple updates of the record at 5, and the update of the record at 13 all create NULL time-stamp values. There is no change to the previous-address value.

An insertion sets both the previous-address and the time-stamp to NULL. An example is given by the record at address 2.

A deletion simply deletes the record. However, subsequent processing at refresh time uses the previous-address field of the subsequent records to detect deleted records. For example, the deletion of the record at location 8 will be detected because the previous-address of the record at location 9 now points to an empty slot.

On receiving a refresh request, the base table is sequentially scanned to reset the previous-address and time-stamp fields, as well as to determine the messages to be sent to the remote site. (As mentioned above, conceptually the two processes are separate. The base-table fixup can be done any time before refresh message generation and before other updates to the base table arrive. However, since both require scanning the base table, the two processes are performed in a single scan.) The algorithm uses the following rules to reset these fields. (In the following, “existing” record refers to a record in the base table at the time of last fixup—i.e., as opposed to a record inserted since the last refresh.)

A record with a NULL previous-address indicates an insertion since the last fixup. The time-stamp of the inserted record is set to the current time and previous-address is set to the address of the previous entry in the base table. In Figure 3, such a record is at address 2.

A record with a non-NULL previous-address and a NULL time-stamp indicates an existing record that was subsequently updated. The time-stamp is set to the current time. In Figure 3, such records are at locations 1, 5, and 13.

A record with a non-NULL previous-address that does not match the address of the immediately preceding existing record indicates that one or more records between the current record and the last existing record have been deleted. Both the time-stamp and previous-address for such records are updated. In Figure 3, such a record is at address 9, since the previous-address for this record does not point to 5, the address of the immediately preceding existing record.

A record with a non-NULL previous-address that does not equal the address of the (current) previous record (but does equal the address of the previous existing record) indicates that the (current) previous record must be an insertion and that no deletions have taken place in the (previously) empty region that ends at the current record. In this case, only the previous-address field is updated. In Figure 3, an example is given by the record at address 4.

As a result of these rules, a record with a time-stamp greater than the time of the previous refresh is either (1) an insertion or a modification, or (2) the boundary of an address region from which one or more deletions have taken place. If such an updated record is qualified, the record and its address are sent to the remote site. On the other hand, if the updated record is not qualified, then the next qualified record is sent, even though its time-stamp may be less than the time-stamp of the previous refresh. In either case, the previous-address field in the refresh message is set to the address of the previous qualified record, so that each message also indicates the boundary of the region that does not contain any qualified records and ends with the record itself.

The remote site issues the refresh request by identifying the snapshot definition and the time of previous refresh. In Figure 3, the remote site issues a refresh request at time 12:00. The request explicitly includes the definition (of the snapshot) and the

Downloaded by [University of Pennsylvania] at 01:16 12 August 2017

Refresh request (Definition: SELECT \* FROM ASSIGNMENTS WHERE HOURS ≥ 15; Snap-Time = 8:30)

<table><tr><td>PREV.ADD.</td><td>CLIENT</td><td>CONSULTANT</td><td>HOURS</td><td>TIMESTAMP</td></tr><tr><td>0</td><td>ABLE &amp;CO.</td><td>PRIZZI</td><td>12</td><td>12:00</td></tr><tr><td>1</td><td>NICOLAI SERV.</td><td>SAHARIA</td><td>15</td><td>12:00</td></tr><tr><td>2</td><td>JR PROD.</td><td>SMITH</td><td>20</td><td>6:30</td></tr><tr><td>4</td><td>NW PIPE DIST.</td><td>DAIGLE</td><td>18</td><td>12:00</td></tr><tr><td>5</td><td>MASON &amp; CO.</td><td>SAHARIA</td><td>9</td><td>12:00</td></tr><tr><td>9</td><td>KELLEY&#x27;S.</td><td>DIEHR</td><td>17</td><td>8:30</td></tr><tr><td>10</td><td>BIOTECH. INC.</td><td>DIEHR</td><td>23</td><td>12:00</td></tr></table>

<table><tr><td>ADDRESS</td><td>PREV.ADD.</td><td>CLIENT</td><td>CONSULTANT</td><td>HOURS</td></tr><tr><td>2</td><td>0</td><td>NICOLAI SERV.</td><td>SAHARIA</td><td>15</td></tr><tr><td>5</td><td>4</td><td>NW PIPE DIST.</td><td>DAIGLE</td><td>18</td></tr><tr><td>10</td><td>5</td><td>KELLEY&#x27;S.</td><td>DIEHR</td><td>17</td></tr><tr><td>13</td><td>10</td><td>BIOTECH. INC.</td><td>DIEHR</td><td>23</td></tr><tr><td>NULL</td><td>13</td><td>NULL</td><td>NULL</td><td>NULL</td></tr></table>

<table><tr><td>ADDRESS</td><td>CLIENT</td><td>CONSULTANT</td><td>HOURS</td></tr><tr><td>2</td><td>NICOLAI SERV.</td><td>SAHARIA</td><td>15</td></tr><tr><td>4</td><td>JR PROD.</td><td>SMITH</td><td>20</td></tr><tr><td>5</td><td>NW PIPE DIST.</td><td>DAIGLE</td><td>18</td></tr><tr><td>10</td><td>KELLEY&#x27;S.</td><td>DIEHR</td><td>17</td></tr><tr><td>13</td><td>BIOTECH. INC.</td><td>DIEHR</td><td>23</td></tr></table>

Figure 3. Message Generation, Database Fixup, and Snapshot Update in the System R\* Scheme. The current refresh occurs at 12:00. The snapshot definition and time of previous refresh are explicitly provided as part of the refresh request.  
![](/api/attachments/6EP92EBK/fulltext/images/37dbe1aab332eee655bfd0e0b855a9624ce6836357dac0a070ffb30b41710216.jpg)

<table><tr><td>ADDRESS</td><td>PRIV ADD.</td><td>CLIENT</td><td>CONSULTANT</td><td>HOURS</td><td>TIME STAMP</td></tr><tr><td>1</td><td>0</td><td>ABLE &amp;CO.</td><td>PRIZZI</td><td>10</td><td>8:30</td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>1</td><td>JR PROD.</td><td>SMITH</td><td>20</td><td>6:30</td></tr><tr><td>5</td><td>4</td><td>NW PIPE DIST.</td><td>PRIZZI</td><td>13</td><td>8:30</td></tr><tr><td>6</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td>5</td><td>VISION SERV.</td><td>DAIGLE</td><td>12</td><td>6:00</td></tr><tr><td>9</td><td>8</td><td>MASON &amp; CO.</td><td>SAHARIA</td><td>9</td><td>7:00</td></tr><tr><td>10</td><td>9</td><td>KELLEY&#x27;S.</td><td>DIEHR</td><td>17</td><td>8:30</td></tr><tr><td>11</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>12</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>13</td><td>10</td><td>BIOTECH. INC.</td><td>DIEHR</td><td>20</td><td>7:00</td></tr></table>

<table><tr><td>ADDRESS</td><td>CLIENT</td><td>CONSULTANT</td><td>HOURS</td></tr><tr><td>4</td><td>JR PROD.</td><td>SMITH</td><td>20</td></tr><tr><td>10</td><td>KELLEY&#x27;S.</td><td>DIEHR</td><td>17</td></tr><tr><td>13</td><td>BIOTECH. INC.</td><td>DIEHR</td><td>20</td></tr></table>

snap-time. The request triggers a scan, during which the base-table entries are fixed and the refresh messages are generated.

After fixup, the records at addresses 2, 5, and 13 have high time-stamp values and are qualified. Therefore, these records are included in the refresh message. The records at locations 1 and 9 have high time-stamp values but are not qualified for the snapshot. These cause the next record qualified for the snapshot to be transmitted, even if it has a low time-stamp. The record at location 9 causes the record at 10 to be transmitted. For each transmitted record, the address of the previous qualified record is also included. Thus, the previous-address field of the record at 10 is set to 5. This indicates that there are no qualified records between locations 5 and 10; hence, all records with intervening addresses should be deleted from the snapshot. Finally, note that the record at location 4 will not be checked for relevance, since it has a low time-stamp, indicating that the record has not been updated, nor have there been any deletions in the empty region preceding this record.

This scheme can generate redundant messages as seen from the example—the deletion of the record at address 8 causes record 10 to be sent. Since record 10 was not updated, and the deleted record at 8 was not qualified, this message is redundant. (Another way to see that this message is redundant is to note that it has no impact on the final form of the snapshot.) This redundancy will occur whenever a nonqualified record is deleted and the next qualified record was not updated.

The following summarizes System $R^{*}$ against the criteria:

(C1) The scheme guarantees point consistency (see C2).

(C2) It requires a file scan. Base-table locking is required during the scan to assure point consistency. Message generation cost will depend primarily on the frequency of refresh; however, the update rate will determine the number of "dirty" base-table pages that must be written to the disk to reset the time-stamp and previous-address fields. Costs will be substantially reduced if refreshes can be performed during off-peak periods and point consistency is not required.

(C3) The number of redundant messages depends on the update rate and refresh frequency. As shown by the subsequent analysis, the proportion of redundant messages is considerable in some situations.

(C4) It supports multiple snapshots. All messages for a snapshot refresh can be identified using the time-stamp field, even if the time-stamp and previous-address fields have been reset in response to a refresh of some other snapshot.

(C5) The scheme requires modification of the database to add time-stamp and previous-address fields and procedures to set these field values on update. Setting these fields (to NULL) could be included as part of transaction processing software. However, it is more convenient (and less prone to error) if these operations are part of the DBMS software.

## 2.3. Use of History Files

An alternative to time-stamping the base-table entries is to maintain a separate file of updates. A database log file, typically maintained by a DBMS, represents such a history file. In response to a refresh request, portions of this log since the last refresh may be scanned, and before and after images that are qualified for the snapshot transmitted to the remote site. A problem with this scheme is that a database log will typically contain updates from all database tables. Thus, it will probably be necessary to scan a large number of records to identify qualified entries. This scanning cost could easily exceed the cost of the file scans required by full regeneration, modified regeneration, and System $R^{*}$ schemes.

![](/api/attachments/6EP92EBK/fulltext/images/a2c333508414bfbc59a0357f03c6708d87680e03b3a2fbbb5a416374e837d1bf.jpg)  
Figure 4. Difference-Table Maintenance and Refresh Message Generation in the Difference-Table Scheme. The snapshot definition is maintained at the central site and is used to determine if a transaction is relevant to the snapshot. The difference table to be used is explicitly identified as part of the refresh request.

Recently, Saharia and Diehr [16] have proposed a scheme that maintains a selective history file, called a difference table, for each active snapshot. In this approach, each update is monitored for potential relevance to the snapshot—if relevant, its effect on the snapshot is determined (i.e., insertion, modification, or deletion) and the record is stored in the difference table. If a record receives multiple updates, the difference table contains only the net effect rather than the entire sequence of updates.

Salient features of the scheme can be described by using the example in Figure 4. Update (i) is an insertion and is relevant, since its hours field is greater than or equal to 15. It causes an insertion in the difference table with FLAG = A to indicate addition. The second update, a deletion, is not relevant, and hence has no impact either on the snapshot or on the difference table. Update (iii) changes hours from 10 to 12. This can be modeled as a deletion of the before-image of the record and an addition of the after-image. Neither is relevant. Update (iv) changes a record from nonqualified to qualified. This creates an insertion to the difference table with FLAG = A. Update (v) modifies this same record, increasing the hours from 15 to 18 and changing the consultant from Prizzi to Daigle. The result is a single entry with FLAG = A in the difference table. This illustrates that multiple updates to the same record do not create multiple DT entries. Upon receiving a refresh request, the difference table is transmitted to the remote site and a new, empty difference table is opened.

If records contain keys, the FLAG value may be either D for deletion, A for addition, or M to indicate field-value modification of an existing record. With keys, update (vi) would be represented in the DT with a single entry: BIOTECH, INC./DIEHR/23, and FLAG = M. Flag values are managed so that redundant messages are never transmitted.

Note that the difference-table approach is related to the differential file approach of Severance and Lohman [1, 17]. However, the purpose and mechanics of the two approaches are quite different:

(1) A differential file stores after-images of all updated records (insertions and value-modifying updates only) to the base table. A snapshot-difference table stores only those updates relevant to the snapshot. The difference table must also store deletions of qualified records.

(2) With a differential file, base-table queries (for all applications) are directed first to the differential file (possibly using a Bloom filter to “indicate” if a record has been updated). A snapshot-difference table has no impact on base-table queries.

(3) The differential file is used to update the base table in a batch mode. A snapshot-difference table has no impact on base-table updates (other than the requirement that updates be examined for relevance to the snapshot).

Thus, a difference table is an appendage designed solely to support a snapshot; if there is currently no snapshot, there will be no difference table. In fact, a database might utilize both a differential file approach for normal base-table queries and updates and difference tables for snapshot support.

The difference-table approach has the following additional characteristics and features in comparison to alternative schemes: (i) it does not require locking the base table during generation of refresh messages, (ii) it does not depend on having records stored in an ordered address space, and (iii) it does not require restructuring the database to include a time-stamp field.

The major disadvantage of a difference-table approach is that updates must be monitored continuously to determine whether they are relevant to a snapshot. This added impact might be significant if the processing load is heavy and/or there are multiple snapshots. However, the relevance check and posting to the difference table can operate as a background process—it is acceptable that posting any updates to the difference table lag behind the database updates. The difference table needs to be brought into a consistent state with the base table only at refresh time (assuming that point consistency is desired). However, to assure that the updates to the base table are correctly posted in the difference table, we may require that the transaction be marked as being relevant to a snapshot on a stable storage medium before the transaction is committed. Otherwise, a system crash after updating the database but before updating one or more difference tables may cause the difference tables to be inconsistent with the base table. Thus, guaranteeing consistency may require additional costs on the transaction processing system. In this work, we assume difference tables are updated as part of the commit protocol and that there are no additional costs associated with guaranteeing such consistency.

Multiple snapshots can be supported simply by having a single difference table per snapshot. This, of course, could become expensive, both in relevance checking costs and even in storage costs. While not detailed herein, multiple snapshots can also be supported by a single difference table. In this case, relevance checking uses the union of all snapshot definitions and additional relevance checking must be performed at refresh time to determine the messages to be transmitted. It is also necessary to time-stamp entries in the difference table so that they may be purged after all snapshots have been refreshed.

To summarize the difference-table scheme against our criteria:

(C1) It creates a point-consistent snapshot (without additional locking).

(C2) It creates a small impact for each database update to perform the relevance check.

(C3) The minimum number of messages is sent.

(C4) Different views are supported by creating multiple difference tables and checking each update against each snapshot definition; a single difference table storing the union of all relevant updates may also be used as outlined above.

(C5) The scheme requires the addition of a difference table. Difference-table maintenance can be included in the transaction processing system. However, it is more desirable to include it as a standard feature of the DBMS software.

## 3. Analysis of Differential Refresh Schemes

IN THIS SECTION, COST MODELS ARE DEVELOPED FOR THE SCHEMES. The schemes are then evaluated using these models. The focus is on costs for generation of refresh messages and transmission of the messages. The following assumptions are made:

(A1) The snapshot is based on a single base table—joins, for example, are not considered.

(A2) The size of the base table is fixed at N records. This assumption implies either that all updates are of the attribute-modifying variety and/or that the number of additions equals the number of deletions.

(A3) The number of updates between two refreshes is static and given by $u * N$ . Note that each addition is matched with a deletion and the pair counted as a single update.

(A4) The probability that a record qualifies for the snapshot is Q.

(A5) The updates are randomly assigned to records (with equal probability). The probability that a record receives an update is independent of the number of updates it has already received. Another way of stating this assumption is that the $u * N$ updates are random draws from the $N$ records with replacement. In the limit, this assumption means that the expected number of records receiving updates between two refreshes is $N * M$ , where $M = 1 - e^{-u}$ is the fraction of records receiving at least one update [1]. $^{1}$

(A6) The cost to read or write a file block is $C_{I/O}$ . All files are written with a blocking factor of B.

(A7) The CPU cost to determine whether a record qualifies for a snapshot is $C_{Q}$ .

(A8) Communication cost per refresh message is $C_{T}$ ; thus, communication cost for one refresh is $C_{T} * NMsg$ , where NMsg is the number of messages. Communication cost is assumed to be independent of the size of a message.

In the following sections, costs are developed for:

full regeneration,

modified regeneration,

time-stamp methods represented by the System $R^{*}$ scheme,

history methods represented by the difference-table scheme.

The parameters used in the discussion are given in Table 1.

## 3.1. Number of Messages

The following sections develop formulas for the number of refresh messages transmitted by each of the schemes.

## 3.1.1. Full Regeneration

In full regeneration, all records currently qualified for the snapshot will be transmitted to the remote site. Thus, the number of refresh messages is simply:

$$
N M s g _ {R e g e n} = N * Q
$$

## 3.1.2. Differential Refresh Schemes

Each refresh message is identified as one of three types of snapshot update:

(i) Modification. Both the old record and the modified record are qualified for the snapshot.

Table 1

<table><tr><td>parameter</td><td>meaning</td><td>value used</td></tr><tr><td>N</td><td>number of records in database</td><td></td></tr><tr><td>Q</td><td>fraction of database records qualified for snapshot</td><td>0.10</td></tr><tr><td>u</td><td>update rate per refresh cycle as a fraction of database size</td><td></td></tr><tr><td>B</td><td>blocking factor</td><td>10</td></tr><tr><td>M</td><td>fraction of base table modified</td><td> $1 - e^{-u}$ </td></tr><tr><td> $C_{I/O}$ </td><td>disk access cost per block</td><td></td></tr><tr><td> $C_T$ </td><td>transmission cost per entry</td><td>1.0 *  $C_{I/O}$ </td></tr><tr><td> $C_Q$ </td><td>CPU cost for qualification check per record</td><td>0.01 *  $C_{I/O}$ </td></tr></table>

(ii) Deletion. Either the corresponding record has been deleted from the database or a record that was previously qualified has become unqualified as the result of an update.

(iii) Addition. Either an addition of a qualified record or a record that was previously unqualified has become qualified as a result of an update.

To the extent that different schemes identify these types of entries in a similar way, we expect the number of refresh messages to be the same for all the schemes. Differences occur because schemes use different mechanisms to represent updates and to identify deletions.

System $R^{*}$ . An updated record relevant to the snapshot when the refresh request is processed will cause one refresh message, irrespective of whether it was previously relevant or not. Similarly, a newly inserted record that is relevant for the snapshot will create one refresh message. A deletion, however, does not generate an explicit refresh message. Rather, the next qualified record indicates an address range of records to be deleted. As noted earlier, deletions may create redundant messages. In a recent paper, Chao et al. [5] show that if the size of the base table is fixed, the number of refresh messages can be closely approximated by:

$$
N M s g _ {R} ^ {*} = N * Q * \left(1 - \frac {(1 - M) * Q}{M + (1 - M) * Q}\right)
$$

where M is the fraction of database records that receives at least one update between refreshes. Following assumption (A5), we approximate M by $(1 - e^{-u})$ . The second term in parentheses gives the fraction of qualified records that are not transmitted, because either (1) they have not been updated since the last refresh, or (2) they do not specify an address range containing unqualified records and/or an empty range in which there has been at least one update or deletion.

Modified-Regeneration and Difference-Table Schemes. Updates of various types generate refresh messages as follows:

(1) An update that changes a nonqualified record to qualified will cause an insertion refresh message.

(2) An update that changes a qualified record to nonqualified will cause a deletion message.

(3) An update that leaves a nonqualified record as nonqualified will create no message.

(4) An update that leaves a qualified record qualified after update will again require only one replacement message, provided we can identify the record to be replaced in the snapshot—that is, the record contains a key.

We assume that the probability that a record is qualified after update is independent of its state before update. Therefore, for records with keys, the average number of messages per updated record is $2 \times Q - Q^{2}$ . Since the number of updated records is $N \times M$ , the number of refresh messages is:

$$
N M s g _ {D i f f T a b l e} = N M s g _ {M o d - R e g} = (2 * Q - Q ^ {2}) * N * M
$$

Consider next the case of a snapshot that does not contain a key. $^{2}$ In this case, a value-modifying update of a qualified record requires generation of a deletion message (which is the full record with FLAG = D). Thus, a value-modifying update in which both before- and after-images are qualified has the same impact as a single deletion followed by a single insertion. In this case, the average number of messages per updated record in the base table is $2 \times Q$ , and the average number of refresh messages is:

$$
N M s g _ {D i f f T a b l e} = N M s g _ {M o d - R e g} = 2 * Q * N * M
$$

In the following evaluation of communication costs, we assume that the snapshot has a key.

## 3.1.3. Comparative Evaluation of Communication Costs

Figure 5 graphs NMsg for full-regeneration, System $R^{*}$ , and the difference-table schemes as a function of the update rate u. (Note the NMsg is same for the difference-table scheme and the modified-regeneration scheme.) At a low to moderate update rate (i.e., less than 50 percent of records updated), both System $R^{*}$ and the difference-table (and hence the modified-regeneration) schemes do substantially better than the full-regeneration scheme. However, System $R^{*}$ generates a considerable number of redundant messages. For example, at an update rate of 10 percent, System $R^{*}$ generates approximately 60 percent more messages than the difference-table/modified-regeneration scheme. Thus, for $u \leq 50$ percent, the difference-table/modified-regeneration schemes are the preferred choices.

At higher update rates, the number of messages in System $R^{*}$ is lower than for the difference-table scheme, and asymptotically approaches the number of messages for full regeneration. The number of messages for the difference-table/modified-regeneration schemes is $(2 * Q - Q^{2}) * N$ .

Even in the region where System $R^{*}$ is best, it is best by only a small amount.

Furthermore, we believe that update fractions as high as 50 percent between refreshes are unlikely. In most situations, working with data in which half or more of the records are “stale” would probably lead to unacceptable decision errors. Thus, from a pure message-cost standpoint, a policy limited to selecting between difference-table/modified-regeneration schemes and full regeneration (i.e., a policy that did not include System $R^{*}$ as an option) would be suboptimal in only rare circumstances, and even then only slightly more costly.

## 3.2. Message Generation Cost

This section develops models for the cost of generating refresh messages for each type of refresh scheme.

## 3.2.1. Message Generation Costs: Full-Regeneration Scheme

For the full-regeneration scheme, messages are generated by scanning the database. Each record is examined to determine if it qualifies for the snapshot. Thus, the message generation cost is given by:

$$
M s g G e n C o s t _ {R e g} = C _ {y _ {0}} * N / B + C _ {Q} * N
$$

The first term in this expression corresponds to reading a disk file stored with blocking factor B; the second term is the cost of identifying qualified records.

Use of an Index. If an index exists that incorporates the snapshot condition, the cost of generating the new snapshot may be less costly than a sequential file scan. For example, assume that an index exists indicating the qualified records. The cost of using the index will depend on a number of factors, such as (1) whether index pointers are absolute addresses or symbolic pointers; (2) whether or not the pointers for a single index key value are sorted; (3) whether the snapshot's qualifying condition is a single key value or a set of values; (4) the amount of internal buffer space; (5) whether records are physically ordered by the index; and (6) the record blocking.

Lohman and Mackert [13] provide an extensive analysis for indexing schemes such as used by System $R^{*}$ . Assuming that the addresses for each key value are ordered (so that each block will be read only once for a given key value), the expected number of blocks read to retrieve $k = Q * N$ qualified records is given by the Yao function [19] $Y(k, B, N)$ . A number of approximations to the Yao function have been discussed in [6, 13]. As a representative example of the cost of using an index, assume the following: (1) index pointers are absolute addresses; (2) the snapshot-qualifying condition specifies a single key value (e.g., $JOB = “ENGR”$ ); (3) pointers for a single key value are sorted; (4) the base table is quite large; (5) the number of records of a single key value (e.g., “ENGR”) is greater than record blocking, i.e., k/B > 1; and (6) records are not clustered on the index key. Under these assumptions, a very close approximation to the Yao function is given by [6, 13]:

$$
N / B (1 - (1 - k / N) ^ {B}) = N / B (1 - (1 - Q) ^ {B}),
$$

which is exact for $B = 1$ . At larger $B$ , the error in this estimate is very small for $k /$

![](/api/attachments/6EP92EBK/fulltext/images/683319fef8cab68c58f251a1794aab5fd318e65f553413941edcc82f65820674.jpg)  
Figure 5. Comparative Evaluation of Number of Messages. Number of messages is the same for difference-table and modified-regeneration shchemes.

B > 1. (E.g., at B = 10, N = 10,000, Q = 10 percent, the exact expression gives 651.5 blocks accessed, while this estimate gives 651.3 blocks.) Note that for smaller values of Q \* B, a simple approximation for the number of blocks accessed is Q \* N, or, equivalently, one access per qualified record.

Under the assumption that each qualified record is retrieved by a single disk access, the cost to access qualified records will be $C_{I/O} * N * Q$ . Such an index will be cost effective versus a full sequential scan if $C_{I/O} * (Q - 1/B) \leq C_Q$ . Since $C_Q$ is likely to be considerably smaller than $C_{I/O}$ , the index will be useful if $Q * B \leq 1$ . In our cost analysis, we assume that full file scans are required to identify qualified records. The reader should keep in mind that the full-regeneration and modified-regeneration schemes can benefit from an index, especially when $Q * B$ is small. Indexes cannot reduce the costs for the System $R^*$ and difference-table schemes.

## 3.2.2. Message Generation Cost: Differential Refresh Schemes

Although the number of refresh messages will be approximately equal in all differential refresh schemes (except as noted above), the cost of creating messages will differ significantly across schemes.

Modified Regeneration. The cost to generate refresh messages includes costs for a file scan, relevance check, and comparison of old and new snapshots:

$$
M s g G e n C o s t _ {M o d - R e g} = C _ {\nu_ {0}} * N / B + C _ {Q} * N + 2 * C _ {\nu_ {0}} * Q * N / B
$$

The first term corresponds to the cost of a base-table scan, the second term is the cost of relevance checking, and the third term is the cost of creating the two differences of old and new snapshots. We assume that the two snapshots are ordered on the same attribute (i.e., they are in the same order as the base table) and that the two differences are determined in a single pass through each snapshot of size $Q * N / B$ blocks. No cost has been associated with the actual comparison of keys of records from the old and new snapshots. (If a relevant index were available and each qualified record required one disk access, the first two terms would be replaced by $C_{I/O} * N * Q$ .)

System $R^{*}$ . Refresh messages are generated by scanning the base table. However, some of the records must be written to reset the time-stamp and previous-address fields. The message generation cost is given by:

$$
M s g G e n C o s t _ {R} ^ {*} = C _ {\nu_ {o}} * N / B + C _ {Q} * N + C _ {\nu_ {o}} * Y (M * N, N, B)
$$

The first term corresponds to a scan of the database, the second to determining which records are qualified, and the third to writing back the pages containing updated records. Following our discussion in section 3.2.1., we use the following estimate for the Yao function [6,13]:

$$
N / B * (1 - (1 - k / N) ^ {B}) = N / B * (1 - (1 - M) ^ {B})
$$

Under assumption (A5), $M$ is given by $(1 - e^{-u})$ . The number of pages to be rewritten is given by $N / B * (1 - e^{-uB})$ .

Difference Table. Assume first the more general case of a snapshot without a key. Each update of an existing record requires a relevance check of both the before- and after-images of the record. If the before-image is qualified, it is inserted into the difference table with FLAG = D. If the after-image is qualified, it is inserted into the difference table with FLAG = A. Each insertion with FLAG = A is checked to see if there is an identical record in the difference table with FLAG = D. If so, the existing entry is deleted. Similarly, each insertion with FLAG = D is checked to see if there is an identical record in the difference table with FLAG = A. If so, the existing entry is deleted. This has the effect of including only the latest version of a record that has gone through multiple updates. (Recall that the number of base-table updates, $u * N$ , pairs each insertion with a deletion and counts the pair as a single update.)

Therefore, the difference table will be modified $2 \times Q \times u \times N$ times between two refreshes. We assume that the difference table is organized as a hash file, so that each modification requires (roughly) two disk accesses—one to read the block to determine if an existing entry matches the current entry, and one to rewrite the block. Thus, the message generation cost is:

$$
M s g G e n C o s t _ {D i f f T a b l e} = C _ {Q} * 2 * u * N + C _ {y _ {0}} * 4 * Q u * N
$$

The first term corresponds to the cost of checking updates for relevance, and the second to modifying the difference table.

If the snapshot includes a key, situations in which the modified record is qualified both before and after update require only a single base-table modification. In this case the second term will reduce to $C_{I/O} * 2 * (2 * Q - Q^{2}) * u * N$ . Presence of a key is assumed in the following comparative analysis so that the appropriate cost model is:

$$
M s g G e n C o s t _ {D i f f T a b l e} = C _ {Q} * 2 * u * N + C _ {y _ {0}} * 2 * (2 * Q - Q ^ {2}) * u * N
$$

## 3.2.3. Comparative Evaluation of Refresh-Message-Generation Costs

Figure 6 gives the cost of generating refresh messages for different schemes as a function of update rate. The base table processing cost for System $R^{*}$ is higher than the scanning costs for full regeneration, because System $R^{*}$ must write “dirtied” pages. The scanning costs for modified regeneration and full regeneration are the same, but modified regeneration also involves costs for comparison of the old and new versions of the snapshot. Thus, if message generation cost is used as the sole criterion, modified regeneration or System $R^{*}$ would never be chosen over full regeneration. The cost for the difference-table scheme grows linearly with the update rate. Therefore, at low update rates the difference-table scheme will be preferred over the full-regeneration scheme.

## 3.3. Evaluation of Schemes Based on Total Cost

The total costs of message generation and transmission for the various schemes are given below:

$$
C o s t _ {R e g e n} = C _ {T} * N M s g _ {R e g e n} + C _ {I / O} * N / B + C _ {Q} * N
$$

$$
\operatorname{Cost} _ {\text {ModReg}} = C _ {T} * N M \operatorname{sg} _ {\text {Regen}} + C _ {I / O} * N / B + C _ {Q} * N + 2 * C _ {I / O} * Q * N / B
$$

$$
C o s t _ {R} ^ {\bullet} = C _ {T} * N M s g _ {R} ^ {\bullet} + C _ {I / O} * N / B + C _ {Q} * N + C _ {I / O} * N / B * (1 - e ^ {- u B})
$$

$$
C o s t _ {D T} = C _ {T} * N M s g _ {D T} + C _ {Q} * 2 * u * N + C _ {I / O} * 2 * u * N * (2 * Q - Q ^ {2})
$$

Cost parameter values are given in Table 1.

Figure 7 is a breakeven analysis between full-regeneration, modified-regeneration, System $R^{*}$ , and difference-table schemes. The figure illustrates the area in which each scheme has lowest cost as a function of update rate, u, expressed as the ratio of number of updates to number of base-table records, and qualification rate, Q. From this figure we draw the following conclusions:

The difference-table scheme prevails at both very low update rates and very low qualification rates independently of the other parameter.

In addition, the difference-table scheme is preferable in the vicinity of the origin. (See our comments below about this region.)

At higher update rates, with qualification rates less than about 40 percent, modified-regeneration or full-regeneration schemes outperform the difference-table scheme. The difference-table scheme “fades” in this region, because it must examine every update for relevance. Modified-regeneration and full-regeneration schemes, in contrast, examine only the last version of every record.

System $R^{*}$ outperforms other schemes in the region of high qualification rate and intermediate update rates. At very low update rates, System $R^{*}$ is dominated by the difference-table scheme because of the added cost of scanning the base table.

![](/api/attachments/6EP92EBK/fulltext/images/45f1b3fe8b5ef87bc2b7071db34e1398fbd36915c4a8ca14a165521c55cd7f57.jpg)  
Figure 6. Comparative Evaluation Based on Refresh Message Generation Cost Measured in Terms of Cost per Record.

These results depend, of course, on the values selected for blocking and costs of I/O, qualification, and message transmission. As can be seen from Table 1, the assumption is that I/O and transmission costs are equal—however, a storage block contains B records while a refresh message contains only a single record. The I/O and message costs are 100 times greater than the qualification cost. With blocking set at ten, this means that the scanning cost per record is ten times greater than the qualification cost per record. Figure 8 gives the breakeven analysis when transmission cost per message is one-tenth of the disk access cost. This would reflect an environment with low communication costs (perhaps due to dedicated communication lines). For such an environment, modified regeneration is dominated by full regeneration for all update rates and qualification ratios, since the additional cost of comparing the old versions and new versions of a snapshot will be more than the reduction in communication costs. Similarly, the region where System $R^{*}$ is cost effective also shrinks, since the additional cost of base-table fixup is not compensated by reduction in communication costs, except for very high qualification rates.

A number of additional breakeven graphs have been produced (but are not included here), varying the relationship between these parameters. For example, one graph was produced with the qualification cost increased by a factor of 10. This would reflect, for example, environments in which CPU time for qualification imposed considerable delay costs on other users. Since the qualification costs for full regeneration and System $R^{*}$ depend only on the number of records, their regions relative to each other remain unchanged. In contrast, for the difference-table scheme, qualification cost depends on the product of number of records and update rate. The result is that the line separating System $R^{*}$ and the difference-table scheme moves to higher update rates.

![](/api/attachments/6EP92EBK/fulltext/images/dae3a21ebfad567d335ab48bbd6ea3eb73350fc82f42b3adc28688418a72312b.jpg)  
Figure 7. Minimum Cost Regions for Refresh Schemes Based on Overall Costs.

Returning to Figure 7, we note that, while the region favoring the difference-table scheme is not physically large, we believe that the region in the vicinity of the origin is the likely operating region for most snapshots—that is, most snapshots will tend to involve a small fraction (e.g., 20 percent) of the base table and will be refreshed at small update rates. Given the cost parameters used for this graph, and the assumption that qualification proportion is typically less than 20 percent, there would be little reason to consider the System $R^{*}$ scheme.

## 4. Extensions and Future Work

SEVERAL ASSUMPTIONS HAVE BEEN MADE IN OUR ANALYSIS that limit the environments and applicability of the analysis. For example, we have assumed that the snapshot was defined over a single base table (e.g., a relational project and select). For snapshots involving joins, several of the schemes and all of the analyses must be extended. System $R^{*}$ , in particular, does not appear to adapt easily to this environment, due to the way it handles deletions. See Saharia and Diehr [16] for analysis of the difference-table scheme for join snapshots.

![](/api/attachments/6EP92EBK/fulltext/images/ac545ca80436b181e62d2e008eb0877c7f33214f6b0fbb4a301d20fe7efbf5cd.jpg)  
Figure 8. Same as Figure 7, except that transmission cost per message is one-tenth of the disk access cost

While we have outlined approaches for handling multiple snapshots with differing definitions, cost analyses are in terms of a single snapshot. Several of the schemes can (and should) be adapted to handle multiple snapshots efficiently. For example, the difference-table scheme can employ either a single difference table for each snapshot or a single difference table for the union of all snapshots (on a single base table). The best approach is not obvious; we are currently modeling and analyzing several alternatives.

## 5. Discussion and Conclusions

THIS PAPER REVIEWS AND ANALYZES SEVERAL SCHEMES for differential refresh of remote snapshots. These schemes utilize the fact that, between two refreshes, only a small proportion of the updates to the database may be relevant for the snapshot. Although these schemes may provide substantial savings over the commonly used full-regeneration scheme, all require additional data structures and processes. In comparing schemes, we have included the costs of these additional processes. Our analyses indicate that no scheme uniformly dominates the others.

At very high update and qualification rates, the costs of generating and transmitting refresh messages are high with any scheme. Therefore, the naive full-regeneration scheme should be used.

At low to moderate update and qualification rates, both the message generation and communication costs for differential refresh schemes (either the modified-regeneration or the difference-table) make them more attractive than either the full-regeneration or the System $R^{*}$ scheme.

For low update rates, or moderate update rates combined with low qualification rates, the difference-table scheme is more efficient than schemes requiring a database scan to generate refresh messages.

Based on the analysis presented here, database administrators and users can identify which scheme is best for their situations. One can visualize a scenario in which the refresh scheme selected for each snapshot depends on the characteristics of update, refresh frequency, proportion of relevant records, and values of the various cost factors. A “smart” refresh system that has maintained such statistics might be able to determine the best approach.

## ACKNOWLEDGEMENTS

This research was supported in part by a grant from the Unisys Corporation for Research and Development of an Information Center and by Summer Research Grants from the School of Business Administration, University of Washington. We would also like to thank two anonymous referees for their very helpful comments and suggestions.

## NOTES

1. Strictly speaking, the binomial distribution gives the following expression for the expected number of records receiving at least one update:

$$
N * (1 - (1 - \frac {1}{N}) ^ {u N})
$$

This expression is also the so-called Yao function for a blocking factor of 1. See the discussion in section 3.2. Also, see [13] for other approximations to the Yao function. The expression used here is obtained by making the Poisson approximation to the binomial distribution.

2. Note that while database theory requires all tables (base or snapshot) to include a key to enforce functional dependencies, in practice most DBMSs do not require a key. Snapshots, where no updates will occur, may not need unique record identifiers, especially if the data are used for statistical types of analyses as opposed to retrieval corresponding to individual entities.

3. For retrievals based on multiple keys, the analysis has to be extended to allow for a finite size buffer, so that a page may be read more than once.

## REFERENCES

1. Aghili, H., and Severence, D. G. Practical guide to the design of differential files for on-line databases. ACM Transactions on Database Systems, 7, 4 (1982), 540–565.

2. Adiba, M., and Lindsay, B. Database snapshots. Proceedings of the Sixth International Conference on Very Large Data Bases (1980), 86–90.

3. Blakeley, J. A.; Larson, P.; and Tompa, F. W. Efficiently updating materialized views. Proceedings of the ACM–SIGMOD Conference (1986), 61–71.

4. Ceri, S., and Pelagatti, G. Distributed Databases: Principles and Systems. New York: McGraw-Hill, 1984.

$$
R ^ {*}
$$

scheme. Working paper #3–90, Department of Management Science, University of Washington, 1990.

6. Cheung, T.-Y. Estimating block accesses and number of records in file management. Communications of the ACM, 25, 7 (1982), 484–487

7. Gorry, G. A., and Scott-Morton, M. S. A framework for management information systems. Sloan Management Review (Fall 1984), 55–70.

8. Hanson, E. N. A performance analysis of view materialization strategies. Proceedings of the ACM–SIGMOD Conference (1987), 440–453.

9. Inmon, W. H. Live data is not necessary: for DSS users, it's not even good for them. Information Center, 2, 8 (1986).

10. Inmon, W. H. For managers only: distinguishing between primitive and derived data is a key to control. Database Programming and Design (July 1988), 23–25.

11. Inmon, W. H. Optimizing Performance in DB2 Software. Englewood Cliffs, NJ: Prentice-Hall, 1988.

12. Lindsay, B.; Haas, L.; Mohan, C.; Pirahesh, H.; and Wilms, P. A snapshot differential refresh algorithm. Proceedings of the ACM–SIGMOD Conference (1986), 53–60.

13. Mackert, L. F., and Lohman, G. M. Index scan using finite LRU buffer: a validated I/O model. ACM Transactions on Database Systems, 14, 3 (1989), 401–424.

14. Roussopolous, N., and Kang, H. Principles and techniques in the design of ADMS. IEEE Computer (December 1986), 19–25.

15. Roussopolous, N. Overview of ADMS: a high performance database management system. Proceedings of the Thirteenth International Conference on Very Large Data Bases (1987).

16. Saharia, A. N., and Diehr, G. Refresh schemes for remote materialized views. To appear in Information Systems Research.

17. Severence, D. G., and Lohman, G. M. Differential files: their application to the maintenance of large databases. ACM Transactions on Database Systems, 1, 3 (1976), 256–267.

18. Sprague, R. H., and Carlson, E. D. Building Effective Decision Support Systems. Englewood Cliffs, NJ: Prentice-Hall, 1982.

19. Yao, S. B. Approximating block accesses in database organizations. Communications of the ACM, 20, 4 (1977), 260–261.
