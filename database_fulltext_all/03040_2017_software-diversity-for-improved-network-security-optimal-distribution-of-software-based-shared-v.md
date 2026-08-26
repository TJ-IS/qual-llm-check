---
otero_id: 3040
otero_key: "YSR6BWKM"
title: "Software Diversity for Improved Network Security: Optimal Distribution of Software-Based Shared Vulnerabilities"
authors: "Orcun Temizkan; Sungjune Park; Cem Saydam"
year: "2017"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0722"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/YSR6BWKM/fulltext/images/810416d9218a5c605a4afc46abe9b410bc4a8b34a0bdca020cc41482a5e675d6.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Software Diversity for Improved Network Security: Optimal Distribution of Software-Based Shared Vulnerabilities

Orcun Temizkan, http://orcid.org/0000-0001-7482-4553Sungjune Park, Cem Saydam

To cite this article:

Orcun Temizkan, http://orcid.org/0000-0001-7482-4553Sungjune Park, Cem Saydam (2017) Software Diversity for Improved Network Security: Optimal Distribution of Software-Based Shared Vulnerabilities. Information Systems Research

Published online in Articles in Advance 31 Aug 2017

https://doi.org/10.1287/isre.2017.0722

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2017, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/YSR6BWKM/fulltext/images/1ea0418b88eeba93ce28f4ec0d8642e16f549cd08c6774238fa9b0090585ddee.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Software Diversity for Improved Network Security: Optimal Distribution of Software-Based Shared Vulnerabilities

Orcun Temizkan,<sup>a</sup> Sungjune Park,<sup>b</sup> Cem Saydam<sup>b</sup>

<sup>a</sup> Faculty of Business, Ozyegin University, 34794 Cekmekoy, Istanbul, Turkey; <sup>b</sup> Belk College of Business, University of North Carolina at Charlotte, Charlotte, North Carolina 28223

Contact: orcun.temizkan@ozyegin.edu.tr (OT); supark@uncc.edu, http://orcid.org/0000-0001-7482-4553 (SP); saydam@uncc.edu (CS)

Received: August 1, 2014 Revised: January 2, 2016; August 30, 2016; February 8, 2017 Accepted: April 11, 2017 Published Online in Articles in Advance: August 31, 2017

https://doi.org/10.1287/isre.2017.072

Copyright: © 2017 INFORMS

Abstract. Firms, and other agencies, tend to adopt widely used software to gain economic benefits of scale, which can lead to a software monoculture. This can, in turn, involve the risk of correlated computer systems failure as all systems on the network are exposed to the same software-based vulnerabilities. Software diversity has been introduced as a strategy for disrupting such a monoculture and ultimately decreasing the risk of correlated failure. Nevertheless, common vulnerabilities can be shared by diferent software products. We thus expand software diversity research here and consider shared vulnerabilities between diferent software alternatives. We develop a combinatorial optimization model of software diversity on a network in an efort to identify the optimal software distribution that best improves network security. We also develop a simulation model of virus propagation based on the susceptible-infected-susceptible model. This model allows calculation of the epidemic threshold, a measure of network resilience to virus propagation. We then test the efectiveness of the proposed software diversity strategies against the spreading of viruses through a series of experiments.

History: Sanjeev Dewan, Senior Editor; Wolfgang Ketter, Associate Editor. Funding: This research was funded in part by the 2012 Belk College Summer Research Grant.

Keywords: software diversity • shared vulnerabilities • epidemic spreading • epidemic threshold • network security • combinatorial optimization simulation

## 1. Introduction

The security of information systems has become a significant concern since cyberattacks/hacking have caused substantial financial losses to a wide number and variety of users (Schneider 2012). The increasing dependence on computer networks for business continuity has brought managerial attention to the management of risk resulting from the failure of computer networks. Understandably, the security of computer networks has attracted significant attention, particularly because many real-world information systems are organized within a network, and thus share selected software components for purposes of economic benefit.

This use of common components throughout a network can understandably lead to a sharing of the same, or similar, vulnerabilities. At the same time, the deployment of security technologies such as firewalls, intrusion detection systems, and antivirus software can reduce the likelihood of successful exploitation of vulnerabilities on a local scale; importantly, though such interventions neither eliminate existing vulnerabilities (Bailey 2005, Chen et al. 2011) nor eradicate the epidemic on a global scale (Pastor-Satorras and Vespignani 2002a). Self-propagating malware such as a computer worm spreads to many independent, but interconnected systems, which are often running software applications that contain a common vulnerability (August et al. 2014). Given the current rising importance of cloud computing, such infected systems on a cloud service infrastructure can easily incur substantial costs to both the provider and the customer.

Furthermore, the continued growth of the Internet of things (IoT) could actually accelerate the propagation of malware because a majority of infected IoTs, for example, police body cameras and networked sensors, may not be equipped with proper protections such as antivirus software (Nichols 2015). Thus, there is a need to make computer networks more resilient/resistant to correlated failures because of security attacks, and, in particular, viruses and worms.

As early as 2003, Wagner and Pescatore of Gartner Research wrote an article in ComputerWeekly entitled “Use more than one operating system to limit the impact of malicious code attacks,” which ofered software diversity as one strategy in which organizations might improve their network’s resilience (Wagner and Pescatore 2003). According to Gartner’s research “enterprises that maintain 20% of their desktops on alternative platforms will experience a 50% reduction in the scope of the business impact of worm attacks.” In such findings, they acknowledged the costs and challenges of managing multiple operating systems (OSs) on the network, and thus concluded that “targeted adoption of a heterogeneous computing environment ofers significant values for some enterprises.”

More recently, Williams et al. (2009, p. 26) wrote “. . . One major threat to our networked infrastructure’s resilience is the software monoculture, the cyber analog of ‘putting all your eggs in the basket.’ ” Gorbenko et al. (2011) showed that Infrastructure as a Service (IaaS) cloud providers can greatly reduce the system’s days of risk by switching between diverse commercial of-the-shelf (COTS) software products such as OS, database management system (DBMS), and web server. Their approach leverages natural diversity of the COTS with dynamic configuration strategies. A software diversity approach for network security can be further extended to other applications because of recent developments in creating such software. Larsen et al. (2014), in fact, present up-to-date methods for creating functionally equivalent diverse software applications such as compile-time diversification and binary rewriting approaches.

Software diversity can be used to break up software monoculture by isolating shared vulnerabilities among computer systems and, eventually, decreasing their exposure to correlated failures (Bailey 2005, Chen et al. 2011). This approach can be efective given that more and more viruses and worms go undetected by antivirus software for extended periods of time (Sukwong et al. 2011). A more desirable form of software diversity can be created by deploying multiple, functionally equivalent programs that have independent probabilities of failure (Bailey 2005, Birman and Schneider 2009, Cox et al. 2006). An exploitation of correlated vulnerabilities would thus be confined to limited segments of a network. Although this approach assumes that diferent software programs do not share the same vulnerabilities, this may not be the case (Alhazmi et al. 2007, Chen et al. 2011, Lala and Schneider 2009). The implication is that any software diversity model should be expanded to consider shared vulnerabilities between diferent software alternatives.

Interestingly, the propagation of viruses or worms on networks has been studied using several epidemic models. The susceptible-infected-susceptible (SIS) model, for example, has been widely used for the study of epidemics leading to an endemic state with a stationary value for the prevalence of infected individuals, i.e., the degree to which the epidemic is widespread in the afected population (Bailey 1975). Hence, in the scenario of interest here, an epidemic threshold can be introduced as a measure of the network’s resilience to the spreading of an epidemic. Prior research has shown the impact of a network topology on epidemic spreading (Bailey 2005, Barthelemy et al. 2005, Pastor-Satorras and Vespignani 2001a, Wang and Chen 2003, Wang et al. 2003), and indicated the absence of an epidemic threshold in scale-free networks, such as the Internet (Moreno et al. 2002; Pastor-Satorras and Vespignani 2001a, b). The literature widely notes that it is efectively impossible to eradicate viruses or worms from scale-free networks (Barabási and Bonabeau 2003). This suggests that scale-free networks are an efective medium for the propagation and persistence of epidemics. Although the impact of immunizations on epidemic spreading has been studied in scale-free networks (Pastor-Satorras and Vespignani 2008), there has been no such research that examines the impact of software diversity on virus propagation in the presence of shared vulnerabilities.

We thus argue that software diversity increases the epidemic threshold in scale-free networks, and makes them more resilient to virus propagation. In this spirit, the current study develops a model that can create software diversity on a network of computer systems (nodes) by optimally distributing multiple software alternatives to the nodes of that network. It then examines, via simulation, the efectiveness of the proposed model against the spread of viruses. We demonstrate that our model can significantly improve the epidemic threshold of scale-free networks while it is suficiently general to allow for application to diferent types of networks. The model assumes that vulnerabilities are shared among a series of selected software alternatives. Yet, despite this condition, it provides an optimal solution to the problem of correlated failures within a network of computer systems by identifying a “best” plan for the distribution of those software alternatives.

For example, a cloud service provider may achieve substantial security gains by deploying Redhat Linux Server and Windows Server 2003 OSs for their network as they share the fewest common vulnerabilities (Garcia et al. 2011). However, an optimal distribution of Redhat Linux Server and Solaris Server OSs, which share more common vulnerabilities than the best set of software alternatives, can also provide efective network security.

A software alternative can also be interpreted as a set of software products, instead of a single software product, which provides the same functionality in a network node. It may also refer to a software configuration where a single software product can be exposed to diferent vulnerabilities depending on its features that are turned on, e.g., enabling or disabling certain types of script to run for a browser or an email client, changing antivirus scan settings for a host, requiring diferent authentication policies, etc.

In designing and testing our proposed software diversity model, the current research efort consists of two stages: The first involves formulating two combinatorial optimization models of software diversity on a network. Two linear programming (LP) models are developed to identify an optimal software distribution that can improve network security. We also develop a software diversity index, and compare the performances of various software distribution solutions. The proposed software distribution model is, to our knowledge, the first attempt to provide security decision makers with a strategy for better managing their software selection and deployment processes when products with practically identical functional capabilities share common vulnerabilities. We also developed a dynamic software allocation algorithm to accommodate growing networks. The epidemic threshold is then used in the second stage as an ultimate performance measure of network resilience to security attacks.

The second stage of our research examines the efectiveness of selected software distributions through a simulation model of virus propagation. The model is an extended version of SIS in which the shared vulnerabilities between software alternatives are explicitly considered. We then compare the impacts of software diversity created by the LP models with that resulting from the targeted distribution strategy (Pastor-Satorras and Vespignani 2008).

The current study thus contributes to the literature by proposing an information-theory-based optimization approach to improve network security. This approach is the first that combines software diversity and virus propagation in the presence of shared vulnerabilities. In addition, our approach uses an LP model to improve network resilience that can be implemented via of-the-shelf solvers such as CPLEX. We show that the resulting optimized software diversity using our model significantly improves network security in terms of an epidemic threshold. For all combinations of experimental conditions, our LP model solutions were found to outperform targeted distribution solutions.

The remainder of the paper is organized as follows. Section 2 reviews the relevant literature, while Section 3 presents the proposed models in detail. Section 4 describes a series of model-based experiments and presents the results. Managerial implications of the results and discussions are presented in Section 5. Section 6 provides conclusions, limitations of the study, and possible directions for future research.

## 2. Literature Review

There are two main streams of research that contribute to the current study. The first is related to software diversity, while the second deals with the spreading of virus epidemics on computer networks.

## 2.1. Software Diversity

Earlier research on software diversity (Eckhardt and Lee 1985, Hughes 1987, Littlewood and Miller 1989, Partridge and Krzanowski 1997) focused on increasing the reliability of computer systems. In this regard,

N-version diversity is the design that seeks to increase software reliability by building redundant systems (Littlewood et al. 2001). Similar to this approach, distinct and coincident failure diversities were developed (Eckhardt and Lee 1985, Hughes 1987, Littlewood and Miller 1989, Partridge and Krzanowski 1997). Both use a voting decision strategy that makes a decision based on the majority votes of multiple, functionally equivalent programs. Results from these studies suggest that a diverse system is more reliable than any single version system (Partridge and Krzanowski 1997). This view is supported by Zhang et al. (2001) who also found that heterogeneity is a critical factor in eforts to increase the survivability of a network.

From an economic perspective, market dynamics such as network externalities are the driving force underlying a firm’s decisions on technology adoption (Brynjolfsson and Kemerer 1996; Chen et al. 2011; Katz and Shapiro 1985, 1986). Organizations thus tend to adopt software that has larger market shares to gain economic benefits through positive network efects, including compatibility, interoperability, and economies of scale in operations and maintenance (Birman and Schneider 2009, Chen et al. 2011, Lala and Schneider 2009, Stamp 2004). However, such a strategy may also be associated with negative network externalities; for example, creation of a software monoculture in which many, or all, computer systems on the network are exposed to the same software vulnerabilities. Such conditions may result in a crippled network, or in a worst case scenario, a total network failure (Bailey 2005; Chen et al. 2005, 2011).

The concept of heterogeneous networking has been ofered as a design concept to improve a network’s defense capabilities (Zhang et al. 2001). It is based on the idea that diferent network elements with similar functional capabilities are less vulnerable to related security attacks. In this regard, the space diagram can be used to measure the diversity distance between network elements such as OSs, e.g., Linux and Windows (Zhang et al. 2001). A greater distance suggests smaller overlapping network elements. Since network elements become less similar, they are less vulnerable to related security attacks. At the same time, heterogeneous network architectures have higher survivability rates than do homogeneous network structures. O’Donnell and Sethu (2005) studied the impact of software diversity on virus propagation by utilizing the epidemic threshold on a real network as well as a simulated network. They showed that randomly generated software diversity improves epidemic threshold that can be further improved by an algorithm generated software diversity. Their study, however, considered neither scalefree networks that have zero epidemic threshold nor shared vulnerabilities that exist among diverse software. Further work in this area has been done by Bailey (2005) who examined system diversity, where layers of servers with a diferent hardware or software are used on core servers to protect networks from virus attacks, as well as to cope with virus propagation. Bailey (2005) also showed that system diversity is an important tool in enhancing network survivability.

The latest development in software diversity involves the consideration of economic losses resulting from the unavailability of systems. Chen et al. (2011), for example, developed a model of software diversity designed to reduce economic losses resulting from a network’s failure to limit the exploitation of its software vulnerabilities. Their results show that software diversification on a network is an efective approach to reducing security losses. They also introduced the concept of a vulnerability matrix, which is a mapping of software vulnerabilities to nodes in a network. It is a representation of situational awareness of which network nodes are vulnerable to the exploitation of a specific vulnerability (Chen et al. 2011). Although prior research assumes that diferent software products do not share vulnerabilities, Chen et al. (2011) indicated that they can indeed share vulnerabilities because of common components in those products.

Chen et al. (2011) also discussed a model for software allocation, where a firm optimally allocates software to achieve the benefit(s) of software diversification. However, their model did not go beyond the illustration stage. By contrast, our study provides both the models and solution procedures, as well as an in-depth analysis of the efects of network topology, and the dynamics of epidemic behavior (i.e., spreading) in computer networks.

## 2.2. Epidemic Spreading on Computer Networks

Epidemic spreading on computer networks is an example of a nonlinear dynamic system that is similar to that in human populations (Chen and Carley 2004, Kephart and White 1993). Various epidemic models have been proposed to represent the phenomenon on computer networks. Among these, the SIS model is the most widely used for virus propagation. Although the epidemic threshold has been introduced as a measure for the rate of virus propagation on a network, it has also been used as a metric for the resilience of computer networks to epidemic spreading (Kim et al. 2004, O’Donnell and Sethu 2005, Pastor-Satorras and Vespignani 2001b).

Previous research on computer networks indicated that their topology has an impact on epidemic spreading (Bailey 2005, Barthelemy et al. 2005, Moreno et al. 2002, Pastor-Satorras and Vespignani 2001a, Wang and Chen 2003, Wang et al. 2003). Pastor-Satorras and Vespignani (2001b) analyzed the propagation of viruses on complex networks, such as scale-free networks, by using the SIS model. Recently, scale-free networks have been extensively studied in the literature since they well represent important complexities. Such networks can occur in social environments, e.g., scientific collaborations and business alliances (Barabási and Bonabeau 2003), and in technological systems and computer networks such as the Internet (Bailey 2005, Barabási et al. 2000, Börner et al. 2007, Caldarelli et al. 2000, Faloutsos et al. 1999).

A scale-free network follows the power-law connectivity distribution expressed as

$$
P (k) \sim k ^ {- \gamma},\tag{1}
$$

where $P ( k )$ is the probability that a node in a network has k connections to other nodes (Barabási and Albert 1999). For connectivity exponents in the range of $2 <$ $\gamma \leq 3 .$ , Equation (1) suggests that each node may have a statistically significant probability of having a very large number of connections relative to the average connectivity <sup>h</sup>k<sup>i</sup> of the network. Therefore, scale-free networks are characterized by the high connectivity fluctuation, <sup>h</sup>k<sup>2i</sup>. This means that scale-free networks are heterogeneous in that the majority of nodes have one or two links, while a few have a large number of links. They are therefore highly clustered networks with significant connectivity fluctuations (Wang and Chen 2003).

More important, high connectivity fluctuation has a dramatic efect on epidemic propagation in infinite size scale-free networks as it results in the absence of an epidemic threshold (Pastor-Satorras and Vespignani 2001a, Wang et al. 2003). Pastor-Satorras and Vespignani (2002b) analyzed epidemic spreading on a scale-free network. Their analysis provides a bound on the epidemic threshold in terms of both average connectivity and connectivity fluctuation.

For scale-free networks, the epidemic threshold has been found as h i

$$
\lambda_ {c} = \frac {\langle k \rangle}{\langle k ^ {2} \rangle}.\tag{2}
$$

This equation implies that, with a connectivity exponent in the range of $2 < \gamma \leq 3$ , when the network size $N \to \infty$ , the connectivity fluctuation $\left. k ^ { 2 } \right. \to \infty$ , which result in the absence of the epidemic threshold, i.e., $\lambda _ { c } = 0 .$ . As a result, for any spreading rate of infection in the absence of an epidemic threshold, the infection can eventually pervade the entire system.

The impact of immunization on epidemic spreading in a scale-free network has been analyzed by making selected nodes resistant to security attacks with random and targeted immunization strategies (Pastor-Satorras and Vespignani 2008). However, results suggest that a random strategy does not eradicate an infection. In particular, an epidemic threshold remains absent because of the connectivity fluctuations of such networks. This result is consistent with earlier findings insofar as scale-free networks have a noticeable resilience to random connection failures without losing their global connectivity properties. This, in turn, allows viruses to penetrate the entire network (Albert et al. 2000, Barabási and Bonabeau 2003). Pastor-Satorras and Vespignani (2008) thus argued that a successful immunization strategy can be developed by accounting for the connectivity fluctuations of scalefree networks. More important, a targeted immunization strategy, which immunizes the most connected nodes, results in a nonzero epidemic threshold.

Although the targeted immunization strategy results in a nonzero epidemic threshold, it is not a practical approach in real networks as it fails to consider either software diversity or shared vulnerabilities across software products. If the highly connected nodes share common vulnerabilities with other nodes, the infection would thus be able to spread. We therefore suggest that such a strategy is potentially vulnerable under a variety of real-world scenarios.

## 2.3. Implications from the Literature Review

From the above discussion, it is clear that most of the earlier research in the field has focused on either software diversity or epidemic spreading. Although each research stream has been well analyzed separately, there has been little to no efort to integrate the models and methodologies from these two streams. Research on software diversity has generally focused on analyzing the efectiveness of software diversity in overcoming the risk of correlated failure of computer systems on networks. As previously noted, prior research on software diversity has assumed that diferent software products do not share vulnerabilities (O’Donnell and Sethu 2005, Pastor-Satorras and Vespignani 2008), however, they may because of their common components, which ofer economic benefits in the form of compatibility, interoperability, and economies of scale in both operations and maintenance (Chen et al. 2011).

Research on epidemic spreading has adopted the SIS model, and introduced the notion of a threshold as a measure of the efectiveness of population-spread epidemics. In this research stream, the impact of immunization has been studied by introducing immune nodes to a network. This approach implicitly considers a single type of software with immunized nodes that are not afected by security attacks. Yet, it does not consider either software diversity using multiple software alternatives, or shared vulnerabilities across software products or computer systems, which are significant gaps, in our view.

Our review of the two noted research streams has identified important research opportunities in the literature. In particular, software diversity research has not suficiently analyzed epidemic spreading in diverse systems such as scale-free networks, nor identified the epidemic threshold as a measure for such spreading.

The resilience of a computer network may thus not be properly or fully assessed without an analysis of its software diversity. We also believe that the impact of software diversity and the presence of shared vulnerabilities on epidemic spreading require further studies.

## 3. Model Development

We argue that software diversity increases the epidemic threshold in scale-free networks, and makes them more resilient to epidemic spreading. The current study thus analyzes the impact of software diversity on network security by developing a model that disaggregates software monoculture in an attempt to increase the epidemic threshold in scale-free networks in the presence of shared vulnerabilities. The model assumes that vulnerabilities are shared among diferent software alternatives, and provides an optimal solution to software distribution for the problem of correlated computer failure. We propose that the nature and level of software diversity resulting from the model solution will allow for the needed increase in epidemic threshold within a scale-free network.

To combine the approaches that have been utilized in software diversity and epidemic spreading, we first develop a measure for software diversity based on the Shannon entropy (Shannon 1948). We develop an information theoretic decision model based on information gain that can determine software alternatives for a pair of nodes. We then propose a software distribution model that can increase the software diversity in a network. Finally, we develop a simulation model for virus propagation, which integrates the software diversity and SIS epidemic spreading models.

We subsequently compare the impact of software diversity created by the proposed models with that created by the targeted distribution. The epidemic threshold is used as a measure of network resilience to epidemic spreading.

## 3.1. Model of Software Diversity

O’Donnell and Sethu (2004) developed the defective edge count as a measure of software diversity. It represents the number of connected nodes running the same software product on a given network. The main limitation of this measure is that it lacks consideration of the shared vulnerabilities between diferent software products. A vulnerability is thus assumed specific to a single software product although diferent software products can share vulnerabilities as noted in Chen et al. (2011). Given this, the defective edge count is considered insuficient for measuring software diversity in the current context.

A search for a good measure for software diversity brings about a diversity index in ecology, which is a measure that reflects how many diferent species there

Figure 1. Node Vulnerability Matrix: A Mapping of Vulnerabilities to Nodes in a Network, Derived by Multiplying the Node-Software Matrix with the Software-Vulnerability Matrix

$$
\begin{array}{c c c c c c c c}S _ {1}&S _ {2}&S _ {3}\\N _ {1}&\left[\begin{array}{l l l}1&0&0\\0&1&0\\0&0&1\end{array}\right]&S _ {1}&V _ {1}&V _ {2}&V _ {3}&V _ {4}&V _ {5}\\N _ {2}&S _ {2}&0&0&1&1&1\\N _ {3}&S _ {3}&0&1&1&0&0\end{array}\left. \right] =\begin{array}{c c c c c}N _ {1}&V _ {1}&V _ {2}&V _ {3}&V _ {4}&V _ {5}\\N _ {2}&\left[\begin{array}{l l l l l}1&1&0&0&0\\0&0&1&1&1\\0&1&1&0&0\end{array}\right]\end{array}
$$

are in a given community. A diversity index summarizes the diversity in the community by taking into account how evenly organisms are distributed among these species. Hill’s diversity index (Hill 1973) is a general diversity measure and given as

$$
N _ {a} = \left(\sum_ {i = 1} ^ {R} p _ {i} ^ {q}\right) ^ {1 / (1 - q)},\tag{3}
$$

where R is richness defined as the total number of types (species), ${ \bf \nabla } \cdot { \bf \nabla } p _ { i }$ is the probability of the ith type, and q is the order of the diversity.

Hill’s diversity index is a generalized form of popular entropy-based diversity measures, such as Rényi entropy (Rényi 1961), and Shannon entropy (Shannon and Weaver 1949). Neti et al. (2012) has modeled software diversity as an entropy-based measurement. Although their model allows a vulnerability to be shared by diferent software products, their diversity measure is not suitable to incorporate network topology. In their model, the relationships between nodes and vulnerabilities are represented as a bipartite graph (two-mode network) where nodes are actors and vulnerabilities are events. Two nodes are related if they have the same vulnerability. However, their diversity measure is limited in considering shared vulnerabilities between diferent software products. Vulnerabilities are uniformly distributed to nodes regardless of whether or not they belong to a specific software. This implicitly assumes that vulnerabilities are independent from software products. This means that nodes do not select software itself but select any set of vulnerabilities that may belong to diferent software products. Indeed, if nodes select a set of vulnerabilities from diferent software products, this means they run associated software, and must have all vulnerabilities that exist in those software products.

Since we consider that diferent software packages can share vulnerabilities, network nodes are immediately subject to those vulnerabilities, even if different packages are used between connected nodes. Hence, we define a new measure for software diversity that captures node-to-node shared vulnerabilities by extending the entropy-based diversity measure ofered by Neti et al. (2012). In doing so, we first create a matrix termed node-vulnerability matrix (NVM), which is based on the works of Chen et al. (2011).

In essence, an NVM shows a mapping of software vulnerabilities to nodes in a network (Chen et al. 2011). It is constructed from two other matrices: a nodesoftware matrix and a software-vulnerability matrix. The former lists the software alternatives installed on each network node, as shown in Figure 1(a) while the latter lists the vulnerabilities across multiple software alternatives, as shown in Figure 1(b). The product of these matrices yields the node-vulnerability matrix as shown in Figure 1(c). Note that a row represents the set of vulnerabilities present in each node, while a column represents the set of nodes that share a particular vulnerability.

With the NVM available, we develop a new software diversity index (SDI) based on the Shannon entropy. The resulting SDI is given as

$$
\begin{array}{c} \text { Software   Diversity   Index } = - \sum_ {i = 1} ^ {v} p _ {i} \log p _ {i}, \\ p _ {i} = \frac {\sum_ {k = 1} ^ {n - 1} \sum_ {l = k + 1} ^ {n} N _ {k l} (1 - N V M _ {k i} \cdot N V M _ {l i})}{\sum_ {j = 1} ^ {v} (\sum_ {k = 1} ^ {n - 1} \sum_ {l = k + 1} ^ {n} N _ {k l})}, \quad \forall N _ {k l} = 1, \end{array} \tag {4}\tag{5}
$$

where i and j are the column index of the matrix items NVM, n is the number of nodes, and v is the number of vulnerability dimensions. The product of $N V M _ { k i }$ and $N V M _ { l i }$ indicates whether nodes k and l share the vulnerability i. If there is a direct connection between node k and l, $N _ { k l }$ is 1, 0 otherwise. In Equation (5), the numerator indicates the number of node pairs that do not share vulnerability i. The denominator indicates the total number of vulnerability dimensions between all node pairs. Therefore, $p _ { i }$ is the proportion of protected connections against vulnerability i.

Given the number of vulnerabilities $v ,$ the maximum value is independent from the number of nodes and connections. For purposes of simplifying further analysis, the SDI is normalized to values between 0 and 1, dividing by its maximum value that is achieved when vulnerabilities are evenly distributed, i.e., $p _ { i } = 1 / v$

We propose that the value of SDI is dependent on similarities between the software alternatives within a given network, although the value can be improved by allocating each software alternative to the “best” nodes. Therefore, we develop an information theoretic decision model for assigning software alternatives to nodes based on the decision tree induction technique used in the Iterative Dichotomiser 3 (ID3) algorithm (Quinlan 1986). Using the decision model based on the Shannon entropy, software alternatives will be selected for nodes to increase uncertainty (diversity).

## 3.2. Information Theoretic Decision Model for Software Allocation

Information theory provides measures of information in a system. A key measure in information theory is entropy, and entropy measures the amount of information (i.e., uncertainty) about an event associated with a given probability distribution (Shannon and Weaver 1949). Based on information theory, diferent combinations of software alternatives result in the varying degree of software diversity based on shared vulnerabilities. Specifically, if any pair of nodes runs the same or similar software, they share the same or similar sets of vulnerabilities, which in turn reduces uncertainty and entropy in the system since the system becomes more homogenous. At the extreme case when all vulnerabilities are shared between software alternatives (perfect overlapping), uncertainty is totally eliminated, and entropy becomes zero. By contrast, if any pair of nodes runs diferent software products, the number of shared vulnerabilities may decrease, which in turn increases uncertainty and entropy in the system since the system becomes more heterogeneous.

The discussion above indicates that assigning different combinations of software to any pair of nodes makes the system more or less heterogeneous, and in turn results in a change (positive or negative) in entropy based on the similarity (the number of shared vulnerabilities) between software alternatives. The less the software alternatives are similar in terms of shared vulnerabilities, the more the system gains entropy. If software alternatives do not share any vulnerability, the maximum software diversity can be achieved. Therefore, the event is defined as whether the software alternatives share vulnerability. In the context of software allocation, we are interested in how much uncertainty (entropy) about an event can be created by allocating software alternatives. The gain is defined as the expected change in entropy (Mitchell 1997, Quinlan 1986). Given an initial entropy, Entropy<sup>(</sup>S<sup>)</sup>, the gain is thus given as (Mitchell 1997)

$$
G a i n (S, A) = E n t r o p y (S) - \sum_ {t \in V a l u e s (A)} \frac {| S _ {t} |}{| S |} E n t r o p y (S _ {t}),\tag{6}
$$

where S is a data set for which entropy is being calculated, A is an attribute of $S ,$ Values<sup>(</sup>A<sup>)</sup> is the set of all possible values for attribute $A , S _ { t }$ is the subset of S for which attribute A has value $t , | S _ { t } |$ is the number of elements in $\boldsymbol { S } _ { t } ,$ and <sup>|</sup>S<sup>|</sup> is the number of elements in S. The ratio of $| S _ { t } | / | S |$ also indicates that getting entropy for large subpartitions is more important than for small subpartitions. Large subpartitions are therefore more critical than small subpartitions to change the final entropy based on the gain criterion.

Equation (6) indicates that given the initial entropy, Entropy<sup>(</sup>S<sup>)</sup>, diferent choices of software alternatives result in diferent level of final entropy. We therefore quantify the gain from assigning software alternatives to nodes by the diference between the initial entropy and the final entropy. Entropy can be extended to a pair of random variables in terms of relative entropy, which is a measure of the distance between two probability distributions (Cover and Thomas 2006, Gray 2013). Mutual information is a measure of the amount of information that one random variable contains about another random variable (Cover and Thomas 2006, Gray 2013). Therefore, mutual information is the reduction in the uncertainty of one random variable due to the knowledge of the other random variable (Cover and Thomas 2006, Gray 2013, MacKay 2003). Relative entropy is mutual information (Cover and Thomas 2006, Gray 2013). Therefore, the change in entropy, which is called the information gain in the context of the decision tree model using the ID3 algorithm (Mitchell 1997, Quinlan 1986), can be measured by mutual information, which is given as

$$
I (X, Y) = p (X, Y) \log \left(\frac {p (X , Y)}{p (X) p (X)}\right),\tag{7}
$$

where $p ( X , Y )$ is the joint probability distribution of X and $\boldsymbol { Y } ,$ and $p ( X )$ and $p ( Y )$ are the marginal probability distribution of X and $\boldsymbol { Y } ,$ respectively. In our software diversity context, $p ( X )$ refers to the probability that an exploited vulnerability is spread from software X on the first node, and $p ( Y )$ refers to the probability that the same vulnerability is spread to software Y on the second node.

Our purpose is to increase entropy (diversity) by reducing the number of shared vulnerabilities. This can be achieved by assigning the best combination of software alternatives with the smallest information gain, which results in the largest entropy. We therefore developed the decision model for assigning software alternatives to nodes based on the decision model using the ID3 algorithm. Based on this decision model, software alternatives will be selected for nodes to increase entropy (diversity) in the system.

In Figure 1(b), the software-vulnerability matrix maps vulnerabilities to software. The decision model assigns a Boolean classification to each vulnerability dimension to identify the shared vulnerabilities by matching mappings of vulnerabilities from selected software alternatives. Matching of vulnerabilities from the second selected software is conditionally dependent on the given set of vulnerabilities existing in the first selected software. Therefore, the joint probability distribution is calculated as $p ( X , Y ) = \dot { p } ( Y | \hat { X } ) p ( X )$

The decision model indicates that the combination of diferent software alternatives results in the lowest reduction in entropy. Information gain (mutual information) is symmetric for the combination of diferent types of software, $\operatorname { I } ( \mathbf { A } , \mathbf { B } ) = \operatorname { I } ( \mathbf { B } , \mathbf { A } )$ , but not symmetric for the combination of the same type of software, $\mathrm { I } ( \mathrm { A } , \mathrm { A } ) \neq \mathrm { I } ( \mathrm { B } , \mathrm { B } )$ , unless they have the same number of vulnerabilities. This emphasizes that if the same type of software has to be selected for assigning to a pair of nodes, selecting software with the lower number of vulnerabilities (which means relatively less shared vulnerability) results in a relatively lower gain. It is also important to note that software with the lower number of vulnerability is less likely to be targeted by security attacks.

Because lower information gain indicates higher resulting entropy, one may expect that high software diversity can be accomplished by employing software alternatives with lower information gain (the lowest for dissimilar software alternatives). However, depending on how well dissimilar software alternatives are distributed across nodes, diversity may dramatically shift, in particular, in scale-free networks. We thus provide a model for distributing software, as developed below.

## 3.3. Software Distribution Model

To prescribe optimal software allocation (diversification) on scale-free networks, we propose and formulate two combinatorial LP models. Our LP models minimize the total information gain produced by assigning software alternatives to all pairs of nodes, which in turn maximize the final entropy in the system. The first model (LP1) is formulated as follows.

Let n be the number of nodes, s the number of software alternatives, and $X _ { i k }$ and $X _ { j l }$ be the binary decision variables that represent whether node i and j run software k and $l ,$ respectively. Let parameter $N _ { i j }$ be 1 if there is a physical connection between node i and $j ,$ 0 otherwise. Let another decision variable $C _ { i j k l }$ be 1 if node i assigns software k $( k = 1 , \ldots , s )$ and node j assigns software l $( l = 1 , \ldots , s ) ,$ , 0 otherwise. Here, $C _ { i j k l }$ is introduced to make the objective function linear. Finally, $\rho _ { k l }$ represents the information gain produced by assigning software alternative k and l to a pair of nodes as defined in Equation (7). LP1 is thus given by

$$
\min \sum_ {i = 1} ^ {n - 1} \sum_ {j = i + 1} ^ {n} \left[ \sum_ {k = 1} ^ {s} \sum_ {l = 1} ^ {s} (\rho_ {k l} C _ {i j k l}) \right]\tag{8}
$$

$$
\text { s.t. } X _ {i k} + X _ {j l} - C _ {i j k l} \leq 1 \quad \forall i, j \in \{1, \dots , n \}, i > j,\tag{9}
$$

$$
\sum_ {k} ^ {s} \sum_ {l} ^ {s} C _ {i j k l} = N _ {i j} \quad \forall i, j \in \{1, \ldots , n \}, i > j,\tag{10}
$$

$$
\sum_ {k = 1} ^ {s} X _ {i k} = 1 \quad \forall i \in \{1, \ldots , n \},\tag{11}
$$

$$
X _ {i k}, X _ {j l}, C _ {i j k l} \text { are   binary   variables. }\tag{12}
$$

Table 1. The Reduction of Vertex Cover to LP1

<table><tr><td>Vertex cover</td><td>LP1</td></tr><tr><td> $G = (V, E)$ </td><td> $U = \{e_1, \dots, e_m\}$ ,  $m = |E|$ </td></tr><tr><td> $k$ </td><td> $S = \{S_1, \dots, S_v\}$ ,  $v = |V|$ ,  $S_v \subseteq E$ </td></tr><tr><td> $c: V \to Q^+$ </td><td> $k$  $c: S \to Q^+$ </td></tr></table>

The objective function (Equation (8)) minimizes the total information gain resulting from software assignments. The constraints in Equations $( 9 ) \mathrm { - } ( 1 1 )$ do the following: (9) tracks the software assignments between any two nodes, while (10) ensures that if nodes i and j are connected $( N _ { i j } = 1 )$ <sup>)</sup> they must be assigned only one of all possible software assignments, while (11) requires that each node is assigned one of the given software alternatives.

The LP1 formulation is based on the integer programs developed for the vertex cover and set cover problems (Vazirani 2001). We can show that LP1 is reduced from vertex cover, which is a special case of set cover. Thus, we show the complexity of LP1 as follows.

## Claim 1. LP1 model is NP-hard.

Proof. We first define LP1 based on set cover by illustrating the reduction of instances of vertex cover to instances of LP1 below.

Vertex Cover. Given an undirected graph $G = ( V , E ) ,$ , a cost function on vertices c: $V \to Q ^ { + }$ , and an integer k as input, is there a subset of vertices (a vertex cover) $V ^ { \prime } \subseteq V$ such that $\begin{array} { r } { | V ^ { \prime } | \leq k , } \end{array}$ and i ${ \sf f } \forall ( v , w ) \in E$ then either $v \in V ^ { \prime } ,$ $w \in V ^ { \prime } ,$ or both?

LP1. Given a universe U of n elements, a collection $S = \{ S _ { 1 } , \ldots , S _ { m } \}$ of subsets of a universe $U , \mathfrak { a }$ cost function $c \colon S \to Q ^ { + }$ , and an integer k as input, does there exist a subcollection (a set cover) $S ^ { \prime } \subseteq S$ such that $| S ^ { \prime } | \leq k$ and its union is a universe U?

We next prove the reduction of LP1 from vertex cover as follows. For any given instance of vertex cover in a graph $G = ( V , E )$ , and an integer k as input, the vertex cover problem determines whether there are k vertices covering all edges. As shown in Table 1, we can construct corresponding instances for our LP model with $U = E _ { \ast }$ , and for each vertex in V there is a set $S \in E$ containing all of the edges in E directly linked to the vertex. Furthermore, for every $S _ { v } \in E .$ , we have the cost of selecting a vertex whose cost is the sum of the cost of all of the edges in $S _ { v }$ . This construction can be done in time that is polynomial in the size of vertex cover instance (Goodrich and Tamassia 2001, Karp 1972). Suppose that G has a vertex cover $V ^ { \prime }$ of size at most $k ,$ then we have a set cover $S ^ { \prime }$ in LP1 by choosing the subsets corresponding to the selected vertices. On the other hand, suppose that we have a set cover $S ^ { \prime }$ in LP1, then we can choose the vertices $V ^ { \prime }$ corresponding to the selected subsets. In this way, we have vertex cover reduce to LP1 (Vertex Cover $\leq _ { p } \mathrm { L P }$ model). Given that vertex cover is NP-hard, LP1 is NP-hard.

Figure 2. Illustration for the Proof that LP1 Is NP-hard  
![](/api/attachments/YSR6BWKM/fulltext/images/bf1f8f74c3591a1d2d3301ff22da11204166f9f3d757ceb31ddae540005ea917.jpg)  
Notes. The vertices are numbered 1 through 9, and the edges are given letter labels a through p. Panel a shows the graph G with the nodes of a vertex cover V of size 3 shaded in grey. Panel b shows the sets associated with each vertex in a graph G, with the subscript of each set identifying the associated vertex. Note that a set cover S contains all of the edges of a graph G.

Figure 2 further illustrates the reduction of vertex cover to LP1. We can define an instance of LP1 in terms of an instance G and k of vertex cover. The universe U corresponds to all edges in the graph G such that $U = \{ e _ { 1 } , \bar { \ldots } , e _ { n } \} , n = | E |$ . Each subset corresponds to a node in the graph and contains all of the edges attached to the node such that $S = \{ S _ { 1 } , \ldots , S _ { v } \} , v = | V | , S _ { v } \subseteq E .$ There is a set cover $S ^ { \prime }$ among these sets $S _ { v }$ of size k if and only if there is a vertex cover $V ^ { \prime }$ of size k in $G .$ Note that a set cover $S ^ { \prime }$ consists of $S _ { 1 } , S _ { 2 } ,$ , and $S _ { 3 } ,$ , which contains all of the edges of a graph G.

Although NP-hard optimization problems are not solvable for finding optimal solutions in polynomial time, they may be polynomial-time reducible if there are efective algorithms or heuristics to find nearoptimal solutions eficiently (Goodrich and Tamassia 2001, Vazirani 2001). If there are polynomial-time solution methods for an NP-hard problem, such solution methods can also be applicable to any optimization problem that is reduced from that NP-hard problem. The branch-and-bound algorithm is an efective algorithm for the vertex cover problem (Goodrich and Tamassia 2001), thus it can also be an efective algorithm for our LP problems. CPLEX uses the branch-and-bound algorithm for mixed-integer programs (MIP). Therefore, we used the branch-andbound algorithm to solve the LP1 model in CPLEX. However, the default CPLEX branch-and-bound algorithm was not suficiently efective to solve the LP1 model. To improve the solution times, we first applied advanced performance tuning techniques available in CPLEX. For example, we performed very aggressive probing on variables before MIP branching. We selected the dual simplex algorithm as a continuous optimizer algorithm to solve the initial MIP relaxation. We also emphasized feasibility over optimality to generate more feasible solutions early. The depthfirst search has been applied for selecting the next node to process when backtracking. We also used the relaxation induced neighborhood search (RINS) heuristic to improve the best solution found, and then applied the periodic heuristic frequently. Finally, we polished a best-found feasible solution to improve it. Although we applied advanced performance tuning techniques, the branch-and-bound algorithm still took too long to solve LP1, possibly due to the challenges created by the structural complexity of networks.

Based on the greedy heuristics developed for the set cover problem (Goodrich and Tamassia 2001, Vazirani 2001) and for the domination set (Alber et al. 2004), we developed two heuristics that generate good initial feasible solutions known as MIP start (CPLEX 2015). The first algorithm assigns software based on the density distribution of nodes, and proceeds as follows:

## Algorithm 1

Step Action

1. Assign a software alternative with minimum vulnerability to the node with maximum connections (the densest).

2. Select the next densest node.

3. If the selected node is connected to any previous denser node(s), then Assign it a diferent software alternative. Else

Assign a software alternative with minimum vulnerability.

4. Repeat steps 2 and 3 until all nodes are assigned a software alternative.

Although Algorithm 1 reduces the solution time, it does not consider the local distribution of software that may be afected by the connectivity fluctuations of scale-free networks. To further improve the quality of the initial solution, we developed a subsequent algorithm that begins with the solution from Algorithm 1, and attempts to locally optimize software distribution. The basic idea is to change the software allocation of a given (densely connected) node by considering the software distribution of its adjacent nodes. Algorithm 2 thus proceeds as follows:

## Algorithm 2

Step Action

1. Locate the densest node.

2. Select next densest node.

3. If the selected node is connected to any previous denser node, then

Calculate the percentage of each software alternatives used by all adjacent nodes.

Assign the least utilized software alternative to the selected node.

If the selected node and previous denser node use the same software alternative, then

Assign the second least utilized to the selected node.

4. Repeat steps 2 and 3 until all nodes are evaluated for a new software alternative.

Algorithm 2 changes the local distribution of software for each node, which then afects the distribution for other nodes. The algorithm can thus be applied iteratively until there are no changes in software distribution. The two algorithms, along with tuning of CPLEX parameters, resulted in a great reduction in solution times.

Although LP1 minimizes the total information gain, it does not consider the connectivity fluctuations and hierarchical dynamics in scale-free networks mentioned above. Alber et al. (2004) indicate that nodes with greater degree are dominating nodes and their union is also important for a local search. We thus extend LP1 by introducing a degree coeficient based on the nodes’ degree hierarchy. The degree coeficient penalizes the network for running the same software on highly connected nodes more than on less connected nodes. With this coeficient incorporated, the LP2 model is able to capture the efect of network topology and take into account the nodes’ degree hierarchy. The degree coeficient, $f _ { i j } ,$ is formally defined as the sum of degrees of node i and j to all other nodes on a network, given as

$$
f _ {i j} = \sum_ {m = 1} ^ {n} (N _ {i m} + N _ {j m}) \quad \forall i, j \text {where} N _ {i j} = 1.\tag{13}
$$

As given in Equation (13), LP2 is formulated to minimize the total information gain weighted by the degree coeficient with the same constraints developed in LP1

$$
\begin{array}{l} \min \sum_ {i = 1} ^ {n - 1} \sum_ {j = i + 1} ^ {n} f _ {i j} \left[ \sum_ {k = 1} ^ {s} \sum_ {l = 1} ^ {s} (\rho_ {k l} N _ {i j k l}) \right] \\ \text { subject   to   constraints(9) - (12). } \end{array}\tag{14}
$$

The two proposed LP models ensure that software alternatives for network nodes are distributed to increase software diversity to the maximum possible level. However, the spreading of viruses or worms also depends on infection and defection processes. We thus developed a virus propagation model that incorporates the shared vulnerabilities between software alternatives.

## 3.4. Dynamic Software Distribution

As organizations grow, their networks grow organically, and thus new nodes are added to the existing networks (Medina et al. 2000). Changing existing software allocation in an organization’s network can be disruptive and computationally burdensome. For networks experiencing growth, decisions may have to be made incrementally on software choices. To accommodate such incremental software decisions, we developed a dynamic software allocation algorithm (Algorithm 3), which is based on the degree coeficient in Equation (13) and Algorithm 2. The algorithm starts with an existing software distribution, which may be optimal or near optimal, and allocates the best software alternative to each new node by considering the degree of the adjacent nodes and existing software allocations. Figure 3 further illustrates Algorithm 3, which proceeds as follows:

## Algorithm 3

Step Action

1. Select a newly added node where adjacent nodes are already assigned a software alternative.

2. Compute the degree of each adjacent node by counting its connections and calculate the degree sum for each software.

3. Compute the degree ratio of each software alternative by dividing the degree sum for each software with the sum of all software degrees.

4. Assign the software alternative with the smallest degree ratio to the selected node. In case of a tie in the degree ratios, assign the software alternative with the minimum vulnerability.

5. Repeat steps 1 to 4 until all newly added nodes are allocated a software alternative.

Figure 3. (Color online) Illustration for the Implementation of Algorithm 3  
![](/api/attachments/YSR6BWKM/fulltext/images/8ca97792af12d7a12edeaaedfd955fb2d0030e5e5b2e581f602304dac29e1acf.jpg)  
Notes. The initial network consists of nine nodes (circles), which run software alternatives labeled A or B. The filled circles represent newly added nodes. For example, the rightmost side node is assigned software B because software B degree ratio is 2/6 (the least utilized alternative).

## 3.5. Virus Propagation Model

To model virus and worm propagation on a network, we adopt the well-known and highly regarded SIS model developed by Bailey (1975). It can model such behavior on either physical networks connecting computers, or social networks connecting people (Chen and Carley 2004). The model assumes that a network node can realize instantaneous transition between two states $( \mathrm { i . e . , }$ , susceptible and infected).

Based on the model’s dynamics, as soon as a node becomes infected, it becomes infectious. Similarly, as soon as a node is disinfected, it is susceptible to reinfection. An efective disinfection process may stop virus spreading if every node remains in a susceptible state. A rapid disinfection rate, or the isolation of susceptible nodes from infected nodes, may achieve such an outcome. However, even after an extensive period of time, the virus may spread because of a faster infection rate, and/or a greater exposure of infected to susceptible nodes. More important, since the SIS model is generally concerned with the rate of propagation and the final epidemic state (Wang and Wang 2003), it fits well with the current study’s objectives.

Within the SIS framework, a node changes its state from susceptible to infected when an infected neighbor passes on its contagion with infection probability rate, $\beta .$ Conversely, a node changes its state from infected to susceptible, and becomes susceptible again with disinfection probability rate, δ. The ratio λ <sup></sup> $\beta / \delta$ is thus defined as the virus spreading rate (VSR) (Pastor-Satorras and Vespignani 2002a). This expression implicitly considers the presence of antivirus software, since all infected individuals eventually return to the susceptible state. Furthermore, it assumes the case in which computer users do not become more aware with respect to viral infection once they have cleaned their computers, which can then, once again, become infected (Kephart and White 1991). In addition, by using the SIS model, we assume that a node can be infected with the same type of viruses again, albeit not the same virus, just as a human catches a cold. Metamorphic and polymorphic viruses change their structure to avoid detection from antivirus software while they do not change the functions (e.g., destructing information, installing backdoor application) they perform (Lin and Stamp 2011).

The VSR, λ, is regarded as the critical point in terms of process continuity. If it is below the epidemic threshold $\lambda _ { c } ,$ the infection will eventually disappear. On the other hand, if it is equal to, or above, $\lambda _ { c } ,$ the infection spreads, and becomes endemic (Pastor-Satorras and Vespignani 2002b). Interestingly, the infection and disinfection processes in the SIS model resemble software vulnerability patch processes (Arora et al. 2010, Temizkan et al. 2012), where vulnerabilities are constantly discovered by attackers and are, in turn, patched by software vendors. A virus or worm may find a specific vulnerability in a software product and exploit it to spread. A patch for the vulnerability may then be developed, wherein an infected node can apply the patch and enter into a “susceptible” state until the same type of vulnerability is again found and exploited (Temizkan et al. 2012).

Previous SIS models on epidemic spreading implicitly consider one type of software as vulnerable to a security attack (O’Donnell and Sethu 2005, Pastor-Satorras and Vespignani 2008). However, neither software diversity nor shared vulnerabilities among software alternatives have been considered. In the current study, we introduce vulnerability dimensions that can represent any software alternative’s weakness to specific types of attacks. For example, a network node is vulnerable to a virus attack type i if the deployed software alternative is weak against vulnerability i. Deploying a diferent software alternative immune to vulnerability i on the adjacent nodes prevents the virus attack type i from spreading. In other words, if the vulnerability is specific to only one software alternative, diversification becomes an efective countermeasure in halting virus propagation (Chen et al. 2011). However, if the attack is against the vulnerability common to the alternatives, deploying diferent software still allows an infection to spread as if the same software is deployed on the adjacent nodes. Because the epidemic threshold depends on how diferent the software alternatives are, which is best measured by the number of shared vulnerabilities, the SIS model is further extended in our research by incorporating the concept of software diversity and shared vulnerabilities.

## 4. Experiments

To evaluate the performance of our software distribution models, we conducted two experiments. The first seeks to determine how much software diversity the LP model solutions are able to provide. These solutions are expected to perform better than those of the targeted distribution strategy. We thus compared the performances of the LP models to that of targeted distribution in terms of SDI. The second experiment evaluates the efectiveness of the LP model solutions in terms of epidemic threshold. This efort involves the simulation of virus propagation under conditions of software diversification. To test the efectiveness of the LP model solutions, we compared their epidemic threshold to that of targeted distribution solutions.

In the first experiment, the IBM CPLEX 12.1 optimization software was used to solve the LP models for software distribution. We conducted all runs on a 64- bit Windows 7 laptop with Intel Core i5 2.4 GHz CPU and 8 GB RAM. The second experiment was conducted on the same machine with the applications developed with Microsoft Visual Studio 2010.

## 4.1. Factors and Levels for the Experiments

The proposed LP models for software distribution were evaluated in terms of SDI. The experimental factors included both network related factors (i.e., number of connections, number of nodes, and network degree centrality), and software related factors (i.e., number of software alternatives and software similarity based on the Jaccard similarity coeficient). The factors and levels are summarized in Table 2. Because high software diversity can lead to a resilient network, the same factors and levels were used in the virus propagation experiment intended to evaluate the performance of the LP model solutions in terms of epidemic threshold.

Table 2. Factors and Levels for Experiments

<table><tr><td>Factors</td><td>Levels</td></tr><tr><td>Number of connections</td><td>1 connection and 2 connections</td></tr><tr><td>Number of nodes</td><td>1,000, 2,500, and 5,000 nodes</td></tr><tr><td>Network degree centrality</td><td>Low and high</td></tr><tr><td>Number of software products</td><td>2 software and 3 software</td></tr><tr><td>Software similarity index</td><td>5% and 40%</td></tr></table>

4.1.1. Network-Related Factors. Network topologies and network parameters may determine the complexity of software distribution, and afect the SDI. For example, we expect that as the size of the network gets larger, the software distribution model becomes more complex, producing inferior software diversity performance. In this regard, we created scale-free networks consisting of 1,000, 2,500, and 5,000 nodes. They are based on Barabási and Albert’s (1999) scale-free network model. The Network Workbench tool (NWB Team 2006) was used to generate these networks for the current set of experiments.

We created two types of scale-free networks by varying the number of connections added at each time when a new node is connected to existing nodes. Beginning with an initial network of three nodes, a new node is added with one or two connections at each time step. The probability of attaching a new node to an existing one is given by the power-law connectivity distribution in Equation (1). The first type of scale-free network (one connectivity network) is created when one node is added to a network, and connected to one of the existing nodes at each time step. The second type (two connectivity network) is created when a single node is added to a network, and connected to two existing nodes at each time step. The connections between the nodes are undirected.

We also created two types of scale-free networks by varying the degree of network centrality, i.e., low- and high-degree centrality. Network degree centrality (NDC) is the measure of how many other nodes are connected to one node in a network (Freeman 1979, Wasserman and Frost 1994). NDC is the variation in the degrees of nodes divided by the maximum degree variation in a network (Nooy et al. 2005). A high NDC suggests a network wherein nodes show high degree diferences, which means that a few nodes may have higher degrees while others have lower degrees. NDC lies in the range from 0 (no variation) to 1 (maximum variation). This metric defined by Freeman (1979) thus characterizes a network’s topology, and its (scale-free) connectivity fluctuations

$$
\text { Network   Degree   Centrality } = \frac {\sum_ {i = 1} ^ {n} \left[ C _ {D} (n ^ {*}) - C _ {D} (i) \right]}{(n - 1) (n - 2)},\tag{15}
$$

where n is the number of nodes, $C _ { D } ( n ^ { * } )$ is the maximum degree, and $C _ { D } ( i )$ is the degree of node i. Since (c) 1,000 nodes, 2-connection, low NDC

Figure 4. (Color online) Network Visualizations  
![](/api/attachments/YSR6BWKM/fulltext/images/aa969ab9477d979eeeab64672d3f1df2615616145b1ca787d91a37fa35e5a193.jpg)

![](/api/attachments/YSR6BWKM/fulltext/images/bed55c5d27e8d2950cc8cc96e2317626b76f346ffc70739ee091ada520523c69.jpg)  
(b) 1,000 nodes, 1-connection, high NDC

the connections between the nodes are undirected in our experimental context and in-degree and outdegree are equal for undirected networks, the maximum degree is calculated based on all edges.

The NDCs have been calculated using UCINET (Borgatti et al. 2002). To create low-degree versus highdegree centrality networks we generated sample networks using the Network Workbench tool. We stopped generating samples until we got an NDC less than 0.2 and greater than 0.5 for low- and high-degree centrality networks, respectively.

Figure 4 illustrates diferent types of networks with a varying number of connections and degree of network centrality. Two connectivity networks show highly connected nodes that are interconnected with each other, whereas one-connectivity networks show a single connection between two highly connected nodes. Highdegree centrality networks show fewer highly connected nodes with more connections from those than low-degree centrality networks.

4.1.2. Software-Related Factors. We expect that more software alternatives with lower similarity increase the value of SDI. We first developed two case scenarios based on the number of software alternatives used to create software diversity. The first is the two-software case and the second is the three-software case where we used two and three software alternatives to create diversity in the network, respectively.

![](/api/attachments/YSR6BWKM/fulltext/images/91251e68a748ac865f01170726379a7539e87bddde452a499e6e9cdf5a676ba5.jpg)

(d) 1,000 nodes, 2-connection, high NDC  
![](/api/attachments/YSR6BWKM/fulltext/images/2933704bc1eed123237b05e338ff239e0e0841175376ab60553ae96abec7d810.jpg)

To capture the degree of similarity between any given pair of software alternatives, we introduce a software similarity index (SSI), defined as the proportion of shared vulnerabilities between software alternatives based on the Jaccard similarity coeficient, which is widely used to compare the similarity of two sets (Sokal and Sneath 1963). Greater software similarity will result in a reduced benefit from software diversification. The SSI between software k and software l is given as

$$
\mathrm{SSI} = \frac {v _ {k l}}{v _ {k} + v _ {l} - v _ {k l}},\tag{16}
$$

where $v _ { k }$ and $v _ { l }$ are the number of vulnerabilities in software k and $l ,$ respectively, and $v _ { k l }$ is the number of shared vulnerabilities between software k and l.

We set the SSI between any given pair of software alternatives to 5% and 40% for both the two and three software cases. To create 5% and 40% levels of software similarity in the two-software case, we created a software-vulnerability matrix with 20 vulnerability dimensions. We used 60 dimensions in the threesoftware case.

## 4.2. Software Diversity Experiment

Results from applying our proposed software distribution model are reported in terms of the previously noted SDI. Outcomes for the two LP models (LP1 and LP2) are presented in Tables 3 and 4, respectively. Note that, for some larger and more complex problems, e.g., involving a two-connection 5,000-node network, we could not obtain precise optimal solutions via CPLEX even after a few days of computation. To address such situations, model gaps were set to less than 5%.

Table 3. Software Diversity Results of the LP Model 1 for the Two-Software Case

<table><tr><td rowspan="3"></td><td colspan="9">SSI = 5%</td><td rowspan="3"></td><td colspan="8">SSI = 40%</td></tr><tr><td colspan="9">Network connectivity = 1</td><td colspan="8">Network connectivity = 1</td></tr><tr><td colspan="4">NDC = Low</td><td colspan="5">NDC = High</td><td colspan="4">NDC = Low</td><td colspan="4">NDC = High</td></tr><tr><td>No. of nodes</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td>No. of nodes</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td></td></tr><tr><td>1,000</td><td>0.17</td><td>49.70</td><td>50.30</td><td>95.00</td><td>0.28</td><td>49.00</td><td>51.00</td><td>95.00</td><td>1,000</td><td>0.17</td><td>49.70</td><td>50.30</td><td>60.00</td><td>0.28</td><td>49.00</td><td>51.00</td><td>60.00</td><td></td></tr><tr><td>2,500</td><td>0.50</td><td>49.32</td><td>50.68</td><td>95.00</td><td>1.29</td><td>49.48</td><td>50.52</td><td>95.00</td><td>2,500</td><td>0.52</td><td>49.32</td><td>50.68</td><td>60.00</td><td>1.31</td><td>49.48</td><td>50.52</td><td>60.00</td><td></td></tr><tr><td>5,000</td><td>1.36</td><td>51.00</td><td>49.00</td><td>95.00</td><td>5.90</td><td>49.34</td><td>50.66</td><td>95.00</td><td>5,000</td><td>1.34</td><td>51.00</td><td>49.00</td><td>60.00</td><td>5.90</td><td>49.34</td><td>50.66</td><td>60.00</td><td></td></tr><tr><td rowspan="3"></td><td colspan="8">SSI = 5%</td><td rowspan="3"></td><td colspan="8">SSI = 40%</td><td></td></tr><tr><td colspan="8">Network connectivity = 2</td><td colspan="8">Network connectivity = 2</td><td></td></tr><tr><td colspan="4">NDC = Low</td><td colspan="4">NDC = High</td><td colspan="4">NDC = Low</td><td colspan="4">NDC = High</td><td></td></tr><tr><td>No. of nodes</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td>No. of nodes</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI(%)</td><td></td></tr><tr><td>1,000</td><td>133.71</td><td>31.00</td><td>69.00</td><td>89.39</td><td>2.09</td><td>89.70</td><td>10.30</td><td>92.39</td><td>1,000</td><td>129.20</td><td>31.00</td><td>69.00</td><td>56.52</td><td>2.11</td><td>89.70</td><td>10.30</td><td>58.31</td><td></td></tr><tr><td>2,500</td><td>390.91</td><td>72.12</td><td>27.88</td><td>89.79</td><td>13.32</td><td>10.24</td><td>89.76</td><td>92.13</td><td>2,500</td><td>420.69</td><td>71.88</td><td>28.12</td><td>56.62</td><td>12.87</td><td>10.36</td><td>89.64</td><td>58.25</td><td></td></tr><tr><td>5,000</td><td>6,895.67</td><td>22.78</td><td>77.22</td><td>89.70</td><td>63.46</td><td>88.94</td><td>11.06</td><td>92.27</td><td>5,000</td><td>5,970.24</td><td>24.18</td><td>75.82</td><td>56.71</td><td>62.74</td><td>88.94</td><td>11.06</td><td>58.22</td><td></td></tr></table>

Table 4. Software Diversity Results of the LP Model 2 for the Two-Software Case

<table><tr><td rowspan="3"></td><td colspan="9">SSI = 5%</td><td rowspan="3"></td><td colspan="8">SSI = 40%</td></tr><tr><td colspan="9">Network connectivity = 1</td><td colspan="8">Network connectivity = 1</td></tr><tr><td colspan="4">NDC = Low</td><td colspan="5">NDC = High</td><td colspan="4">NDC = Low</td><td colspan="4">NDC = High</td></tr><tr><td>No. of nodes</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td>No. of nodes</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td></td></tr><tr><td>1,000</td><td>0.22</td><td>49.70</td><td>50.30</td><td>95.00</td><td>0.28</td><td>49.00</td><td>51.00</td><td>95.00</td><td>1,000</td><td>0.17</td><td>49.70</td><td>50.30</td><td>60.00</td><td>0.28</td><td>50.70</td><td>49.30</td><td>59.66</td><td></td></tr><tr><td>2,500</td><td>0.53</td><td>49.32</td><td>50.68</td><td>95.00</td><td>1.33</td><td>55.24</td><td>44.76</td><td>92.62</td><td>2,500</td><td>0.51</td><td>49.32</td><td>50.68</td><td>60.00</td><td>1.34</td><td>55.08</td><td>44.92</td><td>58.55</td><td></td></tr><tr><td>5,000</td><td>2.67</td><td>49.00</td><td>51.00</td><td>95.00</td><td>6.69</td><td>55.30</td><td>44.70</td><td>91.68</td><td>5,000</td><td>2.96</td><td>49.00</td><td>51.00</td><td>60.00</td><td>6.32</td><td>55.30</td><td>44.70</td><td>57.95</td><td></td></tr><tr><td rowspan="3"></td><td colspan="8">SSI = 5%</td><td rowspan="3"></td><td colspan="8">SSI = 40%</td><td></td></tr><tr><td colspan="8">Network connectivity = 2</td><td colspan="8">Network connectivity = 2</td><td></td></tr><tr><td colspan="4">NDC = Low</td><td colspan="4">NDC = High</td><td colspan="4">NDC = Low</td><td colspan="4">NDC = High</td><td></td></tr><tr><td>No. of nodes</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td>No. of nodes</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI(%)</td><td></td></tr><tr><td>1,000</td><td>6.01</td><td>69.70</td><td>30.30</td><td>86.76</td><td>1.23</td><td>95.50</td><td>4.50</td><td>89.14</td><td>1,000</td><td>5.88</td><td>69.70</td><td>30.30</td><td>54.98</td><td>1.25</td><td>95.50</td><td>4.50</td><td>56.48</td><td></td></tr><tr><td>2,500</td><td>9.98</td><td>75.56</td><td>24.44</td><td>86.37</td><td>7.58</td><td>96.52</td><td>3.48</td><td>89.31</td><td>2,500</td><td>10.33</td><td>75.56</td><td>24.44</td><td>54.77</td><td>7.55</td><td>96.52</td><td>3.48</td><td>56.58</td><td></td></tr><tr><td>5,000</td><td>60.14</td><td>77.60</td><td>22.40</td><td>86.61</td><td>47.11</td><td>96.90</td><td>3.10</td><td>89.97</td><td>5,000</td><td>58.06</td><td>77.60</td><td>22.40</td><td>54.92</td><td>40.11</td><td>95.03</td><td>4.97</td><td>56.38</td><td></td></tr></table>

4.2.1. Software Diversity Results with LP Model Solutions. LP1 creates the greatest possible software diversity (95% and 60% for 5% and 40% software similarities) regardless of degree centrality and the number of nodes on the one-connectivity networks. However, LP1 creates a slightly lower software diversity on the twoconnectivity networks. For highly central networks the

LP1 results in 92% and 58% diversities for 5% and 40% similarities, whereas in less central networks the corresponding diversities tend to be slightly lower than those with highly central networks, 90% and 57%, respectively.

LP2 also creates the greatest possible software diversity on the one-connectivity networks with lower degree centrality for both 5% and 40% of software similarity. In general, LP2 creates slightly lower software diversity than LP1 in all other cases. However, LP2 runs significantly faster than LP1 when the network size is large while it creates almost the same degree of software diversity for the less central and one-connectivity networks for both 5% and 40% of software similarity.

Table 5. Software Diversity Results of Targeted Distribution for the Two-Software Case

<table><tr><td rowspan="3"></td><td colspan="9">SSI = 5%</td><td rowspan="3"></td><td colspan="8">SSI = 40%</td></tr><tr><td colspan="9">Network connectivity = 1</td><td colspan="8">Network connectivity = 1</td></tr><tr><td colspan="4">NDC = Low</td><td colspan="5">NDC = High</td><td colspan="4">NDC = Low</td><td colspan="4">NDC = High</td></tr><tr><td>No. of nodes</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td>No. of nodes</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td></td></tr><tr><td>1,000</td><td>N/A</td><td>86.50</td><td>13.50</td><td>87.87</td><td>N/A</td><td>86.50</td><td>13.50</td><td>89.84</td><td>1,000</td><td>N/A</td><td>86.50</td><td>13.50</td><td>55.45</td><td>N/A</td><td>86.50</td><td>13.50</td><td>56.22</td><td></td></tr><tr><td>2,500</td><td>N/A</td><td>86.48</td><td>13.52</td><td>87.64</td><td>N/A</td><td>86.48</td><td>13.52</td><td>89.81</td><td>2,500</td><td>N/A</td><td>86.48</td><td>13.52</td><td>55.31</td><td>N/A</td><td>86.48</td><td>13.52</td><td>56.21</td><td></td></tr><tr><td>5,000</td><td>N/A</td><td>86.46</td><td>13.54</td><td>87.27</td><td>N/A</td><td>86.46</td><td>13.54</td><td>89.80</td><td>5,000</td><td>N/A</td><td>86.46</td><td>13.54</td><td>55.09</td><td>N/A</td><td>86.46</td><td>13.54</td><td>56.20</td><td></td></tr><tr><td rowspan="3"></td><td colspan="8">SSI = 5%</td><td rowspan="3"></td><td colspan="8">SSI = 40%</td><td></td></tr><tr><td colspan="8">Network connectivity = 2</td><td colspan="8">Network connectivity = 2</td><td></td></tr><tr><td colspan="4">NDC = Low</td><td colspan="4">NDC = High</td><td colspan="4">NDC = Low</td><td colspan="4">NDC = High</td><td></td></tr><tr><td>No. of nodes</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td>No. of nodes</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI (%)</td><td>Time (sec)</td><td>SW1 (%)</td><td>SW2 (%)</td><td>SDI(%)</td><td></td></tr><tr><td>1,000</td><td>N/A</td><td>63.20</td><td>36.80</td><td>82.78</td><td>N/A</td><td>63.20</td><td>36.80</td><td>82.83</td><td>1,000</td><td>N/A</td><td>63.20</td><td>36.80</td><td>51.86</td><td>N/A</td><td>63.20</td><td>36.80</td><td>51.89</td><td></td></tr><tr><td>2,500</td><td>N/A</td><td>63.20</td><td>36.80</td><td>82.81</td><td>N/A</td><td>63.20</td><td>36.80</td><td>82.81</td><td>2,500</td><td>N/A</td><td>63.20</td><td>36.80</td><td>51.87</td><td>N/A</td><td>63.20</td><td>36.80</td><td>51.87</td><td></td></tr><tr><td>5,000</td><td>N/A</td><td>63.22</td><td>36.78</td><td>82.81</td><td>N/A</td><td>63.22</td><td>36.78</td><td>82.81</td><td>5,000</td><td>N/A</td><td>63.22</td><td>36.78</td><td>51.87</td><td>N/A</td><td>63.22</td><td>36.78</td><td>51.87</td><td></td></tr></table>

In LP2, where the connectivity coeficient is introduced, the solution may increase the total number of shared vulnerabilities to make nodes with more connections share less vulnerabilities. LP2 also creates an unbalanced software distribution on the twoconnectivity networks. In the unbalanced software distribution, one of the software alternatives is distributed in as low as 3% of nodes. Network connectivity afects the software distribution in a way that nodes are highly connected and software cannot be distributed evenly to minimize the total number of shared vulnerabilities. This result indicates that running diferent software on a specifically selected few nodes can greatly improve software diversity (and eventually network resilience). In the later simulation results, we observe cases where relatively lower SDI for LP2 (versus LP1) results in a relatively higher epidemic threshold although the difference is small.

4.2.2. Comparison with Targeted Distribution Solutions. For benchmarking purposes, we used the targeted software distribution strategy, which is the most recent software distribution strategy developed to increase the epidemic threshold in scale-free networks (Pastor-Satorras and Vespignani 2008). In the targeted distribution, the most connected nodes in the network select one of the available software alternatives. The remaining nodes select the alternative software. In the case of the existence of three or more software alternatives, the targeted distribution strategy can be applied iteratively to the remaining nodes until there are no unutilized software alternatives. The targeted distribution thus considers the connectivity fluctuations of scale-free networks. The percentage of the most connected nodes is the critical fraction of immunized individuals, given as (Pastor-Satorras and Vespignani 2008)

$$
g _ {c} = \exp \left(\frac {- 2}{m \lambda}\right),\tag{17}
$$

where m is a number of connections created when one node is added to a network at each step and λ is a virus spreading rate.

We report the results of the targeted software distribution that can serve as the base value for the improvement in software diversity for the two-software case in Table 5. The targeted software distribution creates almost the same degree of software diversity regardless of network centrality. The factors afecting the software diversity results of the targeted distribution are the network connectivity and software similarity. For one-connectivity networks the targeted software distribution creates around 87% and 55% diversity for 5% and 40% similarities, respectively, whereas in two-connectivity networks the corresponding diversities tend to be slightly lower than those with one-connectivity networks, 82% and 51%, respectively. When the targeted distribution is compared with LP1 and LP2, both LP models always create significantly higher software diversity than the targeted distribution.

4.2.3. Results of the Three Software Case. Since we observe low software diversity in two connectivity networks, we may consider increasing software diversity by adding more software alternatives. Although we conducted a similar experiment for the three-software case, we decided to conduct an experiment with LP2 only because of the following reasons. First, LP2 runs significantly faster than LP1. Second, as explained in Section 4.3.2, the LP1 and LP2 models perform about the same except for some highly centralized networks. As expected, the software diversity always increased when additional software was deployed. However, the efect of deploying additional software was marginal when 5% software similarity was used, e.g., an improvement from 95% to 97%. The efect was greater when 40% software similarity was used, e.g., an improvement from 60% to 65%.

The result of LP2 with the three-software case indicates that our software distribution model can generate software distribution solutions for desired software diversity with a minimum number of software alternatives. For example, to have the SDI slightly greater than 55%, the targeted software distribution method requires at least three software alternatives when the software similarity is 40%. On the other hand, our model allows us to use only two software alternatives to create SDI greater than 55%.

## 4.3. Virus Propagation Experiment

To better evaluate the software distribution models, we developed a simulation model where a virus propagates based on shared vulnerabilities between software alternatives. The simulation code for this extended SIS model was written in C#. We then compared the performance of the LP model solutions for software distribution in terms of epidemic threshold. A higher epidemic threshold indicates a more efective software distribution. The experimental factors and levels were the same as those utilized in the software diversity experiments, whereas the performance measure is now epidemic threshold instead of SDI. Common random numbers were used to reduce variability in comparing the performance between the LP model solutions and targeted distribution solutions.

Additional experiments for the dynamic software allocation were also performed in two steps. First, a new node is added to the existing network using a preferential attachment mechanism that generates the power law distribution in Equation (1) (Barabási and Albert 1999). Second, after adding a new node to the existing network, software alternatives are assigned to a new node via Algorithm 3. The networks with 1,000 nodes were used as base networks, and expanded by 10%, 20%, and 30%, resulting in 1,100, 1,200, and 1,300 nodes, respectively. We evaluated the performance of the dynamic allocation algorithm solutions with that of fully optimized solutions obtained using LP2.

4.3.1. Simulation of Virus Propagation. As noted earlier, if a software alternative contains a targeted vulnerability, the infection can spread to related alternatives. In modeling virus attacks (infections), we thus assume, for the sake of simplicity, that a particular type of attack targets a single vulnerability. For the twosoftware case, a single vulnerability dimension is randomly selected from a set of 20 possible dimensions, and then 10 randomly selected nodes are infected for each simulation replication. Hence, the probability of successful attacks (infection) depends on the number of vulnerable dimensions and how the vulnerabilities are shared among software alternatives.

For the three-software case, the attack probability had to be adjusted to ensure that the likelihood of an attack targeting a vulnerable dimension of one software alternative would be the same as that of the twosoftware case; and that the pairwise shared vulnerability would match that of the two-software case. Sixty vulnerability dimensions are used for the selection of an attack type. The simulation is then initialized with a set of 10 randomly infected nodes for each replication.

The experimental simulation was run until the system stabilized with a constant average percentage of infected nodes. After multiple trial runs with diferent model parameters, we determined that the system was able to reach a steady state within 10,000 time steps. The virus spreading rate, λ, appeared to be the critical point. If the virus spreading rate was below the epidemic threshold $\lambda _ { c } ,$ the infection brought it to an end, and the percentage of infected nodes went to zero at the end of the simulation. By contrast, if the virus spreading rate was equal to or greater than the epidemic threshold $\lambda _ { c } ,$ an infection persisted in the system, and the system stabilized with a constant percentage of infected nodes.

The epidemic threshold was obtained in an iterative manner. The VSR is initially set up to one (the infection rate <sup></sup> 1 and the disinfection rate <sup></sup> 1), and then either the infection rate or the disinfection rate is changed through subsequent simulation runs. If there are nonzero infected nodes after an initial simulation, the VSR is greater than the epidemic threshold, and the infection rate changes with the fixed disinfection rate, in which the epidemic threshold is smaller than one. If no infected nodes are found after an initial simulation, the VSR is below the epidemic threshold, and the disinfection rate changes with the fixed infection rate, in which the epidemic threshold is greater than one. The search stops when the two successive VSR values are within 0.0001. To find the average epidemic threshold for each experimental factor combination, we ran 20 replications with a randomly selected attack dimension and a random number stream for infection and disinfection process.

4.3.2. Simulation Experimental Results. Overall, both LP1 and LP2 show significantly better performance than targeted distribution. As noted previously, LP1 outperforms LP2 in terms of SDI, albeit the diference

## Figure 5. (Color online) Epidemic Threshold Comparison for the Two-Software Case

(a) Simulation results of LP2 and Targeted Distribution for one-connectivity network with SSI 5%  
![](/api/attachments/YSR6BWKM/fulltext/images/400ab21e1548f7b59995ec093cef8510ee7b1fcf11613ce5c5b4a98b7517e719.jpg)

(c) Simulation results of LP2 and Targeted Distribution for one-connectivity network with SSI 40%  
![](/api/attachments/YSR6BWKM/fulltext/images/2d0ee3bf80040df7297f1e8e1e74f88891f0dfd67cb6a7726a4a35b18e27ab59.jpg)

is negligible as can be seen in Tables 3 and 4. By contrast, the epidemic threshold of LP2 turns out to be slightly better than that of LP1 in some cases. Since LP2 requires much less solution time for large networks and the epidemic threshold is a better performance measure in practice, LP2 is better suited for real applications. Therefore, we only report the performance of LP2. The performance comparison of LP2 and targeted distribution solutions for the two-software case is shown in Figure 5.

For a network of 1,000 nodes, while the targeted distribution results in an epidemic threshold of 2.3, LP2 dramatically increases the epidemic threshold to 12.0 on the less centralized network and to 14.6 on the highly centralized network with one connection and 5% of software similarity. LP2 improves the epidemic threshold up to 1.6 on the less centralized network and up to 1.9 on the highly centralized network with two connections and 5% of software similarity. However, this improvement from epidemic thresholds of the targeted distribution (0.9 and 1.2) is not as dramatic as the improvement achieved with one connection case but indicates a significant (more than 50%) increase.

LP2 significantly increases the epidemic threshold up to 1.8 on the less centralized network and up to 2.1 on the high centralized network with one connection and 40% of software similarity, compared to the targeted distribution that results in epidemic thresholds of 1.2 and 1.4 for less centralized and highly centralized networks, respectively. LP2 increases the epidemic threshold up to 0.6 on the less centralized network and up to 1.0 on the highly centralized network with two connections and 40% of software similarity. The improvement indicates a significant (more than 50%) increase. Overall, the epidemic threshold decreases as the network size increases in all cases, but the improvement pattern remains the same.

(b) Simulation results of LP2 and Targeted Distribution for two-connectivity network with SSI 5%  
![](/api/attachments/YSR6BWKM/fulltext/images/e6e2f64fabb629475583d24e55afc1fdb8850517c069f66530596d859187d486.jpg)

(d) Simulation results of LP2 and Targeted Distribution for two-connectivity network with SSI 40%  
![](/api/attachments/YSR6BWKM/fulltext/images/f67f9ee7ef68816921b7296c97d854aa62e01fd8eef2295f16a2b18e3b6994e6.jpg)

LP2 performs significantly better for 5% of software similarity than 40% of software similarity. The high performance diference between 5% and 40% of software similarity indicates that the high percentage of shared vulnerabilities between two software alternatives significantly facilitates epidemic spreading on a network since two software become more similar with the increased number of shared vulnerabilities, which eliminates the security improvements gained from software diversity. Therefore, the network’s resilience against virus attacks increases as software similarity decreases.

LP2 performs significantly better for the one-connectivity networks than the two-connectivity networks. Network complexity is one of the major factors that restrict the performance of LP models. However, the restriction incurred by the large number of connections in a network may be lessened by deploying more software as evidenced by the three-software case below. This indicates that the impact of software diversity on network security depends on the balance between the number of software deployed on a network and the connectivity number of scale-free networks. The performance diferences of LP models between the oneconnectivity and the two-connectivity networks are high for 5% of software similarity. The performance diference between the one-connectivity and the twoconnectivity networks decreases for 40% of software similarity. Therefore, software similarity and connectivity are the two major factors that restrict the performance of LP2.

The simulation results of the three-software indicate that LP2 improves the epidemic threshold to a value greater than 17 for 5% of software similarity regardless of the number of connections and network degree centrality in the networks of 1,000 nodes. LP2 improves the epidemic threshold to a value greater than 2 for 40% of software similarity regardless of the number of connections and network degree centrality in the networks of 1,000 nodes. The performance of the LP model slightly decreases as the network size increases in all cases.

The results of LP2 in the three-software case indicate that deploying an extra software alternative dramatically improves the performance of LP2 for both one- and two-connectivity networks. The performance diferences of LP2 on the high and less central networks are less prominent in the three-software case. This indicates that deploying extra software may help overcome the restrictions of network centrality on software diversity. LP performs much better for 5% of software similarity than 40% of software similarity. This result is consistent with the result of the two-software case. LP2 performs much better for the one-connectivity networks than the two-connectivity networks. This result is consistent with the result of the two-software case. Finally, the results indicate that the LP2 always performs much better than the targeted distribution in all cases.

The simulation results confirm that higher software diversity created by the LP models provides better network resilience, which is measured by epidemic threshold. The LP models efectively isolate the vulnerabilities, thereby reducing the chances of infection spreading throughout the network. Similar to the software diversity experiment, all experimental factors significantly afect the epidemic threshold.

Algorithm 3 tends to generate near-optimal software distribution solutions for growing networks. The diference between the SDI of Algorithm 3 solutions and that of LP2 solutions is, on average, 0.12% with the maximum diference of 1.49%. These near-optimal solutions result in the epidemic thresholds that are the same as those created by LP2 for 10 out of 12 oneconnectivity networks. The maximum diference is 0.1 even with 30% network growth. These results show that LP2 provides the best possible network security, and for growing networks Algorithm 3 can maintain optimal or near-optimal solutions.

## 5. Discussions and Managerial Implications

Software diversity, when applied properly, can significantly increase the resilience of a computer network against security attacks, such as viruses and worms. Hence, cloud computing service providers and information technology (IT) managers need a tool that can support proper application of software diversity instead of arbitrarily distributing multiple software alternatives in their networks. We found that our proposed LP models enable software diversity to improve to the greatest extent possible, and increase the epidemic threshold of virus spreading networks. The resilience of the network gained from the LP models can be amplified by choosing the right combination of network topology and software alternatives. Our models are flexible enough to add constraints that make the real-world applications more realistic. For example, requiring Windows XP for a legacy medical device that needs network connection (Maron 2013) can be easily implemented in the LP models by simply adding a constraint while keeping the same decision variables.

## 5.1. Recommendations for Improving Network Resilience

We found that deploying dissimilar software without careful consideration, including targeted distribution, provides minimal gains in network resilience. Our results show that LP2 provides substantial improvements in network resilience when software alternatives are dissimilar. The high percentage of shared vulnerabilities between software alternatives significantly facilitates epidemic spreading on a network since software alternatives become more similar with the increased number of shared vulnerabilities, which lessens the security improvements gained from software diversity. Therefore, it is important for cloud service providers and IT managers to evaluate the similarities between software alternatives by examining known vulnerabilities and common software components to take full advantage of the benefits from using our LP models.

The epidemic threshold can be used as an ultimate performance measure of network resilience. IT managers can set a target threshold and make plans for software distribution decisions and software choices. To achieve the target threshold, first, managers select two most dissimilar software alternatives. Second, managers apply the LP2 model to obtain the optimal software distribution solution and compute the epidemic threshold via our simulation model. If the epidemic threshold is less than the target, they should consider buying or developing software that gives the desired dissimilarity, or changing software configurations, or adding new software. This process can be repeated until the desired epidemic threshold is reached.

We found that network connectivity afects the performance of the LP models. The LP models create higher software diversity on the one-connectivity networks than on the two-connectivity networks. Consistent with the software diversity results, the simulation results show that the LP models improve network security for the one-connectivity networks higher than network security for the two-connectivity networks. This result implies that for cloud service providers who build their networks for new or expanded services, low connectivity network designs can provide better security and service reliability by avoiding service disruptions from security attacks. However, it is important to note that low connectivity may adversely afect the infrastructure reliability. Network security is among the top concerns of organizations considering adopting cloud services (Armbrust et al. 2010). Hence, cloud service providers can diferentiate themselves by providing an improved level of security and service reliability through a careful network design along with the use of our LP models.

However, network redesign can be impractical for organizations whose existing network has a large number of connections for the purpose of supporting their primary business processes. Deploying additional software alternatives to increase software diversity is still a viable option for these organizations although it can be costly because of possible loss of network efects and economies of scale in maintaining heterogeneous software (Chen et al. 2011). The LP models create significantly higher software diversity than targeted distribution solutions in both two- and threesoftware cases. The simulation results show that LP2 improves network security in both two- and threesoftware cases. Therefore, using our LP models, organizations can increase network resilience with a few software alternatives.

## 5.2. Cost of Software Diversity

As widely noted in the software diversity literature, there are functionally equivalent software alternatives in the markets such as web browsers, DMBS, firewalls, and routers (Baudry and Monperrus 2015). Middleware and software adapters also provide interoperability and compatibility between various software alternatives (August et al. 2014, Chen et al. 2011). Nonetheless, software diversity does indeed have drawbacks in terms of increased administration and support costs, as well as possible loss of economies of scale (Chen et al. 2011).

Two possible extensions to the proposed LP models can be explored to consider the trade-of between improved security and increased costs. The first would be to explicitly consider the costs in the objective function of the LP models. The cost term could, for example, be a function of the number of installations and software alternatives in a given case. A caveat is that such an approach could add additional computational complexity to the model. The cost function might thus require further theoretical and empirical support, which is beyond the scope of this paper.

The second extension would involve a two-step process, where an IT manager first determines the minimum number of installations that can mitigate the cost of diversity. These could include, for example, the loss of administrative eficiency, economies of scale, and licensing cost savings. Such phenomena would then add the following constraint to the originally proposed LP models:

$$
\sum_ {i = 1} ^ {n} X _ {i k} \geq \bar {n} _ {k} \quad \forall k \in \{1, \ldots , s \},\tag{18}
$$

where $\bar { n } _ { k }$ is the minimum number of installations for software k.

We believe that this latter approach of adding a minimum number of installations for each software alternative is more realistic. This is supported by the fact that such practices can be found in a variety of organizations. For example, supporting Mac OS was not very common when Windows OS was the dominant OS. This was mainly because of the administrative eficiency and lack of required staf and/or training. However, as more users prefer Mac OS because of its improved compatibility with Apple devices, IT managers have begun to generate greater support for Mac machines (Endler 2014).

In this regard, we conducted an experiment by adding the minimum number of installations constraint (18). This was designed to examine any differences in epidemic threshold. We set the minimum number of installations at 30% of the total possible installations. The results, shown in Table 6, suggest that the epidemic thresholds for one-connectivity networks did not change from those without the constraint. Even for two-connectivity networks, significant improvements versus targeted distributions were evident in most cases. A particularly important case was that for 5% software similarity.

From these analyses, it seems clear that our proposed LP models with the minimum installations constraint can serve as an efective tool in evaluating the trade-of(s) between security improvements gained from software diversity and the costs of deploying additional software alternatives.

Table 6. Simulation Results of the LP Model 2 for the Two-Software Case with Minimum Software Installations Constraint (Min <sup></sup> 30%)

<table><tr><td rowspan="3">No. of nodes</td><td colspan="4">SSI = 5%</td><td rowspan="3">No. of nodes</td><td colspan="4">SSI = 40%</td></tr><tr><td colspan="2">Network connectivity = 1</td><td colspan="2">Network connectivity = 2</td><td colspan="2">Network connectivity = 1</td><td colspan="2">Network connectivity = 2</td></tr><tr><td>NDC = Low Threshold</td><td>NDC = High Threshold</td><td>NDC = Low Threshold</td><td>NDC = High Threshold</td><td>NDC = Low Threshold</td><td>NDC = High Threshold</td><td>NDC = Low Threshold</td><td>NDC = High Threshold</td></tr><tr><td>1,000</td><td>12.054</td><td>14.601</td><td>1.590</td><td>1.673</td><td>1,000</td><td>1.771</td><td>2.044</td><td>0.615</td><td>0.896</td></tr><tr><td>2,500</td><td>10.994</td><td>11.443</td><td>1.297</td><td>1.464</td><td>2,500</td><td>1.485</td><td>1.564</td><td>0.527</td><td>0.732</td></tr><tr><td>5,000</td><td>9.093</td><td>9.909</td><td>1.176</td><td>1.301</td><td>5,000</td><td>1.379</td><td>1.380</td><td>0.517</td><td>0.619</td></tr></table>

## 6. Conclusions

We analyzed the impact of software diversity on network security with experiments that involve optimization and simulation models. In doing so, we developed two LP models that minimize the shared vulnerabilities in scale-free networks after defining measures for software diversity in a network and software similarity for multiple alternatives. We also developed a dynamic software allocation algorithm for growing networks. We then developed an epidemic spreading model based on the SIS model and tested the efectiveness of software diversity created by the proposed LP models against the spreading of computer viruses. Finally, we showed that both the LP models and the dynamic allocation algorithm generated solutions that efectively increase the epidemic threshold in various scale-free networks when shared vulnerabilities exist between software alternatives.

This study makes several important theoretical contributions to the literature. This is the first study that uses information theory-based optimization models to improve network security. It is also the first study that combines both software diversity and virus propagation in the presence of shared vulnerabilities by developing deterministic models for the former and a simulation model for the latter.

The study expands the concept of software diversity by considering the shared vulnerabilities between software alternatives, and subsequently develops a new software diversity metric based on information theory. It thus develops the theory for, and then tests how software diversity afects network security in the presence of shared vulnerabilities. In addition, this research uniquely extends the SIS model to take into account viruses spreading through common vulnerabilities. We also show that a high SDI results in improved network resilience against the spread of viruses under various network- and software-related factors.

The separation of the software diversity optimization model from the virus propagation simulation model allowed for more flexibility in the LP formulation. The probabilistic nature of the vulnerabilities and their exploits was primarily addressed in the virus propagation simulation model. Hence, the deterministic software diversity optimization models, which were developed using information gain coeficients, were able to easily account for the cost of that diversity. We believe this aspect to possibly be the most unique and important contribution to the literature. We show that software diversity with the right combination of network topology and software alternatives allows an organization to create a highly resilient network, as shown by increased epidemic thresholds in our simulations.

The current study also makes important contributions to practice. Given that antivirus solutions are becoming less efective because of the camouflaging tactics such as encryption and mutations employed by malware (Lin and Stamp 2011), increasing software diversity can be an additional defense against security attacks. Hence, IT managers and cloud service providers can use the proposed LP models and dynamic software allocation as an efective tool to increase software diversity. We also suggest the use of epidemic threshold as a metric for network resilience while making practical recommendations based on our findings from this study. Finally, we demonstrated the use of an additional constraint along with our LP models to capture the trade-of between improvements gained from software diversity and the cost of deploying additional software alternatives. Although this approach is practical, future research may explore a formal modeling of the cost of software diversity.

In some organizations, decision makers choose software without security considerations. Our virus propagation model with an epidemic threshold can still be useful to measure the current status of network resilience. Should security experts determine that the current network is highly vulnerable (low epidemic threshold), software diversification using our models will result in a significantly higher epidemic threshold.

## Acknowledgments

The authors would like to thank the senior editor, associate editor, and four anonymous reviewers for their constructive comments and guidance in the review process.

## References

Alber J, Fellows MR, Niedermeier R (2004) Polynomial-time data reduction for dominating set. J. ACM 51(3):363–384.

Albert R, Jeong H, Barabási AL (2000) Error and attack tolerance of complex networks. Nature 406:378–382.

Alhazmi OH, Malaiya YK, Ray I (2007) Measuring, analyzing and predicting security vulnerabilities in software systems. Comput. Security 26(3):219–228.

Armbrust M, Fox A, Grifith R, Joseph AD, Katz R, Konwinski A, Lee G, et al. (2010) A view of cloud computing. Comm. ACM 53(4):50–58.

Arora A, Krishnan R, Telang R, Yang Y (2010) An empirical analysis of software vendors’ patch release behavior: Impact of vulnerability disclosure. Inform. Systems Res. 21(1):115–132.

August T, Niculescu MF, Shin H (2014) Cloud implications on software network structure and security risks. Inform. Systems Res. 25(3):489–510.

Bailey MG (2005) Malware resistant networking using system diversity. Proc. 6th Conf. Inform. Tech. Ed. (ACM, New York), 191–197.

Bailey NJT (1975) The Mathematical Theory of Infectious Diseases and Its Applications (Oxford University Press, New York).

Barabási AL, Albert R (1999) Emergence of scaling in random networks. Science 286:509–512.

Barabási AL, Bonabeau E (2003) Scale-free networks. Sci. Amer. 288(5):60–69.

Barabási AL, Albert R, Jeong H (2000) Scale-free characteristics of random networks: The topology of the world-wide web. Physica A 281:69–77.

Barthelemy M, Barrat A, Pastor-Satorras R, Vespignani A (2005) Dynamical patterns of epidemic outbreaks in complex heterogeneous networks. J. Theoret. Biol. 235(2):275–288.

Baudry B, Monperrus M (2015) The multiple facets of software diversity: Recent developments in year 2000 and beyond. ACM Comput. Surveys 48(1):1–26.

Birman KP, Schneider FB (2009) The monoculture risk put into context. IEEE Security Privacy 7(1):14–17.

Borgatti SP, Everett MG, Freeman LC (2002) Ucinet for windows: Software for social network analysis. Analytic Technologies, Harvard, MA.

Börner K, Sanyal S, Vespignani A (2007) Network science. Annual Rev. Inform. Sci. Tech. 41:537–607.

Brynjolfsson E, Kemerer C (1996) Network externalities in microcomputer software: An econometric analysis of the spreadsheet market. Management Sci. 42(12):1627–1647.

Caldarelli G, Marchetti R, Pietronero L (2000) The fractal properties of Internet. Europhysics Lett. 52(4):386–391.

Chen P, Carley KM (2004) The impact of countermeasure propagation on the prevalence of computer viruses. IEEE Trans. Systems, Man, Cybernetics, Part 2 34(2):823–833.

Chen P, Kataria G, Krishnan R (2005) Software diversity for information security. Proc. 4th Workshop Econom. Inform. Systems, Boston.

Chen P, Kataria G, Krishnan R (2011) Correlated failures, diversification, and information security risk management. MIS Quart. 35(2):397–422.

Cover TM, Thomas JA (2006) Elements of Information Theory (John Wiley & Sons, Hoboken, NJ).

Cox B, Evans D, Filipi A, Rowanhill J, Hu W, Davidson J, Knight J, Nguyen-Tuong A, Hiser J (2006) N-variant systems: A secretless framework for security through diversity. Proc. 15th USENIX Security Sympos. (USENIX, Berkeley, CA), 1–16.

CPLEX (2015) Starting from a solution: MIP starts. http://www -01.ibm.com/support/knowledgecenter/SSSA5P\_12.6.3/ilog .odms.cplex.help/CPLEX/UsrMan/topics/discr\_optim/mip/ para/49\_mipStarts.html.

Eckhardt DE, Lee LD (1985) A theoretical basis of multi-version software subject to coincident errors. IEEE Trans. Software Engrg. 11(12):1511–1517.

Endler M (2014) Mac enterprise adoption grows. InformationWeek (June 11), http://www.informationweek.com/infrastructure/pc -and-servers/mac-enterprise-adoption-grows/d/d-id/1269595.

Faloutsos M, Faloutsos P, Faloutsos C (1999) On power-law relationships of the Internet topology. ACM SIGCOMM Comput. Comm. Rev. 29(4):251–262.

Freeman LC (1979) Centrality in social networks: Conceptual clarification. Soc. Networks 1:215–239.

Garcia M, Bessani A, Gashi I, Neves N, Obelheiro R (2011) OS diversity for intrusion tolerance: Myth or reality? Proc. IEEE/IFIP Internat. Conf. Dependable Systems Networks (IEEE Computer Society, Los Alamitos, CA), 383–394.

Goodrich MT, Tamassia R (2001) Algorithm Design: Foundations, Analysis, and Internet Examples (John Wiley & Sons, New York).

Gorbenko A, Kharchenko V, Tarasyuk O, Romanovsky A (2011) Using diversity in cloud-based deployment environment to avoid intrusions. Troubitsyna EA, ed. Software Engrg. Resilient Systems. SERENE 2011, Lecture Notes Comput. Sci., Vol. 6968 (Springer, Berlin Heidelberg), 145–155.

Gray RM (2013) Entropy and Information Theory (Springer-Verlag, New York).

Hill MO (1973) Diversity and evenness: A unifying notation and its consequences. Ecology 54(2):427–432.

Hughes RP (1987) A new approach to common cause failure. Reliability Engrg. 17(3):211–236.

Karp RM (1972) Reducibility among combinatorial problems. Miller RE, Thatcher JW, eds. Complexity of Computer Computations (Plenum, New York), 85–103.

Katz ML, Shapiro C (1985) Network externalities, competition, and compatibility. Amer. Econom. Rev. 75(3):424–440.

Katz ML, Shapiro C (1986) Technology adoption in the presence of network externalities. J. Political Econom. 94(4):822–841.

Kephart JO, White SR (1991) Directed-graph epidemic models of computer viruses. Proc. IEEE Sympos. Res. Security Privacy (IEEE Computer Society, Washington, DC), 343–359.

Kephart JO, White SR (1993) Measuring and modeling computer virus prevalence. Proc. IEEE Sympos. Security Privacy (IEEE Computer Society, Washington, DC), 2–15.

Kim J, Radhakrishnan S, Dhall SK (2004) Measurement and analysis of worm propagation on Internet network topology. Proc. 13th Internat. Conf. Comput. Comm. Networks, (IEEE, Chicago), 495–500.

Lala JH, Schneider FB (2009) IT monoculture security risks and defenses. IEEE Security Privacy 7(1):12–13.

Larsen P, Brunthaler S, Franz M (2014) Security through diversity: Are we there yet? IEEE Security Privacy 12(2):28–35.

Lin D, Stamp M (2011) Hunting for undetectable metamorphic viruses. J. Comput. Virology 7(3):201–214.

Littlewood B, Miller DR (1989) Conceptual modeling of coincident failures in multi-version software engineering. IEEE Trans. Software Engrg. 15(12):1596–1614.

Littlewood B, Popov P, Strigini L (2001) Modeling software design diversity—A review. ACM Comput. Surveys 33(2):177–208.

MacKay DJC (2003) Information Theory, Inference, and Learning Algorithms (Cambridge University Press, Cambridge, UK).

Maron DF (2013) A new cyber concern: Hack attacks on medical devices. Sci. Amer. (June 25), http://www.scientificamerican .com/article/a-new-cyber-concern-hack/.

Medina A, Matta I, Byers J (2000) On the origin of power laws in Internet topologies. Comput. Comm. Rev. 30(2):18–28.

Mitchell TM (1997) Machine Learning (McGraw-Hill, New York).

Moreno Y, Pastor-Satorras R, Vespignani A (2002) Epidemic outbreaks in complex heterogeneous networks. Eur. Physical J. B 26(4):521–529.

Neti S, Somayaji A, Locasto ME (2012) Software diversity: Security, entropy and game theory. 7th USENIX Workshop Hot Topics Security (USENIX, Bellevue, WA), 1–6.

Nichols S (2015) Conficker is back—And it’s infecting police body cams. The Register (November 14), http://www.theregister.co .uk/2015/11/14/remember\_conficker\_its\_back\_and\_its\_infecting\_ police\_body\_cams/.

Nooy WD, Mrvar A, Batagelj V (2005) Exploratory Network Analysis with Pajek (Cambridge University Press, Cambridge, UK).

NWB Team (2006) Network workbench tool. Indiana University, Northeastern University, and University of Michigan, http:// nwb.slis.indiana.edu.

O’Donnell AJ, Sethu H (2004) On achieving software diversity for improved network security using distributed coloring algorithms. Proc. 11th ACM Conf. Comput. Comm. Security (ACM, New York), 121–131.

O’Donnell AJ, Sethu H (2005) Software diversity as a defense against viral propagation: Models and simulations. Proc. 19th Workshop Principles Adv. Distributed Simulation (IEEE Computer Society, Washington, DC), 247–253.

Partridge D, Krzanowski W (1997) Software diversity: Practical statistics for its measurement and exploitation. Inform. Software Tech. 39(10):707–717.

Pastor-Satorras R, Vespignani A (2001a) Epidemic dynamics and endemic states in complex networks. Physical Rev. E 63:066117.

Pastor-Satorras R, Vespignani A (2001b) Epidemic spreading in scalefree networks. Physical Rev. Lett. 86(14):3200–3203.

Pastor-Satorras R, Vespignani A (2002a) Epidemic dynamics in finite size scale-free networks. Physical Rev. E 65:035108.

Pastor-Satorras R, Vespignani A (2002b) Epidemics and immunization in scale-free networks. Bornholdt S, Schuster HG, eds. Handbook of Graphs and Networks: From the Genome to the Internet (Wiley-VCH, Berlin), 111–130.

Pastor-Satorras R, Vespignani A (2008) Immunization of complex networks. Physical Rev. E 65:036104.

Quinlan JR (1986) Induction of decision trees. Machine Learn. 1(1): 81–106.

Rényi A (1961) On Measures of Entropy and Information (University of California Press, Berkeley, CA).

Schneider D (2012) The state of network security. Network Security 2012(2):14–20.

Shannon C (1948) A mathematical theory of communication. Bell System Tech. J. 27(3):379–423.

Shannon CE, Weaver W (1949) The Mathematical Theory of Communication (University of Illinois Press, Urbana, IL).

Sokal RR, Sneath PH (1963) Principles of Numerical Taxonomy (WH Freeman, San Francisco).

Stamp M (2004) Risks of monoculture. Comm. ACM 47(3):120.

Sukwong O, Kim HS, Hoe JC (2011) Commercial antivirus software efectiveness: An empirical study. Comput. 44(3):63–70.

Temizkan O, Kumar RL, Park S, Subramaniam S (2012) Patch release behaviors of software vendors in response to vulnerabilities: An empirical analysis. J. Management Inform. Systems 28(4):305–337.

Vazirani VV (2001) Approximation Algorithms (Springer-Verlag, New York).

Wagner R, Pescatore J (2003) Use more than one operating system to limit the impact of malicious code attacks. Computer Weekly, http://www.computerweekly.com/feature/Use-more -than-one-operating-system-to-limit-the-impact-of-malicious -code-attacks.

Wang XF, Chen G (2003) Complex networks: Small-world, scale-free and beyond. IEEE Circuits Systems 3:6–20.

Wang Y, Wang C (2003) Modeling the efects of timing parameters on virus propagation. ACM Workshop Rapid Malcode (ACM, New York), 61–66.

Wang Y, Chakrabarti D, Wang C, Faloutsos C (2003) Epidemic spreading in real networks: An eigenvalue viewpoint. Proc. 22nd Internat. Sympos. Reliable Distributed Systems (IEEE Computer Society, Washington, DC), 25–34.

Wasserman S, Frost K (1994) Social Network Analysis: Methods and Applications (Cambridge University Press, Cambridge, UK).

Williams D, Hu W, Davidson JW, Hiser JD, Knight JC, Nguyen-Tuong A (2009) Security through diversity: Leveraging virtual machine technology. IEEE Security Privacy 7(1):26–33.

Zhang Y, Vin H, Alvisi L, Lee W, Dao SK (2001) Heterogeneous networking: A new survivability paradigm. Proc. Workshop New Security Paradigms (ACM, New York), 33–39.
