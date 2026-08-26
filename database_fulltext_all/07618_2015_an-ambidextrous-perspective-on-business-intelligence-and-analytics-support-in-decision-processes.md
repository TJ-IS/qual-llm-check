---
otero_id: 7618
otero_key: "XE9WZG28"
title: "An ambidextrous perspective on business intelligence and analytics support in decision processes: Insights from a multiple case study"
authors: "Martin Kowalczyk; Peter Buxmann"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.08.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An ambidextrous perspective on business intelligence and analytics support in decision processes: Insights from a multiple case study

Martin Kowalczyk ⁎, Peter Buxmann <sup>1</sup>

Technische Universität Darmstadt, Hochschulstr. 1, 64289 Darmstadt, German

## a r t i c l e i n f o

Article history: Received 22 May 2014 Received in revised form 15 May 2015 Accepted 26 August 2015 Available online 4 September 2015

Editor: James R Marsden

Keywords: Business intelligence and analytics Decision processes Ambidexterity

## a b s t r a c t

Providing data-centric decision support for organizational decision processes is a crucial but challenging task. Business intelligence and analytics (BI&A) equips analytics experts with the technological capabilities to support decision processes with reliable information and analytic insights, thus potentially raising the quality of managerial decision making. However, the very nature of organizational decision processes imposes conflicting task requirements regarding adaptability and rigor. This research proposes ambidexterity as a theoretical lens to investigate data-centric decision support. Based on an in-depth multiple case study of BI&A-supported decision processes, we identify and discuss tensions that arise from the conflicting task requirements and that pose a challenge for effective BI&A support. We also provide insights into tactics for managing these tensions and thus achieving ambidexterity. Additionally, we shed light on the relationship between ambidexterity and decision quality. Integrating the empirical findings from this research, we propose a theory of ambidexterity in decision support, which explains how such ambidexterity can be facilitated and how it affects decision outcomes. Finally, we discuss the study's implications for theory and practice.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Data-centric decision support is vital for managerial decision making in organizational decision processes. Business intelligence and analytics (BI&A) equips analytics experts (i.e., analysts or data scientists) with the technological capabilities to support decision processes with reliable information and analytic insights [1–4]. The added value of BI&A is based on increasing the utilization of “data-driven” decision making and thus improving decision quality and organizational performance [5–7]. However, realization of these benefits is not assured, and the very nature of organizational decision processes poses challenges for effective BI&A support.

First, the reality of organizational decision processes has often been characterized as nonroutine and ill-structured [8–11]. In these situations, ambiguity prevails and the right questions are not always obvious at the outset. Rather, questions and solution alternatives are developed as part of the decision process and are subject to change [8,10]. As a consequence, data processing and analytics requirements can change frequently [12]. To achieve effective decision support in such nonroutine processes, the analysts who are involved must be able to adjust to these changes and, as a consequence, must maintain a high degree of adaptability and flexibility in their procedures.

Second, effective decision support with BI&A requires analysts to have a high level of specialization in analytics, which is different from the domain knowledge of decision makers, and this leads to further challenges [13]. Specifically, a high degree of analytics elaboration often makes it difficult for decision makers to assess the quality of the analytic advice they receive, due to their lack of analytics knowledge [12,13]. Findings from the cognitive sciences suggest that such knowledge gaps induce information asymmetries, and these can lead decision makers to neglect analysts' advice and to instead overly rely on their own assessment of the decision situation [14,15]. To mitigate this risk, analysts are supposed to provide transparency and alignment with decision makers regarding their procedures and goals in deriving the analytic advice [16,17]. This means that analysts have to ensure the rigor of their procedures in order to achieve coherence and traceability in the decision support that they provide.

In summary, analysts face decision process requirements that appear to be conflicting, or at least difficult to achieve simultaneously. Failure to meet these conflicting demands can thwart the potential benefits of BI&A support. However, despite their critical importance for the success of BI&A support, prior research has not considered these conflicting demands and their implications for managerial decision making. Therefore, in-depth research on this topic is required in order to gain a better understanding of the challenges that analysts face in supporting decision processes with BI&A. Organizational ambidexterity describes the capability of managing conflicting demands and as such provides a useful theoretical lens for our research [18,19]. We use a multiple case study approach to investigate BI&A support of managerial decision making and thus respond to the identified need for research on actual decision processes [20–22].

This paper makes several contributions. (1) We characterize and present previously unexplored tensions that pose a challenge for analysts' ability to provide effective BI&A support in organizational decision processes. (2) We provide insights into the tactics that analysts use to successfully manage those tensions, i.e., tactics that facilitate ambidexterity. (3) Through an investigation of decision processes with varying levels of ambidexterity, we provide initial evidence concerning the effects of ambidexterity by examining its impact on decision quality as well as its influence on decision makers' reliance on rationality and intuition in decision making. (4) Grounded in these empirical findings, we propose a theory of ambidexterity in decision support that addresses how this ambidexterity can be facilitated and how it affects decision outcomes. These contributions have great practical significance, as analysts need to be aware of the tensions and tactics in order to ensure the effectiveness and utilization of their BI&A support.

The remainder of this paper is structured as follows. In Section 2, we discuss the theoretical background for BI&A, conceptions of decision making, and organizational ambidexterity. In Section 3, we describe the details of our empirical study design and the data analysis procedure for our multiple case study research approach. In Section 4, we present the results from the multiple case study. Finally, in Section 5, we close with a discussion of the study's findings and limitations as well as possible directions for future research.

## 2. Theoretical background

This section provides on overview of BI&A and presents conceptions of decision making that have been developed in management and cognitive sciences. It also elaborates on the challenging requirements that organizational decision processes pose for realizing effective BI&A support and introduces conceptions of ambidexterity from management and information systems research.

## 2.1. Data-centric decision support with business intelligence and analytics

BI&A, which has its origins in data-centric approaches such as data warehousing, comprises a number of data collection, integration, and analytics technologies [1,20,23]. BI&A systems aim to improve data processing in order to increase the quality of the information that is available for decision making [1,24]. In this regard, BI&A encompasses a number of basic analytics capabilities, such as online analytical processing, ad hoc queries, and descriptive statistics, as well as advanced analytics capabilities for data mining, prediction, and optimization [1,3,20,23].

With an increasing level of analytics capabilities, the utilization of BI&A for delivering data-centric decision support becomes a specialized task, which requires analytics experts – for instance, data scientists or analysts – to support managerial decision makers [3,13]. Hence, analytic advances induce a knowledge gap between analysts, who specialize in analytics, and decision makers, who have domain-specific knowledge [13]. Due to their lack of analytics knowledge, decision makers have to rely on analysts in the context of BI&A-supported decision processes. At the same time, analysts depend on the domain-specific knowledge of decision makers for developing relevant analytic insights and advice. As a consequence, effective BI&A support requires collaboration between analysts and decision makers [13,22].

Prior research on decision support has mainly assumed decision contexts in which decisions are made by either isolated, individual decision makers or groups of equal, undifferentiated decision makers [21,25]. The implications of specialization, collaboration, and an uneven distribution of decision-making power between decision makers and analysts has not been adequately considered in the literature, despite being highly relevant in practice [12,13,22]. Our research investigates such decisionmaking setups from the underexplored perspective of analysts, focusing on the challenges that arise for effective utilization of BI&A in organizational decision processes.

## 2.2. Conceptions of decision making in management and cognitive sciences

Insights from management and cognitive sciences provide the foundation for a better understanding of the challenges for effective BI&A support of organizational decision processes. In both research areas, interrelated conceptions have been developed that distinguish between more rational and more intuitive modes of information processing and decision making [26–28]. Whereas management research distinguishes between rationality and intuition as two main properties that can characterize decision processes [29–32], cognitive sciences investigate associated cognitive processes under the designation “dual-process theories” [33–35]. We will focus on relations between the two domains and discuss their implications for decision processes.

Although there are variations among dual-process theories, they all distinguish between cognitive processes that are fast, automatic, effortless, and associative and those that are slow, controlled, effortful, and deductive [34,35]. A widely adopted practice in the cognitive sciences designates these two modes of processing as “System 1” and “System 2” [35,36]. System 1 and System 2 are viewed as working concurrently. System 1 is assumed to quickly propose intuitive answers to decision problems, while System 2 is supposed to control the quality of these proposals [35]. However, this is not always the case, as the rational reasoning associated with System 2 requires considerable cognitive effort, and such effort is considered to be limited by human cognitive capacity. Rather, individuals tend to use heuristics or mental shortcuts as adjuncts to System 1 in order to reduce the effort involved in processing difficult tasks. These heuristics have been found to lead to different kinds of systematic errors and to result in biased decision making [37].

In this context, intuition is regarded as decision making that retains a hypothesized proposal from System 1 without control by System 2 [35]. Hence, intuitive judgment is based on System 1 processing and arrives at decisions through informal reasoning without the use of analytical methods or deliberative calculation [38]. In contrast, rational decision making relates to System 2 processing and includes the acquisition of information through conscious reasoning and deliberative analytical thought [39]. In sum, dual-process theories offer cognitive explanations for an interaction between intuition and rational analysis in managerial decision making [28].

In management research, the rationality of decision processes has been investigated both theoretically and empirically [8,29,40,41]. Rationality has been characterized as systematic information gathering and reliance on analysis for the purpose of decision making [29,40,42,43]. Existing evidence about the relationship between rationality and the quality of decision outcomes mainly supports a positive relationship [42, 9,11]. Nevertheless, the presumption that only rationality should be considered in decision making research has been called into question [8,31].

Intuition has been proposed as providing an alternative approach to managerial decision making, particularly for decisions involving ambiguous or uncertain situations. These situations are characterized as having excessive cognitive processing requirements, entailing that decision makers might not be able to utilize rational processes [30,32,39,44]. Intuition has been defined as an interplay between knowing and sensing, which allows understanding to be attained without explicit analytical inferences [28,39,44]. Very few studies have investigated the direct relationship between intuition and decision outcomes, and those that have done so provide an inconclusive picture. Intuition has been found to have a positive effect on decision outcomes in unstable decision environments and a negative effect in stable decision environments [30]. Furthermore, intuition has been found to significantly increase the occurrence of major unexpected, negative decision outcomes [45]. In consequence, intuition is seen as a “troublesome decision tool” [44], and most authors caution that sole reliance on intuition creates a risk in the decision making process [9,32,45,46]. Based on these findings, some researchers suggest the possibility of interactions between intuition and rationality as components of decision making [39,44,47].

The implications of interactions between intuition and rationality in the context of BI&A-supported decision processes remain unexplored, and our understanding of their effects on decision outcomes is limited. From the analyst's perspective, the goal is to deliver analytic insights that will be utilized by decision makers in the decision process [13]. Hence, analysts aim at raising the level of rationality in managerial decision making and thus improving decision quality. However, as will be discussed in the next section, task specialization and the constitution of decision processes pose challenges for analysts' effectively contributing to these ends.

## 2.3. Decision processes and challenges for effective BI&A support

The effectiveness of the BI&A support that analysts provide to decision makers faces challenges stemming from specialization and the constitution of organizational decision processes.

The constitution of a decision process is related to the structure and perceived ambiguity of the decision situation. It is important to note that owing to the nonroutine character of managerial decisions, related tasks are subject to frequent changes and have often been found to be iterative [8,10,11]. This has immediate consequences for BI&A support of decision processes. More specifically, analysts often find themselves in nonroutine decision situations that are ambiguous, with the appropriate questions not obvious at the outset. As a consequence, early definition of information needs can be difficult, and data processing and analytics requirements can change frequently throughout the decision process. These circumstances require analysts to maintain a high degree of flexibility and adaptability in the procedures they utilize in order to effectively support decision makers. Failure to achieve this adaptability typically leads to defective analytic procedures and ineffective solutions [12]. This is a critical issue, because research has found that decision makers revert to intuitive decision making in uncertain or ambiguous decision situations [30,32,39,44]. Hence, if analysts cannot deliver effective analytic advice, they won't be capable of raising the level of rationality in such decision situations and the probability that the decisions will be based mainly on intuition might even increase. Therefore, adaptability is a crucial requirement that poses a challenge for analysts in providing effective BI&A support.

Specialization in BI&A-supported decision processes requires collaboration between the analysts, who contribute analytics capabilities, and the decision makers, who contribute domain-specific knowledge [12,13,22]. To develop relevant analytic insights, analysts must integrate their analytics capabilities with the domain-specific knowledge of decision makers [13]. Complicating the situation, in most organizations, such collaboration is embedded in formalized roles and hierarchies in which decision-making power is seldom distributed equally [22,48].

The cognitive sciences investigate the implications of such decisionmaking setups under the “judge–advisor system” (JAS) paradigm [14,49] and provide insights about advice utilization and discounting [14,17]. From the analyst's perspective, developing analytic advice is not enough, because decision makers frequently have difficulty assessing the quality of analytic advice due to their lack of analytics knowledge [12]. The persistence of such knowledge gaps can induce information asymmetries and uncertainty, which can lead decision makers to neglect advice and instead rely on their own experience [14]. This “egocentric advice discounting,” in which decision makers tend to overemphasize their own evaluation of a decision problem, is one of the most robust findings of the JAS literature [14,15]. Researchers have found that advice discounting occurs mainly because decision makers have access to their internal justifications when making a particular decision, but not to their advisors' procedures, evidence, and reasoning [15]. Hence, evaluation of the advice becomes difficult and uncertain for them. Findings from JAS research suggest that creating transparency and trust might overcome such uncertainty [16,17].

In this regard, reducing knowledge gaps and related information asymmetries in BI&A-supported decision processes seems to be crucial for promoting the utilization of analytic advice. If these gaps persist, decision makers will most likely discount analytic advice and instead rely heavily on their experience-based assessments of decision problems, which decreases the potential for improving rationality and increases the probability that these decisions will be based primarily on intuition. Hence, analysts need to be transparent about their goals and the procedures they use to derive their analytic advice if they want to demonstrate alignment with decision makers and thus create traceability and trust for their analytic advice. Consequently, BI&A support of decision processes necessitates well-structured and traceable procedures. Thus, analysts have the challenge of structuring their procedures adequately in order to align with the decision makers and provide transparency concerning their procedures and delivery of analytic advice.

In summary, analysts are confronted with decision process requirements that demand procedures that are adaptable and flexible, on the one hand, and that provide traceability and alignment, on the other. Simultaneous fulfillment of both needs has been considered difficult, and organizational ambidexterity has been suggested for approaching such conflicting demands [18,19,50].

## 2.4. Ambidexterity and decision processes

The previous sections showed that high demands are placed on analysts and BI&A support in decision processes. Approaching such processes from the perspective of ambidexterity can be useful for gaining insights about the relations between those demands. In general, ambidexterity concerns conflicting task requirements and induced tensions that are difficult to resolve. Previous research has identified various dichotomies involved in conflicting demands, such as alignment and adaptability [19], rigor and agility [50], and efficiency and flexibility [51]. Although the tensions that result cannot be entirely eliminated, successful organizations are capable of reconciling them by simultaneously dealing with the conflicting demands [18,19]. Hence, ambidexterity has often been described as a means to manage such conflicting demands [52].

Based on the demands of decision processes, the concepts of alignment and adaptability and the related process-oriented concepts of rigor and agility seem to be particularly relevant to our research. On the one hand, aspects of BI&A-supported decision processes involving information asymmetries are related to the alignment or rigor dimension. Process rigor has been defined as adherence to predefined, formal, and structured processes, which include explicit definitions of roles, activities, work products, and methods [50]. Achieving rigor throughout a decision process can reduce knowledge gaps and information asymmetries by explicitly specifying procedures and thus increasing transparency and enhancing understanding. On the other hand, aspects of decision processes that concern the unstructured nature of those processes are related to the adaptability or agility dimension. Consistent with the literature, we consider agility to be the ability to effectively sense and respond to changing requirements [50,53]. Hence, achieving agility is the basis for being able to effectively react to changing information requirements within decision processes.

Ambidexterity is the ability to combine capacities from two conflicting dimensions, and the ideal state has been characterized as a balance between the two, which requires excellence in both respects [54]. Attaining such ambidextrous excellence is challenging. This research contributes to understanding how this goal can be achieved by providing detailed insights into the tensions that arise in decision processes. Analysts need to be aware of those tensions in order to ensure effective BI&A support and utilization of their analytic advice. Since we shed light on tactics that can be applied to cope with those tensions, our results also have considerable practical relevance.

## 3. Research method

Investigation of BI&A-supported decision processes is rather complex and requires in-depth analysis of the phenomenon. We therefore decided that a multiple case study approach would be particularly suitable and applied replication logic to our study design [55,56]. Utilizing a series of cases allowed us to achieve results that are more valid and general than a single case study would have allowed [56,57]. This setup enabled us to create a strong empirical foundation, to gain a deep understanding of multiple BI&A-supported organizational decision processes, and therefore to derive more elaborated insights [56–58].

Overview of investigated cases. Table 1

<table><tr><td colspan="4">Organization characteristics</td><td colspan="4">Decision characteristics</td><td colspan="2">Interviewee characteristics</td></tr><tr><td>Case ID</td><td>Industry</td><td>Size of org.</td><td>BI&amp;A technology maturity</td><td>Decision content</td><td>Non-routineness</td><td>Decision maker level</td><td>Decision quality</td><td>Analyst role</td><td>Experience</td></tr><tr><td>1</td><td>Telecom.</td><td>Very large</td><td>Standard BI&amp;A</td><td>Reaction to new competitor</td><td>High (1.0)</td><td>Executive (C-level)</td><td>High (1.0)</td><td>BA unit leader</td><td>&gt;10 years</td></tr><tr><td>2</td><td>Media</td><td>Large</td><td>Standard BI &amp; custom BA</td><td>Product portfolio (pricing)</td><td>High (1.0)</td><td>Executive (C-level)</td><td>High (0.86)</td><td>Analyst</td><td>18 years</td></tr><tr><td>3</td><td>Finance</td><td>Very large</td><td>Standard BI&amp;A</td><td>Introduction of new risk models</td><td>High (0.71)</td><td>Executive (C-level)</td><td>High (0.86)</td><td>Analyst</td><td>&gt;10 years</td></tr><tr><td>4</td><td>Consumer</td><td>Very large</td><td>Standard BI&amp;A</td><td>Product portfolio (product mix)</td><td>High (0.71)</td><td>Executive (C-level)</td><td>High (0.95)</td><td>BA unit leader</td><td>6 years</td></tr><tr><td>5</td><td>Tourism</td><td>Very large</td><td>Standard BI &amp; custom BA</td><td>Product development</td><td>High (0.71)</td><td>Executive (C-level)</td><td>High (0.90)</td><td>BI unit leader</td><td>14 years</td></tr><tr><td>6</td><td>Finance</td><td>Large</td><td>Standard BI&amp;A</td><td>Product portfolio segmentation</td><td>High (1.0)</td><td>Executive (C-level)</td><td>High (0.86)</td><td>Analyst</td><td>&gt;15 years</td></tr><tr><td>7</td><td>Logistics</td><td>Large</td><td>Standard BI&amp;A</td><td>Fleet constitution</td><td>High (0.86)</td><td>Executive (C-level)</td><td>Medium (0.76)</td><td>Analyst</td><td>5 years</td></tr><tr><td>8</td><td>Finance</td><td>Very large</td><td>Standard BI&amp;A</td><td>Introduction of new risk models</td><td>High (0.71)</td><td>Executive (C-level)</td><td>Medium (0.67)</td><td>Analyst</td><td>&gt;10 years</td></tr><tr><td>9</td><td>Logistics</td><td>Very large</td><td>Standard BI&amp;A</td><td>Product portfolio (pricing)</td><td>High (0.86)</td><td>Executive (C-level)</td><td>Medium (0.71)</td><td>Analyst</td><td>&gt;12 years</td></tr><tr><td>10</td><td>Telecom.</td><td>Very large</td><td>Standard BI &amp; custom BA</td><td>Product portfolio (constitution)</td><td>High (0.86)</td><td>Product manager</td><td>Low (0.21)</td><td>BA unit leader</td><td>6 years</td></tr><tr><td>11</td><td>Telecom.</td><td>Very large</td><td>Standard BI &amp; custom BA</td><td>Reaction to new competitor</td><td>High (1.0)</td><td>Brand manager</td><td>Low (0.14)</td><td>Analyst</td><td>&gt;15 years</td></tr></table>

solutions partially based on custom coding, Excel, or R; orga. size: large = employees N 250/revenue N 50 m€, very large = employees N 1000/revenue N 500 m€. Notes: decision nonroutineness: 1.0 ≥ high ≥ 0.7 N medium N 0.3 ≥ low ≥ 0; decision quality: 1.0 ≥ high ≥ 0.8 N medium ≥ 0.5 N low ≥ 0; BI&A tech. maturity: standard = solutions from major BI&A vendors such as SAS, IBM, Oracle, or SAP; custom BA =

## 3.1. Research design

We used a multiple case study approach to investigate eleven BI&A supported decision processes, which we selected based on a theoretical and literal replication logic [55,56]. To achieve literal replication, we examined firms with similar organizational contexts (i.e., large firms) that have used BI&A systems in their decision processes (see Table 1). Furthermore, we investigated cases in which the decision processes had been completed prior to the study's commencement, as we were interested in gaining insights into decision process performance and the quality of the resulting decision. In order to address potential sector-specific influences, we examined firms that operate in different industry sectors (see Table 1). We primarily aimed to investigate decision processes with different levels of agility and rigor in order to achieve theoretical replication. Additionally, we distinguished between the processes based on their resulting decision quality, which allowed us to contrast the analysis results.

Investigation of BI&A-supported decision processes would have been possible from the perspective of decision makers or analysts. The advantage of the latter is that analysts have deep insights into the analytics that are used for supporting decisions and they typically have also achieved an understanding of the decision makers' requirements. Furthermore, they have insights about how their analytic solution is taken into consideration during decision making and how it contributes to the decision outcome. Therefore, in order to maximize insights into the different tasks involved in the decision processes, we based our research design on the analyst perspective.

## 3.2. Data collection

Before commencing our data collection, we drew up a case study protocol in order to assure reliability during the execution of the study. The protocol defined the objectives of our study and the data collection process. Utilizing multiple sources of evidence for data triangulation helped us enhance the validity of our findings [56]. In this regard, we conducted in-depth expert interviews, collected additional documentation where possible, and gathered complementary quantitative data using a followup survey in order to increase the reliability and validity of our findings [56,57].

We decided to use the key informant method in capturing information from the expert interviews [59]. To identify participants who could share their experiences from real decision processes, we relied on social networks for professionals and searched for senior BI&A experts (see Table 1).

For the expert interviews, we developed a semistructured interview guide (see Appendix A). We conducted two pilot interviews to refine this guide. The major part of the interview concerned a specific decision process that the interviewed analyst had supported with BI&A. In order to explore the decision processes in detail, we encouraged the experts to speak openly about everything that came to their minds [60] and, where appropriate, we used the laddering technique to pose successive questions [61]. To complement this means of data collection, we set up a structured survey (see Appendix A) to assess characteristics of the decision processes. The measurements in the survey were based on established literature in the IS and management fields and used seven-point Likert scales. Scales for measuring agility and rigor [50] were adapted to our research context. For assessing procedural rationality [9,40,42,62] and intuition [29,42] as well as decision and outcome characteristics [9,11,40,42], we relied on related management literature.

The case study interviews were conducted over a period of four months, beginning in July 2013. Most of the interviews were performed as face-to-face meetings, and the rest were conducted over the telephone. On average, each case meeting lasted two hours. In all cases, the interviews were audio recorded. Overall, this research approach yielded a rich combination of qualitative and quantitative data that provide a substantial depth and breadth for the data analysis.

## 3.3. Case overview

Table 1 presents a summary of the investigated cases, including characteristics of the decisions, the organizations, and the roles that were involved. All of the decisions we investigated were major decisions within the organizations. They all required executive-level or higher management involvement and were all rated as nonroutine. The decision problems included reacting to new competition (Cases 1 and 11), major segmentation and product portfolio decisions (Cases 2, 4, 5, 6, 9, and 10), the introduction of new risk models (Cases 3 and 8), and substantial changes to the fleet constitution (Case 7). The decisions were supported by senior BI&A experts. On average, the interviewed experts had more than ten years of BI&A-related professional experience. The technological BI&A maturity in these cases was relatively high, and most of the organizations utilized standard, stateof-the-art, BI&A solutions from one of the major vendors.

## 3.4. Data analysis

The audio files were transcribed, producing an average of nineteen pages of transcript per case. The transcriptions made up the main raw data and were used to identify specific tensions related to BI&A support and the tactics analysts used to address them. We used software for qualitative data analysis to support the coding process. We analyzed our data in four main steps, following established recommendations for qualitative data analysis [58,63], and we discussed the intermediate results obtained during the analysis in order to ensure a common understanding.

In the first step, we identified initial categories using in vivo coding to generate first-order codes [63]. More specifically, we used short conceptual descriptions of sections of the transcripts that referred to tensions occurring in the decision process or to approaches for dealing with those tensions. In the second step, we focused on conceptual links between the identified first-order codes in order to group them into adequate second-order topics. We relied on an inductive procedure that allowed concepts and relationships to emerge from the data [63]. In the third step, we used cross-case analysis techniques to conduct case comparisons [58]. We compared the cases with regard to similar concepts and relationships. We also compared interview data with data from the survey with respect to the ratings of the decision processes and their outcomes in order to corroborate the quantitative data with the qualitative descriptions. In the final step of our analysis, we aggregated the identified concepts toward a theory that is grounded in our data and empirical findings [57]. For this purpose we relied on inductive integration of the concepts resulting from the cross-case analysis [57,63,64], as well as on triangulation of perspectives [64]. This allowed us to develop a mid-range theory of ambidexterity in decision support for the purposes of explanation and prediction [64,65]. The theory is represented by means of a conceptual model that includes the identified concepts and their relationships, as well as derived propositions.

## 4. Results

The analysis of BI&A-supported decision processes across the investigated cases reveals several interesting findings. First, we provide detailed insights into the tensions that challenge effective BI&A support and that appeared to be highly robust across the cases. Analysts need to reconcile these tensions if they want to provide effective analytic support for decision makers. We shed light on the tactics they use for this purpose and how they achieve ambidexterity through these means. Next, we present an assessment of the ambidexterity that was achieved in each case, and we outline its relation to the quality of the decisions and the managerial decision making. Finally, we propose a theory of ambidexterity in decision support that integrates the presented results.

## 4.1. Tensions and tactics

Using comparative case analysis, we identified six major tensions and also discovered viable tactics for coping with those tensions. Fig. 1 provides an overview of the tensions that analysts have to address in order to provide effective BI&A support in organizational decision processes and summarizes the tactics they use for coping with those tensions. In what follows, we present these tensions and tactics in more detail. We also provide exemplary quotes that enhance the understanding of these tensions and tactics and highlight their most important aspects.

## 4.1.1. Method and domain specialization

The first general tension, which involves the specialization in analytics, is the tension between method and domain specialization. Method specialization means that the analyst has a high level of proficiency in BI&A methods and technologies. This is a prerequisite for effective decision support, and having a broad specialization in BI&A allows analysts to quickly adapt to changes in nonroutine decision contexts. The expert from Case 5 described this advantage as follows:

“Our great advantage was our extensive knowledge of the structure and content of our data. This allowed us to inform our colleagues about possibilities very early on. It allowed us to indicate which combinations were possible for drawing specific conclusions, […].” (Case 5)

In contrast, domain specialization means that analysts are focused on a problem domain, which provides them with deeper problem-specific knowledge but often restricts the scope of their BI&A proficiency. Having knowledge about the decision maker's problem domain is crucial:

“[…] the problem is that you have to be close to the business to answer dedicated questions. I don't think that a centralized unit would have been capable of developing such a model, as they wouldn't have known the details that were needed for developing it.” (Case 11)

Being capable of combining the two types of specialization has been noted as vital for effective decision support. However, combining them is considered very challenging:

“[…] the ideal for our analysts is to combine the two [capabilities] […], but that's actually barely possible.” (Case 1)

We found two main tactics that are used to manage this tension. These tactics are to compose analytic teams and to explicitly establish an analytic integrator role. Analytic teams are cross-functional and consist of analytics and domain experts who collaborate on supporting a specific decision process. The purpose of these teams is to create a working environment in which analysts and domain experts can contribute and combine their expertise, as described in the following:

“In our case, not just one analyst works on a decision process, but typically three, sometimes even more. We involve the decision makers and domain experts right from the beginning. This goes hand in hand and everybody can contribute according to their strengths.” (Case 1)

The analytic integrator role is designed to bridge the knowledge gaps between analytics experts and decision makers. Hence, the analytic integrator role differs from that of the analysts or data scientists and requires a skill set that specifically focuses on managing requirements, explaining analytic procedures and visualizations, and communicating analytic results:

“We have analysts who focus on managing requirements, on visualization, and on consulting [the decision maker] and we have analysts who focus on actually performing the analysis, utilizing our analytics tools, and experimenting with different analytical methods […].” (Case 1)

![](/api/attachments/XE9WZG28/fulltext/images/1301434d4c191a44be05ab854d472edd4ac29679310a88b8f8b7ae60eb89d2b6.jpg)  
Fig. 1. Overview of tensions and tactics.

## 4.1.2. Method flexibility and stability

The second and third tensions both stem from analysts' need to flexibly experiment with different analytic methods and data sources and to simultaneously maintain an adequate level of rigor in order to reduce information asymmetries with respect to decision makers. The second tension distinguishes between method flexibility and stability. Method flexibility is needed in nonroutine decision contexts because analysts are often unable to prescribe the best analytic procedures at the outset. Consequently, experimentation is necessary for developing a suitable approach to solving the problem. The following statement summarizes the importance of method flexibility:

“[…] we work flexibly and try out different methods, and by no means do we want to state from the start which approach is best suited for solving the problem.” (Case 11)

In contrast, a certain level of method stability is necessary throughout the decision process in order to maintain transparency and hence manage the information asymmetries that can otherwise develop between analysts and decision makers. The following quotation summarizes these needs:

“If you have an established process, a specified method, and everybody knows what you are talking about, this creates a certain degree of transparency about how results were developed […].” (Case 2)

Therefore, the simultaneous need for method flexibility and method stability creates a tension, as the following statement elaborates:

“In cases with several iterations, the decision maker cannot always conceive whether there is actually an improvement in quality […] this has to be well-defined. You typically need two or three iterations; if you need five, then the whole thing is probably poorly defined.” (Case 3)

We noticed that analysts used abstraction as a tactic to cope with this tension. Analysts try to abstract from the details of the analytic procedure while working with decision makers. This allows them to achieve a certain level of flexibility while maintaining the transparency and traceability of their procedures at a higher level of abstraction. They do this by metamodeling the decision problem at a question level that is relevant to the decision maker:

“You try to keep the core of the question similar and […] you build hierarchical models, which ensure that the highest level of questions remain similar.” (Case 2)

## 4.1.3. Data source flexibility and stability

The third tension, which concerns the data sources, is between data flexibility and data stability. Analysts have to rely on various internal and external data sources to effectively support decision processes. In nonroutine situations, there is a particularly high probability that the required data sources are not immediately available and need to be flexibly integrated into the decision process:

“[…] everything occurred quickly; there were no formalized processes. When something was missing in the warehouse, you had to get it there somehow. The integration of new sources was done in the department […] but the quality was never validated outside of it.” (Case 8)

Data source flexibility is advantageous in nonroutine decision contexts, but data source stability also has to be considered. A lack of data source stability is associated with negative consequences regarding data quality and transparency, as summarized in the following quote:

“[…] when you have to act fast […] the wrong data can easily be extracted or combined […] in cases where rapid changes have to be made, data quality is often not considered.” (Case 8)

Data source stability relates to the use of validated data sources. Relying on high quality data sources can help reduce information asymmetries and mistrust. This is especially true if these sources are regarded as reliable and their information is traceable for decision makers:

“If all stakeholders involved in the decision process have knowledge about all utilized methods and data sources […] the procedure becomes controllable at any point in time […].” (Case 2)

In summary, the conflicting demands related to data source flexibility and stability introduce a further tension. We identified two main tactics for coping with this tension. The first involves moving data quality management from the BI&A system to the (internal) source systems and thus maintaining high data quality for internal data. This improves analysts' flexibility when reacting to changing information needs in decision processes, as the following statements highlight:

“Data quality originates from where the data are created, and it is not possible to develop quality after the fact […] data quality issues need to be pushed back to the source systems […].” (Case 5)

“The more complete your warehouse infrastructure is, the more flexibility you have to react to changes in requirements. This presumes that the data quality is assured.” (Case 5)

The second tactic involves increasing the standardization of access to data sources in order to improve the quality of data access, which affects traceability and the analytics quality:

“Typically, analysts […] obtain their data by themselves. Through a little bit of standardization […] we are now able to spend 20% of our time on data collection and 80% on data analysis, and not the other way around. This has a very positive impact on analysis quality.” (Case 1)

## 4.1.4. Advanced and basic analytic elaboration

The tension related to analytics elaboration concerns a fundamental design choice that analysts have to make, namely, a choice between utilizing advanced or basic analytic approaches. This design choice relates to the analytic approaches used throughout the decision process, as well as to the mode of delivering and communicating the analytic results. Use of advanced analytics gives analysts the opportunity to potentially gain new insights or improve the validity of results; consequently, they usually try to harness the best available approaches:

“Analysts typically aim at utilizing the best available models, those with the most advantages from their point of view.” (Case 3)

Despite the benefits that can be realized through advanced analytics, this increases the information asymmetry between decision makers and analysts and therefore poses a challenge. Determining the extent of analytics elaboration should not be based only on considerations related to the analytic quality, but should also consider decision makers' comprehension:

“An important precondition for decision making or for influencing it, apart from data quality, system quality, and analytic capability, is management understanding. For me, this is the crucial dimension. […] if management does not understand it, then they won't use it.” (Case 2)

This particularly relates to the mode of delivering and communicating the final analytic results. Making use of the analytic models allows for an interactive evaluation of solution alternatives during which assumptions can be challenged and variables can be adapted. Such a procedure can be advantageous in terms of addressing the nonroutine decision context and the traceability of the recommendations obtained, but it also requires an advanced understanding of the analytics:

“If the decision maker is a specialist, the results are rather dynamic. Then we meet and together examine the effects of changing inputs and conditions. If we are mandated by management, the dynamics are typically reduced to three scenarios in total.” (Case 1)

For dealing with the tension of analytics elaboration, analysts rely on the abstraction of analytics details in combination with a means to signal quality. During collaboration in the decision process, abstraction allows analysts to maintain flexibility regarding the extent of analytics elaboration while simultaneously enhancing the understanding, as noted in the following quote:

“We provide solution proposals in the form: ‘We think that we can answer your questions in the following ways,’ but this is less oriented toward the details of the analytics in use.” (Case 1)

In their delivery of analytic results, analysts also rely on abstraction by providing analytic advice to decision makers. Such analytic advice is directed toward the goals and questions that were defined during modeling of the problem. This allows analysts to clearly communicate results:

“Using the specified decision tree, we systematically went through the different aspects, and we explained the validity of the results. […] we didn't show the complete calculations, but the figures that were presented provided enough details to assess the final result.” (Case 2)

Additionally, analysts use means for signaling quality. For analytic methods, this involves providing successful cases of application, as summarized in the following expert statement:

“I provided examples of previous applications of the analytical approaches [that is, of] how they performed, just to create a better understanding of and trust in the methods.” (Case 2)

In order to convey the trustworthiness of their analytic results, analysts also rely on signaling the quality of their analytic advice. Signaling quality includes demonstrating problem understanding and providing insights into assumptions, model validity, and data, as well as responding to decision makers' intuitions and involving domain experts in the presentation of analytic results. The following quote summarizes the main aspects of such signaling:

“Accordingly, we had to state the problem clearly once more, so as not to just present the solution, but to clearly characterize the situation, and not only to deliver the numbers, but also the views from Marketing and Sales.” (Case 4)

## 4.1.5. Broad and focused analytic scope

Analytic scope is another general design choice that analysts have to consider for each decision scenario. On the one hand, focused use of analytics allows for maintaining a very manageable analytic scope, which can help analysts cope with information asymmetries. On the other hand, while considering a broader scope might be more adequate for covering the problem space, it can lead to more complex models and induce further gaps in understanding. Moreover, it might become difficult to holistically model all relevant aspects, as the following quote emphasizes:

“I think it's very important to obtain a holistic picture and to make the decision based on all available facts. This also involves aspects that BI&A cannot cover a hundred percent.” (Case 7)

The major tactic that analysts use to address this challenge is to explicitly identify, differentiate, and model qualitative and quantitative aspects of the decision scenario. This enables them to broadly cover the problem space and to simultaneously deliver fact-based information for the most important aspects. The following statement provides an overview of this tactic:

“[…] we developed a decision tree, which required rather strategic work in order to describe all the influencing factors for the pricing decision. On the one hand, there was a quantitative part, […] but then there was also a lot of qualitative work, which was quite laborious.” (Case 2)

## 4.1.6. Open and focused problem and solution space

Support of decision processes involves validation and specification of the decision issue. Furthermore, analysts have to support exploration of alternative solutions in order to create a basis for decision making.

Both types of tasks simultaneously require focus and openness. From the analyst perspective, early and detailed specification provides the opportunity to derive clear information requirements and allows focusing the BI&A support at an early stage. Similarly, a focused solution space aims at reducing the number of alternatives early on. Clear specifications and a focused problem space enable an increase in the alignment and transparency of the analytic procedures, which, according to the following expert quotation, can be considered advantageous:

“When you are developing scenarios, they should not overlap. Instead, you try to design distinct scenarios, and it is not by chance that one designs three alternatives. Simply, left, right, and in the middle, and I think this is beneficial for decision making.” (Case 2)

In contrast, relying on emergent problem specifications and an open solution space provides flexibility for adapting to a nonroutine context. This creates opportunities to validate decision issues from different points of view and to have a more comprehensive as well as explorative search for alternative solutions, as the following expert statement suggests:

“[…] but I think it is really crucial, […] to remain open at this stage and to listen carefully to the different perspectives, to collaborate with the other units […].” (Case 4)

At the same time, this strategy increases the potential for misalignment between the analyst and the decision maker by introducing more options that have to be considered, which reduces clarity. To address this conflict, three main tactics were described. First, decision issues and information requirements are specified using semiformalized approaches, in order to define the problem at a goal-and-questions level, as stated in the following expert quotation:

“In this context, we had discussions with the decision makers regarding the goals, and they wanted to know what we could additionally draw from the data.” (Case 5)

Such an approach seems to provide enough rigor to establish the subsequent directions. Second, during the search for and development of alternatives, analysts provide explicit rationales for the inclusion or exclusion of the various alternatives, thereby restricting their number:

“[…] it was not like ‘those are the numbers and this is the alternative,’ but the numbers provided a good tendency and we then predefined two scenarios and continued working on them.” (Case 4)

Third, involving domain experts in the validation activities during the development of alternative solutions and the reduction of the number of alternatives complements the other two tactics:

“It is really important to discuss the whole thing at intermediate steps Like, ‘We have some first ideas,’ and then we discuss whether we could take any other route. […] this helps to significantly improve the quality of the decision process and, eventually, decision quality.” (Case 1)

## 4.2. Ambidexterity in BI&A-supported decision processes

The previous section introduced the tensions that analysts need to address in order to deliver effective BI&A support. It also presented the tactics that analysts use to resolve these tensions and thus to achieve ambidexterity. In what follows, we first show that ambidexterity affects decision quality. In this context, we also explore the extents of procedural rationality and intuition that characterize decision making within the investigated decision processes. Finally, we integrate our empirical findings by proposing a theory of ambidexterity in decision support.

## 4.2.1. Ambidexterity and the quality of decision process outcomes

In the context of BI&A support within the investigated cases, the conflicting task requirements revolved around needs for process rigor (i.e., traceability, structure, and stability) and agility (i.e., flexibility and adaptability). Consistent with the literature, we assess ambidexterity as a product of the ratings of rigor and agility [19,54] that were provided by the interviewees. Hence, we obtain the levels of ambidexterity that were achieved in the investigated cases (see Fig. 2). This provides initial evidence about the impact of ambidexterity on decision outcomes.

A comparison of the cases that realized high-quality decisions (Cases 1–6) with those that achieved medium- or low-quality decisions (Cases 7–11) shows that the high-quality decision cases exhibit higher ratings of ambidexterity than the less successful cases. The rating of Case 10 seems to be an exception, but the reason for this increased rating lies in the multiplication of highly unbalanced dimensions (agility N rigor), which overrates the actual ambidexterity. Thus, the main finding implies that achievement of an ambidextrous combination of rigor and agility seems to have a positive impact on the success of decision processes. This further confirms that ambidexterity should be considered as relevant and advantageous for decision support.

## 4.2.2. Procedural rationality and intuition in decision processes

Fig. 3 presents the interviewees' assessments of the magnitudes of procedural rationality and intuition that characterized the decision making within the investigated decision processes.

We find that, to a certain extent, both rationality and intuition play a role in decision making. An interesting observation arises from comparison of the cases that realized high-quality decisions (Cases 1–6) with those that achieved medium- or low-quality decisions (Cases 7–11). For the high-quality decision cases, we observe that the ratings for rationality are the same as or higher than those for intuition. In comparison, we mainly find relatively lower ratings for rationality in the less successful decision cases. Additionally, intuition seemed to play a more important role in the latter cases, and it even exceeded rationality in three cases (8, 9, and 11).

These observations imply that in nonroutine decision scenarios, the relationship or ratio between procedural rationality and intuition seems to be of relevance. Notably, rationality seems to exceed the utilization of intuition in cases that exhibit higher levels of ambidexterity, and these cases tend to result in higher quality decision outcomes. In contrast, intuition turns out to be more influential in medium- and low-quality decisions (except for Case 7), and these cases were characterized by lower levels of ambidexterity as well as lower decision quality.

![](/api/attachments/XE9WZG28/fulltext/images/63b8864f2dd22a581ccd14881434e4e52b89bbfba9db4d1c1a96f3f9df1ea80e.jpg)  
Fig. 2. Ambidexterity in cases with high (1–6) and medium/low (7–11) decision quality.

![](/api/attachments/XE9WZG28/fulltext/images/70853b22370ed5d62c78980d77764b3064c9af5e2e4c19cbadc519d0763fe2cd.jpg)  
Procedural Rationality Intuition  
Fig. 3. Procedural rationality and intuition of decision making in cases with high (1–6) and medium/low (7–11) decision quality.

## 4.2.3. A theory of ambidexterity in decision support

In order to integrate the empirical findings from this research, we propose a theory of ambidexterity in decision support, which we developed through inductive analysis of the case study data. These results and propositions are based on the replication logic of our multiple case study design. This means that the proposed model for a theory of ambidexterity in decision support (see Fig. 4) is grounded in replicated empirical findings and can thus provide an explanation of how ambidexterity can be facilitated and how it affects decision outcomes. Furthermore, we derive testable propositions for the identified concepts and their relationships.

Overall, this theory of ambidexterity in decision support suggests that improving analysts' ability to cope with the tensions in decision processes will facilitate ambidexterity, which in turn will lead to higher decision quality (see Fig. 4).

Based on the empirical results of our study, the theory differentiates between four types of tactics for coping with decision process tensions and thus achieving ambidexterity. Organizational tactics (i.e., analytic team, analytic integrator, assurance of data quality, standardization of data source access) address the setup of the working environment for BI&A support. Procedural tactics (i.e., abstraction of the analytic procedure, iterative validation) deal with the process of collaboration between analysts and decision makers. Methodological tactics (i.e., metamodeling, differentiation of qualitative and quantitative aspects, semiformal specification, reduction of alternatives) concern the practices and approaches that analysts utilize during their collaboration with decision makers. Finally, communication tactics (i.e., abstraction of analytics details, quality signaling) comprise means for shaping the direct personal interactions of analysts with decision makers.

In sum, the following proposition can be derived for achieving ambidexterity:

P1. Increasing utilization of organizational, procedural, methodological, and communication tactics will raise the level of ambidexterity in decision support and improve coping with decision process tensions.

Additionally, the proposed theory distinguishes between direct and indirect effects of ambidexterity on the quality of decision outcomes. The results from our analysis suggest that ambidexterity in the support of decision processes has a positive direct influence on decision quality.

Thus, it can be considered as basis for the development of high quality decision support.

This direct effect of ambidexterity is stated in the following proposition:

P2. Increasing the level of ambidexterity in the support of decision processes will result in better decision quality.

The proposed indirect effect of ambidexterity relates to its influence on the extents of procedural rationality and intuition utilized during decision making. The results presented in the previous section suggest that ambidexterity increases the relative extent of procedural rationality compared to intuition, which improves decision makers' utilization of analytic results during decision making. This should have a positive influence on the quality of decision outcomes.

Therefore, the indirect effect of ambidexterity is identified in two propositions:

P3. Increasing the level of ambidexterity in the support of decision processes will result in a higher ratio of procedural rationality to intuition.

P4. A higher ratio of procedural rationality to intuition will result in better decision quality.

The implications of this theory of ambidexterity may be substantial for organizations aspiring to become more analytic in their decision making, because it highlights the need for capabilities that go beyond establishing a BI&A technology in order to improve the quality of decision making.

## 5. Discussion and conclusions

This section discusses the theoretical and practical implications of the presented results, as well as their limitations. Furthermore it outlines opportunities for future research.

## 5.1. Implications for research

Utilizing the underexplored perspective of analytics experts, this research examined the conflicting demands that arise with regard to the analytic support of decision processes with BI&A. We propose ambidexterity as a theoretical lens for investigating the conflicting task requirements, and our research makes four contributions that have considerable theoretical implications for BI&A, as well as DSS and managerial decision making research.

![](/api/attachments/XE9WZG28/fulltext/images/968aacd363986eac25a3a1bd6cffd7c9f88ea0053650d1f831f249a962317cc2.jpg)  
Fig. 4. Model of the theory of ambidexterity in decision support.

First, we identify and provide in-depth insights into six tensions surrounding BI&A support that arose during the decision processes we investigated. These tensions are related to the skill specialization of analytics experts, the simultaneous need for flexibility and stability in their analytic methods and data sources, design choices regarding the elaboration and scope of the analytic approach, and the openness of the problem specification and the solution space. These tensions can impede BI&A support by threatening the effectiveness and utilization of the analytic insights that analysts supply during decision processes to raise the rationality of managerial decision making. By focusing on these challenges arising from collaboration between different specialized roles in the decision processes (i.e., analysts and decision makers), which are highly relevant in practice [12,13,22], these findings provide a much needed complementary perspective on the organizational context of decision support and decision making.

Second, in addition to characterizing the tensions that arise during the decision processes, we identify a set of tactics that analysts use to successfully manage these tensions. These tactics concern organizational, procedural, and methodological aspects of decision support, as well as communication with decision makers. Besides providing valuable insights and guidance for managing the tensions that arise in decision processes, these findings emphasize that achieving effective decision support requires more than choosing the best available technological solution. Previous research has considered it important to extend BI&A and decision support research beyond such a technological perspective in order to strengthen the relevance of our research field for managerial decision makers and analytics experts [20–22].

Third, this research not only presents the tactics that are used to achieve ambidexterity in decision processes, but also examines the relationship between ambidexterity and the quality of decision outcomes. The assessment of ambidexterity across the investigated decision processes suggests that decision processes that achieve higher levels of ambidexterity also realize higher decision quality. To the best of our knowledge, this study is the first to explicitly establish this link. In this context, we also explicitly consider the potential influence of ambidexterity on managerial decision-making behavior. We conceptualized managerial decision making in terms of the extent of the managers' reliance on intuition and on rational analysis. We found that, to a certain extent, intuition played a role in all of the investigated decision processes. This is not surprising, considering managerial research findings [26,28,30,46,47] and the nonroutine character of these decisions. The far more interesting finding concerns the ratio of procedural rationality to the use of intuition. Cases with high levels of ambidexterity exhibit high decision quality, and in these cases we found that the extent of rationality used tends to exceed that of intuition. In contrast, less successful cases with lower levels of ambidexterity mainly exhibit patterns in which reliance on intuition exceeds procedural rationality. This finding supports a notion of complementary interaction between the two dimensions [39,44,47] and thus suggests that ambidexterity could play a role in shaping the ratio between procedural rationality and intuition. In summary, these observed effects of ambidexterity underscore its relevance for decision support research and highlight the importance of understanding and effectively managing the identified tensions.

Fourth, we develop and propose a theory of ambidexterity in decision support based on the empirical findings from this research. This includes the derivation of testable propositions for the identified concepts and their relationships. The presented theoretical model allows an explanation of how ambidexterity can be achieved or improved through the utilization of different types of tactics (i.e., organizational, procedural, methodological, and communicative) that we identified in this research. Furthermore, it suggests that ambidexterity affects the quality of decision outcomes through direct and indirect effects. Ambidexterity should have a positive direct influence on decision quality by contributing to the development of BI&A decision support that effectively addresses the decision problem. Furthermore, it should have a positive indirect effect by improving decision makers' utilization of analytic results during decision making and thus raising the relative extent of procedural rationality, which contributes to improved decision quality.

## 5.2. Implications for practice

The results of this study also have considerable practical significance and make the following contributions. For analytics experts, our results not only highlight the tensions of which they need to be aware in order to deliver effective BI&A support, but also suggest tactics for coping with these tensions. By distinguishing different types of tactics (i.e., organizational, procedural, methodological, and communicative), our results provide guidance on how to systematically improve decision processes and their outcomes. Communication, methodological, and procedural tactics can be readily applied by analysts to balance taskrelated requirements of adaptability and rigor in their collaboration with decision makers. In contrast, for organizational tactics, an institutionalization of the associated practices at the organizational level would be advisable.

Turning to decision makers, the findings suggest that they need to be aware that despite the challenges that come with analytic specialization and nonroutine decisions, overdependence on intuition in decision making is risky. In contrast, the introduction of ambidextrous tactics within the organization can improve decision makers' utilization of analytic advice and thus help them scrutinize intuitive hypotheses during decision making. This will contribute to mitigating the risks of biased decision making and should therefore also raise the quality of decision making.

## 5.3. Limitations and future research directions

We have presented results from a multiple case study of BI&A support in decision processes, and we conclude by noting the following limitations as well as directions for future research.We decided to use a multiple case study approach because it enabled us to deliver more general results than would have been possible had we conducted a single case study. Nevertheless, there is still a need to further discuss and validate the research findings. One limitation of this study is that it relies on the single key informant method, for which we tried to compensate by using data triangulation. Although choosing the analyst's point of view yielded several benefits, investigating the perspectives of other stakeholders could extend this research, and it would be valuable to replicate this study from the decision maker's point of view. A larger empirical basis of BI&A-supported decision processes would also be of great value. Our current setup was too limited, in terms of the number of cases and interviews, to achieve high measurement validity and to explore cultural or domain-specific aspects. Additionally, quantitative research to test the suggested theory of ambidexterity and to address the presented propositions would be of great interest. We hope that by adding ambidexterity to the theoretical base of DSS research, we will actuate further decision-support-related research that can benefit from this perspective.

## Acknowledgments

The authors would like to thank the case study participants for their openness and the valuable time they contributed to this research. Additionally, we acknowledge the developmental review process, and we appreciate the contribution of the entire review team in helping us to improve upon the ideas presented in the paper. Finally, we would like to thank the House of IT e.V. for supporting this work with a research grant.

A<sub>pp</sub>endix A

<table><tr><td>Interview guide</td><td>Survey</td></tr><tr><td>Introduction</td><td>Decision type</td></tr><tr><td>1. Interviewee demographics</td><td>1. Overall, the discussed decision can be described as being ...</td></tr><tr><td>1.1. Background (education &amp; professional experience) and current role?</td><td>1.1. Associated with very low uncertainty (1)-associated with very high uncertainty (7)</td></tr><tr><td>Decision scenario for case study/BI&amp;A - general case information</td><td>1.2. Non-routine (1)-routine (7) (*reverse scaled)</td></tr><tr><td>Now please think of a concrete non-routine decision process that was supported by BI&amp;A:</td><td>Decision process</td></tr><tr><td>2. Decision content - What was the decision about? What was its relevance for your organization?</td><td>[Questions in this section were used for (a) identification of issue/(b) development of solution alternatives/(c) selection]</td></tr><tr><td>2.1. Organizational context of decision scenario (org-unit? when?)?</td><td>2. To which extent do you agree with the following statements concerning the procedure in [a/b/c]? (strongly disagree = 1-strongly agree = 7)</td></tr><tr><td>3. How would you describe the decision process (high level)?</td><td>2.1. Information requirements for the decision were documented in detail.</td></tr><tr><td>4. How would you characterize the decision wrt. routine and structure?</td><td>2.2. Responsibilities were clearly defined and communicated.</td></tr><tr><td>5. BI&amp;A infrastructure in case organization</td><td>2.3. The involved persons planned the procedures in detail.</td></tr><tr><td>5.1. How does BI&amp;A landscape of this organization/unit look like (high-level)?</td><td>2.4. The involved persons used a formal process.</td></tr><tr><td>5.2. What role does BI&amp;A technology play in supporting decisions in contrast to BI&amp;A experts?</td><td>2.5. Information requirements changes were sensed effectively.</td></tr><tr><td>Decision scenario for case study - specific case information</td><td>2.6. The involved persons were able to respond to information requirements changes effectively.</td></tr><tr><td>[Questions 6-9 were used to address trigger &amp; diagnosis/development of solution alternatives/selection]</td><td>2.7. The involved persons were able to make effective decisions to cope with information requirements changes.</td></tr><tr><td>6. Activities/decision process: what activities were performed?</td><td>2.8. The involved persons were able to effectively incorporate information requirements changes into the decision process.</td></tr><tr><td>6.1. What roles (DM/analysts/BI&amp;A exp.) were involved and what was their task?</td><td>3. For [a/b/c], how extensively ... (not at all extensively = 1-very extensively = 7)</td></tr><tr><td>6.2. What were inputs and outputs (results) of those activities?</td><td>3.1. ... did decision makers gather relevant information?</td></tr><tr><td>6.3. How iteratively were those activities performed?</td><td>3.2. ... did decision makers analyze relevant information?</td></tr><tr><td>7. BI → IQ: what BI&amp;A tech was used and how much did you rely on it for performing the activities?</td><td>3.3. ... did decision makers rely on quantitative analytic techniques?</td></tr><tr><td>7.1. What data (qual./quant.) was used? How was it collected?</td><td>3.4. ... was the focusing of attention of decision makers on crucial information?</td></tr><tr><td>7.2. Was there any analysis performed? What kind of?</td><td>4. Overall, from my point of view, the process for [a/b/c] can be best characterized as ...</td></tr><tr><td>7.3. How intensively was BI&amp;A-technology used?</td><td>4.1. Not at all formal (1)-very formal (7)</td></tr><tr><td>8. How would you describe the activities with respect to agility (adaptability)/rigor (formality)?</td><td>4.2. Not at all agile (1)-very agile (7)</td></tr><tr><td>8.1. How frequent were changes in requirements and how effectively were they handled?</td><td>4.3. Not at all stringent (1)-very stringent (7)</td></tr><tr><td>8.2. Is there evidence in form of task descriptions, documented results, work-products, etc.?</td><td>5. From my point of view, the procedure for [a/b/c] can be best characterized as ...</td></tr><tr><td>9. What role did rationality and political behavior play in these activities?</td><td>5.1. Not at all analytical (1)-very analytical (7)</td></tr><tr><td>Decision quality</td><td>5.2. Not at all intuitive (1)-very intuitive (7)</td></tr><tr><td>10. What dimension would you consider as relevant for characterizing the quality of this decision?</td><td>Decision quality</td></tr><tr><td>10.1. Estimated value/contribution/speed ... what else?</td><td>6. Overall, the decision that was made can be best characterized by ...</td></tr><tr><td>10.2. How would you rate the quality of this decision?</td><td>6.1. No value for the company (1)-very high value for the company (1)</td></tr><tr><td></td><td>6.2. No goal achievement for the company (1)-very high goal achievement for the company (7)</td></tr><tr><td></td><td>6.3. Very low decision quality (1)-very high decision quality (7)</td></tr></table>

## References

[1] S. Chaudhuri, U. Dayal, V. Narasayya, An overview of business intelligence technology, Commun. ACM 54 (2011) 88–98, http://dx.doi.org/10.1145/1978542.1978562.

[2] H. Chen, R. Chiang, V. Storey, Business intelligence and analytics: from big data to big impact, MIS Q. 36 (2012) 1165–1188.

[3] T.H. Davenport, J.G. Harris, Competing on Analytics: the New Science of Winning, first edition Harvard Business Review Press, Boston, Mass, 2007

[4] T.H. Davenport, D.J. Patil, Data scientist: the sexiest job of the 21st century, Harv. Bus. Rev. 90 (2012) 70–76.

[5] E. Brynjolfsson, L. Hitt, H. Kim, Strength in numbers: how does data-driven decisionmaking affect firm performance? Proc. ICIS 2011, 2011.

[6] A. McAfee, E. Brynjolfsson, Big data: the management revolution, Harv. Bus. Rev. 90 (2012) 60–66.

[7] J. Pfeffer, R.I. Sutton, Evidence-based management, Harv. Bus. Rev. 84 (2006) 62–74.

[8] K.M. Eisenhardt, M.J. Zbaracki, Strategic decision making, Strateg. Manag. J. 13 (1992) 17–37, http://dx.doi.org/10.1002/smj.4250130904.

[9] S. Elbanna, J. Child, Influences on strategic decision effectiveness: development and test of an integrative model, Strateg. Manag. J. 28 (2007) 431–453.

[10] H. Mintzberg, D. Raisinghani, A. Theoret, The structure of “unstructured” decision processes, Adm. Sci. Q. 21 (1976) 246–275, http://dx.doi.org/10.2307/2392045.

[11] P.C. Nutt, Investigating the success of decision making processes, J. Manag. Stud. 45 (2008) 425–455, http://dx.doi.org/10.1111/j.1467-6486.2007.00756.x

[12] S. Viaene, A. Van den Bunder, The secrets to managing business analytics projects, MIT Sloan Manag. Rev. 65–69 (2011).

[13] S. Viaene, Data scientists aren't domain experts, IT Prof. 15 (2013) 12–17.

[14] S. Bonaccio, R.S. Dalal, Advice taking and decision-making: an integrative literature review, and implications for the organizational sciences, Organ. Behav. Hum. Decis. Process. 101 (2006) 127–151, http://dx.doi.org/10.1016/j.obhdp.2006.07.001.

[15] I. Yaniv, E. Kleinberger, Advice taking in decision making: egocentric discounting and reputation formation, Organ. Behav. Hum. Decis. Process. 83 (2000) 260–281.

[16] J.A. Sniezek, L.M. Van Swol, Trust, confidence, and expertise in a judge–advisor system, Organ. Behav. Hum. Decis. Process. 84 (2001) 288–307, http://dx.doi.org/10. 1006/obhd.2000.2926

[17] L.M. van Swol, J.A. Sniezek, Factors affecting the acceptance of expert advice, Br. J. Soc. Psychol. 44 (2005) 443–461, http://dx.doi.org/10.1348/014466604X17092.

[18] S. Raisch, J. Birkinshaw, Organizational ambidexterity: antecedents, outcomes, and moderators, J. Manag. 34 (2008) 375–409, http://dx.doi.org/10.1177/0149206308316058.

[19] C.B. Gibson, J. Birkinshaw, The antecedents, consequences, and mediating role of organizational ambidexterity, Acad. Manag. J. 47 (2004) 209–226, http://dx.doi.org/ 10.2307/20159573.

[20] D. Arnott, G. Pervan, A critical analysis of decision support systems research revisited: the rise of design science, I. Inf, Technol. 29 (2014) 269–293, http://dx. doi.org/10.1057/jit.2014.16.

[21] D. Arnott, G. Pervan, Eight key issues for the decision support systems discipline, Decis. Support. Syst. 44 (2008) 657–672, http://dx.doi.org/10.1016/j.dss.2007.09.003.

[22] R. Sharma, S. Mithas, A. Kankanhalli, Transforming decision-making processes: a research agenda for understanding the impact of business analytics on organisations, Eur. J. Inf. Syst. 23 (2014) 433–441, http://dx.doi.org/10.1057/ejis.2014.17.

[23] H.J. Watson, Business analytics insight: hype or here to stay? Bus. Intell. J. 16 (2010) 4–8.

[24] A. Popovič, R. Hackney, P.S. Coelho, J. Jaklič, Towards business intelligence systems success: effects of maturity and culture on analytical decision making, Decis. Support. Syst. 54 (2012) 729–739, http://dx.doi.org/10.1016/j.dss.2012.08.017.

[25] D. Arnott, Senior executive information behaviors and decision support, J. Decis. Syst. 19 (2010) 465–480, http://dx.doi.org/10.3166/jds.19.165-480.

[26] C. Akinci, E. Sadler-Smith, Intuition in management research: a historical review, Int. J. Manag. Rev. 14 (2012) 104–122, http://dx.doi.org/10.1111/j.1468-2370.2011.00313.x.

[27] E. Dane, M.G. Pratt, Exploring intuition and its role in managerial decision making, Acad Manag, Rev, 32 (2007) 33–54 http://dx.doiorg/10.5465/AMR.2007.23463682

[28] G.P. Hodgkinson, E. Sadler-Smith, L.A. Burke, G. Claxton, P.R. Sparrow, Intuition in organizations: implications for strategic management, Long Range Plan. 42 (2009) 277–297, http://dx.doi.org/10.1016/j.lrp.2009.05.003.

[29] S. Elbanna, Strategic decision-making: process perspectives, Int. J. Manag. Rev. 8 (2006) 1–20, http://dx.doi.org/10.1111/j.1468-2370.2006.00118.x.

[30] N. Khatri, H.A. Ng, The role of intuition in strategic decision making, Hum. Relat. 53 (2000) 57–86, http://dx.doi.org/10.1177/0018726700531004.

[311 H. Mintzberg, The fall and rise of strategic planning, Hary, Bus, Rey. (1994) 107–114

[32] S. Shapiro, M.T. Spence, Managerial intuition: a conceptual and operational framework, Bus, Horiz, 40 (1997) 63–68 http://dx.doiorg/10.1016/S0007-6813(97)90027-6

[33] S. Chaiken, A. Liberman, A.H. Eagly, Heuristic and systematic information processing within and beyond the persuasion context, in: J.S. Uleman, J.A. Bargh (Eds.), Unintended Thought, Guilford Press, New York 1989, pp. 212 252.

[34] J.S.B.T. Evans, Dual-processing accounts of reasoning, judgment, and social cognition, Annu. Rev. Psychol. 59 (2008) 255–278, http://dx.doi.org/10.1146/annurev. psych.59.103006.093629.

[35] D. Kahneman, S. Frederick, Representativeness revisited: attribute substitution in intuitive judgment, in: T. Gilovich, D. Griffin, D. Kahneman (Eds.), Heuristics Biases Psychol, Cambridge University Press, New York, Intuitive Judgm. 2002, pp. 49–81.

[36] K.E. Stanovich, R.F. West. Advancing the rationality debate, Behay, Brain Sci. 23 (2000) 701–717.

[37] A. Tversky, D. Kahneman, Judgment under uncertainty: heuristics and biases, Science 185 (1974) 1124–1131, http://dx.doi.org/10.1126/science.185.4157.1124

[38] D. Kahneman, A. Tversky, On the study of statistical intuitions, Cognition 11 (1982) 123–141, http://dx.doi.org/10.1016/0010-0277(82)90022-1.

[39] E. Sadler-Smith, E. Shefy, The intuitive executive: understanding and applying “gut feel” in decision-making, Acad. Manag. Exec. 18 (2004) 76–91.

[40] J.W. Dean, M.P. Sharfman, Procedural rationality in the strategic decision-making process, J. Manag. Stud. 30 (1993) 587–610, http://dx.doi.org/10.1111/j.1467- 6486.1993.tb00317.x

[41] T. Hutzschenreuter, I. Kleindienst, Strategy-process research: what have we learned and what is still to be explored, J. Manag. 32 (2006) 673–720, http://dx.doi.org/10. 1177/0149206306291485

[42] J.W. Dean, M.P. Sharfman, Does decision process matter? A study of strategic decision-making effectiveness, Acad. Manag. J. 39 (1996) 368–392, http://dx.doi. org/10.2307/256784.

[43] V.M. Papadakis, S. Lioukas, D. Chambers, Strategic decision-making processes: the role of management and context, Strateg. Manag. J. 19 (1998) 115 147

[44] C.C. Miller, R.D. Ireland, Intuition in strategic decision making: friend or foe in the fast-paced 21st century? Acad. Manag. Exec. 19 (2005) 19–30.

[45] S. Elbanna, J. Child, M. Dayan, A model of antecedents and consequences of intuition in strategic decision-making: evidence from Egypt, Long Range Plan. 46 (2013) 149–176.

[46] M. Sinclair, N.M. Ashkanasy, Intuition myth or a decision-making tool? Manag. Learn. 36 (2005) 353–370, http://dx.doi.org/10.1177/1350507605055351.

[47] J. Woiceshyn, Lessons from “good minds”: how CEOs use intuition, analysis and guiding principles to make strategic decisions, Long Range Plan. 42 (2009) 298–319.

[48] G.P. Huber, A theory of the effects of advanced information technologies on organizational design, intelligence, and decision making, Acad. Manag. Rev. 15 (1990) 47–71.

[49] J.A. Sniezek, T. Buckley, Cueing and cognitive conflict in judge–advisor decision making, Organ. Behav. Hum. Decis. Process. 62 (1995) 159–174, http://dx.doi.org/10. 1006/obhd.1995.1040

[50] G. Lee, W. DeLone, J. Espinosa, The main and interaction effects of process rigor, process standardization, and process agility on system performance in distributed IS development: an ambidexterity perspective, Proc. ICIS 2010, 2010.

[51] P.S. Adler, B. Goldoftas, D.I. Levine, Flexibility versus efficiency? A case study of model changeovers in the Toyota production system, Organ. Sci. 10 (1999) 43–68.

[52] C. Andriopoulos, M.W. Lewis, Exploitation–exploration tensions and organizational ambidexterity: managing paradoxes of innovation, Organ. Sci. 20 (2009) 696–717.

[53] G. Lee, W. Xia, Toward agile: an integrated analysis of quantitative and qualitative field data MIS 0. 34 (2010) 87-114

[54] Q. Cao, E. Gedajlovic, H. Zhang, Unpacking organizational ambidexterity: dimensions, contingencies, and synergistic effects, Organ. Sci. 20 (2009) 781–796.

[55] L. Dubé, G. Paré, Rigor in information systems positivist case research: current practices trends and recommendations MIS 0. 27 (2003) 597–636

[56] R.K. Yin, Case Study Research: Design and Methods, Sage Publications, Thousand Oaks, CA, 2003.

[57] K.M. Eisenhardt, Building theories from case study research, Acad. Manag. Rev. 14 (1989) 532–550, http://dx.doi.org/10.5465/AMR.1989.4308385.

[58] M.B. Miles, A.M. Huberman, Qualitative Data Analysis: An Expanded Sourcebook, second edition Sage Publications, Thousand Oaks, CA, 1994

[59] R.P. Bagozzi, Y. Yi, L.W. Phillips, Assessing construct validity in organizational research Adm, Sci, 0. 36 (1991) 421–458 http://dx.doi.org/10.2307/2393203

[60] K.A. Ericsson, H.A. Simon, Protocol Analysis: Verbal Reports as Data, The MIT Press, Cambridge, MA. 1993.

[61] T.J. Reynolds, J.C. Olson, Understanding Consumer Decision Making: The Means–End Approach to Marketing and Advertising Strategy, Psychology Press, Mahwah, NJ, 2001.

[62] S. Elbanna, H. Younies, The relationships between the characteristics of the strategy process: evidence from Egypt, Manag. Decis. 46 (2008) 626–639.

[63] J. Corbin, A. Strauss, Basics of Qualitative Research: Techniques and Procedures for Developing Grounded Theory, third edition Sage Publications, Los Angeles, CA, 2008.

[64] W. Kuechler, V. Vaishnavi, A framework for theory development in design science research: multiple perspectives, J. Assoc. Inf. Syst. 13 (2012) 395–423.

[65] S. Gregor, The nature of theory in information systems, MIS Q. 30 (2006) 611–642.

![](/api/attachments/XE9WZG28/fulltext/images/839000ca1ba851f71e2022ccd524edc58a6acf7fd3172361bec0da59ada8f4a8.jpg)

Martin Kowalczyk is a researcher at the Technische Universität Darmstadt (TU Darmstadt) at the Chair of Infor: mation Systems. His current research interests focus on the effective utilization of business intelligence and analytics in the context of organizational decision processes. Prior to his current position, Martin was a researcher and consultant at the Fraunhofer Institute for Experimental Software Engineering (IESE). His research activities included subjects concerning software development processes and goaloriented measurement approaches. In this context. he consulted several international organizations from the aerospace, finance, and services domains on topics from the area of software process improvement, analytics and fact-based decision making. He has led process improvement initiatives and has established analytic practices for his customers, Martin has authored and coauthored peer-reviewed publications on software process management, organizational decision processes, as well as business intelligence and analytics

![](/api/attachments/XE9WZG28/fulltext/images/edb3b074141abc82c714bd7520404c975be1bbdc247c02576d03435f2da7af38.jpg)

Peter Buxmann is professor at the Technische Universität Darmstadt (TU Darmstadt). He supervised numerous scientific as well as industry-related research projects and is head of HIGHEST, the start-up incubator of TU Darmstadt and boardmember of the House of IT, where he is responsible for interdisciplinary research and networking between industry and science. His research interests are the economic principles of the Software- and Social Media Industry as well as Information Management and the Future Internet Economy. Peter is author and coauthor of more than 200 publications in international journals, like Information Systems Research (ISR), Information Systems Journal (ISJ), European Journal on Information Systems (EJIS), Journal of Information Technology (JIT) and in proceedings of international conferences (e.g. ICIS, ECIS). Peter

studied Management with focus on Information Management at Frankfurt University, where he also received his Ph.D. After being visiting scholar at the Haas School of Business at the University of California in Berkeley, he qualified as a professor. In 2000 he was appointed Pro fessor for Information Management at TU Freiberg until he received a call to TU Darmstadt, where he now holds the chair of Software Business & Information Management.
