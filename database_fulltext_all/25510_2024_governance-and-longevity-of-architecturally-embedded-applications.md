---
otero_id: 25510
otero_key: "JA5UYB8B"
title: "Governance and Longevity of Architecturally Embedded Applications"
authors: "Karl Akbari; Daniel Fürstenau; Till J. Winkler"
year: "2024"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2023.2301169"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
∂ OPEN ACCESS

Check for updates

# Governance and Longevity of Architecturally Embedded Applications

Karl Akbari <sup>a</sup>, Daniel Fürstenau <sup>b</sup>\*, and Till J. Winkler <sup>c,d</sup>\*

<sup>a</sup>National Taiwan University of Science and Technology, Department of Business Administration, Taipei City, Taiwan (R.O.C.); <sup>b</sup>IT University of Copenhagen, Department of Business IT, Copenhagen; <sup>c</sup>University of Hagen, Faculty of Business Administration and Economics, Hagen, Germany; <sup>d</sup>Copenhagen Business School, Department of Digitalization, Howitzvej, Frederiksberg, Denmark

## ABSTRACT

This study explores the relationship between the governance of architecturally embedded applications and their longevity in organizational use. Using a contingency-fit logic, it posits that alignment between application governance (distribution of decision rights) and architectural contingencies contributes to sustained durations of organizational use. Architectural contingencies include internal application modularity, application inter-connectedness, and governance of surrounding application clusters. Evidence for the governancearchitecture fit hypothesis is derived from analyzing temporally ordered data about applications (n = 225, n = 498, n = 193) from organizations in the media, banking, and utilities sectors over five years. Using a two-step approach with ordinal regression, along with Cox proportional hazards and logistic regression models, our findings indicate that a fit between observed governance and the governance induced by architectural contingencies reduces the likelihood of application decommissioning. The study advances the fields of information systems (IS) governance and architecture by ofering a micro-level perspective on the longevity of organizational IS use while also shedding light on the importance of governance choices aligned with unique architectural application properties.

## KEYWORDS

Digital infrastructure; Application governance; Application longevity; Application discontinuance; Information-systems architecture; Modular systems; Contingency fit; Survival analysis

## Introduction

The digital infrastructure that enables businesses to keep pace in today’s rapidly changing economies is a complex, ever-evolving network of diverse, interdependent applications [24, 38, 63]. This network, often called the information systems (IS) architecture [17], is crucial in determining company competitiveness. It requires careful management, including critical design decisions about the adoption and phasing out of applications and the effective governance of these systems throughout their entire lifespan, which can span several months to several decades [22, 54].

Although the lifetime costs of applications often surpass the initial costs of implementation by a substantial margin, up to five to 20 times [42], previous research in IS has traditionally focused on the planning, adoption, and assimilation of IS, neglecting the governance of individual applications over their lifetimes and their embeddedness in complex and ever-evolving IS architectures [1]. Application governance is a major concern for companies. One case in point is illustrated by Gregory et al. [28], where a bank faced tensions due to its overly centralized governance of core applications without accommodating end-user decision rights. Such misaligned application governance may have consequences for the long-term value creation underexplored in research and practice.

This study aims to fill the gap in understanding how the governance of applications embedded in IS architectures influences their longevity, defined as the duration of organizational use. We refer to application governance as the distribution of application planning and change-coordination rights across a spectrum of more decentralized or centralized archetypes [76]. Previous IS governance research has mostly focused on archetypes at the organizational level of the overall IS function and emphasized that certain contingencies (i.e., possible but not coercive conditions) influence the adequacy of a specific IS governance archetype [55, 72]. However, a growing body of research has emerged that focuses on the micro-level of application governance [64, 76, 79], recognizing that governance for information technology (IT) artifacts today is distributed across multiple stakeholders in organizations.

Nevertheless, this research has not yet fully considered the interdependency of applications, suggesting governance choices are made in isolation. In contrast, the IS architecture literature has acknowledged the interdependency of applications as a central concern [33, 45, 73], but has paid limited attention to their governance. Similarly, studies on IS discontinuance [22, 53, 62] have so far overlooked the potential role of governance in determining discontinuance intentions and thus application longevity.

Previous work has recognized the interrelation between IS architecture and governance [35, 67, 68] and the importance of survivability of applications in supporting organizational performance and extracting value [1]. Tiwana and Konsynski’s [67] study addressed modularity and governance decentralization for organizational agility. However, a microlevel understanding of how application architecture interacts with governance to affect longevity is elusive. This leaves corporate managers without crucial insights for structuring governance frameworks that can sustain long-term application value in evolving IS architectures.

This study builds on the contingency-theoretic premise of the IS governance literature [55], recognizing that no single decision rights distribution fits all organizational IS architecture applications. In the governance-architecture discourse, we explore the role of an application’s governance fit with its unique architectural contingencies in sustaining application longevity. We address the question: How does the fit of application governance with its architectural contingencies affect the longevity of an application in an organizational context?

Taking our vantage point in a modular systems view, this study identifies three architectural contingencies on micro and meso levels and hypothesizes their associations with application governance: (1) internal modularity, (2) inter-connectedness, and (3) cluster governance. After adopting a contingency-fit logic [70], we derive the central hypothesis that the fit of application governance with the governance collectively induced by these contingencies reduces the likelihood of decommissioning and, thus, is conducive to longevity.

Comprehensive temporally ordered archival data collected from three organizations (MEDIA, n = 225; BANKING, n = 498; and UTILITIES, n = 193 applications), covering multiple years and including architectural network information, provide consistent support through ordinal regression analyses for associations between the three contingencies and application governance. Cox proportional-hazards regressions of fit (operationalized as the match of observed and induced governance) on the longevity durations included in the first two datasets (MEDIA and BANKING) display 58% and 54% lower probabilities of application decommissioning, respectively, in the presence of fit over five-year periods. Logistic regressions of fit on the binary survival outcomes for the third dataset (UTILITIES) yield a 64% lower likelihood of application decommissioning in the presence of fit after a similar period.

The findings consistently support the governance-architecture fit hypothesis across all three cases. This study makes three main contributions to the fields of governance, architecture, and discontinuance in IS. First, it embraces micro and meso levels in IS governance, which results in a theory about how to make application governance choices in a way that favors the longevity of applications. Second, the study extends the coevolutionary view of IS architecture and governance by providing evidence for contingencies of application governance with architectural properties on multiple levels. Third, our study establishes a novel nomological linkage between governance and discontinuance by demonstrating that the governance-architecture fit decreases the likelihood of application decommissioning.

## Theoretical Development

## Modular Systems

A modular systems view involves recognizing systems as composed of interconnected subsystems, each capable of dynamic adaptation to internal and external changes, thereby ensuring the system’s overall survivability [58, 65]. The principle of decomposability in these systems facilitates the reconfiguration of components into more stable structures, providing essential adaptability amid changing environments [58].

This study examines the organization-wide IS architecture as a modular system comprising a network of interrelated and heterogeneous internally or externally provided applications, each governed by different stakeholders, see Figure 1. The IS architecture is a critical aspect of a firm’s digital infrastructure, which encompasses the IT, organizational structures, and related services and facilities necessary for the enterprise to operate [63].

At a macro-level, the complexity inherent in IS architecture is often managed by IT portfolio managers and enterprise architects. These professionals maintain a smooth integration of applications, accommodating changes to keep complexity at bay [47]. At a micro level, the agency extends further to different organizational roles exercising agency over individual applications, bundles of IT functions used to support business processes [34]. These roles range from application owners, responsible for key decisions and resources, to regular users, who may influence features through their feedback [50, 64].

Between the individual application and overarching IS architecture network, a gap persists in our understanding of structures between individual applications and IS architecture network. We posit that the meso level contains specific clusters of applications characterized by high internal coherence and distinct inter-cluster differentiation. The management of these clusters is not uniform, as it hinges on the organizational context: some firms assign dedicated IT architecture domain managers for oversight, while others operate without clearly delineated managerial structures for these specific segments.

![](/api/attachments/JA5UYB8B/fulltext/images/aa9752dcb101c466c73a8c951e5073a59793c46ee40a48921cff2bdfb6024d4d.jpg)  
Figure 1. Multi-level view of IS architecture and governance

Zooming deeper into the IS architecture, the application artifact itself has an external and internal micro-architecture [65]. Externally, it is typically inter-connected with other applications enabling basic functionalities and business process flows. This is achieved through application integration techniques and protocols, including point-to-point connections and APIs. Internally, applications are constituted by more or less self-contained internal modules [65]. Modules are logically grouped pieces of code encapsulating subfunctionality in the development of the software. An application’s degree of modularity is the defining property of a system [69]. It determines, amongst others, its client-sided customizability [61] and extensibility [65].

Overall, the modular systems view asserts that IS architectures are not solely controlled by a centralized authority. Instead, they consist of stable, independently governed subsystems. Nevertheless, micro-level decision and resource allocation structures—and resulting decision and action patterns—, so we posit, depend on meso and macro level structures.

## Application Governance

From the perspective of a modular systems view, application governance links the human agency and technological components that comprise the IS architecture (Figure 1). Although central to IS governance, application governance is not always clearly defined [66]. The bulk of previous IS governance studies [9, 55, 72] have taken a macro-level view of governance, assuming a centralized, decentralized, or hybrid approach across applications.

In contrast, a micro-level view of application governance provides more nuanced insight into the different emerging forms of business-managed IT, including shadow IT [31], lightweight IT [11], bottom-up IS [12], and everyone’s IT [28]. For instance, governance for cloud applications is often uncorrelated with the governance of the overall IT organization [76].

The concept of application governance, as per the agency-theoretic premise of distinguishing decision control and decision implementation rights [19], consists of two critical classes of decision rights [76, 78]. These classes include (1) the authority over applicationrelated planning decisions (e.g., making decisions regarding application requirements, usage, and investment) and (2) the responsibility for coordinating changes (e.g., deciding how to enhance an application functionally). Decision rights can be allocated to more centrally positioned actors, such as IT units, or more decentrally positioned actors, such as business units.

In this study, the term IT units refers to all organizational entities that receive a mandate from senior management to provide IT services, whereas all other units are considered business units. This study defines four application governance archetypes that conceptualize application planning and change-coordination rights for these organizational units, as displayed in Table 1. The four archetypes are IT owned, business IT owned, business owned, and business managed, and they range on a discrete scale from centralized to decentralized governance.

## Model Development

This section conceptualizes three architectural properties in IS architectures and hypothesizes their contingent influences on application governance. These properties include internal modularity, inter-connectedness, and surrounding cluster governance. The central hypothesis is that a governance-architecture fit, where application governance aligns with the collective influence induced by its architectural properties, is conducive to application longevity (i.e., durations of organizational use). This idea based on a contingency-fit logic is visualized in Figure 2.

## Internal Modularity

The internal modularity of an application is a micro-architectural property closely related to the decomposability of modular systems [59]. We define internal modularity as the extent to which an application can be decomposed into smaller, standardized, and customizable building blocks instead of being integrated and monolithic in structure. The modularity level in applications affects their modifiability level and perception of technical complexity from a business perspective [77] and their knowledge intensity from a central IT perspective [64]. We, therefore, propose the internal modularity as a first contingency for application governance.

Table 1. Application Governance Archetypes

<table><tr><td></td><td>IT owned (centralized)</td><td>Business IT owned</td><td>Business owned</td><td>Business managed (decentralized)</td></tr><tr><td>Decision control</td><td>Planning decisions with a central IT unit</td><td>Planning decisions with an IT unit within the business</td><td>Planning decisions with a business unit</td><td>Planning decisions with a business unit</td></tr><tr><td>Decision management</td><td>Change-coordination responsibility with a central IT unit</td><td>Change-coordination responsibility with a central IT unit</td><td>Change-coordination responsibility with a central IT unit</td><td>Change-coordination responsibility with a business unit</td></tr></table>

![](/api/attachments/JA5UYB8B/fulltext/images/e260b51d74f659c785701c289ebcfffc1b1e9ea31030861d86d3d3064e707cc6.jpg)  
Figure 2. Research Model

Monolithic solutions tend to be less accessible and adaptable, as observed in firstgeneration core banking solutions that still use monolithic designs, making even small changes (e.g., front end) difficult for end users and requiring extensive IT knowledge [27]. Thus, these applications are more efficiently governed by central IT units that specialize in building and adapting these applications and technology. End users, in contrast, increasingly prefer software that poses minimal technical requirements and often allows customization of modules (e.g., templates and workflows in productivity apps). End users who require responsiveness and have some technical knowledge may opt for customizable opensource solutions, cloud software, or standard software, sometimes managed individually as business-managed IT [41].

Customizability and adaptability can be achieved by more modular internal designs of the software [61]. Higher levels of modularity provide easier access and modification opportunities for end users and enable better integration with the existing IS architecture [75]. This approach leads to increased opportunities for decentralized changes and decision-making by business stakeholders with the technical knowledge to plan and coordinate their changes for highly modular applications [66]. In sum, we pose that an application’s internal modularity plays a significant role in its governance due to its influence on adaptability and extensibility. We posit the following:

Hypothesis 1 (Internal Modularity Contingency). Higher (lower) internal modularity is associated with more decentralized (centralized) governance.

## Inter-connectedness

Inter-connectedness is a micro-level architectural property that derives meaning from the modular systems concept of adaptation. Due to different degrees of connectivity, some components in a modular system have a higher importance in influencing the adaptive evolution of the entire system than other components [39]. In the nervous system of the human body, the brain and spinal cord have a central function to integrate received information about environmental changes and coordinate the activity of all body parts.

In this study of IS architectures, we conceptualize the inter-connectedness of an application as the number of other applications interconnected with a focal application (i.e., those that directly receive data from or transfer data to this application). In contrast to the internal modularity, inter-connectedness is a property of the external architecture of an application [65]. The higher the inter-connectedness of an application, the more the changes in it affect other applications, and the more it is affected by changes in other applications [17]. The inter-connectedness specifies the extent of data and processing dependencies at the level of the individual application. The inter-connectedness, therefore, helps distinguish the core and periphery in an architectural network [43]. Core applications with high interconnectedness, such as authentication, master data, transactional middleware, or other backend applications, often provide services to many other applications. In contrast, peripheral solutions are closer to the end user and consume data from or provide data to backend solutions [24].

Interconnectedness is likely to exert a contingent influence on application governance. The number of changes to be made and planning decisions to be taken increases with more dependencies. Therefore, for peripheral applications with low inter-connectedness, local business stakeholders are more likely to have more significant stakes in planning and coordinating changes, lowering the coordination cost because these applications fulfill the needs of specific user groups. In contrast, core applications with high inter-connectedness are more critical to the organization. Hence, they are likely governed in a more centralized structure to control risks associated with their criticality through specialized central IT units. Dreyfus and Iyer [17] argued that IT unit architects should focus solely on the governance of these architectural control points at the centers of the network to steer the overall architectural evolution in beneficial ways. Therefore, we expect applications with greater inter-connectedness to be governed more centrally due to coordination and control and posit:

Hypothesis 2 (Inter-connectedness Contingency). Higher (lower) inter-connectedness is associated with more centralized (decentralized) governance.

## Cluster Governance

The modular systems concept of decomposability suggests that complex networks tend to form modular clusters, where neighboring nodes influence each other [3]. This phenomenon can be observed in various fields, such as urban studies within sociology, where the neighborhood composition of ethnicity often converges to clear segregation even if each household has a weak preference for neighbors of the same ethnic group [56], or in business ecosystems [40], where cluster members benefit from complementarities. Some network scholars account for causal influences, but others recognize the role of homophily, or similarity among network members [3, 29]. This homophily can drive practice diffusion within groups, either through conformance to group norms or shared interventions [4, 48].

This study focuses on the similarity of governance archetypes among applications in the same cluster. We define cluster governance as the dominant governance archetype of the surrounding applications in the neighborhood of a focal application. Cluster governance ranges discretely between centralized and decentralized governance archetypes (Table 1). The neighborhood refers to a subset of applications with many connections with each other but relatively few connections with other applications in the architectural network (Figure 1). These clusters, being relatively independent subsystems of the IS architecture, have advantages in coordination costs and adaptation speed [58].

Given the modular system concept of adaptability and the arguments regarding network homophily, application governance is likely influenced by the governance of its surrounding applications (i.e., by cluster governance). The cluster governance concept assumes more homogeneous governance within a given subsystem cluster and more heterogeneous governance across different clusters. Similar governance within a cluster may decrease the coordination costs when necessary changes or decisions must be made due to dependencies between connected applications. These dependencies indicate that changes in one application (e.g., updates, overhauls, or replacements) require coordination with the owners of adjacent applications. Coordination costs may be lower if the decision rights for neighboring applications are allocated within the same organizational unit but higher if the decision rights for neighboring applications are allocated to more remote stakeholders. For example, coordination costs arise from the need for knowledge exchange to ensure the compatibility of various technologies. Thus, we expect the governance of each application in the architectural network to be contingent on the aggregated governance of the applications in the surrounding cluster. The hypothesis is as follows:

Hypothesis 3 (Cluster Governance Contingency). Cluster governance (i.e., whether more centralized or more decentralized) is positively associated with application governance.

## Application Longevity

From the vantage point of the modular systems theory, organizational needs change as the environment does, creating pressure toward retiring individual building blocks and adding new ones. In this context, decommissioning refers to the systematic process of taking applications out of service that are to be discontinued. Decommissioning itself can incur major costs since it includes activities such as migrating data, changing workflows, and retiring or reusing technical components. While factors influencing discontinuance decisions have been theorized with multiple application-related dimensions, such as application performance, suitability, and supportability [21, 22], we are particularly interested in the complementary role of application governance for application longevity (i.e., non-decommissioning).

The most identifiable mechanism to ensure application longevity is the investment made into the application, that is, the sustained flow of financial, human, and other resources [46]. Given the changing nature of the organizational, regulatory, technological, and competitive environment, investment decisions are often made based on the relevance of applications relative to others in the organization. This portfolio selection process is subject to agencytheoretic influences [16] and requires aligning potentially conflicting, or at least diverging, interests [57]. Governance is an essential complementary asset to derive value from IT investments [5]. Therefore, we expect applications for which the decision rights are distributed similarly to other ‘architecturally similar’ applications to receive adequate consideration in portfolio and architecture planning processes. These fittingly governed applications are likely to receive the necessary resources for long-term development and thus can continue to create value for the organization.

In contrast, deviating from the commonly accepted archetypes in an organization is likely to incur a cost, often called the misfit cost [15], such as when shielding or disguising the actual governance archetype. For example, in the case of covert ‘shadow IT’ applications, redundant support must be maintained, creating inefficiency [25, 41]. This cost of working against the commonly accepted archetypes might be covered temporally through buffer budgets or individual bootlegging efforts [14]. However, this might be too laborious in the long term, making decommissioning even more likely. Therefore, whether an application is governed in a fitting archetype may play a key role in its investment approval, influencing decision-making regarding continued use.

According to the three theoretically derived contingencies, this research discusses the most common governance for an application in a specific organizational setting, as the governance jointly induced by the application’s architectural properties. We distinguish this conceptually from the governance that can be observed. For example, following the contingency arguments, a highly modular application with low inter-connectedness embedded in a cluster of decentralized applications is likely to induce a highly decentralized (i.e., business-managed) governance archetype. In contrast, a monolithic application with high inter-connectedness embedded in a cluster of central applications induces a highly centralized (i.e., central IT owned) governance archetype.

In line with the multiple contingency logic [55], these three contingencies act concurrently and in concert, such that opposing forces between some contingencies (e.g., high internal modularity vis-à-vis a high inter-connectedness) may counteract one another. Hence, governance archetypes that fall between the two centralization/decentralization extremes may result from a complex interaction of (potentially opposing) forces induced by the three contingent properties. Moreover, organizations may have different organizationally determined preferences in weighting between various contingent forces. This situation is because different organizational settings provide various macro-level contexts (e.g., in competitive strategy, industry stability, and overall IT governance) in which application governance is shaped [8].

Although a correspondence between the observed governance and the induced governance is conducive to application longevity, deviations from the induced governance occur due to the nature of organizational actors enacting local practices and deviating from implicit or explicit organization-wide practices [49]. Consequently, we discuss fit if the observed governance matches the induced governance and misfit if a mismatch exists between the observed and induced governance. Prior research has used equivalent conceptualizations of fit to theorize the adequacy of IS governance at the organizational level. Gu et al. [30] demonstrated that firms with a low IS governance misfit obtain two to three times the value from IT investments than firms with a high IS governance misfit. We posit that if the application governance archetype fits its architectural properties, an organization is more likely to invest in this application over a longer period and less likely to decommission it. We posit the governance-architecture-fit hypothesis as follows:

Hypothesis 4 (Governance-Architecture Fit). The fit of application governance with architectural properties decreases the likelihood of application decommissioning.

Table 2: Constructs and Definitions

<table><tr><td>Construct</td><td>Definition</td><td>Operationalization</td><td>Guiding references</td></tr><tr><td>Application longevity</td><td>Continued operation and organizational use of an application over a predefined period</td><td>Duration in days of operation within the periodBinary attribute0: Inactive at the period end1: Active at the period end</td><td>Agarwal &amp; Tiwana [1]Swanson &amp; Dans [62]Furneaux &amp; Wade [22]</td></tr><tr><td>Application governance</td><td>Distribution of application planning and change-coordination decision rights for an individual business application</td><td>Four rank-ordered archetypes1: IT owned2: Business IT owned3: Business owned4: Business managed</td><td>Winkler &amp; Brown [76]Tiwana &amp; Konsynski [67]Brown &amp; Magill [9]Xue et al. [80]</td></tr><tr><td>Internal modularity</td><td>Extent to which an application can be decomposed into smaller standardized and customizable building blocks (instead of being integrated and monolithic)</td><td>Five rank-ordered types1: Closed legacy software2: Modified software3: Customizable software4: Open software5: Modular end-user software</td><td>Simon [59]Subramanyam et al. [61]Tiwana [65]Tiwana &amp; Safadi [69]</td></tr><tr><td>Inter-connectedness</td><td>Number of other applications interconnected with the focal application</td><td>Degree of information flow dependencies in the architectural network</td><td>Dreyfus &amp; Iyer [17]MacCormack &amp; Lagerström [45]Fürstenau et al. [24]</td></tr><tr><td>Cluster governance</td><td>Dominant governance archetype of surrounding applications in the neighborhood of a focal application</td><td>Median of the governance of all applications in the focal application&#x27;s neighborhood cluster</td><td>Simon [58]David [15]</td></tr><tr><td>(Governance-Architecture) Fit</td><td>Correspondence between observed governance and that collectively induced by architectural contingencies, i.e., whether decision rights are allocated consistently with architecturally similar applications</td><td>1: Observed governance matches induced governance0: Observed governance does not match the induced governance</td><td>Misztal [49]Gu et al. [30]</td></tr></table>

Table 2 summarizes the primary constructs, definitions, guiding references, and operationalization. Operationalization is explained in detail in the next section.

## Methods

This research draws on comprehensive archival data from three case organizations: BANKING, MEDIA, and UTILITIES.<sup>1</sup> These organizations were suitable because they (1) have sufficient size and complexity to require structured IT management. Moreover, they (2) span a range of industries and organizational design structures, allowing for a logic of replication in testing the research model [81]. Additionally, they (3) built an enterprise architecture function that systematically collected information on the IS architecture structure, including information flows. Last, (4) it was vital that the case organizations could provide historical information over multiyear timeframes to determine the longevity of their applications.

Table 3: Case Organization Overview

<table><tr><td>Case</td><td>Total assets</td><td>Employees</td><td>Core activities</td><td> $Apps.^1$ </td><td>IT function  $structure^2$ </td></tr><tr><td>MEDIA</td><td>2 billion euros</td><td>~4,500</td><td>Production, program planning, and broadcasting</td><td>225</td><td>Centralized and decentralized</td></tr><tr><td>BANKING</td><td>46 billion euros</td><td>~3,500</td><td>Account management (private and corporate) and treasury</td><td>498</td><td>Centralized and shared service provider</td></tr><tr><td>UTILITIES</td><td>0.5 billion euros</td><td>~8,000</td><td>Sales/distribution, operations, and financials for waste disposal</td><td>193</td><td>Centralized (corporate and waste management) and decentralized</td></tr></table>

<sup>1</sup>Clean number of applications considered from the enterprise architecture repository.<sup>2</sup> Categorization based on archetypes in Winkler and Brown [74].

## Case Organizations

Table 3 provides an overview of the size, core activities, and IT functions of the case organizations.

MEDIA is a European television broadcaster with total assets of around 2 billion euros, employing around 4,500 people. Its IT function comprises two types of IT units: first, an IT department central to the focal organization employing around 275 people and, second, more decentralized business-IT units serving the needs of one or several business departments, such as IT for accounting, finance, purchasing, or human resources. In addition, end users in the business departments exert decision rights over some applications. Applicationrelated planning and change-coordination responsibilities are shared between these three types of stakeholders (i.e., the central IT department, business-IT units, and business end users). The acquired data stem from the architecture team positioned within the central IT department. The company has built its architecture function since 2008 and has maintained high stability and high-quality architecture data due to consistent funding and staffing of central functions related to the transparency requirements of a public corporation.

With total assets of around 46 billion euros, 3,500 employees, 1.3 million private and 80,000 corporate customers, BANKING is a larger regional bank in Germany. Its IT function is organized into two tiers, with an IT unit centrally positioned within the organization and a shared service provider serving a group of banks with a common brand of which BANKING is a part. Application owners in the business units are assigned planning responsibilities for some applications. The IT strategy over the last years for BANKING has been to decommission individual shadow IT and migrate the operation of many of their larger applications to a shared service provider, primarily due to cost pressures and tendencies to shrink internal operations. Due to the high regulatory pressures in the European banking sector (e.g., Sarbanes-Oxley Act and Solvency II), BANKING has to maintain a high level of transparency and quality of the data in their enterprise architecture repository.

UTILITIES is a privately owned waste and recycling company with total assets of around 500 million euros and 8,000 employees. The company operates in communal and private waste services, steel and metal recycling, facility management, and other related services across regions in Germany, Eastern Europe, and Asia. The IT organization of UTILITIES comprises two centralized and several decentralized IT units. A central IT unit comprising around 15 employees serves the corporate level of the organization and runs central systems, such as the financial or accounting systems. In the waste management division, one of the largest business units of the company, another central IT unit employs around 25 people and serves many of the group organizations. Several smaller decentralized IT units have local IT representatives in regional group companies. The entry point was the central IT unit for waste management, which had built an architectural overview of all of its applications prior to a large enterprise transformation project targeting its core waste management systems.

## Data Collection and Processing

The three case organizations provided proprietary data from their enterprise architecture repositories for the purpose of this study. For MEDIA, data were collected at four time points between 2015 and 2020, specifically January 2015 $\left( \mathrm { t } _ { 0 } \right)$ , November 2016 $\left( \mathrm { t } _ { 1 } \right)$ , August 2018 $\left( \mathfrak { t } _ { 2 } \right)$ , and April 2020 $\left( \mathbf { t } _ { 3 } \right)$ . The data from 2015 comprised n = 225 items, all representing business applications as defined in this study, including externally provided applications that the company’s IS architecture interfaced with.

The data in the analysis for BANKING were collected from four datasets representing snapshots of the enterprise architecture repository from 2016 to 2020. The snapshots were taken at various time points, specifically in May 2016, January 2019, April 2020, and August 2020. The 2016 dataset comprised 1,363 items, each representing an individual application. Exclusions were made for items that did not adhere to the definition of a business application (e.g., pure server or network components) and for those that lacked information regarding the application governance, including the application ownership, responsible business unit, and operational ownership. Thus, we included a total of n = 498 individual applications.

For UTILITIES, we analyzed data from two points in time: 2011 and 2015.<sup>2</sup> The 2011 dataset was from February 2011 and comprised 457 individual items. For 2015, we collected project portfolio data and retrieved a list of applications decommissioned in the course of a large enterprise system implementation. We removed duplicates of the same applications to ensure accuracy, resulting in a clean dataset of n = 193 business applications.

## Operationalization of Variables

The preprocessing of the datasets involved several steps.<sup>3</sup> The dependent variable application longevity, defined as the continued operation and use of an application over a specified period, was operationalized as a duration in days within the given periods for MEDIA and BANKING, and as a binary attribute for UTILITIES, with “1” indicating an active and “0” indicating an inactive application, at the end of the given periods. Longevity thus considered a 4- to 5-year window for each case (2015–2020 for MEDIA, 2016–2020 for BANKING, and 2011–2015 for UTILITIES).<sup>4</sup> For MEDIA and BANKING, we validated the decommission date in the datasets by cross-referencing it with the presence or absence of the application in subsequent datasets. This approach enabled us to determine the durations accurately.

For MEDIA, all other model variables (i.e., application governance, internal modularity, inter-connectedness, cluster governance, and fit) were calculated at the three observation points $( \mathrm { t } _ { 0 } , \mathrm { t } _ { 1 } , \mathrm { a n d t } _ { 2 } )$ . For BANKING and UTILITIES, raw data for the model factors was available only at the beginning of the observation periods (i.e., in 2016 for BANKING, and 2011 for UTILITIES), which resulted in a time-invariant design. Post-hoc analyzes for MEDIA corroborate that, while variations in application governance (for 4 applications) and architectural properties over time lead to changes in fit for some applications (36 out of 225), these variations did not significantly change our results (Figure A.1 in Online Appendix A).

Application governance, the distribution of application planning and change-coordination decision rights, was operationalized in line with the theoretical conceptualization using four rank-ordered governance archetypes (Table 1). Consequently, each application was unambiguously assigned to one of the following archetypes: 1) IT owned, 2) Business IT owned, 3) Business owned IT, and 4) Business managed IT. Coding was performed based on existing fields regarding application responsibility in the data. Two of the authors conducted the coding and discussed discrepancies. Coding was confirmed for a subset of the applications by the key informants as applicable to describe application governance. For UTILITIES, we distinguished two IT owned archetypes by adding a fifth archetype at the centralized (lower) end of the scale, describing applications where planning decisions and change coordination are controlled by corporate IT (instead of central IT). This scale was reflective of UTILITIES’s corporate structure with the two tiers of central and corporate IT departments. In line with our theoretical conceptualization, the coded application governance archetypes from the datasets were considered observed governance.

To test the governance-architecture fit hypothesis, we operationalized induced governance and fit in line with the theory development. We measured induced governance as the archetype to be considered most likely, based on the models that included the three architectural contingencies (H1-H3) and control variables (see next section Analysis Method).<sup>5</sup> Then, we set the binary variable fit to “1,” where the induced governance was identical to the observed governance, and to “0,” where induced governance and observed governance were unequal. The binary operationalization of fit is appropriate given the ordinal (i.e., nonmetric) nature of the application governance scale because (positive or negative) deviations from an ordinal variable cannot be compared.

Internal modularity, the level to which an application can be decomposed into standardized and customizable building blocks, was assessed on a discrete five-point scale tapping into the application’s technology base and its inherent possibilities for loose coupling, extendibility, and user-based customization. We defined the five rank-ordered types of internal modularity as follows. (1) Closed legacy software denotes monolithic applications that run on technological bases that do not correspond to current market standards. These integrated applications make it difficult for developers to add extensions. (2) Modified software refers to formerly monolithic applications gradually opened up over time through client- and server-side extensions to enhance functionality and better control the application. As these applications do not commonly offer standard application programming interfaces, such modifications often require dealing with internal intricacies.<sup>6</sup> (3) Customizable software refers to proprietary applications inherently designed for adaptation and integration into a specific company setting. Customizations are typically performed during implementation by configuring various application modules. Adaptations and extensions can be implemented by customdeveloped code that uses the application’s built-in programming interfaces (APIs). (4) Open software denominates applications that build on nonproprietary technology. Besides being ready for use in their default form, open software affords and often requires customization to a specific setting and typically allows for such customization and extensibility through a trained base of end users. (5) End-user software includes desktop and cloud applications accessible to the user with a low level of difficulty performing customizations (e.g., MS Excel macros). The modularity of these applications thus extends to the user interfacing functionalities, although their customizability is typically limited to what the software permits by design via its desktop or web front end.

Internal modularity was coded based on the descriptive fields in the repository on the application’s technological basis. For UTILITIES, we drew on a binary coding of more modular versus more monolithic software, given the limitations of the data in this dimension. One author and a research assistant coded the data independently (Cohen’s kappa $\kappa = 0 . 7 8$ for MEDIA, $\kappa = 0 . 7 1$ for BANKING, and $\kappa = 0 . 6 3$ for UTILITIES). The remaining discrepancies were resolved in consensus between the two coders and, where necessary, by considering the opinion of a third coder. The coding results were cross-validated by the company informants.

Inter-connectedness, the number of other applications interconnected with the focal application, was calculated after network-analytical processing of the data. Each application was considered a node, and each information flow was a link. In line with prior authors [17, 24], we used the degree defined as the number of node links (i.e., the sum of outgoing and incoming links) to measure the inter-connectedness of an application. We also tested an alternative operationalization using the node outdegree to measure the interconnectedness, yielding similar results. The values for MEDIA in $\mathbf { t } _ { 1 }$ and $\mathbf { t } _ { 2 } ,$ and for BANKING were transformed using the inverse hyperbolic sine (ihs) transformation, defined by log $\left( X + { \sqrt { 1 + X ^ { 2 } } } \right)$ , for the analysis,<sup>7</sup> since the distribution of inter-connectedness in these cases was strongly skewed by a few nodes with very high degrees (as suggested by Burbidge et al. [10]).

Cluster governance, the dominant governance of surrounding applications (i.e., whether more centralized or more decentralized), was calculated in two steps. We first performed graph clustering to identify the existing clusters of connected nodes with high internal and low external cohesion [20]. We chose modularity clustering as a popular method that unifies different approaches [51], drawing particularly on the formulation by Blondel et al. [6]. Modularity clustering identifies clusters by maximizing the number of links within a set of nodes, compared to a random network where each node has the same degree of centrality, but the links are otherwise randomly attached. The number of calculated largestcomponent clusters was 10 for BANKING, 7 to 12 for MEDIA, and 8 for UTILITIES. Second, we calculated cluster governance as the median of the governance of all applications within each cluster. Residual applications in disconnected network components were manually assigned the median governance of their direct neighbors or, where no neighbor existed, the median governance of the entire group of residual applications.

Figure 3 provides an exemplary overview of the IS architecture network in one of the cases (MEDIA), indicating application governance, internal modularity, inter-connectedness, and cluster governance.

We included several control variables in the models to inform our understanding of application governance, aiming to rule out potential influences outside of theoretical reasoning. First, we controlled for the scope of use, a known contingency factor influencing application governance [76]. Scope of use, defined as the extent an application is utilized within an organization, was measured using numbers of business users for BANKING and numbers of business units for MEDIA and UTILITIES.<sup>8</sup>

Second, we controlled for application age for the cases of MEDIA and BANKING. Age was computed as the number of years from the application’s first rollout until the raw data were initially extracted (i.e., until 2015 and 2016 respectively). Application age may influence application governance due to organizational learning effects in using an application [76] and the tendency to maintain proven and stable systems [62].

![](/api/attachments/JA5UYB8B/fulltext/images/740ae4536cbccba2274a88d78fe6d8514b6bf26adfd92e513ec5c40efcc9d005.jpg)  
Figure 3. MEDIA IS Architecture Network (at t ) Notes: Schematic representation. Unconnected applications filtered. Each application unambiguously assigned to one cluster, despite visual overlaps.

Third, we controlled for the effects arising from the business function in which the application was used (e.g., general administration, human resources, and finance). We identified eight business functions for MEDIA, five for BANKING, and six for UTILITIES (see Online Appendix A, Tables A.1-A.3). This approach is also crucial because of the identified influence of differing business unit knowledge, investments, and incentives, contributing to misalignments [30]. The business function may bias application governance systematically because some business units may have more significant stakes in owning and managing applications than others due to their internal incentive structures [44].

In the consideration of longevity, we additionally controlled for the variables risk rating, external applications, documentation quality, and shadow IT policy, as applicable. The risk rating was captured as a mean compound of standard IT security assessments regarding the application’s confidentiality, integrity, and availability requirements. Applications with higher perceived security risks may be more likely decommissioned due to the company’s preference for ensuring compliance and minimizing risks [71]. IT staff at MEDIA and BANKING rated the applications on three-point scales (low, medium, high) where missing values were mean-imputed. External applications denoted those applications in the MEDIA case that were neither developed nor provided in-house (e.g., cloud applications). We controlled for this binary variable since companies may be more or less likely to decommission externally provided applications. In BANKING, the case that faced the highest regulatory transparency requirements, documentation quality was assessed as a mean compound of five items (e.g., level of technical documentation and user documentation), each measured on four possible levels. Regulated companies may have a preference to decommission applications that are poorly documented. In the case of BANKING, we also considered the influence of the firm’s shadow IT policy as an additional control, using a binary variable coded “1” for shadow IT applications and “0” for all other applications, to rule out possible interference of this policy on application longevity. Descriptive statistics for the primary variables are presented in Table 4. Due to space constraints, comprehensive descriptive statistics for MEDIA and control variables in other years can be found in Online Appendix A Tables A.1-3.

Table 4: Descriptive Statistics and Correlations

<table><tr><td></td><td>Mean</td><td>SD</td><td>Median</td><td>[Min, Max]</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td colspan="10"> $MEDIA (t_2)$ </td></tr><tr><td>1. Survival (binary)</td><td>0.87</td><td>0.34</td><td>1.00</td><td>[0, 1]</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. Application governance</td><td>2.41</td><td>0.86</td><td>2.00</td><td>[1, 4]</td><td>-0.17*a</td><td></td><td></td><td></td><td></td></tr><tr><td>3. Internal modularity</td><td>2.82</td><td>0.99</td><td>3.00</td><td>[1, 5]</td><td>0.23***</td><td>0.22**a</td><td></td><td></td><td></td></tr><tr><td> $4. Inter-connectedness^b$ </td><td>2.00</td><td>1.02</td><td>1.82</td><td>[0, 5.77]</td><td>0.06</td><td>-0.28***a</td><td>-0.34***</td><td></td><td></td></tr><tr><td>5. Cluster governance</td><td>2.55</td><td>0.69</td><td>3.00</td><td>[1, 4]</td><td>0.06</td><td>0.16*a</td><td>-0.16*</td><td>0.13</td><td></td></tr><tr><td>6. Fit</td><td>0.56</td><td>0.50</td><td>1.00</td><td>[0, 1]</td><td>0.17*</td><td>-0.15*a</td><td>-0.06</td><td>0.15*</td><td>0.10</td></tr><tr><td colspan="10">BANKING</td></tr><tr><td>1. Survival (binary)</td><td>0.45</td><td>0.50</td><td>0.00</td><td>[0, 1]</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. Application governance</td><td>2.57</td><td>1.18</td><td>2.00</td><td>[1, 4]</td><td>-0.39***a</td><td></td><td></td><td></td><td></td></tr><tr><td>3. Internal modularity</td><td>4.01</td><td>1.10</td><td>4.00</td><td>[1, 5]</td><td>-0.24***</td><td>0.57***a</td><td></td><td></td><td></td></tr><tr><td> $4. Inter-connectedness^b$ </td><td>0.98</td><td>1.23</td><td>0.88</td><td>[0, 6.32]</td><td>0.24***</td><td>-0.53***a</td><td>-0.60***</td><td></td><td></td></tr><tr><td>5. Cluster governance</td><td>2.37</td><td>0.84</td><td>3.00</td><td>[1, 4]</td><td>-0.42***</td><td>0.52***a</td><td>0.51***</td><td>-0.61***</td><td></td></tr><tr><td>6. Fit</td><td>0.53</td><td>0.50</td><td>1.00</td><td>[0, 1]</td><td>-0.01</td><td>0.16***a</td><td>0.15**</td><td>-0.06</td><td>0.06</td></tr><tr><td colspan="10">UTILITIES</td></tr><tr><td>1. Survival (binary)</td><td>0.18</td><td>0.39</td><td>0.00</td><td>[0, 1]</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. Application governance</td><td>3.22</td><td>1.23</td><td>3.00</td><td>[1, 5]</td><td>-0.04a</td><td></td><td></td><td></td><td></td></tr><tr><td>3. Internal modularity</td><td>5.60</td><td>0.49</td><td>6.00</td><td>[5, 6]</td><td>-0.44***</td><td>0.21**a</td><td></td><td></td><td></td></tr><tr><td>4. Inter-connectedness</td><td>2.20</td><td>3.59</td><td>1.00</td><td>[1, 24]</td><td>0.03</td><td>-0.10a</td><td>0.18*</td><td></td><td></td></tr><tr><td>5. Cluster governance</td><td>2.65</td><td>0.59</td><td>3.00</td><td>[2, 4]</td><td>-0.16*</td><td>0.13a</td><td>0.20**</td><td>0.07</td><td></td></tr><tr><td>6. Fit</td><td>0.32</td><td>0.47</td><td>0.00</td><td>[0, 1]</td><td>0.28***</td><td>-0.05a</td><td>-0.28***</td><td>0.06</td><td>-0.16*</td></tr></table>

\*p < 0.05, \*\*p < 0.01, \*\*\*p < 0.001  
Correlations without superscripts are Pearson correlation coeficients  
<sup>a</sup>Spearman correlation coeficient  
<sup>b</sup>ihs-transformed

## Analysis Method

We assessed our research hypotheses in two steps. In Step 1, we tested the effects of the three architectural contingencies (internal modularity, inter-connectedness, and cluster governance) on application governance (H1-H3). In Step 2, we calculated fit from Step 1 and a survival analysis to assess the effect of fit on the expected times until decommissioning (H4).

Due to the ordinal nature of the application governance variable, we employed ordinal logistic regression for Step 1 [2]. Ordinal regression allows us to interpret the results using the odds ratio (OR). The parameters indicate an increase (OR >1) or decrease (OR <1) in the application governance for a one-unit change in the explanatory variable. The application governance model was tested as follows:

$$
\begin{array}{l} \log [ P (\text { More   decentralized   application   governance } _ {t}) ] = \beta_ {j 0 t} + \beta_ {1 t} \text { Internal   modularity } _ {t} \\ \quad + \beta_ {2 t} \text { Inter - connectedness } _ {t} + \beta_ {3 t} \text { Cluster   governance } _ {t} + \sum_ {k} \beta_ {k t} \text { Controls } _ {k t}. \end{array}\tag{1}
$$

In Equation (1), $\beta _ { j 0 }$ describes the intercept for the specific ordinal outcome category j , $\beta _ { 1 }$ to $\beta _ { 3 }$ denote the parameters of the contingency factors, and $\beta _ { k }$ represents the control variable parameters. Indices t indicate for the three observation points for the case of MEDIA.

We employed Equation (1) to estimate the induced application governance. Using the coefficients from the ordinal logistic regression models allows the computation of the expected probability for each governance archetype for each application. We considered the mode of these probabilities (i.e., the governance archetype with the highest category probability) to be the induced governance for each application. We further calculated fit as the match between the observed and induced governance. Correspondingly, a deviating governance archetype was considered a misfit.

Two types of regressions were used for testing the fit hypothesis in Step 2 of the analysis. For MEDIA and BANKING, where longevity was operationalized as a duration in days, we used the Cox proportional hazards model [13] to estimate the effect of fit on the time until decommissioning. To control for systematic biases due to the archetype of application governance, we included application governance as an additional control variable operationalized as a binary variable (central IT owned or business IT owned vis-á-vis business owned or business managed governance). We included age, business function, and the remaining control variables as applicable. Therefore, the hazard of decommissioning at time t is given by

$$
h (\text { Decommissioning }, t) = h _ {0} (t) \exp \left(\beta_ {1} \operatorname{Fit} _ {t} + \sum_ {k} \beta_ {k} \text { Controls }\right)\tag{2}
$$

In Equation $( 2 ) , h _ { 0 } ( t )$ denotes the baseline hazard at time $t \mathrm { ~ , ~ } \beta _ { 1 }$ indicates the parameter of interest (i.e., the effect of fit on the hazard of decommissioning), and $\beta _ { k }$ represents the control variable parameters. As fit can change over time in the MEDIA case, we add a subscript t; for BANKING, there is no change over time.

When estimating the full model, certain business functions appeared to have a strong association with the outcome, such as cases where no application of the respective business function might be commissioned. Therefore, the likelihood of the model converges to a finite value while the parameter estimate diverges to infinity. To correct this issue, we use Firth’s penalized maximum likelihood approach [36], which decreases the bias in the regression parameters for the control variables.

In the case of UTILITIES, where longevity was operationalized as a binary attribute, logistic regression was chosen [32]. Using the same model variables as previously provides the logit of the probability of decommissioning:

$$
\log [ \mathrm{P} (\text { Decommissioning }) ] = \beta_ {0} + \beta_ {1} \text { Fit } + \sum_ {\mathrm{k}} \beta_ {\mathrm{k}} \text { Controls }.\tag{3}
$$

In Equation $( 3 ) , \beta _ { 0 }$ denotes the intercept, $\beta _ { 1 }$ represents the parameter of interest (i.e., the effect of fit on the log odds of decommissioning), and $\beta _ { k }$ indicates the control variable parameters. As before, we used Firth’s procedure of penalized maximum likelihood estimation for logistic regression [37] to account for influential control variables.

## Results

## Architectural Contingencies

Using the ordinal logistic regression analysis, we estimated the probability of an increase in application governance (i.e., decentralization) for independent variables for all three organizations. Furthermore, we included the respective control variables (scope of use, age, business functions, shadow IT policy) as available. The results of the analysis and ORs are presented in Table 5. Extended model tests are provided in Online Appendix A, Table A.4.

The results indicate a good-to-acceptable model fit for all three organizations (MEDIA: $[ \mathrm { t } _ { 0 } \mathrm { : }$ $\chi ^ { 2 } \left( 1 2 \right) = 9 2 . 5 6 \left( p < 0 . 0 0 1 \right) , \mathrm { t } _ { 1 } ; \chi ^ { 2 } \left( 1 2 \right) = 8 7 . 4 4 \left( p < 0 . 0 0 1 \right) , \mathrm { t } _ { 2 } ; \chi ^ { 2 } \left( 1 2 \right) = 8 4 . 7 1 \left( p < 0 . 0 0 1 \right) \mathrm { T } \left( 1 2 \right) .$ BANKING: $\chi ^ { 2 } ( 9 ) = 2 8 6 . 5 2 ( p < 0 . 0 0 1 )$ , and UTILITIES: $\chi ^ { 2 } ~ ( 9 ) = 3 1 . 3 6 , ( p < 0 . 0 0 1 ) )$ . Variance inflation factors did not raise concerns of multicollinearity (VIFs: MEDIA $\left( \mathfrak { t } _ { 0 } / \mathfrak { t } _ { 1 } / \mathfrak { t } _ { 2 } \right)$ : 1.1-2.3/ 1.2-2.3/1.1-2.3, BANKING: 1-2.3, UTILITIES: 1.1-3.8).

Table 5 displays significant negative effects of internal modularity on application governance for all three cases, with $B = 0 . 3 3 , \ p = 0 . 0 4 / B = 0 . 4 0 , \ p = 0 . 0 2 / B = 0 . 6 5 , \ p <$ 0.001 $\left( \mathfrak { t } _ { 0 } / \ \mathfrak { t } _ { 1 } / \ \mathfrak { t } _ { 2 } \right)$ for MEDIA, $B = 0 . 3 8 , \ p < 0 . 0 0 1$ for BANKING, and $B = 0 . 7 2 , \ p = 0 . 0 2$ for UTILITIES. This outcome indicates that higher internal modularity is associated with more decentralized application governance. More specifically, the Exp(B) parameters suggest that, when holding everything else constant, for each one-unit increase in application modularity, the odds of being more decentrally governed are multiplied by 1.40 (i.e., increased by 40%) for MEDIA in $\mathrm { t } _ { 0 }$ (1.49, 1.92, 1.46, and 2.06 and 49%, 92%, 46%, and 106% for MEDIA $\mathbf { t } _ { 1 } ,$ MEDIA $\mathrm { t } _ { 2 } ,$ BANKING, and UTILITIES, respectively). This result supports Hypothesis 1 (H1) for all three cases.

The negative significant coefficients for inter-connectedness for all three organizations (MEDIA: $B = - 0 . 0 6 , \beta = 0 . 0 1 / B = - 0 . 3 7 , \beta = 0 . 0 2 / B = - 0 . 4 1 , \beta < 0 . 0 1 \ [ \mathrm { t _ { 0 } / \ t _ { 1 } / \ t _ { 2 } } ] ;$ ; BANKING: $B = - 0 . 2 8 , \ p < 0 . 0 1$ ; and UTILITIES: $B = - 0 . 1 0 , \ p \ < \ 0 . 0 1 )$ indicate that a higher interconnectedness is associated with more centralized application governance. Therefore, for every one-unit increase in inter-connectedness $( \mathrm { i . e . , }$ for each additional link of an application), the odds of more decentral governance are decreased by 6% and 10% for MEDIA $\left( \mathrm { t } _ { 0 } \right)$ and UTILITIES, respectively. For MEDIA in $\mathrm { t _ { 1 } }$ and $\mathrm { t } _ { 2 } ,$ and BANKING, we ihs-transformed the interconnectedness variable to avoid outliers from overly influencing the B coefficient. The interpretation of the change in OR is performed on a k -fold multiplication of the factor.<sup>9</sup> Thus, doubling the inter-connectedness decreases the odds of being decentrally governed by 23% / 25% (MEDIA $\mathbf { t } _ { 1 }$ : $k ^ { B } = 2 ^ { - 0 . 3 7 } = 0 . 7 7 ~ / ~ \mathrm { t } _ { 2 } \colon k ^ { B } = 2 ^ { - 0 . 4 1 } = 0 . 7 5 )$ and 18% $( k ^ { B } = 2 ^ { - 0 . 3 4 } = 0 . 8 2 )$ ), supporting Hypothesis 2 (H2) for the three cases.

The positive significant coefficients for cluster governance in all three cases (MEDIA $( \mathrm { t } _ { 0 } / \mathrm { t } _ { 1 } / \mathrm { t } _ { 2 } ) \colon$ $B = 0 . 8 3 , p < 0 . 0 1 / B = 0 . 6 6 , p < 0 . 0 1 / B = 0 . 5 5 , p = 0 . 0 1 ; \mathrm { { B a N K I N G } : } B = 0 . 7 3 , p < 0 . 0 0 1$ ; and UTILITIES: $B = 0 . 6 1 , p = 0 . 0 2 )$ indicate that more decentralized cluster governance is associated with more decentralized application governance. Hence, when the cluster governance increases by one unit (i.e., moves one archetype toward more decentralization), the odds that the application becomes more decentralized increase by 130%/93%/73%, 107%, and 85% for MEDIA $\left( \mathfrak { t } _ { 0 } / \mathfrak { t } _ { 1 } / \mathfrak { t } _ { 2 } \right)$ , BANKING, and UTILITIES, respectively, supporting Hypothesis 3 (H3) for all three cases.

As for the controls, scope of use significantly diminishes the likelihood of decentralized application governance across all three cases. The other control variables (age, business functions) did not have a consistent effect on application governance.

## Survival Analysis

In the second model, we estimated the hazard for MEDIA and BANKING and the probability for UTILITIES of application decommissioning, depending on fit (see “Analysis Method” section for an explanation of how fit was measured). According to the proposed model, 54% / 55% /

<table><tr><td rowspan="2"></td><td colspan="6">MEDIA</td><td colspan="2">BANKING</td><td colspan="2">UTILITIES</td></tr><tr><td colspan="6">Application Governance (Ordinal logistic regressions)</td><td colspan="2">Application Governance (Ordinal logistic regression)</td><td colspan="2">Application Governance (Ordinal logistic regression)</td></tr><tr><td></td><td colspan="2"> $t_0$  (2015)</td><td colspan="2"> $t_1$  (2016)</td><td colspan="2"> $t_2$  (2018)</td><td rowspan="2"> $B (SE)^2$ </td><td rowspan="2"> $Exp(B)^2$ </td><td rowspan="2"> $B (SE)^3$ </td><td rowspan="2"> $Exp(B)^3$ </td></tr><tr><td></td><td> $B (SE)^1$ </td><td> $Exp(B)^1$ </td><td> $B (SE)^1$ </td><td> $Exp(B)^1$ </td><td> $B (SE)^1$ </td><td> $Exp(B)^1$ </td></tr><tr><td>H1: Internal modularity</td><td>0.33* (0.16)</td><td>1.40</td><td>0.40* (0.17)</td><td>1.49</td><td>0.65*** (0.18)</td><td>1.92</td><td>0.38*** (0.11)</td><td>1.46</td><td>0.72* (0.32)</td><td>2.06</td></tr><tr><td>H2: Inter-connectedness</td><td>-0.06* (0.03)</td><td>0.94</td><td>-0.37* (0.15) $^4$ </td><td>0.69 $^5$ </td><td>-0.41** (0.15) $^4$ </td><td>0.67 $^6$ </td><td>-0.28** (0.11) $^4$ </td><td>0.75 $^7$ </td><td>-0.10** (0.04)</td><td>0.90</td></tr><tr><td>H3: Cluster governance</td><td>0.83** (0.28)</td><td>2.30</td><td>0.66** (0.23)</td><td>1.93</td><td>0.55* (0.22)</td><td>1.73</td><td>0.73*** (0.14)</td><td>2.07</td><td>0.61* (0.25)</td><td>1.85</td></tr><tr><td>Scope of use</td><td>-0.05*** (0.01)</td><td>0.95</td><td>-0.06*** (0.01)</td><td>0.94</td><td>-0.05*** (0.01)</td><td>0.95</td><td>-0.03* (0.02)</td><td>0.97</td><td>-0.14* (0.06)</td><td>0.87</td></tr><tr><td>Age</td><td>0.03 (0.02)</td><td>1.03</td><td>0.02 (0.02)</td><td>1.02</td><td>0.04* (0.02)</td><td>1.04</td><td>-0.04 (0.02)</td><td>0.96</td><td></td><td></td></tr><tr><td>BF: Operations</td><td>0.27 (0.54)</td><td>1.31</td><td>0.58 (0.52)</td><td>1.78</td><td>0.58 (0.54)</td><td>1.78</td><td>1.47*** (0.27)</td><td>4.36</td><td>-0.24 (0.53)</td><td>0.78</td></tr><tr><td>BF: General administration</td><td>-0.67 (0.66)</td><td>0.51</td><td>-0.44 (0.72)</td><td>0.64</td><td>-0.77 (0.71)</td><td>0.47</td><td>2.07*** (0.29)</td><td>7.89</td><td></td><td></td></tr><tr><td>BF: Distribution</td><td>1.01 (0.53)</td><td>2.74</td><td>1.08* (0.54)</td><td>2.94</td><td>0.77 (0.55)</td><td>2.15</td><td>1.94*** (0.35)</td><td>6.95</td><td></td><td></td></tr><tr><td>BF: Human resources</td><td>1.24* (0.62)</td><td>3.47</td><td>1.38* (0.63)</td><td>3.99</td><td>1.48* (0.72)</td><td>4.40</td><td></td><td></td><td>0.05 (0.69)</td><td>1.05</td></tr><tr><td>BF: Finance</td><td>0.23 (0.49)</td><td>1.26</td><td>0.18 (0.49)</td><td>1.20</td><td>0.05 (0.50)</td><td>1.05</td><td></td><td></td><td>-0.63 (0.57)</td><td>0.53</td></tr><tr><td>BF: Marketing &amp; sales</td><td>0.29 (0.48)</td><td>1.34</td><td>0.36 (0.47)</td><td>1.43</td><td>0.01 (0.48)</td><td>1.01</td><td></td><td></td><td>-0.01 (0.53)</td><td>0.99</td></tr><tr><td>BF: Procurement</td><td>-0.07 (0.64)</td><td>0.93</td><td>-0.25 (0.65)</td><td>0.78</td><td>-0.39 (0.65)</td><td>0.68</td><td></td><td></td><td></td><td></td></tr><tr><td>BF: Infrastructure</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-2.36* (1.10)</td><td>0.09</td><td></td><td></td></tr><tr><td>BF: Customer services</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.38 (0.66)</td><td>1.46</td></tr><tr><td>Num. obs.</td><td colspan="2">225</td><td colspan="2">219</td><td colspan="2">209</td><td colspan="2">498</td><td colspan="2">193</td></tr><tr><td>Nagelkerke  $R^2$ </td><td colspan="2">0.37</td><td colspan="2">0.36</td><td colspan="2">0.36</td><td colspan="2">0.47</td><td colspan="2">0.16</td></tr><tr><td>McFadden  $R^2$ </td><td colspan="2">0.17</td><td colspan="2">0.16</td><td colspan="2">0.16</td><td colspan="2">0.21</td><td colspan="2">0.05</td></tr><tr><td>Log likelihood</td><td colspan="2">-233.30</td><td colspan="2">-229.15</td><td colspan="2">-218.01</td><td colspan="2">-534.43</td><td colspan="2">-278.54</td></tr><tr><td>Model  $\chi^2$ </td><td colspan="2">92.56, df=12, p&lt;0.001</td><td colspan="2">87.44, df=12, p&lt;0.001</td><td colspan="2">84.71, df=12, p&lt;0.001</td><td colspan="2">286.52, df=9, p&lt;0.001</td><td colspan="2">31.36, df=9, p&lt;0.001</td></tr></table>

Table 5: Results for Efects on Application Governance (Contingencies)

<sub>s-transfor</sub>m <sub>ur</sub> <sub>p</sub>l<sub>ann</sub>i<sub>ng</sub> <sub>a</sub><sup>s</sup> <sup>reference</sup> <sup>ca</sup> <sub>upport</sub> <sub>as</sub> <sub>re</sub>f<sup>erence</sup> <sup>cate</sup> <sub>oduct</sub>i<sub>on</sub> <sub>as</sub> <sub>r</sub>e<sup>ference</sup> <sup>cat</sup> .<sub>05,</sub> <sub>\*\*p</sub> <sub><</sub> <sub>0</sub>.<sub>01</sub><sup>,</sup> <sup>\*\*\*p</sup> <sup><</sup> <sub>¼</sub> <sub>2 </sub> 0:<sup>28</sup> <sup>¼</sup> <sup>0</sup>: <sub>¼2 </sub> 0:<sup>41</sup> <sup>¼0</sup>: <sub>¼</sub> <sub>2 </sub> 0:<sup>37</sup> <sup>¼</sup> <sup>0</sup>:

Table 6: Regression Results for Efects on Longevity

<table><tr><td rowspan="3"></td><td colspan="2">MEDIA</td><td colspan="2">BANKING</td><td colspan="2">UTILITIES</td></tr><tr><td colspan="2">Decommissioning (Penalized Cox models)</td><td colspan="2">Decommissioning (Penalized Cox models)</td><td colspan="2">Decommissioning (Penalized binary log.)</td></tr><tr><td> $B (SE)^1$ </td><td> $Exp(B)^1$ </td><td> $B (SE)^2$ </td><td> $Exp(B)^2$ </td><td> $B (SE)^3$ </td><td> $Exp(B)^3$ </td></tr><tr><td>H4: Fit</td><td>-0.86* (0.39)</td><td>0.42</td><td>-0.77*** (0.16)</td><td>0.46</td><td>-1.01* (0.46)</td><td>0.36</td></tr><tr><td>Application governance (binary)</td><td>1.09** (0.40)</td><td>2.96</td><td>0.47 (0.26)</td><td>1.60</td><td>0.51 (0.62)</td><td>1.66</td></tr><tr><td>BF: Operations</td><td>-0.73 (0.74)</td><td>0.48</td><td>0.05 (0.21)</td><td>1.05</td><td>0.47 (0.81)</td><td>1.59</td></tr><tr><td>BF: General administration</td><td>0.31 (0.69)</td><td>1.36</td><td>0.16 (0.22)</td><td>1.17</td><td></td><td></td></tr><tr><td>BF: Distribution</td><td>0.70 (0.64)</td><td>2.02</td><td>-0.31 (0.33)</td><td>0.73</td><td></td><td></td></tr><tr><td>BF: Human resources</td><td>1.14 (0.67)</td><td>3.12</td><td></td><td></td><td>0.38 (1.11)</td><td>1.47</td></tr><tr><td>BF: Finance</td><td>-0.21 (0.79)</td><td>0.81</td><td></td><td></td><td>0.64 (0.96)</td><td>1.90</td></tr><tr><td>BF: Marketing &amp; sales</td><td>-0.21 (0.63)</td><td>0.81</td><td></td><td></td><td>-1.98** (0.77)</td><td>0.14</td></tr><tr><td>BF: Procurement</td><td>-2.39* (1.57)</td><td>0.09</td><td></td><td></td><td></td><td></td></tr><tr><td>BF: Infrastructure</td><td></td><td></td><td>-1.08* (0.56)</td><td>0.34</td><td></td><td></td></tr><tr><td>BF: Customer services</td><td></td><td></td><td></td><td></td><td>1.80 (1.58)</td><td>6.04</td></tr><tr><td>Age</td><td>0.07*** (0.02)</td><td>1.08</td><td>0.12*** (0.01)</td><td>1.13</td><td></td><td></td></tr><tr><td>Risk rating</td><td>-0.08 (0.41)</td><td>0.92</td><td>-0.49*** (0.07)</td><td>0.61</td><td></td><td></td></tr><tr><td>External application</td><td>-0.93 (0.62)</td><td>0.39</td><td></td><td></td><td></td><td></td></tr><tr><td>Shadow IT policy</td><td></td><td></td><td>0.12 (0.34)</td><td>1.13</td><td></td><td></td></tr><tr><td>Documentation quality</td><td></td><td></td><td>0.70*** (0.09)</td><td>2.01</td><td></td><td></td></tr><tr><td>Num. obs.</td><td colspan="2">271</td><td colspan="2">498</td><td colspan="2">193</td></tr><tr><td>Likelihood-ratio test</td><td colspan="2">49.91, df=12, p&lt;0.01</td><td colspan="2">203.56, df=10, p&lt;0.01</td><td colspan="2">52.51, df=7, p&lt;0.01</td></tr><tr><td>Wald test (χ2)</td><td colspan="2">45.84, df=12, p&lt;0.01</td><td colspan="2">189.42, df=10, p&lt;0.01</td><td colspan="2">65.49, df=7, p&lt;0.01</td></tr></table>

\*p < 0.05, \*\*p < 0.01, \*\*\*p < 0.001  
<sup>1</sup>BF: Production as reference category.  
<sup>2</sup>BF: Support as reference category.  
<sup>3</sup>BF: Tour planning as reference category.

56%, 53%, and 32% of the applications exhibited a fit for MEDIA $\left( \mathfrak { t } _ { 0 } / \ \mathfrak { t } _ { 1 } / \ \mathfrak { t } _ { 2 } \right)$ , BANKING, and UTILITIES, respectively (Online Appendix A, Tables A.1-A.3), meaning their observed governance matched the induced governance and was aligned with the archetype commonly accepted for architecturally similar applications in these organizations. Comparisons of the distributions of observed and induced governance are shown in Tables A.6-A.8 of Online Appendix A.

Table 6 presents the results on H4. Extended model tests are provided in Online Appendix A, Table A.5. Multicollinearity was not a major issue with VIFs below common thresholds (MEDIA: 1.1-2.5, BANKING: 1.2-3.7, UTILITIES: 1.1-3.7). Overall, each of the three models indicates good model fit (MEDIA: $\chi ^ { 2 } \left( 1 2 \right) = 4 5 . 8 4 \left( p < 0 . 0 0 1 \right)$ , BANKING: $\chi ^ { 2 } \left( 1 0 \right) = 1 8 9 . 4 2 \left( p < 0 . 0 0 1 \right) :$ and UTILITIES: $\chi ^ { 2 } ~ ( 7 ) = 6 5 . 4 9 , ( p < 0 . 0 0 1 ) )$ . All three models indicate that governance fit negatively influences application decommissioning (MEDIA: B = –0.86, p = 0.02; BANKING: B = –0.77, p < 0.001; and UTILITIES: B = –1.01, p = 0.03). These findings support the governance-architecture fit hypothesis (H4) for all three cases.

For MEDIA and BANKING, the Exp(B) parameters indicate that when application governance fits the induced archetype, the hazard is multiplied by 0.42 (95% confidence interval [CI] [0.20, 0.91]) and 0.46 (CI [0.34, 0.62]), indicating a 58% and 54% lower hazard of decommissioning in the presence of fit, respectively. Figure 4 provides an estimated distribution of survival times for MEDIA and BANKING stratified by fit.<sup>10</sup> The figure reveals that lifetimes were lower for non-fitting applications. For UTILITIES, the Exp(B) parameter of 0.36 (CI [0.14, 0.93]) indicates that the odds of an application’s decommissioning are 64% lower when the application’s governance fits the induced archetype. In summary, we conclude that the governance-architecture fit is highly conducive for application longevity.

![](/api/attachments/JA5UYB8B/fulltext/images/74e3cbdd8c52d3df196f85557408094d1ccf5d7440e0aedabb81139f0c262cff.jpg)

![](/api/attachments/JA5UYB8B/fulltext/images/24f4c2e3497150882ac4db18ee7d2edc9420f751b23bf57e06c349d45506d7a4.jpg)  
FitFit  No Fit  
Figure 4. Estimated Distribution of Survival Times for (A) MEDIA and (B) BANKING (excluding shadow IT)<sup>10</sup>

Regarding controls, for MEDIA, a significant (direct) effect of application governance on decommissioning is noteworthy $( B = 1 . 0 9 , p < 0 . 0 1 )$ . This outcome can be explained by a centralization policy that the company pursued. While not significant, the coefficient for BANKING points in the same direction. Thus, decentralized governance was associated with a higher likelihood of decommissioning. Furthermore, in the cases of MEDIA and BANKING, older applications were more likely to be decommissioned. Furthermore, the risk rating of an application had a negative effect on decommissioning in BANKING, but not in MEDIA. Documentation quality had a positive effect on decommissioning at BANKING. Finally, the business function did not have a consistent effect on decommissioning.

## Limitations

The following limitations merit consideration. First, due to the heterogeneous company sources of the micro-level datasets, we acknowledge the different operationalizations for some of the variables and the different sets of control variables for these cases, which may limit the comparability across the three cases. Second, although replication across cases supports the generalizability of the findings, we could not control for systematic influences that might bias governance at the organizational level, such as competitive strategy, industry stability, and firm size [8]. Third, with our selective emphasis on application governance’s role in longevity, we recognize that factors beyond our theoretical scope could explain discontinuance [e.g., 22, 52]. Additionally, examining non-architectural governance contingencies, like those based on knowledge [e.g., 66], which were outside our focused purview, may prove insightful. Fourth, although we used temporally ordered data to operationalize longevity, and model factors in the case of MEDIA, the methods employed ultimately ascertain only associations, not the causality implied in the theoretical arguments. Finally, due to the lack of established instrumental variables for fit, the analysis could not rule out possible endogeneity, such as reverse causality or selection bias. Concerning reverse causality, a misfit might be intentionally created by an organization planning to decommission an application.<sup>11</sup> Regarding selection bias, while we analyzed all known applications in each case, we did not consider potentially unreported applications, possibly part of the company’s shadow IT. These applications might have poor fit, leading to their intentional concealment to avoid decommissioning, or, if discovered, they may be swiftly removed due to their unauthorized status [e.g., 26].

## Discussion

This study explored the relationship between the governance of architecturally embedded applications and their longevity in an organizational context. We conceptualized the applications’ internal modularity, its inter-connectedness in the architectural network, and surrounding cluster governance as fundamental architectural contingencies for application governance. We then examined how a fit of application governance with these properties is associated with the application’s longevity, indicating long-term organizational use. Comprehensive temporally ordered proprietary data collected from three organizations over five-year periods provide consistent and significant support that a governancearchitecture fit diminishes the likelihood of application decommissioning.

## Theoretical Implications

Five implications for governance, architecture, and discontinuance literatures in IS emerge.

## Implication 1. Embracing Micro and Meso Levels in IS Governance

First, this research establishes the critical importance of embracing a micro-level approach in IS governance, especially when targeting individual application artifacts, and then seamlessly extends this paradigm through the integration of a meso-level perspective. Traditional governance approaches, which often generalize across different applications within an organization, prove to be insufficient [e.g., 55, 72]. Early governance research offered limited insights into the ‘hybrid archetype’—a governance model involving both business and IT stakeholders [8]. More recent works have been calling for a nuanced understanding of IS governance at finer levels, such as projects [64, 79] and applications [76].

By adopting a micro-level perspective and focusing on the architectural context of IS artifacts, our study advances the conversation from descriptive to prescriptive governance insights. While Winkler and Brown [76] laid groundwork by exploring the precursors of application governance, they treated applications in isolation and did not establish a clear metric for governance efficacy. Our research enhances this view through a modular systems approach, considering applications as part of an interconnected IS architecture.

While we identify longevity as an important outcome of effective application governance, it is essential to recognize that longevity does not automatically equate to sustained organizational value. In fact, the enduring presence of an application within an organization can, over time, result in diminishing or even negative returns. This nuanced relationship between application longevity and organizational value remains an intriguing area for future research.

Our empirical results confirm the significant role of architectural properties for application governance (H1-H3) and support the validity of the contingency-fit hypothesis (H4). These findings resonate with the early IS governance literature that has discussed the influence of multiple contingencies on governance choices [55]. Importantly, our work extends the list of known contingent factors relating to company structure and capabilities by a set of architectural contingencies that relate to the application artifact itself. More broadly, the support for the fit hypothesis stands in line with prior governance research highlighting how appropriate governance serves as a complementary asset for long-term IT value creation [5, 30].

Connecting the macro and micro levels, our research introduces the novel concept of cluster governance, which considers the governance patterns within groups of interconnected applications on the meso level. Our data shows that cluster governance significantly influences, but is not always identical with, governance at the individual application level. A one category decentralization in cluster governance makes a shift towards more decentralized application governance 73% to 130% more likely. This not only underscores the interdependent nature of IS governance across levels, but also offers a new avenue for research, particularly concerning the role of network influence in governance choices.

By integrating micro and meso levels with architectural considerations, our research contributes to a layered, interdependent understanding of IS governance. This nuanced model offers academics and practitioners an evidence-based strategy for reassessing and restructuring governance models while navigating evolving digital infrastructures.

## Implication 2. Coevolutionary View of IS Governance and Architecture

The second implication is that this study advances the coevolutionary view of IS architecture and governance. IS researchers have increasingly seen architecture and governance as intrinsically related, emphasizing how varying properties of an organization’s technology architecture (like standardization versus differentiation, integration versus modularization, and stability versus variability) necessitate different governance approaches [35, 67, 68]. Our modular systems perspective underscores that architecture and governance coevolve, with architectural properties at both micro and meso levels being vital for the governance of applications.

Regarding internal architectural properties at the micro level, we utilized the modular systems concept of decomposition [58] to theorize that a modular internal design corresponds with decentralized application governance. Our findings supported this contingency across three cases, indicating that a one-step rise in internal modularity increases the likelihood of more decentralized governance by 40% to 106%.

Tiwana and Konsynski [67] investigated the relationship between architecture modularity and governance at the organizational level. We extend this by addressing modularity and governance at the application’s micro-level. Our results align with those of Tiwana and Konsynski [67] by underscoring the fit between high modularity and decentralized governance for yielding generally desirable outcomes (longevity and agility, respectively). They found that low modularity paired with centralized governance translates to reduced agility [67]. Our study adds the insight that low modularity on the application level paired with centralized application governance enhances longevity. Taken together, this suggests that low agility (i.e., rigidity) is not necessarily at odds with longevity.

However, centralized legacy systems with monolithic architectures, although durable, may accrue technical debt that hinders their discontinuance and locks the organizations into debt-constrained states [54]. Such lock-in situations can potentially hamper organizational innovation on the level of the organization-wide IS architecture by making it challenging to adapt and evolve in response to changing needs and environments.

## Implication 3. Distinguishing Internal and External Micro-Architecture

Our inclusion of inter-connectedness as an additional architectural contingency, next to modularity, is in line with recent research that has emphasized the distinction between internal and external architectural properties of applications [65, 69]. Tiwana [65] showed for apps in a platform ecosystem that the combination of internal architecture monolithicity with external architecture modularity allows apps to better leverage the capabilities of the platform they are connected with. Our findings parallel this notion by showing that higher inter-connectedness (i.e., external architectural modularity) and lower internal modularity (i.e., monolithicity) also go hand-in-hand for greater centralized governance of applications in an organizational IS architecture.

Tiwana and Safadi [69] offer insights into how changes in internal modularity of opensource applications can lead to the decay of their codebase (atrophy) over time, a phenomenon akin to applications losing their cohesive structure as they age. Their model employs increases in external module invocations as an instrument capturing changes in inter-connectedness to establish that increases in the inter-connectedness correlate with losses in internal modularity.

Our study extends the discourse on the role of internal and external architectural properties of applications towards the application’s governance and organizational use. We demonstrate that internal modularity and external inter-connectedness are related with governance when the application is embedded in organization-wide IS architectures. Our empirical evidence underscores the intricate relationships between architectural properties and governance and its subsequent effect on application longevity. Significantly, while decay or ‘code rot’ are viewed as detrimental to longevity [69], our findings advocate for an governance-architecture fit as a longevity booster. That is, while Tiwana and Safadi’s [69] findings hint that decreasing internal modularity and increasing inter-connectedness can lead to faster decay of the codebase, our study suggests that monolithic and interconnected applications can remain in long-term organizational use under centralized governance models.

Logically, our findings do not imply that longer duration of organizational use is necessarily associated with good health of the codebase. Instead, the combined findings may suggest delayed decommissioning decisions of atrophic applications that might not benefit the organization. This, again, resonates with Rinta-Kahila et al.’s [54] notion of organizations being locked into debt-constrained monolithic and deeply embedded legacy systems.

## Implication 4. Integrating Architectural Thinking in IS Governance Decisions

Our findings also contribute to the discourse on architectural thinking in IS governance [e. g., 7, 33], specifically emphasizing the role of inter-connectedness. Each additional connection in the architectural network is associated with a 6% to 10% decrease in the likelihood of adopting decentralized governance. This supports the strategic notion of architectural ‘control points’, as identified by Dreyfus and Iyer [17].

Although Dreyfus and Iyer [17] called attention to the role of central applications in IS architecture evolution, and Lagerström et al. [43] examined the costs associated with architectural changes, neither explicitly considered the implications for governance. Our research fills this gap by demonstrating that the position of an application within the IS architecture—whether at the core or the periphery—matters not just for the costs of architectural changes but also for its appropriate governance.

The validation of the governance-architecture fit hypothesis in our study has significant implications for long-term strategic decision-making. Organizations must recognize the need for different governance models for applications based on their architectural centrality. Failing to appropriately govern strategically critical, highly interconnected applications risks compromising their long-term effectiveness. On the other hand, overly centralized governance applied to less connected, peripheral applications may result in inefficiencies. This brings nuanced insights into architectural thinking, asserting that the governance model must be tailored to an application’s specific architectural context for optimal longterm value.

## Implication 5. Linking IS Governance and (Dis-)continuance

Finally, this work establishes a new nomological linkage from governance to discontinuance. While planning, adoption, and assimilation of IS have been traditional focuses of the IS literature, authors have noted a dearth of theory regarding conditions for survival vis-à- vis the discontinuance of IS [22, 54, 60], whereby survival is essential in the analysis of IS [1].

In the evolving discourse on IS discontinuance, our research offers a nuanced contribution by empirically examining actual discontinuance events within three distinct organizations. While early research in this domain primarily centered on individual or organizational intentions to discontinue IS use [e.g., 22, 23, 52], recent studies began adopting a process-oriented lens [e.g., 53, 54]. These works delve into the complex journey from initial discontinuance intentions to ultimate implementation of the decision, shedding light on emergent complexities such as new dependencies and multi-level dynamics [e.g., 54].

Our study advances this line of inquiry by pivoting from intentions and case evidence to a data-driven examination of realized discontinuance. Drawing on real-world data from three organizations, we provided an extensive analysis of the actual organizational decisions to discontinue IS. Building on the validity of the three architectural contingencies, we posited that aligning application governance with architectural properties reduces the likelihood of decommissioning, thereby enhancing longevity. This alignment, based on organizational decision rights, minimizes misfit costs [15].

However, it is crucial to note that longevity does not necessarily imply sustained or increasing value creation. Indeed, the marginal value generated by a business application can diminish or even become negative over time despite its continued operation. In our empirical findings, fit reduced the likelihood of application decommissioning by 58% and 54% when estimating survival durations for the MEDIA and BANKING cases, respectively, using Cox regression. It also decreased the likelihood of decommissioning by 64% when estimating the binary five-year survival outcome for UTILITIES using logistic regression. Therefore, while fit and governance may extend an application’s lifespan, this longevity should not be conflated with unchanging or incremental value creation over time.

The finding of a governance-architecture fit adds a new antecedent to IS discontinuance research by highlighting the often-overlooked role of governance. Previous empirical studies [e.g., 22, 52, 62] focused on a range of variables, including both internal and external factors influencing decommissioning, such as application performance, suitability, and supportability, without considering the interplay between governance and architectural alignment. Our research suggests that effective governance mechanisms guide investment portfolio decisions toward applications that are congruent with the architectural governance within the organization. This congruence, in turn, influences not just the longevity of these applications, but also their evolving value over time.

## Directions for Future Research

Our study opens up four promising directions for future research. First, given the implication that governance misfits often lead to delayed decommissioning, future qualitative studies could delve into the coping mechanisms that organizations employ temporarily. Second, to better comprehend the resilience of survivor applications, longitudinal research could investigate the diminishing marginal value of legacy applications over time that persist despite misfits, drawing on findings from Rinta-Kahila et al. [54] and Fürstenau et al. [24]. Third, in the spirit of Tiwana and Konsynski [67] and Tiwana and Safadi [69], our results underscore the opportunity for further research that explores the complex interplay between architecture and governance across levels, particularly concerning the interdependencies with the underexplored meso level. Finally, extending this line of research to the ecosystem level would offer insights into how governance and architectural choices interact across the digital infrastructures that connect multiple user organizations.

## Conclusion

This study addressed a critical gap in our understanding of how governance influences the longevity of architecturally embedded applications that form the backbone of a firm’s digital infrastructure. Drawing on a modular systems view and employing a contingency-fit logic, we provided consistent and compelling support for the hypothesis that a governance-architecture fit is conducive to longevity. Three architectural contingencies are significant in this context: application modularity, interconnectedness, and surrounding cluster governance. Our findings prompt IS researchers to rethink organizational IS governance as a multi-level concept that needs to dynamically adapt to the ever-evolving IS architecture to sustain long-term value creation. Managers in organizations should recognize that the governance of business applications is not a one-size-fits-all approach but depends on the specific architectural properties of applications and application clusters. Our research reveals that a fit between governance choices and architectural contingencies significantly impacts typical application lifespans, providing a solid foundation for evidence-based management strategies that can sustain application use and value creation in organizations.

## Notes

1. Anonymized due to confidentiality agreements with these organizations.

2. UTILITIES did not collect intermediate datasets and discontinued/pivoted its enterprise architecture efforts after 2015.

3. See Online Appendix B for a detailed coding guide.

4. To account for survivor bias [18] (the problem of focusing on applications that have endured, while neglecting those that have not), we included age as a separate control variable in the regressions. This information was extracted from a separate, reported field in the datasets called the productive date.

5. Additional exploratory discussions with five application owners, one IT strategist, and one enterprise architect confirmed the relevance of the notion of governancearchitecture fits when confronted with the findings of the analysis. Across all companies, we established close rapport with the architecture group to refine, validate, and challenge the findings.

6. A prominent example of modified legacy software is the Ada-coded US Air Traffic Control system, around which the Federal Aviation Administration (FAA) has built special wrappers and APIs to enable it to interface with more modern external applications [69].

7. Because there are 0 observations, the standard log-transformation is not available. To test robustness, we also experimented with $l n ( X + k ) , \bar { 0 } . 1 \leq k \leq 1 0$ , to inter-connectedness and the results are robust.

8. For MEDIA and UTILITIES, the number of using business units served as a proxy for the scope of use because no other user data were available. For MEDIA, we imputed missing values (n = 5) by drawing on related information, such as the business processes in which the application was used, and validated these imputed values with a key informant. For BANKING, we imputed a low number of missing values (n = 18) with the mean number of users and validated this procedure with a company informant. For UTILITIES, we counted the number of distinct units in a comma-separated field called ‘using business units’ in the raw data. There were no missing values.

9. Note that this is a simplification that holds true for larger values of inter-connectedness. See Online Appendix C for details on the interpretation of coefficients in the log-arcsinh model.

10. BANKING had followed a consolidation policy for its multiple shadow IT applications within the observation period. We had controlled for the bias of this policy on longevity through a separate binary control and only show non-shadow IT applications in Figure 4.

11. An illustrative analysis of the decommissioned applications at MEDIA did not reveal a pattern of reverse causality. Instead, it suggested that application governance was stable, whereas diminishing support in the organization was sometimes expressed in the reduced number of business units using the application. In some cases, the additional analysis also revealed that investments were made in an application to prepare for decommissioning.

## Disclosure statement

No potential conflict of interest was reported by the author(s).

## Notes on contributors

Karl Akbari is an Assistant Professor at the Department of Business Administration at National Taiwan University of Science and Technology. He received his Ph.D. from the University of Vienna. Dr. Akbari’s research interests are pricing issues using econometric modeling and experimental methods. His research has been published in Marketing Science, Review of Managerial Science, and Schmalenbach Journal of Business Research, among other outlets.

Daniel Fürstenau is an Associate Professor in Information Systems at the IT University of Copenhagen. He received his Ph.D. from Freie Universität Berlin. Dr. Fürstenau is an affiliated member of the Einstein Center Digital Future and a digital health researcher at Charité. His research interests include IT management, digital health, and AI-driven innovation. His 2019 Information Systems Research paper received the AoM Organizational Communication and Information Systems best paper runner-up award.

Till J. Winkler is Chair Professor of Information Management at University of Hagen, Germany, and affiliated Associate Professor at the Copenhagen Business School, Denmark. His research on the governance of information technology, service management, and digital health has appeared in Journal of Management Information Systems, Journal of the Association for Information Systems, Journal of Strategic Information Systems, MIS Quarterly Executive, and others. Dr. Winkler is recipient of the Early Career Award of the Association for Information Systems.

## ORCID

Karl Akbari http://orcid.org/0000-0003-0894-2900 Daniel Fürstenau http://orcid.org/0000-0001-8490-7707 Till J. Winkler http://orcid.org/0000-0002-3944-7390

## References

1. Agarwal, R. and Tiwana, A. Evolvable systems: Through the looking glass of IS. Information Systems Research, 26, 3 (2015), 473–479.

2. Agresti, A. Categorical Data Analysis. Wiley-Blackwell, Hoboken, New Jersey, 2013.

3. Aral, S., Muchnik, L., and Sundararajan, A. Distinguishing influence-based contagion from homophily-driven diffusion in dynamic networks. Proceedings of the National Academy of Sciences, 106, 51 (2009), 21544–21549.

4. Aral, S., Muchnik, L., and Sundararajan, A. Engineering social contagions: Optimal network seeding in the presence of homophily. Network Science, 1, 2 (2013), 125–153.

5. Aral, S. and Weill, P. IT assets, organizational capabilities, and firm performance: How resource allocations and organizational differences explain performance variation. Organization Science, 18, 5 (2007), 763–780.

6. Blondel, V.D., Guillaume, J.L., Lambiotte, R., and Lefebvre, E. Fast unfolding of communities in large networks. Journal of Statistical Mechanics: Theory and Experiment, 10 (2008), P10008.

7. Boh, W.F. and Yellin, D. Using enterprise architecture standards in managing information technology. Journal of Management Information Systems, 23, 3 (2006), 163–207.

8. Brown, C. V. Examining the emergence of hybrid IS governance solutions: Evidence from a single case site. Information Systems Research, 8, 1 (1997), 69–94.

9. Brown, C. V. and Magill, S.L. Alignment of the IS functions with the enterprise: Toward a model of antecedents. MIS Quarterly, 18, 4 (1994), 371–395.

10. Burbidge, J.B., Magee, L., and Robb, A.L. Alternative transformations to handle extreme values of the dependent variable. Journal of the American Statistical Association, 83, 401 (1988), 123–127.

11. Bygstad, B. Generative innovation: A comparison of lightweight and heavyweight IT. Journal of Information Technology, 32, 2 (2017), 180–193.

12. Chua, C.E.H. and Storey, V.C. Bottom-up enterprise information systems: Rethinking the roles of central IT departments. Communications of the ACM, 60, 1 (2017), 66–72.

13. Cox, D.R. Regression models and life‐tables. Journal of the Royal Statistical Society: Series B (Methodological), 34, 2 (1972), 187–202.

14. Criscuolo, P., Salter, A., and ter Wal, A.L.J. Going underground: Bootlegging and individual innovative performance. Organization Science, 25, 5 (2014), 1287–1305.

15. David, P.A. Path Dependence: A Foundational Concept for Historical Social Science. In P. Zumbansen and G.-P. Calliess, eds., Law, Economics and Evolutionary Theory. Edward Elgar Publishing, 2011.

16. Dong, J.Q., Karhade, P.P., Rai, A., and Xu, S.X. How firms make information technology investment decisions: Toward a behavioral agency theory. Journal of Management Information Systems, 38, 1 (2021), 29–58.

17. Dreyfus, D. and Iyer, B. Managing architectural emergence: A conceptual model and simulation. Decision Support Systems, 46, 1 (2008), 115–127.

18. Elton, E.J., Gruber, M.J., and Blake, C.R. Survivorship bias and mutual fund performance. Review of Financial Studies, 9, 4 (1996), 1097–1120.

19. Fama, E.F. and Jensen, M.C. Separation of ownership and control. The Journal of Law & Economics, 26, 2 (1983), 301–325.

20. Fortunato, S. Community detection in graphs. Physics Reports, 486, 3–5 (2010), 75–174.

21. Furneaux, B. and Wade, M. The end of the information system life: A model of IS discontinuance. Data Base for Advances in Information Systems, 41, 2 (2010), 45–69.

22. Furneaux, B. and Wade, M. An exploration of organizational level information systems discontinuance intentions. MIS Quarterly, 35, 3 (2011), 573–598.

23. Furneaux, B. and Wade, M. Impediments to information systems replacement: A calculus of discontinuance. Journal of Management Information Systems, 34, 3 (2017), 902–932.

24. Fürstenau, D., Baiyere, A., and Kliewer, N. A dynamic model of embeddedness in digital infrastructures. Information Systems Research, 30, 4 (2019), 1319–1342.

25. Fürstenau, D., Rothe, H., and Sandner, M. Shadow systems, risk, and shifting power relations in organizations. Communications of the Association for Information Systems, 41, (2017), 43–61.

26. Fürstenau, D., Rothe, H., and Sandner, M. Leaving the shadow: A configurational approach to explain post-identification outcomes of shadow IT systems. Business & Information Systems Engineering, 63, 2 (2021), 97–111.

27. Gregory, R.W., Beck, R., and Keil, M. Control balancing in information systems development offshoring projects. MIS Quarterly, 37, 4 (2013), 1211–1232.

28. Gregory, R.W., Kaganer, E., Henfridsson, O., and Ruch, T.J. It consumerization and the transformation of it governance. MIS Quarterly, 42, 4 (2018), 1225–1253.

29. Gu, B., Konana, P., Raghunathan, R., and Chen, H.M. The allure of homophily in social media: Evidence from investor responses on virtual communities. Information Systems Research, 25, 3 (2014), 604–617.

30. Gu, B., Xue, L., and Ray, G. IT governance and IT investment performance: An empirical analysis. In Proceedings of the 29th International Conference on Information Systems (ICIS). 2008, pp. 30.

31. Haag, S. and Eckhardt, A. Shadow IT. Business and Information Systems Engineering, 59, 6 (2017), 469–473.

32. Hair, J., Anderson, R., Babin, B., and Black, W. Multivariate Data Analysis. Cengage Learning, Andover, England, 2018.

33. Haki, K., Beese, J., Aier, S., and Winter, R. The evolution of information systems architecture: An agent-based simulation model. MIS Quarterly, 44, 1 (2020), 155–184.

34. Hanseth, O. and Lyytinen, K. Design theory for dynamic complexity in information infrastructures: The case of building internet. Journal of Information Technology, 25, 1 (2010), 1–19.

35. Hanseth, O. and Rodon Modol, J. The dynamics of architecture-governance configurations: An assemblage theory approach. Journal of the Association for Information Systems, 22, 1 (2021), 130–155.

36. Heinze, G. and Schemper, M. A solution to the problem of monotone likelihood in Cox regression. Biometrics, 57, 1 (2001), 114–119.

37. Heinze, G. and Schemper, M. A solution to the problem of separation in logistic regression. Statistics in Medicine, 21, 16 (2002), 2409–2419.

38. Henfridsson, O. and Bygstad, B. The generative mechanisms of digital infrastructure evolution. MIS Quarterly: Management Information Systems, 37, 3 (2013), 907–931.

39. Iyer, S., Killingback, T., Sundaram, B., and Wang, Z. Attack robustness and centrality of complex networks. PLoS ONE, 8, 4 (2013), e59613.

40. Jacobides, M.G., Cennamo, C., and Gawer, A. Towards a theory of ecosystems. Strategic Management Journal, 39, 8 (2018), 2255–2276.

41. Kopper, A., Fürstenau, D., Zimmermann, S., et al. Shadow IT and business-managed IT. International Journal of IT/Business Alignment and Governance, 9, 2 (2018), 53–71.

42. Kyte, A. The executive guide to application management. Gartner Report. Stamford, Connecticut, 2011.

43. Lagerström, R., Baldwin, C., MacCormack, A., and Aier, S. Visualizing and measuring enterprise application architecture: An exploratory telecom case. In Proceedings of the 47th Hawaii International Conference on System Sciences. IEEE, 2014, pp. 3847–3856.

44. Liu, D., Tan, Y., and Mookerjee, V. When ignorance can be bliss: Organizational structure and coordination in electronic retailing. Information Systems Research, 29, 1 (2018), 70–83.

45. MacCormack, A. and Lagerstrom, R. Designing an agile software portfolio architecture: The impact of coupling on performance. Academy of Management Proceedings, 2017, 1 (2017), 17511.

46. Mata, F.J., Fuerst, W.L., and Barney, J.B. Information technology and sustained competitive advantage: A resource-based analysis. MIS Quarterly, 19, 4 (1995), 487–504.

47. McKelvey, B. Avoiding complexity catastrophe in coevolutionary pockets: Strategies for rugged landscapes. Organization Science, 10, 3 (1999), 294–321.

48. McPherson, M., Smith-Lovin, L., and Cook, J.M. Birds of a feather: Homophily in social networks. Annual Review of Sociology, 27, 1 (2001), 415–444.

49. Misztal, B. Informality: Social Theory and Contemporary Practice. Routledge, London, England, 2002.

50. Nan, N. Capturing bottom-up information technology use processes: A complex adaptive systems model. MIS Quarterly, 35, 2 (2011), 505–532.

51. Newman, M.E.J. Modularity and community structure in networks. Proceedings of the National Academy of Sciences of the United States of America, 103, 23 (2006), 8577–8582.

52. Recker, J. Reasoning about discontinuance of information system use. Journal of Information Technology Theory and Application, 17, 1 (2016), 41–66.

53. Rezazade Mehrizi, M.H., Rodon Modol, J., and Zafar Nezhad, M. Intensifying to cease: Unpacking the process of information systems discontinuance. MIS Quarterly, 43, 1 (2019), 141–165.

54. Rinta-Kahila, T., Penttinen, E., and Lyytinen, K. Getting trapped in technical debt: Sociotechnical analysis of a legacy system’s replacement. MIS Quarterly, 47, 1 (2023), 1–32.

55. Sambamurthy, V. and Zmud, R.W. Arrangements for information technology governance: A theory of multiple contingencies. MIS Quarterly, 23, 2 (1999), 261–290.

56. Schelling, T.C. Dynamic models of segregation. The Journal of Mathematical Sociology, 1, 2 (1971), 143–186.

57. Shollo, A., Constantiou, I., and Kreiner, K. The interplay between evidence and judgment in the IT project prioritization process. Journal of Strategic Information Systems, 24, 3 (2015), 171–188.

58. Simon, H.A. The architecture of complexity. Proceedings of the American Philosophical Society, 106, 6 (1962), 467–482.

59. Simon, H.A. Near decomposability and the speed of evolution. Industrial and Corporate Change, 11, 3 (2002), 587–599.

60. Soliman, W. and Rinta-Kahila, T. Toward a refined conceptualization of IS discontinuance: Reflection on the past and a way forward. Information and Management, 57, 2 (2020), 103167.

61. Subramanyam, R., Ramasubbu, N., and Krishnan, M.S. In search of efficient flexibility: Effects of software component granularity on development effort, defects, and customization effort. Information Systems Research, 23, 3–part–1 (2012), 787–803.

62. Swanson, E.B. and Dans, E. System life expectancy and the maintenance effort: Exploring their equilibration. MIS Quarterly, 24, 2 (2000), 277–297.

63. Tilson, D., Lyytinen, K., and Sørensen, C. Digital infrastructures: The missing IS research agenda. Information Systems Research, 21, 4 (2010), 748–759.

64. Tiwana, A. Governance-knowledge fit in systems development projects. Information Systems Research, 20, 2 (2009), 180–197.

65. Tiwana, A. Platform synergy: Architectural origins and competitive consequences. Information Systems Research, 29, 4 (2018), 829–848.

66. Tiwana, A. and Kim, S.K. Discriminating IT governance. Information Systems Research, 26, 4 (2015), 656–674.

67. Tiwana, A. and Konsynski, B. Complementarities between organizational IT architecture and governance structure. Information Systems Research, 21, 2 (2010), 288–304.

68. Tiwana, A., Konsynski, B., and Venkatraman, N. Information technology and organizational governance: The IT governance cube. Journal of Management Information Systems, 30, 3 (2013), 7–12.

69. Tiwana, A. and Safadi, H. Atrophy in aging systems: Evidence, dynamics, and antidote. Information Systems Research, June (2023), 0–21.

70. Venkatraman, N. The concept of fit in strategy research: Toward verbal and statistical correspondence. Academy of Management Review, 14, 3 (1989), 423–444.

71. Warkentin, M., Johnston, A.C., Shropshire, J., and Barnett, W.D. Continuance of protective security behavior: A longitudinal study. Decision Support Systems, 92, (2016), 25–35.

72. Weill, P. and Ross, J. IT governance: How top performers manage IT decision rights for superior results. Harvard Business School Press, USA, 2010.

73. Widjaja, T. and Gregory, R.W. Monitoring the complexity of it architectures: Design principles and an it artifact. Journal of the Association for Information Systems, 21, 3 (2020), 664–694.

74. Winkler, T. and Brown, C. V. Organizing and configuring the IT function. In A. Tucker, T. Gonzalez, H. Topi and J. Diaz-Herrera, eds., Computing Handbook : Information Systems and Information Technology. CRC Press, Boca Raton, FL, 2014, pp. 1–14.

75. Winkler, T.J. and Benlian, A. The dual role of IS specificity in governing software as a service. In F.G. Joey, ed., Proceedings of the 33rd International Conference on Information Systems (ICIS). Association for Information Systems. AIS Electronic Library (AISeL), Atlanta, GA, 2012.

76. Winkler, T.J. and Brown, C. V. Horizontal allocation of decision rights for on-premise applications and software-as-a-service. Journal of Management Information Systems, 30, 3 (2013), 13–48.

77. Winkler, T.J., Goebel, C., Benlian, A., Bidault, F., and Günther, O. The impact of software as a service on IS authority - a contingency perspective. In Proceedings of the 32nd International Conference on Information Systems (ICIS). 2011, pp. 4052–4068.

78. Winkler, T.J. and Wessel, M. A primer on decision rights in information systems: Review and recommendations. In Proceedings of the 33rd International Conference on Information Systems (ICIS). Association for Information Systems. AIS Electronic Library (AISeL), 2018.

79. Xue, L., Ray, G., and Gu, B. Environmental uncertainty and IT infrastructure governance: A curvilinear relationship. Information Systems Research, 22, 2 (2011), 389–399.

80. Xue, Y., Liang, H., and Boulton, W.R. Information technology governance in information technology investment decision processes: The impact of investment characteristics, external environment, and internal context. MIS Quarterly: Management Information Systems, 32, 1 (2008), 67–96.

81. Yin, R.K. Case study research and applications. Sage Publications, Christchurch, New Zealand, 2017.
