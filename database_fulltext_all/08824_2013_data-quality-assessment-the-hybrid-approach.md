---
otero_id: 8824
otero_key: "CQ2674RG"
title: "Data quality assessment: The Hybrid Approach"
authors: "Philip Woodall; Alexander Borek; Ajith Kumar Parlikad"
year: "2013"
journal: "Information & Management"
doi: "10.1016/j.im.2013.05.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Philip Woodall \*, Alexander Borek, Ajith Kumar Parlikad

University of Cambridge, Department of Engineering, Institute for Manufacturing, 17 Charles Babbage Road, Cambridge CB3 0FS, UK

A R T I C L E I N F O

Article history: Received 13 October 2011 Received in revised form 4 February 2013 Accepted 26 May 2013 Available online 4 June 2013

Keywords: Data quality Information quality Information quality assessment Data quality assessment Hybrid Approach Assessment techniques

## A B S T R A C T

Various techniques have been proposed to enable organisations to assess the current quality level of their data. Unfortunately, organisations have many different requirements related to data quality (DQ) assessment. For example, some organisations may need to focus on ensuring regulations are met rather than reducing costs. Due to this, organisations may be forced to follow an assessment technique, which may not wholly fit their needs and current situation. Therefore, we propose and evaluate the Hybrid Approach to assessing DQ, which demonstrates how to dynamically configure an assessment technique as needed while leveraging the best practices from existing assessment techniques.

\- 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

The quality of an organisation’s data is paramount to its success, and poor data quality (DQ) can have disastrous and even lifethreatening consequences. The explosion of the Challenger space shuttle and the mistaken shooting down of an Iranian civilian aircraft are two high-profile examples where DQ was a causing factor [9]. While these may be extreme examples, many organisations rely on having good quality data to make decisions for their every-day operations. Furthermore, even organisations with advanced data management practices, that implement continuous improvement methodologies, find that employees have a greater need for high quality data [16].

To be assured that data is ‘‘fit for use’’ – where ‘‘fit for use’’ data is of required quality [19] – the first step is the DQ assessment (see Fig. 1), the aim of which is to inspect data to determine the current level of DQ and the extent of any DQ deficiencies [6]. Many assessment techniques (ATs) have been proposed to support this endeavour, and these are typically part of a wider DQ methodology, which in addition provides guidance on how to improve DQ (see for example [3,7,15,17,18]). The focus of this paper is on DQ assessment and the associated ATs rather than the DQ methodology or DQ improvement. There are many methods, which can be used as part of a DQ assessment such as interviewing, data modelling and gap analysis. The ATs support and guide the process of selection and combined usage of these methods to enable organisations to understand their current level of DQ.

Unfortunately, there are many different requirements related to DQ assessment because of domain and context differences associated with different organisations. For example, a large financial institution with advanced data management practices will have different needs than a small utility provider with one or two information systems. With the gamut of possible requirements, organisations may be forced into selecting an existing AT which may not be wholly suitable for their given set of requirements; this could lead to the unnecessary execution of DQ related activities or the omission of essential activities as part of an assessment.

In particular, prior to this research, the authors worked with ten different organisations in the UK (ranging from public sector institutions, to transport organisations to water, electric and gas utility companies), to conduct DQ maturity assessments (see [21]). The differences in the levels of maturity between the organisations necessitated a very different approach to data quality assessments. Some organisations already had existing practices related to DQ assessment and they needed to incorporate missing activities. For example, one organisation was following a similar process as advised by an existing AT, but it did not include an assessment of impacts/costs of poor quality DQ. This activity is shown in other ATs, but it was not obvious where and how to incorporate the costs activity into the organisation’s existing DQ assessment. The organisation was left to place this activity where they thought best. In other cases, some organisations were aware that multiple DQ assessment methodologies existed, but they had no idea, or way in which they could determine, which methodology to use and why. Finally, one maintenance, repair and overhaul (MRO) organisation indicated that they had three requirements for their DQ assessment: to determine the actual costs caused by low DQ, to model the way data is created and how it flows, and to gather existing data models. However, no current existing AT can meet these requirements because no single AT advises how to conduct all of these activities.

![](/api/attachments/CQ2674RG/fulltext/images/c27826112a14b8238977b0a823ed6a1f2f5d6449310f4d56d24f1b01696b4e62.jpg)  
Fig. 1. Relationship of DQ assessment and improvement.

The Hybrid Approach is proposed to address this problem and the aim of this approach is to show how new ATs can be developed by combining the existing activities in order to meet all requirements of any organisation needing to assess DQ. The Hybrid Approach therefore avoids the problem of having to complete unnecessary activities, and also provides the ability to take activities from one AT and integrate them with activities from other assessment techniques to produce a fully customised AT.

For the Hybrid Approach, the existing ATs have been divided into their constituent activities. These activities were then analysed to understand the order in which they should be placed in and whether any activity is dependent on another activity. Finally, a four step process is described that shows how to develop a new AT based on the existing activities and their ordering and dependency constraints.

The business need was not the only motivation for developing the Hybrid Approach. Many different ATs have been developed and it is not clear whether more ATs need to be developed for different contexts. Furthermore, it may also be the case that a theoretically ‘generic’ AT exists, and that each of the existing ATs is in some way an instance of this. The development of a model of the AT activities therefore provides a basis from which new ATs can be explicit in how they are different from existing ATs, and it is also a step towards identifying the fundamental activities required for a DQ assessment.

The terms data and information are used synonymously in this paper, and the rest of this paper is organised as follows: Section 2 describes DQ assessment techniques and Section 3 presents the methodology used to develop the Hybrid Approach. The selection of ATs, the extraction of activities from these ATs, and details of how the activities should be ordered and what activities are necessary for new ATs is described in Section 4. Section 5 lists the steps required to develop a new AT by combining the activities, and Section 6 presents the results of applying the approach within London Underground. Section 7 discusses the evaluation of the Hybrid Approach and, Section 8 describes the limitations. Finally, Section 9 presents the conclusions of the research and future work.

## 2. Data quality assessment techniques

Data quality ATs form a core part of the Hybrid Approach and this work defines an AT to be a series of activities that are used to complete a DQ assessment. A DQ assessment is defined as a process for obtaining measurements of DQ to determine the current state of DQ. The current state can then be used to determine the level of DQ improvement required. In general, DQ measurements are obtained by determining values for different metrics; for example, counting the number of missing entries in a database. To determine the level of DQ improvement required, measurements can be compared to reference values, such as DQ requirements, which could state how many missing entries can be tolerated for the data to be ‘fit for purpose’. This definition of DQ assessment follows the unified terminology of the Data Quality Measurement Information Model (DQMIM) [6] where the idea of assessment is to make a judgement about DQ measurements (to determine the level of DQ improvement required). This is a common definition, although the exact terminology is not always used in a uniform way; for instance, [12] defines assessment as the ‘‘means to identify and document those areas with greatest need of improvement as well as provide a baseline against which further improvements can be measured’’. In a review and classification of the ATs [5], measurement is defined as the process of obtaining values for DQ dimensions and assessment is when these values are compared to reference values to enable a diagnosis of quality. A multitude of DQ dimensions exist and they help to categorise DQ problems, examples include accuracy, completeness, consistency, timeliness [2]. Clearly, these definitions of DQ assessment capture the idea of measurements being just values and assessment being the application of judgement to these values to determine the level of DQ improvement required.

## 2.1. Existing research on configuring assessment techniques

DQ projects can be selected by considering constraints such as the value and cost of a project, and a method for this has been proposed previously [1]. A DQ assessment could be one of these projects and therefore the Hybrid Approach, which describes how to configure the assessment, operates from a less general perspective. The research on selecting DQ projects could be used at a more strategic level to complement the Hybrid Approach by showing what set of projects (or DQ assessments) need to be performed to address DQ on a larger scale throughout an organisation. Some of the existing ATs also suggest that the assessment should be configured, such as by planning what activities need to be done [7,15]. This planning only refers to the activities within a single AT and does not consider what other activities, from external ATs, need to be included. Furthermore, this existing research only acknowledges the fact that an AT should be configured rather than providing specific guidance on how to do it successfully.

## 3. Research methodology

The Hybrid Approach was developed in six main stages, starting with the task of obtaining the existing ATs from the literature, then extracting the activities from these ATs, checking the extraction results and resolving any problems, and, finally, refining the approach based on feedback from a review (see the numbered boxes (tasks) in Fig. 2).

For each of the six tasks, different methods were used (see dashed lines in Fig. 2) to ensure that the Hybrid Approach satisfied the following quality goals from an existing evaluation framework [10]:

\- Validity – All statements made by the approach are correct and relevant to the problem, for the set of statements that are worth testing as valid.

\- Completeness – The approach contains all the statements about the domain that are relevant, for the set of statements that are worth trying to find.

\- Comprehension – The approach is adequately understood by its target audience.

\- Understandability – As far as feasibly possible the approach is presented in an understandable format.

\- Test coverage – The approach has been adequately tested in terms of feasible test coverage. Feasible test coverage means that there may be other relevant tests, but it is not worthwhile identifying and performing them.

![](/api/attachments/CQ2674RG/fulltext/images/d40584e87f30e68c3659864ae0412c8040cb6ec08865bb85504580597a45041f.jpg)  
Fig. 2. The Hybrid Approach development process.

\- Practical utility – The utility of the approach is the extent to which it improves some aspect of performance for the target audience or provides non-trivial insights into the phenomenon being studied.

\- Future resilience – The above quality goals remain stable or improve as the approach is used.

To obtain a more detailed evaluation of the most important components of the Hybrid Approach, the following two components were given special attention with regards to meeting the quality goals:

\- The set of existing ATs used for the approach [ATs].

\- The set of extracted activities from the ATs used in the approach [activities].

The reference to the above components and each of the quality goals is made within the square brackets in Fig. 2; in cases where the entire approach is evaluated, this is referred to as ‘all’ in Fig. 2.

The evaluation framework in [10] is well suited to evaluate the Hybrid Approach because it is useful for approaches that do not produce an output value that can be compared to an actual value. It is also useful in cases where the use of the approach and non-use of the approach are difficult to trial with all contextual factors remaining consistent. This is the case with the Hybrid Approach where it is very difficult to stabilise contextual factors when conducting multiple DQ assessments and no one value indicates the success of the approach over another.

An important aspect of the evaluation framework is that it specifies that methods introduced to achieve these goals should be separated from the means to assess the goals. Therefore, the framework was used both during the development of the Hybrid

Approach (in an attempt to help achieve the goals – see Fig. 2) and also to evaluate the approach after its development (to assess the extent to which the goals have been satisfied – see Section 7).

The original evaluation framework contains the ‘syntactic correctness’ goal (meaning that all statements in the model adhere to the syntax of the language used for the model). This goal was not measured for this work because the Hybrid Approach is not expressed using a formal language. Furthermore, the last quality goal (future resilience) was not specified in the original framework and has been added by this work because it was noticed at the end of the development of the Hybrid Approach that this goal needs to be considered. For this reason, this goal has only been evaluated (see Section 7.4), but was not considered during the development.

The following subsections discuss the specific methods used for each task in Fig. 2.

## 3.1. Selection of ATs

The development of the Hybrid Approach started with the task of obtaining the existing ATs from the literature (see Fig. 2, task 1). The search was done systematically to minimise the chances of missing an AT (completeness quality goal), and the following filtering criteria were used to ensure that the ATs are valid and practically useful:

Studies were selected only if:

1. The study contains an AT (according to the definition in Section 2), which may be part of a wider DQ methodology, and describes what activities are involved.

2. The study contains an AT that has been subject to a rigorous review (as required by papers in high ranking journals or ATs described in peer reviewed books).

3. The study contains an AT that has been subject to an actual implementation and successful trial of the approach.

Studies were rejected if:

4. The study does not describe an AT and the activities in sufficient detail to enable a DQ assessor to clearly and easily implement the activities.

5. The study only describes DQ improvement and not an AT.

The Scopus search engine, ACM digital library, Google books and proceedings of the International Conference on Information Quality were used to search systematically for studies (papers reports/books etc.) which contain ATs. Special attention was given to ensure that the digital libraries covered the relevant journals (such as Information and Management and Communications of the ACM etc.). Moreover, the search continued for additional relevant studies by searching the references section of each study obtained.

## 3.2. Extraction of activities

Task 2 involved extracting the activities from each AT, and this was done using a structured extraction procedure to ensure that no activities would be missed and that each activity is valid (see Fig. 2, task 2). Activities were extracted by reviewing each source describing an AT and recording the activities it describes in an ‘extraction table’. Table 1 shows a sample part of an extraction table for two activities in the TQdM-a AT. The table records the name, description, general comments related to the activity, and the link to the study (where the activity is described in the original source).

In addition to the structured extraction process, the activities were subject to an independent review process shown in Fig. 3. This provided a secondary check that the activities are correct and relevant and to detect any activities that were missed from the extraction (see Fig. 2, tasks 3 and 4). The first author extracted the activities and the second and third authors each performed an independent review of this extraction. After this, the three reviewers met to resolve the differences, such as missing activities etc., and the final list of activities was produced at this meeting.

Table 1  
A sample of the data extraction table.

<table><tr><td>AT reference</td><td colspan="3">TQdM-a [7]</td></tr><tr><td>Comments</td><td colspan="3">None</td></tr><tr><td>Activity</td><td>Definition of activity</td><td>Comments</td><td>Link to study</td></tr><tr><td>Model data creation and flow</td><td>The process of understanding and creating a model of the way data is created, updated, deleted and is transferred from one source to another</td><td>None</td><td>Page 160, Step 3: “determine all business process and applications, and all who create or update a group of data”</td></tr><tr><td>Select a place where data is to be measured</td><td>Select the place where data is to be measured based on the objectives for measurement. This includes determining when and where to measure the data or specifying who will give subjective opinions.</td><td>None</td><td>Page 164, Step 4: “Select a place where data is to be measured”</td></tr></table>

![](/api/attachments/CQ2674RG/fulltext/images/09a3732120f066e633940a256a54e85634a0a8b91c82e7a3894f978ac168fd9a.jpg)  
Fig. 3. Process for validating the activities.

## 3.3. Determining the ordering of activities

A conference paper (see [20]) describing the approach was peer reviewed by three reviewers as part of a conference submission procedure for task 5. The aim was to use the review process as a means to check all the quality goals for the entire approach; although it was not possible to ensure that the reviewers gave specific attention to all quality goals, useful feedback was obtained. In addition to the conference review process, general comments from attending the conference contributed to the quality goals. In particular, the need to provide guidance on how the activities should be ordered in a new AT was suggested as a means to improve the approach, and this was developed in task 6 (see Fig. 2). The extraction procedure was extended to record, for each activity in each AT, the dependencies and any ordering constraints described by the AT. Furthermore, for the final evaluation of the Hybrid Approach, a series of DQ assessments were carried out as part of a trial in a UK-based organisation that manufactures car parts, and these assessments also provided information about the ordering of activities.

Table 2  
DQ assessment techniques that meet the selection criteria.

<table><tr><td>DQ assessment technique name</td><td>Full name</td><td>Study</td></tr><tr><td>AIMQ</td><td>AIM quality</td><td>[11]</td></tr><tr><td rowspan="2">CDQM-a</td><td>Complete data quality</td><td>[3]</td></tr><tr><td>Methodology</td><td>and [4]</td></tr><tr><td>COLDQ-a</td><td>Cost-effect Of low data quality</td><td>[12]</td></tr><tr><td>DQA</td><td>Data quality assessment</td><td>[14]</td></tr><tr><td>EDQP-a</td><td>Executing data quality projects</td><td>[15]</td></tr><tr><td>SODQA-a</td><td>Subjective-objective data quality assessment</td><td>[17]</td></tr><tr><td>TDQM-a</td><td>Total data quality management</td><td>[18]</td></tr><tr><td>TQdM-a</td><td>Total quality data management</td><td>[7]</td></tr></table>

## 4. Results of the selection of ATs and extraction of activities

The complete list ATs, as found by the systematic search process, are shown in Table 2, which lists the name (acronym) of the AT, its full name, and the study which proposed the AT. For the CDQM-a AT, two studies described the same AT and both of these were selected and used to extract the activities. Some studies described a complete DQ methodology (which includes DQ improvement) and not just the assessment stage. In these cases, ‘‘-a’’ is added to the end of the AT name to indicate that the DQ assessment is part of the full methodology; for example, TDQM is the full methodology and ‘TDQM-a’ is the DQ assessment part.

## 4.1. DQ assessment activities

The activities, extracted from the selected ATs, are shown in Table 3. The first column contains the name of the activity and an abbreviation of the activity in parentheses, a description of the activity is given in the second column, and the ATs that contain the activity are listed in the final column.

As a result of the review process of the activities (see Fig. 3), a total of 16 disagreements were found and resolved by either: removing an activity that was mistakenly added; adding an activity that was missed; or refining the name, description, and/or link to the study. Two of the key changes included: (1) changing the description for ‘‘Identify DQ dimensions’’ to account for the case where an existing model of dimensions is already available and can be used without having to select specific individual dimensions and (2) adding the ‘‘Analysis of results’’, ‘‘Identify and prioritise the organisational problems’’, and ‘‘Identify DQ costs’’ activities to TQdM-a, which were originally missed out erroneously.

Another observation concerning the activities is that one activity extracted from EDQP-a described planning the DQ assessment project (where the required activities from the EDQP-a AT are selected). This activity was removed from the extraction because if the Hybrid Approach is used, it becomes the planning activity and therefore describes how to select the relevant activities from not just EDQP-a, but from all the ATs in Table 1.

One problem with extraction procedure used to extract the activities from the ATs was identified: some sources that describe an AT deliberately present the set of activities at a high level of repeating the entire extraction process in Fig. 3 and focussing only on actively checking if any other activities should be attributed to the ATs that do not describe all activities. As a result of this process, the Dims., Data items, Place and Ref. data activities were found to be part of all ATs but are not described in some. As an example, for the Data items activity, Fig. 2 in the paper describing the SODQA-a AT shows ‘‘Dataset in use’’ [17], which implies that the data set has been selected. However, the paper does not describe any activity related to selecting the dataset.

Table 3 Activities associated with existing ATs.

<table><tr><td>Activity + (abbreviation)</td><td>Definition of activity</td><td>Source AT(s)</td></tr><tr><td>Communicate and share the results (Com.)</td><td>Communicate and share the results or current progress of the DQ assessment with relevant people</td><td>TQdM-aEDQP-aCOLDQ-a</td></tr><tr><td>Conduct analysis of results (Analysis)Define DQ requirements (Reqs.)</td><td>The process of analyzing the values from the DQ measurement(s).The process of defining what level of DQ is required (for example, setting minimum thresholds that DQ must meet). DQ requirements can be compared to the measurement values to determine the level of DQ improvement required</td><td>AllAIMQTDQM-aCOLDQ-aEDQP-aCDQM-aTQdM-a</td></tr><tr><td>Expose the DQ assessment project to senior management (Expose)Group/organise data items (Group)</td><td>Expose and establish senior management support for the DQ assessment projectThe process of grouping data items into categories (for example, grouping criteria could include the type of data, level of risk etc.)</td><td>COLDQ-aEDQP-aTQdM-aEDQP-a</td></tr><tr><td>Identify and prioritise the organisational problems (Probs.)</td><td>Based on what is known at the start of the assessment, list the specific problems focussing on problems that relate to DQ</td><td>TQdM-aEDQP-aCDQM-aCOLDQ-a</td></tr><tr><td>Identify DQ costs (Costs)</td><td>The process of determining the business impact and/or economic losses caused by low DQ (note that business impacts may not only be financial)</td><td>TQdM-aCOLDQ-aCDQM-aEDQP-a</td></tr><tr><td>Identify DQ dimensions (Dims.)</td><td>The process of identifying dimensions or using an existing model of DQ dimensions e.g., PSP/IQ DQ.</td><td>AIMQSODQA-aTQdM-aTDQM-aCOLDQ-aEDQP-aCDQM-a(DQA)</td></tr><tr><td>Identify DQ metrics (Metrics)Identify reference data (Ref. data)</td><td>The process of identifying, developing or using an existing set of DQ metricsThe process of determining comparison data which can be used as input to the selected metrics. For example, one metric for measuring accuracy requires the stored value to be compared to the &#x27;real&#x27; reference value; this process attempts to determine and document the &#x27;real&#x27; value</td><td>AllTQdM-a(AIMQ)(SODQA-a)(TDQM-a)(COLDQ-a)(EDQP-a)(DQA)(CDQM-a)</td></tr><tr><td>Model data creation and flow (Model)</td><td>The process of understanding and creating a model of the way data is created, updated, deleted and is transferred from one source to another.</td><td>TQdM-aTDQM-aCOLDQ-aEDQP-aCDQM-a</td></tr><tr><td>Perform objective/subjective DQ measurement (Measure)Select a place where data is to be measured (Place)</td><td>The process of obtaining DQ measurements from an actual data set or by obtaining (subjective) opinions of the current state of DQ.Select the place where data is to be measured based on the objectives for measurement. This includes determining when and where to measure the data or specifying who will give subjective opinions</td><td>AllTQdM-aEDQP-aDQA(AIMQ)(SODQA-a)(TDQM-a)(COLDQ-a)(CDQM-a)</td></tr><tr><td>Select data items (Data items)</td><td>The process of selecting the relevant data values, attributes, tables, information systems, paper files etc. which will be subject to the DQ assessment. This can also include the process of sampling the data to obtain the required data values</td><td>TQdM-aTDQM-aEDQP-aDQA(AIMQ)(SODQA-a)(COLDQ-a)(CDQM-a)</td></tr><tr><td>Select processes (Process)</td><td>The process of selecting business processes that will be focused on in the assessment</td><td>TQdM-aCOLDQ-aCDQM-a</td></tr><tr><td>Gather general meta data (Meta)Perform data profiling (Profile)</td><td>The process of gathering relevant meta data such as data modelsThe process of examining the data and collecting statistics and information about that data such as distribution of values</td><td>DQADQA</td></tr><tr><td>Validate the DQ metrics(Val. Metrics)</td><td>The process of checking that the DQ metrics and the implementation of DQ metrics are correct</td><td>TDQM-aDQA</td></tr></table>

abstraction and therefore miss out some of the more ‘‘obvious’’ activities that must be performed. The extraction procedure alone therefore gives a false picture of the full set of activities in each AT. To address this problem, the extraction procedure was modified to also consider and review these activities. This consisted of

For clarity, the activities that have been attributed to an AT are shown with the AT in parentheses in Table 3.

## 4.2. Classification of activities

The activities in Table 3 were classified as either ‘recommended’ or ‘optional’ based on whether they are included in every existing AT or not. Note that in Table 3 there are seven activities that have been included in every AT (in the ‘source AT’ column, three are listed as ‘‘all’’ and the other five have the AT names listed separately because of the problem described in the preceding section). Recommended activities are those that are recommended to be considered for inclusion in every new AT. According to this classification, the following are recommended activities:

(1) Select data items.

(2) Select a place where data is to be measured.

(3) Identify reference data.

(4) Identify DQ dimensions.

(5) Identify DQ metrics.

(6) Perform measurement.

(7) Conduct analysis of the results.

The measurement process (6) obtains values for the dimensions (4) and metrics (5) for a given set of data items (1) and is the heart of an AT. Furthermore, the values from the measurement are meaningless until some level of interpretation/analysis is applied (7). The place to measure the data (2) needs to be identified in order to know where to apply the metrics in the measurement process, and the reference data activity (3) is conditional depending on what is being measured. For example, reference data may be needed as input to a metric that measures accuracy – in this case, the ‘‘real’’ value (reference value) is needed as well as the recorded value. If the metrics do not require reference data, then it is not necessary to identify reference data.

## 4.3. Ordering and dependencies between activities

It is necessary to know what order the activities should be placed in so that newly developed ATs are usable and do not contain clearly un-implementable links between activities. In addition to ordering, it is also necessary to know, if an activity is added to an AT, what other activities also need to be added (because the first activity cannot be completed in isolation); this type of relationship is referred to as an activity dependency. Ordering indicates whether given any two activities that are present in an AT, which activity must be completed before the other. Dependencies indicate, given the inclusion of one activity in an AT, what other activities must be added to the AT. The dependency gives some indication of ordering because, in many cases, the reason that one activity needs another activity to be included in the AT is because the additional activity needs to be completed before the other activity. There are cases, however, where given an activity in an AT, no other activity needs to be included in the AT, but it is still necessary to determine the ordering between the activities; both concepts therefore need to be considered separately.

Fig. 4 shows the resulting ordering and dependencies between all activities. In this figure, a black dot with an arrow signifies the starting position, the grey boxes indicate the recommended activities, the boxes with grey diagonal lines represent activities that can be placed in various positions subject to constraints (referred to as variable activities), arrows indicate necessary ordering between activities, and dashed arrows indicate dependencies between activities – for example, if the Group activity is included so must the Data items activity. In any part of the AT in Fig. 4 where there are multiple paths, these can be done in parallel until the arrows converge on an activity. In which case, all previous activities must be completed before proceeding.

![](/api/attachments/CQ2674RG/fulltext/images/5935c60e70a8d22d1b972b09733d3642477a5ce11dbd8faa330cf926e43eda5c.jpg)  
Fig. 4. A generic AT.

The Com. activity has no links to other activities and can be done at any position in the AT to keep people informed of progress. In fact, EDQP-a suggests that the Com. activity can be done at various points in the AT to maintain a high level of communication about the assessment to external stakeholders. The Com. activity is therefore a type of variable activity with no constraints on where it may be placed.

Two of the trial assessments (conducted in a UK car parts manufacturer organisation) provided useful findings for this research. In particular, the Data items activity can be preceded by the Process activity and the Dims. activity can be preceded by the Probs. activity. Appendix A gives explanations for the ordering of these and all the other activities (excluding the variable activities, which are described in the next section).

Five of the activities were found to have different possible positions in the AT depending on what is required from the combination of activities, and these are referred to as variable activities. The placement options for these activities are shown in the tables in Appendix B – that is, the list of activities that can be placed before and after the main activity and a description is given for why the variable activities can be placed in the specified order. In these Tables, italics are used to show dependent activities. For example, in Appendix B, Table 10 shows the three activities that costs is dependent on, and at least one of these activities must precede the costs activity. Note that the other activities (including the recommended activities) should always be used in the order shown in Fig. 4.

Fig. 4 shows an AT containing all the activities and represents one configuration of the variable activities that satisfies all the constraints. The Probs. activity can be used first because eight activities are recommended to be done after this activity (see Appendix B Table 7) and can benefit from an initial identification of DQ problems. The modelling of data creation and flow (model activity) is done only for the set of data items identified by the Data items and Group activities, which, in turn, are relevant to the identified DQ problems (see Appendix B Table 11). The Process activity uses the model to select the processes that will be the focus of the assessment (see Appendix B Table 9); note that the processes use and are relevant to the data items from the Data items and Group activities because the model has been developed for these data items. The Place activity uses the model to identify relevant places in the flow of data that can be used to obtain the measurements (see Appendix B Table 11). At the end of the AT, the costs due to poor DQ are determined for the actual DQ problems identified by the measurements and the analysis of the measurements. Note that the Costs activity must precede at least one of the Probs. Measure or Analysis activities (see Appendix B Table 10). In addition, the model is also useful with regard to helping to identify the costs of any failed transactions/processes (see Appendix B Table 10). Finally, DQ requirements can be specified and the understanding of costs can be used to set realistic DQ requirements that are feasible to achieve (see Appendix B Table 8).

Note that data quality profiling is typically done as part of the measure activity. That is, when the metrics have been defined, it is convenient to get profiling software to automatically calculate the values for the metrics. The use of profiling as an actual activity in Fig. 4 shows that it can also be used to help develop suitable metrics in an investigative way.

The generic AT in Fig. 4 does not intend to imply that a ‘waterfall’ style process is needed. In fact the opposite is the case, and it would be fine for iteration to occur between any number of activities. For example, when conducting the assessment, the process of identifying dimensions may highlight a need to re-check the data items selected and so iteration could occur between these activities as many times as required.

There may also be iteration or interaction between developing an AT (using the steps described in the following section) and conducting the assessment. For example, after developing a new AT and then carrying out some of the activities, it may be necessary to re-evaluate the AT and change it as required. The act of delving into the details in this way can help to inform the overall strategic direction that the assessment must take, and could shape what future assessment project(s) need to be carried out.

## 5. Steps to develop a DQ assessment technique

A simple four step procedure is proposed that shows how to use the results from the previous section to develop a new AT that is suitable for specific organisational requirements. When using these steps to develop a new AT, it may be necessary to revisit prior steps in an iterative manner. For example, selecting activities (step 3) could also help with identifying new company requirements (Step 2) that were not thought of the first time.

We use the example of the MRO organisation described in the introduction to give a concrete description of what needs to be done in each step. Note that we decided not to use the MRO case for an evaluation of the approach because the organisation did not continue with the assessment process due to other pressures within the business that put this as a low priority. We designed the technique, but we could not follow up with the organisation to conduct a proper evaluation in accordance with our evaluation criteria. This example is therefore used as illustration only in this section.

## 5.1. Step 1: determine the aim of the assessment

The aim drives the assessment process and is essential to inform DQ assessors of what the resulting AT should be used for. The aim will vary depending on what the organisation intends the assessment to achieve. Example aims include:

\- To measure a particular DQ problem which has been identified previously.

\- To determine and prioritise an organisation’s DQ problems and obtain measurements for each problem.

Continuing the case of the MRO organisation described in the introduction, the organisation intends to perform a DQ assessment in the asset management (AM) part of the organisation (which is responsible for managing the equipment throughout the organisation), and the aim of the assessment is: to identify what financial effect DQ is having on the AM part of the organisation and to identify why people do not want to use the data in the main AM information system.

## 5.2. Step 2: identify the company requirements related to the DQ assessment

Different companies will have different requirements which relate to the DQ assessment. This step requires the organisation wanting to assess DQ to identify these requirements related to the DQ assessment. To ensure the relevance of the requirements, it is useful to check that each requirement follows from the aim (Step 1) and therefore contributes to achieving this aim.

The MRO organisation indicated that they have four requirements:

1. Determine the actual costs caused by low DQ.

2. Obtain an initial estimate of costs to justify the resources for the assessment.

3. Model the way data is created and how it flows.

4. Gather existing data models.

Managers in the organisation recognised that poor DQ was one possible source of financial loss and therefore they wanted to identify if and how much poor DQ was costing the business. Furthermore, having never completed a DQ assessment before, the managers want an initial estimation of costs early in the assessment in order justify the resources being put into the assessment process (they also want a more detailed estimation of costs later). The reason for the third requirement is that the organisation has lost track of where data originates, who uses it throughout the process, and where it ends up. The existing documentation of these details and how the data is transformed filtered etc. when it is moved from one system to another is also missing.

## 5.3. Step 3: select AT activities which meet organisational requirements

The aim of this step is to select the relevant activities, from the list in Table 3, which meet the organisational requirements related to the DQ assessment. In practice, identifying the requirements (in the previous step) may be done with knowledge of the activities as an aid, rather than independently. For instance, it may be difficult to think of requirements without any stimulus and so the list of activities and their descriptions can help to facilitate this process. It is therefore likely to be an iterative process where these steps (2 and 3) are used to complement each other and enable the final list of necessary requirements to be generated.

Table 4  
Mapping of requirements for the MRO organisation.

<table><tr><td>Activity requirement</td><td>Suitable AT activities</td></tr><tr><td>Determine what the impact of low DQ is causing on the ‘bottom line’ of the businessObtain an initial estimate of costs to justify the resources for the assessment</td><td>Identify DQ costsExpose the DQ assessment project to senior managementIdentify DQ costs</td></tr><tr><td>Identify the users of data and where the transfer of data occurs between systems (e.g., via extract transform and load operations), and what transforms are applied</td><td>Model data creation and flowGather general meta data</td></tr></table>

The requirements from the MRO organisation are shown in the ‘activity requirements’ column of Table 4 and the mapping of these requirements to activities is shown in the ‘suitable AT activity’ column. The first requirement maps to the Costs activity because it is about determining how the business is being affected financially. The second requirement maps to both the Expose and Costs activities and also specifies that costs need to be determined early in the assessment programme. This last part of the second requirement indicates how the positions of the activities in the AT need to be configured. The third requirement concerns determining the where the information moves (between different systems) and therefore maps to the Model activity. Also, this requirement identifies that when the data is moved from one system to another, the transformations need to be identified; the Meta activity is needed for this to help to capture the underlying assumptions as to why the data is being transformed and the assumptions that the transform are introducing.

## 5.4. Step 4: configure the activities in the AT

The aim of this step is to arrange the activities (including the required activities from Step 3) into a sensible order and include any activity dependencies. The ‘recommended’ activities should be strongly considered to be included and only removed if there is a sound reason for not needing to perform them. To help with this step it is useful to start with the generic AT in Fig. 4 and remove the activities that are not needed and then move any remaining variable activities to the desired positions. Fig. 5 shows the final AT suitable for the MRO organisation’s requirements; activities surrounded by a thicker border are the required activities from Table 4.

In Fig. 5, the Costs activity has been added twice. The first instance of this activity will be used to obtain an initial estimate of the financial impact of poor DQ and has therefore been placed second in the AT preceded only by the Probs. activity, which must be included before Costs (see Appendix B Table 10). The second instance of Costs (at the end of the AT) will be used to obtain the actual cost of the DQ problems and is preceded by the Measure and Analysis activities so that the costs can be determined for the identified DQ problems. The Expose activity follows the Probs. and Costs activity because it is necessary to identify initial DQ problems before conducting Expose. Furthermore, the Costs activity can also be a useful input to the Expose activity, and this ordering also satisfies the second requirement of the MRO organisation: the management want to see some initial estimate of the costs of poor DQ. Finally, the position of the other activities has been retained from the AT shown in Fig. 4 because there is no need to reorder these. Fig. 5 therefore presents an AT that is a perfect fit for the MRO organisation’s requirements and shows how the activities from multiple ATs can be combined in a ‘best practice order.

![](/api/attachments/CQ2674RG/fulltext/images/1b6f571419aab1bf25316a6033bae2e07d3bd40d83766ab2fd4b4431fba9de97.jpg)  
Fig. 5. A new AT for the MRO organisation.

## 6. Applying the Hybrid Approach within London Underground

In order to evaluate whether the Hybrid Approach is of any practical utility, the approach was trialled within London Underground Limited (LUL). LUL operate and maintain the underground transit system in Greater London, UK, and are a part of Transport for London (TfL). The underground system caters for over 3 million passengers per day, operates 270 stations, 250 miles of track, and rolling stock built from 1968 until present. A new AT was developed and carried out to assess the current state of DQ in the signalling, control and information asset group of LUL. The data used by this group includes maintenance data (such as what infrastructure/equipment etc. has and needs to be replaced) about the train lines operated by LUL and is, therefore, critical for the safety of the passengers.

## 6.1. Administration of the approach

LUL was chosen to apply the approach mainly because they were willing for the authors to have access and take control of the design of the DQ assessment that would ultimately be conducted within the organisation. We were also able to help with the assessment in a way that allowed us to measure each of our evaluation criteria (see Section 3), unlike the MRO case in the previous section.

![](/api/attachments/CQ2674RG/fulltext/images/0bee81b396ccb19ba0ad86364961654e8dda55cffc79b377dafb11e5a51dd109.jpg)  
Fig. 6. AT for London underground.

The data for the evaluation was collected via face-to-face interactions with LUL staff, communications over the telephone and emails. After establishing that we could conduct the design of the DQ assessment, the manager of the signalling, control and information asset group of LUL was interviewed to establish the initial motivation for the assessment. During the second half of this interview the process for determining the requirements for the assessment was started, and the list of activities (in Table 3) was given to the manager to aid this process. The manager was asked to spend some time to think about exactly what was needed for the assessment and speak to other members of staff to determine a final set of requirements. Once the requirements were determined, the first author selected the suitable activities and constructed the AT model shown in Fig. 6. A few iterations and discussions concerning the requirements were needed before the final model emerged. This model was then used as the basis for the assessment, and each activity was planned and conducted by either LUL staff, the first author, or in collaboration. Finally, an industrial report that summarised the process, results and recommendations was sent to LUL.

## 6.2. Details of the trial

The manager of this data is keen to ensure that it is of the highest quality and wants to detect any possible DQ problems. The aim of the assessment was, therefore, to determine what the existing DQ problems are in the signalling, control and information asset group of LUL and obtain measures for these problems.

There are many information systems in use in this group of LUL and therefore one requirement for the assessment was to select the data/systems that would be the focus of the assessment (see the first requirement in Table 5). Furthermore, this data is used by either the finance department or maintenance (or both); thus, the second requirement was to identify what data is used by each department, so that the final results would be meaningful to the different users. Finally, the last requirement was to disseminate the results to the managers of each department so that they could decide whether any necessary future action is required to improve the data.

The three matching activities for these requirements are Select data items, Group/organise data items, and Communicate and share the results (shown in Table 5). The last requirement also implies that the results should be communicated at the end of the assessment when the final results have been obtained. This requirement helps in Step 4 of the Hybrid Approach to indicate that the Com. activity needs to be placed at the end of the AT. The resulting AT, which matches the requirements of LUL, is shown in Fig. 6. Note that this includes all of the required activities, and none of the variable activities were included in the AT because they are not needed to meet the requirements of LUL.

The assessment started with the selection of data items because the manager at LUL wanted to identify if there are any problems with the data in the signalling, control and information asset group. As mentioned before, many systems are used in this group and so this activity firstly identified one of the larger information systems and secondly selected a set of data items from within this system. The data items all contained condition-related data about one of the underground train lines. As part of the grouping activity, the data items were identified as being used by either maintenance or finance or both. Over 50 thousand rows (instances of physical assets/equipment) were extracted from the information system into a spreadsheet. This provided a snapshot of the data from which to check the quality without any chance of affecting the data in the live system; this is a very simple version of a staging area [14]. From the data, two dimensions were identified as being necessary to check: completeness and conformance to business rules – see [7]. These dimensions were then used in the Metrics activity to guide the construction of the metrics. No reference data was needed for the metrics (both completeness and conformance to business rules could be measured without needing additional data) and so the Ref. data activity was not carried out. Many of the metrics for business rule conformance were of the following form: ‘‘number of violations of the business rule’’/‘‘total number values inspected’’ which gave an indication of the proportion of errors.

Table 5 Requirements for LUL.

<table><tr><td>Activity requirement</td><td>Suitable AT activities</td></tr><tr><td>Determine what information systems and specific data to focus on (within in the signalling, control and information asset group)</td><td>Select data items</td></tr><tr><td>Identify what data is used by finance, maintenance and by both departments</td><td>Group/organise data items</td></tr><tr><td>Send the result to the managers of finance and maintenance allow them to judge whether or what improvement is needed to the data</td><td>Communicate and share the results</td></tr></table>

The metrics for completeness were similar except that they checked for missing values rather than ‘‘number of violations of the business rule’’.

The metrics were coded in software and executed on the spreadsheet as part of the measurement activity, and the results were analysed and documented in a final report that was sent from the University of Cambridge to LUL. The analysis included grouping the results according to the users of the data items (identified in the grouping activity). Finally, this report was distributed to the relevant people in LUL as part of the communicate the results activity.

Clearly stating the aim of the AT (see Step 1 of the Hybrid Approach) was essential as it was used in the documentation of the final assessment report. This informed the readers of the report exactly what the assessment had focussed on and what it aimed to achieve. The report is confidential to LUL and therefore no details of the results are presented.

## 6.3. Changes to the Hybrid Approach after the trial

Although the main aim of the trial with LUL was to evaluate the practical utility of the approach, one additional finding about the Ref. data activity was included in the Hybrid Approach. Originally, the only information available about the ordering of the Ref. data activity came from the TQdM-a AT: the reference data must be associated with the particular data items or group of data items (see Appendix A) and should therefore come after the Data items and Group activities. However, in addition, the trial demonstrated that the metrics indicate whether reference data is needed. For instance, a metric that measures the difference between a real-world value and a stored value (the accuracy dimension) needs reference data (the real-world values) as input. Whether or not reference data is needed is therefore known after defining the metrics. This finding was therefore included in the arrangement of activities shown in Fig. 4 and added to the descriptions in Appendix A.

## 7. Discussion of the quality goals

The following subsections present a discussion of the extent to which the quality goals set out in the introduction have been met by the Hybrid Approach.

## 7.1. The practical utility of the approach

The result of the assessment has provided LUL with a current state assessment of the level of DQ and an understanding of what DQ problems exist in one of their main maintenance systems. This meets the main aim of the assessment, as specified by LUL. With the Hybrid Approach, this was achievable without having to spend time conducting many of the activities that are specified by existing ATs and were not needed to achieve the aim of the assessment. In this respect alone, the Hybrid Approach is therefore a useful mechanism for organisations to ensure that DQ assessments are focussed only on their aims and that cost, time and resources are saved by not conducting unnecessary activities.

In addition to the practical utility goal, the development and the implementation of the AT with LUL covers two more of the quality goals by demonstrating that the activities within the LUL AT are valid (correct and relevant to the problem) and the actual trial of the approach in this real scenario forms part of the test coverage goal.

## 7.2. The validity and completeness of the list of ATs and activities

An additional literature search was carried out by an independent researcher to determine the extent to which the list of ATs used in the Hybrid Approach is valid (by checking whether the existing ATs would be selected again) and comprehensive. Furthermore, promising discoveries of new papers/books etc. found by the authors that related to DQ assessment were also checked for ATs. Although these searches were not systematic and tended to be sporadic, they did provide the opportunity to find a new AT because they were conducted over a longer period of time.

The results of both of these searches found two new studies which could possibly contain ATs: [8,13]. Both of these were published after the main literature review and therefore could not have been found initially, confirming that the initial review was feasibly complete.

One of the new studies [13] did contain a new AT and this was used to confirm the validity and completeness of the existing set of activities. To do this, an extraction procedure was performed that checked for existing and new activities in the new AT. The following activities were confirmed by the extraction: Process, Data items, Costs, Meta, Model, Dims, Metrics, Measure, Analyse and Com. The Ref. data activity could only be inferred to be present because it was not explicitly described; the only reference to this was regarding the accuracy dimension where the study describes, in order to check for accuracy, a ‘‘comparison to a system of record’ is needed [13]. No new activities were found confirming the completeness of the activities.

During the extraction, notes were made regarding the ordering of activities, and this study states that the Model activity is useful as an input to the Place activity because the documentation of the information flows can be used to identify the best place to inspect the data – this confirms the original finding (see the Place activity in Appendix A).

## 7.3. The understandability and comprehension of the Hybrid Approach

In addition to the LUL trial of the Hybrid Approach, a series of smaller DQ assessments were carried out in a UK-based organisation that manufactures car parts. These were carried out by an independent data assessor (a student at the Institute for Manufacturing in Cambridge) to evaluate the understandability and comprehension quality goals. The aim was to determine whether, using the existing documentation of the approach (including the previous conference paper, list of steps and activities, existing studies describing the ATs, etc.) the assessor could follow the entire approach and carry out an assessment without assistance from the developers of the approach. The assessor had limited experience of DQ and therefore prior reading about DQ assessment, and DQ research in general, was done before attempting to understand and carry out the Hybrid Approach. During the assessments, which were developed and conducted onsite at the organisation, the first author (PW) maintained telephone contact with the assessor to monitor the progress and help with any problems encountered.

The results indicated that the assessor had no problems understanding the approach and was able to produce and conduct a number of useful DQ assessments in different parts of the organisation. In fact, these assessments were able to provide feedback that could be incorporated in the Hybrid Approach with regard to the ordering of activities; these were described in Section 4.3 and are labelled as ‘‘trial’’ in the table in Appendix A.

## 7.4. Future resilience of the approach

The Hybrid Approach incorporates ATs developed from 1998 to 2008 and all of these ATs advocate using very similar approaches to assess DQ. No one AT differs drastically from the rest in its approach. The assessment process is therefore fundamentally very similar between all of these ATs despite the ten year time span.

Furthermore, the attempt to validate the validity and completeness of the activities and ATs (see Section 7.2) confirmed most of the existing activities and did not find any new activities. Currently, therefore there is no work indicating that these approaches are in any way outdated, and since the Hybrid Approach is based so heavily on these, this provides an assurance that it will also be resilient into the future. However, new activities are likely to be presented in the future, and for the Hybrid Approach to remain current it must demonstrate that it can accommodate these along with any new evidence related to the inputs and outputs of the activities. For the latter, new evidence concerning the ordering has already been incorporated from the various trials of the Hybrid Approach. The Hybrid Approach is also open to the inclusion of new activities by simply including them in the current list of activities. The only stipulation is that, for the activity to be useful, the ordering and dependencies should be specified in the same way as for the existing activities.

## 8. Limitations

One of the main limitations of the research process, and in particular the extraction of activities, was that not all of the ATs described all of the activities even though they are clearly part of the assessment. We modified our extraction procedure to deal with this problem, but the extraction was not as robust as it would have been had the ATs explicitly described all the activities. In order to make this as auditable as possible, Table 3 indicates where the activities have been inferred to be in a particular AT.

In the actual use of the Hybrid Approach, one potential problem that could arise is when there are multiple requirements from different stakeholders, and especially when they are conflicting. For example, if there are multiple stakeholders that require a DQ assessment and one requires costs to be identified and the other does not, then it is not so simple to just include the costs activity because there are often time and resource constraints. Further research is needed to fully identify the impact that multiple requirements, such as these, will have on the Hybrid Approach, and what is the best way of navigating the model of activities based on multiple requirements.

## 9. Conclusion

Data is a critical asset in today’s organisations, and problems with the quality of this data can have catastrophic and even lifethreatening consequences – especially in the case of the London Underground, where data about the maintenance of the underground train lines is used to make decisions about when to maintain the various assets and equipment that transport people continuously around London.

The first step towards high quality data for any organisation is the DQ assessment. This can provide an indication of the current level of DQ in the organisation and is the basis for initiating actions to improve DQ to desirable levels. Currently, no individual existing AT is wholly suitable to assess DQ for all types of requirements due to the varying nature of organisational requirements. The requirements may be different for every organisation and even the same organisation over time due to factors such as changes in the level of information management maturity. The proposed Hybrid Approach shows how to develop new ATs by combining the activities from existing techniques in a way that meets differing requirements whilst still retaining the best practice concepts and ideas inherent in the existing ATs. It also shows what activities can be omitted and carried out in parallel, even when activities have been combined from different existing ATs and no AT describes all the activities and how they should be combined. For the DQ assessment, this affords savings in costs, time and resources which organisations are constantly striving to contain.

From an academic perspective, this work is a step towards identifying the fundamental activities required for a DQ assessment. This is an important contribution because it is easy to develop new ATs that are suitable for a particular application, but not so easy to identify whether a new AT is really needed for the new application and what components need to be specialised. Numerous ATs have already been developed with each giving their own perspective on the problem of assessing DQ. From one point of view, it is a benefit to have many options available to the data professional, but the problem is that most are not significantly different. With a clear model of the general activities that comprise ATs provided by this research, it is possible for future developments of ATs to identify precisely how they are different and how they overlap with the existing techniques. This enables researchers to make a strong case for why a new technique is needed and exactly which parts of the technique need to be tailored, or are specific, to the particular application.

Future research is needed to validate these activities further. While the authors have taken steps to ensure that the activities are as complete and valid as possible, the DQ community as a whole and over time can provide the strongest validation. Further organisational trials will also help to ensure the validity of the process. However, perhaps the most important area of future work is in using the model of activities and taking other steps to ensure that new ATs are not produced without good reason. This holds true not just for ATs, but also for other DQ artefacts, such as DQ related maturity models (of which, in the DQ domain there are many in use or in development). If we are to avoid ‘‘technique overload’’, the DQ community needs works similar to this research that enable researchers to build from a single base and clearly explicate how their new proposal differs and extends previous work.

## Acknowledgements

We would like to thank EPSRC (Grant EP/G038171/1) for supporting this research and Ulrich Saiger for conducting some of the DQ assessments. We also thank London Underground for their assistance with the DQ assessment.

## Appendix A. Explanations for the order of activities

See Table 6.

Table 6  
Ordering of the activities with explanations.

<table><tr><td>Main activity</td><td>Activities which also need to be placed in the AT before the main activity</td><td>Reason</td></tr><tr><td>Com.</td><td>-</td><td>This can be done at any point in the AT to keep people informed of progress</td></tr><tr><td rowspan="2">Analysis</td><td>Measure</td><td>It is only possible to analyse results after the results have been obtained from performing the measurements</td></tr><tr><td>Measure and Reqs.</td><td>The DQ requirements can be compared to the values from the measurement in the analysis stage</td></tr><tr><td>Group</td><td>Data items</td><td>To determine related data items and groupings, the initial set of data items being used for the assessment is needed</td></tr><tr><td rowspan="2">Dims.</td><td>Probs. (trial)</td><td>The dimensions can be selected which are relevant to the DQ problems identified</td></tr><tr><td>Data items, or Group</td><td>The dimensions can be selected that are relevant to the selected set of data items (or group of data items)</td></tr><tr><td rowspan="3">Metrics</td><td>Dims.</td><td>The metrics are developed from each selected dimension because the dimensions define what needs to be measured</td></tr><tr><td>Profile</td><td>Results from data profiling can indicate the types, ranges and distribution of data values, which can help with developing metrics that need to inspect these values</td></tr><tr><td>Meta</td><td>Meta data can be used to help develop the metrics</td></tr><tr><td rowspan="2">Ref. data</td><td>Data items or Group</td><td>The reference data must be associated with the particular data items or group of data items that need to be checked</td></tr><tr><td>Metrics</td><td>The metrics show whether reference data is needed as input to the metrics. (This was a finding from the LUL study)</td></tr><tr><td rowspan="3">Measure</td><td>Metrics</td><td>The measurement is carried out for each identified metric.</td></tr><tr><td>Ref. data</td><td>The reference data may be needed as input to metrics that are being measured.</td></tr><tr><td>Process</td><td>The measurement could focus on obtaining measurements for data items in the selected process(es).</td></tr><tr><td rowspan="4">Data items</td><td>Costs</td><td>The financial impact of DQ for different sets of data needs to be known before selecting data items if the assessment focuses on reducing financial losses caused by DQ problems</td></tr><tr><td>None</td><td>This can be the first activity</td></tr><tr><td>Probs.</td><td>Data items that are relevant to the organisational problems can be selected</td></tr><tr><td>Process (trial)</td><td>Data items can be selected that are used in the selected processes</td></tr><tr><td rowspan="2">Process</td><td>Model</td><td>The model can be used to provide information on where data is likely to be poor quality and the processes related to these areas can be selected</td></tr><tr><td>Group or Data items</td><td>Processes that use and require the previously identified data items should be selected. If the data items have been grouped, then the Group activity provides the input rather than the Data items activity</td></tr><tr><td>Meta</td><td>Data items or Group</td><td>Knowing which data items (or group of data items) are being assessed will help reduce the scope of gathering meta data (only meta data about the relevant data items needs to be gathered)</td></tr><tr><td>Profile</td><td>Data items or Group</td><td>Profiling is done for a specific set of data items (or group of data items)</td></tr><tr><td>Val. metrics</td><td>Measure</td><td>To validate the metrics e.g. check for false positives and false negatives etc. it is necessary to have first performed a measurement and review the results of the application of the metrics.</td></tr><tr><td rowspan="2">Expose</td><td>Probs.</td><td>The best way to gain management support is to show how each identified problem affects the organisation</td></tr><tr><td>Costs</td><td>Demonstrating the financial impact of the DQ problems is a good way to gain management support</td></tr><tr><td rowspan="2">Place</td><td>Data items or Group</td><td>It is necessary to know what data items (or group of data items) need to be measured before determining where they will be measured</td></tr><tr><td>Model (confirmed in AT used for evaluation)</td><td>The model can be used to identify relevant places in the flow of data that can be used to obtain the measurements.</td></tr></table>

## Appendix B. Ordering for the variable activities

See Tables 7–11.

Table 7  
Placement options for the Probs. activity.

<table><tr><td>Main activity</td><td colspan="2">Probs.</td></tr><tr><td>Activity</td><td>Position</td><td>Comments</td></tr><tr><td>Process</td><td>Before</td><td>The people that are associated with the selected processes can help with identifying the DQ problems</td></tr><tr><td>None</td><td>Before</td><td>It is useful to start the assessment with an initial understanding of current organisational DQ problems</td></tr><tr><td>Measure</td><td>After</td><td>It does not make sense to identify suspected DQ problems after a full measurement process has indicated the actual DQ problems</td></tr><tr><td>Expose</td><td>After</td><td>One way to gain management support is to show how each identified DQ problem affects the organisation. (Probs. must be placed before Expose.)</td></tr><tr><td>Dims., Data items or Group</td><td>After</td><td>The dimensions, data items (or group of data items) can be selected for the assessment that are relevant to the DQ problems identified</td></tr><tr><td>Costs*, Reqs.*, Model*</td><td>After</td><td>*See Probs. in the Costs, Reqs. and Model tables</td></tr></table>

Table 8  
Placement options for the Reqs. activity.

<table><tr><td>Main activity</td><td colspan="2">Reqs.</td></tr><tr><td>Activity</td><td>Position</td><td>Comments</td></tr><tr><td>Probs.,</td><td>Before</td><td>The requirements should be relevant to the organisational DQ problems</td></tr><tr><td>Data items or Group, Process</td><td>Before</td><td>The requirements should be specified for the selected data items (or group of data items) and processes where, for example, the people associated with the processes can help specify the requirements</td></tr><tr><td>Measure</td><td>Before</td><td>DQ requirements can be specified for each DQ problem identified from the measurement</td></tr><tr><td>Costs</td><td>Before</td><td>An understanding of costs can be used to set realistic DQ requirements that are feasible to achieve</td></tr><tr><td>Model*</td><td>After</td><td>* See Reqs. in the Model table</td></tr></table>

Table 9  
Placement options for the process activity.

<table><tr><td>Main activity</td><td colspan="2">Process</td></tr><tr><td>Activity</td><td>Position</td><td>Comments</td></tr><tr><td>Data items or Group</td><td>Before</td><td>Processes that use and require the previously identified data items (or group of data items) can be selected</td></tr></table>

Table 9 (Continued )

<table><tr><td>Main activity</td><td colspan="2">Process</td></tr><tr><td>Activity</td><td>Position</td><td>Comments</td></tr><tr><td>Model</td><td>Before</td><td>The model can be used to provide information on where data is likely to be poor quality and the processes related to these areas can be selected</td></tr><tr><td>Data items or Group</td><td>After</td><td>Data items can be selected that are used in the selected processes</td></tr></table>

Table 10  
Placement options for the Costs Activity.

<table><tr><td>Main activity</td><td colspan="2">Costs</td></tr><tr><td>Activity</td><td>Position</td><td>Comments</td></tr><tr><td>Probs.,</td><td>Before</td><td>Organisational problems have an associated financial loss and therefore should be identified before identifying DQ costs. (Either Probs., Measure or Analysis is necessary for Costs, i.e., must be placed before)</td></tr><tr><td>Measure or Analysis</td><td>Before</td><td>The financial impact of the actual DQ problems found in the measurement process (or subsequent analysis) can be determined. (Either Probs., Measure or Analysis is necessary for Costs, i.e. must be placed before)</td></tr><tr><td>Model</td><td>Before</td><td>The model can be used to identify particular transactions/processes that are affected by the DQ problems and the financial impact of the failed transaction/process.</td></tr><tr><td>Data items</td><td>After</td><td>It is possible to drive the selection of data items by first identifying financial losses caused by DQ and then selecting the data items that are relevant to these losses.</td></tr><tr><td>Reqs.*</td><td>After</td><td>*See Costs in the Reqs. table</td></tr><tr><td>Expose</td><td>After</td><td>Demonstrating the financial impact of the DQ problems is a good way to gain management support.</td></tr></table>

Table 11  
Placement options for the Model Activity.

<table><tr><td>Main activity</td><td colspan="2">Model</td></tr><tr><td>Activity</td><td>Position</td><td>Comments</td></tr><tr><td>Data items or group</td><td>Before</td><td>The model can focus on the selected data items (or group of data items) rather than all possible data items in the organisation to reduce the scope of the modelling.</td></tr><tr><td>Reqs.</td><td>Before</td><td>If the intent is to add the DQ requirements to the model, then the requirements need to have been gathered before modelling.</td></tr><tr><td>None</td><td>Before</td><td>An assessment project that is not overly time-constrained can conduct the modelling activity first and use it to identify likely areas containing DQ problems. Modelling first, without any information to reduce the scope, can be very time-consuming.</td></tr><tr><td>Probs.</td><td>Before</td><td>The modelling task can be limited to the areas that relate to the DQ problems previously identified. Modelling is therefore more focussed and faster to complete compared to attempting to model all information flows.</td></tr><tr><td>Measure</td><td>After</td><td>The model is used to identify areas that need to be subject to DQ measurements and therefore needs to be conducted before the measurement process.</td></tr><tr><td>Process*</td><td>After</td><td>*See Model in the Process Table</td></tr><tr><td>Place</td><td>After</td><td>The model can be used to identify relevant places in the flow of data that can be used to obtain the measurements.</td></tr></table>

## References

[1] D. Ballou, G. Tayi, Enhancing data quality in data warehouse environments Communications of the ACM 42, 1999, pp. 73–78.

[2] D. Ballou, H. Pazer, Modeling data and process quality in multi-input, multi output information systems, Management Science 31, 1985, pp. 150–162.

[3] C. Batini, M. Scannapieco, Data Quality: Concepts, Methodologies and Techniques first ed., Springer-Verlag, Inc., New York/Secaucus, NJ, USA, 2006.

[4] C. Batini, F. Cabitza, C. Cappiello, C. Francalanci, A comprehensive data quality methodology for web and structured data, International Journal of Innovative Computing Applications 1, 2008, pp. 205–218.

[5] C. Batini, C. Cappiello, C. Francalanci, A. Maurino, Methodologies for data quality assessment and improvement, ACM Computing Surveys 41, 2009, pp. 1–52.

[6] I. Caballero, E. Verbo, C. Calero, M. Piattini, MMPRO a methodology based on ISO/ IEC 15939 to draw up data quality measurement processes, The 13th Interna tional Conference on Information Quality, 2008.

[7] L. English, Improving Data Warehouse and Business Information Quality: Methods for Reducing Costs and Increasing Profits, John Wiley & Sons, New York, 1999.

[8] L. English, Information Quality Applied: Best Practices for Improving Business Information, Processes and Systems. John Wiley & Sons, Indianapolis, Indiana USA, 2009.

[9] C. Fisher, B. Kingma, Criticality of data quality as exemplified in two disasters Information & Management 39, 2001, pp. 109–116.

[10] B. Kitchenham, S. Linkman, S. Linkman, Experiences of using an evaluation framework, Information and Software Technology 47, 2005, pp. 761–774.

[11] Y.W. Lee, D.M. Strong, B.K. Kahn, R.Y. Wang, AIMQ. A methodology for information quality assessment, Information & Management 40, 2002, pp. 133–146.

[12] D. Loshin, Enterprise Knowledge Management: The Data Quality Approach Morgan Kaufmann Publications, San Francisco, California, USA, 2001.

[13] D. Loshin, The Practitioner’s Guide to Data Quality Improvement, Morgan Kaufmann, Burlington, Massachusetts, USA, 2011.

[14] A. Maydanchik, Data Quality Assessment, Technics Publications LLC, Bradley Beach, New Jersey, USA, 2007.

[15] D. McGilvray, Executing Data Quality Projects: Ten Steps to Quality Data and Trusted Information, Morgan Kaufmann, Burlington, Massachusetts, USA, 2008.

[16] J.M. Pearson, C.S. McCahon, R.T. Hightower, Total quality management. Are information systems managers ready? Information & Management 29, 1995, pp. 251–263.

[17] L.L. Pipino, Y.W. Lee, R.Y. Wang, Data quality assessment, Communications of the ACM 45, 2002, pp. 211–218.

[18] R.Y. Wang, A product perspective on total data quality management, Communications of the ACM 41, 1998, pp. 58–65.

[19] R.Y. Wang, D.M. Strong, Beyond accuracy what data quality means to data consumers, Journal of Management Information Systems 12, 1996, pp. 5–34.

[20] P. Woodall, A. Parlikad, A hybrid approach to assessing data quality, Proceedings of the 2010 International Conference on Information Quality 2010.

[21] P. Woodall, A.K. Parlikad, L. Lebrun, Approaches to information quality management: state of the practice of UK asset intensive organizations, Engineering Asset Management Review 2. 2013

![](/api/attachments/CQ2674RG/fulltext/images/e19fdf01606dabf96c5cf3c64b0fd644307d5cd972a772f1909cb5ccddb320e8.jpg)

Dr Philip Woodall is a research scientist at the University of Cambridge specialising in information management. He has extensive experience working with international public and private organisations from various sectors, including transport, utilities, defence, public sector, manufacturing, and aerospace, to improve their information management and information quality practices.

He has published numerous academic articles in leading international journals and conferences, and is an editor of The International Journal of Information Quality. In 2011, he was elected as the Chairman the IET Asset Management conference in London, after having worked on information quality with several asset management organisations. Philip also advises the UK government and leading business organisations on data management issues within the University of Cambridge Centre for Science and Policy, and is a proud member of St Edmund’s College, Cambridge.

Previously, he worked in the software industry and gained his Ph.D. in Computer Science from Keele University.

![](/api/attachments/CQ2674RG/fulltext/images/d00a0327863f90def1abe297ed168d1a3d3b01d29c106f8b4ff24a0671746ea0.jpg)

Dr. Alexander Borek is a leading expert in applying risk management principles to data management. He is the book author of Total Information Risk Management: Maximizing the Value of Data and Information Assets (Morgan Kaufmann 2013). Dr. Borek has published 12 peer-reviewed research articles and is frequent speaker at international conferences (such as DGIQ, DMIQ, ECIS, ICIQ) covering a range of topics, including EIM, data quality, crowd sourcing and IT business value. In his current role as Senior Strategy Consultant at IBM, Dr. Borek applies data analytics to drive IBM’s world-wide sales strategy. Previously, he led a team at the University of Cambridge to develop the Total Informa tion Risk Management process, working with a number of industrial partners. He holds a Ph.D. in Engineering from the University of Cambridge.

![](/api/attachments/CQ2674RG/fulltext/images/1af6ea7702e9e52c2a777c5fc5ac97cda4adce2c621d93a0f681848dd92d354c.jpg)

Dr Ajith Kumar Parlikad is a Lecturer at the University of Cambridge and the Deputy Director of the Distributed Information and Automation Lab at the Institute for Manufacturing. His research interests lie primarily in industrial asset management and maintenance. His particular focus is examining how asset information can be used to improve asset performance through effective decision-making. He is a member of the IET/IAM TPN Committee on Asset Management and member of the IFAC Working Group on "Advanced Maintenance Engineering, Services and Technology"
