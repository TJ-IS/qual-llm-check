---
otero_id: 2036
otero_key: "PEU2NW8B"
title: "Developer Heterogeneity and Formation of Communication Networks in Open Source Software Projects"
authors: "Param Vir Singh; Yong Tan"
year: "2010"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222270307"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Developer Heterogeneity and Formation of Communication Networks in Open Source Software Projects

Param Vir Singh & Yong Tan

To cite this article: Param Vir Singh & Yong Tan (2010) Developer Heterogeneity and Formation of Communication Networks in Open Source Software Projects, Journal of Management Information Systems, 27:3, 179-210

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222270307

![](/api/attachments/PEU2NW8B/fulltext/images/27a2d9ee795bd994448327c9efe5cc815762a6ad9230d299a7d9589a239fc56a.jpg)

Published online: 09 Dec 2014.

![](/api/attachments/PEU2NW8B/fulltext/images/ed161c0ae9c0746498202c49f233c5c25d220cff5d04c012d2b3f78a1ba5b79a.jpg)

Submit your article to this journal

![](/api/attachments/PEU2NW8B/fulltext/images/4d3baf7c9114aaf09c1ffa66b2e2344c992adfe3429a127d6a795a75bd05497b.jpg)

Article views: 20

![](/api/attachments/PEU2NW8B/fulltext/images/8227efcea7b4367757f58c07143c681aaf2f192179cc8ddf376fdb0341a7ab0b.jpg)

View related articles

![](/api/attachments/PEU2NW8B/fulltext/images/b84bf65718adfcf4b70e5863a6a8d751480d5bef610d13931946259b01fd96d0.jpg)

Citing articles: 1 View citing articles

# Developer Heterogeneity and Formation of Communication Networks in Open Source Software Projects

Param Vir Sin gh and Yon g Tan

Param Vir Singh is an assistant professor of information systems at the Tepper School of Business, Carnegie Mellon University. His research interests include social networks, dynamic structural models, hidden Markov models, and open source software. A primary focus of his research is to design and study the effect of policy interventions on knowledge sharing behavior. His research has been published or is forthcoming at outlets such as Information Systems Research, ACM Transactions on Software Engineering and Methodology, and International Conference on Information Systems proceedings.

Yong Tan is an associate professor of information systems and Evert McCabe faculty fellow at the Michael G. Foster School of Business, University of Washington. His research interests include economics of information systems, social networks, electronic commerce, and software engineering. His research has been published in various journals, such as Management Science, Information Systems Research, and Operations Research. He is an associate editor of Management Science and Information Systems Research.

Abst ract : Over the past few years, open source software (OSS) development has gained a huge popularity and has attracted a large variety of developers. According to software engineering folklore, the architecture and the organization of software depend on the communication patterns of the contributors. Communication patterns among developers influence knowledge sharing among them. Unlike in a formal organization, the communication network structures in an OSS project evolve unrestricted and unplanned. We develop a non-cooperative game-theoretic model to investigate the network formation in an OSS team and to characterize the stable and efficient structures. Developer heterogeneity in the network is incorporated based on their informative value. We find that there may exist several stable structures that are inefficient and there may not always exist a stable structure that is efficient. The tension between the stability and efficiency of structures results from developers acting in their self-interest rather than the group interest. Whenever there is such tension, the stable structure is either underconnected across types or overconnected within type of developers from an efficiency perspective. We further discuss how an administrator can help evolve a stable network into an efficient one. Empirically, we use the latent class model and analyze two real-world OSS projects hosted at SourceForge. For each project, different types of developers and a stable structure are identified, which fits well with the predictions of our model. Overall, our study sheds light on how developer abilities and incentives affect communication network formation in OSS projects.

Key words and p hras es : analytical modeling, economics of IS, network formation, software development.

Recent y ears hav e wit nes ed t he emergence and growing popularity of open source software (OSS) products. OSS development provides many advantages, such as lower software and hardware costs, scaling and integration, lower switching costs, and better quality [23, 27, 32]. OSS products span many different categories: operating systems (Linux), desktop applications (OpenOffice, Mozilla), Web applications (Apache, JBoss), databases (MySQL), and development tools (GCC, Perl, Eclipse), and several others.

Software development has long been known to be an unstructured and nonroutine task [22], requiring a high level of knowledge sharing for effective coordination [1, 36]. According to Conway’s law, which is a rule of thumb, the architecture and the organization of a software product depend on the communication patterns of the contributors [39]. A direct consequence of this law is that two software modules are unlikely to interface correctly unless the designer and the implementer of one communicate with the designer and the implementer of the other. Kraut and Streeter [22] argue that the problem of coordinating activities among development teams is one of the major causes of software crisis, such as cost overrun, software unresponsiveness, software unreliability, and expensive modification costs.

In traditional organizations, there exist formal structured communication networks [37] that can be controlled and modified to suit the advent of new technology or development tools. However, this is not usually true for OSS development. In an OSS project, these communication structures are informal—they evolve in an unplanned manner, and developers are free to organize themselves in any network structure they prefer. There is no formal mechanism by which a specific communication structure can be imposed. Metaphors such as “bazaar,” “clique,” and “town council” are commonly identified with OSS development team structures. These structures represent varying patterns of communication among developers and have been observed in many different OSS projects [6, 15, 33, 34].

Developers in an OSS project vary in their skill sets, experiences, contributions, and motivations [30]. Strengths of the OSS phenomenon are closely associated with the evolution of potential developers through interaction with expert peers [27, 36]. However, the variety of developers attracted toward OSS projects implies greater asymmetries in the informative value of the developers. This heterogeneity among developers makes communicating with better-informed developers more desirable than with the rest. This raises two important research questions:

RQ1: What kind of communication structures are likely to emerge in an OSS project?

RQ2: Will these structures be socially efficient?

Answering these questions, we believe, would result in a more efficient and effective management/governance of OSS projects.

There is a vast literature in sociology that investigates the importance of social networks in many contexts, such as power and centrality of individuals in networks and roles and significance of different social ties [4, 37]. Although the idea of social networks has been applied to OSS development [15, 33, 34], prior research sheds little light on how observed network structures relate to different development scenarios or whether these structures are efficient. Also largely missing from these studies are the strategic models of how these network structures are formed and an understanding of the relationship between individual and societal welfare. Our research attempts to model the team structure based on rigorous theory and apply it to data collected from existing OSS projects to develop useful insights about these structures.

In this research, we develop a non-cooperative game-theoretic framework to study the formation of a communication network for an OSS project in which self-interested developers can form links through mutual consent, but sever links unilaterally. The developers are heterogeneous with respect to the value of the information (intrinsic value) they possess as well as the costs of link formation. Developers are segmented into different types based on their intrinsic values. The type-specific intrinsic values and costs of connecting with other developers enable us to identify stable networks with type-discriminating features. For example, developers may attempt to maintain an intra-type complete network but refuse to connect to other types. Conversely, developers may skip over their own types to reap the benefits of being connected to a developer of another type who might be well connected. We are primarily interested in studying the stability (from a value-allocation perspective) and the social efficiency (from a value-creation perspective) in these communication structures. We identify uniquely efficient structures for the complete value–cost domain. We show that efficient structures are not necessarily stable. Moreover, there may exist more than one stable structure. In general, whenever there is tension between the stability and efficiency of structures, the stable structure is found to be either underconnected across types or overconnected within a type from an efficiency perspective. The instability is a result of the “high”-type developers’ reluctance to form links with the “low” types. In other words, developer’s incentives may lead to underutilization of valuable social resources. We empirically analyze existing OSS projects to validate our analytical model and to obtain insights for better managing these projects.

Next we review related prior literature. In the third section, we provide the definitions comprising the general model. In the fourth section, we characterize the complete domain of value–cost relationships into different scenarios leading to the identification of different stable and uniquely efficient networks. In the fifth section, we provide empirical validation using data from OSS projects hosted at SourceForge (http:// sourceforge.net). To close the paper, we summarize the findings of the paper and provide future research directions.

## Literature Review

This work draws from bot h t he OSS lit erat ure and the game-theoretic models of endogenous network formation. OSS researchers have focused primarily on the motivations of a contributor to such projects. These motivations have been attributed to intellectual curiosity [30, 36], situated learning and identity construction [8, 27, 35], labor economics [24, 29], the need to improve one’s own specific programming skills [23], and the promise of higher future earnings [27]. These varied motivations of developers to participate in OSS projects bring in a wide variety of developers. For instance, a developer who joins an OSS project to reap reputation benefits when interacting with peers is more likely to be a highly skilled or advanced developer [24]. Conversely, a novice or an average skilled developer may join an OSS project to enhance his or her own software development skills by working with better skilled/ experienced developers [24, 36]. Hence, it is important to account for developer heterogeneity when studying open source projects. More recent studies have analyzed the effect of competition between OSS and proprietary software [19, 31] as well as the determinants of license choices [25, 32].

Recently, researchers have used social network theories to investigate the OSS phenomenon. This stream of research has focused primarily on how the developers contribute or communicate in an OSS project. The positions and relationships among actors in a social network play an important role in the efficiency of the network [17, 18]. Social network analysis (SNA) techniques also provide tools that allow inquiries into the patterns of interaction empirically [4, 9, 38]. Many of the supposed strength of OSS projects are closely related with the communication structure. Grewal et al. [15], Singh [33], and Singh et al. [34] find that the structure of an interproject network affects knowledge sharing within and across open source projects and, hence, affects their success. Montazemi et al. [28] show that in electronic trading systems, the market structure of embedded interpersonal ties enables participants to take advantage of information asymmetry for profit taking. Our work differs from those studies in four aspects. First, the network formation process is endogenous in our model. In most of the studies discussed above, the network structure is considered exogenous. The primary interest of those studies is to understand the impact of network structure on project success [15, 33, 34]. In contrast, our primary interest is to understand the underlying processes behind network formation. Second, we incorporate developer heterogeneity into the network structure. The extant literature on OSS, which takes a social network theoretical lens, assumes that the developers are homogeneous in their ability [6, 15, 33, 34]. This follows from the extant social networks research and is typically considered to simplify the network measures construction. However, as discussed earlier, OSS projects attract developers with varying abilities. We are interested in studying how the heterogeneity in the ability of developers affects network formation among developers. Third, we characterize different scenarios leading to the formation of various stable and uniquely efficient networks. Prior research on OSS developer networks does not consider efficient networks. Finally, in the empirical section, unlike prior studies, we consider a link to exist between two developers only if they have communicated multiple times (i.e., stability of a link is tied to its strength). In contrast, earlier studie have assumed a clique-type network structure for every project where all developer within the network are directly connected with each other [15, 33, 34].

Network formation theories can be categorized into two streams based on the link formation mechanism (1) where the actors form links unilaterally (e.g., [2, 11, 17]), and (2) where links are formed based on bilateral agreement (e.g., [3, 7, 12, 18]). Network theories can also be partitioned into two groups based on the symmetry/asymmetry of the agents involved. The majority of network formation studies involve symmetric or homogeneous agents (e.g., [2, 3, 17, 18]). In a study involving homogeneous players and bilateral link formation, for example, Jackson and Wolinsky [18] find that stable networks tend to be overconnected from an efficiency perspective when costs of link formation are high. However, we consider heterogeneous players under a similar setting and find that stable networks tend to be either underconnected across developer types or overconnected within a type. In prior literature, models involving heterogeneous players are few and quite recent. Galeotti et al. [10] study the stability of networks with players who are heterogeneous in values as well as cost. They assume costs of link formation within group to be lower than across groups, and that links can be formed by individuals unilaterally, but the flow of benefits to be frictionless and two-sided. Their main result is that the strict Nash network is either empty, a center-sponsored star, or of a minimal architecture, and that the heterogeneity is unimportant for the architecture of the network. This result is in direct contrast to our findings, which show that heterogeneity significantly affects the network architecture. Galeotti et al. [10] make a simplifying, though unrealistic, assumption that the benefit from an indirect communication between two agents is the same as if they have a direct link between them. The minimal architecture in their result is a direct consequence of this assumption. McBride [26] studies a non-cooperative network formation game characterized by imperfect information about the valuation of individuals. Haller and Sarangi [16] study network formation games considering heterogeneous reliability levels across individuals. Johnson and Gilles [20] introduce spatial heterogeneity in individuals. For studies investigating the dynamics of network formation, see Watts [38] and the references cited therein.

## Model Setup and Definitions

The p rop os ed model can be us ed t o st udy p at erns , flow, and effect of communication in the social network of developers. It is based on graph theory and models the communications among developers. In the graph, nodes represent developers and arcs represent the bilateral relationships among them. Each developer possesses some information valued by other developers. This information may be due to expertise in coding, code architecture, bug fixing, software licensing, patch management, and documentation, or it could be information about bugs and feature demands, among others. Developers in our model form links, for which they incur costs that may be interpreted in terms of time, effort, or opportunity costs.

Developers are assumed to be heterogeneous in the value of the information (intrinsic value) they possess and the costs they incur when forming links. To maintain parsimony, we segment the developers into only two types, “high” and “low,” based on their intrinsic value. For instance, the high-type developers are generally those who have higher skill sets and more experience in the development process. These hightype developers usually contribute to the detailed design and core code development.

Thus, they usually possess more relevant information about the project. This, combined with their greater skill set in the context of the project, would imply that they have the ability to contribute more than the low types in an information exchange about the project.<sup>1</sup> Below, we analyze data collected from real-world OSS projects and find strong evidence of this type of developer heterogeneity.

Most developers participate in OSS projects only on a part-time basis [27, 39]. Highly skilled developers are also in demand outside and have higher opportunity costs for the time they spend participating in OSS projects. To model this behavior, we assume that the high types incur higher costs of link formation compared to the low types.

In communication networks, reciprocity of a link is necessary, and mutual consent is thus needed to establish or maintain the link [18]. Hence, communication link formation is assumed to be a bilateral decision. A developer can augment his or her information by interacting with other developers with formed links. A developer derives full value from the ones he or she is directly connected to and discounted value from the ones he or she is indirectly connected to $( \mathrm { i . e . } ,$ connected through his or her adjacent developers). Direct communication is costly, and the value of communication from the other agents depends on the distance to those agents. Each developer is rational and weighs the value from a link against the cost of forming it.

## Definitions

Let $H = \{ 1 , . . . , m \}$ and $L = \{ 1 , . . . , n \}$ be finite sets of developers having “high” and $\mathrm { \Omega ^ { 6 6 } } \mathrm { \Omega } ^ { 6 6 }$ information value levels, respectively. Let $N = H \cup L$ represent the set of all developers. The network relation between the developers is a graph whose nodes are the developers and arcs are pairwise relations.

## Graphs

The complete graph, denoted $g ^ { N } { } _ { ; }$ , is a set of all subsets of N of size 2. The set of all possible graphs on N is then $\{ g | g \subset g ^ { N } \}$ . A link $i j \subset N$ directly connects developers i and j. The graphs obtained by adding and severing link $i j$ to graph g are denoted by $g + ( i j )$ and $g - ( i j )$ , respectively.

## Path

A path in g connecting $i _ { 1 }$ to $i _ { n } , i _ { 1 } \neq i _ { n }$ , is a set of distinct nodes $\{ i _ { 1 } , i _ { 2 } , . . . , i _ { n } \}$ such that $\{ i _ { 1 } i _ { 2 } , i _ { 2 } i _ { 3 } , . . . , i _ { n - 1 } i _ { n } \} \subset { \bf g }$

## Component

Let $N ( g ) = \{ i | \exists j \mathrm { s . t . } i j \subset \mathbf { g } \}$ . A graph $g ^ { \prime } \subset g$ is a component of g, if for all $i , j \in N ( g ^ { \prime } )$ , $i \neq j ,$ , there exists a path in $g ^ { \prime }$ connecting i and $j ,$ and for any $i , j \in N ( g ^ { \prime } ) , i j \in g$ , implies $i j \in \mathrm {  ~ g ^ { \prime } ~ }$

The amount of total value generated and the distribution of this value among the developers are determined by value functions and allocation rules. In traditional game theory, they would just depend on the developers involved, but here they depend on the network structure as well.

## Values

The value function V of graph g is represented as $V \colon \{ g \mid g \subset g ^ { N } \} \to R$ . We consider the total value to be the aggregate of developer utilities, $V ( g ) = \Sigma _ { _ { i \in N ( g ) } } u _ { _ { i } } ( g )$ , where $u _ { i } \colon \{ g | g \subset g ^ { N } \} \to \mathbb { R }$

The above value function is a component additive in the sense that $\begin{array} { r } { \sum _ { h \in C ( g ) } V ( h ) = V ( g ) } \end{array}$ where $C ( g )$ represents a set of all the components of graph g. This condition rules out externalities across components but allows them within components. For instance, the Apache Web server community has separate user-to-user help and development forums [24]. If there is no link between the user-to-user help forum and the development forum, then the benefits of learning would not travel from one forum to the other.

## Allocation Rule

The allocation rule $Y \colon \{ g : g \subset g ^ { N } \} \times V \to R ^ { N }$ describes how the value generated in a network is distributed among developers. $Y _ { i } ( g , V )$ is the value received by developer i from graph g under V. The utility of developer i from a graph g under the allocation rule $Y _ { _ { i } } ( g , V )$ is then given by

$$
u _ {i} (g) = \sum_ {j \neq i} \delta^ {t _ {i j} - 1} w _ {i j} - \sum_ {j: i j \in g} c _ {i j},
$$

where $t _ { _ { i j } }$ is the number of links in the shortest path between i and $j \left( t _ { _ { i j } } = \infty \right.$ if there is no path between i and j ), and $0 \leq \delta < 1$ is the discount/decay rate,

$$
c _ {i j} = \left\{ \begin{array}{l l} c _ {h} & \text {if} \quad i \in H \\ c _ {l} & \text {if} \quad i \in L \end{array} \right. \text {and} w _ {i j} (g) = \left\{ \begin{array}{l l} v _ {h} & \text {if} \quad j \in H \\ v _ {l} & \text {if} \quad j \in L, \end{array} \right.
$$

where $\nu _ { { } _ { h } } \ge \nu _ { { } _ { l } }$ and $c _ { { } _ { h } } \geq c _ { { } _ { l } } .$ . Here $w _ { i j }$ is the value to developer i of the information possessed by developer j, and $c _ { i j }$ is the cost of link ij to developer i. Note that only direct links are costly, and both the participating developers incur the cost. The allocation rule, $Y _ { i } ( g , V )$ , described above is anonymous within type but not across types.<sup>2</sup> It can be easily seen that the allocation rule is not symmetric.

## Efficiency

A graph $g \subset g ^ { N }$ is strongly efficient if there exists no graph $g ^ { \prime } \subset g ^ { N }$ such that $V ( g ) < V ( g ^ { \prime } )$ The graph $g \subset g ^ { N }$ is said to defeat graph $g ^ { \prime } \subset g ^ { N } \mathrm { i f } \ V ( g ) > V ( g ^ { \prime } )$

## Stability

We only consider pairwise stability. A graph g is pairwise stable with respect to V and Y if (1) for all $i j \in \mathrm { ~ g } , Y _ { i } ( g , V ) \geq Y _ { i } ( g - i j , V )$ , and $Y _ { i } ( g , V ) \ge Y _ { i } ( g - i j , V )$ , and (2) for all $i j \in { \ g } , \operatorname { i f } \ Y _ { i } ( g , V ) < Y _ { i } ( g + i j , V )$ , then $Y _ { _ { j } } ( g , V ) > \dot { Y _ { _ { j } } } ( g + i j , V )$

The formation of a link requires the consent of both parties, but the severance can be done unilaterally. Pairwise stability could prove to be a weaker stability notion if the developers could act in groups. However, even in those cases, the pairwise stability is a necessary, but not a sufficient, condition for overall stability.

## Efficient and Stable Networks

We now cons ider efficiency and st ability of communication networks with high- and low-type developers. We note here that extending our analysis to more than two types of developers poses no conceptual difficulty, although the results are somewhat cumbersome and are therefore not included here. As defined earlier, | H | = m and $| L | = n$ ; we assume that $m , n \geq 3$

Proposition 1: In any pairwise stable network:

(a) There is at most one nonempty component having a low type,

(b) If there is a nonempty component having a low type, all the low types belong to it,

(c) There is at most one nonempty component having a high type,

(d) If there is a nonempty component having a high type, all the high types belong to it,

(e) If there is a nonempty component having a link between a high type and a low type, all the high and low types belong to it.

Proof: Proofs for are provided in the Appendix.

Proposition 1 indicates that developers end up linking to their own types. This has strong implications for the OSS phenomenon that derives its strengths from linking of developers across types. A stable network can have two components, each having one type. This would correspond to the formation of “cliques” for the high and low types. As is evident from the propositions that follow, cliques of two types are never efficient. However, there is evidence of clique-type structures in OSS projects. During the early days of development of Linux 8086, the communication structure represented a “clique” of core developers because of a huge quality difference between “core” and “average” developers [39].

## Mutually Beneficial High Type

In this case, a high type prefers forming links with all the other high types. Mathematically, this scenario is achieved when the intrinsic value and cost of a high type satisfy the following condition:

$$
v _ {h} \geq \overline {{c}} _ {h} \equiv \frac {c _ {h}}{1 - \delta}.\tag{1}
$$

![](/api/attachments/PEU2NW8B/fulltext/images/c5d30321a7718bd5666c06619ddd4aa0af0e3a81c7e4e6e3bb7c0942741e17de.jpg)  
Figure 1. The Completely Connected Network of the High and Low Types

If Equation (1) is satisfied, any stable or efficient network would have all the high types intralinked. For $\nu _ { { } _ { h } } \ge \bar { c } _ { { } _ { h } }$ any two high types that are not linked can increase their individual utilities by forming a link. The stability argument then follows directly from Proposition 1. The efficiency argument is as follows: consider that $g$ is an efficient network with single component and has two high-type developers that are not linked. Let these developers be $i , j \in H ,$ , where $i j \notin g .$ . Let $V ( g )$ be the value of component $g .$ . Then the values of component $g ^ { \prime }$ , where $g ^ { \prime } { = } g + i j$ is at least $V ( g ) + 2 \nu _ { { } _ { h } } - 2 8 \nu _ { { } _ { h } } - 2 c _ { { } _ { h } }$ . However, we know from Equation (1) that $\nu _ { { } _ { h } } - 8 \nu _ { { } _ { h } } - c _ { { } _ { h } } \geq 0$ , which implies that $V ( g ^ { \prime } ) \geq V ( g )$ . For a network with multiple components, the value of the network is increased by forming a link between the high types of the two components as $\nu _ { { } _ { h } } - c _ { { } _ { h } } \ge 0$

## Mutually Beneficial Low Type

In this case, a low type prefers to form links to all the other low types. This situation is achieved when the intrinsic value and cost of a low type satisfy the following condition:

$$
v _ {l} \geq \overline {{c}} _ {l} \equiv \frac {c _ {l}}{1 - \delta}.\tag{2}
$$

Following similar arguments as before, we claim that when Equation (2) is satisfied, an efficient and stable graph has all the low types directly connected to each other. The overall stable or efficient structure, given that Equations (1) and (2) are satisfied, would depend on the cost–value relationships across different types of developers.

Proposition 2: A completely linked network of the low and high types is

(a) Uniquely efficient if $\nu _ { { } _ { h } } \ge \bar { c } _ { { } _ { h } }$ and $\nu _ { { } _ { l } } \ge \bar { c } _ { { } _ { l } }$

(b) Uniquely stable $i f \nu _ { _ { l } } \ge \bar { c } _ { _ { h } } .$

The corresponding network structure for Proposition 2 is shown in Figure 1. The completely linked network is observed when the low-type developers make high-value contributions, as compared to the cost of link formation for the high-type developers. However, it may be efficient even when they do not. An interesting observation to be made here is that for $\bar { c } _ { { \scriptscriptstyle h } } > \nu _ { { \scriptscriptstyle l } } \ge \bar { c } _ { { \scriptscriptstyle l } }$ , the efficient structure of Proposition 2a is not stable. It can be shown that for this range, any stable network would not have complete interlinking between the high- and low-type developers. Such a stable network is clearly underconnected across type from an efficiency perspective. This happens due to the reluctance of the high types to form links with all the low types. The proposed structure is likely to be observed in scenarios where the costs of link formation are very low (relative to the values), which could be a possibility if all the developers involved in the project are highly skilled, altruistic, or motivated by incentives to support their community.

## Mutually Nonbeneficial Low Type

In this scenario, a low-type developer prefers indirect connections compared to a link to the other low-type developers. This situation arises if the following condition holds:

$$
v _ {l} <   \bar {c} _ {l}.\tag{3}
$$

Note that indirect connections do not incur any costs and, hence, are always preferred to having no connections at all:

Proposition 3: Given $\nu _ { { } _ { h } } \ge \bar { c } _ { { } _ { h } }$ and $\nu _ { { } _ { l } } < \bar { c } _ { { } _ { l } }$ , the uniquely efficient network structure has

(a) The high types completely intralinked and each low type linked to all the high types but no links between the low types $i f { \nu } _ { { } _ { h } } + { \nu } _ { { } _ { l } } \ge { \bar { c } } _ { { } _ { h } } + { \bar { c } } _ { { } _ { l } }$

(b) The high types completely intralinked and the low types connected in the shape of a star with a high type at the center $i f { \nu } _ { { } _ { h } } + { \nu } _ { { } _ { l } } < \bar { c } _ { { } _ { h } } + \bar { c } _ { { } _ { l } }$ and $\nu _ { _ h } ( l + \delta ( m - l ) ) +$ $\nu _ { \scriptscriptstyle { l } } ( I + \ S ( n + m - 2 ) ) \geq c _ { \scriptscriptstyle { h } } + c _ { \scriptscriptstyle { l } } .$

The condition in Proposition 3a implies that a link between a low type and a high type adds more value to the network than an indirect connection. The first condition in Proposition 3b is the reverse of the condition in Proposition 3a; for Proposition 3b, an indirect connection between a low type and a high type is preferred to a link. The second condition in Proposition 3b ensures that the proposed structures defeat a single-component completely intralinked network of the high types and no links for the low types.

## Proposition 4: A network structure in which

(a) The high types are completely intralinked and each low type is linked to all the high types but not to another low type is never stable in the range where it is efficient.

(b) The high types are completely intralinked and the low types are connected in a star with a high type at the center is stable $i f \nu _ { _ h } \ge \bar { c } _ { _ h }$ and $c _ { _ h } \leq \nu _ { _ l } < \bar { c } _ { _ l }$

Figure 2 shows the network structures for Propositions 3 and 4. Although the network structure in Proposition 3a is efficient, Proposition 4a implies that a network

High types are completely intralinked and each low type linked to all the high types none of the low types linked to each other

![](/api/attachments/PEU2NW8B/fulltext/images/78e6e37a6daf0fee7de35458e5ca75562a33323d86618349261ea314dec91420.jpg)  
Figure 2. Network Structures from Propositions 3 and 4

will never stabilize to this structure for the value–cost range for which it is efficient. However, it is interesting to see that for a subrange for which Proposition 3a is efficient, the network may stabilize to the structure in Proposition 3b, which will be inefficient in that range. This indicates that a nondegenerate stable structure for this range is underconnected from an efficiency perspective. The value–cost of the two types suggests that in the efficient network, a high type incurs negative utility by forming a direct link with a low type to whom he or she may be indirectly connected, but the low type incurs a much higher positive utility from such a link formation. This is a scenario where the low-type developer gets a lot from the relationship but does not give back sufficiently. Here, the difference between the high and the low types would be quite large.

A plausible scenario for the structure in Proposition 3a is the case where the project under consideration is highly modular. The high types may be the ones with the skills that address the requirements of specific modules. The low types would be the ones with no special but basic skills. In an efficient structure, these low types can help the high types, as and when the requirement arises, by doing mundane tasks and, in return, getting some experience and knowledge. However, this would not be stable because a high type does not value a low type’s contribution to be high enough for him or her to incur the cost of link maintenance.

The network structure implied by Propositions 3b and 4b brings out the typediscriminating features of stable networks nicely. Here, the low types skip their own types to form links with a better-connected high type, whereas the high types stick to their own types. This structure could emerge in a situation where the low types are bug reporters and the high types are core developers. In such a network structure, a high type who acts as a connection between the high and low types is very important to the group. The project may suffer significantly if such a developer leaves the project abruptly.

## Mutually Nonbeneficial High Type

In this scenario, a high type prefers indirect connections to all the other high types. This situation arises if the following condition holds:

$$
v _ {h} <   \bar {c} _ {h}.\tag{4}
$$

Proposition 5: Given $\nu _ { _ h } < \bar { c } _ { _ h }$ and $\nu _ { { } _ { l } } \ge \bar { c } _ { { } _ { l } }$ , the uniquely efficient network structure is

(a) The low types completely intralinked and each high type linked to all the low types but not to another high type $i f { \nu } _ { { } _ { h } } + { \nu } _ { { } _ { l } } \ge { \bar { c } } _ { { } _ { h } } + { \bar { c } } _ { { } _ { l } }$

(b) The low types completely intralinked and the high types connected in a star with a low type at the center $i f { \nu } _ { { } _ { h } } + { \nu } _ { { } _ { l } } < \bar { c } _ { { } _ { h } } + \bar { c } _ { { } _ { l } }$ and $\nu _ { _ h } ( l + 8 ( m + n - 2 ) ) + \nu _ { \scriptscriptstyle l } ( l +$ $\begin{array} { r } { 8 ( n - I ) ) \geq c _ { \boldsymbol { h } } + c _ { \boldsymbol { l } } . } \end{array}$

The condition in Proposition 5a implies that a link between a low type and a high type adds more value to the network than an indirect connection. The first condition in Proposition 5b is the reverse of the condition in Proposition 5a. For Proposition 5b, an indirect link between a high and a low type is preferred to a direct link. The additional condition in Proposition 5b ensures that the value addition by the participation of all the high types is positive.

Proposition 6: A network structure in which

(a) The low types are completely intralinked and each high type is linked to all the low types, but not to another high type, is never stable in the range where it is efficient.

(b) The low types are completely intralinked and the high types are connected in a star with a low type at the center is stable $i f \nu _ { _ h } < \bar { c } _ { _ h }$ and $\nu _ { \scriptscriptstyle l } \ge m a x ( \bar { c } _ { \scriptscriptstyle l } , c _ { \scriptscriptstyle h } )$

Figure 3 shows the network structures from Propositions 5 and 6. The structure proposed in Proposition 5a is efficient for the specified range, but Proposition 5b implies that a network will never stabilize to that structure for that range. Here again, the instability is caused by the high-type developer’s reluctance to form links to all the low types. An interesting observation is the stability of the proposed structure in Proposition 6b. Here the high types skip their own types to form links with a better-connected low type. Moreover, the efficiency and stability ranges for this structure also intersect. Although, in isolation, links to a better-informed developer are preferred, a link to the low-type developer is preferred here due to within-component externalities.

The structures in Proposition 5 are efficient where the low types individually do not provide much useful information but as a group they can provide sufficient information. Moreover, here the low types can help each other more by answering questions. This might be the case where the high types are advanced developers and the low types are beginners with information about enhancing the usage of the product but little information about the minute details of code development. These low-type developers can discuss the new features that might be useful, reach a consensus, or develop small patches and provide the information to a high-type developer. The high type can then incorporate their suggestions into the code.

![](/api/attachments/PEU2NW8B/fulltext/images/232609c22b55c530b92c171f3ce0db56e9acc4267558b69fd5371f86ec82409c.jpg)  
Low types completely intralinked and each high type linked to all the low types but none of the high types linked to each other

![](/api/attachments/PEU2NW8B/fulltext/images/e8608c508b4cf873e8dbe0775099765fad1468b02e7f935d304072494cf9ff22.jpg)  
Low types completely intralinked and the high types connected in the shape of a star with a low type at the center  
Figure 3. Network Structures from Propositions 5 and 6

Proposition 7: Given $\nu _ { _ h } < \bar { c } _ { _ h }$ and $\nu _ { { } _ { l } } < \bar { c } _ { { } _ { l } }$ , the uniquely efficient network structure is

(a) A star structure comprising everyone with a high type at the center if

$$
v _ {h} - v _ {l} \geq \overline {{c}} _ {h} - \overline {{c}} _ {l}
$$

$$
v _ {h} (1 + \delta (m - 1)) + v _ {l} (1 + \delta (n + m - 2)) \geq c _ {h} + c _ {l}
$$

$$
\begin{array}{c} v _ {h} \left(n + 2 m - 2 + \delta (m - 1) (n + m - 2)\right) + v _ {l} \left(2 - n + \delta (n - 2 + n m)\right) \\ \geq (n + 2 m - 2) c _ {h} + (2 - n) c _ {l} \end{array}
$$

and

$$
\begin{array}{c} v _ {h} \left(n + 2 m - 2 + \delta (m - 1) (n + m - 2)\right) + v _ {l} \left(n + \delta n (n + m - 2)\right) \\ \geq c _ {h} \left(n + 2 m - 2\right) + n c _ {l}. \end{array}
$$

(b) A star structure comprising everyone with a low type at the center if

$$
v _ {h} - v _ {l} <   \overline {{c}} _ {h} - \overline {{c}} _ {l}
$$

$$
v _ {h} (1 + \delta (m + n - 2)) + v _ {l} (1 + \delta (n - 1)) \geq c _ {h} + c _ {l}
$$

$$
\begin{array}{c} v _ {h} \left(2 - m + \delta (m + m n - 2)\right) + v _ {l} \left(m + 2 n - 2 + \delta (n - 1) (n + m - 2)\right) \\ \geq c _ {h} (2 - m) + c _ {l} (m + 2 n - 2) \end{array}
$$

and

$$
\begin{array}{c} v _ {h} \left(m + \delta m (n + m - 2)\right) + v _ {l} \left(m + 2 n - 2 + \delta (n - 1) (n + m - 2)\right) \\ \geq m c _ {h} + c _ {l} (m + 2 n - 2). \end{array}
$$

The conditions $\nu _ { _ h } < \bar { c } _ { _ h }$ and $\nu _ { { } _ { l } } < \bar { c } _ { { } _ { l } }$ imply that, for efficiency reasons, indirect connections are preferred to direct links. The first conditions in Proposition 7a and 7b compare the values of the proposed structures of Proposition 7a and 7b. The second and third conditions in Proposition 7a and 7b compare their values with stars of only the high types and stars of only the low types, respectively. The fourth conditions of Proposition 7a and 7b are the nonnegative conditions for the values of the proposed structures. The efficient network selects a high or a low type as the center, depending on who has a lower disutility of forming a link with someone of the same type which may be indirectly connected to the potential center, $\nu _ { { } _ { h } } - \bar { c } _ { { } _ { h } } \mathrm { o r } \nu _ { { } _ { l } } - \bar { c } _ { { } _ { l } }$

Proposition 8: (a) A star structure comprising everyone with a high type at the center is stable $i f \nu _ { _ h } < \bar { c } _ { _ h }$ and $c _ { _ h } \leq \nu _ { _ l } < \bar { c } _ { _ l }$

(b) A star structure comprising everyone with a low type at the center is stable if v<sub>h</sub> < c\<sub>h</sub>, c<sub>l</sub> ≤ v<sub>l</sub> < c\<sub>l</sub> , and v<sub>h</sub> (m – 1)d + v<sub>l</sub>(1 + d (n – 1)) ≥ c<sub>h</sub> .

Figure 4 shows the network structures discussed in Propositions 7 and 8. Star structures would generally be observed during the bug reporting and fixing stages of a project. In such scenarios, the low types could be the bug reporters who want access to a high-type developer who can fix the bug or provide information about fixing the bug. Hence, the low type ends up forming a link with a high type if he or she can provide enough value to the high type or with a low type who is well connected to the high types. Value in a relationship among developers is generated through repeated interactions over time. Compared to core-code development, the repeated interactions in bug reporting and fixing stages between the same set of developers or a bug reporter and a developer are rare. Hence, the value generated is small. However, the costs incurred in the interactions may not be as small. This is due to the highly technical nature of the task involved. A bug fixer may have to spend a lot of time to understand a half-baked bug report or to find the root cause of the bug. If a project involves bug reporters who provide a detailed report with possible causes for the bug or a way to fix the bug, then it reduces the costs incurred by the high types by a significant amount. In such a scenario, it is likely that the network structure would be a star with a high type at the center. Conversely, for a project involving “half-clued” bug reporters, the stable structure could be a star comprising everyone with a low type at the center.

This kind of structure might be efficient during the bug-fixing phase of the project. The individual low-type developers can report bugs to the central developer (high type or low type), and each high type can then decide which task to pick. This might amount to the low-type developers organizing themselves in a way to entice the hightype developers to form links. Also note that the stability ranges for the structures in Proposition 8a and 8b do not intersect.

![](/api/attachments/PEU2NW8B/fulltext/images/92bde4dd1a0bf56a9668be9a574f3a7627dca3383407cc20d281195773a90d95.jpg)  
Low types completely intralinked and each high type linked to all the low types but none of the high types linked to one another

![](/api/attachments/PEU2NW8B/fulltext/images/cf203f50610c172afcaf3419a71eb19fce1b8eee3188de3c7a498b4beb39f248.jpg)  
Low types completely intralinked and the high types connected in the shape of a star with a low type at the center

Figure 4. Network Structures from Propositions 7 and 8

Proposition 9: (a) A star structure of only the high-type developers and no links for the low types is a uniquely efficient network structure if

$$
\frac {2 c _ {h}}{2 + (m - 2) \delta} \leq v _ {h} <   \overline {{c}} _ {h}
$$

$$
v _ {h} (1 + \delta (m - 1)) + v _ {l} (1 + \delta (n + m - 2)) <   c _ {h} + c _ {l}
$$

and

$$
\begin{array}{c} v _ {h} \left(2 - m + \delta (m + m n - 2)\right) + v _ {l} \left(m + 2 n - 2 + \delta (n - 1) (n + m - 2)\right) \\ <   c _ {h} (2 - m) + c _ {l} (m + 2 n - 2). \end{array}
$$

(b) A completely connected structure of only the high-type developers and no links for the low types is a uniquely efficient network structure $i f \nu _ { { } _ { h } } \ge \bar { c } _ { { } _ { h } } ,$ and

$$
v _ {h} (1 + \delta (m - 1)) + v _ {l} (1 + \delta (n + m - 2)) <   c _ {h} + c _ {l}.
$$

A star of the high types only would have a positive value only if $2 c _ { _ { h } } { \le } \nu _ { _ { h } } ( 2 + ( m - 2 ) \delta )$ is satisfied. The second condition in Proposition 9a ensures that the value of the proposed structure is higher than that of a star comprising everyone with a high type at the center. The third condition ensures that the value of the proposed structure is higher than that of a star comprising everyone with a low type at the center. The second condition in Proposition 9b ensures that the proposed structure defeats a network where all the high types are completely intralinked and the low types are connected in a star with a high type at the center.

Proposition 10: (a) A star network of only the high-type developers and no links for the low types is a stable structure $i f c _ { _ h } \le \nu _ { _ h } < \bar { c } _ { _ h }$ and $\nu _ { { } _ { l } } < c _ { { } _ { l } }$

(b) A completely intralinked network of only the high-type developers and no links for the low types is a stable structure $i f \nu _ { { } _ { h } } \ge \bar { c } _ { { } _ { h } }$ and $\nu _ { { } _ { l } } < c _ { { } _ { l } }$

![](/api/attachments/PEU2NW8B/fulltext/images/f8166c211dbd8739986e2f5e227aff81563dd51bcc85b5913d2cb58fcb919143.jpg)  
Figure 5. Network Structures from Propositions 9 and 10

The network structures from Propositions 9 and 10 are shown in Figure 5. In this case also, the range for which the proposed structure is stable does not completely cover the range for which it is efficient. A completely intralinked structure or the star structure of the high-type developers is a representation of the “clique” of the high types. Here a high type does not communicate with a low type at all, because $\nu _ { _ { l } } { < } c _ { _ { l } } { \le } c _ { _ { h } } ;$ that is, the cost incurred outweighs the contribution that a low type can make.

Proposition 11: (a) A star network of only the low-type developers with no links for the high types is a uniquely efficient structure if

$$
\frac {2 c _ {l}}{2 + (n - 2) \delta} \leq v _ {l} <   \overline {{c}} _ {l}
$$

$$
v _ {h} (1 + \delta (n + m - 2)) + v _ {l} (1 + \delta (n - 1)) <   c _ {h} + c _ {l}
$$

and

$$
\begin{array}{c} v _ {h} \left(n + 2 m - 2 + \delta (m - 1) (n + m - 2)\right) + v _ {l} \left(2 - n + \delta (n + m n - 2)\right) \\ <   c _ {h} \left(n + 2 m - 2\right) + c _ {l} \left(2 - n\right). \end{array}
$$

(b) A completely intralinked network of only the low-type developers with no links for the high types is a uniquely efficient structure if $\nu _ { { } _ { l } } \ge \bar { c } _ { { } _ { l } }$ and

$$
v _ {h} (1 + \delta (n + m - 2)) + v _ {l} (1 + \delta (n - 1)) <   c _ {h} + c _ {l}.
$$

A star of low types only will have a positive value only if $2 c _ { \scriptscriptstyle { l } } \leq \nu _ { \scriptscriptstyle { l } } ( 2 + ( n - 2 ) \delta )$ is satisfied. The second condition in Proposition 11a ensures that the value of the proposed structure is higher than that of a star comprising everyone with a low type at the center. The third condition ensures the value of the proposed structure is higher than that of a star comprising everyone with a high type at the center. The second condition in Proposition 11b ensures that the proposed structure defeats a network where all the low types are completely intralinked and the high types are connected in the shape of a star with a low type at the center.

Proposition 12: (a) A star network of only the low-type developers and no links for the high types is a stable structure $i f \nu _ { _ h } < c _ { _ h }$ and

$$
c _ {l} \leq v _ {l} <   \min \left(\overline {{c}} _ {l}, \frac {c _ {h}}{1 + (n - 1) \delta}\right).
$$

(b) A completely intralinked network of only the low-type developers and no links for the high types is a stable structure $i f \nu _ { _ h } < c _ { _ h }$ and

$$
\overline {{c}} _ {l} \leq v _ {l} <   \frac {c _ {h}}{1 + (n - 1) \delta}.
$$

Figure 6 shows the network structures discussed in Propositions 11 and 12. Either a completely connected or a star network of the low-type developers is observed in the case where the low-type developers, even as a group, are not able to provide sufficient value that can outweigh the cost of link formation for a high-type developer. However, the low-type developers are competent enough to help one another. The product in this case could be highly unreliable as there is no communication among the high types and between the two types. If the low-type developers do not undertake code development, then their information would not be reflected in the code at all. More importantly, the stability of the network structures in Propositions 9, 10, 11, and 12 raises serious concerns about the survivability of the project as well as the sustain ability of the developers who are not connected at all.

Proposition 13: (a) An efficient structure has no links if

$$
v _ {l} <   \frac {2 c _ {l}}{2 + (n - 2) \delta}
$$

$$
v _ {h} <   \frac {2 c _ {h}}{2 + (m - 2) \delta}
$$

$$
\begin{array}{c} v _ {h} \left(n + 2 m - 2 + \delta (m - 1) (n + m - 2)\right) + v _ {l} \left(n + \delta n (n + m - 2)\right) \\ <   c _ {h} (n + 2 m - 2) + n c _ {l} \end{array}
$$

and

$$
\begin{array}{c} v _ {h} \left(m + \delta m (n + m - 2)\right) + v _ {l} \left(m + 2 n - 2 + \delta (n - 1) (n + m - 2)\right) \\ <   m c _ {h} + c _ {l} (m + 2 n - 2). \end{array}
$$

(b) An efficient network has at most one nonempty component.

(c) For $\nu _ { _ h } < c _ { _ h }$ and $\nu _ { \scriptscriptstyle { l } } < c _ { \scriptscriptstyle { l } } ,$ , any pairwise stable network that is nonempty is such that each developer has at least two links and thus is inefficient.

![](/api/attachments/PEU2NW8B/fulltext/images/a19b901280cbb6e91fea672dc14bc57c4f0549ba5b785ab9204265087891f02d.jpg)  
Figure 6. Network Structures from Propositions 11 and 12

If the conditions in Proposition 13a are satisfied, there exists no structure that has a nonnegative value. Proposition 13b follows directly from Propositions 2a, 3, 5, 7, 9, 11, and 13a. In Proposition 13c, the conditions $\nu _ { _ h } < c _ { _ h }$ and $\nu _ { _ { l } } { < } c _ { _ { l } }$ preclude “loose ends” in a nonempty structure. Hence, from Propositions 3, 5, 7, 9, and 11, any nonempty pairwise stable structure must be inefficient. In this scenario, no developer is willing to keep a link with any other developer who does not bring in additional new value from indirect connections. Clearly, such a structure is overconnected from an efficiency perspective.

It must be noted that the same structure might be observed across different stages of a project. It would depend on the intrinsic values and costs of the two types at different stages. In the above discussions, we have provided a few examples where these structures might be observed and we discussed the stability of the efficient structures. However, there may be several structures that might be stable for a given range of intrinsic values and costs. For instance, a two-component network where component 1 has all the high types completely intralinked and component 2 has all the low types completely intralinked is stable for $\nu _ { { } _ { h } } \geq \bar { c } _ { { } _ { h } } , \nu _ { { } _ { l } } \geq \bar { c } _ { { } _ { l } }$ , and $\nu _ { \scriptscriptstyle { l } } { < c _ { \scriptscriptstyle { h } } / ( 1 + ( n - 1 ) \delta ) }$

Figure 7 plots the regions for each type of network structure. Here we normalize $\nu _ { _ h } { = } 1$ . Other parameter values are $c _ { \scriptscriptstyle { l } } = 0 . 3 , \delta = 0 . 5 , m = 4 , n = 7$ . The notations of $\mathbf { \omega } ^ { \mathsf { 6 6 7 } } \mathbf { 2 } \mathbf { - } e ,$ $^ { \circ 6 } 7 \mathrm { a } \mathrm { - } s ,$ ” and “7a” indicate that the corresponding network structures (for this case, the network structure described in Proposition 7a) are, respectively, efficient, stable, or both. Several interesting observations have been made. First, it demonstrates the tension between the efficient and stable networks. The structures that are efficient are not stable in the complete range for which they are efficient—that is, unstable structures can be efficient in certain ranges. We find that, in general, whenever there is tension between the stability and efficiency of structures, the stable structure is either underconnected across types or overconnected within type from an efficiency perspective. Also note that most of the efficient structures are stable only in a very limited range. Second, for certain value–cost relationships, the developers skip their own types to form links with a better-connected developer of another type. Such structures are efficient as well as stable, and this fits well with the strengths of the OSS phenomenon in which societal value is generated through interactions across types of developers. Third, we observe that the clique of single types may be stable as well as efficient. These clique structures would be observed when either the high-type developers have very high costs of link formation or the low-type developers provide insufficient contributions to a relationship. Fourth, except the structures in Propositions 2, 3a, 5a, 9b, and 11b, all the efficient structures involved a developer who is better connected than the rest. This raises issues about coordination and dissimilarities in the power of the developers involved. Finally, a multicomponent network is never efficient—that is, an efficient network cannot have more than one component. If two separate networks can create positive values individually, then a combined network of the actors involved can create a much higher positive value.

![](/api/attachments/PEU2NW8B/fulltext/images/227c8f781e2e61d3a755f752b86a39b45a139f34e909c983b4371ef21f7e5dbb.jpg)  
Figure 7. Phase Diagram of Network Structures

## Effect of Network Size

More developers may join the team and the network size increases. Figure 8 depicts how network structures are affected. The networks in the range where $c _ { _ h } \leq \nu _ { _ h }$ do not depend on the numbers of each type of developers (m and n). Therefore, we only show how the boundaries shift with m and n when $c _ { h } > \nu _ { h } .$ . Increasing m or n alone helps the transition from Propositions 11a to 7b, or 11b to 5b; that is, high-type developers are connected to a low-type developer. More low-type developers (an increase in n) help more low-type developers to communicate (P13a to P11a). We find the patterns similar when we fix the total size but vary the ratio of low to high type $( n / m )$ , although the effect is more significant for higher values of $\nu _ { \scriptscriptstyle { l } }$ .

![](/api/attachments/PEU2NW8B/fulltext/images/16b6a28a84321c6ff22f6fab4c855d9c928cab058e25de9abf489275bdfedf59.jpg)

![](/api/attachments/PEU2NW8B/fulltext/images/a53b6b3212bc1b78390145889c6863ef8e9762c4a30ddaaa97014731fb5f2c93.jpg)  
Figure 8. Effect of Network Size

When the team size increases, the value or cost parameters may also change. For example, a larger network may carry more information and expertise. We assume that the values increases with the network size—that is, $\nu _ { _ h } { = } \nu _ { _ h } ^ { _ 0 } \cdot \varphi ^ { } ( n { + } m )$ and $\nu _ { _ { l } } { = } \nu _ { _ { l } } ^ { \mathrm { ~ 0 ~ } } \Phi ^ { ( { n + m } ) }$ where $\Phi ^ { ' } ( n + m ) > 0$ —but the cost parameters remain unchanged as they measure the costs of direct ties (pairwise communications). We examine a scenario where $c _ { _ h } > > \nu _ { _ h } ^ { 0 } .$ $c _ { \scriptscriptstyle l } > \nu _ { \scriptscriptstyle l } ^ { \mathrm { ~ 0 ~ } }$ , and $c _ { _ h } / \nu _ { _ h } ^ { 0 } > > c _ { _ l } / \nu _ { _ l } ^ { 0 }$ . As shown in Figure 9, when the network size increases, low-type developers start to communicate and then high-type developers start to participate; this is followed by more interactions among the low types and then between the two types. Eventually we have a completely connected network.

## Empirical Analysis

Giv en t he comp lexity of t he nat urally occurring net works , researchers have resorted to laboratory experiments for extracting evidence for the principles of stability and efficiency [5, 21]. In such experiments, the intrinsic value and cost parameters are set at some monetary value and are common knowledge. The players are then allowed to form links. This process is run over a number of rounds. Stability is said to be achieved if the same network structure is achieved in three consecutive rounds. In this paper, we do not resort to laboratory experiments. We use the data from OSS projects hosted at SourceForge, which is the primary hosting place for such projects. There were more than 100,000 projects hosted at SourceForge by December 2005. It also had about 1 million registered users by December 2005. Using the SourceForge data, we (1) segment the participants into high and low types based on code contribution behavior using a latent class model, and (2) analyze the communication structure from the developer mailing list<sup>3</sup> to find the stable communication structure. Without the exact intrinsic value and cost information, we cannot identify the efficient structure.

![](/api/attachments/PEU2NW8B/fulltext/images/fedbc275bf481d5402127181350c0ce1e801ace7f829654243a269392cd01302.jpg)  
Figure 9. An Evolution Path of Network Structures

## Data Collection

We concentrate on projects that were registered between January 2000 and June 2000, with SourceForge being their sole development area. The projects were further screened to exclude projects that did not use a concurrent versioning system (CVS) repository and SourceForge mailing lists. We also excluded the projects that use outside mailing lists or forums, as tracking users across lists is troublesome. The projects were further screened to include only those projects that had more than 10 registered developers. This left us with 186 projects, out of which three were randomly chosen for the analysis that we undertake here. The developer e-mail archives and the CVS commit logs were downloaded using Web agents (developed by us), and the discrepancies in IDs/user names were removed manually. The CVS logs contain information about any changes (number of lines added or subtracted), date of change, and the name/ID of the developer who changed it for each source file. TortoiseCVS was used to access the CVS repositories hosted at SourceForge.

## Latent Class Model for Developer Segmentation

We devise a methodology to segment developers of an OSS project into high and low types based on their code contribution behaviors over time. Let $u _ { { \scriptscriptstyle i t } }$ be the expected utility for developer i if he or she develops code at time t. This can be represented as

$$
u _ {i t} = \beta_ {s} X _ {i t} + \varepsilon_ {i t},
$$

where X is a vector of covariates that impact the utility of code development for the developer. Parameter vector $\beta _ { s }$ represents the corresponding vector of impact of the covariates on the utility of a developer in state s, where $s \in \ \{ 1 , 2 , . . . , S \}$ . The above scenario is modeled as a latent state binary logit model, as the true type (class or state) of a developer is unobservable. Let $p _ { _ { i t \mid s } } = \mathrm { p r o b } ( y _ { _ { i t } } = \mathrm { c o d e } \mid \mathrm { s t a t e } = s )$ be the probability that developer i develops code $( y _ { i t } = \mathrm { c o d e } )$ at time t in state s. We have

$$
p _ {i t | s} = \frac {\exp \left(\beta_ {s} X _ {i t}\right)}{1 + \exp \left(\beta_ {s} X _ {i t}\right)}, \quad \forall s \in \{1, 2,..., S \}.
$$

Given a state assignment, the contribution of developer i to the likelihood function is given as the joint probability of the sequence of his or her choice (code or not code), $y _ { i } = ( y _ { i 1 } , y _ { i 2 } , . . . , y _ { i T } )$ . Explicitly,

$$
p _ {i | s} = \prod_ {t = 1} ^ {T} p _ {i t | s}.
$$

The covariates vector, $X _ { i t }$ , includes a constant term, the expected number of source lines to be coded in period t (t is in months) by developer i, the total number of e-mails sent by developer i in period t, and the rank of the project at time (t – 1). The expected number of source lines to be coded in period t by developer i are approximated by the amount of coding effort that the developer undertook the last time he or she coded. SourceForge ranks the projects hosted on its Web site based on traffic, communication, downloads, and code development for each month. The rank of the project is included above to account for the impact of the project environment variables such as overall development effort in the project, user base, and activity in the community that would impact a developer’s own utility.

The class assignment is unknown. Let $\pi _ { _ { i s } }$ be the prior probability for state s for developer i. Then, $\pi _ { _ { i s } }$ can be represented as follows:

$$
\pi_ {i s} = \frac {\exp \left(\rho_ {s} W _ {i}\right)}{\sum_ {s} \exp \left(\rho_ {s} W _ {i}\right)}, \quad \forall s \in \{1, 2,..., S \},
$$

where ${ \rho } _ { s } = 0$ for identification purposes. $W _ { i }$ denotes the observable factors that enter the model for class membership. We assume that $W _ { i }$ includes only a constant term. This corresponds to a situation where no covariates are available for class membership.

The likelihood for individual i is then the expectation over the class-specific contributions:

$$
p _ {i} = \sum_ {s} \pi_ {i s} p _ {i | s}.
$$

The log likelihood function can be represented as

$$
\ln L = \sum_ {i = 1} ^ {n} p _ {i} = \sum_ {i = 1} ^ {n} \ln \left(\sum_ {s} \pi_ {i s} \prod_ {t = 1} ^ {T} p _ {i t | s}\right).
$$

The parameters for the above model are estimated by the Markov Chain Monte Carlo (MCMC) process using the Metropolis-Hastings algorithm [13]. With the parameter estimates, the posterior estimates of the class probability can be obtained as

Table 1. Model Selection Results for the Three Projects

<table><tr><td></td><td>States</td><td>Log likelihood</td><td>BIC</td></tr><tr><td rowspan="3">Project 1</td><td>One</td><td>-296.0397</td><td>-302.9712</td></tr><tr><td>Two</td><td>-233.0242</td><td>-248.6200</td></tr><tr><td>Three</td><td>-235.2637</td><td>-259.5239</td></tr><tr><td rowspan="3">Project 2</td><td>One</td><td>-225.8934</td><td>-235.2577</td></tr><tr><td>Two</td><td>-140.5409</td><td>-161.6105</td></tr><tr><td>Three</td><td>-133.7310</td><td>-166.5060</td></tr><tr><td rowspan="3">Project3</td><td>One</td><td>-213.2817</td><td>-220.7088</td></tr><tr><td>Two</td><td>-174.2062</td><td>-190.9173</td></tr><tr><td>Three</td><td>-158.9375</td><td>-184.9325</td></tr></table>

Note: The boldface lines indicate the model that best fits the data.

$$
\hat {\pi} _ {i | s} = \frac {\hat {p} _ {i | s} \hat {\pi} _ {i s}}{\sum_ {s} \hat {p} _ {i | s} \hat {\pi} _ {i s}}.
$$

A strictly empirical estimator of the latent class within which developer i resides would be that associated with the maximum value of $\hat { \pi } _ { _ { i \mid s } }$ . One of the issues to be confronted is the number of states, S. Greene and Hensher [14] and Roeder et al. [30] suggest the use of a Bayesian information criterion (BIC) for model selection:

$$
\mathrm{BIC} = \ln L - s i z e \times \ln (N) / 2,
$$

where size refers to the number of parameters in the model, and N is the number of developers in the model. For segmentation purposes, for each project, all the developers who appear in the CVS logs or at least three times in the mailing list are considered.

The results for three randomly selected projects are given in Table 1. For Projects 1 and 2, a two-state model is better than the one- and three-state models. However, for Project 3, the three-state model outperforms the one- and two-state models. Note that the one-state model is outperformed in all three projects, which fits nicely with the notion of developer heterogeneity in OSS projects. The type of each developer is identified using its posterior estimate of class probabilities.

The stable and efficient structures derived in previous sections are for a two-state model, although those structures for the three-state model can be derived similarly. In the following, we focus on the analysis of two selected projects that are best described by two-state latent class models. Tables 2 and 3 display the results of model parameter estimates, and Table 4 compares the characteristics of developers in these two projects. A high-type developer is more likely to code than a low type. Project 1 has a higher percentage of high-type developers than Project 2. The developers in Project 1 have a higher propensity to code compared to the corresponding types in Project 2. In both projects, a low-type developer is less likely than a high type to contribute (by coding) if the project ranking drops. In general, a developer’s participation level in communication is a good predictor of his or her willingness to code. We also find that, while absent in Project 1, learning opportunities exist for developers in Project 2, especially for the low types if they code.

Table 2. Model Parameter Estimates for Project 1

<table><tr><td rowspan="2">Variables</td><td colspan="2">Type</td></tr><tr><td>High</td><td>Low</td></tr><tr><td>Constant</td><td>-1.2674(0.2012)</td><td>-3.2146(0.1973)</td></tr><tr><td>Number of lines coded last time (in hundreds)</td><td>0.0021(0.0079)</td><td>0.3847(0.2794)</td></tr><tr><td>Number of communications in period t</td><td>0.2058(0.0323)</td><td>-0.2344(0.2252)</td></tr><tr><td>Rank of the project in period t - 1 (in thousands)</td><td>-0.4097(0.0898)</td><td>-2.8043(0.2030)</td></tr><tr><td colspan="3">Note: Standard errors are in parentheses.</td></tr></table>

Table 3. Model Parameter Estimates for Project 2

<table><tr><td rowspan="2">Variables</td><td colspan="2">Type</td></tr><tr><td>High</td><td>Low</td></tr><tr><td>Constant</td><td>-1.8899(0.3051)</td><td>-4.0070(0.3519)</td></tr><tr><td>Number of lines coded last time (in hundreds)</td><td>0.2287(0.0979)</td><td>0.5881(0.1088)</td></tr><tr><td>Number of communications in period t</td><td>0.2227(0.0447)</td><td>0.1809(0.0380)</td></tr><tr><td>Rank of the project in period t - 1 (in thousands)</td><td>-0.1177(0.0586)</td><td>-1.1936(0.1552)</td></tr><tr><td colspan="3">Note: Standard errors are in parentheses.</td></tr></table>

## Identification of a Stable Network

A stable communication network is derived from the mailing list of each project. SourceForge arranges the e-mails as threads. Any two participants belonging to the same thread are assumed to have a tie. The strength of a link between two developers is equal to the number of ties between them. A network structure is then created that includes only those links that have strength greater than or equal to 5. This helps in separating out the links that show regular interaction from the casual or irregular links, and ensures that we consider only those links that have stabilized over time. We tested for robustness by slightly changing the link strength threshold of 5 and obtained similar structures.

Table 4. Developer Characteristics of Projects 1 and 2 (in percent)

<table><tr><td rowspan="2"></td><td colspan="2">Project 1</td><td colspan="2">Project 2</td></tr><tr><td>High type</td><td>Low type</td><td>High type</td><td>Low type</td></tr><tr><td>Propensity to code</td><td>21.97</td><td>3.86</td><td>13.13</td><td>1.79</td></tr><tr><td>Prior probability of type</td><td>15.37</td><td>84.63</td><td>8.10</td><td>91.90</td></tr><tr><td>Posterior probability of type</td><td>21.88</td><td>78.12</td><td>6.48</td><td>93.52</td></tr></table>

![](/api/attachments/PEU2NW8B/fulltext/images/89244212faf27d53eaa94696250c4d41a5c3747819d0f92fd15c8986c408bc63.jpg)  
Figure 10. Stable Network Structures from Project 1 and Proposition 4

## Project 1

Project 1 had only 10 participants who had at least one link of strength greater than or equal to 5. Out of these 10 participants, 4 are identified as high type and 6 as low type. Figure 10 shows the identified stable structure for Project 1.

It can be seen from the network that the high types are completely connected, and four of the low types are connected in the shape of a star with a high type at the center. This structure resembles closely the structure in Proposition 4b. The slight deviations in the structure obtained in Project 1 are due to the fact that the structure in Proposition 4b is based on the assumption that, within a group, all the developers have the same intrinsic value and cost. However, in reality, there would be slight deviations in these intrinsic values and costs within a group.

## Project 2

For Project 2, we have 13 participants who had at least one tie of strength greater than or equal to 5. Out of these 13 participants, 5 are high type and 8 are low type. Figure 2a shows the identified stable structure for Project 2.

In Project 2, the developer H1 is the most active and interacts with all the other developers. H1 is central to the interactions amount the group in Project 2. This structure closely resembles a star of all the nodes with a high type at the center; this is the same as network structure in Proposition 8a and is shown in Figure 11. The network structure of Project 2 also shows the evolution of the network structure. Developer H2 was the most active developer before H1 took over during the early stages of the project. A stable structure identified from the e-mail archives of only the first few months development period of the project revealed the structure to be a star comprising everyone with H2 at the center.

![](/api/attachments/PEU2NW8B/fulltext/images/89dec964508e18c68eb58d05600457edb42fd72c8320b28a2f0ebb46a9acd882.jpg)  
Figure 11. Stable Network Structures from Project 2 and Proposition 8a

## Comparison of the Two Projects

The main difference between the stable structures in Projects 1 and 2 is the linking of the high types. In Project 1, the high types are completely intralinked as compared to a star structure of the high types in Project 2. An important driver of one’s participation in OSS projects is the prospect of career enhancement, or ego gratification by demonstrating programming prowess to one’s sophisticated peers [24]. A project whose intended audience is the system administrator is likely to show strong community appeal and, hence, would attract sophisticated developers [25]. The intended audiences for Project 1 are system administrators and for Project 2, end users/desktop/developers. This causes a self-selection bias in the sophisticated developers’ choice of project. Project 1 will attract sophisticated developers, which indicates that the intrinsic value of each high-type developer will be high, leading to a complete intralinking among the high types. However, for Project 2, the high types are not that sophisticated and have comparative lower intrinsic value than the high types in Project 1. Hence, the high-type developers in Project 2 arrange themselves in the shape of a star.

## Conclusion

Ov er t he p ast few y ears , s oft ware dev elop ment has witnessed the emergence and growing popularity of the OSS phenomenon. Because the communication structure in an OSS project is an important determinant of the eventual quality of the product, it is necessary to understand how these structures evolve. This understanding would be helpful in managing OSS projects better. In this paper, we adopt a social network perspective and model the interaction of developers using non-cooperative game theory. We consider the heterogeneity of developers both in terms of informative value and the cost of link formation.

We derive several interesting and important results. We show that several kinds of network structures could emerge in OSS communication teams. In the case of heterogeneous developers, the overall value generated by these networks depends not only on the architecture but also on the relative positioning of developers. Because developers are motivated by self-interest rather than group interest, the structures that are efficient are not necessarily stable. We also show that there may exist several structures that are stable, but only one is efficient. In order to test the concept of stability, we consider three real-world OSS projects. Two of these projects mirror our model settings, involving only two types of developers. These two projects are further analyzed empirically. The stable communication structures observed in these projects fit the predictions of our model nicely.

This research provides several practical implications for managing OSS development. First, in addition to managing the codes submitted by the developers, it is important for an administrator to monitor and manage the communication among developers. We demonstrate that it is possible for the administrator to discover the underlying stable structure based on stored communications between developers. Second, because a stable structure is not necessarily efficient, it may be necessary to provide incentives or reduce costs to developers so that their communications stabilize to an efficient structure. We observe that, generally, the high-type developers tend to communicate less than what is desired for efficiency. Appropriate incentive mechanisms should be designed to convince these developers to contribute more in this aspect as well. The equal bargaining rule allows the benefits of a connection to be split equally between two developers [18] and induces the players who contribute less to contribute efficiently. Future research can examine how a similar mechanism should be designed to ensure that the high types derive sufficient value when communicating with the low types. Because developers are often motivated by reputations within the community, a simple ranking mechanism based on the contribution in communication may work. Of course, such a ranking system could invite a lot of “cheap talk,” and one must be careful. The administrator can enrich the content, and enhance the quality, of communication so as to provide more learning opportunities for both types. The administrator can also reduce communication costs by directing communication to developers in a customized manner—for example, sending e-mail to developers who are more likely to be helpful in addressing each question.

Third, in order to assure sustainability of a project, it is important to retain the developers who are at the center of the information exchange networks. This is particularly challenging as developers are free to come and go. Finally, we observed that the communication structure within a project may change over time, as the project moves through stages (such as design, coding, integration, and testing) and the communication need of the team changes. This implies that communication management in a project is a continuing process, and not a one-time activity. How often the administrator should look for a change in the structure and what, if any, incentive adjustments are necessary remain open questions for the OSS community.

This work has a few limitations that open up exciting avenues for future research. The developers are classified according to their intrinsic values and costs. There may exist other dimensions, and, hence, a modeling framework that integrates or consolidates all relevant information is desirable. Although challenging, it is practically useful to allow more developer types and even certain degrees of within-type variability. Future research could also consider classification of developer abilities across multidimensions such as programming ability and domain knowledge. One underlying assumption in the model—that a developer is aware of the true type of other developers—can be limiting. We have assumed that the developer would get to know perfectly about the type of others following some initial exchange with them. Future research should try to relax this assumption by assuming that the developer would know probabilistically about others’ type following some initial exchange. In the current empirical model, the threshold for the number of interactions to reach stability is exogenously chosen. The correct value should be endogenously selected in a more granular model that takes the project and developer characteristics into consideration. More research is needed for the better design of incentive mechanisms that help to stabilize a network into its efficiency.

## Not es

1. Note that a low type contributes less in value only in comparison to a high type; in absolute terms, the value provided by a low type can be quite high. For instance, in comparison to the value provided by a core-code developer, the value provided by a bug reporter is marginal, but the bug reporter’s information alone could be quite significant.

2. Here, anonymity implies that the value to a node in a network is position specific rather than label specific.

3. The developer mailing list maintained by SourceForge contains a complete record of all e-mail exchanges.

4. The authors thank an anonymous reviewer for suggesting this.

## References

1. Ahuja, M.K., and Carley, K.M. Network structure in virtual organizations. Organization Science, 10, 6 (1999), 741–757.

2. Bala, V., and Goyal, S. A non-cooperative model of network formation. Econometrica, 68, 5 (2000), 1181–1229.

3. Bala, V., and Goyal, S. A strategic analysis of network reliability. Review of Economics Design, 5, 3 (2000), 205–228.

4. Borgatti, S.P.; Everett, M.G.; and Freeman, L.C. UCINET 6 for Windows. Cambridge: Harvard: Analytic Technologies, 2002.

5. Callander, S., and Plott, C.R. Principles of network development and evolution: An experimental study. Journal of Public Economics, 89, 8 (August 2005), 1469–1495.

6. Crowston, K., and Howison, J. The social structure of free and open source software development. First Monday, 10, 2 (2005) (available at http://131.193.153.231/www/issues/ issue10\_2/crowston/index.html).

7. Deroian, F. Farsighted strategies in the formation of a communication network. Economics Letters, 80, 3 (2003), 343–349.

8. Fang, Y., and Neufeld, D. Understanding sustained participation in open source software projects. Journal of Management Information Systems, 25, 4 (Spring 2009), 9–50.

9. Freeman, L.C. Centrality in social networks: Conceptual clarification. Social Networks, 1, 3 (1979), 215–239.

10. Galeotti, A.; Goyal, S.; and Kamphorst, J. Network formation with heterogeneous players. Games & Economic Behavior, 54, 2 (2006), 353–372.

11. Goyal, S. Sustainable communications model. Tinbergen Institute Discussion Paper TI 93–250, Rotterdam, 1993.

12. Goyal, S., and Moraga, J.-L. R&D networks. Rand Journal of Economics, 32, 4 (2001), 686–707.

13. Greene, W.H. Econometric Analysis, 5th ed. Upper Saddle River, NJ: Prentice Hall, 2003.

14. Greene, W.H., and Hensher, D.A. A latent class model for discrete choice analysis: Contrasts with mixed logit. Transportation Research Part B: Methodological, 37, 8 (2003), 681–698.

15. Grewal, R.; Lilien, G.; and Mallapragada, G. Location, location, location: How network embeddedness affects project success in OSS. Management Science, 52, 7 (2006), 1043–1056.

16. Haller, H., and Sarangi, S. Nash networks with heterogeneous agents. Mathematical Social Sciences, 72, 2 (2005), 181–201.

17. Jackson, M.O. A survey of models of network formation: Stability and efficiency. In G. Demange and M. Wooders (eds.), Group Formation in Economics: Networks, Clubs and Coalitions. Cambridge: Cambridge University Press, 2004, pp. 1–62.

18. Jackson, M.O., and Wolinsky, A. A strategic model of social and economic networks. Journal of Economic Theory, 71, 1 (1996), 44–74.

19. Jaisingh, J.; See-To, E.W.K.; and Tam, K.Y. The impact of open source software on the strategic choices of firms developing proprietary software. Journal of Management Information Systems, 25, 3 (Winter 2008–9), 241–276.

20. Johnson, C., and Gilles, R.P. Spatial social network. Review of Economic Design, 5, 3 (2001) 273–301.

21. Kosfeld, M. Economic networks in the laboratory: A survey. Review of Network Economics, 3, 1 (2004), 20–41.

22. Kraut, R., and Streeter, L. Coordination in software development. Communications of the ACM, 38, 3 (1995), 69–81.

23. Lakhani, K., and von Hippel, E. How open source software works: “Free” user-to-user assistance. Research Policy, 32, 6 (2003), 923–943.

24. Lerner, J., and Tirole, J. Some simple economics of open source. Journal of Industrial Economics, 50, 2 (2002), 197–234.

25. Lerner, J., and Tirole, J. The scope of open source licensing. Journal of Law, Economics, and Organizations, 21, 1 (2005), 20–56.

26. McBride, M. Imperfect monitoring in communication networks. Journal of Economic Theory, 126, 1 (2006), 97–119.

27. Mehra, A.; Dewan, R.; and Freimer, M. Firms as incubators of open source software development. Information Systems Research (2011, forthcoming).

28. Montazemi, A.R.; Siam, J.J.; and Esfahanipour, A. Effect of network relations on the adoption of electronic trading systems. Journal of Management Information Systems, 25, 1 (Summer 2008), 233–266.

29. Roberts, J.; Hann, I.-H.; and Slaughter, S. Understanding the motivations, participations, and performance of open source software developers: A longitudinal study of Apache projects. Management Science, 52, 7 (2006), 984–999.

30. Roeder, K.; Lynch, K.; and Nagin, D. Modeling uncertainty in latent class membership: A case study in criminology. Journal of American Statistical Association, 94, 447 (1999), 766–776.

31. Sen, R. A strategic analysis of competition between open source and proprietary software. Journal of Management Information Systems, 24, 1 (Summer 2007), 233–257.

32. Sen, R.; Subramaniam, C.; and Nelson, M.L. Determinants of the choice of open source software license. Journal of Management Information Systems, 25, 3 (Winter 2008–9), 207–240.

33. Singh, P.V. The small world effect: The influence of macro level properties of developer collaboration networks on open source project success. ACM Transactions on Software Engineering and Methodology, 20, 2 (2011), article 6.

34. Singh, P.V.; Tan, Y.; and Mookerjee, V. Network effects: The influence of social capital on open source project success. MIS Quarterly (2011, forthcoming) (available at http://papers .ssrn.com/s013/papers.cfm?abstract\_id=1111868/).

35. Singh, P.V.; Tan, Y.; and Youn, N. A hidden Markov model of developer learning dynamics in open source software projects. Information Systems Research (2011, forthcoming).

36. Van de Ven, A.H.; Delbecq, D.; and Koening, R.J. Determinants of coordination modes within organizations. American Sociological Review, 41, 2 (1976), 322–338.

37. Wasserman, S., and Faust, K. Social Network Analysis: Methods and Applications. Cambridge: Cambridge University Press, 1994.

38. Watts, A. A dynamic model of network formation. Games and Economic Behavior, 34, 2 (2001), 331–341.

39. Weber, S. The Success of Open Source. Cambridge: Harvard University Press, 2004.

## Appendix

Here we p rov ide p roofs of all t he p rop os it ions , which are split into two parts for stability and efficiency, respectively.

## Proofs for Stability

## Proof of Proposition 1

Consider that g is a pairwise stable network and has two or more nonempty components having low-type developers. For Proposition 1a, let $u ^ { i j }$ be the utility that accrues to i from link ij, where $j \in L ,$ given graph $g .$ Then, $u ^ { i j } = u _ { { i } } ( g ) - u _ { { i } } ( g - i j )$ if $i j \in g$ and $u ^ { i j } = u _ { i } ( g + i j ) - u _ { i } ( g )$ if $i j \notin g .$ . Let us assume $i j \in g$ , then $u ^ { i j } \geq 0$ . Consider another pair $k l \in g , k \in L ,$ , which belongs to another component. Because i is in the same component with j but k is not, then $u ^ { k j } > u ^ { i j } \ge 0$ because k also gets the discounted value of developer i, which is not included in $u ^ { i j } .$ For similar reasons, $u ^ { j k } > u ^ { l k } \ge 0$ . This contradicts the definition of pairwise stability as $k j \notin g$ . Following this argument, it can be easily seen that in a stable network, all the low types belong to one component only. Along the same lines, it is easy to show that in a stable network, all the high types belong to one component only. Proposition 1e follows from 1b and 1d.

## Proof of Proposition 2b

By definition, the condition in Proposition 2b is equivalent to $\nu _ { { n } } ( 1 - \delta ) \ge \nu _ { { l } } ( 1 - \delta ) \ge c _ { { n } } \ge c _ { { l } }$ Given this condition, we know that the stable structure will have all the high types completely connected. Also, all the low types will be completely connected. It is easy to see that for $\nu _ { \scriptscriptstyle { l } } ( 1 - \delta ) \geq c _ { \scriptscriptstyle { h } } ^ { \mathrm { ~ ~ } } ;$ , any pair of a high and a low type that are not directly connected can increase their own utilities by forming a link.

## Proof of Proposition 4

This follows from the argument that for $\nu _ { _ { h } } ( 1 - \delta ) \geq c _ { _ { h } } ^ { } ,$ , all the high-type developers that are not directly connected can increase their utility by forming links. Also, for $\nu _ { \scriptscriptstyle { l } } ( 1 - \delta ) < c _ { \scriptscriptstyle { l } }$ , all the low-type developers prefer indirect links to direct links among themselves. In Proposition 4a, for $\nu _ { \scriptscriptstyle { l } } ( 1 - \delta ) \geq c _ { \scriptscriptstyle { h ^ { 2 } } }$ , all the high types prefer indirect links to direct links with the low types. So in the above structure, a high type can increase his or her utility by severing links with one or more of the low types. Hence, this structure is not stable. In Proposition 4b, for $c _ { { } _ { h } } \leq \nu _ { { } _ { l } }$ and $c _ { \scriptscriptstyle l } \leq \nu _ { \scriptscriptstyle h } ,$ any low and high type that are directly connected would not like to break the link. However, because $\nu _ { \scriptscriptstyle { l } } ( 1 - \delta ) \geq c _ { \scriptscriptstyle { h } } ,$ , any high type that is indirectly connected to a low type will not like to form a link with the low type. The range for which the structure is stable does not completely cover the range for which it is efficient.

## Proof of Proposition 6

For $\nu _ { \scriptscriptstyle { l } } ( 1 - \delta ) < c _ { \scriptscriptstyle { l } }$ , all the low-type developers that are not directly connected can increase their utility by forming links. For $\nu _ { _ h } ( 1 - \delta ) < c _ { _ h } ,$ the high-type developers prefer indirect connections to direct connections with other high types. In Proposition 6a, these two conditions imply that $\nu _ { \scriptscriptstyle l } ( 1 - \delta ) \geq c _ { \scriptscriptstyle h } .$ . This means that all the high types would prefer indirect links to direct links with the low types. So in the above structure, a high type can increase his or her utility by severing links with one or more of the low types. Hence, the efficient structure is not stable. In Proposition 6b, for $c _ { { } _ { h } } \leq \nu _ { { } _ { l } }$ and $c _ { \scriptscriptstyle l } \leq \nu _ { \scriptscriptstyle h }$ , any low and high type that are directly connected would not like to break the link. However, because $\nu _ { \scriptscriptstyle { l } } ( 1 - \delta ) \geq c _ { \scriptscriptstyle { h } } ,$ any high type that is indirectly connected to a low type would not like to form a link with the low type. Hence, the proposed efficient structure in Proposition 5b is stable for the range given in Proposition 6b. It can also be seen that the structure that is efficient in the range given in Proposition 5a is not stable for the whole range.

## Proof of Proposition 8

In Proposition 8a, for $c _ { _ h } \leq \nu _ { _ h }$ , none of the high-type developers that are directly connected will break the link. For $\nu _ { _ h } ( 1 - \delta ) < c _ { _ h }$ , none of the high-type developers that are indirectly connected to another high type would like to form a direct link. For $\nu _ { \scriptscriptstyle { l } } ( 1 - \delta ) < c _ { \scriptscriptstyle { l } }$ , none of the low types that are indirectly connected to another low type would like to form a direct link. For $c _ { { } _ { h } } \leq \nu _ { { } _ { l } }$ , any low and high type that are directly connected would not like to break the link. However, because $\nu _ { \scriptscriptstyle l } ( 1 - \delta ) \geq c _ { \scriptscriptstyle h } ,$ , any high type that is indirectly connected to a low type will not like to form a link with the low type. In Proposition 8b, for $c _ { \scriptscriptstyle l } \leq \nu _ { \scriptscriptstyle l }$ , none of the low-type developers that are directly connected will break the link. For $\nu _ { \scriptscriptstyle { l } } ( 1 - \delta ) < c _ { \scriptscriptstyle { l } }$ , none of the low-type developers that are indirectly connected would like to form a direct link. For $\nu _ { _ h } ( 1 - \delta ) < c _ { _ h i }$ , none of the high-type developers that are indirectly connected would like to form a direct link. For $( m - 1 ) \delta \nu _ { { } _ { h } } + ( n - 1 ) \delta \nu _ { { } _ { l } } + \nu _ { { } _ { l } } \geq c _ { { } _ { h } }$ and $c _ { \scriptscriptstyle l } \leq \nu _ { \scriptscriptstyle h } .$ , any low and high types that are directly connected would not like to break the link. However, because $\nu _ { \scriptscriptstyle { l } } ( 1 - \delta ) \geq c _ { \scriptscriptstyle { h } } ,$ any high type that is indirectly connected to a low type would not like to form a link with the low type.

## Proof of Proposition 10

In the network structure of Proposition 10a, for $c _ { _ h } \leq \nu _ { _ h }$ , none of the high-type developers that are directly connected will break the link. For $\nu _ { _ h } ( 1 - \delta ) < c _ { _ h i }$ , none of the high-type developers that are indirectly connected would like to form a direct link.

For $\nu _ { { } _ { l } } { < } c _ { { } _ { l } }$ , none of the low-type developers would like to form a link. For $\nu _ { \scriptscriptstyle { l } } < c _ { \scriptscriptstyle { h } } ,$ none of the high types would like to form a link with any of the low types. In the network structure of Proposition 10b, for $\nu _ { { } _ { l } } { < } c _ { { } _ { l } }$ , the low-type developers do not form any links among them. For $\nu _ { \mathrm { } _ { l } } < c _ { \mathrm { } _ { h } }$ , none of the high types want to form a direct link with any of the low types.

## Proof of Proposition 12

In the network structure of Proposition 12a, for $c _ { \scriptscriptstyle l } \leq \nu _ { \scriptscriptstyle l }$ , none of the low-type developers that are directly connected will break the link. For $\nu _ { \scriptscriptstyle { l } } ( 1 - \delta ) < c _ { \scriptscriptstyle { l } }$ , none of the low-type developers that are indirectly connected would like to form a direct link. For $\nu _ { _ h } < c _ { _ h } ,$ none of the high-type developers would like to form a link among them. However, for $\nu _ { \scriptscriptstyle { l } } ( 1 + ( n - 1 ) \delta ) < c _ { \scriptscriptstyle { h } }$ , none of the high-type developers would like to form a link with a low type.

## Proof of Proposition 13

In Proposition 13a, the four conditions state that values of the low-type star, high-type star, star comprising everyone with high type at the center, and star comprising everyone with low type at the center have negative values, respectively. Proposition 13b follows from Propositions 2 through 13a.

## Proofs for Efficiency

Because the complete proofs for efficiency are quite lengthy, here we provide the sketch of the proofs. The complete proofs can be found in an online supplement (http:// faculty.washington.edu/ytan/Research/JMIS\_NetworkOSS\_OLS.pdf). The following methodology is used to prove Propositions 2a, 3, 5, 7, 9, and 11.

For the efficiency proof, the proposed structure should defeat all possible networks for the given value–cost relationships. We compare the value of the proposed structure with all $r : r \geq 0$ component networks. The value of an empty network $( r = 0 )$ is zero and, hence, any network that has a positive value will defeat an empty network. We first compare the proposed structure with the single-component structures and then with two-component networks. Once we show that the proposed structure defeats any single- or two-component networks, the argument that the proposed structure would defeat any r-component structure follows from induction.

The value of any network is calculated by getting the number of direct and indirect links in the network. The value to the network is $2 ( \nu _ { { } _ { h } } - c _ { { } _ { h } } ) , 2 ( \nu _ { { } _ { l } } - c _ { { } _ { l } } )$ , and $( \nu _ { _ { h } } + \nu _ { _ { l } } - c _ { _ { h } } - c _ { _ l } )$ for a direct link between high-high, low-low, and high-low types, respectively. The maximum value of an indirect link can be $2 \delta \nu _ { _ { h } } , 2 \delta \nu _ { _ { l } }$ , and $( \nu _ { _ h } + \nu _ { _ l } )$ for high-high, lowlow, and high-low types, respectively. None of the proposed structures have connections of length greater than 2. Hence, the value of each indirect link in that case will be the maximum value of an indirect connection. For the general case, we assign the maximum possible value to each indirect connection.
