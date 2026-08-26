---
otero_id: 7582
otero_key: "5HP8M4CT"
title: "Optimizing disk storage to support statistical analysis operations"
authors: "Allen Parrish; Susan Vrbsky; Brandon Dixon; Weigang Ni"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.09.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Optimizing disk storage to support statistical analysis operations

Allen Parrish\*, Susan Vrbsky, Brandon Dixon, Weigang Ni

Department of Computer Science, The University of Alabama, Box 870290, Tuscaloosa, AL 35487-0290, USA

Received 1 September 2001; accepted 30 September 2003 Available online 11 December 2003

## Abstract

Data stored in spreadsheets and relational database tables can be viewed as ‘‘worksheets’’ consisting of rows and columns, with rows corresponding to records. Correspondingly, the typical practice is to store the data on disk in row major order. While this practice is reasonable in many cases, it is not necessarily the best practice when computation is dominated by column-based statistics. This short note discusses the performance tradeoffs between row major and column major storage of data in the context of statistical data analysis. A comparison of a software package utilizing column major storage and one using row major storage confirms our results.

<sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Database systems; Data warehouses; Statistical tools; Business intelligence tools; Data mining

## 1. Introduction

A worksheet is a collection of rows and columns of data. Spreadsheets and relational database tables both represent examples of worksheets. Worksheets associated with such applications are stored in persistent form on disk. In addition, there are a number of statistical analysis applications that operate in a similar fashion to spreadsheets but with more advanced statistical operations. Such applications also manipulate worksheets of data that are stored on disk.

Most commercial applications do not publish their disk data storage formats. However, we believe that the vast majority of worksheet-based applications store their data on disk in row major order (i.e., with each row stored contiguously on the disk). This would be consistent with the row-centric nature of such data, in the sense that each row typically represents a record aggregating a set of information regarding some type of semantic entity. In particular, rows are often inserted or deleted as a unit, and to store rows contiguously is most efficient in the context of record-based updates.

While updates tend to be row-oriented, other operations tend to be column-oriented. In particular, many statistical analysis computations are columncentric and may be applied in many cases to a relatively small number of columns. In the context of column-centric operations, the idea of storing worksheets in column major order (i.e., with each column stored contiguously on the disk) has some merit. In general, the performance tradeoffs between row major and column major storage are not entirely clear in the context of column-centric operations.

In this short note, we examine the performance tradeoffs between row major and column major disk worksheet storage in the context of column-centric statistical analysis operations. In particular, we show that different types of access and update patterns favor one approach over the other. However, under certain realistic conditions, column major storage is much faster than row major storage. Given that the underlying record-based data is typically row-centric, we believe this result is not considered in typical commercial practice.

Column major storage requires the use of some form of indexing whenever a subset of the data is to be analyzed. Without indexing (or a variant thereof), column major storage is prohibitively expensive when accessing a subset of the rows. We introduce a variant of indexes which we call filters. Filters provide efficient data access in column major order but without the transaction-driven overhead of indexing. Filters represent a lightweight implementation of indexes that is sufficient for general statistical processing of subsets and are suitable for either row major or column major order. We discuss performance tradeoffs when processing subsets of data in the context of filters. In addition, we show the results of a simple empirical comparison between statistical packages using column major storage versus row major storage.

## 2. Worksheet storage models

Our overall conceptual model is quite simple. As noted in Section 1, a worksheet is a matrix consisting of rows and columns. We allow for the possibility that the number of rows in each column may be distinct. We can refer to cells in each row and column via indices (e.g., row i, column j). Fig. 1 contains an example of a worksheet.

As discussed in the Introduction, row major order involves storing worksheet rows contiguously on disk; column major order involves storing columns contiguously on disk. While these schemes have been classically regarded for many years as alternatives for in-memory array storage [3], they have not typically been used to discuss disk storage which is our concern here.

<table><tr><td>34</td><td>3</td><td>54</td><td>45</td></tr><tr><td>45</td><td>2</td><td>23</td><td>21</td></tr><tr><td>2</td><td>34</td><td>12</td><td>13</td></tr><tr><td>1</td><td>1</td><td>34</td><td>32</td></tr></table>

Fig. 1. Worksheet.

<table><tr><td colspan="4">Physical block</td></tr><tr><td>34</td><td>3</td><td>54</td><td>45</td></tr><tr><td>45</td><td>2</td><td>23</td><td>21</td></tr><tr><td>2</td><td>34</td><td>12</td><td>13</td></tr><tr><td>1</td><td>1</td><td>34</td><td>32</td></tr></table>

Fig. 2. Row major order.

Simple implementations of row major and column major order are as follows. For row major order (Fig. 2), each row could be stored as a logical record within a flat file, with some kind of separation delimiter between the various columns. In the example each row is a proper subset of a physical block. Fig. 2 illustrates row major storage of the worksheet in Fig. 1.

For column major order (Fig. 3), the above file is ‘‘inverted,’’ much as if it were a standard matrix. In particular, the ith physical block contains the ith column of the worksheet. In the example, each column is a subset of its physically containing block. Fig. 3 illustrates column major storage of the worksheet in Fig. 1.

## 3. Performance analysis

We briefly consider a simple performance comparison between the row major and column major approaches. In conducting this analysis, we first assume that the worksheet is rectangular (that is, that every column has an equal number of rows and every row has an equal number of columns). As such, adding or deleting a row requires adding or deleting values for all columns. Similarly, adding or deleting a column requires adding or deleting values for all rows. This rectangularity assumption is typical for databases, although it is less necessary for statistical packages.

<table><tr><td colspan="4">Physical block</td></tr><tr><td>34</td><td>45</td><td>2</td><td>1</td></tr><tr><td>3</td><td>2</td><td>34</td><td>1</td></tr><tr><td>54</td><td>23</td><td>12</td><td>34</td></tr><tr><td>45</td><td>21</td><td>13</td><td>32</td></tr></table>

Fig. 3. Column major order.

We focus principally on the cost of performing a simple statistical computation on the worksheet. We choose the frequency distribution (FREQ) operation as representative of a class of statistical operations (such as minimum, maximum, sum, average, median, mode, etc.) which can be applied to one or more columns of the worksheet. (While FREQ could also be applied to rows, we assume that it is predominantly of interest on columns. This is consistent with the arguments made in Section 1 regarding the rowcentric nature of most data.) FREQ counts the number of occurrences of each value in the column and produces a table and/or histogram representing the distribution. Although many statistical operations are more complex than FREQ, their disk and memory costs are proportional to FREQ when the two storage schemes are compared. In particular, each of these operations requires access to the values for each row for one particular column as well as maintenance of a single value in memory.

We assume that there are n rows and k columns in the worksheet. Moreover, to simplify the analysis, we assume that the block size is exactly k. Thus, with row major storage, each row consumes exactly one physical block. However, for column major storage, a column may span multiple blocks. These assumptions are realistic in that for most data sets of significant size, the number of rows (records) will be much larger than the number of columns (attributes). Hence, a column is going to span multiple blocks, while a row will be much closer to the size of a single block.

With column major storage, qn/ka disk reads are required to perform FREQ on a single column. The number of disk reads required to perform FREQ on f variables with inverted storage is therefore qn/ka f. On the other hand, exactly n reads are required to perform FREQ when row major storage is used regardless of the size of f. Note that as f increases, the time requirement for column major storage approaches the time requirement for row major storage. In particular, when f = k, exactly n disk reads are required in both cases.

Because statistics may often be computed on a small number of columns relative to the size of the worksheet, column major storage is more efficient than row major storage on column-oriented statistical operations. Indeed, when the number of columns involved in the computation is truly small, column major storage is much more efficient than row major storage. Of course, this assumes that statistical operations are entirely column-based in accordance with the model described in Section 1.

When considering other operations (such as additions and deletions that modify the worksheet), column major storage becomes less desirable. In particular, with the rectangularity constraint, rows and columns must be added and deleted as a whole. With row major storage, adding or deleting a row will require only one disk access. With column major storage, however, adding or deleting a row will require k disk accesses (because each column for a given row appears in a separate block). Because adding a row is a common database operation, column major storage is likely to be a disadvantage in a transaction-based environment where the worksheet is frequently modified in a rowbased fashion. Indeed, with a complete RDBMS system, it is likely that row major storage is most efficient for database tables because of the support for transactions as well as for joins and other general relational operations. Of course, if the rectangularity constraint is eliminated, then additions and deletions can occur one value at a time (rather than a whole row or column), not requiring multiple disk access for any single change. Without the rectangularity constraint, row major order offers no performance advantage in the context of updates.

## 4. Subsets, indexes and filters

It is typical for most worksheet-based applications to allow access to a subset of the rows in a particular worksheet. Such subsets are typically based on Boolean restrictions over a subset of the columns in the row. With a conventional RDBMS, one can optionally define indexes (which can be retained in files) in order to provide fast access to a subset of records satisfying particular sets of criteria [1]. Indexes are constructed on one or more columns and may be used to efficiently access records satisfying any Boolean criterion over those columns.

Indexes may be used with row major or column major worksheet storage. Indexes are particularly

Table 1

geared toward transactional RDBMS systems and require overhead to support transactions and relational operations. As Section 3 discussed, column major storage is not generally a good strategy for transactional RDBMS systems. As such, we propose a variant of the standard index that we call a filter. Filters are applicable to row major or column major worksheet storage and require less overhead than indexes. In particular, a filter is a bit string of length n, where the ith bit specifies in the obvious way whether the ith row (record) is part of the analysis (‘0’ out, ‘1’ in). Filters allow the specification of a complex Boolean expression of dataset variables to identify subsets of the data. Filters are applied during the analysis process to specific files containing variables for which analysis is desired by serving as a mask to control which values are read. In particular, values are only read from files corresponding to positions within the bitmap containing a ‘1’. Effectively, filters define specific subsets, while indexes provide a mechanism to obtain fast access to any subset whose membership criterion is based on the columns used within the index.

We note that indexes are optional with row major order. Without an index, it is still possible to make a single pass through the worksheet. When each row is read, it can be analyzed at that point to determine whether it is in the desired subset (i.e., on the fly). However, with column major order, the lack of a filter or index can increase the number of disk reads. Without filters in column major order, each analysis operation requires qn/ka j disk reads, where k is the block size; n is the number of records; and j is the number of variables to define the filter. Thus, if there are f analysis operations, the total time required is proportional to qn/ka( f + j). As j becomes larger, this extra cost becomes prohibitive, making filters very important for implementing subset restrictions in the context of column major order. Filters can also be used as part of a row major storage implementation as an alternative to more traditional indexing, with similar performance benefits.

In order to conduct a fair comparison involving subset restrictions between row major and column major order implementations, we assume the use of the same bitmap model of filters for both implementations as described above. We first consider filter creation cost. If the number of variables in the Boolean expression defining a filter is j and there are n rows with block size k, then jqn/ka disk reads are required to construct a filter in the context of column major storage. On the other hand, n disk reads are required in a row major storage implementation.

We now consider the number of disk reads required for both row major and column major storage structures when filters are involved. We first consider column major storage. The best case for column major occurs when the values in the subset defined by the filter are clustered so as to minimize the number of disk reads. For example, suppose there are g values in the subset defined by the filter. Then if all g values are contiguous, and $g < k ,$ , then only one disk access is required for each variable in the frequency analysis. Thus, in a case where only one variable is involved in the frequency analysis, it is possible to only require one disk access for the entire analysis. The worst case occurs if the g values are distributed, such that each value occurs in a different block, in which case g disk accesses are required for each of the f variables in the frequency analysis (i.e., fg).

On the other hand, with row major storage, exactly g disk accesses are required for any frequency analysis, regardless of the number of variables in the analysis. Thus, the worst case for row major storage is better than the worst case for column major storage by a factor of f (the number of variables in the analysis). Table 1 shows the summary of this comparison.

A performance comparison involving a complete traditional implementation of indexing will be similar to this one. The difference is that the cost of managing the index is higher than that of managing the filter. Because transactional systems are not amenable to column major order, indexing mechanisms with their associated overhead introduces unnecessary complexity into this analysis.

In Fig. 4(a) and (b), we further illustrate the performance differences between the row major and column major storage methods by utilizing specific values for the block size, database size, number of columns, etc. The figures show the time to access the

Row major versus column major storage access with filters

<table><tr><td></td><td>Column major storage</td><td>Row major storage</td></tr><tr><td>Best case</td><td>f</td><td>g</td></tr><tr><td>Worst case</td><td>fg</td><td>g</td></tr></table>

![](/api/attachments/5HP8M4CT/fulltext/images/10f1bea5f2b8517ef2b14190ab22f5bd6c7f5e0e87cca1cf6e7881299efa21f9.jpg)

![](/api/attachments/5HP8M4CT/fulltext/images/94e8ead4acdc89df71889852f6c18222722778873ec3d826c9348351b59cfd2b.jpg)  
Fig. 4. Access time for varying numbers of data values. (a): Small numbers of columns. (b): Large numbers of columns.

data values in seconds, for varying numbers of data values accessed. In these figures, we assume a database with 100,000 rows and 200 columns, and we assume a block (page) size equal to 200 data elements. In the row major method, we assume that one record of data fits on one block, and in the column major method, we assume 200 data values fit per block (requiring 500 blocks of data for each column). The time to access the data is based on a fast disk access rate of 10 ms to access one block of data.

Fig. 4(a) illustrates the number of seconds to access the data for 1 to 5500 data items. The diagonal line illustrates the time to access the data using a row major storage method, and it ranges from 0.01 to 55 s. As mentioned previously, with each additional data value to access, the row major storage method requires an additional record to be read, and hence, results in an additional disk access. The best and worst cases for the row major storage method are the same.

The results for the column major storage method are also illustrated for the column major best case in Fig. 4(a). In the best case, we assume that all of the requested data values are clustered on the same pages. The best case for column major storage with one column is the lowest line in the graph. The time to access the data for one column ranges from 0.01 to 0.11. The best case, when 10 columns are requested, is similar to the one-column line, as values range from 0.1 to 1.1.

We also illustrate the time to access the data for the column major in the worst case, which occurs when each data value requested is stored on a different block. Fig. 4(a) shows the access time for 1 to 5500 data items for the worst case row major when 1 column, 2 columns, 5 columns and 10 columns are requested. The row major method is not affected by the number of columns requested because the entire record, with all of its columns, are accessed each time. However, this is not the case for the column major method. As illustrated in Fig. 4(a), the time to access one column of the data is the same for the worst case column major and the row major until more than 500 values are requested. At this point, all of the blocks for the requested column have been accessed, and hence, the time to access additional data values does not increase for the column major and remains at 5 s. The worst case column major for two columns is greater than the row major method until more than 1000 values are requested, but then again it remains less than the row major. A similar trend is illustrated for the column major worst case when 5 and 10 columns are accessed. We emphasize that Fig. 4(a) only illustrates the results for 5500 of the 100,000 data values per column, and as the percentage of the data that is included in the filter increases, the time to access the data for the row major method continues to increase, while the time for the worst case column major method remains the same.

Fig. 4(b) illustrates the access time for large numbers of columns (100 and 200) for accessing 1 to 100,000 data values for the row major, best case column major and worst case column major methods. An average case would fall somewhere in between the best and worst cases illustrated in Fig. 4. The best case results for 100 and 200 columns remain significantly smaller than those for the row major or worst case column major method. The results for 100 columns when the worst case column major is utilized are worse than the row major until 50,000 data values are accessed. When more than 50,000 data values are access, the row major has a higher access rate. The row major has a shorter access time than the column major worst case with 200 columns for all values until all 100,000 of the data values are read.

The disk access time is typically more time consuming than the computation of the data. An efficient implementation could hide the cost of processing the data, but if not hidden, we would expect that the time to process the data would increase proportionally with the number of data items processed for both row and column major methods. However, we would still expect the disk access time to dominate the time to process the data. We also note that we expect an implementation of row major and column major storage methods to use additional efficient disk access strategies, such as reading more than one page at a time (prefetch), to improve disk access.

In summary, if the number of variables being processed is small, then column major storage with filters (or indexing) is the less expensive implementation in the context of subset restrictions. Filters (or indexing) represent an essential mechanism for dealing with subset restrictions with column major storage and a useful mechanism with row major storage if a large number of analysis operations are conducted with a fixed subset.

## 5. A column major implementation

The Critical Analysis Reporting Environment (CARE) is a software system developed for traffic crash problem identification and evaluation [2]. CARE was originally developed to provide analytical processing of traffic crash report databases. CARE has been developed principally as a standalone product for the Windowsk platform, although a client–server version also exists that runs over the World Wide Web. CARE stores its data entirely in disk-based worksheets in column major order. Filters are used to support the retrieval of subsets. CARE exclusively processes categorical data, that is, data that are either nominal or ordinal, reflecting the type of multiple-choice data typically recorded on traffic crash reports. CARE implements a model of filters (as defined in Section 4) to deal with data subsets.

In this section, we compare the performance of CARE with a well-known statistical package (SPSS) in a limited illustration. This illustration, although not a complete experiment, supports the analysis provided in Section 4. As noted above, the CARE data storage structure is in column major order; although the storage organization for SPSS is not published to our knowledge, we expect that it is row major.

The same data files were used when running both CARE and SPSS. The data consisted of an actual data file from the Alabama Department of Transportation containing Alabama traffic crash data. There were 137,713 rows and 217 columns in the table. We initially accessed all of the data records in the table. We then varied the number of columns on which to perform the frequency counts as: 1, 10, 50, 100, 150 and 200 columns. Table 2 contains our results (in s) in computing frequency counts.

Note the table confirms our previous analysis in Section 3. In particular, when analyzing only a small number of columns, CARE’s performance (using column major storage) is significantly better than either of the row major storage implementations. However, as more columns are added, the performance worsens significantly; with 200 columns, CARE is actually slightly worse than SPSS.

We also examined the performance when a subset of records was selected. We selected a subset of approximately 50% of the records, chosen by selecting specified data values for one of the columns. In CARE, filters were created on a column to select the desired subset, while in SPSS, the Select Cases option was used. Table 3 illustrates our results in this case.

Table 2  
Performance results (in s) from selecting 100% of the data records

<table><tr><td></td><td>1Column</td><td>10Columns</td><td>50Columns</td><td>100Columns</td><td>150Columns</td><td>200Columns</td></tr><tr><td>CARE</td><td>0.1</td><td>1.1</td><td>4.4</td><td>8.8</td><td>14.1</td><td>19.3</td></tr><tr><td>SPSS</td><td>4.3</td><td>5.2</td><td>7.8</td><td>11.1</td><td>13.8</td><td>17.25</td></tr></table>

Table 3  
Performance results (in s) from selecting 50% of the data records

<table><tr><td></td><td>1Column</td><td>10Columns</td><td>50Columns</td><td>100Columns</td><td>150Columns</td><td>200Columns</td></tr><tr><td>CARE</td><td>0.1</td><td>1.0</td><td>4.1</td><td>8.2</td><td>13.3</td><td>18.6</td></tr><tr><td>SPSS</td><td>3.7</td><td>4.8</td><td>6.3</td><td>8.7</td><td>10.1</td><td>11.5</td></tr></table>

Our results in Table 3 are generally similar to Table 2, where all of the records were utilized in the analysis. Utilizing the Select Cases of SPSS reduces the total number of disk accesses to the number of cases in the subset selected. However, in the case of column major order, utilizing a filter in CARE will reduce the number of disk accesses, but as discussed in Section 4, one cannot predict by how much. With 200 columns in Table 3, SPSS is substantially faster than CARE. However, CARE (with its column major data storage) is still substantially faster than SPSS when a small number of columns is used in the analysis.

## 6. Conclusion

In this paper, we have compared the performance of applications using disk-based data worksheets in two storage formats: row major versus column major. Our conclusion is that column major order is better in situations where a small number of variables are being analyzed, provided that updates are infrequent. Because this is not the typical case in general purpose database systems, the applicability of column major order is restricted to special purpose data analysis applications such as our CARE system presented in Section 5. While this is a very simple concept, we see little or no evidence of column major order even in the context of special purpose applications. In cases where small numbers of variables but large numbers of data values are analyzed, column major order provides substantial performance improvements.

## References

[1] R. Elmasri, S. Navathe, Fundamentals of Database Systems, Addison-Wesley, Boston, MA, 2000.

[2] A. Parrish, B. Dixon, D. Cordes, S. Vrbsky, D. Brown, CARE: a tool to analyze automobile crash data, IEEE Computer 36 (6) (2003 June), pp. 22– 30.

[3] M. Scott, Programming Language Pragmatics, Morgan-Kauf man, San Francisco, CA, 2000.

![](/api/attachments/5HP8M4CT/fulltext/images/11cbf9d419d87187c1672706d232d8f674a58cf3f594709b19f2ccbd13a0fb9f.jpg)

Allen Parrish is an Associate Professor in the Department of Computer Science and Director of the CARE Research and Development Laboratory at The Uni versity of Alabama. He received a PhD in Computer and Information Science from The Ohio State University in 1990. His research interests are in soft ware testing, software deployment, data analysis and visualization, and highway safety information systems.

His sponsors have included the National Science Foundation, the Federal Aviation Administration, the National Highway Traffic Safety Administration and a variety of highway safety-related state agencies. He is a member of the IEEE Computer Society Educational Activities Board.

![](/api/attachments/5HP8M4CT/fulltext/images/3f2875c0995053b1b3c1c8e97c839b205bdba242b28206e36da9e899849dc726.jpg)

Susan V. Vrbsky is an Associate Professor in the Department of Computer Science at The University of Alabama. She received her PhD in Computer Science from The University of Illinois, Urbana-Champaign in 1993. Her research interests include database systems, uncertainty and approximations, real-time database systems and mobile data management. Her sponsors have included the National Science Foundation, the Federal Aviation Administration

and the Alabama Department of Transportation.

Brandon Dixon is an Associate Professor in the Department of Computer Science at The University of Alabama. He received a PhD in Computer Science in 1993 from Princeton University. His interests are in computer science theory, algorithm design and software engineering. His current research sponsors include the National Science Foundation, NASA, the Federal Aviation Administration and the Alabama Department of Transportation.

Weigang Ni is a PhD candidate in the Department of Computer Science at The University of Alabama. He is expected to receive his degree in December 2003. His research interests include real-time databases and mobile databases.
