---
otero_id: 21820
otero_key: "P82FHF9R"
title: "Experiments in designing computational economies for mobile users"
authors: "Tracy Mullen; Jack Breese"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00072-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Experiments in designing computational economies for mobile users

Tracy Mullen <sup>a,),1</sup>, Jack Breese <sup>b,2</sup>

<sup>a</sup> Telcordia Technologies, 445 South Street, Morristown, NJ 07960-6438, USA b Microsoft Research, Redmond, WA 98052-6399, USA

## Abstract

Distributed operating systems provide users with transparent access to network-wide resources. As changes occur to network resources, or as user locations and preferences evolve, the system must be able to adapt by reallocating, replicating, or moving its resources. We explore a market-based approach to resource allocation in such environments, and describe initial experiments in designing and building computational markets for distributed operating system resources. We focus on the problem of redistributing network file allocations for a mobile user population in order to improve locality and accessibility. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Computational economies; Distributed resource allocation; Market-based design; Multi-agent systems

## 1. Introduction

As computing becomes more ubiquitous, distributed operating systems must deal with a user population that is increasingly distributed and mobile. Hiding the complexity of such a computing environment from the user requires the operating system to support more location-transparent, adaptable, and self-tuning services 3 .<sup>w</sup> <sup>x</sup>

In this paper, we examine a market-based approach in allocating network-wide files to a mobile user population based on locality and accessibility.

Since a market price system is essentially solving a distributed optimization problem for multiple resource allocation, it provides a natural framework for addressing resource allocation in a distributed computing framework. Through markets, local information about user preferences and resource scarcity are summarized and communicated globally in the form of prices. This information is valuable not only to agents for evaluating tradeoffs between resources, but also useful to the operating system from a more global perspective for self-tuning.

Our eventual goal is the development of computational market systems for allocating resources within distributed operating systems. A computational market system is an infrastructure that implements a computational economy. Economic systems, whether computational or not, are composed from a set of mechanisms and institutions for decision making as well as laws, rules, and overall organizational policy governing their implementation 10,16 . A computa- <sup>w</sup> <sup>x</sup> tional market system must deploy, monitor, and adapt computational markets and institutions on an asneeded basis and in accordance with system policy. Developing computational market systems for the distributed operating systems realm has many promising applications, but it has also many challenges. In this paper, we content ourselves with a few exploratory case studies focusing on the potential value and uses of such systems.

## 1.1. Problem description

Computer users are becoming increasingly mobile. So-called road-warriors travel to remote sites for hours, days, or months at a time. Workers are transferred to new departments, contractors relocate for temporary projects, and telecommuting from home is becoming increasingly common. With wireless connectivity, both users and network nodes can change location dynamically, thus, changing the network topology itself.

As users relocate to different points in a distributed network, file access latency to centrally stored resources such as electronic mail and other intranet databases will vary from one location to another depending on network conditions and configuration. Most current network file management protocols and applications do not support migration of files based on user locality. Location may be keyed to a person’s permanent office or PC location, or may be based on the location at time of setup. As users move to different locations on the local- or wide-area network, service times can vary drastically.

In this paper, we examine the case of a set of mobile users accessing a set of geographically disperse network file servers. Users are allocated file space on one or more of the file servers. As users migrate across the system, their access latency will change depending on network configuration. In these experiments, mobile users have preferences over file access latency vs. amount of file storage space. Users with low tolerance for delay will generally be willing to trade off disk space for faster access. Users also have similar preferences based on the types of tasks requiring these files. Thus, for archived files, access latency may not be important, while for e-mail files, it is somewhat important, and for frequently used files, very important.

## 1.2. Related work

There is an increasing interest in the use of markets for allocating network resources, as exemplified by the volume of material on sites providing collections of papers and projects on information and network economics 6,17,31 . While these ap- <sup>w</sup> <sup>x</sup> proaches share an interest in using economic mechanisms for allocating resources, they vary widely otherwise. We consider two features, among many, to generally classify our approach.

One distinguishing feature is the resource allocation problem being addressed. Is there a single resource to allocate, or are there multiple interrelated resources? Many market or market-like mechanisms for allocating computational resources of various kinds in a distributed computing environment <sup>w</sup> <sup>x</sup> 7,11,13,33 are centered about a global model for the resource, from which each agent or module calculates the marginal value of resource for itself. By using this value for bidding, the market allocates goods efficiently according to marginal value. More recent works on bandwidth allocation for various network or multimedia quality-of-service QoS re-Ž . quirements consider different kinds of pricing policies and problems involving dynamic resource allocation 19,25,29 .<sup>w</sup> <sup>x</sup>

In contrast to these applications, a distributed operating system environment is concerned with finding an allocation for multiple interrelated resources. In other words, each agent is potentially interested in combinations or bundles of goods re-Ž sources, services , rather than a single type. General. equilibrium theory provides a formal model for allocation of multiple interrelated resources under classical conditions such as gross substitutability, continuous goods, and complete markets. Market-oriented programming 35 implements a distributed computa- <sup>w</sup> <sup>x</sup> tional economy as an instance of a general equilibrium system, and finds its competitive equilibrium. Our approach in these experiments was derived from market-oriented programming. Since there are restrictive conditions on guaranteed general equilibrium convergence, as well as associated time delays required for convergence, these systems generally need modification when applied to more real-time, dynamic, and discrete applications 5,15,34 . Multi-<sup>w</sup> <sup>x</sup> object auctions can also be used for the simultaneous sale of many resources, such as the one used by the FCC 21 . Combinatorial auctions allow bidders to<sup>w</sup> <sup>x</sup> bid on combinations of resources, but establishing auction properties and making them computationally tractable is an area of current research 1,27,37 .<sup>w</sup> <sup>x</sup>

A second distinguishing feature of market-based approaches is the design problem being addressed. Is the focus on a single system component, such as auctions 32 , or is it on the overall system architec- <sup>w</sup> <sup>x</sup> ture and supporting middleware 14,24 ? When designing a component, mechanism design and game theory 4,26 provide useful formal tools. However,<sup>w</sup> <sup>x</sup> as systems scale up, and the available resources or services within the system change over time, the ability to support an extensible and flexible set of mechanisms through a computational market system becomes increasingly important. Other types of computational and information networks where these kinds of infrastructural or middleware approaches have been used include digital libraries 2,8 , busi-<sup>w</sup> <sup>x</sup> ness process management 12 , and distributed<sup>w</sup> <sup>x</sup> databases 30 .<sup>w</sup> <sup>x</sup>

## 1.3. Performance criteria

Generally, operating system performance is measured in terms of network efficiency, which involves achieving target levels of service for all users or minimizing required resources. Since users often have diverse and conflicting performance criteria, it can be difficult to define a meaningful system-wide performance goal in terms of network efficiency. Using market-based methods, we can allocate disk space based both on user preferences as well as on current system constraints — optimizing economic 18 , <sup>w</sup> <sup>x</sup> rather than network, efficiency. By incorporating end-user preferences, users may get higher perceived value or utility as a result of a system’s awareness of individual application needs.

Incorporation of user- and application-specific preferences has useful implications for system design. It means that the system can reallocate resources flexibily and dynamically in response to a diverse and potentially changing user population. For example, if one user prefers having more disk space even if it means having slower access latency, while another user prefers faster access latency even if it means having less disk space, it will be hard to find a system-wide performance criteria that satisfies both users. Instead, if we allow the first user to acquire more of the large remote disk space while the second user acquires more of the scarce local disk space, both users may be more satisfied than if we forced them to split the remote and local disk space evenly.

While our initial experiments are based on allocating only two basic resources, the economic framework is intended for allocating multiple interrelated resources and extends to adding other operating system resources, such as signal or graphics processing, or to offering resources under different qualities of service. In such a diverse environment, finding system-wide performance criteria based on network efficiency becomes even less tenable.

## 1.4. Experiment summary

In Sections 3–5.1, we discuss our experiments in network file allocation for mobile users and show qualitative results that arise from different economic design models and assumptions. Below is a summary of the experiments listed according to the design criteria being considered.

## 1.4.1. Support diÕersity of users and tasks

In Sections 3.1–3.3, we consider how different parameters, such as utility parameters and initial endowments, can affect the final allocation. These potentially provide the operating system, or system manager, with tunable parameters for different kinds of policy-level decisions. For example, by changing the initial endowment, the operating system manager can provide some users with a greater share of system resources than others. However, evaluating the tradeoff among resources still rests with the user.

## 1.4.2. Adaptability

In Section 3.4, we consider how price can be used by the operating system to suggest when to replicate resources. By modeling the replication technology, the system can reason about how much should be acquired. In Section 4.1, we consider how the user population’s utility parameter affect the gain users get from dynamic reallocation. This kind of information could potentially be used to provide the system with feedback on how often it should reallocate resources.

## 1.4.3. Market Õs. non-market dynamic reallocation

In Section 4.2, we compare dynamic market reallocation of disk space with that of a non-market heuristic reallocation rule. Given a static and known user population, a simple heuristic rule can achieve the same optimal allocation as the market, without the overhead involved in running the market. However, when the population changes, the market mechanism still finds the optimal allocation while the heuristic rule does not — suggesting that the market approach has the potential to be more flexible and adaptable.

## 1.4.4. Scalability

In Section 5.1, we consider the use of brokers, or information consolidators, which can both simplify the economic setup and reduce the market overhead as the number of resources and<sup>r</sup>or agents in the system are increased.

In Section 2, we describe the computational economy configuration used in our experiments.

## 2. Designing the mobile user economy

To model the mobile user file allocation problem as a computational economy, we must first make explicit both the goods to be exchanged and the participating agents. We also need to specify the market mechanisms, or auctions. Below, we describe these various steps in designing the mobile user economy.

## 2.1. Resources

Computational resources are the goods of a computational economy. Defining the available goods effectively circumscribes the design space. Our first task in designing any economy is determining what resources, or goods, will be produced and consumed.

In the mobile user economy, the resources are the available disk space across the network. To determine what system resources are available, we first need to establish the layout of the underlying network topology. In our case, we defined a simplified distributed network configuration based on the one shown in Fig. 1. The network configuration in Fig. 1 has three servers, each with local disk space. Colocated with each server are multiple clients. These clients have access to the entire network, but only through their local server. We refer to this combination of server, clients, and disk space as a site.

The bottom of Fig. 1 shows the abstract network connections for this configuration. The loop from each site to itself represents the fact that any client at a site can access the disk at that site via the local area network. The numbers on each link in the network represent the average access latency across that link.

For our experiments, we used the 10-site network shown in Fig. 2. Each link between sites has an average latency of 2 s<sup>r</sup>MB, while each site’s local network has an average latency of 1 s<sup>r</sup>MB. Thus, latencies between sites are twice the latency within a site.

Since disk location correlates to file access speed, users need to be able to distinguish between different disk locations. In the mobile user economy, we define disk space on the different sites to be separate goods e.g., diskspace@site0 or diskspace@site9 . InŽ . Section 5.1, we discuss how this model could be modified so users could define their preferences in terms of disk space and access latency only.

Another important characteristic is time — most resources are actually goods over some time period. Thus, the amount of disk-space must be quantified by saying over what time period it is available for — is it per hour, per day, per year? However, if the entire model operates over the same time period, it may not be necessary to explicitly put in the time period. In our case, we assume that all disk space is sold on a per-day time period.

![](/api/attachments/P82FHF9R/fulltext/images/aeeeb641373b2489c7ad940029bee304b542af1e4067bdb7d1e78f51d8cd7654.jpg)  
Fig. 1. A simple network configuration.

![](/api/attachments/P82FHF9R/fulltext/images/6fd5c111a7812079b0d3b98ba59f989edde9dee78117b101848d87bef663d801.jpg)  
Fig. 2. Network configuration for experiments.

A related question, which impacts on the choice of market mechanisms and the quality of the allocations, is whether the goods are continuous or discrete. In other words, can disk space be sold as 1.234 MB or is it only available in 1-MB blocks? Classical general equilibrium systems, mentioned in Section 1.2, assume that goods are continuous. With discrete goods, Pareto optimality or even equilibrium is no longer guaranteed. Therefore, to simplify our economic setup for these initial case studies, we choose to consider all our resources as being continuous.

## 2.2. Agents: producers and consumers

## 2.2.1. Producers

Producer agents are associated with a technology, which specifies an ability to transform some goods into other goods. The sole objective of producers is to choose an activity within their technology so as to maximize profits. Since we are assuming a competitive economy, where agents act as price-takers, this amounts to supplying their goods at marginal cost.

We investigated two different types of producers, fixed capacity and variable capacity, depending on the kind of transformations we wanted to model. The fixed capacity disk storage producer has a fixed amount of disk storage space to sell. For this technology, we assume that there are no incremental costs associated with heavier disk usage, so the producer marginal cost is US\$0. Under this assumption, if there is more disk space available than consumers need, they will be charged US\$0. It is only when disk space is scarce relative to consumer needs that the consumers will have to pay anything. This cost reflects the opportunity cost involved in using that disk space for one consumer’s work over another’s.

The variable capacity producer actually produces disk space with decreasing returns to scale technology. That is, the cost of incremental disk space is higher than that of existing capacity. This production technology reflects not only the cost to the system of buying new disk space but also the congestion associated with increased disk space. However, our main point was not capturing this system cost accurately, but showing how to use this configuration to ask hypothetical questions about when and where to provide additional disk space.

## 2.2.2. Consumers

Consumer agents are endowed with an initial quantity of goods or money and engage in trades so as to maximize their utility subject to their budget constraint. Consumers in this model represent the end-users of the distributed operating system. Consumers’ behavior depends on both their utility functions and their initial endowments. For example, given the same endowment, each user may consume different resources depending on its personal preferences. Additionally, the same user may choose different resources given different endowments or prices. By changing initial endowments, users can be given larger or smaller shares in the system wealth. Users’ endowments can be in the form of some kind of system or real currency or might consist of Ž . owning computational resources, such as disk space or CPU on their own computer, and selling them to buy other resources.

For our experiments, a given user at a site is potentially interested in network-wide disk space given its access latency, and current prices for disk space. We considered three types of users, or diskspace consumers. The first type uses files requiring rapid-access and has twice the income of the other two consumers. This user might represent a technical user who requires more computing power. The second type also uses rapid-access files, but with a lower income. We intended the lower income to reflect a lower system priority for this user. The third type values file space for archiving files over rapidaccess, and also has a lower income than the first type. We assumed that users were willing to spread their storage allocations across different disks orŽ more realistically, that the system could support this kind of file distribution ..

The user’s utility function determines how the user makes the tradeoff between disk space at the different sites. For these experiments, we used a constant elasticity of substitution CES utility func-Ž . tion, defined as follows:

$$
U \left(x _ {\mathrm{ds} 0}, \dots , x _ {\mathrm{ds} 9}\right) = \left(\sum_ {i = 0} ^ {9} \alpha_ {\mathrm{ds} i} ^ {1 - \rho} x _ {\mathrm{ds} i} ^ {\rho}\right) ^ {1 / \rho}.
$$

This utility function defines the substitutability of disk spaces at various sites and weighs them according to their access latency. $x _ { \mathrm { d s } i }$ refers to the quantity of disk space acquired at site i.

There are two tunable parameters, and $\rho .$ The coefficients $\alpha _ { \mathrm { d s } i }$ weigh the consumer’s preference for disk space from each site i. To weigh faster access disk space more, we set $\alpha _ { \mathrm { d s } i }$ to be a function of the access latency from site i, namely 1<sup>r</sup>access<sub>–</sub> latency<sup>10</sup>. The weighing factor 10 was simply chosen to highlight the differences in demands between rapid-access and archival users. The $\rho$ parameter indicates the substitutability between disk space at from different sites. Obviously, disk space at one site can always be substituted for disk space at another connected site. Exactly how substitutable depends on both consumer preference and type of file access. Thus, an archived $\mathrm { f i l e } ' \mathrm { s }$ location is quite substitutable. However, for rapid-access files, location becomes more important and disk space is less substitutable. We modeled this behavior by choosing $\rho =$ 0.99 for consumer archiving and $\rho = 0 . 0 1$ for rapidaccess whereŽ $\rho = 1$ is perfect substitutability and $\rho < 0$ for complementary goods ..

## 2.3. Auctions and market infrastructure

One of our aims was to provide a testbed environment to explore the effect of different kinds of auctions, agents, and market configurations on resource allocation within a distributed operating system environment. To this end, auctions were built as processes within a prototype distributed operating system. Building auctions within the simulator environment enables future work on markets that make use of system data, on measuring market overhead and performance, and on comparing market with non-market systems using real system traces.

Auctions are simply a set of rules for determining a price and<sup>r</sup>or allocation based on a bidding protocol 20 and provide a very flexible market framework — different auction types can have a large effect on the resultant resource allocation properties. Information about the different auction rules and protocols can be captured in a compact, reusable manner through the use of parameterized auction components 23,38 , where auction parameters can<sup>w</sup> <sup>x</sup> be tuned to reflect the type of good being sold, timing requirements or mechanism properties desired. For example, disk space might be sold differently depending on how it is bundled $\left( \mathrm { e . g . } \right.$ , per hour, per day , characteristics size, reliability , or to whom . Ž . it is sold individual, project . Some auction parame-Ž . ters include auction clearing rate e.g., once a day or Ž every 5 min with each new bid , price setting rules. Ž . e.g., first price, second price, zero-excess demand , and whether the resources are divisible or not.

Making these parameters explicit, along with formalizing the bidding interaction protocol, provides a basis for simplifying and automating both the auction creation and agent interaction process. It also provides a basis for reasoning about what kinds of auctions to create for different types of goods and<sup>r</sup>or desired allocation properties. As operating system conditions change, the system itself can apply this knowledge, changing auction parameters appropriately.

For example, for a single auction, there is a tradeoff between the market clearing rate and the allocative efficiency of the result. An efficient allocation occurs when all bids have arrived and the auction sets the price where supply equals demand. However, agents may face a long delay until the resource gets allocated — for some kinds of resources, this may not be important, while for others, it may be critical. On the other hand, in a continuous double auction 9 , bids clear as soon as a match is <sup>w</sup> <sup>x</sup> found. Agents face minimal delay but potentially non-efficient allocations. Intermediate market clearing rates provide different tradeoff points between agent non-delay vs. allocation efficiency. As the number of bidders increases or decreases at the auction, these tradeoff points will change. The operating system may want to adjust the auction clearing rates accordingly.

![](/api/attachments/P82FHF9R/fulltext/images/922c9cadca87a22572d0677a8f6bbbef5903a1a9252976639ba8853a7ad08a79.jpg)  
Fig. 3. Mobile user economy configuration.

We designed the computational economy based on the market-oriented programming approach mentioned in Section 1.2. All resources are sold with continuous units, agents behave competitively i.e.,Ž as price-takers , and auctions set prices at zero-ex- . cess demand i.e., supply equals demand . Each auc-Ž . tion clears whenever a new bid arrives and the system runs until it reaches equilibrium prices — the set of prices under which supply and demand are balanced for all the resources. Although running auctions until they reach equilibrium would not be realistic for many real-time resource allocation situations, we assumed that disk space was allocated on a per-day basis so that market overhead was not an issue.

Section 2.4 describes our original market configuration, which was used in the different experimental setups in Sections 3 and 4.

## 2.4. Mobile user economy configuration

Fig. 3 shows the mobile user economy configuration for the experiments in Sections 3 and 4. For simplicity, only the producers, consumers, and auctions for the first three sites are shown. A producer at site i can sell its disk space through its respective auction for disk space at site i. Consumers at any network site can bid on this disk space. The arrows represent the eventual flow of goods from producers to consumers, where auctions set the price and allocations for agents.

In the first set of scenarios in Section 3, the disk producer agents at all sites are fixed capacity producers. They own their local disk with 1000 MB of space, which they sell<sup>r</sup>rent each day. Since the producer’s marginal cost is US\$0, it has an inelastic supply bid — it will sell any amount of disk space, up to 1000 MB, for US\$0 or more per MB per day.Ž . In the last scenario, we use variable capacity disk producers to explore a hypothetical question about how much disk space should be provided at different locations.

## 3. Experiments with a diverse user population

In these experiments, different user types tradeoff speed of file access for amount of disk space — the actual tradeoff depending on their task and<sup>r</sup>or personal preferences. There are three different types: high-income rapid-access users, low-income rapidaccess users, and low income archive users. There are a total of 30 users 10 for each of the three types Ž . located across the 10 network sites described in Section 2.1. For each scenario, we move the users and then discuss the resulting reallocation.

## 3.1. Scenario 1: all users reside at site 0

Initially, all users start out at the same site, site 0. The final disk space allocations are shown in Fig. 4. The amount of disk space allocated for each type of user is shown as a proportion of the total disk space at each site. Rapid-access users buy almost no disk space on the most remote sites sites 2, 3, 5, 6, 8,Ž and 9 , which have the largest latencies, and small.

![](/api/attachments/P82FHF9R/fulltext/images/3d787197ff71b04e533996a532886c9108b6c4a7cb43e83b82cf5e7498973c74.jpg)  
Fig. 4. Disk space allocation when all users are at site 0.

![](/api/attachments/P82FHF9R/fulltext/images/611fc271de9ed4e1bd22a17642a2a2ac319dbb8f3b554b692c6bf16d4518cf38.jpg)  
Fig. 5. Disk space prices when all users are at site 0.

amount at sites 1, 4, 7, which have slightly lower latencies. Thus, the resulting allocation has rapidaccess users with disk space on the nearer sites Ž . amount depending on income , while archival users dominate the more remote sites. Since the archival users are willing to tolerate slower access rates than the rapid-access users, they are able to acquire more disk space.

Fig. 5 shows the corresponding price per MB per day for disk space at each site. The price of disk space at site 0 is about 30 times than that at the other sites — rapid access users drive the price of disk space at site 0 up until archival users would rather buy disk space at the remote sites. Sites 1, 4, and 7 have marginally higher prices than the remaining sites since rapid access users do buy a small amount of disk space there. The congested resource is easy to spot in Fig. 5.

## 3.2. Scenario 2: uniform user distribution

In this scenario, the users have moved so as to be evenly distributed across the 10 sites. Since demand is spread evenly between disks, it is not surprising that all prices end up being the same, namely US\$0.04. Given the same price, all consumers prefer local storage space to remote storage space. Thus, the amount of disk space acquired is directly proportional to income so that the high-income users get twice the disk space of either of the other two user-types, as shown in Fig. 6.

## 3.3. Scenario 3: high-income rapid-access users concentrated

Instead of a uniform distribution, suppose all of the high-income rapid-access users e.g., technicalŽ staff are concentrated on one sub-net of the net- . work, say sites 2 and 3. The other two types are distributed across the remaining leaf sites — low-income rapid-access users at sites 5 and 8, low-income archival users at sites 6 and 9. Fig. 7 shows rapidaccess users acquiring disk space at their local sites, while archival users spread themselves among the remaining sites.

![](/api/attachments/P82FHF9R/fulltext/images/6cca7d4267dea971198cb4bac293c2e9bd4f8c9ac610f55223db88b769417daa.jpg)  
Fig. 6. Disk space allocation when users are uniformly distributed.

In Fig. 8, high prices at sites 2 and 3 reflect the high demand and willingness to pay for disk space imposed by such a distribution. Smaller price peaks, at sites 5 and 8, represent the demand for disk space at those sites from low-income rapid-access users. In Section 3.4, we consider how this information might be used as a basis for deciding if and how much disk space to acquire at those two sites.

![](/api/attachments/P82FHF9R/fulltext/images/ed8f597e6ec3a16da668cf7b7451a1b040618f9ff94c651b2fe20b26211b4e4b.jpg)  
Fig. 7. Disk space allocation with high-income rapid-access users at sites 2 and 3.

![](/api/attachments/P82FHF9R/fulltext/images/065723eaaee6b4efc0332849afbd900807d7eef73c7e6258a1149b08aee7fb4b.jpg)  
Fig. 8. Disk space prices with high-income rapid-access users at sites 2 and 3.

## 3.4. Scenario 4: Õariable capacity producer

In scenario 3, the high prices at sites 2 and 3 reflect a high willingness to pay for disk space at those sites. A self-tuning operating system might observe the high price and consider whether to recommend acquiring more disk space at a particular location, and if so, how much. Suppose that, instead of a fixed disk size, disk space could be incrementally produced or bought .Ž .

To explore this situation, we changed the disk producer’s technology from a fixed capacity, zeromarginal-cost technology to a variable capacity, decreasing returns to scale technology. In particular, we used a quadratic-cost technology for the disk space producer at sites 2 and 3. Although the quadratic cost function is not particularly realistic, it is a representative and easily illustrated decreasing returns to scale technology. The quadratic-cost disk producer accepts money as input and produces disk space where the cost of producing more disk space goes up quadratically. The producer still supplies disk space according to its marginal cost, however, its marginal cost is no longer zero. Implicit in this production technology is the additional cost required to keep access times the same across the network, in spite of having more disk space available, and therefore, more file accesses.

![](/api/attachments/P82FHF9R/fulltext/images/f417f41ab170bef4e3ddd3319a118018dd1a3e2413d43c18be07297c0e0e8b71.jpg)  
Fig. 9. Disk space allocation with variable capacity producers at sites 2 and 3.

![](/api/attachments/P82FHF9R/fulltext/images/5b09b3b87343b032dce1c312bab578cb0cfd911036b9e279a6e88707ffc54221.jpg)  
Fig. 10. Disk space prices for scenario 3 and scenario 4 compared.

Since we were not modeling any real costs or technology here, we calibrated the parameters of the production function so that a variable capacity producer could supply 1000 MB for half the price of disk space at sites 2 and 3 in scenario 3. Although this choice is somewhat arbitrary, the general idea is to consider what happens when the marginal cost of producing more disk space at sites 2 and 3 is cheaper than its current price. Comparing the final allocations in Fig. 9 to those in scenario 3, we see that sites 2 and 3 location of the high income, rapid-access Ž consumers now support 1400 MB of disk at these. sites, while the other allocations remain essentially the same.

Fig. 10 compares the final prices, given the increased disk space, to the original prices in scenario 3. The prices for disk space at sites 2 and 3 have been reduced; users are no longer willing to pay more for this disk space than the incremental cost of acquiring new disk space. This scenario suggests how price information could potentially be used as the basis for acquiring new disk space and<sup>r</sup>or determining where more disk space should be located.

## 4. Mobility experiments

Having explored the effects of having diverse types of mobile users in the previous section, we now look at the effects of mobility alone on the users’ welfare. First, we show how users’ substitutability affects the gain they receive from a dynamic reallocation and how the system might use this information. Second, we compare the market reallocation mechanism with both the original static allocation and a dynamic reallocation rule.

## 4.1. How substitutability affects reallocation Õalue

To eliminate the diversity aspect, we used 100 users all with the same endowments, and same $\rho ^ { \prime } \mathbf { s }$ and $\alpha { \mathrm { ? } } { \mathrm { s } } .$ Initially, users were distributed evenly across the network, each with a static allocation of 100 MB of local disk space. Next, we randomly moved some percentage of the population to a random location within the network and ran the economy to get a new set of disk space allocations. We then measured the utility gain or loss for each agent between its current utility and the utility of its original static allocation. This utility gain measures the benefits of pricing over fixed static allocation. Since individual-value utility gains or losses varied, we measured average utility gain per user. We found that the benefits of flexible pricing are proportional to the overall mobility of the population, as might be expected. However, the other major determinant of net gain is the degree of substitutability of the resources in the economy.

In Fig. 11, we consider how — that is, how substitutable the users consider system resources — affects the utility gain. On the x-axis, larger $\rho$ values correspond to more substitutable goods. This graph shows the effects when 50% of the population moves; however, the results for other mobility percentages have a similar curve. We see that users with less substitutability get larger utility from reallocating disk space dynamically. This kind of information might be used to gauge how often system resources need to be reallocated — presumably when mobility is less and resources are more substitutable, the system might want to reallocate resources more infrequently than when mobility is high and goods are less substitutable.

![](/api/attachments/P82FHF9R/fulltext/images/13aed3d25659094611a793e980810560f90525f8b4a580c39a90522959062b69.jpg)  
Fig. 11. Average utility gain vs. substitutability for a mobile user.

## 4.2. Comparing reallocation mechanisms

While on average, mobile users experienced a utility gain with the market reallocation of disk space above, this presumably could be demonstrated with any reasonable dynamic reallocation mechanism. In this section, we compare market reallocation to a non-market dynamic reallocation rule, which caters to rapid-access users.

We assume that the network configuration has users only at the leaf sites i.e., sites 2, 3, 5, 6, 7, andŽ 8 . Our non-market dynamic reallocation rule assigns. disk space evenly based on the following locality constraints. First, disk space on a leaf site is distributed among users at that site. Second, disk space on an internal site is distributed among users below it in the network tree. Thus, disk space at site 1 is distributed evenly among users at sites 2 and $^ { 3 , }$ while disk space at site 0 is distributed evenly among users at all the leaf sites.

Users were initially distributed uniformly among the leaf sites 96 users, 16 per site and then aŽ . percentage of the population was moved randomly to another leaf site. This rule performs as well as the market rule when all the users are rapid-access users, and without the overhead incurred by using the market mechanism. Both, not surprisingly, outperformed the original static allocation.

However, when the user population consists of half rapid-access users and half archival users, the market reallocation has higher utility gains than the non-market one. In Fig. 12, we show the results when the user population is split evenly between rapid-access and archival users. Initially, users were distributed evenly among the leaf sites. We then randomly moved different percentages of the user population and compared the market and non-market reallocations.

As the users move, the average utility achieved with no reallocation is used as the baseline, and considered as having zero utility gain in Fig. 12. Average utility gains for the two dynamic reallocation methods are always measured relative to those of the static allocation. We do not currently know if the non-linearity around 50% mobile has any significance, or is just an artifact of the particular network configuration or user population distribution. Elsewhere, the benefits of both market and non-market reallocations are linear with respect to the mobility of the population. However, the non-market allocation does noticeably worse than the market one with a more diverse population than the one it was designed for.

![](/api/attachments/P82FHF9R/fulltext/images/4629e6683c88480e721317d1ffd3fad783d51f6f846baf27166500d0a8b134e3.jpg)  
Fig. 12. Dynamic reallocation: market vs. non-market.

We recognize that this is a very simple non-market reallocation rule, and more sophisticated and adaptive rules could conceivably give better results. However, while a market allocation is not necessarily going to be better than a non-market one for a fixed scenario, we would argue that it is much more flexible and scalable — because it incorporates user preferences in a principled way, the benefit of the economic solution is its ability to dynamically respond to changes in the user population. Presumably, the more dynamic and large scale the environment, the harder it will be to find a good adaptive reallocation rule. A natural extension of this work is to compare currently used reallocation mechanisms to market ones, not only the allocative efficiency but also how much overhead each approach adds. All of these issues and more remain open for future inves-Ž . tigations.

## 5. Market design considerations

## 5.1. Scalability: brokers

Although the economic model in the previous sections displays reasonable qualitative behavior, it has two disadvantages. First, every consumer has to interact with every auction. Second, every consumer has to know about the access latency between their local site and all others in the network. Both of these factors make it hard to scale up the design for large-scale networks. In this section, we consider how the use of brokers, mediator agents who buy and sell goods on behalf of other agents, helps consolidate some of the access latency information requirements and also hide the complexity of the system from the users.

Brokers, as shown in Fig. 13, reduce the network monitoring costs of gathering information about average access latency by each individual agent. Having a broker gather this information once per site reduces system overhead and application complexity. Suppose that there are $n _ { \mathrm { a } }$ agents and $n _ { \mathrm { s } }$ sites, and assuming that it costs two messages to actively measure network latencies to any site, then it will cost $2 n _ { \mathrm { s } } n _ { \mathrm { a } }$ messages for all the agents to individually acquire this information. However, assuming the typical case where $n _ { \mathrm { a } } \gg n _ { \mathrm { s } }$ , then by using brokers, it will only cost $2 n _ { \mathrm { s } } ^ { 2 }$ messages. In the worst case, where $n _ { \mathrm { s } } \gg n _ { \mathrm { a } } ,$ it will never cost more than not having brokers, since brokers will only exist on sites with agents. Brokers might also passively monitor and measure the latency of bidding or other traffic, potentially reducing the extra network traffic to zero. Another transaction cost improvement includes consolidating bids from a given site to both reduce network traffic and cut down on auction processing time since it only has to handle one bid instead ofŽ n.. Finally, auctions themselves could be optimized for particular utility or bidding forms 39 .<sup>w</sup> <sup>x</sup>

Brokers can also help reduce agent-decision complexity costs. Since many applications will tend to have stereotypical values, a broker can provide different quality of service mappings 28 per applica-<sup>w</sup> <sup>x</sup> tion. For example, if e-mail is classified as a rapidaccess application, then its $\rho$ parameter could be automatically set to 0.01 unless overridden.

![](/api/attachments/P82FHF9R/fulltext/images/57526f531bbbae2bc83cda8e8cd1147c3c60533a16bd019c87c84ee289e30891.jpg)  
Fig. 13. Mobile user economy with brokers mediating information flow for auctions.

Finally, application and system constraints regarding minimum disk space size can be monitored and enforced by the broker. The broker may also be designed to provide additional value-added processing by using historical information about access latency or predictive rates. Designing the broker in this manner does not effect the final resource allocation of the system. However, modularizing the networkaware software into the broker can reduce transaction and agent-decision costs, as well as provide enforcement of system policies or other value-added local information services.

## 5.2. Future work

## 5.2.1. Simplify agent good space

If the economy was extended to consider network transportation as an explicit good, then brokers could be used to simplify the user’s decision about where to acquire disk space. Instead of users having to specify their preferences for storage at every disk site, brokers would allow them to define their preferences in terms of access latency and disk space only. We describe below how a broker could replicate a user’s utility function once per available disk and combine them using application-specific or systemspecific utility parameters into a new nested utility function. For example, let us define the user’s utility function between disk space, $x _ { \mathrm { d s } }$ , and access latency, $x _ { \mathrm { a l } } .$ , as $U ( x _ { \mathrm { d s } } , x _ { \mathrm { a l } } )$

Assuming the broker determines the applicationspecific CES parameters to be and , and there are available disks at sites A and B, then the broker’s utility function is

$$
\begin{array}{r l} & U \big (x _ {\mathrm{dsA}}, x _ {\mathrm{alA}}, x _ {\mathrm{dsB}}, x _ {\mathrm{alB}} \big) \\ & = \Big (\alpha_ {\mathrm{dsA}} ^ {1 - \gamma} U _ {\mathrm{dsA}} \big (x _ {\mathrm{dsA}}, x _ {\mathrm{alA}} \big) ^ {\gamma} \\ & + \alpha_ {\mathrm{dsB}} ^ {1 - \gamma} U _ {\mathrm{dsB}} \big (x _ {\mathrm{dsB}}, x _ {\mathrm{alB}} \big) ^ {\gamma} \Big) ^ {1 / \gamma} \end{array}
$$

where $U _ { \mathrm { d s A } }$ and $U _ { \mathrm { d s B } }$ are copies of the user’s original utility function.

From this composite function, one can analytically derive the appropriate four demand functions for $x _ { \mathrm { d s A } } , ~ x _ { \mathrm { a l A } } , ~ x _ { \mathrm { d s B } }$ , and $x _ { \mathrm { a l B } }$ <sup>w</sup> <sup>x</sup> 22 . However, the users only need to know their own preferences between disk space and latency. Additionally, once network transportation is priced, a natural extension would be for brokers to own the network links and then provide admission control 36 .

## 5.2.2. Transacting out of equilibrium

Another assumption made in these experiments was that disk space was allocated statically once a day, after all the markets had converged to an equilibrium, as opposed to dynamically, as needed. If we relax this assumption, a continuous double auction would allow the agents to buy disk space immediately. Of course, agents buying disk space earlier may end up paying less than agents who buy later. Also, there may be some agents willing to pay more for disk space than agents currently using it, who would be rejected — clearly not Pareto efficient. If instead, we use a second price auction, all files will be priced at the highest amount of the denied files, as in the Internet smart market approach 19 . Files<sup>w</sup> <sup>x</sup> would get bumped by higher paying, and therefore higher valued files, and have to relocate to more inexpensive disk space. Although this policy is optimal for a single-disk space auction, we have not seriously addressed the implications for multiple disk space auctions.

## 6. Conclusion

In this paper, we have formulated a market economy for distributed file allocation for mobile users. Results show that a market-based solution based on a notion of economic, rather than network efficiency can result in solutions that increase the overall welfare of users when compared to fixed allocations. These mechanisms are flexible with respect to user mobility and diversity — as users move, or user populations change, prices adjust so that consumers demand just the amount of disk space available in accordance with their utilities.

Adjusting endowments provides additional control of the distributed file system. In the case of the highand low-income rapid-access users, we used initial endowments to provide a means of adjusting priorities across users. One can imagine endowments being determined externally, as part of the consumers overall optimization for file allocation vs. all other goods. This scheme could form the basis of file allocation scheme based on willingness-to-pay.

We also examined how the introduction of variable capacity producers of disk space makes it possible to reason about acquiring or migrating disk space in response to mobile demands. Finally, we examined a number of issues related to market design. Use of brokers reduces communication overhead by not requiring individual users to have knowledge of network latencies and disk locations, however, there may be some loss in flexibility in terms of price stability and efficiency of allocations.

Extending this framework to deal with a real-world distributed operating system, environment requires relaxing many of the simplifying assumptions made, such as requiring continuous goods or transacting only upon equilibrium. We would like to pursue some of these issues as well as extend the simulation environment by adding resources including re-Ž sources with quality of service and using a more. complex network topology. Although the results presented here provide some indication of the applicability of auction-based market mechanisms to distributed file system operations, additional analysis is needed to determine the scalability of the approach and to quantify the benefits relative to both standard fixed allocation and dynamic reallocation approaches.

## Acknowledgements

We would like to thank Eric Horvitz and John Douceur at Microsoft Research who contributed to the concepts and work described here.

## References

<sup>w</sup> <sup>x</sup> 1 S. Bikhchandani, J.M. Ostroy, The package assignment model, in: Maryland Auction Conference, 1998, May.

<sup>w</sup> <sup>x</sup> 2 W.P. Birmingham, K.M. Drabenstott, C.O. Frost, A.J. Warner, K. Willis, The University of Michigan digital library: this is not your father’s library, in: Proceedings of Digital Libraries ’94, 1994, pp. 53–60, June.

<sup>w</sup> <sup>x</sup> 3 W.J. Bolosky, R.P. Draves, R.P. Fitzgerald, C.W. Fraser, M.B. Jones, T.B. Knoblock, R. Rashid, Operating system directions for the next millennium, Technical report, Microsoft Research, http:<sup>rr</sup>research.microsoft.com<sup>r</sup>os<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 4 D.E. Campbell, Resource Allocation Mechanisms, Cambridge Univ. Press, 1987.

<sup>w</sup> <sup>x</sup> 5 J.Q. Cheng, Essays on Designing Economic Mechanisms, PhD thesis, University of Michigan, Economics Department, May 1998.

<sup>w</sup> <sup>x</sup> 6 N. Economides, The economics of networks, http:<sup>rr</sup> raven.stern.nyu.edu<sup>r</sup>networks<sup>r</sup>biblio hframe.html.

<sup>w</sup> <sup>x</sup> 7 D.F. Ferguson, C. Nikolaou, J. Sairamesh, Y. Yemini, Economic models for allocating resources in computer systems, in: S.H. Clearwater Ed. , Market-Based Control: A ParadigmŽ . for Distributed Resource Allocation, World Scientific, 1996.

<sup>w</sup> <sup>x</sup> 8 I.A. Ferguson, M.J. Wooldridge, Paying their way: commercial digital libraries for the 21st century, D-Lib Magazine Ž .1997 June.

<sup>w</sup> <sup>x</sup>9 D. Friedman, J. Rust Eds. , The Double Auction Market,Ž . Addison-Wesley, 1993.

<sup>w</sup> <sup>x</sup> 10 P.R. Gregory, Comparative Economic Systems, Houghton Mifflin, 1989.

<sup>w</sup> <sup>x</sup> 11 K. Harty, D. Cheriton, A market approach to operating system memory allocation, in: S.H. Clearwater Ed. , Mar-Ž . ket-Based Control: A Paradigm for Distributed Resource Allocation, World Scientific, 1996.

<sup>w</sup> <sup>x</sup> 12 N.R. Jennings, P. Faratin, M.J. Johnson, T.J. Norman, P. O’Brien, M.E. Wiegand, Agent-based business process management, International Journal of Cooperative Information Systems 5 2Ž . Ž . <sup>r</sup>3 1996 105–130.

<sup>w</sup> <sup>x</sup> 13 J.F. Kurose, R. Simha, A microeconomic approach to optimal resource allocation in distributed computer systems, IEEE Transactions on Computers 38 5 1989 705–717,Ž . Ž . May.

<sup>w</sup> <sup>x</sup> 14 S. Lalis, C. Nikolaou, D. Papadakis, M. Marazakis, Marketdriven service allocation in a qos-capable environment, in: First International Conference on Information and Computation Economies, 1998, pp. 92–100, October.

<sup>w</sup> <sup>x</sup> 15 A.A. Lazar, N. Semret, Design, analysis and simulation of the progressive second price auction for network bandwidth sharing, Technical Report 487-98-21, Department of Electrical Engineering, Columbia University, 1998.

<sup>w</sup> <sup>x</sup> 16 J.K. MacKie-Mason, Multi-agent systems, mechanism design and institutions, Invited talk handout at The First International Conference on Information and Computation Economies ICE-98 .Ž .

<sup>w</sup> <sup>x</sup>17 J.K. MacKie-Mason, Telecom information resources on the Internet, http:<sup>rr</sup>china.si.umich.edu<sup>r</sup>telecom<sup>r</sup>telecominfo.html.

<sup>w</sup> <sup>x</sup>18 J.K. MacKie-Mason, S. Shenker, H.R. Varian, Service architecture and content provision: the network provider as editor, Telecommunications Policy 20 3 1996 203–217, April.Ž . Ž .

<sup>w</sup> <sup>x</sup> 19 J.K. Mackie-Mason, H.R. Varian, Pricing congestible resources, IEEE Journal on Selected Areas in Communications 13 7 1995 1141–1149.Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 R.P. McAfee, J. McMillan, Auctions and bidding, Journal of Economic Literature 25 1987 699–738.Ž .

21 J. McMillan, Selling spectrum rights, Journal of Economic Perspectives 8 1994 145–162.Ž .

<sup>w</sup> <sup>x</sup> 22 T. Mullen, Design of Computational Market Systems for Network Information Services, PhD thesis, University of Michigan, Computer Science and Engineering Department, May 1999.

<sup>w</sup> <sup>x</sup> 23 T. Mullen, M.P. Wellman, Market-based negotiation for digital library services, in: Second USENIX Workshop on Electronic Commerce, 1996, pp. 259–269, November.

<sup>w</sup> <sup>x</sup> 24 O. Regev, N. Nisan, The POPCORN market — an online market for computational resources, in: First International Conference on Information and Computation Economies, 1998, pp. 148–157, October.

<sup>w</sup> <sup>x</sup> 25 D. Reininger, D. Raychaudhuri, M. Ott, Market based bandwidth allocation policies for QoS control in broadband networks, in: First International Conference on Information and Computation Economies, 1998, pp. 101–110, October.

<sup>w</sup> <sup>x</sup> 26 J.S. Rosenschein, G. Zlotkin, Rules of Encounter: Designing Conventions for Automated Negotiation Among Computers, MIT Press, 1994.

<sup>w</sup> <sup>x</sup> 27 M.H. Rothkopf, A. Pekec, R.M. Harstad, Computationally manageable combinatorial auctions, Technical Report RRR 13-95, RUTCOR, Rutgers University, April 1995.

<sup>w</sup> <sup>x</sup> 28 J. Sairamesh, D. Ferguson, Y. Yemini, An approach to pricing, optimal allocations and quality of service provisioning in high-speed networks, in: Proceedings of the INFO-COM ’95, 1995, pp. 1111–1119.

<sup>w</sup> <sup>x</sup> 29 S. Shenker, D. Clark, D. Estrin, S. Herzog, Pricing in computer networks: reshaping the research agenda, Telecommunications Policy 20 3 1996 183–201.Ž . Ž .

<sup>w</sup> <sup>x</sup> 30 M. Stonebraker, M. Aoki, A. Pfeffer, A. Sah, J. Sidell, C. Staelin, A. Yu, Mariposa: a wide-area distributed database system, VLDB 5 1996 48–63, January. Ž .

<sup>w</sup> <sup>x</sup> 31 H.R. Varian, The information economy, http:<sup>rr</sup>www. sims.berkeley.edu<sup>r</sup>resources<sup>r</sup>infoecon<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 32 H.R. Varian, Economic mechanism design for computerized agents, in: First USENIX Workshop on Electronic Commerce, 1995, July.

<sup>w</sup> <sup>x</sup> 33 C.A. Waldspurger, T. Hogg, B.A. Huberman, J.O. Kephart, S. Stornetta, Spawn: a distributed computational economy, IEEE Transactions on Software Engineering 18 1992 103–Ž . 117.

<sup>w</sup> <sup>x</sup> 34 W.E. Walsh, M.P. Wellman, P.R. Wurman, J.K. MacKie-Mason, Some economics of market-based distributed scheduling, in: Eighteenth International Conference on Distributed Computing Systems ICDCS-98 , 1998, pp. 612–621,Ž . May.

<sup>w</sup> <sup>x</sup> 35 M.P. Wellman, A market-oriented programming environment and its application to distributed multicommodity flow problems, Journal of Artificial Intelligence Research 1 1993Ž . 1–23.

<sup>w</sup> <sup>x</sup> 36 M.P. Wellman, J.K. MacKie-Mason, S. Jamin, Marketbased adaptive architectures for information survivability, http:<sup>rr</sup>www-personal.umich.edu<sup>r</sup>jmm<sup>r</sup>papers<sup>r</sup>darpa<sup>r</sup> Surv Proposal.html, 1997.

<sup>w</sup> <sup>x</sup> 37 P.R. Wurman, Multidimensional auction design for computational economies: A dissertation proposal, http:<sup>rr</sup>ai. eecs.umich.edu<sup>r</sup>people<sup>r</sup>pwurman<sup>r</sup>work.html.

<sup>w</sup> <sup>x</sup> 38 P.R. Wurman, M.P. Wellman, W.E. Walsh, The Michigan internet auctionbot: a configurable auction server for human and software agents, in: Second International Conference on Autonomous Agents, 1998, pp. 301–308, May.

<sup>w</sup> <sup>x</sup> 39 F. Ygge, H. Akkermans, Power load management as a computational market, in: Proceedings of International Conference on Multi-Agent Systems, 1996, pp. 393–400.
