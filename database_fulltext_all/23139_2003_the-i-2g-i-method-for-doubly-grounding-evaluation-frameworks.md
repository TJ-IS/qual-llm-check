---
otero_id: 23139
otero_key: "FQYQGTY9"
title: "The<i> 2G </i>method for doubly grounding evaluation frameworks"
authors: "Björn Lundell; Brian Lings"
year: "2003"
journal: "Information Systems Journal"
doi: "10.1046/j.1365-2575.2003.00154.x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The 2G method for doubly grounding evaluation frameworks

Björn Lundell\* & Brian Lings<sup>†</sup>

\*Department of Computer Science, University of Skövde, Sweden, email: bjorn@ida.his.se, and <sup>†</sup>School of Engineering, Computer Science and Mathematics, University of Exeter, UK, email: B.J.Lings@exeter.ac.uk

Abstract. There are a number of approaches open to an information system (IS) development organization wishing to evaluate the potential relevance of an IT product for use in their own organization. This work considers method support for evaluation of CASE tools, as a complex example of an IT product. Our interest is in evaluation for selection, namely the evaluation of products prior to experience of their use in the defined context. Certain weaknesses are apparent in existing evaluation methods proposed in the literature for evaluation for selection. Our primary concern in this paper is to present a new method which, we claim, addresses these weaknesses. We provide a rationale and a detailed description of the new method, which is referred to as 2G. The method specifically addresses the important early phases of an evaluation, during which an evaluation framework is to be established. The method is to be used within the intended usage context for the IT product, so the resulting evaluation framework will be situated rather than general. We identify weaknesses in previously available methods, and discuss the advantages offered by the 2G method. The method has a solid basis in underlying theory, something which has influenced our presentation of it. Equally importantly, our presentation is strongly influenced by our experience with the method in actual usage situations, in small and medium IS development organizations. We claim that 2G is a practical candidate for any IS development organization wishing to undertake evaluations of CASE tools prior to adoption.

Keywords: CASE-tool evaluation, contextual sensitivity, evaluation framework, Grounded Theory, method development, method support

## INTRODUCTION

Evaluation is an inherently complex process with many facets, but one which managers can ill-afford to neglect (Irani & Love, 2001). In the literature, method support has been considered both for the evaluation of products (e.g. CASE tools) and processes (e.g. modelling processes). In the work reported here, we have addressed the evaluation of products, and have chosen to concentrate initially on CASE tools as an example of complex IT products.

It is apparent that previous studies on CASE-tool evaluation are partitioned into those which assess a set of CASE tools prior to adopting one in a usage situation and those which evaluate experience with adopted CASE tools in a given usage situation. In what follows we refer to the former as pre-usage evaluation, and the latter as post-usage evaluation. Our own concern has been with pre-usage evaluation methods.

For some time now, the deployment of CASE technology has been seen as an important step in increasing productivity and quality control in information systems (IS) development in organizations. However, the success with which IS development organizations deploy modern CASE technology is at best variable (see, e.g. McComb, 1994; Martin, 1995; SEI, 1995; IVF, 1997; Rahim et al., 1997; Sharma & Rai, 2000). One reason for poor adoption results is that expectations of CASE are unrealistic (Senn & Wynekoop, 1995; Glass, 1999; Iivari & Lyytinen, 1999), another is that real user requirements are not being adequately met by products (Kudrass et al., 1996; Jankowski, 1997; Post & Kagan, 2001). Matching expectations with products is a continuing issue, both for users and for manufacturers, highlighting the important role of evaluation.

The importance of systematic method support for CASE-tool evaluation for selection has been recognized by a number of authors. Many of these, including Kitchenham & Jones (1997a), argue that a framework is necessary in order to make any sort of comparative evaluation of CASE tools. It has also been argued that the task of establishing such a framework is complex and related to human concerns, recognizing that each organization has ‘its own personality and culture’ (Prather, 1993, p. 62). This is echoed by Brown & Wallnau (1996), who claim that there are both technical and ‘non-technical considerations’ (p. 42) when evaluating a technology.

As a consequence, we believe that any evaluation of CASE tools should ideally be carried out within the anticipated usage context, and any method developed to support evaluation should explicitly acknowledge this. The dual focus on organizational and technological dimensions makes this a complex issue. In this paper, we present the 2G method for evaluation framework development. Our aim in developing the method has been to provide better support for an IS development organization wishing to conduct pre-usage evaluation of CASE-tool products for a specific usage situation.

The rest of this paper is structured as follows. Firstly, we present the research methods used in the work presented here. We then review related work on pre-usage evaluation of CASE tools, focusing on systematic support for establishing a relevant evaluation framework. Having identified weaknesses in existing approaches, we present the 2G method in overview, identifying its key aspects. This is followed by detailed consideration of each aspect, including the different types of data source (and their potential usage with the method); the two types of evaluation framework developed using the method; and the process of framework development. We then consider implications of our findings for practitioners wishing to conduct a pre-usage evaluation. Finally, we outline areas of ongoing research and draw our conclusions.

## RESEARCH METHOD

Our research has been conducted in the tradition of qualitative/interpretive research, and in particular the use of Grounded Theory, a general method of analysis which has been used in exploring many substantive areas of research. A number of researchers have identified Grounded Theory as a suitable basis for addressing IS problems related to user expectations and requirements (Pidgeon et al., 1991; Urquhart, 1997; Hughes, 1998; Galal & Paul, 1999; Howcroft & Hughes, 1999; Ashry & Taylor, 2000). Further, several researchers report that Grounded Theory has informed their research efforts in the CASE-technology area, and in particular their analysis of CASE tools in a specific usage context (Calloway & Ariav, 1991; 1995; Pries-Heje, 1991; 1992; Orlikowski, 1993; Cronholm, 1995). In fact, there are differing interpretations of Grounded Theory evident in the literature (see Melia, 1996 for a discussion of this). In the work reported in this paper, we have followed the strand emanating from Glaser (as expounded in Glaser & Strauss, 1967; Glaser, 1978; 1992; 1998; Starrin et al., 1991; 1997).

The 2G method was evolved through a formative field study in a small software development company. The company had developed applications for quality control in the automotive industry, and was interested in evaluating whether CASE tools could be utilized in maintaining these systems. Open interviews were conducted with one senior systems developer. The interviewee was well versed in qualitative methods, having used these in a number of IS development projects at the Swedish Social Insurance Organization. Data collection and analysis were performed over six half-day sessions spread over a 6-month period. Data sources included extensive system development documentation and other internal company documents. Two commercial CASE tools were explored in the study.

The formative study was complemented by an ongoing literature review. The review initially focused on method support for pre-usage evaluation of CASE tools, motivated by a perceived lack of method support for evaluation framework development in drafts of ISO 14102 (ISO, 1995; Lundell & Lings, 2002). Later, it was broadened to consider the general evaluation literature, in order to guide validation (including transfer and scalability) of the 2G method through further field studies.

Method transfer was investigated through two studies, each having a method user new to the method. One was a field study, in a different IS development company. The method user was based full-time in the company for a period of 4 months, during which both group and individual open interviews were used. The second was conducted within an academic environment. Apart from transfer, the intention was to gain further experience with the method and particularly the utility of the different phases in 2G.

A fuller field study has been used to address the issue of scalability. It was undertaken in Volvo IT, a company of 2500 co-workers (at the time of the study in 2000) responsible for the development and implementation of IT solutions for several large manufacturing plants in the automotive industry. Nine respondents were selected by the company, on the basis of expertise across all life-cycle phases. Knowledge of CASE tools was extensive, some tools having been developed in-house. The method user was again based in the company, being treated as a member of the team. Open interviews ranged from one to two and a half hours. A decision was made not to tape interviews, but extensive notes were taken. After transcription, each interview generated 600–2300 words of unformatted text complemented by illustrations. These were confirmed with the interviewee. Anonymity was preserved throughout. The evaluation framework developed consisted of about 400 concepts reported in 100 pages of text (23 000 words).

## RELATED WORK

We have observed that methods proposed for pre-usage evaluation<sup>1</sup> are primarily CASE tool centred (Zucconi, 1989; Sodi, 1991; Topper, 1991; Dixon, 1992; IEEE, 1992; 1998; Le Blanc & Korn, 1992; 1994; Mosley, 1992; Huff et al., 1992; Skramstad & Khan, 1992; Beckworth, 1993; du Plessis, 1993; Shafer & Shafer, 1993; Bell, 1994; Antonakopoulos et al., 1995; ISO, 1995; Jankowski, 1995; 1997; Daneva & Terzieva, 1996; Daneva, 1997; Kitchenham & Jones, 1997a,b;<sup>2</sup> Powell et al., 1997; Juric & Kuljis, 1999). They are systematic, in that they embody a systematic way of working during an evaluation. However, they tend to be centred on current technology in that they are feature based, and promote a structured, context-independent process.

There is an underlying assumption in these methods, either implicit or explicit, of an evaluation framework. Such a framework comprises a representation of potentially relevant tool features and how they interrelate, and is sometimes referred to as a checklist. Whereas some published frameworks are rather ‘inclusive’ and aimed at CASE tools in general (Ovum, 1993), others are tailored for use in a pre-usage evaluation of specific types of CASE tool, and perhaps limited aspects of them. For example, there are those designed for analysis of: support for customisability of a CASE tool (Goldkuhl et al., 1992); CASE-tool support for planning and design activities (Henderson & Cooprider, 1990); support for structured systems analysis and design techniques (Vessey et al., 1992); hypertext functionality in CASE tools (Kaipala, 1997); reverse engineering tools (Skramstad & Khan, 1992); data modelling tools (Moriarty, 1998); database design tools (Reiner, 1992); testing tools (Poston & Sexton, 1992); software engineering environments (Palvia, 1992); collaborative work (Vessey & Sravanapudi, 1995); conformance to a specific modelling notation (e.g. UML – Juric & Kuljis, 1999); conformance to method rules in structured analysis (Jankowski, 1997); usability of CASE tools (Cronholm, 1998); and quality assurance of ER Models (Barker, 1990, chapter 10).

However, a number of problems are acknowledged with published frameworks. Firstly, the frameworks proposed in different studies are significantly different. Secondly, frameworks must continually be updated as technology changes. Thirdly, even the developers of frameworks would accept that they cannot be used without modification in a specific usage situation. Fourthly, terms used in frameworks may be interpreted differently in different contexts. We consider each of these problems in turn.

Frameworks differ partly because of a lack of consensus on expectations from CASE tools. This is an interesting observation, given the extensive effort that may be invested in the development of a framework. Both Henderson & Cooprider (1990) and Ovum (1993) have developed rather extensive frameworks for CASE tools, but their content is rather different. Henderson and Cooprider describe the use of ‘leading CASE-designers (both academics and practitioners)’ (p. 230), who identified 98 potentially relevant instances of CASE-tool functionality, which were then sorted (by a set of other experts) ‘into one of the a priori dimensions’ (p. 231) of CASE-tool functionality. As a motivation for their framework, they claim that ‘years of both theoretical and empirical research on I/S planning and design provide a basis for developing an a priori model’ (p. 231).

One problem with published frameworks is that they are inherently static, whereas CASE technology evolves over time. This problem is also recognized in some frameworks (ISO, 1995, p. 25). Moriarty (1995; 1998) presents us with one example of how one individual author’s view of the appropriate content for a framework can change over time. We note that both these sources are designed for the same type of CASE tool (namely for data modelling support).

Most sources emphasize that the contents of presented frameworks are to be taken as potentially relevant aspects, to be considered in an evaluation if found appropriate for the evaluation task at hand. The method by which aspects are to be classified as appropriate is usually not elaborated.

Further, it has been shown to be problematic to arrive at a broadly shared, in-depth understanding of even a single criterion that is defined a priori. This is clearly shown in an empirical and exploratory study (van Reeken & Trienekens, 1992) concerning method and CASE-tool usage, undertaken in 16 of the largest organizations in the Netherlands. Each organization was found to use the same terms in fundamentally different ways.

These difficulties, we claim, give a strong motivation for developing an evaluation framework within a particular organizational setting, and for a specific evaluation activity.

Powell et al. (1997) express the view that contextual issues of an evaluation, such as ‘how the tool may/will be used’ are ‘crucial to a successful evaluation, emplacement and use’ (p. 169). They view a tool evaluation process as consisting of two main activities. In the first, the aim is to understand the usage context, and in the second, the aim is to analyse and understand the tool. For both these activities, they consider it important to ‘capture knowledge’ (p. 170) from the analysis to be used in future evaluations. However, even though they acknowledge the importance of contextual sensitivity when developing an evaluation framework, their approach to utilizing previous experience in a current situation is not elaborated in any detail.

Further, their approach is based on a published framework, and the extent to which its content is grounded in their contextual setting or is taken a priori is unclear. In fact, the lack of an in-depth discussion concerning the origin of their framework and possible problems associated with its interpretation can, in our view, be taken as a strong indication that the authors do not consider this issue to any great extent.

In general, there are few reported experiences from the actual application of pre-usage methods in IS development organizations. Further, those reports that actually provide some evidence from practice (Mosley, 1992; Powell et al., 1997; Calzolari & Cozzio, 1999) contain limited detail concerning how to undertake the task of developing (and situating) an evaluation framework to meet the specific demands from the contextual setting in which the evaluation is to take place.

For other pre-usage methods we have identified, their applicability as general methods in an IS development organization is (at best) unproven. For some, the issue of whether they have actually been applied and tested in an actual IS development organization is either unclear (Le Blanc & Korn, 1994; ISO, 1995), or answered in the negative (Beckworth, 1993; du Plessis, 1993). Others may have been applied, but cannot be considered to be general. This may be because they have been designed for, or only applied in rather ‘technical’ domains (e.g. addressing real-time requirements (Vollman, 1994)<sup>3</sup> or supporting the testing of software components (Antoniol et al., 1999). Alternatively, they may have a very narrow focus (e.g. methods which address conformance to method rules (e.g. Structured Analysis – Jankowski, 1997; UML – Juric & Kuljis, 1999), or support for reverse engineering (Skramstad & Khan, 1992).

Alternatively, there exist general IS methods (Bubenko, 1993; Galal & Paul, 1999; Hughes & Wood-Harper, 1999) which acknowledge the inherent complexity in organizational requirements. With respect to their underlying values and acknowledgement for the contextual issues, such methods are of significant interest in the context of this work. However, we claim that they do not provide the necessary detail in their method support for a pre-usage CASE-tool evaluation activity, and in particular for the systematic exploration of technical issues. The potential for technical exploration to have a major impact on requirements formulation is well recognized (see, e.g. Butler & Fitzgerald, 1999, p. 365); in the context of tool evaluation, we believe it to be critical, and method support to be essential.

One further dimension may be noted. In identifying design criteria for method support in the field of decision support systems, Zuurbier et al. (1994) advocate an iterative approach, as it is difficult to state all requirements in advance. New requirements arise with use of a system, perhaps through several iterations; there is consequently a learning aspect involved, reinforcing an understanding of requirements.

## THE 2G METHOD: AN OVERVIEW

In this section, we present 2G, a pre-usage method for the development of evaluation frameworks. The method specifically addresses the difficult task of integrating the ‘softer’ social and organizational requirements with the more detailed technical aspects of the technology, and in particular what can realistically be expected from current ‘state-of-the-art’ CASE-tool products. To illustrate aspects of the method, we will use examples from a formative field study (Lundel et al., 1999) and a more recent field study (Rehbinder et al., 2001; 2002).

The method differs in two main respects from other systematic methods for developing a CASE-tool evaluation framework. Firstly, it does not use concepts that have been defined a priori. Instead, the definition of concepts evolves during analysis. Secondly, it does not use an a priori structure for interrelating these concepts. Instead, the structure emerges during analysis. Therefore, we would characterize its approach as primarily ‘data driven’. By contrast, other approaches (including ISO 14102, ISO, 1995) could be characterized as ‘concept-driven’, in that all CASE-tool characteristics have (ideally) been previously defined, and organized into a predefined (hierarchical) structure.

In 2G, the method user develops an evaluation framework which is grounded in organizational data. Table 1 shows a number of textual extracts from interview data. These may be seen as indicators<sup>4</sup> that together support the concept of a standard DBMS repository, which will then be incorporated into the evaluation framework.

There are many ways in which such concepts can then be interrelated to aid comprehension. Figure 1 shows one approach used, in which concepts are linked to general categories. This is similar to a pure application of Grounded Theory. However, 2G is unique in that a second framework is developed, which is further grounded in data representing the pragmatics of current state-of-the-art technology. The method therefore implies double grounding (hence 2G). It also differs from Grounded Theory in a number of other technical ways, in particular that the development of a core category for theory development is not a goal.

An application of 2G is initiated with the selection of a number of data sources. Some of these will pre-exist, including organizational manuals, documentation of prior evaluation activities, policy documents, etc. Others will be generated, for example, as the transcripts of open interviews<sup>5</sup> with selected personnel. The data sources are analysed with the goal of evolving a set of interrelated concepts, with agreed interpretation (see Table 2).

Two evaluation frameworks are produced when using 2G: a strategic evaluation framework, which characterizes an ideal CASE tool for the usage context; and a pragmatic evaluation framework, a version of the strategic framework which has been modified pragmatically to

Table 1. Indicators supporting a concept

<table><tr><td>Concept</td><td>Indicators</td></tr><tr><td>Standard DBMS repository</td><td>Repositories should also be heavily standardized with the ultimate goal of having a central multi-user repository that people and CASE tools may connect toSupporting the placement of a central repository in an MS SQL database is goodThe repository should have clear interfaces with the supporting DBMSA repository should indeed be located in a database that users may connect to as opposed to only having local filesData, models and descriptions, disregarding whether in files or in repositories should be maintainable and thus not tool specificA repository should not be tied to a specific database but instead be compatible with several databases...</td></tr></table>

![](/api/attachments/FQYQGTY9/fulltext/images/59e022de4fd68015a4c326bd8f367c59667b120e3e29bcb164e3eb45d0eece88.jpg)  
Figure 1. Concept linking via categories.

Table 2. Concept interpretations

<table><tr><td>Concept</td><td>Interpretation</td></tr><tr><td>Fully automatic code generation</td><td>CASE tools should support generation of complete program code (if possible) based on models and other representations specified by developers</td></tr><tr><td>Change propagation</td><td>CASE tools should support applying changes in models and then have these propagated to other models, code and documentation</td></tr></table>

reflect the state-of-the-art in CASE technology. For example, in one field study the concept traceability from the strategic framework was replaced in the pragmatic framework by the concept annotations as first class objects.<sup>6</sup> This was because none of the candidate CASE tools satisfied traceability as interpreted in the organization, so it would become non-discriminating in any evaluation of the tools. Annotations were seen as a substitute feature, and the nature of annotation features then became an important discriminator.

In practice, the development of an evaluation framework is an evolutionary process involving data collection, analysis and coding (Figure 2). These activities are not inherently sequential; each can affect (and trigger) the others so that, in essence, all activities are going on together.

Phase 2 is entered when the strategic framework is considered stable enough for use in a pilot evaluation of products. Such a pilot is used to develop a new version of the framework. The strategic framework must not itself be refined in phase 2 (it represents an ideal, not constrained by current technology), although new information may cause the process to cycle back to phase 1. For example, the annotation concept (above) was identified through tool exploration and then considered for possible interest to the stakeholders in its own right, not just as a potential alternative to traceability functionality. It thereby contributed to a new concept (document annotations) in the strategic framework.

![](/api/attachments/FQYQGTY9/fulltext/images/278e7f718df7ee8ae7875d2fb938387a856b99cc1b212845199a49db6fa19ce2.jpg)  
Figure 2. The proposed method: its phases and data flow.

The overall development process stops when both frameworks are considered stable and effective. The pragmatic framework can then be used in a full evaluation.

It is important to the method that both pilot and full evaluations take place in the organizational setting in which any chosen tool would be used, to maintain grounding of both evaluation frameworks.

The major novelty in 2G is its use of two distinct phases, each responsible for evolving a distinct version of the evaluation framework, with iteration between them (Figures 2 and 3). It should be noted that the discoveries and experiences flowing back from the phase 2 process into the data sources for the phase 1 process must be abstracted away from current products, into issues at the organizational requirements level. These can then be considered in the next iteration. One version of the framework therefore represents a long-term investment based on organizational requirements and free from specific constraints of current technology. The other is further grounded in the specific CASE tools under consideration. Piloting an evaluation in phase 2 may lead to an organization increasing the precision of, or expanding their own requirements in the next iteration of phase 1. Alternatively, the organization may simply become more conservative in their demands (‘pragmatism’) when it is realized that their requirements cannot be met with an off-the-shelf product. The annotation example illustrates all of these aspects: pragmatism, in that it replaced generally unavailable traceability features with a weaker, alternative concept; increased precision, in that tool investigation led to an understanding of the need for annotations to be first class objects; and expanding requirements, in that annotations were subsequently considered important by stakeholders for othe purposes, and so added as a concept to the strategic framework.

![](/api/attachments/FQYQGTY9/fulltext/images/5a35fccd8901ba72c6835e764c1e58b7f987f906c2ed0c3926fc10bd83f5d512.jpg)  
Figure 3. The roles of the two proposed method phases.

In applying 2G, it is not necessary to initially identify a ‘complete’ set of data sources. Instead, the process of developing an evaluation framework will, over time, invoke new sources naturally during the course of analysis.

## DATA SOURCES FOR 2G

When applying 2G, a broad variety of different types of data source might be relevant for, and have an impact on, the emerging framework. In order to assist the method user, it has been found useful to categorize potential data sources according to who are the stakeholders in its interpretation. It should be emphasized that these are inherently fuzzy concepts, and intended only for guidance.

Contextual data sources refer to data sources for which an interpretation need only be sought from those directly involved in the usage context. It may be that such a source had its origin within the usage context, although this does not need to be so. Interview data in an application of 2G would be classified as a contextual data source.

Organizational data sources refer to data sources for which an interpretation needs to be sought more broadly within the organization. Put another way, the organization controls the interpretation of the data source, not simply those within the usage context. Organizational coding and documentation standards would, if considered relevant to the usage context, be classified as an organizational data source.

External data sources refer to data sources for which an interpretation is imposed outside the organization. For example, an ISO standard will be broadly interpreted within a community. However, a document describing an organization’s interpretation of that standard will be an organizational data source. Table 3 presents examples from each type of data source.

It is worth commenting that a valuable contextual data source will be the developers’ first hand experience of similar development tasks to the one at hand. However, it is potentially dangerous to rule out any type of data source in advance, as what might appear irrelevant during the early phases of analysis might later be shown to be fundamentally important for continued analysis. It is by experience and sensitivity to the usage context that an analyst might successfully identify as relevant data sources that otherwise would not have been considered.

Table 3. Examples of data sources

<table><tr><td>Type of data source</td><td>Examples</td></tr><tr><td>Contextual data</td><td>Primary interview data obtained from direct stakeholders within the context for the analysisPrevious experiences of CASE (written and ‘living’ through personnel within the context for the analysis) in general and/or of specific productsInternal documents (notes, annotations, etc.) concerning the current evaluationPrevious systems (including previous CASE technology) and prototypes being developed and/or maintained within the context for the analysis</td></tr><tr><td>Organizational data</td><td>A company statement/policy saying that UML shall be used for the development of all new systemsA company statement/policy saying that the goal for our organization is that we should follow all IT standardsPrevious experiences of CASE (in general and/or of specific products) within other departments</td></tr><tr><td>External data</td><td>Published reports, books and vendor documentationISO standardsCASE-tool user groups and other interest groupsCASE-tool characteristics obtained from other evaluation methods and through living personnel (e.g. external consultants)General: tutorials, workshops, seminars, exhibitions, vendor demonstrations, etc.Electronic information sources (e.g. web sites)</td></tr></table>

## EVALUATION FRAMEWORKS IN 2G

In applying 2G, an organization is attempting to generate a framework for an evaluation of CASE tools as they might satisfy organizational and application requirements. The framework will consist of a set of interrelated concepts, together with their indicators, representing identified needs and their associations. Note that concepts can be associated as alternatives. For example, in one field study Delphi™ code generation was initially seen as essential. After further discussion, it was concluded that Delphi-compatible component generation was a satisfactory alternative. It is also clear that associations can be qualified, for example, as necessary or simply useful. Such semantic enrichments give structure to subsequent decision procedures (for a full evaluation) based on the framework.

In order to convey a common understanding among the stakeholders, the concepts within the framework should be fully characterized, for example, through rich descriptions as in Table 2.

## Strategic evaluation framework

A strategic evaluation framework aims to facilitate stakeholder learning. Its content should be a reference point for what an ideal CASE tool should consist of within the defined usage context, taking a long-term perspective. It should therefore not be unduly influenced by limitations in current technology. There is no goal of arriving at a ‘generalized’ strategic evaluation framework, that might be broadly applicable to other contextual settings.

Over time, stakeholders are likely to strengthen their understanding of their own long-term needs, something likely to lead to expansion and/or refinement of the framework.

## Pragmatic evaluation framework

A pragmatic evaluation framework is tuned to the evaluation at hand. Its content should be strongly informed by the capabilities of currently available state-of-the-art CASE tools, and will therefore contain a set of characteristics against which the CASE-tool products should be evaluated. In other words, its content will reflect what are currently realistic goals for a CASEtool product, and it is this framework that will be used in an evaluation of currently available tools.

The pragmatic evaluation framework is always a version of the strategic evaluation framework that has been adapted through consideration of current technology. It must be a full version, in the sense that there must be a total mapping of concepts from the strategic to the pragmatic framework. Differences may be in level of abstraction, in which a general concept in the strategic framework may be replaced by one or more functional concepts based on current tools. They may also be more fundamental, in which an insupportable characteristic is replaced by a related, but less demanding requirement.

## CONCEPT DEVELOPMENT IN 2G

## Initiating an application of 2G

In order to apply 2G, a method user must first identify a context for the study and those stakeholders who will contribute initially to characterizing that context. For example, a usage context might be a division within an IS development organization in which a group of developers have responsibility for a specific phase in the IS life cycle. The context will be more clearly defined, and relevant stakeholders identified, as the study continues.

Initial data can be sought through consultation with identified stakeholders, and interviews arranged with them. The method does not require (or even recommend) exhaustive data collection prior to analysis. This means that the data collection process will only to a limited extent be planned in advance; the issues which emerge as important during analysis will guide further data collection. For initial data collection contextual relevance is paramount, so contextual data sources should be preferred initially.

## Interviews in phase 1

Many different styles of interview can be utilized when applying 2G. However, its qualitative nature suggests that it may be beneficial to use an open interview technique for at least some of the sessions, especially in the early stages of a study. In such an interview, the interviewer does not use a fixed agenda but directs the session according to a respondent’s replies, and to a large extent keeps the initiative with the respondent. A detailed discussion of interview techniques is beyond the scope of this paper.

We have found that one consequence of using open interviews for data collection is that interview sessions can vary significantly, both in terms of scope and style. For example, when for some reason a session is in danger of losing its focus, it may be useful to change the level of abstraction or overtly redirect the focus. From experience, we recommend one interviewee in each open session in the early stages of an application of this phase of 2G. However, especially during later stages when an evaluation framework has been developed, it is advisable to use group interview sessions also.

One situation calling for group interviews concerns the presence of problematic indicators. On a number of occasions, we have found that a concept cannot be given a concise interpretation because of conflict between, or lack of clarity in, indicators. In one company, there seemed to be several conflicting views of company policy on, and therefore requirements for, trigger support in SQL. Similarly, there were differing opinions on whether CASE tools should enforce a strict use of UML notation and associated methods, or whether notification of ‘deviation’ would be better in the context. Such conflicts are best pursued, at least initially, within a group session of involved stakeholders.

## Other data sources in phase 1

Observational data are not enough; the analyst must reach deeper than this allows. There are a number of other contextual data sources which can be used in phase 1 other than open interviews (see Table 3), including participant observation by the method user. Such participation within a company can bring with it open access to a rich variety of primary sources, and as importantly informal access to stakeholders for interpretation of sources and culture. We have also observed that this can have a positive effect (in terms of trust and familiarity with the setting) on the open interview sessions, as the method user becomes accepted within the organization.

With respect to the use of non-contextual data in the analysis, there is a potential problem with respect to data quality. This is particularly true for data sources that are ‘conceptually distant’ from the contextual setting, for example, CASE evaluations performed in other divisions of the organization. If the context in which such data have been collected is unclear, its relevance and interpretation in the current context will also be unclear.

There is an obvious risk with the use of external data sources, for example, sets of a priori characteristics. Such sets must be interpreted within the context. For example, use of (parts of) the concept<sup>7</sup> framework within ISO 14102 may influence the development of the initial evaluation framework, but only with appropriate interpretation.

## Developing a strategic evaluation framework

Soon after initiating a study, and once some data have been obtained, the method user must start to look for and compare indicators (see Table 1) of what might constitute important concepts. As the study continues, the method user aims to obtain additional data, comparing new indicators with existing ones in order to strengthen the fit between the data and the content of the framework.

New indicators might either strengthen an emerging concept, or imply the need for reconsidering the framework. For example, if new indicators are entirely consistent with the previously available indicators for an emerging concept, it will be strengthened. However, if a close fit is not evident, additional data must be collected and analysed. A refined and changed framework typically emerges. It should be noted that there may be many indicators in one data source, and each indicator may be associated with many concepts.

An example of this can be found in a session taken from a field study, which involved the analyst and a stakeholder. It addressed a specific functionality (referred to as ‘live data’ in design mode) in the development environment explored. During a session in front of the screen when analysing a specific prototype, the stakeholder expressed the need for ‘the use of live data in design mode', which was incorporated into the framework as an indicator fol the emerging concept validation support. However, the flow of the discussion also established this as an indicator for a different concept – traceability. Hence, this particular indicator became linked with two different concepts. The association with traceability was reinforced when the interviewee mentioned a different tool supporting the same idea but referred to differently.

The goal for this process of constant comparison of indicators and emerging concepts is ultimately to sharpen the fit between the underlying data (as identified by a set of indicators in the data) and an emerging concept. Early in the process, when there is little data available and only rather vague support for an emerging concept, the process is primarily concerned with a constant comparison of indicators. Later, as more indicators are obtained, the balance will gradually change to comparing indicators with evolving concepts.

As this process continues, evidence from the data for each emerging concept will be strengthened. Sometimes, as new indicators in the data are identified, concepts that initially appeared stable might be reconsidered (and recoded) as, perhaps, a subconcept (or property) of another concept. It is important to emphasize that all concepts in the strategic evaluation framework must be traceable to (indicators in) data that have been obtained from the contextual setting. The concepts that are evolved through this process will be of importance in the contextual setting in which 2G is being applied.

Once a set of concepts is considered relatively stable, the emphasis will gradually shift from concept development to concept structuring. This may involve semantic structuring, for example, linking concepts to categories, as shown in Figure 1. It will involve coding value judgements to guide the later full evaluation. The set of concepts will evolve into a whole structure of related concepts, referred to as an evaluation framework.

## Initiating an application of phase 2

Phase 2 in 2G consists of a technological exploration of (a set of) specific ‘state-of-the art’ CASE tools. This exploration is to be undertaken in the light of the content of the evaluation framework that has been developed in phase 1. An important motivation for a distinguished second phase in 2G is that it explicitly incorporates a technology-led investigation of need. As CASE tools are very complex IT products, it is very difficult to identify a set of relevant (and realistic) requirements for an evaluation by only considering organizational issues.

When phase 2 is initiated in 2G, there will always exist a preliminary strategic evaluation framework. This will constitute a starting point from which the technological exploration can start. On the first initiation of phase 2, the pragmatic framework will be initialized as a copy of the strategic framework.

As with data sources in phase 1, it is not recommended that an exhaustive set of CASE tools be identified before applving method phase 2. As its primary role is to ground the content of the evaluation framework in currently available state-of-the-art technology, it is not a problem to use a range of tools, including those likely to be beyond expected budget. However, it is advisable to explicitly include tools thought to be real contenders; the final framework is, after all, intended to discriminate between selected contenders in a full evaluation, and so should be grounded in a reachable technology. The tools used in phase 2 may differ from one iteration of the process to the next.

## Tool exploration in phase 2

When exploring CASE tools, it is advisable to use data from the usage context in order to make the interpretation for the stakeholder easier. Also, for issues to be properly tested, there is a need to ensure that data sets are of representative size and complexity. This is necessary in order to explore scalability appropriately.

The method user may initially undertake a general tool exploration (‘brainstorming’). This can be seen as a strategy to assist in the development and refinement of the evaluation framework, and may deliver insights relating to currently supported functionality. This will include functionality asked for in the evaluation framework, but also what the method user may see, based on acquired knowledge of the context, as other potentially relevant functionality. These insights, when considered as data, can later be used in a further round of open interviews. In one field study, features for active directories and database migration were considered potentially relevant after one such tool exploration. They were therefore raised in subsequent open interviews.

When considering the strategic evaluation framework, concept interpretation may be found to be somewhat unclear. This may indicate areas in need of further elaboration by stakeholders.

Tools may be found to support features associated with many of the concepts in an evaluation framework. However, requirements may be partially supported, or even unsupported in the way envisaged by stakeholders. In each of these cases, the method user should search for alternative approaches which may potentially be of interest in further exploring such requirements. Again, such information should be used as data for subsequent open interviews, and may or may not be found to be relevant. A special case of this is where different tools offer different ways of meeting, or partially meeting a requirement. In such situations, extra information can be gleaned on potential refinement of the pragmatic framework; this will initiate discussions with stakeholders, and is one motivation for phase 2 taking place in the usage context. This was the situation in the example cited earlier, where annotations were considered for supporting traceability, but the issue of their treatment as first class was an important discriminator.

## Developing a pragmatic evaluation framework

It is important, we claim, that as the strategic evaluation framework represents organizational need, it should in some sense guide the technological exploration. This is to ensure a focus on issues that have emerged from the usage context. However, there is a question of balance here. If the evaluation framework is unquestioningly used to set the agenda, this might limit the possible findings, and thereby decrease the value of this phase. On the other hand, if the evaluation framework is kept too much in the background, a technological exploration will be very free and unconstrained by stakeholder need. This may result in important issues not being explored in enough depth. This, in turn, might lead to a loss of stakeholder interest in the next iteration; stakeholders will be confronted with a large amount of data that they do not consider relevant, and at the same time also find that issues which they have previously raised as important (perhaps in previous interviews) have not been thoroughly explored and investigated on the tools.

It is important to emphasize that when a state-of-the-art CASE tool is explored in phase 2, the goal is not to evaluate the specific tool. Instead, one should think of this phase as a very special form of data collection that is technology driven instead of context driven. However, this is not to say that the exploration of a tool will not involve some testing of it: there may be testing of specific functionality, which typically can be undertaken in a very systematic and rigorous way.

## Iteration

As 2G is iterative, and a typical application of it implies that each phase will be undertaken several times, there are decisions to be made regarding when to move between phases. The method user will be in the best position to judge stakeholder reaction, and so make such decisions. Because of the qualitative nature of 2G, it is not possible to predetermine an appropriate time for the transition between phases. Instead, judgement must be based on the relative stability of the two frameworks, and on maintaining stakeholder confidence.

There is organizational overhead associated with each iteration, and delta improvements are likely to undermine stakeholder confidence. For example, open interviews are expensive for both method user and stakeholders. A transition from phase 2 back to phase 1 should only be undertaken if it is felt likely that interpreting new technical data will lead to significant change to the strategic evaluation framework.

## Deciding to move to a full evaluation

At some stage, the method user will judge that the frameworks have stabilized, and that further iterations of the method phases would prove counter-productive. A decision must then be made concerning whether to proceed with a full evaluation.

This decision is, obviously, in the hands of stakeholders. If a decision is made to proceed, it is the pragmatic evaluation framework which will be used in the evaluation.

## IMPLICATIONS FOR PRACTICE

There is a need for managers to take a systematic approach to the important and inherently complex task of CASE-tool evaluation. A necessary prerequisite for a pre-usage evaluation is a suitable evaluation framework, tuned both to the technology of available CASE products and the very context-specific needs and expectations of stakeholders. In developing such a framework, a manager confronts a number of problems.

If a published framework is to be used as a starting point, then it must first be interpreted – the concepts used in the framework, and their associations, are unlikely to match those used and understood in the organizational context in which any tool is to be used. Interpreting a published framework is a difficult task in its own right. Even when this has been achieved, some way is required of modifying the framework to reflect only what is relevant in the context. Relevance must be achieved not simply through removing unwanted concepts from the framework and adding new ones. A more complex process of concept alignment is implied, in which interrelated concepts are refined and substituted with more relevant (possibly more modest) demands. Concept alignment and maintenance of associations within a framework both require a systematic approach. Failing to fully account for tool differences and stakeholder needs may lead to non-discriminatory frameworks, and hence to poor decisions when a full evaluation is undertaken. This in turn would lead to ineffective tool use.

Even if a good framework is achieved, it will reflect only current needs and current technology and so only be relevant to a current evaluation activity. It will be difficult to use it to inform management of organizational need, as it will be strongly coloured by stakeholder views of CASE technology at a particular point in time.

If a general, context-sensitive requirements method were used (e.g. GIST, Hughes, 1998), then it should be possible to develop a framework which is organizationally relevant. It would be similar to an application of phase 1 of the proposed method using a refined method, but without the goal of associating concepts for decision-making. Also, relevance would not be informed by current technology, and the opportunity to gain ideas from a curiosity-led exploration of tools in context would be missing. A resulting framework would therefore lack discrimination with respect to current technology, and the framework would not fully inform a full evaluation.

The 2G method presented here is offered as one systematic method which addresses all of the above issues. However, we believe that evolving evaluation frameworks in 2G should not be seen as useful only for tool evaluation, but as important resources for internal reviews and discussions. For example, identifying conflicting indicators and ill-specified concepts within a framework is not simply useful in directing further iterations of 2G, highlighting areas of the framework in need of clarification. It may also play a useful role in management feedback. For example, the trigger example stemmed from differing interpretations of a management policy on the use of triggers in databases used to support products. Such a set of indicators may be useful in understanding how a policy is being interpreted within an organization, perhaps indicating areas for clarification – or even policy change.

## CONCLUSIONS

In this paper, we have presented 2G, a method which aims to address identified problems with respect to the development of pre-usage evaluation frameworks. Two convictions underlie the development of the method. The first is that an effective evaluation framework is of fundamen tal importance to, and a necessary prerequisite for, the success of any evaluation effort. The second is that there exists a tension between long- and short-term organizational requirements, which must be acknowledged. We consider it important that the method has been evolved through a number of genuine applications in IS development company contexts (Lundell et al., 1999; Lundell & Lings, 1999; 2000; Lundell, 2001; Rehbinder et al., 2001; 2002).

The method presented differs from other systematic methods for developing a pre-usage CASE-tool evaluation framework in being ‘data driven’ rather than ‘concept driven’. In particular, framework content and structure both evolve during analysis, rather than being defined a priori.

For pre-usage evaluation of CASE tools, 2G is unique in specifically addressing the difficult task of integrating ‘softer’ social and organizational requirements with the more technical requirements against which CASE technology is to be evaluated. It uses representative, stateof-the-art technology to both inform and constrain framework development, distinguishing long-term requirements (represented in a strategic evaluation framework) from short-term contingency (represented in a pragmatic evaluation framework, always a version of the former).

There are other motivations for incorporating a distinguished second phase in the method. Somewhat simplified, we have experienced (both in our own applications, and from analysis of other method users’ applications of 2G) at least three advantages (not mutually exclusive) of having phase 2.

Firstly, it helps in improving precision in the content of the framework, by bringing substance to what may otherwise be rather abstract ideas of need and expectation. By, for example, observing a CASE tool in action, using real contextual data, it is typically easier to understand and appreciate what the abstract ideas really mean. It is also more likely to genuinely engage the participating stakeholders.

Secondly, by using and observing the behaviour of CASE tools in the usage context, it might be possible to gain new insights into the way in which a tool can be utilized. Somewhat simplified, what is not thought of is not asked for.

Thirdly, if the framework implies requirements which are far from satisfiable by available CASE tools, it might be wise to raise the question: ‘are we asking too much of the tools that are on the marketplace today?’ It would be worthwhile identifying alternatives at this point rather than planning a full evaluation in which functionality is sought that it is known beforehand will not be found. In the latter case, the evaluation framework would be less discriminating than is desirable. There may be alternative functionality within today’s tools that (partly or indirectly) satisfies the need, perhaps using a different strategy. Incorporating concepts related to these may make the framework more discriminating, and should be raised as an issue to be addressed by stakeholders.

There are still a number of open issues which we are hoping to address in ongoing work.

The special nature of the 2G method would place heavy demands on current qualitative tools, and it is an open question how well any existing tool will be able to meet these demands. We would like to explore how tool support might assist in issues related to scalability as frameworks increase in size and structural complexity.

The real value of the strategic framework is likely to come when the method is applied over a long time span. In particular, currency should be maintained so that it continues to reflect organizational need. It can be used as a resource, to assist in organizational learning, but also as a basis for initiating a further evaluation – perhaps because of technology change, or simply new product availability. A longitudinal study would allow exploration of these issues.

Although 2G evolved specifically with respect to CASE-tool evaluation, there is no reason to believe that it is not more broadly applicable. Indeed, positive experience of its use in developing a framework for web server evaluation has been reported (Lundell & Lings, 1999). In essence, 2G is likely to be of use in any situation in which a technical product is to be evaluated prior to deployment in a specified context, and examples of the product are to be used in informing that evaluation.

## ACKNOWLEDGEMENTS

The authors would like to thank the many people who, through participation in various roles in the field studies, have contributed to the development of the 2G method. We are also indebted to the companies which facilitated these studies. Finally, we would like to thank the anonymous referees for their very helpful reviews of an earlier draft of this paper.

## REFERENCES

Antonakopoulos, T., Agavanakis, K. & Makios, V. (1995) CASE tools evaluation: an automatic process based on fuzzy sets theory. In: Proceedings: Sixth IEEE International Workshop on Rapid System Prototyping, Lauwereine, R. (ed.), pp. 140–146. IEEE Computer Society Press, New York, NY, USA.

Antoniol, G., La Commare, G., Giraudo, G. & Tonella, P. (1999) Effective feature analysis for tool selection. In: International Conference on Product Focused Software Process Improvement, Oivo, M. & Kuvaja, P. (eds), pp. 103–117. VTT Electronics, University of Oulu, VTT Symposium 195, Technical Research Centre of Finland (VTT), Finland.

Ashry, N.Y. & Taylor, W.A. (2000) Requirements analysis as innovation diffusion: a proposed requirements analysis strategy for the development of an integrated hospita information support system. Proceedings of the 33rd Hawaii International Conference on System Sciences, pp. 1699–1708. IEEE Computer Society Press, Los Alamitos CAUSA

Barker, R. (1990) CASE Method: Entity Relationship Modelling. Addison-Wesley Publishing Company/Oracle Corporation, UK Limited, Wokingham, UK.

Beckworth G (1993) Selection Criteria for CASE Tools Department of Computing and Mathematics, Deakin University, Australia, TR C93/25.

Bell, R. (1994) Choosing tools for analysis and design. IEEE Software, 11, 121–125.

Brown, A.W. & Wallnau, K.C. (1996) Framework for eval uating software technology. IEEE Software, 13, 39–49.

Bubenko, J. Jr (1993) Extending the scope of information modelling. Invited paper. In: Proceedings of the Fourth International Workshop on the Deductive Approach to Information Systems and Databases, Olivé, A. (ed.), pp. 73–97. LSI/93–25-R. Departament de Llenguatges Sistemes Informatics. Universitat Politecnica de Catalu nya, Catalonia.

Butler, T. & Fitzgerald, B. (1999) Unpacking the systems development process: an empirical application of the CSF concept in a research context. Journal of Strategic Information Systems, 8, 351–371.

Calloway, L.J. & Ariav, G. (1991) Developing and using a qualitative methodology to study relationships among designers and tools. In: Information Systems Research: Contemporary Approach and Emergent Traditions – Proceedings of the IFIP TC8/WG 8.2 Working Conference on the Information Systems Research Arena of the 90’s Challenges, Perceptions, and Alternative Approaches, Nissen, H.-E., Klein, H.K. & Hirschheim, R. (eds) pp 175–193 North-Holland Amsterdam

Calloway, L.J. & Ariav, G. (1995) Designing with dialogue charts: a qualitative content analysis of end-user design-

ers’ experiences with a software engineering design tool. Information Systems Journal, 5, 75–103.

Calzolari, F. & Cozzio, E. (1999) Improving the requirements definition: the RESPECT project. In: International Conference on Product Focused Software Process Improvement, Oivo, M. & Kuvaja, P. (eds), pp. 575–588. VTT Electronics, University of Oulu, VTT Symposium 195, Technical Research Centre of Finland (VTT), Finland.

Cronholm, S. (1995) Why CASE tools in information systems development? – an empirical study concerning motives for investing in CASE tools. In: Proceedings of the 18th Information Systems Research Seminar in Scandinavia: IRIS 18 – ‘Design in Context’, Dahlbom, B., Kämmerer, F., Ljungberg, F., Stage, J. & Sörensen, C. (eds), pp. 132–144. Gothenburg Studies in Informatics, Report 7.

Cronholm, S. (1998) Metodverktyg och användbarhet – en studie av datorstödd metodbaserad systemutveckling. PhD thesis. Department of Computer and Information Science, Linköping University, Linköping, Sweden [in Swedish].

Daneva, M. (1997) Selecting the best-in-class CASE tool for software process improvement. 7th International Conference on Software Quality (7ICSQ), pp. 93–104. Montgomery, Alabama, USA.

Daneva, M. & Terzieva, R. (1996) Assessing the potentials of CASE-tools in software process improvement: a benchmarking study. In: Proceedings of the Fourth International Symposium on Assessment of Software Tools, Frieder, O. & Wigglesworth, J. (eds), pp. 104– 108. IEEE Computer Society Press, Los Alamitos, CA, USA.

Dixon, R.L. (1992) Winning with CASE: Managing Modern Software Development. McGraw-Hill, New York.

Galal, G.H. & Paul, R.J. (1999) A qualitative scenario approach to managing evolving requirements. Requirements Engineering, 4, 92–102.

Glaser, B.G. (1978) Advances in the Methodology of Grounded Theory: Theoretical Sensitivity. The Sociology Press, Mill Valley, CA.

Glaser, B.G. (1992) Basics of Grounded Theory Analysis. Sociology Press, Mill Valley, CA.

Glaser, B.G. (1998) Doing Grounded Theory: Issues and Discussions. Sociology Press, Mill Valley, CA.

Glaser, B.G. & Strauss, A.L. (1967) The Discovery of Grounded Theory: Strategies for Qualitative Research. Weidenfeld and Nicolson, London.

Glass, R.L. (1999) The loyal opposition: of Open Source, Linux, and Hype. IEEE Software, 16, 126–128.

Goldkuhl, G., Cronholm, S. & Krysander, C. (1992) Adaption of case tools to different systems development methods, In: Proceedings of the 15th IRIS – Part I: Information Systems Research Seminar in Scandinavia, Bjerknes, G., Brattesteig, T. & Karlheinz, K. (eds), pp. 142–156. Department of Informatics, University of Oslo, Oslo.

Henderson, J.C. & Cooprider, J.G. (1990) Dimensions of I/ S planning and design aids: a functional model of CASE technology. Information Systems Research, 1, 227–254.

Howcroft, D. & Hughes, J. (1999) Grounded Theory: I mentioned it once but I think I got away with it. In: Information Systems – the Next Generation: Proceedings of the 4th UKAIS Conference, Brooks, L. & Kimble, C. (eds), pp. 129–141. McGraw-Hill, Maidenhead.

Huff, C., Smith, D., Stepien-Oakes, K., Morris, E. & Zarrella, P. (eds) (1992) Proceedings of the CASE Adoption Workshop. Technical Report, CMU/SEI-91-TR-14. Software Engineering Institute, Carnegie Mellon University, Pittsburgh, PA.

Hughes, J. (1998) The development of the GIST (Ground ing Information SysTems) methodology: determining situated requirements in information systems analysis. PhD thesis, T.I.M.E. Research Institute, Information Sys tems Research Centre, Department of Computer and Mathematical Science, University of Salford, Salford, UK.

Hughes, J. & Wood-Harper, T. (1999) Addressing organizational issues in requirements engineering practice: lessons from action cases. Australian Journal of Information Systems, 7, (Special Edition – Requirements Engineering) 64–74.

IEEE (1992) IEEE Recommended Practice for the Evaluation and Selection of CASE Tools. IEEE Std 1209- 1992, 13 December, IEEE Standards Board, New York.

IEEE. (1998) Information technology – Guideline for the Evaluation and Selection of CASE Tools. IEEE Std 1462-1998, 19 March, IEEE-SA Standards Board, New York.

Iivari, J. & Lyytinen, K. (1999) Research on information systems development in Scandinavia: unity in plurality. In: Rethinking Management Information Systems: an Interdisciplinary Perspective, Galliers, R.D. & Currie, W.L. (eds), pp. 57–102. Oxford University Press, Oxford.

Irani, Z. & Love, P.E.D. (2001) Developing a frame of ref erence for ex-ante IT/IS investment evaluation. European Journal of Information Systems, 10, 183–188.

ISO (1995) Information Technology – Guideline for the Evaluation and Selection of CASE Tools, ISO/IEC JTC1/ SC7/WG4, ISO/IEC 14102:1995(E).

IVF (1997) Europadag om SPI på IVF. Institutet för Verkstadsteknisk forskning, Gothenburg, Sweden, 2 June 1997, Seminar, [in Swedish].

Jankowski, D.J. (1995) CASE tool selection: using methodology support to choose the right tool for the job. Journal of Systems Management, 46, 20–27.

Jankowski, D. (1997) Computer-aided software systems. Empirical Software Engineering: an International Journal, 2, 11–38.

Juric, R. & Kuljis, J. (1999) Building an evaluation instrument for OO CASE tool assessment of unified modelling language support. Proceedings of the Thirty-second Annual Hawaii International Conference on System Science [CD-ROM], 10 pp. IEEE Computer Society Press, Los Alamitos, CA, USA.

Kaipala, J. (1997) Augmenting CASE tools with hypertext: desired functionality and implementation issues. In: Advanced Information Systems Engineering: 9th International Conference, CAiSE ‘97, Olivé, A. & Pastor, J.A. (eds), pp. 217–230. Springer, Berlin.

Kitchenham, B.A. & Jones, L. (1997a) Evaluating software engineering methods and tool – part 5: the influence of human factors. Software Engineering Notes, 22, 13–15.

Kitchenham, B.A. & Jones, L. (1997b) Evaluating software engineering methods and tool – part 6: identifying and scoring features. Software Engineering Notes, 22, 16– 18.

Kitchenham, B., Linkman, S. & Law, D. (1997) DESMET: a methodology for evaluating software engineering methods and tools. Computing and Contrological Engineering Journal, 8, 120–126.

Kudrass, T., Lehmbach, M. & Buchmann, A. (1996) Toolbased re-engineering of a legacy MIS: an experience report. In: Advanced Information Systems Engineering: 8th International Conference, CAiSE ‘96, Constantopoulos, P., Mylopoulos, J. & Vassiliou, Y. (eds), pp. 116– 135. Springer, Berlin.

Le Blanc, L. & Korn, W.M. (1992) A structured approach to the evaluation and selection of CASE tools. In: Proceedings of the 1992 ACM/SIGAPP Symposium on Applied Computing (Vol. II): Technological Challenges of the 1990’s, Berghel, H. (ed.), pp. 1064–1069. Kansas City, MO.

Le Blanc, L.A. & Korn, W.M. (1994) A phased approach to the evaluation and selection of CASE tools. Information and Software Technology, 36, 267–273.

Lundell, B. (2001) Systematic method support for CASEtool evaluation. PhD thesis. University of Exeter, UK.

Lundell, B. & Lings, B. (1999) Validating transfer of a method for the development of evaluation frameworks.

In: Sixth European Conference on the Evaluation of Information Technology (ECEIT’99), Brown, A. & Remenyi, D. (eds), pp. 255–263. Brunel University, Uxbridge, UK.

Lundell, B. & Lings, B. (2000) On method support for developing pre-usage evaluation frameworks for CASE tools. In: Systems Development Methods for Databases, Enterprise Modeling – and Workflow Management, Wojtkowski, W., Wojtkowski, W.G., Wrycza, S. & Zupancic, J. (eds), pp. 169–182. Kluwer Academic/Plenum Publishers, New York.

Lundell, B. & Lings, B. (2002) Comments on ISO 14102: the standard for CASE-tool evaluation. Computer Standards and Interfaces, 24, 381–388

Lundell, B., Lings, B. & Gustafsson, P.-O. (1999) Method support for developing evaluation frameworks for CASE tool evaluation. In: Managing Information Technology Resources in Organizations in the Next Millennium: 1999 Information Resources Management Association International Conference – Track: Computer-Aided Software Engineering Tools, Khosrowpour, M. (ed.), pp. 350–358. IDEA Group Publishing, Hershey.

McComb, M.E. (1994) CASE tools implementation at Amtrak – lessons almost learned. Journal of Systems Management, 45, 16–20.

Martin, M.P. (1995) The case against CASE. Journal of Systems Management, 46, 54–57.

Melia, K.M. (1996) Rediscovering Glaser. Qualitative Health Research, 6, 368–378.

Moriarty, T. (1995) Pure gold found in Silverrun. Database Programming and Design, 8, 76–79.

Moriarty, T. (1998) Searching for the right data modeling tool. DM Review, 8, 74–76.

Mosley, V. (1992) How to assess tools efficiently and quantitatively. IEEE Software, 9, 29–32.

Orlikowski, W.J. (1993) CASE tools as organizationa change: investigation incremental and radical changes in systems development. MIS Quarterly, 17, 309–340.

Ovum (1993) Ovum Evaluated: Case Products. Ovum, London.

Palvia, P. (1992) A comprehensive model and evaluation of the software engineering environment. In: Emerging Information Technology for Competitive Advantage and Economic Development: Proceedings of the 3rd Information Resources Management Association International Conference, Khospowpour, M. (ed.), pp. 302–307. IDEA Group Publishing, Hershey.

Pidgeon, N.F., Turner, B.A. & Blockley, D.I. (1991) The use of Grounded Theory for conceptual analysis in knowl-

edge elicitation. International Journal of Man-Machine Studies, 35, 151–173.

du Plessis, A.L. (1993) A method for CASE tool evaluation. Information and Management, 25, 93–102.

Post, G. & Kagan, A. (2001) User requirements for OO CASE tools. Information and Software Technology, 43, 509–517.

Poston, R.M. & Sexton, M.P. (1992) Evaluating and select ing testing tools. IEEE Software, 9, 31–40.

Powell, A., Vickers, A., Williams, E. & Cooke, B. (1997) A practical strategy for the evaluation of software tools. In: Method Engineering: Principles of Method Construction and Tool Support, Brinkkemper, S., Lyytinen, K. & Welke, R.J. (eds), pp. 165–185. Chapman & Hall, London.

Prather, B. (1993) Critical failure points of CASE tool evaluation and selection. In: Proceedings of the Sixth International Workshop on Computer-Aided Software Engineering: CASE ’93, Lee, H.-Y., Reid, T.F. & Jarzabek, S. (eds), pp. 60–63. IEEE Computer Society Press, Los Alamitos, CA, USA.

Pries-Heje, J. (1991) Three barriers for continuous use of computer-based tools – a Grounded Theory. In: Proceedings of the 14th IRIS: Revised Papers of the 14th Information Systems Research Seminar in Scandinavia, Ivanov, K. (ed.), pp. 171–181. Research Reports in Information Processing and Computer Science, No. 16, Uni versity of Umeå, Sweden.

Pries-Heje, J. (1992) Three barriers for continuing use of computer-based tools in information systems development: a Grounded Theory approach. Scandinavian Journal of Information Systems. 4119–136

Rahim, M.M., Khan, M.K. & Selamat, M.H. (1997) Adoption versus abandonment of CASE tools: lessons from two organizations. Information Technology and People, 10, 316–329.

van Reeken, A.J. & Trienekens, J.J.M. (1992) The practical importance of methods and case tools: results of empirical research. MERIT 92-015. Maastricht Economic Research Institute on Innovation and Technology, 19 pp. University of Limburg, Maastricht, Netherlands.

Rehbinder, A., Lings, B., Lundell, B., Burman, R. & Nilsson, A. (2001) Observations from a field study on developing a framework for pre-usage evaluation of CASEtools. In: New Directions in Information Systems Development (IFIP WG 8.2 Conference 2001), Russo, N.L., Fitzgerald, B. & DeGross, J.I. (eds), pp. 211–220. Kluwer, Boston, MA.

Rehbinder, A., Lings, B., Lundell, B., Burman, R. & Nilsson, A. (2002) Developing a framework for pre-usage evaluations of CASE-tools: a case-study. In: New Per-

spectives on Information Systems Development: Theory, Methods and Practice – the Tenth International Conference: Information Systems Development ISD2001. Harindranath, G., Rosenberg, D., Sillince, J.A.A., Wojt kowski, W., Wojtkowski, W.G., Wrycza, S. & Zupancic, J. (eds), pp. 519–534. Kluwer Academic/Plenum Publishers, New York.

Reiner, D. (1992) Database design tools. In: Conceptual Database Design: an Entity-Relationship Approach, Batini, C., Ceri, S. & Navathe, S.B (eds), pp. 411–454. Benjamin/Cummings Publishing Company, Redwood City, CA.

SEI (1995) CASE Environment Project Description, Slide Presentation January 1995. Software Engineering Insti tute, Carnegie Mellon University, Pittsburgh. URL http:// www.sei.cmu.edu/legacy/case/case\_desc.ps.Z (accessed 26 October 1998).

Senn, J.A. & Wynekoop, J.L. (1995) The other side of CASE implementation: best practices for success. Infor mation Systems Management, 12, 7–14.

Shafer, L.I. & Shafer, D.F. (1993) Establishing a CASE tool box, IS steps to selecting CASE tools. Systems Information Management, 10, 15–23.

Sharma, S. & Rai, A. (2000) CASE deployment in IS orga nizations. Communications of the ACM 43 80–88

Skramstad, T. & Khan, M.K. (1992) Assessment of reverse engineering tools: a MECCA approach. Proceedings 2nd Symposium on Assessment of Quality Software Development Tools, pp. 120–126. IEEE Computer Soci ety Press, Los Alamitos, CA, USA.

Sodi, J. (1991) Software Engineering Methods, Management, and CASE Tools. TAB Professional and Reference Books, Blue Ridge Summit, PA.

Starrin, B., Dahlgren, L., Larsson, G. & Styrborn, S. (1997) Along the Path of Discovery: Qualitative Methods and Grounded Theory. Studentlitteratur, Lund.

Starrin, B., Larsson, G., Dahlgren, L. & Styrborn, S. (1991) Från upptäckt till presentation. Studentlitteratur, Lund [in Swedish].

Topper, A. (1991) Evaluating CASE tools: guidelines fo comparison. American Programmer, 4, 12–20.

Urquhart, C. (1997) Exploring analyst-client communication: using Grounded Theory techniques to investigate interaction in informal requirements gathering. In: Information Systems and Qualitative Research, Lee, A.S., Liebenau, J. & DeGross, J.I. (eds), pp. 149–181. Chap man & Hall London

Vessey, I., Jarvenpaa, S.L. & Tractinsky, N. (1992) Evaluation of vendor products: CASE tools as methodology companions. Communication of the ACM, 35, 90–105.

Vessey, I. & Sravanapudi, A.P. (1995) CASE tools as collaborative support technologies. Communications of the ACM, 38, 83–95.

Vollman, T. (1994) Standards support for software too quality assessment. In: Proceedings: Third Symposium on Assessment of Quality Software Development Tools, Nahouraii, E. (ed.), pp. 29–38. IEEE Computer Society Press, Los Alamitos, CA, USA.

Zucconi, L. (1989) Selecting a CASE tool. ACM SIGSOFT: Software Engineering Notes, 14, 42–44.

Zuurbier, J., Brinkkemper, J., Offereins, M. & Odding, N. (1994) Towards a design methodology for decision support systems. In: Proceedings of the Twenty-seventh Annual Hawaii International Conference on System Sciences: Volume I – Architecture, Mudge, T. & Shriver, B.D. (eds), pp. 25–32. IEEE Computer Science Press, Los Alamitos, CA, USA.

## Biographies

Björn Lundell was awarded an MSc (1991) in Computer Science from the University of Skövde, Sweden, where he is currently a Lecturer. He successfully defended his doctoral thesis, ‘Systematic method support for CASE-too evaluation’, after completing his studies at the University of Exeter, UK (2001). His current research activities centre on CASE technology and associated method support for CASE-tool evaluation. His research is published in a variety of international conferences and journals. He has a general interest in qualitative methods and his research centres on the issues: database modelling, CASE technology, CASE-tool evaluation and development, and Grounded Theory.

Brian Lings was awarded a doctorate in Computer Science from the University of East Anglia in 1975. After a number of years at the University of Queensland, Australia, he joined the Department of Computer Science, now within the School of Engineering and Computer Science at the University of Exeter in 1982. His research interests concern the development of user-centred tools and methods for the effective exploitation of database technology in complex information sharing domains. His recent publications have centred on the areas of CASE-tool evaluation and development active database technology and data warehouse maintenance. Much of his work is conducted in collaboration with colleagues at the University of Skövde, Sweden.
