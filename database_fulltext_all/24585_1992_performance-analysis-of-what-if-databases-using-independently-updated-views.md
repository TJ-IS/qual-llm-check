---
otero_id: 24585
otero_key: "N5FAJ2RM"
title: "Performance Analysis of “What-If” Databases Using Independently Updated Views"
authors: "Richard G. Ramirez; Uday R. Kulkarni; Kathleen A. Moser"
year: "1992"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1992.11517953"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Performance Analysis of "What-If" Databases Using Independently Updated Views

Richard G. Ramirez, Uday R. Kulkarni & Kathleen A. Moser

To cite this article: Richard G. Ramirez, Uday R. Kulkarni & Kathleen A. Moser (1992) Performance Analysis of “What-If” Databases Using Independently Updated Views, Journal of Management Information Systems, 9:1, 185-203, DOI: 10.1080/07421222.1992.11517953

To link to this article: https://doi.org/10.1080/07421222.1992.11517953

![](/api/attachments/N5FAJ2RM/fulltext/images/e0299d0ff62f758d17ed84c73967cf48b6a9a1afb7a50b8051d4d12a9dda464a.jpg)

Published online: 16 Dec 2015.

![](/api/attachments/N5FAJ2RM/fulltext/images/5ecc36dbe343a04de98f2f9a50ffcc96449a2d2730ddcc3dc4aff44900a1d0c7.jpg)

Submit your article to this journal ↗

![](/api/attachments/N5FAJ2RM/fulltext/images/689d09c0fdb1b5846cc627a70f666c0966359d434fd70917d6ef41fa56c2039b.jpg)

View related articles ↗

![](/api/attachments/N5FAJ2RM/fulltext/images/5848facc66544bb9f8fea481dfb900de857d28f0815d70b52daba3bcf8798125.jpg)

Citing articles: 4 View citing articles ↗

# Performance Analysis of “What-If” Databases Using Independently Updated Views

RICHARD G. RAMIREZ, UDAY R. KULKARNI, AND KATHLEEN A. MOSER

RICHARD G. RAMIREZ is an Assistant Professor of Information Systems at Iowa State University of Science and Technology. He received his Ph.D. from Texas A&M University in 1987. His current research interests are in the integration of mathematical programming and databases to develop decision support systems. Professor Ramirez has also published in the areas of relational views and expert databases.

UDAY R. KULKARNI is an Assistant Professor of Computer Information Systems at Arizona State University. He received his B.Tech. degree in electrical engineering from the Indian Institute of Technology, Bombay, in 1977, his M.B.A. degree from the Indian Institute of Management, Calcutta, in 1979, and his Ph.D. in MIS from the University of Wisconsin, Madison, in 1989. His research interests are centered on manipulation of relational views, materialized views in centralized and distributed databases, and design of distributed databases.

KATHLEEN A. MOSER is an Assistant Professor of Information Systems at Iowa State University of Science and Technology. She received her Ph.D. in computer information systems from Arizona State University. Her major research interests are object-oriented modeling and the strategic planning of information systems. Her current research interests focus on object-oriented methodologies for information systems architectures. Professor Moser is a member of TIMS, the Society for Information Management (SIM), and the Academy of Management.

ABSTRACT: Multiple scenarios are critical to “what-if” analysis. Scenarios are built using alternate versions of a database; each version shows, in detail, the result of a decision or a combination of decisions. Relational database management systems, despite their widespread use, lack the explicit capabilities for what-if analysis. We present a concept called independently updated views (IUVs) for creating multiple scenarios. An IUV corresponds to a version of the database. Each version is manipulated and updated as if it were the “real” database; however, only differences between the version and the real database are stored. This paper describes an experiment for measuring the overhead of using IUVs for supporting what-if analysis for a range of typical views and queries. Results indicate that the overhead is minimal for creating what-if scenarios based on views with aggregate functions (SUM, AVG) and on views that are small subsets of the database. These are the classes of views that are more often used in decision making. For views that require retrieval of entire or large portions of the database, the overhead can be high and special data structures may be required.

KEY WORDS AND PHRASES: hypothetical databases, relational databases, relational views, view updates, "what-if" analysis.

## 1. Introduction

MULTIPLE SCENARIOS ARE CRITICAL TO “WHAT-IF” ANALYSIS. Scenarios are developed because different decisions have different operational or political consequences. A classic example is the negotiation of payroll contracts with unions. One scenario may show the effect on paychecks, taxes, and cost of benefits due to a 5 percent salary increase given to all employees. Another scenario may increase salaries by only 3 percent while giving more medical benefits.

What-if scenarios are often developed from existing data. To create a scenario, the data are copied and then modified. Most database management systems (DBMS), including DB2, SQL/DS, and ORACLE, provide no automatic support for developing what-if scenarios. The process must be managed by the decision maker (or the application programmers). This lack of support results in unnecessarily complex manipulation and management of the database, particularly from the viewpoint of the decision maker, as well as in duplication of data which increases computer time and disk space needs.

To support multiple scenarios, a DBMS must provide the following services:

1. Allow the explicit definition of a new scenario with simple statements for this purpose;

2. Allow scenarios to be based on derived data, such as meaningful subsets of the database, computed values, and aggregates, instead of the raw data itself;

3. Label scenarios as versions of data, making it easy to identify versions from original data. Multiple scenarios on the same data should be identified as a group;

4. Reduce data duplication to a minimum in a way that is transparent to the user.

This paper presents a concept called Independently Updated Views (IUVs), an extension to relational databases, to address the above requirements. IUVs manipulate conventional views (virtual relations) to create what-if scenarios. Scenarios built using IUVs may contain subsets of the real database, and computed or aggregate attributes such as averages and cumulative totals. Updates to an IUV are not mapped to the physically stored database, but are stored in a differential table. Multiple scenarios are created by defining multiple IUVs on the same view. The database may be read-only or may be updated. Conflicts arising from updating tuples in the database and the IUV are resolved according to predefined rules.

Our emphasis in this paper is on the overhead of using IUVs. This overhead is mainly given by the time spent in retrieving a view and merging it with its updates to produce the “modified view” (IUV). The analysis presented here is based on experiments using current facilities of commercial DBMSs. The results identify situations where IUVs are cost-effective. Further research can help detect areas in which special data structures and algorithms are needed to provide a more efficient representation and manipulation of what-if databases.

The paper is organized as follows. Section 2 presents the concept of IUVs and discusses their implementation. Section 3 describes an experiment to measure their cost. Section 4 presents the results. Section 5 concludes the paper. An appendix formulates the analytical cost of retrieving IUVs.

## 2. Independently Updated Views for What-If Scenarios

INDEPENDENTLY UPDATED VIEWS (IUVs) SPECIFICALLY SUPPORT what-if analysis. The concept of IUVs builds on differential files and relational views. A differential file is a file that stores changes made to a "source" file [12, 18]. These changes are incorporated into the source file when it is retrieved. A relational view is a table that is derived from one or more base tables, that is, physically stored tables [7]. Views are virtual relations and are not physically stored. Queries to a view are processed using "query modification" [19] to produce a query against the base tables on which the view is defined. Views provide access to data in a way that is natural to the user's application rather than in the way the data are actually stored. For example, a sales database that contains a base table with a row for each invoice may use a view to provide the sales manager with a single row for each customer that summarizes all invoices for that customer.

## 2.1. Independently Updated Views

An IUV represents a hypothetical scenario based on a view of the database. An IUV is a virtual relation, formed by making changes to a view called a parent view (PV) of the IUV. Changes to the PV are stored in a separate base table called a differential table (DT). Whenever a query accesses an IUV, (logically) the IUV is automatically constructed by forming the corresponding PV and incorporating into it the changes stored in the DT. Physically, “query modification” may translate the original query into a query on the relevant base tables. Changes made to the PV, using the DT, are not mapped to the original database; they are only used to form the IUV.

A PV may be defined using an arbitrary relational algebra expression involving the base relations. The primary key of a PV is not necessarily the primary key of any of the base relations because the view may involve selections, projections, joins, and aggregate functions. Multiple DTs may be created for a single PV, resulting in many IUVs representing competing scenarios. In figure 1, $IUV_{m_{1}}$ through $IUV_{m_{k}}$ represent k competing scenarios based on $PV_{m}$ .

A DT contains one row for each PV tuple that is updated (inserted, deleted, or modified). The primary key of a DT is the same as that of the corresponding PV. A DT includes the columns of the PV plus a column to specify the type of update. There is at most one tuple in a DT for each tuple of the corresponding PV. A DT tuple represents the net effect of all changes made to the PV tuple. Therefore, if a tuple is modified and then deleted, only one tuple with “delete” action appears in the DT. Figure 2 shows the IUV $\psi$ based on PV $\pi$ and the DT $\delta$ .

IUVs allow versions to be defined on any valid view. Thus, in figure 2, a tuple in $\pi$ may correspond to a single row in a base table, it may be the result of joining rows from two or more tables, or it may be obtained by an aggregate function on multiple rows. Columns in a PV may be constants, computed values (current salaries plus a 5 percent raise), drawn from one or more base tables, or aggregates (totals by job category). One or more columns may be designated as read-only; an attempt by a DT to modify these is simply ignored. In its simplest form, a PV can be a replica of a base table. This flexibility is very useful in what-if situations.

![](/api/attachments/N5FAJ2RM/fulltext/images/fe3f7084d76eaa225d09c20d0717a406f94eba743c893feb75bdd6ee353e6159.jpg)  
Figure 1. Multiple Scenarios for Multiple Views

![](/api/attachments/N5FAJ2RM/fulltext/images/621371b2c10e4447b95166d0b2a27f92dac376401867f66c4ea1eaa90d3c628c.jpg)  
Figure 2. An Example of IUVs

Besides supporting what-if scenarios, IUVs are also useful in statistical databases that typically deal with aggregates such as means and sums, or functions that are expensive to recompute, such as individual deviations from the mean $[4]$ . Another application of IUVs is in extending the handling of snapshots in distributed databases $[1]$ , by allowing updates to provide “local” variations of global data as well as detecting differences between the updated snapshot and the original information.

## 2.2. Related Research

IUVs are a logical superset of hypothetical relations (HR) proposed in [20]. An HR is a special case of an IUV with the following restrictions: (a) the PV is defined on a single base table; (b) the base table is read-only; it cannot be updated after an HR has been defined on it; (c) all columns and rows of the base table are included in the PV; for example, there are no projections, selections, or aggregate operations; and (d) the user cannot designate some column(s) in the PV as read-only. HRs were first implemented by storing the updates in two differential tables (inclusions and omissions). An HR was obtained as:

## HR = original UNION inclusions DIFFERENCE omissions.

Modifications were represented as a deletion followed by an insertion. The differential tables were append-only. However, this made it impossible to insert a tuple that had been previously deleted. A later implementation in $[23]$ used a single differential file with tuple identifiers and timestamps proposed in $[2]$ .

Derived Relations with Exceptions (DREs) [15, 16] utilize views to represent generalization rules. Exceptions to the rules are stored in differential files. Under certain conditions, it is possible to use the DRE mechanism to implement what-if scenarios [8]. As with HRs, DREs can only be defined on read-only base tables.

Since updates to the PV are never mapped to the database, the classical “view update” problem as discussed in $[3, 9]$ does not arise. This problem occurs when view updates cannot be automatically mapped to the corresponding base tables. The treatment of updates to IUVs is also different from the “snapshot maintenance” problem discussed in $[1, 5, 10, 13]$ , in which a snapshot (a materialized view) is read-only. Snapshots cannot be independently updated; they are “refreshed” by translating the corresponding base table updates to snapshot updates. IUVs, on the other hand, are updated (independently of the base tables) by storing the changes in a DT. However, since the database is not limited to read-only tables, it is possible for a database update to affect a tuple in a PV already modified by a DT tuple. This is referred to as an “update conflict.” The IUV mechanism maintains database consistency by reconciling such conflicts using time-stamps $[17]$ . The reconciliation process does not affect the performance of IUVs significantly, as it involves rewriting a few DT tuples that have already been read.

## 2.3. A Comprehensive Example

The following example illustrates the IUV mechanism and the use of SQL for their implementation. The example describes a scenario for the planning of sales quotas in a company.

SALES (figure 3a) is a base table in which each “emp#” is a salesperson assigned to a “dept” in a “branch,” and has a “sales” and a “quota” which are respectively the actual sales for the current period and planned sales for the planning period. Figure 3b shows sample rows of a PV, BRANCH-SALES, an aggregate view containing total sales and quota of each department in a branch. BRANCH-SALES can be defined using the standard SQL statement:

CREATE VIEW branch\_sales (branch, dept, sales, quota)

AS SELECT branch, dept, SUM(sales), SUM(quota)

FROM sales

GROUP BY branch, dept;

Based on BRANCH-SALES, the company management sets new quotas for selected departments in some branches. Consider a scenario where quotas for the “educational” and “wholesale” departments in Houston are changed, a new “wholesale” department is opened in Los Angeles, and the “retail” department in Phoenix is closed. These changes are stored in the DT DIFF-QUOTA (figure 4a). The scenario is shown by the IUV BRANCH-QUOTAS (figure 4b) formed by processing the PV BRANCH-SALES with the DT DIFF-QUOTA. Values in bold reflect the new quotas. Multiple competing scenarios like the one above may be created by building many DTs for the PV BRANCH-QUOTAS. The selected scenario (plan) is sent to the branches which allocate the quotas among individual salespersons.

To obtain the IUV, two steps are required. First, the following SQL command matches rows in BRANCH-SALES to any updates in DIFF-QUOTA on the primary key. It also retrieves the rows in BRANCH-SALES that were not modified or deleted, as well as the rows inserted into the IUV (nonmatching rows in DIFF-QUOTA).

SELECT pv.branch, pv.dept, pv.sales, pv.quota,

dt.branch, dt.dept, dt.sales, dt.quota

FROM branch-sales pv, diff-quota dt

WHERE pv.branch /=\dt.branch

AND pv.dept /=\dt.dept

AND dt.action != "delete";

An outer join, denoted by "/=\" following the syntax proposed in [6], is used. "An outer join is an extended form of the ordinary (or inner) join in which tuples in one relation having no counterpart in the other appear in the result with nulls in the other attribute positions, instead of being simply ignored" [7]. The second step "chooses" the columns to be returned. For IUV insertions and modifications, columns of DT are used. For nonmatching rows from the parent view (i.e., for unchanged rows), columns of PV are is used. This additional step is performed in main memory and takes a negligible amount of time compared to that required for the above query. Note that the existence of the differential table and the necessary statements to process it can be transparent to the user.

## 3. Determining the Cost of IUVs

THIS SECTION DESCRIBES AN EXPERIMENT TO ESTIMATE the cost of retrieving IUVs using different types of queries on multiple classes of parent views. We use existing facilities in the SQL language. The objective is to determine whether these facilities, as supported by commercial DBMS, provide adequate performance and to identify situations where IUVs are cost-effective. A further research direction would be to identify needs for special data structures and algorithms to provide an improved representation and manipulation of what-if databases. The appendix derives analytical cost estimates of IUVs.

<table><tr><td>EMP#</td><td>BRANCH</td><td>DEPT</td><td>NAME</td><td>SALES</td><td>QUOTA</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>110</td><td>Phoenix</td><td>retail</td><td>John Smith</td><td>15,500</td><td>21,000</td></tr><tr><td>123</td><td>Phoenix</td><td>educ</td><td>Mary Doe</td><td>23,008</td><td>22,000</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>178</td><td>Houston</td><td>retail</td><td>Karen Sanders</td><td>19,872</td><td>18,500</td></tr><tr><td>192</td><td>Phoenix</td><td>retail</td><td>Peter Brown</td><td>12,076</td><td>15,000</td></tr><tr><td>202</td><td>Dallas</td><td>whole</td><td>Albert Deere</td><td>78,973</td><td>75,000</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>226</td><td>Dallas</td><td>educ</td><td>Teresa Jones</td><td>32,620</td><td>31,000</td></tr><tr><td>233</td><td>Houston</td><td>whole</td><td>Alma Fuentes</td><td>84,095</td><td>75,000</td></tr><tr><td>244</td><td>Dallas</td><td>retail</td><td>Tom Dewey</td><td>17,034</td><td>17,000</td></tr><tr><td>267</td><td>Dallas</td><td>educ</td><td>Sharon Perez</td><td>22,617</td><td>23,000</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

3a. Table SALES

<table><tr><td>BRANCH</td><td>DEPT</td><td>SALES</td><td>QUOTA</td></tr><tr><td>Dallas</td><td>educ</td><td>1,213,056</td><td>1,110,000</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>Houston</td><td>retail</td><td>2,100,315</td><td>2,050,000</td></tr><tr><td>Houston</td><td>educ</td><td>1,589,011</td><td>1,300,000</td></tr><tr><td>Houston</td><td>whole</td><td>4,500,974</td><td>3,900,000</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>Phoenix</td><td>retail</td><td>15,500</td><td>21,000</td></tr><tr><td>Phoenix</td><td>whole</td><td>1,305,892</td><td>2,090,000</td></tr></table>

3b. View BRANCH-SALES  
Figure 3. Sample Table and View

## 3.1. The Cost of IUVs

We are interested in comparing the cost of using IUVs for creating what-if scenarios with the cost of creating such scenarios without the IUVs. In the absence of the IUV mechanism, what-if scenarios can be obtained from stored copies of the relevant base tables which have been updated to reflect the hypothetical changes. Hence, the cost of IUVs is defined as the difference between the cost of querying IUVs and the cost of querying the parent view of (a copy of) the base tables, that is, $IUV\_cost = V\_time - P\_time$ , where $V\_time$ is the time to run a query on an IUV and $P\_time$ is the time to run the same query directly on the parent view. Our definition of $IUV\_cost$ , however, does not consider the time to copy the base tables and to perform the updates, or the additional disk space to store the copies.

<table><tr><td>BRANCH</td><td>DEPT</td><td>QUOTA</td><td>ACTION</td></tr><tr><td>Houston</td><td>educ</td><td>1,600,000</td><td>modify</td></tr><tr><td>Houston</td><td>whole</td><td>4,500,000</td><td>modify</td></tr><tr><td>Los Angeles</td><td>whole</td><td>250,000</td><td>insert</td></tr><tr><td>Phoenix</td><td>retail</td><td></td><td>delete</td></tr></table>

4a. Differential Table DIFF-QUOTAS

<table><tr><td>BRANCH</td><td>DEPT</td><td>SALES</td><td>QUOTA</td></tr><tr><td>Dallas</td><td>educ</td><td>1,213,056</td><td>1,110,000</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>Houston</td><td>retail</td><td>2,100,315</td><td>2,050,000</td></tr><tr><td>Houston</td><td>educ</td><td>1,589,011</td><td>1,600,000</td></tr><tr><td>Houston</td><td>whole</td><td>4,500,974</td><td>4,500,000</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>Los Angeles</td><td>whole</td><td>0</td><td>250,000</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>Phoenix</td><td>whole</td><td>1,305,892</td><td>2,090,000</td></tr></table>

4b. IUV BRANCH-QUOTAS  
Figure 4. IUV and Differential File for Sample View

## 3.2. The Experiment

The ORACLE DBMS Version 5.1 was used for the experiment. The computer was a 25 MHz Zenith 386 with 2 MB main memory and a 150 MB SCSI disk. The results obtained may not directly translate to other commercial DBMS because of the peculiarities of different systems in implementing low-level activities such as sorting, use of indexes, outer joins, and the like. ORACLE is, however, widely used across a large number of systems including MS-DOS, UNIX, VAX VMS, OS/2, and IBM's CMS. Also, the query optimization algorithms of ORACLE are similar across all environments.

Queries were run on PVs and the corresponding IUVs and the running times were recorded to obtain the IUV cost. Keeping all hardware- and software-related factors constant, the running time of a query depends on the following parameters of interest:

Query running time = f(class of parent view, type of query, physical structure of the tables)

To evaluate IUV costs under different situations, the parameters were varied as follows:

Classes of Parent Views

Three classes of parent views were considered.

1. Large subsets: The PV is a copy or a “large subset” of a base table or of the join of two tables. The base table(s) must be read in its (their) entirety to obtain the view. These views represent a situation where a decision maker would like potentially to manipulate all tuples to create new scenarios (e.g., all employee quotas).

2. Small subsets: The PV is a “small subset” of a base table or of the join of two tables. These views represent a situation where a decision maker is interested in manipulating only a “few” selected tuples (e.g., employee quotas of a particular department) for creating new scenarios. The size of the subset is small enough so that reading the entire table(s) can be avoided if appropriate indexes exist. Moreover, such subsets can be accommodated in the main memory.

3. Aggregates: Views formed using aggregate functions such as SUM and AVG fall in this category. The entire base table(s) must be read but the result is a “small” number of tuples (e.g., sales grouped by branch). The decision maker manipulates the aggregate data to create new scenarios.

## Types of Queries

Four types of queries were run on the PVs and on the corresponding IUVs.

1. Retrieve the view (PV or IUV) and present it without any special order.

2. Retrieve the view and present it sorted on the key attribute.

3. Retrieve the view and present it sorted on an attribute other than the key.

4. Retrieve the view and present an aggregate of the view.

A program written in C with embedded SQL was used to run the above queries. A cursor was defined for each query. The program used a loop to fetch each row of the resultant table using the cursor, as shown for the query of type 4 on the PV of class "small subsets":

```sql
EXEC SQL DECLARE q4b CURSOR FOR
SELECT b.dept, AVG(diff.amount)
FROM smallview b, diff
WHERE b.emp = diff.emp(+)
GROUP BY b.dept;

EXEC SQL OPEN CURSOR q4b;
do
{
    EXEC SQL fetch q4b INTO :name, :amount;
} while (sqlca.sqlcode == 0);

EXEC SQL CLOSE q4b;
```

Physical Structure of the Tables

The following index options were considered:

1. Base table indexed on the key attribute.

2. Base table without an index.

An index on the DT was not included because it is not beneficial. This is because all the tuples of the differential table are accessed; a sequential access is faster under such circumstances.

A base table BASE, with the schema, BASE (emp, name, region, dept, amount, time) was used, with EMP having unique values. REGION had thirty-six different values and DEPT had twenty different values. Values of REGION, and DEPT were uniformly distributed. AMOUNT was used to obtain aggregates. TIME was a time-stamp generated for each update.

$IUV\_cost$ was obtained for twenty-four combinations (3 PV classes $\times 4$ query types $\times 2$ index options). To study the effect of changing the database size, each combination was run with three different base table sizes (1,000, 5,000, and 10,000 rows). Each combination was repeated at least five times and the average processing time was used for the analysis. To avoid the effect of buffering after a query, the queries (including repetitions) were processed in random order. The base table was randomly generated. Values of the columns used in a join or to form aggregates were uniformly distributed. Rows were also stored in random order to avoid the effect of presorting and clustering.

## 4. Results

THE AVERAGE TIME REQUIRED TO RUN the different types of queries on IUVs (V\_time) was compared with the time required to run the same queries directly on the parent views (P\_time). Costs are tabulated separately for each class of views—large subsets, small subsets, and aggregates. Within each view class, the four query types exhibit different performance. The analysis identifies the conditions under which the use of the IUV mechanism is most beneficial.

Figures 5a–c tabulate the $P\_time$ , $V\_time$ , and the $IUV\_cost$ as a percentage of $P\_time$ , that is, $IUV\_cost(\%) = 100 \times (V\_time - P\_time)/P\_time$ . This is the additional processing time needed to create a scenario using the IUV mechanism, expressed as a percentage increase over the time needed to create the scenario in the absence of the IUV mechanism. Figures 6a–c depict the $IUV\_cost$ normalized for the base table size: normalized $IUV\_cost = (V\_time - P\_time)/n$ , where $n$ is the number of tuples in the base table.

## 4.1. Large Subsets

The PV in the case of “large subsets” contained all the tuples of the base table. The costs of the four queries are shown in figure 5a and the normalized IUV\_costs are plotted in Figure 6a.

<table><tr><td></td><td colspan="3">1,000 Rows</td><td colspan="3">5,000 Rows</td><td colspan="3">10,000 Rows</td></tr><tr><td>QUERY</td><td>P-time</td><td>V-time</td><td>% incr.</td><td>P-time</td><td>V-time</td><td>% incr.</td><td>P-time</td><td>V-time</td><td>% incr.</td></tr><tr><td>1</td><td>4.70</td><td>12.53</td><td>166.6</td><td>22.65</td><td>75.20</td><td>232.0</td><td>44.50</td><td>162.80</td><td>264.0</td></tr><tr><td>2</td><td>11.87</td><td>12.80</td><td>7.8</td><td>74.35</td><td>75.60</td><td>1.5</td><td>161.80</td><td>163.20</td><td>0.9</td></tr><tr><td>3</td><td>9.20</td><td>15.53</td><td>68.8</td><td>51.20</td><td>93.20</td><td>82.0</td><td>103.60</td><td>199.60</td><td>92.7</td></tr><tr><td>4</td><td>4.60</td><td>11.40</td><td>147.8</td><td>20.80</td><td>63.00</td><td>202.9</td><td>41.00</td><td>134.00</td><td>226.8</td></tr></table>

5a. Queries on Large Subset

<table><tr><td colspan="2"></td><td colspan="3">1,000 Rows</td><td colspan="3">5,000 Rows</td><td colspan="3">10,000 Rows</td></tr><tr><td>QUERY</td><td>INDEX</td><td>P-time</td><td>V-time</td><td>% incr.</td><td>P-time</td><td>V-time</td><td>% incr.</td><td>P-time</td><td>V-time</td><td>% incr.</td></tr><tr><td rowspan="2">1</td><td>none</td><td>3.00</td><td>3.53</td><td>17.7</td><td>13.90</td><td>15.00</td><td>7.9</td><td>27.30</td><td>28.60</td><td>4.8</td></tr><tr><td>base</td><td>0.90</td><td>1.33</td><td>47.8</td><td>2.45</td><td>2.80</td><td>14.3</td><td>4.70</td><td>5.20</td><td>10.6</td></tr><tr><td rowspan="2">2</td><td>none</td><td>3.13</td><td>3.27</td><td>4.5</td><td>14.25</td><td>14.80</td><td>3.9</td><td>28.20</td><td>28.60</td><td>1.4</td></tr><tr><td>base</td><td>0.93</td><td>1.07</td><td>15.1</td><td>2.70</td><td>3.00</td><td>11.1</td><td>4.50</td><td>5.00</td><td>11.1</td></tr><tr><td rowspan="2">3</td><td>none</td><td>3.10</td><td>3.33</td><td>7.4</td><td>14.15</td><td>14.80</td><td>4.6</td><td>27.90</td><td>29.20</td><td>4.7</td></tr><tr><td>base</td><td>0.97</td><td>1.27</td><td>30.9</td><td>2.85</td><td>3.00</td><td>5.3</td><td>5.20</td><td>5.80</td><td>11.5</td></tr><tr><td rowspan="2">4</td><td>none</td><td>3.03</td><td>3.40</td><td>12.2</td><td>13.80</td><td>14.40</td><td>4.3</td><td>27.20</td><td>28.80</td><td>5.9</td></tr><tr><td>base</td><td>0.93</td><td>1.27</td><td>36.6</td><td>2.55</td><td>3.00</td><td>17.6</td><td>4.30</td><td>5.20</td><td>20.9</td></tr></table>

5b. Queries on Small Subset

<table><tr><td></td><td colspan="3">1,000 Rows</td><td colspan="3">5,000 Rows</td><td colspan="3">10,000 Rows</td></tr><tr><td>QUERY</td><td>P-time</td><td>V-time</td><td>% incr.</td><td>P-time</td><td>V-time</td><td>% incr.</td><td>P-time</td><td>V-time</td><td>% incr.</td></tr><tr><td>1</td><td>7.93</td><td>9.70</td><td>22.3</td><td>32.95</td><td>35.00</td><td>6.2</td><td>67.20</td><td>72.00</td><td>7.1</td></tr><tr><td>2</td><td>9.33</td><td>10.00</td><td>7.2</td><td>34.65</td><td>35.40</td><td>2.2</td><td>71.90</td><td>73.60</td><td>2.4</td></tr><tr><td>3</td><td>9.27</td><td>11.00</td><td>18.7</td><td>34.55</td><td>36.80</td><td>6.5</td><td>72.00</td><td>75.40</td><td>4.7</td></tr><tr><td>4</td><td>8.10</td><td>9.80</td><td>21.0</td><td>33.20</td><td>35.60</td><td>7.2</td><td>67.70</td><td>71.80</td><td>6.1</td></tr></table>

5c. Queries on Aggregates  
Figure 5. Processing Times for Parent Views and IUVs

## Query-1

Query-1 retrieves the view (PV or the IUV). $P\_time$ consists of reading and displaying the entire base table. $V\_time$ includes the additional time required for joining the PV with the updates, which in ORACLE (as in most DBMS) is performed after sorting the two tables on the joining attribute (EMP) [14, p. 179]. Because of this, $V\_time$ is much higher than $P\_time$ . The normalized $IUV\_cost$ of Query-1 is observed to be increasing with the size of the base table due to the polynomial time required for the sort.

## Query-2

Query-2 retrieves the view and presents it sorted by the key attribute (EMP). This query is amenable to IUV usage. $P\_time$ now also includes sorting the PV by EMP.

![](/api/attachments/N5FAJ2RM/fulltext/images/e006bd40750d5ef1b072eb3131b6d641c8cc0dda4669178cb814c3dc5251af5c.jpg)  
Figure 6a. Queries on Large Subsets

![](/api/attachments/N5FAJ2RM/fulltext/images/259c1d547b8b95bb1da1a3099f6aa8f32f627d34b4f24d5be64dee5d97dc8b58.jpg)  
Figure 6b. Queries on Small Subsets

$V\_time$ , on the other hand, is the same as for Query-1. As a result, the $IUV\_cost$ is only the additional time needed for joining the updates with the already sorted PV. For larger base tables, this is less than 2 percent of $P\_time$ . The normalized $IUV\_cost$ is negligible and hence not shown in figure 6a.

![](/api/attachments/N5FAJ2RM/fulltext/images/a24510f0f53517a3408b996f3b0588727ce9d6656b2aca5a9229a53edcd6e4b5.jpg)  
Figure 6c. Queries on Aggregates  
Query-3  
Query-3 retrieves the view and presents it sorted by a non-key attribute (DEPT). $P\_time$ consists of reading and sorting the base table by DEPT. This is faster than sorting the base table by EMP (as in Query-2) because the number of distinct DEPT values is much smaller than the number of distinct EMP values. $V\_time$ , on the other hand, is much higher than in Queries 1 and 2 because, in addition to sorting the base table and updates by EMP for joining, the result of the join has to be re-sorted by DEPT. Therefore, the $IUV\_cost$ is high and the normalized $IUV\_cost$ increases with the size of the base table.

## Query-4

Query-4 retrieves an aggregate, average amount by DEPT, of the view. $P\_time$ consists of reading the base table, compiling the aggregates as the table is read, and presenting the aggregated information [14, pp. 173, 177]. This time is low compared to Queries 2 and 3 because the number of rows in the result is much smaller. $V\_time$ , on the other hand, is quite high because the base table and the updates need to be sorted by EMP for joining prior to forming the aggregates by DEPT. The $IUV\_cost$ is thus very high and the normalized $IUV\_cost$ increases with the size of the base table.

For this view class, an index on the base table is not expected to improve performance. This is because, all (or most of) the tuples of the base table are read and an index provides no advantage $[14, p. 158]$ . An index is advantageous when only a few selected tuples are accessed. Initial experiments confirmed this expectation; hence, we did not pursue this option further.

## 4.2. Small Subsets

A PV in the case of “small subsets” can be entirely accommodated in the main memory. The key attribute was used in the view predicate. The views in this class were about 2.5 percent of the size of the base table. The differential table was proportionately sized. Figure 5b shows the cost of processing the four queries. The normalized IUV\_costs are plotted in figure 6b.

$P\_time$ for all the queries in this view class is lower than that for large subsets because, in general, much less information is displayed. The $IUV\_cost$ of all four query types is also very low. This is because sorting a smaller PV is much less expensive. The sort, which was the major component of $V\_time$ for large subsets, is no longer the major component. Instead, the major component of $V\_time$ is the time for forming the PV itself. As a result, $V\_time$ is comparable to $P\_time$ . Note that the $IUV\_cost$ without the index option is within 20 percent of $P\_time$ . An index on the base table in this view class is highly beneficial, as it helps in forming the PV. This is substantiated by the great decrease in $P\_time$ as well as $V\_time$ for all four queries. $IUV\_costs$ as a percentage of $P\_time$ are adversely affected but absolute $IUV\_costs$ are lower.

The normalized IUV\_cost decreases with the size of the base table. The reason is that, out of the two components of V\_time, the major component, forming the PV, is proportional to the size of the base table, whereas the second component, sorting and joining the PV and the updates (i.e., forming the IUV), stays relatively constant as long as all the tuples can be accommodated in main memory. Thus, an increase in the size of the base table does not proportionately increase the time for forming the IUV.

## 4.3. Aggregates

In the case of “aggregates,” the PV was formed by computing the average amount for each department within each region. The view thus had a composite key attribute (REGION, DEPT). Queries 1–3 present the view (PV or the IUV) without any order, sorted by the key, and sorted in a different order (DEPT, REGION), respectively. Query 4 presents an aggregate of the view (average amount by REGION). It must be noted that some relational systems have severe limitations on query modification. In DB2, one cannot join a table to a view defined with aggregates. ORACLE, however, allows queries on views that include aggregates, joins, aggregates of joins, and unions of several tables. In some cases, processing these queries may involve creation of temporary tables that are invisible to the user. The costs of the four queries are shown in figure 5c. The normalized IUV\_costs are plotted in figure 6c.

As with small subsets, the IUV\_cost of all four query types is very low for this class of views. This is because the major component of both P\_time and V\_time is forming the aggregate PV. While forming the aggregates on REGION and DEPT, the DBMS also sorts the PV on those attributes $[14, pp. 173, 177]$ . Hence, the PV is available in the order required for joining it with the updates. As a result, the additional component of $V\_time$ (over $P\_time$ ), which is the time required for sorting and merging the updates with the PV, is a comparatively lower-cost activity. The $IUV\_cost$ ranges between 2 percent and 7 percent for the larger base tables. The normalized $IUV\_cost$ is lower in the case of the larger base tables for similar reasons—that is, the PV is already sorted.

As in the case of large subsets, all tuples in the base table must be accessed to form aggregates. Hence, an index on the base table is not expected to be beneficial. This was experimentally confirmed and these results are not included in Figure 5c.

## 4.4. Summary of Results

The cost of using IUVs that are based on small subsets of base tables or on aggregate views is generally within an additional 20 percent of the benchmark of retrieving the same information from physically updated base tables. As the size of the base tables increases, the cost of IUVs decreases in percentage terms to about 1 percent to 8 percent of the benchmark, and the normalized IUV\_cost (IUV\_cost adjusted for the size of the base table) reduces.

For IUVs based on small subsets, using an index option on base tables is highly beneficial. Although the $IUV\_cost$ (as per our definition) is higher, the absolute processing cost of IUVs ( $V\_time$ ) is much lower than without indexes.

The cost of IUVs on base tables that must be retrieved in their entirety (large subsets) is generally high except when the queries require the data to be presented to the user in the same order that is required for processing the updates. For IUVs based on a single base table, this cost can be greatly reduced for DBMS, such as INGRES, that can store the base table and the differential table in order by the joining attribute. This can be done because the primary key of the PV is one or more columns of the base table. An alternative is to use clustering and to store the differential tables in the same cluster as the base table.

In summary, except for large tables that must be retrieved in their entirety, IUVs are cost-effective. The overhead is a small percentage of the cost for the benchmark.

## 5. Conclusion

WE HAVE PRESENTED IUVs AS A VEHICLE for implementing “what-if” databases. The cost of using IUVs is analyzed in detail for various classes of views and for various types of queries. Analysis indicates that small subsets and aggregate views of the database are amenable to IUV usage.

Generally, in planning oriented decision making, a decision maker deals with data at aggregated levels (e.g., summaries by branch, by product class), or deals with small meaningful subsets of the large volume of data (e.g., product sales for a given branch, expenses of a given department). These situations require developing competing scenarios and evaluating their effects. Seldom does a decision maker need to directly manipulate large portions of databases or entire base tables in what-if situations. It is thus implied that the cost of using IUVs is favorable in the case of decision making that requires what-if type of analysis.

Throughout our analysis we have compared the cost of using IUVs with the alternative of retrieving the same information from base tables that are assumed to have been updated to create the required scenario. The cost of creating copies of the base tables and updating the copies to create different versions, the cost of disk space to store the versions, and the cost of managing the versions (cataloging, naming, grouping) are not considered. It is difficult to quantify these costs. If these costs are considered, it may become clearer that IUVs are an efficient tool to support what-if databases.

An alternative to forming the PV every time an IUV is retrieved is to materialize the PV. This can be beneficial in cases where the PV is fairly static. For example, the underlying base tables are read-only (or not actively updated), or few base table updates affect the PV. In other cases, when the view is constantly changing, maintaining a materialized PV current at all times can be costly. We are currently investigating this alternative implementation for IUVs.

The results of the experiment suggest several areas where direct DBMS support can substantially reduce the cost of creating what-if scenarios using IUVs. A file structure that reduces the cost of the join between the parent view and the differential table would have the greatest effect. "Ordered relations," as in [21], can be used to store the differential tables. Ordered relations can also be useful when the parent view preserves the primary key of the base table (large and small subsets in the experiment). DBMS, such as INGRES, that allow a table to be accessed through an indexed sequential (ISAM) or a B-tree structure provide similar support in cases where the primary key of the parent view is part of the (single) base table. The base and differential tables can be stored in order by the primary key. An alternative is "join indices" [22] to store the keys of the tuples in the join. Direct support for full outer joins can also result in performance improvements. With the lack of support for full outer joins, systems such as INGRES and DB2 require a UNION of SELECT operations that are separately optimized.

## REFERENCES

1. Adiba, M.E., and Lindsay, B.G. Database snapshots. Proceedings of the International Conference on Very Large Data Bases, October 1980, 86–91.

2. Agrawal, R., and DeWitt, D.J. Updating hypothetical data bases. Information Processing Letters, 16 (1983), 145–146.

3. Bancilhon, F., and Spyratos, N. Update semantics of relational views. ACM Transactions on Database Systems, 6, 4 (December 1981), 557–575.

4. Bates, D.; Boral, H.; and DeWitt, D.J. A framework for research in database management for statistical analysis. Proceedings of the ACM SIGMOD Conference, 1982, Orlando, Florida.

5. Blakeley, J.A.; Larson, P.; and Tompa, F.W. Efficiently updating materialized views. Proceedings of the ACM SIGMOD Conference, 1986, Washington, D.C., May 1986, 61–71.

6. Codd, E.F. The Relational Model for Database Management, Version 2. Reading, MA: Addison-Wesley, 1990.

7. Date, C.J. An Introduction to Database Systems, vol. 2, 5th ed. Reading, MA: Addison-Wesley, 1990.

8. Dattero, R.; Ramirez, R.G.; and Choobineh, J. Derived relations with exceptions: decision support capabilities. Journal of Management Information Systems, 6, 4 (Spring 1990), 83–101.

9. Dayal, U., and Bernstein, P.A. On the updatability of relational views. Proceedings of the Fourth Conference on Very Large Databases, West Berlin, September 1980, 368–374.

10. Hanson, E.N. A performance analysis of view materialization strategies. Proceedings of the ACM SIGMOD Conference, 1987, San Francisco, 440–453.

11. Kamel, N., and Davidson, S. Semi-materialization: performance analysis. Proceedings of the Twenty-fourth Hawaii International Conference on System Sciences, January 1991, 125–135.

12. Katz, R.H., and Lehman, T.J. Database support for versions and alternatives of large design files. IEEE Transactions on Software Engineering, SE-10, 2 (March 1984), 191–200.

13. Lindsay, B.; Haas, L.; Mohan, C.; Pirahesh, H.; and Wilms, P. A snapshot differential refresh algorithm. Proceedings of the ACM SIGMOD Conference, May 1986, Washington, D.C., 53–60.

14. The ORACLE Database Administrator's Guide, Version 5.1, 1989.

15. Ramirez, R.G. Derived relations with exceptions. Ph.D. dissertation, Texas A&M University, 1987.

16. Ramirez, R.G.; Dattero, R.; and Choobineh, J. Extension of relational views to derived relations with exceptions. Information Systems, 15, 3 (1990), 321–333.

17. Ramirez, R.G.; Kulkarni, U.R.; and Moser, K.A. Extending relational systems to support derived data. Technical Report 89/90–8, Decision and Information Systems, Arizona State University, 1990.

18. Severance, D., and Lohman, G. Differential files: their application to the maintenance of large databases. ACM Transactions on Database Systems, 1, 3 (September 1976), 256–267.

19. Stonebraker, M. Implementation of integrity constraints and views by query modification. Proceedings of the ACM SIGMOD International Conference, June 1975, San Jose, CA.

20. Stonebraker, M. Hypothetical data bases as views. Proceedings of the ACM SIGMOD Conference, 1981, Ann Arbor, MI.

21. Stonebraker, M.; Stetner, H.; Lynn, N.; Kalash, J.; and Guttman, A. Document processing in a relational database system. ACM Transactions on Office Information Systems, 1, 2 (April 1983).

22. Valduriez, P. Join indices. ACM Transactions on Database Systems, 12, 2 (1987), 218–246.

23. Woodfill, J., and Stonebraker, M. An implementation of hypothetical relations. Proceedings of the Ninth International Very Large Data Base Conference, December 1983, Florence, Italy.

24. Yao, S.B. Approximating block accesses in database organizations. Communications of the ACM, 20, 4 (April 1977), 260–261.

## APPENDIX: Estimating the Cost of IUVs

ANALYTICAL FORMULAS TO ESTIMATE THE COST of IUVs are presented. Our approach is similar to that of [10] for performance analysis of view materialization strategies. This approach has been cited by other researchers [e.g., 11] for similar studies. We analyze two typical types of parent views: select/project and aggregates. The parameters used in the analysis are:

$N$ size (number of tuples) of relation $R$

b total pages of R (b = NS/B, where S = bytes/tuple, B = bytes/page)

f view predicate selectivity for select-project PV

$f_{dt}$ size of DT as a fraction of $R$

$f_{ag}$ size of aggregate PV as a fraction of $R$

$C_1$ CPU cost in milliseconds (ms) to screen a tuple

$C_2$ CPU cost in ms of a disk read or write

$C_3$ CPU cost in ms to display a tuple to the user

## Select/Project Parent Views

For parent views involving only selections and projections of a base table R, the IUV is obtained by joining R with the differential table DT. A “nested-loop” join strategy is assumed, with R as the outer relation. DT does not require an index because it is likely to be small (considerably smaller than R) and because every tuple of DT is always accessed. A sequential scan is faster under these conditions. DT is assumed to be sorted on the primary key, the join attribute. Two access methods are considered for R. In the first case, R is not indexed and is scanned sequentially. In the second case, R has an unclustered secondary index on the field used in the view predicate. It is also assumed that the pages of DT reside in main memory throughout the computation. The number of pages touched when accessing k out of n records in a file occupying m disk pages can be estimated by the Yao function, $y(n,m,k)$ [24]. Using an unclustered scan, searching for fN out of the N tuples of R on a total of b pages requires $y(N,b,fN)$ reads. Each of the fN tuples needs to be tested against the view predicate. Hence, the cost to retrieve PV using the index is $C_{2}y(N,b,fN)+C_{1}fN$ . Without the index, the cost to sequentially scan R is $C_{2}b$ . The N tuples are screened according to the view predicate at a cost of $C_{1}N$ . Hence, the cost to retrieve PV sequentially is $C_{2}b+C_{1}N$ . The sequential scan of DT requires $f_{dt}b$ reads costing $C_{2}f_{dt}b$ . Each of the fN tuples of PV is matched with the $f_{dt}N$ tuples of DT. Assuming a binary search of DT, since there is at most one match per tuple of PV, this requires $\log_{2}f_{dt}N$ comparisons, resulting in a cost of $C_{1}fN\log_{2}f_{dt}N$ . The final product (IUV) will have the nonmatching tuples of PV (tuples not changed by DT), plus the nonmatching tuples of DT (tuples with “insert” action in DT), plus the matching tuples of DT with the “modify” action, minus the matching tuples of PV with “delete” action in the corresponding DT tuple. The IUV will have approximately the same number of tuples as PV. The cost of displaying these fN tuples to the user is $C_{3}fN$ . These costs are summarized below:

<table><tr><td>Component of IUV cost</td><td>Cost with index on R</td><td>Cost without index on R</td></tr><tr><td>Cost to read and screen tuples of R</td><td> $C_{2}y(N,b,fN) + C_{1}fN$ </td><td> $C_{2}b + C_{1}N$ </td></tr><tr><td>Cost of sequential scan of DT</td><td> $C_{2}f_{dt} b$ </td><td> $C_{2}f_{dt} b$ </td></tr><tr><td>CPU cost to match PV and DT tuples</td><td> $C_{1}fN\log_{2}f_{dt} N$ </td><td> $C_{1}fN\log_{2}f_{dt} N$ </td></tr><tr><td>Cost to display the result</td><td> $C_{3}fN$ </td><td> $C_{3}fN$ </td></tr></table>

## Aggregate Parent Views

For these views, the aggregate is formed by reading the whole table R. No index on R is considered since all tuples of R are accessed. The tuples of R are grouped according to the aggregation attributes and, simultaneously, the aggregate (SUM, AVERAGE, etc.) is computed. It is assumed that a search tree (with an index fan-out d) is built in memory to create and store the aggregate view. The cost of comparing the value in each tuple of R (N tuples) with the value at each level in the tree $\left(\log_{d}f_{ag}N\right.$ levels) is $C_{1}N\log_{d}f_{ag}N$ , where $f_{ag}N$ is the number of tuples in the PV. The cost of recomputing the aggregate (assumed to be the same as $C_{1}$ ) for the N tuples of R is $C_{1}N$ . Hence, the cost of forming the aggregate PV is $C_{1}N\log_{d}f_{ag}N + C_{1}N$ . PV can be made available in its primary key (the aggregation attribute) order if the leaf nodes of the search tree are “chained” as in a B $^{+}$ -tree. Since DT is also available in primary key order, the merge requires only a single pass over the two tables, the cost of which is $C_{1}(f_{ag}N + f_{dt}N)$ . The IUV cost under these assumptions is:

<table><tr><td>Component of IUV cost</td><td>Cost</td></tr><tr><td>Cost of sequential scan of R</td><td> $C_{2}b$ </td></tr><tr><td>CPU cost to form the aggregate</td><td> $C_{1}N\log_{d}f_{ag}N + C_{1}N$ </td></tr><tr><td>Cost of sequential scan of DT</td><td> $C_{2}f_{dt}b$ </td></tr><tr><td>CPU cost to merge PV and DT tuples</td><td> $C_{1}(f_{ag}N + f_{dt}N)$ </td></tr><tr><td>Cost to display the result</td><td> $C_{3}f_{ag}N$ </td></tr></table>
