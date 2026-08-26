---
otero_id: 20719
otero_key: "3QF46PV4"
title: "Data sustainability: Data governance in data infrastructures across technological and human generations"
authors: "Sirkka L. Jarvenpaa; Anna Essén"
year: "2023"
journal: "Information and Organization"
doi: "10.1016/j.infoandorg.2023.100449"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Data sustainability: Data governance in data infrastructures across technological and human generations

![](/api/attachments/3QF46PV4/fulltext/images/c6bbabc4b9ce8a51cc3b5c6bb8da529ae7461a762e9515ec065c76c9daf34d0d.jpg)

Sirkka L. Jarvenpaa $^{a,*}$ , Anna Essén $^{b}$

$^{a}$ Center for Business, Technology, and Law, McCombs School of Business, University of Texas at Austin, 2110 Speedway Stop B6500, Austin, TX 78712-1750, United States of America

$^{b}$ House of Innovation, Stockholm School of Economics, Sweden

## ARTICLEINFO

Keywords:  
Data governance  
Data sustainability  
Temporality  
Time  
Distant futures  
Infrastructure  
Interoperability  
Environmental sustainability  
Social sustainability

## ABSTRACT

The paper highlights the importance of data sustainability in the data infrastructures aimed at long-term knowledge discoveries. Data sustainability refers to data's capacity to endure across technological and human generations, and it problematizes the data governance literature from a temporal perspective. Existing work has already moved the literature from the organizational setting to more complex interorganizational settings, highlighting discrepancies between normative data governance models and organizational practices. We broaden this literature temporally by examining and outlining research directions for data sustainability from different meta-theoretical perspectives – evolutionary, relational, and durational. Data sustainability across technological and human generations navigates complementary and competing temporal demands: Data need to transition across socio-technical regimes over time, yet be embedded in social and material networks to be meaningful; historical and present data also must remain available and accessible in near and distant futures, for going back in time and seeing new data linkages and combinations. We argue that data sustainability is critical in ensuring progression in social and environmental sustainability. The paper contributes both to data governance and sustainability literatures.

## 1. Introduction

Imagine a young patient – Kim – providing blood samples to her doctor. The doctor uses the sample to confirm Kim's infection levels and to prescribe drugs for her; she also asks Kim for informed consent to share the blood sample with a biobank that sequences the sample, creating digital representations of Kim's genetic profile that are shared with numerous research teams over the coming years, as well as in future decades and centuries, to advance scientific knowledge and new treatments. She receives annual notifications about how the data are being used. She does not evoke her right to delete data or to remove the sample from biobank collections.

Imagine 150 years later. Thanks to the modern storage technology, Kim's sample and the millions of samples provided by other patients of Kim's generation remain in active use; they are re-sequenced to evolve digital data representations that incorporate the latest technological advances. Kim's samples become unexpectedly valuable because she has a certain genetic profile. Researchers ask difficult questions in new ways, test new hypotheses, and conduct scientific studies that help future generations of Kim's children and others with a similar genetic profile.

The need for large-scale digitization and accumulation of data for breakthrough discoveries has given rise to data infrastructures in various research domains, in both public and private settings. Such data infrastructures are necessitated when no organization or consortium alone has the necessary capacity, expertise, and funding to digitize and accumulate the necessary data to address grand challenges in health, climate, and crime, among others (Diamond, Mostashari, & Shirky, 2009; Gille, Vayena, & Blasimme, 2020: Holm & Thomas, 2017; Oliveira, Lima, & Loscio, 2019; Perkmann & Schildt, 2015; Shabani, 2021; Sjoukema, Samia, Bregt, & Crompvoets, 2022; Sudlow et al., 2015). We define such data infrastructures as multilayered and as connecting heterogeneous systems involving inputs from and outputs to many different independent actors (Constantinides, Henfridsson, & G. G., 2018; Lyytinen, Sorensen, & Tilson, 2017; Yoo, Henfridsson, & Lyytinen, 2010). Data extend beyond individual contributors, varied organizational actors, and interorganizational settings. As in the opening illustration, data collected at one point in time may become valuable in relation to industrial, scientific, and policy problems identified tens and hundreds of years later. Yet, this possibility required efforts of a much earlier time and consideration of future needs (Chiasson, Davidson, & Winter, 2018), with continuous investment and practices that sustain data across human and technological generations.

We define data sustainability as the capacity of data to endure across technological and human generations. This capacity includes data's potentiality for transcending technological and social arrangements and facilitating knowledge advances beyond current questions. Data sustainability draws on but is distinct from the definition of sustainability in the information systems (IS) literature, where sustainability is often defined as “the capacity to endure” (Davidson, 2014, p. 1, in Mindel, Mathiassen, & Rai, 2018) and as “development that meets the needs of the present without compromising the ability of future generations to meet their own needs” (World Commission on Environment and Development (WCED), 1987, p. 43). Data sustainability is “an intertemporal concept, one that explicitly anchors performance in the present on a series of comparisons and contrasts with anticipated futures and recollected pasts” (Garud & Gehman, 2012, p. 980).

In this paper, the temporal horizon is the distant future – that is, time across technological and human generations. Data sustainability implies that data accumulation in the past and present is used to meet the needs of the present generation but without compromising the data's use in the future by heterogeneous, independent, and unknown actors. Technological advancements make it meaningful and pertinent to take data sustainability into consideration, given the increased means to store data but also to erase it. This data sustainability lens not only is consistent with the other sustainability views in the IS literature but also is critical of them; these views conceptualize digital artifacts as a means to make organizations, communities, and societies both more socially sustainable (inclusive, fair) and more environmentally sustainable (reducing negative effects on natural resources) (Davidson, 2014; Leidner, Sutano, & Goutas, 2022; Melville, 2010; Seidel, Recker, & Brocke, 2013; Watson, Boudreau, & Chen, 2010; Wunderlich, Veit, & Sarker, 2019). However, the endurance of data from the past and present for possible future uses is a little-discussed aspect of data that has implications for data governance and for sustainability more broadly.

The objective of this paper is to stimulate discussion and future research on data sustainability in data infrastructures. We are not implying that all data should be sustained or that doing so is always ethical (see, e.g., Skloot, 2018; Stelmaszak & Wagner, 2022). We also note that data sustainability is related to many other ongoing discussions. For example, in the IS literature, socio-technical futures studies (e.g., Chiasson et al., 2018; Hovorka & Peter, 2021) improve our understanding of how decisions made about information technology (IT) lead to different futures. In information sciences, linked open data initiatives examine various archival approaches and technologies to connect catalogs of cultural institutions around the world (Gaitanou, Andreou, Sicilia, & Garoufallou, 2022; Thompson & Richard, 2013; Zeitlyn, 2012) while “preserving their original expressivity and richness” (Lampert & Southwick, 2013, p. 243). $^{1}$ Social studies of science focus on data mobility that includes the historical view of data (Leonelli & Tempini, 2020). Yet, what is missing in these works are long-term horizons of past and future, and of discoveries that go beyond domain-specific efforts, such as music cataloguing (Weitz, Toves, Vizine-Goetz, Naught, & Bremer, 2016).

We aim to contribute to the data governance and sustainability literatures. We next review some of the seminal works on data governance and how they are silent about long-term horizons for data. To structure our conversation about data sustainability, we then present three perspectives on sustainability, following Garud and Gehman (2012): evolutionary, relational, and durability. We discuss the complementary and competing demands of the evolutionary and relational perspectives and how the durational perspective can help navigate the demands. We call for more research on data sustainability in data infrastructures. We close by projecting the critical role of incorporating data sustainability in data governance efforts in relation to long-term social and environmental sustainability.

## 2. Organizational scope and data sustainability in data governance studies

According to the Data Governance Institute, n.d., “Data Governance is a system of decision rights and accountabilities for information-related processes, executed according to agreed-upon models which describe who can take what actions with what information, and when, under what circumstances, using what methods” (https://datagovernance.com/the-data-governance-basics/definitions-of-data-governance/n.d). The data governance literature builds extensively on the normative data governance framework of Khatri and Brown (2010) and has extended it to interorganizational settings. Data management studies complement the normative perspective, focusing on the day-to-day construction and use of data. In addition to these two strands of the data governance literature, we draw selectively on the literature on data digitization, data processing, and data use in data infrastructure settings (e.g., Constantinides et al., 2018; Lyytinen et al., 2017; Yoo et al., 2010; Yoo, Boland, Lyytinen, & Majchrzak, 2012).

## 2.1. Normative data governance: from organizational to interorganizational

Early data governance work focused on the single organization context with a normative perspective on the collection, storage, processing, use, sharing, and disposal of data (see, e.g., Khatri & Brown, 2010; Tallon, Ramirez, & Short, 2013; Weber, Otto, & Osterle, 2009; see a review by Abraham, Schneider, & vom Brocke, 2019). The influential Khatri and Brown framework (2010) builds on the firm perspective of Weill and Ross (2004) and outlines five decision domains – areas in which decisions should be made and for which someone should be accountable in the business organization: (1) data principles (clarifying the role of data as an asset for the business); (2) domain decisions (how data quality will be evaluated); (3) metadata (establishing semantics of data, how data will be consistently and continuously defined so that it is interpretable); (4) data access (what the data access standards and procedures are and how compliance is monitored); and (5) data lifecycle (determining the retention and retirement of data).

Subsequent work extended data governance from the IT department to an organization-wide task (Otto, 2011); this work refers to data or information value chains (Abbasi, Suprateek, & Roger, 2016; Markus, 2016; c) that are necessary to convert data into information and knowledge (Sharma, Mithas, & Kankanhalli, 2014) and to identify requisite data governance roles (Korhonen, Melleri, Hiekkanen, & Helenius, 2013); for example, such roles include executive sponsor, data governance council (or data quality board), chief steward, business data steward, and technical steward (Korhonen et al., 2013; Otto, 2011). Normative models suggest the roles and teams that should be in place, and they assume that the persons and team members occupying the roles have the “requisite” accountability and authority to exert influence over others (Korhonen et al., 2013).

Taken together, studies on intra-organizational data governance implicitly discuss sustainability by suggesting roles and procedures ensuring that data will “endure” as an asset for the focal firm, across its internal departments and the different technical systems used within the firm during the current socio-technical generation. Discussions primarily center on the potential to accumulate and use data in real time, discover present patterns, optimize current behaviors, prevent common problems, or react immediately to contingent events. Beyond present concerns, documenting the past is recognized in terms of data provenance and traceability.

Scholarly work has extended the normative intra-organizational data governance models into inter-organizational contexts (Abraham et al., 2019; Alhassan, Sammon, & Daly, 2016; de Prieëlle, de Reuver, & Rezaei, 2022; Lee, Zhu, & Jeffery, 2018). This work recognizes that data producers and data users are often dispersed across organizations, with different power and control contests (Zuboff, 2015). Thus, scholars acknowledge the need for an adjustment of current data governance concepts and dimensions, along with new archetypes of governance modes, including market, bazaar, and network modes (Van den Brock & van Veenstra, 2018), as well as platform modes (Lis & Otto, 2020). Yet, the extended scope has left largely intact the normative governance domains (i.e., principles, decisions, meta-data, access, and lifecycle), as well as their associated roles, with the acknowledgement that the inter-organizational context is different and poses new challenges in these domains (Lee, Zhu, & Jeffery, 2017). Beyond issues of ownership and access, more issues surface, including the contribution estimation (i.e., considering contributors' efforts in data creation) and greater complexity in data use (e.g., access and use cases, conformity, monitoring, and data provenance) (Lee et al., 2017). Solutions have rallied around interorganizational instruments, such as licenses, contract-based agreements, and technical measures for data sharing (Lis & Otto, 2020); collective risk-based approaches for preventing data-embedded discrimination (Janssen, Brous, Estevez, Barbosa, & Janowski, 2020); and collective governance approaches underpinned by principles of fair information practices, privacy impact assessments, and privacy accountability (Barr-Kumarakulasinghe & Boon-Kwee, 2022). Instead of assigning individuals to specific data roles ex ante, such as data owner, steward, and others (as in, e.g., Korhonen et al., 2013), organizations are encouraged to embrace emergent and fluid roles (Oliveira et al., 2019).

Yet, models in the intra-organizational context, even when adjusted to accommodate for multiple organizations, do not necessarily apply in or are appropriate to the interorganizational context. In this context, lack of data sharing and data use is observed (Lis & Otto, 2020; van den Broek & van Veenstra, 2015). In addition to misuse and overuse, which are emphasized in the intra-organizational data governance literature, underuse is an issue in interorganizational settings both because of regulations (Perkmann & Schildt, 2015; Rosenbaum, 2010; Shabani, 2021) and because of the absence of processes, roles, and provenance routines recommended in normative models (Lee et al., 2017). Studies reveal how the interorganizational context is unable to settle some of the key data governance decisions and coordination challenges: how to define data ownership of machine-generated data; how to ensure data security, availability, and sovereignty (i.e., to ensure that data are used only for the intended purpose); how to align incentives among data providers with the goals of data users; and how to ensure the usability and usefulness of the data to the users, among others (Lis & Otto, 2020; Markus & Bui, 2012; Susha, Janssen, & Verhulst, 2017a, 2017b). The literature in several areas – including on data platforms (Jarvenpaa & Markus, 2019; Otto & Jarke, 2019); data marketplaces (Koutroumpis, Leiponen, & Thomas, 2020); and data ecosystems (Aaen, Agger Nielsen, & Carugati, 2022; Benfeldt, Persson, & Madsen, 2020; de Prieelle et al., 2022; Oliveira et al., 2019) – has further led the discussion toward complex contexts, where data are expected to be used and recombined in unexpected ways by multiple organizations. Moral challenges arise, including conflicting views about what constitutes appropriate behavior in relation to the exchange of data, given societal and individuals' privacy and security concerns (Gray, Briscoe, & Ferraro, 2022; Winter & Davidson, 2019).

The studies of interorganizational contexts only implicitly consider sustainability by considering future users in terms of the need to enable discoveries through the shared collection and accumulation of data (Holm & Thomas, 2017; Link et al., 2017; Perkmann &

Table 1  
Assumptions and foci in data governance studies.

<table><tr><td></td><td colspan="5">Data governance (DG) domain issues (Khatri &amp; Brown, 2010)</td></tr><tr><td>Contexts</td><td>Data principles (clarifying the role of data)</td><td>Data quality (establishing requirements for intended use)</td><td>Metadata (semantics of data)</td><td>Data access (access requirements)</td><td>Temporal horizon</td></tr><tr><td>Intra-organizational context</td><td>Establishing data as a strategic asset for firm; suggested firm-level roles: data trustee/producer/enterprise data committee</td><td>Standards used to evaluate quality; firm-level roles: data owner/quality manager/subject matter expert</td><td>Definitions of data; firm-level roles: enterprise data modeler, data architect</td><td>Rules regarding access procedures, compliance, backup, recovery</td><td>Timespan of a present, known business; aim is to exploit data according to the specific firm&#x27;s interest</td></tr><tr><td>Inter-organizational context</td><td>Establishing data as a shared resource for a set of organizations; various shared governance modes suggested, but lacking evidence</td><td>Shared standards suggested, but empirical studies point at lacking enforcement; no single actor has authority to enforce rules</td><td>Shared definitions suggested, but empirical studies point at multiple standards</td><td>Shared rules suggested, but empirical studies point at difficulties in agreeing on level of openness</td><td>Timespan of present organizations; aim is to ensure effective data use by predefined collaborators</td></tr><tr><td>Data management studies</td><td>The role of data is the result of what actually gets recorded and used</td><td>Understandings of data quality emerge as a result of how data are used in practice</td><td>Definitions of data originate, are embedded in the social and material context of data use</td><td>Who gets access to data is the result of negotiations between actors</td><td>Timespan of present practices; aim of DG is embedded in social and material context</td></tr><tr><td>Issues yet to be theorized</td><td>Defining the role of data in relation to future unknown users; expanding DG to acknowledge need to accommodate unknown users and uses of data</td><td>Expanding DG to manage multiple quality standards and ways of implementing them</td><td>Expanding DG to acknowledge gaps between domain bounded and temporally locked-in standards</td><td>Expanding DG to acknowledge role of regulation, multilateral contracts (e.g., legal, social)</td><td>The timespan of generations; how can aim of DG provide continuity but allow for evolving uses over time?</td></tr></table>

Schildt, 2015). In these settings, “reuse” of data is assumed or recommended (Holm & Thomas, 2017), with acknowledgement of the need to accommodate future users; to extend the life of the data beyond the initial project or initiative (Legner, Tobias, & Boris, 2020), including to unexpected uses; and to discover new, hidden insights and details (Laine, Lee, & Nieminen, 2015). Promoting the ability to reuse data and to link data to other data recognizes the need for data to travel beyond its initial contexts (Leonelli & Tempini, 2020; Markus, 2001; Tempini, 2016). Yet, data governance decisions and roles are hidden as they are inscribed into current technological archetypes (i.e., the platforms or ecosystems). Common data standards and the actions of the central orchestrator or trusted intermediary can become critical for crossing instances of different archetypes (Abraham et al., 2019).

A temporal orientation is rather narrowly reflected in terms of data's lifecycle, or it is homogenously perceived as prolonging the current state: The existing interorganizational actors are assumed to be the users of the data in the future (Lee et al., 2017; Lis & Otto, 2020; Oliveira et al., 2019). Thus, the temporal horizon of extant studies generally focuses on the present generations of users, rather than considering a temporal horizon that spans across technological and human generations. The problems that may arise as the current generation of actors and technologies is replaced by new generations are not discussed.

## 2.2. Sustainability in data management

A nascent stream of research spanning organizational and IS studies has begun to recognize not just different interests in the processes of data collection and use but also their varying assumptions, tensions, and conflicts, exhibited in day-to-day data management. These studies view data not as a raw representation of reality and as preceding knowledge production, but as being actively constructed (e.g. Abdelnour, Hasselbladh, & Kallinikos, 2017; Alaimo & Kallinikos, 2022; Alaimo, Kallinikos, & Aaltonen, 2020; Jones, 2019; Leonelli & Tempini, 2020). Even if the varied actors are within one organization, data practices are embedded in larger cultural, social, and technological contexts.

Studies in this stream show that assumptions about data are intertwined with current knowledge and action (Aaltonen, Alaimo, & Kallinikos, 2021; Aaltonen & Tempini, 2014; Alaimo & Kallinikos, 2017, 2021; Constantiou & Kallinikos, 2015; Jones, 2019; Monteiro & Parmiggiani, 2019; Osterlie & Monteiro, 2020; Ribes & Polk, 2015; Tuomi, 1999). For example, Tuomi (1999, p. 7) argues that data “can emerge only if a meaning structure is first fixed and then used to represent information.” Jones (2019, p. 12) notes that data creation involves selection involving a recognition of “what is considered to be the phenomenon” and “what is considered to be data about the phenomenon.” These selections require attention and interpretation (Ocasio, Rhee, & Milner, 2020). This interpretation of data can be done by humans or by technology.

Studies indicate that data practices involve considerable labor, not just in terms of selection, but also of deselection. Deselections of irrelevant data, like selections of relevant data, are a necessary and rational step in the creation of useful data (Osterlie & Monteiro, 2020). Pragmatic concerns of what is technically and economically viable and relevant at specific points in time drive the preparation for and recording of off-line events and objects and their transformation into data. Once digitized, these data tend to become increasingly decoupled from their physical origins but still require and receive attention, selection, and interpretation (Monteiro & Parmiggiani, 2019).

These studies advance our understanding of the embeddedness of organizational and centralized data practices in the present. They generally overlook the tensions that may arise in data creation for use in interorganizational and distributed contexts, involving actors with heterogeneous goals and different temporal intervals. For example, Monteiro and Parmiggiani (2019) study corporate efforts (i.e., NorthOil's efforts) to establish synthetic knowing of the Arctic based on internet-of-things (IoT) capabilities, for the purpose of presenting corporate activities. Others study scientific data infrastructures that were created to be used by multiple actors now and in the future, but they primarily focus on the immediate use by one group of actors (Halfmann, 2020; Karaca, 2020).

To summarize, the extant data management studies have deepened our understanding of how data are actually created and used, including both necessary resources and challenges in the coordination and alignment of the interests of many different stakeholders (see Table 1). Yet neither the data governance studies nor the data management studies have explicitly discussed data sustainability challenges that may arise in allowing data to endure across technological and human generations. Hence, we know little about how to coordinate and balance the interests of future generations of users with the interests of present users; such challenges have not been discussed systematically. The same lacuna of long-term horizons exists in the recent literature on data and artificial intelligence (Jussupow, Spohrer, Heinzl, & Gawlitza, 2021; Lebovitz, Levina, & Lifshitz-Assaf, 2021; Lebovitz, Lifshitz-Assaf, & Levina, 2022; Sturm et al., 2021), as well as in studies on data brokering and data sourcing (Jarvenpaa & Markus, 2020; Koutroumpis et al., 2020; Oliveira et al., 2019; Zuboff, 2015).

## 3. Data sustainability journeys

## 3.1. Evolutionary, relational, and durability perspectives

We ground our discussion of data sustainability in the meta-theory of sustainability journeys of Garud and Gehman (2012): evolutionary, relational, and durational (Table 2). Sustainability journeys consider developments that consider and reconcile the needs of present generations with future generations (Garud & Gehman, 2012; World Commission on Environment and Development (WCED), 1987). Garud and Gehman (2012) introduce the three meta-theoretical perspectives on sustainability journeys to highlight the various challenges and solutions facing actors involved in such journeys. We chose this particular framework of journeys because the perspective aligns with the temporal long-term horizons that we see as critical for data sustainability. Garud and Gehman (2012) considered the three perspectives separately because they build on different meta-theoretical assumptions. That is, each perspective describes certain distinct pathways and mechanisms through which sustainability can be improved. Following Garud and Gehman (2012), we first discuss the perspectives separately in light of their data sustainability-related challenges. We draw on the studies discussed in Section 2 to tease out the challenges. We then extend the discussion by exploring how the perspectives can also inform each other and broaden our ways of thinking about sustainability.

Table 2  
Three perspectives on sustainability and inferred data sustainability challenges in data infrastructures.

<table><tr><td rowspan="2">Perspective on sustainability</td><td colspan="3">Inferred definition of data sustainability and challenges</td></tr><tr><td>Definition of sustainability journeys (Garud &amp; Gehman, 2012)</td><td>Definition of data sustainability</td><td>Data sustainability challenges</td></tr><tr><td>Evolutionary perspective</td><td>Sustainability journey involves shift from one set of socio-technical requirements to another (presumably better) set; involves cognitive routines; regulations and standards; norms and practices; and specialized assets and competences.</td><td>Ability of data to transit across socio-technical regimes</td><td>Data may be locked into old socio-technical regimes and unable to transfer to next socio-technical regime</td></tr><tr><td>Relational perspective</td><td>Sustainability journeys involve the multiple interpretations and conflicts of interest that surface as multiple stakeholders engage in contributing to or performing sustainability</td><td>Ability of data to translate across social and material use contexts</td><td>Data may fail to get embedded into and translated within social and material networks</td></tr><tr><td>Durational perspective</td><td>Sustainability understood as continuity and links between the past, present, and future, noting the possibility and importance of going “back to the future.”</td><td>Ability of data to be located again and used in unknown and unexpected ways over time</td><td>Past data becomes inaccessible and loses its meaning without continuing investments/in light of new knowledge</td></tr></table>

## 3.2. The evolutionary perspective

From an evolutionary economics perspective (Dosi, 1982; Nelson & Winter, 1982), sustainability journeys can be understood as “transitions from one set of socio-technical requirements to another” (Garud & Gehman, 2012, p. 981). Here, selection serves as a mechanism of change as “fields and firms transition from one ‘regime’ to another” (Garud & Gehman, 2012, p. 980).

Shifts are triggered by exogenous sources (e.g., disruptive innovation or a change from a liberal to an authoritarian policy regime) and involve the move from one set of cognitive routines, regulations and standards, norms and practices, and specialized assets and competences (Geels & Schot, 2007) to another (presumably better) one. Shifts are understood as accomplished when the new socio-technical regime once again stabilizes, “albeit around potentially new technologies, actors and policies” (Garud & Gehman, 2012, p.981).

An assumption in the evolutionary perspective is that the relevance and value of technologies shift over time. The shift is evolutionary and introduces new better technologies; new technologies are assumed to replace old technologies at some point in time. The replaced technologies become obsolete and of less value. Hence, the shift from one socio-technical regime to another can improve sustainability – for example, by providing more advanced and precise constructs, tools, and metrics to meet sustainability requirements tied to specific domains (e.g., environmental pollution).

## 3.2.1. Data sustainability challenges

The socio-technical evolutionary shifts have not been foregrounded in the data governance models discussed above. In the data governance literature, as well as in IS literature more broadly (e.g., Constantinides et al., 2018; Lyytinen et al., 2017; Yoo et al., 2012), data are portrayed as a “decoupled layer”; this layer is seen as having the capacity to be freed and disconnected from lower levels in the modular infrastructural hierarchy. Data are normatively seen as highly mobile – a token (McKinney & Yoo, 2010) and commodity (Jarvenpaa & Markus, 2020) – and as able to transition across different cognitive routines, regulations and standards, norms and practices, and specialized assets and competences. The assumption is that data can be easily edited and recombined to create new forms (Kallinikos, Aaltonen, & Aatilla, 2013; Lyytinen et al., 2017; Yoo et al., 2012), but there is little discussion about what happens across shifts in socio-technical regimes.

In the data governance literature, the value of data is assumed to decline over time. Acknowledging that the value of data fluctuates over time, Tallon and Scannell (2007, p. 66) write that “[t]he underlying premise… is that information follows a natural life cycle from capture through application and decline.” In their model, the value of information goes from high in the “application” stage, to medium and to low in the “decline” phase, where information is moved to lower cost storage (e.g., tape, optical) (Tallon & Scannell, 2007, p. 69). There is an implicit assumption that deselection of old data is inevitable.

The notion of “legacy” is commonly used to refer to the creation of long-lasting effects beyond the temporal constraints of the lifespan (Fox, Tost, & Wade-Benzoni, 2010), but in the data context, “legacy” data can imply not just older data but also data that do not meet the socio-technical requirements of the current regime (Salokannel, Tarkkala, & Snell, 2019). Amazon (Rathnam, 2022) and Ferrari Racing $^{2}$ claim to have dashboards that connect to data originating from the organizations’ early days: 28 and 65 years’ worth, respectively. Scientists studying long-term changes of natural systems compare old and new data across lengthy time frames (Edwards, 2010; Halfmann, 2020; Monteiro & Parmiggiani, 2019). However, the studies do not provide details on efforts to transition data across socio-technical regimes and how the five decision domains of data governance (i.e., principles, domain decisions, metadata, data access, and data lifecycles) were carried forward.

## 3.2.2. Research implications

The evolutionary perspective raises questions of what, how, and why data cross socio-technical regimes. Data transitions to new regimes can be spotty, limited, or nonexistent, undermining data sustainability. Transitions across socio-technical generations may be affected by the nature of new socio-technical regimes (Gersick, 2020; Orlikowski, 1996). The regime's design view (Boland & Collopy, 2004; Simon, 1996) may play a role. The design view advocates for design goals that change the current situation to a preferred future one. For example, the old regime may involve hierarchical archetypes with waterfall designs, and new regimes may involve network archetypes with agile and lean approaches or archetypes with a decentralized, autonomous organization (DAO) of data. At what costs do data transition across technological generations? The old technological archetypes might be deeply inscribed in data, making transitions economically and technically difficult. What are the costs when transitions do not take place and old and new socio-technical regimes continue to co-exist?

Future research could ask how the nature of the exogenously triggered regime change makes a difference to data's capacity to cross to the new regime. How is data sustainability affected when shifts are incremental and continuous, versus radical and disruptive? Studies can connect data sustainability to the ongoing literature streams on technology-based organizational change (Orlikowski, 1996), as well as on digital transformation (Wessel, Baiyere, Ologeanu-Taddei, Cha and Blegind Jensen, 2021).

Research needs to attend to how data are planned and prioritized in the new regime. How do standards and policies for metadata influence data decisions in data selection and deselection during shifts from old to new regimes? At what level are data decisions made, and what are the temporal horizons in data selections and deselections? What capabilities (i.e., data practices, tools, policies, and roles) are needed to allow data to participate over time from an evolutionary perspective? What resource bases are critical, such as investments in metadata that can evolve or take on a “common lexicon,” as transitions to different regimes are needed?

Finally, how are data infrastructures prepared at present for technological disruptions in the future? Much can be gained by exploring investments made now, in the present, to ensure data sustainability in relation to expected or unknown breakthroughs. Such investment practices could inform current data governance models, beyond privacy, security, and misuse, to longer term societal benefits (Rychnovská, 2021). What new language is needed in data governance to account for the complexities of future challenges (Rychnovská, 2021)? Can organizations leapfrog socio-technical regimes while maintaining data from the past and present for future uses – for example, by moving from a nondigitized environment to a highly distributed environment while by-passing a regime of data centralization or a central orchestrator?

## 3.3. Relational perspective

In contrast to the evolutionary perspective, the relational perspective on sustainability does not view the exogenous disruptions or the “selection” of superior technologies and deselection of inferior technologies as a given mechanism in sustainability journeys (Garud & Gehman, 2012). Instead, the relational perspective assumes that sustainability develops from within – that is, via translations and the mutual shaping of actors (social, conceptual, and material) in networks in real-time and over time (e.g., Callon, 1987; Latour, 1994; Law, 2009; Pickering, 1993). The relational perspective draws attention to how actors not only are subject to, but also are actively shaping, the shifts in selection environments and the period between such shifts. Translations – transformations of meaning – involve the negotiation of and conflicts between understandings, interpretations, and interest that surface when multiple stakeholders are involved in contributing to or performing sustainability journeys. The flow of entanglements is situated in time, and past and future are remade in the moment. Hence, time cannot be generalized or abstracted from the situation. The mutual shaping of actors in such translations was illustrated by Barley (2015), who describes how the relationships between weather research teams and the partners who used the outputs affected the anticipation of the model outputs, as well as how this anticipation shaped the very practices of the research teams to produce these outputs.

## 3.3.1. Data sustainability challenges

The relational perspective depicted by Garud and Gehman (2012) emphasizes the agency of actors in shaping ongoing and present translation processes (Latour, 1986; Pickering, 1993), through which data are recontextualized, re-embedded, and thus allowed to acquire meaning in new social and material network nodes (Granovetter, 1985; Law, 2009). Expectations of future interactions with particular actors not only lead to inclusion but also exclusion of data, as was found with automobile engineers and their models (Bailey, Leonardi and Barley, 2012). This interrelatedness implies that data are rarely able to be completely delayered and decoupled. The goals, values, and logics of technology are inscribed in data (Sarker, Chatterjee, Xiao, & Elbanna, 2019). The relational perspective calls attention to the multiple interests and the social and material situations that shape how the value of data is understood, which in turn has implications for how data are embedded, translated, and able to participate in the mutual shaping of actors in networks. Situated interests shape what data “become,” how data are combined, and when data are retired. However, when interests and social and material situations shift over time, data may remain anchored to, or locked in, specific historical, social and economic contexts.

A relational perspective is evident in studies that focus on the microlevel details of present data practices in specific social and material networks and on the roles and practices that constitute data creation and use (Leonelli & Tempini, 2020; Osterlie and Monteiro, 2020; Jones, 2019). Monteiro and Parmiggiani (2019) illustrate how offline world objects become transformed from their physical and biological basis into computationally created digital representations, and Halfmann (2020) and Karaca (2020) foreground the material interactions in the early stages of digital data creation that involve trade-offs and choices and that affect what can be known and who can participate. Studies of data governance in interorganizational settings also foreground the multiple interests that need to align and be communicated in data infrastructures (e.g., Holm & Thomas, 2017; Markus & Bui, 2012; Perkmann & Schildt, 2015; Susha et al., 2017a, 2017b). In their study of emergent genomic data markets, Gray et al. (2022) show how different clusters of actors seek to advance their preferred exchange rules to shape markets and how the technologies they selected influenced the enactment of rules that governed the exchanges, ultimately constraining the range of moral choices available. As data become embedded in data markets, they are translated in particular ways, rather than in other ways, across user contexts – for instance, based on rules regarding who owns the data.

Overall, this literature stream highlights the many social and material “nodes” involved in the translation (creation, implementation, and use) of data. As data are embedded into and used by the multiple nodes, different interests influence which data are recorded and used (Jones, 2019; Leonelli, 2015). Many translations and negotiations about data hit a dead end, not because they concern data that are inherently inferior to alternatives (as would be assumed in the evolutionary perspective), but because of the lack of associations formed around the data, between heterogeneous elements constituting social and material networks. Data that lack associations are data without a meaning.

## 3.3.2. Research implications

The relational perspective raises important questions – first, about “what is considered to be the phenomenon” and “what is considered to be data about the phenomenon” (Jones, 2019, p. 12), and second, about how data that fail to become embedded and translated over time present a challenge to data sustainability. Extending the relational perspective backward and forward in time (in contrast to the contemporary present-focused theorizing) provides insights into the virtuous and vicious cycles that cause data to fail or that get data embedded into social networks. Virtuous cycles mean that data become embedded, integrated, cared for, and curated in social networks, which may increase their chances of becoming even more useful and, in turn, cared for (e.g., standardized, indexed, stored for future use). Vicious cycles mean data are not prioritized but are disregarded and left unattended by social nodes or networks at one point in time, which in turn makes rendering the data useful over time even harder because their low-prioritized storage and indexing make them difficult to find.

Data sets that link over time and across domains can be vital for rendering breakthrough discoveries at the population and societal level. In healthcare and wellness, present-day individual or micro concerns around privacy and security can conflict with the future concerns at the population and societal levels, thus presenting obstacles to the embedding and translation of data across nodes. In these settings, how can the micro and macro concerns be addressed productively so that when concerns at the micro level are voiced (e.g., over ownership or data collection legality), legitimate societal voices also are heard (e.g., the opportunity costs of creating borders and barriers)? To illustrate, the Danish Data Authority instructed the large, nationwide Danish health database to erase the “already collected data” because of the illegality of data collection, despite the fact that “the Danish National Archives determin[ed] that it was worth preserving and archiving” (Aaen et al., 2022, p. 291), presumably for future users.

The value of digitized representations, as well as their physical counterparts, can increase over time when these data resources are preserved in ways that ensure their use over time. What mechanisms can facilitate embeddedness but also transfers and translations across societal sectors, industries, and scientific domains over time, without legitimizing illegal or unethical activities? To illustrate, physiological data (e.g., heartrate, pulse, and stress levels of individuals) might be translated for healthcare networks but also for commercial networks of firms that use the data to customize offerings. Such data also might be moved to public sector networks to record potential implications of climate change. How do these data translate back and forth across societal sectors over time? How are data's meanings and interpretations managed across the social domains at certain points in time, as well as over time?

## 3.4. Durational perspective

Durability involves conversations in which past, present, and future are all voiced and shape current actions. As noted by Garud and Gehman (2012, p. 986), “[t]he phenomenological view of time in such theorization offers a counter-intuitive insight: that what we have abandoned in the past can serve as key resources in our quest for sustainability.” More than the other two perspectives, the durational perspective foregrounds links between the past, present, and future in sustainability journeys. From this perspective, durée (cf. Bergson, 1934/2007) serves as a mechanism of sustainability, “highlighting the possibility and importance of going ‘back to the future’” (Garud & Gehman, 2012, p. 980). Going back to the future means revisiting (potentially previously discarded) resources from the past to better understand and solve problems emerging or expected in the future. For instance, Garud and Gehman (2012, p. 980) refer to how farmers in emerging economies initially considered genetically modified crops to be a solution to the problem of sustainable development but returned to previously abandoned practices owing to unintended problems with the modified crops.

Garud and Gehman (2012) discuss a number of challenges to a durational perspective in a sustainability journey. A tremendous challenge is how to align, balance, or compromise the needs of present and future actors (Wade-Benzoni, 2002). One particular reason is that actors in the present may be incapable of anticipating and explicating the needs of users in the future; for example, they may be caught in local rationality traps (Porac, 1997). Further, even in cases where the capacity and motivation exist to address such challenges, “the journey itself is full of ups and down, false starts and dead ends (Van de Ven, Polley, Garud, & Venkataraman, 1999)..., [and] even when we arrive in the future, there will be still more future others waiting for us, thereby setting us up for a journey that can never be completed” (Garud & Gehman, 2012, p. 985).

## 3.4.1. Data sustainability challenges

The durational perspective sensitizes us to the tensions involved in any journey that seeks to align the needs of the present with the needs of the future. Here, “legacy” data provide potentially valuable options for moving forward. Liede et al. (2020, p. 676) discuss data in the biobank context, noting that “new samples require time, resources, communication, educating health care personnel and researchers, interventions, and so on; legacy samples are already there and provide unique research opportunities not available with freshly collected samples.” A recent study on Lyme borreliosis used data collected 50 years ago, when the disease itself was not even yet known (Liede et al., 2020). The study led to the important revelations of the prevalence of the disease during the Finnish agrarian society of the 1960s and 1970s, compared to the present service-based society (Cuellar, Dub, Sane, & Hytonen, 2020). The durational perspective highlights the value in understanding similarities and continuity, as well as differences and discontinuity, between past, present, and future.

Where a durational perspective is traceable in data governance studies, it often is fragmented and implicit in terms of recommending roles and practices “linking” to the past. For example, in terms of suggesting “data provenance” routines, we find studies espousing ways of going back to and double checking the data source and how the data have been used over time (Lee et al., 2017). We also see implicit, loosely defined expectations of the future: Data will be used by actors in the future, which is the reason for the data initiatives to exist. Certain roles – for instance, those involving making decisions about metadata (Abraham et al., 2019; Khatri & Brown, 2010) – further implicitly indicate an expectation about users in the future who will benefit from metadata. Where time is more explicitly present is in notions of the data lifecycle, including its retention and retirement and the total lifecycle costs (Khatri & Brown, 2010; Link et al., 2017).

The durational perspective suggests that imagining the needs of future users of data can be difficult because future use depends on new technological and scientific discoveries. Leonelli and Tempini (2020, p. 9) warn that data journeys are not always, or even frequently, smooth because they involve movement of data across many “sites,” where sites encompass temporal intervals and relations involving diverse interests (i.e., motivated by different commitments, expertise, know-how, and views). Building on Feenberg (2001, 2010a, 2010b) and Aanestad (2011), Chiasson et al. (2018, p. 373) write that “[s]ociotechnical futures evolve not only in relation to which values and interests have been translated into the technical solutions of the past or present (Aanestad, 2011), but also depend on whose values and interests are vying for attention and consideration and may thus become taken-for-granted facts in the future.”

Further, the data necessary for solving future problems may not have been collected and stored in the past. For example, the pursuit to understand the causes for current and future health disparities in the U.S. assumes availability of data that were never collected in the past. Conflicts arise between the resources required to optimize the present use of the data versus ensuring its availability and reusability in the future. Accommodation for yet another future generation of users influences current data practices (Barley, 2015). In addition, new laws or policies affecting data may be enacted, but compliance may be stymied by past decisions or current moralities about the data (Stelmaszak & Wagner, 2022). As in the Lyme borreliosis case, data from the past would need to be re-digitized in terms of “what is considered to be the phenomenon” and “what is considered to be data about the phenomenon” (Jones, 2019). A more recent example is the use of 1918 influenza data to infer insights for Covid-19 (Liang, Liang, & Rosen, 2021; Mamelund, 2018; Martini, Gazzaniga, Bragazzi, & Barberis, 2019). Similar data deficiencies continued with Covid-19 that existed with the 1918 influenza pandemic (Masiero, 2020; Milan, Trere, & Masiero, 2021).

Hence, the extant literature provides clues about the potential similarities and differences between current and future generations from a durational perspective. Yet, we perceive more opportunity, and even the necessity, to understand what data sustainability from a durational perspective entails – in particular, because tensions may emerge if many actors having different values and interests want to use the same data in the future. Similarly, there may be different expectations of who those future users may be, and which ones, among them, are important and legitimate and the one for whom the data should be “prepared.”

## 3.4.2. Research implications

The durational perspective puts forward temporal work that renders time as a resource for action. Temporal work involves interpretations of the past and present, and projections of the future (Bansal, Reinecke, Suddaby, & Langley, 2022; Kaplan & Orlikowski, 2013). As researchers “go back to the future,” past understanding enriches opportunities for acquiring experience, exploiting external developments, and learning from delayed outcomes (Berends & Antonacopoulou, 2014). Yet, how to implement a durational perspective in practice, in terms of incorporating it into current data governance models or enacting it in day-to-day data management practices, is an important research question. How is implementation affected by temporal horizons and orientations, temporal coordination mechanisms, and moralities across time (Bansal et al., 2022)?

A durational perspective indicates that temporal intervals are not temporal structures or constraints; rather, they are springboards for action, and they need to be linked to achieve data sustainability. The durational perspective encourages people to reach back to reinvigorate older data through links and assemblances that were not originally envisioned. That is, simply transitioning data across technological systems and translating data across users in networks are insufficient goals; researchers and other data users might need to go back and forth in time to revisit old data and to pose new questions in entirely new domains; they also might need to ensure that data use today does not compromise possibilities for the future. How can old data about the environment collected in very different manners be used to contrast, challenge, and supplement new data? Balancing these temporal challenges requires negotiating and making trade-offs and transforming meanings. In such contexts, processes, domain-specific knowledge, and commonly used knowledge may need to be both translated and transformed to achieve effective sharing and analysis of past data, as well as translation of what data (along with its metadata) could mean today and in the future. That is, the durational perspective goes beyond the relational perspective by looking at translations back and forth in time.

Future research could take steps toward an operationalization of the durational perspective by investigating several questions tied to the temporal orientations of past and present actors who participate in data infrastructures. What temporal orientations are manifested in the actions of actors involved in data governance or data processing, or of actors acting as data contributors? What role does the past play, and what tools for reinterpreting the past are developed (e.g., hindcasting and forecasting)? And how are alternative and conflicting interpretations of the past and the future negotiated?

Future research can explore how narratives serve as a mechanism to intertwine past, present, and future (Ricoeur, 1984), as well as how narratives serve as essential coordination mechanisms, not only in real time but also over time (Bartel & Garud, 2009) and especially prospectively (van Lente & Rip, 1998). Prospective narratives serve as temporal coordination mechanisms, allowing disparate social and material elements to become mutually entrained along an unfolding path. Because narratives tie several generations of individuals and companies together into a common fate, the very assumptions of, for instance, data ownership might need to be reexamined. Leonelli (2015) remarked that the more distance the data travel from the format and medium of the original point of capture, the harder it is to identify who counts as the author and owner.

In the durational perspective, a key challenge involves the values, or moralities, that gain prominence over others, creating path dependencies that shut down paths to alternative developments (Chiasson et al., 2018; Gray et al., 2022). When values become inscribed into technologies, going back to change the decisions made in the past – without unraveling an entire chain of interdependent connections among the technological components of the exchange system – is made increasingly difficult. Can the range of values that are closed at certain points be reopened? For example, are the prospects of such openings critical to move the discussion beyond individual privacy, security, and misuse to longer term societal implications? From the durational perspective, rather than the past being an impediment, or something inferior, it is the very fabric and basis for our actions. More provocatively, what may be viewed as risk or stigmatized as mistake in the present could well be considered progress in the future, when events are reinterpreted and data sustainability is considered.

The durational perspective encourages research and practice to construct and debate futures that are connected to the past and the present (Chiasson et al., 2018). Orienting to the future requires paying attention to “durable presents” (Risan, 2006, in Aanestad,

2011). Alternative data governance and data management practices provide different paths and have different implications for suppressing or promoting data from the past and present. Here again, we encourage long-term horizons going both back and forth in time. As noted by Feenberg (2010b, p. 9, in Chiasson et al., 2018, p. 373), the consequences of technology choices, “invisible in the immediate zone of action, become visible when a wider or longer range view is available.” Aanestad (2011, p. 36) also raise pertinent questions: “How can we distinguish between durability that restricts the envisioned and desired futures from becoming realised, versus durability that allows cumulative innovation? …How does what we construct today persist for a long time, how do our creations endure, both in intended and unintended ways?”

## 4. Discussion and implications

This paper advances the discourse on data sustainability for long-term knowledge discoveries – an important, although little-discussed, aspect of data in data governance. Data sustainability is data's capacity to endure across technological and human generations. In this case, data accumulated in the present and past is managed so as to meet the needs of the present generation, with a governance and use, that does not compromise the data's capability for reuse in the future by different sets of heterogeneous, independent, and unknown actors. Well-designed data infrastructures are crucial for data sustainability and for supporting the resolution of grand challenges and their wicked problems. Such data infrastructures digitize and accumulate data from many different organizational and individual entities, and they are critical to address global challenges in healthcare, climate, poverty, crime, and other domains. Progression in these global grand challenges is dependent on data sustainability. The discourse on data sustainability can make contributions to the data governance and sustainability literatures.

## 4.1. Contributions to data governance literature

Data sustainability introduces long terms horizons – past and future – to the data governance conversation, pointing to the need to look beyond current organizations and current technologies in data governance frameworks (e.g., Abraham et al., 2019; Khatri & Brown, 2010; Lee et al., 2017, 2018; Lis & Otto, 2020). Our review of contemporary data governance literature suggests that attention has broadened from organizational to interorganizational concerns, but broadening has not happened in terms of perspectives on time. Where the data governance literature has focused on data’s ability to “endure” and to be reused, both within and across organizations, the focus has remained within the timespan of implemented technologies, existing collaborations, and present or short-term aims. Centering on data for real-time or near-time action and interaction is important, but it has come at the expense of duration, the long-term views of phenomena, and of how data might be relevant to distant future generations of technologies and people. Data sustainability sensitizes us to ask questions about and take into consideration those distant pasts and futures. At least, it reminds us to not ignore them.

To examine data sustainability from the temporal perspective, we introduced three perspectives on data sustainability, drawing on Garud and Gehman (2012). The three perspectives rest on different assumptions and foreground unique yet interrelated and even compounding challenges to influence data sustainability. The evolutionary perspective highlights obstacles to data sustainability produced by technological disruptions; the relational perspective highlights the necessity of and challenges tied to data's social embeddedness; and the durational perspective highlights the lack of continuity and work required to achieve continuity across past, present, and future.

Although these challenges involve different temporal intervals and can be considered complementary over time, they require actors to navigate competing demands in the present. The evolutionary perspective draws our attention to the need to release and decouple data from material structures to make data capable of transition across technological generations. The relational perspective emphasizes the need for the data to be embedded and integrated to acquire meaning and to make a difference. From the durational perspective, sustainability foregrounds the need for us to learn to go back to data resources that were previously pushed aside, forgotten, or viewed as inferior as we struggle not only to imagine alternative futures, but also to understand, solve, or even prevent problems in those futures. This constant curiosity about the past is in stark contrast to the contemporary mindset and the tendency to look only to the future and only to see potential in the continuously improved and “bigger” datasets that we generate or plan to generate today. However, “past” data will not be at the disposal of future generations without data practices in the present that ensure future use. Juxtaposing these challenges suggests that data sustainability is a highly complex phenomenon that involves the navigation of ongoing shifts, relational processes, and a continuous flow of competing demands.

In discussing the three perspectives on data sustainability, we raised new data governance questions for research. To navigate the complexity, research on data governance needs to consider all three sustainability perspectives – evolutionary, relational, and durability – as well as their interactions. As noted by Garud and Gehman (2012, p. 980), allowing a conversation among the perspectives may prevent sustainability actors from “talking past one another” or “performing contradictory and conflicting initiatives.”

Each of the three sustainability perspectives of Garud and Gehman (2012) also has methodological implications. The evolutionary perspective requires retrospective studies to understand shifts from one socio-technical regime to another, or it potentially requires a prolonged longitudinal study. The relational perspective suggests following various actors “in the making” of data. The durational perspective emphasizes narratives where temporal agency involves going back to ideas from the past to move forward, or what Garud and Gehman (2012, p. 992) refer to as “zip[ping] back and forth in time.” There are numerous possibilities beyond these, and we call for further development of methodological approaches that could capture how data sustainability is (not) strived for, (not) achieved, and with what consequences, in the governance of data infrastructures.

## 4.2. Contributions to sustainability literature

Data sustainability also contributes to contemporary discussions about sustainability in the IS literature. The social dimensions of sustainability (Monson, 2021) emphasize the need to consider social inclusion and justice, asking how IS innovation may affect conditions for socially disadvantaged groups (Davison, 2021; Young, Selander, & Vaast, 2019) and the endurance of (online) social communities (Curto-Millet and Jiménez, 2022; Mindel et al., 2018). Meanwhile, IS scholars also address the environmental dimensions of sustainability by looking at both the negative and positive effects of IS on the natural environment (Leidner et al., 2022; Seidel et al., 2013; Seidel, Kruse, Szekely, Gau, & Stieger, 2018), including on the quality of air, water, and soil (Jenkin, Webster, & McShane, 2011; Malhotra, Melville, & Watson, 2013) and on wildlife diversity (Shan, Mingwei, Li, & Sandeep, 2021). Both the social and environmental streams assume that digital artifacts, including data, are a means to achieve socially sustainable (inclusive, fair) and environmentally sustainable (reduced negative effects on the natural resources) organizations, communities, and societies. Digital artifacts, such as data visualizations, can play a role by providing relevant affordances – for example, allowing us to see the results of our actions on the environment (Seidel et al., 2018, 2013); with such insight, we may be incentivized to reduce energy consumption and thus CO $^{2}$ emissions (Watson et al., 2010; Wunderlich et al., 2019).

Yet, in the absence of data sustainability, such assumptions about the power of data to support change may not hold. Technological advances in hardware and software and new users trying to improve environmental and social sustainability may find that the data cannot be transitioned and translated across machines and users, thus leading to less sustainable data over time. That is, progression in one dimension of sustainability may threaten progression in another. In this case, we see the dependence of both environmental sustainability (endurance of natural resources and prevention of harm to nature) and social sustainability (endurance of human resources and prevention of exclusion of populations) on data sustainability. Lack of data sustainability means the failure of both data and its meta-data to endure over technological and human generations. It means the data and meta-data cannot be understood and interpreted by diverse actors in different networks with different belief systems. Such lacunae diminish the prospects of deliberating and collectively acting on broad, tough questions to address grand challenges. Studying such lacunae requires new scientific approaches.

As with sustainability in general, data sustainability has normative connotations. Yet, deciding on which data warrant substantial investments in sustainability and on how to operationalize data sustainability involves trade-offs. We are not suggesting that all data should be given the capacity to endure across technological and human generations, or that data sustainability should always be prioritized. Data sustainability requires negotiations between needs in the present, partially known needs tied to upcoming technological and human generations, and largely unknown needs among future technological generations and users. Such negotiations constitute an important dimension of data governance in data infrastructures that are aiming to solve grand challenges – and they need theoretical arguments that can facilitate the understanding of the alternatives at play and of what is at stake.

The IS field has an opportunity to lead the conversations on data governance and to contribute to environmental and social sustainability. These conversations have never been as timely as in medical biobanks and health, smart computer grids, “green” solutions for transport, and inclusive ways of building cities, among others. Neither the field nor global humanity can just rely on “time” and simply expect better outcomes in the future – when technologies will be smarter and future generations of human users will possess more knowledge.

## 5. Conclusion

In the world of ever-faster technological and social change and with the beliefs about data ubiquity and the realities of the abundance in networks, data's endurance is a grand challenge under the broader umbrella of sustainability. We foreground the importance of data sustainability in data infrastructures that aim to solve complex societal problems and to enable long-term knowledge discoveries. As data are shared across sectors and industries to engender more complex solutions (e.g., sustainable smart cities, health, food, and energy), these data infrastructures will become increasingly common and expansive. We introduce three perspectives on data sustainability and offer insights about the sustainability challenges that become visible from these perspectives individually, as well as when one perspective informs another. We argue that technology progression without data sustainability is unlikely to bring sustainable futures. The future research areas outlined provide multiple avenues forward in scholarship about data governance and sustainability.

## Acknowledgements

Anna Essen's work was funded by the MM Wallenberg foundation (project number: 2021.0074).

## References

Aaen, J., Agger Nielsen, J., & Carugati, A. (2022). The dark side of data ecosystems: A longitudinal study of the DAMD project. European Journal of Information Systems, 31(3), 288–312.

Aaltonen, A., Alaimo, C., & Kallinikos, J. (2021). The making of data commodities: Data analytics as an embedded process. Journal of Management Information Systems, 38(2), 401–429.

Aaltonen, A., & Tempini, N. (2014). Everything counts in large amounts: A critical realist case study on data-based production. Journal of Information Technology, 29, 97–110.

Aanestad, M. (2011). Information systems innovation research: Between novel futures and durable presents. 27-42. In M. Chiasson, O. Henfridsson, H. Karsten, & J. I. DeGross (Eds.), Researching the future in information systems. IFIP WG 8.2 working conference Turku, Finland, June 2011 proceedings. IFIP AICT 356.IFIP advances in information and communication technology. Springer.

Abbasi, A., Suprateek, S., & Roger, C. (2016). Big data research in information systems: Toward an inclusive research agenda. Journal of the Association for Information Systems, 17(2), 3.

Abdelnour, S., Hasselbladh, H., & Kallinikos, J. (2017). Agency and institutions in organization studies. Organization Studies, 38(12), 1775–1792.

Abraham, R., Schneider, J., & vom Brocke, J. (2019). Data governance: A conceptual framework, structured review, and research agenda. International Journal of Information Management, 49, 424–438.

Alaimo, C., & Kallinikos, J. (2017). Computing the everyday: Social media as data platforms. The Information Society, 33(4), 175–191.

Alaimo, C., & Kallinikos, J. (2021). Managing by data: Algorithmic categories and organizing. Organization Studies, 42(9), 1385–1407.

Alaimo, C., & Kallinikos, J. (2022). Organizations decentered: Data objects, technology and knowledge. Organization Science, 33(1), 19–37.

Alaimo, C., Kallinikos, J., & Aaltonen, A. (2020). Data and value. In S. In Nambisan, K. Lyytinen, & Y. Yoo (Eds.), Handbook of digital innovation. Edward Elgar Publishing.

Alhassan, I., Sammon, D., & Daly, M. (2016). Data governance activities: An analysis of the literature. Journal of Decision Systems, 25(1), 64–75.

Bailey, D. E., Leonardi, P. M., & Barley, S. R. (2012). The lure of the virtual. Organization Science, 23(5), 1485–1504.

Bansal, P., Reinecke, J., Suddaby, R., & Langley, A. (2022). Temporal work: The strategic organization of time. Strategic Organization, 20(1), 6–19.

Barley, W. C. (2015). Anticipatory work: How the need to represent knowledge across boundaries shapes work practices within them. Organization Science, 26(6), 1612–1628.

Barr-Kumarakulasinghe, C., & Boon-Kwee, N. (2022). Protecting the unprotected consumer data in internet of things: Current scenario of data governance in Malaysia. Sustainability, 14(16), 9893.

Bartel, C. A., & Garud, R. (2009). The role of narratives in sustaining organizational innovation. Organization Science, 20, 107–117.

Benfeldt, O., Persson, J. S., & Madsen, S. (2020). Data governance as a collective action problem. Information Systems Frontiers, 22(2), 299–313.

Berends, H., & Antonacopoulou, E. (2014). Time and organizational learning: A review and agenda for future research. International Journal of Management Reviews, 16(4), 437–453.

Bergson, H. (1934/2007). The Creative Mind. Mineola: Dover Publications.

Boland, R. J., & Collopy, F. (2004). Design matters for management. In Managing as designing (pp. 3–18). Stanford University Press.

Callon, M. (1987). Society in the making: The study of technology as a tool for sociological analysis. In W. E. Bijker, T. P. Hughes, & T. J. Pinch (Eds.), Social construction of technological systems (pp. 83–103). Cambridge: MIT Press.

Chiasson, M., Davidson, E., & Winter, J. (2018). Philosophical foundations for informing the future through IS research. European Journal of Information Systems, 27(3), 367–379.

Constantinides, P., Henfridsson, O. P., & G. G.. (2018). Introduction—platforms and infrastructures in the digital age. Information Systems Research, 29(2), 381–400. https://doi.org/10.1287/isre.2018.0794

Constantiou, I. D., & Kallinikos, J. (2015). New games, new rules: Big data and the changing context of strategy. Journal of Information Technology, 44–57.

Cuellar, J., Dub, T., Sane, J., & Hytonen, J. (2020). Seroprevalence of Lyme borreliosis in Finland 50 years ago. Clinical Microbiology and Infection, 26, 632–636.

Curto-Millet, D., & Jimenez, A. (2022). The sustainability of open source commons. European Journal of Information Systems. https://doi.org/10.1080/0960085X.2022.2046516

Data Governance Institute. Data governance definition. Retrieved from. Accessed January 14, 2023 https://datagovernance.com/the-data-governance-basics/definitions-of-data-governance/.

Davidson, K. (2014). A typology to categorize the ideologies of actors in the sustainable development debate. Sustainable Development, 22(1), 1–14.

Davison, R. M. (2021). Diversity and inclusion at the ISJ. Information Systems Journal, 31(3), 347–355.

Diamond, C. C., Mostashari, F., & Shirky, C. (2009). Collecting and sharing data for population health: A new paradigm. Health Affairs, 28(2), 454–466.

Dosi, G. (1982). Technological paradigms and technological trajectories: A suggested interpretation of the determinants and directions of technical change. Research Policy, 11, 147–162.

Edwards, P. N. (2010). A vast machine: Computer models, climate data, and the politics of global warming. Cambridge, MA: MIT Press.

Feenberg, A. (2001). Democratizing technology: Interests, codes, rights. The Journal of Ethics, 5(2), 177–195.

Feenberg, A. (2010a). Between reason and experience: Essays in technology and modernity. Cambridge: MIT Press.

Feenberg, A. (2010b). Ten paradoxes of technology. Techne, 14(1), 3–13.

Fox, M., Tost, L. P., & Wade-Benzoni, K. A. (2010). The legacy motive: A catalyst for sustainable decision-making in organizations. Business Ethics Quarterly, 20(2), 153–185.

Gaitanou, P., Andreou, I., Sicilia, M. A., & Garoufallou, E. (2022). Linked data for libraries: Creating a global knowledge space, a systematic literature review. Journal of Information Science, 01655515221084645.

Garud, R., & Gehman, J. (2012). Metatheoretical perspectives on sustainability journeys: Evolutionary, relational and durational. Research Policy, 4, 980–995.

Geels, F. W., & Schot, J. (2007). Typology of sociotechnical transition pathways. Research Policy, 36, 399–417.

Gersick, C. (2020). Reflections on revolutionary change. Journal of Change Management, 20(1), 7–23.

Gille, F., Vayena, E., & Blasimme, A. (2020). Future-proofing biobank's governance. European Journal of Human Genetics, 28, 989–996.

Granovetter, M. (1985). Economic action and social structure: The problem of embeddedness. American Journal of Sociology, 91, 481–510.

Gray, B., Briscoe, F., & Ferraro, C. D. (2022). The technological entrainment of moral issues: The case of genomic data markets. Academy of Management Journal. https://doi.org/10.5465/amj.2019.1202

Halfmann, G. (2020). Material origins of a data journey in ocean science: How sampling and scaffolding shape data practices. In S. Leonelli, & N. Tempini (Eds.), Data journeys in the sciences (pp. 27–44). Springer Open.

Holm, S., & Thomas, P. (2017). Big data and health research-the governance challenges in a mixed data economy. Journal of Bioethical Inquiry, 14(4), 515–525.

Hovorka, D., & Peter, S. (2021). Research perspectives: From other worlds: Speculative engagement through digital geographies. Journal of the Association for Information Systems, 22(6), 1736–1752.

Janssen, M., Brous, P., Estevez, E., Barbosa, L. S., & Janowski, T. (2020). Data governance: Organizing data for trustworthy artificial intelligence. Government Information Quarterly, 37(3), Article 101493.

Jarvenpaa, S. L., & Markus, M. L. (2019). Data perspective in digital platforms: Three Tales of genetic platforms. In Hawaii international conference on system sciences (HICSS). January 5, 2019.

Jarvenpaa, S. L., & Markus, M. L. (2020). Data sourcing and data partnerships: Opportunities for IS sourcing research. Information Systems Outsourcing: The Era of Digital Transformation, 61–79.

Jenkin, T. A., Webster, J., & McShane, L. (2011). An agenda for ‘green’ information technology and systems research. Information and Organization, 21(1), 17–40. https://doi.org/10.1016/j.infoandorg.2010.09.003

Jones, M. (2019). What we talk about when we talk about (big) data. The Journal of Strategic Information Systems, 28(1), 3–16.

Jussupow, E., Spohrer, K., Heinzl, A., & Gawlitza, J. (2021). Augmenting medical diagnosis decisions? An investigation into Physicians' decision-making process with artificial intelligence. Information Systems Research, 32(3), 713–735.

Kallinikos, J., Aaltonen, A., & Aatilla, M. (2013). The ambivalent ontology of digital artifacts. MIS Quarterly, 37(2), 357–370.

Kaplan, S., & Orlikowski, W. J. (2013). Temporal work in strategy making. Organization Science, 24(4), 965–995.

Karaca, K. (2020). What data get to travel in High Energy Physics? The construction of data at the large hadron collider. In S. Leonelli, & N. Tempini (Eds.), Data journeys in the sciences (pp. 45–58). Springer Open.

Khatri, V., & Brown, C. V. (2010). Designing data governance. Communications of the ACM, 53(1), 148–152.

Korhonen, J. J., Melleri, I., Hiekkanen, K., & Helenius, M. (2013). Designing data governance structure: An organizational perspective. GSTF Journal on Computing, 2(4), 11–17.

Koutroumpis, P., Leiponen, A., & Thomas, L. D. W. (2020). Markets for Data. Industrial and Corporate Change, 29(3), 645–660.

Laine, S., Lee, C., & Nieminen, M. (2015). Transparent data supply for open information production processes. ECIS completed research papers. Paper 115.

Lampert, C. K., & Southwick, S. B. (2013). Leading to linking: Introducing linked data to academic library digital collections. Journal of Library Metadata, 13(2–3), 230–253.

Latour, B. (1986). The powers of association. In J. Law (Ed.), Power, action and belief (pp. 264–280). London: Routledge.

Latour, B. (1994). On technical mediation. Common Knowledge, 3, 29–64.

Law, J. (2009). Actor network theory and material semiotics. In B. S. Turner (Ed.), The new Blackwell companion to social theory (pp. 141–158). Malden: Blackwell.

Lebovitz, S., Levina, N., & Lifshitz-Assaf, H. (2021). Is AI ground truth really “true”? The dangers of training and evaluating AI tools based on experts’ know-what. MIS Quarterly, 45(3b), 1501–1525.

Lebovitz, S., Lifshitz-Assaf, H., & Levina, N. (2022). To engage or not to engage with AI for critical judgments: How professionals deal with opacity when using AI for medical diagnosis. Organization Science, 33(1), 126–148.

Lee, S. U., Zhu, L., & Jeffery, R. (2017). Data governance for platform ecosystems: Critical factors and the state of practice. In Twenty first Pacific Asia conference on information systems (pp. 1–12).

Lee, S. U., Zhu, L., & Jeffery, R. (2018). A contingency-based approach to data governance design for platform ecosystems. In 2018 proceedings of Pacific Asia conference on information systems (PACIS) (p. 168).

Legner, C., Tobias, P., & Boris, O. (2020). Accumulating design knowledge with reference models: Insights from 12 years' research into data management. Journal of the Association for Information Systems, 21(3), 2–7.

Leidner, D., Sutano, J., & Goutas, L. (2022). Multifarious roles and conflicts on an interorganizational green IS. MIS Quarterly, 46(1), 591–608.

van den Broek, T., & van Veenstra, A. F. (2015). Modes of governance in inter-organizational data collaborations. Twenty-Third European Conference on Information Systems, (ECIS), 1–12.

van Lente, H., & Rip, A. (1998). Expectations in technological developments: An example of prospective structures to be filled in by agency. In C. Disco, & B. van der Meulen (Eds.), Getting new technologies together (pp. 195–220). New York: de Gruyter.

Leonelli, S. (2015). What counts as scientific data? A relational Framework. Philosophy of Science, 82(5), 810–821.

Leonelli, S., & Tempini, N. (2020). Data journeys in the sciences. Springer Open.

Liang, S. T., Liang, L. T., & Rosen, J. M. (2021). COVID-19: A comparison to the 1918 influenza and how we can defeat it. Postgraduate Medical Journal, 97(1147), 273–274.

Liede, S., Soini, S., & Southerington, T. (2020). Comment on “Salokannel et al., Legacy samples in Finnish biobanks: Social and legal issues related to the transfer of old sample collections into biobanks”. Human Genetics, 139, 675–677.

Link, G., Lumbard, K., Conboy, K., Feldman, M., Feller, J., George, J., ... Willis, M. (2017). Contemporary issues of open data in information systems research.

Considerations and recommendations. Communications of the Association for Information Systems, 41. https://doi.org/10.17705/1CAIS.04125

Lis, D., & Otto, B. (2020). Data governance in data ecosystems – insights from organizations. In AMCIS 2020 Proceedings (p. 12).

Lyytinen, K., Sorensen, C., & Tilson, D. (2017). Generativity in digital infrastructures: A research note. In R. D. Galliers, & M. K. Stein (Eds.), Handbook on IS companion book (pp. 253–275). Routledge.

Malhotra, A., Melville, N. P., & Watson, R. T. (2013). Spurring impactful research on information systems for environmental sustainability. MIS Quarterly, 37(4), 1265–1274.

Mamelund, S. E. (2018). 1918 pandemic morbidity: The first wave hits the poor, the second wave hits the rich. Influenza and Other Respiratory Viruses, 12(3), 307–313.

Markus, M. L. (2001). Toward a theory of knowledge reuse: Types of knowledge reuse situations and factors in reuse success. Journal of Management Information Systems, 18(1), 57–93.

Markus, M. L. (2016). 11 obstacles on the road to corporate data responsibility. Big data is not a monolith, 143.

Markus, M. L., & Bui, Q. N. (2012). Going concerns: The governance of interorganizational coordination hubs. Journal of Management Information Systems, 28(4), 163–198.

Martini, M., Gazzaniga, V., Bragazzi, N. L., & Barberis, I. (2019). The Spanish influenza pandemic: A lesson from history 100 years after 1918. Journal of Preventive Medicine and Hygiene, 60(1), E64.

Masiero, S. (2020). COVID-19: What does it mean for digital social protection? Big Data & Society, 7(2), 2053951720978995.

McKinney, E., & Yoo, C. (2010). Information about information: A taxonomy of views. MIS Quarterly, 34(2), 329–344.

Melville, N. P. (2010). Information systems innovation for environmental sustainability. MIS Quarterly, 34(1), 1–21. https://doi.org/10.2307/20721412

Milan, S., Treré, E., & Masiero, S. (2021). COVID-19 from the margins: Pandemic invisibilities, policies and resistance in the datafied society. Theory on Demand, 40.

Mindel, V., Mathiassen, L., & Rai, A. (2018). The sustainability of polycentric information commons. MIS Quarterly, 42(2), 607–614. https://doi.org/10.25300/MISQ/2018/14015

Monson, M. (2021). Socially responsible design science in information systems for sustainable development: A critical research methodology. European Journal of Information Systems. https://doi.org/10.1080/0960085X.2021.1946442

Monteiro, E., & Parmiggiani, E. (2019). Synthetic knowing: The politics of the internet of things. MIS Quarterly, 43(1), 167–184.

Nelson, R. R., & Winter, S. G. (1982). An evolutionary theory of economic change. Cambridge: Harvard University Press.

Ocasio, W., Rhee, L., & Milner, D. (2020). Attention, knowledge, and organizational learning. In The Oxford handbook of group and organizational learning (pp. 81–94).

Oliveira, M. I. S., Lima, G. D. F. B., & Loscio, B. F. (2019). Investigations into data ecosystems: A systematic mapping study. Knowledge and Information Systems, 61(2), 1–42.

Orlikowski, W. J. (1996). Improvising organizational transformation over time: A situated change perspective. Information Systems Research, 7(1), 63–92.

Osterlie, T., & Monteiro, E. (2020). Digital sand: The becoming of digital representations. Information and Organization, 30, Article 100275.

Otto, B. (2011). A morphology of the organisation of data governance. In ECIS 2011 proceedings (p. 272).

Otto, B., & Jarke, M. (2019). Designing a multi-sided data platform: Findings from the international data spaces case. Electronic Markets, 29, 561–580.

Perkmann, M., & Schildt, H. (2015). Open data partnerships between firms and universities: The role of boundary organizations. Research Policy, 44(5), 1133–1143.

Pickering, A. (1993). The mangle of practice: Agency and emergence in the sociology of science. American Journal of Sociology, 99, 559–589.

Porac, J. F. (1997). Local rationality, global blunders, and the boundaries of technological choice: Lessons from IBM and DOS. In R. Garud, P. R. Nayyar, &

de Prieelle, F., de Reuver, M., & Rezaei, J. (2022). The role of ecosystem data governance in adoption of data platforms by internet-of-things data providers: Case of Dutch horticulture industry. IEEE Transactions on Engineering Management, 69(4), 940–950.

Rathnam, S. (2022). Data challenges faced by technology-based companies: privacy, regulations, semantics, and measurement. In Luncheon Presentation at McCombs School of Business, January 21.

Ribes, D., & Polk, J. B. (2015). Organizing for ontological change: The kernel of an AIDS research infrastructure. Social Studies of Science, 45(2), 214–241. Ricoeur, P. (1984). Time and narrative. Chicago: University of Chicago Press.

Risan, L. (2006). The duration of the present and the risk of not telling large stories. EASST. Review, (October). http://www.easst.net/review/oct2006/risan.

Rosenbaum, S. (2010). Data governance and stewardship: Designing data stewardship entities and advancing data access. Health Services Research, 1442–1455.

Rychnovska, D. (2021). Anticipatory governance in biobanking: Security and risk management in digital health. Science and Engineering Ethics, 27(3), 1–18.

Salokannel, M., Tarkkala, H., & Snell, K. (2019). Legacy samples in Finnish biobanks: Social and legal issues related to the transfer of old sample collections into biobanks. Human Genetics, 138, 1287–1299.

Sarker, S., Chatterjee, S., Xiao, X., & Elbanna, A. (2019). The sociotechnical axis of cohesion for the IS discipline: Its historical legacy and its continued relevance. MIS Quarterly., 43(3), 695–720. https://doi.org/10.25300/MISQ/2019/13747

Seidel, S., Kruse, L., Szekely, N., Gau, M., & Stieger, D. (2018). Design principles for sensemaking support systems in environmental sustainability transformations. European Journal of Information Systems, 27(2), 221–247. https://doi.org/10.1057/s41303-017-0039-0

Seidel, S., Recker, J., & Brocke, J. (2013). Sensemaking and sustainable practicing: Functional affordances of information systems in green transformations. MIS Quarterly, 37, 1275–1299. https://doi.org/10.25300/MISQ/2013/37.4.13

Shabani, M. (2021). The data governance act and the EU's move towards facilitating data sharing. Molecular Systems Biology, 17(3), Article e10229.

Shan, L., Mingwei, P., Li, L., Pee, G., & Sandeep, M. S. (2021). Sustainability design principles for a wildlife management analytics system: An action design research. European Journal of Information Systems, 30(4), 452–473. https://doi.org/10.1080/0960085X.2020.1811786

Sharma, R., Mithas, S., & Kankanhalli, A. (2014). Transforming decision-making processes: A research agenda for understanding the impact of business analytics on organisations. European Journal of Information Systems, 23, 433–441.

Simon, H. (1996). The sciences of the artificial (3rd ed.). Cambridge, MA: MIT Press.

Sjoukema, J.-W., Samia, J., Bregt, A. K., & Crompvoets, J. (2022). The governance of INSPIRE: Evaluating and exploring governance scenarios for the European spatial data infrastructure. ISPRS International Journal of Geo-Information, 11(2), 141. MDPI AG. Retrieved from https://doi.org/10.3390/ijgi11020141.Skloot, R. (2018). The immortal life of Henrietta lacks. Picador.

Stelmaszak, M., & Wagner, E. (2022). What flows through data infrastructures: Blockages, bends, and bottlenecks in sharing gender data between institutions. In The Proceedings of the 2022 International Conference of Information Systems (ICIS), 9.

Sturm, T., Gerlach, J., Pumplun, L., Mesbah, N., Peters, F., Tauchert, C., ... Buxmann, P. (2021). Coordinating human and machine learning for effective organizational learning. MIS Quarterly, 45(3b), 1581–1602.

Sudlow, C., Gallacher, J., Allen, N., Beral, V., Burton, P., Danesh, J., et al. (2015). UK biobank: An open access resource for identifying the causes of a wide range of complex diseases of middle and old age. PLoS Medicine, 12(3), Article e1001779.

Susha, I., Janssen, M., & Verhulst, S. (2017a). Data collaboratives as a new frontier of cross sector partnerships in the age of open data: Taxonomy development. In Proceedings of the 50th Hawaii international conference on system sciences in Waikoloa, HI.

Susha, I., Janssen, M., & Verhulst, S. (2017b). Data collaboratives as “bazaars”?: A review of coordination problems and mechanisms to match demand for data with supply. Transforming Government: People, Process and Policy, 11(1), 157–172.

Tallon, P., Ramirez, A. R., & Short, J. (2013). The information artifact in IT governance: Toward a theory of information governance. Journal of Management Information Systems, 30(3), 145–181.

Tallon, P. P., & Scannell, R. (2007). Information lifecycle management. Communications of the ACM, 50(11), 65–69.

Tempini, N. (2016). Science through the “Golden security triangle”: Information security and data journeys in data-intensive biomedicine. In Presented at the 37th international conference on information systems, Dublin, Ireland, 11-14 December 2016.

Thompson, K., & Richard, J. (2013). Moving our data to the semantic web: Leveraging a content management system to create the linked open library. Journal of Library Metadata, 13, 290–309.

Tuomi, I. (1999). Data is more than knowledge implications of the reversed knowledge hierarchy for knowledge management and organizational memory. Journal of Management Information Systems, 16(3), 107–121.

Van de Ven, A. H., Polley, D. E., Garud, R., & Venkataraman, S. (1999). The innovation journey. New York: Oxford University Press.

Van den Brock, T., & van Veenstra, A. F. (2018). Governance of big data collaborations: How to balance regulatory compliance and disruptive innovation. Technological Forecasting and Social Change, 129, 330–338.

Wade-Benzoni, K. A. (2002). A golden rule over time: Reciprocity in intergenerational allocation decisions. Academy of Management Journal, 45, 1011–1028.

Watson, R. T., Boudreau, M. C., & Chen, A. J. (2010). Information systems and environmentally sustainable development: Energy informatics and new directions for the IS community. MIS Quarterly, 34(1), 23–38.

Weber, K., Otto, B., & Osterle, H. (2009). One size does not fit all—a contingency approach to data governance. Journal of Data and Information Quality, 1(1), 1–27. Weill, P., & Ross, J. W. (2004). IT governance. Boston: Harvard Business School Press.

Weitz, J., Toves, J., Vizine-Goetz, D., Naught, N., & Bremer, R. (2016). Mining MARC's hidden treasures: Initial investigations into how notes of the past might shape our future. Journal of Library Metadata, 16(3–4), 166–180.

Wessel, L., Baiyere, A., Ologeanu-Taddei, R., Cha, J., & Blegind Jensen, T. (2021). Unpacking the difference between digital transformation and IT-enabled organizational transformation. Journal of the Association for Information Systems, 22(1), art 6.

Winter, J. S., & Davidson, E. (2019). Big data governance of personal health information and challenges to contextual integrity. The Information Society, 35(1), 36–51. World Commission on Environment and Development (WCED). (1987). Our Common Future. Oxford, UK: Oxford University Press.

Wunderlich, P., Veit, D., & Sarker, S. (2019). Adoption of sustainable technologies: A mixed-methods study of German households. MIS Quarterly, 42, 673–691. https://doi.org/10.25300/MISQ/2019/12112

Yoo, Y., Boland, R., Lyytinen, K., & Majchrzak, A. (2012). Organizing for innovation in a digitized world. Organization Science, 23(5), 1213–1522.

Yoo, Y., Henfridsson, O., & Lyytinen, K. (2010). Research commentary—The new organizing logic of digital innovation: An agenda for information Systems Research. Information Systems Research, 21(4), 724–735.

Young, A., Selander, L., & Vaast, E. (2019). Digital organizing for social impact: Current insights and future research avenues on collective action, social movements, and digital technologies. Information and Organization, 29(3), Article 100257.

Zeitlyn, D. (2012). Anthropology in and of the archives: Possible futures and contingent pasts. Archives as anthropological surrogates. Annual Review of Anthropology, 41(1), 461–480.

Zuboff, S. (2015). Big other: Surveillance capitalism and the prospects of an information civilization. Journal of Information Technology, 30(1), 75–89.
