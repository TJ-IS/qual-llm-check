---
otero_id: 5172
otero_key: "NGB8CEES"
title: "Enterprise model management and next generation decision support"
authors: "Michael Goul; Karen Corral"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.05.023"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Enterprise model management and next generation decision support

Michael Goul, Karen Corral <sup>\*</sup>

Department of Information Systems, W. P. Carey School of Business, P.O. Box 874606, Arizona State University Tempe, AZ 85287-4606, United States

Available online 12 July 2005

## Abstract

The papers included in this special issue sponsored by the Association for Information Systems’ Special Interest Group in Decision Support, Knowledge and Data Management Systems are drawn from the first Annual Pre-ICIS SIG DSS Workshop. These papers and the presentations at the workshop highlight an important new direction for integrated decision support: enterprise model management (EMM). In this paper we discuss our underlying assumptions and suggest several EMM research propositions supported by evidence from the papers included in the special issue. We conclude with our thoughts on harnessing EMM for sustainable competitive advantage. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Decision support systems; Enterprise model management

## 1. Introduction

This special issue on integrated decision support is the culmination of the inaugural pre-ICIS workshop of the Special Interest Group in Decision Support, Knowledge and Data Management Systems (an affiliate of the Association for Information Systems). SIG DSS is an international group of researchers dedicated to the pursuance of research to support decision making. The topic of the workshop, integrated decision support, led to a wide variety of submissions representing the breadth of this field. Integrated decision support not only includes the people, processes and systems involved in decision making, it also includes the processes and systems designed to coordinate multiple, disparate, and distributed organizational and inter-organizational decision points, contexts and resources to create value. As such, integrated decision support requires a wide-angle view of the organization including advancements in data warehouses, knowledge management and model management. Such a view is possible through the lens of enterprise model management (EMM). We define EMM research as the field of study devoted to all of the following aspects.

<sup>!</sup> Furthering the objectives of enterprise modeling, artifact and ontology transformation, and mapping to unified representations.

<sup>!</sup> Defining and expanding the models and operators needed to manipulate, integrate, maintain and store those unified representations in facilitation of organizational decision support services.

<sup>!</sup> Extending the notion of interoperability to higher levels of individual, group and organizational cooperation, collaboration, and interwork (i.e., interorganizational work systems).

<sup>!</sup> Directing the design, development and empirical study of efficient and effective solutions for enabling these new, higher level notions of interoperability.

<sup>!</sup> Advancing the role of integrated decision support in sustaining competitive advantage for <sup>b</sup>networked<sup>Q</sup> or <sup>b</sup>smart<sup>Q</sup> organizations where interwork is common.

<sup>!</sup> Exploring new theories and expanding existing theories of inter-organizational decision support that can serve to advance knowledge about EMM representations, operations, services, support for interwork, and the capability of integrated decision support to provide sustained competitive advantage.

To discuss EMM, it is helpful to begin by examining the history of enterprise modeling (EM). Traditional EM has been around for some time, with approaches ranging from vertical scopes, such as computer integrated manufacturing, to more ambitious organization-encompassing efforts (e.g., [15,16,39,41,42,46,48]). EM is the set of activities, processes, representations and conceptualizations used to develop an enterprise model to address both better enterprise integration and to perform analyses of an enterprise. Most researchers believe that an enterprise model is not a monolithic model, rather it is an assemblage of models (e.g., [43,44]). Recent efforts in formalizing a unified EM language (UEML) were initiated with requirements expanding on that definition as follows.

The prime goal of EM is not only to be applied for better enterprise integration, but also [to be] able to support analysis of an enterprise, and more specifically, to represent and understand how an enterprise works, to capitalize on acquired knowledge and know-how for later reuse, to design (or redesign) a part of the enterprise, to analyze some aspects of the enterprise (by economic analysis, organization analysis, qualitative or quantitative analysis, . . .), to simulate the behavior of (some part of) the enterprise, to make better decisions about enterprise operations and organization, or to control, coordinate and monitor some parts of the enterprise [32].

In a recent critique of traditional EM research and practice, as related to next generation ERP-type systems, four gaps were identified: (1) A lack of formal theory enabling quantitative analysis, (2) Approaches to modeling processes, as a significant aspect of more general EM, have not kept pace with the distributed computing paradigm—including internet technologies, (3) The semantics associated with process redesign lack enterprise-level constructs such as cost and time, and (4) Inadequate linkages between business and production engineering process modeling approaches, particularly with respect to the properties of scalability and dynamism which are necessary to achieve those linkages [11]. We believe that the broad lens of decision support, knowledge and data management systems research can address these challenges, and we offer a research perspective with supporting evidence by the papers included in this special issue. We conclude with an extended challenge to our newly formed community to articulate, formulate, critique and advance enterprise model management (EMM) as a significant aspect of the next generation decision support research agenda.

## 2. Reasons for EMM

Since decision making does not take place in a vacuum, organizational contexts influence virtually every aspect of the processes involved. This invites the question, <sup>b</sup>What is an organization—and how do we model it?<sup>Q</sup> Fox et al. [17] address the question by stating that, <sup>b</sup>Many disciplines have explored the former, and every information system built has been a version of the latter.<sup>Q</sup> This point is valid for most of the research-oriented systems and many of the commercial software products associated with decision support. It is also true of the organization-related research in knowledge management, and it is true for most business intelligence and data management suites as well. In fact, many of the assumptions made in developing these systems implicitly or explicitly embed germane enterprise aspects. The natural next question is, <sup>b</sup>Why do we need a representation of organizational context (i.e., an enterprise model) that is independent of our decision support environments?<sup>Q</sup> One reason is to provide a foundation for realizing the current conceptualization of the <sup>b</sup>smart organization<sup>Q</sup> or the <sup>b</sup>networked organization.<sup>Q</sup> Other reasons include:

1. If there are independent enterprise models, then each and every decision support environment will not have to have those models (or some subset) embedded at creation (i.e., one can achieve a type of enterprise model and decision support environment <sup>b</sup>independence<sup>Q</sup>),

2. Organizations might not be as constrained by their existing business models or, for example, by the addition of new strategic partners, since changes to an enterprise model could be communicated to relevant decision support environments (e.g., via mappings through a series of layers with standardized between-layer transformations) as opposed to requiring extensive redevelopment or revision to those environments,

3. Changing decision support service providers would be less consequential and costly assuming competing alternative applications could be self-configured (i.e., providing opportunities to minimize vendor lock-in, as well as to minimize the time and cost to upgrade applications to make use of emerging technologies),

4. The collection of enterprise models can serve as a repository that can be accessed, either through decision maker directed or automated processes embedded in decision support environments,

5. Conflicts and inconsistencies in underlying conceptualizations of <sup>b</sup>local<sup>Q</sup> enterprise models that are embedded in decision support environments dispersed throughout organizations can be identified and clarified in more <sup>b</sup>global<sup>Q</sup> enterprise models, and

6. The collection of enterprise models can be managed as organizational assets thereby providing an impetus for ownership, security, versioning, change management and other model management facilities.

In addition to these reasons, the objectives of enterprise modeling include analysis made possible through automated scrutiny and evaluation of relevant enterprise representations. Demonstrative efforts in this area include using enterprise models as a reference point for automating ISO 9000 compliance evaluation [23]. EM has been related to activity-based costing methodologies—with reference to Sarbanes–Oxley Act compliance [40]. In fact, the actor dependency EM approach of [47] may well provide the richness in representation needed to track decision making controls to aid Sarbanes– Oxley Section 404 compliance examinations. It is important to note that at the heart of many existing EM efforts, including the UEML initiative, is ontological analysis. Ontology has similarly found its way to enterprise architecture design and development where concepts and methods have a signifi cant overlap with the objectives of EM (e.g., [8]). Recently, the European Commission sponsored Network of Excellence–InterOP–was launched [21]. InterOP is taking a multidisciplinary approach to shaping European research activities on interoperability for enterprise applications and software by merging three research areas:

1. Architectures and platforms to provide implementation frameworks,

2. EM to define interoperability requirements and to support solution implementation, and

3. Ontology to identify interoperability semantics in the enterprise.

The merging of these areas recognizes that ontology is playing an increasing role in current research closely related to EM. For example, Geerts and McCarthy [19] utilize an ontological analysis to evaluate the completeness of the extended REA enterprise information architecture. Decision support researchers and others have recently emphasized the natural synergies between knowledge management aspects of ontology and enterprise environments/ modeling [9,20]. Historically, decision support researchers have advanced the notion of EM [3], but the sheer enormity of such a modeling endeavor for even a reasonably complex organization appears to have precluded its advancement. So what is different now? New research can begin with the assumption of an intermediary language, the UEML, currently advancing from version 1.0 to

2.0 [50]. Fig. 1 shows the core constructs of UEML (adapted from [43]).

As an exemplar of the potential for the UEML approach, model-driven architecture (MDA) proponents have hailed the unified modeling language, the meta-object facility, the XML meta-data interchange, and the common warehouse meta-model as a set of inter-related standards for separating the business logic from implementation-specific aspects. In short, MDA strives to separate the definition of business logic from the implementation of that logic. A platform-independent model (PIM) represents the business logic, and the platform-specific model (PSM) translates the PIM to languages, operating systems, etc. The PIM and the PSM must be composed of well-defined languages to enable automated conversion from either direction. In analogy, a decision support environment can become an EM-independent model, while the UEML representations used by the environment can be considered as transformations to and from proprietary EM toolsets (akin to [38]).

It should be noted that in the above discussions we have adopted the phrase decision support environment (DSE) as a generalization of next generation decision support. This generalization is similar to that proposed in the work systems approach of [1]. Our focus is not limited to the notion of system or artifact, rather we mean to be inclusive of all organizational assets, including people and processes involved in taking those actions that cause a change in an organization’s state of affairs. Our discussion emphasizes models, whether they are embedded in individual’s minds or incorporated into a spreadsheet, they are models of business processes, models of financial performance, etc. A DSE is therefore the complete context of the systems, people and processes engaged in activities impacting an organization’s state of affairs. In addition, a DSE can be inter-organizational in the sense that it becomes a context for jointly supporting participating systems, people and processes engaged in virtual interwork.

## 3. UEML: a new foundation for EMM

In addition to supporting application integration, UEML seeks to become a common language that will increase individual EM toolset integration possibilities in a way that is anticipated to be somewhat similar to the MDA vision. This implies that while one toolset may be best suited to modeling a subset of an enterprise, another toolset might best be used to model another subset. Yet both toolsets should be capable of generating a UEML representation that can, in theory, be merged, integrated, composed or otherwise operated upon to provide a larger subset of an enterprise model, thereby providing what we refer to as a composed EM view of the enterprise that can be exposed in a DSE. A similar model composition operation has been recently studied in a decision support context [10].

![](/api/attachments/NGB8CEES/fulltext/images/2409f2c18eefef441ebfe4f920033276a38abf69d789d2bdfe5eeea6b6cbbb81.jpg)  
Fig. 1. UEML core constructs (adapted from Vernadat [43]).

The need for formalisms for UEML transformations is paramount. Transformations from EM toolsets to UEML, the composition of UEML representations from multiple toolsets, and the transformation of one ontology on which a toolset is based to another ontology, are all examples of the areas where formal methods can provide significant insight. Further, the meta-modeling possibilities implied by the existence of multiple, potentially overlapping model subsets could give rise to entirely new toolsets. The design science methodology has been successfully utilized in decision support research, and it certainly fits this emerging context. There may be a hierarchy of languages that can transparently translate from a decision maker’s visual modeling environment to multiple toolsets, and then back again. This type of middleware capability appears to support the middle-out and prototyping decision support system methodologies and lifecycles while concomitantly providing insulation against perturbations of lower level changes to higher level decision maker interfaces.

The traditional decision support modeling toolsets could potentially derive significant benefit from interpreting/exploiting enterprise models. UEML representations that are output from one model in stance can become input to another model instance, and the enterprise model could provide impetus to more sophisticated interfaces used in customizing that process using UEML-derived domain knowledge to guide interface discourse. In addition, UEML elements could help to provide linkages between models and data. Data almost certainly exists throughout the organization, and the UEML representations may play an important role in active data warehouses.

In summary, the EMM research agenda we propose assumes the successful evolution of the UEML initiative as per the following:

Assumption 1. There will remain heterogeneous domain-oriented EM toolsets that create models in unique and perhaps proprietary internal representations that can be filtered, manipulated and otherwise operated on in transformations to UEML representations—without a loss of model integrity.

This assumption implies a future based on a federated approach to organizational EM toolsets where particular EM tools, designed for application in specific domains, will be predominant. What is currently not well understood is the concept of model integrity in this context. We borrow from the OMG’s <sup>b</sup>Common Warehouse Metamodel<sup>Q</sup> the concepts of black and white box transformations [12]. A black box transformation is where the details of the transformation processes are hidden (as in the translation of a proprietary internal EM representation to a UEML representation). In contrast, a white box transformation can be expressed in any suitable language thereby exposing, at a fine level of detail, all operations involved in that transformation. In a white box transformation the inputs, the transformation engine, and the resulting target UEML representation(s) can be verified for consistency, validity and expressive equivalence through appropriate testing of pre- and post-conditions and through other tests deemed suitable to the particular EM toolset context, i.e., domainspecific integrity tests.

## 3.1. A UEML maturity assumption

Given Assumption 1, the targeted problem sets for EMM approaches based on UEML will be in the area of interoperability. Members of the IDEAS thematic network who developed a recommendation for the European Commission on UEML and the interoperability of enterprise software tagged it <sup>b</sup>plug, play and do-business.<sup>Q</sup> The main focus is on the ability to support inter-organizational linkages using self-managing systems and processes at a variety of levels, especially at levels higher than those traditionally supported through standards designed to support basic transactions. For example, members envision solutions for inter-enterprise coordination, business process integration, semantic and contextual application integration, syntactical and behavioral application integration as well as physical connectivity integration [28]. There are several underlying assumptions relevant to this vision.

First, there is an issue regarding the acceptance of the UEML approach by EM toolset vendors, business and government organizations and researchers. The roadmaps adopted by the IDEAS thematic network are a move in that direction, but the effort is limited in scope to those partners. Table 1 summarizes the progress of the network to date.

Current state of deliverables from the thematic network project (IST–2001–34229) financed by the European Union from (http:// www.ideas-roadmap.net/webpage/Phps/scheme.php or www.ueml. org, 2004)

<table><tr><td>Deliverable No</td><td>Deliverable title</td></tr><tr><td>D1.1</td><td>Report on the State of the Art in Enterprise Modeling</td></tr><tr><td>D1.2</td><td>The User Requirements</td></tr><tr><td>D2.1</td><td>The Goals and the Challenges of the Industry for the 21st Century (1st version)</td></tr><tr><td>D2.2</td><td>The Vision for 2010 (1st version)</td></tr><tr><td>D2.3</td><td>The Goals, Challenges and Vision (2nd version)</td></tr><tr><td>D2.4</td><td>The Vision for 2010 (2nd version)</td></tr><tr><td>D3.1</td><td>A Gap Analysis (first version including choice of the methodology)</td></tr><tr><td>D3.2</td><td>Required Activities in Research, Technology and Standardization to Close the RTS Gap (first version)</td></tr><tr><td>D3.3</td><td>Roadmaps and Recommendations on RTS Activities (first version)</td></tr><tr><td>D3.4</td><td>A Gap Analysis (second version)</td></tr><tr><td>D3.5</td><td>Required Activities in Research, Technology and Standardization to Close the RTS Gap (second version)</td></tr><tr><td>D3.6</td><td>Roadmaps and Recommendations on RTS Activities (second version)</td></tr><tr><td>D4.1</td><td>The Action Plan for Future Research Activity in the Scientific Focus Areas Including Priorities and Schedule</td></tr><tr><td>D4.2</td><td>Project Management Plan for Large Projects and Networks</td></tr><tr><td>D5.1</td><td>Taxonomy and Glossary for Interoperability—proposal draft (3 months) Public</td></tr><tr><td>D5.2</td><td>Taxonomy and Glossary for Interoperability</td></tr><tr><td>D6.1</td><td>Reports on Dissemination (1st report)</td></tr><tr><td>D6.2</td><td>Reports on Dissemination (2nd report)</td></tr><tr><td>D7.1</td><td>Management and Progress Report (1st version)</td></tr><tr><td>D7.2</td><td>Management and Progress Report (2nd version)</td></tr></table>

Second, when accepted, there will need to be significant research studies, practical implementations and information sharing to validate the approaches, as documented in [34]. Thematic network members have envisioned patterns of implementation and the actors and stakeholders whose perceptions are deemed important to those patterns as well as a preliminary set of activities to validate and evaluate progress [34]. For purposes of extending a next generation decision support agenda, it is plausible to state the following assumption with respect to anticipated progress on the thematic network’s activities:

Assumption 2. UEML-based modeling approaches, processes and systems capable of the self-management of interoperability between heterogeneous, diverse and autonomous enterprises at levels of abstraction higher than at the transaction-oriented level will be shown to be feasible. Demonstrative implementations will emerge that enable partnering at the levels of cooperation, collaboration and interwork.

Current decision support research offers important implications and preliminary validation for this assumption. For example, Liu and Shen [29] recently addressed a process-view model for enterprise interoperability that provides another perspective beyond traditional activity-based modeling approaches. Considering that EM toolsets might support each view independently, that UEML should provide a common ground representation, and that organizations engaged in a cross-enterprise workflow will need to focus on the management of external exposure to their business processes, this research demonstrates the important relationships between the thematic network’s agenda and the next generation decision support agenda. With respect to the notion of interwork, there is a striking overlap with prospects for next generation decision support. For example, the specific enterprise modeling vision stated by the thematic network is:

Enterprise modeling [will] enable cross-enterprise teams to perform dependency and performance analysis, to develop consistent, complete and compliant enterprise knowledge architectures to support generation of simple workplaces as well as elaborate design environments. The power of enterprise visual scenes will augment human capacities for design, problem solving and learning! [28, p.15]

## 3.2. The UEML-based meta-modeling assumption

Assumption 2 suggests that a next consideration for EMM involves the operations, manipulations and theoretical underpinnings of meta-modeling constructs and rules that can be sufficiently generalized for interorganizational contexts. These constructs and rules will serve as a set of building blocks that can be used to integrate, derive, transform and otherwise manipulate models in the UEML domain. Petit [33] has suggested an analogy between UEML-based meta-modeling and the database integration problem. Others view EM integration as a pattern-driven endeavor [26]. In addition, recent research efforts have targeted meta-modeling approaches with the following vision:

The goal of model management is to develop a generic infrastructure that offers an order-of-magnitude productivity improvement to builders of model-driven applications, such as database tools, application design tools, message translators, and customizable commercial applications. Today’s model-driven applications include much object-at-a-time programming on relational schemas, DTDs, web-site structures, E/R diagrams, UML models, etc. The main ideas behind model management are that: 1) such object-at-a-time programming can be abstracted as high-level operations on models (i.e., schemas) and 2) mappings between models, and these operations can be made independent of the data model and application of interest, that is, generic. [5]

Bernstein and his colleagues’ efforts in the area are likely to be a source of reference for UEML-based meta-modeling (e.g., [6,7,30,31,36,37]). However, it is interesting to note that many approaches to model management were initiated by the decision support community some time ago and have been extended/ updated (e.g., [2,13,18,24]). We presume continued progress in this area will be forthcoming as stated in the following:

Assumption 3. Well-formed UEML representations will facilitate the theoretical and applied feasibility of model management constructs including, but not limited to, inverse, match (or composition/integration), difference, function application, selection and instantiation.

The constructs listed in Assumption 3 are drawn from [7], although their focus was not on the implementation of those constructs. We offer this lack of implementation experience as a caveat to Assumption 3. There is one additional caveat. The constructs listed in Assumption 3 have a clear role in the context of operations on UEML representations, but not necessarily in ontology-to-ontology, UEML representationto-ontology, and ontology-to-UEML representation transformations and manipulations. Ontology-to-ontology mappings are tedious, error-prone and nearly impossible without knowing the semantic mappings between their constituent elements [14,35]. The reason this is significant in the EMM area is that different EM toolsets are designed and based on different ontologies. It may be desirable to define mappings between ontologies since those mappings may provide more complex operators than those envisioned in current model management perspectives, and those mappings may be very useful, particularly in the context of the <sup>b</sup>match<sup>Q</sup> function that would serve to integrate or compose two or more UEML representations. Even with these caveats, there is ample evidence emerging of the validity of Assumption 3 (e.g., [25,26]).

## 4. Example scenarios

To illustrate the ideas discussed so far, we present two scenarios. First, suppose there are two hospitals representing two distinct organizations located in two non-adjacent geographical areas. In the course of an operation at one of the hospitals (A) a rare circumstance arises requiring the expertise of specialists located at the second hospital (B). A DSE configured for this inter-organizational situation could require rapidly linking the models, processes, people, machines and systems in A and B. It may be that A does not possess the models necessary to examine the blood test results to verify the severity of the rare circumstance. It would follow that A would not likely have set forth the appropriate policies or processes for dealing with those circumstances. It also may be that specific diagnostic machines are not available at A,

but at B they can be configured to accept data from A to provide diagnostic results. It is also likely the case that A has set policies for sharing data with hospitals that are a part of another organization. We could consider then that A needs to restrict the type of data that can be shared, configure the appropriate application to prepare that data for sharing and open a port with appropriate security configuration to communicate with B. Similarly, if there is real-time video linkage available (as in the case of this rare situation arising during a surgery), then A would need to configure that linkage in a manner consistent with a standard that is compatible with B’s real-time video capabilities. The resulting DSE could be something akin to conducting joint surgery, with experts at B using information from B’s decision tools that is derived through analysis of data ported from A. Whether the outputs of the decision tools at B would be available to the people at A would be decided through the process mapping, and perhaps by the people located at A.

If we consider the above scenario in terms of the core UEML constructs of Fig. 1, we can see how the representations of people, processes, enterprise objects (including machines, people and data porting applications) can be addressed. Process aspects can be represented in the constructs as well. It follows that A and B could rely on different enterprise modeling tools that translate to the UEML standard, and when the scenario above arises, a subset of the UEML representation would be brought to bear in configuring a DSE. For example, since A will not expose some patient data, that aspect of the UEML representation would be removed before being integrated, composed or <sup>b</sup>matched<sup>Q</sup> with a similarly configured UEML representation from B. B’s UEML representations may not expose all of the specific decision tools in the DSE, in which case B’s UEML representation would be manipulated accordingly using relevant model management operators. The matching of A’s and B’s UEML representations should give rise to configuration of the DSE. This configuration needs to be done efficiently and effectively in order to support the timeliness and significance of the decision context. Assumption 1 is illustrated through the independent transformation of enterprise models to a UEML representation. Assumption 2 is illustrated through a restriction of the UEML constructs to a fundamental level. An example could be the ability to describe the previous situation such that the decision tool outputs might be shared between A and B. Assumption 3 is more rigorous in that the model management operations required to prepare A’s and B’s UEML representations for the subsequent application of the match function are somewhat fuzzy given the caveats identified, but the relevance of the indicated model management <sup>b</sup>match<sup>Q</sup> operator is clearly demonstrated.

![](/api/attachments/NGB8CEES/fulltext/images/020c3cd928983748daef8b9b334fe2d7685ca7342cbdff9e60c8234074720d9f.jpg)  
Fig. 2. Intra- and inter-organizational heterogeneous decision models.

The above DSE scenario is fairly fundamental from an enterprise model management perspective because it assumes operations on UEML representations at A and B culminating in their match; the result of which is presumed to be used in configuration of the interorganizational DSE intended to support collaboration and interwork. More complex enterprise model management scenarios are likely relevant in other circumstances. In this next scenario, we examine one approach to a classic book ordering situation in which a professor is responsible for making an estimate of course enrollment for a particular semester, and the bookstore is responsible for ordering the books for the course as well as all other courses at the University. The professor might determine the number of students expected based on cohort enrollment in a recently completed prerequisite along with other pertinent historical data. The bookstore must consider an estimate of the used book buy-back (assuming it is not a new book order), perhaps the prior estimating behavior of the professor and maybe even the anticipated book sales by other bookstores. An enterprise model management perspective to create a DSE for this context may well discover that because of some previous higher-than-normal estimates of enrollment by the professor, that the bookstore has included in its decision tool the automatic reduction of

![](/api/attachments/NGB8CEES/fulltext/images/4843f09b9f38b7eac3068e03ff53a210229fbd3dffc6ca749a82b6b2be9d901f.jpg)  
Fig. 3. High-level sample model of a UEML-based representation (professor request for books).

any order provided by that professor (e.g., through a cell entry in a spreadsheet). In addition, by matching the UEML representations of the two intra-organizational entities, it may be possible to discover that there is no process linkage whereby feedback is provided to the professor of the actual number of books placed on order by the bookstore. This scenario is shown in Fig. 2 where enterprise modeling tools might be used to represent the professor’s and the bookstore’s processes and decision models. A match operator applied to the two representations may well need to provide a deeper analysis than discussed in the first scenario in order to unveil the reduction factor embedded in the bookstore’s spreadsheet decision tool.

We can further complicate the scenario by including the publisher entity as shown in Fig. 2 and the

![](/api/attachments/NGB8CEES/fulltext/images/c0296c04de2bfdf325fb796a900fb38a1723ca65db7e34d856642e8996863648.jpg)  
Fig. 4. Where does the business model fit in the system architecture within an organization?

high-level sample UEML representation of the professor in Fig. 3. Here we assume the publisher is a distinct entity, so the scenario now reflects both interand intra-organizational contexts. Once again, the publisher’s decision model may include a reduction factor that reflects historical book returns based on over-ordering. However, this factor is based on analysis derived from aggregated data from multiple bookstore orders. In the case of a University deciding it has major problems with a publisher because of repeated textbook availability shortages, it may be necessary to construct a DSE that supports a temporary strategic alliance to address the problem. Note that such a DSE could be constructed using a variety of enterprise model management constructs. For example, a subset of the professor’s UEML representation (Fig. 3) may be matched with a subset of the publisher’s UEML representation, a subset of a matched professor’s and bookstore’s UEML representations may be matched with a subset of the publisher’s UEML representation, and so on. This scenario illustrates the complexities associated with Assumption 3, above, and it serves to demonstrate the possible strategic significance associated with configuring DSEs to support specific types of organizational alliances—including the importance of making decisions about the organizational level at which such alliances might be undertaken.

![](/api/attachments/NGB8CEES/fulltext/images/4e65310f458a43ea3b03601140252d4a540bff4a19bcd581996417206c564690.jpg)  
Fig. 5. Inter-organizational DSE inherits exposed UEML from partnering organizations.

Given these scenarios, it is now possible to discuss abstractions of the ideas discussed thus far. First, we can generalize UEML representations and the operators on those representations as <sup>b</sup>the new DSE middleware.<sup>Q</sup> By using the term middleware, we imply that these representations will be used in configuring a DSE. Note that we assume operations on UEML representations generate UEML representations, i.e., the operations are closed on UEML representations. Further, we assume that UEML representations can be used in MDA, particularly in the PIM. Note that this latter use of UEML representations appears to be a predominant focus of the InterOP Network of Excellence. Our view of the resulting architecture–for a single organization–is shown in Fig. 4. The rectangles labeled <sup>b</sup>EM-#<sup>Q</sup> represent enterprise models generated from proprietary toolsets, with their associated UEML representations shown as a reduced diagram of the core constructs of UEML as in Fig. 1. Note that a DSE may be configured from one or more UEML representations at the DSE middleware layer.

![](/api/attachments/NGB8CEES/fulltext/images/acf70916a97960c89f7b87395ef248fced6af667f74c11766ade065ea991d29e.jpg)  
Fig. 6. Sample enterprise model management operators.

Fig. 5 extends this abstracted perspective to interorganization DSEs. Here, an inter-organizational DSE is shown as configurable from UEML representations that are opted to be exposed by partnering organizations. Please note that the diagram does not depict that UEML representations from different organizational levels might be exposed and matched to enable configuration of a DSE in accordance with the strategic nature of a particular alliance. Fig. 6 depicts several enterprise model management operators at a high level of abstraction. Here we use the term <sup>b</sup>instantiate<sup>Q</sup> <sup>Q</sup> to infer the configuration of a DSE from a UEML representation. We also imply that as part of this instantiation process, the DSE inherits capabilities and properties from the underlying UEML representation. Finally, Fig. 6 shows how a derived UEML representation can become a part of an organization’s repository of UEML representations as akin to an algebra with variable assignment and memory.

## 5. Papers in this special issue and research propositions

Enabling integrated decision support is essential to coordinate the organizational and inter-organizational activities that current business practices demand. Using the lens of enterprise model management supports the view necessary for such integration. Enterprise modeling toolsets are becoming increasingly user-friendly. We anticipate these toolsets to follow a market-driven path with those tools most suited to a particular task, organizational context or class of users, etc., becoming increasingly commoditized. Toolsets requiring specialist interaction will be too labor intensive and therefore too costly. For example, as the market for EM toolsets evolves, those remaining after a shakeout may be too difficult for practitioners to use, which would result in a likely failure of the EMM research agenda. In addition, there is need for research to assess the usability of EM toolsets and to assess their diffusion.

Considerable research is needed in the different aspects of integrated decision support. In synthesizing the papers in this special issue, one is struck by the unilateral requirement that the tools used to support inter-organizational decision making must be available to the decision makers themselves. This, with the assumptions and scenarios discussed above, leads to the following research proposition:

Proposition 1. UEML representations can be maintained by business people, where maintenance implies the ability to create, personalize, enhance and evolve representations without requiring modeling specialist interaction.

This very rich and broad proposition can be tackled from several different directions. The papers in this special issue highlight a few of those possible directions.

## 5.1. Collaboration

Integrating across organizations will magnify collaboration challenges. One aspect of this is presented in <sup>b</sup>Model-Driven DSS: Concepts and Research Directions,<sup>Q</sup> by Daniel J. Power and Ramesh Sharda. They address the model-based research stream in decision support and recommend a much broader research agenda for the future than model-based research has previously taken. As they state in their conclusion:

Collaborative building of model-driven DSS and collaborative use of model-driven DSS are both interesting areas for further research. The <sup>d</sup>how<sup>T</sup> of supporting collaboration may be the same or it may differ in these two situations. Besides integrating the use of collaborative technologies such as chat, desktop sharing, whiteboarding, voice exchange, video conferencing, etc. into the model development and use processes, advanced interfaces for simultaneous manipulation of models and results need to be explored.

## 5.2. Architecture

Robb Klashner and Sameh Sabat echo Power and Sharda’s call for broader approaches to modeling while specifically discussing advancements in infrastructure including platforms and architectures. <sup>b</sup>A DSS Design Model for Complex Problems: Lessons from a Mission Critical Infrastructure<sup>Q</sup> uses a realworld context for validating a DSS design model. They state:

The DSS Design Model is validated using a tool instantiation, microgrid mini-case, and current research of a KMDSS for telecommunications. Main findings suggest that broader and more integrated approaches are necessary to design DSS for complex domains. . . DSS research can benefit from the progress in Software Architecture research. . . .a more comprehensive <sup>d</sup>Systems<sup>T</sup> design approach is needed to address the nondeterministic complexities arising from today’s real-world decision making-requirements.

## 5.3. Data and process support

Salvatore T. March and Alan R. Hevner raise the current limitations of data warehouses to support inter-organizational decision making in their paper, <sup>b</sup>Integrated Decision Support Systems: A Data Warehousing Perspective.<sup>Q</sup>

Clearly the data warehouse must go beyond its current role as a repository of historical data describing the operations and transactions in which the organization has engaged. It must include data describing partners and partnerships, policies and rules of the business, competitors and markets, goals and standards, opportunities and problems, successes and failures, and alternatives and predicted futures.

As March and Hevner point out: <sup>b</sup>methodologies and representational formalisms for this level of analysis are sorely lacking.<sup>Q</sup> Again arguing for tools that can be used by the decision makers, they go on to say <sup>b</sup>effective integration decisions can only be made by those thoroughly familiar with the domain ontologies both internal and external to the business system.<sup>Q</sup>

In <sup>b</sup>A Business Process Context for Knowledge Management,<sup>Q</sup> T.S. Raghu and Ajay Vinze consider next generation decision support from a knowledge management perspective. They emphasize the importance of linking business process contexts to the knowledge needed to support those processes. Their findings are supported through experiential case studies. An important insight they have regarding innovation is central to the issue of sustained competitive advantage through next generation decision support as articulated in the following:

[Business] processes emphasizing autonomous decision making structures present the most conducive process environment for knowledge synthesis as they are inherently designed to allow innovations in procedures and business rules. KM efforts in such processes would have the most impact in enabling knowledge synthesis through effective sharing, storage and retrieval practices. . . The traditional view of knowledge as data and information fails to incorporate process and associated assumptions thus causing loss of context for the knowledge that is stored. . .

Kannan Mohan and Balasubramaniam Ramesh develop a prototype that addresses the challenge that results when knowledge integration is necessary. Using traceability, their approach provides new research directions for synthesizing DSS research. The comprehensive insights they have are represented in the following statements from their paper, titled <sup>b</sup>Traceability-Based Knowledge Integration in Group Decision and Negotiation Activities.<sup>Q</sup>

A traceability approach that integrates knowledge that is distributed and fragmented across different artifacts, stakeholders, and phases of the. . . lifecycle, addresses key challenges in knowledge integration. . . Our prototype system supports knowledge sharing, flexible definition of knowledge schema, acquisition and integration of knowledge in a visual, network form, consistency maintenance, and seamless integration with commonly used work process and productivity tools. . .

## 5.4. Development time

In a world with almost instantaneous communication possibilities, users cannot wait weeks or even days for the necessary support to be assembled. The need for rapid configuration of DSEs enables exposure of only the necessary data, processes, knowledge and tools for an inter-organizational collaboration is forcefully demonstrated in, <sup>b</sup>Decision Support for Improvisation in Response to Extreme Events: Learning from the Response to the 2001 World Trade Center Attack<sup>Q</sup> by David Mendonc¸a. He says:

. . .multiple decision makers (e.g., representatives of impacted or responding organizations) may compete or negotiate while responding to the event. It may therefore be advisable to consider how decision support systems can support the management of proprietary information and shared resources. As a participant in improvisation, then, the model should provide guidance that is informed both by knowledge of the event and of the intentions of the organization.

## 5.5. Behavioral

DSEs will provide users with access to an everexpanding universe of applications including those emerging in the spatial DSS area. In <sup>b</sup>Exploring the Influence of Perceptual Factors in the Success of Web-based Spatial DSS,<sup>Q</sup> Suprasith Jarupathirun and Fatemeh <sup>b</sup>Mariam<sup>Q</sup> Zahedi provide insights into the need for interface characteristics reflecting the background and knowledge of intended users. This need is exacerbated as inter-organizational DSE participants will likely be multi-disciplinary, familiar with some decision tools but not others, and as participants opt in and out of a decision process, there will likely be frequent changes to familiarity levels. This is reflected in their statement as follows:

A major source of online support for Spatial DSS users could be an intelligent interface guiding decision makers in using SDSS. For example, integrating intelligent agents with SDSS makes it possible to provide help for novice SDSS users in selecting and using the appropriate SDSS functionalities. The extent of help could subside as decision makers attain mastery, become more comfortable using the SDSS, and reach a higher level of self-efficacy.

## 5.6. Intelligent agents

Theoretical foundations for next generation decision support such as those required to advance our understanding of inter-organizational DSE design requirements may well come from controlled studies of computer-based multi-agent coordination. In addition, it is likely that multiple intelligent agents will be important participants in the decision processes supported by such DSEs. Parag C. Pendharker’s paper, titled <sup>b</sup>The Theory and Experiments of Designing Cooperative Intelligent Systems,<sup>Q</sup> addresses this arena with findings suggestive of a long-term research stream to identify prescriptive agent coordination approaches. Following is a statement reflective of the research stream represented by this paper:

. . .in the current research, a <sup>d</sup>prescriptive,<sup>T</sup> rather than a <sup>d</sup>descriptive,<sup>T</sup> approach to multi-agent coordination was used. Some of the avenues for the extension of the current coordination scheme are: 1) redesign the coordination scheme that penalizes a coordinating agent for <sup>d</sup>cheating,<sup>T</sup> and 2) develop a set of norms regulating the coordination between agents in a way that is beneficial for the whole group and not for any agent in particular.

The EMM research agenda will lack significance if it does not provide organizations with measurable strategic advantage. Our belief is that the abilityto design and construct DSEs to enable collaborations, both internally and with organizational partners, represents one of the most significant organizational capabilities in need of a major research thrust.

## 6. Conclusion

Speaking of conceptual modeling in information systems research, Wand and Weber [45] addressed the fundamental question, <sup>b</sup>How can we model the world to better facilitate our developing, implementing, using and maintaining more valuable information systems<sup>Q</sup> [2002]. Research in enterprise model management extends that question to a somewhat different and more specific question, <sup>b</sup>How can enterprise modeling standards (like UEML) be leveraged through meta-modeling constructs in an EMM research agenda targeted to intra- and inter-organizational DSE configuration and instantiation intended to support interwork in a manner that creates sustainable competitive advantage?<sup>Q</sup> The papers in this special issue demonstrate the breadth of approaches to this question.

While business people are posited to be able to maintain UEML representations through EM toolsets, there is a need for more complex training for individuals capable of manipulating UEML representations using operators that have been discussed earlier. This <sup>b</sup>meta-modeling<sup>Q</sup> required to instantiate DSEs, particularly in the context of inter-organizational alliance support, will likely require the role of EMM specialist. The notion of DSE middleware implies the need for those knowledgeable enough to map that middleware to lower layers, particularly in the MDA context. In addition, business knowledge is required to understand both the representations being manipulated and the strategic alliance objectives desired by the highest level managers of the enterprise. There are also likely time pressures on instantiating DSEs as demonstrated in the hospital scenario. There is a need to maintain a repository of DSE instantiations to track their progress and to update/discontinue their connections when a collaboration is revised while underway or it is completed. This repository will also be useful for instantiating new DSEs with properties similar to the one that has been previously instantiated. For example, in the University/Publisher scenario, there would likely be similar instantiations of inter-organizational DSEs with multiple publishers and perhaps even book brokers. The role of meta-modeling and the need for new EMM specialists are addressed in the following proposition:

Proposition 2. The role of meta-modeling and associated constructs for manipulating, abstracting, configuring, synthesizing and instantiating UEML representations into DSEs will become the new agenda for Enterprise Model Management research—and it will provide the foundation for creating the need for the EMM specialist charge with the role of DSE instantiation.

Historical research on achieving competitive advantage through inter-organizational systems stems from comparative efficiency and bargaining power (e.g., [4,22]). Inter-organizational DSEs may well fit neatly into earlier typologies, for example, those of [27]. However, the ability to rapidly configure appropriate DSEs may well provide the <sup>b</sup>alertness<sup>Q</sup> and <sup>b</sup>responsiveness<sup>Q</sup> addressed by Zaheer and Zaheer [49] in the context of global electronic networks. This latter lens is central to current <sup>b</sup>decisions that matter.<sup>Q</sup> DSEs that enable organizations to <sup>b</sup>catch the wave<sup>Q</sup> through alertness and responsiveness are the EMM capabilities that can create sustainable competitive advantage. Alertness in this case is the facilitation of cross-organization innovation that can be achieved by configuring and instantiating coordination-directed DSEs. And responsiveness is the ability to configure and instantiate interwork DSEs that can enable organizations to act on those innovations. Both alertness and responsiveness require speed, but at a reasonable cost. This leads to our third research proposition:

Proposition 3. The <sup>b</sup>decisions that matter<sup>Q</sup> will increasingly require DSEs that can be rapidly configured, protect and expose the right data, knowledge, decision tools and visualizations to support virtual interwork, and that can be seamlessly synthesized with partnering organization DSEs similarly configured and likewise based on a standard like UEML.

Rapid configuration and instantiation of DSEs through efficient UEML-based meta-modeling constructs are imperative to achieving both timeliness and cost-effective enterprise model management solutions. However, much more research, both theoretical and applied, is necessary. We hope that what we have discussed and the insights our colleagues have presented in their papers for this special issue will together contribute to a lively debate both within and outside of our SIG DSS community as we search for research synergies in our previously somewhat dispersed and disjointed field of study.

## Acknowledgements

The authors wish to acknowledge the participants of the 2nd Annual Pre-ICIS SIG DSS Workshop for their comments and suggestions regarding the concepts and research directions we discuss here. In addition, we especially thank, on behalf of the entire membership of SIG DSS, Professor Andy Whinston for providing us with an opportunity to publish an inaugural special issue.

## References

[1] S. Alter, A work system view of DSS in its fourth decade, Decision Support Systems 38 (3) (2004) 319–327.

[2] B. Applegate, R. Konsynski, J.F. Nunamaker, Model management systems: design for decision support, Decision Support Systems 2 (1) (1986) 81– 91.

[3] S. Ba, A.B. Whinston, K.R. Lang, An enterprise modeling approach to organization decision support, Proceedings of the 28th International Conference on System Sciences, 1995, pp. 312– 320.

[4] J.Y. Bakos, M.E. Treacy, Information technology and corporate strategy: a research perspective, MIS Quarterly 10 (2) (1986) 107–119.

[5] P.A. Bernstein, Applying model management to classical meta data problems, Proceedings CIDR, 2003, pp. 209– 220.

[6] P.A. Bernstein, E. Rahm, Data warehouse scenarios for model management, ER 2000 Conference Proceedings, 2000, pp. 1 – 15.

[7] P.A. Bernstein, A. Levy, R.A. Pottinger, A Vision for Management of Complex Models, Microsoft Technical Report MSR-TR-2000-53, http://www.research.microsoft.com (2000) 1–17.

[8] K. Beznosov, Architecture of Information Enterprises: Problems and Perspectives, Center for Advanced Distributed Systems Engineering (CADSE), Florida International University, Miami, Technical Report #2000-06 (2000) 1–15.

[9] N. Bolloju, M. Khalifa, E. Turban, Integrating knowledge management into enterprise environments for next generation decision support, Decision Support Systems 33 (2002) 163– 176.

[10] K. Chari, Model composition in a distributed environment, Decision Support Systems 35 (2003) 399–413.

[11] N. Dalal, M. Kolarik, E. Silvaraman, Toward an integrated framework for modeling enterprise processes, Communications of the ACM 47 (3) (2004) 83– 87.

[12] Data Warehousing, CWM and MOF Resource Page, http:// www.omg.org/cwm (2004).

[13] D. Delen, P. Benjamin, M. Erraguntla, Integrated modeling and analysis generator environment (IMAGE): a decision support tool, Proceedings of the 1998 Winter Simulation Conference, 1998, pp. 1401–1408.

[14] A. Doan, J. Madhavan, P. Domingos, A. Halevy, Learning to map between ontologies on the semantic web, Eleventh International WWW Conference, Hawaii, US2002, (http://citeseer. ist.psu.edu/doan02learning.html).

[15] M.S. Fox, M. Gruninger, Ontologies for enterprise integration, Second Conference on Cooperative Information Systems, 1994, pp. 1 – 8.

[16] M.S. Fox, M. Gruninger, Enterprise modeling, AI Magazine (1998 (Fall)) 109–121.

[17] M.S. Fox, M. Barbuceanu, M. Gruninger, J. Lin, An organisation ontology for enterprise modelling, in: M. Prietula, K. Carley, L. Gasser (Eds.), Simulating Organizations: Computational Models of Institutions and Groups, AAAI/MIT Press, Menlo Park, CA, 1998, pp. 131–152.

[18] U. Frank, Multi-Perspective Enterprise Modeling (MEMO)— conceptual framework and modeling languages, Proceedings of the 35th International Conference on System Sciences, 2002, pp. 1 – 10.

[19] G. Geerts, W. McCarthy, An Ontological Analysis of the Primitives of the Extended-REA Enterprise Information Architecture, International Journal of Accounting Information Systems, forthcoming.

[20] H.T. Goranson, Ed., A Merged Future for Knowledge Management and Enterprise Modeling, CIMOSA Working Paper, http://www.cimosa.de/EI3-IC/WS1WG1V3.htm (2004).

[21] InterOP: Interoperability Research for Networked Enterprises Applications and Software 1 (Spring 2004) http://www. interop-noe.org/.

[22] H.R. Johnston, M.R. Vitale, Creating competitive advantage with inter-organizational information systems, MIS Quarterly 12 (2) (1988) 153 – 165.

[23] H.M. Kim, M.S. Fox, Using enterprise reference models for automated ISO 9000 compliance evaluation, Proceedings of the 35th International Conference on Systems Science, 2002, pp. 1– 10.

[24] R. Krishnan, K. Chari, Model management: survey, future research directions and a bibliography, Interactive Transactions of OR/MS 3 (1) (2000).

[25] J. Krogstie, H.D. Jorgensen, Interactive models for supporting networked organizations, 16th International Conference CAiSE, 2005, pp. 550– 563.

[26] K. Kuhn, F. Bayer, S. Junginger, D. Karagiannis, Enterprise model integration, in: K. Bauknecht, A.M. Tjoa, G. Quirchmayr (Eds.), Proceedings of the 4th International Conference EC-Web 2003—Dexa, 2003, pp. 379–392.

[27] K. Kumar, H.G. van Dissel, Sustainable collaboration: managing conflict and cooperation in inter-organizational systems, MIS Quarterly 20 (3) (1996) 279– 300.

[28] F. Lillehagen, Ed., D2.2, The Vision for 2010, Thematic Network, Contract No. IST-2001-37368 (2003) http://isg.uninova. pt/pub.ideas/bscw.cgi/0/45163.

[29] D. Liu, M. Shen, Business-to-business workflow interoperation based on process-views, Decision Support Systems 38 (2003) 399– 419.

[30] J. Madhavan, P.A. Bernstein, P. Domingos, A. Halevy, Representing and reasoning about mappings between domain models, Proceedings 2002 AAAI/IAAI, 2002, pp. 1– 7.

[31] S. Melnik, P.A. Bernstein, A. Halevy, E. Rahm, A Semantics for Model Management Operators, Microsoft Technical Report (2004) 1–12.

[32] M. Petit, Ed., D1.1, Report on the State of the Art in Enterprise Modeling, Thematic Network—Contract No. IST-2001-34229 (2002). http://www.rtd.computas.com/websolution/Default. asp?SystemID=4 and FolderID=5&ServiceURL=WebComputas/ ComputasPage.asp?pageID=121&WebID=239.

[33] M. Petit, Some methodological clues for defining a unified enterprise modelling language, International Conference on Enterprise Integration and Modeling Technology (ICEIMT’02), 2002, pp. 359– 369.

[34] M. Petit, Ed., D4.1, The Action Plan for Future Research Activity in the Scientific Focus Area Including Priorities and Schedule, Thematic Network—Contract No. IST-2001-37368 (2003). http://www.rtd.computas.com/websolution/Default. asp?SystemID=4&FolderID=5&ServiceURL=WebComputas ComputasPage.asp?pageID=121&WebID=239.

[35] H.S. Pinto, A. Gomez-Perez, J. Martins, Some issues on ontology integration, Proceedings of the IJCAI-99 Workshop on Ontologies and Problem-Solving Methods (KRR5), vol. 7(1), 1999, pp. 7 – 12.

[36] R.A. Pottinger, P.A. Bernstein, Merging models based on given correspondences, Proceedings of the 29th VLDB Conference, 2003, pp. 1– 12.

[37] E. Rahm, P.A. Bernstein, A survey of approaches to automatic schema matching, The VLDB Journal 10 (2001) 334– 350.

[38] S. Sendall, W. Kozacaynski, Model Transformation—the Heart and Soul of Model-Driven Software Development, Technical Report IC<sup>\_</sup>TECH<sup>\_</sup>REPORT<sup>\_</sup>200352, http://icwww. epfl.ch/publications/documents/IC<sup>\_</sup>TECH<sup>\_</sup>REPORT<sup>\_</sup>200352. pdf (2003).

[39] K.D. Tham, M.S. Fox, Enterprise models and their cost per spective, Proceedings for the Industrial Engineering and Management, Canadian Society for Mechanical Engineers Forum, 1998.

[40] K.D. Tham, M.S. Fox, Determining requirements and specifi cations of enterprise information systems for profitability, Proceedings of the 6th International Conference on Enterprise Information Systems, 2004, pp. 309 – 316.

[41] M. Ushold, M. King, S. Moralee, Y. Zorgios, The enterprise ontology, KER: Revised Completed Draft, 1997, pp. 1 –69.

[42] J.P. Van Belle, A Survey of Generic Enterprise Models, SACLA, East-London, 2002, pp. 1 – 15.

[43] F. Vernadat, UEML: towards a unified enterprise modelling language, International Journal of Production Research 40 (17) (2002) 4309– 4321.

[44] F. Vernadat, Enterprise Modelling: Objectives, Constructs and Ontologies, tutorial held at the EMOI-CAiSE Workshop, Riga, Latvia (June 7, 2004) 1–100.

[45] Y. Wand, R. Weber, Research commentary: information systems and conceptual modeling—a research agenda, Information Systems Research 13 (4) (2002) 363–376.

[46] L. Whitman, K. Ramachandran, V. Ketkar, A taxonomy of a living model of the enterprise, Proceedings of the 2001 Winter Simulation Conference, 2001, pp. 848–855.

[47] E. Yu, Strategic modelling for enterprise integration, Proceedings of the 14th World Congress of International Federation of Automatic Control, 1999, pp. 127 – 132.

[48] E. Yu, J. Mylopoulos, An Actor dependency model of organizational work—with application to business process reengineering, COOCS’93, 1993, pp. 258 – 268.

[49] A. Zaheer, S. Zaheer, Catching the wave: alertness, responsiveness and market influence in global electronic networks, Management Science 43 (11) (1997) 1493– 1509.

[50] M. Zelm, Ed., The UEML Project, CIMOSA-News 10 (1) (4/15/2003) http://www.cimosa.de/n030415.html.

K. Michael Goul is Professor in the Department of Information Systems, W. P. Carey School of Business, Arizona State University. He received a BS, an MBA and a PhD in computer science from Oregon State University. His research and teaching interests are in the areas of decision support, enterprise model management and service-oriented computing.

Karen Corral is Assistant Professor in the Department of Information Systems, W. P. Carey School of Business, Arizona State University. She received a BA from the University of Michigan, an MS and a PhD in computer information systems from Arizona State University. Her research and teaching interests are in the areas of data and knowledge management, and decision support systems.
