---
otero_id: 14480
otero_key: "VGQ6EZRA"
title: "An admission-control technique for delay reduction in proxy caching"
authors: "Cuneyd C. Kaya; Guoying Zhang; Yong Tan; Vijay S. Mookerjee"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.10.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An admission-control technique for delay reduction in proxy caching

Cuneyd C. Kaya <sup>a</sup>, Guoying Zhang <sup>b</sup>, Yong Tan <sup>c,</sup>⁎, Vijay S. Mookerjee <sup>a</sup>

<sup>a</sup> School of Management, University of Texas at Dallas, Richardson, TX 75080, United States

<sup>b</sup> Dillard College of Business Administration, Midwestern State University, Wichita Falls, TX 76308-2099, United States

<sup>c</sup> Michael G. Foster School of Business, University of Washington, Seattle, WA 98195-3200, United States

## a r t i c l e i n f o

Article history: Received 5 April 2007 Received in revised form 17 October 2008 Accepted 27 October 2008 Available online 3 November 2008

Keywords: Cache management Proxy caching Admission control Screening Delay reduction Download traf<sup>fi</sup>c

## a b s t r a c t

We evaluate an admission-control (screening) policy for proxy server caching that augments the LRU (Least Recently Used) algorithm. Our results are useful for operating a proxy server deployed by an Internet Service Provider or for an enterprise (forward) proxy server through which employees browse the Internet. The admission-control policy classi<sup>fi</sup>es documents as cacheable and non-cacheable based on loading times and then uses LRU to operate the cache. The mathematical analysis of the admission control approach is particularly challenging because it considers the dynamics of the caching policy (LRU) operating at the proxy server. Our results show substantial reduction (around 50% in our numerical simulations) in user delay. The improvement can be even larger at high levels of proxy server capacity or when the user demand patterns are more random. An approximation technique provides near optimal results for large problem sizes demonstrating that our approach can be used in real-world situations. We also show that the traf<sup>fi</sup>c downloaded by the proxy server does not change much (as compared to LRU) as a result of screening. A detailed simulation study on LRU and other caching algorithms validate the theoretical results and provide additional insights. Furthermore, we have provided ways to estimate policy parameter values using real world trace data.

© 2008 Elsevier B.V. All rights reserved

## 1. Introduction

The last few years have witnessed a tremendous growth in the amount of information available on the World Wide Web. In addition to personal computer access, there is also an increase in the variety of devices (such as mobile phones, Personal Digital Assistants, etc.), being used to retrieve information from the World Wide Web. As the proliferation of the internet continues, it is important that users continue to get acceptable performance while using the Web. However, although network and server capacities have dramatically increased over the past several years, the emergence of bandwidth hungry applications such as video, audio on demand and distributed games has made the demand for performance even greater.

Previous studies show that the estimated monetary loss to ecommerce <sup>fi</sup>rms from slow response times exceeded \$4 billion in 2001 [42] and in 2000 Christmas shopping season alone, e-tailers' loss was estimated at \$14 billion [17]. The amount of time it takes to view a web page has been shown to be a signi<sup>fi</sup>cant factor in determining the success of a site as well as the satisfaction of its users. Reducing delays can have substantial economic impacts. For example, decreasing the loading time of an electronic retailer's home page by one second reduced the rate of visitors abandoning the web page from 30% to 8% [42].

Web caching (among other technologies) addresses issues of capacity and performance and has become an integral part of the Web infrastructure [20,31]. When a user requests a document, it may have to be fetched from a remote server and loaded on the user's computer. While the document is being fetched, the user often waits without doing anything productive. Most users do not like to wait much for a document and long response times often lead to user frustration and eventual termination of use [24,40]. Web caching can take place at different locations; $\mathrm { e . g . }$ , at the user's browser, at a proxy server, etc. [27]. Browser caching is carried out by commercial software with built-in caching capabilities, while proxy caching is done by specialized caching algorithms run at proxy servers implemented at the Points of Presence (POP) of an Internet Service Provider (ISP) or at the edge of an enterprise network.

This study deals with improving the caching performance of a proxy server placed at the edge of an (ISP or enterprise) network. Proxy caching has two main purposes. First, it reduces user delay by caching popular documents at the proxy server. Second, proxy caching can reduce the traf<sup>fi</sup>c generated by the proxy server when downloading from documents' original servers (or simply download traf<sup>fi</sup>c by proxy server, $D _ { \mathsf { p } } )$ and lower the associated bandwidth costs. Proxy servers have non-caching bene<sup>fi</sup>ts as well, e.g., they prevent users in the enterprise networks to access to sites, such as online games and entertainment websites, which are not related to the business, thus preventing reduced productivity [31].

![](/api/attachments/VGQ6EZRA/fulltext/images/ef7467ec36bc13085293df60b75b7169df65e650e635e6dfdeef7bdca3254a78.jpg)  
Fig. 1. Model setting.

Fig. 1 shows the basic setting for our model. An ISP (or an enterprise network) implements a proxy server that keeps an up-todate copy of popular web documents in its cache. When a user requests a cached document the request can directly be served from the proxy cache. Otherwise, the proxy server downloads the document from the origin server using an outgoing communication link.

The goal of this paper is to improve proxy caching performance (in terms of reducing end user delay). A secondary measure of performance is the amount of download traf<sup>fi</sup>c $( D _ { \mathrm { p } } )$ by the proxy server. This measure is important because the amount of download traf<sup>fi</sup>c can affect the cost of operating the outgoing link. Our experiments show that the admission control (screening) technique proposed here can substantially reduce end user delay while holding the download traf<sup>fi</sup>c $( D _ { \mathrm { p } } )$ at about the same level.

Most existing research on proxy caching uses the LRU policy;<sup>1</sup> for example, the popular Squid proxy cache software uses a minor variation of LRU [15,30]. One limitation of the LRU algorithm is that it ignores the loading time (the time taken to fetch the document from the origin server) of documents. Intuitively speaking, the bene<sup>fi</sup>t from caching is most when a document with high loading time is requested and can be supplied from the cache. Our approach improves LRU performance by screening out documents (i.e., deeming these documents non-cacheable) with relatively low loading times.

## 1.1. Contributions of the study

First, we provide a precise way to screen documents. This is done by deriving an exact mathematical expression for performance (average delay per request) under screening. Using this delay expression, we <sup>fi</sup>nd the optimal extent of screening so as to minimize delay. Second, we <sup>fi</sup>nd an approximation for the delay expression and derive a closed form expression for the optimal (with respect to the approximation) extent of screening. The approximation technique is particularly useful when there are a large number of documents that can be potentially accessed by the user. Third, we conduct a variety of numerical experiments that show signi<sup>fi</sup>cant improvement over basic LRU that can be achieved by screening without a signi<sup>fi</sup>cant change in the download traffic $( D _ { \mathrm { p } } ) .$ We also study the bene<sup>fi</sup>t of screening for other proxy caching algorithms such as Latency estimation algorithm (LAT) [40] and Greedy Dual Size (GD-Size) [8]. Finally, we conduct a simulation study as well as an experiment with real web trace data to validate the theoretical results obtained in the paper.

## 1.2. Summary of results

The main result of this paper is that screening can offer substantial bene<sup>fi</sup>ts (in terms of delay) over the basic LRU policy. These bene<sup>fi</sup>ts are especially high if the proxy server's cache capacity is high or if the user demand for documents is more random unless the capacity is low. Another useful result is that the optimal screening threshold can be extremely accurately approximated by a simple formula using parameters of the problem that are typically easy to obtain. The approximation formula is particularly useful when there are thousands or even hundreds of thousands of documents that can potentially be requested by users. We also demonstrate that the delay reducing bene<sup>fi</sup>ts of screening do not come at the cost of additional download traf<sup>fi</sup>c on the outgoing link. Similar improvements are observed for other caching algorithms, such as LAT and GD-Size.

The paper is organized as follows. In Section 2 we review related literature on Web caching. In Section 3, we present and analyze the screening policy. A series of numerical experiments are conducted to study its properties. Section 4 describes a simulation study to validate the theoretical results. In Section 5, we propose methods to estimate parameters using real-world web trace data. Section 6 summarizes and concludes the paper.

## 2. Related work

The literature on Web caching is vast. Barish and Obraczke [6] discuss several caching architectures and deployment options. Caches can be deployed near the consumer (in the case of browser caching or proxy caching), near the content provider (in the case of web server caching) or at a point in the middle (in the case of proxy caching) depending on the network topology and conditions. In our study, proxy server is placed at the edge of the network (ISP or enterprise network) that the user belongs to. Podlipnig and Bözsörmenyi [30] provide a detailed survey on caching algorithms for the World Wide Web. Datta et al. [14] identify the problems on the web that cause delays and review various caching strategies to ease them. Scaling issues also attracted attention. A scalable website is the one that can serve enough requests even under high workloads. Menascé [25] describes a caching solution on the web server itself that will provide some level of scaling. Challenger et al. [9] provide a scalable system for caching dynamic web data. Fagni et al. [16] proposes a caching strategy that extracts from historical usage data the results of the most frequently submitted web queries and stores them in a static, readonly portion of the cache. The remaining entries of the cache are dynamically managed according to a given replacement policy. More recently, Chiang et al. [12] propose a periodic cache replacement policy to handle increasingly dynamic content on the Web. The heuristic approach in their study addresses the decision problems of how frequently a cache should be replaced and which dynamic fragments should be selected to the cache.

Our focus is on the Least Recently Used (LRU) algorithm as well as its variations and its limitations. The LRU algorithm (and its variants) is one of the most popular methods used in proxy caching [4]. Mookerjee and Tan [27] derive mathematical expressions to estimate expected latency. Jelenkovic and Radovanovic [18] provide an explicit average-case analysis of LRU caching with statistically dependent request sequences. The surprising insensitivity of LRU caching performance demonstrates its robustness to changes in document popularity.

LRU's variants mainly consist of paying attention to document size, in addition to the recency based priority given to a document by the basic LRU policy. Dilley et al. [15] improve the replacement policy in Squid (a prominent proxy cache implementation) with LFU-DA (Least Frequently Used-Dynamic Aging), and GDS-Hits (Greedy Dual Size-Hits) algorithms. LFU-DA and LFU-Age policies introduce an aging factor in the basic LFU policy in order to reduce cache pollution [2]. Abrams et al. [1] enhance LRU by introducing the LRU-Threshold and LRU-MIN policies. LRU-Threshold is a size and recency-based strategy that only caches documents no larger than a threshold size. Within the cache, replacements occur based on LRU policy. LRU-MIN tries to minimize the number of documents replaced by replacing larger documents before smaller ones. Murta et al. [28] divide the cache into several partitions with different sizes and each partition is operated based on LRU. Documents of similar size are placed in the same partition. This partitioning strategy reduces size heterogeneity, and hence documents of very different sizes are not likely to compete with one other for space in cache. Another improvement on LRU is Segmented LRU [3]. Here the cache is divided into two segments: an unprotected segment and a protected segment. Both segments use the basic LRU policy for replacement. Once a document in the cache is hit, it is moved to the protected segment. A document cannot be removed from the cache if it is in the protected segment, however, it may be moved to the unprotected segment and evicted from the cache from there, if necessary. Other improvements to LRU include using a usage frequency count to prioritize documents, for example, Generational Replacement [29] and LRU⁎ [10]; a document popularity metric such as LRU-Hot [26]); and size based priority LRU-SP [11]. Kumar and Norris [22] propose a proxy caching mechanism that takes into consideration of aggregate user request pattern. Both the historical request pattern and current dynamic request pattern are incorporated in their optimization model. Kumar et al. [21] implement a prototype of an online analytical processing system for mobile devices. The prototype utilizes multi-layered caching techniques to improve the performance.

Reddy and Fletcher [32] improve the existing algorithms by an adaptive technique that uses document life histories to optimize the cache performance. By using the age notion, they also suggest that LRU is capable of estimating the future demand on a document although this may not be optimal. Juurlink [19] presents a replacement policy that predicts the time each page will be referenced again and evicts the page that has the largest predicted time of next reference. Usually, client browsers cache some content as their default settings. This causes the same document to be cached by both the browser and the proxy server. Tan et al. [37] study the duplication effects on browser and proxy caching. They provide an exact expression for the optimal level of duplication between a set of browsers and a proxy server. The results show that the level of duplication should be controlled when the content being cached is volatile.

There is a limited amount of recent work on introducing document delay into the operation of the basic LRU policy. Most of this work is based on simulation and modi<sup>fi</sup>es the basic LRU policy. For example, Watson et al. [39] present an empirically derived model of Web useraccess activity, which can be used to conduct model-driven simulation studies of cache performance analysis. Scheuermann et al. [34] provide a delay-conscious caching algorithm where a pro<sup>fi</sup>t metric is used to calculate the bene<sup>fi</sup>t of retrieving the document from the cache rather than retrieving from the original server. Shin et al. [36] introduce the algorithm LRU-SLFR, LRU-based small latency <sup>fi</sup>rst replacement, which combines LRU policy with real latency to achieve the best overall performance. LRU-SLFR algorithm is a LRU policy with real network latency and access-count. It makes the linked-list as the LRU policy and makes groups by the algorithms. Wooster and Abrams [40] explore a proxy caching algorithm that estimates the download time for a document based on a history of download times. The algorithm (LAT) chooses the document with the smallest download time for replacement, i.e., document popularity is not considered. Cao and Irani [8] provide improved performance with the GreedyDual-

Table 1 Consideration of loading time in caching

<table><tr><td></td><td>LRU</td><td>LAT</td><td>GD-Size</td></tr><tr><td>Entry</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Exit</td><td>No</td><td>Yes</td><td>Yes</td></tr></table>

Size algorithm where the size of the document is also considered in document purging decisions from the proxy caches. The GreedyDual-Size algorithm is an extension of the DualSize algorithm proposed by [41] by using Cost/Size as the parameter used in caching. Here, cost is de<sup>fi</sup>ned as the cost of bringing the document to the server, and size is the size of the document. The cost can be de<sup>fi</sup>ned depending on the goal of the algorithm, thus, the cost corresponds to the loading time of the document in our study. We test the screening technique over the LAT and the GD-Size algorithms in this paper, since both algorithms consider document loading times when purging documents from the cache.

Although not based on LRU, a screening algorithm for web caching to reduce disk usage on proxy servers has been studied. It is suggested that without screening, most caching algorithms maximize hit ratio, however, maximizing hit ratio does not necessarily maximize the cache performance. Caching an object requires a disk access. Frequent disk access causes the proxy server to be overloaded and this in turn results in lower proxy performance [23]. Rizzo and Vicisano [33] provide a replacement policy (LRV) that is based on the relative value of each document. The document with the least relative value is purged from the cache. The relative value of the document is calculated using the document's age, number of previous accesses and size. Bose and Cheng [7] build a queuing model to understand how various factors such as hit rate, arrival rate and <sup>fi</sup>le sizes affect the proxy server performance.

Table 1 presents three popular proxy caching algorithms in terms of whether these algorithms consider loading time in entry decisions (deciding on whether a document should be admitted into cache) and/ or exit decisions (deciding which cached document to remove from the cache). As can be seen, none of the popular caching algorithms consider loading time for entry decisions but both LAT and GD-Size consider loading time for exit decisions.<sup>2</sup> Since the screening technique proposed here affects the entry decision, the technique is potentially useful for all three algorithms. One advantage of our screening approach is that it does not alter the existing policy that is implemented in the proxy server, rather, the screening is done outside and caching technique is still the existing policy except that it operates on a screened set of documents. This allows the vast number of LRU implementations to remain intact — only a front-end step can be added on to the existing implementation. In the next section we describe the screening policy and derive a delay expression for the same.

## 3. Analysis of screening policy

The screening technique is implemented as follows. After a document is fetched from the origin server, its loading time (denoted by z) is estimated. If the loading time is below a pre-determined threshold (¯z), i.e. z bz¯, the document is not cached; otherwise the document is cached and its tenure in the cache is in accordance with the LRU policy. Note that if ¯z=0, the proposed screening policy reduces to the basic LRU policy. In the following, the screening threshold (¯z) is determined so as to minimize the expected end user delay.

## 3.1. Assumptions

We begin with the following two assumptions:

1. Document loading times follow a heavy tailed distribution [5] such as Pareto distribution with density function given by

$$
f (z) = \frac {a b ^ {a}}{z ^ {a + 1}}, a > 0, \forall z \geq b,\tag{1}
$$

In the Pareto distribution a and b are the shape and the scale parameters respectively. The distribution is heavy tailed and captures the possibility that there could be a signi<sup>fi</sup>cant number of documents with high loading times. Barford and Crovella [5] review the essentials of generating web workloads to test network and server performance where the underlying distribution for loading times follows a Power Law distribution. We have also derived all the results in this section using a Uniform loading time distribution. While the qualitative nature of the results is maintained with uniform loading times, we only report the results pertaining to the Pareto distribution since it is more realistic.

2. A document's age is de<sup>fi</sup>ned as the amount of time elapsed since last access to the document. The demand on a document with age x is a non-homogenous Poisson process with instantaneous mean rate given by

$$
\theta (x) = \frac {1}{\alpha x + \beta}; \quad \alpha , \beta > 0, \text {   and   } \alpha <   1,\tag{2}
$$

where α is the age-sensitivity parameter. As α increases, document demand is more age-sensitive and the age is a stronger predictor of demand; conversely as α decreases, document demand becomes less predictive and hence more random. The demand model in Eq. (2) re<sup>fl</sup>ects the fact that a document that is frequently accessed is likely to have low age (on average). By using a non-homogeneous process (i.e., allowing the mean θ(x) to change) we accommodate the fact that the popularity of a document could change over time.

## 3.2. Screening parameter

After some analysis, it is possible to show that the optimal extent of screening (¯z) is given by

$$
\overline {{z}} = b \left(\frac {n}{L ^ {*}}\right) ^ {1 / a},\tag{3}
$$

for a set of n documents that could potentially be accessed by the users of the proxy server. In Eq. (3), L⁎ denotes the optimum number of documents marked as cacheable in the set of n documents. The value of $L ^ { * }$ is obtained by solving

$$
\frac {\partial}{\partial L} \left(L ^ {1 - \frac {1}{a}} \left(1 - \left(1 - \frac {R}{L}\right) ^ {\frac {1}{1 - \alpha}}\right)\right) = 0.\tag{4}
$$

In Eq. (4) R is the cache capacity in terms of the average number of documents that can be accommodated in the cache. In the next subsection and Appendix B, we derive Eqs. (3) and (4).

## 3.3. Derivation

We <sup>fi</sup>rst <sup>fi</sup>nd the number of documents (L) that should make up the set of cacheable documents. When L documents are accepted into the cacheable set, the lowest $( n - L )$ documents (in terms of loading time) are considered non-cacheable. Thus we can restate the problem as follows. Given n documents whose loading times and sizes are drawn from known distributions, <sup>fi</sup>nd $L ^ { * }$ such that the expected delay per access, W(L), is minimized.

Let us label the n documents as $1 , 2 , . . . , n .$ First, sort the documents in descending order of loading time: $z _ { ( 1 ) } { \ge } z _ { ( 2 ) } { \ge } z _ { ( 3 ) } { \ge } . . . { \ge } z _ { ( n ) }$ . Next, select the <sup>fi</sup>rst L documents in this ordering as the cacheable set. The expected delay per access for a given value of L is composed of two terms: $W ( L ) = W _ { 1 } ( L ) + W _ { 2 } ( L )$ . The <sup>fi</sup>rst term, $W _ { 1 } ( L ) ,$ , is the expected delay when the user requests one of the documents in the cacheable set, while the delay associated with the non-cacheable set is $W _ { 2 } ( L ) .$ Note that the user experiences delay only when the request causes a cache miss, i.e., the request is made on one of the documents outside of the cache.

The average loading time of a cacheable document is $\begin{array} { r } { L ^ { - 1 } \Sigma _ { i = 1 } ^ { L } z _ { ( i ) } , } \end{array}$ and the probability of a cache miss is given by $1 - \Sigma _ { r = 1 } ^ { L } p _ { r } q _ { \mathrm { r } }$ . The term p is the probability that there are r documents in the cache and $q _ { r }$ is the probability that a document in the cache is requested, given that there are r documents in the cache. Thus the delay associated with cacheable documents is given by,

$$
W _ {1} (L) = \frac {L}{n} \cdot \left(L ^ {- 1} \sum_ {i = 1} ^ {L} z _ {(i)}\right) \cdot \left(1 - \sum_ {i = 1} ^ {L} p _ {r} q _ {r}\right).\tag{5}
$$

The expression for $q _ { r }$ is derived in [27] as

$$
q _ {r} = 1 - \frac {L - r}{L} \prod_ {l = L - r + 1} ^ {L} \frac {(1 - \alpha) l}{(1 - \alpha) l + \alpha},\tag{6}
$$

If the document sizes have mean $\mu _ { y }$ and standard deviation $\sigma _ { y }$ (but can follow any general distribution), it can be shown that [27]:

$$
p _ {r} \approx \Phi \left(\frac {C - \mu_ {y} r}{\sigma_ {y} \sqrt {r (L - r) / (L - 1)}}\right) - \Phi \left(\frac {C - \mu_ {y} (r + 1)}{\sigma_ {y} \sqrt {(r + 1) (L - r - 1) / (L - 1)}}\right),\tag{7}
$$

where Φ(·) is the CDF of standard Normal. Using order statistics arguments, we derive an expression for the average loading time of the <sup>fi</sup>rst L documents as below (See Appendix A):

$$
\frac {1}{L} \sum_ {i = 1} ^ {L} z _ {(i)} = \frac {a b}{(a - 1)} \frac {\Gamma (n + 1)}{\Gamma (n + 1 - 1 / a)} \frac {\Gamma (L + 1 - 1 / a)}{\Gamma (L + 1)}.\tag{8}
$$

To evaluate $W _ { 2 } ( L )$ (the delay associated with non-cacheable documents) we note that the average loading time for a document in the non-cacheable set is $( n - L ) ^ { - 1 } \Sigma ^ { n } { } _ { i = L + 1 } z _ { ( i ) } .$ . The delay associated with non-cacheable documents is therefore,

$$
W _ {2} (L) = \left(\frac {n - L}{n}\right) \cdot \left(\frac {1}{n - L} \sum_ {i = L + 1} ^ {n} z _ {(i)}\right).\tag{9}
$$

The total expected delay is $W ( L ) = W _ { 1 } ( L ) + W _ { 2 } ( L )$ . To <sup>fi</sup>nd the optimum $L ^ { * }$ value, the following approximation can be used. For a cache capacity of C, the average number of documents that will <sup>fi</sup>t in the cache can be approximated by $R { = } C / \mu _ { y } .$ . The total expected delay can be written as (See Appendix B):

Approximation results (10,000 documents, a=1.5 and high cache capacity)

<table><tr><td> $\alpha$ </td><td> $L_{approx}$ </td><td> $L^{*}$ </td><td>Delay with  $L = L_{approx}$ </td><td>Delay with  $L = L^{*}$ </td></tr><tr><td>0.15</td><td>3002</td><td>3002</td><td>19.8361</td><td>19.8361</td></tr><tr><td>0.2</td><td>3015</td><td>3015</td><td>19.8242</td><td>19.8242</td></tr><tr><td>0.3</td><td>3111</td><td>3111</td><td>19.6965</td><td>19.6965</td></tr><tr><td>0.4</td><td>3339</td><td>3338</td><td>19.2990</td><td>19.2990</td></tr><tr><td>0.5</td><td>3750</td><td>3749</td><td>18.4682</td><td>18.4682</td></tr><tr><td>0.6</td><td>4448</td><td>4447</td><td>16.9740</td><td>16.9740</td></tr><tr><td>0.7</td><td>5689</td><td>5688</td><td>14.3796</td><td>14.3796</td></tr><tr><td>0.8</td><td>8257</td><td>8255</td><td>9.6063</td><td>9.6063</td></tr><tr><td>0.9</td><td>10,000</td><td>10,000</td><td>1.7006</td><td>1.7006</td></tr></table>

![](/api/attachments/VGQ6EZRA/fulltext/images/43ad670a3aa4e2beba139e71b8f1c6179314dbddf39d687f778eb51321435f6d.jpg)  
Fig. 2. Effect of cache size on loading time threshold (¯z).

$$
W = \frac {a b}{a - 1} - \frac {a b}{a - 1} \left(\frac {L}{n}\right) ^ {1 - \frac {1}{a}} \left(1 - \left(1 - \frac {R}{L}\right) ^ {\frac {1}{1 - \alpha}}\right).\tag{10}
$$

The minimization of Eq. (10) yields the <sup>fi</sup>rst order condition in Eq. (4) that can be solved to obtain L⁎ and consequently the optimal screening parameter (¯z).

As can be seen from Table 2, the approximation works well in all the cases that were studied. In addition, the nature of the delay function is such that it is relatively <sup>fl</sup>at around the optimal value. Thus small deviations from the optimal value do not cause a signi<sup>fi</sup>cant difference in the delay.

## 3.4. Numerical results

We study different levels of proxy cache capacity ranging from 1% to 30% of all the potential documents (n). Other parameters varied in these experiments are the age-sensitivity of the documents and the document size standard deviation. The following Table shows the values used for the numerical study.

From $\operatorname { E q . } \left( 3 \right)$ one can easily estimate the effect of scale and shape parameters b and a. Note that age sensitivity parameter α implicitly affects ¯z, because L⁎ is obtained from (4). Fig. 2 shows that the loading time threshold, ¯z, varies signi<sup>fi</sup>cantly with the cache capacity; however, is relatively insensitive to α.

Fig. 3 shows the effects of the age-sensitivity parameter on the expected delay per access for different levels of capacity. A low capacity cache in our experiments stores 1% of the documents; hence, for our experiments the cache capacity is 10 documents. At medium capacity, the cache can store 5% of the documents while high and very high cache capacity correspond to 10% and 30% of the documents, respectively. Fig. 3 implies that as the cache capacity increases, the improvement (over LRU) increases for low levels of the age-sensitivity parameter. However, the improvement over LRU (across cache capacities) is roughly the same at high levels of age-sensitivity. The reason for this is that when age-sensitivity is high, there is less need for a large cache, i.e., the re-referencing behavior at high α ensures that a relatively small cache is suf<sup>fi</sup>cient to provide adequate response.

![](/api/attachments/VGQ6EZRA/fulltext/images/0458a975220300e55f2caac5c72cfa2670827a92c11853f195858b883e7b8aea.jpg)  
Fig. 3. Improvement over LRU.

![](/api/attachments/VGQ6EZRA/fulltext/images/fac631a03c1ded951f5bae35677b4977f990fa1d854fd3f8635886d02cd61a10.jpg)  
Fig. 4. Minimum average expected delay per request.

For lower levels of cache capacities the improvement drops slightly as the request pattern becomes more age-sensitive. However, for higher cache capacities, the drop in improvement is more dramatic. Once again, the reason for this is that the large cache size becomes less important as the request pattern becomes more age-sensitive.

Fig. 4 shows the delay with respect to age-sensitivity. For each level of cache capacity, the delay (slightly) decreases as the age-sensitivity of demand increases. The intuition behind this is shown in Fig. 5, where it can be seen that the number of cacheable documents increases with age-sensitivity. As age-sensitivity increases, fewer documents are screened out (i.e., the cacheable set becomes larger) because at high age-sensitivity, once a document is requested, it can keep getting requested and the penalty of not allowing this document in the cache can be very high. As can be seen from Fig. 5, at high agesensitivity and very high levels of cache capacity, the screening policy becomes very close to the basic LRU policy.

Another factor that could affect the performance of the screening policy is variation in document size. To study size variation effects, the mean document size is held at 10 units, and to avoid negative sizes, we only consider $\sigma _ { y } = 1 , 2$ and 3 corresponding to a low, medium and high variation respectively. Fig. 6 shows that there is little effect of document size variation on the performance of screening policy.

![](/api/attachments/VGQ6EZRA/fulltext/images/46e40bbf04aebca4b75bcf5195037d361ac0f86fc061e729881e9d7c6510d364.jpg)  
Fig. 5. L⁎ for different levels of age-sensitivity and cache capacity.

![](/api/attachments/VGQ6EZRA/fulltext/images/ad039a15ed18c0bdfcdbcfca07b5d5ad3a27947cc6f72f94165d9437b6d7997e.jpg)  
Fig. 6. Variation of document sizes and capacity (α = 0.3).

Fig. 7 shows a result similar to Fig. 6. One important aspect to note in this experiment is that the loading times and document sizes are uncorrelated. Because of this, the variation in document size does not have an impact — a <sup>fi</sup>nding consistent to the one by [27] where the performance of the LRU algorithm was found to be insensitive to document size variation.<sup>3</sup>

## 4. Simulation validation

The simulation experiments in this section serve to validate the theoretical results in the previous section. First we simulate the basic LRU algorithm and demonstrate that the theoretical delay predicted for this algorithm matches with the simulation results. Next we <sup>fi</sup>nd the optimal theoretical delay for the screening approach and compare this to the simulation result. In addition, we use simulation as a means to obtain the expected delays for other policies such as LAT and GD-Size. Finally, the simulation results allow us to examine the performances of these policies when the second objective, namely, traf<sup>fi</sup>c downloaded, is adopted.

## 4.1. Document generation

Before starting the simulation, n (in this case one thousand) documents with loading times and sizes are generated. As stated earlier, loading times are drawn from a Pareto distribution using the following inverse distribution function

$$
z _ {i} = b \left(\frac {1}{1 - s}\right) ^ {\frac {1}{a}},\tag{11}
$$

where a and b are the shape and scale parameters of Pareto distribution and s is a random number uniformly distributed between 0 and 1. The document sizes are drawn from a Normal distribution with mean size of 10 and standard deviations of 1, 2 and 3.

In order to test the effects of correlation between loading time and size, we <sup>fi</sup>x the set of loading times (z ) and choose a (correlated) set of sizes (y ) as follows

$$
y _ {i} = \frac {z _ {i} + u}{v},\tag{12}
$$

where v is the scaling constant to set the mean of the sizes to a desired value (in this case 10) and u is a random number that is drawn from

![](/api/attachments/VGQ6EZRA/fulltext/images/2136ea4c4c2ae0ad956ffbea361a2dcddefcf879c625894b7ed17ad06273a697.jpg)  
Fig. 7. Age-sensitivity and document size variation (medium C).

$N ( \mu _ { y } \nu , \sigma _ { y } ) .$ (See Appendix C to see how $\sigma _ { y }$ is chosen to have the desired correlation between loading time and size).

## 4.2. Demand trace generation

The next step in the simulation is to generate a demand trace. We generate a demand trace in the following way.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Step 1 Start with n documents with random ages; Set a small time interval h; Choose demand parameters  $\alpha$ ,  $\beta$ , and demand trace size D; Set k=0.
Step 2 Generate a random number  $p\in[0,1]$ ;  $p=p+h$ .
Step 3 Calculate  $T(i)=\left(x_{i}+\frac{\beta}{\alpha}\right)\left(p^{-\frac{\alpha}{1-\alpha}}-1\right)$  for each i; This is the time to next access for document i.
Step 4 Find  $\Delta t=\min T(i),\forall i=1,2,\ldots,n.$ 
Step 5 Increase  $x_{j}(j\neq i)$  by  $\Delta t$ , and set  $x_{i}=0$ .
Step 6 k=k+1; If k=D then Stop; Else If k&lt;D then go to STEP 2.
</div>

## 4.3. Simulation results

A trace of 10,000 hits was generated using the above procedure. Table 3 shows simulation results for documents with a size coef<sup>fi</sup>cient of variation of 0.1 (i.e. standard deviation of 1) and cache capacity of 500 KB, corresponding to the ability to cache 5% of the documents. The <sup>fi</sup>rst group of three columns shows the average delay when LRU is implemented, the delay when the screening method is used over LRU and the bene<sup>fi</sup>t of screening for LRU. The screening parameter ¯z is found using Eq. (3). We also use this parameter to run screening on LAT and GD-Size, and <sup>fi</sup>nd improvements. However, since ¯z in Eq. (3) is derived for LRU, it may not necessarily yield the best performance for LAT and GD-Size. Instead, Table 4 shows the best improvements due to screening observed in simulation experiments. Both LAT and GD-Size can be further improved with screening to almost 7% and 49%, respectively.

Table 5 shows simulation results for different levels of document size variation and cache capacity. The bene<sup>fi</sup>ts of screening are higher when the demand pattern is more random (relatively low α) and the cache capacity is high (able to accommodate 10% of the documents). This is consistent with our <sup>fi</sup>ndings in Section 3 (see Fig. 3), thus

## Table 3

Experimental parameter values

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Number of documents (n) 10,000
Cache capacity 500 units (e.g., KB, MB, GB etc.) unless noted otherwise
Low: 100, Medium: 500, High: 1000, Very high: 3000
Loading time distribution Pareto distribution with a=1.5 and b=20.
Mean document size ( $\mu_{y}$ ) 10 units (e.g. KB, MB, GB etc.)
S.D. of document sizes ( $\sigma_{y}$ ) 1 unless noted otherwise; Low: 1, Medium: 2, High: 3
Age-sensitivity parameter 0.3 unless noted otherwise; Low: 0.2, Medium: 0.4,
( $\alpha$ ) High: 0.6
</div>

Simulation results for different age sensitivities at medium cache capacity (500 KB) (Cov of document sizes: 0.3)

<table><tr><td rowspan="2">Alpha</td><td colspan="3">LRU delays</td><td colspan="3">LAT delays</td><td colspan="3">GD-Size delay</td></tr><tr><td>LRU</td><td>Screening</td><td>Benefit (%)</td><td>LAT</td><td>Screening</td><td>Benefit (%)</td><td>GD-Size</td><td>Screening</td><td>Benefit (%)</td></tr><tr><td>0.1</td><td>56.954</td><td>40.825</td><td>40</td><td>40.700</td><td>37.818</td><td>8</td><td>59.540</td><td>44.662</td><td>33</td></tr><tr><td>0.2</td><td>56.358</td><td>38.598</td><td>46</td><td>40.499</td><td>37.535</td><td>8</td><td>59.661</td><td>39.926</td><td>49</td></tr><tr><td>0.3</td><td>55.506</td><td>37.955</td><td>46</td><td>39.597</td><td>37.180</td><td>7</td><td>59.349</td><td>44.554</td><td>33</td></tr><tr><td>0.4</td><td>51.922</td><td>37.892</td><td>37</td><td>39.455</td><td>37.001</td><td>7</td><td>56.745</td><td>42.615</td><td>33</td></tr><tr><td>0.5</td><td>51.210</td><td>39.093</td><td>31</td><td>38.758</td><td>36.325</td><td>7</td><td>57.182</td><td>38.837</td><td>47</td></tr></table>

providing further validation of the theoretical results in section 4 and the method of <sup>fi</sup>nding ¯z.

We also consider the correlation between loading time and document size. The results of the experiments on a trace where there is relatively low correlation (0.3 and 0.4) between size and loading time are displayed in Table 6. These correlation levels are consistent with the characteristics of the real web trace we use in the next section where the correlation coef<sup>fi</sup>cient between loading time and size is 0.37. Scheuermann et al. [34] suggest a similar level of correlation. The process of obtaining a correlated size values given the loading time of the document is given in Appendix C.

## 4.4. Traffic implications

This section looks at the effects of the screening policy on the traf<sup>fi</sup>c generated on the outgoing link. To address this question, we consider some of the parameter settings used in Section 4.3 and use simulation to estimate the traf<sup>fi</sup>c downloaded by each caching technique and screening.

Here the loading times are exogenously provided to the designer and these times may or may not be correlated with size. An example of uncorrelated exogenous loading times is when the download traf<sup>fi</sup>c <sup>fl</sup>ows on different routes and the congestion parameters associated with these routes vary considerably across the routes. Thus a small document following a congested route may take more time to download than a large document that follows a less congested route. Exogenous loading times that are correlated with size could occur if the traf<sup>fi</sup>c <sup>fl</sup>ows on uniformly congested routes (or the same route with constant expected delay) and hence, the delays are proportional to the document sizes. However, these loading times can be considered exogenous if the congestion parameters are not signi<sup>fi</sup>cantly in<sup>fl</sup>uenced by the traf<sup>fi</sup>c generated by the users of the proxy server network (e.g., because the traf<sup>fi</sup>c contributed by the network users is small in proportion to the total traf<sup>fi</sup>c).

The results on Table 7 show that except for some extreme cases (such as high age sensitivity) there is no signi<sup>fi</sup>cant change in the download traf<sup>fi</sup>c between screening and LRU. Thus the reduction in delay obtained by using screening does not come at the cost of additional download traf<sup>fi</sup>c.

## 5. Parameter estimation using real web-trace data

In this section, we propose ways to estimate parameter values from real web-trace data obtained from the server log <sup>fi</sup>les of the University of California at Berkeley Home IP Web Traces [38]. The last subsection describes the <sup>fi</sup>ndings when our screening technique is simulated using the real web-trace data.

## 5.1. Estimation of demand parameters

A data point in the web trace consists of the following information: $( t _ { i j } , \ s _ { i j } , \ z _ { i j } ) ,$ , where $t _ { i j }$ is the time at which the jth hit on the ith document took place, s and $z _ { i j }$ are the size and delay of ith document at the jth hit. These values can change over time since the contents of the document as well as its loading time could change across hits. We de<sup>fi</sup>ne the age of the ith document just before the jth hit as

$$
x _ {i j} = t _ {i j} - t _ {i (j - 1)}, j > 1.\tag{13}
$$

The instantaneous access rate to document i right before its jth hit can be estimated as

$$
\theta_ {i j} = \frac {j}{t _ {i j} - t _ {i 1}}.\tag{14}
$$

According to Eq. (2), we can formulate the following regression model:

$$
\theta^ {- 1} = \alpha \cdot x + \beta + \widetilde {\varepsilon}\tag{15}
$$

to estimate the parameters α and β. Using the data from the Berkeley web trace [38], the above regression model provides an estimate of α=0.43 and $\beta = 2 0 0 0$ . The $R ^ { 2 }$ is 0.79; this indicates that (15) provides a very good <sup>fi</sup>t to the trace data.

## 5.2. Estimation of parameters for loading time distribution

To estimate the shape and scale parameter for the loading time, <sup>fi</sup>rst, we use the fact that Eq. (1) can be written as

$$
f (z) = \frac {a b ^ {a}}{(z + b) ^ {a + 1}}, \forall z \geq 0.\tag{16}
$$

Taking the maximum loading times for each document, and minimizing the sum of squared errors of the distribution function, the Berkeley web trace yields an estimate of a=1.26 and b=6.89, for the shape and scale parameters respectively. A plot of the distribution function displaying a good visual <sup>fi</sup>t using the above parameters is given in Fig. 8 below. In this estimation, we used an unbiased and ef<sup>fi</sup>cient bin size $3 . 4 9 \sigma N ^ { - 1 / 3 }$ where σ is the standard deviation of the sample and N is the sample size [35]. Although our algorithm works with any size distribution, other work on real web traces suggest that document sizes are also found to follow Pareto distribution [13].

Simulation results for different levels of cache capacity and size variation

<table><tr><td rowspan="2">Alpha</td><td rowspan="2">Size S.D.</td><td rowspan="2">Cache capacity (%)</td><td colspan="3">LRU delay</td><td colspan="3">LAT delay</td><td colspan="3">GD-Size delay</td></tr><tr><td>LRU</td><td>Screening</td><td>Benefit (%)</td><td>LAT</td><td>Screening</td><td>Benefit (%)</td><td>GD-Size</td><td>Screening</td><td>Benefit (%)</td></tr><tr><td rowspan="4">0.2</td><td rowspan="2">1</td><td>1</td><td>59.760</td><td>50.574</td><td>18</td><td>52.430</td><td>49.856</td><td>5</td><td>59.495</td><td>51.673</td><td>15</td></tr><tr><td>10</td><td>52.505</td><td>33.210</td><td>58</td><td>38.647</td><td>33.388</td><td>16</td><td>59.661</td><td>39.926</td><td>49</td></tr><tr><td rowspan="2">3</td><td>1</td><td>59.775</td><td>50.878</td><td>17</td><td>50.065</td><td>49.043</td><td>2</td><td>59.495</td><td>51.600</td><td>15</td></tr><tr><td>10</td><td>52.632</td><td>32.736</td><td>61</td><td>38.647</td><td>32.112</td><td>20</td><td>59.661</td><td>39.926</td><td>49</td></tr><tr><td rowspan="4">0.5</td><td rowspan="2">1</td><td>1</td><td>57.259</td><td>49.091</td><td>17</td><td>49.354</td><td>48.459</td><td>2</td><td>57.550</td><td>49.952</td><td>15</td></tr><tr><td>10</td><td>43.563</td><td>32.349</td><td>35</td><td>36.680</td><td>32.043</td><td>14</td><td>57.125</td><td>39.308</td><td>45</td></tr><tr><td rowspan="2">3</td><td>1</td><td>57.288</td><td>49.394</td><td>16</td><td>50.065</td><td>47.930</td><td>4</td><td>57.550</td><td>49.952</td><td>15</td></tr><tr><td>10</td><td>43.563</td><td>33.119</td><td>32</td><td>36.680</td><td>30.277</td><td>21</td><td>57.125</td><td>39.308</td><td>45</td></tr></table>

Effects of correlation between size and loading time (α =0.3, C=500)

<table><tr><td rowspan="2"> $\rho (y, z)$ </td><td rowspan="2">S.D of doc sizes</td><td colspan="3">Delay savings</td><td colspan="3">Traffic savings</td></tr><tr><td>LRU (%)</td><td>LAT (%)</td><td>GD-Size (%)</td><td>LRU (%)</td><td>LAT (%)</td><td>GD-Size (%)</td></tr><tr><td rowspan="2">0.3</td><td>Low (0.76)</td><td>37.60</td><td>0.28</td><td>20.19</td><td>-1.82</td><td>-0.11</td><td>-1.52</td></tr><tr><td>High (2.67)</td><td>32.15</td><td>0.31</td><td>18.09</td><td>-2.20</td><td>-0.07</td><td>-2.05</td></tr><tr><td rowspan="2">0.4</td><td>Low (0.61)</td><td>36.99</td><td>0.17</td><td>20.40</td><td>-2.14</td><td>-0.12</td><td>-1.45</td></tr><tr><td>High (2.88)</td><td>30.61</td><td>0.29</td><td>19.77</td><td>-2.05</td><td>-0.18</td><td>-1.05</td></tr></table>

Once the values for these parameters are estimated, L⁎ can be found using Eq. (3), and hence the optimal screening parameter, ¯z. For the Berkeley web trace, the optimal screening parameter ¯z≈52 at the medium cache level (5%). Any document below a loading time of 52 seconds is not admitted into the cache.

## 5.3. Size dependency

The documents which are accessed in the real trace are discovered to have a high variation in their size. This phenomenon causes the cache to be <sup>fi</sup>lled inef<sup>fi</sup>ciently. In addition, we discover some dependency between loading time and size of the documents in the real web trace. When a large document with high delay is accessed and therefore admitted to the cache, the remaining cache space may not be enough for the next requested document causing the policy to remove many documents in order to accommodate the new document.

In order to avoid this problem we screen the documents according to loading time/size ratio. This allows us to smooth the variation of the document size and is enough to capture the variation in the loading time. Table 8 shows the bene<sup>fi</sup>t of screening against no screening. Similarly, with a little improvement of bandwidth the end users can bene<sup>fi</sup>t from screening.

## 6. Summary and conclusions

This study proposed and evaluated a screening policy for browser caching that was based upon the loading time of documents. In the <sup>fi</sup>rst phase of this study, we expressed the average expected delay for a screening policy and found the optimum number of documents to consider as cacheable. We have presented a method to convert the screening threshold to a loading time threshold to be used in the screening policy. To validate the analytical results, we simulated the LRU policy and the screening policy and found a close match between the analytical values of delay and those obtained in the simulation experiment. An important result of study is that screening can be especially bene<sup>fi</sup>cial when the document request pattern is more random (as opposed to one that strongly exhibits re-referencing) or when the cache capacity is relatively high. We also simulated the screening policy to augment the LAT and GD-Size policies and these simulations provided similar insights. However, as expected, the LAT policy did not provide as much bene<sup>fi</sup>t as the other two algorithms, because it already takes loading time as the criteria when purging a document from the cache.

![](/api/attachments/VGQ6EZRA/fulltext/images/f321c35ae7ec49bfdb96b9e750e2ef6ac20944e5cee347f23226c2c7439d5e98.jpg)  
Fig. 8. Distribution function of loading times.

While running the simulations we kept track of the sizes of the documents and the bandwidth usage of the proxy server. The interest was to see if screening can reduce delays without signi<sup>fi</sup>cantly impacting the traf<sup>fi</sup>c on the outgoing link. Our experiments showed that screening can signi<sup>fi</sup>cantly reduce delays, while holding the download traf<sup>fi</sup>c at (approximately) the same level.

We also found that the documents accessed in the actual web trace have very high size variation and that the loading times of the documents were dependent to their size. This led us to extend the loading time criterion to loading time/size. The simulations showed a smaller bene<sup>fi</sup>t than the case of generated trace.

This study is part of our on-going interest in the operational and economic aspects of content delivery on the Internet. This study can be bene<sup>fi</sup>cial to companies in the business of creating content delivery products (such as edge servers, caching accelerators) as well as those involved in the business of providing content delivery services (such as content distributors, Internet Service Providers). For future research on this problem we plan to study the interaction between the caching policy used at proxy-servers and the placement of these servers, e.g., a way for proxy-servers to cooperate with one another for the fast distribution of content.

Delay and bandwidth savings for loading times

<table><tr><td rowspan="2">Alpha</td><td rowspan="2"> $\rho (y, z)$ </td><td rowspan="2">Cache capacity</td><td colspan="2">LRU</td><td colspan="2">LAT</td><td colspan="2">GD-Size</td></tr><tr><td>Delay savings (%)</td><td>Bandwidth savings (%)</td><td>Delay savings (%)</td><td>Bandwidth savings (%)</td><td>Delay savings (%)</td><td>Bandwidth savings (%)</td></tr><tr><td rowspan="6">0.1</td><td rowspan="2">0</td><td>500</td><td>46.17</td><td>-0.42</td><td>1.81</td><td>0.54</td><td>33.31</td><td>0.31</td></tr><tr><td>1000</td><td>63.62</td><td>-0.85</td><td>14.82</td><td>5.27</td><td>48.58</td><td>3.31</td></tr><tr><td rowspan="2">0.5</td><td>500</td><td>44.26</td><td>-0.38</td><td>1.81</td><td>0.54</td><td>33.24</td><td>1.81</td></tr><tr><td>1000</td><td>62.41</td><td>-0.76</td><td>-3.81</td><td>-1.99</td><td>45.85</td><td>3.95</td></tr><tr><td rowspan="2">1</td><td>500</td><td>0.08</td><td>0.08</td><td>1.81</td><td>0.54</td><td>0.00</td><td>0.00</td></tr><tr><td>1000</td><td>0.66</td><td>0.66</td><td>2.78</td><td>1.02</td><td>64.74</td><td>64.74</td></tr><tr><td rowspan="6">0.3</td><td rowspan="2">0</td><td>500</td><td>44.89</td><td>-2.76</td><td>1.90</td><td>0.51</td><td>33.21</td><td>0.48</td></tr><tr><td>1000</td><td>58.57</td><td>-5.29</td><td>14.66</td><td>5.36</td><td>50.27</td><td>2.80</td></tr><tr><td rowspan="2">0.5</td><td>500</td><td>41.66</td><td>-0.32</td><td>1.90</td><td>0.51</td><td>31.05</td><td>1.98</td></tr><tr><td>1000</td><td>62.41</td><td>-0.76</td><td>2.92</td><td>1.04</td><td>46.27</td><td>3.36</td></tr><tr><td rowspan="2">1</td><td>500</td><td>0.00</td><td>0.00</td><td>1.90</td><td>0.51</td><td>26.30</td><td>26.30</td></tr><tr><td>1000</td><td>-1.89</td><td>-1.89</td><td>2.92</td><td>1.04</td><td>0.00</td><td>0.00</td></tr><tr><td rowspan="6">0.5</td><td rowspan="2">0</td><td>500</td><td>30.21</td><td>-8.89</td><td>2.36</td><td>0.65</td><td>27.06</td><td>-2.57</td></tr><tr><td>1000</td><td>31.09</td><td>-17.19</td><td>14.47</td><td>5.61</td><td>45.32</td><td>0.38</td></tr><tr><td rowspan="2">0.5</td><td>500</td><td>30.23</td><td>-8.59</td><td>2.36</td><td>0.65</td><td>27.48</td><td>-0.41</td></tr><tr><td>1000</td><td>30.36</td><td>-16.79</td><td>2.65</td><td>0.86</td><td>42.55</td><td>2.59</td></tr><tr><td rowspan="2">1</td><td>500</td><td>-1.59</td><td>-1.59</td><td>2.36</td><td>0.65</td><td>6.63</td><td>6.63</td></tr><tr><td>1000</td><td>-5.16</td><td>-5.16</td><td>2.65</td><td>0.86</td><td>59.20</td><td>59.20</td></tr></table>

Table 8  
Delay and bandwidth savings for loading times

<table><tr><td rowspan="2">Cache capacity (%)</td><td colspan="3">Delay savings</td><td colspan="3">Traffic difference</td></tr><tr><td>LRU (%)</td><td>LAT (%)</td><td>GD-Size (%)</td><td>LRU (%)</td><td>LAT (%)</td><td>GD-Size (%)</td></tr><tr><td>1.0</td><td>1.753</td><td>6.612</td><td>0.003</td><td>-10.525</td><td>-3.035</td><td>0.000</td></tr><tr><td>0.5</td><td>3.074</td><td>5.502</td><td>0.005</td><td>-7.622</td><td>-2.671</td><td>-0.003</td></tr><tr><td>0.1</td><td>4.583</td><td>0.129</td><td>0.246</td><td>-3.404</td><td>-0.066</td><td>-0.030</td></tr></table>

## Appendix

## A. Proof for order statistics

If all z's are drawn from a distribution $f ( z ) ,$ , given a value of z, when drawn n times, the probability of being the ith ranked is,

$$
P (i \text {th} | z) = \binom{n - 1}{i - 1} (1 - F (z)) ^ {i - 1} (F (z)) ^ {n - i}.\tag{A1}
$$

One can verify that

$$
\sum_ {i = 1} ^ {n} P (i \text {th} | z) = 1;\tag{A2}
$$

and

$$
P (i \text {th}) = \int_ {z \in Z} P (i \text {th} | z) f (z) d z = \binom{n - 1}{i - 1} \frac {(i - 1) ! (n - i) !}{n !} = \frac {1}{n}.\tag{A3}
$$

So given ith ranked, the conditional z distribution is

$$
f (z | i \mathrm{th}) = \frac {P (i \mathrm{th} | z) f (z)}{P (i \mathrm{th})} = \frac {\Gamma (n + 1)}{\Gamma (n - i + 1) \Gamma (i)} \left(1 - F (z)\right) ^ {i - 1} \left(F (z)\right) ^ {n - i} f (z).\tag{A4}
$$

The conditional mean is

$$
E (z | i \text {th}) = \int_ {z \in Z} z f (z | i \text {th}) d z.\tag{A5}
$$

If z follows Pareto distribution with density $f ( z ) = a b ^ { a } z ^ { - a - 1 }$ , where a>1, and $z > b$

$$
E (z | i \mathbf {t h}) = b \int_ {0} ^ {1} \frac {\Gamma (\mathbf {n} + 1)}{\Gamma (\mathbf {n} - i + 1) \Gamma (\mathbf {i})} (1 - z) ^ {\mathrm{i} - 1 - 1 / a} z ^ {\mathrm{n} - i} \mathrm{d} z,\tag{A6}
$$

which leads to,

$$
E (z | i \mathrm{th}) = b \frac {\Gamma (i - 1 / a) \Gamma (n + 1)}{\Gamma (i) \Gamma (n + 1 - 1 / a)}.\tag{A7}
$$

One can <sup>fi</sup>nd the mean for <sup>fi</sup>rst L documents and the last n−L documents as follows,

$$
\frac {1}{L} \sum_ {i = 1} ^ {L} E (z | i \text {th}) = \frac {a b}{(a - 1)} \frac {\Gamma (n + 1)}{\Gamma (n + 1 - 1 / a)} \frac {\Gamma (L + 1 - 1 / a)}{\Gamma (L + 1)},\tag{A8}
$$

and given the expected mean for n documents is ab $\textstyle { \big / } ( a - 1 )$ , then the expected mean for the last (n−L) documents is,

$$
\frac {1}{n - L} \sum_ {i = L + 1} ^ {L} E (z | i \text {th}) = \frac {1}{n - L} \frac {a b}{(a - 1)} \left(n - L \frac {\Gamma (n + 1)}{\Gamma (n + 1 - 1 / a)} \frac {\Gamma (L + 1 - 1 / a)}{\Gamma (L + 1)}\right).\tag{A9}
$$

## B. Proof for approximation

Average delay per access can be written as,

$$
\begin{array}{l} W = \left(\frac {n - L}{n}\right) \left(\frac {1}{n - L} \frac {a b}{(a - 1)} \left(n - L \frac {\Gamma (n + 1)}{\Gamma (n + 1 - 1 / a)} \frac {\Gamma (L + 1 - 1 / a)}{\Gamma (L + 1)}\right)\right) \\ \quad + \frac {L}{n} \left(\frac {a b}{(a - 1)} \frac {\Gamma (n + 1)}{\Gamma (n + 1 - 1 / a)} \frac {\Gamma (L + 1 - 1 / a)}{\Gamma (L + 1)}\right) \left(1 - \sum_ {r = 1} ^ {L} p _ {r} q _ {r}\right), \end{array}\tag{B1}
$$

where $q _ { r }$ and $p _ { r }$ are given by Eqs. (6) and (7). The <sup>fi</sup>rst step of the approximation is to assume equal size documents. Let $R { = } C / \mu _ { y }$ . Then we have,

$$
W = \frac {a b}{a - 1} - \frac {1}{n} \frac {a b}{a - 1} \left(\frac {\Gamma (n + 1)}{\Gamma (n + 1 - 1 / a)} \frac {\Gamma (L + 1 - 1 / a)}{\Gamma (L + 1)}\right) \left(1 - \left(1 - \frac {R}{L}\right) ^ {\frac {1}{1 - \alpha}}\right),\tag{B2}
$$

where we assume that $R / L < < 1 .$ Furthermore, since n is large and $a > 1$ we can use the approximate form of the Gamma function and get,

$$
W = \frac {a b}{a - 1} - \frac {a b}{a - 1} \left(\frac {L}{n}\right) ^ {1 - \frac {1}{a}} \left(1 - \left(1 - \frac {R}{L}\right) ^ {\frac {1}{1 - \alpha}}\right).\tag{B3}
$$

From Eq. (B3), L⁎ can be found by solving,

$$
\frac {\partial}{\partial L} \left(L ^ {1 - \frac {1}{a}} \left(1 - \left(1 - \frac {R}{L}\right) ^ {\frac {1}{1 - \alpha}}\right)\right) = 0.\tag{B4}
$$

In general we can write

$$
L ^ {*} = \varphi (a, \alpha) R.\tag{B5}
$$

C. Correlated size generation

Take three random variables Z, Y and U such that $Y = Z + U ,$ and assume that Z and U are independent. If the correlation between Y and Z is $\rho ( Y , Z )$ then,

$$
\operatorname{Var} (U) = \operatorname{Var} (Z) \left(\frac {1}{\rho (Y , Z) ^ {2}} - 1\right).
$$

Proof: Assume that $Y = Z + U ; Z$ and U are any two independent random variables with variances $\sigma _ { Z } ^ { 2 }$ and σ<sup>2</sup> respectively. $\operatorname { C o v } ( Y , Z ) =$ $\operatorname { C o v } ( Z , Z + U ) = \operatorname { C o v } ( Z ) + \operatorname { C o v } ( Z , U )$ . From the independence assumption, $\mathsf { C o v } ( Z , U ) = 0 ,$ , and therefore, $\begin{array} { r } { \mathrm { C o v } ( Y , Z ) = \mathrm { V a r } ( Z ) = \sigma _ { Z } ^ { \hat { 2 } } . \mathrm { S i n c e } \rho ( Y , Z ) = \frac { \mathrm { C o v } ( Y , Z ) } { \sigma _ { Y } \sigma _ { 7 } } , } \end{array}$ then $\begin{array} { r } { \rho ( Y , Z ) = \frac { \sigma _ { Z } } { \sigma _ { \mathrm { v } } } . } \end{array}$ . Furthermore, Z and U are independent, and thus, $\begin{array} { r } { \rho ( Y , Z ) = \frac { \sigma _ { Z } } { \sqrt { \sigma _ { Z } ^ { 2 } + \sigma _ { U } ^ { 2 } } } . } \end{array}$

## References

[1] M. Abrams, C.R. Standridge, G. Abdulla, S. Williams, E.A. Fox, Caching proxies: limitations and potentials, Proceedings of the 4th International WWW Conference Boston MA December 1995

[2] M.F. Arlitt, L. Cherkasova, J. Dilley, R.J. Friedrich, T.Y. Jin, evaluating content management techniques for Web proxy caches, ACM SIGMETRICS perform, Evaluation Review 27 (4) (March 2000) 3–11.

[3] M.F. Arlitt, R.J. Friedrich, T.Y. Jin, Performance evaluation of Web proxy cache replacement policies, Technical Report HPL-98-97 (R.1), Hewlett–Packard Company, Palo Alto, CA, 1999.

[4] R. Ayani, Y.M. Teo, Y.S. Ng, Cache pollution in Web proxy servers, Proceedings of International Parallel and Distributed Processing Symposium, 2003, pp. 1–7.

[5] P. Barford, M. Crovella, Generating representative Web workloads for network and server performance evaluation, Proceedings of the Joint International Conference on Measurement and Modeling of Computer Systems (SIGMETRICS'98 PERFORMANCE'98), Madison, WI, June 1998, pp. 151–160.

[6] G. Barish, K. Obraczke, World Wide Web caching: trends and techniques, IEEE Communications Magazine 38 (5) (May 2000) 178–184.

[7] I. Bose, H.K. Cheng, Performance models of a <sup>fi</sup>rm's proxy cache server, Decision Support Systems 29 (2000) 47–57

[8] P. Cao, S. Irani, Cost-aware WWW Proxy caching algorithms, Proceedings of the USENIX Symposium on Internet Technologies and Systems, Monterey, CA, December 1997

[9] J. Challenger, A. Lyengar, P. Dantzig, A scalable system for consistently caching dynamic Web data, Proceedings of IEEE INFOCOM'99, vol.1, IEEE Press, Piscataway, N.J., March 1999, p. 294.

[10] C.Y. Chang, T. McGregor, G. Holmes, The LRU⁎ WWW proxy cache document replacement algorithm, Proceedings of the Asia Paci<sup>fi</sup>c Web Conference, 1999.

[11] K. Cheng, Y. Kambayashi, LRU-SP: a size-adjusted and popularity-aware LRU replacement algorithm for Web caching, Proceedings of the 24th Annual International Computer Software and Applications Conference, 2000, p. 48.

[12] I.R. Chiang, P.B. Goes, Z. Zhang, Periodic cache replacement policy for dynamic content at application server, Decision Support Systems 43 (2007) 336–348.

[13] C. Cunha, A. Bestavros, M. Crovella, Characteristics of WWW client-based traces, Technical Report TR-95-010, Boston University, April 1995.

[14] A. Datta, K. Dutta, H. Thomas, D. VanderMeer, World Wide Wait: a study of Internet scalability and cache-based approaches to alleviate it, Management Science 49 (10) (2003) 1425–1444.

[15] J. Dilley, M. Arlitt, S. Perret, Enhancement and validation of the squid cache replacement policy, Proceedings of the 4th International Web Caching Workshop 1999.

[16] T. Fagni, R. Perego, F. Silvestri, S. Orlando, Boosting the performance of web search engines: Caching and prefetching query results by exploiting historical usage data, ACM Transactions on Information Systems 24 (1) (2006) 51–78.

[17] J. Hahn, R.J. Kauffman, J. Park, Designing for ROI: toward a value-driven discipline for E-commerce system design, Proceedings of the 2002 Hawaii International Conference on System Sciences, Big Island, HI, January 2002, pp. 2663–2672.

[18] P. Jelenkovic, A. Radovanovic, Asymptotic insensitivity of least-recently-used caching to statistical dependency, INFOCOM 2003 22nd Annual Joint Conference of the IEEE Computer and Communications Societies, 2003, pp. 438–447.

[19] B. Juurlink, Approximating the optimal replacement algorithm, Proceedings of the 1st conference on Computing frontiers, 2004, pp. 313–319.

[20] B. Krishnamurthy, J. Rexford, Web Protocols and Practice: HTTP/1.1, Networking Protocols, Caching, and Traf<sup>fi</sup>c Measurement, Addison Wesley, 2001.

[21] N. Kumar, A. Gangopadhyay, G. Karabatis, Supporting mobile decision making with association rules and multi-layered caching, Decision Support Systems 43 (2007) 16–30.

[22] C. Kumar, J.B. Norris, A new approach for a proxy-level web caching mechanism, Decision Support Systems 46 (1) (2008) 52–60.

[23] M. Kurcewicz, W. Sylwestrzak, A. Wierzbicki, A <sup>fi</sup>ltering algorithm for web caches, Computer Networks and ISDN Systems 30 (22–23) (November 1998) 2203–2209

[24] J. Mardesich, The Web is no shopper's paradise, Fortune (November 8 1999) 188–198.

[25] D. Menascé, Scaling Web sites through caching, IEEE Internet Computing 7 (4) (July/August 2003) 86–89.

[26] J.M. Menaud, V. Issarny, M. Banatre, Improving effectiveness of Web caching, Recent Advances in Distributed Systems. Lecture Notes in Computer Science, vol.1752, Springer–Verlag, Berlin, Germany, 2000, pp. 375–401.

[27] V. Mookerjee, Y. Tan, Analysis of a least recently used cache management policy for Web browsers, Operations Research 50 (2) (2002) 345–357.

[28] C.D. Murta, V.A.F. Almeida, W. Meira, Analyzing performance of partitioned caches for the WWW, Proceedings of the 3rd International WWW Caching Workshop, Manchester, England, June 1998.

[29] N. Osawa T Yuba K. Hakozaki Generational replacement schemes for a WWW proxy server, high-performance computing and networking (HPCN'97), Lecture Notes in Computer Science, vol. 1225, Springer-Verlag, Berlin, Germany, 1997 pp. 940–949.

[30] S. Podlipnig, L. Bözsörmenyi, A survey of web cache replacement strategies, ACM Computing Surveys 35 (4) (December 2003) 374–398.

[31] M. Rabinovich, L. Spatscheck, Web Caching and Replication, 1st editionAddison Wesley, 2002.

[32] M. Reddy, G.P. Fletcher, Intelligent web caching using document life histories: a comparison with existing cache management, Proceedings of the 3rd International WWW Caching Workshop, Manchester, England, June 1998.

[33] R. Rizzo, L. Vicisano, Replacement policies for a proxy cache, IEEE/ACM Transactions on Networking 8 (2) (2000) 158–170.

[34] P. Scheuermann, J. Shim, R. Vingralek, A case for delay-conscious caching of Web documents, Computer Networks and ISDN Systems 29 (8–13) (September 1997) 997–1005.

[35] D. Scott, On optimal and data-based histograms, Biometrika 66 (3) (1979) 605–610.

[36] S.W. Shin, K.Y. Kim, J.S. Jang, LRU based small latency <sup>fi</sup>rst replacement (SLFR) algorithm for the proxy cache, Proceedings of IEEE/WIC International Conference, 2003, pp. 499–502.

[37] Y. Tan, Y. Ji, V.S. Mookerjee, Analyzing document-duplication effects on policies for browser and proxy caching, INFORMS Journal on Computing 18 (4) (2006) 506–522.

[38] UC Berkeley Home IP Web Traces, 2006, available at http://ita.ee.lbl.gov/html/ contrib/UCB.home-IP-HTTP.html. Last accessed on January 16, 2006.

[39] E.F. Watson, Y. Shi, Y.S. Chen, A user-access model-driven approach to proxy cache performance analysis, Decision Support Systems 25 (1999) 309–338.

[40] R.P. Wooster, M. Abrams, Proxy caching that estimates page load delays, Computer Networks and ISDN Systems 29 (1997) 977–986.

[41] N. Young, The k-server dual and loose competitiveness for paging, Algorithmica 11 (6) (June 1994) 525–541.

[42] M. Zari, H. Saiedian, M. Naeem, Understanding and reducing Web delays, IEEE Computer 34 (12) (December 2001) 30–37.

![](/api/attachments/VGQ6EZRA/fulltext/images/03cc76d4ed62be4a1ee96b78b63fcf785465f365c584c4ab0b282f957bdbd863.jpg)

Cüneyd C. Kaya received his MS in Information Technology and Management and his PhD in Management Science with Information Systems concentration from the University of Texas at Dallas. He has a BSc in Mathematics from Istanbul Technical University. His research interests are in economics of Web content distribution, performance evaluation of web proxy servers, and capacity management in content provision sites. He is also interested in information systems security and dynamics of web user communities. He is currently Manager of Decision Analysis at Blockbuster.

Guoying Zhang is an Assistant Professor of Management Information Systems at the Dillard College of Business Administration, Midwestern State University. She received her PhD in Information Systems from the University of Washington. Her research interests include information security, social networks, and economics of information systems.

![](/api/attachments/VGQ6EZRA/fulltext/images/b1e7e831a4622adc7892e1b94e0a1ea38600d1a2d1f80d5f64887d8f2bbab100.jpg)

Yong Tan is an Associate Professor of Information Systems and Evert McCabe Faculty Fellow at the Michael G. Foster School of Business, University of Washington. His research interests include electronic commerce, social networks, software engineering, and economics of information systems. He has published in Operations Research, Management Science Information Systems Research INFORMS Journal on Computing, IEEE/ACM Transactions on Networking, IEEE Transactions on Software Engineering, IEEE Transactions on Knowledge and Data Engineering, IIE Transactions, and European Journal of Operational Research. He is an associate editor of Management Science and Information Systems Research.

![](/api/attachments/VGQ6EZRA/fulltext/images/0dbd8c9c64fae4ee3583e52b44ea8f9e309aba324d17f66bc444828f7d589b48.jpg)

Vijay S. Mookerjee is the Charles and Nancy Davidson Distinguished Professor of Information Systems at the School of Management, University of Texas at Dallas. He holds a Ph.D. in Management, with a major in MIS. from Purdue University His current research interests include optimal software development methodologies storage and cache management, and the economic design of expert systems and machine learning systems. He has published in and has articles forthcoming in several archival Information Systems, Computer Science, and Operations Research journals. He serves on the editorial board of Management Science, Information Systems research, INFORMS Journal on

Computing, Operations Research, Decision Support Systems, Information Technology and Management, and Journal of Database Management.
