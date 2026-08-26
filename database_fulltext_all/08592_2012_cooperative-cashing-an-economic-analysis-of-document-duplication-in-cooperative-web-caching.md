---
otero_id: 8592
otero_key: "RHAY5RGT"
title: "Cooperative Cashing? An Economic Analysis of Document Duplication in Cooperative Web Caching"
authors: "Kartik Hosanagar; Yong Tan"
year: "2012"
journal: "Information Systems Research"
doi: "10.1287/isre.1110.0347"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Cooperative Cashing? An Economic Analysis of Document Duplication in Cooperative Web Caching

Kartik Hosanagar

Operations and Information Management, The Wharton School of the University of Pennsylvania, Philadelphia, Pennsylvania 19103, kartikh@wharton.upenn.edu

Yong Tan Foster School of Business, University of Washington, Seattle, Washington 98195, ytan@uw.edu

ooperative caching is a popular mechanism to allow an array of distributed caches to cooperate and serve each others’ Web requests. Controlling duplication of documents across cooperating caches is a challenging problem faced by cache managers. In this paper, we study the economics of document duplication in strategic and nonstrategic settings. We have three primary findings. First, we find that the optimum level of duplication at a cache is nondecreasing in intercache latency, cache size, and extent of request locality. Second, in situations in which cache peering spans organizations, we find that the interaction between caches is a game of strategic substitutes wherein a cache employs lesser resources towards eliminating duplicate documents when the other caches employs more resources towards eliminating duplicate documents at that cache. Thus, a significant chal lenge will be to simultaneously induce multiple caches to contribute more resources towards reducing duplicate documents in the system. Finally, centralized decision making, which as expected provides improvements in average latency over a decentralized setup, can entail highly asymmetric duplication levels at the caches. This in turn can benefit one set of users at the expense of the other, and thus will be challenging to implement.

Key words: Web caching; cooperative caching; duplication in caching; analytical modeling; incentive-centered design; game theory

History: Paulo Goes, Senior Editor, Giri Kumar Tayi, Associate Editor; This paper was received on April 10, 2008, and was with authors 20 months for 3 revisions. Published online in Articles in Advance April 8, 2011.

## 1. Introduction

Web caching refers to the temporary storage of Web content somewhere between Web servers and clients in order to satisfy future requests from the nearby location (see Figure 1). Proxy caches, located at the gateways of large organizations and ISPs, play an important role in reducing latency (i.e., delay in content delivery) and bandwidth costs. Forrester Research prescribes caching as one of four best practices to improve performance for websites and ISPs (Gualteiri and Staten 2009).

Often, multiple caches in a network coordinate and share resources in order to serve each others’ requests (see Figure 2). This is also known as cooperative caching. When a cache does not have the requested data object, it can forward the request to a nearby cooperating cache that can serve the object faster than the origin server. The primary benefits of cache cooperation are higher hit rates<sup>1</sup> and lower average latency for end users. Cooperative caching is typically implemented across caches within an organization such as a large enterprise, ISP, or a content delivery network (CDN). Cache cooperation can sometimes span organizational boundaries, for example, with cache peering at exchanges such as Packet Clearing House and Equinix as well as implementations in the public domain such as IRCache and w3cache.<sup>2</sup>

A number of protocols have been proposed to help determine how caches should communicate and coordinate. These include Inter Cache Protocol (ICP), Cache Array Routing Protocol (CARP), Summary Cache and Home Protocol. ICP (Wessels and Claffy 1998), one of the first cooperative caching protocols to be supported in commercial proxy servers, lets each cache independently determine what objects to cache without accounting for content in other caches. This eliminates the need to coordinate, but can result in low array hit ratio because of duplication of objects across the caches. CARP (Valloppillil and Ross 1998), a protocol first used in Microsoft Proxy Server, assigns every data object to a designated cache based on a hash function. Each cache stores only those objects that it is designated to cache. This maximizes the number of objects collectively stored by the cache array. However, it can result in a low local hit ratio, e.g., when a popular object is always fetched from a remote cache. Ultimately, the end user is concerned with latency, which is a function of both local and array hit rates. To achieve a better balance, protocols that set duplication levels in between that achieved under ICP and CARP have also been proposed. Using trace-driven simulations, studies show that these protocols help balance the load of the caches and reduce user latency by 10%–20% (Wu and Yu 1999a, Zu and Subhlok 2003). Given the nontrivial gains realizable from tuning the duplication level, this is a key factor influencing the returns from cache cooperation.

Figure 1 A Proxy Web Cache  
![](/api/attachments/RHAY5RGT/fulltext/images/c19ce971a427ab2ac6c517ef8bb8ed4826d1b232088e0c029f22f18054d1953a.jpg)

Figure 2 Cooperative Caching  
![](/api/attachments/RHAY5RGT/fulltext/images/f0dd97e47b98dab148fe6854f2f8ec319585d37889ad31d135f2a6bdf841cbe8.jpg)

Recognizing that neither ICP nor CARP will consistently outperform the other, most proxy servers including Squid and Sun Java System proxy server currently support both ICP and CARP and let the system administrator select the protocol at deployment. System administrators can also set intermediate duplication levels using recent techniques that although not currently supported in commercial proxy servers, can be implemented with some additional effort such as through the logical partitioning of caches (Wu and Yu 1999a). The absence of a default setting in most proxy servers is because the optimal choice depends on the deployment context. This provides significant flexibility to administrators, but also imposes the additional burden of selecting the right level of duplication. Considerable experimentation is often needed to determine the appropriate choice.<sup>3</sup> The trade and academic press provide prescriptions ranging from “CARP versus ICP: 0 0 0 CARP is a genuine evolution of ICP, providing much better scalability and performance” (Northrup 1998, p. 515) to “ICP (has) considerably lower response time than CARP. The reason is the low local hit ratio of CARP” (Zu and Subhlok 2003).<sup>4</sup> Simultaneously, recent academic studies suggest that intermediate levels of duplication are desirable. These studies are based on simulations of distributed nonstrategic caches and the diversity of their conclusions reflects the diversity of the simulation settings. They do not develop a theory to help understand the fundamental trade-offs in determining duplication levels. Furthermore, they raise additional questions for the policymaker. For example, when should the cache manager use configurations that result in no duplication, unmonitored duplication, or some intermediate level of duplication? In the case of cache peering across organizations, what is the impact of strategic behavior on equilibrium duplication levels and latency? We conduct an economic analysis of document duplication to address these questions.

We study the problem in two ways. First, we develop analytical models to study document duplication in cooperative caching.<sup>5</sup> We make several assumptions that help specify a tractable model from which insights regarding the impact of various parameters can be derived. Second, we turn to trace-driven simulations to validate our findings under more realistic settings. The novelty of our analytic approach lies in the fact that we model the request process and caching decisions for the full set of documents in a cache to ultimately capture the impact of document duplication on expected latency. As a result, the economic model captures the operational details of cooperative caching protocols.

Our main contribution is the development of a formal framework with which to analyze the trade-offs associated with document duplication in cooperative Web caching. We arrive at three primary findings. First, we find that the optimum level of duplication is nondecreasing in intercache latency, cache size, and extent of request locality.<sup>6</sup> Correspondingly, zero duplication is preferable to unmonitored duplication when caches are close by and are smaller in size and requests exhibit low locality, and vice versa. Second, in situations in which cache peering spans organizations, we find that the interaction between caches is a game of strategic substitutes wherein a cache employs lesser resources towards eliminating duplicate documents when the other caches employ more resources towards eliminating duplicate documents. Thus, a significant challenge will be to simultaneously induce multiple caches to allocate resources towards reducing document duplication in the cache array. Finally, centralized decision making, as expected, provides improvements in latency over a decentralized setup. However, more significantly, it can entail highly asymmetric duplication levels at the caches. This in turn penalizes some users while benefiting others and thus raises implementation challenges.

The rest of the paper is organized as follows. In §2, we review the related literature. In §3, we develop a model to study optimal duplication in a setting with two caches. We apply the model to a variety of decision contexts, including decentralized and centralized decision contexts. In §4, we test the robustness of our results in two parts. First, we extend our analytical model and relax two key assumptions. Next, we use trace-driven simulations to validate our theoretical findings under a realistic environment. We conclude the study in §5.

## 2. Literature Review

Web caching has been a popular research stream in computer science and information systems. The two streams of work most relevant to our paper are the ones on (a) cooperative caching protocols with a particular emphasis on document duplication, and (b) management science research on caching.

2.1. Document Duplication in Cooperative Caching A number of protocols have been proposed to address cache coordination in cooperative caching. These include ICP, CARP, Summary Cache, Home, and Twoexit LRU among others.

In ICP (Wessels and Claffy 1998), each cache independently determines which objects to cache (e.g., each cache uses LRU).<sup>7</sup> Whenever there is a local miss, queries are sent to all other caches in the array. If any of the caches have the content, they respond with the content, else the request is forwarded to the origin server. A major disadvantage of ICP is that a large number of queries are sent, especially if the number of caches in the array is large. Summary Cache (Fan et al. 2000) and Cache Digest (Rousskov and Wessels 1998) address this by maintaining an index/directory of current content in all the caches. A local miss results in a lookup of the index, and the request is forwarded to the relevant cache. Several studies show that the indexes can be maintained with relatively low overheads if caches delay propagation of directory updates (Fan et al. 2000, Tewari et al. 1999). There is a high degree of duplication of objects in ICP, Summary Cache, and Cache Digest because the caches do not coordinate which objects to store. This results in low array hit ratio.

In CARP (Valloppillil and Ross 1998), every data object is assigned to a designated cache based on a hash function. Each cache stores only the objects it is designated to cache. This helps ensure that the maximum number of data objects is collectively stored in the array, resulting in a high array hit ratio. Furthermore, a local miss results in the request being forwarded to the designated cache alone, which implies lower query traffic. However, a primary disadvantage of CARP is that it has a low local hit ratio. For example, a popular document may be assigned to another cache, resulting in a local miss whenever the document is requested locally.

Figure 3 Controlling Duplication by Logical Partitioning of Caches  
![](/api/attachments/RHAY5RGT/fulltext/images/98a47a9e2551704659da932fe930ef247815f49b24d31b74037ad9cbc8f42c91.jpg)

Given the deficiencies of unmonitored duplication and zero duplication, recent research has proposed allowing some amount of duplication of documents across caches. Two-Exit LRU (Wu and Yu 1999a), Adaptable Controllable Replication (Wu and Yu 1999b), Home Protocol (Zu and Subhlok 2003) and Hosanagar and Tan (2004) all allow a cache to store its most popular documents irrespective of its presence in one or more other caches. These schemes often divide a cache into two regions, as shown in Figure 3. In the duplication region, a regular LRU scheme is used to store the most popular documents, independent of whether these documents also exist in the other caches. In the nonduplication region, the cache will not store a document if it exists in another cache. The decision of whether to store a document in the nonduplication region can be made using a hash function (Wu and Yu 1999a, b) or by using an index to confirm that the document is not in another cache (Hosanagar and Tan 2004).

In summary, the protocols differ along two main dimensions—communication overhead and level of duplication (see Table 1). In terms of communication overhead, ICP broadcasts queries to all caches in the array whenever there is a local miss, whereas the other protocols query caches in a targeted manner through either the use of directories or URL hashing. ICP is rarely used when there are a large number of caches in the array because of the communication overhead of broadcasting to all caches. When the array size is relatively manageable, this overhead of ICP is less of an issue. In terms of duplication, ICP, Summary Cache and Cache Digest do not monitor duplication levels, CARP does not permit duplication, and Two-Exit LRU and Home can set duplication to any value in between.

Our paper focuses exclusively on the level of duplication, and we do not evaluate overhead costs. This is partly because it is possible to use URL hashing or directories to achieve low communication overhead regardless of the level of duplication. For example, Two-exit LRU uses URL hashing to reduce communication overhead but can implement zero duplication and unmonitored duplication as special cases. Further, unlike communication overhead, of which less is always better, there is no universally preferred level of duplication. Therefore, we focus on the optimal level of duplication and investigate how it depends on various parameters. These arguments notwithstanding, a natural extension of our work is to focus on the issue of protocol selection by considering duplication levels, communication and storage overheads and other factors.

It is also worth noting that although many of the papers described above use simulations to demonstrate that controlled duplication often helps improve latency, they neither prescribe the optimal level of duplication nor do they provide a framework to understand the factors driving the optimal duplication levels. Further, even though cooperative caching is a decentralized process, they do not consider the strategic behavior of the caches. Our model complements these papers by developing a theoretical framework to better understand the tradeoffs in determining document duplication and the impact of strategic behavior on equilibrium outcomes. These insights can help cache operators select the best approach when deploying a network of peering caches.

2.2. Management Science Research on Web Caching There has been a lot of recent interest in web caching in the information systems (IS)/management science (MS) community. For a detailed overview of web caching from a management science perspective, we refer the reader to Datta et al. (2003). One important stream of work has focused on modeling the key operational decisions at proxy caches and demonstrated that performance improvements can be achieved through careful optimization. The key operational decisions at proxy caches include the rules to determine which objects to add to a cache (placement policy) and rules to determine which objects to remove when a new object is added (replacement policy). Fang et al. (2006) propose and test a prefetching technique for caches in a network storage system to prefetch objects that users are likely to request in the near future. Dutta et al. (2006) and Chiang et al. (2007) formulate models for identifying objects/fragments to cache and the frequency with which they should be replaced. Mookerjee and Tan (2002) analyze the performance of an LRU policy for browser caches. Kaya et al. (2009) propose an admission-control policy for proxy server caching that augments the LRU mechanism. Kumar and Norris (2008) propose a mechanism that takes into account aggregate patterns in user object requests and show that it can outperform LRU. Bose and Cheng (2000) show that proxy caching is beneficial if the hit rate exceeds a threshold, and identify the factors on which the threshold depends.

Table 1 Comparison of Cooperative Caching Protocols

<table><tr><td></td><td>ICP</td><td>Summary cache</td><td>Cache digest</td><td>CARP</td><td>Two-exit LRU</td><td>Home</td></tr><tr><td>Communication with other caches</td><td>Broadcast</td><td>Targeted (directory-based)</td><td>Targeted (directory-based)</td><td>Targeted (URL hashing)</td><td>Targeted (URL hashing)</td><td>Targeted (URL hashing)</td></tr><tr><td>Duplication</td><td>Unmonitored</td><td>Unmonitored</td><td>Unmonitored</td><td>Zero</td><td>Intermediate</td><td>Intermediate</td></tr></table>

The stream of work that is closely related to our paper is that studying the economics and operational aspects of distributed caching. Chan et al. (1999) and Chuang and Sirbu (2000) propose markets for QoSbased caching services and Hosanagar et al. (2005) study the design and pricing of these services. Geng et al. (2003) also discuss a cooperative caching market in which ISPs may trade cache capacity. More recently, Du et al. (2008) address the viability of a cache coordination network coordinated through an allocation hub. Cache networks can also be deployed by a central provider such as a content delivery network (CDN). Dogan et al. (2003) and Hosanagar et al. (2008) study pricing of CDNs that maintain a network of cooperating caches. In terms of operational issues, Tan et al. (2006) develop models for coordinating object placement decisions between browser and proxy-server caches, and Tawarmalani et al. (2009) and Kumar (2009) formulate and solve nonlinear programs to allocate objects in a cache array. The technologies and market mechanisms that facilitate distributed caching within and across organizational boundaries have clearly been of much interest to the management science community. Our paper contributes to this stream of work by studying the economics of document duplication in cooperative caching.

## 3. Analytical Model

We begin by stating our assumptions and introducing our notation. We analyze the case of two caches cooperating with each other. The caches are heterogeneous in terms of their sizes. Requests to the caches are independent. All documents are of the same size, and server download time for all the documents is the same. This assumption is for analytical tractability. In §4, we relax our assumptions and test the robustness of our findings using trace-driven simulations.

Request arrival at a cache is assumed to follow an inhomogeneous Poisson process. That is, the request arrivals for any document follows a Poisson distribution, but the mean arrival rates vary based on the time since the last request for the object. Although a Poisson arrival process at caches is commonly assumed in the literature (e.g., Che et al. 2002), it ignores locality in Web requests. We use an inhomogeneous Poisson process to address this shortcoming. In our model, the mean instantaneous access rate for a document with LRU age (time since the last request) x is assumed to be

$$
\theta (x) = \frac {1}{\alpha \cdot x + \beta}; \quad \alpha , \beta > 0; \alpha <   1.\tag{1}
$$

The parameter  measures the sensitivity of the access rate to the LRU age. A high value of  implies that LRU age is a good predictor of future requests, i.e., there is high locality in requests. Setting  = 0 models a regular Poisson process. With an inhomogeneous Poisson process, the probability density of a document with age x, i.e., the probability of having a document with LRU age x (Tan et al. 2006), is

$$
f (x) = \beta^ {(1 - \alpha) / \alpha} (1 - \alpha) (\alpha \cdot x + \beta) ^ {- 1 / \alpha}, \quad x > 0.\tag{2}
$$

The total mean access rate for the n documents (Tan et al. 2006) is:

$$
H _ {0} = n \int_ {0} ^ {\infty} \theta f (x) d x = \frac {1 - \alpha}{\beta} n.\tag{3}
$$

At any given instant, we can rank order the n documents based on their LRU age in a proxy cache. With a simple LRU policy, a cache of size R would have stored the top R documents. In the new scheme, the cache is divided into a duplication region of size L and a nonduplication region of size (R − L). The cache can store any document in the duplication region, but no duplication is allowed in the nonduplication region. Thus, the L most popular documents are stored in the duplication region regardless of whether these documents are in the other cache. However, document (L + 1) is stored in the cache only if it is not already present in the other cache. Similarly, for documents (L + 2) and onwards, the cache stores only those documents that are not present in the other cache. The advantage of this framework is that it incorporates zero duplication and unmonitored duplication as special cases (L = 0 and L = R, respectively). The setup is similar to the Two-Exit LRU scheme proposed by Wu and Yu (1999a, b) and a variant discussed by Hosanagar and Tan (2004). Wu and Yu (1999a) use a hash function like in CARP to determine which objects to store in the nonduplication region. Hosanagar and Tan (2004) adopt a variant that does not use a hash function, but instead verifies an object that is not in another cache by consulting a directory/index as in Summary Cache.

Figure 4 Objects Stored in Duplication and Nonduplication Regions of Cache 2  
![](/api/attachments/RHAY5RGT/fulltext/images/61c949ed500a24ea386021669d733a777a6b424c0011a7d5a1dc46543172dd27.jpg)

We sketch the implementation of both these schemes in the online appendix.<sup>8</sup> To fix a context, and also because it is harder to model hash functions analytically, our model below assumes a directory-based approach. Although we study the trade-offs under the directory-based approach, we expect that the fundamental trade-offs tied to duplication do not depend on the specific mechanism used to coordinate the nonduplication region.

Consider the configuration of cache 2 at some arbitrary instant. The indicator variable $\varphi _ { k }$ denotes whether document k exists in cache 1. That is, document k is tagged $\varphi _ { k } = 1$ if it is in cache 1 and $\varphi _ { k } = 0$ otherwise. If we rank order the documents by their LRU age in cache 2, the first $L _ { 2 }$ documents are stored in cache 2 irrespective of the value of $\varphi _ { k }$ for these documents. Let us denote the number of tagged documents among the first $L _ { 2 }$ documents by j. That is, $\begin{array} { r } { \sum _ { k = 1 } ^ { L _ { 2 } } \varphi _ { k } = j . } \end{array}$ For document $( L _ { 2 } + 1 )$ and higher, the document is stored only if $\varphi _ { k } = 0$ . Let i denote the number of documents that are skipped (i.e., not stored in cache 2 because they exist in cache 1) before the $( R _ { 2 } - L _ { 2 } ) !$ th document is encountered for the noduplication region. That is, the final document that is stored in cache 2 is the $( R _ { 2 } + i ) \mathrm { t h }$ document. Thus, $\begin{array} { r } { \sum _ { k = L _ { 7 } + 1 } ^ { R _ { 2 } + i } \varphi _ { k } = i . } \end{array}$ It is clear that if the size of the duplication region is reduced, the two caches collectively store more documents (i increases if the size of the duplication region decreases). Figure 4 represents the above-described schematic at a particular instant of time. The documents are sorted by their LRU age, and documents that are currently in cache 1 are shaded.

The probability of a request for a document is given by its mean arrival rate divided by the total request arrival rate at the cache, i.e., $\mathrm { P r o b } ( \mathrm { r e q u e s t } ) = \theta ( x _ { k } ) / H _ { 0 } .$ The latency experienced by a user of cache 2 for a given sorted arrangement of documents is

$$
\begin{array}{l} \Big (\sum_ {k = 0} ^ {L _ {2}} \frac {\theta (x _ {k})}{H _ {0}} \cdot 0 + \sum_ {k = L _ {2} + 1} ^ {R _ {2} + i - 1} \frac {\theta (x _ {k})}{H _ {0}} (\varphi_ {k} \cdot D + (1 - \varphi_ {k}) \cdot 0) \\ \qquad + \sum_ {k = R _ {2} + i + 1} ^ {n} \frac {\theta (x _ {k})}{H _ {0}} (\varphi_ {k} \cdot D + (1 - \varphi_ {k})) \Big). \end{array}\tag{4}
$$

For the first $L _ { 2 }$ documents, all requests are satisfied by the cache, and hence the delay is 0. For documents $( L _ { 2 } + 1 )$ through $( R _ { 2 } + i - 1 )$ , the document may be in cache 2 or in cache 1. If the document is in cache 1 $( \varphi _ { k } = 1 )$ , then the document can be fetched from cache 1 with a delay of D. If the document is not tagged $( \varphi _ { k } = 0 )$ , then the document is returned from the local cache with no delay. Document $( R _ { 2 } + i )$ is in cache 2, and hence incurs no delay. Finally, documents $( R _ { 2 } + i + 1 )$ through n may either be fetched from cache 1 if they are tagged $( \varphi _ { k } = 1 )$ for a delay of D or fetched from the origin server $( \varphi _ { k } = 0 )$ for a delay of 1. Without loss of generality, the server delay is normalized to 1. If the intercache latency were greater than server delay, then cooperating does not make sense, implying that $D \in [ 0 , \bar { 1 } ]$ . The expected latency for a user of cache 2 is given by averaging Equation (4) over all possible values of document ages $\{ x _ { 1 } \in [ 0 , \infty ] , x _ { 2 } \in [ x _ { 1 } , \infty ] , \ldots , x _ { n } \in [ x _ { n - 1 } , \infty ] \}$ and all possible combinations of $\{ i , j \}$

$$
\begin{array}{l} E L _ {2} = \sum_ {j = 0} ^ {\min (L _ {2}, R _ {1})} \sum_ {i = 0} ^ {R _ {1} - j} p (j, i) E _ {\varphi | j, i} \\ \cdot n! \int_ {0} ^ {\infty} f (x _ {1}) d x _ {1} \int_ {x _ {1}} ^ {\infty} f (x _ {2}) d x _ {2} \dots \int_ {x _ {n - 1}} ^ {\infty} f (x _ {n}) d x _ {n} \\ \cdot \left(\sum_ {k = L _ {2} + 1} ^ {R _ {2} + i - 1} \frac {\theta (x _ {k})}{H _ {0}} \varphi_ {k} \cdot D + \sum_ {k = R _ {2} + i + 1} ^ {n} \frac {\theta (x _ {k})}{H _ {0}} \right. \\ \left. \cdot (\varphi_ {k} \cdot D + (1 - \varphi_ {k}))\right) \end{array} \tag {5}
$$

$E L _ { 2 }$ denotes the expected latency at cache 2. $p ( j , i )$ is the probability that there are j tagged documents among the first $L _ { 2 }$ documents and i tagged documents before the $( R _ { 2 } - L _ { 2 } )$ th untagged document is encountered for the no-duplication region. We also define an operator, $\mathbf { E } _ { \varphi \mid j , i } ,$ that allows us to consider all possible combinations in which documents can be tagged for a given j and i.

The decision problem faced by the cache operator is to select the value of $L _ { 2 }$ that minimizes the expected latency. In the proceeding analysis, we investigate the solution of this decision problem. In §3.1, we begin with a problem in which cache 2 makes a duplication decision given that cache 1 uses a traditional LRU policy $( L _ { 1 } = R _ { 1 } )$ . This can refer to a scenario in which cache 1 is not strategic about optimal duplication levels, or one in which cache 2 considers the worst-case outcome, wherein cache 1 makes no effort to reduce duplication in the array.<sup>9</sup> In §3.2, we optimize the duplication levels at both caches. We consider both decentralized and centralized decision contexts. We summarize our notation in Table 2.

Table 2 Glossary of Terms

<table><tr><td>n</td><td>Total number of documents on the Web</td></tr><tr><td> $R_i$ </td><td>Size of cache i (expressed as number of documents the cache can store)</td></tr><tr><td> $L_i$ </td><td>Size of “duplication region”(also in terms of number of documents)</td></tr><tr><td>D</td><td>Delay incurred in fetching a document from other cache, D &lt; 1</td></tr><tr><td> $x_k$ </td><td>LRU age (time since last request) for document k</td></tr><tr><td> $\theta(x_k)$ </td><td>Instantaneous rate of access for a document with LRU age  $x_k$ . $\theta(x_k) = 1/(\alpha \cdot x_k + \beta); \quad \alpha, \beta > 0; \alpha < 1$ </td></tr><tr><td> $f(x_k)$ </td><td>Probability density of a document with LRU age  $x_k$ </td></tr><tr><td> $H_0$ </td><td>The total mean access rate at the cache</td></tr><tr><td> $\phi_k$ </td><td>Indicator variable set to 1 if document k is currently in cache 1 or  $\phi_k = 0$  otherwise</td></tr><tr><td>p(j,i)</td><td>Probability that there are j tagged documents in the duplication region and i tagged documents before the ( $R_2L_2$ )th untagged document is encountered for the no-duplication region</td></tr><tr><td> $EL_i$ </td><td>Expected latency at cache i</td></tr></table>

3.1. Optimal Duplication Under LRU at Cache 1 In this section, we assume that cache 1 uses a regular LRU policy. Cache 2 breaks up its cache into duplication and no-duplication regions. Under these assumptions, the probability $p ( j , i )$ is

$$
p (j, i) = \binom{L _ {2}}{j} \binom{R _ {2} - L _ {2} + i - 1}{i} \binom{n - R _ {2} - i}{R _ {1} - j - i} \cdot \binom{n}{R _ {1}} ^ {- 1},\tag{6}
$$

where $j \in \{ 0 , \ldots , L _ { 2 } \}$ and $i \in \{ 0 , \ldots , R _ { 1 } - j \}$ . In the above expression, the number of ways in which we can tag j documents in the duplication region is ${ \binom { L _ { 2 } } { j } } .$ i documents between $( L _ { 2 } + 1 ) \mathrm { t h }$ and $( R _ { 2 } + i - 1 ) \mathrm { t h }$ h is $\binom { R _ { 2 } - L _ { 2 } + i - 1 } { i }$ ; and $( R _ { 1 } - j - i )$ documents between $( R _ { 2 } +$ $i + 1 ) \mathrm { t h }$ and n-th is $\binom { n - R _ { 2 } - i } { R _ { 1 } - j - i }$ (see Figure 4). The total number of ways to tag $' R _ { 1 }$ documents in the sorted list of n documents is $\scriptstyle { \binom { n } { R _ { 1 } } }$

The constraints on the binary indicator variables are $\begin{array} { r } { \sum _ { k = L _ { 7 } + 1 } ^ { R _ { 2 } + i - 1 } \varphi _ { k } = i , } \end{array}$ and $\begin{array} { r } { \sum _ { k = R _ { 2 } + i + 1 } ^ { n } \varphi _ { k } = R _ { 1 } - j - i . } \end{array}$ . In Appendix $\scriptstyle \mathbf { A } ,$ we have explicitly evaluated Equation (5) under these assumptions to arrive at the following expression for the expected delay at cache 2:

$$
\begin{array}{c} E L _ {2} = \frac {R _ {1}}{n} \cdot D \cdot w (n, L _ {2}) + \sum_ {j = 0} ^ {L _ {2}} \sum_ {i = 0} ^ {R _ {1} - j} p (j, i) \\ \cdot \frac {n - R _ {2} - R _ {1} + j}{n - R _ {2} - i} w (n, R _ {2} + i), \end{array}\tag{7}
$$

where w $( x , y ) = ( 1 - y / x ) ^ { 1 / ( 1 - \alpha ) }$ . When $R / n$ is small, we can approximate the above expression, as shown in Appendix A:

$$
E L _ {2} = \frac {R _ {1}}{n} w (n, L _ {2}) \cdot D + \left(1 - \frac {R _ {1}}{n}\right) w \left(n, R _ {2} + R _ {1} \cdot \frac {R _ {2} - L _ {2}}{n - R _ {1}}\right).\tag{8}
$$

The expected delay may be interpreted as $E L _ { 2 } =$ Pr(request satisfied locally) · 0 + Pr(request satisfied by cache 1) · D + Pr(request satisfied by origin server) · 1. Note that $( R _ { 1 } / n ) w ( n , L _ { 2 } )$ is decreasing in $L _ { 2 }$ and $( 1 - R _ { 1 } / n ) w ( n , R _ { 2 } + R _ { 1 } \cdot ( R _ { 2 } - L _ { 2 } / n - R _ { 1 } ) )$ is increasing in $L _ { 2 } .$ This observation highlights the main trade-off in choosing the size of duplication region $\left( L _ { 2 } \right) :$ : if the cache manager increases $L _ { 2 } ,$ more requests get satisfied locally, fewer requests are satisfied at cache 1, and a greater proportion of requests go to the origin server. In other words, the local hit rate increases but array hit rate decreases. ICP and Summary Cache attempt to maximize the local hit rate and set $L _ { 2 } = R _ { 2 }$ $\mathrm { C A R } \bar { \mathrm { P } }$ attempts to maximize the array hit rate and sets $L _ { 2 } = 0$ . The expected latency depends on both the local and array hit rates.

<sup>Proposition</sup> <sup>1.</sup> Zero duplication is preferable to unmonitored duplication for $D < D _ { T h }$ and vice versa, where

$$
\begin{array}{r l} & D _ {T h} = \left(\frac {n}{R _ {1}} - 1\right) \\ & \qquad \cdot \bigg [ \frac {(1 - R _ {2} / n) ^ {1 / (1 - \alpha)} - (1 - R _ {2} / (n - R _ {1})) ^ {1 / (1 - \alpha)}}{1 - (1 - R _ {2} / n) ^ {1 / (1 - \alpha)}} \bigg ]. \end{array}
$$

The proof is in Appendix B. Given that most proxy servers support both ICP and CARP and let the cache operator select the duplication level, Proposition 1 provides an important qualitative insight to guide the decision. Specifically, zero duplication is preferable to unmonitored duplication when intercache latency (D) or request locality () are low. The finding can be explained as follows. At high intercache latency, there are limited gains from fetching an object from another cache in the event of a local miss. So the emphasis is on maximizing local hit rate through unmonitored duplication. In contrast, at low intercache latency, an array hit is almost as effective as a hit from the local cache. Therefore, the emphasis is on maximizing the array hit rate through zero duplication. Similarly, when request locality is very high, the locality is best exploited by ensuring that recently requested objects are stored locally as opposed to eliminating them if they exist in another cache. Thus, unmonitored duplication is preferred at high locality. The converse is true at low locality.

The optimal duplication level corresponds to the value of $L _ { 2 }$ that minimizes the expected latency. That is, $L _ { 2 } ^ { * } = \operatorname* { m i n } _ { L _ { 2 } } \{ E L _ { 2 } \}$ . The objective function is globally convex in $L _ { 2 } .$ . The minimization problem has a closedform solution given by

Figure 5 Impact of Intercache Latency and Request Locality on Optimal Duplication  
![](/api/attachments/RHAY5RGT/fulltext/images/853881a9f3a00aee5b6129a45ebed06946601be09512083e3ce1391f2dac4c1d.jpg)

$$
L _ {2} ^ {*} = n - \frac {n \cdot (n - R _ {2})}{(n - R _ {1}) \cdot D ^ {(1 / \alpha) - 1} + R _ {1}}.\tag{9}
$$

Equation (9) is always less than the cache size $R _ { 2 }$ However, the expression may sometimes result in a negative value. Incorporating the nonnegativity constraint, the proposition follows.

<sup>Proposition</sup> <sup>2.</sup> The optimal size of the duplication region is given by

$$
L _ {2} ^ {*} = \max \bigg (0, n - \frac {n \cdot (n - R _ {2})}{(n - R _ {1}) \cdot D ^ {\alpha^ {- 1} - 1} + R _ {1}} \bigg).\tag{10}
$$

<sup>Corollary</sup> <sup>1.</sup> The optimal size of the duplication region is (a) nondecreasing in the intercache wait time, $D ;$ (b) nondecreasing in request locality; (c) nondecreasing in the size of the other cache, $R _ { 1 } ;$ and (d) nondecreasing in cache size $R _ { 2 } ^ { } ,$

The proofs are in Appendix B. In Figure 5, we illustrate results (a) and (b) from Corollary 1 for a case in which $\{ n = 5 , 0 0 0 , \ : R _ { 1 } = 5 0 0 , \ : R _ { 2 } = 4 0 0 \}$ . When $D = 0 ,$ i.e., there is no perceivable difference between fetching the document from the local cache or the other cache, then $L _ { 2 } ^ { * } = 0$ . That is, there will be no duplication of content, and a scheme like CARP is desirable. For small intercache latencies, zero duplication continues to perform well. However, as the intercache latency increases, it is optimal for the cache manager to allow some duplication in order to ensure that the most popular documents are locally stored irrespective of their presence in the other cache.<sup>10</sup>

Now consider the impact of request locality. Recall that a high value of  implies that LRU age is a good predictor of future requests. Thus, as  increases, it becomes appealing to always store the items with the lowest LRU age. Eliminating a recently requested document just because it exists in the other cache can result in significant decline in local hit rates, which in turn drives up the latency. As a result, we observe that $( L _ { 2 } ^ { * } / R _ { 2 } )$ weakly increases with .

Finally, consider the impact of the cache sizes. If the size of either cache increases, the overall capacity of the array also increases. The additional capacity in the array reduces the negative impact of duplication, resulting in an increase in $L _ { 2 } .$ A clear recommendation from Corollary 1 is that policies with zero or low duplication of content (CARP, Two-Exit LRU with small duplication, etc.) are recommended when the caches are located close by, cache capacity is limited, and temporal locality in requests is relatively low (all else constant). When caches are geographically farther apart, temporal locality is high, and the cache capacities are high, then greater levels of duplication are preferred.

<sup>Corollary</sup> <sup>2.</sup> Unmonitored duplication $( L _ { i } = R _ { i } )$ is optimal if $D = 1$ or $\alpha = 1 .$ , and no duplication $( L _ { i } = 0 )$ is optimal if $D ^ { \alpha ^ { - 1 } - 1 } \leq 1 - R _ { 2 } / ( n - R _ { 1 } )$

Corollary 2 indicates that unmonitored duplication (e.g., ICP, Summary Cache) is optimal if the intercache latency or request locality is high. Conversely, zero duplication $( \mathrm { e . g . }$ , CARP) is optimal when intercache latency and request locality are low. This is consistent with Proposition 1. Proposition 1 identified the conditions under which zero duplication is better than unmonitored duplication, and vice versa. In contrast, Corollary 2 identifies the conditions under which these decisions are optimal. In short, Proposition 1 informs a cache operator considering only zero or unmonitored duplication, whereas Corollary 2 informs an operator willing to expend the effort to logically partition the caches to achieve any level of duplication. Figure 6 plots the expected latency at cache 2 with zero duplication $( L _ { 2 } = 0 )$ , unmonitored duplication $( L _ { 2 } = R _ { 2 } )$ , and optimal duplication $( L _ { 2 } = L _ { 2 } ^ { * } )$ . The remaining parameters are $\bar  \{ n = 5 , 0 0 0$

Figure 6 Average Latency with Different Duplication Schemes  
![](/api/attachments/RHAY5RGT/fulltext/images/9fbac7cf09b5b8ca003421ee35f6b243b590081ed8941215a2800f1124879319.jpg)

$R _ { 1 } = 5 0 0 , R _ { 2 } = 4 0 0 , \alpha = 0 . 9 5 \}$ . It is clear that there exist a wide range of parameters under which it is optimal for the cache operator to select unmonitored duplication or zero duplication. At the same time, choosing the wrong duplication level $( \mathrm { e . g . }$ , choosing unmonitored duplication when no duplication is optimal) can result in significant deterioration of performance. The expected latency with optimal duplication traces the inner envelope of the latency curves of unmonitored and zero duplication and provides the maximum benefit at intermediate levels of intercache latencies.

Our results highlight how various factors, including intercache latency and request locality, affect the optimal duplication levels. We now turn to the optimization of duplication levels at both caches.

## 3.2. Optimizing Duplication at Both Caches

We evaluate the problem under two decision scenarios. The first is a setting in which the duplication decisions are decentralized, i.e., made independently at each cache. Whenever cooperative caching spans organizational boundaries, it is expected that individual organizations choose policies that are locally optimal (i.e., minimize latency for their own users). For example, this corresponds to a situation in which two ISPs may peer with one another at bilateral peering points or at exchanges such as Packet Clearing House and Equinix. Cooperative caching implementations in the public domain, such as IRCache and w3cache, are also relevant here. The second decision setting is a centralized one, which corresponds to a situation in which an ISP or a large organization implements cooperative caching across its proxy servers.

3.2.1. Decentralized Coordination. When both caches are strategic, we need to compute each cache’s best response to the other cache’s decision in order to compute the equilibrium outcomes. The expression for expected latency is the same as Equation (5). However, $p ( j , i )$ , the probability that there are j tagged documents among the first $L _ { 2 }$ documents and i tagged documents before the $( R _ { 2 } - L _ { 2 } )$ )th untagged document is encountered for the no-duplication region, has a different functional form. This is because the number of documents collectively stored increases as cache 1 reduces the size of its duplication region $L _ { 1 } .$ . Under this game structure, $p ( j , i )$ can be computed as shown in Appendix C:

$$
p (j, i) = \binom{L _ {2}}{j} \binom{R _ {2} - L _ {2} + i - 1}{i} \binom{n - R _ {2} - i}{R _ {1} - j - i} \binom{R _ {1} - j}{L _ {1} - j}
$$

$$
\cdot \binom{n - L _ {2}}{R _ {1} - L _ {1}} ^ {- 1} \binom{n + L _ {1} - R _ {1}}{L _ {1}} ^ {- 1}.\tag{11}
$$

Combining Equations (11) and (5) and simplifying as shown in Appendix $C ,$

$$
\begin{array}{l} E L _ {2} = \frac {1}{n - L _ {2}} \left(R _ {1} - \frac {L _ {1} L _ {2}}{n + L _ {1} - R _ {1}}\right) \cdot D \cdot w (n, L _ {2}) \\ \qquad + \sum_ {j = 0} ^ {L _ {2}} \sum_ {i = 0} ^ {R _ {1} - j} p (j, i) \frac {n - R _ {2} - R _ {1} + j}{n - R _ {2} - i} w (n, R _ {2} + i) \end{array}\tag{12}
$$

where $w ( x , y ) = ( 1 - ( y / x ) ) ^ { 1 / ( 1 - \alpha ) }$

As before, we can interpret (12) as the probability that the request goes to cache 1 times $D ,$ plus the probability that the request goes to the origin server times 1. Assuming that $R _ { 1 } / n$ and $R _ { 2 } / n$ are small, we further show that (12) can be approximated by

$$
\begin{array}{l} E L _ {2} = \frac {1}{n - L _ {2}} \bigg (R _ {1} - \frac {L _ {1} L _ {2}}{n + L _ {1} - R _ {1}} \bigg) \cdot D \cdot w (n, L _ {2}) \\ \qquad + \bigg (1 - \frac {1}{n - L _ {2}} \bigg (R _ {1} - \frac {L _ {1} L _ {2}}{n + L _ {1} - R _ {1}} \bigg) \bigg) \\ \qquad \cdot w \bigg (n, R _ {2} + \frac {R _ {1} (n + L _ {1} - R _ {1}) - L _ {1} L _ {2}}{n + L _ {1} - L _ {2} - R _ {1}} \frac {R _ {2} - L _ {2}}{n - R _ {1}} \bigg). \end{array}\tag{13}
$$

The response function for cache 2 can be computed by $L _ { 2 } ^ { * } ( L _ { 1 } ) \stackrel { \bullet } { = } \operatorname* { m i n } _ { L } \{ E L _ { 2 } \}$ . Similarly, the response function for cache 1 is obtained by setting up the expression for the expected latency at cache 1, $E L _ { 1 } ,$ , and solving $L _ { 1 } ^ { * } ( L _ { 2 } ) { \stackrel { - } { = } } \operatorname* { m i n } _ { L _ { 1 } } \{ E L _ { 1 } \}$ . Unfortunately, these decision problems have no closed-form solutions. However, the following property of the response functions can be derived.

<sup>Proposition</sup> <sup>3.</sup> The best-response curves, $L _ { 2 } ^ { * } ( L _ { 1 } )$ and $L _ { 1 } ^ { * } ( L _ { 2 } )$ , are nonincreasing in $L _ { 1 }$ and $L _ { 2 } ,$ respectively. Further, the existence of an equilibrium is guaranteed.

The proof is in Appendix C. The response functions are nonincreasing. Thus, this is a game of strategic substitutes wherein a reduction of the duplication region at one cache results in an expansion of the duplication region at the other.<sup>11</sup> Proposition 3 highlights a key result regarding the nature of the strategic interaction between caches. If a cache allocates more resources towards eliminating duplicate documents, this creates an incentive for the other cache to free-ride and increase the size of its own duplication region. This can be explained as follows. A small increase in the size of the duplication region at a cache (say, cache 2) provides a benefit in the form of a slight increase in the local hit rate, but also imposes a cost in the form of a slight increase in requests forwarded to the origin server (due to a drop in the array hit rate). However, the latter cost is relatively small when the other cache (cache 1) reduces the size of its duplication region. This allows cache 2 to reduce the size of its duplication region without having to deal with a significant increase in requests forwarded to the original server. As a result, it is hard to simultaneously induce both caches to contribute greater resources towards reducing duplicate documents in the system in the absence of additional incentives such as payments.

Figure 7 Best-Response Curves and Equilibrium Duplication Levels for the Two Caches  
![](/api/attachments/RHAY5RGT/fulltext/images/a70857c175a557ba2401a7c0caf78fd393ad6d0e391f8fd65477084369ede345.jpg)

Although there is no closed-form solution for the equilibrium values, they can be evaluated numerically.<sup>12</sup> Figure 7 plots the response curves of the two caches when $\{ n = 5 , 0 0 0 , \ R _ { 1 } = 5 0 0 , \ R _ { 2 } = 4 0 0 , \ \alpha = 0 . 9 ,$ and $D = 0 . 5 \}$ . The equilibrium solution is given by $\{ L _ { 1 } ^ { * } = 1 9 7 , L _ { 2 } ^ { * } = 9 2 \}$ . The equilibrium $L _ { 2 } ^ { * }$ is higher than would be the case if cache 1 uses a regular LRU policy $( L _ { 2 } ^ { * } = 7 1$ when $L _ { 1 } = 5 0 0 )$ . The fact that cache 2 is aware that cache 1 has an incentive to reduce $L _ { 1 }$ results in an increase in $L _ { 2 } .$

<sup>Proposition</sup> <sup>4.</sup> The best-response curves, $L _ { 2 } ^ { * } ( L _ { 1 } )$ and $L _ { 1 } ^ { * } ( L _ { 2 } ) .$ , are both nondecreasing in intercache latency, D.

Holding the other player’s choice of L fixed, the size of the duplication region at a cache weakly increases with intercache latency. This does not imply that equilibrium duplication levels are nondecreasing in D. In Figure 8, we illustrate that the equilibrium duplication levels can decrease with D even though the response curves $L _ { 2 } ^ { * } ( L _ { 1 } )$ and $L _ { 1 } ^ { * } ( L _ { 2 } )$ are monotonically nondecreasing in D. This result can be explained as follows. A decrease in D may cause one cache to lower the size of its duplication region, L. However, because the cache’s decisions are strategic substitutes, there is a second-order effect wherein a decrease in the size of the duplication region by one cache encourages the other to increase L, resulting in the nonmonotonicity in equilibrium.

Figure 8 Monotonic Response Functions and Nonmonotonic Equilibria  
![](/api/attachments/RHAY5RGT/fulltext/images/aefbb42ce9a987468fc050d786244b5f35ee6f8da1ac5efe4168909a7b735cf6.jpg)

Finally, Figure 9 plots the average latency at cache 2 under the equilibrium and contrasts it with the average latency when both caches choose zero duplication and both choose unmonitored duplication. The remaining parameters are $\{ n = 5 , 0 0 0 , \ \bar { R } _ { 1 } = 5 0 0$ $R _ { 2 } = 4 0 0 , \alpha = 0 . 9 5 \}$ . As before, choosing unmonitored duplication when zero duplication is optimal (and vice versa) can result in significant performance deterioration. Also, the average latency under the equilibrium again traces the inner envelope of the latency curves of unmonitored and zero duplication and provides the maximum benefit at intermediate levels of intercache latencies. These results are qualitatively similar to Figure 6 and they help underscore the fact that tuning the duplication levels can provide significant gains even under strategic behavior.

We now explore the optimal duplication levels chosen by a central planner and contrast the solution with the equilibrium duplication levels computed above.

3.2.2. Centralized Coordination. Consider a central planner that sets the optimal duplication level at each cache in order to minimize overall latency in the system (i.e., maximize social welfare). The decision

Figure 9 Average Latency with Different Duplication Schemes  
![](/api/attachments/RHAY5RGT/fulltext/images/800965c4130fa7d60ffb2cffd161eb82a689fd8a55e62244236e53ccd8a91b1b.jpg)

problem can be stated as

$$
\min _ {L _ {1}, L _ {2}} \left(\frac {H _ {1} \cdot E L _ {1} + H _ {2} \cdot E L _ {2}}{H _ {1} + H _ {2}}\right),\tag{14}
$$

where $H _ { 1 }$ and $H _ { 2 }$ are the request arrival rates at caches 1 and 2, respectively, and are specified by Equation (3). The objective function represents the average latency experienced in the system, which is a weighted sum of the average latencies at the individual caches. Assuming the same values for  and $\beta$ at the two caches, the decision problem is $\mathrm { m i n } _ { L _ { 1 } , L _ { 2 } } ( E L _ { 1 } + E L _ { 2 } ) / 2$

In Table 3, we present the solution for different values of intercache latency and request locality. The remaining parameters are $\{ n = 5 , 0 0 0 ,$ $R _ { 1 } = 5 0 0 , R _ { 2 } = 4 0 0 \}$ . For moderate values of intercache latency, we observe that the centralized solution entails greater resource commitment from cache 2 (i.e., low $L _ { 2 } )$ and lower commitment from cache 1 (high $L _ { 1 } )$ . Setting L to a very low value at one cache ensures minimal duplication of documents across the two caches. The central planner can then set a high value of L at the other cache $( \mathrm { i . e . , }$ , an LRU-like policy) to ensure low latency at that cache. Thus, the social optimum may entail penalizing users at one cache in order to ensure very low average latency at the other. When cooperative caching is done by independent organizations, it is not clear whether solutions with such asymmetric resource commitment can be implemented in the absence of additional mechanisms such as payments.<sup>13</sup>

For each of the parameter values in Table 3, we also computed the expected latency under the centralized and decentralized setups. The expected latency under the centralized setup is 0.00%–3.00% lower than that achieved under decentralized decision making. As expected, centralized decision making is better.

## 3.3. Discussion

Our analysis yields a number of insights for cache operators. First, we find that even if other caches do not do much to monitor duplication, a selfish cache may still want to take steps to control duplication. Thus, free-riding (setting $L = R )$ need not be optimal even if other caches do not attempt to eliminate duplicate documents. The primary trade-off associated with duplication is as follows: if the cache operator does not monitor duplication and chooses a placement/replacement policy that is locally optimal, then it maximizes the local hit rate but also results in fewer requests being satisfied at other caches. At the same time, eliminating documents that are currently stored elsewhere has the risk of lowering local hit rate. As a result, the cache operator may benefit from controlling duplication even when other caches take no such action.

Table 3 Socially Optimal Duplication Levels $( R _ { 1 } = 5 0 0 , R _ { 2 } = 4 0 0 )$

<table><tr><td rowspan="2">D</td><td colspan="2"> $\alpha = 0.85$ </td><td colspan="2"> $\alpha = 0.90$ </td><td colspan="2"> $\alpha = 0.95$ </td></tr><tr><td> $L_{1}^{*}$ </td><td> $L_{2}^{*}$ </td><td> $L_{1}^{*}$ </td><td> $L_{2}^{*}$ </td><td> $L_{1}^{*}$ </td><td> $L_{2}^{*}$ </td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0.1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.01</td><td>0</td></tr><tr><td>0.2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>150.65</td><td>45.95</td></tr><tr><td>0.3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>233.70</td><td>133.98</td></tr><tr><td>0.4</td><td>0</td><td>0</td><td>106.57</td><td>0</td><td>294.85</td><td>196.89</td></tr><tr><td>0.5</td><td>51.12</td><td>0</td><td>190</td><td>80.43</td><td>343.38</td><td>245.95</td></tr><tr><td>0.6</td><td>162.21</td><td>33.39</td><td>263.10</td><td>160.50</td><td>383.71</td><td>286.20</td></tr><tr><td>0.7</td><td>244.81</td><td>135.15</td><td>329.76</td><td>230.28</td><td>418.28</td><td>320.38</td></tr><tr><td>0.8</td><td>330.27</td><td>228.7</td><td>390.85</td><td>292.37</td><td>448.58</td><td>350.09</td></tr><tr><td>0.9</td><td>415.52</td><td>316.44</td><td>447.32</td><td>348.52</td><td>475.59</td><td>376.39</td></tr><tr><td>1</td><td>500</td><td>400</td><td>500</td><td>400</td><td>500</td><td>400</td></tr></table>

We also find that there exist a range of settings in which it might just suffice to choose one of two extreme solutions. Specifically, zero duplication is optimal at low intercache latencies or low levels of request locality. Conversely, unmonitored duplication is optimal at high intercache latencies or high levels of request locality. Choosing zero (unmonitored) duplication when unmonitored (zero) duplication is optimal can have an adverse impact and negate much of the value from cache cooperation. This observation is particularly important because most proxy servers, including Squid and Sun Java Proxy Server, support both zero and unmonitored duplication and leave the specific choice to the cache operator. Cache operators must be careful in selecting the right setting. Finally, at intermediate values of request locality and intercache latency, the extra effort of implementing two-exit policies may be justified. The size of the duplication region in these two exit policies is nondecreasing in request locality, intercache latency, and cache sizes.

Cooperative caching can be implemented within large organizations as with an ISP with multiple proxy servers, or across organizations as with bilateral peering among ISPs and cache peering at exchanges like Equinix. A key question here relates to the impact of strategic behavior on the success of cache peering. Our analysis provides a few insights here as well. First, we find that the interaction among strategic caches is a game of strategic substitutes. That is, it is best for a cache to employ lesser resources towards eliminating duplicate documents when other caches employ more resources towards reducing document duplication. Thus, it may be hard to simultaneously induce multiple caches to contribute towards the best global performance in the absence of mechanisms such as payments and audits. We also find, as expected, that centralized decision making does better than decentralized decision making. More importantly, the size of the duplication regions under this centralized setup can be highly asymmetric. This in turn can benefit users connected to the cache with the largest duplication region while penalizing users who are connected to the cache that has the smallest duplication region. This has the potential to be perceived as unfair by one set of users. Thus, issues of fairness may need to be addressed when implementing the optimal centralized decision.

All of the above insights are derived from a model in which we make several simplifying assumptions for tractability. We now test the robustness of these insights by relaxing several of the key assumptions made in this section.

## 4. Robustness of Results

We approach robustness tests in two parts. First, we test the robustness of the analytical findings from §3.1 by relaxing two key independence assumptions in our two-cache setup: (i) intercache latency is independent of traffic, (ii) requests are independent at the two caches. These assumptions are relaxed within the framework of our analytical model. Next, we evaluate the findings tied to centralized versus decentralized coordination in a setting with more than two caches and with real-world request traces. These tests are conducted within a simulation environment.

## 4.1. Extending Analytical Model to Relax Independence Assumptions

4.1.1. Traffic-Dependent Intercache Delay. In $\ S 3 ,$ the intercache latency is assumed to be independent of the traffic between the two caches. However, traffic can influence the waiting and processing times for requests at a cache and thereby affect the overall latency. We now explicitly model the waiting/processing time at a cache as a function of the traffic.

In Equation (8), $( R _ { 1 } / n ) w ( n , L _ { 2 } )$ is the probability that documents are fetched from cache 1. Because $( 1 - \alpha / \beta ) n$ is the total demand, $\lambda = ( 1 - \alpha / \beta ) n$ $( R _ { 1 } / n ) w ( n , L _ { 2 } )$ is the mean traffic intensity to cache 1. If  denotes the mean service time at cache 1 $( \mathrm { i . e . , }$ service rate is $\mu = 1 / \tau )$ , then the mean time in the system for requests forwarded to cache 1 is given by

$$
{\frac {1}{\mu - \lambda}} = {\frac {\tau}{1 - ((1 - \alpha / \beta) n (R _ {1} / n) w (n , L _ {2})) \tau}}.
$$

Thus, the expression for expected latency at cache 2 is

$$
\begin{array}{l} E L _ {2} = \frac {R _ {1}}{n} w (n, L _ {2}) \bigg (D + \frac {\tau}{1 - ((1 - \alpha / \beta) R _ {1} w (n , L _ {2})) \tau} \bigg) \\ \qquad + \bigg (1 - \frac {R _ {1}}{n} \bigg) w \bigg (n, R _ {2} + R _ {1} \cdot \frac {R _ {2} - L _ {2}}{n - R _ {1}} \bigg). \end{array}
$$

The cache operator’s decision problem is $L _ { 2 } ^ { * } =$ $\mathrm { m i n } _ { L _ { 2 } } \{ E L _ { 2 } \}$ . There is no closed-form solution for $L _ { 2 } ^ { * }$ However, applying the conjugate pairs theorem, we can show that:

<sup>Proposition</sup> <sup>5.</sup> With traffic-dependent intercache latency, the optimal size of the duplication region is (a) nondecreasing in the intercache delay D, (b) nondecreasing in request locality  for  below some positive threshold, (c) nondecreasing in cache size $R _ { 2 } ,$ (d) nondecreasing in cache size $R _ { 1 } ,$ and (e) nondecreasing in mean service time .

The proof is in Appendix D. These results are consistent with the results of §3. However, if  is very high, the result regarding request locality can change signs, as highlighted in the appendix. That the size of the duplication region is nondecreasing in the mean service time  is expected because the value from cooperative caching reduces when the other proxy cache takes too long to process requests. Consequently, the cache operator is better off ensuring that the requests for popular documents get serviced locally.

4.1.2. Correlated Demand. In §3.1, the expression for p4j1 i5 assumes that requests at the two caches are independent. Here, we relax the assumption to consider positively correlated requests. For arbitrary correlation structures, it is hard to derive an analytical expression for the expected latency, so we consider a specific form below.

In the original model, the number of tagged documents (j) in cache $2 ^ { \prime } \mathrm { s }$ duplication region varies from zero to $L _ { 2 } ,$ and the probability distribution of j is obtained by assuming that requests are independent. If requests are positively correlated, we are more likely to see higher values of j than the lower values. Thus the probability density around low values of j reduces and that around high values of j increases. To model this, we truncate the parameter j by removing its small values. That is, j varies from min(l1 $L _ { 2 } )$ to $L _ { 2 } .$ . A low value of l is close to our original independence assumption, and a high value indicates that the popular items at cache 2 are likely to also be in cache 1. Specifically, we modify the probability $p ( j , i )$ as follows:

$$
p _ {c} (j, i) = \binom{L _ {2}}{j} \binom{R _ {2} - L _ {2} + i - 1}{i} \binom{n - R _ {2} - i}{R _ {1} - j - i} \cdot N F ^ {- 1},
$$

where $l \leq j \leq L _ { 2 }$ and $0 \leq i \leq R _ { 1 } - j .$ NF is a normalization factor such that $\begin{array} { r } { \sum _ { j = l } ^ { L _ { 2 } } \cdot \sum _ { i = 0 } ^ { R _ { 1 } - j } p _ { c } ( j , i ) = 1 } \end{array}$

Under this new model, the expected delay can be computed in the same manner as in $\ S 3$ . The new expression is

$$
\begin{array}{c} E L _ {2} = D \frac {R _ {1} - \varphi}{n} \bigg (1 - \frac {L _ {2}}{n} \bigg) ^ {\alpha / (1 - \alpha)} + \bigg (1 - \frac {R _ {1} - \varphi}{n - L _ {2}} \bigg) \\ \cdot \bigg (1 - \frac {n R _ {2} - L _ {2} (R _ {1} + R _ {2} - \varphi)}{n (n - L _ {2} - R _ {1} + \varphi)} \bigg) ^ {1 / (1 - \alpha)}, \end{array}
$$

Figure 10 Impact of Correlated Requests on Optimal Duplication  
![](/api/attachments/RHAY5RGT/fulltext/images/6a962291460ed2449b149f2780185cf3912bba3072580521094ac4281281d18f.jpg)

where

$$
\begin{array}{c} \varphi = l + \big (_ {3} F _ {2} \big (2, 1 + l - L _ {2}, 1 + l - R _ {1}; 2 + l, \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \cdot \big (_ {3} F _ {2} (1, l - L _ {2}, l - R _ {1}; 1 + l, 1 + l + n - L _ {2} - R _ {1}; 1) \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad (l + 1) (1 + l + n - L _ {2} - R _ {1}) \big) ^ {- 1}, \end{array}
$$

and ${ } _ { a } F _ { b } ( )$ denotes the HyperGeometric function.

The optimal value $L _ { 2 } ^ { * }$ that minimizes $E L _ { 2 }$ can be obtained numerically. Figure 10 shows that the size of the duplication region is nonmonotonic with the correlation parameter l $( \alpha = 0 . 9 5 , D = 0 . 4 )$ . Figure 11 shows that the size of the duplication region is nondecreasing in the intercache latency and request locality $( n = 5 , \bar { 0 } 0 0 , \ R _ { 1 } = 5 0 0 , \ R _ { 2 } = 4 0 0 , \ l = 4 0 )$ . These results are consistent with those in §3.

## 4.2. Simulations

In this section, we use trace-driven simulations to evaluate our findings under more realistic requests and with multiple caches. We used a large request stream collected on January 09, 2007 by the Urbana-Champaign proxy server of the IRCache project.<sup>14</sup> The trace consists of 423,968 requests for 207,206 unique URLs submitted by users of the proxy server. The log reports the size of the response as well as the response time for each request. For size, the trace records number of bytes written to the client rather than size of the data object. Because header sizes vary across requests, there can be minor variations in size across requests for the same URL. In accord with Kelly et al. (1999), we define the size of a URL as the maximum recorded transfer size among all requests for it and assume that the URLs remain unchanged throughout the day. The object sizes in our trace range from

Figure 11 Impact of Intercache Latency and Locality on Optimal Duplication  
![](/api/attachments/RHAY5RGT/fulltext/images/63045835dc6e49f2aa71d543c1dcfe2555281c30afdc9027f9e71c25ce5a6143.jpg)

0.2 KB to 129 MB, with an average size of 26.71 KB. Because the trace does not report the origin server’s response time during cache hits, we use the maximum recorded response time for a URL as the origin server’s response time for that URL.

All requests in the trace are generated by users of a single proxy cache. In order to test cooperative caching schemes, we create M caches in any simulation run (M is an input parameter) and randomly assign the users in the log file to one of the M caches. Once users are assigned, requests at individual caches are generated in accordance with the sequence and timing specified in the trace. The intercache latency is fixed as a constant fraction, D, of the origin server’s response time for a URL. All caches are initially empty and are populated in accordance with the two-exit policy discussed in §3. The results from the first 25,000 requests at any cache are discarded to eliminate data from the initial period when caches are not yet full.

The input parameters for the simulation are the number of caches (M), the caches sizes $( R _ { i } ) ,$ and the ratio D. Other parameters are determined by the trace. In the simulations, we considered the cases of two, four, and five caches $( M \in \{ 2 , 4 , 5 \} )$ as well as a variety of cache sizes. Below, we report results for $M = 4$ and asymmetric cache sizes $\begin{array} { r } { \bar { ( } R _ { 1 } = 6 2 . 6 ~ \mathrm { M B } , } \end{array}$ $R _ { 2 } = 8 3 . 4$ MB, $\overset { \cdot } { R _ { 3 } } = 1 0 4 . 4$ MB, $R _ { 4 } = 1 2 5 . 2 2 ~ \mathrm { M B } )$ . The smallest cache is $2 , 4 0 0$ times the average size of an object in our trace and the largest cache is $4 { , } 8 0 0$ times the average size of an object. The results are qualitatively similar for other values. In contrast, our results are sensitive to the intercache latency. Hence, we report the results for a range of D.

Our simulations test four policies. The first two policies are $L _ { i } = 0$ and $L _ { i } = R _ { i }$ . The third policy allows each cache to independently determine a locally optimal $L _ { i }$ and evaluates the performance at the resulting equilibrium. There is no simple method to compute the equilibrium in our multicache simulations. We consider an iterative best-response procedure. To determine the best response for cache i (i.e., optimal $L _ { i }$ given $L _ { - i } ) ,$ , we use simulations to compute the expected latency at cache i for all candidate values of $L _ { i } . ^ { 1 5 }$ The optimal $L _ { i }$ minimizes the expected latency at cache i. Given a starting point ${ \cal L } ^ { 0 } { } = ( L _ { 1 } , L _ { 2 } , \ldots , L _ { M } )$ , the iterative best-response procedure sequentially optimizes the duplication levels of caches 1 through M and repeats the process until the duplication levels converge. In order to account for the possibility of multiple equilibria, we consider several randomly chosen starting points $L ^ { 0 }$ The fourth policy we consider is the socially optimal duplication level. We exhaustively consider all possible values of $( L _ { 1 } , L _ { 2 } , \dots , L _ { _ { M } } )$ and choose the one that minimizes the average latency in the cache array.<sup>16</sup>

In Table 4, we report the average latency in the cache array under each of the four policies. The average latency under zero duplication and unmonitored duplication are in the first two columns. The column labeled “Equilib.” presents the average latency realized in equilibrium with decentralized decision making. The socially optimal policy is labeled “Min.” We additionally report the maximum expected latency observed during our exhaustive evaluation of all possible $( L _ { 1 } , L _ { 2 } , \dots , L _ { _ { M } } )$ . This maximum latency along with the socially optimal value help benchmark the other three policies. For consistency with §3, the expected latency under a regime where all requests are forwarded to the origin server is normalized to 1. In accord with the results in $\ S 3 ,$ , we find that policies with zero duplication $( L _ { i } = 0 )$ are desirable at low intercache latency and policies with unmonitored duplication $( L _ { i } = R _ { i } )$ are desirable at high latencies and that optimizing duplication levels provides benefits over both policies. As expected, there are costs to decentralized decision making, although they are somewhat low. Finally, we investigated the shape of the best-response function by comparing the best response at each cache obtained during the iterative procedure. Specifically, we did a pairwise comparison of all computed $L _ { i } ^ { * } ( \bar { \sum _ { j = 1 \dots M , j \neq i } } L _ { j } )$ at each cache. Providing support for the observation that this is a game of strategic substitutes, 86.33% of these pairwise comparisons were nondecreasing.

In summary, we find that the key insights from the analytical model continue to hold in the trace-driven simulations.

Table 4 Expected Latency from Different Duplication Policies

<table><tr><td rowspan="2"></td><td colspan="5">Average latency</td></tr><tr><td> $L_i=0$ </td><td> $L_i=R_i$ </td><td>Equilib.</td><td>Min</td><td>Max</td></tr><tr><td>D=0.0</td><td>0.568</td><td>0.590</td><td>0.568</td><td>0.568</td><td>0.590</td></tr><tr><td>D=0.2</td><td>0.606</td><td>0.597</td><td>0.585</td><td>0.582</td><td>0.606</td></tr><tr><td>D=0.4</td><td>0.644</td><td>0.606</td><td>0.598</td><td>0.595</td><td>0.644</td></tr><tr><td>D=0.6</td><td>0.683</td><td>0.614</td><td>0.611</td><td>0.610</td><td>0.683</td></tr><tr><td>D=0.8</td><td>0.721</td><td>0.623</td><td>0.623</td><td>0.623</td><td>0.721</td></tr><tr><td>D=1.0</td><td>0.759</td><td>0.635</td><td>0.635</td><td>0.635</td><td>0.759</td></tr></table>

## 5. Conclusions

Tuning the level of duplication across cooperating caches is a key operational decision for cache operators. They may choose to not monitor duplication (e.g., by choosing ICP, Summary Cache, or Cache Digest), have zero duplication across caches $( \mathrm { e . g . } ,$ by choosing CARP), or expend additional effort to achieve intermediate levels of duplication $( \mathrm { e . g . , }$ Home, Two-Exit LRU). The optimal decision depends on the deployment context, and operators have to experiment considerably before making the decision. We develop a model to study the relevant trade-offs and generate insights regarding optimal duplication in strategic and nonstrategic settings.

Our study represents an initial foray into understanding the trade-offs tied to document duplication. However, the study has several limitations. First, although our study provides several insights regarding optimal duplication levels, protocol selection in cooperative caching requires additional considerations. One of these relates to overheads associated with the different protocols. As mentioned earlier, ICP queries all caches upon a local miss, and thus generates significant query traffic when the cache array is large. Thus, ICP is undesirable for large cache arrays. Furthermore, Summary cache and Cache Digest require use of directories. This imposes overheads tied to maintaining the directories and also storing them. Fortunately, these issues have received considerable attention. For example, studies show that the directories can be maintained with low overheads if caches delay propagation of directory updates. Further, directories can be stored in a compact manner by using Bloom filters. URL hashing used in CARP, Two-Exit LRU, and Home do not have these communication and storage overheads, with the latter two protocols capable of implementing any level of duplication. However, known challenges with URL hashing are the significant disruption every time a cache is added or removed, and achieving even load distribution among proxy caches. Recent work on consistent hashing proposes several solutions to these hash disruption issues. These considerations need to be factored into protocol selection. Future work can look at protocol selection more holistically after accounting for all relevant factors including duplication, overheads, and implementation complexity.

Another limitation of our work is that we assume that proxy caches are always closer than the origin server. In global-scale caches, this is not always true, and a key challenge is that of proxy pruning, namely, selecting between remote proxies and the origin server. Our model does not account for this. We also do not consider cache hierarchies, and instead assume all caches are at the same level. Incorporating proxy pruning and cache hierarchies into our framework is clearly of value. Finally, a promising direction for future work is the study of mechanisms to ensure that the socially optimal duplication levels can be attained in practice under decentralized decision making. Such a study can provide prescriptions for contracting and auditing in cooperative caching.

## Electronic Companion

An electronic companion to this paper is available as part of the online version at http://dx.doi.org/10.1287/ isre.1110.0347.

## Appendix A. Expected Latency

<sup>Result</sup> <sup>A.1.</sup> In order to derive a simple expression for the expected latency, we will first prove the following result:

$$
\begin{array}{c} n! \int_ {0} ^ {\infty} f (x _ {1})   d x _ {1} \dots \int_ {x _ {n - 1}} ^ {\infty} f (x _ {n})   d x _ {n} \sum_ {k = m + 1} ^ {n} \frac {\theta (x _ {k})}{H _ {0}} \\ = \frac {n - m}{n} \prod_ {l = n - m + 1} ^ {n} \left(1 + \frac {\alpha}{l \cdot (1 - \alpha)}\right) ^ {- 1}. \end{array}\tag{A.1}
$$

<sup>Proof.</sup> Plugging Equations (1) and (2) into the left-hand side of the above expression and simplifying, we get:

$$
\begin{array}{l} n! \int_ {0} ^ {\infty} f (x _ {1})   d x _ {1} \dots \int_ {x _ {n - 1}} ^ {\infty} f (x _ {n})   d x _ {n} \sum_ {k = m + 1} ^ {n} \frac {\theta (x _ {k})}{H _ {0}} \\ \qquad = n! \bigg (\frac {1}{\alpha} - 1 \bigg) ^ {n} \frac {1}{\beta} \frac {1}{H _ {0}} \sum_ {k = m + 1} ^ {n} \prod_ {j = 1} ^ {n - k} \frac {1}{j (1 / \alpha - 1)} \\ \qquad \cdot \prod_ {i = n - k + 1} ^ {n} \frac {1}{i (1 / \alpha - 1) + 1}. \end{array}\tag{A.2}
$$

Relabeling with the new index $k ^ { \prime } = n - k + 1$ (hereafter, the prime is omitted)

$$
= n! \left(\frac {1}{\alpha} - 1\right) ^ {n} \frac {1}{\beta} \frac {1}{H _ {0}} \sum_ {k = 1} ^ {n - m k - 1} \prod_ {j = 1} \frac {1}{j (1 / \alpha - 1)} \prod_ {i = k} ^ {n} \frac {1}{i (1 / \alpha - 1) + 1}.\tag{A.3}
$$

By induction, we have

$$
\sum_ {k = 1} ^ {l} \prod_ {j = 1} ^ {k - 1} \frac {1}{j (1 / \alpha - 1)} \prod_ {i = k} ^ {l} \frac {1}{i (1 / \alpha - 1) + 1} = \frac {\alpha}{(1 / \alpha - 1) ^ {l - 1} (l - 1) !}.\tag{A.4}
$$

Substituting Equation (A.4) into Equation (A.3), we have

$$
\begin{array}{l} = n! \bigg (\frac {1}{\alpha} - 1 \bigg) ^ {n} \frac {1}{\beta} \frac {1}{H _ {0}} \frac {\alpha}{(1 / \alpha - 1) ^ {n - m - 1} (n - m - 1) !} \\ \cdot \prod_ {l = n - m + 1} ^ {n} \frac {1}{l (1 / \alpha - 1) + 1} \\ = \bigg (1 - \frac {m}{n} \bigg) \prod_ {l = n - m + 1} ^ {n} \bigg (1 + \frac {\alpha}{l (1 - \alpha)} \bigg) ^ {- 1}. \quad \text { Q.E.D. } \end{array}\tag{A.5}
$$

Hence proved.

## Expected Latency

We will now proceed to evaluate the expected latency. The expected latency in cache 2 is formulated in Equation (5). It can be restated as

$$
\begin{array}{l} E L = \sum_ {j = 0} ^ {\min (L _ {2}, R _ {1})} p (j) \cdot \sum_ {i = 0} ^ {R _ {1} - j} p (i | j) E _ {\varphi | j, i} \int_ {0} ^ {\infty} f (x _ {1}) d x _ {1} \dots \int_ {x _ {n - 1}} ^ {\infty} f (x _ {n}) d x _ {n} \\ \qquad \cdot \bigg (\sum_ {k = L _ {2} + 1} ^ {R _ {2} + i - 1} \frac {\theta (x _ {k})}{H _ {0}} \varphi_ {k} \cdot D + \sum_ {k = R _ {2} + i + 1} ^ {n} \frac {\theta (x _ {k})}{H _ {0}} (\varphi_ {k} \cdot D + (1 - \varphi_ {k})) \bigg), \end{array}\tag{A.6}
$$

where we have merely substituted $p ( j , i ) = p ( j ) \cdot p ( i | j )$ into Equation (5).

To simplify the above expression, we begin by looking at the probability that there are j tagged documents among the first $L _ { 2 }$ documents:

$$
p (j) = \sum_ {i = 0} ^ {R _ {1} - j} p (j, i) = \binom{L _ {2}}{j} \binom{n - L _ {2}}{R _ {1} - j} \cdot \binom{n}{R _ {1}} ^ {- 1}.\tag{A.7}
$$

Because ${ \binom { m } { k } } = 0$ for $k < 0$ and $k > m ,$ it follows that $p ( j ) = 0$ for $j > \mathrm { m i n } ( L _ { 2 } , R _ { 1 } )$ . We apply this result later in this section. Using $( \mathrm { A } . 7 ) .$ , we can also derive the conditional probability of having i tagged documents among the documents ranked from the $( L _ { 2 } + 1$ )th to the $\left( R _ { 2 } + i - 1 \right)$ )th:

$$
p (i \mid j) = \frac {p (j , i)}{p (j)} = \binom {R _ {2} - L _ {2} + i - 1} {i} \binom {n - R _ {2} - i} {R _ {1} - j - i} \cdot \binom {n - L _ {2}} {R _ {1} - j} ^ {- 1}.\tag{A.8}
$$

Now note that the $( R _ { 2 } + i )$ th document cannot be tagged because it is stored in cache 2. Similarly, given values of j and i, each document k has a probability of

$$
\mathbf {E} _ {\varphi ; j, i} \circ \varphi_ {k} = \left\{ \begin{array}{l l} \frac {i}{R _ {2} - L _ {2} + i - 1}, & \text { if } L _ {2} + 1 \leq k \leq R _ {2} + i - 1; \\ \frac {R _ {1} - j - i}{n - R _ {2} - i}, & \text { if } k \geq R _ {2} + i + 1 \end{array} \right.\tag{A.9}
$$

of being tagged. The above expression follows directly from Figure 4. In the figure, note that there are i tagged documents in the no-duplication region and $( R _ { 1 } - j - i )$ tagged documents among the final $( n - R _ { 2 } - i )$ documents. It can be verified that

$$
\begin{array}{l} \sum_ {i = 0} ^ {R _ {1} - j} p (i \mid j) \frac {i}{R _ {2} - L _ {2} + i - 1} = \frac {R _ {1} - j}{n - L _ {2}} \quad \text { and } \\ \sum_ {i = 0} ^ {R _ {1} - j} p (i \mid j) \frac {R _ {1} - j - i}{n - R _ {2} - i} = \frac {R _ {1} - j}{n - L _ {2}}. \end{array}\tag{A.10}
$$

That is, the probability that any random document outside the duplication-allowed region is tagged (given j tagged documents in duplication region) is $( R _ { 1 } - j ) / ( n - L _ { 2 } )$

By combining Equations (A.1) and (A.9), we get

$$
\begin{array}{l} T 1 = \mathbf {E} _ {\varphi ; j, i} \circ n! \int_ {0} ^ {\infty} f (x _ {1}) d x _ {1} \dots \int_ {x _ {n - 1}} ^ {\infty} f (x _ {n}) d x _ {n} \\ \cdot \left(\sum_ {k = L _ {2} + 1} ^ {R _ {2} + i - 1} \frac {\theta (x _ {k})}{H _ {0}} \varphi_ {k} D + \sum_ {k = R _ {2} + i + 1} ^ {n} \frac {\theta (x _ {k})}{H _ {0}} (\varphi_ {k} D + (1 - \varphi_ {k}))\right) \\ = \frac {i}{R _ {2} - L _ {2} + i - 1} \cdot D \left(\frac {n - L _ {2}}{n} \prod_ {l = n - L _ {2} + 1} ^ {n} \left(1 + \frac {\alpha}{l \cdot (1 - \alpha)}\right) ^ {- 1} - \frac {n - R _ {2} - i + 1}{n} \prod_ {l = n - R _ {2} - i + 2} ^ {n} \left(1 + \frac {\alpha}{l \cdot (1 - \alpha)}\right) ^ {- 1}\right) \\ + \left(\frac {R _ {1} - j - i}{n - R _ {2} - i} \cdot D + \frac {n - R _ {2} - R _ {1} + j}{n - R _ {2} - i}\right) \frac {n - R _ {2} - i}{n} \\ \cdot \prod_ {l = n - R _ {2} - i + 1} ^ {n} \left(1 + \frac {\alpha}{l \cdot (1 - \alpha)}\right) ^ {- 1}. \end{array} \tag {A.11}
$$

Averaging the above expression over i and simplifying,

$$
\begin{array}{l} T 2 = \sum_ {i = 0} ^ {R _ {1} - j} p (i | j) \cdot T 1 = \frac {R _ {1} - j}{n} \prod_ {l = n - L _ {2} + 1} ^ {n} \left(1 + \frac {\alpha}{l \cdot (1 - \alpha)}\right) ^ {- 1} \cdot D \\ \qquad + \frac {n - R _ {2} - R _ {1} + j}{n} \sum_ {i = 0} ^ {R _ {1} - j} p (i | j) \prod_ {l = n - R _ {2} - i + 1} ^ {n} \left(1 + \frac {\alpha}{l \cdot (1 - \alpha)}\right) ^ {- 1}, \end{array}\tag{A.12}
$$

which can be further reduced, after averaging over j to yield,<sup>17</sup>

$$
\begin{array}{l} E L = \sum_ {j = 0} ^ {\min (L _ {2}, R _ {1})} p (j) \cdot T 2 = \sum_ {j = 0} ^ {L _ {2}} p (j) \cdot T 2 = \frac {R _ {1}}{n} \frac {n - L _ {2}}{n} \\ \cdot \prod_ {l = n - L _ {2} + 1} ^ {n} \left(1 + \frac {\alpha}{l \cdot (1 - \alpha)}\right) ^ {- 1} \cdot D + \sum_ {j = 0} ^ {L _ {2}} \sum_ {i = 0} ^ {R _ {1} - j} p (j, i) \\ \cdot \frac {n - R _ {2} - R _ {1} + j}{n} \prod_ {l = n - R _ {2} - i + 1} ^ {n} \left(1 + \frac {\alpha}{l \cdot (1 - \alpha)}\right) ^ {- 1}. \end{array}\tag{A.13}
$$

Upon further simplification, we get

$$
\begin{array}{l} E L = \frac {R _ {1}}{n} \cdot D \cdot w (n, L _ {2}) \\ \qquad + \sum_ {j = 0} ^ {L _ {2}} \sum_ {i = 0} ^ {R _ {1} - j} p (j, i) \frac {n - R _ {2} - R _ {1} + j}{n - R _ {2} - i} w (n, R _ {2} + i), \end{array}\tag{A.14}
$$

where $w ( x , y ) = ( 1 - ( y / x ) ) ^ { 1 / ( 1 - \alpha ) }$

When $R \ll n ,$ , we can expand

$$
w (n, R _ {2} + i) \approx 1 - \frac {1}{1 - \alpha} \frac {R _ {2} + i}{n} + \frac {1}{2} \frac {\alpha}{(1 - \alpha) ^ {2}} \left(\frac {R _ {2} + i}{n}\right) ^ {2}.\tag{A.15}
$$

<sup>17</sup> Because $p ( j ) = 0 \mathrm { f o r } j > \mathrm { m i n } ( L _ { 2 } , R _ { 1 } )$ , it follows that $\begin{array} { r } { \sum _ { j = 0 } ^ { \operatorname* { m i n } ( L _ { 2 } , R _ { 1 } ) } p ( j ) } \end{array}$ $\begin{array} { r } { T 2 = \sum _ { j = 0 } ^ { L _ { 2 } } p ( j ) \cdot T 2 } \end{array}$

Substituting this into (A.14), the expected latency can be approximated by

$$
E L = \frac {R _ {1}}{n} \cdot D \cdot w (n, L _ {2}) + \left(1 - \frac {R _ {1}}{n}\right) w \left(n, R _ {2} + R _ {1} \cdot \frac {R _ {2} - L _ {2}}{n - R _ {1}}\right).\tag{A.16}
$$

## Appendix B

<sup>Proposition</sup> <sup>1.</sup> Zero duplication $( C A R P )$ is preferable to unmonitored duplication $( I C P ) f o r D < D _ { T h }$ and vice versa, where

$$
D _ {T h} = \left(\frac {n}{R _ {1}} - 1\right) \left[ \frac {(1 - R _ {2} / n) ^ {1 / (1 - \alpha)} - (1 - R _ {2} / (n - R _ {1})) ^ {1 / (1 - \alpha)}}{1 - (1 - R _ {2} / n) ^ {1 / (1 - \alpha)}} \right].
$$

<sup>Proof.</sup> The expected latency is given by $E L _ { 2 } \ =$ $( R _ { 1 } / n ) w ( n , L _ { 2 } ) \quad \cdot \quad \stackrel { \cdot } { D } \quad + \quad ( 1 - \stackrel { \cdot } { R _ { 1 } } / n ) w ( n , R _ { 2 } + R _ { 1 } \cdot ( R _ { 2 } - L _ { 2 } /$ $n - R _ { 1 } ) )$ . In the case of zero duplication, we have

$$
E L _ {2} (L _ {2} = 0) = \frac {R _ {1}}{n} D + \left(1 - \frac {R _ {1}}{n}\right) \left(1 - \cdot \frac {R _ {2}}{n - R _ {1}}\right) ^ {1 / (1 - \alpha)}.
$$

Similarly, with $L _ { 2 } = R _ { 2 } ,$ , we have

$$
E L _ {2} \left(L _ {2} = R _ {2}\right) = \frac {R _ {1}}{n} D \left(1 - \cdot \frac {R _ {2}}{n}\right) ^ {1 / 1 - \alpha} + \left(1 - \frac {R _ {1}}{n}\right) \left(1 - \cdot \frac {R _ {2}}{n}\right) ^ {1 / 1 - \alpha}.
$$

Equating the two expressions for the expected latency, we get the $D _ { T h }$ specified in Proposition 1.

<sup>Proposition</sup> <sup>2.</sup> The optimal size of the duplication region is $L _ { 2 } ^ { * } = \operatorname * { m a x } ( 0 , n - ( n \cdot ( n - \dot { R } _ { 2 } ) ) / ( ( n - \dot { R } _ { 1 } ) \cdot D ^ { \alpha ^ { - 1 } - 1 } + R _ { 1 } ) )$

<sup>Proof.</sup> The objective function is

$$
\begin{array}{l} \underset {L _ {2}} {\text { Min }} \{E L \} = \underset {L _ {2}} {\text { Min }} \bigg \{D \cdot \frac {R _ {1}}{n} w (n, L _ {2}) \\ \qquad + \bigg (1 - \frac {R _ {1}}{n} \bigg) w \bigg (n, R _ {2} + R _ {1} \cdot \frac {R _ {2} - L _ {2}}{n - R _ {1}} \bigg) \bigg \}, \end{array}\tag{B.1}
$$

where $w ( x , y ) = ( 1 - y / x ) ^ { 1 / ( 1 - \alpha ) }$ . The first-order condition (FOC) leads to the following expression for the optimal size of the duplication region:

$$
L _ {2} ^ {*} = n - \frac {n \cdot (n - R _ {2})}{\left((n - R _ {1}) \cdot D ^ {(\alpha^ {- 1} - 1)} + R _ {1}\right)}.\tag{B.2}
$$

We will first verify that $L _ { 2 } ^ { * } \leq R _ { 2 }$ is always satisfied. Plugging in the expression for $L _ { 2 } ^ { * }$ into this condition, we get $L _ { 2 } ^ { * } \leq R _ { 2 }$ if and only if (iff)

$$
n - \frac {n \cdot (n - R _ {2})}{(n - R _ {1}) \cdot D ^ {(1 / \alpha) - 1} + R _ {1}} \leq R _ {2}\tag{B.3}
$$

$$
\Rightarrow (n - R _ {1}) \cdot D ^ {(1 / \alpha) - 1} + R _ {1} \leq n,\tag{B.4}
$$

i.e., iff $D ^ { ( \alpha ^ { - 1 } - 1 ) } \leq 1 \qquad $ . This is guaranteed because $D \leq 1$ and $\alpha < 1 \ \mathrm { b y }$ definition. Thus, $\bar { L } _ { 2 } ^ { * } \leq R _ { 2 }$ is always guaranteed. However, the expression may sometimes give negative values. In such cases, the lowest latency for $\breve { L } _ { 2 } \in [ 0 , \breve { R } _ { 2 } ]$ is realized at $L _ { 2 } = 0 .$ Thus, it follows that

$$
L _ {2} ^ {*} = \max \left(0, n - \frac {n \cdot (n - R _ {2})}{(n - R _ {1}) \cdot D ^ {\alpha^ {- 1} - 1} + R _ {1}}\right). \quad \text { Q.E.D. }
$$

<sup>Corollary</sup> <sup>1.</sup> The optimal size of the duplication region is (a) nondecreasing in the intercache wait time, D; (b) nondecreasing in request locality; (c) nondecreasing in the size of the other cache $R _ { 1 } ;$ and (d) nondecreasing in cache size $R _ { 2 } .$

<sup>Proof.</sup> (a) Impact of intercache latency $D \colon$

$$
\begin{array}{c} \frac {\partial}{\partial D} \bigg (n - \frac {n \cdot (n - R _ {2})}{((n - R _ {1}) \cdot D ^ {(\alpha^ {- 1} - 1)} + R _ {1})} \bigg) \\ = \frac {(1 - \alpha) \cdot D ^ {1 / \alpha} n (n - R _ {1}) (n - R _ {2})}{\alpha (D ^ {1 / \alpha} (n - R _ {1}) + D R _ {1}) ^ {2}} \geq 0. \end{array}\tag{B.5}
$$

Thus, $n - ( n \cdot ( n - R ) ) / ( ( n - R ) \cdot D ^ { ( \alpha ^ { - 1 } - 1 ) } + R )$ is nondecreasing in $D ,$ implying that L<sup>∗</sup> is also nondecreasing in intercache latency D.

(b) Impact of request locality (5:

Proof.

$$
\begin{array}{c} \frac {\partial}{\partial \alpha} \bigg (n - \frac {n \cdot (n - R _ {2})}{((n - R _ {1}) \cdot D ^ {(\alpha^ {- 1} - 1)} + R _ {1})} \bigg) \\ = \frac {D ^ {(1 + \alpha) / \alpha} n (n - R _ {1}) (n - R _ {2}) \cdot \mathrm{Log} (1 / D)}{(\alpha D ^ {1 / \alpha} (n - R _ {1}) + \alpha D R _ {1}) ^ {2}} \geq 0. \end{array}\tag{B.6}
$$

Thus, it follows that $L _ { 2 } ^ { * }$ is nondecreasing in .

(c) Impact of $R _ { 1 } ,$ , the size of the other cache. Q.E.D

Proof.

$$
\begin{array}{c} \frac {\partial}{\partial R _ {1}} \bigg (n - \frac {n \cdot (n - R _ {2})}{((n - R _ {1}) \cdot D ^ {(\alpha^ {- 1} - 1)} + R _ {1})} \bigg) \\ = \frac {D ^ {2} n (n - R _ {2}) (1 - D ^ {(1 / \alpha) - 1})}{(D ^ {1 / \alpha} (n - R _ {1}) + D R _ {1}) ^ {2}} \geq 0. \end{array}\tag{B.7}
$$

Thus, it follows that $L _ { 2 } ^ { * }$ is nondecreasing in $R _ { 1 }$ .

(d) Impact of cache size $R _ { 2 }$

$$
\begin{array}{c} \frac {\partial}{\partial R _ {2}} \bigg (n - \frac {n \cdot (n - R _ {2})}{((n - R _ {1}) \cdot D ^ {(\alpha^ {- 1} - 1)} + R _ {1})} \bigg) \\ = \frac {D n}{(D ^ {1 / \alpha} (n - R _ {1}) + D R _ {1})} \geq 0 \end{array}\tag{B.8}
$$

Thus, it follows that $L _ { 2 } ^ { * }$ is non-decreasing in $R _ { 2 }$ . Q.E.D.

Appendix C

The first $L _ { 1 }$ documents from cache 1 can be located anywhere in the sorted list at cache 2 (i.e., documents sorted by LRU age at cache 2), whereas the next $( R _ { 1 } - L _ { 1 } )$ can only be between $( L _ { 2 } + 1 )$ to n because by definition these documents cannot be in cache 2. Suppose there are j tagged documents in the first $L _ { 2 }$ documents at cache 2 and i tagged documents from $( L _ { 2 } + 1 )$ to $( R _ { 2 } + i - 1 )$ . Out of these i documents, k are from Cache 1’s $( R _ { 1 } - L _ { 1 } )$ region. The total number of ways in which these documents to tag may be chosen is given by

$$
\begin{array}{c} N _ {1} (i, j) = \sum_ {k = 0} ^ {i} \binom {L _ {2}} {j} \binom {R _ {2} + i - 1 - L _ {2}} {i} \binom {i} {k} \\ \cdot \binom {n - R _ {2} - i} {R _ {1} - i - j} \binom {R _ {1} - i - j} {R _ {1} - L _ {1} - k}. \end{array}\tag{C.1}
$$

The first term refers to the number of ways in which we can choose the j documents to tag in cache 2’s duplication region. The second term selects the i tagged documents between $( L _ { 2 } + 1 )$ and $( R _ { 2 } + i - 1 )$ . Among these i documents, k are selected and marked as belonging to cache ${ 1 \mathrm { { ' } s } }$ nonduplication region (third term). The fourth term selects and tags the remaining $( R _ { 1 } - j - i )$ documents between $( R _ { 2 } + i + 1 )$ and n. Because k documents have already been marked as belonging to the nonduplication region of cache 1, this leaves us with $( R _ { 1 } - L _ { 1 } - k )$ documents yet to be selected for the nonduplication region. These can be selected from the $( R _ { 1 } - j - i )$ tagged documents in $\binom { R _ { 1 } - j - i } { R _ { 1 } - L _ { 1 } - k }$ ways (fifth term). Upon simplification,

$$
N _ {1} (i, j) = \binom{L _ {2}}{j} \binom{R _ {2} + i - 1 - L _ {2}}{i} \binom{n - R _ {2} - i}{R _ {1} - i - j} \binom{R _ {1} - j}{L _ {1} - j}.\tag{Č.2}
$$

Given j tagged documents in cache $2 ^ { \prime } \mathrm { s }$ duplication region, $i \in [ 0 , R _ { 1 } - j ]$ . Thus, the total number of ways in which we can select the j tagged documents is

$$
\begin{array}{c} N (j) = \sum_ {i = 0} ^ {R _ {1} - j} N (i, j) = \sum_ {i = 0} ^ {R _ {1} - j} \binom {L _ {2}} {j} \binom {R _ {2} + i - 1 - L _ {2}} {i} \\ \qquad \qquad \qquad \qquad \qquad \qquad \cdot \binom {n - R _ {2} - i} {R _ {1} - i - j} \binom {R _ {1} - j} {L _ {1} - j} \\ \Rightarrow N (j) = \binom {L _ {2}} {j} \binom {n - L _ {2}} {R _ {1} - j} \binom {R _ {1} - j} {L _ {1} - j}. \end{array}\tag{C.3}
$$

(C.4)

The value of j can itself be anywhere from 0 to min $\phantom { } _ { 1 } ( L _ { 2 } , R _ { 1 } )$ . Thus, the total number of ways in which the documents can be tagged $\mathrm { i s ^ { 1 8 } }$

$$
N = \sum_ {j = 0} ^ {L _ {2}} \binom {L _ {2}} {j} \binom {n - L _ {2}} {R _ {1} - j} \binom {R _ {1} - j} {L _ {1} - j} = \binom {n - L _ {2}} {R _ {1} - L _ {1}} \binom {n + L _ {1} - R _ {1}} {L _ {1}}.
$$

Dividing (C.4) by (C.5):

$$
\begin{array}{c} p (j) = \binom {L _ {2}} {j} \binom {n - L _ {2}} {R _ {1} - j} \binom {R _ {1} - j} {L _ {1} - j} \\ \cdot \binom {n - L _ {2}} {R _ {1} - L _ {1}} ^ {- 1} \binom {n + L _ {1} - R _ {1}} {L _ {1}} ^ {- 1}. \end{array}\tag{C.6}
$$

And dividing (C.2) by (C.5),

$$
\begin{array}{l} p (j, i) = \binom {L _ {2}} {j} \binom {R _ {2} + i - 1 - L _ {2}} {i} \binom {n - R _ {2} - i} {R _ {1} - i - j} \binom {R _ {1} - j} {L _ {1} - j} \\ \cdot \binom {n - L _ {2}} {R _ {1} - L _ {1}} ^ {- 1} \binom {n + L _ {1} - R _ {1}} {L _ {1}} ^ {- 1}. \end{array} \tag {C.7}
$$

We also have

$$
\sum_ {i = 0} ^ {R _ {1} - j} p (i \mid j) \frac {i}{R _ {2} - L _ {2} + i - 1} = \frac {R _ {1} - j}{n - L _ {2}}\tag{C.8}
$$

<sup>18</sup> Because ${ \binom { m } { k } } \ = \ 0$ for $k \ < \ 0$ and $k \ > \ m ,$ , it follows that $\begin{array} { r } { \sum _ { j = 0 } ^ { \operatorname* { m i n } ( L _ { 2 } , R _ { 1 } ) } N ( j ) = \sum _ { j = 0 } ^ { L _ { 2 } } N ( j ) } \end{array}$

and

$$
\sum_ {i = 0} ^ {R _ {1} - j} p (i \mid j) \frac {i}{R _ {2} - L _ {2} + i - 1} = \frac {R _ {1} - j}{n - L _ {2}}.\tag{C.9}
$$

The expected latency at cache 2 is given by

$$
E L = \sum_ {j = 0} ^ {L _ {2}} \left\{p (j) \cdot \sum_ {i = 0} ^ {R _ {1} - j} p (i \mid j) \cdot T 1 \right\},\tag{C.10}
$$

where T 1 is given by Equation (A.11). Here, again, we use $p ( j ) = 0$ for j > min $( \bar { L _ { 2 } } , \bar { R _ { 1 } } )$ and set the upper bound for j as $L _ { 2 } .$ Substituting Equations (C.6) and (C.7) into (A.11) and using results (C.8) and (C.9).

$$
\begin{array}{l} E L = \frac {1}{n - L _ {2}} \bigg (R _ {1} - \frac {L _ {1} L _ {2}}{n + L _ {1} - R _ {1}} \bigg) \frac {n - L _ {2}}{n} \\ \quad \cdot \prod_ {l = n - L _ {2} + 1} ^ {n} \bigg (1 + \frac {\alpha}{l \cdot (1 - \alpha)} \bigg) ^ {- 1} \cdot D \\ \quad + \sum_ {j = 0} ^ {L _ {2}} \sum_ {i = 0} ^ {R _ {1} - j} p (j, i) \frac {n - R _ {2} - R _ {1} + j}{n} \\ \quad \cdot \prod_ {l = n - R _ {2} - i + 1} ^ {n} \bigg (1 + \frac {\alpha}{l \cdot (1 - \alpha)} \bigg) ^ {- 1}. \end{array}\tag{C.11}
$$

Upon simplification,

$$
\begin{array}{l} E L = \frac {1}{n - L _ {2}} \bigg (R _ {1} - \frac {L _ {1} L _ {2}}{n + L _ {1} - R _ {1}} \bigg) \cdot D \cdot w (n, L _ {2}) \\ \qquad + \sum_ {j = 0} ^ {L _ {2}} \sum_ {i = 0} ^ {R _ {1} - j} p (j, i) \frac {n - R _ {2} - R _ {1} + j}{n - R _ {2} - i} w (n, R _ {2} + i). \end{array}\tag{C.12}
$$

Equation (C.12) can be simplified further when n is sufficiently large as described below.

## Approximation

If the ratios $R _ { 1 } / n$ and $R _ { 2 } / n$ are small, we can expand

$$
w (n, R _ {2} + i) \approx 1 - \frac {1}{1 - \alpha} \frac {R _ {2} + i}{n} + \frac {1}{2} \frac {\alpha}{(1 - \alpha) ^ {2}} \left(\frac {R _ {2} + i}{n}\right) ^ {2}.\tag{C.13}
$$

Substituting this into (C.12) and using the following two results

$$
\sum_ {j = 0} ^ {L _ {2}} \sum_ {i = 0} ^ {R _ {1} - j} p (j, i) \frac {n - R _ {1} - R _ {2} + j}{n - R _ {2} - i} = \frac {n - R _ {1}}{n - L _ {2}} \frac {n + L _ {1} - L _ {2} - R _ {1}}{n + L _ {1} - R _ {1}}\tag{C.14}
$$

$$
\sum_ {j = 0} ^ {L _ {2}} \sum_ {i = 0} ^ {R _ {1} - j} p (j, i) \frac {n - R _ {1} - R _ {2} + j}{n - R _ {2} - i} \frac {i}{n} = \frac {R _ {2} - L _ {2}}{n (n - L _ {2})} \left(R _ {1} - \frac {L _ {1} L _ {2}}{n + L _ {1} - R _ {1}}\right),\tag{C.15}
$$

we get

$$
\begin{array}{l} E L = \frac {1}{n - L _ {2}} \bigg (R _ {1} - \frac {L _ {1} L _ {2}}{n + L _ {1} - R _ {1}} \bigg) \cdot D \cdot w (n, L _ {2}) \\ \qquad + \bigg (1 - \frac {1}{n - L _ {2}} \bigg (R _ {1} - \frac {L _ {1} L _ {2}}{n + L _ {1} - R _ {1}} \bigg) \bigg) \\ \qquad \cdot w \bigg (n, R _ {2} + \frac {R _ {1} (n + L _ {1} - R _ {1}) - L _ {1} L _ {2}}{n + L _ {1} - L _ {2} - R _ {1}} \frac {R _ {2} - L _ {2}}{n - R _ {1}} \bigg). \end{array}\tag{C.16}
$$

<sup>Proposition</sup> <sup>3.</sup> The best-response curves, $L _ { 2 } ^ { * } ( L _ { 1 } )$ and $L _ { 1 } ^ { * } ( L _ { 2 } )$ are nonincreasing in $L _ { 1 }$ and $L _ { 2 } ,$ respectively. Further, the existence of an equilibrium is guaranteed.

<sup>Proof</sup> To prove this result, we apply the Binomial theorem to expand $w ( x , y )$ :

$$
w (x, y) = \left(1 - \frac {y}{x}\right) ^ {1 / (1 - \alpha)} = 1 - \frac {1}{(1 - \alpha)} \frac {y}{x} + \frac {\alpha}{2 (1 - \alpha) ^ {2}} \left(\frac {y}{x}\right) ^ {2} + \dots\tag{C.17}
$$

For $x \gg y ,$ we can ignore the cubic and other higher-order terms to get

$$
w (x, y) = \left(1 - \frac {y}{x}\right) ^ {1 / (1 - \alpha)} = 1 - \frac {1}{(1 - \alpha)} \frac {y}{x} + \frac {\alpha}{2 (1 - \alpha) ^ {2}} \left(\frac {y}{x}\right) ^ {2}.\tag{Č.18}
$$

When the number of documents, $n ,$ is much larger than the size of either cache, we can use (C.18) to rewrite (C.16) as follows:

$$
\begin{array}{l} E L _ {2} = \left\{\frac {1}{n - L _ {2}} \left(R _ {1} - \frac {L _ {1} L _ {2}}{n + L _ {1} - R _ {1}}\right) \right. \\ \cdot \left(1 - \frac {1}{(1 - \alpha)} \frac {L _ {2}}{n} + \frac {\alpha}{2 (1 - \alpha) ^ {2}} \left(\frac {L _ {2}}{n}\right) ^ {2}\right) D \Bigg \} \\ + \left(1 - \frac {1}{n - L _ {2}} \left(R _ {1} - \frac {L _ {1} L _ {2}}{n + L _ {1} - R _ {1}}\right)\right) \\ \cdot \left(1 - \frac {1}{(1 - \alpha)} ((R _ {2} + ((R _ {1} (n + L _ {1} - R _ {1}) - L _ {1} L _ {2}) (R _ {2} - L _ {2})) / ((n + L _ {1} - L _ {2} - R _ {1}) (n - R _ {1}))) \cdot (n) ^ {- 1}) + \frac {\alpha}{2 (1 - \alpha) ^ {2}} \cdot (((R _ {2} + ((R _ {1} (n + L _ {1} - R _ {1}) - L _ {1} L _ {2}) (R _ {2} - L _ {2})) / ((n + L _ {1} - L _ {2} - R _ {1}) (n - R _ {1}))) \cdot (n) ^ {- 1}) ^ {2})\right). \end{array} \tag {C.19}
$$

We now apply the conjugate pairs theorem, which states that for the problem min<sub>x</sub> $F ( x , a )$ , the derivative $\partial x ^ { * } / \partial a$ and the cross-partial $F _ { x a }$ have opposite signs. Taking the crosspartial of (C.19) with respect to $L _ { 1 }$ and $L _ { 2 } ,$

$$
\begin{array}{l} \frac {\partial^ {2} E L _ {2}}{\partial L _ {1} \partial L _ {2}} \\ = \frac {(1 - D) (n ^ {8} (1 - \alpha) + n ^ {7} (3 (1 - \alpha) L _ {1} - (5 - 3 \alpha) L _ {2} - 5 (1 - \alpha) R _ {1})) + O (n ^ {6})}{(1 - \alpha) n ^ {2} (n - L _ {2}) ^ {2} (n + L _ {1} - R _ {1}) ^ {2} (n - R _ {1}) (n + L _ {1} - L _ {2} - R _ {1}) ^ {3}} \end{array}\tag{C.20}
$$

where $O ( n ^ { 6 } )$ denotes terms of order $n ^ { 6 }$ or lower. For large n, these terms can be ignored relative to the higher-order terms (i.e., terms of order 7 and 8).

$$
\begin{array}{l} \frac {\partial^ {2} E L _ {2}}{\partial L _ {1} \partial L _ {2}} \\ = \frac {n ^ {7} (1 - D) (n (1 - \alpha) + 3 (1 - \alpha) L _ {1} - (5 - 3 \alpha) L _ {2} - 5 (1 - \alpha) R _ {1})}{(1 - \alpha) n ^ {2} (n - L _ {2}) ^ {2} (n + L _ {1} - R _ {1}) ^ {2} (n - R _ {1}) (n + L _ {1} - L _ {2} - R _ {1}) ^ {3}} \end{array}\tag{C.21}
$$

As long as $\alpha \leq ( 1 - 2 L _ { 2 } / ( n + 3 L _ { 1 } - 3 L _ { 2 } - 5 R _ { 1 } ) )$ 5, the above expression is greater than or equal to zero for all $L _ { 2 }$ $[ 0 , { \bar { R } } _ { 2 } ] .$ . Because $n \gg$ max $( R _ { 1 } , R _ { 2 } )$ , the right-hand side of the constraint on  approaches 1. Because $\alpha < 1$ , we have $\left( \partial ^ { 2 } E L _ { 2 } / \partial L _ { 1 } \partial L _ { 2 } \right) \geq 0 . ^ { 1 9 }$ It follows that $L _ { 2 } ^ { * }$ is weakly decreasing in $L _ { 1 } .$ . In exactly the same manner, we can set up the expression for expected latency at cache 1 and show that $L _ { 1 } ^ { * }$ is weakly decreasing in $L _ { 2 }$

To prove existence of an equilibrium, we compute the second-order derivative of (C.16). As before, assuming that $n \gg \operatorname* { m a x } ( R _ { 1 } , R _ { 2 } )$ and ignoring terms with lower exponents of $n ,$ we get the followed simplified expression:

$$
\frac {\partial^ {2} E L _ {2}}{\partial L _ {2} ^ {2}} = \frac {2 \alpha (1 - D) (R _ {1} - L _ {1}) (n - R _ {1})}{(1 - \alpha) (n - L _ {2}) ^ {3} (n + L _ {1} - R _ {1})} \geq 0.\tag{C.22}
$$

Note that the strategy space is compact and convex for each player $( L _ { 1 } \in [ 0 , R _ { 1 } ] , \stackrel { \_ } { L } _ { 2 } \in [ 0 , R _ { 2 } ] )$ and the objective function to be minimized is continuous and quasi-convex in each player’s own strategy. Thus, it follows that the game has at least one pure-strategy Nash equilibrium (Debreu 1952).

<sup>Proposition</sup> <sup>4.</sup> The best-response curves, $L _ { 2 } ^ { * } ( L _ { 1 } )$ and $L _ { 1 } ^ { * } ( L _ { 2 } )$ are both nondecreasing in intercache latency, D.

<sup>Proof.</sup> To prove the result, we again use the conjugate pairs theorem. Taking the cross-partial of Equation (C.16),

$$
\begin{array}{c} \frac {\partial^ {2} E L}{\partial D \partial L _ {2}} = - \frac {(n - L _ {2}) ^ {\alpha / (1 - \alpha)}}{n ^ {1 / (1 - \alpha)}} \\ \cdot \bigg (\frac {L _ {1}}{n + L _ {1} - R _ {1}} + \frac {\alpha}{1 - \alpha} \\ \cdot \bigg (R _ {1} - \frac {L _ {1} L _ {2}}{n + L _ {1} - R _ {1}} \bigg) (n - L _ {2}) ^ {- 1} \bigg) <   0. \end{array}\tag{C.23}
$$

Thus, it follows that $L _ { 2 } ^ { * } ( L _ { 1 } )$ is nondecreasing in D. In a similar manner, it can be shown that $L _ { 1 } ^ { * } ( L _ { 2 } )$ is nondecreasing in D.

## Appendix D

<sup>Proposition</sup> <sup>5.</sup> With traffic-dependent intercache latency, the optimal size of the duplication region is (a) nondecreasing in the intercache delay D, (b) nondecreasing in request locality  for  below some positive threshold, (c) nondecreasing in cache size $R _ { 2 } . .$ , and (d) nondecreasing in mean service time .

<sup>Proof.</sup> We apply the conjugate pairs theorem to prove the result.

(a) nondecreasing in the intercache delay D: $\partial ^ { 2 } E L _ { 2 } / \partial L _ { 2 } \partial D = 1 ( \tilde { R _ { 1 } ( 1 - L _ { 2 } / n ) ^ { \alpha / 1 - \alpha } } ) / ( n ^ { 2 } ( 1 - \alpha ) ) \leq 0$ . Thus, it follows that $( \partial L _ { 2 } ^ { * } / \partial D ) \geq 0$

(b) nondecreasing in request locality  for low :

$$
\begin{array}{l} \frac {\partial^ {2} E L _ {2}}{\partial L _ {2} \partial \alpha} = \frac {R _ {1}}{n ^ {2}} \frac {1}{(1 - \alpha) ^ {2} \alpha} \left(1 - \frac {L _ {2}}{n}\right) ^ {\alpha / (1 - \alpha)} \\ \qquad \cdot \left(- \alpha \frac {R _ {1}}{n} w (n, L _ {2}) \ln (w (n, L _ {2})) \psi^ {\prime \prime} + \psi^ {\prime} \ln (\psi^ {\prime})\right), \end{array}
$$

where

$$
\begin{array}{c} \psi^ {\prime} = D + \frac {\tau}{(1 - ((1 - \alpha / \beta) n \tau) (R _ {1} / n) w) ^ {2}} \quad \text { and } \\ \psi^ {\prime \prime} = \bigg (\frac {1 - \alpha}{\beta} n \tau \bigg) \frac {2 \tau}{(1 - ((1 - \alpha / \beta) n \tau) (R _ {1} / n) w) ^ {3}}. \end{array}
$$

Note that when $\tau = 0 ,$ , we have $\psi ^ { \prime } = D$ and $\psi ^ { \prime \prime } = 0$ . Thus, the cross-partial is negative and the optimal $L _ { 2 } ^ { * }$ is nondecreasing in . For higher values of $\tau ,$ the sign of the cross partial is determined by the sign of:

$\Gamma _ { 0 } = - \alpha ( R _ { 1 } / n ) ( w \ln w ) \psi ^ { \prime \prime } + \psi ^ { \prime } \ln ( \psi ^ { \prime } )$ . Because $0 < w \leq 1 ,$ we have w ln w $\geq - e ^ { - 1 }$ . Thus,

$\Gamma _ { 0 } \le \Gamma \equiv \alpha ( R _ { 1 } / n ) e ^ { - 1 } \cdot \psi ^ { \prime \prime } + \psi ^ { \prime } \ln ( \psi ^ { \prime } ) = ( 2 \sqrt { \tau } \alpha ( 1 - \alpha ) R _ { 1 } ) /$ $e \beta ( \psi ^ { \prime } - D ) ^ { 3 / 2 } + \psi ^ { \prime } \ln ( \psi ^ { \prime } )$ 0 â 4<sup>0</sup>5is a convex function of <sup>0</sup> in the range $D \leq \psi ^ { \prime } \leq 1$ , and $\Gamma ( \psi ^ { \prime } = D ) < 0 , \ \Gamma ( \psi ^ { \prime } = 1 ) >$ 0. Therefore, there exists a unique threshold for $\psi ^ { \prime } ,$ below which the cross-partial is negative and $L _ { 2 } ^ { * }$ is nondecreasing in . Because $\psi ^ { \prime }$ is increasing in $\tau ,$ it follows that there is a corresponding threshold for  as well.

(c) nondecreasing in cache size $R _ { 2 } \mathrm { : }$

$$
\begin{array}{l} \frac {\partial^ {2} E L _ {2}}{\partial L _ {2} \partial R _ {2}} \\ = - \frac {R _ {1} (n - R _ {1}) (1 - (n R _ {2} - L _ {2} R _ {1} / n (n - R _ {1}))) ^ {1 / 1 - \alpha} / \alpha}{(n ^ {2} - n (R _ {2} + R _ {1}) + L _ {2} R _ {1}) ^ {2} (1 - \alpha) ^ {2}} \leq 0. \end{array}
$$

Thus, it follows that $L _ { \gamma } ^ { * }$ is nondecreasing in $R _ { 2 }$ .

(d) nondecreasing in cache size $R _ { 1 } { : }$ We can rewrite $E L _ { 2 }$ as

$$
E L _ {2} = \psi \left(\frac {R _ {1}}{n} w (n, L _ {2})\right) + \left(1 - \frac {R _ {1}}{n}\right) w \left(n, R _ {2} + R _ {1} \cdot \frac {R _ {2} - L _ {2}}{n - R _ {1}}\right),
$$

where the function  is convexly increasing, that is, $\psi ^ { \prime } > 0$ and $\psi ^ { \prime \prime } > 0$ . Taking the cross-partial:

$$
\begin{array}{c} \frac {\partial^ {2} E L _ {2}}{\partial L _ {2} \partial R _ {1}} = \frac {R _ {1}}{n ^ {2}} \frac {1}{1 - \alpha} \biggl (- \biggl (1 - \frac {L _ {2}}{n} \biggr) ^ {\alpha / (1 - \alpha)} \frac {1}{n} w (n, L _ {2}) \psi^ {\prime \prime} - \frac {\alpha}{1 - \alpha} \\ \qquad \cdot \biggl (1 - \frac {1}{n} \biggl (R _ {2} + R _ {1} \cdot \frac {R _ {2} - L _ {2}}{n - R _ {1}} \biggr) \biggr) ^ {(2 \alpha - 1) / (1 - \alpha)} \\ \qquad \cdot \frac {R _ {2} - L _ {2}}{(n - R _ {1}) ^ {2}} \biggr) <   0. \end{array}
$$

Thus, it follows that L<sup>∗</sup> is nondecreasing in $R _ { 1 } ^ { \phantom { } } .$ (e) nondecreasing in mean service time :

$$
\begin{array}{l} \frac {\partial^ {2} E L}{\partial L _ {2} \partial \tau} \\ = - \frac {\beta^ {2} (1 - L _ {2} / n) ^ {- 1 / 1 - \alpha} R _ {1} (\beta (1 - L _ {2} / n) ^ {- 1 / 1 - \alpha} + R _ {1} \tau (1 - \alpha))}{n (n - L _ {2}) (1 - \alpha) (\beta (1 - L _ {2} / n) ^ {- 1 / 1 - \alpha} - R _ {1} \tau (1 - \alpha)) ^ {3}} \leq 0. \end{array}
$$

It follows that ${ { \partial } L _ { 2 } ^ { * } } / { { \partial } \tau } \geq 0$

## References

Bose, I., H. K. Cheng. 2000. Performance models of a firm’s proxy cache server. Decision Support Systems 29(1) 47–57.

Chan, Y. M., J. Womer, J. K. MacKie-Mason, S. Jamin. 1999. One size doesn’t fit all: Improving network QoS through preference driven Web caching. Proc. 27th Annual Telecomm. Policy Res. Conf. Alexandria, VA

Che, H., Y. Tung, Z. Wang. 2002. Hierarchical Web caching systems: Modeling, design and experimental results. IEEE J. Selected Areas Comm. 20(7) 1305–1314.

Chiang, I. R., P. Goes, Z. Zhang. 2007 Periodic cache replacement policy for dynamic content at application server. Decision Support Systems 43(2) 336–348.

Chuang, J., M. Sirbu. 2000. Distributed network storage with quality-of-service guarantees. J. Network Comput. Appl. 23(3) 163–185.

Datta, A., K. Datta, H. Thomas, D. VanderMeer. 2003. WORLD WIDE WAIT: A study of Internet scalability and cache-based approaches to alleviate it. Management Sci. 49(10) 1425–1444.

Debreu, D. 1952. A social equilibrium existence theorem. Proc. National Acad. Sci. 38 886–893.

Dogan, K., C. Kaya, V. Mookerjee. 2003 An economic and operational analysis of the market for content distribution services. Proc. Internat. Conf. Inform. Systems, Association of Information Systems, Seattle, WA, 14–17.

Du, A., X. Geng, R. Gopal, R. Ramesh, A. B. Whinston. 2008. Capacity provision networks: Foundations of markets for sharable resources in distributed computational economies. Inform. Systems Res. 19(2) 144–160.

Dutta, K., S. Soni, S. Narasimhan, A. Datta. 2006. Optimization in object caching. INFORMS J. Comput. 18(2) 243–254.

Fan, L., P. Cao, J. Almeida, A. Z. Broder. 2000. Summary cache: A scalable wide-area Web cache sharing protocol. IEEE/ACM Trans. Networking 8(3) 281–293.

Fang, X., O. Sheng, W. Gao, B. Iyer. 2006. A data-mining-based prefetching approach to caching for network storage systems. INFORMS J. Comput. 18(2) 267–282.

Geng, X., R. D. Gopal, R. Ramesh, A. B. Whinston. 2003. Scaling Web services with capacity provision networks. IEEE Comput. 36(11) 64–73.

Gualtieri, M., J. Staten. 2009. Best practices: Attaining and maintaining blazing fast Web site performance. Forrester Industry Report, Cambridge, MA.

Hosanagar, K., Y. Tan. 2004. Optimal duplication in cooperative web caching. Proc. Fourteenth Annual Workshop Inform. Technologies and Systems (WITS), Washington, DC, 92–97.

Hosanagar, K., J. Chuang, R. Krishnan, M. Smith. 2008. Service adoption and pricing of content delivery network (CDN) services. Management Sci. 54(9) 1579–1593.

Hosanagar, K., R. Krishnan, J. Chuang, V. Choudhary. 2005. Pricing and resource allocation in caching networks with multiple levels of QoS. Management Sci. 51(12) 1844–1899.

Kaya, C., G. Zhang, Y. Tan, V. Mookerjee. 2009. An admissioncontrol technique for delay reduction in proxy caching. Decision Support Systems 46(2) 594–603.

Kelly, T., S. Jamin, J. K. MacKie-Mason. 1999. Variable QoS from shared Web caches: User-centered design and value-sensitive

replacement. MIT Workshop on Internet Service Quality Economics, Cambridge, MA.

Kumar, C. 2009. Performance evaluation for implementations of a network of proxy caches. Decision Support Systems 46(2) 492–500.

Kumar, C., J. Norris. 2008. A new approach for a proxy-level Web caching mechanism. Decision Support Systems 46(1) 52–60.

Mookerjee, V., Y. Tan. 2002. Analysis of a least recently used cache management policy for Web browsers. Oper. Res. 50(2) 345–357.

Northrup, A. 1998. NT Network Plumbing. IDG Books, 515.

Rousskov, A., D. Wessels. 1998. Cache digest. Proc. 3rd Internat. WWW Caching Workshop, Hungry Minds, Inc., San Diego.

Tan, Y., V. S. Mookerjee, Y. Ji. 2006. Analyzing documentduplication effects on policies for browser and proxy caching. INFORMS J. Comput. 18(4) 506–522.

Tawarmalani, M., K. Kannan, P. De, C. Kumar. 2009. Allocating objects in a network of caches: Social welfare and incentive compatibility. Management Sci. 55(1) 132–147.

Tewari, R., M. Dahlin, H. M. Vin, J. S. Kay. 1999. Design considerations for distributed caching on the Internet. Proc. 19th IEEE Internat. Conf. Distributed Comput. Systems, Austin, TX, 273–284.

Valloppillil, V., K. W. Ross. 1998. Cache array routing protocol v1.0. Internet draft, February 1998, http://www.globecom.net/ ietf/draft/draft-vinod-carp-v1-03.html.

Wessels, D., K. Claffy. 1998. ICP and the squid Web cache. IEEE J. Selected Areas Comm. 16(3) 345–357. http://ircache.nlanr.net/ ∼wessels/Papers/icp-squid.

Wu, K., P. S. Yu. 1999a. Local replication for proxy Web caches with hash routing. Proc. 8th Internat. Conf. Inform. Knowledge Management (CIKM), Kansas City, MO.

Wu, K., P. S Yu. 1999b. Load balancing and hot spot relief for hash routing among a collection of proxy caches. Proc. 19th IEEE Internat. Conf. Distributed Comput. Systems, Austin, TX, 536–543.

Zu, M., J. Subhlok. 2003. Home based cooperative Web caching. 7th Multi-Conf. Systemics, Cybernetics and Informatics, Orlando, FL. http://www2.cs.uh.edu/<sup>\~</sup>jsteach/HPSL/projects/dance.html.
