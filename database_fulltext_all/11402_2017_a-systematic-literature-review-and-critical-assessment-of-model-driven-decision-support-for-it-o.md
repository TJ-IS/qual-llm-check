---
otero_id: 11402
otero_key: "VMG4VDBV"
title: "A systematic literature review and critical assessment of model-driven decision support for IT outsourcing"
authors: "Mohammad Mehdi Rajaeian; Aileen Cater-Steel; Michael Lane"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.07.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

A systematic literature review and critical assessment of modeldriven decision support for IT outsourcing

ELSEVIER Decision Support Systems

Mohammad Mehdi Rajaeian, Aileen Cater-Steel, Michael Lane

![](/api/attachments/VMG4VDBV/fulltext/images/b8a92a95238d9a5f95c6b680001a878bc65a9b589dcdc82bed4b7eaf0b084218.jpg)

PII: S0167-9236(17)30124-0

DOI: doi: 10.1016/j.dss.2017.07.002

Reference: DECSUP 12863

To appear in: Decision Support Systems

Received date: 12 November 2016

Revised date: 31 May 2017

Accepted date: 6 July 2017

Please cite this article as: Mohammad Mehdi Rajaeian, Aileen Cater-Steel, Michael Lane , A systematic literature review and critical assessment of model-driven decision support for IT outsourcing, Decision Support Systems (2017), doi: 10.1016/j.dss.2017.07.002

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# A systematic literature review and critical assessment of model-driven decision support for IT outsourcing

Mohammad Mehdi Rajaeian<sup>\*1</sup>, Aileen Cater-Steel<sup>2</sup>, Michael Lane<sup>3</sup>

1, 2, 3: School of Management and Enterprise, University of Southern Queensland (USQ), Australia

\* Corresponding author, email: MohammadMehdi.Rajaeian@usq.edu.au

# A systematic literature review and critical assessment of model-driven decision support for IT outsourcing

## Abstract

Information technology outsourcing (ITO) is a widely-adopted strategy for IT governance. The decisions involved in IT outsourcing are complicated. Empirical research confirms that a rational and formalized decision-making process results in better decision outcomes. However, formal and systematic approaches for making ITO decisions appear to be scarce in practice. To support organizational decision-makers involved in IT outsourcing (including cloud sourcing), researchers have suggested several decision support methods. To date there is no comprehensive review and assessment of the research in this domain. In this study 133 model-driven decision support research articles for IT outsourcing and cloud sourcing were identified through a systematic literature review and assessed based on a highly-regarded research framework. An analysis of these 133 research articles suggested a range of Multiple Criteria Decision Making (MCDM), optimization and simulation methods to support different IT outsourcing decisions. Our findings raise concerns about the limited use of reference design theories, and the lack of validation and naturalistic evaluation of the decision support artifacts reported in ITO decision support literature. Based on the review, we provide future research directions, as well as a number of recommendations to enhance the rigor and relevance of ITO Decision Support Systems research.

Keywords - IT Outsourcing; Cloud Sourcing; Model-driven Decision Support; Research Evaluation; Systematic Literature Review

## 1. Introduction

IT outsourcing (ITO) is an established IT governance strategy and IT outsourcing decisions are vital for organizations. The ITO industry is expanding continuously [1], shaped by intricate multi-

# ACCEPTED MANUSCRIPT

sourced environments and disruptive technologies such as cloud computing. In practice, despite the widespread adoption of ITO, not all organizations are satisfied with their ITO initiatives. There are numerous cases of ITO failure or dissatisfaction reported in the literature [e.g. 2, 3, 4]. In addition, some organizations that adopted ITO, later decide to abandon their ITO initiative and bring their IT back in-house due to dissatisfaction with ITO outcomes or due to internal or external organizational changes. The following instance exemplifies a case in which an organization changed its IT sourcing model over time: “Kellwood’s multimillion dollar IT outsourcing deal with EDS served it well for many years. But after significant organizational changes and intense investigation of the 13-year deal, it became clear that insourcing was the best way for the apparel maker to save money moving forward … Analysis revealed that … insourcing IT would not only streamline IT services and provide greater flexibility than outsourcing; it would also generate even more cost savings” [5]. As another example, in 2002 JPMorgan announced its seven-year, five billion dollars outsourcing arrangement with IBM, which was at the time the largest outsourcing deal on record. However, in 2005, the company decided to end the contract with IBM and bring its IT back in-h use [6]. These examples clearly show the complexity and the risks involved in ITO decisions and highlight the importance of a comprehensive and prudent ITO decision-making process for organizations. Moreover, the complex nature of ITO decision-making is a well-recognized and agreed upon fact among academic ITO researchers [7-9]. In addition, empirical research confirms that a rational and formalized decision-making process results in better decision outcomes [10], and the lack of a structured and systematic approach to IT outsourcing (ITO) decision making in practice is frequently highlighted in the literature [11-15].

The research into IT outsourcing is extensive and IT outsourcing decisions have been the subject of both descriptive and normative research for nearly three decades. The descriptive strand, with adoption of various theories from different disciplines, seeks to understand the processes by which organizations make ITO decisions and also to understand the outcomes of those decisions [16]. The normative strand, which includes model-driven Decision Support Systems (DSS) research, is concerned more with how organizations can make effective ITO decisions. The increase in adoption, volume and complexity of ITO has prompted academic researchers to develop various model-driven decision artifacts to support practitioners in their ITO decision making. However, these decisionsupport artefacts have not been identified and assessed in one place, e.g. in a literature review paper, and have not been critically assessed for rigor and relevance. Moreover, the normative ITO research should exploit the findings of descriptive ITO research to develop rigorous and scientific-grounded DSS for ITO initiatives. However, to the best of authors’ knowledge there is no study that investigates whether research-based decision support artifacts are built on descriptive ITO research findings or not. Furthermore, previous empirical studies have raised concerns about the limited impact of ITO research on decision making in practice [e.g. 10, 13, 17]. For instance, Westphal and Sohal [10] noted: “ITO decisions seem to be made without the use of any of the decision models [proposed by researchers]”.

To address these research problems, a literature review approach was adopted in this study. The need for and importance of literature reviews in the IS discipline has been recently highlighted [e.g. 18, 19] because such papers provide reflection on prior research and provide a foundation for future studies and can be used to raise practitioners’ awareness of extant research. Although there are several journal articles that provide reviews of the descriptive ITO literature [e.g. 16, 20, 21-23], to date, to the best of our knowledge, there is little in the way of a comprehensive review of normative ITO literature, i.e. ITO decision support models/tools. Thus, there is no assessment of this body of literature available to provide a comprehensive account to practitioners who may be in search of a decision support tool for their ITO decisions or to researchers who wish to expand the depth and breadth of the field. To address this gap, we focused our study on the following research questions:

RQ1: What decision analysis methods have been suggested in the literature to support organizational IT outsourcing decisions?

RQ2: What level of rigor is evident in the model-driven artifacts developed to support organizational IT outsourcing decisions?

This article provides a systematic review of the model-driven ITO decision support literature in order to provide a critical assessment of work to date. Model-driven DSSs (also called model-oriented

DSS or computationally-oriented DSS) use quantitative models including algebraic, decision analytic, financial, simulation, and optimization models to provide decision support functionality [24, 25].

As a result of this systematic literature review, we identify that model-driven decision support for IT outsourcing can be categorized according to the type of decision being supported and the type of decision-making method used.

This study is significant in its comprehensive assessment of the body of knowledge pertaining to the ITO decision-support field, identification of its weaknesses, and suggestions of a rigorous foundation for future designs of ITO decision support systems.

This paper is organized as follows. In section 2, prior research with regard to evaluation and assessment of DSS research, decision analysis methods, and descriptive ITO decision-making research is briefly discussed to provide the background to the study. In section 3, the literature review survey method and sample are described. In section 4, the results of the literature survey are provided. recommendations for improvement and suggest further research directions.

## 2. Background research

## 2.1.Approaches used for assessment of DSS

Classic assessment frameworks and models [e.g. 26, 27, 28] have been criticized for their lack of “a holistic worldview that considers jointly the organizational, user, designer and builder criteria of interest” [29, p.643]. Several studies [e.g. 30, 31-33] have reviewed and assessed the DSS literature using a design science-based approach as a superior strategy for assessment of DSS research, since it takes the entire range of development activities into consideration [34]. For instance, Arnott and Pervan [31] conducted a content analysis of 1,093 DSS articles published in 14 major journals from 1990 to 2004 and used Hevner, March, Park and Ram’s [35] design science research (DSR) guidelines to assess the rigor and relevance of the academic field of DSS. Their analysis highlighted the main areas of weakness, i.e. evaluation, research design, and lack of supporting theory, and suggested that the rigor of DSS research is in need of improvement. In a similar vein, motivated by suggestions from Arnott and Pervan [30-32] and drawing on socio-technical design for IS development [36], Miah, Debuse and Kerr [34] proposed a conceptual DSS assessment approach based on the DSR framework of Peffers, Tuunanen, Rothenberger and Chatterjee [37].

## 2.2.Descriptive ITO decision-making research

IT Outsourcing, also known as Information Systems (IS) outsourcing, is defined as “handing over to a third party, management of IT/IS assets, resources, and/or activities for a required result” [38, operations, applications development and maintenance, network and telecommunications management, help desk and end-user support, and systems planning and management [39]. In this paper, we use IT outsourcing as a generic term that covers various ways to obtain IT resources/services from external organizations. IT outsourcing includes IT offshoring, net-sourcing, and cloud-sourcing. Net-sourcing means accessing centrally managed business applications provided by Application Service Providers (ASPs) to multiple users from a shared facility over the Internet for rent or pay per use [40, 41]. In offshoring or offshore outsourcing the service provider and the client firm are located in different countries [42]. organizations to purchase IT resources and capabilities from another organization as a service [43]. Cloud sourcing involves similar decisions to traditional ITO such as decision to adopt cloud services and service/provider selection [44]. Nevertheless, cloud computing differs from IT outsourcing in some key aspects. One key difference is the lack of fixed long-term contracts for cloud services that gives more control and flexibility to clients compared to traditional IT outsourcing [45]. Although outsourcing encompasses a wide range of sourcing options, purchasing goods or services cannot be considered as outsourcing, except in the case of make or buy decisions in which the goods or services were previously provided internally [46] or could have been provided internally. For instance, when an organization purchases Microsoft Office software, the decision cannot be considered as outsourcing, since the internal provision of the software is almost never an option.

This section presents a brief summary of the prior literature reviews of descriptive ITO decision making research [16, 20, 21, 23, 47]. Later we apply the knowledge gained from the descriptive ITO research to suggest recommendations for improvement of ITO normative research (i.e. ITO DSS).

Empirical research suggests that the main decision makers in ITO decisions are IS/IT executives (e.g. CIOs) and other top management executives (e.g. CEOs), and that decisions are normally made through group decision making processes [16, 20, 48]. The various decisions that have typically been the subject of research in the ITO decisions category include: to outsource or not?, which IT supplier is better to select?, should the organization consider offshore outsourcing? [16, 20, 23]. Dibbern, Goles, Hirschheim and Jayatilaka [20] mapped these decisions across two distinct phases of the IT outsourcing process – decision process and the implementation process (Figure 1). In this stage model, four types of ITO decisions (why, what, which, how) are situated across the two phases, and the details of each decision are presented under ‘application of outsourcing stages’. We discuss these four types of ITO decisions in more detail in the rest of this section.

![](/api/attachments/VMG4VDBV/fulltext/images/7f877512e9edec4e37c65e85ff3aa4d0584da7a310d1c7257fa3a7357d4865f8.jpg)  
Figure 1. Stage model of IT/IS outsourcing. Source: Adapted from Dibbern, Goles, Hirschheim and Jayatilaka [20]

As Figure 1 shows, organizations should first decide whether to outsource or not. In other words, they should answer why an organization might consider outsourcing its IS/IT functions? This question is not always easily answered. To answer this why question, the determinants or antecedents that might contribute to a decision to outsource and the risks and rewards, or advantages and disadvantages, associated with outsourcing should be determined. Most ITO decisions involve many complexities due to involvement of numerous factors in decision making [49], both technological and business factors [50], some of them with uncertain value [51], and very convoluted interrelationships among the factors [52].

It is recognized that no single theory can fully explain the multifaceted practices involved in IT outsourcing [23, 53, 54]. The high level of complexity of IT outsourcing decisions has led to the use of many theories from diverse disciplines such as economics, management, psychology, behavioral science and technology to endeavor to better understand the decision-making process in ITO. The range of theories that have been applied by researchers to investigate IT outsourcing include Transaction Cost Theory (TCT) [e.g. 55]; Agency Theory [e.g. 53]; Knowledge based Transaction Costs (KTC) [e.g. 56]; Path Dependence Theory [e.g. 57]; Prospect Theory [e.g. 56]; Game Theory [e.g. 58]; Social Exchange Theory [e.g. 59]; Diffusio nnovation Theory [e.g. 60]; Power and Politics theories [e.g. 46]; Social Capital Theory [e.g. 61]; Theory of Institutional Isomorphism [e.g. 49]; Resource-Based Theory/View (RBT/RBV) [e.g. 62]; Strategic Management theories (Taxonomy of Defenders, Prospectors, and Analyzer; theories of Strategic Advantage) [e.g. 63]; Knowledge-[e.g. 65].

The main factors that motivate firms to outsource their IT/IS include cost reduction, focus on core capabilities, access to external expertise/skills and technology/innovation, business/process performance improvements, flexibility enablement, commercial exploitation (to partner with a supplier to commercially exploit existing client assets or form a new enterprise), scalability, rapid delivery, cost predictability and head count reduction/stabilization. On the other hand, ITO can confront organizations with a range of risks and challenges. These risks include loss of control, security/intellectual property issues, high transaction costs and potential conflicts in relationships with IT service provider(s). Furthermore, there are specific characteristics of the client firm (outsourcer)

that could affect the ITO decision including firm size, industry, prior firm/IT department performance, IT department size, culture, critical role of IS in the firm, information intensity, firm’s experience with outsourcing, financial position, and business strategy [16].

The second main decision in the ITO process is what to outsource? The answers to why to outsource? from the previous stage can be used as criteria to evaluate the options available when asking what to outsource?. Five fundamental parameters should be considered at this stage: first, degree of outsourcing, which can be selective or total depending on the extent of IT assets, leases, staff and management responsibility for delivery of IT services that are transferred to the vendor in the outsourcing arrangement [66]; second, ownership of the outsourcing arrangement which can be external (wholly owned by vendor), partial (joint-venture), or internal (spin-offs wholly owned subsidiary); third, outsourcing mode which can be single vendor - single client, single vendor - multiple clients, multiple vendors - single client, or multiple vendors - multiple clients; fourth, time frame (short term or long term); and fifth, sourcing service delivery model (traditional ITO, cloud computing, etc.) [20, 43].

The next question faced is which choice to make? This refers to procedures to arrive at an choice; and the actual selection of the final decision [20]. The actual decision-making processes that lead to ITO decisions are still unknown, and considered as a black-box that needs to be investigated [23]. What we know about the ITO decision making process is limited to some of its attributes (characteristics) rather than an in-depth understanding of the actual decision-making process as it is practiced in the real world. For example, past studies revealed that ITO decisions are not necessarily the result of decision makers’ rational choice, instead various political or institutional forces (e.g. mimetic or bandwagon effect) can influence them. Hsieh and Huang [67] argued that three main concepts characterize the ITO decision-making process practiced in organizations. First, ITO decisions are negotiated outcomes, i.e. decisions are negotiated via internal or external interest groups rather than being made independently by decision maker(s). Second, ITO decisions are contextdependent i.e. situated in a specific internal or external context that is influenced by environmenta factors or organizational structures. Third, ITO decisions are not isolated, but interwoven [68] and interlinked with earlier decisions, thus previous decisions may impact on subsequent decisions.

Once the decision to outsource has been made, the next question is how to outsource?. The major decision in this stage is vendor (service provider) selection. Vendor selection comprises various variables such as vendors’ location (on-shore, offshore), expertise, service quality, cost and prior client/supplier working relationship.

## 2.3.Decision analysis and multi-criteria decision-making methods

Decision analysis is widely recognized as a sound prescriptive theory [69]. According to Parnell, Bresnick, Tani and Johnson [70] the term decision analysis was coined by Howard [71, p.2] and defined as “a body of knowledge and professional practice for the logical illumination of decision problems” and regarded as the application of decision theory [72]. A more detailed definition of decision analysis is provided by Clemen and Reilly [73]: “decision analysis provides effective methods for organizing a problem into a structure that can be analyzed. In particular, elements of a decision’s structure include the possible courses of action, the possible outcomes that could result, the likelihood of those outcomes, and eventual consequences (e.g., costs and benefits) to be derived from the different outcomes”.

To overcome bounded rationality [74, 75] and restrictions of humans to evaluate trade-off alternatives, scholars have been in pursuit of methods to support decision makers to make optimal decisions. As a result, the Multi-Criteria Decision-Making (MCDM) or Multiple-Criteria Decision Analysis (MCDA) discipline has emerged and various methods have been developed over the past five decades [76]. MCDM methods have been applied to solve real world problems with multiple and conflicting criteria in various domains. MCDM methods are divided into two categories: Multi-Objective Decision-Making (MODM) and Multi-Attribute Decision-Making (MADM) [76, 77]. MODM methods include decision variable values that are determined in a continuous or integer domain with either an infinite or a large number of alternative choices, to best satisfy the decision maker’s constraints, preferences or priorities. MADM methods, on the other hand, have been used to solve problems with discrete decision spaces and a predetermined or a limited number of alternative choices, requiring criterion comparisons, and involving implicit or explicit trade-offs [69].

A brief description of the most frequently adopted MCDM decision making approaches to support ITO decisions is provided in Table 1. These methods are widely used in the ITO decision support literature and will be discussed in section 4.

Table 1. A brief description of the MCDM approaches applied in ITO literature

<table><tr><td>Decision method</td><td>Description</td><td>Pioneer author(s)</td></tr><tr><td>AHP (Analytic Hierarchy Process)</td><td>AHP simplifies complex problems by arranging decision attributes and alternatives in a hierarchical structure and ranks alternatives by use of a series of pairwise comparisons and relies on judgements of experts to derive priority scales.</td><td>Saaty [78], Saaty [79], Saaty [80]</td></tr><tr><td>ANP (Analytic Network Process)</td><td>A generalization of AHP for dealing with decisions that cannot be structured in hierarchy because of interdependence and interaction between decision attributes.</td><td>Saaty [81], Saaty [82]</td></tr><tr><td>ELECTRE (ELimination Et Choix Traduisant la REalité)</td><td>ELECTRE belongs to outranking methods and is based on pairwise comparison of the alternatives in which every option is compared to all other options.</td><td>Roy [83]</td></tr><tr><td>PROMETHEE (Preference Ranking Organization METHOD for Enrichment of Evaluations)</td><td>This method provides decision maker with a ranking of choices/alternatives based on preference degrees. A preference degree is a score between 0 and 1 which shows how much a choice/alternative is preferred over another one.</td><td>Brans, Vincke and Mareschal [84]</td></tr><tr><td>TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)</td><td>The fundamental concept of TOPSIS is that the chosen alternative should have shortest geometric distance from the positive ideal solution and the longest geometric distance from the negative ideal solution. It allows trade-offs between criteria, where a poor result in one criterion can be neutralized by a good result in another criterion.</td><td>Hwang and Yoon [77], Yoon [85]</td></tr><tr><td>VIKOR (VIseKriterijumska Optimizacija I Kompromisno Resenje)</td><td>VIKOR employs liner normalization to rank alternatives and determines the solution (named compromise) that is the closest to ideal</td><td>Opricovic [86], Opricovic and Tzeng [87]</td></tr><tr><td>Weighted-Criteria Evaluation</td><td>Simple Additive Weighting (SAW) or Weighted Sum Model (WSM) determines a weighted score for each alternative by adding contributions of each attribute multiplied by their weights.</td><td>Fishburn [88]</td></tr><tr><td>Goal programming</td><td>Goal programming is the application of linear programming to solve problems with multiple objects that can be conflicting.</td><td>Charnes, Cooper and Ferguson [89], Charnes and Cooper [90]</td></tr><tr><td>LINMAP (Linear Programming Technique for Multidimensional Analysis of Preference)</td><td>LINMAP receives the pair-wise alternatives&#x27; comparisons given by decision maker as input and generates best compromise alternative (or solution) that has the shortest distance to positive ideal solution.</td><td>Srinivasan and Shocker [91]</td></tr><tr><td>Fuzzy set theory</td><td>Fuzzy set theory has been designed to mathematically represent uncertainty and vagueness and provide formalized tools for dealing with imprecision inherent to decision-making problems that involve subjective (qualitative) evaluation indices in which the assessment relies on decision-makers&#x27; linguistic judgment that carries inherent impression, vagueness and to some extent uncertainty due to variation in human perception.</td><td>Zadeh [92], Zadeh [93]</td></tr></table>

## 3. Methodology

In this paper we adopted a systematic literature review methodology [94, 95], to identify peer reviewed articles that developed model-driven decision-making artifacts to support ITO, ASP, netsourcing and cloud sourcing decisions. The articles were identified by querying six academic publication indexing databases: EBSCOhost Business Source Complete, Science Direct, Scopus, Emerald Insight, AIS Electronic Library (AISeL) and IEEE Xplorer. We consider our choice of the six databases was reasonable and sufficient. AISeL is a dedicated repository for information systems research articles. IEEE Xplorer is one of the world’s largest collections of technical literature on engineering, computer science and related technologies with more than four million documents [96]. The other four databases are considered among the most prominent in academic institutions and are frequently used by other researchers. The following search terms were applied: ‘Outsourcing AND (Decision OR Select\* OR Framework)’, ‘Cloud AND (Decision OR Select\* OR Framework OR Adoption)’, ‘(“Application Service” OR ASP OR Net-sourcing) AND (Decision OR Select\* OR Framework)’.

The search was conducted in August 2016. Potentially relevant articles were shortlisted for further analysis based on the examination of the title and abstract of the article and keywords. Relevant articles were identified through the examination of the full-text of the shortlisted articles. In addition, a backward search [94] within the reference lists of the identified articles was performed to identify further relevant articles. Four inclusion criteria were applied for our systematic literature review search: (1) Subject area: IT outsourcing, IS outsourcing, cloud computing, cloud sourcing; (2) Content: model-based decision support artifact (method/software …); (3) Decision-making level: Organizational/ Managerial; and (4) Decision-making method: model-based/ quantitative. Our review is aimed at organizational decision making for ITO, thus does not cover decision making at application level and technical level, e.g. the optimum cloud configuration. Nine articles were identified as duplicates and were excluded. In each case, the most recent article was selected when multiple articles were found based on a single study. The final number of articles selected for analysis was 133.

We adapted the Information System Research Framework [35] (Figure 2) to develop our article coding frame (detailed in Appendix A) for content analysis of the surveyed articles. Although this framework is used to underpin Design Science Research (DSR), it is a high level generic framework that can be applied to IS research in general. We did not base our assessment on any specific DSR guidelines because firstly, there is lack of consensus among IS scholars on a single set of DSR guidelines [97] and some guidelines [e.g. 35, p.82] advise against “mandatory or rote” use of guidelines. Secondly, although a designed artifact is present in all of the assessed articles, the majority of the authors did not explicitly label their work as a DSR study, therefore use of a specific DSR lens to assess their work could be disputed. We limited our assessment of the identified literature (research articles) to the factors that allow an objective assessment and avoid possible bias and subjectivity. For the assessment of research rigor of each identified research article, we analyzed use of theoretical foundations (reference theories/frameworks and decision analysis methods), research methodologies and evaluation methods. To assess the extent of relevance considered in the 133 research articles, we analyzed the consideration of business needs (people, organization and technology requirements) in the articles. We applied Hevner et al.’s [35] taxonomy of evaluation methods and Venable et al.’s [98] evaluation quadrant to investigate the evaluation methods applied in the surveyed articles.

![](/api/attachments/VMG4VDBV/fulltext/images/705109201594825782fdd0f68c5cd86380ff8832ba9fe9373e4de598711eebcc.jpg)  
Figure 2. Information System Research Framework (Source: adapted from Hevner, March, Park and Ram [35])

Qualitative content analysis was performed to systematically describe the meaning of textual data from the selected articles by assigning successive parts of the material to the categories of the article coding frame (See Appendix A – Article Coding Frame) [99].The article coding frame was implemented in NVivo software, by defining each question as a node and each response option as a sub-node [100]. The content analysis involved reading the full-text of each article and coding the data by finding the relevant text within the article and assigning text fragments to response sub-nodes. Response options for Question 7 (theories and decision analysis methods applied in the surveyed articles) emerged from the document analysis. Question 6 and Question 8 in the article coding frame allowed the emergence of additional sub-nodes. Use of NVivo enabled reliable document analysis by recording the exact location of the text used to answer the questions in the coding frame [101]. The second round of document analysis was performed using NVivo’s search capability across multiple documents to ensure the consistency and accuracy of coding across the 133 identified research articles. Due to the emergent nature of response options for Question 7, searches were conducted for each emergent response (i.e. each theory or decision analysis method) across all articles to ensure the accuracy of analysis. The two rounds of content analysis guided by the article coding frame were performed by the first co-author. The other two co-authors coded a random sample of articles and the coding reliability was discussed and confirmed.

## 4. Literature Survey Findings

This section reports the results of the analysis of the surveyed articles. The section is structured according to the IS research framework (Figure 2). In total, we identified 133 articles (73 journal articles and 60 conference papers) that applied single or hybrid decision-making methods to IT outsourcing decisions. Publication dates of these articles ranged from 1995 to 2016.

## 4.1. Developed artifact

All of the 133 articles identified by the systematic literature review developed a kind of decision support method. In addition to the suggested method, 16 articles reported development of an instantiation in the form of a software tool, either as their final product or as a prototype [102-115]. Traditional ITO decisions were the focus of 57 percent of articles while the remaining articles focused on cloud sourcing, $\mathbf { A S P }$ or net-sourcing. As Figure 3 shows, the emergence of cloud computing in recent years has attracted the attention of researchers and has significantly contributed to the rise in the number of research publications on ITO decision support.

![](/api/attachments/VMG4VDBV/fulltext/images/2396365856ad9baa3084ab4b9934f2135a7c4ba56ff9dd016b224a1589ff3465.jpg)  
Figure 3. Frequency of ITO decision support model articles by type and year

In eight articles the designed artifacts were developed for specific sectors/industries: government agency [116]; banking/finance [50, 117]; health [118, 119]; tourism [120]; and higher education [121, 122]. Thirteen articles explicated the size of the targeted organization (outsourcer) as small or medium enterprise (SME) [112, 120, 123-129], or large [102, 124, 130, 131]. One quarter of all articles indicated that the suggested decision support artifact aids group decision making.

## 4.2.Theoretical foundations

The majority of surveyed articles include references to previous related works, although the extent of the literature review reported in each article varies significantly. We focused our assessment of theoretical foundations on the analysis of decision analysis methods and reference theories/ frameworks adopted by the authors of the surveyed articles as presented in this section.

## 4.2.1. Decision analysis methods

The decision analysis methods applied to ITO decision making in the surveyed literature are summarized in Table 2.

The most frequent MCDM method adopted in the surveyed literature was AHP which was used individually or in combination with other methods in 24 percent of articles. Fuzzy version of AHP (Fuzzy AHP) was used in nine percent of articles individually or in combination with other methods. Two thirds of the articles (70%) assumed IT outsourcing decisions as deterministic decision-making problems while the remainder used fuzzy decision-making theory. From a historical perspective, optimization using mixed-integer programing was the first decision analysis method to appear in the ITO literature [132]. Then the application of AHP to ITO decision support problems was reported by Akomode, Lees and Irgens [133] and remained a popular method for researchers, sometimes complemented by other decision analysis techniques. While this diversity expresses the creative endeavor of IT outsourcing decision support researchers, it also reveals that the convergence of research approaches has not happened to date.

Table 2. Summary of decision analysis methods identified in literature as being applied to ITO decisions

<table><tr><td colspan="3" rowspan="2"></td><td colspan="8">Application</td></tr><tr><td colspan="5">Traditional IT outsourcing</td><td colspan="3">Cloud sourcing, Net-sourcing, ASP</td></tr><tr><td colspan="2">Decision analysis approach/method</td><td>Count</td><td>ITO adoption</td><td>Deciding the level of ITO - sourcing model</td><td>What to outsource</td><td>Outsourcing location selection</td><td>IT Vendor/Supplier- selection, vendor portfolio management</td><td>Adoption</td><td>Cloud deployment model selection</td><td>Service provider selection, vendor portfolio management</td></tr><tr><td rowspan="12">MCDM</td><td>AHP</td><td>20</td><td>[134]; [135]; [136]; [137]; [138]; [115]</td><td>[136]; [50]; [139]</td><td>[140]; [139]</td><td>[141]</td><td>[133]; [123]</td><td>[109]; [114]; [122]; [142]</td><td></td><td>[143]; [144]; [145]; [146]</td></tr><tr><td>AHP + PROMETHEE</td><td>2</td><td></td><td></td><td>[147]; [148]</td><td>[148]</td><td></td><td></td><td></td><td></td></tr><tr><td>AHP + ELECTRE</td><td>1</td><td></td><td></td><td>[149]</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AHP + Optimization</td><td>8</td><td></td><td>[150]</td><td></td><td></td><td>[151]</td><td>[105]; [152]; [153]</td><td></td><td>[112]; [154]; [155]</td></tr><tr><td>ANP</td><td>5</td><td></td><td>[156]; [157]</td><td></td><td></td><td></td><td>[158]</td><td></td><td>[107]; [159]</td></tr><tr><td>ANP + Optimization</td><td>2</td><td></td><td>[160]</td><td>[160]</td><td></td><td>[161]</td><td></td><td></td><td></td></tr><tr><td>ELECTRE</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[162]; [108]</td></tr><tr><td>TOPSIS</td><td>2</td><td></td><td></td><td></td><td></td><td>[118]</td><td></td><td></td><td>[108]</td></tr><tr><td>Simple Additive Weighting</td><td>12</td><td>[102]; [104]; [163]; [164]; [165]; [166]</td><td></td><td></td><td></td><td>[52]; [167]</td><td>[128]; [127]</td><td>[125]</td><td>[113]</td></tr><tr><td>Extended Ordered Weighted Averaging + Optimization</td><td>1</td><td></td><td></td><td></td><td></td><td>[168]</td><td></td><td></td><td></td></tr><tr><td>PROMETHEE</td><td>2</td><td></td><td></td><td>[169]</td><td>[170]</td><td></td><td></td><td></td><td></td></tr><tr><td>PROMETHEE + ELECTRE</td><td>1</td><td></td><td></td><td>[171]</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="13">Fuzzy MCDM</td><td>Fuzzy AHP</td><td>8</td><td></td><td></td><td>[172]; [173]; [174]</td><td></td><td>[175]</td><td></td><td></td><td>[176]; [177]; [178]; [119]</td></tr><tr><td>Fuzzy DEA+AHP</td><td>1</td><td></td><td></td><td></td><td></td><td>[179]</td><td></td><td></td><td></td></tr><tr><td>Fuzzy AHP + Grey-TOPSIS</td><td>1</td><td></td><td></td><td></td><td></td><td>[180]</td><td></td><td></td><td></td></tr><tr><td>Fuzzy ANP</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[181]</td></tr><tr><td>Fuzzy ANP + Fuzzy AHP + Fuzzy TOPSIS</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[182]</td></tr><tr><td>Fuzzy AHP + Fuzzy TOPSIS</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[183]</td></tr><tr><td>Fuzzy TOPSIS</td><td>5</td><td></td><td></td><td>[172]</td><td></td><td>[184]; [185]; [179]</td><td></td><td></td><td>[177]</td></tr><tr><td>Fuzzy TOPSIS + Optimization</td><td>2</td><td></td><td></td><td></td><td></td><td>[186]; [187]</td><td></td><td></td><td></td></tr><tr><td>Fuzzy PROMETHEE</td><td>2</td><td></td><td></td><td></td><td></td><td>[188]; [189]</td><td></td><td></td><td></td></tr><tr><td>Fuzzy Simple Additive Weighting</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[190]</td></tr><tr><td>Fuzzy VIKOR</td><td>2</td><td></td><td></td><td></td><td></td><td>[191]; [192]</td><td></td><td></td><td></td></tr><tr><td>Fuzzy VIKOR + Fuzzy AHP</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[120]</td></tr><tr><td>Other Fuzzy methods</td><td>15</td><td>[193]; [194]; [195]; [196]; [197]</td><td></td><td>[198]; [199]</td><td></td><td>[200]; [51]; [201]</td><td>[202]</td><td></td><td>[203]; [204]; [205]; [206]</td></tr><tr><td rowspan="7">Optimization</td><td>Integer Programming</td><td>3</td><td>[207]</td><td></td><td></td><td></td><td>[132]; [208]</td><td></td><td></td><td></td></tr><tr><td>Fuzzy Linear Programming</td><td>1</td><td></td><td></td><td>[209]</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dynamic programming</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[130]; [154]</td></tr><tr><td>Genetic Algorithm (GA)</td><td>2</td><td>[210]</td><td></td><td></td><td>[211]</td><td></td><td></td><td></td><td></td></tr><tr><td>Zero-One Goal Programming</td><td>2</td><td></td><td></td><td></td><td></td><td>[161]</td><td>[212]</td><td></td><td></td></tr><tr><td>Multi-objective nonlinear integer programming</td><td>1</td><td></td><td></td><td></td><td></td><td>[213]</td><td></td><td></td><td></td></tr><tr><td>Other optimization methods</td><td>8</td><td>[166]</td><td></td><td></td><td>[126]</td><td>[214]</td><td>[215]; [216]; [217]</td><td></td><td>[218]; [219]</td></tr><tr><td rowspan="4">Other Methods</td><td>Real Options</td><td>3</td><td>[220]; [221]</td><td>[220]</td><td>[220]</td><td></td><td>[220]</td><td>[129]</td><td></td><td></td></tr><tr><td>System Dynamics</td><td>2</td><td>[222]</td><td>[222]; [116]</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Game theory</td><td>2</td><td>[223]</td><td></td><td></td><td></td><td></td><td>[224]</td><td></td><td></td></tr><tr><td>Logistic regressionCost Modelling using Net Present Value</td><td>18</td><td>[163]; [117]; [221]</td><td></td><td></td><td></td><td></td><td>[225][226]; [129]; [124]; [216]</td><td></td><td>[106]</td></tr><tr><td></td><td>Other mathematical methods</td><td>7</td><td>[227]; [228]; [229]; [230]</td><td></td><td></td><td></td><td></td><td>[124]</td><td></td><td>[103]; [231]; [111]</td></tr><tr><td colspan="3">Count of articles</td><td>28</td><td>10</td><td>15</td><td>5</td><td>27</td><td>20</td><td>1</td><td>32</td></tr></table>

Furthermore, Table 2 categorizes the articles by the major sourcing decision and reference type. The ITO adoption decision, which was the subject of 21 percent of articles, includes identification of the determinants of outsourcing (i.e. decision variables) and assessment of advantages and disadvantages of outsourcing versus in-sourcing (i.e. risk-benefit analysis/assessment) and answers the question whether to outsource or not?. Deciding on the level of ITO or sourcing model was studied in seven percent of articles. Almost 11 percent of articles covered the decision of what to outsource? This decision considers each of the IT infrastructure components (e.g. data center, communication network, etc.) and services (e.g. hardware maintenance, software development, etc.) as an alternative for the organization to outsource. Outsourcing location and IT vendor/supplier selection were the other decisions studied and were present in four and 20 percent of articles respectively. In the articles focused on cloud sourcing, net-sourcing or ASP, the most frequent topic was service provider selection (24% of articles) followed by cloud adoption (15% of articles) and cloud deployment model selection (one article).

## 4.2.2. Reference theories/frameworks

The majority of articles (70%) did not provide any specific theory or framework as the theoretical foundation of their study. As shown in Table 3, the most frequently cited types of ITO reference theories were Economic theories. Strategic theories and Social/ Organizational theories were cited in 16 and six percent of articles respectively.

Table 3. Analysis of theoretical foundation referenced in the surveyed articles

<table><tr><td>Category</td><td>Theory/Framework</td><td>Count</td><td>Reference</td></tr><tr><td rowspan="5">Economic Theories</td><td>Transaction Cost Theory</td><td>22</td><td>[112]; [145]; [154]; [135]; [192]; [229]; [214]; [104]; [175]; [185]; [173]; [150]; [157]; [140]; [208]; [207]; [208]; [219]; [225]; [197]; [210]; [141]</td></tr><tr><td>Production Cost Theory</td><td>2</td><td>[112]; [154]</td></tr><tr><td>Agency Theory</td><td>11</td><td>[112]; [145]; [154]; [135]; [157]; [207]; [219]; [197]; [229]; [225]; [227]</td></tr><tr><td>Property Rights Theory</td><td>1</td><td>[157]</td></tr><tr><td>Portfolio Theory</td><td>3</td><td>[214]; [219]; [112]</td></tr><tr><td rowspan="3">Strategic Theories</td><td>Resource Based Theory</td><td>12</td><td>[112]; [145]; [154]; [192]; [229]; [173]; [157]; [207]; [120]; [194]; [127]; [126]</td></tr><tr><td>Competitive Advantage Theory</td><td>14</td><td>[173]; [120]; [160]; [192]; [150]; [180]; [133]; [194]; [161]; [117]; [119]; [135]; [172]; [126]</td></tr><tr><td>Power Theory</td><td>1</td><td>[157]</td></tr><tr><td rowspan="3">Social/Organizational Theories</td><td>Institutional Theory</td><td>1</td><td>[154]</td></tr><tr><td>Relationship Theory</td><td>3</td><td>[112]; [145]; [154]</td></tr><tr><td>Socio-Technical TheoryRisk Theory</td><td>11</td><td>[106][111]</td></tr><tr><td rowspan="3"></td><td>Theory Of Risk Aversion</td><td>2</td><td>[228]; [214]</td></tr><tr><td>Social Exchange Theory</td><td>1</td><td>[219]</td></tr><tr><td>Learning Theory</td><td>1</td><td>[112]</td></tr><tr><td>Other theories</td><td>Knowledge Base Theory</td><td>2</td><td>[157]; [138]</td></tr><tr><td rowspan="5">Frameworks</td><td>Gap Evaluation Model</td><td>1</td><td>[206]</td></tr><tr><td>Cloud Trust Models</td><td>1</td><td>[111]</td></tr><tr><td>Cloud Adoption Framework</td><td>1</td><td>[127]</td></tr><tr><td>Technology, Organization, and Environment Framework</td><td>1</td><td>[120]</td></tr><tr><td>Balanced Scorecard (BSC)</td><td>2</td><td>[153]; [157]</td></tr></table>

## 4.3.Use of research paradigms/methodologies

Three articles [126, 154, 219] adopted the Design Science Research paradigm, although these did not fully follow the design science methodology. For instance, no design principles [232] were identified and implemented in these three articles. One article [133] reported use of Action Research in addition to quantitative modeling, but no detail about the implementation of the action research process is given in the article. Case Study research methodology was adopted in one study [122]. The other 96 percent of the articles can be classified under the axiomatic research paradigm [233] and used a quantitative modeling methodology. In axiomatic research, as opposed to empirical research, “a high degree of knowledge is assumed a priori about the goals and the socio-technical structure of the organization” [233, p.305]. In other words, this type of research is based on the underlying assumption that building objective models that can capture the organizational decision-making problems is possible. In axiomatic research the relationships between the variables are recognized as causal and quantitative. As a result, the models can be used to predict the future state of the modeled processes. Nevertheless, it is problematic to claim that the predictions are unambiguous and verifiable in the world outside the model [234]. As Bertrand and Fransoo [234] showed, the issue of poor verification and lack of empirical validation has hardly been addressed in the prior operations management research and caused a theory-practice gap in that domain.

## 4.4.Use of evaluation and validation methods

Evaluation of a DSS is defined as assessment of its overall value [235]. Evaluation includes validation, verification and substantiation [236, p.228]. Validation is the process of testing the agreement between behavior of the model/DSS and that of the real world system being modeled [237]. In other words, the purpose of validation is to ensure building “the right system” [235, p.83],

# ACCEPTED MANUSCRIPT

which is a system that performs with an acceptable level of accuracy. In model-based decision support systems, one should remember that we always solve a simplified model of the real world problem, thus achieving one hundred percent level of accuracy is not possible [236, 237]. Verification is defined as the “process of testing the extent to which a model has been faithful to its conception whether or not it and its conception are valid” [238, p.530]. In other words, verification concerns “building the system right” [235, p.83], which means the system has been implemented according to the specification. Substantiation is defined as “the demonstration that a computer model [DSS], within its domain of applicability, possesses a satisfactory range of accuracy consistent with the intended application of the model” [239, p.104]. An example of substantiation is producing a software application that incorporates the various elements of DSS and can be used/trialed by users.

We assessed the presence of evaluation in general and validation in particular, in the surveyed articles. We adapted previous definitions and a taxonomy of evaluation methods [35] and then analyzed the methods that were used in the surveyed articles to evaluate the design of the artifact Evaluation methods can also be used to evaluate the design process [98], but no such use was found in the surveyed articles. Due to a lack of consensus on terminologies, different authors used one term with different meanings. For instance, authors applied the term case study to illustrative examples, experiments and simulations. Thus we based our analysis on the Hevner, March, Park and Ram [35] definitions and concede that the evaluation approach may have been labeled differently in the respective articles.

The results of this analysis are provided in Table 4. In 89 percent of the articles we found at least one evaluation method. Simulation, the execution of the decision model with artificial data, was the most frequent evaluation method and was used in 48 percent of the articles. The second most frequent evaluation method (31%) was controlled experiment, execution of the decision model with real-world data. Scenarios and sensitivity analysis were used in 22 percent of the articles. The other less frequent evaluation methods used were case study (11%), informed argument (7 %), optimization (5%) and static analysis (1.5%). Whenever the artifact was evaluated using an empirical method such as questionnaire, interview or focus group with practitioners or through implementation in a case organization, we categorized the evaluation method as case study.

Table 4. Summary of analysis of evaluation methods used in ITO decision support literature

<table><tr><td>Evaluation category</td><td>Evaluation method</td><td>Definition</td><td>Count</td><td>Reference</td></tr><tr><td>Observational</td><td>Case study</td><td>Execute artifact with real-world data and study the artifact in business environment</td><td>15</td><td>[106]; [215]; [107];[122]; [145]; [50]; [118]; [196]; [102]; [179]; [165]; [117]; [210]; [139]; [141]</td></tr><tr><td rowspan="2">Analytical</td><td>Static Analysis</td><td>Examine structure of artifact for static qualities (e.g. complexity)</td><td>2</td><td>[143]; [151]</td></tr><tr><td>Optimization</td><td>Demonstrate optimality bounds on artifact behavior</td><td>7</td><td>[218]; [209]; [228]; [219]; [151]; [210]; [217]</td></tr><tr><td rowspan="2">Experimental</td><td>Controlled experiment</td><td>Controlled experiment: Execute artifact with real-world data</td><td>41</td><td>[109]; [202]; [206]; [143]; [240]; [125]; [181]; [112]; [127]; [113]; [162]; [138];[198]; [123]; [200]; [189]; [229];[195]; [172];[161]; [175]; [185]; [186];[227]; [134]; [194]; [169]; [173]; [163]; [180]; [187]; [188]; [157]; [179]; [164]; [201]; [197]; [166]; [225]; [174]; [120]</td></tr><tr><td>Simulation</td><td>Execute artifact with artificial data</td><td>64</td><td>[110]; [130]; [202]; [103]; [159]; [143]; [111]; [146]; [205]; [182]; [112];[226]; [144]; [241]; [114]; [153]; [203]; [183];[154];[242]; [209]; [133]; [116, 191];[228]; [192]; [214]; [136]; [211]; [171];[149]; [148]; [52]; [194]; [170]; [150]; [213]; [137]; [160]; [147]; [135]; [168]; [184]; [199]; [140]; [193]; [51]; [142]; [132]; [208]; [207]; [167]; [155]; [208]; [124]; [224]; [216]; [219]; [117]; [221]; [230]; [190]; [222]; [115]</td></tr><tr><td rowspan="2">Descriptive</td><td>Informed argument</td><td>Use information from the knowledge base (e.g., relevant research) to build a convincing argument for the artifact&#x27;s utility</td><td>9</td><td>[212]; [125]; [112]; [108]; [221]; [223]; [230]; [225]; [183]</td></tr><tr><td>Scenarios</td><td>Construct detailed scenarios around the artifact to demonstrate its utility</td><td>30</td><td>[130]; [202]; [103]; [111];[105];[181]; [182];[215]; [112];[226];[144];[153]; [154];[242]; [138];[116]; [191]; [229];[161]; [173]; [150]; [180] ; [137]; [157]; [147]; [168]; [132]; [216]; [219]; [222]</td></tr></table>

The DSR Evaluation Method Selection Framework [98] (Table 5) provides another perspective for the analysis of the evaluation methods. The framework provides classification of evaluation methods on two dimensions. The first dimension is the evaluation timing which is categorized as ex ante (prior to artifact construction) versus ex post evaluation (after artifact construction). The second dimension is the nature of the evaluation method that comprises naturalistic (e.g., field setting) versus artificial evaluation (e.g., laboratory setting). The evaluation methods reported were analyzed according to the four quadrants. The majority of the surveyed articles used artificial ex post evaluation methods. The use of naturalistic evaluation was limited to about 11 percent of the articles.

Table 5. DSR Evaluation Method Classification Framework (adapted from Venable, Pries-Heje and Baskerville [98])

<table><tr><td>Evaluation</td><td>Ex Ante</td><td>Ex Post</td></tr><tr><td>Naturalistic</td><td>Action Research [133]Focus group [196]</td><td>Action Research [133]Case study [106]; [215]; [107];[122]; [145]; [50]; [118]; [196]; [102]; [179]; [165]; [117]; [210]; [139]; [141]</td></tr><tr><td>Percentage of Articles: 11%</td><td>Percentage of Articles: 1.5%</td><td>Percentage of Articles: 11%</td></tr><tr><td>Artificial</td><td>Mathematical or logical proof [228]; [229]; [103]; [104]; [112]; [153];[154]; [143]; [212]; [125]; [108]; [221]</td><td>Experiment and scenario building, computer simulation (list of articles is provided in Table 4)</td></tr><tr><td>Percentage of Articles: 78%</td><td>Percentage of Articles: 9%</td><td>Percentage of Articles: 75%</td></tr></table>

Peffers, Tuunanen, Rothenberger and Chatterjee [37] considered simulation and experiment as demonstration and distinguished them from evaluation. While both artificial and naturalistic evaluation methods have their strengths and weaknesses, evaluation in a naturalistic setting is “the real proof of the pudding” [243, p.5]. Particularly for sociotechnical artifacts, the ITO DSS in our case, it seems naturalistic evaluation should be expected [98].

Only seven percent of articles [50, 103, 107, 110, 111, 125, 202, 206, 225] validated their suggested decision model by comparing the results of the proposed decision model with the decision made by experts, historical data, or the result of other available decision tools.

## 5. Discussion and recommendations

In this section we discuss the results of our analysis of model-driven ITO decision support recommendations for improvement.

RQ1: What decision analysis methods have been suggested in the literature to support organizational IT outsourcing decisions?

The review identified the potential of various decision analysis methods to support different decisions involved in the process of ITO and cloud sourcing. These methods included MCDM methods, optimization, system dynamics, real options and other mathematical models. The most frequent decision analysis method was AHP, which was applied individually in 20 articles, and in combination with other methods in 11 articles. Also, a further eight articles applied Fuzzy AHP, which combines AHP with Fuzzy set theory, and four articles applied a hybrid of Fuzzy AHP with other decision analysis methods. Thirty percent of the articles used Fuzzy set theory to enhance the capacity of the decision support model to deal with human subjectivity in rating decision factors. The most frequent IT outsourcing decisions supported in the surveyed literature were ITO vendor or cloud service provider selection (44%) followed by ITO/Cloud adoption (36%), what to outsource? (10%), deciding the level of outsourcing or sourcing model (8%), outsourcing location selection (4%) and cloud deployment model selection (one article).

RQ2: What level of rigor is evident in the model-driven artifacts developed to support organizational IT outsourcing decisions?

The second research question (RQ2) concerned the level of rigor applied by researchers in developing IT outsourcing decision-support artefacts. Only one-third of the identified articles cited one or more ITO reference theories. Although the majority of the surveyed articles reported an evaluation of their decision support artefact, in most cases the evaluation was a simulation or execution of the model in an artificial setting to demonstrate the feasibility of their suggested model but did not include its validation. Lack of validation of the decision support artefact in the vast majority (93%) of articles was the main weakness identified in our analysis of the ITO decision support literature. These findings are consistent with the prior assessment of DSS literature [e.g. 30, 31-33] in which limited use of validation and naturalistic evaluation methods was raised as a major shortcoming in DSS literature in terms of relevance to real practice. Validation of models in real-life trials is essential for decision support research [234]. Otherwise, the research lacks relevance and can be perceived by practitioners as addressing “fictitious problems” [233]. In the absence of rigorous verification and validation, a decision support model can produce optimum results, but those results are only valid for the hypothesized model, not for the real-world phenomenon being modelled. In such situations, the relevance of the decision model for making real-life decisions will be questionable.

Next, twelve recommendations are presented and numbered according to the four components of the Information System Research Framework [35], viz. environment, theoretical foundations, methodologies, and justify/evaluate. Table 6 provides a summary of recommendations for improvement of ITO DSS research.

Table 6. Recommendations for improvements to ITO DSS research

<table><tr><td>Rec #</td><td>Environment (Organization, Technology, People)</td><td>Underpinning source</td></tr><tr><td>R1.1</td><td>Artifact should be capable of group decision support and capable of supporting C-level managers</td><td rowspan="2">Empirical ITO literature (see section 2.2)</td></tr><tr><td>R1.2</td><td>Organizational context and characteristics should be considered in the artifact design and</td></tr><tr><td colspan="3">development process and should be explicitly presented</td></tr><tr><td colspan="3">Theoretical Foundations</td></tr><tr><td>R2.1</td><td>DSS artifacts should be grounded in organizational decision-making research</td><td>DSS literature [31]</td></tr><tr><td>R2.2</td><td>Decision variables incorporated in the designed artifact (ITO DSS) should be derived from ITO descriptive literature and grounded in ITO reference theories</td><td rowspan="2">IS research framework [35]</td></tr><tr><td>R2.3</td><td>ITO decision support frameworks, instruments, models, constructs, methods and instantiations available in the literature should be reviewed and critically assessed</td></tr><tr><td colspan="3">Methodologies</td></tr><tr><td>R3.1</td><td>Practice-oriented research methodologies that consider both rigor and relevance such as design science research, action research and case study should be used for development of ITO DSS</td><td>Rigor and Relevance requirement [35]</td></tr><tr><td colspan="3">Justify/Evaluate</td></tr><tr><td>R4.1</td><td>ITO decision support artifact should be validated</td><td rowspan="4">DSS literature (see section 4.7) &amp; IS research framework [35]</td></tr><tr><td>R4.2</td><td>ITO decision support artifact should be verified</td></tr><tr><td>R4.3</td><td>Requirements for implementation of the artifact including usability, readiness for use should be addressed</td></tr><tr><td>R4.4</td><td>Assumptions and limitations of the artifact, its appropriate use, and the logic of decision model should be presented</td></tr><tr><td>R4.5</td><td>Naturalistic (field setting) evaluation should be used</td><td>Relevance requirement [37, 98, 243]</td></tr><tr><td>R4.6</td><td>Appropriateness of the decision analysis method(s) selected for DSS should be justified</td><td>Rigor requirement according to IS research framework [35]</td></tr></table>

## 5.1.Environment (people, organization and technology requirements)

According to the empirical ITO literature (summarized in section 2.2) ITO decisions are normally group based and made by C-level managers, both technical and non-technical due to the sociotechnical nature of the decisions. Thus the ITO DSS artifact (e.g. method or software) should be capable of group decision support, and consider the needs and requirement of both technical and nontechnical C-level managers (R1.1). Our analysis of the 133 ITO DSS articles showed only about 25 percent of articles explicitly considered group decision making as a requirement and not one article discussed the type or organizational level of the ITO decision makers.

The ITO literature suggests that ITO decisions are contextual i.e. favorable ITO decisions depend structure), therefore organizational context and characteristics should be considered in the artifact design and development process and explicitly presented (R1.2). As shown in section 4.2, articles that explicate the contingencies of their proposed decision support artifact were in the minority.

## 5.2.Theoretical foundations

Because the mission of DSS is to improve managerial decision-making, the DSS artifacts should be grounded in organizational decision-making research [31] (R2.1). Reference to, and discussion about organizational decision-making theories was barely found in the majority of the articles we analyzed. As discussed in section 2, an extensive body of descriptive ITO literature has been

# ACCEPTED MANUSCRIPT

accumulated over three decades of research. This literature includes many reference theories and empirical findings (e.g. decision variables, benefits and risks of ITO) that form a knowledge base for ITO. This extensive knowledge base of descriptive literature on ITO should be used so that the designed ITO DSS artefact will be more rigorous and underpinned by scientific research (R2.2). Although all the articles we analyzed cited prior ITO literature, the depth and breadth of ITO literature cited was very limited in some of the articles. In other words, much of the normative (i.e.

ITO decision support frameworks, instruments, models, methods and instantiations available in the literature should be reviewed and critically assessed to base the design effort on the accumulated scholarship of research and avoid reinvention of the wheel (R2.3). As is evident from the results of our analysis, repeated use of decision analysis methods (e.g. AHP) for the same decisions (e.g. service provider selection) in the normative ITO literature shows the limited attempt of some researchers to review prior research and avoid duplication of research on decision analysis methods in ITO DSS context that are already well understood.

## 5.3.Research methodologies

As our findings showed, the majority of decision support artifacts available in the literature used a quantitative modeling methodology. While quantitative modeling is well-established to overcome the complexity of real-world problems, relying solely on such methodologies can lead to models that could be considered “fictitious problems” in the real world [233, p.320]. Thus, practice-oriented research methodologies such as design science research, case study and action research that consider both rigor and relevance should be adopted (R3.1). Evidence from the assessment of DSS literature has confirmed the higher chance of relevance for studies that used case study or design science research methodologies [31].

## 5.4.Justify/Evaluate/Validate

There is consensus in the literature on the need to validate the decision support artifacts (R4.1) [236]. Without validating the designed artifact, real world decision makers cannot rely on the results generated by the artifact (DSS). As revealed by our analysis, only a very small proportion (7%) of articles validated the proposed decision support artifact. In addition, as part of evaluation, verification of the artifact (DSS) should be performed (R4.2) by careful examination of the artifact’s conception and by testing the extent to which the artifact has been faithful to its conception. To justify the feasibility of implementation and to facilitate adoption of the artifact by organizational practitioners, the designed artifact should be instantiated and the requirements for implementation of the artifact including usability, and readiness for use should be addressed (R4.3). The assumptions and limitations of the artifact, its appropriate use, and the logic of the decision model should also be presented (R4.4). Without considering the implementation requirement, the practical relevance of the artifact could be questionable, even if the artifact satisfies the rigor criteria. Since the artifact is designed to be used in the practice world of organizations, its effectiveness needs to be evaluated using naturalistic evaluation methods (R4.5). In addition, the appropriateness of the decision analysis method(s) selected for DSS should be justified (R4.6), because each decision analysis method is suitable for a specific type of problem and is based on specific assumptions.

## 6. Conclusion, contributions, limitations and future research

This paper provided a critical assessment of model-driven decision support for IT outsourcing in academic research through a systematic literature review and document analysis of a total of 133 peer-reviewed articles published between 1995 and 2016.

Our review identified the potential of various decision analysis methods to support different decisions required in the process of ITO and cloud sourcing. These methods included MCDM methods, optimization, system dynamics, real options and other mathematical models. The most frequent IT outsourcing decisions supported in the surveyed literature related to ITO vendor or cloud service provider selection followed by ITO/Cloud adoption. Other ITO decisions viz. what to outsource?, deciding on the level of outsourcing or sourcing model, where to outsource (onshore or offshore)? and cloud deployment model selection were targeted in a small number of the articles.

Lack of validation and naturalistic evaluation of the decision support artifact was the main weakness identified in the vast majority of articles in our analysis of the ITO decision support literature. This problem provides further impetus for academic research that is grounded in methodological approaches such as design science which explicitly includes evaluation in practice as part of the research process.

In sum, ITO DSS literature suggested various decision-support artefacts to help practitioners with their ITO decision-making, but in the majority of the published articles, no justification for the utility of the artefact [244] was provided. In other words, one or a hybrid of decision analysis methods were applied to one or more ITO decisions without proving that the suggested approach would provide any ld application of much of the existing academic research in this domain could be questioned. The limited level of rigor applied to ITO decision support research, and the fact that some of this research is published in high ranked journals, provides an instance that supports Gill’s (2010) assertion that the rigor of Business/IS research findings is vastly overestimated.

## 6.1.Limitations

Although we selected the main research databases related to the topic, we cannot guarantee that all model-driven DSS articles were selected for review. Also, in applying the systematic literature method we did not perform forward searches [94] due to temporal and resource constraints.

## 6.2.Future research

We hope this research may encourage and motivate scholars to join us in continuous improvement of the ITO decision support field. Since various MCDM methods have different characteristics and may lead to inconsistent results, future research is required to determine the most suitable MCDM method for each type of IT outsourcing decision. Future research should establish criteria to support ITO decision makers to select one or a hybrid of MCDM methods that are most appropriate to improve the quality of IT outsourcing decisions. Also, investigation of the adoption of the proposed MCDM approaches in practice is another promising future research topic that appears to be missing in the literature to date. Such studies can establish the feedback loop required for improvement of research relevance in the ITO DSS field. Contributions

# ACCEPTED MANUSCRIPT

Our main contributions in this paper are threefold. First, we systematically surveyed the ITO decision support literature and created a novel categorization of IT outsourcing decisions and the decision analysis approaches suggested to support them as presented in Table 2. Second, our analysi of the rigor of the surveyed literature on normative ITO DSS identified improvement opportunities, particularly with regard to the use of foundation theories (e.g. descriptive ITO literature) and evaluation methods. Third, based on the systematic review of the ITO decision support literature we suggested recommendations and future directions for ITO decision support research. The result of our analysis is a comprehensive account as well as a critical review of extant model-based decision support for IT outsourcing. This paper can help ITO practitioners who seek scientific approaches for evidence-based decision making to grasp the current state of the art of ITO research. It also warns ITO practitioners about the risks involved in using the non-validated decision support models in real world settings. For ITO researchers, the summarized and critically assessed ITO DSS research that spans more than two decades can be a timesaver. This paper also informs ITO researchers about the any further improvements). We believe the implementation of the recommendations presented here has the potential to greatly enhance the rigor and relevance of ITO DSS research and provide support for managers facing critical decisions in this increasingly complex and dynamic environment.

## Funding sources

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## References

[1] Gartner, Gartner says worldwide IT outsourcing market to reach \$288 billion in 2013, 2013.

[2] J. Barthélemy, The hidden costs of IT outsourcing, MIT Sloan Management Review, 42 (2001) 60- 69.

[3] S. Cabral, B. Quelin, W. Maia, Outsourcing failure and reintegration: the influence of contractual and external factors, Long Range Planning, 47 (2014) 365-378.

[4] G. Erber, A. Sayed-Ahmed, Offshore Outsourcing, Intereconomics, 40 (2005) 100-112.

[5] S. Overby, Company Saves Millions By Ending IT Outsourcing Deal, 2010

[6] S. Overby, Outsourcing--and Backsourcing--at JPMorgan Chase, 2005.

[7] H.A. Smith, J.D. McKeen, Developments in practice XIV: IT sourcing - how far can you go?, Communications of the Association for Information Systems, 13 (2004) 508-520

[8] M.C. Lacity, L.P. Willcocks, J.W. Rottman, Global outsourcing of back office services: Lessons, trends, and enduring challenges, Strategic Outsourcing: An International Journal, 1 (2008) 13-34.

[9] R. McIvor, What is the right outsourcing strategy for your process?, European Management Journal, 26 (2008) 24-34.

[10] P. Westphal, A. Sohal, Outsourcing decision-making: does the process matter?, Production Planning & Control, 27 (2016) 1-15.

[11] P.C. Palvia, A dialectic view of information systems outsourcing: Pros and cons, Information & Management, 29 (1995) 265-275.

[12] L.A. De Looff, Information systems outsourcing decision making: A framework, organizational theories and case studies, Journal of Information Technology, 10 (1995) 281-297.

[13] P. Westphal, A. Sohal, Taxonomy of outsourcing decision models, Production Planning and Control, 24 (2013) 347-358.

[14] R. McIvor, A practical framework for understanding the outsourcing process, Supply Chain Management: An International Journal, 5 (2000) 22-36.

[15] A. Brannemo, How does the industry work with sourcing decisions? Case study at two Swedish companies, Journal of Manufacturing Technology Management, 17 (2006) 547-560.

[16] M.C. Lacity, S. Khan, A. Yan, L.P. Willcocks, A review of the IT outsourcing empirical literature and future research directions, Journal of Information Technology, 25 (2010) 395-433.

[17] T. Kramer, L. Klimpke, A. Heinzl, Outsourcing decisions of small and medium-sized enterprises: A multiple-case study approach in the German software industry, 46th Hawaii International Conference on System Sciences, IEEE, Hawaii 2013, pp. 4236-4245.

[18] K.S. Boell, D. Cecez-Kecmanovic, Debating systematic literature reviews (SLR) and their ramifications for IS: a rejoinder to Mike Chiasson, Briony Oates, Ulrike Schultze, and Richard Watson, Journal of Information Technology, 30 (2015) 188-193.

[19] G. Paré, M.-C. Trudel, M. Jaana, S. Kitsiou, Synthesizing information systems knowledge: A typology of literature reviews, Information & Management, 52 (2015) 183-199.

[20] J. Dibbern, T. Goles, R. Hirschheim, B. Jayatilaka, Information systems outsourcing: A survey and analysis of the literature, SIGMIS Database, 35 (2004) 6-102.

[21] R. Gonzalez, J. Gasco, J. Llopis, Information systems outsourcing: A literature analysis, Information & Management, 43 (2006) 821-834.

[22] M.C. Lacity, S.A. Khan, L.P. Willcocks, A review of the IT outsourcing literature: Insights for practice, The Journal of Strategic Information Systems, 18 (2009) 130-146.

[23] J. Blaskovich, N. Mintchik, Information technology outsourcing: A taxonomy of prior studies and directions for future research, Journal of Information Systems, 25 (2011) 1-36.

[24] D.J. Power, R. Sharda, F. Burstein, Decision Support Systems, in: D. Straub, R. Welke (Eds.) Wiley Encyclopedia of Management, John Wiley & Sons2015, pp. 1-4.

[25] D.J. Power, R. Sharda, Model-driven decision support systems: Concepts and research directions, Decision Support Systems, 43 (2007) 1044-1061.

[26] R. Santhanam, T. Guimaraes, Assessing the quality of institutional DSS, European Journal of Information Systems, 4 (1995) 159-170.

[27] Y. Sun, P.B. Kantor, Cross-Evaluation: A new model for information system evaluation, Journal of the American Society for Information Science and Technology, 57 (2006) 614-628.

[28] P.G.W. Keen, Value analysis: Justifying decision support systems, MIS Quarterly, 5 (1981) 1-15.

[29] G. Phillips-Wren, M. Mora, G.A. Forgionne, J.N.D. Gupta, An integrative evaluation framework

for intelligent decision support systems, European Journal of Operational Research, 195 (2009) 642-652.

[30] D. Arnott, G. Pervan, A critical analysis of decision support systems research, Journal of Information Technology, 20 (2005) 67-87.

[31] D. Arnott, G. Pervan, Eight key issues for the decision support systems discipline, Decision Support Systems, 44 (2008) 657-672.

[32] D. Arnott, G. Pervan, An assessment of DSS design science using the Hevner, March, Park and Ram guidelines, in: S.D. Gregor, D.N. Hart (Eds.) Information Systems Foundations (‘The role of design science’) Workshop, ANU E Press, Canberra, Australia, 2008.

[33] S. Purao, V.C. Storey, Evaluating the adoption potential of design science efforts: The case of APSARA, Decision Support Systems, 44 (2008) 369-381.

[34] S.J. Miah, J. Debuse, D. Kerr, A development-oriented DSS evaluation approach: A case demonstration for conceptual assessment, Australasian Journal of Information Systems, 17 (2012) 43-55.

[35] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Quarterly, 28 (2004) 75-105.

[36] D. Mackrell, D. Kerr, L. von Hellens, A qualitative case study of the adoption and use of an agricultural decision support system in the Australian cotton industry: The socio-technical view, Decision Support Systems, 47 (2009) 143-153.

[37] K. Peffers, T. Tuunanen, M.A. Rothenberger, S. Chatterjee, A Design Science Research Methodology for Information Systems Research, Journal of Management Information Systems, 24 (2007) 45-77.

[38] P.L. Willcocks, T. Kern, IT outsourcing as strategic partnering: the case of the UK Inland Revenue, European Journal of Information Systems, 7 (1998) 29-45.

[39] V. Grover, M.J. Cheon, J.T.C. Teng, A descriptive study on the outsourcing of information systems functions, Information & Management, 27 (1994) 33-44.

[40] T. Kern, M.C. Lacity, L. Willcocks, Netsourcing: Renting business applications and services over a network, Financial Times Prentice Hall, NJ, 2002

[41] C. Loebbecke, C. Huyskens, What drives netsourcing decisions? An empirical analysis, European Journal of Information Systems, 15 (2006) 415-423.

[42] E. Carmel, P. Tjia, Offshoring information technology: Sourcing and outsourcing to a global workforce, Cambridge University Press, Cambridge, UK, 2005.

[43] O.M. Yigitbasioglu, K. Mackenzie, R. Low, Cloud computing: How does it differ from IT outsourcing and what are the implications for practice and research?, International Journal of Digital Accounting Research, 13 (2013) 99-121.

[44] M.C. Lacity, P. Reynolds, Cloud services practices for small and medium-sized enterprises, MIS Quarterly Executive, 13 (2014) 31-44.

[45] A. Khajeh-Hosseini, I. Sommerville, J. Bogaerts, P. Teregowda, Decision support tools for cloud migration in the enterprise, IEEE International Conference on Cloud Computing Washington, USA, 2011, pp. 541-548.

[46] M.C. Lacity, R. Hirschheim, The information systems outsourcing bandwagon, Sloan Management Review, 35 (1993) 75-86.

[47] H. Liang, J.-J. Wang, Y. Xue, X. Cui, IT outsourcing research from 1992 to 2013: A literature review based on main path analysis, Information & Management, 53 (2016) 227-251.

[48] U.M. Apte, M.G. Sobol, S. Hanaoka, T. Shimada, T. Saarinen, T. Salmela, A.P. Vepsalainen, IS outsourcing practices in the USA, Japan and Finland: A comparative study, Journal of information technology, 12 (1997) 289-304.

[49] S. Ang, L.L. Cummings, Strategic response to institutional influences on information systems outsourcing, Organization Science, 8 (1997) 235-256.

[50] U. Gulla, M. Gupta, Deciding the level of information systems outsourcing: Proposing a framework and validation with three Indian banks, Journal of Enterprise Information Management, 25 (2011) 28-59.

[51] Q. Zhang, L. Jiang, Y. Huang, An interval intuitionistic fuzzy decision approach for supplier selection in information technology service outsourcing, Journal of Information and Computational Science, 9 (2012) 4329-4336.

[52] W. Liu, Q. Li, A multi-criteria decision making method based on linguistic preference information for IT outsourcing vendor selection in hospitals, International Conference on Information, Business and Education Technology, Beijing, China 2013.

[53] M. Hancox, R. Hackney, IT outsourcing: Frameworks for conceptualizing practice and perception, Information Systems Journal, 10 (2000) 217-237.

[54] A. Tiwana, A.A. Bush, A comparison of transaction cost, agency, and knowledge-based theory predictors of IT outsourcing decisions: A US-Japan cross-cultural field study, Journal of Managemen Information Systems, 24 (2007) 259-300.

[55] M.C. Lacity, L.P. Willcocks, Interpreting information technology sourcing decisions from a transaction cost perspective: Findings and critique, Accounting, Management and Information Technologies, 5 (1995) 203-244.

[56] A. Jain, R.A. Thietart, Knowledge based transactions and decision framing in information technology outsourcing, Journal of Strategic Information Systems, 22 (2013) 315-327.

[57] J. Vetter, A. Benlian, T. Hess, Setting targets right! How non-rational biases affect the risk preference of IT-outsourcing decision makers-an empirical investigation, European Conference on Information Systems (ECIS), Helsinki, Finland, 2011.

[58] R. Elitzur, A. Wensley, Game theory as a tool for understanding information services outsourcing, Journal of Information Technology, 12 (1997) 45-60

[59] J. Goo, R. Kishore, K. Nam, H.R. Rao, Y. Song, An investigation of factors that influence the duration of IT outsourcing relationships, Decision Support Systems, 42 (2007) 2107-2125.

[60] L. Loh, N. Venkatraman, Diffusion of information technology outsourcing: Influence sources and the Kodak effect, Information Systems Research, 3 (1992) 334-358.

[61] T. Kern, L.P. Willcocks, The relationship advantage: Information technologies, sourcing, and management, Oxford University Press, London, 2001.

[62] B. Watjatrakul, Determinants of IS sourcing decisions: A comparative study of transaction cost theory versus the resource-based view, Journal of Strategic Information Systems, 14 (2005) 389-415.

[63] B.A. Aubert, G. Beaurivage, A.-M. Croteau, S. Rivard, Firm strategic profile and IT outsourcing, Information Systems Frontiers, 10 (2008) 129-143.

[64] T.F. Stafford, Active priming of cultural stereotypes in outsourcing decision making, Journal of Global Information Technology Management, 14 (2011) 27-47.

[65] J. Goo, C.D. Huang, Facilitating relational governance through service level agreements in IT outsourcing: An application of the commitment–trust theory, Decision Support Systems, 46 (2008) 216- 232.

[66] M.C. Lacity, L.P. Willcocks, D.F. Feeny, The value of selective IT sourcing, MIT Sloan Management Review, 37 (1996) 13.

[67] C.-C. Hsieh, C.-C. Huang, A dynamic model of decision-making in the IS/IT outsourcing process: a case study from a government-supported project, International Conference on Information Resources Management (Conf-IRM), Ontario, Canada, 2008.

[68] A. Langley, H. Mintzberg, P. Pitcher, E. Posada, J. Saint-Macary, Opening up decision making: The view from the black stool, Organization Science, 6 (1995) 260-279.

[69] E.K. Zavadskas, Z. Turskis, Multiple criteria decision making (MCDM) methods in economics: an overview, Technological and Economic Development of Economy, 17 (2011) 397-427.

[70] G.S. Parnell, T. Bresnick, S.N. Tani, E.R. Johnson, Handbook of decision analysis, John Wiley & Sons, Hoboken, NJ, 2013.

[71] R.A. Howard, Decision analysis: Applied decision theory, in: D.B. Herty, J. Melese (Eds.) Fourth International Conference on Operations Research Wiley -Interscience, NY, 1966, pp. 55-71.

[72] R.A. Howard, The foundations of decision analysis, IEEE Transactions on Systems Science and Cybernetics, 4 (1968) 211-219.

[73] R.T. Clemen, T. Reilly, Making hard decisions with Decision Tools, 2 ed., Duxbury/Thomson Learning, Pacific Grove, CA, 2001.

[74] H.A. Simon, A behavioral model of rational choice, The Quarterly Journal of Economics, 69 (1955) 99-118.

[75] H.A. Simon, The new science of management decisions, Englewood Cliffs, NJ: Prentice-Hall, 1977.

[76] G.-H. Tzeng, J.-J. Huang, Multiple attribute decision making: methods and applications, CRC press, Boca Raton, FL, 2011.

[77] C.L. Hwang, K. Yoon, Multiple attribute decision making: methods and applications, Springer-Verlag, NY, 1981.

[78] T.L. Saaty, A scaling method for priorities in hierarchical structures, Journal of Mathematical Psychology, 15 (1977) 234-281.

[79] T.L. Saaty, The Analytic Hierarchy Process, McGraw Hill, NY, 1980.

[80] T.L. Saaty, Decision making with the analytic hierarchy process, International Journal of Services Sciences, 1 (2008) 83-98.

[81] T.L. Saaty, Decision making for Leaders, RWS Publications, Pittsburgh, PA, 1996.

[82] T.L. Saaty, Analytic network process, Encyclopedia of Operations Research and Management Science, Springer, Boston, MA, 2001, pp. 28-35.

[83] B. Roy, Classement et choix en présence de points de vue multiples (la méthode ELECTRE), La Revue d'Informatique et de Recherche Opérationelle (RIRO), 8 (1968) 57-75.

[84] J.-P. Brans, P. Vincke, B. Mareschal, How to select and how to rank projects: The PROMETHEE method, European journal of operational research, 24 (1986) 228-238.

[85] K. Yoon, A reconciliation among discrete compromise solutions, Journal of Operational Research Society, 38 (1987) 277-286.

[86] S. Opricovic, Multicriteria optimization of civil engineering systems, Faculty of Civil Engineering, Belgrade, 2 (1998) 5-21.

[87] S. Opricovic, G.H. Tzeng, Compromise solution by MCDM methods: A comparative analysis of VIKOR and TOPSIS, European Journal of Operational Research, 156 (2004) 445-455.

[88] P.C. Fishburn, Additive utilities with incomplete product sets: application to priorities and assignments, Operations Research, 15 (1967) 537-542.

[89] A. Charnes, W.W. Cooper, R.O. Ferguson, Optimal estimation of executive compensation by linear programming, Management Science, 1 (1955) 138-151.

[90] A. Charnes, W.W. Cooper, Management models and industrial applications of linear programming, Management Science, 4 (1957) 38-91.

[91] V. Srinivasan, A.D. Shocker, Linear programming techniques for multidimensional analysis of preferences, Psychometrika, 38 (1973) 337-369.

[92] L.A. Zadeh, Fuzzy sets, Information and Control, 8 (1965) 338-353.

[93] L.A. Zadeh, The concept of a linguistic variable and its application to approximate reasoning, Information Sciences, 8 (1975) 199-249.

[94] J. vom Brocke, A. Simons, K. Riemer, B. Niehaves, R. Plattfaut, A. Cleven, Standing on the shoulders of giants: Challenges and recommendations of literature search in information systems research, Communications of the Association for Information Systems, 37 (2015) 205-224.

[95] C. Okoli, A Guide to conducting a standalone systematic lterature review, Communications of the Association for Information Systems, 37 (2015) 879-910.

[96] IEEE, IEEE Xplore® Digital library reaches four million documents as pace of technical contributions accelerates, 2016.

[97] J.R. Venable, Design science research post Hevner et al.: Criteria, standards, guidelines, and expectations, in: R. Winter, J.L. Zhao, S. Aier (Eds.) Global Perspectives on Design Science Research: 5th International Conference, DESRIST 2010, Springer Berlin Heidelberg, St. Gallen, Switzerland, 2010, pp. 109-123.

[98] J.R. Venable, J. Pries-Heje, R. Baskerville, A comprehensive framework for evaluation in design science research, in: K. Peffers, M. Rothenberger, B. Kuechler (Eds.) Design Science Research in Information Systems. Advances in Theory and Practice, Springer, Berlin, Germany, 2012, pp. 423-438.

[99] M. Schreier, Qualitative content analysis, The SAGE handbook of qualitative data analysis, DOI (2014) 170-183.

[100] P. Bazeley, K. Jackson, Qualitative data analysis with NVivo, Sage Publications Limited, London, UK, 2013.

[101] K. Boréus, G. Bergström, Analyzing Text and Discourse: Eight Approaches for the Social Sciences, SAGE2017.

[102] C. Andresen, G. Hodosi, I. Saprykina, L. Rusu, User acceptance of a software tool for decision making in IT outsourcing: A qualitative study in large companies from Sweden, 3rd World Summit on the Knowledge Society (WSKS 2010), Greece, 2010, pp. 277-288.

[103] S. Ding, C.-Y. Xia, K.-L. Zhou, S.-L. Yang, J.S. Shang, Decision support for personalized cloud service selection through multi-attribute trustworthiness evaluation, PLoS ONE, 9 (2014) 1-11

[104] G. Hodosi, L. Rusu, A software tool that supports decisions for companies to outsource information technology or not, Mediterranean Conference on Information Systems (MCIS), Venice, Italy, 2007, pp. 22.

[105] A. Juan-Verdejo, H. Baars, Decision support for partially moving applications to the cloud - The example of business intelligence, 2013 International Workshop on Hot Topics in Cloud Services, Prague, Czech Republic, 2013, pp. 35-42.

[106] A. Khajeh-Hosseini, D. Greenwood, J.W. Smith, I. Sommerville, The cloud adoption toolkit: supporting cloud adoption decisions in the enterprise, Software: Practice & Experience, 42 (2012) 447- 465.

[107] M. Menzel, M. Schönherr, S. Tai, (MC2)2: criteria, requirements and a software prototype for cloud infrastructure decisions, Software: Practice and Experience, 43 (2013) 1283-1297.

[108] Z. Rehman, O.K. Hussain, F.K. Hussain, User-side cloud service management: State-of-the-art and future directions, Journal of Network and Computer Applications, 55 (2015) 108-122.

[109] V. Andrikopoulos, Z. Song, F. Leymann, Supporting the migration of applications to the cloud through a decision support system, Sixth International Conference on Cloud Computing, Santa Clara, CA, USA, 2013, pp. 565-572.

[110] E. Cayirci, A. Garaga, A. Santana de Oliveira, Y. Roudier, A cloud adoption risk assessment model, IEEE/ACM 7th International Conference on Utility and Cloud Computing (UCC), London, United Kingdom, 2014, pp. 908-913.

[111] N. Ghosh, S.K. Ghosh, S.K. Das, SelCSP: a framework to facilitate selection of cloud service providers, IEEE Transactions on Cloud Computing, 3 (2015) 66-79.

[112] B. Martens, F. Teuteberg, Decision-making in cloud computing environments: A cost and risk based approach, Information Systems Frontiers, 14 (2012) 871-893.

[113] M.K. Naseer, S. Jabbar, I. Zafar, A novel trust model for selection of cloud service provider, World Symposium on Computer Applications & Research (WSCAR 2014), Sousse, Tunisia, 2014, pp. 1- 6.

[114] S.V. Razumnikov, M.S. Kremneva, Decision support system of transition IT-applications in the cloud enviroment, 2015 International Siberian Conference on Control and Communications (SIBCON), Omsk, Russia, 2015, pp. 1-4.

[115] J.-R. Chen, T.-C. Chou, Y.-C. Lin, Design and implementation of an ontology-based information technology outsourcing evaluation system using AHP, International Journal of Innovation and Learning, 4 (2007) 74-91.

[116] T.R. Bezerra, A. Moura, A.S. Lima, A system dynamics model to support strategic decision making on IT outsourcing: A case study at a state revenue agency in Brazil, Network Operations and Management Symposium (NOMS), IEEE, Krakow, Poland, 2014, pp. 1-4.

[117] S. Paisittanand, D.L. Olson, A simulation study of IT outsourcing in the credit card business, European Journal of Operational Research, 175 (2006) 1248-1261.

[118] P.-F. Hsu, M.-G. Hsu, Optimizing the information outsourcing practices of primary care medical organizations using entropy and TOPSIS, Qual Quant, 42 (2008) 181-201.

[119] C. Low, Y. Hsueh Chen, Criteria for the evaluation of a cloud-based hospital information system outsourcing provider, Journal of Medical Systems, 36 (2012) 3543-3553.

[120] S.-W. Lin, The critical success factors for a travel application service provider evaluation and selection by travel intermediaries, Tourism Management, 56 (2016) 126-141.

[121] F. Mohd Nishat, R. Syed Asif, IT outsourcing intent in academic institutions in GCC countries: An empirical investigation and multi-criteria decision model for vendor selection, Journal of Enterprise Information Management, 29 (2016) 432-453.

[122] N. Ramachandran, P. Sivaprakasam, G. Thangamani, G. Anand, Selecting a suitable cloud computing technology deployment model for an academic institute, Campus-Wide Information Systems, 31 (2014) 319-345.

[123] S.-I. Chang, D.C. Yen, C.S.-P. Ng, W.-T. Chang, An analysis of IT/IS outsourcing provider selection for small- and medium-sized enterprises in Taiwan, Information & Management, 49 (2012) 199-209.

[124] E. Walker, W. Brisken, J. Romney, To lease or not to lease from storage clouds, Computer, 43 (2010) 44-50.

[125] J. Keung, F. Kwok, Cloud deployment model selection assessment for SMEs: renting or buying a cloud, IEEE Fifth International Conference onUtility and Cloud Computing (UCC), Chicago, Illinois, USA, 2012, pp. 21-28.

[126] T. Kramer, M. Eschweiler, Outsourcing location selection with SODA: A requirements based decision support methodology and tool, 25th international conference on Advanced Information Systems Engineering Springer-Verlag Berlin, Valencia, Spain, 2013, pp. 530-545.

[127] C.P. Muir, A decision making model for the adoption of cloud computing in Jamaican organizations, Americas Conference on Information Systems (AMCIS), Chicago, Illinois, USA, 2013, pp. 55-64.

[128] P. Saripalli, G. Pingali, MADMAC: multiple attribute decision methodology for adoption of clouds, IEEE International Conference on Cloud Computing, Melbourne, Australia, 2011, pp. 316-323.

[129] C.-Y. Yam, A. Baldwin, S. Shiu, C. Ioannidis, Migration to cloud as real option: Investment decision under uncertainty, IEEE International Conference on Trust, Security and Privacy in Computing and Communications, Changsha, China, 2011, pp. 940-949.

[130] C.-W. Chang, P. Liu, J.-J. Wu, Probability-based cloud storage providers selection algorithms with maximum availability, 41st International Conference on Parallel Processing (ICPP), Pittsburgh, Pennsylvania, USA, 2012, pp. 199-208.

[131] J.L. Henderson, S. MacKay, M. Peterson-Badali, Closing the research-practice gap: Factors affecting adoption and implementation of a children's mental health program, J. Clin. Child Adolesc. Psychol., 35 (2006) 2-12.

[132] A. Chaudhury, K. Nam, H.R. Rao, Management of information systems outsourcing: a bidding perspective, Journal of Management Information Systems, 12 (1995) 131-159.

[133] O.J. Akomode, B. Lees, C. Irgens, Constructing customised models and providing information to support IT outsourcing decisions, Logistics Information Management, 11 (1998) 114-127.

[134] P.S. Lokachari, M. Mohanarangan, Outsourcing of information technology services: A decisionmaking framework, Portland International Conference on Management of Engineering and Technology, Seattle, WA, USA, 2002, pp. 411.

[135] B. Xinyi, X. Jingjing, Developing a decision model for IT outsourcing using analytic hierarchy process, International Conference on Management and Service Science (MASS), Wuhan, China, 2009.

[136] G.G. Udo, Using analytic hierarchy process to analyze the information technology outsourcing decision, Industrial Management & Data Systems, 100 (2000) 421.

[137] S. Tajdini, M. Nazari, IS outsourcing decision: A quantitative approach, International Journal of Business & Management, 7 (2012) 113-129.

[138] M.A. Atkinson, O. Bayazit, B. Karpak, A case study using the Analytic Hierarchy Process for IT outsourcing decision making, International Journal of Information Systems and Supply Chain Management (IJISSCM), 8 (2015) 60-84.

[139] V. Pandey, V. Bansal, A decision-making framework for IT outsourcing using the analytic hierarchy process, International Conference on Systemics, Cybernetics and Informatics, Orlando, USA, 2004.

[140] C. Yang, J.-B. Huang, A decision model for IS outsourcing, International Journal of Information Management, 20 (2000) 225-239.

[141] L.B. Liu, P. Berger, A. Zeng, A. Gerstenfeld, Applying the analytic hierarchy process to the offshore outsourcing location decision, Supply Chain Management: An International Journal, 13 (2008) 435-449.

[142] C. Yiming, Z. Yiwei, SaaS vendor selection basing on Analytic Hierarchy Process, Fourth International Joint Conference on Computational Sciences and Optimization (CSO), Kunming and Lijiang City, China, 2011, pp. 511-515.

[143] S.K. Garg, S. Versteeg, R. Buyya, A framework for ranking of cloud computing services, Future Generation Computer Systems, 29 (2013) 1012-1023.

[144] M. Sun, T. Zang, X. Xu, R. Wang, Consumer-centered cloud services selection using AHP, International Conference on Service Sciences (ICSS), Shenzhen, China, 2013, pp. 1-6.

[145] J. Repschlaeger, T. Proehl, R. Zarnekow, Cloud service management decision support: An application of AHP for provider selection of a cloud-based IT service management system, Intelligent Decision Technologies, 8 (2014) 95-110.

[146] M. Godse, S. Mulik, An approach for selecting Software-as-a-Service (SaaS) product, IEEE International Conference on Cloud Computing, Bangalore, India, 2009, pp. 155-158.

[147] J.-J. Wang, D.L. Yang, Using a hybrid multi-criteria decision aid method for information systems outsourcing, Computers & Operations Research, 34 (2007) 3691-3700.

[148] H. Li, J. Wang, D. Yang, Where to outsource: Using a hybrid multi-criteria decision aid method for selecting an offshore outsourcing location, Americas Conference on Information Systems (AMCIS 2006), Acapulco, Mexico, 2006, pp. 3119-3127.

[149] J.-J. Wang, Z.-k. Lin, G.-Q. Zhang, A decision model for IS outsourcing based on AHP and ELECTREIII, 4th International Conference on Wireless Communications, Networking and Mobile Computing, Dalian, China, 2008, pp. 1-4.

[150] O.K. Ngwenyama, N. Bryson, Making the information systems outsourcing decision: A transaction cost approach to analyzing outsourcing decision problems, European Journal of Operational Research, 115 (1999) 351-367.

[151] K.-M. Osei-Bryson, O.K. Ngwenyama, Managing risks in information systems outsourcing: An approach to analyzing outsourcing risks and structuring incentive contracts, European Journal of Operational Research, 174 (2006) 245-264.

[152] A. Juan-Verdejo, S. Zschaler, B. Surajbali, H. Baars, H.G. Kemper, InCLOUDer: a formalised decision support modelling approach to migrate applications to cloud environments, 40th EUROMICRO Conference on Software Engineering and Advanced Applications (SEAA), Verona, Italy, 2014, pp. 467- 474.

[153] M. Ribas, C.G. Furtado, N. Souza, G. Barroso, A. Moura, A.S. Lima, F.R.C. Sousa, A Petri netbased decision-making framework for assessing cloud services adoption: The use of spot instances for cost reduction, Journal of Network and Computer Applications, Volume 57 (2015) 102–118.

[154] M. Walterbusch, B. Martens, F. Teuteberg, A decision model for the evaluation and selection of cloud computing services: a first step towards a more sustainable perspective, International Journal of Information Technology & Decision Making, 14 (2015) 253-285.

[155] K.K.F. Yuen, Software-as-a-Service evaluation in cloud paradigm: Primitive cognitive network process approach, IEEE International Conference on Signal Processing, Communications and Computing (ICSPCC), Hong Kong, 2012, pp. 119-124.

[156] M.N. Faisal, D.K. Banwet, Analysing alternatives for information technology outsourcing decision: An analytic network process approach, International Journal of Business Information Systems, 4 (2009) 47-62.

[157] Y. Tjader, J.H. May, J. Shang, L.G. Vargas, N. Gao, Firm-level outsourcing decision making: A balanced scorecard-based analytic network process model, International Journal of Production Economics, 147 (2014) 614-623.

[158] H. Tang-Nguyen, Y.C. Lee, The SWOT-ANP decision framework for the enterprise's cloud computing strategy, Information 18 (2015) 85-91.

[159] B. Do Chung, S. Kwang-Kyu, A cloud service selection model based on Analytic Network Process, Indian Journal of Science and Technology, 8 (2015).

[160] W.H. Tsai, J.D. Leu, J.Y. Liu, S.J. Lin, M.J. Shaw, A MCDM approach for sourcing strategy mix decision in IT projects, Expert Systems with Applications, 37 (2010) 3870-3886.

[161] J. Cao, G. Cao, W. Wang, A hybrid model using analytic network process and gray relationa analysis for bank's IT outsourcing vendor selection, Kybernetes, 41 (2012) 994-1013.

[162] S. Silas, E.B. Rajsingh, K. Ezra, Efficient service selection middleware using ELECTRE methodology for cloud environments, Information Technology Journal, 11 (2012) 868-875.

[163] D.L. Olson, Evaluation of ERP outsourcing, Computers & Operations Research, 34 (2007) 3715- 3724.

[164] B. Corbitt, I. Tho, Towards an economic analysis of IT outsourcing risks, Australasian Conference on Information Systems (ACIS 2005), Sydney, Australia, 2005.

[165] J. Dasgupta, R.P. Mohanty, Towards evaluating the risks of software services outsourcing industry, XIMB Journal of Management, 6 (2009) 29-48.

[166] D.L. Olson, D.D. WU, Multiple criteria analysis for evaluation of information system risk, Asia-Pacific Journal of Operational Research, 28 (2011) 25-39.

[167] Z.A. Fekete, L.-V. Hancu, A supplier selection model for software development outsourcing, Annals of the University of Oradea, Economic Science Series, 19 (2010) 1190-1195.

[168] B. Watjatrakul, Vendor selection strategy for IT outsourcing: The weighted-criteria evaluation technique, Journal of Enterprise Information Management, 27 (2014) 122-138.

[169] D.C. Morais, A.P.C. Costa, A.T. de Almeida, Group decision model for outsourcing it services, Procedia Technology, 16 (2014) 562-568.

[170] P. Nduwimfura, J. Zheng, A model for offshore information systems outsourcing provider selection in developing countries, International Business Research, 8 (2015) p68.

[171] J.-J. Wang, H.-F. Li, X.-J. Diao, D.-l. Yang, Developing a decision support model for information systems outsourcing, Second International Conference on Innovative Computing, Information and Control, 2007 (ICICIC '07), Tokyo, Japan, 2007, pp. 533-533.

[172] L. Hatami-Shirkouhi, K. Rezaie, S. Nazari-Shirkouhi, A. Ansarinejad, S. Miri-Nargesi, A practical framework for IS outsourcing using the integrated fuzzy group decision making approach, Computational Intelligence, Modelling and Simulation (CIMSiM), IEEE, Bali, Indonesia 2010, pp. 47- 50.

[173] S. Nazari-Shirkouhi, A. Ansarinejad, S. Miri-Nargesi, V.M. Dalfard, K. Rezaie, Information systems outsourcing decisions under fuzzy group decision making approach, International Journal of Information Technology and Decision Making, 10 (2011) 989-1022.

[174] S. Miri-Nargesi, A. Keramati, A. Ansarinejad, S. Nazari-Shirkouhi, A structured methodology for information systems outsourcing decisions using fuzzy MCDM, 2011 international conference on industrial engineering and operations management, Kuala Lumpur, Malaysia, 2011, pp. 445-450.

[175] C. Kahraman, A. Beskese, I. Kaya, Selection among ERP outsourcing alternatives using a fuzzy multi-criteria decision making methodology, International Journal of Production Research, 48 (2010) 547-566.

[176] C.-T. Chen, K.-H. Lin, A decision-making method based on interval-valued fuzzy sets for cloud service evaluation, International Conference on New Trends in Information Science and Service Science (NISS), Gyeongju, South Korea, 2010, pp. 559-564.

[177] G. Nie, Q. She, D. Chen, The evaluation and selection of cloud service by fuzzy MCDM, Journal of Systems Science & Information, 9 (2011) 135-144.

[178] H.-K. Kwon, K.-K. Seo, A Fuzzy AHP based multi-criteria decision-making model to select a cloud service, International Journal of Smart Home, 8 (2014) 175-180.

[179] A. Karami, Z. Guo, A fuzzy logic multi-criteria decision framework for selecting IT service providers, 45th Hawaii International Conference on System Science (HICSS), Maui, Hawaii, 2012, pp. 1118-1127.

[180] B. Oztaysi, A decision model for information technology selection using AHP integrated TOPSIS-Grey: The case of content management systems, Knowledge-Based Systems, 70 (2014) 44-54.

[181] S. Le, H. Dong, F.K. Hussain, O.K. Hussain, J. Ma, Y. Zhang, Multicriteria decision making with fuzziness and criteria interdependence in cloud service selection, IEEE International Conference on Fuzzy Systems, Beijing, China, 2014, pp. 1929-1936.

[182] S. Le, H. Dong, F.K. Hussain, O.K. Hussain, J. Ma, Y. Zhang, A hybrid fuzzy framework for cloud service selection, IEEE International Conference on Web Services (ICWS), Anchorage, Alaska, USA, 2014, pp. 313-320.

[183] H. Singh, R. Randhawa, CPSEL: Cloud provider selection framework for ranking AND selection oF cloud provider, International Journal of Applied Engineering Research, 10 (2015) 18787-18810.

[184] G. Xie, S. Mei, The strategic decision of fuzzy TOPSIS on partner' choice in IT outsourcing projects, 2011 International Conference on Computer Science and Service System (CSSS), Nanjing, China, 2011, pp. 906-909.

[185] C. Kahraman, O. Engin, O. Kabak, I. Kaya, Information systems outsourcing decisions using a group decision-making approach, Engineering Applications of Artificial Intelligence, 22 (2009) 832-841.

[186] D.-F. Li, S.-P. Wan, Fuzzy heterogeneous multiattribute decision making method for outsourcing provider selection, Expert Systems with Applications, 41 (2014) 3047-3059.

[187] R. Qiang, D. Li, An inhomogeneous multi-attribute decision making method and application to IT/IS outsourcing provider selection, International Journal of Industrial Engineering: Theory, Applications and Practice, 22 (2015) 252-266.

[188] T.-C. Wang, L.Y. Chen, Y.-H. Chen, Applying fuzzy PROMETHEE method for evaluating is outsourcing suppliers, Fifth International Conference on Fuzzy Systems and Knowledge Discovery, Jinan, Shandong, China, 2008, pp. 361-365.

[189] Y.H. Chen, T.C. Wang, C.Y. Wu, Strategic decisions using the fuzzy PROMETHEE for IS outsourcing, Expert Systems with Applications, 38 (2011) 13216-13222.

[190] L. Qu, Y. Wang, M.A. Orgun, Cloud service selection based on the aggregation of user feedback and quantitative performance assessment, IEEE International Conference on Services Computing (SCC), Santa Clara, CA, 2013, pp. 152-159.

[191] K. Chatterjee, M.B. Kar, S. Kar, Strategic decisions using intuitionistic Fuzzy Vikor method for information system (IS) outsourcing, International Symposium on Computational and Business Intelligence (ISCBI), IEEE, New Delhi, India 2013, pp. 123-126.

[192] L.Y. Chen, T.-C. Wang, Optimizing partners’ choice in IS/IT outsourcing projects: The strategic decision of fuzzy VIKOR, International Journal of Production Economics, 120 (2009) 233-242.

[193] J. Zhang, G. Cong, Y. Yu, Y. Gong, A fuzzy rough group decision-making model for rating and ranking IT outsourcing aggressive risk, International Conference on Service Systems and Service Management, IEEE, Troyes; France, 2006, pp. 1050-1056.

[194] S.K. Mathew, Understanding risk in IT outsourcing: A fuzzy framework, Journal of Information Technology Case & Application Research, 8 (2006) 27-39.

[195] G. Cong, J. Zhang, T. Chen, K.K. Lai, A variable precision fuzzy rough group decision-making model for IT offshore outsourcing risk evaluation, Journal of Global Information Management, 16 (2008) 18-34.

[196] C. Samantra, S. Datta, S.S. Mahapatra, Risk assessment in IT outsourcing using fuzzy decisionmaking approach: An Indian perspective, Expert Systems with Applications, 41 (2014) 4010-4022.

[197] Z.-P. Fan, W.-L. Suo, B. Feng, Identifying risk factors of IT outsourcing using interdependent information: An extended DEMATEL method, Expert Systems with Applications, 39 (2012) 3832-3840.

[198] G. Büyüközkan, O. Feyzioğlu, An intelligent decision support system for IT outsourcing, in: L.

Wang, L. Jiao, G. Shi, X. Li, J. Liu (Eds.) Third international conference on Fuzzy Systems and Knowledge Discovery, Springer-Verlag, Xi'an, China, 2006, pp. 1303-1312.

[199] X. Xiang, G. Zhong-liang, Study on a decision model of IT outsourcing prioritization, International Conference on Systems, Computing Sciences and Software Engineering (SCSS 05), Bridgeport, Connecticut, US, 2006, pp. 265-269.

[200] X. Chen, J. Han, A novel IS/IT outsourcing service vendor selection method based on fuzzy axiomatic design, IEEE 18th International Conference on Industrial Engineering and Engineering Management, IE and EM 2011, Changchun, China, 2011, pp. 21-25.

[201] M.N. Faisal, R.S. Asif, IT outsourcing intent in academic institutions in GCC countries: An empirical investigation and multi-criteria decision model for vendor selection, Journal of Enterprise Information Management, 29 (2016) 432-453.

[202] A. Christoforou, A.S. Andreou, A multilayer fuzzy cognitive maps approach to the cloud adoption decision support problem, IEEE International Conference on Fuzzy Systems (FUZZ-IEEE), Istanbul, Turkey, 2015, pp. 1-8.

[203] U. Shivakumar, V. Ravi, G.R. Gangadharan, Ranking cloud services using fuzzy multi-attribute decision making, IEEE International Conference on Fuzzy Systems, Hyderabad, India, 2013.

[204] Y.-F. Zheng, J. Xu, Multiple attribute decision making with triangular intuitionistic fuzzy numbers and application to cloud service provider selection, 2nd International Conference on Information Technology and Electronic Commerce（ICITEC 2014), Dalian, China, 2014, pp. 311-315.

[205] S. Grandhi, S. Wibowo, Performance evaluation of cloud computing providers using fuzzy multiattribute group decision making model, 12th International Conference on Fuzzy Systems and Knowledge Discovery (FSKD), Zhangjiajie, China, 2015, pp. 130-135.

[206] W. Fan, S. Yang, J. Pei, A novel two-stage model for cloud service trustworthiness evaluation, Expert Systems, 31 (2014) 136-153.

[207] C.-H. Cheng, J. Balakrishnan, W.-C. Wong, A quantitative model for analysing IS outsourcing decisions, International Journal of Services Operations and Informatics, 1 (2006) 221-232.

[208] F.-J. Chen, P. Cao, Ant colony optimization algorithm for vendor selection in information systems outsourcing, International Conference on Business Intelligence and Financial Engineering, IEEE, Beijing, China, 2009, pp. 134-137.

[209] F. Zandi, A bi-level constraint-oriented outsourcing framework for orchestration of an ERP system, International Journal of Production Research, 52 (2014) 130-148.

[210] C.-I. Hsu, C. Chiu, P.-L. Hsu, Predicting information systems outsourcing success using a hierarchical design of case-based reasoning, Expert Systems with Applications, 26 (2004) 435-441.

[211] Y. Jiang, L. Chen, X. Zhou, Y. Liu, Process-oriented software outsourcing decision based on genetic algorithm, International Conference on Service Operations and Logistics, and Informatics (SOLI), IEEE QingDao, China, 2010, pp. 386-391.

[212] B. Hanus, J. Windsor, Multidimensional decision model for investment in cloud computing, Americas Conference on Information Systems (AMCIS), Chicago, USA, 2013, pp. 2498-2508.

[213] C. Ping, C. Fu-ji, Z. Jian, A multi-objective model of information system outsourcing decision for suppliers selection, International Conference on Computational Intelligence and Natural Computing (CINC), Wuhan, China, 2009, pp. 242-245.

[214] G. Fridgen, H.-V. Müller, An approach for portfolio selection in multi-vendor IT outsourcing, Thirty Second International Conference on Information Systems, Shanghai, China, 2011.

[215] M. Lilienthal, A decision support model for cloud bursting, Business & Information Systems Engineering, 5 (2013) 71-81.

[216] C. Singh, R. Shelor, J. Jiang, G. Klein, Rental software valuation in IT investment decisions, Decision Support Systems, 38 (2004) 115-130.

[217] N. Roedder, P. Karaenke, R. Knapper, A risk-aware decision model for service sourcing IEEE International Conference on Service-Oriented Computing and Applications, 2013, pp. 135-139.

[218] G. Baranwal, D.P. Vidyarthi, A framework for selection of best cloud service provider using ranked voting method, IEEE International Advance Computing Conference (IACC), Gurgaon, India, 2014, pp. 831-837.

[219] C. König, P. Mette, H.-V. Müller, Multivendor portfolio strategies in cloud computing, 21st European Conference on Information Systems (ECIS), Utrecht, the Netherlands, 2013, pp. 61.

[220] J.B. Davis, Insights from a real options approach to evaluate IT sourcing decisions, Americas Conference on Information Systems (AMCIS 2005), Savannah, Georgia, USA, 2005, pp. 2971-2977.

[221] M. Benaroch, Managing information technology investment risk: a Real Options perspective, Journal of Management Information Systems, 19 (2002) 43-84.

[222] S.T. Roehling, J.S. Collofello, B.G. Hermann, D.E. Smith-Daniels, System dynamics modeling applied to software outsourcing decision support, Software Process: Improvement and Practice, 5 (2000) 169-182.

[223] Z. Tang, G. Liang, R. Wu, A game analysis of outsourcing strategy for enterprise informatization, in: L.D. Xu, A.M. Tjoa, S.S. Chaudhry (Eds.) IFIP International Conference on Research and Practical Issues of Enterprise Information Systems Boston: Springer, Beijing, China, 2008, pp. 1523-1528.

[224] E. Furuncu, I. Sogukpinar, Scalable risk assessment method for cloud computing using game theory (CCRAM), Computer Standards & Interfaces, 38 (2015) 44-50.

[225] C. Loebbecke, C. Huyskens, Development of a model-based netsourcing decision support system using a five-stage methodology, European Journal of Operational Research, 195 (2009) 653-661.

[226] L. Mastroeni, M. Naldi, Storage Buy-or-Lease decisions in cloud computing under price uncertainty, 7th EURO-NGI Conference on Next Generation Internet (NGI), Kaiserslautern, Germany, 2011, pp. 1-8.

[227] L. Xiu-Wu, W. Tao, L. Yuan, A Bayesian network model under group decision making for evaluating IT outsourcing risk, International Conference on Risk Management and Engineering Management (ICRMEM ), IEEE, Beijing; China, 2008, pp. 559-564.

[228] H.U. Buhl, G. Fridgen, C. König, Using financial derivatives to hedge against market risks in IT outsourcing projects - a quantitative decision model, Journal of Decision Systems, 22 (2013) 249-264.

[229] G. Cong, T. Chen, A novel dynamic algorithm for IT outsourcing risk assessment based on transaction cost theory, Discrete Dynamics in Nature and Society, 2015 (2015).

[230] G. Xie, J. Zhang, K.K. Lai, A group decision-making model of risk evasion in software project bidding based on VPRS, 10th International Conference Rough Sets, Fuzzy Sets, Data Mining, and Granular Computing, Regina, Canada, 2005, pp. 530-538.

[231] Z. Rehman, F.K. Hussain, O.K. Hussain, Towards multi-criteria cloud service selection, International Conference on Innovative Mobile and Internet Services in Ubiquitous Computing (IMIS), Seoul, Korea, 2011, pp. 44-48.

[232] S. Gregor, D. Jones, The Anatomy of a Design Theory, Journal of the Association for Information Systems, 8 (2007) 313-335.

[233] J.R. Meredith, A. Raturi, K. Amoako-Gyampah, B. Kaplan, Alternative research paradigms in operations, Journal of Operations Management, 8 (1989) 297-326.

[234] J.W.M. Bertrand, J.C. Fransoo, Operations management research methodologies using quantitative modeling, International Journal of Operations & Production Management, 22 (2002) 241-264.

[235] R.M. O'Keefe, O. Balci, E.P. Smith, Validation of expert system performance, IEEE Expert 2(1986) 81-90.

[236] D. Borenstein, Towards a practical method to validate decision support systems, Decision Support Systems, 23 (1998) 227-239.

[237] P.N. Finlay, Introducing decision support systems, NCC Blackwell, Oxford, UK, 1989.

[238] H. Miser, E. Quade, Validation, in: H. Miser, E. Quade (Eds.) Handbook of Systems Analysis: Craft issues and Procedural Choices, Wiley, UK, 1988, pp. 527-565.

[239] S. Schlesinger, R.E. Crosbie, R.E. Gagné, G.S. Innis, C.S. Lalwani, J. Loch, R.J. Sylvester, R.D. Wright, N. Kheir, D. Bartos, Terminology for model credibility, Simulation, 32 (1979) 103-104.

[240] B. Johnson, Y. Qu, A holistic model for making cloud migration decision: a consideration of security, architecture and business economics, IEEE 10th International Symposium on Parallel and Distributed Processing with Applications (ISPA), Madrid, Spain, 2012, pp. 435-441

[241] F. Moyano, K. Beckers, C. Fernandez-Gago, Trust-aware decision-making methodology for cloud sourcing, 26th International Conference on Advanced Information Systems Engineering (CAiSE 2014), Springer, Thessaloniki, Greece, 2014, pp. 136-149.

[242] Q. Yu, CloudRec: a framework for personalized service Recommendation in the Cloud, Knowledge and Information Systems, 43 (2015) 417–443.

[243] J.R. Venable, A framework for design science research activities, 2006 Information Resource Management Association Conference, Washington, DC, USA, 2006, pp. 21-24.

[244] T.G. Gill, A.R. Hevner, A fitness-utility model for design science research, ACM Transactions on Management Information Systems (TMIS), 4 (2013) 1-24.

## Appendix A: Article coding frame

The following template was used to code and analyze the surveyed articles.

1. Article title:

2. Publication year:

3. Article Type : Journal / Conference

4. The designed artifact

4.1. Type of artifact: a) Construct b) Model c) Method d) Instantiation

5. What ITO technology is supported? a) General ITO b) Cloud sourcing c) ASP d) Netsourcing

6. What IT sourcing decisions are supported?

a) Adoption / Risk assessment

b) Deciding the level of ITO

c) What to outsource

d) IT Vendor/Service provider/location selection

7. Theoretical foundations:

7.1. What theories/frameworks have been cited?

7.2. What decision analysis method(s) is (are) used?

8. Research methodologies: What research methodology has been adopted?

9. Evaluation

9.1. Type of evaluation according to Hevner et al.’s taxonomy

<table><tr><td>Category of Evaluation Method</td><td>Specific Evaluation Method</td></tr><tr><td>Observational</td><td>1. Case Study 2. Field Study</td></tr><tr><td>Analytical</td><td>3. Static 4. Architecture 5. Optimization 6. Dynamic Testing</td></tr><tr><td>Experimental</td><td>7. Controlled Experiment 8. Simulation</td></tr><tr><td>Testing</td><td>9. Functional (Black Box) 10. Structural (White Box)</td></tr><tr><td>Descriptive</td><td>11. Informed Argument 12. Scenarios</td></tr><tr><td>No evaluation</td><td>13. None</td></tr></table>

9.2. Type of evaluation according to Venable et al.’s quadrant

9.2.1. Evaluation timeline: a) Ex ante b) Ex post

9.2.2. Evaluation nature: a) Naturalistic b) Artificial

10. Did the article report validation of the artifact?

11. What organizational factors are considered in the design of the artifact?

11.1. Sector/Industry

11.2. Size (e.g. small, medium, large)

12. Is support for group decision-making mentioned in the article? a) Yes b) No.

## Biographical Note

Dr. Mohammad Mehdi Rajaeian is a casual academic staff at the University of Southern Queensland (USQ), Australia. He received a BSc in Industrial Engineering and a MBA both from Sharif University of Technology, Iran, and a PhD in Information Systems from USQ. His research interest include: IT outsourcing, Decision Support Systems, System Theory, Diffusion of Innovation and researchpractice gap. Mehdi holds a Lecturing position at Sadjad University of Technology, Iran. Prior to his academic career, He worked as system analyst, programmer and IT Manager in different organizations.

![](/api/attachments/VMG4VDBV/fulltext/images/29f3ae06c9cedfcee60b957682d6bc3392731820e96c4e8e143fe0032ef2b6a9.jpg)

Professor Aileen Cater-Steel’s research interests include IT Service Management (ITSM), IT Standards and Governance, e-Learning systems, and IT outsourcing. She was Lead Chief Investigator on two ITSM projects that achieved funding from the Australian Research Council. She has published in top journals and co-edited three research books. Her work has been recognized with a citation from the Australian Learning & Teaching Council for outstanding contribution to student learning. Prior to her academic appointment, Aileen worked in the private sector and government organizations where her career progressed from programmer to IT Manager. She is a Fellow of the Australian Computer Society (ACS) and member of the ACS Professional Standards Board.

![](/api/attachments/VMG4VDBV/fulltext/images/23b63a3e7de672007f24c5ff5401e859cc2ac5bac026b62c2a21bb38a218aee0.jpg)

Dr. Michael Lane is a senior lecturer in Information Systems, within the School of Management and Enterprise and Law. He holds a PhD in Information Systems from the University of Southern Queensland. He has a strong managerial and technical background in ICT. Michael Lane has extensive experience in IT Outsourcing from research and industry perspectives. His research in information outsourcing includes Impact of Partnership and Service quality on the IT Outsourcing Relationship and IT

Outsourcing Success, and the Governance of Risks in IT Sourcing Models including IT Outsourcing and Offshoring.

![](/api/attachments/VMG4VDBV/fulltext/images/714dead914e2b0401f49f5920ff46451a4dd851f8351bcd7d1c051bca6e5b669.jpg)

## Highlights

 IT sourcing decision support researchers adopted diverse decision analysis methods

 Use of naturalistic evaluation & reference theories is limited in IT sourcing research

 Recommendation for development of IT sourcing decision support artifacts presented
