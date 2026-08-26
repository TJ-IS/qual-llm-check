---
otero_id: 3792
otero_key: "5C8UMDZE"
title: "Spatial Decision Support Systems: Three decades on"
authors: "Peter Bernard Keenan; Piotr Jankowski"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.10.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Peter Bernard Keenan<sup>a,⁎</sup>, Piotr Jankowski<sup>b,c</sup>

<sup>a</sup> UCD School of Business, University College Dublin, Belfield, Dublin D04 V1W8, Ireland

<sup>b</sup> Department of Geography, San Diego State University, San Diego, CA, USA

<sup>c</sup> Institute of Geoecology and Geoinformation, Adam Mickiewicz University, Poznań, Poland

## A R T I C L E I N F O

Keywords: Geographic Information Systems Spatial Decision Support Systems Bibliographic analysis

## A B S T R A C T

This paper uses a bibliometric approach to examine the growth of and changes in the Spatial Decision Support Systems (SDSS) field over the past three decades. Bibliographic databases such as Web of Science (WOS) and Scopus provide valuable information on academic disciplines as they contain both the articles published and the articles cited. The articles published, and the disciplinary categorization of where they are published, are indicative of the changing disciplinary balance in SDSS, while the citation links of these papers illustrate the intellectual structure of the field. The analysis shows that despite conceptual links rooted in DSS, the field of SDSS developed largely independently from DSS, with little interaction between both. This is surprising, given the growing importance of spatial applications in DSS and an overlapping interest in business analytics and big data space-time analytics. The paper argues for greater interest in SDSS developments in the DSS field, including emergency response SDSS and public participation SDSS, as two forms of SDSS which extend DSS.

## 1. Introduction

## 1.1. Spatial Decision Support Systems

Spatial data are data connected to a location, a place on the earth. Spatial decision-making exploits the geographic relationships within this data to make decisions. Spatial Decision Support Systems (SDSS) combine spatial and non-spatial data, the analysis and visualization functions of Geographic Information Systems (GIS), and decision models in specific domains, to compute the characteristics of problem solutions, facilitate the evaluation of solution alternatives and the as. sessment of their trade-ofs [1]. The decision problems in SDSS are typically characterized by a combination of spatial and non-spatial characteristics, with the former recording a location's geographical coordinates and spatial relations (i.e., proximity, overlap, containment, distribution pattern). The types of decision problems include; site se lection, resource allocation, network routing, location-allocation, and service coverage. The term SDSS originated with Hopkins & Armstrong [2] and became widely accepted after the inclusion of SDSS as a chapter [3] in the definitive 1991 research compendium on the science, application, and practice of GIS [4]. While there had been a small number of systems incorporating decision support functions and spatial data before 1990, the resource-intensive nature of spatial processing meant that SDSS only became generally feasible in the 1990s [5].

Compared to traditional DSS, data from outside the organization using the DSS plays a much greater role in SDSS applications because richer decision modeling is made possible by the inclusion of relevant external data. For example, an organization might conduct a location analysis for its depot using data on the location of its customers. However, the inclusion of detailed road networks would greatly enhance the quality of the transport modeling, demographic data would allow modeling of prospective customers as well as current customers and utility data might identify feasible locations. Consequently, the availability of external spatial data has allowed a richer representation of spatial problems of considerable value to decision-makers. While other types of DSS application have made use of external data, this data is usually closely related to the domain of the decision-maker and its integration has often proved challenging [6]. Spatial applications generally combine organization-specific data with data on the geographic properties and relationships of the area encompassing the decision problem; the latter data is typically sourced outside the organization and is not specific to the organization or the decision problem. The progress of algorithmic, computational, and communication approaches both directly made SDSS technically feasible and indirectly provided the availability of third-party spatial data, which made SDSS applications economically feasible. This is an ongoing process, and the data needed for diferent forms of decision has become available at diferent times, so that SDSS has developed faster in some fields than others. External spatial data typically initially originated from specialized government agencies, and later came from commercial providers. However, an important recent development is the contribution of vo lunteered geospatial information (VGI) in spatial analytics through ad hoc crowdsourcing initiatives [7] and by the general public through more systematic eforts such as Open Street Map [8].

## 1.2. Research approach

The objective of this research has been to trace the intellectual, methodological, and technological trends influencing the development of SDSS field from its inception in the mid-1980s until the present. This period includes: 1) early SDSS developments, during the late 1980s and the decade of the 1990s, constrained by limited spatial data resources and GIS software lacking standardized application programming interfaces, 2) the decade of 2000s characterized by rapid technological developments of hardware, geospatial software, and data, and 3) the period after 2010, during which SDSS have proliferated into individualized location-based services, dynamic systems taking advantage of frequent data updates, and public sector decision support applications relying on public participation and abundant data streams collected from a variety of location-aware sensors. This research has been motivated by the question of whether two related fields: DSS and SDSS, have grown in isolation of each other or whether there has been a cross-fertilization resulting in new concepts, methods, and application areas. This paper contributes to research on DSS/SDSS in two ways; first, it maps the field based on a bibliometric approach to publication records held in bibliographic databases and traces linkages among concepts, methods, and authors who influenced the development of SDSS. Second, it is an insight into the conceptual/methodological and technological triggers that shaped the trajectory of the field and that have led to its current status.

Bibliographic databases such as Web of Science (WOS) and Scopu not only contain information on a substantial proportion of articles published but, more importantly, also on the publications cited. The articles and the disciplinary categorization of their publication outlets are indicative of the changing disciplinary balance in SDSS, while the citation links of these papers trace the lineage of ideas, concepts, and methods. This research approach combines the coverage of computer ized databases with modern computer processing power to gain quantitative insight into the development of scientific fields. The paper employs scientometric software to analyze the WOS and Scopus databases to provide visualizations and network analyses of the SDSS field.

A science map is one of the most widely used scientometric visualizations. Small [9] page 799 says “A map of science is a spatial representation of how disciplines, fields, specialties, and individual papers or authors are related to one another as shown by their physical proximity and relative locations, analogous to the way geographic maps show the relationships of political or physical features on the Earth”. The interpretation and analysis of journal databases is facilitated by standard maps of the subject space and the use of standard clustering of disciplines. These approaches allow the identification of fields and subfields from the clustering of papers, authors or journals and allow the representation of both citing and cited publications. Leydesdorf, with various collaborators [10–12] has developed programs to analyze WOS data, whose output can be exported to Vosviewer [13], a software tool to visualize bibliometric maps. In this research, we compare the disciplinary distribution of SDSS papers to the distribution of papers in all scientific disciplines and look at the distribution of papers within SDSS. We also used the CitNetExplorer software [14.15] to visualize the citation network of key papers in the development of the SDSS field.

## 1.3. Bibliographic analysis techniques

In bibliographic analysis, networks are formed from publications represented by nodes and the links between them, which provides both a visual representation of a field and allows for the automated analysis of that field [16]. This analysis is now a subset of the broader field of social network analysis whose techniques have significantly advanced in recent years as more data has become available [17].

A basic citation network is a mathematical graph where each node represents a citing publication, and each directed link represents a citation from the current publication to an earlier cited publication. Bibliographic coupling groups publications which cite the same publication, for instance a simple cited reference search on WOS or Google Scholar will show all publications which cite an earlier publication. Cocitation coupling [18] looks at the references cited by a publication and forms an undirected co-citation network linking publications which are cited together. Two publications are said to be co-cited when they are both cited by a third document, if they are cited together in multiple publications then they have a stronger relationship. In a co-citation network, the link weights represent the number of times that two documents were jointly cited. From these links and link weights, we can identify research clusters with groups of strongly connected references. Earlier papers can be clustered by common citation by later publications, revealing a commonality in earlier concurrent papers. Document co-citation analysis (DCA) built on the methods pioneered by Small [9,19] is widely used to analyze individual papers. DCA can produce large networks as it may include links between all documents cited by articles of interest, so normal practice is to reduce the network by excluding documents with a small number of citations and with low levels of co-citation.

Journal co-citation analysis (JCA) [20] uses cited journals as the network nodes, this generates a smaller network than DCA will pro duce. Other bibliographic techniques include author co-citation analysis (ACA). As only the first author is included in WOS data, we did not use ACA in this paper. In this research, we used CiteSpace [21] and Vosviewer [13,15] to build DCA and JCA networks and to visualize the network and Pajek software [22] to perform network analysis and to identify key papers.

## 1.4. Bibliographic data used

The Thomson-Reuters Web of Science™ Core Collection covers over 12,000 of the highest impact journals worldwide, including Open Access journals, and over 150,000 conference proceedings. It provides author details for these papers and full citation information and categorizes publications using 252 disciplinary categories. This information can be analyzed in various ways, and several computerized tools have been developed to facilitate the analysis and visualization of WOS data. In 2017, Scopus covered some 22,800 titles from over 5000 publishers, of which 21,950 were published in peer-reviewed journals. Compared to WOS, Scopus has more coverage, especially in the humanities, but has some limitations for older records [12]. Because of these limitations and as the set of journals has expanded over time, our analysis for Scopus only includes the recent period 2006–2015. We used the conversion tool in CiteSpace to convert Scopus data to WOS format. This conversion performs well in relation to citations to journals but has some limitations where the citation is to a book and even more problems when the citation is to a book chapter. In general, records relating to journals are consistently organized and can be processed by computerized tools, while records relating to conference proceedings and book chapters are less consistent and are therefore more dificult to process. Consequently, this paper follows the frequent practice in bibliographic research of concentrating on journals and their citations. While citations of journals are more consistent than those of books significant manual processing of journal names was still required where diferent abbreviations for journals had been used. Coding diferences made integrating the records from WOS and Scopus dificult and so we have analyzed them separately.

This paper uses data drawn from both WOS and Scopus, using the search terms in Table 1. The datasets contain citations from journal articles and exclude citations from books and conference proceedings. They do include citations of books and conference proceedings from journal articles. The numbers of cited references (Table 2) reflects using some cleaning of the data to identify journals and authors referenced in slightly diferent ways. We used the CRExplorer software [23] to clean the data by removing references without dates and to identify similar references.

Table 1

<table><tr><td colspan="2">Table 1Search terms used.</td></tr><tr><td></td><td>“spatial decision support system” OR “spatial DSS”</td></tr><tr><td>OR</td><td>(“decision support system” OR (“decision support” AND DSS))AND (“geographical information system” OR “geographic information system”) OR(Geographic and GIS) OR (Geographical and GIS) OR (spatial and GIS))</td></tr><tr><td>OR</td><td>“decision” and (“location analytics” or “location-based service” or “location-based service”)</td></tr><tr><td>OR</td><td>(“spatial decision making” and system) or (“spatial decision-making” and system))</td></tr></table>

Table 2  
Datasets extracted using search terms in Table 1.

<table><tr><td></td><td>Web of Science (Core Collection)</td><td>Scopus</td></tr><tr><td>Period</td><td>1990–2015</td><td>2006–2015</td></tr><tr><td>Citing records</td><td>844</td><td>2636</td></tr><tr><td>Cited refs</td><td>26,895</td><td>79,053</td></tr></table>

## 2. SDSS technology

## 2.1. Technology background

The changes in SDSS represented in this research have been made possible by the ongoing improvement in the capacity of widely avail able technology to support spatial data collection, spatial data manipulation, and spatial analysis. Since the early period of SDSS, GIS software has acquired a diverse range of analysis and geoprocessing tools that are of benefit to DSS builders [3,5,24]. With the advance in computer performance, GIS software will now run on commonly available computers and even on handheld devices. In addition to commercial software, open source software has now reached comparative maturity, for example QGIS. In the earlier period of SDSS development, integrating GIS software with modeling was frequently challenging and an obstacle to building SDSS [24]. However, this situation has greatly improved and both commercial and open software is now designed to facilitate interaction with other software, with a large range of plugins and third-party tools now available [25]. It is these combinations of software and modeling and their ease of integration that has greatly extended the range of SDSS applications to the current diversity [5].

## 2.2. Internet and mobile SDSS

The Internet and mobile systems represent technologies which have been growing in importance since the early days of SDSS. The Internet has become a widely-used platform for commercial mapping services to which an SDSS may be connected. In a 2003 review of Internet SDSS, Rinner [26] found that many systems fell short of the definition of a DSS, but suggested that public participation SDSS would become important. This reflects that geographic space is shared and that the Internet is one way of reaching the multiple users who may have an in terest in that space. Mobile technologies developed rapidly following the growth of the Internet and their development was spurred by the availability of unrestricted Global Positioning System (GPS) signals since 2000. As modern smartphones and tablets are equipped with a GPS receiver, this has facilitated location-based services (LBS), which ofer great possibilities for decision support, for instance, in dealing with transport emergencies [27] and creating new forms of mobile commerce as an extension of e-commerce [28]. However, in addition to extending existing areas of application, LBS also ofers new and interesting forms of SDSS application, an example being precision agriculture, where decisions about agricultural practice are made at a micro level [29].

While mobile technologies facilitate the delivery of SDSS, other developments such as cloud computing have provided the computing capacity to address problems with large amounts of data. The intrinsically large volumes of data in spatial applications mean that SDSS may represent one form of DSS where the capacity of cloud computing is actually required [30]. SDSS can benefit from the development of suitable cloud-based tools which they can incorporate into their systems [31].

Even in the pre-computer age, the map was one of the most advanced forms of visualization and cartographic techniques have long been recognized as an important form of visualization for decisionmaking [32]. Many potential SDSS users trained in spatial disciplines are accustomed to visual representations and are accepting of these in an SDSS context. However, Jarupathirun and Zahedi [33] found that non-spatially trained users also believed that SDSS assisted their decision-making. Public acceptance of SDSS has likely increased since this research was done, as spatial representations have become even more widely used by the public in the form of mapping websites, route planners, mobile apps, and similar free tools [34]. Nevertheless, SDSS visualization presents a challenge, as the object is not to directly represent space but to represent a decision with a spatial component [35]. In DSS, including SDSS, the decision representation will have to reflect the specific problem and specific requirements of the decision-maker [36].

## 2.3. Spatial data

SDSS is distinctive in the DSS world, as the feasibility of a project is determined not only by the available technology but also by the available spatial data from outside the organization and outside the discipline of the SDSS user. The availability of spatial data has greatly improved over the past 30 years, thanks in part to the lowering of data acquisition costs and also due to national and transnational geospatial data initiatives. A wider range of data is available and diverse sources of spatial data have been cataloged by Spatial Data Infrastructure (SDI) initiatives, although problems remain in integrating data from diferent sources at diferent spatial scales and standards and from diferent types of organization [37]. Traditional government and commercial sources of spatial data have been augmented with open source crowdsourced data, notably the OpenStreetMap project [38]. This free data has become available for parts of the world where comprehensive geographic data had never become available from government and commercial sources or where budgetary pressures slowed data updates resulting in data obsolescence. As most geographic data remains stable, the coverage can improve over time as shown by OpenStreetMap [8,39], which is continually being extended and quality errors are gradually being eliminated. Consequently, crowdsourced data is now used for a wide range of applications [40], and the international standardization of OpenStreetMap makes systems implementable throughout the world [41]. Crowdsourced data and its combination with open source software can make SDSS projects economically feasible in a much wider range of situations, especially in less prosperous countries.

OpenStreetMap represents spatial data that is structured and deliberately collected. However, there is a growing volume of spatial data originating in social media that is either passively generated (e.g. mobile phone locations) or where the spatial element is a minor part of the user's interest (geo tagged photographs). This spatial data derived from social media is an increasingly important resource for decision makers interested in public behavior [42]. Where data is explicitly geo-tagged it may be used fairly easily, but often the location is implicit rather than explicit, for instance a tweet may contain a text reference to a location. Implicit locations may require significant processing of the source data to become useful geo data [43].

The increase in the volumes of spatial data reflects the large increase in data volumes generally, which underlie the growth in “big data” and analytics. Modern data analytics includes the use of spatial data, not only traditional geographic data but also the spatial movement of people within transportation corridors, shopping malls, airports, sporting event venues, and other locales [44], and across urban space and time [45]. While spatial techniques were confined to specialized software in the 1990s, since then support for spatial data has been added to the major database products that support big data [46]. As a result, spatial techniques are now used in a wide variety of applications, but this use frequently does not constitute comprehensive decision support. One issue arising with “big data” is that data from diferent sources are aggregated, including spatial data, and analyzed without a good understanding of the data sources [47], which is at odds with the DSS concept of an informed decision-maker directing the process.

Fig. 1 illustrates the major influences on SDSS; both from the DSS and decision-making domains and those from spatial concepts and techniques. These influences also suggest how certain groups came to SDSS. Some groups who had long used modeling and who had already used these techniques in DSS found it beneficial to add spatial techniques and exploit publicly available data, examples would be location analysis or routing [48]. Other groups had used GIS and spatial datasets and then moved to SDSS by adding additional decision tools under the control of the decision-maker, for instance in forestry [49,50] or land management [51], to better exploit these spatial resources for decision modeling. Like DSS, individual SDSS subsequently evolved into group applications [52,53] and toward analytics. The greater technical demands of SDSS meant that its evolution generally has taken place later than many other forms of DSS; there are also sub-domains within SDSS at diferent stages of evolution, as the relevant spatial data or the technology to process it only became available at a later date.

## 3. SDSS literature

Modern bibliographic databases potentially provide great insight into the evolution of academic disciplines, including the range of authors, journals, and disciplines cited by specific journals. This form of bibliographic analysis is now facilitated by the availability of citation databases in electronic form and the capacity of modern computers to process these. Over the years, various forms of research have examined the range of disciplines relevant to DSS [55] and the spread of DSS applications [56,57]. These studies conducted a rigorous examination of the field by assessing whether articles fell within a classic definition of DSS; in the structure of the decision, the interaction with the user and the use of models and databases. A labor-intensive approach of reading each paper can be beneficial owing to the diversity in the use of the term DSS, as many papers use the term to describe systems that do not meet the classic definition of DSS. However, with an increasing number of papers published the labor-intensive approach becomes infeasible, while new software bibliographic tools both allow investigation of a larger number of papers and ofer additional insights to facilitate the understanding of academic fields.

![](/api/attachments/5C8UMDZE/fulltext/images/0cdfafbf7b89768c47cd505bc7f71f10cd10be15f0190ab5ca43cb49386f1883.jpg)  
Fig. 1. The genealogy of the SDSS field. (Adapted from [54].)

![](/api/attachments/5C8UMDZE/fulltext/images/cdd5cd792f3d9bd94a49b32e1e8dcace215eb25642cf66da802af8e098b6dff0.jpg)  
Fig. 2. Visualization of SDSS publications in WOS http://www.leydesdorf.net/journals12/.

## 3.1. Visualization of SDSS disciplines

The interpretation and analysis of journal databases is facilitated by standard visualizations of the subject space and the use of standard clustering of disciplines. Leydesdorf, with various collaborators [10–12] has developed several programs to analyze WOS data and allow the visualization of both citing and cited publications. The disciplinary plot of SDSS publications in Fig. 2 uses a base map of all journals based on their citing patterns and using an algorithm for the coloring of 12 clusters [11,12]. Fig. 2 plots journal articles identified in WOS for the period 1990–2015 (see Table 2 above). In Fig. 2, the traditional publication outlets for DSS are found on the right-hand side of the visualization, as represented by the journal Decision Support Systems and by OR/MS journals and Transportation journals positioned above. Many examples in this group are application domains that have long been users of DSS, but who have taken advantage of the greater availability of spatial data to provide richer decision support for their problems. However, traditional areas of DSS represent a declining proportion of SDSS papers, as the number of papers in other areas has increased more rapidly. In the lower right of the figure are the discipline journals representing with the more traditional users of GIS. Frequently, this group evolved from using GIS as a record of their activities to subsequent decision support applications, in much the same way as business applications moved from data processing to DSS. The traditional sectors have had a relatively constant proportion of SDSS papers over the period. Note that the International Journal of Geographical Information Science (IJGIS) (formerly called the International Journal of Geographical Information Systems until 1997) is positioned close to the Decision Support Systems journal, although they are allocated to diferent clusters. This positioning and clustering are derived from Leydesdorf and based on the overall citing patterns of the journals across all articles. The size of each node in Fig. 2 reflects the specific number of citing articles relating to SDSS and the position represents the relationships identified by Leydesdorf for all articles in WOS [11].

At the top of Fig. 2 are papers in the environmental sciences, an expanding area of DSS and GIS deployment, much of it in the form of SDSS [58]. The largest group, distributed across a wide range of journals, is in environmental management. These papers are concerned with themes such as the management of waste, pollution and dealing with natural hazards. The top left includes areas such as forestry and agriculture. Forestry is a long-established area of DSS and GIS application, and an early adopter of SDSS [59], while agricultural SDSS papers have become frequent only in recent years. The health sector, to the left of the figure, is a growing area of application within the DSS field as whole [58], but hasn't yet had a significant proportion of SDSS examples, although there are epidemiological applications in environmental modeling journals on the top left of the diagram and a handful of isolated examples elsewhere. Other research communities such as biosciences and economics are little represented. Table 3 shows the proportions of SDSS papers in diferent disciplines in two periods. It shows a decline in the proportion of papers in OR/MS and Information Technology and in Agriculture/Forestry and growth in Environmental Engineering and in GIS/Planning, which reflects the much greater volumes of environmental spatial data in later periods.

Disciplinary breakdown of SDSS papers in journals the Web of Science, Core Collection.

<table><tr><td>Sector</td><td>1990–2005</td><td>2006–2015</td></tr><tr><td>GIS/planning</td><td>16%</td><td>19%</td></tr><tr><td>OR/MS and information technology</td><td>21%</td><td>16%</td></tr><tr><td>Agriculture/forestry</td><td>25%</td><td>22%</td></tr><tr><td>Physical science</td><td>2%</td><td>1%</td></tr><tr><td>Environmental engineering</td><td>34%</td><td>38%</td></tr><tr><td>Other</td><td>2%</td><td>4%</td></tr></table>

## 3.2. Important journals in SDSS research

Of the journal articles in WOS with keywords related to SDSS in the period 1990–2015 (citing articles), the journals with the most citing papers are IJGIS and four journals related to Agriculture or Environmental Engineering (Computers and Electronics in Agriculture, Journal of Environmental Engineering, Environmental Modelling & Software, and Ecological Modelling). Following these, the next five include two journals long associated with GIS, Computer, Environment and Urban Systems, and Environment and Planning B, and two further environmental journals, Environmental Management and Environmental Monitoring and Assessment. The most highly ranked traditional DSS journal by the number of citing articles is Decision Support Systems in seventh place, which is grouped with OR/MS and Information Systems (IS) journals in Table 3 and Fig. 2.

CiteSpace is a bibliographic tool for visualizing and analyzing structural and temporal patterns in the scientific literature [21]. Cite-Space operates on data drawn from WOS, like many other bibliographic tools, but also has a conversion tool for Scopus data. Wei, Grubesic, and Bishop [60] used CiteSpace to create a bibliographic network of GIS publications and to identify key publications. They also used CiteSpace to identify clusters using DCA and they suggested that the clusters on landfill site selection and emergency facilities represented SDSS applications.

In our analysis, we used the Scopus dataset to create a JCA network. While Citespace could build and visualize a JCA network we found it slow to complete network calculations, taking several days in some cases. Consequently, we exported the JCA network generated by Vosviewer [13] and used the Pajek software [22], an extremely eficient tool for analyzing social networks, to analyze the network. To reduce the size of the network for the network analysis, we excluded journals with less than 10 citations in total, leaving 900 journals in the set. We also used a network of the 40 journals with the most citations to provide the visualization shown in Fig. 3. This shows the most cited journals for SDSS grouped into clusters based on their common citation. In this visualization, we used three clusters, with many of the most cited journals found in the centrally positioned cluster. The most cited journal in Scopus is IJGIS, which is located near the center of the figure. In general, centrally placed journals provide modeling and technical approaches, EJOR is a good example. SDSS applications are more peripheral in the figure, with those on the left being predominantly from planning and geography and those on the right side from environmental domains.

Social network analysis uses many ideas from Freeman [61] and these algorithms have been used in bibliographic analysis [62] and are now included in citation analysis tools. “Betweenness” is a measure of how often a node, a journal, book or paper in bibliographic analysis, is located on the shortest path between other nodes in the network. A paper or journal with high betweenness is located on multiple shortest paths and can be characterized as linking two groups in the network. In general, nodes with significant numbers of citations and with higher betweenness scores represent papers, authors or journals which play an important role in connecting diferent parts of the network. If $\mathbf { g _ { j k } }$ is defined as the number of geodesic paths between j and $k ,$ and $g _ { \mathrm { j i k } }$ is the number of these geodesics that pass through i, then node i's betweenness centrality is defined as

$$
\sum_ {j} \sum_ {k} \frac {g _ {j i k}}{g _ {j k}} i \neq j \neq k
$$

Betweenness is usually normalized to reflect the size of the network. A paper cited by other papers, which did not cite papers in common, could have a betweenness score of 1. While this value would not arise in practice, a higher betweenness score for the subset of papers examined would indicate that a paper served to connect other papers in that subset.

“Closeness centrality” is a measure of the distance of a node from all other nodes in the network, this too is usually normalized. $C _ { c } ( n _ { i } )$ is the closeness centrality of node i where d(n , n ) is the distance between two vertices in the network.

$$
C _ {c} (n _ {i}) = \sum_ {j = 1} ^ {g} \left[ \frac {1}{\mathrm{d} (n _ {i} , n _ {j})} \right]
$$

Centrality measures have been used in social network analysis [63], and to some extent in citation analysis. Choi, Yi and Lee [64] analyzed keyword networks in MIS journals, including Decision Support Systems, using centrality measures. A recent paper used co-citation networks and centrality measures to characterize the cloud computing literature and emphasized the importance of betweenness [65]. Leydesdorf [62] examined all WOS journals using these measures, he found a wide var iation in the measures for diferent journals, with Decision Support Systems being close to the median for both betweenness and closeness centrality, but with IJGIS having a betweenness score above the median, suggesting that IJGIS serves to link diferent research communities.

![](/api/attachments/5C8UMDZE/fulltext/images/fe9d097a76ca7387a80e979e332b9f0d6d5b28e985bf5895d607794cfd59adef.jpg)  
Fig. 3. SDSS key journals in Scopus visualized in Vosviewer.

Table 4  
Most often cited journals by SDSS journal articles in Scopus.

<table><tr><td>Citations</td><td>Closeness</td><td>Betweenness</td><td>Journal</td></tr><tr><td>823</td><td>0.631006</td><td>0.019133</td><td>International Journal of Geographical Info Science</td></tr><tr><td>457</td><td>0.590832</td><td>0.008018</td><td>Journal of Environmental Management</td></tr><tr><td>423</td><td>0.583147</td><td>0.006845</td><td>Environmental Modelling &amp; Software</td></tr><tr><td>352</td><td>0.566709</td><td>0.008755</td><td>Euro Journal of Operational Research</td></tr><tr><td>320</td><td>0.560623</td><td>0.004306</td><td>Transactions in GIS</td></tr><tr><td>315</td><td>0.564695</td><td>0.013041</td><td>Computers &amp; Geosciences</td></tr><tr><td>283</td><td>0.549804</td><td>0.000105</td><td>Decision Support Systems</td></tr><tr><td>279</td><td>0.538580</td><td>0.001226</td><td>Environment and Planning B</td></tr><tr><td>277</td><td>0.562955</td><td>0.004637</td><td>Ecological Modelling</td></tr><tr><td>276</td><td>0.544824</td><td>0.002689</td><td>Landscape &amp; Urban Planning</td></tr><tr><td>263</td><td>0.550736</td><td>0.000863</td><td>Annals of the Assoc of American Geographers</td></tr></table>

Leydesdorf undertook subsequent research to show that IJGIS and the Environment and Planning B journals served to link the spatial dis ciplines with computer science journals [66]. Table 4 shows the clo seness and betweenness scores for the journals most often cited by SDSS journal articles in Scopus. IJGIS has both a high closeness centrality score, reflecting its centrality in SDSS and a high betweenness score reflecting that it connects papers not otherwise connected. The central place of IJGIS for SDSS literature comes from its positioning at the confluence of fundamental research in Geoinformatics and Geographic Information Science and topical applied research in SDSS domains such as environmental management, geo-hazard modeling, and location analysis.

## 3.3. Cross-fertilization between DSS and SDSS

We reviewed the abstracts of papers published between 2014 and 2018 in selected DSS, OR/MS and GI (Geographic Information) journals to examine whether the technologies, methods, and DSS application areas reported in DSS and OR-MS journals in the recent years have been adopted in SDSS, and vice-versa whether DSS papers are using geospatial data. For the GI journals, we selected papers citing Decision Support Systems or the European Journal of Operational Research (EJOR), as these are the two most often cited journals from DSS or OR/MS (Table 4). For the DSS and OR/MS fields we selected papers with a GI keyword from the business and OR/MS research fields in WOS.

To select the body of relevant papers (abstracts) we started with a broad list of journals that have published papers in one or more of three “geo-related” research areas listed in WOS [Geography, Physical Geography, Geology] and selected those papers that cite either Decision Support Systems or EJOR. We then narrowed down the set of selected papers by searching with the following keywords: (“geographic information” or “geographical information”) or (map and spatial) or GIS or (location and spatial). These keywords do not include “DSS” or “decision” so represent a broader search than in Table 1 and consequently the search provided some papers that were not strictly DSS. This resulted in the subset of 163 GI papers published between 2014 and 2018 citing DSS or EJOR papers. We also searched using these keywords in the WOS OR/MS and Business Economics research areas and selected those journals in the DSS field with more than one paper in the 2014–2018 period resulting in a set of 88 papers. The journals with most papers were Expert Systems with Applications, Decision Support Systems, Transportation Research Part A, and EJOR.

The abstracts of papers in GI related journals, citing DSS and OR/MS papers, show trends in the adoption of developments in DSS and OR/ MS mostly in methods and technology, and much less in conceptual frameworks. In the area of methods, the developments in social network data mining have been applied to derive spatio-temporal association patterns. OR/MS-based optimization algorithms have been adopted to develop heuristics combining the space-time characteristics of decision space (e.g. a space-time feature guided search), and spatial optimization algorithms aimed at achieving more eficient solutions of NP-hard spatial optimization problems. Some of these algorithms are hybrid techniques incorporating spatial structure information into metaheuristics. In the area of technology, techniques from Web-based DSS have been adopted for developing GI-based systems with near-real time data and event simulation capabilities (in natural disaster events: floods, fires).

The abstracts of the papers in DSS related journals with GI related keywords show two trends in the use of spatial data and algorithms. First, new algorithms for traditional routing and location problems, some of them developed by spatial modelers, are employed by DSS researchers in new problems reflecting current environmental concerns. The examples include locating renewable energy and recycling facilities, modeling of bicycle sharing and bicycle routes, and modeling of drone fly paths for data collection and monitoring. Second, locationbased systems are of increasing importance. New applications increasingly exploit spatial data found in social media, with the identification of points of interest from the aggregate behavior of large numbers of people.

There are also trends found in the reviewed abstracts that point to developments in SDSS emerging in relative isolation from the larger field of DSS/OR-MS. They include geovisual analytics combining data mining with interactive visualization, the use of VGI (volunteered geospatial information) in predictive analytics (e.g., in public health) and in location-based recommending systems combining VGI with social media data, and new SDSS applications in environmental and health domains (e.g., selection of suitable sites for marine energy farms, planning of staging sites for drones with medical equipment supplies). In summary, the flow from the larger field of DSS into a smaller field of SDSS has been limited to OR methods, primarily optimization algorithms “spatialized” in SDSS, and to MS-adopted technologies, primarily Web-based real-time decision support, extended to emergency response applications in SDSS. The flow in the opposite direction, from SDSS to DSS, has been marked by the recognition of location and time as two essential characteristics of entities, events, and phenomena traditionally captured by DSS applications.

## 3.4. Citation structure of SDSS research on WOS

CitNetExplorer [14] is a software tool for visualizing and analyzing citation networks of scientific publications, using data downloaded from the WOS. CitNetExplorer focuses on citation networks of individual publications, as distinct from aggregated networks of particular authors or journals. CitNetExplorer allows citation networks to be explored interactively, for instance by drilling down into a network and by identifying clusters of closely related publications. The visual representation of CitNetExplorer is one of its greatest strengths, as it retains the sense of time and of citation to earlier works. For publications in WOS, CitNetExplorer can show both citations by the paper (citing papers) and citations of the paper (cited papers). For publications not in WOS, CitNetExplorer can only show citations to that paper from pub lications that do appear in WOS, but not citations from that paper.

The CitNetExplorer visualization of the 50 most cited publications in WOS is shown in Fig. 4 with early cited papers shown at the top of the figure. Simon [67] and Sprague and Carlson [68] are important seminal works that would be expected in any discussion of DSS. Likewise, the articles by Zadeh [69], Keeney and Raifa [70], and the article and book by Saaty [71,72] represent decision-making approaches widely cited in DSS. Multi-criteria analysis (MCA), also known as multi criteria decision analysis (MCDA), and multi-criteria decision-making (MCDM), represents an important approach in DSS. Voogd [73] represents a well-cited book applying MCA decision techniques to planning, a specific domain of relevance to SDSS. Cowen [74] was an important paper defining the decision support nature of GIS. Armstrong and Densham [75] and Densham [3] represent key papers that in troduced the SDSS concept in a way founded on the definitions of DSS established in the earlier DSS literature. Consequently, the many papers that have drawn on these works use a characterization of SDSS familiar to anyone from the DSS field. All of these influential early papers appeared in GIS-related publications, the traditional DSS field paid little attention to SDSS until the publication of Crossland, Wynne, and Perkins [76]. MCA represents the largest class of modeling approaches used in SDSS, substantially influenced by the widely cited pre-GIS book by Voogd [73] and the later book by Malczewski [77]. A later review by Malczewski [78] indicated that most systems were concerned with land suitability problems, site search/selection problems or resource allo cation problems. A recent review in the area noted the importance of MCA for SDSS, and also the challenges of integrating complex spatial data with MCA methods [79].

![](/api/attachments/5C8UMDZE/fulltext/images/c6f5b4763b7284270cd76aa936d64057a9e9b85070056dc2ba817d1a96f232d8.jpg)  
Fig. 4. Key SDSS publications in WOS represented in CitNetExplorer.

CitNetExplorer also allows a drill-down facility to investigate parts of the citation network. Fig. 5 shows the papers citing the important paper by Crossland, Wynne, and Perkins [76], which served to introduce the journals also related to the traditional DSS field, for instance Decision Support Systems [48,80] or Transportation Research: Part C, to the SDSS field [81,82]. However, these works were then cited in a wider range of publications, reflecting the increasing representation of

SDSS publication in journals other than those where DSS publications are traditionally found.

## 3.5. Key papers in SDSS research

We used Pajek [22] to perform network analysis on a DCA network exported from Vosviewer. This allowed the identification of the key papers and books cited in WOS. This analysis shown in Table 5, illustrates the importance of MCA papers in SDSS, which serve to link different SDSS subdomains and so have high betweenness scores. The MCA group includes papers by Carver [83], Jankowski [84], Malczewski [78] and Saaty [71] and the books by Saaty [72], Voogd [73] and Malczewski [77]. The papers by Densham [3] and Crossland, Wynne, and Perkins [76] are important papers linking SDSS to the DSS literature. It is notable that work by Saaty with no spatial content plays such a central role in SDSS literature.

## 4. Links between SDSS and the broader DSS field

## 4.1. SDSS within the DSS field

SDSS is still finding new areas of application and there is an evolution of initial systems built in new application domains analogous to that which took place in business domains in the past. However, SDSS does present complex and novel problems and systems which can contribute to the development of the DSS field in general. In particular, emergency and disaster response SDSS area is a frontier of DSS application which illustrates how spatial techniques can allow richer modeling of long-established problems. These are advanced systems, which must support urgent decisions in often complex situations. Public participation systems represent an extension of the group decision support system (GDSS) concept to the general public and are an important extension of GDSS. Public participation systems illustrate how SDSS techniques open new areas of decision-making and extend DSS to a wider set of decision-makers.

![](/api/attachments/5C8UMDZE/fulltext/images/6399efdb15f46cd0b20b42ae319687188cf4a432ef0bbdb59fee48de06e446e2.jpg)  
Fig. 5. SDSS papers in WOS citing Crossland, Wynne, and Perkins [76].

Table 5  
Key papers and books cited by SDSS papers in journals the Web of Science, Core Collection 1990–2015.

<table><tr><td>Citations</td><td>Closeness</td><td>Betweenness</td><td>Paper</td></tr><tr><td>96</td><td>0.4811</td><td>0.1567</td><td>Malczewski [77].</td></tr><tr><td>63</td><td>0.4449</td><td>0.0649</td><td>Saaty [72]</td></tr><tr><td>54</td><td>0.4461</td><td>0.0514</td><td>Carver [83]</td></tr><tr><td>46</td><td>0.4405</td><td>0.0744</td><td>Densham [3]</td></tr><tr><td>43</td><td>0.4383</td><td>0.0260</td><td>Jankowski [84]</td></tr><tr><td>39</td><td>0.4305</td><td>0.0289</td><td>Malczewski [78]</td></tr><tr><td>34</td><td>0.4173</td><td>0.0198</td><td>Malczewski [85]</td></tr><tr><td>32</td><td>0.4124</td><td>0.0296</td><td>Crossland, Wynne &amp; Perkins [76]</td></tr><tr><td>32</td><td>0.4027</td><td>0.0136</td><td>Saaty [71]</td></tr><tr><td>31</td><td>0.4092</td><td>0.0137</td><td>Voogd [73]</td></tr></table>

## 4.2. Emergency and disaster response

Emergency and disaster response represent an area of SDSS appli cation that illustrates the value of the integration of GIS technologie and spatial data with a wide range of modeling approaches [86]. Such problems represent a leading edge of DSS application, owing to the life or death nature of the issues that arise, the urgency of the problems, the complexity of the modeling required and consequentially the data re quired for this modeling, and the challenge of making these powerful techniques available in a way that is easily controlled by the decisionmaker. Given the importance of emergency applications, SDSS has been used for these applications since the late 1980s. For instance, an in fluential early example of integration between modeling drawn from

OR/MS and GIS was concerned with modeling emergency evacuation [87].

Decision support takes on multiple potential roles, including plan ning in anticipation of possible adverse events, evacuation, the dispatch of emergency equipment and materials, and the restoration of damaged facilities. Almost all emergency situations have a clear spatial component and a role for SDSS including: volcanic eruptions [88], floods [89], tsunami [90], forest fire [91], marine rescue [92], wind [93], and earthquake [94]. Emergency response applications integrate diferent forms of spatial data and the sourcing and representation of that data is an important design characteristic of such systems. The timely availability of spatial data is critical, requiring both advanced planning in the provision of appropriate SDI data [95] and the use of crowdsourcing and real-time data collection to augment or update existing data [96]. In addition to the challenges of DSS generally, emergency SDSS faces additional limitations imposed by computer performance and spatial data availability. Advance planning SDSS can use computationally in tensive models as execution time is less urgent, while real-time response SDSS [97] may need updated spatial data and requires the ability to process that data quickly. Over time, these limitations are being overcome as technology improves and more data is collected, although a process of assessment of new spatial data sources is needed if users are to have confidence in its use in an emergency situation [98]. Emergency response support requires spatial data sharing between organizations and also represents a challenging GDSS application [99].

However, richer sources of data and increased complexity only in crease the decision-support challenge of presenting information in a way that reflects the needs of decision-makers, rather than the perspective of system designers or those who collected the data. Emergency systems require rapid decision making, and the clarity of information display plays a huge role in their success. In order to effectively support complex spatial decision-making, SDSS must provide rich problem representations, including the use of dashboards with multiple GIS layers linked with graphs, tables, and text and/or 3D visualization [35] to inform multiple decision-makers. In addition, specialist decision-makers must also be able to efectively interact with the interface to direct the system to meet their decision needs [100]. These divergent requirements of problem representation and system interaction pose serious challenges for SDSS interface designers.

## 4.3. Public participation SDSS

GDSS has sought to use technology to support decisions by multiple decision-makers, with the objective of achieving better decisions, increasing participation and improving group confidence in the decision [101]. While earlier GDSS research in the mid-1980s largely concentrated on decision rooms, researchers envisaged a future in which people with common afiliations might use electronic communication as a medium for decision making [102] and improvements in technology such as ubiquitous mobile data devices and cloud computing have greatly facilitated this. Residents of a geographic region will have a real interest in decisions made afecting that region, especially in the planning domain. However, any decision process may bring together people from quite diferent social and educational backgrounds, and this diversity poses a challenge to software supporting that decision process. Consequently, public participation SDSS represents a demanding and advanced application of GDSS principles which typically evolved in more homogeneous single organizational context where users had more in common with each other.

When appropriate technology became available, SDSS quickly formed a branch called Group SDSS, where multiple users could interact in the decision-making process [52]. The technical challenges of single user SDSS were multiplied in Group SDSS, and so technology needed to advance further for some ideas to fully develop. Given that spatial decision-making often afected people located throughout a district, there was immediate interest in the potential of the Internet to involve the public in spatial decision making [53]. While same location SDSS tools continue to have a role in exploiting new technology and new representations [103], public participation systems represent a distinctive and important contribution of SDSS to the DSS field generally. This is because they extend GDSS to the public, who have a stake in the solution and so bring the benefits of place-specific knowledge and improved participation which characterize GDSS [104]. As is generally true for GDSS, these systems do not expose their users to complex modeling, but focus on collecting communal preferences for the decision alternatives and articulating trade-ofs [105].

Recent group SDSS examples include the Web-based applications called geo-questionnaire and geo-discussion, in which questions and structured online discussion are coupled with an interactive map for the purpose of collecting data on people's preferences concerning current and/or future conditions. Web-based applications involving partici pating public have been developed in domains such as transportation, environmental management, and urban planning [106]. In these ap plications, land development preferences expressed by the participating public are accompanied by an interactive map providing users with a rich geographical context and the functionality to mark a location or a spatial footprint corresponding to a stated preference. Spatial attributes are collected through sketching features on an interactive map. Each geographical feature may also be linked with questions about a feature's attributes (e.g. its urban function or land use type) and answers contributed by a respondent in a pop-up dialog. Answers and marked/ sketched features are visible to other respondents. The respondents can switch between diferent thematic map layers and query map objects. In addition to the map and the spatial features, the input of other non spatial data not directly linked with the map is facilitated by slider bars, single- and multiple-choice questions, and open-ended questions. This type of application requires the representation of the decision problem in a format suitable for the public who may have had no training in spatial representations, so the range of skills in such a group is likely larger than usually associated with GDSS. Web-based applications, such as the one described in [106], broaden the concept of group SDSS from an expert-based problem solving to a crowd-sourcing of geo-referenced preferences that might be considered in a problem solution. The key issue in SDSS open to public participation is the need to evaluate SDSS outcomes and to provide evidence of success.

## 4.4. Links with DSS literature

The early work on SDSS, for instance Armstrong, Densham, & Rushton [107] and Densham [3], contained strong links to earlier DSS literature. Many subsequent SDSS papers cited these foundation works rather than linking to the contemporaneous DSS literature directly. This reflects a tendency for early papers in a subdomain to act as ‘bridge works introducing the concept of DSS and for later authors in that domain to look mainly to such ‘bridge’ works in their own domain rather than the overall DSS field [58]. While modern databases like WOS and Scopus, and search provided by Google tools, would be expected to expose authors to a wide range of papers outside their own sub-domain, people still see a greater relevance in examples from their own discipline and are more likely to refer to a paper within their own dis cipline than a DSS paper from another field. The concern is that reference to an early ‘bridging’ publication in a discipline may mean that newer developments in the DSS field are not fully recognized in that domain.

New subdomains have typically seen rapid growth in SDSS when advancing technical performance and better data availability come together to make systems economically feasible in that subdomain. The early period of SDSS use in a subdomain often sees an important paper providing a bridging role from existing SDSS literature outside that domain. A higher score for betweenness centrality, discussed above, is one indicator that a paper may be performing a bridging function. In SDSS, one example is Hill et al. [108] which discusses the use of MCA in SDSS in an environmental context. This paper cites a wide literature, including multiple articles in EJOR and IJGIS, and brings concepts from this literature to the environmental domain, where it is predominantly cited.

The fragmentation of DSS is a known phenomenon, Arnott and Pervan [114,119] noted the fragmentation of DSS into subfields and noted the conservative nature of DSS research and the slow dissemination of new decision theories in the field. With the fragmentation of DSS applications, there is a danger that core DSS concepts will be largely invisible to those working in the subfields, in this case, SDSS. There is a further danger that fragmentation within SDSS field itself will slow the transmission of concepts drawn from the core DSS discipline. There is also a danger that interesting work of value in the diverse application areas will fail to inform the DSS field generally, for instance, the examples of emergency response and public participation systems discussed in this paper.

Arnott and Pervan [54] suggested that the DSS field was increasingly influenced by the work of Kahneman and Tversky [109,110], in addition to the earlier work of Simon [67]. While Simon's work clearly influenced the early researchers in SDSS, and in turn influenced the many SDSS articles that refer to early SDSS articles, there is little evidence of substantial influence on the SDSS field from the Kahneman and Tyersky theory. Arnott and Pervan noted that Design Science had become important in the DSS field in the period 2003–2010 and argued for its role as a research strategy for SDSS. However, citation databases currently show little influence by Design Science in the SDSS field, with few SDSS papers, other than from the IS field, citing of the seminal Design Science paper by March and Smith [111]. However, recent citations show some evidence of influence by Design Science in SDSS, for instance, Goodspeed [112] and Ran and Nedović-Budić [113].

The concept of SDSS has had a limited influence on mainstream DSS literature. In a review of the DSS field, Arnott and Pervan [114] noted the fragmentation of the field and identified a framework to link subfields of DSS, but did not mention spatial applications. Vizecky and El-Gayar [115] extended Arnott and Pervan's framework to include both GIS and SDSS. Hosack et al. [116] briefly mentioned GIS, without substantial discussion of its relationship with DSS, and argued for the role of mobile computing in Arnott and Pervan's framework. In a later paper, Arnott and Pervan [54] added Business Analytics to their earlier framework but did not respond to Vizecky and El-Gayar's point. Responding to Hosack et al. [116], they suggested that mobile computing was not a distinct DSS type in their framework. However, neither linked mobile DSS to location-based systems as we do here in Fig. 1. Even a review of mobile DSS emphasized the convenience and 24/7 nature of mobile systems, but only a single reference to the concept of location [117]. However, some DSS researchers do recognize the role of spatial systems, for instance, Power and Sharda [118] did give some examples of SDSS in their review of model-driven DSS. The recent special issue on location analytics and decision support in the Decision Support Systems journal (Vol. 99, 2017) will hopefully facilitate greater cross-fertiliza tion between SDSS and the DSS field generally [42].

## 5. Conclusion

At the start of the three decades discussed in this paper, SDSS was technically challenging to build and spatial applications were only beginning to move toward decision support, as less computationally demanding business applications had already done a decade or more previously. The pioneer researchers in SDSS looked to existing DSS research for the key concepts of decision support and adapted these concepts to SDSS. From that time, SDSS developed quickly as various technical requirements fell into place. In particular, SDSS benefited from the greater public availability of spatial data and the more flexible software, which made it easier to integrate modeling into GIS. SDSS users initially came from two starting points; some users were DSS users who included the use of spatial techniques in their systems, while other SDSS users were GIS users who added decision-making functionality. However, as time has gone by, new communities have started to use spatial data and take advantage of new technologies, initially in relatively simple SDSS applications and later in more complex systems. This extension of SDSS use is particularly notable in ecological disciplines, which are a growing area of DSS application [58], and a substantial proportion of these new cases are spatial applications. However, there has been much less influence of SDSS in medical disciplines, which are also an important area of DSS application growth.

This paper has examined the bibliographic structure of SDSS papers in WOS and Scopus, using modern techniques that have not been used previously in this domain. This reveals a surprisingly fragmented picture. Although applications with spatial element have come to account for up to half of DSS applications, there has been little discussion of SDSS in the mainstream DSS literature. While SDSS started with a solid base in the earlier seminal DSS literature, the rapidly expanding literature since then has had limited links to the DSS literature and new areas of SDSS application often have limited links to either the DSS or GIS literature. While fragmentation has always occurred in DSS, the diverse range of disciplines where SDSS is now used aggravates the disconnection. This fragmentation means that new decision-making concepts may be slow to disseminate and innovations in one subdomain may remain unknown elsewhere. Consequently, we see a need for more research interaction between the DSS and SDSS communities, to the mutual benefit of both.

## References

[1] P. Jankowski, Spatial decision support systems, in: K.K. Kemp (Ed.), Encyclopedi of Geographic Information Science, SAGE Publications, Inc., Thousand Oaks, California, 2008, http://sk.sagepub.com/reference/geoinfoscience

[2] L.D. Hopkins, M.P. Armstrong, Analytic and cartographic data storage: a twotiered approach to spatial decision support systems, Proceedings, Seventh International Symposium on Computer-assisted Cartography, American Congress

on Surveying and Mapping, Washington, DC, 1985.

[3] P.J. Densham, Spatial decision support systems, in: D.J. Maguire, M.F. Goodchild, D.W. Rhind (Eds.), Geographical Information Systems, Volume 1: Principles, Longman Scientific & Technical, Harlow, Essex, 1991, pp. 403–412.

[4] D.J. Maguire, M.F. Goodchild, D.W. Rhind, Geographical Information Systems: Principles, Techniques, Management and Applications, Longman Scientific & Technical, Harlow, Essex, 1991

[5] R. Sugumaran, J. Degroote, Spatial Decision Support Systems, CRC Press, Boca Raton, FL, USA, 2011.

[6] W.B. Locander, H.A. Napier, R.W. Scamell, A team approach to managing the development of a decision support system, MIS Quarterly 3 (1979) 53–63

[7] M.F. Goodchild, Citizens as sensors: the world of volunteered geography, GeoJournal 69 (2007) 211–221

[8] M. Haklay, How good is volunteered geographical information? A comparative study of OpenStreetMap and Ordnance Survey datasets, Environment and Planning. B. Planning & Design 37 (2010) 682–703.

[9] H. Small, Visualizing science by citation mapping, Journal of the Association for Information Science and Technology 50 (1999) 799.

[10] L. Leydesdorf, I. Rafols, Interactive overlays: a new method for generating global journal maps from web-of-science data, Journal of Informetrics 6 (2012) 318–332.

[11] L. Leydesdorf, I. Rafols, C. Chen, Interactive overlays of journals and the measurement of interdisciplinarity on the basis of aggregated journal–journal cita tions, Journal of the American Society for Information Science and Technology 64 (2013) 2573–2586.

[12] L. Leydesdorf, F. de Moya-Anegón, W. de Nooy, Aggregated journal–journal citation relations in scopus and web of science matched and compared in terms of networks, maps, and interactive overlays, Journal of the Association for Information Science and Technology 67 (2016) 2194–2211

[13] N.J. van Eck, L. Waltman, Software survey: VOSviewer, a computer program for bibliometric mapping, Scientometrics 84 (2010) 523–538.

[14] N.J. van Eck, L. Waltman, CitNetExplorer: a new software tool for analyzing and visualizing citation networks, Journal of Informetrics 8 (2014) 802–823.

[16] D.J. de Solla Price, Networks of scientific papers, Science 149 (1965) 510–515.

[17] J. Scott, Social Network Analysis, Sage, Los Angeles, 2017

[18] H. Small, Co-citation in the scientific literature: a new measure of the relationship between two documents, Journal of the American Society for Information Science 24 (1973)265–269.

[19] H. Small, Co-citation context analysis and the structure of paradigms, Journal of Documentation 36 (1980).183–196

[20] K.W. McCain, Mapping economics through the journal literature: an experiment in journal cocitation analysis, Journal of the American Society for Information Science 42 (1991) 290–296

[21] C. Chen, CiteSpace: visualizing patterns and trends in scientific literature, http:/ cluster.cis.drexel.edu/\~cchen/citespace/, (2016).

[22] A. Mrvar, V. Batagelj, Analysis and visualization of large networks with program package Pajek, Complex Adaptive Systems Modeling 4 (2016) 6.

[23] A. Thor, W. Marx, L. Leydesdorf, L. Bornmann, Introducing CitedReferencesExplorer (CRExplorer): a program for reference publication year spectroscopy with cited references standardization, Journal of Informetrics 10 (2016) 503–515.

[24] R.R. Sengupta, D.A. Bennett, Agent-based modelling environment for spatial decision support, International Journal of Geographical Information Science 17 (2003).157–180.

[25] S. Steiniger, A.J. Hunter, The 2012 free and open source GIS software map–a guide to facilitate research. development. and adoption. Computers. Environment and Urban Systems 39 (2013) 136–150.

[26] C. Rinner, Web-based spatial decision support: status and research directions, Journal of Geographic Information and Decision Analysis 7 (2003) 14–31

[27] E.W.T. Ngai, T.K.P. Leung, Y.H. Wong, M.C.M. Lee, P.Y.F. Chai, Y.S. Choi, Design and development of a context-aware decision support system for real-time accident handling in logistics. Decision Support Systems 52 (2012) 816–827

[28] S.Y. Ho. The effects of location personalization on individuals' intention to use mobile services, Decision Support Systems 53 (2012) 802–812

[29] K. Sood, S. Singh, R.S. Rana, A. Rana, V. Kalia, A. Kaushal, Application of GIS in precision agriculture, National Seminar on Precision Farming Technologies for High Himalayas, High Mountain Arid Agriculture Research Institute, Ladakh, India, 2015, pp. 8–16.

[30] P.B. Keenan, Cloud computing and DSS: the case of spatial DSS, Internationa Journal of Information and Decision Sciences 5 (2013) 283–294

[31] P. Yue, H. Zhou, J. Gong, L. Hu, Geoprocessing in cloud computing platforms–a comparative analysis, International Journal of Digital Earth 6 (2013) 404–425.

[32] D. Bačić, A. Fadlalla, Business information visualization intellectual contributions: an integrative framework of visualization capabilities and dimensions of visual intelligence. Decision Support Systems 89 (2016) 77–86

[33] S. Jarupathirun. E.M. Zahedi. Exploring the influence of perceptual factors in the success of web-based spatial DSS. Decision Support Systems 43 (2007) 933–951.

[34] A.C. Robinson, U. Demšar, A.B. Moore, A. Buckley, B. Jiang, K. Field, M.-J. Kraak, S.P. Camboim, C.R. Sluter, Geospatial big data and cartography: research challenges and opportunities for making maps that matter, International Journal of Cartography 3 (2017) 32–60.

[35] G. Andrienko, N. Andrienko, P. Jankowski, D. Keim, M.J. Kraak, A. MacEachren, S. Wrobel, Geovisual analytics for spatial decision support: setting the research agenda, International Journal of Geographical Information Science 21 (2007) 839–857.

[36] M.A. Erskine, D.G. Gregg, J. Karimi, J.E. Scott, Business decision-making using geospatial data: a research framework and literature review, Axioms 3 (2013) 10–30.

[37] E. Dessers, G. Vancauwenberghe, D. Vandenbroucke, J. Crompvoets, G. Van Hootegem, Analysing spatial data performance in inter-organisational processes, International Journal of Digital Earth 8 (2015) 403–420.

[38] M.F. Goodchild, Perspectives on the new cartography, Environment and Planning A 47 (2015) 1341–1345

[39] M.F. Goodchild, L. Li, Assuring the quality of volunteered geographic information, Spatial Statistics 1 (2012) 110–120.

[40] C.E.C. Campelo, M. Bertolotto, P. Corcoran, Volunteered geographic information and the future of geospatial data, Advances in Geospatial Technologies (AGT) Book Series, IGI Global, Hershey, PA, 2017.

[41] S. Kisilevich, D. Keim, L. Rokach, A GIS-based decision support system for hotel room rate estimation and temporal price prediction: the hotel brokers' context, Decision Support Systems 54 (2013) 1119–1133.

[42] J.B. Pick, O. Turetken, A.V. Deokar, A. Sarkar, Location analytics and decision support: reflections on recent advancements, a research framework, and the path ahead. Decision Support Systems 99 (2017) 1–8.

[43] H. Cerezo-Costas, A. Fernández-Vilas, M. Martín-Vicente, R. P. Díaz-Redondo, Discovering geo-dependent stories by combining density-based clustering and thread-based aggregation techniques, Expert Systems with Applications 95 (2018) 32–42.

[44] R.M. Chang, R.J. Kaufman, Y. Kwon, Understanding the paradigm shift to computational social science in the presence of big data, Decision Support Systems 63 (2014) 67–80.

[45] N. Andrienko, G. Andrienko, G. Fuchs, P. Jankowski, Scalable and privacy-respectful interactive discovery of place semantics from human mobility traces, Information Visualization 15 (2016) 117–153.

[46] S. Li, S. Dragicevic, F.A. Castro, M. Sester, S. Winter, A. Coltekin, C. Pettit, B. Jiang, J. Haworth, A. Stein, Geospatial big data handling theory and methods: review and research challenges, ISPRS Journal of Photogrammetry and Remote Sensing 115 (2016) 119–133.

[47] R. Kitchin, The Data Revolution: Big Data, Open Data, Data Infrastructures and Their Consequences, Sage, Los Angeles, 2014.

[48] P.B. Keenan, Spatial decision support systems for vehicle routing, Decision Support Systems 22 (1998) 65–71.

[49] C.M. Gold, Forestry spatial decision support system classification, and the ‘flight simulator’ approach, Proceedings GIS'93 Symposium, Vancouver, Canada, 1993, pp. 797–802.

[50] R.L. Church, A.T. Murray, M.A. Figueroa, K.H. Barber, Support system development for forest ecosystem management, European Journal of Operational Research 121 (2000) 247–258

[51] J. Aerts, M. Van Herwijnen, R. Janssen, T. Stewart, Evaluating spatial design techniques for solving land-use allocation problems, Journal of Environmental Planning and Management 48 (2005) 121–142.

[52] M.P. Armstrong, Requirements for the development of GIS-based group decisionsupport systems, Journal of the American Society for Information Science 45 (1994) 669.

[53] P. Jankowski, M. Stasik, Design considerations for space and time distributed collaborative spatial decision making, Journal of Geographic Information and Decision Analysis 1 (1997) 1–9.

[54] D. Arnott, G. Pervan, A critical analysis of decision support systems research revisited: the rise of design science, Journal of Information Technology 29 (2014) 269–293.

[55] S. Eom, The intellectual structure of decision support systems research (1991–2004), in: D. Schuf, D. Paradice, F. Burstein, D.J. Power, R. Sharda (Eds.), Decision Support: An Examination of the DSS Discipline, Springer, New York, 2011, pp. 49–68.

[56] H. Eom, S. Lee, Decision support systems applications research: a bibliography (1971–1988), European Journal of Operational Research 46 (1990) 333–342

[57] S. Eom, All author cocitation analysis and first author cocitation analysis: a comparative empirical investigation, Journal of Informetrics 2 (2008) 53–64.

[58] P. Keenan, Changes in DSS disciplines in the Web of Science, Journal of Decision Systems 25 (2016) 542–549.

[59] E. Næsset, Geographical information systems in long-term forest management and planning with special reference to preservation of biological diversity: a review, Forest Ecology and Management 93 (1997) 121–136.

[60] F. Wei, T.H. Grubesic, B.W. Bishop, Exploring the GIS knowledge domain using CiteSpace, The Professional Geographer 67 (2015) 374–384.

[61] L.C. Freeman, Centrality in social networks conceptual clarification, Socia Networks 1.(1978) 215–239

[62] L. Leydesdorf, Betweenness centrality as an indicator of the interdisciplinarity of scientific journals, Journal of the Association for Information Science and Technology 58 (2007) 1303–1319.

[63] C. Kiss. M. Bichler. Identification of influencers—measuring influence in customer networks, Decision Support Systems 46 (2008) 233–253

[64] J. Choi, S. Yi, K.C. Lee, Analysis of keyword networks in MIS research and implications for predicting knowledge evolution, Information & Management 48 (2011) 371–381.

[65] N. Wang, H. Liang, Y. Jia, S. Ge, Y. Xue, Z. Wang, Cloud computing research in the IS discipline: a citation/co-citation analysis, Decision Support Systems 86 (2016) 35–47.

[66] L. Leydesdorf, Mapping interdisciplinarity at the interfaces between the Science Citation Index and the Social Science Citation Index, Scientometrics 71 (2007) 391–405.

[67] H.A. Simon, The New Science of Management Decision, Harper & Brothers, New York, NY, US, 1960.

[68] R.H. Sprague, E.D. Carlson, Building Efective Decision Support Systems, Prentice Hall International, Englewood Cliffs, N.J., 1982.

[69] L.A. Zadeh, Fuzzy sets, Information and Control 8 (1965) 338–353.

[70] R.L. Keeney, H. Raifa, Decision With Multiple Objectives, Wiley, New York, 1976.

[71] T.L. Saaty, A scaling method for priorities in hierarchical structures, Journal of Mathematical Psychology 15 (1977) 234–281.

[72] T.L. Saaty, The Analytic Hierarchy Process: Planning, Priority Setting, Resources Allocation, McGraw, New York, 1980.

[73] H. Voogd, Multicriteria Evaluation for Urban and Regional Planning, Taylor & Francis, London, 1983

[74] D.J. Cowen, GIS versus CAD versus DBMS: what are the diferences? Photogrammetric Engineering and Remote Sensing 54 (1988) 1551–1555.

[75] A.P. Armstrong, P.J. Densham, Database organization strategies for spatial decision support systems, International Journal of Geographical Information Systems 4 (1990) 3–20.

[76] M.D. Crossland, B.E. Wynne, W.C. Perkins, Spatial decision support systems: an overview of technology and a test of eficacy, Decision Support Systems 14 (1995) 219–235.

[77] J. Malczewski, GIS and Multicriteria Decision Analysis, John Wiley & Sons, New York, 1999.

[78] J. Malczewski, GIS-based multicriteria decision analysis: a survey of the literature, International Journal of Geographical Information Science 20 (2006) 703–726.

[79] V. Ferretti, G. Montibeller, Key challenges and meta-choices in designing and applying multi-criteria spatial decision support systems, Decision Support Systems 84 (2016) 41–52.

[80] V. Maniezzo, I. Mendes, M. Paruccini, Decision support for siting problems, Decision Support Systems 23 (1998) 273–284.

[81] T.L. Nyerges, R. Montejano, C. Oshiro, M. Dadswell, Group-based geographic information systems for transportation improvement site selection, Transportation Research Part C: Emerging Technologies 5 (1997) 349–369

[82] T.A. Arentze, H. Timmermans, A spatial decision support system for retail plan generation and impact assessment, Transportation Research Part C: Emerging Technologies 8 (2000) 361–380.

[83] S.J. Carver, Integrating multi-criteria evaluation with geographical information systems, International Journal of Geographical Information Systems 5 (1991) 321-339.

[84] P. Jankowski, Integrating geographical information systems and multiple criteria decision-making methods, International Journal of Geographical Information Systems 9 (1995) 251–273.

[85] J. Malczewski, GIS-based land-use suitability analysis: a critical overview, Progress in Planning 62 (2004) 3–65.

[86] L. Özdamar, M.A. Ertem, Models, solutions and enabling technologies in humanitarian logistics, European Journal of Operational Research 244 (2015) 55–65.

[87] M. Pidd, R. Eglese, F.N. de Silva, CEMPS: a prototype spatial decision support system to aid in planning emergency evacuations, Transactions in GIS 1 (1996) 321–334.

[88] Jumadi, S. Carver, D. Quincey, SAFE volcano: spatial information framework for volcanic eruption evacuation site selection-allocation, GIS Research UK Conference 2015. Leeds. England. 2015.

[89] O. Rodríguez-Espíndola, P. Albores, C. Brewster, GIS and optimisation: potential benefits for emergency facility location in humanitarian logistics. Geosciences 6 (2016) 18.

[90] F. Ai, L.K. Comfort, Y. Dong, T. Znati, A dynamic decision support system based on geographical information and mobile social networks: a model for tsunami risk mitigation in Padang, Indonesia, Safety Science 90 (2015) 62–74.

[91] A.P. Pacheco, J. Claro, P.M. Fernandes, R. de Neufville, T.M. Oliveira, J.G. Borges, J.C. Rodrigues, Cohesive fire management within an uncertain environment: a review of risk handling and decision support systems, Forest Ecology and Management 347 (2015) 1–17

[92] M. Siliander, E. Venäläinen, F. Goerlandt. P. Pellikka, GIS-based cost distance modelling to support strategic maritime search and rescue planning: a feasibility study, Applied Geography 57 (2015) 54–70.

[93] M.-H. Hsu, A.S. Chen, L.-C. Chen, C.-S. Lee, F.-T. Lin, C.-J. Huang, A GIS-based decision support system for typhoon emergency response in Taiwan, Geotechnical and Geological Engineering 29 (2011) 7–12.

[94] M. Pollino, G. Fattoruso, A.B. Della Rocca, L. La Porta, S.L. Curzio, A. Arolchi, V. James, C. Pascale, An open source GIS system for earthquake early warning and post-event emergency management, International Conference on Computational Science and Its Applications, Springer, 2011, pp. 376–391.

[95] W. Li, M. Song, B. Zhou, K. Cao, S. Gao, Performance improvement techniques for geospatial web services in a cyberinfrastructure environment–a case study with a disaster management portal, Computers, Environment and Urban Systems 54 (2015) 314–325.

[96] F.E. Horita, J.P. de Albuquerque, L.C. Degrossi, E.M. Mendiondo, J. Ueyama, Development of a spatial decision support system for flood risk management in Brazil that combines volunteered geographic information with wireless sensor networks, Computers & Geosciences 80 (2015) 84–94

[97] A. Zerger, D. Ingle-Smith, Impediments to using GIS for real-time disaster decision support, Computers, Environment and Urban Systems 27 (2003) 123–141.

[98] M. Eckle, J. Porto de Albuquerque, B. Herfort, R. Wolf, A. Zipf, R. Leiner, C. Jacobs, Leveraging OpenStreetMap to support flood risk management in mu nicipalities: a prototype decision support system, in: A.H. Tapia, P. Antunes, V.A. Bañuls, K. Moore, J. Porto de Albuquerque (Eds.), 13th International Conference on Information Systems for Crisis Response and Management ISCRAM

2016, Rio de Janeiro, Brazil, 2016 http://wrap.warwick.ac.uk/78697.

[99] J. Breen Joseph, R. Parrish David, GIS in emergency management cultures: an empirical approach to understanding inter- and intra-agency communication during emergencies, Journal of Homeland Security and Emergency Managemen 10 (2013) 477.

[100] M. Shen, M. Carswell, R. Santhanam, K. Bailey, Emergency management information systems: could decision makers be supported in choosing display formats? Decision Support Systems 52 (2012) 318–330.

[101] G. DeSanctis, B. Gallupe, Group decision support systems: a new frontier, ACM SIGMIS Database 16 (1984) 3–10.

[102] G. Desanctis, R.B. Gallupe, A foundation for the study of group decision support systems, Management Science 33 (1987) 589–609.

[103] N. Ploskas, I. Athanasiadis, J. Papathanasiou, N. Samaras, An interactive spatial decision support system enabling co-located collaboration using tangible user in terfaces for the multiple capacitated facility location problem, International Journal of Decision Support System Technology (IJDSST) 7 (2015) 15–28

[104] P. Jankowski, T.L. Nyerges, Geographic Information Systems for Group Decision Making: Towards a Participatory, Geographic Information Science, Taylor & Francis. London. 2001.

[105] S. Balram, Collaborative Geographic Information Systems, IGI Global, Hershey, PA, 2006.

[106] P. Jankowski, M. Czepkiewicz, M. Młodkowski, Z. Zwoliński, Geo-questionnaire: a method and tool for public preference elicitation in land use planning, Transactions in GIS 20 (2016) 903–924.

[107] M.P. Armstrong, P.J. Densham, G. Rushton, Architecture for a microcomputer based spatial decision support system, Second International Symposium on Spatia Data Handling, Int. Geogr. Union, 1986, pp. 120–130.

[108] M.J. Hill, R. Braaten, S.M. Veitch, B.G. Lees, S. Sharma, Multi-criteria decision analysis in spatial decision support: the ASSESS analytic hierarchy process and the role of quantitative methods and spatially explicit analysis, Environmental Modelling & Software 20 (2005) 955–976.

[109] D. Kahneman, A. Tversky, Choices, values, and frames, American Psychologist 39 (1984) 341–350.

[110] A. Tversky, D. Kahneman, The framing of decisions and the psychology of choice, Environmental Impact Assessment, Technology Assessment, and Risk Analysis, Springer, 1985, pp. 107–129.

[111] S.T. March, G.F. Smith, Design and natural science research on information

technology, Decision Support Systems 15 (1995) 251–266

[112] R. Goodspeed, Sketching and learning: a planning support system field study, Environment and Planning. B, Planning & Design (3) (2016) 444–463.

[113] J. Ran, Z. Nedovic-Budic, Integrating spatial planning and flood risk management: a new conceptual framework for the spatially integrated policy infrastructure, Computers, Environment and Urban Systems 57 (2016) 68–79.

[114] D. Arnott, G. Pervan, A critical analysis of decision support systems research, Journal of Information Technology 20 (2005) 67–87.

[115] K. Vizecky, O. El-Gayar, Increasing research relevance in DSS: looking forward by reflecting on 40 years of progress, 44th Hawaii International Conference on System Sciences (HICSS), IEEE, Kauai, Hawaii, USA, 2011, pp. 1–9.

[116] B. Hosack, D. Hall, D. Paradice, J.F. Courtney, A look toward the future: decision support systems research is alive and well, Journal of the Association for Information Systems 13 (2012) 315–340

[117] S. Gao, Mobile decision support systems research: a literature analysis, Journal of Decision Systems 22 (2013) 10–27.

[118] D.J. Power, R. Sharda, Model-driven decision support systems: concepts and re search directions, Decision Support Systems 43 (2007) 1044–1061.

[119] D. Arnott, G. Pervan, Eight key issues for the decision support systems discipline, Decis. Support. Syst. 44 (3) (2008) 657–672.

Peter Bernard Keenan holds a PhD in Management Science from University College Dublin. He is associate Professor in the Centre for Business Analytics in the UCD Business School, and former Head of the Management Information Systems Subject area. His research interests include decision support for routing problems, the integration of geographic information systems (GIS) and decision support systems and the use of GIS in business.

Piotr Jankowski earned his PhD from the University of Washington. He is currently a professor and the chair of the Department of Geography at San Diego State University. His research focuses on spatial decision support systems, participatory geographic information systems, and sensitivity analysis in spatial models. He is an author of over 90 peerreviewed journal papers and the co-author of two books: Geographic Information Systems for Group Decision Making and GIS for Urban and Regional Environments: A Spatial Decision Support Approach.
