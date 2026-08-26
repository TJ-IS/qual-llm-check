---
otero_id: 7188
otero_key: "KKQDAXY3"
title: "Visual analysis of supply network risks: Insights from the electronics industry"
authors: "Rahul C. Basole; Marcus A. Bellamy"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.08.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Visual analysis of supply network risks: Insights from the electronics industry

Rahul C. Basole <sup>a,</sup>⁎, Marcus A. Bellamy

<sup>a</sup> School of Interactive Computing & Tennenbaum Institute, Georgia Institute of Technology, 85 Fifth Street NW, Atlanta, GA 30332, USA

<sup>b</sup> Scheller College of Business & Tennenbaum Institute, Georgia Institute of Technology, 800 West Peachtree Street NW, Atlanta, GA 30308, USA

## a r t i c l e i n f o

Article history: Received 13 December 2013 Received in revised form 16 June 2014 Accepted 31 August 2014 Available online xxxx

Keywords: Supply networks Risk management Visualization Network analysis Decision support Electronics industry

## a b s t r a c t

In today's complex, global supply networks it has become increasingly challenging to identify, evaluate, and mitigate risks of disruption. Traditional supply chain practices have primarily focused on dyadic risk management, rarely considering risks in the sub-tier supply network. However, this approach severely limits a decision maker's ability to understand the highly interconnected nature of systemic risks and develop corresponding mitigation strategies. Grounded in theories of supply chains as complex systems, network analysis, and risk management, we demonstrate the importance of visual decision support for supply network risk assessment. We empirically illustrate our approach with supply network visualization examples from the electronics industry. We conclude the study with implications for the design and implementation of visual supply network decision support systems and future research opportunities.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Managing supply chain risks in today's dynamic business environment is becoming increasingly challenging as traditionally linear supply chains are replaced by complex, global supply networks [12]. With growing interdependencies among <sup>fi</sup>rms in these networks, risks of all types – including operational failures, <sup>fi</sup>nancial distress, labor issues, weak economic climates, cultural differences, and political instability – can rapidly cascade through the entire supply chain enterprise and cripple its performance [16]. Despite increasing digital interconnectedness, visibility into sub-tiers is often limited and not available. Yet, increased competition and customer demands require <sup>fi</sup>rms to design and manage their supply chain enterprise in such a fashion that sustains their capability to manufacture and deliver their products and services just as well or preferably better than their competitors [59].

Previous research has shown that many <sup>fi</sup>rms are not adequately prepared for assessing and addressing supply chain risks and disruptions [42]. One reason is that traditional practices rarely consider the complex interconnected and multi-dimensional nature of supply network risk beyond the <sup>fi</sup>rst tier and there is a lack of literature on system analysis and decision support models for insight into systemic risk [93,94]. Given the continuing shift of enterprises toward network-centric forms of organization and the multi-dimensional nature of supply network risk, novel tools and approaches for supply chain risk management are thus required.

One emerging <sup>fi</sup>eld, visual network analytics, which fuses complex network analysis with information visualization, promises to provide important methods and interactive tools to comprehensively examine the structural complexities of supply networks and aid supply chain managers in the discovery, exploration, and resolution of potentially hidden sources of risk [7,8,6]. Grounded in theories of supply chains as complex systems, risk management, and network analysis, we demonstrate the importance of visual decision support for supply network risk assessment. We empirically illustrate our approach with supply network visualization examples from the electronics industry.

Theoretically, this study contributes to our broader understanding of visual decision support for complex risk management tasks. We show that a visual network analytic approach provides superior insight into supply network risk and can greatly facilitate decision making. More broadly, we contribute to research at the interface of information systems and operations management, in general, and decision support in a supply network context in particular. From a managerial perspective, we address an important practical need of designing and developing effective decision support capabilities that help identify and assess complex global supply risk in a systemic and interactive way. The visual approach proposed in our study thereby also addresses the call to expand decision makers' tool kit of decision support tools [29].

The remainder of the study is structured as follows. Section 2 provides the theoretical background. Section 3 describes our methodology, data, metrics, and visualization approach. Section 4 presents the analysis and discusses the results. Section 5 concludes the study and provides future research opportunities.

R.C. Basole, M.A. Bellamy / Decision Support Systems xxx (2014) xxx–xxx

## 2. Theoretical foundation

## 2.1. Supply chains as complex networked systems

There has been a long-standing recognition that supply chains are systems [39]. Building on Porter's linear value chain framework [107,90], for instance, describes a supply chain as a system whose constituent parts include material suppliers, production facilities, distribution services, and customers linked together via a feed forward <sup>fl</sup>ow of materials and the feedback <sup>fl</sup>ow of information. Today, supply networks are composed of a diverse set of vertical and horizontal interactions between suppliers, manufacturers, distributors, retailers, and customers, which have transformed the traditional linear supply chain into a complex network of interactions between system members [24]. At the same time, globalization has led to geographically dispersed supply chains with high levels of inter<sup>fi</sup>rm dependency [108]. Management of such complex networked systems requires signi<sup>fi</sup>cant coordination, collaboration, delegation, and monitoring [12].

Traditional supply chain modeling and analyses have employed a dyadic approach and focused on <sup>fi</sup>rms in isolation. This approach, however, fails to account for the systemic effects resulting from the complex structural and behavioral aspects inherent in supply networks [15]. It has been argued that effective supply chain management must emphasize the importance and consideration of behavior and performance of the entire supply network [81]. In particular, research has shown the particular value and applicability in modeling supply networks as complex networked systems comprised of autonomous, self-organizing, interdependent, and adaptive members involved in the manufacturing, integration, and delivery of products and services [24,91].

Bellamy and Basole [15] argue that there are three distinct but related research themes that characterize network analytic studies of supply chains as complex networked systems: system architecture (i.e. network structure), system behavior (i.e. supply network dynamics), and system policy and control (i.e. supply network strategy). Since supply networks represent a socially constructed organizational structure, a complex network approach enables incorporating both technical and social issues and thereby offering a more complete picture of supply network phenomena and their implications on performance [18]. The network lens draws on the well-established <sup>fi</sup>eld of graph theory. Several decision support-related studies have adopted the network lens to investigate: sampling and classi<sup>fi</sup>cation techniques for various network topologies [1], work<sup>fl</sup>ow execution using social network metrics to capture team cohesion [4], the in<sup>fl</sup>uence of individual knowledge on the structure of advice network relationships [49], and identi<sup>fi</sup>cation of highly in<sup>fl</sup>uencing nodes based on the topology of their network [51,54].

In the supply network context, nodes represent <sup>fi</sup>rms (or other organizational entities, such as factories) and edges represent relationships between <sup>fi</sup>rms, such as buyer–supplier relationships, material <sup>fl</sup>ow, and information exchange. The resulting topology and its structural properties describe the position and (inter)connectedness of <sup>fi</sup>rms within the supply network [50]. It has been argued that real-world supply networks assume one of three common supply network topologies (e.g. random, small-world and scale-free networks), each with its own strengths and weaknesses [74]. More speci<sup>fi</sup>cally, supply chain-related studies have shown that the structure has signi<sup>fi</sup>cant implications on performance, dynamics, and governance [66,74]. Basole et al. [9], for example, empirically show that central supply network <sup>fi</sup>rms tend to be in more powerful and in<sup>fl</sup>uential positions, helping them reduce transactional costs and improve operational ef<sup>fi</sup>ciency, ultimately leading to better operating and business performance. It has also been shown that the type and nature of supply network relationships matter as well. For instance Yli-Renko et al. [109], identi<sup>fi</sup>ed that the strength of network relations positively facilitates knowledge exchange and Oke and colleagues [73,72] found that strength of ties positively affects new product development outcomes.

## 2.2. Supply network risk assessment

Supply chain managers conduct risk assessments with different intentions. Whereas some supply chain managers may look for speci<sup>fi</sup>c supply chain vulnerabilities, others may want to obtain a big picture of the overall “health” of the supply network [7]. As contemporary supply networks continue to transform in both scale and complexity, the variety of risks that supply chain managers must identify, assess, and mitigate has grown substantially as well [16]. Prior research in decision support has made some progress, resorting to data on manager perceptions of risk [56] and simulation studies [85] to study supply chain risk management.

## 2.2.1. Types of risks

There are a wide variety of risks that exist in supply networks [94,102]. Broadly, these risks can be categorized according to whether the source of risk lies inside (endogenous) or outside (exogenous) the supply network [98].

Exogenous risks arise from the uncertainty faced by the supply network that cannot be controlled by the focal <sup>fi</sup>rm or the other entities in the supply network. Common exogenous risks are political/country risk, regulatory risk, disaster risk, and foreign exchange rate risk. Political/ country risk emanates from the political turmoil or acts of terrorism affecting a country where part of a focal <sup>fi</sup>rm's production or distribution resides [52]. Regulatory risk relates to uncertainty from import/export costs and restrictions [23] as well as from environmental, health, and safety regulations [62]. Disaster risk arises from catastrophic events such as earthquakes, hurricanes, <sup>fi</sup>res and disease outbreaks [26,71]. Exchange rate risk stems from the <sup>fl</sup>uctuating exchange rates experienced by a country involved in the production or distribution phases of a <sup>fi</sup>rm's supply network. This sort of risk is ampli<sup>fi</sup>ed when a <sup>fi</sup>rm has no or limited <sup>fl</sup>exibility in co-locating facilities in various countries to hedge against the volatility in exchange rates [44,47]. Examples of real-world supply chain disruptions originating from exogenous risk factors are plentiful. Ericsson incurred a \$400 million loss in sales after a massive <sup>fi</sup>re destroyed millions of microchips at its semiconductor plant in New Mexico [55]. Compaq, Apple, and Gateway suffered delayed shipments lasting several weeks and, in some cases, months after an earthquake struck Taiwan, leaving these companies unable to receive key computer components for their products [57]. Ford, Toyota, and DaimlerChrysler faced signi<sup>fi</sup>cant indirect consequences from the terrorist attacks of September 11, particularly major supply disruptions at their North-American assembly plants [86].

In contrast to exogenous risks, endogenous risks emerge inside the supply network and are dependent on the relationships between the focal <sup>fi</sup>rm, its supply base, and its customer base [98]. Examples of endogenous risks include operational risk, <sup>fi</sup>nancial risk, collaboration risk, strategic risk, and information risk. Operational risk relates to the events that can lead to lower operational effectiveness and capabilities of the <sup>fi</sup>rm. This type of risk emanates from issues such as inadequate manufacturing or processing capability, low process stability, and changes in technology [61]. Financial risk affects the <sup>fi</sup>nancial sustainability and growth of a <sup>fi</sup>rm. While a <sup>fi</sup>rm's own <sup>fi</sup>nancial state obviously affects their level of <sup>fi</sup>nancial risk, the <sup>fi</sup>nancial instability of a <sup>fi</sup>rm's suppliers has also been shown to make that <sup>fi</sup>rm more vulnerable to risk (e.g. [43]). This is possible as the <sup>fi</sup>rm may absorb some <sup>fi</sup>nancial shock from the <sup>fi</sup>nancial instability of one or more suppliers in their supply network (e.g. from the default, insolvency, or bankruptcy of a supplier) [3,104]. Greater vulnerability within a supply network can thus stem from detrimental <sup>fi</sup>nancial health conditions of a <sup>fi</sup>rm's individual suppliers [17,96,105]. Collaboration risk is based on a <sup>fi</sup>rm's degree of collaboration with its suppliers and customers [7]. Collaboration risk comes from lack of ability to support the operations or governance mechanisms between a <sup>fi</sup>rm and its partners, contractual obligations that constrain <sup>fi</sup>rm relationships with partners, and lack of trust in non-contractual interactions [16]. Information risk relates to the level

Please cite this article as: R.C. Basole, M.A. Bellamy, Visual analysis of supply network risks: Insights from the electronics industry, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.08.008

of information accuracy, information system security and disruption, intellectual property, and information outsourcing of a <sup>fi</sup>rm [98]. Lastly, strategic risk affects a <sup>fi</sup>rm's ability to manage and execute change initiatives [7]. A primary strategic risk while working to transform a supply network is failing to get stakeholders to understand and be aligned with a focal <sup>fi</sup>rm's intents to avoid serious time delays and performance barriers. Another major strategic risk is how to manage the supply network using the right balance between a command-and-control an incentive/ penalties governance system that results in the desired supply network behavior and performance [16].

While several endogenous risks arise from a <sup>fi</sup>rm's environment, previous research has also emphasized that these risks can come upstream from suppliers or downstream from customers [92]. Supply risk emanates from the disruption of supply, inventory, schedules, and technology access, price escalation, quality issues, technological uncertainty, product complexity, and frequent design changes. Demand risk can arise from new product introductions, variations in demand due to fads, seasonality, and disruptive technologies, and demand distortion and ampli<sup>fi</sup>cation [61]. Table A.1 provides a summary of risk metrics. In light of this multi-dimensionality of risk and the rapidly growing global interconnectedness, complexity, and scale of supply chains, new risk analysis and assessment tools are needed that go beyond traditional but limited approaches most commonly used [20].

## 2.2.2. Risk assessment tasks

Corresponding to these risks, prior literature has suggested that supply chain managers pursue many different risk assessment tasks [38,41,61,111]. When analyzing supply networks, supply chain managers can gain valuable insight into understanding potential risks by focusing on the structural characteristics of supply networks. Knowledge of and insight into these types of structural characteristics of supply networks can signi<sup>fi</sup>cantly help in revealing risks and vulnerabilities as well as possible paths of risk diffusion in supply networks. Based on our literature review and <sup>fi</sup>eld studies with practitioners, several relevant tasks related to the structural characteristics and risk assessment of supply networks can be identi<sup>fi</sup>ed. These are shown in Table 1 below.

## 3. Methodology

Our research approach consists of four fundamental steps: (1) identi-<sup>fi</sup>cation and curation of relevant supply network structure and risk data, (2) construction of multi-tier supply networks for a given focal <sup>fi</sup>rm, (3) computation of both structural and risk metrics, and (4) visualization of risk-encoded supply networks.

## 3.1. Data

Our study utilized multiple data sources to construct the supply network structure of <sup>fi</sup>rms operating in the electronics industry. We focused our study on <sup>fi</sup>rms in the electronics industry for several reasons.

## Table 1

Common risk assessment tasks.

<table><tr><td>Level</td><td>Task description</td></tr><tr><td>Firm</td><td>(T1) Identify the most influential partner(s) in the supply network(T2) Determine the patterns of interaction between shared partners, first tier and beyond(T3) Identify partner(s) whose removal would result in the disruption of the supply network(T4) Identify direct and sub-tier partners with high levels of risk(T5) Determine the risk concentration across each tier</td></tr><tr><td>Network</td><td>(T6) Describe the overall structure of the supply network(T7) Identify how risk is distributed across the supply network(T8) Determine variation in risk by tier and by number of direct partners(T9) Determine variation in supply network visibility by tier and number of direct partners</td></tr></table>

First, the electronics industry is characterized by high levels of collaboration and partnering [89]. Second, the electronics industry is considered a fast clockspeed industry with new products and services emerging rapidly [33]. Lastly, the electronics industry is global in nature with the bulk of <sup>fi</sup>rms coming from North America, Europe, and Asia. Consequently, our context will enable us to account for potential geographic differences in supply networks.

The network structure was built using two data sources: Thomson Reuters Financial SDC Platinum Alliance & Joint-Venture (SDC Platinum) database and Connexiti. The SDC Platinum database is a commonly used data source for the study of strategic alliances and inter<sup>fi</sup>rm networks and is regarded as one of the most comprehensive databases of its kind [78]. SDC Platinum includes information on many different types of relationships, including strategic alliances, supply, research and development (R&D), marketing, licensing and manufacturing. We included all active relationships from 2005–2009 in which at least one of the <sup>fi</sup>rms participated in. We excluded relationships that were terminated during this time period. We cross-validated and augmented the SDC Platinum dataset with relationship information from Connexiti. Connexiti is a comprehensive supply chain intelligence database that captures both supply and customer relationships for 20,000+ global <sup>fi</sup>rms. Several previous studies have used Connexiti to study inter<sup>fi</sup>rm networks in the information and communication technology industry (e.g. [5,9]). The <sup>fi</sup>nal dataset included 911 <sup>fi</sup>rms and 7311 unique relationships.

The three-tier supply network of each <sup>fi</sup>rm was constructed using a binary adjacency matrix, with cell entries marked as 1 if there is any relationship between two <sup>fi</sup>rms and 0 otherwise. Since we were primarily concerned whether a relationship between two <sup>fi</sup>rms exists and not with multiplex relationships, multiple relationships between the same pair of <sup>fi</sup>rms were treated as a single link (see [79]). Furthermore, as collaborative relationships are considered to be bidirectional, it resulted in an undirected unipartite graph [69].

## 3.2. Metrics

## 3.2.1. Betweenness centrality (structural importance)

There are many topological measures that have been used to describe the structural importance of a node (<sup>fi</sup>rm) in a network [50]. Borgatti and Li [18] identi<sup>fi</sup>ed betweenness centrality as one particularly relevant measure in a supply chain context. A <sup>fi</sup>rm's betweenness centrality re<sup>fl</sup>ects the amount of control it exerts over the interactions of other <sup>fi</sup>rms in the network. A <sup>fi</sup>rm will have a high betweenness centrality score if many supply network partners use the <sup>fi</sup>rm as an intermediate source (forming a direct connection between the particular partner and <sup>fi</sup>rm) to link them with other partners in the network (forming an indirect connection between the particular partner and another partner in the network) [18]. These <sup>fi</sup>rms are considered important because if they disappeared or slowed production they would affect many more <sup>fi</sup>rms than those with lower betweenness scores. Similar to keystones in the ecosystem context, <sup>fi</sup>rms with high betweenness thus in<sup>fl</sup>uence the health of the entire network [45].

Following [34], we calculate betweenness centrality $C _ { B } ( \nu )$ as follows:

$$
C _ {B} (v) = \sum_ {s \neq v \neq t \in V} \frac {\sigma_ {s t} (v)}{\sigma_ {s t}}\tag{1}
$$

where $\sigma _ { s t } = \sigma _ { t s }$ denotes the number of shortest paths from $\mathsf { s } \in V _ { } \mathrm { t } 0 t \in V ,$ where $\sigma _ { s s } = 1$ by convention, and $\sigma _ { s t } ( \nu )$ denotes the number of shortest paths from s to t that some $\nu \in V$ lies on.

## 3.2.2. Altman Z-Score (financial risk)

Previous studies have highlighted a <sup>fi</sup>rm's vulnerability to risks emanating from the detrimental or failed health of its supply chain partners [17,43,96,105]. It is therefore important that decision makers make use of widely applicable measures in their risk assessment of their partners.

Please cite this article as: R.C. Basole, M.A. Bellamy, Visual analysis of supply network risks: Insights from the electronics industry, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.08.008

One such widely used measure is the Altman Z-Score, developed by Edward Altman [2] and highly praised as having strong predictive ability of a <sup>fi</sup>rm's distress in today's competitive environment.<sup>1</sup> The Z-Score is a composite reference measure that uses weighted coef<sup>fi</sup>cients on <sup>fi</sup>ve <sup>fi</sup>nancial factors: Working Capital/Total Assets $( X _ { 1 } ) _ { \mathrm { { } } } .$ , Retained Earnings/ Total Assets $\left( X _ { 2 } \right)$ , Earnings Before Interest and Tax/Total Assets $\left( { { X } _ { 3 } } \right)$ Market Value of Equity/Total Liabilities $( X _ { 4 } )$ , and Sales/Total Assets $( X _ { 5 } )$ . The Z-Score for a <sup>fi</sup>rm is computed as follows:

$$
Z = 1. 2 X _ {1} + 1. 4 X _ {2} + 3. 3 X _ {3} + 0. 6 X _ {4} + 1. 0 X _ {5}.\tag{2}
$$

Once a Z-Score is calculated, it is then compared against Altman's cutoff points, which are as follows:

• if Z N 2.99, a <sup>fi</sup>rm has a low risk of bankruptcy;

• if 2.99 N Z N 1.81, a <sup>fi</sup>rm has an intermediate risk of bankruptcy;

• if Z b 1.81, a <sup>fi</sup>rm has a high risk of bankruptcy.

We calculated Z-Scores for all public <sup>fi</sup>rms in our dataset using the Compustat database.

## 3.2.3. Inventory variability (operational risk)

In addition to <sup>fi</sup>nancial risk, we use inventory variability (IV) as an illustrative example for operational risk. Great variability in a supplier's inventory can lead to increased uncertainty in delivery times to its customers. If such delays arise as a result, it causes instable levels of production lead times [84]. Moreover, delivery delays hinder the <sup>fl</sup>ow of goods and services through the supply-chain, ultimately resulting in poor service [40]. Analogous to <sup>fi</sup>nancial risk, we code operational risk at low, medium, or high levels as follows:

• if IV N 75.72, a <sup>fi</sup>rm has a low operational risk;

• if $1 2 7 7 . 9 8 > I V > 7 5 . 7 2 ,$ , a <sup>fi</sup>rm has an intermediate operational risk;

• i $\ : \lceil V < 1 2 7 7 . 9 8 , i$ a <sup>fi</sup>rm has a high operational risk.

We calculated IV level for all public <sup>fi</sup>rms in our dataset using the Compustat database.

## 3.3. Visualization

Graphical visualization of supply networks can provide signi<sup>fi</sup>cant new insights into their underpinning structure, dynamics and strategy [15,25]. Contrary to the perception that supply network visualizations are merely artistic representations of complex socio-technical systems, they can be used to explore, interpret and communicate data in order to aid decision makers in overcoming their cognitive limitations, making structure, patterns, relationships and themes visible, and providing a means to ef<sup>fi</sup>ciently comparing multiple representations of the same data [10]. Indeed, visualization has been identi<sup>fi</sup>ed as an integral part of the scienti<sup>fi</sup>c approach and considered a fundamental method of transforming data to knowledge [100]. Examples of visual representations of networks include biological and ecological networks, social networks, the Internet and citation networks [70].

Graphical visualizations of collaborative networks are increasingly used as an important complement to traditional summaries of network statistics [5,11,46,76,75,78,79]. Basole [5] for example uses visualization to describe the structure of the converging mobile ecosystem. Powell et al. [76] use network representations to describe the evolution of collaboration in the life sciences industry. Iyer et al. [46] visualize the small-world structure in the software industry. Rosenkopf and Schilling [79] argue that visualizations are particularly effective when trying to explain substantive differences between network structures. They demonstrate their approach with a visualization of nine industry network structures. It has been suggested that visual approaches can be extremely valuable for understanding and analyzing business issues, including competitive intelligence, strategy, scenario planning and problemsolving [99].

All of these studies, however, consider portraying the structure of the entire industry. There are no existing studies that have provided a visual comparison of the collaborative network structure of individual <sup>fi</sup>rms. One possible explanation for the scarcity of supply network visualizations is that it is not only a very challenging and dif<sup>fi</sup>cult task but also very resource intensive. Complete or even comprehensive supply network data is generally not available. At the same time, even if the data is collected and appropriately curated, the amount of information can often be overwhelming to the end-user if not presented appropriately. In many instances, what global supply network data are and how they are visualized depend not only on the nature of the data but also on the question that is being asked and ultimately the cognitive abilities of the decision-maker. In order to overcome the aforementioned challenges, supply chain researchers must therefore ensure a balance between detail, abstraction, accuracy, ef<sup>fi</sup>ciency, perceptual tension and esthetics in their visualizations. These observations highlight the importance of setting the context and de<sup>fi</sup>ning the elements in a supply network visualization study very carefully.

We use Gephi, an open-source software for visualizing and analyzing large network graphs to create graphical representations of each supply network of interest [13]. We used a concentric layout approach to create visually appealing and insightful supply network representations. The focal <sup>fi</sup>rm is placed at the center of the visualization while <sup>fi</sup>rms n steps away from the focal <sup>fi</sup>rm are placed on the nth circle. Node size is proportional to the <sup>fi</sup>rm's importance as measured by betweenness centrality. Node color indicates the <sup>fi</sup>rm's distress as measured by its Z-Score and IV. Fig. 1 conceptualizes our visualization approach.

## 4. Results & discussion

We frame the discussion of our results using a micro-to-macro perspective approach. We <sup>fi</sup>rst present results using an illustrative focal <sup>fi</sup>rm in the electronics industry. We then shift our level of analysis to the entire industry. Throughout our discussion, we refer back to the aforementioned risk assessment tasks presented in Table 1.

## 4.1. Firm-level analysis

## 4.1.1. Direct and Tier 1 supply network perspective

Our <sup>fi</sup>rm-level analysis focuses on a major global hardware manufacturer. Fig. 2a–c illustrates the difference when examining only a focal <sup>fi</sup>rm's direct relationships, their ego network, and their ego network with topological and risk information encoded, respectively. Fig. 2a shows the direct connections of the focal <sup>fi</sup>rm. The focal <sup>fi</sup>rm is placed at the center and its connections are shown in a circle, connected by curved relationship edges.<sup>2</sup> Such visualizations would help a decision maker compare the relative supply network size of two or more focal <sup>fi</sup>rms. Often times, however, it is important to understand the nature of collaboration among a focal <sup>fi</sup>rm's supply network partners. These interconnections are shown in Fig. 2b. The ego network of the focal <sup>fi</sup>rm depicts the direct connections of focal <sup>fi</sup>rm and the connections among them. This additional structural insight allows decision makers to evaluate how interconnected, or interrelated, the supply network base is and how resources flow across the ego network The first two <sup>fi</sup>gures, however, are purely topological and do not clearly depict the nature of risk in a focal <sup>fi</sup>rm's Tier-1 supply network. Fig. 2c expands the decision maker's insight by modifying the network through two measures: topological importance (node size) and risk level (node color). We can directly observe that the focal <sup>fi</sup>rm has many low risk <sup>fi</sup>rms (depicted in green), but also several moderate and high-level risk <sup>fi</sup>rms (depicted in orange and red). In addition, it also has no information on the solvency of many <sup>fi</sup>rms in its supply network (depicted in gray). The combination of both topological importance and risk level enables decision makers to understand the distribution of risk in its Tier-1 supply network as well as how well connected or important their suppliers are in the overall network structure. This enables decision makers an ability to focus on particular supply network partners of concern.

![](/api/attachments/KKQDAXY3/fulltext/images/5c30ad0d4ff23ebbdb4ec812441073fabbc41842190faf19348b1afaea0265fd.jpg)  
Fig. 1. A conceptual model of risk visualization in supply networks.

## 4.1.2. Supply network perspective

A Tier-1 perspective of supply chains gives only a partial picture of the supply network and fails to capture the embeddedness of a focal <sup>fi</sup>rm in the broader context. Fig. 3 visualizes the entire Tier-3 supply network of our hardware manufacturer. We can observe that there are many well connected Tier-2 supply chain partners (depicted by node size), many of which are either at a moderate or at a high risk level (depicted by orange and red node colors). Furthermore, we can see that there are a few well-connected partners at the third tier that have a high risk level. This visualization clearly illustrates the importance of the broader context. If only considering the Tier-1 supply network, the subtier risks are missed completely. The whole system visualization also provides an ability to understand the distribution of risk levels across tiers. In this example, we can observe that approximately over half of the <sup>fi</sup>rms are at moderate to high risk. Such a supply network snapshot should consequently raise a concern to the decision maker.

The dense structure of the supply network can be further analyzed for risk distribution patterns. Figs. 4a–d and 5a–d provide risk level <sup>fi</sup>ltered versions of the full supply network. Figs. 4a and 5a illustrate that there is a substantial percentage of <sup>fi</sup>rms in the supply network for which no risk information is available (in our instance, the Z-Score and inventory variability). Many of these <sup>fi</sup>rms are in fact quite well connected. This portrayal may suggest that decision makers should make some effort to identify the risk levels of these <sup>fi</sup>rms proactively. Figs. 4d and 5d show the high risk supply network. This <sup>fi</sup>gure reinforces that while there are only a few well-connected high risk <sup>fi</sup>rms at the <sup>fi</sup>rst tier, many high risk <sup>fi</sup>rms are at the second tier. The ability to <sup>fi</sup>lter the supply network interactively enables decision makers to explore the risk space.

## 4.2. Industry-level analysis

The preceding example of an illustrative focal <sup>fi</sup>rm highlights the value of taking a visual network analytic approach to understand risks in a supply chain. In this section we shift our discussion to the entire electronics industry.

## 4.2.1. Distribution of supply network size

Fig. 6 shows the distribution of network size across each supply network tier. More, speci<sup>fi</sup>cally, Fig. 6a–c depicts the frequency of <sup>fi</sup>rms who can reach k nodes in their supply network when extending the network 1, 2, and 3 tiers out. Each of these graphical depictions helps characterize the structural dispersion and similarities across tiers. Fig. 6a shows the distribution of Tier-1 network sizes, which is also referred to as the degree distribution plot. This degree distribution plot supports the common <sup>fi</sup>nding in literature that real-world networks do not favor a random graph in their degree distributions [70]. Hence, rather than having a Poisson distribution, the degrees of the

![](/api/attachments/KKQDAXY3/fulltext/images/8ea8a0b4639269bdef62fd49020271c3ae08898ded8dea473d4b2372a2edf85f.jpg)

![](/api/attachments/KKQDAXY3/fulltext/images/66db197d395bbfe0bdc641324242472b2d7f3cc43ef2885b2203143b98303a04.jpg)  
(b) Ego Network (EN)

![](/api/attachments/KKQDAXY3/fulltext/images/7a54ac5c0a74b4d613da235cc5928702e7934bc59c71b5cff5d6faf923d23100.jpg)  
Fig, 2. Supply network. (For interpretation of the references to color in this figure the reader is referred to the web version of this article.)

Please cite this article as: R.C. Basole, M.A. Bellamy, Visual analysis of supply network risks: Insights from the electronics industry, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.08.008

![](/api/attachments/KKQDAXY3/fulltext/images/30780244b406ac5dcef6a5e2f7742a6267395c7182d82b5b125bb2a0c4165dcf.jpg)  
(a) Z-Score

![](/api/attachments/KKQDAXY3/fulltext/images/3e28facbd945ef941e891a91b08770e7d0abf7249a2f83eeb5c7b3542219da74.jpg)  
(b) IV

Fig. 3. Three tier supply network of a major hardware manufacturer.  
![](/api/attachments/KKQDAXY3/fulltext/images/6ad69d705698acc2497b1f6cbce2fc70d5e25a4f6d63ea355723e6a8c11eed42.jpg)  
(a) Unknown Risk

![](/api/attachments/KKQDAXY3/fulltext/images/6b04633368302e0c147b13e3a95d7a1be126249b35d81aa483ca65f2317a62db.jpg)

![](/api/attachments/KKQDAXY3/fulltext/images/dc08740bf13976c8225433541d810b8536a2f626141c8fd3b40d799434942249.jpg)  
(c) Moderate Risk

(b) Low Risk  
![](/api/attachments/KKQDAXY3/fulltext/images/8a2b503acf8483fa6cf93f97b973a1b6b83a0405c15d2f1bdd9db0f30e836978.jpg)  
(d) High Risk  
Fig. 4. Supply network <sup>fi</sup>ltered by <sup>fi</sup>nancial risk level (Z-Score).

Please cite this article as: R.C. Basole, M.A. Bellamy, Visual analysis of supply network risks: Insights from the electronics industry, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.08.008

![](/api/attachments/KKQDAXY3/fulltext/images/5658f25cb1c9a5b89ed84e6e51eb3565e9be2381b0003e84a569148c4f48cc26.jpg)  
(a) Unknown Risk

![](/api/attachments/KKQDAXY3/fulltext/images/cbe1d3866f3240d41e7738fa1b070e458f854fa2d0b6dcae510474e1cf551cc7.jpg)  
(b) Low Risk

![](/api/attachments/KKQDAXY3/fulltext/images/503474f18aab0410ae1e1ad992c7cf91d7e3153375956162d64f42622cd3420d.jpg)  
(c) Moderate Risk

![](/api/attachments/KKQDAXY3/fulltext/images/047e6ebbb07d677e630eee5cb16541b0447e56fdeb86c814a725514e67f689fa.jpg)  
(d) High Risk  
Fig. 5. Supply network <sup>fi</sup>ltered by operational risk level (IV).

<sup>fi</sup>rms in the supply network are highly skewed, as evidenced in the long tail of values as the plot approaches the zero-degree line.

Fig. 6b, depicting the frequency of Tier-2 network sizes for all <sup>fi</sup>rms, has the most structurally ambiguous distribution, though there is a visible spike in frequency of <sup>fi</sup>rms with network sizes 100–250. Similar to the distribution of Tier-1 network sizes in Fig. 6a, the frequency of Tier-3 network sizes in Fig. 6c clearly has a right-skewed distribution. In particular, the long tail of values shifts from the left-hand side in Fig. 6a to the right-hand side, with more of an exponential rise as the plot approaches the maximum network size of 911. It is also interesting to note that

![](/api/attachments/KKQDAXY3/fulltext/images/453447293a417da8e8762602e74c4ed4a1f8979e360e8e03ae1ed5a73b4b71b5.jpg)  
(a) Tier 1

![](/api/attachments/KKQDAXY3/fulltext/images/6ce5063d0d85aa26fe4657c25d74f5ef89c94f0bc7cf07569c6c49d108ed823d.jpg)  
(b) Tier 2

![](/api/attachments/KKQDAXY3/fulltext/images/695bc7a65d40f24e44b39de49f7f5d63229290c024ee10cbedd17e620434cf30.jpg)  
(c) Tier 3  
Fig. 6. Network size distribution by tier.

Please cite this article as: R.C. Basole, M.A. Bellamy, Visual analysis of supply network risks: Insights from the electronics industry, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.08.008

<sup>fi</sup>rms are dispersed across a much smaller number of possible network sizes in Tier 1 (99 unique frequency groups), much higher number in Tier 2 (490 unique frequency groups), and near the middle of the two in Tier 3 (243 unique frequency groups). Lastly, by viewing the density plots of each tier in Fig. 7, we can see further evidence of the leftskewed, bell-shape, and right-skewed behavior of network size distributions at Tiers 1, 2, and 3, respectively.

## 4.2.2. Distribution of risk

Fig. 8 shows the density plots of the average supply network partner Z-Score and IV, respectively by tier. Two interesting observations can be made. First, the average Z-Score and IV decreases as you move further away from the focal <sup>fi</sup>rm, suggesting that, on average, lower tier suppliers are in higher <sup>fi</sup>nancial distress. Second, the variance of Z-Scores and IV is substantially higher in the <sup>fi</sup>rst tier as compared to Tier-2 and Tier-3 partners. The results highlight that subtier risks are quite prevalent in supply networks in the electronics industry and distributions differ by tier. At the same time, it also highlights that even direct supply network connections can be a signi<sup>fi</sup>cant source of risks.

Fig. 9a–c and d–f examines the distribution of risk as a function of the focal <sup>fi</sup>rm's direct connections (i.e. degree) by tier level.

## 4.2.3. Impact of visibility level

Fig. 10 shows the degree of visibility afforded by additional tiers of insight by a focal <sup>fi</sup>rm's Tier-1 supply network size. The <sup>fi</sup>rst observation is that visibility using only Tier-1 supply network partners ranges from 1–20%. The level of visibility increases as the size of the Tier-1 supply network increases. The results also show that with the addition of only one tier, the total visibility into the supply network increases substantially, between 25–85%. If all three tiers are taken into consideration, 100% visibility is achieved.

Together, these results further underline that each additional tier can provide substantial insight into the overall supply network. However, there are some diminishing returns. Achieving full Tier-3 insight may be desirable, but not necessary or even economically bene<sup>fi</sup>cial. The cost of achieving full insight could be substantial, requiring signi<sup>fi</sup>cant resources.

## 4.3. Summary of risk assessment tasks

The preceding discussion underlines the value of our visual approach with respect to the risk assessment tasks identi<sup>fi</sup>ed in Table 1. Below is a summary of our approach and <sup>fi</sup>ndings for tasks at the <sup>fi</sup>rm (T1–T5) and the network level (T6–T9).

• (T1) Identify the most influential partner(s) in the supply network. Veri<sup>fi</sup>cation can come from both quantitative and visual analyses.

![](/api/attachments/KKQDAXY3/fulltext/images/ba1a314fcce62e246472e43957e78e4ccf2cb38b7931ba949d5aadbc691e42ef.jpg)  
Fig. 7. Network size density plots.

First, the decision maker can rank partners by betweenness centrality scores, as these scores help re<sup>fl</sup>ect the amount of in<sup>fl</sup>uence each partner has over other partners in the supply network. Second, the concentric layout visualizations in Fig. 2b and c shed light on the importance and patterns of relationships that shape each partner's level of in<sup>fl</sup>u ence in the network.

• (T2) Determine the patterns of interaction between shared partners, first tier and beyond. Veri<sup>fi</sup>cation can be better served by visual analysis. For example, Fig. 3 reveals a high proportion of partners who are well connected to each other at Tier-2 (depicted by node size), but a relatively low level of interconnectedness among Tier-1 partners.

• (T3) Identify partner(s) whose removal would result in the disruption of the supply network. Veri<sup>fi</sup>cation can come partly from identifying partners with both a high betweenness centrality and a low risk level (refer to Figs. 3 and 4), as these partners are both in<sup>fl</sup>uential and are expected to be less likely to spread negative risk to other partners in the supply network. However, structurally in<sup>fl</sup>uential partners with unknown risk levels should also be identi<sup>fi</sup>ed and further assessed, as the potential positive or negative risk in<sup>fl</sup>uence is more ambiguous.

• (T4) Identify direct and sub-tier partners with high levels of risk. Veri<sup>fi</sup>- cation can come partly from identifying partners with both a high betweenness centrality and a high risk level (refer to Figs. 3 and 4), as these partners are both in<sup>fl</sup>uential and are expected to be more likely to spread negative risk to other partners in the supply network. As in the previous question, care should also be taken to structurally in<sup>fl</sup>uential partners with unknown risk levels due to their greater risk ambiguity.

• (T5) Determine the risk concentration across each tier. Veri<sup>fi</sup>cation can come from comparing Tier-3 supply networks <sup>fi</sup>ltered by risk level, using visuals such as those depicted in Fig. 4. As evidenced by the <sup>fi</sup>gure, decision makers can get a sense not only of concentration of risk across each supply network tier, but also of which risk levels also have the largest share of in<sup>fl</sup>uential partners.

• (T6) Describe the overall structure of the supply network. Veri<sup>fi</sup>cation can come from comparison of network size distributions across tiers (Fig. 5) and network size density plots (Fig. 6).

• (T7) Identify how risk is distributed across the supply network. Veri<sup>fi</sup>cation can come from comparison of risk density plots (such as Z-Score and IV comparisons in Fig. 7).

• (T8) Determine the variation in risk by tier and by number of direct partners. Veri<sup>fi</sup>cation can come from comparison of risk to degree plots, at each tier level (such as Z-Score and inventory variability comparisons in Fig. 8).

• (T9) Determine the variation in supply network visibility by tier and by number of direct partners. Veri<sup>fi</sup>cation can come from comparison of visibility to degree plots, at each tier level (such as the visibility comparisons in Fig. 9).

## 5. Conclusions

Risk identi<sup>fi</sup>cation, analysis, and mitigation has unquestionably become an important topic in supply chain management research. A network perspective provides a powerful way to systemically understand the complex supply network dependencies and <sup>fl</sup>ows. Our empirical study demonstrates that the fusion of network analysis and information visualization represents a particularly valuable methodological approach that can enhance decision makers' ability to identify and manage risks in supply networks. We illustrate our approach with visualization examples from the electronics industry.

Our study has several important implications for both supply chain researchers and practitioners. First, we emphasize the importance of developing (new) supply network intelligence capabilities. Supply networks are becoming increasingly global and complex. Identi<sup>fi</sup>cation and management of risks and opportunities is increasingly challenging. Most <sup>fi</sup>rms have only very little visibility into their supply network beyond the <sup>fi</sup>rst tier. Our study shows that visualization can provide

Please cite this article as: R.C. Basole, M.A. Bellamy, Visual analysis of supply network risks: Insights from the electronics industry, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.08.008

![](/api/attachments/KKQDAXY3/fulltext/images/c191d42650157f16f64065e54116121e62c12f30c1479e0823fc2841d4aa252b.jpg)  
(a) Z-Score Density Plots

![](/api/attachments/KKQDAXY3/fulltext/images/f4be809290638b201379a6b22548654657f3ee18facf38c8d1ebd3dfa36a207e.jpg)  
b) IV Density Plots  
Fig. 8. Density plots.

systemic insight into the competitive and collaborative network structure. Visualization combined with analytics leads to an important supply network capability that allows mapping of <sup>fi</sup>rms, <sup>fl</sup>ow, information, and risk. Integrating these diagrammatic representations and developing custom views – such as heatmaps of collaboration intensity – with enterprise information systems, and the creation of new risk metrics – such as heatmaps of supplier risk intensity – will enable timely identi<sup>fi</sup>- cation of peripheral activities and risks in the supply network. Further, they will help shed light on the critical roles and linkages that previously would have been left unnoticed. At the same time, it provides insight into the competitive strategies other <sup>fi</sup>rms are pursuing. We believe that the approach presented in this study is a <sup>fi</sup>rst step toward the development of novel and critical supply network risk intelligence capabilities.

Second, we advance our understanding of decision support tools and supply chain theory through network analysis and visualization. While it is well-established that relationships and networks are core aspects of today's global business environment and have been studied extensively in strategy and organizational behavior, the supply chain community is only beginning to apply a social network analysis lens and visualization to study salient issues. Our research thus contributes to the supply chain community and to the current pool of decision support models, by presenting a new empirical approach (network analysis and visualization) that provides a macroscopic view and enables the study of risk issues that shape supply networks across multiple tiers.

Lastly, decision support tools and dashboards only augment supply chain decision making. Decision makers must use these tools to help them continuously monitor, cultivate, and manage effective supply network relationships. There is an increasing recognition that the shift from simple transactional and contractual-based relationships to more long-term relational forms of collaboration between supply network partners can lead to many bene<sup>fi</sup>cial outcomes including the reduction of risks [48]. However, it also requires the right combination of “sticks and carrots” that encourage, incentivize, and empower a focal <sup>fi</sup>rm's partners to meet its desired high operational standards. In order to build the ability to learn of and mitigate risks in the supply network, managers should cultivate a collaborative philosophy with a focus on leveraging the strength of the supply network and must continually scan their supply networks for value creation potential from the capacities and capabilities of each partner [32]. In times where resources are limited and decision makers' attention must be focused, a visual structural analysis, as presented in this study, can quickly help identify (potentially new) partners that provide access to resources, ideas, and information and streamline their supply chain base to help them maximize opportunities while mitigating impending risks.

![](/api/attachments/KKQDAXY3/fulltext/images/ce2514c5733551657057465e39018df31220a950a76481df0b3bef4e1df57381.jpg)  
(a) Tier 1

![](/api/attachments/KKQDAXY3/fulltext/images/306980dcfc26344038d701568703db6ae0a937b348f6e1eda0a57a944ad39fc3.jpg)

![](/api/attachments/KKQDAXY3/fulltext/images/6658487a8f9461b343f9e157119288d5215fe4d4a5ba8761d4357b28f20a565e.jpg)  
(b) Tier 2  
(c) Tier 3

![](/api/attachments/KKQDAXY3/fulltext/images/4cf4cb81cf70f0cbed582eb6f297ed9176add7718b38d54bd182a8b6f5ba2de8.jpg)  
(d) Tier 1

![](/api/attachments/KKQDAXY3/fulltext/images/5f0cecf035a61681500dee22f35afe201c1935ebd53d63e9aad724bb405f7c9d.jpg)  
(e) Tier 2

![](/api/attachments/KKQDAXY3/fulltext/images/6fe6b0449ce8f1ab9e07db7e06aea6dd282ece2b21dda07026f903fa9303170e.jpg)  
(f) Tier 3  
Fig. 9. Risk vs. degree.  
Please cite this article as: R.C. Basole, M.A. Bellamy, Visual analysis of supply network risks: Insights from the electronics industry, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.08.008

![](/api/attachments/KKQDAXY3/fulltext/images/e284ae1c2c156c41356192da1f7be1193dd797cb122fdfd3c2faccb449cff8e1.jpg)  
Fig. 10. Visibility at each tier vs. degree.

Our study is not without limitations. As with any empirical study, the accuracy of our results is dependent on the quality of our data. To this extent, we have taken every precaution to validate both the structural and risk data. Additional data sources could help triangulate the validity of our data. We also acknowledge that we only present two types of risks – the Z-Score and IV – in our analysis. While we believe that these two are representative risk types, there are clearly many others. Future work should incorporate several different risk types and explore how to best visualize composite as well as continuous risks. Visual differentiation between upstream and downstream supply network <sup>fi</sup>rms – perhaps through alternate shape encodings or layout algorithms – would also be valuable. Lastly, the power of visualization really comes from being able to “play” with the data and networks interactively. In our study we merely provided static snapshots. Future work should evaluate alternative designs of interactive tools and empirically evaluate them through a <sup>fi</sup>eld study with actual decision makers. Each of these limitations presents exciting opportunities for future research.

## Appendix A. Risks

Table A.1 provides a de<sup>fi</sup>nition for several of the broad risk areas as well as a set of representative measures pertaining to each area. Other noteworthy studies have done an extensive surveying of performance measures and metrics in logistics and supply chain management, with a heavy emphasis on process-based operational and some <sup>fi</sup>nancial measures [37,87]. Many enterprises may have already developed in-house key performance indicators (KPIs) for their global supply networks; others may have to be developed. In general, a comprehensive assessment of all four areas requires both primary and secondary data collection, especially for the collaborative- and strategic-based measures, and interconnected enterprise information systems. A variety of common operational, <sup>fi</sup>nancial, collaborative, and strategic risk metrics can be supplemented using existing public and commercial databases such as Compustat (e.g. [65]) and Thomson Reuters SDC Platinum (e.g. [82]).

## Table A.1

Summary of risk metrics (O = Operational; F = Financial; C = Collaboration; I = Information; ST = Strategic; D = Demand; S = Supply).

<table><tr><td>Category</td><td>Example</td><td>References</td></tr><tr><td>Delivery performance $^{O,S}$ </td><td>On-time receipt of parts/servicesDelivery ratings</td><td>[27,31,63,80]</td></tr><tr><td>Dependency/ redundancy $^{O,S}$ </td><td>Extent of supplier dependencyExtent of supplier redundancy</td><td>[28,30,53]</td></tr><tr><td>Mfg. performance $^{O,S}$ </td><td>Scheduled vs. actual production/cycle timeProductivityLead time</td><td>[22,31,63,64,88]</td></tr><tr><td>Costs $^{D,O,S}$ </td><td>InventoryProductionTransportation and handlingTransaction-based</td><td>[59,67]</td></tr><tr><td>Quality $^{D,O,S}$ </td><td>Processes/products meeting customer reqs.Quality ratings</td><td>[19,22,35,63,80]</td></tr><tr><td>Flexibility $^{D,O}$ </td><td>Cost-effective ability to meet customer reqs.Ability to recover from external shocks</td><td>[22,59,63,64,83]</td></tr><tr><td>Sustainability $^{D,F}$ </td><td>Solvency (e.g. Z-Score model)Return on assets (ROA)LiquidityMarket share</td><td>[2,31,60,64,65]</td></tr><tr><td>Growth $^{D,F}$ </td><td>Asset build-upSolvency growth rate</td><td>[31,60]</td></tr><tr><td>Information sharing $^{C,I,S}$ </td><td>Extent of shared information between partnersKnowledge transferDegree of IT integration with partners</td><td>[28,30,53,97,110]</td></tr><tr><td>Decision synchronization $^{C,D,S}$ </td><td>Degree of decision synchronization with partners</td><td>[21,95,110]</td></tr><tr><td>Incentive alignment $^{C,D,S,ST}$ </td><td>Degree of incentive alignment with partners</td><td>[80,97]</td></tr><tr><td>Strategic alliance $^{C,S,ST}$ </td><td>Alliance formationAlliance partner diversityAlliance geographic diversity</td><td>[36,58,68,82]</td></tr><tr><td>Leadership $^{S,ST}$ </td><td>Change communication, management, executionAvailability/measurement of change processesInternal/external alignmentCultureTrust</td><td>[28,53,101,103]</td></tr></table>

## References

[1] E.M. Airoldi, X. Bai, K.M. Carley, Network sampling and classi<sup>fi</sup>cation: an investigation of network model representations, Decision Support Systems 51 (2011) 506–518.

[2] E.I. Altman, Financial ratios, discriminant analysis and the prediction of corporate bankruptcy, The Journal of Finance 23 (1968) 589–609.

[3] V. Babich, A. Burnetas, P. Ritchken, Competition and diversi<sup>fi</sup>cation effects in supply chains with supplier default risk, Manufacturing & Service Operations Management 9 (2007) 123–146.

[4] A. Bajaj, R. Russell, Awsm: allocation of work<sup>fl</sup>ows utilizing social network metrics, Decision Support Systems 50 (2010) 191–202.

[5] R.C. Basole, Visualization of inter<sup>fi</sup>rm relations in a converging mobile ecosystem, Journal of Information Technology 24 (2009) 144–159.

[6] R.C. Basole, Visual Business Ecosystem Intelligence: Lessons from the Field, Computer Graphics and Applications, IEEE 34 (5) (2014) 26–34.

[7] R.C. Basole, M. Bellamy, Global supply network health: Analysis and visualization, Global Supply Network Health: Analysis and Visualization. Tennenbaum Institute Series on Enterprise SystemsIOS Press, Amsterdam. 2012

[8] R.C. Basole, T. Clear, M. Hu, H. Mehrotra, J. Stasko, Understanding inter<sup>fi</sup>rm relationships in business ecosystems with interactive visualization, IEEE Transactions on Visualization and Computer Graphics 19 (2013) 2526–2535.

[9] R.C. Basole, S. Ghosh, M. Hora, Association between Supply Networks Properties and Performance: Evidence from the Electronics Industry, Working Paper2013.

[10] R.C. Basole, M. Hu, P. Patel, J.T. Stasko, Visual analytics for converging-businessecosystem intelligence, IEEE Computer Graphics and Applications 32 (2012) 92–96.

[11] R.C. Basole, J. Karla, On the evolution of mobile platform ecosystem structure and strategy, Business & Information Systems Engineering 3 (2011) 1–10.

[12]. R.C. Basole W.B. Rouse Complexity of service value networks: conceptualization and empirical investigation IBM Systems Journal 47 (2008) 53–70

[13] M. Bastian, S. Heymann, M. Jacomy, Gephi: An open source software for exploring and manipulating networks, International AAAI conference on Weblogs and Social Media 2009.

[14] G.D. Battista, P. Eades, R. Tamassia, I.G. Tollis, Algorithms for drawing graphs: an annotated bibliography, Computational Geometry 4 (1994) 235–282.

[15] M. Bellamy, R.C. Basole, Network analysis of supply chain systems: a systematic review and future research, Systems Engineering 16 (2013) 235–249.

[16] N. Bennett, W. Kessler, L. McGinnis, Enterprise Transformation and Manufacturing in a Global Enterprise, Volume 5 of Tennenbaum Institute Series on Enterprise Systems, IOS Press, Amsterdam, 2012.

[17] C. Blome, T. Schoenherr, Supply chain risk management in <sup>fi</sup>nancial crises—a multiple case-study approach, International Journal of Production Economics 134 (2011) 43–57.

[18] S.P. Borgatti, X. Li, On social network analysis in a supply chain context, Journal of Supply Chain Management 45 (2009) 5–22.

[19] J.L. Bower, T.M. Hout, Fast cycle capability for competitive power, Harvard Business Review 66 (1988) 110–118.

[20] C. Buhman, S. Kekre, J. Singhal, Interdisciplinary and interorganizational research: establishing the science of enterprise networks, Production & Operations Management 14 (2005) 493–513.

[21] A. Carr, J. Pearson, Strategically managed buyer–supplier relationships and performance outcomes, Journal of Operations Management 17 (1999) 497–519.

[22] F.T.S. Chan, Performance measurement in a supply chain, The International Journal of Advanced Manufacturing Technology 21 (2003) 534–548.

[23] J. Cho, B. Kang, Bene<sup>fi</sup>ts and challenges of global sourcing: perceptions of US apparel retail <sup>fi</sup>rms, International Marketing Review 18 (2001) 542–561.

[24] T.Y. Choi, K.J. Dooley, M. Rungtusanatham, Supply networks and complex adaptive systems: control versus emergence, Journal of Operations Management 19 (2001) 351–366.

[25] T.Y. Choi, D.R. Krause, The supply base and its complexity: implications for transaction costs, risks, responsiveness, and innovation, Journal of Operations Management 24 (2006) 637–652.

[26] S. Chopra, M.S. Sodhi, Managing risk to avoid supply-chain breakdown, MIT Sloan Management Review 46 (2004) 53–62.

[27] G. Cleveland, R.G. Schroeder, J.C. Anderson, A theory of production competence, Decision Sciences 20 (1989) 655–668.

[28] D. Corsten, T. Gruen, M. Peyinghaus, The effects of supplier-to-buyer identi<sup>fi</sup>cation on operational performance—an empirical investigation of inter-organizational identi<sup>fi</sup>cation in automotive relationships, Journal of Operations Management 29 (2011) 549–560.

[29] H. Courtney, D. Lovallo, C. Clarke, Deciding how to decide, Harvard Business Review 91 (2013) (62–+).

[30] P.D. Cousins, B. Menguc, The implications of socialization and integration in supply chain management, Journal of Operations Management 24 (2006) 604–620.

[31] J.R. Evans, An exploratory study of performance measurement systems and relationships with performance results, Journal of Operations Management 22 (2004) 219–232.

[32] S.E. Fawcett, S.L. Jones, A.M. Fawcett, Supply chain trust: the catalyst for collaborative innovation, Business Horizons 55 (2012) 163–178.

[33] C. Fine, Clockspeed-based strategies for supply chain design, Production and Operations Management 9 (2000) 213–221.

[34] L. Freeman, Centrality in social networks conceptual clari<sup>fi</sup>cation, Social Networks 1 (1979) 215–239

[35] R.R. Fullerton, C.S. McWatters, C. Fawson, An examination of the relationships between JIT and <sup>fi</sup>nancial performance, Journal of Operations Management 21 (2003) 383–404.

[36] R. Gulati, Alliances and networks, Strategic Management Journal 19 (1998) 293317.

[37] A. Gunasekaran, B. Kobu, Performance measures and metrics in logistics and supply chain management: a review of recent literature (1995–2004) for research and applications, International Journal of Production Research 45 (2007) 2819-2840.

[38] J. Hallikas, I. Karvonen, U. Pulkkinen, V.M. Virolainen, M. Tuominen, Risk management processes in supplier networks, International Journal of Production Economics 90 (2004) 47–58.

[39] G. Hamel, Y. Doz, C. Prahalad, Collaborate with your competitors and win, Harvard Business Review 67 (1989) 133–139.

[40] R.B. Hand<sup>fi</sup>eld, E.L. Nichols, Supply Chain Redesign: Transforming Supply Chains into Integrated Value Systems, FT Press, 2002.

[41] C. Harland, R. Brenchley, H. Walker, Risk in supply networks, Journal of Purchasing and Supply Management 9 (2003) 51–62.

[42] K. Hendricks, V. Singhal, An empirical analysis of the effect of supply chain disruptions on long-run stock price performance and equity risk of the <sup>fi</sup>rm, Production and Operations Management 14 (2009) 35–52.

[43] Z. Hua, Y. Sun, X. Xu, Operational causes of bankruptcy propagation in supply chain, Decision Support Systems 51 (2011) 671–681.

[44] A. Huchzermeier, M. Cohen, Valuing operational <sup>fl</sup>exibility under exchange rate risk, Operations Research 44 (1996) 100–113

[45] M. Iansiti, R. Levien, The Keystone Advantage: What New Dynamics of Business Ecosystems Mean for Strategy Innovation, and Sustainability, Harvard Business School Press Boston 2004

[46] B. Iyer, C.H. Lee, N. Venkatraman, Managing in a “small world ecosystem”: lessons from the software sector. California Management Review 48 (2006) 28–47.

[47] M. Johnson, Learning from toys: lessons in managing supply chain risk from the toy industry, California Management Review 43 (2001) 106–124.

[48] M. Kalwani, N. Narayandas, Long-term manufacturer–supplier relationships: do they pay off for supplier <sup>fi</sup>rms? Journal of Marketing 59 (1995) 1–16.

[49] M. Keith, H. Demirkan, M. Goul, The in<sup>fl</sup>uence of collaborative technology knowledge on advice network structures, Decision Support Systems 50 (2010) 140–151.

[50] Y. Kim, T.Y. Choi, T. Yan, K. Dooley, Structural investigation of supply networks: a social network analysis approach, Journal of Operations Management 29 (2011) 194–211.

[51] C. Kiss, M. Bichler, Identi<sup>fi</sup>cation of in<sup>fl</sup>uencers—measuring in<sup>fl</sup>uence in customer networks, Decision Support Systems 46 (2008) 233–253.

[52] P.R. Kleindorfer, G.H. Saad, Managing disruption risks in supply chains, Production and Operations Management 14 (2005) 53–68.

[53] D.R. Krause, R.B. Hand<sup>fi</sup>eld, B.B. Tyler, The relationships between supplier development, commitment, social capital accumulation and performance improvement, Journal of Operations Management 25 (2007) 528–545.

[54] C.J. Kuhlman, V.A. Kumar, M.V. Marathe, S. Ravi, D.J. Rosenkrantz, Finding Critical Nodes for Inhibiting Diffusion of Complex Contagions in Social Networks, Machine Learning and Knowledge Discovery in Databases, Springer, 2010. 111–127.

[55] A. Latour, Trial by <sup>fi</sup>re: a blaze in Albuquerque sets off major crisis for cell-phone giants, Wall Street Journal 1 (2001) 2001.

[56] O. Lavastre, A. Gunasekaran, A. Spalanzani, Supply chain risk management in French companies, Decision Support Systems 52 (2012) 828–838.

[57] H. Lee, The triple—a supply chain, Harvard Business Review 82 (2004) 102–112.

[58] Y. Li, Y. Liu, M. Li, H. Wu, Transformational offshore outsourcing: empirical evidence from alliances in China, Journal of Operations Management 26 (2008) 257–274.

[59] Y. Liao, P. Hong, S.S. Rao, Supply management, supply <sup>fl</sup>exibility and performance outcomes: an empirical investigation of manufacturing <sup>fi</sup>rms, Journal of Supply Chain Management 46 (2010) 6–22.

[60] R. Lynch, K. Cross, Measure Up!: Yardsticks for Continuous Improvement, 2nd ed. Blackwell Business, Cambridge, MA, 1995.

[61] I. Manuj, J. Mentzer, Global supply chain risk management, Journal of Business Logistics 29 (2008) 133–155.

[62] A. Marucheck, N. Greis, C. Mena, L. Cai, Product safety and security in the global supply chain: issues, challenges and research opportunities, Journal of Operations Management 29 (2011) 707–720.

[63] B.H. Maskell, Performance Measurement for World Class Manufacturing: a Model for American Companies, Productivity Press, Portland, OR, 1991.

[64] Y.Z. Mehrjerdi, Excellent supply chain management, Assembly Automation 29 (2009) 52–60.

[65] S.B. Modi, S. Mishra, What drives <sup>fi</sup>nancial performance—resource ef<sup>fi</sup>ciency or resource slack?: evidence from US. based manufacturing firms from 1991 to 2006, Journal of Operations Management 29 (2011) 254–273.

[66] A. Nair, J.M. Vidal, Supply network topology and robustness against disruptions — an investigation using multi-agent model, International Journal of Production Research 49 (2010) 1391–1404.

[67] R. Narasimhan, A. Das, The impact of purchasing integration and practices on manufacturing performance, Journal of Operations Management 19 (2001) 593–609.

[68] R. Narasimhan, A. Nair, The antecedent role of quality, information sharing and supply chain proximity on strategic alliance formation and performance, International Journal of Production Economics 96 (2005) 301–313.

[69] M. Newman, S. Strogatz, D. Watts, Random graphs with arbitrary degree distributions and their applications, Physical Review E 64 (2000).

[70] M.E.J. Newman, The structure and function of complex networks, SIAM Review 45 (2003) 167-167.

[71] A. Norrman, U. Jansson, Ericsson's proactive supply chain risk management approach after a serious sub-supplier accident, International Iournal of Physical Distribution & Logistics Management 34 (2004) 434–456.

[72] A. Oke, M. Idiagbon-Oke, Communication channels, innovation tasks and NPD project outcomes in innovation-driven horizontal networks, Journal of Operations Management 28 (2010) 442–453.

[73] A. Oke, M. Idiagbon-Oke, F. Walumbwa, The relationship between brokers' in<sup>fl</sup>uence, strength of ties and NPD project outcomes in innovation-driven horizontal networks, Journal of Operations Management 26 (2008) 571–589.

[74] S.D. Pathak, D.M. Dilts, S. Mahadevan, Investigating population and topological evolution in a complex adaptive supply network, Journal of Supply Chain Management 45 (2009) 54–57.

[75] A. Perer, B. Shneiderman, Balancing systematic and <sup>fl</sup>exible exploration of social networks, Visualization and Computer Graphics, IEEE Transactions on 12 (2006) 693–700.

[76] W.W. Powell, D.R. White, K.W. Koput, J. Owen-Smith, Network dynamics and <sup>fi</sup>eld evolution: the growth of interorganizational collaboration in the life sciences, American Journal of Sociology 110 (2005) 1132–1205.

[77] H. Purchase, Which aesthetic has the greatest effect on human understanding, Graph Drawing, Springer, 1998, pp. 248–261.

[78] L. Rosenkopf, G. Padula, Investigating the microstructure of network evolution: alliance formation in the mobile communications industry, Organization Science 19 (2008) 669–687.

[79] L. Rosenkopf, M.A. Schilling, Comparing alliance network structure across industries: observations and explanations Strategic Entrepreneurship Journal 1 (2008) 191–209

[80] A.D. Ross, F.P. Buffa, C. Droge, D. Carrington, Using buyer–supplier performance frontiers to manage relationship performance Decision Sciences 40 (2009) 37–64

[81] W.B. Rouse, Enterprises as systems: essential challenges and approaches to transformation, Systems Engineering 8 (2005) 138–150.

[82] M.A. Schilling, C.C. Phelps, Inter<sup>fi</sup>rm collaboration networks: the impact of largescale network structure on <sup>fi</sup>rm innovation, Management Science 53 (2007) 1113–1126.

[83] R.W. Schmenner, International factory productivity gains, Journal of Operations Management 10 (1991) 229–254.

[84] R.W. Schmenner, M.L. Swink, On theory in operations management, Journal of Operations Management 17 (1998) 97–113.

[85] H. Schrdl, K. Turowski, Risk management in hybrid value creation, Decision Support Systems (2014) forthcoming.

[86] Y. Shef<sup>fi</sup>, Supply chain management under the threat of international terrorism, The International Journal of Logistics Management 12 (2001) 1–11.

[87] C. Shepherd, H. Günter, Measuring supply chain performance: current research and future directions, International Journal of Productivity and Performance Management 55 (2006) 242–258.

[88] H. Shin, D.A. Collier, D.D. Wilson, Supply management orientation and supplier/ buyer performance, Journal of Operations Management 18 (2000) 317–333.

[89] N. Shin, K. Kraemer, J. Dedrick, R&D, value chain location and <sup>fi</sup>rm performance in the global electronics industry, Industry and Innovation 16 (2009) 315–330.

[90] G. Stevens, Integrating the supply chain, International Journal of Physical Distribution & Logistics Management 19 (1989) 3–8.

[91] A. Surana, S. Kumara, M. Greaves, U.N. Raghavan, Supply-chain networks: a complex adaptive systems perspective, International Journal of Production Research 43 (2005) 4235–4265.

[92] C. Tang, B. Tomlin, The power of <sup>fl</sup>exibility for mitigating supply chain risks, International Journal of Production Economics 116 (20o8) 12–27

[93] C.S. Tang, J.D. Zimmerman, J.I. Nelson, Managing new product development and supply chain risks: the Boeing 787 case, Supply Chain Forum: an International Journal 10 (2009) 74–86.

[94] O. Tang, S. Nurmaya Musa, Identifying risk issues and research advancements in supply chain risk management, International Journal of Production Economics 133 (2011) 25–34.

[95] D.J. Thomas, P.M. Grif<sup>fi</sup>n, Coordinated supply chain management, European Journal of Operational Research 94 (1996) 1–15.

[96] J.H. Thun, D. Hoenig, An empirical analysis of supply chain risk management in the German automotive industry, International Journal of Production Economics 131 (2011) 242–249.

[97] A. De Toni, G. Nissimbeni, S. Tonchia, New trends in supply environment, Logistics Information Management 4 (1994) 41–50.

[98] P. Trkman, K. McCormack, Supply chain risk in turbulent environments—a conceptual model for managing supply chain network risk, International Journal of Production Economics 119 (2009) 247–258.

[99] E. Tufte, The Visual Display of Quantitative Information, Graphics Press, Cheshire, 1983.

[100] E. Tufte, Envisioning Information, Graphics Press, Cheshire, 1990.

[101] S. Vachon, A. Halley, M. Beaulieu, Aligning competitive priorities in the supply chain: the role of interactions with suppliers, International Journal of Operations & Production Management 29 (2009) 322–340.

[102] J.P.P. Vilko, J.M. Hallikas, Risk assessment in multimodal supply chains, International Journal of Production Economics 140 (2011) 586–595.

[103] V.H. Villena, E. Revilla, T.Y. Choi, The dark side of buyer–supplier relationships: a social capital perspective, Journal of Operations Management 29 (2011) 561–576.

[104] S.M. Wagner, C. Bode, P. Koziol, Supplier default dependencies: empirical evidence from the automotive industry, European Journal of Operational Research 199 (2009) 150–161.

[105] S.M. Wagner, N. Neshat, Assessing the vulnerability of supply chains using graph theory, International Journal of Production Economics 126 (2010) 121–129.

[106] C. Ware, H. Purchase, L. Colpoys, M. McGill, Cognitive measurements of graph aesthetics, Information Visualization 1 (2002) 103–110.

[107] D. Watts, Networks, dynamics, and the small-world phenomenon, American Journal of Sociology 105 (1999) 493–527.

[108] H. Wei, M. Dong, S. Sun, Inoperability input–output modeling (IIM) of disruptions to supply chain networks, Systems Engineering 13 (2010) 324–339.

[109] H. Yli-Renko, E. Autio, H. Sapienza, Social capital, knowledge acquisition, and knowledge exploitation in young technology-based <sup>fi</sup>rms, Strategic Management Journal 22 (2001) 587–613.

[110] Z.G. Zacharia, N.W. Nix, R.F. Lusch, Capabilities that enhance outcomes of an episodic supply chain collaboration, Journal of Operations Management 29 (2011) 591–603.

[111] G. Zsidisin, L. Ellram, J. Carter, J. Cavinato, An analysis of supply risk assessment techniques, International Journal of Physical Distribution & Logistics Management 34 (2004) 397–413.

Rahul C. Basole is an Associate Professor in the School of Interactive Computing, the Associate Director for Enterprise Transformation in the Tennenbaum Institute/IPaT, and an af<sup>fi</sup>liated faculty member in the GVU Center at the Georgia Institute of Technology. He is also a Visiting Scholar in HSTAR at Stanford University. His research and teaching focuses on computational enterprise science, information visualization, and strategic decision support. His work has received numerous best paper awards and he has extensively published in leading computer science, management, and engineering journals. He received a B.S. degree in industrial and systems engineering from Virginia Tech, has completed graduate studies in engineering-economic systems, operations research, and management information systems at Stanford University and the University of Michigan, and received a Ph.D. degree in industrial and systems engineering from the Georgia Institute of Technology.

Marcus A. Bellamy is a Ph.D. candidate of Operations Management in the Scheller College of Business at the Georgia Institute of Technology. He is also a Graduate Fellow in the Tennenbaum Institute. His research interests include supply chain management, empirical operations management, supply chains and innovation, risk management and mitigation, and inter-organizational networks. Marcus received his M.S. in Industrial Engineering at Georgia Tech, his B.S. in Mechanical Engineering at the University of New Mexico, and was also a Fulbright scholar for a teaching and researching position in Madrid, Spain. He is a member of the Academy of Management (AOM), Institute for Operations Research and Management Science (INFORMS) and Production and Operations Management (POMS).
