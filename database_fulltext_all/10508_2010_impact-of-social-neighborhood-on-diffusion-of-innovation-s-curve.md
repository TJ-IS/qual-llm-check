---
otero_id: 10508
otero_key: "GVNV426D"
title: "Impact of social neighborhood on diffusion of innovation S-curve"
authors: "Lev Kuandykov; Maxim Sokolov"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.11.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Impact of social neighborhood on diffusion of innovation S-curve

Lev Kuandykov ⁎, Maxim Sokolov

Corning Inc., Corning Scientific Center, Shatelena Str. 26A, 194021 Saint-Petersburg, Russia

## a r t i c l e i n f o

Article history: Received 17 July 2008 Received in revised form 22 October 2009 Accepted 6 November 2009 Available online 11 November 2009

Keywords: Diffusion of innovation Agent-based modeling Word of mouth Social networks

## a b s t r a c t

Agent-based modeling (ABM) of Diffusion of Innovation (DOI) allows capturing of complex system phenomena that are related to social network topology, in contrast to traditional approaches such as Fisher-Pry or Bass models. These effects can be crucial for accurate prediction of DOI in the markets with strong in<sup>fl</sup>uence of word-of-mouth. In this paper we compared DOI through random and scale-free social networks using ABM. The model predicts faster product adoption for a random network compared with a scale-free network with the same number of nodes due to the presence of hubs. Longer diffusion time in scale-free networks is related to lower information equality. Real world social networks can be a mixture of the two considered extreme cases and also can depend on the type of product.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Market analysts often use a Diffusion of Innovation (DOI) approach for a new product adoption rate prediction. The major outcome of DOI modeling is a cumulative number of adopters, individuals who have already adopted the innovation, function of time. The function curve usually has an “S” like shape and is therefore called an S-curve. Traditional DOI modeling implies knowledge of historical data and has limited parameter set to obtain detailed market evaluation. The DOI process can be modeled much more ef<sup>fi</sup>ciently with an agent-based approach that is capable to capture all relevant elements of the market including social networks. In this paper we discuss effect of social neighborhood topology on diffusion of innovation using the agentbased modeling technique.

## 1.1. Traditional diffusion of innovation approach

Traditional DOI theory implies product adoption by individuals due to internal in<sup>fl</sup>uences that marketers often call “word-of-mouth” (Fisher-Pry model) or by both internal and external in<sup>fl</sup>uences like mass media advertising (Bass model) [10]. The following equation illustrates classical Bass model for DOI S-curve N(t)

$$
\frac {d N (t)}{d t} = \frac {q}{m} \cdot N (t) (m - N (t)) + p \cdot (m - N (t)),\tag{1}
$$

where $N ( t )$ is the number of cumulative adopters, p is the coef<sup>fi</sup>cient of external in<sup>fl</sup>uence, q is the coef<sup>fi</sup>cient of internal in<sup>fl</sup>uence, and m is the market potential or potential number of ultimate adopters.

Market researchers use Eq. (1) to predict future sales by varying the coef<sup>fi</sup>cients p and q using different assumptions, experience, and historical sales data. One can see from this equation that the Bass model is more for treatment of the system as a whole than for studying the system's internal structure. In addition to the model limitations listed in Ref. [10], such approach does not allow treatments of <sup>fi</sup>ne system structures like social network and clustering.

## 1.2. Social neighborhood and social networks

The consumer decision making process on the new product adoption involves a complex interaction of various external and internal factors like mass media, advertizing, word-of-mouth, personal preferences and experience. Interpersonal communications, without a doubt, constitute an important communication media especially for social groups that are hardly reachable by mass media advertising [5,8,9]. A friend's opinion or advice often can be a decisive argument for a purchase. If one wants to provide accurate and reliable estimations of diffusion of innovation rate then he or she should not neglect existence and structure of the social neighborhood where potential innovation adopters live.

Ref. [1] points out on two possible topology types for social networks: random network and scale-free network. In random networks most nodes have approximately the same number of links, while in scale-free networks some nodes named hubs could have very high numbers of connections. These networks are two extreme examples of social neighborhood topology.

When individual behavior patterns of the product adopters are similar, one can describe their social neighborhood topology as a random network where each person has an equal number of peers or friends. For example, researchers can use random networks in behavior studies of large societies, like a state or country, where personal features of each particular individual do not have signi<sup>fi</sup>cant impact on the product adoption.

Scale-free networks can be useful for describing highly inhomogeneous social neighborhoods where certain persons (hubs) have the ability to reach a large number of people while most others have only few connections. Sales professionals and hiring agents are examples of such social hubs.

It is clear from Eq. (1) that the traditional approach to diffusion of innovation modeling, like the Bass model, is not very helpful when one wants to take social networking effects into account. Agent-based modeling is one of possible approaches that allow capturing of the system structure and interaction of the system elements.

## 1.3. Agent-based modeling

Agent-based modeling (ABM) is a relatively new technique that is based on the concept of an agent, which is an autonomous decisionmaking entity that individually assesses its situation and makes decisions based on a set of rules [6]. Approaches like System dynamics [14] or traditional DOI models postulates relationships between known macro variables and study the systems “top-to-bottom”. While ABM reveal dynamic effects from the constituent building blocks, agent, and potentially allows description of all relevant elements of a system, including social neighborhood thus treating the system from the “bottom-up”.

Moreover, ABM captures emergent phenomenon, a demonstration of new system features which were not initially observed in the system components (agents). As a result, ABM can provide outcomes that are often counterintuitive. Ref. [2] describes the effect of clustering on a DOI S-curve by using two clusters where agents preferably establish links with other agents from the same cluster rather than with agents from other cluster. In the case of two clusters, full product adoption to occur twice as fast versus the case of one cluster with the same total number of agents.

In this paper we study the impact of social network type on a diffusion of innovation S-curve using agent-based modeling. The work covers clustering effects and comparison of two social topologies: random and scale-free networks.

## 2. Model formulation

We developed an agent-based model for diffusion of innovation using NetLogo environment [15]. In the model, information about a new product spreads from agent to agent through the links of the social network. At each time step each agent looks at its social neighbors, counts those who adopted the product, and makes a decision on the product adoption with the probability the same as in Ref. [2]

$$
V (\rho) = \frac {\rho_ {k} ^ {d}}{\rho_ {k} ^ {d} + \theta^ {d}} \cdot (1 + \theta^ {d}),\tag{2}
$$

where $\rho _ { k } = n _ { k } / n$ is the fraction of agents in agent k's neighborhood who have adopted the product; n is the total number of k's agent neighbors; $n _ { k }$ is the number of k's agent neighbors who already adopted the product; θ and d are <sup>fi</sup>tting parameters that determine time to adoption start and S-curve steepness, respectively. Those agents, which adopted the product at zero time are set manually and called initial adopters. Parameters θ and d re<sup>fl</sup>ect probability of adoption according to the Eq. (2). The values of these parameters (θ=0.5 and d=5) were chosen so that adoption probability is equal to 0.95 when 80% of the node neighborhood already adopted innovation and the probability is 0.01 when only 20% of the nodes become adopters.

## 3. Results and discussions

## 3.1. Random network

In the present work, we consider three clusters populated with identical agents (Fig. 1), and compare three different cases.

## 3.1.1. Case A (1 cluster)

One cluster has 150 agents where each agent has 30 links with other randomly selected agents. This is a pure example of the random network where each node has the same number of neighbors. At the beginning of the simulation, 5 initial adopters are randomly distributed along the network. At each time step, agents re-evaluate their status and decide whether to adopt new product or not with the probability $V ( \rho )$ de<sup>fi</sup>ned in Eq. (2). Fig. 2 shows the relationship between number of cumulative adopters and number of time steps (S-curve).

## 3.1.2. Case B (3 clusters linked consequently)

150 identical agents are equally distributed through 3 clusters that are connected sequentially: I–II–III. Each agent has about 25 connections with other agents in the same cluster and about 5 connections with agents from other cluster. For example, an agent from the cluster I can have 25 links in the cluster I and 5 links in the cluster II. Agents from the cluster II can simultaneously have 25 links in their native cluster, a couple of links with agents in the cluster I, and another couple of links with agents in the cluster III. As mentioned, in this case the clusters I and III have no direct connections. At the beginning of simulation only 5 initial adopters exist in the cluster I and no initial adopters exist in the rest of clusters. Fig. 2 demonstrates the computed DOI S-curve for Case B (dashed line). Steps on the S-curve indicate penetration jumps within a localized cluster by innovation adopters. Since the cluster I has all the initial adopters, at <sup>fi</sup>rst innovation spreads in the cluster I then in the cluster II and then in the cluster III.

## 3.1.3. Case C (3 clusters linked circularly)

This case is similar to Case B, with some difference in cluster connections. Here the social network is absolutely symmetrical and all agents can establish links with other agents either from their native or any other cluster. As in Case B, an agent is 5 times more likely to establish connection with an agent from the same cluster than with an agent from another cluster. So, a typical agent from the cluster I will have about 25 links in the cluster I, 2 or 3 links in the cluster II, and 2 or 3 links in the cluster III. The same situation exists for agents from the clusters II and III. As before, 5 randomly distributed initial adopters exist only in the cluster I. Fig. 2 presents the DOI S-curve for Case C with dash–dot line.

![](/api/attachments/GVNV426D/fulltext/images/52774e398e09287e471e0bb7a61aef88020ec7e15dd7589fd25933b5d271be48.jpg)  
Fig. 1. Schematic illustration of the random network of 150 agents and 3 clusters. The network is similar to the network from Case C, except here each agent has 10 connections instead of 30 to make visualization of the network easier.

![](/api/attachments/GVNV426D/fulltext/images/a38296b234f8993a349042c18e578cea3c3dcf6c0cdb05235912412400a614bf.jpg)  
Fig. 2. Diffusion of innovation S-curves computed with agent-based model of a social neighborhood for 3 cases: Case A — all agents are in one cluster; Case B — agents are equally distributed between 3 clusters that are connected sequentially; Case C — the same as Case B but all 3 clusters are interconnected as in Fig. 1.

The steps of the S-curves in the Cases B and C are related to the quicker DOI inside the small clusters. Case B is the most pronounced demonstration of such staged DOI (Fig. 2, dashed line) where the DOI goes in the cluster I then in the cluster II and then in the cluster III. In the Case C, the DOI in the clusters II and III goes in parallel after the innovation covers the cluster I <sup>fi</sup>rst. This is rather natural since the initial adopters are located in the cluster I and in the Case C both cluster II and III has direct links with the cluster I.

The major conclusion from the studies is that innovation spreads remarkably faster through a clustered random network (Case B and C) than through one uniform cluster (Case A) with the same total population and same number of initial adopters. Note that in all three cases initial adopters are only located in the cluster I. Ref. [2] demonstrates this effect with a two cluster DOI model. In the present paper, we observe the same effect of DOI acceleration in case of three clusters connected either consequently one by one (Case B) or all together (Case C, Fig. 1). We also performed comparison of innovation diffusion process in random and scale-free networks (Section 3.2) which we consider as a major contribution of the present paper.

One can see from Fig. 2 that the curves have different takeoff time. According to Ref. [3], no single de<sup>fi</sup>nition of the S-curve takeoff time exists so far but the S-curve usually takes off within 10–20% adoption [12]. In our studies, we select the takeoff threshold at the level of 15%. At the takeoff moment, the number of adopters in an arbitrary agent neighborhood is several times higher for the clustered network topology than for the one cluster case which is the origin for the higher DOI speed in the clustered network topology.

## 3.2. Scale-free network

Scale-free networks significantly differ from random networks in the manner of agent connects. The random network consists of agents with about the same number of connections. Contrary, in the scalefree network, most of the agents have a few links (nodes) while some of the agents have lots of connections (hubs). Fig. 3 illustrates a scalefree network built on a preferential attachment principle that is each new agent that enters the system will preferably but not necessarily establish connection with an agent that has highest number of connections so far [11].

![](/api/attachments/GVNV426D/fulltext/images/68b299dffe27149a21f7645e6615306b3aab235137635ca5d4b48375fbf0e7b7.jpg)  
Fig. 3. The scale-free network of 150 agents used for DOI modeling. While most agents have only one connection (node), some agents have several connections (hubs). Circles and squares mark initial adopters used for computing the DOI S-curves presented in Fig. 4.

We use the same agent behavior rules for DOI through the scalefree network as in the case of random network and computed the DOI S-curves for two types of initial adopters: hubs and nodes (Fig. 4). In both cases we consider the same number of initial adopters equal to 5 and the same total number of agents equal to 150. One can see from Fig. 4 that a product adoption process started from hubs goes much faster than an adoption process started from nodes. Two long <sup>fl</sup>at terraces in the dashed curve (Fig. 4) indicate the time the nodes need to convince the hubs to adopt the product, or, in other words, the time the hubs need to note product adoption levels among the hub's numerous connections. Once the hub adopts the product, the DOI process speeds up dramatically. The jump in the dashed curve at around 150000 time steps in Fig. 4 indicates product adoption by one of two largest hubs in the center of the scale-free network in Fig. 3.

In the presented results, time to 100% adoption in the case of scalefree networks is longer than in the case of random networks in spite of the same total number of agents and the same number of initial adopters. The reason for that we see in the lower information equality. Ref. [13] contains a recent research on social and media latency effect on DOI. The authors suggests that innovation diffusion propagation speed depends on so-called “information equality”. A network with higher information equality will conduct DOI much faster than the lower information equality network. As a result, the adoption curve will rise earlier in such networks. According to Ref. [13], information equality depends on the social network structure. Longer diffusion time in the scale-free networks is related to lower information equality in comparison with random network topology. However, we observed the tendency for the time to full adoption to grow with the number of links in the random network. So, at some point the DOI in random-networks can also take very long times. Literally speaking, in random networks with large number of links the initial adopters are lost among the others and their presence becomes less signi<sup>fi</sup>cant for other agents. We will use the same language to explain DOI in the scale-free networks. When initial adopter is a hub, its status is more visible for others when the initial adopter is a node. When information about the product reaches a hub the adoption curve sharply raises since the hub's neighborhood immediately adopts the product following the hub. That is why the DOI process goes much faster (solid line in Fig. 4) when the hubs are initial adopters.

![](/api/attachments/GVNV426D/fulltext/images/6cbf18af0eb488a4857cf770af10d6274a545c947c561f9f2f11534f38300b55.jpg)  
Fig. 4. The diffusion of innovation S-curves computed with agent-based model of a social scale-free network presented in Fig. 3 with 2 different initial conditions: 1. DO starts from 5 hubs (solid line); 2. DOI starts from 5 nodes (dashed line).

The information equality also explains lower initial growth in the earlier phases of the DOI in random-networks than a classical symmetrical diffusion S-curve. In this case, social network topology induces the information inequality in the sense that the initial adopters can reach only limited number of agents from their direct neighborhood. Namely, each initial adopter can reach only 30 agents. The ABM S-curve will almost have the same symmetrical type as classical S-curve if all the agents will be directly linked with each other [2].

## 4. Advantages and issues of agent-based modeling

In the previous sections we demonstrated the agent-based technique capabilities for diffusion of innovation modeling that are missed in traditional DOI models such as social neighborhood and social network topologies. Refs. [4,7] discuss issues of the agent-based modeling for social systems in details. Here we will point out some of them that are of high importance for DOI modeling: system size, network topology, time step size, and phenomenological calibration.

Most relevant system size is the size of the real society where DOI occurs. However, such approach can lead to incorporation of millions of agents into the model. Simulations of large systems are very expensive in terms of computational time and are hard to build and control. A proper choice of representative consumer group could help solving these problems. If a further increase of the number of agents will not have a major effect on the model outcomes then one may conclude that this is the optimal system size for the modeling.

In this paper we considered two types of social networks: random and scale-free. In real life there is always something in between. The social network structure is among the most crucial data that researchers may need for adequate DOI modeling. We have no single advice about the right social networks choice for the model except our thoughts listed in the Introduction section. De<sup>fi</sup>nitely, the network topology depends on the product and can be different for different products even within the same social group.

All relationships in the previous section (Figs. 2 and 4) are plotted in the time scale equal to the model time step or, in other words, the model iteration. In the model, iteration is the act of status rethinking by potential adopter. Each iteration, agent looks on its neighbors and decides if the innovation worth adoption or not. How many times a day people think about the new product and how often they contact their neighbors on this topic is a subject of research.

Traditional views on the time step size, the same as on values of θ and d in Eq. (2), would be considering it as <sup>fi</sup>tting parameters used for the model calibration and adjustment to the real world data. If one looks at it this way, then ABM does not go much further than classical

DOI models with parameters p and q (see Eq. (1)). Conservative thinking suggests that if we do not know θ and d then we could not extract much value from agent-based DOI modeling. This is the same problem as with low value of traditional DOI when p and q are unknown. The important advantage of ABM is in its ability to run various DOI scenarios by varying the system parameters and run it in a very natural and intuitive form. The agent-based technology is more for understanding of system behavior then for exact number predictions. One should use ABM for revealing patterns, tendencies, and trends in the system evolution instead of expecting exact adoption rates or market shares. ABM is especially useful for DOI modeling of completely new products in the absence of historical data and relevant markets. If the product is unique or the market is emerging and there is no chance of making surveys and experiments then testing scenarios of possible product adoption could be the best alternative for the market researcher. The ABM can help acquire understanding of the market reaction on the product depending on product features and the customer perception at early stages when real diffusion of innovation is even not started.

## 5. Conclusions

We study effect of social neighborhood on diffusion of innovation for two types of social networks, random and scale-free, using an agent-based modeling technique. The agent-based approach allows capturing of complex system phenomena in contrast to the traditional diffusion of innovation models like Fisher-Pry or Bass model.

In terms of the presented model, in random networks the diffusion of innovation accelerates signi<sup>fi</sup>cantly if the population is split into clusters. This happens because at the S-curve takeoff moment, the number of adopters in an arbitrary agent neighborhood is higher for the clustered network topology than for the one cluster case.

In comparison with a random network, our simulation showed complete market adoption later for the case of a scale-free network built on preferential attachment principle. Longer diffusion time in the scale-free networks is related to lower information equality in comparison with random network topology. The DOI spreads faster through the scale-free network if the initial adopters are hubs and slower if they are ordinary nodes. When initial adopter is a hub, its status is more visible for other nodes. When information about the product reaches a hub the adoption curve sharply raises since the hub's neighborhood immediately adopts the product following the hub. At the same time hubs that are not initial adopters could become a bottleneck for the innovation diffusion.

The social network topology induces the information inequality in the sense that the initial adopters can reach only limited number of agents from their direct neighborhood. In the limit case, when all agents are interconnected the ABM S-curve will almost have the same symmetrical type as in classical Fisher-Pry theory.

## References

[1] A.-L. Barabasi, E. Bonabeau, Scale-Free Networks, Scienti<sup>fi</sup>c American 4 (2003).

[2] E. Bonabeau, Agent-based modeling: Methods and techniques for simulating human systems, Proceedings of the National Academy of Science of the United States of America 99 (suppl. 3) (2002).

[3] D. Chandrasekaran, G.J. Tellis, A Critical Review of Marketing Research on Diffusion of New Products, Review of Marketing Research 3 (2006).

[4] C. Ciof<sup>fi</sup>-Revilla, Invariance and universality in social agent-based simulations Proceedings of the National Academy of Science of the United States of America 99 (suppl. 3) (2002).

[5] K. de Valck, G.H. van Bruggen, B. Wierenga, Virtual communities: A marketing perspective, Decision Support Systems 47 (3) (2009).

[6] A.P. Engelbrecht, Fundamentals of Computational SWARM Intelligence, Wiley & Sons, England, 2006.

[7] R. Garcia, P. Rummel, J. Hause, Validating Agent-Based Marketing Models Using Conjoint-Analysis, Journal of Business Research 60 (8) (2007).

[8] P. Gaudiano, O. Bandte, D. Duzevik, D. Anev, How Word-of-Mouth Impacts Medicare Product Launch and Product Design, Proceedings of the Word of Mouth Marketing Summit (WOMMA) Las Vegas NV 2007.

[9] C. Kiss, M. Bichler, Identi<sup>fi</sup>cation of in<sup>fl</sup>uencers – Measuring in<sup>fl</sup>uence in customer networks, Decision Support Systems 46 (1) (2008).

[10] V. Mahajan, E. Muller, F. Bass, New Product Diffusion Models in Marketing: a Review and Directions for Research, Journal of Marketing 54 (1) (1990).

[11] A. Reka, A.-L. Barabasi, Statistical mechanics of complex networks, Reviews of Modern Physics 74 (1) (2002).

[12] E. Rogers, Diffusion of Innovations, Free Press, New York, 1995.

[13] A. Sinnreich, A. Chib, J. Gilbert, Modeling Information Equality: Social and Media Latency Effects on Information Diffusion, International Journal of Communication 2 (2008).

[14] J.D. Sterman, Business Dynamics: Systems Thinking and Modeling for a Complex World, McGraw-Hill, USA, 2000.

[15] U. Wilensky, Center for Connected Learning and Computer-Based Modeling Northwestern University, Evanston, IL, 1999 http://www.ccl.northwestern.edu netlogo.

![](/api/attachments/GVNV426D/fulltext/images/2ac7ed0dc9b21850ecdf110ab50eab08719fe45f709e63ad2073bf519a35f264.jpg)  
Maxim Sokolov is a Senior Research Scientist at Corning Incorporated, Modeling and Simulation department. He also serves as IEEE Russia Northwest Section Secretary. His research interests are in scienti<sup>fi</sup>c computing, data mining, machine learning and pattern recognition. Maxim earned his Engineering degree in Applied Math and PhD degree in Computer Science from St. Petersburg State Electrotechnical University “LETI” in Russia. He was awarded President of Russian Federation stipend for postgraduates in 2000. In 2007 he got Executive Certi<sup>fi</sup>cate in Management in Leadership from MIT Sloan School of Management, Cambridge, MA, USA.

![](/api/attachments/GVNV426D/fulltext/images/e9f34d1214287715e8306cf9ce540c3dc72b8f9f6423049461330abc8d9b1b59.jpg)

Lev Kuandykov is a Senior Research Scientist and Project Manager at Modeling & Simulation department of Corning Incorporated. He holds PhD in Physics from Ioffe Physico-Technical Institute, Saint-Petersburg, Russia and Executive Certi<sup>fi</sup>cate in Management in Leadership from MIT Sloan School of Management, Cambridge, MA, USA. Lev has published more than 20 papers in professional journals and conferences on computer modeling and numerical simulations. He earned strong international experience working as a research scientist in Japan, USA, France and Russia. His research interests include computer modeling for technology and business applications that require advanced data and process analysis.
