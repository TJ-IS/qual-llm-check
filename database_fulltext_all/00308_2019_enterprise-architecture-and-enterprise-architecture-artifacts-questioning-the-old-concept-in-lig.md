---
otero_id: 308
otero_key: "V5U75PGR"
title: "Enterprise architecture and enterprise architecture artifacts: Questioning the old concept in light of new findings"
authors: "Svyatoslav Kotusev"
year: "2019"
journal: "Journal of Information Technology"
doi: "10.1177/0268396218816273"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research Paper

# Enterprise architecture and enterprise architecture artifacts: Questioning the old concept in light of new findings

Svyatoslav Kotusev

Journal of Information Technology 1–27 © Association for Information Technology Trust 2019 Article reuse guidelines: sagepub.com/journals-permissions https://doi.org/10.1177/026839621881627DOI: 10.1177/0268396218816273 Journals.sagepub.com/jinf SAGE

## Abstract

Enterprise architecture is a description of an enterprise from an integrated business and IT perspective intended to bridge the communication gap between business and IT stakeholders and improve business and IT alignment. Enterprise architecture consists of multiple different artifacts providing certain views of an organization and the available enterprise architecture literature offers a number of comprehensive lists of artifacts that can be used as part of an enterprise architecture practice. However, these lists of enterprise architecture artifacts were never validated empirically and the practical usage of different artifacts still remains largely unexplored. Based on a comprehensive empirical analysis of enterprise architecture artifacts used in 27 diverse organizations, this study identifies the list of 24 common artifacts that proved useful in practice and describes in detail their usage and purpose. Although this study does not attempt to theorize on the findings, it makes a significant empirical contribution to the enterprise architecture discipline. In particular, this study (1) provides the first consistent list of enterprise architecture artifacts that actually proved useful in organizations, (2) offers the first available systematic description of their usage, (3) questions the common view of enterprise architecture as a set of business, information, applications and technology architectures and (4) questions the widely accepted conceptualization of enterprise architecture as a set of the current state, future state and transition roadmap. This study provides compelling empirical evidence in favor of reconceptualizing enterprise architecture and calls for further research in this direction.

## Keywords

Enterprise architecture, artifacts, list, usage, reconceptualization, case studies

## Introduction

The upcoming epoch of digital business transformation forces organizations to rethink their attitude toward IT (Keen & Williams, 2013; Weill & Woerner, 2018b; Westerman & Bonnet, 2015). Latest developments in IT are not only changing existing business models but also constantly create new opportunities for the business of many companies (Ross et al., 2016; Weill & Woerner, 2013b; Westerman, Bonnet, & McAfee, 2014). These tectonic shifts in the competitive market environment related to digitization increase the importance of achieving closer business and IT alignment in organizations (Li, Liu, Belitski, Ghobadian, & O’Regan, 2016). Unsurprisingly, the problem of alignment consistently tops among the most critical concerns of IT executives (Kappelman, McLean,

Johnson, & Gerhart, 2014; Kappelman, McLean, Johnson, & Torres, 2016; Kappelman et al., 2017). Enterprise architecture (EA) is a description of an enterprise from an integrated business and IT perspective intended to bridge the communication gap between business and IT stakeholders and improve business and IT alignment.

EA consists of multiple individual documents typically called as EA artifacts (Kotusev, Singh, & Storey, 2015b; Niemi & Pekkola, 2017; Winter & Fischer, 2006). These EA artifacts describe various aspects of EA and can be very diverse in nature and range from high-level principles (Greefhorst & Proper, 2011) to low-level technical diagrams (Lankhorst, 2013). Popular EA sources (Bernard, 2012; The Open Group Architecture Framework (TOGAF), 2011; van’t Wout, Waage, Hartman, Stahlecker, & Hofman, 2010) offer recommended lists of \~30–80 different EA artifacts that can be created as part of an EA practice. A number of taxonomical EA frameworks have been proposed to organize and structure these EA artifacts (Schekkerman, 2006; Sowa & Zachman, 1992). The EA literature (Bernard, 2012; Federal Enterprise Architecture (FEA), 2001) also suggests that EA artifacts should describe the current state of an organization, the desired future state of an organization and a roadmap for transition between them, and conceptualizes EA accordingly (Lange, Mendling, & Recker, 2016).

However, none of the EA sources providing comprehensive lists of EA artifacts (Bernard, 2012; Department of Defense Architecture Framework (DoDAF), 2007; Spewak & Hill, 1992; TOGAF, 2011; van’t Wout et al., 2010) gives a clear explanation of how exactly these EA artifacts should be used after being developed. Moreover, all the popular EA publications recommending specific lists of EA artifacts, proposing frameworks for organizing them and defining the highest level structure of EA as a set of current states, future states and roadmaps are prescriptive in nature and authored by fashion-setters, that is, consultancies, industry experts and gurus (Abrahamson, 1991, 1996; Gibson & Tesone, 2001; Kieser, 1997). At the same time, a comprehensive review of the available EA literature (Kotusev, 2017b) demonstrates that the prescriptions of these EA publications were generally taken for granted as useful and valid, but never questioned and actually validated empirically.

Consequently, at the present moment the available EA literature neither provides an empirically validated list of EA artifacts that proved useful in practice nor explains how exactly these EA artifacts are actually used in organizations. This deficiency prevents EA scholars from studying an EA practice at the more detailed level of individual EA artifacts. Moreover, the existing uncertainty around EA artifacts and their usage also leaves the practical applicability of taxonomical EA frameworks and even the validity of the higher level conceptualization of EA as the current state, future state and roadmap essentially unconfirmed.

The problem of the inadequate understanding of EA artifacts and their practical usage, though acknowledged by EA researchers (Kotusev et al., 2015b; Niemi & Pekkola, 2017), still received little attention in the EA literature. In order to address this longstanding deficiency of the basic information on EA artifacts, this study answers the following research question: “What EA artifacts are used in organizations and how they are used?”

Importantly, this study does not intend to develop any new theories, but rather to make an empirical contribution to the EA discipline (Agerfalk, 2014; Avison & Malaurent, 2014; Hambrick, 2007), that is, to provide “a novel account of an empirical phenomenon that challenges existing assumptions about the world or reveals something previously undocumented” (Agerfalk, 2014, p. 594). This article is deliberately “atheoretic” (Miller, 2007) and belongs to “theory light” papers, that is, to papers “where theory plays no significant part in the paper and the contribution lies elsewhere, for example, new arguments, facts, patterns or relationships” (Avison & Malaurent, 2014, p. 327). These papers “might be rich qualitative descriptions of important but unexplored phenomena that, once described, could stimulate the development of theory and other insights” (Hambrick, 2007, p. 1350).

This article continues as follows: (1) I discuss EA artifacts and their organization, conceptualization of EA, associated problems and the motivation for this research; (2) I describe the research design, data collection and analysis procedures; (3) I present the resulting list of EA artifacts identified in organizations and describe their practical usage; (4) I discuss the findings of this study from the perspective of the current EA literature; (5) I explain the empirical contribution of this study to the EA discipline; (6) I discuss the limitations of this study; and (7) I conclude the article and outline directions for future research.

## Literature review

In this section, I will discuss EA artifacts and their organization, high-level conceptualization of EA, problems related to EA artifacts and then explain the motivation for this study.

## EA artifacts

An EA artifact is a descriptive document providing a specific view of an organization from the perspective of its business and IT (Abraham, 2013; Bischoff et al., 2014; Kotusev et al., 2015b; Niemi & Pekkola, 2017; Winter & Fischer, 2006). EA artifacts are the most basic underlying components of EA, while EA can be considered simply as a collection of diverse EA artifacts. However, different EA sources recom mend different sets of EA artifacts to be developed as part of an EA practice. For example, Spewak and Hill (1992) provide more than 50 diverse EA artifacts aligned to the steps of the prescribed EA methodology (planning initiation, business modeling, current systems and technology, data architecture, applications architecture, technology architecture and migration plans). DoDAF (2007) describes 29 different EA artifacts aligned to the operational, services, technical standards and “all” views. van’t Wout et al. (2010) recommend more than 80 EA artifacts aligned to five aspect areas: contextual, business, information, information systems and technology infrastructure. TOGAF (2011) describes more than 50 EA artifacts and deliverables aligned to the phases of the recommended architecture development method (ADM). Finally, Bernard (2012) lists 46 EA artifacts aligned to eight different domains (strategic goals and initiatives, business products and services, data and information, systems and applications, networks and infrastructure, security, standards and workforce). Therefore, various EA sources provide comprehensive lists of EA artifacts that may be created to practice EA.

## Organizing EA artifacts

An EA framework can be defined as “a logical structure for classifying and organizing the descriptive representations of an Enterprise [i.e. EA artifacts] that are significant to the management of the Enterprise as well as to the develop ment of the Enterprise’s systems” (Zachman, 1996, p. 2). A number of various taxonomical EA frameworks have been proposed by different authors for organizing EA artifacts (Connor, 1988; Partnership for Research in Information Systems Management (PRISM), 1986; Pulkkinen, 2006; Schekkerman, 2006; Sowa & Zachman, 1992; Treasury Enterprise Architecture Framework (TEAF), 2000; van’t Wout et al., 2010; Wardle, 1984; Zachman, 1987). For example, Wardle (1984) initially proposed a taxonomy for organizing EA artifacts into 12 distinct categories according to four domains (data, applications, communications and technology) and three levels (conceptual, logical and design guidelines and boundaries). Then, the PRISM framework (PRISM, 1986) classified EA artifacts into 16 categories according to four domains (infrastructure, data, application and organization) and four types (inventory, principles, models and standards). The STRIPE matrix (Connor, 1988) organized EA artifacts into 15 categories according to five domains (business, data, application, technical environment and type of plan) and three planning levels (strategic, tactical and operational). Zachman (1987) and Sowa and Zachman (1992) argued that EA artifacts should be classified into 30 categories according to five abstraction levels (planner, owner, designer, builder and subcontractor) and six interrogatives (what, how, where, who, when and why). However, most proposed EA frameworks (Connor, 1988; Federal Enterprise Architecture Framework (FEAF), 1999; PRISM, 1986; Pulkkinen, 2006; Schekkerman, 2006; TOGAF, 2011; Technical Architecture Framework for Information Management (TAFIM), 1996; TEAF, 2000; van’t Wout et al., 2010) in some or the other form classify all EA artifacts into four typical EA domains: business, information, applications and technology.

## Conceptualization of EA

EA at the highest level, as a collection of diverse EA artifacts, is typically conceptualized as a comprehensive description of the current state of an organization, a description of its desired future state and a roadmap for transition between these states (Bernard, 2012; FEA, 2001; Lange et al., 2016; Tamm et al., 2011; TOGAF, 2011). For instance, FEA (2001) states that “an enterprise architecture includes a baseline architecture, target architecture, and a sequencing plan” (p. 5). Joseph (2009) argues that “the essence of Enterprise Architecture is to document the current and future states of an enterprise and to institute a reasonable transition process from current to future state so that any enterprise can sustain in vibrant environment” (p. 9). Bernard (2012) even defines EA as “the analysis and documentation of an enterprise in its current and future states.” Accordingly, Lange et al. (2016) conceptualize EA as a set of as-is architecture, to-be architecture, transformation roadmap and principles. Therefore, the most widely accepted view of EA conceptualizes it as the current state, future state and transition roadmap.<sup>1</sup>

## Problems related to EA artifacts

A closer scrutiny of the recommended EA artifacts and related suggestions shows a number of highly alarming facts. First, most publications providing the lists of EA artifacts are purely prescriptive in nature, based only on anecdotal evidence and authored by fashion-setters, that is, consultancies, gurus and industry experts (Abrahamson, 1991, 1996; Gibson & Tesone, 2001; Kieser, 1997), none of them resulted from evidence-based research. At the same time, the available comprehensive research-based EA sources (Ahlemann, Stettiner, Messerschmidt, & Legner, 2012; Ross, Weill, & Robertson, 2006) do not offer specific lists of EA artifacts (a more detailed explanation of why these comprehensive sources do not answer the “simple” research question of this study is provided in Appendix A).

Second, a comprehensive review of the available EA literature (Kotusev, 2017b) shows that the anecdotal prescriptions of these publications have never been validated independently by researchers, but only generally assumed to be valid. Moreover, the EA literature does not provide any documented examples of successful EA practices based on the recommended sets of EA artifacts.

Third, most EA publications providing comprehensive lists of EA artifacts to be developed (Bernard, 2012; DoDAF, 2007; Spewak & Hill, 1992; TOGAF, 2011; van’t Wout et al., 2010) do not explain how exactly these EA artifacts should be used and do not describe their artifactspecific use cases, as if the sole purpose of all these EA artifacts is merely describing organizations from all possible viewpoints.

## Research question

The problems around EA artifacts described above suggest the existence of numerous open questions related to EA artifacts of significant importance for the whole EA discipline. In particular, currently it is still largely unclear (1) what EA artifacts proved useful in organizations, (2) how exactly these EA artifacts are used, (3) to what extent these EA artifacts overlap with the sets of EA artifacts prescribed by popular EA sources, (4) whether these EA artifacts can be actually organized as proposed by multiple taxonomical EA frameworks and (5) whether all these EA artifacts taken together resemble the most popular conceptualization of EA as the current state, future state and transition roadmap.

These uncertainties around EA artifacts significantly complicate, if not prevent, any in-depth studies of an EA practice and often “force” EA academics to make considerable unfounded assumptions in their research. For example, due to the absence of any empirically validated lists of EA artifacts that can be used as a reliable foundation for research, for their survey-based study of the utility of EA artifacts Bischoff, Aier, and Winter (2014) “arbitrarily” selected 26 EA artifacts recommended by TOGAF (2011) with no apparent justifications of their choice. More importantly, even the higher level conceptualization of EA as the current state, future state and transition roadmap used as the basis for survey-based studies, for instance by Lange et al. (2016), also cannot be traced to the underlying EA artifacts.

Therefore, the research question of this study can be formulated as follows: “What EA artifacts are used in organizations and how they are used?” A clear answer to this question will provide a sound foundation for further indepth studies of an EA practice and will also help assess the applicability of proposed taxonomical EA frameworks as well as the general validity of the most widely accepted high-level conceptualization of EA.

## Research design

This research is qualitative, inductive and exploratory in nature. Therefore, I selected the case studies research method as the most suitable approach for studying qualitatively a contemporary unexplored phenomenon in its full complexity and natural settings (Darke, Shanks, & Broadbent, 1998; Eisenhardt, 1989; Yin, 2003). In order to provide a generalizable answer to the research question reflecting the experience of many diverse organizations, I focused on multiple case studies (Benbasat, Goldstein, & Mead, 1987; Yin, 2003).

Specifically, to meet both the depth and breadth objectives, the study has been conducted in two sequential phases: exploratory and confirmatory. During the first exploratory phase, a small number of organizations have been studied in great detail to identify the initial set of EA artifacts and achieve an in-depth understanding of their usage. During the second confirmatory phase, a larger number of organizations have been studied in less detail to confirm the initial usage patterns identified during the exploratory phase and extend the “statistics” of EA artifacts.

## Exploratory phase of data collection

The goal of the exploratory phase of this research was to study in detail several “typical” EA practices, identify the preliminary set of useful EA artifacts and thoroughly understand their practical usage. For this purpose, I conducted five in-depth case studies of Australian organizations practicing EA from different industry sectors (academe, finance, telecommunication, delivery and retail) selected according to the following criteria: (1) large organizations employing at least 100 full-time IT staff, (2) having permanent EA teams and consistent EA-related processes and (3) practicing EA at least for 3 years. Brief descriptions of the five organizations studied as part of the exploratory phase of this research can be found in Appendix B.

Data in the five studied organizations were collected predominantly from semi-structured interviews. However, numerous samples of EA artifacts demonstrated by the interviewees were also analyzed. In total, during the exploratory phase, I took 31 face-to-face 1-h interviews with direct participants of the EA practices in the studied organizations, or \~6.2 interviews on average per organization. The interviewees included mostly architects of different denominations (e.g. enterprise architects, principal architects, domain architects and solution architects) and architecture managers. All the interviewees were asked to list main types of EA artifacts used in their organizations and then to describe in detail their informational contents and various aspects of their usage, for example, developers, users, use cases and purposes.

## Confirmatory phase of data collection

After the exploratory phase was completed, this research proceeded to its confirmatory phase. The goal of the confirmatory phase was to encompass a larger number of organizations, confirm and refine the initial set of useful EA artifacts and their usage patterns as well as to extend the overall “statistics” of identified EA artifacts. For this purpose, I conducted 22 follow-up “mini-case studies” (Weill & Olson, 1989) of diverse Australian, New Zealand and international organizations from different industry sectors practicing EA chosen according to the “loosened” selection criteria: (1) no specific size requirements, (2) have permanent architecture teams and (3) practice EA at least for 1–2 years. Brief descriptions of the 22 organizations studied as part of the confirmatory phase of this research can be found in Appendix B.

Data in the 22 studied organizations were collected primarily from semi-structured interviews. Samples of EA artifacts provided by the interviewees were analyzed as well. In total, during the confirmatory phase, I took 32 faceto-face and Skype 1-h interviews with architects and architecture managers in the studied organizations or \~1.5 interviews on average per organization (many of these organizations employed only a single permanent enterprise architect or architecture manager). Similar to the exploratory phase, all the interviewees were asked to list main types of EA artifacts used in their organizations and then to describe in detail their informational contents and various aspects of their usage.

## Data analysis

Since this study intends to make an empirical contribution to the EA discipline (Agerfalk, 2014; Avison & Malaurent, 2014; Hambrick, 2007), that is, to identify EA artifacts that proved useful in practice and describe their usage, it is deliberately “atheoretic” in nature (Miller, 2007). From this perspective, the use of any theoretical lenses for data analysis can be considered as harmful for the purposes of this study due to a number of reasons widely acknowledged in the literature (Agerfalk, 2014; Avison & Malaurent, 2014; Hambrick, 2007; Helfat, 2007; Miller, 2007).

Instead, the data analysis in this study has been performed via comparing the descriptions and samples of EA artifacts provided by the interviewees in different organizations, identifying differences and similarities between these EA artifacts and then articulating “typical” EA artifacts based on their evident similarities. In particular, the following essential aspects of EA artifacts have been used as the basis for their comparison: (1) informational contents, (2) presentation formats, (3) users and stakeholders, (4) use cases, (5) lifecycles and (6) purposes in the context of an EA practice (importantly, the titles of many EA artifacts were inconsistent, highly organization-specific and in most cases could not have been used as a reliable basis for their comparison). Comparing identified EA artifacts with each other based on these aspects allowed producing the list of EA artifacts commonly used across the 27 studied organizations.

## EA artifacts used in organizations

In total, the analysis of all EA artifacts used in the 27 studied organizations identified 288 EA artifacts, or \~10.7 EA artifacts on average per organization. While 21 of these EA artifacts were unique for specific organizations and had no close analogs in other studied organizations, the remaining 267 EA artifacts proved to be rather common and, therefore, have been grouped into 24 different types of EA artifacts. Each of these 24 types was found at least in 3 out of the 27 studied organizations practicing EA. All the 24 types of EA artifacts have reasonably consistent informational contents, users, usage, lifecycles and purposes in all the organizations in which these EA artifacts were identified.

Table 1 describes in detail all the 24 identified EA artifacts in order of their relative popularity. Since most of these EA artifacts had different titles in different organizations, often very peculiar and highly organization-specific ones, the titles provided in Table 1 represent the most typical and “reasonable” titles under which these EA artifacts are used. Schematic graphical structures of all the 24 EA artifacts reflecting their typical informational contents and presentation formats can be found in Appendix C.

## Discussion of findings

The list of EA artifacts resulting from this study (see Table 1 and Appendix C) represents the first evidence-based “snapshot” of EA artifacts that actually proved useful in organizations. Moreover, this study provides the first systematic description of how these EA artifacts are used in practice and thereby “responds” to the earlier call for exploring the usage of EA artifacts by Niemi and Pekkola (2017). An evidence-based understanding of EA artifacts, and especially of their informational contents and practical usage, allows contrasting the observed empirical facts about EA artifacts against the numerous anecdotal claims made in the available EA literature.

## Comparison with the available lists of EA artifacts

The EA literature provides a number of comprehensive lists of EA artifacts prescribed by different authors (Bernard, 2012; DoDAF, 2007; Spewak & Hill, 1992; TOGAF, 2011; van’t Wout et al., 2010). A detailed comparison between these recommended lists and the list of EA artifacts resulting from this research shows at least two major differences between the EA literature and practice.

First, the number of EA artifacts described in literature is dramatically different from the number of EA artifacts actually distinguished by practitioners. While different EA sources recommend from 29 (DoDAF, 2007) to more than 80 (van’t Wout et al., 2010) types of EA artifacts, practicing architects distinguished only \~10.7 types of EA artifacts on average per organization. This difference can be partially explained by two reasons. On one hand, multiple different types of technical diagrams distinguished in the literature as separate EA artifacts are considered by EA practitioners essentially as a single type of Landscape Diagrams due to the close similarity of their contents, usage and purpose, that is, all these diagrams capture the current structure of the IT landscape and help plan its modifications during the implementation of new IT initiatives. On the other hand, in the literature, separate technical diagrams are often distinguished as full-fledged EA artifacts, while in practice, only cohesive combinations of these diagrams are considered as full-fledged EA artifacts, for example, Solution Overviews and Solution Designs.

Second, far from all EA artifacts that proved useful in practice are mentioned in the literature and far from all EA artifacts described in the literature can be found in practice, that is, the lists of EA artifacts from the literature and practice actually have only a rather limited intersection. For example, very widely used Business Capability Models and rather popular Enterprise Systems Portfolio are not even mentioned in any lists of EA artifacts available in the literature. At the same time, none of the matrix-style EA artifacts advocated in the literature (Spewak & Hill, 1992; TOGAF, 2011) have been identified in practice. Some EA artifacts found in organizations, for example, Technology Reference Models and Inventories, though mentioned in the literature in some form (TOGAF, 2011), actually differ substantially from the provided descriptions.

Table 1. Description of the identified EA artifacts including their contents, usage and purpose.

<table><tr><td>EA artifacts</td><td>Informational contents</td><td>Practical usage</td><td>Key purpose</td></tr><tr><td>Solution Designs (found in 26 organizations (96.3%), were also called detailed designs, technical designs, physical designs, high-level designs, solution architectures, full solution architectures, solution definitions and solution specifications)</td><td>Detailed technical and functional specifications of approved IT solutions actionable for project teams of ~25–50 pages long, in some cases longer</td><td>Developed collaboratively by architects and project teams at the implementation stages of IT initiatives, used by project teams to deliver IT solutions and then archived</td><td>Improve the quality of implemented IT solutions and achieve better traceability of business and architectural requirements</td></tr><tr><td>Roadmaps (found in 25 organizations (92.6%), were also called investment roadmaps, capability roadmaps, application roadmaps and technology roadmaps)</td><td>Structured graphical views of all planned IT initiatives in specific business areas having direct business value</td><td>Developed collectively by architects and senior business leaders, used to prioritize and schedule planned IT investments and updated periodically according to the changes in strategic business priorities</td><td>Achieve clearer traceability between the business strategy and future IT investments</td></tr><tr><td>Technology Reference Models (found in 24 organizations (88.9%), were also called technology standards, technical reference models, technology reference architectures or split into separate infrastructure and application reference models)</td><td>Structured graphical representations of all technologies used in an organization</td><td>Created primarily by architects and subject-matter experts, used mostly to select appropriate technologies for new IT initiatives and periodically updated according to the changes in the technological environment</td><td>Achieve better technological consistency and reduce complexity of the IT landscape</td></tr><tr><td>Principles (found in 20 organizations (74.1%), were also called maxims and drivers)</td><td>Global high-level guidelines influencing all decision-making and planning in an organization</td><td>Formulated collaboratively by architects and senior business leaders, used to assess the appropriateness of all other architectural decisions and periodically revised, often once a year</td><td>Facilitate overall conceptual consistency between business and IT</td></tr><tr><td>Business Capability Models (found in 19 organizations (70.4%), were also called business capability maps and capability reference models)</td><td>Provide structured graphical representations of all organizational business capabilities, their relationship and hierarchy</td><td>Developed collectively by architects and senior business leaders, used to focus future IT investments on the most important business capabilities and periodically “re-heatmapped” according to the changes in the business strategy</td><td>Align strategic business goals with the priorities for IT investments and thereby improve strategic business and IT alignment</td></tr><tr><td>Guidelines (found in 17 organizations (63.0%), were also called simply standards)</td><td>IT-specific implementation-level prescriptions applicable in narrow technology-specific areas or domains</td><td>Established by architects and relevant subject-matter experts, used to select appropriate implementation approaches for new IT initiatives and updated according to learned best practices and acquired experience with respective technologies and products</td><td>Facilitate reuse of proven best practices and reduce general technical complexity of the IT landscape</td></tr><tr><td>Solution Overviews (found in 17 organizations (63.0%), were also called solution outlines, conceptual architectures, preliminary solution architectures, conceptual designs and solution briefs)</td><td>High-level descriptions of specific proposed IT solutions understandable to business leaders of ~15–30 pages long</td><td>Developed collaboratively by architects and business leaders at the early stages of IT initiatives, used to approve the implementation of corresponding IT solutions and then archived after investment decisions are made</td><td>Improve the assessment of proposed IT solutions and achieve better transparency of their impact, costs and benefits</td></tr><tr><td>Landscape Diagrams (found in 15 organizations (55.6%), were also called simply an architectural repository or used under very diverse titles including relational diagrams, system interaction diagrams, one-page diagrams, platform architectures, enterprise system models, integration contexts, etc.)</td><td>Technical “boxes and arrows” schemes of different scopes and granularities describing the organizational IT landscape</td><td>Created and owned predominantly by architects, used mostly to plan the implementation of new IT solutions and their integration into the current IT environment and periodically updated to reflect the evolution of the organizational IT landscape, for example, after new IT systems are deployed</td><td>Help architects understand, analyze and modify the structure of the IT landscape</td></tr><tr><td>IT Roadmaps (found in 12 organizations (44.4%), were also called technology roadmaps, platform roadmaps, infrastructure roadmaps and integration roadmaps)</td><td>Structured graphical views of all planned IT initiatives of a purely technical nature having no visible business impact</td><td>Developed collaboratively by architects and other senior IT stakeholders, used to plan and schedule necessary technical improvements in the organizational IT landscape and periodically updated according to the evolution of the landscape</td><td>Reduce the dependence on legacy systems and technologies as well as to improve the technical efficiency and reliability of the IT landscape</td></tr><tr><td>Inventories (found in 11 organizations (40.7%), were also called asset registers and architectural repositories)</td><td>Structured catalogs of currently available IT assets describing their essential properties and features</td><td>Created and owned primarily by architects, utilized for reusing existing IT assets in new IT initiatives, decommissioning legacy IT assets and maintained current to accurately reflect the actual state of the IT landscape</td><td>Achieve better control of the available IT assets, increase their reuse and ease the management of their lifecycles</td></tr><tr><td>Patterns (found in 11 organizations (40.7%), were also called reference architectures)</td><td>Generic reusable solutions to commonly occurring problems in the design of IT systems</td><td>Established by architects and subject-matter experts, used to select standardized solution components for new IT solutions and periodically updated according to the changes in preferred implementation approaches</td><td>Increase the reuse of proven “building blocks,” reduce technical risks and heterogeneity of the IT landscape</td></tr><tr><td>IT Principles (found in 10 organizations (37.0%), were also called simply principles)</td><td>Global high-level IT-specific guidelines influencing all IT-related decisions and plans in an organization</td><td>Formulated by architects, used to assess the technical feasibility of all IT-related planning decisions and reviewed on a periodical basis, often yearly</td><td>Promote the use of consistent approaches to IT and facilitate better conceptual homogeneity of IT-related decision-making</td></tr><tr><td>Options Assessments (found in eight organizations (29.6%), were also called options analyses, options papers, solution options, solution assessments and discussion papers)</td><td>Lists of available high-level implementation options for specific IT initiatives with their pros and cons</td><td>Developed collaboratively by architects and business leaders at the very early stages of IT initiatives, used to discuss possible high-level solution implementation options and then archived after specific options are chosen as preferable</td><td>Achieve better engagement between business and IT, improve transparency of recommended IT solutions and increase business returns on IT investments</td></tr><tr><td>Target States (found in eight organizations (29.6%), were also called target architectures, future state architectures and business reference architectures)</td><td>High-level graphical descriptions of the desired long-term future state of an organization</td><td>Developed collectively by architects and senior business leaders, used to define long-term strategic goals for IT investments and periodically updated according to the changes in the business strategy, often on a yearly basis</td><td>Enable strategic dialog business and IT and facilitate business and IT alignment in the long run</td></tr><tr><td>Enterprise System Portfolios (found in seven organizations (25.9%), were also called application portfolios, application models, IT system value maps and IT strategy maps)</td><td>Structured high-level mappings of all essential IT systems to relevant business capabilities</td><td>Created and owned by architects, used to rationalize the organizational IT landscape, manage the life cycle of major IT assets and updated periodically according to the changes in the landscape</td><td>Control the duplication and reuse of IT assets, facilitate the analysis of the IT landscape and its overall organizational fitness</td></tr><tr><td>Policies (found in six organizations (22.2%), were also called security policies, cloud policies and access policies)</td><td>Overarching organizational norms typically of a restrictive nature providing compulsory prescriptions in certain areas</td><td>Formulated collaboratively by architects and senior business leaders, used to assess the appropriateness of IT-related planning decisions and periodically updated according to the changes in the business strategy and legislative environment</td><td>Improve security, compliance and overall conceptual consistency</td></tr><tr><td>Initiative Proposals (found in five organizations (18.5%), were also called solution proposals, initiative summaries, investment cases and idea briefs)</td><td>Very early idea-level descriptions of proposed IT initiatives and their justifications</td><td>Developed collectively by architects and business leaders at the inception stages of IT initiatives, used to assess the potential business value of proposed IT initiatives and then archived after the “seed” funding is secured</td><td>Facilitate the initial benefit assessment of possible IT initiatives at their earliest conception stages</td></tr><tr><td>Preliminary Solution Designs (found in five organizations (18.5%), were also called preliminary solution architectures, solution architectures and logical designs)</td><td>Preliminary high-level technical and functional designs of specific approved IT solutions of ~20–40 pages long</td><td>Created by architects and project teams in the beginning of the implementation stages of IT initiatives, used to agree on the tentative implementation plans, confirm previous time and cost estimates and then converted into full-fledged actionable solution designs</td><td>Ensure that IT initiatives can be actually implemented as expected in a way approved earlier by senior business leaders, for example, according to their agreed high-level solution overviews</td></tr><tr><td>Conceptual Data Models (found in four organizations (14.8%), were also called enterprise data models and information models)</td><td>Abstract definitions of the main data entities critical for the business of an organization and their relationship</td><td>Developed collaboratively by architects and business leaders, used to align all new IT solutions to organization-wide information requirements and periodically updated according to the changes in the business and its operations</td><td>Achieve better global data consistency and uniform handling of information in all IT systems</td></tr><tr><td>Direction Statements (found in four organizations (14.8%), were also called architecture strategies, governance papers, position papers and strategic papers)</td><td>Conceptual messages communicating major organization-wide decisions with far-reaching consequences</td><td>Developed collectively by architects and senior business leaders, used to align all “downstream” IT-related planning decisions to the established strategic direction and then archived when no longer relevant</td><td>Facilitate conceptual consistency between general business and IT directions</td></tr><tr><td>Logical Data Models (found in four organizations (14.8%), were also called logical information models, canonical data models and data schemas)</td><td>Logical or even physical platform-specific definitions of the key data entities and their relationship</td><td>Created and owned mostly by architects, used to select appropriate data structures for new IT initiatives and periodically revised according to the changes in business operations and their information requirements</td><td>Achieve better logical data consistency and interoperability between different IT systems</td></tr><tr><td>Analytical Reports (found in three organizations (11.1%), were also called whitepapers, position papers and strategy papers)</td><td>Executive-level analyses of relevant technology trends and their potential impact on the business of an organization</td><td>Developed collaboratively by architects and senior business leaders, used to assess the disruptive influence of recent technological opportunities and then either updated yearly, or archived if no longer relevant</td><td>Align the general business and IT strategy to the current technological tends</td></tr><tr><td>Context Diagrams (found in three organizations (11.1%), were also called business context diagrams, application diagrams and concepts of operations)</td><td>High-level graphical descriptions of the current operational flows of an organization</td><td>Created collectively by architects and senior business leaders, used to discuss the potential opportunities for future IT investments and maintained current to reflect major changes in business operations</td><td>Provide a common context for discussions between business and IT leaders, facilitate strategic dialog and alignment</td></tr><tr><td>Value Chains (found in three organizations (11.1%), were also called value reference models and business activity models)</td><td>Structured graphical representations of the added value chain of an organization</td><td>Developed collaboratively by architects and business leaders, used to focus future IT investments on strategic business operations and periodically “re-heatmapped” in a way similar to business capability models</td><td>Align strategic business goals with the priorities for IT investments and improve strategic business and IT alignment</td></tr></table>

EA: enterprise architecture.

Generally, the comparison between useful and prescribed EA artifacts suggests that the overlap between these sets is rather limited. Moreover, this overlap seems to be largely “accidental” in nature since no traceable and consistent connection between literature and practice can be observed. Although the list of useful EA artifacts identified in organizations (see Table 1) “resembles” the lists of EA artifacts offered in the literature, it is hard to formulate clearly how exactly they correlate.

Metaphorically, the relationship between useful and prescribed EA artifacts can be explained as the same as the relationship between meaningful sentences and separate words. Separate words, though provide components for meaningful sentences, still convey little or no meaning on their own since connections between these words are critically important as well. From this perspective, all the lists of EA artifacts provided in the literature can be considered at best only as “dictionaries,” that is, they can provide only some components for a meaningful “story,” but cannot tell the real “story.”

To summarize, none of the lists of EA artifacts offered in the literature (Bernard, 2012; DoDAF, 2007; Spewak & Hill, 1992; TOGAF, 2011; van’t Wout et al., 2010) provides a reasonably accurate description of “real” EA artifacts. EA artifacts distinguished by practitioners are significantly different from EA artifacts distinguished in the literature. Therefore, none of these lists can be taken as a sound basis for further EA research.

## Comparison with the popular conceptualizations of EA

An evidence-based view of EA artifacts allows comparing empirical realities of EA with the popular conceptualizations of EA found in the literature. First, most EA frameworks (FEAF, 1999; PRISM, 1986; Pulkkinen, 2006; Schekkerman, 2006; TOGAF, 2011; TAFIM, 1996; TEAF, 2000; van’t Wout et al., 2010) articulate business, information, applications and technology elements of EA. In fact, most comprehensive lists of EA artifacts (Bernard, 2012; Spewak & Hill, 1992; TOGAF, 2011; van’t Wout et al., 2010) even explicitly relate all these EA artifacts to one of these four “classic” EA domains. Unsurprisingly, EA is often considered as a combination of separate business, information, applications and technology architectures. Second, EA at the highest level is typically conceptualized as a combination of the current state, future state and transformation roadmap (Bernard, 2012; FEA, 2001; Lange et al., 2016; Tamm et al., 2011; TOGAF, 2011).

However, the properties of real EA artifacts demonstrate a much more diverse and complex picture. The analysis of the 24 identified EA artifacts from the perspective of their domains and states is summarized in Table 2.

The analysis of the actual EA artifacts found in organizations suggests that these EA artifacts generally cannot be classified into one of the four typical EA domains and related either to the current state or to the future state. First, most EA artifacts describe multiple different EA domains simultaneously, rather than a single EA domain. With the exception of Business Capability Models, Value Chains, Conceptual Data Models and Logical Data Models which can be unambiguously related to single EA domains (business and information, respectively) and individual instances of Guidelines, Patterns and IT Principles, all other types of

EA artifacts combine several EA domains. Moreover, for many EA artifacts, most notably for Solution Designs, Solution Overviews and Enterprise System Portfolios, combing multiple EA domains and explaining the relationship between the corresponding objects, for example, between business capabilities and applications supporting these capabilities, is absolutely essential for their purposes in the context of an EA practice. At the same time, applying more fine-grained classifications proposed by many EA frameworks, for example, what, how and where (Schekkerman, 2006; Sowa & Zachman, 1992; van’t Wout et al., 2010), to real EA artifacts is even more problematic.

Second, EA artifacts can actually focus on describing current states, short-term (<1 year), mid-term (1–2 years) and long-term (3–5 years) future states, as well as their various combinations. Moreover, EA artifacts also can be essentially stateless in nature, for example, describe certain rules that do not refer to specific points in time, but are active until modified or canceled. While some EA artifacts including Inventories, Enterprise System Portfolios and Context Diagrams focus predominantly on the current state, most other EA artifacts are either stateless, like Technology Reference Models and Principles, or focus on different time horizons in the future. Furthermore, some EA artifacts, most notably Solution Designs and Solution Overviews, often describe both the current state and some future state simultaneously.

Consequently, the conceptualization of EA as a set of separate business, application, information and technology architectures is empirically invalid since these architectures are very closely intertwined and in most cases cannot be described separately from each other. Moreover, from the empirical perspective, the very notions of “business architecture,” “application architecture,” “information architecture” and “technology architecture” are essentially non-existing since none of these notions is clearly manifested in underlying EA artifacts. However, a loosened understanding of EA as a set of descriptions or artifacts covering business, application, information and technology domains, not necessarily separately, is still empirically valid.

At the same time, the classification of EA artifacts into business, application, information and technology domains is also not explanatory and largely useless. Even for EA artifacts that can be clearly related to one of these domains, this classification is unable to explain their essential properties. For example, both Conceptual Data Models and Logical Data Models unequivocally belong to the information domain. However, these two EA artifacts are still used very differently and intended for different audiences and purposes. While Conceptual Data Models are used by senior business leaders to decide what information assets their organization should possess, maintain and leverage, Logical Data Models are used mostly by architects for planning specific IT solutions. Even worse, distinct elements of “information architecture” can be also found in many other

Table 2. Analysis of the identified EA artifacts from the perspective of their domains and states.

<table><tr><td>EA artifacts</td><td>Domains</td><td>States</td></tr><tr><td>Solution Designs</td><td>Usually all the four EA domains</td><td>Short-term future and often the current state as well</td></tr><tr><td>Roadmaps</td><td>Business and applications in some form</td><td>The full-time range between the current state and long-term future</td></tr><tr><td>Technology Reference Models</td><td>Technology and sometimes applications</td><td>Largely stateless</td></tr><tr><td>Principles</td><td>Mostly business, but often can be also related to applications and information</td><td>Stateless</td></tr><tr><td>Business Capability Models</td><td>Only business</td><td>Mostly long-term future</td></tr><tr><td>Guidelines</td><td>Usually relate to information, applications or technology</td><td>Stateless</td></tr><tr><td>Solution Overviews</td><td>Usually business, information and applications</td><td>Mid-term future and often the current state as well</td></tr><tr><td>Landscape Diagrams</td><td>Usually information, applications and technology and sometimes business as well</td><td>Mostly current state, but sometimes the short-term and mid-term future as well</td></tr><tr><td>IT Roadmaps</td><td>Technology and sometimes applications</td><td>The full-time range between the current state and mid-term future</td></tr><tr><td>Inventories</td><td>Usually information, applications and technology</td><td>Current state</td></tr><tr><td>Patterns</td><td>Usually relate to information, applications or technology</td><td>Stateless</td></tr><tr><td>IT Principles</td><td>Usually relate to information, applications or technology</td><td>Stateless</td></tr><tr><td>Options Assessments</td><td>Usually business, information and applications</td><td>Mid-term future and sometimes the current state as well</td></tr><tr><td>Target States</td><td>Usually business, information and applications</td><td>Long-term future</td></tr><tr><td>Enterprise System Portfolios</td><td>Always business and applications</td><td>Current state</td></tr><tr><td>Policies</td><td>Usually relate to business and information</td><td>Stateless</td></tr><tr><td>Initiative Proposals</td><td>Usually business, information and applications</td><td>Mid-term future and sometimes the current state as well</td></tr><tr><td>Preliminary Solution Designs</td><td>Usually all the four EA domains</td><td>Short-term future and often the current state as well</td></tr><tr><td>Conceptual Data Models</td><td>Only information</td><td>Stateless</td></tr><tr><td>Direction Statements</td><td>Usually business, information and applications</td><td>Mostly long-term future</td></tr><tr><td>Logical Data Models</td><td>Only information</td><td>Stateless</td></tr><tr><td>Analytical Reports</td><td>Usually business and technology</td><td>Mostly long-term future</td></tr><tr><td>Context Diagrams</td><td>Usually business, information and applications</td><td>Current state</td></tr><tr><td>Value Chains</td><td>Only business</td><td>Mostly long-term future</td></tr></table>

EA: enterprise architecture.

EA artifacts with disparate properties and purposes including, among others, Target States, Inventories, Solution Overviews and Solution Designs. Therefore, the classification of EA artifacts into different domains is self-referential and explains only which domains these EA artifacts describe, but no other properties, for example, users, usage, purpose and life cycle.

Describing EA as a set of business, application, information and technology architectures can be metaphorically compared with describing a car as a set of metal, plastic, glass and rubber. Although cars indeed consist mostly of these four elements, these elements still cannot be considered as “real” components of cars like wheels, engines and cabins. For instance, the operations of a car cannot be analyzed from the perspective of metal, plastic, glass and rubber in any real sense, even though all these elements are present. Analogously, the work of an EA practice cannot be analyzed in a meaningful way from the perspective of business, application, information and technology architectures, even though all these domains are described in some EA artifacts.

More importantly, the conceptualization of EA as the current state, future state and transition roadmap is also empirically invalid because of a number of related reasons. First, as noted earlier, many useful EA artifacts actually describe both the current and future states. Second, none of the studied organizations had comprehensive descriptions of their current states, but only pragmatic sets of EA artifacts, most often Landscape Diagrams or Inventories, providing some views of the existing IT landscape. Third, none of the studied organizations had comprehensive descriptions of their future states. On one hand, more or less detailed descriptions of the short-term and mid-term future were developed only for specific change initiatives, most often in the form of Solution Designs and Solution Overviews, respectively. On the other hand, most organizations did not have systematic descriptions of their global long-term future states in any real sense beyond highlighted strategic capabilities in Business Capability Models, while the minority of organizations having these descriptions defined their long-term future only as brief, often one-page executive-level Target States. Fourth, Roadmaps were developed mostly based on the strategic investment priorities formulated by business executives, but not based on a formal gap analysis between the current and future states as suggested by the EA literature. Moreover, since most organizations did not have any descriptions of their desired future states, as noted above, the general intent of Roadmaps in most cases was only to align future IT investments with strategic business capabilities, rather than to reach some definite, well-understood target states.

To summarize, both the popular conceptualizations of EA as a set of business, application, information and technology architectures, and as a set of current states, future states and transition roadmaps are empirically invalid and distant from the practical realities of EA.

## Definition of EA

Many of the numerous definitions of EA found in the literature (Saint-Louis, Morency, & Lapalme, 2017; Schoenherr, 2008) define EA as some comprehensive description, or even as a blueprint, of an entire organization from the business and IT perspective. For instance, Schekkerman (2004) puts it in the most striking way: “Enterprise Architecture is a complete expression of the enterprise” (p. 13).

However, in none of the studied organizations, EA actually resembled a holistic overarching description or a comprehensive blueprint of the whole organization, let alone “a complete expression of the enterprise.” Instead, in all the studied organizations, the notion of EA was understood essentially only as an umbrella term for all the various EA artifacts used as part of their EA practices. Moreover, these EA artifacts had different use cases, stakeholders, purposes and lifecycles, that is, were developed and used at different time moments independently of each other.

Consequently, an empirically valid definition of EA should necessarily reflect the critical fact that EA is actually a complex set of very diverse descriptions intended for different decision-makers and purposes, rather than a single comprehensive description that is developed and then used by all stakeholders. In light of these findings, a reasonable evidence-based definition of EA can be formulated, for example, as follows:

EA is a collection of special documents (EA artifacts) describing various aspects of an organization from an integrated business and IT perspective intended to bridge the communication gap between business and IT stakeholders, facilitate information systems planning and thereby improve business and IT alignment.

## Other observations regarding EA artifacts

A detailed understanding of EA artifacts and their practical usage resulting from this study allows making a number of other theoretically significant observations regarding EA artifacts.

Different sets of EA artifacts are used in different organizations. As this study demonstrates, different organizations use unique sets of EA artifacts in their EA practices. Moreover, with some rare exceptions, for example, Business Capability Models, organizations also use different titles for these EA artifacts. As a result, in different organizations, similar EA artifacts can have different titles, while EA artifacts with similar titles can have different meanings. Consequently, sets of EA artifacts and their titles are not standardized across the industry and cannot be relied on in EA research. For example, specific titles of EA artifacts cannot be used in EA-related surveys since the interpretation of these titles may be significantly different in different organizations leading to corrupted findings.

All EA artifacts are fit for purpose. In the studied organizations with established EA practices, all EA artifacts are created for specific purposes, rather than simply to describe some aspects of organizations. Moreover, in established EA practices, all EA artifacts are fit for purpose, that is, informational contents of an EA artifact limit its usage to a specific purpose and a particular purpose of an EA artifact requires specific informational contents. Therefore, the informational contents, usage and purpose of EA artifacts are inseparably connected. Each EA artifact is strongly associated with one or a few closely related use cases (see Table 1). No EA artifacts are created merely for the sake of having some descriptions.

Sets of EA artifacts are industry-independent. The 27 studied organizations represented very diverse industry sectors (see Appendix B) and industry is considered as an important factor influencing the use of information systems in organizations (Chiasson & Davidson, 2005). However, no articulate industry-specific differences in the sets of EA artifacts or their usage in these organizations have been identified during this study. This observation suggests that the fundamental mechanisms of an EA practice are essentially industry-independent.

Size determines quantity, but not types of EA artifacts. The 27 studied organizations varied significantly in their sizes and ranged from tens to thousands of IT staff (see Appendix B), but no articulate size-specific differences in the sets of EA artifacts or their usage in these organizations have been identified during this study. However, the size of an organization still directly influenced the quantity of EA artifacts of a specific type. For example, small organizations typically developed only one or a few Roadmaps for an entire organization, while large organizations often created tens of Roadmaps aligned to different business units or departments. Consequently, both types of EA artifacts and their practical usage are remarkably consistent across organizations of diverse sizes, only their quantity varies roughly proportionally to the size of an organization.

Sets of EA artifacts do not depend on the declared use of EA frameworks. The 27 studied organizations differed significantly from the perspective of their adoption and use of popular EA frameworks. For example, five of the studied organizations were included in the “official” list of TOGAF users provided by The Open Group (2016), some organizations reported that they used TOGAF or other EA frameworks, but only as the basis for their EA practices, while other organizations did not use any EA frameworks at all. However, no articulate differences in the sets of EA artifacts or their usage in these organizations have been identified during this study. In all cases, the use of TOGAF and other EA frameworks was purely declarative in nature and did not define resulting EA practices in any real sense.

Consequently, the declared usage, as well as non-usage, of EA frameworks cannot be considered as a significant factor in EA research. For instance, all the industry surveys showing which EA frameworks are used in organizations (Ambler, 2010; Aziz & Obitz, 2007; Buckl, Ernst, Lankes, Matthes, & Schweda, 2009; Cameron & McMillan, 2013; Dahalin, Razak, Ibrahim, Yusop, & Kasiran, 2010; Gall, 2012; Obitz & Babu, 2009; Schekkerman, 2005; Scholtz, Calitz, & Connolley, 2013) cannot be considered as informative since no specific correlation between the declared use of EA frameworks and actual EA practices can be observed. Generally, EA frameworks demonstrate evident signs of management fads (Miller & Hartwick, 2002; Miller, Hartwick, & Le Breton-Miller, 2004), while their prescriptions are very distant from the established EA best practices widely adopted in industry.

## Empirical contribution

As noted earlier, this study did not intend to develop any new theories, but rather to make an empirical contribution to the EA discipline (Agerfalk, 2014; Avison & Malaurent, 2014; Hambrick, 2007), which “may have more far-reaching theoretical implications than many self-proclaimed theoretical contributions” (Agerfalk, 2014, p. 596). Specifically, this study (1) provides the first evidence-based list of EA artifacts that proved useful in organizations; (2) explains the usage of these EA artifacts in the context of an EA practice; (3) questions the popular view of EA as a set of separate business, information, applications and technology architectures; and (4) demonstrates the empirical invalidity of the most popular conceptualization of EA as the current state, future state and transition roadmap.

## Evidence-based list of useful EA artifacts

Although the available EA literature provides a number of comprehensive lists of EA artifacts (Bernard, 2012; DoDAF, 2007; Spewak & Hill, 1992; TOGAF, 2011; van’t Wout et al., 2010), these lists are purely prescriptive, based only on anecdotal evidence and were never validated previously by independent research (Kotusev, 2017b). Essentially, the current EA literature is unable to explain what EA artifacts are actually used in organizations.

Based on an extensive empirical inquiry involving 27 diverse organizations, this study closes this gap, articulates 24 consistent types of EA artifacts that proved useful in practice and analyzes their relative popularity (see Table 1). The list of useful EA artifacts resulting from this research provides a sound foundation for further in-depth studies of an EA practice at the level of specific EA artifacts, rather than at the higher level of EA as a whole. Moreover, this study demonstrates that the lists of EA artifacts recommended in the literature barely overlap with the actual EA artifacts used in established EA practices and, therefore, cannot be taken as a reliable basis for EA research, for example, for formulating deductive propositions and conducting surveys.

## Practical usage of EA artifacts

The current EA literature focuses mostly on the application and benefits of EA as a whole (Alaeddini & Salekfard, 2013; Bradley et al., 2012; Foorthuis, van Steenbergen, Brinkkemper, & Bruls, 2016; Rahimi, Gotze, & Moller, 2017; Schmidt & Buxmann, 2011; Simon, Fischbach, & Schoder, 2014; Tamm et al., 2011), but rarely discusses the usage of specific EA artifacts constituting EA. Unsurprisingly, an insufficient understanding of EA artifacts, their practical usage, purposes and roles in the context of an EA practice is acknowledged as a significant gap in the EA discipline (Niemi & Pekkola, 2017).

This study offers the first rich descriptive view of the practical usage of individual EA artifacts contributing to our understanding of the realities of EA in organizations. The diversity of useful EA artifacts and their purposes in an EA practice suggests that the EA community should focus more closely on studying specific EA artifacts, rather than EA in general as a collection of all EA artifacts, since many conclusions may be perfectly correct for some types of EA artifacts, but at the same time invalid for other types of EA artifacts.

## Business, information, applications and technology architectures

The current EA literature typically classifies EA artifacts into business, information, applications and technology domains and considers EA accordingly as a set of separate business, information, applications and technology architectures (FEAF, 1999; PRISM, 1986; Pulkkinen, 2006; Schekkerman, 2006; TOGAF, 2011; TAFIM, 1996;

TEAF, 2000; van’t Wout et al., 2010). However, the find ings of this study regarding EA artifacts and their practical usage question these views as non-empirical and non-descriptive.

On one hand, most useful EA artifacts describe multiple EA domains in some or the other form. On the other hand, the loose classification of EA artifacts according to the typical EA domains, even when it can be applied, does not clarify the usage and purpose of respective EA artifacts in any real sense. Therefore, the view of EA as a set of business, information, applications and technology architectures can be considered as empirically invalid and largely useless for analytical purposes.

## Current states, future states and transition roadmaps

Currently, at the highest level, EA is typically conceptualized as a set of the current state, future state and transition roadmap (Bernard, 2012; FEA, 2001; Lange et al., 2016; Tamm et al., 2011; TOGAF, 2011). However, the analysis of EA artifacts and their practical usage offered by this study demonstrates that EA cannot be conceptualized in this way.

In particular, the current state in practice is usually represented by purely technical views of the existing IT land scape, a systematic description of the organization-wide long-term future state is most often missing altogether, while roadmaps typically result from the discussions of perceived business priorities of specific IT initiatives, rather than from a formal gap analysis between the current and future states. Many EA artifacts describe both the current state and the future state at various time horizons.

Moreover, none of the studied EA practices resembled the step-wise processes prescribed by the vast majority of EA methodologies (Armour, Kaisler, & Liu, 1999; Bernard, 2012; Bittler & Kreizman, 2005; Boar, 1999; Carbone, 2004; Covington & Jahangir, 2009; FEAF, 1999; Holcman, 2013; IBM, 2006; Longepe, 2003; Niemann, 2006; TOGAF, 2011; Schekkerman, 2008; Spewak & Hill, 1992; TAFIM, 1996; Theuerkorn, 2004; van’t Wout et al., 2010) all of which in some or the other form imply describing the current state, defining the future state, creating the transition roadmap and then implementing this roadmap. Thereby, this study demonstrates that the most widely accepted conceptualization of EA is empirically invalid.

Consequently, this study makes a significant empirical contribution to the EA literature by demonstrating important empirical facts that question established theories, can stimulate future research and substantially alter the EA discipline (Agerfalk, 2014; Avison & Malaurent, 2014; Hambrick, 2007). Despite being “atheoretic,” this article “has a high potential for stimulating research that will impact on information systems theory and/or practice” (Avison & Malaurent, 2014, p. 327).

## Limitations of this study

Despite its extensive scope, this study has three limitations that should be explicitly acknowledged and taken into account.

## Reflection of the views of architects

The vast majority of the interviews conducted as part of this study involved representatives of organizational architecture functions, that is, architects of various denominations and architecture managers. Non-architecture stakeholders of EA artifacts proved to be “inconvenient” interviewees for the purposes of this study since they typically used only one or a few closely related types of EA artifacts in their jobs and were naturally unaware of all other EA artifacts existing in their organizations. Moreover, many EA artifacts, for example, Technology Reference Models and Inventories, are intended mostly for architects and have no other “external” stakeholders outside of the architecture function.

However, the primary focus on interviewing architects suggests that this study reflects mostly the perspective of architects, rather than of other EA stakeholders (when these stakeholders existed). Since the descriptions of the usage scenarios of EA artifacts were provided predominantly by architects, these descriptions inevitably contain a certain architecture-centric bias. In other words, the use cases of EA artifacts described in this study for the most part represent use cases in their perception by architects.

## Possible Australia-specific bias in EA artifacts

Out of the 27 organizations studied as part of this research, 24 were Australian companies. The Australian EA community is somewhat isolated from the United States and European EA communities, characterized by a rather limited supply of experienced architects and largely dominated by a narrow pool of local EA consultancies that helped many Australian companies start their EA journeys and shaped their EA practices. All these factors might have introduced a certain Australia-specific bias in the selection and practical usage of EA artifacts in organizations. Even though the analysis of three non-Australian organizations (two companies from New Zealand and one international company headquartered in United Kingdom) did not reveal any articulate country-specific differences in EA practices, the overall “statistics” of the identified EA artifacts might still be somewhat Australia-centric.

## Identified popularity of EA artifacts is rather conditional

The primary objective of this study was to identify what EA artifacts proved useful and understand how exactly these EA artifacts are used in organizations. Besides fulfilling this objective, this study also estimated the relative popularity of different EA artifacts in practice. Although this popularity can be considered as a rough proxy for the practical importance, usefulness and value of respective EA artifacts, the specific numbers provided by this study should be treated with caution.

First, these numbers are based on the analysis of a reasonably large, but still not statistically significant sample of organizations. Second, all EA practices in the studied organizations were reasonably mature, but still differed from the perspective of their maturity, and more mature EA practices tended to employ somewhat larger numbers of different EA artifacts. These facts suggest that the numbers indicating the relative popularity of EA artifacts provided by this study can be considered only as basic and tentative orienteers, but not as an exact statistical snapshot of the usage of EA artifacts. At the same time, due to considerable terminological differences in EA practices, the creation of such a snapshot via structured surveys seems highly problematic.

## Conclusion and directions for future research

The ongoing IT-enabled business transformation requires well-developed dynamic capabilities to be able to respond to emerging digital disruptions and keep up with the accelerating pace of change (Karimi & Walter, 2015; Yeow, Soh, & Hansen, 2018). One of the most critical elements supporting these dynamic capabilities and respective digitized business models is sound IT platforms (Keen & Williams, 2013; Weill, Ross, & Quaadgras, 2010; Weill & Woerner, 2013b), and the architectural diversity of IT platforms is constantly increasing as these platforms become more and more overarching and multilayered in nature (de Reuver, Sørensen, & Basole, 2018). At the same time, these digitized platforms should enable agile and scalable business operations (Sia, Soh, & Weill, 2016), integrated customer experience and processes (Westerman & Bonnet, 2015), leverage existing legacy systems (Edelman, 2015) while restraining overall complexity in organizations (Weill & Woerner, 2018a). These and other conflicting demands put additional pressure on business and IT leaders to achieve a shared mindset and common architectural view in order to intertwine business and IT plans together (Hansen, Kraemmergaard, & Mathiassen, 2011; Li et al., 2016).

In the epoch of “total digitization” (Weill & Woerner, 2013a), EA, as a proven means for connecting business and IT, can be considered as a critical tool in the organizational toolkit necessary for building solid IT platforms and thereby implementing innovative digital business models and strategies. However, the current understanding of EA artifacts is still based largely on the comprehensive lists of EA artifacts (Bernard, 2012; DoDAF, 2007; Spewak & Hill, 1992; TOGAF, 2011; van’t Wout et al., 2010) that were only “proposed” by fashion-setters, for example, consultancies and gurus, but never validated empirically (Kotusev, 2017b). Moreover, the practical usage of EA artifacts remains largely an unexplored area of the EA discipline (Niemi & Pekkola, 2017).

This study represents the first comprehensive empirical investigation of EA artifacts intended to close the aforementioned gaps in our knowledge. The study provides the list of 24 EA artifacts that provided useful in organizations, explains their practical usage and, based on this understanding, analyzes the empirical validity of the most popular conceptualizations of EA. Most importantly, this study essentially invalidates the conceptualization of EA as a set of business, information, applications and technology architectures as well as the conceptualization of EA a set of the current state, future state and transition roadmap since both these conceptualizations contradict empirical evidence from numerous established EA practices.

These findings closely correlate with the conclusions of earlier EA literature reviews and empirical studies. On one hand, the comprehensive EA literature reviews (Kotusev, 2017b; Langenberg & Wegmann, 2004; Radeke, 2010) consistently demonstrated that the entire EA discipline has rather low empirical validity and is based largely on prescriptive works of questionable origin. On the other hand, previous empirical studies demonstrated, among other things, “the lack of any theoretically-based concept of gap analysis or detailed as-is and to-be architecture [in successful EA practices]” (Holst & Steensen, 2011, p. 20) and that “the [EA] frameworks appear theoretical and impossible to implement” (Buckl et al., 2009, p. 15).

These observations suggest that currently the EA discipline lacks sound theoretical models able to accurately describe the very concept of EA in a way consistent with empirical realities, while this study identifies “compelling empirical patterns that cry out for future research and theorizing” (Hambrick, 2007, p. 1350). In other words, this study provides strong empirical arguments in favor of reconceptualizing the very notion of EA, which will have profound implications for the whole EA discipline and theory and calls for further research in the corresponding direction.

Even though this study does not offer any theoretical contribution, it has considerable theoretical implications that are “likely to stimulate future research with the potential to alter IS theory and practice” (Agerfalk, 2014, p. 596). Therefore, this study makes a significant empirical contribution to the EA literature by demonstrating important empirical facts that question established theories, can stimulate future research and substantially alter the EA discipline (Agerfalk, 2014; Avison & Malaurent, 2014; Hambrick, 2007).

## Declaration of conflicting interests

The author(s) declared no potential conflicts of interest with respect to the research, authorship, and/or publication of this article.

## Funding

The author(s) received no financial support for the research, authorship, and/or publication of this article.

## Note

1. Actually, some other approaches to enterprise architecture (EA) inconsistent with this conceptualization have been also proposed in the EA literature (Kotusev, 2017a; Kotusev, Singh, & Storey, 2015a; Ross et al., 2006; Wagter, van den Berg, Luijpers, & van Steenbergen, 2005). However, these approaches arguably (1) do not offer alternative comprehensive conceptualizations of EA and (2) do not represent current mainstream academic views on EA. See Appendix A for a more detailed discussion.

## References

Abraham, R. (2013). Enterprise architecture artifacts as boundary objects—A framework of properties. In J. van Hillegersberg, E. van Heck, & R. Connolly (Eds.), Proceedings of the 21st European Conference on Information Systems (pp. 1–12). Atlanta, GA: Association for Information Systems.

Abrahamson, E. (1991). Managerial fads and fashions: The diffusion and rejection of innovations. Academy of Management Review, 16, 586–612.

Abrahamson, E. (1996). Management fashion. Academy of Management Review, 21, 254–285.

Agerfalk, P. J. (2014). Insufficient theoretical contribution: A conclusive rationale for rejection? European Journal of Information Systems, 23, 593–599.

Ahlemann, F., Legner, C., & Schafczuk, D. (2012). Introduction. In F. Ahlemann, E. Stettiner, M. Messerschmidt, & C. Legner (Eds.), Strategic enterprise architecture management: Challenges, best practices, and future developments (pp. 1–33). Berlin, Germany: Springer.

Ahlemann, F., Stettiner, E., Messerschmidt, M., & Legner, C. (Eds.). (2012). Strategic enterprise architecture management: Challenges, best practices, and future developments. Berlin, Germany: Springer.

Alaeddini, M., & Salekfard, S. (2013). Investigating the role of an enterprise architecture project in the business-IT alignment in Iran. Information Systems Frontiers, 15, 67–88.

Ambler, S. W. (2010). Enterprise architecture: Reality over rhetoric. Retrieved from http://www.drdobbs.com/architecture-and-design/enterprise-architecture-reality-overrhe/224600174

Armour, F. J., Kaisler, S. H., & Liu, S. Y. (1999). Building an enterprise architecture step by step. IT Professional, 1(4), 31–39.

Avison, D., & Malaurent, J. (2014). Is theory king? Questioning the theory fetish in information systems. Journal of Information Technology, 29, 327–336.

Aziz, S., & Obitz, T. (2007). Infosys Enterprise Architecture Survey 2007. Bangalore, India: Infosys.

Benbasat, I., Goldstein, D. K., & Mead, M. (1987). The case research strategy in studies of information systems. MIS Quarterly, 11, 369–386.

Bernard, S. A. (2012). An introduction to enterprise architecture (3rd ed.). Bloomington, IN: AuthorHouse.

Bischoff, S., Aier, S., & Winter, R. (2014). Use it or lose it? The role of pressure for use and utility of enterprise architecture artifacts. In H. A. Proper, J. Ralyte, S. Marchand-Maillet, & K. J. Lin, (Eds.), Proceedings of the 16th IEEE Conference on Business Informatics (pp. 133–140). New York, NY: IEEE.

Bittler, R. S., & Kreizman, G. (2005). Gartner enterprise architecture process: Evolution 2005 (#G00130849). Stamford, CT: Gartner.

Blomqvist, S., Halen, M., & Helenius, M. (2015). Connecting enterprise architecture with strategic planning processes: Case study of a large Nordic finance organization. In E. Kornyshova (Ed.), Proceedings of the 17th IEEE Conference on Business Informatics (pp. 43–50). New York, NY: IEEE.

Boar, B. H. (1999). Constructing blueprints for enterprise IT architectures. New York, NY: Wiley.

Bradley, R. V., Pratt, R. M., Byrd, T. A., Outlay, C. N., & Wynn, D. E.Jr. (2012). Enterprise architecture, IT effectiveness and the mediating role of IT alignment in US hospitals. Information Systems Journal, 22, 97–127.

Buckl, S., Ernst, A. M., Lankes, J., Matthes, F., & Schweda, C. M. (2009). State of the art in enterprise architecture management. Munich, Germany: Software Engineering for Business Information Systems.

Cameron, B. H., & McMillan, E. (2013). Analyzing the current trends in enterprise architecture frameworks. Journal of Enterprise Architecture, 9(1), 60–71.

Carbone, J. A. (2004). IT architecture toolkit. Upper Saddle River, NJ: Prentice Hall

Chiasson, M. W., & Davidson, E. (2005). Taking industry seriously in information systems research. MIS Quarterly, 29, 591–605.

Connor, D. A. (1988). Computer systems development: Strategic Resource Information Planning and Execution. Englewood Cliffs, NJ: Prentice Hall.

Covington, R., & Jahangir, H. (2009). The oracle enterprise architecture framework. Redwood Shores, CA: Oracle.

Dahalin, Z. M., Razak, R. A., Ibrahim, H., Yusop, N. I., & Kasiran, M. K. (2010). An enterprise architecture methodology for business-IT alignment: Adopter and developer perspectives. In K. S. Soliman (Ed.), Proceedings of the 14th International Business Information Management Association Conference (pp. 1–14). King of Prussia, PA: International Business Information Management Association.

Darke, P., Shanks, G., & Broadbent, M. (1998). Successfully completing case study research: Combining rigour, relevance and pragmatism. Information Systems Journal, 8, 273–289.

Department of Defense Architecture Framework. (2007). The DoDAF architecture framework (Version 1.5, Vol. II: Product Descriptions). Arlington County, VA: Department of Defense.

de Reuver, M., Sørensen, C., & Basole, R. C. (2018). The digi tal platform: A research agenda. Journal of Information Technology, 33, 124–135.

de Vries, M., & van Rensburg, A. C. J. (2009). Evaluating and refining the ‘enterprise architecture as strategy’ approach and artifacts. South African Journal of Industrial Engineering, 20(1), 31–43.

Edelman, B. (2015). How to launch your digital platform. Harvard Business Review, 93(4), 90–97.

Eisenhardt, K. M. (1989). Building theories from case study research. Academy of Management Review, 14, 532–550.

Fallmyr, T., & Bygstad, B. (2014). Enterprise architecture practice and organizational agility: An exploratory study. In R. H. Sprague (Ed.), Proceedings of the 47th Hawaii International Conference on System Sciences (pp. 3788–3797). New York, NY: IEEE.

Federal Enterprise Architecture. (2001). A practical guide to federal enterprise architecture (Version 1.0). Springfield, VA: Chief Information Officer Council.

Federal Enterprise Architecture Framework. (1999). Federal enterprise architecture framework (Version 1.1). Springfield, VA: Chief Information Officer Council.

Foorthuis, R., van Steenbergen, M., Brinkkemper, S., & Bruls, W. A. (2016). A theory building study of enterprise architecture practices and benefits. Information Systems Frontiers, 18, 541–564.

Gall, N. (2012). Gartner’s 2011 Global Enterprise Architecture Survey: EA frameworks are still homemade and hybrid (#G00226400). Stamford, CT: Gartner.

Gibson, J. W., & Tesone, D. V. (2001). Management fads: Emergence, evolution, and implications for managers. Academy of Management Executive, 15, 122–133.

Greefhorst, D., & Proper, E. (2011). Architecture principles: The cornerstones of enterprise architecture. Berlin, Germany: Springer.

Halen, M., Blomqvist, S., & Helenius, M. (2014). Enterprise architecture applied or not? In V. Grozdanic (Ed.), Proceedings of the 10th European Conference on Management, Leadership and Governance (pp. 118–127). Sonning Common, UK: Academic Conferences and Publishing International.

Hambrick, D. C. (2007). The field of management’s devotion to theory: Too much of a good thing? Academy of Management Journal, 50, 1346–1352.

Hansen, A. M., Kraemmergaard, P., & Mathiassen, L. (2011). Rapid adaptation in digital transformation: A participatory process for engaging IS and business leaders. MIS Quarterly Executive, 10, 175–185.

Harrell, J. M., & Sage, A. P. (2010). An enterprise architecture methodology to address the enterprise dilemma. Information, Knowledge, Systems Management, 9, 211–237.

Helfat, C. E. (2007). Stylized facts, empirical research and theory development in management. Strategic Organization, 5, 185–192.

Holcman, S. B. (2013). Reaching the pinnacle: A methodology of business understanding, technology planning, and change. Pinckney, MI: Pinnacle Business Group.

Holst, M. S., & Steensen, T. W. (2011). The successful enterprise architecture effort. Journal of Enterprise Architecture, 7(4), 16–22.

IBM. (2006). An introduction to IBM’s enterprise architecture consulting method. Armonk, NY: IBM Global Services.

Joseph, D. (2009). Trends in enterprise architecture: Virtualization, visualization, service-orientation, and personal architectures. Journal of Enterprise Architecture, 5(3), 9–17.

Kappelman, L., McLean, E., Johnson, V., & Gerhart, N. (2014). The 2014 SIM IT key issues and trends study. MIS Quarterly Executive, 13, 237–263.

Kappelman, L., McLean, E., Johnson, V., & Torres, R. (2016). The 2015 SIM IT issues and trends study. MIS Quarterly Executive, 15(1), 55–83.

Kappelman, L., McLean, E., Johnson, V., Torres, R., Nguyen, Q., Maurer, C., & Snyder, M. (2017). The 2016 SIM IT issues and trends study. MIS Quarterly Executive, 16(1), 47–80.

Karimi, J., & Walter, Z. (2015). The role of dynamic capabilities in responding to digital disruption: A factor-based study of the newspaper industry. Journal of Management Information Systems, 32(1), 39–81.

Keen, P., & Williams, R. (2013). Value architectures for digital busi ness: Beyond the business model. MIS Quarterly, 37, 643–648.

Kiat, S. E., Chiew, L. H., Hong, P. S., & Fung, C. C. (2008). The organization’s compass–Enterprise architecture. Journal of Enterprise Architecture, 4(1), 11–19.

Kieser, A. (1997). Rhetoric and myth in management fashion. Organization, 4, 49–74.

Kotusev, S. (2017a). Different approaches to enterprise architecture. Journal of Enterprise Architecture, 12(4), 9–16.

Kotusev, S. (2017b). Enterprise architecture: What did we study? International Journal of Cooperative Information Systems, 26(4), 1–84.

Kotusev, S., Singh, M., & Storey, I. (2015a). Consolidating enterprise architecture management research. In T. X. Bui & R. H. Sprague (Eds.), Proceedings of the 48th Hawaii International Conference on System Sciences (pp. 4069–4078). New York, NY: IEEE.

Kotusev, S., Singh, M., & Storey, I. (2015b). Investigating the usage of enterprise architecture artifacts. In J. Becker, J. vom Brocke, & M. de Marco (Eds.), Proceedings of the 23rd European Conference on Information Systems (pp. 1–12). Atlanta, GA: Association for Information Systems.

Lange, M., Mendling, J., & Recker, J. (2016). An empirical analysis of the factors and measures of enterprise architecture management success. European Journal of Information Systems, 25, 411–431.

Langenberg, K., & Wegmann, A. (2004). Enterprise architecture: What aspects is current Research targeting? (#IC/2004/77). Lausanne, Switzerland: Ecole Polytechnique Federale de Lausanne.

Lankhorst, M. (2013). Enterprise architecture at work: Modelling, communication and analysis (3rd ed.). Berlin, Germany: Springer.

Li, W., Liu, K., Belitski, M., Ghobadian, A., & O’Regan, N. (2016). e-Leadership through strategic alignment: An empirical study of small- and medium-sized enterprises in the digital age. Journal of Information Technology, 31, 185–206.

Longepe, C. (2003). The enterprise architecture IT project: The urbanisation paradigm. London, England: Kogan Page Science.

Miller, D. (2007). Paradigm prison, or in praise of atheoretic research. Strategic Organization, 5, 177–184.

Miller, D., & Hartwick, J. (2002). Spotting management fads. Harvard Business Review, 80(10), 26–27.

Miller, D., Hartwick, J., & Le Breton-Miller, I. (2004). How to detect a management fad—And distinguish it from a classic. Business Horizons, 47(4), 7–16.

Mykhashchuk, M., Buckl, S., Dierl, T., & Schweda, C. M. (2011). Charting the landscape of enterprise architecture management. In A. Bernstein & G. Schwabe (Eds.), Proceedings of the 9th International Conference on Wirtschaftsinformatik (pp. 570– 577). Atlanta, GA: Association for Information Systems.

Niemann, K. D. (2006). From enterprise architecture to IT governance: Elements of effective IT management. Wiesbaden, Germany: Vieweg.

Niemi, E., & Pekkola, S. (2017). Using enterprise architecture artefacts in an organisation. Enterprise Information Systems, 11, 313–338.

Nurcan, S., & Schmidt, R. (2009). Service oriented enterprisearchitecture for enterprise engineering introduction. In V. Tosic (Ed.), Proceedings of the 13th IEEE International Enterprise Distributed Object Computing Conference Workshops (pp. 247–253). New York, NY: IEEE.

Obitz, T., & Babu, M. (2009). Infosys Enterprise Architecture Survey 2008/2009. Bangalore, India: Infosys.

The Open Group. (2016). TOGAF users by market sector. Retrieved from http://web.archive.org/web/20151121161238/http:// www.opengroup.org/togaf/users-by-market-sector

The Open Group Architecture Framework. (2011). TOGAF Version 9.1 (#G116). Reading, UK: The Open Group.

Partnership for Research in Information Systems Management. (1986). PRISM: Dispersion and interconnection: Approaches to distributed systems architecture. Cambridge, MA: CSC Index.

Pulkkinen, M. (2006). Systemic management of architectural decisions in enterprise architecture planning. Four dimensions and three abstraction levels. In R. H. Sprague (Ed.), Proceedings of the 39th Hawaii International Conference on System Sciences (pp. 1–9). New York, NY: IEEE.

Radeke, F. (2010). Awaiting explanation in the field of enterprise architecture management. In M. Santana, J. N. Luftman, & A. S. Vinze (Eds.), Proceedings of the 16th Americas Conference on Information Systems (pp. 1–10). Atlanta, GA: Association for Information Systems.

Rahimi, F., Gotze, J., & Moller, C. (2017). Enterprise architecture management: Toward a taxonomy of applications. Communications of the Association for Information Systems, 40, 120–166.

Ross, J. W. (2011). Gaining competitive advantage from enterprise architecture (Executive Seminar: Enabling IT Value Through Enterprise Architecture). Retrieved from https:// www.youtube.com/watch?v=ScHG63YmJ2k&t=572

Ross, J. W., Sebastian, I., Beath, C., Mocker, M., Moloney, K., & Fonstad, N. (2016). Designing and executing digital strategies. In B. Fitzgerald, & J. Mooney (Eds.), Proceedings of the 37th International Conference on Information Systems (pp. 1–17). Atlanta, GA: Association for Information Systems.

Ross, J. W., Weill, P., & Robertson, D. C. (2006). Enterprise architecture as strategy: Creating a foundation for business execution. Boston, MA: Harvard Business School Press.

Saint-Louis, P., Morency, M. C., & Lapalme, J. (2017). Defining enterprise architecture: A systematic literature review. In S. Halle, R. Dijkman, & J. Lapalme (Eds.), Proceedings of the 21st IEEE International Enterprise Distributed Object Computing Conference Workshops (pp. 41–49). New York, NY: IEEE.

Schekkerman, J. (2004). How to survive in the jungle of enterprise architecture frameworks: Creating or choosing an enterprise architecture framework (2nd ed.). Victoria, British Columbia, Canada: Trafford Publishing.

Schekkerman, J. (2005). Trends in enterprise architecture 2005: How are organizations progressing? Amersfoort, The Netherlands: Institute for Enterprise Architecture Developments.

Schekkerman, J. (2006). Extended enterprise architecture framework essentials guide (Version 1.5). Amersfoort, The Netherlands: Institute for Enterprise Architecture Developments.

Schekkerman, J. (2008). Enterprise architecture good practices guide: How to manage the enterprise architecture practice. Victoria, British Columbia, Canada: Trafford Publishing.

Schmidt, C., & Buxmann, P. (2011). Outcomes and success factors of enterprise IT architecture management: Empirical insight from the international financial services industry. European Journal of Information Systems, 20, 168–185.

Schoenherr, M. (2008). Towards a common terminology in the discipline of enterprise architecture. In G. Feuerlicht, & W. Lamersdorf (Eds.), Proceedings of the 3rd Trends in Enterprise Architecture Research Workshop (pp. 400–413). New York, NY: Springer.

Scholtz, B., Calitz, A., & Connolley, A. (2013). An analysis of the adoption and usage of enterprise architecture. In A. Gerber, & P. van Deventer (Eds.), Proceedings of the 1st Enterprise Systems Conference (pp. 1–9). New York, NY: IEEE.

Shanks, G., Gloet, M., Someh, I. A., Frampton, K., & Tamm, T. (2018). Achieving benefits with enterprise architecture. Journal of Strategic Information Systems, 27, 139–156.

Sia, S. K., Soh, C., & Weill, P. (2016). How DBS bank pursued a digital business strategy. MIS Quarterly Executive, 15, 105–121.

Simon, D., Fischbach, K., & Schoder, D. (2013). An exploration of enterprise architecture research. Communications of the Association for Information Systems, 32(1), 1–72.

Simon, D., Fischbach, K., & Schoder, D. (2014). Enterprise architecture management and its role in corporate strategic management. Information Systems and E-Business Management, 12(1), 5–42.

Sowa, J. F., & Zachman, J. A. (1992). Extending and formalizing the framework for information systems architecture. IBM Systems Journal, 31, 590–616.

Spewak, S. H., & Hill, S. C. (1992). Enterprise architecture plan ning: Developing a blueprint for data, applications and technology. New York, NY: Wiley.

Tamm, T., Seddon, P. B., Shanks, G., & Reynolds, P. (2011). How does enterprise architecture add value to organisations? Communications of the Association for Information Systems, 28, 141–168.

Technical Architecture Framework for Information Management. (1996). Department of defense technical architecture framework for information management (Vol. 4, DoD Standards-Based Architecture Planning Guide, Version 3.0). Arlington County, VA: Defense Information Systems Agency.

Theuerkorn, F. (2004). Lightweight enterprise architectures. Boca Raton, FL: Auerbach Publications.

Treasury Enterprise Architecture Framework. (2000). Treasury enterprise architecture framework (Version 1). Washington, DC: Department of the Treasury.

van’t Wout, J., Waage, M., Hartman, H., Stahlecker, M., & Hofman, A. (2010). The integrated architecture framework explained: Why, what, how. Berlin, Germany: Springer.

Wagter, R., van den Berg, M., Luijpers, J., & van Steenbergen, M. (2005). Dynamic enterprise architecture: How to make it work. Hoboken, NJ: Wiley.

Wardle, C. (1984). The evolution of information systems architecture. In J. Nunamaker, J. L. King, & K. L. Kraemer (Eds.), Proceedings of the 5th International Conference on Information Systems (pp. 205–217). Atlanta, GA: Association for Information Systems.

Weill, P., & Olson, M. H. (1989). Managing investment in information technology: Mini case examples and implications. MIS Quarterly, 13(1), 3–17.

Weill, P., Ross, J. W., & Quaadgras, A. (2010). Achieving superior value from digitization: The MIT CISR value framework. Cambridge, MA: Center for Information Systems Research, MIT Sloan School of Management.

Weill, P., & Woerner, S. L. (2013a). Managing total digitization: The next frontier. Cambridge, MA: Center for Information Systems Research, MIT Sloan School of Management.

Weill, P., & Woerner, S. L. (2013b). Optimizing your digital business model. MIT Sloan Management Review, 54(3), 71–78.

Weill, P., & Woerner, S. L. (2018a). Is your company ready for a digital future? MIT Sloan Management Review, 59(2), 21–25.

Weill, P., & Woerner, S. L. (2018b). What’s your digital business model? Six questions to help you build the next-generation enterprise. Boston, MA: Harvard Business School Press.

Westerman, G., & Bonnet, D. (2015). Revamping your business through digital transformation. MIT Sloan Management Review, 56(3), 10–13.

Westerman, G., Bonnet, D., & McAfee, A. (2014). Leading digital: Turning technology into business transformation. Boston, MA: Harvard Business School Press.

Winter, R., & Fischer, R. (2006). Essential layers, artifacts, and dependencies of enterprise architecture. In A. Vallecillo

(Ed.), Proceedings of the 10th IEEE International Enterprise Distributed Object Computing Conference Workshops (pp. 30–37). New York, NY: IEEE.

Yeow, A., Soh, C., & Hansen, R. (2018). Aligning with new digital strategy: A dynamic capabilities approach. Journal of Strategic Information Systems, 27(1), 43–58.

Yin, R. K. (2003). Case study research: Design and methods (3rd ed.). Thousand Oaks, CA: SAGE.

Zachman, J. A. (1987). A framework for information systems architecture. IBM Systems Journal, 26, 276–292.

Zachman, J. A. (1996). Concepts of the framework for enterprise architecture: Background, description and utility. Monument, CO: Zachman International.

## Author biography

Svyatoslav Kotusev is a PhD Candidate in the School of Business IT and Logistics at RMIT University, Melbourne, Australia. He focuses on studying enterprise architecture practices in organizations. He is an author of the book The Practice of Enterprise Architecture: A Modern Approach to Business and IT Alignment and many articles on enterprise architecture that appeared in various outlets.

## Appendix A

## Analysis of research-based enterprise architecture sources

This appendix contains the analysis of rare comprehensive evidence-based enterprise architecture (EA) sources from the perspective of this study and its research question. Besides numerous anecdotal EA sources of questionable empirical validity (Bernard, 2012; DoDAF, 2007; Holcman, 2013; Lankhorst, 2013; Schekkerman, 2008; Spewak & Hill, 1992; TOGAF, 2011; van’t Wout et al., 2010), at least two comprehensive research-based EA sources are also available (Ahlemann, Stettiner, Messerschmidt, & Legner, 2012; Ross, Weill, & Robertson, 2006). However, due to the reasons described in great detail below, these sources still fail to provide adequate answers to the apparently simple research question of this study (“What EA artifacts are used in organizations and how they are used?”) and do not offer strong conceptualizations of EA that can be compared against the empirical findings.

Enterprise architecture as strategy (2006). The book “Enterprise Architecture as Strategy: Creating a Foundation for Business Execution” (Ross et al., 2006) is based on an extensive empirical research conducted mostly at the MIT Center for Information Systems Research (CISR) from 1995 to 2005 and including 68 case studies, surveys of 183 companies and additional data from the previous studies of IT governance (Ross et al., 2006, pp. ix–xi). This book is among the most widely known and highly cited EA sources (Mykhashchuk, Buckl, Dierl, & Schweda, 2011; Simon, Fischbach, & Schoder, 2013). However, due to a number of reasons, this book offers little in terms of understanding EA arti facts and their practical usage.

Most importantly, the very meaning of the term “enterprise architecture” used in this book is rather different from the commonly accepted meaning of this term adopted in the vast majority of EA publications including this article. This difference is explicitly acknowledged and clearly explained by the authors, for instance, in the following fragment of the book:

The enterprise architecture core diagrams we describe in this chapter are focused on communicating the high-level business process and IT requirements of a company’s operating model. They do not provide the necessary detail to map out technical or process design requirements. The IT unit typically addresses four levels of architecture below the enterprise architecture: business process architecture [. . .]; data or information architecture [. . .]; applications architecture [. . .]; and technology architecture [. . .]. The term enterprise architecture can be confusing because the IT unit in some companies refers to one of these architectures—or the set of all four architectures—as the enterprise architecture. Our use of the term refers to the high-level logic for business processes and IT capabilities. [. . .] Detailed architecture development conducted within the IT unit is an important element of building a foundation for execution. However, it is outside the scope of this book. (Ross et al., 2006, pp. 48–49)

Therefore, the term “enterprise architecture” in the book of Ross et al. (2006) refers only to the highest level organizing logic for business and IT, while more detailed architecture (“four levels of architecture below the enterprise architecture”) is simply out of the scope of this book. However, these four levels of architecture are typically considered as “enterprise architecture” in the rest of the EA literature including this article. In other words, “enterprise architecture” described in this book represents only a narrow top-level subset of broader “enterprise architecture” discussed in this article, or only “a small tip of the whole EA iceberg.” Importantly, this terminological inconsistency should not be considered as surprising since the term “enterprise architecture” was, in fact, picked by Jeanne Ross purely accidentally and never had any relationship to the same term used, for example, in EA frameworks:

When I started studying enterprise architecture it was never my intention to study enterprise architecture. In fact, I had studied it for five years before I gave it a name, and I thought I had come up with such a great name only to find out that it had been a name that had been around for a long time, Zachman and others had created the concept probably ten years earlier than I had. (Ross, 2011)

From the perspective of EA artifacts, due to the different, much more narrow understanding of the very term “enterprise architecture,” Ross et al. (2006) describe in detail only a single type of EA artifacts—core diagrams. Although other artifacts considered in this book as IT architecture, for example, technical standards and models, are also briefly mentioned in the text, the book does not provide detailed lists of these artifacts and does not describe their usage. Consequently, for the purposes of this article, the book of Ross et al. (2006) offers neither a detailed set of EA artifacts nor a comprehensive conceptualization of EA that can be confirmed or criticized. Put it simply, despite being based on extensive empirical research, this book provides an incomplete coverage of EA artifacts.

It is also important to realize that the book of Ross et al. (2006) is prescriptive in nature, that is, based on successful experience of some companies, it provides a recommended approach for other companies to follow, rather than describes what most companies are actually doing. This prescriptive attitude raises a number of questions regarding the relationship between the approach described in the book and actual industry realities. For instance, it is not clear (1) how many EA practitioners read the book and are aware of the recommended approach; (2) how many organizations actually adopted the recommended approach, even if the book is widely read; (3) to what extent and in what aspects the provided recommendations are followed; and (4) how the recommended approach differs from “average” mainstream approaches adopted in most organizations. For these reasons, the approach described by Ross et al. (2006) cannot be taken as-is as an adequate generalized representation of what is practiced in industry. Specifically from the perspective of EA artifacts, it is not clear how widely core diagrams recommended in the book are actually used among organizations (numerous interviews taken as part of this study suggest that (1) only some architects actually read this book, while most architects did not; (2) the terms “operating model,” “core diagram” and “IT engagement model” promoted by this book are rarely, if ever, used in organizations; (3) EA artifacts semantically equivalent to core diagrams are rather rarely used; (4) but most organizations still have an implicit understanding of their operating models, though without using the term “operating model” explicitly; and (5) IT engagement models are implemented in some or the other form in most organizations).

More interestingly, despite that the book itself is very widely cited in the literature (Mykhashchuk et al., 2011; Simon et al., 2013), the key ideas and the overall planning approach described by Ross et al. (2006), by some or the other reasons, remain largely unnoticed and ignored by the EA research community. Even though they are based on solid research, these ideas did not shape the mainstream view of EA prevalent in academic EA publications. This fact has multiple different manifestations in the existing EA literature including, but not limited to, the following ones.

First, the recent comprehensive EA literature review covering 1075 publications (Kotusev, 2017b) identifies only seven publications (Blomqvist, Halen, & Helenius, 2015; de Vries & van Rensburg, 2009; Fallmyr & Bygstad, 2014; Halen, Blomqvist, & Helenius, 2014; Harrell & Sage, 2010; Kiat, Chiew, Hong, & Fung, 2008; Nurcan & Schmidt, 2009) that intentionally discuss the ideas of Ross et al. (2006), for example, operating models, core diagrams and IT engagement models, and none of these publications appeared in the leading IS journals. At the same time, the overwhelming majority of the identified EA publications were, to different extents, based on the ideas of popular EA frameworks (FEAF, 1999; Sowa & Zachman, 1992; TOGAF, 2011).

Second, the latest EA publication from the basket of leading IS journals (Shanks, Gloet, Someh, Frampton, & Tamm, 2018, p. 139) opens with the statement that EA “defines the current and desirable future states of an organization’s processes, capabilities, application systems, data, and IT infrastructure and provides a roadmap for achieving this target from the current state,” which is wholly inspired by EA frameworks (FEAF, 1999; TOGAF, 2011), even though the book of Ross et al. (2006) is provided as one of the references to substantiate this claim. Likewise, the previous EA publication from the leading IS journal (Lange, Mendling, & Recker, 2016) even explicitly conceptualizes EA as a set of as-is architecture, to-be architecture and transformation roadmap, that is, in a manner imposed by EA frameworks, not by the book of Ross et al. (2006), even though this book is also cited in the article among other sources.

Finally, the very existence of different and inconsistent views of an EA practice is not widely acknowledged in the EA literature. For instance, there are only a very few publications (Kotusev, 2017a; Kotusev, Singh, & Storey, 2015a) explicitly comparing the ideas of EA frameworks with the ideas of Ross et al. (2006). It would be also arguably fair to say that the EA research community generally does not notice the difference between evidence-based recommendations of Ross et al. (2006) and speculative prescriptions of EA frameworks.

Strategic enterprise architecture management (2012). The book “Strategic Enterprise Architecture Management: Challenges, Best Practices, and Future Developments” (Ahlemann, Stettiner, et al., 2012b) is based on eight indepth case studies of large European companies conducted between the spring of 2009 and the autumn of 2010 by a joint team of 13 participants including researchers from EBS Business School and consultants from PricewaterhouseCoopers (PwC) (Ahlemann, Legner, & Schafczuk, 2012a, pp. 25–29). Despite being one of the most comprehensive research-based EA sources available today, this book is seemingly not widely known in the EA community, not particularly highly cited in the academic EA literature and undeservingly still remains largely unnoticed.

This book focuses specifically on “enterprise architecture management” (EAM) defined as

a management practice that establishes, maintains and uses a coherent set of guidelines, architecture principles and governance regimes that provide direction for and practical help with the design and the development of an enterprise’s architecture in order to achieve its vision and strategy. (Ahlemann, Legner, & Schafczuk, 2012a, p. 20)

Accordingly, this book describes in great detail the integration of EA-related management processes into regular organizational processes including strategic planning, project life cycle, operations and monitoring as well as some other important aspects of an EA practice, for example, EA modeling and tools. However, due to its intentional process-centricity, this book pays little attention to EA artifacts and their usage. In particular, the book barely mentions specific EA artifacts, does not discuss in detail any of them and hardly explains how exactly they are used as part of EAM. An evidence-based conceptualization of EA in this book is also missing.

All the facts discussed above suggest that despite the existence of some comprehensive evidence-based EA sources (Ahlemann, Stettiner, et al., 2012b; Ross et al., 2006), a detailed understanding of EA artifacts and their usage in an EA practice is still missing. Moreover, even in the presence of significantly different views on EA, including the planning approach recommended by Ross et al. (2006), by some or the other reasons for the vast majority of people EA is closely associated, if not synonymous, with popular EA frameworks (FEAF, 1999; TOGAF, 2011; Zachman, 1987). Unsurprisingly, most people involved in EA research seemingly still consider EA either as a set of business, data, application and technology architectures, or as a set of current states, future states and roadmaps, as conceptualized by these EA frameworks.

## Appendix B

## List of studied organizations

This appendix contains the lists of organizations studied as part of the exploratory and confirmatory phases of this research.

Exploratory phase. The list of organizations studied in great detail during the exploratory phase of this research is provided in Table 3. These organizations satisfied the following selection criteria: (1) large organizations employing at least 100 full-time IT staff, (2) having permanent EA teams and consistent EArelated processes and (3) practicing EA at least for 3years.

Table 3. Organizations studied during the exploratory phase.

<table><tr><td>Organization</td><td>Industry</td><td>Size</td><td>EA experience</td></tr><tr><td>Organization 1</td><td>Education</td><td>More than 7000 employees and 500 IT employees</td><td>More than 3 years</td></tr><tr><td>Organization 2</td><td>Finance</td><td>More than 40,000 employees and 3000 IT employees</td><td>More than 8 years</td></tr><tr><td>Organization 3</td><td>Telecom</td><td>More than 4000 employees and 500 IT employees</td><td>More than 6 years</td></tr><tr><td>Organization 4</td><td>Delivery</td><td>More than 30,000 employees and 500 IT employees</td><td>More than 5 years</td></tr><tr><td>Organization 5</td><td>Retail</td><td>More than 80,000 employees and 1000 IT employees</td><td>More than 4 years</td></tr></table>

EA: enterprise architecture.

Confirmatory phase. The list of organizations studied in less detail during the confirmatory phase of this research is provided in Table 4. These organizations satisfied the following selection criteria: (1) no specific size requirements, (2) have permanent architecture teams and (3) practice EA at least for 1–2 years.

Table 4. Organizations studied during the confirmatory phase.

<table><tr><td>Organization</td><td>Industry</td><td>Size</td><td>EA experience</td></tr><tr><td>Organization 6</td><td>Education</td><td>~5000 employees and ~250 IT employees</td><td>~2 years</td></tr><tr><td>Organization 7</td><td>Finance</td><td>More than 40,000 employees and 5000 IT employees</td><td>More than 10 years</td></tr><tr><td>Organization 8</td><td>Education</td><td>More than 5000 employees and 200 IT employees</td><td>~3 years</td></tr><tr><td>Organization 9</td><td>Transport</td><td>~2000 employees and ~300 IT employees</td><td>More than 5 years</td></tr><tr><td>Organization 10</td><td>Emergency</td><td>~2100 employees and ~60 IT employees</td><td>~1 year</td></tr><tr><td>Organization 11</td><td>Emergency</td><td>More than 17,000 employees and 300 IT employees</td><td>More than 5 years</td></tr><tr><td>Organization 12</td><td>Automobile</td><td>~2600 employees and ~120 IT employees</td><td>~2.5 years</td></tr><tr><td>Organization 13</td><td>Finance</td><td>~250 employees and ~40 IT employees</td><td>~3 years</td></tr><tr><td>Organization 14</td><td>Marketing</td><td>~2500 employees and ~600 IT employees</td><td>~2 years</td></tr><tr><td>Organization 15</td><td>Resources</td><td>~80,000 employees and several thousand IT employees</td><td>More than 10 years</td></tr><tr><td>Organization 16</td><td>Finance</td><td>~7000 employees and ~500 IT employees</td><td>~5 years</td></tr><tr><td>Organization 17</td><td>Government</td><td>~250 employees and ~100 IT employees</td><td>~1 year</td></tr><tr><td>Organization 18</td><td>Energy</td><td>~2500 employees, ~25 permanent in IT + outsourcers</td><td>~4 years</td></tr><tr><td>Organization 19</td><td>Retail</td><td>More than 20,000 employees and 500 IT employees</td><td>More than 5 years</td></tr><tr><td>Organization 20</td><td>Insurance</td><td>~20,000 employees and ~1500 IT employees</td><td>More than 5 years</td></tr><tr><td>Organization 21</td><td>Food</td><td>~1600 employees, ~15 permanent in IT + partners</td><td>~1 year</td></tr><tr><td>Organization 22</td><td>Manufacturing</td><td>~3500 employees, only ~4 permanent in IT + partners</td><td>~3 years</td></tr><tr><td>Organization 23</td><td>Telecom</td><td>More than 30,000 employees and 3000 IT employees</td><td>~2 years</td></tr><tr><td>Organization 24</td><td>Government</td><td>~2500 employees and ~400 IT employees</td><td>~4 years</td></tr><tr><td>Organization 25</td><td>Resources</td><td>~6000 employees and ~550 IT employees</td><td>More than 6 years</td></tr><tr><td>Organization 26</td><td>Resources</td><td>~2000 employees and ~200 IT employees</td><td>More than 5 years</td></tr><tr><td>Organization 27</td><td>Delivery</td><td>~8000 employees and ~500 IT employees</td><td>~5 years</td></tr></table>

EA: enterprise architecture.

## Appendix C

## Schematic structures of EA artifacts

This appendix contains schematic graphical structures of all the 24 EA artifacts identified in this study in order of their relative popularity: Solution Designs, Roadmaps, Technology Reference Models, Principles (shown in Figure 1), Business Capability Models, Guidelines,

Solution Overviews, Landscape Diagrams (shown in Figure 2), IT Roadmaps, Inventories, Patterns, IT Principles (shown in Figure 3), Options Assessments, Target States, Enterprise System Portfolios, Policies (shown in Figure 4), Initiative Proposals, Preliminary Solution Designs, Conceptual Data Models, Direction Statements (shown in Figure 5), Logical Data Models, Analytical Reports, Context Diagrams and Value Chains (shown in Figure 6).

![](/api/attachments/V5U75PGR/fulltext/images/d450527ead6bc86b5e9342e3aa284336324a28341a1d0cfe30c62be90f1494ba.jpg)  
Figure 1. Schematic graphical structures of EA artifacts (part 1).

<table><tr><td rowspan="2">Server Deployment Standards</td><td>Guideline 1: Run Applications as OS Services Description: ......</td></tr><tr><td>Guideline 2: Store Deployment Packages in VCS Description: ......</td></tr><tr><td rowspan="2">Network Protocol Standards</td><td>Guideline 3: Avoid Using UDP Multicast Description: ......</td></tr><tr><td>Guideline 4: Prefer REST Over SOAP Description: ......</td></tr><tr><td rowspan="2">Data Encryption Standards</td><td>Guideline 5: Use 256-Bit Encryption Keys Description: ......</td></tr><tr><td>Guideline 6: Store MD5 Hashes of Passwords Description: ......</td></tr><tr><td rowspan="2">Interface Design Guidelines</td><td>Guideline 7: Use Web-Safe Colours Description: ......</td></tr><tr><td>Guideline 8: Place Menu in the Top Right Corner Description: ......</td></tr><tr><td rowspan="2">Secure Coding Guidelines</td><td>Guideline 9: Initialize Variables to Safe Defaults Description: ......</td></tr><tr><td>Guideline 10: Validate All Incoming Data Description: ......</td></tr></table>

![](/api/attachments/V5U75PGR/fulltext/images/4fa7475a34c934944dcde1db6b147f02c3c04e8b5f8c8e4d1633c975ffa3302c.jpg)  
Figure 2. Schematic graphical structures of EA artifacts (part 2).

![](/api/attachments/V5U75PGR/fulltext/images/4b3390e558cc65fe8e64df3a6e0136c49adb90f614b4a826203e82a1e86e2cec.jpg)  
Figure 3. Schematic graphical structures of EA artifacts (part 3).

<table><tr><td rowspan="2">Applications</td><td>IT Principle 1: Prefer Open Source Solutions Description: ......</td></tr><tr><td>IT Principle 2: Log All Main Operations Description: ......</td></tr><tr><td rowspan="2">Data</td><td>IT Principle 3: Use Scalable Storage Description: ......</td></tr><tr><td>IT Principle 4: Backup All Permanent Data Description: ......</td></tr><tr><td rowspan="2">Integration</td><td>IT Principle 5: Use Middleware for Integration Description: ......</td></tr><tr><td>IT Principle 6: Avoid Binary Integration Protocols Description: ......</td></tr><tr><td rowspan="2">Infrastructure</td><td>IT Principle 7: Host in the Cloud Description: ......</td></tr><tr><td>IT Principle 8: Dedicated Server for Each System Description: ......</td></tr><tr><td rowspan="2">Security</td><td>IT Principle 9: Place Public Systems in DMZ Description: ......</td></tr><tr><td>IT Principle 10: Secure by Default Description: ......</td></tr></table>

Options Assessments (29.6%)  
![](/api/attachments/V5U75PGR/fulltext/images/feb494e4a83b29ea278c21b25d215ee3dcbd06bd44d8c5d53cd7b9092acafa68.jpg)

![](/api/attachments/V5U75PGR/fulltext/images/5c5df69af7bdcb6588e28c28b1a0cefa6f954cc1b670e206cc6374b10a54d6db.jpg)

Enterprise System Portfolios (25.9%)  
![](/api/attachments/V5U75PGR/fulltext/images/fe9b10c88e0fa655e57c3412cdf1415a7ed800e013cbd8e834b02e853eeeaa95.jpg)  
Figure 4. Schematic graphical structures of EA artifacts (part 4).

Policies (22.2%)

<table><tr><td rowspan="4">External</td><td rowspan="2">National Privacy Policies</td><td>Policy 1: Personal Data Must Be Stored Onshore Description:......</td></tr><tr><td>Policy 2: Destroy Personal Data When Not Needed Description:......</td></tr><tr><td rowspan="2">Sarbanes-Oxley Policies</td><td>Policy 3: Log All Accesses to Accounting Systems Description:......</td></tr><tr><td>Policy 4: Retain Audit Trails and Emails for 5 Years Description:......</td></tr><tr><td rowspan="6">Internal</td><td rowspan="2">Data Security Policies</td><td>Policy 5: No Sensitive Data on Mobile Devices Description:......</td></tr><tr><td>Policy 6: Store Credit Cards in Encrypted Formats Description:......</td></tr><tr><td rowspan="2">Data Exchange Policies</td><td>Policy 7: Do Not Share Key Data with Third Parties Description:......</td></tr><tr><td>Policy 8: Share Client Data with Trusted Partners Description:......</td></tr><tr><td rowspan="2">Cloud Hosting Policies</td><td>Policy 9: Use Only the PCI DSS Compliant Cloud Description:......</td></tr><tr><td>Policy 10: Do Not Store Health Data in the Cloud Description:......</td></tr></table>

![](/api/attachments/V5U75PGR/fulltext/images/41f97342466ab2278b4512aae79857d6bdfe5f79f0c30ac9ea0b22e6474ecf88.jpg)

## Initiative Proposals (18.5%)

2. Goals and Objectives

3. Anticipated Benefits

4. Scope and Stakeholders

6. Preliminary EstimationsTime: 6-12 monthsCost: \$1.5-3.0 million

## Preliminary Solution Designs (18.5%)

3. Scope and Stakeholders

5. Involved Partners

4. Business Requirements

• IBM • Accenture

Figure 5. Schematic graphical structures of EA artifacts (part 5).  
![](/api/attachments/V5U75PGR/fulltext/images/9511a5d0641d64593efc51d274f1db945b68ec3a5a355b85caeed9ec641da8dc.jpg)

## Conceptual Data Models (14.8%)

• Java EE Platform • IBM BPM and DB2

7. Accurate Estimations Time: 8-9 months Cost: \$2.1-2.3 million

8. Technical Risks

## Direction Statements (14.8%)

1. Current Business Strategy

2. Identified IT Capability Gaps Inability to provide a timely and comprehensive trends analysis to relevant business stakeholders

3. Recommended Strategic Direction for IT Introduce a data warehouse aggregating relevant data from all IT systems to enable the analytical capability

![](/api/attachments/V5U75PGR/fulltext/images/5fba5c400536d56251ab5fc5df8a7bee1dfebb5501bbec81e2baa0dda3c0f49e.jpg)

![](/api/attachments/V5U75PGR/fulltext/images/cc069ec185c1ada291136ab183f73b8c51a4f247ac0194ea9328d8537b035df6.jpg)  
Figure 6. Schematic graphical structures of EA artifacts (part 6).
