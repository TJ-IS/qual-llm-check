---
otero_id: 16785
otero_key: "USNQVUBG"
title: "Strategic alignment of enterprise architecture management – how portfolios of control mechanisms track a decade of enterprise transformation at Commerzbank"
authors: "Jannis Beese; Kazem Haki; Raphael Schilling; Martin Kraus; Stephan Aier; Robert Winter"
year: "2023"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2022.2085200"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/USNQVUBG/fulltext/images/2264e44ddf605f2f0dfe6467fddc00099ed3e9514e03cddc0813c1e0ca2f1e35.jpg)

# Strategic alignment of enterprise architecture management – how portfolios of control mechanisms track a decade of enterprise transformation at Commerzbank

Jannis Beese, Kazem Haki, Raphael Schilling, Martin Kraus, Stephan Aier, Robert Winter & (Outgoing Editor)

To cite this article: Jannis Beese, Kazem Haki, Raphael Schilling, Martin Kraus, Stephan Aier, Robert Winter & (Outgoing Editor) (2022): Strategic alignment of enterprise architecture management – how portfolios of control mechanisms track a decade of enterprise transformation at Commerzbank, European Journal of Information Systems, DOI: 10.1080/0960085X.2022.2085200

To link to this article: https://doi.org/10.1080/0960085X.2022.2085200

![](/api/attachments/USNQVUBG/fulltext/images/feacb0429256e84aa344f41c2a4a8222f56d46d7e78e8882fa86f492cc3bd5ae.jpg)

© 2022 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group.

![](/api/attachments/USNQVUBG/fulltext/images/1695ccb1c6acf7c0e57e7d3089a03b9723d6e4b30297f72e67880af74aa9eaa5.jpg)

Submit your article to this journal

![](/api/attachments/USNQVUBG/fulltext/images/20ac0a926ad3ad031efdb733c0e3a304c9884648b311c7c18f5fdab58e720db7.jpg)

View related articles

![](/api/attachments/USNQVUBG/fulltext/images/78685899e79da2410889ab4919de218580e444b1782ee2affe990ca169ccf201.jpg)

Published online: 08 Jul 2022.

Article views: 808

![](/api/attachments/USNQVUBG/fulltext/images/6b99ee88713530c661a50d81d38fa8e6140700d35e29f7da77eaa78528ec710b.jpg)

View Crossmark data

EMPIRICAL RESEARCH

∂ OPEN ACCESS

Check for updates

# Strategic alignment of enterprise architecture management – how portfolios of control mechanisms track a decade of enterprise transformation at Commerzbank

Jannis Beese<sup>a</sup>, Kazem Haki <sup>a,b</sup>, Raphael Schilling<sup>c</sup>, Martin Kraus<sup>d</sup>, Stephan Aier<sup>a</sup>, Robert Winter<sup>a</sup> (Outgoing Editor)

<sup>a</sup>Institute of Information Management, University of St Gallen, St Gallen, Switzerland; <sup>b</sup> Geneva School of Business Administration (HES-SO, HEG Genève); <sup>c</sup>Migros-Genossenschafts-Bund, Zurich, Switzerland; <sup>d</sup>Commerzbank AG, Frankfurt am Main, German

## ABSTRACT

Enterprise architecture management (EAM) is commonly employed by large organisations to coordinate local information system development eforts in line with organisation-wide strategic objectives while simultaneously avoiding redundancies and inconsistencies. Even though EAM tools and processes have become increasingly mature over the past decade, many organisations still struggle to generate impact from their EAM initiatives. To this end, we describe how enterprise architects at Commerzbank, a major international bank, employed a control mechanism portfolio perspective to more efectively anchor EAM within the organisation. This approach allows to purposefully combine a wide range of diferent formal and informal EAM control mechanisms, thereby going beyond the formal, top-down driven mechanisms predominantly discussed in EAM literature. Furthermore, such EAM control mechanism portfolios provide an efective means to purposefully realign EAM in reaction to major strategic shifts. The application of this perspective is demonstrated by tracing the evolution of EAM at Commerzbank for more than a decade (2008 to 2018) through a turbulent and challenging competitive environment, resulting in several major strategic realignments that required corresponding adjustments in EAM. We believe that such consciously designed and diversified EAM control mechanism portfolios also provide a useful means for other large organisations to more efectively conduct EAM.

ARTICLE HISTORY Received 15 September 2020 Accepted 24 May 2022

KEYWORDS Enterprise architecture management; control theory; control mechanism portfolio; episodic change

## 1. Introduction

Modern organisations extensively rely on interconnected information systems (IS) to support their core business processes. Continuously changing competitive environments and business requirements necessitate the development of new IS as well as frequent changes to existing systems. While such adaptations are inevitable, they also have the potential to create conflicts among involved stakeholders with diverging perspectives on IS development (M. K. Haki et al., 2016). Local business entities, such as project teams, tend to advocate for specialised IS solutions that fit their specific needs and individual preferences. In contrast, global business entities, such as strategic initiatives, aim to improve the overall eficiency and efectiveness of the entire set of IS in the organisation from an overarching, organisation-wide perspective (Malaurent & Avison, 2016).

Enterprise Architecture Management (EAM) addresses these conflicts by trying to align local and global perspectives on IS development (Boh & Yellin, 2006; Richardson et al., 1990; Zachman, 1987). Enterprise

Architecture (EA) thereby refers to the actual and envisioned IS architecture of an organisation, covering all IS components as well any interdependencies (ISO/IEC/ IEEE, 2011). EAM, in turn, encompasses all related processes, methods, and tools that are used to design and purposefully guide the evolution of EA (K. Haki et al., 2020; Simon et al., 2013). Notwithstanding significant advances in these areas – including established and comprehensive EAM frameworks (e.g., The Open Group, 2018) – and despite considerable eforts in organisations to adopt and implement EAM, many EAM initiatives still fail (Löhe & Legner, 2014) and organisations are witnessing rising levels of IS complexity in their EA (Beese et al., 2016; Mocker, 2009). Consequently, there still is a need to better understand how EAM can be efectively conducted in large organisations.

To this end, we provide a first-hand report and reflection on the development of EAM at Commerzbank, a large European financial service provider, from 2008 to 2018. During this period, Commerzbank was facing a turbulent and challenging competitive environment – including the 2008 financial crisis, the takeover of a major competitor, and multiple technological reorientations – resulting in four major strategic realignments that necessitated corresponding adjustments in EAM. Thus, we can observe multiple diferent approaches to EAM within the same organisation at diferent points in time. These shifts, often driven by a perceived inadequacy of established EAM practices in novel circumstances, highlight the need for a situated and more nuanced approach to EAM that adequately reflects the emerged organisational context, thereby going beyond simple best-practices.

In order to generalise the insights gained within Commerzbank, we suggest to conceptualise EAM as a control function that aims to align local IS development projects with global organisation-wide objectives (Cram et al., 2016b). Control thereby refers to a dyadic process, in which a controller tries to regulate or adjust the behaviour of a controlee (Choudhury & Sabherwal, 2003). Since the efectiveness of control mechanisms depends on the specific circumstances under which they are employed, successful EAM requires to use various control mechanisms – potentially in combination – which need to be adapted to accommodate changes in the organisational context (Kirsch, 1997). From this perspective, EAM can therefore be construed as a situated portfolio of control mechanisms, i.e., a context-dependent set of means to align individual behaviour with organisation-wide objectives.

Our analysis of Commerzbank’s EAM journey emphasises the need for organisations to frequently review and revise the control mechanism portfolio employed by their EAM to be aligned with a continuously changing context. Accordingly, we propose a situated approach to EAM that constantly re-evaluates EAM structures and activities according to evolving opportunities and constraints (Feldman et al., 2016). The proposed EAM control mechanism portfolio perspective thereby ofers a broader understanding of control and its underlying mechanisms, allowing organisations to draw upon a wide range of diferent control mechanisms. Our findings further suggest that, depending on the given situation and the current organisational culture, diferent types of control mechanisms can be emphasised, but the overall EAM control mechanism portfolio should be balanced and aligned with the organisation’s strategic initiatives and with the priorities of the top management.

In the following, we first introduce the key concepts of EAM and control theory, then present our case analysis and results, and finally conclude with a discussion of the key findings.

## 2. Enterprise architecture management and control theory

Over the last decade, major changes in customer behaviour (e.g., the ubiquity of online banking) along with significant technological (e.g., big data and machine learning) and regulatory advances, require that financial service providers, such as Commerzbank, continuously adapt their IS to fit new requirements. A key challenge in such a turbulent environment is to guide the development of the overall IS architecture towards organisation-wide objectives (K. Haki et al., 2020; Vessey & Ward, 2013). EAM aims to address this challenge by building on a long tradition of established frameworks (Scheer & Schneider, 2005; The Open Group, 2018; Zachman, 1987) and related tools (e.g., Jonkers et al., 2006; Ross, 2006), allowing to analyse IS development from an architectural perspective that considers all relevant entities within the organisation as well as their interrelations.

After gaining traction both in research and practice during the early 2000s (Ross et al., 2006), EAM frameworks (e.g., The Open Group, 2017) have reached mature stages and are now commonly employed by large organisations (Rahimi et al., 2017), which rely on comprehensive modelling languages (Lankhorst et al., 2004) and related methods (Robert et al., 2019). A survey conducted in 2011 (i.e., towards the beginning of our engagement with Commerzbank) by Ross and Quaadgras (2012) already reports that most organisations have reached a high level of EAM maturity, supporting the development of increasingly robust technology and process platforms. However, Ross and Quaadgras (2012) also highlight that high levels of EAM maturity do not correlate with the achievement of corresponding business objectives in their study. They argue, essentially, that EAM might become more mature and formalised without generating a valuable impact within an organisation (Ross & Quaadgras, 2012).

This observation sparked a number of subsequent investigations on how to more efectively, in terms of impact, control IS development from an overarching perspective (K. Haki et al., 2020; Winter, 2014), which also motivated our prolonged engagement within Commerzbank. One hypothesis is that the limited impact of EAM might be due to a too narrow focus on top-down formalised modes of control to spread EAM within an organisation (Brown & Grant, 2005; K. Haki et al., 2020; Schilling et al., 2019). For example, enterprise architects usually aim to develop a future target architecture by contrasting the current state of IS in the organisation with the organisation’s strategy and future business objectives (Boh & Yellin, 2006). Such a target architecture is then often propagated and enforced throughout the organisation in a straightforward, centralised, top-down manner (Boh & Yellin, 2006). In this case, however, the actors in local project teams tend to perceive EAM primarily as an unwelcome restriction of their individual design freedom, which might lead to low levels of acceptance and impact (Brosius & Aier, 2016). Consequently, approaches to EAM that are solely grounded in a centralised and deterministic understanding of control may not be entirely suitable to manage complex socio-technical systems, such as large organisations that are manoeuvring through turbulent changes in their organisational environment (Ciborra et al., 2000).

## 2.1. Control theory

In the following, we introduce several concepts from control theory that originate from general sociology (e.g., Nye, 1958), but have since been frequently applied in management research (e.g., Tannenbaum, 2019) and more recently in studies of IS development (e.g., Wiener et al., 2016). In line with Cram et al. (2016b) and Wiener et al. (2016), we argue that – similar to their investigations of IS development eforts – control theory ofers a practical way to better understand how and why diferent control mechanisms function more or less efectively in EAM in large organisations. Consequently, the general ideas introduced in the following – in particular, diferent modes of control and control mechanism portfolios (Kirsch, 1997; Wiener et al., 2016) – enable us to take a more comprehensive perspective in our subsequent analysis of Commerzbank’s EAM journey. Furthermore, these concepts also gained traction within Commerzbank during our prolonged engagement (see Appendix A for the details) and were adopted by the EAM team to critically reflect and purposefully adapt the prevalent EAM approaches in the organisation over time.

Central to our application of control theory to EAM is the diferentiation between diferent formal and informal modes of control (Kirsch, 1997; Ouchi, 1979). Formal modes of control are characterised by the existence of some sort of explicit performance evaluation and incentive system (Eisenhardt, 1985). In contrast, informal modes of control are grounded in a person’s intrinsic motivation and in interpersonal interactions, relying on the self-regulation dynamics that implicitly govern the behaviour of people within their social context. Control theory typically distinguishes between three diferent formal modes of control (input control, behaviour control, and outcome control) and two informal modes of control (self-control and clan control; Choudhury & Sabherwal, 2003; Kirsch, 1997; Wiener et al., 2016). Related literature not only describes how these different modes of control operate, but also provides general situational considerations of contextual factors that are expected to impact the eficacy of a given mode of control (see, Table 1 for an overview).

Regarding the formal modes of control, input control refers to control that is enacted by the controller (such as high-level managers) through the allocation of resources to the controlee (such as employees in an IS development project) and by monitoring to which extent the controlee utilises the allotted resources (Wiener et al., 2016). This includes human, financial, and material resources, as well as related organisational structures and processes (e.g., recruitment criteria and access to trainings). Efectively exerting input control thus depends on the existence of limited yet desirable resources – which ideally are related to the targeted outcomes – and on appropriate organisational structures to manage and supervise this allocation.

Table 1. Classification of control mechanisms in control theory.

<table><tr><td>Control mechanism</td><td>Description and operation</td><td>Situational considerations</td></tr><tr><td colspan="3">Formal modes of control</td></tr><tr><td>Input control (IC)</td><td>Control through allocatingHuman resources,Financial resources,Material resources andCorresponding organisational arrangements.</td><td>Resources must be limited, desirable and ideally related to the targeted goals.Appropriate structures to allocate resources are required.</td></tr><tr><td>Behaviour control (BC)</td><td>Control through establishingProcesses that govern individual actions,Rules to guide individual actions,Mechanisms to observe compliance andReward systems for compliance.</td><td>Incentives to reward compliance are necessary.Appropriate behaviours must be known and observable.</td></tr><tr><td>Outcome control (OC)</td><td>Control through establishingSpecific desired outcomes andProcesses to measure and promote outcomes.</td><td>Outcomes must be measurable and in line with objectives.Incentives to reward compliance are necessary.</td></tr><tr><td colspan="3">Informal modes of control</td></tr><tr><td>Clan control (CC)</td><td>Control through the institution ofShared norms, values, and beliefs,Reflective activities, andStrong interpersonal social ties.</td><td>Effects may be delayed and only arise over time.Works even without clear target outcomes and processes.</td></tr><tr><td>Self-control (SC)</td><td>Control through fostering individuals’Intrinsic motivation andPersonal standards.</td><td>Employees must feel autonomous in their work.Difficult to influence directly.</td></tr></table>

In behaviour control the controller monitors and rewards (or sanctions) the extent to which the controlee follows defined rules, procedures, and processes (e.g., architecture principles or development methodologies). Related organisational processes include regular status meetings and reports (Cram et al., 2016b; Wiener et al., 2016). In order to efectively enact behaviour control, appropriate behaviours must both be known and observable, which may be dificult in situations where the controller only has a limited capacity to oversee the actual execution of tasks (Kirsch, 1997). Furthermore, corresponding incentive structures to reward compliance (or punish noncompliance) are required (Wiener et al., 2016).

A controller exerts output control by defining and evaluating interim or final outputs (e.g., project milestones or design documents) that the controlee needs to deliver and by monitoring the extent to which these outputs are achieved (Wiener et al., 2016). Efective enactment of output control requires a set of measurable outputs that accurately represent the targeted objectives as well as corresponding incentive structures to reward compliance (Wiener et al., 2016).

Regarding the informal modes of control, clan control refers to behavioural changes of the controlee due to shared norms and values within a peer group (e.g., a shared architectural vision and related goals). Controllers, who are often outside the peer group, can promote and reinforce desired behaviour through specific ceremonies and rituals (e.g., by publicly praising/criticising observed actions) as well as by strengthening social ties through activities (e.g., team events) and organisational structures (e.g., allowing for breakroom discussions and activities; Kirsch, 1997). Clan control thus represents a more indirect approach, requiring to carefully introduce norms, values, and beliefs into a social peer group over time, but works even in situations where clear targets and related activities are not yet known (Cram et al., 2016b; Kirsch, 1997).

Finally, self-control concerns the intrinsic motivation of individuals to achieve personal goals and adhere to their own standards (such as senior architects, who continuously strive to redefine and improve existing processes). Consequently, efective use of selfcontrol requires that individuals feel empowered and encouraged to autonomously work towards their goals (Kirsch, 1997).

## 2.2. Evolution of an EAM control mechanism portfolio over time

Building on the preceding discussion of diferent types of control mechanisms, we use the term EAM control mechanism portfolio to refer to a situated combination of any number of such control mechanisms. The portfolio concept is intended to imply that the overall efectiveness of all employed control mechanisms depends on the portfolio’s internal consistency and on whether the control mechanisms are both appropriate for the given context and in line with organisational objectives (Busby & Collins,

2014; Haki et al., 2016). Consequently, changing circumstances and objectives require organisations to be in a continuously ongoing process of reevaluating and adjusting their portfolio in response (Cardinal et al., 2004; Cram et al., 2016a; Wiener et al., 2016). From this perspective, EAM activities can be conceptualised as an ongoing organisational process that guides a dynamic reconfiguration of EAM control mechanism portfolios (i.e., purposefully altering the overall setup of control mechanisms related to EAM in an organisation in a particular way), which may include diferent control mechanisms relating to diferent modes of control at diferent points in time.

In our analysis, we distinguish three distinct episodes at Commerzbank, referring to periods of relative stability that are separated by “episodic changes”. Such episodic changes are infrequent, discontinuous, and intentional changes to the overall organisation, which simultaneously impact a significant number of components (e.g., business processes, organisational structures, and information systems) in fundamental ways (Pettigrew et al., 2001; Weick & Quinn, 1999). While we acknowledge the importance of understanding the ongoing, evolving, and cumulative changes to the EAM control mechanism portfolios within the individual episodes in more detail, we deliberately focus our investigation on the adjustments that are made during episodic changes. Lacking a solid literature base that investigates EAM from a control mechanism portfolio perspective, the major reconfigurations that happen during episodic changes provide a promising starting point to not only describe changes in EAM control mechanism portfolios over time, but also understand how and why these changes were made.

In line with extant literature on organisational change, we find episodic changes to be driven by major environmental jolts (such as the 2008 financial crisis) or series of cumulative changes, which in turn lead to an overall major misalignment between the organisation and external requirements (Pettigrew et al., 2001). In response, the overall strategy of the organisation shifts, which leads to significant changes in diverse areas, such as organisational structures, established practices, and the overall workforce as well as senior management. These strategic shifts and the resultant organisational changes then necessitate a re-evaluation and purposeful reconfiguration of the EAM control mechanism portfolios and its constituent control mechanisms, which must be realigned with the overall strategy and adapted to fit the emerged organisational context. This leads to fundamental changes for all control mechanism types between episodes (IC1 → IC2 → IC3, . . .; see, Figure 1).

![](/api/attachments/USNQVUBG/fulltext/images/a732bdbdc6c91cc19b54bb932cf286a2dc69b7105781d8ef780d1158195da4bd.jpg)  
Figure 1. EAM as a dynamic reconfiguration of control mechanism portfolios.

## 3. Case description and method

Commerzbank AG is a major international bank headquartered in Frankfurt, Germany, and operating in more than 50 countries worldwide. In 2019, towards the end of our data collection, Commerzbank comprised 48ʹ512 employees who managed approximately 463.6 billion € in assets and generated an operating profit of 1.25 billion € (Commerzbank, 2020). Over the last decade, Commerzbank – and the financial services industry in general – experienced fundamental changes in terms of customer behaviour, market structure, and regulation. As a result, Commerzbank went through several fundamental organisational restructurings and considerable changes in its business and technology strategy over the last decade. This encouraged us to share our experience at Commerzbank, since the digital strategy of Commerzbank – and consequently the portfolio of EAM control mechanisms – went through significant changes over time. Throughout this process, we managed to dynamically readjust the portfolio of EAM control mechanisms to efectively achieve desired EAM outcomes in very diferent circumstances, which could be of interest for other large organisations.

This research paper is the result of a long-lasting collaboration between Commerzbank’s EAM team and a research group (see Appendix A). Starting with first discussions in 2008, this collaboration intensified in 2011, when we began to discuss diferent ways to better anchor EAM within the overall organisation in two tri-annual competence centres and through additional related workshops, exchanges of best practices, joint participation at conferences, and training sessions. When reviewing the evolution of the EAM function within Commerzbank over time, we noticed that the EAM control mechanism portfolio concept (including the diferent types of control mechanisms)

was increasingly perceived to be helpful to guide EAM activities in reaction to changing circumstances. For example, the EAM control mechanism portfolio concept was adopted by Commerzbank’s EAM team in meetings and presentations to review EAM activities and plan future changes. Consequently, in 2017, we set out together to gather rich qualitative data that allows us to retrace and explain shifts in the organisational context and corresponding changes to the EAM control mechanism portfolio over time (Pettigrew, 1992). The methodological details of our approach, including the interview process as well as the coding and analysis procedures, are described in Appendix B. An overview of the overall process is provided in Figure 2.

In this process, we could on the one hand build on data created and collected through our direct collaboration. This comprises, for example, a total of 218 sets of notes, presentations, and workshop results from regular competence centre meetings between 2011 and 2018 along with notes from irregular meetings between senior researchers and senior executives, joint contributions to conferences, and strategy and alignment documents that were shared during ongoing discussions within our group. Furthermore, we collected all publicly available shareholder communication between 2011 and 2018, including all annual reports and additional communication, e.g., in reaction to major takeovers or the financial crisis. All documents were initially collected, grouped by type, put into chronological order and then manually reviewed by the author team.

Building on this vast set of data, we wanted to complement our own impressions with an external perspective of additional stakeholders outside of the EAM department at Commerzbank, ensuring to capture the view of both IT and business functions within the overall organisation. This led to an additional tranche of data collection that took place between

![](/api/attachments/USNQVUBG/fulltext/images/6596e36baa71fda51a7ee2429d5cdc29ce948b356611a75c3a9692a82e349f34.jpg)  
Figure 2. Overview of data collection and analysis process (also see, Table 3 in Appendix A).

July and October 2017, comprising a set of ten semistructured interviews with multiple stakeholders from both business and IT and on diferent hierarchical levels (top management and operational levels). Questions were aimed at discovering major turning points that led to adjustments in the EAM approach and the portfolio of control mechanisms as well as discovering misalignments between the perspectives of diferent EAM stakeholders, which are likely to trigger readjustment processes. Furthermore, we were interested in discovering diferent formal and informal modes of control as well as identifying measures of success, as indicators of the efectiveness of control mechanisms.

The obtained interview data was iteratively coded (starting with codes for the diferent types of control mechanisms derived from literature), structured, and mapped against the timeline from 2008–2018. We then went back to our original data and triangulated the coded interviews with the information obtained through our direct collaboration as well as the publicly available shareholder communications. In combination, the rich data collected during our prolonged engagement with Commerzbank’s EAM department and the external interview data from other stakeholders within the organisation allows us to accurately trace and explain the complex organisational dynamics (Pettigrew, 1997; Vom Brocke et al., 2021) that commonly underly the development of EAM in large organisations.

Following a dynamic (vs. static) perspective and to systematically analyse the evolution of EAM at Commerzbank, we relied on process theory, which is frequently employed to examine how organisational phenomena emerge over time (Markus & Robey, 1988; Mohr, 1982; Pettigrew, 1997; Van de Ven & Huber, 1990). Process studies analyse three main components, namely antecedents, turningpoint episodes, and outcomes. Antecedents, which trigger a turning-point episode, consist of external (e.g., business ecosystem, technological) and internal (e.g., organisational culture) contextual factors.

In turn, outcomes are the results of each turningpoint episode. As such, a process represents a sequence of collective episodes unfolding over time (Pettigrew, 1997). In the context of our inquiry at Commerzbank, each episode corresponds to a major change in Commerzbank’s approach to EAM. Therefore, next to the constituent constructs of control theory (Table 1), we included the constructs of process theory in a coding scheme that helped us analyse (1) the chain of events that collectively brought about the most recent EAM control mechanism portfolio, (2) the antecedents that brought about the emergence of various EAM control mechanism portfolios over time, and (3) the outcomes of establishing various EAM control mechanism portfolios over time.

## 4. Evolution of the EAM control mechanism portfolio at Commerzbank

The EAM control mechanism portfolio concept was used both to proactively develop EAM within Commerzbank and to retrospectively describe and evaluate past EAM activities in our analysis. Using this lens, we find that the strategic development of Commerzbank over the last decade can be roughly grouped into three distinct episodes (see, Figure 3). In the following, we use [IC], [BC], . . . to mark observations relating to Input Control, Behavioural Control, etc.

Following process theory, this section presents the major turning-point episodes in the evolution of EAM at Commerzbank along with each episode’s corresponding antecedents, the resultant EAM control mechanism portfolio, and outcomes.

Episode I (2008–2011). Antecedents: Prior to 2008, Commerzbank was operating in a rather stable environment and generating good returns. Local organisational entities experienced a relatively low level of formal control and were comparatively free in making use of their IT budgets. EAM was perceived as an “ivory tower”: While enterprise architects described themselves to be “a central staf function defining the future of the company’s IT architecture”, others perceived EAM to be a “cumbersome” governance function, whose impact was perceived as being limited to the “definition of the Java version that has to be used”.

![](/api/attachments/USNQVUBG/fulltext/images/92c5bc99f8eafb0926cd15f9c27b48299ea813a80a66b1b0e76860fa52d5c08c.jpg)  
Figure 3. Evolution of EAM control mechanism portfolios over time.

Then, towards the end of 2008, the financial crisis hit Commerzbank in full force, causing a drop in the operating profit from 2ʹ513 million € in 2007 to a deficit of 378 million € in 2008 and a deficit of 2ʹ270 million € in 2009 (Commerzbank, 2009a). Furthermore, on August 31<sup>st</sup>, 2008, Commerzbank had announced to acquire Dresdner Bank, a major competitor, and the merger was legally completed in May 2009 (Commerzbank, 2009c).

Resultant EAM control mechanism portfolio: Both events, the financial crisis and the takeover of Dresdner Bank, caused a strategic shift in the organisation with an emphasis on “focus, optimization, downsizing” [OC], which became central in the strategic Roadmap 2012 of Commerzbank (Commerzbank, 2009b). Considering the circumstances (a clear target, but high environmental uncertainty, financial pressures, and scarce resources), rigid resource allocation and control mechanisms [IC] were deemed to be most efective, which could take efect immediately to direct involved stakeholders towards a top-down defined target architecture. Consequently, a new architectural task force was stafed [IC] to develop architectural blueprints for the target landscape [OC], the execution of which was overseen by management [BC] and tracked through implementation roadmaps [BC]. Furthermore, architects were directly assigned to the core modules of the merger project to supervise the integration eforts and to ensure that ongoing activities are in line with the overall architectural vision [BC].

Regarding informal control, there was a tacit agreement between all involved stakeholders in 2008 and 2009 (while the merger was not fully completed, and the financial crisis was still in full force) to mitigate risks as much as possible and to focus on ensuring the stability of the IS [IC]. In this setting, EAM managed to position itself as a welcome enabler of stability in the organisation, who could provide guidance and accountability on the way forward [IC].

Outcomes: Overall, the chosen EAM approach was successful in the sense that the combined Commerzbank/ Dresdner Bank was one of the very few banks that completed a major merger during the financial crisis and managed to get rid of duplicate IS in a comparatively short period of time. This outcome greatly strengthened the perceived value of overarching target architectures and EAM in general at Commerzbank.

Episode II (2012–2016). Antecedents: Following the successful completion of the merger project and the end of the Roadmap 2012 strategy, Commerzbank had once again become profitable at the end of episode I (Commerzbank, 2012a). A strategic shift at Commerzbank regarding EAM was marked by the appointment of a new CIO in 2012, who declared a strong belief in the strategic value of EAM.

Aside from personnel and organisational changes, management in Commerzbank had also noticed a significant backlog of necessary adjustments and updates in their core IT infrastructure, including central components such as customer master data systems and online banking platforms. Consequently, after years of focusing the merger, a need to catch up with deferred investments in the modernisation of the IT platform triggered a series of large strategic transformation projects. The oficial communication at the Commerzbank Investor’s Day in 2012 (Commerzbank, 2012b) highlights both the successful completion of the integration of Dresdner Bank and the efective cost management during the previous years, as well as the new strategic focus on a “strong investment commitment in core infrastructure” that would enable the bank to remain competitive in the future.

Resultant EAM control mechanism portfolio: The newly appointed CIA extended the mandate of the new head of enterprise architecture to include formerly decentrally organised domain architects [IC] in order to ensure clear responsibilities and an increased visibility of EAM in the organisation. Consequently, during this episode, the chief enterprise architect emphasised the architects’ role to build a connection between business and IT sides through intensified networking activities [CC]. Based on initial experiences from new implementation projects, the architecture team concluded that efective guidance could not simply be enforced by just designing blueprints of a future target architecture [OC], but that relevant stakeholders from business and IT need to be actively involved in these architectural discussions [BC]. Initially, it was agreed that project managers must regularly consult with the EAM team [BC], while simultaneously striving for a more active engagement of architects in IT projects [BC] through new allocation processes [IC].

During phase II, projects were actively and voluntarily requesting support from the EAM team [SC] and architectural topics were discussed by a variety of stakeholders [CC]. The increased demand for EAM was further strengthened by a stronger regulatory oversight, which mandated regular quality checks on documentation, project structure, and software development processes for banks [OC], helping to track progress even during the initial discussions without clearly established target pictures.

Architectural discussions were also organisationally anchored in a variety of committees [BC], in which the architects reiterated their message that a better integration of the various IS components in the bank would allow for the creation of new business oferings. This active participation of both business and IT management in the committees ensured a joint discussion process towards commonly supported and agreed architectural target pictures over time [CC].

Outcomes: Experiences from initial projects in combination with the large investments to rebuild Commerzbank’s digital core started to create a significant demand for EAM in the organisation. This is a major shift in the mode of operation of the EAM team, as previously IT project teams often perceived architectural involvement to be either an annoying external restriction of design freedom or, during the merger with Dresdner Bank, a management-mandated imperative. Overall, EAM was perceived to be a major contributor to the successful completion of several major transformation projects that helped to modernise the core IT infrastructure of Commerzbank during phase II.

Episode III (2016–2018). Antecedents: While the eforts to modernise the core IT infrastructure of Commerzbank showed positive results after several major transformation projects were concluded, management was not convinced that the organisation was adequately set up to make full use of the newly acquired technological capabilities. Therefore, in September 2016, Commerzbank publicly announced its new “Commerzbank 4.0” strategy (Commerzbank, 2016), focussing on growth, digital transformation, and increased eficiency to address comparatively low revenue margins. Building on this new strategy, Commerzbank set out to “transform from a financial service provider into a digital technology company”, with the aim to automate all the relevant core processes and focus on the creation of new innovative financial service oferings.

Resultant EAM control mechanism portfolio: Building on the successes of the previous periods, the EAM function was given a priority to support the corresponding technological transformation in all application domains [OC] and a major extension of the EAM headcount was approved [IC], to also counteract the observed capacity shortcomings during the previous period. The new strategy, which also highlighted the importance of architecture for the overall organisation [SC], resulted in non-architects critically reflecting on their role within the bank and on how the overall strategic goal to become a technology company can best be achieved [SC]. Many stakeholders looked for guidance from the EAM team to close this “abstraction gap” [CC]. As part of this process, architects as well as representatives from top management and business experts from several domains were brought together to jointly discuss architectural concepts [CC]. At the same time, architects continued to be involved in major strategic design decisions during the early stages of new IT projects with the responsibility to ensure the fit of the individual solutions with the overall enterprise architecture [BC]. However, despite the overall increased capacity of the architecture team, architects were still lacking time to align and plan among themselves due to the increased demand for general guidance as well as their concrete contributions in projects. Consequently, standardised roles [IC] and formal processes handling, for example, escalations of architectural agreements, were reintroduced over time [IC].

Outcomes: In the wake of rebuilding the core IT infrastructure during the previous years, the wider organisation now showed increased appreciation for

IT, which was perceived more as a business enabler and core capability of a financial services provider at the end of episode III, rather than a mere cost factor. This allowed EAM to not only support infrastructure projects, but also to engage with bottom-up innovation initiatives, which aimed to find creative ways to use new technologies within Commerzbank.

Outlook (since 2018): During 2018 it became clear that delivery of new IT functionality in the current organisational model of Commerzbank was not able to keep up with customer demand for digital services. As a reaction, Commerzbank decided to transform the previous IT department into an agile product-centric organisation with joint business and technical expertise. As a part of this strategic reorganisation, the EAM department was restructured to be part of a new executive area responsible for digital transformation. Consequently, the mode of operation of EAM in Commerzbank is again expected to change considerably, moving architects out of the individual development projects to focus less on direct engagement and more on strategic topics.

Summary: On a high level, the changes in the EAM control mechanism portfolio over time indicate a shift from mostly formal control mechanisms in episode I – when resources are scarce as the overall organisation is navigating through a financial crisis – towards increasingly emphasising informal control during the later episodes, when renewal and innovation considered key outcomes. In the following, we discuss this development on a more general level, arguing first that the specific EAM control mechanism portfolios with diferent emphases are appropriate for the given circumstances in each episode and that organisations in general must adapt their portfolios to newly emerging circumstances. Second, we highlight the importance to have an overall balanced portfolio that, despite allowing for certain emphases, makes use of a variety of formal and informal control mechanisms in the long run.

## 5. Discussion

This article reports on the development of the EAM function at Commerzbank over more than a decade with the aim to explain the dynamic reconfigurations of the employed EAM control mechanism portfolios. Following the journey of EAM at Commerzbank through the 2008 financial crisis and the takeover of Dresdner Bank (episode I, 2008–2011), the development of a new technological core (episode II, 2012 − 2016) and the strategic reorientation towards the Commerzbank 4.0 strategy (episode III, 2016– 2018), we find the EAM control mechanism portfolio to comprise very diferent control mechanisms at different points in time, reflecting a situated response to major strategic shifts (Choudhury & Sabherwal, 2003;

Gregory et al., 2013). The employed modes of control thereby result from considerations of the involved stakeholders on what is most efective in the given context (Wiener et al., 2016). Over time, this context is expected to evolve, most notably during infrequent periods of discontinuous and intentional episodic change (Farjoun, 2010; Weick & Quinn, 1999). Accordingly, we argue that EAM should not be conceptualised as a linear process with clearly defined steps and constant goals. Instead, more attention should be devoted to developing a situated EAM that considers a broad range of control mechanisms to efectively reach a large part of the organisation.

Such a situated approach to EAM essentially considers EAM to be a routinised practice (Feldman & Orlikowski, 2011), i.e., a constantly ongoing reevaluation of EAM structures and activities, which contribute to both stability and change, in line with evol ving opportunities and constraints within the organisation and in the overall environment (Feldman et al., 2016). The proposed EAM control mechanism portfolio perspective thereby ofers a broader understanding of control and its underlying mechanisms, which goes beyond the formal, top-down driven mechanisms predominantly discussed in EAM literature. It allows to deconstruct EAM activities and structures, which typically constitute complex overarching organisational arrangements, into specific instances of general modes of control. This additional level of abstraction then allows to trace the overall development of EAM in the organisation over time through a process approach. Such process-based theory development can provide additional detail (compared to variance-based approaches) on the antecedents and underlying mechanisms of complex change processes, as made evident by our detailed explanations of the observed shifts in Commerzbank’s EAM control mechanism portfolio between two episodes.

We draw from our analysis that major shifts in the approach to EAM, captured through the overall portfolio of EAM control mechanisms, often follow new opportunities or major changes in the surrounding constraints within which an organisation operates. Consequently, the transition between two episodes in our case was generally preceded by the realisation that certain assumptions no longer hold true or by uncovering entirely new paths of action, for example, in the form of previously not envisioned types of technology. The EAM control mechanism portfolio perspective provided an efective means for Commerzbank to continuously readjust their EAM in reaction to such changing circumstances, allowing to match the EAM control mechanism portfolio with the overall situation, strategy, and top-level management priorities.

Episode I provides a good example of a scarcity and crisis situation that is well-suited for emphasising formal modes of control. Limited resources enable a strict, topdown driven focus on integration and cost reduction, which is facilitated by a clear relation between input control mechanisms and the targeted goals. Furthermore, there was a clear need for the control mechanisms to become efective almost immediately. This contrasts with the episode III, in which the severe financial constraints were lessened, and the focus shifted to fostering innovation in new technologies. In this situation, without clear a priori outcomes, various informal modes of control that allow for slack and support employee empowerment as well as social exchange proved to be more efective.

In general, we found that behavioural and output control work best when there are clear goals and procedures to establish adequate control structures. In contrast, informal modes of control are wellsuited for handling turbulent situations with a large degree of uncertainty regarding targeted outcomes as well as how to get there, since they can be implemented even in the absence of clear targets and roadmaps.

Despite these situational considerations, our findings suggest that EAM, similar to, for example, business process management (BPM; Mendling et al., 2020), needs to balance several critical aspects in the long run. These include, for example, balancing short-term and long term goals as well as local project needs and global organisational targets (Brosius et al., 2018), which in turn requires to establish structures and practices that (re-)enforce compliance while still allowing for positive deviance in unforeseen situations (Mendling et al., 2020). Essentially, we argue that enterprise architects need to find a balance between actively enforcing clear structures, architectural blueprints, roadmaps, and principles on the one hand, and purposefully allowing an open exchange of ideas, values, and beliefs on the other hand (K. Haki et al., 2020).

This notion of “balance” is clearly visible in our analysis of Commerzbank’s EAM journey. We found that formal control is often quicker to take efect compared to informal control, which may take a long time to achieve noticeable impacts in the overall organisation. However, even though it may be advisable to emphasise formal control in scarcity and crisis situations (such as the beginning of episode I), it is still important to adequately position EAM in the overall organisation in terms of informal control, for example, by highlighting its potential to provide some degree of safety and stability. While not as immediately efective as direct formal control, taking on conscious eforts to establish such informal modes of control in the organisation has led to an increased appreciation of EAM over time, even during challenging times. Similarly, even in situations that are well-suited for informal control, resource use and allocation should still be monitored and controlled. For example, in the beginning of episode II, when the development of the new target architecture was just starting, progress could already be tracked by considering intermediate artefacts, such as documentation (output control) or adherence to best practices (behavioural control).

Table 2 summarises the practical insights that we draw from our case with regard to specific situational considerations while still aiming for an overall balanced EAM control mechanism portfolio.

Table 2. Key practical insights and related observations.

<table><tr><td>Theme</td><td>Practical insight</td><td>Explanation</td></tr><tr><td rowspan="4">Portfolio must match the situation, strategy, and top-level priorities</td><td>In scarcity and crisis situations, input control is highly effective</td><td rowspan="2">Limited and desirable resources enable input controlClear relation between control mechanisms and goalsCan be quickly established with impactSupported by allowing for slackEmployees must feel empowered to think on their ownFurther strengthened through social exchanges and knowledge sharing</td></tr><tr><td>Innovation can effectively be supported through informal control</td></tr><tr><td>Behavioural and output control requires clear goals and procedures</td><td>Goals must be clear and measurableProcedures must be suitable to reach goalsSupervision must be possible and socially accepted</td></tr><tr><td>Uncertainties can effectively be managed through informal control</td><td>In case of unclear uncertainties and turbulences, social exchange facilitates alignmentSocial pressures to perform well are independent of external objective goal formulations</td></tr><tr><td rowspan="4">Portfolio must be balanced in the long term</td><td>Formal control is often faster to implement than informal control</td><td>Formal control can be established with a direct and immediate impactInformal control takes time to function effectivelyLong-term benefits of informal control are crucial</td></tr><tr><td>In scarcity and crisis situations, safety and stability is valued</td><td>Even in crisis situations, informal control can be effective by positioning the controller as a stabilising elementIn contrast, emphasise freedom and opportunity to support innovation</td></tr><tr><td>Uncertain goals can be tracked by formal intermediate artefacts</td><td>In the absence of clear goals, intermediate artefacts (documentation, best practices) can be trackedAllows for a high-level management perspective in uncertain times</td></tr><tr><td>Support informal control through formal roles and allocation processes</td><td>Effectively exerting informal control can be very time consumingCounteract excessive use of resources through complementary formal roles and allocation processes</td></tr></table>

Within Commerzbank, the EAM team employed this perspective to reflect on and continuously readjust how EAM should operate in the organisation. The concept of control mechanism portfolios allowed to derive thorough explanations for the efectiveness (or ineficacy) of specific structures and activities in a given organisational setting, which enabled the involved stakeholders to continuously adapt their EAM approach to match constantly evolving constraints and opportunities.

In this paper, we traced the development EAM at Commerzbank for more than a decade and through three distinct episodes. Even though our analysis is limited to a single organisation, over time we have demonstrated the applicability of this approach to three very diferent situations. Regarding projectability of our findings, we want to highlight two aspects: First, we expect there to be a critical threshold regarding the size and overall complexity of an organisation for certain issues with EAM to arise. For example, the discussion of balancing local and global perspectives in EAM only arises in large organisations (Brosius et al., 2018). Second, Commerzbank, as any other large international bank, is operating within an environment that forced fundamental strategic shifts in the organisation, leading to multiple distinct episodes of EAM between 2008–2018. Consequently, we believe our findings to apply to other large organisations in industries that were afected by major strategic disruptions (e.g., energy and utilities), but not in other industries (e.g., logistics).

## Disclosure statement

No potential conflict of interest was reported by the author(s).

## Funding

This work was supported by the Schweizerischer Nationalfonds zur Förderung der Wissenschaftlichen Forschung [247310].

## ORCID

Kazem Haki http://orcid.org/0000-0002-8807-0147

## References

Aier, S., Labusch, N., & Pähler, P. (2015). Implementing architectural thinking: A case study at commerzbank Ag. Proceedings of the CAiSE 2015 Workshops, Stockholm, Sweden, Lecture Notes in Business Information Processing, 215, Cham: Springer.

Beese, J., Aier, S., Haki, K., & Aleatrati Khosroshahi, P. (2016). Drivers and efects of information systems architecture complexity: A mixed-methods study.

24th European Conference on Information Systems (ECIS), Istanbul, Turkey, Association for Information Systems.

Boh, W. F., & Yellin, D. (2006). Using enterprise architecture standards in managing information technology. Journal of Management Information Systems, 23(3), 163–207. https://doi.org/10.2753/ MIS0742-1222230307

Brosius, M., & Aier, S. (2016). The impact of enterprise architecture management on design decisions in is change projects. In V. Nissen, D. Stelzer, S. Straßburger, & D. Fischer (Eds.), Multikonferenz Wirtschaftsinformatik (Vol. 2016, pp. 1405–1416). Univ.-Verl.

Brosius, M., Aier, S., Haki, K., & Winter, R. (2018). Enterprise architecture assimilation: An institutional perspective. Proceedings of the 39th International Conference on Information Systems (ICIS 2018), San Francisco, USA, Association for Information Systems.

Brown, A. E., & Grant, G. G. (2005). Framing the frameworks: A review of it governance research. Communications of the Association for Information Systems, 15(1), 696–712. https://doi.org/10.17705/1CAIS.01538

Busby, J. S., & Collins, A. M. (2014). Organizational sensemaking about risk controls: The case of ofshore hydrocarbons production. Risk Analysis, 34(9), 1738–1752. https://doi.org/10.1111/risa.12198

Cardinal, L. B., Sitkin, S. B., & Long, C. P. (2004). Balancing and rebalancing in the creation and evolution of organizational control. Organization Science, 15(4), 411–431. https://doi.org/10.1287/orsc.1040.0084

Choudhury, V., & Sabherwal, R. (2003). Portfolios of control in outsourced software development projects. Information System Research, 14(3), 291–314. https:// doi.org/10.1287/isre.14.3.291.16563

Ciborra, C. U., Braa, K., Cordella, A., Dahlom, B., Failla, A., Hanseth, O., Hepso, V., Ljungberg, J., Monteiro, E., & Simon, K. (2000). From control to drift: the dynamics of corporate information infastructures. Oxford University Press.

Commerzbank. (2009a). Annual report 2008.

Commerzbank. (2009b). Commerzbank Roadmap 2012.

Commerzbank. (2009c). Press release: Dresdner bank merged into commerzbank.

Commerzbank. (2012a). Annual Report 2011

Commerzbank. (2012b). Group services: From integration to operational excellence. Investors’ Day 2012

Commerzbank. (2016). Commerzbank to increase profitability through focus and digitalisation.

Commerzbank. (2020). Annual Report 2019.

Cram, W. A., Brohman, M. K., & Gallupe, R. B. (2016a). Hitting a moving target: A process model of information systems control change. Information Systems Journal, 26 (3), 195–226. https://doi.org/10.1111/isj.12059

Cram, W. A., Brohman, M. K., & Gallupe, R. B. (2016b). Information systems control: A review and framework for emerging information systems processes. Journal of the Association for Information Systems, 17(4), 216–266. https://doi.org/10.17705/1jais.00427

Eisenhardt, K. M. (1985). Control: organizational and economic approaches. Management Science, 31(2), 134–149. https://doi.org/10.1287/mnsc.31.2.134

Eisenhardt, K. M. (1989). Building theories from case-study research. Academy of Management Review, 14(4), 532–550. https://doi.org/10.2307/258557

Farjoun, M. (2010). beyond dualism: stability and change as a duality. Academy of Management Review, 35(2) , 202– 225. https://doi.org/10.5465/amr.35.2.zok202

Feldman, M. S., & Orlikowski, W. J. (2011). Theorizing practice and practicing theory. Organization Science, 22 (5), 1240–1253. https://doi.org/10.1287/orsc.1100.0612

Feldman, M. S., Pentland, B. T., D’Adderio, L., & Lazaric, N. (2016). Beyond routines as things: Introduction to the special issue on routine dynamics. Informs, 3 ,505–513. https://doi.org/10.1287/orsc.2016.1070

Gregory, R. W., Beck, R., & Keil, M. (2013). Control balancing in information systems development ofshoring projects. MIS Quarterly, 37(4), 1211–1232. https://doi. org/10.25300/MISQ/2013/37.4.10

Haki, M. K., Aier, S., & Winter, R. (2016). A stakeholder perspective to study enterprisewide is initiatives. 24th European Conference on Information Systems (ECIS), Istanbul, Turkey, Association for Information Systems.

Haki, K., Beese, J., Aier, S., & Winter, R. (2020). The evolution of information systems architecture: An agent-based simulation model. MIS Quarterly, 44(1), 155–184. https:// doi.org/10.25300/MISQ/2020/14494

ISO/IEC/IEEE. (2011). Systems and software engineering— architecture description (ISO/IEC/IEEE Std 42010:2011). ISO/IEC and IEEE Computer Society.

Jonkers, H., Lankhorst, M., ter Doest, H., Arbab, F., Bosma, H., & Wieringa, R. (2006). Enterprise architecture: Management tool and blueprint for the organisation. Information Systems Frontiers, 8(2), 63–66. https://doi.org/10.1007/s10796-006-7970-2

Kirsch, L. J. (1997). Portfolios of control modes and is project management. Information Systems Research, 8 (3), 215–239. https://doi.org/10.1287/isre.8.3.215

Lagerström, R., MacCormack, A., Dreyfus, D., & Baldwin, C. (2019). A methodology for operationalizing enterprise it architecture and evaluating its modifiability. Complex Systems Informatics and Modeling Quarterly, 19 ,75–98. doi:10.7250/csimq.2019-19.05.

Lankhorst, M., van Buuren, R., van Leeuwen, D., Jonkers, H., & ter Doest, H. (2004). Enterprise architecture modelling - the issue of integration. Advanced Engineering Informatics, 18(4), 205–216. https://doi.org 10.1016/j.aei.2005.01.005

Löhe, J., & Legner, C. (2014). Overcoming Implementation challenges in enterprise architecture management: A design theory for architecture-driven it management (Adrima). Information Systems and E-Business Management, 12(1), 101–137. https://doi.org/10.1007/s10257-012-0211-y

Malaurent, J., & Avison, D. (2016). Reconciling global and local needs: A canonical action research project to deal with workarounds. Information Systems Journal, 26(3), 227–257. https://doi.org/10.1111/isj.12074

Markus, M. L., & Robey, D. (1988). Information technology and organizational change - causal structure in theory and research. Management Science, 34(5), 583–598. https://doi.org/10.1287/mnsc.34.5.583

Mendling, J., Pentland, B. T., & Recker, J. (2020). Building a complementary agenda for business process management and digital innovation (pp. 208–219). Taylor & Francis.

Mocker, M. (2009). What Is complex about 273 applications? Untangling application architecture complexity in a case of European investment banking,” 42nd Hawaii International Conference on System Sciences (HICSS 2009), Big Island, USA. IEEE Computer Society.

Mohr, L. B. (ed.). (1982). Explaining organizational behavior. Jossey-Bass.

Nye, F. I. (1958). Family relationships and delinquent beha vior. John Wiley.

Ouchi, W. G. (1979). A conceptual framework for the design of organizational control mechanisms. Management Science, 25(9), 833–848. https://doi.org/10.1287/mnsc. 25.9.833

Pettigrew, A. M. (1992). The character and significance of strategy process research. Strategic Management Journal, 13(S2), 5–16. https://doi.org/10.1002/smj. 4250130903

Pettigrew, A. M. (1997). What is a processual analysis? Scandinavian Journal of Management, 13(4), 337–348. https://doi.org/10.1016/S0956-5221(97)00020-1

Pettigrew, A. M., Woodman, R. W., & Cameron, K. S. (2001). studying organizational change and development: challenges for future research. The Academy of Management Journal, 44(4), 697–713. https://doi.org/10. 5465/3069411

Rahimi, F., Gøtze, J., & Møller, C. (2017). Enterprise architecture management: toward a taxonomy of applications. Communications of the Association for Information Systems, 40(1), 120–166. https://doi.org/10.17705/ 1CAIS.04007

Richardson, G. L., Jackson, B. M., & Dickson, G. W. (1990). A principles-based enterprise architecture: Lessons from texaco and star enterprise. MIS Quarterly, 14(4), 385–403. https://doi.org/10.2307/249787

Ross, J. W., Weill, P., & Robertson, D. C. (2006). enterprise architecture as strategy. creating a foundation for business execution. Harvard Business School Press.

Ross, J. W. (2006). Maturity matters: how firms generate value from enterprise architecture. Center for Information Systems Research Sloan School of Management Massachusetts Institute of Technology.

Ross, J. W., & Quaadgras, A. (2012). enterprise architecture is not just for architects. Center for Information Systems Research Sloan School of Management Massachusetts Institute of Technology.

Scheer, A.-W., & Schneider, K. (2005). Aris - architecture of integrated information systems. In P. Bernus, K. Mertins, & G. Schmidt (Eds.), Handbook on architectures of information systems (pp. 605–623). Springer.

Schilling, R. D., Aier, S., & Winter, R. (2019). “Designing an artifact for informal control in enterprise architecture management. Proceedings of the 40th International Conference on Information Systems (ICIS 2019). Munich, Germany. Association for Information Systems.

Simon, D., Fischbach, K., & Schoder, D. (2013). An exploration of enterprise architecture research. Communications of the Association for Information Systems, 32(1), 1–72. https://doi.org/10.17705/1CAIS.03201

Tannenbaum, A. S. (1962). Control in organizations: Individual adjustment and organizational performance. Administrative Science Quarterly, 7(2), 236–257. https:// doi.org/10.2307/2390857

The Open Group, The Open Group (2017). Archimate® 3.0.1 specification.

The Open Group. (2018). the open group architecture framework (Togaf) Version 9.2. Van Haren Publishing.

Van de Ven, A. H., & Huber, G. P. (1990). Longitudinal field research methods for studying processes of organizational change. Organization Science, 1(3), 213–219. https://doi.org/10.1287/orsc.1.3.213

Vessey, I., & Ward, K. (2013). The dynamics of sustainable is alignment: The case for is adaptivity. Journal of the Association for Information Systems, 14(6), 283–311. https://doi.org/10.17705/1jais.00336

Vom Brocke, J., van der Aalst, W., Grisold, T., Kremser, W., Mendling, J., Pentland, B., Recker, J., Roeglinger, M., Rosemann, M., & Weber, B. (2021 (Elsevier)). Process science: The interdisciplinary study of continuous change. Available at SSRN 3916817.

Weick, K. E., & Quinn, R. E. (1999). Organizational change and development. Annual Review of Psychology, 50(1), 361–386. https://doi.org/10.1146/annurev.psych.50.1.361

Wiener, M., Mähring, M., Remus, U., & Saunders, C. (2016). Control configuration and control enactment in information systems projects - review and expanded theoretical framework. MIS Quarterly, 40(3), 741–774. https://doi.org/10.25300/MISQ/2016/40.3.11

Winter, R. (2014). Architectural thinking. Business & Information Systems Engineering, 6(6), 361–364. https:/ doi.org/10.1007/s12599-014-0352-2

Zachman, J. A. (1987). A framework for information systems architecture. IBM Systems Journal, 26(3), 276–292. https://doi.org/10.1147/sj.263.0276

## Appendix A: Details of the cooperation with Commerzbank

This research project originates from a long-term collaboration between corporate enterprise architects of Commerzbank AG and the University of St.Gallen, dating back to first discussions in 2008. Regular meetings between Commerzbank’s senior enterprise architects and university researchers consequently led to the founding of two diferent competence centres (the Competence Centre Corporate Intelligence – CC CI, and the Competence Centre on Business Intelligence in the Banking Community – BI BC) in 2011, focussing on enterprise architecture and data management and analytics respectively. Each competence centre organised three two-day workshops each year, in which the current topics from practice and new academic insights were discussed. Over time, several focus areas emerged (i.e., work and research streams that spanned multiple workshops with additional engagements in between), including joint eforts to increase the impact of enterprise architecture management (EAM) within Commerzbank. See, Table 3 for an overview of these engagements.

Martin Kraus, the fourth author of this paper, played a key role in this engagement. From 2009 to 2019 Martin Kraus was leading the enterprise architecture team for the corporate centre functions, i.e., the risk, finance, and compliance areas of Commerzbank. During our prolonged collaboration, he not only ensured that we could directly observe critical developments and that the relevant colleagues from Commerzbank engaged with our team during joint workshops and discussions, but also that the generated ideas and results would find their way back into the EAM community within Commerzbank. He also actively contributed to writing this paper.

Initial discussions and solution approaches in 2012 were sparked by the, at that time, novel report by Ross and Quaadgras (2012), highlighting that overly formalised EAM often fails to achieve the desired results. Consequently, we were looking for diferent ways to broaden our perspective on how to best institutionalise EAM in an organisation, going beyond the formal, topdown driven mechanisms predominantly discussed both within Commerzbank and in EAM literature. Over time, driven by both academic research and feedback from practice, the idea of the “EAM control mechanism portfolios” emerged and found its way into discussions, slides, and strategic plans. Having noticed that this idea had become ingrained in the EAM department, we decided in 2017 to conduct a series of interviews and to review old documents, with the aim to formalise the EAM control mechanism portfolio concept by reconstructing how it had been historically applied within Commerzbank. Again, this was a joint efort, in which we relied on the existing collaboration structures (e.g., the two competence centres and our direct contacts) to identify suitable interviewees and relevant documents and to analyse, organise, and review our results. See Appendix B for the methodological details.

Table 3. Overview of related engagements between Commerzbank and the author team.

<table><tr><td>Competence centre workshops</td><td>Other events and engagements</td></tr><tr><td>Expert communities, in which senior subject matter experts, management, and academics jointly discuss current challenges and opportunities. Competence Centre Corporate Intelligence (CC CI):</td><td>Joint conference paper: Implementing Architectural Thinking: A Case Study at Commerzbank AG (Aier et al., 2015)</td></tr><tr><td>Focus on architectural coordination and enterprise-wide perspectives on IS6. CC CI WS, 02./03.12.20137. CC CI WS, 31.03./01.04.20148. CC CI WS, 16./17.06.20149. CC CI WS, 13./14.10.201410. CC CI WS, 11./12.02.201511. CC CI WS, 11./12.05.201512. CC CI WS, 19./20.10.201513. CC CI WS, 29.02./01.03.2016</td><td>Public events08.06.2015: The authors hosted the 42. St. Galler Anwenderforum (an EA practitioner conference), where Commerzbank reported on their current EAM approach.29.10.2018: Martin Kraus, head of Commerzbank&#x27;s Architecture Corporate Centre (the fourth author), presented Commerzbank&#x27;s approach to Data Architecture Management.Other workshops11.09.2014: The authors held an EAM workshop at Commerzbank in Frankfurt28.11.2014: The authors held a presentation and a workshop on EAM at Commerzbank&#x27;s Architecture Day03.04.2019: The fifth author held an EAM workshop at Commerzbank in Frankfurt</td></tr><tr><td>Business Intelligence Banking Community (BI BC) – later renamed to Data Management and Analytics Community in Banking (DMAC): Focus on architectural thinking and enterprise-wide perspectives on data</td><td></td></tr><tr><td>01. Workshop BI BC, 28./29.03.201202. Workshop BI BC, 14./15.01.201303. Workshop BI BC, 07./08.07.201404. Workshop BI BC, 01./02.12.201405. Workshop BI BC, 27./28.04.201506. Workshop BI BC, 03./04.09.201507. Workshop BI BC, 05./06.11.201508. Workshop BI BC, 11./12.04.201609. Workshop BI BC, 29./30.06.201610. Workshop BI BC, 10./11.10.201611. Workshop BI BC, 23./24.02.201712. Workshop BI BC, 26./27.06.201713. Workshop BI BC, 06./07.11.201714. Workshop BI BC, 26./27.02.201815. Workshop BI BC, 18./19.06.201816. Workshop BI BC, 03./04.12.201817. Workshop BI BC, 18./19.03.201919. Workshop DMAC, 04./05.11.2019</td><td></td></tr></table>

## Appendix B: Methodological details

This appendix provides the details of our methodological approach, including the overall procedure, the interviews (primary data), other secondary data, and our coding process.

## Interview procedure and document acquisition

Regarding interviewee selection, while working closely with the core EAM team, we also ensured to interview other stakeholders inside Commerzbank to understand the outside perception of EAM activities within the bank over time. Thus, we specifically focussed on employees with long tenure from both business and IT functions on diferent hierarchical levels (top management and operational levels), enabling us to reconstruct how and why adjustments to the EAM control mechanism portfolio were made during each episode and how these changes were perceived in the overall organisation. The final ten interview candidates were chosen from four distinct areas (see, Table 4): Business global (strategic perspective on the operations of the organisation), business local (local operations), IT global (strategic perspective on the overall IT function), and IT local (local business support).

All interviews were conducted by two researchers who led through the interview with the help of a previously developed interview guideline (covering the diferent types of control mechanisms and the development and perception of EAM activities over time). All ten interviews lasted between 51 and 79 minutes (see, Table 4), and were recorded, transcribed, and subsequently coded.

In addition to the interviews, we also collected internal presentations of past joint workshops from the two competence centres (totalling 218 PowerPoint presentations from 2011–2018) and publicly available reports, including strategy documents released to shareholders and all annual reports between 2008 and 2018. These documents were not fully coded, but only skimmed through after the interview coding to provide additional context to the findings and to complement the overall story with documentation that can be referenced and publicly accessed.

Table B1: Overview of codes for the control mechanisms.

<table><tr><td>Control mechanism</td><td>Code</td></tr><tr><td rowspan="4">Input control</td><td>Allocation of human resources [IC-1]</td></tr><tr><td>Allocation of financial resources [IC-2]</td></tr><tr><td>Allocation of material resources [IC-3]</td></tr><tr><td>Organizational arrangements for allocating resources [IC-4]</td></tr><tr><td rowspan="4">Behaviour control</td><td>Processes to govern individual actions [BC-1]</td></tr><tr><td>Rules to guide individual actions [BC-2]</td></tr><tr><td>Mechanisms to observe compliance [BC-3]</td></tr><tr><td>Systems to reward compliance with rules/processes [BC-4]</td></tr><tr><td rowspan="2">Outcome control</td><td>Specific desired outcomes [OC-1]</td></tr><tr><td>Processes to measure and promote outcomes [OC-2]</td></tr><tr><td rowspan="3">Clan control</td><td>Shared norms, values, and beliefs [CC-1]</td></tr><tr><td>Reflective activities [CC-2]</td></tr><tr><td>Interpersonal social ties [CC-3]</td></tr><tr><td rowspan="2">Self-control</td><td>Intrinsic motivation [SC-1]</td></tr><tr><td>Personal and professional standards [SC-2]</td></tr></table>

## Coding procedure

We employed a coding scheme based on the diferent control mechanisms shown in Table B1, following the recommendation of Eisenhardt (1989). Additionally, we also coded perceived major environmental jolts and misalignments, as well as corresponding interpretations of strategic consequences and reactions in terms of EAM portfolio adjustments, focussing on why these adjustments were deemed to be efective and appropriate. The final coding guideline included specific definitions and examples for each code to guide the coding process.

We then coded the documents in a partially top-down (i.e., starting with codes for the diferent control mechanisms) and partially bottom-up fashion (i.e., allowing for new codes to capture a control mechanism’s efectiveness or major turning points). In this process, we first highlighted all relevant occurrences of a code in the transcripts and added a short descriptive summary for each occurrence. After this initial round of coding, results were discussed among the authors to achieve a suficiently high level of reliability and agreement on the categorisation of data. Then we proceeded to structure and group the resulting codes (leading to the identification of the diferent episodes), and finally went back to the transcripts as well as the additional presentation slides and public documents to gather further contextual information and to position the codes along the timeline from 2008 to 2018. This allowed us to analyse how the environmental jolts and strategic shifts were interpreted by the involved stakeholders and how these interpretations resulted in changes to the EAM control mechanism portfolio over time for each episode.

Table 4. Profiles of interviewees.

<table><tr><td colspan="2">Organisational level</td><td>#</td><td>Role</td><td>Tenure (years working at Commerzbank)</td><td>Duration of the interview in minutes</td></tr><tr><td rowspan="4">Business</td><td rowspan="2">Global</td><td>1</td><td>Divisional board member</td><td>5</td><td>57</td></tr><tr><td>2</td><td>Division manager</td><td>12</td><td>54</td></tr><tr><td rowspan="2">Local</td><td>3</td><td>Programme manager</td><td>13</td><td>55</td></tr><tr><td>4</td><td>Department head</td><td>18</td><td>52</td></tr><tr><td rowspan="6">IT</td><td rowspan="2">Global</td><td>5</td><td>Enterprise architect</td><td>23</td><td>79</td></tr><tr><td>6</td><td>Enterprise architect</td><td>15</td><td>58</td></tr><tr><td rowspan="4">Local</td><td>7</td><td>Representative of «agile community»</td><td>17</td><td>59</td></tr><tr><td>8</td><td>Head of development resources</td><td>7</td><td>76</td></tr><tr><td>9</td><td>Delivery manager</td><td>17</td><td>51</td></tr><tr><td>10</td><td>Project lead</td><td>7</td><td>64</td></tr></table>
