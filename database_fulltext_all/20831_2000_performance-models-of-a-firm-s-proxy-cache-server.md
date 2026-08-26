---
otero_id: 20831
otero_key: "2ADZ3F8C"
title: "Performance models of a firm's proxy cache server"
authors: "Indranil Bose; Hsing Kenneth Cheng"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00062-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Performance models of a firm’s proxy cache server

Indranil Bose <sup>1</sup>, Hsing Kenneth Cheng )

Department of Decision and Information Sciences, Warrington College of Business Administration, P.O. Box 117169 The UniÕersity of Florida, GainesÕille, FL 32611-7169, USA

Accepted 14 February 2000

## Abstract

We examine the impact of installing a proxy cache server PCS on overall response time to Web requests. We analyzeŽ . how various factors affect the performance of that server. Our research specifically identifies a ‘‘crossover probability’’, the minimum cache ‘‘hit rate’’ probability at which installing a PCS becomes beneficial. We find that this probability decreases as the arrival rate of Web requests or the average file size increases. In particular, the benefits of installing a PCS are more pronounced when the firm’s users exhibit heavy Web accesses. We also find a ‘‘diminishing rate of return’’ phenomenon in terms of enhancing the PCS’s performance. The managerial implication is that it may not pay to choose an overpowerful PCS as the marginal reduction in the overall response time becomes unjustified. Moreover, the ‘‘bottleneck’’ effect of the firm’s network bandwidth is investigated and demonstrated. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Electronic commerce; Proxy cache server; World Wide Web

## 1. Introduction

The last several years have witnessed an explosive growth of the Internet. The number of people around the world connected to the Internet grew from 40 million in 1996 to 100 million in 1997. The number of Internet domain names increased from 627,000 in 1996 to 1.5 million in 1997, and traffic on the Internet doubled every 100 days 11 . The<sup>w</sup> <sup>x</sup> explosive use of the Internet and the World Wide Web has caused congested networks and overloaded servers. As a result, the average waiting time for Web page delivery is estimated to be as high as 15 to 45 s 7 . Adding more network bandwidth is consid-<sup>w</sup> <sup>x</sup> ered an expensive and ineffective solution to the problem of long delays of Web page delivery.

It is commonly held that the majority of World Wide Web accesses are redundant. An ‘‘80–20’’ rule best describes such a phenomenon, with 80% of requested Web pages coming from 20% of the extant Web sites. Corporate users exhibit more redundant patterns since people doing similar tasks tend to access similar Web resources. ‘‘Caching,’’ i.e., storing, these frequently accessed Web pages closer to the requesting users can greatly speed up Web page delivery and impose less cost in bandwidth.

In general, caching can be implemented at 1Ž . individual browser software, 2 the originating WebŽ . sites the sites delivering the requested pages , 3Ž . Ž .

the Internet Service Providers ISP , and 4 theŽ . Ž . boundary between a local area network LAN andŽ . the Internet. Browser caches are inefficient since they cache for only one user. The caching at the ‘‘point of origin’’ Web sites can improve performance markedly for the originating Web servers by off-loading requests from the outside world, although the requested files are still subject to delivery through the Internet. ISPs such as America Online, cache numerous Web pages to satisfy their members’ requests more efficiently. For example, instead of fetching the same weather pages from the Weather Channel at each member’s request, these pages are cached at the ISP’s server and delivered directly to the members.

It has been suggested that, given the current state of technology, the greatest improvement in response time for corporations will come from installing a proxy cache server PCS at the boundary between Ž . the corporate LAN and the Internet 5 . The primary<sup>w</sup> <sup>x</sup> benefits include lower bandwidth requirements and faster response times. Corporations can accommodate more users with a given Internet connection capacity since the PCS can satisfy redundant requests from different users. Delivering duplicate requests directly from the PCS at LAN speed also improves the response time. This type of server is the primary focus of our paper.

Caching plays a vital role in improving response time to Web requests. Thus, it has become an increasingly important research area. Prior research has focused on analyzing or developing various cache replacement algorithms 1,3,9,14,15,17 , among oth-<sup>w</sup> <sup>x</sup> ers. For example, Ref. 15 discusses a caching algo- <sup>w</sup> <sup>x</sup> rithm for cache replacement and maintenance of consistency for cached documents, while Ref. 1<sup>w</sup> <sup>x</sup> shows that the cache replacement problem is similar to a knapsack problem and suggests a greedy heuristic for solving the problem.

Our research looks at a more fundamental problem: notably, the impact of installing a PCS on overall response time to Web requests. In particular, we study the conditions under which installing a PCS becomes beneficial. We also analyze how various factors affect the performance of a firm’s PCS. These factors include the arrival rates of requests, the probability of desired content already residing on the PCS the cache ‘‘hit rate’’ probability , the average Ž .

file sizes of Web requests, the speed of the PCS, and the firm’s network bandwidth.

Our model focuses on the performance impact of installing a PCS on the overall response time to users’ requests. We do not intend to analyze the pros and cons of various cache replacement algorithms, nor are we concerned with the freshness of the cached content issue. To minimize these concerns, a common practice is for the PCS to have a reasonably large storage and to refresh the cached content during off-peak hours e.g., nights . Ž .

We specifically identify a ‘‘crossover probability’’, the minimum cache ‘‘hit rate’’ probability at which it is beneficial to install a PCS. We find that this probability decreases as the arrival rate of Web requests or the average file size increases. In particular, the benefits of installing a PCS are more pronounced when the firm’s users exhibit heavy Web accesses. We also find a ‘‘diminishing rate of return’ phenomenon in terms of enhancing the PCS’s performance, so that it may not pay to choose an overpowerful PCS, as the marginal gain in reducing the overall response time becomes unjustified. Moreover, we investigate and demonstrate the ‘‘bottleneck’’ effect of the firm’s network.

This paper is structured as follows. In Section 2, we propose a queuing network model to study the dynamics of installing a firm’s PCS. Overall response time formulas are developed for both the case with and without a PCS. Several insights from the model are offered in this section. Section 3 reports numerical experiments conducted to examine the response time behavior of the firm’s PCS with respect to various parameters of the model. Section 4 provides concluding remarks and potential extensions of this research.

## 2. The model

Consider the case where members of a firm need to access the World Wide Web to accomplish their tasks. In doing so, they are likely to repeatedly frequent the same Web sites. For example, the purchasing personnel may look up the same pricing catalogues of a few major suppliers’ Web sites. Retrieving the same content repeatedly in this case clogs up both the firm’s and the suppliers’ useful bandwidth resources, and causes an unnecessary increase of workload for the suppliers’ Web servers. A popular practice to improve the response time is to install a PCS that stores repeatedly retrieved files.

With a PCS, a user’s Web requests will first be routed to the firm’s PCS. If the requested files are already stored in the PCS, the requested Web pages or files will be directly delivered to the user from the PCS. When the requested files cannot be found in the PCS, it initiates the process of fetching the desired files from the remote Web site. These new files will be stored in the firm’s PCS, while a copy will be sent to the requesting user.

The benefits of a PCS depend on several factors. The most prominent of these factors are the likelihood of desired files already stored in the PCS theŽ ‘‘hit rate’’ , the speed of the PCS, the bandwidth of . the firm’s Internet connection, the speed of the remote Web server, and the remote Web site’s network bandwidth.

To discern the effect of the aforementioned factors on the PCS’s performance, we use a network of queues to model the dynamics of how the users’ requests are handled in the presence of a PCS over the World Wide Web. As seen in Fig. 1, requests for Web pages or files arrive at the PCS at a Poisson rate of per unit of time. Let F denote the average size of requested files. The probability that the PCS can fulfill a request is $p .$ . Thus, $p$ is the probability that desired files already reside on the PCS. With probability $( 1 - p )$ , the PCS needs to fetch the requested files from the remote Web site.

![](/api/attachments/2ADZ3F8C/fulltext/images/05f4d73f662a65c877623ef887c67fc46fdd3ccd632c5013ec5171a8c4348ce7.jpg)  
Fig. 1. The performance model of a PCS.

We define $\lambda _ { 1 }$ and $\lambda _ { 2 }$ such that:

$$
\lambda = \lambda_ {1} + \lambda_ {2}, \text {   where   } \lambda_ {1} = p \lambda \text {   and   } \lambda_ {2} = (1 - p) \lambda .\tag{1}
$$

The $\lambda _ { 1 }$ traffic, depicted by a solid line in Fig. 1, delivers the readily available content from the PCS to the requesting user. The dashed line in Fig. 1 represents the $\lambda _ { 2 }$ traffic that fetches the desired files from the remote Web server and returns to the PCS. The $\lambda _ { 2 }$ traffic first goes through a one-time initialization. This initialization captures the time of all the required handshakings to establish a Transmission Control Protocol TCP connection between theŽ . firm’s PCS and the remote Web site. We use the parameter $I _ { \mathrm { s } }$ to characterize this one-time initialization. The remote Web server then retrieves the requested files and delivers them to the firm’s PCS. A copy of the files is, in turn, downloaded to the requesting user.

The remote Web server performance is characterized by 1 the size of its output buffer in bytes ,Ž . Ž . $B _ { \mathrm { s } } ,$ Ž . Ž .2 the static server time in seconds , $Y _ { \mathrm { s } } ,$ Ž .and 3 the dynamic server rate in bytes per second ,Ž . $R _ { \mathrm { s } }$ . The second parameter of the remote Web server, $Y _ { \mathrm { s } } ,$ models the fixed overhead irrespective of the size of the requested files. The dynamic server rate, $R _ { \mathrm { s } }$ , is closely related to the conventional measures of a server’s power, e.g., millions of instructions per second MIPS . In Section 3, numerical experimentsŽ . are conducted using realistic parameter values reported in Ref. 12 . Likewise, the firm’s PCS is <sup>w</sup> <sup>x</sup> characterized by $B _ { \mathrm { x c } } , ~ Y _ { \mathrm { x c } }$ , and $R _ { \mathrm { x c } }$ where the subscript ‘‘xc’’ stands for ‘‘proxy cache.’’ After one output buffer’s worth of data is retrieved from the remote Web server, it is delivered to the PCS through the Web server’s Internet connection. The latter is termed the server network bandwidth in Fig. 1.

It is not unusual for the size of the requested file, $F ,$ to exceed the remote Web server’s output buffer size, $B _ { \mathrm { s } } .$ . In this case, it may take several loops of retrieving and delivering smaller files to complete the PCS’s request. This looping phenomenon is inherent in the Hyper Text Transfer Protocol HTTPŽ .

where retrieval of the home page is followed by retrieval of embedded inline images. To model this looping, let $q$ be the branching probability that a request from the PCS can be fulfilled at the first try; or $q = \operatorname* { m i n } \{ 1 , ( B _ { \mathrm { s } } / F ) \}$ . Consequently, a $( 1 - q )$ proportion of the requests will loop back to the remote Web server for further processing. In equilibrium, the traffic coming out of the remote Web server toward the PCS after branching should equal the original incoming traffic, $\lambda _ { 2 }$ . Hence, $q \lambda _ { 2 } ^ { \prime }$ equals $\lambda _ { 2 }$ in Fig. 1 where ${ \boldsymbol { \lambda } } _ { 2 } ^ { \prime }$ is the traffic leaving server network bandwidth before branching. Section 5 lists the notation used in the model.

The queuing network of Fig. 1 is assumed to be a Jackson network. In essence, such a network behaves as $i f$ all nodes are independent $\mathbf { M } / \mathbf { M } / 1$ queues 8 . <sup>w</sup> <sup>x</sup> It then follows that the overall response time for completing users’ requests in the presence of a PCS is given by Eq. 2:

$$
T _ {\mathrm{xc}} = \frac {1}{\frac {1}{I _ {\mathrm{xc}}} - \lambda} + p \left\{\frac {1}{\frac {1}{\frac {F}{B _ {\mathrm{xc}}} \left[ Y _ {\mathrm{xc}} + \frac {B _ {\mathrm{xc}}}{R _ {\mathrm{xc}}} \right]} - \lambda_ {1}} + \frac {F}{N _ {\mathrm{c}}} \right\}
$$

$$
+ (1 - p) \left\{\frac {1}{\frac {1}{I _ {\mathrm{s}}} - \lambda_ {2}} + \frac {1}{\frac {1}{\frac {F}{B _ {\mathrm{s}}} \left[ Y _ {\mathrm{s}} + \frac {B _ {\mathrm{s}}}{R _ {\mathrm{s}}} \right]} - \lambda_ {2} / q} \right.
$$

$$
\left. + \frac {F}{N _ {\mathrm{s}}} + \frac {1}{\frac {1}{\frac {F}{B _ {\mathrm{xc}}} \left[ Y _ {\mathrm{xc}} + \frac {B _ {\mathrm{xc}}}{R _ {\mathrm{xc}}} \right]} - \lambda_ {2}} + \frac {F}{N _ {\mathrm{c}}} \right\}.\tag{2}
$$

The first term in Eq. 2 is the expected look-up time required to see if the desired files are available from the PCS. With probability $p ,$ the content is already stored. The second term in Eq. 2 describes the expected time for the content to be delivered to the requesting user. The third term in Eq. 2 identifies the expected time required from the time the PCS initiates the fetching of desired files and the remote Web server transfers the files to the PCS, to the time the PCS delivers a copy to the requesting user. From Fig. 1 and Eq. 2, the arrival rate to the remote Web server is ${ \boldsymbol { \lambda } } _ { 2 } ^ { \prime }$ , which equals $\lambda _ { 2 } / q$ , due to the looping nature of processing at the remote Web server.

Without a PCS, our model reduces to a special case reported in Ref. 16 where the overall response<sup>w</sup> <sup>x</sup> time is described by Eq. 3:

$$
T = \frac {1}{\frac {1}{I _ {\mathrm{s}}} - \lambda} + \frac {1}{\frac {1}{\frac {F}{B _ {\mathrm{s}}} \left[ Y _ {\mathrm{s}} + \frac {B _ {\mathrm{s}}}{R _ {\mathrm{s}}} \right]} - \lambda / q} + \frac {F}{N _ {\mathrm{s}}} + \frac {F}{N _ {\mathrm{c}}}.\tag{3}
$$

A quick inspection of Eqs. 2 and 3 shows that both contain the term $F / N _ { \mathrm { c } }$ . This implies that the client network bandwidth should not affect the decision of whether to install the PCS to improve the overall response time. The client network bandwidth is irrelevant in deciding whether to install the PCS, since improving the client network bandwidth enhances the performance equally with or without it.

The upper limits on the arrival rates of users requests, $\lambda _ { \operatorname* { m a x } }$ , and the average file sizes, $F _ { \mathrm { m a x } }$ , can be derived by prohibiting negative terms in Eq. 2 as follows:

$$
\begin{array}{r l} \lambda_ {\max} = & \min \left\{\frac {1}{I _ {\mathrm{s}}}, \frac {1}{I _ {\mathrm{xc}}}, \frac {q B _ {\mathrm{s}} R _ {\mathrm{s}}}{F (R _ {\mathrm{s}} Y _ {\mathrm{s}} + R _ {\mathrm{s}})}, \right. \\ & \left. \frac {q B _ {\mathrm{xc}} R _ {\mathrm{xc}}}{F (R _ {\mathrm{xc}} Y _ {\mathrm{xc}} + R _ {\mathrm{xc}})} \right\} \end{array}\tag{4}
$$

and

$$
\begin{array}{c} F _ {\max} = \min \left\{\frac {q B _ {\mathrm{s}} R _ {\mathrm{s}}}{\lambda \left(R _ {\mathrm{s}} Y _ {\mathrm{s}} + R _ {\mathrm{s}}\right)}, \right. \\ \left. \frac {q B _ {\mathrm{xc}} R _ {\mathrm{xc}}}{\lambda \left(R _ {\mathrm{xc}} Y _ {\mathrm{xc}} + R _ {\mathrm{xc}}\right)} \right\}. \end{array}\tag{5}
$$

The implication of Eqs. 4 and 5 is that when arrival rates or file sizes exceed the limits, the result will be an intolerably long response time for the users.

## 3. Numerical explorations

Several numerical experiments are undertaken to examine the performance behavior of the PCS with respect to various parameter values. Parameter values of our numerical experiments are summarized in Table 1. These experiments seek to determine the conditions making a PCS beneficial. Our results provide guidelines to network managers on when to incorporate proxy caches for Web servers.

The arrival rate of users’ request, , is varied from 10 to 90 requests $/ \mathrm { s } .$ . Some literature, e.g., Ref. <sup>w</sup> <sup>x</sup> 13 , experimented with only up to 10 requests<sup>r</sup>s, while we consider a broader range of the arrival rates as long as they fall within the range specified in Eq. 4. The average size of requested files, $F ,$ varies widely from one Web site to another. Slothouber 16 <sup>w</sup> <sup>x</sup> visited 1000 Web pages at random using the ‘‘random link’’ feature from several search engines and found the average file size to be 5275 bytes. Hence, we experiment with values of F below and above 5275 bytes, varying from 1250 to 8750 bytes. This range of values is consistent with Ref. 2 where 94%<sup>w</sup> <sup>x</sup> of the requested files was reported as less than 50 kbytes.

The size of the Web server’s output buffer, $B _ { \mathrm { s } } .$ equals 2000 bytes as in Ref. 16 . The one-time<sup>w</sup> <sup>x</sup> initialization time of the remote Web server, $I _ { \mathrm { s } } ,$ equals 0.004 s. The static server time of the remote Web server, $Y _ { \mathrm { s } } ,$ is 0.000016 s and the dynamic server rate, $R _ { \mathrm { s } }$ , is set at 1.25 Mbytes<sup>r</sup>s. These values are chosen to conform to the performance characteristics of Web servers in Ref. 12 .<sup>w</sup> <sup>x</sup>

Table 1  
Parameter values in numerical experiments

<table><tr><td>Parameter</td><td>Experimented value</td></tr><tr><td> $\lambda$ </td><td>10–90 requests/s</td></tr><tr><td> $F$ </td><td>1250–8750 bytes</td></tr><tr><td> $B_{s}$ </td><td>2000 bytes</td></tr><tr><td> $I_{s}$ </td><td>0.004 s</td></tr><tr><td> $Y_{s}$ </td><td>0.000016 s</td></tr><tr><td> $R_{s}$ </td><td>1.25 Mbytes/s</td></tr><tr><td> $\alpha = B_{xc}/B_{s}$ </td><td>0.1–1.0</td></tr><tr><td> $\beta = R_{xc}/R_{s} = Y_{xc}/Y_{s}$ </td><td>0.1–1.0</td></tr><tr><td> $\gamma = I_{xc}/I_{s}$ </td><td>0.1–1.0</td></tr><tr><td> $p$ </td><td>0.1–0.9</td></tr></table>

Table 2  
Available choices of network bandwidth $N _ { \mathrm { c } }$ and $N _ { \mathrm { s } }$

<table><tr><td>Type of connection</td><td>Bandwidth (kbps)</td></tr><tr><td>ISDN 1</td><td>64</td></tr><tr><td>ISDN 2</td><td>128</td></tr><tr><td>T1</td><td>1,544</td></tr><tr><td>T3</td><td>45,000</td></tr><tr><td>Ethernet</td><td>10,000</td></tr><tr><td>Fast Ethernet</td><td>100,000</td></tr><tr><td>OC-3</td><td>154,400</td></tr><tr><td>OC-12</td><td>622,000</td></tr></table>

In order to discern the effect of the PCS’s speed, we specifically make its parameter values dependent on those of the remote Web server as follows. We let $\alpha = B _ { \mathrm { x c } } / B _ { \mathrm { s } } , \beta = R _ { \mathrm { x c } } / R _ { \mathrm { s } } = Y _ { \mathrm { x c } } / Y _ { \mathrm { s } }$ , and $\gamma = I _ { \mathrm { x c } } / I _ { \mathrm { s } }$ In the first experiments, , , are set to 1.0, which implies that the remote Web server and the PCS have identical performance characteristics. In the last set of experiments, we vary , ,  separately from 0.1 to 1.0 to investigate the effect of the PCS’s speed on the overall response time to users Web requests. The probability that requested files are readily available from the PCS is varied from 0.1 to 0.9. The empirical statistics of $p$ ranges from 21.3– 56.6% in Ref. 4 to 30–60% in Ref. 10 . The<sup>w x</sup> <sup>w</sup> <sup>x</sup> available choices of values for the client network bandwidth, $N _ { \mathrm { c } }$ , and the server network bandwidth, $N _ { \mathrm { s } }$ , are from Ref. 12 see Table 2 .<sup>w</sup> <sup>x</sup> Ž .

In our experiments, we tacitly assume that the client-side network is slower than the server-side network and set the network bandwidth parameters at $N _ { \mathrm { c } } = 1 2 8$ kbps and $N _ { \mathrm { s } } = 1 5 4 4$ kbps.

## 3.1. Effect of the cache ‘‘hit rate’’ probability, p

Several numerical experiments are conducted to examine the effect of the cache ‘‘hit rate’’ probability on overall response time, where the arrival rate is set to 20 requests $/ \mathrm { { s } }$ and F set to 5000 bytes. The probability $p$ is varied from 0.0 to 1.0 in increments of 0.1. The overall response time without a cache server is independent of $p ,$ as observed from Eq. 3. Hence, $T = 0 . 3 4 7 8 \mathrm { ~ s ~ }$ for all values of $p .$ The overall response time with a PCS, $T _ { \mathrm { x c } }$ , decreases as $p$ increases, as seen in Fig. 2.

![](/api/attachments/2ADZ3F8C/fulltext/images/063adfedfa89ea22398030656c69b4a4f9a650686f22f9043abab23b80900d44.jpg)  
Fig. 2. Overall response time with respect to cache ‘‘hit rate’’ probability Ž . <sup>s</sup>20 requests<sup>r</sup>s and F <sup>s</sup>5000 bytes .

There is a crossover between the graphs representing T and $T _ { \mathrm { x c } }$ . This crossover point gives us the corresponding ‘‘crossover probability’’ defined as $p ^ { * }$ . This crossover probability is significant in deciding whether to install a PCS. For any cache hit rate greater than this crossover probability, $p > p ^ { * }$ , the benefits are realized from installing a PCS since the overall response time to users’ Web requests will be reduced.

## 3.2. Effect of the arriÕal rate,

The effect of a heavy arrival of Web requests on the overall response time is shown in Fig. 3, where the arrival rate is increased to 90 requests<sup>r</sup>s with all other parameters held fixed.

![](/api/attachments/2ADZ3F8C/fulltext/images/d96bee422c8e4a5f6e5b6bf697475437a8f7a5dfa01aef230a572c7094ee9282.jpg)  
Fig. 3. Overall response time in case of heavy arrival $( \lambda = 9 0$ requests<sup>r</sup>s and F <sup>s</sup>5000 bytes ..

Fig. 3 shows that for higher arrival rates, the response times suffer for both the cases, with and without a PCS. The ‘‘crossover probability,’’ $p ^ { * }$ however, decreases as the arrival rate, , increases. Figs. 2 and 3 show that $\boldsymbol { p } ^ { * } = 0 . 2 3 8$ when the arrival rate is 20 requests $/ \mathrm { s } ,$ and $\boldsymbol { p } ^ { * }$ is reduced to 0.030 when the arrival rate is increased to 90 requests<sup>r</sup>s. A PCS is more beneficial in the case of heavy traffic.

To reveal the relationship between the ‘‘crossover probability,’’ $\boldsymbol { p } ^ { * }$ , and the arrival rate, we vary the rates from 10 to 90 requests $/ \mathrm { { s } }$ in increments of 10 requests $/ \mathrm { s } ,$ and plot the corresponding crossover probability in Fig. 4. As expected, the crossover probability decreases as the arrival rate increases. Fig. 4 shows that crossover probability is a strictly decreasing and a strictly concave function of the arrival rate. This implies that the benefits of installing a PCS are more pronounced for heavier Web usage.

## 3.3. Effect of the aÕerage size of requested files, F

In Fig. 5, we plot the overall response times, $T _ { \mathrm { x c } }$ and T, with respect to the cache ‘‘hit rate’’ probability when the average file size is large. The arrival rate is 20 requests $/ \mathrm { { s } }$ and the average requested file size equals 8750 bytes. The crossover probability, $p ^ { * }$ , is found at 0.148, implying that the overall response time with a PCS will be smaller when the probability that the requested files are stored in the PCS exceeds 0.148.

![](/api/attachments/2ADZ3F8C/fulltext/images/4cbb256a696508bcf9ec5997416a65083a092a02dd574948fa6f0d8cc492dbf4.jpg)  
Fig. 4. The effect of arrival rate on crossover probability $p ^ { * }$ Ž . F <sup>s</sup>5000 bytes .

![](/api/attachments/2ADZ3F8C/fulltext/images/5bc829cb0bd71ef02b8f893ce0a1d17b339224704e5cba42ebe8b43d60a7c791.jpg)  
Fig. 5. Overall response time when average file size is large Ž . <sup>s</sup>20 requests<sup>r</sup>s and F <sup>s</sup>8750 bytes .

Fig. 6 shows the effect of the average file size on the crossover probability where the arrival rate is held the same at 20 requests<sup>r</sup>s. The crossover probability in Fig. 6 decreases as the average file size increases, indicating that the advantage of having a proxy cache is more evident when the file size is larger. This result is rather intuitive since the reduction of response time is more significant for larger files with a PCS. Therefore, a smaller crossover probability is needed to realize the benefit of installing one.

![](/api/attachments/2ADZ3F8C/fulltext/images/d255c691c563b429105f8d3a97ffcc7466e164ccadf814f0881f9d9325168ca2.jpg)  
Fig. 6. The effect of file size on the crossover probability $p ^ { * }$ Ž . <sup>s</sup> 20 requests<sup>r</sup>s .

![](/api/attachments/2ADZ3F8C/fulltext/images/e34a27d0d340b4d6768225876d89b73afa336cab9e1640633f6c13d01a8fbee6.jpg)  
Fig. 7. Effect of proxy cache server’s buffer size on overall response time Ž . <sup>s</sup>20 requests<sup>r</sup>s and F <sup>s</sup>5000 bytes .

The curve in Fig. 6 is convex and then becomes slightly concave for file size larger than 6800 bytes. The reduction of the crossover probability is more prominent in the region of 1250–3750 bytes in Fig. 6. When the average file size exceeds 3750 bytes, the ‘‘marginal’’ reduction in the crossover probability plateaus. Fig. 6 exhibits an inflection point when file size is around 6800 bytes.

## 3.4. Effect of the serÕer parameters

In the previous experiments, we tacitly assume the PCS to be identical to the remote Web server, and let $B _ { \mathrm { x c } } = B _ { \mathrm { s } } , R _ { \mathrm { x c } } = R _ { \mathrm { s } } , Y _ { \mathrm { x c } } = Y _ { \mathrm { s } }$ , and $I _ { \mathrm { x c } } = I _ { \mathrm { s } }$ Identical servers are assumed to isolate and study the effect of the arrival rate of requests, the average file size, and the cache ‘‘hit rate’’ probability on the overall response time in the presence and absence of a PCS. It is not necessarily true, however, that the PCS is identical to the remote Web server. In this section, we study the effect of the PCS’s parameters on the overall response time behavior. We assume that $\alpha = B _ { \mathrm { x c } } / B _ { \mathrm { s } } , \beta = R _ { \mathrm { x c } } / R _ { \mathrm { s } } = Y _ { \mathrm { x c } } / Y _ { \mathrm { s } }$ , and $\gamma =$ $I _ { \mathrm { x c } } / I _ { \mathrm { s } }$ . In Fig. 7, we show the behavior of $T _ { \mathrm { x c } }$ with respect to $\alpha$ , the output buffer size ratio between the PCS and the remote Web server, while keeping $\beta = \gamma = 1$ . The arrival rate is fixed at <sup>s</sup>20 requests<sup>r</sup>s and the file size is kept at $F = 5 0 0 0$ bytes. As we increase this output buffer ratio, the average response time decreases. Ceteris paribus, increasing the output buffer size of the PCS reduces the delivery time of requested files.

![](/api/attachments/2ADZ3F8C/fulltext/images/f9a1b2df1d033678d014a3a4eeacb13379c15edfb630abdc90baf3e900fca8bf.jpg)  
Fig. 8. Effect of proxy cache server’s speed on overall response time Ž . <sup>s</sup>20 requests<sup>r</sup>s and F <sup>s</sup>5000 bytes .

Table 3  
The bottleneck effect of $N _ { \mathrm { c } }$ on $T _ { \mathrm { x c } }$ in Eq. 6

<table><tr><td> $N_c$ </td><td>Term 1</td><td>Term 2</td><td>Term 3</td><td>Term 4</td><td>Term 5</td><td>Term 6</td><td>Term 7</td><td> $T_{xc}$ </td></tr><tr><td>64 kbps</td><td>0.0043</td><td>0.0021</td><td>0.6250</td><td>0.0021</td><td>0.0022</td><td>0.0130</td><td>0.0021</td><td>0.6500</td></tr><tr><td>128 kbps</td><td>0.0043</td><td>0.0021</td><td>0.3125</td><td>0.0021</td><td>0.0022</td><td>0.0130</td><td>0.0021</td><td>0.3383</td></tr><tr><td>1.544 Mbps</td><td>0.0043</td><td>0.0021</td><td>0.0259</td><td>0.0021</td><td>0.0022</td><td>0.0130</td><td>0.0021</td><td>0.0517</td></tr></table>

In Fig. 8, we plot the behavior of $T _ { \mathrm { x c } }$ with respect to, $\beta ,$ the speed ratio between the PCS and the remote Web server, keeping $\alpha = \gamma = 1$ . As in Fig. 7, the arrival rate and the average file size remain the same. We observe the same pattern of behavior as in Fig. 7. As the speed of the PCS increases, the service time decreases. This leads to a reduction in the overall response time.

The ‘‘marginal’’ decrease in the overall response time in the region of $\alpha > 0 . 5$ and $\beta > 0 . 5$ becomes minimal in Figs. 7 and 8, respectively, exhibiting a ‘‘diminishing rate of return’’ phenomenon. From a managerial perspective, it may not pay to choose an overpowerful PCS, as the marginal reduction in the overall response time cannot be justified. This turning point occurs roughly around the point where the PCS is half as powerful as the remote Web server.

We experiment with the effect of the PCS’s look up time, $I _ { \mathrm { x c } }$ . The reduction of the overall response time, $T _ { \mathrm { x c } }$ , exhibits a linear behavior with respect to the reduction of $I _ { \mathrm { x c } }$ , a straightforward result as implied by the first term in Eq. 2.

## 3.5. Effect of the firm’s network bandwidth

In our experiments, the remote Web server’s network bandwidth is equivalent to a T1 line, $N _ { \mathrm { s } } = 1$ .544 Mbps, while the firm’s network bandwidth is the same as an ISDN line, $N _ { \mathrm { c } } = 1 2 8$ kbps. Since the firm usually has little control on the remote Web server’s network bandwidth, we do not investigate the effect of $N _ { \mathrm { s } }$ on the overall response time. Instead, we show the effect of the firm’s network bandwidth, $N _ { \mathrm { c } }$ , on the overall response time. Again, $N _ { \mathrm { c } }$ affects $T _ { \mathrm { x c } }$ and $T$ in the same way. Hence, changes in the firm’s network bandwidth, $N _ { \mathrm { c } }$ , will not positively or negatively affect the ‘‘relative’’ performance of the PCS as compared to the case without it. To see the ‘‘bottleneck’’ effect of the firm’s network bandwidth, which tends to be the slowest component in both Eqs. 2 and 3, we rearrange Eqs. 2 and 3 as follows:Overall response time with a PCS, $T _ { \mathrm { x c } }$

$$
\begin{array}{r l} T _ {\mathrm{xc}} & = \frac {I _ {\mathrm{xc}}}{1 - \lambda I _ {\mathrm{xc}}} + \frac {p}{\frac {B _ {\mathrm{xc}} R _ {\mathrm{xc}}}{\left(F Y _ {\mathrm{xc}} R _ {\mathrm{xc}} + F B _ {\mathrm{xc}}\right)} - \lambda_ {1}} + \frac {F}{N _ {\mathrm{c}}} \\ & + \frac {(1 - p) I _ {\mathrm{s}}}{1 - \lambda_ {2} I _ {\mathrm{s}}} + \frac {(1 - p)}{\frac {B _ {\mathrm{s}} R _ {\mathrm{s}}}{\left[ F Y _ {\mathrm{s}} R _ {\mathrm{s}} + F B _ {\mathrm{s}} \right]} - \lambda_ {2} / q} \\ & + \frac {(1 - p) F}{N _ {\mathrm{s}}} + \frac {p}{\frac {B _ {\mathrm{xc}} R _ {\mathrm{xc}}}{\left(F Y _ {\mathrm{xc}} R _ {\mathrm{xc}} + F B _ {\mathrm{xc}}\right)} - \lambda_ {2}}, \end{array}\tag{6}
$$

Table 4  
The bottleneck effect of $N _ { c }$ on T in Eq. 7

<table><tr><td> $N_c$ </td><td>Term 1</td><td>Term 2</td><td>Term 3</td><td>Term 4</td><td>T</td></tr><tr><td>64 kbps</td><td>0.0043</td><td>0.0051</td><td>0.0259</td><td>0.6250</td><td>0.6603</td></tr><tr><td>128 kbps</td><td>0.0043</td><td>0.0051</td><td>0.0259</td><td>0.3125</td><td>0.3478</td></tr><tr><td>1.54 Mbps</td><td>0.0043</td><td>0.0051</td><td>0.0259</td><td>0.0259</td><td>0.0612</td></tr></table>

and overall response time without a PCS, T:

$$
\begin{array}{l} T = \frac {I _ {\mathrm{s}}}{1 - \lambda I _ {\mathrm{s}}} + \frac {1}{\frac {B _ {\mathrm{s}} R _ {\mathrm{s}}}{\left(F Y _ {\mathrm{s}} R _ {\mathrm{s}} + F B _ {\mathrm{s}}\right)} - \lambda / q} \\ + \frac {F}{N _ {\mathrm{s}}} + \frac {F}{N _ {\mathrm{c}}}. \end{array}\tag{7}
$$

Tables 2 and 3 show the breakdown of all components of $T _ { \mathrm { x c } }$ in Eq. 6 and T in Eq. 7 when $N _ { \mathrm { c } }$ is varied. Both tables demonstrate that any increase in $N _ { \mathrm { c } }$ will decrease the overall response time to a great extent, either with or without a PCS. In these experiments, the arrival rate of users’ requests is <sup>s</sup> 20 requests $/ \mathrm { s } ,$ the average file size equals F<sup>s</sup>5000 bytes, the ‘‘cache hit rate’’ probability p is set at 0.5, and the remote Web server has the bandwidth of a T1 line.

In both Tables 3 and 4, the bottleneck effect of the firm’s network bandwidth is evidenced by $N _ { \mathrm { c } }$ being the dominant terms in both tables. In fact, increasing $N _ { \mathrm { c } }$ from 64 to 128 kbps reduces $T _ { \mathrm { x c } }$ by 47.33% and T by 47.95%. Although the firm’s network bandwidth does not impact the decision of whether to install a PCS, Tables 2 and 3 indicate that improving it has the significant benefit of shortening the overall response time to users’ Web requests.

## 4. Concluding remarks and future research

Coincident with the World Wide Web’s taking off in recent years, the role of a PCS in improving response time to Web requests has become an active research area. Prior research has focused on analyz ing or developing various cache replacement algorithms. We look at a more fundamental problem by examining the impact of installing a PCS on overall response time to Web requests. Using an analytical queuing model, we examine various performance issues related to a firm’s PCS. Several factors are identified that influence the behavior of the PCS. These factors include the arrival rate of users’ Web requests, the average size of requested files, the ‘‘cache hit rate’’ probability, the bandwidth of the LAN, and several server-specific parameters.

The major findings show that the response time decreases as cache ‘‘hit rate’’ probability increases, for various arrival rates and different file sizes. With higher arrival rates or larger file sizes, the response time increases for both the cache and the non-cache cases, and the benefit of the PCS becomes more prominent.

We identified a ‘‘crossover probability’’ that represents the minimum cache ‘‘hit rate’’ probability after which installing a PCS becomes beneficial. This probability decreases with increases in the arrival rate of Web requests or the requested file size. The benefits of installing a PCS were seen to be more pronounced for heavier Web usage. Further, the marginal reduction of the crossover probability levels off for larger files.

The response time decreases when the PCS has a bigger output buffer, or a faster server rate. There is, however, a ‘‘diminishing rate of return’’ phenomenon to enhance the PCS performance. From the manager’s standpoint, it may not pay to choose an overpowerful PCS, as the marginal reduction in the overall response time cannot be justified.

We have not been concerned with the pros and cons of different cache replacement algorithms, nor with the freshness of the cached content. A common practice to diminish these issues is for the PCS to have a reasonably large storage and to refresh the cached content during off-peak hours e.g., nights . Ž . The queuing model used is a static model that provides a snapshot of randomly fluctuating arrival patterns. For those types of arrivals, a transient analysis would be more appropriate, but this is beyond the scope of this research.

There are several potentially fruitful extensions to this work. The model assumes that the requested files are, on the average, of the same size. In reality, multimedia files audio, video and image files areŽ . larger in size compared to non-multimedia files plainŽ text and pure HTML . One extension would consider.

two classes of files, large files and small files. Using similar numerical techniques, the behavior of the PCS for handling a mixture of files of various sizes can be explored. The desired model should consider assigning higher priority to multimedia traffic. In the presence of multimedia traffic, the variance as well as the mean of response times should be examined. Also to be investigated is whether the PCS becomes especially beneficial for improving the response time as the proportion of multimedia traffic increases.

Recent literature on modeling Internet traffic reported that the Web traffic is usually bursty and as such, there is some debate on how good Markovian models are in analyzing this kind of traffic 6 . It<sup>w</sup> <sup>x</sup> would be useful to understand the behavior of the PCS given bursty arrivals that are modeled as Markov Modulated Poisson Processes. We have considered the case of a single PCS with a single remote Web server, which could be extended to the case of several PCSs in a serial or parallel mode. Further extensions would incorporate multiple proxy caches and study the interactions and influences between them, or explore the effect of ‘‘mirror’’ remote Web servers.

## 5. Model parameters

λ arrival rate of requests for Web pages inŽ number of requests per second.

$F$ the average file size of users’ requests inŽ bytes.

$B _ { \mathrm { s } }$ the size of Web server’s output buffer inŽ bytes.

$I _ { \mathrm { s } }$ total time required for the one-time initialization at the remote Web server in sec-Ž onds.

$Y _ { \mathrm { s } }$ the static server time of the Web server inŽ seconds.

$R _ { \mathrm { s } }$ dynamic server rate of the Web server inŽ bytes per second.

$B _ { \mathrm { x c } }$ the size of PCS’s output buffer in bytesŽ . $I _ { \mathrm { x c } }$ the lookup time of the PCS in secondsŽ .

$Y _ { \mathrm { x c } }$ the static server time of the PCS in sec-Ž onds.

$R _ { \mathrm { x c } }$ dynamic server rate of the PCS in bytesŽ per second.

$$
p
$$

the probability that the desired content is already stored at the PCS

$q$ the branching probability that the remote Web server can fulfill a request from the proxy cache at the first try

$N _ { \mathrm { s } }$ server network bandwidth, the speed of the server’s connection to the Internet in bitsŽ per second.

$N _ { \mathrm { c } }$ client network bandwidth, the average speed the client browser software receives a buffer’s worth of data in bits per sec-Ž ond.

## Acknowledgements

The authors gratefully acknowledge comments and suggestions of Professors Ira Horowitz and Gary Koehler and two anonymous reviewers. Any remaining error belongs to the authors.

## References

<sup>w</sup> <sup>x</sup> 1 C. Aggarwal, J.L. Wolf, P.S. Yu, Caching on the World Wide Web, IEEE Transactions on Knowledge and Data Engineering 11 1999 94–107.Ž .

<sup>w</sup> <sup>x</sup> 2 V.A.F. Almeida, J.M. de Almeida, C.S. Murta, Performance analysis of a WWW server, in: Proceedings of the 22nd International Conference for the Resource Management and Performance Evaluation of Enterprise Computing Systems, San Diego, USA, December 8–13, 1996.

<sup>w</sup> <sup>x</sup> 3 M.A. Arlitt, C.L. Williamson, Internet Web servers: workload characterization and performance implications, IEEE<sup>r</sup>ACM Transactions on Networking 5 5 1997 631–Ž . Ž . 645, October.

<sup>w</sup> <sup>x</sup> 4 M. Baentsch, L. Baum, G. Molter, S. Rothkugel, P. Sturm, Enhancing the Web’s infrastructure: from caching to replication, IEEE Internet Computing 1997 18–27, MarchŽ . <sup>r</sup>April.

<sup>w</sup> <sup>x</sup> 5 S.J. Caughey, D.B. Ingham, M.C. Little, Flexible open caching for the Web, Computer Networks and ISDN Systems 29 1997 1007–1017.Ž .

<sup>w</sup> <sup>x</sup> 6 M.E. Crovella, A. Bestavros, Self-similarity in World Wide Web traffic: evidence and possible causes, IEEE<sup>r</sup>ACM Transactions on Networking 5 6 1997 835–846, Decem-Ž . Ž . ber.

<sup>w</sup> <sup>x</sup> 7 M. Ferelli, Like politics, all web caching should be local, Computer Technology Review 1998 1–19, April. Ž .

<sup>w</sup> <sup>x</sup> 8 D. Gross, C.M. Harris, in: Fundamentals of Queuing Theory, 2nd edn., Wiley, 1985.

<sup>w</sup> <sup>x</sup> 9 M. Kurcewicz, W. Sylwestrzak, A. Wierzbicki, A filtering

algorithm for Web caches, Computer Networks and ISDN Systems 1998 2203–2209, November 25.Ž .

<sup>w</sup> <sup>x</sup> 10 A. Luotonen, Web Proxy Servers, Prentice-Hall, 1998.

<sup>w</sup> <sup>x</sup> 11 L. Margherio, et al., The emerging digital economy, U.S. Department of Commerce Report, 1998 http:Ž <sup>rr</sup>www.ecommerce.gov ..

<sup>w</sup> <sup>x</sup> 12 D.A. Menasce, V.A.F. Almeida, Capacity Planning for Web Performance: Metric, Models, and Methods, Prentice-Hall, 1998.

<sup>w</sup> <sup>x</sup> 13 P. Rodriguez, E.W. Biersack, Continuous multicast push of Web documents over the Internet, IEEE Network 1998Ž . 18–31, March<sup>r</sup>April.

<sup>w</sup> <sup>x</sup> 14 P. Scheuermann, J. Shim, R. Vingralek, A case for delayconscious caching of Web documents, Computer Networks and ISDN Systems 29 1997 997–1005.Ž .

<sup>w</sup> <sup>x</sup> 15 J. Shim, P. Scheuermann, R. Vingralek, Proxy cache algorithms: design, implementation and performance, IEEE Transactions on Knowledge and Data Engineering 11 1999Ž . 549–561.

<sup>w</sup> <sup>x</sup> 16 L.P. Slothouber, A model of Web server performance, in: 5th International World Wide Web Conference, Paris, France, May, 1996.

<sup>w</sup> <sup>x</sup> 17 R.P. Wooster, M. Abrams, Proxy caching that estimates page load delays, Computer Networks and ISDN Systems 29 Ž . 1997 977–986.

Dr. Indranil Bose received his PhD from Krannert Graduate School of Management, Purdue University in 1997. He has research interests in telecommunications design and policy issues, data mining and artificial intelligence, electronic commerce, applied operations research, human–computer interaction and telemedicine. His teaching interests are in telecommunications, database management, systems analysis and design, and global management of information systems. He has had works published in Computers and Operations Research, and Ergonomics.

Dr. Hsing Kenneth Cheng received his PhD from William E. Simon Graduate School of Business Administration, University of Rochester in 1992. Professor Cheng teaches information technology strategy and electronic commerce. His research interests involve electronic commerce, economics of information systems, and computer clustering technology. His works have appeared in Computers and Operations Research, Decision Support Systems, European Journal of Operational Research, IEICE Transactions, Journal of Business Ethics, Journal of Management Information Systems, and Socio-Economic Planning Sciences. He also contributed book chapters on ‘‘Hacking, Computer Viruses, and Software Piracy: The Implications of Modern Computer Fraud for Corporations’’ and ‘‘The Critical Role of Information Technology for Employee Success in the Coming Decade.’’
