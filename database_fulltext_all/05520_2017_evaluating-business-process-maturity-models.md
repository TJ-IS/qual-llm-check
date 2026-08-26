---
otero_id: 5520
otero_key: "ZZRNMAD4"
title: "Evaluating Business Process Maturity Models"
authors: "Amy Looy; Geert Poels; Monique Snoeck"
year: "2017"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00460"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
6-28-2017

# Evaluating Business Process Maturity Models

Amy Van Looy , Amy.VanLooy@UGent.be

Geert Poels

, Geert.Poels@UGent.be

Monique Snoeck

, monique.snoeck@kuleuven.be

Follow this and additional works at: https://aisel.aisnet.org/jais

Research Paper

ISSN: 1536-9323

# Evaluating Business Process Maturity Models

Amy Van Looy Ghent University, Belgium Amy.VanLooy@UGent.be

Geert Poels Ghent University, Belgium

Monique Snoeck K.U. Leuven, Belgium

## Abstract:

Maturity models have become important aids to support process improvement. However, researchers have frequently criticized the many business process maturity models (BPMMs) for differing in quality, which creates a demand for comparing and evaluating these models. This paper describes a well-founded, ranked, and weighted set of critical criteria for BPMMs that are most important to prospective users. The paper also demonstrates how this set can serve as a standard or guideline for designing BPMMs. In evaluating the used sample of BPMMs against the set of criteria, we reveal gaps and shortcomings of current BPMMs, make suggestions for raising the quality of BPMMs, and highlight future research avenues.

Keywords: Analytical Hierarchy Process, Content Analysis, Delphi Technique, Design Science, Evaluation Study, Maturity Model, Process Improvement, Trade-offs.

## 1 Introduction

In this paper, we investigate maturity models for business processes and business process management (BPM) in general, a topic that has received considerable attention mainly in practitioner (but less so academic) literature from the 2000s. In particular, business process maturity models (BPMMs) have become real assets for organizations to increase business (process) performance (Dijkman, Lammers, & de Jong, 2015; McCormack & Johnson, 2001; Skrinjar, Bosilj-Vuksic, & Stemberger, 2008). BPMMs originate from quality control models (Crosby, 1979), which have been adapted for software processes (e.g., CMM, CMMI) (Ahern, Clouse, & Turner, 2004) and afterwards business processes and BPM. Their practical relevance is widely recognized (Harmon, 2013; Harmon & Wolf, 2014) because improving business processes (or the organizational way of working) increases in importance due to globalization, compliance requirements, IT opportunities, outsourcing, and so on (Harrington, 2006; vom Brocke & Rosemann, 2010). In response to this high demand (Harmon, 2013; Harmon & Wolf, 2014), many scholars, institutions, and consultancy firms have developed a BPMM. Although we lack concrete numbers, estimates mention more than 200 process improvement frameworks (among others BPMMs and standards) (Curtis & Alden, 2007; El Emam & Birk, 2000) or over 150 BPMMs that address one or more BPM areas (de Bruin and Rosemann, 2007). Inspired by Sheard (2001), we may accurately refer to this situation as a quagmire in which practitioners tend to drown. Examples of BPMMs that are frequently cited in the literature include CMMI (Ahern et al., 2004; SEI, 2009), OMG (2008), the models of de Bruin and Rosemann (2007), Hammer (2007), Harrington (2006), and McCormack and Johnson (2001). We illustrate the notion of business process maturity via the maturity levels of OMG (2008), which concerns a generic BPMM that follows the CMMI tradition and is supported by a large industry consortium (Curtis & Alden, 2007). OMG’s maturity levels range from 1) initial or ad hoc practices to 2) managed, departmental practices, 3) standardized, end-to-end practices, 4) predictable or quantitatively managed practices, and 5) innovating practices.

Notwithstanding the high demand for BPMMs (Harmon, 2013; Harmon & Wolf, 2014) and the many BPMMs nowadays (Sheard, 2001; de Bruin & Rosemann, 2007), few studies have taken the point of view of prospective users who face the challenge of evaluating and selecting one out of many BPMMs for their organization. Instead, the literature on BPMMs focuses mainly on the perspective on how one should design maturity models (Becker, Knackstedt & Pöppelbuss, 2009; Maier, Moultrie, & Clarkson, 2012) or on authors who design a particular BPMM (de Bruin & Rosemann, 2007). The literature still lacks a set of general selection criteria for BPMMs that transcends the needs of a particular organization to evaluate the strengths and weaknesses in the many BPMMs today. The latter is of paramount importance because maturity models are typically criticized for oversimplifying the complex reality and for differing in quality (Röglinger et al., 2012; Maier et al., 2009). Yet, the perceived utility of BPMMs in industry is high (Harmon, 2013; Harmon & Wolf, 2014), and scholars have empirically demonstrated a positive relationship between business process maturity and business performance (McCormack & Johnson, 2001; Skrinjar et al., 2008). A set of general selection criteria would not only address a contemporary business problem but also have the opportunity to shed more light on BPMM designs by adding the missing angle of prospective users.

To fill this gap, we develop a set of critical factors or criteria for selecting a BPMM, examine the relative importance of the different criteria, and evaluate existing BPMMs against this set. As such, we investigate two research questions to introduce a user perspective to BPMM research, which currently focuses only on the designer perspective:

RQ1: Which criteria are most relevant for BPMM selection, and what is their relative importance?

RQ2: How can one evaluate current BPMMs against these selection criteria?

The corresponding research objectives are to:

Develop a comprehensive, ranked, and weighted set of selection criteria for BPMMs that are not specific to any organization.

• Evaluate existing BPMMs against this set of selection criteria.

This study introduces the notion of quality of BPMMs from a user perspective as meeting end user expectations and evaluates the extent to which a representative sample of 69 BPMMs meets the identified selection criteria. By investigating the research questions, we provide evidence of the varying quality among BPMMs without, however, focusing on individual BPMMs. Our user perspective complements the designer perspective in BPMM research because the absence of certain model characteristics that users need to evaluate BPMMs may inform proposals for improving model designs. One can characterize our empirical and interpretive study as a meta-study (Bostrom, Gupta & Thomas, 2009; Zhao, 1991) because we generalize differences between BPMMs based on an in-depth analysis and discussion. We do so by synthesizing knowledge of current BPMMs, detecting areas for improvement, and laying a foundation for further BPMM research based on the identified shortcomings. Thus, this paper makes a novel academic contribution as both the BPMM literature and particular models could benefit from issues about relevant variances of BPMMs.

This paper proceeds as follows: in Section 2, we review the research on maturity models. In Section 3, we describe the research methods. In the subsequent sections, we present our data analysis and results. In particular, in Section 4, we explore the initial criteria for BPMM selection and, in Section 5, work towards a ranked and weighted set of criteria. In Section 6, we apply the findings to existing BPMMs in order to conduct a quality check on their coverage of elements required to evaluate the identified selection criteria. In Section 7, we discuss the results and presents research implications and, in Section 8, conclude the paper.

## 2 Literature review

Although the number of academic publications on maturity models is reasonable (i.e., about 332 papers in the Web of Science until 2015), only a small subset of this literature addresses maturity models for business processes. These papers mostly focus on particular maturity models (e.g., for project management, knowledge management, business-IT alignment, or specific process types such as software processes) or on model development (see next paragraphs). Papers that report on maturity model evaluation address the validation or application of a particular maturity model in a specific situation and assess or evaluate the application results rather than compare them with or check their quality against existing maturity models (as we target in this study). Similarly, previous studies use the term “selection” to refer to the choice of specific application areas or case situations rather than the choice for one or another maturity model (which is the user perspective we address in our study). Thus, the academic literature on the evaluation or selection of BPMMs is still very scarce. While Wendler (2012) confirms that especially reflective publications with theoretical implications on maturity models are scarce and a gap exists in evaluating those models, her literature review is not specific to BPMMs nor to the perspective of prospective model users. Further, Van Looy, De Backer, Poels and Snoeck (2013) present a decision tool for selecting one BPMM out of a large sample of existing BPMMs but do not generalize the substantial differences between these BPMMs as we focus on in this study.

Röglinger, Pöppelbuss, and Becker (2012) propose design criteria specifically for BPMMs and present a limited BPMM comparison but do not give advice on how to choose a BPMM that fits a particular organization. Mettler (2009) offers a first attempt to translate design criteria into a user perspective by considering maturity models in general (i.e., independent of the specific business process context) and without evaluating existing maturity models. Similar to Mettler (2009), it is interesting to look at the design science literature and verify the extent to which one can translate the design criteria for BPMMs to a user perspective.

Particularly, one can build and test maturity models by following a specific design research cycle (Becker et al., 2009; Mettler & Rohner, 2009) in which each phase should meet specific evaluation guidelines (Becker et al., 2009; Hevner, March, Park, and Ram, 2004). Referring to March and Smith’s (1995) categorization of design artifacts, Mettler and Rohner (2009) and Donnellan and Helfert (2010) conclude that maturity models generally offer models (e.g., maturity levels), methods (e.g., best practices to achieve higher levels) and instantiations (e.g., documents or websites for organizations to use). Nonetheless, the literature still lacks a common conceptualization with constructs for designing maturity models in general and BPMMs in particular (Mettler & Rohner, 2009).

In order to learn more about the constructs that typify maturity models, we launched a search query by combining the keywords “maturity model” and “design science” in 2011. Because the few resulting papers in the Web of Science database mainly involved specific maturity models (except for Becker et al., 2009; Tapia, Daneva, van Eck, & Wieringa, 2008; van Steenbergen, Bos, Brinkkemper, van de Weerd, & Bekkers, 2010), we did a similar search in Google Scholar in order to find more relevant studies (de Bruin et al., 2005; Maier et al., 2009; Mettler et al., 2009). We analyzed the resulting papers via a content analysis that focused on finding common elements or characteristics in the design of maturity models (see Table 1).

Table 1. Common Elements in the Design of Maturity Models (Until 2011—Before Our Study)

<table><tr><td></td><td>Becker et al. (2009)</td><td>de Bruin, Freeze, Kulkarni, &amp; Rosemann (2005)</td><td>Maier, Moultrie, &amp; Clarkson (2009)</td><td>Mettler &amp; Rohner (2009)</td><td>Tapia et al. (2008)</td><td>van Steenbergen et al. (2010)</td></tr><tr><td colspan="7">Assessors (Who)</td></tr><tr><td>* Lead assessor</td><td>X</td><td>X</td><td>X</td><td>-</td><td>X</td><td>X</td></tr><tr><td>* Other assessors and respondents</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td colspan="7">Assessment method (How)</td></tr><tr><td>* Data-collection technique to obtain information to assess</td><td>X</td><td>X</td><td>X</td><td>X</td><td>-</td><td>X</td></tr><tr><td>* Calculation to interpret the collected data as lifecycle levels</td><td>X</td><td>X</td><td>X</td><td>-</td><td>X</td><td>X</td></tr><tr><td>* Representation to visualize lifecycle levels</td><td>-</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td colspan="7">Improvement method (What)</td></tr><tr><td>* Capability areas to be assessed and improved</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>* Lifecycle levels</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>* Architecture (i.e., road map or improvement path) to link capability areas to levels by step-by-step improvements</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr></table>

Table 1 shows that three original groups of functionalities seem to be present in maturity model design (Becker et al., 2009; de Bruin et al., 2005; Maier et al., 2009; Mettler et al., 2009; Tapia et al., 2008; van Steenbergen et al., 2010). In particular, Table 1 reveals that a maturity model may act as an assessment method and an improvement method and that it may involve elements referring to the assessors as a third group. This third original group (“assessors”) covers all design elements related to who measures maturity, while the “assessment method” specifies how maturity is measured (e.g., how data is collected and analyzed) and the “improvement method” groups elements describing what is measured as maturity (e.g., the capability areas and their improvements necessary to reach each the consecutive level).

Since the papers in Table 1 are not specific to the context of a BPMM, we verified the extent to which the common design elements and original groups of functionalities are mentioned in the definition of a BPMM. Therefore, we relied on a comprehensive definition that we derived from Van Looy, De Backer and Poels (2011, pp. 1132-1133) who compare current BPMM definitions and, as a result, define a BPMM as:

A model to assess and/or to guide best practice improvements in organizational maturity and process capability, expressed in lifecycle levels, by taking into account an evolutionary road map regarding (1) process modeling, (2) process deployment, (3) process optimization, (4) process management, (5) the organizational culture, and/or (6) the organizational structure.

This BPMM definition defines a BPMM as an assessment method (i.e., “to assess”) and/or as an improvement method (“to guide best practice improvements”): two important BPMM functionalities. The specification of the six elements in the definition (i.e., process modeling, deployment, optimization, management, culture and/or structure) is a translation of the capability areas that a BPMM will assess and improve. Furthermore, the keywords in this definition, such as “maturity lifecycle levels” and “capability lifecycle levels”, may serve as major constructs in a common conceptualization for BPMMs.

Despite the fact that most of the papers in Table 1 mention the identified common elements and that Van Looy, De Backer and Poels (2011, pp. 1132-1133) address some of them in their definition for BPMM, none detail all common design elements in concrete options nor translate them to the BPMM context. This paper takes the perspective of prospective model users, as a new angle in the literature, to develop such conceptualization required to compare and evaluate different BPMMs and to identify strengths and weaknesses in existing BPMMs.

## 3 Research Method

We present a meta-study (Bostrom et al., 2009; Zhao, 1991) by producing detailed and standardized constructs, which allows one to objectively compare and evaluate existing BPMMs. A meta-study typically examines a particular problem encountered in a discipline, such as the increasing number of BPMMs without evaluation from a user perspective, and ends with prescriptions for resolving the problem. More specifically, the paper concerns a meta-data-analysis because it is based on empirical research for the purpose of understanding and integrating the findings (Zhao, 1991).

Figure 1 summarizes our overall approach and indicates the different research phases with inputs and outputs.

![](/api/attachments/ZZRNMAD4/fulltext/images/e49a54ad8f1ab10a1cd95cc8c3ab529e11bac1676f32df4f03c1da3d6beca7c4.jpg)  
Figure 1. The Research Approach for this Paper

In particular, our research approach combined recognized methods (i.e., grounded theory and the Delphi technique) in order to drive research rigor. First, we used a grounded theory study (Glaser & Strauss, 1967) to explore the problem situation. In doing so, we focused on thoroughly familiarizing ourselves with the phenomenon of interest. Further on, we conducted a Delphi study (Dalkey & Helmer, 1963) that we extended with the analytical hierarchy process (AHP) (Saaty, 1990) for problem solving. More specifically, by conducting the Delphi study, we could identify the most important (i.e., ranked and weighted) criteria for BPMM selection based on consensus-seeking and multi-criteria decision making (RQ1). In order to respond to RQ2, we evaluated a sample of BPMMs against this general set of selection criteria (i.e., with a case-independent ranking and weights) to shed light on the degree to which one can apply these criteria to current BPMMs.

## 3.1 Grounded Theory Study

We conducted a content analysis of existing BPMMs in line with grounded theory (Glaser & Strauss, 1967) since the literature we review in Section 2 largely focuses on maturity models in general and since few papers address maturity models for business processes in particular. Moreover, with this way of working, we could specify the concrete options per common design element. We analyzed the descriptions in the available documentation (i.e., manuals or descriptive documents) of a representative sample of 69 BPMMs (Van Looy, De Backer, Poels & Snoeck, 2013). Thirty-two of these BPMMs address specific process types (24 for supply chains and eight for collaboration processes to include end-to-end value chains), whereas 37 BPMMs are generic and can be applied to any process type. We identified the BPMMs in this sample by searching in the Web of Science, Business Process Management Journal, the Google and Google Scholar search engines with the combined keywords of “process” and “maturity”. Further, we traced the references in the identified papers for other relevant sources (i.e., a snowballing search strategy). We included models if they: 1) contained maturity levels and/or capability levels and 2)

primarily focused on improving generic business processes, supply chains, or collaboration processes instead of other organizational assets. We conducted the sampling in 2010 and confirmed its comprehensiveness in 2012 when a resampling effort did not result in additional BPMMs (taking into account some limitations regarding the accessibility of documents, the language, and the keywords). By including different process types (i.e., generic, supply chains, and collaboration), the sample suggests versatility to transfer the findings to other process types (e.g., software processes).

Conforming to grounded theory’s terminology (Glaser & Strauss, 1967), we analyzed the existing BPMMs to identify model characteristics as possible selection criteria and options (i.e., values per criterion) through three coding stages: 1) initial (open) coding, 2) intermediate (axial) coding, and 3) advanced (selective) coding. Table 2 shows a coding example to illustrate how an extract from BPMM descriptions led to the induction of a pattern; the codes represent possible selection criteria with different options.

Table 2. A Coding Example

<table><tr><td>Extract from BPMM descriptions</td><td>Codes</td></tr><tr><td>“ Conformance with the BPMM is evaluated in appraisals led by an authorized Lead Appraiser, who has been trained extensively.”</td><td>[Assessment][Assessor type – lead assessor][Training]</td></tr><tr><td>“ Conformance is evaluated by using the following forms of evidence: review of artifacts, interviews, and quantitative data describing the performance of a process, its outcomes, and business results.”</td><td>[Data-collection techniques – document review][Data-collection techniques – interview][Rating scale – qualitative data][Rating scale – quantitative data]</td></tr></table>

First, during initial (open) coding, we read the collected documentation of existing BPMMs by going back and forth to identify possible criteria and options. For instance, different BPMMs mentioned that one can measure maturity by collecting data from document reviews, questionnaires, interviews, focus groups, or observations. We grouped these different options in a criterion that refers to “data-collection techniques”. As another example, different BPMMs presented information on the assessment items that they use to collect data (i.e., open questions or questions with nominal, ordinal, discrete, interval, and ratio scales). Hence, we coded “rating scale” as another possible criterion. After this stage, in the Delphi study, we started to discuss and find potential criteria and options.

Second, during intermediate (axial) coding, we reconsidered the criteria and options obtained through the initial coding based on the feedback from the Delphi study and linked them to the common design elements of maturity models (Section 2). For instance, we linked the criterion “data-collection techniques” to the assessment method and changed it to “objective” and “subjective” data-collection techniques. Also, we linked the criterion “rating scale” to the assessment method and changed it to “qualitative” data and “quantitative” data.

Afterwards, during advanced (selective) coding, we reread the documentation of existing BPMMs to record how these models actually cover the identified criteria and options. We note that we executed this final coding stage once we had obtained the final set of selection criteria in the Delphi study.

## 3.2 Delphi Study

During the Delphi study, we validated and extended the set of criteria from the first research phase in order to obtain a comprehensive, ranked, and weighted set of selection criteria. To introduce a user perspective, we supplemented the initial criteria with criteria obtained from peer feedback at a conference on enterprise information systems and a pilot study with business process management (BPM) scholars at our faculty. Regarding the pilot, we engaged two PhD students working on BPM research to focus on formulating the criteria, whereas two BPM professors also checked for missing criteria and biases. Independent subject-matter experts reviewed the resulting set of criteria. We also asked the experts for additional criteria that are relevant for BPMM selection in an international modified Delphi study (Table 3).

Table 3. The Different Delphi Types (Based on Hasson, Keeney & McKenna, 2000)

<table><tr><td>Delphi type</td><td>Purpose</td></tr><tr><td>Classical Delphi</td><td>For consensus-building with anonymity, starting with open questions</td></tr><tr><td>Forecast Delphi</td><td>Classical Delphi to combine opinions on trends (i.e., the likelihood and time scale of developments in science, technology, business, etc.)</td></tr><tr><td>Real-time Delphi</td><td>Classical Delphi with real-time calculation and aggregation of group responses (i.e., online Delphi conference)</td></tr><tr><td>Modified Delphi</td><td>For consensus-building with anonymity, also including closed questions to orient people to the topic</td></tr><tr><td>Decision Delphi</td><td>For consensus-building on social developments with quasi-anonymity (i.e., experts are mentioned by name, but answers remain anonymous)</td></tr><tr><td>Policy Delphi</td><td>For dissensus-building with anonymity, to elicit opposing views or alternatives</td></tr></table>

A Delphi study is an established consensus-seeking decision making method that uses “a series of sequential questionnaires or rounds, interspersed by controlled feedback, that seek to gain the most reliable consensus of opinion of an expert panel” (Dalkey & Helmer, 1963, p. 458). Different types of Delphi studies exist (see Table 3). We opted for the modified Delphi approach because we included the criteria from grounded theory study to orient diverse subject-matter experts to the research topic.

In November 2011, the Delphi study started with 22 BPM experts: 11 academics and 11 practitioners from five continents. The academics had credible BPM(M) publications in academic journals, and the practitioners had experience in designing a BPMM, applying BPM(M), or were genuinely interested in BPMM selection. All practitioners were consultants or managers with decision power in large to mediumsized organizations (both profit and non-profit). The selection procedure that we applied conforms to Okoli and Pawlowski (2004): that is, we introduced different backgrounds to minimize bias and allow normative discussions. Per round, four coders (one of whom was from another university) anonymously analyzed the responses.

The coders stopped iterating a particular criterion when they reached one of the three stopping conditions (Hasson et al., 2000; Okoli & Pawlowski, 2004): 1) they reached consensus to include a criterion for BPMM selection, 2) results for the criterion became stable before reaching consensus to exclude a criterion, or 3) the majority of experts were no longer willing to continue iterating to exclude all remaining criteria. The coders defined consensus conditions on a seven-point Likert scale (Hasson et al., 2000): 1) 50 percent of the experts must agree on the two most extreme scores (i.e., 6-7), 2) 75 percent must agree on the three most extreme scores (i.e., 5-6-7), 3) the interquartile range must be 1.50 or less, and 4) no expert can give an opposite extreme score (i.e., 1). The coders measured stability with Spearman’s rho, Kendall’s tau-b, and the Cohen’s Kappa level of agreement on a recoded three-point scale to examine opinion changes (i.e., between unimportance 1-2-3, neutral 4, and importance 5-6-7).

![](/api/attachments/ZZRNMAD4/fulltext/images/fc686a01851a0dccd6c44983ca0e8d603a887c3f091e8c643072628dfe8af976.jpg)  
STEP 2. To which DEGREE is each ROW option more important than each COLUMN option for BPMM selection? (Score between 1 and 9)  
Figure 2. Extract from a Completed Delphi Questionnaire (Round 4) with Judgment Matrix

Once we elicited the selection criteria with consensus, we asked the experts to determine which were more important in pairwise comparisons. Therefore, we applied the analytical hierarchy process (AHP) (Saaty, 1990). We asked the experts to complete judgment matrices by using the typical AHP nine-point scale (1/9 = extremely less important; 1 = equally important; 9 = extremely more important) to describe how much more important each row item was compared to each column item as Figure 2 exemplifies. AHP then calculates a priority vector (or principal Eigen vector) and a consistency ratio (CR) per matrix. Afterwards, we aggregated the experts’ opinions by geometrically averaging only non-random judgments (CR ≤0.1). As such, we obtained the aggregated priorities or relative importance of selection criteria and their options.

## 3.3 Evaluation Study

Third, in the evaluation study, we focused on demonstrating the applicability of the developed set of selection criteria to compare and evaluate BPMMs via a general ranking with weights. We evaluated the set of criteria for its utility, effectiveness, and efficiency based on predefined requirements as Table 4 shows.

Table 4. The Requirements for the Developed Set of Selection Criteria for BPMMs

<table><tr><td></td><td>Requirements</td><td>Requirement satisfaction tests</td></tr><tr><td>Utility</td><td>The ranked and weighted set of selection criteria should enable one to compare and evaluate BPMMs.</td><td>• Criteria utility: based on a textual description of the selection criteria, people not involved in our research can evaluate other BPMMs than those involved in our sample. The Cohen&#x27;s Kappa represents a significant level of agreement or interrater reliability (0.4 = &lt; kappa = &lt; 1; p &lt; 0.05).• Ranking utility: based on descriptive statistics, one can generate comparative tables to visualize the weights of individual selection criteria along with the support in current BPMMs.• Clarity: in the comparative tables, one can highlight the main differences between BPMMs with respect to the ranked and weighted selection criteria.</td></tr><tr><td>Effectiveness</td><td>The ranked and weighted set of selection criteria should represent relevant BPMM characteristics that prospective BPMM users consider when selecting a BPMM.</td><td>Prospective users are satisfied with 1) the selection criteria in the developed set, 2) their descriptions of trade-offs, and 3) the sequence in which they appear based on a general ranking with weights (i.e., 50% for scores 5-6-7 on a seven-point Likert scale, and no opposite extreme score of 1).</td></tr><tr><td>Efficiency</td><td>The ranked and weighted set of selection criteria should lead one to more easily compare and evaluate BPMMs compared with an ad hoc way of working.</td><td>Based on the comparative tables, one can detect relevant differences among BPMMs by following a standard way of working.</td></tr></table>

To evaluate the applicability of the selection criteria, we evaluated existing BPMMs (i.e., input of the first research phase) against the ranked set of selection criteria for BPMMs (i.e., output of the second research phase). At the same time, this evaluation provides information about the fit of each BPMM with the selection criteria. The size of the sample (69 maturity models) allowed us to compare and evaluate a comprehensive and unique dataset and to draw general conclusions.

The fact that the same researchers performed both the Delphi study and the content analysis, introduced a danger of bias for the content analysis. To avoid biasing the content analysis with our knowledge about the ranking and weighting of the selection criteria, the researchers performed the content analysis before finalizing the Delphi study. Reversely, we kept the results from the content analysis hidden from the experts who participated in the Delphi study.

## 4 Preparatory Phase: Initial Criteria for BPMM Selection

Table 5 shows the criteria that resulted from the grounded theory study (see Section 3.1). We used these criteria as input for the Delphi study for the expert panel to determine their rank and discuss their tradeoffs. Table 5 also indicates which criteria the experts proposed in addition to the criteria that resulted from the grounded theory study (see Section 5).

Table 5. The List of all Criteria Considered in the Delphi Study

<table><tr><td>Criterion</td><td>Criterion description</td></tr><tr><td>1) Number of assessed organizations</td><td>The number of organizations (i.e., autonomous legal entities) included in the assessment.</td></tr><tr><td>2) Lead assessor</td><td>Whether an external (quasi-) independent person (i.e., third party) led the assessment.</td></tr><tr><td>3) Number of assessors</td><td>The number of assessors who are required to conduct an assessment.</td></tr><tr><td>4) Functional role of respondents</td><td>The explicit recognition to include people from outside the assessed organizations as respondents.</td></tr><tr><td>5) Business versus IT respondents</td><td>The explicit recognition to include IT people and/or business people as respondents in the assessment.</td></tr><tr><td>6) Data-collection technique</td><td>The way information is collected during an assessment.</td></tr><tr><td>7) Number of assessment items</td><td>The maximal number of questions to be answered during an assessment.</td></tr><tr><td>8) Assessment duration</td><td>The maximal duration of a particular assessment.</td></tr><tr><td>(9) Rating scale</td><td>The type of data collected during an assessment.</td></tr><tr><td>10) Presence of capabilities</td><td>The capabilities to be assessed and improved.</td></tr><tr><td>11) Number of business processes</td><td>The number of business processes to be assessed and improved: 1) one, 2) more, or 3) all.</td></tr><tr><td>12) Type of business processes</td><td>Whether the BPMM is generic (i.e., for business processes in general) or domain specific (e.g., for business processes in supply chains or collaboration situations).</td></tr><tr><td>13) Architecture type</td><td>The possibility to define a road map per capability, a road map for overall maturity, or both (i.e., a staged architecture with maturity levels and/or a continuous architecture with capability levels).</td></tr><tr><td>14) Number of lifecycle levels (i.e., maturity levels or capability levels)</td><td>The number of maturity levels or capability levels that are defined.</td></tr><tr><td>15) Level calculation</td><td>The way the resulting maturity levels or capability levels are calculated.</td></tr><tr><td>16) Level representation</td><td>The way the resulting maturity levels or capability levels are displayed.</td></tr><tr><td>17) Labeling of levels</td><td>The way maturity levels or capability levels are labelled (i.e., what they indicate or explicitly refer to).</td></tr><tr><td>18) External view of levels</td><td>The extent to which maturity levels or capability levels consider possible relationships between individual organizations.</td></tr><tr><td>19) Architecture details</td><td>The degree of guidance that a BPMM gives on one&#x27;s journey towards higher maturity (i.e., with descriptive or prescriptive improvements).</td></tr><tr><td>20) Methodology used to create a BPMM (p)</td><td>The way the BPMM was created.</td></tr><tr><td>21) Methodology used to validate a BPMM (p)</td><td>Whether or not empirical evidence is given that the BPMM helps to enhance the efficiency and effectiveness of business processes.</td></tr><tr><td>22) Direct costs to access and use a BPMM (p)</td><td>The direct costs to access and use a BPMM.</td></tr><tr><td>23) Purpose of BPMM use (*)</td><td>The purpose for which a BPMM is intended to be used (i.e., only raising awareness or also benchmarking or certification).</td></tr><tr><td>24) Assessment availability (*)</td><td>Whether the assessment questions and corresponding level calculation are publicly available (instead of only known to the assessors).</td></tr><tr><td colspan="2">* Additional criteria that the experts proposed; (p) criteria obtained from prior peer feedback and pilot study.</td></tr></table>

## 5 Intermediate Phase: Ranked and Weighted Set of BPMM Selection Criteria

In the Delphi study, we focused on building consensus in order to validate and extend the set of criteria from the first research phase. After three rounds, we stopped iterating because 75 percent of the experts indicated they were no longer willing to continue iterating (Figure 3). This is similar to other Delphi studies, which typically take three to four rounds (de Bruin & Rosemann, 2007; Hasson et al., 2000). On the right, Figure 3 shows that 14 out of 24 criteria reached consensus of being important for BPMM selection. They constitute our final set of selection criteria for BPMM. The Appendix details these selection criteria and their trade-offs (derived from the Delphi study). Other criteria had no trend towards consensus due to the condition that no expert could give an opposite extreme score in any round. In all rounds, the response rates exceeded the minimum value of 70 percent, which enhances our research’s rigor and validity (Hasson et al., 2000). Moreover, 95 percent of the respondents in the third round (N = 17) agreed that the set of final selection criteria was very to extremely important for BPMM selection (i.e., scores 6 or 7; median = 6; interquartile range = 0).

(\*) Criteria proposed by experts  
![](/api/attachments/ZZRNMAD4/fulltext/images/956d8324eba8dbc790503611393698d9c8f771cc60cebc962c923983550c5ab1.jpg)  
Figure 3. An Overview of the Criteria throughout the Consensus-seeking Delphi Rounds

We grouped and weighted the 14 selection criteria that reached consensus in a fourth Delphi round to obtain a ranked set. AHP uses a hierarchical approach to first assign weights to groups of criteria, then to the criteria per group, and afterwards to the options per criterion. In Section 2, we write that the literature on maturity models mentions three original groups: assessors, assessment method, and improvement method. Nonetheless, since most criteria regarding the assessors and respondents did not reach consensus of being most important for BPMM selection, we added the remaining criterion (i.e., functional role of the respondents) of the assessors group to the assessment method group. We justify doing so with the fact that AHP requires groups with multiple criteria and preferably of almost similar sizes to avoid a bias or overestimation. Hence, we chose the assessment method and the improvement method as possible groups for our study. We could not classify some selection criteria in the assessment method group or the improvement method group because they involved general or practical considerations of a BPMM (e.g., the costs to access and use a BPMM, or the degree to which a BPMM has been validated). The latter concern criteria that we grouped as “contextual” criteria (i.e., in the sense that they are rather model independent because they do not belong to the assessment method or improvement method of a BPMM). Hence, we grouped the remaining selection criteria as follows (Figure 4): 1) assessment method criteria (i.e., how maturity is measured and by whom), 2) improvement method criteria (i.e., what is measured as maturity, particularly the capability areas and their improvements to reach successive levels), and 3) contextual criteria (e.g., costs).

![](/api/attachments/ZZRNMAD4/fulltext/images/c3495bd7576d7778dde9ba1bee5b2fafe0e496beab797bbdeb7957f01d905975.jpg)  
Figure 4. The Hierarchical AHP Model for BPMM Selection

Figure 4 shows the resulting weights. The experts argued that the improvement method criteria should be more decisive for BPMM selection (i.e., represent a higher overall weight in Figure 4) than the assessment method criteria or the contextual criteria. This finding reflects that the levels provided by BPMMs are not an end goal but that capability improvements and performance improvements are. Similarly, organizations that merely strive for the highest (not optimal) levels misuse BPMMs (Dijkman et al., 2015; Maier et al., 2009). Hence, the capability areas criterion received the highest weight because it ultimately represents what is being measured and improved. The costs criterion received the lowest weight to avoid an organization from selecting a free model that measures the wrong scope of capabilities for that organization (and become useless as such).

In a fifth and final Delphi round, 95 percent of the respondents (N = 20) were satisfied with the obtained weights (i.e., scores 5, 6 or 7; median = 6; interquartile range = 0). Consequently, the vast majority confirmed the resulting ranking and weighting by AHP.

In the previous paragraphs, we explain how we managed the internal validity and objectivity for identifying and weighting selection criteria in the best possible way. Due to the small sample size, Delphi results cannot be repeated. Nevertheless, we ensured reliability with careful expert selection and multiple coders. In order to further enhance external validity, one could repeat our methodology (e.g., for other types of maturity models).

## 6 Advanced Phase: Evaluation of the Selection Criteria and Application to Existing BPMMs

## 6.1 Evaluation of the Selection Criteria

In the evaluation study, we focused on demonstrating the applicability of the ranked and weighted set of criteria for comparing and evaluating BPMMs based on the requirements of Table 4.

First, for evaluating the criteria utility requirement, we asked two former master’s students who recently graduated in business informatics to look for additional BPMMs by using the same search query as we describe in Section 3.1. The students were unbiased in the sense that they were unfamiliar with our research on business process maturity models and received only the list of 69 BPMMs that we previously found and used in our research. In order to control for possible biases based on the origin of maturity models, we asked one student to look for an additional BPMM in an academic database (e.g., Web of Science or Google Scholar) and the other student to search for a BPMM created by consultants and described on the Internet. Then, we asked them to individually evaluate each of the two newly found BPMMs (i.e., based on the documents found) using the descriptions of the selection criteria and their options as the Appendix provides. The students mapped both BPMMs to the criteria in a similar way for 10 out of 14 criteria for the academic model and for 12 out of 14 criteria for the non-academic model (0.4 < kappa = 0.571 < 1; p = 0.002 < 0.05), which suggests that others can repeat our way of working for other BPMMs.

Regarding the effectiveness requirement, we asked seven prospective BPMM users to rate their satisfaction with the criteria, the descriptions of trade-offs between options of criteria, and the sequence in which the criteria and their options appear (as an equivalent to the ranking and weights) on a seven-point Likert scale (1 = very dissatisfied; 7 = very satisfied). We strategically chose users to cover different business scenarios:

Four practitioners who enrolled for the BPM course of a postgraduate training program and who represented different organizational sizes (micro, small, medium, large)

Two managers who wanted to use a BPMM in their organization and who represented different organizational sectors (non-profit, private), and

• One scholar who wanted to use a BPMM in her research.

It turned out that five out of seven prospective users were satisfied with the selection criteria, their descriptions, and their sequence (i.e., scores 5, 6, or 7; median = 6; min. = 4; max. = 7). The two remaining users gave a neutral score of 4 because they deemed themselves too unexperienced as practitioners to evaluate the set of criteria, while all other prospective users gave positive scores. This finding suggests that BPMMs should rather to be used by people in managerial roles.

The other requirement satisfaction tests (i.e., for ranking utility, clarity, and efficiency) of Table 4 are demonstrated by applying the selection criteria to the sampled BPMMs (N=69), as described in the next section.

## 6.2 Application of the Selection Criteria to BPMMs

We mapped each of the BPMMs from our sample (N = 69) to the selection criteria and investigated to what extent the importance attributed to each criterion corresponds to the effective support in the BPMMs. Effective support means that current BPMMs cover the elements important to the evaluation and that missing elements correspond to what experts deem less important. As a result of this evaluation, we obtained information on the fit of the BPMMs with the selection criteria.

In this section, we review the evaluation of the BPMMs against the selection criteria. A detailed report per BPMM is out of our scope here, but we can provide it if requested.

## 6.2.1 Evaluation of BPMMs against the Assessment Method Criteria

Table 6 summarizes the results of the content analysis (i.e., last column) along the options and the weights for selection criteria pertaining to a maturity assessment. Bold text indicates the highest values for weight and number of BPMMs. We italicize the number of missing values. When the highest valued option for a criterion does not match the largest number of BPMMs that offer this option (i.e., when the bold values are not on the same row), one can uncover a quality gap for that particular criterion.

Table 6. Selection Criteria Pertaining to the Assessment Method of a BPMM

<table><tr><td>Assessment method criteria</td><td>Options</td><td>Weight (%)</td><td>Number of BPMMs (N = 69)</td></tr><tr><td rowspan="4">Rating scale</td><td>Qualitative</td><td>3.57</td><td>41</td></tr><tr><td>Quantitative</td><td>2.98</td><td>1</td></tr><tr><td>Both</td><td>7.78</td><td>14</td></tr><tr><td>(Missing value)</td><td></td><td>(13)</td></tr><tr><td rowspan="4">Data-collection technique</td><td>Objective</td><td>3.58</td><td>4</td></tr><tr><td>Subjective</td><td>2.28</td><td>41</td></tr><tr><td>Both</td><td>7.44</td><td>11</td></tr><tr><td>(Missing value)</td><td></td><td>(13)</td></tr><tr><td rowspan="4">Assessment duration</td><td>Day</td><td>1.63</td><td>18</td></tr><tr><td>Week</td><td>3.91</td><td>9</td></tr><tr><td>Longer</td><td>1.41</td><td>7</td></tr><tr><td>(Missing value)</td><td></td><td>(43)</td></tr><tr><td rowspan="4">Assessment availability</td><td>Fully known</td><td>3.82</td><td>31</td></tr><tr><td>Partially known</td><td>3.31</td><td>23</td></tr><tr><td>Fully unknown</td><td>1.27</td><td>15</td></tr><tr><td>(Missing value)</td><td></td><td>(0)</td></tr><tr><td rowspan="3">Functional role of respondents</td><td>Only internal</td><td>2.10</td><td>46</td></tr><tr><td>Also external</td><td>3.82</td><td>9</td></tr><tr><td>(Missing value)</td><td></td><td>(14)</td></tr><tr><td rowspan="6">Number of assessment items</td><td>0-19</td><td>1.66</td><td>17</td></tr><tr><td>20-49</td><td>3.69</td><td>16</td></tr><tr><td>50-99</td><td>3.10</td><td>6</td></tr><tr><td>100-299</td><td>1.34</td><td>7</td></tr><tr><td>&gt;=300</td><td>0.53</td><td>3</td></tr><tr><td>(Missing value)</td><td></td><td>(20)</td></tr></table>

For only two of the six assessment method criteria, the experts’ preferences for the different options per criterion were almost similar to what the sampled BPMMs cover (i.e., the highest values in the last two columns of Table 6 cover similar rows). These two criteria are called assessment availability and number of assessment items. They express an appreciation for the assessment availability of most BPMMs without an excessive list of assessment items. In particular, 54 out of 69 sampled BPMMs address the two highest weights for the assessment availability criterion, while almost half of the models address the highest weight of 3.82. Regarding the number of assessment items criterion, almost a third of the sampled BPMMs address the two highest weights, while the majority of the evaluated models address the three highest weights.

On the other hand, Table 6 shows that the experts preferred a combination of qualitative and quantitative scales and of objective and subjective data-collection techniques to obtain results that are closer to reality. Nevertheless, the large majority of BPMMs cover only qualitative scales with subjective techniques, which are easier for respondents to assess (e.g., the perceived instead of actual performance). Another gap concerns the expected duration of a maturity assessment. The experts preferred an assessment that takes between one day and one week because it must be seriously undertaken. On the other hand, many existing BPMMs, according to their documentation, allow one to assess a business process or a set of business processes in a single day, which responds to managers’ busy lives. We must, however, note that 43 out of 69 sampled BPMMs do not explicitly mention the expected assessment duration in their documentation, which indicates a considerable planning uncertainty for practitioners. Finally, we look at the criterion called functional role of respondents. While the large majority of BPMMs (i.e., 46 out of 69 models) are restricted to internal respondents, the experts recommended the inclusion of external respondents to allow a complete 360-degree feedback. Information from external parties may add perspectives for (future) cross-organizational collaboration and policy acceptance.

## 6.2.2 Evaluation of BPMMs against the Improvement Method Criteria

Table 7 highlights the strengths and weaknesses in actual BPMMs according to the selection criteria about the improvement method aspect.

Table 7. Selection Criteria Pertaining to the Improvement Method of a BPMM

<table><tr><td>Improvement method criteria</td><td>Options</td><td>Weight (%)</td><td>Number of BPMMs (N = 69)</td></tr><tr><td rowspan="7">Capability areas</td><td>Modeling</td><td>2.69</td><td>56</td></tr><tr><td>Deployment</td><td>2.54</td><td>68</td></tr><tr><td>Optimization</td><td>2.58</td><td>68</td></tr><tr><td>Management</td><td>4.47</td><td>67</td></tr><tr><td>Culture</td><td>2.84</td><td>57</td></tr><tr><td>Structure</td><td>1.91</td><td>30</td></tr><tr><td>(Missing value)</td><td></td><td>(0)</td></tr><tr><td rowspan="4">Architecture types</td><td>Continuous</td><td>7.28</td><td>14</td></tr><tr><td>Staged</td><td>7.50</td><td>31</td></tr><tr><td>Both</td><td>10.55</td><td>24</td></tr><tr><td>(Missing value)</td><td></td><td>(0)</td></tr><tr><td rowspan="4">Architecture details</td><td>Descriptive</td><td>5.93</td><td>21</td></tr><tr><td>Implicit prescriptive</td><td>10.28</td><td>30</td></tr><tr><td>Explicit prescriptive</td><td>5.84</td><td>18</td></tr><tr><td>(Missing value)</td><td></td><td>(0)</td></tr><tr><td rowspan="3">Type of business processes</td><td>Generic</td><td>8.31</td><td>37</td></tr><tr><td>Domain-specific</td><td>4.44</td><td>32</td></tr><tr><td>(Missing value)</td><td></td><td>(0)</td></tr><tr><td rowspan="5">Number of business processes</td><td>One</td><td>1.83</td><td>7</td></tr><tr><td>More</td><td>4.35</td><td>36</td></tr><tr><td>All</td><td>4.62</td><td>24</td></tr><tr><td>Combination</td><td>5.97</td><td>2</td></tr><tr><td>(Missing value)</td><td></td><td>(0)</td></tr></table>

For three of the five improvement method criteria (capability areas, architecture details, and type of business processes), the experts’ preferences were almost similar to what BPMMs actually offer (Table 7). We grouped the identified capability areas according to (Van Looy, De Backer & Poels, 2014); namely, along the phases of the traditional business process lifecycle (Weske, 2010) which are influenced by the cultural and structural aspects in an organization (vom Brocke & Rosemann, 2010). Existing BPMMs seem to address these capability areas in line with the experts’ expectations. Almost all sampled BPMMs cover the areas related to the traditional business process lifecycle (i.e., 56 sampled BPMMs cover modeling, all models cover deployment and optimization, and 67 cover management) (Weske, 2010), plus culture (i.e., 57 out of 69 BPMMs) (vom Brocke & Rosemann, 2010). In line with the literature, BPMMs relatively less frequently address structural reconfigurations in the organization chart or the formal introduction of a competence center, called the center of excellence (vom Brocke & Rosemann, 2010), and the experts also considered them as less relevant (i.e., indicated by the lowest weight for this criterion). In general, the experts considered good management by a professional process owner or process manager as essential for improving business (process) performance. Second, regarding the architecture details criterion, most BPMMs only implicitly offer a prescriptive roadmap (Maier et al., 2009).

Also the experts believed that BPMMs must offer sufficient guidance while allowing organizations to make their own choices instead of being too restrictive. Third, the experts rated generic BPMMs higher than domain-specific BPMMs because one can apply the former to any process type. Also, the BPMM sample contained slightly more generic models (i.e., 37 generic versus 32 domain-specific BPMMs), which suggests that generic models are easy to find.

Table 7 shows that 36 BPMMs cope with multiple processes in a certain business domain (i.e., referring to the option “more”, such as in supply chains), 24 BPMMs cope with all processes in an organization, and seven BPMMs address a single business process. Although the experts agreed that a combination of particular and all processes would benefit organizations, only two sampled BPMMs cover this combination.

Finally, regarding the architecture types, Table 7 indicates that most BPMMs offer a staged architecture with maturity levels, possibly in combination with a continuous architecture containing capability levels, whereas the experts recommended combining both maturity levels and capability levels in order to obtain a refined overview. In particular, a maturity level expresses the overall state of a business process or a set of business processes, while capability levels can add information on individual capability areas needed for realizing specific organizational objectives (de Bruin & Rosemann, 2007; Tapia et al., 2008). For instance, separate capability levels for capability areas related to process deployment and process optimization may add information on a specific customer service objective or the capability area of process modeling can help an organization realize an objective for obtaining grants or quality labels via a capability level that measures the efforts.

## 6.2.3 Evaluation of BPMMs against the Contextual Criteria

Table 8 focuses on the selection criteria pertaining to the contextual factors of a BPMM.

Table 8. Selection Criteria Pertaining to the Contextual Factors of a BPMM

<table><tr><td>Contextual criteria</td><td>Options</td><td>Weight (%)</td><td>Number of BPMMs (N = 69)</td></tr><tr><td rowspan="4">Purpose</td><td>Awareness</td><td>7.18</td><td>46</td></tr><tr><td>Also benchmarking</td><td>7.41</td><td>20</td></tr><tr><td>Also certification</td><td>2.33</td><td>3</td></tr><tr><td>(Missing value)</td><td></td><td>(0)</td></tr><tr><td rowspan="3">Validation</td><td>Application</td><td>2.04</td><td>25</td></tr><tr><td>Outcomes</td><td>6.57</td><td>19</td></tr><tr><td>(Missing value)</td><td></td><td>(25)</td></tr><tr><td rowspan="3">Costs</td><td>Free</td><td>3.42</td><td>31</td></tr><tr><td>Charged</td><td>1.47</td><td>13</td></tr><tr><td>(Missing value)</td><td></td><td>(25)</td></tr></table>

For two of the three contextual criteria, the experts’ preferences correspond to what most sampled BPMMs offer (Table 8). Regarding the purpose criterion, the experts agreed that BPMMs focus on improving an organization’s internal way of working, but they also advised BPMM designers to enable benchmarking (i.e., by comparing maturity levels against competitors, across departments, industries or regions). Similarly, one can use 46 out of 69 sampled BPMMs to just raise awareness, while 20 BPMMs also allow benchmarking. The experts perceived certification for external recognition as rather an unnecessary effort. Similarly, only few existing BPMMs issue a certificate. Furthermore, regarding the costs criterion, one can access and use many BPMMs free of charge, which the experts also appreciated. On the other hand, the experts highly valued the validation of outcomes in the validation criterion, whereas only a minority of BPMMs guarantee it (i.e., 19 out of 69 BPMMs or 27.5%). Strikingly, 25 sampled BPMMs do not mention any validation efforts in their documentation.

## 7 Discussion about the Research Questions

In this paper, we investigate selection criteria or BPMM desiderata without focusing on particular BPMMs. We contribute to the literature by distilling a ranked and weighted set of BPMM selection criteria. Given that we use strict research methods, we posit that one can consider the 14 developed criteria as being the most important ones for BPMM selection (RQ1). They constitute an objective (or rather inter-subjective) set of criteria that identifies the main differences among BPMMs for prospective users. In other words, our research efforts ensure that we can consider the proposed set as valid and that, if specific BPMMs cover only some of the selection criteria, these maturity models may be flawed. For instance, a well-designed BPMM incorporates several assessment items, techniques for data collection, activities for improving capability areas, and so on.

From examining the extent to which selection criteria apply to current BPMMs (RQ2) while considering the ranks and weights, we provide empirical evidence of the differences (and so the varying quality) among BPMMs (see Section 7.2 for a deeper discussion). As such, we demonstrate the applicability of this ranked set to assess the quality of BPMMs by satisfying the initial requirements (Table 9), which allows one to reflect on the selection criteria themselves (see Section 7.3 for further reflections).

Table 9. Evidence for the Applicability of Our Set of Selection Criteria for BPMMs

<table><tr><td></td><td>Requirement satisfaction tests</td><td>Evidence</td></tr><tr><td>Utility</td><td>Criteria utility: based on a textual description of the selection criteria, other people can evaluate BPMMs other than those involved in our sample. The Cohen&#x27;s kappa represents a significant level of agreement or interrater reliability (0.4 = &lt; kappa = &lt; 1; p &lt; 0.05).Ranking utility: based on descriptive statistics, one can generate comparative tables to visualize the weights of individual selection criteria along with the effective support in current BPMMs.Clarity: in the comparative tables, one can highlight the main differences between BPMMs with respect to the ranked and weighted selection criteria.</td><td>Criteria utility: kappa = 0.571 (p = 0.002).Ranking utility: Table 6, Table 7, Table 8Clarity: highlights in Table 6, Table 7, and Table 8 (i.e., bold for the highest weights and number of BPMMs; italics for the number of missing values)</td></tr><tr><td>Effectiveness</td><td>Prospective users are satisfied with 1) the selection criteria in the developed set, 2) their descriptions of trade-offs, and 3) the sequence in which they appear based on a general ranking with weights (i.e., 50% for scores 5-6-7 on a seven-point Likert scale, and no opposite extreme score of 1).</td><td>Satisfaction of 5 out of 7 prospective users (or 71.4%); no negative scores</td></tr><tr><td>Efficiency</td><td>Based on the comparative tables, one can detect relevant differences among BPMMs by following a standard way of working.</td><td>A difference exists between the general weights and the support in BPMMs for:4 out of 6 assessment method criteria2 out of 5 improvement method criteria1 out of 3 contextual criteria</td></tr></table>

## 7.1 Discussion about BPMMs

In the evaluation study, we noticed discrepancies between the experts’ opinions and what BPMMs actually offer. Therefore, starting with the assessment method criteria, we took a closer look at some major issues. In particular, the use of qualitative versus quantitative scales and of objective versus subjective data-collection techniques is a first point of discussion. The fact that one BPMM in our sample uses only quantitative scales and four BPMMs use only objective techniques for data collection emphasizes the importance of an organizational setting. For instance, some capability areas (such as management or culture) are hard to measure with numbers and document reviews alone. Many BPMMs still have an opportunity to enhance the accuracy of their assessments by applying data triangulation and combining the advantages of different rating scales and data-collection techniques.

Second, in terms of the improvement method, a strong difference exists in terms of the number of business processes that one needs to assess and improve. This discrepancy indicates a substantial gap in existing BPMMs, which one can explain with the historical evolution of BPMMs. From the 1980s, the CMM(I) tradition has inspired many maturity models to cover particular processes (Ahern et al., 2004). The focus on the BPM mastery of an organization appeared only in the 2000s (McCormack & Johnson, 2001, de Bruin & Rosemann, 2007; Hammer, 2007). A next logical step in the BPMM evolution might be to simultaneously examine particular and all business processes in an organization.

Third, one can explain the experts’ preferences for contextual criteria with existing theories. For instance, the results show that BPMMs would generally profit from introducing more benchmarking possibilities.

Also, in the literature, benchmarking is associated with best practices that can lead to organizational performance and learning as a substitute for market and stakeholder forces (Van Helden & Tillema, 2005). If led by a third party, the assessment may acquire more external recognition (i.e., credibility) but at higher cost (Mettler, 2009). Following Grabowski and Lee (1993), organizations must decide on how much money they are willing to spend in relation to their strategy and budget. Finally, we uncovered another great challenge for most BPMMs in the validation criterion (see Section 6.2.3). In line with Soh and Markus (1995), organizations must recognize that they can create business value only with a time delay between design (or selection), appropriate use, and outcomes. In other words, validating the outcomes of a BPMM takes time, but maturity models can at least provide some information on their (ongoing) validation efforts in their documentation.

The discussion also gives rise to three concrete areas for improving existing BPMMs. These areas represent calls to action for both BPMM designers (i.e., who should include the identified selection criteria in the documentation of their models) and users (i.e., who should consider the selection criteria).

Figure 5 illustrates that all the sampled BPMMs address the improvement method criteria but that they generally do not discuss the assessment method criteria and the contextual criteria. This point applies particularly to the assessment duration (with 43 missing values out of 69 BPMMs), validation and costs (both with 25 missing values). The improvement method criteria represent a BPMM’s direction independent of a practical assessment and, thus, received the highest weights. Another explanation for the missing values is that the design studies we present in Section 2 each address less than half of our selection criteria (Mettler, 2009; Röglinger et al., 2012), which may affect the decisions that BPMM designers have made so far. As such, we formulate a first area in which BPMMs need to improve (suggested improvements (SI)):

SI1: Designers (e.g., scholars or consultancy firms) should provide information on all identified selection criteria to facilitate users’ choices.

![](/api/attachments/ZZRNMAD4/fulltext/images/8f9962b50168029b9750c92258a21ea57bbe972688856ca12d8156437675e703.jpg)  
Figure 5. The Number of BPMMs with Missing Values per Selection Criterion (N = 69)

This first suggested improvement is not a trivial matter in practice since many BPMM designers can still enhance their existing BPMMs by addressing the criteria we discuss in our study. Figure 6 provides further evidence for the varying quality of BPMMs by looking at the rankings. Based on the relative weights obtained through AHP in the international Delphi study, we calculated a selection score (from 0 to 100) per sampled BPMM. Per criterion, we scored each BPMM according to the weight that corresponds to the option to which it applies.

![](/api/attachments/ZZRNMAD4/fulltext/images/d64fa641bfd66bb4d842156977da01a22a77f09eacb2a090aa4d93ecf55482e2.jpg)  
Figure 6. The Frequency Distribution of Selection Scores across BPMMs (N = 69)

Figure 6 shows that the selection scores in the BPMM sample ranged from 40 to 90 (mean = 67.14 and SD = 10.35). Fifty-one BPMMs had a score between 60 and 80, whereas four BPMMs have a higher score and 14 BPMMs have a lower score. Hence, no BPMM in the sample covers all the ideal options as the experts stipulated them. Specific organizations’ preferences may, however, still differ from the assigned weights. Although we make general conclusions (instead of focusing on particular BPMMs), we note that the most mentioned BPMMs in the literature are not mediocre. For instance, the models of CMMI (SEI, 2009), OMG (2008), and Harrington (2006) scored between 65 and 70, whereas the models of de Bruin and Rosemann (2007) and Hammer (2007) scored around 75. McCormack and Johnson’s model (2001) was in the forefront with almost 82 points. A direct comparison, however, remains difficult as a fit with an organization’s particular needs is paramount. For instance, the number of business processes that these BPMMs address differ. Instead, we generalize that BPMMs with the lowest selection scores (i.e., with many missing values and/or a combination of less preferred options) may need improvements.

SI2: Designers should consider the different options per selection criterion and possibly make their design more flexible by providing alternative options to offer a better fit for purpose.

The third area for improvement refers to the wide range of selection scores.

SI3: Organizations, as potential BPMM users, should develop a critical attitude towards the fit for purpose of BPMMs instead of taking quality for granted.

We do not assert that all BPMMs are flawed and that one should never select any of them given that organizations positively perceive the practical value of using a maturity model (Harmon, 2013; Harmon & Wolf, 2014) and that research has empirically demonstrated such value (McCormack & Johnson, 2001; Skrinjar et al., 2008). Instead, the evaluation study indicates ample opportunities for designers to improve their BPMMs and indicates that organizations should not choose just any BPMM. Our findings motivate why we do not advocate a single BPMM. The perfect BPMM (i.e., which satisfies all needs of all organizations) seems non-existent and is perhaps unrealistic to design. Hence, organizations must make concessions on selection criteria that are less relevant to them. However, given the importance of the capability areas criterion, it seems that organizations should never make concessions for this criterion.

## 7.2 Discussion about the Selection Criteria for BPMMs

We now discuss the distilled set of selection criteria themselves and the contributions to knowledge we make, and we offer possible refinements to each criterion in future research.

First, our research offers standardized steps with which one can compare other or new BPMMs:

Search for BPMM documentation by combining the keywords “process” and “maturity” and verify whether such documentation: 1) contains maturity levels and/or capability levels, and 2) primarily focuses on business processes instead of other organizational assets.

Perform a content analysis of the identified BPMM documentation to analyze how the selection criteria in Table 5 and the Appendix apply to it.

• Compare the results of the content analysis with the general weights of Figure 4.

Evaluate the BPMM documentation by counting the missing values (Figure 5) and the number of times the model does not apply the selection criteria options as the experts preferred (i.e., the options with the highest weights) (Figure 6).

Furthermore, we demonstrate that the criterion for type of business processes allows one to specify domain-specific BPMMs for supply chains and collaboration processes. Although not investigated, other domain-specific BPMMs may be similarly covered, such as those specifically for software processes. Further research could extend our approach to other maturity models than BPMMs, such as for business-IT alignment, e-government, project management, and so on. Many selection criteria (particularly those related to the assessment method and the contextual criteria) seem generic for any maturity model. Moreover, one can reuse our methodology with other maturity model types. Opportunities also exist for fellow scholars to examine BPMMs during their use and the impact these designs may have on the ability of individuals to understand the models.

Next, we discuss the degree to which the developed set of selection criteria goes beyond the current body of knowledge. Although we considered diverse elements in the design of maturity models (see Section 2, Table 1) in the Delphi study as possible BPMM desiderata, it turned out that some are less decisive for BPMM selection, which proves that selection criteria or BPMM desiderata differ from currently known design criteria and that the former can supplement the latter. At first sight, when contrasting our findings with the comparative work of Mettler (2009) and Röglinger et al. (2012), it seems that each study addresses less than half of the criteria we identified. Both design studies neither discuss trade-offs nor alternatives (e.g., different ratings scales, data-collection techniques, or ways to calculate and represent lifecycle levels). Because the presented design studies do not address many BPMM desiderata, these desiderata contribute to the business process management discipline as new knowledge about BPMMs. Nonetheless, a direct comparison remains difficult because the design criteria of Mettler (2009) and Röglinger et al. (2012) are at different levels of analysis. For instance, many design criteria in Mettler (2009) seem to refer to decisions that organizations must make independently of a BPMM (e.g., whether to launch improvement projects, whether consultants should lead such projects, and the link between process improvements and other organizational targets). Furthermore, Röglinger et al. (2012) present a criterion that they have never seen in any BPMM. It concerns a decision calculus (or cost-benefit analysis) to verify which improvements best fit a particular organization. This criterion might supplement our costs criterion in future research. Surprisingly, only Röglinger et al. (2012) mention the presence of capability areas (which are core to all maturity models) albeit without identifying the capability areas. Mettler (2009) does not mention capability areas at all. Because we assign top priority to capability areas, we encourage further research on their theoretical understanding. Particularly, only a handful of scholars have a conceptualization of business process capability areas (de Bruin & Rosemann, 2007; Van Looy, De Backer & Poels, 2014). We need more research to verify how they can be improved in a more dynamic way instead of a static, one-size-fits-all roadmap that current BPMMs present (Pöppelbuss et al., 2011) and to refine capability areas with a contingency approach depending on organization-specific characteristics (Plattfaut, Niehaves, Pöppelbuss, & Becker, 2011; vom Brocke, Zelt, & Schmiedel, 2016). This final criticism is valid not only for BPMMs but also generally for most maturity models (Donnellan & Helfert, 2010).

As for future research opportunities, one could similarly evaluate BPMMs in five or ten years to examine any progress or evolution made in BPMM documentation. We also strongly encourage further research on how capability areas can become more dynamic and contingent on organization-specific factors (such as organization size, market competitiveness, and so on). For instance, new Delphi or case studies could generate ideas that help solve such problems in order to further theorize about BPMMs and the business process management discipline. Given the observed shortcomings, current BPMMs may help raise awareness and serve as benchmarking tools without being the ultimate solution to all implementation problems. Furthermore, another Delphi study could collect data to elaborate on the trade-offs of other selection criteria. In particular, the costs criterion could be detailed with price levels to develop a cost-benefit analysis or decision calculus. Meanwhile, organizations could benefit from customization by changing and combining existing

BPMMs to create a BPMM that better fits their organizational needs (possibly supported by a more advanced decision support tool than what Van Looy, De Backer, Poels and Snoeck (2013) present).

## 8 Conclusion

With this study, we contribute to research on business process management and maturity models by performing an in-depth analysis of the constituents of BPMMs to identify selection criteria. We discuss a range of weighted criteria that impact the selection of a BPMM (based on an international Delphi study with strict consensus conditions and coder triangulation) in order to provide evidence of BPMMs’ strengths and weaknesses (based on a content analysis of a large BPMM sample for generic processes, supply chains, and collaboration processes). The findings shed light on issues in the documentation of BPMMs that are relevant to managers and executives when making investment decisions in choosing a particular BPMM. Moreover, by evaluating the applicability of selection criteria, we empirically analyze the deficiencies in BPMMs. To the best of our knowledge, this study is the first to evaluate BPMMs in such detail from a user perspective. The results also confirm that obtaining the highest maturity levels is not an end goal of BPMMs but that capability improvements and performance improvements are. In sum, we have uncovered a rich understanding of normative user behavior associated with BPMM selection and, thus, supplement existing design studies. We also provide evidence for the varying quality of many BPMMs that exist today and, as a result, make calls to action for both designers and organizations. Avenues for future research include 1) generalizing our methodology and selection criteria towards other types of maturity models and 2) examining the actual use of BPMMs (to supplement selection, which comes first). Other research can also refine the BPMM selection criteria by, for instance, investigating how the process capability areas can become more dynamic and contingent (i.e., organization dependent) and by investigating how BPMMs can facilitate a cost-benefit analysis for organizations to make accurate investments with respect to improvement initiatives. Other Delphi studies might be conducted to further explore and overcome these limitations.

## Acknowledgments

We presented a limited version of this manuscript at the ECIS 2013, which provided us with early feedback to strengthen our work. We also thank JAIS’s reviewers and senior editor for their constructive feedback.

## References

Ahern, D. M., Clouse, A., & Turner, R. (2004). CMMI distilled. Boston: Pearson Education.

Becker, J., Knackstedt, R., & Pöppelbuss, J. (2009). Developing maturity models for IT management. Business & Information Systems Engineering, 1(3), 213-222.

Van Looy, A., De Backer, M., Poels, G., & Snoeck, M. (2013). Choosing the right business process maturity model. Information & Management, 50(7), 466-488.

Van Looy, A., De Backer, M., & Poels, G. (2011). Defining business process maturity. A journey towards excellence. Total Quality Management & Business Excellence, 22(11), 1119-1137.

Van Looy, A., De Backer, M., & Poels, G. (2014). A conceptual framework and classification of capability areas for business process maturity. Enterprise Information Systems, 8(2), 188-224.

Bostrom, R. P., Gupta, S., & Thomas, D. (2009). A meta-theory for understanding information systems within sociotechnical systems. Journal of Management Information Systems, 26(1), 17-47.

Crosby P. B. (1979). Quality is free. New York: McGraw-Hill.

Curtis, B., & Alden, J. (2007). The business process maturity model: What, why, and how. BPTrends.

Dalkey, N., & Helmer, O. (1963). An experimental application of the Delphi method to the use of experts. Management Science, 9(3), 458-467.

de Bruin, T., Freeze, R., Kulkarni, U., & Rosemann, M. (2005). Understanding the main phases of developing a maturity assessment model. In Proceedings of the Australasian Conference on Information Systems (pp. 1-10).

de Bruin, T., & Rosemann, M. (2007). Using the Delphi technique to identify BPM capability areas. In Proceedings of the Australasian Conference on Information Systems (pp. 642-653).

Donnellan, B., & Helfert, M. (2010). The IT-CMF: A practical application of design science. In Proceedings of DESRIST (pp. 550-553). St. Gallen: Springer.

El Emam, K., & Birk, A. (2000). Validating the ISO/IEC 15504 measure of software requirements analysis process capability. IEEE of Transaction Software Engineering, 26(6), 541-566.

Glaser, B. G., & Strauss, A. L. (1967). The discovery of grounded theory: Strategies for qualitative research. New Jersey: Transaction Publishers.

Grabowski, M., & Lee, S. (1993). Linking information systems application portfolios and organizational strategy. In R. D. Banker, R. J. Kauffman & M. A. Mahmood (Eds.), Strategic information technology management (pp. 33-54). Pennsylvania: IGI Global.

Hammer, M. (2007). The process audit. Harvard Business Review, 4, 111-123.

Harmon, P. (2013). Case studies in how organizations become more mature. BPTrends.

Harmon, P., & Wolf, C. (2014). The state of business process management 2014. BPTrends.

Harrington, H. J. (2006). Process management excellence. California: Paton Press.

Hasson, F., Keeney, S., & McKenna, H. (2000). Research guidelines for the Delphi survey technique. Journal of Advanced Nursing, 32(4), 1008-1015.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75-105.

Maier, A. M., Moultrie, J., & Clarkson, J. P. (2009). Developing maturity grids for assessing organizational capabilities: Practitioner guidance. In Proceedings of ICMC (pp. 1-29). Vienna: Management Consulting Division.

Maier, A. M., Moultrie J., & Clarkson, J. P. (2012). A review of maturity grid based approaches to assessing organizational capabilities. IEEE Transactions on Engineering Management, 59(1), 138- 159.

March, S. T., & Smith, G.F. (1995). Design and natural science research on information technology. Decision Support Systems, 15(4), 251-266.

McCormack, K., & Johnson, W. C. ( 2001). Business process orientation. Florida: St. Lucie Press.

Mettler, T. (2009). A design science research perspective on maturity models in information systems (Report BE IWI/HNE/03). St. Gallen: Institute of Information Management.

Mettler, T., & Rohner, P. (2009). Situational maturity models as instrumental artifacts for organizational design. In Proceedings of DESRIST (pp. 1-9). Malvern: ACM.

Okoli, C., & Pawlowski, S. D. (2004). The Delphi method as a research tool: An example, design constructions and applications. Information & Management, 42, 15-29.

OMG. (2008). Business process maturity model (version 1.0). Retrieved from http://www.omg.org/spec/BPMM/1.0/PDF

Plattfaut, R., Niehaves, B., Pöppelbuss, J., & Becker, J. (2011). Development of BPM capabilities. In Proceedings of the European Conference on Information Systems (pp. 1-12). Helsinki: AISEL.

Pöppelbuss, J., Plattfaut, R., Ortbach, K., Malsbender, A., Voigt, M., Niehaves, B., & Becker, J. (2011). Service innovation capability: Proposing a new framework. In Proceedings of FedCSIS (pp. 545- 551). Szczecin, Poland: IEEE Explore.

Dijkman, R., Lammers, S. V., & de Jong, A. (2015). Properties that influence business process management maturity and its effect on organizational performance. Information Systems Frontiers, 18(4), 717-734.

Röglinger, M., Pöppelbuss, J., & Becker, J. (2012). Maturity models in business process management. Business Process Management Journal, 18(2), 1-19.

Saaty, T. L. (1990). An exposition of the AHP in reply to the paper “remarks on the analytical hierarchy process”. Management Science, 36(3), 259-268.

SEI. (2009). CMMI for services (version 1.2). Retrieved from http://www.sei.cmu.edu/reports/09tr001.pdf

Sheard, S. A. (2001). Evolution of the frameworks quagmire. IEEE Computer, 34(7), 96-98.

Skrinjar, R., Bosilj-Vuksic, V., & Stemberger, M. I. (2008). The impact of business process orientation on financial and non-financial performance. Business Process Management Journal, 14(5), 738-754.

Soh, C., & Markus, L. M. (1995). How IT creates business value: A process theory synthesis. In Proceedings of the International Conference on Information Systems (pp. 1-12).

Tapia, R. S., Daneva, M., van Eck, P., & Wieringa, R. (2008). Towards a business-IT alignment maturity model for collaborative networked organizations. In Proceedings of the EDOC Workshop (pp. 70- 81).

Van Helden, J. G., & Tillema, S. (2005). In search of a benchmarking theory for the public sector. Financial Accountability and Management, 21(3), 337-361.

van Steenbergen, M., Bos, R., Brinkkemper, S., van de Weerd, I., & Bekkers, W. (2010). The design of focus area maturity models. In Proceedings of DESRIST (pp. 317-332). St.Gallen: Springer.

vom Brocke, J., & Rosemann, M. (2010). Foreword. In J. vom Brocke & M. Rosemann (Eds.), Handbook on BPM 2 (pp. vii-ix). Berlin: Springer.

vom Brocke, J., Zelt, S., & Schmiedel, T. (2016). On the role of context in business process management. International Journal of Information Management, 36(3), 486-495.

Wendler, R. (2012). The maturity of maturity model research: A systematic mapping study. Information and Software Technology, 54(12), 1317-1339.

Weske, M. (2010). Business process management. Berlin Heidelberg: Springer.

Zhao, S. (1991). Metatheory, metamethod, meta-data-analysis: What, why, and how? Sociological Perspectives, 34(3), 377-390.

## Appendix: BPMM Selection Criteria

## A. Assessment method criteria

• Rating scale: the type of data that is collected during an assessment.

Quantitative data (discrete, interval, or ratio scales) can be statistically analyzed and compared independently of the assessors’ interpretation. Qualitative data (nominal or ordinal scales) provide more in-depth descriptions but depend more on the assessors’ skills. Also, a combination is possible depending on the available data and skills.

• Data-collection technique: the way information is collected during an assessment.

Objective techniques involve document reviews and give an idea of how organizations work without interrupting individuals or activities. They minimize biased results of (particularly internal) assessors and respondents. Subjective techniques gather information about how organizations actually work (e.g., with questionnaires, interviews, or observations). As it concerns personal beliefs, some precautions can be taken (e.g., a third party lead assessor, multiple assessors and respondents, data-collection training, or a combination with objective techniques).

• Assessment duration: the maximal duration of a particular assessment.

Some BPMMs only take one day (e.g., a quick scan in 15 minutes), whereas other BPMMs present a more profound analysis of one week or longer. Because time is money, users must consider how much time they want to spend on the assessment alone.

Assessment availability: whether the assessment questions and corresponding level calculation are publicly available (instead of only known to the assessors).

BPMMs (particularly non-academic models, such as in consultancy) do not always provide full details. The user must decide whether this limited availability is an issue for the organization. For instance, one can use fully known BPMMs (i.e., either free or charged) for educating process team members or for earning credibility.

Functional role of respondents: the explicit recognition to include people from outside the assessed organizations as respondents.

If only internal respondents (managers and/or staff) are questioned, the user assumes they fully know the stakeholders’ needs. By involving stakeholders, an organization recognizes the need for an outside-in perspective by explicitly listening to them.

Number of assessment items: the maximal number of questions to be answered during an assessment.

More questions provide more insight to develop a road map but may be less feasible and/or take longer. Less than 20 questions are rather used as a teaser or a quick scan.

## B. Improvement method criteria

• Capability areas: the capabilities to be assessed and improved.

BPMMs differ in the capabilities they address, varying from basic capabilities related to the traditional business process lifecycle (i.e., modeling, deployment, optimization, and management) to the addition of organizational capabilities (i.e., to create a process-oriented culture and structure). In theory, fully mature business processes require all presented capability areas. However, in practice, an organization can opt for a subset (e.g., depending on the degree of top management support, IT background of the user, prior BPM experience, organization size, etc). For instance, organizations with local, bottom-up initiatives or with limited BPM experience might wish to start with the basic capability areas limited to the traditional business process lifecycle. Additionally, the culture capability area requires a minimum level of management support to promote business processes and granting (financial) rewards to process performance. Finally, structural configurations inherently require top management support. The latter is recommended if one already has some BPM experience or if one seeks to standardize processes across large departments or divisions. The user must select a set of capability areas that best fits its organizational needs.

Architecture type: the possibility to define a road map per capability, a road map for overall maturity, or both.

It concerns linking (maturity of capability) levels to capability areas in a step-by-step plan, which explains how to reach each consecutive level. A continuous architecture provides capability levels per capability area (i.e., one road map per area). It allows organizations to assess and improve each capability area separately and, thus, to improve areas at a different pace or to limit their scope to only those capability areas they are interested in. Because one does not necessarily consider all capability areas in a continuous architecture, one risks suboptimal optimizations (in terms of overall maturity). On the other hand, a staged architecture provides maturity levels linked to all capability areas together (i.e., one road map for overall maturity). The emphasis is on simultaneous advancements instead of individual capability advancements.

Architecture details: the degree of guidance that a BPMM provides on one’s journey towards higher maturity.

It concerns the extent to which the road map (step-by-step plan) explains which criteria (goals and best practices) must be satisfied before reaching each particular level: 1) descriptive, 2) implicit prescriptive, or 3) explicit prescriptive. A descriptive road map is limited to high-level descriptions. Because it gives less support, it suits organizations that want to become acquainted with BPMM or those highly experienced with process improvements. An implicit prescriptive road map has criteria interwoven in the assessment questions (i.e., with an ordinal scale or a matrix) that explain all capability areas per level. Assessors can derive the criteria from the assessment questions. Finally, an explicit prescriptive road map gives most guidance by separately listing criteria from the assessment questions.

Type of business processes: whether the BPMM is generic (i.e., for business processes in general) or domain specific (e.g., for business processes in supply chains or collaboration situations).

The terminology used in generic BPMMs (e.g., in the assessment questions) is likely more holistic. Benchmarking becomes possible across business domains. Domain-specific BPMMs use terminology adapted to their domain, which might be less abstract and, thus, better understandable. However, benchmarking remains limited to organizations in the same domain. This choice requires strategic considerations.

Number of business processes: the number of business processes to be assessed and improved: 1) one, 2) more, or 3) all.

For BPMMs that focus on a single business process, the user must define the process boundaries (e.g., whether a business process is assessed and improved as a subprocess or as a separate process). BPMMs can also focus on more than one, but not all, business processes in the assessed organizations. Assessment questions then deal with a particular business domain or value chain and all its (sub)processes. Furthermore, BPMMs can cope with all business processes in the assessed organizations. As such, assessment questions take a management perspective by focusing on how organizations deal with business processes in general, without focusing on particular processes. By improving this BPM mastery, one will likely indirectly improve particular processes, too.

## C．Contextual criteria

• Purpose: the purpose for which a BPMM is intended.

The basic purpose of any BPMM is assessing and identifying process improvements (i.e., raising awareness). The key is recognizing deficiencies, creating willingness to act, and following through on the findings. Besides raising awareness, BPMMs can allow benchmarking (to compare with competitors and share best practices) or certification (for external recognition of assessment results).

Validation: whether or not the BPMM documentation gives empirical evidence that the BPMM can be used to enhance the efficiency and effectiveness of business processes.

Most BPMMs do not provide any proof of validity (or success). If they do, evidence is frequently limited to enumerating how many other organizations apply the model. Only few BPMMs give evidence for the performance outcomes. Users must decide whether they need some proof of validity depending on the planned investments. However, we discourage the use of nonvalidated BPMMs. They can result in frustration and time and money losses (i.e., if they appear to be flawed or unusable after one starts using it).

• Costs: the direct costs to access and use a BPMM.

Not all BPMMs are free of charges. Particularly non-academic models may ask a one-off access fee or a required training to be followed. Recurring costs rather serve to pay a third party lead assessor, certification or benchmarking. Users must decide which budget can be spent, and adapt their expectations accordingly: one often get what one pays for. Academic models can be free if they use your data for research enhancements.

## About the Authors

Amy Van Looy holds a PhD in applied economics. She is Assistant Professor at the Faculty of Economics and Business Administration of Ghent University (Belgium). Before entering academia, she worked as an IT consultant for e-government projects. She is passionate about the adoption and evolution of a process-oriented approach, including organizational capabilities and the impact on culture, people, governance, strategy, and structure, the contextual factors affecting process realizations, and digital innovation. Her research is published in scientific outlets such as Total Quality Management & Business Excellence, Enterprise Information Systems, Information & Management, Business & Information Systems Engineering, and Journal for the Association of Information Systems. She obtained the “Highest Award for Achievement” at the Dale Carnegie Consulting Program (2007) and the “Award for Best Contribution” at the OnTheMove Academy (2010). Additionally, Amy was nominated in the top-10 for “Young ICT Lady of the Year 2014” by the Belgian magazine DataNews.

Geert Poels is head of the Business Informatics research team, which he founded in 2005. He is full professor of Management Information Systems (since October 1, 2012) and member of the professorial staff of the Faculty of Economics and Business Administration, Ghent University (since October 1, 2002). He is member of the University Research Council and chairman of the Faculty Scientific Research Committee. Within the Business Informatics research team he coordinates the Enterprise Modelling research cluster and directs research on the modelling and analysis of strategic fit, value delivery, business capabilities, and business services. A common thread in this line of research is the disruptive impact of Information Technology on business models and business processes. In the 2008-2017 period, he was promoter of eight completed PhD research projects, while currently he is promoter of eight ongoing PhD projects. His personal research interests concern the quality of conceptual models, the conceptual modelling of service systems, and business process architecture.

Monique Snoeck holds a PhD in computer science from the KU Leuven. She is full professor in the Department of Decision Sciences and Information Management of the Faculty of Economics and Business of the KU Leuven and visiting professor at the University of Namur (UNamur). She has a strong research track in conceptual modeling, requirements engineering, software architecture, model-driven engineering and business process management. Main guiding research themes are domain modelling, business process modelling, model quality, model-driven engineering, and e-learning. Previous research has resulted in the Enterprise Information Systems Engineering approach MERODE, and its companion elearning and prototyping tool JMermaid. She is author of two books and (co-)author of over 38 peerreviewed journal papers and over 56 peer-reviewed conference papers. She is member of the program committee of numerous conferences in the IS domain such as CAiSE, EIS, EMMSAD, MORE-BI, QoIS, REFSQ.

Copyright © 2017 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints or via email from publications@aisnet.org.
