---
otero_id: 19132
otero_key: "XGMQZTSC"
title: "Using knowledge-based systems for strategic market assessment"
authors: "Matthew J. Liberatore; Anthony C. Stylianou"
year: "1994"
journal: "Information & Management"
doi: "10.1016/0378-7206(94)90050-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Using knowledge-based systems for strategic market assessment $*$

Matthew J. Liberatore, Anthony C. Stylianou \*

Department of Management, Villanova University, Villanova, PA 19085, USA

Department of Management Information Systems and OM, University of North Carolina at Charlotte, Charlotte, NC 28223, USA

## Abstract

A methodology for the design, development, and implementation of knowledge-based decision support systems for strategic market assessment is applied and tested. The approach integrates knowledge-based systems with scoring models, logic tables, and the analytic hierarchy process. The resulting system, known as the Strategic Market Assessment System (SMAS), is designed to provide the decision support necessary to evaluate whether or not full-scale development of a candidate product should proceed. It can function as a stand-alone system or in conjunction with other evaluation systems (e.g., those providing financial, technological, manufacturing, and customer satisfaction evaluations) to provide a complete assessment of the product under consideration. Since its implementation, the experts' and other users' expressions of complete satisfaction and commitment to the system is an indication of its value as an important decision support tool.

Keywords: Knowledge-based DSS; Expert systems; Decision support systems; Project selection; Project evaluation; Strategic market assessment; Product development; Analytic hierarchy process

## 1. Introduction

As a result of intensifying global competition and accelerating technological change, new prod-

\* Corresponding author.

uct development has been increasingly expensive, risky, and time-sensitive. For example, about one in seven concepts that enter the new product development process becomes a commercial success; about half of the resources that U.S. industry spends on new product development leads to failed or canceled products [3]. Also, the competitive and financial benefits of even relatively short reduction in the time required for the new product development process in technology-based businesses can be quite substantial. A McKinsey and Co. model [6] estimates that a high-tech product that comes to market six months late but on budget earns 33% less profit over five years.

For these reasons, it is necessary to evaluate ongoing projects at key decision points as they proceed through the development cycle. The evaluations should be strategic in nature and take into account the various financial, technological, manufacturing, market and customer factors and inter-relationships that influence executive decision-making within a specific firm. The evaluation process itself should incorporate the knowledge of key managers and should not be resource intensive or so time consuming that the product development process is impeded. This paper presents a knowledge-based decision support system with these characteristics; it has been successfully implemented in the strategic market assessment domain.

We focus on the strategic decision to commit to full-scale development of the product. The project is presumed to be at the stage in its development cycle where a major resource commitment is required to “prove” the product and its technology. This may occur when the product concept moves from preliminary development and testing to scale-up, where piloting or either small-scale or contract manufacturing is required.

## 2. Literature review and critique

The extensive literature on the evaluation and selection of R&D projects has been reviewed in various surveys [1], [8]. Conceptually simple approaches such as checklists and scoring models are widely used, while more sophisticated models such as mathematical programming have had limited impact in practice [13], [25].

Scoring models or weighted attribute models $[4]$ , $[10]$ are easy to use and understand, systematize the review of projects, and focus attention on the most important issues. However, scoring models are seen as oversimplifications when they attempt to reduce complicated decisions to a product score based on a small number of criteria. The analytic hierarchy process (AHP) developed by Saaty $[22]$ can be used in conjunction with scoring models to improve the project evaluation process. The AHP is a decision-making method for prioritizing alternatives when multiple criteria must be considered. It allows the decision maker to structure a problem in the form of a hierarchy or a set of integrated levels. As applied to project selection and evaluation, these levels might be:

(1) the goal (to select the best projects),

(2) the criteria, such as net present value and market size,

(3) the ratings scale, used to score each of the projects with respect to each criterion, and

(4) the projects themselves.

The hierarchy lends itself to an analysis based on the impact of a given level on the next higher level. The process begins by determining the relative importance of the criteria in meeting the goal. Next, one must determine the relative importance of the rating scale categories for each of the criteria. The focus shifts to measuring the extent to which the projects achieve each of the criteria. Finally, the results of the analysis are synthesized using a weighted averaging process to compute the relative importance of the projects in meeting the goal.

The AHP-scoring approach can form the basis of a decision support system (DSS) for project evaluation $[11]$ , $[12]$ . However, additional flexibility may be required if the benefits of scoring and the AHP are to be combined with the knowledge and expertise of those marketing managers required to make strategic product assessments. This flexibility may not be found in traditional marketing information systems, which are often unresponsive to the changing informational needs of individual marketing managers $[7]$ .

Knowledge-based systems provide the capability to capture, model, and process the knowledge of marketing and development managers. Recently, several authors have promoted the use of expert systems in the marketing function $[16]$ , $[23]$ , $[24]$ . Others have described some broad guidelines for the development of expert systems for the marketing function $[15]$ . The actual or suggested application to product development evaluation has been limited to “generic” systems that do not capture the organization-specific knowledge required to develop a model suitable for strategic new product development decisionmaking [2], [21], [26]. A recent survey supports this assertion [9].

## 3. Knowledge-based decision support systems

The approach selected for the development of SMAS was knowledge-based decision support systems (KBDSS). Generic, conceptual models of KBDSS (also known as expert support systems, or intelligent DSS) have been described by many researchers in the DSS and expert systems fields (see [5] for a review).

The KBDSS approach has the distinct advantage of being able to combine the desired capabilities from both decision support systems and knowledge-based approaches. The development and implementation methods associated with the two technologies, and the capabilities provided by them, open up a variety of opportunities to provide better and more comprehensive support for a wider spectrum of decision situations. A system supporting strategic market assessments must incorporate heuristics and other qualitative factors, along with quantitatively-oriented evaluation methods and criteria that are commonly used in practice. The flexibility of the KBDSS approach to draw from management science, DSS, and knowledge-based approaches, and to accommodate organizational and decision-making differences is ideally suited to the strategic market assessment task at hand.

A KBDSS approach for market assessment requires a means to extract knowledge from decision makers responsible for performing strategic market assessments, design a knowledge structure based on the models and methods used, integrate the modeled knowledge into a system, and disseminate it to general managers, development managers, and others in the organization. Such an approach could lead to an improvement in both the quality and consistency of decisions, as well as the decision-making process itself.

The structured methodology presented here integrates methods and approaches from management science and information systems. It has been field-tested and validated through several system development processes and is applicable to the development of assessment systems in a variety of organizational contexts.

## 4. Strategic market assessment at Armstrong World Industries

Armstrong World Industries is the recognized industry leader in the development and commercialization of new flooring products. A strategic market assessment system (SMAS) for new product development projects was implemented in their Floor Products Operations. This system was designed to assist Armstrong in meeting its strategic commitment to the customer. The managers of residential and commercial sales and marketing within Floor Products Operations served as the experts for the development of SMAS. They are members of the Floor Products Operations Strategy Team, which has overall responsibility for new product development. As a result, their evaluations and recommendations have a significant impact on strategic decisions concerning the mix of floor products. Specific decisions of the strategy team range from a commitment for pilot plant testing from in-house or contract manufacturing to the termination of all future work on the product concept.

Previously, the strategy team had used a planning process called Customer-Based Strategic Planning (CBSP) to assist in new product development decision making. That evaluation process used a scoring method which the business planning teams felt was inadequate for making informed and timely decisions. After further investigation it became clear that the teams were not in full agreement as to the specific set of factors that should comprise a complete project assessment. The result was frequent, and often lengthy, meetings held over a period of several months to assess specific projects. This time lag runs counter to the desire of Armstrong (and many other firms) to accelerate the product development cycle.

For competitive reasons, the strategy team wanted a new support system that would aid in considering the issues to be addressed during the discussions of each product development project.

This was the impetus for developing SMAS and other companion assessment systems [14].

As a result, a project was initiated to develop a knowledge-based support system for the strategic market assessment of possible new products. The system development effort received strong internal support and was initially sponsored by Armstrong's General Manager for Pioneering Research. This individual appointed the senior scientist for expert systems as the study liaison.

## 5. The strategic market assessment system (SMAS)

The design of SMAS was subject to extensive review and critique by Armstrong's floor products strategy team during a series of group sessions. The team fully supported it, since strategic market assessment is a major component of Armstrong's strategy. Key potential benefits which were identified by the strategy team include consistency in addressing market assessment issues, and clarity in processing the necessary information and communicating recommendations.

The KBDSS development methodology consists of the following tasks:

1. Knowledge Acquisition, which involves (a) becoming familiar with the problem characteristics and participants, (b) identifying concepts and relationships, and (c) extracting the knowledge from the expert(s);

2. Knowledge Modeling, which involves determining the appropriate models and using them to organize/model the knowledge;

3. Knowledge Representation, which involves codifying the knowledge, developing prototypes and also developing the necessary DSS modeling routines and support programs;

4. System Validation and Verification;

5. System Implementation; and

6. Follow-up Review and Maintenance.

## 5.1. Knowledge acquisition

The initial objective of this process was to develop some basic understanding of the overall project evaluation process and the significance of the strategic market assessment within that process. A series of interviews was conducted with the members of the strategy team on both an individual and collective basis. At the suggestion of the strategy team, several others were interviewed to clarify certain policies and procedures, especially as they affect marketing analysis of new product concepts. Once these tasks were accomplished, an intensive knowledge engineering effort was required to elicit from each of the two primary experts (managers of residential and commercial sales and marketing) their knowledge of the process and the criteria used to evaluate the strategic market potential of prospective products. Through intensive and frequent interaction, we began to determine the key project characteristics that influence their evaluations and recommendations. Questionnaires and other forms were completed by the experts in order to help organize and refine the ideas, criteria, and issues arising during the formal knowledge engineering sessions.

Expert knowledge includes the assessment criteria along with the associated sub-criteria, measurement scales, and data requirements; the weights assigned to the various evaluation factors; the process by which a numerical score and the supporting diagnostics would be generated; and the reasoning path for making market assessment decisions given the knowledge and data associated with a specific project. Direct assessment techniques, pairwise comparisons, and logic tables were used in varying degrees to allow the experts to assign weights to the evaluation factors.

The knowledge acquisition process also revealed significant differences in the evaluation of products targeted for the residential versus the commercial market sectors. Armstrong defines a “residential product” as a flooring product that will find eventual use by residential customers. “Commercial products” are sold for commercial or light commercial applications in end-use segments such as health care, education, mercantile, and institutions. The mix of factors and their relative impact on previous decisions for each market sector were extensively discussed.

Based on the results, a hierarchical structure chart was developed to represent the relationships between the criteria, sub-criteria, and ratings scales (see Fig. 1). This chart was reviewed and approved by the entire floor products strategy team.

## 5.2. Organizing and modeling the knowledge

Logic tables were used to elicit weights from experts when there were dependencies between the items being evaluated. In other situations, the AHP (as implemented in the software program

Expert Choice) was used to solicit pairwise comparisons of the items and to develop the necessary tradeoffs and weights. SMAS then views AHP as a knowledge engineering tool that can be used in conjunction with other approaches. The KBDSS approach is flexible enough to accommodate different knowledge acquisition and modeling techniques, such as regression analysis, discriminant analysis, utility models, multi-criteria decision making, and neural networks.

Pairwise comparisons were used to determine the importance of the seven top-level criteria (direct profit margin is not weighted since its impact is included in the financial assessment system) separately for the residential and commercial sectors. Specifically, this required a total of 21 ([7 × 6]/2) items to be pairwise compared for the residential sector of SMAS, and 21 for the commercial sector. In both cases, the weights of these criteria were determined by Expert Choice. A hypothetical set of pairwise comparisons and weights for the seven evaluation criteria are given in Table 1. Each criterion's weight was apportioned to its rating scale using pairwise comparisons with or without logic tables. To maximize flexibility and ease of maintenance, these adjusted weights were placed in database files (using the dBase III + software program). A series of if–then rules process the user's responses to the various questions about each of the evaluation criteria and obtain a total score which sums the scores over all seven criteria. This total is translated into a verbal strategic market assessment: high, good, moderate, fair or poor.

![](/api/attachments/XGMQZTSC/fulltext/images/2da5089ec663253b3bab24e7effd570965e55c6550f40fb49b69876f6d258706.jpg)  
Fig. 1. SMAS structure chart.

The AHP was used in developing the weights for the scales or categories associated with Target Market (TM), Future Market Opportunities (FMO), Competitive Situation (CS), Breadth of Line (BOL), and Sales Distribution (SD). In each of these cases, the AHP-derived weights had to be adjusted so that an absolute rating could be assigned to the project under evaluation. For example, if a candidate project was judged to have a “low” CS, an AHP local weight of .626 is appropriate in our example. Since “low” is the highest CS ratings category, then 100% of CS’s overall assessment weight of .063 (first matrix in Table 1) should be scored. Similarly, if “moderate” is selected, then .280/.626 = .447 or 44.7% of CS’s overall weight of .063 should be scored. This leads to an adjustment rule that requires dividing the local AHP weights for a criterion’s category or scales by the maximum local AHP weight associated with that criterion. This adjustment was consistently applied throughout SMAS.

The development of rating scale weights for the Market Segment (MS) and Sales (S) criteria required the use of logic tables and the AHP as summarized in Table 2. For example, the various levels of the First-Year Volume and Five-Year Growth Rate scales are combined through a logic table to provide overall Sales ratings. Also, a “Moderate” First-Year Volume and a “Fair” First-Year Growth Rate leads to a “Fair” Sales rating. The weights attached to the specific Sales ratings were developed using pairwise comparisons. A “Fair” sales rating has an adjusted weight of .146.

The development of rating scale weights for the market segment (MS) criterion required the use of a logic table. For the residential sector, four key market segments were identified Do-It-Yourself (DIY), Build-It-Yourself (BIY), Professional, and Builder. Note that a “+” is assigned if the new product will compete in a given market segment, and a “−” is assigned if it will not. Depending on the number and specific market segments where the product will compete, an MS rating assessment of very favorable (VF), favorable (F), somewhat favorable (SF), acceptable (A), or poor (P) is assigned. Again, the adjusted AHP process used to assign weights to these five ratings categories is the same as in the other criteria. For example, if a “+” is assigned to “Professional” and “−” to the rest, an “Acceptable” rating is assessed. This corresponds to an adjusted AHP weight of .191. A different set of market segments are used for the commercial sector.

## 5.3. Knowledge representation and prototype development

Rapid prototyping was used throughout the SMAS development process. After each formal knowledge acquisition session was completed, the information was analyzed and SMAS prototypes were provided to the experts for testing and evaluation. This enabled the timely identification of problems, accelerating the convergence toward an acceptable system. Keeping the experts involved gave them a sense of ownership and a certain level of comfort and confidence with the system, both of which are well-known critical success factors.

After experimentation and development of initial prototypes with several expert system shells, we found that Level5 possessed the flexibility suitable for our needs. Both experts tested SMAS \*\* Adjusted AHP weights are obtained by dividing the AHP-derived weights by the maximum AHP weight.

Table 1  
Deriving adjusted AHP weights for SMAS - residential sector

<table><tr><td colspan="8">Overall assessment criteria</td><td></td></tr><tr><td></td><td>TM</td><td>S</td><td>FMO</td><td>MS</td><td>SD</td><td>CS</td><td>BOL WTS</td><td></td></tr><tr><td>TM</td><td></td><td>3</td><td>3</td><td>4</td><td>5</td><td>3</td><td>4 0.341</td><td></td></tr><tr><td>S</td><td></td><td></td><td>1</td><td>3</td><td>4</td><td>2</td><td>5 0.189</td><td></td></tr><tr><td>FMO</td><td></td><td></td><td></td><td>3</td><td>4</td><td>2</td><td>4 0.183</td><td></td></tr><tr><td>MS</td><td></td><td></td><td></td><td></td><td>3</td><td>3</td><td>3 0.111</td><td></td></tr><tr><td>SD</td><td></td><td></td><td></td><td></td><td></td><td>2</td><td>3 0.069</td><td></td></tr><tr><td>CS</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1 0.063</td><td></td></tr><tr><td>BOL</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.044</td></tr><tr><td colspan="8">Inconsistency Ratio = 0.078</td><td></td></tr><tr><td colspan="8">Target market (TM) *New Armstrong Competitor WTS ADJ WTS **</td><td></td></tr><tr><td>New</td><td></td><td>6</td><td></td><td>4</td><td></td><td>0.701</td><td>1.000</td><td></td></tr><tr><td>Armstrong</td><td></td><td></td><td></td><td>1/2</td><td></td><td>0.106</td><td>0.151</td><td></td></tr><tr><td>Competitor</td><td></td><td></td><td></td><td></td><td></td><td>0.193</td><td>0.275</td><td></td></tr><tr><td colspan="8">Inconsistency Ratio = 0.009</td><td></td></tr><tr><td colspan="8">Future market opportunities *High Moderate Low WTS ADJ WTS **</td><td></td></tr><tr><td>High</td><td></td><td>4</td><td></td><td>7</td><td>0.696</td><td>1.000</td><td></td><td></td></tr><tr><td>Moderate</td><td></td><td></td><td></td><td>4</td><td>0.229</td><td>0.329</td><td></td><td></td></tr><tr><td>Low</td><td></td><td></td><td></td><td></td><td>0.075</td><td>0.108</td><td></td><td></td></tr><tr><td colspan="8">Inconsistency Ratio = 0.073</td><td></td></tr><tr><td colspan="8">Competitive Situations (CS) *High Moderate Low WTS ADJ WTS **</td><td></td></tr><tr><td>High</td><td></td><td>1/4</td><td></td><td>1/5</td><td>0.094</td><td>0.150</td><td></td><td></td></tr><tr><td>Moderate</td><td></td><td></td><td></td><td>1/3</td><td>0.280</td><td>0.447</td><td></td><td></td></tr><tr><td>Low</td><td></td><td></td><td></td><td></td><td>0.626</td><td>1.000</td><td></td><td></td></tr><tr><td colspan="8">Inconsistency Ratio = 0.082</td><td></td></tr><tr><td colspan="8">Breadth of Line (BOL) *Narrow S. Narrow Wide V. WTS ADJ WTS **</td><td></td></tr><tr><td>Narrow</td><td></td><td>3</td><td></td><td>4</td><td>5</td><td>0.537</td><td>1.000</td><td></td></tr><tr><td>S. Narrow</td><td></td><td></td><td></td><td>2</td><td>5</td><td>0.259</td><td>0.482</td><td></td></tr><tr><td>Wide</td><td></td><td></td><td></td><td></td><td>2</td><td>0.132</td><td>0.246</td><td></td></tr><tr><td>V. Wide.</td><td></td><td></td><td></td><td></td><td></td><td>0.072</td><td>0.134</td><td></td></tr><tr><td colspan="8">Inconsistency Ratio = 0.039</td><td></td></tr><tr><td colspan="8">Sales Distribution (SD) *High Moderate Low WTS ADJ WTS **</td><td></td></tr><tr><td>High</td><td></td><td>4</td><td></td><td>5</td><td>0.683</td><td>1.000</td><td></td><td></td></tr><tr><td>Moderate</td><td></td><td></td><td></td><td>2</td><td>0.200</td><td>0.293</td><td></td><td></td></tr><tr><td>Low</td><td></td><td></td><td></td><td></td><td>0.117</td><td>0.171</td><td></td><td></td></tr><tr><td colspan="8">Inconsistency Ratio = 0.023</td><td></td></tr></table>

Inconsistency Ratio = 0.023  
\* All of the categories under each criterion are defined and illustrated within SMAS; e.g., a high Target Market (TM) might be one where estimated compound growth rate exceed 20% or more over a five year period.

extensively and became dedicated users and proponents of the system. Their efforts allowed the rapid development of a number of prototypes leading to the final model and system.

In its latest release, SMAS's knowledge base contains 130 rules (see Fig. 2 for sample rules) that are supported by database files holding 83 data items. These represent scoring model weights developed by AHP and other knowledge acquisition techniques.

## 5.4. System validation and verification

SMAS was subject to extensive and formal evaluation efforts. The verification and validation procedures integrated throughout the SMAS development life cycle were consistent with the proposed frameworks and guidelines $[17,19]$ as well as the paradigms $[18, 20]$ described by other researchers. These procedures addressed content, construct, subsystem, and input validity issues. For example, content validity procedures included (1) comparison of the system's performance with that of different experts (face validity); and (2) use of historic test cases to compare system performance against known results. In addition, a special strategy team subcommittee performed an in-depth assessment of twelve different projects (some completed and some active) representing the spectrum of project types that SMAS would be expected to handle.

The experts along with other potential users also participated in the intensive validation/verification process. This proved critical to the eventual success of the system.

## 5.5. System implementation and use

Since market assessment has a significant impact on decisions concerning continued product development, the members of the various business planning teams are the principal users of SMAS. The product development teams also use it as a guide in gathering the information necessary to prepare preliminary product evaluations that they present to the business planning teams. The system, in effect, provides access to the same process and the same evaluation criteria across the various levels of decision making.

SMAS begins by asking the user questions concerning the time to develop/market the product. If the time to market does not meet Armstrong's standards, the system produces appropriate warning messages. The remainder of the assessment process is dependent on whether the product is targeted for the residential or commercial market sectors. The scales for many of the criteria reflect an implied comparison between the product being evaluated and others currently being marketed by Armstrong and its competitors. This approach is necessary, since market feedback is, of course, not available at the time the strategic market assessment is being made.

The user responses to the various questions fire a series of if–then rules eventually leading to a normative evaluation (i.e., score) as well as other supporting outputs, including

(a) Final strategic market assessment for the new product concept;

(b) Summary information describing how the market assessment for each of the evaluation criteria was reached (Fig. 3);

(c) Diagnostic warnings when certain conditions are violated (e.g., time to develop/market exceeds company standard); and

(d) Explanations of system actions, reasoning path, and conclusions (available on user request).

The results can be both displayed and/or printed and are also saved in a case file for later use.

An important advantage of SMAS over previous systems is its ease of use. Level5 provides SMAS with a friendly interface that enables it to question the user concerning preferences and as-

Table 2  
Developing the market segment and sales assessment ratings and score

<table><tr><td colspan="5">Market Segment Logic Table</td><td colspan="8">Market Segment Ratings Weights</td></tr><tr><td>DIY</td><td>BIY</td><td>PROF</td><td>BUILDER</td><td>RATING</td><td></td><td>VF</td><td>F</td><td>SF</td><td>A</td><td>P</td><td>Wts</td><td>Adj * Wts</td></tr><tr><td>+</td><td>+</td><td>+</td><td>+</td><td>VF</td><td>VF</td><td></td><td>2</td><td>4</td><td>5</td><td>8</td><td>0.460</td><td>1.000</td></tr><tr><td>+</td><td>+</td><td>+</td><td>-</td><td>F</td><td>F</td><td></td><td></td><td>2</td><td>4</td><td>6</td><td>0.273</td><td>0.593</td></tr><tr><td>·</td><td>·</td><td>·</td><td>·</td><td></td><td>SF</td><td></td><td></td><td></td><td>2</td><td>3</td><td>0.136</td><td>0.296</td></tr><tr><td>·</td><td>·</td><td>·</td><td>·</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>·</td><td>·</td><td>·</td><td>·</td><td></td><td> $\Lambda$ </td><td></td><td></td><td></td><td></td><td>3</td><td>0.088</td><td>0.191</td></tr><tr><td>-</td><td>-</td><td>+</td><td>-</td><td>A</td><td>P</td><td></td><td></td><td></td><td></td><td></td><td>0.043</td><td>0.093</td></tr><tr><td>·</td><td>·</td><td>·</td><td>·</td><td></td><td colspan="8">Inconsistency Ratio = 0.019</td></tr><tr><td>·</td><td>·</td><td>·</td><td>·</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>·</td><td>·</td><td>·</td><td>·</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>P</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Legend: VF = Very Favorable; F = Favorable; SF = Somewhat Favorable; A = Acceptable; P = Poor

Sales Assessment Logic Table Sales Ratings Weights

<table><tr><td>1st Yr</td><td>5 Yr</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Adj *</td></tr><tr><td>Vol</td><td>Gwth</td><td>Rating</td><td></td><td>H</td><td>G</td><td>M</td><td>F</td><td>P</td><td>Wts</td><td>Wts</td></tr><tr><td>H</td><td>H</td><td>H</td><td>H</td><td></td><td>3</td><td>4</td><td>6</td><td>7</td><td>0.492</td><td>1.000</td></tr><tr><td>H</td><td>H</td><td>G</td><td>G</td><td></td><td></td><td>3</td><td>4</td><td>6</td><td>0.264</td><td>0.537</td></tr><tr><td>.</td><td>.</td><td>.</td><td>M</td><td></td><td></td><td></td><td>2</td><td>4</td><td>0.128</td><td>0.260</td></tr><tr><td>.</td><td>.</td><td>.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>.</td><td>.</td><td>.</td><td>F</td><td></td><td></td><td></td><td></td><td>2</td><td>0.072</td><td>0.146</td></tr><tr><td>M</td><td>F</td><td>F</td><td>P</td><td></td><td></td><td></td><td></td><td></td><td>0.044</td><td>0.089</td></tr><tr><td>.</td><td>.</td><td>.</td><td colspan="8">Inconsistency Ratio = 0.035</td></tr><tr><td>.</td><td>.</td><td>.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>.</td><td>.</td><td>.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>P</td><td>P</td><td>P</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Legend: H = High; G = Good; M = Moderate; F = Fair  
Adjusted Weights obtained by dividing the AHP-derived Weights by the maximum AHP Weight

RULE M2.1
IF Time To Develop And Market <= 20
THEN Time To Market Assessment IS Meets Standard
ELSE Time To Market Assessment IS Does Not Meet Standard
AND DISPLAY Time To Market Warning

## RULE M3.4

IF Time To Develop And Market <= 28
AND Market Segment Commercial IS Mercantile
THEN Commercial Time To Fashion Has Been Assessed
AND Time To Fashion Assessment IS Meets Standard

## RULE RM5.2

IF Residential First Year Volume IS High . . 8.1 millions of sq. ft. or above AND Five Year Compound Growth Rate IS Fair . . 5.6 - 6.9 millions of sq. ft. THEN Sales IS Good

AND Total\_Market := Total\_Market + (MARKET\_R\_BASE.SALES \* MARKET\_R\_BASE.SALES\_G)

## RULE CM5.2.7

IF Commercial Sheet First Year Volume IS Poor .. 2.3 millions of sq. ft. or less
AND Five Year Compound Growth Rate IS High .. 4.5 % or higher
THEN Sales IS Good
AND Total\_Market := Total\_Market + (MARKET\_C\_BASE.SALES \*
MARKET\_C\_BASE.SALES\_G)

Fig. 2. SMAS sample rules.

sessments relating to the various criteria, sub-criteria and evaluation factors. Furthermore, the user can request explanations from the system about certain questions and why they are being asked, how conclusions are derived, and what is known at any point in time during the consultation.

The implementation process was accomplished through close cooperation with Armstrong's senior scientist responsible for expert systems. In addition, a systems facilitator was appointed to assist the various user groups with data preparation and related procedures, and to coordinate the system's usage. The implementation plan allows SMAS to be run as a stand-alone system, or in conjunction with a multi-expert KBDSS, called PRAS (Project Assessment System). This system differs from SMAS in that it captures the collective expertise of the entire Floor Products Strategy Team concerning product evaluation, involving customer satisfaction, finance, marketing, manufacturing, and technology assessments. PRAS brings together SMAS and these other KBDSS's to yield a comprehensive evaluation of a product development effort [14].

![](/api/attachments/XGMQZTSC/fulltext/images/74b9fa94dfcf3fdda90c217ffffda9f2c279826e2de9c757a49874297d81e34e.jpg)  
Fig. 3. SMAS sample output summary.

SMAS went on-line at Armstrong World Industries in November, 1991. The strategy team requires that all active strategic projects be run through SMAS and its companion systems. In addition, four of the six tactical teams have made multiple runs for six active projects, while the newly established global team has tested these systems with a “live” project. A survey conducted by Armstrong of all SMAS users to-date has indicated complete satisfaction with the system. Armstrong is implementing a New Product Delivery (NPD) Process that will recommend the use of SMAS and its companion systems across all planning levels – global, strategic, and tactical.

## 5.6. Knowledge maintenance and learning

The need to adapt to changing market conditions was specifically taken into account in designing SMAS. By storing the AHP and scoring model weights in database files, changes in weights can be made easily by modifying the appropriate records. Changes in the criteria or their interrelationships require altering the knowledge base.

In order to enable SMAS to remain an effective support tool in a changing environment, formal procedures have been established for monitoring its effectiveness on a continuing basis. A case history database is also planned to enhance the present monitoring system. The contents of the database will include the user's assessments and responses to system questions and SMAS's evaluation and recommendation. In addition, the actual decisions taken by the business planning teams and possibly some measures of product success will be added to the database. The case history database could be used to assist in reviewing the effectiveness of SMAS and maintaining/updating the system as necessary.

The case history database could be used to spur development of future evaluation systems that are even easier to use and maintain. For example, the database could be processed by an inductive expert system, a neural network, or case-based reasoning software to better isolate those factors and relationships that lead to better market performance of specific product development projects. Armstrong plans to maintain the necessary case history files for future systems development.

## 6. Summary and conclusions

Here, we have applied a field-tested, structured methodology and framework for the development of knowledge-based decision support systems for strategic market assessment. We have demonstrated the hierarchical structure of one such system and provided examples of the types of knowledge that this system can process in its knowledge base. The application of several innovative methods and techniques for knowledge acquisition and modeling was reported. The specific KBDSS described was subject to extensive testing, verification, and validation, and is now in full-scale implementation.

The experience gained with it and other related systems development efforts supports the proposition that the KBDSS approach is an appropriate modeling framework for new product development evaluation. Several key contributing factors should be recognized. First, automated knowledge processing and modeling tools helped to reduce the time required for systems development, and provided a mechanism for documenting the development and necessary modifications of the various scoring weights. Second, the expert system shell provided much-needed flexibility for both systems development and structuring the user interface. Third, the support of the information systems technical staff provided valuable assistance in managing the interface between experts, users and systems developers.

Strategic market assessment is essential for the evaluation of new product development projects. The KBDSS approach has means for collecting, organizing, processing, and modeling the expertise of knowledgeable marketing managers and other strategy team members, and it can incorporate the results of marketing research. Disseminating and utilizing this valuable knowledge can enable a firm to improve its strategic assessment processes. The on-going usage of SMAS as a decision support tool by the experts and the other strategy team members at Armstrong is an important indication of the merits of the approach.

## References

[1] Baker, N.R. (1974) R&D project selection models: an assessment. IEEE Transactions on Engineering Management, EM-21, 165–171.

[2] Balachandra, R. (1989) Early Warning Signals for R&D Projects. Lexington MA, Lexington Books.

[3] Booz Allen and Hamilton (1982) New Product Management for the 1980's. Booz Allen and Hamilton, Inc.

[4] Cooper, R.G. (1985) Selecting winning new product projects using the NewProd system. Journal of Product Innovation Management, 2, 34–44.

[5] El-Najdawi, M.K. and Stylianou, A.C. (1993) Expert support systems: Integrating AI technologies. Communications of the ACM, 36(12).

[6] Fortune (1989) How to regain the productive edge. (May 22), 92–104.

[7] Goslar, M.D. and Brown, S.W. (1986) Decision support systems: Advantages in consumer marketing settings. The Journal of Consumer Marketing, 3(3), 43–50.

[8] Gupta, S.K. and Taube, L.R. (1985) State of the art survey on project management. In B.V. Dean(Ed.), Project Management: Methods and Studies, North-Holland, Amsterdam, 293–313.

[9] Higby, M.A. and Farah, B.N. The status of marketing information systems, decision support systems and expert systems in the marketing function of U.S. firms. Information and Management, 20, 29–35.

[10] Kettelhut, M.C. (1991) Using a DSS to incorporate expert opinion in strategic product development funding decisions. Information and Management, 20, 363–371.

[11] Liberatore, M.J. (1987) An extension of the analytic hierarchy process for industrial R&D project selection and resource allocation. IEEE Transactions on Engineering Management, EM-34, 12–18.

[12] Liberatore, M.J. (1989) A decision support approach for R&D project selection. In B.L. Golden, E.A. Wasil, and P.T. Harker (Eds.) The Analytic Hierarchy Process: Applications and Studies, Heidelberg, Germany, Springer-Verlag, 82–100.

[13] Liberatore, M.J. and Titus, G.J. (1983) The practice of

management science in R&D project management. Management Science, 29, 962–974.

[14] Liberatore, M.J. and Stylianou, A.C. (1994) Expert support systems for new product development decision making: A modeling framework and applications. Management Science, forthcoming.

[15] Mentzer, J.T. and Gandhi, N. (1992) Expert systems in marketing: guidelines for development. Journal of the Academy of Marketing Science, 20(1), 71–80.

[16] Moutinho, L. and Paton, R. (1988) Expert systems: A new tool in marketing. The Quarterly Review of Marketing, (Summer), 5–13.

[17] O'Keefe, R.M., Balci, O. and Smith, E.P. Validating expert system performance. IEEE Expert, 2(4), 81–89.

[18] O'Leary, T.J., Goul, M., Moffitt, K.E. and Radwan, A.E. (1990) Validating expert systems. IEEE Expert, 51–58.

[19] O'Leary, D.E. (1987) Validation of expert systems – with applications to auditing and accounting expert systems. Decision Sciences, 18(3), 468–486.

[20] Radwan, A.E., Goul, M., O'Leary, T.J. and Moffitt, K.E. (1989) A verification approach for knowledge-based systems. Transportation Research, 23A(4), 287–300.

[21] Ram, S. and Ram, S. (1988) INNOVATOR: An expert system for new product launch decisions. Applied Artificial Intelligence, 2, 129–148.

[22] Saaty, T.L., (1980) The analytic hierarchy process. New York, McGraw-Hill.

[23] Schwoerer, J. and Frappa, J. (1986) Artificial intelligence and expert systems: any applications for marketing and marketing research. European Research, 14(4), 510–524.

[24] Sisodia, R.S. (1991) Expert systems for services marketing – prospects and payoffs. Journal of Services Marketing, 5(3), 37–54.

[25] Watts, K.M. and Higgins, J.C. (1987) The use of advanced management techniques in R&D. Omega, 15, 21–29.

[26] Wilkinson, A. (1991) Developing an expert system on project evaluation. R&D Management, 21, 19–29.

![](/api/attachments/XGMQZTSC/fulltext/images/c87e2c79b89496a2032199f15e95c4c1397da0ea7a7569f300a02d89832aa652.jpg)

Matthew J. Liberatore is Professor and Chairperson of the Department of Management at Villanova University. He received his Ph.D. in operations research from the University of Pennsylvania. His previous industrial experience includes positions with RCA and FMC corporations. Dr. Liberatore serves as production/operations editor Interfaces, and is a member of the editorial boards of the American Journal of Mathematical and

Management Sciences and Entrepreneurship Theory and Practice. He has published extensively in the areas of management science, information systems, and strategic management. His current research focuses on project evaluation methods and systems, and management science and information systems applications in research and technology management.

![](/api/attachments/XGMQZTSC/fulltext/images/fac338897155ff875f14d2ac121316954b4d92bae4c3be2ba524c03cb8dfbdcc.jpg)

Anthony C. Stylianou is assistant professor of management information systems at the University of North Carolina at Charlotte. He received his Ph.D. in MIS from Kent State University. Dr. Stylianou has published articles in the Communications of the ACM, Management Science, Decision Sciences, Journal of Management Systems, Computers in Personnel, and other journals. He is currently doing research on the use of expert systems and neural networks in R&D and financial areas, the application of total quality management techniques in the information systems function, the use of information technologies in the banking industry, and issues related to the potential of information technology for providing a competitive advantage in an international market.
