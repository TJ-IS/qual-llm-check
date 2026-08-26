---
otero_id: 26560
otero_key: "W8RG62DT"
title: "Join Up or Stay Away? Coalition Formation for Critical IT Infrastructure"
authors: "Hong Guo; Yipeng Liu; Barrie R. Nault"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.0463"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Join Up or Stay Away? Coalition Formation for Critical IT Infrastructure

Hong Guo,<sup>a</sup> Yipeng Liu,<sup>b</sup> Barrie R. Nault<sup>c,</sup>\*

<sup>a</sup> W. P. Carey School of Business, Arizona State University, Tempe, Arizona 85287; <sup>b</sup> College of Business, Northern Illinois University, DeKalb, Illinois 60115; <sup>c</sup> Haskayne School of Business, University of Calgary, Calgary, Alberta T2N 1N4, Canada

Contact: hguo@asu.edu, https://orcid.org/0000-0001-6028-8155 (HG); yliu@niu.edu, https://orcid.org/0000-0001-7645-4883 (YL); nault@ucalgary.ca, https://orcid.org/0000-0001-7856-885X (BRN)

Received: September 9, 2021 Revised: August 25, 2022; July 3, 2023 Accepted: August 23, 2023 Published Online in Articles in Advance: October 23, 2023

https://doi.org/10.1287/isre.2021.0463

Copyright: © 2023 INFORMS

Abstract. We consider districts that invest in critical IT infrastructure, which spill over to other districts. IT infrastructure is considered critical if its disruption can cause significant damage to security, the economy, public health, or safety. Districts choose whether to participate in a coalition noncooperatively, and the coalition subsequently makes resource investment decisions cooperatively. Districts “inside” the coalition have superior interoperability in the spillovers relative to “outside” districts. Inside districts also benefit from a coalition economy of scale and a discounted resource investment cost, and they face diseconomies of scope in the number of coalition members and their investment levels. Coalition structures include grand, partial (varying in size), minimal (two members), and singleton, and we consider the formation of only one coalition. We find that inside districts’ resource levels decrease with coalition size. Even with homogeneous districts, any size coalition can be an equilibrium depending on the coalition economy of scale and the relative interoperability of resources in inside versus outside districts. The equilibrium coalition size is increasing in the economy of scale and decreasing in relative interoperability. Similarly, any size coalition can be socially optimal depending on the coalition economy of scale and relative interoperability. The socially optimal coalition size is also increasing in the economy of scale and decreasing in relative interoperability. In most cases, the socially optimal coalition size is larger than the equilibrium coalition. A subsidy or tax can incentivize the equilibrium coalition size and district resource levels to be socially optimal, providing a general solution to the provisioning of critical IT infrastructure. We use the European Union’s Digital COVID Certificate program providing vaccine status information and the U.S. Government’s Direct Project that supports the establishment of nationwide health information exchanges to illustrate elements of our model.

History: Juan Feng, Senior Editor; Yifan Dou, Associate Editor

Funding: This work was supported by Social Sciences and Humanities Research Council (SSHRC) of Canada [Grant 435-2016-0431].

Supplemental Material: The e-companion is available at https://doi.org/10.1287/isre.2021.0463.

Keywords: coalition formation • critical IT infrastructure • organizational economics • interoperability • public policy

## 1. Introduction

Critical IT infrastructure differs from basic IT infrastructure in how damaging the consequences of the infrastructure’s disruption are. Consequences include “ … a debilitating effect on security, national economic security, national public health or safety, or any combination thereof” (Cybersecurity and Infrastructure Security Agency 2021a). Disruptions to IT infrastructure can spill over to other infrastructures that are critical and even spill over across borders (Gallais and Filiol 2017). For example, in Canada, critical IT infrastructure can be interconnected and interdependent within and across provinces, territories, and national borders (Government of Canada 2009).

IT infrastructure is often classified as “hard” or “soft,” where the former is physical, such as fiber-optic cables for high-speed internet, and the latter is institutional, such as data sharing among emergency services and government departments. A conceptual view of IT infrastructure is an interconnected set of platforms for activities where the seamless functioning of IT infrastructure from connected jurisdictions depends on compatibility and interoperability. Crucial to compatibility and interoperability are technical standards and supporting services, which, in turn, are essential for IT infrastructure to fulfill its potential as a public good (NCOIC 2012).

The more technologically complex the IT infrastructure is, the less well defined technical standards and supporting services are. As a result, compatibility and interoperability can be compromised. In this case, centralized decisions about critical IT infrastructure investment, where standards and supporting services are uniform, can take advantage of positive externalities and benefit individual jurisdictions and society. Obtaining this benefit requires coordinating decisions among a set of jurisdictions such that they behave as a coalition whereby the coalition can enforce agreements with coalition members.

In brief, our objectives are to construct a model of coalition formation where different jurisdictions, which we refer to as districts, decide whether to participate noncooperatively but the coalition invests cooperatively based on spillovers, interoperability, and cost elements, and to characterize what coalition structures can occur in equilibrium, how these would differ from coalition structures that are socially optimal, and whether there is a direct incentive that would cause equilibrium coalition structures to be socially optimal. As such, our work is normative in that we build a model to represent a generic institutional setting, identify the goals of different participants and how these lead to different coalition structures, and design a direct mechanism to achieve the policy objective.

## 1.1. Illustrative Examples

We use two examples to help explain our model, recognizing that our goal is to illustrate elements of our analysis but not to model the institutional details of each example directly. First, we use the European Union’s Digital COVID Certificate (EUDCC) program, which provides certified information about an individual’s vaccination, testing, and recovery status during the COVID-19 pandemic. The certificates allow for travel between participating member states as well as access to venues and services within member states based on an individual’s certificate status and the individual member state’s chosen restrictions. The EUDCC program has technical specifications delineated by the eHealth Network, a cooperative European Commission organization consisting of member states and observer representation.<sup>1</sup> The EUDCC program involves an IT infrastructure “gateway” that stores and shares cryptographic public keys across participating member states used for verification of certificates. member states have autonomy regarding restrictions that require an EUDCC and what certificate types are accepted for certain restrictions.

These open-source specifications include technical specifications of approved regulations and implementing decisions,<sup>2</sup> the architecture and information relations using a central management system gateway or digital COVID certificate gateway (DCCG),<sup>3</sup> an interoperable two-dimensional code detailing the use of an encoding mechanism, QR barcode,<sup>4</sup> specifications for transferring shared information,<sup>5</sup> public key certificate governance, which details the exchange of cryptographic information within a region and with the gateway,<sup>6</sup> and EUDCC val idation rules.

Our second illustrative example is the Direct Project, a U.S. government initiative that is part of the Nationwide Health Information Network. The Direct Project’s goal is to support health information exchange (HIE) activities by providing a common policy framework specifying “ … a secure, scalable, standards-based way to establish universal health addressing and transport for participants (including providers, laboratories, hospitals, pharmacies, and patients) to send encrypted health information directly to cryptographically validated recipients over the Internet” (Direct Project 2019). In practice, the Direct Project provides technical standards and services that enable secure and interoperable exchange of health information by neutral third-party organizations that facilitate information exchange called HIEs or alternatively called health information organizations (HIOs) (Vest and Gamm 2010). The role of HIOs is to facilitate health information exchange such as access to and retrieval of electronic health informa tion among health service providers, including hospitals, clinics, and other healthcare providers. Many are regional HIOs (then called RHIOs) such as Indiana HIE, Washing ton State’s OneHealthPort, Rhode Island Quality Institute, and Mississippi Coastal Health Information Exchange.

In their role as facilitators of health information exchange, HIOs invest in health information technology (HIT) resources including hardware, telecommunications, software, and policies to ensure the speed and safety of accessing health information. The Office of the National Coordinator for Health Information Technology (ONC) evaluates the applicability of standards chosen by individual HIOs with respect to specifications developed by the Direct Project.<sup>8</sup>

In part of its broader mission, the World Health Organization’s Digital Implementation Investment Guide (DIIG) describes a setting for Digital Document of COVID-19 Certificate Vaccination Status (DDCC:VS) that uses a multihealthcare service-related OpenHIE architecture with mechanisms for interoperability across different applications in the DIIG. Thus, there is a conceptual level where our two examples converge.

## 1.2. Research Questions and Results Preview

Using a district to represent a jurisdiction as a decisionmaking unit, we address a set of related research questions. The first question is whether a coalition of districts other than the grand coalition can be an equilibrium in which no districts “inside” the coalition prefer to leave and those “outside” the coalition do not want to participate, especially when districts are homogeneous. In the context of our examples, this means whether some but not all member states (HIOs) choose to participate in the EUDCC program (Direct Project) in equilibrium. The second question is whether a coalition of districts other than the grand coalition can be socially optimal. In our examples, this is whether it is socially optimal for some but not all member states (HIOs) to choose to participate in the EUDCC program (Direct Project). The third question is whether an equilibrium coalition size can also be socially optimal and, if not, then whether there is a simple mechanism that can induce the equilibrium coalition size to be socially optimal. In our examples, this is whether the number of member states (HIOs) that choose to participate is also socially optimal and, if not, then whether there is a simple and implementable incentive that the EUDCC program (Direct Project) can employ to induce the socially optimal number of member states (HIOs) to participate.

To answer these questions, we develop a model for the provisioning of critical IT infrastructure across a fixed number of districts, where each district invests in infrastructure resources and where these infrastructure resources spill over to other districts. Districts choose whether to participate in a coalition noncooperatively where infrastructure investments of districts that choose to participate are decided cooperatively and centrally by a coalition coordinator. The coalition coordinator’s role is to maximize the surplus of the coalition through the choice of infrastructure investments for participating districts. There is perfect interoperability for resource spillovers within the coalition, and the coalition benefits from a coalition economy of scale in infrastructure investment but suffers diseconomies of scope in the number of districts in the coalition and their levels of investment. Districts outside the coalition make infrastructure investments as stand-alone entities, and their infrastructure spillovers with other districts, including those inside the coalition, are reduced because of lower levels of interoperability.

In our examples, in the EUDCC program, the eHealth Network provides technical specifications for the EUDCCs, districts that participate are member states that use a national “backend” IT system as well as issuer, holder (wallet), and verifier applications.<sup>9</sup> Thus, the coalition coordinator that decides the specifications of IT infrastructure for participating member states, which are effectively the IT infrastructure investments, is the eHealth Network. In the Direct Project, the ONC for HIT provides technical standards and support services, districts are HIOs engaged in health information exchange, and infrastructure investments are HIT resources, including hardware, telecommunications, software, and policies. Thus, the ONC for HIT acts as coalition coordinator through its interoperability standards advisory. Table 1 systematically lists examples of critical IT infrastructures in different industry sectors. For each example, we specify the coalition coordinator and district, which illustrate the connections between our key modeling components and real-world applications.

It is important to note that the social planner and coalition coordinator have different roles in these contexts. In the context of the EUDCC program, the social planner is the European Commission, and the coalition coordinator is the eHealth Network. As a social planner, the European Commission’s role is to maximize social welfare that includes all member states in the European Union. In contrast, the eHealth network acting as the coalition coordinator primarily focuses on maximizing the benefits of the member states that choose to participate in the EUDCC program. In the context of the Direct Project, the social planner is the U.S. Department of Health and Human Services (HHS), and the coalition coordinator is the ONC. HHS is responsible for all HIOs, whether they participate in the Direct Project or not. In contrast, the ONC is directed by HHS to focus on HIOs that participate in the Direct Project. In the E-ZPass example, the coordinator’s role is to maximize the benefits of the E-ZPass system for this specific coalition, focusing on solutions and improvements that address the coalition’s particular needs and challenges. In contrast, a social plan ner would aim to optimize the toll collection system’s benefits across all states and jurisdictions. In the positive train control (PTC) example, a social planner, for exam ple, the Federal Railroad Administration, would be con cerned with the nationwide implementation, operation, and benefits of this system. Their focus would be to maxi mize safety and efficiency of all rail networks across the country. In contrast, a coalition coordinator, for example, the American Railway Engineering and Maintenance-of Way Association (AREMA), would focus on a specific group of rail companies or regions that have decided to work together on PTC issues. The coalition coordinator’s role would be to optimize the benefits of the PTC system for this specific coalition. They would work on coordinat ing implementation schedules, sharing best practices, and addressing shared challenges or needs.

In our formulation, if all districts choose to invest in infrastructure resources individually (i.e., no district chooses to participate in a coalition), then we call the resulting coalition structure a singleton. If only two districts choose to participate in a coalition, then we call it a minimal coalition. If at least three districts choose to participate, then we call it either a partial coalition when a strict subset of districts choose to participate or a grand coalition when all districts choose to participate.

Analyzing our coalition formation model leads to the following main results. First, we show that all sizes of coalitions other than the grand coalition can arise in equilibrium even when districts are homogeneous. Next, we determine the equilibrium coalition size and social optimum coalition size and then detail their properties such as how the different coalition structures become the equilibrium structure with changes in the underlying parameters. Third, we compare the equilibrium coalition size and social optimum coalition size, showing when they overlap and when they do not, and we derive a simple incentive mechanism that can induce the equilibrium coalition size to also be socially optimal.

Table 1. Critical IT Infrastructure Examples

<table><tr><td>Sector</td><td>Critical IT infrastructure</td><td>Coalition coordinator</td><td>District</td></tr><tr><td>Healthcare</td><td>European Union&#x27;s Digital COVID Certificate (EUDCC) program</td><td>eHealth Network</td><td>European Union member states</td></tr><tr><td>Healthcare</td><td>Direct Project as a part of Nationwide Health Information Network</td><td>Office of the National Coordinator for Health Information Technology (ONC)</td><td>Health information exchange (HIE) or health information organizations (HIOs)</td></tr><tr><td>Security</td><td>National Cybersecurity Protection System (NCPS)</td><td>Cybersecurity and Infrastructure Security Agency (CISA)</td><td>Federal Civilian Executive Branch (FCEB) agencies</td></tr><tr><td>Transportation</td><td>Electronic toll collection (ETC) system</td><td>E-ZPass Interagency Group (IAG)</td><td>Individual states&#x27; toll collection agencies</td></tr><tr><td>Transportation</td><td>Positive train control (PTC) system</td><td>American Railway Engineering and Maintenance-of-Way Association (AREMA)</td><td>Amtrak, commuter railroads, and freight railroads</td></tr><tr><td>Finance</td><td>Society for Worldwide Interbank Financial Telecommunication (SWIFT)</td><td>SWIFT operations center</td><td>Financial institutions</td></tr><tr><td>Energy</td><td>Public electric vehicle charging infrastructure</td><td>Electric Vehicle Charging Association (EVCA)</td><td>Automotive manufacturers, private charging station providers, and local municipalities</td></tr></table>

Note. Except for the EUDCC and SWIFT examples, all other cases are located in the United States.

The social planner determines the incentive mechanism to achieve the socially optimal size maximizing welfare across districts.

We also extend our analysis in two directions. First, in Online Appendix B, we consider districts with different resource investment costs and examine the impact of such heterogeneity across districts. We find that, similar to when districts are homogeneous, all coalition structures (sizes) can arise in equilibrium. Moreover, the pattern of transitions between equilibrium coalition structures as the underlying parameters change is the same as with homogeneous districts. Second, in Online Appendix C, we relax our assumption on the range of interoperability between districts outside the coalition with those inside and find that when interoperability is low, certain coalition sizes cannot be socially optimal.

## 2. Literature Review

Our work is related to two research streams: provisioning of critical IT infrastructure and coalition formation. In this section, we first review these two research streams and then discuss our contribution to the existing literature.

The first research stream is that of provisioning critical IT infrastructure. Prior studies in this area focus on the provision of different types of critical IT infrastructures such as internet (Cheng et al. 2011), public safety networks (Liu et al. 2017), cloud computing (Guo et al. 2019), intelligent transportation systems (Cheng et al. 2020), and disaster management systems (Guo et al. 2021).

Cheng et al. (2011) investigate the impact of net neutrality on broadband service providers’ incentive to invest in their internet infrastructure and find that the incentive is likely to be lower in the absence of net neu trality. Nault and Zimmermann (2019) study openness and prioritization in a two-tier internet and find that to maintain the quality of service of the open internet and increase welfare, a policy mechanism is necessary to motivate broadband provider investment in internet infrastructure. Liu et al. (2017) compare centralized, decentralized, and mixed organization forms in the provision of public safety networks. The focus is on individual districts’ incentives to opt in or opt out of the centralized organization form. Guo et al. (2019) study cloud service providers’ provisioning strategies of virtual infrastructure resources under cloud service agreements. Online optimization algorithms are developed for both periodic and aperiodic policies. Besides the investment in transportation infrastructure, Cheng et al. (2020) offer empirical evidence that IT-enabled intelli gent traffic systems are effective in mitigating traffic congestion. Guo et al. (2021) capture key characteristics of provisioning disaster management systems and propose a framework that reflects the differences among three interoperability approaches: integrated, unified, and federated. They further analyze the equilibrium and socially optimal interoperability approach in a two-district setting.

Related to this work is research on the effect of IT infrastructure capability on cross-unit coordination. Firms with higher IT infrastructure capability, capability that includes infrastructure services that cross organizational boundaries and reach constituencies inside and outside the firm to transfer information and process transactions, are better able to adopt and implement changes in processes quickly (Broadbent et al. 1999). In the context of supply chains, IT infrastructure integration is the degree to which firms establish information systems for consistent and rapid transfer of information within and across their boundaries. Such integrated IT infrastructure allows firms to separate information and physical flows and to share information with partners to improve planning for the staging and movement of physical products (Rai et al. 2006). Also, there is evidence that with higher levels of environmental uncertainty (e.g., volatility in the environment and heterogeneity among outside entities), such as would be the case with critical IT infrastructure, centralized IT infrastructure governance has advantages both in terms of sharing and coordination of resources and of economies of scale (Xue et al. 2011).

The second research stream our work is related to is coalition structures in the literature on coalition formation. For a recent survey of the general topic of coalition formation, refer to Ray and Vohra (2015). Here, we focus on reviewing prior studies on coalition structures. Ray and Vohra (1999) characterize equilibrium coalition structures in a general context with widespread externalities and binding agreements among agents within a coalition. Ray and Vohra (2001) study the provision of public goods when agents may form coalitions through agreements among themselves and make rational predictions of the coalition structure. Thijssen et al. (2004) consider a coalition structure with one coalition and a group of outside agents and analyze a spillover game that captures the spillovers from the coalition to outside agents. Nagarajan and Sosˇic ´ (2007) examine agents forming coalitions dynamically in competitive markets and analyze the stability of coalition structures. Hu et al. (2013) study the revenue-sharing schemes in airline alliances combining cooperative and noncooperative game theory. Their focus is on deriving a revenue-sharing rule that induces the grand coalition and that ensures the individual airlines achieve the same revenues as a central planner managing the global alliance network.

In the coalition formation literature, there are different solution concepts that can be broadly categorized into noncooperative solution concepts and cooperative solution concepts (Carraro 2003). A cooperative solution may require that no subset of agents have an incentive to break away from the coalition, that is, to eliminate the possibility that a subset of agents may collude and break away together from the coalition. In a noncooperative game of coalition formation, all agents simultaneously decide whether to join the coalition, and individual agents make their participation decisions independently.

Our contribution to the existing literature is threefold. First, we model the essential generic features of critical IT infrastructure as opposed to a particular type of critical IT infrastructure studied in the literature.

Specifically, individual districts enjoy resource spill over benefits from other districts, and the spillover is moderated by the interoperability between the two districts’ infrastructure. Second, we characterize unique features of provisioning critical IT infrastructure through coalition formation, where districts simultaneously make decisions to join the coalition noncooperatively. Moreover, provisioning critical IT infrastructure cooperatively through the coalition exhibits both an economy of scale and diseconomies of scope, and the interoperability between inside and outside districts is lower compared with that among the inside districts. Finally, we contribute to the literature by being the first to analyze the provision of critical IT infrastructure involving more than two districts, whereas most of the existing literature on critical IT infrastructure considers only two districts. Modeling more than two districts enables the analysis of different equilibrium coalition structures (singleton, minimal coalition, partial coalition, and grand coalition) and the corresponding coalition size. We further design a general incentive mechanism to induce the socially optimal coali tion structure.

## 3. Model Setup

In this section, we build a coalition formation game to model the provisioning of interoperable critical IT infrastructure. Following d’Aspremont et al. (1983) and Thijssen et al. (2004), we model the formation of a single coalition where districts outside the coalition are a group of singletons—effectively a noncooperative game of coalition formation whereby individual districts choose whether to join the coalition. This is the case with the EUDCC program where member states decide whether to participate to provide certified vaccination information for their resident and member states that do not participate do not use the EUDCC program. Similarly, HIOs that participate in the Direct Project are members of the coalition, and those HIOs that do not participate instead exchange information with idiosyncratic protocols. This structure also mirrors that of a government, an alliance building a public network, and a cartel (Thijssen et al. 2004).

Once the coalition forms, districts in the coalition enter a binding agreement to centralize district IT infrastructure resource investment decisions, allocating these decisions to a single designated coalition coordinator. The coalition coordinator is an external party that can enforce the centralized resource investment decisions, making district resource investment a cooperative game. In the EUDCC program, the eHealth Network as coalition coordinator directs resource investment decisions of participating member states through its technical specifications that define the necessary capabilities, which, in turn, determine the investments required to meet these capabilities. In the Direct Project, the ONC as coalition coordinator directs resource investment decisions by evaluating standards chosen by participating HIOs with technical standards and services developed by the Direct Project. Again, these standards determine the investments required to meet the capabilities resulting from these standards.

Thus, in our model setup districts decide whether to participate in the coalition as a noncooperative game—a coalition coordinator cannot mandate participation— but districts that participate allocate resource investment decision rights to an external party whereby districts in the coalition play a cooperative game to maximize the welfare of the coalition.

## 3.1. Coalition Structures

We consider a finite number, n, of homogeneous districts, $i \in \left\{ { 1 , 2 , \dots , n } \right\}$ , that provide a system of critical IT infrastructure. In our examples, the candidate districts are well defined so that the potential number of districts, $n ,$ is known. The districts invest resources in their critical IT infrastructure, and there are positive externalities between districts. We consider districts that can invest in resources to support infrastructure either through coalition or by themselves, where there are interoperability benefits for those districts that participate in a coalition. In Online Appendix B, we consider heterogeneous districts with different resource investment costs and examine the impact of such heterogeneity across districts.

When a coalition forms, district IT infrastructure resource investment decisions are centralized to a single designated coalition coordinator. As Xue et al. (2011) find, there are advantages provided by centralized IT infrastructure governance for the sharing and coordination of resources. When there is no coalition (i.e., singleton), or for districts that do not participate in the coalition, then the resource investment decision is decentralized to the individual districts.

Let $j \in \{ 2 . . . n \}$ denote the number of districts that choose resource levels to support infrastructure together, hence forming a coalition. Without loss of generality, we assume districts $\{ 1 , 2 , \ldots , j \}$ are the districts that form the coalition, and districts $\{ j + 1 , j + 2 , \ldots , n \}$ are the districts that are not part of the coalition. The grand-coalition case of j � n corresponds to all districts choosing to invest in infrastructure resources as a coalition. The partialcoalition case of $2 < j < n$ corresponds to some districts choosing to invest in infrastructure resources through coalition, whereas others do not. A minimal coalition corresponds to the case when only two districts form a coalition to invest in infrastructure resource levels, $j = 2 .$ Finally, a singleton is where each district invests in its infrastructure resource level without concern for other districts.

Infrastructure resources are distributed across districts but can be accessible to all. This causes an individual district to value infrastructure resource investments in the other districts as well as valuing these resource investments in its own district, giving rise to positive externalities. Using subscripts to identify individual districts, let $g _ { i } \in [ 0 , \bar { g } ]$ denote the levels of infrastructure resource investment made by each district, and let $p \in R ^ { + }$ denote the cost per unit of resource investment.

Following prior work in public finance (Oates 1972) and provisioning of critical IT infrastructure (Liu et al. 2017, Guo et al. 2021), for a given district, we use κ ∈ [0, 0:5] to denote the weight of resources in the other districts that spill over and provide value and use 1 � κ to denote the weight of resources in its own district. Defining κ this way ensures local infrastructure resources always have a higher weight: when $\kappa = 0 ,$ , a district only values resources in its own district; when $\kappa = 0 . 5 ,$ , a district values resources in its own and other districts equally. We interpret κ as the degree of spillover of resources between districts such that a higher κ represents a higher cross-district value from resources, that is, greater positive externalities.

In our main model with homogeneous districts, a common weighting for local infrastructure resources is inherently consistent. In our extension to heterogeneous districts in Online Appendix B, each district would know their κ (e.g., κ is implied by policy in the EUDCC example) or can accurately estimate κ (especially if the policy was public).

Regarding the EUDCC program, spillovers can result from both personal and business travel as well as logistics supporting intermember state trade. For the Direct Project, benefits from spillovers result from different HIOs sharing health information in order to provide healthcare service to different participants, including patients, hospitals, pharmacies, laboratories, etc.

## 3.2. Assumptions

We use the terms “inside” and “outside” to identify those districts inside and outside the coalition, respectively. Our first assumption differentiates the interoperability efficiency of the resource spillover for those districts inside versus outside the coalition.

Assumption 1. Compared with districts inside the coali tion, those districts outside the coalition have a relative interoperability of between 50% and 100%.

We use $\beta \in \left( 1 / 2 , 1 \right]$ to represent the overall relative interoperability for outside districts compared with inside districts where the smaller the $\beta ,$ , the lower the relative interoperability. We place a lower limit on relative interoperability such that $\beta > 1 / 2$ to ensure social welfare is concave in coalition size. It is also reasonable that relative interoperability is at least 50%. In our second extension in Online Appendix C, we relax this lower limit.

When $\beta = 1$ , resources are fully interoperable across all districts regardless of whether the district is inside or outside the coalition. When $\beta \in \left( 1 / 2 , 1 \right)$ , a district within the coalition derives more value from resources in other districts within the coalition than from resources in districts outside the coalition.

In our EUDCC program example, member states that participate and use the DCC’s technical specifications are our inside districts, and those that do not are outside districts. Residents of member states that participate in the program can use the DCC for seamless travel between participating member states (conditional on local restrictions) for personal and business purposes, including the movement of goods for trade. Residents of nonparticipating states and countries face delays and even exclusion from the participating member states. The EUDCC program requires that participating member states implement a universal system of standards. Consequently, interoperability is known and perfect among the member states that participate (the interoperability among all inside districts is normalized to one in our model). Moreover, as these standards are open source, nonparticipants can determine their interoperability, $\beta ,$ with the coalition participants, and we take this $\beta$ as the same for all nonparticipants.

Mapping the Direct Project example to our model, participants of the Direct Project correspond to inside districts, and nonparticipants correspond to outside districts. All participants can leverage specified protocols and standards to access and retrieve health information from each other. However, nonparticipants may have to exert extra effort, such as significantly redesigning their clinical workflow, to communicate with other health information organizations. Interoperability issues in critical IT infrastructure are common, for example, in disaster management systems (Guo et al. 2021).

Using the elements we defined, we can detail the benefits each district receives from resources based on whether they are inside or outside the coalition. We take the benefits as additive and use $B _ { i } ( j )$ to denote the benefits of district I given a coalition size j:

$$
B _ {i} (j) = \left\{ \begin{array}{l} [ 1 - \kappa ] g _ {i} + \kappa \left[ \sum_ {l = 1} ^ {i - 1} g _ {l} + \sum_ {l = i + 1} ^ {j} g _ {l} \right] + \kappa \beta \sum_ {l = j + 1} ^ {n} g _ {l}, \\ \text { for   inside   district } i \in \{1, \ldots , j \} \\ [ 1 - \kappa ] g _ {i} + \kappa \beta \left[ \sum_ {l = 1} ^ {i - 1} g _ {l} + \sum_ {l = i + 1} ^ {n} g _ {l} \right], \\ \text { for   outside   district } i \in \{j + 1, \ldots , n \}. \end{array} \right.\tag{1}
$$

The difference in benefit $B _ { i } ( j )$ for inside districts relative to outside districts is that they have full interoperability of the resource spillovers from other inside districts (first line, second term), but they have only relative interoperability of the resource spillovers from outside districts (first line, third term). In contrast, outside districts have only relative interoperability for all resource spillovers (second line, second term). Thus, the benefit of being inside is the relative interoperability of resource spil lovers from other inside districts. Our setup using κ and $\beta$ has the same effect as using a different κ for inside and outside districts with the additional advantage of parameterizing the difference. There is little loss in generality of modeling benefit as additive so long as benefits aggregate, and aggregation for outside districts is tempered by $\beta .$

Cost Structure. For simplicity and tractability, we use a quadratic form for the costs of resources. For any district outside the coalition, costs are

$$
C _ {i} = p g _ {i} ^ {2} \mathrm{for} i \in \{j + 1, \ldots , n \}.
$$

Formulating the total costs across all inside districts in the coalition, we develop a cost function form that captures both a coalition economy of scale and diseconomies of scope. We expect a cost economy of scale would occur for the accumulation of district resources across the coalition with the removal of duplicate resources, learning by doing across districts using similar resources, etc. We expect cost diseconomies of scope that would result from challenges of interoperability, integration, and coordination of resources from different districts in the coalition. Our second assumption implements these scale and scope economies.

Assumption 2. There are separate effects of scale and scope on the accumulated resource costs faced by the coalition:

(a) A coalition economy of scale decreases the accumulated resource costs faced by the coalition;

(b) Diseconomies of scope increase the accumulated resource costs faced by the coalition.

We use the parameter $\alpha ,$ where $\alpha \in ( 0 , 1 )$ , to capture the benefits of a coalition economy of scale when multiple districts form the coalition. Effectively, α is a proportional resource cost reduction for a minimal-or-greate coalition that dampens the accumulated resource costs faced by the coalition. To keep our model tractable, we model α as a constant across the different possible sizes of the coalition where our main focus is to capture a cost reduction as a consequence of being inside the coalition, and when considering joining the coalition, the districts would be informed about α. The smaller α is, the greater the coalition economy of scale. In other words, α is a reverse measure of the coalition economy of scale. Meanwhile, as the coalition size grows, there are more districts and resources to coordinate; hence, the total cost to maintain the effectiveness of resources in the coa lition increases. To capture diseconomies of scope, we use the square of the sum (which is greater than the sum of the squares) for the total cost the coalition faces. Ou form for the total cost of resources in a coalition of size j is

$$
T C (j) = \alpha p [ g _ {1} + \dots + g _ {j} ] ^ {2} \mathrm{for} j \in \{2, \ldots , n \}.\tag{2}
$$

Note that in the singleton case, where no coalition is formed, all districts have the same cost structure as the outside district, $p g _ { i } ^ { 2 }$

To summarize, this cost structure captures both a cost economy of scale and cost diseconomies of scope. When districts form a coalition, we operationalize cost advantages of being an inside district via an economy of scale (α) and cost disadvantages of being an inside district via diseconomies of scope (square of the sum). When there is no coalition (singleton case), there are no economies of scale or diseconomies of scope in each district’s resource cost. Qualitatively, there is little loss of generality in our choosing a quadratic form for costs—what is necessary is a form of cost convexity that yields diseconomies of scope.

In the EUDCC program, there is both a coalition economy of scale and diseconomies of scope. On one hand, because the issuer, holder, and verifier applications have common specifications, there is a coalition economy of scale across participating member states, as coding can be shared. On the other hand, each member state provides its national “backend” that connects to the DCC “gateway” for certificate information and may be integrated with their own healthcare systems where specifications are likely idiosyncratic, creating diseconomies of scope. In our Direct Project example, both an economy of scale and diseconomies of scope exist. As more HIOs participate in the Direct Project, thanks to the economy of scale, participants enjoy proportionally lower resource costs for data storage, data protection, and data sharing from cloud-based solutions. At the same time, participants also suffer diseconomies of scope with higher costs of integration such as tracking and analyzing larger numbers of electronic health record (EHR) systems.

## 3.3. Coalition Welfare and Outside District Surplus

We use CW(j) to denote the coalition welfare for a coalition of size j, which is the sum of total benefits from infrastructure resources of all inside districts minus the total cost of resources to the coalition. When the coalition is minimal, partial, or grand, the coalition welfare is given by

$$
\begin{array}{l} C W (j) = \sum_ {i = 1} ^ {j} B _ {i} (j) - T C (j) \\ \qquad = [ 1 - \kappa ] \sum_ {i = 1} ^ {j} g _ {i} + \kappa [ j - 1 ] \sum_ {i = 1} ^ {j} g _ {i} + \kappa \beta j \sum_ {i = j + 1} ^ {n} g _ {i} \\ \qquad - \alpha p \left[ \sum_ {i = 1} ^ {j} g _ {i} \right] ^ {2}. \end{array}
$$

The first term on the right-hand side is resources from inside districts, the second term is resource spillovers inside the coalition, the third term is resource spillovers from districts outside the coalition with relative interoperability, $\cdot \beta ,$ and the last term is costs capturing our coalition economy of scale α and diseconomies of scope (square of the sum).

The surplus for each district outside the coalition is given by 「 7

$$
\begin{array}{c} S _ {j + 1} (j) = B _ {j + 1} (j) - C _ {j + 1} = [ 1 - \kappa ] g _ {j + 1} + \kappa \beta \left[ \sum_ {i = 1} ^ {n} g _ {i} - g _ {j + 1} \right] - p g _ {j + 1} ^ {2} \\ \vdots \\ S _ {n} (j) = B _ {n} (j) - C _ {n} = [ 1 - \kappa ] g _ {n} + \kappa \beta \sum_ {i = 1} ^ {n - 1} g _ {i} - p g _ {n} ^ {2}, \end{array}
$$

where the terms on the right-hand side are a district’s own resources, spillovers from other districts with relative interoperability, $\beta ,$ and full costs.

Timing. The timing of our coalition formation game is as follows. In stage 1, each district chooses whether to participate in the coalition. The resulting coalition structure is the grand coalition with all n districts choosing to participate, a partial coalition with $j > 2$ districts choosing to participate, a minimal coalition with only two districts choosing to participate, or a singleton with no district choosing to participate. In stage 2, each outside district chooses the resource level of its own critical IT infrastruc ture. Simultaneously, the coalition coordinator chooses the resource level for each inside district.

## 4. Optimal District Resources

We solve our coalition formation game through backward induction. Given the coalition structure, in stage 2, the resource levels for districts inside the coalition are determined through a cooperative game where the coalition coordinator chooses resource levels for inside districts to maximize coalition welfare and outside districts choose their resource levels to maximize their surpluses.

## 4.1. Resource Level for Inside Districts

For districts that choose to build the infrastructure system cooperatively through the coalition, the coalition centralizes the choice of resource levels for each district to maximize the coalition welfare, CW(j). The formula tion in (3) presents the decision problem for the coalition coordinator:

$$
\begin{array}{l} \max _ {g _ {1}, \dots , g _ {j}} C W (j) = \max _ {g _ {1}, \dots , g _ {j}} \left\{\left[ 1 - \kappa \right] \sum_ {i = 1} ^ {j} g _ {i} + \kappa [ j - 1 ] \sum_ {i = 1} ^ {j} g _ {i} \right. \\ \qquad \qquad \qquad \qquad + \kappa \beta j \sum_ {i = j + 1} ^ {n} g _ {i} - \alpha p \left[ \sum_ {i = 1} ^ {j} g _ {i} \right] ^ {2} \Bigg \} \\ \text { Subject   to: } \quad 0 \leq g _ {i} \leq \overline {{g}} \text { for } i \in \{1, \ldots , j \}. \end{array}\tag{3}
$$

Solving the maximization problem for districts inside the coalition, where subscript in corresponds to district in inside the coalition, thus in $\in \{ 1 , \ldots , j \}$ , we find that the optimal resource level is given by

$$
g _ {1} ^ {*} (j) = \dots = g _ {j} ^ {*} (j) = g _ {i n} (j) = \frac {1 + [ j - 2 ] \kappa}{2 \alpha j p},\tag{4}
$$

where $g _ { i n } ( j )$ depends on the coalition size, $j ,$ given the degree of spillover (κ), the coalition economy of scale parameter (α), and our resource cost parameter (p). It is straightforward that the optimal resource level for an inside district is increasing in the coalition economy of scale, $\partial g _ { i n } ( j ) / \partial \alpha < 0$ , where a greater coalition economy of scale corresponds to a lower α.

As districts are homogeneous, the optimal resource level provided by each inside district is the same. Therefore, the benefits for each inside district are the same and are given by

$$
\begin{array}{r l} & B _ {1} ^ {*} (j) = \dots = B _ {j} ^ {*} (j) = B _ {i n} (j) \\ & \qquad = \frac {1}{2 j p \alpha} [ \kappa j ^ {2} [ \kappa - \alpha \beta [ 1 - \kappa ] ] \\ & \qquad + \kappa j [ \alpha \beta [ 1 - \kappa ] n + 2 - 4 \kappa ] + [ 1 - 2 \kappa ] ^ {2} ]. \end{array}\tag{5}
$$

Notice our relative interoperability parameter, $\beta ,$ only matters directly in the benefit function and not through the optimal resource level.

## 4.2. Resource Level for Outside Districts

If a district chooses to build its infrastructure system outside the coalition, then it makes the choice of resource level to maximize the total surplus for its own district. The formulation in (6) presents outside district i’s decision problem:

$$
\begin{array}{c} \max _ {g _ {i}} S _ {i} (j) = \max _ {g _ {i}} \Bigg \{[ 1 - \kappa ] g _ {i} \\ + \kappa \beta \left[ \sum_ {l = 1} ^ {j} g _ {l} (j) + \sum_ {l = j + 1} ^ {n} g _ {l} - g _ {i} \right] - p g _ {i} ^ {2} \Bigg \}, \\ \ni 0 \leq g _ {i} \leq \overline {{g}}. \end{array}\tag{6}
$$

The optimization in (6) is solved for each district outside the coalition, $i = j + 1 , \dotsc , n .$ . Solving the individual district’s maximization problem for districts outside the coalition, where subscript out denotes a district outside the coalition, thus out $\in \bar { \{ j + 1 , \ldots , n \} }$ , the optimal resource level is

$$
g _ {j + 1} ^ {*} = \dots = g _ {n} ^ {*} = g _ {o u t} = \frac {1 - \kappa}{2 p},\tag{7}
$$

where the optimal resource level for an outside district does not depend on the coalition size. Although an outside district’s optimal resource level, $g _ { o u t } ,$ does not depend on the coalition size, an outside district’s surplus, $S _ { o u t } ( j )$ , does. This can be seen by restating the

optimization in (6),

$$
\begin{array}{c} \max _ {g _ {o u t}} S _ {o u t} (j) = \max _ {g _ {o u t}} \{[ 1 - \kappa ] g _ {o u t} + \kappa \beta [ j g _ {i n} (j) \\ \qquad + [ n - j - 1 ] g _ {o u t} ] - p g _ {o u t} ^ {2} \}, \ni 0 \leq g _ {o u t} \leq \overline {{g}}, \end{array}
$$

where $g _ { i n } ( j )$ depends on j from (4). Thus, there is an indi rect effect of coalition size on $S _ { o u t } ( j )$ through $g _ { i n } ( j )$

Based on the given analysis, the optimal resource levels for all inside districts are the same, that is, $g _ { i n }$ , and the optimal resource levels for all outside districts are the same, that is, $g _ { o u t } .$ Consequently, all outside districts have the same surplus, as given by

$$
\begin{array}{r l} & S _ {o u t} (j) = \frac {1}{4 p \alpha} [ 2 \beta \kappa [ 1 + [ j - 2 ] \kappa ] \\ & \qquad + \alpha [ 1 - \kappa ] [ 1 - \kappa + 2 \beta \kappa [ n - j - 1 ] ] ]. \end{array}\tag{8}
$$

Equation (8) shows that the surplus for an outside district does depend on the coalition size because the out side district surplus includes a spillover from districts inside the coalition, although with an interoperability efficiency loss.

For the special case of singleton, where no coalition is formed, the surplus for each district is the same:

$$
S _ {s i n g l e} = \frac {[ 1 - \kappa ] [ \kappa [ 2 \beta [ n - 1 ] - 1 ] + 1 ]}{4 p}.\tag{9}
$$

## 4.3. Optimal Resource Levels and Coalition Size

Our first proposition shows how optimal district resource levels change as the coalition size changes and how the resource levels for inside districts compare with those of outside districts. Proofs of all propositions, lemmas, and corollaries are relegated to Online Appendix A.

Proposition 1 (Properties of Optimal Resource Levels). Optimal resource levels have the following properties:

(a) Inside districts’ resource level $g _ { i n } ( j )$ decreases in the coalition size j;

(b) Outside districts’ resource level $g _ { o u t }$ is independent of the coalition size j;

(c) There exists a threshold coalition size, $\begin{array} { r } { \check { j } \equiv \frac { 1 - 2 \kappa } { \alpha - \kappa [ 1 + \alpha ] } , } \end{array}$ defined by $g _ { i n } ( \check { j } ) = g _ { o u t }$ . If the coalition size is smaller than the threshold $j \leq \check { j }$ , then inside districts’ resource levels are higher than those of outside districts $g _ { i n } ( j ) \geq g _ { o u t } ;$ otherwise, outside districts’ resource levels are higher $g _ { i n } ( j ) < g _ { o u t }$

In Proposition 1(a), the optimal resource level provided by each inside district decreases as the size of the coalition increases. This is because resources are fully interoperable within the coalition and it is more expensive to integrate resources together as the coalition size grows because of diseconomies of scope (Assumption 2(b)).

This can be seen directly from the derivative of (4) in the proof and the effect results from the last term in (3) being squared.

Furthermore, in Proposition 1(b), the optimal resource level for an outside district is independent of the coalition size j because, for a district outside the coalition, its choice of resource level, $g _ { i } , i > j ,$ is additively separable in (6) from all the other districts’ resource levels. Finally, Proposition 1(c) follows directly from the definition of the threshold coalition size that results from equating resource levels of inside and outside districts, together with Proposition 1(a).

Corollary 1. The threshold coalition size, ${ \check { j } } ,$ from Proposition 1(c) decreases in α and increases in κ.

In Corollary 1, as the economy of scale decreases (α increases), the cost of resources for inside districts increases and $g _ { i n }$ decreases. $\operatorname { A s } g _ { i n }$ also decreases with coalition size from Proposition 1(a), the threshold coalition size decreases, and there is a smaller range of coalition sizes where optimal resource level of inside districts is greater than those of outside districts. In contrast, a greater spillover increases optimal resource levels of inside districts and decreases those of outside districts, thereby increasing the threshold coalition size and increasing the range of coalition sizes where optimal resource levels of inside districts are greater than those of outside districts.

Corollary 2. The benefit for each inside district, $B _ { i n } ( j ) .$ , and the surplus $f o r$ each outside district, $S _ { o u t } ( j )$ , decrease in α and increase in $\beta .$

Similar to Corollary 1, in Corollary 2, as the coalition economy of scale decreases (α increases), the cost of resources for inside districts increases, and $g _ { i n }$ decreases. This directly reduces the benefit for inside districts and indirectly reduces the benefit and, hence, the surplus of outside districts through the reduced spillover from inside districts. An increase in relative interoperability (an increase in $\beta )$ increases the spillover benefit for all districts. In this way, the inside and outside districts are connected.

In our examples, benefits to member states (HIOs) that participate and not both increase as the coalition economy of scale increases and as relative interoperability increases. The latter is because the ability of EU residents to travel across borders and access venues in the case of nonparticipants in the EUDCC program, and the ability to exchange health information with nonparticipating HIOs in the Direct Project, increase.

## 5. Equilibrium Analysis Under Equal Cost Sharing

With homogeneous districts in the coalition, we use equal cost sharing for the cost of the coalition resources. The surplus for each district inside the coalition is

given by

$$
S _ {i n} (j) = B _ {i n} (j) - \frac {T C (j)}{j},
$$

where the total cost of coalition $T C ( j )$ is defined in (2).

The grand coalition is an equilibrium, where all districts are inside the coalition with $j _ { e q m } ^ { * } = n ,$ , if and only if

$$
S _ {i n} (j = n) \geq S _ {o u t} (j = n - 1),\tag{10}
$$

where, given our noncooperative solution concept, we only need to consider when only one district can change.

$\mathrm { A }$ partial coalition with size $j _ { e q m } ^ { * } \in \{ 3 , \ldots , n - 1 \}$ is an equilibrium if and only if

$$
S _ {i n} (j = j _ {e q m} ^ {*}) \geq S _ {o u t} (j = j _ {e q m} ^ {*} - 1), \mathrm{and}\tag{11}
$$

$$
S _ {o u t} (j = j _ {e q m} ^ {*}) \geq S _ {i n} (j = j _ {e q m} ^ {*} + 1).\tag{12}
$$

The condition in (11) ensures that given other districts coalition participation choices, a district inside the coalition does not have any incentive to deviate and leave the coalition. The condition in (12) ensures that given other districts’ coalition participation choices, a district outside the coalition does not have any incentive to deviate and participate in the coalition. Thus, (11) and (12) are effectively incentive compatibility (IC) conditions for inside districts and outside districts, respectively.

The minimal coalition is an equilibrium with only two districts inside the coalition, $j _ { e q m } ^ { * } = 2$ , if and only if

$$
S _ {i n} (j = 2) \geq S _ {s i n g l e}, \mathrm{and}
$$

$$
S _ {o u t} (j = 2) \geq S _ {i n} (j = 3).\tag{13}
$$

(14)

The conditions in (13) and (14) play the same role for the minimal coalition as (11) and (12) do for the partial coalition. They are also effectively IC conditions for the inside districts and outside districts, respectively.

Singleton is an equilibrium if and only if

$$
S _ {s i n g l e} \geq S _ {i n} (j = 2),\tag{15}
$$

where this is an IC condition for each district.

Note that obtaining the equilibrium for the partial coalition and the minimal coalition involves solving two conditions simultaneously, that is, conditions in (11) and (12) for the partial coalition and conditions in (13) and (14) for the minimal coalition. This results in a solution for the equilibrium coalition size $j _ { e q m } ^ { * } \in \{ 2 , \ldots , n - 1 \}$ that we provide in Online Appendix A.

We use our coalition economy of scale parameter, $\alpha ,$ to determine transitions between our different coalition structures based on coalition size. Setting inequalities in (15) and (11) to equalities and solving for α in each equal ity yields equilibrium thresholds $\alpha _ { e q m 1 } ( \beta )$ and $\alpha _ { e q m 3 } ( \beta )$ , respectively. Setting inequality in (12) when $j _ { e q m } ^ { * } = 2$ to equality and solving for α yields equilibrium threshold $\alpha _ { e q m 2 } ( \beta )$ . These equilibrium thresholds are effectively solutions for our coalition economy of scale parameter, $\alpha ,$ in terms of our relative interoperability parameter, $\beta \colon$

$$
\alpha_ {e q m 1} (\beta) = \frac {1}{2 - 4 \kappa + 4 \beta \kappa + 2 \kappa^ {2} - 4 \beta \kappa^ {2}},
$$

$$
\alpha_ {e q m 2} (\beta) = \frac {1 + \kappa [ 2 - 6 \beta + \kappa ]}{3 [ 1 - \kappa ] ^ {2}}, \mathrm{and}
$$

$$
\alpha_ {e q m 3} (\beta) = \frac {[ 1 + [ n - 2 ] \kappa ] ^ {2} - 2 n \beta \kappa [ 1 + [ n - 3 ] \kappa ]}{n [ 1 - \kappa ] ^ {2}}.
$$

The following lemma shows that these equilibrium thresholds are strictly ordered.

Lemma 1. The equilibrium thresholds are strictly ordered as follows: $\alpha _ { e q m 3 } ( \beta ) < \alpha _ { e q m 2 } ( \beta ) < \alpha _ { e q m 1 } ( \beta )$

The following proposition outlines the possible equilibrium coalition structures.

Proposition 2 (Equilibrium Coalition Structures). All four coalition structures are possible equilibrium:

(a) When $\alpha < \alpha _ { e q m 3 } ( \beta )$ , the equilibrium is the grand coalition with $j _ { e q m } ^ { * } = n ;$

(b) When $\alpha _ { e q m 3 } ( \beta ) < \alpha < \alpha _ { e q m 2 } ( \beta )$ , the equilibrium is $a$ partial coalition with $j _ { e q m } ^ { * } = \lfloor j _ { e q m } \} ;$

(c) When $\alpha _ { e q m 2 } ( \beta ) \dot { < } \alpha < \alpha _ { e q m 1 } ( \beta )$ , the equilibrium is the minimal coalition with $j _ { e q m } ^ { * } = 2 ;$

(d) When $\alpha > \alpha _ { e q m 1 } ( \beta ) .$ , the equilibrium is a singleton.

Here, $j _ { e q m }$ is a continuous approximation of the equilibrium coalition size in case of the partial coalition, which solves the first-order conditions for the surplus maximization problem. We note that the equilibrium results are unique—that is, multiple equilibria do not exist given a pair of α and $\beta .$ Details are available from the authors.

Figure 1. (Color online) Equilibrium Coalition Structures  
![](/api/attachments/W8RG62DT/fulltext/images/ba8572b05387027cc62a03f410d622a2b78d88ccf05fdda2f6fee47ff19ac1fc.jpg)  
Notes. This figure is based on parameter values of $n = 1 0$ and $\kappa = 0 . 3 5$ Figures based on other parameter values remain qualitatively the same.

Our results from Proposition 2 are displayed in Figure 1. They show different equilibrium coalition structures in different parameter regions based on our coalition economy of scale parameter, $\alpha ,$ and relative interoperability parameter, $\beta .$ . What this shows in an example like the Direct Project is that without supplemental incentives, any number of HIOs may participate, and many choose to not participate.

A greater coalition economy of scale (lower $\alpha )$ and lesser relative interoperability (lower $\beta )$ both favor larger-sized coalition structures, whereas diseconomies of scope (the square of the sum of total costs) favo smaller-size coalition structures. As α and $\beta$ become smaller, the impact of the coalition economy of scale and relative interoperability outweighs the impact of diseco nomies of scope; hence, a coalition structure with a greater number of districts is the equilibrium. This is illustrated in Figure 1: as α and $\beta$ move from the upper right corner to the lower left corner, the equilibrium coalition structure changes from no coalition (singleton) to minimal coalition to partial coalition and eventually to the grand coalition.

A closer examination on the properties of the equilibrium thresholds reveal that they all decrease in the relative interoperability, $\beta ,$ corresponding to the decreasing boundary lines in Figure 1. For example, considering that $\alpha _ { e q m 3 } ( \beta )$ decreases with $\beta ,$ moving from a point within the partial-coalition region to the right does not result in reaching the grand-coalition region. This is because increasing $\beta$ corresponds to the provision of additional spillover benefits to the outside districts, which essentially reduces their incentives to join the coalition. Therefore, to achieve the grand coalition, it is necessary to simultaneously reduce the resource costs faced by the coalition (lower α) as $\beta$ increases.

Next, we present how various parameters affect the equilibrium coalition size in the following proposition.

Proposition 3 (Properties of the Equilibrium Coalition Size). The equilibrium coalition size has the following properties:

(a) The equilibrium coalition size is increasing in the coalition economy of scale: the smaller is $\alpha ,$ , the larger $i s j _ { e q m } ^ { * } ,$

(b) The equilibrium coalition size is decreasing in relative interoperability: the smaller is $\beta ,$ the larger is $j _ { e q m } ^ { * } \rangle$

(c) The equilibrium coalition size is weakly increasing in the total number of districts, n.

In Proposition 3(a), an increase in the coalition economy of scale increases optimal resource levels for inside districts, increasing spillovers. As spillovers are higher for inside districts than for outside districts because of their full interoperability, more districts benefit from being in the coalition. In Proposition $3 ( \mathrm { b } )$ , a decrease in relative interoperability directly reduces the spillover benefits all districts can enjoy from other districts. This effect is stronger for the outside districts, as relative interoperability affects outside districts more than inside districts, leading to a larger coalition size. In Proposition $3 ( \mathrm { c } )$ , an increase in the total number of districts $( \mathrm { e . g . , }$ from n to $n + 1 )$ has no impact on the optimal resource levels for either inside or outside districts. The added district has the same impact on any existing district’s surplus regardless of whether the district is inside or outside the coalition. As a result, tradeoffs between participating in the coalition or not are the same for all districts. Therefore, the equilibrium coalition size remains unchanged for most cases. The only exception is when grand coalition is the equilibrium, and the resulting equilibrium coalition size increases from n to n + 1.

As many of the application specifications are open source in the EUDCC program and could easily be shared among adopting member states, for example, the wallet (holder) and verifier applications, there is a substantial coalition economy of scale favoring a larger coalition size whereby many, if not all, the member states participate. Similarly, the lower the relative interoperability from outside the EUDCC participants, the greater the payoffs from participating in the EUDCC program, allowing for unimpeded travel and trade.

## 6. Socially Optimal Coalition Structure

In this section, we derive the socially optimal coalition structure and examine properties of the socially optimal coalition size. Here, district participation is decided noncooperatively, and resource investment is decided cooperatively, where the social planner is an external party that can incentivize participation. In the context of the EUDCC program, the social planner is the European Commission that manages EU policies and promotes the EUDCC program to member states, and the socially optimal structure and size is the level of participation of member states. In the context of the Direct Project, the social planner is the HHS that advocates for potential members to participate in the Direct Project, and the socially optimal structure and size is analogous to the level of HIO participation that would be preferred by the HHS. Our social optimality is distinct from first best where the social planner could dictate coalition participation and resource investment for all districts. First best would require substantial information and enforcement capabilities that do not exist in our examples.

Substituting the optimal resource levels back into the surplus functions for all districts, we obtain the coalition welfare $C W ( j ) = S _ { 1 } ( j ) + \cdot \cdot \cdot + S _ { j } ( j ) = j S _ { i n } ( j )$ for all inside districts and $S _ { o u t } ( j )$ from (8) for each outside district. Specifically, for coalition welfare, we have

$$
\begin{array}{c} C W (j) = \frac {1}{4 p \alpha} [ 1 + 2 [ j - 2 + j [ n - j ] \alpha \beta ] \kappa \\ + [ [ j - 2 ] ^ {2} - 2 j [ n - j ] \alpha \beta ] \kappa^ {2} ]. \end{array}
$$

By adding the surpluses of all n districts together, we obtain the overall social welfare for the n districts:

$S W ( j ) = C W ( j ) + [ n - j ] S _ { o u t } ( j )$ if a coalition is formed or $S W _ { s i n g l e t o n } = n S _ { s i n g l e t o n }$ if no coalition is formed.

A social planner’s objective is to find the optimal coalition structure and size when that structure is a partial coalition such that the overall social welfare is maximized:

$$
\max \{S W _ {s i n g l e t o n}, S W (j) \},\tag{16}
$$

where $S W ( j ) = \{ C W ( j ) + [ n - j ] S _ { o u t } ( j ) \}$ for $j \in \{ 2 , \dots , n \}$

Using our Assumption 1 that defines the range of the parameter we use to model relative interoperability, $\textstyle { \bar { \frac { 1 } { 2 } } } < \beta < 1$ , social welfare, $S W ( j ) ,$ , is a concave quadratic function. Therefore, the necessary and sufficient conditions for the socially optimal coalition structure are as follows:

The grand coalition is socially optimal, that $\begin{array} { r } { \mathbf { i s } , j _ { s w } ^ { * } = n , } \end{array}$ if and only if

$$
S W (j = n) \geq S W (j = n - 1).\tag{17}
$$

A partial coalition is socially optimal, that is, $j _ { s w } ^ { \ast } \in \{ 3 , \dots ,$ $n - 1 \}$ , if and only if

$$
S W (j = j _ {s w} ^ {*}) \geq S W (j = j _ {s w} ^ {*} + 1), \text { and }\tag{18}
$$

$$
S W (j = j _ {s w} ^ {*}) \geq S W (j = j _ {s w} ^ {*} - 1).\tag{19}
$$

A minimal coalition is socially optimal, that is, $j _ { s w } ^ { * } = 2 ,$ , if and only if

$$
S W (j = 2) \geq S W (j = 3), \mathrm{and}\tag{20}
$$

$$
S W (j = 2) \geq S W _ {s i n g l e t o n}.\tag{21}
$$

A singleton is socially optimal if and only if

$$
S W _ {s i n g l e t o n} \geq S W (j = 2).\tag{22}
$$

Similar to the way we determined equilibrium thresh olds based on our coalition economy of scale parameter, $\alpha ,$ in the prior section where the thresholds represent transitions between coalition structures, we set Inequal ities (22), (20), and (17) to equalities and solve for $\alpha ,$ yielding three welfare thresholds $\alpha _ { s w 1 } ( \beta ) , \alpha _ { s w 2 } ( \beta )$ , and $\alpha _ { s w 3 } ( \beta )$ , respectively, as functions of our interoperability efficiency parameter, $\cdot \beta \colon$

$$
\alpha_ {s w 1} (\beta) = \frac {1 + 2 [ n - 2 ] \beta \kappa}{2 [ 1 - \kappa ] [ 1 + [ 2 [ n - 1 ] \beta - 1 ] \kappa ]},
$$

$$
\alpha_ {s w 2} (\beta) = \frac {\kappa [ 2 + \kappa + 2 \beta [ [ n - 3 ] \kappa - 1 ] ]}{[ 1 - \kappa ] [ 1 + [ 2 [ n - 1 ] \beta - 1 ] \kappa ]}, \mathrm{and}
$$

$$
\alpha_ {s w 3} (\beta) = \frac {\kappa [ [ 2 n - 5 ] \kappa - 2 \beta [ 1 + [ n - 3 ] \kappa ] + 2 ]}{[ 1 - \kappa ] [ 1 + [ 2 [ n - 1 ] \beta - 1 ] \kappa ]}.
$$

With the help of these three thresholds, we next present the socially optimal coalition structures. To begin, the following lemma shows that these welfare thresholds are strictly ordered.

Lemma 2. The welfare thresholds are strictly ordered as follows: $\alpha _ { s w 3 } ( \beta ) < \alpha _ { s w 2 } ( \beta ) < \alpha _ { s w 1 } ( \beta )$

We characterize the possible socially optimal coalition structures in the following proposition.

Proposition 4 (Socially Optimal Coalition Structure). There are four possible socially optimal coalition structures:

(a) When $\alpha < \alpha _ { s w 3 } ( \beta )$ , the grand coalition with size $j _ { s w } ^ { * } = n$ is the social optimum;

(b) When $\alpha _ { s w 3 } ( \beta ) < \alpha < \alpha _ { s w 2 } ( \beta )$ , a partial coalition with size $j _ { s w } ^ { * } = \lceil j _ { s w } \rceil o r \lfloor j _ { s w } \rfloor$ is the social optimum, depending on which yields a higher social welfare;

(c) When $\alpha _ { s w 2 } ( \beta ) < \alpha < \alpha _ { s w 1 } ( \beta )$ , the minimal coalition with size $j _ { s w } ^ { * } = 2$ is the social optimum;

(d) When $\alpha > \alpha _ { s w 1 } ( \beta )$ , a singleton is the social optimum.

Here, $j _ { s w } ^ { * }$ is a continuous approximation of the socially optimal coalition size, which solves the first-order condition of the social welfare maximization problem. Using results from Proposition $^ { 4 , }$ similar to Figure 1 with equilibrium coalition structures, Figure 2 shows different socially optimal coalition structures in differentparameter regions based on our coalition economy of scale parameter, $\alpha ,$ and relative interoperability parameter, β. As illustrated in Figure 2, the socially optimal coalition structure changes from no coalition (singleton) to minimal coalition to partial coalition and to the grand coalition when moving from the upper right corner to the lower left corner. This pattern is similar to the equilibrium coalition structure results because a greater coalition economy of scale (lower α) and lesser relative interoperability (lower $\beta )$ both favor larger-size coalition structures. However, as we show, the social planner prefers larger-size coalition structures in a larger-parameter region than do individual districts when deciding their equilibrium coalition structure $( \mathrm { e . g . }$ , the grand coalition region in Figure 2 is larger than that in Figure 1).

Figure 2. (Color online) Socially Optimal Coalition Structures  
![](/api/attachments/W8RG62DT/fulltext/images/e522cc552162c3b82974be834063158a1b529ba08c64311c83b242badca56467.jpg)  
Note. This figure is based on parameter values of n � 10 and $\kappa = 0 . 3 5 .$

Further examination of the properties of the social welfare thresholds reveal that they all decrease in the relative interoperability, $\beta ,$ corresponding to the decreasing boundary lines in Figure 2. This indicates that for an existing partial coalition, no matter how much extra spillover can be generated (larger $\beta )$ , a grand coalition is never possible to be socially optimal when the coalition resource costs remain the same. In practice, enhancing data integration and interoperability does not necessarily lead to the formation of a grand coalition; the cost associated with coalition formation, such as data privacy protection and maintenance, must also be taken into account.

Next, we present how various parameters affect the socially optimal coalition size.

Proposition 5 (Properties of the Socially Optimal Coalition Size). The socially optimal coalition size, $j _ { s w } ^ { * } ,$ has the following properties:

(a) The socially optimal coalition size is increasing in the coalition economy of scale: the smaller the $\alpha ,$ the larger is $j _ { s w } ^ { * } ,$

(b) The socially optimal coalition size is decreasing in relative interoperability: the smaller is $\beta ,$ the larger is $j _ { s w } ^ { * } ,$

(c) The socially optimal coalition size is weakly increasing in the number of districts, n.

The impacts of the coalition economy of scale and relative interoperability parameters on the socially optima coalition size (Proposition 5(a) and 5(b)) are similar to their impacts on the equilibrium coalition size (Proposition 3(a) and 3(b)). In Proposition 5(c), as the total num ber of districts increases from n to $n + 1 .$ , the existing separating lines for regions of different coalition sizes, $\{ 1 , 2 . . . , n \}$ , all shift upward, and a new separating line $( \mathrm { i } . \mathrm { e } . , n + 1 )$ is added below. As a result, for a given market condition (i.e., a given α and $\beta ) _ { \cdot }$ , the coalition size could remain unchanged or increase, depending on whether the coalition size region shifted.

Next, we compare the equilibrium coalition structures to the socially optimal coalition structures.

Figure 3 illustrates how the socially optimal coalition structure regions in Figure 2 differ from the equilibrium coalition structure regions in Figure 1. In Figure 3, the symbols $< , =$ , and > represent regions where the equi librium coalition structure is smaller than, the same as, or greater than the socially optimal coalition structure in size, respectively.

As shown in Figure 3, the equilibrium coalition structures are aligned with the social optimum in some regions but are at odds with the social optimum in other regions. Specifically, individual districts prefer smaller-size coalition structures than does the social planner under most combinations of α and $\beta .$ In Figure 3, there is only a small region where the equilibrium coalition structure is larger than the socially optimal coalition structure. It is also worth noting that in the partial-coalition region where the equilibrium and socially optimal coalition structures coincide, the coalitions under each regime may differ in size. That is, there is variation in size within the same structure. This is because the partial-coalition region is defined as when $j _ { e q m } ^ { * } \in \{ 2 , \ldots , n - 1 \}$ for the equilibrium coalition and $j _ { s w } ^ { * } \in \{ 2 , \ldots , n - 1 \}$ for the socially optimal coalition.

Figure 3. (Color online) Deviation of Equilibrium Coalition Structures from Socially Optimal Coalition Structures  
![](/api/attachments/W8RG62DT/fulltext/images/9a00020717934bedf2a50a13b9af409f4c1063a407c16b0ba91d83a107f4640c.jpg)  
Note. This figure is based on parameter values of $n = 1 0$ and $\kappa = 0 . 3 5 .$

As applied to our Direct Project example, the deviation shown in Figure 3 demonstrates the differences in levels of participation in the Direct Project—which involves resource levels determined by the ONC for those HIOs that choose to participate—between levels of participation that would be chosen by the HIOs individually and those that HHS would prefer.

## 7. Incentives to Induce the Socially Optimal Coalition

In this section, we design an incentive mechanism to induce the socially optimal coalition structure and, in the case of a partial coalition, to induce the socially optimal coalition size. Here, we solely focus on offering incentives (subsidy or tax) to participating districts and not consider penalties for nonparticipating districts.<sup>10</sup> In our EUDCC example, this involves the EU Commission providing incentives to participating member states to motivate the socially optimal level of member state participation in the EUDCC program. The EU Commission cannot impose penalties on member states that choose not to participate in the EUDCC program.

## 7.1. Incentive Mechanism Design

In this subsection, we model a social planner who provide incentives to districts for coalition participation. To our two-stage setup, we add a stage 0 where a social planner decides the incentive for districts inside the coalition to maximize social welfare. Stage 1 and stage 2 remain the same as in our equilibrium model wherein stage 1 districts decide whether to participate in the coalition, and in stage 2, the coalition coordinator decides participating districts’ resource levels.

In stage 0, the social planner announces an incentive, $\phi _ { j } \in R ( \mathrm { i . e . , } \phi _ { j }$ can be a subsidy or tax), given to each district inside the coalition when the size of the coalition is $j \in \{ 2 , \ldots , n \}$

Providing incentives to districts within a coalition often incurs an opportunity cost for the social planner where the necessary funds must be obtained through interest-bearing loans or the diversion of resources from alternative government initiatives. We capture this cost as a fraction of the incentive, denoted by $\gamma .$ Consequently, the social planner’s objective is to maximize the total surplus across all districts, taking into account the incentives received by the districts within the coalition, while also factoring in the cost of providing such incentives.

$$
\max _ {j} \{S W (j) = C W (j) + [ n - j ] S _ {o u t} (j) - [ 1 + \gamma ] j \phi_ {j} \}
$$

As a result, for each inside district, the total surplus is

$$
S _ {i n} (j) = B _ {i n} (j) - \frac {T C (j)}{j} + \phi_ {j}.
$$

The total surplus for the outside districts, $S _ { o u t } ( j )$ , remains the same as in the analysis of optimal resource levels.

As before, in stage 1, each district chooses whether to participate in the coalition based on its surplus, $S _ { i n } ( j )$

and $S _ { o u t } ( j )$ . In stage 2, each outside district chooses its own resource level to maximize its surplus, $S _ { o u t } ( j )$ Simultaneously, the coalition coordinator chooses the resource level for each inside district to maximize coalition welfare, $C W ( j ) = j S _ { i n } ( j ) = j B _ { i n } ( j ) - T C ( j ) + j \phi$ . Because the incentive $\phi _ { j }$ is both fixed and additive to the inside district surplus, it does not affect the choice of resource level for an individual district, and therefore, the optimal resource levels for inside and outside districts are the same as in the optimal district resource analysis in Section 4.

The socially optimal grand coalition $( \mathrm { i . e . , } j _ { s w } ^ { \ast } = n )$ is an equilibrium if and only if

$$
S _ {i n} (j = n) \geq S _ {o u t} (j = n - 1).\tag{23}
$$

The socially optimal partial coalition $( \mathrm { i . e . , ~ } j _ { s w } ^ { \ast } \in \{ 3 , \dots ,$ $n - 1 \}$ is an equilibrium if and only if

$$
S _ {i n} (j = j _ {s w} ^ {*}) \geq S _ {o u t} (j = j _ {s w} ^ {*} - 1), \mathrm{and}\tag{24}
$$

$$
S _ {o u t} (j = j _ {s w} ^ {*}) \geq S _ {i n} (j = j _ {s w} ^ {*} + 1).\tag{25}
$$

The socially optimal minimal coalition $( \mathrm { i } . \mathrm { e } . , j _ { s w } ^ { \ast } = 2 )$ is an equilibrium if and only if

$$
S _ {i n} (j = 2) \geq S _ {s i n g l e t o n}, \mathrm{and}\tag{26}
$$

$$
S _ {o u t} (j = 2) \geq S _ {i n} (j = 3).\tag{27}
$$

The socially optimal singleton is an equilibrium if and only if

$$
S _ {s i n g l e t o n} \geq S _ {i n} (j = 2).\tag{28}
$$

Conditions (23) through (28) are analogous to those in (10) through (15) when determining the equilibrium coalition size.

We again use our coalition economy of scale parameter, α, to determine thresholds for transitions between coalition structures. Employing the subscript im on α to denote thresholds for our incentive mechanism, setting Inequality (28) to equality yields threshold

$$
\alpha_ {i m 1} (\beta , \phi_ {2}) = \frac {1}{2 \kappa [ 2 \beta [ 1 - \kappa ] + \kappa - 2 ] - 8 p \phi_ {2} + 2}.
$$

Setting Inequalities (25) or Inequality (27) to equality for $j _ { s w } ^ { * } = j \bar { \in } \{ 3 , \bar { \mathbf { \Omega } } . . . , n \}$ yield a group of thresholds:

$$
\begin{array}{l} \alpha_ {i m \{j - 1 \}} (\beta , \phi_ {j}) \\ = \frac {j \kappa [ - 2 \beta [ [ j - 3 ] \kappa + 1 ] + [ j - 4 ] \kappa + 2 ] - 4 [ 1 - \kappa ] \kappa + 1}{j [ [ 1 - \kappa ] ^ {2} - 4 p \phi_ {j} ]}. \end{array}
$$

The thresholds $\alpha _ { i m 1 } ( \beta , \phi _ { 2 } )$ and $\alpha _ { i m \{ j - 1 \} } ( \beta , \phi _ { j } )$ represent solutions for our coalition economy of scale as IC conditions for the equilibrium coalition size being the socially optimal coalition size as a function of our model parameters and our socially optimal incentive.

Setting Inequality (18) or Inequality (17) to equality from Section 6 when $j _ { s w } ^ { * } = j \in \{ 3 , \bar { \ldots } , n \}$ yields the threshold IC condition for the socially optimal coalition being the partial or grand coalitions:

$$
\alpha_ {s w \{j - 1 \}} (\beta) = \frac {\kappa [ 2 [ 1 - \beta ] + \kappa [ 2 \beta [ n + 5 ] - 2 [ 2 \beta - 1 ] j - 7 ] ]}{[ 1 - \kappa ] [ \kappa [ 2 \beta [ n - 1 ] - 1 ] + 1 ]}.
$$

Using these thresholds as IC conditions, we derive a suf ficient incentive mechanism to ensure that the socially optimal coalition size is the equilibrium as a function of our model parameters. Denoting the incentive for a coalition of size j as $\phi _ { j } ,$ we solve for $\phi _ { j }$ in the case where we have the minimal coalition $( \phi _ { 2 } )$ and where we have a partial coalition by equating the corresponding IC conditions for the equilibrium and socially optimal coalition structures:

$$
\begin{array}{r} \alpha_ {i m 1} (\beta , \phi_ {2}) = \alpha_ {s w 1} (\beta , \phi_ {2}) \Rightarrow \phi_ {2} (\beta , n, \kappa , \gamma) \\ = \frac {\beta [ 2 \beta - 1 ] [ 1 - \kappa ] \kappa^ {2} [ n - 2 ]}{2 p [ 1 + \gamma + 2 \beta \kappa [ n - 2 ] ]}, \end{array}
$$

where $\alpha _ { s w 1 } ( \beta , \phi _ { 2 } )$ is defined by $S W _ { s i n g l e t o n } = S W ( j = 2 )$ Other incentives, $\boldsymbol { \phi } _ { j } ,$ for $j \in \{ 3 , \ldots , n \}$ are defined recursively as follows:

$$
\begin{array}{c} \alpha_ {i m \{j - 1 \}} (\beta , \phi_ {j}) = \alpha_ {s w \{j - 1 \}} (\beta , \phi_ {j - 1}, \phi_ {j}) \text {for} j \in \{3, \ldots , n \} \\ \Rightarrow \phi_ {j} (\beta , n, \kappa , \gamma) = F _ {1} (\beta , n, \kappa , \gamma) * \phi_ {j - 1} + F _ {2} (\beta , n, \kappa , \gamma) \\ \text {for} j \in \{3, \ldots , n \} \end{array}
$$

The expressions for functions $F _ { 1 } ( \beta , n , \kappa , \gamma )$ and $F _ { 2 } ( \beta , n , \kappa , \gamma )$ can be found in Online Appendix A.

Note that the socially optimal incentives, $\phi _ { 2 } ( \beta , n , \kappa , \gamma )$ and $\phi _ { j } ( \beta , n , \kappa , \gamma )$ , are functions of our parameters of interest: relative interoperability, $\beta ;$ number of districts, n; degree of spillover, κ; and the opportunity cost, $\gamma .$ . We shorten the socially optimal incentives as $\phi _ { 2 } ( \cdot )$ and $\phi _ { j } ( \cdot )$ for the remainder of our analyses.

## 7.2. Socially Optimal Incentives When the Opportunity Cost Is Negligible

Because of the intricate nature of the socially optimal incentive mechanism design in a multidistrict system and the additional layer of complexity introduced by the presence of opportunity cost, it is infeasible to obtain closedform explicit analytical solutions. Consequently, we begin our analytical investigation by focusing on the spe cial case where opportunity cost is negligible (i.e., when $\gamma = 0 )$ ). This allows us to gain insights under simplified conditions. To gain a more comprehensive understanding, in the next subsection, we employ numerical analysis to explore the properties of the optimal incentives when the opportunity cost is not zero.

In the following proposition, we investigate the properties of the socially optimal incentives when the opportunity cost is negligible.

Proposition 6 (Socially Optimal Incentives When Opportunity Cost Is Negligible). When opportunity cost $\gamma = 0 ,$ the optimal incentives for the socially optimal coalitions have the following properties:

(a) Inside districts in the minimal coalition are subsidized, that is, $\phi _ { 2 } ( \cdot ) > 0$

(b) If relative interoperability is high and there are a large number of districts, then inside districts in a partial or grand coalition are subsidized, that is, $\begin{array} { r } { i f \beta \geq \frac { 4 \kappa ^ { 2 } - \kappa + 1 } { 6 \kappa } } \end{array}$ and $n \geq { \hat { n } } ( \beta )$ then $\phi _ { i } ( \cdot ) \geq 0 f o r j \in \{ 3 , \ldots , n \}$

(c) If relative interoperability is low, or if relative interoperability is high and there are a smaller number of districts, then inside districts in a small partial coalition are taxed, and inside districts in a large partial or grand coalition are subsidized; that is, if $\beta < \frac { 4 \kappa ^ { \sum } - \kappa + 1 } { 6 \kappa }$ , or if $\beta > \frac { 4 \kappa ^ { 2 } - \kappa + 1 } { 6 \kappa }$ and $n < { \hat { n } } ( \beta )$ , then $\phi _ { i } ( \cdot ) < 0 f o r j \in \{ 3 , \ldots , \hat { j } \}$ and $\phi _ { i } ( \cdot ) > 0 f o r j \in \{ \hat { j } , \ldots , n \}$

The expressions for thresholds nˆ(β) and <sup>ˆ</sup>j can be found in Online Appendix A.

From Proposition 6, both the incentive and the relative interoperability are coalition size specific. The proposition given here is directly related to Figure 4, whereby the sign of $\phi _ { j } ( \cdot )$ indicates whether the equilibrium coalition size is smaller or larger than the socially optimal coalition size. If $\phi _ { j } ( \cdot ) > 0$ , then districts receive a subsidy to participate the coalition, and if $\phi _ { i } ( \cdot ) < 0$ , then districts in the coalition are taxed. Referring back to Figure 3, the regions where the equilibrium coalition structure is smaller than the socially optimal coalition structure call for a subsidy and vice versa where the relative coalition structure sizes are reversed. However, there are situations when the partial-coalition structure is both the equilibrium and socially optimal form where the coalition sizes are different, and in these cases, a nonzero incentive is needed to align the equilibrium coalition size with the socially optimal one. Although our incentive is sufficient to align the equilibrium coalition size with the socially optimal coalition size under all our parameter ranges, it is not necessary when the equilibrium and socially optimal coalition sizes are the same; rather, it is only necessary and sufficient when they are different.

Figure 4. Socially Optimal Incentives When Opportunity Cost Is Negligible  
![](/api/attachments/W8RG62DT/fulltext/images/f9df22f451f03f1150bafa2e9e9a10fc9abb2ba47d3cade37d85a370f66aa203.jpg)  
Note. This figure is based on parameter value of $\kappa = 0 . 3 5 .$

## 7.3. Socially Optimal Incentives in the Presence of Opportunity Cost

In this subsection, we investigate the properties of socially optimal incentives in the presence of opportunity cost $( \mathrm { i . e . } ,$ when $\gamma > 0 )$ . As discussed in Section 7.1, socially optimal incentives to inside districts are recursive solutions. In the base case, the incentive to inside districts in a minimal coalition, $\phi _ { 2 } ,$ has an explicit solution, and we derive analytical results for its properties. However, for other incentives beyond the minimum coalition $\phi _ { i } , j \in \{ 3 , \ldots , n \}$ , we must rely on numerical analysis to investigate their properties because of the interdependencies among the socially optimal incentives. In the following, we present the analytical results concerning the properties of $\phi _ { 2 }$ and the numerical observations concerning the properties of $\phi _ { 3 }$ when opportunity cost is nonnegligible.

Observation 1 (Socially Optimal Incentives in the Presence of Opportunity Cost). (Properties of $\phi _ { 2 }$ and $\phi _ { 3 } )$ When opportunity cost is nonnegligible, the socially opti mal incentives $\phi _ { 2 }$ and $\phi _ { 3 }$ have the following properties:

(a) The socially optimal incentive $\phi _ { 2 }$ always takes the form of a subsidy, that is, $\phi _ { 2 } > 0 ;$ the socially optimal subsidy $\phi _ { 2 }$ decreases in opportunity cost γ.

(b) The socially optimal incentive $\phi _ { 3 }$ can take the form of either a subsidy or tax; that is, $\phi _ { 3 } > 0$ if $\beta$ exceeds a threshold and $\phi _ { 3 } < 0$ otherwise; the socially optimal subsidy $\phi _ { 3 }$ decreases in opportunity cost $\gamma ;$ the socially optimal tax $| \phi _ { 3 } |$ also decreases in opportunity cost γ.

We find that the structure of the optimal policy (subsidy or tax) for the social planner in the presence of opportunity cost is similar to that in the absence of opportunity cost (as summarized in Proposition 6). Spe cifically, inside districts for the minimal coalition should always be subsidized. Beyond the minimal coalition, as depicted in Figure 5, if $\beta$ exceeds a certain threshold, the optimal policy for the social planner is to provide a sub sidy to districts within the coalition, whereas if $\beta$ is below this threshold, the optimal policy is to impose a tax on the districts within the coalition. Furthermore, we find that the socially optimal incentives, whether in the form of subsidies or taxes, decrease as the opportunity cost, γ, increases. As the opportunity cost, γ, increases, the social planner should reduce the amount of the provided incentives (either subsidy or tax) because of the reduced efficiency of this policy instrument.

## 7.4. Discussion about the Implementation of Socially Optimal Incentive

Our socially optimal incentive is not designed to achieve budget balance. Achieving budget balance is not a critical objective when the social planner faces substantial natural disasters or pandemics such as COVID-19. Allowing cross-member-state travel and trade while maintaining population health is a primary objective of the EU Commission, and the EUDCC program is essential in achieving it. In the United States, health information exchange between HIOs has proven critical in treatment of ICU patients and in the distribution of vaccines, illustrating the importance of the Direct Project. However, when the socially optimal incentive $\phi _ { j } ( \cdot )$ is effectively a tax, $\phi _ { j } ( \cdot ) < 0$ , then overall social welfare is improved by the incentive both through achieving the socially optimal coalition structure/size and through the proceeds from the tax. When the incentive is a subsidy, the social planner has to weigh the gain in coalition welfare, CW, with the aggregate cost of the subsidy, $\phi _ { j } ( \cdot ) > 0$ . In both the EUDCC program and the Direct Project, the social planner (EU Commission and HHS, respectively) has made substantial investments of public funds.

Figure 5. Socially Optimal Incentive $\phi _ { 3 }$ in the Presence of Opportunity Cost  
![](/api/attachments/W8RG62DT/fulltext/images/64cccee8e94dc0cbc99112e98675ad5f51ab9aadb7b0d5a6c12540ba443e0dff.jpg)  
Note. This figure is based on parameter values of n � 10 and $\gamma = 1 0 \%$

Reviewing the timing of implementation of our socially optimal incentive, the stages unfold as follows:

Stage 0: The social planner announces the incentives $\phi _ { 2 }$ and $\boldsymbol { \phi } _ { j }$ where $j \in \{ 3 , \ldots , n \}$ , based on all parameters other than the economy of scale parameter, α.

Stage 1: In response to the announced incentives, individual districts choose whether to participate in the coalition noncooperatively based on all parameters, including the coalition economy of scale parameter, $\alpha .$ The resulting equilibrium coalition size is socially optimal.

Stage 2: The coalition coordinator chooses optimal resource levels cooperatively for inside districts and outside districts choose their own optimal resource levels. The resources levels are not directly affected by the additive incentive but are indirectly affected by changes in the coalition structure or size.

## 8. Conclusions

We study a relatively general setting with districts choosing whether to participate in a critical IT infrastructure coalition noncooperatively where decisions about resource levels within the coalition are made cooperatively and centrally. In our setting, there are resource spillovers between districts, there is lesser interoperability for districts outside the coalition, and there are different economies of scale and scope inside the coalition. As two illustrative examples, we use the EUDCC program, an EU initiative to implement digital COVID certificates $( \mathrm { e . g . }$ , vaccine passports) to support movement across member states, and we use the Direct Project, a U.S. HHS initiative to make information exchange across HIOs fully interoperable.

Even with homogeneous districts, we find that, in addition to no coalition or the grand coalition, a minimal, or partial, coalition can be the equilibrium coalition structure. Similarly, all four coalition structures can be socially optimal. Although there are cases where the equilibrium coalition structure and even size correspond to the social optimum, there are other cases where they do not correspond. In these cases, it is most likely that the socially optimal coalition is larger, and we present a straightforward incentive mechanism that aligns the equilibrium and socially optimal coalition structure and size.

We also find that benefits for inside districts and the surplus for outside districts are higher with a greater coalition economy of scale and with higher relative interoperability of resources from outside districts. However, the coalition size in equilibrium and at the social optimal is larger with a greater coalition economy of scale and smaller with higher relative interoperability of resources from outside districts.

Our results are important reminders to policy makers that critical IT infrastructure programs such as the Direct Project should not expect that all potential participants will choose to participate and, more significantly, that it may not be socially optimal for all potential participants to participate—that is, the grand coalition may not be socially optimal. Interestingly, in the EUDCC program, not only did all 27 member states participate in the program but equivalence was accepted in 40 non-EU nations, including most European Economic Area countries and others (e.g., Iceland) that directly participated in the EUDCC program. Thus, although the EUDCC program was designed for and targeted toward the participation of member states, there was additional social benefit from the program.

Our modeling approach has some limitations common to most analytical models. We chose specific functional forms for our benefits and surplus functions where our key parameters such as spillovers, relative interoperability, and coalition economy of scale enter linearly and our aggregation is additive. Our results are likely to generalize to a wide variety of settings and mathematical forms, but technically, we only establish our results for those forms. A feature of our main mode that can be considered a limitation is homogeneous districts, and through our extension, we find that with limited heterogeneity, such as districts with two different levels of resource costs, our equilibrium results and transitions between coalition structures as our underlying parameters change are qualitatively the same—hence, we believe most of our results would hold with heterogeneous districts. For example, in a franchise network with positive participation and investment externalities (i.e., spillovers), Nault and Dexter (1994) found that universal participation across heterogeneous territories (i.e., districts) was not necessarily profit maximizing for a franchisor or franchisees because greater participation diluted the investment incentive.

In our model, the coalition coordinator chooses and enforces investments for inside districts maximizing coalition welfare. When there is no coalition coordinator, the coalition needs a mechanism that fills these functions. The coalition could contract to an external party giving them decision and enforcement rights—in our examples, the social planner (EU Commission and HHS) allocates these rights to their chosen coalition coordinator (eHealth network and ONC, respectively). Alternatively, the coalition could act as a decentralized autonomous organization (DAO) using algorithms to determine inside district investment and smart contracts to enforce investments, and communication between districts would be necessary to achieve this. The coalition in our model is in part a form of DAO that is characterized by a finite number of potentially autonomous units, and the decentralized autonomy extends to deciding whether to join the coalition. In our examples (EUDCC program and the Direct Project), we found that some elements of resource investment implementation are decentralized, and some of the underlying standards are centralized—consistent with a DAO. However, given our model is directed toward public policy, it differs from DAOs in that levels of resource investment are determined cooperatively and centrally rather than being decentralized.

Generically, our study examines benefits of interoperability and spillovers in a positive-spillover setting with multiple (more than two) districts where a coalition coordinator dictates investment and benefits are shared through spillovers. In addition to treating the coalition as a DAO as discussed, future research opportunities include developing mechanisms for multiple districts to directly share benefits through transfers or through cooperative game solutions that incorporate the critical feature of interoperability as well as incorporating decentralized investment decisions in coalition formation.

## Acknowledgments

The authors thank the colloquium participants at the University of Calgary for helpful comments. The authors also thank Jeanette Burman for excellent editing and a detailed report on different COVID-19 vaccine passport programs, one of which is used as an example in this work. This research was supported by the Social Science and Humanities Research Council (SSHRC) of Canada.

## Endnotes

<sup>1</sup> The European Commission is the executive of the European Union responsible for initiating and enforcing EU laws and managing EU policies.

<sup>2</sup> See https://health.ec.europa.eu/system/files/2022-02/digital-covidcertificates\_v1\_en.pdf

<sup>3</sup> See https://health.ec.europa.eu/system/files/2022-07/digital-covidcertificates\_v2\_en.pdf

<sup>4</sup> See https://health.ec.europa.eu/system/files/2022-02/digital-covidcertificates\_v3\_en\_0.pdf.

<sup>5</sup> See https://health.ec.europa.eu/system/files/2022-07/digital-covidcertificates\_v4\_en.pdf.

<sup>6</sup> See https://health.ec.europa.eu/system/files/2022-03/digital-covidcertificate\_v5\_en.pdf.

<sup>7</sup> See https://health.ec.europa.eu/system/files/2022-02/eu-dcc\_validationrules\_en.pdf.

<sup>8</sup> The Direct Project is an example of critical IT infrastructure in the U.S. Healthcare and Public Health sector, one of 16 sectors defined as critical infrastructure sectors. As the U.S. Government Cybersecurity & Infrastructure Security Agency states, “ … Because th vast majority of the sector’s assets are privately owned and operated, collaboration and information sharing between the public and private sectors is essential to increasing resilience of the nation’s Healthcare and Public Health critical infrastructure” (Cybersecurity and Infrastructure Security Agency 2021b).

<sup>9</sup> As we describe in the conclusion, non-EU European Economic Area countries also participated to some extent.

<sup>10</sup> In our setting, there are several reasons for not considering a penalty to outside districts. First, the social planer may lack the jurisdic tional authority to enforce a penalty on nonparticipating districts. Second, the contracts/agreements that are agreed to by participating districts are less restrictive, less invasive, and more easily enforceable compared with those imposed on nonparticipating districts. Third, aversive incentive solutions such as penalties are typi cally met with resistance from the districts’ perspective and thus are deemed undesirable from the social planner’s perspective.

## References

Broadbent M, Weill P, Clair D (1999) The implications of information technology infrastructure for business process redesign. Management Inform. Systems Quart. 23(2):159–182.

Carraro C (2003) The Endogenous Formation of Economic Coalitions (Edward Elgar, Cheltenham, UK).

Cheng HK, Bandyopadhyay S, Guo H (2011) The debate on net neutrality: A policy perspective. Inform. Systems Res. 22(1):60–82.

Cheng ZA, Pang MS, Pavlou PA (2020) Mitigating traffic congestion: The role of intelligent transportation systems. Inform. Systems Res. 31(3):653–674.

Cybersecurity and Infrastructure Security Agency (2021a) About CISA: Critical infrastructure sectors. Accessed June 1, 2021, https://www.cisa.gov/critical-infrastructure-sectors.

Cybersecurity and Infrastructure Security Agency (2021b) About CISA: Healthcare and public health sector. Accessed June 1, 2021, https://www.cisa.gov/healthcare-and-public-health-sector.

d’Aspremont C, Jacquemin A, Gabszewicz J, Weymark J (1983) On the stability of collusive price leadership. Canadian J. Econom. 16(1):17–25.

Direct Project (2019) Main page: Direct project. Accessed May 20, 2021, http://wiki.directproject.org/w/index.php?title=Main\_ Page&oldid=1589.

Gallais C, Filiol E (2017) Critical infrastructure: Where do we stand today? A comprehensive and comparative study of the defini tions of a critical infrastructure. J. Inform. Warfare 16(1):64–87.

Government of Canada (2009) National strategy for critical infrastructure. Accessed June 1, 2021, https://www.publicsafety.gc. ca/cnt/rsrcs/pblctns/srtg-crtcl-nfrstrctr/index-en.aspx.

Guo H, Liu Y, Nault BR (2021) Provisioning interoperable disaster management systems: Integrated, unified, and federated approaches. Management Inform. Systems Quart. 45(1):45–82.

Guo Z, Li J, Ramesh R (2019) Optimal management of virtual infrastructures under flexible cloud service agreements. Inform. Sys tems Res. 30(4):1424–1446.

Hu X, Caldentey R, Vulcano G (2013) Revenue sharing in airline alliances. Management Sci. 59(5):1177–1195.

Liu Y, Guo H, Nault BR (2017) Organization of public safety net works: Spillovers, interoperability, and participation. Production Oper. Management 26(4):704–723.

Nagarajan M, Sosˇic ´ G (2007) Stable farsighted coalitions in competi tive markets. Management Sci. 53(1):29–45.

Nault BR, Dexter AS (1994) Adoption, transfers and incentives in a franchise network with positive externalities. Marketing Sci. 13(4):412–423.

Nault BR, Zimmermann S (2019) Balancing openness and prioritization in a two-tier Internet. Inform. Systems Res. 30(3): 745–763.

NCOIC (2012) What is interoperability? Technical report, Network Centric Operations Industry Consortium (NCOIC). Accessed June 1, 2021, https://www.ncoic.org/what-is-interoperability/.

Oates WE (1972) Fiscal Federalism (Harcourt Brace Jovanovich, New York)

Rai A, Patnayakuni R, Seth N (2006) Firm performance impacts of digitally enabled supply chain integration capabilities. Management Inform. Systems Quart. 30(2):225–246.

Ray D, Vohra R (1999) A theory of endogenous coalition structures Games Econom. Behav. 26:286–336

Ray D, Vohra R (2001) Coalitional power and public goods. J. Politi cal Econom. 109(6):1355–1385.

Ray D, Vohra R (2015) Coalition formation. Young P, Zamir S, eds. Handbook of Game Theory with Economic Applications (Elsevier, Oxford, UK), 239–326.

Thijssen J, Hendrickx R, Borm P (2004) Spillovers and Strategic Cooperative Behaviour. Investment Under Uncertainty, Coalition Spillovers and Market Evolution in a Game Theoretic Perspective. (Kluwer Aca demic Publishers, New York), 143–164.

Vest JR, Gamm LD (2010) Health information exchange: Persistent challenges and new strategies. J. Amer. Medical Inform. Assoc. 17:288–294.

Xue L, Ray G, Gu B (2011) Environmental uncertainty and IT infrastructure governance: A curvilinear relationship. Inform. Systems Res. 22(2):389–399.
