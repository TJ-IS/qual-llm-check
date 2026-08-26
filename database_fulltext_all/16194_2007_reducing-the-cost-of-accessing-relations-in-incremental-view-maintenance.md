---
otero_id: 16194
otero_key: "VV4YJ8XU"
title: "Reducing the cost of accessing relations in incremental view maintenance"
authors: "Ki Yong Lee; Jin Hyun Son; Myoung Ho Kim"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.11.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 43 (2007) 512– 526

www.elsevier.com/locate/dss

# Reducing the cost of accessing relations in incremental view maintenance

Ki Yong Lee <sup>a,⁎</sup>, Jin Hyun Son <sup>b</sup>, Myoung Ho Kim <sup>a</sup>

<sup>a</sup> Department of Electrical Engineering and Computer Science, KAIST, 373-1 Guseong-dong, Yuseong-gu, Daejeon, 305-701, South Korea <sup>b</sup> Department of Computer Science and Engineering, Hanyang University, 1271 Sa-1 dong, Ansan, Kyunggi-Do, 425-791, South Korea

Received 23 August 2005; received in revised form 6 November 2006; accepted 12 November 2006 Available online 11 January 2007

## Abstract

In the data warehouse environment, the concept of a materialized view is common and important for efficient support of OLAP query processing. Materialized views are generally derived from several relations. These materialized views need to be updated when source relations change. Since the propagation of updates to the views may impose a significant overhead, it is essential to update the warehouse views efficiently. Though various view maintenance strategies have been discussed in the past, optimizations on the total accesses to relations have not been sufficiently investigated.

In this paper we propose an efficient incremental view maintenance method called optimal delta evaluation that can minimize the total accesses to relations. We first present the delta evaluation expression and a delta evaluation tree which are core concepts of the method. Then, a dynamic programming algorithm that can find the optimal delta evaluation tree is proposed. We also present various experimental results that show the usefulness and efficiency of our proposed method. © 2006 Elsevier B.V. All rights reserved.

Keywords: Materialized view; View maintenance; Incremental maintenance

## 1. Introduction

The concept of a data warehouses has been used to provide analysts and managers with strategic information about the key figures of the underlying business. Data warehouses periodically extract and store the data needed for analytical purposes from remote information sources. Most queries on data warehouses are related to statistics involving aggregates rather than specific data content. They need to be processed in highly efficient manner to facilitate on-line analytical processing (OLAP). These kinds of queries generally include joins of many relations, which incur considerable query processing costs. In this regard, materialized views in a data warehouse should be effective in speeding up the OLAP queries, and are increasingly supported by many commercial systems.

The main objective of a materialized view is to improve query performance. When base relations in a data warehouse are updated due to the changes of remote information sources, the materialized views defined by the base relations must also be updated. Since the amount of data reflected to data warehouses and queries calling for up-to-date information have been increasing, an efficient view maintenance strategy has been an important issue in data warehouse applications.

We can reflect changes in base relations to materialized views by either recomputation or incremental maintenance. Here, incrementally maintaining a materialized view denotes the propagation of only its changes. Since the amounts of changes are much smaller than the sizes of base relations and views in general, computing only the changes of a view is usually much cheaper than recomputing from scratch. Thus, many possible methods that allow incremental view maintenance have been proposed in the past [5,3,8,19,15,7].

## 1.1. Related work

Various kinds of materialized views can be formed over base relations, e.g., select views, project views, select-project-join (SPJ) views, aggregation views, and so on. [5,3,6] proposed formal expressions through which we can incrementally maintain SPJ views. The incremental view maintenance expressions that can additionally support aggregation views were proposed in Refs. [8,19,15,7]. However, they did not mention how to select an efficient maintenance expression from many possible expressions that can be applied to a view. Recently, the incremental maintenance of views with more complex operators, such as non-distributive aggregate functions [17], top-k queries [25], pivots and unpivots [1], was proposed.

In this paper, we will focus on SPJ materialized views that have been one of the most widely used materialized views in data warehouse applications. There have been a few methods for incremental maintenance of an SPJ view. For an n-way join view $V = R _ { 1 } \bowtie R _ { 2 } \bowtie \ldots \bowtie R _ { n } ,$ [5] proposed the following maintenance expression to compute the change of $V ,$ which is denoted by $\Delta V .$

$$
\begin{array}{c} \Delta V = (\Delta R _ {1} \bowtie R _ {2} \bowtie \dots \bowtie R _ {n}) \cup (R _ {1} \bowtie \Delta R _ {2} \bowtie \dots \bowtie R _ {n}) \\ \cup \dots (\Delta R _ {1} \bowtie \Delta R _ {2} \bowtie \dots \bowtie \Delta R _ {n}). \end{array}\tag{1}
$$

Here, $\Delta R _ { \mathrm { i } }$ denotes the change of base relation $R _ { \mathrm { i \cdot } }$ . To update view $V ,$ it is sufficient to compute $\Delta V$ and propagate it to V. The relation that denotes the change of some relation such as $\Delta R _ { \mathrm { i } }$ is called a delta relation. Let each join expression, i.e., a subexpression consisting of only joins, be called a join term, or simply a term. Then, expression (1) consists of $( 2 ^ { n } - 1 )$ terms $( \mathrm { i } . \mathrm { e } . , \ \Delta R _ { 1 }$ ⋈ $R _ { 2 }$ ⋈…⋈ $R _ { n } , R _ { 1 }$ ⋈ΔR ⋈…⋈ $R _ { n } , . . . , \Delta R _ { 1 }$ ⋈ $\Delta R _ { 2 }$ ⋈ $\ldots \boxtimes \Delta R _ { n } )$ . For example, $\Delta V _ { }$ of a 3-way join view $V =$

$R _ { 1 }$ ⋈ $R _ { 2 }$ ⋈ $R _ { 3 }$ can be obtained by the following expression consisting of seven terms:

$$
\begin{array}{l} \Delta V = (\Delta R _ {1} \bowtie R _ {2} \bowtie R _ {3}) \cup (R _ {1} \bowtie \Delta R _ {2} \bowtie R _ {3}) \\ \quad \cup (R _ {1} \bowtie R _ {2} \bowtie \Delta R _ {3}) \cup (\Delta R _ {1} \bowtie \Delta R _ {2} \bowtie R _ {3}) \\ \quad \cup (\Delta R _ {1} \bowtie R _ {2} \bowtie \Delta R _ {3}) \cup (R _ {1} \bowtie \Delta R _ {2} \bowtie \Delta R _ {3}) \\ \quad \cup (\Delta R _ {1} \bowtie \Delta R _ {2} \bowtie \Delta R _ {3}). \end{array}
$$

Since expression (1) requires too many terms in computing the change of a view, a new maintenance expression consisting of only n-terms has been proposed in Ref. [8] as follows.

$$
\begin{array}{c} \Delta V = (\Delta R _ {1} \bowtie R _ {2} \bowtie R _ {3} \bowtie \dots \bowtie R _ {n}) \\ \cup (R _ {1} ^ {\prime} \bowtie \Delta R _ {2} \bowtie R _ {3} \bowtie \dots \bowtie R _ {n}) \cup \dots \\ \cup (R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie \dots \bowtie R _ {n - 1} ^ {\prime} \bowtie \Delta R _ {n}). \end{array}\tag{2}
$$

Here, $R _ { \mathrm { ~ i ~ } } ^ { \prime }$ represents $R _ { \mathrm { i } } \cup \Delta R _ { \mathrm { i } }$ . Expression (2) is equivalent to expression (1), but has fewer terms. Roughly speaking, each term in expression (2) represents the change of $V$ due to the change of a certain base relation. For example, the first term $\Delta R _ { 1 } \bowtie R _ { 2 } \bowtie \ldots \bowtie R _ { n }$ represents the change of $V$ due to $\Delta R _ { 1 } ,$ , and the second term $R ^ { \prime } { } _ { 1 } \bowtie \Delta R _ { 2 } \bowtie R _ { 3 } \bowtie . . . \bowtie R _ { n }$ represents the change of $V$ due to $\Delta R _ { 2 }$ after $R _ { \mathrm { I } }$ has been updated. In general, the term $R ^ { \prime } { } _ { 1 } \bowtie \ldots \bowtie R ^ { \prime } { } _ { i - 1 }$ ⋈ $\Delta R _ { \mathrm { i } } \Join R _ { i + 1 } \Join .$ …⋈ $R _ { n }$ represents the change of $V$ due to $\Delta R _ { \mathrm { i } }$ after $R _ { 1 } , R _ { 2 } , . . . , R _ { i - 1 }$ have been updated.

Besides expression (1) and expression (2), there can be many other expressions that can be applied to compute the change of an SPJ view. In Ref. [12], however, it has shown that expression (2) can build the most efficient maintenance strategy so far.

How to maintain views correctly using the previous maintenance expressions when multiple data sources are distributed and their changes occur concurrently was discussed in Refs. [27,26,2]. Incremental maintenance of join views in a parallel RDBMS was described in Ref. [13]. Ref. [14] proposed a maintenance algorithm that exploits common subexpressions among view maintenance expressions. Ref. [10] proposed a new incremental view maintenance strategy that selectively propagates the change of some base relations while keeping batching others. However, all these works are based on expression (1) or expression (2) to compute the change of SPJ views.

## 1.2. Motivation

For the performance of an incremental maintenance express ion, the total amount of accesses to relations is very important. As we showed before, an incremental maintenance expression is composed of base relations and their delta relations in certain ways. Because the size of a base relation is much larger than that of its changes in general, the cost of evaluating incremental maintenance expression is mainly affected by the number of accesses to base relations.

Consider a view V defined over n base relations, i.e., $V = R _ { 1 } \bowtie R _ { 2 } \bowtie \ldots \bowtie R _ { n } .$ . Let us assume that each of the terms in a maintenance expression is evaluated independently. In expression (1), there are $( 2 ^ { n } - 1 )$ terms and each base relations is included in exactly $( 2 ^ { n - 1 } - 1 )$ terms. Thus, each base relation has to be accessed at least $( 2 ^ { n - 1 } - 1 )$ times to evaluate expression (2). On the other hand, expression (2) consists of $n -$ terms and each base relation is included in (n − 1) terms. Hence, each base relation is accessed only (n − 1) times to evaluate expression (2). This expression has been known to be the most efficient among all expressions developed until now [13]. However, we can further reduce the number of accesses to base relations. The following example motivates our approach.

For a view $V { = } R _ { 1 } \bowtie R _ { 2 } \bowtie R _ { 3 } ,$ , one of the expressions that compute $\Delta V$ by expression (2) is as follows.

$$
\begin{array}{c} \Delta V = (\Delta R _ {1} \bowtie R _ {2} \bowtie R _ {3}) \cup (R _ {1} ^ {\prime} \bowtie \Delta R _ {2} \bowtie R _ {3}) \\ \cup (R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie \Delta R _ {3}). \end{array}\tag{3}
$$

Consider the following expression that is equivalent to the above expression.

$$
\begin{array}{c} \Delta V = (((\Delta R _ {1} \bowtie R _ {2}) \cup (R _ {1} ^ {\prime} \bowtie \Delta R _ {2})) \bowtie R _ {3}) \\ \cup (R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie \Delta R _ {3}). \end{array}\tag{4}
$$

Here, $( \Delta R _ { 1 } \bowtie R _ { 2 } ) \cup ( R ^ { \prime } _ { 1 } \bowtie \Delta R _ { 2 } )$ is evaluated first, and then its result is joined with $R _ { 3 } { \mathrm { . } }$ . Hence, base relation $R _ { 3 }$ is accessed only once in expression (4) while $R _ { 3 }$ is accessed two times in expression (3). Thus, if the size of $R _ { 3 }$ is much larger than those of $R _ { 1 }$ and $R _ { 2 } { \mathrm { : } }$ , we can reduce the cost of computing $\Delta V$ considerably. Though the transformation in this case is quite simple, the optimal expression in the general case is not very straightforward. In this paper we propose an efficient incremental view maintenance method that guarantees high performance view maintenance.

We will assume throughout this paper that the join operation W has precedence over the union operation ⋃. Thus, we will sometimes omit the parenthesis in the expression if there is no ambiguity. That is, expression (4) can be described as $\Delta V = ( \Delta R _ { 1 } \bowtie R _ { 1 } \cup R ^ { \prime }  _ { 1 } \bowtie \Delta R _ { 2 } )$ ⋈ $R _ { 3 } \cup R ^ { \prime } _ { 1 } \bowtie R ^ { \prime } _ { 2 } \bowtie \Delta R _ { 3 }$

The remainder of the paper is organized as follows. In Section 2, we present our materialized view model, and then its cost model for performance comparison of various view maintenance strategies. Our view maintenance method called optimal delta evaluation is proposed in Section 3. Analysis of the proposed method is described in Section 4. We present an extension of the method to multiple views in Section 5. Section 6 gives results of performance experiments. Finally, we conclude our work in Section 7.

## 2. Preliminaries

## 2.1. View definition model

The derived data from remote information sources is stored in a data warehouse as fact tables, dimension tables or summary tables [11]. These tables can be seen as materialized views defined over certain base relations. When base relations are changed, the changes need to be propagated to these views properly to keep them up-to-date. In most data warehouse applications, source changes are gathered and propagated to the views in large batches for efficiency. The data warehouse is unavailable to users during the batch window. Hence, the study of the efficient view maintenance mechanisms is being pursed vigorously.

A materialized view can be variously defined over base relations or other materialized views or both. In this paper we consider materialized views defined by the select-project-join (SPJ) expression. SPJ views as a general form of a view definition can cover most of materialized views in a data warehouse environment. Moreover, an SPJ view can be easily extended to accommodate a view with aggregations using generalized projections [19].

An SPJ view V over n base relations $R _ { 1 } , R _ { 2 } , . . . R _ { 3 } ,$ , is defined as follows:

$$
V = \Pi_ {L \sigma C} (R _ {1} \bowtie R _ {2} \bowtie \dots \bowtie R _ {n})
$$

where L is a list of projection attributes and C is a selection condition.

For a base relation R, the changes of R are denoted by ΔR. We keep additional count information in each tuple of R and ΔR as in Ref. [8]. The count value for a tuple of R represents the number of distinct derivations of the tuple. The positive count value for a tuple of $\Delta R$ represents the number of newly inserted copies of the tuple into $R ,$ while the negative count value means the number of deleted copies of the tuple from R. An update is modeled as a delete followed by an insert. Some more details can be found in Ref. [8]. $R ^ { \prime }$ represents the relation R to which ΔR is propagated, i.e., $R ^ { \prime } { = } R \cup \Delta R .$ The formal definition of the union operator with the count value can be found in Refs. [5,8]. Based on this framework, our method can be applied to inserts, deletes, and updates of base tables. If the change of a view V is computed by $\Delta V { = } ( \Delta R _ { 1 } { \bowtie } R _ { 2 } ) \cup ( R ^ { \prime } { } _ { 1 } { \bowtie } \Delta R _ { 2 } )$ then an incremental maintenance of $V$ can be expressed as follows:

$$
V ^ {\prime} = V \cup (\Delta R _ {1} \bowtie R _ {2}) \cup (R _ {1} ^ {\prime} \bowtie \Delta R _ {2}).
$$

Note that our method can also be applied to aggregate SPJ views. For an SPJ view $V ,$ an aggregate SPJ view can be expressed as $\Pi _ { L } \left( V \right)$ , where Π is the generalized projection and L is the projected attributes that include aggregate functions. If aggregate functions are distributive (e.g., COUNT, SUM, AVG), the change of the aggregate SPJ view $\Pi _ { L } ( V )$ can be written as $\Delta ( \Pi _ { L } ( V ) ) =$ $\Pi _ { L } \left( \Delta V \right)$ where $\Delta V$ is the change of $V \left[ 1 9 \right]$ . Thus, our method can be applied to compute $\Delta V$ in $\Pi _ { L } \left( \Delta V \right)$ .

## 2.2. Cost model

In this paper we adopt the linear work metric developed in Ref. [12] as a cost model to compare view maintenance expressions. Although the linear work metric is relatively simple, the cost of processing complex maintenance expressions can be effectively estimated [12]. In the linear work metric, tne cost or processing a maintenance expression is tne sum or tne costs or processing each term of the expression when each term is assumed to be evaluated independently, and the cost of processing a term is proportional to the sum of the sizes of the operands of the term. Let Cost(E) be the cost of processing the expression E. If the change of view $V { = } R _ { 1 } \bowtie R _ { 2 } \bowtie R _ { 3 }$ is computed by expression (3), then the cost of computing $\Delta V$ can be obtained as follows:

$$
\begin{array}{l} \text { Cost } (\Delta V) = \text { Cost } (\Delta R _ {1} \bowtie R _ {2} \bowtie R _ {3}) \\ \qquad + \text { Cost } (R _ {1} ^ {\prime} \bowtie \Delta R _ {2} \bowtie R _ {3}) \\ \qquad + \text { Cost } (R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie \Delta R _ {3}) \\ = c \cdot (| \Delta R _ {1} | + | R _ {2} | + | R _ {3} |) \\ \qquad + c \cdot (| R _ {1} ^ {\prime} | + | \Delta R _ {2} | + | R _ {3} |) \\ \qquad + c \cdot (| R _ {1} ^ {\prime} | + | R _ {2} ^ {\prime} | + | \Delta R _ {3} |). \end{array}\tag{5}
$$

Here, c is a constant and $| R |$ is the size of relation R. $\mathrm { I f } \ \Delta V$ is computed by expression (4), Cost(ΔV) is as follows:

$$
\begin{array}{l} \operatorname{Cost} (\Delta V) = \operatorname{Cost} (((\Delta R _ {1} \bowtie R _ {2}) \cup (R _ {1} ^ {\prime} \bowtie \Delta R _ {2} ^ {\prime})) \bowtie R _ {3}) \\ \qquad + \operatorname{Cost} (R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie \Delta R _ {3}) \\ = \operatorname{Cost} ((\Delta R _ {1} \bowtie R _ {2}) \cup (R _ {1} ^ {\prime} \bowtie \Delta R _ {2})) \\ \qquad + c \cdot (| (\Delta R _ {1} \bowtie R _ {2}) \cup (R _ {1} ^ {\prime} \bowtie \Delta R _ {2}) | + | R _ {3} |) \\ \qquad + c \cdot (| R _ {1} ^ {\prime} | + | R _ {2} ^ {\prime} | + | \Delta R _ {3} |) \\ = c \cdot (| \Delta R _ {1} | + | R _ {2} | + | R _ {1} ^ {\prime} | + | \Delta R _ {2} |) \\ \qquad + c \cdot (| (\Delta R _ {1} \bowtie R _ {2}) \cup (R _ {1} ^ {\prime} \bowtie \Delta R _ {2} | + | R _ {3} |) \\ \qquad + c \cdot (| R _ {1} ^ {\prime} | + | R _ {2} ^ {\prime} | + | \Delta R _ {3} |). \end{array}\tag{6}
$$

Recall that $( \Delta R ^ { 1 } \bowtie R ^ { 2 } ) \cup ( R ^ { \prime } \bot \bowtie \Delta R ^ { 2 } )$ is evaluated first, and then its result is joined with R3 in expression (4).

## 3. Optimal delta evaluation method

We propose a new view maintenance method called the optimal delta evaluation method wmcn can minimize the cost of computing the change of a view. $\Delta V$ can be computed in many ways, each of which depends on the expression for $\Delta V .$ Thus, we need to find the optimal maintenance expression to minimize the cost of computing $\Delta V .$ For example, from expression (5) and expression (6), we can notice that the costs of computing $\Delta V$ become different depending on the expressions for $\Delta V .$

As we mentioned before, expression (2) has been known to be the most efficient maintenance expression described so far [12]. However, we can find out other equivalent maintenance expressions that further reduce accesses to base relations. The basic idea is based on recursive partitioning which is described below.

## 3.1. Recursive partitioning

Consider a view $V = R _ { 1 } \bowtie R _ { 2 } \bowtie R _ { 3 } \bowtie R _ { 4 }$ . According to expression (2), $\Delta V$ can be computed as follows.

$$
\Delta V = \left(\Delta R _ {1} \bowtie R _ {2} \bowtie R _ {3} \bowtie R _ {4}\right) \cup \left(R _ {1} ^ {\prime} \bowtie \Delta R _ {2} \bowtie R _ {3} \bowtie R _ {4}\right) \cup \left(R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie \Delta R _ {3} \bowtie R _ {4}\right) \cup \left(R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie R _ {3} ^ {\prime} \bowtie \Delta R _ {4}\right).\tag{7}
$$

By factoring out $R _ { 3 }$ ⋈ $R _ { 4 }$ from the first and second terms and $R _ { \mathrm { ~ l ~ } } ^ { \prime }$ ⋈ ${ { R } ^ { \prime } } _ { 2 }$ from the third and fourth terms, expression (7) can be rewritten such that

$$
\Delta V = \left(\left(\Delta R _ {1} \bowtie R _ {2} \cup R _ {1} ^ {\prime} \bowtie \Delta R _ {2}\right) \bowtie R _ {3} \bowtie R _ {4}\right) \cup \left(R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie \left(\Delta R _ {3} \bowtie R _ {4} \cup R _ {3} ^ {\prime} \bowtie \Delta R _ {4}\right)\right).\tag{8}
$$

Note that the number of accesses to each of $R _ { 1 } , R _ { 2 } , R _ { 3 } ,$ , and $R _ { 4 }$ is reduced to 2 in expression (8) while it is 3 in expression (7).

$$
\Delta \left(R _ {\mathrm{i}} \bowtie R _ {\mathrm{j}} \bowtie \dots \bowtie R _ {\mathrm{k}}\right)
$$

$$
\Delta \left(R _ {\mathrm{i}} \bowtie R _ {\mathrm{j}} \bowtie \dots \bowtie R _ {\mathrm{k}}\right)
$$

$$
R _ {\mathrm{i}} ^ {\prime} \bowtie R _ {\mathrm{j}} ^ {\prime} \bowtie \dots \bowtie R _ {\mathrm{k}} ^ {\prime}
$$

$$
R _ {\mathrm{i}} \bowtie R _ {\mathrm{j}} \bowtie \dots \bowtie R _ {\mathrm{k}}
$$

$$
R _ {\mathrm{i}} \bowtie R _ {\mathrm{j}} \bowtie \dots \bowtie R _ {\mathrm{k}}
$$

$$
\Delta V = \left(\Delta (R _ {1} \bowtie R _ {2}) \bowtie R _ {3} \bowtie R _ {4}\right) \cup \left(R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie \Delta (R _ {3} \bowtie R _ {4})\right),\tag{9}
$$

where $\Delta ( R _ { 1 } \bowtie R _ { 2 } ) { = } ( \Delta R _ { 1 } \bowtie R _ { 2 } ) \cup ( R ^ { \prime } \sb { 1 } \bowtie \Delta R _ { 2 } )$ and $\Delta ( R _ { 3 } \boxtimes R _ { 4 } ) = ( \Delta R _ { 3 } \boxtimes R _ { 4 } ) \cup ( R _ { 3 } ^ { \prime } \boxtimes \Delta R _ { 4 } )$ . Here, $\Delta ( R _ { 1 } \bowtie R _ { 2 } )$ and $\Delta ( R _ { 3 } \bowtie R _ { 4 } )$ are computed first before other remaining joins to compute $\Delta V .$ Expression (9) implies the following evaluation steps:

(i) The base relations are grouped into $\{ R _ { 1 } , R _ { 2 } \}$ and $\{ R _ { 3 } , R _ { 4 } \}$

(ii) For each group, the change of the join of base relations in that group is computed.

(iii) Then, the overall change of $V , \operatorname { i . e . , } \Delta V$ is computed by using the results of (ii).

Expression (7) can be rewritten in a number of different ways. For example,

$$
\Delta V = \left(\Delta \left(R _ {1} \bowtie R _ {2} \bowtie R _ {3}\right) \bowtie R _ {4}\right) \cup \left(R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie R _ {3} ^ {\prime} \bowtie \Delta (R _ {4})\right),\tag{10}
$$

where $\Delta ( R _ { 1 } \bowtie R _ { 2 } \bowtie R _ { 3 } ) = ( \Delta R _ { 1 } \bowtie R _ { 2 } \bowtie R _ { 3 } ) \cup ( R ^ { \prime } \sb 1 \bowtie \Delta R _ { 2 } \bowtie R _ { 3 } ) \cup ( R ^ { \prime } \sb 1 \bowtie R ^ { \prime } \sb 2 \bowtie \Delta R _ { 3 } )$ . Here, $\Delta ( R _ { 1 } \bowtie R _ { 2 } \bowtie R _ { 3 } )$ is computed first before other remaining joins. In this case, the base relations are grouped into $\{ R _ { 1 } , R _ { 2 } , R _ { 3 } )$ and $\{ R _ { 4 } \}$ which results in only one access to $R _ { 4 } .$ . Note that expression (9) and expression (10) show two different partitions of $\{ R _ { 1 } , R _ { 2 } , R _ { 3 } , R _ { 4 } \} , { \mathrm { i . e . , ~ } } \{ \{ R _ { 1 } , R _ { 2 } \} , \{ R _ { 3 } , R _ { 4 } \} \}$ } and $\{ \{ R _ { 1 } , R _ { 2 } , R _ { 3 } \} , \{ R _ { 4 } \} \}$ . Moreover, the evaluation costs of expression (9) and expression (10) should be different.

Now we generalize this concept. Suppose $V = R _ { 1 } \bowtie R _ { 2 } \bowtie \ldots \bowtie R _ { n } .$ . Let $\{ P _ { 1 } , P _ { 2 } , . . . P _ { m } \}$ be a partition of $\{ R _ { 1 } , R _ { 2 } , . . . R _ { n } \}$ such that $\cup _ { i = 1 } ^ { \mathrm { m } } P _ { \mathrm { i } } = \{ R _ { 1 } , R _ { 2 } , \cdot \cdot \cdot , R _ { n } \} , P _ { \mathrm { i } } \cap P _ { \mathrm { j } } = \varphi ( 1 \leq i \neq j \leq m )$ ; and $\mathrm { P _ { i } } \mathrm { \neq } \varphi \ \mathrm { ( 1 \leq i \leq m ) }$ . Then $\Delta V$ can be represented as follows:

$$
\begin{array}{c} \Delta V = (\Delta (\bowtie P _ {1}) \bowtie (\bowtie P _ {2}) \bowtie \dots \bowtie (\bowtie P _ {m})) \cup ((\bowtie P _ {1} ^ {\prime}) \bowtie \Delta (\bowtie P _ {2}) \bowtie \dots \bowtie (\bowtie P _ {m})) \cup \dots \\ \cup ((\bowtie P _ {1} ^ {\prime}) \bowtie (\bowtie P _ {2} ^ {\prime}) \bowtie \dots \bowtie \Delta (\bowtie P _ {m})), \end{array}\tag{11}
$$

where ⋈ $P _ { \mathrm { i } }$ and $\bowtie P _ { \mathrm { ~ i ~ } } ^ { \prime }$ denote $R _ { \mathrm { s } } \boxtimes R _ { \mathrm { t } } \boxtimes . . . \bowtie R _ { \mathrm { u } }$ and $R _ { \mathrm { ~ s ~ } } ^ { \prime } \boxtimes R _ { \mathrm { ~ t ~ } } ^ { \prime } \boxtimes . . . \ J \nabla _ { \mathrm { ~ u ~ } } ^ { \prime }$ respectively for $P _ { \mathrm { i } } { = } \{ R _ { \mathrm { s } } , R _ { \mathrm { t } } , {  } R _ { \mathrm { u } } \}$ Expression (11) partitions the set of base relations $\{ R _ { 1 } , R _ { 2 } , . . . , R _ { n } \}$ into m groups $P _ { 1 } , P _ { 2 } , . . . , P _ { m } ,$ , and the join of relations in each group is treated as if it were a base relation. It computes Δ(⋈ $P _ { 1 } ) , \Delta ( \Join P _ { 2 } ) , . . . , \Delta ( \Join P _ { m } )$ first, and then finally computes the overall change of V by using the results of $\Delta ( \bowtie P _ { 1 } ) , \Delta ( \bowtie P _ { 2 } ) , . . . , \Delta ( \bowtie P _ { m } )$

Now, computation of $\Delta ( \bowtie P _ { \mathrm { i } } ) ( 1 \leq i \leq m )$ can proceed by applying the same strategy recursively. In other words, computing $\Delta ( \bowtie P _ { \mathrm { i } } )$ can be performed by partitioning $P _ { \mathrm { i } }$ into multiple groups. Partitioning is recursively performed until each group in a partition has only one base relation. We call expression (11) a delta evaluation expression. Here, it is assumed that the expression is recursively expanded until $\Delta ( \bowtie P _ { \mathrm { i } } ) ( 1 \leq i \leq m )$ is resolved into $\Delta R _ { \mathrm { j } }$ for some $j \left( 1 \leq j \leq n \right)$ It is easy to see that the delta evaluation expression computes the changes of a view correctly.

Depending on the choices of $P _ { 1 } , P _ { 2 } , \dots , P _ { m } ,$ there can be many delta evaluation expressions for a view. For example, $P _ { \mathrm { i } } { = } \{ R _ { 1 } , ~ R _ { 2 } \} , ~ P _ { 2 } { = } \{ R _ { 3 } \}$ for a view $V { = } R _ { 1 } \bowtie R _ { 2 } \bowtie R _ { 3 }$ produce a delta evaluation expression $\Delta V =$ $( \Delta ( R _ { 1 } \bowtie R _ { 2 } ) \bowtie R _ { 3 } ) \cup ( R ^ { \prime } \sb 1 \bowtie R ^ { \prime } \sb 2 \bowtie \Delta ( R _ { 3 } ) )$ , while $P _ { \mathrm { i } } { = } \{ R _ { 1 } \} , P _ { 2 } { = } \{ R _ { 2 } \} , P _ { 3 } { = } \{ R _ { 3 } \}$ produce $\Delta V { = } ( \Delta ( R _ { 1 } ) \bowtie R _ { 2 } \bowtie R _ { 3 } ) \cup$ $( R ^ { \prime } \boldsymbol { \mathrm { _ 1 } } \bowtie \Delta ( R _ { 2 } ) \bowtie R _ { 3 } ) \cup ( R ^ { \prime } \boldsymbol { \mathrm { _ 1 } } \bowtie R ^ { \prime } \boldsymbol { \mathrm { _ 2 } } \bowtie \Delta ( R _ { 3 } ) )$ . Although all these expressions are equivalent, i.e., compute the change of the view correctly, their evaluation costs differ. Thus, we need to find the optimal delta evaluation expression among these expressions to minimize the maintenance cost. An incremental view maintenance method that uses the optimal delta evaluation expression to compute the change of a view is called the optimal delta evaluation method. Shortly, we will present an algorithm that finds the optimal delta evaluation expression for a view.

## 3.2. Delta evaluation trees

A delta evaluation expression can be represented as a tree, which we call a delta evaluation tree. Consider a delta evaluation expression for a view $V { = } R _ { 1 } \bowtie R _ { 2 } \bowtie . . . \bowtie R _ { n } .$ . Then the root node of the delta evaluation tree representing that expression is $\Delta V , { \mathrm { i . e . , ~ } } \Delta ( R _ { 1 } \bowtie R _ { 2 } \bowtie . . . \bowtie R _ { n } )$ . The changes of each base relation, i.e., $\Delta R _ { 1 } , \Delta R _ { 2 } , \dots \Delta R _ { n } ,$ become the leaf nodes of the tree. Each nonleaf node corresponds to $\Delta ( R _ { \mathrm { s } } \bowtie R _ { \mathrm { t } } \bowtie \ldots \ J \mathcal { A } R _ { \mathrm { u } } )$ for some $\{ R _ { \mathrm { s } } , R _ { \mathrm { t } } , \ldots , R _ { \mathrm { u } } \} \subseteq \{ R _ { 1 } , R _ { 2 } ,$ $. . . , R _ { n } \} . \ \mathrm { I f } \ \{ R _ { \mathrm { s } } , \ R _ { \mathrm { t } } . . . , R _ { \mathrm { u } } \}$ is partitioned into $P _ { 1 } , P _ { 2 , \cdots } P _ { m }$ in the corresponding delta evaluation expression for this tree, then $\Delta ( \bowtie P _ { 1 } ) , \Delta ( \bowtie P _ { 2 } ) , . . . , \Delta ( \bowtie P _ { m } )$ become the children of the node $\Delta ( R _ { \mathrm { s } } \boxtimes R _ { \mathrm { t } } \boxtimes . . . R _ { \mathrm { u } } )$ with $\Delta ( \bowtie P _ { \mathrm { i } } ) ( 1 \leq i \leq m )$ being the ith child from the left. For example, Fig. 1 shows two possible delta evaluation trees for $V = R _ { 1 } \bowtie R _ { 2 } \bowtie .$ $R _ { 3 } \bowtie R _ { 4 } \bowtie R _ { 5 } \bowtie R _ { 6 } .$ (The numbers in the upper left corner of each node in Fig. 1 will be described in Section 4.) Each tree in Fig. 1 represents the following delta evaluation expression:

$$
\begin{array}{c} (a) \Delta (R _ {1} \bowtie R _ {2} \bowtie R _ {3} \bowtie R _ {4} \bowtie R _ {5} \bowtie R _ {6}) = (\Delta (R _ {1} \bowtie R _ {2} \bowtie R _ {3} \bowtie R _ {4} \bowtie R _ {5}) \bowtie R _ {6}) \cup (R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie R _ {3} ^ {\prime} \bowtie R _ {4} ^ {\prime} \bowtie R _ {5} ^ {\prime} \bowtie \Delta (R _ {6})) \\ \Delta (R _ {1} \bowtie R _ {2} \bowtie R _ {3} \bowtie R _ {4} \bowtie R _ {5}) = (\Delta (R _ {1} \bowtie R _ {2}) \bowtie R _ {3} \bowtie R _ {4} \bowtie R _ {5}) \cup (R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie \Delta (R _ {3}) \bowtie R _ {4} \bowtie R _ {5}) \\ \cup (R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie R _ {3} ^ {\prime} \bowtie \Delta (R _ {4} \bowtie R _ {5})) \\ \Delta (R _ {1} \bowtie R _ {2}) = (\Delta (R _ {1}) \bowtie R _ {2}) \cup (R _ {1} ^ {\prime} \bowtie \Delta (R _ {2})) \\ \Delta (R _ {4} \bowtie R _ {5}) = (\Delta (R _ {4}) \bowtie R _ {5}) \cup (R _ {4} ^ {\prime} \bowtie \Delta (R _ {5})) \end{array}
$$

$$
\begin{array}{l} \text {(b)} \Delta (R _ {1} \bowtie R _ {2} \bowtie R _ {3} \bowtie R _ {4} \bowtie R _ {5} \bowtie R _ {6}) = (\Delta (R _ {1}) \bowtie R _ {2} \bowtie R _ {3} \bowtie R _ {4} \bowtie R _ {5} \bowtie R _ {6}) \cup (R _ {1} ^ {\prime} \bowtie \Delta (R _ {2}) \bowtie R _ {3} \bowtie R _ {4} \bowtie R _ {5} \bowtie R _ {6}) \\ \qquad \qquad \qquad \cup (R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie \Delta (R _ {3}) \bowtie R _ {4} \bowtie R _ {5} \bowtie R _ {6}) \cup (R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie R _ {3} ^ {\prime} \bowtie \Delta (R _ {4}) \bowtie R _ {5} \bowtie R _ {6}) \\ \qquad \qquad \qquad \cup (R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie R _ {3} ^ {\prime} \bowtie R _ {4} ^ {\prime} \bowtie \Delta (R _ {5}) \bowtie R _ {6}) \cup (R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie R _ {3} ^ {\prime} \bowtie R _ {4} ^ {\prime} \bowtie R _ {5} ^ {\prime} \bowtie \Delta (R _ {6}))  . \end{array}
$$

As you can notice, the expression represented by Fig. 1-(b) is the same as expression (2). In fact, when $P _ { 1 } { = } \{ R _ { 1 } \}$ $P _ { 2 } { = } \{ R _ { 2 } \} { \mathrm { , . . . , ~ } } P _ { n } { = } \{ R _ { n } \}$ , expression (11) is resolved into expression (2). That is, the delta evaluation expressions cover all the expressions that have the form of expression (2). As we mentioned before, there can be many possible delta evaluation trees for a given view. We will discuss how to find the optimal delta evaluation tree among them in the next subsection.

## 3.3. Optimal delta evaluation tree

In this paper, the optimal delta evaluation tree means one whose corresponding delta evaluation expression requires the minimal evaluation cost with respect to the cost model described in Section 2.2. We now present a dynamic programming algorithm that can find out the optimal delta evaluation tree for a given view.

For a given SPJ view, there can be many possible delta evaluation trees. As we can see in expression (11), different partitions $\{ P _ { 1 } , P _ { 2 } , . . . , P _ { m } \}$ of $\{ R _ { 1 } , R _ { 2 } , . . . , R _ { n } \}$ result in different delta evaluation trees. The number of different partitions $\{ P _ { 1 } , P _ { 2 } , . . . , P _ { m } \}$ of $\{ R _ { 1 } , R _ { 2 } , . . . , R _ { n } \}$ is $B ( n ) { \mathrm { . } }$ , which is the nth Bell number [16]. For a large value $n , B ( n )$ is approximately $n ^ { n } \left[ 9 \right]$ . Thus, there can be a large number of delta evaluation trees for a given view. The optimal delta evaluation tree is the one with the minimal evaluation cost among them.

![](/api/attachments/VV4YJ8XU/fulltext/images/fc48b7c33fce6de8dae2717f575561c00caa5ac64ad484f5c44f96882c646db3.jpg)  
Fig. 1. Delta evaluation trees.

We can obtain the evaluation cost of a delta evaluation tree by applying the linear work metric described in Section 2.2 to the delta evaluation expression represented by the tree. From expression (11) and the definition of the linear work metric, the cost of a delta evaluation expression can be computed recursively by the following equation. Here, we assume that the constant $c$ is equal to 1 in the linear work metric, for simplicity.

$$
\begin{array}{c} \operatorname{Cost} (\Delta R _ {\mathrm{i}}) = 0 \\ \operatorname{Cost} (\Delta (R _ {1} \bowtie R _ {2} \bowtie \dots \bowtie R _ {n})) = \sum_ {i = 1} ^ {m} \operatorname{Cost} (\Delta (\bowtie P _ {\mathrm{i}})) + (| P _ {1} ^ {\prime} | + | \Delta (\bowtie P _ {2}) |) + \dots + | P _ {m} |) \\ + \dots + (| P _ {1} ^ {\prime} | + | P _ {2} ^ {\prime} | + \dots + | \Delta (\bowtie P _ {m}) |), \end{array}\tag{12}
$$

where $| P _ { \mathrm { i } } | , | P _ { \mathrm { i } } ^ { \prime } |$ and $| \Delta ( \bowtie P _ { \mathrm { i } } ) |$ denote $| R _ { \mathrm { s } } | + | R _ { \mathrm { t } } | + \ldots + | R _ { \mathrm { u } } | , | R _ { \mathrm { ~ s } } ^ { \prime } | + | R _ { \mathrm { ~ t } } ^ { \prime } | + \ldots + | R _ { \mathrm { ~ u } } ^ { \prime } |$ and $| \Delta ( R _ { \mathrm { s } } { \bowtie } R _ { \mathrm { t } } { \bowtie } \ldots { \bowtie } R _ { \mathrm { u } } ) |$ respectively for $P _ { \mathrm { i } } { = } \{ R _ { \mathrm { s } } , R _ { \mathrm { t } } , { \ldots } , R _ { \mathrm { u } } \}$ }. Note that we assume $\mathrm { C o s t } ( \Delta R _ { \mathrm { i } } ) { = } 0$ because $\Delta R _ { \mathrm { i } } \left( 1 \leq i \leq n \right)$ are given, which means no need for computing it. The optimal delta evaluation expression is the one that minimizes expression (12).

To find an optimal solution that minimizes expression (12), we use the dynamic programming, which is commonly applied to optimization problems (Fig. 2). We use a bottom-up approach. That is, we first construct optimal delta evaluation tree for each base relation $R _ { \mathrm { i } } .$ Then we construct optimal delta evaluation trees for $R _ { \mathrm { i } } \bowtie R _ { \mathrm { j } } ( i \neq j )$ using the results of the first step. In the next step we construct optimal delta evaluation trees for $R _ { \mathrm { i } }$ ⋈ $R _ { \mathrm { j } } \bowtie R _ { \mathrm { k } } ( i \neq j \neq k )$ using the results of the previous steps. In this way, we can eventually construct the optimal delta evaluation tree for $R _ { 1 } \bowtie R _ { 2 } \bowtie \ldots$ ⋈ $R _ { n } .$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Procedure FindOptimalDeltaEvaluationTree(input: view  $V = R_{1} \bowtie R_{2} \bowtie \cdots \bowtie R_{n}$ )
/* Initialize */
For (i = 1 to n) do
    - Construct the optimal delta evaluation tree for  $R_{i}$ , i.e.,  $\Delta R_{i}$ .
/* Main body */
For (i = 2 to n) do
    For (each  $P \subseteq \{R_{1}, R_{2}, \cdots, R_{n}\}$  (such that the cardinality of P is i) do
    - Find the partition  $\{P_{1}, P_{2}, \cdots, P_{m}\}$  of P that minimizes expression (12).
    - Construct the optimal delta evaluation tree for  $(\mathbb{M} P)$  using optimal delta evaluation trees for  $(\mathbb{M} P_{1}), (\mathbb{M} P_{2}), \cdots, (\mathbb{M} P_{m})$ .
    (Note that the optimal delta evaluation tree for  $(\mathbb{M} P_{i})$  ( $1 \leq i \leq m$ ) is already obtained.)
    - Compute  $|P|, |P'|, |\Delta(\mathbb{M} P)|$  using  $|P_{i}|, |P_{i}'|, |\Delta(\mathbb{M} P_{i})|$  ( $1 \leq i \leq m$ ).
End For
End For
/* As a result, we can obtain an optimal delta evaluation tree for the input view V */
End Procedure
</div>

Fig. 2. Dynamic programming algorithm.

To construct the optimal delta evaluation tree for $R _ { \mathrm { s } }$ ⋈ $R _ { \mathrm { t } } { \bowtie } \ldots { \bowtie } R _ { \mathrm { u } } ,$ , we first find the partition $\{ P _ { 1 } , P _ { 2 } , . . . , P _ { m } \}$ of $\{ R _ { \mathrm { s } } , \ R _ { \mathrm { t } } , . . . , R _ { \mathrm { u } } \}$ that minimizes expression (12). Then the optimal delta evaluation tree for $R _ { \mathrm { s } } \boxtimes R _ { \mathrm { t } } \boxtimes . . . \bowtie R _ { \mathrm { u } }$ is constructed as follows. We make $\Delta ( R _ { \mathrm { s } } \bowtie R _ { \mathrm { t } } \bowtie \ldots \ J \bigotimes R _ { \mathrm { u } } )$ the new root node, and the optimal delta evaluation tree obtained for $( \bowtie P _ { \mathrm { i } } ) ( 1 \leq i \leq m )$ becomes the ith child from the left. Note that by the Principle of Optimality any subtree of an optimal delta evaluation tree must be also an optimal delta evaluation tree.

When we wish to apply the bottom-up based dynamic programming to expression (12), we need to compute $| \{ R _ { 1 } ,$ $R _ { 2 } . . . , R _ { n } \} | , | \{ R ^ { \prime } _ { 1 } , R ^ { \prime } _ { 2 } . . . , R ^ { \prime } _ { n } \} |$ and $| \Delta ( R _ { 1 } \bowtie R _ { 2 } \bowtie \ldots \ J \ O _ { M } R _ { n } ) |$ in terms of $| P _ { \mathrm { i } } | , | P _ { \mathrm { i } } ^ { \prime } |$ , and $| \Delta ( \bowtie P _ { \mathrm { i } } ) |$ . While $| \{ R _ { 1 } , R _ { 2 , \cdots } , R _ { n } \} | =$ $| P _ { 1 } | { + } | P _ { 2 } | { + } . . . { + } | P _ { m } |$ and $| \{ R ^ { \prime } { } _ { 1 } , \ R ^ { \prime } { } _ { 2 } , . . . , R ^ { \prime } { } _ { \mathrm { n } } \} | { } = | P ^ { \prime } { } _ { 1 } | + | P ^ { \prime } { } _ { 2 } | + . . . . + | P ^ { \prime } { } _ { \mathrm { m } } |$ can be easily computed, $| \Delta ( R _ { 1 } \bowtie R _ { 2 } \bowtie \ldots \bowtie R _ { n } ) |$ needs some way to compute it. Let JS $( R _ { 1 } , R _ { 2 } )$ be the join selectivity of relation $R _ { 1 }$ and $R _ { 2 } , \mathrm { i . e . }$ , the expected size of the join result divided by the maximum size $| R _ { 1 } | \times | R _ { 2 } |$ and then we have $ | R _ { 1 } \bowtie R _ { 2 } | = \mathrm { J S } \ ( R _ { 1 } , R _ { 2 } ) \times | R _ { 1 } | \times | R _ { 2 } |$ |. We can easily extend this to any number of relations as follows [24]:

$$
\left| R _ {1} \bowtie R _ {2} \bowtie \dots \bowtie R _ {n} \right| = \big (\prod_ {1 \leq i, j \leq n, i <   j} J S (R _ {\mathrm{i}}, R _ {\mathrm{j}}) \big) \times \left| R _ {1} \right| \times \left| R _ {2} \right| \times \dots \times \left| R _ {n} \right|.
$$

For simplicity, let us assume that $| ( \Delta R \bowtie S ) \cup ( R ^ { \prime } \bowtie \Delta S ) |$ is equal to $\left| \Delta R \bowtie S \right| { + } \left| R ^ { \prime } \bowtie \Delta S \right| ^ { 1 } [ 4 ]$ . Then we have

$$
\begin{array}{l} | \Delta (R _ {1} \bowtie R _ {2} \bowtie \dots \bowtie R _ {n}) | = | \Delta (\bowtie P _ {1}) \bowtie (\bowtie P _ {2}) \bowtie \dots \bowtie (\bowtie P _ {m}) | + | (\bowtie P _ {1} ^ {\prime}) \bowtie \Delta (\bowtie P _ {2}) \bowtie \dots \bowtie (\bowtie P _ {m}) | + \dots \\ \qquad + | (\bowtie P _ {1} ^ {\prime}) \bowtie (\bowtie P _ {2} ^ {\prime}) \bowtie \dots \bowtie \Delta (\bowtie P _ {m}) | \\ = \prod_ {1 \leq i, j \leq n, i <   j} J S (R _ {\mathrm{i}}, R _ {\mathrm{j}}) \times (| \Delta (\bowtie P _ {1}) | \times \prod_ {R _ {\mathrm{k}} \in P _ {2}} | R _ {\mathrm{k}} | \times \dots \times \prod_ {R _ {\mathrm{k}} \in P _ {m}} | R _ {\mathrm{k}} | + \prod_ {R _ {k} ^ {\prime} \in P _ {1} ^ {\prime}} | R _ {\mathrm{k}} ^ {\prime} | \\ \qquad \times | \Delta (\bowtie P _ {2}) | \times \dots \times \prod_ {R _ {\mathrm{k}} \in P _ {m}} | R _ {\mathrm{k}} | + \dots + \prod_ {R _ {k} ^ {\prime} \in P _ {1} ^ {\prime}} | R _ {\mathrm{k}} ^ {\prime} | \times \prod_ {R _ {k} ^ {\prime} \in P _ {2} ^ {\prime}} | R _ {\mathrm{k}} ^ {\prime} | \times \dots \times | \Delta (\bowtie P _ {m}) |). \end{array}
$$

From the above equation, we can obtain $| \Delta ( R _ { 1 } \bowtie R _ { 2 } \bowtie \ldots \ J \ O _ { n } ) |$

Based on the above observations, our dynamic programming algorithm named as FindOptimalDeltaEvaluationTree is presented in Fig. 4. FindOptimalDeltaEvaluationTree finds out the optimal delta evaluation tree for a given view based on the bottom-up approach. The algorithm first constructs the optimal delta evaluation tree for each base relation, which is unique and trivial as you expect. Then, it iteratively constructs the optimal delta evaluation tree for the join of each subset of $\{ R _ { 1 } , R _ { 2 } , . . . , R _ { n } \}$ from size 2 to n in stages. When we try to construct an optimal delta evaluation tree for the join of a subset of size $i ,$ the algorithm uses optimal delta evaluation trees already obtained for joins of subsets of size 1 to $( i - 1 )$ . Eventually, the algorithm finds out the optimal delta evaluation tree for a view defined over n base relations. For example, Fig. 3 shows how FindOptimalDeltaEvaluationTree finds the optimal delta evaluation tree for a view $V { = } R _ { 1 } \bowtie R _ { 2 } \bowtie R _ { 3 }$ . Each tree in Fig. 3 represents the optimal delta evaluation tree for the join of a certain subset of $\{ R _ { 1 } , R _ { 2 } , R _ { 3 } \}$

## 4. Analysis of the proposed method

First, let us consider the time complexity of Find OptimalDeltaEvaluationTree. Given a view $V { = } R _ { 1 }$ ⋈ $R _ { 2 } \bowtie \ldots \bowtie R _ { n } ,$ , the algorithm considers all possible subsets of $\{ R _ { 1 } , R _ { 2 } , . . . , R _ { n } \}$ to find out the optimal delta evaluation tree for the join of each subset of $\{ R _ { 1 } , R _ { 2 } , . . . ,$ $\textstyle R _ { n } \}$ . Also, for each subset $\{ R _ { \mathrm { s } } , R _ { \mathrm { t } } , . . . , R _ { \mathrm { u } } \} \subseteq \{ R _ { 1 } , R _ { 2 } , . . . ,$ $\textstyle R _ { n } \}$ , the algorithm traces all possible partitions of $\{ R _ { \mathrm { s } } , R _ { \mathrm { t } } ,$ $\cdots ^ { R _ { \mathrm { u } } } \}$ to construct the optimal delta evaluation tree for $R _ { \mathrm { s } }$ ⋈ $R _ { \mathrm { t } } { \bowtie } \ldots { \bowtie } R _ { \mathrm { u } } .$ . The number of all possible subsets of $\{ R _ { 1 } , R _ { 2 } , . . . , R _ { n } \}$ is $\textstyle \sum _ { i = 1 } ^ { n } C _ { i }$ ; where ${ } _ { n } C _ { i }$ is the number of combinations of size i from n distinct objects, and the number of all possible partitions of a set of size i is $B \left( i \right)$ Therefore, the worst time complexity of the algorithm is approximately $O ( \sum _ { i = 1 } ^ { n } \left( _ { n } C _ { i } \times B ( i ) \right) )$ . However, in prac-<sup>ð ¼ ð - ð ÞÞÞ</sup>tice, most views in data warehouses are defined over less than 10 base relations. For example, in TPC-R, which is a standard benchmark for decision support systems, each of the queries is defined over at most 7 base relations [23]. For $n \leq 7 , \ B ( n )$ is less than 900. Therefore, the algorithm can be used properly in finding out optimal delta evaluation trees for most data warehouse applications.

![](/api/attachments/VV4YJ8XU/fulltext/images/58d79a3ecbfcc3a26547e96a0f58278027301347367ae5b256cedf172cee4bc8.jpg)  
Fig. 3. An example of FindOptimalDeltaEvaluationTree.

Now, let us compare our optimal delta evaluation method with previous incremental maintenance methods. As we mentioned in Section 1.1, expression (2) has been known to be the most efficient maintenance expression among others proposed so far. Hence, we compare our method with a method that uses expression (2). We will compare the number of accesses to base relations in both methods, and then analyze the processing cost of both methods under the linear work metric.

As we mentioned in Section 1.2, every base relation has to be accessed (n − 1) times to evaluate expression (2). On the contrary, the number of accesses to each base relation may vary between 1 and (n − 1) in our method.

Theorem 4.1. For any delta evaluation expression of a view $V = R _ { I } \bowtie R _ { 2 } \bowtie \ldots \bowtie R _ { n } ,$ the number of accesses to base relation $R _ { i } ( l \leq i \leq n )$ , denoted by A , is less than or equal to $( n - l ) , i . e . , I \le A _ { i } \le ( n - l )$

Proof. We assume that the number of accesses to a base relation is simply equal to frequencies that the base relation appears in the maintenance expression. In expression (11), the terms in which base relation

$R _ { \mathrm { i } }$ (or $R _ { \mathrm { ~ i ~ } } ^ { \prime }$ appears always include $\Delta ( R _ { \mathrm { s } } \ \boxtimes \ R _ { \mathrm { t } } \boxtimes . . .$ ⋈ $R _ { \mathrm { u } } )$ where $R _ { \mathrm { i } } \notin \{ R _ { \mathrm { s } } , \ R _ { \mathrm { t } } , . . . , \ R _ { \mathrm { u } } \}$ . Thus, the number of accesses to $R _ { \mathrm { i } }$ can not exceed the number of all possible $\Delta ( R _ { \mathrm { s } } { \boxtimes } R _ { \mathrm { t } } { \boxtimes } \ldots { \boxtimes } R _ { \mathrm { u } } )$ , where $R _ { \mathrm { i } } \notin \{ R _ { \mathrm { s } } , \ R _ { \mathrm { t } } , . . . ,$ $R _ { \mathrm { u } } \}$ and $\{ R _ { \mathrm { s } } , R _ { \mathrm { t } } , . . . , R _ { \mathrm { u } } \} \subset \{ R _ { 1 } , R _ { 2 } , . . . , R _ { n } \}$ . Because any two $\{ R _ { \mathrm { s } } , R _ { \mathrm { t } } , . . . , R _ { \mathrm { u } } \}$ of such $\Delta \{ R _ { \mathrm { s } } \bowtie$ $R _ { \mathrm { t } } { \boxtimes } . . . { \boxtimes } R _ { \mathrm { u } }  \}$ are disjoint with each other, the number of all possible $\Delta ( R _ { \mathrm { s } } { \boxtimes } R _ { \mathrm { t } } { \boxtimes } . . . \ { \bowtie } R _ { \mathrm { u } }  \big \}$ is at most $| \{ R _ { 1 } , R _ { 2 }$ $. . . , R _ { n } \} - \{ R _ { \mathrm { i } } \} = \left( n - 1 \right)$ . Hence, this theorem may follow. □

Thus, the number of accesses to each base relation in the delta evaluation expression is always less than or equal to that in expression (2).

As we have seen, while all base relation need to be accessed (n − 1) times equally in expression (2), the number of accesses to each base relation can vary in our method. This makes our method more flexible and advantageous than previous methods. Suppose that $R _ { 6 }$ is much larger than the other base relations in Fig. 1. If we use a delta evaluation tree in Fig. 1-(a) rather than Fig. 1-(b), then we can reduce the cost of accessing the base relations considerably by reducing the number of accesses to $R _ { 6 }$ from 5 to 1. Note that even though the number of accesses to $R _ { 6 }$ is reduced to 1, the number of accesses to the other base relations, i.e., $R _ { 1 } , R _ { 2 } , R _ { 3 } ,$ $R _ { 4 } , R _ { 5 } ,$ , is still less than 5.

![](/api/attachments/VV4YJ8XU/fulltext/images/d0f23c658ac5eae707944ae83141b93668f1ee022e53403d5e4f9a32278136c5.jpg)  
Fig. 4. Reusing common intermediate results.

From now on, we will compare our method with a method that uses expression (2) with respect to the linear work metric. Consider a view $V { = } R _ { 1 } \bowtie R _ { 2 } \bowtie R _ { 3 } ,$ and suppose that $| R _ { 3 } |$ is much larger than $| R _ { 1 } |$ and $| R _ { 2 } |$ If we use expression (12), Cost(ΔV) can be as follows.

$$
\begin{array}{c} \operatorname{Cost} (\Delta V) = \operatorname{Cost} (\Delta R _ {1} \bowtie R _ {2} \bowtie R _ {3}) \\ \qquad + \operatorname{Cost} (R _ {1} ^ {\prime} \bowtie \Delta R _ {2} \bowtie R _ {3}) \\ \qquad + \operatorname{Cost} (R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie \Delta R _ {3}) \\ \qquad = 2 | R _ {1} ^ {\prime} | + | R _ {2} | + | R _ {2} ^ {\prime} | + 2 | R _ {3} | \\ \qquad + | \Delta R _ {1} | + | \Delta R _ {2} | + | \Delta R _ {3} |. \end{array}\tag{13}
$$

To reduce the number of accesses to $R _ { 3 } ,$ suppose that we use the following delta evaluation expression: $\Delta V =$ $( \Delta ( R _ { 1 } \bowtie R _ { 2 } ) \bowtie R _ { 3 } ) \cup ( R ^ { \prime } \sb { 1 } \bowtie R ^ { \prime } \sb { 2 } \bowtie \Delta R _ { 3 } ) , \Delta ( R _ { 1 } \bowtie R _ { 2 } ) =$ $( \Delta R _ { 1 } \bowtie R _ { 2 } ) \cup ( R ^ { \prime } _ { 1 } \bowtie \Delta R _ { 2 } )$ . In this case, the cost of computing $\Delta V$ is as follows:

$$
\begin{array}{l} \text { Cost } (\Delta V) = \text { Cost } ((\Delta (R _ {1} \bowtie R _ {2}) \bowtie R _ {3}) \cup (R _ {1} ^ {\prime} \bowtie R _ {2} ^ {\prime} \bowtie \Delta R _ {3})) \\ \quad = \text { Cost } (\Delta (R _ {1} \bowtie R _ {2})) + (| \Delta (R _ {1} \bowtie R _ {2}) | + | R _ {3} | \\ \quad \quad + | R _ {1} ^ {\prime} | + | R _ {2} ^ {\prime} | + | \Delta R _ {3} |) \\ \quad = (| \Delta R _ {1} | + | R _ {2} | + | R _ {1} ^ {\prime} | + | \Delta R _ {2} |) \\ \quad \quad + (| \Delta (R _ {1} \bowtie R _ {2}) | + | R _ {3} | + | R _ {1} ^ {\prime} | + | R _ {2} ^ {\prime} | \\ \quad \quad + | \Delta R _ {3} |) \\ \quad = 2 | R _ {1} ^ {\prime} | + | R _ {2} | + | R _ {2} ^ {\prime} | + | R _ {3} | \\ \quad \quad + | \Delta (R _ {1} \bowtie R _ {2}) | + | \Delta R _ {1} | + | \Delta R _ {2} | + | \Delta R _ {3} |. \end{array}\tag{14}
$$

Expression (13) and expression (14) differ only in that expression (13) has $2 \left| R _ { 3 } \right|$ while expression (14) has $| R _ { 3 } | + | \Delta ( R _ { 1 } \bowtie R _ { 2 } )$ | instead of $2 | R _ { 3 } |$ . This means that $R _ { 3 }$ is accessed twice in expression (13), while $R _ { 3 }$ is accessed only once but the temporary relation $\Delta ( R _ { 1 } \bowtie R _ { 2 } )$ is accessed additionally in expression (13). Because we have assumed that $| R _ { 1 } | \ll | R _ { 3 } |$ and $| R _ { 2 } | \ll | R _ { 3 } |$ , we can expect $| \Delta ( R _ { 1 } \bowtie R _ { 2 } ) | \ll | R _ { 3 } |$ in general. Thus, the cost of expression (14) is less than the cost of expression (13) in most cases. Therefore, we can conclude that our method can find out more efficient maintenance expressions than expression (2) with respect to the linear cost metric.

As we mentioned before, the major limitation of expression (2) is that every base relation must be accessed $( n - 1 )$ times equally regardless of its size. Compared with that, the optimal delta evaluation method can save the cost considerably by reducing the cost of accessing such large relations, e.g., $R _ { 3 }$ in expression (13).

## 5. Extension to multiple views

So far, we have described a strategy for maintaining a single view. However, in general, there can be more than one view in the data warehouse. These views often share some common expressions among them. If the intermediate results generated during maintaining some views can be reused to maintain other views, we may significantly reduce the overall maintenance cost. Recall that, in expression (11), our method computes $\Delta ( \bowtie P _ { 1 } ) , \ \Delta ( \bowtie P _ { 2 } ) , . . . , \Delta ( \bowtie P _ { m } )$ first to compute the overall change of V. Thus, if we can reuse $\Delta ( \bowtie P _ { \mathrm { i } } )$ to maintain other views, we may reduce the overall cost of accessing relations even more. In this section, we present an algorithm that reuses common intermediate results to maintain more than one view. The following example motivates our approach for sharing intermediate results.

Consider $V _ { 1 } { = } A \bowtie B \bowtie C$ and $V _ { 2 } = B \bowtie C \bowtie D$ . Fig. 4-(a) shows the optimal delta evaluation trees for $V _ { 1 }$ and $V _ { 2 }$ when $\Delta V _ { 1 }$ and $\Delta V _ { 2 }$ are computed separately. These are the locally optimal trees for $V _ { 1 }$ and $V _ { 2 } .$ However, if we reuse $\Delta ( B \bowtie C )$ , it may lead to the globally optimal plan. Fig. 4-(b) shows the globally optimal trees for $V _ { 1 }$ and $V _ { 2 }$ that share $\Delta ( B \bowtie C )$ . Note that reusing common results may not always lead to a globally optimal strategy. If $| \Delta ( B \bowtie C ) |$ is considerably larger than $| \Delta ( A \bowtie B )$ |, reusing $\Delta ( B \bowtie C )$ may not be a good plan. Thus, we need to decide what intermediate results should be materialized and reused. We will call this problem the multiple view maintenance problem.

## 5.1. Problem formulation

Let $V { = \{ V _ { 1 } , V _ { 2 } , . . . , V _ { n } \} }$ be a set of views to be maintained, and let MinCost $( \Delta V _ { \mathrm { i } } )$ denote the cost of the optimal delta evaluation tree for $V _ { \mathrm { i \cdot } }$ If we do not reuse any intermediate results, the total cost TotalCost of computing $\Delta V _ { 1 } , \Delta V _ { 2 }$ $. . . , \Delta V _ { n }$ and is as follows.

$$
\operatorname{TotalCost} (V) = \sum_ {V _ {\mathrm{i}} \in V} \operatorname{MinCost} (\Delta V _ {\mathrm{i}}).\tag{15}
$$

Let S denote a set of the intermediate results that are decided to be materialized and reused. For example, $S { = } \{ \}$ in Fig. 4-(a) and $S { = } \{ \Delta ( B \bowtie C ) \}$ in Fig. 4-(b). Let $\mathrm { M i n C o s t } ( \Delta V _ { \mathrm { i } } | S )$ denote the cost of the optimal delta evaluation tree for $V _ { \mathrm { i } }$ given that the expressions in S are already computed and materialized. It is clear that MinCost(ΔV |S) ≤ MinCost $( \Delta V _ { \mathrm { i } } )$ . Given a set $S ,$ the total cost TotalCost(V|S) of computing $\Delta V _ { \mathrm { 1 } } , \Delta V _ { \mathrm { 2 } } . . . \Delta V _ { \mathrm { n } }$ and using S is as follows.

$$
\operatorname{TotalCost} (V | S) = \sum_ {S _ {\mathrm{i}} \in S} \operatorname{MinCost} \left(S _ {\mathrm{i}} \mid S - \left\{S _ {\mathrm{i}} \right\}\right) + \sum_ {V _ {\mathrm{i}} \in V} \operatorname{MinCost} \left(\Delta V _ {\mathrm{i}} \mid S\right).\tag{16}
$$

The first term corresponds to the cost of computing S. Note that $\mathrm { M i n C o s t } ( S _ { \mathrm { i } } | S - \{ S _ { \mathrm { i } } \} )$ is used because $S _ { \mathrm { i } }$ should not be in S when we compute $S _ { \mathrm { i } } .$ . The second term corresponds to the cost of computing $\Delta V _ { 1 } , \Delta V _ { 2 } , . . . , \Delta V _ { n }$ given that the expressions in S are computed and materialized. To obtain $\mathrm { M i n C o s t } ( \Delta V _ { \mathrm { i } } )$ , we can use the FindOptimalDeltaEvaluationTree procedure in Section 3.3. However, for MinCost $( \Delta V _ { \mathrm { i } } | S )$ , we need to extend expression (12) in Section 3.3 to reflect S. Expression (12) is extended as follows:

$$
\begin{array}{c} \operatorname{Cost} (\Delta R _ {\mathrm{i}} | S) = 0 \\ \operatorname{Cost} (\Delta (R _ {1} \bowtie R _ {2} \bowtie \dots \bowtie R _ {n}) | S) = 0, \text { if } \Delta (R _ {1} \bowtie R _ {2} \bowtie \dots \bowtie R _ {n}) \in S \\ \operatorname{Cost} (\Delta R _ {1} \bowtie R _ {2} \bowtie \dots \bowtie R _ {n}) | S) = \sum_ {i = 1} ^ {m} \operatorname{Cost} (\Delta (\bowtie P _ {\mathrm{i}}) | S) + (| \Delta (\bowtie P _ {1}) | + | P _ {2} | + \dots + | P _ {m} |) \\ + (| P _ {1} ^ {\prime} | + | \Delta (\bowtie P _ {2}) | + \dots + | P _ {m} |) + \dots + (| P _ {1} ^ {\prime} | + | P _ {2} ^ {\prime} | \\ + \dots + | \Delta (\bowtie P _ {m}) |), \text { otherwise } \end{array}\tag{17}
$$

where $\mathrm { C o s t } ( \Delta V _ { \mathrm { i } } | S )$ denotes the cost of processing expression ΔV given that expressions S are materialized. Note that if we have $\Delta ( R _ { 1 } \bowtie R _ { 2 } \bowtie \ldots \bowtie R _ { n } )$ in S, Cost $\scriptstyle \Delta ( R _ { 1 } \bowtie R _ { 2 } \bowtie , . . . , \bowtie R _ { n } ) | S ) = 0$ . Using expression (17), we can obtain MinCost $( \Delta V _ { \mathrm { i } } | S )$ and the corresponding optimal delta evaluation tree for $V _ { \mathrm { i } }$ that uses S. Now, we can define the multiple view maintenance problem as follows: Given $V { = } \{ V _ { 1 } , ~ V _ { 2 } { , } { . } { . } { . } , V _ { n } \} ,$ find a set of intermediate results S to be materialized and reused, and the optimal delta evaluation trees for $V _ { 1 } , \ V _ { 2 } , . . . , V _ { n }$ that use $S$ such that TotalCost $( V | S )$ is minimized.

## 5.2. The greedy algorithm

The multiple view maintenance problem we have defined has the same form as the traditional multiple query optimization problem [21,18,22,20]. The aim of multiple query optimization is to exploit common subexpressions to reduce overall evaluation cost. A delta evaluation tree for a view in our problem corresponds to an access plan for a query in the multiple query optimization problem. Similarly, common nodes among delta evaluation trees correspond to common subexpressions among input queries. However, Ref. [21] showed that the multiple query optimization problem is NP-hard. For this reason, most work on the multiple query optimization has concentrated on heuristic algorithms. In this paper, we develop a heuristic algorithm that selects a set S to be reused in a greedy manner. Our approach is similar to that of Ref. [20]. After S is selected, the algorithm constructs the optimal delta evaluation tree for each view using S.

In our heuristic algorithm, we first construct a set C that contains all possible intermediate results that can be reused among views. It is clear that S must be a subset of C, i.e., S ⊆ C. To find the optimal set S that minimizes TotalCost(V| S), one of the simplest methods is to iterate over each subset of C and select a subset of C that minimizes TotalCost(V| S). However, the number of subsets of C is exponential in the size of C. Therefore the exhaustive algorithm that iterates over each subset of C is impractical. Fig. 5 shows a heuristic algorithm that selects S in a greedy manner. The algorithm iteratively picks shared expressions to materialize. At each iteration, the expression that is most beneficial to the total cost if it is materialized is chosen to be added to S. We present the performance result of our algorithm for multiple views in Section 6.

## 6. Experiments

We show in this section the results of various performance experiments among several view maintenance methods. The performance of each view maintenance method was measured by the time taken for updating a view by that method. In the experiments, we used the TPC-R benchmark 256MB RAM was used as the data warehouse environment. We defined two views, i.e., $V _ { 1 }$ and $V _ { 2 } ,$ each of which was defined as follows:

$$
\begin{array}{c} V _ {1} = \text { CUSTOMER } \bowtie \text { ORDERS } \bowtie \text { LINEITEM } \\ \bowtie \text { SUPPLIER } \bowtie \text { NATION } \bowtie \text { REGION } \end{array}
$$

V<sub>2</sub> PARTTSUPPLIERTLINEITEMTPARTSUPP TORDERTNATION:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Procedure GreedyMultipleViews(input: $V = \{V_1; V_2, ..., V_n\}$)
/* Initialize */
$C = \{ \Delta(R_s \bowtie R_t \bowtie ... \bowtie R_u) | R_s \bowtie R_t \bowtie ... \bowtie R_u \text{ is a common subexpression among two or more views in } V \}$ $S = \emptyset$
/* Main loop */
While ($C \neq \emptyset$) do
    Choose $c \in C$ which minimizes TotalCost ($V|S \cup \{c\}$)
    If (TotalCost($V|S \cup \{c\}) &lt; TotalCost(V|S)$) do
    $S = S \cup \{c\}; C = C - \{c\}$
    Else
    $C = \emptyset$
    End If
End While
/* Results */
Construct the optimal delta evaluation trees for $V_1; V_2, ..., V_n$ using $S$.
End Procedure
</div>

Fig. 5. A greedy algorithm for multiple views.

(a) $\mathrm { V } _ { 1 }$  
![](/api/attachments/VV4YJ8XU/fulltext/images/15254fe0c0cbec7a8fb2a10e4f8f4ddac0a53b2f06e485ef497c33ef8678110f.jpg)

(b) $\mathrm { V } _ { 2 }$  
![](/api/attachments/VV4YJ8XU/fulltext/images/3ab849675fcffd7d2cf84ba6199a24f00c6853b393e3256d21726d8900820c0f.jpg)  
Fig. 6. The performance evaluation by varying the size of changes.

The definitions of $V _ { 1 }$ and $V _ { 2 }$ are based on the TPC-R query $\mathcal { Q } _ { 5 }$ and $Q _ { 9 }$ respectively, and all the base relations were created and populated using the TPC-R schema.

In the experiments, we compared our optimal delta evaluation method with the recomputation method and the incremental maintenance method proposed in Ref. [12]. The method proposed in Ref. [12] uses expression (2) to maintain a view. As we mentioned in Section 1.1, Ref. [12] has showed that expression (2) is the best strategy among existing incremental strategies. Let us call expression (2) and the method in Ref. [12] the $n -$ term expression and the n-term method respectively. The n-term method uses an optimal n-term expression to maintain a view. According to Ref. [12], an optimal $n -$ term expression is the one that propagates the changes of base relations in increasing order of the size of the deltas of the base relations, i.e., $\left| R _ { \mathrm { i } } ^ { \prime } \right| - \left| R _ { \mathrm { i } } \right|$ . In the experiments, we used optimal n-term expressions for the n-term method.

The time taken for executing each view maintenance method for $V _ { 1 }$ and $V _ { 2 }$ is shown in Fig. 6-(a) and (b) respectively. In the experiment, we made changes to the base relations by inserting new tuples to the base relations. We varied the size of the changes to the base relations from 2% to 20% of their original size, which is a typically used range of changes in the experiments of incremental view maintenance methods [15,12]. Fig. 6 shows that our optimal delta evaluation method outperforms the other methods in our whole experiments, i.e., when changes are no greater than 20%.

The time reported in Fig. 6 includes optimization time. For the n-term method, optimization time means the time taken for finding an optimal n-term expression for a view. Similarly, for our method, optimization time means the time taken for finding an optimal delta evaluation tree for a view. However, for both methods, these optimizations took less than 2 s in our environment, which is negligible.

Table 1 shows the relative sizes of the base relations used in the experiments and the number of accesses to each base relation in the n-term method and our delta evaluation method for $V _ { 1 }$ and $V _ { 2 } .$ From Table 1, we can see that the number of accesses to relatively large base relations, e.g., LINEITEM, ORDERS, was reduced in our method. Consequently, our method becomes more efficient than the n-term method as we can see in Fig. 6.

![](/api/attachments/VV4YJ8XU/fulltext/images/58bfe96652562c1aef716f9bbca77de1fa3360e76fe01fc638763c6f21909115.jpg)

(b) $\mathrm { v } _ { 2 }$  
![](/api/attachments/VV4YJ8XU/fulltext/images/f15699a4aeccb6c956f41ba068792211e1965726caf0445ae569b4291dbf1b7e.jpg)  
Fig. 7. The performance evaluation by scaling the size of base relations.

Table 1  
The number of access to each base relation in the two incremental methods

<table><tr><td colspan="4"> $V_1$ </td><td colspan="4"> $V_2$ </td></tr><tr><td rowspan="2">Relation</td><td rowspan="2">Relative size</td><td colspan="2">Number of access</td><td rowspan="2">Relation</td><td rowspan="2">Relative size</td><td colspan="2">Number of access</td></tr><tr><td>n-term</td><td>Ours</td><td>n-term</td><td>Ours</td></tr><tr><td>REGION</td><td>Less than 1</td><td>5</td><td>5</td><td>NATION</td><td>Less than 1</td><td>5</td><td>5</td></tr><tr><td>NATION</td><td>Less than 1</td><td>5</td><td>5</td><td>SUPPLIER</td><td>1</td><td>5</td><td>5</td></tr><tr><td>SUPPLIER</td><td>1</td><td>5</td><td>4</td><td>PART</td><td>20</td><td>5</td><td>4</td></tr><tr><td>CUSTOMER</td><td>15</td><td>5</td><td>3</td><td>PARTSSUP</td><td>80</td><td>5</td><td>4</td></tr><tr><td>ORDERS</td><td>150</td><td>5</td><td>2</td><td>ORDERS</td><td>150</td><td>5</td><td>4</td></tr><tr><td>LINEITEM</td><td>600</td><td>5</td><td>2</td><td>LINEITEM</td><td>600</td><td>5</td><td>4</td></tr></table>

According to the cost model specified in the paper, the size of base relations may considerably affect the performance of view maintenance strategies. Fig. 7 shows the performance results of the three methods when we scaled the size of the base relations from 100% to 500%. Again in this case, our proposed method outperforms the other methods for both $V _ { 1 }$ and $V _ { 2 } .$ . Hence, we can confirm that our delta evaluation method is more efficient than existing ones in maintaining materialized views.

So far, we have considered the performance of maintaining a single view. The performance result of maintaining multiple views is shown in Fig. 8. Here, our method that allows sharing of intermediate results (i.e., ours (sharing)) is compared with the one that does not allow sharing (i.e., ours (no sharing)). The n-term method is also compared in the experiment. Along with $V _ { 1 }$ and $V _ { 2 } ,$ we also used the following four views in the experiment, all of which are based on the TPC-R queries.

V<sub>3</sub> PARTTSUPPLIERTPARTSSUPTNATION TREGION

V<sub>4</sub> CUSTOMERTORDERSTLINEITEM V<sub>5</sub> NATIONTLINEITEMTORDERSTSUPPLIER V<sub>6</sub> NATIONTCUSTOMERTORDERS TLINEITEM:

![](/api/attachments/VV4YJ8XU/fulltext/images/4943723c09ebd7deffdf71aaea2ac30c45052d294f9baaaf715e27807299f6d4.jpg)  
Fig. 8. The performance evaluation of updating multiple views.

The time reported in Fig. 8 is the optimization time plus the total time for updating all the six views. i.e., $V _ { 1 } ,$ $V _ { 2 } , . . . , V _ { 6 }$ and our optimal delta evaluation method performs better than the n-term method in this case also. As expected our extension to multiple views that share common intermediate results outperforms all the other methods.

## 7. Conclusion

Data warehouses store a large amount of summarized data to support decision making process. These summarized data can be seen as materialized views defined over some data sources. When data sources change, these materialized views need to be updated to reflect the changes of data sources. Since the updates of views may impose a significant overhead on the warehouse, it is very important to update the warehouse views efficiently. We presented the optimal delta evaluation method that can maintain materialized views efficiently in the data warehouse environment. The concept of the delta evaluation tree with consideration of the size of each base relation makes it possible to minimize the cost of maintaining views. As a result, the experimental results show the efficiency of the proposed method compared with previous methods. Moreover, the intermediate results of delta evaluation trees can be shared among views. We have also developed an extension such that intermediate results of delta evaluation trees can be reused when multiple views are updated. We showed through experiment that the proposed extension gives even more benefits than the method that maintains each view separately.

## References

[1] S. Chen, E.A. Rundensteiner, GPIVOT: efficient incremental maintenance of complex ROLAP views, Proceedings of ICDE Conference, 2005, pp. 552–563.

[2] S. Chen, B. Liu, E.A. Rundensteiner, Multiversion-based view maintenance over distributed data sources, ACM Transactions on Database Systems 29 (4) (2004) 675–709.

[3] L.S. Colby, T. Griffin, L. Libkin, I.S. Mumick, H. Trickey, Algorithms for deferred view maintenance, Proceedings of ACM SIGMOD Conference, 1996, pp. 469–492.

[4] H. Garcia-Molina, J.D. Ullman, J. Widom, Database System Implementation, Prentice Hall, 2000.

[5] T. Griffin, L. Libkin, Incremental maintenance of views with duplicates, Proceedings of ACM SIGMOD Conference, 1995, pp. 328–339.

[6] T.G. Griffin, L. Libkin, H. Trickey, An improved algorithm for the incremental recomputation of active relational expressions, IEEE Transactions on Knowledge and Data Engineering 9 (3) (1997) 508–511.

[7] H. Gupta, I.S. Mumick, Incremental Maintenance of Aggregate and Outerjoin Expressions, Technical Report, Stanford University, 1999.

[8] A. Gupta, I.S. Mumick, V.S. Subrahmanian, Maintaining views incrementally, Proceedings of ACM SIGMOD Conference, 1993, pp. 157–166.

[9] M. Hammer, B. Niamir, A heuristic approach to attribute partitioning, Proceedings of ACM SIGMOD Conference, 1979, pp. 93–101.

[10] H. He, J. Xie, J. Yang, H. Yu, Asymmetric batch incremental view maintenance, Proceedings of ICDE Conference, 2005, pp. 106–117.

[11] W.H. Immon, Building the Data Warehouse, Wiley Computer Publishing, 1996.

[12] W.J. Labio, R. Yerneni, H. Garcia-Molina, Shrinking the warehouse update window, Proceedings of ACM SIGMOD Conference, 1999, pp. 383–394.

[13] G. Luo, J.F. Naughton, C. Ellmann, M. Watzke, A comparison of three methods for join view maintenance in parallel RDBMS, Proceedings of ICDE Conference, 2003, pp. 177–188.

[14] H. Mistry, R. Roy, S. Sudarshan, K. Ramamritham, Materialized view selection and maintenance using multi-query optimization, Proceedings of ACM SIGMOD Conference, 2001, pp. 307–318.

[15] I.S. Mumick, D. Quass, B.S. Mumick, Maintenance of data cubes and summary tables in a warehouse, Proceedings of ACM SIGMOD Conference, 1997, pp. 100–111.

[16] B. Niamir, Attribute Partitioning in a Self-Adaptive Relational Database System, Technical Report, Massachusetts Institute of Technology, 1978.

[17] T. Palpanas, R. Sidle, R. Cochrane, H. Pirahesh, Incremental maintenance for non-distributive aggregate functions, Proceedings of VLDB Conference, 2002, pp. 802–813.

[18] J. Park, A. Segev, Using common sub-expressions to optimize multiple queries, Proceedings of ICDE Conference, 1998, pp. 311–319.

[19] D. Quass, Maintenance expressions for views with aggregation, Workshop on Materialized Views: Techniques and Applications, 1996, pp. 110–118.

[20] P. Roy, S. Seshadri, S. Sudarshan, S. Bhobe, Efficient and extensible algorithms for multi query optimization, Proceedings of ACM SIGMOD Conference, 2000, pp. 249–260.

[21] T. Sellis, Multiple query optimization, ACM Transactions on Database Systems 13 (1) (1988) 23–52.

[22] K. Shim, T. Sellis, D. Nau, Improvements on a heuristic algorithm for multi-query optimization, Data and Knowledge Engineering 12 (1994) 197–222.

[23] TPC Committee, Transaction Processing Council, http://www. tpc.org/.

[24] B. Vance, D. Maier, Rapid bushy join-order optimization with Cartesian products, Proceedings of ACM SIGMOD Conference, 1996, pp. 35–46.

[25] K. Yi, H. Yu, J. Yang, G. Xia, Y. Chen, Efficient maintenance of materialized top-k views, Proceedings of the ICDE Conference, 2003, pp. 189–200.

[26] X. Zhang, L. Ding, E.A. Rundensteiner, Parallel multisource view maintenance, The VLDB Journal 13 (1) (2004) 22–48.

[27] Y. Zhuge, H. Garcia-Molina, J.L. Wiener, Consistency algorithms for multi-source warehouse view maintenance, Distributed and Parallel Databases 6 (1) (1998) 7–40.

![](/api/attachments/VV4YJ8XU/fulltext/images/e4bd2402d2154dc5048d5f60425b53f732b8221bcc36ebe5c4dd5ee04662c430.jpg)  
Ki Yong Lee is a senior engineer at Samsung Electronics Co., Korea. He received his B.S. and M.S. degrees in Computer Science from Korea Advanced Institute of Science and Technology (KAIST), Daejeon, Korea, in 1998 and 2000, respectively, and his Ph.D. degree in Computer Science from KAIST in 2006. His research interests include database systems, data warehousing, OLAP and embedded software.

![](/api/attachments/VV4YJ8XU/fulltext/images/f7d19ba30e99402678ba17548b9d65a729f0ceb0164a72bf72cce1c486d935aa.jpg)

Jin Hyun Son is an assistant professor of the Department of Computer Science and Engineering at Hanyang University, Korea, from 2001. He was a postdoctoral researcher in the Division of Computer Science at Korea Advanced Institute of Science and Technology (KAIST), Daejon, Korea. He received his B.S. degree in Computer Science from Sogang University, Seoul, Korea, in 1996, and his M.S. and Ph.D. degrees in Computer Science from KAIST in

1998 and 2001, respectively. His research interests include database systems, distributed processing, business process management and embedded software.

![](/api/attachments/VV4YJ8XU/fulltext/images/e71132ad6d09bf27e8f90687315cd35716056b421978254f01dfa40774e3e8a8.jpg)

Myoung Ho Kim received his B.S. and M.S. degrees in Computer Engineering from Seoul National University, Seoul, Korea, in 1982 and 1984, respectively, and his Ph.D. degree in Computer Science from Michigan State University, East Lansing, MI, in 1989. In 1989 he joined the faculty of the Department of Computer Science at KAIST, Taejon, Korea, where currently he is a full professor. His research interests include database sys-

tems, data stream processing, sensor networks, mobile computing, OLAP, XML, information retrieval, workflow and distributed processing. He is a member of the ACM and IEEE Computer Society.
