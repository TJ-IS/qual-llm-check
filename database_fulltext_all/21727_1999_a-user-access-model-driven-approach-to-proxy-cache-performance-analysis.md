---
otero_id: 21727
otero_key: "HUGGV76D"
title: "A user-access model-driven approach to proxy cache performance analysis"
authors: "Edward F Watson; Ying Shi; Ye-Sho Chen"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00017-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A user-access model-driven approach to proxy cache performance analysis

Edward F. Watson <sup>)</sup>, Ying Shi <sup>1</sup>, Ye-Sho Chen <sup>2</sup>

Department of Information Systems and Decision Sciences, E.J. Ourso College of Business Administration, Louisiana State UniÕersity, 3190 CEBA Building, Baton Rouge, LA, 70803-6316, USA

Accepted 11 February 1999

## Abstract

World-Wide Web usage has experienced tremendous growth in recent years. This growth has resulted in a significant increase in network and server loads that have adversely affected user response times. Among many viable and available approaches to reducing user response time, Web caching has received considerable attention. The purpose of this paper is to present an empirically derived model of Internet user-access activity, and to demonstrate its usefulness for conducting model-driven discrete simulation studies of cache performance analysis. The user-access model is shown to be a reasonable representation of Internet activity, and the user-access approach to cache performance analysis is shown to be a favorable alternative to trace-driven simulation. A report on the accuracy of the model and a summary of the findings are presented. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Internet; Network cache policy; Model-driven simulation; User-access patterns

## 1. Introduction

The World-Wide Web a.k.a. WWW, the ‘web’,Ž the ‘net’, and W3 has experienced exponential . growth in recent years. This growth has created a tremendous increase in network loads that have subsequently affected user response times. Increased user response times have caused many web users to cynically refer to the WWW as the world-wide-wait <sup>w</sup> <sup>x</sup> 2 . This growth shows no signs of diminishing especially as new applications of electronic commerce appear. This demand has motivated many research efforts aimed at improving WWW performance 39 . One way to enhance WWW perfor-<sup>w</sup> <sup>x</sup> mance is through technology innovation such as two-way cabling, digital subscriber lines, satellites, dual-line modems, and platform upgrades 37 . But it is realistic to expect that demand for the WWW will continue to be greater than supply for some time despite continuous WWW bandwidth upgrades. Other approaches to WWW performance enhancement referred to as ‘quick and dirty’ approaches 11 include <sup>w</sup> <sup>x</sup> traffic management, toll roads, load balancing and caches. WWW caching has been identified as an important and promising area of research 25 . This<sup>w</sup> <sup>x</sup> paper addresses the problem of analyzing web-based cache management policies and proposes the use of a model-driven approach, based on a user-access model, for cache policy analysis. We are specifically interested in how to improve decision support for WWW cache management.

## 1.1. WWW cache performance

The WWW is based on a client–server model. A Web browser is used by a client to access documents stored on one of many Web servers. A Web server responds to requests for documents made by the browser. Communication is always in the form of request–response pairs, and is always initiated by the client. Web clients and servers communicate using the HyperText Transfer Protocol 3 .<sup>w</sup> <sup>x</sup>

A cache is nothing more than a computer storage medium where certain documents are stored often based on the frequency or recency of document usage. The cache maintains a copy of certain documents from remote servers so to reside geographically closer to clients. This can reduce the transmission distance significantly and may result in a reduction in network load, Web server load, and user response time.

Several metrics are commonly used when evaluating web cache performance 2 . The<sup>w</sup> <sup>x</sup> hit rate Ž .HR is generally the ratio of documents obtained through using the caching mechanism vs. the total documents requested. It is often expressed as a percentage of document requests that are satisfied by the cache inventory. A high HR reflects an effective cache policy. If the documents are homogeneous in size, this measure may be a reasonable measure of effectiveness. If the documents are of varying sizes, weighted hit rate WHR is a better performance Ž . measurement 1 . WHR is defined as the ratio of the<sup>w</sup> <sup>x</sup> number of bytes loaded from the Cache to the total number of bytes accessed. Bandwidth utilization is another measure where the obvious objective is to reduce the amount of bandwidth consumed. A fourth measure is user response time i.e., the time a userŽ waits for the system to retrieve a requested document . Although these measures are related, optimiz- . ing one measurement may not optimize another 4 .<sup>w</sup> <sup>x</sup> An increase in HR, for instance, does not necessarily result in reduced network traffic.

Various factors affect Web cache performance. The behavior of the user population that request documents from the cache is characterized by the user-access pattern. If a user accesses a small number of documents most of the time then these documents are obvious candidates for caching. Useraccess patterns are usually not static and this implies that an effective cache policy should not be static.

Web cache remoÕal policies are the rules that dictate which document to remove when the cache is full. They are the subject of Section 1.2. The cache remoÕal period dictates at what point in time may a document s be removed. AŽ . continuous removal period implies that documents will be removed when there is no space in the cache to hold the actiÕe document. The active document is the document currently being accessed. A fixed cache removal period indicates that documents will only be removed at the beginning of the removal period.

Cache size is another factor influencing cache performance. Intuitively, the larger the cache size is the more documents it can maintain and the higher the cache HR is. However, cache space is expensive. Therefore, an optimal cache size involves a trade-off between cache cost and cache performance HR . Ž . Document size is also associated with cache performance. Given a certain cache size, the cache can store more small sized documents or fewer large sized documents. Maximum cacheable document size Ž . threshold is a user-defined factor that places a ceiling on the size of the documents that are allowed to be stored in the cache.

A cache may actually appear at three locations on a network. A client cache Žalso referred to as a browser refers to a Web browser with caching that. stores not only the documents currently displayed in the browser window but also documents requested in the past. An example of client cache is the cache built into Netscapee. A proxy cache Ži.e., a proxy cache server refers to a cache that is located in a. server on the path from multiple clients to multiple servers 23 . An example of caching proxies is the <sup>w</sup> <sup>x</sup> CERN proxy server 16 . The proxy cache server <sup>w</sup> <sup>x</sup> receives URLs generated by multiple clients and then checks if the requested document is stored. It is possible to use proxy caches hierarchically, so that a proxy cache receives document requests from other proxy caches. A serÕer cache Ž . i.e., site cache refers to caching at the remote servers and although it does not result in reduced network load it does tend to reduce the load on the remote server. In terms of reduction of network traffic congestion and user response time, these three kinds of the web caches have different effects. Caching documents at the client is only effective for the specific user. Caching at the original server site can reduce disk access latency, thus reducing response time, by using main memory. When a document is available in the proxy cache, the response time is likely to be much shorter than accessing the remote server. In addition, if the proxy cache results in many hits then the network traffic and remote server load are reduced.

Web browsers are configured to send requests to local proxy cache servers. When a document is first requested, the proxy cache server acts as a web user to retrieve the object and return it to the user. The document is saved by the proxy cache server, and if another user requests the same document, the proxy cache acts as a server and returns the cached copy to the user 21 . We can see that for distant documents<sup>w</sup> <sup>x</sup> a proxy cache server can result in an improved user response time if the documents are cached. If the documents are not cached then the response time may be slightly impaired due to the involvement of the proxy server. For documents located close to the user, however, use of the proxy cache does not have particular benefit. To avoid this problem, a web browser can be configured with a list of domains from which a user would frequently retrieve preferred documents directly.

Two cache factors that are not addressed in this paper include cooperation and consistency. Cooperation refers to the coordination of user requests amongst many proxy caches in a hierarchical proxy cache environment 12,17,21 . Cache consistency<sup>w</sup> <sup>x</sup> refers to maintaining copies of documents in cache that are not outdated e.g., stock market quotes 13 .Ž . <sup>w</sup> <sup>x</sup> There are other factors that indirectly affect proxy cache performance. For example, protection copyright security increases the complexity of proxy Ž . cache design. Uncacheable documents i.e., Pay- Ž Per-View are also a potential concern. .

## 1.2. Cache remoÕal policy reÕiew

As Web popularity grows, the network bandwidth required to connect users to web sites has increased.

Since the strategy of increasing network bandwidth to keep up with user demand is very expensive, people attempt to increase cache size to improve user response time since a larger cache will store more documents. But Web cache is a scarce resource on the Internet and only partially contributes to the improvement of cache performance. Research shows <sup>w</sup> <sup>x</sup> 1,19,38 that an increase in cache size will improve HR up to some threshold whereby additional cache size increases will only marginally improve cache HR. Markatos 19 found that the web server envi-<sup>w</sup> <sup>x</sup> ronment also has an effect on cache HR. He reported that a cache as small as 4 MB megabytes resultedŽ . in a 80% HR for the NCSA server, but only a 63% HR for the Parallab server.

Unlike a CPU cache, which stores homogenous size program blocks, Web cache stores documents of various sizes. Several studies 1,9,19,38 have inves- <sup>w</sup> <sup>x</sup> tigated the influence of document size on cache performance. The results are roughly the same. Caching small documents and removing large documents result in higher HRs. Results may vary depending on what maximum cacheable document size is assumed.

Web cache removal policies vary in complexity depending on what factors are considered by the policy. Williams et al. 38 and Markatos 19 point<sup>w x</sup> <sup>w x</sup> out that heterogeneous document sizes and types allow for a rich variety of policies. The most common web cache removal policies are FIFO first-in-Ž first-out , LFU least frequently used , LRU least. Ž . Ž recently used , and SIZE documents are removed. Ž according to document size . The FIFO, LFU and. LRU policies are borrowed from CPU cache policies while the SIZE policy is proposed by Williams et al. <sup>w</sup> <sup>x</sup> 38 .

In studies reported by Recker and Pitkow 28 ,<sup>w</sup> <sup>x</sup> recency was shown to be a stronger predictor than frequency. These studies show that a mean HR of between 67% and 69% could be achieved by simply caching only the documents accessed 1 day ago. This observation is also made by Wessels 33 who indi- <sup>w</sup> <sup>x</sup> cates that those documents accessed on any given day are likely to be accessed on the next day but those documents that are accessed on the previous day or earlier have a lower probability of being accessed on the next day. Therefore, the results of Pitkow and Recker, and Wessels imply that LRU

Ž . Ž recency based policy is better than LFU frequency based policy . Though, these results are only relevant. to the environment e.g., user-access pattern in whichŽ . the experiment was conducted.

The poor performance of LFU is in part due to the fact that once the cache stores a set of highly accessed documents, those documents are rarely removed. As the access pattern changes with time, the Ž . previously popular documents may not be accessed again but will remain in the cache for some time. The LFU-aging policy, proposed by Arlitt and Williamson 3 attempts to reduce the priority of a <sup>w</sup> <sup>x</sup> document that has not recently been accessed but that still has a high frequency associated with it.

Abrams et al. 1 monitor traffic corresponding to<sup>w</sup> <sup>x</sup> three types of educational workloads over a onesemester period and used this as input to a cache simulation. They report that when the cache is full and a document is removed, the LRU removal policy performs poorly. Based on the LRU policy they propose two cache removal policies LRU-min andŽ LRU-thold , that were shown to be better than the. LRU policy. The poor performance of the LRU policy in the study by Abrams et al. 1 may be attributed to ‘persistent’ users. If the majority of users persistently retrieve certain documents frequently then a frequency based cache policy may be better than a recency based policy. It is apparent that user access pattern is clearly an important factor and one which should be considered during the web cache removal policy analysis.

Williams et al. 38 propose a removal policy <sup>w</sup> <sup>x</sup> based on document size called SIZE. The SIZE removal policy means that when the cache is full the largest or smallest document in the cache should be Ž . removed. Through trace-driven simulation they attempt to determine the maximum possible HR and WHR that a cache could ever achieve and the removal policy that maximizes HR and WHR. The experiments used five traces of 37 to 185 days of client requests. The results are that removal policy based on SIZE always outperforms any other removal policy. Based on these simulation experiments, they rank HR performance of several removal policies in the following order best first : SIZE,Ž . LRU, LFU.

Abrams et al. 1 argue that LRU may discard<sup>w</sup> <sup>x</sup> many small documents to make room for one large document, resulting in misses for many users. Two new hybrid algorithms are proposed based on LRU: LRU-min and LRU-thold which try to minimize the number of documents replaced. The principle of LRU-min is to apply LRU only to the largest documents and then to groups of successively smaller documents. The LRU-thold policy is different from LRU in that no document larger than a threshold size is cached.

Common cache policies use heuristic rules that lack a mathematical or empirical foundation 10,<sup>w</sup> 16,27 . Web system administrators and browser<sup>x</sup> users arbitrarily define certain important, hard-coded caching parameters such as the primary and secondary cache policy, the time-to-live for cached files, and the maximum file size allowed in the cache. Typically, such systems perform sub-optimally, averaging HRs below 55%. Commercially available Web caching software continue efforts to improve this performance 34–36 .<sup>w</sup> <sup>x</sup>

A user access model is an important consideration when designing caching schemes. A model attempts to characterize how the user will access web documents. By knowing the user access pattern, better caching predictions can be made as to what documents will be requested. However, the conventional web cache policy studies assume a trace-driven simulation approach that lacks the capability to extract and represent the dynamic aspects of user access patterns. Previous studies 9,10 of user access pat-<sup>w</sup> <sup>x</sup> terns use simple statistical methods such as log data distributions and histograms. Several authors <sup>w</sup> <sup>x</sup> 2,19,27,38 have evaluated the impact of various factors on web cache performance with inconsistent results. In Section 2, a model for WWW user-access patterns is proposed. This model is then used in a model-driven simulation to evaluate various cache removal policies under different environments.

## 2. User access modeling

The objective of user access modeling is to find a mathematical based model that accurately represents the user access pattern of WWW clients. The vast majority of cache policy research utilizes trace-based simulation where each simulation is based on a specific user-access log trace. This makes experimentation and the generalization of experiments very difficult. A mathematical model of user-access activity facilitates experimentation and helps to better understand how to develop efficient Web cache policies. This section begins with a look at the user-access logs used to evaluate the model. Some background work in this area is presented. A user-access model based on Simon’s information processing model is proposed.

## 2.1. Workload traces: obtaining user access logs

In this study, four workload traces are used. Two workload traces are proxy-based, one being similar to a client-based trace and the other being similar to a server-based trace. The two other work loads are single server-based traces. A summary of this data is presented in Table 1. Two proxy-based traces studied collected for this study from a University Web site Ž . Virginia Tech were previously used by Williams et al. 38 in their cache removal policy study<sup>w</sup> <sup>x</sup> Ž . ftp:<sup>rr</sup>ei.cs.vt.edu<sup>r</sup>pub<sup>r</sup>succeed<sup>r</sup>Sigcomm96 . The details about the workloads are available in their paper. One of the workloads is called ‘remote client backbone accesses BR ’. BR records the accessŽ . activity of world-wide clients to several web servers in their computer science department. This workload includes every URL request appearing on the Ethernet backbone of domain .cs.vt.edu with a client outside that domain naming a web server inside that domain for a 37-day period in September and October 1995. There are a total of 227,210 requests made in that time period and that require a 9.38 GB log transmission. Two 1-week periods of trace data Oc-Ž tober 1 to October 7 and October 15 to October 21. are downloaded and used to validate the user-access model. The other workload is called ‘local client backbone accesses BL ’. The BL workload is aŽ . collection of the accesses of the department client requests to any outside server in the world for a 37-day period in September and October 1995. This represents 91,188 accesses requiring a transmission of a 641.8 MB log. Two 1-week periods of trace data ŽOctober 1 to October 7 and October 15 to October 21 are downloaded and used to validate the user-. access model.

The single server-based traces are obtained from Louisiana State University LSU library web serversŽ . Ž . http:<sup>rr</sup>www.lib.lsu.edu<sup>r</sup>stats<sup>r</sup>usage.html and the core resource web server at Columbia University Ž . www.cis.columbia.edu<sup>r</sup>stats.htmlaArchive . The workload traces from LSU cover all the user accesses in July of 1996, representing 329,385 total requests to 2457 static web pages on LSU library servers. The workload traces from Columbia cover all the user accesses over a 2-month period in 1996, representing 156,926 total requests to 508 static web pages.

Table 1  
Summary of access log characteristics

<table><tr><td>Item</td><td>Virginia Tech (BL)</td><td>Virginia Tech (BR)</td><td>LSU Library</td><td>Columbia University (Core Resource)</td></tr><tr><td>Category</td><td>Proxy-based (or client-based) workload</td><td>Proxy-based (or server-based) workload</td><td>Single server workload</td><td>Single server workload</td></tr><tr><td>Access log during</td><td>2 weeks</td><td>2 weeks</td><td>1 month</td><td>2 months</td></tr><tr><td>Access log start date</td><td>October 1–October 7, 1995; October 15–October 21, 1995</td><td>October 1–October 7, 1995; October 15–October 21, 1995</td><td>July 1996</td><td>April 12, 1996</td></tr><tr><td>Total documents requested</td><td>16,427</td><td>8893</td><td>2457</td><td>508</td></tr><tr><td>Total requests</td><td>31,145</td><td>83,125</td><td>329,385</td><td>156,926</td></tr><tr><td>Average requests/day</td><td>2225</td><td>5938</td><td>10,625</td><td>2242</td></tr><tr><td>Bytes transferred (MB)</td><td>243</td><td>3549</td><td>7501</td><td>1796</td></tr><tr><td>Average bytes/day (MB)</td><td>17</td><td>253</td><td>242</td><td>25</td></tr></table>

Ž . 1 Client-based log: logs collected by instrumenting a set of web clients.  
Ž . 2 Multiple web server logs: logs collected by monitoring traffic from clients throughout the Internet to a few servers.  
Ž . 3 Single web server logs: logs collected from individual web servers.

## 2.2. Empirical eÕidence of web user-access actiÕity

Determining WWW user-access patterns is an area of active research. Three basic models of useraccess patterns reported in the literature are briefly reported here: the Pareto distribution, the psychological human memory model, and a simple proxy cache metric.

## 2.2.1. The Pareto distribution model

The Pareto distribution also referred to as theŽ power-law distribution, the double-exponential distribution, and the hyperbolic distribution has been . used to model various phenomena such as the distribution of income 24 and firm size growth 30 . The <sup>w x</sup> <sup>w x</sup> Pareto distribution has a hyperbola shape 9 and its <sup>w</sup> <sup>x</sup> probability mass function and cumulative distribution functions are

$$
p (x) = a k ^ {a} x ^ {- a - 1},
$$

and

$$
p \big [ X \leq x \big ] = 1 - \big (k / x \big) ^ {a}, \quad a, k \geq 0,   x \geq k.
$$

respectively. The parameters a and k are shape parameter and location factor, respectively. $\operatorname { I f } \left( 2 \geq a \right) $ then the distribution has infinite variance, and if $\left( 1 \geq a \right)$ , then the distribution has infinite mean. The heavy-tailed Pareto distribution a large portion ofŽ the probability mass is present in the tail of the distribution is defined as below if:.

$$
P \big [ X \geq x \big ] \approx c x ^ {- a}, \quad \text { as } x \to \infty , \alpha \geq 0.
$$

Cunha et al. 9 investigate user-access patterns<sup>w</sup> <sup>x</sup> based on over half a million accesses and show that many web access characteristics can be modeled using the heavy-tailed Pareto distribution. This includes the distribution of document sizes, the distribution of user requests for documents, and the number of accesses to documents as a function of their overall rank in popularity. The major findings, from their study, about user access pattern are:

1. the relationship between accesses to document Ž . Ž . y and document ranking x is

$$
y = - 0. 9 8 6 x ^ {- 1} \quad R ^ {2} = 1. 0 0,
$$

2. the relationship between accesses to document Ž . Ž . y and document size z is

$$
y \propto z ^ {- 1. 6 6} \quad R ^ {2} = 0. 8 9, \text {   and   }
$$

3. the relationship between the number of documents Ž . Ž . w vs. document size z is

$$
w \propto z ^ {- 1. 3 5} \quad R ^ {2} = 0. 9 6.
$$

Markatos 19 gathered several web server traces<sup>w</sup> <sup>x</sup> from a variety of environments that include universities, research institutions, and supercomputing centers from Europe and the United States. The study indicates that the number of accesses to documents depends on the environment or the server. From this research it is clear that HR is not only a function of cache size, but also affected by the web server’s environment. As explained in the paper, the 10 most frequently accessed documents in NCSA server are responsible for almost 50% of the accesses, while the 10 most frequently accessed documents in Parallab server are responsible for roughly 10% of the accesses. Glassman 10 set up a web proxy cache for<sup>w</sup> <sup>x</sup> Digital Equipment’s facilities in Palo Alto, CA, which handled about 2000 requests from 60 users each day. The ratio of the number of requests made by the ith most frequent user to the Ž . i <sup>q</sup> 1 -st most frequent user is approximately 1.02. The plot of user requests and rankings is approximately log–linear.

## 2.2.2. The psychological memory model

Recker and Pitkow 28 propose a user access<sup>w</sup> <sup>x</sup> model that is derived from psychological research on human memory. This psychological model focuses on frequency and recency of user access patterns. To the best of our knowledge, this model is the only dynamic model of user access pattern in all published research to date. In their paper Recker and Pitkow explain that recency probabilities are computed like frequency probabilities. This research shows that document access can be predicted by using a model combining document frequency and recency. The cache performance studied in the paper has been improved from below 55% to 67% HR for accesses from off-campus for a 3-month period. However, this model is obtained through a regression analysis of actual access data using a rolling-horizon approach. As such, this model only describes the general behavior of user accesses and it cannot be used to simulate user access behaviors. A user access model is needed that not only provides a good approximation of user access behavior, but also provides a good mechanism to generate user access behaviors. As well, Recker and Pitkow state that the relationship between recency and frequency in predicting document access remains unclear.

## 2.2.3. The proxy cache metrics model

Wessels 33 found that cached documents can be<sup>w</sup> <sup>x</sup> prioritized based on a simple metric. Three factors are considered in the metric: frequency, recency, and size. For these calculations, the administrator has to set a window size which typically is 1 week. Frequency is calculated in units of accesses per day. Given the number of accesses $( N )$ , the time of earliest access $( T _ { 1 } ) _ { \cdot }$ , the time of most recent access $( T _ { 2 } )$ , and the current time $( T _ { 0 } )$ Ž . , then frequency F , recency Ž . R , and a metric M are defined as:

$$
F = N / \left(T _ {2} - T _ {1}\right)
$$

and

$$
R = T _ {0} - T _ {2}.
$$

$$
M = F ^ {f} R ^ {r} S ^ {s}
$$

where S represents the document size and $f , r ,$ and s are exponents chosen by the administrator. But in this paper no attempt is made to determine how to estimate $f , r ,$ and s.

Arlitt and Williamson 3 make five key observa-<sup>w</sup> <sup>x</sup> tions regarding user behavior on the Web. First, there is an extremely high concentration of Web server requests to a small set of highly popular documents. This suggests that a maximum cacheable document size would tend to be small to avoid caching large documents that are not accessed frequently, or at all, after the initial request. Second, there is a distinct difference between designing a Web server cache to maximize cache HR vs. designing a Web server cache to minimize bytes transferred Ž . i.e., data volume . For instance, maximum cache HR would be desirable to the user and would imply that smaller documents should be cached agreeing Ž with the first observation . Third, the document ac-. cess patterns found in Web server access logs show little temporal locality. This confirms the idea that user-patterns are constantly changing and that a cache policy must be able to adapt to this change. Fourth, many Web server documents are accessed only once, the distribution of document sizes of Web servers is heavy tailed. A user-pattern generating mechanism should be able to deal with this phenomenon. Finally, different document types e.g., HTML, image,Ž audio, video, and postscript have different size char-.

acteristics and access frequencies. Many of the larger file types are not stored in cache nor subject to frequent updates.

The research discussed in this section sends a consistent message regarding document accesses: the Pareto distribution is a good approximation of document access number. These studies provide good empirical evidence that describe common user-access patterns. However, they do not indicate the mechanism for generating such a pattern in a model-driven simulation study. To address this issue we propose the development of a user-access model.

## 2.3. Simon’s information processing model

Determining user access patterns for Web sites is an area of active research since it can lead to improved cache performance and user-response time. Empirical studies of web site user activity have been reported in the literature for the size distribution of documents available on the web 9 , the requests<sup>w</sup> <sup>x</sup> made by users 10,19 , and of the relationship be-<sup>w</sup> <sup>x</sup> tween document size and popularity 9 . Two power- <sup>w</sup> <sup>x</sup> law distributions, Zipf’s law of word frequency 41 <sup>w</sup> <sup>x</sup> and Pareto’s law of income distribution 24 stand<sup>w</sup> <sup>x</sup> out as the leading empirical distributions for Web site activity 7 .<sup>w</sup> <sup>x</sup>

In their comprehensive review on information productivity modeling Chen and Chong 6 examine<sup>w</sup> <sup>x</sup> two distributions, Zipf and Pareto, and other related empirical laws in information processing. The primary goal of their study is to develop a theoretical foundation for the empirical phenomena and show its implications in describing how a very large data base, such as a document-based data base, would change oÕer time. They compare several leading generating mechanisms of the empirical laws, including the multinominal urn model, the Markov chain <sup>w x</sup> <sup>w x</sup> 20 , Mandelbrot–Shannon model 18 , and the Simon–Yule model 30 . They conclude that the Si-<sup>w</sup> <sup>x</sup> mon–Yule model is the most promising approach to explain and generate the empirical laws.

The Simon–Yule model began as a generalization of the Markov chain model in 1955 30 . According<sup>w</sup> <sup>x</sup> to Simon the stochastic process by which words i.e.,Ž word usage are chosen is a two-fold stochastic. process that includes association and imitation. A person selects what to use according to what he has used before and what others are using imitation , asŽ . well as what he has just recently used association .Ž . Simon states this selection process in the following assumptions, where $f ( n , t )$ is the number of different words that have occurred exactly n times in the first t words.

Ž . 1 There is a constant probability, , that the Ž . t<sup>q</sup>1 -st word be a new word—that is, a word that has not occurred in the first t words.

Ž .2 The probability that the $( t + 1 ) { \mathrm { - s t } }$ word is a word that has appeared n times is proportional to $n f ( n , t )$ ; that is, to the total number of occurrences of all the words that have appeared exactly n times.

Based on the two assumptions, Simon derived

$$
h (n) = \rho B (n, \rho + 1),
$$

where $h ( n )$ is the expected relative frequency of words appearing n times, $\rho = 1 / ( 1 - \alpha )$ and $B ( n , \rho$ $^ { + 1 ) }$ is the Beta function with parameters n and $( \rho + 1 )$ 5 . Simon calls the last equation a Yule <sup>w</sup> <sup>x</sup> distribution because Yule’s paper 40 , which pre- <sup>w</sup> <sup>x</sup> dated the modern theory of stochastic processes, derived the same equation in a study of biological problems. Simon’s model is frequently cited as the Simon–Yule model.

Simon presents three models 14,29 . The Version<sup>w</sup> <sup>x</sup> I model assumed a constant entry rate of new words. That is, the entry rate of new words is assumed to be constant, thus independent of the total number of works, $k , \ k = 1 , \ 2 , . . . , \ N$ that have been selected. Simon refines the Version I model making VersionŽ II by making. Ž . dependent on k, k . That is, there is a decreasing probability function $\alpha ( k ) , 0 \leq$ $\alpha ( k ) \leq 1$ Ž , that the kth word is a new word i.e., decreasing entry rate . However, the Version II model . did not take into account the possibility that words not used have a tendency of being ‘forgotten.’ In other words, the probability of using the particular word will decrease with time if the word is not in use i.e., auto-regressive growth . Simon refined hisŽ . first two models to account for this auto-regressive growth 14 . In the auto-regressive model, the iden-<sup>w</sup> <sup>x</sup> tity of each word is maintained from one time period to the next. The word selection process is now governed by a stochastic process that depends on <sup>w</sup> <sup>x</sup> 15 the number of times a word has been used before, and also 22 the time that has elapsed since<sup>w</sup> <sup>x</sup> it was last used. For simplicity, Simon assumed that only one word was selected in each time period. The probability that a word will be used next is assumed to be proportional to a weighted sum of its usage history, where the weight of a usage decreases geometrically, at a rate $\gamma ,$ from the time it was last used.

Simon formalizes the Version III model as follows. Let $y _ { j } ( k )$ be the indicator of the access of the jth document during the kth time interval, where $y _ { j } ( k )$ Žis either 1 or 0 1<sup>s</sup>the document is accessed, and 0<sup>s</sup>the document is not accessed . Then the. total number of accesses of the jth document at the end of the k th time interval is simply $\scriptstyle \sum _ { \tau = 1 } ^ { k } y _ { j } ( \tau )$ The probability of accessing the jth document at the $( k + 1$ . th access can be formalized as:

$$
p \left[ y _ {j} (k + 1) = 1 \right] = \frac {1}{W _ {k}} \sum_ {\tau = 1} ^ {k} y _ {j} (\tau -) \gamma^ {k - \tau}
$$

where $W _ { k }$ is the sum of weighted usage of all documents, which is a function of time k and is the same for all documents; $\gamma$ is the parameter that determines how rapidly the influence of past accesses on a new selection dies out.

Simon’s simulation results closely resemble the historical data sampled, hinting that his model provides considerable insight into how these empirical data are generated in their considerably diverse environments. Version III of Simon’s model is illustrated in Appendix B.

## 2.4. Estimating Simon’s model parameters

In order to use a user-access model in a modeldriven simulation experiment there must generating mechanism for the user accesses for Web documents. The user-access generating algorithm used in this paper was developed by Simon and Van Wormer <sup>w</sup> <sup>x</sup> 29 for their study of firm size growth. This model requires two parameters, and . The estimation of these parameters and an evaluation of their accuracy is presented below. Since it is observed that web access closely follows a Pareto distribution the next step is to determine if, under the two assumptions of new entry and autocorrelation, the generated data still has a Pareto distribution. This is the objective of the Monte Carlo simulation.

## 2.4.1. Simon’s model parameters $( \alpha , \gamma )$

Ijiri and Simon 14 explain the technique for <sup>w</sup> <sup>x</sup> estimating  Ži.e., the probability of a new docu-

ment entry in their research. Thus, the value of. is approximately equal to $R / T ,$ where R is the total number of different documents accessed and T is the total number of documents. The ability to approximate the value of from $R / T$ is an intuitive relationship. It is known that  is the probability of the entry of a new document. Therefore, the total number of different document accesses should be the product of T and . For the LSU data set $\alpha { = } R / T$ $= 2 4 5 7 / 3 2 9 , 3 8 5 = 0 . 0 0 7 2 5 9 4 ,$ , and for Columbia University $\alpha = R / T = 5 0 9 / 1 5 6 , 9 2 6 = 0 . 0 0 3 2 4 4 .$

Tong 31 used the slope of the Pareto curve to<sup>w</sup> <sup>x</sup> estimate , but the estimated results were not good. Instead, a response surface approach is used to estimate this parameter as illustrated in Fig. 1. To improve the  estimate, Pareto curves for different

![](/api/attachments/HUGGV76D/fulltext/images/ea10649d2f8fa27395e6c57fb7019165c1247591c6c78fa8346a9b911339507c.jpg)  
Note: 1) Index Approach (Chen and Leimkuhler, 1986):

It is a method to take the scattering pattern of observerd values into account, and calculate the Pareto curve area.

2) Simon's Simulation:

A algorithm proposed by Simon and Yule (1963) to simulate a stochastical process in text generation.

Fig. 1. Comparing actual vs. simulated web access pattern.

combinations of and are generated. The Index Approach 8 summarized in Appendix C is used to<sup>w</sup> <sup>x</sup> calculate the area under the curve. A discrete table is populated with values of Area for combinations of and . From this table of values a regression response surface is constructed for the curve’s area. The details surrounding this analysis is contained in Appendix D. Given some , a one-to-one relationship between and Area is assumed. This relationship is found to be sufficient for approximations. The equation is used to estimate the  web access data given the  calculated from the raw data and the Area calculated from the raw data using the Index approach. The estimated of the LSU Web data and the Columbia Web data are 0.99 and 0.96, respectively. The estimated $\alpha$ and  are used as input to Simon’s model to generate simulated Web data. The simulated curve can then be graphically compared to the actual curve.

## 2.4.2. The impact of parameters and on the Pareto shape

Fig. 2 shows the significant role the new document entry rate plays on shaping the Pareto curve. Specifically, as  decreases, the graph curves more to the northwest direction. As  increases, the graph curves more to the y<sup>s</sup>x line. This indicates that with a lower probability of new document entry there are more requests for existing documents, and a significant few documents account for most of the requests. On the other hand, with a higher , the document request are often to new documents, the total requests are then spread over more documents, and the curve tends not to resemble the Pareto principal.

The Impact of α on Pareto Curve (γ =1, T=10000) Top down: α=0.01, 0.18,0.5,0.8,0.9)  
![](/api/attachments/HUGGV76D/fulltext/images/a353713bc9a0458fc6d489a652cc4b15518b38125c567f42a11d6a2a62f5661f.jpg)  
Fig. 2. The impact of  on Pareto curve.

![](/api/attachments/HUGGV76D/fulltext/images/5bbf14524b099cf7cc9c404c34d929c22f33a2a5eb41f1a031644b9e082095a0.jpg)  
Fig. 3. The impact of on the Pareto curve.

From Fig. 3 one can observe that a higher means a slower rate of decay, i.e., a document’s usage probability is less affected by it not being used. Thus, when $\gamma = 1 . 0 ;$ , there is no decay taking place at all and document requests for that document never go away the result is the same as considering Ž only. On the other hand, a small implies that documents that have not been used recently are likely to be neglected for a long time regardless of how active they had previously been. A related interpretation is that previously inactive documents do have a chance to become dominant in the future selection process even if this dominance is temporary. The curves in Fig. 4 indicate that under most circumstances, this interpretation is plausible. However, when varies from 0.01 to 0.5 and is held at 0.18, the curve shape is almost identical. This means that document requests are not sensitive to in the range of 0.01 to 0.5, when is 0.18.

## 2.5. Simon’s algorithm

In their articles on text generation and firm size growth Simon and Van Wormer 29 and Ijiri and<sup>w</sup> <sup>x</sup> Simon 14 argue that the use of computational ex-<sup>w</sup> <sup>x</sup> perimentation is necessary to study text generation and firm size growth. Computational experiments allow them to go beyond the analytical methods available. The simulation algorithm proposed by Simon and Van Wormer can be programmed on a computer to simulate empirical web access data.

Using the notation defined in the Simon’s model, we can describe the two steps of the simulation algorithm of the model version III as follows.Ž .

Step 1. For the kth document selection $( 1 \leq k \leq$ N ., we generate a random number a from the uniform distribution with range 0 to 1. If $a \leq \alpha$ Žthe probability of document entry , then we declare that . this is an access to a ‘new’ document never ac-Ž cessed before ; otherwise, we consider this access to. an ‘old’ document accessed before and go to Step Ž . 2.

![](/api/attachments/HUGGV76D/fulltext/images/f63afec51d5680dd45b546e22b61a7863f558f21e43338d83a3c395960edfc93.jpg)  
(a)

![](/api/attachments/HUGGV76D/fulltext/images/92025b7478fa733c75b8a81526a8fb7cd3e296b6036791dfd58523e97a8d1943.jpg)  
(b)  
Fig. 4. VT local clients backbone accesses simulation.

Step 2. A random number, b, is drawn from the uniform distribution with the range $1 \leq b \leq W _ { k }$ Žtotal weighted usage . Starting with. $n = 1$ , the cumulant of ${ \bar { \Sigma } } _ { \tau = 1 } ^ { k } y _ { j } ( \tau ) { \overline { { \gamma } } } ^ { k - \tau }$ is computed and compared to b until a j is found that ${ \textstyle \sum _ { n = 1 } ^ { j } \sum _ { \tau = 1 } ^ { k } y _ { j } ( \tau ) \gamma ^ { k - \tau } \ge b }$ . We then set $y _ { j } ( k ) = 1$ ; that is, the k th access is accessed to the jth document.

In this algorithm the two parameters  and have opposite effects on the Pareto curve. Basically, small induces a higher concentration of web accesses while small Ž . higher ‘forgetfulness’ induces a lower concentration. In our simulation study the parameter  estimated from Virginia Tech proxy cache access data is usually large approximately in Ž the range of 0.1 to 0.6 , since the clients access . documents world-wide Ž is approximately equal to the ratio of total documents to total accesses in a period of time , or remote clients in the world ac-. cessed the documents located on the different web servers at Virginia Tech. If is large, it means that clients are likely to access documents that have not been accessed previously. However, in a group of clients, perhaps there are some clients who are likely to concentrate their accesses to their preferred documents rather than to new documents. In the simulation study, it was found that even a large $\gamma ( \gamma = 1 )$

still cannot represent this concentration attributed to a small group of clients. In order to solve this problem the algorithm is modified a bit. A coefficient $( 1 - 0 . 2 5 \alpha )$ is used to reduce the uniform distribution range $1 \leq b \leq W _ { k }$ Ž . step 2 . The range becomes: $1 \leq b \leq W _ { k } \left( 1 - 0 . 2 5 \alpha \right)$ . The larger gets, the smaller the range is. The reduction of the uniform distribution range results in a concentration of accesses. This eliminates the problem that  does not have sufficient power to control the concentration of accesses when is large.

## 2.6. Results from user access pattern simulations

In order to validate Simon’s model as a web user access model we use the simulated data to compare with the empirical access data obtained from a Virginia Tech proxy cache local clients backbone ac-Ž cesses , Virginia Tech proxy cache remote clients. Ž backbone accesses , LSU library web server, and . Columbia University. These four set of empirical access data represent four different users access patterns.

## 2.6.1. VT proxy cache access simulation local clients( backbone accesses)

Two sets of empirical data of VT local clients backbone accesses are simulated; these represent 1Ž . 15,894 accesses to 8187 documents from October 1 to October 7, 1995 and 2 15,251 accesses to 8240Ž . documents from October 15 to October 21, 1995. This access data represents a group of client accesses to web pages throughout the world. Simon’s model parameter estimates from the two sets of empirical data are: $\alpha = 0 . 5 1 5 1$ $\gamma = 1$ October 1–7, 1995 ,Ž . and $\alpha = 0 . 5 4 , \gamma = 1$ October 15–21, 1995 .Ž .

Given these estimations for and as input to Simon’s model, the simulation program is run to generate the simulated access data. The simulated data and the corresponding empirical data are plotted in Fig. 4a and b. These plots indicate that two sets of simulated data very well match the corresponding empirical data with a slight deviation near the middle part of the curve. The mismatch may be associated with the accuracy of the parameter  estimate 14 . <sup>w</sup> <sup>x</sup>

## 2.6.2. VT proxy cache access simulation remote( clients backbone accesses)

Two sets of empirical data of VT remote clients backbone accesses are simulated; these represent 1Ž . 36,522 accesses to 4174 documents from October 1 to 7, 1995 and 2 46,603 accesses to 4719 docu-Ž . ments from October 15 to 21, 1995. These data are representative of several remote client accesses Ž .world-wide to documents on several web servers within a large organization. The estimated Simon’s model parameters from the two sets of empirical data are as follows: <sup>s</sup>0.1163, <sup>s</sup>0.92 October 1–7, Ž 1995 and. $\begin{array} { r } { \alpha = 0 . 1 0 1 3 . } \end{array}$ $\gamma = 0 . 9 3$ Ž October 15–21, 1995 . The simulated data and the actual data are. plotted in Fig. 5a and b. These two plots indicate an excellent match, again with a slight deviation near the middle part of the curve.

## 2.6.3. LSU library web access simulation

The LSU library user log contains 329,385 accesses to a web server that held 2457 documents during July 1996. This data is representative of some remote client accesses world-wide to documents onŽ . a single web server within a small organization. The parameter estimates for  and  are: $\alpha = 0 . 0 0 7 4 5 9 4$ and $\gamma = 0 . 9 9$ . From Fig. 3a one can see that the simulated data and empirical data fit well except around the middle part of the curve.

![](/api/attachments/HUGGV76D/fulltext/images/264673986aa0869bde81a85941488c879356307153d5bb4ae135db417e19390e.jpg)  
(a)

## 2.6.4. Columbia UniÕersity web access simulation

Columbia University’s web access data shows that the total number of accesses is 156,926 from 508 documents. The parameters and are estimated as 0.003244 and 0.96, respectively. Fig. 6b suggests the same conclusions as above. Note that the LSU data are more concentrated $( \gamma = 0 . 9 9 )$ than those from the Columbia’s data $( \gamma = 0 . 9 6 )$ . That is, the entry rate of new documents at LSU is slightly higher than that of Columbia’s.

In the simulated curves of Fig. 6a and b, the middle part of the curve is consistently mismatched. Perhaps, this may be related to the accuracy of estimated <sup>w</sup> <sup>x</sup> 14 . In addition, one could suggest that and are actually a function of Web-access time Ž . dynamic rather than constant as had been assumed. However, the functional form of a dynamic function is difficult to estimate and we approximate with constant values. This approximation may also contribute to the mismatch in the curves.

As described in this section, Simon’s model is proposed for describing the Web user-access process. Simon’s model appears to provide a good benchmark for justifying a complex stochastic model. It reflects user-access behavior attributes of frequency, recency, and web document entry. Web access data follows a Pareto distribution. The analysis of log data is consistent with past studies. Based on the two assumptions of web accesses new entry and auto-Ž correlation , we show that the generated data using . Simon’s model simulation also is Pareto distributed. The small lack-of-fit in the simulated Pareto curve Ž . relative to the actual data may be due to the approximation assumption made when estimating . Further work towards a better estimated is appropriate.

![](/api/attachments/HUGGV76D/fulltext/images/308a4350b6b28178dc6101ff653fb6f17078f6a5cbec09d1d8f73fc26444c717.jpg)  
(b)  
Fig. 5. VT remote clients backbone accesses simulation.

![](/api/attachments/HUGGV76D/fulltext/images/baf0c99ad3d2b1326b73a17d4af9d30dff36f53794a18acc4bd2f1e47fa9fe55.jpg)  
(a)

![](/api/attachments/HUGGV76D/fulltext/images/7d6cd04a6e2c838d4f3ad0fc0e316556f97b359f9c3df18aae45b8e8a6ba1e69.jpg)  
(b)  
Fig. 6. LSU library and Columbia University web access patterns Ž . b .

## 3. Simulation modeling and analysis of web cache policies

The purpose of this section is three-fold. First, a general overview of model-drive simulation is presented to familiarize the reader with this approach. The user-access model proposed in Section 2 allows the authors to utilize a model-driven simulation to perform web cache analysis. Second, a brief overview of the simulation logic is presented as well as the key assumptions made during the simulation analysis. Finally, a series of simulation experiments is conducted to provide insight into the complexity of web cache management problems and to illustrate the immense value that a model-driven simulation approach provides to cache analysis. In this manner, the authors intend to develop in the reader an appreciation for the important role that the user-access model proposed in Section 2 plays in Web cache analysis.

## 3.1. Model-driÕen Õs. trace-driÕen simulation

Trace-driven simulation of CPU cache policies has been popular for decades, this is because the analytical study of stochastic processes with serial correlation has proven to be too complex to solve. In the last 30 years over 50 different trace-driven simulation tools for the evaluation of CPU cache polices have been developed 32 . Due to the success of <sup>w</sup> <sup>x</sup> trace-driven simulation for evaluating CPU cache polices, many have applied this method to evaluate web cache policies.

Uhlig 32 presents the basic algorithm of trace-<sup>w</sup> <sup>x</sup> driven simulation in his survey of trace-driven simulation techniques. A trace-driven simulation procedure includes three major activities: trace collection, trace reduction and trace processing. The first step in trace-driven simulation is trace collection. Trace collection is the process of collecting user access logs of some workload of interest. Trace quality is one of the key factors affecting the simulation results. According to Uhlig 32 an ideal trace should<sup>w</sup> <sup>x</sup> be complete, detailed, and free of any distortions. A complete trace should include all the user access logs of the workloads of interest. Incomplete data collection seriously reduces the simulation quality.

A large trace consumes both storage and CPU time. Therefore, most trace-driven simulation tools include a trace reduction module to remove unneeded or redundant data from collected trace data. The final step in a trace-driven simulation is trace processing. Its input is the collected trace data after reduction; the output is the performance of the cache measured by cache hits or misses. The algorithm essentially consists of four steps: 1 Obtain a docu-Ž . ment number from the trace; 2 Search for thisŽ . document number in the simulated cache; 3 IfŽ . Ž . this document number is found in the cache then record a hit; 4 If this document number is notŽ . found in the cache then record a miss and invoke a removal policy to remove an existing document from the cache to make room for the active document Žunder the assumption of a continuous removal policy . 5 If at the end of the trace, stop. Otherwise,. Ž . go to step 1.

From the algorithm and procedure of the tracedriven simulation, inherent shortcomings of tracedriven simulation can be identified: 1 The input isŽ . the trace data of some workload of interest. Once the workload is selected, the user access pattern is determined. This makes it difficult to study dynamic user access patterns. 2 Though trace processing is a Ž . simple process, the search operation must be performed for every document in the cache. Each search in a cache holding a large number of documents consumes significant time 32 . 3 Trace collection<sup>w</sup> <sup>x</sup> Ž . and trace-reduction are also time-consuming activities 38 . <sup>w</sup> <sup>x</sup>

To overcome the problems of trace-driven simulation, a different method for evaluating web cache policies termed model-driÕen simulation is proposed. A model-driven simulation assumes a model exists to simulate time-dependent user-access behavior. In model-driven simulation different user access patterns are represented simply by changing the model’s parameters while a user access pattern in a trace-driven simulation is inherently determined once the traces are selected. It is difficult for researchers to collect and analyze a wide range of traces in order to incorporate various user access patterns, since trace collection usually takes several weeks, sometimes several months. Thus, model-driven simulation reduces Web cache analysis time and it allows one to study a broad range of user-access patterns.

## 3.2. Cache simulation study

This section provides an overview of the modeldriven cache simulation, the factors used in the simulation analysis, and the results from the simulation. The purpose of this section is to demonstrate the flexibility that a model-driven approach to simulation analysis provides and to explore various Web cache phenomena.

## 3.2.1. Model-driÕen cache simulation

The simulation model of web cache policies includes two steps: generate a user request and process the request. Simon’s model is used to generate the user request. A request for a document may be satisfied from cache or it may not. If not, then the cache removal policy will determine whether the new document should be held in cache and possibly result in the removal of an existing cached document. The simulation model to model this process is written in the SIMAN simulation language 26 . The <sup>w</sup> <sup>x</sup> first step in the model algorithm is to initialize input variables such as cache size, average document size, and the shape parameters Ž and $\gamma )$ . The basic simulation algorithm is summarized as follows.

<sup>.</sup> Compute total usage of all documents, and weighted usage of each document as described earlier.

<sup>.</sup> Determine if the access is to a new document or to a document previously accessed. A random number $N _ { 1 }$ Ž . 0–1 is generated and used to classify the access type. If $N _ { 1 }$ is less than or equal to , this access is to a new document. Otherwise, it is to an old document.

Ž . 1 If the access is to a new document, the new document will be assigned a number and size. Then the frequency and recency of this document is assigned 1 and 0 most recently accessed , respec- Ž . tively. The statistics of HR, WHR and response time will be updated.

Ž . 2 If the access is to an old document then the following occurs. At first, a random number $N _ { 2 }$ is generated between 0 and total usage of all documents. The number $N _ { 2 }$ is used to determine which old document is accessed. The determination method is as follows: the weighted usage of each document is added up until a document number at which the added weighted usage is just greater than $N _ { 2 }$ , then this document is considered as being accessed. Then the statistics of HR, WHR and response time will be updated.

<sup>.</sup> If the cache is full or the cache needs document removal, a cache removal policy will be invoked. At first, all the documents in cache will be indexed on the basis of the removal policy. Then the documents to be removed out have been determined in terms of cache space requirements. Finally, a removal policy is invoked and the documents are removed out.

Table 2  
Factors and levels in the simulation experiments

<table><tr><td>Factors and policies</td><td>Experiment 1</td><td>Experiment 2</td><td>Experiment 3</td><td>Experiment 4</td></tr><tr><td> $\alpha$ </td><td>0.1, 0.4</td><td>0.1, 0.4</td><td>0.1, 0.4</td><td>0.1, 0.4</td></tr><tr><td> $\gamma$ </td><td>0.98, 0.999</td><td>0.98, 0.999</td><td>0.98, 0.999</td><td>0.98, 0.999</td></tr><tr><td>Cache size</td><td>5% max-needed</td><td>2%, 4%, 6%, 8%, 10%, 20%, 50% max-needed</td><td>2%, 4%, 6%, 8%, 10%, 20%, 50% max-needed</td><td>2%, 4%, 6%, 8%, 10%, 20%, 50% max-needed</td></tr><tr><td>Average document size (KB)</td><td>10, 15</td><td>10</td><td>10</td><td>10</td></tr><tr><td>Removal policy</td><td>LFU, LWU</td><td>LWU, LRU, LFU, SIZE</td><td>LWU</td><td>LWU</td></tr><tr><td>Removal Method</td><td>Continuous</td><td>Continuous</td><td>Continuous, 5/10/20 periods</td><td>Continuous</td></tr><tr><td>Cache comfort level</td><td>50%, 80% cache size</td><td>60% cache size</td><td>60% cache size</td><td>20%, 50%, 80% cache size</td></tr><tr><td>Threshold policy (KB)</td><td>25, no threshold</td><td>No threshold</td><td>No threshold</td><td>No threshold</td></tr></table>

<sup>.</sup> Return to the beginning of the loop.

In this simulation study, a proxy cache environment with many users, a proxy cache, and many web servers are assumed. To simulate the performance of different web cache policies a few assumptions are made:

1. User requests are generated from a user access model.

2. User access patterns are determined by two parameters Ž . , of Simon’s model.

3. Document sizes are generated from a discrete exponential function.

4. Cache consistency staleness , cache cooperation, Ž .

Table 3  
Analysis of variance for hit rate

<table><tr><td>Source</td><td>df</td><td>SS</td><td>MS</td><td>F</td><td>P</td></tr><tr><td>α</td><td>1</td><td>2.547786</td><td>2.547786</td><td>4915.69</td><td>0.000</td></tr><tr><td>γ</td><td>1</td><td>0.990757</td><td>0.990757</td><td>1911.56</td><td>0.000</td></tr><tr><td>Document size</td><td>1</td><td>0.035748</td><td>0.035748</td><td>68.97</td><td>0.000</td></tr><tr><td>Comfort level</td><td>1</td><td>0.002279</td><td>0.002279</td><td>4.4</td><td>0.040</td></tr><tr><td>Threshold policy</td><td>1</td><td>0.000264</td><td>0.000264</td><td>0.51</td><td>0.478</td></tr><tr><td>Removal policy</td><td>1</td><td>0.153811</td><td>0.153811</td><td>296.76</td><td>0.000</td></tr><tr><td>α * γ</td><td>1</td><td>0.109787</td><td>0.109787</td><td>211.82</td><td>0.000</td></tr><tr><td>α * document size</td><td>1</td><td>0.000025</td><td>0.000025</td><td>0.05</td><td>0.826</td></tr><tr><td>α * comfort level</td><td>1</td><td>0.004309</td><td>0.004309</td><td>8.31</td><td>0.005</td></tr><tr><td>α * threshold policy</td><td>1</td><td>0.000170</td><td>0.000170</td><td>0.33</td><td>0.569</td></tr><tr><td>α * removal policy</td><td>1</td><td>0.011073</td><td>0.011073</td><td>21.36</td><td>0.000</td></tr><tr><td>γ * document size</td><td>1</td><td>0.000936</td><td>0.000936</td><td>1.81</td><td>0.184</td></tr><tr><td>γ * comfort level</td><td>1</td><td>0.011995</td><td>0.011995</td><td>23.14</td><td>0.000</td></tr><tr><td>γ * threshold policy</td><td>1</td><td>0.011478</td><td>0.011478</td><td>22.15</td><td>0.000</td></tr><tr><td>γ * removal policy</td><td>1</td><td>0.010309</td><td>0.010309</td><td>19.89</td><td>0.000</td></tr><tr><td>Other interactions</td><td>(negligible)</td><td></td><td></td><td></td><td></td></tr><tr><td>Error</td><td>64</td><td>0.033171</td><td>0.000518</td><td></td><td></td></tr><tr><td>Total</td><td>127</td><td>3.986842</td><td></td><td></td><td></td></tr></table>

![](/api/attachments/HUGGV76D/fulltext/images/bf23652756350192feae0a37fabbcc2db025d49ae1872d34fb0684f38968bac3.jpg)

(b) min. cache level=60%, continuous removal, 0 alpha=0.1,gamma=0.999  
![](/api/attachments/HUGGV76D/fulltext/images/e304744845fc3e5ab9b7c1da9f9bcfbd6b185f84523200204174becb410be726.jpg)  
Fig. 7. The performance comparison of cache removal policies.

![](/api/attachments/HUGGV76D/fulltext/images/28bfb52a07d75ce069329d690ded45f4fcde7c47668fbae5571909b6f421db78.jpg)

![](/api/attachments/HUGGV76D/fulltext/images/02907415a9cb39a5e0c32d6450dbbc55c502d2dbc06daf62f8b7cb1ff874c7a3.jpg)  
Fig. 7 continued . Ž .

private documents, and dynamic documents are not addressed.

5. New documents have an initial HR of zero.

6. The Web cache assumes a continuous review policy.

## 3.2.2. Simulation factors and conditions

A series of experiments are run to gain insight into the cache phenomena. Factor levels are chosen based on author’s interests as well as on past research. Below is an overview of the factors studied.

![](/api/attachments/HUGGV76D/fulltext/images/b677e84073b9e2f2f37834f6c430c0c46a84b6e63fd691affe9ab605b4c05c31.jpg)

![](/api/attachments/HUGGV76D/fulltext/images/ed07da620b33a5619b7d474ae35ceb780604aff17a1595c689a81031729440db.jpg)  
Fig. 8. The performance comparison of cache removal methods.

![](/api/attachments/HUGGV76D/fulltext/images/3540786fd4f114b64612b7ebc7ba28b5ac13fd1e5a4a546f524e6da32c3b45cb.jpg)

![](/api/attachments/HUGGV76D/fulltext/images/eae7e3a1a24b663c223cb6cae0b3c533557274f1429b1601d9764cf38a99da5e.jpg)

3.2.2.1. User access pattern ( ) , . Simon’s model parameters can take on any value in the range 0–1. Practically speaking, user-access patterns encountered from previous studies indicate that will essentially fall between 0.9 and 1.0. It is observed that the HR measure is very sensitive to the parameter in this range. Instead of looking at the entire range of values between 0.9 and 1.0 we focus on a portion on this range $( \gamma = 0 . 9 8 \ – 0 . 9 9 9 9 )$ Similarly with the parameter $( \alpha = 0 . 1 0 \ – 0 . 4 0 )$

The feasible values of these parameters $( \alpha , \ \gamma ) ,$ placed on the x- and y-axes, respectively, results in

(a)  
![](/api/attachments/HUGGV76D/fulltext/images/d34677d012f1eac34b646d1e5a437d1fbfec62dc5be660eb5437e0d2b6984c25.jpg)

(b)  
![](/api/attachments/HUGGV76D/fulltext/images/a1328aadc1adba7fb8a6e3c2f16c6f43aba3874addbf43674753803af164d003.jpg)  
Fig. 9. The performance comparison of cache comfort level.

![](/api/attachments/HUGGV76D/fulltext/images/1d2e56a4075b72daad4a02f90b1725a1ad22ecacfd964e20af2c0a2042d107b3.jpg)

![](/api/attachments/HUGGV76D/fulltext/images/7f40a38c04842bf80114951a816a90e05f02d3af7072dbc392a27ca4693da7fc.jpg)

a matrix of possible user-access patterns. These experiments focus on only a portion of this matrix.

3.2.2.2. Cache size. To study the impact of cache size on cache performance, several levels of cache size are used in the simulation experiments. Past studies indicate that the impact of cache size on cache performance is nonlinear in the small range of cache size, but changes only slightly in the large range. The levels of cache size used in the experiments are determined by the cache size max-needed with different user access patterns. The cache size max-needed is determined by the three factors: user access pattern $( \alpha , \gamma )$ , average document size and total access number. The way to determine maximum cache size needed is described below.

Suppose that there are seven levels of cache size in an experiment: 2, 4, 6, 8, 10, 20, and 50% of maximum cache size needed. Further, suppose that is 0.2, the average document size in the simulation is 10 KB, and the total accesses is equal to 10,000. Then the total documents in this simulation is roughly $1 0 , 0 0 0 \times 0 . 2 = 2 0 0 0 .$ . Since the average document size is 10 KB, the maximum cache size needed to store all the documents would be $2 0 0 0 \times 1 0 = 2 0 { , } 0 0 0$ KB i.e., 20 MB . Thus, the seven levels of cacheŽ . size assumed in the simulation experiment are: 400

![](/api/attachments/HUGGV76D/fulltext/images/ec34b88a560ad52586eb9dfa3c98874f8659fef0d5b7590eb576536e26f6fc3b.jpg)

![](/api/attachments/HUGGV76D/fulltext/images/b655af22e0f83077d631b4a1f9f7e28783f6f8edae205dccef91a1768379a561.jpg)  
Fig. 10. Performance comparison of threshold policies.

![](/api/attachments/HUGGV76D/fulltext/images/c4680863a3ffeda269f59f95c685dd516aaac3ed9a776c4b99b803183e442309.jpg)

![](/api/attachments/HUGGV76D/fulltext/images/829418dadee639f9b5e4e028170177a67bd63f6ea0cef1aebeff4788759309e6.jpg)  
Fig. 10 continued . Ž .

Ž . i.e., 2%<sup>=</sup>20,000 KB , 800, 1200, 1600, 2000, 4000, and 10,000 KB.

3.2.2.3. Document size. Document size distribution has been studied by Cunha et al. 9 . This study<sup>w</sup> <sup>x</sup> confirms that the distribution is approximately exponential. Therefore, all the document sizes in the simulation experiments are generated from an exponential function.

3.2.2.4. RemoÕal policy. In these experiments four removal policies are examined: LWU, LRU, LFU and SIZE. The primary purpose is to see if LWU performs best among the four removal policies. LWU, as described in Appendix A, is a new removal policy proposed by the authors.

3.2.2.5. RemoÕal method. Removal method determines when documents should be removed. Two removal methods are examined in these experiments: continuous and periodic.

3.2.2.6. Cache comfort leÕel. Cache comfort level determines how many documents should be removed when a removal policy is executed. A higher cache comfort level means that only a small number of documents will be removed from cache in a removal action.

3.2.2.7. Threshold policy. A threshold policy is a rule that places a constraint on document size, thus not allowing those documents larger than the predefined threshold to enter into a cache.

3.2.2.8. Warm-up period and run length. Preliminary simulation studies show that the simulation output Ž . HR, WHR and response time is stable after 10,000 accesses. In the simulation experiment, the warm-up period is set to 10,000 accesses, and the run length is set to 10,000 accesses. Multiple runs will not affect this comparison.

Table 2 summarizes the factors and the factor assumed by the simulation experiments.

## 3.2.3. Simulation results

3.2.3.1. Experiment 1: screening. In this experiment, the objective is to study the effects of main factors and their interactions on cache performance. The ANOVA analysis for HR in Table 3 shows that three significant factors affect cache performance: , , and removal policy cache size is also a significantŽ factor, which can be seen in the following experiments . These factors explain approximately 90% of . the variation in HR. Also, the interaction between and  is significant and all other interactions are negligible.

3.2.3.2. Experiment 2: comparison of remoÕal policies. Finding a robust dynamic removal policy has been the aim of web cache simulation studies over the past few years. In this experiment the LWU removal policy is compared to other removal policies. This experiment assumes 10 KB average document size, no threshold policy and a continuous removal method. In addition, a random rule is used as the cache removal tie-breaking rule.

As expected, LWU removal policy performs best among the four policies, especially on the small cache sizes Fig. 7 . Its good performance is due toŽ . its property that incorporates three characteristics of user access patterns: frequency, recency and size. The performance order of the three removal policies is generally consistent. LRU seems to perform better than LFU across the cache sizes used and different user access patterns considered in this experiment. SIZE performance seems to be lower than LRU and higher than LFU, but quite inconsistent in the graphs of Fig. 7.

The results show that cache HR increases for all removal policies with an increase of cache size. The performance difference among the policies is apparent in the small cache size range but negligible in large cache sizes. This result is consistent with the previous studies of Arlitt and Williamson 3 , and <sup>w</sup> <sup>x</sup> Abrams et al. 1 . Intuitively, a large size cache results in a high HR. When the HR of a cache nearly reaches its maximum HR, the impact of the removal policy and all other factors on cache performance is very small.

3.2.3.3. Experiment 3: comparison of remoÕal methods. The purpose of this experiment is to compare two types of removal methods, continuous and periodic, and determine which method is better.

Fig. 9a,c,d show that the continuous removal policy achieves higher HRs over the given cache size range. In Fig. 8b, continuous removal method has a good performance beyond 1000 KB of the cache size, but a poor performance below that point.

In the three periodic removal scenarios, a large number of removal periods 20 periods performsŽ . better than a small number of removal periods 5Ž periods particularly in the case of. $\gamma = 0 . 9 8$ Ž  Fig. 8a and c . This phenomenon may be associated with the. small value of . For example, when is 0.98, it represents a user access pattern where documents accessed in the recent past will likely be accessed again in the near future. In this case documents should be removed frequently and not allowed to reside in the cache for a long time.

Another interesting phenomenon is observed for the case of $\gamma = 0 . 9 9 9$ Fig. 8b and d . With theŽ . increase of cache size the performance in all three scenarios increases, but once it reaches the highest

HR, then the performance starts to decrease. This situation may be due to the large value of . Again for large Ž . 0.999 , this represents a user-access pattern where documents accessed frequently in the past will likely be accessed again in the near future. Thus, documents should reside in the cache for a relatively long time in order to meet the users’ requests in the future. When cache size increases inŽ the small range , cache performance should increase.. When the cache size reaches a point where the cache has sufficient capacity to capture the most requested documents, continual frequent removal of the documents from the cache will degrade performance. Furthermore, the two graphs Fig. 8b and d indicateŽ . that beyond this cache size point the larger the number of removal periods, the worse the cache performance.

It can be seen from this experiment that the continuous removal policy is better than the periodic removal policy. Also in terms of simplicity, the periodic removal method requires one to determine an optimal removal cycle.

3.2.3.4. Experiment 4: the study of comfort leÕel. Intuitively, a cache with a high comfort level will be frequently full. The advantage of this condition is that the cache space is fully utilized, while the disadvantage is that the documents, which may not be interesting to the users, would reside in the cache for a long time i.e., obsolete documents . In con-Ž . trast, in the low comfort level system the cache is rarely full, a great deal of cache space is wasted, but there are fewer obsolete documents. In practice, these two situations result in a trade-off for a cache administrator. In this experiment a presumably reasonable cache comfort level is assumed.

Apparent in Fig. 9, cache performance in the three comfort levels is approximately the same in the large range of cache sizes when is small Ž . <sup>s</sup>0.98 . However, the cache performance with a low comfort level 20% is worse whenŽ . Ž . is large <sup>s</sup>0.999 . This phenomenon may be related to a large  user’s behavior. A large  indicates that users typically concentrate on some documents to access. Thus, more space of a cache can store more documents that are frequently accessed. Since a low comfort level has a drawback in that cache space is wasted, a cache with this low comfort level would store only a small number of documents. Therefore, its HR would be low.

3.2.3.5. Experiment 5: the study of threshold policy. The threshold policy has been studied by Arlitt and Williamson 3 and Abrams et al. 1 . The basic <sup>w x</sup> <sup>w x</sup> conclusion drawn from their studies is that threshold policy will significantly reduce WHR, but produce only a slight decrease in HR. We believe that this conclusion is reasonable. Our main purpose in this experiment is to examine if this conclusion is still true using different user access patterns.

Fig. 10 illustrates the cache performance under two threshold strategies 25 KB and no thresholdŽ . using different user access patterns. Essentially, the conclusions from the previous studies are reproduced in this experiment. WHRs are significantly reduced, and HRs decrease slightly if 25 KB threshold policy is imposed. This conclusion continues to hold true for varying user-access patterns.

## 4. Conclusions

The Web cache problem is of growing concern in the recent past as the demand for the Internet continues to escalate. Web caches are fast becoming a viable means to alleviate the high user response times experienced by many Web users. Many commercial systems are available to support web cache decisions.

The analysis of Web cache policies has relied mostly on trace-driven simulation that has obvious disadvantages. A reasonable user-access model is proposed in this paper to address the shortcomings of the trace-driven simulation approach. Simon’s model provides a robust dynamic model of web user access patterns. It integrates frequency and recency into a simple mathematical model. This user-access model simulates the generation of document requests that are then fed into a model-driven simulation of Web cache policy. A model-driven approach to Web cache analysis provides a better mechanism for experimentation and for generalization of results.

The results from the simulation study show that the LWU removal policy performs best due to its ability to adapt both frequency and recency in different application environments. Also, the continuous

removal method generally performs better than the periodic removal method. Finally, a low comfort level less than 50% cache size and threshold policyŽ . generally degrades web cache performance.

## Appendix A. Least weighted usage LWU cache removal policy ( )

A cache removal policy based on Simon’s information processing model is proposed. Least weighted usage Ž . LWU is defined as follows:

$$
\mathrm{LWU} _ {j} = \sum_ {\tau = 1} ^ {k} y _ {j} (\tau) \gamma^ {k - \tau} \quad (\text { document   size   is   smaller   than } 5 0 \mathrm{KB})
$$

$$
\mathrm{LWU} _ {j} = \left(\sum_ {\tau = 1} ^ {k} y _ {j} (\tau) \gamma^ {k - \tau}\right) \left(\frac {1}{\text { size } _ {j}}\right) \quad (\text { document   size   is   equal   or   larger   than   50KB })
$$

where N is the total access number to a cache, j is the document number, is the sequence of the accesses to a cache, $y _ { j } ( \tau )$ is 1 or 0, if the  th access is the jth document then $y _ { j } ( \tau )$ is 1, otherwise it is 0, and $\mathrm { s i z e } _ { j }$ is the size of document $j .$

Both frequency $y _ { j } ( \tau )$ and recency are used to define this measure. Frequency is the access number or hitsŽ . to a cached document. Recency takes into consideration the timing of accesses called decay factor in Simon’sŽ model . The LWU policy removes the cached document that has the least weighted usage. The LWU value is. calculated using the defined formula above.

This removal policy incorporates some important characteristics of user access patterns: frequency, recency, and size. Document size is incorporated into the formula in the form of $1 / \mathrm { s i z e } _ { i } ,$ since large documents are not frequently requested. If user access patterns change i.e.,Ž .and change , LWU policy can adapt to this change. Therefore, we refer to the LWU policy as a dynamic removal policy.

## Appendix B. Simon’s model version III illustrated

Suppose there are five documents accessed 10 times in a short time interval $( \tau = 1 0$ and $j = 5 )$

<table><tr><td>τ</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>j</td><td>A</td><td>B</td><td>A</td><td>C</td><td>D</td><td>B</td><td>B</td><td>E</td><td>C</td><td>A</td></tr></table>

Suppose that $\alpha = 0 . 2 , \ \gamma = 0 . 9 9$

<table><tr><td> $j$ </td><td colspan="10"> $\tau$ </td><td> $\mathop{\sum }\limits_{{\tau } = 1}^{k = {10}}{y}_{j}\left( \tau \right)$ </td><td> $\mathop{\sum }\limits_{{\tau } = 1}^{10}{y}_{j}\left( \tau \right) {\gamma }^{10 - \tau }$ </td><td> ${P}_{j}\left( {11}\right) =$  $\left( {1 - \alpha }\right) {W}_{j}/{W}_{5}$ </td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td></td><td></td><td></td></tr><tr><td>A</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>3</td><td>2.84558</td><td>0.238</td></tr><tr><td>B</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>3</td><td>2.85364</td><td>0.239</td></tr><tr><td>C</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>2</td><td>1.93148</td><td>0.162</td></tr><tr><td>D</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0.95099</td><td>0.080</td></tr><tr><td>E</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0.98010</td><td>0.082</td></tr></table>

The following computation is to illustrate how to compute frequency $\textstyle ( \sum _ { \tau = 1 } ^ { k = 1 0 } y _ { j } ( \tau ) )$ , weighted usage $\begin{array} { r } { ( \sum _ { \tau = 1 } ^ { 1 0 } y _ { j } ( \tau ) \gamma ^ { 1 0 - \bar { \tau } } ) } \end{array}$ , and the accessing probability $( P _ { j } ( 1 1 ) = ( 1 - \alpha ) W _ { j } / W _ { 5 } )$ of each document after 10 accesses. Let us take document A as an example.

$$
\begin{array}{l} \sum_ {\tau = 1} ^ {k = 1 0} y _ {\mathrm{A}} (\tau) = 1 + 0 + 1 + 0 + 0 + 0 + 0 + 0 + 0 + 1 = 3 \\ W _ {\mathrm{A}} = \sum_ {\tau = 1} ^ {1 0} y _ {\mathrm{A}} (\tau) r ^ {1 0 - \tau} = 1 (0. 9 9) ^ {(1 0 - 1)} + 0 + 1 (0. 9 9) ^ {(1 0 - 3)} + 0 + 0 + 0 + 0 + 0 + 0 + 1 (0. 9 9) ^ {(1 0 - 1 0)} \\ = 2. 8 4 5 5 8 \end{array}
$$

Suppose that we have obtained the values of $W _ { \mathrm { A } } , \ W _ { \mathrm { B } } , \ W _ { \mathrm { C } } , \ W _ { \mathrm { D } } , \ W _ { \mathrm { E } }$ , we can add up them to obtain total weighted usage of all the documents.

$$
W _ {\mathrm{A}} = \sum_ {j = 1} ^ {5} W _ {j} = (2. 8 4 5 5 8 + 2. 8 5 3 6 4 + 1. 9 3 1 4 8 + 0. 9 5 0 9 9 + 0. 9 8 0 1 0) = 9. 5 6 1 7 9
$$

The final step is to compute the accessing probability $( P _ { j } ( 1 1 ) = ( 1 - \alpha ) W _ { i } / W _ { 5 } )$ of each document after 10 accesses. For example, the accessing probability of document A at the 11th access is computed as follows:

$$
p _ {\mathrm{A}} (1 1) = (1 - a) W _ {\mathrm{A}} / W _ {5} = (1 - 0. 2) 2. 8 4 5 5 8 / 9. 5 6 1 7 9 = 0. 2 3 8
$$

Therefore, the expected probability of each document at the 11th access for selection is:

<table><tr><td>New Document</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr><tr><td>0.20</td><td>0.238</td><td>0.239</td><td>0.162</td><td>0.080</td><td>0.082</td></tr></table>

## Appendix C. The index method

At this point, it is necessary to describe the index approach which is proposed by Chen and Leimkuhler 7 . <sup>w</sup> <sup>x</sup> This index approach forms the basis for the expression of simulated results of Simon’s model. Kendall 1960Ž . studied 1763 papers published on operational research. He arranged the number of authors who have published n papers in a list, and observed that n does not run consecutively at places, especially it is true when n is large. In order to take into account the scattering of the larger values of n, Chen and Leimkuhler 7 introduced an<sup>w</sup> <sup>x</sup> index $i = 1 , 2 , \ldots , m$ , for the m successive observations of n, and let $n _ { i }$ denote the ith nonzero value of n, where $n _ { i } < n _ { i + 1 } .$

In order to apply this approach to our simulation data organization, we define the notation of this approach in context of web accesses. Suppose that user request documents through a web cache during a period of time, we define m<sup>s</sup>the maximum number of the list of documents with same access number; $n _ { i } =$ the number of times a document is accessed; $f ( n _ { i } ) = { \mathrm { n u m b e r } }$ of documents with access $\begin{array} { r } { n _ { i } ; ~ r _ { i } = \sum _ { k - i + 1 } ^ { m } n _ { k } f ( n _ { k } ) = \mathrm { t h e } } \end{array}$ rank of document i ranked according to its access; $\begin{array} { r } { G ( r _ { i } ) = \sum _ { k = m - i + 1 } ^ { m } n _ { k } f ( n _ { k } ) = } \end{array}$ total number of accesses for documents ranked no greater than $\begin{array} { r } { r _ { i } ; T = \sum _ { i = 1 } ^ { m } f ( n _ { i } ) = } \end{array}$ total documents in the web cache; $\begin{array} { r } { R = \sum _ { i = 1 } ^ { m } n _ { i } f ( n _ { i } ) = } \end{array}$ total accesses to the cache; $x _ { i } = ( 1 / T ) \Sigma _ { k = m - i + 1 } ^ { m } f ( n _ { k } ) =$ the fraction of total documents; $y _ { i } =$ $( 1 / R ) \Sigma _ { k = m - i + 1 } ^ { m } n _ { k } f ( n _ { k } ) =$ the fraction of total accesses; ${ \begin{array} { r } { \mathrm { A r e a } = { \frac { y _ { 1 } x _ { 1 } } { 2 } } + { \frac { ( y _ { 1 } + y _ { 2 } ) ( x _ { 2 } - x _ { 1 } ) } { 2 } } - { \frac { ( y _ { 2 } + y _ { 3 } ) ( x _ { 3 } - x _ { 2 } ) } { 2 } } + \ldots + } \end{array} }$ $\begin{array} { r } { \frac { ( y _ { m - 1 } + y _ { m } ) ( x _ { m } - x _ { m - 1 } ) } { 2 } - \frac { 1 } { 2 } } \end{array}$ , the area is between the curve and the line $y = x .$

## Appendix D. Reference equations regression analysis

Simon’s model parameters are estimated in Section 2.4. Part of this estimation involves populating a table with values for the Pareto curve Area given different discrete combinations of and . A response surface is then developed so that can be back calculated given and Area from the actual data. In this appendix, the regression models actually developed for this analysis are presented. The table is split into two response surfaces since the sensitivity of the dependent variable to was much greater in the range $\delta = 0 . 9 \ \mathrm { t o } \ 1 . 0 .$

Modeling AREA $( Y _ { 1 } )$ at $X _ { 1 } \colon \mathrm { { A l p h a } } = \{ 0 . 0 { - } 1 . 0 \} , \ X _ { 2 } \colon$  4  Gamma <sup>s</sup> 0.0–0.9, including 0.9 .  
The primary result obtained is the analysis of variance table below:

<table><tr><td>Regression</td><td>df</td><td>Type I sum of squares</td><td> $R^{2}$ </td><td>F-ratio</td><td>P&gt;F</td></tr><tr><td>Linear</td><td>2</td><td>1.450555</td><td>0.9692</td><td>18,229</td><td>0.0000</td></tr><tr><td>Quadratic</td><td>2</td><td>0.001850</td><td>0.0012</td><td>23.252</td><td>0.0000</td></tr><tr><td>Cross-product</td><td>1</td><td>0.037258</td><td>0.0249</td><td>936.4</td><td>0.0000</td></tr><tr><td>Total regression</td><td>5</td><td>1.489664</td><td>0.9954</td><td>7488.1</td><td>0.0000</td></tr></table>

This presents the individual contribution of each type of effect to the statistical fit. In the case of fitting the model 1 , the results indicate that the cross-product effect is significant Ž . $( P < 0 . 0 5 )$ . On the other hand, there is a significant linear as well as quadratic effect. In conclusion, the overall quadratic polynomial response surface model 1 is significant. Thus, there is a strong evidence that the Alpha and Beta the explanatory variables in Ž . Ž the model are related to the expected value of Area..

The regression equation illustrated in the table below explains the importance and significance of each independent variable $( X _ { 1 }$ and $X _ { 2 } )$ Ž, their cross-products interactions: $X _ { 1 } X _ { 2 } )$ , and whether, from analysis of quadratic terms $( X _ { 1 } X _ { 1 } , \ X _ { 2 } X _ { 2 } ) .$ , a linear or a curve response surface is needed to model the response. The AREA is significantly $( P < 0 . 0 5 )$ affected by $X _ { 1 }$ Ž .negative effect and $X _ { 2 }$ Ž . positive effect . On the other hand, the square of $X _ { 1 }$ and $X _ { 2 }$ as well as the interaction effect $( X _ { 1 } X _ { 2 } )$ are statistically significant $( P < 0 . 0 5 )$ suggesting that the effect of $X _ { 1 }$ and $X _ { 2 }$ are nonlinear within the range of experimental conditions used and that the response variable is affected by the combination of $X _ { 1 }$ and $X _ { 2 }$

<table><tr><td>Parameter</td><td>df</td><td>Parameter estimate</td><td>Standard error</td><td>T for  $H_0$ : parameter = 0</td><td>P &gt; |T|</td></tr><tr><td>Intercept</td><td>1</td><td>0.275</td><td>0.0027</td><td>102.7</td><td>0.0000</td></tr><tr><td> $X_1$ </td><td>1</td><td>-0.213</td><td>0.0089</td><td>-23.91</td><td>0.0000</td></tr><tr><td> $X_2$ </td><td>1</td><td>0.182</td><td>0.0069</td><td>26.38</td><td>0.0000</td></tr><tr><td> $X_1 * X_1$ </td><td>1</td><td>-0.039</td><td>0.0078</td><td>-5.001</td><td>0.0000</td></tr><tr><td> $X_2 * X_1$ </td><td>1</td><td>-0.193</td><td>0.0063</td><td>-4.636</td><td>0.0000</td></tr><tr><td> $X_2 * X_2$ </td><td>1</td><td>-0.03</td><td>0.0065</td><td>-30.60</td><td>0.0000</td></tr></table>

The predicted model is: $\mathrm { A r e a } = 0 . 2 7 5 - 0 . 2 1 3 * \mathrm { A l p h a } + 0 . 1 8 2 * \mathrm { G a m m a } - 0 . 0 3 9 * \mathrm { ( A l p h a ) ^ { 2 } - }$ Ž .<sup>2</sup> 0.03) Gamma <sup>y</sup>0.193)Ž . Ž . Alpha ) Gamma .

Modeling AREA $( Y _ { 1 } )$ at $X _ { 1 } \colon \mathrm { { A l p h a } } = \{ 0 . 0 { - } 1 . 0 \} ; \ X _ { 2 } \colon$  4  Gamma <sup>s</sup> 0.9–1.0, not including 0.9 .  
The primary result obtained is the analysis of variance table below:

<table><tr><td>Parameter</td><td>df</td><td>Type I sum of squares</td><td> $R^{2}$ </td><td>F-ratio</td><td>P&gt;F</td></tr><tr><td>Linear</td><td>2</td><td>1.682219</td><td>0.9873</td><td>8925.1</td><td>0.0000</td></tr><tr><td>Quadratic</td><td>2</td><td>0.008279</td><td>0.0049</td><td>43.923</td><td>0.0000</td></tr><tr><td>Cross-product</td><td>1</td><td>0.002024</td><td>0.0012</td><td>21.474</td><td>0.0000</td></tr><tr><td>Total regression</td><td>5</td><td>1.692521</td><td>0.9934</td><td>3591.9</td><td>0.0000</td></tr></table>

This presents the individual contribution of each type of effect to the statistical fit. In the case of fitting the model 1 , the results indicate that the cross-product effect is significantŽ . $( P < 0 . 0 5 )$ . On the other hand, there is a significant linear as well as quadratic effect. In conclusion, the overall quadratic polynomial response surface model 1 is significant. Thus, there is a strong evidence that the Alpha and Gamma the explanatory variablesŽ . Ž in the model are related to the expected value of Area..

The regression equation illustrated in the table below explains the importance and significance of each independent variable $( X _ { 1 }$ and $X _ { 2 } )$ Ž, their cross-products interactions: $X _ { 1 } X _ { 2 } ) .$ , and whether, from analysis of quadratic terms $( X _ { 1 } X _ { 1 } , \ X _ { 2 } X _ { 2 } )$ , a linear or a curve response surface is needed to model the response. The AREA is significantly $\left( P < 0 . 0 5 \right)$ affected by $X _ { 1 }$ Ž .positive effect and $X _ { 2 }$ Ž . negative effect . On the other hand, the square of $X _ { 1 }$ and $X _ { 2 }$ as well as the interaction effect $( X _ { 1 } X _ { 2 } )$ are statistically significant $( P < 0 . 0 5 )$ suggesting that the effect of $X _ { 1 }$ and $X _ { 2 }$ are nonlinear within the range of experimental conditions used and that the response variable is affected by the combination of $X _ { 1 }$ and $X _ { 2 }$

<table><tr><td>Parameter</td><td>df</td><td>Parameter estimate</td><td>Standard error</td><td>T for  $H_0$ : parameter = 0</td><td>P &gt; |T|</td></tr><tr><td>Intercept</td><td>1</td><td>18.69</td><td>3.777</td><td>4.949</td><td>0.0000</td></tr><tr><td> $X_1$ </td><td>1</td><td>0.348</td><td>0.198</td><td>1.760</td><td>0.0000</td></tr><tr><td> $X_2$ </td><td>1</td><td>-38.20</td><td>7.747</td><td>-4.931</td><td>0.0000</td></tr><tr><td> $X_1 * X_1$ </td><td>1</td><td>0.114</td><td>0.014</td><td>7.908</td><td>0.0000</td></tr><tr><td> $X_2 * X_1$ </td><td>1</td><td>-0.924</td><td>3.971</td><td>5.031</td><td>0.0000</td></tr><tr><td> $X_2 * X_2$ </td><td>1</td><td>19.98</td><td>0.199</td><td>-4.634</td><td>0.0000</td></tr></table>

The predicted model is: $\mathrm { { A r e a } = 1 8 . 6 9 + 0 . 3 4 8 * \mathrm { { A l p h a } - 3 8 . 2 0 * \mathrm { { G a m m a } + 0 . 1 1 4 * ( A l p h a ) ^ { 2 } + \Omega ^ { 6 } } } }$ $1 9 . 9 8 * ( \mathrm { G a m m a } ) ^ { 2 } - 0 . 9 2 4 * ( \mathrm { A l p h a } ) * ( \mathrm { G a m m a } )$

## References

<sup>w</sup> <sup>x</sup> 1 M. Abrams, C. Standridge, G. Abdulla, S. Williams, E. Fox, Caching Proxies, Limitations and Potentials, World Wide Web Journal Issue 1, 4th WWW Conference, 1995, pp. 119–133.

<sup>w</sup> <sup>x</sup> 2 M. Abrams, WWW: Beyond the Basics, 1997, http:<sup>rr</sup> ei.cs.vt.edu<sup>r ;</sup> wwwbtb<sup>r</sup>fall.96<sup>r</sup>book<sup>r</sup>chap25<sup>r</sup>index.html.

<sup>w</sup> <sup>x</sup> 3 M. Arlitt, C.L. Williamson, Trace-drive simulation of document caching strategies for internet web servers, Simulation 68 1 1997 23–33.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 M. Arlitt, C.L. Williamson, Web server workload characterization: the search for invariants, Proceedings of the 1996 ACM SIGMETRICS Conference on the Measurement and Modeling of Computer Systems, Philadelphia, PA, May 23– 26, 1996, pp. 126–137.

<sup>w</sup> <sup>x</sup> 5 Y.S. Chen, Zipf’s Law in Natural Languages, Programming Languages, and Command Languages: the Simon–Yule $\mathsf { A p - }$ proach, 1991.

<sup>w</sup> <sup>x</sup> 6 Y.S. Chen, P.P. Chong, Information productivity modeling: the Simon–Yule approach, Encyclopedia of Library and Information Science 61 1998 170–200, Supplement 24.Ž .

<sup>w</sup> <sup>x</sup> 7 Y.S. Chen, F.F. Leimkuhler, A relationship between Lotka’s law, Bradford’s law, and Zipf’s law, Journal of the American Society for Information Science, September 1986, pp. 307– 314.

<sup>w</sup> <sup>x</sup>8 Y.S. Chen, P.P. Chong, M.Y. Tong, Mathematical and computer modeling of the Pareto principle, Mathematical Computer Modeling 19 9 1994 61–80.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 R.C. Cunha, A. Bestavros, E.M. Crovela, Characteristics of WWW Client-based Traces, Computer Science Department,

Boston University BU-CS-95-010 , 1996, http:Ž . <sup>rr</sup>cs-www. bu.edu<sup>r</sup>faculty<sup>r</sup>crovella<sup>r</sup>paper-archive<sup>r</sup>TR-95-010<sup>r</sup>paper. html.

<sup>w</sup> <sup>x</sup> 10 S. Glassman, A caching relay for the world web, Proceedings of the First International Conference on the World-Wide Web WWW94 , Elsevier, May 1994.Ž .

<sup>w</sup> <sup>x</sup> 11 N. Gross, Clearing the traffic jams in cyberspace, Business Week, November 17, 1997, p. 82.

<sup>w</sup> <sup>x</sup> 12 J.D. Guyton, M.F. Schwartz, Locating nearby copies of replicated internet servers, Technical Report CU-CS-762-5, University of Colorado at Boulder, 1995.

<sup>w</sup> <sup>x</sup> 13 J. Gwertzman, M. Seltzer, World wide web cache consistency, Report, Microsoft and Harvard University, 1996.

<sup>w</sup> <sup>x</sup> 14 Y. Ijiri, H.A. Simon, Skew Distributions and the Sizes of Business Firms, North-Holland, 1977.

<sup>w</sup> <sup>x</sup> 15 F.F. Leimkuhler, P.M. Morse, Analysis and application of information productivity models, NSF Grant IST-791189333A1, 1979.

<sup>w</sup> <sup>x</sup> 16 A. Luotonen, K. Atlis, World-wide web proxies, Proceedings of the First International World Wide Web Conference, Amserdam, Elserver, May 1994.

<sup>w</sup> <sup>x</sup>17 R. Malpani, J. Lorch, D. Berger, Making world wide web caching servers cooperate, 1996, http:<sup>rr</sup>www.w3.org<sup>r</sup> pub<sup>r</sup>conferences<sup>r</sup>www4<sup>r</sup>papers<sup>r</sup>59<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 18 B. Mandelbrot, An information theory of statistical structure of languages, Proceedings of the Symposium on Applications of Communication Theory, London, Butterworths, London, 1953, pp. 486–500.

<sup>w</sup> <sup>x</sup> 19 P. Markatos, Main memory caching of web documents, Proceedings of the Fifth International Conference on the World-Wide Web WWW96 , Paris, May 1996. Ž .

<sup>w</sup> <sup>x</sup> 20 A.A. Markov, An example of a statistical investigation of the text of ‘Eugen Onegin’ illustrating the connection of trials in a chain, Bulletin de L’Academie Imperiale des Science de st, Petersburg 7 1913 153. Ž .

<sup>w</sup> <sup>x</sup> 21 R.E. McGrath, Caching for large scale systems, D-Lib Magazine, January 1996, http:<sup>rr</sup>repository.cnri.reston.va.us<sup>r</sup> dlib<sup>r</sup>january96<sup>r</sup>ncsa<sup>r</sup>01mcgrath.html.

<sup>w</sup> <sup>x</sup> 22 P.M. Morse, F.F. Leimkuhler, Exact solution for the Bradford distribution and its use in modeling informational data, Operations Research 27 1979 187–198, NLANR, Squid,Ž . http:<sup>rr</sup>squid.nlanr.net<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 23 D. O’Callaghan, A central caching proxy server for WWW users at the University of Melbourne, The First Australian World Wide Web Conference, March 1995.

<sup>w</sup> <sup>x</sup> 24 V. Pareto, Manuale d’Economia Politica, 1909; A.M. Kelley, English Translation, 1971.

<sup>w</sup> <sup>x</sup> 25 V. Paxson, S. Floyd, Why we don’t know how to simulate the internet, in: S. Andradottir, K.J. Healy, D.H. Withers, B.L. Nelson Eds. , Proceedings of the 1997 Winter Simula-Ž . tion Conference, 1997, pp. 1037–1044.

<sup>w</sup> <sup>x</sup> 26 C.D. Pegden, R.E. Shannon, R.P. Sadowsk, Introduction to Simulation Using SIMAN, 2nd edn., McGraw-Hill, 1995.

<sup>w</sup> <sup>x</sup> 27 J.E. Pitkow, M.M. Recker, A simple yet robust caching algorithm based on dynamic access patterns, Proceedings of the First International Conference on the World-Wide Web Ž . WWW94 , Elsevier, May 1994.

<sup>w</sup> <sup>x</sup> 28 M.M. Recker, E.J. Pitkow, Predicting document access in large, multimedia repositories, Report, Graphics, Visualization and Usability Center, Georgia Institute of Technology, 1996.

<sup>w</sup> <sup>x</sup> 29 H.A. Simon, T.A. Van Wormer, Some Monte Carlo estimates of the Yule distribution, Behavior Science, 1963, pp. 203–210.

<sup>w</sup> <sup>x</sup> 30 H.A. Simon, On a class of skew distribution function, Biometrika 42 1955 425–440.Ž .

<sup>w</sup> <sup>x</sup> 31 Y. Tong, A self-adaptive database buffer replacement scheme, PhD Dissertation, 1994.

<sup>w</sup> <sup>x</sup> 32 A.R. Uhlig, Trap-driven memory simulation, Dissertation, Department of Electronic Engineering and Computer Sciences, University of Michigan, 1995, http:<sup>rr</sup>www. eecs.umich.edu<sup>r ;</sup> uhlig<sup>r</sup>thesis<sup>r</sup>index.html.

<sup>w</sup> <sup>x</sup> 33 D. Wessels, Intelligent caching for world-wide web objects, Thesis, University of Colorado, 1995a.

<sup>w</sup> <sup>x</sup> 34 D. Wessels, Harvest Project, 1995b, http:<sup>rr</sup>harvest.cs.colorado.edu<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 35 D. Wessels, Squid Cache Server, 1996a, http:<sup>rr</sup>www. nlanr.net<sup>r</sup>Squid<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 36 D. Wessels, NLANR Cache, 1996b, http:<sup>rr</sup>www. nlanr.net<sup>r</sup>Cache<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 37 S.H. Wildstrom, When the web gets too sticky, Business Week, December 8, 1997, p. 22.

<sup>w</sup> <sup>x</sup> 38 S. Williams, et al., Removal policies in network caches for world-wide web documents, The Association for Computing Machinery ACM 96 Conference, Stanford, CA, August Ž . 1996.

39 N. Yeager, R. McGrath, Web Server Technology: The Advanced Guide for World Wide Web Information Providers, Morgan Kaufmann Publishers, San Francisco, 1996.

<sup>w</sup> <sup>x</sup> 40 G.U. Yule, Mathematical theory of evolution, based on the conclusion of Dr. J.C. Willis, F.R.S., Philosophical Transactions B 213 1924 21–83.Ž .

<sup>w</sup> <sup>x</sup> 41 G.K. Zipf, Human Behavior and the Principle of Least Effort, Addison-Wesley, Cambridge, MA, 1949.

![](/api/attachments/HUGGV76D/fulltext/images/b329da6f89baf0ffdf06db783513fbf6ce65a7fce576354b5d2c4f8286fa9184.jpg)

Edward Watson is an Assistant Professor in the Department of Information Systems and Decision Sciences at Louisiana State University. His research interests and major publications are in the areas of enterprise systems, process modeling and engineering, performance analysis, and simulation modeling and analysis. He has a BS in Industrial Engineering and Operations Research from Syracuse University, and MS and PhD degrees in Industrial Engineering from

Penn State. He has 6 years of industry experience at General Motors and Systems Modeling, and has consulted for many companies on productivity and capacity problems. He is a member of DSI, INFORMS, SCS, and AIS.

![](/api/attachments/HUGGV76D/fulltext/images/925667753f440183aac49632749a38fbe59433504d24548cd1accb1c36d3a2fe.jpg)

Ying Shi is a Research Scientist at Exxon Chemical in the Data Processing Center. He received a PhD in Business Administration and a MS degree in Petroleum Engineering from Louisiana State University in 1983 and 1988, respectively. He also received a BS degree in Petroleum Engineering from Daqing Petroleum Institute in 1985. His current research interests focus on applications of stochastic modeling and simulation, Internet technologies and problems, and oil exploration.

![](/api/attachments/HUGGV76D/fulltext/images/68789249bd71b7d54bd8d9db16c69dbca818f6fcf8f5a2d6e2243e476a85dabd.jpg)

Ye-Sho Chen is a Professor in the Department of Information Systems and Decision Sciences at Louisiana State University. He received a BS in mathematics from National Cheng Kung University in Taiwan, an MS in statistics from National Tseng Hua University, and a PhD in Industrial Engineering with Operations Research Emphasis from Purdue University. His research interests and major publications are in data warehouse, information technology in small

business, and information productivity modeling. Dr. Chen has consulted for many companies on database and information productivity issues. Dr. Chen is a member of ACM, AIS, and INFORMS.
