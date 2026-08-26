---
otero_id: 4878
otero_key: "AG3YSB9U"
title: "Customer-oriented catalog segmentation: Effective solution approaches"
authors: "Ali Amiri"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.04.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 42 (2006) 1860– 1871

www.elsevier.com/locate/dss

# Customer-oriented catalog segmentation: Effective solution approaches

Ali Amiri <sup>⁎</sup>

Department of MSIS, College of Business, Oklahoma State University, Stillwater, OK 74078, USA

Received 23 May 2005; received in revised form 6 December 2005; accepted 2 April 2006 Available online 14 July 2006

## Abstract

We consider in this paper the customer-oriented catalog segmentation problem that consists of designing K catalogs, each of size r products that maximize the number of covered customers. A customer is covered if he/she has interest in at least the specified minimum number of products in one of the catalogs. The problem addresses the crucial issue of the design of the actual contents of the catalogs that serves as a back-end to catalog production for the purpose of more focused design of catalogs as a targeted marketing tool. We developed two algorithms to solve the problem. Results of an extensive computational study using real and synthetic data sets show that one of the proposed algorithms outperforms the state-of-the-art algorithm found in the literature in terms of customer coverage, resulting potentially in significant increase in organization profit. In the spirit of the guidance role that a Decision Support System (DSS) should play by recommending alternative, satisfactory solutions to the decision maker, the prototype of a DSS integrating all three algorithms is presented to provide the decision maker with an easy-to-use, yet powerful tool to examine various catalog design options and their implications on the contents of the catalogs and the clusters of covered customers.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Decision support system; Catalog design; Customer clustering

## 1. Introduction

In today's marketing-oriented era, product catalogs are used as an effective tool by a large number of companies that strive to achieve their goals through customer attraction, satisfaction, and retention. For these companies there is an increasing need to optimize the design of their product catalogs. By producing a variety of catalogs, a company can customize the contents of each catalog to meet the needs of a variety of segments of customers. With the fast growing number of products offered by retailers and e-retailers alike, the design of one catalog that can contain all products becomes impractical and non-economical. In many cases, some customers are interested in only a small portion of the products the company carries. It is more convenient for them (and more cost-effective for the company) to receive a catalog that represents just those particular lines or product categories that suit their needs.

Print catalogs are even widely used by online stores to allow customers to place orders online or by phone. For example, Landsend.com and Americanmusical.com have integrated their catalogs with their online stores to allow a customer to order items online easily by simply entering the item numbers as they appear in the catalogs.

In fact, the latest Benchmark Report on Operations conducted by Catalog Age magazine in 2005 [5] indicates that 70% of all survey respondents with sales of at least \$10 million have their transactional websites fully integrated with their catalog management systems. Catalogs, whether in the form of paper, CD-ROM or online, are used as an effective tool to attract customers to a store and purchase more products beyond the ones contained in the catalog.

One of the top challenges that companies using catalogs as a marketing tool face is the increase in marketing costs. The latest Benchmark Survey on Critical Issues and Trends conducted by Catalog Age magazine in 2003 [4] indicates that catalog companies that participated in the survey spent a mean 26.1% of their revenue on marketing expenses and that print and postage costs account for nearly half of those expenses. Catalogs created in other forms are also expensive. The number of catalogs that companies send to customers and potential buyers is increasing at a fast pace. For instance, Victoria's Secret mails around 395 million catalogs every year. The same survey mentioned earlier indicates that nearly four out of five of the respondents (79%) cited “the need to reduce costs without reducing offerings or services” as one of the top three management issues facing their companies. Faced with increasing marketing costs combined with the need to compete in the global economy, companies are looking for new ways to produce and use their catalogs more effectively. One way that has already been adopted is the automation of the creation of the layout of the catalog using expensive state-of-the-art software packages with price tags as high as millions of dollars depending on the integrated modules and the volume of products the software can handle. These software packages serve as a front-end in the catalog production process. In this paper, we address the crucial issue of the design of the actual contents of the catalogs that serves as a backend to catalog production for the purpose of more focused design of catalogs as a targeted marketing tool. This issue is independent of the catalog delivery media (e.g., paper, CD, or online) and hence all companies – traditional brick-and-mortar or online – can benefit from proper design of the contents of their catalogs.

Similar to the strategy of a manufacturer to offer a product line rather than a single product, a company can produce a line of catalogs rather than one single catalog to address the varying needs and interests of its customers. We consider in this paper the customeroriented catalog segmentation problem, first introduced in Ester et al. [7] as an extension to the classical catalog segmentation problem [11]. The customer-oriented catalog segmentation problem consists of designing K catalogs, each of size r products that maximize the number of covered customers. A customer is covered if he/she has interest in at least a specified minimum number t, called threshold, of products in one of the catalogs. A similar problem has been mentioned as an open problem in Kleinberg et al. [11].

The customer-oriented catalog segmentation problem is a customer clustering problem where:

• The task is to determine K clusters of customers where each cluster is defined by a set of products of interest to the customers and each customer is assigned to the cluster (equivalent to a catalog) that contains the largest number of products of interest to him/her.

• An acceptable clustering should satisfy two constraints:

○ The size of each cluster is r products,

○ A customer can be assigned to (i.e., covered by) a cluster of products only if the cluster contains at least t products of interest to the customer.

The goal is to maximize the number of customers assigned to (i.e., covered by) the clusters.

The conceptual foundation of catalog segmentation is the microeconomic framework for data mining that was introduced in Kleinberg et al. [10]. In this framework, a company considers many possible decisions about its customers who, depending on the decision selected, contribute differently to the overall utility/benefit of the decision [7]. In the case of segmentation (clustering) problems, the company strives to make the optimal decision per customer segment rather than per individual customer. The utility/ benefit of a catalog is measured by the number of customers who have interest in at least a specified minimum number of products in the catalog.

The classical catalog segmentation problem, introduced in Kleinberg et al. [11] seeks to maximize the number of catalog products of interest to customers with no regards to the customer utility to the company defined in terms of the minimum interest of the customer in at least t products in the catalog he/she receives, a concept referred to as customer coverage. The publication literature, with the exception of Ester et al. [7] focused exclusively on the classical segmentation problem. The authors in Refs. [10] and [12] outlined a sampling-based algorithm by basically enumerating and evaluating all possible partitions of a selected sample of customers. According to the authors [12], “the algorithm can only be shown to work under a fairly strong density assumption on instances” in the sample. Xu et al. [15] studied the 2-catalog segmentation problem where only two catalogs are designed. They developed an approximation algorithm based on semi-definite programming that has a performance guarantee of 1 / 2 for any size r of the catalog and a value greater than 1 / 2 when the size of the catalog is at least $m / 3$ , where m is the number of available products.

To overcome the inefficiency of the sampling-based algorithm, Steinbach et al. [13] studied two variations of the problem where a customer receives one catalog in the first variation and multiple catalogs over time in the second variation. They developed three algorithms based on the K-means clustering approach and reported computational results that compare the performance of the three algorithms.

As in Ester et al. [7], we study the customer-oriented catalog segmentation problem where the benefit/utility of a catalog is measured by the number of customers that have at least a specified minimum interest of t products in the catalogs sent to them. This concept of customer coverage in catalog segmentation is similar to the concept of minimum support in association rule mining [1,14]. The concept of customer coverage serves several purposes: (i) catalogs are not personalized to the individual level but to a like-behaving group of customers with similar interests [13]; (ii) a catalog sent to a customer containing only very few products of interest to him/her will not get his/her attention and therefore will be ineffective; and (iii) developing catalogs to target most promising customers can reduce marketing costs.

Given the complexity of the customer-oriented segmentation problem (discussed in the next section), we propose two algorithms to solve the problem. The first one constructs the catalogs one at a time in a greedy fashion. Each catalog contains initially all products and then some products are removed so as to minimize the number of uncovered customers until the necessary catalog size is reached. This greedy algorithm includes a clever randomization feature to avoid getting trapped in a local optimum. The second algorithm is inspired from association rule mining in the area of data mining and constructs also the catalogs one at a time. Products are grouped in catalogs to maximize associations between products defined in terms of customer interest relationships. Results of an extensive computational study using real and synthetic data sets show that the proposed greedy algorithm outperforms the state-of-the-art algorithm developed in Ester et al. [7] in terms of customer coverage, resulting potentially in significant increase in organization profit.

In the spirit of the guidance role that a DSS should play by recommending alternative, satisfactory (or satisfying) solutions to the decision maker (DM) [2], we present the prototype of a DSS integrating all three algorithms to provide the DM with an easy-to-use, yet powerful tool to investigate various catalog design options and their implications on the contents of the catalogs and the clusters of covered customers.

The remainder of the paper is organized as follows. In Section 2, we give the definition and formulation of the customer-oriented catalog segmentation problem. In Section 3, we present our two proposed algorithms to solve the problem. The following section discusses the DSS that integrates all algorithms to guide the decision maker in obtaining satisfactory catalog line. We then report the results of the extensive computational study to evaluate the performance of the algorithms in comparison with the one proposed in Ester et al. [7]. Finally, we provide conclusions and directions for future research in Section 6.

## 2. Problem definition and formulation

We assume that customers and their product interests are known [7]. The main input data for catalog segmentation is the customer interest database that contains the set of products that each customer is interested in. The product interests of a customer can be obtained either by aggregating all purchase transactions of the customer or by obtaining his/her explicit preferences from a set of products [7]. The customer-oriented catalog segmentation problem consists of designing K catalogs, each of size r products that maximize the number of covered customers. A customer is covered if he/she has interest in at least the specified minimum number (t) of products in one of the catalogs. Let $C _ { j }$ represent the set of products to be included in catalog j.

The following notation is used in the formulation of the model.

$$
\begin{array}{l l} N & \text {   set   of   customers,   indexed   by   } k \\ M & \text {   set   of   products,   indexed   by   } i \end{array}
$$

$$
a _ {k i} = \left\{ \begin{array}{l l} 1 & \text { if   customer } k \text { has   interest   in   product } i \\ 0 & \text { otherwise } \end{array} \right.
$$

$T$ set of catalogs, indexed by $j ; | T | = K$

r size of a catalog; i.e., $| C _ { j } | { = } r$

t minimum customer interest threshold

The decision variables are:

$$
X _ {k} = \left\{ \begin{array}{l l} 1 & \text { if   customer   } k \text {   is   covered,   i.e., } \\ & \text { the   customer   is   interested   in   at   least } \\ & t \text {   products   in   one   of   the   catalogs } \\ 0 & \text { otherwise } \end{array} \right.
$$

if customer k is covered by catalog j; V<sub>kj</sub> i:e:; the customer is interested in at least<sub>t products in the catalog</sub> 0 otherwise

$$
Y _ {j i} = \left\{ \begin{array}{l l} 1 & \text { if   customer } j \text { includes   product } i \\ 0 & \text { otherwise } \end{array} \right.
$$

$$
\text { Max } Z = \sum_ {k \in N} X _ {k}\tag{1}
$$

Subject to

$$
\sum_ {i \in M} Y _ {j i} = r \quad \forall j \in T\tag{2}
$$

$$
t V _ {k j} \leq \sum_ {i \in M} a _ {k i} Y _ {j i} \quad \forall k \in N, j \in T\tag{3}
$$

$$
X _ {k} \leq \sum_ {j \in T} V _ {k j} \quad \forall k \in N\tag{4}
$$

$$
X _ {k}, Y _ {j i}, V _ {k j} \in \{0, 1 \} \quad \forall k \in N, i \in M \text {   and   } j \in T\tag{5}
$$

The objective function represents the number of customers covered by at least one catalog. Constraints (2) ensure that each catalog includes r products. Constraints (3) guarantee that a catalog $j \in T$ covers a customer $k \in N$ only if the customer is interested in at least t products in the catalog. Constraints (4) ensure that a customer $k \in N$ is covered $( \mathrm { i } . \mathrm { e } . , X _ { k } { = } 1 )$ only if he/she is covered by at least one catalog. Constraints (5) represent the integrality requirements for the decision variables. Note that if the sizes of the catalogs are different, then the right-hand sides of constraints (2) should be set to $Q _ { j } ,$ where $\mathcal { Q } _ { j }$ is the number of products to include in catalog $j .$ The two algorithms developed in the next section as well as the algorithm presented in Ester et al. [7] to solve the problem can be effortlessly adapted to handle this extension very easily.

The following case example illustrates the definition of the problem. There are 20 customers and 10 products. The customer interest database is shown in Table 1. The threshold for the minimum customer interest is t = 4 products. The company wants to design 2 catalogs $( \mathrm { i } . \mathrm { e } . , K { = } 2 )$ of size $r { = } 4$ products each. One possible solution consists of catalogs 1 and 2 made of products {2,4,6,9} and {1,5,7,8}, respectively. This results in customers 4, 6, and 14 covered by catalog 1 and customers 3 and 9 covered by catalog 2. The task in the customer-oriented catalog segmentation problem is to create the catalog line that yields the optimal customer coverage.

Table 1  
Customer interest table for the case example

<table><tr><td>Customer</td><td>Products of interest</td><td>Customer</td><td>Products of interest</td></tr><tr><td>1</td><td>1,10</td><td>11</td><td>1,2,3,6,8,9</td></tr><tr><td>2</td><td>2,4</td><td>12</td><td>5</td></tr><tr><td>3</td><td>1,3,4,5,7,8</td><td>13</td><td>2,6,8</td></tr><tr><td>4</td><td>1,2,3,4,6,7,9,10</td><td>14</td><td>2,3,4,6,7,8,9,10</td></tr><tr><td>5</td><td>2,9</td><td>15</td><td>3,4,5</td></tr><tr><td>6</td><td>1,2,4,6,9</td><td>16</td><td>2,3,8</td></tr><tr><td>7</td><td>3,5</td><td>17</td><td>4,6</td></tr><tr><td>8</td><td>5,6,7,8</td><td>18</td><td>1,2,5,7,8</td></tr><tr><td>9</td><td>1,4,5,6,7,8,9</td><td>19</td><td>1,2,3,4,5,7,9</td></tr><tr><td>10</td><td>2</td><td>20</td><td>3,4,5,6,10</td></tr></table>

## 3. Catalog segmentation algorithms

The customer-oriented segmentation problem is very complex from a computational point of view. It is NPhard [7] as it is a generalization of the well-known NPhard maximum set covering problem [8]. This means the time needed to solve the problem increases at a much higher rate (non-polynomial) than the increase in the size of the problem. Therefore, for problem instances of realistic size, it is impractical to obtain optimal solutions in reasonable amount of time. For example, if the task is to create one catalog containing 10 products chosen from 40 available products, the total number of possible configurations exceeds ${ 1 0 } ^ { 9 }$ . This makes the strategic task of selecting even, say four catalogs combinatorially complex. Consequently, heuristics or approximate algorithms are proposed to generate “good” feasible solutions efficiently, but not necessarily optimally. This is in accordance with the recommendation of Barkhi at al. [2] to use approximate algorithms to find satisfactory (or satisfying) solutions in a timely fashion to complex problems such as ours when traditional optimization techniques such as Branch and Bound are doomed to fail to generate optimal (or even near-optimal) solutions in acceptable amount of time.

We propose two algorithms to solve the customeroriented segmentation problem. The first one, called Greedy Out (GO) algorithm, constructs the catalogs one at a time. Each catalog is formed initially by including all the products in the catalog and then removing $( | { \cal M } | ^ { - } r )$ products, one at a time, from the catalog in a greedy fashion so as to minimize the number of uncovered customers. The Greedy Out algorithm includes a randomization feature to avoid getting trapped in a local optimum. The second one, called Association-Based (AB) algorithm, is inspired from association rule mining in the area of data mining and constructs also the catalogs one at a time. Products are grouped in catalogs to maximize associations between products defined in terms of customer interest relationships.

## 3.1. The Greedy Out algorithm

The Greedy Out algorithm, as its name indicates, constructs the catalogs in a greedy fashion so as to maximize the number of customers covered. Each catalog $C _ { j }$ contains initially all available products, and then products are removed consecutively from the catalog until the number of products left in the catalog equals the required catalog size $r ,$ while minimizing the decrease of the number of covered customers. The algorithm uses two quantities to guide the search for the “victim” product to remove next from the catalog. The first quantity, called counter(k), represents the number of products in the current catalog that customer k is interested in, initially equals $\textstyle \sum _ { i \in M } a _ { k i }$ . The second quantity, called score(i), is computed for each product i included in the catalog $j _ { \scriptscriptstyle 1 }$ being formed as follows: $\begin{array} { r } { \mathrm { S c o r e } ( i ) = \sum _ { k \in N _ { j } ^ { \mathrm { c } } : a _ { k i } = 1 } \frac { 1 } { \mathrm { c o u n t e r } \ k } ; } \end{array}$ where $N _ { j } ^ { \mathrm { c } } { = } \mathrm { s e t }$ of cus-<sup>¼</sup>tomers (not covered by previous catalogs) who have interest in at least t products in the current catalog $j .$ Here, the parameter score(i) is used to identify the next product to remove from the current catalog. It is the product with the lowest score; that is, the product that makes the lowest number of customers uncovered or closer to being uncovered by the current catalog.

The Greedy Out algorithm is outlined below.

Step 1: Initialization:

$C _ { j } { = } M \forall j \in T ;$ i.e., catalog j initially includes all products.

• Counter k  P<sub>iaM</sub> a<sub>ki</sub> kaN

<sup>ð Þ ¼</sup>• Set of covered customers: $N ^ { \mathrm { c } } { = } \phi$

Step 2: For each catalog $j \in T$ do:

$N _ { j } ^ { \mathrm { c } } { = } \mathrm { S e t }$ of customers (not covered by previous catalogs) who have interest in at least t products in the current catalog $j ; ~ ( \mathrm { i . e . , }$ temporarily covered by catalog j which is under construction).

• For $h \mathrm { : } = 1$ to $| M |$ and r do

• For each product $i \in M$ included in the current catalog j do

▪ Calculate score(i)

• Remove the product $i ^ { * }$ with the lowest score from catalog $j , \mathrm { i . e . , } C _ { j } { : = } C _ { j } \backslash \{ i ^ { * } \}$

• For each uncovered customer $k \in N _ { j } ^ { \mathrm { c } }$ who has an interest in $i ^ { * }$ do

▪ counter(k): = counter(k) − 1

▪ if counter(k) < t, then $N _ { j } ^ { \mathrm { c } } { : = } N _ { j } ^ { \mathrm { c } } \backslash \{ k \}$

$N ^ { \mathrm { c } } { : = } N ^ { \mathrm { c } } \cup N _ { j } ^ { \mathrm { c } }$

• For each uncovered customer $k \notin N ^ { \mathrm { c } }$ reset $\begin{array} { r } { \mathrm { c o u n t e r } ( k ) \colon = \sum _ { j \in M } a _ { k i } } \end{array}$

Basically, the algorithm works as follows. Initially, none of the customers is covered $( \mathrm { i } . { \bf e } . , \ N ^ { \mathrm { c } } { = } \phi )$ . The catalogs are then constructed one at a time. Each catalog $j$ initially contains all available products $( \mathrm { i . e . , } \ C _ { j } { = } M )$ then products are removed until the catalog size r is reached, and at this stage the set $N _ { j } ^ { \mathrm { c } }$ of uncovered customers $( \mathrm { i . e . , }$ customers who do not belong to $N ^ { \mathrm { c } } )$ who still have interest in at least t products in the catalog j become covered (i.e., $N ^ { \mathrm { c } } { : = } N ^ { \mathrm { c } } \cup N _ { i } ^ { \mathrm { c } } )$ .

Greedy heuristics can get trapped in a local optimum. To overcome this problem, we add a randomization feature to our Greedy Out algorithm similar to the one used in Haouari and Chaouachi [9] to solve the set covering problem. Instead of removing the product $i ^ { * }$ with the lowest score from the catalog in step 2, we proceed in two sub-steps as follows. First, a set B of the f products with the lowest $f$ scores is identified (ties are broken arbitrarily). Second, a product in B is randomly selected for removal from the catalog. The selection probability of a product $i \in B$ is

$$
\begin{array}{l} p _ {i} = \frac {S _ {\max} - \operatorname{score} (i) + 1}{\sum_ {i \in B} (S _ {\max} - \operatorname{score} (i) + 1)}; \qquad \text { where } S _ {\max} \\ = \max \{\operatorname{score} (i): i \in B \}. \end{array}
$$

This probability distribution is decreasing with the scores of the products, and in this manner, the products with the lowest scores are favored. The value of the parameter f should be strictly greater than 1 to make the randomization feature active, but a large value of $f$ tends to make the heuristic pure random.

Given the significant computational complexity of the customer-oriented catalog segmentation problem, one can speed up the Greedy Out algorithm (as well as the other algorithms) by restricting the search of the products to include in the catalogs to the subset of the L most “popular” products, i.e., products with the highest interests among customers. These popular products can be easily identified by first sorting in non-increasing order the products based on $\textstyle \sum _ { k \in N } a _ { k i } .$ , and then selecting the first L products.

The proposed Greedy Out algorithm differs from the Randomized Best Product Fit algorithm (referred to as RBPF) proposed in Ester et al. [7] in the following ways. First, our algorithm starts with a catalog containing all products and then removes (|M| − r) products that results in the least number of customers loosing coverage; whereas the RBPF algorithm starts with an empty catalog and adds r products that results in the coverage of the highest number of customers. Second, the randomization feature is fully integrated in the Greedy Out algorithm so as to incorporate diversification within the algorithm; whereas the randomization step in the RBPF algorithm is applied only at the end of the algorithm. This step is repeated a specified number of times and involves selecting randomly a catalog, a product in the catalog, and a product not in the catalog and swapping the two products if the number of covered customers increases.

## 3.2. The Association-Based algorithm

Ideally, one wants to form a catalog by selecting a subset of r products from among the |M| available products that cover the maximum number of customers. Unfortunately, a complete enumeration of the exponential number of such subsets is computationally infeasible. The Association-Based algorithm groups products in a catalog to maximize associations between products defined in terms of customer interest relationships. These interest relationships indicate collections of products that are frequently liked together, i.e., have high associations. The motivation of this algorithm is the successful use of association rule mining in the area of data mining, especially in market basket analysis. By mining a basket data, a marketer identifies associations between products that are often purchased together by customers.

The Association-Based algorithm uses the following parameter: $S _ { i h }$ is the support for the 2-item set of products i and $h ;$ i.e., the number of uncovered customers who like both products i and $h ;$ in other words, $\begin{array} { r } { S _ { i h } = \sum _ { k \in N ^ { \mathrm { u } } } a _ { k i } a _ { k h } } \end{array}$ , where $N ^ { \mathrm { u } }$ is the set of uncovered <sup>¼</sup>customers. We limit ourselves to create a catalog by creating then union of 2-item sets such that the sum of their pairwise support is maximize. This is the equivalent to solving the following quadratic problem.

Problem Q:

Application of the algorithms to the case example

$$
\text { Max } \sum_ {i \in M} \sum_ {h \in M} S _ {i h} W _ {i} W _ {h}
$$

Subject to

$$
\sum_ {i \in M} W _ {i} = r
$$

$$
W _ {i} \in \{0, 1 \}
$$

$\begin{array} { r } { { W } _ { i } = \left\{ \begin{array} { l l } { 1 } \\ { 0 } \end{array} \right. } \end{array}$ if product i is included in the catalog where otherwise

The Association-Based algorithm is outlined below.

Step 1: Initialization:

$C _ { j } { = } \phi \ \forall j \in T$

• Set of uncovered customers $N ^ { \mathrm { u } } { = } N$

Step 2: For each catalog $j \in M$ do:

• Computer $S _ { i h }$ for every pair of products (i,h).

• Solve problem Q (either optimally or heuristically) to create catalog j.

• If a customer k is covered by catalog j, then $N ^ { \mathrm { u } } { : = } N ^ { \mathrm { u } } \backslash \{ \mathrm { k } \}$

Unfortunately, problem Q can be solved optimally and efficiently only for small size problems. For large size problems, we solve problem Q heuristically as follows. First, we select the pair of products that have the highest support among all pairs and include them in the catalog. Next, we add in a greedy fashion one product at a time. At each iteration, the product to be added to the catalog is the one that has the highest total support with the products already in the catalog.

## 3.3. Illustrative example

The results of the application of the three algorithms to the case example are shown in Table 2. The optimal solution obtained using CPLEX [6] is also included in the same table. The RBPF algorithm [7] produces a catalog line covering 3 customers. The solution produced by the Greedy Out algorithm covers 5 customers. The quality of the solution generated by the Association-Based algorithm depends on whether problem Q is solved heuristically (3 customers are covered) or optimally (5 customers are covered). The optimal catalog line covers 6 customers.

Table 2

<table><tr><td rowspan="2"></td><td rowspan="2">RBPF</td><td rowspan="2">Greedy out</td><td colspan="2">Association-Based algorithm</td><td rowspan="2">Optimal</td></tr><tr><td>Qis solved heuristically</td><td>Qis solved optimally</td></tr><tr><td>Catalogs</td><td>{1,2,3,4} {1,4,6,7}</td><td>{1,4,7,8} {2,3,4,9}</td><td>{1,2,3,4} {1,2,7,8}</td><td>{2,4,6,9} {1,5,7,8}</td><td>{1,2,6,9} {1,5,7,8}</td></tr><tr><td>Covered customers</td><td>{3,4,9}</td><td>{3,9,4,14,19}</td><td>{4,19,18}</td><td>{4,6,14,3,9}</td><td>{4,6,11,3,9,18}</td></tr></table>

![](/api/attachments/AG3YSB9U/fulltext/images/ffc6f1417e3c7185d459431a97e813d31db2f1004314e304af1cd07d04d5ba26.jpg)  
Fig. 1. DSS architecture.

## 4. DSS for customer-oriented catalog segmentation

In the spirit of the guidance role that a DSS should play by recommending alternative, satisfactory (or satisfying) solutions to the decision maker (DM) [2], we developed a prototype of a DSS integrating all three algorithms to provide the DM with an easy-to-use, yet powerful tool to investigate various catalog design options and their implications on the contents of the catalogs and the clusters of covered customers.

The main purpose of the DSS is to aid the decision maker (DM) in designing a catalog line and creating customer clusters. The DSS can be used on any PC running Windows. The general architecture of the DSS is shown in Fig. 1. The user interface is developed using the Delphi object-oriented programming language. The interactive environment of the DSS is based on the WIMP (window-menu-point) paradigm. A menu bar at the top of the screen lists the titles of the available pulldown menus. Scalable windows are used for displaying tabular or graphical information, allowing the visualization of the same information in different forms.

![](/api/attachments/AG3YSB9U/fulltext/images/33fe335f51e6319ba7c0b353aef8b85d59430c141a0768f432c0704ac6b66129.jpg)  
Fig. 2. The DSS welcome screen.

Dialog boxes are used to enter data, display messages, etc. Data entered by keying values in the appropriate locations in a dialog box is validated after the DM has clicked on the “Ok” button, therefore helping avoid input errors. The “Cancel” button in a dialog box nullifies the latest user request. The “Close” button is used to close a window that is used mainly to display information.

The DSS provides the DM with an easy-to-use, yet powerful tool to tackle this complex catalog segmentation problem. It allows the DM to examine various catalog design alternatives and their effects on the contents of the catalogs and the clusters of covered customers. When the DSS is launched, it displays a start-up, welcome notice (sometimes called a splash window) (Fig. 2). This window contains the name of the application (Catalog Segmentation Optimizer) and could contain other information (not shown here) such as user support information. Initially, the DM can load the customer interest database and specify values for the problem parameters such as the number of catalogs to create, their sizes, and the minimum interest threshold (Fig. 3). The customer interest data could be stored in a spreadsheet or relational database such MS Access or SQL Server database. Next, the DM can choose to solve the problem (using RBPF, Greedy Out, and Association-Based algorithms) from the Solve pulldown menu. The user can display the generated solution either graphically or in tabular form (Fig. 4). He/she can also solve the problem repeatedly for different values the problem parameters to be able to identify the best compromise design. The DM can, of course, edit the problem at any time by changing its parameter values.

![](/api/attachments/AG3YSB9U/fulltext/images/ee913c7d7a911895077193e21a89e7c33931d5009148fa5f43340290a23bc25c.jpg)  
Fig. 3. DSS user interface to load problem data.

![](/api/attachments/AG3YSB9U/fulltext/images/191026fc13c98a34323cb8a4f62c70da8c2778ff7385eb8745b03f437eb716b6.jpg)  
Fig. 4. DSS user interface to display the solution.

## 5. Computational experiments and results

We conducted extensive computational experiments using both real and synthetic data sets. This section describes the data used in the computational study and analyses the results.

## 5.1. Results for the real data set

The real data set corresponds to a retail market data set from an anonymous Belgian retail store reported in Brijs et al. [3] and it is available at the FIMI repository (http://fimi.cs.helsinki.fi/). The real data set includes 88 162 customers and 16 469 products, with each customer interested in 10.3 products on average. This data set is much larger than the real data set used in Ester et al. [7] based on the data set density (i.e., $\textstyle \sum _ { k \in N } \sum _ { i \in M } a _ { k i }$ which is equal to 908576 for our data set and 355 908 for the data set used in Ester et al. [7]). The task is to create a catalog line of 5 catalogs, each of containing 100 products. The threshold t for customer coverage equals 3. The RBPF algorithm [7] generated a catalog line that covers 54 483 customers, whereas our Greedy Out algorithm created a catalog line that covers 56100 customers. This corresponds to a 3% improvement in customer coverage. When we designed a catalog line with 4 catalogs, each of containing 500 products, and a threshold of 10, the RBPF algorithm generated a catalog line that covers 11 302 customers, whereas our Greedy Out algorithm created a catalog line that covers 12855 customers, corresponding to a 13.74% improvement in customer coverage. This important improvement in customer coverage can potentially result in significant increase in profit. The RBPF algorithm [7] took more than 20 h to solve the problem, whereas our Greedy Out algorithm took only 5 h.

## 5.2. Results for the synthetic data sets

We investigate the impact of various problem characteristics such as number of customers, number of products, and catalog size on the performance of the three algorithms, namely RBPF, Greedy Out, and Association-Based algorithm (solved heuristically) using the synthetic data sets. To this end, we employed a full factorial design experiment for the synthetic data sets using the following factors:

1. Number of customers (5000, 10000, 20000, 30000)

2. Number of products (1000, 2000)

3. Number of catalogs (1–4)

4. Catalog size (200–1000)

5. Threshold (8–12).

Following Ester et al. [7], the synthetic data sets are generated using the well-known IBM data generator [1]. We generated 10 instances of each problem category, resulting in a total of 65 data sets. Some of these data sets are much larger than the synthetic data set used in Ester et al. [7] based on the data set density (i.e., $\textstyle \sum _ { k \in N } \sum _ { i \in M } a _ { k i }$ which is equal to 613984 for our largest data set and 376 713 for the data set used in Ester et al. [7]). The results of applying the algorithms are given in Tables 3–5. Tables 3, 4 and 5 show the effects of changes in the threshold (t), number of catalogs (K), and catalog size (r) on the performances of all three algorithms, respectively. The average interest size, reported in the tables, represents the average number of products a customer is interested in.

We compare the performance of the three algorithms by comparing the values of the objective function of the solutions generated by the three algorithms. To this end, we use ${ \mathrm { G a p } } _ { X , Y }$ to represent the percentage change (i.e., increase if $\mathrm { G a p } _ { X , Y } { > } 0$ and decrease if $\mathrm { G a p } _ { X , Y } { < } 0 )$ in the number of customers covered by the catalog line generated by algorithm X over the number of customers covered by the catalog line generated by algorithm Y. More specifically $\mathrm { G a p } _ { X , Y } { = } 1 0 0 \% [ ( | N _ { X } ^ { \mathrm { c } } | - | N _ { Y } ^ { \mathrm { c } } | ) / ( | N _ { Y } ^ { \mathrm { c } } | ) ] ,$ where |N <sup>c</sup>| is the number of customers covered by the solution obtained using algorithm $Z ; ~ Z$ is either

Effects of changes in threshold (t) on the performance of the solution algorithms

<table><tr><td rowspan="2">|N|</td><td rowspan="2">|M|</td><td rowspan="2">Average interest size</td><td rowspan="2">K</td><td rowspan="2">r</td><td rowspan="2">t</td><td colspan="3">% Gap</td><td colspan="3">CPU (s)</td></tr><tr><td>RBPF,AB</td><td>GO,AB</td><td>GO,RBPF</td><td>RBPF</td><td>GO</td><td>AB</td></tr><tr><td rowspan="5">5000</td><td rowspan="5">1000</td><td rowspan="5">20.5</td><td rowspan="5">4</td><td rowspan="5">500</td><td>8</td><td>27.96</td><td>29.78</td><td>1.42</td><td>565</td><td>413</td><td>587</td></tr><tr><td>9</td><td>28.84</td><td>33.00</td><td>3.23</td><td>675</td><td>436</td><td>608</td></tr><tr><td>10</td><td>31.18</td><td>36.88</td><td>4.34</td><td>780</td><td>471</td><td>642</td></tr><tr><td>11</td><td>36.40</td><td>43.92</td><td>5.51</td><td>916</td><td>506</td><td>702</td></tr><tr><td>12</td><td>42.37</td><td>50.28</td><td>5.55</td><td>1050</td><td>549</td><td>760</td></tr><tr><td rowspan="5">10000</td><td rowspan="5">2000</td><td rowspan="5">20.6</td><td rowspan="5">4</td><td rowspan="5">500</td><td>8</td><td>26.64</td><td>32.68</td><td>4.77</td><td>6445</td><td>9295</td><td>12445</td></tr><tr><td>9</td><td>28.82</td><td>37.75</td><td>6.93</td><td>7542</td><td>9980</td><td>13979</td></tr><tr><td>10</td><td>31.44</td><td>45.33</td><td>10.57</td><td>8447</td><td>10260</td><td>13392</td></tr><tr><td>11</td><td>27.98</td><td>49.65</td><td>16.93</td><td>9251</td><td>10846</td><td>13485</td></tr><tr><td>12</td><td>29.06</td><td>59.08</td><td>23.25</td><td>10203</td><td>11879</td><td>14608</td></tr><tr><td rowspan="5">20000</td><td rowspan="5">2000</td><td rowspan="5">20.5</td><td rowspan="5">4</td><td rowspan="5">500</td><td>8</td><td>25.42</td><td>31.76</td><td>5.05</td><td>7154</td><td>8693</td><td>11137</td></tr><tr><td>9</td><td>42.61</td><td>51.77</td><td>6.42</td><td>8570</td><td>9711</td><td>11717</td></tr><tr><td>10</td><td>65.73</td><td>79.52</td><td>8.32</td><td>9800</td><td>10499</td><td>11657</td></tr><tr><td>11</td><td>93.49</td><td>118.18</td><td>12.76</td><td>10889</td><td>10917</td><td>11654</td></tr><tr><td>12</td><td>122.89</td><td>165.67</td><td>19.19</td><td>11760</td><td>11162</td><td>11808</td></tr><tr><td rowspan="5">30000</td><td rowspan="5">2000</td><td rowspan="5">20.5</td><td rowspan="5">4</td><td rowspan="5">500</td><td>8</td><td>27.23</td><td>32.19</td><td>3.90</td><td>11263</td><td>13847</td><td>16852</td></tr><tr><td>9</td><td>43.78</td><td>52.47</td><td>6.04</td><td>13227</td><td>15000</td><td>18252</td></tr><tr><td>10</td><td>69.33</td><td>80.59</td><td>6.65</td><td>14994</td><td>16044</td><td>19526</td></tr><tr><td>11</td><td>97.69</td><td>119.78</td><td>11.18</td><td>16500</td><td>16571</td><td>20167</td></tr><tr><td>12</td><td>131.19</td><td>167.91</td><td>15.88</td><td>17814</td><td>16875</td><td>20537</td></tr></table>

RBPF: Randomized Best Product Fit algorithm, AB: Association-Based algorithm, GO: Greedy Out algorithm $\mathrm { G a p } _ { X , Y } { = } 1 0 0 \% [ ( | N _ { X } ^ { \mathrm { c } } | - | N _ { Y } ^ { \mathrm { c } } | ) / ( | N _ { Y } ^ { \mathrm { c } } | ) ] ,$ where |N<sup>c</sup>| is the number of customers covered by the solution obtained using algorithm Z.

RBPF, Greedy Out (GO), or Association-Based (AB) algorithm. The higher the ${ \mathrm { G a p } } _ { X , Y }$ is, the better the performance of algorithm X is compared to algorithm Y. The gaps reported are the averages over the 10 instances in each category. The computational tests were run on a PC with an Intel Pentium III 1800 MHz processor 512 MB of memory.

Based on the results of the computational experiments reported in Tables 3–5, the Association-Based algorithm was the least effective in solving the problem.

Effects of changes in number of catalogs (K) on the performance of the solution algorithms

<table><tr><td rowspan="2">|N|</td><td rowspan="2">|M|</td><td rowspan="2">Average interest size</td><td rowspan="2">K</td><td rowspan="2">r</td><td rowspan="2">t</td><td colspan="3">% Gap</td><td colspan="3">CPU (s)</td></tr><tr><td>RBPF,AB</td><td>GO,AB</td><td>GO,RBPF</td><td>RBPF</td><td>GO</td><td>AB</td></tr><tr><td rowspan="4">5000</td><td rowspan="4">1000</td><td rowspan="4">20.5</td><td>1</td><td>500</td><td>10</td><td>11.75</td><td>9.22</td><td>-2.27</td><td>465</td><td>273</td><td>289</td></tr><tr><td>2</td><td></td><td></td><td>23.05</td><td>24.90</td><td>1.50</td><td>594</td><td>354</td><td>410</td></tr><tr><td>3</td><td></td><td></td><td>28.14</td><td>32.32</td><td>3.26</td><td>691</td><td>417</td><td>526</td></tr><tr><td>4</td><td></td><td></td><td>31.18</td><td>36.88</td><td>4.34</td><td>780</td><td>471</td><td>642</td></tr><tr><td rowspan="4">10000</td><td rowspan="4">2000</td><td rowspan="4">20.6</td><td>1</td><td>500</td><td>10</td><td>9.19</td><td>12.23</td><td>2.58</td><td>6888</td><td>8538</td><td>9025</td></tr><tr><td>2</td><td></td><td></td><td>5.05</td><td>13.56</td><td>8.10</td><td>7537</td><td>9460</td><td>11477</td></tr><tr><td>3</td><td></td><td></td><td>6.96</td><td>16.71</td><td>9.11</td><td>8090</td><td>9895</td><td>13860</td></tr><tr><td>4</td><td></td><td></td><td>6.49</td><td>17.75</td><td>10.57</td><td>8447</td><td>10260</td><td>16173</td></tr><tr><td rowspan="4">20000</td><td rowspan="4">2000</td><td rowspan="4">20.5</td><td>1</td><td>500</td><td>10</td><td>23.77</td><td>28.15</td><td>3.41</td><td>5953</td><td>6079</td><td>6034</td></tr><tr><td>2</td><td></td><td></td><td>28.84</td><td>37.02</td><td>6.35</td><td>7560</td><td>7912</td><td>8618</td></tr><tr><td>3</td><td></td><td></td><td>6.88</td><td>47.52</td><td>7.77</td><td>8791</td><td>9324</td><td>11275</td></tr><tr><td>4</td><td></td><td></td><td>40.11</td><td>51.77</td><td>8.32</td><td>9800</td><td>10499</td><td>13641</td></tr><tr><td rowspan="4">30000</td><td rowspan="4">2000</td><td rowspan="4">20.5</td><td>1</td><td>500</td><td>10</td><td>28.70</td><td>31.45</td><td>1.78</td><td>9172</td><td>9291</td><td>11431</td></tr><tr><td>2</td><td></td><td></td><td>30.46</td><td>36.53</td><td>4.65</td><td>11724</td><td>12216</td><td>15030</td></tr><tr><td>3</td><td></td><td></td><td>39.15</td><td>46.88</td><td>5.55</td><td>13661</td><td>14442</td><td>17571</td></tr><tr><td>4</td><td></td><td></td><td>42.96</td><td>52.47</td><td>6.65</td><td>14994</td><td>16044</td><td>19740</td></tr></table>

RBPF: Randomized Best Product Fit algorithm, AB: Association-Based algorithm, GO: Greedy Out algorithm $\mathrm { G a p } _ { X , Y } { = } 1 0 0 \% [ ( | N _ { X } ^ { \mathrm { c } } | - | N _ { Y } ^ { \mathrm { c } } | ) / ( | N _ { Y } ^ { \mathrm { c } } | ) ] ,$ where |N <sup>c</sup>| is the number of customers covered by the solution obtained using algorithm Z.

Effects of changes in catalog size (r) on the performance of the solution algorithms

<table><tr><td rowspan="2">|N|</td><td rowspan="2">|M|</td><td rowspan="2">Average interest size</td><td rowspan="2">K</td><td rowspan="2">r</td><td rowspan="2">t</td><td colspan="3">% Gap</td><td colspan="3">CPU (s)</td></tr><tr><td>RBPF,AB</td><td>GO,AB</td><td>GO,RBPF</td><td>RBPF</td><td>GO</td><td>AB</td></tr><tr><td rowspan="5">5000</td><td rowspan="5">1000</td><td rowspan="5">20.5</td><td rowspan="5">4</td><td>200</td><td></td><td>92.37</td><td>135.95</td><td>22.66</td><td>942</td><td>1414</td><td>1866</td></tr><tr><td>300</td><td></td><td>51.76</td><td>65.59</td><td>9.11</td><td>1030</td><td>1029</td><td>1327</td></tr><tr><td>400</td><td></td><td>39.90</td><td>48.36</td><td>6.05</td><td>902</td><td>666</td><td>879</td></tr><tr><td>500</td><td></td><td>31.18</td><td>36.88</td><td>4.34</td><td>780</td><td>471</td><td>642</td></tr><tr><td>600</td><td></td><td>8.04</td><td>9.81</td><td>1.63</td><td>710</td><td>349</td><td>471</td></tr><tr><td rowspan="8">10000</td><td rowspan="8">2000</td><td rowspan="8">20.6</td><td rowspan="8">4</td><td>300</td><td></td><td>72.80</td><td>171.71</td><td>57.24</td><td>6180</td><td>12840</td><td>17976</td></tr><tr><td>400</td><td></td><td>34.34</td><td>59.19</td><td>18.50</td><td>7906</td><td>12168</td><td>15575</td></tr><tr><td>500</td><td></td><td>31.44</td><td>45.33</td><td>10.57</td><td>8447</td><td>10260</td><td>13392</td></tr><tr><td>600</td><td></td><td>22.32</td><td>32.16</td><td>8.04</td><td>9339</td><td>9163</td><td>12095</td></tr><tr><td>700</td><td></td><td>18.47</td><td>25.97</td><td>6.33</td><td>8671</td><td>9737</td><td>11879</td></tr><tr><td>800</td><td></td><td>15.03</td><td>21.10</td><td>5.28</td><td>8357</td><td>6720</td><td>8333</td></tr><tr><td>900</td><td></td><td>12.03</td><td>16.72</td><td>4.18</td><td>8118</td><td>6077</td><td>7961</td></tr><tr><td>1000</td><td></td><td>11.18</td><td>15.00</td><td>3.44</td><td>7849</td><td>5305</td><td>6631</td></tr><tr><td rowspan="8">20000</td><td rowspan="8">2000</td><td rowspan="8">20.5</td><td rowspan="8">4</td><td>300</td><td></td><td>95.92</td><td>188.00</td><td>47.00</td><td>6250</td><td>12618</td><td>17160</td></tr><tr><td>400</td><td></td><td>79.22</td><td>106.48</td><td>15.21</td><td>8843</td><td>11835</td><td>15622</td></tr><tr><td>500</td><td></td><td>65.73</td><td>79.52</td><td>8.32</td><td>9800</td><td>10499</td><td>11657</td></tr><tr><td>600</td><td></td><td>44.64</td><td>54.50</td><td>6.81</td><td>9725</td><td>8632</td><td>11740</td></tr><tr><td>700</td><td></td><td>38.47</td><td>46.40</td><td>5.73</td><td>9051</td><td>6977</td><td>9210</td></tr><tr><td>800</td><td></td><td>28.64</td><td>34.30</td><td>4.40</td><td>8777</td><td>5807</td><td>7201</td></tr><tr><td>900</td><td></td><td>23.28</td><td>27.52</td><td>3.44</td><td>8368</td><td>4849</td><td>5867</td></tr><tr><td>1000</td><td></td><td>21.08</td><td>24.84</td><td>3.11</td><td>8030</td><td>4142</td><td>5178</td></tr><tr><td rowspan="8">30000</td><td rowspan="8">2000</td><td rowspan="8">20.5</td><td rowspan="8">4</td><td>300</td><td></td><td>210.66</td><td>344.39</td><td>43.05</td><td>10422</td><td>18960</td><td>23510</td></tr><tr><td>400</td><td></td><td>129.77</td><td>160.82</td><td>13.51</td><td>13562</td><td>17849</td><td>21597</td></tr><tr><td>500</td><td></td><td>69.33</td><td>80.59</td><td>6.65</td><td>14994</td><td>16044</td><td>19526</td></tr><tr><td>600</td><td></td><td>53.22</td><td>61.56</td><td>5.45</td><td>15180</td><td>13575</td><td>18598</td></tr><tr><td>700</td><td></td><td>45.18</td><td>51.91</td><td>4.64</td><td>14200</td><td>11446</td><td>15567</td></tr><tr><td>800</td><td></td><td>39.05</td><td>44.32</td><td>3.79</td><td>14318</td><td>9727</td><td>12840</td></tr><tr><td>900</td><td></td><td>34.73</td><td>39.17</td><td>3.29</td><td>14200</td><td>8292</td><td>10282</td></tr><tr><td>1000</td><td></td><td>31.69</td><td>35.60</td><td>2.97</td><td>13164</td><td>7125</td><td>8621</td></tr></table>

RBPF: Randomized Best Product Fit algorithm, AB: Association-Based algorithm, GO: Greedy Out algorithm Gap<sub>X,Y</sub> = 100%[(|N<sub>X</sub><sup>c</sup>| − |N<sub>Y</sub><sup>c</sup>|) / (|N<sub>Y</sub><sup>c</sup>|)], where |N<sup>c</sup>| is the number of customers covered by the solution obtained using algorithm Z.

The most likely reason is that problem Q was solved heuristically. Computational tests (not reported here) using very small instances show that the algorithm produced very competitive results when problem Q was solved optimally. However, solving problem Q optimally using the synthetic data sets described in the section turned out to be computationally impractical. Despite its relatively poor performance, the Association-Based algorithm is conceptually innovative. It draws its logic from the successful use of association rule mining in the area of data mining, especially in market basket analysis. The only shortcoming of the implementation of this algorithm is that the heuristic it uses to solve problem Q is not very effective. However, this does not diminish the merit of presenting and discussing the algorithm in the paper. In future research studies, researchers may develop more effective and efficient heuristics to solve problem Q, making the algorithm a more viable alternative to solve the customer-oriented catalog segmentation problem.

![](/api/attachments/AG3YSB9U/fulltext/images/f6470fd0215febdb1a648572c9d52431a7a65f18916c989f4b35798575a407c9.jpg)  
Fig. 5. Percentage of covered customers vs. threshold (t) using Greedy Out algorithm.

![](/api/attachments/AG3YSB9U/fulltext/images/f53fc29f5956a11b275048c6d8e8bc8cfc96ab961148283238f37f73067c289e.jpg)  
Fig. 6. Percentage of covered customers vs. number of catalogs (K) using Greedy Out algorithm.

Based on the results of the same experiments, our other proposed algorithm Greedy Out was the best; it produced solutions that are on average 9.14% better than those produced by RBPF. This out-performance is statistically significant (p-value = 0.000). The performance gap between Greedy Out and RBPF widens significantly in favor of Greedy Out with increases in the threshold (t) and the number of catalogs to create (K) and decrease in the size of the catalogs (r).

The Greedy Out and RBPF are still preferred to an exhaustive search for the optimal solution through branch-and-bound for example. Indeed, the state-ofthe-art commercial optimization software CPLEX [6], implementing a branch-and-bound approach, is very ineffective and inefficient in solving even small instances of the customer-oriented catalog segmentation problem. For example, we used Greedy Out, RBPF, and CPLEX to solve a small instance of the problem with 1000 customers and 20 products to construct a catalog line of 4 catalogs, each containing 4 products with a threshold equal to 4. The Greedy Out and RBPF algorithms generated catalog lines that cover 435 and 417 customers, respectively. Each algorithm took less than 1 s. However, CPLEX generated a catalog line that covers 419 customers after running for 7200 s. So, the common solver CPLEX is definitely not suitable to solve the customer-oriented catalog segmentation problem.

Figs. 5–7 show the change in the percentage of covered customers due to changes in the threshold (t), number of catalogs (K), and catalog size (r), respectively for the data sets with 5000 customers and 1000 products (using the Greedy Out algorithm). It is important to note that it may be impossible to cover 100% of the customers, as there may exist some customers who are interested in fewer products than the threshold t.

![](/api/attachments/AG3YSB9U/fulltext/images/327da518b8059b0cbfcbc71cda934d244f814588b12c7abd42a15411163f4465.jpg)  
Fig. 7. Percentage of covered customers vs. catalog size (r) using Greedy Out algorithm.

## 6. Concluding remarks

The microeconomic view of data mining has been widely used as a theoretical framework capturing the notion of utility of the discovered knowledge especially in the area of catalog segmentation. We studied in this paper the customer-oriented catalog segmentation problem where the utility/benefit of a catalog is measured by the number of customers who have interest in at least a specified minimum number of products in the catalog. Specifically, the problem consists of designing K catalogs, each of size r products that maximize the number of covered customers. A customer is covered if he/she has interest in at least a specified minimum number of products in one of the catalogs. The problem addresses the crucial issue of the design of the actual contents of the catalogs that serves as a back-end to catalog production for the purpose of more focused design of catalogs as a targeted marketing tool.

We proposed two algorithms to solve the customeroriented catalog segmentation problem. The first one, called Greedy Out algorithm, constructs the catalogs one at a time. Each catalog is formed initially by including all the products in the catalog and then removing (|M − r) products, one at a time, from the catalog in a greedy fashion so as to minimize the number of uncovered customers. The Greedy Out algorithm includes a randomization feature to avoid getting trapped in a local optimum. The second one, called Association-Based (AB) heuristic, is inspired from association rule mining in the area of data mining and constructs also the catalogs one at a time. Products are grouped in catalogs to maximize associations between products defined in terms of customer interest relationships.

We conducted an extensive computational study using real and synthetic data sets to compare the performance of the proposed algorithms to the Randomized Best Product Fit (RBPF) proposed in Ester et al. [7]. The results of the study show that the Greedy Out algorithm outperforms the AB and RBPF algorithm in terms of customer coverage, resulting potentially in significant increase in organization profit. The Greedy Out algorithm covers on average 59.65% and 9.14% (statistically significant) more customers than the AB and RBPF algorithms, respectively, using the synthetic data sets. The out-performance of the Greedy Out algorithm over the RBPF algorithm is also significant for the real data set as the former algorithm covered 3% to 13.74% more customers than the latter.

In the spirit of the guidance role that a DSS should play by recommending alternative, satisfactory (or satisfying) solutions to the decision maker (DM) [2], we presented the prototype of a DSS integrating all three algorithms to provide the DM with an easy-to-use, yet powerful tool to examine various catalog design options and their implications on the contents of the catalogs and the clusters of covered customers.

Although the current study makes a significant contribution in the area of catalog segmentation by developing an algorithm that outperforms another algorithm previously proposed by other researchers and by integrating all three algorithms discussed here in a DSS to guide the decision maker in designing a satisfactory catalog line, there are still some important issues in catalog segmentation that are not considered in the current study as well as past studies and therefore could be the subject of future research efforts. One such issue is the need to develop a way to evaluate the quality of the solutions to the problem by, for example, generating tight upper bounds to the problem. This is a very challenging issue since the customer-oriented segmentation problem is NPhard even when only one catalog is to be created and the interest threshold t = 1 [7]. Another issue deals with the space requirements of the products included in the catalogs. A product included in the catalog consumes space in the catalog for a description and image of the product. Space requirements are usually the same for all products. However, in special cases where these requirements are different, the capacity of a catalog should be redefined in terms of the space requirements of the products the catalog can accommodate rather in terms of the number of products it can include. This extension makes the problem much more difficult to solve.

## Acknowledgments

The author would like to thank Dr. Ramesh Sharda and Dr. Varghese Jacob and the anonymous referees for their useful feedback that helped improve the paper's contents and presentation.

## References

[1] R. Agrawal, R. Srikant, Fast algorithms for mining association rules, Proceedings of the 20th International Conference on Very Large Databases, Santiago, Chile, September 1994.

[2] R. Barkhi, E. Rolland, J. Butler, W. Fan, Decision Support System induced guidance for model formulation and solution, Decision Support Systems 40 (2) (2005) 269–281.

[3] T. Brijs, G. Swinnen, K. Vanhoof, G. Wets, The use of association rules for product assortment decisions: a case study, Proceedings of the Fifth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Diego, CA, August 1999, pp. 254–260.

[4] S. Chiger, Benchmark survey on critical issues and trends, Catalog Age 20 (13) (2003) 32–37.

[5] S. Chiger, Benchmark 2005 on Operations, www.catalogagemag. com, April 1, 2005.

[6] CPLEX 9.0 User's Manual, ILOG Inc., http://www.ilog.com, Mountain View, CA, 2004.

[7] M. Ester, R. Ge, W. Jin, Z. Hu, A Microeconomic Data Mining Problem: Customer-Oriented Catalog Segmentation, Proceedings of the 2004 ACM SIGKDD international conference on Knowledge discovery and data mining (Seattle, Washington), 2004, pp. 557–562.

[8] M.R. Garey, D.S. Johnson, Computers and Intractability, A Guide to the Theory of NP-Completeness, Freeman and Company, 1979.

[9] M. Haouari, J.S. Chaouachi, A probabilistic greedy search algorithm for combinatorial optimisation with application to the set covering problem, Journal of the Operational Research Society 53 (7) (2002) 792–799.

[10] J. Kleinberg, C. Papadimitriou, P. Raghavan, A microeconomic view of data mining, Data Mining and Knowledge Discovery 2 (1998) 311–324.

[11] J. Kleinberg, C. Papadimitriou, P. Raghavan, Segmentation problems, Proceedings of the Thirtieth Annual ACM Symposium on Theory of Computing (Dallas, Texas), 1998, pp. 473–482.

[12] J. Kleinberg, C. Papadimitriou, P. Raghavan, Segmentation problems, Journal of the ACM 51 (2) (2004) 263–280.

[13] M. Steinbach, G. Karypis, V. Kumar, Efficient algorithms for creating product catalogs, Proceedings of SDM, 2001.

[14] V. Verykios, A. Elmagarmid, E. Bertino, Y. Saygin, E. Dasseni, Association rule hiding, IEEE Transactions on Knowledge and Data Engineering 16 (4) (2004) 434–447.

[15] D. Xu, Y. Ye, J. Zhang, Approximating the 2-catalog segmentation problem using semidefinite programming relaxations, Optimization Methods and Software 18 (6) (2003) 705–719.

Ali Amiri received MBA and Ph.D. degrees in information systems from the Ohio State University, Columbus, OH, in 1988 and 1992, respectively, and a B.S. degree in business administration from the Institut des Hautes Commerciales, Tunisia, in 1985. He is an Associate Professor of Management Science and Information Systems at Oklahoma State University. His research interests include data communications, electronic commerce, data mining, and database management. His papers have appeared in a variety of journals including the European Journal of Operational Research, INFORMS Journal on Computing, ACM Transactions on Internet Technology, Information Sciences, and Naval Research Logistics.
