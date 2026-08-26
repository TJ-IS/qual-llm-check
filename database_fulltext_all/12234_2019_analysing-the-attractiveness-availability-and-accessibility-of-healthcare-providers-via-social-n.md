---
otero_id: 12234
otero_key: "2V8NCENC"
title: "Analysing the attractiveness, availability and accessibility of healthcare providers via social network analysis (SNA)"
authors: "Fernanda Strozzi; Elisabetta Garagiola; Paolo Trucco"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.03.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Analysing the attractiveness, availability and accessibility of healthcare providers via social network analysis (SNA)

![](/api/attachments/2V8NCENC/fulltext/images/8fd123de97aba333f78f7ff1eb1d5063357691ced5e7ee4fb30a893e87fdabe6.jpg)

Fernanda Strozzi<sup>a,⁎</sup>, Elisabetta Garagiola<sup>a</sup>, Paolo Trucco

<sup>a</sup> School of Industrial Engineering, Cattaneo University-LIUC, C.so Matteotti, 22, 21053 Castellanza, Italy

<sup>b</sup> Politecnico di Milano, School of Management, Economics and Industrial Engineering, Via Lambruschini 4b, 20156 Milan, (Italy)

## A R T I C L E I N F O

Keywords: Healthcare Planning Patient's choice Attractiveness Accessibility Social network analysis

## A B S T R A C T

Due to the increasing pressure on resource limitations and the need for eficiency improvements, efective healthcare service planning should analyse trends in citizens' demand for healthcare services, as well as patients choices of healthcare providers, which are determined not only by prestige, but also by physical accessibility and availability. The main objective of the present study is to explore the benefits of adopting the social network analysis (SNA) approach to investigate the determinants of a patient's choice of healthcare provider as a way to support better resource allocation decisions in healthcare systems. For the purpose of the analysis, admini strative data was used to track the flow of patients within orthopaedic departments of the Lombardy region (Italy) in 2014. A network was developed with two types of nodes: those of orthopaedic departments in the regional hospitals (114 nodes), and those of municipalities (5092 nodes). Using the Louvain algorithm, the communities and sub-communities were determined on the basis of patients' choices, without any prior geographical considerations or planned catchment areas.

Traditional SNA measures and other novel indicators, specifically developed for this study, were applied: in particular, attractiveness (i.e. the preference that patients assign to a certain department against the others available in the same reference area) and confinement (of demand) (i.e. the degree of the unique use of a certain department). A decision support matrix based on these indicators was defined for decision makers to use in evaluating department profiles, and optimizing the location of services and allocation of resources, while pre serving accessibility to care and patients' preferences. The decision support matrix was also evaluated on the basis of real practice and decisions made by regional healthcare managers.

## 1. Introduction

The continuous evolution in diagnostic, treatment and rehabilita tion practices, largely driven by the availability of innovative health technologies, has resulted in a more dynamic demand for specialized health services. This trend challenges policymakers and healthcare managers to design new governance models and plan healthcare services diferently [45]. Decision makers should act on the basis of trusted information on appropriateness, eficiency and efectiveness, while preserving the sustainability of the entire health system [44].

The increasing pressure from resource limitations and the need for eficiency improvements in healthcare delivery is a significant concern in many developed countries [33] and a key driver of resource allocation in modern health systems. To this end, a systematic analysis of the network of hospital departments – primarily in terms of geographical distribution, the mix and characteristics of their oferings, and their quality, safety, and eficiency performance [37] – is a key prerequisite for efective planning. In an era of more open health systems, in which patients are empowered by easy access to medical knowledge and health-related information on the Internet, the problem of efectively distributing healthcare service facilities and allocating resources is a priority for decision makers, so they may avoid limited accessibility, insuficient coverage (i.e. a facility located too far away from patients), and congestion (i.e. excessive waiting list for healthcare services), and secure higher quality standards [14]. All these elements should be assessed in an integrated way by decision makers during the strategy definition and service planning processes [47].

In developed countries that have adopted a universal health system [25], the importance of defining proper geographical areas of reference (i.e. catchment areas) for hospitals has always been recognised [21] as a key element of healthcare service planning. However, under the current pressure to ofer more personalized treatments and pathways, and improve patients' experiences [26], efective healthcare service plan ning should start from a more careful analysis of trends in citizens demand for healthcare services, which includes the service mix and dependencies, geographical distribution of the service demand, and patterns in patients' choices of healthcare providers. Undoubtedly, giving patients more freedom to choose their preferred provider adds complexity to the planning problem; therefore, a better understanding of a patient's choice determinants becomes of paramount importance.

A patient's choice entails many spatial and non-spatial factors [52], including distance, availability, seriousness of illness, the need for a quick answer to the health problem and the perceived quality. A patient's choice is often the result of an optimization problem, solved autonomously by taking into consideration a variety of factors, such as personal priorities and preferences, available information, and the actual or perceived constraints of the oferings. For example, if a patient must undergo orthopaedic surgery on a hip and the operation is not urgent, he/she will likely spend more time gathering information on the hospital with the highest prestige, adequate accessibility and availability (i.e. length of the waiting list). The same patient could decide diferently in the case of an urgent surgery, for example, by sacrificing prestige for accessibility (i.e. a shorter waiting list). Whether a patient's judgment is correct – for example, regarding the perceived quality of the department vs. the actual quality – should be considered and well understood by healthcare managers when making strategic and tactical decisions.

In this context, a social network analysis (SNA) could ofer ad vanced analytical capabilities to capture the key characteristics and drivers of this complex phenomenon, which in many ways is similar to social relationships. An SNA considers the society as a network in which individuals are nodes and their relationships are links [24,42]. Although it was developed to study social networks, the SNA approach has found several applications in the physics, biochemistry and computer science domains [8]. Batagelj et al. [12] also applied an SNA to study a customer's choice of networks. In the healthcare sector, an SNA was applied to study the networks of healthcare professionals [17] and their communication, as well as the healthcare value chain [30]. However, to the best of the authors' knowledge, it has never been used to study a patient's choice of healthcare providers.

The main objective of the present study is to explore the benefits of adopting an SNA to investigate the determinants of a patient's choice to support better resource allocation decisions in healthcare systems. Therefore, the following research question is presented:

RQ: How can an SNA be used to support resource allocation deci sions in healthcare systems that take into consideration the patient' choice?

The empirical part of the study is developed in the context of a recent reform of the regional health system (Regional Law n. 23 of 11 August 2015) in Lombardy (Italy). The aim of the reform was to reduce costs, improve the quality of care and strengthen control, while maintaining the principle of patients' freedom of choice as a priority. In the perspective of system rationalization, decision makers apply criteria and methods to identify single departments or entire hospitals suitable for further investment and improvements, or as candidates for closure. In this regard, a deeper understanding of the factors that guide patients' choices and the implications in terms of patients' access to healthcare services, as well as the quality and responsiveness of service providers, are all key elements for optimal planning and use of scarce resources. Using traditional SNA and other specifically developed measures, we built a novel decision matrix that supports decision makers in identifying the importance of a department for a given geographical area, which then assists in the consequent allocation of resources. More specifically, an SNA was applied to map and analyse the attractiveness of the providers and the reasons for such attractiveness (i.e. prestige, accessibility and availability) as attributes of a patient's preference. The method and proposed indicators were tested on the orthopaedic departments of the Lombardy region only, but the characteristics of the proposed approach make it suitable for wider applications covering other medical disciplines.

The remainder of the paper is organized as follows. In Section 2, a review of the state of healthcare planning is presented and focuses on two main topics: decision support systems for healthcare management, and patient choice issues connected with the healthcare planning problem. Section 3 introduces the materials used and the stepwise procedure applied in this work. Results are reported in Section 4. A novel decision tool for healthcare planning (decision matrix) is introduced in Section 5 and discussed in Section 6. Finally, Section 7 summarises the implications for research and practice, and ofers some insights for future developments.

## 2. State of healthcare planning

## 2.1. Decision support systems (DSS) for healthcare planning

The management of healthcare systems is a complex problem; policymakers and managers require tools to properly allocate resources with the aim of satisfying patients' needs and preferences. Scientific literature reports on a plethora of decision support tools designed for and implemented in the healthcare setting. For example, at the operational level, Ayed et al. [5] proposed a DSS based on knowledge discovery to involve physicians in healthcare delivery decisions. The approach has been validated with physicians from the intensive care unit (ICU) of a hospital in Tunisia. Adeyemi et al. [1] studied the individual clinical pathways of patients afected by chronic obstructive pulmonary disease (COPD) to identify the determinants of multiple readmissions in hospitals. The application of similar methodologies to other diseases may support the decisions of healthcare managers or policymakers in improving performance monitoring and management in hospitals. Bai et al. [6] developed a two-stage decision-making methodology for optimizing healthcare workflows and task assignments while mitigating the risk of information disclosure. The first stage optimizes the operational eficiency but may increase the risk of information disclosure. To mitigate this side efect, the authors introduced several security-control strategies in the second step.

Other decision support systems have been implemented in healthcare at the policy level. Tremblay et al. [49] applied the on-line analytical processing (OLAP) tool to the comprehensive assessment for tracking community health (CATCH) dataset used by knowledge workers at a regional health planning agency in Florida (United States). The CATCH database includes quantitative indicators and a framework for ranking healthcare problems. Barjis et al. [11] proposed a homebased healthcare system in displaced rural areas of southern Africa, equipped with a patient monitoring system. This system supports nurses' and doctors' decisions, which leverage the continuous monitoring of patients' vital signs. Ranerup et al. [46] compared diferent tools provided by a web portal in Sweden to support the patient's choice of a primary care provider.

Literature also suggests that geographic distribution greatly afects population health maintenance [27]. Indeed, facilitating access means helping patients select appropriate healthcare providers to preserve or improve their health [28]. Li et al. [32] proposed a framework to build a spatial decision support system (SDSS) to enable decision makers to explore physician shortage areas. This framework allows the use of diferent spatial and non-spatial determinants of a patient's choice to develop a spatial accessibility index (SPAI) that healthcare managers may use to detect shortage areas and ensure equitable healthcare access.

In this view, Apparicio et al. [4] measured the geographical accessibility of health services considering four elements: a definition of the residential area, a method for aggregation into areas, a measure of accessibility of the area, and the distance from the health service. Similarly, Higgs [29] focused on geographical information systems (GIS)

as a decision support tool in healthcare, reviewing the measures of access to healthcare services, and exploring the relationship between geographic access, utilization, quality and health outcomes.

## 2.2. Patient's choice and service accessibility in healthcare planning

In the last 10 years, patients' choices in healthcare started to gain interest and have been thoroughly studied in northwest European countries, such as the Netherlands and the UK [20,46,51]. In fact, patients' choices promote competition between providers, reduce wait times and increase patients' centrality in health system management without compromising quality and economic sustainability [51].

A patient's choice is strictly connected with patient satisfaction and can provide a measure of service quality together with a predictor of health-related behaviours [43]; indeed, it is not only driven by the quality of the provider, both objective and perceived, but also by the accessibility of services. In literature, accessibility is a multifaceted concept, defined by researchers in diferent ways. Fortney et al. [22] defined accessibility as the travel time between each subject and the closest provider. Gulliford et al. [28] measured access in terms of uti lization of healthcare providers and tested its dependence on many elements, including afordability, physical accessibility and acceptability of services. Moreover, the availability of services and barriers to access must be considered in relation to diferent health needs and cultural facets.

The factors commonly used in literature to measure accessibility, which indirectly influence a patient's choice, can be classified into two categories: spatial and non-spatial [32]. The main spatial factor is the travel distance, but the available means of transport is sometimes considered among spatial factors. Empirical evidence shows that distance and time factors strongly influence patients in choosing a hospital, even in metropolitan areas where more alternatives are normally available [40,48,50]. Bejleri et al. [13] considered as spatial determinants hospital accessibility and the availability of alternatives. Accessibility was assessed using the time it took for patients to travel to and from the hospital, and availability was measured as the total oferings of healthcare services within a certain geographical area. The authors applied a GIS and measured how the round-trip time and availability of alternatives influence the choice of healthcare providers.

Spatial accessibility has been largely studied using the two-step floating catchment area (2SFCA) method [36] and its variations. The 2SFCA consists of drawing polygons around supply and demand centroids (where supply centroids are the locations of the healthcare providers and demand centroids may be the centre of the census tracts of the patients). The polygons are defined supposing a travel threshold. The polygons and their crossing areas identify zones with a diferent ratio between demand and supply. By summing these ratios, it is possible to obtain an index (SPAI) that takes into account providers and population density at the same time. Many variations of the 2SFCA exist in literature. The enhanced 2SFCA (E2SFCA) introduces a distance decay function [39]; other proposed improvements are based on different ways of considering travel time, such as including public transport [38].

Common non-spatial factors considered in literature include age, sex, ethnicity, income, social class, education or language ability, and high healthcare needs [54]. Li et al. [32] assumed the availability of revealed access (i.e. actual utilization) to understand the utilization pattern. They studied the demand composition using the population characteristics identified by the behavioural model [2]. They modified the 2SFCA model [53] to create the utilization-based healthcare accessibility algorithm, which weighs diferent population characteristics using the behavioural model. Furthermore, a patient's choice also depends on the attractiveness (i.e. reputation) of the provider [35]. Bejleri et al. [13] defined hospital prestige as the number of times a hospital was chosen, that is, its ability to attract patients.

Levesque et al. [31] did not limit the analysis of a patient's choice to spatial and non-spatial factors but tried to explain it in a comprehensive and dynamic way using a multilevel perspective, comprising the individual, household, community, and population levels. The results considered five dimensions of accessibility: approachability, acceptability, availability and accommodation, afordability, and appropriateness.

In this study, a novel approach is proposed allowing for extracting a patient's choice determinants directly from administrative data. Prior knowledge on spatial factors – such as distance – or non-spatial factors – such as age, sex and education – is not considered direct input. The analysis is built on the network comprising the nodes of patients' origins (ZIP codes) and healthcare providers. Using an SNA, patients' choices are mapped and analysed using network metrics to infer some properties of the departments starting from their attractiveness. Consequently, the degree of influence of possible distance constraints on a patient's choice can be inferred ex post. This approach is appropriate for supporting resource allocation and planning universal health system in which patients have the ability to choose providers, implying that a patient's choice determinants and dynamics strongly influence optimal decisions.

## 3. Material and methods

## 3.1. Material

The administrative data used in this study tracks the flow of patients towards the orthopaedic departments of the Lombardy region (Italy) in 2014, without any restrictions regarding the type of surgical procedure. Overall, the data set comprises 142,346 records.

For the purpose of the analysis, a network with the following two types of nodes was developed: those of healthcare providers (i.e. the orthopaedic departments in the regional hospitals; 114 nodes), and those of municipalities (i.e. the ZIP codes of patients; 5092 nodes). The links between nodes (arrows) represent the events of patients living in a certain municipality who were hospitalized in an orthopaedic department for a surgical procedure. Each arrow was weighted by the number of similar events in 2014. It is important to underline that some orthopaedic departments in the Lombardy region are extremely attractive and many patients come from other Italian regions or from abroad.

For the sake of confidentiality, data was anonymised; in the following, municipalities are indicated without using the real ZIP code, and the orthopaedic departments are denoted with a fake code (the label “Dep” followed by a number). The network and SNA measures were implemented in Pajek, a free software package for social network analyses and visualization [19].

## 4. Methods

To assess the attractiveness (or prestige) of an orthopaedic department, the number of surgical procedures (i.e. the weighted in-degree of that department node) was used, following Chanut et al.'s [18] study. They applied the in-degree to measure the number of patients that physicians transferred to another hospital because of better competences or higher resources compared to the hospital of origin. In the present study, the decision is made by the patients and not the physician, and the in-degrees of departments were calculated using communities, a well-known partition technique of the SNA approach. The communities were identified using patients' choices and helped highlight smaller areas where the in-degree of a department becomes a measure of local attractiveness.

The community partition allowed for the development of a novel indicator – confinement – which measures the level of constrained demand served by a department in terms of the portion of patients (ZIP codes) that goes to that department in the community because there is a lack of accessible or available alternatives. From a healthcare system planning perspective, this indicator is particularly relevant because it is a measure of the impact that a closure of that department might have on the accessibility of patients to care services. In Section 5, attractiveness and confinement are considered two dimensions of a decision matrix for supporting healthcare network planning. In Table 1, these indicators are compared with similar ones proposed in the literature.

Table 1  
Indicators proposed to study patients' choices in the context of healthcare network planning.

<table><tr><td>Indicator</td><td>Quantification with SNA measures</td><td>Similar indicators in literature</td></tr><tr><td>AttractivenessThe preference that patients assign to a certain department against all the others available in the same reference area.</td><td>Weighed in-degree of the department in the second-level partition</td><td rowspan="2">PrestigeThe number of times the hospital was chosen by patients [13,18].UtilizationActual demand [32].AccessibilityTime round-trip to reach the department [13].AvailabilityShort waiting lists or uniqueness of the department in the neighbourhood [13].</td></tr><tr><td>Confinement (of demand)The degree of the unique use of a certain department; it measures the strength of all the factors (including accessibility and availability) that encourage or force patients to always choose that department.</td><td>Weighed in-degree in the second-level partition considering only the nodes connected with that department but not with others.It measures the number of orphan nodes in case of department closure.</td></tr></table>

The concept of communities is often used in the SNA approach [23]. Analytically, a community is a partition of the network based on the measure of the density of links inside a subset of nodes, which is relatively higher in comparison to the links between other subsets. The density of the links in the network between nodes (ZIP codes and departments) shows that some municipalities represent a constituency of patients for those departments. To detect communities in the network, Blondel et al.'s [15] Louvain algorithm was applied in Pajek. An example of its application to a small test network is shown in Fig. 1. In this case, the algorithm detects the presence of two communities.

The analysis was articulated into three levels, corresponding to diferent partitions of the entire network. The whole network of orthopaedic departments and ZIP codes in the Lombardy region represents the zero-level partition. The communities obtained by applying the Louvain algorithm to the zero-level partition is referred to as the first-level partition. Finally, the second-level partition is the set of subnetworks (sub-communities) identified by applying the Louvain algorithm to the communities detected in the first level. At the second level, the sub-communities include no more than 5000 patients; however, the proposed method is scalable and the levels of partitions to be considered in a specific study can be set by the analyst.

The simplest measure of centrality of a node in a social network is its degree and, in the case of a direct network such as the patient's choice network, the in-degree. It represents the patients' incoming flow in the departments. The in-degree is calculated for each department in consideration of its specific community level (see Table 2). The secondlevel partition identifies the local attractiveness of the department, as well as the ZIP codes that always choose the same department (confinement of demand).

## 5. Analysis of the patient's choice network

## 5.1. Analysis of the zero-level partition

The network of orthopaedic departments and municipalities of the Lombardy region includes 5206 vertices: 5092 municipalities and 114 orthopaedic departments. There are 28,390 arrows connecting municipalities to departments, and 13,196 of those have a weight greater than one; this means that, in some municipalities, more than one patient was hospitalized in the same orthopaedic department.

The weighted in-degree of a department (i.e. the weighted sum of the arrows pointing to it) expresses its attractiveness at the regional level; the in-degree of municipality nodes is zero because they only have outgoing patients. Fig. 2 shows the ABC plot of the patients' flow in the orthopaedic departments in 2014; it can be noted that only a few departments (20%) perform up to 50% of the annual orthopaedic surgical procedures, and less than 60% absorb 80% of patients. This means that the system is characterised by a group of over-used (very attractive) providers and a group of under-used providers, leading to opportunities for rationalization of the system.

The histogram of the in-degree values of the 114 departments (Fig. 3) shows a shape similar to that of a scale-free network. The scalefree network model often appears in natural systems [7,9,10]. It is characterised by the presence of many nodes with a low in-degree and a few nodes with a high in-degree. In our case, this means few departments with a large patient in-flow and many departments with a low patient in-flow. In scale-free networks, the probability of finding a node with a degree greater than k (P(degree > k)) scales linearly with k (in the logarithmic scale). Fig. 4 shows the survival function of the network under analysis and its adherence to a linear function. This implies that the probability of finding a node with a very high degree is not negli gible, as would be the case, for example, if the distribution were exponential [34]. Barabasi et al. [9] found that many natural networks, such as social networks and other self-organized networks, are characterised by a similar rate of decreasing; this property can thus be used to detect the degree of similarity of the patient's choice network with a natural network. The relevant properties of scale-free networks and their implications from a healthcare planning perspective are presented in Section 6.

![](/api/attachments/2V8NCENC/fulltext/images/dc37b49b1d1a9db241e03aff6da4747c4d9c9e591f4b8d1fa694673a6ff9c736.jpg)  
Fig. 1. Example of application of Louvain algorithm to detect two communities (partitions) in the network

Table 2  
In-degree, attractiveness and confinement for each orthopaedic department in Communities 9 and 10, calculated at diferent network partition levels.

<table><tr><td>Community</td><td>Sub-community</td><td>Department</td><td>In-degree at regional level (zero-level partition)</td><td>In-degree at community level (first-level partition)</td><td>Attractiveness (in-degree at sub-community level or second-level partition)</td><td>In-degree at sub-community level (second-level partition) of the pruned network</td><td>Confinement (e = c-d)</td></tr><tr><td></td><td></td><td></td><td>a</td><td>b</td><td>c</td><td>d</td><td>e</td></tr><tr><td rowspan="10">9</td><td rowspan="3">9.1</td><td>Dep_5</td><td>513</td><td>413</td><td>382</td><td>380</td><td>2</td></tr><tr><td>Dep_4</td><td>905</td><td>811</td><td>750</td><td>747</td><td>3</td></tr><tr><td>Dep_6</td><td>2406</td><td>1612</td><td>1309</td><td>1136</td><td>173</td></tr><tr><td rowspan="3">9.2</td><td>Dep_9</td><td>401</td><td>322</td><td>281</td><td>279</td><td>2</td></tr><tr><td>Dep_1</td><td>1032</td><td>647</td><td>558</td><td>367</td><td>191</td></tr><tr><td>Dep_2</td><td>1442</td><td>1162</td><td>1005</td><td>958</td><td>47</td></tr><tr><td>9.3</td><td>Dep_10</td><td>907</td><td>782</td><td>567</td><td>0</td><td>567</td></tr><tr><td>9.4</td><td>Dep_3</td><td>436</td><td>327</td><td>230</td><td>0</td><td>230</td></tr><tr><td rowspan="2">9.5</td><td>Dep_8</td><td>271</td><td>243</td><td>165</td><td>155</td><td>10</td></tr><tr><td>Dep_7</td><td>1318</td><td>748</td><td>366</td><td>198</td><td>168</td></tr><tr><td rowspan="3">10</td><td rowspan="3">10.1</td><td>Dep_1</td><td>344</td><td>312</td><td>312</td><td>307</td><td>5</td></tr><tr><td>Dep_2</td><td>744</td><td>648</td><td>648</td><td>616</td><td>32</td></tr><tr><td>Dep_3</td><td>1067</td><td>945</td><td>945</td><td>878</td><td>67</td></tr></table>

## 5.2. Analysis of first-level partition network

The in-degree at the regional level (zero-level) does not give detailed information in terms of patients' choices at the local level, but only provides the number of patients hospitalized during 2014 in dif ferent orthopaedic departments.

Patients do not prioritise departments by looking at their reputation only (attractiveness), but consider also their accessibility and availability within a certain geographic area. To extract this information from administrative data, we identified the subsets of nodes (departments and ZIP codes) more strictly connected by common patterns of a patient's choice, considering that a decision is made over a trade-of between the attractiveness, accessibility and availability of the departments.

![](/api/attachments/2V8NCENC/fulltext/images/336a959ccec06615c30496352d4d243bb688aa8fe4d7c6b7df3a4306e5019dd5.jpg)  
Fig. 3. Number of departments (n0) with a given weighted in-degree (k) at the regional level (zero-level partition).

![](/api/attachments/2V8NCENC/fulltext/images/82c86659914884035430faa68c4b9c2c2292bbc4c1876c86344184b0e31de84b.jpg)  
Fig. 2. ABC plot of the orthopaedic departments in the Lombardy region.

![](/api/attachments/2V8NCENC/fulltext/images/930fd4f4e32faa3b5fb0a1a33e6871e86fd758116bbce9eb1f151ca2c5f07b71.jpg)  
Fig. 4. The survivor function of the in-degree distribution of departments in a logarithmic scale.

![](/api/attachments/2V8NCENC/fulltext/images/1f248e36f96ef2f92b667bcf21b743d506d55b2950ba3ae64e7fae92cf1f5472.jpg)  
Fig. 5. The 10 communities of orthopaedic surgery in the Lombardy region.

The Louvain algorithm applied to the entire network identified 10 communities. It is worth noting that, using the Louvain algorithm, the communities are determined only on the basis of patients' choices, without any prior geographical considerations or planned catchment areas. In Fig. 5, the nodes of each community (origin area ZIP codes and departments) are depicted by ovals and the patients' flow is indicated with light grey arrows. It is possible to see that communities are not completely isolated and that flows of patients exist between commu nities too.

In Fig. $^ { 6 , }$ the orthopaedic departments of each community are shown on the map, which uses diferent shades of grey to identify the 10 communities. The partition of departments seems to overlap quite well with the administrative provinces in the region, with only a few exceptions.

## 5.3. Analysis of second-level partition and indicators of confinement and attractiveness

The 10 communities identified at the regional level vary greatly in size – some have more than 20,000 patients (e.g. Communities 1 and 2) and others have only 5000 (e.g. Community 10). The second-level partition further divides the 10 communities into sub-communities. The analysis revealed that the larger communities are divided into smaller sub-communities with no more than 5000 patients, but smaller communities (e.g. Community 10) do not show lower-level structures.

In this section, the sub-communities of Communities 9 and 10, the smallest ones, are analysed in detail. Community 9 is made of 490 nodes: 10 hospital departments and 480 municipalities (ZIP codes). In Fig. 7, the size of each department node represents its in-degree (patient in-flow) at the community level (i.e. its attractiveness). By applying the Louvain algorithm to this community, it is possible to identify five subcommunities. Sub-communities 9.1 and 9.2 include three department nodes each, sub-communities 9.3 and 9.4 have only one, and sub community 9.5 has two departments.

![](/api/attachments/2V8NCENC/fulltext/images/3edeaad0d5597afd8e4de6792a15724a629e9fa100ed39ba87eab4c6d03af5dc.jpg)  
Fig. 6. Map of the orthopaedic departments in the Lombardy region

Community 10 has no sub-communities. It comprises three department nodes, 94 municipality nodes and 181 arcs (among which 123 have a weight higher than one). In Fig. 8, department nodes have different sizes according to their in-degrees (i.e. attractiveness; see also Column “c" in Table 2).

The second-level partition analysis of the network enables a detailed investigation of the diferent factors that may explain the level and type of attractiveness of departments, which include prestige, shorter waiting times, and unavailability of accessible alternatives. Indeed, observing Fig. 8a, it is possible to identify departments with some unique origins (i.e. municipalities that access a specific department only). The number of patients from these municipalities represents a measure

![](/api/attachments/2V8NCENC/fulltext/images/86e122b678e928e49a8ecf6806ca89ef0553dd21b0a1c3115069dece964e18bd.jpg)  
Fig. 7. Community 9 and its five sub-communities (the linked nodes with only labels are the municipalities).

![](/api/attachments/2V8NCENC/fulltext/images/cf3a8b94dcf0860d7a848fc9031c32652dfa428cd39910d612f1ca80caef21ad.jpg)

a)  
![](/api/attachments/2V8NCENC/fulltext/images/dfc00b21b1bd3972cc90906f99a91c304ca61a59bb28b83d747fe89a06cb0925.jpg)  
b)  
Fig. 8. Community 10 before (a) and after (b) pruning (municipalities with one link only are eliminated).

of the importance of the department in terms of accessibility to and availability of care services. On the contrary, the municipalities linked to more than one department represent groups of patients who are free to choose. The flow of these patients can be measured by “pruning” the original network $( { \mathrm { F i g } } .$ 8a) and re-calculating the in-degree of the department nodes of the “pruned” network (Fig. 8b). The diference between the in-degrees of nodes in the two networks captures this phenomenon (Column $" \boldsymbol { \mathrm { e } } ^ { \prime \prime }$ of Table 2). This indicator expresses the confinement of the demand that the current health system forces on a specific department. From a system planning point of view, this measure contains more information than the in-degree alone; for example, one department might have a low in-degree value but a high ratio of unique links (i.e. a high confinement) and, if closed, the level of accessibility to health services would be highly degraded for many municipalities because patients in those municipalities currently have no suitable alternatives for orthopaedic surgery.

## 5.4. Comparison between the attractiveness of departments at diferent partition levels

In this section, the values of attractiveness of the departments at the regional level (zero-level partition), community level (one-level partition), and sub-community level (two-level partition) are compared. In Fig. 9, the departments are ordered using their attractiveness at the regional level from the lowest to the highest value. Results show that higher values at the zero-level partition often correspond to higher values at level one and two. If a department is attractive at the regional level, it is normally also attractive locally (i.e. in the first and second levels). This seems primarily connected to the reputation of the department, which can be easily prioritised against other factors when patients reside close to it. In contrast, moving from level zero to level one or two, the increase in attractiveness becomes less smooth (see diamond compared to star markers in Fig. 9). This can be explained by the fact that, for some surgical orthopaedic interventions (generally, the simplest), the patient's choice may be less driven by the attractiveness (prestige) of the department and more by its availability and accessibility.

![](/api/attachments/2V8NCENC/fulltext/images/4b01947f1a581d6f52587db89781b5d236349445e021af5dd9e2b9fe0a5a757f.jpg)  
Fig. 9. In-degree of the orthopaedic departments at diferent partitions of the network (Level 0 = entire region; Level 1 = communities; Level 2 = sub-communities).

![](/api/attachments/2V8NCENC/fulltext/images/c313469c6afe9411a547105452f9fc1a6fae7f10f9bdf6997749915136b45308.jpg)  
Fig. 10. Histograms of number of departments (n) with a given in-degree (k) at Level 1 (n1) and at Level 2 (n2).

The distribution of departments according to their in-degree at level zero is reported in Fig. 3; Fig. 10 reports the distributions calculated at the first- and second-level partitions.

Moving from level zero to level one and two, the distributions of indegrees gradually lose the typical scale-free shape and move towards a lognormal profile (i.e. the distribution of the logarithms of the in-degree is normal). The hypothesis of a lognormal distribution was confirmed by the Anderson-Darling test [3], with a significance level of 5%. Hence, the distribution of the attractiveness of departments changes in shape moving from the regional level (Fig. 3) to levels one and two (Fig. 10). The finding implies that at the local level (community or subcommunity levels), the network cannot be assimilated to a scale-free network, which signifies that, locally, there are groups of patients with a relatively lower degree of freedom in choosing a preferred provider. This suggests the importance for decision makers to consider attractiveness at the sub-community level, and not at the regional level, as a criterion to establish the minimum service volume (e.g. annual surgical procedures) that justifies the closure of a department.

## 6. The decision support matrix

The attractiveness and confinement indicators can be jointly used to segment healthcare providers and support planning decisions. To this end, in Fig. 11, a decision support matrix is introduced. For each dimension of the matrix, the two thresholds of attractiveness and con finement $( \mathsf { A } _ { \mathrm { T } }$ and $\mathrm { C _ { T } } )$ should be calibrated by health managers considering diferent facets of the problem. When departments are located in the quadrant of high attractiveness and low confinement, it means that within these providers, patients have the freedom to choose without compromising the quality of care. On the contrary, depart ments located in the region of low attractiveness and low confinement are those that are relatively less attractive than other departments available in the same community; these are candidates for possible closure, in favour of reallocating resources to higher quality departments without compromising the accessibility to care. The most critical quadrant is the one with high confinement and low attractiveness; these are departments that patients are forced to choose because of the lack of easily accessible alternatives; thus, despite their low attractiveness, they cannot be considered for closure without compromising the acces to care for local patients.

![](/api/attachments/2V8NCENC/fulltext/images/0a5e72a9373135f885e486e80297d6746298aa89816843e891e6784693d89c81.jpg)  
Fig. 11. The decision support matrix based on the attractiveness and confinement indexes of healthcare departments.

Fig. 12 shows the application of the decision support matrix to the orthopaedic departments of Community 9. Dep\_8 has the lowest attractiveness in its sub-community; indeed, it is geographically very close to other departments with higher attractiveness (Dep\_1 and Dep\_2). Alternatively, Dep\_3, despite its low attractiveness, has a high level of confinement and this is justified by its geographic location. This department is important to satisfy local demand and assure accessibility to care. Decision makers should not consider its closure but set proper investments and an improvement programme to increase its attractiveness above the $\mathbf { A } _ { \mathrm { T } }$ level, so as to secure an adequate level of quality for local patients.

Fig. 13 shows the decision matrix with the values of attractiveness and confinement for all the orthopaedic departments of the Lombardy region. Two departments (Dep-a and Dep-b), both belonging to Com munity 1 (i.e. the Milan area), appear to be outliers; in fact, they are the two most prestigious orthopaedic departments in the region, attracting patients from the entire country and from abroad. They have the highest values of attractiveness, but Dep-a has a significantly lower level of confinement. The higher attractiveness of Dep-a in the subcommunity is due to its strict relationship with patients located in the Milan area: 60% of its patients came from Milan, whereas they account for only 25% of the Dep-b patients. Indeed, the high confinement of demand in Dep-b is justified by its higher availability and the higher ratio of patients coming from other Italian regions. Some departments show equal attractiveness and confinement values (i.e. the in-degree before and after network pruning is the same); this means that these departments are alone in their sub-community, and the pruning procedure reduces their in-degree close to zero (Column “d” in Table 2). They are critical in granting accessibility to orthopaedic surgery to patients in those areas. Several departments have a very low level of confinement (laying very close to the attractiveness axis); this means that their attractiveness remains the same after network pruning. These are departments that are not alone in their sub-communities, whose relevance for the system depends only on their attractiveness in a relatively higher competitive context. We may conclude that the closer the department points are to the attractiveness axis, the more competitive the healthcare system is, and a higher degree of freedom is granted to patients' choices.

![](/api/attachments/2V8NCENC/fulltext/images/2e24fa31ce579c12d94c7e28ee5f3a38329246e907a8111430023deb24055f67.jpg)  
Confinement  
Fig. 12. Application of the decision support matrix to the orthopaedic departments of Community 9.

## 7. Discussion

Making use of the SNA technique and some of its tools (i.e., indegree measure and community detection), two indicators, namely attractiveness and confinement, were introduced and used to build a decision matrix. Decision makers may refer to this matrix to gain useful insights not only on the attractiveness of a department at the local level, but also to understand the drivers of a patient's choice (i.e. prestige, accessibility and availability) that steer demand towards diferent departments. This information is relevant to decision makers and is usually not available at the local level. In fact, the key issue in the healthcare planning problem consists of defining the concept of “local.”

In literature, diferent measures have been developed to define catchment areas, such as the geographical distance or reachability of a department via public transport [54]. The main element of novelty of the proposed approach is in using the concept of community applied to the patient's choice network as a more robust way to identify catchment areas. In other words, we leave it to the patient's choice to decide if a department is too far, when prioritised against other non-spatial factors. Furthermore, the confinement indicator is proposed to be jointly used with the more traditional attractiveness (i.e. prestige) indicator. Confinement highlights if the attractiveness of a department is primarily due to its prestige (i.e. the perceived quality) or to other determinants of a patient's choice, such as availability or accessibility. It is worth noting that in contexts in which patients' preferences and corresponding choices are volatile, the health planning process is rarely efective if driven by the ex-ante definition of the catchment areas of departments and hospitals. On the other hand, relying on the identification of communities and sub-communities, driven by the SNA, allows for rapid detection of any dynamism in demand patterns or patients' preferences, and may lead to more robust and eficient decisions.

Aiming to test the validity of the proposed approach, it is possible to compare the actions suggested by the decision matrix (Fig. 11), when applied to the administrative data of orthopaedic surgery in the Lombardy region (Figs. 12 and 13), with the real actions taken by regional health managers in 2015, when they started to implement the reform. The cases of three relevant departments and the corresponding deci sions made are discussed next.

![](/api/attachments/2V8NCENC/fulltext/images/6a328e26802f3faf60bb1219210710b677f0b7b6c56917bcacfb1539ffbc9e3d.jpg)  
Fig. 13. Attractiveness ys. confinement of the orthopaedic departments in the Lombardy region (Italy): two outlier departments of Community 1 (Milan area) are highlighted and the quadrant bisector has been designated with a continuous line.

The first two cases involve the departments of Community 8. Because they are located in the lower left quadrant of the matrix (low attractiveness and low confinement), the decision matrix suggests a rationalization of the in-patient activity. In practice, one of the two departments was forced to reduce its surgical activities because of the lack of orthopaedic specialists; currently, less complex surgical interventions and out-patient visits are performed in this department. A similar situation also occurred in the second department of the same community – it was not closed definitively but a radical change in its surgical activities was registered; activities at a lower intensity of care are currently performed by the department. Given the low confinement level, it is expected that the matrix mirrors the actual decisions made by looking at the attractiveness of departments only.

The third case concerns an orthopaedic department of Community 4 that the regional health managers decided to close due to its very low level of attractiveness. Nevertheless, after a strong protest from citizens and patient associations, it was reopened. This event is well explained and justified by looking at the position of this department in the decision support matrix. The department is located in the low right quadrant, having a low level of attractiveness and a high level of confinement. According to the decision matrix, this is exactly the case of departments whose closure would lead to degraded accessibility to care for local patients – a phenomenon that is rarely visible at the regional level and without the proper identification of communities of patients.

The application of an SNA to a patient's choice network built on administrative data also enables a qualitative assessment of the actual degree of freedom that the current configuration of the health system grants to patients for specialities. The analysis can be carried out by comparing the properties of the patient's choice network with the typical properties of a scale-free network (e.g. social and natural networks; [16]). Social networks (e.g. Facebook and Instagram), and other natural networks (e.g. protein networks) are characterised by a particular degree distribution that is correlated to important properties of the network. Compared to a random network, the scale-free network has a very diferent kind of connectivity because the degree distribution is defined by a power law distribution instead of the Poisson distribution associated with the random network. In a scale-free network, a small number of nodes contribute heavily to connectivity (hubs), whereas in a random network, each node contributes fairly equally to the overall connectivity of the network. Scale-free networks are self. similar – any part of the network is statistically similar to the whole network. Scale-free networks are also tolerant to failure, as they maintain their structure and functionality even under the random re moval of a few nodes.

What is relevant from a healthcare planning perspective is that, in a social network, people are free to choose friends, and the resulting degree distribution of links in the network shows the existence of a few nodes with a high degree (many friends) and many nodes with a low degree (few friends). The similarity of a patient's choice network with a typical social or natural network may be considered the measure of the degree of freedom that the health system grants to patients in choosing their preferred providers for diferent specialities and needs. It is also interesting to see how this distribution may change when the in-degree of the departments is measured in the community or sub-communities (i.e. at local level); looking at the network of orthopaedic surgery in the Lombardy region, the in-degree distribution becomes more similar to a lognormal one, which is typical of a random network. In this case, it seems that patients progressively lose some degrees of freedom in making their choices and that the contribution of diferent departments in satisfying local demand tends to level of.

However, the proposed approach also has some limitations. In terms of applicability, it is useful for rationalizing universal health systems only when an eficient and efective planning process takes into consideration the degree of freedom the system grants to patients in choosing between diferent providers. Additionally, the proposed approach and the decision support matrix help managers make investment and closure decisions for existing departments but do not provide any direct information on if and where a new department is needed. Thus, the current version of the proposed approach and decision support matrix can only be used for planning mature and stable health systems in developed countries and not for emergent and rapidly growing health systems.

In terms of the empirical analysis, this study limited its scope to one year of orthopaedic surgical procedures (2014), but it is conceivable that the attractiveness and confinement of an orthopaedic department may change over time due to various reasons. For example, highly skilled and renowned surgeons may move from one department to another, or new regional investments may increase the service capacity or reachability of some departments. Although the possible dynamism in the network does not afect the validity of the proposed approach, gaining further insights from longitudinal studies is worthy of future research.

Finally, because diferent community definitions and detection al gorithms exist in literature (e.g. [41]), it is plausible that slightly different results might be achieved when shifting from one algorithm to another. In the present study, we applied the Louvain algorithm [15], which is considered highly accurate [55]. A systematic comparison of diferent algorithms requires a specifically designed study and goes beyond the aim of the present one; however, we recommend further research to clarify this methodological aspect.

## 8. Conclusions

A patient's choice is a complex phenomenon, determined not only by the prestige of providers, but also by other capabilities, such as physical accessibility and availability (e.g. length of waiting lists) or afordability (when considering non-universal health systems). In this study, an SNA was applied to map and analyse the patient's choice determinants with regard to orthopaedic surgery. To this end, administrative data on the surgical procedures performed in all 114 orthopaedic departments of the Lombardy region in 2014 was used for the analysis.

Both traditional SNA measures and other novel indicators, specifi cally developed for this study, were applied. In particular, a decision support matrix was defined so that decision makers could use it to evaluate departments' profiles, optimizing the location of services and allocation of resources, while preserving accessibility to care and patients' preferences. Two new indicators were introduced, namely at tractiveness and confinement, to characterize healthcare departments emphasising a patient's perspective; both indicators are calculated on a specific partition of the network, which comprises patients' origins (ZIP codes) and departments. The adoption of a community detection algorithm allows for clustering department nodes by similar patterns of patients' choices.

From a theoretical viewpoint, the present study is the first attempt to apply an SNA to investigate a patient's choice determinants and their implications on resource allocation decisions and healthcare service network planning. The identification via an SNA of communities of patients sharing common patterns of choice enables going beyond the limitations of current theory and practice, which refer to measures of physical accessibility (e.g. spatial distance or catchment area) only. The study also ofers initial insights on how an SNA could be used to assess the actual degree of freedom, at various geographical scopes, that the healthcare network grants to patients for diferent specialities. We argue that, in the face of possible high dynamism of patients' needs and preferences, the proposed approach is more adaptive and may lead to more robust resource allocation decisions, particularly when compared

[37] H. Magee, L.-J. Davis, A. Coulter, Public views on healthcare performance indicators and patient choice. Journal of the Roval Society of Medicine (7) (2o03) 96

to the rigidity of approaches based on the ex-ante definition of catch ment areas.

The present study also contributes to practice by ofering decision makers consistent metrics for understanding a patient's choice determinants and a decision support matrix to integrate them into resource allocation decisions. In addition, it suggests setting attractive ness and confinement thresholds locally (i.e. at the sub-community level), where patients' choices are more constrained and rationalization decisions might severely hinder their access to care.

Future application-oriented research could focus on the joint analysis of a larger spectrum of healthcare specialities, or even on benchmarking diferent regional healthcare systems by applying the same algorithm and set of indicators. This is possible because the proposed indicators are neutral and do not consider any specific aspect of the department's speciality. Considering that hospitals and other healthcare facilities are generally multi-speciality centres, and that patients also tend to move beyond regional borders, it is conceivable that crossspecialities or cross-regional analyses could contribute to more consistent planning of distributed healthcare services for an optimal allocation of scarce resources that truly recognises patients' rights and preferences.

## Declarations of interest

None.

## Acknowledgment

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors and is based only on a framework agreement with the Lombardy Region Health General Directorate that regulates free access to administrative data for research purposes.

## References

[1] S. Adeyemi, E. Demir, T. Chaussalet, Towards an evidence-based decision making healthcare system management: modelling patient pathways to improve clinical outcomes, Decision Support Systems 55 (1) (2013) 117–125

[2] R.M. Andersen, Revisiting the behavioral model and access to medical care: does it

[3] T.W. Anderson, D.A. Darling, Asymptotic theory of certain ‘goodness of fit’ criteria based on stochastic processes, The Annals of Mathematical Statistics (1952) 193–212.

[4] Apparicio, P., Abdelmajid, M., Riva, M., & Shearmur, R. (2008). Comparing alternative approaches to measuring the geographical accessibility of urban health services: distance types and aggregation-error issues. International Journal of Health Geographics, Z. art, no. 7.

[5] M.B. Ayed, H. Ltifi, C. Kolski, A.M. Alimi, A user-centered approach for the design and implementation of KDD-based DSS: a case study in the healthcare domain. Decision Support Systems 50 (1) (2010) 64–78.

[6] X. Bai, R. Gopal, M. Nunez, D. Zhdanov, A decision methodology for managing operational efficiency and information disclosure risk in healthcare processes. Decision Support Systems 57 (2014) 406–416.

[7] A.L. Barabási, Network Science, Cambridge University Press, Cambridge, UK, 2016.

[8] A.L. Barabási, R. Albert, Emergence of scaling in random networks, Science 286 (5439) (1999) 509–512

[9] A.L. Barabási, H. Jeong, Z. Néda, E. Ravasz, A. Schubert, T. Vicsek, Evolution of the social network of scientific collaborations. Physica A: Statistical Mechanics and its Applications 311 (3–4) (2002) 590–614

[10] A.L. Barabasi, Z.N. Oltvai, Network biology: understanding the cell's functional organization, Nature Reviews Genetics 5 (2) (2004) 101.

[11] J. Barjis, G. Kolfschoten, J. Maritz, A sustainable and afordable support system fo rural healthcare delivery, Decision Support Systems 56 (2013) 223–233.

[12] V. Batagelj, N. Kejzar, S. Korenjak-Cerne, Analysis of the customers' choice networks: an application on Amazon books and CDs data, Metodoloski Zvezki 4 (2) (2007) 191.

[13] I. Bejleri, R. Steiner, D. Nef, S. Yoon, M. Bumbach, Informing planning to address health care disparities: Assessing spatial accessibility to health care using GIS analysis. CUPUM 2015 - 14th International Conference on Computers in Urban Planning and Urban Management. 2015.

[14] O. Berman, D. Krass, J. Wang, Locating service facilities to reduce lost demand, IIE Transactions (Institute of Industrial Engineers) 38 (11) (2006).

[15] V.D. Blondel, J.L. Guillaume, R. Lambiotte, E. Lefebvre, Fast unfolding of communities in large networks. Journal of Statistical Mechanics: Theory and

Experiment 10 (2008) P10008.

[16] S. Boccaletti, V. Latora, Y. Moreno, M. Chavez, D.U. Hwang, Complex networks: structure and dynamics, Physics Reports 424 (4–5) (2006) 175–308.

[17] D. Chambers, P. Wilson, C. Thompson, M. Harden, Social network analysis in healthcare settings: a systematic scoping review, PLoS One 7 (8) (2012) e41911, , https://doi.org/10.1371/journal.pone.0041911.

[18] C. Chanut, L. Boyer, S. Robitail, C. Horte, B. Jacqueme, B. Giusiano, P. Auquier, L'analyse des réseaux sociaux appliquée au système de santé, Santé Publique 17 (3) (2005) 403–415.

[19] W. De Nooy, A. Mrvar, V. Batagelj, Exploratory Social Network Analysis with Pajek, vol. 27, Cambridge University Press, Cambridge, UK, 2011.

[20] A. Dixon, R. Robertson, R. Bal, The experience of implementing choice at point of referral: a comparison of the Netherlands and England, Health Economics, Polic and Law 5 (3) (2010) 295–317

[21] G.M. Erickson, S.A. Finkler, Determinants of market share for a hospital's services, Medical Care 23 (8) (1985)

[22] Fortney, J., Rost, K., & Warren, J. (2000). Comparing alternative methods of measuring geographic access to health services. Health Services and Outcomes Research Methodology, 1(2), art. no. 265228.

[23] S. Fortunato, Community detection in graphs, Physics Reports 486 (3) (2010) 75–174.

[24] L. Freeman, The development of social network analysis, Studies in Sociology of Science 1 (2004).

[25] J. Frenk, D. De Ferranti, Universal health coverage: good health, good economics, The Lancet 380 (9845) (2012) 862–864

[26] P. Groves, B. Kayyali, D. Knott, S. Van Kuiken, The ‘big data’ revolution in healthcare, McKinsey Quarterly 2 (3) (2013).

[27] M.F. Guagliardo, Spatial accessibility of primary care: concepts, methods and challenges, International Journal of Health Geographics, 3, art. no. (2004) 3.

[28] M. Gulliford, J. Figueroa-Munoz, M. Morgan, D. Hughes, B. Gibson, R. Beech, M. Hudson, What does 'access to health care' mean? Journal of Health Service Research and Policy 7 (3) (2002)

[29] G.A. Higgs, Literature review of the use of GIS-based measures of access to health care services, Health Services and Outcomes Research Methodology 5 (2) (2004).

[30] Jain, V., & Sakhuja, S. (2014). Structural investigation of a healthcare value chain: A social network analysis approach. Industrial Engineering and Engineering Management (IEEM), 2014 IEEE International Conference (pp. 179–183).

[31] Levesque, J. -F., Harris, M. F., & Russell, G. (2013). Patient-centred access to health care: Conceptualising access at the interface of health systems and populations. International Journal for Equity in Health, 12(1), art. (no. 18).

[32] Y. Li, A. Vo, M. Randhawa, G. Fick, Designing utilization-based spatial healthcare accessibility decision support systems: a case of a regional health plan, Decision Support Systems 99 (2017) 51–63.

[33] L. Liaropoulos, I. Goranitis, Health care financing and the sustainability of health systems, International Journal for Equity in Health 14 (1) (2015) 80.

[34] P.L. Logunov, Characterization of an exponential distribution, Journal of Mathematical Sciences 69 (4) (1994) 1178–1181.

[35] J. Luo, Integrating the huf model and floating catchment area methods to analyze spatial access to healthcare services, Transactions in GIS 18 (3) (2014) 436–448.

[36] W. Luo, F. Wang, Measures of spatial accessibility to health care in a GIS en vironment: synthesis and a case study in the Chicago region. Environment and Planning B: Planning and Design 30 (6) (2003) 865–884

[38] L. Mao, D. Nekorchuk, Measuring spatial accessibility to healthcare for populations with multiple transportation modes. Health & Place 24 (2013) 115–122.

[39] M.R. McGrail, Spatial accessibility of primary health care utilising the two step floating catchment area method: an assessment of recent improvements, International Journal of Health Geographics 11 (1) (2012) 50

[40] M.A. McGuirk, F.W. Porell, Spatial patterns of hospital utilization: the confinement of distance and time, Inquiry (1) (1984) 21.

[41] P. Nerurkar, M. Chandane, S. Bhirud, A comparative analysis of community de tection algorithms on social networks, Computational Intelligence: Theories Applications and Future Directions-Volume I, Springer, Singapore, 2019, pp 287-298

[42] E. Otte, R. Rousseau, Social network analysis: a powerful strategy, also for the information sciences, Journal of Information Science 28 (6) (2002) 441–453.

[43] G.C. Pascoe, Patient satisfaction in primary health care: a literature review and analysis, Evaluation and Program Planning 6 (3–4) (1983).

[44] M. Pinzone, E. Lettieri, C. Masella, Proactive environmental strategies in healthcare organizations: drivers and barriers in Italy, Journal of Business Ethics (2014) 1–15.

[45] G. Radaelli, E. Lettieri, C. Masella, L. Merlino, A. Strada, M. Tringali, Implementation of Eunethta core model in Lombardia: the VTS framework, International Journal of Technology Assessment in Health Care 30 (1) (2014) 105–112.

[46] A. Ranerup, L. Norén, C. Sparud-Lundin, Decision support systems for choosing a primary health care provider in Sweden, Patient Education and Counseling 86 (3) (2012).342-347

[47] B. Shengelia, A. Tandon, O.B. Adams, C.J.L. Murray, Access, utilization, quality, strategy, Social Science and Medicine 61 (1) (2005).

[48] P. Sivey, The effect of waiting time and distance on hospital choice for English cataract patients, Health Economics 21 (4) (2012) 444–456.

[49] M.C. Tremblay, R. Fuller, D. Berndt, J. Studnicki, Doing more with more information: changing healthcare planning with OLAP tools, Decision Support Systems 43 (4) (2007) 1305–1320.

[50] V. Verter, S. Lapierre, Location of preventive health care facilities, Annals of Operations Research 110 (1–4) (2002).

[51] A. Victoor, R.D. Friele, D.M. Delnoij, J.J. Rademakers, Free choice of healthcare providers in the Netherlands is both a goal in itself and a precondition: modelling the policy assumptions underlying the promotion of patient choice through documentary analysis and interviews, BMC Health Services Research 12 (1) (2011) 441.

[52] A. Victoor, D.M. Delnoij, R.D. Friele, J.J. Rademakers, Determinants of patient choice of healthcare providers: a scoping review, BMC Health Services Research 12 (1) (2012) 272.

[53] F. Wang, Measurement, optimization, and confinement of health care accessibility: a methodological review, Annals of the Association of American Geographers 102 (5) (2012) 1104–1112.

[54] F. Wang, W. Luo, Assessing spatial and nonspatial factors for healthcare access: towards an integrated approach to defining health professional shortage areas, Health & Place 11 (2) (2005) 131–146.

[55] Z. Yang, R. Algesheimer, C.J. Tessone, A comparative analysis of community detection algorithms on artificial networks, Scientific Reports 6 (2016) 30750.

![](/api/attachments/2V8NCENC/fulltext/images/5ef27198e4a6fe19b21683527376a6f686720342cc04ae1bda9b70f018dde96e.jpg)

Prof. Fernanda Strozzi, PhD is an associate professor at Cattaneo university. She is graduated in Mathematics and received her PhD in Chemical Engineering. Her main research interests include Social Network Analysis, Theory of Nonlinear Systems and Time Series Analysis. On these is sues, she is the author of more than 100 papers in peerreviewed journals and she has been the coordinator of European funded projects on the sensitivity of chemical reactions and on man-made complex networks such as power grids and supply chains.

![](/api/attachments/2V8NCENC/fulltext/images/dd73c9292576810987d3e06e9b64be3fa27b4d6d673417ad6721195e77f84d5a.jpg)

![](/api/attachments/2V8NCENC/fulltext/images/5a10d8d2bb3ecd199dfb49dc8925915eec90bc9eb629a7f0cbc51b4967c88783.jpg)

Ing. Elisabetta Garagiola, PhD is a lecturer. She has participated in many research projects with a particular focus on the implementation of health management tools. She worked on the optimization of the processes in the Neurology and Ophthalmology Operative Units, on the mapping and economic valorization of the pathway of the HIV patient and the septic patient, on the evaluation of the impact on the regional budget of the breast screening pathways and the new pharmacological treatments for the pathology of HCV.

Prof. Paolo Trucco, PhD is Full Professor of Risk Management at the School of Management, Politecnico di Milano, where he is also Director of the PhD Programme in Management Engineering. His research interests concentrate in planning complex socio-technical systems under uncertainty, with expertise in the manufacturing, oil&gas, energy, transportation, and healthcare sectors. He is author of more than 250 publications and coordinated international and national projects on healthcare operations management, patient safety, eHealth and telemedicine. He is advisor of the Lombardy Region Government (Italy) on Healthcare Risk Management and Clinical Governance. He regularly trains healthcare managers on operations and risk management subjects.
