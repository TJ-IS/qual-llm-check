---
otero_id: 20815
otero_key: "QJHB7KH3"
title: "Creating business value with process mining"
authors: "Peyman Badakhshan; Bastian Wurm; Thomas Grisold; Jerome Geyer-Klingeberg; Jan Mendling; Jan vom Brocke"
year: "2022"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/j.jsis.2022.101745"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Creating business value with process mining

![](/api/attachments/QJHB7KH3/fulltext/images/524ebece6a8bbe94517f6e62a3dabf40f6ac6f91a8e4045cb6968707de2b0c2d.jpg)

Peyman Badakhshan <sup>a</sup>, Bastian Wurm <sup>c</sup>, Thomas Grisold <sup>b</sup>, Jerome Geyer-Klingeberg <sup>d,f</sup>, Jan Mendling <sup>e</sup>, Jan vom Brocke b,

<sup>a</sup> SAP, Munich, Germany

<sup>b</sup> Institute of Information Systems, University of Liechtenstein, Liechtenstein

<sup>c</sup> LMU Munich School of Management, LMU Munich, Munich, Germany

<sup>d</sup> Institute of Materials Resource Management, University of Augsburg, Augsburg, Germany

<sup>e</sup> Department of Computer Science, Humboldt-Universitat ¨ zu Berlin, Berlin, Germany

<sup>f</sup> Celonis SE, Munich, Germany

## A RTICLE IN FO

Keywords: Process Mining Big Data Analytic Business Intelligence Business Value Multiple Case Study

## A B S T R A C T

Information systems research has a long-standing interest in how organizations gain value through information technology. In this article, we investigate a business process intelligence (BPI) technology that is receiving increasing interest in research and practice: process mining. Process mining uses digital trace data to visualize and measure the performance of business processes in order to inform managerial actions. While process mining has received tremendous uptake in practice, it is unknown how organizations use it to generate business value. We present the results of a multiple case study with key stakeholders from eight internationally operating companies. We identify key features of process mining – data & connectivity, process visualiza tion, and process analytics – and show how they translate into a set of affordances that enable value creation. Specifically, process mining affords (1) perceiving end-to-end process visualiza tions and performance indicators, (2) sense-making of process-related information, (3) datadriven decision making, and (4) implementing interventions. Value is realized, in turn, in the form of process efficiency, monetary gains, and non-monetary gains, such as customer satisfac tion. Our findings have implications for the discourse on IT value creation as we show how process mining constitutes a new class of business intelligence & analytics (BI&A) technology, that enables behavioral visibility and allows organizations to make evidence-based decisions about their business processes.

## Introduction

Recent vears have seen an increasing uptake of process mining in industry (Reinkemever, 2020). Process mining is a business intelligence and analytics (BI&A) technology (Chen, Chiang and Storey, 2012) that is concerned with the real-time analysis and visual ization of end-to-end business processes based on event log data (van der Aalst, 2016; Augusto et al., 2019; vom Brocke, Jans, Mendling and Reijers, 2021). Business processes are key to accomplishing work in organizations (Nelson and Winter, 1982; Dumas, La Rosa, Mendling and Reijers, 2018), and process mining provides an evidence-based means to observe, adjust, and communicate about process work on a continuous basis (Eggers. Hein. Böhm and Krcmar. 2021: Martin et al., 2021)

Process mining vendors, such as the German company Celonis, report growth rates of 100 % and more in recent years, and analysts expect the market for process mining to grow tenfold over the coming years (Kerremans, 2019; Everest Group, 2020; Kerremans, Samantha, Tushar and Kimihiko, 2020). Organizations expect further value realization from process mining as research and practice continuously develop more sophisticated algorithms and analysis techniques, which perform, for example, predictions about future process behavior (Polato, Sperduti, Burattin and de Leoni, 2016; Mehdiyev, Evermann and Fettke, 2020). Despite its wide and rapid uptake in practice, however, research has insufficiently understood how organizations realize value through process mining. The few reports about process mining value are essentially sourced from process mining vendors (Grisold. Mendling. Otto and vom Brocke 2020) or based on anecdotal evidence (Reinkemeyer, 2020). Understanding how process mining creates business value is important as respective insights can guide organizations in their decision to adopt and how to make the best use of this novel technology.

Research on BI&A has described a broad range of technologies that are used in various organizational contexts and for different purposes (Chen et al., 2012). In particular, several studies have focused specifically on mechanisms of value creation through BI&A (e. g. Lehrer et al., 2018; Müller, Fay and vom Brocke, 2018; Bordeleau, Mosconi and de Santa-Eulalia, 2020). However, previous research on value creation of BI&A technology is not well suited to explain the value generation mechanisms of process mining. This is because the established body of knowledge focuses on BI&A applications that are used for strategic and one-time decision making processes (Shollo and Galliers, 2016; Seddon, Constantinidis, Tamm and Dod, 2017), such as service innovation (Lehrer et al., 2018). To stress its distinctiveness in comparison to other BI&A technologies, and to emphasize its focus on the analysis of end-to-end business processes. process mining has been referred to as a business process intelligence technology (BPI) (Grigori et al., 2004; Castellanos et al., 2009; van der Aalst, Zhao and Wang, 2015). Key to this shift in terminology is to highlight that process mining enables the continuous analysis of business processes (Grisold, Mendling, et al., 2020; Eggers et al., 2021; vom Brocke et al., 2021), and thus enables different action possibilities for organizations, which may come with different value creation opportunities.

This study is the first to empirically investigate the research question: How do organizations use process mining to create business value? To this end, we employed a qualitative inductive study design (e.g., Sahay and Ranjan, 2008; Seddon et al., 2017; Grover, Chiang, Liang and Zhang, 2018). Specifically, we conducted a multiple case study with eight companies from different industries that have used process mining over an extended period and consider it an important technology for improving organizational work. We interviewed process mining stakeholders to explore why they use process mining in their organizations and how its usage has led to business value. To analyze our data, we drew on the affordance perspective (Seidel. Recker and vom Brocke. 2013: Strong. Volkoff. Johnson and Pelletier, 2014; Leidner, Gonzalez and Koch, 2018; Markus and Rowe, 2018). Affordance theory is particularly useful as it allows us to distinguish between features of process mining and the action potentials (i.e., affordances) that key stakeholders, such as process analysts and process managers, enact in order to achieve certain goals. Prior studies have used an affordance perspective to understand, for instance, how features of information systems create affordances that can be used for green transformations (Seide et al., 2013) or how BI&A can be employed for service innovation (Lehrer et al., 2018). We use affordance theory to examine value realization with process mining technology.

Grounded in our data, we identify-four process mining affordances: (1) perceiving end-to-end process visualizations and perfor mance indicators; (2) sense-making of process-related information; (3) data-driven decision making; and (4) implementing in terventions based on the obtained insights. These affordances are interrelated and have a cyclical relationship: after implementing interventions, organizations engage in another round of sense-making and decision-making to understand and decide whether further changes to the process are necessary. In doing so, companies are able to realize process efficiency, monetary values, and non-monetary values.

We continue as follows. First, we present the theoretical background of our work. We then introduce the research design of our study, followed by the presentation of our findings. Finally, we discuss the implications and limitations of our work and provide a brief conclusion.

## Theoretical background

In this section, we outline the theoretical background of our work. First, we introduce process mining and discuss its key features. We then contrast process mining with the literature on BI&A and argue that further research is required to understand how organi zations use the unique features of process mining to generate business value. Last, we introduce affordance theory as our theoretica lens and explain how it allows us to untangle features, affordances, and business values of process mining technology.

## Process mining

Process mining encompasses a family of techniques for extracting, visualizing, and analyzing processual information from event data, stored in so-called event logs¹ (van der Aalst. 2011). The central focus of process mining lies on the analysis of end-to-end business processes (van der Aalst, 2016). Based on data collected during the performance of business processes, process mining generates models that show how processes are carried out and monitors their on-going performance (van der Aalst, 2016). Process mining provides organizations with what has recently been called ‘behavioral visibility' (Leonardi and Treem. 2020: vom Brocke et al.

2021). It draws on the increasing datafication of work places and enables analysts to pinpoint specific actions and actors that appear interesting for further investigation (e.g., when a process does not run as expected, it is possible to see who is or was involved).

Research on process mining is devoted to the development of three broad classes of features: features to connect with data sources, features to visualize process behavior, and features to obtain analytical insights into process behavior (van der Aalst, 2016). The development of features to connect with data sources comprises, for instance, techniques for the creation of event logs from relationa databases (Jans and Soffer, 2017), and various aspects of data quality (Suriadi, Andrews, ter Hofstede and Wynn, 2017). The development of features to visualize processes, also referred to as process discovery algorithms, aims to derive a process model that represents the process execution based on data stored in an event log (Augusto et al., 2019). Finally, the development of features to obtain analytical insights into process behavior encompasses conformance checking algorithms that compare an ‘as is’ process mode derived through process discovery against a ‘to be’ process model (Carmona, van Dongen, Solti and Weidlich, 2018). This class of features also includes techniques and measures to monitor changes to (Yeshchenko, Ciccio, Mendling and Polyvyanyy, 2021) and the complexity of business processes (Augusto, Mendling, Vidgof and Wurm, 2022). Process mining can be combined with a wide range of methods and technologies from other disciplines. For example, process mining can discover manually performed activities and robotic process automation can replace those manual process steps through machine-driven activities (van der Aalst, Bichler and Heinzl, 2018; Hofmann, Samp and Urbach, 2020); machine learning can be used to predict process behavior and outcomes (van der Aalst, Scho nenberg and Song, 2011; Veit et al., 2017), and other AI-driven methods can help to produce machine-generated recommendations for process improvement by learning from historical process data (Okove et al., 2018: Terragni and Hassani, 2018).

Anecdotal evidence suggests that organizations can realize significant business value through the use of process mining (Rein kemeyer, 2020). Globally operating companies (such as BMW and Siemens, among many others) use process mining to monitor their daily operations (Reinkemeyer, 2020) to continuously find opportunities for improvement, for example, by lowering costs or customer waiting times (Grisold, Mendling, et al., 2020). The growing market capitalization of process mining companies reflects the increasing interest from practice. Celonis, a major process mining provider, has reached a market valuation of \$11 billion and SAP only recently acquired Signavio for \$2 billion to strengthen its “capacity to help companies quickly understand, improve, transform and manage their business processes at scale” (SAP, 2021).

From a research perspective, first studies on the use of process mining in organizations give a hint of how organizations produce value through process mining features (Grisold, Mendling, et al., 2020; Eggers et al., 2021). These studies suggest that process mining fundamentally changes how organizations manage business processes. They indicate, for example, that process mining affords evidence-based means to analyze operations (Chen et al., 2012), and take evidence-based decisions (Eggers et al., 2021; Grisold, Mendling, et al., 2020). Whereas organizations have traditionally managed business processes with an eye on ‘to be’ processes, i.e., how they should be performed, process mining allows them to visualize, manage, and optimize ‘as is’ business processes, i.e., how processes are actually performed (Davenport and Spanyi, 2019). However, to this date, how organizations use features of process mining for value creation is unknown.

In summary, process mining enables organizations to gain detailed insights into their organizational processes, based on features to (1) connect with data sources, (2) visualize process behavior, and (3) obtain analytical insights into process execution (van der Aalst, 2016). Organizations have started to report on significant benefits gained through process mining technology (Grisold, Mendling, et al., 2020; Reinkemeyer, 2020). Understanding how process mining enables value creation for organizations is important for at least two reasons. First, it can guide organizations in their decision to adapt process mining and how to capitalize on its features. Second, insights on process mining usage in organizations can spark further technical innovations and the development of algorithmic advancements.

## Process mining as business process intelligence: a new form of business intelligence and analytics

Business intelligence and analytics (BI&A) technologies leverage various kinds of big data to provide insights on business and market activities and enable effective decision making (Chen et al., 2012; Galetsi, Katsaliaki and Kumar, 2020). A plethora of research has studied how organizations use such technologies to realize value (Seddon, Constantinidis and Dod, 2012; Sharma, Mithas and Kankanhalli, 2014; Grover et al., 2018). To this end, BI&A typically includes technologies, such as (1) big data analytics, (2) text analytics, (3) web analytics, (4) network analytics, and (5) mobile analytics (Chen et al., 2012). Process mining was initially considered to fall into the broad category BI& A technologies, primarily because of its capacity to turn big data into relevant business insights (Chen et al., 2012). However, it is important to stress that it considerably differs from established BI&A technologies because it enables behavioral visibility (Leonardi and Treem, 2020) and creates on-going transparency around everyday activities in organizational work on a continuous basis (Grisold, Mendling, et al., 2020; Reinkemeyer, 2020; Eggers et al., 2021; vom Brocke et al., 2021).

Recognizing the distinct quality of process mining, research in the areas of business process management (BPM) and computer science has referred to this class of BI&A technologies as business process intelligence (BPI) (Grigori et al., 2004; Tan et al., 2008; Castellanos et al., 2009: van der Aalst et al., 2015). The key to BPI technologies is that they enable decision-making in relation to single process steps and on the basis of real-time information. BPI informs managers, for example, about the performance of business pro cesses as they unfold at a given point in time. This stands in stark contrast to the majority of studies on BI&A technologies, which are typically concerned with specific strategic decisions, which can include increasing customer satisfaction (Trieu, 2017), reacting to actions taken by competitors (Eric Zheng, Fader and Padmanabhan, 2012), and sensing innovation potentials based on user behavior (Lehrer et al., 2018; Lozada, Arias-P´erez and Perdomo-Charry, 2019), among others. Hence, these studies provide limited insights on how value is created through day-by-day managerial decision-making on a business process level, as it is enabled by BPI technologies. Examining the use of process mining helps us develop a more nuanced understanding about BPI as an emerging class of BI&A

technologies.

## Affordances for value creation

In order to get at the value creation mechanisms underlying process mining, we draw from the affordance concept. Broadly speaking, affordances are action potentials that users of technology perceive when they pursue a certain goal (e.g., Leonardi, 2013; Strong et al., 2014). Rooted in Gibson’s ecological psychology (e.g., Gibson, 1977, 1986), affordances reconcile perspectives of technological determinism and social constructivism; users make their own interpretations when they interact with a technology. Yet what they can do is constrained by the features, i.e., the material properties, of the respective technology (Leonardi and Barley, 2008). Thereby, features are those functional properties of information technology that “have some stability across contexts and time” (Lehrer et al., 2018, p. 429). Leidner et al. (2018) remind us that it is crucial to differentiate between feature use and affordances. While feature use pertains to what users can do with a technology (e.g. merge data), affordances only emerge as action possibilities as a consequence of this use (e.g., developing a shared understanding of data).

The affordance concept has proven particularly useful to understand why users enact emerging technologies (Zammuto et al., 2007). Typically grounded in qualitative-inductive research designs (e.g. Seidel et al., 2013), an affordance view helps us understand the expectations that users associate with a given technology along with the actions through which users interact with the technology (Yoo, Boland, Lyytinen and Majchrzak, 2012). To this end, affordances have been used to study all kinds of digital technologies, such as social media (Leonardi and Vaast, 2017), enterprise social media (Leidner et al., 2018), blockchain (Du, Pan, Leidner and Ying, 2019), and various other digital technologies that are used in organizations and beyond (Goh, Gao and Agarwal, 2011; Seidel et al., 2013; Nan and Lu, 2014; Ess´en and Varlander, ¨ 2019). Big data analytics technologies, for example, offer different features, such as data storage visualization, and prediction. These features translate into different affordances, depending on what users seek to do. For instance, when users pursue the development of individualized customer service, features such as data storage, visualization, and pattern recognition, afford users to proactively approach and interact with customers (Lehrer et al., 2018).

Users tend to experiment with new technologies and explore different action opportunities (Du et al., 2019; Keller et al., 2019), but over time, they establish relations with technologies that are stable across time and space (Karahanna, Xu, Xu and Zhang, 2018; Ess´en and Varlander, ¨ 2019). In other words, when users recognize that they can reliably achieve a certain goal by using a digital technology in a given way, they will rigidify these affordances (Faraj and Azad, 2012; Ess´en and Varlander, ¨ 2019). In such cases, users have learnt that they can pursue a certain goal by taking certain actions (Volkoff and Strong, 2013; Leonardi, Bailey and Pierce, 2019). Prior studies have used an affordance perspective to understand, for instance, how information systems enable green transformations (Seide et al., 2013) or how BI&A affords service innovation (Lehrer et al., 2018).

Following our interest to study how process mining leads to value creation in organizations, we deem affordance theory particular useful as it allows us to distinguish between features of process mining, the action potentials (i.e., affordances) that arise for key stakeholders, such as process analysts and process managers, and the goals that they pursue as they enact affordances. Organizations adopt process mining because they aim to improve process efficiency (Grisold, Mendling, et al., 2020; Reinkemeyer, 2020). Hence, there is a clear expectation on the side of organizations that they can improve their operations. This expectation, in turn, translates into specific goals (Grisold, Mendling, et al., 2020; vom Brocke et al., 2021). Hence, by understanding what users aim to achieve (i.e., their goals) when using process mining (i.e., its features), and how it enables them to take corresponding actions (i.e., affordances), we can better understand how and why it enables value creation in organizations.

## Summary

Process mining offers unique features that allow organizations to monitor and improve business process on a day-to-day basis. This has two crucial implications. First, process mining represents a new class of BI&A technologies that has been labelled as business process intelligence (BPI). Second, insights about value creation in traditional BI&A tools tell us little about how organizations use process mining and how this creates value. Given that one of the key goals of IS research is to recognize and study the impact of emerging technologies on organizations and economies (Sarker, Chatterjee, Xiao and Elbanna, 2019), and in light of the practica relevance of process mining, we suggest directing our attention to the mechanisms of value creation underlying process mining technology. To do so, we employ an affordance lens (e.g. Strong et al., 2014; Markus and Rowe, 2018) that enables us to untangle features, affordances, and associated business values of process mining technology.

## Research method

To study how organizations use process mining to create business value, we adopt a qualitative inductive research design. This decision aligns well with recent claims in the literature to identify mechanisms and evolving practices associated with big data use as well as affordance enactment from a qualitative-inductive perspective (e.g., Sahay and Ranjan, 2008; Seddon et al., 2017; Grover, Chiang, Liang and Zhang, 2018). For example, Trieu (2017) stresses that grounded theory-based study designs enable unpacking the conversion process from BI&A use to value, Similarly. Seddon et al. (2017) stress that inductive process-models – compared to deductive variance models – are useful to understand the steps involved in value creation

Specifically, we adopted a multiple case study design following the principles of Grounded Theory (Strauss and Corbin, 1998). Our research process comprised four steps as outlined in Fig. 1. First, we selected suitable case companies, For a purposeful selection ot cases, we followed the recommendations of Eisenhardt, (1989), Par´e (2004), and Eisenhardt and Graebner (2007). In line with Par´e (2004), we ensured that cases are diverse regarding their industry, size, location, and the objective for using process mining. Overall, we selected eight organizations for our study.

All of the selected organizations have been using process mining for more than one and a half years and consider it an important technology for the creation of business value. All organizations have various initiatives in place to leverage insights from process mining to support, for example, continuous process improvement, process automation, process compliance, and audit, among others. We selected 17 respondents that are considered process mining experts in their respective organization. Table 1 presents an overview of the interview participants. We provide further details on the eight case companies in Appendix A.

Second, we conducted seventeen semi-structured in-depth interviews with our selected key informants. We used a semi-structured interview guideline with open-ended questions in order to guide the interviews but not restrict interviewees’ answers (Par´e, 2004). The complete interview guideline is available in Appendix B. We allowed for follow-up questions to account for and clarify individua responses, and gain a more comprehensive understanding about the specific use context of a respective organization. Each interview lasted between 60 and 90 minutes. All interviews were held in English using a virtual video conferencing tool. All interviews were recorded, transcribed, and subsequently coded. In order to answer our research question “How do organizations use process mining to create business value?”, we developed a set of questions, which can be arranged along five broad thematic areas. These areas covered: (1) the reasoning behind the adoption of process mining; (2) how its implementation was facilitated; (3) challenges that were faced; (4) governance and organizational setup for handling the tool; and (5) perceived business values of process mining.

Third, we analyzed our interview data following the general principles of Grounded Theory (Strauss and Corbin, 1998, Charmaz and Belgrave 2012). Together with data collection. this step took place iteratively until we reached theoretical saturation. To get an impression about the data at hand, we started with open coding and writing memos about each interview. Since our aim was to develop novel explanations about how process mining is used in organizations to create business value, we approached the data openly and without any specific theoretical concepts. To establish coding reliability (Lavrakas, 2008), the first three authors individually coded the first set of interviews resulting in approximately 100 open codes. They then discussed their findings in order to derive a first rough coding scheme. The discussions helped to establish a common understanding of the data and pointed to several high-level and lowlevel codes that were identified as relevant with respect to the research question. The discussion among the authors and constant comparison of codes also led to the reduction of codes, leading to approximately 50 relevant codes. Afterwards, we coded each interview in detail while allowing for the emergence of additional codes and the adjustment of existing ones. We then compared the derived patterns of each within-case analysis and checked if they were applicable across all cases (Eisenhardt, 1989; Par´e, 2004; Eisenhardt and Graebner, 2007). After the eighth interview, we realized that only a few new codes emerged, i.e. we noticed the start of theoretical saturation. We continued with the collection and coding of further interview data, since we wanted to examine whether our findings were holding across our cases and their diverse backgrounds. Overall, we created around 150 open codes. For the coding of the interviews, we used the ATLAS.ti software. Table 2 presents an exemplary selection of open codes along with illustrative interview data.

We then continued with the axial coding of our data, i.e., we coded around what emerged to be important code categories in light of our research question. We found that three categories were particularly relevant: 1) features of process mining technology; 2) actions that organizations took drawing on process mining: and 3) the specific goals that organizations pursued with these actions to realize business value. Table 3 gives an overview of the axial codes and selected sub-categories.

During the selective coding stage, we integrated the axial codes into a coherent theoretical model that describes how organizations use process mining to create business value. This is also when we drew on affordance theory (e.g. Volkoff and Strong, 2013; Strong et al., 2014; Ess´en and Varlander, ¨ 2019) to understand how the features of process mining translate into action potentials to achieve certain goals. In particular, we went back to our data to see whether a framing through the lens of affordances was appropriate. Finally, we found that the categories –features, affordances and goals– integrated the other codes into one coherent model. The continuous comparison of our empirical data with the literature and ongoing theoretical reflections within our author team facilitated this process.

![](/api/attachments/QJHB7KH3/fulltext/images/484149d20cd931e876a2d987e7738d6ba4d5dffa5ea7c9161f7841163c8d19ed.jpg)  
Fig. 1. Research Process.

Table 1  
Interview Participants.

<table><tr><td>Organization</td><td>Industry</td><td>Organization Headquarter</td><td>Interviewees</td></tr><tr><td>A</td><td>Manufacturing and Production</td><td>Switzerland</td><td>(A1) Head of Business Excellence and Group Process Management (A2) Head of Operational Excellence</td></tr><tr><td>B</td><td>Chemicals</td><td>The Netherlands</td><td>(B1) Senior Manager (B2) Senior Business Process Consultant (B3) Senior Project Manager and Analyst</td></tr><tr><td>C</td><td>Healthcare</td><td>Germany</td><td>(C1) Director of Business Process Management (C2) Senior Business Process Analyst (C3) Senior Business Process Analyst</td></tr><tr><td>D</td><td>Energy</td><td>Germany</td><td>(D1) Lead Center of Excellence for process mining (D2) Vice President of Business Design</td></tr><tr><td>E</td><td>Financial Services and Banking</td><td>The Netherlands</td><td>(E1) Senior data scientist and process mining expert (E2) Product Owner / Data Scientist</td></tr><tr><td>F</td><td>E-commerce</td><td>Germany</td><td>(F1) Senior process mining Consultant (F2) Senior Process Controller and Analyst</td></tr><tr><td>G</td><td>Food Industry</td><td>Austria</td><td>(G1) Director of Business Process Management department</td></tr><tr><td>H</td><td>Automotive</td><td>Switzerland</td><td>(H1) Group Vice President, Head of Advanced Process Analytics (H2) Lead Center of Excellence for process mining</td></tr></table>

## Table 2

Open Coding Examples.

<table><tr><td>Open code</td><td>Illustrative data</td></tr><tr><td>Data accuracy and completeness</td><td>“Before process mining, we got extracts from databases and mainly looked into data manually. A lot of meetings, paper-based checks, and sample checks were required. Every year, we had more than 160,000 process cycles and we only accessed one part of all cases such as 10 or 15 samples out of 160,000. The result of these sample checks was upscaling the situation which is not based on reality.” (Interviewee D1)</td></tr><tr><td>Perceiving end-to-end process visualizations</td><td>“The main value of process mining is that it is process aware. It does not assume data to be tabular, so just rows and columns, but considers a sequence of steps executed to go from A to Z in a certain process. This helps for showing and visualizing the process map. The common KPIs [Key Performance Indicators] in traditional BI tools are also process centric but the view of the process was missing.” (Interviewee E1)</td></tr><tr><td>Sensemaking at the process level</td><td>“The improvements as they come out of the analysis is something that we don’t own but we facilitate. One of the key roles is the business analyst because first you think the tool is doing everything for you and you would see all areas and detect improvements and automation, but you need business experts to interpret the data and findings; somebody who explores, analyzes, and presents, and interprets the data [...]” (Interviewee A2)</td></tr><tr><td>Cycle time reduction</td><td>“We also worked on cyle time around customer experience, so when we see order rejections, we can now see the timestamps and then we realize that the customer is expecting the delivery and this was not communicated. So we have use cases around customer satisfaction and derive actions from our findings to act on time.” (Interviewee E2)</td></tr></table>

## Table 3

Axial Coding Examples.

<table><tr><td>Axial code</td><td>Sub-category</td></tr><tr><td>Process Mining Features</td><td>Data &amp; ConnectivityReal-time ConnectivityMulti System ConnectionQuick Data ExtractionBig Data Processing</td></tr><tr><td>Affordance-Cycle for Value Creation</td><td>Sense-making of process-related informationUnderstanding business needsBusiness-IT PartneringDefining KPIs, measurements, &amp; rules for alerts and recommendationsContinuous Monitoring &amp; EvaluationDetecting process improvement opportunitiesDescriptive &amp; Prescriptive Process AnalysisRoot Cause Analysis</td></tr><tr><td>Business Values</td><td>Non-Monetary ValuesIncreased Customer SatisfactionIncreased ComplianceIncreased Safety</td></tr></table>

Next, we discuss our findings.

## Findings

Our theoretical model summarizes the findings of our multiple case study and is depicted in Fig. 2. Grounded in the interview data from our multiple case study, our model illustrates how organizations use process mining to generate business value. It integrates three main categories: Process Mining Features, Process Mining Affordances, and Business Values. First, Process Mining Features are the tech nological characteristics of process mining software that our interviewees use (left part of the model). In particular, features comprise (1) data & connectivity, (2) process visualization, and (3) process analytics. Second, the Affordance-based Value Creation Cycle sum marizes what process mining affords to its stakeholders (middle part of the model). It comprises four affordances: (1) perceiving endto-end process models and metrics; (2) making sense of process-related information; (3) engaging in data-driven decision making; and (4) implementing interventions to adjust business process work. The cyclic character of the value creation cycle emphasizes that these affordances build on each other; the enactment of the value creation cycle takes place iteratively and continuously. In turn, the value creation cycle leads to improvements on process and organizational levels that are captured in the third category, Business Values (right part of the model). This category represents the three specific goals that are being pursued by users: process efficiency, monetary values, and non-monetary values. Additional to the three main categories, we found that value creation through process mining is enabled through Organizational Structure & Governance (lower part of the model). This category captures the adoption of process mining technology from technical and managerial perspectives. In the following, we provide a detailed explanation of each category and how they are intertwined

## Process mining features

Based on our interview data, we investigated which features our interviewees referred to when reporting on how they use process mining for value creation in their respective organization. We have coded and grouped those features into three sub-categories. First, interviewees repeatedly mentioned certain features, including (1) real-time connectivity, (2) multi-system connection, (3) quick data extraction, and (4) big data processing. These features are grouped as Data & Connectivity. Data & Connectivity indicates that process mining is usually connected to multiple source systems, thereby extracting relevant data on a real-time basis and transforming them into an event log, i.e., a process-oriented data format. Interviewees repeatedly stated that with process mining, it is easier to collect process-related data. Data collection and integration features of process mining further enable the overcoming of data collection challenges associated with traditional process analysis techniques.

“In the old days, if we wanted to improve a process, we had to have long workshops with different departments and discuss step by step what they thought was happening. With classical queries in SAP, we had to find the filter criteria that we needed to get all data pulled out of the system. Most of the time, we had to combine different types of SAP reports and merge them, and most of the data was not available to us, so we had to ask other departments. So data collection took a lot of time. The performance of excel and other tools was very difficult to handle.” (Interviewee C2)

“Before process mining, we had manual Excel sheets. So, we had SQL queries, which [we used to] retrieve data from the data lake. It was super slow with the big data. Sometimes the calculation of the file took more than 30 minutes. For preparing the management meetings, we had a minimum of 5 h every week manual workload, which with process mining is now decreased to zero, and we can focus better on the analysis and reports.” (Interviewee F2)

![](/api/attachments/QJHB7KH3/fulltext/images/1c88ca610420c92d1275fbbed00bad2a581d139778de56783c1ad012a17b0e6e.jpg)  
Fig. 2. Process Mining Value Model.

Second, interviewees emphasized the importance of Process Visualization features that visualize the process based on activities that were performed and are stored in an event log. Process Visualization features translate process data into end-to-end process diagrams. Specifically, process mining (1) visualizes the overall process flow on the grounds of the activities recorded in the connected infor mation systems, and (2) represents the process flow with respect to different criteria in a dynamic fashion. For example, process mining can depict process variants, i.e., groupings of process instances that share the same sequence of activities. Furthermore, process mining allows for drilling down into specific process performances, for example, by selecting process performances that include a certain activity. Our interviewees reported that process mining offers high levels of detail and various possibilities to filter process behavior.

“If you don’t have data, then you put a couple of people in a room and sketch the process as they envision it goes in reality. But experts always have a personal and limited view of the process. With process mining, if you get the right data then you have complete and realistic data. So, you see the exceptions that happened once or twice. If you talk to experts, you get the happy flow or 80 % flow but with process mining you see a complete model.” (Interviewee E1)

“You can set the filters together with the business and immediately see the process flow and its variants. This is a dramatic change comparing to previous workshops where we got only one model that people had in mind as their best flow. With process mining you see all process variants. You can directly validate the process with business units and discuss further filter criteria.” (Interviewee C2)

Third, interviewees stated that process mining provides various features for Process Analytics. This includes: (1) the calculation of key performance indicators (KPIs) on the process level; (2) rule-based alerts and action recommendations; and (3) the comparison of the process to a predefined model (conformance checking). Process mining software provides several standard KPIs (e.g., cycle time), but also enables organizations to calculate customized process KPIs.

“An important use of process mining for us is that it's KPI driven. We can calculate the KPI that is defined together with the business. We used the corporate definition of KPIs and rolled [them] out automatically so people are not manually gathering data and reporting KPIs and they do it automatically using process mining on top of SAP systems.” (Interviewee H1)

Process mining features allow for setting process-related rules and conditions for triggering process activities. The user receives alerts and action recommendations if rules are violated or conditions met. These alerts and recommendations prompt users to potentially harmful or inefficient process behavior, and allow users to address them proactively.

“With process mining, we monitor what is changing, why it is changing and where, and receive the list of violations and where they are happening, as well as receiving recommendations on what to do with the detected violations.” (Interviewee G1) “Process mining sends us signals and recommended actions based on defined process rules, and we derive actions on time form these signals. For instance, we find if an RPA bot is not functioning or if there are automation opportunities in our processes.” (Interviewee B1)

Another Process Analytics feature of process mining is conformance checking. Often used by internal audit departments, confor mance checking activities involve comparing the performed process as documented in the event-log against a respective process mode to detect and classify deviations, such as undesired activities or undesired sequences of activities

“We use process mining features such as the conformance checker to understand the differences and learn what is the most efficient process and what needs to be changed. We realize what are the gaps that we need to fulfill. Why is it not happening in other regions? By that we make global decisions on, for instance, process standardization.” (Interviewee B1)

Table 4 summarizes the sub-categories related to process mining features.

## Table 4

Process Mining Features.

<table><tr><td>Sub-Category</td><td>Description</td><td>Examples</td></tr><tr><td>Data &amp; Connectivity</td><td>Features that extract, integrate, and combine process-related data.</td><td>Receive, extract, and transform process data as they are executedConnect multiple source systemsGather and analyze big dataTransform data into process log</td></tr><tr><td>Process Visualization</td><td>Features that visualize process execution.</td><td>Visualize processes based on executed process activitiesAdapt process visualizations based on different criteria (e.g. activity selection)</td></tr><tr><td>Process Analytics</td><td>Features that generate various process-related KPIs.</td><td>Use out of the box or define customized KPIsPossibility to define rules and conditions and accordingly receiving alerts as something deviates from expectations in the processCompare ‘as is’ against ‘to be’ process models to detect deviations</td></tr></table>

## Affordance-based value creation cycle

Our study revealed how our case organizations enacted upon the process mining features in order to generate value in their or ganization. Stakeholders perceive and enact a set of affordances as they aim to realize business value. In specific, process mining affords them: 1) perceiving end-to-end process visualizations and performance indicators; 2) sense-making of process-related infor mation; 3) data-driven decision making; and 4) implementing interventions. These affordances refer to each other in a circular way. Importantly, there is a feedback loop between the implementation of interventions and the perception of how the respective process is enacted. Because process mining affords quick connectivity to a variety of source systems, process changes are almost instantly visualized. Depending on whether or not intended process changes have been realized, another iteration in the value creation cycle might be triggered. In the following, we explain the affordances in the value creation cycle in detail.

## Perceiving end-to-end process visualizations and performance indicators

Process mining visualizes process activities performed as well as their causal-temporal interdependence, which we conceptualize as the affordance of perceiving end-to-end process visualizations and performance indicators. In our interviews, all respondents stated that process mining creates end-to-end transparency. Our interviewees indicated that this transparency affords them an objective perspective on process performance. Whereas traditional process analysis and evaluation relied on discussions and subjective in terpretations (see e.g. Huising, 2019), process mining enables an objectively shared view on business processes among all stakeholders. This, in turn, prompts discussions among managers and analysts around the behavior of the process as well as potential improvements.

“The only way to improve the process is to understand it, and therefore, you need process transparency. In the past, we missed this transparency. Talking to different consultants, having workshops, asking five different people, getting five different views of the process, and then thinking and guessing where the issue is and how to resolve it was very time-consuming. Now with the power of instant and continuous transparency on the processes [afforded through process mining], we directly see changes and where we can improve the process.” (Interviewee D2)

“The main thing is transparency. That is how we react faster to bottlenecks, be more efficient, and save costs because we have faster production. We have less manual effort and spend much less time on data gathering and preparation, and therefore have more time to do deep analysis.” (Interviewee F2)

Hence, process mining enables insights into process behavior, even among users who might not be specialized in process analysis or data analytics. Overall, these insights are useful because they are comprehensive and accurate.

“We were previously dependent on one person who is an expert in querying and finding out what’s wrong with the process, but we never had a complete overview of how the process functions, and finding issues or improving processes were mostly symptomatic. People assumed that everything works as it is designed. Now we see a pile of spaghetti [i.e., a large number of different process enactments] and right away see there are lots of things that can be improved.” (Interviewee E2)

“Previously we never had a tool that could manage such a high volume of data from an end-to-end point of view. So, the visibility was never there before in upstream activities. For example, what is really happening to sales orders? We monitored specific things in different projects but never saw in such a way what actions were driving specific KPIs. With process mining, we can go down and see what kind of behavior is in the process.” (Interviewee B2)

Finally, process KPIs provide high-level indications about the health of the process and guide users in their analysis efforts. As the following quote illustrates, KPIs can indicate process issues, which can then be further examined by drilling into the data and process visualizations

“We continuously check and monitor KPIs. When we see a specific KPI got worse, then we specifically focus on that topic to see the bottleneck and drilldown to find the root cause. So, we filter on specific data attributes to see where and how the problem is appearing. We communicate these results to the management and responsible teams. If there are small problems, then oper ational experts look into it, find root causes and make sure to prevent those issues. If the problem is bigger in the process, then the process excellence team contacts different teams and speaks to relevant people, then initiating brainstorming and design thinking sessions to discuss potential solutions […].” (Interviewee F2)

## Sense-making of process-related information

Process mining provides an end-to-end perspective on how processes are executed. To understand the current performance of a process and identify improvement opportunities, process mining affords stakeholders to engage in sense-making of process-related information – i.e., interpreting and discussing process mining visualizations and KPIs in light of contextual information (e.g., external factors such as country regulations or COVID-19 impact on organizational objectives) on business processes. Sense-making hence helps understand the needs of involved stakeholders, find root causes, identify opportunities for process improvement, and, ultimately, supports decision making.

Knowledge of both technical and business aspects is key to turning representations in process mining software into actionable information. On the one hand, organizations need to build up technical expertise to guarantee data availability and correct usage of features. On the other hand, contextual knowledge is required to interpret findings and draw conclusions from process mining. This contextual knowledge pertains to information on processes and respective regulations to triangulate findings derived through the analysis of process visualizations and KPIs. In other words, this knowledge helps to differentiate actual bottlenecks from noise. For example, contextual knowledge might relate to differences in laws and business practices across different regions. While in Europe the payment of goods is usually triggered after goods receipt, in Russia, payment is typically required before goods delivery. Emphasizing the importance of contextual knowledge to interpret process mining results, one interviewee stated:

“Process mining provides all the data, but you need to know how to interpret it, to place the right filters, and understand the sequence of activities, and know if there are some issues in the process flow. You need to understand and be able to translate what happens in the system vs. what you see in the tool. Knowledge is needed to interpret the results and show the right things to the business.” (Interviewee B3)

With the respective contextual knowledge, process mining findings can be interpreted to identify inefficiencies and detect process improvement opportunities.

“Process mining is like your partner on the journey of continuous improvement. Process mining is part of our improvement methodology. It supports root cause analysis, dashboarding, and tracking and monitoring. With process mining, we understand variations and where they are happening. We understand if the variations are valid or not. With the help of process mining, we understand how can we remove, optimize, or automate these steps.” (Interviewee G1)

Interviewees stated that process mining affords sense-making both in terms of descriptive and prescriptive analyses. Process mining not only affords the analysis of past data but also predicts probable process behaviors. By providing alerts and action recommenda tions, process mining enables processes to run smoothly and detect problems.

“I see the real value in using process mining on the one hand for descriptive analytics and continuous improvement and on the other hand on having prescriptive analytics and to make sure that based on the real-time information, we work much faster on improving the operations. So, we are not only analyzing the process with process mining but also driving processes.” (Inter viewee H1)

“We have built analyses, defined rules for receiving signals, and started creating value for the purchase-to-pay process by optimizing the process […] and acting on-time to changes based on alerts that we receive from process mining.” (Interviewee B1)

While process mining affords continuous monitoring of KPIs, it goes beyond the sole reporting of KPIs and adds more granular information by offering adjustable visualizations of process behavior. Users can visually inspect processes with varying levels of detail by drilling into the data. If certain activities of the process seem interesting, users can analyze the process behavior on a more granular level to detect deviations and their respective root causes.

“In process mining, we have a process view to see how the process works. We can focus on process-specific analysis such as process variants, wrong sequences, missing process steps, the cycle time in processes, and that’s something you can’t get from any other tool. For example, we get the information that an order is not on time, and we can see the root cause of why the order is not on time. For instance, we see that specific plants or vendors are mostly correlated to certain violations.” (Interviewee A2) “Initiating process improvement is always a challenge. What needs to be changed and where should we start? Process mining helps to understand evaluating and monitoring process metrics and know where a change is needed. The ability of process mining lies in drilling down into the data and discovering what is going wrong and why is it going wrong. It supports process management in a way to know what needs to change and when.” (Interviewee B3)

Overall, the combination of process mining results and contextual knowledge affords sense-making of process-related information and the identification of opportunities for process improvement.

## Data-driven decision making

Based on their understanding of process-related information, stakeholders plan, prioritize, and select suitable process interventions based on data provided by process mining. Compared to other techniques to derive and decide about process improvements, in terviewees argued that, with process mining, decisions can be made based on data that originates from their source systems.

“Process mining is about the system’s data, so it’s something that you can’t argue against. Therefore, it is used for decision making. There is a council that is making decisions based on findings. These decisions are so far taken on process conformance. For that, we identify how processes are being executed by different attributes such as regions and then compare the process variants in terms of rework activities, cycle times etc. and find the best combination of attributes and then think about potential changes.” (Interviewee B3)

Based on these data, organizations assess the financial impact to be realized from improvement opportunities and prioritize them accordingly.

“Process change is initiated from process mining findings. A group of analysts identifies opportunities in different domains of processes, qualifies and quantifies those opportunities, and submits them to the global process owner. If the case value is over €100 k, we will put it in the project charter, and if it’s below €100 k but operationally beneficial, we would cascade it down to business. We can realize that there is a specific change in behavior or process setup, and then we focus on value-adding ac tivities.” (Interviewee B2)

Organizations also use process mining to leverage knowledge on processes across the organization. While formerly, due to lack of objective data, it was difficult to compare processes performed in different regions, process mining can be used to objectively assess processes and make decisions grounded in data.

“We are looking at the process and evaluating the best way to purchase technical services. For example, for hiring contractors in a plant or getting some services done on the plant for maintenance. We use process mining capabilities such as the conformance checker to learn the most efficient process and understand why this is not happening in other regions. With process mining, we realize all reworks and deviations and make global decisions proactively, such as standardizing processes. Before process mining, we were not able to make global decisions at all. Everybody thought they had the best process in place and were not open to changing anything.” (Interviewee B1)

## Implementing interventions

After perceiving visualizations, making sense of process-related information, and making decisions, process mining also affords organizations to design and implement interventions to improve their business processes and overall organizational performance. Interventions comprise changes to processes, systems, and organizational policies. For instance, conformance checking is used to compare the ‘as is’ processes with a process model in order to detect deviations. Consequently, deviations are prioritized based on the severity of mismatch, and actions are performed to reach the desired standardization level. Another example is the reduction of costs through the reduction of rework and the elimination of unnecessary activities. One interviewee explained that their organization changed the system set up in order to improve the management of payment blocks in their Order-to-Cash process. The interviewee further describes how interventions are based on sense-making of process mining results and how they affect process performance.

“We realized that 30 % of orders are getting blocked due to credit checks, and 99 % of them are released on the same day. This was a huge cost as it is an outsourced activity to unblock those orders. Using process mining, we identified what was causing them, meaning which blocks we have in place, and changed the system set-up in different regions. The number of blocks went down, but the ones remaining on the block went up, and that is good because people don’t release everything automatically and security is increased but really spending time to properly check when there is a more effective credit policy and look at those orders.” (Interviewee B2)

Another example for interventions is the plant maintenance process, where organizations use process mining to perform risk as sessments and change their processes to increase workers’ safety.

“Process mining increases safety in a way that shows if a working permit ticket due date is passed and the permit is not returned, so we know somebody is not allowed to work at a certain time. We can’t start the powerplant and bring back the power as it can be dangerous. A team member should go to the place and check for the reasons.” (Interviewee D1)

Above, we described some of the common interventions that organizations take as a result of insights derived from process mining. Other types of interventions include updating the master data, negotiating with suppliers for better contracts, and performing changes in processes, systems, or organizational policies.

## Feedback loop

We also identified a feedback loop between the implementation of interventions and the perception of how the respective process is enacted. Because process changes are almost instantly visualized and performance indicators recalculated, it is possible to constantly check processes and see if interventions have led to satisfying results. If the process is not performed as expected, further actions can be taken to make sure that the gap between the as is' and to be' process is minimized. Thus, process mining allows organizations to examine the effects of interventions on organizational processes at unprecedented speed and accuracy.

## Table 5

Affordance-Based Value Creation Cycle.

<table><tr><td>Sub-Category</td><td>Description</td><td>Examples</td></tr><tr><td>Perceiving End-to-End Process Visualizations and Performance Indicators</td><td>Perceiving process visualizations and performance indicators and adapting them to focus on specific parts of the process.</td><td>·Perceiving process visualizations·Perceiving process KPIs·Adapting process visualizations according to chosen criteria</td></tr><tr><td>Sense-making of Process-related Information</td><td>Interpreting process visualizations and KPIs in light of business knowledge to detect issues and improvement opportunities.</td><td>·Interpreting process mining findings in light of contextual knowledge (legal, cultural, etc.)·Finding root causes and reasons correlated to the current issues·Identifying improvement potential</td></tr><tr><td>Data-Driven Decision Making</td><td>Planning, prioritizing, and making decisions on how to approach detected issues and improvement opportunities.</td><td>·Planning,·Prioritizing·Making decisions</td></tr><tr><td>Implementing Interventions</td><td>Implementing interventions to improve process work.</td><td>·Eliminate unnecessary process steps·Reduce rework·Standardize processes</td></tr></table>

“Whenever we try something new or adjust something, we can see the results the day after. So, we can check if the process change went wrong or not, and react quickly.” (Interviewee F2)

“With process mining, you can continuously measure KPIs and determine areas to define new KPIs. You can measure the change and evaluate if you were successful or not. We mainly follow the DMAIC methodology from Six Sigma. We are using process mining in different phases of this methodology, for example, to define critical KPIs, determine them in ‘as is’ analysis, and control them to show the improvements. We take action items for improvements out of process mining and include them in our Kanban boards.” (Interviewee C3)

Table 5 summarizes the sub-categories related to the affordances of process mining.

## Business values

We were also interested in the various goals that process managers and analysts pursue as they draw from process mining features and enact affordances. We intended to identify different value dimensions to which the use of process mining can contribute. Table 6 summarizes the sub-categories related to the business values of process mining. The first sub-category addresses values that relate to different aspects of process efficiency. Process mining usage leads to the reduction of process cost and cycle time, RPA optimization, and increased First-Time-Right (FTR)

“RPA is supported by process mining. Once we have visibility to the end-to-end FTR, then we detect automation opportunities and support monitoring the bots. In process mining, we see when we get all those spaghetti processes and so many variants, and for sure, we don’t want the bot to go through all those paths. So, we use process mining first to stabilize the process and then automate it.” (Interviewee B2)

The second sub-category refers to monetary values. In contrast to the first category, these business values do not relate to the im mediate improvement of process efficiency, but aim at the improvement of overall organizational indicators. First, working capital optimization ensures sufficient cash flow and efficient management of obligations and operating costs. Second, Full-time Equivalent (FTE) productivity reflects the working hours that a full-time employee requires to execute a certain task. This metric is used for cost estimations and for planning the hiring of new employees. One interviewee stated with respect to the Purchase-to-Pay (P2P) process:

“When we pulled in all data in the P2P domain, we saw that a third of our purchasing orders were less than €200 coming from non-product related units, which first explained that we have highly inefficient non-product related processes in place on the purchasing side (e.g., office supplies and marketing costs). We realized that everybody was placing orders in different offices with no policies and authorization. That impacts people’s productivity a lot. We could see which areas of the business create a high volume of orders and restructure the FTEs accordingly. We also focused on working capital. We improved the operating cash coming from different areas of opportunities that impact working capital ultimately. It brings a financial bottom line, so it’s very useful.” (Interviewee B2)

The third sub-category summarizes non-monetary values generated by process mining and includes customer satisfaction, increased compliance, and increased safety.

“The main goal for us is customer satisfaction. Using process mining, we look into finding correlations between happy and unhappy customers and their process flows and customer journey. For this purpose, we are looking into the perceived customer value and underlying metrics like throughput time and the number of customer calls. In the first phase of customer satisfaction analysis with process mining, we were investigating why people called before receiving their retirement payment. We realized that on our end. the process seemed to have a clear end and that people should wait to retire and then, at the end of the month. receive their payment. But in process mining, we saw that people called a lot in this phase, and we had to explain the process. Therefore, we took the necessary actions to inform people about our online self-service portal and send them the retirement plan and FAQ explaining the process. This resulted in happier customers and receiving fewer calls from them.” (Interviewee E1)

Table 6  
Business Values.

<table><tr><td>Sub-Category</td><td>Description</td><td>Examples</td></tr><tr><td>Process Efficiency</td><td>Business values that pertain to process efficiency gains realized from process mining.</td><td>Reduce process costsReduce process cycle timeIncrease first-time-rightOptimize robotic process automation</td></tr><tr><td>Monetary Values</td><td>Business values that pertain to monetary values on an organizational level realized from process mining.</td><td>Optimize working capitalIncrease full-time employee productivity</td></tr><tr><td>Non-Monetary Values</td><td>Business values that pertain to non-monetary values realized from process mining.</td><td>Increase customer satisfactionIncrease process complianceIncrease employee safety</td></tr></table>

Organizational structure & governance

Our investigation also revealed insights into roles and responsibilities associated with process mining, which we summarized under the category Organizational Structure & Governance. This category encompasses all necessary cultural and administrative work as wel as governance initiatives that need to be carried out to support the use of process mining technology for value creation, and thus, enact the affordances identified. Cultural aspects and change management were reported as important requirements to support value cre ation. Process mining affordances, such as process analytics and process visualization, provide both value and challenges for orga nizations according to our interviewees. Before implementing the technology, employees asked for guarantees that process mining is intended to help them do their job more efficiently and that it will not be used for finger-pointing or individual performance moni toring. In order to be able to achieve sustained organizational acceptance and usage, employees must trust the technology.

“You should avoid being in the role of the police and finger-pointing. People were asking if this is a tool for observing people, and we had to talk it through and show the value of the technology. We went to different departments and presented the technology and learnings and showed its potential to increase trust to get the open doors.” (Interviewee D1)

Our case organizations employed different governance models with specific responsibilities to support process mining usage. While exact implementation details differed, all governance models aim to facilitate the usage of process mining, provide training, and increase the readiness and awareness about process mining throughout the organization. The governance team should make sure that process stakeholders are involved early on in the project. In this context, it has proven successful for organizations to start exper imenting on a small scale before engaging in global projects.

Our analysis shows that an important factor in creating value with process mining is to have clear responsibilities for tool pro motion and usage. Merely promoting the technology in the organization without assigning clear responsibilities will not lead to value creation. To facilitate adoption and value creation from process mining, a functioning business-IT partnership is integral. Different skil sets, such as tool expertise, technical expertise, and process expertise must be combined –oftentimes across established boundaries within an organization– to generate valid insights with and draw correct conclusions from process mining. In this respect, one interviewee commented:

“In the process mining center of excellence, we collaborate with experts from the business side to do data validation to make sure we are looking at the reality. Implementation of a measure is the business’s responsibility, but then tracking and controlling them can be done by the center of excellence.” (Interviewee A2)

Overall, process mining requires organizational structures and governance as much as many other technologies do. However, governance plays a crucial role in supporting the adoption and usage of process mining features and, therefore, is included in the model. Our interviewees pointed to cultural readiness and trust, as well as skill sets, along with collaboration, commitment and involvement, and governance models as the most important aspects related to the category organizational structure and governance. Because this category supports but is not directly part of the value creation with process mining, we omit a corresponding table with sub-categories and their descriptions for space reasons.

## Implications

Our study makes important contributions to the understanding of how organizations use process mining (e.g. Mans et al., 2013; Eggers et al., 2021) and how they use process mining to realize business value, in particular. Focusing on process mining allows us to explore how organizations gain value as they leverage real-time process data on a continuous basis to assess their process performance, gain process visibility, detect root causes, and take appropriate decisions. Following a qualitative-inductive approach to understand how features of process mining provide affordances (Volkoff and Strong, 2013; Strong et al., 2014; Ess´en and V¨arlander, 2019) for value realization, we provide a dynamic view of the value creation process (Sharma et al., 2014; Boˇziˇc and Dimovski, 2019). Spe cifically, our study has important implications for (1) research on BI&A, (2) research on behavioral visibility, (3) research on IT value realization. (4) research on process mining, and (5) practice.

Implications for research on business intelligence and analytics: business process intelligence as a new class of business intelligence and analytics

We argue that BPI is a new class of BI&A that is concerned with creating transparency and behavioral visibility of end-to-end business processes to enable ongoing value creation. BPI is different from well-understood BI&A technologies that support specific decisions and strategic initiatives, in that it focuses on the development of algorithms and methods to make end-to-end organizational processes transparent and analyzable on a continuous basis (Grisold. Mendling, et al., 2020: Eggers et al., 2021: Martin et al., 2021)

Although process mining has been previously identified as a BI&A technology (Chen et al., 2012), the adoption of the term BPI (Grigori et al., 2004; Tan et al., 2008; Castellanos et al., 2009; van der Aalst et al., 2015) allows us to recognize the full potential that the analysis of real-time process log data offers. Recognizing BPI as a distinct field in BI&A, further enables research to study the unique features and value creation mechanisms associated with these process-centric technologies, such as process mining and RPA. Our results already indicate important conditions regarding cultural aspects and change management. Arguably, BPI technologies will also require new organizational structures and governance models to support the continuous evidence-based analysis and improvement of business processes (Grisold, Mendling, et al., 2020).

Our findings provide first empirical insights into how organizations can capitalize on the transparency created by BPI technologies to (1) perceive end-to-end process visualizations and KPIs; (2) make sense of process-related information; (3) enable data-driven decision making; and (4) support process interventions. The realization of value through process mining as a BPI technology takes the form of an ongoing cycle where emerging insights, interventions, and realized outcomes constantly influence each other. Thus, interventions taken to change the process influence subsequent sense-making and decision making regarding further process improvements.

Taken together, we suggest that process mining belongs to an emerging class of BI&A technologies that is referred to as business process intelligence (BPI). By explaining how process mining affords value creation as employees use this technology on a continuous day-to-day basis, our study provides a new angle on the BI&A literature where the main emphasis had been placed on value creation through the strategic use of big data (Trieu, 2017; Lehrer et al., 2018; Anand, Sharma and Kohli, 2020).

## Implications for research on behavioral visibility: discovering process work from digital trace data

Process mining as a BPI technology offers features that relate to the emerging phenomenon of behavioral visibility (Leonardi and Treem, 2020) in organizational contexts. The key idea behind behavioral visibility is that people leave digital traces when interacting with digital technologies. The datafication of their behavior enables further analyses and insights, e.g., by finding previously unknown patterns and correlations. In the case of process mining, this is provided through features that make it possible to discover dynamics of process work, such as process deviations (Carmona et al., 2018; Augusto et al., 2019; Grisold, Wurm, Mendling and vom Brocke, 2020). Leonardi and Treem (2020) also stress that the availability of visible behavioral data has implications for decision making. On the one hand, one can ground decisions in facts gathered across multiple instances in which a specific performance took place. On the other hand, one can make inferences from these data about causes and motives of actors (Pentland, 2014; Zhang, Li and Krishnan, 2020) Both observations resonate with arguments that are made in relation to process mining. The opportunity to make fact-based decisions for processes is considered a key tenet of this technology (van der Aalst, 2016; Dumas et al., 2018), and arguments in the literature stress that this affords new management practices (Grisold. Wurm. et al., 2020: Reinkemever. 2020). Our study contributes to this stream by showing how behavioral visibility can manifest in organizational contexts and how it can be managed in order to gain value

## Implications for research on process mining: from technical to socio-technical contributions

Our research also speaks to the field of business process management. Process mining is emerging from this field, where but it is primarily looked at from technical perspectives (Grisold, Mendling, et al., 2020; Martin et al., 2021). While recent claims suggest that process mining’s broader implications are key to understanding how and why process mining is adopted in organizations (or, for that matter, not adopted) (Grisold, Mendling, et al., 2020; Reinkemeyer, 2020), empirical findings are scarce (vom Brocke et al., 2021). Adopting a qualitative-inductive approach to study the affordances through which process mining leads to value realization, we provide BPM research with a new perspective to look at process mining. Our findings emphasize that process mining not only relies on algorithms and techniques but that we need to acknowledge human capabilities and goals. along with organizational factors (Keller et al., 2019). Finally, we sketch out what forms of value are associated with process mining. Our model explains how process mining realizes its value across different levels. Following vom Brocke et al.’s (2021) recent five-level framework to study process mining, our findings stress the connection between the technical level (technological features), individual level (which involves sense-making, decision making, and interventions), and the organizational level (where value is ultimately realized).

Future research can further investigate the organizational implications of process mining. For example, Wixom and Watson (2010) emphasize that the real-time visibility of processes requires new structures and forms of organizing. Some estimates suggest that 60–70 % of business intelligence implementations fail due to various issues, including the culture of an organization (Olszak, 2016). Therefore, future research can explore which competencies and skills are required to adopt process mining successfully, or are related to perceiving certain affordances over others (see Leonardi, 2013). An exemplary guiding question could be: What is the best way of raising awareness and increasing trust among people to use process mining? In this respect, a recent report by Celonis finds that a structured governance increases the return on investment from process mining, irrespective of the exact organizational set-up (Reinkemeyer et al., 2022).

In our study, we did not encounter contradicting opinions among our case companies. but realized common usage patterns despite contextual differences, such as the use case and organizational size. However, we encountered differences in objectives for the usage of process mining technology, which are reflected in our theoretical model. For instance, one case organization primarily focused on nonmonetary values, specifically the improvement of customer satisfaction and the safety of employees in the plant maintenance process. Another case organization was mainly using process mining for financial matters, controlling cash flows, and optimizing working capital. Regardless of their objectives, interviewees’ accounts were similar with regards to the affordances they enacted based on process mining features. Hence, while the exact use case of process mining might be different, the way that organizations realize them is based on the action opportunities it provides.

## Implications for practice: three pillars to understand how process mining leads to business value

A number of implications for practice arise from our study. First and foremost, our analysis and theoretical model point to three main pillars that help practitioners understand the impacts of process mining and how it leads to business value. To this end, it is crucial to understand and adopt process mining features that afford continuous process monitoring, data-driven decision making, and proactive decision making. Second, it is important to create process awareness and understand business processes, scenarios, and rules to make the most sense of existing data and execute process steps. Third, people and change management initiatives are key to involving the right stakeholders early, providing training, improving communication, increasing trust and confidence in the tool, and forming a governance model to capitalize on the features and affordances of this technology.

Furthermore, the real-time connectivity to live source systems provides full transparency over how processes are performed. Such connectivity and end-to-end transparency of process data afford continuity in monitoring, data-driven decision making, and in terventions into processes. An important implication of our theoretical model is that process improvement opportunities can be derived and process changes can be evaluated much faster than with the classical BPM lifecycle as outlined by Dumas et al. (2018). Process mining saves considerable work in the lifecycle phases of process discovery, design/redesign, analysis, and monitoring, leading to faster value realization than classical process improvement approaches.

Finally, pursuing business value needs proper sense-making of available data to understand the meaning of process events (Boland, 2008), make decisions, and take appropriate actions (Dervin and Foreman-Wernet, 2012). Activities regarding sense-making, datadriven decision making, and interventions are impacted by mining features such as real-time connectivity and end-to-end transparency of processes in terms of speed and accuracy. The complete view over process data and its metrics ensures continuous process man agement while proactively sensing and responding to changes. However, our analysis shows that contextual knowledge in business rules and process experience is needed in order to realize impacts. Also, in order to realize the full value spectrum of process mining, organizations should increase their readiness for adopting the technology. People should trust it and always be aware of its existence for the projects they have ahead of them.

## Limitations

Our study entails certain limitations. Our insights are limited to the experiences of our interviewees. The interviewees were involved in different projects, spent different periods working with process mining, and were part of different organizational structures and cultures that potentially could influence their experience with the technology. Additionally, we only accessed companies that were successful in the usage of process mining. While this sampling strategy is appropriate to answer our research question, the investigation of unsuccessful cases may shed further light on roadblocks and process mining limitations. Furthermore, we do not account for the different types of processes that process mining was used for. Certain processes impact organizational performance more than others (e.g. Tallon, Kraemer and Gurbaxani, 2000; Melville, Kraemer and Gurbaxani, 2019), primarily due to the scope and importance of the process for overall value creation of the respective organization (Dehning and Richardson, 2002; Subramani, 2004; Elbashir, Collier and Davern, 2008; Melville et al., 2019). It is likely that these processes profit more from process mining initiatives, than other less important ones.

## Conclusion

In this paper, we reported on a qualitative study to investigate how organizations create business value with process mining. We carried out a multiple case study with key stakeholders from organizations that differed regarding their size, industry, and objectives for using process mining. Grounded in our data, we derived a model that explains how process mining generates value for organi zations. Our findings suggest that the features of process mining – data & connectivity, process visualization, and process analytics – afford a value creation cycle with (1) perceiving end-to-end process visualization and performance indicators, (2) sense-making of process-related information, (3) data-driven decision making, and (4) implementing interventions, whereby a feedback loop affords evaluating whether and how interventions have led to changes in process behavior. In turn, the proposed value creation cycle yields to increased process efficiency as well as monetary and non-monetary business values. Our findings contribute to research on value creation with BI&A and BPI technologies in particular. Future research can investigate success factors for the adoption of BPI tech nologies and how governance models to support effective use develop over time

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

This research was carried out, among others, within the framework of the Schöller Senior Fellowship on “Process Science - The Interdisciplinary Study of Continuous Change”. The research has also been funded by the Hilti Family Foundation, the ERASMUS + program of the European Union (EU Funding 2021-1-LI01-KA220-HED-000027575 “Developing Process Mining Capabilities at the Enterprise Level”) and by the Liechtenstein Research Fund (grant number 705076 “Process Science: Conceptual foundation for the interdisciplinary study of continuous change”). We would like to express our gratitude to the Dr. Theo and Friedl Scholler-Foundation,¨ the Hilti Family Foundation Liechtenstein, the European Union, AIBA Liechtenstein, and the Principality of Liechtenstein

Appendix A:. Case organization details

<table><tr><td>Organization</td><td>Description</td><td>Size in employees</td></tr><tr><td>A</td><td>Case A is an international organization with headquarters in Switzerland. It provides products, services, and systems for the construction industry. Organization A claims to be keen on getting new impulses to improve processes and customer satisfaction. Process mining supports firm A to achieve global process excellence by better handling the process management lifecycle (documentation, analysis, implementation, and monitoring). The main objective of Organization A to use process mining is continuous and data-driven management.</td><td>25,001–50,000</td></tr><tr><td>B</td><td>Case B is a chemical producer with headquarters in the Netherlands. It focuses on solutions for water purity as well as the improvement of food safety and packaging. Process mining supports firm B to continuously improve business processes, find process automation opportunities, and increase process compliance. Organization B&#x27;s main objective for using process mining is continuous and data-driven management as well as process automation.</td><td>10,001–25,000</td></tr><tr><td>C</td><td>Case C is a global organization with headquarters in Germany that provides medical instruments for human and veterinary medicine. Traditionally, business and process-related decisions were taken based on the intuition of the CEO and the BPM team. Process mining supports organization C with continuous and data-driven decision making. Organization C&#x27;s main objectives for using process mining are process compliance, and system migration.</td><td>5,001–10,000</td></tr><tr><td>D</td><td>Case D is an international organization with headquarters in Germany. The company provides energy services and products, such as operating in power plants for producing electricity. Process mining supports organization D to increase work safety by enabling real-time connectivity and increasing the transparency on working permits. It also optimizes processes and increases conformity. The main objective of organization D to use process mining is audit and compliance.</td><td>10,001–25,000</td></tr><tr><td>E</td><td>E is a Dutch organization providing pension schedules and associated services. One of its key strategic goals is customer satisfaction. Process mining supports organization E by enabling continuous and data-driven management of processes. Process mining allows organization E to focus on the customer journey, and to detect and remove process bottlenecks (e.g., reducing the number of customer calls) to reduce costs.</td><td>1,001–5,000</td></tr><tr><td>F</td><td>Case F is an international fashion retailer with headquarters in Germany. The organization sees itself as a driver for innovation in the fashion industry and is open to new ideas to better focus on customers and employees. Process mining supports organization F in data-driven management, provides an end-to-end process perspective, helps to sense crucial process changes, and respond to these proactively. Organization F&#x27;s main objective for using process mining is continuous and data-driven management and process automation.</td><td>10,001–25,000</td></tr><tr><td>G</td><td>Case G is an international organization with headquarters in Austria. The organization sees itself as best in class in producing high-quality drinks and beverages. To stay competitive, organization G emphasizes continuous and data-driven management of processes to decrease process inefficiency and costs while increasing quality. Process mining supports organization G to connect multiple systems in real-time, ultimately increasing transparency on organizational processes. This newly gained transparency helps organization G to support continuous improvement (e.g., 6 Sigma DMAIC cycle), RPA, and process documentation. The main declared objective of organization G for using process mining is continuous and data-driven management.</td><td>10,001–25,000</td></tr><tr><td>H</td><td>Case H is an international organization with headquarters in Switzerland, providing various products such as electrical motors. Process mining supports organization H to manage processes end-to-end by integrating more than 40 ERP systems. In turn, this accelerates the speed of getting insights on process quality, detecting supply chain inefficiencies, and reducing lead-time to customers. Organization H&#x27;s main objective for using process mining is continuous and data-driven management and process automation.</td><td>greater than50,000</td></tr></table>

## Appendix B:. Interview guideline

## Block 1: Intro and General questions

1. Introduction: How do you describe your working position?

2. How much experience do you have with process mining?

## Block 2: Question concerning the decision on adoption and implementation (awareness-to-implementation)

3. Why did your organization decide to adopt process mining?

4. What is/was the organizational setup for process mining in your organization?

5. How did higher management levels support process mining in your organization?

6. What were the organizational pitfalls you faced while implementing process mining?

7. How did you deal with the pitfalls?

## Block 3: Questions concerning the use of process mining (implementation-to-use)

8. How does process mining impact your daily work? How often do you work with process mining?

9. How many people are actively using process mining in your organization?

10. How do you encourage/ensure the use of process mining?

11. What are your key learnings from the implementation of process mining?

## Block 4: Changes before/ after process mining (use-to-impact)

12. What are the main application scenarios of process mining in your organization?

13. How did you approach these application scenarios before using process mining?

14. How did the way you do process management change since the introduction of process mining?

15. How did process mining impact process analysis in your organizations?

16. In what ways does process mining create business value from your point of view? (1- value generation, 2- productivity, 3- communication, 4- routines?! and day to day work)

17. How did process mining impact your decision making process?

18. How do you translate the results out of process mining into strategies and actions?

## References

Anand, A., Sharma, R., Kohli, R., 2020. The effects of operational and financial performance failure on BI&A-enabled search behaviors: A theory of performance driven search. Information Systems Research 31 (4), 1144–1163.

Augusto, A., Conforti, R., Dumas, M., La Rosa, M., Maggi, F.M., Marrella, A., Soo, A., 2019. Automated Discovery of Process Models from Event Logs: Review and Benchmark. IEEE Transactions on Knowledge and Data Engineering 31 (4), 686–705.

Augusto, A., Mendling, J., Vidgof, M., Wurm, B., 2022. The connection between process complexity of event sequences and models discovered by process mining. Information Sciences 598, 196–215.

Boland, R. J. (2008). “Decision Making and Sensemaking.” In: F. Burstein & C. W. Holsapple (Eds.), Handbook on Decision Support Systems 1 (pp. 55–63).

Bordeleau, F.E., Mosconi, E., de Santa-Eulalia, L.A., 2020. Business intelligence and analytics value creation in Industry 4.0: a multiple case study in manufacturing medium enterprises. Production Planning and Control 31 (2–3), 173–185.

Boˇziˇc, K., Dimovski, V., 2019. Business intelligence and analytics for value creation: The role of absorptive capacity. International Journal of Information Management 46 (February 2018), 93–103.

Carmona, J., van Dongen, B., Solti, A., Weidlich, M., 2018. Conformance checking. Springer.

Castellanos, M., A. K. Alves de Medeiros, J. Mendling, B. Weber and A. J. M. M. Weijters. (2009). “Business Process Intelligence.” In: Handbook of Research on Business Process Modeling (pp. 456–480)

Charmaz, K. and L. Belgrave. (2012). “Qualitative interviewing and grounded theory analysis.” In: The SAGE handbook of interview research: The complexity of the craft (2nd ed., pp. 347–365).

Chen, H., Chiang, R.H.L., Storey, V.C., 2012. Business Intelligence and Analytics: From Big Data to Big Impact. MIS Quarterly 36 (4), 1165–1188.

Davenport, T.H., Spanyi, A., 2019. What Process Mining Is, and Why Companies Should Do It. Retrieved from. In: https://hbr.org/2019/04/what-process-mining-isand-why-companies-should-do-it.

Dehning, B., Richardson, V.J., 2002. Returns on Investments in Information Technology: A Research Synthesis. Journal of Information Systems 16 (1), 7–30

Dervin, B., Foreman-Wernet, L., 2012. Sense-Making Methodology as an Approach to Understanding and Designing for Campaign Audiences. In: Rice, R.E., Atkin, C.K. (Eds.), Public Communication Campaignes. Sage Publications, pp. 147–162.

Du, W.D., Pan, S.L., Leidner, D.E., Ying, W., 2019. Affordances, experimentation and actualization of FinTech: A blockchain implementation study. The Journal of Strategic Information Systems 28 (1). 50–65

Dumas, M., La Rosa, M., Mendling, J., Reijers, H.A., 2018. Fundamentals of Business Process Management, 2nd Ed. Springer, Heidelberg.

Transparency to Achieve Increased Process Awareness”. Business and Information Systems Engineering.

Eisenhardt. K.M., 1989. Building theories from case study research. The Academy of Management Review 14 (4). 532–550.

Eisenhardt, K.M., Graebner, M.E., 2007. Theory building from cases: Opportunities and challenges. Academy of Management Journal 50 (1), 25–32.

performance. International Journal of Accounting Information Systems 9 (3), 135–153.

Eric Zheng, Z., Fader, P., Padmanabhan, B., 2012. From business intelligence to competitive intelligence: Inferring competitive measures using augmented site-centric data. Information Systems Research 23 (3-part-1), 698–720.

Essén, A.. Värlander, S.W., 2019. How technology-afforded practices at the micro-level can generate change at the field level: Theorizing the recursive mechanism actualized in swedish rheumatology 2000–2014. MIS Ouarterly 43 (4), 1155–1176.

Everest Group, 2020. Process Mining Market More Than Doubles in Revenue and Client Base in 2019. Retrieved from. https://www.everestgrp.com/2020-07-process mining-market-more-than-doubles-in-revenue-and-client-base-in-2019everest-group-press-release-.html.

Faraj, S., Azad, B., 2012. The Materiality of Technology: An Affordance Perspective. In: Leonardi, P.M., Nardi, B.A., Kallinikos, J. (Eds.), Materiality and Organizing. Oxford University Press, Oxford, pp. 237–258.

Galetsi. P.. Katsaliaki. K.. Kumar, S., 2020. Big data analytics in health sector: Theoretical framework, techniques and prospects. International Journal of Information Management 50 (March 2019). 206–216.

Gibson, J.J., 1977. The Concept of Affordances. In: Bransford, J. (Ed.). Perceiving, Acting and Knowing. Lawrence Erlbaum, Hillsdale, NJ

Gibson, JJ., 1986. The Ecological Approach to Visual Perception. Lawrence Erlbaum Associates. Hillsdale, NJ.

Goh, J. M., G. (Gordon) Gao and R. Agarwal. (2011). “Evolving Work Routines: Adaptive Routinization of Information Technology in Healthcare.” Information Systems Research, 22(3), 565–585.

Grigori, D., Casati, F., Castellanos, M., Dayal, U., Sayal, M., Shan, M.C., 2004. Business Process Intelligence. Computers in Industry 53 (3), 321–343.

Grisold. T., B. Wurm, J. Mendling and J. vom Brocke. (2020). “Using Process Mining to Support Theorizing About Change in Organizations." In: 53rd Hawaiian International Conference on System Sciences (HICSS 2020).

(2), 369–387.

Grover, V., Chiang, R.H.L., Liang, T.P., Zhang, D., 2018. Creating Strategic Business Value from Big Data Analytics: A Research Framework. Journal of Management

Hofmann, P., Samp, C., Urbach, N., 2020. Robotic Process Automation. Electronic Markets 30, 99–106.

Huising, R., 2019. Moving off the Map: How Knowledge of Organizational Operations Empowers and Alienates. Organization Science 30 (5), 1054–1075.

Jans, M. and P. Soffer. (2017). “From relational database to event log: decisions with quality impact.” In: International Conference on Business Process Management (pp. 588–599). Springer, Cham.

Karahanna, E., S. X. Xu, Y. Xu and N. (Andy) Zhang. (2018). “The needs-affordances-features perspective for the use of social media.” MIS Quarterly, 42(3), 737–756.

Keller, R., A. Stohr, G. Fridgen, J. Lockl and A. Rieger. (2019). “Affordance-Experimentation-Actualization Theory in Artificial Intelligence Research – A Predictive Maintenance Story." In: Fortieth International Conference on Information Systems (Munich 2019).

Kerremans, M., 2019. Market Guide for Process Mining. Retrieved from. https://www.gartner.com/en/documents/3939836/market-guide-for-process-mining Kerremans, M., Samantha, S., Tushar, S., Kimihiko, I., 2020. 2020. Gartner Inc, Market guide for process mining.

Lavrakas, P.J., 2008. Encyclopedia of survey research methods. Sage publications.

Veit, F., Geyer-Klingeberg, J., Madrzak, J., Haug, M., Thomson, J., 2017. The proactive insights engine: Process mining meets machine learning and artificial intelligence. CEUR Workshop Proceedings 1920 (July).

Lehrer, C., Wieneke, A., vom Brocke, J., Jung, R., Seidel, S., 2018. How Big Data Analytics Enables Service Innovation: Materiality, Affordance, and the Individualization of Service. Journal of Management Information Systems 35 (2), 424–460.

Leidner, D.E., Gonzalez, E., Koch, H., 2018. Affordance perspective of enterprise social media and organizational socialization. Journal of Strategic Information Systems 27 (2), 117–138.

Leonardi, P.M., 2013. When Does Technology Use Enable Network Change in Organizations? A Comparative Study of Feature Use and Shared Affordances. MIS Quarterly 37 (3), 749–775.

Leonardi, P.M., Barley, S.R., 2008. Materiality and change: Challenges to building better theory about technology and organizing. Information and. Organization

Leonardi, P.M., Treem, J.W., 2020. Behavioral Visibility: A new paradigm for organization studies in the age of digitization, digitalization, and datafication. Organization Studies 41 (12), 1601–1625.

Leonardi, P.M., Bailey, D.E., Pierce, C.S., 2019. The Coevolution of Objects and Boundaries over Time: Materiality, Affordances, and Boundary Salience. Information Systems Research 30 (2), 665–686.

Leonardi, P.M., Vaast, E., 2017. Social Media and Their Affordances for Organizing: A Review and Agenda for Research. The Academy of Management Annals 11 (1), 150-188.

Lozada, N., Arias-P´erez, J., Perdomo-Charry, G., 2019. Big data analytics capability and co-innovation: An empirical study. Heliyon 5 (10).

Mans, R., R. Hajo, B. Hans, B. Wasana and P. Rogier. (2013). “Business Process Mining Success.” In: Proceedings of the 21st European Conference on Information Systems (ECIS 2013).

Markus, M.L., Rowe, F., 2018. Is IT Changing the World? Conceptions of Causality for Information Systems Theorizing. MIS Quarterly 42 (4), 1255–1280.

Martin, N., D. A. Fischer, G. Kerpedzhiev, K. Goel, M. Leemans, Sander Roglinger, ¨ M. van der Aalst, Wil M. P. Dumas, … M. T. Wynn. (2021). “Opportunities and Challenges for Process Mining in Organisations : Results of a Delphi Study.” Business & Information Systems Engineering.

Mehdiyev, N., Evermann, J., Fettke, P., 2020. A novel business process prediction model using a deep learning method. Business & Information Systems Engineering 62 (2), 143–157.

Melville. N., Kraemer, K., Gurbaxani, V., 2019. Review: Information Technology and Organizational Performance: An Integrative Model of. MIS Ouarterly 28 (2). 283–322.

Müller, O., Fay, M., vom Brocke, J., 2018. The Effect of Big Data and Analytics on Firm Performance: An Econometric Analysis Considering Industry Characteristics. Journal of Management Information Systems 35 (2), 488–509.

Nan, N., Lu, Y., 2014. Harnessing the Power of Self-Organization in an Online Community During Organizational Crisis. MIS Quarterly 38 (4), 1135–1158.

Nelson, R.R., Winter, S.G., 1982. An evolutionary theory of economic change (Cambridge). Harvard University Press.

Okoye, K., Islam, S., Naeem, U., Sharif, M.S., Azam, M.A., Karami, A., 2018. The Application of a Semantic-Based Process Mining Framework on a Learning Process Domain. In: In: Proceedings of SAI Intelligent Systems Conference, pp. 1381–1403.

Olszak, C.M., 2016. Toward Better Understanding and Use of Business Intelligence in Organizations. Information Systems Management 33 (2), 105–123.

Par´e, G., 2004. Investigating Information Systems with Positivist Case Research. Communications of the Association for Information Systems 13, 233–264.

Pentland, A., 2014. Social physics: How good ideas spread-the lessons from a new science. Penguin.

Polato, M., Sperduti, A., Burattin, A., de Leoni, M., 2016. Time and Activity Sequence Prediction of Business Process Instances. Computing 100 (9), 1005–1031

Reinkemeyer, L., P. Grindemann, V. Egli, M. Roglinger, ¨ L. Marcus and L. Fabri. (2022). Accelerating Business Transformation with Process Mining Centers of Excellence (CoEs).

Reinkemeyer, L. (2020). Process Mining in Action: Principles, Use Cases and Outlook.

Sahay, B.S., Ranjan, J., 2008. Real time business intelligence in supply chain analytics. Information Management and Computer Security 16 (1), 28–48.

Sap, 2021. SAP to Acquire Business Process Intelligence Company Signavio. Retrieved from. https://news.sap.com/2021/01/sap-to-acquire-signavio/.

Sarker, S., Chatterjee, S., Xiao, X., Elbanna, A., 2019. The sociotechnical axis of cohesion for the IS discipline: Its historical legacy and its continued relevance. MIS Quarterly 43 (3), 695–719.

Seddon. P.B., Constantinidis. D., Tamm. T.. Dod. H., 2017. How does business analytics contribute to business value? Information Systems Journal 27 (3). 237–269.

Seddon, P. B., D. Constantinidis and H. Dod. (2012). “How Does Business Analytics Contribute to Business Value.” Proceedings of the Thirty-Third Internationa Conference on Information Systems (ICIS 2012), 1–17.

Seidel. S., Recker, J., vom Brocke, J., 2013. Sensemaking and Sustainable Practicing: Functional Affordances of Information Systems in Green Transformations. MIS Quarterly 37 (4), 1275–1299.

Sharma, R., Mithas, S., Kankanhalli, A., 2014. Transforming decision-making processes: A research agenda for understanding the impact of business analytics on organisations. European Journal of Information Systems 23 (4), 433–441.

Shollo, A., Galliers, R.D., 2016. Towards an understanding of the role of business intelligence systems in organisational knowing. Information Systems Journal 26 (4), 339–367.

Strauss, A., Corbin, J., 1998. Basics of Oualitative Research Techniques. Sage publications, Thousand Oaks, CA.

Strong, D.M., Volkoff, O., Johnson, S.A., Pelletier, L.R., 2014. A Theory of Organization-EHR Affordance Actualization. Journal of the Association for Information Systems 15 (2), 53–85.

Subramani, M., 2004. How Do Suppliers Benefit from Information Technology Use in Supply Chain Relationships? MIS Ouarterly 28 (1), 45–73

Suriadi. S., Andrews. R., ter Hofstede. A.H., Wynn. M., 2017. Event log imperfection patterns for process mining: Towards a systematic approach to cleaning event logs. Information Systems 132–150.

Management Information Systems 16 (4), 145–173.

Systems, Man and Cybernetics Part C: Applications and Reviews 38 (6), 745–756.

Terragni, A. and M. Hassani. (2018). “Analyzing Customer Journey with Process Mining: From Discovery to Recommendations.” In: 2018 IEEE 6th International Conference on Future Internet of Things and Cloud (FiCloud) (pp. 224–229).

Trieu, V.-H., 2017. Getting value from Business Intelligence systems: A review and research agenda. Decision Support Systems 93, 111–124.

van der Aalst, W.M.P., 2011. Using process mining to bridge the gap between BI and BPM. IEEE Computer 44 (12), 77–80

van der Aalst, W.M.P., 2016. Process mining: Data Science in Action. Data Science, Process Mining in Action.

van der Aalst, W.M.P., Zhao, J.L., Wang, H.J., 2015. Business Process Intelligence: Connecting Data and Processes. ACM Transactions on Management Information Systems 5 (4), 1–7.

van der Aalst, W.M.P., Bichler, M., Heinzl, A., 2018. Robotic Process Automation. Business and Information Systems Engineering 60 (4), 269–272.

Volkoff, O., Strong, D.M., 2013. Critical realism and affordances: Theorizing It-associated organizational change. MIS Quarterly 37 (3), 819–834.

vom Brocke, J., Jans, M., Mendling, J., Reijers, H.A., 2021. A Five-Level Framework for Research on Process Mining. Business and Information Systems Engineering.

Yeshchenko, A., Di Ciccio, C., Mendling, J., Polyvyanyy, A., 2021. Visual Drift Detection for Event Sequence Data of Business Processes. IEEE Transactions on Visualization and Computer Graphics.

Yoo, Y., Boland, R.J., Lyytinen, K., Majchrzak, A., 2012. Organizing for Innovation in the Digitized World. Organization Science 23 (5), 1398–1408.

Zammuto, R.F., Griffith, T.L., Majchrzak, A., Faraj, S., Dougherty, D.J., 2007. Information Technology and the Changing Fabric of Organization. Organization Science 18 (5), 749–762.

Zhang, Y., Li, B., Krishnan, R., 2020. Learning individual behavior using sensor data: The case of global positioning system traces and taxi drivers. Information Systems Research 31 (4), 1301–1321.
