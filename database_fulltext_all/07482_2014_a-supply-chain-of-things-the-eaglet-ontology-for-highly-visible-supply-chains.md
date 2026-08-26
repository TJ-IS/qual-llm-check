---
otero_id: 7482
otero_key: "XUJ9ZHXG"
title: "A supply chain of things: The EAGLET ontology for highly visible supply chains"
authors: "Guido L. Geerts; Daniel E. O'Leary"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.09.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A supply chain of things: The EAGLET ontology for highly visible supply chains

Guido L. Geerts <sup>a,</sup>⁎, Daniel E. O'Leary

<sup>a</sup> Department of Accounting and MIS, The Alfred Lerner College of Business and Economics, University of Delaware, Newark, DE 19716, United States

<sup>b</sup> Marshall School of Business, University of Southern California, 3660 Trousdale Parkway, Los Angeles, CA 90089-0441, United States

## a r t i c l e i n f o

Available online xxxx

Keywords: EAGLET ontology Individual object identi<sup>fi</sup>cation Internet of Things Supply Chain of Things Traceability

## a b s t r a c t

Recently, technological developments, such as radio frequency identi<sup>fi</sup>cation (RFID), have facilitated the identi<sup>fi</sup>cation of individual things and information sharing regarding their behavior throughout the supply chain. Such developments have generated the capabilities of a highly visible supply chain (HVSC): a supply chain where the location of arbitrary individual things can be determined at any point in time by all appropriate supply chain partners, made possible by an “Internet of Things” for the supply chain, referred to as a “Supply Chain of Things.” A critical component of a Supply Chain of Things is an ontology to facilitate the visibility and interoperability of things along the supply chain. As a result, the objective of this paper is to de<sup>fi</sup>ne an ontology that leverages the availability of an individual thing's (object) identi<sup>fi</sup>cation information within the context of a standard set of economic phenomena that support multiple views in a range of data architectures. Our design science approach begins with a set of ontological primitives and gradually de<sup>fi</sup>nes structuring principles that provide guidance for the design of supply chain systems that are characterized by increased visibility and interoperability and which facilitate management of and collaborative decision making about supply chain activities. The EAGLET ontology is named after its <sup>fi</sup>ve primitives: Event, AGent, Location, Equipment, and Thing. The following are some of its unique characteristics: location and equipment are recognized as ontological primitives, and creating and destroying of containment structures is explicitly modeled; the economic phenomena underlying the supply chain are de<sup>fi</sup>ned from an independent view, as opposed to a trading-partner view; the supply chain is de<sup>fi</sup>ned from three different perspectives: the physical <sup>fl</sup>ow, the chain of custody, and the chain of ownership; event sequences that resemble the economic scripts underlying the supply chain are de<sup>fi</sup>ned.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

In real-world supply chains, goods sometimes cannot be found in a store's cluttered backroom, goods get lost in transit, goods arrive late, tainted goods cannot be traced back to their origins, etc. Many such problems stem from a lack of visibility of the individual objects (i.e., individual goods, cases of goods, pallets of goods, and even trucks of goods), and a lack of shared semantics in the supply chain. If the goods could inform supply chain participants of their current location, their past locations, what has happened to them, and who has handled them, then the preceding issues could be more easily addressed. If there was an Internet of Things [1] for the supply chain, i.e., if only there was a Supply Chain of Things, where things could interact with each other and other components of the supply chain, governed by speci<sup>fi</sup>c supply chain economic phenomena. A Supply Chain of Things could bring visibility to each individual item, generating a highly visible supply chain (HVSC), where the location and characteristics of all the things in the supply chain could be ascertained at any point in time. The generation of such a capability would require an appropriate semantic model that described the things and the corresponding economic phenomena.

The purpose of this paper is to develop such a model, in the form of an ontology that describes a Supply Chain of Things to create an HVSC capability.

## 1.1. Need for a Supply Chain of Things

Companies such as Metro and Walmart have used individual object identi<sup>fi</sup>cation (IoI) technologies to facilitate and support decision making regarding individual things in the supply chain, supply chain design and improving the customer experience, typically using radio frequency identi<sup>fi</sup>cation (RFID). In particular, IoI technologies provide real-time data about things that can be used by management to facilitate decision making, enabling forecasting and mitigating or eliminating out of stock situations [2]. Monitoring a speci<sup>fi</sup>c thing's velocity through the supply chain can determine if it is moving at the expected rate. If not, then managers of the supply chain can collaborate and decide to speed up or slow the <sup>fl</sup>ow so the goods arrive with locations prepared with proper resources for loading, unloading, and storage [3]. For example, recently, Metro noted that roughly 66% of its shipments from suppliers in Asia arrived more than <sup>fi</sup>ve days late, whereas 2% of shipments arrived early [4]. Because Metro uses a just-in-time approach, shipments must arrive on time; otherwise, demand will not be met with available goods, or there will be insuf<sup>fi</sup>cient warehousing space to

G.L. Geerts, D.E. O'Leary / Decision Support Systems xxx (2013) xxx–xxx

store goods that arrive early. Therefore, it is important to monitor the location of goods in the supply chain from Asia to determine if resources must be mobilized to facilitate the on-time delivery of goods [5]. Accordingly, a Supply Chain of Things could be monitored and used for decision making to help the goods arrive on time, not before and not after. Further, reports continue to surface that there are tainted agricultural goods in our food systems [6], an issue that would bene<sup>fi</sup>t from information a Supply Chain of Things could provide. A recent study by Derbyshire [7] noted that it took periods ranging from weeks to months to trace poisons in food back to their origins. A Supply Chain of Things could facilitate the identi<sup>fi</sup>cation of the origin and diffusion of such goods over time. Further, development of a Supply Chain of Things could improve issues such as “trust” in the supply chain, because an increased visibility of things can remove information asymmetries.

## 1.2. Need for shared semantics

In addition to visibility, supporting a collaborative decision making process requires data interoperability enabled by shared semantics. The latter is ampli<sup>fi</sup>ed in supply chains because multiple organizations are involved in the process of moving goods from one location to another. Often, those organizations can have different de<sup>fi</sup>nitions of the same events and supply chain objects. These organizations might only share select accounting information – not operational data such as locations – with other organizations. In addition, each organization will typically capture different data, in different formats, for its own respective system, so even if the data was shared, it would not necessarily be compatible. Accordingly, as discussed by Pathak et al. [8], there is a general lack of understanding regarding phenomena that occur in the supply chain, and thus, an additional analysis using alternative methodologies (e.g., development of supply chain ontology) is promulgated.

## 1.3. Ontology for a Supply Chain of Thing

Supporting collaborative decision making requires transparency, standardized structures, and semantics for the data generated. Such standardization can be accomplished through ontological speci<sup>fi</sup>cations; as a result, it is probably not surprising that a European Commission [9] suggested the importance of generating semantic models associated with the Internet of Things.

Accordingly, this paper generates a semantic model ontology for a supply chain that leverages the availability of individual object information, within the context of a sequence of standard economic events, to generate the capabilities of a HVSC, within a number of different data architectures. Ultimately, this ontology facilitates interoperability between systems across the supply chain, and enables decision makers to collaborate. Therefore, an important objective of this paper is to de<sup>fi</sup>ne these common standard economic phenomena, and their components, as part of an ontological speci<sup>fi</sup>cation. The chosen method is based on a set of ontological primitives (Event, Agent, Location, Equipment, and Thing), and gradually de<sup>fi</sup>nes structuring principles. The development of the resulting EAGLET ontology, and the corresponding templates that capture the movement of individually identi<sup>fi</sup>ed goods through the supply chain, provide support for decision making and communication.

The EAGLET ontology further addresses two speci<sup>fi</sup>c demands for supply chain data modeling. First, economic phenomena are modeled from an independent, or public, view as opposed to the point of view of its particular individual partners. Second, the speci<sup>fi</sup>cation is driven by visibility requirements, with individual object visibility being able to facilitate communication, drive down information asymmetries, and support individual and collaborative decision making.

## 1.4. Summary of problem identification and motivation

We have identi<sup>fi</sup>ed many of the real-world problems in supply chain environments that result from a lack of visibility and interoperability, and they can be summarized as follows: there is a lack of visibility of things and inconsistent semantic communications in the supply chain, resulting in information asymmetries and overall supply chain complexity that leads to goods not arriving when needed and an inability to trace trails of goods in real time.

## 1.5. This paper

This paper proceeds as follows. The Introduction discussed the notion of a Supply Chain of Things as deriving from the Internet of Things. IoI technologies were identi<sup>fi</sup>ed as enablers for HVSCs and the two key criteria for collaborative decision making in such an environment determined to be visibility and interoperability. The de<sup>fi</sup>nition of EAGLET – an ontological speci<sup>fi</sup>cation for HVSCs – was further discussed as the paper's main contribution. Section 2 summarizes previous research related to the intersection of supply chains, ontologies, and the Internet of Things, enabled by IoI technologies such as RFID. Section 3 examines in detail the design science research method used in this paper and provides a design science structure for the remainder of the paper. Section 4 de<sup>fi</sup>nes the speci<sup>fi</sup>c objective of the artifact being created: the EAGLET ontology. The speci<sup>fi</sup>cations of the EAGLET ontology, both its primitives and structuring rules, are then discussed in Section 5. The structuring rules comprise stereotypical patterns, meta-patterns, and scripts. Section 6 illustrates how the EAGLET ontology can be used to solve an actual problem; i.e., a data model for an actual supply chain is de<sup>fi</sup>ned as an instantiation of the EAGLET ontology. Section 7 evaluates the EAGLET ontology; the two main types of evaluation conducted and discussed are comprehensiveness analysis and strength analysis. Finally, Section 8 provides a brief summary of the paper, summarizes how the paper relates to design science guidelines, and provides potential areas for future research.

## 2. Previous research

The purpose of this section is to analyze the existing gap in the research related to the intersection of supply chains, ontologies, and the Internet of Things, enabled by IoI technologies such as RFID. Examining that gap, we de<sup>fi</sup>ne the three concepts individually and then review research that has emerged from the interaction of those three concepts.

A supply chain “encompasses all activities associated with the <sup>fl</sup>ow and transformation of goods from the raw materials stage (extraction), through to the end user, as well as the associated information <sup>fl</sup>ows” (Ballou [10], p. 5). Management of a supply chain requires an in-depth understanding of its physical <sup>fl</sup>ow, as well as coordination and collaboration among the supply chain partners.

The most commonly used de<sup>fi</sup>nition of an ontology is “an explicit speci<sup>fi</sup>cation of a conceptualization” (Gruber [11], p. 199). Chandrasekaran et al. [12] suggest that ontologies provide both a vocabulary and a body of knowledge describing a speci<sup>fi</sup>c domain. They note the importance of an ontology as a content theory that might be implemented using different mechanisms or forms of knowledge representations. Chandrasekaran et al. ([12], p. 22) also note that constructing ontologies is an “ongoing research enterprise.”

As noted by Ashton [13], the term Internet of Things, developed in 1999, initially was meant to describe the following type of situation:

“Today computers – and, therefore, the Internet – are almost wholly dependent on human beings for information. …The problem is, people have limited time, attention and accuracy—all of which means they are not very good at capturing data about things in the real world. …Computers need to be empowered with their own means

G.L. Geerts, D.E. O'Leary / Decision Support Systems xxx (2013) xxx–xxx

of gathering information, so they can see, hear and smell the world for themselves….”

However, increasingly, the Internet of Things is evolving toward an “Internet of Everything” [14], where more than just other computers and sensors, but also people, are linked together by the Internet.

Next, we provide an overview of research that has emerged as these three concepts are paired: (1) supply chain ontologies (supply chain + ontologies), (2) Supply Chain of Things (supply chain + Internet of Things), and (3) ontologies for the Internet of Things (ontologies + Internet of Things).

## 2.1. Supply chain ontologies

An ontology answers questions about critical supply chain matters, such as inventory. As things move through the supply chain, information regarding their origin, location, and movement can be requested. As a result, ontologies can facilitate a supply chain memory that provides content for critical supply chain decisions. Supply chain researchers have examined a number of issues associated with supply chain ontologies. Smirnov and Chandra [15] examined the use of ontologies to facilitate cooperative supply chains. Frey et al. [16] developed an ontology based on individual <sup>fi</sup>rm-based documents used in support of the supply chain. Although there is extensive research on supply chain ontologies, in a recent survey, Grubic and Fan [17] found a number of limitations in the supply chain ontologies they analyzed, including none accounted for traceability, as accommodated by RFID, and other IoI technologies, none of the ontologies were for the operational level, but were instead aimed at the strategic level and other issues. If the ontology does not provide for these, then there is no knowledge and no organizational memory of them.

## 2.2. Supply Chain of Things

Other research examines the use of RFID and the Internet of Things in the supply chain, but does not develop a supply chain ontology as promulgated in this paper. For example, Ringsberg [18] analyzed the potential use of RFID for food traceability in the supply chain. O'Leary [2] developed an architecture for autonomic systems in the supply chain, in an application that could be characterized as consistent with the Supply Chain of Things. Chui et al. [19], in a discussion of the Internet of Things, mentioned the supply chain as a potential application area. Yan and Huang [20] investigated notions of information asymmetry in the supply chain considering the Internet of Things. Fleisch [21] provided an economic perspective on the Internet of Things and the supply chain. Katsma et al. [22] develop a framework of the supply chain as maturing to the Internet of Things. However, none of the previously mentioned studies considered the notion of an ontology for the Supply Chain of Things.

## 2.3. Ontologies for the Internet of Things

Recent research has developed ontologies for IoI applications but does not apply that research to the supply chain, instead focusing on speci<sup>fi</sup>c IoI technology components. In a recent study, the Norwegian Oil and Gas Industry [23] examined deployment of RFID in their industry from a technological perspective, focusing on speci<sup>fi</sup>c components of RFID technology. In that study, they generated a one-page example illustration of an RFID ontology that consists primarily of RFID system component information such as reader, tag, and portal. Li et al. [24] also developed an ontology that focused on the speci<sup>fi</sup>c RFID components but did not include any supply chain speci<sup>fi</sup>c information. Other researchers developed an ontology for RFID use, but not within a supply chain environment. For example, Chen and Tu [25] developed an ontology based on the use of RFID in a single <sup>fi</sup>rm production environment.

In summary, there is substantial research regarding supply chain ontologies, the Supply Chain of Things, and ontology development in the context of the Internet of Things. However, at the same time, it is clear that there is limited research regarding ontology development for the Supply Chain of Things that aims to improve interoperability and visibility, and as a result, such research is the subject of this paper.

## 3. Research method

How can the large quantities of data generated by IoI technologies in the Supply Chain of Things be conceptually organized so they can be understood and used by all supply chain partners involved? Recently, numerous studies [26–28] have called for academic researchers to engage in design science research. As Holmstrom et al. ([28], p. 67) describe it, design science researchers build “an artifact to solve a problem.” In particular, design science is a research method that focuses on problem solving through the creation of artifacts that address an unsolved problem in a unique or innovative way or a solved problem in a more effective or ef<sup>fi</sup>cient way [26]. Accordingly, a design science research approach is employed in this paper to generate an ontological speci<sup>fi</sup>cation as an innovative and powerful artifact that will structure information regarding the <sup>fl</sup>ow of items across the supply chain. In doing so, speci<sup>fi</sup>c operations, activities, and capabilities – such as locating goods in a store's backroom or determining the location of tainted foods – can be actualized.

## 3.1. Ontological approach

An ontological approach is taken that a conceptual data organization supporting visibility and interoperability requires a common understanding of the phenomena that can affect an item in the supply chain. The ontological speci<sup>fi</sup>cation de<sup>fi</sup>nes standardized patterns for describing the behavior of IoI-enabled objects in a supply chain using a representational format that can facilitate a common understanding of those phenomena.

For the speci<sup>fi</sup>cation of the EAGLET ontology, an approach is followed similar to the line of research of enterprise ontologies, in particular the Resource–Event–Agent Enterprise Ontology (REA-EO) [29,30], which de-<sup>fi</sup>nes primitives and structuring rules for enterprise modeling, as opposed to supply chain modeling. For EAGLET, a number of primitives speci<sup>fi</sup>c to supply chains, such as location and equipment, structuring rules, and stereotypical patterns, are identi<sup>fi</sup>ed. They are aimed at modeling an item's physical <sup>fl</sup>ow through the supply chain, and de<sup>fi</sup>ning who owns the item and who has custody of it at any point in time.

## 3.2. Design science research methodology

Peffers et al. [27] argued that there is a need for a stereotypical template to produce and present design science research, similar to templates used to present natural science research. They suggest a template referred to as the Design Science Research Methodology (DSRM), which consists of a nominal sequence of six activities: (1) problem identi<sup>fi</sup>cation and motivation, (2) de<sup>fi</sup>nition of the objectives of a solution, (3) design and development, (4) demonstration, (5) evaluation, and (6) communication. The bene<sup>fi</sup>t resulting from the pattern is that it makes it easier to recognize, analyze, and evaluate the research contributions. Accordingly, the remainder of this paper is structured based on the DSRM, as summarized in Table 1. The <sup>fi</sup>rst and second columns in Table 1 summarize the activities and give a brief description of the six DSRM activities applied to the research presented in this paper. The third column in Table 1 presents the knowledge tools used in each of the six steps [31]. Knowledge tools represent the raw material through which design science research is accomplished, e.g., foundational theories, frameworks, and system instantiations.

Please cite this article as: G.L. Geerts, D.E. O'Leary, A supply chain of things: The EAGLET ontology for highly visible supply chains, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.007

Table 1  
DSRM process for the EAGLET ontology.

<table><tr><td>DSRM activities</td><td>Activity description</td><td>Knowledge base</td></tr><tr><td>Problem identification and motivation</td><td>There is a lack of visibility of things and inconsistent semantic communications in the supply chain, resulting in information asymmetries and overall supply chain complexity that leads to goods not arriving when needed and an inability to trace trails of goods in real time.</td><td>Literature review of studies that discuss issues with current supply chain systems, and of studies that explore the potential of a supply chain of things.</td></tr><tr><td>Define the objectives of a solution</td><td>A comprehensive understanding of the phenomena that can happen to a thing when it moves across the supply chain and their representation.</td><td>Understanding of the visibility and interoperability expectations inherent to the supply chain of things; literature review.</td></tr><tr><td>Design and development</td><td>Definition of the EAGLET ontology that identifies the concepts and structuring rules underlying supply chains and that can be used for the development of a wide variety of supply chain applications.</td><td>Economic and supply chain theory, supply chain practice, literature review of existing ontologies and reference models, data modeling, ontological engineering.</td></tr><tr><td>Demonstration</td><td>Definition of an EAGLET model for a retail supply chain.</td><td>Supply chain practice. Data modeling. Application of EAGLET&#x27;s primitives and structuring rules.</td></tr><tr><td>Evaluation</td><td>Evaluation of EAGLET&#x27;s comprehensiveness and strengths. Evaluation of EAGLET&#x27;s strengths starting from a gap analysis of existing supply chain ontologies.</td><td>Analysis and knowledge of case studies, reference models, regulatory guidelines, standards, and existing supply chain ontologies.</td></tr><tr><td>Communication</td><td>Presentation to a wide variety of audiences including accounting, information systems, and supply chain management audiences. Publication in Decision Support Systems.</td><td>Knowledge of the disciplinary culture.</td></tr></table>

In the Introduction, identi<sup>fi</sup>cation of the problem and motivation to resolve the problem were provided. Next, the objectives of the EAGLET ontology are de<sup>fi</sup>ned.

## 4. Objective of the EAGLET ontology

Two key aspects of the Internet of Things are interoperability [32] and visibility [33]. Accordingly, they are critical issues for the Supply Chain of Things. However, in the context of a supply chain, interoperability and visibility require a common understanding of what can happen to things as they move across the supply chain. Thus far, there have been at least three efforts focused on developing such an understanding: RFID data modeling, XML-based standards for supply chain management, and speci<sup>fi</sup>cation of legislative requirements.

## 4.1. RFID data modeling

A series of research studies have focused on RFID data modeling [34,35], with much emphasis on speci<sup>fi</sup>c applications, such as libraries [36]. RFID readers generate a vast amount of raw data that have an object, location, and time format. Unfortunately, the data generated by RFID applications can contain inconsistencies. As a result, further applications are required to make sense of the data, <sup>fi</sup>lter irrelevant data, clean duplicate data, and analyze erroneous data. From a business and supply chain perspective, the key concerns are identifying things (items), knowing when a thing enters the warehouse, the location of the thing in the warehouse, and when a thing exits the warehouse. However, inferring business event-related data, and mapping RFID data into complex events, is a complicated matter [37–39].

## 4.2. XML-based standards for supply chain management

A number of XML-based standards have been developed to communicate information related to supply chain phenomena. The de<sup>fi</sup>nition of such standards requires the explicit de<sup>fi</sup>nition of the phenomena to be described. Two examples of such standards are Physical Markup Language (PML) and TraceCore. PML [40] describes the containment structures, location, and measurement of physical objects. TraceCore [41] is a standard for exchanging information about traceability using XML and is a successor to TraceFish. TraceCore was intended to develop the minimum elements necessary for traceability, thus the name “Core.”

## 4.3. Legislative requirements

Recent legislation describes what phenomena should be captured by traceability systems in a number of different industries, including automotive, food, and pharmaceutical; examples include the handbook for introduction of food traceability systems [42] and the standards document created for the grocery industry [43].

## 4.4. Summary and objective

The studies previously discussed provide an initial understanding of what happens in the supply chain. However, for the Supply Chain of Things, a more comprehensive understanding is required, as well as a more explicit representation of such phenomena. Such speci<sup>fi</sup>cation should not only include the basic phenomena but also a speci<sup>fi</sup>cation of how such phenomena relate to each other. Therefore, the following is the overall objective for the artifact: A comprehensive understanding of the phenomena that can happen to a thing when it moves across the supply chain and their representation.

## 5. Design and development

Different approaches have been suggested for the development of ontologies [44]. In this paper, we have adopted the approach followed for the de<sup>fi</sup>nition of the REA-EO [29,30]. EAGLET provides an innovative and purposeful artifact that has two main characteristics. First, it de<sup>fi</sup>nes the common phenomena underlying the Supply Chain of Things and it can therefore be used for any kind of architecture (e.g., centralized vs. decentralized), at any level of granularity (e.g., HVSCs), and for any type of application (e.g., decision support system). The use of EAGLET as a common denominator across applications increases interoperability. Second, EAGLET de<sup>fi</sup>nes a body of knowledge consisting of primitives and structuring rules. The structuring rules differentiate EAGLET from similar studies and preserve the integrity of the supply chain applications being built.

## 5.1. Design issues

Speci<sup>fi</sup>cation of EAGLET required addressing (1) whether to use a dependent or an independent view, and (2) whether or not to specify object properties as part of the ontology.

## 5.1.1. Dependent vs. independent view

Two different schools of thought have emerged in regard to the definition and modeling of supply chain phenomena: (1) the dependent,

G.L. Geerts, D.E. O'Leary / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/XUJ9ZHXG/fulltext/images/2048c9c35e409b8b33b3c86569d66764ce89a3ba25bcce0bc60dedfd436efec3.jpg)  
Fig. 1. Object primitives.

trading partner, proprietary, private, or enterprise view; and (2) the independent, supply chain, or public view [45–48]. In the dependent view, each supply chain partner records information about phenomena from their own perspective, possibly creating redundant information. In the independent view, different phenomena are recorded once from a supply chain view. For example, an “unloading” operation for one company (e.g., the transportation company) is a “loading” operation for another company (e.g., the company receiving the goods). However, from a supply chain perspective, there is only one “handling” event that needs to be monitored. The dependent view is more appropriate for decentralized systems, whereas the independent view is more appropriate for centralized systems. EAGLET adheres to the independent view in that it focuses on a neutral de<sup>fi</sup>nition of the phenomena underlying the supply chain.

## 5.1.2. Properties

There are some limited speci<sup>fi</sup>cations of properties in EAGLET. First, we consider time as an intrinsic property of an event, determining when it occurs. Second, the differentiation of ontological concepts into subtypes is in essence based on properties, e.g., start and end time properties need to be speci<sup>fi</sup>ed for all duration events. Further, the interorganizational nature of supply chains creates interoperability issues with regard to properties, e.g., the term “measure” can have different meanings for two partners in the supply chain [49], but we do not address such issues in this paper.

## 5.2. Object primitives

The EAGLET ontology has <sup>fi</sup>ve object primitives: Event, Agent, Location, Equipment, and Thing. In the Supply Chain of Things, each of these object primitives could be described as things, because they all have a presence of their own. However, we have found that the basic nature of those <sup>fi</sup>ve primitives is different. In particular, an event describes what happens to a thing, agents are those who move and handle things, locations are where things are, equipment is used to move and process things, and things move through the supply chain.

## 5.2.1. Thing

Fig. 1(A)<sup>1</sup> de<sup>fi</sup>nes thing as the <sup>fi</sup>rst object primitive in the EAGLET ontology. A thing represents any item of which the physical <sup>fl</sup>ow, custody, and ownership is being traced throughout the supply chain. As mentioned in GS1 [43], a thing can take a variety of forms including trade item, lot, and box. The level at which a thing is de<sup>fi</sup>ned – i.e., its granularity – de<sup>fi</sup>nes its operational visibility and a thing can be de<sup>fi</sup>ned at any level of granularity. In Fig. 1(A), we follow Senneset et al. [50] and GS1 [43] in distinguishing between trade units and logistic units, using two subtypes. GS1 ([43], pp. 59, 61) de<sup>fi</sup>nes a trade unit as “any item (product or service) upon which there is a need to retrieve pre-de<sup>fi</sup>ned information and that may be priced, or ordered, or invoiced at any point in any supply chain” and a logistic unit as “an item of any composition established for transport and/or storage that needs to be managed through the supply chain.” A number of studies, including Senneset et al. [50], explicitly model structural relationships between trade and logistic units. A distinctive characteristic of the EAGLET ontology is that structural relationships between things are not explicitly modeled. Instead, the formation and destruction of such relationships is captured through the event primitive.

## 5.2.2. Event

Fig. 1(B) portrays the EAGLET de<sup>fi</sup>nition of the event object primitive. Events are occurrences in time that change a thing, such as its location (movement) or its intrinsic characteristics (production). Time is viewed as an intrinsic property of an event that determines when it occurs. We differentiate between economic events that occur instantaneously (instant) and economic events that occur over a period of time and thus possess duration (interval). For example, whereas a transfer might occur instantaneously (e.g., when an item leaves the shipping

G.L. Geerts, D.E. O'Leary / Decision Support Systems xxx (2013) xxx–xxx

area), a transportation event typically has duration. Fig. 1(B) graphically de<sup>fi</sup>nes instantaneous and duration events as subtypes of the event object primitive. For simplicity purposes, ontological speci<sup>fi</sup>cations for time are not integrated as part of the EAGLET ontology. See Hobbs and Pan [51] for a time ontology speci<sup>fi</sup>cation.

## 5.2.3. Agent

Fig. 1(C) portrays the de<sup>fi</sup>nition of agent in the EAGLET ontology. A supply chain represents collaborations between supply chain partners and they represent a <sup>fi</sup>rst group of agents to be described as part of a supply chain management system. Common examples of supply chain partners, and therefore EAGLET agents, are manufacturer, distributor, retailer, carrier, and customer. Second, agent information speci<sup>fi</sup>c to a supply chain partner must often be shared with other partners, e.g., for authorization to receive goods. The recursive “relates\_to” association in Fig. 1(C) captures such information.

## 5.2.4. Location

Fig. 1(D) de<sup>fi</sup>nes location as an object primitive. Schuster et al. ([52], p. 40) state that “an important characteristic of future supply chains will be the ability to locate objects that might be stationary or in transit, potentially anywhere within or beyond the boundaries of a company.” Brock et al. [40], p. 17] further note, “although location is a seemingly simple concept it is somewhat dif<sup>fi</sup>cult to represent accurately.” There are numerous issues to be taken into consideration when de<sup>fi</sup>ning location. First, it is common to distinguish geographic and symbolic locations. A geographic location (similar to the Global Positioning System) is typically de<sup>fi</sup>ned in terms of latitude, longitude, and altitude. The use of standardized measurements increases interoperability. As suggested by Liu et al. [53], symbolic locations are de<sup>fi</sup>ned by an ID, a name, and an owner such as 1 (ID) being a warehouse (name) at the manufacturer (owner). Fig. 1(D) graphically differentiates between geographic and symbolic locations using subtype de<sup>fi</sup>nitions. Second, EPCGlobal [54] differentiates between “read points” and “business locations.” A read point speci<sup>fi</sup>es the speci<sup>fi</sup>c place where an observation (e.g., by an RFID reader) took place. A business location represents the location where an object is assumed to be until it is observed again. For example, an item is assumed to be in the warehouse (business location) after it has been observed at one of its doorways (read point); or, stated differently, business locations are inferred from read points. The EAGLET ontology location primitive refers to business locations. Third, it is common to consider containment relationships between locations [53]. For example, a bin (location) can be considered part of a warehouse (location). The recursive layout association in Fig. 1(D) enables the de<sup>fi</sup>nition of layout structures; e.g., how is a warehouse organized. Layout information often needs to be shared with supply chain partners, e.g., entry door of warehouse for delivery.

## 5.2.5. Equipment

Fig. 1(E) de<sup>fi</sup>nes equipment as an object primitive. Instances of equipment represent the means that move and process things as part of the supply chain, e.g., a forklift or a truck. Equipment is not traced throughout the supply chain or delivered to the consumer.

## 5.3. Association primitives

Association primitives de<sup>fi</sup>ne permissible interactions through relationships between object primitives and are therefore structuring rules. Event is the basic unit of analysis in the EAGLET ontology and, as is illustrated in Fig. 2, links different primitives together in four key associations: Event–Agent, Event–Thing, Event–Location, and Event–Equipment.

## 5.3.1. Event–Agent

An Event–Agent association de<sup>fi</sup>nes who is involved in an event and in what capacity. As shown in Fig. 2(A), we differentiate between three different roles: from, to, and participates. The “from” and “to” roles are used to de<sup>fi</sup>ne who is involved in an exchange of ownership or an exchange of custody. The from role indicates that an event results in an agent giving up ownership or custody and indicates that an event results in an agent receiving ownership or custody. For example, a distributor selling an item to a retail store results in an exchange of ownership from the former to the latter. Custody and ownership are two distinct concepts. Ownership de<sup>fi</sup>nes who has economic control over a thing [55]. Custody determines who has authorized possession and custody information is useful for tracing in case of recalls. Industries, such as <sup>fi</sup>shing, now mandate recording of chain of custody information. The bottom section of Fig. 2(A) shows the “participates” association, a

![](/api/attachments/XUJ9ZHXG/fulltext/images/6a86296ce0f82bfdecaeb22df3bca71ef2911d555815efbff2e0ae2248a45598.jpg)  
Fig. 2. Association primitives

Please cite this article as: G.L. Geerts, D.E. O'Leary, A supply chain of things: The EAGLET ontology for highly visible supply chains, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.007

catchall term that refers to all other roles an agent can play in regard to an event.

## 5.3.2. Event–Thing

Event and thing are generally considered as the two core elements of supply chain systems [56]. The Event–Thing associations de<sup>fi</sup>ne what happens to an item when it moves through the supply chain. We differentiate between the following types of Event–Thing associations: custody, ownership, takes, forms, breaks, into, applies-to, enters, exits, and disrupts.

The upper section of Fig. 2(B) shows the “custody” and “ownership” Event–Thing associations, whereas the middle section deals with recon<sup>fi</sup>gurations: the formation and destruction of part–whole or containment associations. Most studies [53] de<sup>fi</sup>ne containment as an association between things. However, as shown in the middle section of Fig. 2(B), EAGLET uses events to de<sup>fi</sup>ne the formation and destruction of containment structures, allowing identi<sup>fi</sup>cation of the recon<sup>fi</sup>gurations for who, where, and when. Recon<sup>fi</sup>guration can take many forms. The “takes” and “forms” roles are used to describe the creation of a containment structure – e.g., an event takes an item (part) and puts it into (forms) a case (whole) – or a conversion process—e.g. raw materials (parts) are used to (takes) produce (forms) a product (whole). The “breaks” and “into” roles are used to describe the destruction of a containment structure; e.g., a recon<sup>fi</sup>guration event breaks a pallet (whole) into its cases (parts). Recon<sup>fi</sup>guration associations always occur in pairs and link inputs with outputs through events.

The bottom section of Fig. 2(B) shows four additional Event–Thing associations: applies-to, enters, exits, and disrupts. They differ from the recon<sup>fi</sup>guration associations in that they are not paired up and there is no input–output relationship. The “applies-to” association is meant to be used in a variety of scenarios, including processing (such as the cooling of items), handling, and moving of things. An “enters” association de<sup>fi</sup>nes entry of an item into the supply chain, such as a <sup>fi</sup>sh being caught. Similarly, an “exits” association de<sup>fi</sup>nes an item's exit from the supply chain such as an item passing the Point-of-Sale (POS) terminal as a sale. Finally, “disrupts” represents the situation where an event disrupts an item's <sup>fl</sup>ow.

## 5.3.3. Event–Location

The Event–Location association is used to describe how a thing's position changes or where an event occurs. Fig. 2(C) differentiates between three Event–Location associations: origin, destination, and at. The “origin” and “destination” associations are used to represent a change in position and de<sup>fi</sup>ne from where (origin) to where (destination) a thing is moved. For example, a pallet has been moved (event) from the receiving area (origin) to the picking station (destination). The “at” association de<sup>fi</sup>nes where an event occurs, such as where a thing is lost or where a service such as packaging occurs. “At” associations can also be used to de<sup>fi</sup>ne the location history for a duration event. For example, carriers such as UPS observe where a resource is at different points in time. Event–Location associations enable the tracking (where it is) and tracing (where it has been) of things and therefore are a key ingredient to generating a value chain's visibility.

## 5.3.4. Event–Equipment

Fig. 2(D) differentiates between three different Event–Equipment associations: from, to, and uses. The “from” and “to” associations are used to connect and disconnect things with production and transportation equipment; e.g., an item is loaded on a truck (to). The “uses” association is used to describe how equipment is employed by an event. For example, a cooker is used to cook.

## 5.4. Stereotypical patterns

In this next layer of structuring, the EAGLET object and association primitives are aggregated into nine stereotypical patterns: recon<sup>fi</sup>guration, relocation, handling, processing, entry, exit, disruption, exchange of custody, and exchange of ownership. The <sup>fi</sup>rst seven patterns provide a grammar for de<sup>fi</sup>ning the physical <sup>fl</sup>ow of things through the supply chain; i.e., the movement of things through speci<sup>fi</sup>ed states of production, processing, storage, and distribution. The last two patterns provide a grammar for the de<sup>fi</sup>nition of two alternative perspectives: the chain of custody and the chain of ownership.

## 5.4.1. The reconfiguration pattern

The recon<sup>fi</sup>guration pattern in Fig. 3-1(A) uses events to de<sup>fi</sup>ne input–output relationships between things and how, when, where, and by whom it was done. Recon<sup>fi</sup>guration occurs in many different forms, including conversion and assembly. Conversion alters the physical properties of the input when creating the new output, e.g., when producing sausages from meat and other ingredients, and assembly puts a number of items together. As shown in Fig. 3-1(A), the recon<sup>fi</sup>guration pattern describes who participates (agent), where it occurs (location), and how it is done (equipment). For manual operations, equipment obviously does not have to be speci<sup>fi</sup>ed. As previously discussed, the takes and forms associations are used to de<sup>fi</sup>ne formation processes, whereas the breaks and into associations are used to de<sup>fi</sup>ne splitting (destruction) processes. For input–output recon<sup>fi</sup>guration patterns, takes and forms are joint roles, i.e., if an event participates in one association, it also participates in the other, and the same is true for the breaks and into associations. On the other hand, takes/forms and breaks/into are exclusive pairs of roles—either a new item is formed or an existing item is split.

## 5.4.2. The relocation pattern

Fig. 3-1(B) de<sup>fi</sup>nes the relocation pattern. Fisher [57] de<sup>fi</sup>nes relocation or transportation as a change in an item's position. An item's relocation does not change its intrinsic characteristics. The pattern in Fig. 3-1(B) integrates the following information regarding relocation events: the things being relocated, the event's duration, origin (from), and destination (to) of the relocation event, a thing's current position, and who executes the relocation event. The “applies\_to” association describes the things that are being relocated, whereas the “origin” and “destination” associations de<sup>fi</sup>ne from where and to where a thing is relocated. Origin and destination are joint roles and one cannot exist without the other. The “at” association, on the other hand, is used to determine an item's current position. The “participates” association describes who relocates a thing. Relocation events are typically duration events.

## 5.4.3. The handling pattern

Handling deals with the transition between movement, recon<sup>fi</sup>guration, and storage. Fig. 3-1(C) de<sup>fi</sup>nes the handling pattern and integrates information about the thing being handled, when the handling occurs (event), the location where the handling occurs, the agent who executes the handling, the equipment from/to which the thing is moved, and the equipment used for the handling process. The following are three common scenarios supported by the handling pattern. First, things are loaded to transportation equipment in preparation for movement, e.g., pallets (things) are loaded on a lift truck (equipment) by the manufacturer (agent) at the shipping area (location). Second, things can be loaded to equipment for recon<sup>fi</sup>guration or processing purposes, e.g., shrimp are loaded to a cooker. Third, things can be placed in storage, e.g., products are stored in a warehouse bin.

## 5.4.4. The processing pattern

Fig. 3-1(D) de<sup>fi</sup>nes the processing pattern. The pattern describes how the process (event) changes a thing's characteristics, who participates in it, where it takes place, and which equipment is used. The process pattern can be considered a variation of the recon<sup>fi</sup>guration pattern with the main difference being that there is no input–output relationship between the things; the process adds value to the thing.

G.L. Geerts, D.E. O'Leary / Decision Support Systems xxx (2013) xxx–xxx

## 5.4.5. The entry and exit patterns

Fig. 3-2(E) and -2(F) de<sup>fi</sup>ne the entry and exit patterns, respectively, and they are used to describe when a thing enters and when it leaves the supply chain. For both patterns, it is described when and where a thing enters/exits the supply chain, who is involved, and what equipment is being used during the entry/exit process. Again, both patterns can be considered a variation of the recon<sup>fi</sup>guration pattern, with the main difference being that there is no input–output relationship between the things.

## 5.4.6. The disruption pattern

The disruption pattern in Fig. 3-2(G) de<sup>fi</sup>nes a disruption of a thing's <sup>fl</sup>ow through the supply chain and integrates the following information: the thing of which the <sup>fl</sup>ow was disrupted, when the disruption took place, where the disruption was observed, and who observed it. Events that cause disruptions are instantaneous: items (pallets, cases, or individual items) have perished or have not perished; items have been stolen or have not been stolen. The “at” location describes where the disruption of the <sup>fl</sup>ow was observed; e.g., the location an item was last seen before it was stolen or the location where the perished goods were found. The participation association describes by whom the disruption was observed.

## 5.4.7. Exchange of custody pattern

Visibility requires that it is known who has custody of a thing at any given time. Some industries, e.g., the <sup>fi</sup>sh industry, have mandated the

![](/api/attachments/XUJ9ZHXG/fulltext/images/152de125268975eb5b7997040a2d32d5e6cbe5e590f543612d79bae7a8c1eb65.jpg)  
Fig. 3. 1. Stereotypical patterns: Recon<sup>fi</sup>guration, relocation, handling, and processing. 2. Stereotypical patterns: Entry, exit, and disruption. 3. Stereotypical patterns: Exchange of custod and exchange of ownership.

Please cite this article as: G.L. Geerts, D.E. O'Leary, A supply chain of things: The EAGLET ontology for highly visible supply chains, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.007

G.L. Geerts, D.E. O'Leary / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/XUJ9ZHXG/fulltext/images/1d9df64ffe571e1854a7c47990ea4099a63ffedb45fec3a243d6d306ecfe0c90.jpg)  
Fig. 3 (continued).

recording of a chain of custody. Fig. 3-3(H) de<sup>fi</sup>nes the exchange of custody pattern and integrates the following information: the thing being exchanged, when the exchange occurs, who gives up custody (from), who receives custody (to), and where the exchange takes place (at). The custody association de<sup>fi</sup>nes the things that are the subject of the exchange. Exchange of custody is instantaneous. From and to are joint roles and indicate the agents involved in the exchange, as well as its direction.

## 5.4.8. Exchange of ownership pattern

Fig. 3-3(I) de<sup>fi</sup>nes the exchange of ownership pattern. Its structure is similar to the exchange of custody pattern; the only difference is that the custody association is replaced by the ownership association. Ownership and custody issues are of utmost importance for supply chains, especially in case of practices such as Vendor Managed Inventory (VMI), where the vendor takes control of managing inventory for their customers.

## 5.5. Pattern integration

As mentioned previously, the nine stereotypical patterns de<sup>fi</sup>ne three different perspectives: (1) the physical <sup>fl</sup>ow: patterns A–G, (2) the chain of custody: pattern H, and (3) the chain of ownership: pattern I. Often, the different perspectives will overlap, which requires integration of the patterns. Two examples of such integration are discussed next.

## 5.5.1. Custody/ownership congruency

The distinction between custody and ownership determines who holds an item (possession) and who owns it (legal title). Custody and ownership often differ for in-transit goods. While the carrier will have custody of the goods, ownership is determined by the terms of the shipping agreement. Common practices are (1) freight on board (f.o.b) shipping point, ownership is transferred at the shipping point; and (2) f.o.b. destination, ownership is not transferred until the items arrive at their destination. The EAGLET ontology traces custody and ownership separately. However, in some cases the two overlap. For example, in a transfer with no carriers involved, both custody and ownership are exchanged when an item is delivered to the buyer, merging the custody and ownership associations (Fig. 3-3H and I).

## 5.5.2. Handling/custody/ownership congruency

Handling refers to the transition between movement, recon<sup>fi</sup>guration, and storage and often takes the form of loading and unloading. In some cases, a handling event does not imply an exchange of custody or ownership, e.g., loading items onto a lift truck for transfer to another shelf. However, in other cases, handling events imply an exchange of custody and/or an exchange of ownership. The handling (physical <sup>fl</sup>ow), exchange of custody, and exchange of ownership events then occur together and Fig. 4 shows how the three different patterns, 3-1 C, 3-3 H, and 3-3 I, are integrated into one. Consider when items are loaded on a truck (f.o.b. shipping point) and delivered by a carrier. Using the semantics of the integrated pattern shown in the northwest corner of Fig. 4, the situation can be described as follows. An item (thing) is loaded (event) by the manufacturer (agent) at the shipping area (location) from the lift truck to the truck (equipment), custody is exchanged from the manufacturer (agent) to the carrier (agent), and ownership is exchanged from the manufacturer (agent) to the distributor (agent). Some information, e.g., location, is congruent across all three views and therefore is presented only once in the integrated pattern.

## 5.6. Meta-patterns

Structuring does not necessarily end with the nine stereotypical patterns previously identi<sup>fi</sup>ed. Fig. 5 shows a meta-pattern consisting of a sequence of a load, a relocation, and an unload event. Metapatterns provide vehicles to integrate patterns, to address speci<sup>fi</sup>c modeling issues, and to express dependencies. The example in Fig. 5 integrates the location, equipment, and agent primitives from the load, relocation, and unloads patterns, and the following three dependencies can be de<sup>fi</sup>ned for it. First, there is an implicit temporal order between the three events: load b relocation b unload. Second, the “to” equipment instance of the <sup>fi</sup>rst handling event (load) is the same as the

G.L. Geerts, D.E. O'Leary / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/XUJ9ZHXG/fulltext/images/c89ca41b6ec706f5df072bdad83f9abe8656d4dd8f8b8e0c84eba222d9df548a.jpg)  
Fig. 4. Pattern integration.

“from” equipment instance of the second handling event (unload); e.g., items that are loaded on a truck need to be unloaded from the same truck after transportation (relocation). Third, dependencies exist between the location speci<sup>fi</sup>cations: the location at which the item is loaded is the origin of the relocation event and the location at which the item is unloaded is the destination of the relocation event. The meta-pattern example in Fig. 5 focuses on the physical <sup>fl</sup>ow. Intermodal transportation, e.g., truck/boat/truck, can be modeled as a sequence of instantiations of this meta-pattern.

## 5.7. Script definitions

The <sup>fi</sup>nal, and most advanced level of structuring, is the de<sup>fi</sup>nition of the economic script underlying the supply chain. Two types of

![](/api/attachments/XUJ9ZHXG/fulltext/images/d1a4ee0b41373353fcebdfc92e59e4072a5a80b3848cdb42fe5c4663cb6ce90d.jpg)  
Fig. 5. Meta-pattern.

Please cite this article as: G.L. Geerts, D.E. O'Leary, A supply chain of things: The EAGLET ontology for highly visible supply chains, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.007

structural relationships exist between the events that guide the definition of a supply chain's economic script: (1) reciprocity, and (2) temporal ordering.

## 5.7.1. Reciprocity

Merriam-Webster de<sup>fi</sup>nes reciprocity as “a relation of mutual dependence.” For the EAGLET ontology, we distinguish between three different types of reciprocity. First, we adopt the duality principle from the REA-EO (McCarthy [29], p. 562) that links “each increment in the resource set of the enterprise with a corresponding decrement (Ijiri, [55, Ch. 5]).” The duality principle is an integral part of the EAGLET ontology because it (1) determines the resources needed to execute the supply chain, and (2) de<sup>fi</sup>nes the give/take nature of transfer associations between the supply chain partners. Second, for most logistic units, a reciprocal relationship exists between formation and splitting (destruction) events. In a retail supply chain, trading units are packed for logistical purposes (formation), but the logistic units need to be broken again (splitting) before they can be sold to the customer. For example, items such as cans are packed into cases and cases are put on pallets; however, cans are sold to customers. The inverse relationship between formation and splitting events helps structure supply chain data models. However, as opposed to the duality principle, there is no explicit association between such events. Third, a similar reciprocal relationship exists between “load” and “unload” handling events. A load handling event for speci<sup>fi</sup>c equipment must be matched by an unload handling event for the same equipment.

## 5.7.2. Temporal ordering

Events are subject to temporal ordering, which determines the different paths through which a thing can <sup>fl</sup>ow. Different mechanisms are available to de<sup>fi</sup>ne temporal ordering, including rules and explicit semantic relationships. First, temporal ordering can be expressed as a set of rules. For example, a thing (e.g., a speci<sup>fi</sup>c pallet) can only be transported after it has been loaded (thing.handling.endtime b = thing.relocation. starttime). Second, temporal ordering can be hardwired as explicit semantic relationships as part of a supply chain data model, as illustrated by the diagram in Fig. 6. The “follows” association and its “start” and “end” roles help to de<sup>fi</sup>ne permissible sequences of events and thus, the supply chain's economic script (gray areas in Fig. 6). For example, loading from the receiving area can be followed by (1) moving to the picking area, (2) moving to the shipping area (cross docking), or (3) loss of the item.

Some temporal ordering is implied by the EAGLET ontology primitives, as illustrated by the four rules discussed below. An operational rule is part of the actual supply chain system. A design rule provides guidance during the de<sup>fi</sup>nition of an EAGLET model; an instance of the EAGLET ontology. First, the existence of a location entity makes sense only if it participates in at least one “destination” association and in at least one “origin” association (design). Things <sup>fl</sup>ow through the supply chain and do not stay in the same location, e.g., in retail stores, there should be at least one event that puts items on shelves, and there should be at least one event that takes items from shelves. Second, an origin event for a location is always preceded by a destination event for the same location (operational). Third, “entry” events cannot be the “end” event in a “follows” association (design). Fourth, “exit” or “disruption” events cannot be the “start” event in a “follows” association (design).

## 6. Demonstration

Peffers et al. ([27], p. 13) describe the DSRM demonstration activity as follows: “demonstrate the use of the artifact to solve one or more instances of the problem.” In addition, we note that demonstration also provides evidence of evaluation (the next step) because demonstration illustrates how the artifact actually works in some initial context.

In this section, an EAGLET model for a retail supply chain is de<sup>fi</sup>ned. Supply chains come in a variety of forms, with each being subject to their own speci<sup>fi</sup>c practices. For demonstration purposes, we focus on the manufacturer-to-retail portion of the supply chain and thus, outbound logistics. Fig. 7 presents one speci<sup>fi</sup>c instantiation of the retail supply chain with special attention given to the visibility of its physical <sup>fl</sup>ow as enabled by IoI technologies, such as RFID. The corresponding EAGLET model is shown in Fig. 8.

## 6.1. Supply chain practices

The supply chain representation in Fig. 7 starts with the manufacturer producing items that can be uniquely identi<sup>fi</sup>ed. The manufacturer

![](/api/attachments/XUJ9ZHXG/fulltext/images/525635c676c8f8bc957923c6d0955a6e0e5fdea56a86becb3b825fb831a0427a.jpg)  
Fig. 6. Script de<sup>fi</sup>nition.

Please cite this article as: G.L. Geerts, D.E. O'Leary, A supply chain of things: The EAGLET ontology for highly visible supply chains, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.007

G.L. Geerts, D.E. O'Leary / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/XUJ9ZHXG/fulltext/images/3f540b6b286c96e08123dbf18fda1e1d675adee7ec078277d8cbc29de733b74d.jpg)  
Fig. 7. Retail supply chain.

tags the individual items, packs them into cases, and puts them on pallets. Cases and pallets represent logistic units that have their own unique identi<sup>fi</sup>er and tags. The pallets are then moved by a lift truck, which may be tagged, from the production <sup>fl</sup>oor to the shipping area where they are picked up by a carrier. The transportation from manufacturer to distributor is outsourced to carriers. Carriers use trucks for transportation purposes. Carriers unload items at the distributor's receiving docks. While carriers are supply chain agents themselves, they are not modeled as such in Fig. 7 to keep the graphical representation simple. The distributor's main function is that of rearrangement [58]. The pallets delivered by the carrier are <sup>fi</sup>rst put into storage areas at the picking station. Following, the pallets are broken and mixed. Finally, the remixed pallets are moved to the shipping area from where they are transported to the retailer. A carrier transports the remixed pallets to the retailer. As shown at the bottom of Fig. 7, the retailer <sup>fi</sup>rst puts the pallets received into the backroom. Following, the pallets and cases are broken and the items are put on shelves. Finally, customers take the items from the shelves and pay for them. An item exits the supply chain when it is checked out at a POS terminal.

## 6.2. EAGLET model

The EAGLET model in Fig. 8 de<sup>fi</sup>nes the phenomena underlying the supply chain practices shown in Fig. 7 and discussed previously. The UML stereotype symbol – bb NN – is used to indicate the EAGLET primitive of which the object or association is an instantiation. Further, several of the object classes – e.g., production <sup>fl</sup>oor and supply chain agent – are repeated multiple times. While this is not common practice, it improves the model's clarity. Further, numbers and accolades – {} – , a symbol which is not part of the UML syntax, are used to identify the different patterns used in Fig. 8. The same numbers are also used for cross-referencing between Figs. 7 and 8, focusing on the representation of the physical <sup>fl</sup>ow.

The model in Fig. 8 employs the following EAGLET patterns: recon-<sup>fi</sup>guration {1,2,12,13,23,24}, handling {3,5,6,8,9,11,14,16,17,19,20,22, 25,27}, relocation {4,7,10,15,18,21,26}, and exit {28}. The model further integrates multiple instantiations of the meta-pattern shown in Fig. 5. Most of the EAGLET model in Fig. 8 is self-explanatory, thus we focus on more speci<sup>fi</sup>c issues. First, EAGLET models represent supply chain phenomena from the independent view. For example, consider the item's exit at the retailer, while for the retailer a sale occurs at that point, from the independent view, the item is checked out when it passes the POS terminal. One of the results of adhering to the independent view is that intra-organizational phenomena {e.g., {3,4,5}) and inter-organizational phenomena (e.g., {6,7,8}) are represented in a uniform way. Second, for simplicity purposes, “supply chain agent” is used as instance for the agent EAGLET primitive throughout the whole model. We assume that manufacturer, carrier, distributor, etc. are its only instances. The use of speci<sup>fi</sup>c roles would add more preciseness to the model. Third, for many practices, compromised patterns suf<sup>fi</sup>ce. For example, no use of equipment needs to be speci<sup>fi</sup>ed if items are manually put in cases.

## 6.3. EAGLET structuring rules

The EAGLET model in Fig. 8 is compliant with the structuring rules discussed in the previous section. For example, reciprocal relationships exist between the loading and unloading events, and the exit event is not followed by any other event. In addition, for simplicity purposes, no script was hardwired as part of the model in Fig. 8. However, it would be easy to connect the “pack” event {1} with the “put-on” event {2}, the “put-on” event {2} with the “load” event {3}, etc. with “follows” associations.

## 7. Evaluation

In design science research, the goal of the evaluation phase is to “observe and measure how well the artifact supports a solution to the problem.” (Peffers et al. [27], p. 56]). As pointed out by Vaishnavi and Keuchler [59] and Geerts [31], design and evaluation of an artifact typically require different skill sets and are therefore often conducted in separate research studies. Such separation is illustrated by numerous seminal artifacts in the information systems discipline, including the relational database model [60] and the entity-relationship model [61]. Although the initial presentation of those research models provided some evaluation of the artifacts, the primary evaluation was completed as other researchers analyzed the artifacts and as the artifacts were put into other settings. Accordingly, a complete design and evaluation are rarely completed in the same paper.

In the remainder of this section, two different evaluations that were conducted with regard to the EAGLET ontology are discussed. First, the comprehensiveness analysis, an observation and measurement of EAGLET's objective as stated in Section 4: “A comprehensive understanding of the phenomena that can happen to a thing when it moves across the supply chain and their representation,” is discussed. Second, the strength analysis, an evaluation of EAGLET's overall strengths, starting from a gap analysis of existing supply chain ontologies [17], is discussed. The following discussion can be considered as an application of what Hevner et al. [26] referred to as the “informed argument” method.

## 7.1. Comprehensiveness analysis

The EAGLET ontology presented in Section 5 of this paper results from a development process that mirrors the <sup>fi</sup>rst two phases presented in Holmstrom et al. [28]. The <sup>fi</sup>rst phase, incubation, frames the problem and develops the rudiments of a potential solution design. The second phase, re<sup>fi</sup>nement, combines design improvements, implementation, and evaluation.

The overall objective of the EAGLET ontology is to determine the common phenomena underlying the Supply Chain of Things. During the incubation phase, EAGLET's design was primarily theory driven. The following are the main sources for the de<sup>fi</sup>nition of EAGLET's primitives and structuring rules during this phase: economic theory [55,57,62]; supply chain theory [10,63]; basic descriptions of supply chain operations, such as the core activities taking place in a warehouse [10]; the work on HVSCs in the context of emerging technologies, such as RFID [40,64]; and the primitives and structuring principles underlying the REA-EO [29,30].

During the re<sup>fi</sup>nement phase, the focus was on evaluating the comprehensiveness of these theory-driven speci<sup>fi</sup>cations; in particular, the extent to which EAGLET is capable of describing the different aspects of the physical <sup>fl</sup>ow of an item through a supply chain. This was done by evaluating EAGLET against case studies [65–68], reference models for traceability systems [47,56,69], regulatory guidelines [42], and standards and best practices [43]. Next, we provide a more indepth discussion of how we used the analysis of two real-world case studies for evaluating EAGLET's comprehensiveness.

As part of our evaluation process, we applied EAGLET to two realworld case studies documenting Metro Group's integrated use of RFID as part of their supply chain activities. Metro Group is Germany's largest retailer and began testing RFID technology as part of its Future Store Initiative in 2003 [67]. The <sup>fi</sup>rst case study (Metro Group videos [70]) –

![](/api/attachments/XUJ9ZHXG/fulltext/images/f2d991a7bbadd23f66c58d6e85bc045a5d088d1789b0f48dee01a8d2d7d492c5.jpg)  
Fig. 8. EAGLET model for a retail supply chain.  
Please cite this article as: G.L. Geerts, D.E. O'Leary, A supply chain of things: The EAGLET ontology for highly visible supply chains, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.007

G.L. Geerts, D.E. O'Leary / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/XUJ9ZHXG/fulltext/images/9609528f060427ca0a475f0f0f966162a9f1eb0ace6503774b6284d9d0ec9d35.jpg)  
Fig. 8 (continued).

referred to as the Video Case for the remainder of this paper – consists of four videos that visualize a supply chain for soup cans and focus on the production process and downstream distribution. The second case study (Metro Group [71]) – referred to as the Process Case for the remainder of this paper – focuses on downstream distribution and presents a “Process and Bene<sup>fi</sup>ts Model” for a prototypical grocery supply chain that examines key potential process differences associated with using RFID and the bene<sup>fi</sup>ts resulting from such differences.

Both cases portray the physical <sup>fl</sup>ow of things through the supply chain but deal with different supply chain con<sup>fi</sup>gurations, which is bene<sup>fi</sup>cial for the evaluation process. There is complementarity between the two cases, given that we limit ourselves to the <sup>fi</sup>rst two videos of the Video Case, which focus primarily on production, whereas the Process Case focuses primarily on the logistic processes from the end of the factory production line until products move onto the store <sup>fl</sup>oor. For simplicity purposes, returns, which are part of the “Process and Bene<sup>fi</sup>t Model,” are excluded from our analysis.

The results of our analysis of the Video Case are shown in Table 2. Operationally, we identi<sup>fi</sup>ed the events in the two videos and then chose an EAGLET pattern for each of the events. The results of our analysis of the Process Case are shown in Table 3. Operationally, we identi<sup>fi</sup>ed the events in the narrative description of the supply chain processes and then chose an EAGLET pattern for each of the events. In both tables, the EAGLET patterns are used for uniform description of the supply chain scripts underlying the respective case and the patterns employed are referenced in the last column. The <sup>fi</sup>rst <sup>fi</sup>ve columns in both tables de<sup>fi</sup>ne the supply chain activities in terms of the <sup>fi</sup>ve EAGLET primitives: Thing, Event, Agent, Location, and Equipment. Columns six and seven in Table 2 detail in which video the event takes place (1 or 2) and where the event visualization in the video is found (time). Neither of the cases includes exchange of ownership or exchange of custody information. However, to illustrate the integrated use of the custody and ownership patterns, we added a “Custody and Ownership Pattern” column in Table 3, which we completed based on assumptions, such as the assumption that the exchange of ownership between the manufacturer and the retailer occurs when the goods are unloaded at the retailer's distribution center. For Table 2, our goal was to de<sup>fi</sup>ne the complete supply chain script visualized in the two videos in terms of EAGLET. For Table 3, our starting point is a narrative description of a supply chain script. As pointed out by the authors [71], given their focus on process differences associated with using RFID, the descriptions are incomplete. The events explicitly listed as part of the “Process and Bene<sup>fi</sup>t Model” in Metro Group [71]) are underlined in Table 3, however, we attempted to portray the complete supply chain script. The events in Table 3 that are not underlined and do not have a sequence number were generated based on EAGLET's structuring rules and common business logic.

The same process was followed to analyze each case: the case was <sup>fi</sup>rst independently analyzed by each of the authors, after which a consensus was reached, represented in the tables. Differences in outcomes resulted in discussions of the EAGLET foundations and were an important part of the evaluation process.

With regard to comprehensiveness, we learned the following from our case study analysis. First, an important part of representing a supply chain is to identify its underlying events. As illustrated by the Process Case, EAGLET's patterns and structuring rules are useful tools in understanding a supply chain script and identifying the events that comprises it. For example, in Table 3, event #9 describes how pallets are loaded at the retailer's distribution center, whereas event #10 describes how pallets are unloaded at the retailer's store stockroom. It is easy to infer that a relocation event is required to complete the enterprise script. Second, using the EAGLET grammar presented in Section 5,

G.L. Geerts, D.E. O'Leary / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/XUJ9ZHXG/fulltext/images/d30506007d57e79b6155719565ab18d231c5a698f12ddfe73b43a8c77196e1b3.jpg)  
Fig. 8 (continued).

we were able to represent all events identi<sup>fi</sup>ed in both cases and therefore able to fully represent the physical <sup>fl</sup>ow of items in both supply chains. Third, EAGLET provides representational consistency using patterns. All events in Tables 2 and 3 are de<sup>fi</sup>ned in terms of EAGLET's <sup>fi</sup>ve object primitives: Thing, Event, Agent, Location, and Equipment. Such consistency is an important tool for complete and accurate speci<sup>fi</sup>- cations. For example, in Table 3, equipment is not speci<sup>fi</sup>ed (N/S) for many of the events by Metro [71]. While less-than-full EAGLET speci<sup>fi</sup>- cations are acceptable and even expected, the normative nature of the pattern raises awareness. In this particular case, the question is whether equipment was used, and if so, whether the equipment speci<sup>fi</sup>cations for these events are useful in a supply chain environment.

Overall, our comprehensiveness analysis of EAGLET using case studies, references models, regulatory guidelines, and best practices resulted in the identi<sup>fi</sup>cation of a number of modi<sup>fi</sup>cations to improve EAGLET's description of an item's physical <sup>fl</sup>ow through the value chain. More speci<sup>fi</sup>cally, four signi<sup>fi</sup>cant modi<sup>fi</sup>cations to EAGLET were identi<sup>fi</sup>ed and each is brie<sup>fl</sup>y discussed next. It is important to note that these modi<sup>fi</sup>cations are already integrated in the EAGLET ontology speci<sup>fi</sup>cation in Section 5. As such, this is a good example of the “generate– test” cycle, which is inherent in design science research.

## 7.1.1. Generalizations

Initially, loading and unloading were considered the two main handling functions. However, the modeling of different cases and other sources, such as Ballou [10], clearly indicated the existence of other handling functions. The more restrictive role names “load” and “unload” were therefore changed to ones that are more generic: “to” and “from;” see Fig. 3-1(C). Our second modi<sup>fi</sup>cation re<sup>fl</sup>ecting generalization is the use of the term “forms” to describe the creation of new con<sup>fi</sup>gurations, instead of the more restrictive term “puts-into;” see Fig. 3-1(A).

## 7.1.2. Explicit distinction between trade items and logistic units

Following other studies, such as Senneset et al. [50] and GS1 [43], an explicit distinction is made between trade items and logistic units; see Fig. 1(A). Such a differentiation enables a more accurate description of the logistic formation process.

## 7.1.3. Additional patterns: processing, entry, and disruption

Through comprehensiveness analysis, we identi<sup>fi</sup>ed three scenarios for which the existing ontological constructs did not have a clear-cut de<sup>fi</sup>nition: processing, entry, and disruption. We de<sup>fi</sup>ned the necessary primitives and patterns for each; see patterns D, E, and G in Fig. 3-1 and - 2. For example, the “disrupts” association helps to differentiate semantically between an item that was sold (exits) and an item that has perished or was stolen (disrupts). In addition, the newly created patterns have unique constellations of primitives. For example, as can be seen in Fig. 3-2(G), the disruption pattern does not include an equipment speci<sup>fi</sup>cation. Other sources [42,66] also con<sup>fi</sup>rmed the need to represent these three scenarios.

## 7.1.4. Integration of the use of equipment in several patterns

Many of the sources we used for evaluation purposes in the re<sup>fi</sup>nement phase indicated the need to record the equipment used in the different processes. For example, many of the traceability reference models – e.g., Jansen-Vullers et al. [69] – included equipment as a primitive. In addition, in food chains, equipment has often been the source of contamination. Therefore, we decided to integrate the use of equipment explicitly as part of EAGLET and <sup>fi</sup>ve of EAGLET's patterns –

G.L. Geerts, D.E. O'Leary / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/XUJ9ZHXG/fulltext/images/96475b6ea6942e1412336d0c11814433c8547984bb96984e3b8f1505f8f3e437.jpg)  
Fig. 8 (continued).

Table 2  
Evaluation: Template analysis of Metro videos.

<table><tr><td>#</td><td>Thing</td><td>Event</td><td>Agent</td><td>Location</td><td>Equipment</td><td>Metro video</td><td>Event time in movie</td><td>Pattern</td></tr><tr><td>1</td><td>Tinplate (in) cans (out)</td><td>Welding</td><td>Line supervisor (manufacturer)</td><td>Production floor manufacturer (assembly line)</td><td>Welding machine</td><td>1</td><td>0:25</td><td>3-1-a</td></tr><tr><td>2</td><td>Cans</td><td>Tagging</td><td>Line supervisor (manufacturer)</td><td>Production floor manufacturer (assembly line)</td><td>Tagging equipment</td><td>1</td><td>0:30</td><td>3-1-d</td></tr><tr><td>3</td><td>Cans</td><td>Identify damaged cans</td><td>Line supervisor (manufacturer)</td><td>Production floor manufacturer (assembly line)</td><td>Scanner</td><td>1</td><td>0:45</td><td>3-1-d</td></tr><tr><td>4</td><td>Damaged cans</td><td>Pull out</td><td>Line supervisor (manufacturer)</td><td>Production floor manufacturer (assembly line)</td><td>Robot</td><td>1</td><td>1:01</td><td>5</td></tr><tr><td>5</td><td>Soup (in) cans (in) filled cans (out)</td><td>Filling</td><td>line supervisor (manufacturer)</td><td>Production floor manufacturer (assembly line)</td><td>Filler machine</td><td>1</td><td>1:15</td><td>3-1-a</td></tr><tr><td>6</td><td>Lids (in) filled cans (in) sealed cans (out)</td><td>Sealing</td><td>Line supervisor (manufacturer)</td><td>Production floor manufacturer (assembly line)</td><td>Sealing machine</td><td>1</td><td>1:30</td><td>3-1-a</td></tr><tr><td>7</td><td>Sealed cans (in) cases (out)</td><td>Packing</td><td>Line supervisor (manufacturer)</td><td>Production floor manufacturer (assembly line)</td><td>Case packer</td><td>1</td><td>1:50</td><td>3-1-a</td></tr><tr><td>8</td><td>Cases</td><td>Tagging</td><td>Line supervisor (manufacturer)</td><td>Production floor manufacturer (assembly line)</td><td>Tagging equipment</td><td>1</td><td>2:15</td><td>3-1-d</td></tr><tr><td>9</td><td>Cases (in) pallets (out)</td><td>Packing</td><td>Line supervisor (manufacturer)</td><td>Production floor manufacturer (assembly line)</td><td>Palletizer</td><td>1</td><td>2:35</td><td>3-1-a</td></tr><tr><td>10</td><td>Pallets</td><td>Tagging</td><td>Line supervisor (manufacturer)</td><td>Production floor manufacturer (assembly line)</td><td>Tagging equipment</td><td>1</td><td>2:38</td><td>3-1-d</td></tr><tr><td>11</td><td>Pallets</td><td>Validation</td><td>Line supervisor (manufacturer)</td><td>Production floor manufacturer (assembly line)</td><td>Scanner</td><td>1</td><td>2:44</td><td>3-1-d</td></tr><tr><td>12</td><td>Pallets</td><td>Loading pallets from assembly line to pallet mover</td><td>Driver pallet mover (manufacturer)</td><td>Production floor manufacturer (assembly line)</td><td>Pallet mover</td><td colspan="2">Not shown in video (inference)</td><td>3-1-c</td></tr><tr><td>13</td><td>Pallets</td><td>Relocation</td><td>Driver pallet mover</td><td>From production floor to loading dock (manufacturer)</td><td>N/A</td><td>2</td><td>0:16</td><td>3-1-b</td></tr><tr><td>14</td><td>Pallets</td><td>Unloading/loading</td><td>Driver pallet mover</td><td>Loading dock (manufacturer)</td><td>Pallet mover (to truck)</td><td>2</td><td>0:36</td><td>3-1-c</td></tr><tr><td>15</td><td>Pallets</td><td>Relocation</td><td>Truck driver (third party)</td><td>From manufacturer to distribution center</td><td>N/A</td><td>2</td><td>0:42</td><td>3-1-b</td></tr><tr><td>16</td><td>Pallets</td><td>Unloading pallets from truck to pallet mover</td><td>Pallet mover handler</td><td>Loading dock (distribution center)</td><td>Pallet mover (from truck)</td><td>2</td><td>1:30</td><td>3-1-c</td></tr></table>

Please cite this article as: G.L. Geerts, D.E. O'Leary, A supply chain of things: The EAGLET ontology for highly visible supply chains, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.09.007

Evaluation: Template analysis of Metro's process and bene<sup>fi</sup>ts model.

<table><tr><td>#</td><td>Thing</td><td>Event</td><td>Agent</td><td>Location</td><td>Equipment</td><td>Custody and ownership Pattern</td><td>Physical flow Pattern</td></tr><tr><td rowspan="2">1</td><td>Cases (in) pallets (out)</td><td>Assembly tagging pallets</td><td>Manufacturer</td><td>Factory</td><td>N/S</td><td>N/A</td><td>3-1-a 3-1-d</td></tr><tr><td>Pallets</td><td>Loading; relocation to warehouse</td><td>Manufacturer</td><td>Factory; from factory to warehouse</td><td>N/S</td><td>N/A</td><td>3-1-c 3-1-b</td></tr><tr><td>2</td><td>Pallets</td><td>Goods receipt and staging: unloading</td><td>Manufacturer</td><td>Warehouse</td><td>N/S</td><td>N/A</td><td>3-1-c</td></tr><tr><td>3</td><td>Pallets (in) Grouping of Pallets (out)</td><td>Truckload assembly</td><td>Manufacturer</td><td>Warehouse</td><td>Forklift</td><td>N/A</td><td>3-1-a</td></tr><tr><td rowspan="2">4</td><td>Pallets</td><td>Truck loading</td><td>Manufacturer</td><td>Warehouse</td><td>Forklift (uses), truck (to)</td><td>3-3-H (custody to third party)</td><td>3-1-c</td></tr><tr><td>Pallets</td><td>Relocation</td><td>Third party logistics provider</td><td>From warehouse to distribution center</td><td>N/A</td><td>N/A</td><td>3-1-b</td></tr><tr><td>5</td><td>Pallets</td><td>Shipment receipt and staging: unloading</td><td>Retailer</td><td>Distribution center</td><td>Truck (from)</td><td>3-3-H; 3-3-I (custody and ownership to retailer)</td><td>3-1-c</td></tr><tr><td>6</td><td>Pallets (in) Cases (out)</td><td>Pallet breaking</td><td>Retailer</td><td>Distribution center</td><td>N/S</td><td>N/A</td><td>3-1-a</td></tr><tr><td>7</td><td>Cases (in) Pallets (out)</td><td>Mixed pallet picking</td><td>Retailer</td><td>Distribution center</td><td>Hand Lift truck</td><td>N/A</td><td>3-1-a</td></tr><tr><td>8</td><td>Pallets (in) Grouping of Pallets (out)</td><td>Order assembly</td><td>Retailer</td><td>distribution center</td><td>N/S</td><td>N/A</td><td>3-1-a</td></tr><tr><td rowspan="2">9</td><td>Pallets</td><td>Truck loading</td><td>Retailer</td><td>Distribution center</td><td>Truck (to)</td><td>3-3-H (custody to third party)</td><td>3-1-c</td></tr><tr><td>Pallets</td><td>Relocation</td><td>Third party logistics provider</td><td>From distribution center to retailer (store stockroom)</td><td>N/A</td><td>N/A</td><td>3-1-b</td></tr><tr><td>10</td><td>Pallets</td><td>Order receipt and pallet staging: unloading</td><td>Retailer</td><td>Store stockroom</td><td>Truck (from)</td><td>3-3-H (custody to retailer)</td><td>3-1-c</td></tr><tr><td>11</td><td>Pallets (in) Cases (out)</td><td>Breakdown</td><td>Retailer</td><td>Store stockroom</td><td>N/S</td><td>N/A</td><td>3-1-a</td></tr><tr><td>12</td><td>Cases</td><td>Routing: loading, relocation, unloading</td><td>Retailer</td><td>Store stockroom</td><td>N/S</td><td>N/A</td><td>5</td></tr><tr><td>13</td><td>Cases (in) Products (out)</td><td>Breakdown</td><td>Retailer</td><td>Store stockroom</td><td>N/S</td><td>N/A</td><td>3-1-a</td></tr><tr><td>14</td><td>Products</td><td>Restocking: load, relocation, unload</td><td>Retailer</td><td>From store stockroom to store floor</td><td>N/S</td><td>N/A</td><td>5</td></tr></table>

recon<sup>fi</sup>guration, handling, processing, entry, and exit – were modi<sup>fi</sup>ed accordingly.

## 7.2. Strength analysis

Grubic and Fan [17] presented an extensive analysis of supply chain ontologies. The outcome of their study was the identi<sup>fi</sup>cation of several major weaknesses in existing supply chain ontologies. Next, we leverage their weakness analysis to articulate the strengths of the EAGLET ontology. Table 4 summarizes how we convert the weaknesses presented by Grubic and Fan [17] to a set of <sup>fi</sup>ve criteria that we use to evaluate EAGLET's strengths: scope, granularity, traceability, semantic richness, and relevance.

## 7.2.1. Scope

Scope, in the context of this paper, refers to the set of phenomena that are part of the supply chain and addressed by the ontology. Grubic and Fan [17] argue that the scope of the existing supply chain ontologies is too restricted. First, as part of their study, they concluded that all existing supply chain ontologies focus on the strategic level and do not address the operational level. At the strategic level, a blueprint for implementation is established. At the operational level, the actualization of the supply chain business processes is described [72]. The EAGLET ontology aims to follow transactions of individual items, cases, pallets, or even truck shipments, and therefore accounts for the operational level. Currently, EAGLET does not focus on strategic concepts, and therefore, one could argue that the ontologies reviewed by Grubic and Fan [17] and the EAGLET ontology are complementary.

Second, Grubic and Fan [17] relied on a study by Harland [73] to differentiate between four different types of supply chain relationships: (1) internal supply chain; (2) dyadic relationship; (3) external supply chain; and (4) inter-business network. After completing their analysis, they concluded that most of the ontologies focus on the internal supply chain only, while none of them addressed dyadic relationships or external supply chains. In contrast, the EAGLET ontology is capable of supporting all four relationship types. Both intra- and interorganizational physical <sup>fl</sup>ows of things are supported, and the ownership and custody patterns are especially useful for capturing dyadic relationships.

Third, Grubic and Fan [17] argued that existing supply chain ontologies focus on manufacturing activities and do not consider other activities, such as replenishment, transport, and reverse logistics, and such practices can be captured easily by EAGLET's patterns.

## 7.2.2. Granularity

As part of their study, Grubic and Fan [17] concluded that all existing supply chain ontologies focus on the strategic level and therefore, deal with coarse descriptions of supply chain <sup>fl</sup>ows. In contrast, the EAGLET ontology focuses on the operational level and therefore deals with more re<sup>fi</sup>ned descriptions of supply chain <sup>fl</sup>ow.

Generally, the decision of what granularity level to use to describe the <sup>fl</sup>ow of things through a supply chain is complex and has several dimensions; Karlsen et al. [74] explore the optimal granularity level for traceability purposes. Another complex issue is the effect a mixed level of granularity – in our case, across the supply chain – has on interoperability [75]. As discussed in Section 5, EAGLET is a meta-model that does not prescribe at what level of granularity things, events, locations, and other information needs to be described. However, it provides mechanisms to integrate different granularity levels, such as the use of the recon<sup>fi</sup>guration pattern to describe part–whole relationships between things. IoI technologies and the Supply Chain of Things re<sup>fl</sup>ect the trend toward more <sup>fi</sup>ne-grained descriptions of supply chain <sup>fl</sup>ows; EAGLET is designed for such an environment.

Table 4 Strength analysis: Summary.

<table><tr><td rowspan="2">Evaluation criteria</td><td>Weaknesses of existing supply chain ontologies</td><td>EAGLET&#x27;s strengths</td></tr><tr><td>Grubic and Fan [17]</td><td>This paper</td></tr><tr><td>#1: Scope</td><td>Only a subset of the phenomena that are part of a supply chain are covered in existing supply chain ontologies.First, all existing supply chain ontologies focus on the strategic level and there is no work into the operational level.Second, the majority of supply chain ontologies focus on the internal supply chain only while none of them capture dyadic relationships or external supply chains.Third, existing supply chain ontologies focus on manufacturing activities.</td><td>First, the EAGLET ontology focuses on the operational level—the physical flow of an item through the Supply Chain of Things.Second, the EAGLET ontology is capable of supporting the four types of supply chain collaborations recognized in Harland [73]: (1) internal supply chain, (2) dyadic relationship, (3) external supply chain, and (4) inter-business network.Third, the EAGLET ontology is able to accommodate non-manufacturing activities such as replenishment, transportation, and reverse logistics.</td></tr><tr><td>#2: Granularity</td><td>High level of granularity given that all existing supply chain ontologies focus on the strategic level.</td><td>Lower level of granularity given that the EAGLET ontology focuses on the operational level.Further, EAGLET is a meta-model which enables to model physical flows of things at different levels of granularity.</td></tr><tr><td>#3: Traceability</td><td>None of the existing ontologies address tracking or tracing.</td><td>As shown by the different patterns in Section 5, tracking and tracing are an integral part of the EAGLET ontology.</td></tr><tr><td>#4: Semantics richness</td><td>The majority of existing supply chain ontologies focuses on terminology to solve interoperability problems.</td><td>EAGLET is situated in the middle of the ontology spectrum (conceptual schema) and is semantically richer than taxonomies or thesauri.EAGLET further incorporates a large set of domain-specific structuring rules.</td></tr><tr><td>#5: Relevance</td><td>The majority of existing supply chain ontologies are based on inspiration and synthesis.They do not rely enough on the vast theoretical base pertinent to supply chain management and lack any real-world validation and are therefore too remote from actual real-world practice.</td><td>EAGLET was developed in two phases: (1) during the incubation phase, EAGLET&#x27;s design was primarily theory-driven (economic and supply chain theory), and (2) during the refinement phase, EAGLET&#x27;s design was improved based on validation against more practice-oriented sources such as real-world cases.</td></tr></table>

## 7.2.3. Traceability

Grubic and Fan [17] stated that none of the existing ontologies address the tracking and tracing of materials. In contrast, improved traceability and visibility are key goals of the EAGLET ontology. In essence, EAGLET captures the locations of things that move through the supply chain to ensure visibility.

## 7.2.4. Semantic richness

Grubic and Fan [17] concluded that the majority of existing supply chain ontologies focus on terminology to solve interoperability issues. Such efforts are typically associated with ontological speci<sup>fi</sup>cations that take the form of taxonomies or thesauri, which are considered to have weak semantics in the ontology spectrum presented in Obrst [76]. The EAGLET ontology is much broader than just terminological de<sup>fi</sup>nitions and includes a set of semantic primitives and associations, patterns, and scripts. In terms of the ontological spectrum, it is a conceptual model, situated in the middle: richer in semantics than taxonomies and thesauri but weaker in semantics than logical theories. EAGLET's semantics could be further extended by de<sup>fi</sup>ning them in formal languages, which would also make them available for advanced automated reasoning.

## 7.2.5. Relevance

Relevance, in the context of this paper, refers to the level of compliance of the ontological speci<sup>fi</sup>cations to real-world practices. Grubic and Fan [17] argue that the methodological approaches adopted by existing supply chain ontologies are too remote from real-world practices, primarily because they rely heavily on inspiration and synthesis. EAGLET's level of compliance with real-world practices is much higher, given the sources used for its development. The primitives and structuring rules de<sup>fi</sup>ned in the incubation phase are grounded in economic and supply chain theory. During the re<sup>fi</sup>nement phase, EAGLET's content was validated against a series of practice-oriented sources, such as the Metro Group cases.

## 8. Conclusions and further research directions

The purpose of this paper was to generate an ontology for a HVSC where the location and other characteristics of individual things could be captured and traced, including their current location, their past locations, what has happened to them, who has handled them, how they were transported, and other concerns. The resulting ontology, EAGLET, integrates three different perspectives: the physical <sup>fl</sup>ow, the chain of custody, and the chain of ownership. In addition, EAGLET's strong semantics are an important asset in addressing interoperability issues and improving communication across the supply chain and thus, improving collaborative decision making. A unique characteristic of EAGLET is the inclusion of a large set of structuring rules that take the form of stereotypical patterns, meta-patterns, and economic scripts and that improve the accuracy of the supply chain speci<sup>fi</sup>cations and result in consistency across the supply chain.

The DSRM [27] was used to develop EAGLET. In addition to strong articulations of problem identi<sup>fi</sup>cation, motivation, and objectives, we demonstrated EAGLET by applying it to a retail supply chain scenario and evaluated it using comprehensiveness and strength analysis. Table 5 further summarizes how each of the seven guidelines for design science information systems research, outlined in Hevner et al. [26], were addressed in this paper.

There are additional aspects of the EAGLET ontology that could result in further research. First, EAGLET could be further formalized beyond the current knowledge level formulation. Second, the EAGLET ontology could be extended to address more supply chain practices, such as the collaboration between supply chain partners to plan and forecast. Third, other uses of the EAGLET ontology than as an instantiation pattern could be explored; applications would especially bene<sup>fi</sup>t from the semanticization of supply chain data in terms of the EAGLET ontology. Advantages and potential uses resulting from ontology based semanticization are discussed in Geerts and McCarthy [77] and De¸˘dek et al. [78]. Fourth, although we have focused on inventory visibility, additional efforts could focus on other visibility issues, such as <sup>fi</sup>xed asset and agent visibility. For example, we could build an ontology to explore the use and control of <sup>fi</sup>xed assets or an ontology to track employees and visitors. Fifth, in the Internet of Things, things can communicate with other things; in our case, that would mean inventory objects could communicate with other inventory objects. As a result, we could extend the work here to characterize those communications. Finally, evaluation of domain ontologies is an underdeveloped research area. In this paper, we conducted preliminary evaluations based on comprehensiveness analysis and strength analysis; however, alternative evaluation studies could rely on other methods, such as behavioral experiments.

Adherence to design science research guidelines.

<table><tr><td>Guideline</td><td>Paper contribution</td></tr><tr><td>#1: Design as an artifact</td><td>The EAGLET ontology: an ontological specification of the primitives and structuring rules for constructing models that describe the movements of things across the supply chain</td></tr><tr><td>#2: Problem relevance</td><td>Instantiations of the EAGLET ontology result in highly visible and interoperable descriptions of supply chain phenomena from three different perspectives – physical flow, custody, and ownership – that address problems, such as lack of visibility, that negatively impact information regarding when an item should arrive and things that are lost in store rooms and throughout the supply chain.</td></tr><tr><td>#3: Design evaluation</td><td>The design of the EAGLET ontology followed the prototypical generate–test cycle for design science research.The patterns generated are consistent with notions of the Internet of Things.Testing was done through comprehensiveness analysis, including the evaluation of EAGLETS&#x27;s ability to represent the supply chain scripts of a large retail company.Gap analysis was used to evaluate EAGLET&#x27;s overall strengths compared to other supply chain ontologies.</td></tr><tr><td>#4: Research contributions</td><td>EAGLET is an ontology that enables a comprehensive understanding of the phenomena that can happen to a thing when it moves across the supply chain and therefore, facilitates a HVSC capability.It mitigates many limitations of previous supply chain ontologies, as identified in a recent study.</td></tr><tr><td>#5: Research rigor</td><td>EAGLET was rigorously designed based on (1) strong reliance on economic and supply chain theory and (2) heavy use of the generate–test cycle, including testing of its comprehensiveness against real-world case studies, reference models, regulatory guidelines, and best practices.</td></tr><tr><td>#6: Design as a search process</td><td>The design of EAGLET is an inherently iterative process.During the incubation phase, EAGLET&#x27;s design was primarily theory-driven.During the refinement phase, its comprehensiveness and strengths were evaluated, resulting in several modifications. Possible areas for further research are also identified.</td></tr><tr><td>#7: Communication of research</td><td>A paper summarizing the developed artifact and its modifications through the generate–test cycle is presented.The ideas have been presented to a wide variety of audiences, including accounting, information systems, and supply chain management audiences.</td></tr></table>

## Acknowledgments

We appreciate the helpful comments of the editor, three anonymous reviewers, Wim Laurier, the participants of the Drexel iSchool workshop, and the participants of the 4th International Conference on Knowledge Engineering and Ontology Development.

## References

[1] N. Gershenfeld, R. Krikorian, D. Cohen, The internet of things, Scienti<sup>fi</sup>c American 291 (4) (2004) 76–81.

[2] D.E. O'Leary, Supporting decisions in real time enterprises: autonomic supply chain systems, Information Systems and e-Business Management 6 (3) (2008) 239–255.

[3] A. Llic, T. Andersen, F. Michahelles, Increasing supply-chain visibility with rulebased RFID data analysis, IEEE Internet Computing 13 (1) (2009) 31–38.

[4] M. Roberti, Metro details some of its RFID successes, RFID Journal (2009)(available from: http://www.r<sup>fi</sup>djournal.com/article/print/5332, (accessed on February 15, 2012)).

[5] PRN Newswire, Metro group and checkpoint systems expand tag-it-easy program, available from: http://www.prnewswire.com/news-releases/metro-groupand-checkpoint-systems-expand-r<sup>fi</sup>d-tag-it-easy-program-59833772.html 2009 (accessed February 15, 2012).

[6] M. Hui, In organic hungry Hong Kong, corn as high as an elevator's climb, New York Times, October 3, 2012.

[7] D. Derbyshire, Poison food in shops for three weeks, available from: http:// www.dailymail.co.uk/health/article-1344914/Dioxin-scandal-Food-containingcontaminated-eggs-Germany-shops-3-WEEKS.html 2011(accessed February 15, 2012).

[8] S.D. Pathak, J.D. Day, A. Nair, W.J. Sawaya, M.M. Kristal, Complexity and adaptivity in supply networks: building a supply network theory using a complex adaptive systems perspective, Decision Sciences 38 (4) (2007) 547–577.

[9] European Commission, Internet of things: strategic research roadmap, https://www. google.com/#bav=on.2,or.r\_qf.&fp=96772b0512365327&q=22.%09European+ Commission%2C+Internet+of+Things:+Strategic+Research+Roadmap%2C+15+ September+2009 September 15 2009

[10] R.H. Ballou, Business Logistics—Supply Chain Management Planning, Organizing and Controlling the Supply Chain, <sup>fi</sup>fth ed. Pearson—Prentice Hall, New Jersey, 2004.

[11] T. Gruber, A translation approach to portable ontology speci<sup>fi</sup>cations, Knowledge Acquisition 5 (2) (1993) 199–220.

[12] B. Chandrasekaran, J. Josephson, V.R. Benjamins, What are ontologies and why do we need them? IEEE Intelligent Systems 14 (1) (1999) 20–26.

[13] K. Ashton, That ‘internet of things’ thing, available from: http://www.r<sup>fi</sup>djournal. com/article/view/49862009(accessed February 15, 2012).

[14] SRA, The internet of things strategic road map, available from: http://www. internet-of-things-research.eu/pdf/IoT\_Cluster\_Strategic\_Research\_Agenda\_2009. pdf 2009(accessed February 15, 2012).

[15] A. Smirnov, C. Chandra, Ontology-based knowledge management for co-operative supply chain con<sup>fi</sup>guration, Proceedings of the 2000 AAAI spring symposium on bringing knowledge to business processes, AAAI Press, Stanford, CA, 2000, pp, 85–92.

[16] D. Frey, T. Stockheim, P. Woelk, R. Zimmerman, Integrated multi-agent-based supply chain management, Proceedings of the 12th IEEE international workshops on enabling technologies: Infrastructure for collaborative enterprises, Linz, Austria, 2003, pp. 24–29.

[17] T. Grubic, I. Fan, Supply chain ontology: review, analysis, and synthesis, Computers in Industry 61 (2010) 776–786.

[18] H. Ringsberg, Traceability in food chains. exploring governmental authority and industrial effects, available from: http://lup.lub.lu.se/luur/download?func= downloadFile&recordOId=1857150&<sup>fi</sup>leOId=1858923 2011(accessed February 15, 2012).

[19] M. Chui, M. Lof<sup>fl</sup>er, R. Roberts, The internet of things, McKinsey Quarterly 2 (2010) 1–9.

[20] B. Yan, G. Huang, Supply chain information transmission based on RFID and the internet of things, Proceeding of the 2009 ISCECS International Colloquium on Computing Communication Control and Management Sanva China 2oo9 pp. 166–169.

[21] E. Fleisch, What is the internet of things?, available from: http://www.autoidlabs. org/uploads/media/AUTOIDLABS-WP-BIZAPP-53.pdf 2010(accessed February 15, 2012).

[22] C. Katsma, H. Moonen, J. Hillegersberg, Supply chain maturing towards the internet of things: a framework, Proceedings of the 24th Bled eConference, eFuture: Creating Solutions for the Individual, Organizations and Society, Bled, Slovenia, 2000.

[23] Norwegian Oil and Gas Association, Deployment of radio frequency identification in the oil and gas industry, https://www.posccaesar.org/svn/pub/LogisticHub/121127\_ Guideline\_112\_Part2\_Architecture\_and\_Integration\_Draft.pdf 2012(accessed February 15, 2013).

[24] Z. Li, C. Chu, W. Yao, SIP-RLTS: an RFID location tracking system based on SIP, IEEE international conference on RFID, 2008, pp. 173–182.

[25] R. Chen, M. Tu, Development of an agent-based system for manufacturing control and coordination with ontology and RFID technology, Expert Systems with Applications 36 (4) (2009) 7581–7593.

[26] A. Hevner, S. March, J. Park, S. Ram, Design science in information systems research, MIS Quarterly 28 (1) (2004) 75–105.

[27] K. Peffers, T. Tuunanen, M.A. Rothenberger, S. Chatterjee, A design science research methodology for information systems research, Journal of Management Information Systems 24 (3) (2008) 45–77.

[28] M. Holmstrom, A.P. Ketokivi, Hameri, Bridging practice and theory: a decision science approach, Decision Sciences 40 (1) (2009) 65–87.

[29] W.E. McCarthy, The REA accounting model: a generalized framework for accounting systems in a shared data environment, The Accounting Review 57 (1982) 554–578.

[30] G.L. Geerts, W.E. McCarthy, The ontological foundation of REA enterprise information systems, available from: http://www.msu.edu/user/mccarth4/ alabama.doc 2000(accessed February 15, 2012).

[31] G.L. Geerts, A design science research methodology and its application to accounting information systems research, International Journal of Accounting Information Systems 12 (2011) 127–150.

[32] G. Mintchel, Interoperability test for internet of things a success, Automation World, 2011. (available from: http://www.automationworld.com/information-management/ interoperability-test-internet-things-success, (accessed February 15, 2012)).

[33] L. Atzori, A. Lera, G. Morbito, The internet of things: a survey, Computer Networks 54 (15) (2010) 2787–2805.

[34] S. Liu, F. Wang, P. Liu, Integrated RFID data modeling: an approach for querying physical objects in pervasive computing, Proceedings of the International Conference on Information and Knowledge Management, Arlington, Virginia, 2006.

[35] F. Wang, S. Liu, P. Liu, A temporal RFID data model for querying physical objects, Pervasive and Mobile Computing 6 (3) (2010) 382–397.

[36] R. Boss, Danish National Library Authority, RFID Data Model for Libraries Working Group, Danish National Library Authority, 2005.

[37] D. Luckham, The power of events, An Introduction to Complex Event Processing in Distributed Enterprise Systems, Addison-Wesley, Boston, MA, 2002.

[38] G. Barros, A. Decker, A. Grosskopf, Complex events in business processes, Lectur Notes in Computer Science, 4439, Springer, Verlag, 2007, pp. 29–40.

[39] C. Chan, H.K. Chow, W.S. Siu, H. Lang, H.L. Ng, T.H. Chu, H.C. Chan, C. Chan, H.K. Chow, W.S. Siu, H. Lang, H.L. Ng, T.H. Chu, H.C. Chan, A multi-agent-based RFID framework for smart-object applications, Proceedings of the international multiconference of engineers and computer scientists (IMECS), Hong Kong, 2012.

[40] D.L. Brock, T.O. Milne, Y.K. Kang, B. Lewis, The physical markup language. Core components: time and place, available from: http://www.tracefood.org/images/5/58 TCX\_BarcaMeeting\_20090205\_TT\_presentation.pdf 2009(accessed February 15, 2012).

[41] S. Kjaernsrod, R. Hancke, H. Bjastad, TraceCore and EPCglobal, available from: http:// 193.156.107.66/ff/po/Trains/XML\_presentasjoner%5CTraceCore.pdf 2007(accessed February 15, 2012).

[42] Food Marketing Research and Information Center, Handbook for Introduction of Food Traceability Systems, second ed., 2007. (Tokyo, Japan).

[43] GS1, GS1 standards, business process and systems requirements for full chain traceability, issue 1.2.2, available from: http://www.gs1.org/docs/gsmp/traceability/ Global\_Traceability\_Standard.pdf 2010(accessed February 15, 2012).

[44] A. Gomez-Perez, Knowledge sharing and reuse, in: J. Liebowitz (Ed.), The Handbook of Applied Expert Systems, CRC, Northwest Boca Raton, FL, 1998, pp. 10–36, (Ch. 10).

[45] R. Haugen, W.E. McCarthy, REA, a semantic model for internet supply chain collaboration, in: J. Sutherland (Ed.), Business Objects and Component Design and Implementation Workshop VI: Enterprise Application Integration, 2000, (available from: http://jeffsutherland.org/oopsla2000/mccarthy/mccarthy. htm, (accessed February 15, 2012)).

[46] A. McAfee, G. Bounds, Extricity, Harvard Business School, 2001. (9-601-113).

[47] K.J. Van Dorp, Tracking and tracing: a structure for development and contemporary practices, Logistics Information Management 15 (1) (2002) 24–33.

[48] International Organization for Standardization (ISO), Information Technology— Business Operational View, Part 4: Business Transaction Scenarios—Accounting and Economic Ontology International Organization for Standardization 20o7.

[49] G.L. Geerts, H.J. Wang, The timeless way of building REA enterprise systems, Journal of Emerging Technologies in Accounting 4 (2007) 161–182

[50] G. Senneset, E. Foras, K.M. Fremme, Challenges regarding implementation of electronic chain traceability, British Food Journal 109 (2007) 805–818.

[51] J.R. Hobbs, F. Pan, An ontology of time for the semantic web, ACM Transactions on Asian Language Information Processing 3 (1) (2004) 66–85.

[52] E.W. Schuster, S.J. Allen, D.L. Brock, Global RFID: The Value of the EPCglobal Network for Supply Chain Management, Springer, London, 2007

[53] S. Liu, F. Wang, P. Liu, A temporal RFID data model for querying physical objects, Technical Report TR-88, TimeCenter, 2007. (available from: http://timecenter.cs. aau.dk/TimeCenterPublications/TR-88.pdf, (accessed February 15, 2012)).

[54] EPCGlobal, EPC information services (EPCIS) version 1.0 speci<sup>fi</sup>cation, available from: http://www.epcglobalinc.org/standards/epcis/epcis\_1\_0-standard-20070412. pdf 2007(accessed February 15, 2012).

[55] Y. Ijiri, Theory of Accounting Measurement, American Accounting Association, Sarasota FL 1975

[56] A. Bechini, M.G.C.A. Cimino, F. Marcelloni, A. Tomasi, Patterns and technologies for enabling supply chain traceability through collaborative e-business, Information and Software Technology 50 (4) (2008) 342–359.

[57] I. Fisher, The Nature of Capital and Income, MacMillan, 1906.

[58] M. Lewis, A. Rai, D. Forquer, UPS and HP: Value Creation through Supply Chain Partnerships, Ivey, 2007. (907D02).

[59] V.K. Vaishnavi, W.J. Kuechler, Design Science Research Methods and Patterns: Innovating Information and Communication Technology, Auerbach, New York, NY 2007.

[60] E.F. Codd, A relational model of data for large shared data banks, Communications of the ACM.13 (6) (1970) 377-387

[61] P.P. Chen, The entity-relationship model—toward a uni<sup>fi</sup>ed view of data, ACM Transactions on Database Systems 1 (1) (1976) 9–36.

[62] J.D. Black, A.G. Black, Production Organization, Henry Holt and Company, 1929

[63] D.J. Bowersox, D.J. Closs, M.B. Cooper, Supply Chain Logistics Management, second ed. McGraw-Hill Irwin, Boston, MA. 2007.

[64] T. Nguyen, Y.K. Lee, R. Huq, B.S. Jeong, S. Lee, A data model for EPC information services, available from: http://www.ieice.org/iss/de/DEWS/DEWS2007/pdf/m6-3. pdf 2007(accessed February 15, 2012).

[65] K.A.M. Donnelly, K.M. Karlsen, P. Olsen, The importance of transformations for traceability—a case study of lamb and lamb products, Meat Science 83 (1) (2009) 68–73.

[66] M. Thakur, C.R. Hurburgh, Framework for implementing traceability system in a bulk grain supply chain, Journal of Food Engineering 95 (4) (2009) 617–626.

[67] Z. Ton, V. Dessain, M. Stachowiak-Joulain, RFID at the Metro Group, Harvard Business School, April 1, 2009. (9-606-053).

[68] K.M. Karlsen, P. Olsen, K.A.M. Donnelly, Implementing traceability: practical challenges at a mineral water bottling plant, British Food Journal 112 (2) (2010) 187–197.

[69] M. Jansen-Vullers, C. Wan Dorp, A. Beulens, Managing traceability information in manufacture, International Journal of Information Management 23 (5) (2003) 395–413.

[70] Metro Group videos, “RFID in Use at the Producer,” “RFID in use at Logistics and Transport,” “Einsatz von RFID im Zwishenlager” (RFID in use at the Warehouse), “Ensatz von RFID im Future Store” (RFID in use at the Future Store), No date.

[71] Metro Group, RFID: Uncovering the Value: Applying RFID within the Retail and Consumer Package Goods Value Chain, Report, Metro Group Future Store Initiative, 2004.

[72] K.K. Croxton, S.J. Garcia-Dastugue, D.M. Lambert, D.S. Rogers, The supply chain management processes, International Journal of Logistics Management 12 (2) (2001) 13–36.

[73] C.M. Harland, Supply chain management: relationships, chains and networks, British Journal of Management 7 (1996) S63–S80(Special Issue).

[74] K.M. Karlsen, K.A.M. Donnelly, P. Olsen, Granularity and its importance for traceability in a farmed salmon supply chain, Journal of Food Engineering 102 (2011) 1–8.

[75] G. Maiga, D. Williams, A reference model for biomedical ontology evaluation: the perspective of granularity International Journal of Computing and ICT Research 5 (1) (2011) 35–52.

[76] L. Obrst, Ontologies for semantically interoperable systems, Proceedings of the 12th international conference on information and knowledge management, 2003, pp. 366–369.

[77] G.L. Geerts, W.E. McCarthy, Augmented intensional reasoning in knowledge-based accounting systems, Journal of Information Systems 14 (2) (2000) 127–150.

[78] J.A. De¸˘dek, A. Eckhardt, P. Vojtá , Web semantization—design and principles, in: V. Snášel, P.S. Szczepaniak, A. Abraham, J. Kacprzyk (Eds.), Advances in Intelligent Web Mastering-2, Proceedings of the 6th Atlantic Web Intelligence Conference(AWIC), Prague, Czech Republic, 2009, pp. 3–18.

[79] OMG, Uni<sup>fi</sup>ed Modeling Language: Infrastructure, version 2.1.2, OMG, 2007.
