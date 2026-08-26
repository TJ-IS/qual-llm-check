---
otero_id: 14354
otero_key: "8KUPYUN6"
title: "Periodic cache replacement policy for dynamic content at application server"
authors: "I. Robert Chiang; Paulo B. Goes; Zhongju Zhang"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.10.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Periodic cache replacement policy for dynamic content at application server

I. Robert Chiang <sup>a</sup>, Paulo B. Goes <sup>b</sup>, Zhongju Zhang <sup>b,⁎</sup>

<sup>a</sup> Accenture - Hartford, One Financial Plaza, Hartford, Connecticut 06103, United States <sup>b</sup> School of Business, University of Connecticut 2100 Hillside Road, Storrs, CT 06269-1041, United States

Received 6 April 2006; received in revised form 25 August 2006; accepted 11 October 2006 Available online 6 December 2006

## Abstract

Web caching has been widely adopted to improve server responsiveness without resorting to costly infrastructure overhauls. However, due to the need to support real-time transactions and content customization, an increasing proportion of web pages contain fragments that are dynamically generated, typically results of database queries, rendering whole-page caching at browser or proxy level inappropriate. A promising approach has been to place dynamic fragments in a web application server cache for multiple web requests. In this paper, we propose a periodic cache replacement policy for dynamic web content at application server. Since the content of a dynamically generated web fragment could become stale, the value of a cached copy of the fragment will likely decrease as updates accumulate at the back-end database. Constantly replacing the cached copy of the fragment will increase its freshness and value, yet will also incur a high cache replacement cost. In addition, not all fragments are equally important to various applications and it is preferable to cache mission-critical fragments. The decision problem then consists of what fragments should be selected to cache and how frequently the cache should be replaced so that the total cache benefits per unit time is maximized. Numerical and simulation experiments show that the periodic cache replacement policy is robust and effective in handling dynamic content.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Server-side caching; Dynamic web contents; Knapsack problem; Cache invalidation

## 1. Introduction

During the past decades, the Internet has undergone a dramatic transformation from a military research experiment to an indispensable platform for such areas as science, education, and commerce. Reached by over 60% of the U.S. population and 10% worldwide [29], the Internet has gained global ubiquity while it continues to grow at a fast clip. However, due to the Internet's expanding presence and the growing user base, a recurring concern has been to maintain its performance [32]. The need for a responsive web site is especially crucial for e-commerce providers. As web users have become more sophisticated and less patient, they respond to long waits by making fewer purchases, or outright site abandonment. This could translate to significant business losses [18,35].

During the infancy of the commercialized Internet, long waiting times were often due to network transmission delays caused by the then limited backbone infrastructure. The frenzy telecom build-out in the dotcom era [14] has subsequently made the communication network a lesser source of user frustration. Browser or proxy level caches (mostly for static content) have also helped to mitigate the network transmission delays. Over the last few years, however, dynamic web contents (such as real-time news, stock quotes, sportscasts, etc.) have increased dramatically. In the meantime, many online portals also allow end users to personalize the web contents based on their own preferences. These dynamic and customized contents are mostly furnished by backend database operations and are generally not cacheable at the browser or proxy level [19,20,5]. Hence the management of dynamic content to deliver high value while at the same time keeping the overhead low poses significant challenges for e-business managers. In this context, IT managers need caching mechanisms that enable more efficient use of computing resources.

The objective of caching web content has been to minimize the re-transmission of identical content by placing caches close to where the requests originate. Previous literature on web content caching can generally be classified into two categories: static content caching and dynamic content caching [15]. Static content caching is usually implemented either at the browser or proxy side to help reduce the load on the public network. Much of the work in the browser-based caching has focused on active (i.e., prefetching) caching schemes (e.g., [9,31,36]). Proxy caching has been extensively studied in the context of when to remove items from cache (cache replacement). For example, Williams et al. [38] study a replacement policy which evicts the largest document in the cache. Mookerjee and Tan [28] analyze a least recently used policy for cache management in a web browser. Abrams et al. [1] propose a least recently used threshold replacement policy where documents larger than a certain threshold are never cached. Young [40] study the greedy dual policy where documents in the cache have the same size, but incur different costs to fetch from the secondary storage. Cao and Irani [12] extend the work of Young to allow variable-size documents. This policy was later generalized to incorporate both the frequency and the temporal locality of documents [23,33]. Aggarwal et al. [2] formulate the cache replacement problem as a knapsack problem to minimize the sum of frequencies for the outgoing objects. In order to maintain the consistency between the web cache and the data sources, cache invalidation mechanisms have been incorporated in the context of web proxy caching. For example, Cate [13] proposes an adaptive time-to-live (TTL) technique which associates a TTL with each cached object. Liu and Cao [25] study the server invalidation schemes to maintain the strong cache consistency.

Traditional caching mechanisms that handle static web content do not work well for database-driven dynamic content because of the volatility and variation of the content. Since most e-commerce applications are sensitive to the freshness of the information provided to end users, the dynamically generated content are usually made non-cacheable or expire immediately. Consequently, subsequent requests to the dynamically generated pages with the same content result in repeated computation overhead for the back-end (application and database) systems. There are several approaches to address this problem. One way is to cache the entire dynamically generated pages in the proxy cache (pagelevel caching) and constantly refresh the cached pages to keep them up-to-date [22,11]. However, this usually consumes significant amount of processing and communication resources, and sometimes requires architectural changes (such as adding a sniffer and invalidator) in the back-end systems. Another way is to periodically (rather than constantly) refresh the pages through the web server [3,39]. In this case, the amount of resources consumed will be reduced even though staleness of the content is unavoidable. Finally page-level caching becomes inefficient in the context of personalized pages because some parts of a page may change more rapidly than others. Even for the same page, individual users may see different content according to different preferences. Towards that end, fragment-level caching where dynamic fragments are cached at either proxies or application servers has been proposed [16,8,30].

In this paper, we propose a periodic cache replacement policy for dynamic web fragment at application server. This policy does not require architectural changes in the server side, nor does it consume considerable computing resources. Since a dynamically generated web fragment could change, the value of a cached copy of the fragment will likely decrease as updates accumulate at the back-end database. Constantly replacing the cached copy of the fragment will increase its freshness and value, yet will also incur a high cache replacement cost because of the overhead involved in tracking updates. In this context, continuous cache replacement to always maintain a fresh copy of the fragment (such as the one proposed by Candan et al. [11]) will not be optimal. In addition, not all fragments are equally important to various applications and it is preferable to cache mission-critical fragments. The decision problem then consists of what fragments should be selected to cache and how frequently the cache should be replaced so that the total cache benefits per unit time is maximized. A greedy heuristic is proposed to solve the optimization problem, and numerical results presented. Finally we conduct simulation experiments and show that the periodic cache replacement policy is robust and effective in handling dynamic content.

The rest of the paper is organized as follows. Section 2 discusses the key issues relevant to server-side caching design. Section 3 presents the basic modeling framework for dynamic web content caching, along with numerical results. Section 4 compares the proposed caching policy with two popular document replacement algorithms as well as examines the validity of the Poisson assumption through simulation experiments. Section 5 concludes the paper and offers directions for future research.

## 2. Dynamic caching issues

To improve dynamic caching decisions, it is necessary to examine how a dynamic web page is constructed. Fig. 1 shows a simplified illustration of server-side caching. An http command containing requests for dynamic content arrives at the web server. The command is parsed by the web server and requests for dynamic content are passed to the application server, which in turn queries the database server to generate original data elements. The application server then assembles and formats these elements to form partial-page fragments. A page template is then applied to describe the position and presentation of each fragment in the final page. Since the underlying data elements are dynamic, this process potentially is repeated each time a page request arrives. These repeated requests for dynamic pages (usually made for identical or similar content) place a significant strain on application infrastructure [30].

Fig. 1 also illustrates the two main technical solutions for caching dynamic content. The first one uses a frontend (i.e., reverse-proxy) cache for whole-page content [11], while the second one utilizes an application cache to store page fragments generated by database query results or materialized views [3]. Our approach focuses on managing the application cache for two reasons. First, much of the existing literature on proxy caching (with cache invalidation mechanism) of static content could be easily extended to the analysis of the reverseproxy cache. Second and more importantly, due to the bookkeeping overhead that is involved in tracking updates and requests, whole-page caching could be very costly in content personalization and customization environments [3].

Caching dynamically generated web content requires that consistency be maintained between the content in the cache and the content in the original data repositories. In general, two main mechanisms are available: expiration and invalidation. Under expiration, a fragment in the cache is assigned a time-to-live (TTL), after which a page request requiring that fragment will need to wait for it to be generated from the database server. While easy to implement, expiration mechanism is typically used in cases where content is updated at regular intervals (such as weather forecasts).

Invalidation messages are generally used in situations where changes are less predictable and more frequent [30]. These messages are sent from the database server to the cache manager, which marks specific fragments as invalid. Messages are typically triggered when a threshold of the number of database updates is reached. After being marked invalid in the cache, new requests to the fragment are served from the database. Even though content fragments could expire or be invalidated at different intervals or rates, replacements of the fragments are usually not done on an individual basis due to the tremendous overhead and setup costs. Rather, the whole (or a portion of) cache is replaced periodically to maintain the validity of the cached contents. The issue is of course when to conduct the cache replacement so as to tradeoff the accrued values of serving content from the cache against the costs of maintaining cache consistency.

## 3. The model

As said earlier, dynamic fragments are usually generated through queries from the back-end database. Since the underlying content of a fragment changes, the business value derived from serving a fragment from the cache will drop, depending on a number of factors, such as the elapsed time from last refresh, the rate of update process, the sensitivity of the application to the staleness, etc. We model the decreasing value of a cached fragment using a step function. Fig. 2 shows how the value of cached fragments will decrease as more updates are made to the corresponding database records.

![](/api/attachments/8KUPYUN6/fulltext/images/05ac64e775ff4d19c681005e7c8356e2f4c66e83a2b753a36a4b4552eb39a214.jpg)  
Fig. 1. Reverse-proxy cache and application cache at a web server site.

Assume that the intrinsic value for fragment i initially to be $V _ { i } ,$ i.e., the value of a fresh copy of fragment i is $V _ { i \cdot }$ The fragment value decreases on average by $C _ { i }$ following each database update, and will become zero (or the fragment becomes invalidated) after $n _ { i } \ ( n _ { i } \ge 1 )$ number of database updates. In the figure, for instance, the value of fragment 2 will become zero after two updates at time $\tilde { t } _ { 2 } ,$ where $\tilde { t } _ { 2 }$ is a random variable and denotes when the second update arrives. An invalidated fragment will still be served from the cache, but it will not add any value after it is invalidated. It should be pointed out that another fine-grained caching policy would be that once a cached fragment is marked invalid, the web cache requests the fragment from application (and database) server. The web cache then retains a copy of the fragment for subsequent requests. This mechanism might create an undesirable situation called “cache choking,” which occurs if the majority of the cache requests are re-directed to the database server.

We assume that the updates arriving at the database follow a Poisson process with a rate of $\gamma _ { i }$ for fragment i, and the requests for page fragment i follow another independent Poisson process with a rate of $\lambda _ { i \cdot }$ Since updates and requests are made by independent sources (users), it has been shown that the Poisson process is a reasonable approximation for the aggregate rate for each fragment [17]. In order to maintain cache consistency with the original data source, the whole cache<sup>1</sup> is to be replaced after every T time units, i.e., the contents from the cache are purged and fresh copies of the fragments are re-generated from the original repository. Alternatively, one could replace each fragment separately, at an interval of $T _ { i }$ for each fragment. However, this approach of cache replacement is unlikely in practice because of the high cost of replacement and large number of database connections.

Let us now look at the costs associated with maintaining cache consistency for fragment i after T time units. These costs have typically two components: (a) the set up cost (or fixed cost) B to open database connections, and (b) the execution cost (or variable cost) to query fragment i after T units of time are elapsed. The set up cost can be significant, which also help to explain why a group-based cache replacement policy is favorable since replacing fragments one at a time would result in incurring that fixed cost repeatedly. The execution cost involves executing a query at the database to obtain a fresh copy of the fragment. In the web context, the dynamic fragment usually contains small amount of information and does not involve complex queries (for example a stock quote). Further the fresh copy often depends on the most recent update, not the total accumulated updates, at the database. So we can assume that the query execution cost for fragment i is a constant $G _ { i } .$

![](/api/attachments/8KUPYUN6/fulltext/images/8bc8bc36b96ecba4bd61cf046e3eb12862fa9944b085392bebef5a7d54e4451b.jpg)  
Fig. 2. Value function and fragment invalidation.

In order to compute the expected total cumulative value $\mathrm { E V } _ { i } ( T )$ of a cached fragment i accrued by all requests during [0,T ], let us first consider the expected value during $[ 0 , T { + } \Delta T ]$ where $\Delta T$ is a small interval. If fragment i is invalidated with probability of $\scriptstyle \sum _ { k = n _ { i } } ^ { \infty } { \frac { \left( \gamma _ { i } T \right) ^ { k } \mathrm { e } ^ { - \gamma _ { i } T } } { k ! } }$ , the expected cumulative value remains <sup>¼</sup>the same. If fragment i is still valid, an additional value of $\lambda _ { i } \ : \Delta T ( V _ { i } - k C _ { i } )$ will be accrued where k is the number of updates occurred during [0,T]. Hence we can write the following differential equation:

$$
\begin{array}{l} \mathrm{EV} _ {i} (T + \varDelta T) = \sum_ {k = n _ {i}} ^ {\infty} \frac {(\gamma_ {i} T) ^ {k} \mathrm{e} ^ {- \gamma_ {i} T}}{k !} \mathrm{EV} _ {i} (T) \\ \qquad + \sum_ {k = 0} ^ {n _ {i} - 1} \frac {(\gamma_ {i} T) ^ {k} \mathrm{e} ^ {- \gamma_ {i} T}}{k !} [ \mathrm{EV} _ {i} (T) \\ \qquad + \lambda_ {i} \varDelta T (V _ {i} - k C _ {i}) ]. \end{array}
$$

Rearranging the terms and taking the limit when $\Delta T {  } 0$ , we get

$$
\begin{array}{c} \frac {\mathrm{dEV} _ {i} (T)}{\mathrm{d} t} = \lambda_ {i} V _ {i} \sum_ {k = 0} ^ {n _ {i} - 1} \frac {(\gamma_ {i} T) ^ {k} \mathrm{e} ^ {- \gamma_ {i} T}}{k !} \\ - \lambda_ {i} C _ {i} \sum_ {k = 1} ^ {n _ {i} - 1} \frac {(\gamma_ {i} T) ^ {k} \mathrm{e} ^ {- \gamma_ {i} T}}{(k - 1) !}. \end{array}
$$

The above differential equations can be solved, and the expected cumulative value of a cached fragment i is given by:

Proposition 1. (proof in the Appendix):

$$
\begin{array}{l} \mathrm{EV} _ {i} (T) = \lambda_ {i} V _ {i} T M _ {i} \\ \qquad + \frac {\lambda_ {i} n _ {i}}{\gamma_ {i}} \left[ V _ {i} + \frac {C _ {i}}{2} (1 - n _ {i}) \right] \left[ 1 - M _ {i} - \frac {\gamma_ {i} ^ {n _ {i}} T ^ {n _ {i}} \mathrm{e} ^ {- \gamma_ {i} T}}{n _ {i} !} \right] \\ \qquad - \frac {\lambda_ {i} \gamma_ {i} C _ {i}}{2} T ^ {2} \left[ M _ {i} - \frac {\gamma_ {i} ^ {n _ {i} - 1} T ^ {n _ {i} - 1} \mathrm{e} ^ {- \gamma_ {i} T}}{(n _ {i} - 1) !} \right], \end{array}
$$

where $M _ { i } = \sum _ { n = 0 } ^ { n _ { i } - 1 } \frac { ( \gamma _ { i } T ) ^ { n } \mathrm { e } ^ { - \gamma _ { i } T } } { n ! } .$ . It can be seen from Proposi-<sup>¼</sup>tion 1 that the total expected value EV (T) for fragment i increases as $V _ { i } , \lambda _ { i }$ increases, but decreases with $C _ { i } .$ . If a fragment is more popular, it should be more valuable and probably be given preference in selecting to cache. On the other hand, the value of a cached fragment that is more prone to change will likely decrease because the cached copy does not reflect the up-to-date information.

For a given cache size S, the overall decision is to maximize the expected total cache benefits per unit of time by selecting page fragments (i.e., setting $y _ { i }$ to 1 if fragment i is cached and 0 otherwise) and the refresh interval T.

$$
\begin{array}{l l} \max _ {T, y _ {i}} & z = \sum_ {i} y _ {i} \left[ \frac {\mathrm{EV} _ {i} (T) - G _ {i}}{T} \right] \\ \text {s.t.} & \sum_ {i} s _ {i} y _ {i} \leq S, \\ & y _ {i} \in \{0, 1 \}, \\ & T \geq 0, \end{array}\tag{1}
$$

where $s _ { i }$ is the size for fragment i and $\mathrm { E V } _ { i } ( T )$ is given by Proposition 1. The above problem is a non-linear mixedinteger optimization problem. This formulation, however, can be seen as a knapsack problem requiring additional considerations that the benefit brought by each item is time dependent, and the choice of the total time to keep the items in the knapsack is also part of the decision. It should be noted that in the above formulation, we omit the fixed set up cost B. This will not affect our optimal solution as the expected cache benefits per unit of time given by Eq. (1) would merely have a constant term (fixed set up cost) subtracted from it.

## 3.1. Solution procedures

Solutions for the non-linear mixed-integer problem in Eq. (1) can be obtained using an optimization software package for large-scale non-linear optimization problems. Due to the size of the problem (a cache could store thousands of fragments), however, a solution may not be possible when the size limit of the optimization software is exceeded. Another concern is the issue of “cache choking”, which could occur when majority of cache requests will be re-directed to database if the computation time exceeds the optimal refresh interval. We propose a simple heuristic solution procedure, which searches for the optimal value of $T ,$ and uses a well-known greedy method to select fragments according to the maximum “value per unit of storage” for the 0/1 knapsack problem within each iteration.

## 3.1.1. Heuristic

Step 0: Choose an arbitrary and positive value for T. EV<sub>i</sub> T −G<sub>i</sub>

Step 1: For given T, calculate the $\frac { T } { s _ { i } }$ ratio of each <sup>i</sup>fragment. Place fragments to cache based on the value in descending order until the capacity is reached.

Step 2: Based on the assignment, $y _ { i } ,$ obtained in Step 1, calculate the optimal refresh interval $T ^ { * }$

Step 3: If $\vert T ^ { * } - T \vert < \varepsilon ,$ , STOP; otherwise, set $T = T ^ { * }$ and repeat from Step 1.

For a given interval T, Step 1 above requires a simple sort operation on each fragment's benefit-to-size ratio.

## 3.2. Remarks on basic model formulation

## 3.2.1. Cache partitions

As mentioned before, it is possible to replace a section of the cache. The optimization problem in

Table 1

<table><tr><td>Parameters</td><td>Description</td><td>Unit</td></tr><tr><td> $V_i$ </td><td>Intrinsic business value of fragment  $i$ </td><td>$</td></tr><tr><td> $\lambda_i$ </td><td>Arrival rate of requests for fragment  $i$ </td><td>Arrivals/minute</td></tr><tr><td> $\gamma_i$ </td><td>Update rate for fragment  $i$ </td><td>Updates/minute</td></tr><tr><td> $s_i$ </td><td>Size of fragment  $i$ </td><td>Kbytes</td></tr><tr><td> $n_i$ </td><td>Number of updates that fragment  $i$  will be invalidated</td><td>-</td></tr><tr><td> $C_i$ </td><td>Value decrement per update for  $i$ </td><td>$</td></tr><tr><td> $G_i$ </td><td>Execution cost of fragment  $i$ </td><td>$</td></tr><tr><td> $S$ </td><td>Total cache size</td><td>Kbytes</td></tr></table>

Table 2  
Baseline parameter values

<table><tr><td>Parameters</td><td>Range of values</td></tr><tr><td> $V_i$ </td><td>Uniform [0.1, 0.5]</td></tr><tr><td> $λ_i$ </td><td>Uniform [10, 20]</td></tr><tr><td> $γ_i$ </td><td>Uniform [1, 5]</td></tr><tr><td> $s_i$ </td><td>Uniform [0, 2]</td></tr><tr><td> $n_i$ </td><td>Uniform [1, 20]</td></tr><tr><td> $G_i$ </td><td>Uniform [0.1, 0.3]</td></tr><tr><td>S</td><td>100</td></tr></table>

Eq. (1) may be more applicable to partitions of the cache. By using association rules [21] and other machine learning techniques on the access patterns of the fragments, page fragments can first be grouped into separate partitions [10]. The formulation in Eq. (1) can then be used to identify the best refresh intervals and fragments selection for each partition.

## 3.2.2. Capacity

It has been argued [24] that one does not need a capacity constraint to address cache fragment selection in the web environment. On one hand, the capacity costs have decreased dramatically in the last few years. On the other hand, the complexity of the operations in the tiered architecture of web caching has also increased substantially with increased cache capacity. The capacity decision is exogenous in our model, while naturally larger capacities will increase the size of the optimization problem.

## 3.2.3. Estimation of parameters

The remaining issue in our model formulation is the estimation of various parameters that are summarized in Table 1.

There are three types of parameters in our model, the arrival rates of requests $( \lambda _ { i } )$ and updates $( \gamma _ { i } )$ for a fragment, the fragment size $( s _ { i } )$ , and the various cost parameters $( V _ { i } , G _ { i } , C _ { i } )$ . The arrival rates and fragment size can be determined by observing the arrival patterns available from the transaction log of the web server and the database server. With respect to the different cost parameters, a Delphi-type procedure could be employed for eliciting them from the end users [26,7,4,6].

![](/api/attachments/8KUPYUN6/fulltext/images/efb43e309a0925716e1176132a8c362c7f2a3d67b116edcbeeeba0237e80e3a1.jpg)  
Fig. 3. The impact of the refresh interval on total cache value.

(a) Refresh Interval % Deviations  
![](/api/attachments/8KUPYUN6/fulltext/images/cb8a6bc877d35b1ca57d3be1b531e4e729ec107358e42e45edfbb4bc4ab2e3ed.jpg)

(b) Total Benefit % Deviations  
![](/api/attachments/8KUPYUN6/fulltext/images/0f14274676255ad611a2ef818e22ae9a388e3e9e58013d3801e17ac6b2787673.jpg)  
Fig. 4. Percentage deviations between optimal and heuristic results

## 3.3. Computational results

## 3.3.1. Model robustness

We obtained the numerical results using a desktop computer with Pentium IV CPU 3 GHz and 1 GB RAM. To find the optimal solution for a problem of sufficient size, we installed the premium Solver platform from Frontline Systems. Our experiments show that for a problem size of 499 fragments the Solver solution procedure takes on average about 10 min while the heuristic procedure takes about 5 s. Table 2 shows the baseline parameter values we used in our experiment. In selecting these parameter values, we referenced the traffic trace from a busy WWW server<sup>2</sup> and parameter choices from previous research (like [37,3]). We also set that the residual value of fragment i upon invalidation should be uniformly distributed<sup>3</sup> in [0,V ]. The decrement in the fragment value after each database update, $C _ { i } ,$ can then be calculated based on $n _ { i } , \ V _ { i } ,$ and the residual value.

For these base parameters, the total cache benefit is maximized at ${ z ^ { * } } \mathrm { = } \$ 939.1$ for the optimal refresh interval of $T ^ { * } { = } 0 . 6$ min. Fig. 3 shows how the total expected cache value changes with T. It can be seen that frequent cache refreshing (or small refresh interval $T ) ,$ while reduces fragment staleness, also reduces the net caching benefits because of the high cost associated with maintaining cache consistency. Beyond a certain threshold of refresh interval, the total cache benefits level off and then start to drop. This is due to the fact that fragments will be invalidated after a certain number of updates at the back-end database. At the optimal, a total of 194 (out of 499) fragments was cached. This is expected since in selecting fragments into the cache, small fragments (with large value of per unit storage) were favored over larger ones.

To validate the robustness of the heuristic, we define $z _ { h }$ as the percentage difference of the total expected cache benefits when problem (1) is solved both optimally and by the proposed heuristic, $T _ { h }$ the percentage difference of the refresh interval between the optimal and the heuristic solution. In other words, $z _ { h } = \frac { \left| z _ { \mathrm { h e u r i s t i c } } ^ { \star } - z _ { \mathrm { o p t i m a l } } \right| } { z _ { \mathrm { o p t i m a l } } } \mathrm { a n d } T _ { h } = \frac { \left| T _ { \mathrm { h e u r i s t i c } } - T _ { \mathrm { o p t i m a l } } \right| } { T _ { \mathrm { o p t i m a l } } }$ . Fig. 4 shows how $z _ { h }$ and $T _ { h }$ change with the cache capacity S. It is clear from this figure that the heuristic solutions in every case are very close to the optimal ones. In order to investigate the robustness further, we also identify the percentage of fragments that were left out of the cache by the heuristic (i.e., Type-I error) and the percentage of fragments that were erroneously included in the cache by the heuristic (i.e., Type-II error), when comparing with the optimal solution. At various values of S, Fig. 5 shows that these errors are within small bounds. Since we evidenced this robustness with many different choices of parameter values, we conclude that the heuristic would produce near-optimal solutions in most situations with significantly less computational time.

![](/api/attachments/8KUPYUN6/fulltext/images/132301da1bb153cf0f7a81ee56c7754d74f8b292521838722574745820bf2c11.jpg)  
Fig. 5. Type-I and Type-II errors.

(a) On Refresh Interval  
![](/api/attachments/8KUPYUN6/fulltext/images/e3d4a68351003efe3f0159ad6ca22f59dfc612f715f049ae69dbe8b43b45fddf.jpg)  
(b) On Total Cache Value

![](/api/attachments/8KUPYUN6/fulltext/images/52fcede68475dad5f10dd39c093c8c6a9e0a5a109222d726ed4885733884d03c.jpg)  
Fig. 6. Impacts of cache size.

## 3.3.2. Caching policy and sensitivity analysis

In this section, we examine how the periodic caching policy will be impacted by various model parameters, such as cache size (S), request arrival rate $( \lambda _ { i } ) ,$ , update arrival rate $( \gamma _ { i } ) .$ , and fragment invalidation (n ). Fig. 6 shows how the replacement interval and the total cache benefits would change with the cache size S. It can be seen from Fig. 6(a) that the optimal replacement interval is quite flat, implying that the replacement decision is quite robust and not very sensitive to the cache size. The total cache benefits increase with the cache size, yet at a diminishing rate.

As discussed in Section 3 that the expected value for a cached fragment increases with $V _ { i }$ and $\lambda _ { i } .$ . When the demand (or request rate $\lambda _ { i } )$ for a fragment increases, the cache should be replaced more frequently (i.e. smaller $T ^ { * } )$ so that more requests hitting the cache could get up-to-date information. Similarly, when the update rate $( \gamma _ { i } )$ increases (i.e., the cached fragments become stale faster), the cache needs to be replaced more frequently (smaller $T ^ { * } )$ to maintain its consistency with the backend database. Fig. 7 depict these effects using the same set of baseline parameter values as in Table 2.<sup>4</sup>

(a) Effect of Arrival Rate  
![](/api/attachments/8KUPYUN6/fulltext/images/a007da7077fd17825087e2b117057d8583e9da24625a61bedd7e6e072eecd70c.jpg)

(b) Effect of Update Rate  
![](/api/attachments/8KUPYUN6/fulltext/images/fd10698736297a7579bc54333e6e3a36c346764c96bd1d3464e81e695c064e9b.jpg)  
Fig. 7. Effects of arrival rate and update rate.  
(a) On Optimal Refresh Interval  
(b) On Optimal Total Cache Benefit

The effects of $n _ { i }$ on the optimal replacement interval and total cache benefits are plotted in Fig. 8. It can be seen from the figure that as fragments are more tolerant to database updates (large n ), the cache needs to be replaced less frequently (i.e. larger $T ^ { * } )$ since the cached fragments will stay valid for a longer period of time. The total cache benefits will increase because the cache replacement cost reduces while the expected fragment value increases.

Fig. 8. The impacts of fragment invalidation.  
![](/api/attachments/8KUPYUN6/fulltext/images/6f43bc87504a141cb24eb9188203210f6d5bef1c5a2978b2b72ec4622e42f2cf.jpg)

![](/api/attachments/8KUPYUN6/fulltext/images/cd9e6d03cc7b10e303ee90ca01235849bbfd84e7cee4fa2d1e12cc1f0e853b8a.jpg)

Hit ratio (HR) is a widely used performance metric for a document replacement algorithm. Hit ratio refers to the number of requests hit in the cache as a percentage of total requests. The hit ratio for the server-side cache with dynamic content depends on three factors: (i) which fragments are cached, (ii) how long the fragments could stay valid once cached, and (iii) what documents to evict from the cache once it is full. Since we adopted a periodic cache replacement policy and the caching decision is made at the beginning of each cycle, a cached fragment would not be evicted within the cycle; in other words, the hit ratio will not change within each replacement cycle. On the other hand, within each replacement cycle, the cache hit ratio depends on the duration of time before a cached fragment is invalidated. If we define $\mathrm { H R } _ { i }$ as the

## 3.3.3. Hit ratio

probability that a cached fragment i stay valid during $[ 0 , T ]$ , the hit ratio (HR) for the entire cache in the cycle can be defined as:

$$
\mathrm{HR} = \sum_ {i} y _ {i} \lambda_ {i} \mathrm{HR} _ {i} / \sum_ {i} \lambda_ {i}.
$$

Note that the above equation subsumes to the traditional hit ratio, where a cached fragment is static and never becomes invalid $( \mathrm { i . e . , H R } _ { i } { = } 1 )$ .

Let us now examine $\mathrm { H R } _ { i }$ for dynamic content. For a cached fragment i, the probability that there are j updates in [0,T] is $\operatorname* { P r } \{ j$ updates in $\begin{array} { r } { [ 0 , T ] \} = \frac { ( \gamma _ { i } T ) ^ { j } \mathrm { e } ^ { - \gamma _ { i } T } } { j ! } . \operatorname { I f } j < n _ { i } , } \end{array}$ fragment i stays valid throughout [0,T], or $\mathrm { H R } _ { i } { = } 1$ . On the other hand, if $j \geq n _ { i } ,$ the hit ratio of fragment i depends on the time t that the $n _ { i } ^ { \mathrm { t h } }$ update arrives; in other words, $\mathrm { H R } _ { i } { = } t / T .$ Since the update process is Poisson with rate $\gamma _ { i } ,$ the probability of j updates in [0,T] and the $n _ { i } ^ { \mathrm { t h } }$ update arrives at t (t < T) is given by:

![](/api/attachments/8KUPYUN6/fulltext/images/fdc5c089040c9eaca49e62667b0ecc3ad96d460e0c37388a6a91ee92ee30bacb.jpg)  
Fig. 9. The impact of S on cache choking.

Pr j updates in 0; T ; the $n _ { i } ^ { \mathrm { t h } }$ arrives at $t \}$

$$
= \frac {\gamma_ {i} ^ {j - 1} \mathrm{e} ^ {- \gamma_ {i} T} t ^ {n _ {i} - 1} (T - t) ^ {j - n _ {i}}}{(n _ {i} - 1) ! (j - n _ {i}) !}
$$

The hit ratio of fragment $i , \mathrm { H R } _ { i } ,$ can then be derived by taking expectation over j and t.

$$
\begin{array}{l} \mathrm{HR} _ {i} = \sum_ {j = 0} ^ {n _ {i} - 1} \frac {\left(\gamma_ {t} T\right) ^ {j} \mathrm{e} ^ {- \gamma_ {i} T}}{j !} \\ \quad + \sum_ {j = n _ {i}} ^ {\infty} \int_ {0} ^ {T} \frac {\gamma_ {i} ^ {j - 1} \mathrm{e} ^ {- \gamma_ {i} T} t ^ {n _ {i} - 1} (T - t) ^ {j - n _ {i}}}{(n _ {i} - 1) ! (j - n _ {i}) !} \frac {t}{T} \mathrm{d} t \\ = M _ {i} + \frac {1}{T} \sum_ {j = n _ {i}} ^ {\infty} \gamma_ {i} ^ {j - 1} \mathrm{e} ^ {- \gamma_ {i} T} \int_ {0} ^ {T} \frac {t ^ {n _ {i}} (T - t) ^ {j - n _ {i}}}{(n _ {i} - 1) ! (j - n _ {i}) !} \mathrm{d} t \\ = M _ {i} + \frac {1}{T} \int_ {0} ^ {T} \frac {t ^ {n _ {i}} \mathrm{e} ^ {- \gamma_ {i} T}}{(n _ {i} - 1) !} \sum_ {j = n _ {i}} ^ {\infty} \frac {\gamma_ {i} ^ {j - 1} (T - t) ^ {j - n _ {i}}}{(j - n _ {i}) !} \mathrm{d} t \\ = M _ {i} + \frac {1}{T} \int_ {0} ^ {T} \frac {t ^ {n _ {i}} \mathrm{e} ^ {- \gamma_ {i} T}}{(n _ {i} - 1) !} \frac {\gamma_ {i} ^ {n _ {i}} \mathrm{e} ^ {\gamma_ {i} (T - t)}}{\gamma_ {i}} \mathrm{d} t \\ = M _ {i} + \frac {1}{T \gamma_ {i}} \int_ {0} ^ {T} \frac {\left(\gamma_ {i} t\right) ^ {n _ {i}} \mathrm{e} ^ {- \gamma_ {i} t}}{(n _ {i} - 1) !} \mathrm{d} t \end{array}
$$

For the periodic cache replacement policy defined earlier, there could be requests that $\mathrm { ^ { 6 6 } h i t ^ { \circ 3 } }$ the cache for a fragment that has already been invalidated (i.e., the cached fragment no longer adds value since the copy in the cache is obsolete). We define the percentage of such requests in a replacement cycle as the cache chocking (CC). To derive the cache choking, first, the total number of requests to the cache is $\sum _ { i } y _ { i } \lambda _ { i }$ . Out of these requests, i the number of effective hits is $\textstyle \sum _ { i } y _ { i } \lambda _ { i } \mathrm { H R } _ { i }$ Hence cache choking can be computed as

$$
\mathrm{CC} = 1 - \left(\sum_ {i} y _ {i} \lambda_ {i} \mathrm{HR} _ {i} / \sum_ {i} y _ {i} \lambda_ {i}\right).
$$

Fig. 9 shows how the hit ratio and the cache choking change with S using the same baseline parameter values in Table 2. There are several observations from the figure. First, the cache hit ratio increases with the cache size. This is intuitive. Second, cache choking also rises as cache size increases. This is because more (updatesensitive) fragments will be stored in the cache as the cache becomes bigger. These fragments will be invalidated quicker, resulting in a higher percentage of fragment requests being directed to the database. Finally, the cache choking is well below the 8% level even if the cache can accommodate all the fragments, indicating that the periodic cache replacement policy is indeed effective.

## 4. Simulations

In this section, we conduct a series of simulation experiments to supplement the results obtained in the previous section. The purpose of conducting simulations is twofold. First, we would like to compare our periodic caching replacement policy with the existing document replacement algorithms, more specifically the least recently used (LRU) and the lowest relative value (LRV) algorithms. LRU is a cache replacement policy that decides on the fly which cache fragment to evict to make room for a “better fragment”. Although designed for static content, this replacement decision can also be used with dynamic content. LRV, on the other hand, evicts the fragment with the lowest relative value [33] and is suitable for caching dynamic content whose value decreases over time. Our intention here is to show the improvement of using an optimal periodic replacement vs. myopic ones (such as LRU and LRV) in the context of database-driven dynamic content. The second purpose of conducting simulations is that we would like to study how the model performs when the fragment request and update arrivals deviate from a Poisson process, i.e. the inter-arrival times for requests and updates do not follow an exponential distribution. We simulate the request arrival process and update process for the 499 fragments using discrete-event simulation. All the experiments were coded in C++ and carried out on a Pentium IV computer (with 3 GHz CPU and 1 GB RAM), with Windows XP OS. For each problem instance, we ran simulation experiments for 100,000 iterations, each of which representing a sufficiently long period of time. The total cache benefits (per unit time) and the hit ratio were computed by averaging over the total number of iterations.

To simulate the LRU (LRV) algorithm, we use the same parameter values for the fragments as that in

Table 2. Rather than periodically replacing the cached fragments, the LRU policy chooses to evict the least recently used fragment while the LRV policy evicts the fragment with the lowest relative value once the cache is full. Fig. 10 shows the total expected cache value (per unit time) and the hit ratio for the three policies by varying the cache size. It can be seen that the periodic replacement policy outperforms (in terms of higher cache benefits and hit ratio) both the LRU and the LRV policies, which are quite close to each other. As expected, the cache accrues more benefits under LRV than that under LRU.

In order to see how the periodic cache replacement policy performs if the request and update arrivals deviate from Poisson process, we considered several arrival processes with non-exponential distributions for inter-arrival times. In choosing these distributions, we ensured that the distribution had the same mean as the original exponential distribution (see the Appendix for the details of these distributions).

For each distribution, we choose the optimal cache replacement interval $T ^ { * }$ as derived from Eq. (1) and ran simulation experiments to observe the per unit time cache benefits z and the cache hit ratio HR. The cache benefits and hit ratio were then compared to the analytical results obtained under Poisson assumption.

(a)  
![](/api/attachments/8KUPYUN6/fulltext/images/7125720930a70d93dcc2adbc384ceb2fae5214891631b947532bf2d37cc4d5e9.jpg)

(b)  
![](/api/attachments/8KUPYUN6/fulltext/images/781887d89c6d5430f4be1358b91391ec8af501e72b15973649499578e40cadcd.jpg)  
Fig. 10. Comparison of periodic, LRU, and LRV policies.

(a)  
![](/api/attachments/8KUPYUN6/fulltext/images/2b8bd10bd881d7e5a7fd14c44ae6fb4e4e4f4c4514fbbbe187c3c2a90bb3b8ea.jpg)

(b)  
![](/api/attachments/8KUPYUN6/fulltext/images/850406cbfb514d035b94896f70bb49d48d3df77f39bf801d44c4a9bbddcdd4a4.jpg)  
Fig. 11. Cash benefits and hit ratio for different distributions of interarrival times operating under the replacement interval obtained in Eq. (1).

Fig. 11 provides the results of these experiments. It can be seen from the figure that the per-time-unit cache benefit as well as the cache hit ratio in every case was very close to the analytical results. We evidenced this robustness with many different choices of parameter values; hence it appears that Poisson assumption would work well in most situations.

## 5. Discussions and concluding remarks

Web applications that support dynamic content have become prevalent over the last few years, necessitating good solutions for the management of cache with dynamic contents. One of the main challenges of dynamic web fragment caching is the volatility of the content. To address this issue, we propose a periodic cache replacement policy that tradeoff the benefits of serving slight stale fragment from the cache against the cost of maintaining cache consistency to obtain what fragments should be placed in the cache to derive the optimal interval when the cache needs to be replaced. We develop fast and accurate heuristic procedures for the optimization problem. We also examine the validity of the model and compare the proposed policy to the popular LRU and LRV algorithms by designing appropriate simulation experiments. Results from the experiments show that the periodic cache replacement policy is robustness and effectiveness in handling dynamic content.

It should be noted that, while we assume the application cache stores only the materialized views of database queries in our model, the analyses presented in this paper also apply to a more general situation in which cache entries can be a larger page fragment [3] consisting of multiple query results as well as presentation/formatting information. Furthermore, it is possible to extend the concept of server-side caching to the management of edge and proxy caches, as proposed by [16]. Since the edge servers provide further reduction in the transmission cost while incurring higher consistency costs with the main server, the inclusion of the edge server cache provides further flexibility as to where a page fragment should be placed.

There are several possible extensions from the current research. One direction is to incorporate the recency of requests in the value-based optimization model. Under the new setup, two events could trigger the cache replacement: either the elapsed time has reached the prescribed $T ^ { * }$ , or there has been a noticeable shift in page demand patterns. Another interesting direction will be to relax the assumption, which allows a fragment to be served from the cache even though it becomes invalid. A possible and realistic extension is to replace the individual fragment immediately rather than waiting for the whole cache is replaced.

## Acknowledgement

Partial support for this work was provided by TECI — Treibick Electronic Commerce Initiative at the Operations and Information Management Department−University of Connecticut.

## Appendix A

Proof of Proposition 1. Since ${ \frac { \mathrm { d } \mathrm { E V } _ { i } ( T ) } { \mathrm { d } t } } = \lambda _ { i } V _ { i } \sum _ { k = 0 } ^ { n _ { i } - 1 } \ { \frac { ( \gamma _ { i } T ) ^ { k } \mathrm { e } ^ { - \gamma _ { i } T } } { k ! } }$ $\begin{array} { r } { \lambda _ { i } C _ { i } \sum _ { k = 1 } ^ { n _ { i } - 1 } \frac { ( \gamma _ { i } T ) ^ { k } \mathrm { e } ^ { - \gamma _ { i } T } } { ( k - 1 ) ! } , } \end{array}$ we can obtain $\mathrm { E V } _ { i } ( T )$ by integrating both sides and recognizing that $\mathrm { E V } _ { i } ( 0 ) { = } 0 \mathrm { : }$

$$
\begin{array}{l} \mathrm{EV} _ {i} (T) = \lambda_ {i} V _ {i} \sum_ {k = 0} ^ {n _ {i} - 1} \frac {\gamma_ {i} ^ {k}}{k !} \int_ {0} ^ {T} t ^ {k} \mathrm{e} ^ {- \gamma_ {i} T} \mathrm{d} t - \lambda_ {i} C _ {i} \gamma_ {i} \sum_ {k = 0} ^ {n _ {i} - 2} \frac {\gamma_ {i} ^ {k}}{k !} \\ \times \int_ {0} ^ {T} t ^ {k + 1} \mathrm{e} ^ {- \gamma_ {i} T} \mathrm{d} t. \end{array}
$$

It can be shown that $\int _ { 0 } ^ { T } t ^ { k } \mathrm { e } ^ { - \gamma _ { i } T } \mathrm { d } t = \frac { k ! } { \gamma _ { i } ^ { k + 1 } } - \mathrm { e } ^ { - \gamma _ { i } T } \sum _ { j = 0 } ^ { k } \frac { k ! } { j ! }$ $\frac { T ^ { j } } { \gamma _ { i } ^ { k - j + 1 } }$ g. Substituting it back to the above equation, we get

$$
\begin{array}{l} \mathrm{EV} _ {i} (T) = \lambda_ {i} V _ {i} \sum_ {k = 0} ^ {n _ {i} - 1} \frac {\gamma_ {i} ^ {k}}{k !} \left(\frac {k !}{\gamma_ {i} ^ {k + 1}} - \mathrm{e} ^ {- \gamma_ {i} T} \sum_ {j = 0} ^ {k} \frac {k !}{j !} \frac {T ^ {j}}{\gamma_ {i} ^ {k - j + 1}}\right) \\ \qquad - \lambda_ {i} C _ {i} \gamma_ {i} \sum_ {k = 0} ^ {n _ {i} - 2} \frac {\gamma_ {i} ^ {k}}{k !} \left(\frac {(k + 1) !}{\gamma_ {i} ^ {k + 2}} - \mathrm{e} ^ {- \gamma_ {i} T} \sum_ {j = 0} ^ {k + 1} \frac {(k + 1) !}{j !} \frac {T ^ {j}}{\gamma_ {i} ^ {k - j + 2}}\right) \\ = \frac {\lambda_ {i} V _ {i} n _ {i}}{\gamma_ {i}} - \frac {\lambda_ {i} C _ {i}}{\gamma_ {i}} \frac {n _ {i} (n _ {i} - 1)}{2} - \frac {\lambda_ {i} V _ {i}}{\gamma_ {i}} \sum_ {k = 0} ^ {n _ {i} - 1} \sum_ {j = 0} ^ {k} \frac {(\gamma_ {i} T) ^ {j} \mathrm{e} ^ {- \gamma_ {i} T}}{j !} \\ \qquad + \frac {\lambda_ {i} C _ {i}}{\gamma_ {i}} \sum_ {k = 0} ^ {n _ {i} - 2} \sum_ {j = 0} ^ {k + 1} (k + 1) \frac {(\gamma_ {i} T) ^ {j} \mathrm{e} ^ {- \gamma_ {i} T}}{j !} \\ = \frac {\lambda_ {i} V _ {i} n _ {i}}{\gamma_ {i}} - \frac {\lambda_ {i} C _ {i}}{\gamma_ {i}} \frac {n _ {i} (n _ {i} - 1)}{2} - \frac {\lambda_ {i} V _ {i}}{\gamma_ {i}} \left[ n _ {i} \sum_ {j = 0} ^ {n _ {i} - 1} \frac {(\gamma_ {i} T) ^ {j} \mathrm{e} ^ {- \gamma_ {i} T}}{j !} \right. \\ \qquad - \sum_ {j = 1} ^ {n _ {i} - 1} \frac {(\gamma_ {i} T) ^ {j} \mathrm{e} ^ {- \gamma_ {i} T}}{(j - 1) !} ] + \frac {\lambda_ {i} C _ {i}}{\gamma_ {i}} \sum_ {j = 0} ^ {n _ {i} - 1} \frac {(\gamma_ {i} T) ^ {j} \mathrm{e} ^ {- \gamma_ {i} T}}{j !} \\ \qquad \times \frac {(n _ {i} - j) (n _ {i} + j - 1)}{2} = \frac {\lambda_ {i} V _ {i n _ {i}}}{\gamma_ {i}} - \frac {\lambda_ {i} C _ {i}}{\gamma_ {i}} \frac {n _ {i} (n _ {i} - 1)}{2} \\ \qquad - \frac {\lambda_ {i} V _ {i}}{\gamma_ {i}} \left[ n _ {i} M _ {i} - \gamma_ {i} T \left(M _ {i} - \frac {\left(\gamma_ {i} T\right) ^ {n _ {i} - 1} \mathrm{e} ^ {- \gamma_ {i} T}}{(n _ {i} - 1) !}\right) \right] \\ \qquad + \frac {\lambda_ {i} C _ {i}}{2 \gamma_ {i}} (n _ {i} ^ {2} - n _ {i}) M _ {i} - \frac {\lambda_ {i} C _ {i}}{2 \gamma_ {i}} \sum_ {j = 2} ^ {n _ {i} - 1} \frac {\left(\gamma_ {i} T\right) ^ {j} \mathrm{e} ^ {- \gamma_ {i} T}}{(j - 2) !} \\ = \frac {\lambda_ {i} V _ {i n _ {i}}}{\gamma_ {i}} - \frac {\lambda_ {i} C _ {i}}{\gamma_ {i}} \frac {n _ {i} (n _ {i} - 1)}{2} - \frac {\lambda_ {i} V _ {i}}{\gamma_ {i}} \\ \qquad \times \left[ n _ {i} M _ {i} - \gamma_ {i} T M _ {i} + \frac {\left(\gamma_ {i} T\right) ^ {n _ {i}} \mathrm{e} ^ {- \gamma_ {i} T}}{(n _ {i} - 1) !} \right] \\ \qquad + \frac {\lambda_ {i} C _ {i}}{2 \gamma_ {i}} (n _ {i} ^ {2} - n _ {i}) M _ {i} - \frac {\lambda_ {i} C _ {i}}{2} (\gamma_ {\mathrm{i}} T ^ {\mathrm{d}} \\ \qquad \times \left[ M _ {\mathrm{i}} - \frac {\left(\gamma_ {\mathrm{i}} T\right) ^ {{n _ {\mathrm{i}}} - 2} e ^ {- \gamma_ {\mathrm{i}} T}}{{(n _ {\mathrm{i}} - 2) !}} - \frac {\left(\gamma_ {\mathrm{i}} T\right) ^ {{n _ {\mathrm{i}}} - 1} e ^ {- \gamma_ {\mathrm{i}} T}}{{(n _ {\mathrm{i}} - 1) !}} \right] \end{array}
$$

Simplifying the above equation and collecting terms, we get

$$
\begin{array}{l} \mathrm{EV} _ {i} (T) = \lambda_ {i} V _ {i} T M _ {i} + \frac {\lambda_ {i} n _ {i}}{\gamma_ {i}} \left[ V _ {i} + \frac {C _ {i}}{2} (1 - n _ {i}) \right] \\ \left[ 1 - M _ {i} - \frac {\gamma_ {i} ^ {n _ {i}} T ^ {n _ {i}} \mathrm{e} ^ {- \gamma_ {i} T}}{n _ {i} !} \right] - \frac {\lambda_ {i} \gamma_ {i} C _ {i}}{2} T ^ {2} \\ \left[ M _ {i} - \frac {\gamma_ {i} ^ {n _ {i} - 1} T ^ {n _ {i} - 1} \mathrm{e} ^ {- \gamma_ {i} T}}{(n _ {i} - 1) !} \right]. \end{array}
$$

## A.1. Distributions used in simulation experiments

We discuss the various distributions of inter-arrival times used in the simulation experiments described in Section 4 of the paper.

## A.1.1. Exponential distribution

To obtain an exponential random variable x with rate $\lambda ,$ we generated a uniform random number $\mu \in [ 0 , 1 ]$ and set $x \overset { \mathbf { \tilde { \mathbf { \theta } } } } { = } - \frac { \ln ( \mu ) } { \lambda }$ . The coefficient of variation (CV = mean / standard deviation) of x is 1.

## A.1.2. Lognormal distribution

If a random variable Z follows the normal distribution with mean $\mu$ and variance $\sigma ^ { 2 }$ , then a random variable $\scriptstyle x = e _ { , } ^ { Z }$ is said to have a lognormal distribution, with mean $\mathrm { e } ^ { \mu + \frac { \sigma ^ { \angle } } { 2 } }$ and variance $\mathrm { e } ^ { 2 \mu + 2 \sigma ^ { 2 } } - \mathrm { e } ^ { 2 \mu + \sigma ^ { 2 } }$ . Given two uniform random numbers $\mu _ { 1 }$ and $\mu _ { 2 }$ in $[ 0 , 1 ]$ , a standard normal random variable z can be generated by using the Box– Muller transformation $[ 3 4 ] \colon z = { \sqrt { - 2 \ln \mu _ { 1 } \cos ( 2 \pi \mu _ { 2 } ) } }$ . A normal variable $Z ( \mu , \sigma ^ { 2 } )$ <sup>¼</sup>can then be obtained from $Z { = } \mu { + } \sigma z$ , which can, in turn, be used to generate the lognormal variable $\displaystyle x = e ^ { Z } .$ . In our experiments, to keep the rate at $\lambda ,$ we set $\mu = - \mathrm { l n } ( \lambda \sqrt { 2 } )$ and $\sigma ^ { 2 } { = } \ln 2$ , so that the CV of x was 1.

## A.1.3. Pareto distribution

A random variable x following the Pareto distribution has the following cumulative distribution function [27]:

$$
F (x) = 1 - \left(\frac {\gamma}{x}\right) ^ {\theta}, \text { where } \gamma , \theta > 0.
$$

After drawing a uniform random number $\mu \in [ 0 , 1 ]$ we can generate a Pareto random variable x by setting $x = \gamma ( 1 { - } u ) ^ { - ( \frac { 1 } { \theta } ) }$ . In our experiments, we set $\begin{array} { r } { \gamma = \frac { 1 } { \lambda } \frac { \sqrt { 2 } } { 1 + \sqrt { 2 } } } \end{array}$ <sup>¼</sup>and $\theta = 1 + \sqrt { 2 }$ <sup>g ¼</sup>in order to keep the rate at λ and $\mathrm { C V } { \overset { ! } { = } } 1 .$

## A.1.4. Uniform distribution

After drawing a uniform random number $\mu \in [ 0 , 1 ]$ , a uniform random variable x with rate λ can be obtained by setting $x = \frac { 2 \mu } { \lambda }$ The CV of x is ${ \frac { 1 } { \sqrt { 3 } } } .$

## References

[1] M. Abrams, C. Standbridge, G. Abdulla, S. Williams, E. Fox, Caching proxies: limitations and potentials, Proceedings of the 4th WWW Conference, 1995, Boston, MA.

[2] C. Aggarwal, J.L. Wolf, P.S. Yu, Caching on the World Wide Web, IEEE Transactions on Knowledge and Data Engineering 11 (1) (1999) 94–107.

[3] J. Anton, L. Jacobs, X. Liu, J. Parker, Z. Zeng, T. Zhong, Web Caching for Database Applications with Oracle Web Cache, ACM SIGMOD, June 2002.

[4] Y.M. Babad, A.N. Saharia, Use of stale answers in database applications, Proceedings of International Conference on Information Systems, December 1992, pp. 233–239, Dallas, TX.

[5] B. Baccala, Standardized caching of dynamic web content, Internet Engineering Task Force (IEFT), March 2003 Available at: http://www.freesoft.org.

[6] D.P. Ballou, H.L. Pazer, Designing information systems to optimize the accuracy-timeliness tradeoff, Information Systems Research 6 (1995) 51–72.

[7] D.P. Ballou, G.K. Tayi, Methodology for allocating resources for data quality enhancement, Communications of the ACM 32 (1989) 320–329.

[8] BEA Systems, WebLogic Application Server, , 2003 available at: http://www.bea.com/products/weblogic/index.html.

[9] A. Bestavros, Using speculation to reduce server load and service time on the WWW, Proceedings of the International Conference on Information and Knowledge Management, 1995, pp. 403–410, Baltimore, MD.

[10] F. Bonchi, F. Gianotti, G. Manco, C. Renso, M. Nanni, D. Pedreschi, S. Ruggieri, Data mining for intelligent web caching, International Conference on Information Technology: Coding and Computing, April 2001, Las Vegas, NV.

[11] K. Candan, W. Li, Q. Luo, W. Hsiung, D. Agrawal, Enabling Dynamic Content Caching for Database-Driven Web Sites, ACM SIGMOD, 2001.

[12] P. Cao, S. Irani, Cost-aware WWW proxy caching algorithms, Proceedings of the USENIX Symposium on Internet Technologies and Systems, 1997, Monterey, CA.

[13] A. Cate, Alex-a global file system, Proceedings of the USENIX File System Workshop, 1992, pp. 1–11, Ann Arbor, MI.

[14] C. Chen, The Last-Mover Advantage, Fortune, July 9 2001.

[15] A. Datta, K. Dutta, H. Thomas, D. VanderMeer, World Wide Wait: a study of Internet scalability and cache-based approaches to alleviate it, Management Science 49 (10) (2003) 1425–1444.

[16] A. Datta, K. Dutta, H. Thomas, D. VanderMeer, K. Ramamritham, Proxy-based acceleration of dynamically generated content on the World Wide Web: an approach and implementation, Proceedings of the ACM SIGMOD International Conference on Management of Data, 2002, pp. 96–108, Madison, WI.

[17] D. Dey, Z. Zhang, P. De, Optimal synchronization policies for data warehouses, INFORMS Journal on Computing 18 (2) (2006) 229–242.

[18] ETrade, Introducing 2-second Execution Guarantee, 2004 available at: https://us.etrade.com/e/t/home.

[19] A. Feldmann, R. Caceres, F. Douglis, G. Glass, M. Rabinovich, Performance of web proxy caching in heterogeneous bandwidth environments, Proceedings of INFOCOM, 1999, pp. 107–116.

[20] P. Fox, Dynamic web pages prepared for takeoff, Computerworld 36 (2) (January 7 2002) 46.

[21] J. Han, M. Kamber, Data Mining: Concepts and Techniques, Morgan Kauffman, San Mateo, 2000.

[22] A. Iyergar, J. Challenger, Improving web server performance by caching dynamic data, Proceedings of the USENIX Symposium on Internet Technologies and Systems, 1997, Monterey, CA.

[23] S. Jin, A. Bestavros, GreedyDual\* web caching algorithm: exploiting the two sources of temporal locality in web request streams, International Journal on Computer Communications 24 (2) (February 2001) 174–183.

[24] A. Labrinidis, N. Roussopoulos, Web view materialization, Proceedings of the ACM SIGMOD International Conference of Management of Data, May 2000, Dallas, Texas.

[25] C. Liu, P. Cao, Maintaining strong cache consistency in the World Wide Web, IEEE Transactions on Computers 47 (4) (1998) 445–457.

[26] H. Mendelson, A.N. Saharia, Incomplete information costs and database design, ACM Transactions on Database Systems 11 (1986) 159–185.

[27] A.M. Mood, F.A. Graybill, D.C. Boes, Introduction to the Theory of Statistics, McGraw-Hall, NY, 1974.

[28] V. Mookerjee, Y. Tan, Analysis of a least recently used cache management policy for web browsers, Operations Research 50 (2) (2002) 345–357.

[29] Nua Internet Surveys, How many online? Nua Internet Surveys, 2003 available at: http://www.nua.com/surveys/how\_many\_online.

[30] Oracle, Caching in on the enterprise grid: turbo-charge your applications with OracleAS web cache, Oracle White Paper, 2003 available at: http://www.oracle.com/technology/products ias/web\_cache/pdf/WebCache1012\_t wp.pdf.

[31] V. Padmanabhan, J. Mogul, Using predictive prefetching to improve the World Wide Web latency, Proceedings of ACM SIGCOMM'96, 1996, Stanford, CA.

[32] M. Rabinovich, O. Spatscheck, Web Caching and Replication, Addison Wesley, 2002.

[33] L. Rizzo, L. Vicisano, Replacement policies for a proxy cache, IEEE/ACM Transactions on Networking 8 (2) (2000) 158–170.

[34] S. Ross, Simulation, Academic Press, San Diego, CA, 1997.

[35] J. Shenton, Shopping cart abandonment, Global Millennia Marketing, April 2002 available at: http://www.globalmillenniamarketing. com.

[36] Z. Wang, J. Crowcroft, Prefetching in World Wide Web, Proceeding of the Global Internet Symposium, 1996.

[37] E.F. Watson, Y. Shi, Y. Chen, A user-access model-driven approach to proxy cache performance analysis, Decision Support Systems 25 (1999) 309–338.

[38] S. Williams, M. Abrams, C. Standbridge, G. Abdulla, E. Fox, Removal policies in network caches for World Wide Web documents, Proceedings of ACM SIGCOMM'96, 1996, pp. 293–305, Stanford, CA.

[39] J.W. Wong, D. Evans, M. Kwok, On staleness and the delivery of web pages, Information Systems Frontiers 5 (2) (2003) 129–136.

[40] N. Young, The K-server loose and competitiveness for paging, Algorithmica 11 (6) (1994) 525–541.

I. Robert Chiang is a senior consultant at Accenture a leading program office for large-scale client engagements. His research interests are in software project management, information systems economics, and electronic commerce design. In addition to DSS, he has articles which appeared or are forthcoming in IEEE, INFORMS, and ACM publications.

![](/api/attachments/8KUPYUN6/fulltext/images/42d4296d399b366c39da76f43e1202d9f72c4eeb81371b9ffd7f9d680a25fb74.jpg)

Paulo B. Goes is the Gladstein Professor of Information Technology and Innovation at the School of Business of the University of Connecticut. He received his PhD from the University of Rochester. His research interests are in the areas of design and evaluation of models for e-business, emerging technologies, online auctions, database technology and systems, and technology infrastructure. His research has appeared in several journals including Management Science, MISQ, ISR,

Journal of MIS, Operations Research, INFORMS Journal on Computing, IEEE Transactions on Communications, IEEE Transactions on Computers. Dr. Goes is Senior Editor of Information Systems Research, and Associate Editor of Management Science, Decision Sciences, Journal of Management Information Systems, and the INFORMS Journal on Computing. In 2004 he co-chaired WITS, the Workshop on Information Technology and Systems, and was recently elected the WITS Organization President. He is the co-founder and director of CIDRIS, a research center dedicated to research with Internet data.

![](/api/attachments/8KUPYUN6/fulltext/images/549ddda64bb39dc9d255b4a599a9c8814bc63b91c88729d2972a0db7a007a86e.jpg)

Zhongju Zhang is an Assistant Professor at the Operations and Information Management Department, University of Connecticut. He holds a PhD in Information Systems from the University of Washington. Zhang's main research interests include e-business/e-commerce, economics of information systems/ technologies, online communities, technology adoption/diffusion, data warehousing and data mining. His research has been published in INFORMS Journal on Computing, European

Journal of Operational Research, International Journal on Human Computer Studies, Decision Support Systems, Communications of the ACM, Electronic Commerce Research and Applications, as well as in leading international conference proceedings. He currently serves on the editorial board of the Journal of Database Management.
