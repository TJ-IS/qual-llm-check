---
otero_id: 3806
otero_key: "QPF5RBNS"
title: "An empirical study of IS architectures in French SMEs: integration approaches"
authors: "Marc Bidan; Frantz Rowe; Duane Truex"
year: "2012"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.2012.12"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
RESEARCH ARTICLE

# An empirical study of IS architectures in French SMEs: integration approaches<sub>w</sub>

Marc Bidan<sup>1</sup>, Frantz Rowe<sup>1,2</sup> and Duane Truex<sup>3,4</sup>

<sup>1</sup>LEMNA, Universite´ de Nantes, France; <sup>2</sup>SKEMA Business School, France; <sup>3</sup>Georgia State University, CIS Department, J. Mack Robinson College of Business, Atlanta, Georgia, U.S.A; <sup>4</sup>Mittuniversitetet (Mid Sweden University) Department of Information Technology and Media Sundsvall, Sweden

Correspondence: Duane Truex, Georgia State University, CIS Department, J. Mack Robinson College of Business, 33 Broad Street, Atlanta, Georgia, 30303-3083, U.S.A. Tel: þ 1 404 413 7380; Fax: þ 1 404 964 3240; E-mail: dtruex@gsu.edu

## Abstract

This paper, based on a cross-sectional empirical study of information system (IS) architectures within 143 small to medium enterprises (SMEs) in France, reports findings on how SMEs architect to achieve IS integration and interoperability. This research provides an empirically derived taxonomy of enterprise architectural variants of the types often described in the literature for large firms. This study finds indications that for SMEs the immediate goal of interoperability prevailed over fuller and more formal system integration. The most common means for approaching enterprise architecture and any form of integration is via the construction of software bridges and interfaces. Partially standardized architectures based on Enterprise Systems (ERP) are the next most common type. Hybrid architectures – mixed Enterprise Applications Integration and ERP – are the third most common. The contribution of this paper lies not in the identification of the three types but resides (1) in the description of their distribution in SMEs; (2) in the absence of other integration/interoperability types in this population; and (3) most importantly in the interpretation of the organizational and historical rationale explaining the emergence of these types in this organizational context. European Journal of Information Systems (2012) 21, 287–302. doi:10.1057/ejis.2012.12; published online 27 March 2012; corrected online 27 March 2012

Keywords: information systems integration; IT architecture; SME (small to medium enterprise)

## Introduction and problem statement

Achieving information systems (ISs) integration, a daunting task for any organization, is especially challenging for small firms. Specific challenges facing small to medium enterprises (SMEs) during these projects arise from their small size, centralized management, lack of organizational specialization, intuitive strategic planning and relatively unsophisticated deployment of ISs. Typical SMEs face difficulties during information technology (IT) adoption arising from a lack of technical competency and know-how, shortages of qualified human resources, risk aversion and environmental uncertainty, insufficient support technologies or organizational structures (Blili & Raymond, 1993; Ballantine et al, 1998; Duhan et al, 2001; Themistocleous & Chen, 2004; Benlian, 2009). Small firms have relatively fewer resources to redeploy than larger organizations while still facing the same competitive challenges and reasons for investing in ITs and ISs as the large firm. There is evidence that SMEs trying to achieve a measure of integration through the deployment of Enterprise Systems (ERP) have relatively more problems in gaining sufficient participation from different organizational functions during ERP selection (Laukkanen et al, 2005).

SMEs are also major engines of economic growth and employment worldwide (Susman, 2007), and in Europe the ‘20 million SMEs in the EU represent 99% of businesses’ with 1.1 million of these firms contributing 40% of the total European economic turnover (European Commission, 2003). In France, the setting from which this study is drawn, SMEs represent more than half of all private employment and more than half of gross national product (A<sup>´</sup> cs et al, 2008; A<sup>´</sup> cs & Szerb, 2009). SMEs are also understood to be sources of creative energy and innovation providers of novel solutions to practical problems, but because they have proportionately smaller resource bases to draw from, it has been suggested that they must be more frugal and creative in the management of organizational resources (Admiraal et al, 2003; A<sup>´</sup> cs et al, 2008; A<sup>´</sup> cs & Szerb, 2009). Although some literature exists on ERP adoption (Buonanno et al, 2005), SME-specific IS architectural surveys are virtually non-existent. And, since much of the current literature examines IS integration through the lens of the large-scale enterprise, it is unclear whether these findings generalize well to the SME. Therefore, we thought that having better empirically derived understanding of how the SMEs approach ISs integration and the way they manage to acquire, husband and deploy ISs resources into a logical IS architecture would be valuable for two reasons. First, if novel models of how they manage these resources were to be discovered, others would benefit from this knowledge. Second, if finding patterns of problems in this population of organizations later leads to more efficient operations for these firms, then society benefits. In either case, describing how SMEs approach the problem of IS integration and how we can best describe their resulting IT architecture in their organizational context (i.e., IS architecture) is valuable given their economic impact and the sheer numbers of SMEs.

The special attention paid to the technology context is in accord with Orlikowski & Iacono’s (2001) view that many IS studies have privileged the organizational context at the expense of the technological context (Orlikowski & Iacono. 2001). Much of the mainstream IS literature is focused on why people develop and use IT in organizational settings without being explicit as to the technical context itself (Orlikowski & Iacono, 2001). Unfortunately, generalized references to technological concepts deprive us of the ability to describe those objects with and any degree of precision leading to another problem recognized by Orlikowski and Iacono. Namely, ‘that IT is not a major player on its own playing field [that] y IT artifacts are either absent, black-boxed, abstracted from social life or reduced to surrogate measures’. We see our research as one attempt to ‘put the IT back into IT research’ by giving greater clarity of definition about the IT artifact. We see this research as being positioned between Orlikowski and Iacono’s tool view and ensemble view of the IT artifact. This is because our study examines which ITs are present as backbones of the architecture and also how they are organized to further ISs integration. But we do not ignore the diversity of the SMEs own history and organizational context; we contextualize our description of IS architectures and systems integration in light of the firm’s technological history and firm size.

With these concerns in mind, we developed an exploratory research plan with two primary research questions:

\- RQ1: What are the main IS architectures found in SMEs?

\- RQ2: What kinds of systems integration approaches are present in SMEs?

As the starting point, we first turn attention to the definitions of the artifacts under consideration because the study of a discipline is principally the study of the language of the discipline (Postman, 1988). Agreed-upon terms lead to agreed-upon meanings (Davenport, 2005). These agreements allow for standardized use, the identification of metrics and the development of standardized measures used to compare and control process. Establishing a clear definition of the term in question helps determine the precision of the finding. In the section ‘Prior Research: IS Architectures, System Integration and Standards’, we situate and discuss the persistent question of IT-organizational integration and prior research on IS architectures (sometimes called enterprise architectures) and the integration of ISs. The section ‘Research Method’ explains the research methodology. The section ‘Result: A Taxonomy of Three IT Architecture Types’ presents results including a taxonomy (Bensaou & Venkatraman, 1995) of architectural standards arising from our analysis of a large sample of French SMEs, one that differs from commonly cited typologies in the literature. The section ‘Discussion’ discusses the findings and draws conclusions for future research.

## Prior research: IS architectures, systems integration and standards

The goal of creating systems that are truly interoperable has driven research and practice through generations of conceptual development in information engineering, database research, ERP, and more recently of Enterprise Applications Integration (EAI) (Sharif et al, 2005) and service architectures (Puschmann & Alt, 2005). Firms have sought to achieve interoperability via ad hoc application-to-application connections and via formal planned solutions. In the following subsections, we examine key concepts associated with the goal of gaining greater interoperability – the notions of IS architectures and ISs Integration – to ground the working definitions guiding this research. We first turn attention to the concept of ‘the architecture’.

## IS architecture

For both IS management and IS academics, the concept of an IS architecture has been used since the very beginning of the IS discipline (Farrell & Saloner, 1985; Brancheau & Wetherbe, 1986) and remains of critical interest today (Luckham & Vera, 1995; Medvidovic &

Table 1 Ross’ architectural types

<table><tr><td>Type-Ross terminology</td><td>Ross/Ross et al</td><td>Our treatment</td></tr><tr><td>Enterprise architecture</td><td>‘... the organizing logic for business process and IT capabilities reflecting the integration and standardization requirements ...’</td><td>The logic and goals behind the need for ISs. We prefer the term IS architecture. Indeed, this logic is reflected in architecture of IS components in relationship with its organizational context</td></tr><tr><td>IT architecture</td><td>The plan for the next infrastructure referring to sets of standards.</td><td>Sets of tools with the goal of some level of interoperability and/or integration</td></tr><tr><td>Enterprise IT architecture</td><td>The IT architecture connected to business requirements.</td><td>We do not address this issue in this research.</td></tr></table>

Taylor, 2000). Achieving scalable and flexible architectures regularly appears as an important concern to CIOs in the SIM (Society for Information Management) annual survey. The topic continues to appear in the IT literature on databases, e-commerce, integration architecture for process portals and software engineering (Niederman et al, 1991; Sowa & Zachman, 1992; Colomb & Orlowska, 1995; Gomaa, 1995; Hamilton, 1999; Sambamurthy & Zmud, 2000; Puschmann & Alt, 2005) and in the literature on managing organizational ISs (Chalmeta et al, 2001). This literature assumes a general agreement or common understanding of the term ‘IS architecture’ while often ignoring the meta-level concept itself.

The notion of an architecture is problematic in part because it seems to be usefully ambiguous and is often used at a high level of abstraction where anyone can agree that it is a useful concept. But, at lower levels of abstraction, the term ‘IS Architecture’ has many different meanings and realizations (Peristeras & Tarabanis, 2000). Corneliussen describes architecture as being ‘a plastic concept y ametaphorical idea that shapes the categories, discourse and language used’ (Corneliussen, 2008). Smolander et al (2008, p. 575) ‘identify multiple metaphors – “blueprint”, “literature” “Language” and “Decision” that stakeholders use to understand y the term software architecture and effectively participate in its use’. In the architecture-as-blueprint metaphor, the IS architecture is seen as the ‘structure of the system y a plan for some future IT artefact’. In the IS literature, variants of the notion include: application architecture, Information Architecture (the rationality and design of databases (Martin, 1986; Finkelstein, 1989), Enterprise Architecture (Zachman, 1997; Boh & Yellin, 2006), Software Architecture (Kruchten, 1996; Gru¨nbacher et al, 2004), IT architecture, and Enterprise IT Architecture. To make matter worse, these various terms are often used interchangeably. In this paper, we adopt the definition of an architecture provided by the IEEE (Institute of Electrical and Electronics Engineers) standard 1471–2000 that reads:

## Enterprise architecture

The Enterprise Architecture is an overarching construct supporting the alignment of IT and business goals (Lapkin, 2004; Rohloff, 2005, 2008). Our view is consistent with Ross’s et al notion of the Enterprise Architecture as an organizing logic.

The enterprise architecture is the organizing logic for business process and IT capabilities reflecting the integration and standardization requirements of the firm’s operating model. (Ross et al, 2006)

Arguing that the ‘IT architecture [also] y lacks a universally accepted definition’ Ross (2003, p. 31) characterizes the concept of an architecture in three ways – as Enterprise Architecture, IT Architecture and Enterprise IT architecture. We summarize Ross’s characterizations in Table 1 below illustrating that although a suitable comprehensive definition may not be established in the literature there are commonly understood definitions at different levels of organizational abstraction.

## IT architecture

At the level of the technical system, Ross and others refer to the ‘IT Architecture’ covering both technical standards and infrastructure level elements.

y the terms architecture and infrastructure are sometimes used interchangeably, with architecture seen as the plan for the next infrastructure. More often, IT architecture refers to a firm’s list of technology standards. But viewing IT architecture only as technology standards does not connect it to business requirements. The enterprise IT architecture concept, though, does place technology standards in the context of business requirements. (Ross, 2003, p. 32)

Ross et al also identify a ‘four stage model of increasing enterprise IT architecture competency’: (1) the applica tion silo; (2) standardized technology; (3) a rationalized data architecture; and, (4) modular architecture. These stages depict a hierarchical evolution wherein companies develop IT architectures dealing with data, technology infrastructure and applications (Ross, 2003, p. 37). To our thinking, this viewpoint privileges the role of standards and modular components that characterize IT architectures. While we concur with the idea that architectures may be contextualized at different levels of organizational abstraction, we find that the Ross’s first definition, that of the enterprise architecture, underlines two different issues: the rationale of the firm itself, and the technical aspects of integration and interoperability.

For us, the ‘enterprise architecture’ is the rationale of the firm behind the set of organizational ISs; it is that which makes sense of these systems. Accordingly, in this paper, we distinguish between the operationalization of how ISs components are made to communicate or to connect at a relatively superficial level (i.e., its level of integration or of interoperability of its IT Architecture) and the logic behind (i.e., enterprise architecture), which is an expression of the rationale of the firm behind the set of organizational ISs; it is that which makes sense of these systems.

## IS integration

The origins of the term ISs integration are technical and closely associated with the application implementation level of abstraction (Beniger, 1986; Ross, 2003). The ideal integrated IS long sought by both researchers and vendors alike (Beniger, 1986; Besson & Rowe, 2001; Sharif et al, 2005), such as the concept of an architecture, is characterized in many ways in our literature: database, taxonomy, meta types, process integration, application integration, business integration, web services, EDI or simple API connectors. We see these characterizations of integration as falling into generalized classes: first, those providing interconnectivity between the individual components of hardware infrastructures and, second, those providing software interoperability of applications (packages), of processes (ERP) or of data (databases) or combinations of these three elements. (Boh et al, 2003; Boh & Yellin, 2006).

There are also different domains of integration – within or between the departments, functions, firms, supply chains and industries – sometimes referred to as interand intra-organizational systems. At the datalogical level, database integration provides the means to both rationalize the sharing and access to data (Cheney & Kasper, 1993, p. 28). At the application and process levels, integration is sometimes equated with an ERP implementation even when the ERP treat the ERP as just another application. That is, rather than providing greater organizational systems integration, the ERP simply creates stovepipes of localized integration and may further exacerbate other islands of automation (Huin, 2004) and may make further integration of data and processes extremely difficult and unlikely (Truex & Ngwenyama, 2000).

Drawing from the world of practice, Markus (2000b, p. 7) provides a typology of three broad approaches to systems integration (c.f., Table 2) and dismisses application-interface integration as insignificant because it only connects superficially at a high level of abstraction leaving processes and data alone.

The typologies and examples as provided by Ross et al (2006), Markus (2000a) and examples from Sharif et al (2005) and Irani et al (2003) discussed above were derived from very large-scale organizations. Our own research examines the behaviors of much smaller-sized organization. Thus, as we began our analysis of data drawn from the domain of the SME, we wondered whether these typologies derived from the domain of the large organization would prove to hold true in the case of SMEs in France. Our research is primarily concerned with how SMEs, in practice, actually do achieve varying degrees of interoperability or even of integration. In our data, we found that many actually used APIs and software bridges as whole or partial solutions for achieving IS interoperability. But, since Markus and Ross dismissed the building of software interfaces as a kind of bona fide integration, we found it necessary to reintroduce the application interface-level approach (called Interface or software bridges) in our explication of the Markus-identified integration approaches.

Table 2 Characterization of approaches to IS integration or interoperability

<table><tr><td>Approaches architectural dimensions</td><td>Data warehousing</td><td>ERP systems</td><td>Re-architected systems (EAI)</td><td>(APIs) Interface or software bridges and/or web services</td></tr><tr><td>Databases</td><td>Several DBs with extraction to a data warehouse for processing and analysis</td><td>Several DBs but only one logical DB</td><td>Several DBs but only one logical DB</td><td>Several DBs</td></tr><tr><td>Logical view of the architecture</td><td>Hierarchical: Tree structure</td><td>Modular</td><td>Modular and tree structure</td><td>Opportunistic, heterogeneous, patchwork, bricolage</td></tr><tr><td>Major integration practices</td><td>Extraction and pertinent processing of data</td><td>Re-engineering of processes</td><td>Interconnection of application&#x27;s DBs</td><td>Interconnection of few applications and/or DBs, cloud computing</td></tr><tr><td>Major integration impact</td><td>Structuring of data and updating of processing</td><td>Real time, unique reference and cross-functionality</td><td>Increase the scope of extant/legacy systems w/o changing logical data models</td><td>Degrees of interoperability degrees of flexibility</td></tr><tr><td>Major architectural feature</td><td>Data extraction process</td><td>Single logical database; modular architecture</td><td>Middleware</td><td>Application connectors</td></tr><tr><td>Major integration objects</td><td>Data</td><td>Database and Process</td><td>Application</td><td>Application Internet</td></tr></table>

In Table 2, we compare integration approaches using six different criteria for comparison. Those criteria include: (1) the databases, for example are they distributed, one logical data model or several relatively independent models (Giachetti et al, 2003; Giachetti, 2004); (2) the logical view of the architecture, (Kruchten, 1996); (3) integration practices, that is, what you do with the technology; (4) integration impacts (Markus 2000a, b; Rowe et al, 2005); (5) major architectural feature, the primary focus of the integration practice; and, finally (6) the major integration object, the focal object of the integration approach (Peristeras & Tarabanis, 2000).

The four approaches, shown in Table 2, describe systems solutions that can be either (1) complimentary, as in the case of the conjunction of ERP and data warehouse or in the case of ERP and EAI (Sharif et al, 2005); or (2) substitutable, wherein types may be used in combination at the operational level or may be entirely replaced as in instances where an ERP replaces a set of prior systems. Functionality may differ, but all changes to the systems are made in response to real-world organizational requirements. Thus, we refer to these four approaches as: (1) Data warehousing; (2) ERP systems; (3) EAI re-architected systems; and (4) Interface software (API). Each of these have ‘pros and cons’ arising from various organizational, competitive and environmental factors (Markus 2000a, b; Lam, 2005; Sharif et al, 2005). We note, for instance, that

\- Data warehousing achieves data integration without changes in source systems or business process. Data warehousing does not, therefore, support process integration.

\- Conversely, ERP systems achieve excellent internal data and process integration when all legacy systems are replaced. But ERP systems demand a single common data model. Thus, ERP systems limit the opportunities to incorporate external data sources and do not readily allow integrated reporting and analysis environments requiring both internal and external data. ERP solutions also often require extensive organizational change and dislocations. ‘The problem with this thinking is that it assumes that the ERP software provides an acceptable level of business fit when it is first implemented’ (Light et al, 2001).

\- EAI achieves internal data integration and can support process integration without replacement of legacy systems (Irani et al, 2003; Sharif et al, 2005). This allows a firm to retain legacy systems for some operations and keep extant production databases. However, EAI requires modification of source systems. ERP and EAI projects share several common characteristics (Lam, 2005). Like ERP systems, EAI also encourages use of ‘best-of-breed’ applications from multiple vendors. Yet EAI leaves the organization with vestiges of its original and familiar systems. Because it is difficult and expensive and offers a large diversity of solutions but no de facto standard (Khoumbati et al, 2006), SMEs are still suspicious about the maturity, the future and applicability of this technology.

\- APIs allow limited degrees of interoperability without requiring any formal architectural planning. In this approach, the individual application is king and the pragmatic need to connect at a superficial level requires the development and maintenance of software bridges linking application to application. Their development may be haphazard and may, over time, become a bricolage of programming. If the organization and its systems grow substantially, the complexity of maintaining these individual software APIs may overwhelm or force a move to other more formal or systematic integration approaches. But it is also true that this approach may well serve those small organizations having few applications for a very long time.

The typologies as discussed above provide an attractive and somewhat intuitive and clear description of how firms might go about architecting and integrating ISs, but the real world is messy. The IT manager is always facing the pragmatics of daily operations while having to rationalize the systems architecture. In practice, one rarely sees IT architectures based on only one type of IS integration approach; there tend to be many mixed and partial systems integration implementations. For instance, among firms deploying ERP systems, very few adopt all the available process modules, opting not to be fully committed to the integration and standardization options required by the ERP (Themistocleous et al, 2001; Rowe et al, 2005). Or, when firms merge, bringing legacy systems and databases from each firm, it is often necessary to integrate data from multiple sources. At the strategic and practical level, combining data warehousing in addition to ERP systems may be required (Holland & Light, 2001). The combination may forestall a situation wherein one of the merged firms has to abandon its investment before integrating its systems. This suggests that the requirement that systems be up and running is an overarching concern. Consequently, their linkages are of prime concern, whereas the formality of the rationality governing the operations and interoperability of these systems is of secondary concern. Because of these pragmatic operational concerns, we were also very curious to determine whether in our data we might discover clear delineations in architectural and integration approaches.

## Research method

Much of the empirical literature on IS architectures and system integration is based on case studies (Avital & Vandenbosch, 2000; Markus, 2000a; Truex, 2001; Irani et al, 2003; Sharif et al, 2005; Ross et al, 2006) vs surveybased research, a notable exception being Tractinsky & Jarvenpaa (1995). Our research arises from a larger project developed to better know the kinds of IS architectures in place in various sized French businesses. Previous publications from this research project have addressed the use of ERP in firms of all sizes (citations withheld during review). This paper explicitly addresses the SME portion of the larger data set. At the outset of this research program, we chose a mixed methods research design in which we conducted field studies, and interviews and collected survey data. Part of the research involved an exploratory questionnaire from which was conducted a kind of cluster analysis, typically used to describe firms as configurations in a holistic way (Aldenferder & Blashfield, 1984), to identify similar sets of organizations from which we could select exemplars for in-depth case studies (citations withheld during review).

Because this present paper extracts from an exploratory questionnaire and because we do not test propositions drawn from a body of well-developed theory, we view this research as exploratory. We see this research as contributing to the description of the artifacts and to furthering the development of taxonomies by which we can establish standardized terminology and later a theory of those artifacts and their ecosystems (Star & Ruhleder, 1996).

In this paper, the descriptions of the IS architectures and systems integration are derived through statistical analysis rather than being derived from a particular theory ex ante to the research. Why? Because we are looking for commonalities between organizations in various demographic clusters and we cannot preclude any particular commonality a priori to the analysis. For example, do any of the integration patterns resemble the approaches described in Table 2? We simply identified the types that surfaced from the cluster analysis and then compared those with these approaches derived from the literature. This research follows the well-established French school of multivariate analysis (Lebart et al, 1984) more fully described below.

## Data collection, pre-testing and measures

One author had developed a firm contact list of more than 600 French firms during his supervision of professional student internship placements. Starting with this database, he selected a convenience sample of the 223 firms whom he knew to be concerned about their IS issues. He made telephone contact with key IS decision makers asking them whether they were concerned with IS integration issues and whether they would agree to answer a questionnaire about the firms’ IS architecture, systems integration and firm demographics. In each instance, his contact was the manager most knowledgeable or principally responsible for the firm’s system integration issues. Most of the time, the respondents turned out to be the CIO.

The initial questionnaire was developed following an extensive literature review and discussion with team members and other researchers examining these issues in larger firms in France and the United States. The survey instrument was pre-tested with 13 integration practitioners, project managers and CIOs. The survey pre-tests helped clarify terminology and cut the length of the questionnaire. In the pretest phase, we found that the data warehouse concept required clarification and explication. For many SME managers, it was simply not relevant or applicable. Therefore, when it was later determined that none of our SME survey set deployed data warehousing, this item was removed. Data were gathered in early 2002.

In our pre-contact phase, 223 firms had agreed to participate, and thus 223 surveys were sent out. Out of those surveys sent, 156 replied – a 69.95% yield. We followed up with telephone questions when surveys were incomplete. But even with our telephone follow-ups, 61 firms never completed the instrument and we eliminated another 13 survey responses considered to be inconsistent or illegible. In the end, we had 143 useable surveys, a 64% yield. By comparison, an earlier attempt to survey SMEs using ‘cold call’ mailed instruments to SMEs in Paris netted a paltry a 15% response rate. In this research, the data collection was highly interactive and we believe that our ‘high-touch’ process of data collection explains the high response rate and the high quality of the data obtained.

The questionnaire had two main parts. The first part described the organizational context and demographic characteristics including age and size of firm. Part two addressed the degree of IT architectural integration by including questions asking the degree and maturity of system integration (Markus, 2000a, b; Ross, 2003; Sharif et al, 2005). The questionnaire included 15 items covering contextual issues and IS architectures and IS integration. The constructs, the possible item values and the underlying core notions for each question are described in the appendix.

## Data analysis, statistical tool and tests

Cluster analysis The analysis tool we used, SPAD.N version 3.21, although commonly used and well accepted in France both by researchers and practitioners, may be unfamiliar to non-Francophone researchers. The main reasons for using SPAD.N is that (1) it integrates methods for analyzing multiple correspondence in nominal data; (2) its power in analyzing the automatic ranking classification; (3) for its descriptive power in identifying clusters and describing them by characteristic modality; and, (4) for the relevance of its aggregated criteria of the primary measure, namely the Value Test (VT). SPAD.N and its use has already been introduced in the Englishlanguage IS literature (Rowe & Struck, 1999).

We first performed a cluster analysis to discover factors differentiating the firms in our convenience sample. In rough terms, this is a two-step process. Step 1 involves the construction of the main clusters derived iteratively in the statistical tool SPAD (Lebart et al, 1984). The second step is to describe each cluster. Those descriptions arise from the various VT and other statistics as described below.

Cluster formation There are several methods for forming clusters (Everitt, 1993; Sharma, 1996; Hair et al, 1998). In this study, we used a hierarchical agglomerate method to define initial cluster. In contrast, the nonhierarchical procedure does not involve the construction of a treelike structure, where the results at an earlier stage are always nested within the results of a later stage (Gerdin, 2005). Instead, objects may be reassigned if they are closer to another cluster than the one originally assigned. We examined the results from the hierarchical clustering procedure and made adjustments as part of the iterative analysis to establish the number of clusters. In this analysis, we choose three clusters because they provide the best partitioning and representation of intra-cluster relevance and inter-cluster distance (See Table 3).

SPAD.N’s cluster analysis approach identifies and systematically sorts, among the variables included in the model, those (discrete or continuous) that are statistically significantly related to a specific discrete variable. The test compares various proportions using, on the one hand, $\chi ^ { 2 }$ for discrete variables and, on the other, a statistic related to the t-test for continuous variables. The computed statistics are converted into a probability level, allowing for a simultaneous sorting of both types of variables. In order to assess the differences between percentages or average means, SPAD 3.21 performs different statistical tests (hypergeometrical law for proportions and corrected t-tests for average means) that it expresses as the standard deviation of a distribution. The VT equals the standard deviation (for VT42, at the 5% error threshold). Typically, it can be used for answering a complex question such as ‘Is the proportion of enterprise architecture which are categorized by some integration greater when these EAs use ERP than when they use a other technology?’ (Rowe & Struck, 1999).

To learn more about the tool and these techniques, refer to Lamarche (Lamarche et al, 2003).

Cluster separation and description The level of difference between the clusters is given as a set of researcherselected variables. It is a type of multivariate analysis. The analyst examines the relative strength of individual variable or subsets of variables (including outlier variables) that the tool has characterized by its various measures of cluster closeness/relatedness. In SPAD.N, these measures are characterized as VTs. The next step is to interpret these clusters and relate them back to our empirical analysis template drawn from the literature.

Dendograms A dendogram, a visual representation of the cluster, shows the entire sample organized by the relative nearness factors computed by the clustering tool. We used a hierarchical clustering procedure as represented in the dendogram (Figure 1).

Within the hierarchical cluster procedure, there are several ways of forming clusters (see Sharma (1996) for an overview of widely used clustering algorithms). Ward’s optimizing algorithm, combined with squared Euclidean distance as the measure of similarity, was chosen on the basis that it has been widely used within the social sciences (Everitt, 1993). This method maximizes within-clusters homogeneity; i.e., it minimizes the within-group sum of squares (Sharma, 1996). (Gerdin, 2005)

## Sample description and partition

The study initially targeted the mid-size market segment as defined by the ERP vendor’s market criteria. It quickly became apparent that the primary criterion in the purchase decision for the SME market segment, is ‘the fit with current business processes’ (Van Everdingen et al, 2000). SMEs are, like their larger-firm brethren, courted by a host of ERP vendors and system integrators. From the ERP vendor’s point of view, their mid-size market is defined as comprising firms employing from 30 to 3000 employees. (c.f., SAP annual report for (2006) or Gartner market reports, (Scavo, 2007)). For instance, SAP itself describes its product Business One as being for firms employing 30–300 and R/3 as being for larger firms. Smaller firms are served by other vendors such as SAGE Software or Lawson-Intentia, although SAP acknowledges that the mid-size market is an important and growing part of their portfolio. These market segments account for approximately 65% of SAP’s total customer base, and are an important part of their plan for ambitious revenue growth.

Table 3 Partitioning

<table><tr><td>Best partition combinations in n categories by the change of relative inertia (n=2 by10)</td><td>Number of firms in each category (Total=143)</td><td>Inter class inertia/total inertia ratio. Before the consolidation of the partition</td><td>Inter class inertia/total inertia ratio. After the consolidation of the partition</td><td>Change in inertia ratio (After/Before)</td></tr><tr><td>2</td><td>C1=61/C2=82</td><td>0.2648</td><td>0.2648</td><td>1</td></tr><tr><td>3</td><td>61/29/53</td><td>0.3485</td><td>0.3513</td><td>1.0080</td></tr><tr><td>5</td><td>61/29/10/11/32</td><td>0.4595</td><td>0.4668</td><td>1.0158</td></tr><tr><td>7</td><td>33/7/21/29/10/11/32</td><td>0.5226</td><td>0.5324</td><td>1.0187</td></tr></table>

Classification hierarchigue directe  
![](/api/attachments/QPF5RBNS/fulltext/images/24b7c7d6604d05b421920809bbad64dc43a92c0c7cf0996e94f1020e2402b9f4.jpg)  
177,204188,221,236,233159226,222,228040202,203151195135,214,213,208,235,234220229192,227207183137131,206201,215066,230205,231,197217,218,219,232126125140130211,216138,109209  
Figure 1 Our dendogram.

Table 4 Sample distribution

<table><tr><td>Size</td><td>10–30</td><td>31–100</td><td>101–250</td><td>251–500</td><td>501–3000</td><td>Total</td></tr><tr><td>N</td><td>3</td><td>72</td><td>16</td><td>29</td><td>23</td><td>143</td></tr><tr><td>Percentage</td><td>2</td><td>50.5</td><td>11.1</td><td>20.2</td><td>16.2</td><td>100</td></tr></table>

In Table 4, we see that 98% of firms in our sample belong to the ‘mid-size’ segment, firms with 30–3000 employees. At the tails of the distribution, we note that only 2% of firms in our sample are smaller than 30 employees and 16% employ more than 500 people. Because of the size distribution of our sample respondents, and since in France the medium size firm employs 100–500 employees, small firms employ 10–100 and so-called micro-firms employ fewer than 10, we have adopted a French-sized classification scheme. As to firm size, our sample mean is 244.5 with a rather large standard deviation of 347.5. This deviation occurs because a few of the sampled firms were relatively large having 2500–3000 employees. (c.f., Table 4).

Using the clustering technique described earlier, we conducted an n-wise partitioning of the sample into two, three and five categories. We examined the before and after comparisons of inter-class inertia/total inertia ratios and retained only the most stable – that is, those having the smallest in the ratio between iterations consolidation – and the most empirically relevant partitioning. We gained precision and achieved stability after two iterations when the change in the inter-class inertia was almost null (0%) for t. For categories three, five and seven, the consolidation stopped after three iterations when stability was reached. Table 3 gives the main characteristics of the various partitioning and shows the changes in the inertia ratios after each iteration (c.f., Table 3). Normally, we would stop after the first iteration achieving stability at two clusters – the first with firms having an ERP system and the second as firms without ERP systems. Although we determined that two clusters gave a rigorous clustering, we chose to continue the process and found that with additional iterations we retained nearly the same precision but acquired much greater operational relevance. Even though we have reported the full results in Table 3 to be consistent and clear, we provide a description of the first two category partitioning representing, respectively, 61 and 82 firms. As described earlier, this partitioning shows clearly that IT architecture first differs by the federated vs the integrated archetypal distinction.

The Silos Architecture type (N ¼ 61) displays the following very significant characteristics:

\- No ERP (VT ¼ 13.5)

\- No common database (VT ¼ 13.5)

\- More than eight specific applications (SA) (VT ¼ 4.5)

While the integration type (N ¼ 82) also displays the following characteristics:

\- One ERP (VT ¼ 14.6);

\- Having a common database (VT ¼ 4.3)

\- Having between 4 and 8 modules deployed (VT ¼ 6.2).

The ‘Silos Architecture’ category (representing 61 firms or roughly 43% of the population) is reasonably homogeneous. The ‘integration’ category, however, can be further fragmented, which is suggested by the partitioning in three, then five categories. The seven category partitioning shown in Table 3, simultaneously, fragments the two archetypes of the very first partitioning and is overkill. We found the partitioning into three categories to be more satisfying in terms of change of inertia ratio, and more interesting than the mere distinction between the two archetypes. We will therefore focus on this taxonomy in the following description and analysis.

Table 5 ‘Silos architecture  
Category 1: Silos architecture  
N1 ¼ 61 or 42.7% of 143 (the most common category)

<table><tr><td>Column 1</td><td>Column 2</td><td>Column 3</td><td>Column 4</td></tr><tr><td>Attributes found significant</td><td>VT (&gt;2 is significant at the 0.005 level)</td><td>Attribute/Category (percentage of the category n with this characteristic)</td><td>Total sample (percentage of the total with this characteristic)</td></tr><tr><td>No ERP</td><td>13.5</td><td>100</td><td>42.6</td></tr><tr><td>Support specific applications</td><td>8.5</td><td>88.5</td><td>48.2</td></tr><tr><td>Core specific application</td><td>8.2</td><td>88.5</td><td>49.6</td></tr><tr><td>&gt;8 specific applications</td><td>4.5</td><td>39.3</td><td>21</td></tr><tr><td>Without a common DB</td><td>4.3</td><td>100</td><td>86.7</td></tr><tr><td>&lt;100 employees</td><td>2.5</td><td>65.6</td><td>52.4</td></tr></table>

Result: a taxonomy of three IT architecture types In this partitioning, we identified three categories or classes, which we call (1) the ‘Silos Architecture’, (2) the ‘Partially Standardized Architecture’ and (3) the ‘Mixed Architecture’. We will describe each using only variables for which the VT is greater than 2 (i.e., less than 5% threshold error) and can therefore be considered or statistically significant. In the following tables, variables always appear by decreasing order of characterization of a category.

## First category: silos architecture

We call this category ‘Silos Architecture’ because our cases show that, most of the time, there are no clear and formalized enterprise architecture policies in the firms falling in this category. However, there is a trend toward a vision of the MIS that calls for some understanding of its enterprise architecture. Even in this category, it is becoming quite rare that firms use applications in completely closed silos. However, the logic of the Silos architecture is not that of integration in the pure sense, as we shall see below, but simply of limited or controlled interoperability. In Table 3 and the following tables, ‘SA’ refers to Specific Applications, or as they are alternatively called in the literature, autonomous applications.

First, because the table structure and presentation we use in this paper, while common in French technical literature, is less common in English literature, we provide a bit of orientation to the presentation of the data in the following sections. The first column gives all discernable characteristics that were found statistically significant at the 0.05 level. Column 2 gives the actual VT values. Columns 3 and 4 offer different views of the data. As an example of one such view, Row 6 describes those firms without a common enterprise data model. Row 6/Column 3, Attribute/category, shows that 100% of the 61 Applications Silos firms were did not have common databases. Row 6/Column 4 shows that 100% of the firms without common databases comprise 86.71% of the total sample of 143 firms. In other words, Column 3 describes the specific attributes of the firms in this category. Continuing with our interpretation of Table 5, the VTs indicate that the ‘Silos Architecture’ category firms are strongly characterized by the lack of ERP systems, and therefore have a large number of autonomous SA, both for operation and support functions. This category does not utilize a common logical database and is made up of rather smaller firms of fewer than 100 employees. The architecture looks like a set of heterogeneous applications with few interfaces, and is a non-modular, tree-type, hierarchical architecture. These firms have SA without ERP modules in both core activities and support activities (c.f., Figure 2).

![](/api/attachments/QPF5RBNS/fulltext/images/d7cbff585d623b84608ef25e07d52828113c4a8e05d73c69a849be772ed4255b.jpg)  
Figure 2 Silos architecture.

## Second category: partially standardized architecture

This Partially Standardized Architecture category (c.f., Table 6) is characterized by the limited coverage of the ERP (in terms of the number of modules installed). One hundred percent of the firms of this class have a unique ERP, 90% for at least one module for its support activities and 77% for its core activities. However, 77% of the firms in this category have from one to three modules deployed and one to three SA. Partially Standardized Architecture with 83% of reporting firms do not have an EAI platform and have no common database. These firms are of rather modest size with 90% having fewer than 100 employees. They are also young firms; 80% of them are less than

Table 6 Partially standardized architecture  
Category 2: partially standardized architecture  
N2 ¼ 30 or 21% of 143

<table><tr><td>Column 1</td><td>Column 2</td><td>Column 3</td><td>Column 4</td></tr><tr><td>Attributes found significant</td><td>VT (&gt;2 is significant at the 0.005 level)</td><td>Attribute/Category (percentage of the category n with this characteristic)</td><td>Total sample (percentage of the total with this characteristic)</td></tr><tr><td>1–3 ERP modules</td><td>8.5</td><td>76.7</td><td>14.5</td></tr><tr><td>A unique ERP</td><td>6.5</td><td>100</td><td>51</td></tr><tr><td>1–3 specific application</td><td>6.4</td><td>86.7</td><td>35</td></tr><tr><td>Support ERP module</td><td>4.8</td><td>90</td><td>51</td></tr><tr><td>&lt;100 employees</td><td>4.7</td><td>90</td><td>52.4</td></tr><tr><td>No support specific application</td><td>4.3</td><td>86.7</td><td>51.7</td></tr><tr><td>No EAI</td><td>4.1</td><td>83.3</td><td>49.6</td></tr><tr><td>Core ERP module</td><td>3.2</td><td>76.7</td><td>49.6</td></tr><tr><td>No core specific application</td><td>3.1</td><td>76.7</td><td>50.3</td></tr><tr><td>&lt;5 years old</td><td>2.9</td><td>80</td><td>55.2</td></tr><tr><td>CEO responding</td><td>2.8</td><td>50</td><td>27.3</td></tr></table>

Table 7 Mixed architecture  
Category 3: mixed architecture  
N3 ¼ 52 or 36.3% of 143

<table><tr><td>Column 1</td><td>Column 2</td><td>Column 3</td><td>Column 4</td></tr><tr><td>Attributes found significant</td><td>VT (&gt;2 is significant at the 0.005 level)</td><td>Attribute/Category (percentage of the category n with this characteristic)</td><td>Total sample</td></tr><tr><td>Core ERP module</td><td>8</td><td>92.3</td><td>49.6</td></tr><tr><td>4–8 ERP modules</td><td>7</td><td>61.5</td><td>26.6</td></tr><tr><td>Support ERP module</td><td>6.9</td><td>88.5</td><td>51</td></tr><tr><td>A unique ERP</td><td>5.7</td><td>82.7</td><td>51</td></tr><tr><td>&gt;8 ERP modules</td><td>5.5</td><td>34.6</td><td>13.3</td></tr><tr><td>No core specific application</td><td>5.5</td><td>80.7</td><td>50.3</td></tr><tr><td>No support specific application</td><td>4.8</td><td>78.8</td><td>51.7</td></tr><tr><td>4–8 specific application</td><td>4.4</td><td>69.2</td><td>44.1</td></tr><tr><td>&gt;501 employees</td><td>4.3</td><td>34.6</td><td>16.1</td></tr><tr><td>Common enterprise DB</td><td>3.8</td><td>28.8</td><td>13.3</td></tr><tr><td>Several ERP</td><td>3.81</td><td>17.3</td><td>6.3</td></tr><tr><td>101–500 employees</td><td>3.4</td><td>50</td><td>31.5</td></tr><tr><td>EAI platform</td><td>2.6</td><td>65.4</td><td>50.3</td></tr></table>

![](/api/attachments/QPF5RBNS/fulltext/images/db281012d5554513c38a5d6f4056773f1346b73e98d945d1f79671689275f1fd.jpg)  
Figure 3 Partially standardized architecture.

5 years old. Their CEO is heavily involved as he or she led the project and responded to the questionnaire. This architectural type is represented in the Figure 3.

## Third category: mixed architecture

In this category (c.f., Table 7), we find that 29% of the firms do have common databases. Most (83%) have one ERP system, and a few (17%) have more than one. Firms in this category have at least a core activity module (92%), and a support activity module (88%). Many of these firms have from four to eight ERP modules in place (62%), with more than a third having (35%) having eight or more ERP modules. In transitioning to ERP, most firms appear to have abandoned autonomous SA in favor of the ERP system’s core operations (81%) and support activities (79%). They often have an EAI platform (65%) as well. Nearly one-third of these firms are among the largest firms of our total sample. This category also represents 29% of the firms having a common database. Because they have generally an ERP and an EAI, and a common database, they represent the closest match to Markus’ broad category of the hybrid firm (Markus, 2000a, b). We represent this category in Figure 4.

Table 8 Categories of SMEs IT architecture

<table><tr><td>Architectures</td><td>Silos</td><td>Partially standardized</td><td>Mixed</td></tr><tr><td>Databases</td><td>Several heterogeneous</td><td>One principal</td><td>Multiple databases; database interoperability via middleware data conversion</td></tr><tr><td>Major de facto standard</td><td>None: opportunistic, heterogeneous, patchwork, bricolage</td><td>Via the ERP</td><td>ERP</td></tr><tr><td>Major integration tools</td><td>Software bridges</td><td>ERP and Software bridges</td><td>ERP and EAI</td></tr><tr><td>Major integration focus/scope</td><td>Within functions</td><td>Intra firm</td><td>Intra firm and limited inter firm</td></tr></table>

![](/api/attachments/QPF5RBNS/fulltext/images/17e31b63a6d9acea3ff598bff0308728d413c4b5cca9c8a0bce601e18ad80e8a.jpg)  
Figure 4 Mixed architecture.

## Discussion

We first compare the three clusters of IS architectures for these SMEs (see Table 8) and then examine the findings in light of each of the initial research questions. Given the elements forming the IT architecture types (Table 8), we can now interpret these connecting them with the social and organizational context (Star & Ruhleder, 1996).

## Interpretation of the three clusters in terms of IS architecture

The first form, Silos Architecture, is characterized by (1) having multiple unrelated databases, that are not united by a common data model; (2) integration is effectively the interoperability arising from the building of software bridges and interfaces (APIs); and, (3) similarly, the tools enabling any interconnection are these software bridges.

We see two ways to interpret why firms exhibit this type of architecture. The first, suggested directly by the data, is that these firms are not particularly young; that is, the age of the firm is not a discriminating factor. Their extant systems were started well before ERP alternatives for SMEs became available, and evolved over time. When the ERP alternative was made available, SME managers faced the decision of abandoning workable interoperable systems and having to allocate substantial new resources for an enterprise solution that they also understood to carry substantial risk of failure. The second interpretation comes from in-depth cases drawn from this sample and investigated and previously described (citation withheld during review). Strategically, firms did not want to integrate different business functions because they feared that such integration would risk disclosure of critical and survival threatening confidential information. To them, total integration simply did not make sense.

The second form, Partially Standardized Architecture wherein integration, is characterized by: (1) having some limited ERP implementation (single vendor only), which imposed de facto standards; (2) also having software bridges in addition to the ERP system, and; (3) achieving integration via the ERP and any additional software bridges. From the data, we know that these firms are both young and relatively small. Unlike the case of the Applications Silos, we attribute their acquisition of ERP systems to two things. The first is, for owners/managers, that ISs are neither a core competency nor their primary focus, and thus achieving integration as simply as possible is more appealing than building in house systems, and that the ERP opportunities were presented at the right time. As noted above, 80% of these firms used ERP with three or fewer modules. These firms commonly elected to exclude databases for R&D and customer identity data.

The third form, Mixed Architecture, is the most advanced with regard to IS architectural and systems integration because this organization type mixes EAI and ERP systems (Sharif et al, 2005). They are characterized by: (1) having common database models; (2) widespread use of an ERP system, with integration standards arising from the greater adoption of the ERP modules, and; (3) by combining ERP and EAI technologies in various ways (Khoumbati et al, 2006). This set of SMEs tends to be the larger firms in our sample. From our previous casework, we discovered that the primary IS issues these firms expressed were those dealing with operational efficiency and interoperability with certain privileged customers (citation removed during review). Because these firms wanted interoperability, flexibility and cost efficiencies, they chose to standardize around the ERP/EAI. They clearly understood the benefit of aligning the IT implementation with firm growth strategies.

Each of the three architectural types has an internal logic. That logic for the first, the silos architecture, is heavily influenced by the necessity of having working interoperable solutions. Despite the inroads made by ERP vendors in developing mid-market and smaller firm models for ERP implementation, in this data set the Silos Architecture type remains the dominant means of seeking a degree of interoperability, which justifies their understanding it as an integration approach. We conjecture that this is principally because managers want to control their own data, and/or also because adapting to an ERP solutions later remains too costly. In many of these firms, the principal application set was used for production management. Maintaining production control was the critical, and immediate, problem SMEs sought to address via the applications silos alternatives. The logic of the architectural second type, the Partially Standardized Architecture, is consistent observations made Applegate (2009 ICIS) where she found that 80% of the US firms she had studied considered IT integration essential. They sought to acquire and use standardized systems resources to increase levels of integration. Of special note is the fact that this architectural type is the only place in our study data in which we found the maturity curve suggested by Ross et al (2006). The logic of this third type has been described in the literature (c.f., Themistocleous et al, 2001; Themistocleous & Chen, 2004; Themistocleous & Irani, 2006) and in a case study developed by Sharif et al (2005). Being a member of this IT architectural type requires having the resources more typical to mid-size firms or large firms (Themistocleous & Chen, 2004 cited by Lam, 2005). While the firms in this cluster are larger than those firms belonging to the other two architectural types, the IT focus remains on interoperability and not the possibilities that might be afforded by having data warehouses and online analytical processing and data mining systems.

## Findings in light of the research questions

Finally, given our understanding of the data, and in light of our initial theoretical discussion above, we summarize the findings with regard to the initial research questions.

## Research Question 1: What are the main IS architectures found in SMEs?

Our taxonomy identifies three types of IT architectures and shows how they partially reflect their organizational SMEs context, and thus the IS architecture. The first two, Silos Architecture and Partially Standardized Architecture, are consistent with those described in the IT literature, particularly the work of Ross et al (2006). The third type has not been described in the earlier, large firm-derived, typologies. We further find that the cluster into which an organization falls is likely to be governed by the interaction of a set of demographic (the firms age and size) and environmental factors. The environment factors include firm history regarding IT development and when IT integration opportunities that fit the organizations strategy and architecture actually became available.

## Research Question 2: What kind of systems integration approaches are present in SMEs?

We found that in SMEs the systems integration approaches were different from the mainstream typologies and idealized models representing large firm integration approaches, as described in Table 2. The first difference was that data warehousing was found to be largely irrelevant by this study set. We posit that this might be the case because in order to benefit from data warehousing, technologies require a certain reflexivity, sophistication and focus on continuous analysis with respect to historical data. It requires that they have to capture data in some organized and systematic fashion and have to mature towards obtaining strategic value from the ERP by system by adding complementary information (Holland & Light, 2001). This is a luxury few SMEs can afford. The second difference is that for these firms the primary goal is to have some measure of interoperability. It is the goal of operational interoperability that drives the evolution of the architecture and not some ideal of architectural integration. While the maturity model suggested by Holland & Light (2001) presents the ERP as the de facto (and becoming) standard, the Partially Standardized Architecture is closer to becoming a dominant existing form at least with these SMEs. While it includes an ERP. this form nevertheless also includes the software bridges, which, in a way, allow for the necessary business responsiveness and data protection.

For this set of firms, it was clear that for them the immediate goal of interoperability prevailed over fuller, and more formal, system integration. Comparing the three IT architectures and IS systems integration types, the most common means for approaching any form of integration is via the construction of software bridges and interfaces. Given that Ross and Markus essentially disregarded the Software bridge/interface/API as a legitimate form of integration in the domain of the large organization, the fact that the software bridge approach dominates in the domain of the SME flies in the face of the canonical view. Let us be quite clear that the means of achieving interoperability essentially discarded as an artifact of the past and of poor and unsustainable practice for the large organization remains the principle means of achieving some interoperability in the case of this set of small organization.

## Conclusion

Following the challenge made by Orlikowski & Iacono (2001), this research takes the IT artifact seriously and provides a taxonomy of IS architectures and systems integration. Having examined how these architectural and systems integration forms arise in the SME and not the domain of the large-scale enterprise allowed us to propose that the typologies arising from studies of large firms are not universally applicable to all firms. In the process, we believe that we have also contributed to theory development via a clarification of nomenclature definitional confusion around the term ‘IS architecture’ and of the many different definitions related to the ‘architectural’ construct. In addition, the results suggest reasons why architectures are not more integrated than we might have expected. Related to the practice of maintaining an IT portfolio, this research also implies that an IS manager adding IS resources must be aware of the type of IS architecture in place. New IS resources must be compatible and not be in conflict with the existing ecological infrastructure and extant systems integration approach.

However, there are several limitations inherent in this study. First, surveys on enterprise integration architectures are rare, particularly in the arena of the SMEs. Therefore, as a first stab at describing and understanding IS architectures and systems integration typologies in the SME, we had to adjust to surprises encountered at each step of the process. In the past, we have been accused of being too enamored of the new technological alternatives for enterprise integration and, like most others, we had ‘bought into’ the inevitability of how firms would climb the sophistication and integration technologies ladder (c.f., Ross et al, 2006, p. 72, Figure 4–1). Therefore, we were rather surprised by our own findings; namely, that the SME has slightly different goals and perspectives, the emphasis on interoperability and not the technology of how. Whereas others (e.g. Ross and Markus) discount APIs as a ‘legitimate’ integration approach, the SMEs are fine with this alternative if it provides results at low cost.

Second, this is the first study of this type examining French firms. It has been 9 years since our initial study, and despite other work in this domain we find that some of the items that we tested have not been asked in follow on surveys. For instance, we have examined data from other (and newer) surveys examining how French firms equip themselves with ERP, in-house software solutions or other specialized packages, but those surveys do not ask respondents to describe the ways these solutions are integrated and whether there is any significant interoperability. Therefore, we hold that our data set and findings are unique and cover items not dealt with elsewhere in empirical studies. We make no claim that the French SME is unique among SMEs, nor do we know of substantive cultural differences that would prohibit theoretical generalization from these findings (Lee & Baskerville, 2003). These firms are, nonetheless, drawn from a single cultural backdrop, and because of the data we collected we are able to describe that context in some detail.

Third, our convenience sample targeted the mid-size market of SMEs, and thus we note that the mean firm size of our sample may exhibit a sample biased toward the large–medium size firms rather than the very small firm. And fourth, there are suggestions that BI (business intelligence), web services (Puschman & Alt, 2005), cloud computing and ‘The Grid’ may be making inroads even into the domain of the SME. Given that the study conducted in 2002 before the widespread availability of BI tools, Service Oriented Architectures, web services, cloud computing and grid computing within the firm, software as a service (SaaS) and so on, we have no way to test that proposition with this data set. Given that other propositions drawn from the world of large firms do not apply with out adjustment to the domain of the SME, the only way we will know for sure is via further study. However, this question led us to seek further insight in the literature as well and from colleagues at recent conferences. Two relatively recent articles examine SMEs and EDI use (Khazanchi, 2005) or SaaS as an outsourcing solution (Benlian, 2009). Both articles discuss the problems of risk adversity toward ITs and of environmental uncertainty that causes the SMEs to hold back on adoption. So, we conclude that although there is speculation that the SME such as the larger firms ought to be adopting the newer, closer-to-the-bleeding-edge technologies, our research, our reading and our inquiries do not find evidence that this is so.

In general, for SMEs, the use of IS tends to be operational in nature and focus rather than on the strategic. For those firms that did have explicit integration strategies, typically the larger and older firms, we intuited a much higher degree of strategic alignment between the IS function and firm-level strategy, but even in these firms the pragmatic aspect of interoperability ruled the day. We think that empirical follow-up work is required to test this question. A related issue would be to identify possible paths from one type of architecture to another. That is, to answer the question: does a maturity curve exist for these organizations? Do firm strategies become more complex and sophisticated as they get older and larger, or, are there operational and environmental factors that play more important roles in the process? It also would have been interesting to have a complementary survey accessing the leadership role to see how this could influence architecture and enterprise architecture choices. One of the most intriguing questions that we have yet to address, one hinted at in this research, is the issue of why implementing an ERP may not lead to greater application and organizational level integration. Finally, although we think that these findings can be meaningful in the EU as a whole, the study was drawn from a set of regional French firms. However, current reports from the European commission suggest that the case of the small enterprise in France is typical throughout the European Union; and since the SME is a formidable and important economic force across the globe, it is our hope that these findings may be of general interest to managers both inside the domain of the European Union and outside Europe as well.

## About the authors

Marc Bidan is a Professor of Information Systems at Polytech Nantes, the Graduate School of Engineering of the University of Nantes, France. Since 2011, he is the President of the French-speaking academic Association Information and Management (AIM). He obtained his Ph.D. from the University of Nantes and was a Professor at the University of La Rochelle and at the University of Angers. He is a member of the LEMNA (Laboratoire d’Economie et de Management de Nantes Atlantique). His research interests include enterprise systems and enterprise architectures. His work in these areas has been published in journals such as Syste\`mes d<sup>0</sup>Information et Management, Revue Franc¸aise de Gestion, and presented in several conferences such as ICIS, ECIS or ICEIS.

Frantz Rowe has been serving as a Professor, and as a CIO and an Advisor to the president, at the Institute of Economics and Management de Nantes (IEMN-IAE) of the University of Nantes, France, since 1995. He is a Researcher at LEMNA and at SKEMA Business School. He earned an M.S. from the University of California, Berkeley, and a Ph.D. from the University of Paris-Nanterre. His research on IS-enabled organizational transformation (ERP dynamics, call centers – including shared or virtual – and electronic marketplaces) has appeared in Information Systems Journal, Journal of Information Technology, Data Base, Accounting, Management and Information Technologies,

## References

A<sup>´</sup>CS Z, BOSMA N and STERNBERG R (2008) The entrepreneurial advantage of world cities: evidence from global entrepreneurship monitor data. Jena Economic Research Papers, 2008–063.

A<sup>´</sup>CS Z and SZERB L (2009) The global entrepreneurship index (geindex). Foundations and Trends<sup>s</sup> in Entrepreneurship 5(5), 341–435.

ADMIRAAL W, DE LAAT M, RUBENS W and LALLY V (2003) ICT support for workplace learning: eLearning in small and medium enterprises (SMEs), In Online Book of Abstracts of the European Conference on Educational Research. [WWW document] http://www.eera-ecer.eu/.

ALDENFERDER M and BLASHFIELD R (1984) Cluster analysis. In Sage University Series: Quantitative Applications in the Social Sciences (LEWIS-BECK M, Ed), Vol. 44, Sage, Newbury Park, CA, 88pp.

AVITAL M and VANDENBOSCH B (2000) Sap implementation at metalica: an organizational drama. Journal of Information Technology 15(3), 665– 673.

BALLANTINE J, LEVY M and POWELL P (1998) Evaluating information systems in small and medium-sized enterprises: issues and evidence. European Journal of Information Systems 7(4), 241–251.

BENIGER JR (1986) The Control Revolution: Technological and Economic Origins of the Information Society. Harvard University Press, Cambridge, MA.

BENLIAN A (2009) A transaction cost theoretical analysis of software-as-aservice (SaaS)-based sourcing in SMBs and enterprises. In European Conference on Information Systems (MARCO MD, LOEBBECKE C and WILLCOCKS L, Eds), Paper ECIS2009-0003.R1, pp 1–13, ECIS 17, Verona Italy.

BENSAOU B and VENKATRAMAN N (1995) Configurations of interorganizational relationships: a comparison between U.S. and Japanese automakers. Manggement Science 41(9). 1471–1492.

BESSON P and ROWE F (2001) ERP project dynamics and enacted dialogue: perceived understanding, perceived leeway, and the nature of taskrelated conflicts. Database for Advances in Information Systems 33(4), 47-66.

Journal of Global Information Management, Journal of Decision Systems, Transportation Research, Technological Forecasting and Social Change, IEEE Transactions on Engineering Management, ISDN Networks and Computer Systems and MIS Quarterly. He has served Syste\`mes d’Information et Management as editor-in-chief for 13 years, and as the cochair of ICIS 2008 in Paris, with Dov Te’eni.

Duane Truex holds a joint appointment in the CIS department of Georgia State University’s J. Mack Robinson College of Business and in its Institute of International Business. He is the Program Director for the GSU’s University of Nantes (France) Academic Exchange program. A former Leverhulme Fellow in England, Truex currently holds academic affiliations with the Mid Sweden University (Sundsvall Sweden) and the University of Nantes (France). His research explores the social impacts of information systems (IS) on organizational stakeholders, how emergent organizations properties are reflected in enterprise architectures and IS research methods, and the nature of scholarly influence. He has published 90 peer-refereed works in journals, IFIP, ACM and IEEE transactions, books and proceedings. He is active in the IFIP working groups 8.2 and 8.6 research communities and has served as program chair, track chair or doctoral consortia co-chair of several major international conferences including the (ICIS) 2008-Paris.

BLILI S and RAYMOND L (1993) Information technology: threats and opportunities for small and medium-sized enterprise. International Journal of Information Management 13(6), 439–448.

BOH WF and YELLIN D (2006) Using enterprise architecture standards in managing information technology. Journal of Management Information Systems 23(3), 163–207.

BOH WF, YELLIN D, DILL B and HERBSLEB J (2003) Effectively managing information systems architecture standards: an intra-organizational perspective. In Standard Making: A Critical Research Frontier for Information Systems, MISQ Special Issue Workshop, Pre-conference workshop for International Conference on Information Systems (KING J and LYYTINEN K, Eds), pp 12–14, ICIS 2003, Seattle, Washington.

BRANCHEAU JC and WETHERBE J (1986) Information architectures – methods and practice. Information Processing & Management 22(6), 453–463.

BUONANNO G, FAVERIO P, RAVARANI A, SCIUTO D and TAGLIAVINI M (2005) Factors affecting ERP system adoption, a comparative analysis between SMEs and large companies. Journal of Enterprise Information Management 18(5), 384–426.

CHALMETA R, CAMPOS C and GRANGEL R (2001) Reference architectures for enterprise integration. Journal of Systems and Software 57(3), 175-191

CHENEY PH and KASPER GM (1993) Responding to world competition: developing the global is professional. Journal of Global Information Management 1(1), 21–31.

COLOMB RM and ORLOWSKA ME (1995) Interoperability in informationsystems. Information Systems Journal 5(1), 37–50.

CORNELIUSSEN MS (2008) It architecturing: reconceptualizing current notions of architecture in is research. In 16th European Conference on Information Systems (GOLDEN W, ACTON T, CONBOY K, VAN DER HEIJDEN H and TUUNAINEN VK, Eds) CD-ROM, Galway, Ireland.

DAVENPORT T (2005) The coming commoditization of processes. Harvard Business Review 83(6). 100–108.

DUHAN S, LEVY M and POWELL P (2001) Information systems strategies in knowledge-based SMEs: the role of core competencies. European Journal of Information Systems 10(1), 25–40.

EUROPEAN COMMISSION (2003) Recommandation 2003/361/EC. [WWW document] http://ec.europa.eu/enterprise/policies/.

EVERITT BS (1993) Cluster Analysis. Heinemann, London.

FARRELL J and SALONER G (1985) Standardization, compatibility, and innovation. R Journal of Economics 16(1), 70–83.

FINKELSTEIN C (1989) An Introduction to Information Engineering: From Strategic Planning to Information Systems. Addison-Wesley, New York.

GERDIN J (2005) Management accounting system design in manufacturing departments: an empirical investigation using a multiple contingencies approach. Accounting, Organizations and Society 30(2), 99–126.

GIACHETTI R (2004) Enterprise integration: an information integration perspective. International Journal of Production Research 42(6), 1147-1166

GIACHETTI R, ARTETA BM and NUNEZ AN (2003) An assessment of enterprise integration approaches and technologies. In 17th International Conference on Production Research, Blacksburg, VA.

GOLDING P, DONALDSON OA, TENNANT VM and BLACK K (2008) An analysis of factors affecting the adoption of ICT by SMEs in rural and urban Jamaica. In 16th European Conference on Information Systems (GOLDEN W, ACTON T, CONBOY K, VAN DER HEIJDEN H and TUUNAINEN VK, Eds) CD-ROM. Galway. Ireland

GOLDKUHL GL and LYYTINEN K (1984) Information system specification as rule reconstruction. In Beyond Productivity: Information Systems Development for Organizational Effectiveness (BEMELMANS TMA, Ed), pp 79–95, Elsevier Science Publishers, North-Holland, Amsterdam.

GOMAA H (1995) Reusable software requirements and architectures for families of systems. Journal of Systems & Software 28(3), 189–202.

GRu¨NBACHER P, EGYED A and MEDVIDOVIC N (2004) Reconciling software requirements and architectures with intermediate models. Software & Systems Modeling 3(3), 235–253.

HAIR JF, ANDERSON RE, TATHAM RL and BLACK WC (1998) Multivariate Data Analysis. Prentice-Hall, Englewood Cliffs, NJ.

HAMILTON D (1999) Linking strategic information systems concepts to practice: systems integration at the portfolio level. Journal of Information Technology 14(1), 69–82.

HOLLAND C and LIGHT B (2001) A stage maturity model for ERP systems use. Database for Advances in Information Systems 32(2), 34–45.

HUIN SF (2004) Managing deployment of ERP systems in SMEs using multiagents. International Journal of Project Management 22(6), 511–517.

IRANI Z, THEMISTOCLEOUS M and LOVE PED (2003) The impact of EAI on information system lifecycles. Information and Management 41(2), 177-18Z.

KHAZANCHI D (2005) Information technology (IT) appropriateness: the contingency theory of ‘fit’ and IT implementation in small and medium enterprises. Journal of Computer Information Systems 45(3), 88–95.

KHOUMBATI K, THEMISTOCLEOUS M and IRANI Z (2006) Evaluating the adoption of enterprise application integration in health-care organizations. Journal of Management Information Systems 22(4), 69–108.

KRUCHTEN P (1996) Software architecture-a rational metamodel. In SIGSOFT 96 Workshop (WOLF A, FINKLESTEIN A, SPANOUDAKIS G and VIDAL A, Eds), pp 5–7, ACM, San Francisco CA U.S.A.

LAM W (2005) Investigating success factors in enterprise application integration: a case-driven analysis. European Journal of Information Systems 14(2), 175–187.

LAMARCHE PA, BEAULIEU MD, PINEAULT R, CONTANDRIOPOULOS AP, DENIS JL and HAGGERTY J (2003) Choices for change: the path for restructuring primary healthcare services in Canada. A report delivered to the Saskatchewan Department of Health, the Ministe\`re de la sante´ et des services sociaux du Ouébec and Health Canada.

LAPKIN A (2004) Architecture Frameworks: How to Choose Architecture Frameworks: Some Options. Gartner, New York.

LAUKKANEN S, SARPOLA S and HALLIKANEM P (2005) ERP system adoption: does the size matter? In 38th Hawaii International Conference on System Sciences (SPRAGUE RH, Ed), 3–6 January, p 226b, HICSS, Big Island, Hawaii.

LEBART L, MORINEAU A and WARWICK KM (1984) Multivariate Descriptive Statistical Analysis: Correspondence Analysis and Related Techniques for Large Matrices. John Wiley & Sons, New York.

LEE AS and BASKERVILLE R (2003) Generalizing generalizability in information systems research. Information System Research 14(3), 221–243.

LIGHT B (2005) Potential pitfalls in packaged software adoption. Communications of the ACM 48(5), 119–121.

LIGHT B, HOLLAND CP and WILLS K (2001) ERP and best of breed: a comparative analysis. Business Process Management Journal 7(3), 216.

LUCKHAM DC and VERA J (1995) An event-based architecture definition language. IEEE Transactions on Software Engineering 21(9), 717–734.

MARKUS ML (2000a) Toward an integrated theory of IT-related risk control. In Organizational and Social Perspectives on Information Technology (BASKERVILLE R, STAGE J and DEGROSS J, Eds), pp 167–178, Kluwer Academic Publishers, London.

MARKUS ML (2000b) Paradigm shifts – e-business and business/systems integration. Communications of the Association for Information Systems: Vol. 4, Article 10. [WWW document] http://aisel.aisnet.org/cais/Vol4/iss1/10.

MARKUS ML (2001) Reflections on the systems integration enterprise. Business Process Management Journal 7(3), 1–9.

MARKUS ML and TANNIS C (2000) The enterprise system experience: from adoption to success. In Framing the Domains of I.T. Management (ZMUD, R, Ed), pp 173–208, Pinnaflex, Cincinnati.

MARTIN J (1986) Information Engineering. Savant, Camforth, UK.

MEDVIDOVIC N and TAYLOR RN (2000) A classification and comparison framework for software architecture description languages. IEEE Transactions on Software Engineering 26(1), 70–93.

NIEDERMAN F, BRANCHEAU JC and WETHERBE JC (1991) Information systems management issues in the 1990s. MIS Quarterly 15(4), 477–499.

ORLIKOWSKI WJ and IACONO CS (2001) Research commentary: desperately seeking the ‘It’ In it research – a call to theorizing the it artifact. Information Systems Research 1(2), 121–134.

PARNAS D (1972) A technique for software module specification with examples. Communications of the ACM 15(5), 330–336.

PERISTERAS V and TARABANIS K (2000) Towards an enterprise architecture for public administration using a top-down approach. European Journal of Information Systems 9(4), 252–260.

PORTER ME (1985) Competitive Advantage. Free Press, New York.

POSTMAN N (1988) Conscientious Objections: Stirring Up Trouble About Language, Technology and Education. Vintage Books, New York.

PUSCHMANN T and ALT R (2005) Developing an integration architecture for process portals. European Journal of Information Systems 14(2), 121–134.

ROHLOFF M (2005) Enterprise architecture – framework and methodology for the design of architectures in the large. In ECIS 2005 Information Systems in a Rapidly Changing Economy. Paper 113, European Conference on Information systems, Regensburg, Germany.

ROHLOFF M (2008) Framework and reference for architecture design. In AMCIS 2008 Proceedings (PARSONS J and YUAN Y, Eds) Paper 118, AIS, Toronto.

ROSS J, WEILL P and ROBERTSON J (2006) Enterprise as Strategy. Harvard Business School Press, Cambridge, MA.

ROSS JW (2003) Creating a strategic it architecture competency: learning in stages. MIS Quarterly Executive 2(1), 31–44.

ROWE F, ELAMRANI R, BIDAN M, MARCINIAK R and GEFFROY-MARONNAT B (2005) Does ERP provide a cross-functional view of the firm? Challenging conventional wisdom for SMEs and large French firms. In ICIS 2005 Forever New Frontiers (A D and G D, Eds) Association of Information Systems, Las Vegas, NV.

ROWE F and STRUCK D (1999) Cultural values, media richness and telecommunication use in an organization. Accounting Management and Information Technologies 9(3), 161–192.

SAMBAMURTHY V and ZMUD RW (2000) Research commentary: the organizing logic for an enterprise’s it activities in the digital era – a prognosis of practice and a call for research. Information Systems Research 11(2), 105–114.

SAP ANNUAL REPORT (2006) SAP-AG. Online at www.sap.com/investor.

SCAVO F (2007) Gartner retires mid-market ERP magic quadrant. The Enterprise System Spectator, 1 April. [WWW document] http://fscavo .blogspot.com/2007/01/gartner-retires-mid-market-erp-magic.html.

SHARIF AM, IRANI Z and LOVE PED (2005) Integrating ERP using EAI: a model for post-hoc evaluation. European Journal of Information Systems 14(2), 162–174.

SHARMA S (1996) Applied Multivariate Techniques. John Wiley & Sons, New York.

S K, R M and P S (2008) Software architectures: blueprint, literature, language or decision. European Journal of Information Systems 17(6), 575–588.

SOWA JF and ZACHMAN JA (1992) Extending and formalizing the framework for information systems architecture. IBM Systems Journa 31(3), 590–616.

STAR SL and RUHLEDER K (1996) Steps toward an ecology of infrastructure: design and access for large information spaces. Information Systems Research 7(1), 111–134.

SUSMAN G (2007) Small and Medium-Sized Enterprises and the Global Economy. Edward Elgar Publishing, Northampton, MA.

THEMISTOCLEOUS M and CHEN H (2004) Investigating the integration of SMEs’ information systems: an exploratory case study. International Journal of Information Technology and Management 3(2/3/4), 208–234.

THEMISTOCLEOUS M and IRANI Z (2006) Towards a methodology for the development of integrated IT infrastructures. Proceedings of the 39th Hawaii International Conference on System Sciences, Hawaii.

THEMISTOCLEOUS M, IRANI Z and O’KEEFE RM (2001) ERP and application integration: exploratory survey. Business Process Management Journa 7(3), 195–204.

TRACTINSKY N and JARVENPAA SL (1995) Information systems design decisions in a global versus domestic context. MIS Quarterly 19(4), 507–529.

TRUEX D (2001) ERP systems as facilitating and confounding factors in corporate mergers: the case of two Canadian telecommunications companies. Systemes d’Information et Management 1(6), 7–21.

TRUEX D and NGWENYAMA O (2000) ERP systems: Facilitating or confounding factors in corporate telecommunications mergers? In ECIS 2000 a Cyberspace Odyssey (HANSEN HR, BICHLER M and MAHRER H, Eds), pp 645–651, ECIS 2000, Wirtschaftsunversita¨t Wien Vienna University of Economics and Business Administration.

VAN EVERDINGEN Y, VAN HILLGERSBERG J and WAARTS E (2000) ERP adoption by European midsize companies. Communications of the ACM 43(4), 27–31.

XU L and BRINKKEMPER S (2007) Concepts of product software. European Journal of Information Systems 16(5), 531–541.

ZACHMAN J (1997) Enterprise architecture: the issue of the century. Database Programming and Design 10(3), 44–53.

## Correction

A number of proofing corrections were not included in the HTML version of this article, originally published 27 March 2012. These corrections have been made in this final version.

## Appendix

Table A1 Research instrument: constructs, possible item values and core notions

<table><tr><td></td><td>Possible item values</td><td>Core notion and reference authors</td></tr><tr><td colspan="3">A. Contextual items</td></tr><tr><td>1 What is the number of employees in your firm?</td><td>30–100 or 101–500 or &gt;500</td><td>Pragmatic classification based on ERP vendor and EU Commission recommendations (Themistocleous &amp; Chen, 2004)</td></tr><tr><td>2 What is the main activity in your firm?</td><td>Agriculture or manufacturing or services</td><td>A classical distinction still appropriate</td></tr><tr><td>3 What is your main organizational type?</td><td>Functional-oriented or project-oriented or others</td><td>Blili &amp; Raymond (1993) SME and IT Systems. Applies in most developing countries, China and India, and also in many regions of the Western economy.</td></tr><tr><td>4 What is the age of your firm?</td><td>&lt;5 or 5–10 or &gt;10 years</td><td>Blili &amp; Raymond (1993) as above</td></tr><tr><td colspan="3">B. Technological items</td></tr><tr><td>5 How many vendor ERP packages have you implemented in your firm?</td><td>0 or 1 or &gt;1</td><td>Packaged software (Light, 2005; Xu &amp; Brinkkemper, 2007)</td></tr><tr><td>6 How many ERP modules of the same package have you implemented in your organization?</td><td>1–3 or 4–8 or &gt;8</td><td>Modules (Parnas, 1972; Markus, 2001)</td></tr><tr><td>7 Have you implemented any ‘support function’ type ERP module?</td><td>Yes or No answer</td><td>Porter (1985) core vs support function; Rowe et al (2005) Core module vs support module</td></tr><tr><td>8 Have you implemented any ‘core function’ type ERP module?</td><td>Yes or No or No answer</td><td>Same as above</td></tr><tr><td>9 How many legacy systems do you have in your organization?</td><td>1–3 or 4–8 or &gt;8</td><td>Notion of legacy systems as ‘spaghetti’ confounding later development (Markus &amp; Tannis, 2000; Sharif et al., 2005)</td></tr><tr><td>10 Do you have any non-ERP support applications programs in your organization?</td><td>Yes or No or No answer</td><td>Porter (1985) core vs support function; Rowe et al, 2005 Core module vs support module</td></tr><tr><td>11 Do you have any non-ERP core applications program in your organization?</td><td>Yes or No or No answer</td><td>Same as #10 above</td></tr><tr><td>12 Do you have a common logical database for MIS?</td><td>Yes or No or No answer</td><td>Themistocleous et al, 2001</td></tr><tr><td>13 Do you have a common IS nomenclature for the firm? Data structure</td><td>Yes or No or No answer</td><td>Data structure (Goldkuhl &amp; Lyytinen, 1984; Golding et al, 2008)</td></tr><tr><td>14 Do you use an EAI platform for MIS?</td><td>Yes or No or No answer</td><td>Markus, 2001; Themistocleous et al, 2001; Lam, 2005</td></tr><tr><td>15 For you are your information systems satisfactorily integrated?</td><td>Yes or No or No answer</td><td>Themistocleous et al, 2001, Lam, 2005</td></tr></table>
