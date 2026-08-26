---
otero_id: 9826
otero_key: "PMMRCDWH"
title: "Facilitating like Darwin: Supporting cross-fertilisation in crowdsourcing"
authors: "Henner Gimpel; Valerie Graf-Drasch; Robert J. Laubacher; Moritz Wöhl"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113282"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Facilitating like Darwin: Supporting cross-fertilisation in crowdsourcing

Henner Gimpel<sup>a,b</sup>, Valerie Graf-Drasch<sup>b</sup>, Robert J. Laubacher<sup>c</sup>, Moritz Wöhl<sup>a,b,⁎</sup>

![](/api/attachments/PMMRCDWH/fulltext/images/5c36d7ec72e5a957c4088bf7d7ff58dfa7f985daaa8f95f01f6ae9f47ae7b69b.jpg)

<sup>a</sup> FIM Research Center, University of Augsburg, Germany

<sup>b</sup> Project Group Business & Information Systems Engineering of the Fraunhofer FIT, Germany

<sup>c</sup> Center for Collective Intelligence, Massachusetts Institute of Technology (MIT), United States of America

## A R T I C L E I N F O

Keywords: Cross-fertilisation Crowdsolving Facilitation Collective intelligence Design science

## A B S T R A C T

Humankind faces many “wicked” decision-making problems, which must be solved. One promising approach refers to crowdsourcing systems that hold the potential to solve any kind of problem – notably wicked ones. Crowdsourced solutions work well because crowds exchange knowledge from diferent domains – a concept known as “cross-fertilisation.” Thereby, the “facilitator” of a crowdsourcing system is the primary decision maker when it comes to specifying and managing the crowd. The facilitator's role includes actively managing cross-fertilisation. However, in the light of technological advancements and large-scale data, facilitation proves difficult – especially in one particular type of crowdsourcing – crowdsolving. Thus, academia recently called for relieving some burden of facilitators and started developing tools for supporting or automated facilitation. Yet, the focus of existing tools is not on fostering the innermost core of crowdsolving endeavours – cross-fertilisation. By taking a design science perspective, we propose design principles and design guidelines for a decision-support tool aiding facilitators to (a) set the boundary conditions for, (b) measure, and (c) facilitate cross-fertilisation. We evaluate feasibility and value added of the abstract design by applying it to diferent crowdsolving platforms including a prototypical implementation and qualitative evaluation by facilitators.

## 1. Introduction

Our global society faces many important decision-making problems of “wicked” kind [1,2]. These are highly complex problems for which no single computational formulation is suficient, and for which involved stakeholders even disagree on what the problem actually is [2–5]. One of these wicked problems is global climate change: it clearly is universal, it must be addressed with haste, and there is a lack of central authority pushing towards a solution [2,3,6,7].

To solve wicked problems in general, and climate change in parti cular, crowdsourcing as a promising approach has received much attention over the past years in research and practice [1,2,8,9]. Howe [10] already asserted over a decade ago that crowdsourcing holds the potential to solve any kind of problem. The rationale making crowdsourced solutions so valuable originates from diversity, often coming along with crowds: diverse crowd members are able to intellectually cross-fertilise one another, providing solutions superior to those ofered by lone individuals [11–14]. Thus, heterogeneous crowds may provide significant insight and wisdom, and cross-fertilisation enhances their ability to develop solutions to so-called “wicked problems” [13–17].

Thereby, “facilitators” in crowdsourcing systems take on a central role, as they are primarily responsible for avoiding homogeneous knowledge creation in the crowd and managing associated processes accordingly [9,18,19]. Particularly, a facilitator must decide upon procedural and/or content-related actions to eficiently coordinate, lead, integrate, classify, and summarise the discussion so that the crowd can achieve efective results [9]. Thus, the facilitator greatly afects crowd behaviour and quality of associated contributions [9,18].

As information and insights do not automatically emerge out or raw crowdsourced data, the facilitator must make active decisions [19,20]. Thereby, in current times of greater scope and large-scale crowdsourcing systems, facilitators are forced to acquire systematic methodologies to maintain a high degree of information and knowledge accessibility. Otherwise, they could not establish options and select adequate courses of action to guide the crowdsourcing process [8,18,19].

Only recently, academia acknowledged that facilitators must be supported in managing such crowdsourcing systems [8,9,18,19]. In relieving some burden of facilitators, scholars have proposed advancements in machine learning algorithms for supporting automated facilitation [8,9,18,21]. While this research stream has already made great strides, the focus of existing tools primarily is on supporting the facilitator in achieving consensus within crowd discussions eficiently [8,9]. However, tools supporting the facilitator in measuring and fostering cross-fertilisation especially in a particular type of crowdsourcing – crowdsolving – are currently missing (see Section 2.2 for details on crowdsolving). In this work, we address this gap and follow scholars current call to action in this regard [8,9]. Particularly, the objective of our study is to:

Develop design principles and design guidelines for intelligent decision-making support tools aiding facilitators of crowdsolving for wicked problems in fostering and managing cross-fertilisation in their crowds.

Taking an information systems design science perspective, we propose four generic design principles leading to 15 detailed design guidelines for a decision-support tool aiding the facilitator of a crowdsolving system, to (a) set the boundary conditions for, (b) mea sure, and (c) facilitate cross-fertilisation. For brevity, we use the term “the tool” as reference to the abstract design principles and guidelines for the respective decision-support tool. To demonstrate the tool's value added and feasibility, we instantiate a respective prototype in the realworld crowdsourcing system "Futures CoLab", henceforth referred to as the “FCL”. The FCL is a crowdsolving system, jointly operated by the Center for Collective Intelligence of the Massachusetts Institute of Technology (MIT CCI) and Future Earth. The goal of the FCL is to enable diverse experts to collectively explore solutions to global systemic challenges, referencing wicked problems [22]. Additionally, we discuss the tool's feasibility in the surrounding space of further crowdsourcing systems. With this study, we contribute to both research and practice on crowdsourcing. For research on crowdsourcing, we outline how to design information systems and in particular evolving decision-support tools to provide adequate support for facilitators. For practice on crowdsourcing, our research is triggered by the needs of practitioners, and resulting design principles and guidelines primarily aim at sup porting and advancing their daily operations.

The remainder of this paper is structured as follows. We present the theoretical background of our work and review related literature on crowdsourcing and existing support tools for facilitators. In Section 3 we describe the paper's underlying methodology. We develop design principles and guidelines in Section 4 and evaluate them in Section 5. We conclude by discussing the implications for theory and practice.

## 2. Theoretical background

## 2.1. Wicked problems

Academia defines two overarching problem categories: hard and soft. Hard problems are mostly mathematic or algorithmic, such as stock-price prediction or proposals for the exploration of new raw material occurrences. Solutions to hard problems must comply with well-defined evaluation criteria and preserve objectivity [23,24].

By contrast, soft problems lack clear solutions and objectivity [23,24]. Extremely complex and vague soft problems, which involve divergent viewpoints and the interests of multiple stakeholders, reference wicked problems. Global climate change, social injustice, or afordable, high-quality healthcare are just a few examples of wicked problems [2,3,6,7]. Solving wicked problems is not easy. Their subjective nature means that definitions of these problems – and potential solutions – are often highly contentious. Consequently, intervention, rather than a solution, is usually the goal [24–26]. To measure the success of an intervention is dificult for three reasons: (1) the future development of a problem is often hard to predict; (2) the efects often take a very long time to become apparent; (3) it is a delicate analysis to isolate the impact of a single intervention given the vast number of interventions taking place [27–30]. Most promising approaches to identifying a reasonable intervention are collaborative, utilising tech enabled approaches to bring together stakeholders and combine the abilities of humans and machines $[ 1 3 - 1 5 , 1 7 , 3 1 ]$ . Collaborative strategies base on the rationale that individuals achieve better results working together than they do working alone. Ultimately, wicked problems are social issues and, as such, demand responses which are fundamentally social in their nature $[ 1 5 \mathrm { - } 1 7 , 3 2 , 3 3 ]$ . One approach falling within this paradigm and additionally asserted to be particularly suitable for solving wicked problems is crowdsourcing $[ 1 , 2 , 1 0 , 3 4 ]$

## 2.2. Crowdsourcing as a solution approach for wicked problems

Crowdsourcing is often used as an umbrella term for a variety of approaches, which harness the potential of the human collective by issuing open calls for contributions to a particular task [11,23,35]. In organisational contexts, crowdsourcing is often linked to open innovation [36]. Particularly, when the sourcing serves a corporate goal, open innovation is consistent with crowdsourcing and can be efectively done in the crowdsourcing mode [37,38]. However, it is worth noting that although the two concepts share the assumptions that knowledge is distributed and the crowd wisdom and the collective intelligence can be a source of competitive advantage, crowdsourcing and open innovation have some diferences [39]: On the one hand, open innovation exclusively focuses on innovation processes while crowdsourcing is much broader in perspective [37,39]. On the other hand, open innovation mainly describes knowledge flows between firms, or when applied to a very large degree, also with stakeholders (mainly customers) [38,40]. By contrast, crowdsourcing refers to links between an organisation and an (rather) undefined, anonymous crowd [39].

We follow an established stream of literature and define crowdsourcing as a sourcing approach for information, which supports decision makers in their decision making through wisdom generated by an anonymous crowd [19,41,42]. This wisdom is the result of improvements made by one person providing the foundation for the additional improvements made by the next in the crowd [43–47].

Surowiecki [34] found that a diverse, decentralised, and independent crowd tends to lead to successful crowdsourcing. Thereby, particularly diversity is key in yielding solutions from crowdsourced tasks for reasonably complex tasks [48]. This link between diversity and superior performance is originally rooted in biology and known as cross-fertilisation. Historically, the natural scientist Charles Darwin examined the self- and cross-fertilisation of plants and found that self-fertilised progeny had weaker characteristics than cross-fertilised progeny [49,50]. Recently, this concept has found its way from biology to social science where it serves as performance accelerator since scholars emphasised that diverse groups outperform homogenous ones [33,51–54]. Although a widely accepted definition of cross-fertilisation in this social context is not yet established, current explanations focus on the inter action of diverse individuals with regards to either knowledge, specialisations, or domains [18,55–57]. And while exchanges between people from diferent domains of knowledge do not always result in superior ideas (e.g., because of too little exchange or conflicts among diverse participants), the probability of high-quality ideas being generated is higher than in an exchange between people from the same knowledge domain [55].

Darwin not only observed but also facilitated cross-fertilisation by, firstly, planting various species and creating a diverse set of plants and, secondly, actively managing pollination to accelerate reproduction [49]. Likewise, the cross-fertilisation of human ideas can also be facilitated by, firstly, creating an environment in which cross-fertilisation can easily occur – i.e., by bringing together diverse, open-minded, and motivated people as a crowd – and, secondly, purposefully influencing interaction therein [55]. A crowdsourcing system for which such crossfertilisation may be particularly valuable, is one that seeks heterogeneous contributions which are appraised individually in accordance with their quality, and which unfold their value in an emergent way (i.e., the value emerges from a subset of contributions which are considered in combination). Such crowdsourcing systems are considered as “crowdsolving” systems, which are in the focus of this work [23,42]. Thus, we henceforth use the term “crowdsolving” to reference this focus.

A crowdsolving system considers three categories of actors [19,42]:

1) the (diverse) individuals forming the crowd,

2) stakeholder(s) $( \boldsymbol { \mathrm { e . g . } } ,$ organisations) benefitting from the crowd's contributions,

3) an intermediation platform and facilitator, linking the crowd and the stakeholder(s) and thus, serving as crowdsourcing enabler.

Those actors are involved in crowdsourcing respectively crowdsolving throughout the whole process, which typically consists of five phases, namely sourcing, validating, consolidating, evaluating, and choosing. During these phases, content is generated, verified, aggregated, rated among relevant criteria, and relevant contributions are selected. These phases usually build upon each, however, it is possible to jump back to previous phases [19]. A central and boundary-spanning role at this interface is taken on by the “facilitator” as primary decision maker when it comes to specifying and managing the crowd and associated crowd data [19,58,59].

## 2.3. Facilitator as central decision-maker in crowdsolving

A facilitator has various actions to influence crowd work. We follow Ito [9] and assume that a facilitator thereby selects the action that maximises the expected utility corresponding to his/her intention. Literature on the matter distinguishes two overarching categories of actions that facilitators can take: process and content facilitation [60,61].

In process facilitation, the focus is on the crowd's processes and relationships. In this sense, a facilitator equals a process guide who simplifies processes and increases convenience in this regard [9,60]. Exemplary actions include the monitoring of postings in subject threads, observing replies or voting behaviour, motivating participants for productive and fruitful discussions, or identifying participants who are engaging in anti-social behaviour [9,58–60]. In content facilitation, a facilitator's action directly influences the (further) content of crowd work [60,61]. Exemplary actions refer to facilitator comments to crowd members' contributions to make them aware of connections with other contributions and knowledge domains for avoiding homogenous knowledge creation. Strategies like fostering remixing or divergent thinking have emerged in this context [62,63]. Accordingly, content facilitation supports the recombination potential of the focal knowledge nodes and therefore its inventive potential [18]. This work focuses more on content-facilitation, which arguably dominates the results of crowdsolving systems [8,18].

For facilitating crowdsourcing systems, facilitators are required to have a high degree of information and knowledge accessibility, which allows them to support knowledge aggregation and integration across contributions [9,18]. However, since crowdsourcing is characterised by dispersive, multi-threaded, and asynchronous work, human facilitators need systematic methodologies to perform associated actions [8,55]. Thus, research recently started supporting automated facilitation via developing associated tools: particularly, Ito [9] developed and implemented an intelligent crowd decision-making support system that has facilitator support functions to lead crowd discussions to better results. Similarly, Yang et al. [8] proposed a novel case-based reasoning approach to facilitate online discussions for crowd-scale deliberation. Additionally, Rhyn and Blohm [21] recently constructed a design theory for semi-automated information processing and decision support in crowdsourcing, yielding more eficient and efective decisionmaking. Although there has recently been some technical progress, scholars call for further investigation and advanced technical solutions [8,9,18]. In this work, we follow this call and aid facilitators by providing design principles and guidelines that coalesce in a tool supporting them in deciding on cross-fertilisation.

## 3. Method

We apply an information systems (IS) design science research (DSR) approach. Design is a search process [64]. Following the classification of types of theories in IS suggested by Gregor [65], our research contributes to a theory for design and action (type V). Our contribution can be classified as “improvement”, a “level 2 nascent design theory” that produces knowledge in the form of operational principles [66]. We follow the DSR methodology by Pefers et al. [67] which aims for applicable solutions for organisational problems and broadly usable artefacts [68]. Our design involves design principles (DPs) and design guidelines (DGs) for a tool to support facilitators of crowdsolving systems, enabling them to create, assess, and facilitate an environment for cross-fertilisation. DPs are generic descriptions of functionalities of an instantiation while DGs are more detailed recommendations on how to implement the DPs. Instantiations of this abstract design should hold the potential to advance crowdsolving endeavours and, thus, contribute to addressing wicked problems. Importantly, we do not claim to provide a well-developed level 3 mid-range or even grand design theory [66] – this is yet to emerge from maturing and generalising design knowledge. Rather our contribution is prescriptive knowledge captured in DPs and DGs. Design knowledge is prescriptive knowledge that is considered to have no truth value in itself [69]. Thus, the validity of DSR results can only be assessed by means of descriptive knowledge obtained in the DSR process. In the search for a satisficing design, evaluation against descriptive knowledge plays a particularly important role. For evaluation of our design artefact, we take the design objective (Section 1) as overarching objective and evaluate from an outcome-oriented, practical view [68].

We build on the six-step process of Pefers et al. [67]: (step I) Identify problem and motivate, (step II) define objectives of a solution, (step III) design and development, (step IV) demonstration, (step V) evaluation, and (step VI) communication. As our research is triggered by the needs of practitioners, the entry point of our approach is an “objective-centred solution” [67].

In Section 1 Introduction, we detail the motivations behind our research and identify a research gap (step I) and our design objective (step II). The resultant DPs and DGs were defined via a search process [64] and gradually improve in the course of our project (step III). The search process includes literature review enriched by interviews with experienced facilitators to create an initial design, which then is enriched with insights from prototyping and use of the prototype in a realworld case.

In addition to fulfilling the design objective, the tool must fulfil a meta-requirement (MR) [66]. We derived the MR from interviews with facilitators of the FCL (see Section 1 for explanation of FCL), which enabled us to identify the facilitators' mission: to extract as much value as possible from the participants' experiences and perspectives while minimising the time the participants spend on non-value-creating activities (e.g., reading duplicates, rereading ambiguous instructions, etc.). Most of the facilitators' actions, therefore, involve communication $( \mathrm { i . e . , }$ providing clear instructions and guidance, summarising content), although they are also responsible for other tasks such as deleting redundancies and synthesising results. However, facilitators' primary goal is to enable valuable contributions from the crowd [70]. Because crossfertilisation is likely to improve the quality of these contributions, it needs to be assessed. Consequently, in order to reach our design objective our meta-requirement is:

MR: Enable the facilitator to assess the level of cross-fertilisation.

The DPs and DGs for a tool to facilitate cross-fertilisation on crowdsourcing platforms were based on justificatory knowledge [71] presented in Section 2. We instantiate a prototype of this tool for testing its design in a real-world crowdsolving system (step IV). The DPs and DGs are evaluated with regards to the ease of use, eficiency, generality, and operationality. With regards to the prototype, that demonstrates the design is feasible, efective, eficient, and has an impact on the user's environment as suggested by Sonnenberg and vom Brocke [69]. These criteria ensure added value for the facilitator, applicability across various platforms, and the fulfilment of our meta-requirement (step V). Lastly, we communicate the final design of the tool (step VI).

## 4. Artefact design

Our design objective is the development of DPs and DGs for in telligent decision-making support tools that, when instantiated, aid facilitators of crowdsolving for wicked problems in fostering and managing cross-fertilisation in their crowds. To understand how and where a tool could support facilitators, we needed to gain insight into the tasks and challenges they face during a crowdsourcing process. Access to the records of previous crowdsolving endeavours provided such insights, as did our interviews with facilitators. The semi-structured expert interviews we conducted provided insights in facilitators' needs. Overall, we interviewed two facilitators and three additional stakeholders in the surrounding field of the facilitators up to ten times each. We took field notes of the interviews and analysed them subsequently [72,73]. The interviewees had already run several projects and realised that an awareness of the ways in which participants interact and contribute on the platform is of central importance when attempting to efectively facilitate the exercise. Facilitators are very interested in honing the decisions they make during the crowdsolving endeavour. They agree that there is a need for support of their facilitation decisions, which would help them to facilitate the exercise and eventually improve the quality of contributions [70].

Facilitators aim at gaining meaningful and diverse insights from experts on a given topic [70]. These insights will inform proposals for interventions on a wicked problem (see Section 2.1). We divide this goal into four sub-goals achieved via facilitation: 1) encourage parti cipants to contribute, 2) ensure they are focused on the task, 3) keep them up to date, and 4) encourage broad thinking. Depending on the sub-goal the facilitator is trying to achieve, s/he can take facilitation actions. The columns in Fig. 1 indicate the matching between the sub goal and possible facilitation actions. In terms of fostering cross-fertilisation, a facilitator will become most active in the validation and consolidation phase of a crowdsourcing process [19].

In the following, we elaborate on each of these four sub-goals and discuss possible actions the facilitator may take to achieve her/his (sub-)goal. Based on the facilitator's sub-goal we derive DPs, which are supported by literature. The DPs aim at both, building an environment for cross-fertilisation by creating the appropriate preconditions (DP1–3), and assessing cross-fertilisation (DP4). Building an environment for cross-fertilisation mostly centres around knowing what is being contributed and who is contributing so if a perspective is missing the facilitator can reach out and try to bring it to the table. The DGs are more detailed; either based on insights from literature or previous crowdsolving endeavours (identified via the interviews) and guide the implementation of the DPs.

## 4.1. Encourage participation

Inactive participants do not contribute to solving problems. Without interaction between participants, cross-fertilisation cannot take place [55,74]. Thus, active participants are crucial to any crowdsolving endeavour, however, encouraging participation is a challenge [70,75,76]. Information about activity is essential for the facilitator, who can monitor and manage the participants' activity and, potentially, intervene (i.e., send a reminder) if, for example, not enough participants are actively contributing [41,70]. Measuring activity also makes it possible to observe patterns of exchange [77] and identify lead users [78], which may provide further valuable insights for improving the crowdsolving endeavour. Furthermore, with knowledge of the participants' professional backgrounds, the facilitator can assess whether participants have contributed perspectives from all relevant areas based on their knowledge of their professional background. When this is the case, a prerequisite for cross-fertilisation is fulfilled. We define activity as posting, commenting, liking, or voting for contributions, which are typical functionalities on crowdsolving platforms (e.g., Climate CoLab, OpenIDEO, etc.). In short, the tool should assess the participants' activity, which is important information for the facilitator. Thus:

## DP 1: Track participants' activity.

Crowdsolving activities usually have multiple phases and types of activity [19], which are of interest for the facilitator both on a detailed and aggregated level. Assessing detailed data on activity per phase later enables Drill-Up operations (DG1.1). In addition, activity data can be condensed by calculating KPIs like active participants, comments per participants, etc. to get an impression of the activity level within the crowd (DG1.2). Activity might not always be tracked on crowdsolving platforms. In this case, the facilitator would need to manually collect information about activity, which would be a time-consuming process, prone to errors, and not scalable – consequently a tool ideally auto matically extracts and processes the activity data (DG1.3). Although activity tracking itself does not provide the facilitator with novel information, enriching the report with background information about the participants (e.g., profession, country, etc.) enables OLAP-like operations to extract insights and thus enables targeted facilitation actions fo sub-groups (DG1.4) (Table 1) [70].

![](/api/attachments/PMMRCDWH/fulltext/images/311bb2e14d700d3c312009ade6587e2edacad0478241a385213521a4ec515cf8.jpg)  
1:n broadcasting on site actions { individual messaging  
Fig. 1. Facilitation actions in a crowdsolving endeavour.

Table 1  
Design guidelines for tracking participants' activity.

<table><tr><td>Design principle</td><td>Supporting literature</td><td>Design guidelines</td></tr><tr><td>DP 1: Track participants&#x27; activity</td><td>[41,75,76]</td><td>DG1.1: Record activity data and calculate statistics by phase and type of activity per participantDG1.2: Aggregate activity into relevant KPIsDG1.3: Automatically extract activity dataDG1.4: Enrich activity statistics with background information</td></tr></table>

## 4.2. Ensure focus of participants

In contrast to numerous advantages of crowdsolving, a few chal lenges need to be tackled to make crowdsolving, respectively crowd sourcing in general, successful. In particular, the vast amount of het erogeneous content creates a problem of attention, both on the facilitator's and on the participants' side [70,79]. In order to properly contribute, participants need to be up-to-date on existing content on a crowdsolving platform and remain focused, which falls under the facilitator's responsibility [61,70,76]. Redundancy can be a problem, particularly towards the end of multi-stage processes when participants use content generated in earlier phases [21,70]. If there is too much content, the participants may experience cognitive overload, feel overwhelmed, and have dificulty contributing. As a result, the quality of the process and the potential for cross-fertilisation can sufer in later phases [30]. In a similar vein, the facilitator is eager to receive the “right” amount of contributions. The facilitator will later synthesise the contributions to provide a collective opinion. While a minimum amount of valuable contributions is necessary to provide a certain level of insight, gathering too many contributions may be counterproductive, as the efort needed to manage the heterogeneous content increases [70,79,80]. To ensure that both parties (i.e., the facilitator and the crowd) bring their limited resources to bear in the most value-adding way, it is important to reduce the redundancy of contributions [19,21]. One aspect of idea quality is rarity (i.e., non-redundancy) and, thus, reducing redundant contributions promotes the quality of the whole crowdsolving endeavour [81]. Redundancy can be tackled by applying appropriate filter mechanisms and ensuring that redundant contributions are identified and removed or consolidated as early as possible [80]. Filters include, for example, clear instructions provided to the participants [30,82], and manual monitoring and intervention by the facilitator, e.g., deleting or merging existing contributions [70]. However, a more (resource) eficient way to operationalise filtering is via automatically identifying redundancies before they are put into the system, comparing the (entered) contribution to the existing content before it is submitted [80]. Thus:

## DP 2: Assess the similarity between contributions.

Detecting duplicates via the use of keywords may not be efective because, thanks to the richness of natural language, the same can be said using diferent words, and diferent messages can be conveyed using similar phrasing. We suggest addressing this problem by comparing the semantics of contributions, for example, via natural language processing (NLP). The outcome of this assessment should be a machinereadable output, which allows comparing two contributions with each other to assess their semantic relatedness (DG2.1). Depending on the task and the aim of a crowdsolving endeavour, a threshold should be defined, which allows to manage whether nuances of a topic are desired or rather misleading [21,70]. From a practical perspective, it will be of interest to create a way to display all matches of potentially redundant contributions, as it is more eficient to screen a list of potential duplicates rather than screening the full content on the site. So the facilitator is able to easily identify and delete or merge those contributions. which rather cost valuable time without giving new insights (DG2.2) [21,30,70]. In a similar vein, a facilitator could use the same functionality to compare contributions, which are non-redundant but appear to be related by semantics (as those contributions were contributed in diferent content categories potentially existing and/or emerging in crowdsolving endeavours) (DG2.3). This builds upon the concept of remixing, bringing up new connections between topics. Ideally, deletion of redundant contributions is not the task of the facilitator but a presumably intelligent technical artefact, which identifies and deletes irrelevant or duplicate contributions [21]. Alternatively, the crowdsolving platform implements filter mechanisms which involve the par ticipants into the process of avoiding redundant contributions, so there is not ex-post assessment, but redundant contributions are not even entered into the system (DG2.4) (Table 2) [80].

## 4.3. Keep participants up to date

Time is a constraint for both facilitators and participants. Section 4.2 outlines that irrelevant contributions do cost time. Getting an overview of the topics being discussed costs time, too [70,79]. It is in the facilitator's interest to summarise the content and guide the process, so the participants are able to bring their perspectives to bear [61,70,76,83]. One way to summarise is by aggregating content so it can be accessed and prioritised more easily [19,21,70]. Another is linking or merging of contributions, which are thematically similar (but not redundant). This type of summarising is an important means of assessing the wisdom [34,84] and intelligence [44–47] of the crowd.

Table 2  
Design guidelines for the assessment of semantics.

<table><tr><td>Design principle</td><td>Supporting literature</td><td>Design guidelines</td></tr><tr><td>DP 2: Assess the similarity between contributions</td><td>[19,21,30,79,80,81]</td><td>DG2.1: Assess the semantic similarity of pairs or larger sets of contributions (and define similarity threshold)DG2.2: Provide a list of pairs/sets of potentially redundant contributions (i.e., similar contributions from the same category)DG2.3: Provide a list of similar contributions (i.e., from different categories)DG2.4: Help participants to avoid redundancy when submitting their contributions</td></tr></table>

Keeping participants up-to-date on the main discussion streams enables them to join the discussion at any point, introducing other/new perspectives and increasing the potential for cross-fertilisation [61,76]. Aggregation is also important for the facilitator, as it allows handling many contributions and identifying the topics participants are talking about [70,80]. The facilitator is then able to intervene if a particular (apriori known) topic is absent from the discussion and to otherwise enrich the process. Aggregation can be operationalised in two ways. One method is to link all the contributions which belong together and then process them as a whole (e.g., all of the individual contributions in a group are either eliminated or promoted) [30]. The other method is to merge similar contributions to produce one that represents them all. However, great manual efort is needed to group contributions and identify commonalities between them [70]. Depending on the use-case, diferent levels of granularity are required [21], which of course impacts the extent to which contributions will be aggregated. This can involve anything from the selective combination of specific contributions to the assignment of contributions to a few main topics. Thus:

DP 3: Group thematically linked contributions and identify the to pics of the resultant groups.

In analogy to redundancy detection, grouping might be necessary at diferent levels of granularity. Hence, the facilitator seeks for ways to be flexible in creating groups of related contributions. A tool should support this end by making multiple suggestions (DG3.1) [21,70]. From a practical point of view, the facilitator might still want to overrule the tool's suggestion. Thus, it could be reasonable to allow manual intervention with regards to the grouping outcome (DG3.2) [21,70]. Finally, to grasp the gist of what is being discussed, it is not enough to simply group together contributions, but the facilitator will be interested in the topic(s) presented in one group of contributions, which then again helps to guide the endeavour and to encourage other perspectives (DG3.3) (Table 3) [61,70,76,83].

## 4.4. Encourage broad thinking

In terms of enabling and fostering cross-fertilisation the most important task of the facilitator is to encourage and support multiple perspectives and divergent thinking [70,76,85,86]. Hence, an indicator of cross-fertilisation is the diversity and number of perspectives accounted for by a single contribution or within one stream of discussion. With increasing heterogeneity of participants with respect to, for ex ample, their disciplinary background the barriers to collaboration increase, yet so do the potential benefits of cross-fertilisation [55]. The result is that, for cross-fertilisation to take place, cross-disciplinary community building is necessary [56]. To assess whether cross-disciplinary communities are forming, the facilitator needs to assess which knowledge domains respectively perspectives are represented in the contribution. Thus:

## DP 4: Assess the knowledge domains captured by contributions.

Section 4.3 highlights that extracting the topics from the contribu tions is important. On a broader scale, topics are potentially too narrow. The facilitator is interested in around which knowledge domains a discussion is turning (e.g., sustainability, information technology, etc.). Consequently, instead of assessing such information manually, the facilitator seeks for an automated way to assess from which perspectives a topic is being discussed (DG4.1) [70]. In order to automatically assess such information, the perspectives, which will be covered, need to be anticipated respectively predefined. Two sets of knowledge domains are relevant. First, the set of domains, which are relevant for the given task respectively the wicked problem (e.g., for climate change; sustainability, policy, etc.) (DG4.2). Second, the set of domains, which parti cipants bring into the discussion, i.e., their (professional) backgrounds (DG4.3). Finally, as one of the main goals of the facilitator is to foster cross-fertilisation, the facilitator will observe how the knowledge domains covered over time will develop (DG4.4) (Table 4).

## 5. Artefact evaluation

Evaluation is an important step of DSR. We present the criteria re levant for the evaluation in Section 3. In particular, we will outline that the presented DPs and DGs support facilitators in fostering cross-fertilisation and to emphasise the broad applicability of our design, we exemplarily discuss three use cases of crowdsolving platforms, the Climate CoLab, OpenIDEO and the FCL. For all three cases, we argue from a qualitative perspective that the proposed design would be applicable and of value to the facilitator of these platforms. In addition, we developed a prototypical instantiation that helped to demonstrate the feasibility of the design and supported an in-depth analysis of our design for the case of the FCL from a quantitative and a qualitative perspective. Details on the implementation of the prototype and its evaluation are available upon request.

## 5.1. Use case #1: climate CoLab

The Climate CoLab (CCL) [1,2,87] has a community of > 120,000 people from all around the world participating in online contests that seek proposals about actions that might be taken to address specific aspects of the problem of global climate change (e.g., increasing building eficiency or decarbonising electricity production). Participants can comment or like the proposals submitted by others. After submission, a recruited panel of experts reviews the proposals and selects semi-finalists. The semi-finalists then may revise their submissions and the judges select the finalists. Afterwards, the judges select the winner of the Judges' Choice Award and the community votes to select the winner of the Popular Choice Award. In addition to running contests in specific domains, the Climate CoLab has also used contest webs, in which integrated proposals are sought that combine entries from earlier contests [1]. In that particular case, cross-fertilisation is essential as the quality of contributions emerges when multiple perspectives are considered in an integrated way [87].

An instantiation of our DGs would help the facilitators of the Climate CoLab to foster cross-fertilisation. First, a functionality to track activity (DP1) would be, regardless of whether cross-fertilisation is a major goal or not, a baseline functionality. Facilitators could use it to check how actively participants contribute to the CCL. Second, as anyone is able to contribute to the CCL and the first phase is usually a “sourcing” phase, the entries need to be validated among others in the sense that redundancies need to be removed (DP2) [19,88]. By design of most contests, value is generated by one single best solution; consequently, a matching of contributions (DG2.3) might not be relevant in terms of processing contributions [88]. But because participants are able to join forces by forming teams, such functionality could help them to find the right partner to create a powerful team [70]. Third, clustering of contributions (DP3) seems not to be relevant in the “consolidation” phase, since in the CCL single contributions are being judged [19,70]. However, the facilitation team might have a need to keep track of all topics and potentially promote contributions from certain tracks. In such a case, the judges' selection of (semi-) finalist could be supported by a thematic clustering (DG3.2) of the contribu tions, or at least a list of topics (DG3.3), to address various tracks more equally [2]. Finally, although the evaluation criteria for the contests difer with regards to what the winning contribution should outline, generally the purpose of the CCL is to harness the collective intelligence from people all over the world [87]. In this realm, cross-fertilisation plays an important role, so regardless of the winning contribution in the current contest, the CCL has an interest in participants that cross-fer tilise and create better ideas even though it might only afect future contributions [70,87]. As a result, the facilitation team of the CCL should also monitor the addressed knowledge domains over time (DP4).

Design guidelines for grouping of contributions.

<table><tr><td>Design principle</td><td>Supporting literature</td><td>Design guidelines</td></tr><tr><td>DP 3: Group contributions which are thematically linked and identify the topics of these groups</td><td>[21,30,61,76,79,80]</td><td>DG3.1: Provide suggestions of clusters, accounting for multiple levels of detailDG3.2: Provide suggestions for groups of contributions, which are easily rearrangeableDG3.3: Identify topic(s) in content groups</td></tr></table>

3. Disruptions in Phase 2 were reordered based on topic and then voted on  
Table 4  
Design guidelines for the assessment of knowledge domains.

<table><tr><td>Design principle</td><td>Supporting literature</td><td>Design guidelines</td></tr><tr><td>DP 4: Assess the knowledge domains captured by contributions</td><td>[56,61]</td><td>DG4.1: Indicate the extent to which knowledge domains are represented per contributionDG4.2: Define a set of knowledge domains relevant to the given taskDG4.3: Define a set of knowledge domains based on participants&#x27; backgroundsDG4.4: Assess knowledge domains covered over time</td></tr></table>

Altogether, our DPs could create value in running the CCL by creating an environment for cross-fertilisation and the assessment of it. Although cross-fertilisation might only be a secondary goal in the CCL, it does not contradict the primary goal of eliciting good ideas from people from all around the world. Rather, cross-fertilisation supports the primary goal, as participants in the CCL are refining their contributions over the course of the contest and, thus, incorporating further perspectives from others (via discussions, collaboration, etc.) helps to mature the contributions so they become better. In particular, when contests build upon each other [1,70].

In addition, the functionalities that result from the DPs and DGs could not only help facilitators but also participants. Finding a related comment on a diferent contribution or grouping contributions on related topics could help picking up relevant perspectives to connect participants, which hopefully sparks cross-fertilisation [70].

## 5.2. Use case #2: OpenIDEO

The collaborative design network OpenIDEO is another web plat form that relies on a contest model. Participants aim to solve an outlined challenge, usually via a five-phase process, which involves initial research, the contribution of ideas, the refinement of ideas, the provi sion of feedback, and the evaluation of top ideas. During the process, participants can post and respond to comments on the submitted concepts, which fosters interaction [89,90]. Overall, the default process on OpenIDEO is comparable to the one on the CCL. Consequently, the arguments we brought up for the CCL are also valid in the context of OpenIDEO, and an instantiation of our DPs and DGs could help to create an environment for cross-fertilisation and help to assess it on Open-IDEO.

OpenIDEO does not host contest webs as the CCL does. Nevertheless, some of the hosted contests encompass an inspiration phase in which the participants primarily research, question, and explore a topic without generating ideas [91,92]. This initial step of the process aims at cross-fertilisation in the sense that participants become aware of the facets of a topic. They get a feeling for where to bring in their perspective and have the chance to discuss with others [91]. Especially in this scenario, a tool implementing our design could help to create an environment for cross-fertilisation.

## 5.3. Use case #3: Futures CoLab

The FCL hosts a process for asynchronous and facilitated dialogue among a network of diverse international experts on a crowdsolving platform. The goal of Futures CoLab is to enable subject matter experts to collectively explore solutions to global systemic challenges. The crowdsolving platform is developed by MIT CCI and run in cooperation with Future Earth (an international non-profit organisation whose mission is to accelerate transformations to global sustainability through research an innovation [93]). In contrast to the CCL or OpenIDEO, Future Earth is seeking numerous insights concerning their research, not just one top contribution. In the case we use here as an example, the FCL invited 181 participants to contribute ideas about potential systemlevel changes which might enhance global sustainability. In addition to encouraging innovative contributions, the secondary goal was to encourage collective learning among the participants, who were recruited via Future Earth's network and were professionally and geographically diverse. They contributed during a three-phase process of the type commonly used in crowdsolving platforms, depicted in Fig. 2 [19]. The overall process took three weeks. For screenshots of the platform, please refer to the Appendix (Fig. 3, Fig. 4, and Fig. 5). Throughout, the facilitator (employee of Future Earth) stayed in touch with the participants via e-mail, sending updates, summaries, etc. several times each week. In the aftermath of the process, an advisory board of selected senior researchers evaluated the innovative potential and impact of the top contributions, which served as input for workshops aiming to define a research agenda to accelerate the transformation towards global sustainability.

![](/api/attachments/PMMRCDWH/fulltext/images/28b2de3f97248498a52f11ab270752fdefaa43aaf901dcc815845c994763bf6c.jpg)  
Fig. 2. Process description of FCL.

Phase 1 involved brainstorming: Participants were asked to identify (a) systems which prevent society from shifting to a sustainable and equitable path (three categories: political-economic, technology and infrastructure, and cognitive socio-cultural) and (b) disruptions which have occurred in the past or are on the horizon (three categories: political economic, technological, and other). Participants' contributions consisted of a compulsory title, a tweet-length description of the idea, and an optional full description. Participants could also comment on or “like” contributions. In this phase, participants identified 92 systems (which collectively solicited 175 comments and 256 likes; example: “air transportation systems”, for details see Table 6) and 80 disruptions (81 comments and 171 likes; example: “direct democracy”, for details see Table 6). At the end of this phase, the facilitation team, with the help of our prototype, sorted the 92 systems into 13 groups, which reflected the gist of the contributions therein.

Phase 2 involved refining and developing the contributed content. Participants were asked to suggest disruptions, which might resolve the inertia that maintains unsustainable systems. This resulted in 71 contributions (with 142 comments and 205 likes; example: “real accounting of environmental externalities”, for details see Table 6). Participants were invited to connect their contributions to – and thus enrich – one of the 13 groups from Phase 1. This step, however, was optional.

In Phase 3, participants were asked to identify promising contributions from Phase 2. Participants voted for the disruptions most likely to enable transformations towards sustainability (each participant had up to 15 votes, with a maximum of 5 per contribution), and were also invited to further discuss their opinions in the comments (total of 141 comments and 903 votes, for details see Table 6).

Generally, similar arguments as for the CCL and OpenIDEO apply to the FCL. The biggest diference between the FCL and the other two platforms is the fact that the FCL does not seek for a single best contribution, rather for a set of interesting and novel thoughts. Consequently, the focus is less on refining single contributions to a mature state, rather considering a subset of contributions as a whole and discussing thoughts. Therefore, the FCL is predestined for fostering cross-fertilisation. In contrast to the CCL and OpenIDEO, especially DP2 is of interest as it enables to further develop and connect ideas of participants, besides the aforementioned arguments with regards to content aggregation, etc.

In addition to a qualitative evaluation how our DPs and DGs would also help the facilitators of the FCL, we exemplarily instantiated our DPs and DGs and apply our prototype in a real-world setting. In particular, we evaluate whether the instantiation of the DP's is suitable for use in a live crowdsolving endeavour, rather than merely ex-post. The problem-solving process on the FCL was supported by a five-person facilitation team (led by Future Earth) consisting of one experienced main facilitator, two assistants and two authors of this paper, of which one had led several former crowdsolving endeavours. The prototype regularly processed the input from the FCL. The tool's output was collated by one of the authors and presented in a comprehensive report to the other members of the facilitation team. In future applications, this process could also be fully automated [21]. During a daily call with all members of the facilitation team overseeing the process, the insights from the reports were discussed and conclusions about the facilitation actions were drawn. In the aftermath of the 3-week process, we interviewed the head of the facilitation team, who is not an author of this paper, to ensure our evaluation reflected the facilitator's point of view. In order to gather more feedback, a survey evaluating the overall process was sent out to the participants. In addition to qualitative judge ments, we analysed quantitative metrics.

When cross-fertilisation occurs, the results should be apparent. It should be evident in the development of their contributions that participants have incorporated other perspectives into their thoughts (DG4.4). Consequently, we expect that, over time, contributions will relate to more knowledge domains. In our case, we defined seven knowledge domains we anticipated to be discussed (for detailed list refer to Appendix) and ran during the process a classifier trained to assess the prevalence of a knowledge domain in each contribution and return a value between 0% (not at all represented) and 100% (fully represented). All of the label values can be added up to represent the Overall Fit (OF) of the contribution to the entire set of labels (in our case, adding up to a possible maximum of 700%, indicating full representation of all seven knowledge domains, for details see Table 6). Two examples make the OF measure more tangible: A contribution from Phase 1 at the lower end of the OF (\~120%) was very specific and exclusively addressed the IT domain “Artificial intelligence and advances in machine learning”. In contrast, a contribution from Phase 2 covered a broader scope (OF \~ 310%), addressing earth science, IT, and sustainability “multi-scale, transparent, streaming ecosystem and biodiversity monitoring.” In the survey sent out at the end of the process, a question included a 5-point Likert scale to rate the seven contributions which drew the most votes. These were evaluated according to four criteria: impact. novelty. feasibility, and scope. The latter reflects the extent of a contribution's disruptive potential, which may be limited to a particular niche (narrow scope) or wide-ranging (broad scope). The OF of the entire set of labels should reflect this dimension. When we compared the OF of the contributions with the survey's appraisal of the scope, we observed a correlation of 91% between the two measurements. As the labels were the foundation for the following analytical evaluation, this gives credibility to the assigned labels.

As we expect that over time people cross-fertilise, they incorporate more perspectives into their thoughts and thus the OF should increase over time. To test for this, we ran a simple linear regression. We modelled the day of the process (i.e., the first day of the process as “day 1”) as the independent variable and the OF as the dependent variable. We observed an increase in the OF over time. The estimate for the time is 1.4% (p-value 0.031, intercept 204%). This means that the average OF of contributions increased day by day, indicating that the participants were thinking in broader terms. Near the beginning of the process, the average OF of a contribution was around 200%, whereas, towards the end, the average exceeded 230%. This makes sense, as later contributions were presumably informed by more discussions, which would have encouraged cross-fertilisation.

We found further evidence to support this claim. Comparing the labelling from the authors' original text with their final text in the contribution (including comments), we also observed significant differences, as a Wilcoxon-signed rank test reveals (p-value < 0.001). For example, in a contribution concerning the development of improved data and analytical tools as a means to better understand systems (labelled as IT), a participant added his thoughts on policy implications, which enriched the discussion and brought more perspectives to the table. Further investigation of the entire text of a contribution, including the comments, using another linear regression revealed that the comments did significantly increase the OF (estimate of 3.6% and pvalue of 0.002). In this case, the OF of the final contribution was the dependent variable, and the number of comments was the independent variable. The OF increased over time, and the comments contributed to this increase. While, at a single point in time, the OF does not necessarily convey information about the level of cross-fertilisation, the development of the OF over time does. Hence, it is this development that the facilitator should monitor (DG4.4).

In the aftermath of the process, participants reported in an online survey that they had learned something from other participants, engaged with persons they would not normally have engaged with, and benefited from the variety of perspectives. Together with the quanti tative indications, these statements suggest that cross-fertilisation occurred. Our DP's provide guidance to facilitators how to foster and measure cross-fertilisation and we fulfil our meta-requirement.

## 6. Discussion

## 6.1. Contribution

Our research proposes a design for a facilitation support tool that helps in fostering cross-fertilisation in a crowdsourcing (and particularly crowdsolving) context. By applying DSR, we identified four design principles (DPs) and 15 more detailed design guidelines (DGs) for a tool to support the facilitator of a crowdsolving system to (a) set the boundary conditions for, (b) measure, and (c) facilitate cross-fertilisa tion. For evaluation, we first assessed the design's applicability and value for two crowdsolving platforms on an argumentative basis from the outside. Then, we developed a prototypical instantiation of our design. The prototype used Natural Language Processing (NLP) for purposes such as redundancy detection, content clustering, and topic identification (DP2–4). We applied this prototype in the facilitation of a three-week real-world crowdsolving task with 181 participants. Feedback from the facilitation team (two of five members of that team at authors of the present paper), ex-post survey data from the crowd members, and quantitative analyses of the digital trace data that emerged on the crowdsolving platform support efectiveness, eficiency, and impact on the user's environment of the prototype. We found way to encourage cross-fertilisation between diverse participants. Further, we demonstrated that cross-fertilisation can be observed over time and is of interest to the facilitator of a crowdsourcing endeavour as it improves the quality of results. Specifically, we developed a metric that allows the facilitator to monitor the scope of the online dialogue, in dicating whether participants are able to anticipate other/more perspectives. As Charles Darwin earlier revealed, cross-fertilisation occurs naturally but facilitating enables us to reach a “desired” state sooner. In our context, the gradient of the OF over time indicates whether, and to what extent, cross-fertilisation is taking place. In the aftermath of the process, the head of the facilitation team outlined the “advantage of combining human and machine learning” [94] with regards to the prototype which incorporated our design. Cumulatively, these evaluation steps suggest that the design is easy to use, eficient, generalisable, and operationalisable.

Table 6  
Descriptive statistics of participation in the FCL.

<table><tr><td></td><td>Overall</td><td>Phase 1</td><td>Phase 2</td><td>Phase 3</td></tr><tr><td colspan="5">Contribution length (in words)</td></tr><tr><td>Max</td><td>477</td><td>401</td><td>477</td><td>-</td></tr><tr><td>Min</td><td>17</td><td>19</td><td>17</td><td>-</td></tr><tr><td>SD</td><td>86</td><td>83</td><td>97</td><td>-</td></tr><tr><td>Average</td><td>100</td><td>98</td><td>105</td><td>-</td></tr><tr><td colspan="5">Overall Fit (OF) of contributions</td></tr><tr><td>Max</td><td>341%</td><td>318%</td><td>341%</td><td>-</td></tr><tr><td>Min</td><td>113%</td><td>113%</td><td>120%</td><td>-</td></tr><tr><td>SD</td><td>45%</td><td>45%</td><td>44%</td><td>-</td></tr><tr><td>Average</td><td>211%</td><td>207%</td><td>219%</td><td>-</td></tr><tr><td colspan="5">Comment length (in words)</td></tr><tr><td>Max</td><td>505</td><td>383</td><td>505</td><td>421</td></tr><tr><td>Min</td><td>2</td><td>3</td><td>2</td><td>5</td></tr><tr><td>SD</td><td>69</td><td>60</td><td>63</td><td>83</td></tr><tr><td>Average</td><td>78</td><td>70</td><td>69</td><td>102</td></tr><tr><td colspan="5">Participation</td></tr><tr><td>Contributions</td><td>243</td><td>172</td><td>71</td><td>-</td></tr><tr><td>Comments</td><td>539</td><td>256</td><td>142</td><td>141</td></tr><tr><td>Likes</td><td>632</td><td>427</td><td>205</td><td>-</td></tr><tr><td>Votes</td><td>903</td><td>-</td><td>-</td><td>903</td></tr><tr><td>Active participants</td><td>103</td><td>83</td><td>70</td><td>70</td></tr></table>

Gregor and Jones [71] suggest that a design theory should consist of eight components. In Table 5, we list specific components relating to knowledge about design originating from this study. This design knowledge is the core theoretical contribution if the present paper.

Beyond this, the facilitator of the FCL process mentioned that now that she is used to the tool and familiar with its capabilities she could imagine that, rather than simply using the tool as additional support for her facilitation actions, she could design further problem-solving processes around the tool in order to fully leverage its potential. Yet, our tool is not only of practical use in research focused on finding solutions to wicked problems. It will also assist organisations that employ crowdsourcing in ideation competitions or open innovation, wherein cross-fertilisation is desirable. In terms of filter design, the instantiation of DP3 which allows processing several contributions as a whole is of particular interest. The prototypical implementation of the NLP cap abilities we present (namely redundancy detection, content clustering, topic identification, and text labelling) may also hold value in context where practitioners need to monitor and process vast amounts of het erogeneous context. Examples include monitoring reviews of, or complaints about, products via online social networks.

Table 5  
Eight components of an information systems design theory [71] and their specific manifestations in this study.

<table><tr><td>Component</td><td>Description</td></tr><tr><td>Purpose and scope</td><td>Support intelligent decision-making aiding facilitators of crowdsolving for wicked problems in fostering and managing cross-fertilisation in their crowds.</td></tr><tr><td>Constructs</td><td>Relating to purpose and scope: Facilitation, cross-fertilisation, crowdsolving, wicked problems.Relating to the design principles: Semantic embedding, platform activity, NLP.Relating to the tool&#x27;s functionalities: Redundancy detection, content clustering, topic identification, text labelling, activity tracking.</td></tr><tr><td>Principle of form and function</td><td>We provide four design principles (DPs) and 15 design guidelines (DGs) for a tool, which enables and enriches facilitation actions during a crowdsolving endeavour thus fostering cross-fertilisation among participants.</td></tr><tr><td>Artefact mutability</td><td>Depending on how a platform runs the problem-solving process, the functionality of the tool needs to be tailored, which has implications on the instantiation.</td></tr><tr><td>Testable propositions</td><td>Implementing the DPs leads to increased efficiency and effectiveness in facilitating cross-fertilisation in crowdsolving.</td></tr><tr><td>Justificatory knowledge</td><td>Extant knowledge of facilitation, cross-fertilisation, crowdsourcing, collective intelligence, and wicked problems.</td></tr><tr><td>Principles of implementation</td><td>IT systems implementing the DPs and DGs can be built based on statistical, machine learning and Natural Language Processing (NLP) techniques that operate on digital trace data from the IT platform supporting a crowdsolving exercise.</td></tr><tr><td>Expository instantiation</td><td>A prototypical instantiation of the abstract design has been applied in facilitating crowdsolving and achieving cross-fertilisation.</td></tr></table>

## 6.2. Limitations and further research

Our study involves some limitations, which we hope will stimulate further research. Firstly, as we did not run A/B or comparable tests, we were unable to disentangle the efects of the tool's individual compo nents including the process itself, which was predefined. What is more, as cross-fertilisation between participants also occurs without facilita tion, we are unable to make any claims about the extent to which the tool or the facilitator is responsible for the cross-fertilisation we ob served. Nonetheless, qualitative feedback from facilitators suggests that the support provided by the tool was of great value to them and, as the tool fulfils the MR, it also fulfils our design objective. Future research might analyse the efectiveness of single DPs and DGs, or the design as a whole, by running multiple comparable crowdsolving processes (in parallel). Secondly, our assessment of cross-fertilisation is not suitable for comparing processes with one another due to the variability of participants, goals, knowledge domains and the time horizon, which will presumably require diferent labels and produce diferent OF gra dients over time. Thirdly, in terms of cross-fertilisation, we expect the OF will meet its upper limit when the process exceeds a certain duration, so a facilitator will not always observe an increase in the OF even though cross-fertilisation continues. In this case, a more sophisticated measure of cross-fertilisation is necessary. Since we did not have any information on how often participants logged in or which discussion thread they followed, we had to assume cross-fertilisation happened over time. Future research might address this issue, identifying whether certain participants, which e.g. login more often, cross-fertilise more than others do and which other factors are involved. Fourthly, our prototypical way of identifying diferent knowledge domains cannot detect the extent to which ideas and concepts from diferent knowledge domains are discussed in parallel or synthesised to form comprehensive concepts. To this end, we assume that, at least in the FCL, either the facilitator or other participants would ask for or provide further explanation when concepts are insuficiently integrated, which would then lead to actual cross-fertilisation. Fifthly, the amount of noise generated during a crowdsolving process, as we have described it, does depend on the expert knowledge of the participants in the given context. Cross-fertilisation, therefore, might be more favourable for generalist tasks, whereas for specialist tasks it presumably leads to more noise. Nonetheless, even in specialist tasks, cross-fertilisation may be the foundation for disruption but future research is necessary to explore ways to explicitly foster cross-fertilisation in specialist tasks. Finally, we only evaluated a prototypical instantiation of the design in a single crowdsolving exercise.

## 7. Conclusion

Cross-fertilisation is a crucial mechanism, which increases the probability of high-quality ideas emerging in problem-solving or ideagenerating exercises. This paper establishes four design principles and 15 design guidelines for a decision-support tool for facilitators of crowdsolving endeavours, who must make decisions about facilitation actions intended to foster cross-fertilisation among participants. Our design principles and guidelines are prototypically operationalised by NLP, which lets the facilitator handle the vast amount of input they receive. In order to evaluate our design, we analysed three crowdsolving platforms and applied an instantiation of the design in the context of the FCL and demonstrated the tool's ability to derive meaningful insights and actionable input which support the facilitator and indirectly contribute to solving wicked problems.

## CRediT authorship contribution statement

Henner Gimpel: Conceptualization, Methodology, Supervision, Writing - review & editing. Valerie Graf-Drasch: Investigation, Validation, Writing - original draft, Writing - review & editing. Robert J. Laubacher: Conceptualization, Investigation, Resources, Supervision, Writing - review & editing. Moritz Wöhl: Formal analysis, Investigation, Software, Visualization, Writing - original draft.

## Acknowledgments

We are grateful for funding and support from the German Research Foundation (project 343128888).

## Appendix A

## Appendix

Identified knowledge domains from participants and corresponding keywords used to obtain training data.

<table><tr><td>Knowledge domain</td><td>Business/economics</td><td>Earth sciences/energy</td><td>IT</td><td>Natural sciences</td><td>Policy</td><td>Society</td><td>Sustainability</td></tr><tr><td rowspan="7">Keywords</td><td>Business</td><td>Earth sciences</td><td>Artificial intelligence</td><td>Biology</td><td>Legislation</td><td>Culture</td><td>Climate change</td></tr><tr><td>Economics</td><td>Earth systems</td><td>Computer science</td><td>Chemistry</td><td>Policy</td><td>Philosophy</td><td>Ecology</td></tr><tr><td>Finance</td><td>Energy</td><td>Data</td><td>Engineering</td><td>Politics</td><td>Social sciences</td><td>Global warming</td></tr><tr><td>Management</td><td>Geography</td><td>Distributed ledger technology</td><td>Nanotechnology</td><td></td><td>Society</td><td>Sustainability</td></tr><tr><td></td><td>Geology</td><td>Information technology</td><td>Physics</td><td></td><td>Sociology</td><td></td></tr><tr><td></td><td>Resources</td><td>Technology</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Water</td><td></td><td></td><td></td><td></td><td></td></tr></table>

These keywords were used to extract texts from Wikipedia articles, which were then used to train the classifier that assessed the prevalence of knowledge domains in the contributions (see Section 5.3).

<table><tr><td>Futures CoLab</td><td>About</td><td>Previous activity</td><td>Participate</td><td>Community</td><td>SEARCH</td><td>HELP</td></tr></table>

## Go to Contest Management Tool

## Categories

Below are some guiding questions for each of the three weeks to provoke your thinking and spark a dialogue on potential disruptions that could steer society toward enhanced sustainability and equity. The outcomes of this exercise will be used to develop a Research and Innovation Agenda to help galvanize needed investments around these issues

![](/api/attachments/PMMRCDWH/fulltext/images/63ce14ceaf44e56d492edc112bae1347a6f54fc0404e481a6aea895826f1f638.jpg)

## Week 3: Voting on disruptions

Which disruptions from Week 2 have the highest potential to positively impact progress toward sustainable and equitable development around the world?

Closed

![](/api/attachments/PMMRCDWH/fulltext/images/f35a713362025649552b62726ad1c1fae4a131d34d755e60dee4529c3426da04.jpg)

## Week 1: Political economic systems

What major political economic systems are sustaining our unsustainability?

Closed

![](/api/attachments/PMMRCDWH/fulltext/images/6ff20d4609f46fee5b02f5503087346651f3db478166e78f1a38730fe03fde3f.jpg)

![](/api/attachments/PMMRCDWH/fulltext/images/1a1348178a36db273af1491a7a5013db0fe7ae9231c0aa4bec1cb6391dc70eb3.jpg)

## Week 1: Technology and infrastructure systems

What major technological or infrastructural systems are sustaining our unsustainability?

Closed

![](/api/attachments/PMMRCDWH/fulltext/images/05a2d4c1d30554f951d54ef18368ac59a6ee85bda6a1a1017ce9caba10132cde.jpg)

![](/api/attachments/PMMRCDWH/fulltext/images/138f2a37f223ca6194f6ad47897e16334b1bce09a6f1b3559ea464b1af786f51.jpg)  
Fig. 3. Landing page of the FCL.

## Week 1: Cognitive social cultural systems

What major cognitive, social, or cultural systems are sustaining our unsustainability?

## Week 1: Political economic disruptions

![](/api/attachments/PMMRCDWH/fulltext/images/1225bfccbe9ef83a681c73a4025e062d721cb2b5b5ceefbffdd336adf245e095.jpg)

What major policy-economic disruptions have taken place in the past or are on the horizon?

Closed

## Week 1: Technological disruptions

What major technological disruptions have taken place in the past or are on the horizon?

Closed

## Week 1: Other disruptions

What other disruptions have taken place in the past or are on the horizon?

Categories > Week 1: Political economic systems

## Week 1: Political economic systems

What major political economic systems are sustaining our unsustainability?

Please submit up to three ideas this week across the different categories of systems. We encourage you to think outside the box and consider systems that span boundaries and scales.

Please also comment on at least two contributions from others this week, for example providing additional thoughts to expand on or refine the contribution.

<table><tr><td colspan="2"></td><td>Export CSV</td><td>Edit Contest</td></tr><tr><td colspan="3">38 Contributions</td><td>Contribute</td></tr><tr><td>Contribution name*</td><td></td><td></td><td></td></tr><tr><td>Anti-Complexity Government and Policy Making</td><td>0</td><td>2</td><td>1</td></tr><tr><td colspan="4">The sustainability challenges we face are complex, highly interconnected and interdependent. Siloed &quot;anti-complex&quot; government structures, processes and functions only function to undermine our ability to address these issues because they fail to recognise this complex reality.</td></tr><tr><td>Capitalism</td><td>0</td><td>5</td><td>6</td></tr><tr><td colspan="4">The current capitalist system is bound up in power relationships and languages that do not allow us to think about the planet outside of financial terms.</td></tr><tr><td>Carbon Lock-In (coined by John Unruh) and overlapping pol/econ forces</td><td>0</td><td>3</td><td>0</td></tr><tr><td colspan="4">The challenge of climate change is disrupting multiple and overlapping pol/econ forces that serve to reinforce and naturalize the use of fossil energy. Seeking leverage points for disruption needs to take the layered and interdependent nature of carbon lock-in into account</td></tr><tr><td>Climate Emergency ~ isn&#x27;t this a bit pointless?</td><td>0</td><td>2</td><td>8</td></tr><tr><td colspan="4">Of course, there is an &quot;emergency&quot; but do we really think that by engaging &quot;citizens&quot; that it will make a useful difference (e.g. lowering carbon dioxide emissions)?</td></tr><tr><td>Corruption undermining the legitimacy and effectiveness of institutions</td><td>0</td><td>4</td><td>1</td></tr></table>

Fig. 4. Contribution overview after opening category on landing page in the FCL.

![](/api/attachments/PMMRCDWH/fulltext/images/fe58d585ba06d5077659cd6614a61787d64ebf4df5df8129ec83d6591d80cddb.jpg)  
Fig. 5. Contribution in FCL including comment.

## References

[1] T.W. Malone, J.V. Nickerson, R.J. Laubacher, L.H. Fisher, P. de Boer, Y. Han, W.B. Towne, Putting the pieces back together again, Proceedings of the 2017 ACM Conference on Computer Supported Cooperative Work and Social Computing, Portland, Oregon, USA, ACM Association for Computing Machinery, New York, NY, 2017, pp. 1661–1674.

[2] J. Introne, R.J. Laubacher, G. Olson, T.W. Malone, Solving wicked social problem with socio-computational systems, KI – Künstliche Intelligenz 27 (2013) 45–52, https://doi.org/10.1007/s13218-012-0231-2

[3] B.W. Head, Wicked problems in public policy, Public Policy 3 (2008) 101.

[4] J. Conklin, Dialogue Mapping, Building Shared Understanding of Wicked Problems, John Wiley & Sons, West Sussex, England, 2006.

[5] C.W. Churchman, Guest editorial: wicked problems, Management Science 14 (1967) B141-B142

[6] R. DeFries, H. Nagendra, Ecosystem management as a wicked problem, Science 356 (2017) 265–270, https://doi.org/10.1126/science.aal1950.

[7] P. Loos, W. Nebel, J. Marx Gómez, H. Hasan, R.T. Watson, J. vom Brocke, S. Seidel, J. Recker, I.T. Green, A matter of business and information systems engineering? Business and Information Systems Engineering 3 (2011) 245–252, https://doi.org 10.1007/s12599-011-0165-5.

[8] C. Yang, W. Gu, T. Ito, Toward case-based reasoning facilitation for online discussion in deliberation, 2019 IEEE 23rd International Conference on Computer Supported Cooperative Work in Design (CSCWD), IEEE, Porto, Portugal, 2019, pp. 517–523 5/6/2019 - 5/8/.

[9] T. Ito, Towards agent-based large-scale decision support system: the efect of facilitators, Proceedings of the 51st Hawaii International Conference on System Sciences, Hawaii International Conference on System Sciences, 2018.

[10] J. Howe, Crowdsourcing: Why the Power of the Crowd Is Driving the Future of Business, Three Rivers Press, New York, NY, USA, 2009.

[11] J. Howe, The rise of crowdsourcing, Wired Magazine 14 (2006) 1–4.

[12] A. Guazzini, D. Vilone, C. Donati, A. Nardi, Z. Levnajić, Modeling crowdsourcing as collective problem solving, Scientific Reports 5 (2015), https://doi.org/10.1038/ srep16557.

[13] P. Michelucci, J.L. Dickinson, Human computation: the power of crowds, Science 351 (2016) 32–33, https://doi.org/10.1126/science.aad6499.

[14] A. Potter, M. McClure, K. Sellers, Mass collaboration problem solving: a new approach to wicked problems, International Symposium on Collaborative Technologies and Systems, Chicago, IL, USA, IEEE, Piscataway, NJ, 2010, pp. 398–407.

[15] J.E. Innes, D.E. Booher, Collaborative rationality as a strategy for working with wicked problems, Landscape and Urban Planning 154 (2016) 8–10, https://doi.org 10.1016/j.landurbplan.2016.03.016.

[16] E.P. Weber, A.M. Khademian, Wicked problems, knowledge challenges, and collaborative capacity builders in network settings, Public Administration Review 68 (2008) 334–349, https://doi.org/10.1111/j.1540-6210.2007.00866.x.

[17] N. Roberts, Wicked problems and network approaches to resolution. International Public Management Review 1 (2000) 1–19.

[18] H. Zhu, A. Kock, M. Wentker, J. Leker, How does online interaction affect idea quality? The efect of feedback in firm-internal idea competitions, Journal of Product Innovation Management 36 (2019) 24–40, https://doi.org/10.1111/jpim 12442.

[19] M. Rhyn, I. Blohm, Patterns of data-driven decision-making: how decision-maker leverage crowdsourced data, 40th International Conference on Information Systems, Munich, 2019.

[20] R. Sharma, S. Mithas, A. Kankanhalli, Transforming decision-making processes: a research agenda for understanding the impact of business analytics on organisa tions, European Journal of Information Systems 23 (2014) 433–441, https://doi. org/10.1057/ejis,2014.17.

[21] M. Rhyn. I. Blohm. Combining collective and artificial intelligence: towards a design theory for decision support in crowdsourcing, 25th European Conference on Information Systems, Guimarães, Portugal, 2017, pp. 2656–2666.

[22] About Futures CoLab, Futures CoLab, 2019, https://futurescolab.org/page/about , Accessed date: 17 April 2017.

[23] D. Geiger, M. Rosemann, E. Fielt, M. Schader, Crowdsourcing information systemsdefinition typology, and design, 33rd International Conference on Information Systems, Orlando, FL, 2012.

[24] P. Checkland, Systems Thinking, Systems Practice, Wiley, Chichester, 1981

[25] R. Knapp, Wholesome design for wicked problems, The Public Sphere Project 15 (2008).

[26] M. Pacanowsky, Team tools for wicked problems, Organizational Dynamics 23 (1995).36–51. bttps://doi org/10.1016/0090-2616(95)90024-1

[27] W. Ketter, M. Peters, J. Collins, A. Gupta, Competitive benchmarking: an IS research approach to address wicked problems with big data and analytics, SSRN Journal (2015), https://doi.org/10.2139/ssrn.2700333.

[28] H.W.J. Rittel, M.M. Webber, Dilemmas in a general theory of planning, Policy Sciences 4 (1973) 155–169, https://doi.org/10.1007/BF01405730.

[29] I. Blohm, U. Bretschneider, J.M. Leimeister, H. Krcmar, Does collaboration among participants lead to better ideas in IT-based idea competitions? An empirical investigation, 43rd Hawaii International Conference on System Sciences, Honolulu, Hawaii, USA, IEEE, Piscataway, NJ, 2010, pp. 1–10.

[30] M. Klein, A.C.B. Garcia, High-speed idea filtering with the bag of lemons, Decision Support Systems 78 (2015) 39–50, https://doi.org/10.1016/j.dss.2015.06.005.

[31]. R. Weber, Ontological Foundations of Information Systems. Coopers & Lybrand and the Accounting Association of Australia and New Zealand. 1997.

[32] P. Tatham, L. Houghton, The wicked problem of humanitarian logistics and disaster relief aid, Journal of Humanitarian Logistics and Supply Chain Management 1 (2011) 15–31, https://doi.org/10.1108/20426741111122394.

[33] L. Hong, S.E. Page, Groups of diverse problem solvers can outperform groups of high-ability problem solvers, Proceedings of the National Academy of Sciences of the United States of America 101 (2004) 16385–16389, https://doi.org/10.1073/ pnas.0403723101.

[34] J. Surowiecki, The Wisdom of Crowds: Why the Many Are Smarter Than the Few and How Collective Wisdom Shapes Business, Economies, Societies, and Nations Doubleday, New York, NY, 2004.

[35] J. Howe, Crowdsourcing: How the Power of the Crowd Is Driving the Future of Business, Crown Business, New York, 2008.

[36] H.W. Chesbrough, Open Innovation: The New Imperative for Creating and Profiting From Technology, Harvard Business Press, 2006.

[37] M. Bogers, J. West, Managing distributed innovation: strategic utilization of open and user innovation, Creativity and Innovation Management 21 (2012) 61–75, https://doi.org/10.1111/j.1467-8691.2011.00622.x.

[38] E. Schenk, C. Guittard, Towards a characterization of crowdsourcing practices, Journal of Innovation Economics 7 (2011) 93, https://doi.org/10.3917/jie.007. 0093.

[39] Y. Zhao, Q. Zhu, Evaluation on crowdsourcing research: current status and future direction, Information Systems Frontiers 16 (2014) 417–434, https://doi.org/10. 1007/s10796-012-9350-4.

[40] H.W. Chesbrough, The era of open innovation, Managing Innovation and Change 127 (2006) 34–41.

[41] E. Bonabeau, Decisions 2.0: the power of collective intelligence, MIT Sloar Management Review 50 (2009) 45.

[42] D. Geiger, M. Schader, Personalized task recommendation in crowdsourcing information systems — current state of the art, Decision Support Systems 65 (2014) 3–16, https://doi.org/10.1016/j.dss.2014.05.007.

[43] S.E. Page, Making the diference: applying a logic of diversity, Academy of Management Perspectives 21 (2007) 6–20, https://doi.org/10.5465/amp.2007 27895335.

[44] W. Van Osch, M. Avital, Collective generativity: the emergence of IT-induced mass innovation, Sprouts: Working Papers on Information Systems, 2009.

[45] H. Gimpel, Interview with Thomas W. Malone on “collective intelligence, climate change, and the future of work”, Business and Information Systems Engineering 57 (2015) 275–278, https://doi.org/10.1007/s12599-015-0382-4

[46] T.W. Malone, M.S. Bernstein, Handbook of Collective Intelligence, The MIT Press, Cambridge, MA. 2015

[47] T.W. Malone, R.J. Laubacher, C.N. Dellarocas, Harnessing crowds: mapping the genome of collective intelligence, SSRN Journal (2009), https://doi.org/10.2139/ ssrn.1381502

[48] E. Seltzer, D. Mahmoudi, Citizen participation, open innovation, and crowdsour cing, Journal of Planning Literature 28 (2013) 3–18, https://doi.org/10.1177/ 0885412212469112

[49] C.R. Darwin, The Efects of Cross and Self Fertilisation in the Vegetable Kingdom, John Murray, London, England, 1876.

[50] C.R. Darwin, On the Origin of Species: By Means of Natural Selection, or the Preservation of Favoured Races in the Struggle for Life, John Murray, London, England. 1859.

[51] S.R. Sommers, On racial diversity and group decision making: identifying multiple effects of racial composition on jury deliberations, Journal of Personality and Social Psychology 90 (2006) 597–612, https://doi,org/10.1037/0022-3514.90.4.597

[52] K.S. Cheruvelil, P.A. Soranno, K.C. Weathers, P.C. Hanson, S.J. Goring, C.T. Filstrup, E.K. Read, Creating and maintaining high-performing collaborative research teams: the importance of diversity and interpersonal skills, Frontiers in Ecology and the Environment 12 (2014) 31–38. https://doi,org/10.1890/130001

[53] J.N. Cummings, Work groups, structural diversity, and knowledge sharing in a global organization, Management Science 50 (2004) 352–364, https://doi.org/10. 1287/mnsc.1030.0134

[54] A.G. Tekleab. A. Karaca, N.R. Ouigley, E.W.K. Tsang, Re-examining the functional diversity–performance relationship: the roles of behavioral integration, team cohesion, and team learning, Journal of Business Research 69 (2016) 3500–3507 https://doi.org/10.1016/i.ibusres.2016.01.036

[55] H. Barke, L. Prechelt, Some reasons why actual cross-fertilization in cross-functional agile teams is dificult, Proceedings of the 11th International Workshop on Cooperative and Human Aspects of Software Engineering, Gothenburg, Sweden, ACM Press, New York, NY, USA, 2018, pp. 97–103.

[56] A. Davies, S. Manning, J. Söderlund, When neighboring disciplines fail to learn from each other: the case of innovation and project management research, Research Policy 47 (2018) 965–979, https://doi.org/10.1016/j.respol.2018.03.002

[57] S.S. Gunasekaran, S.A. Mostafa, M.S. Ahmad, A. Tang, Cross-fertilization of ideas in collective intelligence model, The 2nd International Symposium on Agents, Multi Agent Systems and Robotics, Bangi, Malaysia, IEEE, Piscataway, NJ, 2016, pp. 27-33.

[58] M. Lopez, M. Vukovic, J. Laredo, PeopleCloud service for enterprise crowdsourcing, 2010 IEEE International Conference on Services Computing, Miami, FL, USA, IEEE, 2010, pp. 538–545 05.07.2010 - 10.07.

[59] A. Ghezzi, D. Gabelloni, A. Martini, A. Natalicchio, Crowdsourcing: a review and suggestions for future research, International Journal of Management Reviews 20 (2018) 343–363, https://doi.org/10.1111/ijmr.12135.

[60] J. Chan, S. Dang, S.P. Dow, Improving crowd innovation with expert facilitation, Proceedings of the 19th ACM Conference on Computer-Supported Cooperative Work & Social Computing - CSCW ’16, San Francisco, California, USA, ACM Press, New York, New York, USA, 2016, pp. 1221–1233.

[61] V.K. Clawson, R.P. Bostrom, Research-driven facilitation training for computersupported environments, Group Decision and Negotiation 5 (1996) 7–29, https:// doi.org/10.1007/BF02404174.

[62] D.C. Brabham, Crowdsourcing the public participation process for planning projects, Planning Theory 8 (2009) 242–262, https://doi.org/10.1177/ 1473095209104824.

[63] M.K. Koszolko, Crowdsourcing, jamming and remixing: a qualitative study of con temporary music production practices in the cloud, Journal on the Art of Record Production 10 (2015).

[64] A.R. Hevner, March, park, ram, design science in information systems research, MI Quarterly 28 (2004) 75, https://doi.org/10.2307/25148625.

[65] S. Gregor, The nature of theory in information systems, MIS Quarterly 30 (2006) 611–642.

[66] S. Gregor, A.R. Hevner, Positioning and presenting design science research for maximum impact, MIS Quarterly 37 (2013) 337–355, https://doi.org/10.25300 MISO/2013/37.2.01.

[67] K. Pefers, T. Tuunanen, M.A. Rothenberger, S. Chatterjee, A design science research methodology for information systems research, Journal of Management Information Systems 24 (2007) 45–77. https://doi,org/10.2753/MIS0742- 1222240302.

[68] K. Pefers, T. Tuunanen, B. Niehaves, Design science research genres: introduction to the special issue on exemplars and criteria for applicable design science research, European Journal of Information Systems 27 (2018) 129–139, https://doi.org/10. 1080/0960085X.2018.1458066

[69] C. Sonnenberg, J. vom Brocke, Evaluations in the science of the artificial – reconsidering the build-evaluate pattern in design science research. Design Science Research in Information Systems: Advances in Theory and Practice: 7th International Conferonee Las Vegas NV USA Springer Rerlin 2012 pp 381, 397

[70] Facilitators of the FCL, Facilitators’ Experience From Former FCL Processes or Other Crowdsourcing Exercises, (2019).

[71] S. Gregor, D. Jones, The anatomy of a design theory, Journal of the Association for Information Systems 8 (2007).

[72] M.B. Miles, A.M. Huberman, Qualitative Data Analysis: An Expanded Sourcebook, Sage, Thousand Oaks, Calif, 1994.

[73] P. Wunderlich, D.J. Veit, S. Sarker, Adoption of sustainable technologies: a mixed methods study of German households, MIS Quarterly 43 (2019) 673–691, https:/ doi.org/10.25300/MISQ/2019/12112.

[74] M. Avital, D. Te'eni, From generative fit to generative capacity: exploring an emerging dimension of information systems design and task performance, Information Systems Journal 19 (2009) 345–367, https://doi.org/10.1111/j.1365- 2575.2007.00291 x

[75] S. Adamczyk, A.C. Bullinger, K.M. Moeslein, Commenting for new ideas: insights from an open innovation platform, International Journal of Technology Intelligence and Planning 7 (2011) 232–249

[76] H. Tarmizi, G.J. de Vreede, A facilitation task taxonomy for communities of practice, AMCIS 2005 Proceedings. 2005, p. 485

[77] S. Faraj, S.L. Johnson, Network exchange patterns in online communities,

Organization Science 22 (2011) 1464–1480, https://doi.org/10.1287/orsc.1100. 0600.

[78] M.C. Schuhmacher, S. Kuester, Identification of lead user characteristics driving the quality of service innovation ideas, Creativity and Innovation Management 21 (2012) 427–442, https://doi.org/10.1111/caim.12002

[79] M. Hossain, Performance and potential of open innovation intermediaries, Procedia - Social and Behavioral Sciences 58 (2012) 754–764, https://doi.org/10.1016/j. sbspro.2012.09.1053.

[80] I. Blohm, J.M. Leimeister, H. Krcmar, Crowdsourcing: how to benefit from (too) many great ideas, MIS Quarterly Executive 12 (2013) 199–211.

[81] D.L. Dean, J. Hender, T. Rodgers, E. Santanen, Identifying good ideas: constructs and scales for idea evaluation, Journal of the Association for Information Systems 7 (10) (2006) 646–699.

[82] M. Beretta, Idea selection in web-enabled ideation systems, Journal of Produc Innovation Management 7 (2018) 232, https://doi.org/10.1111/jpim.12439.

[83] G.W. Dickson, J.E. Lee-Partridge, M. Limayem, G.L. Desanctis, Facilitating computer-supported meetings: a cumulative analysis in a multiple-criteria task environment, Group Decision and Negotiation 5 (1996) 51–72.

[84] D.G. Gregg, Designing for collective intelligence, Communications of the ACM 53 (2010) 134, https://doi.org/10.1145/1721654.1721691.

[85] V.K. Clawson, R.P. Bostrom, The facilitation role in group support systems environments. Proceedings of the 1993 Conference on Computer Personnel Research St Louis, Missouri, United States, ACM, New York, NY, 1993, pp. 323–335.

[86] L. Yu, J.V. Nickerson, Generating Creative Ideas Through Crowds: An Experimental Study of Combination, (2011).

[87] Climate CoLab, About the project, https://www.climatecolab.org/page/about, (2019).

[88] Climate CoLab, Contests and workspaces, https://www.climatecolab.org/page/ crowdsourcing.

[89] M. Fuge, K. Tee, A. Agogino, N. Maton, Analysis of collaborative design networks: a case study of OpenIDEO, Journal of Computing and Information Science in Engineering 14 (2014) 764, https://doi.org/10.1115/1.4026510.

[90] J. Bianchi, Y. Knopper, O. Eris, P. Badke-Schaub, L. Roussos, Online ways of sharedness: a syntactic analysis of design collaboration in OpenIDEO, Proceeding of the 20th International Conference on Engineering Design, Milan, Design Society, Glasgow, 2015, pp. 339–348

[91] OpenIDEO, OpenIDEO challenges - design thinking sprints for social impact https://www.openideo.com/challenges?\_ga=2.183188707.415391568. 1579216493-1677928810.1576186325#how-challenges-work. Accessed date: 10 January 2020.

[92] OpenIDEO, OpenIDEO - inspiration phase: learning for innovation, https:// challenges.openideo.com/blog/inspiration-phase-learning-for-innovation, (2011) , Accessed date: 11 January 2020.

[93] Our Work, Future Earth, (2019) https://futureearth.org/about/our-work/ , Accessed date: 11 July 2019.

[94] Facilitator’s Evaluation of the Decision Support Tool Following the FCL Process, Facilitator of the Futures CoLab. 2019.
