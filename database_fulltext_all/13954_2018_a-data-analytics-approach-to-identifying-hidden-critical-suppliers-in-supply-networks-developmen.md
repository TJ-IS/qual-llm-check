---
otero_id: 13954
otero_key: "UJB95UUQ"
title: "A data-analytics approach to identifying hidden critical suppliers in supply networks: Development of nexus supplier index"
authors: "Benjamin B.M. Shao; Zhan (Michael) Shi; Thomas Y. Choi; Sangho Chae"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.08.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
<table><tr><td>PII:</td><td>S0167-9236(18)30137-4</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2018.08.008</td></tr><tr><td>Reference:</td><td>DECSUP 12982</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>3 April 2018</td></tr><tr><td>Revised date:</td><td>15 July 2018</td></tr><tr><td>Accepted date:</td><td>17 August 2018</td></tr></table>

## Accepted Manuscript

A data-analytics approach to identifying hidden critical suppliers in supply networks: Development of nexus supplier index

ELSEVIE Decision Support Systems

Benjamin B.M. Shao, Zhan (Michael) Shi, Thomas Y. Choi, Sangho Chae

![](/api/attachments/UJB95UUQ/fulltext/images/75f6a522018061a42f0b203fdb3915da0917ee333307ef214a647de05451ea2f.jpg)

Please cite this article as: Benjamin B.M. Shao, Zhan (Michael) Shi, Thomas Y. Choi, Sangho Chae , A data-analytics approach to identifying hidden critical suppliers in supply networks: Development of nexus supplier index. Decsup (2018), doi:10.1016/ j.dss.2018.08.008

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# A Data-Analytics Approach to Identifying Hidden Critical Suppliers in Supply Networks: Development of Nexus Supplier Index

Benjamin B.M. Shao<sup>a</sup>, Zhan (Michael) Shi<sup>a,\*</sup>, Thomas Y. Choi<sup>a</sup>, Sangho Chae<sup>b</sup>

<sup>a</sup>W. P. Carey School of Business Arizona State University Tempe, AZ 85287, USA

<sup>b</sup>Tilburg School of Economics and Management Tilburg University 5000 LE Tilburg, The Netherlands

## Abstract

Recent events involving supplier-caused business disruptions bring to the forefront the issue of managing hidden yet critical suppliers that may exist deep in the supply network. While managing prominent strategic suppliers in the top tier is well understood, we have only just begun to recognize a different type of critical suppliers called nexus suppliers. Nexus suppliers are critical because of their structural positions in the supply network. They can be several tiers removed in the extended supply network and hence may not have direct contact with, and not be visible to, the focal buying firm. In this study, we explore the identification and categorization of nexus suppliers. Based on the theory of nexus supplier and data envelopment analysis (DEA), we propose a data-analytics approach to compute what we call Nexus Supplier Index (NSI). It is a measure that combines various network centrality measures to capture and reflect different aspects of a supplier’s structural importance. The contribution of our study is to take the concept of nexus suppliers that exists only in theory to practice and demonstrate how to look for nexus suppliers in the real world. To achieve this aim, we develop a mathematical model for NSI, compile a large data set using Bloomberg Terminal, and engage in computations to identify and categorize nexus suppliers. The target company is Honda, and we review the results with the top supply management team at Honda of America. Implications for practice and future research are discussed.

Keywords: Nexus supplier index, data analytics, hidden suppliers, centrality measures, social network analysis, data envelopment analysis

# ACCEPTED MANUSCRIPT

## 1. Introduction

Recent events that involved supplier-caused business disruptions bring to the forefront the issue of managing critical suppliers that are embedded deep in the supply network. When an explosion occurred at a plant of Evonik Industries, a little-known raw materials supplier, it brought the global automotive supply chain to a halt (Carty, 2012). While the theory and practice of managing prominent strategic suppliers are well understood (Kaufman et al., 2000; Slobodow et al., 2008; Koufteros et al., 2012), managers and researchers have only just begun to recognize the potential criticality of these less-known suppliers. Yan et al. (2015) propose the theory of nexus suppliers to emphasize the importance of such hidden critical suppliers, where nexus supplier is defined as “any supplier in a multi-tiered supply network that potentially exerts a profound impact on a buyer’s performance due to its network position.”

Traditional strategic suppliers refer to the suppliers in a firm’s supply base whose actions and outcomes have significant and direct impact on the focal firm’s risk management (Kraljic, 1983). A strategic supplier provides the focal firm with essential input materials and critical products or technologies (Wagner & Johnson, 2004; Borgatti & Li, 2009). In this regard, strategic suppliers tend to be top-tier suppliers with high impact on the buying firm’s profitability, and the performance of the focal firm depends largely on these suppliers’ capabilities and resources. As a result, the focal firm aims to cultivate a collaborative partnership with strategic suppliers (Bensaou, 1999; Chen et al., 2004).

By contrast, a nexus supplier refers to a supplier that is critical to the focal firm’s operations because of its structural position in the firm’s supply network, such as how its business relationships are linked with other firms in the focal firm’s extended supply network. Recent theoretical studies such as Ang at el. (2016) have shown the topology of top-tier supply relationships can significantly influence the performance and strategy of downstream buying firms. A nexus supplier may be several tiers removed in the supply network, and hence may not be immediately visible to the focal buying firm (Yan et al., 2015). Incidents such as the explosion at Evonik Industries reflect the importance of understanding how a supplier’s structural embeddedness in the extended supply network (i.e., the extent to which a supplier’s

# ACCEPTED MANUSCRIPT

criticality depends on the position and structure of its supply network) may influence the performance of downstream firms (i.e. General Motors, Ford, etc.). This need for understanding prompts firms to find the nexus suppliers that could potentially affect its performance. Companies with a better understanding of suppliers’ network positions are likely to outperform those that do not consider them (Choi & Kim 2008).

Presently, the concept of nexus supplier exists only in theory. Yet to be answered is the question of how to identify them in practice. Only then can a buying firm proactively manage its nexus suppliers to mitigate the associated risks (e.g., materials flow disruption) or take advantage of potential market benefits (e.g., innovation opportunities). The difficulty of identifying nexus suppliers is further compounded by the fact that many buying firms do not have a global view of their extended supply networks and thus they do not know a priori which suppliers can be the candidates for nexus suppliers. For example, Toyota did not know, let alone manage, much of its lower-tier supply chain until the 2011 Tohoku earthquake disrupted its suppliers’ suppliers (Ang et al., 2017). In response, we map out a multitier supply network based on the data collected from Bloomberg Terminal and develop a data-analytics framework to capture a supplier’s network structural importance for identifying nexus suppliers.

We propose a mathematical model called Nexus Supplier Index (NSI). Our NSI model is based on data envelopment analysis (DEA) and incorporates various network centrality measures (i.e., degree, betweenness, eigenvector, and closeness), each of which reflects a certain aspect of a supplier’s importance in the focal buying firm’s supply network. NSI provides a single unified metric that combines multiple centrality measures to evaluate a supplier’s potential for being a nexus supplier. We take this position because no single centrality measure is comprehensive enough to reflect the overall criticality of a supplier. The proposed NSI is designed to reflect the overall structural importance of a supplier and help a buying firm make informed decisions by qualifying certain suppliers as nexus suppliers for better risk assessment, evaluation, and portfolio development of suppliers.

To apply and evaluate the proposed NSI model, we empirically examine a real-world supply network that is constructed for Honda Motor Company. Going beyond top-tier suppliers, we identify

# ACCEPTED MANUSCRIPT

lower-tier suppliers for Honda beyond its supply base to the fourth-tier to map out a supply network. We develop a data-analytics system to facilitate the tasks of data storage, visualization, and NSI computation. Using the system, we compute the NSI scores for all the suppliers in Honda’s supply network to identify the nexus supplier candidates and then categorize them into specific types. Through this empirical instantiation, we demonstrate the feasibility of putting the nexus supplier concept into action by leveraging data-analytics methods and exploiting a large volume of business relationship data. We present and discuss the results with the top supply management team at Honda of America for result validation.

## 2. Literature Review

## 2.1. Rating of strategic suppliers

Strategic suppliers (Dyer & Singh, 1998; Gadde & Snehota, 2000) and strategic alliances (McCarter & Northcraft, 2007) have been explored by researchers in operations management and strategic management. Strategic suppliers offer essential products, capabilities and technologies (Olsen & Ellram, 1997; Ellram & Carr, 1994; Monczka et al., 1998; Azadegan et al., 2008) while strategic alliances are formed to promote interfirm communication and cultural fit (Cavusgil et al., 1995; Arino et al., 1997; Dacin et al., 1997; Hitt et al., 2000; Zahra et al., 2000; Wu et al., 2009).

Systematic approaches have been proposed to evaluate the performance of these strategic suppliers. Liu and Hai (2005) present a voting analytic hierarchy process (VAHP) method for ranking and selecting suppliers. They extend Yahya and Kingsman's (1999) analytic hierarchy process (AHP) method for rating suppliers by integrating DEA and managers’ supplier evaluations based on multiple criteria. Mafakheri et al. (2011) also apply AHP to propose a multiple-criteria dynamic programming (MCDP) method for supplier evaluation and order allocation. Considering production capacity interdependence among suppliers, Li et al. (2013) develop analytical models to optimize buying firms’ sourcing and pricing decisions when there are multiple suppliers with different wholesale prices and reliability levels. Hu and Kostamis (2015) and Yim (2014) also examine the buying firm’s multiple-sourcing strategies to propose an analytical model that optimizes order quantities for multiple suppliers.

# ACCEPTED MANUSCRIPT

While these studies provide practical and systematic approaches to rating suppliers, their focus is on internal capabilities of top-tier suppliers and ranking these top-tier suppliers. In the cases of further upstream suppliers (i.e. tiers 2 and 3 suppliers), often their internal capabilities are unknown to the buying firm, making it difficult to apply the above approaches. For instance, how could a final assembler who is at the downstream end of the supply network begin to consider the potential impact of these unknown suppliers on its performance? To evaluate the unknown suppliers beyond top-tier, we have chosen to take a network perspective to understand structural characteristics of the firms in supply networks.

## 2.2. A network perspective

Recently, researchers have moved beyond two-tier supply chains (Guo et al., 2010) to evaluate a supplier’s importance by considering its position in the larger supply network context (Choi et al., 2001; Andersson et al., 2002; Pathak et al., 2007; Artto et al., 2008; Kim et al., 2011; Basole & Bellamy, 2014; Bhattacharjee & Cruz, 2015). At the core of the argument is a firm’s structural relationship with other firms in the supply network and its impact on performance. While a supplier’s internal capabilities, its competitiveness, and direct ties with other firms are crucial factors to consider (Gnyawali & Madhavan, 2001; Echols & Tsai, 2005; Hagedoorn, 2006; Li, 2013), salient network attributes such as centrality, network density, repeated ties, and common ties also need to be taken into account when evaluating suppliers (Gulati & Gargiulo, 1999).

Emphasizing the concept of structural embeddedness, Choi and Kim (2008) suggest buying firms consider network structural characteristics when evaluating suppliers. Structural embeddedness of a supplier refers to the extent to which a supplier’s criticality depends on the position and structure of its supply network. They argue that suppliers’ performance is influenced by other companies in the supply networks, so suppliers’ structural embeddedness can be as important as their internal capabilities. Borgatti and Li (2009) call for more development of network perspectives and point out how social network concepts such as ego-network structure, structural holes, node centrality, network cohesion, and structural equivalence can potentially be applied to supply chain management. Kim et al. (2011) apply the key

# ACCEPTED MANUSCRIPT

metrics of social network analysis to supply network constructs. They illuminate the importance of understanding individual supply network members in terms of structural position in the network and suggest buying firms consider the potential roles of suppliers based on their network centrality measures such as degree, closeness, betweenness and eigenvector.

Degree centrality in the social graph is defined as the number of links that a node has (Freeman, 1978). In the supply network context, degree centrality reflects a firm’s influence over its supply chain partners (Borgatti & Li, 2009). Closeness centrality describes the extent to which a node is geodesically close to all the other nodes in the social network (Marsden, 2002), and it indicates reliable access to information from the supply network (Kim et al., 2011). A node with high betweenness centrality plays the role of intermediary in the social network (Freeman, 1978), and can facilitate or control the flows of materials and information in supply networks (Kim et al., 2011). Finally, eigenvector centrality is a measure of the network status in which a node has many links with other central nodes (Bonacich, 1987). A supplier with high eigenvector centrality provides indirect linkages to critical players in supply networks (Yan et al., 2015). Recent studies by Bellamy et al. (2014) and Dong et al. (2015) apply some of these centrality measures to study their association with the focal firm’s performance. However, a systematic approach to integrate different network centrality measures to evaluate direct and indirect suppliers is yet to be developed.

## 2.3. Nexus suppliers and data analytics

Reflecting the structural perspective of supply network research, Yan et al. (2015) conceptualize critical suppliers based on their positions in the supply networks. The nexus suppliers can potentially exert influence on a buying firm’s performance because they take central positions in the buying firm’s supply network and can take up a gate-keeping position for materials flow, cost, quality management, and information access. Nexus suppliers can be categorized into three types: operational, monopolistic and informational nexus suppliers (Yan et al., 2015). Each type plays a different role with varying degree of criticality, interdependence, and asymmetry, all of which carry different managerial implications for the

# ACCEPTED MANUSCRIPT

focal buying firm. An operational nexus supplier has a large number of ties; it organizes and incorporates parts from multiple suppliers for the focal buying company. A monopolistic nexus supplier exists in the extended industrial network and has a greater chance of sitting on the shortest paths between pairs of other nodes; it would thus likely affect supply continuity and assurance. Finally, an informational nexus supplier is connected to a highly diverse group of firms in the supply network; it may serve as the source of early market information or technological innovations for the focal firm. Because of their different nature, each type of nexus suppliers is expected to exert different influence on the buying firm’s performance. While Yan et al. (2015) introduce the concept of nexus supplier, their study is largely theoretical. We are in need of a model that can empirically evaluate and identify nexus suppliers.

Researchers have recently begun to apply data analytics to operations management issues, such as inventory management, quality management, process design, pricing, and new product development (Simchi-Levi, 2014). Ferreira et al. (2016) apply data analytics to develop demand forecasting and price optimization models. Basole et al. (2017) demonstrate data-driven approach to visualize innovationfocused supply networks. Huang and Van Mieghem (2014) propose a framework to convert clickstream data from non-transactional websites into advance demand information that can be used for inventory management. The framework complements traditional approaches of inventory management by analyzing the webpage clicking behavior of customers as an additional variable for demand forecasting. Abrahams et al. (2015) present a text analytic framework for discovering product defects. Chan et al. (2016) introduce a mixed-method approach for utilizing social media data in new product development projects.

Our goal then is to adopt a data analytics approach to assess the criticality of nexus suppliers through a composite of several centrality measures to arrive at index scores, which we call nexus supplier index (NSI). In the following sections, we first propose the NSI framework and then demonstrate its feasibility by examining the real-world supply network of the automaker Honda. Our intent is to help supply managers interpret the results of our data analysis, consider limitations in the model and data currently available, and generate insights that can help manage nexus suppliers.

# ACCEPTED MANUSCRIPT

## 3. Nexus Supplier Index (NSI)

We develop a mathematical model composed of well-defined network constructs to compute the Nexus Supplier Index (NSI). The purpose of NSI is to provide a single unified metric that combines multiple centrality measures (e.g., degree, betweenness, eigenvector, etc.) to evaluate the overall criticality of suppliers in the focal firm’s supply network, as no single centrality measure is comprehensive enough to capture the aggregate importance of a supplier. While it is possible to apply each centrality measure separately to the task at hand, such an approach would be ad hoc and time consuming. In addition, the interpretation of those results would be convoluted by the peculiar properties associated with each measure. Our approach, instead, is to develop a composite NSI measure that reflects the overall importance of a supplier to help the focal firm make an informed decision on whether a supplier in its supply network could be qualified as a nexus supplier.

Our NSI framework is built based on data envelopment analysis (DEA). Originally intended to construct a production frontier, DEA is a non-parametric, linear programming method for calculating efficiency. DEA has since been used for developing other advanced performance metrics, such as Malmquist index that compares production output across different economies, industries and firms (Färe et al., 1994; Chou & Shao, 2014). Further, DEA has then been extended to resource-allocation rules (Korhonen & Syrjänen, 2004), quality management (Chin et al., 2009), multi-criteria ranking (Giannoulis & Ishizaka, 2010) and strategic sourcing decisions (Talluri et al., 2013).

DEA has been used as a benchmarking tool to generate a score that indicates the relative distance of an entity to the best practices so as to measure its overall performance compared with its peers (Cook et al., 2014). More importantly and related to our study, such overall performance measured by DEA is manifested in the form of a composite measure that aggregates individual indicators (Cook et al., 2014). Following the same logic, we employ DEA as the method for developing our NSI score by aggregating individual centrality measures to identify nexus suppliers in a supply network.

Our DEA-based model for computing the nexus supplier index (NSI) of supplier node p in a supply network is formulated as follows:

$$
\text { Maximize   NSIp } = \frac {\alpha D p + \beta B p + \gamma V p}{\sigma F p}\tag{1}
$$

$$
\text { subject   to } \frac {\alpha D i + \beta B i + \gamma V i}{\sigma F i} \leq 1 (i = 1, \dots , N)\tag{2}
$$

$$
\alpha , \beta , \gamma , \sigma \geq 0\tag{3}
$$

where D is degree centrality, B is betweenness centrality, V is eigenvector centrality, and F is distance farness measure. The definitions of these centrality measures are given in the network analysis literature (e.g., Wasserman and Faust, 1994): $D _ { p } = \frac { \sum X _ { p j } } { ( N - 1 ) }$ where $X _ { p j } = 1$ if there is a link between node $p$ and node $j ,$ or 0 otherwise; $B _ { p } = { \frac { 2 \Sigma d ( i , p ) } { d ( d - 1 ) } }$ where $d ( i , p )$ is the number of paths node $p$ is on, and d is the number of geodesics connecting p; $V = \delta ( I { - } \omega R ) R T$ where δ is the scaling vector for score normalization, I is the identity matrix, ω reflects the extent one weighs the centrality of other nodes p is tied to, R is the adjacency matrix, and T is the a matrix of 1’s; and $F = \frac { 2 \Sigma d ( i , p ) } { N ( N - 1 ) }$ is the reciprocal of closeness. Note α, β, γ, and σ in Eq. (1) are weights to be decided for degree, betweenness, eigenvector, and farness, respectively. In essence, they are decision variables and the only restriction is their positivity of Constraint (3). In our NSI context, these weights provide information on how a supplier firm’s structural embeddedness can be changed to make it more critical (e.g., through the focal firm’s direct sourcing from a lower-tier supplier).

We choose these centrality measures because they capture different aspects of node importance at the node level (degree), neighborhood level (eigenvector), and network level (betweenness and farness). Degree refers to the number of links a node has. A node with more links and higher degree is deemed more important. However, relying on degree alone can be misleading as it is a local measure, where one simply counts the links attached to a specific node. Eigenvector measures the prestige of a node based on the importance of the other nodes it is connected to. Nodes that are connected to other important nodes should have higher prestige and influence. Betweenness is measured based on the entire network under

# ACCEPTED MANUSCRIPT

consideration. It counts the number of shortest paths a certain node resides on between any other two nodes, and is developed based on the idea that a node lying on the shortest paths controls communication flows. A node with high degree, betweenness and eigenvector is thus considered more critical, so these centrality measures ought to be maximized and hence placed in the numerator of Eq. (1).

We also have distance farness in the denominator of Eq. (1), which measures the average distance of a node to every other node and can be viewed the reciprocal of the closeness centrality. A node is considered less important if it is relatively farther from all other nodes. The smaller the value of farness a node has, the more important it is deemed to be. The goal is to minimize the distance farness measure, placing it in the denominator of Eq. (1). Constraint (2) ensures the NSI score for supplier node p be less than 1, where a higher NSI score indicates greater importance of a supplier node and hence its higher propensity to be a nexus supplier. Our NSI model thus includes the four essential centrality measures most frequently used in social network analysis (Kilduff & Tsai, 2003) and combines them into one composite index that reflects the various aspects of node importance (i.e., supplier criticality). In theory, NSI reflects a supplier’s structural embeddedness in a supplier network using an integrative and comprehensive approach that considers four essential dimensions of node criticality.

Huang et al. (2014) identify the node role in a network using multiple indicators. Similarly, we use multiple centrality measures to evaluate the importance of a supplier node and indicate its criticality in a supply network. However, instead of using normalized simple averages of the multiple indicators (i.e., α ${ \bf \beta } = \beta = \gamma = \sigma = 1 )$ as in Huang et al. (2014), we find appropriate weights α, β, γ and σ for their respective centrality measures to derive the NSI score. In doing so, we address the open problem of automatic optimization of weights previous researchers have put forth (Huang et al., 2014). As noted by Sherman and Zhu (2006), DEA gives each unit the benefit by making itself look as good as possible when compared with other units through its own weight selection. Our DEA-based NSI approach differs from a simple ratio measure by treating weights as independent variables that are objectively decided when optimizing the NSI score. This weight solution represents a departure from previous studies, which either use normalized weights to assume equal importance of the components or ask the decision maker to assign subjective weights to reflect the perceived importance of each component.

One potential problem with the model (1)-(3) is that it has an infinite number of solutions: if $( a ^ { * } ,$ $\beta ^ { * } , \gamma ^ { * }$ and $\sigma ^ { * } )$ is a solution, then $( c \alpha ^ { * } , c \beta ^ { * } , c \gamma ^ { * }$ and $c \sigma ^ { * } )$ is another solution for any constant c. To address this problem, the constraint $\sigma F _ { p } = 1$ can be added. Moreover, the model (1)-(3) assumes constant returns to scale (CRS) (Charnes et al., 1978). Thus, to allow for the more flexible case of variable returns to scale (VRS) (Banker et al., 1984), we incorporate a scale factor $\mu$ (Coelli et al., 2005; Sherman & Zhu, 2006). Thus, our complete NSI model is as follows:

$$
\mathrm{MaximizeNSIp} = \alpha D p + \beta B p + \gamma V p + \mu\tag{4}
$$

$$
\text { subject   to } \alpha D i + \beta B i + \gamma V i - \sigma F i + \mu \leq 0 (i = 1, \dots , N)\tag{5}
$$

$$
\sigma F p = 1\tag{6}
$$

$$
\alpha , \beta , \gamma , \sigma \geq 0\tag{7}
$$

$$
\mu \text {   unrestricted }\tag{8}
$$

Using the duality in linear programming, we derive an equivalent envelopment form of the primal model (4)-(8) that involves fewer constraints and hence is preferred (Coelli, et al., 2005):

$$
\text { Minimize } \theta_ {p} - \varepsilon (s _ {F} ^ {-} + s _ {D} ^ {+} + s _ {B} ^ {+} + s _ {V} ^ {+})\tag{9}
$$

$$
\mathrm{subjectto} \sum_ {i = 1} ^ {N} \lambda_ {i} F _ {i} + s _ {F} ^ {-} = \theta_ {p} F _ {p}\tag{10}
$$

$$
\sum_ {i = 1} ^ {N} \lambda_ {i} D _ {i} - s _ {D} ^ {+} = D _ {p}\tag{11}
$$

$$
\sum_ {i = 1} ^ {N} \lambda_ {i} B _ {i} - s _ {B} ^ {+} = B _ {p}\tag{12}
$$

$$
\sum_ {i = 1} ^ {N} \lambda_ {i} V _ {i} - s _ {V} ^ {+} = V _ {p}\tag{13}
$$

$$
\lambda_ {i} \geq 0 (i = 1, \dots , N)\tag{14}
$$

$$
\sum_ {i = 1} ^ {N} \lambda_ {i} = 1\tag{15}
$$

$$
s _ {F} ^ {-}, s _ {D} ^ {+}, s _ {B} ^ {+}, s _ {V} ^ {+} \geq 0\tag{16}
$$

## ACCEPTED MANUSCRIPT

In the model (9)-(16), $\theta _ { p }$ is the NSI score to be optimized. Parameter ε represents an infinitely small number that has no impact on the optimal NSI score $\theta _ { p } ; s _ { F } ^ { - }$ represents the slack for the farness measure; and $s _ { D } ^ { + } , s _ { B } ^ { + }$ , and $s _ { V } ^ { + }$ indicate the slack for degree, betweenness, and eigenvector centrality measures, respectively. Our NSI model consists of the following notable characteristics. First, it provides a comprehensive way to evaluate the criticality of a supplier node in the focal firm’s supply network and hence its likelihood of being a nexus supplier. Second, through the aggregate NSI score that combines degree, betweenness, eigenvector, and distance farness measures, our objective function incorporates the practical meanings of each measure and reflects them in the functional form (i.e., by maximizing degree, betweenness, and eigenvector, while minimizing distance farness). Third, the NSI model produces a score $\theta _ { p }$ between 0 and 1, a range that is similar to a ratio measure, and the NSI score follows our intuitive understanding of how NSI scores should behave: a greater score would mean higher criticality, and numerically it would stay between 0 and 1. In sum, our DEA-based NSI model represents a composite measure of supplier node importance that allows managers to better assess each supplier’s criticality against other nodes in the supplier network (Cook et al., 2014).

Once a supplier is found to possess a high NSI score, it becomes a candidate for nexus supplier. We can then examine its individual centrality measures to determine its type as operational, monopolistic, and/or informational (Yan et al., 2015). We carry out this task by using the categorization model depicted in Table 1 to help associate a nexus supplier with its type. This categorization scheme serves as a useful mechanism for classifying the nexus suppliers identified by the NSI model (9)-(16). We consider degree, betweenness, eigenvector, and diversity measures, as specified in Table 1. Of particular interest is the concept of diversity, as it captures a supplier’s exposure to varied ideas and propensity of being an informational nexus supplier. Diversity is measured by counting the number of unique industries a node’s suppliers belong to, and it reflects the extent to which a supplier is connected to a range of different organizations across different industries. A supplier with high diversity can be critical, as it is exposed to heterogeneous experiences and contextually varied information about market opportunities and technology innovations (Mackelprang et al., 2017).

Table 1. Characteristics of the Three Types of Nexus Suppliers

<table><tr><td></td><td>Operational Nexus Supplier</td><td>Monopolistic Nexus Supplier</td><td>Informational Nexus Supplier</td></tr><tr><td>Structural Characteristics</td><td>High degree, betweenness and eigenvector centrality</td><td>High betweenness centrality</td><td>High diversity</td></tr><tr><td>Criticality</td><td>Significant impacts on the operational performance of the end product</td><td>Significant impacts on supply continuity due to low substitutability</td><td>Sources of early market and technological information</td></tr></table>

Source: Adapted from Yan et al. (2015)

## 4. Data and Analytics System

## 4.1. Data: Honda Motor Company’s supply network

We use Honda’s supply network primarily because the company has been featured extensively in a stream of studies (e.g., Choi & Hong 2002, Choi & Linton 2011, Kim et al. 2011) that we have chosen to build on. In general, industry analysts consider Honda’s supply chain management in high regard, which increases the practical value of this study’s outcome. Their supply chain would also tend to be relatively stable, and that helps justify taking a cross-sectional view of its supply network based on publiclyavailable data. Mapping out the multi-tier supply network for a global industrial company is a challenging task. The main difficulty has been the lack of a reliable and comprehensive dataset that covers the flow of sales from suppliers to customers. In practice, such information is revealed in many different sources yet each source tends to be incomplete. For example, in the United States, public firms disclose their customer information in the filings to the Securities and Exchange Commission (SEC), but the disclosure is mandatory only if 10% or more of their revenue is derived from sales to a particular customer (a public firm can also voluntarily report other customers to which the sales are below the 10% threshold if the firm determines that such disclosure is in its own best interest). In addition to public filings, supplier-customer information is also scattered in other sources such as earnings call transcripts, industry reports, press releases, firm websites, etc.

Only recently have financial data vendors started to collect supplier-customer-relationship data systematically from these different places and integrate them into a coherent database. For this research, we utilize the Bloomberg Supply Chain (SPLC) database, which is available on Bloomberg Terminal. Bloomberg SPLC keeps track of about 28,000 companies worldwide. For each of these companies, the database provides a list of suppliers based on the flow of sales information it has aggregated from a variety of sources. Though there is no guarantee that these supplier lists are exhaustive, to the best of our knowledge, SPLC is comparatively comprehensive in the coverage. The resolution of SPLC data is at the company level, so the plant-level or component-level supplier data is unavailable. Also, SPLC provides only cross-sectional, not longitudinal, data on firms’ suppliers.

We compile Honda’s supply network data one link at a time from the SPLC database and our data collection strategy reflects the multi-tier nature of the supply network. Figure 1 helps illustrate the data collection process. With Honda as the focal buying firm (heavy solid oval in Figure 1), we first collect all the companies listed in SPLC that have a direct sales flow to Honda and we call these companies Honda’s top-tier suppliers (illustrated as lighter ovals in Figure 1 with arrows representing the direction of sales). We then iterate through the top-tier suppliers: For each of them (e.g., Bridgestone Corp), we treat it as the focal company and collect all of its top-tier suppliers that are not currently in our dataset. These newly added companies are each two tiers removed from Honda and we thus label them tier 2 suppliers of Honda (dashed ovals in Figure 1). Note that a top-tier supplier of Honda can have a direct sales flow to another top-tier supplier of Honda, as Bridgestone does in Figure 1. In this case, we use the length of the shortest path to Honda for tier labeling. Then, we repeat this iterative process further upstream. By the end of the data collection period, we have gathered all the supplier information for companies in the top, second, and third tiers of Honda’s supply network; we collect data to the fourth-tier companies but not their suppliers. It should be noted that Bloomberg does not allow downloading the SPLC data in bulk nor does it provide an interface for retrieving the data programmatically. Therefore, we used a research assistant to manually collect the data and save it in plain text format. The data collection process took 15 weeks and over 300 person-hours.

Figure 1. Data Collection Procedure  
![](/api/attachments/UJB95UUQ/fulltext/images/ad31d1dca9c8eed5edcad45fc0d545da016d5d6b9f37bbf206b17488fc41f725.jpg)

Up to tier 4, the final data set includes the network consisting of 10,833 companies and 47,183 supplier-customer relationships (these supplier-customer relationships represent uni-directional relationships rather than bi-directional, so if firm A supplies to firm B and firm B also supplies to firm A, then they are represented as two distinct relationships in our statistics). Of the 10,832 companies excluding Honda, 245 are Honda’s top-tier suppliers, 1,643 are tier 2 suppliers, 4,605 are tier 3 suppliers, and 4,339 are tier 4 suppliers. SPLC also provides information about the country of a company’s headquarters and the industry sector it belongs to using the Global Industry Classification Standard (GICS) (see https://www.msci.com/gics). The collected supply network spans 83 countries and 66 industry sectors. Tables 2 and 3 list the top 10 countries and top 10 GICS industries represented in the dataset. Not surprisingly, the suppliers in the United States, Honda’s home country of Japan, and East Asian countries are ranked high in the country list. In the industry list, the electronic components and semiconductor sectors are ranked high. This finding is consistent with the observed industry trend of “drive-by-wire” where many of the mechanical auto parts are being replaced with high-tech components.

Table 2. Breakdown of Companies by Country

<table><tr><td>Rank</td><td>Country/Region</td><td># of Companies</td></tr><tr><td>1</td><td>U.S.</td><td>1,595</td></tr><tr><td>2</td><td>Japan</td><td>1,226</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td>3</td><td>South Korea</td><td>876</td></tr><tr><td>4</td><td>China</td><td>822</td></tr><tr><td>5</td><td>Taiwan</td><td>603</td></tr><tr><td>6</td><td>India</td><td>269</td></tr><tr><td>7</td><td>United Kingdom</td><td>259</td></tr><tr><td>8</td><td>France</td><td>190</td></tr><tr><td>9</td><td>Germany</td><td>142</td></tr><tr><td>10</td><td>Australia</td><td>128</td></tr></table>

Table 3. Breakdown of Companies by GICS

<table><tr><td>Rank</td><td>GICS Code</td><td>Industry</td><td># of Companies</td></tr><tr><td>1</td><td>452030</td><td>Electronic Equipment &amp; Components</td><td>678</td></tr><tr><td>2</td><td>453010</td><td>Semiconductors &amp; Semiconductor Equipment</td><td>513</td></tr><tr><td>3</td><td>201060</td><td>Machinery</td><td>473</td></tr><tr><td>4</td><td>151010</td><td>Chemicals</td><td>437</td></tr><tr><td>5</td><td>451030</td><td>Software</td><td>411</td></tr><tr><td>6</td><td>151040</td><td>Metals &amp; Mining</td><td>344</td></tr><tr><td>7</td><td>251010</td><td>Auto Components</td><td>338</td></tr><tr><td>8</td><td>451020</td><td>IT Services</td><td>314</td></tr><tr><td>9</td><td>201040</td><td>Electrical Equipment</td><td>277</td></tr><tr><td>10</td><td>452010</td><td>Communications Equipment</td><td>241</td></tr></table>

As for the number of top-tier suppliers each company in the network has (the number of companies from which there is a direct sales flow), the number ranges from 0 to 433 and is highly skewed to the right. We further calculate the mean number of top-tier suppliers for companies in each tier (away from Honda) and the result shows the mean number displays a decreasing pattern, from 19 for top-tier, to 13 for tier 2, and to 5 for tier 3. It suggests that as we move from the center of the Honda supply network to its peripheral, the number of suppliers per company decreases on average. This result is consistent with our intuition that companies further upstream in a supply chain in general have fewer suppliers.

## 4.2. Data-analytics system: Storage, visualization, and computation of network data

To facilitate the analysis of Honda data and to potentially generalize to other supply chain datasets, we build an integrated data-analytics system. It assists in streamlining the tasks of supply network data storage, visualization, and NSI computation. Utilizing the raw data exported from sources such as Bloomberg SPLC, the system comprises three main components (solid boxes) and three ancillary modules (dashed boxes), as shown in Figure 2.

## ACCEPTED MANUSCRIPT

Figure 2. Architecture of Data-Analytics System  
![](/api/attachments/UJB95UUQ/fulltext/images/ed1265f36eddde318dfd65924e077876bf15715139bfe11971fb81da93aaa4a0.jpg)

The first ancillary module, implemented in scripting language, pre-processes the raw data by transforming it to a format that can be loaded into the storage component of our system. We manage the collected supply network data in a dedicated graph database, which is an emerging data storage technology (see https://en.wikipedia.org/wiki/Graph\_database and http://neo4j.org). Unlike traditional database which represents data in tabular format, a graph database represents data as nodes, edges, and properties. Graph database is easily scalable and has demonstrated advantages in the analytics of big, networked data. Using a graph to represent the supply network is natural, as companies, their characteristics, supply relationships, and details of the supply relationships can be represented as nodes, nodes’ properties, directed edges between nodes, and edges’ properties, respectively. More importantly, using the graph database technology renders graph-like analytical queries much more efficient. It would take a significantly less amount of time to find out, for instance, who are the tier 3 suppliers to a particular company, or what is the shortest path between any two companies in the supply network.

The supply network database then feeds the data to two components in the system that handle the analytics workflow. The first is a user interface for visualizing and navigating the supply network. Taking the Honda dataset, for example, once it is loaded into the graph database, we can visualize the whole supply network. Using the interface, researchers can also execute queries or interactively zoom into a particular local segment of the supply network. Figure 3 is such an example where the focal buying firm

Honda and 25 randomly selected top-tier suppliers are visualized. The second component that handles the analytics is a computing engine implemented in statistical programming language R. The component takes supply network data as input, calculates various network centralities measures, and carries out the optimization algorithm as specified in the model to compute NSI scores. Lastly, based on the scores, it generates a list of candidates for researchers and managers to conduct further analysis.

Figure 3. Honda's Local Supply Network (Partially Shown)  
![](/api/attachments/UJB95UUQ/fulltext/images/faabe94ed1d0d94262103ba60990c76788cedb7907c0667d0a0147662d26844e.jpg)

The supply network database then feeds the data to two components in the system that handle the analytics workflow. The first is a user interface for visualizing and navigating the supply network. Taking the Honda dataset, for example, once it is loaded into the graph database, we can visualize the whole supply network. Using the interface, researchers can also execute queries or interactively zoom into a particular local segment of the supply network. Figure 3 is such an example where the focal buying firm Honda and 25 randomly selected top-tier suppliers are visualized. The second component that handles the analytics is a computing engine implemented in statistical programming language R. The component takes supply network data as input, calculates various network centralities measures, and carries out the optimization algorithm as specified in the model to compute NSI scores. Lastly, based on the scores, it generates a list of candidates for researchers and managers to conduct further analysis.

## 5. Results and Evaluation

## 5.1. Analysis results

Using the data-analytics system, we compute NSI scores for all the suppliers in the second and third tiers of Honda’s supply network. We skip the top-tier suppliers because they are all known to Honda and our focus is on identifying unknown but critical suppliers. We do not compute NSI scores for the fourthtier suppliers because we lack data on those in tier 5. In Figure 4, we plot the distribution of NSI scores. We observe a bell-shaped curve with a thin long right tail. The suppliers located at this tail are those identified to be of great importance and, hence, candidates for nexus suppliers. The inflection point on the right side of the curve occurring pretty close to the long tail is encouraging from the management perspective because that means we have only a handful of potential nexus suppliers to consider.

Figure 4. Distribution of NSI Scores in the $2 ^ { \mathbf { n d } }$ and ${ \mathfrak { z } } ^ { \mathbf { r d } }$ Tiers of Honda Supply Network  
![](/api/attachments/UJB95UUQ/fulltext/images/f45ebffd9e6810e1f1450aeb97b549cf87fa31521bdf60118e0d8d1836eca82a.jpg)

In Table 4, we list the top 50 suppliers, ranked in the descending order of NSI scores. We find major multinational companies in the list, such as Siemens, SAP, Hewlett-Packard, and General Electric, across diverse industry sectors such as electronics, chemicals, and software development. We observe an overwhelming majority from the second tier, suggesting a systematic difference between the scores of the tiers 2 and 3 suppliers. Hence, we investigate the respective distributions of NSI scores in the second and third tiers. In Figure 5, the solid and dotted distributions correspond to the second and third tiers, respectively. We find the distribution for the second tier is shifted towards the right, suggesting the tier 2 suppliers on average have a higher NSI score than tier 3 suppliers. The shape of the two curves appears similar, which suggests lack of underlying systematic bias. In Tables 5 and 6, we list the top 50 suppliers by NSI score from the second and third tiers.

Table 4. Top 50 Suppliers Ranked by NSI Score in the $2 ^ { \mathbf { n d } }$ and ${ \mathfrak { z } } ^ { \mathbf { r d } }$ Tiers of Honda Supply Network

<table><tr><td>Rank</td><td>Name</td><td>Tier</td><td>NSI</td><td>Rank</td><td>Name</td><td>Tier</td><td>NSI</td></tr><tr><td>1</td><td>Siemens AG</td><td>2</td><td>1.0000</td><td>26</td><td>Amazon.com Inc</td><td>3</td><td>0.8998</td></tr><tr><td>2</td><td>SAP SE</td><td>2</td><td>0.9711</td><td>27</td><td>Silicon Laboratories Inc</td><td>2</td><td>0.8977</td></tr><tr><td>3</td><td>Hewlett-Packard Co</td><td>2</td><td>0.9701</td><td>28</td><td>Texas Instruments Inc</td><td>2</td><td>0.8976</td></tr><tr><td>4</td><td>General Electric Co</td><td>2</td><td>0.9657</td><td>29</td><td>Bayerische Motoren Werke AG</td><td>3</td><td>0.8969</td></tr><tr><td>5</td><td>Samsung Electronics Co Ltd</td><td>2</td><td>0.9598</td><td>30</td><td>Dow Chemical Co/The</td><td>2</td><td>0.8955</td></tr><tr><td>6</td><td>Microsoft Corp</td><td>2</td><td>0.9327</td><td>31</td><td>ON Semiconductor Corp</td><td>2</td><td>0.8954</td></tr><tr><td>7</td><td>LG Electronics Inc</td><td>2</td><td>0.9319</td><td>32</td><td>BT Group PLC</td><td>2</td><td>0.8953</td></tr><tr><td>8</td><td>Apple Inc</td><td>3</td><td>0.9267</td><td>33</td><td>Daimler AG</td><td>2</td><td>0.8946</td></tr><tr><td>9</td><td>Ford Motor Co</td><td>2</td><td>0.9263</td><td>34</td><td>Ingram Micro Inc</td><td>2</td><td>0.8938</td></tr><tr><td>10</td><td>General Motors Co</td><td>2</td><td>0.9229</td><td>35</td><td>Cisco Systems Inc</td><td>2</td><td>0.8934</td></tr><tr><td>11</td><td>Intel Corp</td><td>2</td><td>0.9209</td><td>36</td><td>Nissan Motor Co Ltd</td><td>2</td><td>0.8922</td></tr><tr><td>12</td><td>Toyota Motor Corp</td><td>2</td><td>0.9199</td><td>37</td><td>Telefonaktiebolaget LM Ericsson</td><td>2</td><td>0.8915</td></tr><tr><td>13</td><td>Accenture PLC</td><td>2</td><td>0.9168</td><td>38</td><td>Airbus Group NV</td><td>3</td><td>0.8910</td></tr><tr><td>14</td><td>Akzo Nobel NV</td><td>2</td><td>0.9135</td><td>39</td><td>Caterpillar Inc</td><td>2</td><td>0.8908</td></tr><tr><td>15</td><td>Sony Corp</td><td>3</td><td>0.9132</td><td>40</td><td>Arrow Electronics Inc</td><td>2</td><td>0.8907</td></tr><tr><td>16</td><td>Flextronics International Ltd</td><td>2</td><td>0.9132</td><td>41</td><td>Avago Technologies Ltd</td><td>2</td><td>0.8903</td></tr><tr><td>17</td><td>Infineon Technologies AG</td><td>2</td><td>0.9130</td><td>42</td><td>Vodafone Group PLC</td><td>2</td><td>0.8902</td></tr><tr><td>18</td><td>Zebra Technologies Corp</td><td>2</td><td>0.9119</td><td>43</td><td>Atmel Corp</td><td>2</td><td>0.8901</td></tr><tr><td>19</td><td>Volkswagen AG</td><td>2</td><td>0.9119</td><td>44</td><td>Open Text Corp</td><td>2</td><td>0.8899</td></tr><tr><td>20</td><td>Fujitsu Ltd</td><td>2</td><td>0.9111</td><td>45</td><td>Adobe Systems Inc</td><td>2</td><td>0.8894</td></tr><tr><td>21</td><td>VeriSign Inc</td><td>2</td><td>0.9100</td><td>46</td><td>Avnet Inc</td><td>2</td><td>0.8856</td></tr><tr><td>22</td><td>ANSYS Inc</td><td>2</td><td>0.9097</td><td>47</td><td>Boeing Co/The</td><td>3</td><td>0.8844</td></tr><tr><td>23</td><td>ABB Ltd</td><td>2</td><td>0.9052</td><td>48</td><td>Polycom Inc</td><td>2</td><td>0.8840</td></tr><tr><td>24</td><td>Linde AG</td><td>2</td><td>0.9012</td><td>49</td><td>Fiat Chrysler Automobiles NV</td><td>3</td><td>0.8824</td></tr><tr><td>25</td><td>Honeywell International Inc</td><td>2</td><td>0.9002</td><td>50</td><td>Danaher Corp</td><td>2</td><td>0.8820</td></tr></table>

Table 5. Top 50 Suppliers Ranked by NSI Score in the $2 ^ { \mathbf { n d } }$ Tier of Honda Supply Network

<table><tr><td>Rank</td><td>Name</td><td>NSI</td><td>Rank</td><td>Name</td><td>NSI</td></tr><tr><td>1</td><td>Siemens AG</td><td>1.0000</td><td>26</td><td>Dow Chemical Co/The</td><td>0.8955</td></tr><tr><td>2</td><td>SAP SE</td><td>0.9711</td><td>27</td><td>ON Semiconductor Corp</td><td>0.8954</td></tr><tr><td>3</td><td>Hewlett-Packard Co</td><td>0.9701</td><td>28</td><td>BT Group PLC</td><td>0.8953</td></tr><tr><td>4</td><td>General Electric Co</td><td>0.9657</td><td>29</td><td>Daimler AG</td><td>0.8946</td></tr><tr><td>5</td><td>Samsung Electronics Co Ltd</td><td>0.9598</td><td>30</td><td>Ingram Micro Inc</td><td>0.8938</td></tr><tr><td>6</td><td>Microsoft Corp</td><td>0.9327</td><td>31</td><td>Cisco Systems Inc</td><td>0.8934</td></tr><tr><td>7</td><td>LG Electronics Inc</td><td>0.9319</td><td>32</td><td>Nissan Motor Co Ltd</td><td>0.8922</td></tr><tr><td>8</td><td>Ford Motor Co</td><td>0.9263</td><td>33</td><td>Telefonaktiebolaget Ericsson</td><td>0.8915</td></tr></table>

<table><tr><td>9</td><td>General Motors Co</td><td>0.9229</td><td>34</td></tr><tr><td>10</td><td>Intel Corp</td><td>0.9209</td><td>35</td></tr><tr><td>11</td><td>Toyota Motor Corp</td><td>0.9199</td><td>36</td></tr><tr><td>12</td><td>Accenture PLC</td><td>0.9168</td><td>37</td></tr><tr><td>13</td><td>Akzo Nobel NV</td><td>0.9135</td><td>38</td></tr><tr><td>14</td><td>Flextronics International Ltd</td><td>0.9132</td><td>39</td></tr><tr><td>15</td><td>Infineon Technologies AG</td><td>0.9130</td><td>40</td></tr><tr><td>16</td><td>Zebra Technologies Corp</td><td>0.9119</td><td>41</td></tr><tr><td>17</td><td>Volkswagen AG</td><td>0.9119</td><td>42</td></tr><tr><td>18</td><td>Fujitsu Ltd</td><td>0.9111</td><td>43</td></tr><tr><td>19</td><td>VeriSign Inc</td><td>0.9100</td><td>44</td></tr><tr><td>20</td><td>ANSYS Inc</td><td>0.9097</td><td>45</td></tr><tr><td>21</td><td>ABB Ltd</td><td>0.9052</td><td>46</td></tr><tr><td>22</td><td>Linde AG</td><td>0.9012</td><td>47</td></tr><tr><td>23</td><td>Honeywell International Inc</td><td>0.9002</td><td>48</td></tr><tr><td>24</td><td>Silicon Laboratories Inc</td><td>0.8977</td><td>49</td></tr><tr><td>25</td><td>Texas Instruments Inc</td><td>0.8976</td><td>50</td></tr></table>

<table><tr><td>Caterpillar Inc</td><td>0.8908</td></tr><tr><td>Arrow Electronics Inc</td><td>0.8907</td></tr><tr><td>Avago Technologies Ltd</td><td>0.8903</td></tr><tr><td>Vodafone Group PLC</td><td>0.8902</td></tr><tr><td>Atmel Corp</td><td>0.8901</td></tr><tr><td>Open Text Corp</td><td>0.8899</td></tr><tr><td>Adobe Systems Inc</td><td>0.8894</td></tr><tr><td>Avnet Inc</td><td>0.8856</td></tr><tr><td>Polycom Inc</td><td>0.8840</td></tr><tr><td>Danaher Corp</td><td>0.8820</td></tr><tr><td>WPP PLC</td><td>0.8816</td></tr><tr><td>MicroStrategy Inc</td><td>0.8800</td></tr><tr><td>salesforce.com inc</td><td>0.8791</td></tr><tr><td>Teradata Corp</td><td>0.8758</td></tr><tr><td>Rio Tinto PLC</td><td>0.8753</td></tr><tr><td>Smiths Group PLC</td><td>0.8752</td></tr><tr><td>Renault SA</td><td>0.8751</td></tr></table>

Table 6. Top 50 Suppliers Ranked by NSI Score in the ${ \mathfrak { z } } ^ { \mathbf { r d } }$ Tier of Honda Supply Network

<table><tr><td>Rank</td><td>Name</td><td>NSI</td><td>Rank</td></tr><tr><td>1</td><td>Apple Inc</td><td>0.9267</td><td>26</td></tr><tr><td>2</td><td>Sony Corp</td><td>0.9132</td><td>27</td></tr><tr><td>3</td><td>Amazon.com Inc</td><td>0.8998</td><td>28</td></tr><tr><td>4</td><td>Bayerische Motoren Werke AG</td><td>0.8969</td><td>29</td></tr><tr><td>5</td><td>Airbus Group NV</td><td>0.8910</td><td>30</td></tr><tr><td>6</td><td>Boeing Co/The</td><td>0.8844</td><td>31</td></tr><tr><td>7</td><td>Fiat Chrysler Automobiles NV</td><td>0.8824</td><td>32</td></tr><tr><td>8</td><td>Royal Dutch Shell PLC</td><td>0.8790</td><td>33</td></tr><tr><td>9</td><td>Hyundai Motor Co</td><td>0.8765</td><td>34</td></tr><tr><td>10</td><td>Verizon Communications Inc</td><td>0.8756</td><td>35</td></tr><tr><td>11</td><td>Lockheed Martin Corp</td><td>0.8749</td><td>36</td></tr><tr><td>12</td><td>Koninklijke Philips NV</td><td>0.8738</td><td>37</td></tr><tr><td>13</td><td>Nestle SA</td><td>0.8658</td><td>38</td></tr><tr><td>14</td><td>Unilever NV</td><td>0.8643</td><td>39</td></tr><tr><td>15</td><td>Peugeot SA</td><td>0.8605</td><td>40</td></tr><tr><td>16</td><td>Telefonica SA</td><td>0.8559</td><td>41</td></tr><tr><td>17</td><td>Bombardier Inc</td><td>0.8555</td><td>42</td></tr><tr><td>18</td><td>Exxon Mobil Corp</td><td>0.8552</td><td>43</td></tr><tr><td>19</td><td>Deutsche Lufthansa AG</td><td>0.8531</td><td>44</td></tr><tr><td>20</td><td>HTC Corp</td><td>0.8527</td><td>45</td></tr><tr><td>21</td><td>AT&amp;T Inc</td><td>0.8481</td><td>46</td></tr><tr><td>22</td><td>Northrop Grumman Corp</td><td>0.8471</td><td>47</td></tr><tr><td>23</td><td>Berkshire Hathaway Inc</td><td>0.8464</td><td>48</td></tr><tr><td>24</td><td>Mitsubishi Motors Corp</td><td>0.8464</td><td>49</td></tr><tr><td>25</td><td>Kia Motors Corp</td><td>0.8460</td><td>50</td></tr></table>

<table><tr><td>Name</td><td>NSI</td></tr><tr><td>Procter &amp; Gamble Co/The</td><td>0.8445</td></tr><tr><td>Rolls-Royce Holdings PLC</td><td>0.8423</td></tr><tr><td>China Mobile Ltd</td><td>0.8383</td></tr><tr><td>RadioShack Corp</td><td>0.8379</td></tr><tr><td>Asustek Computer Inc</td><td>0.8371</td></tr><tr><td>Delta Electronics Inc</td><td>0.8364</td></tr><tr><td>Byd Co Ltd</td><td>0.8358</td></tr><tr><td>China Unicom Hong Kong Ltd</td><td>0.8352</td></tr><tr><td>Huawei Technologies Co Ltd</td><td>0.8337</td></tr><tr><td>Areva SA</td><td>0.8331</td></tr><tr><td>Safran SA</td><td>0.8315</td></tr><tr><td>Koninklijke KPN NV</td><td>0.8284</td></tr><tr><td>Deutsche Post AG</td><td>0.8272</td></tr><tr><td>General Dynamics Corp</td><td>0.8266</td></tr><tr><td>China Telecom Corp Ltd</td><td>0.8264</td></tr><tr><td>Walgreens Boots Alliance Inc</td><td>0.8260</td></tr><tr><td>Petroleo Brasileiro SA</td><td>0.8247</td></tr><tr><td>Robert Bosch GmbH</td><td>0.8240</td></tr><tr><td>Staples Inc</td><td>0.8236</td></tr><tr><td>International Paper Co</td><td>0.8234</td></tr><tr><td>Hyundai Heavy Industries Co</td><td>0.8229</td></tr><tr><td>Textron Inc</td><td>0.8217</td></tr><tr><td>Redington India Ltd</td><td>0.8209</td></tr><tr><td>WPG Holdings Ltd</td><td>0.8205</td></tr><tr><td>Sprint Corp</td><td>0.8193</td></tr></table>

Figure 5. Distribution of NSI Scores by Tier in Honda Supply Network  
![](/api/attachments/UJB95UUQ/fulltext/images/349e383193b2dc4185352ef6b38df921354cedeeedf36fb169284338a961e945.jpg)

We classify the top 50 nexus supplier candidates in the second tier (Table 5) and those in the third tier (Table 6) into three groups: operational, monopolistic, and informational nexus suppliers, according to their characteristics in network structure. We apply the following decision criteria per Table 1:

 A supplier is an operational nexus supplier if its degree, betweenness, and eigenvector centrality values are all in the top 20 percentile among the top 50 nexus suppliers in its own tier. They are expected to have significant influence on the operational performance of Honda’s end products.

 A supplier is a monopolistic nexus supplier if its betweenness centrality value is in the top 10 percentile among the top 50 nexus suppliers in its tier. They are expected to have significant impacts on Honda’s supply continuity.

 A supplier is an informational nexus supplier if the number of unique industries its suppliers encompass is in the top 10 percentile among the top 50 nexus suppliers in its own tier. Due to their diverse ties in the extended supply network, these nexus suppliers are expected to be Honda’s important sources of early market and technological information.

In choosing the cutoff percentage points (i.e., 20% for operational nexus supplier, 10% for monopolistic nexus supplier, and 10% for informational nexus supplier), our goal is to identify the top 5 companies from the 50 nexus suppliers for each category. Supply chain managers should choose the cutoff points based on their specific business requirement and constraints. Applying our cutoff points to the data, we identify the operational, monopolistic, and informational nexus suppliers in the second and third tiers of the Honda supply network, as shown in Tables 7, 8, and 9, respectively. We observe there is a significant overlap between top operational, monopolistic, and informational nexus suppliers. In Tier 2, Siemens, Hewlett-Packard, General Electric, and Samsung are among the top 5 in all three lists, and in Tier 3, Amazon and Koninklijke Philips appear in all three lists. We stress that since our data is on the business relationships between companies, the index captures the criticality of companies in the network of business relationships, so it does not necessarily reflect their importance in terms of material flow.

Table 7. Operational Suppliers

<table><tr><td colspan="5">Tier 2</td></tr><tr><td>Company</td><td>Degree</td><td>Betweenness</td><td>Eigenvector</td><td>NSI</td></tr><tr><td>Siemens AG</td><td>0.0479</td><td>0.0594</td><td>0.0991</td><td>1.0000</td></tr><tr><td>SAP SE</td><td>0.0281</td><td>0.0246</td><td>0.1067</td><td>0.9711</td></tr><tr><td>Hewlett-Packard Co</td><td>0.0514</td><td>0.0414</td><td>0.1652</td><td>0.9701</td></tr><tr><td>General Electric Co</td><td>0.0503</td><td>0.0568</td><td>0.1025</td><td>0.9657</td></tr><tr><td>Samsung Electronics Co</td><td>0.0407</td><td>0.0414</td><td>0.1362</td><td>0.9598</td></tr><tr><td colspan="5">Tier 3</td></tr><tr><td>Company</td><td>Degree</td><td>Betweenness</td><td>Eigenvector</td><td>NSI</td></tr><tr><td>Apple Inc</td><td>0.0327</td><td>0.0274</td><td>0.1015</td><td>0.9267</td></tr><tr><td>Sony Corp</td><td>0.0272</td><td>0.0131</td><td>0.1064</td><td>0.9132</td></tr><tr><td>Amazon.com Inc</td><td>0.0253</td><td>0.0178</td><td>0.0855</td><td>0.8998</td></tr><tr><td>Boeing Co/The</td><td>0.0269</td><td>0.0126</td><td>0.0619</td><td>0.8844</td></tr><tr><td>Koninklijke Philips NV</td><td>0.0281</td><td>0.0169</td><td>0.0652</td><td>0.8738</td></tr></table>

Table 8. Monopolistic Suppliers

<table><tr><td>Company</td><td>Betweenness</td><td>NSI</td></tr><tr><td>Siemens AG</td><td>0.0594</td><td>1.0000</td></tr><tr><td>General Electric Co</td><td>0.0568</td><td>0.9657</td></tr><tr><td>LG Electronics Inc</td><td>0.0505</td><td>0.9319</td></tr><tr><td>Hewlett-Packard Co</td><td>0.0414</td><td>0.9701</td></tr><tr><td>Samsung Electronics Co</td><td>0.0414</td><td>0.9598</td></tr><tr><td>Tier 3</td><td></td><td></td></tr><tr><td>Company</td><td>Betweenness</td><td>NSI</td></tr><tr><td>Apple Inc</td><td>0.0274</td><td>0.9267</td></tr><tr><td>Nestle SA</td><td>0.0246</td><td>0.8658</td></tr><tr><td>Unilever NV</td><td>0.0229</td><td>0.8643</td></tr><tr><td>Amazon.com Inc</td><td>0.0178</td><td>0.8998</td></tr><tr><td>Koninklijke Philips NV</td><td>0.0169</td><td>0.8738</td></tr></table>

Table 9. Informational Suppliers

<table><tr><td colspan="3">Tier 2</td></tr><tr><td>Company</td><td>Industries</td><td>NSI</td></tr><tr><td>General Electric Co</td><td>41</td><td>0.9657</td></tr><tr><td>Siemens AG</td><td>38</td><td>1.0000</td></tr><tr><td>Hewlett-Packard Co</td><td>36</td><td>0.9701</td></tr><tr><td>Telefonaktiebolaget LM Ericsson</td><td>32</td><td>0.8915</td></tr><tr><td>Samsung Electronics Co Ltd</td><td>29</td><td>0.9598</td></tr><tr><td>Volkswagen AG</td><td>29</td><td>0.9119</td></tr><tr><td>Dow Chemical Co/The</td><td>29</td><td>0.8955</td></tr><tr><td>Tier 3</td><td></td><td></td></tr><tr><td>Company</td><td>Industries</td><td>NSI</td></tr><tr><td>Unilever NV</td><td>45</td><td>0.8643</td></tr><tr><td>Nestle SA</td><td>43</td><td>0.8658</td></tr><tr><td>Koninklijke Philips NV</td><td>40</td><td>0.8738</td></tr><tr><td>Amazon.com Inc</td><td>36</td><td>0.8998</td></tr><tr><td>Walgreens Boots Alliance Inc</td><td>33</td><td>0.8260</td></tr></table>

## 5.2. Evaluation and validation: Visit to Honda

One member of our research team met with the supply chain managers of Honda North America to discuss the results. The Honda supply chain managers recognized that the data analytics approach underlying this study of nexus supplier index provides a novel perspective and could be complementary to the current practice of strategic supplier management which is largely material-flow based and risk oriented. Through carefully examining our results (e.g., Tables 4-9), Honda managers found that the proposed NSI analytical framework could contribute to the practice in a number of ways. The lists of nexus supplier candidates based on NSI scores could help managers to look for key companies that they were not aware of (i.e., identifying blind spots in their supply networks). For instance, there were suppliers in the lists we compiled whose names they had not heard before, and seeing them on the list would motivate the Honda managers to begin getting better acquainted with these suppliers.

Further, while Honda managers anticipated Siemens and SAP would come out on top in Table 4, new observation was made that Honda and VW are connected in the tier 2 level (see Table 5). Given that VW was currently experiencing difficulties and might reduce its production, Honda could look at which of the Honda’s top-tier suppliers might end up suffering and take proactive measures to mitigate any potential negative impact. Other novel findings include that Apple is the most important tier 3 supplier to Honda (see Table 6). This was a surprise to Honda managers. It is possible that the suppliers in the second tier may be buying a lot of hardware products from Apple and that is how Apple appears as the most significant nexus supplier at the third tier. However, Apple also sells software and it is possible software produced by Apple may end up in a component that goes into a Honda product. In a sense, our results offer what to look for and where to start looking.

For the suppliers not well-known to Honda, managers expressed that they could start with a small contract to begin the process of discovery and relationship building. Honda can also introduce them to its other supplier companies. For instance, if the NSI list identifies a tier 3 supplier Honda is interested in working with more closely, Honda could introduce this company to other top tier and tier 2 suppliers for potential business relationships. These new findings make it possible for Honda to determine which suppliers and/or their extended business relationships to monitor more closely when making policy or investment decisions. These lists could offer the first cut at which supplier companies to consider.

## 6. Discussion and Implications

Our study attempts to identify critical suppliers that may be embedded deep in a supply chain. A focal buying firm such as Honda may not be aware of these hidden yet critical suppliers called nexus suppliers. We have taken a step toward looking beyond a buying firm’s typical supply chain management space. Since it is impossible to actively manage all suppliers in the supply network, we posit that these nexus suppliers offer a good starting point. To that end, we articulate a way of computing the NSI and show how to use the results from the focal buying firm’s perspective.

To manage a multi-tier supply chain, one needs to engage in the mapping of the supply network (e.g., Choi & Hong, 2002; Pathak et al., 2007). This mapping can be difficult and time-consuming. Often, plant-level supply networks are constructed through the use of bill of materials (BOM) (they identify all suppliers attached to each part and then start building the network one tier at a time). A Japanese semiconductor company mapped their supply networks after the 2011 tsunami and the complete mapping of their supply networks took one year and involved more than 100 people. A pharmaceutical company also revealed to us that when it mapped the supply network for one of its drug products, they had to devote 400 to 500 people and a total of 18 months. Thus, in comparison, even with its granularity

shortcomings (i.e. the data exist at the company level), the use of Bloomberg Terminal data still represents a viable approach to developing the NSI.

According to a Honda top executive, “If we can glean one or two or 10 key hints on the list, these might be suppliers we need to dig into more, partner with, mitigate risk with; there is huge value to that.” NSI provides a company like Honda with insights into which suppliers to partner with. It can help the company look beyond the top-tier level and outside its normal supply chain scope. It can also help the company look at its supply chain differently, not just to manage risks such as natural disasters but also to identify certain suppliers as “nuggets” to facilitate closer partnerships and seek more information sharing.

NSI identifies a new kind of critical suppliers, different from strategic suppliers that a buying company is used to working with (Yan et al., 20015). While a strategic supplier is critical due to its internal attributes, a nexus supplier is critical because of its ties with other suppliers in the supply network. Typically, the focal buying firm and its strategic suppliers have high co-dependence and often undertake costly integration projects (Salvador & Villena, 2013). In contrast, the focal firm and its nexus suppliers are not necessarily connected with each other. Instead of direct connections, they are likely connected over multiple links in an indirect way (Yan et al., 20015). Nexus suppliers may not possess superior capabilities and resources that can have immediate impact on the buying firm. The benefits of managing nexus suppliers consist in the portfolio of ties within the broader supply network. To that end, the focal firm should examine the network positions and embeddedness of its suppliers and evaluate their overall criticality from a network perspective (Choi & Kim, 2008). In essence, the buying firm should try to identify nexus suppliers through the complex interrelations (i.e., links) with its other suppliers in the extended supply network.

Due to the time and resource constraints, many buying firms focus on their top-tier, strategic suppliers. This is understandable, but giving exclusive attention to top-tier suppliers can increase susceptibility to risk. Suppliers further upstream in the supply chain can cause unexpected disruptions to a firm’s operations. In this light, it is crucial for the focal firm to identify its nexus suppliers and seek ways

# ACCEPTED MANUSCRIPT

to manage them proactively. These suppliers may have a profound impact on its performance, depending on how they are embedded in the supply network and how an unforeseen risk event takes place. The influence of a nexus supplier on the focal firm can lag in time, depending again on how many tiers they are removed from the buying firm. Still, the impact of nexus suppliers can be real and significant, especially in the areas of materials flow, emerging ideas, and market information.

## 6.1. Research implications

Implications can be drawn from our data analytics approach for academic research that also uses network data. First, our study showcases the feasibility of identifying potentially important nodes in a network by integrating various centrality measures. Instead of using each measure individually, our DEAbased model combines them into one aggregate measure that reflects the overall criticality of a certain node in the network. Researchers in other disciplines like computer science and psychology can adopt the same approach for developing their own methodologies if a similar need arises from a specific context (e.g., relationship cultivations in social media).

Second, the aggregate measure makes it possible to highlight a node of significance through data visualization and facilitate the drill down capability in data analytics. That is, data scientists can use a number like NSI score to visually rank order the nodes or display them in different sizes and colors to help users focus on most important areas. It is also noted that our DEA-based model takes into account the node importance at multiple levels—at the node level (degree), neighborhood level (eigenvector), and network level (betweenness and farness) (Marsden, 2002; Wasserman & Faust, 1994). Therefore, compared with the individual approaches that rely on a particular centrality measure, our NSI approach is theoretically more comprehensive.

Finally, by letting the data speak for itself, our DEA-based model suggests an objective approach to deciding the weights when combining individual measures for the optimization of NSI scores. Our approach avoids the equal and subjective weighting schemes commonly used in existing studies (e.g., Huang et al., 2014). In other words, our DEA-based model does not assume equal importance for the

centrality measures involved; neither does it assign subjective weights based on the user’s perception about their importance. Instead, our model treats weights as decision variables and objectively decides their values in optimizing NSI scores. In the future, researchers in this genre of studies should look for alternate ways of weighting approaches beyond what we have done here.

## 6.2. Practical implications

Several practical implications can also be drawn from our findings. First, part of the importance of NSI derives from nexus suppliers’ potential to provide strategic information and help enhance the performance of operations at the buying firm. This potential can be only realized if the buying firm would recognize and monitor its nexus suppliers to leverage such potentials. Second, nexus suppliers differ from strategic suppliers in the way they are embedded in the extended supply network (Yan et al., 20015). It is noted that nexus suppliers may not necessarily have superior internal capabilities in terms of operational capability, technological leadership, or strategic cultural congruence with the buying company. As such, the focal firm may easily overlook these critical yet hidden suppliers. Third, the extended supply network is the context through which one identifies nexus suppliers. Managers need to consider a supplier’s relationships not only within the buying firm’s supply base but also with firms outside the base in other related industries.

Our NSI study provides guidelines for supply managers to better understand the concept of nexus suppliers and identify and categorize them into the respective types. As the potential risks incurred by failure of nexus suppliers rise, firms are in need to learn more about nexus suppliers but they have difficulty identifying these critical suppliers. A better understanding of nexus suppliers should help supply managers take a multi-tier network view to look beyond strategic suppliers in the immediate range of its supply network (Craighead et al., 2007; Yan et al., 2015). In a changing business environment, many innovative ideas will come from non-traditional suppliers of parts and components or from start-up enterprises in emerging markets. These suppliers can more appropriately be qualified as nexus suppliers but less likely as strategic suppliers.

# ACCEPTED MANUSCRIPT

NSI can also help firms manage supply risks. For instance, the buying firm could develop a supplier development program, which would require the commitment of significant financial, capital, and personnel resources. It is critical for the buying firm to select the right portfolio of suppliers to be included in the program. However, selecting the right suppliers is not straightforward, as it requires the assessment of a supplier’s true value, determined not only by its internal qualities but also by its network positions. Analysis of the extended supplier network through our NSI model can help in this regard. A supplier can also benefit from a better understanding of how its position in the broader interorganizational networks may affect its value to other customers and stakeholders. It can proactively cultivate the relationships with other firms in its extended supply network, and by doing so, it can gain competitive advantage. For example, once a supplier learns that a particular customer is seeking ideas for product innovation, it can diversify its inter-organizational links to help capture early market signals and share relevant information with that customer. By the same token, upon recognizing its potential value as a nexus supplier to its customers, a supplier can approach them directly as a more attractive candidate for supplier development or investment and seek to develop mutually beneficial long-term relationships.

## 6.3. Limitations

Like any research, our study has limitations. First, we recognize the exploratory nature of our NSI study. The DEA model will need to be further refined as we continue to gather more insights on nexus suppliers. The data-analytics framework is general and the best analytic components can be adapted and adopted on a case-by-case basis. When applying our framework to a different company or dataset, non-DEA approaches (e.g., AHP, MCDP, etc.) can be considered to implement the NSI. Future studies can investigate the advantages and disadvantages of different approaches. Second, the issue of how a nexus supplier may impact the performance of the focal company needs to be further investigated. Our NSI study takes the first step toward a model by which nexus suppliers can be identified and categorized into different types. However, the specific patterns through which the impact on the focal firm’s performance manifests itself still need to be empirically investigated. Third, while the Bloomberg SPLC data provides an extensive coverage of business relationships among firms, its lack of data resolution (e.g., lack of plant- or product-level information, lack of temporal information, etc.) has limited our empirical analysis and interpretation. As another avenue for future research, additional data sources, contexts, and firms (e.g., firms in the service industry) can be sought to further validate and improve the NSI model and the data analytics approach to assess if they can be generalized to other settings. Finally, the focus of our paper is on the identification of nexus suppliers, but each type of nexus suppliers may exhibit different network behaviors and hence have different impacts on the performance of the focal buying firm. Future research can look into such performance impacts in terms of operations, continuity and technological innovations of the focal buying firm based on the types of nexus suppliers.

## 7. Conclusion

In this study, we propose Nexus Supplier Index (NSI), a data-analytics framework for identifying and classifying nexus suppliers. We assess the method’s effectiveness through an empirical application to the real-world supply network of Honda. The novelty and potential of our findings are positively evaluated by Honda managers. To streamline the analytics workflow for NSI, we also build an integrated information system to handle the tasks of data storage, management, navigation, and analytics. Through this research, we put the theory of nexus suppliers into action and demonstrate the value of data analytics in providing supply managers with a better understanding of nexus suppliers both as a management tool and as a practical procedure that can help them manage the risks and harness market opportunities. Our research takes the first step toward the practical use of the nexus supplier concept by identifying and categorizing nexus suppliers with publicly available data (e.g., Bloomberg SPLC). Many firms have difficulty identifying nexus suppliers, let alone knowing how to develop effective strategies for managing relationships with them. Our research provides supply managers with insights into this critical issue and assists them in developing a roadmap to manage nexus supplier relationships.

Using data analytics, we offer a roadmap for the focal buying firm to identify and categorize nexus suppliers. We discuss practical implications and lessons learned from the findings of our study. This

research provides supply managers with insights into the presence of nexus suppliers and assists them in developing potential strategies to better manage this new type of critical suppliers whose importance is grounded in their network structural positions in the supply networks.

## Acknowledgments

The authors thank the anonymous reviewers and the editor-in-chief for their constructive comments and insightful suggestions. Any errors that remain are the sole responsibility of the authors.

## References

Ang, E., lancu, D.A., & Swinney, R. (2017). Disruption Risk and Optimal Sourcing in Multitier Supply Networks. Management Science, 63(8), 2397-2419.

Abrahams, A.S., Fan, W., Wang, G.A., Zhang, Z., & Jiao, J. (2015). An integrated text analytic framework for product defect discovery. Production and Operations Management, 24, 975–990.

Andersson, U., Forsgren, M., & Holm, U. (2002). The strategic impact of external networks: Subsidiary performance and competence development in the multinational corporation. Strategic Management Journal, 23, 979–996.

Arino, A., Abramov, M., Skorobogatykh, I., Rykounina, I., & Vila, J. (1997). Partner selection and trust building in West European-Russian joint ventures: A western perspective. International Studies of Management & Organization, 27, 19–37.

Artto, K., Eloranta, K., & Kujala, J. (2008). Subcontractors’ business relationships as risk sources in project networks. International Journal of Managing Projects in Business, 1, 88–105.

Azadegan, A., Dooley, K.J., Carter, P.L., & Carter, J.R. (2008). Supplier innovativeness and the role of interorganizational learning in enhancing manufacturer capabilities. Journal of Supply Chain Management, 44, 14–35.

Basole, R.C., & Bellamy, M.A. (2014). Visual analysis of supply network risks: Insights from the electronics industry. Decision Support Systems, 67, 109-120.

Basole, R.C., Bellamy, M.A., & Park, H. (2017). Visualization of innovation in global supply chain networks. Decision Sciences, 48(2), 288-306.

Bellamy, M.A., Ghosh, S., & Hora, M. (2014). The influence of supply network structure on firm innovation. Journal of Operations Management, 32, 357–373.

Bensaou, M. (1999). Portfolios of buyer-supplier relationships. Sloan Management Review, 40(4), 35–44.

Bhattacharjee, S., & Cruz, J. (2015). Economic sustainability of closed loop supply chains: A holistic model for decision and policy analysis. Decision Support Systems, 77, 67-86.

Bonacich, P. (1987). Power and centrality: A family of measures. American Journal of Sociology, 92(5), 1170-1182.

Borgatti, S.P., & Li, X. (2009). On social network analysis in a supply chain context. Journal of Supply Chain Management, 45, 5–22.

Carty, S.S. (2012). PA-12 resin shortages from German supplier fire could disrupt auto industry. The Huffington Post, April 17, 2012.

Cavusgil, S.T., Yeoh, P.-L., & Mitri, M. (1995). Selecting foreign distributors: An expert systems approach. Industrial Marketing Management, 24, 297–304.

Chan, H.K., Wang, X., Lacka, E., & Zhang, M. (2016). A mixed-method approach to extracting the value of social media data. Production and Operations Management, 25(3), 568-583.

Charnes, A., Cooper, W.W., & Rhodes, E. (1978). Measuring the efficiency of decision making units, European Journal of Operational Research, 2(6), 429–444.

Chen, I.J., Paulraj, A., & Lado, A.A. (2004). Strategic purchasing, supply management, and firm performance. Journal of Operations Management, 22, 505–523.

Chin, K.S., Wang, Y.M., Poon, G.K.K., & Yang, J.B. (2009). Failure mode and effects analysis by data envelopment analysis. Decision Support Systems, 48(1), 246-256.

Choi, T.Y., Dooley, K.J., & Rungtusanatham, M. (2001). Supply networks and complex adaptive systems: Control versus emergence. Journal of Operations Management, 19, 351–366.

Choi, T.Y., & Hong, Y. (2002). Unveiling the structure of supply networks: Case studies in Honda, Acura, and DaimlerChrysler. Journal of Operations Management, 20, 469–493.

Choi, T.Y., & Kim, Y. (2008). Structural embeddedness and supplier management: A network perspective. Journal of Supply Chain Management, 44, 5–13.

Choi, T.Y., Linton, T. (2011). Don’t let your supply chain control your business. Harvard Business Review 89. 112–117.

Chou, Y.C., & Shao, B.B.M. (2014). Total factor productivity growth in information technology services industries: A multi-theoretical perspective. Decision Support Systems, 62(1), 106-118.

Coelli, T.J., Rao, D.S.P., O’Donnell, C.J., & Battese, G.E. (2005). An Introduction to Efficiency and Productivity Analysis. New York, NY: Springer Science & Business Media.

Cook, W.D., Tone, K., & Zhu, J. (2014). Data envelopment analysis: Prior to choosing a model. Omega, 44, 1-4.

Craighead, C. W., Blackhurst, J., Rungtusanatham, M. J., & Handfield, R. B. (2007). The severity of supply chain disruptions: Design characteristics and mitigation capabilities. Decision Sciences, 38(1), 131-156.

Dacin, M.T., Ventresca, M.J., & Beal, B.D. (1999). The embeddedness of organizations: Dialogue & directions. Journal of Management, 25, 317–356.

Dong, M.C., Liu, Z., Yu, Y., & Zheng, J.-H. (2015). Opportunism in distribution networks: The role of network embeddedness and dependence. Production and Operations Management, 24, 1657–1670.

Dyer, J.H., & Singh, H. (1998). The relational view: Cooperative strategy and sources of interorganizational competitive advantage. Academy of Management Review, 23, 660–679.

Echols, A., & Tsai, W. (2005). Niche and performance: The moderating role of network embeddedness. Strategic Management Journal, 26, 219–238.

Ellram, L.M., & Carr, A. (1994). Strategic purchasing: A history and review of the literature. Journal of Supply Chain Management, 30(1), 9–19.

Färe, R., Grosskopt, S., Norris, M., & Zhang, Z. (1994). Productivity growth, technical progress, and efficiency change in industrialized countries. American Economic Review, 84(1), 66-83.

Ferreira, K.J., Lee, B.H.A., & Simchi-Levi, D. (2016). Analytics for an online retailer: Demand forecasting and price optimization. Manufacturing & Service Operations Management, 18(1), 69-88.

Freeman, L. C. (1978). Centrality in social networks conceptual clarification. Social Networks, 1(3), 215- 239.

Gadde, L.-E., & Snehota, I. (2000). Making the most of supplier relationships. Industrial Marketing Management, 29, 305–316.

Giannoulis, C., & Ishizaka, A. (2010). A Web-based decision support system with ELECTRE III for a personalised ranking of British universities. Decision Support Systems, 48(3), 488-497, 2010.

Gnyawali, D.R., & Madhavan, R. (2001). Cooperative networks and competitive dynamics: A structural embeddedness perspective. Academy of Management Review, 26, 431–445.

Gulati, R., & Gargiulo, M. (1999). Where do interorganizational networks come from? American Journal of Sociology, 104, 177–231.

Guo, P., Song, J.S., & Wang, Y. (2010). Outsourcing structures and information flow in a three-tier supply chain. International Journal of Production Economics, 128, 175-187.

Hagedoorn, J. (2006). Understanding the cross-level embeddedness of interfirm partnership formation. Academy of Management Review, 31, 670–680.

Hitt, M.A., Dacin, M.T., Levitas, E., Arregle, J.-L., & Borza, A. (2000). Partner selection in emerging and developed market contexts: Resource-based and organizational learning perspectives. Academy of Management Journal, 43, 449–467.

Hu, B., Kostamis, D. (2015). Managing supply disruptions when sourcing from reliable and unreliable suppliers. Production and Operations Management, 24, 808–820.

Huang, S., Lv, T., Zhang, X., Yang, Y., Zheng, W., & Wen, C. (2014). Identifying node role in social network based on multiple indicators. PLOS ONE, 9(8), 1–16.

Huang, T., & Van Mieghem, J.A. (2014). Clickstream data and inventory management: Model and empirical analysis. Production and Operations Management, 23, 333–347.

Kaufman, A., Wood, C.H., & Theyel, G. (2000). Collaboration and technology linkages: A strategic supplier typology. Strategic Management Journal, 21, 649–663.

Kilduff, M. & Tsai, W. (2003). Social Networks and Organizations. Sage Publications, London.

Kim, Y., Choi, T.Y., Yan, T., & Dooley, K. (2011). Structural investigation of supply networks: A social network analysis approach. Journal of Operations Management, 29, 194–211.

Korhonen, P., & Syrjänen, M. (2004). Resource allocation based on efficiency analysis. Management Science, 50(8), 1134-1144.

Koufteros, X., Vickery, S.K., & Dröge, C. (2012). The effects of strategic supplier selection on buyer competitive performance in matched domains: Does supplier integration mediate the relationships? Journal of Supply Chain Management, 48, 93–115.

Kraljic, P. (1983). Purchasing must become supply management. Harvard Business Review, 61(5), 109– 117.

Li, C. (2013). Sourcing for supplier effort and competition: Design of the supply base and pricing mechanism. Management Science, 59, 1389-1406.

Li, T., Sethi, S.P., & Zhang, J. (2013). Supply diversification with responsive pricing. Production and Operations Management, 22, 447–458.

Liu, F.-H.F., & Hai, H.L. (2005). The voting analytic hierarchy process method for selecting supplier. International Journal of Production Economics, 97, 308–317.

Mackelprang, A. W., Bernardes, E., Burke, G. J., & Welter, C. (2017). Supplier innovation strategy and performance: A matter of supply chain market positioning. Decision Sciences (forthcoming).

Mafakheri, F., Breton, M., & Ghoniem, A. (2011). Supplier selection-order allocation: A two-stage multiple criteria dynamic programming approach. International Journal of Production Economics, 132, 52–57.

Marsden, P. V. (2002). Egocentric and sociocentric measures of network centrality. Social Networks, 24(4), 407-422.

McCarter, M.W., & Northcraft, G.B. (2007). Happy together? Insights and implications of viewing managed supply chains as a social dilemma. Journal of Operations Management, 25, 498–511.

Monczka, R.M., Petersen, K.J., Handfield, R.B., & Ragatz, G.L. (1998). Success factors in strategic supplier alliances: The buying company perspective. Decision Sciences, 29, 553–577.

Olsen, R.F., & Ellram, L.M. (1997). A portfolio approach to supplier relationships. Industrial Marketing Management, 26, 101–113.

Pathak, S.D., Day, J.M., Nair, A., Sawaya, W.J., & Kristal, M.M. (2007). Complexity and adaptivity in supply networks: Building supply network theory using a complex adaptive systems perspective. Decision Sciences, 38, 547–580.

Salvador, F., & Villena, V.H. (2013). Supplier integration and NPD outcomes: Conditional moderation effects of modular design competence. Journal of Supply Chain Management, 49(1), 87-113.

Sherman, H.D., & Zhu, J. (2006). Service Productivity Management: Improving Service Performance Using Data Envelopment Analysis (DEA). New York, NY: Springer Science & Business Media.

## ACCEPTED MANUSCRIPT

Simchi-Levi, D. (2014). OM research: From problem-driven to data-driven research. Manufacturing & Service Operations Management, 16, 2–10.

Slobodow, B., Abdullah, O., & Babuschak, W.C. (2008). When supplier partnerships aren’t. Sloan Management Review, 49(2), 77-83.

Talluri, S., DeCampos. H.A., & Hult, G.T.M. (2013). Supplier rationalization: A sourcing decision model. Decision Sciences, 44(1), 57-86.

Wagner, S.M., & Johnson, J.L. (2004). Configuring and managing strategic supplier portfolios. Industrial Marketing Management, 33, 717–730.

Wasserman, S., & Faust, K. (1994). Social Network Analysis. New York: Cambridge University Press.

Wu, W.Y., Shih, H.-A., & Chan, H.-C. (2009). The analytic network process for partner selection criteria in strategic alliances. Expert Systems with Applications, 36, 4646–4653.

Yahya, S., & Kingsman, B. (1999). Vendor rating for an entrepreneur development programme: A case study using the analytic hierarchy process method. Journal of the Operational Research Society, 50, 916–930.

Yan, T., Choi, T.Y., Kim, Y., & Yang, Y. (2015). A theory of the nexus supplier: A critical supplier from a network perspective. Journal of Supply Chain Management, 51, 52–66.

Yim, A. (2014). Failure risk and quality cost management in single versus multiple sourcing decision. Decision Sciences, 45(2), 341-354.

Zahra, S.A., Ireland, R.D., Gutierrez, I., & Hitt, M.A. (2000). Introduction to special topic forum privatization and entrepreneurial transformation: Emerging issues and a future research agenda. Academy of Management Review, 25, 509–524.

# ACCEPTED MANUSCRIPT

Biographic Note

Benjamin Shao is an associate professor of information systems and the co-director of the Digital Society Initiative in the W. P. Carey School of Business at Arizona State University. His research interests include IT impacts, business analytics, IT supply chain interface, and healthcare IT.

Zhan (Michael) Shi is an assistant professor of information systems at W.P. Carey School of Business, Arizona State University. He uses economic models and machine learning methods to study digita product markets, social and organization networks, and entrepreneurship in the tech industry.

Thomas Choi is Harold E. Fearon Chair of Purchasing Management at W. P. Carey School of Business, Arizona State University. He has been studying the upstream side of supply chains, where a buying company interfaces with many suppliers organized in various forms of networks.

Sangho Chae is an assistant professor of supply chain management in Tilburg School of Economics and Management at Tilburg University. His research interests include supply network structure, multi-tier supply chain management, and behavioral aspects of supply chain decision-making.

# ACCEPTED MANUSCRIPT

## Highlights

 We propose a data-analytic approach for identifying hidden critical suppliers in supply networks.

 We construct a large dataset of the multi-tier supply network of Honda Motors.

 We apply our data-analytic method to analyze Honda’s supply network and identify the nexus suppliers.

 We review the method and results with the supply management team at Honda America.
