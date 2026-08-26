---
otero_id: 26114
otero_key: "E9S8TQ3S"
title: "Data science in organizations: Conceptualizing its breakthroughs and blind spots"
authors: "Jacob L Cybulski; Rens Scheepers"
year: "2021"
journal: "Journal of Information Technology"
doi: "10.1177/0268396220988539"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Data science in organizations: Conceptualizing its breakthroughs and blind spots

Jacob L Cybulski and Rens Scheepers

Journal of Information Technology 1–22 © Association for Information Technology Trust 2021 Article reuse guidelines: sagepub.com/journals-permissions https://doi.org/10.1177/026839622098853DOI: 10.1177/0268396220988539 Journals.sagepub.com/jinf ⑤SAGE

## Abstract

The field of data science emerged in recent years, building on advances in computational statistics, machine learning, artificial intelligence, and big data. Modern organizations are immersed in data and are turning toward data science to address a variety of business problems. While numerous complex problems in science have become solvable through data science, not all scientific solutions are equally applicable to business. Many data-intensive business problems are situated in complex socio-political and behavioral contexts that still elude commonly used scientific methods. To what extent can such problems be addressed through data science? Does data science have any inherent blind spots in this regard? What types of business problems are likely to be addressed by data science in the near future, which will not and why? We develop a conceptual framework to inform the application of data science in business. The framework draws on an extensive review of data science literature across four domains: data, method, interfaces, and cognition. We draw on Ashby’s Law of Requisite Variety as theoretical principle. We conclude that data-scientific advances across the four domains, in aggregate, could constitute requisite variety for particular types of business problems. This explains why such problems can be fully or only partially addressed, solved, or automated through data science. We distinguish between situations that can be improved due to cross-domain compensatory effects, and problems where data science at best, only contributes merely to better understanding of complex phenomena.

## Keywords

Data science, big data, machine learning, artificial intelligence, complexity, cybernetics

## Introduction

Many organizations are turning toward data science as a means of leveraging the ever-increasing suite of data resources available today. Ransbotham et al. (2017) found that three-quarters of executives believe that data science will enable their companies to move into new businesses.

The field of data science spans mathematics, machine learning, artificial intelligence (AI), computational statistics, databases, and optimization (Dhar, 2013). The rationale for deploying such a vast arsenal of data science approaches in business environments is to uncover insights that are inherent in data (Cao, 2017b) in order to improve the quality of firm decisions (Ghasemaghaei et al., 2018). This encompasses problem-solving and predicting outcomes (Waller and Fawcett, 2013) to increase business performance (Ghasemaghaei et al., 2017; Müller et al., 2018; Trieu, 2017) in markets and supply chains (Chen et al., 2015; Grover et al., 2018).

There are many different definitions of data science as a field of scientific and professional endeavor (e.g. Cao, 2017a; Donoho, 2017). Some authors highlight the field’s transdisciplinary nature (Cao, 2017b), some its statistical and computational roots (Karpatne et al., 2017), others its quantitative and qualitative methods (Waller and Fawcett, 2013). Some emphasize derivation of value or knowledge from data (Dhar, 2013; Van der Aalst, 2016), some consider systematic generation of actionable insights (Pierson, 2015: Chapter 1), while others prioritize its ability to assist human understanding and decision-making (Blei and Smyth, 2017). Our focus is on the application of data science in organizational contexts (Medeiros et al., 2020; Steinberg and Aronovich, 2020; Vicario and Coleman, 2020). We thus adopt Provost and Fawcett’s (2013: 53) conceptualization of data science in the organizational context: understanding phenomena via the analysis of data with the ultimate goal of improving decision-making.

![](/api/attachments/E9S8TQ3S/fulltext/images/58ca0f2ba03e507eead817c0c9bd753a566b54ffb6e6cc76212b269fc649c028.jpg)  
Figure 1. Research process.

Data science seems particularly applicable to certain types of business problems. Solutions to these problems follow from analyses and predictions of “smooth” scientific data which lend themselves to the use of calculus, computational statistics, and machine learning approaches. These include applications unimaginable only a few years ago, for example, cognitive service automation (such as IBM Watson), self-driving cars, and advanced robotics, to name a few. However, many other business problems do not exhibit such characteristics; they are situated in complex socio-technical and behavioral contexts, exhibit nonrationality and their associated data are often unstructured, biased, or ill defined. Does data science have inherent blind spots for these types of problems?

We are framing the paper for researchers seeking to conceptualize data science opportunities and limitations for business problems that typically reflect socio-technical considerations. Socio-technical systems theories view organizational systems as consisting of social and technical subsystems, interacting with and influencing each other (Bostrom et al., 2009). In this regard, our scope is focused toward business problems exhibiting the following characteristics. First, the nature of problems involves data science and human decision-makers in organizational contexts. Second, we are interested in business data analyzed through data-scientific methods. Such data typically encompass social phenomena (e.g. consumer behavior, patterns, choices, and tradeoffs). Third, the results obtained through the application of data science methods, typically require human-systems interaction (e.g. interactive visualization) and human cognition for their interpretation, sense-making, insight generation, problem-solving, and decision-making. Our scope thus excludes more general topics pertaining to the deployment of data science in organizational contexts such as organizational strategy, business models, organizational culture, and stakeholder interests (Coombs et al., 2020; Günther et al., 2017).

How can we conceptualize the applicability of data science for socio-technical business problems? What types of business problems are addressable through the deployment of data science, and to what extent?

Given our audience and scope, we develop a conceptual framework, which we call the Data Science Organizational Framework (DSOF), to help researchers consider these questions, given recent advances, but also inherent limitations in data science today. A review of research literature pertinent to data science informs our framework development. We draw on and develop cybernetic logic, and in particular, Ashby’s Law of Requisite Variety as explanatory principle in the DSOF. We illustrate the applicability of the DSOF by analyzing a typical complex business problem that has recently become addressable through data science. We use the framework to consider classes of business problems which will remain only partially addressable, to different extents through data science, at least in the near future.

## Methodology

Our premise was that organizations deploy data science to inform problem-solving or decision-making about business phenomena. This involves obtaining data pertinent to the phenomenon of interest, applying various data science methods, generating, and interpreting results. Individuals and teams typically require a visual or other type of interface to interact with such data, methods, and results. Ultimately, decision-makers turn to data science to generate insights and enhance their understanding—their cognition—of particular business phenomena in order to inform problem-solving or decision-making.

To confirm this premise, we reviewed and interpreted the research literature pertaining to data science in organizations. Our research process was conducted in four stages (Figure 1). An extensive review of the literature was undertaken in the initial two stages of the process. As described below, Stage 1 involved literature selection, followed by detailed analysis (Stage 2). In this stage, we integrated the literature sources (Paré et al., 2015), utilizing automated (unsupervised) text analytics of all the selected article abstracts to produce a preliminary model of concepts covered by the assembled literature (Figure 2, Co-occurrence network). The researchers then interpreted the results from the unsupervised text analytics, labeling and partitioning the obtained constructs (Figure 2, Domain model). This occurred in an iterative manner, augmented by manual content analysis (Paré et al., 2015) of the literature to critically assess the association of constructs, sub-constructs, and their relationships (details in the appendix). This process confirmed the premise that four broad domain partitions (data, methods, interface, and cognition) are evident in the data science literature with relevance to organizational contexts. In Stage 3, the results from the literature review were combined with cybernetic principles to develop a framework to conceptualize the advances and limitations of data science in organizations (Figure 3). Finally, in Stage 4, we illustrate how this conceptual framework could be applied to analyze the extent to which data science can address different types of business phenomena.

![](/api/attachments/E9S8TQ3S/fulltext/images/0f67ec6592f2cba6a30744d0a55c28ef36ef3af44ab48ee247a750936f025ca2.jpg)  
Figure 2. Text analytics of data science topic structures in research literature.

![](/api/attachments/E9S8TQ3S/fulltext/images/fd69e58da42e147985a161597c0f664a09c32d7819a0e6cc5f25452d0927e211.jpg)  
Figure 3. Data science organizational framework (DSOF).  
Areas in blue denote increases in variety as result of data science advances in recent years in each domain. Areas in white denote limitations that are likely to remain in the near future. For details, refer the appendix.

The literature selection (Stage 1) focused on academic journals with some relevance to organizational contexts or business decision-making. A total of 41 journals were identified (see Table 1), with papers spanning the 7-year period (2014–2020) that approximately coincides with the notion of Big Data 2.0 and the increasing adoption of data science by business (Provost and Fawcett, 2013). Journals selected included the “the basket of 8” IS journals, eight top journals selected by the authors as having a strong emphasis on business decision-making in organizational contexts, and journals which were included as a result of keyword searches via EBSCOhost research platform. The top 16 journals were systematically scanned issue-by-issue for relevant papers. After the comprehensive scan, the journal database was further searched by keywords related to the area of data science, big data, analytics, and AI with relevance to decision-making in organizational contexts (see Table 1). Recommendations from the EBSCOhost research platform of related sources were also considered for inclusion. This process yielded a sample of 424 papers. After reading each paper’s abstract in detail, 294 were selected for further analysis (of these, just over 150 are directly cited in this paper).

In Stage 2, the 294 paper abstracts were initially analyzed using automated text analytics.<sup>1</sup> This enabled us to explore the research area and to identify the main research topics and their relationships. The relevant paper abstracts were lexically analyzed to extract stems of all nouns and verbs (representing concepts, objects, subjects and places, as well as events and activities), stop words were removed, and a documents-vs-terms matrix was generated. The matrix was subsequently used to determine pairwise co-occurrence of terms (Danowski, 1993; Osgood, 1959) within each individual article abstract and generalized across all abstracts.

Table 1. Journals and keywords selected for review of data science papers.

<table><tr><td>Basket of 8 IS JournalsEuropean Journal of Information SystemsInformation Systems JournalInformation Systems ResearchJournal of the Association for Information SystemsJournal of Information TechnologyJournal of Management Information SystemsJournal of Strategic Information SystemsManagement Information Systems QuarterlyJournals with emphasis on decision-making in Organizational ContextsCommunications of the ACMCommunications of the Association for Information SystemsDecision Support SystemsHarvard Business ReviewHuman–Computer InteractionManagement ScienceMIT Sloan Management ReviewOrganization ScienceExamples of Other Journals with papers related to Data Science within an Organizational ContextACM Computing SurveysACM Transactions on Computer-Human InteractionCognitive Biases in VisualizationsCreativity and Innovation ManagementExpert Systems with ApplicationsEuropean Journal of Operational ResearchIEEE Transactions on Visualization and Computer GraphicsIEEE Transactions on Pattern Analysis &amp; Machine IntelligenceIEEE Transactions on Intelligent Transportation SystemsIEEE Transactions on Biomedical EngineeringInformation Processing &amp; ManagementInformation SystemsInformation SciencesInteractionsJournal of AdvertisingJournal of Big DataJournal of Computer Information SystemsJournal of Decision SystemsJournal of Economics, Finance and Administrative ScienceJournal of Management AnalyticsJournal of Parallel and Distributed ComputingKnowledge-Based SystemsNeurocomputingScienceThe Journal of Finance and Data Science...and others. . .</td><td>Keywords used to identify relevant papers:Data ScienceData AnalyticsData AnalysisBusiness AnalyticsPredictive AnalyticsDecision AnalyticsMachine LearningDeep LearningData MiningData EngineeringBig DataData VisualizationInformation VisualizationInteractive VisualizationVisual AnalyticsDecision SupportGroup Decision SupportHuman–Computer InteractionIntelligent InterfacesDistributed CognitionArtificial IntelligenceExpert SystemsKnowledge-Based SystemsAdditional terms used to focus the search on business context:BusinessOrganization</td></tr></table>

Term co-occurrences were measured with the Jaccard coefficient of similarity, which is especially effective in the analysis of large text documents, such as article abstracts. The larger the Jaccard coefficient between two terms, the higher their similarity (closeness) or strength of relationship between the concepts they represent. The terms and their similarity form a network of nodes and weighted links. Such a network usually consists of many sub-networks, which are either separate or weakly interconnected. Each of the fully connected sub-networks, called community, represents a group of strongly related terms, which can be interpreted in aggregate as a higher-level concept.

The co-occurrence network forms a three-dimensional (3D) structure, which is difficult to visualize and comprehend. It is hence commonly mapped onto a two-dimensional (2D) plot using an automatic layout algorithm. In this case, the Fruchterman and Reingold (1991) algorithm was used to optimize placement of nodes in 2D, in such a way that their relative spatial (similarity-determined) distances in 3D are preserved (whenever possible).

As a result, terms commonly used in similar contexts are displayed close to each other and inter-related communities are also placed in relative proximity. To enhance readability of the layout, each of the communities is displayed as a minimum spanning tree of its sub-network, using only the highest co-occurrence links and thus strongest similarity. This eliminates less important term-to-term connections. Figure 2 (Co-occurrence Network) depicts the resulting cooccurrence term network. The size of nodes indicates their relative frequency of occurrence across all abstracts. Solid line links between terms within the same community indicate their co-occurrence (as measured by the Jaccard coefficient). Different communities are linked with dashed lines. Communities are color-coded so that all their members share the same node color. Colored dashed lines around these communities were added by the authors to delineate domain boundaries (discussed below).

The process of text analytics and visualization was unsupervised.<sup>2</sup> However, the process was parameterized by the number of displayed links, which influences the amount of displayed information and the formation of communities. When the number of links is small, communities are abstract and consist of few high frequency terms. However, such networks commonly suffer from fragmentation due to many small and disconnected communities. When the number of links is large, the community structure can be overly complex and difficult to interpret; however, communities consist of many well-connected groups of terms.

We experimented with different numbers of displayed links ranging from small to large (500). Beyond 420 links, the layout algorithm failed due to the network complexity. In this process, we monitored the integrity of resulting community structures, as well as their evolution due to their creation, splitting, merging, and transforming.

At 420 links (top of Figure 2), the co-occurrence network no longer suffers from fragmentation. Its communities are well integrated with meaningful inter-community connections. Terms forming each community have sufficient level of semantic cohesion to allow their interpretation and separation from other communities. This enabled preliminary labeling and partitioning of the terms into larger structures, which we refer to as domains—the only manual tasks in this process. The researchers’ interpretation of the machine-generated co-occurrence network (top of Figure 2) is reflected in the Domain model (bottom part of Figure 2), which occurred iteratively following detailed reading of the source papers and manual content analysis (see the appendix).

The co-occurrence network confirmed that the data domain, methods domain, interface domain, and cognitive domain are pertinent to conceptualize the application of data science application in organizational contexts. The model also features a separate area of concepts related to business phenomena, which set the context for, but are outside the scope of data science and its methods.

The Data domain, which represents various aspects of data and information processing, assumes a central position in the co-occurrence network. It is strongly interconnected with the Cognitive and to a lesser extent the Interface domains. The Cognitive domain describes a wide spectrum of aspects associated with individual cognitive processes, such as decision-making, insight generation, problem-solving, and understanding (Kahneman and Tversky, 1984; for example, Simon, 1979). The cognitive domain also identifies concepts associated with group decision-making and collaborative insight generation, which are commonly attributed to distributed cognition in organizational contexts and work carried out in communities of practice. This is in line with Provost and Fawcett’s (2013: 53) goal behind the deployment of data science in organizational contexts, that is, (1) problem-solving/automation, (2) improving a situation though individual/collaborative decision-making, and (3) insight generation and better understanding of phenomena. The Methods domain consists of two separate areas, one describing various technical methods of data analysis, including machine learning, databases, and algorithms. Another area of methods highlights conceptual foundations of model and theory development. The Interface domain acts as a bridge between Data and Methods. It includes two inter-related communities, one to do with visualization techniques and another with interactivity and support for collaboration. The area of business phenomena describes intelligence and analysis functions within an organization, as well as the conceptualization and codification of organizational phenomena (e.g. customer behavior) in a variety of formats.

The Domain model in Figure 2 represents a higher-level abstraction, developed by the researchers from the cooccurrence network. As such, the machine-based process informed the development of the Domain model, which mirrors the structure of the detailed literature review of constructs, sub-constructs, and their relationships (as reported in the appendix). The authors’ manual content review refined and enriched the concepts discovered in the process of unsupervised text analysis. The manual review also focused on the socio-technical nature of business phenomena addressed via data science in the literature, including advances and limitations in each of the four domains.

The results from the machine-based and manual content analysis informed the development of the DSOF, which is presented next.

## Conceptual framing

This section describes Stage 3 of our research process, in which we develop a DSOF to conceptualize the advances and limitations of data science in relation to socio-technical business problems. The development of the framework draws on the four identified data science domains (data, method, interface, and cognition) and the advances and limitations in each domain (as summarized in Tables 5 to 8 in the appendix). We situate and adapt cybernetic principles to consider the opportunities afforded to organizations by data science vis-a-vis the nature of particular social technical problems they seek to address through such capabilities. The DSOF is depicted in Figure 3.

Historically, the field of cybernetics has explored principles relating to complex systems and regulatory control, drawing on key concepts such as the notion of variety (Ashby, 1958, 1961, 1968). Broadly speaking, cybernetic variety refers to the “complexity” of a system, indicated by its richness, heterogeneity, number of subsystems, and different system states. Cybernetic principles have been applied to theorize the management of complex socio-tech nical systems, including environmental and social systems such as organizations (Beer, 1984; Poulis and Poulis, 2016).

Cybernetics utilizes a vocabulary of regulators (controllers) controlling phenomena. Ashby’s Law of Requisite Variety is a central principle in this regard. In brief, the law states that a regulator needs to have a level of variety that exceeds that of the system to be controlled, in order to achieve homeostasis (or equilibrium). The simple analogy of a person driving a car illustrates Ashby’s Law (Introna, 1991): the variety of the driver (the regulator) must exceed the variety of the car on the road (the phenomenon) to keep the car under control (homeostasis). However, increased speed or unanticipated environmental disturbances such as bad weather or stray animals could cause the variety of the phenomenon to exceed that of the regulator. In that case, the regulator can no longer control the phenomenon as the variety of the latter now exceeds the variety of the former.

“First order” cybernetics (Heylighen and Joslyn, 2001) theorized simple regulation scenarios (e.g. thermostatic control of room temperature), based on environmental feedback (current room temperature) and adaptive control (increasing/decreasing heating/cooling) in line with some objective (ideal room temperature). However, more complex regulation-control scenarios demanded richer theorizing. A complex set of relations and dependencies could exist between the regulator, the phenomenon being controlled, and the environment in which regulating takes place. Furthermore, the variety of both the regulator and phenomenon being controlled could vary dynamically.

“Second order” cybernetics have evolved beyond simple regulation-control scenarios toward more complex, selforganizing systems (Goldstein, 2011). This development links to the notion of autopoiesis in biology (e.g. Maturana and Varela, 1991) and advanced adaptive computer systems (Winograd et al., 1986). In particular, the notion of the “emergence” of novel variety, which derives from the observation that above a certain threshold of variety, a regulator could transcend the functionality and behavior it was originally designed for.

This emergent variety adds to the overall variety of the regulator to better cope with increasingly diverse and unexpected environmental disturbances. Highly complex automata can gain the capability of adaptation in response to environmental change, akin to living organisms rather than material machines. Consider contemporary examples such as cognitive service automation, robotic automation, and self-driving cars. Such automata not only incorporate sophisticated functionality (e.g. automated decision-making) but also learn and adapt (e.g. to react to unforeseen circumstances) by absorbing feedback from the environment (e.g. via sensors), thus exhibiting a significant degree of autonomy.

When considering modern organizations and the advances in data science that increases the variety of regulators, the logic of second-order cybernetics provides an appropriate theoretical foundation for the DSOF. Accordingly, as summarized in Table 2, we adapt secondorder cybernetics concepts in the DSOF. To support the adaptation, we situate literature relevant to the organizational deployment of data science (refer the appendix) with the DSOF constructs.

We adapt the cybernetic notion of a regulator as defined in Table 2. Our adaptation of the construct was primarily informed by the detailed review of the data science literature (see the appendix). In addition, we situate literature pertinent to data science deployment as part of this construct—that included the notion of an organizational capability (Amit and Schoemaker, 1993) and its dimensions (knowledge and skills, technical and managerial systems, and values and norms) (Leonard-Barton, 1992). We also situate literature on human/technology collaborative networks (e.g. distributed cognition – Hollan et al., 2000; and actor-network theory – Latour, 1996) with this construct (cf. Tables 7 and 8 in the appendix). We followed a similar process with the other constructs of the DSOF.

Historically, the variety of many complex business problems typically exceeded the variety of regulators at the time. Drawing on the notion of emergence in second-order cybernetics, advances in data science in recent years in the domains of data, method, interface, and cognition (refer the appendix) imply an aggregate increase in the variety of the regulator in relation to some classes of business problems. Advances in data science in each of the domains are depicted in the area shaded in blue in Figure 3, for example, availability of large data repositories pertinent to business phenomena, new methods of analysis using specialist software and hardware, rich tools for visualization, and partautomation of business decision-making.

For some business phenomena, these aggregate variety increases of the regulator meet or exceed the level of requisite variety under Ashby’s law for such problems. This explains why such phenomena can be fully addressed through data science today (i.e. such problems can be solved, solutions can even be automated). Conversely, despite advances in data science in recent years, key limitations in data, method, interfaces, and cognition (refer the appendix) exist in relation to many other business phenomena. Limitations in each of the domains are depicted in the areas shaded in white in Figure 3, for example, poor data quality, data fragmentation, social factors impeding the application of data-scientific methods, lack of suitable visual metaphors for abstract business data, and human cognitive limitations in decision-making about complex phenomena. These limitations imply upper bounds to aggregate variety increases of a regulator. Such variety imbalances explain why many classes of business problems are only partially addressable through data science, at least in the foreseeable future.

Table 2. Constructs in the DSOF.

<table><tr><td>Construct</td><td>Definition</td></tr><tr><td>Phenomenon</td><td>A socio-technical business problem or situation that an organization is seeking to control through the deployment of data science. For example, predicting consumer demand is typically a socio-technical business problem, requiring customer data, predictive methods, understanding of consumer behavior, etc.</td></tr><tr><td>Variety of phenomenon</td><td>The socio-technical complexity of a phenomenon, encompassing both technical (e.g. heterogeneity, number of subsystems, different system states) and social complexity indicators (e.g. understandability, intractability, observability, predictability).</td></tr><tr><td>Control</td><td>A regulator&#x27;s interventions to (1) solve a problem (including automation or part-automation thereof), (2) significantly improve a situation via data-driven analyses that inform decision-making, or (3) to generate insights to better understand a complex phenomenon (refer Figure 2, Domain Model) through the deployment of data science. Many phenomena cannot be “controlled.”</td></tr><tr><td>Feedback</td><td>Environmental signals related to phenomenon (refer also Data below), including response to control interventions (where applicable), for example, consumer response to a promotion.</td></tr><tr><td>Regulator</td><td>An organizational capability to deploy human and technical data science resources to control phenomena, effected through data-based decision-making and problem-solving, to achieve desired business objectives. Encompasses individual or multiple human decision-makers collaborating. Regulators in organizational contexts are typically bound by values and norms that guide the deployment of data science within their sphere of their responsibility.</td></tr><tr><td>Variety of Regulator</td><td>The aggregate levels of variety in the domains of data, method, interface, and cognition, $^a$ including cross-domain interaction effects. The variety of the regulator is situation- and context-specific and considered in relation to particular phenomena.</td></tr><tr><td>Data, Method Interface, and Cognition</td><td>Advances in data science in each of these domains add to the aggregate variety of the regulator. Limitations in each domain that exist today, denote upper bounds to variety increases (see the appendix).</td></tr><tr><td>Requisite Variety</td><td>Under Ashby&#x27;s Law of Requisite Variety, and in line with the definitions above, the minimum level of aggregate variety that a regulator needs to attain in order to control a particular phenomenon.</td></tr></table>

DSOF: Data Science Organizational Framework.  
<sup>a</sup>The broader business management literature documents several factors pertinent to the efficacy of organizational capabilities such as cultural, political, and resource aspects. Such factors are contextual to data science deployment, but fall outside the scope of our present analysis. We focu specifically on the human-technical instrumentality of data science in organizational contexts.

The second-order cybernetic notion of emergent variety operates as follows in the DSOF. First, as described above, data science advances in each of the domains add to the aggregate variety of regulator, for example, additional data or novel predictive methods. Second, feedback from the environment (both the external and internal environment) can add to emergent variety. For example, consumer responses to a promotion, or feedback from internal R&D processes, can yield additional data and generate new cognitive insights that can be leveraged in subsequent decision-making. This situates emergent variety in the context of data science as a means of leveraging environmental feedback to inform learning, adaptation, and decision-mak ing regarding phenomena of interest.

Cross-domain interaction effects can occur in the DSOF. For example, limitations in the cognitive understanding of a complex phenomenon could be ameliorated in part through emergent variety in other domains (e.g. new data, improved visualization, or novel methods of analysis). Such cross-domain interactions can have a compensatory effect on the variety of a regulator, to the extent where aggregate variety approaches requisite variety for particular phenomena. This would explain why data science, despite some limitations, could still enable a regulator to address such phenomena to a significant extent.

In the sections that follow, we illustrate how the DSOF could be applied to consider the deployment of data science for different classes of business problems.

## Illustrative example: product quality control

In this section, we consider a business problem that has recently become solvable through the application of data science. The illustrative example is analyzed using the DSOF.

Product quality underpins organizational competitiveness, especially in manufacturing and production environments.

The quality movement set forth by W. Edwards Deming, Joseph Juran, and Kaoru Ishikawa instilled the ethos of total quality management, throughout the production processes (Hackman and Wageman, 1995). Exercising effective quality control is a particularly complex agency problem in distributed manufacturing (e.g. in franchise chains). In such environments, product quality is largely under the control of distributed outlets run by franchisees, yet quality impacts the reputation and brand growth of the franchisor.

For many years, the global franchise chain Domino’s Pizza Enterprises Ltd has faced exactly this business problem. Its business model involves semi-autonomous franchised outlets, where workers, typically working shifts, prepare pizzas for customers. The quality of pizzas is the responsibility of each franchise, but of course ultimately determined by customers. Making a pizza is prescribed; however, the process is manual and the outcome has many acceptable and unacceptable variants. Various factors such as time pressure (e.g. during peak periods) or employee training could influence the end result. Quality control can thus be difficult to ensure, involving checking of ingredients, the production process, and the final product. Visual perception of the product quality can be influenced by assessors’ background, personal taste, training, experience, and fatigue. Furthermore, each franchise may also have its own impact factors, which may be related to its location, culture, and the management style.

To overcome the problem of ensuring product quality across their chain of franchises, Domino’s recently imple mented the “DOM Pizza Checker,” a machine learning solution in their franchises (Domino’s, 2019). The solution automates the quality assessment by utilizing a smart scanner with a display monitor, typically installed above the pizza cutting area that checks and reports on the quality of every pizza made prior to packing and delivery. The technology incorporates image recognition and machine learning to analyze and rate each pizza based on its type, toppings, and the distribution of ingredients (Domino’s, 2019). This is achieved by comparing the image of a pizza being made against a large database of images of previously made and assessed pizzas. Pizzas that fail the quality check are remade.

Utilizing the vocabulary and logic provided by the DSOF, this example of a complex business problem—the phenomenon of product quality control across the franchise—that ha become addressable through data science can be explained as follows. The regulator in this instance is Domino’s franchisor (i.e. their corporate entity). The deployment of data science is their new distributed organizational capability for quality control. All four domains of the DSOF (data, method, interface, and cognition) are pertinent to this example.

The cybernetic variety of the business phenomenon (overall product quality control across the chain) is very high, as it would have been difficult for the franchise or to accurately monitor and ensure quality across all franchises/ individual employees. This encompasses the complexity of managing quality control across local outlets, during peak periods, combined with rising consumer expectations in terms of pizza preparation, cooking preferences, range of toppings, and crusts.

The data science deployment brings significant new variety to the regulator. Assessment of product quality, based on visual appearance, can now be fully automated. The machine learning model used in the process represents the cumulative experience of numerous quality assessors, thus augmenting the cognitive abilities of individuals with distributed cognition of many assessors. Significant variety in data exists on what well-cooked, and conversely substandard, pizzas look like from a customer satisfaction perspective. Data of the chain’s different types of pizzas, toppings selections, optimal presentation, and so on have been captured digitally in a large image database. Pizza images contain only unstructured and hard-to-interpret data. However, by applying data-scientific image analysis methods, most of the data relevant to quality control for this particular business problem could be captured, structured, and pre-classified. The latter would typically involve assigning a numeric or ordinal value to denote quality, to enable subsequent training of machine learning image recognition models that were acquired via Domino’s turnkey scanners at each franchise. Of course, such models would be updated periodically, for example, to recognize new types of pizzas, toppings, preparation modes, and so forth. However, the data for this type of business problem are relatively stable and not subject to rapid change.

The method used by the “DOM Pizza Checker” combines technical hardware and software elements, with highprecision video scanners and machine learning software developed by Dragontail Systems in partnership with Google (news.com.au, 2017). Google AI tools are well known for their capability of large-scale image recognition and classification despite the data volume, lack of structure, fragmentation, or reliability. In case of pizza quality control, the Google AI–based process is likely to involve creation of machine learning models (possibly deep learning models) trained on a very large number of pizza images, pre-classified in terms of their quality ratings. Trained models can subsequently be deployed in each store, as part of the smart video scanners, thus providing an affordable means for image capture, recognition, and processing.

The interface of the solution includes the scanners and in-store monitors, which utilize simple interactivity, providing feedback in the form of percentage ratings displayed to store managers and employees, who can easily be trained to observe and action quality recommendation. Moreover, accumulated analytics for each store are typically collated for the subsequent analysis and possible monitoring by the franchisor. The franchisor could get an overview of overall product quality at any point in time across the entire chain, for example, via simple “heat map”–based visualizations.

In aggregate, the variety of the regulator in this example meets the requisite variety to control this phenomenon. No major limitations exist in any of the DSOF domains for this class of problem. Consequently, this particular business problem has become addressable through data science, to the point of an automated solution.

## Discussion

We now discuss the application of the DSOF more generally to conceptualize the extent to which different types of business problems are addressable through the deployment of data science. As outlined earlier (refer Table 2), a regulator’s ability to control a phenomenon encompasses (1) solving a problem (including automation or part-automation thereof), (2) significantly improving a situation via data-based predictions that inform decision-making, or (3) generating insights to better understand a complex phenomenon, through the deployment of data science. We consider these different objectives behind the deployment of data science in the context of the illustrative example and four additional short vignettes.

Product quality control. The pizza quality control example (above) serves as an illustration of former complex socio-technical problems that have been recently solved and automated via the deployment of data science.

Many classes of business problems exhibit similar increases in requisite variety across all domains in the DSOF and which have been effectively solved. These include the former complex problem of automated interaction with customers (utilizing voice recognition, responding intelligently to customer questions, etc.). Today, digital assistants such as Apple Siri, Google Assistant, Amazon Alexa, and Microsoft Cortana enable a variety of business solutions, such as automated call service response. Follow-up waves of innovation that build on voice recognition and breakthroughs in neural networks, language, and semantic analysis have enabled business applications such as automated robot call services (e.g. Google Duplex) and cognitive service automation (e.g. IBM Watson) (Scheepers et al., 2018).

For these classes of problems, there are no significant limitations in any of the DSOF domains. Such breakthroughs can therefore be explained in the same manner: advances in data science in recent years have resulted in variety increases across all four DSOF domains. On aggregate, the variety of the regulator now meets or exceeds the requisite variety to control these specific phenomena. Consequently, these former complex problems have become solvable (including automation or part-automation thereof).

Traffic congestion. Management of traffic congestion is a phenomenon where, under normal circumstances, most of the time the patterns of events are predictable and outcomes are well understood. However, unexpected traffic peaks, accidents, weather, and so forth instantaneously escalate the variety of the phenomenon. Feedback of real-time traffic data from sensors, traffic modeling, and interactive visualization are increasing the aggregate variety of the regulator, considerably improving traffic management in many cities today.

Consumer churn. Consumer churn is a prevalent phenomenon, especially in service industries such as telecommunications and hospitality. Consumers may switch to a different provider, based on perceptions of their current provider, for opportunistic reasons, and so on. Significant modeling of churn behavior exists in the literature (Tamaddoni et al., 2016), with typical patterns of customers who are likely to churn, and those less likely to do so. Many service providers have extensive historical and current data on churn behavior, probabilistic churn modeling, and interactive visualizations of customer behavior trends. This can inform decisions around suitable interventions (e.g. providing incentives or discounts to valuable customers who are likely to churn).

In the traffic congestion and consumer churn examples, extensive real-time or near real-time data, predictive modeling and visualization yield insights that enable regulators to significantly improve these complex situations. Despite key limitations in one or more of the DSOF domains (e.g. cognition of emotionally driven behavior, complex network externalities), these situations are partially ameliorated through cross-domain variety increases (e.g. richer, real-time data, increasingly sophisticated predictive modeling, interactive visualization). While the aggregate variety of the regulator still remains below requisite variety to fully control such phenomena, the deployment of data science can enable organizations to significantly improve these situations via informed decision-making.

Stock market predictions. Non-rationality and volatility that often drive human behavior in these types of phenomena cannot adequately be modeled or captured, even with increasingly rich data. Furthermore, understanding of underlying causes of fluctuation and socio-political developments that potentially all manifest in complex market volatility is limited. As a consequence, despite an ever-increasing body of real-time financial data and advances in methods, such as financial and econometric modeling and visualization of long-term trends, the insurmountable limitations in data and cognition funda mentally restrict the level of variety of any regulator.

Parallels of this situation can be found in economic forecasting and real-estate price estimation. In all such cases, vast amounts of transaction data are available to organizations in these sectors. Such data reflect the high volatility of these phenomena. Data analytics in these areas are domain specific and can be effective for short-term prediction. However, they remain ineffective for long-term forecasting. While visuali zation of transaction-level fluctuations is available, there is a lack of suitable metaphors to represent useful insights embedded in complex datasets. Other data pertinent to such phenomena (e.g. developing news or regulatory information)

are difficult to operationalize in automated modeling. Multivariate relationships in real time lead to NP-complete problems with few known solutions. Across all DSOF domains, the variety of these phenomena thus well exceed that of regulators. Other examples of such business phenomena include predicting outcomes of enterprise bargaining, litigation, and marketing campaigns. Consequently, at this point in time, data science has limited potential to effectively address such phenomena; at best, the contribution is the generation of insights to better understand these phenomena.

Prevention of fraud and cyber security attacks. Fraudulent activity continues to frustrate banks’ and law enforcement agencies’ efforts to curtail it. Over time, such organizations have built up a cumulative stock of knowledge about typical patterns of fraudulent activity and measures to counter such activities. This is supported by data-scientific methods such as advanced algorithms for anomaly detection, the use of fraud analytics, and digital forensics. Each time a new form of fraud is identified, it is added to the global stockpile of knowledge and appropriate preventive measures can be deployed.

According to the DSOF, for the regulator, this amounts to an increasing level of aggregate variety, which enables improved fraud detection and prevention. However, fraudsters continue to develop new and more sophisticated schemes, diminishing the relevance of past fraud incident data. Consequently, preventive methods and interactive exploration of incident data are limited. Each time a new fraudulent scheme is conceived, the variety of the phenomenon (fraudulent activity) increases vis-a-vis that of the regulator, and so this “arms race” continues. There are many other cases of similar adversarial situations, for example, cyber security attacks. Typically, organizations upgrade their cyber defenses following security breaches, only to be found wanting again when cyber-criminals devise new and more sophisticated modes of attack. While data science can be used to analyze known patterns in these cases, the potential to effectively prevent such phenomena is limited due to the dynamic, continued increase in the variety of these phenomena.

Table 3 summarizes analysis of the vignettes through the DSOF constructs. Inherent limitations (above the dashed line) and advancements (below the dashed line) of data science in relation to these problems are indicated. The vignettes illustrate a spectrum of the potential of data science in business, given the variety of the phenomenon and the aggregate variety of the regulator across the DSOF domains.

Table 3 suggests that the ability of the regulator to control phenomena (i.e. solving problems, improving situations, or gaining understanding) degrades commensurately with an increase in the limitations in the different DSOF domains and an increase in the variety of the phenomenon. Table 4 represents the essence of this proposition, indicating the extent to which different types of business phenomena can effectively be addressed through data science, given the aggregate variety of the regulator versus that of the phenomenon.

Table 3. Vignettes illustrating limitations and advances across DSOF domains.

<table><tr><td rowspan="2">Example</td><td colspan="4">Aggregate variety of the regulator (afforded by data science) $^a$ </td><td rowspan="2">Regulator&#x27;s ability to control phenomenon</td></tr><tr><td>Data</td><td>Method</td><td>Interface</td><td>Cognition</td></tr><tr><td rowspan="2">Pizza quality control</td><td></td><td></td><td>-</td><td>-</td><td rowspan="2">Problem solving (including automation)</td></tr><tr><td>Reflective, availability of structured and unstructured data</td><td>Image analysis through deep learning and AI</td><td>Simple interface at branch; “Heat-map” visualization of quality across whole chain</td><td>Replacement of intuition with automated judgment</td></tr><tr><td rowspan="2">Traffic congestion</td><td>-</td><td>Computationally challenging</td><td>-</td><td>-</td><td rowspan="2">Significantly improving the situation</td></tr><tr><td>Reflective, availability of real-time data</td><td>Short-term predictable</td><td>Detailed real-time visualization</td><td>Well understood</td></tr><tr><td rowspan="2">Consumer churn</td><td>-</td><td>-</td><td>-</td><td>Unpredictable opportunistic or emotional behavior</td><td rowspan="2">Significantly improving the situation</td></tr><tr><td>Reflective, availability of historical trends</td><td>Increasingly sophisticated probabilistic churn modeling</td><td>Churn propensity can be visualized effectively</td><td>Understanding of some typical patterns</td></tr><tr><td rowspan="2">Stock market predictions</td><td>Not reflective, high volume, high velocity, too many patterns</td><td>Domain-specific solutions, computationally challenging</td><td>Abstract, lack of visual metaphor for non-numeric</td><td>NP-complete problem, irrational, emotional</td><td rowspan="2">Limited ability to control, other than better understanding of phenomenon</td></tr><tr><td>Vast amounts of shared data</td><td>Short-term predictable</td><td>Can be visualized in part</td><td>Partially understood</td></tr><tr><td rowspan="2">Fraud, cyber attacks</td><td>Not reflective of current schemes, legal limits</td><td>Domain-specific solutions, unpredictable human behavior</td><td>Difficult to visualize, lack of visual metaphor</td><td>Asymmetric vis-a-viz adversaries, hard-to-engage-with subcultures</td><td rowspan="2">Limited ability to control, other than better understanding of phenomenon</td></tr><tr><td>Repositories of past incidents, malware, and cyber attacks</td><td>Specialist analytics and tools are available</td><td>-</td><td>Growing understanding of criminal entities</td></tr></table>

aLimitations appear above, and advances below the dotted line respectively. AI: Artificial Intelligence; DSOF: Data Science Organizational Framework.

Table 4. Extent to which business phenomena can be addressed through data science.

<table><tr><td>Aggregate variety of regulator vs phenomenon (according to the DSOF)</td><td>Problem-solving, including decision automation</td><td>Improving situations via data-based decision-making</td><td>Enhanced understanding of phenomenon</td></tr><tr><td>At requisite variety (no limitations in any of the domains)</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Below requisite variety (some limitations, compensatory cross-domain effects)</td><td>-</td><td>√</td><td>√</td></tr><tr><td>Well below requisite variety (significant limitations in multiple domains)</td><td>-</td><td>-</td><td>√</td></tr></table>

DSOF: Data Science Organizational Framework.

## Conclusion

The proliferation of data throughout society, combined with the availability and affordability of advanced computing capabilities, unimaginable only a few years ago, has prompted many organizations to consider data science deployments. We illustrated how the DSOF framework can inform the extent to which data science can address different types of business problems.

Our central argument is that advances in data science in aggregate across the four DSOF domains of data, method, interface, and cognition could constitute requisite variety and therefore enable organizations to effectively solve particular business problems. For other types of problems, cross-domain emergent variety could compensate for key limitations in data science today, enabling decision-making to significantly improve such situations. Last, for many complex business problems, insurmountable limitations across multiple domains implies that data science today, at best, can only advance understanding of such phenomena.

The DSOF, while rooted in cybernetics, echoes longstanding views on socio-technical approaches to conceptualizing information technology in organizational contexts. Of particular note is the mutual constitutional and co-evolution of the social and technology in organizational deployments (e.g. Sawyer and Jarrahi, 2014). The DSOF adds to this discourse in the context of data science by situating Cognition and Interface (the social) along with Data and Method (the technology) and considering their co-evolution and cross-domain interaction. This suggests fruitful avenues for future research in exploring how co-evolution between social and technical domains can ameliorate limitations and culminate in more effective data science deployments. For example, novel visualization metaphors can trigger new avenues of enquiry when dealing with highly complex phenomena (illustrating interaction between the Interface and Cognitive domains). Future research could also explore the role of strategic information alliances and data science outsourcing as approaches to overcome key limitations in the Data, Method, and Interface domains of particular regulators.

This research is limited in the sense that we did not specifically consider organizations’ particular deployments of data science. It should be noted that cross-domain variety effects could be a double-edged sword, depending on an organization’s specific deployment. Poor data quality, limited analysis skills, crude visual interfaces, and so on can all erode particular regulators’ overall variety to the detriment of effective decision-making and problem-solving.

## Declaration of conflicting interests

The author(s) declared the following potential conflicts of interest with respect to the research, authorship, and/or publication of this article: The paper’s second author Rens Scheepers is part of Journal of Information Technology (JIT) editorial board.

## Funding

The author(s) received no financial support for the research, authorship, and/or publication of this article.

## ORCID iD

Jacob L Cybulski https://orcid.org/0000-0002-9061-9389

## Notes

1. We used KH Coder, open-source analytics content analysis and text mining (see https://khcoder.net/en/).

2. “Unsupervised” means topics and their community groupings were derived purely from machine algorithmic analysis of abstracts with no researcher intervention (other than community labeling and domain partitioning).

## References

Agarwal R and Dhar V (2014) Editorial—Big data, data science, and analytics: The opportunity and challenge for IS research. Information Systems Research 25(3): 443–448.

Al-Kassab J, Ouertani ZM, Schiuma G, et al. (2014) Information visualization to support management decisions. International Journal of Information Technology & Decision Making 13(02): 407–428.

Aleksander I (2017) Partners of humans: A realistic assessment of the role of robots in the foreseeable future. Journal of Information Technology 32(1): 1–9.

Amit R and Schoemaker PJH (1993) Strategic assets and organizational rent: Strategic assets. Strategic Management Journal 14(1): 33–46.

Arnott D and Pervan G (2005) A critical analysis of decision support systems research. Journal of Information Technology 20(2): 67–87.

Ashby WR (1958) Requisite variety and its implications for the control of complex systems. Cybernetica 1(2): 83–99.

Ashby WR (1961) An Introduction to Cybernetics. London: Chapman & Hall Ltd.

Ashby WR (1968) Variety, constraint, and the law of requisite variety. In: Buckley W (ed.) Modern Systems Research for the Behavioral Scientist: A Sourcebook. Chicago, IL: Aldine Publishing Co, pp. 129–136.

Baars H and Kemper H-G (2008) Management support with structured and unstructured data—An integrated business intelligence framework. Information Systems Management 25(2): 132–148.

Baesens B, Bapna R, Marsden JR, et al. (2016) Transformational Issues of Big Data and Analytics in Networked Business. MIS Quarterly 40(4): 807–818.

Baker J, Jones D and Burkman J (2009) Using visual representations of data to enhance sensemaking in data exploration tasks. Journal of the Association for Information Systems 10(7): 533–559.

Beer S (1984) The viable system model: Its provenance, development, methodology and pathology. Journal of the Operational Research Society 35(1): 7–25.

Berinato S (2016) Visualizations that really work. Harvard Business Review 94(6): 92–100.

Bhimani A (2015) Exploring big data’s strategic consequences. Journal of Information Technology 30(1): 66–69.

Biamonte J, Wittek P, Pancotti N, et al. (2017) Quantum machine learning. Nature 549(7671): 195–202.

Blei DM and Smyth P (2017) Science and data science. Proceedings of the National Academy of Sciences 114(33): 8689–8692.

Blum A, Hopcroft J and Kannan R (2020) Foundations of Data Science. Cambridge: Cambridge University Press.

Bonomi F, Milito R, Natarajan P, et al. (2014) Fog computing: A platform for internet of things and analytics. In: Bessis N and Dobre C (eds) Big Data and Internet of Things: A Roadmap for Smart Environments. Cham: Springer, pp. 169–186.

Bostrom RP, Gupta S and Thomas D (2009) A meta-theory for understanding information systems within sociotechnical systems. Journal of Management Information Systems 26(1): 17–48.

Buchanan R (1992) Wicked problems in design thinking. Design Issues 8(2): 5–21.

Buxbaum-Conradi S, Redlich T and Branding J-H (2016) Conceptualizing hybrid human-machine systems and interaction. In: 49th Hawaii international conference on system sciences (HICSS), Koloa, HI, USA, 5-8 January 2016, pp. 551–559. New York, NY: IEEE.

Cao L (2017a) Data science: A comprehensive overview. ACM Computing Surveys (CSUR) 50(3): 43.

Cao L (2017b) Data science: Challenges and directions. Communications of the ACM 60(8): 59–68.

Chen DQ, Preston DS and Swink M (2015) How the use of big data analytics affects value creation in supply chain management. Journal of Management Information Systems 32(4): 4–39.

Chen H, Chiang R and Storey V (2012) Business intelligence and analytics: From big data to big impact. MIS Quarterly 36(4): 1165–1188.

Chen H, Hailey D, Wang N, et al. (2014a) A review of data quality assessment methods for public health information systems. International Journal of Environmental Research and Public Health 11(5): 5170–5207.

Chen M, Mao S and Liu Y (2014b) Big data: A survey. Mobile Networks and Applications 19(2): 171–209.

Chen W, Guo F and Wang F-Y (2015) A survey of traffic data visualization. IEEE Transactions on Intelligent Transportation Systems 16(6): 2970–2984.

Churchman CW (1967) Guest editorial: Wicked problems. Management Science 14(4): B141–B142.

Cichosz P (2014) Data Mining Algorithms: Explained Using R. Chichester: John Wiley & Sons.

Clarke R (2016) Big data, big risks. Information Systems Journal 26(1): 77–90.

Coombs C, Hislop D, Taneva SK, et al. (2020) The strategic impacts of Intelligent automation for knowledge and service work: An interdisciplinary review. The Journal of Strategic Information Systems 29(4): 101600.

Cox A (2005) What are communities of practice? A comparative review of four seminal works. Journal of Information Science 31(6): 527–540.

Cybulski JL, Keller S and Saundage D (2015) Interactive exploration of data with visual metaphors. International Journal of Software Engineering and Knowledge Engineering 25(02): 231–252.

Dallemule L and Davenport TH (2017) What’s your data strategy? Harvard Business Review 95(3): 112–121.

Danowski JA (1993) Network analysis of message content. Progress in Communication Sciences 12: 198–221.

D’Aveni R (2015) The 3-D printing revolution. Harvard Business Review 93(5): 40–48.

Davenport TH (2006) Competing on analytics. Harvard Business Review 84(1): 98.

Davenport TH and Kirby J (2015) Beyond automation. Harvard Business Review 93(6): 58–65.

Davenport TH and Kirby J (2016) Just how smart are smart machines? MIT Sloan Management Review 57(3): 21–25.

Davis E and Marcus G (2015) Commonsense reasoning and commonsense knowledge in artificial intelligence. Communications of the ACM 58(9): 92–103.

De Reuver M, Sørensen C and Basole RC (2018) The digital platform: A research agenda. Journal of Information Technology 33(2): 124–135.

Dhar V (2013) Data science and prediction. Communications of the ACM 56(12): 64–73.

Dietvorst BJ, Simmons JP and Massey C (2016) Overcoming algorithm aversion: People will use imperfect algorithms if they can (even slightly) modify them. Management Science 64(3): 1155–1170.

Dilla W, Janvrin DJ and Raschke R (2010) Interactive data visualization: New directions for accounting information systems research. Journal of Information Systems 24(2): 1–37.

Domino’s (2019) DOM pizza checker. Available at: https:// dompizzachecker.dominos.com.au/ (accessed 2 July 2019).

Donoho D (2017) 50 years of data science. Journal of Computational and Graphical Statistics 26(4): 745–766.

Edmondson AC (2016) Wicked problem solvers. Harvard Business Review 94(6): 52–59.

Edmunds A and Morris A (2000) The problem of information overload in business organisations: A review of the literature. International Journal of Information Management 20(1): 17–28.

Fekete J-D, Van Wijk JJ, Stasko JT, et al. (2008) The value of information visualization. In: Kerren A, Stasko JT and Fekete J-D, et al. (eds) Information Visualization. Springer, pp. 1–18. Available at: http://link.springer.com/chapter/10.1007/978-3-540-70956-5\_1 (accessed 3 October 2016).

Fruchterman TM and Reingold EM (1991) Graph drawing by force-directed placement. Software: Practice and Experience 21(11):: 1129–1164.

Fukunaga AS and Korf RE (2007) Bin completion algorithms for multicontainer packing, knapsack, and covering problems. Journal of Artificial Intelligence Research 28: 393–429.

Galliers RD, Newell S, Shanks G, et al. (2017) Datification and its human, organizational and societal effects: The strategic opportunities and challenges of algorithmic decision-making. The Journal of Strategic Information Systems 26(3): 185–190.

Gartner (2018) Magic Quadrant for Data Science and Machinelearning Platforms. Gartner. Available at: https://www.gartner. com/en/documents/3860063/magic-quadrant-for-data-science-and-machine-learning-pla0/ (accessed 14 January 2020).

Ghasemaghaei M, Ebrahimi S and Hassanein K (2018) Data analytics competency for improving firm decision making performance. The Journal of Strategic Information Systems 27(1): 101–113.

Ghasemaghaei M, Hassanein K and Turel O (2017) Increasing firm agility through the use of data analytics: The role of fit. Decision Support Systems 101: 95–105.

Goldstein J (2011) Introduction by Jeffrey Goldstein to variety, constraint, and the law of requisite variety. Emergence: Complexity and Organization 13(1/2): 190.

Goodfellow I, Bengio Y and Courville A (2016) Deep Learning. Cambridge, MA: The MIT Press.

Gray P (1987) Group decision support systems. Decision Support Systems 3(3): 233–242.

Greengard S (2017) Making chips smarter. Communications of the ACM 60(5): 13–15.

Grover V, Chiang RHL, Liang T-P, et al. (2018) Creating strategic business value from big data analytics: A research framework. Journal of Management Information Systems 35(2): 388–423.

Günther WA, Rezazade Mehrizi MH, Huysman M, et al. (2017) Debating big data: A literature review on realizing value from big data. The Journal of Strategic Information Systems 26(3): 191–209.

Guszcza J, Rahwan I, Bible W, et al. (2018) Why we need to audit algorithms. Harvard Business Review (Digital Article), 28 November. Available at: https://hbr.org/2018/11/why-weneed-to-audit-algorithms (accessed 13 December 2018).

Hackman JR and Wageman R (1995) Total quality management: Empirical, conceptual, and practical issues. Administrative Science Quarterly 40(June): 309–342.

Han J, Kamber M and Pei J (2011) Data Mining: Concepts and Techniques, Third Edition (3rd edn). Burlington, MA: Morgan Kaufmann.

Hayashi AM (2014) Thriving in a big data world. MIT Sloan Management Review 55(2): 35–39.

Heer J and Shneiderman B (2012) Interactive dynamics for visual analysis. Communications of the ACM 55(4): 45–54.

Heule MJH and Kullmann O (2017) The science of Brute Force. Communications of the ACM 60(8): 70–79.

Heylighen F and Joslyn C (2001) Cybernetics and second-order cybernetics. In: Meyers RA (ed.) Encyclopedia of Physical Science & Technology, vol. 4. New York: Academic Press, pp. 155–170.

Hibbeln M, Jenkins JL, Schneider C, et al. (2017) How is your user feeling? Inferring emotion through human-computer interaction devices. MIS Quarterly 41(1): 1–21.

Hollan J, Hutchins E and Kirsh D (2000) Distributed cognition: Toward a new foundation for human-computer interaction research. ACM Transactions on Computer-Human Interaction (TOCHI) 7(2): 174–196.

Holsapple CW, Hsiao S-H and Pakath R (2018) Business social media analytics: Characterization and conceptual framework. Decision Support Systems 110: 32–45.

Holt D (2016) Branding in the age of social media. Harvard Business Review 94(3): 40–50.

Hopcroft JE and Ullman JD (1979) An Introduction to Automata Theory, Languages, and Computation (1st edn). Philippines: Addison-Wesley Publishing Company.

Hossain M and Kauranen I (2015) Crowdsourcing: A comprehensive literature review. Strategic Outsourcing: An International Journal 8(1): 2–22.

Introna LD (1991) Example from Lecture Series on Information Management. University of Pretoria.

Isenberg P, Elmqvist N, Scholtz J, et al. (2011) Collaborative visualization: Definition, challenges, and research agenda. Information Visualization 10(4): 310–326.

Jackson P (1998) Introduction to Expert Systems. Boston, MA: Addison-Wesley Longman Publishing Co., Inc.

Jawandhiya P (2018) Hardware design for machine learn ing. International Journal of Artificial Intelligence & Applications 9(1): 63–84.

Kahneman D and Tversky A (1984) Choices, values, and frames. American Psychologist 39(4): 341.

Kahneman D, Rosenfield AM, Gandhi L, et al. (2016) Noise: How to overcome the high, hidden cost of inconsistent decision making. Harvard Business Review 94(10): 38–46.

Kambatla K, Kollias G, Kumar V, et al. (2014) Trends in big data analytics. Journal of Parallel and Distributed Computing 74(7): 2561–2573.

Karpatne A, Atluri G, Faghmous JH, et al. (2017) Theoryguided data science: A new paradigm for scientific discovery from data. IEEE Transactions on Knowledge and Data Engineering 29(10): 2318–2331.

Keenan PB and Jankowski P (2019) Spatial decision support systems: Three decades on. Decision Support Systems 116: 64–76.

Keim DA (2001) Visual exploration of large data sets. Communications of the ACM 44(8): 38–44.

Keim DA (2002) Information visualization and visual data mining. IEEE Transactions on Visualization and Computer Graphics 8(1): 1–8.

Keim DA, Mansmann F, Schneidewind J, et al. (2008) Visual analytics: Scope and challenges. In: Simoff SJ, Böhlen MH and Mazeika A (eds) Visual Data Mining, Lecture Notes in Computer Science 4404. Berlin: Springer, pp. 76–90.

King G (2011) Ensuring the data-rich future of the social sciences. Science 331(6018): 719–721.

Kratzwald B, Ilić S, Kraus M, et al. (2018) Deep learning for affective computing: Text-based emotion recognition in decision support. Decision Support Systems 115: 24–35.

Kurzhals K, Burch M, Pfeiffer T, et al. (2015) Eye tracking in computer-based visualization. Computing in Science Engineering 17(5): 64–71.

Lacity M (2018) The cogs and wrenches of cognitive automation. In: Lacity M and Willcocks LP (eds) Robotic Process and Cognitive Automation: The Next Phase. Stratford upon Avon: SB Publishing., pp. 95–144

Lacity M and Willcocks LP (2018) Robotic Process and Cognitive Automation: The Next Phase. Ashford: SB Publishing.

Landset S, Khoshgoftaar TM, Richter AN, et al. (2015) A survey of open source tools for machine learning with big data in the Hadoop ecosystem. Journal of Big Data 2(1): 24.

Latour B (1996) On actor-network theory: A few clarifications. Soziale Welt 47(4): 369–381.

Lease M (2011) On quality control and machine learning in crowdsourcing. In: Workshops at the twenty-fifth AAAI conference on artificial intelligence, San Francisco, CA, 7–11 August 2011.

Leonard-Barton D (1992) Core capabilities and core rigidities: A paradox in managing new product development. Strategic Management Journal 13(S1): 111–125.

Lerner JS, Li Y, Valdesolo P, et al. (2015) Emotion and decision making. Annual Review of Psychology 66(1): 799–823.

Linden T and Cybulski JL (2009) Application of hermeneutics to studying an experience mining process. Journal of Information Technology 24(3): 231–250.

Liu Z, Nersessian N and Stasko J (2008) Distributed cognition as a theoretical framework for information visualization. IEEE Transactions on Visualization and Computer Graphics 14(6): 1173–1180.

Lowry PB, D’Arcy J, Hammer B, et al. (2016) “Cargo Cult” science in traditional organization and information systems survey research: A case for using nontraditional methods of data collection, including Mechanical Turk and online panels. The Journal of Strategic Information Systems 25(3): 232–240.

Luca M, Kleinberg J and Mullainathan S (2016) Algorithms need managers, too. Harvard Business Review 94(1): 96–101.

Lycett M (2013) ‘Datafication’: Making sense of (big) data in a complex world. European Journal of Information Systems 22(4): 381–386.

Malone TW (2018) How Human-Computer “Superminds” Are Redefining the Future of Work. MIT Sloan Management Review 59(4): 34–41.

Mangold WG and Faulds DJ (2009) Social media: The new hybrid element of the promotion mix. Business Horizons 52(4): 357–365.

Martin RL and Golsby-Smith T (2017) Management is much more than a science: The limits of data-driven decision making. Harvard Business Review 95(5): 128–135.

Martinez M and Walton B (2014) The wisdom of crowds: The potential of online communities as a tool for data analysis. Technovation 34(4): 203–214.

Martinez-Maldonado R, Kay J, Shum SB, et al. (2019) Collocated collaboration analytics: Principles and dilemmas for mining multimodal interaction data. Human–Computer Interaction 34(1): 1–50.

Mason RO (2017) Four ethical issues of the information age. In: Weckert J (ed.) Computer Ethics (Ebook) (1st edn). London: Routledge, pp. 41–48.

Maturana HR and Varela FJ (1991) Autopoiesis and Cognition: The Realization of the Living. Dordrecht, Netherlands: Springer Science & Business Media.

Medeiros MM, De Hoppen N and Maçada ACG (2020) Data sci ence for business: Benefits, challenges and opportunities. The Bottom Line 33(2): 149–163.

Moldoveanu MC (2016) Algorithmic foundations for business strategy. 17–036, Working Paper. Boston, MA: Harvard Business School.

Monroe D (2018) Chips for artificial intelligence. Communications of the ACM 61(4): 15–17.

Morey T, Forbath T and Schoop A (2015) Customer data: Designing for transparency and trust. Harvard Business Review 93(5): 96–105.

Müller O, Fay M and Vom Brocke J (2018) The effect of big data and analytics on firm performance: An econometric analysis considering industry characteristics. Journal of Management Information Systems 35(2): 488–509.

Newell A, Shaw JC and Simon HA (1959) Report on a general problem solving program. In: IFIP congress, Paris, France, 15-20 June 1959, p. 64. Pittsburgh, PA.

Newell S and Marabelli M (2015) Strategic opportunities (and challenges) of algorithmic decision-making: A call for action on the long-term societal effects of “datification.” The Journal of Strategic Information Systems 24(1): 3–14.

news.com.au (2017) Domino’s answer to common pizza gripe. Available at: https://www.news.com.au/finance/business/ retail/dominos-launches-hightech-solution-to-common-pizzagripe/news-story/ed763ef8a666cba0d53a7aa834161ae9#. onuqu (accessed 2 July 2019).

Nonaka I and Takeuchi H (2007) The knowledge-creating com pany. Harvard Business Review 85(7/8): 162–171.

Olshannikova E, Ometov A, Koucheryavy Y, et al. (2015) Visualizing big data with augmented and virtual reality: Challenges and research agenda. Journal of Big Data 2(1): 22.

Osgood CE (1959) The representational model and relevant research materials. In: Pool I (ed.) Trends in Content Analysis. Urbana, IL: University of Illinois Press, pp. 33–88.

Oxford Dictionaries (2018) Definition of cognition in English. Available at: https://en.oxforddictionaries.com/definition/ cognition (accessed 27 October 2018).

Paré G, Trudel M-C, Jaana M, et al. (2015) Synthesizing information systems knowledge: A typology of literature reviews. Information & Management 52(2): 183–199.

Pierson L (2015) Data Science for Dummies (1st edn). Hoboken, NJ: For Dummies.

Piller F, Vossen A and Ihl C (2012) From social media to social product development: The impact of social media on co-creation of innovation. Die Unternehmung 66(1): 7–27.

Porter ME and Heppelmann JE (2017) Why every organization needs an augmented reality strategy. Harvard Business Review 95(6): 46–57.

Poulis K and Poulis E (2016) Problematizing fit and survival: Transforming the law of requisite variety through complexity misalignment. Academy of Management Review 41(3): 503–527.

Pouyanfar S, Sadiq S, Yan Y, et al. (2018) A survey on deep learning: Algorithms, techniques, and applications. ACM Computing Surveys 51(5): 921–92:36.

Provost F and Fawcett T (2013) Data science and its relationship to big data and data-driven decision making. Big Data 1(1): 51–59.

Ransbotham S, Kiron D and Prentice PK (2015) Minding the analytics gap. MIT Sloan Management Review 56(3): 63–68.

Ransbotham S, Kiron D, Gerbert P, et al. (2017) Reshaping business with artificial intelligence: Closing the gap between ambition and action. MIT Sloan Management Review 59(1).

Russom P (2011) Big data analytics. TDWI Best Practices Report. The Data Warehousing Institute TDWI. Available at: http://tdwi.org/research/2011/09/best-practices-reportq4-big-data-analytics/asset.aspx?tc=assetpg (accessed 18 November 2012).

Sacha D, Senaratne H, Kwon BC, et al. (2016) The role of uncertainty, awareness, and trust in visual analytics. IEEE Transactions on Visualization and Computer Graphics 22(1): 240–249.

Saiyeda A and Mir MA (2017) Cloud computing for deep learning analytics: A survey of current trends and challenges. International Journal of Advanced Research in Computer Science 8(2): 68–72.

Sargut G and McGrath RG (2011) Learning to live with complexity. Harvard Business Review 89(9): 68–76.

Sawyer S and Jarrahi MH (2014) Sociotechnical approaches to the study of information systems. In: Tucker A and Topi H (eds) Computing Handbook, Third Edition: Information Systems and Information Technology. Boca Raton, FL: CRC Press, pp. 5–1.

Schatsky D and Puliyakodil RK (2017) From fantasy to reality: Quantum computing is coming to the marketplace. Available at: https://www2.deloitte.com/insights/us/en/focus/signalsfor-strategists/quantum-computing-enterprise-applications. html (accessed 7 March 2018).

Scheepers R, Lacity MC and Willcocks LP (2018) Cognitive automation as part of Deakin University’s digital strategy. MIS Quarterly Executive 17(2): 89–107.

Schinckus C (2018) An essay on financial information in the era of computerization. Journal of Information Technology 33(1): 9–18.

Schroeck M, Shockley R, Smart J, et al. (2012) Analytics: The Real-World Use of Big Data: How Innovative Enterprises Extract Value from Uncertain Data. IBM Institute for Business Value. Available at: https://www.informationweek.com/pdf\_whitepapers/approved/1372892704\_analytics\_the\_real\_world\_ use\_of\_big\_data.pdf (accessed 15 January 2021).

Sedgewick R and Wayne K (2011) Algorithms (4th edn). Upper Saddle River, NJ: Addison-Wesley Professional.

Shalev-Shwartz S and Ben-David S (2014) Understanding Machine Learning: From Theory to Algorithms. Cambridge: Cambridge University Press.

Simon HA (1972) Theories of bounded rationality. Decision and Organization 1(1): 161–176.

Simon HA (1979) Rational decision making in business organizations. The American Economic Review 69(4): 493–513.

Singh D and Reddy CK (2015) A survey on platforms for big data analytics. Journal of Big Data 2(1): 1–20.

Smith G (2020) Data mining fool’s gold. Journal of Information Technology 35(3): 182–194.

Sonnenburg S, Braun ML, Ong CS, et al. (2007) The need for open source software in machine learning. Journal of Machine Learning Research 8: 2443–2466.

Spiekermann S and Korunovska J (2017) Towards a value theory for personal data. Journal of Information Technology 32(1): 62–84.

Steelman ZR, Hammer BI and Limayem M (2014) Data collection in the digital age: Innovative alternatives to student samples. MIS Quarterly 38(2): 355–378.

Steinberg DM and Aronovich E (2020) Thoughts on data science in business and industry. Applied Stochastic Models in Business and Industry 36(1): 36–40.

Stodder D (2016) Improving Data Preparation for Business Analytics: Applying Technologies and Methods for Establishing Trusted Data Assets for More Productive Users. Best Practices Report. TDWI (co-sponsored by RedPoint). Available at: https://www.redpointglobal.com/wp-content uploads/2016/10/TDWI\_BPReport\_Q316\_RedPoint\_F\_ rev2\_code\_Final.pdf (accessed 15 January 2021).

Tamaddoni A, Stakhovych S and Ewing M (2016) Comparing churn prediction techniques and assessing their performance: A contingent perspective. Journal of Service Research 19(2): 123–141.

Trieu V-H (2017) Getting value from business intelligence systems: A review and research agenda. Decision Support Systems 93: 111–124.

Tversky A and Kahneman D (1974) Judgment under uncertainty: Heuristics and biases. Science 185(4157): 1124–1131.

Tversky A and Kahneman D (1986) Rational choice and the fram ing of decisions. Journal of Business 59(4): S251–S278.

Van der Aalst W (2016) Data science in action. In: Van der Aalst W (ed.) Process Mining: Data Science in Action. Berlin: Springer, pp. 3–23.

Vicario G and Coleman S (2020) A review of data science in business and industry and a future view. Applied Stochastic Models in Business and Industry 36(1): 6–18.

Wall E, Blaha LM, Paul CL, et al. (2018) Four perspectives on human bias in visual analytics. In: Ellis G (ed.) Cognitive Biases in Visualizations. Cham: Springer International Publishing, pp. 29–42.

Waller MA and Fawcett SE (2013) Data science, predictive analytics, and big data: A revolution that will transform supply chain design and management. Journal of Business Logistics 34(2): 77–84.

Watson HJ, Annino DA, Wixom BH, et al. (2001) Current practices in data warehousing. Information Systems Management 18(1): 47–55.

Watts DJ (2011) Everything Is Obvious: Once You Know the Answer (1st edn). New York: Crown Business.

Wenger EC and Snyder WM (2000) Communities of practice: The organizational frontier. Harvard Business Review 78(1): 139–146.

Wilson HJ and Daugherty PR (2018) Collaborative intelligence: Humans and AI are joining forces. Harvard Business Review (Digital Article), 1 July. Available at: https://hbr.org/2018/07/ collaborative-intelligence-humans-and-ai-are-joining-forces (accessed 11 December 2018).

Winograd T, Flores F and Flores FF (1986) Understanding Computers and Cognition: A New Foundation for Design. Norwood, NJ: Ablex Publishing Intellect.

Yi S, Hao Z, Qin Z, et al. (2015) Fog computing: Platform and applications. In: 2015 Third IEEE Workshop on Hot Topics in Web Systems and Technologies (HotWeb), pp. 73–78. IEEE. Available at: http://citeseerx.ist.psu.edu/viewdoc/downloa d?doi=10.1.1.702.7479&rep=rep1&type=pdf (accessed 15 January 2021).

Zhang Z and Gupta BB (2016) Social media security and trustworthiness: Overview and new direction. Future Generation Computer Systems 86: 914–925.

## Author biographies

Jacob Cybulski is an Associate Professor in Deakin Business School, Department of Information Systems and Business Analytics at Deakin University. He is a Discipline Leader in Business Analytics and undertakes research, consulting and teaching in data analytics, machine learning and data visualisation. He managed large cross-institutional research programs in data visualization, business analytics and e-simulations, which received national awards in Australia. He completed and published results of several large projects funded by the government and industry.

<table><tr><td>Limitations:</td></tr><tr><td>Phenomenon complexityDifficult problems, commonly due to socio-political contexts, which do not easily yield to technological solutions (Buchanan, 1992; Churchman, 1967; Edmondson, 2016)Existence of intractable (NP-complete) problems (Sedgewick and Wayne, 2011: Chapter 6.6)Formation of hard-to-deal-with digital subcultures (Holt, 2016)</td></tr><tr><td>Cognitive limitationsCognitive biases (Tversky and Kahneman, 1974, 1986) resulting from poor memories, false beliefs (Watts, 2011) and emotions (Lerner et al., 2015)Human reasoning suffering from bounded rationality, satisficing, and optimizing (Simon, 1972), leading to poor decisions, over-reliance on intuition, introspection, and common-senseInconsistency of human decisions (noise) in organizations (Kahneman et al., 2016)Advances in data science to extend cognitive capabilities (given limitations above):</td></tr><tr><td>Automated decision-making to support exploration, consistency, and self-improvementReplacement of intuition with plausible reasoning (Davis and Marcus, 2015)Expert and general problem-solving (Jackson, 1998; Newell et al., 1959)Mechanization of insight generation and decision-making (Arnott and Pervan, 2005)Human intelligence augmentation (Davenport and Kirby, 2015)</td></tr><tr><td>Distributed cognition to extend individual cognitive capabilitiesDistributed cognition support (Hollan et al., 2000; Liu et al., 2008)Communities of practice and crowd-based problem-solving (Wenger and Snyder, 2000)Group decision support systems to facilitate negotiation and consensus building (Gray, 1987)Emergence of organizational cognitive architectures (Davenport and Kirby, 2016)</td></tr></table>

Rens Scheepers is a Professor in the Department of Information Systems and Business Analytics at Deakin University. He currently serves as theme leader for Business & Technology research at the Deakin Business School. His research focuses on how organisations can derive competitive advantages from the application of contemporary information and communication technologies and systems.

## Appendix

## Literature content analysis—limitations and advances in data, method, interfaces, and cognition

This appendix summarizes the manual content analysis (part of Stage 2, Figure 1) of literature pertinent to developments in data science of relevance to modern organizational contexts. While many recent surveys have considered benefits and challenges of data science in business (Günther et al., 2017; Steinberg and Aronovich, 2020; Vicario and Coleman, 2020), in this article, data science advances and limitations were reviewed from the cybernetic vantage point of an organizational capability seeking to control data-intensive business phenomena. The list of journals that formed the basis for this review appears in Table 1. The review process was guided by the concepts, their relationships and groupings, as well as terminology, which were identified in the previous stage of research and presented in the co-occurrence network and domain model (Figure 2). Insights of this content analysis are collected in Tables 5 to 8, which were subsequently summarized in Data Science Organizational Framework (DSOF) framework (depicted in Figure 3). Much of the extant literature tends to place an emphasis on data science breakthroughs, with only a few scholars giving consideration to the complexities and limitations of their deployment in organizational practice (e.g. Lacity, 2018; Smith, 2020). This review aims to redress this imbalance.

Table 5. Cognitive limitations and advances in data science alleviating them.  
Table 6. Key limitations and advances in data pertinent to data science.

<table><tr><td>Limitations and challenges:</td></tr><tr><td>• Poor quality of data, not relevant or reliable</td></tr><tr><td>○ Lack of data validity, identity, signification, accuracy, precision, relevance, currency, completeness, controls, and auditability (Chen et al., 2014a; Clarke, 2016)</td></tr><tr><td>○ Big data has no focus so it is often tangential to the analytic task (Agarwal and Dhar, 2014)</td></tr><tr><td>○ Big data often includes too many patterns (Hayashi, 2014)</td></tr><tr><td>○ Lack of trust and transparency in data management (Morey et al., 2015)</td></tr></table>

## Table 6. (Continued)

• Issues with data volume, distribution, access, and fragmentation

 Technical limitations of big data analytics (Kambatla et al., 2014)

 Legal and ethical aspects of data privacy, accuracy, and accessibility (King, 2011; Mason, 2017)

 Unwillingness to share data, information, and experience (Linden and Cybulski, 2009)

• High velocity and rapid change of data

 Need for data-driven business strategies (Baesens et al., 2016; Dallemule and Davenport, 2017)

 Large amounts of data redefine organizational relationships (Bhimani, 2015)

 Data represents and shapes new hyper-reality (Schinckus, 2018)

Advances in data pertinent to data science:

• Mass conceptualization and codification

 Data re-represents the world phenomena, global effort to conceptualize and codify the world, which improves sense-making

and informed decision-making (Galliers et al., 2017; Lycett, 2013)

• Vast repositories of structured and unstructured data

 Availability of structured and unstructured data (Baars and Kemper, 2008)

 New storage models for large and high velocity (Watson et al., 2001)

 Emergence of efficient data processing models and tools (Chen et al., 2014b)

• Information services / systems

 Data processing systems and services—no need for own data infrastructure (Stodder, 2016)

 Creation of new digital platforms and ecosystems (De Reuver et al., 2018)

• Availability of rich and real-time data for private and business use

 Open data for business and public use (Chen et al., 2014b; Günther et al., 2017)

 Personal information traded as a commodity (Spiekermann and Korunovska, 2017)

## Table 7. Key limitations and advances in methods pertinent to data science.

## Limitations:

• Computationally challenging problems and sub-optimal solution

 Some complex solutions will remain sub-optimal (Sargut and McGrath, 2011)

 Some problems are computationally unsolvable (Fukunaga and Korf, 2007; Moldoveanu, 2016)

• Narrow, domain-specific solutions

 Difficulties in capturing and analysis of tacit knowledge (Nonaka and Takeuchi, 2007)

 Algorithms encode human biases, rumors, disinformation, or opinions (Guszcza et al., 2018)

 Data analytics cannot replace logic, teamwork, or persuasion (Martin and Golsby-Smith, 2017)

 Algorithms are literal and often black boxes (Luca et al., 2016)

• Human and organizational factors affecting effectiveness of methods

 Data analytics costly and time-consuming (Davenport, 2006)

 Unreliable machine problem-solving (Lowry et al., 2016; Steelman et al., 2014)

 Potential abuse of algorithmic decision-making (Newell and Marabelli, 2015)

 Fear of algorithms and machines (Aleksander, 2017; Dietvorst et al., 2016)

 Gap between analytics and their effective applications (Ransbotham et al., 2015)

Advances in methods pertinent to data science:

• Conceptual foundations enabling new modes of analysis

 Mathematical foundations for data science (Blum et al., 2020)

 New computational mathematics and algorithms (Cichosz, 2014; Heule and Kullmann, 2017)

 Advances in scientific theory and model development (Karpatne et al., 2017)

 Emergence of transdisciplinary data science (Blei and Smyth, 2017; Cao, 2017b)

• Technical software methods providing sophisticated functionality

 Machine learning algorithms (Han et al., 2011; Shalev-Shwartz and Ben-David, 2014)

 Text, sentiment, and social media analytics (Holsapple et al., 2018)

 Big data analytics for business (Chen et al., 2012)

 Deep learning and the (new) AI (Goodfellow et al., 2016; Pouyanfar et al., 2018)

 Robotic process and cognitive automation (Lacity and Willcocks, 2018)

 Availability of data science and machine learning platforms (Gartner, 2018)

 Availability of open-source machine learning tools (Landset et al., 2015; Sonnenburg et al., 2007)

• Technical hardware offering high performance and affordable processing

 Computer networks and clusters for big data analytics (Singh and Reddy, 2015)

 Cloud services for high-performance machine learning (Saiyeda and Mir, 2017)

 Specialized hardware for analytics and AI (Greengard, 2017; Jawandhiya, 2018; Monroe, 2018)

 Internet of Things (IoT) and fog computing for analytics (Bonomi et al., 2014; Yi et al., 2015)

 Quantum machine learning (Biamonte et al., 2017; Schatsky and Puliyakodil, 2017)

## Table 7. (Continued)

<table><tr><td>Socio-technical methods enabling collaborative problem-solving</td></tr><tr><td>Collaboration and distributed cognition (Hollan et al., 2000)Communities of practice, interest, and expertise (Cox, 2005)Crowdsourcing for data analysis (Hossain and Kauranen, 2015; Martinez and Walton, 2014)Human-machine collaboration and “superminds” (Malone, 2018; Wilson and Daugherty, 2018)</td></tr></table>

## Table 8. Key limitations and advances in interfaces pertinent to data science.

<table><tr><td>Limitations:</td></tr><tr><td>• Abstract, unstructured, and complex business data hard to visualize○ Visualization of large and abstract business data is difficult (Dilla et al., 2010)</td></tr><tr><td>• Lack of visual metaphors fit for business applications○ Difficulty selecting effective visual metaphor (Chen et al., 2015)○ Difficulty in visualizing business data (Al-Kassab et al., 2014; Edmunds and Morris, 2000)○ Behavioral habits and cognitive biases lower effectiveness of visualization (Sacha et al., 2016)</td></tr><tr><td>• Difficulty to represent some business phenomena with the available visual methods○ Using visualization requires special skills and training (Berinato, 2016; Wall et al., 2018)○ Difficulties collaborating via visual forms (Martinez-Maldonado et al., 2019)</td></tr><tr><td>Advances in interfaces pertinent to data science:</td></tr><tr><td>• Rich variety of tools for data visualization and vocalization○ Data visualization amplifies cognition (Fekete et al., 2008; Keenan and Jankowski, 2019)○ Visual exploration simplifies analysis of very large data sets (Keim, 2001, 2002)○ Visual metaphors make data easier to understand (Cybulski et al., 2015)○ Physical representations of data are now possible, for example, 3D printing (D&#x27;Aveni, 2015)</td></tr><tr><td>• Rich variety of interactivity types to aid data visualization○ Interactivity improves visualizations (Heer and Shneiderman, 2012)○ Detecting emotions possible (Hibbeln et al., 2017; Kratzwald et al., 2018; Kurzhals et al., 2015)○ Augmented reality for businesses (Olshannikova et al., 2015; Porter and Heppelmann, 2017)○ Hybrid human-machine systems (Buxbaum-Conradi et al., 2016)</td></tr><tr><td>• Support for collaborative data visualization and exploration○ Collaboration via interactive visual analytics (Isenberg et al., 2011)○ Interactive visualization for distributed cognition (Liu et al., 2008)</td></tr></table>

While the practical data science processes typically commence with data, then application of methods and interfaces, the overarching objective is enhanced cognitive understanding of a phenomenon. As such, the review commences with cognition as pivotal in the data science domain. Note also that due to very large number of references summarized in this appendix, for the sake of readability, we refrained from duplicating references listed in tables and table descriptions.

Cognition. Human cognition can be defined as the mental action or process of acquiring knowledge and understand ing through thought, experience, and the senses (Oxford Dictionaries, 2018). These cognitive faculties translate to learning, decision-making, insight generation, and problem-solving that could be supported through data science in modern organizations. Application of data science in this area provides clear benefits to human cognitive processes but also faces some challenges (see Table 5).

Many business phenomena are complex. Decisionmakers operate in challenging multidisciplinary sociopolitical contexts and must rely on organizational subgroups with highly specialized skills (such as AI and data analytics). Such subgroups often exhibit subcultures (e.g. “hacker” communities) which can be foreign to traditional business decision processes.

Human cognition has limitations in dealing with complexity. Poor memory, false beliefs, bias, and emotions commonly impair evidence-based reasoning required in modern decision processes. Herbert Simon coined the notion of satisficing as a cognitive heuristic when decisionmakers are seeking to identify optimal solutions under certain conditions. He observed that when there is a lack of information, or when there just are too many alternatives to consider exhaustively, decision-makers tend to satisfice: they either seek optimum solutions for simplified scenarios or try to find sub-optimal solutions for realistic scenarios. Decision-makers also exhibit bounded rationality, whereby their actions are often only partly rational and even irrational.

This behavior affects the development of effective strategies and action plans, resulting in poor outcomes, inconsistencies, distortions, and incorrect judgments. Data science can help alleviate decision-makers’ inherent cognitive limitations. In general, data science utilizes data to create methods of automating, part-automating, or assisting human cognitive tasks (Dhar, 2013). With the proliferation of data and new algorithm design, data science could reduce the reliance on intuition and support plausible reasoning, expert and general problem-solving, and automatic decision-making. This could overcome the bounded rationality of individuals and their cognitive biases in some decisionmaking scenarios, potentially reducing decision-makers inclination to satisfice.

As articulated in the theories of distributed cognition and communities of practice, cognition extends beyond the individual mind. Collective problem-solving, interpretation, and insight generation can be especially effective when supported with suitable technology capable of offloading human memory and extending cognitive abilities with analytics.

Data. Contemporary society is engaged in mass conceptualization and codification of world phenomena, leading to re-representation of the world, including the business world, in data (see Table 6). Consequently, in organizational contexts, terms such as big data and digital transformation have become commonplace. Most organizations today have access to systems and services allowing processing and storage of data, such as projects, products, transactions, employees, and customers. Personal information becomes a valuable commodity. These trends allow organizations to engage in evidence-based sense-making and informed decision-making.

That said, much of the data that are available to organizations exhibit significant limitations (Lacity, 2018, pp. 111–113). For example, data can often be invalid, unreliable, inaccurate, or subjective. Data may be lacking organizational relevance, be too complex to manage, or hard to verify. Labels such as fake news and fake data are often used to call into question the trustworthiness of data and entire data sources (Zhang and Gupta, 2016).

Furthermore, despite the proliferation of data throughout society, much of the data available to organizations are fragmented over multiple repositories or are in different formats and thus impractical to integrate and utilize. Data on particular phenomena are often not available, inaccessible, or difficult to use. This might be due to technical, ethical, and legal reasons. Moreover, many individuals and/or organizations do not participate in the activities of information sharing and do not disseminate their collected information or experience publicly.

This proliferation of data has given rise to new managerial challenges such as information overload, appropriate data governance, and dealing with information privacy/ confidentiality, all of which require new organizational approaches, strategies, and developments. The majority of organizations today have access to large shared data repositories that redefine the nature of business relationships and introduce the notion of information alliances centered around creation and maintenance of shared data resources.

Access to global information sources alters business processes and creates a business environment where datarelated events and their perceptions can have tremendous impacts on markets, finance, and the global economy. This implies significant challenges for business but also opens new opportunities.

Much of today’s organizational and extra-organizational data are semi-structured or unstructured, often consisting of text, media artifacts, and logs created, stored, and shared by the collective effort of communities on a global scale. This richness, level of detail, and the real-time nature of such data are valuable attributes of this resource. A significant amount of business and personal data are commoditized, traded, and exchanged, rendering this useful in analyzing market trends, or probing views and opinions of customers. Monitoring and efficient processing of high-velocity social media has been instrumental in areas such as new product development and customer service management (Mangold and Faulds, 2009; Piller et al., 2012). In addition, there is a wealth of commercial and open data services today that provide new data services, analytics infrastructure, and digital platforms to support maintenance of data sources and processing to inform business decision-making (Baars and Kemper, 2008).

Method. Data science provides methods of automating data acquisition, transformation, reasoning and insight generation, decision-making and problem-solving (Dhar, 2013), as well as supporting idea generation and knowledge creation in organizations. Such methods rely on conceptual and theoretical, technical (software and hardware), and socio-technical advances, which aim to increase organizational decision-making capabilities (see Table 7).

Despite the recent advances in data science, several limitations remain in its methods’ applicability to business today (Lacity, 2018, pp. 113–114). Optimal solutions to many classes of complex business problems remain challenging. For example, optimization of production schedules, container utilization in logistics, and so on are NP-complete, that is, their direct algorithmic solutions require nondeterministic polynomial time (Hopcroft and Ullman, 1979: 323–324). This means that as the size of the problem grows, the time required for solving it computationally becomes unreasonably long. Consequently, workable approaches are often “sub-optimal,” with heuristics or probabilistic estimations as the only alternative.

Furthermore, recent methodological developments tend to be either highly domain-specific or geared toward engi neering and scientific problems, with little impact within a broader business domain. While some data science methods successfully transitioned to business applications, many suffer in their ability to accommodate individual and organizational biases and prejudices. Some methods are “black boxes,” with an inability to adequately explain inherent assumptions, justify predictions, interpretations, and recommendations.

There are technical, human, and organizational factors that limit efficient and effective deployment of data science methods. Some scientific methods are still unreliable for business application. Methods can be open to abuse, which instills some justified fears for both organizations and the general public. Some methods demand extensive and scarce technical or esoteric expertise.

Data science is founded upon conceptual and theoretical advances that assist in data acquisition, exploration, and analysis, leading to decision support. There are many areas of mathematics that lay the grounds for these analytic tasks. Moreover, mathematics itself has become computational. Data science has become transdisciplinary to incorporate methodological concepts and techniques from computer science, artificial intelligence and cognitive science, linguistics, and physics and engineering.

Data science efforts have resulted in the creation of software methods assisting the generation of insights from business data. Examples include machine learning algorithms, predictive models, deep learning, and the “new” artificial intelligence (AI)—the methods constituting the “cogs of cognitive automation” (Lacity, 2018, pp. 96–109).

Large collections of data science software are today routinely packaged into specialist programming languages (e.g. R and Python), large-scale analytic packages (e.g. Tensorflow), and analytics platforms (e.g. AWS). The majority of such resources have been released into the open-source community.

Consequently, the combined efforts of the open-source community and commercial providers have led to a wealth of highly sophisticated data science functionality that is available to organizations, researchers, educators, students, and independent developers today.

Data science software would not be effective without powerful computing hardware. Distributed analytics takes advantage of inter-networked machines, cloud services, and the Internet of Things (IoT). Affordable devices offering massively parallel processing are available to individual developers (e.g. Graphics Processing Units (GPUs)). Specialized AI processors (e.g. Tensor Processing Units (TPUs)) and quantum computers featuring machine learning algorithms are also accessible via inexpensive cloud services from various vendors.

Finally, data science methods consider combinations of machine intelligence with human intelligence, forming the co-called “super-mind.” Some data science cloud platforms offer analytic solutions by relying on the collective “wisdom of the crowd” of individuals, collaborating communities and assistive machine infrastructure. Interestingly, data science aggregator platforms increasingly feature hybrid approaches to data analysis, where machine learning could be applied to crowd-collected data or where machine-generated predictions could be validated by appealing to crowd-generated judgment (Lease, 2011).

Interface. The Interface domain includes variety of mechanisms that enable individuals to turn data into business reports and visualizations, for the purpose of exploration, illustration, aggregation, representation, and communication of the results of analysis (see Table 8). Data science interfaces enable visualization, vocalization, and interaction with such analyses. User interfaces play an important role in bridging the gaps between data complexity and human perception, especially when working in collaborative teams.

Despite the rapid development of computer graphics and natural user interfaces, a number of inherent limitations of interfaces remain in regard to their use in business today (Lacity, 2018, pp. 114–115).

The commonly used business visualizations (e.g. graphs and charts) are often not well suited to the visualization of multi-dimensional and abstract socio-technical data. The nuances of social relationships, events and actions, patterns, and groups do not easily map into intuitive visual representations. The lack of suitable business metaphors for business data representation leads to problems in comprehension and information overload.

In many cases, cognitive biases and poor technical skills, combined with data complexity, impair individuals’ ability to make informed decisions from data science analyses. While terminology, concepts, and their visual representations are often standardized in scientific applications, this is not the case in business. Users may require special skills and training to be effective in dealing with rich visualizations. Sharing and collaboration of business data across geographical boundaries, different languages, and cultures is more difficult, especially in multi-national corporations.

Still, visualization techniques provide a perceptual-cognitive bridge between data, methods, and human cognition. Data visualization assists understanding of data, especially very large data sets, and making sense of complex phenomena that such data represent (Baker et al., 2009). Practical applications of using data visualization techniques can be found across many professional fields, including medicine, engineering, and business (Keim et al., 2008; Russom, 2011; Schroeck et al., 2012).

Data visualization may include screens, surround displays, three-dimensional (3D) visualization using virtual and augmented reality systems, and even physical representation of data (e.g. via 3D printing). Such devices allow to “spatialize” and aggregate abstract data, which help analysts to think by analogy, be creative in problem-solving, and effective in decision-making. Data visualization provides perceptual support and has the potential to stimulate users’ cognition of phenomena.

Some tools extend analytic methods with interactive facilities capable of involving multiple individuals in the process of data filtering, sorting, recording, navigation, transformation and manipulation, as well as the coordination of insights derived from data. Interactivity involves specialized hardware to enhance manipulation of visual artifacts, through touch, gestures and body movement, eye tracking, and facial expression.

Interactive features are particularly important where the analysts are involved in collaborative analysis. A variety of assistive technologies exist today that enable distributed visualization capabilities, data sharing and analytics functionality, and extensive communication infrastructure that support applications in research, command and control, environmental, and mission planning. Collaborative visual analytics empower data analysts to harness social interaction and networking, work parallelization, and social organization.
