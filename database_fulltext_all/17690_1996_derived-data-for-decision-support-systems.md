---
otero_id: 17690
otero_key: "75PNCQEC"
title: "Derived data for decision support systems"
authors: "Richard G. Ramirez; Uday R. Kulkarni; Kathleen A. Moser"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00008-9"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Derived data for decision support systems

Richard G. Ramirez $^{a,*}$ , Uday R. Kulkarni $^{b}$ , Kathleen A. Moser $^{a}$

$^{a}$ College of Business, Iowa State University, Ames IA 50011-2063, USA

$^{b}$ Decision and Information Systems, Arizona State University, Tempe AZ 85287-4206, USA

## Abstract

In decision-making situations requiring “what-if” analysis, in statistical databases, and in distributed databases, it is desirable to explicitly store derived data without losing consistency with the original data. We introduce independently-updated views (IUVs) for storage and use of derived data for decision-support systems. IUVs support multiple versions, provide derivation transparency, maintain data consistency, and afford control over time of derivation. The notion of data consistency is extended to allow for multiple versions so that versions are consistent with the actively updated database on which they are defined. Implementation issues are discussed and the cost of retrieving IUVs representing different types of derived data is estimated.

Keywords: What-if analysis; Derived data; Relational databases; Versions; Views; View updates

## 1. Introduction

Business databases are typically designed under the philosophy of “storing a fact once and only once” to avoid redundancy and potential inconsistencies. However, user queries, particularly those needed for managerial decision making, cannot be satisfied with data as it is stored and require the derivation of data. Derived data may include simple computations on a record (balance = previous - charges + credits), data combined from several files, or summary data such as sums, averages, and totals. Different users require different derived data from the same stored data.

Decision-support systems (DSS) can benefit from increased automatic support for derived data. Such support would address needs that are specific to decision-making and facilitate related tasks that presently require the intervention of a programmer. A decision-maker would then be free to concentrate on the decision rather than on the implementation. An obvious candidate for support of derived data is multiple scenarios for "what-if" analysis. Derived data in what-if analysis often takes the form of "versions." Consider a grocery store chain that has profiles of the products bought together by customers ("product baskets"). The chain wishes to observe the impact of reducing the prices of some products (to attract customers) while simultaneously increasing the prices of others. The alternatives are studied by building what-if scenarios; each scenario is a copy of the complete price list that is modified for a few prices and processed to obtain the product baskets. In most database management systems (DBMSs) available today, such as DB2 and ORACLE, each copy must be individually created and stored as a new table. The burden of managing these copies falls on the decision-maker since the DBMS has no knowledge that these new tables are derived from other tables and that they, in fact, differ only on a few items. An alternative would be to mark each copy as a “version” of the original table. A better alternative, as proposed in [38], would be to store only the differences to avoid duplication of data and update anomalies.

Another candidate for automatic support is data derived by aggregate functions in statistical and summary databases for managerial decision-making. If an operational database contains information about every customer order, the summary database may contain tables that store only total sales per store by month. As with what-if analysis, currently these databases must be individually created and managed as if their data were independent of the original database.

Data must often be derived as a consequence of database design. For example, to display an invoice, two files are usually joined: PRODUCTS, containing product number, description, and unit price, and ORDERS, containing the product number and quantity ordered. Database normalization typically results in multiple tables that must be joined for any given query.

In this paper, we propose Independently-Updated Views (IUVs) that explicitly address manipulation of derived data. IUVs present the following features:

1. Derivation transparency: Data may be treated identically regardless of whether it is derived or not. Derived data may be updated if the application so requires.

2. Support for multiple versions and what-if scenarios: Versions are explicitly defined and no duplication of data is necessary.

3. Database consistency: For versions defined on a dynamic database (i.e., a database constantly being updated), it is possible to detect database updates that would contradict the data in a version, and process those according to predefined policies.

4. Control over derivation: IUVs allow the user to specify whether derived data is stored to facilitate retrievals, or recomputed when needed.

The remainder of the paper is as follows. Section 2 introduces IUVs, presents a comprehensive example, and discusses retrievals and updates to IUVs. IUVs on dynamic databases and the maintenance of consistency are discussed. Section 3 discusses the performance of IUVs. We derive analytical cost expressions for retrieving IUVs and provide results of experiments with different types of derived data. Section 4 shows how IUVs provide support for the four different features listed above and compares IUVs with other mechanisms in the research literature on derived data. Section 5 concludes the paper.

## 2. Independently-updated views

We present Independently-Updated Views in top-down fashion. 2.1 gives an overview and introduces concepts and terminology. In 2.2 we provide details on the structures of the various tables involved. In 2.3 we discuss forming and querying IUVs. Updates to IUVs and their relationship to the underlying database are discussed in 2.4. In 2.5 and 2.6, we introduce the notion of “overlapping updates” and the maintenance of consistency in dynamic databases. The section concludes with a review of previous research.

## 2.1. Overview of IUVs

In introducing IUVs, we follow the common relational terminology. A base table is a relation defined independently from other tables in the sense that no base table is completely derivable from any other table or tables $[7]$ . A view is a table that is derived from one or more base tables $[12]$ . Views that are not physically stored are virtual relations while views that are physically stored are snapshots or materialized views $[2]$ . A differential table stores changes made to a “source” table $[18,36]$ ; these changes are incorporated into the source table when it is retrieved.

An independently-updated view, or IUV, is a virtual relation formed by making changes to a table called the parent table (PT) of the IUV. These changes are stored in a differential table (DT) and do not physically modify base tables;

they are only used to form the IUV. Being virtual relations, IUVs are not physically stored, only their DTs are physically stored. Conceptually, an IUV is formed by retrieving its PT and incorporating into it the changes stored in the DT. Fig. 1 shows the conceptual retrieval of an IUV. Physically, “query modification” [37] translates a query on an IUV into a query on physically-stored tables.

The PT contains data used as the basis for decision making. PT is either a base table, a view, or another IUV. Without loss of generality, we assume that PT is defined by a query definition. An IUV is an updated version of its PT. Updates (insertions, deletions, modifications) to an IUV are stored in its DT as differences between PT and the desired status of the IUV. DT contains one row for each PT row that appears changed (modified or deleted) in the IUV plus any rows added to the IUV not already in PT. DT has the columns of the PT and an additional column called ACTION that specifies the operation to be performed when the IUV is retrieved. If ACTION = ins, the DT row is inserted in the IUV. If ACTION = mod, the DT row replaces the corresponding PT row in the IUV. If ACTION = del, the corresponding PT row is deleted in the IUV. PT rows that are not changed in the IUV have no matching rows in DT.

Fig. 2 shows an IUV DEPT-MGR based on the PT DM and the DT DIFF-DM. Dept. No. is the primary key for all tables. TS (timestamp) is a system column that is automatically added and updated by the DBMS. The purpose of TS is described in 2.2. The IUV is obtained by outer-joining PT and DT on the primary key and then selecting columns and rows according to the ACTION code. The details of this operation are in 2.3. The rows in PT that have a matching row in DT (departments D1 and D2) are changed according to the value of the ACTION code. Thus, in the IUV, the expense budget of department D1 is modified to "520" (or \$520,000) and the row for D2 is deleted (i.e., it does not appear in the IUV). Non-matching rows in PT (department D3) are incorporated in the IUV without change. Non-matching rows in DT (department D4) are insertions into the IUV. Note that Fig. 2 does not make any assumption about the PT DM; DM can be a base table, any type of view (such as select/project, join, aggregate), or another IUV.

![](/api/attachments/75PNCQEC/fulltext/images/2d705035fdbee324375d3186d2e05f8008bcdfad6dadf6f79c9ed8c78761b13d.jpg)  
Fig. 1. Independently-updated views.

Parent Table DM

<table><tr><td>Dept No</td><td>Dept. Name</td><td>Manager</td><td>Budget</td><td>TS</td></tr><tr><td>D1</td><td>Sales-Corporate</td><td>John Smith</td><td>410</td><td>567</td></tr><tr><td>D2</td><td>Sales - Retail</td><td>Jane Adams</td><td>320</td><td>573</td></tr><tr><td>D3</td><td>Production</td><td>Sally Kiefer</td><td>330</td><td>801</td></tr></table>

Differential Table DIFF-DM

<table><tr><td>Dept No</td><td>Dept. Name</td><td>Manager</td><td>Budget</td><td>ACTION</td><td>TS</td></tr><tr><td>D1</td><td>Sales-Corporate</td><td>John Smith</td><td>520</td><td>mod</td><td>901</td></tr><tr><td>D2</td><td></td><td></td><td></td><td>del</td><td>903</td></tr><tr><td>D4</td><td>Design</td><td>Henry Field</td><td>600</td><td>ins</td><td>907</td></tr></table>

IUV DEPT-MGR

<table><tr><td>Dept No</td><td>Dept. Name</td><td>Manager</td><td>Budget</td><td>TS</td></tr><tr><td>D1</td><td>Sales-Corporate</td><td>John Smith</td><td>520</td><td>901</td></tr><tr><td>D3</td><td>Production</td><td>Sally Kiefer</td><td>330</td><td>801</td></tr><tr><td>D4</td><td>Design</td><td>Henry Field</td><td>600</td><td>907</td></tr></table>

Fig. 2. Sample IUV.

An IUV is a version of its parent table. Multiple versions of a PT are created by simply defining multiple IUVs with the same PT. Only their DTs are physically-stored. “Versions of versions” are created when the parent table of an IUV is another IUV. In general, “version hierarchies” are created when multiple IUVs are defined on the same parent table and each IUV is used as the parent table for other IUVs.

If the database is not read-only (i.e., is updatable), there are two sources of changes to an IUV: IUV updates and PT updates. A PT update to an IUV v is a database update to a table other than v that nonetheless causes a change to v. In the example, adding a new row to DM with department D5 will result in that row also appearing in DEPT-MGR. A PT update is automatically propagated to the IUV. In 2.6, we discuss update propagation in detail and introduce the problem of “overlapping updates” caused by PT updates to rows already modified in the IUV. The resolution of overlapping updates requires the modification (“refreshing”) of DT to reflect the desired outcome.

## 2.2. The structure of IUV, PT, and DT

We now describe the structure of the tables involved in an IUV. Consider first the PT. As mentioned earlier, PT can be either a base table, a view, or another IUV. In our example, the PT DM in Fig. 2 is a view derived from the base tables in Fig. 3. DM is obtained using the following SQL statement. The system column TS is automatically added by the DBMS.

<table><tr><td>CREATE VIEW</td><td>dm (deptno, deptName, manager, budget)</td></tr><tr><td>AS SELECT</td><td>d.deptno, d.deptName, e.empName, d.budget</td></tr><tr><td>FROM</td><td>depts d, emps e</td></tr><tr><td>WHERE</td><td>d.mgrno = e.empno</td></tr><tr><td>AND</td><td>region = 1.</td></tr></table>

If the PT is a view, it may be a virtual relation or a materialized view. If the PT is a materialized view, we assume its currency is maintained by a refresh procedure such as those in $[2,6,16]$ . Since all these procedures are semantically equivalent, they can all be applied to the maintenance of a materialized PT.

Following conventional semantics of the relational model, we assume that every relation has a primary key $[11]$ including views $[8]$ , and therefore PT has a primary key. The primary key serves to guarantee that each row represents an object about which information is stored in the database and that is uniquely and explicitly identified $[8]$ .

Tables in a database also contain system columns. System columns are not visible to the user (unless explicitly requested). They are added and manipulated automatically by the DBMS.

Base Table DEPTS

<table><tr><td>Dept No</td><td>Region</td><td>Dept. Name</td><td>Mgr No</td><td>Budget</td><td>TS</td></tr><tr><td>D1</td><td>1</td><td>Sales - Corporate</td><td>E100</td><td>410</td><td>567</td></tr><tr><td>D2</td><td>1</td><td>Sales - Retail</td><td>E230</td><td>320</td><td>428</td></tr><tr><td>D3</td><td>1</td><td>Production</td><td>E367</td><td>330</td><td>780</td></tr><tr><td>D11</td><td>2</td><td>Sales - Midwest</td><td>E175</td><td>40</td><td>689</td></tr><tr><td>D12</td><td>2</td><td>Warehouse</td><td>E412</td><td>150</td><td>483</td></tr></table>

Base Table EMPS

<table><tr><td>Emp No</td><td>Emp Name</td><td>Dept No</td><td>Salary</td><td>TS</td></tr><tr><td>E100</td><td>John Smith</td><td>D1</td><td>50,000</td><td>345</td></tr><tr><td>E150</td><td>Mary Jones</td><td>D1</td><td>30,000</td><td>602</td></tr><tr><td>E175</td><td>Beth Helms</td><td>D11</td><td>67,000</td><td>783</td></tr><tr><td>E200</td><td>Tom Myers</td><td>D2</td><td>45,000</td><td>574</td></tr><tr><td>E230</td><td>Jane Adams</td><td>D2</td><td>60,000</td><td>573</td></tr><tr><td>E310</td><td>Kim Burton</td><td>D3</td><td>25,000</td><td>605</td></tr><tr><td>E367</td><td>Sally Kiefer</td><td>D3</td><td>55,000</td><td>801</td></tr><tr><td>E390</td><td>Henry Field</td><td>D3</td><td>45,000</td><td>893</td></tr><tr><td>E412</td><td>Tim Falk</td><td>D12</td><td>48,000</td><td>515</td></tr></table>

Fig. 3. Base tables for sample IUV.

We assume that all tables have a system column TS showing the timestamp when the row was last inserted or modified (see [17] for a discussion of timestamps in DSS databases). Timestamps are used to detect overlapping updates. For derived tables, the timestamp of a row $\rho_{PT}$ in PT is the latest timestamp of the rows used to form PT. The first row of DM in Fig. 2 is obtained from the row for department D1 in DEPTS and the row for employee E100 in EMPS in Fig. 3. The timestamp is 567 since the row for department D1 has a later timestamp (TS = 567) than the row for the employee (TS = 345). For the second row in DM, the timestamp is taken from the EMPS row rather than from the DEPTS row since employee E230 has a later timestamp. For derived tables formed using aggregate functions such as SUM, the timestamp is the latest in the row subset used to compute an aggregate value.

DT is a physically-stored table that has the same columns as PT, including the timestamp, plus an additional system column ACTION. DT also has the same primary key as PT. A DT row represents the net effect of all updates made to an IUV row. At any time, there is at most one row in a DT for each row of its PT. For example, if an IUV row is modified and then deleted, only one row with del action appears in the DT. DT rows are modified as a result of: (a) user updates to the IUV and (b) the resolution of overlapping updates (discussed in 2.5).

An IUV is a virtual relation that has the same columns and the same primary key as its PT. For each IUV there is a corresponding DT. Multiple IUVs (and therefore DTs) can be defined on a single PT. The key is used to form the IUV by outer-joining the parent and differential tables, as explained in 2.3. The key also allows the DBMS to check for entity integrity (nulls, duplicates) at the time the IUV is formed. The key of an IUV must be explicitly given at the time of definition since the key of the PT may not be known to the DBMS. We note that most DBMSs and SQL implementations do not require key specifications on base tables. In cases where the key of the PT is known to the DBMS or it may be automatically determined, a check is made to detect conflicting definitions. This is the case with PTs that are: (a) base tables with DBMS-known primary keys, (b) updatable views on a base table with a DBMS-known primary key, (c) views obtained using aggregates (the grouping attributes form the key), or (d) IUVs.

## 2.3. Forming the IUV

The IUV is formed by: (1) obtaining the outer join of PT and DT, and (2) forming rows in the IUV based on the result of the outer join. These actions are performed together since the outer join brings to main memory all the necessary information. Additional processing to resolve overlapping updates, described in 2.6, is necessary when the underlying database is updatable.

The first action is straightforward. Conceptually, PT is retrieved and full outer joined with DT on the primary key. Fig. 4 shows the outer join of DM and DIFF-DM used to produce the IUV DEPT-MGR. A full outer join is performed because a “normal” (or inner) join would include only those rows from PT that match rows in DT; the full outer join includes non-matching rows in PT (rows not updated in the IUV) as well as non-matching rows in DT (rows inserted in the IUV). Note that physically PT may never be formed due to the DBMS query optimization. More specifically, “query modification” [37] translates the outer join and the query that defines PT to an equivalent algebraic expression on physically-stored tables.

The outer join produces rows that contain all the columns in both DT and PT. Then, forming the IUV involves choosing from the outer join the columns that will appear in the IUV. For non-matching rows of PT, i.e., rows not modified in DT (e.g. department D3), the columns from PT are used. For non-matching rows of DT, i.e., IUV insertions (e.g., department D4), the columns from DT are used. For matching rows, if the ACTION value is mod (e.g., department D1) the columns of DT are used; if the ACTION value is del (e.g., department D2), the corresponding row is not included in the IUV.

We conclude this subsection by commenting on primary key updates. Consider a row $\rho_{PT}\epsilon PT$ and a row $\rho_{DT}\epsilon DT$ , both with the same key value and representing the same real world entity. The outer join correctly generates a single row combining $\rho_{PT}$ and $\rho_{DT}$ . Modifying the key in either $\rho_{PT}$ (a PT update) or $\rho_{DT}$ (an IUV update) incorrectly causes two rows to be formed by the outer join. The problem of updates to keys is well documented in the literature [20,22]. It is a natural consequence of having user-defined keys as the main approach to object-identity in the relational model. This causes key updates to be semantically different from updates to non-key attributes. Since the key identifies the object or event described by the non-key attributes, a key update has the interpretation of “the non-key attributes here actually describe another real-world object or event” when in fact the intention may be “to correct a social security number that was entered incorrectly.” In his RM/T revision to the relational model, Codd [7] proposed the use of surrogates as a solution. The similar idea of object-identifiers is well established in object-oriented databases [1,22]. An alternative approach in SQL-92 uses primary and foreign key specifications to automatically propagate changes to a key throughout the database [27]. As these approaches affect only the mechanics of IUVs and not their semantics, we defer their detailed presentation to the appendix. Briefly, one can use an additional column(s) in DT for the key as it appears in the PT. This column is used in the outer join and is kept consistent with the database using key update propagations or triggers.

<table><tr><td colspan="5">columns from DM</td><td colspan="6">columns from DIFF-DM</td></tr><tr><td>Dept</td><td>Dept Name</td><td>Manager</td><td>Budget</td><td>TS</td><td>Dept</td><td>Dept Name</td><td>Manager</td><td>Budget</td><td>Action</td><td>TS</td></tr><tr><td>D1</td><td>Sales - Corporate</td><td>John Smith</td><td>410</td><td>567</td><td>D1</td><td>Sales - Corporate</td><td>John Smith</td><td>520</td><td>mod</td><td>901</td></tr><tr><td>D2</td><td>Sales - Retail</td><td>Jane Adams</td><td>320</td><td>573</td><td>D2</td><td>----</td><td>----</td><td>---</td><td>del</td><td>903</td></tr><tr><td>D3</td><td>Production</td><td>Sally Kiefer</td><td>330</td><td>801</td><td>---</td><td>----</td><td>----</td><td>---</td><td>----</td><td>----</td></tr><tr><td>----</td><td>----</td><td>----</td><td>---</td><td>----</td><td>D4</td><td>Design</td><td>Henry Field</td><td>600</td><td>ins</td><td>907</td></tr></table>

Fig. 4. Outer join of DM and DIFF-DM.

Another problem related to keys is the violation of the “entity integrity” rule $[12]$ . This occurs when a null value is assigned to the primary key of any row or when two rows have the same primary key value. Entity integrity is typically assumed in relational databases. However, in most DBMSs a key specification is not required for base tables and therefore it is possible to encounter invalid rows. For this reason, we establish the following semantics for entity integrity violations: (1) any row whose primary key has a null value is ignored and does not appear in the IUV, and (2) whenever two or more rows have the same primary key value, the row with the latest timestamp is used and the other is ignored.

## 2.4. Updating IUVs

For updating, users treat an IUV just like a base table. Updating (modifying, inserting, deleting) an IUV row means that, on retrieval, the row will appear updated (modified, inserted, deleted) as intended. As the name “independently updated view” indicates, IUV updates are independent of the base tables from which the IUV is derived. The express purpose of updating an IUV is to change only that IUV and not to affect the underlying base tables. This is different from the traditional view updating where a view is updated with the purpose of making changes to the underlying database.

Before an IUV is updated, it is identical to its PT and its DT is empty. Updates to an IUV are translated into changes to its DT so that when the IUV is retrieved it reflects the updates. When an IUV row is updated (inserted, modified, deleted), a check is made for the existence of a DT row with the same key value. Table 1 shows the processing of each type of IUV update given the ACTION code in the corresponding DT row.

Table 1  
Processing of IUV updates

<table><tr><td rowspan="2">ACTION code in the DT row</td><td colspan="3">IUV update and its effect on DT</td></tr><tr><td>Insertion</td><td>Modification</td><td>Deletion</td></tr><tr><td>no DT row</td><td>Insert a new DT row with  $ACTION = ins$  if no row with that key exists in PT. Reject otherwise.</td><td>Insert a new row with  $ACTION = mod.$ </td><td>Insert a new row with  $ACTION = delete.$ </td></tr><tr><td>mod</td><td>Reject. Row with same key already exists in the IUV.</td><td>Replace DT row with a new row with  $ACTION = mod.$ </td><td>Replace DT row with a new row with  $ACTION = del.$ </td></tr><tr><td>ins</td><td>Reject. Row with same key already exists in the IUV.</td><td>Replace DT row with a new row with  $ACTION = ins.$ </td><td>Replace DT row with a new row with  $ACTION = del.$ </td></tr><tr><td>del</td><td>Replace DT row with a new row with  $ACTION = mod.$ </td><td>Reject. Row with this key does not exist in IUV.</td><td>Reject. Row with this key does not exist in IUV.</td></tr></table>

Note that the classical view update problem of $[4,14]$ does not arise in the case of IUVs. This problem occurs when view updates cannot be automatically mapped to the corresponding base tables. IUVs do not present the view update problem because the IUV is treated as a base table and updates are mapped to the DT and not to the underlying database. The difficulty of mapping view updates to base tables is the reason that most DBMSs support updates only for views that are row or column subsets of a single base table $[27,10]$ . However, some front-end systems allow definition of views based on joins. INGRES supports “JoinDefs” that define a join, typically those which join a primary key to a foreign key $[33]$ . A JoinDef can be used with the forms-based front-end for updates but not directly with SQL or QUEL, the INGRES query languages. Microsoft Access supports updating of some join queries (“dynasets”) $[26]$ . Other approaches to extending view updatability that have not been incorporated in commercial DBMSs include a “complementary view” $[4,9]$ , Keller’s intelligent assistant that helps to define mappings at view definition time $[19]$ , and the capture of semantic information at both view definition and view update time $[24]$ . Unlike IUVs, all these approaches are designed to update the database through views.

IUVs share the row disappearance problem with views. This problem arises when a row is changed in such a way that it “disappears” from the view because it violates the view definition. Consider a view defined as a selection where sales >10,000 and a view update that changes the sales amount in a row from 17,000 to 9,000. This row disappears from the view since it no longer satisfies the selection criterion. In SQL systems, the WITH CHECK OPTION [12,23,27] is used to prevent these view updates by rejecting any change that would violate the predicate in the WHERE clause of the view definition. We assume a similar mechanism for IUVs.

## 2.5. IUVs on updatable databases

If an IUV is defined on a database that is not read-only, changes in the database are automatically propagated to the IUV. Database updates are either: (1) PT updates, i.e. those that affect the PT of an IUV, or (2) irrelevant updates, i.e., those that have no effect on the PT (see [6] for a discussion on irrelevant updates). In the case of the IUV DEPT-MGR, an update to a department in region 1 in the base table DEPTS is a PT update. Whereas any update to a department in region 5 is irrelevant since it has no effect on the state of PT. Irrelevant updates do not affect an IUV and are not discussed any further. Note that an update that changes a department from region 1 to region 5 is not irrelevant since it affects the PT. Its effect is to delete that department from PT.

The interaction of IUV and PT updates can lead to overlapping updates. Consider the row for department D1 in the PT DM of Fig. 2. The dept.

<table><tr><td>Time</td><td>EVENT</td><td>EFFECT</td><td>NOTES</td></tr><tr><td> $t_0$ </td><td>An IUV is defined on a PT.</td><td>DT is an empty table.</td><td>IUV is identical to its PT.</td></tr><tr><td> $t_1$ </td><td>The IUV is updated.No updates are made to the database.</td><td>IUV is not the same as at  $t_0$ . IUV updates are stored in the DT which is no longer empty. PT is the same as at  $t_0$ .</td><td>IUV is different from its PT. Overlapping updates do not exist.</td></tr><tr><td> $t_2$ </td><td>Database is updated.</td><td>Database updates may affect the PT.Some of the affected PT rows may have been updated in the IUV at  $t_1$ .</td><td>IUV is different from its PT. Overlapping updates may exist.</td></tr></table>

Fig. 5. A sequence of IUV and database updates.

budget “410” is modified in the IUV to “520.” This update can be interpreted as “increase the dept. D1 expense budget from \$410,000 to \$520,000.” If the PT is read-only, the original budget (“410”) will never change and therefore this interpretation will always remain valid. However, if PT is not read-only, it is possible for the value “410” in the PT DM to be updated to, say, “540.” In that case, the IUV update now has the meaning “decrease the dept. D1 expense budget from \$540,000 to \$520,000.” Since this may not be what the decision maker intended, a problem has been created.

Fig. 5 shows a sequence of IUV and PT updates leading to overlapping updates. At time $t_{0}$ , the IUV is identical to its PT. At time $t_{1}$ the IUV is updated; the database does not change. The IUV and its PT are no longer identical. At time $t_{2}$ , the database is updated. At this time, a PT update is: (i) an overlapping update if it changes a PT row already modified in the IUV or (ii) a non-overlapping update if it changes a PT row that has not been modified in the IUV.

More precisely, given an IUV and its PT and rows $\rho_{IUV}\in IUV$ and $\rho_{PT}\in PT$ with the same key value, a PT update is an overlapping update if (1) at time t, an IUV update modifies or deletes $\rho IUV$ , and at time $t',t'>t$ , the PT update modifies or deletes $\rho_{PT}$ , or (2) at time t, an IUV update inserts $\rho_{IUV}$ such that no $\rho_{PT}\in PT$ exists with the same key value, and at time $t',t'>t$ , the PT update inserts $\rho_{PT}$ with the same key value.

Overlapping updates cause inconsistencies between an IUV and its PT, temporarily making the IUV invalid. Overlapping updates must be resolved so that the IUV can be constructed as per the intended changes. We define the following policies to that effect; each policy reflects a different intent.

\- Policy 1: IUV updates prevail over PT updates; an overlapping update is not reflected in the IUV. A PT row is considered to be a basis or an assumption that is valid only as long as it is not changed by an IUV update. The user intends the change made to an IUV to be permanent, only to be affected by further IUV updates. Subsequent PT updates should not affect the user's intentional changes.

\- Policy 2: PT updates prevail over IUV updates. An IUV update is valid only as long as the original information remains unchanged. Any update of a PT row subsequent to an IUV update of the same row is reflected in the IUV. Thus, updating a PT row that has been earlier modified in the IUV renders the IUV update ineffective.

The policies do not differ on the treatment of both non-overlapping PT updates and IUV updates of rows not affected by later PT updates. Both types of updates are treated in the same manner under the two policies.

## 2.6. Detecting and resolving overlapping updates

An overlapping update is detected whenever an IUV row is accessed (either for update or retrieval) by comparing the PT and the DT. The procedure, shown in Table 2, uses the ACTION value in the DT row and the timestamps d and p of matching DT and PT rows, respectively. The shaded cells in Table 2 show the types of overlapping updates. Consider the insert/insert cell, i.e., an overlapping updated caused by the insertion of an IUV row followed by an insertion of a PT row with the same primary key value. The IUV insertion creates a DT row with timestamp d and ACTION ins. The subsequent PT row insertion creates a PT row with timestamp p > d. The overlapping update is detected by the condition ACTION = ins and p > d. Similarly, the modify/delete cell represents an IUV modification followed by a PT deletion that is detected by the condition ACTION = mod and “no PT row.”

Table 2  
Detecting overlapping updates

<table><tr><td rowspan="2">DT ACTION value</td><td colspan="3">Timestamps of matching DT and PT rowsd = DT timestamp, p = PT timestamp</td></tr><tr><td>No PT row</td><td>p ≥ d</td><td>p &lt; d</td></tr><tr><td>ins</td><td>no overlapping update</td><td>insert / insert</td><td>no overlapping update</td></tr><tr><td>mod</td><td>modify / delete</td><td>modify / modify</td><td>no overlapping update</td></tr><tr><td>del</td><td>delete / delete</td><td>delete / modify</td><td>no overlapping update</td></tr></table>

Once detected, an overlapping update is resolved according to one of the two policies discussed in 2.5. For each overlapping update, the DT is changed to reflect the resolution. Consider the insert /insert overlapping update. For Policy 1 IUVs, an IUV update prevails over a subsequent PT update. Hence, the resolution results in keeping the inserted IUV row by changing the ACTION in DT from ins to mod. In addition, the timestamp of the DT row is made current $d \leftarrow t$ to reflect that the conflict has been resolved.

For Policy 1 IUVs, the actions to resolve the overlapping updates are:

\- for modify / delete overlapping update: Make $d \leftarrow t$ . Change ACTION to insert.

\- for delete / delete overlapping update: Make $d \leftarrow t$ .

\- for insert /insert overlapping update: Make $d \leftarrow t$ . Change ACTION to modify.

\- for modify / modify overlapping update: Make $d \leftarrow t$ .

\- for delete / modify overlapping update: Make $d \leftarrow t$ .

For Policy 2 IUVs, PT updates prevail over the IUV updates. Hence, an overlapping update is resolved by nullifying the effect of the IUV update. This is done by deleting the corresponding DT row.

Regardless of policy, overlapping updates are checked and detected only when the IUV row is accessed. A consequence of this is that multiple database updates affecting the same row in the PT between two IUV accesses are treated as a single update. Therefore, the situations in Table 2 may occur as a result of one or more database updates. For example, the overlapping update “insert/insert” may be the result of one insertion of a row in the PT, or an insertion followed by a modification of the same row. Multiple database updates do not affect the tests for detecting overlapping updates.

Note that IUVs require no overhead for database (e.g. PT) updates since it is not necessary to monitor, separately store, or propagate database updates as they occur. A processing cost occurs only when the IUV is accessed. Also note that the cost of processing the overlapping updates is minimal since the DT rows are already in main memory (for forming the IUV rows). The major cost is for writing back the refreshed DT and it therefore depends mainly on the size of the DT and the extent of overlap. In normal IUV applications, the DT is not expected to be very large because it stores only the difference between the PT and the DT.

## 2.7. Prior research

The notion of IUVs was introduced in $[32]$ which focused only on the retrieval aspects and did not discuss IUVs on dynamic databases or multiple base tables (e.g. PTs defined using joins). The Oracle DBMS was used to evaluate retrieval times for IUVs defined using selection and aggregation of single base tables. $[32]$ is most closely related to portions of Section 3 which generalizes $[32]$ with implementation-independent analytical expressions and different file structures for IUVs based on selections, joins, and aggregates. The cost of refreshing the differential file is also studied in Section 3 for the first time.

The propagation of PT updates to IUVs is similar to the refreshing of snapshots. Snapshots differ from IUVs in that they are read-only tables that cannot be updated; a snapshot is a read-only materialization of a view $[2]$ . Snapshots avoid the cost of generating a view every time a query is made on the view. To maintain consistency with the original data, snapshots need to be “refreshed” (i.e., regenerated) periodically to reflect updates made to the database $[2,6,16,25]$ . The periodic regeneration of Adiba and Lindsay $[2]$ does not require any modifications to the update mechanism to base tables. Thus, it can be easily be implemented on an existent DBMS. A variant by Segev and Park $[35]$ uses a differential file to propagate updates to several materialized views. Unlike IUVs, the mechanism of $[35]$ adds overhead to database updates by requiring every update to a base table to create a new row in the differential file.

The notion of differential tables to support multiple versions of a relation has been used for hypothetical relations (HRs) $[3,38–40]$ and derived relations with exceptions (DREs) $[13,30]$ . Both HRs and DREs differ from IUVs in that they cannot be kept consistent when they are defined on non read-only tables. DREs allow versions to be defined on an arbitrary view $[30,31]$ as IUVs do. However, HRs can only be defined on a single read-only base table; they do not allow versions to be created based on derived data, such as summary data or data derived from multiple base tables.

## 3. Processing costs

To evaluate the processing costs of IUVs, we derive generalized analytical cost expressions for their retrieval. These cost expressions can then be used to estimate the performance of IUVs under various operating conditions and hardware configurations. We consider commonly used views (select/project, join, and aggregate) that have been used in similar studies in the context of view materialization strategies $[16,6]$ .

To assess the performance of IUVs, we compare the cost of an IUV (IUV-cost) with the cost of retrieving just its parent table (PT-cost). This is a very conservative estimate since IUVs by definition involve more processing. However, as the results show, IUV costs are reasonably close to PT costs in most cases. We define %IUV-cost as 100 x (IUV-cost - PT-cost)/PT-cost.

We assume that a primary clustered B + tree index is available on the physical tables. Such indexes can be useful in retrieving both the view and the corresponding IUV, as well as for updating the relations and the DT. Only complete retrievals of the IUV are considered. The following parameters are used in the cost expressions:

$N_{i}$ Number of rows in relation $\mathbf{R}_{i}$

$P_{i}$ Number of blocks occupied by relation $\mathrm{R}_{\mathrm{i}}(P_{i}=\lceil N_{i} tsize/B\rceil)$ where B=block size;
tsize = row size

$f_{pt}$ View or PT predicate selectivity $(N_{pt} = f_{pt}N_i)$

$f_{dt}$ Fraction of PT changed by DT $(N_{dt} = f_{dt}N_{pt})$

$f_{ref}$ Fraction of DT refreshed between every IUV retrieval due to overlapping updates

$C_{1}$ Average Rotational Delay

$C_{2}$ Average I/O cost to read/write a block randomly

To construct an IUV, its PT and DT are retrieved and joined. In addition, DT is refreshed to resolve overlapping updates since the last access to the IUV. This involves modifying the relevant DT rows and writing them back. We assume that CPU operations (such as screening, comparing, computing) are carried out simultaneously with the I/O operations because of double buffering. The cost to construct an IUV can be broken down into the following three components: $IUV-cost = cost$ to retrieve PT (Hp) + cost to retrieve DT (Hd) + cost to refresh DT (Hr).

## 3.1. Select / project IUVs

Parent tables of these IUVs are formed using a relational algebra selection and projection on a relation $R_{1}$ . The selection applies a predicate with selectivity $f_{pt}$ to a subset of the attributes of $R_{1}$ . Selected rows are projected according to the attributes in the view's definition. We assume that the primary key of $R_{1}$ is preserved by the projection.

To retrieve the parent table, the entire relation $R_{1}(P_{1}$ blocks) is read using a clustered scan, each block requiring one disk access. Rows are screened against the view predicate and projection is carried out as they are read. Therefore, the estimated retrieval cost of the parent table is $Hp = C_{2}P_{1}$ .

The retrieval cost of DT, Hd, is the cost to read the $P_{dt}$ blocks of DT, also using a clustered scan. Hence, $Hd = C_{2}P_{dt}$ . Since both PT and DT are formed using a clustered scan, their rows are available in order by primary key and the join requires only a single pass over the two relations, without any additional I/O.

Hr, the cost to refresh the differential table, consists of the cost to update (modify or delete)

$f_{ref}N_{dt}$ rows of DT in place. In terms of the number of blocks, this works out to $y(N_{dt},P_{dt},f_{ref}N_{dt})$ , where the function $y(n,m,k)$ estimates the number of blocks touched when accessing k out of n records in a file occupying m blocks [41]. Therefore, $Hr = 2C_1 \times y(N_{dt},P_{dt},f_{ref}N_{dt})$ , where $2C_1$ is the additional time for one complete rotation of the disk needed for writing back a block in its original location after it is read; no seek time is needed [34]. Thus, IUV-cost (select/project) = $C_2P_1 + C_2P_{dt} + 2C_1 \times y(N_{dt},P_{dt},f_{ref}N_{dt})$

## 3.2. Join IUVs

These IUVs have parent tables formed using a natural join of two relations, $R_{1}$ and $R_{2}$ . For generality, join views may also include selection and projection operations. We assume that the selection restricts $R_{1}$ with selectivity $f_{pt}$ and that every row of $R_{1}$ joins to exactly one row of $R_{2}$ . This is a very common join in practice, occurring when an attribute d is the primary key of $R_{2}$ and a foreign key in $R_{1}$ . We assume the simple hash join algorithm of [29] with $R_{2}$ read first. As $R_{2}$ is read, a hash index is formed in memory. $R_{1}$ is read and joined with $R_{2}$ using the hash index. The join requires only one pass over $R_{1}$ and $R_{2}$ if the hash index can be fully accommodated in memory (in our study, $R_{1}$ had a size of 100,000 rows and $R_{2}$ a size of 2,000; much larger tables can be accommodated). Therefore, $Hp = C_{2}P_{1} + C_{2}P_{2}$ . The cost expressions for the other components of IUV-cost of these IUVs, Hd and Hr, are the same as those of select/project views. Hence, IUV-cost (join) = $C_{2}P_{1} + C_{2}P_{2} + C_{2}P_{dt} + 2C_{1} \times y(N_{dt}, P_{dt}, f_{ref}N_{dt})$ .

## 3.3. Aggregate IUVs

The PT of an aggregate IUV is formed using one or more aggregate functions such as SUM, AVG, or COUNT on a single relation $R_{1}$ . A subset of the attributes of $R_{1}$ serves as the aggregation attributes. The PT is formed by reading the entire relation $R_{1}$ and computing the aggregate in one pass over the $N_{1}$ rows of $R_{1}$ . We assume that as each row is scanned, a hash index is built in memory and the values of the aggregation attribute are computed simultaneously. Hence the cost of retrieving the aggregate view, $Hp = C_{2}P_{1}$ . The hash index on the PT can also be used for joining the PT and the DT. Note that the primary key of an aggregate view is formed by the aggregation attributes. The remaining components of IUV-cost, the cost to retrieve DT, Hd, and the cost to refresh DT, Hr, have the same expressions as in the earlier cases. Therefore, IUV-cost (aggregate) = $C_{2}P_{1} + C_{2}P_{dt} + 2C_{1} \times y(N_{dt}, P_{dt}, f_{ref}N_{dt})$ .

## 3.4. Results

Table 3 summarizes the performance of IUVs for the three view types using the following parameter values: $N_{1}=100,000$ tuples, $N_{2}=200$ tuples values, tsize=100 bytes, B=4000 bytes, $C_{1}=8$ ms, $C_{2}=25$ ms.

We considered three values of $f_{pt}$ (0.1, 0.2, and 0.3) representing views that are subsets of base tables (i.e., up to 30% of the size of the base tables). For the differential tables, we considered a range of values for $f_{dt}$ . This range represents IUVs that differ by 20% to 40% from their parent tables. We believe that these parameter values cover views that are typically used for supporting managerial decision-making. The $f_{ref}$ value of 0.0 represents a read-only or a static database; there are no overlapping updates and hence there is no cost to maintain the DT. On the other hand, the $f_{ref}$ value of 0.5 represents a extremely dynamic database where 50% of the DT tuples are affected by overlapping updates between every IUV access.

Table 3
Performance results

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">%IUV-cost</td></tr><tr><td> $f_{pt}=0.1f_{dt}$ range 0.2–0.4</td><td> $f_{pt}=0.2f_{dt}$ range 0.2–0.4</td><td> $f_{pt}=0.3f_{dt}$ range 0.2–0.4</td></tr><tr><td rowspan="2">Select/project</td><td> $f_{ref}=0.0$ </td><td>2.0%--4.1%</td><td>4.1%--8.1%</td><td>6.1%–11.8%</td></tr><tr><td> $f_{ref}=0.5$ </td><td>3.4%--6.4%</td><td>6.4%--13.2%</td><td>10.0%–19.6%</td></tr><tr><td rowspan="2">Join</td><td> $f_{ref}=0.0$ </td><td>2.0%--4.0%</td><td>4.0%--7.6%</td><td>6.0%–11.6%</td></tr><tr><td> $f_{ref}=0.5$ </td><td>3.3%--6.3%</td><td>6.3%--12.9%</td><td>9.6%–19.2%</td></tr><tr><td rowspan="2">Aggregate</td><td> $f_{ref}=0.0$ </td><td>2.0%--4.1%</td><td>4.1%--8.1%</td><td>6.1%–11.8%</td></tr><tr><td> $f_{ref}=0.5$ </td><td>3.4%--6.4%</td><td>6.4%--13.2%</td><td>10.0%–19.6%</td></tr></table>

The results show that the $\% IUV$ -cost is less than $20\%$ of the cost of retrieving the corresponding view for all the three types of views. Over a major portion of the range, the $\% IUV$ -cost is well below $10\%$ . For smaller values of $f_{pt}$ , the $\% IUV$ -cost would be even lower. Thus, in most cases a user would feel no appreciable difference between running a query on a conventional view or on an IUV. For aggregate IUVs, where aggregate functions result in a parent table that is substantially smaller than the original tables, this is particularly true. We also found that the cost of processing overlapping updates tapers of as $f_{ref}$ increases beyond a certain limit ( $f_{ref} = 0.5$ represents an extreme) because of the nature of the $y(n, m, k)$ function [41].

## 4. Derived data in decision-support systems

This section discusses support for derived data in decision support systems using the summary requirements listed in Table 4. These requirements are classified as: (1) derivation transparency, (2) the ability to build multiple versions or scenarios, (4) automatic maintenance of consistency, and (3) control over the time of derivation. For each requirement, the support given by IUVs is described. The section concludes with a comparative summary of other mechanisms for derived data.

## 4.1. Derivation transparency

Ideally, a relational database system should allow users to treat all tables identically, regardless of whether they are physically-stored or not. We refer to this capability as derivation transparency. In practice, DBMSs significantly restrict the user's ability to manipulate derived data, causing decision makers to manipulate the database in ways that are unnatural to the application.

Fig. 6 helps explain derivation transparency in relational databases. Fig. 6(a) shows a database that appears to programmers and end-users as a collection of views and base tables. If views V1 and V2 are updatable, the user schema for Fig. 6(a) consists of tables B1, V1, and V2. On the other hand, if V1 and V2 are not updatable, then the user schema must also include tables B2–B4 to support updates. Thus, the lack of derivation transparency forces users to manipulate tables that do not provide additional information. While in many cases, a decision maker may utilize views for retrieval and have a programmer write the routines for correct updating, this is an unnecessary complication. Fig. 6(b), on the other hand, shows a database in which all tables in the user schema can be treated identically, regardless of whether they are derived or base tables.

We make a further distinction between data that is derived from the user point of view (“logically-derived data”) and data that is derived from the database point of view (“physically-derived” data). From a relational database viewpoint, data is either stored in base tables (base data) or it is physically-derived. Base data is obtained from the outside world through direct measurement or observation such as names, product prices, and salaries. On the other hand, data is physically-derived because of choices in the database design. Data stored in two base tables (often as a result of normalization) but retrieved as one table for ease of use, is an example of physically-derived data. Another example of physically-derived data is the use of a copy of the table PRODUCT placed in Houston to avoid the communication costs of accessing the original table in Hong-Kong.

From a user's point of view, data is either primitive or logically-derived. Primitive data is data that is treated by an application as if it were obtained directly from the outside world and not derived from any other data in the database. In actuality, primitive data may be base data or physically derived. By contrast, data is logically-

derived as a consequence of its basic nature or definition and corresponds to averages, summations, and the result of formulas such as “quantity times price." Generally, it is meaningful for an application to update data that it deems as primitive.

Table 4  
Desirable support for derived data

<table><tr><td>Capability</td><td>Description</td><td>Necessary support</td></tr><tr><td>Derivation transparency</td><td>Users should manipulate derived and base data in the same way, unless required by the application.</td><td>Table updatability should not be determined by storage form.</td></tr><tr><td>Multiple versions</td><td>Necessary for what-if analysis, historical and backup copies of files, and versions of programs.</td><td>Database systems should explicitly (a) identify a table as a version of another, and (b) avoid duplication of data between versions.</td></tr><tr><td>Data consistency</td><td>Version changes should not affect other versions. Global changes should be automatically detected and treated according to user policies.</td><td>Automatic maintenance of consistency for derived data and versions.</td></tr><tr><td>Derivation control</td><td>Derived data should be recomputed only when cheaper than explicit storage, to increase derivation transparency and to facilitate use.</td><td>Allow different choices for materialization depending on costs of recomputation and storage.</td></tr></table>

![](/api/attachments/75PNCQEC/fulltext/images/cdd7ff83c97b81c9491755279adf323c7ac744a3402521139ab644df2f35a4cc.jpg)  
Fig. 6. Derivation transparency. (a) Current relational databases. (b) Relational databases with full derivation transparency.

The distinction between primitive and logically-derived data is application dependent, and not an absolute property of a data item. Consider two cases. (1) Different levels of aggregation: from a CEO's point of view, when budgeting for various divisions' expenses, each division's total salaries is a primitive item. However, a divisional application treats that division's total salaries as the aggregate of salaries of that division's personnel, e.g. a logically-derived item. (2) Different uses of the data: product cost in a manufacturing company may be a logically derived item for production engineers (sum of part and labor costs). At the same time, it may be a primitive item for accounting personnel who manipulate the combined product cost as a single value for adjusting the value of inventory for inflation.

Since many classes of conventional views (especially aggregate views which are often used in managerial/strategic decision-making) cannot be updated, an application cannot modify data that it deems as primitive but is actually physically-derived. The IUV mechanism, as opposed to conventional views, provides derivation transparency by allowing users to update primitive data (in the form of IUVs) regardless of its storage form (base or derived). When an IUV is accessed, its PT is retrieved, any derived fields are computed, and the IUV updates are applied regardless of whether the original values were physically stored or derived. For example, in a what-if analysis, given a derived table summarizing the number of employees per department, a manager may wish to change the number of employees in a department from 11 to 10 without necessarily making the choice (at this point) of the particular employee to be dismissed. Retail sales provide another example. A store may give a discount on the total invoice amount rather than modifying the unit price of individual products.

By providing derivation transparency, IUVs treat updatability correctly as a semantic issue rather than as a physical constraint. A data item is updatable if it is a primitive item for a particular application. The same item can be treated as primitive and updatable for some applications, and as derived and non-updatable for others.

## 4.2. Multiple versions

Multiple versions are necessary to support what-if scenarios and different interpretations of the same data. Versions go beyond simply being different “windows” to the database, as views are. The difference lies primarily in the treatment of changes to the data. Updates made through one view (or “window”) are mapped to the base tables and affect all other views on the same data. Updates to a version, on the other hand, affect only that particular version and are not visible in any other version.

Without explicit support for multiple versions, users are forced to make copies of the data, and then manipulate each copy independently. Multiple what-if scenarios result in multiple copies of mostly the same data. In many cases a version differs from the original data or from another version only on a few values. This not only results in waste of storage space, but requires additional effort from the decision-maker to manage the multiple copies. No indication exists in the system that the new tables are copies or versions of other tables.

Support for versions, according to Katz and Lehman [18], requires (a) minimum redundancy, with only changed records stored in the new version, (b) that all versions can be accessed, and (c) that all records in a version can be accessed. The existence of specific mechanisms to create and access (“reference”) versions is emphasized in the IRIS System [5,15]. In ORION, version hierarchies can be defined, rather than simple linear versions of versions [21].

IUVs provide basic support for multiple versions. As with IRIS, IUVs provide explicit support for versions and establish the relationships between tables and their versions. All IUVs and all rows in an IUV are accessible to the user; however, access can be restricted following standard SQL practice. Version hierarchies are created by defining IUVs whose PTs are also IUVs. Minimum redundancy is obtained by storing only changed rows in the DT.

IUVs also provide the ability to identify and separate versions from other information. Any implementation of IUVs will store information about IUVs in the system catalog, explicitly identifying IUVs as separate from base tables and views. For example, the system table SYSTABLES in DB2 [10] indicates whether the table is a base table or a view. Another system table would indicate the parent table of an IUV and other specifics of the IUVs.

Version hierarchies are formed by using an IUV as the parent table. Any version in the hierarchy can be accessed. In particular, versions in a sequence of versions can be accessed if the names of the versions are known or by tracing the hierarchy in the system catalog.

The basic capabilities of IUVs for version management can be enhanced to build ad hoc and more comprehensive support. For example, the “merging” of versions can be done by combining the differential tables. A version hierarchy may be “collapsed” by merging sequential versions. The differential tables provide a record of the changes used to build a version.

## 4.3. Database consistency

Data consistency is a critical issue in databases. It guarantees that all users receive the same information for the same real world entity. Consistency is equally significant when multiple versions and derivation transparency are supported. However, a version is intended to be different from the original data. We use the notion of “intent” to define the concept of version consistency.

Conventionally, data are consistent if two data items representing the same fact have exactly the same value. Thus, if “Mary Doe” had January sales of \$15,000 and there are database tables A and B with this information, both tables need to have exactly \$15,000 to be consistent. The two tables need not be base tables; table A may be a base table with one rows for each sales transaction, while table B may be a view with one row per salesperson. The value \$15,000 appears as one data item in table B and as several in table A that together add up to \$15,000.

The conventional notion does not help in dealing with versions and alternative what-if scenarios which introduce differences by definition. Therefore we differentiate version differences from those that create inconsistencies. Before attempting a definition consider the following cases. First, a sales manager may create a what-if scenario where “Mary Doe” has sales of \$17,000 while the actual sales are still \$15,000. Since the sales manager is purposely introducing a difference to the actual sales, the version is deemed consistent. In other cases, a difference in the version is a true inconsistency. One case is when the user mistakenly believes that the version represents actual data or is not aware of the intention behind the version. This occurs because of the user’s interpretation of the version. Another case is when the data on which the version is based changes as the database is updated. These database changes must be either reflected in the version or it should be recognized that these changes do not affect the version; in both cases the version “acknowledges” the changes in the database. If the version is incognizant of the changes to the data on which it is based, the version becomes inconsistent.

We define two conditions for version consistency: (1) there must exist at least two versions of the same data item, one of which is identified as the “original data” and the others as “versions,” and (2) there must be a mapping from the original data to each version. Condition 1 eliminates the case of (possibly incorrect) database design where users are not aware that the same data item is stored independently in several locations. Condition 2 establishes the fact that differences created when versions are updated do not cause inconsistency; inconsistency may arise only when the original data is modified. This is so because the purpose of updates to a version is to modify data as it originally existed. An update to a version only re-establishes the mapping between the original data and the version; the version is still consistent. The user is (or should be) fully aware of the change. A version can become inconsistent if this mapping is destroyed. This can happen if the original data is updated and the mapping is not re-established. Our definition of version consistency subsumes data consistency, in that data are assumed to be consistent in the conventional sense.

IUVs meet Condition 1 automatically since an IUV, by definition, is a view (a version) on some base tables, and it is explicitly labeled as a version. Condition 2 is met because the mapping between the original data and an IUV is maintained at all times. A change in the original data that affects a previous IUV updates is detected as an overlapping update whenever the IUV is accessed. The overlapping update is resolved by modifying the DT to reflect the new mapping. For Policy 1 IUVs, the DT modification has the effect of intentionally ignoring the database changes in the version. For Policy 2 IUVs, the effect is propagation of the changes to the version.

In practical terms, support for data consistency in IUVs means that a version or a what-if scenario can be defined on “live” databases in active use. It is not necessary to make a copy of the database at some point in time and use this copy as the basis for scenarios. For example, in planning a payroll budget, a version can be defined based on the payroll data of May 1993. The different policies allow the budget planner to (a) treat the payroll data as “frozen” as of May 1993, thus ignoring for planning purposes all actual payroll changes after May, or (b) automatically detect changes occurring after May and incorporate them to the new budget as they occur. Using “live” databases provides more realistic scenarios and simplifies application development as copies and updates are automatically managed by the system.

The extended notion of consistency introduced here applies in other areas. Copies made for back-up purposes are one example. A month-old copy of the table PAYROLL (i.e., a snapshot) that does not include changes made in the current month is an inconsistent copy only if its users are unaware that no changes are included. In the earlier example of a retail store maintaining a local version of a global price list in a distributed database, the local version is prepared by intentionally modifying specific items' values in the current global price list. Changes to the global price list can cause the version to be inconsistent unless the changes are reflected in the version or are intentionally ignored.

## 4.4. Control over derivation

Derivation control is an efficiency concern as it mostly affects response time. An ideal system gives the database administrator the choice of storing derived data or recomputing it every time it is needed. Virtual relations are recomputed every time they are needed. A view may be materialized if the cost of storage is lower than the cost of recomputation. In processing environments that are heavily loaded with on-line updates, a materialized view is expensive to maintain. On the other hand, if the database is read-only or seldom updated, a materialized view may be cost-effective. Not only the time to form the view is eliminated, but indexes and clustering techniques can be applied to the materialized view to further improve the response time. Hanson [16] found that the choice of whether to materialize or not is highly application-dependent.

Table 5  
Comparison of support for derived data

<table><tr><td></td><td>Derivation transparency</td><td>Multiple versions</td><td>Data consistency</td><td>Derivation control</td></tr><tr><td>Virtual relations</td><td>for retrieval only, not for updates</td><td>not supported</td><td>single copy of data accessed</td><td>recompute whenever accessed</td></tr><tr><td>Snapshots</td><td>for retrieval only, not for updates</td><td>not supported</td><td>single copy of data, may be inconsistent until refreshed</td><td>store materialized copy and refresh periodically</td></tr><tr><td>Hypothetical relations</td><td>no derived data, exact copy of a single base table</td><td>supported only for single table</td><td>original data must be read-only</td><td>recompute whenever accessed</td></tr><tr><td>DREs</td><td>supported</td><td>supported</td><td>original data must be read-only</td><td>recompute whenever accessed</td></tr><tr><td>IUVs</td><td>supported</td><td>supported</td><td>original data can be modified</td><td>option of materialized copy or recompute whenever accessed</td></tr></table>

IUVs provide derivation control by allowing the PT to be a virtual relation or a materialized relation, and thus giving users the control over whether PT is recomputed each time it is needed, or computed once and stored for fast retrieval. To maintain the currency of the materialized PT, any of the mechanisms proposed in the literature can be used as noted in 2.7. An easy to implement solution is a complete regeneration of the PT periodically or on demand, as suggested in [2]. Other solutions are more efficient, such as those that capture each database update and use it to refresh the materialized view [6,16] but require modifications to the DBMS.

## 4.5. Comparison with other proposals for derived data

We conclude this section with a brief comparison between IUVs and other proposals for derived data in the literature. Table 5 compares IUVs, virtual relations, snapshots, hypothetical relations (HR), and derived relations with exceptions (DRE). IUVs can be regarded as a logical superset of those proposals. If the database is not updatable, then an IUV behaves like a DRE. If, in addition, the parent table is restricted to be a base table, the IUV behaves like an HR. In the case of HRs and DREs, since the database cannot be updated, the question of version consistency does not arise, but the use of versions becomes less flexible. Moreover, an HR is not a version of derived data but of a single base table. Hence, some very common applications involving aggregates, joins, and subsets of base tables cannot be supported. If there are no IUV updates (DT is empty), then an IUV becomes a snapshot or a conventional view, depending on whether the parent table is materialized or not. Views and snapshots facilitate the use of derived data only for retrieval, hence derived data has to be treated differently than primitive data. Also, since a version cannot be updated, multiple versions cannot be created.

## 5. Summary and conclusions

We have presented Independently-Updated Views (IUVs), a new approach for derived data in decision-support systems. IUVs allow a decision maker the freedom to manipulate derived data according to the needs of the application by removing many of the limitations in current database systems. IUVs are particularly useful in decision-making situations requiring what-if analysis, statistical databases, and local control of data in distributed databases. We showed how multiple versions of derived data can be created without substantially duplication of data. Moreover, these capabilities are achieved without having to compromise on the operational value of the database, i.e., the normal database operations are not affected at all. IUVs offer update as well as retrieval derivation transparency, and can be defined on dynamic databases to reflect the changing conditions in the real world. Consistency between the IUVs and the underlying database is maintained at all times.

An advantage of IUVs is their simplicity of implementation; IUVs can be implemented using conventional DBMS facilities and data structures. A differential table stores the mapping between the database and a version. It is just another base table. A front-end processor can translate queries and updates on IUVs to those on base tables. Alternatively, programmers may translate IUV queries directly into SQL queries as in [32]. For increased performance, the DBMS query processor can be modified to take advantage of the characteristics and structure of IUVs.

To determine the performance of IUVs, we derived analytical cost expressions that generalize the experimental results obtained in [32] using the ORACLE DBMS. For the views typically used in decision-making processes such as budgetting, forecasting, and planning (aggregates, joins, and subsets of base tables), we found that the cost of IUVs is within 10% over the cost of simply retrieving the corresponding parent table.

We presented a comparison between IUV capabilities and those of other alternatives proposed for derived data, namely, virtual relations, snapshots, hypothetical relations (HR), and derived relations with exceptions (DRE). In addition to having many of the desirable capabilities for use of derived data in DSS, IUVs are a superset of those proposals for derived data.

## Appendix A. Updates to keys

Our presentation of IUVs has followed the traditional semantics of the relational model where a user-defined primary key identifies a unique object in the real world [12]. The primary key is a subset of the object's attributes that captures its uniqueness. Therefore, two rows in different tables that refer to the same object would have the same key value.

User-defined keys are the main approach to object identity in relational databases. However, they suffer from several problems (see $[20,22,7]$ ). A classic example is the insertion of rows for persons without a social security number in payroll, student, and library databases. Not only is there a problem during insertion when a temporary number must be given, but eventually when a social security number is obtained, all references to that person in the database must be changed to the new number. This may involve multiple tables. If the user or programmer making the changes is unaware or unauthorized to change all of them, dangling references are created. Codd $[7]$ , in his RM/T extension to the relational model, proposed the use of surrogates as a solution. Tables reference each other based on the surrogate rather than the value of the key. The similar notion of “object identifiers” is well established in object-oriented databases $[1,22]$ . In conventional relational systems, the newer implementations of SQL provide mechanisms to automatically propagate changes to a key throughout the database.

This appendix presents a solution to the problem caused by updating keys. First, we describe the problem in the context of IUVs. We then present a general solution followed by alternative implementations using triggers, declarative referential integrity, or surrogates. In all the cases, the implementation can be made transparent to the user.

## A.1. The key update problem

Consider an IUV SAMPLE with PT DEPT1, a view defined on a base table as follows.

<table><tr><td>CREATE VIEW</td><td>dept1</td></tr><tr><td>AS</td><td>SELECT empno, nameFROM employeesWHERE deptno = 1;</td></tr><tr><td>CREATE TABLE</td><td></td></tr><tr><td>employees</td><td></td></tr><tr><td>(empno)</td><td>INTEGER NOT NULL,</td></tr><tr><td>deptno</td><td>INTEGER,</td></tr><tr><td>name</td><td>CHAR(20),</td></tr><tr><td>position</td><td>CHAR(10),</td></tr><tr><td>salary</td><td>DECIMAL(9,2),</td></tr><tr><td>PRIMARY KEY(empno)).</td><td></td></tr></table>

We first illustrate the potential problem due to updates to the PT key. Assume that DEPT1 initially contains a single row with empno 100 and name “Jane Smith.” The first update to the IUV SAMPLE changes the name from “Jane Smith” to “Jane Blake.” This creates a row in the DT with empno 100, name “Jane Blake” and ACTION mod. Next, an update to EMPLOYEES changes empno from 100 to 125. A subsequent access of the IUV SAMPLE will detect an overlapping update of type modify / delete since there is no PT row with the same key value as the DT row. Following Section 2.6, the resolution of this overlapping update for Policy 1 results in two rows in the IUV: “100 Jane Blake” (from DT) and “125 Jane Smith” (from PT), an unintended result from the IUV user’s point of view. A problem also occurs if the above PT update (from 100 to 125) is followed by a PT insertion of “100 Tom Sanders.” If this insertion happens before the IUV is accessed, the previous IUV update (from “Jane Adams” to “Jane Blake”) is considered as being from “Tom Sanders” to “Jane Blake.” For Policy 2, these key updates do not present a problem because the IUV update is correctly treated (disregarded) in both situations.

Note that not all key updates to base tables cause problems. Of all PT updates to a key, only those that result in overlapping updates cause a problem. Also note that some key updates are semantically invalid regardless of the type of table, such as changing an employee number from 100 to 125 if 125 already exists in the table.

Consider now the problem caused by updates to the IUV key. Again we start with the single PT row with empno 100, and name “Jane Smith.” Assume now that the IUV update changes the row from “100 Jane Smith” to “150 Jane Smith.” A later PT update changes the PT row to “125 Jane Smith.” Under Policy 1, there will be two rows in the IUV: “125 Jane Smith” (from PT) and “150 Jane Smith” (from DT), an unintended result. Under Policy 2, the problem does not exist since the IUV update will be treated as an IUV modification followed by a PT deletion and therefore correctly ignored.

## A.2. A general solution

A general solution is to define DT with two key columns (or two sets of columns in case of a multi-attribute key). The column BASE\_KEY stores the value of the key as found in the PT and the column DIFF\_KEY stores the value to appear in the IUV. BASE\_KEY is a system column (like the timestamp and ACTION) and therefore hidden to the user. Ordinarily, the values of both BASE\_KEY and DIFF\_KEY are the same; their values differ only when key updates occur. To retrieve the IUV, the mechanism of 2.3 uses BASE\_KEY, instead of the DIFF\_KEY, to outer join the DT and the PT. The value of BASE\_KEY never appears in the IUV; it is used only for joining DT and PT.

If an IUV update modifies the key, BASE\_KEY will retain the previous value and DIFF\_KEY will have the modified value. If a PT update modifies a key value, the change is propagated to the corresponding BASE\_KEY in the DT and the timestamps of both the PT and DT rows are made equal. This reflects the fact that the update takes effect simultaneously in both tables. To propagate (or cascade, in the SQL terminology) the PT change as it occurs, we discuss in A.3 the application of mechanisms that are widely available in SQL implementations.

We illustrate the general solution in Table 6 for the five overlapping updates. For the first four cases assume that there is a PT row with initial values “100, JS, t” for empno, name, and the timestamp (TS), respectively. For the last case there is no PT row.

Consider the first case (modify / modify) in Table 6. A time t0, a non-key IUV update changes the name from “JS” to “JB” (short for “Jane Smith” and “Jane Blake”). This creates the DT row with “JB” shown in column 2. BASE\_KEY and DIFF\_KEY are the same since the key was not modified. At time $t_{1}$ , a PT update changes the key empno from 100 to 125 as shown in column 3. Column 4 shows the DT row after the propagation of the new key value (BASE\_KEY is now 125). Then, at time $t_{2}$ , the IUV is accessed. Column 5 shows the DT row after resolving the overlapping update for both policies, and column 6 shows the resulting IUV row.

Detection and resolution of updates to keys

<table><tr><td rowspan="2">(1)Type of overlapping update</td><td>(2) time  $t_0$ DT row</td><td></td><td>(3) time  $t_1$ PT row after key update</td><td>(4) time  $t_1$ DT row after cascading key update</td><td rowspan="2"></td><td>(5) time  $t_2$ DT row after resolving over-lapping update</td><td>(6) time  $t_2$ IUV row (result)</td></tr><tr><td colspan="2">base diffkey name action TS</td><td>empno name TS</td><td>base diffkey name action TS</td><td>base diffkey name action TS</td><td>empno name TS</td></tr><tr><td rowspan="2">modify / modify</td><td rowspan="2" colspan="2">100 100 JB modify  $t_0$ </td><td rowspan="2">125 JS  $t_1$ </td><td rowspan="2">125 100 JB modify  $t_1$ </td><td>Policy 1</td><td>125 100 JB modify  $t_2$ </td><td>100 JB  $t_2$ </td></tr><tr><td>Policy 2</td><td>no DT row</td><td>125 JS  $t_1$ </td></tr><tr><td rowspan="2">modify / delete</td><td rowspan="2" colspan="2">100 100 JB modify  $t_0$ </td><td rowspan="2">no PT row</td><td rowspan="2">null 100 JB modify  $t_1$ </td><td>Policy 1</td><td>null 100 JB insert  $t_2$ </td><td>100 JB  $t_2$ </td></tr><tr><td>Policy 2</td><td>no DT row</td><td>no IUV row</td></tr><tr><td rowspan="2">delete / modify</td><td rowspan="2" colspan="2">100 100 JS delete  $t_0$ </td><td rowspan="2">125 JS  $t_1$ </td><td rowspan="2">125 100 JS delete  $t_1$ </td><td>Policy 1</td><td>125 100 JS delete  $t_2$ </td><td>no IUV row</td></tr><tr><td>Policy 2</td><td>no DT row</td><td>125 JS  $t_1$ </td></tr><tr><td rowspan="2">delete / delete</td><td rowspan="2" colspan="2">100 100 JS delete  $t_0$ </td><td rowspan="2">no PT row</td><td rowspan="2">null 100 JS delete  $t_1$ </td><td>Policy 1</td><td>null 100 JS delete  $t_2$ </td><td>no IUV row</td></tr><tr><td>Policy 2</td><td>no DT row</td><td>no IUV row</td></tr><tr><td rowspan="2">insert / insert</td><td rowspan="2" colspan="2">200 200 AT insert  $t_0$ </td><td rowspan="2">200 AK  $t_1$ </td><td rowspan="2">200 200 AT insert  $t_0$ </td><td>Policy 1</td><td>200 200 AT insert  $t_2$ </td><td>200 AT  $t_2$ </td></tr><tr><td>Policy 2</td><td>no DT row</td><td>200 AK  $t_1$ </td></tr></table>

The other cases in Table 5 are mostly self-explanatory. The “no PT row” entry in column 3 for modify / delete and delete / delete denotes the deletion of the PT row at time $t_{1}$ . This results in cascading a null value to the BASE\_KEY in the DT row. The case insert/insert denotes the insertion of an IUV row with empno 200 and name “AT” at time $t_{0}$ , followed by an insertion of a PT row with the same key value but a different name (column 3) at time $t_{1}$ .

## A.3. Implementation of key updates

To implement the general solution, two widely available mechanisms in SQL systems are used: triggers and referential integrity constraints. Triggers are supported by many DBMSs, including DEC's RDB, the Sybase and Microsoft SQL Servers, SQL/DS, INGRES, and Oracle 7. We illustrate the automatic cascading of key updates to DT using the SQL Server syntax [28] for triggers. In this syntax, the logical table “inserted” contains the values of the columns after the update. The trigger is automatically fired by the DBMS whenever the specified table is updated. The following example updates the DT DIFF-SAMPLE whenever EMPLOYEES is updated.

<table><tr><td>CREATE TRIGGER</td><td>cascadeKey ON employees</td></tr><tr><td>FOR UPDATE AS</td><td></td></tr><tr><td>UPDATE</td><td>diffSample</td></tr><tr><td>SET</td><td>base_key = inserted.empno</td></tr><tr><td>WHERE</td><td>base_key = employees.empno.</td></tr></table>

An alternative to triggers is the declarative referential integrity of SQL-92 supported by most DBMSs. The differential table is created with an additional foreign key clause that references the primary key of a base table. This base table may or may not be the PT; all that is required is that it contains the current values for that key (i.e., it plays a role similar to the E-relations of [7]).

<table><tr><td>CREATE TABLE</td><td>diff-sample2</td></tr><tr><td>(base_key</td><td>INTEGER,</td></tr><tr><td>diff_key</td><td>INTEGER,</td></tr><tr><td>name</td><td>CHAR(30),</td></tr><tr><td>salary</td><td>DECIMAL(9,2),</td></tr><tr><td>PRIMARY KEY (diff_key),</td><td></td></tr><tr><td>FOREIGN KEY (base_key)</td><td></td></tr><tr><td>REFERENCES employees</td><td></td></tr><tr><td>ON UPDATE CASCADE ON</td><td></td></tr><tr><td>DELETE SET NULL.</td><td></td></tr></table>

Using referential integrity constraints to implement the general solution requires a special treatment for IUV insertions. By definition, IUV insertions violate the constraint since the key in the inserted DT row has no match in the PT. In systems that support the temporary deactivation of key constraints, such as SQL/DS and Oracle 7, a simple solution is to deactivate the constraint whenever an IUV insertion is made. In systems that do not support temporary deactivation, insertions to the IUV must use a null value for BASE\_KEY and check for two IUV rows with the same key value when the IUV is accessed. The presence of two rows with the same key values indicates an overlapping update that is resolved by retaining only one of the two rows in the IUV, according to its policy.

A variation of the referential integrity approach is to use surrogates. A surrogate is implemented using the row (or tuple) identifier (TID) of the PT row. TIDs are assigned when a base table row is first inserted and do not change throughout the existence of the row. In the DT, BASE\_KEY contains either the TID of the matching PT row or a null value if there is no matching row. Base table updates that modify the value of the key do not modify the TID. Neither do the IUV updates. Surrogates replace the primary key for the purpose of joining DT and PT. DT rows with null TIDs are processed as indicated in the previous paragraph for systems that do not support temporary deactivation of foreign key constraints. TIDs have been used for hypothetical relations [40] and materialized views [35] and simplify dealing with long multi-attribute keys. A limitation of this approach is that TIDs can only be used when the PT preserves the primary key of a base table on which it is defined or is a row subset of a single base table.

## References

[1] S. Abiteboul and P. Kanellakis, 1989, Object Identity as a Query Language Primitive, Proceedings of the ACM SIGMOD Conference Portland, Oregon, June 1989.

[2] M.E. Adiba and B G. Lindsay, 1980, Database Snapshots, Proceedings of the International Conference on Very Large Data Bases (October 1980), pp. 86–91.

[3] R. Agrawal and D.J. DeWitt, 1983, Updating Hypothetical Data Bases, Information Processing Letters 16 (1983), pp. 145–146.

[4] F. Bancilhon and N. Spyratos, 1981, Update Semantics of Relational Views, ACM Transactions on Database Systems 6, No. 4 (December), pp. 557–575.

[5] D. Beech and B. Mahbod, 1988, Generalized Version Control in an Object-Oriented Database Language, Proceedings of the 1988 SIGMOD Conference, Chicago, Ill. (June 1988), pp. 56–68.

[6] J.A. Blakeley, P. Larson and F.W. Tompa, 1986, Efficiently Updating Materialized Views, Proceedings of the 1986 ACM-SIGMOD Conference on Management of Data, Washington DC (May 1986), pp. 61–71.

[7] E.F. Codd, 1979, Extending the Relational Model to Capture More Meaning, ACM Transactions on Database Systems 4 (1979), No. 4, pp. 397–434.

[8] E.F. Codd, 1990, The Relational Model for Database Management: Version 2 (Addison-Wesley, Reading, Massachusetts, 1990).

[9] S. Cosmadakis and C. Papadimitriou, 1984, Updates on Relational Views, Journal of ACM 31, No. 4, pp. 742–760.

[10] C.J. Date and C. White, 1989, A Guide to DB2, 3rd edition (Addison-Wesley Publishing Company, Reading, Massachusetts, 1989).

[11] C.J. Date, 1986, Why Every Relation Should Have Exactly One Primary Key, in: C.J. Date, Relational Database: Selected Writings, Addison-Wesley (1986), pp. 33–40.

[12] C.J. Date, 1990, An Introduction to Database Systems, 5th edition (Addison-Wesley Publishing Company, Reading, Massachusetts, 1990).

[13] R. Dattero, R.G. Ramirez, and J. Choobineh, 1990, Derived Relations with Exceptions: Decision Support Capabilities, Journal of Management Information Systems 6, No. 4 (Spring 1990), pp. 83–101.

[14] U. Dayal and P.A. Bernstein, 1980, On The Updatability of Relational Views, Proceedings of the Fourth Conference on Very Large Databases, West Berlin (September 1980), pp. 368–374.

[15] D. Fishman et al, IRIS: An Object-Oriented Database Management System, ACM Transactions on Office Information Systems 5, No. 1 (1987), pp. 48–69.

[16] E.N. Hanson, 1987, A Performance Analysis of View Materialization Strategies, Proceedings of ACM SIGMOD 1987, San Francisco, pp. 440–453.

[17] W.H. Inmon, 1990, Using Oracle to Build Decision Support Systems (QED Information Sciences, Inc., 1990).

[18] R.H. Katz and T.J. Lehman, 1984, Database Support for Versions and Alternatives of Large Design Files, IEEE Transactions on Software Engineering SE-10, No. 2 (March 1984), pp. 191–200.

[19] A.M. Keller, 1986, Choosing Translator at View Definition Time, Proceedings of the 12th VLDB Conference, Kyoto, Japan.

[20] W. Kent, 1979, Limitations of Record-Based Information Systems, ACM Transactions on Database Systems 4, No. 1, pp. 107–131.

[21] W. Kim, 1990, Introduction to Object-Oriented Databases (The MIT Press, Cambridge, MA, 1990).

[22] S. Khoshafian and George P. Copeland, 1990, Object Identity, in Readings in Object-Oriented Database Systems, Stanley B. Zodnik and David Maier, Eds. (Morgan-Kaufmann Publishers, Inc., 1990). A previous version appears in Proceedings of OOPSLA 1986.

[23] S. Khoshafian, C. Arvola, A. Wong and H.K.T. Wong, 1991, A Guide to Developing Client/Server SQL Applications (Morgan Kaufmann Publishers).

[24] J.A. Larson and A.P. Sheth, 1991, Updating Relational Views using Knowledge at View Definition and View Update Time, Information Systems 16, No. 2, pp. 145–168.

[25] B. Lindsay, L. Haas, C. Mohan, H. Pirahesh and P. Wilms, 1986, A Snapshot Differential Refresh Algorithm, Proceedings of the 1986 ACM-SIGMOD Conference on Management of Data, Washington DC (May 1986), pp. 53–60.

[26] Microsoft, 1993, Microsoft Access - User's Guide (Microsoft Corporation, 1993).

[27] J. Melton and A.R. Simon, 1993, Understanding the New SQL: A Complete Guide (Morgan Kaufmann Publishers, Inc.).

[28] Microsoft, 1993, Microsoft SQL Server Language Reference (Microsoft Corporation).

[29] P. Mishra and E.M. Heich, Join Processing in Relational Databases, ACM Computing Surveys 24, No. 1 (March 1992), pp. 64–113.

[30] R.G. Ramirez, R. Dattero and J. Choobineh, Representing Generalization Rules and Exceptions in Expert

Database Systems, Decision Support Systems 5 (1990), pp. 29–44.

[31] R.G. Ramirez, R. Dattero and J. Choobineh, 1990b, Extension of Relational Views to Derived Relations with Exceptions, Information Systems 15, No. 3 (1990).

[32] R.G. Ramirez, U. Kulkarni and K.A. Moser, 1992, Performance Analysis of “What-if” Databases Using Independently-Updated Views, Journal of Management Information Systems 9, No. 1 (Summer 1992), pp. 185–203.

[33] RTI, 1990, The INGRES Documentation Set (Relational Technology Inc.).

[34] B. Salzberg, File Structures (Prentice Hall, 1988).

[35] A. Segev and J. Park, 1989, Updating Distributed Materialized Views, IEEE Transactions on Knowledge and Data Engineering 1, No. 2 (June 1989).

[36] D. Severance and G. Lohman, 1976, Differential Files: Their Application to the Maintenance of Large Databases, ACM Transactions on Database Systems, June 1976.

[37] M. Stonebraker, 1975, Implementation of Integrity Constraints and Views by Query Modification, Proceedings of the 1975 ACM-SIGMOD International Conference on Management of Data, San Jose, CA, June 1975.

[38] M. Stonebraker, 1980, Embedding Expert Knowledge and Hypothetical Data Bases into a Data Base System, Proceedings of the 1980 ACM-SIGMOD Conference on Management of Data, Santa Monica, CA., May 1980.

[39] M. Stonebraker, 1981, Hypothetical Data Bases as Views, Proceedings of the 1981 ACM-SIGMOD Conference on Management of Data, Ann Arbor.

[40] J. Woodfill and M. Stonebraker, 1983, An Implementation of Hypothetical Relations, Proceedings of the Ninth International Very Large Data Base Conference Florence, Italy, December 1983.

[41] S.B. Yao, 1977, Approximating Block Accesses in Database Organizations, Communications of the ACM 20, No. 4 (April 1977), pp. 260–261.

Richard G. Ramirez is an Assistant Professor of Information Systems at Iowa State University. A graduate of Texas A&M University, his research interests are object-oriented systems and the integration of mathematical programming and databases. Professor Ramirez has published research on relational databases and decision support systems.

Uday R. Kulkarni is an Assistant Professor of Computer Information Systems at Arizona State University. He received his B. Tech. degree in electrical engineering from the Indian Institute of Technology, Bombay, in 1977, his MBA degree from the Indian Institute of Management, Calcutta, in 1979, and his Ph.D. in MIS from the University of Wisconsin, Milwaukee, in 1989. His research interests are centered on manipulation of relational views, materialized views in centralized and distributed databases, and design of distributed databases.

![](/api/attachments/75PNCQEC/fulltext/images/0674bef19452b45ed737d66d8fd7157f95308b42e2db0ba6f0b813f8043ffebc.jpg)

Kathleen A. Moser is an Assistant Professor of Information Systems at Iowa State University. She received her Ph.D. in computer information systems from Arizona State University. Her major research interests are gender issues in information systems, and strategic planning. Professor Moser is a member of AIS, the Society for Information Management (SIM), and the Association for Systems Management (ASM).
