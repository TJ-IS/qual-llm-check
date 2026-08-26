---
otero_id: 8870
otero_key: "JVJHE3QM"
title: "Network sampling and classification: An investigation of network model representations"
authors: "Edoardo M. Airoldi; Xue Bai; Kathleen M. Carley"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.02.014"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Network sampling and classi<sup>fi</sup>cation: An investigation of network model representations

Edoardo M. Airoldi <sup>a</sup>, Xue Bai <sup>b,</sup>⁎, Kathleen M. Carley <sup>c</sup>

<sup>a</sup> Department of Statistics, Harvard University, Cambridge, MA 02138, USA

<sup>b</sup> Department of Operations and Information Management, School of Business, University of Connecticut, Storrs, CT 06269, USA

<sup>c</sup> School of Computer Science, Carnegie Mellon University, Pittsburgh, PA 15213, USA

## a r t i c l e i n f o

Article history: Received 20 April 2010 Received in revised form 19 January 2011 Accepted 7 February 2011 Available online 26 February 2011

Keywords: Connectivity pattern Network type Network metrics Network sampling Network classi<sup>fi</sup>cation

## a b s t r a c t

Methods for generating a random sample of networks with desired properties are important tools for the analysis of social, biological, and information networks. Algorithm-based approaches to sampling networks have received a great deal of attention in recent literature. Most of these algorithms are based on simple intuitions that associate the full features of connectivity patterns with speci<sup>fi</sup>c values of only one or two network metrics. Substantive conclusions are crucially dependent on this association holding true. However, the extent to which this simple intuition holds true is not yet known. In this paper, we examine the association between the connectivity patterns that a network sampling algorithm aims to generate and the connectivity patterns of the generated networks, measured by an existing set of popular network metrics. We <sup>fi</sup>nd that different network sampling algorithms can yield networks with similar connectivity patterns. We also <sup>fi</sup>nd that the alternative algorithms for the same connectivity pattern can yield networks with different connectivity patterns. We argue that conclusions based on simulated network studies must focus on the full features of the connectivity patterns of a network instead of on the limited set of networkmetrics for a speci<sup>fi</sup>c network type. This fact has important implications for network data analysis: for instance, implications related to the way signi<sup>fi</sup>cance is currently assessed.

© 2011 Elsevier B.V. All rights reserved

## 1. Introduction

Data about connections among individual entities arise in many areas such as management sciences [6,22,36], medical and biological sciences [14], and social, economic and information sciences [16,24– 26,31]. Evidence from research and practice suggests that patterns of connectivity, rather than the intensity of interactions, drive productivity and other important aspects of collective behavior. A connectivity pattern is intuitively de<sup>fi</sup>ned in terms of a special arrangement of connections among a set of nodes in a network. Connectivity patterns are also referred to as characteristics of a network type and can be quantitatively characterized in terms of network metrics. For example, networks with six degrees of separation, also known as small-world networks, are typically characterized quantitatively in terms of two network metrics: network diameter and clustering coef<sup>fi</sup>cients. The typical connectivity pattern in a small-world network is one where, intuitively, nodes have many local connections and a few longdistance connections according to some given distance measure. Commonly seen network types include ring-lattice, small-world, scalefree, core–periphery, and random networks. There are 47 network metrics widely adopted in the social and physical sciences. Examples of popular network metrics include a variety of centrality measures, clustering coefficients, connectedness, hierarchies, and average distances [39].

Algorithm-based approaches to sampling networks [3,34,40] have received a great deal of attention in recent literature [9,11,15,30,41]. Most of the algorithms for sampling networks are based on simple intuitions. These algorithms associate only one or two connectivity patterns of an observed network—such as degree distribution, or diameter and clustering coef<sup>fi</sup>cient—with a simple process that aims to generate networks with the desired connectivity pattern [20].

However, current approaches have a number of issues. For example, the association between published algorithms and the connectivity pattern they are meant to generate has not been formally analyzed in the literature. The ef<sup>fi</sup>ciency and robustness of these algorithms in generating networks with the desired connectivity patterns have not been quanti<sup>fi</sup>ed. Moreover, the association between these algorithms and the full set of network metrics of the networks they can generate has not been explored.

Typically, the structure of a network is de<sup>fi</sup>ned as $G = ( { \mathcal { N } } , { \mathcal { V } } ) ,$ in which is a set of nodes that represent individual entities, and is a set of edges that represent the connectivity pattern among the nodes. The connectivity pattern can be characterized by a popular set of network metrics, including measures of centrality of individuals, degree-based metrics, and global network metrics. Practitioners, however, rely on a limited subset of these network metrics to quantify structural patterns of network types of interest [3]. The disconnect between the limited network metrics that most sampling algorithms consider and the full set of network metrics that a network entails have important implications for network data analysis. For example, many empirical analyses implicitly assume that there is an association between a single metric and a type of networks. An analysis would then claim, for example, that scale-free networks are characterized by having a power-law degree distribution [40]. The substantive conclusions of this analysis crucially depend on the implicit assumption that one individual metric completely determines the structure of scale-free networks. Similarly, high clustering coef<sup>fi</sup>cient and low network diameter are believed to completely determine the structure of small-world networks [5]. In contrast, recent results have shown how it is possible to generate small-world networks with scale-free distribution, as well as scale-free networks with high clustering coef<sup>fi</sup>cient and low diameter [21]. Thus, in general, the problematic issue is that empirical and theoretical studies often claim that an observed network has a certain topological structure. However, the analyses that support such claims are often restricted to one or two network metrics. This is reasonable only if two conditions are met: 1) that one can assume the association between the algorithms and the topological structure is one-to-one, or approximately so; and 2) that the network metrics under consideration fully determine the topological structure of a network. These conditions are often not met.

Another set of issues is related to the existence of multiple algorithms to generate the same type of networks. For instance, there are multiple papers dealing with small-world networks, each one proposing an algorithm to generate small-world networks where nodes live in different metric spaces: on a ring-lattice [40] or in the plane [28]. How similar are the networks generated by these algorithms if we represent the sampled networks in terms of the currently available metrics?

In this paper, we formally assess the extent to which alternative algorithms for generating the same network type actually generate networks with equivalent connectivity patterns; we refer to this issue as the stability issue. We also assess the extent to which different network types de<sup>fi</sup>ned in terms of the commonly used network metrics actually display distinguishable connectivity patterns; we refer to this issue as the separability issue. In performing these assessments, we build on earlier work by Airoldi and Carley [3]. We expand their design of experiments and perform both qualitative and quantitative analyses of the stability of different network sampling methods and those of the separability of different network types. In addition, we discuss the statistical issues involved in network model selection such as suf<sup>fi</sup>ciency, and the implications of our <sup>fi</sup>ndings for parameter estimation and p-value computation for network metrics. These are our key contributions to network analysis literature.

## 1.1. Brief overview of analyses and results

We <sup>fi</sup>nd that the popular network sampling algorithms, e.g., those for scale-free and small-world networks, generate networks with similar connectivity patterns for non-pathological values of the relevant underlying constants. Furthermore, we <sup>fi</sup>nd that alternative algorithms that supposedly generate networks with non-distinguishable connectivity patterns (e.g., algorithms for scale-free networks by different authors) actually give easily distinguishable connectivity patterns. These <sup>fi</sup>ndings prompt us to make recommendations on how to provide successful assessments of the sensitivity of an analysis, to the connectivity patterns of different network types. Our <sup>fi</sup>ndings also suggest that real-world networks may be better modeled as mixtures of these popular network types.

## 2. Problem de<sup>fi</sup>nition

In this section we give a brief overview of the mathematical characteristics of a network, introduce our research context, and formally frame the research questions.

## 2.1. Mathematical characterizations of a network

A network G is de<sup>fi</sup>ned by a set of N vertices, ${ \mathcal { N } } ,$ and a set of edges, . The network G is fully speci<sup>fi</sup>ed by the adjacency matrix, Y, where the element $Y ( n , m ) \in \{ 0 , 1 \}$ , where 1 indicates a directed connection from node n to node m, i.e., n→m; 0 indicates that there is no such connection.

The matrix Y encodes the connectivity patterns of the network it represents. We refer to those functions that map Y to scalar values as network metrics. For instance, the degree of a node is a node-specific metric, meaning every node has a degree measure; the density of a network is a global metric, meaning a network has a single density measure. For example, consider a binary network, the degree of the binary network is de<sup>fi</sup>ned as

$$
d _ {G} (n) = \sum_ {m} Y (n, m) \text { for } n \in \mathcal {N}.
$$

The density of the binary network is de<sup>fi</sup>ned as

$$
\delta_ {G} = \sum_ {n <   m} Y (n, m) \bigg / \binom {N} {2}.
$$

A collection of metrics induced from the adjacency matrix Y provides a quantitative representation of the connectivity patterns of the corresponding network G. In this sense, Y fully characterizes the values of the metrics on G. However, the contrary is not necessarily true.

From a data analysis perspective, we would like to characterize a network in terms of its essential connectivity patterns in the space of metrics to maintain interpretability of the results. In fact, a number of metrics have been proposed in the quantitative psychology and social sciences literatures, and are based on well-established theories of individual and collective behavior [12,39].

## 2.2. Research problems

The utility and appeal of sampling algorithms stems from the assumption that these algorithms are guaranteed to generate the desired connectivity patterns. For example, the “six degrees of separation” among individuals observed by Ref. [33] is captured by the “small-world” network of Ref. [40]. This connectivity pattern informs the sampling algorithm that “individuals form local acquaintances, few of which relocate to places far away.” This stylized model of behavior is suf<sup>fi</sup>cient to replicate the phenomenon observed by Ref. [33], and it “sounds” like a plausible explanation [33,40]. Therefore we have the following research problem.

Problem 1. (Sampling) Given algorithms that generate networks of the same type, we want to assess the stability of the connectivity patterns of the networks generated by these algorithms.

Sampling algorithms can be both deterministic and probabilistic, and they typically depend on a small set of parameters. To fully evaluate their validity, it is important to provide ways to estimate such parameters from observed data.

A related problem, on the other hand, is that of determining which type we should assign to a network under analysis. Network types are used by practitioners to this extent. For example, homeland security of<sup>fi</sup>cers are interested in determining whether an observed criminal network is cellular, given partial measurements about the network.

![](/api/attachments/JVJHE3QM/fulltext/images/4d05a8ccbc51c010f3194238c6d97d494db7d2d8c475610fed76992065805258.jpg)  
Fig. 1. An illustration of the two research problems.

If so, the conclusion may be drawn that destabilization strategies that are successful in cellular networks will be successful in destabilizing the given network. Hence we have the second research question.

Problem 2. (Classification) Given algorithms that generate networks of different types, we want to assess the separability of the connectivity patterns of the networks generated by these algorithms.

In the same example of the “homeland security” scenario, in order for of<sup>fi</sup>cers to determine the correct network type of the criminal network under investigation, it is important for the connectivity patterns of the same network type to be stable and for those of different network types to be separable. We de<sup>fi</sup>ne a connectivity pattern to be stable if the networks sampled using algorithms for the same network type are similar in some metric space. We de<sup>fi</sup>ne connectivity patterns to be separable if the networks sampled using algorithms for different network types are far apart in some metric space. Fig. 1 shows an illustrative example of the two research questions.

The goal of sampling networks (left) is to assess the consistency of alternative algorithms to generate the same type of networks. The larger the intersection between the supports, the more consistent alternative de<sup>fi</sup>nitions are—since they cannot generate many different networks. The goal of classifying networks (right) is to assess the need for de<sup>fi</sup>ning alternative types of networks. The smaller the intersection between the supports, the less confounded different types of networks are—this is because the generated networks are different enough to be distinguishable. The reference space used in this paper is de<sup>fi</sup>ned by 47 metrics [39]. We project all sampled networks in this space.

The stability property of alternative sampling algorithms for the same network type guarantees that choosing one speci<sup>fi</sup>c algorithm over another does not affect the validity of the conclusions. The separability property of alternative sampling algorithms for different network types guarantees that any set of observed connectivity patterns identi<sup>fi</sup>es a unique network type. In other words, separability suggests that it is logically possible to answer questions such as “Is the given network of type X?” The experiments in Section 3.3 are devoted to assess stability and separability of the sampling algorithms surveyed or introduced in Section 3.1.

## 3. Experimental design

The two research problems we tackle are: (1) stability, i.e., to what extent different sampling algorithms for the same pure network type lead to consistent connectivity patterns, as captured by the set of network metrics, and (2) separability, i.e., to what extent the classi<sup>fi</sup>cation of an observed network mapped into the reference space of metrics can uniquely determine the pure network types. In this section, we begin by the heuristic descriptions of the six network types that are commonly seen in network analysis. We then discuss the set of network metrics used in our experiments. After that, we present the experimental setting and the classi<sup>fi</sup>cation scheme.

## 3.1. Network types sampled

Type 1. (Ring lattice) Each node is connected to its neighbors, according to the ring-induced distance (Fig. 2).

Type 2. (Small world) Each node is connected to several of its neighbors and a few distant nodes, according to the ring-induced distance [40] (Fig. 3).

Type 3. (Erdös–Rényi–Gilbert Random) Each node is connected to a random set of the remaining nodes [8,17,19] (Fig. 4).

Type 4. (Scale free) Most of the nodes are connected to a few other nodes, while a small number of nodes are connected to many other nodes. This relation is formally described with a power law, between the number of edges and the number of connections [5] (Fig. 5).

Type 5. (Cellular) Nodes are divided into cells. Connections are frequent between nodes within each cell, and rare between nodes in different cells [18] (Fig. 6).

Type 6. (Core–periphery) Nodes belong exclusively to either the core or the periphery. Core and periphery nodes are connected to core nodes, while there are no edges among periphery nodes [10] (Fig. 7).

Table 1 presents a summary of the algorithms that we consider in the present study.

## 3.2. Network metrics used

We focused our analysis on the 47 metrics that are widely adopted in the social and physical sciences [39]. These metrics are: degree centrality (nos. 1–4<sup>1</sup>), which measures the centrality of a node in terms of its degree distribution; betweenness centrality (nos. 5–8), which measures the centrality of a node in terms of the shortest paths of which the node is a member; closeness centrality (nos. 9–12), inverse closeness centrality (nos. 13–16), eigenvector centrality (nos. 17–20), clustering coef<sup>fi</sup>cient (nos. 21–24, density of the connectivity around a node), effective network size (nos. 25–28), network constraint (nos. 29–32), node levels (nos. 33–36), triad count (nos. 37– 40), global ef<sup>fi</sup>ciency (no. 41), local ef<sup>fi</sup>ciency (no. 42), ef<sup>fi</sup>ciency (no. 43), connectedness (no. 44), hierarchy (no. 45), upper boundedness (no. 46), and average distance (no. 47). Formal de<sup>fi</sup>nitions are available in Ref. [39]. The detailed descriptions of the metrics we used are available in Ref. [12].

![](/api/attachments/JVJHE3QM/fulltext/images/c85b716e4e747992c00f218d486e6c44f67327b3ff04d747694d5b229f320265.jpg)  
Fig. 2. A ring-lattice network.

## 3.3. Performing sampling and classification

A few of the network metrics we consider depend on the size and the average connectivity of a network; for instance, the degree distribution and the triad counts. In order to obtain results and substantiate claims that are independent from these network characteristics, we <sup>fi</sup>x network size and average connectivity in our experimental design. For each of the six network types, we set an evenly spaced grid that spans the entire parameter space. We sampled at least ten networks for each parameter con<sup>fi</sup>guration. The algorithms with more parameters have more possible con<sup>fi</sup>gurations, and result in a larger sample of networks—which we control for in the experiments using strati<sup>fi</sup>ed <sup>fi</sup>ve-fold cross-validation scheme, which are detailed in the next two paragraphs. In addition, we control for other relevant parameters when generating the same network type using different algorithms, with the goal of making sampled networks of the same type consistent across the alternative generating algorithms. Full speci<sup>fi</sup>cations of the experimental design are detailed in Table 2.

We choose the naïve Bayes classi<sup>fi</sup>er as the classi<sup>fi</sup>er. Naïve Bayes classifier has been shown to be the most accurate in predicting the network type of a given network [4]. The classi<sup>fi</sup>cation procedure is as follows. For a given network, we examine the connectivity patterns as captured by the set of 47 metrics we consider. We sample a large quantity of networks, with different parameter values for each pure type. For each sampled network, we <sup>fi</sup>rst compute the corresponding metrics, then classify it into a network type according to the posterior probability of types given its metric con<sup>fi</sup>gurations. We use classification errors to indicate the degree to which pairs of pure network types overlap in the reference space of metrics, see Fig. 1.

![](/api/attachments/JVJHE3QM/fulltext/images/cc772543b35936475ca5f65c2451609f0fbd4058d7d6bf0600c86c0f798ae01e.jpg)  
Fig. 3. A small-world network.

![](/api/attachments/JVJHE3QM/fulltext/images/fd2d5c942a14cfafa77fed7d1d877023b35671219773a47142bcf70fb1db0a91.jpg)  
Fig. 4. A random network.

In order to estimate the classi<sup>fi</sup>cation errors we use a strati<sup>fi</sup>ed <sup>fi</sup>ve-fold cross validation scheme. Five-fold cross validation step aims at estimating error on out-of-sample networks. It consists of the following procedure: we split the set of sample networks into <sup>fi</sup>ve mutually exclusive batches, we then iteratively $( i { = } 1 , . . . , 5 )$ train naïve Bayes classi<sup>fi</sup>er on four batches and test on the ith one, and <sup>fi</sup>nally we estimate the prediction error using the average prediction errors on the <sup>fi</sup>ve-folds. The strati<sup>fi</sup>cation step makes sure that in each training set there are networks of each type, despite some types being more abundant than others in the design. The proportions of networks of each type in the training set are the same as the proportions of networks of each type in the overall sample. The strati<sup>fi</sup>cation aims at minimizing the potential over-<sup>fi</sup>tting in the estimated accuracy [23].

## 4. Computational results

Here we present quantitative and qualitative analyses to explore the stability and separability issues that arise in the classi<sup>fi</sup>cation problem introduced in Section 2.2.

## 4.1. Qualitative assessment of stability

To assess the variability in the network metrics of the sampled networks by alternative sampling algorithms, for each type of the network, we report the comparative empirical distributions of the 47 metrics by each of the alternative sampling algorithms. Figs. 8–12 present the comparative results for <sup>fi</sup>ve network types: random, cellular, scale-free, core–periphery, and small-world, respectively. Since there are no alternative algorithms to generate ring-lattice networks, we did not report those histograms. The empirical distributions in these <sup>fi</sup>gures were estimated using kernel density estimator, which estimates a continuous histogram using a sliding window and a function, the kernel, to weigh the contribution of different points in the window [38]. Each <sup>fi</sup>gure consists of 47 panels; each panel corresponds to a metric, clearly labeled at the top of each panel. Within each panel, we plot multiple density estimates in different colors; each color representing one of the alternative sampling algorithms for a network type. The values each metric can take are rescaled into the interval between 0 and 1. A legend that speci<sup>fi</sup>es the corresponding color for each sampling algorithm in Table 2 is given in the bottom right panel of the <sup>fi</sup>gure.

![](/api/attachments/JVJHE3QM/fulltext/images/026064f694073a4583f6d5f855d3436a022d89a9519bfeea6d17c7e6aaaf72e8.jpg)  
Fig. 5. A scale-free network.

![](/api/attachments/JVJHE3QM/fulltext/images/b4b072b3c2295ea91fe9efede6143d8837acf0163a9b73e773eeaac71494fa9e.jpg)  
Fig. 6. A cellular network.

The comparison of each metric provides a <sup>fi</sup>rst look at the consistency of alternative sampling algorithms. As described in Section 2.2 and illustrated in the left panel of Fig. 1, we want to assess the consistency of alternative algorithms to generate the same type of networks. A large overlap among the network instances by alternative sampling algorithms is desirable, since it would suggest consistency of the alternative algorithmic de<sup>fi</sup>nitions of a network type. In the context of Figs. 8–12, similar distributions for each of the metrics is desirable, since it would suggest consistency of alternative de<sup>fi</sup>nitions of the same network type. However, as shown in the panels, almost all of the metric distributions are different to various degrees. For example, in the random networks (Fig. 8), 45 out of 47 metrics distributions are vastly different. The only two that are similar are the standard deviation of betweenness centrality (the eighth panel on the top row) and the maximum eigenvector centrality (the second panel on the third row from the top). Similar assessments can be conducted based on the distributions in Figs. 9–12. The lack of similarity we see in these Figures suggests that alternative de<sup>fi</sup>nitions of network types are not consistent.

Fig. 7. A core–periphery network.  
![](/api/attachments/JVJHE3QM/fulltext/images/fdcd0b0e3f2616906082537466af0251b9d3beefc8dd930dd7a07e4602ec7f35.jpg)

Table 1  
Summary of published and newly introduced generative algorithms

<table><tr><td>Type</td><td>Algorithm</td><td>Parameters</td><td>Description of parameters</td></tr><tr><td>1.1.</td><td>Ring lattice [8]</td><td> $\Theta = (n,k)$ </td><td>Nodes, neighbors</td></tr><tr><td>2.1.</td><td>Small world [40]</td><td> $\Theta = (n,k,p_n)$ </td><td>Nodes, neighbors, pr rewire</td></tr><tr><td>2.2.</td><td>Small world [27]</td><td> $\Theta = (n,k,l,r)$ </td><td>Nodes, neighbors, distant nodes, power-law exp</td></tr><tr><td>2.3.</td><td>Small world</td><td> $\Theta = (n,k,p_k,p_n,r)$ </td><td>Nodes, init neighbors, pr neighbor, pr distant nodes, power-law exp</td></tr><tr><td>3.1.</td><td>Random [17]</td><td> $\Theta = (n,p_n)$ </td><td>Nodes, pr edge</td></tr><tr><td>3.2.</td><td>Random [19]</td><td> $\Theta = (n,m)$ </td><td>Nodes, edges</td></tr><tr><td>4.1.</td><td>Scale free [7]</td><td> $\Theta = (n,n_0,p_0,p_n)$ </td><td>Nodes, init nodes, pr init edge, pr edge</td></tr><tr><td>4.2.</td><td>Scale free</td><td> $\Theta = (n,m,r)$ </td><td>Nodes, edges, power-law exp</td></tr><tr><td>5.1.</td><td>Core-periphery [10]</td><td> $\Theta = (n,p_0,p)$ </td><td>Nodes, pr core nodes, pr edge</td></tr><tr><td>5.2.</td><td>Core-periphery</td><td> $\Theta = (n,p_0,p)$ </td><td>Nodes, pr core nodes, pr edge</td></tr><tr><td>6.1.</td><td>Cellular [18]</td><td> $\Theta = (n,k,p_k,p_n)$ </td><td>Nodes, pr in-node, cells, pr out-node</td></tr><tr><td>6.2.</td><td>Cellular</td><td> $\Theta = (n,k,p_k,p_n,r)$ </td><td>Nodes, pr in-node, cells, pr out-node, power-law exp</td></tr></table>

More speci<sup>fi</sup>cally, Fig. 8, for example, displays the empirical distributions for the 47 metrics computed on the random networks generated using algorithms 3.1 (np) and 3.2 (nm). Here “np” stands for the two parameters, n and p, that algorithm 3.1 uses as inputs; n and m are the two parameters that algorithm 3.2 uses as inputs. The set of parameter values used to generate the network samples are speci<sup>fi</sup>ed in Table 2. As an illustration, the fourth panel on the top row describes the empirical distributions of the standard deviation of the node degrees for algorithms 3.1 and 3.2. The distribution in green (Algorithm 3.1. np) corresponds to algorithm 3.1. The distribution in red (Algorithm 3.2. nm) corresponds to algorithm 3.2. As expected, the standard deviation of the node degree is much smaller for the networks generated with algorithm 3.2, because this algorithm leads

Table 2  
Design of experiments.

<table><tr><td>Type</td><td>Algorithm</td><td>Samples</td><td>Parameter configuration</td></tr><tr><td>1.1</td><td>Ring lattice</td><td>25</td><td>n=250, k=2,4,...,50</td></tr><tr><td>2.1</td><td>Small world (rewire)</td><td>484</td><td>n=250, k=2,4,...,50,p=0.10,0.15,...,0.90</td></tr><tr><td>2.2</td><td>Small world (number)</td><td>1250</td><td>n=250, k=2,4,...,50, l=1,2,...,10,r=1,2,...,5</td></tr><tr><td>2.3</td><td>Small world (prob.)</td><td>2670</td><td>n=250, k=2,4,...,50, pk=0.20,0.30,...,0.80,pn=0.20,0.30,...,0.80, r=1,2,...,5</td></tr><tr><td>3.1</td><td>Random (prob.)</td><td>17</td><td>n=250, p=0.10,0.15,...,0.90</td></tr><tr><td>3.2</td><td>Random (number)</td><td>17</td><td>n=250, m=311,622,...,28012</td></tr><tr><td>4.1</td><td>Scale free (pref.)</td><td>729</td><td>n=250, n0=10,15,...,50, p=0.10,0.20,...,0.90,p0=0.10,0.20,...,0.90</td></tr><tr><td>4.2</td><td>Scale free (power)</td><td>45</td><td>n=250, m=311,622,...,28012, r=1,2,...,5</td></tr><tr><td>5.1</td><td>Core-periphery (uniform)</td><td>54</td><td>n=250, p0=0.10,0.20,...,0.90,p=0.25,0.35,...,0.75</td></tr><tr><td>5.2</td><td>Core-periphery (pref.)</td><td>54</td><td>n=250, p0=0.10,0.20,...,0.90,p=0.25,0.35,...,0.75</td></tr><tr><td>6.1</td><td>Cellular (uniform)</td><td>360</td><td>n=250, k=2,4,...,20, pk=0.25,0.35,...,0.75,pn=0.25,0.35,...,0.75</td></tr><tr><td>6.2</td><td>Cellular (power)</td><td>360</td><td>n=250, k=2,4,...,20, pk=0.25,0.35,...,0.75,pn=0.25,0.35,...,0.75, r=1</td></tr></table>

![](/api/attachments/JVJHE3QM/fulltext/images/9789fbef0c6eb388eceaf550e07218464c6c0688bf5332efdc2348c82f39d367.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/221736b90bbf11f28cfe444660372ce45b1d9af11364a061d0e01919735c8629.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/0e290677b592ec0a85076059fbf9971519f041c0a64aa1b38f2899c10dfde822.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/9513dc822ccc43e76d3422d805c404f264f8a7f0267c45695251a01ee873fa1e.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/600ba1208e6ac34b414e79b862097573a2013fd3824a76b169dcb6802c897507.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/137619c6a138e7f62c418da89e4970e515d09e4e01eae38d8205aa64fe69b9a6.jpg)  
Fig. 8. Random: empirical distributions of the 47 metrics we consider, excluding shortest path. The distributions were estimated using the sample of random networks generated by algorithms 3.1 (np) and 3.2 (nm) in the experimental design in Table 2.

to networks that have the same exact average connectivity whenever the same value of the parameter (the number of connections m in this case) is used. The red (Algorithm 3.2. nm) distribution of standard deviation re<sup>fl</sup>ects changes in the parameter values detailed in Table 2. The green (Algorithm 3.1. np) distribution of the standard deviation, which corresponds to networks generated with algorithm 3.1, re<sup>fl</sup>ects both changes in the parameter values and a higher variability of the node degrees due to the design of algorithm 3.1 itself.

## 4.2. quantitative assessment of stability

Next, we assess the stability of connectivity patterns of the network types to the alternative algorithms used to generate networks of a given type. The values reported are <sup>fi</sup>ve-fold cross-validated errors in a classi<sup>fi</sup>cation task: the lower the error is, the less stable connectivity patterns are, since a slight variation in the sampling algorithm leads to distinguishable sets of measurements.

Random. Using the set of metrics, we can discriminate almost exactly which type of network was generated by which algorithm. The extremal statistics (min and max) are very powerful discriminators in this case. The area under the Receiver Operating Characteristic (ROC) curve is about 1 and the classi<sup>fi</sup>cation error is about 0.00%. Core periphery. Using the set of metrics, we cannot discriminate which type of network was generated from which algorithm. The classi<sup>fi</sup>cation error is about 50% and the area under the ROC curve is 0.501.

![](/api/attachments/JVJHE3QM/fulltext/images/d93c02715fe8a8c55543289779b67c2833b073b2a54671dd48a6f4bb23125efb.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/b13015424ae61bbe488b0845b326627bc84a94152ae50d973d9f64e551fdd756.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/25b002b7907f862bd0604102214541cf14b278004c037d5c41b6ea7945a89070.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/06ba31cc9e5ec4440137761204801bcba844fab8780f26e182428e161b2332ed.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/49c31f66c1a74b44604c41d92bdb452a808753fc751ecb5d8059858915dcd759.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/a0df08f3cdd357e1471da2c23a74489eaf261d4ee5c030e48941e244257dfebe.jpg)  
Fig. 9. Cellular: empirical distributions of the 47 metrics we consider, excluding shortest path. The distributions were estimated using the sample of cellular networks generated by to algorithms 6.1 (nkpq) and 6.2 (nkpqr) in the experimental design in Table 2.

Cellular. Using the set of metrics, we can discriminate fairly well which type of network was generated from which algorithm. The area under the ROC curve is 0.928 and the classi<sup>fi</sup>cation error is 17.64%.

Scale free. Using the set of metrics, we can discriminate almost exactly which type of network was generated from which algorithm. The area under the ROC curve is about 1 and the classi<sup>fi</sup>cation error is 0.07%. Small world. Using the set of metrics, we can barely discriminate which type of network was generated from which algorithm. The area under the ROC curve is not available because this is a three-way classi<sup>fi</sup>cation problem. The three-way classi<sup>fi</sup>cation error is 24.78% (the base error is at 33.33%). Pairwise classi<sup>fi</sup>cation errors are presented in Table 3. Compared to the base error rate of 50%, the pairwise classi<sup>fi</sup>cation results suggest that any pair of the alternative sampling algorithms yield distinguishable sets of small-world networks.

## 4.3. Qualitative assessment of separability

To explore the variability in the network metrics induced by different network types, we look at the empirical distributions of the

![](/api/attachments/JVJHE3QM/fulltext/images/ae344051d7d06eff5fe5c271547d1bc0badb95942a294efee57209bfa9c90e46.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/22201ee4df7368e95a396ffbdb41c2ba66e06b219f413502229df71c7bcb7820.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/98928ed8bae04589ae06691d1aa5bd18b193823edf094b24d172d24a9079d7fd.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/e70311a780404a6ba3da5626fc39a2e2e0b57a5249d580bcdac72a498c1174f3.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/375159b87f84226bc085cd5806a1f8f80a5f29eef787a8dd602356477753af2e.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/2ef1168d0dba9776867a8c6361f917c8a5fa729ea888b5412505b1546f986b86.jpg)  
Fig. 10. Scale-free: empirical distributions of the 47 metrics we consider, excluding shortest path. The distributions were estimated using the sample of scale-free networks generated by algorithms 4.1 (nipi) and 4.2 (nmr) in the experimental design in Table 2.

47 metrics without distinguishing which networks were generated by which algorithms, in Fig. 13. This Figure has 47 panels, each panel corresponding to a metric, clearly labeled at the top as in the previous set of Figures. In each panel, we plot multiple density estimates in different colors, each density corresponding to one of the network types, without distinguishing the sampling algorithm used. A legend that speci<sup>fi</sup>es which color corresponds to which network type in Table 2 is given in the bottom right panel.

This analysis provides a <sup>fi</sup>rst look at the separability issue of network types, as described in Section 2.2 and illustrated in the right panel of Fig. 1 and to what extent algorithms for a new network type actually generate networks (in terms of their connectivity properties) that existing network types cannot generate. In the right panel of Fig. 1 a small intersection would be desirable, as it would suggest a substantial difference among the six network types we consider. In the context of Fig. 13, a small intersection in the distributions for each of the metrics would be desirable, as the differences would lead to better separability among network types. However, the plots in Fig. 13 show that such differences are distinguishable in some metric distributions (e.g., the average degree centrality, connectedness, and hierarchy) while similar in others (e.g., the standard deviation of inverse centrality and max closeness centrality), suggesting that different network types are only separable in terms of some network metrics, not in others.

As a speci<sup>fi</sup>c example, in Fig. 13, the third panel on the top row plots six empirical distributions of average degree centrality corresponding to the six network types we consider. This measure of centrality takes very different values across network types, which suggests that the six network types are different in terms of those properties of the connections that in<sup>fl</sup>uence degree centrality. However, this metric is one of the few metrics with respect to which the network types are fairly different. The six distributions tend to be more similar than not in most of the other panels. For instance, consider the clustering coef<sup>fi</sup>cient in the seventh panel on the third row, or the effective network size in the <sup>fi</sup>fth panel on the fourth row. According to these metrics the network types are not very different. This suggests that the six network types are more similar than not in terms of those properties of the connections that in<sup>fl</sup>uence most metrics.

![](/api/attachments/JVJHE3QM/fulltext/images/aaa8b10915be1bd6d300b395aa97ebb4db85e721e9a9a32e555e90e419442e50.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/66dc4350d022f56aff84c1a85637fe80e90a5b1c2c901a30100319843c656762.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/61f7d9c3ccf9849cd07eadd7ebf91507f2e7ec296c796c4967089cf402edc6c8.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/790e0d49a8b4c5d00a768563678d36df722822454b6df7c33b64d46e1a2ea50e.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/555d3389963daaf6eeac4b5c7a46cd98b2ca3fe849633a651617e7f9c201fda6.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/2130d879fd06ea3c1edcabcbb6e0638f09919c0ea672d9a37b97c7b2d5a4e399.jpg)  
Fig. 11. Core–periphery: empirical distributions of the 47 metrics we consider, excluding shortest path. The distributions were estimated using the sample of core–periphery networks generated by algorithms 5.1 (npi-uni) and 5.2 (npi-prf) in the design in Table 2.

## 4.4. Quantitative assessment of separability

Finally, we assessed the separability of sampling algorithms for different network types. Table 4 summarizes the <sup>fi</sup>ve-fold crossvalidated errors in the corresponding classi<sup>fi</sup>cation tasks. Diagonal cells replicate the stability results discussed above. Off-diagonal cells quote separability results. The lower the error is, the more separable connectivity patterns are, since the instances of different pure types entail distinguishable sets of metrics.

In Table 4, we quote the cross-validate classi<sup>fi</sup>cation errors. The off-diagonal element (i, j) is the error in classifying networks of type i from networks of type j. Since network types i and j are different

Table 3  
![](/api/attachments/JVJHE3QM/fulltext/images/16b1135966ade974698dd8d567ddb3d2c35fa17103da0a7b997f97395a805aab.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/6c192bf840e61b7a1c91b5d56e22706b718bb161c5f570960cd5d6faf89668b3.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/f0114e046348fd70e22704c0861ad8c3824072623c7191ebcbb35349e9e0ad0c.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/3f911640a29fdf943f15aa2fc1cf566cdb2865e4b70634748cea4664537f3816.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/24fce3990074b0bb89d3e7b1f78b8d9a283ba0dedb6a84e411dab8d80dc8cffd.jpg)

![](/api/attachments/JVJHE3QM/fulltext/images/412a5e4d2f8d2ccb5c91f7b0031a00732b1bdcd29bfe6f6212ee2aad0919ca0f.jpg)  
Fig. 12. Small-world: empirical distributions of the 47 metrics we consider, excluding shortest path. The distributions were estimated using the sample of small-world networks generated by algorithms 2.1 (nkp), 2.2 (nklr) and 2.3 (nkpqr) in the design in Table 2.

for off diagonal entries, low error is desirable. It means that network types i and j are separable. The diagonal element (i,i) is the error in classifying networks of type i generated with different sampling algorithms. Note that the top-left element (RL,RL) is not available, since we only consider one sampling algorithm for regular lattice networks. Since there is only one network type i for diagonal entries, high error is desirable. It means that networks generated by alternative sampling algorithms are not separable, thus leading to a consistent de<sup>fi</sup>nition of the network type.

Pairwise classi<sup>fi</sup>cation error of small-world sampling algorithms.

<table><tr><td></td><td>SW 1.</td><td>SW 2.</td><td>SW 3.</td></tr><tr><td>SW 1.</td><td>-</td><td>16.04%</td><td>21.12%</td></tr><tr><td>SW 2.</td><td>-</td><td>-</td><td>13.31%</td></tr></table>

Table 4 suggests that cellular, core–periphery and scale-free types are weakly separable (26.45%, 33.33% and 37.15% error), and share common connectivity patterns with random types (2nd row; 27.94%, 32.55%, and 25.00%). These types are separable from small-world networks (3rd row, 8.66%, 13.12%, and 5.31%) that, in turn, share a set of different connectivity patterns with random types (41.22%). Note that, key differences between cellular, core–periphery, scale-free and random are that (a) the differences are more apparent at moderate density (approximately 25% range) and (b) certain metrics can be used to separate these four types of networks.

![](/api/attachments/JVJHE3QM/fulltext/images/fec528c22becaa56eec02f040bef72538b5fc67224e5697ee57b1ad2f0338c32.jpg)  
Fig. 13. Six network types: empirical distributions of the 47 metrics we consider, excluding shortest path. The distributions were estimated using the entire sample of networks generated according to all the algorithms in the experimental design of Table 2.

## 5. Discussion

The computational results on stability suggest that all of the studied network sampling methods are fairly simple. These methods

## Table 4

Classi<sup>fi</sup>cation error on different network types. The column labels are: RL for ringlattice, Rnd for Erdös random, SW for small-world, SF for scale-free, Cel for cellular and CP for core–periphery.

<table><tr><td></td><td>RL</td><td>Rnd</td><td>SW</td><td>SF</td><td>Cel</td><td>CP</td></tr><tr><td>RL</td><td>-</td><td>27.00%</td><td>7.45%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td></tr><tr><td>Rnd</td><td></td><td>0.00%</td><td>41.22%</td><td>27.94%</td><td>32.55%</td><td>25.00%</td></tr><tr><td>SW</td><td></td><td></td><td>24.78%</td><td>8.66%</td><td>13.12%</td><td>5.31%</td></tr><tr><td>SF</td><td></td><td></td><td></td><td>0.07%</td><td>26.45%</td><td>33.33%</td></tr><tr><td>Cel</td><td></td><td></td><td></td><td></td><td>17.64%</td><td>37.15%</td></tr><tr><td>CP</td><td></td><td></td><td></td><td></td><td></td><td>50.00%</td></tr></table>

may entail “no variability” for a speci<sup>fi</sup>c metric over a fairly large range of parameter values, or by construction, e.g., all instances of an Erdös random (n,m) have the same number of edges, i.e., m. While these algorithms are of theoretical value and help us grasp insights about phenomena of interest, they may lead to unreliable statistical tests (e.g., highly variable p-values) in practice. This is because rich variability pro<sup>fi</sup>les are crucial in determining the stability of connectivity patterns of a pure type to alternative sampling algorithms that generate it. In other words, low variability pro<sup>fi</sup>les lead to high sensitivity of connectivity patterns, as captured by the metrics of interest, and ultimately to high sensitivity of relevant statistics to the speci<sup>fi</sup>c version of the algorithms adopted. For example, the variability pro<sup>fi</sup>le of the clustering coef<sup>fi</sup>cient is extremely sensitive to the speci<sup>fi</sup>c algorithm used to sample both random and scale-free types. As a consequence the p-value, e.g., of small-world-ness, will vary. A simple suggestion to overcome this problem is to sample network types according to different algorithms, and then to mix the networks. This directly aims at increasing the variability pro<sup>fi</sup>les of the metrics of interest, and possibly leads to more robust parameter estimations.

Overall, we <sup>fi</sup>nd low stability and low separability. Alternative sampling algorithms that we considered for the same type appear similar. Yet the connectivity patterns they yield are neither consistent to alternative algorithms, nor separable across different network types. The low stability (not desirable) is likely to be a consequence of the fact that the algorithms are too simple and do not lead to rich enough variability pro<sup>fi</sup>les for the metrics of interest. In fact, we <sup>fi</sup>nd that the extremal statistics (min and max) have high information gain with respect to the network type categories, and drive the classi<sup>fi</sup>cation in several cases. The low separability (not desirable) means that pure types are stylized models of behavior at the sampling level, which lead to networks that share connectivity patterns, as captured by the network metrics of interest. Aside from the simplicity of the algorithms, this is consistent with what we would expect to see in the real world, i.e., observed networks display multiple stylized behaviors to different degrees. This translates into the more realistic hypothesis of “mixtures of types,” at the sampling level, as a better starting point for developing models and algorithms for network analysis.

## 5.1. Open issues in network model selection

The problem we addressed in this paper is an instance of the network model selection problem in statistics, i. e., how to select a most appropriate network model M for an observed network G? A model M speci<sup>fi</sup>es a probability distribution $P _ { M } ( G | \Theta )$ on space of possible networks G giving some parameters Θ. The model selection problem amounts to determining which model best <sup>fi</sup>ts the observed network among a set of models.

The current practice to select a network model is the following [e.g., see Ref. 32]. Consider an observed network G and a candidate statistical model M. The observed network is represented as a set of network metrics $t _ { M } ( G )$ . Using these metrics, optimal values of the parameters $\hat { \Theta }$ are estimated, then a large number B of networks $G _ { 1 : B }$ are generated from the probability distribution $P _ { M } \Big ( G | \hat { \Theta } \Big )$ . Finally, an overall p-value of the observed network is computed. The overall p-value of the observed network is informative about how unexpected the connectivity pattern is, with respect to the expected pattern under the candidate model M. Lower p-values indicate that the observed network is more unusual under the model M. This sequence of steps is repeated for a set of models. The model that best <sup>fi</sup>ts the connectivity pattern of the observed network is chosen.

There are two issues with the current practice outlined above. The procedures to estimate the optimal parameter values Θ<sup>ˆ</sup> lack a sound statistical basis. The metrics used in the estimation procedure $t _ { M }$ may not carry suf<sup>fi</sup>cient information about a candidate model M.

To estimate optimal parameter values $\begin{array} { r } { \hat { \Theta } , } \end{array}$ for instance, a typical procedure identi<sup>fi</sup>es the values of the parameters that match the empirical values network metrics $t _ { M } ,$ such as average number of interaction per individual, to the expected value of these metrics computed using the candidate model M. The full speci<sup>fi</sup>cations of probability distribution $P _ { M }$ are used to compute expectations, thus linking Θ to the observed network data. A more principled estimation procedure would be to <sup>fi</sup>nd the values of the parameters that best explain the observed network data, for instance, by maximizing the probability of the data $P _ { M } ( G | \Theta )$ with respect to Θ. Another option would be to set expectations on the parameters in terms of a probability distribution P(Θ) to <sup>fi</sup>nd the values of the parameters that are most likely given the data, by maximizing $P _ { M } ( \Theta | G )$ with respect to Θ. These estimation procedures would correspond to maximum likelihood and maximum a-posteriori estimation [38].

Another fundamental issue is the choice of the metrics that quantitatively summarize the interaction data and inform the estimation of the parameters. In principle, we should estimate the parameters of a model $P _ { M } ( G | \Theta )$ using a set of metrics $u _ { M } ( G )$ that are suf<sup>fi</sup>cient to characterize G [13]. That is, we should use metrics that carry all the information about the network that is necessary to estimate the parameters in a candidate model $P _ { M } .$ Each model, $P _ { M }$ corresponds to a speci<sup>fi</sup>c set of metrics $u _ { M }$ that are suf<sup>fi</sup>cient statistics. Statistical network analysis, however, is still in its infancy. It is often infeasible to compute or even write down the likelihood $P _ { M }$ for a given model M. Often, we cannot tell what set of metrics $u _ { M }$ is suf<sup>fi</sup>cient to estimate the parameters in a given model [29].

In practice, as reported above, each statistical model characterizes networks in terms of speci<sup>fi</sup>c metrics $t _ { M } ( G )$ . Community-based models, such as the cellular networks, portray interactions in which individuals work in tight teams, most often interacting with other team members and occasionally interacting with other teams [35]. Centralized models, such as core–periphery networks, portray interactions in which most individuals report to a central <sup>fi</sup>gure and seldom interact with one another [1,37]. Current estimation practice leverages the purported correspondence between a given network model and a speci<sup>fi</sup>c set of metrics $t _ { M } .$ . Parameters are estimated using only the information about the network captured by $t _ { M } ,$ according to the procedures outlined above. However, there may be a substantial difference between the information captured by the arbitrary set of metrics $t _ { M }$ and the information captured by the metrics set $u _ { M } ,$ that is, $t _ { M }$ may be highly insuf<sup>fi</sup>cient for summarizing the information of an observed network. In the current literature, the metrics t associated to models $P _ { M }$ are typically one or two. The small-world model, for example, is characterized in the literature in terms of metrics t quantifying diameter and clustering coef<sup>fi</sup>cient [40]. Estimating the parameters of the small-world model using the limited information captured by $t _ { M }$ is problematic, and leads to unstable p-values and suboptimal decisions.

## 6. Conclusion

In this paper, we performed statistical analysis of the stability of the network sampling methods and the separability of different network types as captured by a set of network metrics that are widely adopted in the social and physical sciences. Contrary to the widespread assumptions in research, we found that the sampling algorithms considered are neither stable to alternative speci<sup>fi</sup>cations, nor separable in terms of the connectivity patterns they entail. The lack of stability is a cause for concern. We encourage the practitioners who employ the simple sampling algorithms discussed in this paper to consider more variable schemes, such as mixtures, in order to obtain more robust network modeling parameters in general. The lack of separability was somewhat anticipated, as real world networks hardly present the variability pro<sup>fi</sup>le of a single pure network type. Our results support the assumption of mixtures of network types as an alternative starting point for developing models and algorithms for network analysis [e.g. 2]. Developing novel network metrics and exploring alternative network representations grounded in scienti<sup>fi</sup>c theories are promising directions for future research, which may transform the way we do network analysis today.

## Acknowledgments

This work was partially supported by the National Institutes of Health under grant no. R01 AG023141-01, by the Of<sup>fi</sup>ce of Naval Research under contract no. N00014-02-1-0973 and N000140811186, by the National Science Foundation under grant no. IIS-0218466, and by the Department of Defense, all to Carnegie Mellon University, and by the National Science Foundation under grants no. DMS-0907009 and no. IIS-1017967, by the National Institute of Health under grant no. R01-GM096193, and by the

Army Research Of<sup>fi</sup>ce Multidisciplinary University Research Initiative under grant no. 58153-MA-MUR all to Harvard University. Additional support was provided by the Center for Computational Analysis of Social and Organizational Systems (CASOS) at Carnegie Mellon University. The views and conclusions contained in this document are those of the authors and should not be interpreted as representing the of<sup>fi</sup>cial policies, either expressed or implied, of the National Institute of Health, the Of<sup>fi</sup>ce of Naval Research, the National Science Foundation, or the U.S. government.

## References

[1] M.A. Ahuja, K.M. Carley, Network structure in virtual organizations, Organization Science 10 (6) (1999) 741–757.

[2] E.M. Airoldi, D.M. Blei, S.E. Fienberg, E.P. Xing, Mixed membership stochastic blockmodels, Journal of Machine Learning Research 9 (2008) 1981–2014.

[3] E.M. Airoldi, K.M. Carley, Sampling algorithms for pure network topologies: stability and separability of metric embeddings, ACM SIGKDD Explorations 7 (2) (2005) 13–22.

[4] E.M. Airoldi, W.W. Cohen, S.E. Fienberg, Bayesian models for frequent terms in text, Proceedings of the Classi<sup>fi</sup>cation Society of North America and INTERFACE Annual Meetings, 2005.

[5] R. Albert, A.L. Barabasi, Statistical mechanics of complex networks, Reviews of Modern Physics 74 (47) (2002).

[6] A. Bajaj, R. Russell, Awsm: allocation of work<sup>fl</sup>ows utilizing social network metrics, Decision Support Systems 50 (1) (2010) 191–202.

[7] A.L. Barabasi, R. Albert, Emergence of scaling in random networks, Science 286 (1999) 509–512.

[8] B. Bollobás, Random Graphs, 2nd edition, Academic Press, New York, 2001.

[9] S.P. Borgatti, R. Cross, A relational view of information seeking and learning in social networks, Management Science 49 (4) (2003) 432–445.

[10] S.P. Borgatti, M.G. Everett, Models of core/periphery structures, Social Networks 21 (1999) 375–395.

[11] K.M. Carley, J. Diesner, J. Reminga, M. Tsvetovat, Toward an interoperable dynamic network analysis toolkit, Decision Support Systems 43 (4) (2007) 1324–1347.

[12] K.M. Carley, J. Reminga, ORA: organizational risk analyzer, Technical Report CMU-ISRI-04-106, Carnegie Mellon University, 2004.

[13] G. Casella, R.L. Berger, Statistical inference, 2nd edition, Duxbury Press, 2002

[14] N.A. Christakis, J.H. Fowler, Connected: The Surprising Power of Our Social Networks and How They Shape Our Lives, Little, Brown and Company, 2009.

[15] P.S. Dodds, D.J. Watts, C.F. Sabel, Information exchange and the robustness of organizational networks, Proceedings of the National Academy of Sciences 100 (21) (2003) 12516–12521.

[16] D. Easley, J. Kleinberg, Networks, Crowds, and Markets: Reasoning About a Highly Connected World, Cambridge University Press, 2010.

[17] P. Erdös, A. Rényi, On random graphs, Publicationes Mathematicae Debrecen 5 (1959) 290–297.

[18] T. Frantz, K.M. Carley, A formal characterization of cellular networks, Technical Report CMU-ISRI-05-109, School of Computer Science, Canregie Mellon University, 2005.

[19] E.N. Gilbert, Random graphs, Annals of Mathematical Statistics 30 (1959) 1141-1144

[20] A. Goldenberg, A.X. Zheng, S.E. Fienberg, E.M. Airoldi, A survey of statistical network models, Foundation and Trends in Machine Learning 2 (2) (2010) 1–117.

[21] M.S. Handcock, M. Morris, A simple model for complex networks with arbitrary degree distribution and clustering, Workshop on Statistical Network Analysis Lecture Notes in Computer Science, Springer, 2007, pp. 103–114.

[22] F. Harary, Graph theoretic methods in the management sciences, Management Science 5 (4) (1959) 387–403.

[23] T. Hastie, R. Tibshirani, J.H. Friedman, The Elements of Statistical Learning: Data Mining, Inference, and Prediction, Springer-Verlag, 2001.

[24] M.O. Jackson, Social and Economic Networks, Princeton University Press, 2008.

[25] M. Keith, H. Demirkan, M. Goul, The in<sup>fl</sup>uence of collaborative technology knowledge on advice network structures, Decision Support Systems 50 (1) (2010) 140–151.

[26] C. Kiss, M. Bichler, Identi<sup>fi</sup>cation of in<sup>fl</sup>uencers—measuring in<sup>fl</sup>uence in customer networks, Decision Support Systems 46 (1) (2008) 233–253.

[27] J. Kleinberg, The small-world phenomenon: an algorithmic perspective, Technical Report 99-1776, Department of Computer Science, Cornell University, 1999.

[28] J. Kleinberg, Navigation in a small world, Nature 845 (2000).

[29] E.D. Kolaczyk, Statistical Analysis of Network Data: Methods and Models, Springer, 2009.

[30] G. Kossinets, D.J. Watts, Empirical analysis of an evolving social network, Science 311 (2006) 88–90.

[31] A. Mayer, Online social networks in economics, Decision Support Systems 47 (3) (2009) 169–184

[32] M. Middendorf, E. Ziv, C.H. Wiggins, Inferring network mechanisms: the Drosophila melanogaster protein interaction network, Proceedings of the National Academy of Sciences 102 (9) (2006) 3192–3197.

[33] S. Milgram, The small world phenomenon, Psychology Today 1 (61) (1967).

[34] M.E.J. Newman, D.J. Watts, S.H. Strogatz, Random graph models of social networks, Proceedings of the National Academy of Sciences 99 (2002) 2566–2572.

[35] W. Oh, S. Jeon, Membership herding and network stability in the open source community: the Ising perspective, Management Science 53 (7) (2007) 1086–1101.

[36] S. Shane, D. Cable, Network ties, reputation, and the <sup>fi</sup>nancing of new ventures, Management Science 48 (3) (2002) 364–381.

[37] G. Walker, B. Kogut, W. Shan, Social capital, structural holes and the formation of an industry network, Organization Science 8 (2) (1997) 109–125.

[38] L. Wasserman, All of Statistics, Springer-Verlag, 2004

[39] S. Wasserman, K. Faust, Social Network Analysis: Methods and Applications, Cambridge University Press, 1994.

[40] D.J. Watts, S.H. Strogatz, Collective dynamics of “small-world” networks, Nature 393 (1998) 440–442.

[41] B. Zhu, S.A. Watts, Visualization of network concepts: the impact of working memory capacity differences, Information Systems Research 21 (2) (June 2010) 327–344.

Dr. Edoardo M. Airoldi is an Assistant Professor of Statistics at Harvard University. He is also a member of the Center for Systems Biology in the Faculty of Arts and Sciences at Harvard University. He received a PhD degree in Computer Science from Carnegie Mellon University. He was a postdoctoral fellow at Princeton University, in the Lewis-Sigler Institute for Integrative Genomics, and the Department of Computer Science. His research interests include statistical methodology and theory for the analysis of complex networks and random graph dynamics, with application to the social and biological sciences.

Dr. Xue Bai is an Assistant Professor of Management Information Systems in the Department of Operations and Information Management, University of Connecticut. She received her PhD degree in Management Information Systems from Carnegie Mellon University. Her research includes data mining and machine learning methods applied to text classi<sup>fi</sup>cation, sentiment extraction, online marketing analysis and clinical diagnosis, Another area of her research is in the application of optimization methods to data quality and information security associated risks in enterprise systems.

Dr. Kathleen M. Carley is a Professor of Computation, Organizations and Society in the Institute for Software Research Department in the School of Computer Science at Carnegie Mellon and the director of the Center for Computational Analysis of Social and Organizational Systems (CASOS). Her research combines cognitive science, social networks and computer science to address complex social and organizational problems. Her speci<sup>fi</sup>c research areas are dynamic network analysis, computational social science, agent based modeling, and the dispersion of information, disease, and beliefs. She and members of her center have developed technologies for extracting, analyzing, and assessing change in networks through space and time.
