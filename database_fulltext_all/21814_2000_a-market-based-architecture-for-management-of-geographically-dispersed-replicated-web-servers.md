---
otero_id: 21814
otero_key: "NEVKRV9Y"
title: "A market-based architecture for management of geographically dispersed, replicated Web servers"
authors: "Mehmet Karaul; Yannis A. Korilis; Ariel Orda"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00068-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A market-based architecture for management of geographically dispersed, replicated Web servers

Mehmet Karaul <sup>a,)</sup>, Yannis A. Korilis <sup>b,1</sup>, Ariel Orda <sup>c,2</sup>

Bell Laboratories, Murray Hill, NJ 07974-0636, USA

Bell Laboratories, Holmdel, NJ 07733-3030, USA

Department of Electrical Engineering, Technion, Technion City, Haifa 32000, Israel

## Abstract

Distributed Web sites require allocation mechanisms to dispatch request in a scalable and controllable manner among a set of replicated servers. Unlike most existing approaches, we propose a technique that pushes the allocation functionality onto the client and argue that this approach scales well and may result in increased performance in many cases. Building on theoretical work based on game theory, we show that the usage of individual replicas can be effectively controlled with cost functions even when the clients are noncooperative. We present the design and implementation of WebSeAl, our prototype system realizing these techniques, and present experiment results. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Resource allocation; Load balancing; Scalability; Replication; HTTP; Pricing; Game theor

## 1. Introduction

The rapid growth of the World Wide Web has led to a steady increase of client requests to many popular Web sites. Both, overloaded servers and network congestion, contribute to slow response times of such sites. It may not be cost-effective to upgrade the server machine with a more powerful one, especially when incremental scalability is desired. Instead, most sites opt to replace the single server with a cluster of replicated servers 16,17 .<sup>w</sup> <sup>x</sup> Although this may solve the problem of overloaded servers, it does not address network congestion. Some sites choose to geographically distribute the replicated servers — this approach has become popular with software archives e.g., Ref. 21 , which haveŽ <sup>w</sup> <sup>x</sup>. mirror sites, typically on several continents. Such a distributed architecture may result in increased availability of the service in times of network congestion and partial unavailability, and it may increase performance by taking advantage of proximity between clients and servers. Typically, the service content is replicated or a distributed file system 9,19 is used.<sup>w</sup> <sup>x</sup>

Service providers using such a distributed architecture require means to effectively control the usage of individual replicas. More specifically, they require means to route<sup>3</sup> requests in a way such that the resulting load distribution coincides with the target load distribution the service provider seeks. A target load distribution might be to partition the incoming requests evenly among the replicas; or the service provider might want to temporarily discourage clients from using a certain replica, for maintenance reasons or to perform other site’s specific tasks, for example.

Currently, many distributed Web sites require the user to manually select a server out of a list of replicas. This is inconvenient for the user, and a decision to use a certain server might result in poor performance depending on network conditions and the load of the selected server. Furthermore, this approach does not allow service providers to control the load distribution among the replicas.

Designing a transparent allocation strategy for a distributed Web site that does not sacrifice any of the benefits of such a distributed architecture is a challenging task. A successful solution must meet several requirements including:

<sup>Ø</sup> Load Balancing: Service providers should be able to effectively control the utilization of individual servers.

<sup>Ø</sup> Geographic Distribution: Network delays between a client and individual servers of a distributed service might differ significantly. Server allocation should take advantage of this while still accommodating dynamic changes in network performance and server load.

<sup>Ø</sup> Scalability: Server allocation should gracefully scale with the increasing number of clients.

<sup>Ø</sup> Transparent Name Resolving: Popular Web sites have well-publicized server names and require a transparent mapping to replicated servers.

<sup>Ø</sup> Dynamic Changes in Server Pool: Addition, removal, and migration of servers should be supported, and changes should be reflected as quickly as possible.

<sup>Ø</sup> Fault Transparency: Unresponsive machines should be detected and requests transparently redirected to other replicas. Also, previously unresponsive machines that become available again should be incorporated quickly.

<sup>Ø</sup> Flexibility: Different users may have different objectives when accessing Web sites, requiring support for customized strategies.

<sup>Ø</sup> Legacy Code and Standards: It should not require any changes to existing client or server code and should conform to existing standards.

A comprehensive solution for allocation of distributed Web servers must address all these factors. We are not aware of any other system that achieves this. In this paper, we present a system called Web-SeAl that addresses these issues.

The research leading to WebSeAl is based on theoretical work, where provable methods for controlling network load using pricing mechanisms were developed 13,14 . It was shown that even with<sup>w</sup> <sup>x</sup> noncooperative clients in a fully distributed, and Ž therefore scalable fashion , the network load can be. controlled effectively. The work presented here applies these techniques to provide scalable and controllable load balancing for distributed Web servers.

The remainder of this paper is structured as follows. Section 2 gives an overview of related work. We will then present the decentralized design of WebSeAl and then describe how logical names are resolved. Sections 5 and 6 discuss how WebSeAl can enforce any desired load distribution over the server pool. In Section 7, implementation issues regarding our prototype are addressed. This will be followed by experiments and concluding remarks.

## 2. Related work

The HTTP redirect 1 approach uses the HTTP<sup>w</sup> <sup>x</sup> return code URL Redirection <sup>w</sup> <sup>x</sup> 2 to perform load balancing. A busy server returns the address of another server instead of the actual response, asking the client to resubmit its request to that server. This creates additional network traffic and increased latency. Every request is initially addressed to the publicly known server that creates a single point of failure and the potential for a bottleneck due to servicing redirects.

Domain Name Server DNS -based approachesŽ . <sup>w</sup> <sup>x</sup> 3,5,11 perform load balancing at the name resolution level. The name server at the server side is modified to respond to translation requests with the IP numbers of different hosts in a round-robin fashion. This results in partitioning client requests among the replicated hosts. The main disadvantage of this approach is that intermediate name servers and clients’ cache name-to-IP mappings, which can result in significant load imbalance. A similar approach is described in Ref. 8 , where any cast resolvers are<sup>w</sup> <sup>x</sup> used to perform a one-to-many mapping based on locally maintained performance data about individual replicas. The goal is no minimize end-to-end delays, but the issue of enforcing a desired load distribution is not addressed.

Server-side approaches 5,7 use a server-side <sup>w</sup> <sup>x</sup> routing module that redirects all incoming requests to a set of clustered hosts based on load characteristics. This is achieved at the IP layer — i.e., the routing module modifies all IP packets before forwarding them to individual hosts. An alternate server-side solution that avoids modifying IP packets is presented in Ref. 6 . These approaches have the<sup>w</sup> <sup>x</sup> drawback that the routing module represents a single point of failure, and therefore can result in a bottleneck since all requests pass through it. In addition, server-side approaches work well only for clustered servers.

Perhaps most closely related to WebSeAl is the work presented in Ref. 22 . It uses a modified Web<sup>w</sup> <sup>x</sup> browser to perform routing decisions at the client side. The browser downloads an applet, which the service provider needs to implement to realize service specific routing. This approach creates increased network traffic due to applet transmission and potential control messages between the applet and the servers.

## 3. Design

A simple solution to enforce a load distribution over a set of replicated servers is to make sure that all requests pass through some sort of a central dispatcher, which directs individual requests to different replicas depending on the target load distribution. Since this central dispatcher has global knowledge, ensuring a specific load distribution is not difficult. However, such an approach raises scalability concerns. Also, it does not address the issue of geographic distribution appropriately; a client will not be able to take advantage of a close-by replica if the central dispatcher is located far away since each request needs to pass through the dispatcher.

WebSeAl uses a decentralized approach to address the issue of scalability and geographic distribution. In WebSeAl, it is actually the client who makes routing decisions. At times, we will refer to such clients as noncooperative. There is no central entity that dispatches the requests. This fully distributed approach should scale well with the number of clients, and it makes it possible for clients to take advantage of geographic proximity, specifically, fast network connections between the client and certain replicas.

The basic functionality at the client side can be described as follows:

<sup>Ø</sup> Clients make routing decisions.

<sup>Ø</sup> They maintain a cache of address information.

<sup>Ø</sup> They collect dynamic performance data e.g., net- Ž work conditions, server load, and other site’s specific data ..

<sup>Ø</sup> Clients base routing decisions on this data.

<sup>Ø</sup> They automatically redirect the request to an alternate server if the selected server is not responsive.

Besides delivering the actual service, servers provide clients with address information. They also communicate with other site’s specific data, which might be used to control access to the server pool, to support charging for services, and so forth, as will be discussed in Section 6.

With such a decentralized approach, the actual load distribution among the server pool will solely depend on how clients make their routing decisions. Therefore, the challenge is to make sure that clients implement routing strategies so that the resulting load distribution coincides with the desired one. This is a much harder problem compared to the centralized approach since each client has only ‘‘partial knowledge’’, and there is no entity that has global knowledge. We will discuss in Sections 5 and 6 how WebSeAl ensures that any target load distribution can be enforced. Before addressing these issues, we will first describe how clients find out about replicas.

## 4. Name resolution

A server is identified by a logical address in the form of a hostname. When a client attempts to contact a server, the DNS system transparently resolves the hostname to an IP number, which is successively used to establish the connection. To contact a distributed server in a transparent fashion, a one-to-many mapping from the hostname to one of the IP numbers of the replicated machines is needed. WebSeAl pushes this name resolving functionality onto the clients.

## 4.1. Replica address cache

As mentioned earlier, clients maintain a cache of replica address information. They use this information to access a distributed Web site identified by a hostname, e.g., www.yahoo.com. A mapping consists of the hostname and the IP numbers of the replicas making up the distributed service. Using this information, clients perform a one-to-many mapping from the public hostname to the IP numbers of the individual replicas see Fig. 1 .Ž .

When a client attempts to access a distributed server for which it does not have a mapping cached, it uses standard DNS name resolving and contacts the server at that hostname. This means that one of the replicas is known to the standard DNS system by the logical address of the distributed Web site. More specifically, a distributed Web site consists of a set of servers $S _ { 1 } , \ldots , S _ { n }$ , each with its own IP number $\operatorname { I P } _ { 1 } \ldots . \operatorname { I P } _ { n }$ Fig. 2 . One of these servers is known toŽ . the standard DNS system by the hostname of the distributed Web site. This server will successively communicate the addresses of all replicas to the client as will be discussed below . Future requestsŽ . to this distributed service use this information to perform one-to-many mappings from the logical address to the individual hosts. The standard DNS system is used only for bootstrapping — once a mapping for a logical address is cached, the DNS system is not needed to access any of the replicas. The service will be accessible as long as at least one replica remains responsive.

![](/api/attachments/NEVKRV9Y/fulltext/images/c09f0a1765f14738740d72f60a8d0eea4900e790435ffc10949cb54212458864.jpg)  
Fig. 1. One-to-many mapping from hostname to IP numbers.

![](/api/attachments/NEVKRV9Y/fulltext/images/73629f2b7179507be492145473784694ebd3487ee1133a0a5b4b5ab6a9152c09.jpg)  
Fig. 2. A distributed Web site with logical address and IP numbers.

Servers communicate address information to the clients. Each server is assumed to have address information about all replicas — this information can be made available to individual replicas in the same way the service content is made available to them. Servers include the addresses of the individual servers in the actual response they generate. Clients extract these addresses from the response and update their cache accordingly.

Clients need to retrieve the addresses of the servers only to create an initial entry or to refresh their cache if the address information has changed in any way. To avoid unnecessary transmission of address information, clients include a timestamp in their requests, which indicates the state of the currently cached mapping for the given distributed server. Servers along with the addresses provide this timestamp. Upon receipt of a request, a server inspects this timestamp and includes the addresses and the new timestamp in the response only if more up-to-date address information is available. This is very similar in nature to the If-modified-since header 2 , which is<sup>w</sup> <sup>x</sup> used to avoid retrieving cached files that have not been modified since a certain date.

GET http://www.yahoo.com/index.html HTTP/1.0 Timestamp: Sun, 06 Nov 1994 08:49:37 GMT

Fig. 3. HTTP request message with Timestamp header.

## 4.2. Propagation of addresses

HTTP allows application specific header fields and requires that all intermediaries such as proxies or gateways conforming to HTTP ignore these and forward them unchanged. This is used to piggyback timestamps and addresses in HTTP messages. Web-SeAl introduces two new message headers: Timestamp and Addresses. Clients use the first header to notify servers about the status of their cached addresses for the distributed server at hand see Fig. 3 .Ž . Servers use both headers to return a list of addresses and the timestamp at which this information was generated see Fig. 4 .Ž .

The format of a Timestamp header is defined as follows:

## Timestamp: HTTP-date

HTTP-date is the standard date<sup>r</sup>time stamp format used on the Internet as defined in Ref. 2 .<sup>w</sup> <sup>x</sup>

The format of an Addresses header is defined as follows:

## Addresses: IP-number-list

IP-number-list is the list of IP numbers separated by whitespaces.

Mapping a hostname to a set of IP numbers shares many similarities with DNS-based and server-side approaches, which will be described in Section 2. Notice that these approaches require that the servers on all replicated hosts accept connections at the same port. In addition, the directory structure must be identical on each host. WebSeAl’s architecture relaxes these restrictions. The mapping from hostname to IP numbers can easily be extended to a mapping from hostname and port to IP number and port to accommodate the usage of different port numbers. This requires that the address information included in responses be extended to contain port numbers as well as host-names. Path offsets can be accommodated similarly see Fig. 5 . For example, www.Ž . yahoo.com:80<sup>r</sup> can be mapped to 122.140.128. 40:8080<sup>r</sup>yahoo<sup>r</sup>. On the first host, the server is accepting connections at port 80 and the directory structure is rooted at <sup>r</sup>. On the second host, the server accepts connections at port 8080 and the root directory is at <sup>r</sup>yahoo<sup>r</sup>. Many mirror sites use different root directories and require a relative path offset. This allows a single host to serve as a replica for multiple distributed Web sites.

Fig. 4. HTTP response message with Timestamp<sup>r</sup>Addresses headers.  
![](/api/attachments/NEVKRV9Y/fulltext/images/414b8f5559d9151ce83c0afedc3c8f963f0378e1f805ad8f18ca7b13902a4994.jpg)  
Fig. 5. Extended mapping with port numbers and relative path offsets.

## 5. Routing strategies

As mentioned before, in WebSeAl, it is the clients who make routing decisions. When clients make routing decisions, the resulting load distribution over the server pool will be solely the result of the routing strategies the clients implement. To be able to control the resulting load distribution, mechanisms are needed to influence the client-side routing decisions. We use a pricing scheme to achieve this in Web-SeAl. We will present the details in two steps. In this section, we will assume that the service provider does not attempt to enforce a specific load distribution, and that the only objective for clients is to minimize their own delay. In Section 6, we will extend these techniques and present how WebSeAl can enforce any target load distribution.

The fact that many Web pages contain several images and frames results in the generation of several requests to retrieve a single Web page. WebSeAl clients measure the total response time for each such request. The total response time measured is the complete end-to-end delay, which includes connection establishment, network delay, and server time. WebSeAl clients strive to minimize this total delay.

Each client makes routing decisions based on the average response time of each server. These averages are estimated using the measured response times for the N most recent requests, for some N. The updated routing strategy is used to direct the next N requests to the appropriate servers in the pool. Alternatively, the client could estimate the average response times by sending occasional probes at the cost of increased network traffic. In the current prototype, we decided against this approach to avoid control messages between clients and servers.

One possible routing strategy clients could employ is to always contact the most responsive server. This approach, however, will fail to collect new performance data for the slower servers. Instead, we use probabilistic routing to ensure that clients collect new performance data for all servers. More specifically, if $T _ { i }$ denotes the average response time for requests routed from a client to server i, then the client will route its next N requests based on the probability distribution:

$$
p _ {i} = \frac {1 / T _ {i} ^ {k}}{\sum_ {j} 1 / T _ {j} ^ {k}},\tag{1}
$$

where the exponent $k \geq 0$ is a constant.

With $k = 0$ , requests are routed to the servers randomly, without taking into account their performance. With k<sup>s</sup>1, we can achieve linear distribution. This will favor fast machines while still using slower ones. However, the overall performance might suffer due to possibly long delays from slow servers. By raising k, more requests will be routed to the most responsive servers. Very high routing probabilities for the fastest servers will cause very infrequent usage of slower ones, which in turn will decrease the potential to quickly detect improved servers. WebSeAl imposes a minimum threshold to prevent very low probabilities.

In the current prototype, routing decisions are based on the most recent N measurements. We are considering several alternate strategies:

<sup>Ø</sup> Sliding Window: Instead of calculating estimates every N requests using the last N measurements, one could update the estimates after every measurement, always using the last N measurements.

<sup>Ø</sup> Weighted Average: When calculating the performance estimates of replicas, more recent data should impact the overall performance more than older data, and the estimates should be updated more frequently.

<sup>Ø</sup> Time-of-Day: Network conditions and server usage vary with the time-of-day or the day of the week 4,10 , and this information could be con-<sup>w</sup> <sup>x</sup> sidered in the routing strategy.

WebSeAl allows different clients to use different routing strategies. As future work, we plan to experiment with various strategies and to investigate how each one and various combinations perform in different settings. Our goal is to realize a set of routing strategies and to adapt dynamically to changing conditions.

As explained earlier, in the current implementation of WebSeAl, the routing strategy employed by the clients aims at forwarding requests to the most responsive servers. It is worth mentioning that if the clients aim at minimizing the average response time for their requests, this is not the optimal routing strategy. More specifically, as shown in Refs. 18,12 , the optimal routing strategy is to send requests to servers with minimal deriÕatiÕes of the response times. Assuming, however, that there is a very large number of clients, each of which contributes a small fraction of the total offered load,<sup>5</sup> contacting the servers with minimal response times approximates the optimal routing strategy.

## 6. Load distribution

Using the results from the previous section, the load distribution over the server pool also calledŽ operating point. is solely the result of the interaction among the distributed clients and cannot be controlled by the service provider. In this section, we will discuss strategies that can be used at the server side to control the load distribution while clients make their routing decisions in a noncooperative manner.

The service provider aims at distributing the load currently offered to the server pool in a way that is deemed efficient from the system’s point of view. The provider, for instance, might desire a load distribution that minimizes the oÕerall average response time of the server pool. In other cases, the provider might want to discourage usage of certain machines — even if they are the most responsive ones — in order to perform other site’s specific tasks. Therefore, a mechanism is needed to make the distributed clients implement routing strategies that lead to a load distribution that coincides with the desired one.

The problem of managing the behavior of systems, where control is distributed and noncooperative, is a fundamental one. The interaction among the various distributed controllers the clients in Web-Ž SeAl can be modeled as a . game, and Game Theory provides the systematic framework to study and analyze the behavior of such systems — for an overview of game theoretic aspects in computer networking, see Ref. 12 and references therein. The operating<sup>w</sup> <sup>x</sup> points of the system are the Nash equilibria of the underlying control game. Noncooperative equilibria are inherently inefficient: while each controller strives to optimize its individual performance, the overall behavior of the system is generically suboptimal.

WebSeAl uses a pricing mechanism to provide incentives to the noncooperative clients to implement routing strategies that lead to the desired load distribution over the server pool. The methodology is motivated by recent analytical studies in the area of networking, which have shown that a network<sup>r</sup> service provider can enforce any desired operating point by means of appropriate pricing strategies <sup>w</sup> <sup>x</sup> 13,14 . The key idea in WebSeAl’s pricing mechanism is that there is a weight factor associated with obtaining service from each server in the pool. Clients make their routing decisions based not only on performance statistics, but also on weight information for each server. The main assumption behind this mechanism is that the clients are indeed sensitive to weight factors. This behavior is expected in private Intranets, where clients and the pricing mechanism are part of the same management system. For external clients accessing a Web site, this behavior can be enforced by actual usage-based service charges forŽ commercial Web sites , or by means of limited. electronic budget allocated to each client — an architecture developed according to these ideas is proposed in Ref. 15 . When clients are sensitive to<sup>w</sup> <sup>x</sup> weight factors, the service provider can control not only the load distribution over the available servers, but also the total offered load itself.

## 6.1. Pricing strategies

The goal of the pricing mechanism in WebSeAl is twofold:

<sup>Ø</sup> Avoidance of congestion overload conditions atŽ . various servers.

<sup>Ø</sup> Load balancing — that is, distribution of the total load offered to the Web site among the available servers in a way that is deemed efficient by the provider.

The pricing strategies in the current version of WebSeAl are based on analytical results in Ref. 14 .<sup>w</sup> <sup>x</sup> That study considers a system of general network resources accessed by a number of noncooperative clients. Each resource is characterized by its ‘‘capacity’’, that is, the maximum load that can be accommodated by the resource. Congestion pricing is proposed as a means for avoiding overload conditions: the weight factor per size unit i.e., the price of eachŽ . resource is proportional to the congestion level at the resource that depends on the total load offered to it by the clients. More specifically, the price of each resource is given by the congestion function associated with the resource multiplied by a weight factor. These weight factors determine the relative sensitivity of the clients to the congestion level at the various resources. Load balancing can be achieved by appropriate choice of these weight factors. This pricing strategy is shown to allow the provider to enforce any desired operating point while the clients make their routing decisions noncooperatively.

Along the lines of these analytical results, the pricing strategy in the current design of WebSeAl is based on a weight factor for each server in the pool, which determines the relative sensitivity of the clients to the responsiveness of the server.<sup>6</sup> In particular, the performance metric considered by each client in making its routing decisions is the average response time of each server multiplied by the corresponding weight factor. Therefore, if $w _ { i }$ is the weight factor of server i, and $T _ { i }$ the average response time from the server to a client, then the routing strategy of the client described by Eq. 1 becomes:

$$
p _ {i} = \frac {1 / (w _ {i} T _ {i}) ^ {k}}{\sum_ {j} 1 / (w _ {j} T _ {j}) ^ {k}}.\tag{2}
$$

We note that $w _ { i } T _ { i }$ corresponds to the price for receiving service from server i. Therefore, the rout ing strategy of the client aims at forwarding requests to servers of minimal price. Similarly to the remark at the end of Section 5, if the client aims at minimizing the total service cost, the optimal routing strategy is to send requests to servers with minimal derivatives of the service prices 14 . Assuming, however, that there is a very large number of clients, each of which contributes a small fraction of the total offered load, contacting the servers with minimal service prices approximates the optimal routing strategy.

## 6.2. AdaptiÕe algorithm to determine weight factors

Server weight factors are determined based on the operating point the provider wants to enforce. One way to determine these factors is to map the parameters of the model considered in Ref. 14 to the<sup>w</sup> <sup>x</sup> characteristics of WebSeAl and apply the corresponding analytical results, expecting to achieve a good approximation of the desired operating point. Instead, we choose to use an adaptiÕe algorithm, also proposed in Ref. 14 , which does not depend on <sup>w</sup> <sup>x</sup> the details of the underlying analytical model. The algorithm updates the weight factors iteratively, based on the ‘‘distance’’ of the current operating point from the desired one.

If $f _ { i } ^ { * }$ denotes the desired load at server i and $f _ { i } ( n )$ the actual load offered to the server during the nth iteration, then its weight factor $w _ { i }$ is updated using the following:

$$
w _ {i} (n + 1) = w _ {i} (n) e ^ {\theta_ {i} (f _ {i} (n) - f _ {i} ^ {*})},\tag{3}
$$

where $\theta _ { i } > 0$ is a constant that determines the rate of change in the weight factor of server i. The idea behind this iterative scheme is that if the server is currently receiving less load than the desired one, its weight factor should be decreased. This decreases the clients’ sensitivity to the congestion level at the server, thus encouraging them to direct more of their requests to it. Similarly, if the server receives more load than the desired one, its weight factor is increased. Under a set of general assumptions guaranteeing that the client population as a total reacts ‘‘rationally’’ to price changes, this iterative scheme was shown in Ref. 14 to drive the system to the<sup>w</sup> <sup>x</sup> desired operating point.

In the current implementation of WebSeAl, server load is expressed in requests per unit of time. Considering HTTP requests, we expect that each client generates a large number of requests, each of which will be small to moderate size. Therefore, this is a satisfactory approximation. A more precise load metric would consider the actual size of each request and will be incorporated in future implementations.

Each distributed Web site is equipped with a pricing manager. Based on the target operating point, the pricing manager determines the weight factors to access each server and communicates it to the corresponding server. More specifically, the pricing manager periodically collects information about the load offered to each server by contacting the corresponding server, updates the weight factors according to iteration 3, and communicates them to the servers. Each server receives only the update of its own weight factor and is responsible for advertising this to the clients. This is achieved by piggybacking the weight factor of the server to HTTP messages, which contain the responses to the clients’ requests.

## 7. Implementation

WebSeAl’s server-side functionality could be added to existing Web servers quite easily and should impose only little computational overhead. However, to create a usable system without having to modify existing servers, WebSeAl provides a stand-alone Java application, called serÕer agent, which implements the server-side functionality see Fig. 6 . TheŽ . server agent functionality can be outlined as follows:

<sup>Ø</sup> The server agent uses the HTTP port to intercept each incoming request.

![](/api/attachments/NEVKRV9Y/fulltext/images/e8bf6d2e56fb75a81573e74488b59f0f64827352cc81126f43daf06d4dae258b.jpg)  
Fig. 6. WebSeAl client agent and server agent.

<sup>Ø</sup> It forwards the request to the local HTTP server.

<sup>Ø</sup> It accepts the response.

<sup>Ø</sup> The server agent adds address information in-Ž cluding timestamps to the response, as needed..

<sup>Ø</sup> It forwards the response to the client.

The client-side functionality is somewhat more complex, but it should be fairly straightforward to extend existing Web browsers or proxies to support this functionality. Similar to the server agent, Web-SeAl provides a stand-alone Java application, called client agent, which realizes the client-side functionality in order to provide a usable system without having to modify existing browsers or proxies. We take advantage of the fact that virtually all browsers support proxies to intercept requests. When the client agent is started up, it creates a server socket that accepts HTTP requests, very much like a proxy does. By configuring the browser to use the ‘‘proxy’’ i.e., Ž WebSeAl client agent , the client agent effectively. intercepts each request. More specifically, the client agent functionality can be described as follows:

<sup>Ø</sup> A client agent uses the proxy ‘‘hook’’ to intercept each request generated by browsers.

<sup>Ø</sup> It maintains a cache of replica address information.

<sup>Ø</sup> It makes routing decisions as described above.

<sup>Ø</sup> The client agent adds a timestamp to the request.

<sup>Ø</sup> It measures the total end-to-end delay of the request.

<sup>Ø</sup> It forwards the request to the selected server.

<sup>Ø</sup> It accepts the response.

<sup>Ø</sup> The client agent transparently redirects the request to alternate servers if a selected server remains unresponsive for a certain timeout period.

<sup>Ø</sup> It extracts address information and updates its cache, if necessary.

<sup>Ø</sup> It forwards the response to the client.

Proxies are generally used to allow Internet access through firewalls and perform caching of Web documents. WebSeAl’s client agent can accommodate proxies in two ways. A client agent can be located between one or more clients and a proxy. Since name resolution is performed at the client agent, the proxy will treat identical documents from different replicas of the same distributed server as different documents and create redundant copies in its cache. Alternatively, the client agent can be located ‘‘behind’’ the proxy. This configuration avoids the problem of redundant copies in the proxy cache. Also, only one address cache and a single set of statistical data is maintained for a number of users, resulting in more up-to-date address caches and more accurate estimates.

Both WebSeAl’s server and client agent functionality should ideally be included in Web servers and browser or proxies. We provide client and server agents to enable service providers and users to take advantage of this technology without the need to modify existing systems. Independent of whether agents are used or existing systems are modified, for a system like WebSeAl to gain wide acceptance, it needs to be backward compatible with regard to clients and servers lacking this functionality. Web-SeAl is backward compatible and supports gradual infiltration.

WebSeAl Client and Standard Server: A standard HTTP server is required to ignore the timestamp header in a request from a WebSeAl client agent and will service the request as usual. The lack of address information in the response indicates to the client agent that it is dealing with a standard server. It can react to this, for example, by infrequently including the timestamp in its future requests in order to update its cache in case this site is upgraded.

Standard Client and WebSeAl Server: A request received by a server agent will not contain a timestamp header if the client lacks WebSeAl functionality. The server can react to this in several ways; two possibilities are: 1 it can service the request inŽ . a standard manner without including any address information in its response; 2 it can route theŽ . request on behalf of the client to individual servers.

There are a few issues that are not addressed in the current prototype. All of these seem to be solvable, and we plan to incorporate these in future versions of the system. Two concerns are as follows.

Cookies using IP numbers: Since request may be served by different hosts with different IP numbers, it is possible that the browser stores multiple cookies for the same distributed Web server if the cookies use IP numbers, which can create various problems. One simple solution for this is to use the hostname instead of IP numbers.

State at the server and sessions: Some Web sites use sessions, thereby effectively creating different states among the replicas. If the replicas can be expected to be actively replicated, this does not pose a problem. If not, a simple solution is to assure that a single replica is used throughout a session.

## 8. Experiments

In this section, we will present performance results. We conducted three series of experiments to test how WebSeAl 1 takes advantage of geographicŽ . proximity, 2 dynamically adapts to performance Ž . changes, 3 accommodates changes in the serverŽ . pool, and 4 enforces a target load distribution overŽ . a server pool.

## 8.1. Minimizing end-to-end delays

The first experiment consisted of two tests. We used ten mirror sites of a popular software archive that repeatedly appears in Ref. 20 as one of the <sup>w</sup> <sup>x</sup> most accessed Web sites. These tests were conducted under real world conditions, using standard machines, networks, and software. The ten servers were located on six continents: two each in North America, South America, Europe, and Asia, and one each in Africa and Australia. The client was running at New York University. Geographically, the closest server to the client was located in Massachusetts, the second closest in California.

The client running five threads generated 1000 requests for a file of length 4253 bytes. All requests were addressed to a single logical address. A local client agent intercepted each request and provided transparent access to a distributed Web site. Since we experimented with existing Web sites not running WebSeAl’s server agent, we added the server addresses manually into the cache of the client. Also, since the servers did not provide the client agent with a service weight factor, the client agent used Eq. 1 to route requests the constant Ž k was set to 4.0 . The clients’ only goal was to minimize its own . delay, independent of the resulting load distribution at the server side.

The first test consisted of two parts: one using WebSeAl’s client agent and one contacting the closest server directly. Using the client agent, the total response time for 1000 requests was 291.6 s. The response time measured is the end-to-end delay, which includes connection establishment, network delay, and server time. 95.4% of the requests were serviced by the closest server. The total response time for contacting the closest server directly was 266.9 s. This translates to an overhead of 9.2%. The fact that the WebSeAl client agent sent the vast majority of the requests to the closest server indicates that this server was delivering the best performance. Besides the computational and communication overhead of the client agent, an important factor contributing to this overhead is that 4.6% of the requests were routed to slower servers to update performance data for these machines. As mentioned before, this could be avoided by occasionally sending probes at the cost of generating additional traffic.

In the second test, we used the same setup as above, but ran the test at a different time of the day. This time, only 3.9% of the requests were serviced by the closest site. The total response time was 761.4 s as opposed to 1295.3 s when contacting the closest host directly — an improvement of 41.2%. These two tests indicate that WebSeAl can deliver significant performance gains while imposing only little overhead, compared to the scenario when the user is able to always pick the fastest machine.

![](/api/attachments/NEVKRV9Y/fulltext/images/5542f3d80bc0fe2a2efae583921fa401541c3426930b94eaab723a2ab6fb93f4.jpg)  
Fig. 7. Request distribution in a dynamically changing environment.

## 8.2. Dynamic performance changes

The second experiment investigates how Web-SeAl client agents adapt to dynamic performance changes of individual servers. The setup was the same as in the previous experiment. As with the previous experiment, the client, using a local client agent, generated 1000 requests to a logical address. After 300 requests, we started downloading several large files from the fastest site, which happened to be the geographically closest one, thus generating additional load at that server. This traffic was discontinued after another 300 requests see Fig. 7 . Of theŽ . first 300 requests, 93.3% were serviced by the closest server. This percentage sank to 11.6% for the next 300 requests, and went up again to 93.2% for the last 400 requests. The second closest server received initially 2.0% of the requests, which increased to 69.3% when the performance of the closest server started to degrade. This indicates that WebSeAl adapts well to performance changes in the server pool.

![](/api/attachments/NEVKRV9Y/fulltext/images/542dc53f46db2d5c3464c303006547f32d957904ba01fe32630e7f2beeedb5e3.jpg)  
Fig. 8. Price and load changes with $\theta = 0 . 2 5 / f ^ { \ast }$

![](/api/attachments/NEVKRV9Y/fulltext/images/63aca89a5d41f986d280410d93a0225900d436f15661c530f04f23617dc3ef79.jpg)  
Fig. 9. Price and load changes with $\theta = 0 . 5 / f ^ { \ast }$

## 8.3. Changes in serÕer pool

For the third experiment, several identical machines in a controlled environment were used to show how WebSeAl reacts to changes in the server pool. On each of four machines, a WebSeAl server agent and a standard HTTP server were started. We first used three servers, added another one after about 300 requests, and removed one of the original three servers after another 400 requests.<sup>7</sup> Since we used identical machines, it can be expected that the two fully available machines would each get 300 requests, the other two each 200 requests. The actual distribution was 295 and 286 requests for the first two machines, and 225 and 194 requests for the other two. This illustrates that WebSeAl quickly and effectively accommodates changes in the server pool.

## 8.4. Enforcing a target load distribution

For the last experiment, we used four identical machines in a controlled environment to show how

![](/api/attachments/NEVKRV9Y/fulltext/images/75d47c62c1e34df2dc1db17b681bf046afc46e0d162a7b3061fa0aa5da3a3110.jpg)  
Fig. 10. Price and load changes with $\theta = 1 . 0 / f ^ { \ast }$

WebSeAl enforces a desired load distribution. Two clients were used, each with a local client agent, and two servers with a local server agent. On a fifth machine, we ran the pricing manager, which contacted server agents and updated weight factors every second. Each client generated 500 requests each, for a total of 1000 requests. We started with a target load distribution of 0.5 and 0.5 for the two servers, expecting to distribute the total load evenly. After about 500 requests, we changed the target load distribution to 0.8 and 0.2, expecting to have 80% of the requests routed to one server and the rest to the other one. We ran five tests with varying from $0 . 5 / f ^ { \ast }$ to $4 . 0 / f ^ { * }$ . Figs. 8–12, show the weight factors and the measured load for each server.

As was to be expected, low values for  result in slow changes to weight factors, leading to slow changes in the measured load. By increasing , we can reach a desired distribution faster. However, too high a value for  results in oscillating prices and load, which is not desirable. More importantly, for the algorithm to converge, must be ‘‘sufficiently’’ small 14 .<sup>w</sup> <sup>x</sup>

![](/api/attachments/NEVKRV9Y/fulltext/images/bd0ff60cc73b914d0726770e305f71ddf2714d670061aadd0757b72dd0615636.jpg)  
Fig. 11. Price and load changes with $\theta = 2 . 0 / f ^ { * }$

![](/api/attachments/NEVKRV9Y/fulltext/images/7accf098140951c3a62122625614cf3f0f7339c241688bce0cc49bb80ce3ee22.jpg)  
Fig. 12. Price and load changes with $\theta = 4 . 0 / f ^ { \ast }$

## 9. Conclusions

WebSeAl is a novel architecture for managing resources of Web sites consisting of a pool of geographically dispersed, replicated servers. Unlike most existing proposals, in WebSeAl, it is the responsibility of the clients to route their requests to individual servers. This architecture supports geographic distribution, scales well with the number of users, and provides fault masking.

We proposed routing strategies for directing client requests to the most responsive servers. Unlike server-side approaches, routing decisions are based not only on server load, but also on network traffic conditions. We also proposed strategies that can be used at the server side to induce efficient allocation of resources load balancing while clients make Ž . their routing decisions in a noncooperative manner. Motivated by recent studies on game-theoretic aspects of networking, we proposed a pricing mechanism that provides incentives to the clients to route their requests in a way that is deemed efficient by the service provider.

We have implemented a prototype system based on this architecture and have validated its functionality through a series of experiments. These results indicate that WebSeAl can deliver significant performance gains while imposing minimal overhead.

## Acknowledgements

Equipment for this research was sponsored in part by the Defense Advanced Research Projects Agency and Rome Laboratory, Air Force Material Command, USAF, under agreement number F30602-96- 1-0320; by the National Science Foundation under grant number CCR-94-11590; and by Intel. The US government is authorized to reproduce and distribute reprints for Governmental purposes notwithstanding any copyright annotation thereon. The views and conclusions contained herein are those of the authors and should not be interpreted as necessarily representing the official policies or endorsements, either expressed or implied, of the Defense Advanced Research Projects Agency, Rome Laboratory, or the US government.

## References

<sup>w</sup> <sup>x</sup> 1 D. Andresen, T. Yang, V. Holmedahl, O.H. Ibarra, SWEB: towards a scalable World Wide Web server on multicomputers, in: Proceedings of the 10th International Parallel Processing Symposium IPPS ’96 , IEEE Computer Society Press. Ž .

<sup>w</sup> <sup>x</sup> 2 T. Berners-Lee, R. Fielding, H. Nielsen, RFC 1945: Hypertext Transfer Protocol-HTTP<sup>r</sup>1.0, May 1996.

<sup>w</sup> <sup>x</sup> 3 T. Brisco, RFC 1794: DNS Support for Load Balancing, April 1995.

<sup>w</sup> <sup>x</sup> 4 K.C. Claffy, H.W. Braun, G.C. Polyzos, Tracking long-term growth of the NSFNET, Communications of the ACM 37 8Ž . Ž . 1994 34–45, August.

<sup>w</sup> <sup>x</sup> 5 IBM, Interactive Network Dispatcher User’s Guide,1997. http: <sup>r</sup> <sup>r</sup> www.ics.raleigh.ibm.com <sup>r</sup> netdispatch <sup>r</sup> nd2mst. HTM.

<sup>w</sup> <sup>x</sup> 6 O.P. Damani, P.E. Chung, Y. Huang, C. Kintala, Y.M. Wang, One-IP: techniques for hosting a service on a cluster of machines, in: Proceedings of the Sixth International World Wide Web Conference, Santa Clara, CA, April, 1997.

<sup>w</sup> <sup>x</sup> 7 D. Dias, W. Kish, R. Mukherjee, R. Tewari, A scalable and highly available server. Digest of Papers, in: COMPCON ’96. Technologies for the Information Superhighway, Santa Clara, CA, February, IEEE Computer Society Press, 1996, pp. 68–74.

<sup>w</sup> <sup>x</sup> 8 Z. Fei, S. Bhattacharjee, E.W. Zegura, M.H. Ammar, A novel server selection technique for improving the response time of a replicated service, in: Proceedings of the IEEE INFOCOMM, March–April, 1998.

<sup>w</sup> <sup>x</sup> 9 J.H. Howard, M.L. Kazar, S.G. Menees, D.A. Nichols, M. Satyanarayanan, R.N. Sidebotham, M.J. West, Scale and performance in a distributed file system, ACM Transactions on Computer Systems 6 1 1988 51–81, February.Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 Matrix Information and Directory Services, MIDS Internet

Weather Report. Available at http:<sup>rr</sup>www3.mids.org<sup>r</sup> weather.

<sup>w</sup> <sup>x</sup> 11 E.D. Katz, M. Butler, R. McGrath, A scalable HTTP server: the NCSA prototype, Computer Networks and ISDN Systems 27 2 1994 155–164.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 Y.A. Korilis, A.A. Lazar, A. Orda, Architecting noncooperative networks, IEEE Journal on Selected Areas in Communications 13 7 1995 1241–1251, September.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 Y.A. Korilis, T.A. Varvarigou, S.R. Ahuja, Optimal pricing strategies in noncooperative networks, in: Proceedings of the 5th International Conference on Telecommunication Systems: Modeling and Analysis, Nashville, TN, March, 1997, pp. 110–123.

<sup>w</sup> <sup>x</sup> 14 Y.A. Korilis, T.A. Varvarigou, S.R. Ahuja, Incentive-compatible network pricing, in: Proceedings of the IEEE INFO-COMM, March–April, 1998.

<sup>w</sup> <sup>x</sup> 15 Y.A. Korilis, T.A. Varvarigou, G.A. Efthivoulidis, S.R. Ahuja, Pricing techniques for distributed resource management in an intranet, in: Proceedings of Third IEEE Symposium on Computers and Communications, June–July, 1998.

<sup>w</sup> <sup>x</sup> 16 http:<sup>rr</sup>www.ncsa.uiuc.edu.

<sup>w</sup> <sup>x</sup> 17 http:<sup>rr</sup>www.netscape.com.

<sup>w</sup> <sup>x</sup>18 A. Orda, R. Rom, N. Shimkin, Competitive routing in multiuser communication networks, IEEE<sup>r</sup>ACM Transactions on Networking 1 5 1993 510–521, October.Ž . Ž .

<sup>w</sup> <sup>x</sup>19 A. Siegal, K. Birman, K. Marzullo, Deceit: a flexible distributed file system, in: Proceedings of the 1990 Summer USENIX Conference, Anaheim, CA, June, 1990.

<sup>w</sup> <sup>x</sup> 20 http:<sup>rr</sup>www.top100.com.

<sup>w</sup> <sup>x</sup> 21 http:<sup>rr</sup>www.tucows.com.

<sup>w</sup> <sup>x</sup> 22 C. Yoshikawa, B. Chun, P. Eastham, A. Vahdat, T. Anderson, D. Culler, Using smart clients to build scalable services, in: Proceedings of the 1997 USENIX Annual Technical Conference, Anaheim, CA, January, USENIX, 1997, pp. 105–117.

Mehmet Karaul was born in Turkey in 1964. He received his Diploma in Computer Science from the University of Bremen, Germany, in 1991, and his MSc and PhD in Computer Science from New York University, New York, in 1995 and 1998, respectively. He joined the Research Staff at Bell Laboratories in 1998 as a member of the Networking Techniques Research Department. His research interests include distributed computing with focus on load balancing, fault tolerance and scalability issues, resource allocation, and networking.

Yannis A. Korilis was born in Thessaloniki, Greece, in 1966. He received the Diploma from the National Technical University of Athens, Greece, in 1989, and the MSc, M. Phil., and PhD degrees in Electrical Engineering from Columbia University, New York, in 1990, 1992 and 1995, respectively. Since 1995, he has been a Member of the Technical Staff at Bell Laboratories, Lucent Technologies, Holmdel, NJ. He has held adjunct Assistant Professor positions at Columbia University and New York University. His research interests include network control and management, network pricing, economic and game theoretic models for networking and distributed algorithms.

Ariel Orda was born in Argentina in 1961. He received the BSc Ž . Summa Cum Laude , MSc and DSc degrees in Electrical Engineering from the Technion - Israel Institute of Technology, Haifa, Israel, in 1983, 1985 and 1991, respectively. From 1983 to 1985 he was a Teaching Assistant at the Technion. From 1985 to 1990, he served in the IDF as a Research Engineer. From 1990 to 1991, he was a Teaching Instructor at the Technion. In 1991, he joined the Faculty of Electrical Engineering at the Technion, as a Lecturer. During the academic year 1993–1994, he was a Visiting Scientist with the Center for Telecommunications Research, Columbia University, New York, NY. Since 1994, he has been a Senior Lecturer at the Technion. During 1991–1997, he held consulting positions in Bell Laboratories and in the Israeli industry. During the summers of 1995, 1996 and 1998, he was an Academic Visitor at IBM T.J. Watson Research Center. His current research interests include the control and management of broadband networks, the application of game theory to computer networking, QoS routing, and on-line network algorithms.
