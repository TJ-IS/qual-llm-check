---
otero_id: 12358
otero_key: "75KKT4K5"
title: "Provisioning Interoperable Disaster Management Systems: Integrated, Unified, and Federated Approaches"
authors: "Hong Guo; Yipeng Liu; Barrie R. Nault"
year: "2021"
journal: "MIS Quarterly"
doi: "10.25300/misq/2020/14947"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# PROVISIONING INTEROPERABLE DISASTERMANAGEMENT SYSTEMS: INTEGRATED, UNIFIED,AND FEDERATED APPROACHES<sup>1</sup>

Hong Guo Mendoza College of Business, University of Notre Dame, Notre Dame, IN 46556 U.S.A. {hguo@nd.edu}

Yipeng Liu College of Business, Northern Illinois University, DeKalb, IL 60115 U.S.A. {yliu@niu.edu}

Barrie R. Nault Haskayne School of Business, University of Calgary, Calgary AB T2N 1N4 CANADA {nault@calgary.ca}

In this paper, we analyze the choice of interoperability approach for the provision of disaster management systems (DMS) when resources are distributed across districts, and in times of disaster resources can be shared. The degree to which sharing (a spillover) can be coordinated efficiently depends on resource interoperability. In this public sector setting, we model the provisioning of DMS as the choice between interoperability approaches; in decreasing order of centralization they are integrated, unified, and federated. A unique feature of our setting is that the interoperability approach is a collective decision by districts. Districts choose their own DMS resources and interoperability effort, and face different interoperability efficiency and technology misfit costs depending on the interoperability approach.

We find that any approach can be an equilibrium depending on interoperability efficiency, and that when the social optimum deviates from the equilibrium the socially optimal approach is more centralized. When subsidies and taxes are implemented, the socially optimal interoperability approach can be achieved with budget balance. When only subsidies can be used, the socially optimal approach can be achieved but only under certain interoperability efficiency and misfit cost conditions is there a net social gain. Having an initial level of interoperability causes the equilibrium interoperability approach to shift toward a less centralized one. Our results generalize to other settings characterized by interoperability concerns, collective decisions, and spillovers.

Keywords: Disaster management systems, interoperability framework, spillovers, centralization, public policy

## Introduction

Disasters, either natural or human-made, represent a primary cause of human, economic, and environmental losses for local communities and society. In 2015, around 98.6 million people were affected by natural disasters worldwide with \$66.5 billion U.S. dollars of economic damages (UNISDR 2016). In many such calamities, local communities are unable to cope using their own resources. Disaster management refers to processes required to deal with a crisis in the best possible way. One of disaster management’s most important characteristics is its multi-agency nature, whereby resources, skills, and knowledge come from different protection and public safety agencies—some in adjacent jurisdictions or districts—that combine to meet the needs of all those affected in a crisis environment (Blanchard 2008).

Cooperation and coordination, essential components in disaster management, are especially challenging when considering the range of involved parties: multiple districts, different levels of government, numerous agencies, and hundreds of thousands of individual and organizational sponsors. For example, when two pressure-cooker bombs exploded near the finish line of the Boston Marathon on April 15, 2013, local police, firefighters, and emergency medical technicians joined with state and federal officials to respond to the attack. They collectively issued alerts, warnings, and information, as well as gathered tips, videos, and photos through social media. Rear Admiral Ronald Hewitt, the director of the Department of Homeland Security, stated that the bombings

illustrated a rapidly changing landscape for emergency communications, not just traditional land mobile radio use by first responders, but also citizen communications and increased use of broadband or Internet technologies (Vicinanzo 2014).

This example demonstrates the importance of exchanging and understanding information, especially in major metropolitan areas, where first responders from multiple jurisdictions swarm a dire emergency.

We define the capability of a system to exchange and understand information from other systems as interoperability. In heterogeneous and complex disaster environments, interoperability is key to the orchestration of disaster management system (DMS) resources, allowing for a coordinated and collaborative response. In this context, DMS resources include information and communications hardware and software, people (e.g., first responders), and physical assets (e.g., fire trucks and ambulances). Unfortunately, in the United States, many of the current state-level DMS resources are two decades old and not interoperable unless efforts have been made to make them so. Typical information and communication technologies, such as land mobile radios that we detail later as an example, may work only within the county where a trooper is assigned, and communicating with other agencies requires patching through the local dispatcher. If a trooper moves out of the county or needs to work with local police, then s/he often has to borrow a radio from local police. Raymond Lehr, Maryland’s interoperability director of the First Responder Network Authority (FirstNet) stated, “It’s something that has to be replaced” (Jackson 2013).

The communications failures during Louisiana’s flooding from Hurricane Katrina in August 2005 are another reminder of why first responders need a resilient, reliable, and purposebuilt disaster management system (DMS). Ronnie Johnson, Louisiana’s Army National Guard, director of Information Management stated,

… our troops, some of the best-equipped in the world, could not communicate with each other in the field. All of the commercial wireless networks went down amid the devastation, and were no more available for our first responders than they were for citizens trying to make and receive calls to loved ones (Johnson 2016).

First responders along with National Guard forces from Louisiana and other states were positioned and repositioned in response to disaster events. Being forced to rely on shortrange communications systems due to the lack of communication and information systems interoperability, the first responders were unable to coordinate search and rescue, had less knowledge of available rescue resources, and less situational information to guide them to the locations requesting assistance. Supplies and assistance from other states could not be incorporated and delivered in real time. Similar absence of basic information and communication interoperability proved devastating in post-Hurricane Maria’s slow relief effort of Puerto Rico in September 2017. These failures demonstrate that interoperable DMS is crucial in rescue, relief, and other disaster management efforts, and that the provision of resources in disaster management needs to improve (Currie 2014; GAO 2009).

That DMS interoperability is critical as evidenced by the attention it receives from government. For example, the Federal Emergency Management Agency has a disaster emergency communications division whose role is in part to provide and support interoperable communications across different levels of government; The Department of Homeland Security’s Office of Emergency Communication has developed a set of operational interoperability guides; The Commonwealth of Virginia maintains a “Statewide Interoperability Coordinator” to implement and coordinate interoperability activities across the Commonwealth; and other states such as Minnesota’s Department of Public Safety also recognize the need to exchange information within and across emergency responders. Finally, the federal government’s FirstNet mission is in part to provide a framework for robust interoperable emergency communications.

Provisioning of resources is critical to all aspects of disaster management: preparedness, response, and recovery. In this public sector setting, we consider two districts with heterogeneous preferences for disaster management resources and explicitly model their investment in an effort to improve interoperability of shared resources. Our point of departure is one that is determined by prior installations of DMSs by districts at a time before spillovers and interoperability were important concerns and can be thought of as a result of resource choices based on local conditions such as geography, population, budget, culture, etc. From this perspective, resources can include communication devices and networks, rescue and relief resources, emergency response personnel, within-district enterprise architecture, etc. Over time, as information technology used with a district’s DMS changes, effectively sharing resources (spillovers) becomes possible. It is at this point that our model begins whereby districts have to decide on their interoperability approach, additional resources, and interoperability effort.

We use the example of land mobile radio (LMR) systems to illustrate our model’s variables, parameters, assumptions, and some of the results. LMR systems are land-based wireless communications systems that include hardware such as handheld portable radios, mobile radios, base stations, a network, and repeaters (DHS 2016), as well as software for encryption, network management, etc. These are used by emergency responders at all levels of government, public works, and military. LMR systems are the primary voice communications in public safety applications, and public safety agencies are trained and skilled in LMR systems use. Deployed since the 1930s for mission critical voice communication, LMR systems have been continually enhanced, in part with new information technologies, and government agencies have invested billions of dollars in LMR infrastructure.

Many challenges agencies face when investing in LMR systems are interoperability-based. Agencies and vendors have designed systems for specific missions, and such LMR systems are often customized and not compatible with neighboring public agency systems. In addition, many LMR systems that incorporate new information technologies are not designed to be backward compatible. Although there have been attempts to develop underlying standards, currently there remain three types of modulation that each support three different system architectures (NIST 2020). Depending on the geography and application, there are also LMR radio spectrum issues: very high frequency (VHF) spectrums are better for rural and mountainous environments whereas ultra-high frequency (UHF) spectrums are better for high-noise urban environments. Even in a LMR system without communication barriers, critical information needs to be shared in real time among first responders including police, firepersons, and medical personnel.

As we discuss in more detail later, we make use of the enterprise interoperability framework (Chen and Daclin 2006; D. Chen et al. 2008). In this framework there are three interoperability approaches that represent ways that barriers to interoperability can be removed. In our DMS context these are

(1) Integrated approach: All districts agree on a common format or standard.

(2) Unified approach: There is no common format, but there is a common meta-level structure. Districts establish semantic equivalence between their resources and the common meta-level structure.

(3) Federated approach: There is no common meta-level structure. To establish interoperability, districts must accommodate other districts’ resources on the fly.

The choice among integrated, unified, or federated approaches are elements of organization design. These approaches differ in terms of technology misfit costs between a district’s own resources and preferences, and interoperability efficiency with other districts’ resources. Misfit costs are highest under the integrated approach, followed by the unified approach, and lowest under the federated approach. In contrast, given the same joint interoperability efforts, interoperability efficiency is highest under the integrated, lower under the unified, and lowest under the federated approaches. This is consistent with centralized systems being more interoperable, and our interoperability approaches are ranked from more to less centralized moving from integrated, to unified, and to federated.

We treat interoperability as a continuous endogenous variable where the interoperability level of a given approach is increased through investments in effort. Such effort improves how effectively resources from one district can be used in another district, and effort can be directed to systems design, implementation, policies and procedures, etc. In all three approaches, each district chooses its own resources and interoperability effort to maximize its own surplus. Consequently, individual districts’ effort choices jointly determine the interoperability of DMS.

A unique feature of our formulation is that the choice of interoperability approach is a collective decision by districts. An integrated form is obtained only if all districts prefer the integrated approach. The unified form is selected if both districts choose the unified approach or one district chooses integrated and the other chooses unified. The resulting interoperability approach is federated if at least one district chooses the federated approach. Thus, both the choice of interoperability approach and the requirement of a collective decision for an interoperability approach to form differentiates our work from others.

We develop a stylized model that formulates district surplus including potential spillovers from other districts for each of our interoperability approaches. The approaches differ in interoperability efficiency for resources that spillover from other districts and in technology misfit costs for their own resources. We set up a two-stage game where in Stage 1 districts choose their preferred interoperability approach. In Stage 2, districts choose their own resources where value is affected by misfit costs, and interoperability effort which together with interoperability efficiency determines the interoperability level for resource spillovers. We compare which interoperability approach is superior for DMS in terms of resources, interoperability, and social welfare.

We find that all three approaches are possible equilibria depending on interoperability efficiency. In addition, we find that all three approaches can be socially optimal, again depending on interoperability efficiency. However, we also find that an individual district’s preferences may deviate from the socially optimal approach. When districts have the incentive to deviate from the social optimum, we identify the region of misalignment between equilibrium and social optimal interoperability approaches. From this misalignment, we suggest how different incentive mechanisms such as subsidies and taxes can be deployed to induce the social optimum where a budget balance arises naturally, and how subsidies alone can be deployed where taxes are politically, legally, or otherwise infeasible. Finally, we examine the impact of having an initial interoperability level and find that our qualitative results do not change, but districts prefer a less centralized approach over a larger range of interoperability efficiency.

The remainder of the paper is organized as follows. After a brief literature review in our next section, the following section explains our notation, assumptions, and model setup. We then determine the equilibria by incorporating the district’s choice of interoperability approaches influenced by interoperability efficiency and technology misfit cost. Subsequently, we define the social optimum, compare it to equilibrium approaches, and show the properties of an incentive mechanism comprised of subsidies and taxes to induce the social optimum approach. Our conclusion summarizes our results, and discusses implications, limitations, and future research.

## Literature Review

We review two related research streams and discuss our contributions to the existing literature. To begin, our work is related to the research stream that studies coordination issues in the context of disaster management and the determinants of interoperability. Next, our work is related to the literature on organizational economics, and specifically using incentives as a form of coordination mechanisms. We then discuss related models and the positioning of this work.

## Interoperability and Coordination for Disaster Management

Disaster relief agencies face unprecedented and complex coordination challenges because they operate in urgent, uncertain, and volatile environments (Beck and Plowman 2014; Majchrzak et al. 2007). Many factors contribute to the efficiency of cooperation and coordination efforts in disaster management. Efficient expertise coordination among emergent or temporal response groups requires structural elements and role enactments that facilitate adaptability, speed, and learning (Bechky 2006; Kellogg et al. 2006; Majchrzak et al. 2007). Coordination mechanisms are needed to assure that the efforts of various agencies are synchronized, and that rescue missions and operations remain aligned for knowledge integration of cross-functional teams (Faraj and Xiao 2006; Majchrzak et al. 2012; Okhuysen and Eisenhardt 2002).

A recent report to public sector managers and political leaders finds that “most cross-agency collaborations need to set up a new kind of governing structure,” and recommends to “leverage technology to advance a collaborative network” (Sawyer and Fedorowicz 2012 p. 6) In general, there is a lack of consistent standards for emergency response, and agencies are challenged to share task-critical information in a timely manner (R. Chen et al. 2008). Some research has been done in developing a data model to reduce information interoperability barriers in fire-related extreme events (Chen et al. 2013), and enterprise application integration has been suggested as a way government authorities can overcome challenges in integrating autonomous information systems (Kamal 2009).

We next define and position the three interoperability approaches from the interoperability literature. According to the interoperability framework developed in (D. Chen et al. 2008), three categories of barriers (conceptual, technological, and organizational) prevent systems from being interoperable. Developing interoperability means developing knowledge and solutions to remove these barriers (Chen et al. 2006; D. Chen et al. 2008). The objective of this framework is to tackle interoperability problems through the identification of barriers that prevent interoperability. The interoperability barriers (conceptual, technological, and organizational) constitute the problem space of interoperability. After identifying the problem space, three interoperability approaches (integrated, unified, and federated) are proposed as the organization solutions to this problem space.

Under the integrated approach, various system components are implemented using a common standard so that interoperability is designed-in. Under the unified approach, the focus is semantic equivalence so that different parties can map their own models and applications to a neutral meta-level format. In this way, policies and standards are ways to lower conceptual barriers, enabling an integrated approach or at least a unified approach. Organizational barriers can also be addressed in part by policies such as mapping responsibility and authority between parties that are attempting to be operationally interoperable. Under the federated approach, parties bring their own models and applications, and the meta-level mapping is a one-of-a-kind peer-to-peer.

A historical analogue to the interoperability approaches is the analysis of centralized versus decentralized computing by King (1983) that categorized management options into extensive centralization, intermediate arrangements, and extensive decentralization. These options can be mapped to our integrated, unified, and federated approaches, respectively. Each option is then defined by the locus of control—allocation of decision rights, physical location such as the distribution of system assets, and management of system functions—ranging from consolidated to devolved.

In the context of disaster management, the recent organization of FirstNet by the U.S. government (see Manner et al. 2010) represents a centralized strategic center (i.e., the integrated approach). The Waterloo Regional Police Service case (Compeau and Movold 2007) represents a locally driven example of third party coordination where a third party was to provide a common information management system across more than half a dozen police organizations (i.e., the unified approach). Finally, the provision of public safety networks in the past (see Peha 2007) resembles decentralized spot markets (i.e., the federated approach). Research into the implementation of these approaches is ongoing, including the present work.

From the perspective of provisioning and managing information technology (IT) resources, new technologies such as Web 2.0 social networking tools (Majchrzak and More 2011), global positioning systems (Gaukler et al. 2008), and natural disaster management websites (Chou et al. 2014) have shown promise to help responders and volunteers in creative problem solving and coordination during relief operations. Simply distributing emergency management responsibilities across agencies is not sufficient to guarantee successful use of disaster relief resources (DeSanctis and Jackson 1994). Interoperability involves commonality of processes and technology, facilitating interactions between responders, stakeholders, and volunteers (Waugh and Streib 2006). The IT infrastructure governance choice should integrate local information processing with control and coordination (Xue et al. 2011; Xue et al. 2012). Coordination through interoperability is necessary for efficient and timely crisis response. But so far, developing the necessary process and infrastructure for crisis response has proven to be difficult (Thomas et al. 2010).

## Organization Economics and Incentive Mechanisms

The literature on organizational economics focuses on organizational forms and determinants of such forms. Prior studies identify various modes of organizations ranging from purely decentralized spot markets, to hybrid forms such as alliances, joint ventures, information-based networks, third-party coordination, strategic center, and further to purely centralized hierarchies. Two main drivers of the modes of organizations are the need for coordination and control along with the benefits of pooled strategic resources (Menard 2012).

Early literature, specifically Coase (1937, 2013), realized that using prices and markets to trade rights to perform certain actions as a means of coordinating decentralized production faces transaction costs such as a legal system that can reduce the returns to a decentralized form. Other methods of coordination such as integration into a firm (a form of centralization) that have their own costs could be preferable. Following this reasoning, Williamson (1991) defines a hybrid organization form between the polar opposites of hierarchy (firm) and markets that preserve ownership autonomy, provide strong incentives, and support bilateral dependency. Hybrids can be alternatives to vertically integrated firms where the latter has been found to create issues in sharing proprietary knowledge between a head office and subsidiaries (e.g., Nault 1998; Pierce 2012). Contracts can be the basis for hybrids such as alliances and joint ventures, and findings suggest contracts between firms where one or both engage in frequent deals are more detailed and include enforcement (Ryall and Rachelle 2009; Tan and Carrillo 2017).

## Related Models and Our Positioning

As a starting point for our modeling, we use the classic fiscal federalism framework in public finance (Besley and Coate 2003; Oates 1972) to capture the government’s decision problem of maximizing the aggregate surplus of its citizens. In prior literature, modeling the provision of assets to a public safety network using the policies proposed with FirstNet as a paradigm (see Manner et al. 2010) whereby U.S. states can opt-in or opt-out of FirstNet, Liu et al. (2017) consider a noncooperative game setting that compares centralized, decentralized, and mixed organization forms. They focus on individual districts’ incentives to opt-in or opt-out of the centralized form where districts that opt-in allocate their decisions to a central government with the result that the central government can make decisions for one district while the other district chooses to make its own decisions—a mixed form.

Although our district profit functions have some of the same structure as Liu et al., we incorporate novel elements that reflect the differences between the three interoperability approaches. These novel elements are central to our new results, and as such the set-up is significantly different. In these elements, we capture key characteristics of provisioning DMS and analyze the equilibrium and socially optimal organization form. We adopt a well-established interoperability framework, formulate our model consistent with the three interoperability approaches (integrated, unified, and federated), and set up our analysis as a multi-stage game. Table 1 illustrates the positioning of our work in terms of the interoperability barriers and interoperability approaches we address relative to other related studies.

## Notation, Assumptions, and Model Structure

## Resources for Disaster Management

Our model has two districts, indexed by j 0 {1, 2}, that consider the provision of DMS resources. In the case of a disaster in one district, resources from the other district can be used as part of the disaster management response. As such, there are potential spillovers from the resources in one district to the other district that depend in part on interoperability. Consequently, when making resource decisions, the choice of resources in one district must account for the choice of resources in the other district.

As discussed earlier, we consider three interoperability approaches: integrated, unified, and federated, denoted by $i \in$ $\{ I , U , F \}$ . We denote the DMS resources associated with the two districts for each interoperability approach by $g _ { i 1 }$ and $g _ { i 2 } ,$ respectively, with $g _ { i j } \in [ 0 , \overline { { g } } ]$ , where $\bar { g }$ is the upper bound for resources and is large enough to guarantee the feasibility of the interior solution. We use a quadratic cost function $p g _ { i j } ^ { 2 }$ with parameter $p \in R ^ { + }$ to capture the increasing marginal cost associated with building/acquiring resources. There are other functional forms for costs, but these would require more elaborate assumptions, and some type of convexity would still be necessary to get interior solutions. Given this fact, the most commonly used form (affine benefits and quadratic costs) is more generalizable and comparable to other models in the literature. Technically, all that is needed is that costs are convex. Examples include the cost of building communication networks, acquiring rescue and relief resources, training emergency response personnel, etc.

To illustrate, consider our example of LMR systems for emergency responders. DMS resources in this context correspond to hardware (such as portable and mobile radios, base station radios, network and repeaters), software (such as encryption and network management), and other resources including people (such as police, firepersons, and medical personnel) and physical assets (such as fire trucks and ambulances). Regarding our assumption of convex costs, as the total amount of DMS resources increase, the marginal cost to support the growing system increases. Hence the overall cost is convex, which we model with quadratic costs.

Each district is characterized by a resource preference that we denote by $m _ { j } \in R ^ { \dag }$ . The district with a higher $m _ { j }$ values the resources more. Different districts often have heterogeneous preferences for resources. For example, one district may face higher threats from forest wildfire due to local terrain, land use, and weather conditions. We use $m _ { j }$ to represent the resource preferences at an aggregate level of all citizens in a district, which depends on publicly observable district-level characteristics such as population density, geography, etc. Thus, $m _ { j }$ is publicly observable and cannot be misrepresented. Without loss of generality, we capture heterogeneous resource preferences in the following assumption.

ASSUMPTION 1. District 1 values resources more than District 2: $m _ { 1 } \geq m _ { 2 }$

Resource spillovers enable a district to make use $\operatorname { o f } ,$ and therefore receive, value from resources in another district. In valuing resources, we use the parameter ê $\varepsilon [ 0 , 0 . 5 ]$ to denote the relative weight of resources in the other district and use $[ 1 - \kappa ]$ as the relative weight of resources in its own district. Defining ê this way ensures local resources always have a higher relative weight: when $\kappa = 0 _ { ; }$ , a district only values resources in its own district; when $\kappa = 0 . 5 ,$ , a district values resources in both districts equally. We interpret ê as a degree of spillover of resources between districts such that a higher ê represents a higher cross-district value, and given our restriction $\kappa \in [ 0 , 0 . 5 ]$ , a district’s own resources are always at least as valuable as those resources that spillover from the other district. To simplify our analyses, we treat generically, that is, ê is not district-specific.

<table><tr><td rowspan="2">Interoperability Literature</td><td colspan="3">Interoperability Barriers</td><td colspan="3">Interoperability Approaches</td></tr><tr><td>Conceptual</td><td>Technological</td><td>Organizational</td><td>Integrated</td><td>Unified</td><td>Federated</td></tr><tr><td>Bechky 2006</td><td>X</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Beck and Plowman 2014</td><td>X</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>D. Chen et al. 2006; D. Chen et al. 2008</td><td></td><td></td><td></td><td>X</td><td>X</td><td>X</td></tr><tr><td>R. Chen et al. 2008 &amp; 2013</td><td>X</td><td>X</td><td></td><td></td><td></td><td>X</td></tr><tr><td>DeSanctis and Jackson 1994</td><td></td><td>X</td><td>X</td><td></td><td></td><td></td></tr><tr><td>Kellogg et al. 2006</td><td>X</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Liu et al. 2017</td><td></td><td></td><td>X</td><td>X</td><td></td><td>X</td></tr><tr><td>Majchrzak et al. 2007; Majchrzak et al. 2012</td><td>X</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Majchrzak and More 2011</td><td></td><td>X</td><td>X</td><td></td><td></td><td></td></tr><tr><td>Manner et al. 2010</td><td></td><td>X</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>Peha 2007</td><td></td><td>X</td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>This paper</td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr></table>

## Interoperability Approaches, Effort, and Efficiency

Our three interoperability approaches have different payoff structures that reflect interoperability and technology misfit that we provide detail about later. Based on its surplus, each district chooses its preferred interoperability approach, denoted by $t _ { 1 }$ and t with $t _ { 1 } , t _ { 2 } \in \{ I , U , F \}$

We model the cross-district coordination such that effort can be made to improve the interoperability among different resources with a cost. Thus, an important element of our model is the inclusion of interoperability effort between districts. As we saw earlier in our LMR example, interoperability is challenged by LMR systems that are customized for specific missions, multiple vendors, issues with standards and backward compatibility, and even spectrum choices.

Each district chooses its interoperability effort for a given interoperability approach $e _ { i j } \in [ 0 , \bar { e } ]$ , where $i \in \{ I , U , F \}$ and $j \in \{ 1 , 2 \}$ , to integrate different technologies, resources, and personnel to provide cross-district disaster management services. The upper bound $\overline { { e } }$ is the maximum overall interoperability effort level. When the combined interoperability effort between the two districts is equivalent to $\overline { { e } } ,$ the DMS from both districts are fully interoperable. In this way, we use ¯e as a numeraire to normalize interoperability effort in terms of this maximum effort level. Coordination and hence the benefits derived from the DMS depend on the combined interoperability effort. Our next assumption details how the interoperability efforts are combined in our model.

ASSUMPTION 2. Interoperability effort from the districts is combined additively and normalized $b y \overset { - } { e } i$ o obtain the interoperability level between districts: $( e _ { i 1 } + e _ { i 2 } ) / { \overline { { e } } }$

We take the additive form $( \mathrm { i . e . , } e _ { i 1 } + e _ { i 2 } )$ for the combined interoperability effort to guarantee that District j derives benefit from investing in interoperability even if the other district does not invest in effort $( \mathrm { i } . \mathrm { e } . , e _ { i \mid j } = 0 )$ . Both districts accept this mutual dependence of their joint investments in interoperability to create greater value from the spillover of their investments in resources which are unattainable otherwise (Bakos and Nault 1997; Borys and Jemison 1989). If the combined interoperability effort is high, resulting in high interoperability, then both districts derive greater value from the other district in the presence of spillover.

In disaster management, the value of resources from another district depends on the degree to which the resources are interoperable. Thus, the efficiency of coordination between districts is affected by the interoperability of the resources within a DMS. When using the unified or federated approaches each district makes its own resource decisions including technology choices as well as implementation choices, both of which are geared to local conditions and history. When using such approaches there are always issues with compatibility and interoperability. Furthermore, under the unified approach, as a common standard is adopted for meta technologies, interoperability issues are less severe compared to the federated approach. In other words, relative to the integrated approach, unified and federated approaches may bring flexibility and fast response to changing local needs, as well as other benefits, but those approaches also make systems integration difficult and present a barrier to standardization (see DeSanctis and Jackson 1994; Gopal et al. 2003; Harter et al. 2000; King 1983; Krishnan et al. 2000; Schuff and St. Louis 2001; Xue et al. 2011; Zmud 1980).

As we described earlier, because interoperability is more challenging under the unified and federated approaches, we parameterize interoperability efficiency of these approaches relative to the integrated approach with $\beta _ { U }$ and $\beta _ { F } ,$ , respectively, where the interoperability efficiency of the integrated approach, $\beta _ { I } ,$ is normalized to 1. This leads to our next assumption.

ASSUMPTION 3. Relative to the integrated approach, there is an efficiency loss in coordination under the unified and federated approaches: $0 < \beta _ { F } < \beta _ { U } < \beta _ { I } = 1$

Returning to our LMR example, an integrated approach corresponds to a system without communication barriers $( \mathrm { e . g . } ,$ both districts using the same radio frequency). However, information is relayed from emergency responders to the individual district’s head office for review and processing by investigators, supervisors, and other command staff before being communicated to the other district. Establishing formal channels and protocols is an example of effort invested by both districts to further improve coordination and interoperability. A unified approach corresponds to both districts agreeing upon an open radio frequency channel or reprogramming their LMR devices when communicating across districts. A federated approach corresponds to where an officer must locate and borrow the LMR device from the other district’s officer. Comparing interoperability efficiency across interoperability approaches, the integrated approach is the most efficient with the federated approach being the least efficient.

## Technology Misfit Cost

As districts differ in their DMS needs based on their local conditions, their choices of the kind of DMS resources that are most effective may differ as well. This gives rise to potential misfits in technology choice under the integrated and unified approaches relative to what each district may find optimal in isolation. We parameterize the technology misfit costs of the integrated and unified approaches relative to the federated approach with $f _ { I }$ and $f _ { U } ,$ respectively. Under the federated approach, the districts have the freedom to choose technologies that fit their local needs with minimal technology misfit cost. We normalize the technology misfit costs of the federated approach, $f _ { F } ,$ to zero. Under the integrated approach, both districts choose the same standard technology, which may deviate from their own ideal choices, leading to a technology misfit cost. Similarly, under the unified approach, although two districts can choose different technologies, they have to adopt a common meta technology. Thus, both districts also suffer a technology misfit cost under the unified approach, which we take as less severe than that under the integrated approach. To capture these differences in misfit costs, we make the next assumption.

ASSUMPTION 4. Relative to the federated approach, there are technology misfit costs in choices under the integrated and unified approaches, where the integrated approach incurs greater costs: $0 = f _ { \scriptscriptstyle F } < f _ { \scriptscriptstyle U } < f _ { \scriptscriptstyle I } < 1$

Note that our characterization of technology misfit costs is dependent on interoperability approaches and independent of district. Here, our focus is to differentiate between districts based on their resource preferences, $m _ { j } ,$ where district 1 values resources more than district 2 (Assumption 1). As a result, different districts incur different technology misfit costs. In our LMR example, the misfit cost can be seen in districts’ choices of different radio spectrums. The VHF spectrum is good for districts with large rural or hilly/ mountainous areas to cover. The UHF spectrum is well suited for districts with high-noise urban environments. Thus, LMR spectrums that are mismatched with a district’s characteristics result in misfit costs that reduce the value of their LMR systems.

We partition the effects of misfit costs and interoperability level between a district’s own resources and those that spill over from another district. This partition effectively means that interoperability effort mitigates issues of technology misfit from spillovers. That is, misfit costs as a separate construct from interoperability level do not affect spillovers from the other district. Thus, misfit costs apply only to a district’s own resources. This is our last assumption.

ASSUMPTION 5. The interoperability level affects the value of the spillover similarly across different interoperability approaches and misfit costs do not affect spillovers.

This assumption recognizes that technology choices of either district may vary in how they fit the other, and that the fit is affected by the interoperability effort. Interoperability effort leading to interoperability level can be interpreted in part as addressing issues of fit between the DMS resources that spill over and a district’s own resources. For example, with LMR systems if there are misfit costs due to differences in spectrum choices, then interoperability effort will be directed to overcoming those misfit costs.

<table><tr><td colspan="2">Table 2. Summary of Notation</td></tr><tr><td colspan="2">Decision Variables</td></tr><tr><td> $t_1$  and  $t_2$ </td><td>Choice of interoperability approach by individual districts,  $t_1, t_2 \in \{I, U, F\}$ </td></tr><tr><td> $g_{i1}$  and  $g_{i2}$ </td><td>DMS resources chosen by each district using approach i, where i ∈ {I (integrated), U (unified), F (federated)}</td></tr><tr><td> $e_{i1}$  and  $e_{i2}$ </td><td>Interoperability efforts chosen by each district using approach i</td></tr><tr><td> $x_{i1}$  and  $x_{i2}$ </td><td>Subsidy/Tax associated with approach i offered to each district, chosen by the social planner under the incentive mechanism</td></tr><tr><td colspan="2">Other Variables</td></tr><tr><td> $S_{i1}$  and  $S_{i2}$ </td><td>Total surplus within District 1 and 2 under approach i</td></tr><tr><td> $S_i$ </td><td>Social welfare using approach i</td></tr><tr><td colspan="2">Parameters</td></tr><tr><td> $\overline{g}$ </td><td>Upper bound for DMS resources</td></tr><tr><td> $m_1$  and  $m_2$ </td><td>DMS resource preference of District 1 and 2, respectively</td></tr><tr><td>κ</td><td>Degree of spillover</td></tr><tr><td> $β_U$  and  $β_F$ </td><td>Interoperability efficiency under the unified and federated approaches, 0 &lt;  $β_F$  &lt;  $β_U$  &lt; 1</td></tr><tr><td> $f_I$  and  $f_U$ </td><td>Technology misfit cost parameter under the integrated and unified approaches, 0 &lt;  $f_U$  &lt;  $f_I$  &lt; 1</td></tr><tr><td> $\overline{e}$ </td><td>Maximum overall interoperability effort level</td></tr><tr><td>p</td><td>Cost parameter associated with producing or acquiring DMS resources</td></tr><tr><td>δ</td><td>Cost parameter associated with effort to improve interoperability</td></tr><tr><td colspan="2">Thresholds</td></tr><tr><td> $\hat{\beta}_{U1}$  and  $\hat{\beta}_{U2}$ </td><td>Threshold for  $[\beta_U]^2$  such that  $S_{Ij} = S_{Uj}$  when  $[\beta_U]^2 = \hat{\beta}_{Uj}, j = 1, 2$ </td></tr><tr><td> $\hat{\beta}_{F1}$  and  $\hat{\beta}_{F2}$ </td><td>Threshold for  $[\beta_F]^2$  such that  $S_{Ij} = S_{Fj}$  when  $[\beta_F]^2 = \hat{\beta}_{Fj}$ </td></tr><tr><td> $\hat{\beta}_{UF1}$  and  $\hat{\beta}_{UF2}$ </td><td>Threshold for  $[\beta_U]^2$  such that  $S_{Uj} = S_{Fj}$  when  $[\beta_U]^2 = \hat{\beta}_{UFj}$ </td></tr><tr><td> $\hat{\beta}_{U}^{Eqm}, \hat{\beta}_{F}^{Eqm}, \text{and } \hat{\beta}_{UF}^{Eqm}$ </td><td>Separating thresholds for the equilibrium approaches</td></tr><tr><td> $\hat{\beta}_{U}^{SW}, \hat{\beta}_{F}^{SW}, \text{and } \hat{\beta}_{UF}^{SW}$ </td><td>Separating thresholds for the social optimal approaches, where superscript SW represents social welfare</td></tr><tr><td> $\hat{\beta}_{U}^{SG}, \hat{\beta}_{F}^{SG}, \text{and } \hat{\beta}_{UF}^{SG}$ </td><td>Separating thresholds for the cost effectiveness of the incentive mechanism, where superscript SG represents social gain</td></tr></table>

We take all parameters and the relationships between the parameters in Assumptions 1–5 as public information. Our notation is summarized in Table 2.

## Individual Districts’ Surplus under Different Interoperability Approaches

Next, we present individual districts’ surplus using each of the three interoperability approaches.

Integrated: Under the integrated approach the individual districts’ surplus is

$$
\begin{array}{l} S _ {I j} \left(g _ {I j}, e _ {I j}\right) = \\ m _ {j} \left[ [ 1 - \kappa ] [ 1 - f _ {I} ] g _ {I j} + \kappa \left[ \frac {e _ {i j} + e _ {I \setminus j}}{\overline {{e}}} \right] g _ {I \setminus j} \right] - p g _ {I j} ^ {2} - \delta e _ {f j} ^ {2} \end{array}
$$

Here we use j to denote the focal district and \j to denote the other district. There are three main components in each district’s surplus: the benefits of DMS resources, the cost of producing or acquiring DMS resources with parameter $^ { p , }$ and the cost of interoperability effort with parameter ä. We take it that the cost parameters of resources and of efforts are not so large as to make the problem trivial (i.e., districts choosing zero resources or efforts). The benefits from DMS resources consist of two parts: the first part is the benefit derived from the focal district’s own resources, which is moderated by misfit cost parameter $f _ { I }$ Here $f _ { I }$ can be considered as misfit cost measured in percentages. The second part is the benefit derived from the other district’s resources, which is moderated by interoperability level $\displaystyle \left[ \frac { e _ { I 1 } + e _ { I 2 } } { \overline { { e } } } \right]$

Under the unified and federated approaches, interoperability level takes the form of $\beta _ { U } \left[ \frac { e _ { 1 } + e _ { 2 } } { \overline { { e } } } \right]$ and $\beta _ { F } \left[ \frac { e _ { 1 } + e _ { 2 } } { \overline { { e } } } \right]$ respectively. It is worth recognizing that under the integrated approach interoperability efficiency does not suffer as it does under the unified and federated approaches because of the adoption of a standard technology under the integrated approach.

Unified: Under the unified approach the individual districts surplus are

$$
\begin{array}{l} S _ {U j} \left(g _ {U j}, e _ {U j}\right) = \\ m _ {j} \left[ [ 1 - \kappa ] [ 1 - f _ {U} ] g _ {U j} + \kappa \beta_ {U} \left[ \frac {e _ {U j} + e _ {U \backslash j}}{\bar {e}} \right] g _ {U \backslash j} \right] - p g _ {U j} ^ {2} - \delta e _ {U j} ^ {2} \end{array}
$$

The key difference in the districts’ surpluses between the integrated and unified approaches lies in the technology misfit cost parameter $f _ { U }$ and interoperability efficiency level $\beta _ { U } \left[ { \frac { e _ { U 1 } + e _ { U 2 } } { \overline { { e } } } } \right]$

Federated: Under the federated approach the individual districts’ surplus are

$$
\begin{array}{l} S _ {F j} \left(g _ {F j}, e _ {F j}\right) = \\ m _ {j} \left[ \left[ 1 - \kappa \right] g _ {F j} + \kappa \beta_ {F} \left[ \frac {e _ {F j} + e _ {F \backslash j}}{\bar {e}} \right] g _ {F \backslash j} \right] - p g _ {F j} ^ {2} - \delta e _ {F j} ^ {2} \end{array}
$$

The key difference in the districts’ surplus between the unified and federated approaches lies in technology misfit cost parameter $f _ { F } = 0$ and interoperability efficiency level $\beta _ { F } \Bigg [ \frac { e _ { F 1 } + e _ { F 2 } } { \overline { { e } } } \Bigg ]$

To summarize, the differences among the three approaches are captured in Assumptions 3 and 4: $0 < \beta _ { F } < \beta _ { U } < \beta _ { I } = 1$ and $0 = f _ { F } { < } f _ { U } { < } f _ { I } { < } 1$

## Model Structure

In our provisioning game, each district first chooses an interoperability approach, then chooses its resources and interoperability effort. We set this up as a two-stage game where the stages are defined below.

Stage 1: In Stage 1, each district chooses an interoperability approach among three options, $t _ { 1 , ~ } t _ { 2 } \in ~ \{ I , ~ U , ~ F \}$ The resulting approach is a collective decision: the resulting interoperability approach is the less centralized between the choices of the two districts. This is based on the reasoning that one district cannot force an approach that requires more coordination (or less independence) on the other. Consequently,

• the interoperability approach is integrated if both districts choose I,

the interoperability approach is unified if both districts choose U or one district chooses I and the other chooses $U ,$ and

• the interoperability approach is federated if at least one district chooses F.

As shown in Table 3, if two districts choose different interoperability approaches, then the less centralized approach is the result consistent with the collective decision described above. Using our parameterization of interoperability efficiency and technology misfit costs, the reasons for this are as follows: If I and U are chosen, then I faces $\beta _ { U }$ as well as $f _ { I }$ so prefers U. If I and F are chosen, then I faces $\beta _ { F }$ as well as $f _ { I }$ so prefers F. If U and F are chosen, then U faces $\beta _ { F }$ as well as $f _ { U }$ so prefers F.

Stage 2: In Stage 2, using the resulting interoperability approach i, each district chooses resources $g _ { i j }$ and interoperability effort $e _ { i j }$ to maximize the total surplus within its district $j \in \{ 1 , 2 \}$ In other words, District 1’s decision problem is $S _ { i 1 }$ and District 2’s decision problem is gf1,e11 max $S _ { i 2 }$ , with $i \in \{ I , U , F \}$ , where the equations that describe g12.e12 the total surplus within each district for a given interoperability approach are provided in the prior section.

Regarding the order of decision making, our formulation is standard: the design of how districts work together (interoperability approach) is set first, then districts react to that design in their choice of investments in resources and interoperability effort. In the context of LMR systems the choice of interoperability approach is whether to have common choices in spectrum, vendor, equipment, software, personnel training programs, etc. (integrated), or limited matching in terms of perhaps vendor, and software (unified), or each district makes their own choices independently (federated). This results in different levels of misfit costs and of interoperability efficiency. Given this, districts then make their investments in LMR resources and interoperability effort.

<table><tr><td colspan="5">Table 3. Determination of Interoperability Approaches</td></tr><tr><td rowspan="2" colspan="2"></td><td colspan="3">District 2&#x27;s Choice</td></tr><tr><td> $t_2 = I$ </td><td> $t_2 = U$ </td><td> $t_2 = F$ </td></tr><tr><td rowspan="3">District 1&#x27;s Choice</td><td> $t_1 = I$ </td><td>I</td><td>U</td><td>F</td></tr><tr><td> $t_1 = U$ </td><td>U</td><td>U</td><td>F</td></tr><tr><td> $t_1 = F$ </td><td>F</td><td>F</td><td>F</td></tr></table>

## Equilibrium Analysis of the Model

We solve the DMS provisioning game using backward induction, where investments are determined for each interoperability approach yielding the surplus each district receive under each interoperability approach, and then the interoperability approach is chosen.

Stage 2: In Stage 2, given two districts’ choices of interoperability approaches $t _ { 1 }$ and $t _ { 2 } ,$ the resulting interoperability approach $i \in \{ I , ~ U , ~ F \}$ is obtained from Table 3. For each interoperability approach, each district maximizes its surplus by choosing resources and interoperability effort. Jointly solving for individual districts’ optimal resources, $g _ { i j }$ and interoperability effort, $e _ { i j } ,$ yields a Nash equilibrium where the resources and interoperability efforts are optimal value functions of our parameters. We note that solving for optimal resources and interoperability effort sequentially yields the same results because there is no “event” that occurs between the choice of resources and interoperability effort. We then compute the corresponding surplus for each of the districts, $S _ { i j } .$ The expressions for the individual districts’ resources, interoperability effort, and surplus are given in the Appendix.

Stage 1: In Stage 1, we compare individual district’s surplus, $S _ { i j } ,$ across the three interoperability approaches to determine the districts’ choices. Depending on the values of interoperability efficiency parameters $\beta _ { U }$ and $\beta _ { F }$ , there are nine cases illustrated by nine numbered regions in Figure 1. We use the squares of $\beta _ { C }$ and $\beta _ { F }$ as axes throughout our figures so that partitioning the space can be done with lines rather than curves. The cases are defined by the surplus ranking for each district across the three interoperability approaches, and by the interoperability approach that results from the two districts’ collective choices. The feasible region that contains these cases defined is by our Assumption $3 , 0 < \beta _ { F } < \beta _ { U } < \beta _ { I }$ = 1, and corresponds to the upper triangle whose boundaries are indicated by the bold lines. To the right of the figure are the surplus rankings for each district across the three interoperability approaches. The regions are determined by a set of interoperability efficiency thresholds defined by when a given district is indifferent between two interoperability approaches.

The interoperability efficiency thresholds $\hat { \beta } _ { U j } , \hat { \beta } _ { F j }$ , and $\hat { \beta } _ { U F j }$ for District $j ~ \in ~ \{ 1 , ~ 2 \}$ are defined as follows. When $\left[ \beta _ { U } \right] ^ { 2 } = \hat { \beta } _ { U j }$ , District j is indifferent between the integrated and unified approaches (i.e., $S _ { I j } = S _ { U j }$ at $\left[ \beta _ { U } \right] ^ { 2 } = \hat { \beta } _ { U j } )$ . When $\left[ \beta _ { F } \right] ^ { 2 } = \hat { \beta } _ { F j }$ , District j is indifferent between the integrated and federated approaches $( \mathrm { i . e . , } S _ { I j } = S _ { F j } \mathrm { a t } \left[ \beta _ { F } \right] ^ { 2 } = \hat { \beta } _ { F j } )$ . When $\left[ \beta _ { U } \right] ^ { 2 } = \hat { \beta } _ { U F j }$ , District j is indifferent between the unified and federated approaches, $( \mathrm { i . e . , } S _ { U j } = S _ { F j } \mathrm { a t } \left[ \beta _ { U } \right] ^ { 2 } = \hat { \beta } _ { U F j } )$ .

For each region in the upper triangle of Figure 1 there is the possibility of multiple Nash equilibrium interoperability approaches. When there are multiple equilibria, we refine the set of equilibria based on Pareto efficiency where a Pareto efficient equilibrium is characterized by an equilibrium interoperability approach where there is not another equilibrium that makes one district better off without making the other worse off. We use Case 1 as an example to show how we solve for and refine the equilibrium. The analyses of the remaining cases are relegated to the Appendix. In Case 1, as illustrated in Table 4, we use underline to indicate the preference of District 1 and overline to indicate the preference of District 2.

To determine whether a given cell is a Nash equilibrium, we check whether one district has the incentive to deviate given the other district’s choice: we check whether their strategy is a best response. Given District 2 chooses $I ( t _ { 2 } = I )$ , District 1 prefers I because $S _ { I 1 } > S _ { F 1 } > S _ { U 1 }$ . Given District 1 chooses $I ( t _ { 1 } = I )$ , District 2 prefers I because $S _ { I 2 } > S _ { F 2 } > S _ { U 2 }$ . Thus,

![](/api/attachments/75KKT4K5/fulltext/images/c2b87b214c0c3ecdb6b5c83442c30bd3d97f25283d40df7b9fb93df216c0c9ef.jpg)  
Note: The feasible region defined by Assumption 3 corresponds to the upper triangle, indicated by the bold lines. The red solid lines correspond to District 1’s preference, while the green dotted lines correspond to District 2’s preference.

## Figure 1. Nine Equilibrium Cases

<table><tr><td colspan="5">Table 4. Equilibrium Derivation for Case 1</td></tr><tr><td rowspan="2" colspan="2"></td><td colspan="3">District 2&#x27;s Choice</td></tr><tr><td> $t_2 = I$ </td><td> $t_2 = U$ </td><td> $t_2 = F$ </td></tr><tr><td rowspan="3">District 1&#x27;s Choice</td><td> $t_1 = I$ </td><td> $I(S_{I1},S_{I2})$ </td><td> $U(S_{U1},S_{U2})$ </td><td> $F(S_{F1},S_{F2})$ </td></tr><tr><td> $t_1 = U$ </td><td> $U(S_{U1},S_{U2})$ </td><td> $U(S_{U1},S_{U2})$ </td><td> $F(S_{F1},S_{F2})$ </td></tr><tr><td> $t_1 = F$ </td><td> $F(S_{F1},S_{F2})$ </td><td> $F(S_{F1},S_{F2})$ </td><td> $F(S_{F1},S_{F2})$ </td></tr></table>

(I, I) is a best response equilibrium. Similarly, we check the other eight outcomes. After checking all nine outcomes, we find that there are four Nash equilibria in Case 1: (I, I), (F, U), (U, F), and $( F , F )$ . In these, there are two equilibrium interoperability approaches: integrated and federated.

We further compare both districts’ surplus in these two equilibrium interoperability approaches. Because $S _ { I 1 } > S _ { F 1 } > S _ { U 1 }$ and $S _ { I 2 } > S _ { F 2 } > S _ { U 2 } ,$ we conclude that the (I, I) is the Pareto efficient equilibrium because at (I, I) as both districts are better off using an integrated interoperability approach than a federated one. This Pareto efficient equilibrium is indicated by the highlighted cell in Table 4.

Summarizing the equilibrium interoperability approach in all nine cases, in Cases 1–5 with relatively low $\beta _ { F } ,$ there are multiple equilibria. In Cases 1–3, the integrated approach is the Pareto efficient equilibrium. In Cases 4–5, the unified approach is the Pareto efficient equilibrium. In Cases 6–9, the federated approach is the only possible equilibrium. Lemmas 1 and 2 formally summarize the districts’ choices and the equilibrium interoperability approach. Proofs of our lemmas and propositions are available in the Appendix.

LEMMA 1: The Pareto efficient interoperability approach of District j 0 {1, 2} is integrated $i f { \left[ \beta _ { v } \right] } ^ { 2 } < \hat { \beta } _ { U j }$ and $\left[ \beta _ { F } \right] ^ { 2 } < \hat { \beta } _ { F j }$ unified $i f \left[ \beta _ { v } \right] ^ { 2 } \geq \operatorname* { m a x } \left\{ \hat { \beta } _ { v j } , \hat { \beta } _ { U F j } \right\}$ ; and federated if $\left[ \beta _ { U } \right] ^ { 2 } < \hat { \beta } _ { U F j }$ and $\left[ \beta _ { F } \right] ^ { 2 } \geq \hat { \beta } _ { F j }$

![](/api/attachments/75KKT4K5/fulltext/images/76f76fcbee010f79a9f7ce584a2c0c621a01ab88ad9748bc8a9f746d3d2a921e.jpg)  
Figure 2. Individual Districts’ Preferred Interoperability Approach

Lemma 1 and Figure 2 show individual districts’ preferred interoperability approach. Intuitively, a district prefers the integrated approach when the interoperability efficiency loss under the other two approaches are high (i.e., both $\beta _ { U }$ and $\beta _ { F }$ lower than a threshold). The federated approach is preferred when $\beta _ { F }$ is relatively high and $\beta _ { U }$ is relatively low. Otherwise, the unified approach is preferred. As illustrated in Figure 2, the red solid lines correspond to District 1’s preference while the green dotted lines correspond to District 2’s preference.

Figure 3 also shows that District 1’s preferred interoperability approach is either the same or less centralized than District 2’s preferred approach. From our Table 3 this means that the equilibrium interoperability thresholds, $\hat { \beta } _ { U } ^ { E q m } , \hat { \beta } _ { F } ^ { E q m }$ , and $\hat { \beta } _ { U F } ^ { E q m }$ are those of District 1.

LEMMA 2: The Pareto efficient equilibrium interoperability approach is integrated if $\left[ \beta _ { U } \right] ^ { 2 } < \hat { \beta } _ { U } ^ { E q m }$ and $\left[ \beta _ { F } \right] ^ { 2 } < \hat { \beta } _ { F } ^ { E q m } ,$ unified $i f \left[ \beta _ { v } \right] ^ { 2 } \geq \operatorname* { m a x } \left\{ \hat { \beta } _ { v } ^ { E q m } , \hat { \beta } _ { v F } ^ { E q m } \right\}$ ; and federated i $f \left[ \beta _ { U } \right] ^ { 2 } < \hat { \beta } _ { U F } ^ { E q m }$ and $\left[ \beta _ { F } \right] ^ { 2 } \ge \hat { \beta } _ { F } ^ { E q m }$

Lemma 2 and Figure 3 show the Pareto efficient equilibrium interoperability approach. Based on individual districts’ preferences, a more centralized interoperability approach is the equilibrium if and only if both districts prefer that approach. If at least one district prefers a less centralized approach, then the less centralized approach becomes the equilibrium. When $\beta _ { U }$ is large and $\beta _ { F }$ is not, it indicates that the unified approach becomes more efficient in converting interoperability efforts into benefits, which makes the unified approach more desirable to both districts. Thus, the unified approach is more likely to be the equilibrium. Similarly, when $1 \beta _ { F }$ becomes large, the federated approach becomes more efficient. Meanwhile the misfit cost of DMS resources is lower under the federated approach, hence the federated approach is more likely to be the equilibrium. When $\beta _ { U }$ and $\beta _ { F }$ are both small, the interoperability efficiency benefits of the integrated approach far outweigh the misfit cost, and as a result the integrated approach is more likely to be the equilibrium.

PROPOSITION 1: (Properties of equilibrium interoperability approaches): All three interoperability approaches are possible equilibria. The equilibrium is determined by District 1’s preference (i.e., $\hat { \beta } _ { U } ^ { E q m } = \hat { \beta } _ { U 1 } , \hat { \beta } _ { F } ^ { E q m } = \hat { \beta } _ { F 1 }$ ,and $\hat { \beta } _ { U F } ^ { E q m } = \hat { \beta } _ { U F 1 } )$

The equilibrium interoperability approach critically depends on interoperability efficiencies captured by the parameters $\beta _ { U }$ and $\beta _ { F }$ , and the Pareto efficient equilibrium is determined by District 1’s preferences only. Recall that the only difference between two districts lies in their preferences for DMS resources with District 1 valuing DMS resources more (i.e., $m _ { 1 } > m _ { 2 } ~ )$ . This heterogeneous characteristic leads to two districts’ different choices of resources and interoperability effort, as well as their different preferences for interoperability approaches. The reason why District 1 prefers a more centralized approach in a smaller region than District 2 is because of Assumption 1: with a higher valuation for resources than District 2, the resources and interoperability effort chosen by District 1 are higher, and thus the spill over is more valuable to District 2.

![](/api/attachments/75KKT4K5/fulltext/images/f756641c1a92f629892f6041edc76515dc980443eea77b200bb66c91c44e9802.jpg)  
Figure 3. Equilibrium Interoperability Approach

COROLLARY 1: (Impact of misfit cost and degree of spillover on equilibrium interoperability approaches):

(i) When f increases, $\hat { \beta } _ { U } ^ { E q m }$ and $\hat { \beta } _ { F } ^ { E q m }$ decrease while $\hat { \beta } _ { U F } ^ { E q m }$ remains unchanged. When $f _ { U }$ increases, $\hat { \beta } _ { U } ^ { E q m }$ increases and both the slope and the intercept of $\hat { \beta } _ { U F } ^ { E q m }$ increase, while $\hat { \beta } _ { F } ^ { E q m }$ remains unchanged.

(ii) When ê increases, $\hat { \beta } _ { U } ^ { E q m }$ and $\hat { \beta } _ { F } ^ { E q m }$ increase while $\hat { \beta } _ { U F } ^ { E q m }$ decreases.

Corollary 1 presents the impact of misfit costs and degree of spillover on equilibrium interoperability approaches. With an increase of the misfit cost, $f _ { U }$ or $f _ { I } ,$ the corresponding interoperability approach, U or $I ,$ becomes less likely to be the equilibrium approach. In LMR systems for example, as the cost of using a radio spectrum that does not match with the district’s geography increases, the unified or integrated approaches are less likely to be the equilibrium approach. With an increase of the degree of spillover, the districts reply more on the other district’s resources. Consequently, the districts prefer a more centralized approach in a larger parameter space to take advantage of a higher interoperability efficiency.

## Analysis of Socially Optimal Interoperability Approach

We explore the socially optimal interoperability approach. We start with the first-best social optimum. Theoretically, the first-best social optimum involves the social planner maximizing social welfare (the overall total surplus of both districts) by selecting the interoperability approach $( i ) ,$ resources $( g _ { i 1 }$ and $g _ { i 2 } )$ , and interoperability efforts $( e _ { i 1 }$ and $e _ { i 2 } )$ for the two districts. The social planner’s decision problem can be formulated as max $S _ { i } = S _ { i 1 } + S _ { i 2 }$ . However, this first-best i.g1,812,e1,e12 social optimum is practically unattainable due to various reasons such as incomplete information regarding local needs of districts, non-contractibility of interoperability tasks, etc.

Instead, we investigate a social optimum that allows each district to choose its optimal resources $( g _ { i j } )$ and interoperability effort $( e _ { i j } )$ for each interoperability approach. Then the socially optimal approach is the one that maximizes social welfare across different approaches. Lemma 3 summarizes the results of the socially optimal interoperability approach. There are again interoperability efficiency thresholds for social welfare: $\hat { \beta } _ { U } ^ { S W } , \hat { \beta } _ { F } ^ { S W }$ , and $\hat { \beta } _ { U F } ^ { S W }$ . When $\left[ \beta _ { U } \right] ^ { 2 } = \hat { \beta } _ { U } ^ { S W }$ , the planner is indifferent between the integrated and unified approaches $\mathrm { ( i . e . , } S _ { I 1 } + S _ { I 2 } = S _ { U 1 } + S _ { U 2 } \mathrm { a t } \left[ \beta _ { U } \right] ^ { 2 } = \hat { \beta } _ { U } ^ { S W } \mathrm { ) }$ . Similarly, when $\left[ \beta _ { F } \right] ^ { 2 } = \hat { \beta } _ { F } ^ { S W }$ , the planner is indifferent between the integrated and federated approaches, and when $\left[ \beta _ { U } \right] ^ { 2 } = \hat { \beta } _ { U F } ^ { S W }$ , the planner is indifferent between the unified and federated approaches.

LEMMA 3: The socially optimal interoperability approach is integrated if $\left[ \beta _ { U } \right] ^ { 2 } < \hat { \beta } _ { U } ^ { S W }$ and $\left[ \beta _ { F } \right] ^ { 2 } < \hat { \beta } _ { F } ^ { S W }$ ; unified if $\left[ \beta _ { v } \right] ^ { 2 } \geq \operatorname* { m a x } \left\{ \hat { \beta } _ { U } ^ { S W } , \hat { \beta } _ { U F } ^ { S W } \right\}$ ; and federated $i f \left[ \beta _ { U } \right] ^ { 2 } < \hat { \beta } _ { U F } ^ { S W }$ and $\left[ \beta _ { F } \right] ^ { 2 } \ge \hat { \beta } _ { F } ^ { S W }$

![](/api/attachments/75KKT4K5/fulltext/images/2fc10b6b8af061c901e8a4b049dd9c2d1be4f07f8424ccb46fa05b7e8683f568.jpg)  
Note: The blue dotted lines correspond to the equilibrium while the orange solid lines correspond to the social optimum. The shaded areas correspond to areas of misalignment between equilibrium and socially optimal interoperability approaches.

## Figure 4. Equilibrium and Socially Optimal Interoperability Approaches and Deviations

The properties of socially optimal interoperability approaches are presented in Proposition 2 and shown graphically in Figure 4.

PROPOSITION 2: (Properties of socially optimal interoperability approaches): All three interoperability approaches are possible socially optimal approaches. The social planner prefers a more centralized interoperability approach over a broader parameter region compared to the equilibrium interoperability approaches (i.e., $\hat { \beta } _ { U } ^ { S W } > \hat { \beta } _ { U } ^ { E q m }$ $\hat { \beta } _ { F } ^ { S W } > \hat { \beta } _ { F } ^ { E q m }$ , and $\hat { \beta } _ { U F } ^ { S W } < \hat { \beta } _ { U F } ^ { E q m } )$

The social planner prefers a more centralized interoperability approach over a greater range of interoperability efficiency and misfit costs, effectively our technology conditions, than the individual districts do. This result is driven by the fact that when choosing interoperability approaches, individual districts do not take the positive externality of a more centralized approach imposed on the other district into account. As a result, individual districts can end up choosing a less centralized approach than the social planner. For spectrum choice in LMR systems this means, for example, there is a broader range of interoperability efficiency where the social planner prefers both districts use the same spectrum (integrated) whereas individual districts prefer different spectra (unified and federated).

Directly comparing the socially optimal approaches with our equilibrium results, the social planner prefers integrated, but the equilibrium result is unified, when $\hat { \beta } _ { U } ^ { S W } > \left[ \beta _ { U } \right] ^ { 2 }$ > max $\left\{ \hat { \beta } _ { U } ^ { E q m } , \hat { \beta } _ { U F } ^ { E q m } \right\}$ . Similarly, the social planner prefers integrated, but the equilibrium result is federated, when $\hat { \beta } _ { F } ^ { S W } > \left[ \beta _ { F } \right] ^ { 2 } > \hat { \beta } _ { F } ^ { E q m }$ and $\left[ \beta _ { U } \right] ^ { 2 } < \operatorname* { m i n } \left\{ \hat { \beta } _ { U } ^ { S W } , \hat { \beta } _ { U F } ^ { E q m } \right\}$ . Finally, the social planner prefers unified, but the equilibrium result is federated, when $\hat { \beta } _ { v F } ^ { E q m } > \left[ \beta _ { v } \right] ^ { 2 } > \operatorname* { m a x } \left\{ \hat { \beta } _ { v } ^ { S W } , \hat { \beta } _ { v F } ^ { S W } \right\}$

Figure 4 also shows three regions of misalignment between equilibrium and socially optimal interoperability approaches (horizontally, vertically, and diagonally shaded) corresponding to the comparisons detailed above. These regions of misalignment represent the ranges in our technology conditions (Assumptions 3 and 4) under which regulatory intervention is needed.

COROLLARY 2: (Impact of misfit cost and degree of spillover on socially optimal interoperability approaches)

(i) When f increases, $\hat { \beta } _ { U } ^ { S W }$ and $\hat { \beta } _ { F } ^ { S W }$ decrease while $\hat { \beta } _ { U F } ^ { S W }$ remains unchanged. When $f _ { U }$ increases, $\hat { \beta } _ { U } ^ { S W }$ increases and both the slope and the intercept of $\hat { \beta } _ { U F } ^ { S W }$ increase, while $\hat { \beta } _ { F } ^ { S W }$ remains unchanged.

(ii) When ê increases, $\hat { \beta } _ { U } ^ { S W }$ and $\hat { \beta } _ { F } ^ { S W }$ increase while $\hat { \beta } _ { U F } ^ { S W }$ decreases.

Corollary 2 shows the impact of misfit cost and degree of spillover on the socially optimal interoperability approaches. Similar to its effects on equilibrium interoperability approaches, a higher misfit cost (increased $f _ { I } \mathrm { o r } f _ { U } )$ also leads to a less centralized approach for the social planner. Additionally, a higher degree of spillover (ê) leads to a more centralized approach for the social planner.

## Design of an Incentive Mechanism to Induce the Socially Optimal Approach

We now explore how incentive mechanisms can be deployed to induce the socially optimal interoperability approach. In our formulation, before individual districts make their decisions, the social planner designs and announces an incentive mechanism which consists of subsidies and/or taxes to the districts. To implement this, we add a Stage 0 to the game:

Stage 0: The social planner announces the incentive mechanism, that is, the planner offers a subsidy or tax $x _ { i j }$ to District $j \in \{ 1 , 2 \}$ given the resulting interoperability approach $i \in \{ I ,$ $U , F \}$

Stage 1: Each district chooses its preferred interoperability approach. The resulting interoperability approach is determined in the same way as in the equilibrium analysis.

Stage 2: Under the resulting interoperability approach $i ,$ each district chooses resources $g _ { i j }$ and interoperability effort $e _ { i j }$ to maximize the total surplus within District j 0 {1, 2}.

Recall from our collective decision-making that if two districts choose different interoperability approaches, then the least centralized approach is the result, conditional on any subsidy or tax they may receive. The solution to optimal subsidies and taxes (our incentive mechanism) to induce the socially optimal interoperability approach in our provisioning game is given in Lemma 4.

LEMMA 4: The optimal incentive mechanism with subsidy a n d t a x fo r t h e i ntegrated approach i s $\begin{array} { r } { x _ { _ { I 1 } } = - x _ { _ { I 2 } } = \frac { f _ { I } \left[ 2 - f _ { I } \right] \left[ m _ { 1 } - m _ { 2 } \right] \left[ m _ { 1 } + m _ { 2 } \right] \left[ 1 - \kappa \right] ^ { 2 } } { 8 p } } \end{array}$ , for the unified approach it is $\begin{array} { r } { x _ { _ { U 1 } } = - x _ { _ { U 2 } } = \frac { f _ { U } \left[ 2 - f _ { U } \right] \left[ m _ { 1 } - m _ { 2 } \right] \left[ m _ { 1 } + m _ { 2 } \right] \left[ 1 - \kappa \right] ^ { 2 } } { 8 p } } \end{array}$ , and for the federated approach it is $x _ { { } _ { F 1 } } = x _ { { } _ { F 2 } } = 0$

Lemma 4 specifies the optimal subsidy and tax levels offered to the two districts, which induces the socially optimal interoperability approach. In the first two situations the incentive mechanism is simply a transfer between districts to induce

District 1 to choose a more centralized approach, and this transfer is decreasing in the degree of spillover and increasing in the relevant misfit costs. In addition, from Figure 4 there is no situation in which the socially optimal approach is federated, and the equilibrium approach is integrated or unified, so no subsidy or tax is needed when the socially optimal approach is federated. It is also worth recognizing that the optimal incentive (transfer) is designed to cross the threshold values that are defined in terms of interoperability efficiency, and that the incentive depends on the misfit costs. Next, we analyze the properties of the optimal incentive mechanism with subsidy and tax. We summarize these in Proposition 3.

PROPOSITION 3: (Properties of the optimal incentive mechanism with subsidy and tax): The social planner should subsidize District 1 and tax District 2. The total incentives given to both districts in all three interoperability approaches is zero: $x _ { _ { I 1 } } + x _ { _ { I 2 } } = x _ { _ { U 1 } } + x _ { _ { U 2 } } = x _ { _ { F 1 } } + x _ { _ { F 2 } } = 0$ . To achieve t h e s o c i a l o p t i m u m , $x _ { _ { I 1 } } > x _ { _ { U 1 } } > x _ { _ { F 1 } } = 0$ a n d $x _ { _ { I 2 } } < x _ { _ { U 2 } } < x _ { _ { F 2 } } = 0$ , District 1 receives the maximum sub sidy with integrated approach while District 2 pays the minimum tax with federated approach.

Proposition 3 reveals that to achieve the social optimum the social planner should subsidize District 1 to encourage it to choose a more centralized interoperability approach. In the meantime, the social planner should tax District 2 the same amount to discourage it from choosing a more centralized approach because the result is still a less centralized approach when District 2 is the only district choosing a more centralized approach. As a result, the incentive between districts is a transfer, which means no extra funding is needed to induce the social optimum, and budget balance arises naturally from our formulation. Finally, and not surprisingly, a larger transfer in the form of a subsidy (tax) is needed for District 1 (2) under a more centralized approach.

However, taxing a district for choosing a more centralized interoperability approach may not be feasible in practice for political, legal, or other reasons. Thus, we derive the optimal incentive mechanism with a subsidy only in Lemma 5.

LEMMA 5: The optimal incentive mechanism with subsidy o n l y f o r t h e i n t e g r a t e d a p p r o a c h i s $\begin{array} { r } { x _ { I 1 } = \frac { f _ { I } \left[ 2 - f _ { I } \right] \left[ m _ { 1 } - m _ { 2 } \right] \left[ m _ { 1 } + m _ { 2 } \right] \left[ 1 - \kappa \right] ^ { 2 } } { 8 p } } \end{array}$ and $x _ { I 2 } = 0$ , for the unified a p p r o a c h i s $\begin{array} { r } { x _ { U 1 } = \frac { f _ { U } \left[ 2 - f _ { U } \right] \left[ m _ { 1 } - m _ { 2 } \right] \left[ m _ { 1 } + m _ { 2 } \right] \left[ 1 - \kappa \right] ^ { 2 } } { 8 p } } \end{array}$ a n d $\begin{array} { r } { x _ { _ { U 2 } } = \frac { \left[ f _ { I } \left[ 2 - f _ { I } \right] - f _ { U } \left[ 2 - f _ { U } \right] \right] \left[ m _ { 1 } - m _ { 2 } \right] \left[ m _ { 1 } + m _ { 2 } \right] \left[ 1 - \kappa \right] ^ { 2 } } { 8 p } } \end{array}$ , and for the federated approach is $x _ { F 1 } = 0$ and $\begin{array} { r } { x _ { F 2 } = \frac { f _ { I } \left[ 2 - f _ { I } \right] \left[ m _ { 1 } - m _ { 2 } \right] \left[ m _ { 1 } + m _ { 2 } \right] \left[ 1 - \kappa \right] ^ { 2 } } { 8 p } } \end{array}$

Lemma 5 reveals a different incentive structure when taxing a district is not allowed although similar to Lemma 4 the subsidy is decreasing in the degree of spillover and increasing in the relevant misfit costs. The properties of the optimal incentive mechanism with a subsidy only are shown in Proposition 4.

PROPOSITION 4: (Properties of the optimal incentive mechanism with a subsidy only):

(i) The social planner should subsidize District 1 for more centralized interoperability approaches and subsidize District 2 for less centralized approaches.

(ii) The total incentives given to both districts in all three interoperability approaches are the same: $x _ { I 1 } + x _ { I 2 } = x _ { U 1 } + x _ { U 2 }$ $= x _ { F 1 } + x _ { F 2 } > 0$

(iii) To achieve the social optimum, $x _ { I 1 } > x _ { U 1 } > x _ { F 1 }$ and $x _ { I 2 } <$ $x _ { U 2 } < x _ { F 2 } ,$ District 1 receives the highest level of subsidy with the integrated approach while District 2 receives the highest level of subsidy with the federated approach.

Different from the incentive mechanism with both subsidies and taxes, Proposition 4 (iii) shows that District 2 is subsidized for less centralized approaches rather than taxed for more centralized approaches, again because District 2 values the spillover more and favors more centralized approaches. The converse is true for District 1 that is subsidized for more centralized approaches because it values spillovers less. When taxes are infeasible, extra funding is needed to cover the total subsidy given to both districts and thus positive total incentives are given out.

Next, we verify whether the social gain (from inducing the socially optimal interoperability approach) exceeds the extra funding needed to support the subsidies. Lemma 6 summarizes the comparison results between the social gain and the total subsidy.

LEMMA 6: Comparing the total subsidy given to both districts with the social gain yields:

(i) When $\hat { \beta } _ { U } ^ { S W } > \left[ \beta _ { U } \right] ^ { 2 } > \operatorname* { m a x } \left\{ \hat { \beta } _ { U } ^ { E q m } , \hat { \beta } _ { U F } ^ { E q m } \right\}$ , (i.e., in the horizontally shaded area in Figure 4), the social gain is $S _ { I } ( x _ { I 1 } , x _ { I 2 } ) -$ $S _ { U } ( x _ { U 1 } , x _ { U 2 } )$ . Furthermore, the social gain is sufficient to cover the total subsidy if and only if $\big [ \beta _ { U } \big ] ^ { 2 } \leq \hat { \beta } _ { U } ^ { S G }$

(ii) When $\hat { \beta } _ { F } ^ { E q m } < \left[ \beta _ { F } \right] ^ { 2 } < \hat { \beta } _ { F } ^ { S W }$ and $\left[ \beta _ { v } \right] ^ { 2 } < \operatorname* { m i n } \left\{ \hat { \beta } _ { U } ^ { s w } , \hat { \beta } _ { U F } ^ { g q m } \right\} ( i . e .$ in the vertically shaded area in Figure 4), the social gain is

$S _ { I } ( x _ { I 1 } , x _ { I 2 } ) \ : - \ : S _ { F } ( x _ { F 1 } , x _ { F 2 } )$ . Furthermore, the social gain is sufficient to cover the total subsidy if and only if $\left[ \beta _ { F } \right] ^ { 2 } \leq \hat { \beta } _ { F } ^ { S G }$

(iii) When $\left\{ \hat { \beta } _ { U F } ^ { S W } , \hat { \beta } _ { U } ^ { S W } \right\} < \left[ \beta _ { U } \right] ^ { 2 } < \hat { \beta } _ { U F } ^ { E q m } \left( i . e . \right.$ , in the diagonally shaded area in Figure 4), the social gain is $S _ { U } ( x _ { U 1 } , x _ { U 2 } ) \textrm { - }$ $S _ { F } ( x _ { F 1 } , x _ { F 2 } )$ . Furthermore, the social gain is sufficient to cover the total subsidy if and only $i f \big [ \beta _ { U } \big ] ^ { 2 } \geq \hat { \beta } _ { U F } ^ { S G }$

Considering all three regions (horizontally, vertically, and diagonally shaded) of misalignment in Figure 4, we consolidate and compare the results in Proposition 5.

PROPOSITION 5: (Comparison between the total subsidy with subsidy only and the social gain):

Case a: $\frac { f _ { I } [ 2 - f _ { I } ] } { f _ { U } [ 2 - f _ { U } ] } \geq 2$

(a-i) The social gain is sufficient to cover the total subsidy, if max $\cdot \left\{ { \hat { \beta } } _ { U } ^ { E q m } , { \hat { \beta } } _ { U F } ^ { E q m } \right\} < \left[ \beta _ { U } \right] ^ { 2 } < { \hat { \beta } } _ { U } ^ { S G } o r { \hat { \beta } } _ { F } ^ { E q m } < \left[ \beta _ { F } \right] ^ { 2 } < { \hat { \beta } } _ { F } ^ { S G }$

(a-ii) The social gain is not sufficient to cover the total subsidy, if $\hat { \beta } _ { U } ^ { S G } < \left[ \beta _ { U } \right] ^ { 2 } < \hat { \beta } _ { U } ^ { S W }$ or $\hat { \beta } _ { F } ^ { S G } < \left[ \beta _ { F } \right] ^ { 2 } < \hat { \beta } _ { F } ^ { S W }$ or max $\left\{ \hat { \beta } _ { U F } ^ { S W } , \hat { \beta } _ { U } ^ { S W } \right\} < \left[ \beta _ { U } \right] ^ { 2 } < \hat { \beta } _ { U F } ^ { E q m }$

Case b: $\begin{array} { r } { \frac { f _ { I } \left[ 2 - f _ { I } \right] } { f _ { U } \left[ 2 - f _ { U } \right] } < 2 } \end{array}$

(b-i) The social gain is sufficient to cover the total subsidy, if $\hat { \beta } _ { F } ^ { E q m } < \left[ \beta _ { F } \right] ^ { 2 } < \hat { \beta } _ { F } ^ { S G } o r \hat { \beta } _ { { \scriptscriptstyle U F } } ^ { S G } < \left[ \beta _ { U } \right] ^ { 2 } < \hat { \beta } _ { { \scriptscriptstyle U F } } ^ { E q m }$

(b-ii) The social gain is not sufficient to cover the total s u b s i d y , i f $\left\{ \hat { \beta } _ { U } ^ { E q m } , \hat { \beta } _ { U F } ^ { E q m } \right\} < \left[ \beta _ { U } \right] ^ { 2 } < \hat { \beta } _ { U } ^ { S W }$ o r $\begin{array} { r } { \hat { \beta } _ { F } ^ { S G } < \left[ \beta _ { F } \right] ^ { 2 } < \hat { \beta } _ { F } ^ { S W } \ { o r } \ \operatorname* { m a x } \left\{ \hat { \beta } _ { U F } ^ { S W } , \hat { \beta } _ { U } ^ { S W } \right\} < \left[ \beta _ { U } \right] ^ { 2 } < \hat { \beta } _ { U F } ^ { S G } . } \end{array}$

The results from Proposition 5 are illustrated in Figures 5 and 6. In Figure 5, where differentiation is captured, the comparison pattern between the total subsidy and the social gain depends on how much the misfit costs of the integrated and unified approaches differ from each other, captured by $\frac { f _ { I } \left[ 2 - f _ { I } \right] } { f _ { U } \left[ 2 - f _ { U } \right] }$ . There are two cases: the highly differentiated-misfit cost case (Case a with $\frac { f _ { I } [ 2 - f _ { I } ] } { f _ { U } [ 2 - f _ { U } ] } \ge 2 )$ and the less differentiated-misfit cost case (Case b with $\begin{array} { r } { \frac { f _ { I } \left[ 2 - f _ { I } \right] } { f _ { U } \left[ 2 - f _ { U } \right] } < 2 ) } \end{array}$ .

Figure 6 demonstrates the technology conditions based on interoperability efficiency and misfit costs (the green shaded areas) where the social gain is sufficient to cover the total subsidy. In other words, in the parameter regions where the social gain is not sufficient to cover the total subsidy, additional funding is needed to cover the subsidies given to the districts in order to induce the socially optimum interoperability approach.

![](/api/attachments/75KKT4K5/fulltext/images/5bf1a10dd41cbac07b76d3bbe7baf3e9574f39ca5b7d4817876a4b785cbbabd8.jpg)

Figure 5. Misfit Cases  
![](/api/attachments/75KKT4K5/fulltext/images/309dd0fc7bef57701988b401f15b1658eb04b0ffd84028d0dd35df8b9636d8ca.jpg)

![](/api/attachments/75KKT4K5/fulltext/images/4d2de75c5f8e4ebbd380c5ca1c7da760c083964384c119a6d40501d39e38f010.jpg)  
Notes: The green shaded areas correspond to the parameter regions where the social gain is sufficient to cover the total subsidy.  
Figure 6. Comparison between the Total Subsidy under Incentive with Subsidy Alone and the Social Gain

## The Impact of Initial Interoperability

When facing the provision decision of a DMS, districts may have existing investment in interoperability that could apply to coordinating spillovers from other districts’ newly acquired resources. Here we examine the impact of such initial interoperability levels on the equilibrium outcomes. We denote the initial interoperability level as $I _ { 0 } \in [ 0 , 1 ]$ , which represents the interoperability level of the existing DMS for the two districts. We present individual districts’ decision problems under each of the three interoperability approaches.

Under the integrated approach, the individual district’s decision problem is

$$
\begin{array}{r l} \max S _ {l j} \left(g _ {l j}, e _ {l j}\right) & = m _ {j} \left[ \left[ 1 - \kappa \right] \left[ 1 - f _ {I} \right] g _ {l j} + \kappa \left[ I _ {0} + \frac {e _ {l j} + e _ {I J}}{\bar {e}} \right] g _ {I \setminus j} \right] \\ & \quad - p g _ {l j} ^ {2} - \delta e _ {l j} ^ {2} \end{array}
$$

Subjectto $\begin{array} { r } { 0 \le e _ { I j } \le \overline { e } , 0 \le g _ { I j } \le \overline { g } , 0 \le I _ { 0 } + \beta _ { I } \left[ \frac { e _ { I j } + e _ { I \backslash j } } { \overline { e } } \right] \le 1 } \end{array}$ , where $j = 1 , 2 .$

The spillover benefit derived from the other district’s resources is now moderated by the new interoperability level $\begin{array} { r } { \left[ I _ { 0 } + \frac { e _ { I j } + e _ { I \setminus j } } { \overline { { e } } } \right] } \end{array}$ . When existing systems are already fully interoperable $( \mathrm { i . e . , } I _ { 0 } = 1 )$ , the districts do not have any incentive to invest in additional interoperability effort $( \mathrm { i } . \mathrm { e } . , e _ { I i } = 0 )$ . When existing systems are not interoperable $( \mathrm { i . e . , } I _ { 0 } = \mathrm { 0 ) }$ , the districts’ decision problems reduce to the main model presented in the previous section.

Under the unified approach, an individual district’s decision problem is

$$
\begin{array}{r l} \max S _ {U j} \left(g _ {U j}, e _ {U j}\right) & = m _ {j} \left[ \left[ 1 - \kappa \right] \left[ 1 - f _ {U} \right] g _ {U j} + \kappa \left[ I _ {0} + \beta_ {U} \left[ \frac {e _ {U j} + e _ {U \setminus j}}{\bar {e}} \right] \right] g _ {U \setminus j} \right] \\ & \quad - p g _ {U j} ^ {2} - \delta e _ {U j} ^ {2} \end{array}
$$

Subject to $\begin{array} { r } { 0 \le e _ { U j } \le \overline { { e } } , 0 \le g _ { U j } \le \overline { { g } } , 0 \le I _ { 0 } + \beta _ { U } \left[ \frac { e _ { U j } + e _ { U \backslash j } } { \overline { { e } } } \right] \le 1 } \end{array}$ where j = 1, 2.

As before, compared to the integrated approach, interoperability effort under the unified approach is less efficient, $\beta _ { U } < 1$

Under the federated approach, an individual district’s decision problem is

$$
\begin{array}{r l} \max _ {F _ {j}} \left(g _ {F j}, e _ {F j}\right) & = m _ {j} \left[ \left[ 1 - \kappa \right] g _ {F j} + \kappa \left[ I _ {0} + \beta_ {F} \left[ \frac {e _ {F j} + e _ {F \setminus j}}{\bar {e}} \right] \right] g _ {F \setminus j} \right] \\ & - p g _ {F j} ^ {2} - \delta e _ {F j} ^ {2} \end{array}
$$

Subject to $\begin{array} { r } { 0 \leq e _ { F j } \leq \overline { { e } } , 0 \leq g _ { F j } \leq \overline { { g } } , 0 \leq I _ { 0 } + \beta _ { F } \left[ \frac { e _ { F j } + e _ { F \backslash j } } { \overline { { e } } } \right] \leq 1 } \end{array}$ where j = 1, 2.

Similar to the unified approach, the interoperability effort under the federated approach is less efficient compared to the integrated approach, $\beta _ { F } < 1$ . and the interoperability efficiency loss is more severe under the federated approach than under the unified approach, $\beta _ { F } < \beta _ { U }$

Under each interoperability approach, the districts’ choices of resources and interoperability efforts are either interior or boundary solutions. Under interoperability approach $i \in \{ I ,$ $U , F \}$ , the interior solution corresponds to $\begin{array} { r } { I _ { 0 } + \beta _ { i } \left[ { \frac { e _ { i 1 } + e _ { i 2 } } { \overline { { e } } } } \right] < 1 } \end{array}$ while the boundary solution corresponds to $\begin{array} { r } { I _ { 0 } + \beta _ { i } \left[ { \frac { e _ { i 1 } + e _ { i 2 } } { \overline { { e } } } } \right] = 1 } \end{array}$ Specifically, we find that under interoperability approach $i ,$ the interior solution is the equilibrium if $\begin{array} { r } { I _ { 0 } \leq 1 - \frac { 3 m _ { 1 } m _ { 2 } \beta _ { i } ^ { 2 } \kappa \left[ 1 - \kappa \right] \left[ 1 - f _ { i } \right] } { 2 \overline { { e } } p \delta } } \end{array}$ ; otherwise, the boundary solution is the equilibrium. Empirical evidence shows that existing DMSs suffer from low initial interoperability levels $( \mathrm { i . e . , } I _ { 0 }$ is low). Therefore, we focus on interior solutions. We summarize the impact of the initial interoperability level on equilibrium interoperability approaches in Proposition 6.

PROPOSITION 6 (Impact of initial interoperability level on equilibrium interoperability approaches): When the initial interoperability level $I _ { 0 }$ increases, both districts prefer a less centralized interoperability approach. However, the equili brium interoperability approach remains qualitatively the same for all levels of $\mathrm { \Delta } I _ { 0 } .$ That is, all three interoperability approaches are still possible equilibria; the equilibrium is still determined by District 1’s preference.

Regions of individual districts’ preferred interoperability approach are shown in Figure 7 (revised Figure 2). Compared to Figure 2, the horizontal line moves down (whereby both districts prefer the unified approach over the integrated approach in a larger parameter space); the vertical line moves left (whereby both districts prefer the federated approach over the integrated approach in a larger parameter space); and the diagonal line moves up (whereby both districts prefer the federated approach over the unified approach in a larger parameter space).

In the presence of $I _ { 0 } ,$ although the districts’ preferences for interoperability approaches shift toward a less centralized approach, the relative positions between the two districts’ preferences remain the same $( \mathrm { i . e . , ~ } \ \hat { \beta } _ { U 1 } < \hat { \beta } _ { U 2 } , \hat { \beta } _ { F 1 } < \hat { \beta } _ { F }$ and $\hat { \beta } _ { U F 1 } > \hat { \beta } _ { U F 2 } )$ . As a result, regions of the equilibrium interoperability approach remain qualitatively the same. As shown in Figure 8 (revised Figure 3), although the separating lines for equilibrium interoperability approach shift toward a less centralized approach, all three interoperability approaches are still possible equilibria and the equilibrium is still determined by District 1’s preference.

![](/api/attachments/75KKT4K5/fulltext/images/dc654a53cceec918a47e35462a7adc267f011e92536ce217a39625af4e99b47e.jpg)  
Figure 7. Individual Districts’ Preferred Interoperability Approach

![](/api/attachments/75KKT4K5/fulltext/images/616f631971b67ec4e0eb9c9e7de063350c9ba5d7395ca3db96a0c09af80fac0d.jpg)  
Figure 8. Equilibrium Interoperability Approach

## Conclusions

This work introduces an important dimension, interoperability, to the problem of DMS provision. Although in DMS a given district values resources in the other district as well as resources in its own district, this value depends on the degree to which the resources are interoperable. We use the interoperability framework developed by D. Chen et al. (2008) to identify three interoperability approaches that in decreasing order of centralization are integrated, unified, and federated. These interoperability approaches differ in their interoperability efficiency and technology misfit costs. For each approach we model cross-district interoperability of resources as a continuous feature such that efforts can be made to improve the interoperability among different districts’ resources with a cost. A unique feature of our formulation is that the interoperability approach results from collective decision-making: a more centralized approach is only obtained when districts all prefer the more centralized approach.

We find that any approach can be an equilibrium depending on interoperability efficiency, where the lower the efficiency the more centralized the equilibrium approach, and that the equilibrium is determined by preferences of the district with lesser spillover benefits. In addition, any approach can be socially optimal again depending on interoperability efficiency, and where the socially optimal approach is not the equilibrium approach, the former is more centralized. We also find that the social planner can devise a transfer (subsidy and tax) that provides incentives for districts to choose the socially optimal approach, and this transfer maintains budget balance. When a tax is not politically or otherwise acceptable, then the social planner can provide subsidies to incent districts to choose the socially optimal approach. However, this is not always welfare-maximizing in that there are circumstances where the social gain is less than the necessary subsidies. Finally, we find that if there is an initial interoperability level that applies to spillovers of newly acquired resources from other districts, all our prior results hold although the equilibrium interoperability approach shifts toward a less centralized approach.

## Implications

Our findings shed light upon alternative interoperability approaches for DMS. Our analysis reveals that although an integrated approach has the advantage of higher interoperability efficiency, it also has a disadvantage in misfit costs. These tensions between interoperability of resources when there are inter-district spillovers and the fit of resources to local needs provides an opportunity for a social planner to design an incentive mechanism, for example, subsidies and taxes, to induce districts to prefer the socially optimal interoperability approach.

Although our model set-up is based on the provision of DMS, it is sufficiently general in many aspects that it could apply to other settings. The districts in our model are entities that make up parts of a larger whole, such as counties in a state, firms in supply chain systems, or organizations in alliances. The entities make investments in resources and interoperability effort independently. There are externalities that depend on both of these investments and the interoperability approach chosen collectively reflects a level of centralization. Examples in disaster management include police forces, fire brigades, search and rescue, and forest fire management. All have resources in local jurisdictions, all have agreements in some form to support neighboring jurisdictions, and all face challenges of coordination when sharing resources.

## Limitations and Future Research

Our mathematical formulation is a stylized model where we make several critical choices. Our assumptions capture the differences in valuation of resources between districts as a single-dimension whereas aggregating preferences over DMS resources in a population may be less unidimensional. We take interoperability efficiency and misfit costs each as unidimensional and independent of district, where in reality these may not reduce to a single dimension and may vary across districts.

Our set-up also makes important functional form choices. These choices include quadratic costs, the additive nature of investments in interoperability effort, the same degree of spillovers between districts, and the linear form in which interoperability efficiency and misfit costs have their effects. These choices play a role in the tractability of our formulation, but we recognize that our results contribute to knowledge by showing what happens only when real circumstances conform fairly closely to our functional form choices. Future research could work toward generalizing the functional form choices such as different aggregations of interoperability effort and allowing for asymmetric spillovers. Our formulation also contains only two districts, allowing us to examine specific features of their interactions. Including more than two districts makes the resulting algebra opaque, thus a more general formulation without specific functional forms may yield interesting results when there are more districts.

An important implicit assumption in our modeling is that districts choose resources independently, and there is efficiency loss due to the lack of interoperability between these resources. As an alternative to subsidies or taxes based on the choice of interoperability approach, the social planner could consider incentives for matching resource types, thereby making interoperability effort more effective. Another important implicit assumption is that we start with a zero base; that is, we do not presume there are existing resources in the district which would affect choices of new resources and interoperability effort. Sensitivity to such initial conditions may be a fruitful avenue for future research.

Finally, to implement our results in a practical context requires estimating our parameters. Cost parameters such as those for resources and interoperability effort are usually straightforward to obtain. Our interoperability efficiency parameters are relative to each other, as are our misfit cost parameters. These parameters may be best estimated through questionnaire and interviews of the principals in different districts using preference assessment methods. Our resource preference parameters relate to the value at risk from disasters in the districts. It is likely that as part of their responsibilities different jurisdictions have information about this based on their disaster and public safety planning.

## Acknowledgments

We thank the Social Sciences and Humanities Research Council of Canada, (Insight Grant) and the College of Business at Northern Illinois University (MIS Faculty Research Fellowship) for financial support. We also thank Jeanette Burman for outstanding editing advice. Finally, we thank the senior editor and other members of the MIS Quarterly review team for excellent suggestions, and the conference participants at INFORMS 2017 and the seminar participants at the University of Texas at Dallas for helpful comments.

## References

Bakos, J. Y., and Nault, B. R. 1997. “Ownership and Investment in Electronic Networks,” Information Systems Research (8:4), pp. 321-341.

Bechky, B. A. 2006. “Gaffers, Gofers, and Grips: Role-Based Coordination in Temporary Organizations,” Organization Science (17:1), pp. 3-21.

Beck, T. E., and Plowman, D. A. 2014. “Temporary, Emergent Interorganizational Collaboration in Unexpected Circumstances: A Study of the Columbia Space Shuttle Response Effort,” Organization Science (25:4), pp. 1234-1252.

Besley, T., and Coate, S. 2003. “Centralized Versus Decentralized Provision of Local Public Goods: A Political Economy Approach,” Journal of Public Economics (87:12), pp. 2611-2637.

Blanchard, B. W. 2008. “Guide to Emergency Management and Related Terms, Definitions, Concepts, Acronyms, Organizations, Programs, Guidance, Executive Orders & Legislation,” Federal Emergency Management Agency, Washington, DC.

Borys, B., and Jemison, D. B. 1989. “Hybrid Arrangements as Strategic Alliances: Theoretical Issues in Organizational Combinations,” Academy of Management Review (14:2), pp. 234-249.

Chen, D., and Daclin, N. 2006. “Framework for Enterprise Interoperability,” in Interoperability for Enterprise Software and Applications: Proceedings of the Workshops and the Doctoral Symposium of the Second IFAC/IFIP I-ESA International Conference, H. Panetto and N. Boudjlida (eds.), Bordeaux, France.

Chen, D., Dassisti, M., and Elvaester, B. 2006. “Interoperability Knowledge Corpus, Intermediate Report,” Deliverable DI.1b, Network of Excellence InterOp, Contract No. IST-508011.

Chen, D., Doumeingts, G., and Vernadat, F. 2008. “Architectures for Enterprise Integration and Interoperability: Past, Present and Future,” Computers in Industry (59:7), pp. 647-659.

Chen, R., Sharman, R., Rao, H. R., and Upadhyaya, S. J. 2008. “Coordination in Emergency Response Management,” Communications of the ACM (51:5), pp. 66-73.

Chen, R., Sharman, R., Rao, H. R., and Upadhyaya, S. J. 2013. “Data Model Development for Fire Related Extreme Events: An Activity Theory Approach,” MIS Quarterly (37:1), pp. 125-147.

Chou, C., Zahedi, F. M., and Zhao, H. 2014. “Ontology-Based Evaluation of Natural Disaster Management Websites: A Multi-Stakeholder Perspective,” MIS Quarterly (38:4), pp. 997-1016.

Coase, R. H. 1937. “The Nature of the Firm,” Economica (4:16), pp. 386-405.

Coase, R. H. 2013. “The Problem of Social Cost,” The Journal of Law and Economics (56:4), pp. 837-877.

Compeau, D., and Movold, J. 2007. Waterloo Regional Police Services: Reassessing the CIMS Project. Case Study, Boston: Harvard Business School Publishing.

Currie, C. 2014. Disaster Resilience: Actions Are Underway, but Federal Fiscal Exposure Highlights the Need for Continued Attention to Longstanding Challenges, GAO-14-503T, U. S. Government Accountability Office.

DHS. 2016. “LMR101: Educating Decision Makers on LMR Technologies,” Department of Homeland Security (DHS. 2016. (https://www.cisa.gov/safecom/funding).

DeSanctis, G., and Jackson, B. M. 1994. “Coordination of Information Technology Management: Team-Based Structures and Computer-Based Communication Systems,” Journal of Management Information Systems (10:4), pp. 85-110.

Faraj, S., and Xiao, Y. 2006. “Coordination in Fast-Response Organizations,” Management Science (52:8), pp. 1155-1169.

GAO. 2009. Disaster Recovery: Experiences from Past Disasters Offer Insights for Effective Collaboration After Catastrophic Events, U.S. Government Accountability Office.

Gaukler, G. M., Ozer, O., and Hausman, W. H. 2008. “Order Progress Information: Improved Dynamic Emergency Ordering Policies,” Production and Operations Management (17:6), pp. 599-613.

Gopal, A., Sivaramakrishnan, K., Krishnan, M. S., and Mukhopadhyay, T. 2003. “Contracts in Offshore Software Development: An Empirical Analysis,” Management Science (49:12), pp. 1671-1683.

Harter, D. E., Krishnan, M. S., and Slaughter, S. 2000. “Effects of Process Maturity on Quality Cycle Time, and Effort in Software Product Development,” Management Science (46:4), pp. 451-466.

Jackson, W. 2013. “Can FirstNet Create a Truly Nationwide Public Safety Network?,” GCN Technology, Tools and Tactics for Public Sector IT (https://gcn.com/articles/2013/04/05/ firstnetnationwide-public-safety-network.aspx).

Johnson, R. 2016. “Unreliable Wireless Network Left First Responders High and Dry during Louisiana Floods,” Forbes

(https://www.forbes.com/sites/realspin/2016/08/23/unreliablewireless-network-left-first-responders-high-and-dry-during louisiana-floods/#519d3a2f4fb2).

Kamal, M. M. 2009. “A Multiple Case Study on Integrating IT Infrastructures in the Public Domain,” International Journal of Electronic Government Research (5:3), pp. 1-20.

Kellogg, K. C., Orlikowski, W. J., and Yates, J. 2006. “Life in the Trading Zone: Structuring Coordination Across Boundaries in Postbureaucratic Organizations,” Organization Science (17:1), pp. 22-44.

King, J. L. 1983. “Centralized Versus Decentralized Computing: Organizational Considerations and Management Options,” Computing Surveys (15:4), pp. 219-349.

Krishnan, M. S., Kriebel, C. H., Kekre, S., and Mukhopadhyay, T. 2000. “An Empirical Analysis of Productivity and Quality in Software Products,” Management Science (46:6), pp. 745-759.

Liu, Y., Guo, H., and Nault, B. R. 2017. “Organization of Public Safety Networks: Spillovers, Interoperability, and Participation,” Production and Operations Management (26:4), pp. 704-723.

Majchrzak, A., Jarvenpaa, S. L., and Hollingshead, A. B. 2007. “Coordinating Expertise among Emergent Groups Responding to Disasters,” Organization Science (18:1), pp. 147-161.

Majchrzak, A., and More, P. H. B. 2011. “Emergency! Web 2.0 to the Rescue,” Communications of the ACM (54:4), pp. 125-132.

Majchrzak, A., More, P. H. B. , and Faraj, S. 2012. “Transcending Knowledge Differences in Cross-Functional Teams,” Organization Science (23:4), pp. 951-970.

Manner, J. A., Newman, S., and Peha, J. M. 2010. “The FCC Plan for a Public Safety Broadband Wireless Network,” in Proceedings of the 38<sup>th</sup> Telecommunications Policy Research Conference.

Menard, C. 2012. “Hybrid Modes of Organization, Alliances, Joint Ventures, Networks, and Other ‘Strange’ Animals,” in The Handbook of Organizational Economics, R. GIbbons and J. Roberts (eds.), Princeton, NJ: Princeton University Press, pp. 1066-1108.

Nault, B. R. 1998. “Information Technology and Organization Design: Locating Decisions and Information,” Management Science (44:10), pp. 1321-1335.

NIST. 2020. “Security Analysis of First Responder Mobile and Wearable Devices,” National Institute of Standards and Technology NISTIR 8196, U.S. Department of Commerce (https://doi.org/10.6028/NIST.IR.8196).

Oates, W. E. 1972. Fiscal Federalism, New York: Harcourt Brace Jovanovich.

Okhuysen, G. A., and Eisenhardt, K. M. 2002. “Integrating Knowledge in Groups: How Formal Interventions Enable Flexibility,” Organization Science (13:4), pp. 370-386.

Peha, J. M. 2007. “How America’s Fragmented Approach to Public Safety Wastes Money and Spectrum,” Telecommunications Policy (31:10), pp. 605-618.

Pierce, L. 2012. “Organizational Structure and the Limits of Knowledge Sharing: Incentive Conflict and Agency in Car Leasing,” Management Science (58:6), pp. 1106-1121.

Ryall, M. D., and Rachelle, S. C. 2009. “Formal Contracts in the Presence of Relational Enforcement Mechanisms: Evidence from Technology Development Projects,” Management Science (55:9), pp. 906-925.

Sawyer, S., and Fedorowicz, J. 2012. “Designing Collaborative Networks: Lessons Learned from Public Safety,” IBM Center for the Business of Government.

Schuff, D., and St. Louis, R. 2001. “Centralization Vs. Decentralization of Application Software,” Communications of ACM (44:6), pp. 88-94.

Tan, Y., and Carrillo, J. 2017. “Strategic Analysis of the Agency Model for Digital Goods,” Production and Operations Management (26:4), pp. 724-741.

Thomas, K., Bergethon, P. R., and Reimer, M. 2010. “Interoperability for First Responders and Emergency Management: Definition, Need, and the Path Forward,” World Medical and Health Policy (2:3), pp. 161-166.

UNISDR. 2016. “2015 Disasters in Numbers,” United Nations Office for Disaster Risk Reduction.

Vicinanzo, A. 2014. “Interoperable Communications Show Dramatic Improvement Since 9/11, but Problems Remain,” Homeland Security Today.

Waugh, W. L., and Streib, G. 2006. “Collaboration and Leadership for Effective Emergency Management,” Public Administration Review (66:1), pp. 131-140.

Williamson, O. E. 1991. “Comparative Economic Organization: The Analysis of Discrete Structural Alternatives,” Administrative Science Quarterly (36:2), pp. 269-296.

Xue, L., Ray, G., and Gu, B. 2011. “Environmental Uncertainty and IT Infrastructure Governance: A Curvilinear Relationship,” Information Systems Research (22:2), pp. 389-399.

Xue, L., Ray, G., and Sambamurthy, V. 2012. “Efficiency or Innovation: How Do Industry Environments Moderate the Effects of Firms’ IT Asset Portfolios,” MIS Quarterly (36:2), pp. 509-528.

Zmud, R. W. 1980. “Management of Large Software Development Efforts,” MIS Quarterly (4:2), pp. 45-55.

## About the Authors

Hong Guo is Professor of IT, Analytics, and Operations at the Mendoza College of Business, University of Notre Dame. She studies emerging phenomena in IT by characterizing key design features of such systems (e.g., mobile platforms, digital games, product review systems, etc.) and examining firms’ corresponding strategies. She is also interested in economic analysis of IT policy issues such as net neutrality and public safety networks. Hong’s research has been published in top journals such as MIS Quarterly, Information Systems Research, Manufacturing & Service Operations Management, and Production and Operations Management.

Yipeng Liu is the Dean’s Outstanding Junior Professor in the Department of Operations Management and Information Systems at Northern Illinois University. His research work focus on the economic modeling of information systems. The concentration is on using analytical modeling and game theory techniques to reveal economic and social aspects of central interests in business fields. Yipeng is very active on the research topic and his research has appeared in top ranked business journals such as MIS Quarterly, Information Systems Research, Journal of Management Information Systems, and Production and Operations Management. Yipeng also serves as the Assistant Chair in the OM&IS Department.

Barrie R. Nault is Distinguished Research Professor at the University of Calgary. He has served as an IS Department editor for Management Science, and is a Distinguished Fellow of the INFORMS Information Systems Society. His research includes IT productivity; incentives and investment in networks and platforms, virtual organizations, and supply chains; public safety networks; and net neutrality. Barrie has published in Information Systems Research, MIS Quarterly, Management Science, Production and Operations Management, Strategic Management Journal, Marketing Science, and Organization Science, among others. He has held grants from the NSF in the U.S. as well as NSERC and SSHRC in Canada.

## Appendix

## Equilibrium Analysis in Stage 2

Integrated Approach: Each district maximizes their individual surplus by choice of resources $g _ { I j }$ and interoperability effort $e _ { I j } \colon$

$$
\max _ {g _ {I 1}, e _ {I 1}} S _ {I 1} = m _ {1} \left[ [ 1 - \kappa ] [ 1 - f _ {I} ] g _ {I 1} + \kappa \left[ \frac {e _ {I 1} + e _ {I 2}}{\bar {e}} \right] g _ {I 2} \right] - p g _ {I 1} ^ {2} - \delta e _ {I 1} ^ {2} \mathrm{and}
$$

$$
\max _ {g _ {I 2}, e _ {I 2}} S _ {I 2} = m _ {2} \left[ [ 1 - \kappa ] [ 1 - f _ {I} ] g _ {I 2} + \kappa \left[ \frac {e _ {I 1} + e _ {I 2}}{\bar {e}} \right] g _ {I 1} \right] - p g _ {I 2} ^ {2} - \delta e _ {I 2} ^ {2},
$$

subject to $g _ { I j } \in [ 0 , \overline { { g } } ]$ and $e _ { I j } \in [ 0 , \overline { { e } } ]$

Jointly solving for individual districts’ optimal resources and interoperability effort, and assuming interior solutions to both, yields a Nash equilibrium:

$$
g _ {I 1} = \frac {m _ {1} [ 1 - \kappa ] [ 1 - f _ {I} ]}{2 p}, g _ {I 2} = \frac {m _ {2} [ 1 - \kappa ] [ 1 - f _ {I} ]}{2 p},
$$

$$
e _ {I 1} = e _ {I 2} = \frac {m _ {1} m _ {2} \kappa [ 1 - \kappa ] [ 1 - f _ {I} ]}{4 p \delta \bar {e}}.
$$

We then compute the corresponding surplus for each district and social welfare in equilibrium:

$$
\begin{array}{r} S _ {I 1} ^ {e q m} = \frac {[ 1 - f _ {I} ] ^ {2} m _ {1} ^ {2} [ 1 - \kappa ] ^ {2} [ 4 \bar {e} ^ {2} p \delta + 3 m _ {2} ^ {2} \kappa^ {2} ]}{1 6 \bar {e} ^ {2} p ^ {2} \delta}, \\ S _ {I 2} ^ {e q m} = \frac {[ 1 - f _ {I} ] ^ {2} m _ {2} ^ {2} [ 1 - \kappa ] ^ {2} [ 4 \bar {e} ^ {2} p \delta + 3 m _ {1} ^ {2} \kappa^ {2} ]}{1 6 \bar {e} ^ {2} p ^ {2} \delta}, \\ S _ {I} ^ {e q m} = S _ {I 1} ^ {e q m} + S _ {I 2} ^ {e q m} = \frac {[ 1 - f _ {I} ] ^ {2} [ 1 - \kappa ] ^ {2} [ 2 \bar {e} ^ {2} [ m _ {1} ^ {2} + m _ {2} ^ {2} ] p \delta + 3 m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2} ]}{8 \bar {e} ^ {2} p ^ {2} \delta}. \end{array}
$$

Unified Approach: Each district maximizes their individual surplus by choice of resources $g _ { U j }$ and interoperability effort $e _ { U j }$ :

$$
\max _ {g _ {U 1}, e _ {U 1}} S _ {U 1} = m _ {1} \left[ [ 1 - \kappa ] [ 1 - f _ {U} ] g _ {U 1} + \kappa \beta_ {U} \left[ \frac {e _ {U 1} + e _ {U 2}}{\bar {e}} \right] g _ {U 2} \right] - p g _ {U 1} ^ {2} - \delta e _ {U 1} ^ {2} \mathrm{and}
$$

$$
\max _ {g _ {U 2}, e _ {U 2}} S _ {U 2} = m _ {2} \left[ [ 1 - \kappa ] [ 1 - f _ {U} ] g _ {U 2} + \kappa \beta_ {U} \left[ \frac {e _ {U 1} + e _ {U 2}}{\bar {e}} \right] g _ {U 1} \right] - p g _ {U 2} ^ {2} - \delta e _ {U 2} ^ {2},
$$

subject to $g _ { U j } \in [ 0 , \overline { { g } } ]$ and $e _ { U j } \in [ 0 , \overline { { e } } ]$

Jointly solving for individual districts’ optimal resources and interoperability effort, and assuming interior solutions to both, yields a Nash equilibrium

$$
g _ {U 1} = \frac {m _ {1} [ 1 - \kappa ] [ 1 - f _ {U} ]}{2 p}, g _ {U 2} = \frac {m _ {2} [ 1 - \kappa ] [ 1 - f _ {U} ]}{2 p},
$$

$$
e _ {U 1} = e _ {U 2} = \frac {m _ {1} m _ {2} \beta_ {U} \kappa [ 1 - \kappa ] [ 1 - f _ {U} ]}{4 p \delta \bar {e}}.
$$

We then compute the corresponding surplus for each district and social welfare in equilibrium:

$$
\begin{array}{r} S _ {U 1} ^ {e q m} = \frac {m _ {1} ^ {2} [ 1 - \kappa ] ^ {2} [ 1 - f _ {U} ] ^ {2} [ 3 m _ {2} ^ {2} \beta_ {U} ^ {2} \kappa^ {2} + 4 p \delta \bar {e} ^ {2} ]}{1 6 p ^ {2} \delta \bar {e} ^ {2}}, \\ S _ {U 2} ^ {e q m} = \frac {m _ {2} ^ {2} [ 1 - \kappa ] ^ {2} [ 1 - f _ {U} ] ^ {2} [ 3 m _ {1} ^ {2} \beta_ {U} ^ {2} \kappa^ {2} + 4 p \delta \bar {e} ^ {2} ]}{1 6 p ^ {2} \delta \bar {e} ^ {2}}, \\ S _ {U} ^ {e q m} = S _ {U 1} ^ {e q m} + S _ {U 2} ^ {e q m} = \frac {[ 1 - f _ {U} ] ^ {2} [ 1 - \kappa ] ^ {2} [ 2 \bar {e} ^ {2} [ m _ {1} ^ {2} + m _ {2} ^ {2} ] p \delta + 3 m _ {1} ^ {2} m _ {2} ^ {2} \beta_ {U} ^ {2} \kappa^ {2} ]}{8 p ^ {2} \delta \bar {e} ^ {2}}. \end{array}
$$

Federated Approach: Each district maximizes their individual surplus by choice of resources $g _ { F j }$ and interoperability effort $e _ { F j }$

$$
\max _ {g _ {F _ {1}}, e _ {F _ {1}}} S _ {F _ {1}} = m _ {1} \left[ [ 1 - \kappa ] g _ {F _ {1}} + \kappa \beta_ {F} \left[ \frac {e _ {F _ {1}} + e _ {F _ {2}}}{\bar {e}} \right] g _ {F _ {2}} \right] - p g _ {F _ {1}} ^ {2} - \delta e _ {F _ {1}} ^ {2} \mathrm{and}
$$

$$
\max _ {g _ {F 2}, e _ {F 2}} S _ {F 2} = m _ {2} \left[ [ 1 - \kappa ] g _ {F 2} + \kappa \beta_ {F} \left[ \frac {e _ {F 1} + e _ {F 2}}{\bar {e}} \right] g _ {F 1} \right] - p g _ {F 2} ^ {2} - \delta e _ {F 2} ^ {2},
$$

subject to $g _ { F j } \in [ 0 , \overline { { g } } ]$ and $e _ { F j } \in [ 0 , \overline { { e } } ]$

Jointly solving for individual districts’ optimal resources and interoperability effort, and assuming interior solutions to both, yields a Nash equilibrium

$$
g _ {F 1} = \frac {[ 1 - \kappa ] m _ {1}}{2 p}, g _ {F 2} = \frac {[ 1 - \kappa ] m _ {2}}{2 p},
$$

$$
e _ {F 1} = e _ {F 2} = \frac {\kappa \beta_ {F} [ 1 - \kappa ] m _ {1} m _ {2}}{4 \bar {e} p \delta}.
$$

We then compute the corresponding surplus for each district and social welfare in equilibrium:

$$
\begin{array}{r} S _ {F 1} ^ {e q m} = \frac {m _ {1} ^ {2} [ 1 - \kappa ] ^ {2} [ 4 \bar {e} ^ {2} p \delta + 3 m _ {2} ^ {2} \beta_ {F} ^ {2} \kappa^ {2} ]}{1 6 \bar {e} ^ {2} p ^ {2} \delta}, \\ S _ {F 2} ^ {e q m} = \frac {m _ {2} ^ {2} [ 1 - \kappa ] ^ {2} [ 4 \bar {e} ^ {2} p \delta + 3 m _ {1} ^ {2} \beta_ {F} ^ {2} \kappa^ {2} ]}{1 6 \bar {e} ^ {2} p ^ {2} \delta}, \\ S _ {F} ^ {e q m} = S _ {F 1} ^ {e q m} + S _ {F 2} ^ {e q m} = \frac {[ 1 - \kappa ] ^ {2} [ 2 \bar {e} ^ {2} [ m _ {1} ^ {2} + m _ {2} ^ {2} ] p \delta + 3 m _ {1} ^ {2} m _ {2} ^ {2} \beta_ {F} ^ {2} \kappa^ {2} ]}{8 \bar {e} ^ {2} p ^ {2} \delta}. \end{array}
$$

## Equilibrium Analysis in Stage 1

There are nine cases:

Case 1:

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">District 2</td></tr><tr><td> $t_2 = I$ </td><td> $t_2 = U$ </td><td> $t_2 = F$ </td></tr><tr><td rowspan="3">District 1</td><td> $t_1 = I$ </td><td>I  $\overline{(S_{I1}, S_{I2})}$ </td><td>U ( $S_{U1}, S_{U2}$ )</td><td>F  $\underline{(S_{F1}, S_{F2})}$ </td></tr><tr><td> $t_1 = U$ </td><td>U ( $S_{U1}, S_{U2}$ )</td><td>U ( $S_{U1}, S_{U2}$ )</td><td>F  $\underline{(S_{F1}, S_{F2})}$ </td></tr><tr><td> $t_1 = F$ </td><td>F  $\overline{(S_{F1}, S_{F2})}$ </td><td>F  $\underline{(S_{F1}, S_{F2})}$ </td><td>F  $\underline{(S_{F1}, S_{F2})}$ </td></tr></table>

Case 2:

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">District 2</td></tr><tr><td> $t_2 = I$ </td><td> $t_2 = U$ </td><td> $t_2 = F$ </td></tr><tr><td rowspan="3">District 1</td><td> $t_1 = I$ </td><td>I  $\overline{(S_{I1}, S_{I2})}$ </td><td>U ( $S_{U1}, S_{U2}$ )</td><td>F  $(S_{F1}, S_{F2})$ </td></tr><tr><td> $t_1 = U$ </td><td>U  $(S_{U1}, S_{U2})$ </td><td>U  $(S_{U1}, S_{U2})$ </td><td>F  $(S_{F1}, S_{F2})$ </td></tr><tr><td> $t_1 = F$ </td><td>F  $(S_{F1}, S_{F2})$ </td><td>F  $(S_{F1}, S_{F2})$ </td><td>F  $(S_{F1}, S_{F2})$ </td></tr></table>

Case 3:

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">District 2</td></tr><tr><td> $t_2 = I$ </td><td> $t_2 = U$ </td><td> $t_2 = F$ </td></tr><tr><td rowspan="3">District 1</td><td> $t_1 = I$ </td><td>I  $\overline{(S_{I1}, S_{I2})}$ </td><td>U  $\underline{(S_{U1}, S_{U2})}$ </td><td>F  $\underline{(S_{F1}, S_{F2})}$ </td></tr><tr><td> $t_1 = U$ </td><td>U  $\overline{(S_{U1}, S_{U2})}$ </td><td>U  $\underline{(S_{U1}, S_{U2})}$ </td><td>F  $\underline{(S_{F1}, S_{F2})}$ </td></tr><tr><td> $t_1 = F$ </td><td>F  $\overline{(S_{F1}, S_{F2})}$ </td><td>F  $\overline{(S_{F1}, S_{F2})}$ </td><td>F  $\underline{(S_{F1}, S_{F2})}$ </td></tr></table>

Case 4:

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">District 2</td></tr><tr><td> $t_2 = I$ </td><td> $t_2 = U$ </td><td> $t_2 = F$ </td></tr><tr><td rowspan="3">District 1</td><td> $t_1 = I$ </td><td> $\text{I} \overline{(S_{I1}, S_{I2})}$ </td><td> $\text{U} \underline{(S_{U1}, S_{U2})}$ </td><td> $\text{F} \underline{(S_{F1}, S_{F2})}$ </td></tr><tr><td> $t_1 = U$ </td><td> $\text{U} \underline{(S_{U1}, S_{U2})}$ </td><td> $\text{U} \underline{(S_{U1}, S_{U2})}$ </td><td> $\text{F} \underline{(S_{F1}, S_{F2})}$ </td></tr><tr><td> $t_1 = F$ </td><td> $\text{F} \overline{(S_{F1}, S_{F2})}$ </td><td> $\text{F} \overline{(S_{F1}, S_{F2})}$ </td><td> $\text{F} \underline{(S_{F1}, S_{F2})}$ </td></tr></table>

Case 5:

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">District 2</td></tr><tr><td> $t_2 = I$ </td><td> $t_2 = U$ </td><td> $t_2 = F$ </td></tr><tr><td rowspan="3">District 1</td><td> $t_1 = I$ </td><td>I ( $S_{I1},S_{I2}$ )</td><td>U  $\overline{(S_{U1},S_{U2})}$ </td><td>F  $(S_{F1},S_{F2})$ </td></tr><tr><td> $t_1 = U$ </td><td>U  $\overline{(S_{U1},S_{U2})}$ </td><td>U  $\overline{(S_{U1},S_{U2})}$ </td><td>F  $(S_{F1},S_{F2})$ </td></tr><tr><td> $t_1 = F$ </td><td>F  $\overline{(S_{F1},S_{F2})}$ </td><td>F  $\overline{(S_{F1},S_{F2})}$ </td><td>F  $\overline{(S_{F1},S_{F2})}$ </td></tr></table>

Case 6:

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">District 2</td></tr><tr><td> $t_2 = I$ </td><td> $t_2 = U$ </td><td> $t_2 = F$ </td></tr><tr><td rowspan="3">District 1</td><td> $t_1 = I$ </td><td>I ( $S_{I1},S_{I2}$ )</td><td>U ( $S_{U1},S_{U2}$ )</td><td>F ( $S_{F1},S_{F2}$ )</td></tr><tr><td> $t_1 = U$ </td><td>U ( $S_{U1},S_{U2}$ )</td><td>U ( $S_{U1},S_{U2}$ )</td><td>F ( $S_{F1},S_{F2}$ )</td></tr><tr><td> $t_1 = F$ </td><td>F ( $S_{F1},S_{F2}$ )</td><td>F ( $S_{F1},S_{F2}$ )</td><td>F ( $S_{F1},S_{F2}$ )</td></tr></table>

Case 7:

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">District 2</td></tr><tr><td> $t_2 = I$ </td><td> $t_2 = U$ </td><td> $t_2 = F$ </td></tr><tr><td rowspan="3">District 1</td><td> $t_1 = I$ </td><td> $\text{I} \overline{(S_{I1}, S_{I2})}$ </td><td> $\text{U} (S_{U1}, S_{U2})$ </td><td> $\text{F} \underline{(S_{F1}, S_{F2})}$ </td></tr><tr><td> $t_1 = U$ </td><td> $\text{U} \overline{(S_{U1}, S_{U2})}$ </td><td> $\text{U} \overline{(S_{U1}, S_{U2})}$ </td><td> $\text{F} \underline{(S_{F1}, S_{F2})}$ </td></tr><tr><td> $t_1 = F$ </td><td> $\text{F} \underline{(S_{F1}, S_{F2})}$ </td><td> $\text{F} \underline{(S_{F1}, S_{F2})}$ </td><td> $\text{F} \underline{(S_{F1}, S_{F2})}$ </td></tr></table>

Case 8:

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">District 2</td></tr><tr><td> $t_2 = I$ </td><td> $t_2 = U$ </td><td> $t_2 = F$ </td></tr><tr><td rowspan="3">District 1</td><td> $t_1 = I$ </td><td> $\text{I} \overline{(S_{I1}, S_{I2})}$ </td><td> $\text{U} (S_{U1}, S_{U2})$ </td><td> $\text{F} \underline{(S_{F1}, S_{F2})}$ </td></tr><tr><td> $t_1 = U$ </td><td> $\text{U} (S_{U1}, S_{U2})$ </td><td> $\text{U} (S_{U1}, S_{U2})$ </td><td> $\text{F} \underline{(S_{F1}, S_{F2})}$ </td></tr><tr><td> $t_1 = F$ </td><td> $\text{F} \underline{(S_{F1}, S_{F2})}$ </td><td> $\text{F} \underline{(S_{F1}, S_{F2})}$ </td><td> $\text{F} \underline{(S_{F1}, S_{F2})}$ </td></tr></table>

Case 9:

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">District 2</td></tr><tr><td> $t_2 = I$ </td><td> $t_2 = U$ </td><td> $t_2 = F$ </td></tr><tr><td rowspan="3">District 1</td><td> $t_1 = I$ </td><td>I ( $S_{I1},S_{I2}$ )</td><td>U ( $S_{U1},S_{U2}$ )</td><td>F  $\overline{(S_{F1},S_{F2})}$ </td></tr><tr><td> $t_1 = U$ </td><td>U ( $S_{U1},S_{U2}$ )</td><td>U ( $S_{U1},S_{U2}$ )</td><td>F  $\overline{(S_{F1},S_{F2})}$ </td></tr><tr><td> $t_1 = F$ </td><td>F  $\overline{(S_{F1},S_{F2})}$ </td><td>F  $\overline{(S_{F1},S_{F2})}$ </td><td>F  $\overline{(S_{F1},S_{F2})}$ </td></tr></table>

## Proof of Lemma 1

For District 1: If $[ \beta _ { U } ] ^ { 2 } < \hat { \beta } _ { U 1 }$ and $[ \beta _ { F } ] ^ { 2 } < \hat { \beta } _ { F 1 }$ , then this corresponds to the regions defined in Cases 1, 2, & 3 as shown in Figure 1. Under all three cases, the Integrated approach is preferred by District 1 as it provides higher surplus than the other two approaches, hence the Pareto efficient interoperability approach is Integrated. If $[ \beta _ { U } ] ^ { 2 } \ge m a x \{ \hat { \beta } _ { U 1 } , \hat { \beta } _ { U F 1 } \} .$ , then this corresponds to the regions defined in Cases 4 & 5 as shown in Figure 1. Under both cases, the Unified approach provides higher surplus than the other two approaches, hence the Pareto efficient interoperability approach is Unified. $\mathrm { I f } [ \beta _ { U } ] ^ { 2 } < \hat { \beta } _ { U F 1 }$ and $[ \beta _ { F } ] ^ { 2 } \ge \hat { \beta } _ { F 1 }$ , then this corresponds to the regions defined in Cases 6, 7, 8, & 9 as shown in Figure 1. Under all four cases, the Federated approach provides higher surplus than the other two approaches, hence the Pareto efficient interoperability approach is Federated.

For District 2: Similarly, $\mathrm { i f } [ \beta _ { U } ] ^ { 2 } < \hat { \beta } _ { U 2 }$ and $[ \beta _ { F } ] ^ { 2 } < \hat { \beta } _ { F 2 } $ , then this corresponds to the regions defined in Cases 1, 2, 3, 4, 7, & 8 as shown in Figure 1. Under all six cases, the Integrated approach provides higher surplus than the other two approaches, hence the Pareto efficient interoperability approach is Integrated. $\mathrm { I f } [ \beta _ { U } ] ^ { 2 } \ge m a x \{ \hat { \beta } _ { U 2 } , \hat { \beta } _ { U F 2 } \}$ , then this corresponds to the regions defined in Cases 5 & 6 as shown in Figure 1. Under both cases, the Unified approach provides higher surplus than the other two approaches, hence the Pareto efficient interoperability approach is Unified. If $[ \beta _ { U } ] ^ { 2 } < \hat { \beta } _ { U F 2 }$ and $[ \beta _ { F } ] ^ { 2 } \ge \hat { \beta } _ { F 2 } .$ , then this corresponds to the regions defined in Case 9 as shown in Figure 1. Under Case 9, the Federated approach provides higher surplus than the other two approaches, hence the Pareto efficient interoperability approach is Federated.

Lemma 1 is obtained by combing the above results for both Districts.

## Proof of Lemma 2

Lemma 2 is derived based on the definition of the equilibrium interoperability approach, which is determined by individual districts preferences. The Integrated approach is the equilibrium if and only if both districts prefer the Integrated approach. The Unified approach is the equilibrium if both districts prefer the Unified approach or one district prefers Unified but the other prefers Integrated. The Federated approach is the equilibrium if either district prefers the Federated approach.

## Proof of Proposition 1

The threshold values are given below:

$$
\hat {\beta} _ {U 1} = \frac {[ 1 - f _ {I} ] ^ {2}}{[ 1 - f _ {U} ] ^ {2}} - \frac {4 \bar {e} ^ {- 2} p \delta [ f _ {I} - f _ {U} ] [ 2 - f _ {I} - f _ {U} ]}{3 [ 1 - f _ {U} ] ^ {2} m _ {2} ^ {2} \kappa^ {2}},
$$

$$
\hat {\beta} _ {F 1} = 1 - \frac {1}{3} [ 2 - f _ {I} ] f _ {I} \left[ 3 + \frac {4 \bar {e} ^ {2} p \delta}{m _ {2} ^ {2} \kappa^ {2}} \right],
$$

$$
\hat {\beta} _ {U F 1} = \frac {1}{[ 1 - f _ {U} ] ^ {2}} \hat {\beta} _ {F 1} + \frac {4 \bar {e} ^ {2} p \delta [ 2 - f _ {U} ] f _ {U}}{3 [ 1 - f _ {U} ] ^ {2} m _ {2} ^ {2} \kappa^ {2}},
$$

$$
\hat {\beta} _ {U 2} = \frac {[ 1 - f _ {I} ] ^ {2}}{[ 1 - f _ {U} ] ^ {2}} - \frac {4 \bar {e} ^ {- 2} p \delta [ f _ {I} - f _ {U} ] [ 2 - f _ {I} - f _ {U} ]}{3 [ 1 - f _ {U} ] ^ {2} m _ {1} ^ {2} \kappa^ {2}},
$$

$$
\hat {\beta} _ {F 2} = 1 - \frac {1}{3} [ 2 - f _ {I} ] f _ {I} \left[ 3 + \frac {4 \bar {e} ^ {2} p \delta}{m _ {1} ^ {2} \kappa^ {2}} \right],
$$

$$
\hat {\beta} _ {U F 2} = \frac {1}{[ 1 - f _ {U} ] ^ {2}} \hat {\beta} _ {F 2} + \frac {4 \bar {e} ^ {2} p \delta [ 2 - f _ {U} ] f _ {U}}{3 [ 1 - f _ {U} ] ^ {2} m _ {1} ^ {2} \kappa^ {2}}.
$$

Comparing the values of the thresholds, we find:

$$
\hat {\beta} _ {U 1} <   \hat {\beta} _ {U 2}, \hat {\beta} _ {F 1} <   \hat {\beta} _ {F 2} \mathrm{and} \hat {\beta} _ {U F 1} > \hat {\beta} _ {U F 2}. (\mathrm{As} m _ {1} > m _ {2})
$$

If $\dot { \bf \Delta } [ \beta _ { U } ] ^ { 2 } < \hat { \beta } _ { U 1 } \& [ \beta _ { U } ] ^ { 2 } < \hat { \beta } _ { F 1 }$ , then both Districts prefer the Integrated approach and Integrated is the equilibrium.

If $[ \beta _ { U } ] ^ { 2 } > \hat { \beta } _ { U 1 } \& [ \beta _ { U } ] ^ { 2 } > \hat { \beta } _ { U F 1 }$ , then District 1 prefers the Unified approach, District 2 prefers either the Integrated $( \mathrm { i . e . , } \hat { \beta } _ { U 1 } < [ \beta _ { U } ] ^ { 2 } <$ $\hat { \beta } _ { U 2 } )$ or Unified approach $( \mathrm { i } . \mathrm { e } . , [ \beta _ { U } ] ^ { 2 } > \hat { \beta } _ { U 2 } )$ . By definition Unified is the equilibrium.

$\mathrm { I f } [ \beta _ { U } ] ^ { 2 } > \hat { \beta } _ { F 1 } \& [ \beta _ { U } ] ^ { 2 } < \hat { \beta } _ { U F 1 }$ , then District 1 prefers the Federated approach. By definition Federated is the equilibrium.

Based on the above, the Pareto efficient equilibrium is determined by District 1’s preferences only. Henc $\hat { \beta } _ { U } ^ { E q m } = \hat { \beta } _ { U 1 } , \hat { \beta } _ { F } ^ { E q m } = \hat { \beta } _ { F 1 }$ , and $\hat { \beta } _ { U F } ^ { E q m } = \hat { \beta } _ { U F 1 }$

## Proof of Corollary 1

Comparative statics of $f _ { I }$ and $f _ { U } \colon$

$$
\frac {\partial \widehat {\beta} _ {U} ^ {E q m}}{\partial f _ {I}} = - \frac {2 [ 1 - f _ {I} ] [ 4 \bar {e} ^ {2} p \delta + 3 m _ {2} ^ {2} \kappa^ {2} ]}{3 [ 1 - f _ {U} ] ^ {2} m _ {2} ^ {2} \kappa^ {2}} <   0,
$$

$$
\frac {\partial \widehat {\beta} _ {U} ^ {E q m}}{\partial f _ {U}} = \frac {2 [ 1 - f _ {I} ] ^ {2} [ 4 \bar {e} ^ {2} p \delta + 3 m _ {2} ^ {2} \kappa^ {2} ]}{3 [ 1 - f _ {U} ] ^ {3} m _ {2} ^ {2} \kappa^ {2}} > 0,
$$

$$
\frac {\partial \widehat {\beta} _ {F} ^ {E q m}}{\partial f _ {I}} = - \frac {2}{3} [ 1 - f _ {I} ] \left[ 3 + \frac {4 \bar {e} ^ {2} p \delta}{m _ {2} ^ {2} \kappa^ {2}} \right] <   0,
$$

$$
\frac {\partial \widehat {\beta} _ {F} ^ {E q m}}{\partial f _ {U}} = 0,
$$

$$
\frac {\partial \widehat {\beta} _ {U F} ^ {E q m}}{\partial f _ {I}} = 0.
$$

The slope of $\hat { \beta } _ { U F } ^ { E q m } \ \mathrm { i s } \frac { 1 } { [ 1 - f _ { U } ] ^ { 2 } }$ , which increases with the increase of $f _ { U }$ .

The intercept o $\begin{array} { r } { \cdot \hat { \beta } _ { U F } ^ { E q m } \mathrm { ~ i s ~ } \frac { 4 \bar { e } ^ { 2 } p \delta \left[ 2 - f _ { U } \right] f _ { U } } { 3 \left[ 1 - f _ { U } \right] ^ { 2 } m { _ 2 } ^ { 2 } \kappa ^ { 2 } } \mathrm { a n d } \frac { \partial \frac { 4 \bar { e } ^ { 2 } p \delta \left[ 2 - f _ { U } \right] f _ { U } } { 3 \left[ 1 - f _ { U } \right] ^ { 2 } m { _ 2 } ^ { 2 } \kappa ^ { 2 } } } { \partial f _ { U } } = \frac { 8 \bar { e } ^ { 2 } p \delta } { 3 \left[ 1 - f _ { U } \right] ^ { 3 } m { _ 2 } ^ { 2 } \kappa ^ { 2 } } > 0 . } \end{array}$

Based on the signs of the comparative statics above, we obtain results about the impact of $\cdot _ { f _ { I } }$ and $f _ { U }$ as reported in Corollary 1(i).

Comparative statics of <sub>??</sub>:

$$
\frac {\partial \widehat {\beta} _ {U} ^ {E q m}}{\partial \kappa} = \frac {8 \bar {e} ^ {2} p \delta [ 2 - f _ {I} - f _ {U} ]}{3 [ 1 - f _ {U} ] ^ {2} m _ {2} ^ {2} \kappa^ {3}} > 0,
$$

$$
\frac {\partial \widehat {\beta} _ {F} ^ {E q m}}{\partial \kappa} = \frac {8 \bar {e} ^ {2} p \delta [ 2 - f _ {I} ]}{3 m _ {2} ^ {2} \kappa^ {3}} > 0,
$$

$$
\frac {\partial \widehat {\beta} _ {U F} ^ {E q m}}{\partial \kappa} = - \frac {8 \bar {e} ^ {2} p \delta [ 2 - f _ {U} ] f _ {U}}{3 [ 1 - f _ {U} ] ^ {2} m _ {2} ^ {2} \kappa^ {3}} <   0.
$$

Based on the signs of the comparative statics above, we obtain results about the impact of <sub>??</sub> as reported in Corollary 1(ii).

## Proof of Lemma 3

The socially optimal interoperability approach is obtained by comparing social welfare across the three approaches. The social welfare of each interoperability approach is given below:

Integrated Approach:

$$
\mathrm{SW} _ {I} = S _ {I 1} + S _ {I 2} = \frac {[ 1 - f _ {I} ] ^ {2} [ 1 - \kappa ] ^ {2} [ 2 \bar {e} ^ {2} [ m _ {1} ^ {2} + m _ {2} ^ {2} ] p \delta + 3 m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2} ]}{8 \bar {e} ^ {2} p ^ {2} \delta}.
$$

Unified Approach:

$$
\mathrm{SW} _ {U} = S _ {U 1} + S _ {U 2} = \frac {[ 1 - f _ {U} ] ^ {2} [ 1 - \kappa ] ^ {2} [ 2 \bar {e} ^ {2} [ m _ {1} ^ {2} + m _ {2} ^ {2} ] p \delta + 3 m _ {1} ^ {2} m _ {2} ^ {2} \beta_ {U} ^ {2} \kappa^ {2} ]}{8 \bar {e} ^ {2} p ^ {2} \delta}.
$$

Federated Approach:

$$
\mathrm{SW} _ {F} = S _ {F 1} + S _ {F 2} = \frac {[ 1 - \kappa ] ^ {2} [ 2 \bar {e} ^ {2} [ m _ {1} ^ {2} + m _ {2} ^ {2} ] p \delta + 3 m _ {1} ^ {2} m _ {2} ^ {2} \beta_ {F} ^ {2} \kappa^ {2} ]}{8 \bar {e} ^ {2} p ^ {2} \delta}.
$$

$\hat { \beta } _ { U } ^ { S W }$ is obtained by comparing $\mathrm { S W } _ { I }$ and $\operatorname { S W } _ { U }$ (i.e., solve for $[ \beta _ { U } ] ^ { 2 }$ such that $\mathrm { S W } _ { I } = \mathrm { S W } _ { U } ) ;$

$$
\hat {\beta} _ {U} ^ {S W} = \frac {3 [ 1 - f _ {I} ] ^ {2} + \frac {2 \bar {e} ^ {2} [ f _ {I} - f _ {U} ] [ f _ {I} + f _ {U} - 2 ] [ m _ {1} ^ {2} + m _ {2} ^ {2} ] p \delta}{m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}}}{3 [ 1 - f _ {U} ] ^ {2}}.
$$

$\hat { \beta } _ { F } ^ { S W } \mathrm { i }$ s obtained by comparing $\mathrm { S W } _ { I }$ and $\mathsf { S W } _ { F }$ (i.e., solve for $[ \beta _ { F } ] ^ { 2 }$ such that $\mathsf { S W } _ { I } = \mathsf { S W } _ { F } )$

$$
\hat {\beta} _ {F} ^ {S W} = 1 - \frac {1}{3} [ 2 - f _ {I} ] f _ {I} \left[ 3 + \frac {2 \bar {e} ^ {2} [ m _ {1} ^ {2} + m _ {2} ^ {2} ] p \delta}{m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}} \right].
$$

$\hat { \beta } _ { U F } ^ { S W }$ is obtained by comparing $\operatorname { S W } _ { U }$ and $\mathsf { S W } _ { F }$ (i.e., solve for $[ \beta _ { U } ] ^ { 2 }$ such that $\mathsf { S W } _ { U } = \mathsf { S W } _ { F } )$

$$
\hat {\beta} _ {U F} ^ {S W} = \frac {3 \beta_ {F} ^ {2} + \frac {2 \bar {e} ^ {2} [ 2 - f _ {U} ] f _ {U} [ m _ {1} ^ {2} + m _ {2} ^ {2} ] p \delta}{m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}}}{3 [ 1 - f _ {U} ] ^ {2}}.
$$

If $[ \beta _ { U } ] ^ { 2 } < \hat { \beta } _ { U } ^ { S W }$ and $[ \beta _ { F } ] ^ { 2 } < \hat { \beta } _ { F } ^ { S W }$ , then $\mathrm { S W } _ { I } > \mathrm { S W } _ { U }$ and $\mathrm { S W } _ { I } > \mathrm { S W } _ { F }$ , indicating that the socially optimal approach is Integrated. $\mathrm { I f } [ \beta _ { U } ] ^ { 2 } \ge \operatorname* { m a x } \{ \hat { \beta } _ { U } ^ { S W } , \hat { \beta } _ { U F } ^ { S W } \}$ , then $\mathrm { S W } _ { I } < \mathrm { S W } _ { U }$ and $\mathrm { S W } _ { F } < \mathrm { S W } _ { U }$ , indicating that the socially optimal approach is Unified.

$\mathrm { I f } [ \beta _ { U } ] ^ { 2 } < \hat { \beta } _ { U F } ^ { S W }$ and $[ \beta _ { F } ] ^ { 2 } \ge \hat { \beta } _ { F } ^ { S W }$ , then $\mathsf { S W } _ { U } < \mathsf { S W } _ { F }$ and $\mathrm { S W } _ { I } < \mathrm { S W } _ { F }$ , indicating that the socially optimal approach is Federated.

## Proof of Proposition 2

The results are obtained by comparing $\hat { \beta } _ { U } ^ { S W }$ with $\hat { \beta } _ { U } ^ { E q m } , \hat { \beta } _ { F } ^ { S W }$ with $\hat { \beta } _ { F } ^ { E q m }$ , and $\hat { \beta } _ { U F } ^ { S W }$ with $\hat { \beta } _ { U F } ^ { E q m }$

$$
\hat {\beta} _ {U} ^ {E q m} = \frac {3 [ 1 - f _ {I} ] ^ {2} + \frac {4 \bar {\epsilon} ^ {2} [ f _ {I} - f _ {U} ] [ f _ {I} + f _ {U} - 2 ] p \delta}{m _ {2} ^ {2} \kappa^ {2}}}{3 [ 1 - f _ {U} ] ^ {2}},
$$

$$
\hat {\beta} _ {F} ^ {E q m} = 1 - \frac {1}{3} [ 2 - f _ {I} ] f _ {I} \left[ 3 + \frac {4 \bar {e} ^ {2} p \delta}{m _ {2} ^ {2} \kappa^ {2}} \right],
$$

$$
\hat {\beta} _ {U F} ^ {E q m} = \frac {3 \beta_ {F} ^ {2} + \frac {2 \bar {e} ^ {2} [ 2 - f _ {U} ] f _ {U} [ m _ {1} ^ {2} + m _ {2} ^ {2} ] p \delta}{m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}}}{3 [ 1 - f _ {U} ] ^ {2}}.
$$

Comparing the socially optimal thresholds with equilibrium thresholds we obtain

$$
\hat {\beta} _ {U} ^ {S W} - \hat {\beta} _ {U} ^ {E q m} = \frac {2 \bar {e} ^ {2} [ f _ {I} - f _ {U} ] [ 2 - f _ {I} - f _ {U} ] [ m _ {1} ^ {2} - m _ {2} ^ {2} ] p \delta}{3 [ 1 - f _ {U} ] ^ {2} m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}} > 0,
$$

$$
\hat {\beta} _ {F} ^ {S W} - \hat {\beta} _ {F} ^ {E q m} = \frac {2 \bar {e} ^ {2} [ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] p \delta}{3 m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}} > 0,
$$

$$
\hat {\beta} _ {U F} ^ {S W} - \hat {\beta} _ {U F} ^ {E q m} = - \frac {2 \bar {e} ^ {2} [ 2 - f _ {U} ] f _ {U} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] p \delta}{3 [ 1 - f _ {U} ] ^ {2} m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}} <   0.
$$

From the above, we obtain $\hat { \beta } _ { U } ^ { S W } > \hat { \beta } _ { U } ^ { E q m } , \hat { \beta } _ { F } ^ { S W } > \hat { \beta } _ { F } ^ { E q m }$ , and $\hat { \beta } _ { U F } ^ { S W } < \hat { \beta } _ { U F } ^ { E q m }$

## Proof of Corollary 2

Comparative statics of $f _ { I }$ and $f _ { U }$ on the socially optimal interoperability approaches:

$$
\frac {\partial \widehat {\beta} _ {U} ^ {S W}}{\partial f _ {I}} = - \frac {2 [ 1 - f _ {I} ] [ 2 \bar {e} ^ {2} p \delta [ m _ {1} ^ {2} + m _ {2} ^ {2} ] + 3 m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2} ]}{3 [ 1 - f _ {U} ] ^ {2} m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}} <   0,
$$

$$
\frac {\partial \widehat {\beta} _ {U} ^ {S W}}{\partial f _ {U}} = \frac {2 [ 1 - f _ {I} ] ^ {2} [ 2 \bar {e} ^ {2} p \delta [ m _ {1} ^ {2} + m _ {2} ^ {2} ] + 3 m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2} ]}{3 [ 1 - f _ {U} ] ^ {3} m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}} > 0,
$$

$$
\frac {\partial \widehat {\beta} _ {F} ^ {S W}}{\partial f _ {I}} = - \frac {2}{3} [ 1 - f _ {I} ] \left[ 3 + \frac {2 \bar {e} ^ {2} p \delta [ m _ {1} ^ {2} + m _ {2} ^ {2} ]}{m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}} \right] <   0,
$$

$$
\frac {\partial \widehat {\beta} _ {F} ^ {S W}}{\partial f _ {U}} = 0,
$$

$$
\frac {\partial \widehat {\beta} _ {U F} ^ {S W}}{\partial f _ {I}} = 0.
$$

The slope of $\hat { \beta } _ { U F } ^ { S W } \mathrm { i s } \frac { 1 } { [ 1 - f _ { U } ] ^ { 2 } }$ , which increases with the increase of $f _ { U }$ .

$$
\mathrm{e} \mathrm{interceptof} \hat {\beta} _ {U F} ^ {S W} \mathrm{is} \frac {2 \bar {e} ^ {2} p \delta f _ {U} [ 2 - f _ {U} ] [ m _ {1} ^ {2} + m _ {2} ^ {2} ]}{3 [ 1 - f _ {U} ] ^ {2} m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}} \mathrm{and} \frac {\partial^ {\frac {2 \bar {e} ^ {2} p \delta f _ {U} [ 2 - f _ {U} ] [ m _ {1} ^ {2} + m _ {2} ^ {2} ]}{3 [ 1 - f _ {U} ] ^ {2} m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}}}}{\partial f _ {U}} = \frac {4 \bar {e} ^ {2} p \delta [ m _ {1} ^ {2} + m _ {2} ^ {2} ]}{3 [ 1 - f _ {U} ] ^ {3} m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}} > 0.
$$

Based on the signs of the comparative statics above, we obtain the results about the impact of $f _ { I }$ and $f _ { U }$ as reported in Corollary 2(i).

Comparative statics of <sub>??</sub> on the socially optimal interoperability approaches:

$$
\frac {\partial \widehat {\beta} _ {U} ^ {S W}}{\partial \kappa} = \frac {4 \bar {e} ^ {2} p \delta [ f _ {I} - f _ {U} ] [ 2 - f _ {I} - f _ {U} ] [ m _ {1} ^ {2} + m _ {2} ^ {2} ]}{3 [ 1 - f _ {U} ] ^ {2} m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {3}} > 0,
$$

$$
\frac {\partial \widehat {\beta} _ {F} ^ {S W}}{\partial \kappa} = \frac {4 \bar {e} ^ {2} p \delta f _ {I} [ 2 - f _ {I} ] [ m _ {1} ^ {2} + m _ {2} ^ {2} ]}{3 m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {3}} > 0,
$$

$$
\frac {\partial \widehat {\beta} _ {U F} ^ {S W}}{\partial \kappa} = - \frac {4 \bar {e} ^ {2} p \delta f _ {U} [ 2 - f _ {U} ] [ m _ {1} ^ {2} + m _ {2} ^ {2} ]}{3 [ 1 - f _ {U} ] ^ {2} m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {3}} <   0.
$$

Based on the signs of the comparative statics above, we obtain the results about the impact of <sub>??</sub> as reported in Corollary 2(ii).

## Proof of Lemma 4

A social planner should find the optimal incentive mechanism that achieves social optimum while minimizing the total administrative effort under the federated approach. That is

$$
\min _ {x _ {i j}} [ | x _ {F 1} | + | x _ {F 2} | ].
$$

The incentive mechanism must satisfy the following conditions:

$$
x _ {I 1} - x _ {F 1} = \frac {[ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p},
$$

$$
x _ {U 1} - x _ {F 1} = \frac {[ 2 - f _ {U} ] f _ {U} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p},
$$

$$
x _ {I 2} - x _ {F 2} = - \frac {[ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p},
$$

$$
x _ {U 2} - x _ {F 2} = - \frac {[ 2 - f _ {U} ] f _ {U} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p}.
$$

When both tax and subsidy are available to a social planner, a district shall receive no tax as a penalty nor subsidy as an incentive if the choose the Federated approach $( { \mathrm { i . e . , } } x _ { F 1 } = x _ { F 2 } = 0 )$ . This way the social planner avoids its involvement as much as possible. As for any non-zero tax/subsidy, a social planner must rely on extra funds or incur extra expenses to induce the social optimum, which is not desirable. Given that $x _ { F 1 } = x _ { F 2 } = 0$ , we solve for the amount of tax/subsidy given to each district.

$$
x _ {I 1} = \frac {[ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p} > 0,
$$

$$
x _ {U 1} = \frac {[ 2 - f _ {U} ] f _ {U} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p} > 0,
$$

$$
x _ {I 2} = - x _ {I 1} = - \frac {[ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p} <   0,
$$

$$
x _ {U 2} = - x _ {U 1} \frac {[ 2 - f _ {U} ] f _ {U} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p} <   0.
$$

## Proof of Proposition 3

Based on the results in Lemma $^ { 4 , }$ we have:

$$
\begin{array}{r l} & x _ {I 1} + x _ {I 2} = \frac {[ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p} - \frac {[ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p} = 0, \\ & x _ {U 1} + x _ {U 2} = \frac {[ 2 - f _ {U} ] f _ {U} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p} - \frac {[ 2 - f _ {U} ] f _ {U} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p} = 0. \end{array}
$$

$$
x _ {F 1} + x _ {F 2} = 0 + 0 = 0
$$

Because $1 > f _ { I } > f _ { U } > 0$ , simple algebra indicates $[ 2 - f _ { I } ] f _ { I } > [ 2 - f _ { U } ] f _ { U }$ , hence we have $x _ { I 1 } > x _ { U 1 } > x _ { F 1 } = 0$ and $x _ { I 2 } < x _ { U 2 } < x _ { F 2 } =$ 0.

## Proof of Lemma 5

To induce the social optimum, the incentive mechanism must satisfy the same conditions as shown in the proof of Lemma 4. When a subsid is the only available incentive mechanism, a social planner should find the optimal incentive mechanism that achieves social optimum while minimizing the total incentives provided to both districts under all three approaches. That is

$$
\min _ {x _ {i j}} [ x _ {I 1} + x _ {I 2} + x _ {U 1} + x _ {U 2} + x _ {F 1} + x _ {F 2} ]
$$

Subject to:

$$
x _ {I 1} - x _ {F 1} = \frac {[ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p}
$$

$$
x _ {U 1} - x _ {F 1} = \frac {[ 2 - f _ {U} ] f _ {U} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p}
$$

$$
x _ {I 2} - x _ {F 2} = - \frac {[ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p}
$$

$$
x _ {U 2} - x _ {F 2} = - \frac {[ 2 - f _ {U} ] f _ {U} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p}
$$

$$
x _ {I 1}, x _ {I 2}, x _ {U 1}, x _ {U 2}, x _ {F 1}, x _ {F 2} \geq 0.
$$

Solving the above minimization problem leads to the solutions we reported in Lemma 5:

$$
x _ {I 1} = \frac {[ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p},
$$

$$
x _ {I 2} = 0,
$$

$$
x _ {U 1} = \frac {[ 2 - f _ {U} ] f _ {U} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p},
$$

$$
x _ {U 2} = \frac {\big [ [ 2 - f _ {I} ] f _ {I} - [ 2 - f _ {U} ] f _ {U} \big ] [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p},
$$

$$
x _ {F 1} = 0,
$$

$$
x _ {F 2} = \frac {[ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p}.
$$

## Proof of Proposition 4

(i) is obtained based on the results we obtained in Lemma 5: i.e., $x _ { I 1 } > 0 , x _ { U 1 } > 0 , x _ { F 1 } = 0$ , and $x _ { F 2 } > 0 , \ x _ { U 2 } > 0 , \ x _ { I 2 } = 0 \ / $

(ii) is obtained based on the following:

$$
x _ {I 1} + x _ {I 2} = \frac {[ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p} > 0,
$$

$$
x _ {U 1} + x _ {U 2} = \frac {[ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p} > 0,
$$

$$
x _ {F 1} + x _ {F 2} = \frac {[ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p} > 0.
$$

And hence $x _ { I 1 } + x _ { I 2 } = x _ { U 1 } + x _ { U 2 } = x _ { F 1 } + x _ { F 2 } > 0 .$

(iii) Given that $0 < f _ { U } < f _ { I } < 1$ , simple calculation indicates $x _ { I 1 } > x _ { U 1 } > x _ { F 1 } = 0 \mathrm { a n d } x _ { F 2 } > x _ { U 2 } > x _ { I 2 } = 0$

## Proof of Lemma 6 and Proposition 5

Total subsidy needed for each approach to induce social optimum is given by:

$$
x _ {I 1} + x _ {I 2} = x _ {U 1} + x _ {U 2} = x _ {F 1} + x _ {F 2} = \frac {[ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] [ 1 - \kappa ] ^ {2}}{8 p}.
$$

We compare this amount to the social gain and see if a subsidy can be justified.

Case 1: When the social optimum is Integrated, but the equilibrium is Unified (the horizontally shaded area in Figure 4), the social gain is given by:

$$
S _ {I} (x _ {I 1}, x _ {I 2}) - S _ {U} (x _ {U 1}, x _ {U 2}) = \frac {[ 1 - \kappa ] ^ {2} [ 2 \bar {e} ^ {2} [ f _ {I} - f _ {U} ] [ f _ {I} + f _ {U} - 2 ] [ m _ {1} ^ {2} + m _ {2} ^ {2} ] p \delta + 3 m _ {1} ^ {2} m _ {2} ^ {2} [ [ 1 - f _ {I} ] ^ {2} - [ 1 - f _ {U} ] ^ {2} \beta_ {U} ^ {2} ] \kappa^ {2} ]}{8 \bar {e} ^ {2} p ^ {2} \delta}.
$$

The separating thresholds for the cost effectiveness of the incentive mechanism is obtained by comparing the social gain with the total subsidy:

$$
\hat {\beta} _ {U} ^ {S G} = \frac {3 [ 1 - f _ {I} ] ^ {2} + \frac {\bar {e} ^ {2} p \delta \left[ [ 3 [ f _ {I} - 2 ] f _ {I} - 2 [ f _ {U} - 2 ] f _ {U} ] m _ {1} ^ {2} + \left[ [ f _ {I} - 2 ] f _ {I} - 2 [ f _ {U} - 2 ] f _ {U} \right] m _ {2} ^ {2} \right]}{m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}}}{3 [ 1 - f _ {U} ] ^ {2}},
$$

$$
S _ {I} (x _ {I 1}, x _ {I 2}) - S _ {U} (x _ {U 1}, x _ {U 2}) > x _ {I 1} + x _ {I 2} \mathrm{if} [ \beta_ {U} ] ^ {2} <   \hat {\beta} _ {U} ^ {S G}
$$

To show that the social gain is enough to cover the total subsidy, we need to show $[ \beta _ { U } ] ^ { 2 } < \hat { \beta } _ { U } ^ { S G }$ of all valid values of $[ \beta _ { U } ] ^ { 2 }$ within the horizontally shaded area of Figure 4. The necessary and sufficient condition for $[ \beta _ { U } ] ^ { 2 } < \hat { \beta } _ { U } ^ { S G }$ is to show that $\hat { \beta } _ { U } ^ { S G } > \hat { \beta } _ { U } ^ { S W }$ :

$$
\hat {\beta} _ {U} ^ {S G} - \hat {\beta} _ {U} ^ {S W} = - \frac {\bar {e} ^ {2} [ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] p \delta}{3 [ 1 - f _ {U} ] ^ {2} m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}} <   0.
$$

This indicates that the social gain cannot justify the total subsidy for all valid values of $[ \beta _ { U } ] ^ { 2 }$ . To see if the social gain is enough to justify a portion of the horizontally shaded area in Figure 4, we then compare $\hat { \beta } _ { U } ^ { S G }$ with $\hat { \beta } _ { U } ^ { E q m }$ :

$$
\hat {\beta} _ {U} ^ {S G} - \hat {\beta} _ {U} ^ {E q m} = \frac {\bar {e} ^ {2} \big [ [ 2 - f _ {I} ] f _ {I} - 2 [ 2 - f _ {U} ] f _ {U} \big ] [ m _ {1} ^ {2} - m _ {2} ^ {2} ] p \delta}{3 [ 1 - f _ {U} ] ^ {2} m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}}
$$

$\hat { \beta } _ { U } ^ { S G } - \hat { \beta } _ { U } ^ { E q m } \ge 0 \mathrm { ~ i f ~ } [ 2 - f _ { I } ] f _ { I } - 2 [ 2 - f _ { U } ] f _ { U } \ge 0 ,$ , otherwise $\hat { \beta } _ { U } ^ { S G } - \hat { \beta } _ { U } ^ { E q m } < 0 .$

$\begin{array} { r } { \mathrm { I f } { \frac { f _ { I } [ 2 - f _ { I } ] } { f _ { U } [ 2 - f _ { U } ] } } \geq 2 } \end{array}$ , then $\hat { \beta } _ { U } ^ { E q m } < \hat { \beta } _ { U } ^ { S G } < \hat { \beta } _ { U } ^ { S W }$ , this in turn indicates that within the horizontally shaded region, total subsidy can be justified by social gain if $\dot { \rho } _ { U } ^ { E q m } < [ \beta _ { U } ] ^ { 2 } < \hat { \beta } _ { U } ^ { S G }$ . Otherwise, total subsidy cannot be justified by social gain.

Case 2: When social optimum is Integrated, but the equilibrium is Federated (the vertically shaded area in Figure 4), the social gain is given by:

$$
S _ {I} (x _ {I 1}, x _ {I 2}) - S _ {F} (x _ {F 1}, x _ {F 2}) = \frac {[ 1 - \kappa ] ^ {2} [ 2 \bar {e} ^ {2} [ f _ {I} - 2 ] [ m _ {1} ^ {2} + m _ {2} ^ {2} ] p \delta + 3 m _ {1} ^ {2} m _ {2} ^ {2} [ [ 1 - f _ {I} ] ^ {2} - \beta_ {F} ^ {2} ] \kappa^ {2} ]}{8 \bar {e} ^ {2} p ^ {2} \delta}.
$$

The separating thresholds for the cost effectiveness of the incentive mechanism is obtained by comparing the social gain with the total subsidy:

$$
\hat {\beta} _ {F} ^ {S G} = 1 - \frac {1}{3} [ 2 - f _ {I} ] f _ {I} \left[ 3 + \frac {\bar {e} ^ {2} [ 3 m _ {1} ^ {2} + m _ {2} ^ {2} ] p \delta}{m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}} \right]
$$

$$
S _ {I} (x _ {I 1}, x _ {I 2}) - S _ {F} (x _ {F 1}, x _ {F 2}) > x _ {F 1} + x _ {F 2} \mathrm{if} [ \beta_ {F} ] ^ {2} <   \hat {\beta} _ {F} ^ {S G}.
$$

To show that the social gain is enough to cover the total subsidy, we need to show $[ \beta _ { F } ] ^ { 2 } < \hat { \beta } _ { F } ^ { S G }$ for all valid values of $[ \beta _ { F } ] ^ { 2 }$ within the vertically shaded area of Figure 4. The necessary and sufficient condition for $[ \beta _ { F } ] ^ { 2 } < \hat { \beta } _ { F } ^ { S G }$ is to show that $\hat { \beta } _ { F } ^ { S G } > \hat { \beta } _ { F } ^ { S W }$

$$
\hat {\beta} _ {F} ^ {S G} - \hat {\beta} _ {F} ^ {S W} = - \frac {\bar {e} ^ {2} [ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] p \delta}{3 m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}} <   0.
$$

This indicates that the social gain cannot justify the total subsidy for all values of $[ \beta _ { F } ] ^ { 2 }$ . To see if the social gain is enough to justify a portion of the vertically shaded area in Figure 4, we then compare $\hat { \beta } _ { F } ^ { S G }$ with $\hat { \beta } _ { F } ^ { E q m }$ :

$$
\hat {\beta} _ {F} ^ {S G} - \hat {\beta} _ {F} ^ {E q m} = \frac {\bar {e} ^ {2} [ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] p \delta}{3 m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}} > 0.
$$

The above results suggest $\hat { \beta } _ { F } ^ { E q m } < \hat { \beta } _ { F } ^ { S G } < \hat { \beta } _ { F } ^ { S W }$ is always true. As a result, if $\hat { \beta } _ { F } ^ { E q m } < [ \beta _ { F } ] ^ { 2 } < \hat { \beta } _ { F } ^ { S G }$ , then the social gain is sufficient to cover the total subsidy, otherwise the social gain is not sufficient to cover the total subsidy.

Case 3: When social optimum is Unified, but the equilibrium is Federated (the diagonally shaded area in Figure 4), the social gain is given by:

$$
S _ {U} (x _ {U 1}, x _ {U 2}) - S _ {F} (x _ {F 1}, x _ {F 2}) = \frac {[ 1 - \kappa ] ^ {2} [ 2 \bar {e} ^ {2} [ f _ {U} - 2 ] f _ {U} [ m _ {1} ^ {2} + m _ {2} ^ {2} ] p \delta + 3 m _ {1} ^ {2} m _ {2} ^ {2} [ [ 1 - f _ {U} ] ^ {2} \beta_ {U} ^ {2} - \beta_ {F} ^ {2} ] \kappa^ {2} ]}{8 \bar {e} ^ {2} p ^ {2} \delta}.
$$

The separating thresholds for the cost effectiveness of the incentive mechanism is obtained by comparing the social gain with the total subsidy:

$$
\hat {\beta} _ {U F} ^ {S G} = \frac {3 \beta_ {F} ^ {2} + \frac {\bar {e} ^ {2} p \delta \left[ \left[ [ 2 - f _ {I} ] f _ {I} - 2 [ 2 - f _ {U} ] f _ {U} \right] m _ {1} ^ {2} + \left[ [ f _ {I} - 2 ] f _ {I} - 2 [ f _ {U} - 2 ] f _ {U} \right] m _ {2} ^ {2} \right]}{m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}}}{3 [ 1 - f _ {U} ] ^ {2}}
$$

$$
S _ {U} (x _ {U 1}, x _ {U 2}) - S _ {F} (x _ {F 1}, x _ {F 2}) > x _ {U 1} + x _ {U 2} \mathrm{if} [ \beta_ {U} ] ^ {2} > \hat {\beta} _ {U F} ^ {S G}.
$$

To show that the social gain is enough to cover the total subsidy, we need to show $[ \beta _ { U } ] ^ { 2 } > \hat { \beta } _ { U F } ^ { S G }$ for all valid values of $[ \beta _ { U } ] ^ { 2 }$ within the diagonally shaded area of Figure 4. The necessary and sufficient condition for $[ \beta _ { U } ] ^ { 2 } > \hat { \beta } _ { U F } ^ { S G }$ is to show that $\hat { \beta } _ { U F } ^ { S G } < \hat { \beta } _ { U F } ^ { S W }$ :

$$
\hat {\beta} _ {U F} ^ {S G} - \hat {\beta} _ {U F} ^ {S W} = \frac {\bar {e} ^ {2} [ 2 - f _ {I} ] f _ {I} [ m _ {1} ^ {2} - m _ {2} ^ {2} ] p \delta}{3 m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}} > 0.
$$

The above result indicates that the social gain cannot justify the total subsidy for all values of $[ \beta _ { U } ] ^ { 2 }$ . To see if the social gain is enough to justify a portion of the diagonally shaded area in Figure 4, we then compare $\hat { \beta } _ { U F } ^ { S G }$ with $\hat { \beta } _ { U F } ^ { E q m }$ :

$$
\hat {\beta} _ {U F} ^ {E q m} - \hat {\beta} _ {U F} ^ {S G} = - \frac {\bar {e} ^ {2} \big [ [ 2 - f _ {I} ] f _ {I} - 2 [ 2 - f _ {U} ] f _ {U} \big ] [ m _ {1} ^ {2} - m _ {2} ^ {2} ] p \delta}{3 [ 1 - f _ {U} ] ^ {2} m _ {1} ^ {2} m _ {2} ^ {2} \kappa^ {2}}
$$

$$
\hat {\beta} _ {U} ^ {E q m} - \hat {\beta} _ {U} ^ {S G} \geq 0 \text {   if   } [ 2 - f _ {I} ] f _ {I} - 2 [ 2 - f _ {U} ] f _ {U} \leq 0, \text {   otherwise   } \hat {\beta} _ {U} ^ {E q m} - \hat {\beta} _ {U} ^ {S G} <   0.
$$

$\begin{array} { r } { \mathrm { I f } \ \frac { f _ { I } [ 2 - f _ { I } ] } { f _ { U } [ 2 - f _ { U } ] } \ge 2 . } \end{array}$ , then the social gain is sufficient to cover the total subsidy when $\hat { \beta } _ { U F } ^ { E q m } < [ \beta _ { U } ] ^ { 2 } < \hat { \beta } _ { U F } ^ { S G }$

$\begin{array} { r } { \mathrm { I f } \ \frac { f _ { I } [ 2 - f _ { I } ] } { f _ { U } [ 2 - f _ { U } ] } < 2 . } \end{array}$ , then the social gain is sufficient to cover the total subsidy when $\hat { \beta } _ { U F } ^ { S G } < [ \beta _ { U } ] ^ { 2 } < \hat { \beta } _ { U F } ^ { E q m }$

The social gain is not sufficient to cover the total subsidy for all other cases.

When we combine the results of Cases 1-3 together, we obtain Lemma 6 and Propositions 5.

## Proof of Proposition 6

First, focusing on the interior solutions, we obtain the new threshold values under the impact of initial interoperability $I _ { 0 } \colon$

$$
\hat {\beta} _ {U 1 - n e w} = \frac {[ 1 - f _ {I} ] ^ {2}}{[ 1 - f _ {U} ] ^ {2}} - \frac {4 \bar {e} ^ {2} p \delta [ f _ {I} - f _ {U} ] [ m _ {1} [ 2 - f _ {I} - f _ {U} ] [ 1 - \kappa ] + 2 I _ {0} m _ {2} \kappa ]}{3 m _ {1} m _ {2} ^ {2} [ 1 - f _ {U} ] ^ {2} [ 1 - \kappa ] \kappa^ {2}},
$$

$$
\hat {\beta} _ {F 1 - n e w} = [ 1 - f _ {I} ] ^ {2} - \frac {4 \bar {e} ^ {2} p \delta f _ {I} [ m _ {1} [ 2 - f _ {I} ] [ 1 - \kappa ] + 2 I _ {0} m _ {2} \kappa ]}{3 m _ {1} m _ {2} ^ {2} [ 1 - \kappa ] \kappa^ {2}},
$$

$$
\hat {\beta} _ {U F 1 - n e w} = \frac {1}{[ 1 - f _ {U} ] ^ {2}} \hat {\beta} _ {F 1 - n e w} + \frac {4 \bar {e} ^ {2} p \delta f _ {U} [ m _ {1} [ 2 - f _ {U} ] [ 1 - \kappa ] + 2 I _ {0} m _ {2} \kappa ]}{3 m _ {1} m _ {2} ^ {2} [ 1 - f _ {U} ] ^ {2} [ 1 - \kappa ] \kappa^ {2}},
$$

$$
\hat {\beta} _ {U 2 - n e w} = \frac {[ 1 - f _ {I} ] ^ {2}}{[ 1 - f _ {U} ] ^ {2}} - \frac {4 \bar {e} ^ {2} p \delta [ f _ {I} - f _ {U} ] [ m _ {2} [ 2 - f _ {I} - f _ {U} ] [ 1 - \kappa ] + 2 I _ {0} m _ {1} \kappa ]}{3 m _ {1} ^ {2} m _ {2} [ 1 - f _ {U} ] ^ {2} [ 1 - \kappa ] \kappa^ {2}},
$$

$$
\hat {\beta} _ {F 2 - n e w} = [ 1 - f _ {I} ] ^ {2} - \frac {4 \bar {e} ^ {2} p \delta f _ {I} [ m _ {2} [ 2 - f _ {I} ] [ 1 - \kappa ] + 2 I _ {0} m _ {1} \kappa ]}{3 m _ {1} ^ {2} m _ {2} [ 1 - \kappa ] \kappa^ {2}},
$$

$$
\hat {\beta} _ {U F 2 - n e w} = \frac {1}{[ 1 - f _ {U} ] ^ {2}} \hat {\beta} _ {F 2 - n e w} + \frac {4 \bar {e} ^ {2} p \delta f _ {U} [ m _ {2} [ 2 - f _ {U} ] [ 1 - \kappa ] + 2 I _ {0} m _ {1} \kappa ]}{3 m _ {1} ^ {2} m _ {2} [ 1 - f _ {U} ] ^ {2} [ 1 - \kappa ] \kappa^ {2}}.
$$

When we compare the new threshold values with the old threshold values (as given in the proof of Proposition 1) we obtain:

$$
\hat {\beta} _ {U 1 - n e w} <   \hat {\beta} _ {U 1}, \hat {\beta} _ {F 1 - n e w} <   \hat {\beta} _ {F 1}, \mathrm{and} \hat {\beta} _ {U F 1 - n e w} > \hat {\beta} _ {U F 1};
$$

$$
\hat {\beta} _ {U 2 - n e w} <   \hat {\beta} _ {U 2}, \hat {\beta} _ {F 2 - n e w} <   \hat {\beta} _ {F 2}, \mathrm{and} \hat {\beta} _ {U F 2 - n e w} > \hat {\beta} _ {U F 2}.
$$

This indicate the horizontal line moves down; the vertical line moves left, and the diagonal line moves up towards the upper left corner.

When we compare the new threshold values between District 1 and District 2 we obtain:

$$
\hat {\beta} _ {U 1 - n e w} <   \hat {\beta} _ {U 2 - n e w}, \hat {\beta} _ {F 1 - n e w} <   \hat {\beta} _ {F 2 - n e w} \mathrm{and} \hat {\beta} _ {U F 1 - n e w} > \hat {\beta} _ {U F 2 - n e w}.
$$

Recall that when the initial interoperability is not considered, we also have:

$$
\hat {\beta} _ {U 1} <   \hat {\beta} _ {U 2}, \hat {\beta} _ {F 1} <   \hat {\beta} _ {F 2} \mathrm{and} \hat {\beta} _ {U F 1} > \hat {\beta} _ {U F 2}.
$$

This indicates that the relative positions between the two districts’ preferences remain the same with or without the influence of initial interoperability. This proves all the results reported in Proposition 6.

Next, we focus on the case of boundary solution (i.e., the initial interoperability is large), we then solve for the optimal $e _ { i j }$ and $g _ { i j }$ under the new constraint $\begin{array} { r } { I _ { 0 } + \beta _ { i } \left[ { \frac { e _ { i 1 } + e _ { i 2 } } { \bar { e } } } \right] = 1 } \end{array}$ . Here we use the maximization problem for unified approach as a demonstration, the results for the other two interoperability approaches can be derived in a similar way.

Under the unified approach, the individual district’s decision problem is

$$
\max S _ {U j} (g _ {U j}, e _ {U j}) = m _ {j} \left[ [ 1 - \kappa ] [ 1 - f _ {U} ] g _ {U j} + \kappa \left[ I _ {0} + \beta_ {U} \left[ \frac {e _ {U j} + e _ {U \setminus j}}{\bar {e}} \right] \right] g _ {U \setminus j} \right] - p g _ {U j} ^ {2} - \delta e _ {U j} ^ {2}
$$

Subject to $\begin{array} { r } { 0 \le e _ { U j } \le \overline { { e } } , 0 \le g _ { U j } \le \overline { { g } } , 0 \le I _ { 0 } + \beta _ { U } \left[ \frac { e _ { U j } + e _ { U \backslash j } } { \overline { { e } } } \right] = 1 _ { } } \end{array}$ <sup>,</sup> <sup>where</sup> ?? ∈ {1, 2}.

Solve for the above maximization problem under the new binding constraint, we obtain:

$$
g _ {U 1} = \frac {m _ {1} (1 - f _ {U}) (1 - \kappa)}{2 p}, g _ {U 2} = \frac {m _ {2} (1 - f _ {U}) (1 - \kappa)}{2 p}, e _ {U 1} = e _ {U 2} = \frac {\overline {{e}} (1 - I _ {0})}{2 \beta_ {U}}.
$$

Here we can see that if the initial interoperability is very high $( \mathrm { e . g . , } I _ { 0 } = 1 )$ , then the optimal effort level should be zero for both districts.

The boundary solution surplus for each district is

$$
S _ {U 1 - B} = \frac {1}{4} \bigg [ \frac {m _ {1} [ 1 - f _ {U} ] [ 1 - \kappa ] [ m _ {1} [ 1 - f _ {U} ] [ 1 - \kappa ] + 2 m _ {2} \kappa ]}{p} - \frac {\bar {e} ^ {2} \delta [ 1 - I _ {0} ] ^ {2}}{\beta_ {U} ^ {2}} \bigg ],
$$

$$
S _ {U 2 - B} = \frac {1}{4} \left[ \frac {m _ {2} [ 1 - f _ {U} ] [ 1 - \kappa ] [ m _ {2} [ 1 - f _ {U} ] [ 1 - \kappa ] + 2 m _ {1} \kappa ]}{p} - \frac {\bar {e} ^ {2} \delta [ 1 - I _ {0} ] ^ {2}}{\beta_ {U} ^ {2}} \right].
$$

Here we use subscript B to denote Boundary solution.

The interior solution surplus for each district is

$$
S _ {U 1} = \frac {m _ {1} [ 1 - f _ {U} ] [ 1 - \kappa ] \Big [ 3 m _ {1} m _ {2} ^ {2} \beta_ {U} ^ {2} [ 1 - f _ {U} ] [ 1 - \kappa ] \kappa^ {2} + 4 \bar {e} ^ {2} p \delta [ m _ {1} [ 1 - f _ {U} ] [ 1 - \kappa ] + 2 I _ {0} m _ {2} \kappa ] \Big ]}{1 6 \bar {e} ^ {2} p \delta},
$$

$$
S _ {U 2} = \frac {m _ {2} [ 1 - f _ {U} ] [ 1 - \kappa ] \Big [ 3 m _ {1} ^ {2} m _ {2} \beta_ {U} ^ {2} [ 1 - f _ {U} ] [ 1 - \kappa ] \kappa^ {2} + 4 \bar {e} ^ {2} p \delta [ m _ {2} [ 1 - f _ {U} ] [ 1 - \kappa ] + 2 I _ {0} m _ {1} \kappa ] \Big ]}{1 6 \bar {e} ^ {2} p \delta}.
$$

Comparing the boundary solution’s surpluses with interior solution’s surpluses for each district, we derive the conditions for boundary solution. We find that the boundary solution’s condition is the same for both districts $( \mathrm { i . e . , }$ , both districts prefer the boundary solution or both districts prefer the interior solution simultaneously), in other words, the case whereby one district prefers the boundary solution and the other district prefers the interior solution does not exist. Specifically, when $\begin{array} { r } { I _ { 0 } \leq 1 - \frac { 3 m _ { 1 } m _ { 2 } \beta _ { i } ^ { 2 } \kappa \left( 1 - \kappa \right) \left( 1 - f _ { i } \right) } { 2 \overline { { e } } p \delta } } \end{array}$ , then the interior solution provides higher surplus to both districts and hence is the equilibrium, otherwise, the boundary solution is the equilibrium.
