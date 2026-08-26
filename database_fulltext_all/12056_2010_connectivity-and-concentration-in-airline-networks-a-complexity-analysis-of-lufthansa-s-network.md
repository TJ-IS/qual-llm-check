---
otero_id: 12056
otero_key: "SRG9BXYA"
title: "Connectivity and concentration in airline networks: a complexity analysis of Lufthansa's network"
authors: "Aura Reggiani; Peter Nijkamp; Alessandro Cento"
year: "2010"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.2010.11"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Connectivity and concentration in airline networks: a complexity analysis of Lufthansa’s network

Aura Reggiani<sup>1</sup> Peter Nijkamp<sup>2</sup> and Alessandro Cento<sup>3</sup>

<sup>1</sup>Department of Economics, University of Bologna, Italy; <sup>2</sup>Department of Spatial Economics, VU University Amsterdam, the Netherlands; <sup>3</sup>KLM Royal Dutch Airlines, Milan, Italy.

Correspondence: Aura Reggiani, Department of Economics, University of Bologna, Piazza Scaravilli, 2, Bologna 40126, Italy. Fax: 390512098143; E-mail: aura.reggiani@unibo.it

## Abstract

Information, communication and transport networks have always been in a state of flux, while they also influence each other. Extensive research efforts have been made to investigate the dynamics in the structure and use of networks, for example, by means of network geometries, Small-World effects and Scale-Free phenomena. We will illustrate these new developments on the basis of airline network evolution. Using Lufthansa’s networks as an example, this paper aims to show the empirical relevance of various network indicators – such as connectivity and concentration – for understanding changing patterns in airline network configurations. After an extensive discussion of various statistical results, a decision-aid method, viz. multi-criteria analysis, is used to investigate the robustness of our findings. The results highlight the actual strategic choices made by Lufthansa for its own network, as well in combination with its partners in Star Alliance. European Journal of Information Systems (2010) 19, 449–461. doi:10.1057/ejis.2010.11; published online 16 March 2010

Keywords: airline networks; complexity; connectivity; concentration; network geometry; multicriteria analysis

## Analysis of complex networks

Networks are organized constellations that aim to shape and control human activities in an efficient way. In an open dynamic society, networks will be challenged to adjust themselves to new circumstances. And, consequently, all information, communication and transport networks are permanently in a state of flux. The use of advanced information systems offers even many more possibilities for a flexible adjustment of networks. The structure and formation of complex networks – using ingredients from information systems analysis – have received much attention in recent years. Boolean algebra in combination with digitally coded information form the constituents of network analysis, as exemplified, for instance, by traditional graph theory. Network analysis has become an established tool in, for example, operations research, telecommunication systems analysis and transportation science, while in more recent years it has also become an important analytical tool in industrial organization, sociology, social psychology and economics and business administration (Barthe´lemy, 2003; Gorman, 2005; Schintler et al., 2005a, b; Reggiani & Nijkamp, 2006, 2009; Goyal, 2007; Patuelli, 2007; Vervest et al., 2009). Air transport is a prominent example of modern network constellations and will be addressed in this paper from a structural network connectivity perspective. Air transport patterns show indeed clear network configurations, which impact on the way single airline carriers operate (Button & Stough, 2000). The abundant scientific literature on airline networks has addressed this topic in terms of both mathematical modelling and empirical measurements on different typologies of airline network configurations.

In this context, interesting research has emerged that mainly addressed the issue of describing and classifying networks by means of geographical concentration indices of traffic or flight frequency (Caves et al., 1984; Toh & Higgins, 1985; McShan, 1986; Reynolds-Feighan, 1994, 1998, 2001; Bowen, 2002; Lijesen, 2004; Cento, 2009). These measures, such as the Gini concentration index or the Theil index, provide a proper measure of frequency or traffic concentration on main airports in a simple, well-organized network. However, if a real-world network structure is complex, including multi-hub or mixed point-to-point and hub-spokes connections, the concentration indices may record high values for all types of structure, but fail to clearly discriminate between different network shapes (Alderighi et al., 2007). Consequently, there is a need for a more appropriate measurement of connectivity structures in complex networks, in particular, since in the modern airline industry competition takes place at all levels between companies, between airports and between airline networks. Sophisticated data analysis, instigated by advances in information systems technology, have laid the foundation for rapid and flexible adjustments of all actors in the aviation business, thus increasing competitiveness in this sector.

Starting from the above contextual observations, the present paper aims to investigate the relevance and applicability of a set of network connectivity/concentration indices, in order to properly typify and map out structural developments in complex airline network configurations. For reasons of data availability, the application of our analysis will address Lufthansa’s network, both European and world wide, while making a distinction between Lufthansa as an individual firm and Lufthansa in combination with Star Alliance. To put our analysis in perspective, we will first offer in the next section a concise review of recent developments in the airline industry. Then we will highlight the importance of network measurement analysis, followed by a description and assessment of various connectivity and concentration indices, applied to Lufthansa’s network. A robustness test using multicriteria analysis (MCA) is also undertaken, followed by concluding remarks.

## Structural changes in the airline industry

The airline industry has moved from a patchwork of individual and protected companies to a liberalized system of globally interconnected corporate organizations (see Martin & Voltes-Dorta, 2008; Nijkamp, 2008). The aviation sector has traditionally been a publicly controlled industry, with a high degree of government intervention, for both strategic and economic reasons. Already in 1919, the Paris Convention stipulated that states have sovereign rights in the airspace above their territory. Consequently, a series of bilateral agreements was established between countries that the airlines wished to fly over. The Chicago Convention (1944) made a distinction between various forms of freedom for using the airspace, ranging from the first freedom (the right to fly over the territory of a contracting state without landing) to the eigth freedom (the right to transport passengers and cargo within another state between the airports in that state). The airline sector ultimately became an overregulated – and thus inefficiently operating – industrial sector in the post-war period all.

The U.S. Airline Deregulation Act (1978) set the tone for a clear market orientation of the aviation sector in the U.S.A., where U.S.-based airlines were allowed to autonomously determine their routes, destinations, frequencies and airfares on their domestic flights, while new firms that were fit, willing and able to properly perform air transportation were free to enter the market. The resulting competition led to a rise in efficiency and innovative strategies in the airline industry and resulted in lower airfares, the entry of many new companies, and a significant increase in demand.

The airline deregulation in Europe has taken a much slower pace, due to the heterogeneity among European countries, the diversity of air traffic control systems and nationalistic motives for promoting a national carrier. Since the year 1988, Europe has gradually introduced a series of steps (so-called packages) to ensure a full deregulation of the European airline sector by the end of the last century, based on an integrated airline market characterized by fair competition and sound economic growth.

The next step in this deregulation process has been the Open Skies Agreement between the U.S.A. and Europe, which has opened up many more opportunities for carriers on both sides of the Atlantic to increase their financial viability and their market shares in a free competition across the Atlantic.

The changes in regulatory regimes in the European airline sector have prompted various new actions and strategies of European carriers in the past decade, such as mergers, takeovers and alliances. But the fierce competition has also led to bankruptcy of several existing carriers (such as Swissair and Sabena). More competition in a free market in Europe has largely had the same effects as in the U.S.A., except for the fact that flag carriers still kept a large share of the market.

In Europe, we currently observe – as a result of the deregulation packages – three airline business models: (i) full-service carriers (offering a variety of services and network linkages); (ii) low cost carriers/LCCs (offering a limited number of services on specific segments of the network (e.g., regional airports) at low prices, mainly on a point-to-point basis; and (iii) charter companies (offering various services to specific holiday destinations). The changing scene in competition in response to the deregulation has prompted a variety of network strategies (ranging from hub-and-spoke systems to point-to-point systems) and yield management practices (e.g., through market segmentation, product differentiation, booking classes, price setting and distribution channels). Various alliances have also occurred, but less mergers, to strike a balance between scale advantages and national identity/visibility (see Albers et al., 2005; Brueckner & Pels, 2005).

The above described force field has had far-reaching implications for the network strategies of airline companies. In the present paper, we will investigate the structure and evolution of the airline network of Lufthansa, both individually and in association with its international partners (in particular, Star Alliance) by paying particular attention to the connectivity and concentration patterns in a dynamic airline industry. Lufthansa has become a strong partner in the European airline sector, through its own strength as a large European company in one of the largest EU countries and through its successful strategic alliances with several European and non-European companies. This has induced important changes in its networks structure, as a consequence of both complementarity and competition. Advances in Information and Communication Technology (ICT) have helped to create a flexible adjustment pattern in the airline industry. A mixed type of multi-hub-and-spokes system has emerged which may be rather typical for the spatial-economic development of modern airline networks in Europe (see also Guimera & Amaral, 2004).

## Complex network analysis

Airline networks exhibit a clear example of a dynamically evolving, complex network. Modelling complex networks is a great challenge: on the one side, the topology of the network is governing the complex connectivity dynamics (see, for instance, Baraba´si & Oltvai, 2004); on the other side, the functional-economic relationships in such networks may also depend on the type of connectivity structure. The understanding of these two interlinked network aspects may be instrumental for capturing and analyzing airline network patterns (see also Guimera et al., 2005).

In the last decades network theory has gained scientific interest and sophisticated network models have been used in different fields, including economics and geography (Waters, 2006). This trend faced also quite some difficulty, because existing models were not able to clearly describe the network properties of many realworld systems, whose complexity could not fully be understood (Baraba´si & Albert, 1999). An interesting new development can inter alia be found in exponential random graph modelling, in which networks are represented as a dynamic graph, in which the network is growing in an exponential way. Through maximum likelihood procedures such random developments can be statistically investigated (see, e.g., Robins et al., 2007). In our approach, we will use in particular notions and concepts from complexity theory.

Spatial-economics systems – including air transport networks – are complex, because agents interact in order to obtain significant benefits by means of a joint activity (Boschma, 2005). This interacting process may become a permanent feature prompting a structure change, thus leading to a new meso- or macro-structure, for example, to the creation of activity clusters.

Air transport systems have over the past years been experiencing a variety of such clustering processes. An example is provided by airlines’ alliances. The processes underlying the creation of an alliance can be clearly depicted by considering the integration of Lufthansa and Swiss, described in the Lufthansa Annual Report (2005) (see http://konzern.lufthansa.com/en/html/ueber\_uns/ swiss/index.html). The main reason why airline carriers cooperate or form alliances stems from cost reductions they can thus obtain. Being a member of an alliance impacts on the carriers’ strategy for a long time and also influences the network configuration adopted by partners and competitors. It is worth noteworthy that alliances play also an important role in shaping market dynamics: in 2005, the three main alliances in air transport accounted for 80 per cent of the total capacity offer (see www.tourismfuturesintl.com/special%20reports/ alliances.html). Therefore, it is important to develop airline network models that can adequately take into account clustering and merger processes.

A further important trend many real networks show is the so-called ‘Small-World (SW) effect’. This term indicates that the diameter of a network is so small that it takes only a few movements along links in order to move between any two nodes of a network (the concept of diameter is defined in Table 1; see also Gorman & Kulkarni, 2004; Reggiani & Vinciguerra, 2007). In air transport systems, we can highlight the SW effect by taking into consideration and comparing the network configuration of single carriers or of alliances; such systems exhibit a clear SW effect when it takes only a small number of flights to link the two most distant airports in the network (see also Anderson et al., 1999).

Alongside the SW effect, the SW network model has been developed in order to take into account both the SW effect and the related clustering processes (Watts & Strogatz, 1998). The main features of this model are a short diameter and a high clustering coefficient.

A promising research direction related to the SW model is the study of so-called Scale-Free (SF) networks introduced by Baraba´si & Albert (1999) in order to incorporate two mechanisms upon which many real networks have proven to be based: growth and preferential attachment. The former points to the dynamic character of networks, which grow by the addition of new nodes and new vertices; the latter explains how new nodes enter the network, namely by connecting themselves to the nodes having the highest number of links.

An important feature of SF networks is represented by their vertex degree distribution. The vertex degree distribution is one of the key tools we may use to point out the network configuration (Reggiani & Vinciguerra, 2007), since this function determines the way nodes are connected. It can be defined as the probability P(k) that a chosen node has exactly k links (Baraba´si & Oltvai, 2004). In general, we can state that:

Table 1 Network’s topology indices

<table><tr><td>Index or measurement</td><td>Description</td><td>Formulation</td><td>Variables</td><td>Source</td></tr><tr><td>Degree</td><td>The degree of a node is given by the number of its links</td><td> $K(v)$ </td><td> $K(v)$  is the number of links of node  $v$ </td><td>Barabási &amp; Oltvai (2004)</td></tr><tr><td>Closeness</td><td>It indicates a node&#x27;s proximity to the other nodes</td><td> $C(v) = \frac{1}{\sum_{t \in V} d_{vt}}$ </td><td> $d_{vt}$  is the shortest path (geodesic distance) between nodes  $v$  and  $t$ ;  $n$  is the number of nodes in the network</td><td>Newman (2005)</td></tr><tr><td>Betweenness</td><td>It indicates a node&#x27;s ability to stand between the others, and therefore, to control the flows among them</td><td> $B(v) = \sum_{s \neq t \neq v \in V} \frac{\sigma_{st}(v)}{\sigma_{st}}$ </td><td> $\sigma_{st}(v)$  and  $\sigma_{st}$  are, respectively, the number of geodesic distances between  $s$  and  $t$  that pass through node  $v$ , and the overall number of geodesic distances between nodes  $s$  and  $t$ </td><td>Freeman (1977)</td></tr><tr><td>Diameter</td><td>It measures the maximum value of the geodesic distances between all nodes</td><td> $D = \max_{s,t \in V,s \neq t} d_{st}$ </td><td> $d_{st}$  is the geodesic distance between nodes  $s$  and  $t$ </td><td>Boccaletti et al. (2006)</td></tr><tr><td>Clustering coefficient</td><td>It measures the cliquishness of a node</td><td> $Cl(v) = \frac{l_v}{\max l_v}$ </td><td> $l_v$  and  $\max l_v$  are, respectively, the number of existing and maximum possible links between the nodes directly connected to node  $v$  (its neighbours)</td><td>Watts &amp; Strogatz (1998)</td></tr></table>

$$
P (k) = \frac {N (k)}{N},\tag{1}
$$

where N(k) is the number of nodes with k links and N is the number of nodes of the network.

In particular, in SF networks, the vertex degree distribution $P ( k )$ is proportional to $k ^ { - \gamma }$ (with k being the number of links), that is, to a power-law specification, as follows:

$$
P (k) \sim k ^ {- \gamma}.\tag{2}
$$

The power-lawfunction (2) characterizes networks having a small number of nodes with a very high degree, while the majority of nodes have a few links (Barabasi & Bonabeau, 2003). Eq. (2) has important economic implications: it characterizes SF networks, where the term SF refers to the fact that the power-law distribution does not change its form no matter what scale is used to observe it (Reggiani & Vinciguerra, 2007, p. 150), and that, in these networks, distances are irrelevant. Therefore, we expect to find SF networks in ‘global networks’, such as the Internet and air transport, and in general in those networks where relevant economic aggregation clusters (preferential attachments) attract flows from distant nodes.

The value of the degree exponent $\gamma$ in Eq. (2) depends on the attributes of the single systems and is crucial to detect the exact network topology, in particular the existence of the hubs (highly connected nodes). As Baraba´si & Oltvai (2004) highlight, an SF network embeds the proper hub-and-spoke model only when $\gamma = 2 ,$ , while for $2 \textless \gamma \leqslant 3$ a hierarchy of hubs emerges. For $\gamma > 3 ,$ , the hub features are absent and the SF network behaves like a random one.

In air transport systems, we can identify SF networks by considering full-service carriers. Without national or political impediments in a free market, these carriers typically organize their network into a hub-and-spoke system, where one or a few central airports called ‘hubs’ have a high number of links to the other airports called ‘spokes’. Passengers travelling from a place of origin to a place of destination have to stop typically in one or a few hubs to change aircraft. Hubs are organized in order to allow flight connectivity by coordinating the scheduled timetable of the arriving and departing flights. Investigating the airline strategy in designing hub connectivity and timetable coordination has been the aim of several empirical network studies. Some examples of theoretical and empirical investigation of hub connectivity can be found in the works of Bootsma (1997), Dennis (1998), Rietveld & Brons (2001), Veldhuis & Kroes (2002) and Burghouwt & de Wit (2005). As a consequence, the hub has to manage normally a high volume of traffic at the same time, due to their central connecting role in the network.

In contrast to SF networks, we have to highlight also random networks (Erdo¨s & Re´nyi, 1959), which display homogeneous, sparse patterns, without cluster characters. Their vertex degree distribution P(k) follows a Poisson distribution, as follows:

$$
P (k) \sim e ^ {<   k >} \frac {<   k > ^ {k}}{k !},\tag{3}
$$

and describes networks where the majority of nodes have approximately the same number of links, close to the average ok4(Baraba´si & Albert, 1999). For a review of random models, SF models and SW models, see also Albert & Baraba´si (2002) and Jeong (2003).

In air transport, random networks are useful to map point-to-point connections, as is the case for low-cost airlines (Cento, 2009). In the ideal point-to-point network all airports are connected to each other, so that passengers can fly from one airport to any other directly without stopping in any hub to change aircrafts. These networks have a low diameter, as a consequence of the high number of direct links between airports. Reggiani & Vinciguerra (2007, p. 148) point out that a random network can be seen as a homogeneous system which gives accessibility to the majority of the nodes in the same way. Furthermore, as is evident by looking at the plot of the exponential function, the probability to find highly connected nodes is equal to 0. Therefore, no clear hubs exist, and the network configuration appears to be random because no single airport displays a dominant role in a connected network.

In summary, this network topology is typical of equilibrated economic-geographical areas, where a high number of direct links can be profitably operated.

How can we describe the topological structure of networks? Networks can be analyzed from the perspective of their geometry and their concentration. Various relevant indices are included in Tables 1 and $^ { 2 , }$ respectively.

All the indicators in Tables 1 and 2 will be utilized in the empirical analysis concerning the exploration of the Lufthansa network’s topology and concentration.

## Application to airline networks: the case of Lufthansa

## Introduction

Information systems advances have created flexible possibilities for various kinds of partnership – ranging from code sharing to mergers – in the modern aviation sector. This has prompted the emergence of various types of network evolution in the airline business. This is clearly illustrated in the dynamics in Lufthansa’s network. We will address here the spatial configuration of Lufthansa’s aviation network in the year 2006. As mentioned above, the Lufthansa network is not an esoteric case, but rather representative of European airline developments, where complementarity between the airline operations of partners is sought, so that individual networks do not overlap significantly (unless joint flights or code sharing are used). The airline network measurement of such new configurations is essential for exploring the airline behaviour and its implications for the supply, the traffic demand, the airports’ infrastructure and aviation planning. The airline network can be subdivided into domestic, international or intercontinental configurations depending on whether the airports connected are located within a country, a continent or in different continents. Furthermore, an airline network can be interconnected or interlined to partner’s networks within the alliance concerned. This classification is based on geographical, air transportpolitical and economic characteristics, such as airlines’ degree of freedom from the Chicago Convention (see Cento, 2009) market liberalization, or costs and traffic demand. Therefore, the overall network configuration is the result of the integrated optimization of the domestic, international and intercontinental parts of the total network. These sub-network configurations may range from fully-connected or point-to-point to hub-and-spokes configurations to alliances (fully-contracted) or to a mix of these configurations. Within this conceptual framework, we will present our analysis of four sub-networks of Lufthansa. As summarized in Table 3, networks A1 and A2 refer respectively to the flights operated by Lufthansa in Europe and in the whole world, while networks B1 and B2 take into consideration – respectively at a European and at a global level – the flights operated by all the carriers which are members of Star Alliance (to which Lufthansa belongs). In particular, in 2010 the Star Alliance members are: Adria; Air Canada; Air China; Air New Zealand; ANA; Asiana Airlines; Austrian; Blue1; bmi; Brussels Airlines; Continental Airlines; Croatia Airlines, Egyptair; LOT Polish Airlines; Lufthansa; Scandinavian Airlines; Shanghai Airlines; Singapore Airlines; South African Airlines; Spanair; Swiss; TAP Portugal; THAI; Turkish Airlines; United; U.S. Airways (the list was retrieved from www.staralliance.com).

Table 2 Network’s concentration indices

<table><tr><td>Indicator</td><td>Formula</td><td>Use</td><td>Variables used</td><td>Sources</td></tr><tr><td>Gini concentration index</td><td> $G = \frac{\sum\limits_{i=1}^{n}\sum\limits_{j=1}^{n}\left|x_i - x_j\right|}{2n^2\mu}$ </td><td>It is a measure of geographical concentration</td><td> $x_i, x_j$  are the number of weekly flights from airports  $i$  and  $j$ , ranked in increasing order; $n$  is the number of airports in the network; $\mu$  is  $\sum_i x_i / n$ </td><td>Cento (2009)</td></tr><tr><td>Freeman centrality index</td><td> $F_B = \frac{\sum\limits_{i} [F_B(x^*) - F_B(x_i)]}{n^3 - 4n^2 + 5n - 2}$ </td><td>It is a measure of similarity to a perfect star network</td><td> $F_B(x_i) = \sum \sum b_{jk}(x_i)$  is the  $j < k$  betweenness centrality of node  $x_i; F_B(x^*)$  is the highest betweenness centrality value of the distribution</td><td>Cento (2009)</td></tr><tr><td>Entropy function</td><td> $E = -\sum\limits_{ij} p_{ij} \ln p_{ij}$ </td><td>It measures the degree of spatial organization and variety in a system</td><td> $p_{ij}$  is the probability of a link between nodes  $i$  and  $j$ </td><td>Nijkamp &amp; Reggiani (1992); Frenken &amp; Nuvolari (2004)</td></tr></table>

Table 3 Lufthansa’s network constellation (2006)

<table><tr><td>Network</td><td>Area under consideration</td><td>Carrier or alliance operating the flight</td><td>Nodes</td><td>Total number of links</td></tr><tr><td>A1</td><td>Europe</td><td>Lufthansa</td><td>111</td><td>522</td></tr><tr><td>A2</td><td>World</td><td>Lufthansa</td><td>188</td><td>692</td></tr><tr><td>B1</td><td>Europe</td><td>Star Alliance</td><td>111</td><td>3230</td></tr><tr><td>B2</td><td>World</td><td>Star Alliance</td><td>188</td><td>6084</td></tr></table>

The variable under analysis is represented by the number of direct connections of each airport in the summer season of the year 2006, measured on a weekly basis (Official Airline Guides (OAG), 2006). In all four cases, we only consider those airports where Lufthansa operates with its fleet and not by partner airlines (usually with code-sharing or franchising agreements). When we consider the A1 and A2 networks, we can clearly see that the majority of Lufthansa’s flights are operated within the considered continent. On the contrary, nearly half of Star Alliance’s flights are operated between Europe and other continents (between continents) or within non-European continents. This finding confirms our prior expectations, and is mainly explained by the fact that the majority of Star Alliance carrier members are established in non-European countries. It is thus clear that network structure is a response to a company’s strategy, and consequently, many aviation networks show nowadays a complex dynamics. We will now successively present and interpret the empirical results for network measures reflecting geometry, concentration and degree distribution, respectively.

## Network geometry

In order to examine the nodes’ location, we have computed the three centrality measures (degree, closeness and betweenness) described in Table 1 . Concerning the investigation of the nodes’ relations, we have examined the diameter and the clustering coefficient of the network (see Table 1).

The degree of a node (Table 1) can be seen as a measure of centrality if we assume – in the framework of our analysis – that the best connected airports have a greater power over the whole network, as they can control a considerable amount of all flights. In all networks, we find that the airports of Frankfurt and Munich have always the highest degree (see Table A1 in Annex A).

A further analysis of nodes’ centrality focuses on their ‘ease-of-access’ to the other nodes. It can be assumed that access to the network is easier when nodes are closer (Freeman, 1979). In order to investigate this concept we have computed (using the Pajek software, http:/ vlado.fmf.uni-lj.si/pub/networks/pajek) the closeness centrality (Table 1). The values of this index for the networks under consideration (listed in Table A2 in Annex A) show that the highest values usually correspond to the best connected nodes; therefore, closeness centrality is able to map out – in the framework of our study – the most important airports in terms of connectivity. A similar trend can be observed by considering betweenness centrality (Table 1; the values for networks A1, A2, B1 and B2 are listed in Table A3 in Annex A). This finding is interesting, since hubs – in the framework of the hub-and-spoke model – are chosen from those airports falling among the highest possible number of pairs of other airports (O’ Kelly & Miller, 1994; Button & Stough, 2000). Thus, strategic choices of companies appear to have a clear impact on network geometry.

The networks’ topology can also be explored by examining how the various nodes relate and link. since this last attribute impacts the configuration of the whole structure. For this purpose, we have computed the clustering coefficient (defined in Table 1; the 10 highest values for the nodes of the four networks of our experiments are listed in Table A4 in Annex A). The values indicate a significant difference between the networks A1 and A2 and the networks B1 and B2; in the former case the airports of Frankfurt and Munich dominate the chart; in the latter case, other airports appear to emerge, thus showing that flights are spread more equally on the whole network.

In addition, we will also consider the diameter of the above networks in order to investigate how the links patterns influence the ability to move inside the network.

Both A1 and A2 have a diameter of 4, while B1 and B2 have a diameter of 2. This can be justified only if there is no significant difference in the geographical configuration between A1 and A2, approximately a hub-and spoke, while B1 and B2 can be a mixture of hub-and-spoke and point-to-point networks. In other words, the integration of Lufthansa network in the Star Alliance reduces the travel distance, as the passengers can benefit from more connections and thus shorter paths to travel between the origin and the destination. This has important implications in the context of our study, because it entails that Lufthansa’s networks shrink, when we consider the flights of all Star Alliance members.

## Network concentration

The study of the networks’ degree of concentration – which is carried out in the present subsection – is crucial in order to detect the exact network topology, because the hub-and-spoke model is highly concentrated, while point-to-point networks do not show this feature (see also Butts, 2006).

First, Table 4 presents the normalized Gini index (see Table 1) for the four networks under consideration. Both Star Alliance networks are less concentrated than the Lufthansa counterparts, meaning that when we enlarge the measurement to a broader network including intercontinental destinations and partners’ networks, the configuration will probably evolve into a mix of multi hub-and-spoke and point-to-point structures. In particular, network A2 appears to be the most concentrated.

The information provided by the Gini index refers to the degree of concentration existing in a network, without any evidence on how this concentration impacts on the network topology. For this last purpose the Freeman centrality index (Table 1) has been computed. Its normalized values are represented in Table 4. This index assumes the value 1 for a hub-and-spoke network, and the value 0 for a point-to-point network (Cento, 2009).

According to the Freeman index, again networks A1 and A2 turn out to be the most concentrated ones. In particular, A2 network seems to be again the closest to the hub-and-spoke model; we may suppose that this network is characterized by a strong hierarchy among nodes.

Finally, concerning the last concentration index, that is, entropy (Table 1), Table 4 shows the related values for the networks A1, A2, B1 and B2. The results show that the entropy values are higher when we consider those flights operated by Lufthansa’s partners (networks B1 and B2). A likely explanation for this increase is given by the process of construction of these networks, obtained by the addition of flights to the nodes of A1 and $\mathrm { A } 2 ,$ respectively. Both B1 and B2 are therefore the ‘sum’ of the networks implemented by the different carriers that are members of Star Alliance, and hence they are not the result of a specific strategy, as is the case for A1 and A2. Clearly, the above values indicate that A1 and A2 networks are more concentrated and less dispersed than the B1 and B2 networks; more specifically, A1 appears to be the most concentrated network.

Table 4 Concentration indices

<table><tr><td>Network</td><td>Gini index</td><td>Freeman index</td><td>Entropy</td></tr><tr><td>A1</td><td>0.762</td><td>0.504</td><td>5.954</td></tr><tr><td>A2</td><td>0.813</td><td>0.757</td><td>6.194</td></tr><tr><td>B1</td><td>0.524</td><td>0.059</td><td>7.790</td></tr><tr><td>B2</td><td>0.699</td><td>0.056</td><td>8.389</td></tr></table>

In conclusion, from the above three indicators, networks A1 and A2 appear to be the most concentrated. However, among these two networks, A2 seems the most concentrated with respect to two indicators (Gini and Freeman), while A1 seems the most concentrated with respect to the entropy index.

## Network connectivity: degree distribution of the Lufthansa networks

The vertex degree distribution function is important in order to detect the most plausible network connectivity feature (see ‘Complex network analysis’ section). In this section, we will explore whether the variable ‘number of weekly connections’ is rank-distributed – over A1, A2, B1 and B2 – according to either an exponential or a power function. The $R ^ { 2 }$ values and the b coefficients of the two interpolating functions (exponential and power) concerning the four ranked distributions (in log terms) are listed in Table 5. The plots of both functions for the four networks under consideration are displayed in Annex B (Figures B1 and B2).

Both Table 5 and Figures B1 and B2 (in Annex B) highlight that our data sets better fit a power function, as the higher $R ^ { 2 }$ values indicate. Adamic (2000) shows that the power-law exponent $\gamma$ (emerging from the nodes’ probability distribution (Eq. (2)) is related to the power function coefficient b (emerging from the relation between the degree of the nodes and their rank (rank size rule); see Figures B1 and B2 in Annex B) as follows:

$$
\gamma = 1 + \left(\frac {1}{b}\right).\tag{4}
$$

Table 5 Exponential and power fitting of rank distributions

<table><tr><td rowspan="2"></td><td colspan="8">Network</td></tr><tr><td colspan="2">A1</td><td colspan="2">A2</td><td colspan="2">B1</td><td colspan="2">B2</td></tr><tr><td colspan="9">Network parameters</td></tr><tr><td>Distribution function</td><td> $R^2$ </td><td>b</td><td> $R^2$ </td><td>b</td><td> $R^2$ </td><td>b</td><td> $R^2$ </td><td>b</td></tr><tr><td>Power</td><td>0.95</td><td>0.99</td><td>0.93</td><td>0.82</td><td>0.75</td><td>0.67</td><td>0.70</td><td>0.65</td></tr><tr><td>Exponential</td><td>0.75</td><td>0.03</td><td>0.67</td><td>0.01</td><td>0.66</td><td>0.02</td><td>0.48</td><td>0.01</td></tr></table>

It is worth noting that the b coefficient of the power function for the networks A1, A2, B1 and B2 is, respectively, equal to 0.99, 0.82, 0.67 and 0.65 (Table 5). If we carry out a transformation of these coefficients according to Eq. (4), we observe that the A1 network displays a power-law exponent g equal to 2, thus indicating a stronger tendency to a hub-and-spoke system according to Baraba´si & Oltvai (2004), while the other three networks A2, B1 and B2 display a power-law exponent between 2 and $^ { 3 , }$ thus indicating a tendency to a hierarchy of hub/agglomeration patterns.

A further issue concerns the fitting of the exponential function. Also in this case we obtain high ${ \hat { R } } ^ { 2 }$ values, although inferior to the ones emerging in the power case; however, the coefficient of the exponential function is always very low, ranging from 0.01 to 0.03 (Table 5). Therefore, if we look at the $R ^ { 2 }$ indicators, all networks under consideration appear to be in a ‘border-line’ situation (that is, an ambiguity between a power and exponential fitting). Nevertheless, if we look at the coefficient values, the four networks seem to show a tendency toward an agglomeration structure of SF type, expressed by a clear power-law vertex degree distribution, with the degree exponent g equal to 2 (network A1), or varying between 2 and 3 (networks A2, B1, B2).

A further consideration concerns the plots of networks B1 and B2 (Figure B2 in Annex B). We can clearly see that both identify a power function with a cut-off. Thus, if we eliminate – in both networks B1 and B2 – those nodes which have less than 10 links, we slightly improve the fitting of their power function, obtaining for networks B1 and B2, respectively, $R ^ { 2 }$ values of 0.84 and 0.75, but still lower than the $R ^ { 2 }$ values regarding A1 and A2.

In conclusion, from our estimation results, the networks A1, A2 appear to show the strongest characteristics of connectivity to preferential nodes (see also Annex B and Table A1 in Annex A). In particular, network A1 appears to be the closest to the hub-and-spoke model, from the perspective of Baraba´si and Oltvai’s approach. Given these preliminary results, it is worth to examine these connectivity characteristics, jointly with some indicators of network concentration and topology previously considered. Consequently, a multidimensional method, such as MCA, taking into account – by means of an integrative approach – all adopted indicators and related results, was next carried out and utilized for further analysis.

## Network configuration: classification of the Lufthansa networks by means of MCA

The indicators assessed in the previous sections may be seen as characteristic features for various airline network configurations. These indicators may be interpreted as implicit achievement criteria, so that the four network configurations considered may be mutually compared by means of a multidimensional benchmark analysis in order to find out the most representative network. A multidimensional assessment approach, such as MCA, will now be applied to the four Lufthansa networks in order to identify the most appropriate system, according to the network indicators previously calculated. This may also be regarded as a test on network robustness. In this framework, the Regime method and software have been used (Hinloopen & Nijkamp, 1990).

Consequently, the alternatives are the four networks A1, A2, B1, B2 under consideration, while the criteria have been grouped according to three macro-criteria: network concentration, topology and connectivity (Table 6). It should be noted that, concerning the geometric criteria, we have considered the diameter and the clustering coefficient, as these two indices provide the network geometry’s features. In particular, concerning the latter, the average clustering coefficient has been adopted (Baraba´si & Oltvai, 2004).

The first group of macro-criteria is related to the networks’ concentration. It should be noted that in our MCA procedure, the entropy indicator needs to be transformed and interpreted positively, because the real values of the entropy function increase when networks are more heterogeneous, that is, less concentrated. The second group of macro-criteria refers to the networks’ physical measurement. Here, the diameter needs to be converted in utility, because its value is higher when networks are less centralized. The third group of macrocriteria is related to connectivity. This property is investigated through the interpolation of the ranked degree distributions, where – in the power function –the highest exponent of 0.99 implies, according to Eq. (4), a value of the exponent degree g – in the associated powerlaw distribution – close to 2 (perfect hub-and-spoke). The $R ^ { 2 }$ and the coefficient of the exponential function need to be converted to utility, since both values indicate random and homogeneous patterns.

We have carried out five scenarios by considering: (a) all the criteria mentioned above; (b) each macro-criteria separately; (c) concentration and topology criteria

## Table 6 Alternatives and criteria

<table><tr><td rowspan="4">Alternatives</td><td>A1 (Lufthansa, Europe)</td></tr><tr><td>A2 (Lufthansa, World)</td></tr><tr><td>B1 (Star Alliance, Europe)</td></tr><tr><td>B2 (Star Alliance, World)</td></tr><tr><td rowspan="3">‘Concentration’ criteria</td><td>Gini index</td></tr><tr><td>Freeman index</td></tr><tr><td>Entropy</td></tr><tr><td rowspan="2">‘Topology’ criteria</td><td>Diameter</td></tr><tr><td>Average Clustering Coefficient</td></tr><tr><td rowspan="4">‘Connectivity’ criteria</td><td> $R^{2}$  of the fitted power function (ranked degree distribution)</td></tr><tr><td>Coefficient of the power function</td></tr><tr><td> $R^{2}$  of the fitted exponential function (ranked degree distribution)</td></tr><tr><td>Coefficient of the exponential function</td></tr></table>

Table 7 Findings of multicriteria analyses

<table><tr><td>Criteria considered</td><td>All criteria combined</td><td>Concentration criteria</td><td>Topology criteria</td><td>Connectivity criteria</td><td>Concentration and topology criteria</td></tr><tr><td rowspan="4">Hierarchy of the alternatives</td><td>A1</td><td>A2</td><td>B1</td><td>A1</td><td>A1</td></tr><tr><td>A2</td><td>A1</td><td>B2</td><td>B1</td><td>B1</td></tr><tr><td>B2</td><td>B2</td><td>A1</td><td>A2</td><td>A2</td></tr><tr><td>B1</td><td>B1</td><td>A2</td><td>B2</td><td>B2</td></tr></table>

together. In each scenario an equal weight, that is, unknown priority, has been given to the single criteria. The results are listed in Table 7.

These rather robust findings point out that network A1 prevails, however with two exceptions. The former is represented by network A2, which is the top-scorer when we consider the criteria related to the networks’ concentration/geography: this finding comes from the higher centralization and concentration degree of network A2, as demonstrated by the Freeman and Gini indices. The latter exception is represented by network B1, which prevails when we consider the criteria related to the physical measurement of networks.

It turns out that the Lufthansa network A1 is the most connected one; we can conjecture that A1 is close to a hub-and-spoke system, according to the values expressed by its exponent degree in the power-law distribution (see Table 5). This result confirms the dual-hubs network strategy advocated by the German carrier (Lufthansa, 2005). Frankfurt and Munich act as central hubs, where all intercontinental flights depart and arrive in conjunction with the European and domestic flights. This timetable coordination is designed to allow passengers to transfer from one flight to another for different national and international destinations.

An interesting issue connected to the SF networks is the resilience of these networks, mostly in the context of transport security, epidemics, etc. SF networks are highly resistant to random failures, but very vulnerable to a deliberate attack directed against the major hubs. This might require additional protection: for example, by means of communication and information systems more strongly oriented to this specific aspect (see, e.g., Allenby & Fink, 2005).

## Retrospect and prospect

Network analysis turns out to be a powerful tool for analyzing the structure and evolution of transportation systems. Airline networks are fascinating examples of emerging complex and interacting structures, which may evolve in a competitive environment under liberalized market conditions. They may exhibit different configurations, especially if a given carrier has developed a flanking network framework together with partner airlines.

The present paper has investigated the network structure of four types of networks of Lufthansa by considering several indicators concerning the concentration, topology and connectivity (degree distribution), which – as outlined above – map out structural functions characteristics of this carrier. An integrated multidimensional approach, in particular MCA has been adopted, in order to take into account all information obtained by the above indices, and thus extrapolate the most representative network, according to these indicators.

The related results point out that all the four Lufthansa networks can be properly mapped into the SF model of the Baraba´si type. In particular, network A1 can be formally identified as a hub-and-spoke structure. In general, we can conjecture a ‘tendency’ towards a hubs’ hierarchy or hub-and-spoke configuration in Lufthansa’s European network (network A1), as also witnessed by the emergence of various nodes (Frankfurt, Munich and Dusseldorf) which are organized as hubs in the framework of Lufthansa’s activities. Apparently, this has been a rather successful network model, given the strong performance of Lufthansa in the Central European area. Preferential attachment is clearly an important anchor point for network design. All in all, the four networks exhibit a hierarchical structure mainly dominated by German airports. The moderate hub-and-spoke profile of the European airline industry is in agreement with the mixed structure of this industry, in which national interest, relatively small distances and competition by railways play an intermediate role.

The results obtained thus far highlight various characteristic features of complex aviation networks, but need to be complemented with additional investigations, in particular, on the structure and driving forces of the demand side (types of customers, in particular). Furthermore, the market is decisive in a liberalized airline system, and hence also price responses of customers as well as competitive responses of main competitors would need to be studied in the future. This might also offer a reply to the question whether and why LCCs operate in different niche markets or under different operating costs conditions.

From a methodological viewpoint a refined weighted network analysis – taking into account the strength of each connecting link – might offer better insights into the topological structure of the airline network at hand (see, e.g., Barrat et al., 2004), as well as into its structural dynamics and its implications for connectivity and concentration measures.

It ought to be recognized that our analysis was mainly prompted by the European aviation business development. But the general principles of network evolution as a smart response to external challenges (worldwide spread of diseases, terrorism, etc.) or to market competition (e.g., as a result of liberalization) hold across the entire airline industry. Obviously, different regions of our world face different challenges, but the type of network analysis presented here has a more universal validity. It is thus clear that modern network analysis offers a wealth of new and important research challenges to the scientific community. Proper information systems and information sharing from airline carriers is, of course, necessary to undertaken more sophisticated statistical analyses, but the current data bases are unfortunately fragmented, incomplete or too aggregate.

Finally, analysis of various network topologies – as a result of different competitive strategies of partners in an alliance – prompts a question on the returns accruing from a given network topology (see, e.g., Iatrou &

## About the authors

Aura Reggiani has a Ph.D. in Spatial Economics from the Free University of Amsterdam, the Netherlands. She is Full Professor of Economic Policy and currently chairing the courses of Transport Economics and Mathematical Methods for Economic Analysis at the University of Bologna (Italy), Department of Economics, Faculty of Statistics. She is a specialist in spatial and transport economics and modelling, with a particular view on the study on network evolution and complexity, from both the theoretical and empirical viewpoint. In these fields she has led several National/European research projects, by developing new network concepts and by applying them to the transport and telecommunication field. She has a long list of international publications in her field of expertise (about 20 volumes, 8 special issues, and 120 articles). She has been chairperson, speaker and discussant at numerous European and international conferences, and has lectured at several Universities in Europe and the U.S.A. She has been a fellow of the Netherlands Institute of Advanced Studies at the Royal Dutch Academy since 1991, working on network dynamics and evolutionary theories. She has been member of the executive committees of various International scientific organizations (e.g., Network for European Communications and Transport Activities Research (NECTAR), International Geographical Union (IGU), Regional Science Association International (RSAI) and is currently on the editorial boards of internationally recognized journals in her field (e.g., Transportation Research A, Networks and Spatial Economics, Transportation Research D, Journal of Geographical Systems, European Journal of Transport and Infrastructure Research, Logistics and Sustainable Transport,

Alamdari, 2005; Kleymann, 2005; Martin & Voltes-Dorta, 2008). This economic performance question leads us into yield management and strategic performance management, which would be a promising follow-up research endeavour.

## Acknowledgements

The present paper is a revised version of a previous paper ‘Network Measures in Civil Air Transport: A Case Study of Lufthansa’, published in Networks, Topology and Dynamics, Springer Series Lecture Notes in Economics an Mathematical Systems, 2008, Vol. 613 (A.K. Naimzada, S. Stefani, A. Torriero, eds). The authors wish to thanks Sara Signoretti (University of Bologna) for her assistance concerning the empirical application, as well as Roberto Patuelli (Institute for Economic Research, University of Lugano) for his comments on the present paper, as well as for his cooperation in the editing process. The authors also wish to acknowledge constructive comments by two anonymous referees on a previous version of the paper.

Journal of Transport and Land Use, Discrete Dynamics in Nature and Society, International Journal of Management and Network Economics). She has been Associated Coordinator for the EU-STELLA project (Sustainable Transport in Europe and Links and Liaisons with America) (www .stellaproject.org). She is currently President of NECTAR (http://www.nectar-eu.org), and also Member of the Science Board of the European Trans-disciplinary Institute IPL (Institute Para Limes: http://www.paralimes.org).

Peter Nijkamp is professor in regional and urban economics and in economic geography at the VU University, Amsterdam. His main research interests cover quantitative plan evaluation, regional and urban modelling, multicriteria analysis, transport systems analysis, mathematical systems modelling, technological innovation, entrepreneurship, environmental and resource management, and sustainable development. In the past years, he has focussed his research in particular on new quantitative methods for policy analysis, as well as on spatial-behavioural analysis of economic agents. He has a broad expertise in the area of public policy, services planning, infrastructure management and environmental protection. In all these fields he has published many books and numerous articles. He is member of editorial advisory boards of more than 30 journals. He has been visiting professor in many universities all over the world. According to the RePec list he belongs to the top 30 of well-known economists worldwide. He is past president of the European Regional Science Association and of the Regional Science Association International. He is also fellow of the Royal Netherlands Academy of Sciences, and past vice-president of this organization. From 2002 to 2009, he has served as president of the governing board of the Netherlands Research Council (NWO). In addition, he is past president of the European Heads of Research Councils (EUROHORCs). He is also fellow of the Academia Europaea, and member of many international scientific organizations. He has acted regularly as advisor to (inter) national bodies and (local and national) governments. In 1996, he was awarded the most prestigious scientific prize in the Netherlands, the Spinoza award. Detailed information can be found at http://staff.feweb.vu.nl/pnijkamp.

Alessandro Cento graduated (cum laude) in Statistics and Economics at the University of Bologna, Italy. He has worked as a researcher for the University of Lugano,

## References

ADAMIC LA (2000) Zipf, power-laws, and Pareto – a ranking tutorial. [WWW document] http://www.hpl.hp.com (accessed 16 April 2007).

ALBERS S, KOCH B and RUFF C (2005) Strategic alliances between airlines and airports: theoretical assessment and practical evidence. Journal of Air Transport Management 11, 49–58.

ALBERT R and BARABA<sup>´</sup> SI A-L (2002) Statistical mechanics of complex networks. Review of Modern Physics 74, 47–97.

A M, C A, N P and R P (2007) Assessment of new hub-and-spoke and point-to-point airline network configurations. Transportation Reviews 27, 529–549.

ALLENBY B and FINK J (2005) Towards inherently secure and resilient societies. Science 309, 1034–1036.

ANDERSON BS, BuTTs CT and CARLEY KM (1999) The interaction of size and density with graph level indices. Social Networks 21(3), 239–267.

BARABA<sup>´</sup> SI A-L and ALBERT R (1999) Emerging of scaling in random networks. Science 286, 509–512.

BARABASI A-L and BONABEAU E (2003) Scale-free networks. Scientific American 288, 60–69.

B <sup>´</sup> A-L and O ZN (2004) Network’s biology: understanding the cell’s functional organization. Nature Reviews-Genetics 5, 101–113.

BARRAT A, BARTHE´LEMY M, PASTOR-SATORRAS R and VESPIGNANI A (2004) The architecture of complex weighted networks. Proceedings of the National Academy of Sciences of the United States of America (PNAS) 101(11), 3747–3752 [WWW document] http://www.pnas.org/cgi/ doi//10.1073/pnas.0400087101.

BARTHE´LEMY M (2003) Crossover from scale-free to spatial networks. Europhysics Letters 63, 915–921.

BOCCALETTI S, LATORA V, MORENO Y, CHAVEZ M and HWANG D-U (2006) Complex networks: structure and dynamics. Physics Reports 424, 175–308.

BOSCHMA RA (2005) Proximity and innovation. A critical assessment. Regional Studies 39, 61–74.

BOOTSMA PD (1997) Airline Flight Schedule Development: Analysis and Design Tools for European Hinterland Hubs. University of Twente, Utrecht.

BOWEN J (2002) Network change, deregulation, and access in the global airline industry. Economic Geography 78, 425–439.

BRUECKNER JK and PELS E (2005) European airline mergers, alliance consolidation and consumer welfare. Journal of Air Transport Management 11. 27–41.

BURGHOUWT G and DE WIT J (2005) Temporal configurations of European airline networks. Journal of Air Transport Management 11(3), 185–198.

BUTTON K and STOUGH R (2000) Air Transport Networks: Theory and Policy Implications, Edward Elgar, Cheltenham.

BUTTS CT (2006) Exact bounds for degree centralization. Social Networks 28(4), 283–296.

C DW, C LR and T MW (1984) Economics of density versus economies of scale: why trunks and local service airline costs differ. Rand Journal of Economics 15, 471–489.

CENTO A (2009) The Airline Industry. Springer-Verlag, Berlin.

Switzerland and for the Swiss National Science Foundation in the field of Telecommunication and Transport Economics, publishing several articles and books contributions. In 2000, he joined KLM Royal Dutch Airlines in Milan in the Revenue Management Department. In 2006, he obtained a Ph.D. from the Faculty of Economics and Business Administration, VU University Amsterdam, the Netherlands. His Ph.D. research on Air Transport resulted in a monographic book published by Physica-Verlag. He is currently employed at Air France-KLM, while still carrying on international research collaborations with several Universities. He is member of the Air Transport Research Society, Regional Science Association International, European Regional Science Association and several other scientific societies.

DENNIS NPS (1998) Competition between hub airports in Europe and a methodology for forecasting connecting traffic. Paper presented at the 8th World Conference on Transport Research, Antwerp.

ERDO¨ S P and RE´NYI A (1959) On random graphs I. Publicationes Mathematiques 6, 290–297.

FREEMAN LC (1977) A set of measures of centrality based on

betweenness. Sociometrics 40, 35–41.

FREEMAN LC (1979) Centrality in social networks: a conceptual clarification. Social Networks 1, 215–239.

FRENKEN K and NUVOLARI A (2004) The early development of the steam engine: an evolutionary interpretation using complexity theory. Industrial Corporate Change 13, 419–450.

GORMAN SP (2005) Networks, Security and Complexity. Edward Elgar, Cheltenham.

GORMAN SP and KULKARNI R (2004) Spatial small worlds. Environment and Planning B 31, 273–296.

G S (2007) Connections: An Introduction to the Economics of Networks. Princeton University Press, Princeton and Oxford.

G R and A LAN (2004) Modeling the world-wide airport network. European Physical Journal B 38, 381–385.

GUIMERA R, MOSSA S, TURTSCHI A and AMARAL LAN (2005) The worldwide air transportation network: anomalous centrality, community structure, and cities’ global roles. Proceedings of the National Academy of Sciences 102(May 31), 7794–7799.

HINLOOPEN E and NIJKAMP P (1990) Qualitative multiple criteria choice analysis: the dominant regime method. Quality and Quantity 24, 37–56.

IATROU K and ALAMDARI F (2005) The empirical analysis of the impact of alliances on airline operations. Journal of Air Transport Management 11, 127–134.

JEONG H (2003) Complex scale-free networks. Physics A 321, 226–237.

KLEYMANN B (2005) The dynamics of multilateral allying: a process perspective on airline alliances. Journal of Air Transport Management 11, 135–147.

LIJESEN MG (2004) Adjusting the Herfindahl index for close substitutes: an application to pricing in civil aviation. Transportation Research E 40, 123-134

LUFTHANSA (2005) Annual report. [WWW document] http://konzern .lufthansa.com/en/html/ueber\_uns/swiss/index.html.

MARTIN JC and VOLTES-DORTA A (2008) Theoretical evidence of exciting pitfalls in measuring hubbing practices in airline networks. Networks and Spatial Economics 9, 161–182.

MCSHAN WS (1986) An economic analysis of hub-and-spoke routing strategy in the airline industry. PhD Thesis, Northwestern University.

NEWMAN MEJ (2005) A measure of betweenness centrality based on random walks. Social Networks 27(1), 39–54.

NIJKAMP P (2008) Policy developments in the airline industry. In Blue Skies or Storm Clouds (DE JONG D, KAASHOEK B and ZONDAG WJ, Eds), pp 20–25, Airlines Magazine Foundation, the Hague.

NIJKAMP P and REGGIANI A (1992) Interaction, Evolution and Chaos in Space. Springer-Verlag, Berlin.

OFFICIAL AIRLINE GUIDES (OAG) 2006 Worldwide Flight Guide. [WWW document] http://www.oag.com.

O’ KELLY EM and MILLER HJ (1994) The hub network design problem: an overview and synthesis. Journal of Transport Geography 2, 31–40.

PATUELLI R (2007) Regional labour markets in Germany: statistical analysis of spatio-temporal disparities and network structures. PhD Thesis, VU University Amsterdam.

REGGIANI A and NIJKAMP P (Eds) (2006) Spatial Dynamics, Networks and Modelling. Edward Elgar, Cheltenham.

REGGIANI A and NIJKAMP P (Eds) (2009) Complexity and Spatial Networks. In Search of Simplicity. Springer-Verlag, Berlin.

REGGIANI A and VINCIGUERRA S (2007) Network connectivity models: an overview and empirical applications. In Network Science, Nonlinear Science and Infrastructure Systems (FRIESZ T, Ed), pp 147–165, Springer-Verlag, New York.

REYNOLDS-FEIGHAN AJ (1994) EC and US air freight markets: network organisation in a deregulated environment. Transportation Reviews 14, 193–217.

R -F AJ (1998) The impact of US airline deregulation on airport traffic patterns. Geographical Analysis 30, 234–253.

REYNOLDS-FEIGHAN AJ (2001) Traffic distribution in low-cost and full service carrier network in the US air transport market. Journal of Air Transport Manggement 7. 265–275.

## Annex A

## Top 10 airports

In this Annex, we will present the top 10 scores of the airports – according to the main topological indices illustrated in Table 1 – belonging to the four airline networks A1, A2, B1 and B2.

See Tables A1–A5.

Table A1 Top 10 scores of airports according to the degree index (corresponding values in brackets)

<table><tr><td>A1</td><td>A2</td><td>B1</td><td>B2</td></tr><tr><td>MUC (82)</td><td>FRA (138)</td><td>FRA (106)</td><td>FRA (183)</td></tr><tr><td>FRA (81)</td><td>MUC (100)</td><td>MUC (105)</td><td>MUC (179)</td></tr><tr><td>DUS (39)</td><td>DUS (41)</td><td>BRE (97)</td><td>HAM (172)</td></tr><tr><td>HAM (24)</td><td>HAM (24)</td><td>HAM (97)</td><td>DUS (171)</td></tr><tr><td>STR (18)</td><td>STR (18)</td><td>BSL (94)</td><td>STR (168)</td></tr><tr><td>TXL (10)</td><td>TXL (10)</td><td>DUS (94)</td><td>LEJ (166)</td></tr><tr><td>CDG (8)</td><td>CDG (8)</td><td>LEJ (92)</td><td>ZRH (165)</td></tr><tr><td>NUE (8)</td><td>NUE (8)</td><td>NUE (92)</td><td>TXL (164)</td></tr><tr><td>BRU (7)</td><td>BRU (7)</td><td>STR (92)</td><td>NUE (163)</td></tr><tr><td>LHR (6)</td><td>MXP (6)</td><td>CGN (89)</td><td>BRE (162)</td></tr></table>

RIETVELD P and BRONS M (2001) Quality of hub-and-spoke networks; the effects of timetable coordination on waiting time and rescheduling time. Journal of Air Transport Management 7, 241–249.

ROBINS G. PATTISON P. KALISH Y and LUSHER D (2007) An introduction td exponential random graph (p\*) models for social networks. Social Networks 29, 173–191.

SCHINTLER LA, GORMAN SP, REGGIANI A, PATUELLI R and NIJKAMP P (2005a) Small-world phenomena in communication networks: a cross-Atlantic comparison. In Methods and Models in Transport and Telecommunications: Cross Atlantic Perspectives (REGGIANI A and SCHINTLER LA, Eds), pp 201–220, Springer-Verlag, Berlin.

SCHINTLER LA, GORMAN SP, REGGIANI A, PATUELLI R, GILLESPIE A, NIJKAMP P and R J (2005b) Complex network phenomena in telecommunication systems. Networks and Spatial Economics 5, 351–370.

TOH RS and HIGGINS RG (1985) The impact of hub-and-spoke network centralization and route monopoly on domestic airline profitability. Transportation Journal 24, 16–27.

VELDHUIS J and KROES E (2002) Dynamics in relative network performance of the main European hub airports. Paper presented at the European Transport Conference, Cambridge.

VERVEST PHM, VAN LIERE DW and ZHENG L (Eds) (2009) The Network Experience. Springer-Verlag, Berlin.

WATERS N (2006) Network and nodal indices. Measures of complexity and redundancy: a review. In Spatial Dynamics, Networks and Modelling (REGGIANI A and NIJKAMP P, Eds), pp 16–33, Edward Elgar, Cheltenham.

WATTS DJ and STROGATZ SH (1998) Collective dynamics of small world networks. Nature 393. 440–442

Table A2 Top 10 scores of airports according to the closeness index (corresponding values in brackets)

<table><tr><td>A1</td><td>A2</td><td>B1</td><td>B2</td></tr><tr><td>MUC (0.78)</td><td>FRA (0.79)</td><td>FRA (0.96)</td><td>BRE (1)</td></tr><tr><td>FRA (0.76)</td><td>MUC (0.64)</td><td>MUC (0.95)</td><td>DUS (1)</td></tr><tr><td>DUS (0.60)</td><td>DUS (0.53)</td><td>HAM (0.89)</td><td>ZRH (1)</td></tr><tr><td>HAM (0.55)</td><td>HAM (0.51)</td><td>DUS (0.87)</td><td>FRA (0.98)</td></tr><tr><td>STR (0.54)</td><td>STR (0.50)</td><td>NUE (0.86)</td><td>MUC (0.95)</td></tr><tr><td>TXL (0.51)</td><td>CDG (0.49)</td><td>STR (0.86)</td><td>HAM (0.93)</td></tr><tr><td>CDG (0.51)</td><td>NUE (0.49)</td><td>LEJ (0.85)</td><td>STR (0.91)</td></tr><tr><td>NUE (0.51)</td><td>BRU (0.48)</td><td>CGN (0.84)</td><td>LEJ (0.89)</td></tr><tr><td>LHR (0.51)</td><td>LHR (0.48)</td><td>TXL (0.84)</td><td>NUE (0.89)</td></tr><tr><td>MXP (0.51)</td><td>MXP (0.48)</td><td>ZRH (0.84)</td><td>FMO (0.85)</td></tr><tr><td></td><td>VIE (0.48)</td><td></td><td></td></tr></table>

Table A3 Top 10 scores of airports according to the betweenness index (corresponding values in brackets)

<table><tr><td>A1</td><td>A2</td><td>B1</td><td>B2</td></tr><tr><td>MUC (0.51)</td><td>FRA (0.76)</td><td>MUC (0.06)</td><td>MUC (0.06)</td></tr><tr><td>FRA (0.50)</td><td>MUC (0.03)</td><td>FRA (0.06)</td><td>FRA (0.06)</td></tr><tr><td>DUS (0.06)</td><td>DUS (0.03)</td><td>DUS (0.05)</td><td>DUS (0.06)</td></tr><tr><td>KUF (0.05)</td><td>BKK (0.02)</td><td>HAM (0.05)</td><td>BRE (0.05)</td></tr><tr><td>HAM (0.03)</td><td>KUF (0.02)</td><td>STR (0.05)</td><td>CGN (0.05)</td></tr><tr><td>GOJ (0.02)</td><td>HAM (0.01)</td><td>BRE (0.04)</td><td>HAM (0.05)</td></tr><tr><td>STR (0.01)</td><td>CAI (0.01)</td><td>HAJ (0.04)</td><td>NUE (0.05)</td></tr><tr><td>CDG ( $4.5e^{-4}$ )</td><td>CAN (0.01)</td><td>NUE (0.04)</td><td>STR (0.05)</td></tr><tr><td>CGN ( $9.5e^{-5}$ )</td><td>GOJ (0.01)</td><td>TXL (0.04)</td><td>ZRH (0.05)</td></tr><tr><td>BRU ( $1.9e^{-5}$ )</td><td>GRU (0.01)</td><td>CGN (0.04)</td><td>CGN (0.05)</td></tr><tr><td></td><td>JED (0.01)</td><td></td><td>DRS (0.05)</td></tr><tr><td></td><td>KRT (0.01)</td><td></td><td>LEJ (0.05)</td></tr><tr><td></td><td>LOS (0.01)</td><td></td><td></td></tr><tr><td></td><td>PHC (0.01)</td><td></td><td></td></tr></table>

Table A4 Top 10 scores of airports according to the clustering coefficient (corresponding values in brackets)

<table><tr><td>A1</td><td>A2</td><td>B1</td><td>B2</td></tr><tr><td>MUC (0.82)</td><td>FRA (0.75)</td><td>FRA (0.96)</td><td>BRE (1)</td></tr><tr><td>FRA (0.80)</td><td>MUC (0.48)</td><td>MUC (0.89)</td><td>DUS (1)</td></tr><tr><td>DUS (0.24)</td><td>DUS (0.11)</td><td>LEJ (0.77)</td><td>ZRH (1)</td></tr><tr><td>HAM (0.10)</td><td>HAM (0.04)</td><td>ZRH (0.67)</td><td>FRA (0.96)</td></tr><tr><td>STR (0.06)</td><td>STR (0.02)</td><td>BSL (0.66)</td><td>MUC (0.88)</td></tr><tr><td>CDG (0.01)</td><td>TXL ( $6e^{-3}$ )</td><td>STR (0.57)</td><td>LEJ (0.84)</td></tr><tr><td>TXL (0.01)</td><td>CDG ( $5e^{-6}$ )</td><td>DUS (0.55)</td><td>BSL (0.81)</td></tr><tr><td>NUE ( $9e^{-3}$ )</td><td>NUE ( $4e^{-3}$ )</td><td>HAM (0.55)</td><td>GVA (0.67)</td></tr><tr><td>BRU ( $6e^{-3}$ )</td><td>BRU ( $2e^{-3}$ )</td><td>GVA (0.48)</td><td>HAM (0.63)</td></tr><tr><td>MXP ( $4e^{-4}$ )</td><td>ZRH ( $2e^{-3}$ )</td><td>TXL (0.47)</td><td>STR (0.60)</td></tr><tr><td>VIE ( $4e^{-4}$ )</td><td></td><td></td><td></td></tr></table>

Table A5 Nomenclature of airports under study

<table><tr><td>BKK Bangkok</td><td>JED Jedda</td></tr><tr><td>BRE Bremen</td><td>KRT Khartoum</td></tr><tr><td>BRU Bruxelles</td><td>KUF Samara</td></tr><tr><td>BSL Basel</td><td>LEJ Leipzig</td></tr><tr><td>CDG Paris Charles de Gaulle</td><td>LHR London-Heathrow</td></tr><tr><td>CGN Koln</td><td>LOS Laos</td></tr><tr><td>DRS Dresden</td><td>MUC Munich</td></tr><tr><td>DUS Dusseldorf</td><td>MXP Milano-Malpensa</td></tr><tr><td>FMO Munster</td><td>NUE Nuremberg</td></tr><tr><td>FRA Frankfurt</td><td>PHC Port Harcour</td></tr><tr><td>GOJ Novgorod</td><td>STR Stuttgart</td></tr><tr><td>GRU Sao Paulo</td><td>TXL Berlin-Tegel</td></tr><tr><td>GVA Geneva</td><td>VIE Wien</td></tr><tr><td>HAM Hamburg</td><td>ZRH Zurich</td></tr></table>

## Annex B

## Rank distributions

In this Annex, we will present the rank distribution fitting for the networks A1, A2, B1 and B2, with reference to the following variables: y axis ¼ number of weekly connections; x axis ¼ airport (node) rank. The related fitting has been carried out by considering both an exponential and a power interpolation (see Table 5 for the synthesis of the results).

See Figures B1 and B2.

![](/api/attachments/SRG9BXYA/fulltext/images/a3465b1cb29a381bcb3141d76b19d7f2bafbe5e7fd3a3a599c266e1e68017838.jpg)

![](/api/attachments/SRG9BXYA/fulltext/images/53657d2a652d77fd4e3f69cb46582518926e00c6f917666916bfaab877f79765.jpg)  
Figure B1 Rank distribution fitting for networks A1 and A2.

![](/api/attachments/SRG9BXYA/fulltext/images/dd9903fa0e3261669774ebaa41c853f438216ea21317177c7d1c6541791a1102.jpg)

![](/api/attachments/SRG9BXYA/fulltext/images/85b628c56513c88c31c930f9533561848c55bd782403a96cb82938f1b208a801.jpg)  
Figure B2 Rank distribution fitting for networks B1 and B2.
