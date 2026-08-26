---
otero_id: 21227
otero_key: "FF3R5HVX"
title: "Space-efficient cubes for OLAP range-sum queries"
authors: "Seok-Ju Chun; Chin-Wan Chung; Seok-Lyong Lee"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00003-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Space-efficient cubes for OLAP range-sum queries

Seok-Ju Chun $^{a}$ , Chin-Wan Chung $^{b,*}$ , Seok-Lyong Lee $^{c}$

$^{a}$ Department of Information and Communication Engineering, Korea Advanced Institute of Science and Technology, 373-1 Kusung-dong, Yusung, Taejon 305-701, South Korea

$^{b}$ Division of Computer Science, Korea Advanced Institute of Science and Technology,

373-1 Kusung-dong, Yusung, Taejon 305-701, South Korea $^{c}$ School of Industrial and Information System Engineering, Hankuk University of Foreign Studies, 89 Wangsan-ri Mohyun, Yongin-si, Kyounggi-do, South Korea

Received 1 September 2002; accepted 1 December 2002

## Abstract

Data cubes support a powerful data analysis method called the range-sum query. The range-sum query is widely used in finding trends and in discovering relationships among attributes in diverse database applications. A range-sum query computes aggregate information over an online analytical processing (OLAP) data cube in specified query ranges. Existing techniques for range-sum queries on data cubes use an additional cube called the prefix sum cube (PC), to store the cumulative sums of data, causing a high space overhead. This space overhead not only leads to extra costs for storage devices, but also causes additional propagations of updates and longer access time on physical devices.

In this paper, we present a new cube representation called ‘the PC Pool’, which drastically reduces the space of the PC in a large data warehouse. The PC Pool decreases the update propagation caused by the dependency between values in cells of the PC. We develop an effective algorithm, which finds dense sub-cubes from a large data cube. We perform an extensive experiment with diverse data sets, and examine the space reduction and performance of our proposed method with respect to various dimensions of the data cube and query sizes. Experimental results show that our method reduces the space of the PC while having a reasonable query performance.

© 2003 Elsevier B.V. All rights reserved

Keywords: Range-sum query; OLAP; Data cube; Clustering

## 1. Introduction

Data cubes are data structures that store subsets of the data warehouse data for quick response to user queries. Data cubes usually store aggregations and summaries of the data in the data warehouse or even the OLTP database. Data cubes return the values of attributes that affect the decision making process in the organization such as sales amount, inventory, etc. [21]. To build a data cube for a data warehouse, certain attributes are chosen to be measure attributes, i.e., the attributes whose values are of interest. Other attributes are selected as dimensions or functional attributes. The measure attributes are aggregated according to the dimensions. For example, consider a data cube maintained by an insurance company. It is assumed that the data cube has four dimensions CUSTOMER\_AGE,

YEAR, REGION and INSURANCE\_TYPE and one measure attribute AMOUNT\_OF\_SALES. Let the domain of CUSTOMER\_AGE be between 1 and 120, of YEAR be 1992–2001, of REGION contain 40 regions, and of INSURANCE\_TYPE be {home, auto, health}. Then the data cube has $120 \times 10 \times 40 \times 3$ cells, and each cell contains the value of AMOUNT\_OF\_SALES as a measure attribute for the corresponding combination of four functional attributes.

The data cube is a data structure that enables a range-sum query that applies an aggregate operation to the measure attribute within the range of the query. The range query is a very useful tool in finding trends and in discovering relationships among attributes in a data warehouse $[13]$ . A typical example includes “Find the total amount of sales in NY for customers aged from 26 to 45 with auto insurances, in years 1998–2001”. Queries of this form are very useful in finding trends and in investigating relationships among attributes in a data warehouse. Much work $[4,6,8,9,13]$ has been done to develop algorithms, which reduce the response time of queries significantly. Those methods use an additional cube called the prefix sum cube (PC). However, in typical online analytical processing (OLAP) applications, the data are massive and yet sparse, that is, number of nonzero cells in the data cube is much smaller than the total number of cells. This provides an opportunity to improve on the existing methods by taking advantage of the data sparsity. For example, let us consider real-world data from the U.S. Census Bureau using their Data Extraction System (DES) $[18]$ . Only 11 attributes are chosen from 372 attributes for an analysis as follows: A measure attribute is income, and 10 functional attributes are age, marital\_status, sex, education, race, origin, family\_type, detailed\_household\_summary, age\_group, and class\_of\_worker. Although the data cube is 10-dimensional resulting with more than 16 million cells, the density of the cube is about 0.001. There are only 15,985 nonzero elements $[19]$ . Our aim in this paper is to develop a system, which drastically reduces the space requirement in a large data warehouse as well as the cost of queries and updates.

In this paper, we present a new technique called ‘the PC Pool’, which stores a large sparse data cube in a space-efficient manner. Based on dense intervals, we identify a set of dense sub-cubes with respect to a given density threshold. We build multiple small PCs, one for each sub-cube in the set, and store them into the PC Pool. The PC Pool reduces drastically the space requirement. We also use a data structure called ‘Δcube’ for maintaining both outlier cells and changed cells in the data cube efficiently. The Δcube reduces the update propagation caused by the dependency between values in cells of the PC. We explain how dense sub-cubes are identified, how outlier cells are represented, how queries and updates are processed efficiently with our proposed method.

Our contributions are summarized as follows:

\- We present a new cube representation called ‘the PC Pool’, which drastically reduces the space using clustering techniques in a large data warehouse. We provide an analysis with various sizes of data cubes and an experimental evaluation, which shows that our method performs very efficiently on various dimensionalities.

\- We develop a new clustering technique suitable for sparse data cubes. The technique efficiently finds dense intervals in each dimension and constructs sub-cubes based on the dense intervals.

The remainder of the paper is organized as follows. In Section 2, related work is given. Section 3 provides a detailed description of our proposed work. The method to find dense sub-cubes is explained in Section 4. The experimental evaluation of our approach is discussed in Section 5. Section 6 concludes the paper.

## 2. Related work

There are two classes of methods for processing OLAP queries: exact methods and approximate methods. Much work has been done on providing an exact answer to a query over the data cube. Ho et al. [12] have presented an elegant algorithm for computing range queries in data cubes, which we call the prefix sum approach. The essential idea of the prefix sum approach is to precompute many prefix sums of the data cube, which can be used to answer ad hoc queries at run-time. This approach shows that range-sum queries are processed in constant time regardless of the size of the data cube. But it is very expensive to maintain the PC when data elements in the data cube are frequently changed. Recently, various excellent studies $[4,6,8,9,13]$ , which are based on the prefix sum approach, have been made to reduce the update cost. But, the biggest problem with these approaches is that the PC is typically very dense even when the original data cube is sparse. Therefore, the PC takes a large amount of space. The space overhead not only leads to extra costs for storage devices, but also causes additional propagations of updates and longer access time on physical devices $[16]$ .

On the other hand, various approximate methods for processing OLAP queries are studied in Refs. $[2,17,19,20]$ . These works have been done on approximating data cubes through various forms of compression techniques such as wavelet $[19,20]$ and statistical structures of data $[2,17]$ . All these approaches have good advantages in both space and time. However, in these methods the exact answer is not optional. If all queries are responded by approximate answers, they cannot be used for supporting a critical decision.

## 3. Proposed work

## 3.1. Motivating example

Analysts may want to explore the relationship among diverse attributes to find business trends and opportunities. A data cube for such analysis should have a high dimensionality. However, a high dimensionality causes the data cube to be very sparse. The following example shows that a data cube is highly sparse $[15]$ .

Example 1. We consider a data cube of eight dimensions. Table 1 shows the US census data cube, which contains more than $2 \times 10^{14}$ cells. When we assume that the US census bureau stores data for 200 million Americans, at most 0.0001% of the cells will be nonempty.

Table 1  
Attributes and their domains for a census data set

<table><tr><td>Attribute</td><td>Domain</td><td>Attribute</td><td>Domain</td></tr><tr><td>Age</td><td>0–150</td><td>Income</td><td>0–99999</td></tr><tr><td>Weight</td><td>1–500</td><td>Race</td><td>1–5</td></tr><tr><td>Family type</td><td>1–5</td><td>Marital status</td><td>1–7</td></tr><tr><td>Class of worker</td><td>0–8</td><td>Education</td><td>1–17</td></tr></table>

In Ref. [12], Ho et al. developed techniques to guarantee the access time for range-sum queries that is independent of the size of the query-cube (constant cost) by pre-aggregating information in the data cube [15]. This approach uses an additional cube called the PC to store the cumulative sum of data. The PC is dense even when the original data cube is sparse. The existing works until now have focused on the response time of queries and updates, and have not considered the storage overhead seriously. In reality, these approaches using the PC cause a severe storage overhead and also incur an update propagation problem caused by the dependency between values in cells of the PC. If the OLAP system has a limited storage, it is not possible to implement the PC. Furthermore, the update propagation problem is amplified as the size of the PC increases.

## 3.2. Idea

Many data warehouses contain numerous small regions of clustered multidimensional data (dense region), with points sparsely scattered over the rest of the space $[5]$ . The basic idea of our method is that we find and group dense sub-cubes based on the density function in a large sparse data cube. Then, for each subcube we build a PC and store it into the PC Pool. The cells in the data cube that are not contained in these sub-cubes are regarded as outliers and stored in the $\Delta$ cube. When a range-sum query is processed, the PC Pool and $\Delta$ cube are manipulated simultaneously. Fig. 1 shows the basic concept of the PC Pool and $\Delta$ cube. Detailed descriptions on the PC Pool and $\Delta$ cube are given in Sections 3.3 and 3.4, respectively.

The ideas proposed in this paper are summarized as follows:

\- We find a set of dense sub-cubes that satisfy predefined density conditions. Instead of building one huge PC, we build multiple small PCs, one for each sub-cube in the set, and store them into the PC Pool. This drastically reduces the space requirement of a large sparse data cube and relieves the update propagation problem in some degree. A detailed description for finding dense sub-cubes is presented in Section 4.

\- Whenever a cell of a data cube is changed, we compute the update cost (UCOST), which is the number of cells to be accessed for updating the PC Pool. If UCOST is less than a given time bound, we update the corresponding PC in the PC Pool directly. Otherwise, we store the changed cell into the $\Delta$ cube. The size of the $\Delta$ cube can increase monotonically over time. When the $\Delta$ cube is too large, the cost of search and update becomes high. Thus, all updated information stored in the $\Delta$ cube needs to be reflected on the PC Pool periodically, i.e., weekly, monthly, or at some threshold, depending on applications.

![](/api/attachments/FF3R5HVX/fulltext/images/3aa3d391e32d3c48ce31fe9bae589939bf4b6ed926bdbc661ce3cd01b4f03f9e.jpg)  
Fig. 1. The basic concept of the PC Pool and $\Delta$ cube.

\- As new cells are inserted into a data cube or existing cells fade away, dense sub-cubes in the data cube are subject to a change. When the PC Pool dose not reflect dense sub-cubes of the data cube appropriately, it needs to be rebuilt off-line.

## 3.3. Building PC pool

In this section, we briefly introduce the background of the PC and discuss the algorithm that builds the PC Pool from dense sub-cubes. Let $D=\{1,2,\ldots,d\}$ denote the set of dimensions and $n_{i}$ denote the cardinality of dimension i. Then, we represent a d-dimensional data cube by $C[0:n_{1}-1,\ldots,0:n_{d}-1]$ . The problem of computing a range-sum query in a d-dimensional data cube can be formulated as follows:

$$
\begin{array}{l} \text { Sum } (l _ {1}: h _ {1}, l _ {2}: h _ {2}, \ldots , l _ {d}: h _ {d}) \\ = \sum_ {i _ {1} = l _ {1}} ^ {h _ {1}} \dots \sum_ {i _ {1} = l _ {d}} ^ {h _ {d}} C [ i _ {1}, \dots , i _ {d} ]. \end{array}
$$

The range parameters $l_{j}$ , $h_{j}$ for all $j \in D$ is specified by a user and typically not known in advance. We represent a d-dimensional PC by PC[0:n\_{1}-1, ...,

$0:n_{d}-1]$ . PC will be used to store precomputed prefix sums of C. We will precompute, for all $0 \leq x_{j} < n_{j}-1$ and $j \in D$ ,

$$
\begin{array}{r l} \mathrm{PC} [ x _ {1}, x _ {2}, \dots , x _ {d} ] & = \operatorname{Sum} (0: x _ {1}, 0: x _ {2}, \dots , 0: x _ {d}) \\ & = \sum_ {i _ {1} = 0} ^ {x _ {1}} \sum_ {i _ {2} = 0} ^ {x _ {2}} \dots \sum_ {i _ {d} = 0} ^ {x _ {d}} C [ i _ {1}, \dots , i _ {d} ] \end{array}\tag{1}
$$

Ho et al. [12] have presented a simple method which needs $N=\prod_{i=1}^{d}n_{i}$ additional cells to store precomputed prefix sums such that any d-dimensional range-sum can be computed in $2^{d}-1$ steps, based on up to $2^{d}$ appropriate precomputed prefix sums. Lemma 1 [8] below provides how any range-sum query for C can be computed from up to $2^{d}$ appropriate elements of the PC. The left-hand side of Eq. (2) specifies a range-sum of C. The right-hand side consists of $2^{d}$ additive terms, each of which is from an element of PC with a sign “+” or “-” determined by the product of all $s(j)$ s. For notational convenience, let $PC[x_{1},x_{2},\ldots,x_{d}]=0$ if $x_{j}=-1$ for some $j\in D$ .

Lemma 1

$$
\text { For   all } j \in D, \text { let } s (j) = \left\{ \begin{array}{l l} 1, & \text { if } x _ {j} = h _ {j}, \\ - 1, & \text { if } x _ {j} = l _ {j} - 1, \end{array} \right.
$$

Then, for all $j \in D$ ,

$$
\begin{array}{l} \text { Sum } (l _ {1}: h _ {1}, l _ {2}: h _ {2}, \dots , l _ {d}: h _ {d}) \\ = \sum_ {\forall_ {x _ {j}} \in \{l _ {j} - 1, h _ {j} \}} \left\{\left(\prod_ {j = 1} ^ {d} s (j)\right) \mathrm{PC} [ x _ {1}, x _ {2}, \dots , x _ {d} ] \right\} \end{array}\tag{2}
$$

![](/api/attachments/FF3R5HVX/fulltext/images/72389cdf1765c4bbc55aed3a9d3b9a35b9871b022884e6840ff86d209ce2f9c3.jpg)  
(a)

![](/api/attachments/FF3R5HVX/fulltext/images/efe98bf4e2cb070423f1dbed5df0ea8ec3ce6f47283bbae9e95d849a2c0c01da.jpg)  
Fig. 2. The basic concepts of the PC Pool. (a) Data cube $C$ (b) PC Pool v.

PC Pool v is a set of PCs, which have been made from dense sub-cubes. Let $v = \{PC_{k} | k = 1, 2, \ldots, m\}$ and m be the number of dense sub-cubes. We can represent the k-th dense sub-cube by $C[pl_{k,1}:ph_{k,1}, \ldots, pl_{k,d}:ph_{k,d}]$ . Therefore, the equation for building $PC_{k}$ is as follows: For all $0 \leq pl_{k,i} \leq x_{i} \leq ph_{k,i} < n_{i}$ and $i \in D$ ,

$$
\begin{array}{l} \mathrm{PC} _ {k} [ x _ {1}, x _ {2}, \dots , x _ {d} ] = \operatorname{Sum} (p l _ {k, 1}: x _ {1}, p l _ {k, 2} \\ : x _ {2}, \dots , p l _ {k, d}: x _ {d}) = \sum_ {i _ {1} = p l _ {k, 1}} ^ {x _ {1}} \sum_ {i _ {2} = p l _ {k, 2}} ^ {x _ {2}} \dots \sum_ {i _ {d} = p l _ {k, d}} ^ {x _ {d}} \\ \times C [ i _ {1}, \dots , i _ {d} ] \end{array}\tag{3}
$$

Example 2. Consider an $8 \times 8$ data cube shown in Fig. 2a. The data cube is sparse and not uniformly distributed. Let five dense sub-cubes be identified in the process of finding dense sub-cubes. We can build PCs for five dense sub-cubes, respectively, and store them into the PC Pool as shown in Fig. 2b.

Lemma 2 states how the range-sum query for $PC_{k}$ can be computed from up to $2^{d}$ appropriate elements of $PC_{k}$ . The left-hand side of Eq. (4) specifies a range-sum of C for $PC_{k}$ . The right-hand side of Eq. (4) consists of $2^{d}$ additive terms, each of which is an element of $PC_{k}$ with a sign “+” or “−” determined by the product of all $s(j)$ s. For notational convenience, let $PC_{k}[x_{1},x_{2},\ldots,x_{d}]=0$ if $x_{j}<pl_{j}$ for some $j\in D$ .

## Lemma 2

For all $j\in D$ , and $s(j)$

$$
= \left\{ \begin{array}{l l} 1, & \text { if   } x _ {j} = h _ {j} \text {   or   } x _ {j} = p h _ {j}, \\ - 1, & \text { if   } x _ {j} = l _ {j} - 1, \end{array} \right.
$$

Then, for all $j \in D$ , $X_{j}$

$$
= \left\{ \begin{array}{l l} \{p h _ {j} \}, & \text { if } l _ {j} \leq p l _ {j} \leq p h _ {j} \leq h _ {j}, \\ \{h _ {j} \}, & \text { if } l _ {j} \leq p l _ {j} \leq h _ {j} <   p h _ {j}, \\ \{l _ {j} - 1, h _ {j} \}, & \text { if } p l _ {j} <   l _ {j} \leq h _ {j} \leq p h _ {j}, \\ \{l _ {j} - 1, p h _ {j} \}, & \text { if } p l _ {j} <   l _ {j} \leq p h _ {j} <   h _ {j} \end{array} \right.
$$

and

$$
\begin{array}{l} \operatorname{Sum} _ {k} \left(l _ {1}: h _ {1}, l _ {2}: h _ {2}, \dots , l _ {d}: h _ {d}\right) = \sum_ {\forall_ {x _ {j}} \in X _ {j}} \left\{\binom {d} {j = 1} s (j)\right) \\ \times \mathrm{PC} _ {k} \left[ x _ {1}, x _ {2}, \dots , x _ {d} \right] \Bigg \} \end{array} \tag {4}\tag{4}
$$

Proof. (See Appendix A.)

Example 3. Fig. 3 gives the relationship between $PC_{k}[pl_{1}:ph_{1}]$ and range-sum query $Q(l_{1}:h_{1})$ when d=1. There can be four cases of relationships as follows:

![](/api/attachments/FF3R5HVX/fulltext/images/2a89fd510df38cb953bcc124dab29cf93712b20fb0f99c2ad8ce2ea04e4eb05b.jpg)  
Fig. 3. The relationship between $\mathrm{PC}_k[pl_1:ph_1]$ and range sum query $Q(l_{1}:h_{1})$ when $d = 1$ .

$$
\begin{array}{l} (1) l _ {1} \leq p l _ {1} \leq p h _ {1} \leq h _ {1}, (2) l _ {1} \leq p l _ {1} \leq h _ {1} <   p h _ {1}, (3) p l _ {1} \\ <   l _ {1} \leq h _ {1} \leq p h _ {1}, \text { and } (4) p l _ {1} <   l _ {1} \leq p h _ {1} <   h _ {1}. \end{array}
$$

Example 4. For instance in Fig. 2, $\operatorname{Sum}_{4}(4:5, 3:5)$ can be derived as follows:

$$
\begin{array}{l} \mathrm{PC} _ {4} [ 4, 4 ] - \mathrm{PC} _ {4} [ 3, 4 ] - \mathrm{PC} _ {4} [ 4, 2 ] + \mathrm{PC} _ {4} [ 3, 2 ] \\ = 2 6 - 1 9 - 1 0 + 6 = 3. \end{array}
$$

## 3.4. $\Delta$ Cube

The $\Delta$ cube contains only both outlier cells and changed cells of the data cube. Therefore, the $\Delta$ cube is very sparse. It is space-wasteful to store sparse data into a multi-dimensional array since most cells will remain unused. In the scientific computing community, a considerable amount of work has been done to represent sparse matrices in two and three dimensions using a suitable sparse data structure. Higher dimensional sparse data structures have not received much attention in the scientific domain [10]. Recently, we have proposed the ‘ $\Delta$ -tree’ to manage updates efficiently in the dynamic OLAP environment [6]. The basic idea of this approach is that the changes of the data cube are stored into the $\Delta$ -tree and managed separately from the cube. This drastically reduces the update cost at the run time. The construction process of the $\Delta$ -tree is the same as that of the R\*-tree [3].

Whenever the data cube cell is changed, the difference $(\Delta)$ between the new and old values of the data cube cell and its spatial position are stored into the tree. The changed cells that are spatially close are clustered into a corresponding minimum bounding rectangle (MBR). A data node contains the $\Delta$ value and positional index of the changed cell. A directory node consists of the addresses of child nodes, MBRs enclosing its child nodes and $\Sigma\Delta$ values each of which is the sum of all $\Delta$ values of sub-tree nodes. The $\Delta$ cube has the structure similar to that of the $\Delta$ -tree in the context that it manages changed cells efficiently. However, it differs from the $\Delta$ -tree in that initially, it contains outlier cells of the data cube while the $\Delta$ -tree has only a directory node. When searching the $\Delta$ cube, MBRs of the $\Delta$ cube nonoverlapping with the query MBR are pruned efficiently. The interested readers are referred to Ref. [6] for the details.

Example 5. Fig. 3 shows the basic structure of the $\Delta$ cube. As shown in Fig. 4a, initially the $\Delta$ cube contains outlier cells of the data cube, that is, each MBR in the lowest level of the $\Delta$ cube contains these outlier cells. Fig. 4b shows the tree structure of the $\Delta$ cube.

## 3.5. Queries and updates

## 3.5.1. Queries

When a range-sum query $Q$ , which is represented by $(l_1:h_1, l_2:h_2, \ldots, l_d:h_d)$ , is given, we use the PC Pool and $\Delta$ cube for obtaining the answer of $Q$ . Let $\text{Sum}(Q)$ be the function that returns the answer of $Q$ , PC\_Pool\_sum( $Q$ ) be the function that returns the answer which is calculated from PC Pool v, and $\Delta_{\text{sum}}(Q)$ be the function that returns the answer which is found from the $\Delta_{cube}$ . Let $\text{Sum}_{k}(Q)$ be the function that returns the answer which is calculated from the k-th PC in v, which can be obtained ‘on-the fly’ by Lemma 2. During exploring PCs in v in order to obtain PC\_Pool\_sum(Q), in general, a few PCs enveloping a query participate in answering the range-sum query. Let m be the number of these PCs. Then, the answer will be:

![](/api/attachments/FF3R5HVX/fulltext/images/0f5f74e2248ff2d21e02db8869cb4277d7c317fe3e3dcdc5327b906fe733c76c.jpg)

![](/api/attachments/FF3R5HVX/fulltext/images/160403acc1823a4859bb705261322c3ae9d805a46e00a667534e0fcfeec5f8d0.jpg)  
Fig. 4. The basic concepts of the $\Delta$ cube. (a) The $\Delta$ cube, (b) the tree structure of the $\Delta$ cube.

![](/api/attachments/FF3R5HVX/fulltext/images/91871691870a2324a5a9088a8f517687370d436676e47c4d1798a282897f1694.jpg)

![](/api/attachments/FF3R5HVX/fulltext/images/f57a6bcbacc46f9a9270dfdaf98e1abbe12eda98beab3587549c958bc2598171.jpg)  
Fig. 5. An example of a range-sum query using the PC Pool and $\Delta$ cube. (a) PC Pool (b) $\Delta$ cube.

$$
\begin{array}{l} \text { Sum } (Q) = \text { PC\_Pool\_Sum } (Q) + \Delta \_ \text { sum } (Q) \\ = \sum_ {k = 1} ^ {m} \text { Sum } _ {k} (Q) + \Delta \_ \text { sum } (Q) \end{array}
$$

Definition 1 (Disjoint, inclusive, intersecting). Let $MBR_{Q}$ and $MBR_{T}$ be the MBR of a query Q and the MBR of a node T in the $\Delta$ cube, respectively. The relationship between $MBR_{Q}$ and $MBR_{T}$ is formally defined as

(1) Disjoint iff $\mathrm{MBR}_Q\cap \mathrm{MBR}_T = \phi$

(2) Inclusive iff $MBR_{O} \supseteq MBR_{T}$ .

(3) Intersecting iff $MBR_{Q} \cap MBR_{T} \neq \phi$ and not inclusive.

Note that $MBR_{Q} \subset MBR_{T}$ is defined to be intersecting.

When the $\Delta$ cube is traversed to find the result from the function $\Delta$ -sum(), the root node is visited first, and each entry of the root node is evaluated with respect to the spatial relationship between $\mathrm{MBR}_Q$ and $\mathrm{MBR}_T$ , as described in Definition 1. The algorithm of the function $\Delta$ -sum() is shown as follows:

Algorithm $\Delta_{\text{sum}}()$ .

Input: query Q, $\Delta$ cube

## Output: answer

Procedure:

(1) Visit the nodes in the $\Delta$ cube in the depth first order starting from the root node. If there is no more node to be visited, return answer.

(2) Each entry of the node is evaluated. There are three cases of the relationship between MBRQ and MBRT of each entry, as described in Definition 1. Those cases and the corresponding pruning strategies are as follows:

Case 1 (disjoint): the entry related to MBRT is irrelevant to the query Q. Thus, the sub-tree under the entry is pruned.

Case 2 (inclusive): $\Sigma\Delta$ of the entry related to MBRT is added to answer. It is not necessary to traverse the sub-tree under the entry any more since $\Sigma\Delta$ is an exact answer with respect to this entry.

Case 3 (intersecting): in this case, to get a precise answer, we need to evaluate every child MBR, which is included in $MBR_{T}$ . The algorithm $\Delta_{sum}()$ is recursively called with the $\Delta$ cube replaced by the sub-tree under this entry.

Example 6. As shown in Fig. 5, when a range-sum query Q, that is, Sum(4:7, 2:6) is given (dotted box), we can obtain the answer of Q using the PC Pool and $\Delta$ cube. As shown in Fig. 5a, $PC_{4}$ and $PC_{5}$ participate in answering Q. Thus, the answer of Q is as follows:

$$
\begin{array}{r l} \operatorname{Sum} (4: 7, 2: 6) & = \mathrm{PC} _ {4} [ 4, 4 ] - \mathrm{PC} _ {4} [ 3, 4 ] + \mathrm{PC} _ {5} [ 7, 4 ] \\ & + 7 = 2 6 - 1 9 + 2 1 + 7 = 3 5. \end{array}
$$

## 3.5.2. Updates

In a dynamic OLAP environment, the cells of a data cube are frequently changed. Whenever a cell is changed, we compute the update cost UCOST, which is the number of cells to be accessed for updating the PC Pool. If UCOST is less than a given time bound t, we update the corresponding PC in the PC Pool directly. Otherwise, we store a changed cell into the $\Delta$ cube. We use the algorithm same as that of the $\Delta$ -tree to update the $\Delta$ cube. For more details on the update of the $\Delta$ -tree, see Section 3.5 in Ref. [6].

Definition 2 (Update cost). Let $C[x_1, x_2, \ldots, x_d]$ be a cell that has been changed in the data cube $C$ and $\mathrm{PC}_k[pl_1:ph_1, \ldots, pl_d:ph_d]$ be the $k$ -th PC in the PC Pool. The update cost is the number of cells to be accessed for updating $\mathrm{PC}_k$ due to the change of the cell.. Thus, the update cost is defined as

$$
\begin{array}{l} \mathrm{UCOST} _ {k} (C [ x _ {1}, x _ {2}, \dots , x _ {d} ]) \\ = \left\{ \begin{array}{l l} \prod_ {i = 1} ^ {d} (p h _ {i} - x _ {i} + 1), & \text { iff } p l _ {i} \leq x _ {i} \leq p h _ {i}, \\ 0, & \text { Otherwise }. \end{array} \right. \end{array}
$$

Example 7. Let us consider the update process at the cells C[3,3] and C[3,7] as shown in Fig. 2a and t=3. The values of them are changed from 5 and 3 to 9 and 6, respectively. Then, we are able to compute the update costs for PC $_{3}$ and PC $_{4}$ , say, UCOST $_{3}$ (C[3,7]) = 2 and UCOST $_{4}$ (C[3,3]) = 4. As shown in Fig. 6b, the changed cell C[3,3] is stored into the $\Delta$ cube since the update cost of PC $_{4}$ exceeds t. The oblique stroked area in Fig. 6a indicates the cells which have been updated for PC $_{3}$ .

![](/api/attachments/FF3R5HVX/fulltext/images/2b80a71508ff489858b4ee13fb3a70d33c7eccefff0c4785304419ddea7c318c.jpg)

## 4. Finding dense sub-cubes

In this section, we discuss the method that identifies dense sub-cubes in a large sparse data cube based on the density function. Various clustering methods, such as Refs. [1,7,11,14,22], have been studied in database communities. However, finding dense sub-cubes should be handled in a way different from the existing clustering methods in the sense that the shapes of sub-cubes are confined to hyper-rectangles. We present an effective method that finds dense intervals in each dimension and constructs sub-cubes based on the dense intervals. The sparse cube C may have a number of dense regions and thus be represented by sub-cubes SC $[l_{1}:h_{1},\ldots,l_{d}:h_{d}]$ where $l_{i}$ and $h_{i}$ are lower bound and upper bounds, respectively, such that $0\leq l_{i}\leq h_{i}\leq n_{i}-1$ . Then, the problem of finding sub-cubes is formalized as follows:

Given: a d-dimensional data cube C[0:n1-1,...,0:n\_d-1], the minimum number of cells minCells in a sub-cube, and the density thresholds $\delta 1$ , $\delta 2$

Target: to find a set of dense sub-cubes that satisfy the predefined conditions

An input parameter $\delta_{1}$ is needed to determine the dense intervals in each dimension, while $\delta_{2}$ is used to control the merging and shrinking of produced sub-cubes. An input parameter minCells is needed to determine outliers to be stored in the $\Delta$ cube. If a sub-cube has cells less than this value, the populated (nonempty) cells in the sub-cube are regarded as outliers. This value is of course heuristically determined depending on applications. A too small value of minCells makes unimportant sub-cubes be identified, degrading the memory utilization, while a too large value makes meaningful sub-cubes be missed.

![](/api/attachments/FF3R5HVX/fulltext/images/8e140c087b1ad0692817d9ecc434e13c6d37dfcefd18df7f843b2f46c4ee5901.jpg)  
Fig. 6. An example of updates using a given time bound. (a) PC Pool (b) $\Delta$ cube.

## 4.1. Brief sketch of the method

The brief sketch of our method for finding dense sub-cubes from a given data cube is shown in Fig. 7. Populated cells in the data cube are marked in the first step that is a straightforward process. In the second step, dense intervals in each dimension are identified by the projection of marked cells to a 1-dimensional array of each dimension and the computation of the density.

Based on the dense intervals, we build the initial sub-cubes. For each sub-cube built, dense intervals are identified and sub-cubes are built again based on new dense intervals. This process is applied repeatedly until a sub-cube is dense enough. In the third step, candidate sub-cubes produced in the previous step are refined with respect to the given density threshold. The sub-cubes that are closely placed may be merged together in the growing phase, while sparse surfaces of candidate sub-cubes are pruned from the cubes in the shrinking phase. Finally, we get a set of sound sub-cubes.

## 4.2. Marking the populated cells

Each cell of a data cube may contain a measure attribute value. We maintain the data structure to hold the information on whether the specific cell is empty or not. Each cell is represented by a bit, holding ON (nonempty) or OFF (empty). Fig. 8 shows a 2-dimensional $16 \times 16$ data cube C, 33 cells of which are nonempty and thus are marked.

## 4.3. Finding dense intervals in each dimension

We describe briefly an algorithm to find the dense intervals from each dimension, called the neighborhood-flattening based algorithm.

We maintain an 1-dimensional array for each dimension whose size is $n_{i}$ . Each bin holds the cardinality of cells in the cube with respect to the bin. For instance in Fig. 8, the array for the dimension 1 has 16 bins. Each marked cell in the cube is projected to the corresponding bins of each dimension. A bin is dense if it exceeds the density threshold $\delta_{1}$ . In the above example, we get two dense intervals, [1:5] and [8:14] for dimension 1, and similarly, an interval [1:13] for dimension 2, when $\delta_{1}=1$ . The neighborhood-flattening technique is used for smoothing the differences of values among bins of the histogram.

Fig. 9 shows the histogram for a dimension with bins and their cardinalities. Let the i-th bin have the value $v_{i}v_{i}$ is generated by the projection of the corresponding cells to the respective dimension, representing the number of marked cells with respect to the bin. We do not take $v_{i}$ as the representative value of the bin i. Instead, we do consider its neighboring bins as follows. Let f denote the flattening factor. When f=0, no flattening occurs. When f=1, two neighbors (left and right), are involved to compute the representative value $v_{i}^{\prime}=(v_{i-1}+v_{i}+v_{i+1})/3$ . Similarly, when f=2, four neighbors are involved. Thus, we get $v_{i}^{\prime}=(v_{i-2}+v_{i-1}+v_{i}+v_{i+1}+v_{i+2})/5$ . In general, for the histogram H with k bins that covers the interval $[l:h]$ , the $v_{i}^{\prime}$ of the i-th bin is computed as follows:

![](/api/attachments/FF3R5HVX/fulltext/images/8bc6283cee6a8393daebeaf6975bc5279ebe17087bd36f2dc22865071e989337.jpg)  
Fig. 7. The brief sketch for finding dense sub-cubes from a given data cube.

![](/api/attachments/FF3R5HVX/fulltext/images/a0e667872aa70f325a0f617caf082efe4d5105f238b3754caebb91b29c5594c8.jpg)  
Fig. 8. A 2-dimensional $16 \times 16$ data cube C in which 33 cells are marked.

$$
v _ {i} ^ {\prime} = \frac {1}{2 f + 1} \sum_ {t = i - f} ^ {i + f} v _ {t}
$$

The value $v_{i}^{\prime}$ of the first and the last f bins, however, should be treated differently since the number of bins involved to compute $v_{i}^{\prime}$ is less than $2f+1$ . For instance, the $v_{1}^{\prime}$ for the first bin is computed as $v_{1}^{\prime}=(v_{1}+v_{2}+v_{3})/3$ , and the $v_{2}^{\prime}$ for the second bin is computed as $v_{2}^{\prime}=(v_{1}+v_{2}+v_{3}+v_{4})/4$ when f=2. After we get the flattened values for all bins of the histogram, each value is evaluated with respect to the density threshold $\delta_{1}$ , to determine whether the bin is dense or not. A bin, the value of which is greater than $\delta_{1}$ , is regarded as the dense bin. By extracting the dense bins, we are able to identify dense intervals. In our example, the histogram for the dimension 1 is computed as shown in Table 2, when f=0, 1, and 2. When f=1 and $\delta_{1}=1$ , we get the dense intervals, [1:5] and [8:13]. When f=2 and $\delta_{1}=1$ , we get a single dense interval [1:14], and when f=2 and $\delta_{1}=2$ , we get the dense intervals, [1:4] and [9:13].

## 4.4. Building candidate sub-cubes

Once we identify dense intervals in each dimension, we build sub-cubes based on the intervals. When f=1, we get two dense intervals, [1:5] and [8:14] for dimension 1, and one interval [1:13] for dimension 2. Using these intervals, we draw two initial sub-cubes, SC $_{1}$ [1:5, 1:13] and SC $_{2}$ [8:14, 1:13] as shown in Fig. 10a. However, these sub-cubes still include sparse regions. Thus, we apply again the process for finding dense intervals with respect to each dimension of each sub-cube. For a sub-cube SC $_{1}$ [1:5, 1:13], we get one dense interval [1:5] for $D_{1}$ and two dense intervals, [3:3] and [5:10] for $D_{2}$ , producing two sub-cubes, SC $_{11}$ [1:5, 3] and SC $_{12}$ [1:5, 5:10]. Similarly, for a sub-cube C $_{2}$ [8:14, 1:13], we get one dense interval [8:14] for $D_{1}$ and three intervals, [1:4], [6:6], and [9:13] for D $_{2}$ , producing three sub-cubes, SC $_{21}$ [8:14, 1:4], SC $_{22}$ [8:14, 6], and SC $_{23}$ [8:14, 9:13]. By repeating this process for each sub-cube until it is not divisible, we get five candidate sub-cubes finally as shown in Fig. 10b.

![](/api/attachments/FF3R5HVX/fulltext/images/3b08baba1ae9e151f66ac777f93640c57f490d471ffb5a0750efa492e1e2d674.jpg)  
Fig. 9. Neighborhood-flattening technique.

Table 2  
The histogram for the dimension 1 when f=1, 2, and 3

<table><tr><td rowspan="2"> $f$ </td><td colspan="16">Bin</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td></tr><tr><td>0</td><td>0</td><td>1</td><td>3</td><td>4</td><td>3</td><td>2</td><td>0</td><td>0</td><td>2</td><td>3</td><td>4</td><td>5</td><td>4</td><td>1</td><td>1</td><td>0</td></tr><tr><td>1</td><td>0.50</td><td>1.33</td><td>2.67</td><td>3.33</td><td>3.00</td><td>1.67</td><td>0.67</td><td>0.67</td><td>1.67</td><td>3.00</td><td>4.00</td><td>4.33</td><td>3.33</td><td>2.00</td><td>0.67</td><td>0.50</td></tr><tr><td>2</td><td>1.33</td><td>2.00</td><td>2.20</td><td>2.60</td><td>2.40</td><td>1.80</td><td>1.40</td><td>1.40</td><td>1.80</td><td>2.80</td><td>3.60</td><td>3.40</td><td>3.00</td><td>2.20</td><td>1.50</td><td>0.67</td></tr></table>

## 4.5. Refining the sub-cubes

The candidate sub-cubes identified by the iterative process are refined in this step based on the density of a cube. The density of cube C, density(C), is defined as the number of dense cells, numDenseCells(C), divided by the total number of cells, numCells(C). Then, the density of the data cube C in our example is computed as $\text{density}(C)=33/(16\times16)=0.129$ . When k sub-cubes, $SC_{1}$ , $SC_{2}$ , ..., $SC_{k}$ , are identified from the cube C, we are also able to compute the mean density of the sub-cubes as the following:

$$
\text { density } _ {\text { mean }} (\mathrm{SC}) = \frac {\sum_ {i = 1} ^ {k} \text { numDenseCells } (\mathrm{SC} _ {i})}{\sum_ {i = 1} ^ {k} \text { numCells } (\mathrm{SC} _ {i})}
$$

## 4.5.1. Growing phase

Two closely located sub-cubes are merged during the growing phase if the merging satisfies a prespecified condition. We call this phase as a ‘growing’ phase in the context that merging two cubes produces one larger cube. We first define a merging operator between two sub-cubes as follows:

Definition 3 (Merging operator $\oplus$ ). Consider two $d$ -dimensional cubes, $A[l_{1,A}:h_{1,A},\ldots,l_{d,A}:h_{d,A}]$ and $B[l_{1,B}:h_{1,B},\ldots,l_{d,B}:h_{d,B}]$ that are to be merged. Then, the merging operator $\oplus$ is defined as $A\oplus B=C[l_{1,C}:h_{1,C},\ldots,l_{d,C}:h_{d,C}]$ such that $l_{i,C}=\min(l_{i,A},\quad l_{i,B})\}$ and $h_{i,C}=\max(h_{i,A},\quad h_{i,B})$ for $i=1,2,\ldots,d$ . Let cube $B$ be merged to cube $A$ . The number of cells increased by the merging is computed as $\text{numCells}(A\oplus B)-\text{numCells}(A)$ . On the other hand, the number of dense cells increased by merging two cubes is the same as that of cube $B$ , that is, $\text{numDenseCells}(B)$ . Thus, the density of the increased portion, $\text{density}(\Delta_{A,B})$ , of the merged cube is as follows:

$$
\text { density } (\Delta_ {A, B}) = \frac {\text { numDenseCells } (B)}{\text { numCells } (A \oplus B) - \text { numCells } (A)}
$$

In our example, consider that a sub-cube $SC_{111}[2:3,3]$ is merged to a sub-cube $SC_{121}[1:5,5:10]$ . The merging operation of Definition 3, $SC_{111} \oplus SC_{121}$ , produces a merged cube $SC'[1:5,3:10]$ . Thus, the density of the increased portion, density( $\Delta_{A,B}$ ), of the merged cube is 2/10 = 0.20.

Merging two cubes is allowed only when a certain condition is satisfied. When cube B is to be merged to cube A, the merging condition should be satisfied and is defined as the following:

$$
\text { density } (\Delta_ {A, B}) \geq \delta_ {2}
$$

The density threshold $\delta_{2}$ is determined depending on various application requirements, and is given by a user. We, however, give some tips to determine the threshold. First, it can be chosen as the density of cube A when cube B is to be merged to cube A, say,

b

![](/api/attachments/FF3R5HVX/fulltext/images/6b606354dbdcb02e1680ae8197e49c35567e0827dd3389b84c02bdbaded2a9e1.jpg)

![](/api/attachments/FF3R5HVX/fulltext/images/8c567e65ad5c5b9377f2f0e96eaccea6beebe555ba36b7618afeb241106fe1ad.jpg)  
Fig. 10. (a) Two initial sub-cubes, $\mathrm{SC}_1[1:5, 1:13]$ and $\mathrm{SC}_2[8:14, 1:13]$ , generated by dense intervals when $f = 1$ (b) Five candidate sub-cubes, $\mathrm{SC}_{111}[2:3, 3]$ , $\mathrm{SC}_{121}[1:5, 5:10]$ , $\mathrm{SC}_{211}[9:14, 1:4]$ , $\mathrm{SC}_{221}[8, 6]$ , $\mathrm{SC}_{231}[8:12, 9:13]$ , identified finally using the iterative process.

$\delta_{2}=density(A)$ . Another choice can be the mean density of sub-cubes identified by the previous process. In our example, let us consider the situation that a sub-cube $SC_{111}[2:3,3]$ is merged to one of other sub-cubes. The density( $\Delta$ )s are 0.20 for the sub-cube $C_{121}[1:5,5:10]$ , 0.07 for $C_{211}[9:14,1:4]$ , 0.07 for $C_{221}[8,6]$ , and 0.02 for $C_{231}[8:12,9:13]$ , respectively. When we adopt the first case, the merging is not allowed to any sub-cube since density()s for $C_{121}[1:5,5:10]$ , $C_{211}[9:14,1:4]$ , $C_{221}[8,6]$ , and $C_{231}[8:12,9:13]$ are 0.37, 0.38, 1.00, and 0.40, respectively, and all these values do not meet the merging condition. On the other hand, if a user specifies the threshold explicitly, say, 0.15, then the sub-cube $C_{111}[2:3,3]$ is merged to the $C_{121}[1:5,5:10]$ , producing a new larger sub-cube $C_{121}'[1:5,3:10]$ .

## 4.5.2. Shrinking phase

Even though sub-cubes are merged at the growing phase under a prespecified condition, newly produced sub-cubes may contain sparse portions in their surfaces. Thus, we evaluate each surface to prune it if its density is lower than the density threshold. A 2-dimensional cube $C[l_1:h_1, l_2:h_2]$ has four surfaces $(S_1[l_1:h_1, l_2], S_2[l_1:h_1, h_2], S_3[l_1, l_2:h_2]$ , and $S_4[h_1, l_2:h_2]$ ). In general, the $d$ -dimensional cube $C[l_1:$

$h_{1},\ldots,l_{d}:h_{d}]$ has 2d surfaces ( $S_{1}[l_{1}:h_{1}, l_{2}:h_{2},\ldots,l_{d}],\ldots,S_{2d}[h_{1}, l_{2}:h_{2},\ldots,l_{d}:h_{d}]$ ). We call these surfaces as surface slices. We evaluate the surface slices of each candidate cube produced by the merging phase. If the density of a slice is lower than $\delta_{2}$ , the slice is pruned from the cube, resulting in shrinking cubes. For example, let us consider the sub-cube $C_{121}[1:5,3:10]$ that is produced by merging two sub-cubes. It has four surface slices, S[1:5, 3], S[1:5, 10], S[1, 3:10], and S[5, 3:10]. The densities of these slices are 0.4, 0.4, 0.125, and 0.25, respectively. If we adopt density(C) (=0.129) as the density threshold, then the surface slice S[1, 3:10] is pruned, producing the shrunken sub-cube $C_{121}'[2:5,3:10]$ .

We take the minimum number of cells in a cube, minCells, as an input parameter to eliminate the sub-cubes that have less cells than this value. All marked cells in these sub-cubes are regarded as outliers and stored in the $\Delta$ cube.

## 5. Experiments

In order to evaluate the effectiveness and efficiency of our proposed method, we have conducted extensive experiments on diverse data sets that are generated synthetically with various dimensionalities. Our experiment focuses on showing the effectiveness and the efficiency, in terms of the space to store the sparse data cube and the execution time to respond users' range queries. The experiment was conducted using Pentium 4 1.7 GHz processor with 512 M memory and 80 G hard disk. In this section, we describe our preparation for the experiment and give the results with analyses.

<table><tr><td>d</td><td>s</td><td>z</td></tr><tr><td>2</td><td>1000 × 1000</td><td>4000</td></tr><tr><td>3</td><td>250 × 100 × 50</td><td>10,000</td></tr><tr><td>4</td><td>150 × 60 × 50 × 30</td><td>30,000</td></tr><tr><td>5</td><td>100 × 50 × 40 × 30 × 20</td><td>90,000</td></tr></table>

## 5.1. Experimental preparation

For the experiment, we have generated synthetically some sparse data cubes that have several dense regions in them. The area outside dense regions is sparse. From each data cube, we extracted dense sub-cubes using the method for finding sub-cubes shown in Section 4. The parameters to generate data cubes are the dimensionality d, the size of a data cube s, and the total number of nonempty cells z. Table 3 shows parameters that are used to generate data cubes. The experiment was conducted for four dimensions $(d=2,3,4,5)$ for convenience, but our method does not restrict the dimensionality of data sets. For each dimension, we generated 10 data cubes, resulting in 40 data cubes.

![](/api/attachments/FF3R5HVX/fulltext/images/aecfab43a8d4cbefdfc5f9797f7fa68f257f8a427c0f454d34809216b11ad4cc.jpg)  
Fig. 11. The cubing quality with respect to dimensionality.

![](/api/attachments/FF3R5HVX/fulltext/images/051c6957bca03812cb9a58e02be529fa8a6d966b72b8f0cc5c2ec2f5fc32cb79.jpg)  
Fig. 12. Comparison of storage requirements for the PC and the PC pool.

We have discussed various parameters to produce sub-cubes from a data cube in Section 4. We have used 2 as the neighborhood-flattening factor $(f)$ , resulting in four neighbor bins to be involved for computing the density of the bin. To find dense intervals at each dimension during generating sub-cubes, we have used the average value of histogram bins at each dimension for the density threshold $\delta_{1}$ . For the density threshold $\delta_{2}$ that is used to control the merging and shrinking of sub-cubes, the density of the data cube was used. We have adopted 16 for minCells, the number of minimum cells per sub-cube. All populated cells in the sub-cube that has cells less than 16 are treated as outliers and stored in the $\Delta$ cube.

For the evaluation of the query performance, we have used various queries with different sizes. The edge lengths of query rectangles are selected as 50%, 40%, 30%, 20%, and 10% of the corresponding dimension length of the data cube. We have generated 10 range queries for each size and for each data cube. Thus, 500 queries were used for each dimension, and we averaged results from them to report the performance.

![](/api/attachments/FF3R5HVX/fulltext/images/7b902eaf15f2d7cbc34f838ea210a676e56347705c1b4948440d10a2e19e6e36.jpg)  
Fig. 13. Ratio of storage for the PC Pool to that for the PC.

![](/api/attachments/FF3R5HVX/fulltext/images/a517abf5d14349d987bf8a9c64441ae29f66bf3c9c50f7338b916c9f84cbf701.jpg)  
Fig. 14. Space requirement ratio for the number of sub-PCs when dimension = 2.

## 5.2. Experimental results

## 5.2.1. Finding sub-cubes

To evaluate the effectiveness of finding sub-cubes from data cubes, we define the cubing quality (CQ) based on the density as follows:

$$
\mathrm{CQ} = \frac {N _ {\mathrm{SC}}}{N _ {C}}
$$

where $N_{C}$ is the number of dense cells in the data cube and $N_{SC}$ is the number of dense cells in the sub-cubes found by our algorithm. Fig. 11 shows that the cubing quality for each dimension is from 86% to 95%, saying that the majority of dense cells in the data cube are included in the sub-cubes identified. The dense cells outside sub-cubes are regarded as outliers and stored to $\Delta$ cube. On the other hand, the cubing quality decreases as the dimensionality increases. It is because the data cubes become sparser as the dimensionality becomes higher as shown in Table 3.

![](/api/attachments/FF3R5HVX/fulltext/images/966b90b4b6398c25b267e2b06f152633e6079b33a74faa3a35da55d942a3e5bf.jpg)  
Fig. 15. Space requirement ratio for the number of sub-PCs when dimension = 3.

![](/api/attachments/FF3R5HVX/fulltext/images/a0d3c75b212a421ed87d299960c309f08ca01330bc0a24a9bb4667d3704e8187.jpg)  
Fig. 16. Space requirement ratio for the number of sub-PCs when dimension = 4.

## 5.2.2. Storage reduction ratio

The primary advantage of the proposed method is that it greatly reduces the storage to store the cubes. The total volume of sub-cubes produced by our method is generally much smaller than that of the PC, causing a remarkable storage reduction. The produced sub-cubes are stored in the PC pool. Fig. 12 shows that the storage requirement for the PC increases rapidly as the dimensionality increases, while the size of PC pool shows slow moving. Fig. 13 shows the ratio of the storage for the PC Pool to that for the PC. We are able to observe that the ratio decreases as the dimensionality increases. It means that the efficiency of storage saving is getting better in higher dimensions.

![](/api/attachments/FF3R5HVX/fulltext/images/dcc52a8d83473488c4bb11120e9299781c1b59bafe6525b75086baa0a7f20a87.jpg)  
Fig. 17. Space requirement ratio for the number of sub-PCs when dimension = 5.

![](/api/attachments/FF3R5HVX/fulltext/images/0d2e671f86ca315e44eb635c8323c54609fdd6a3b82efd3fe78582b1fd01d219.jpg)  
Fig. 18. The number of page I/Os when dimension=2, the X coordinates is the ratio of edge lengths of query rectangles to the edge length of data cube.

## 5.2.3. Effects on the number of sub-cubes

Figs. 14–17 show the ratio of the storage with respect to the number of sub-cubes, for dimension 2, 3, 4, and 5, respectively. We can observe that there is some tendency that the space requirement decreases as the number of sub-cubes identified increases, and the degree of decrease becomes larger as the dimensionality is getting higher.

## 5.2.4. Query performance

The query performance is measured by the number of page I/Os to access the PC Pool and the $\Delta$ cube for answering the query. We assume that the storage space to hold the PC and PC Pool is very large. The PC and PC Pool are stored in disks and thus accessing them may require disk page I/Os. However, the query computation for the PC and PC Pool can be answered within a constant number of page I/Os by Lemmas 1 and 2. We have executed 10 queries for each query size, each dimension, and each data cube. And we have taken the average of the query results. We have added the page accesses by the $\Delta$ cube to the page I/O by the PC Pool. Figs. 18–21 show that the page I/O decreases as the size of a query decreases when the PC Pool is used. The result shows that the PC Pool drastically reduces the space requirements, while the performance with it is comparable to that with the PC.

![](/api/attachments/FF3R5HVX/fulltext/images/68c2db54b293d442efc852e3aac680e64582adffa403f4f8836cbd33e5da47c4.jpg)  
Fig. 19. The number of page I/Os when dimension = 3.

![](/api/attachments/FF3R5HVX/fulltext/images/e5fc51383ba88943ba6965faf387efc9c459dad81cfe9e3124a90b5e5a45a873.jpg)  
Fig. 20. The number of page I/Os when dimension = 4.

## 5.2.5. Analysis

We will give detailed query performance analyses of our proposed approach. We consider a 2-dimensional PC Pool as shown in Fig. 22. There may be several sub-cubes overlapping with the query MBR when processing a range-sum query using the PC Pool approach. We can classify these sub-cubes as subcube (1)-sub-cube (10). Fig. 22 shows geometrical relationships between the range-sum query and subcubes in the PC Pool. The dotted box denotes the region of the range-sum query. In Fig. 22, the range-sum in sub-cube (1) can be computed in four page I/Os. In the cases of sub-cubes (2), (3), (4), and (7), the range-sum in each sub-cube can be computed in two page I/Os, respectively. Similarly, in the cases of sub-cubes (5), (6), (8), and (9), the range-sum in each sub-cube can be computed in only one page I/O for each case. On the other hand, sub-cube (10) is a special case. That is, a range-sum can be simply answered by a single sub-cube as in the case of the PC. In that case, the range-sum can be computed by at most four page I/Os. The number of sub-cubes overlapping with the query increases as the query size increases. However, since the number of sub-cubes like sub-cube (5) increases as the query size increases, the total number of page I/Os does not increase severely. This is because sub-cube (5) requires only one page I/O. The number of sub-cubes overlapping with the query also decreases as the query size decreases. In special cases, the PC Pool approach may not require any page I/O, since there may be no sub-cube overlapping with the query when the query size is small. However, the PC approach requires at least one page I/O. In general, the query performance of the PC Pool approach is affected by the types of sub-cubes (e.g., sub-cube (1)–(10)) and the number of sub-cubes overlapping with the query.

![](/api/attachments/FF3R5HVX/fulltext/images/60f20bd133a191e7fa4ef6af00583f1041550c1d9f9fdc306b5230d45d6345d6.jpg)  
Fig. 21. The number of page I/Os when dimension = 5.

![](/api/attachments/FF3R5HVX/fulltext/images/87ee5829718da55def7af2fcbfb2290debaae963afe6e6d705e034c344bbbfb6.jpg)  
PC Pool  
Fig. 22. Geometrical relationships between the query and sub-cubes for a 2-dimensional case.

The average number of sub-cubes overlapping with the query is very small for a sparse data cube in high dimensions. Therefore, the type of sub-cubes affects deeply the query performance of the PC Pool approach. For instance, we assume that the number of sub-cubes overlapping with the query is two and the page I/O by the $\Delta$ cube is zero. If the type of two sub-cubes is (1), the PC approach outperforms the PC Pool approach. If the types of two sub-cubes, however, are (5), (6), (8) or (9), the PC Pool approach outperforms the PC approach. Similarly, if the types of two sub-cubes are (2), (3), (4) or (7), both approaches have the same query performance, that is, four page I/Os. Therefore, in many cases, the PC Pool approach outperforms the PC approach since the average number of overlapping sub-cubes decreases as the dimension increases.

Table 4 depicts detailed query processing time of the PC Pool approach. We built 10 PC Pools for each dimension $(d=2,3,4,5)$ and averaged the number of sub-cubes in each PC Pool. We selected the query size as 0.1, 0.3, 0.3, and 0.4 for 2, 3, 4 and 5 dimensions, respectively. We also conducted 100 queries for each query size and each dimension and obtained the best case, average case, and worst case query times. The query time includes page I/Os by both the PC Pool and the $\Delta$ cube. For example, Table 4 shows that the worst case query time is 18 when the dimensions is 3. That is, there are 14 page I/Os by the PC Pool and 4 page I/Os by the $\Delta$ cube.

## 6. Conclusion

In this paper, we considered the problem of the space overhead in the existing OLAP methods based on the prefix sum approach. In a real OLAP environment, analysts may want to explore the relationship among diverse attributes to find business trends and opportunities. A data cube for such analyses generally has a high dimensionality. However, a high dimensionality causes the data cube to be very sparse. This is the motivation that we proposed a new technique called ‘the PC Pool’, which drastically reduces the space of the PC using clustering techniques in a large data warehouse. The main idea is to find a set of dense sub-cubes that satisfy predefined density conditions and to build multiple small PCs, instead of building one huge PC. This drastically reduces the space requirement for the PC of a large sparse data cube. Experiments demonstrate the effect of the storage reduction for various sizes of data cubes.

Table 4  
Detailed query processing time of the PC Pool approach

<table><tr><td>d</td><td>Number of sub-cubes (average)</td><td>The size of Δcube (approximate)</td><td>Query size</td><td>Best case query time (number of page I/Os)</td><td>Average case query time (number of page I/Os)</td><td>Worst case query time (number of page I/Os)</td><td>Number of sub-cubes overlapping with the query (average)</td></tr><tr><td>2</td><td>22.8</td><td>200</td><td>0.1</td><td>3</td><td>4.48</td><td>11</td><td>0.78</td></tr><tr><td>3</td><td>18.1</td><td>700</td><td>0.3</td><td>4</td><td>8.12</td><td>18</td><td>1.51</td></tr><tr><td>4</td><td>16.9</td><td>2700</td><td>0.3</td><td>8</td><td>13.54</td><td>42</td><td>1.32</td></tr><tr><td>5</td><td>27.3</td><td>11,700</td><td>0.4</td><td>16</td><td>25.69</td><td>78</td><td>2.19</td></tr></table>

We also developed an effective algorithm that finds dense intervals in each dimension of a data cube, called the neighborhood-flattening based algorithm and proposed a method to find dense sub-cubes based on the algorithm. We performed an extensive experiment with diverse data sets, and examined the space reduction and performance of our proposed method with respect to diverse dimensions of the data cube and query sizes. Experimental results show that our method reduces almost 82–93% of the space of the PC while having a reasonable query performance.

As future work, we plan to develop more efficient clustering algorithms for high-dimensional data cubes, and to further extend the idea of our work and apply it to a new cube problem such as ‘iceberg cube’, which is a subset of a cube containing only those cells whose measure satisfies certain constraints, such as minimal support threshold.

## Appendix A. The proof of Lemma 2

## Lemma 2

For all $j\in D$ , and

$$
s (j) = \left\{ \begin{array}{l l} 1, & \text { if } x _ {j} = h _ {j} \text { or } x _ {j} = p h _ {j}, \\ - 1, & \text { if } x _ {j} = l _ {j} - 1, \end{array} \right.
$$

Then, for all $j \in D$ ,

$$
X _ {j} = \left\{ \begin{array}{c l} \{p h _ {j} \}, & \text {if} l _ {j} \leq p l _ {j} \leq p h _ {j} \leq h _ {j}, \\ \{h _ {j} \}, & \text {if} l _ {j} \leq p l _ {j} \leq h _ {j} <   p h _ {j}, \\ \{l _ {j} - 1, h _ {j} \}, & \text {if} p l _ {j} <   l _ {j} \leq h _ {j} \leq p h _ {j}, \\ \{l _ {j} - 1, p h _ {j} \}, & \text {if} p l _ {j} <   l _ {j} \leq p h _ {j} <   h _ {j} \end{array} \right.
$$

and

$$
\begin{array}{l} \operatorname{Sum} _ {k} (l _ {1}: h _ {1}, l _ {2}: h _ {2}, \dots , l _ {d}: h _ {d}) \\ = \sum_ {\forall_ {x _ {j}} \in X _ {j}} \left\{\left(\prod_ {j = 1} ^ {d} s (j)\right) \mathrm{PC} _ {k} [ x _ {1}, x _ {2}, \dots , x _ {d} ] \right\}. \end{array}
$$

Proof. We assume that $d, n_{j}, j \in D$ , and $C$ are all given as an input. Also, assume $\mathrm{PC}_{k}[x_{1}, x_{2}, \ldots, x_{d}]$ s as defined in Eq. (3) have been precomputed for all $pl_{j} \leq x_{j} \leq ph_{j}$ , and $j \in D$ . We will prove the lemma by proving the following equation instead, for all $t \in D$ by induction:

$$
\begin{array}{l} \text {Sum} _ {k} (l _ {1}: h _ {1}, l _ {2}: h _ {2}, \ldots , l _ {t}: h _ {t}, 0: x _ {t + 1}, \ldots , 0: x _ {d}) \\ = \sum_ {\forall_ {x _ {j}} \in X _ {j}, 1 \leq j \leq t} \left\{\left(\prod_ {j = 1} ^ {t} s (j)\right) \text {PC} _ {k} [ x _ {1}, x _ {2}, \ldots , x _ {d} ] \right\}. \end{array}\tag{5}
$$

□

For the basis t=1, it can be shown from the definition of $PC_{k}$ . Assume, for the sake of induction hypothesis that Eq. (5) holds for t=m for some m where $1 \leq m < d$ .

That is, we have

$$
\begin{array}{l} \operatorname{Sum} _ {k} (l _ {1}: h _ {1}, l _ {2}: h _ {2}, \ldots , l _ {m}: h _ {m}, 0: x _ {m + 1}, \ldots , 0: x _ {d}) \\ = \sum_ {\forall_ {x _ {j}} \in X _ {j}, 1 \leq j \leq m} \left\{\left(\prod_ {j = 1} ^ {m} s (j)\right) \mathrm{PC} _ {k} [ x _ {1}, x _ {2}, \ldots , x _ {d} ] \right\}. \end{array}\tag{6}
$$

We wish to show that Eq. (5) still holds for $t = m + 1$ .

By letting $x_{m + 1} = l_{m + 1}$ in Eq. (6), we have

$$
\begin{array}{l} \operatorname{Sum} _ {k} (l _ {1}: h _ {1}, \dots , l _ {m}: h _ {m}, 0: l _ {m + 1}, 0: x _ {m + 2}, \dots , 0: x _ {d}) \\ = \left\{ \begin{array}{l l} 0, & \text { if } l _ {m + 1} \leq p l _ {m + 1} \leq p h _ {m + 1} \leq h _ {m + 1}, \\ 0, & \text { if } l _ {m + 1} \leq p l _ {m + 1} \leq h _ {m + 1} \leq p h _ {m + 1}, \\ \sum_ {\forall_ {x _ {j}} \in X _ {j}, 1 \leq j \leq m} \left\{\left(\prod_ {j = 1} ^ {m} s (j)\right) \mathrm{PC} _ {k} [ x _ {1}, \dots , x _ {m}, l _ {m + 1}, x _ {m + 2}, \dots , x _ {d} ] \right\}, & \text { if } p l _ {m + 1} <   l _ {m + 1} \leq h _ {m + 1} \leq p h _ {m + 1}, \\ \sum_ {\forall_ {x _ {j}} \in X _ {j}, 1 \leq j \leq m} \left\{\left(\prod_ {j = 1} ^ {m} s (j)\right) \mathrm{PC} _ {k} [ x _ {i}, \dots , x _ {m}, l _ {m + 1}, x _ {m + 2}, \dots , x _ {d} ] \right\}, & \text { if } p l _ {m + 1} <   l _ {m + 1} \leq p h _ {m + 1} \leq h _ {m + 1}. \end{array} \right. \end{array}\tag{7}
$$

Similarly, by letting $x_{m+1}=h_{m+1}$ in Eq. (6), we have

$$
\begin{array}{l} \text {Sum} _ {k} (l _ {1}: h _ {1}, \ldots , l _ {m}: h _ {m}, 0: h _ {m + 1}, 0: x _ {m + 2}, \ldots , 0: x _ {d}) \\ = \left\{ \begin{array}{l l} \sum_ {\forall_ {x _ {j}} \in X _ {j}, 1 \leq j \leq m} \Bigg \{\bigg (\prod_ {j = 1} ^ {m} s (j) \bigg) \mathrm{PC} _ {k} [ x _ {1}, \ldots , x _ {m}, p h _ {m + 1}, x _ {m + 2}, \ldots , x _ {d} ] \Bigg \}, & \text {if} l _ {m + 1} \leq p l _ {m + 1} \leq p h _ {m + 1} \leq h _ {m + 1}, \\ \sum_ {\forall_ {x _ {j}} \in X _ {j}, 1 \leq j \leq m} \Bigg \{\bigg (\prod_ {j = 1} ^ {m} s (j) \bigg) \mathrm{PC} _ {k} [ x _ {1}, \ldots , x _ {m}, h _ {m + 1}, x _ {m + 2}, \ldots , x _ {d} ] \Bigg \}, & \text {if} l _ {m + 1} \leq p l _ {m + 1} \leq h _ {m + 1} <   p h _ {m + 1}, \\ \sum_ {\forall_ {x _ {j}} \in X _ {j}, 1 \leq j \leq m} \Bigg \{\bigg (\prod_ {j = 1} ^ {m} s (j) \bigg) \mathrm{PC} _ {k} [ x _ {1}, \ldots , x _ {m}, h _ {m + 1}, y _ {m + 2}, \ldots , y _ {d} ] \Bigg \}, & \text {if} p l _ {m + 1} <   l _ {m + 1} \leq h _ {m + 1} \leq p h _ {m + 1}, \\ \sum_ {\forall_ {x _ {j}} \in X _ {j}, 1 \leq j \leq m} \Bigg \{\bigg (\prod_ {j = 1} ^ {m} s (j) \bigg) \mathrm{PC} _ {k} [ x _ {1}, \ldots , x _ {m}, p h _ {m + 1}, x _ {m + 2}, y _ {m + 2}, y _ {d} ] \Bigg \}, & \text {if} p l _ {m + 1} <   l _ {m + 1} \leq p h _ {m + 1} <   h _ {m + 1}, \end{array} \right. \end{array}\tag{8}
$$

For convenience, denote the terms in Eqs. (7) and (8) by $T_{1}$ and $T_{2}$ , respectively. Notice that

$$
\begin{array}{l} \operatorname{Sum} _ {k} (l _ {1}: h _ {1}, \dots , l _ {m}: h _ {m}, l _ {m + 1}: h _ {m + 1}, 0: x _ {m + 2}, \dots , 0: x _ {d}) = T _ {2} - T _ {1} \\ = \left\{ \begin{array}{l l} \operatorname{Sum} _ {k} (l _ {1}: h _ {1}, \dots , l _ {m}: h _ {m}, p l _ {m + 1}: p h _ {m + 1}, 0: x _ {m + 2}, \dots , 0: x _ {d}), & \text { if } l _ {m + 1} \leq p l _ {m + 1} \leq p h _ {m + 1} \leq h _ {m + 1}, \\ \operatorname{Sum} _ {k} (l _ {1}: h _ {1}, \dots , l _ {m}: h _ {m}, p l _ {m + 1}: h _ {m + 1}, 0: x _ {m + 2}, \dots , 0: x _ {d}), & \text { if } l _ {m + 1} \leq p l _ {m + 1} \leq h _ {m + 1} <   p h _ {m + 1}, \\ \operatorname{Sum} _ {k} (l _ {1}: h _ {1}, \dots , l _ {m}: h _ {m}, l _ {m + 1}: h _ {m + 1}, 0: x _ {m + 2}, \dots , 0: x _ {d}), & \text { if } p l _ {m + 1} <   l _ {m + 1} \leq h _ {m + 1} \leq p h _ {m + 1}, \\ \operatorname{Sum} _ {k} (l _ {1}: h _ {1}, \dots , l _ {m}: h _ {m}, l _ {m + 1}: p h _ {m + 1}, 0: x _ {m + 2}, \dots , 0: x _ {d}), & \text { if } p l _ {m + 1} <   l _ {m + 1} \leq p h _ {m + 1} <   h _ {m + 1}. \end{array} \right. \\ = \sum_ {\forall_ {x _ {j}} \in X _ {j}, 1 \leq j \leq m + 1} \left\{\left(\prod_ {j = 1} ^ {m + 1} s (j)\right) \mathrm{PC} _ {k} [ x _ {1}, x _ {2}, \dots , x _ {d} ] \right\}. \end{array}\tag{9}
$$

That is, we have shown that Eq. (5) holds for $t=m+1$ . This completes the proof of the lemma.

## References

[1] R. Agrawal, J. Gehrke, D. Gunopulos, P. Raghavan, Automatic subspace clustering of high dimensional data for data mining applications, Proceedings of ACM SIGMOD Int'l Conference on Management of Data, Washington, ACM Press, 1998, pp. 94–105.

[2] D. Barbara, M. Sullivan, A space-efficient way support approximate multidimensional databases, George Mason University Technical Report ISSE-TR-98-03, 1998.

[3] N. Beckmann, H. Kriegel, R. Schneider, B. Seeger, The R\*-tree: an efficient and robust access method for points and rectangles, Proceedings of ACM SIGMOD Int'l Conference on Management of Data, New Jersey, ACM Press, 1990, pp. 322–331.

[4] C.-Y. Chan, Y.E. Ioannidis, Hierarchical cubes for range-sum queries, Proceedings of Int'l Conference on Very Large Data Bases, Scotland, Morgan Kaufmann, 1999, pp. 675–686.

[5] D.W. Cheung, B. Zhou, B. Kao, H. Kan, S.D. Lee, Towards the building of a dense-region based OLAP system, in: Data and Knowledge Engineering, vol. 36, Elsevier Science, 2001 (January), pp. 1–27.

[6] S.-J. Chun, C.-W. Chung, J.-H. Lee, S.-L. Lee, Dynamic update cube for range-sum queries, Proceedings of Int'l Conference on Very Large Data Bases Conference, Italy, Morgan Kaufmann, 2001, pp. 521–530.

[7] M. Ester, H.P. Kriegel, J. Sander, X. Xu, A density-based algorithm for discovering clusters in large spatial databases with noise, Int'l Conference on Knowledge Discovery in Databases and Data Mining, Oregon, AAAI Press, 1996, pp. 226–231.

[8] S. Geffner, D. Agrawal, A. El Abbadi, T. Smith, Relative prefix sums: an efficient approach for querying dynamic OLAP data cubes, Proceedings of Int'l Conference on Data Engineering, Australia, IEEE Computer Society Press, 1999, pp. 328–335.

[9] S. Geffner, D. Agrawal, A. El Abbadi, The dynamic data cube, Proceedings of Int'l Conference on Extending Database Technology, Germany, Springer, 2000, pp. 237–253.

[10] S. Goil, A. Choudhary, BESS: Sparse data storage of multidimensional data for OLAP and data mining, Technical report, Northwestern University, 1997.

[11] S. Guha, R. Rastogi, K. Shim, CURE: an efficient clustering algorithm for large databases, Proceedings of ACM SIGMOD Int'l Conference on Management of Data, Washington, ACM Press, 1998, pp. 73–84.

[12] C. Ho, R. Agrawal, N. Megido, R. Srikant, Range queries in OLAP data cubes, Proceedings of ACM SIGMOD Int'l Conference on Management of Data, Arizona, ACM Press, 1997, pp. 73–88.

[13] W. Liang, H. Wang, M.E. Orlowska, Range queries in dynamic OLAP data cubes, Data and Knowledge Engineering 34 (2000) 21–38.

[14] R.T. Ng, J. Han, Efficient and effective clustering methods for spatial data mining, Proceedings of Int'l Conference on Very Large Data Bases, Chile, Morgan Kaufmann, 1994, pp. 144–155.

[15] M. Riedewald, D. Agrawal, A.E. Abbadi, pCube: update-efficient online aggregation with progressive feedback and error bounds, SSDBM Conference, Berlin, IEEE Computer Society, 2000, pp. 95–108.

[16] M. Riedewald, D. Agrawal, A.E. Abbadi, R. Pajarola, Space-efficient data cubes for dynamic environments, DaWaK Conference, London, Springer, 2000, pp. 24–33.

[17] J. Shanmugasundaram, U. Fayyad, P. Bradley, Compressed data cubes for OLAP aggregate query approximation on continuous dimensions, KDD conference, San Diego, ACM 1999, pp. 223–232.

[18] U.S. Census Bureau, Census bureau databases, The online data are available on the web at http://www.census.gov/.

[19] J.S. Vitter, M. Wang, Approximate computation of multidimensional aggregates of sparse data using wavelets, SIGMOD Conference, Pennsylvania, ACM Press, 1999, pp. 193–204.

[20] J.S. Vitter, M. Wang, B.R. Iyer, Data cube approximation and histograms via wavelets, CIKM Conference, Maryland, ACM, 1998, pp. 96–104.

[21] S. Youness, Professional Data Warehousing with SQL Server 7.0 and OLAP Services, Wrox Press, 2000.

[22] T. Zhang, R. Ramakrishnan, M. Livny, BIRCH: an efficient data clustering method for very large databases, Proceedings of ACM SIGMOD Int'l Conference on Management of Data, Canada, ACM Press, 1996, pp. 103–114.

Seok-Ju Chun received the BS and MS degrees in electronic engineering from Kyungpook National University in 1987 and 1989, respectively, and the PhD degree in information and communication engineering from KAIST in 2002. From 1989 to 1995, he worked as a System Engineer in Research and Development Center at Hyundai Heavy Industries, Korea. His current research interests include OLAP, data warehouses, multimedia databases, and data mining.

Chin-Wan Chung received the PhD degree from the University of Michigan, Ann Arbor in 1983. He was a Senior Research Scientist and a Staff Research Scientist in the Computer Science Department at the General Motors Research Laboratories (GMR). While at GMR, he developed DATAPLEX, a heterogeneous distributed database management system integrating relational databases and hierarchical databases. Since 1993, he has been a Professor in the Division of Computer Science at the Korea Advanced Institute of Science and Technology (KAIST), South Korea. At KAIST, he developed a full-scale object-oriented spatial database management system called OMEGA, which supports ODMG standards. His current research interests include XML, OLAP, multimedia databases, spatiotemporal databases, and the semantic web.

Seok-Lyong Lee received the BS degree in mechanical engineering in 1984 and MS degree in computer science in 1993 from Yonsei University, and PhD degree in information and communication engineering from KAIST in 2001. He was an Advisory S/W Engineer in S/W Development Institute at IBM Korea from 1984 to 1995. He is currently an assistant professor in School of Industrial and Information System Engineering at Hankuk University of Foreign Studies. His major research interests include multimedia databases, data mining and warehousing, and Web information retrieval.
