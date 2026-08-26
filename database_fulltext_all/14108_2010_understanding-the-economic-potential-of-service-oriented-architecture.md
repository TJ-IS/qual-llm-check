---
otero_id: 14108
otero_key: "VT35T3KJ"
title: "Understanding the Economic Potential of Service-Oriented Architecture"
authors: "Benjamin Mueller; Goetz Viering; Christine Legner; Gerold Riempp"
year: "2010"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222260406"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Understanding the Economic Potential of Service-Oriented Architecture

Ben jamin Mue lle r, Goe tz Vie ring , Chris tine Legn r, and Ge ro ld Riem pp

Benjamin Mueller is a Ph.D. candidate and research assistant at the Institute of Research on Information Systems (IRIS), European Business School (EBS), Wiesbaden/ Oestrich-Winkel, Germany. His research interests include the economic potential of IS architectures, IT performance measurement and management, and the systemic and group aspects of strategic IT management. He has published and presented his research at key international refereed conferences, such as the International Conference on Information Systems (ICIS) and the European Conference on Information Systems (ECIS). Before starting his Ph.D., he graduated in Business Administration from EBS and the Robinson College of Business at Georgia State University in Atlanta. Beyond his research, he has worked as a consultant in the area of IT strategy and IT benchmarking and gathered practical experience with corporations in the United States and Europe.

Goetz Viering is a Ph.D. candidate and research assistant at the Institute of Research on Information Systems (IRIS), European Business School (EBS), Wiesbaden/Oestrich-Winkel, Germany. He holds a Diploma of Business Administration from EBS and an M.S. in International Business from Bond University, Queensland, Australia. His research has mainly focused on the business value of service-oriented architectures and their adoption in practice. He has presented his research at leading international conferences, including the European Conference on Information Systems (ECIS) and Wirtschaftsinformatik.

Christine Leg ner is a Deputy Professor at the Institute of Research on Information Systems (IRIS), European Business School (EBS), Wiesbaden/Oestrich-Winkel, Germany. She was senior lecturer and research project manager at the University of St. Gallen, Switzerland. Dr. Legner received a Ph.D. from the University of St. Gallen (Switzerland), an M.S. in Economics from Université Paris–Dauphine (France), and a Diploma in Industrial Engineering from the University of Karlsruhe (Germany). She has practical and academic experience in designing IS landscapes for global organizations and value chains. Her research interests include business networking, collaborative business processes, inter- and intra-enterprise systems, and service-oriented architectures. She has published more than 30 articles in peer-reviewed journals, including the Journal of the AIS, International Journal of Technology Management, and Electronic Markets, and conference proceedings.

Gerold Riempp is a Full Professor of Information Systems at the European Business School (EBS), Wiesbaden/Oestrich-Winkel, Germany. He is executive director of the Institute of Research on Information Systems (IRIS) at EBS. He was senior lecturer and research project manager at the University of St. Gallen, Switzerland. Dr. Riempp received a Ph.D. from the University of Paderborn, Germany, and graduated with a Diploma in Industrial Engineering from the Technical University of Darmstadt, Germany. His research focuses on strategic IT management, enterprise architecture, knowledge management, and customer relationship management. He has published two books and more than 80 articles in reputed journals and conference proceedings. Riempp has several years of consulting experience, among others at Horváth & Partners, Information Management Group, and PricewaterhouseCoopers.

Ab strac t: Service-oriented architecture (SOA) is one of the most discussed topics in the information systems (IS) discipline. While most computer scientists agree that the service-oriented paradigm has clear benefits in terms of technical quality attributes, it has been difficult to justify SOA economically. The few studies that have investigated the strategic and economic aspects of SOA are mostly exploratory and lack a more comprehensive framework for understanding the sources of its economic potential. Based on IS and SOA literature, our work goes further in suggesting the SOA economic potential model, which describes the causal relationships between the SOA’s style characteristics and value it can provide on the business side. Using this model, we investigate 164 SOA cases published between 2003 and 2008 to explore the economic rationale for adopting SOA. Our findings suggest that SOA’s business benefits are currently mainly driven by operational and information technology infrastructural improvements. However, enterprises also realize strategic benefits from SOA; for example, by electronically integrating with their business partners by means of SOA. We use the results of our study to derive propositions and suggest a research model for future studies on SOA’s economic potential.

Key words and phrases: business benefits, economic potential, IS value, serviceoriented architecture, service science, services.

Serv ic e-oriented arc hitec ture (SOA ) is currently one of the most discussed topics in the information systems (IS) discipline [24, 25, 94]. SOA builds on the concept of services as fundamental elements for the flexible composition of IS landscapes. It promises to resolve many of the existing IS architectures’ limitations such as the difficulties with integrating a growing number of (mostly) monolithic applications (enterprise resource planning [ERP ], customer relationship management, and supply chain management systems) within and across enterprises, or the inability of such IS to quickly adapt to changing requirements. While SOA platforms have become more mature and their implementations have spread, the discussion of SOA’s economic potential is at an early stage. The constantly growing body of research on SOA is mostly technology oriented, focusing on Web services as a specific implementation technology [4, 14, 34, 63] and on various aspects of service design and management [70, 94]. Researchers have, however, more recently started to look at SOA and Web services for specific business domains [1, 2, 7, 44, 75, 76]. While the technological understanding of SOA is refined by this discussion, its economic impact and business value are yet to be explored [25]. In addition, there is increasing awareness that SOA should be put into perspective in the broader context of service science, management, and engineering (SSME) [3].

Many authors postulate that SOA will ultimately improve the agility and reduce the complexity of IS landscapes [28, 38, 65], but only a few, mostly exploratory studies, have investigated SOA’s strategic and economic aspects [7, 55]. None of these studies offers the comprehensive view of the benefits needed for a sound justification of SOA investments. Given the lack of models to clarify the economic potential of SOA, our research’s long-term aim is to establish a framework to understand how the IS architectural paradigm SOA generates value on the business side. In this study, we investigate 164 SOA cases published between 2003 and 2008. We base our exploratory analysis on a conceptual model, the service-oriented architecture economic potential model (SOA‑ EPM), in which we use the resource-based view to link SOA as an architectural style to an SOA-specific benefits framework. With this model, we look for patterns that will help us understand SOA’s economic potential. The insights from the case analysis are the basis for aggregating our findings into a model for future research and deriving a set of propositions that can guide future studies on SOA’s economic potential.

## Current State of SOA Research

Ac ording to a surv ey c onduc ted b y Forrester Research, 63 percent of all North American, European, and Asian-Pacific companies had already started using SOA or planned to do so by the end of 2008 [41]. While the service-oriented paradigm is rapidly gaining popularity among practitioners [65], the academic debate on SOA has focused on technical aspects, such as Web services architecture [34, 87, 93], as well as service-oriented software design and componentization [91]. Drawing on the definition of SOA, the following section reviews prior investigations into its business benefits and demonstrates that the debate on this topic is still at an early stage.

## SOA as an Architectural Style

SOA is a multi-layered, distributed IS architecture paradigm encapsulating parts of the IS landscape as services [7, 28, 46, 53, 69]. Building on the view of SOA as an architectural style [28, 30, 46, 69], the literature largely agrees that it is characterized by certain basic architectural elements—notably, services—and a set of distinct design principles [55, 56].

The first design principle is modularity [63], which some authors denote as autonomy [28]. An SOA decomposes the existing application architecture and structures it into a manageable number of partially autonomous subsystems—that is, domains and services. This is in accordance with module or component design principles, according to which a service group’s functions or resources are highly interdependent (cohesive) [46, 71, 83]. Adherence to this principle allows a quick and easy composing of services that will optimally meet current requirements [38]. The second principle is loose coupling [28], which means that the logical and run-time dependencies between services are as low as possible [53, 71]. Ideally, the only connection between services is their service contract [11]. Because application-like logic is never realized statically in an SOA [52], adherence to this principle is essential for the dynamic binding of components. SOA relies on compatible interfaces and the use of standards [27, 28, 60] as a third design principle. In heterogeneous environments, this is particularly important to ensure interoperability and to guarantee seamless integration [60]. Although SOA is not tied to a specific technology, Web service standards are increasingly applied to overcome platform and vendor dependency. Some authors [10, 53, 69], along with the Semantic Web community, emphasize that with regard to business tasks and data, technical standardization has to be complemented by common semantics. For integration within and across enterprises, SOA should, if possible, rely on open and widely applied industry standards [7, 71].

## Economic Potential of SOA

To date, only a few studies have systematically investigated SOA’s economic potential. The exploratory nature of these studies is indicative of the early stage of research into this area. An exception is the study conducted by Tafti et al. [84] that, based on a combination of secondary data sources and a sample of 375 firms, suggests that investments in SOA-based, flexible information technology (IT) infrastructures enable firms to derive greater value from collaborative joint ventures. Most other publications build on single or multiple case studies to assess SOA initiatives’ business outcomes. In their comparative, cross-cultural case study of two European banks, Baskerville et al. [7] analyze how SOA adds value by addressing the four major architecture challenges of this particular industry: application integration, value reconfiguration processes, value preservation after mergers and acquisitions, and more agile forms of IS development. They conclude that SOA enhances architectural extensibility, thereby providing potential for greater organizational agility and competitiveness. Studying four SOA implementations, Legner and Heutschi [56] identify three focus areas of SOA adoption. These are characterized by a set of specific objectives and related benefits from the company perspective: (1) as a standardized integration infrastructure, SOA decreases overall system integration costs; (2) SOA reduces enterprise-wide IT costs and decreases IT projects’ time-to-market with regard to decoupling application domains; and (3) SOA improves IS support for end users regarding flexible user/business process integration. Lim and Wen [57] discuss the business opportunities of Web service technologies and illustrate the business benefits with five success stories from various industries. They emphasize that SOA allows companies to sell their internal services to other companies needing similar functionalities.

To summarize, all of these studies provide interesting insights into SOA implementations’ specific benefits, but still lack a broader empirical validation and do not tie their analyses to an underlying conceptual framework. Furthermore, a few authors have developed models with which to systematically analyze the benefits of SOA. Two of these are Lagerström and Öhrström [54], who, by using extended influence diagrams, have designed a framework for assessing SOA implementation. This framework considers SOA business value resulting from modification effects (system modifiability and change complexity), financial impact (cost and revenue), and organizational effects. Müller et al. [67] suggest that SOA design principles are the sources of economic potential and present a multilayer model to describe the causal relationships. They have applied their model in the banking and the automotive distribution fields. A similar, but less refined, line of argumentation is suggested by Hau et al. [40] to derive criteria for SOA project selection. They argue that the SOA design principles lead to agility, complexity reduction, increased reusability, and better interoperability. In a conceptual article, Huang and Hu [45] suggest a balanced scorecard approach to integrate Web services with competitive strategies. According to their study, Web services can create value for the adopting firm in infrastructure, operational, and strategic dimensions. The authors then relate these to the four balanced scorecard perspectives.

From this review, two main limitations were identified in the current state of research: first, there is still no comprehensive model for analyzing SOA’s economic potential. In this regard, the current debate on SOA’s potential economic outcome fails to pick up on earlier research on the effectiveness and value of IS. Second, existing studies have mainly investigated SOA benefits by means of single or multiple case studies, but their findings have not been collected in a comprehensive framework, or validated on a broader empirical basis.

## Theoretical Foundation

SOA is one of the rec ent examples of IT -b ased innov ations that have been introduced over the past decades. In this regard, the current debate on SOA benefits needs to be related to the more fundamental debate on whether, and to what extent, IT investments pay off. The following section reviews prior research on the effectiveness and value of IS and derives the theoretical cornerstones for understanding SOA’s economic potential.

## Anchoring SOA in the IS Value Discourse

Despite the provocative discourse titled “IT doesn’t matter” [16], the research community has largely agreed that the use of IS provides some form of value [51]. There is also consent that the use of IS—if regarded as hardware and software components—does not create value in isolation and that benefits only emerge if individuals or organizations improve their ways of communicating or working by means of IS [64]. Thus, IS value is tied to the adopting entity’s perspective. The two most popular perspectives in IS literature are the individual and the organizational perspectives (see Table 1).

A great number of studies have investigated the effectiveness of IS via the user perspective, thus resulting in models that explain IS success [22, 23] and technology acceptance [20, 21]. In this context, three dimensions of IS effectiveness are distinguished: technical success resulting from better systems quality, semantic success generated by better information quality, and individual effects determined by use and

<sub>ior</sub> <sub>Literature</sub> R<sup>elated</sup> <sup>to</sup> <sup>IS</sup> <sup>Effectiveness</sup>

<table><tr><td>Unit of analysis (adopting entity)</td><td>Approaches for assessing IS effectiveness and value</td><td>Findings</td><td>Implications for understanding the economic potential of SOA</td></tr><tr><td rowspan="2">Individual</td><td>IS success models [22, 23]</td><td>The success or effectiveness of IS as perceived by the receiver depends on three factors: “systems quality,” which measures technical success; “information quality,” which measures semantic success; and “use, user satisfaction,” which measures individual effects.</td><td rowspan="2">Like enterprise software, SOA does affect the individual user in its role as part of a larger organizational unit. A conceptual model of SOA’s economic potential should not exclusively focus on the individual perspective.In addition, SOA usually has no direct implications for the user, as the user is unable to identify whether an SOA or a monolithic application is behind a particular user front end.</td></tr><tr><td>Technology acceptance models [20, 21]</td><td>The acceptability of an IS is determined by its perceived usefulness and perceived ease of use.</td></tr><tr><td>Organization</td><td>IS and productivity [12, 13]</td><td>The productivity gains from increased IS spending are difficult to measure due to inadequate measurement methodology, time lags in measuring payoff, and various intermediate and context-related factors.</td><td>In accordance with the literature, it is hard to measure SOA value only in terms of financial performance indicators.</td></tr></table>

<sub>s</sub>i<sub>ness</sub> v<sup>a</sup>l<sup>u</sup> ili<sub>t</sub>i<sub>es</sub>, w<sup>h</sup>i<sup>ch</sup> i<sup>n</sup> <sup>turn</sup> <sup>gene</sup> <sub>SOA</sub> i<sup>mproves</sup> <sup>a</sup> <sup>firm</sup>’<sup>s</sup> ili<sub>ty</sub>. T<sup>h</sup>i<sup>s</sup> <sup>ca</sup>ll<sup>s</sup> <sup>for</sup> <sup>an</sup> <sup>ana</sup>l<sup>y</sup> <sub>an</sub> <sub>on</sub>l<sub>y</sub> <sub>dep</sub>lo<sup>y</sup> <sup>va</sup>l<sup>ue</sup> <sup>as</sup> <sup>a</sup> m<sup>s</sup> <sup>of</sup> <sup>the</sup> <sup>resource-based</sup>

<sub>proc</sub><sup>ess</sup> l<sup>ev</sup> <sub>d</sub> <sub>at</sub> i<sub>ntermed</sub>i<sub>ate</sub> l<sub>eve</sub>l<sub>s</sub>—<sup>n</sup> <sub>us</sub>i<sub>ness</sub> <sub>outco</sub>m<sup>es</sup> <sup>shou</sup>

<sub>se</sub>a<sup>rc</sup> <sub>een</sub> <sub>h</sub>i<sub>gh</sub>li<sub>ghte</sub><sup>d</sup> <sup>by</sup> <sup>pr</sup>i<sup>o</sup> i<sub>z</sub>i<sub>ng</sub> <sub>the</sub> m<sup>an</sup>i<sup>fo</sup>l<sup>d</sup> <sup>aspect</sup> <sub>fram</sub>e<sup>work</sup> <sup>prov</sup>i<sup>des</sup> <sup>supp</sup> <sub>an</sub>i<sub>zat</sub>i<sub>ons</sub>, <sub>a</sub> <sub>mu</sub>l<sub>t</sub>i<sup>d</sup>i<sup>mens</sup> <sub>ther</sub> IS i<sup>nnovat</sup>i<sup>ons</sup> <sup>ap</sup>

<sub>ransact</sub>i<sup>on</sup> <sup>co</sup> <sub>uent</sub>l<sub>y</sub>, <sub>there</sub> m<sup>ay</sup> <sup>be</sup> <sup>a</sup> <sup>dec</sup> <sub>at</sub>i<sub>on</sub> <sub>of</sub> b<sup>us</sup>i<sup>ness</sup> <sup>part</sup> i<sub>ng)</sub> <sub>s</sub>im<sup>p</sup>li<sup>fy</sup> <sup>the</sup> <sup>e</sup>l<sup>ect</sup> <sub>u</sub>l<sub>ar</sub>i<sub>ty</sub>, <sub>stand</sub><sup>ards</sup>, <sup>and</sup> l <sub>ree</sub> <sub>des</sub>i<sub>gn</sub> <sup>pr</sup>i<sup>nc</sup>i<sup>p</sup>l<sup>es</sup> <sup>of</sup>

<sub>g</sub> <sub>to</sub> <sub>new</sub> <sub>f</sub>o<sup>rms</sup> <sup>of</sup> <sup>coord</sup>i <sub>t</sub> <sub>the</sub> <sub>co</sub>m<sup>pany</sup> <sup>boundar</sup>i<sup>e</sup> <sub>e</sub> <sub>of</sub> IS <sup>decreases</sup> <sup>trans</sup>

<sub>f</sub> IS <sub>d</sub>im<sup>ens</sup>i<sup>ons</sup> <sup>to</sup> <sup>reflect</sup> <sup>the</sup> i <sub>t</sub> <sub>framework</sub>s <sup>compr</sup>i<sup>se</sup> <sup>m</sup>

<sub>co</sub>m<sup>pet</sup>i<sup>t</sup>i<sup>ve</sup> <sup>advant</sup> li<sub>t</sub>i<sub>es</sub>, w<sup>h</sup>i<sup>ch</sup> i<sup>n</sup> <sup>turn</sup> <sup>creates</sup> <sub>ces</sub> <sub>may</sub> l<sub>e</sub>a<sup>d</sup> <sup>to</sup> i<sup>mproved</sup> <sub>of</sub> <sub>ho</sub>w I<sup>T</sup> <sup>creates</sup> <sup>va</sup>l<sup>ue</sup>. <sub>source-based</sub> <sub>v</sub>i<sub>e</sub>w <sup>exp</sup>l<sup>or</sup>

<sub>or</sub>m<sup>ance</sup> i<sup>nd</sup>i<sup>cat</sup> <sub>ture</sub> <sub>than</sub> <sub>at</sub> <sub>the</sub> l<sup>eve</sup>l <sup>of</sup> <sup>fin</sup> <sub>ct</sub> <sub>at</sub> <sub>the</sub> <sub>pro</sub>c<sup>ess</sup> l<sup>eve</sup>l i<sup>s</sup> <sup>far</sup> <sub>fit</sub> <sub>fram</sub>e<sup>works</sup> <sup>[33</sup>

<sub>b</sub>ili<sub>t</sub>i<sub>es</sub> <sub>[4</sub>, <sub>9</sub>, <sup>26</sup>, <sup>62</sup> <sub>urce-based</sub> <sub>v</sub>i<sub>e</sub>w<sup>/</sup>I

user satisfaction. However, this stream of research mostly focuses on individual users, omitting the organizational context [88], which is the most relevant with regard to SOA benefits.

Regarding the organizational perspective, early studies encountered difficulties in demonstrating the productivity gains from growing IS expenditure [12, 13]. In the meantime, the “productivity paradox” has been found to be due to inadequate measurement methodology, time lags in measuring payoff, and various intermediate and context-related factors [14, 50]. While researchers have been able to demonstrate productivity improvements from IS spending [43], they have also found that it is easier to capture IS impact at intermediate levels—notably, at the process level [64, 66]. The emergence of enterprise systems, which provide data integration and support an organization’s main business functions, provides additional insights into the great variety of IS benefits. These range from operational business process improvements (cycle times), to profitability gains (return on assets), to enhanced competitive advantage due to the supply chain’s improved responsiveness. Consequently, some authors [33, 81] suggest the use of multidimensional benefit frameworks and classify business benefits according to benefit dimensions.

In addition to the multiple facets of IS value, the logic of overall IS-based value creation has gained some attention from researchers. According to the resource-based view, a firm’s IS/IT resources—that is, its IT infrastructure, IS, and IT-related skills— create IS/IT capability [4, 9, 26, 62, 73]. This is a functional capability in the hierarchy of organizational capabilities suggested by Grant [36]. Because these capabilities are difficult to copy, they are instrumental in fostering better business capabilities and, ultimately, a firm’s ability to generate competitive advantage [51].

From the existing literature, we gained a number of valuable insights for further assessing the economic potential of SOA, which Table 1 describes in more detail. First, we presume that SOA has a multifaceted impact that is hard to measure only in terms of financial performance indicators. A multidimensional benefit framework may therefore be more appropriate to cover the manifold aspects emphasized by prior SOA studies. Second, it will be difficult to link SOA investments directly to businessesrelevant benefits. SOA value does not materialize directly, but only manifests across a number of intermediate steps, thus constituting logical chains of IS-based value creation. Building on the resource-based view, this calls for an analysis of how SOA improves a firm’s capabilities, which in turn generates business value.

## Conceptualizing the Economic Potential of SOA

In order to better handle the complexity of the SOA and economic potential concepts, we follow the approach of gradual decomposition [78], which is frequently applied in the context of IS benefits [74]. For the conceptual decomposition of SOA, we build on the resource-based view [4, 9, 35, 62, 84] by arguing that SOA improves an organization’s ability to assemble, integrate, and deploy IT resources. Building on the three design principles (modularity, loose coupling, and standards), SOA enhances the way IS are consistently designed and deployed across an organization. With the resulting capabilities focusing on IS, we label them IS capabilities of SOA. This means that the SOA concept creates new IS capabilities or reinforces existing ones through the application of its three design principles. Typical examples of specific IS capabilities fostered by SOA design principles are reusability or interoperability [40]. This threestep hierarchy represents the technical sources of SOA’s economic potential.

Table 2. Overview of Enterprise Systems’ Benefits According to Shang and Seddon [81]

<table><tr><td>Operational benefits</td><td>Streamlined processes and automated transactions provide business benefits by speeding up processes, substituting labor, and increasing operational volumes.</td></tr><tr><td>Managerial benefits</td><td>Allocation and control of the firm&#x27;s resources, monitoring of operations, and support of strategic business decisions.</td></tr><tr><td>Strategic benefits</td><td>Attainment of a sustained IT-based competitive advantage.</td></tr><tr><td>IT infrastructure benefits</td><td>Sharable and reusable IT resources that provide a foundation for present and future business applications: (1) business flexibility for future changes; (2) reduced IT costs and marginal costs of business units&#x27; IT; and (3) increased capability for prompt and economic implementation of new applications.</td></tr><tr><td>Organizational benefits</td><td>Build integrated processes, improve employee communication, foster the development of a “common vision” and user empowerment, support customer services, and facilitate a flattening of the organizational structure.</td></tr></table>

In order to conceptualize the economic potential, we refer to existing multidimensional benefit frameworks to classify potential benefits that ultimately lead to economic potential. In the context of enterprise systems, Shang and Seddon [81] have determined five benefit dimensions from IS literature (Table 2) and aggregated 21 subdimensions suitable for use by business managers seeking to assess the benefits of their enterprise system. These dimensions have subsequently been used and refined by other studies related to ERP systems [17, 48], and have also been applied to study the benefits of other IS innovations at the enterprise level—notably, enterprise application integration (EAI) [49]. This implies that Shang and Seddon’s [81] benefits dimensions are suitable as a more generic model for classifying the benefits that enterprises realize from using IS (organizational perspective according to Table 1).

Following this line of thought, we argue that there are three main reasons for an application of Shang and Seddon’s benefit dimensions in the context of SOA. First, three of the five dimensions—infrastructure, operational, and strategic benefits—have been explicitly suggested by prior SOA research [45], and managerial and organizational benefits have been implicitly mentioned in some of the existing empirical studies [7,

![](/api/attachments/VT35T3KJ/fulltext/images/beb2f95adbafbace4636a6b47042a5ae1a75ef1e21560c955dd4a5989e391b0d.jpg)  
Figure 1. Conceptual Foundations of the Service-Oriented Architecture Economic Potential Model (SOA-EPM)

55]. Second, as mentioned earlier, SOA, as an architectural style, prescribes enterprisewide “guidelines” for implementing and deploying IS in an enterprise. Given the increasing number of systems along with their many implementation and configuration options, SOA is tightly linked to the design of enterprise system landscapes, which form the digital backbone of modern organizations. Third, software vendors increasingly conceive modern enterprise systems as enterprise-wide platforms that follow SOA’s design principles (i.e., modularity, loose coupling, and standards) [92].

While the main benefits dimensions suggested by Shang and Seddon [81] will be applied as a classification model for SOA’s economic potential, benefit subdimensions are necessary to further decompose the main benefit dimensions. Part of our research’s exploratory work was to provide a specific set of benefit subdimensions in the context of SOA. Examples of subdimensions that have been mentioned in the context of SOA are system modifiability [54], agile IS development, and application integration [7], which can be associated with the infrastructure benefit dimension, or the creation of new products and services [45] in the strategic benefit dimension. Taking all of the above into consideration, our conceptualization of SOA’s economic potential is depicted in Figure 1. Because the definition of SOA-specific IS capabilities and benefit subdimensions was part of our exploratory work and is described in the following sections of the paper, the respective layers are left blank at this stage. Later, based on the analysis of the cases, they are filled.

To summarize, we argue that as an architectural style, SOA is characterized by a set of specific design principles that are the source of new or enhanced IS capabilities within an enterprise. These capabilities are expected to generate certain economic benefits that ultimately create SOA’s economic potential. This conceptualization will form the basis of our model for understanding SOA’s economic potential (SOA‑ EPM). In order to bring together the two gradually decomposed concepts of SOA and economic potential, we will need to identify SOA’s specific IS capabilities and connect them to related benefit subdimensions of SOA implementations.

## Research Design

## Research Objectives and Approach

Giv en that the ac ademic disc ussion on SOA ’s b enefits is still at an early stage, our research goal is to explore how SOA generates economic potential from the enterprise perspective. Gregor [37] classifies this type of research as a theory for explaining. Case study is one of the recommended research approaches to explain how and why things happen in real-world situations.

Our approach is to analyze SOA implementation projects based on written case material that describes how the SOA concept is applied in real-world situations. We specifically study the arguments used to illustrate SOA’s perceived economic potential in current or past implementation projects. Following the logic of gradually decomposing complex concepts to make them more easily accessible [78], these arguments can be represented with elements that, altogether, form a cause-and-effect structure. Other studies in the field of IS value research apply a similar logic when analyzing such complex constructs [51, 74, 81]. By coding the arguments evident in the case material [77], we analyze and structure these arguments, using our conceptual model that builds on the logic depicted in Figure 1. Based on the arguments represented by chains of model elements, we analyze the sources of economic potential across multiple cases and search for reoccurring patterns. Such patterns may be groups of elements present in a high number of cases, links between a set of these elements, or these elements as a complete chain linking SOA and economic potential. These patterns may help us gain an understanding of SOA’s economic potential.

Seddon et al. [80] suggest that it is necessary to clarify several parameters of organizational effectiveness measurement before evaluating an IT investment. To refine our approach, we discuss the parameters originally suggested by Cameron and Whetten [15] in Table 3.

## Data Collection

One of the key difficulties of IS value research is the accessibility of data from realworld implementations [51]. This particularly applies to the SOA concept, which is relatively new [95] and at an early stage of industry adoption. Because our aim was to gather a broad empirical basis of SOA implementations, we decided to base our study on secondary data.

We consequently collected SOA case material on current and past SOA projects. This approach is consistent with data collection strategies employed by others in the context of IS value research [81] and other areas of IS research [32, 79, 84]. The set of cases initially identified comprised more than 180 case descriptions, which we acquired from journal databases, print publications, case collections, press coverage, and material issued by companies, vendors, consultants, and analysts dealing with SOA. The following selection criteria were applied: (1) a case describes a real-world implementation of SOA and (2) it explicitly states the benefits that have been attained by introducing SOA. Opinion pieces by industry experts or lessons-learned documents with no particular and directly attributable case example were removed from the set. We scanned the remaining 171 case descriptions for business benefits and explanations of how these were realized by means of an SOA. In this phase, an additional seven sources were eliminated due to incomplete or partial information.

Table 3. Seven Questions to Answer When Measuring Organizational Performance

<table><tr><td>Seven questions for measuring organizational performance</td><td>Answers in this study for evaluating the economic potential of SOA</td></tr><tr><td>1. From whose perspective is effectiveness being judged?</td><td>Business and IT managers.</td></tr><tr><td>2. What is the domain of activity?</td><td>Businesses from a broad set of industries involved in current or past projects to implement an SOA.</td></tr><tr><td>3. What is the level of analysis?</td><td>The organization (or organizational unit) that engages in SOA implementation.</td></tr><tr><td>4. What is the purpose of evaluation?</td><td>The identification of the core drivers of the economic potential of SOA in a business context from an organizational perspective in order to develop an SOA benefits framework based on the resource-based view (see Table 1).</td></tr><tr><td>5. What time frame is employed?</td><td>Normally SOA projects at any stage (piloting, implementation, and deployment).</td></tr><tr><td>6. What types of data are to be used?</td><td>Perceptual descriptions of SOA implementations and the specific benefit for the organization as documented in a case study format.</td></tr><tr><td>7. Against which referent is effectiveness to be judged?</td><td>The stated goals of the organization (the business case for the SOA project, as well as the overall business strategy).</td></tr></table>

The final data set consists of 164 case descriptions covering 141 organizations from 32 industries with current or past SOA implementation projects. These cases were covered in a total of 127 bibliographic sources.<sup>1</sup> Of these sources, we classified 39 (31 percent) as originating from scientific sources (journal databases or case collections, also including our own case studies), 36 (28 percent) sources as press coverage (newspaper or magazine articles), and 52 (41 percent) sources as material released by companies (vendor implementation cases, analyst or consultant studies, or company announcements).

## Research Process and Data Analysis

A three-step research process was followed in order to ensure that the insights derived from SOA’s economic potential took prior literature into account and were based on a broader empirical validation.

## Step 1: Building a Model for SOA’s Economic Potential

The basis for our model, which we denote as service-oriented architecture economic potential model (SOA‑ EPM), is the theoretical foundation introduced above. We refined both the SOA and economic potential concept, as summarized in Figure 1. To populate the different layers of the model, we conducted a literature review. Following established approaches [29, 90], we covered literature from IS as well as from the business and computer science disciplines. After the initial population of the layers, we started collecting case material reporting on any current or past SOA projects. A sample from the cases was used to check our conceptual model’s elements. We discussed refinements to and extensions of the model and introduced these if they were compatible with theory.

To finalize our model, the SOA and economic potential concepts had to be linked. The model will only help us understand SOA’s economic potential if it provides a possibility to consistently code the arguments linking SOA and economic potential. To account for the notion that economic potential is only generated if applied to a current problem [42], we used the case material sample to derive a number of application scenarios. The latter allow the missing link between our model’s technical and the economic side to be established. Along with other sources identifying such application scenarios [67], the scenarios found in the cases were discussed in a series of workshops and included in our model when consensus was reached.

The result of this first step of our research was a model that established three layers of elements to refine each of the concepts of SOA and economic potential. These are linked via a connection layer of application scenarios, located as a central layer between the two. The model will be presented in detail in the following section.

## Step 2: Analyzing the Sources of SOA’s Economic Potential

At the outset of the second step of our research, we translated the SOA‑ EPM into a coding scheme for text analysis [72]. We used a Microsoft Access database to implement the coding scheme representing the seven layers of our model by means of tables containing the respective elements. The case material was also cataloged in this database. When analyzing the cases, an argument was captured regarding how SOA created economic potential in a specific case by (1) selecting the case, (2) describing complete cause-and-effect chains by selecting one of the elements from each of the seven layers, and (3) collecting additional information (coder’s interpretation, etc.). Choudhury and Sabherwal [18], for example, who built on the concepts of Tesch [85], also used such qualitative material analysis to investigate certain concepts and the reasons for using them. The case material was divided among the authors before the analysis was undertaken. Each case was first analyzed by one of the authors, who coded the causeand-effect chains. In order to increase the interrater reliability, a second author then analyzed each case. If there was agreement on the coding, the chains were accepted. The remaining chains were subject to further discussions by all the authors. Chains on which no agreement could be achieved were excluded from the data set. In addition, we consolidated chains that were recorded multiple times per SOA implementation.<sup>2</sup>

Overall, our approach resulted in a total of 571 cause-and-effect chains. Ensuring interrater reliability led to the elimination of 12 chains, and the elimination of duplicates removed another 12 chains. The final set comprises 547 chains. After consolidating the results of the coding and ensuring data quality, we analyzed our data set with respect to three questions:

•	 Which of the conceptual model elements were present in the analyzed case material? This was determined by examining the absolute number of times an element was used to describe a cause-and-effect chain between SOA and economic potential.

•	 Which strong, pair-wise links occur between the various layers of the conceptual model? Cross tabulation that showed which element of layer n was linked to which elements on layer n + 1 was used to determine this.

•	 Which are the most prominent cause-and-effect chains that link SOA and business benefits? This was determined by examining entire chains—that is, unique combinations of elements from the conceptual model’s different layers—and identifying the chains found in multiple cases.

To ensure the quality of our data set and the analyses depicted above, we randomly split the case material and corresponding chains into two samples to conduct a cross validation. The set was split 50:50 or 82:82 cases, respectively.<sup>3</sup> We decided to split with respect to the cases because the implemented SOA constitutes our unit of analysis. The subsets were examined by means of cross tabulation. The tables were then normalized according to the number of total chains associated with the respective subset to eliminate the effects of an unequal number of chains associated with each subset. The subsets were used to check the analyses of our overall sample. The results of our analysis presented below are based on the overall sample. Each conclusion drawn from the full sample was examined by looking at the two random subsamples to either confirm or refute the conclusions drawn. Only if the subsamples suggested that the conclusion was valid was the analysis included as a result. This comparison of the total sample with two randomly split subsets of our data provided us with an indication that the results discussed below are likely to reoccur in any sufficiently large and randomly selected sample of SOA implementation cases. A repeated analysis with a different assignment and split yielded similar results.

## Step 3: Deriving Propositions and Developing a Research Model

From the results of the analysis of our data set, we aggregated our findings on elements and their links into a set of propositions for future research on SOA’s economic potential. The resulting research model depicts the understanding we gained of the relation between the SOA’s style characteristics and the value it can provide on the business side. The propositions that we identify are intended to provide a basis to conduct empirically grounded studies.

## Conceptual Model for SOA’s Economic Potential

Building on the theoretic al foundations and conceptualization summarized in Figure 1, this section presents the service-oriented architecture economic potential model (SOA‑ EPM). Based on the definition of SOA as an architectural style (layer 1) with the design principles modularity, standards, and loose coupling (layer 2), we deduced 10 elements that describe SOA’s IS capabilities (layer 3). These elements are based on a literature review and the analysis of SOA cases as described in the research process. Following the same approach, we identified 19 SOA-specific benefit subdimensions (layer 5) that aggregate into the five benefit dimensions (layer 6) derived from Shang and Seddon [81]. Ultimately, these dimensions constitute SOA’s economic potential (layer 7). This logic results in a diamond-shaped model. Figure 2 shows our model’s logical structure with the layers 1 to 7 and the interspaces A to F between the layers.

Now that we had not only defined SOA, its design principles, and its IS capabilities (layers 1–3), but also the benefit subdimensions, benefit dimensions, and economic potential (layers 5–7), these elements needed to be connected to allow for causal relationships that explain an SOA’s economic potential. Consequently, a connection layer, built on “application scenarios,” was designed to which both business units and IT departments can relate. For example, reusability on layer 3 leads to reduced project/ development cost as an “application scenario” on layer 4 and results in reduced maintenance and operation costs on layer 5. By examining all the elements of layers 3 and 5, and using the insights gained from our case material, we developed the connection layer (layer 4) consisting of 23 elements. Building on Figure 2’s logical structure, Figure 3 provides an overview of our conceptual model. Two exemplary cause-and-effect chains illustrate the logic of the model. For better comprehension, Figure 3 shows a reduced number of elements on layers 3 to 5. A full overview of the SOA‑ EPM, its layers, and all of its elements is provided in Appendix Figure A 1. We use it as the structural basis of the analysis of the case material that we collected, which will be discussed in the following section.

## Analysis of SOA’s Economic Potential

From the analysis of the 164 c ases and the resulting 547 coded chains, a rich data set was generated, which yielded a large variety of findings. In the following section, we discuss these findings according to three distinct perspectives: (1) the total number of occurrences of the elements per layer of the conceptual model, (2) the distribution of pair-wise links of elements between any two adjacent layers of the conceptual model’s seven layers, and (3) the composition of elements from all seven layers into whole chains connecting all layers describing SOA’s economic potential as found in the cases.

![](/api/attachments/VT35T3KJ/fulltext/images/36d56a864e933be7e3779d0fd444ee168d98427f11526fdb550ea5abd9009603.jpg)  
Figure 2. Logical Structure of the Service-Oriented Architecture Economic Potential Model (SOA-EPM)

![](/api/attachments/VT35T3KJ/fulltext/images/ede22712eca844e25b97b046f6a4c110f8a644369b57919aabd0aa345c241fe7.jpg)  
Figure 3. Two Exemplary Chains in the Service-Oriented Architecture Economic Potentia Model (Excerpt)

## Discussion of Elements

On the second layer, which displays SOA’s design principles, we find that—according to the analyzed cases’ authors—modularity is the dominant principle (coded as part of 317 chains). This is followed by standards (163) and loose coupling (67). Our understanding of the case material suggests that modularity is perceived as most relevant given the many issues resulting from current silo architectures and the high number of monolithic applications operating on different platforms. Changes are difficult to implement in such IS landscapes, a shortcoming that SOA is perceived to overcome.

On the level of IS capabilities (layer 3), our case base shows that reusability (138) is mentioned most often. It is followed by interoperability (102). Interestingly, many of the case authors regard reusability as a key SOA IS capability, which they were able to develop by specifying reusable services to support frequent business activities and tasks. The high number of interoperability occurrences emphasizes that SOA’s economic potential only unfolds if service interface specifications truly adhere to full technical and semantic interoperability. On examining the links between the second and third layer, we find that standards are the main prerequisite for realizing interoperability. Other third-layer elements that occurred frequently in our analysis are flexibility (76), standardization (65), infrastructure and application abstraction (63), and service composition (52). This indicates SOA’s perceived importance regarding transforming formerly monolithic applications into standardized services that can be flexibly composed into solutions that fit business needs. This is supported by an examination of the links between layers 3 and 4, which indicates that these four IS capabilities strongly support data and application integration and a faster adaptation to change.

On examining the connection layer (layer 4), the data gathered show that the aforementioned data and application integration capabilities (76) is the dominant element. This element is followed by integrate external partners (53) and information provisioning for end users and roles (45). With respect to SOA’s economic potential, this indicates that SOA can extend a firm’s IS capability in terms of both functional range and organizational reach, thus demonstrating SOA’s integrative potential—within and across the entities—in today’s complex value chains. In the midrange of layer 4, our analysis identified the ability to realize an existing repository of business functionality (44), the potential to reduce project/development cost (38), the ability to leverage legacy applications and infrastructure (37), the possibility of process integration (35), as well as faster adaptation to change (34).

Our model’s fifth layer, which displays possible benefit subdimensions that describe SOA’s economic potential, shows very clear results: better asset utilization and realizing economies of scale (76), better alignment of business and IT (70), and the potential to reduce maintenance and operations cost (65) are the elements most mentioned in the cases. This indicates that SOA has a twofold potential in a business context. It can, first, be applied to improve IT efficiency (the first and third elements mentioned above) and will, second, enable corporate IT to better align with business needs and requirements, hence increasing IT’s effectiveness (second element).

The midrange of this layer consists of six elements: business process improvements (42), improved interorganizational coordination and communication (42), increased availability of information (40), reduced time-to-market (30), higher business agility (26), and reduced redundancy (25). These findings continue the interpretations provided above with respect to both the internal and external integration abilities, as well as the twofold focus on efficiency and effectiveness.

The benefit dimensions (layer 6) that we considered in our analysis show that IT infrastructure benefits (225) dominate SOA’s perceived effects, followed by operational benefits (175) and strategic benefits (105). Managerial (28) and organizational benefits (14) occur less frequently. In its current stage, SOA is therefore largely perceived as a means of improving IT infrastructural properties. SOA’s second-strongest impact lies in operational improvements. The analysis of the links between layers 5 and 6 indicates that increased customer satisfaction (41 links), business process improvement (38 links), increased availability of information (25 links), and reduced maintenance and operation cost (17 links) are the main constituents of such operational benefits. In the light of vendors and consultants’ promises [65] to deliver SOA as a “strategic weapon,” it is interesting that strategic benefits only rank third in the analyzed cases perception.

An overall view of these results leads us to the interpretation that the three SOA design principles (modularity, standards, and loose coupling) result in three main benefit dimensions (IT infrastructure, operational, and strategic benefits). The remaining benefit dimensions (managerial and organizational benefits) only account for about 8 percent of all chains. These elements’ number of connections via the 547 coded chains is depicted in Table 4.

It is interesting that roughly the same percentage of all the chains running through any one of the design principles is linked to each of the three benefit dimensions mentioned most often: about 41 percent<sup>4</sup> are connected to IT infrastructure benefits, about 33 percent are linked to operational benefits, and about 19 percent are linked to strategic benefits. Managerial and organizational benefits represent only 5 percent and 3 percent, respectively. Although less clear, the same is true when the links from the benefit dimensions perspective are examined: about 56 percent<sup>5</sup> of all incoming chains run through the modularity design principle, about 30 percent are derived from standards, and about 14 percent are realized in chains that build on loose coupling. This illustrates the patterns we are looking for on a “macro” level: by collapsing the three middle layers of the conceptual model (IS capabilities, connection layer, and subdimensions) to gain a better overview of the overall structure, clear patterns connect SOA’s design principles to the dominant business benefits.

## Discussion of Links

In the next level of analysis, we looked at the pair-wise links between any two of our conceptual model’s adjacent layers to gain a deeper understanding of the causal connections. These links were analyzed by examining the interspaces of the SOA‑ EPM (Figure 2) with regard to both the entire data set as well as the two randomly split subsets. As a general finding across all six interspaces, we find that the cross validation with the help of the two subsets resulted in similar patterns with regard to all interspaces. We already outlined some of the results of the pair-wise link level in the preceding section. Looking at the results from this perspective, there seems to be a set of dominant links per interspace, a field of links in the midrange, and some less frequent connections in the perception of the analyzed case material’s authors.

Table 4. Number of Chains Connecting SOA’s Design Principles and Benefit Dimensions

<table><tr><td rowspan="2">Benefit dimensions</td><td colspan="4">Design principles</td></tr><tr><td>Loose coupling</td><td>Modularity</td><td>Standards</td><td>Sum</td></tr><tr><td>Infrastructure benefits</td><td>27</td><td>134</td><td>64</td><td>225</td></tr><tr><td>Managerial benefits</td><td>3</td><td>19</td><td>6</td><td>28</td></tr><tr><td>Operational benefits</td><td>24</td><td>103</td><td>48</td><td>175</td></tr><tr><td>Organizational benefits</td><td>3</td><td>6</td><td>5</td><td>14</td></tr><tr><td>Strategic benefits</td><td>10</td><td>55</td><td>40</td><td>105</td></tr><tr><td>Sum</td><td>67</td><td>317</td><td>163</td><td>547</td></tr></table>

Across our model’s various interspaces, there are some pair-wise links that we deem to be especially remarkable. With respect to the second interspace (B in Figure 2)—that is, the links between SOA’s design principles and the resulting IS capabilities— modularity mainly leads to reusability (126 links), flexibility (59 links), infrastructure and application abstraction (48 links), and service composition (44 links). This aspect underlines that SOA enhances a firm’s IS capabilities by providing reusable services, which can be abstracted from their implementation and can be flexibly composed. On the other hand, because standards link to interoperability (73 links) and to standardization (62 links), this shows that these services need to be based on sound standards in order to work together.

Our analysis with respect to the elements has already indicated that the increased ability to align business and IT is an important aspect of SOA effectiveness. On examining the incoming links (interspace D), we find that SOA mainly enables alignment by allowing a faster adaptation to change (13 links), reducing project and development time (13 links), and through its ability to provide services implementing business logic in process steps (12 links). These 38 incoming links represent 54.3 percent of all chains that enable economic potential through better alignment between business and IT (70 chains).

While we found that there are several important elements on the benefit subdimensions layer (layer 5), the sources of these elements are sometimes very diverse. Cases in point are increased customer satisfaction and reduced maintenance and operation costs with 8.59 percent and 11.88 percent of all chains encompassing these elements, respectively. However, on examining the elements that constitute these two benefit subdimensions on layer 4, the data indicate that not a single item in the two subdimensions accounts for more than 2.56 percent or 1.83 percent, respectively. In total, the two subdimensions are composed of 15 and 16 elements from layer 4. This illustrates that the targeted deployment of an SOA to address these benefit subdimensions seems to be highly situational [89].

## Discussion of Chains

Interestingly, there is no indication of only a few dominant chains, which would explain how SOA generates economic potential. Of the 547 causal chains, 399 chains were found to be unique. Only 70 causal chains were coded from the case material more than once. We assume that the large variety is mainly caused by the high number of elements on layers 4 and 5 of our model. Since each of the elements that we initially found was later used at least once for coding, this indicates that the large variety of elements on layers 4 and 5 actually reflects the individual motivations that drive organizations to adopt SOA, resulting in a multitude of chains that explain the economic potential obtained from SOA. The two most frequently occurring chains (also used as exemplary chains in Figure 3) were coded eight times.

The first of these chains (Figure 4) leads from standards, as a design principle, to strategic benefits. The eight cases encompassing this chain applied SOA to increase systems’ interoperability, targeting the interface to their external partners. Consequently, these companies could improve their communication and coordination across the organizational boundaries and realize competitive advantage by strengthening their value chain or ecosystem. While also confirmed by other studies [84], this line of argumentation is particularly frequent in distribution networks and emphasizes SOA and Web services’ potential to extend electronic integration to the space between enterprises [28].

Figure 5 shows a cause-and-effect chain that applies to a more internal perspective on SOA’s economic potential. Starting with modularity, it shows that eight companies analyzed in the data set used their SOA implementations to create services that are composable and encapsulate the business logic of business processes’ single steps. Given that processes become more adaptable, they use SOA to improve alignment between business and IT, which ultimately results in IT infrastructure benefits. This chain reflects, for example, the situation of early SOA adopters, who restructure their IS landscape according to SOA principles in order to better adapt their IS landscape to changing business requirements [39, 55].

## Deriving Propositions and a Research Model

The empiric al material that we analyzed illustrates how SOA, as an architectural style, enhances IS capabilities, which can in turn contribute to the generation of business benefits. A key finding from our study is that SOA’s economic potential does not seem to be determined by a few dominant paths, but by a variety of different cause-and-effect chains. Thus, our research demonstrates SOA’s versatility as an architectural paradigm and suggests that an SOA business case should be situational. From analyzing our data set, we found common patterns in the elements and pair-wise links across the cases that helped us to understand SOA’s economic potential and form the basis for our research propositions. The number of occurrences of such patterns is an indicator for the significance those patterns have beyond the individual case—that is, the effect described is not random. Because the number of occurrences of a pattern in the cases does not necessarily indicate the actual strength of the respective effect, the propositions focus on the significance rather than the strength of a path.

![](/api/attachments/VT35T3KJ/fulltext/images/3a69ec36ab83227199fc9d7af1bb5edf3a4be97b1976f1672daa6bc0ccd40dcd.jpg)

<sub>Helps</sub> <sub>Achieve</sub> <sub>Strate</sub><sup>gic</sup> <sup>Benefits</sup> <sup>Across</sup> <sup>Organization</sup>  
![](/api/attachments/VT35T3KJ/fulltext/images/244c68458bf8d40ed44c3ca2e5b1141dae4f4373c963c0c9109e33b1a860195d.jpg)  
<sub>s</sub> M<sup>odularity</sup> <sup>Helps</sup> <sup>Implement</sup> <sup>ITProcesses</sup> <sup>Close</sup> <sup>to</sup> <sup>Busi</sup>

Looking at the economic aspects of the 547 chains summarized in Table 4, 41 percent of these chains lead to infrastructure benefits, making it the most relevant benefit dimension of SOA. While operational (32 percent) and strategic benefits (19 percent) are also important drivers of SOA’s economic potential, there is little empirical evidence for managerial and organizational benefits. We thus assert:

Proposition 1 (The Primary Importance of Infrastructure Benefits Proposition): The most significant constituent of SOA’s economic potential is infrastructure benefits, followed by operational and strategic benefits.

In terms of SOA’s characteristics as an architectural style, an analysis of Table 4 shows that the design principle modularity accounts for almost 58 percent of the chains in our sample, followed by standards (30 percent) and loose coupling (12 percent). Hence, modularity is the key driver of new or reinforced IS capabilities through SOA. Our second proposition is on design principles:

Proposition 2 (The Primary Importance of Modularity and Standards Proposi tion): In the context of SOA, the design principles modularity and standards are most significant in creating and reinforcing IS capabilities, which in turn constitute economic potential.

To explain how these design principles generate benefits according to the relevant benefit dimensions discussed above, we conducted a cluster analysis<sup>6</sup> of the links depicted in Table 4. This analysis revealed that the effects that constitute SOA’s economic potential as an IS architectural paradigm are threefold. First, SOA fosters a more modular IS landscape design that allows for a more flexible reuse of IT assets and enhances the technical integration abilities in a heterogeneous environment. The resulting improvements mainly affect the effectiveness and efficiency of the IT resources, thereby creating IT infrastructure benefits. We consider this to be a first-order effect [6, 48] of SOA. Following this logic, we assert our third proposition:

Proposition 3 (First-Order Effects of SOA Proposition): As first-order effects, SOA most significantly generates infrastructure benefits through a modular IS architectural design (modularity).

Second, a more flexible and adaptable IS landscape generates second-order effects on the operational level. If SOA allows invoking and composing of business logic as services without having to rebuild them, it also increases a firm’s ability to modify business processes. Hence, it improves the speed with which a company can respond to a changing environment. These second-order effects can also help companies improve end users’ information access. Hence, our fourth proposition is

Proposition 4 (Second-Order Effects of SOA Proposition): As second-order effects, SOA most significantly generates operational benefits through a modular IS architectural design (modularity).

Third, and based on the effects described above, a number of more specific higherlevel effects can be realized on a strategic level. This relates to both modularity and standards, which have two effects. On the one hand, a company using SOA can offer electronic services to a larger number of external partners and more intensely use third-party services. On the other hand, SOA has an effect in terms of reducing timeto-market, which has the potential to reinforce the responsiveness discussed above. Two other higher-level effects are generated by standards as the architectural design principle that results in operational and infrastructure benefits. In both cases, standards create IS capabilities in terms of higher interoperability and reduced heterogeneity. Based on this analysis, our Higher-Level Effects of SOA Propositions are:

Proposition 5a (The Modularity Creates Strategic Benefits Proposition): In the context of SOA, modularity creates strategic benefits most significantly through reducing time-to-market.

Proposition 5b (The Interorganizational Coordination and Communication Proposition): With SOA, standards create strategic benefits most significantly through improving the interorganizational coordination and communication.

Proposition 5c (The Standardization and Interoperability Proposition): For SOA, IS architectural design based on standards creates infrastructure benefits most significantly by standardization and interoperability.

Proposition 5d (The Operational Benefits and Interoperability Proposition): In the context of SOA, IS architectural design based on standards creates operational benefits most significantly by interoperability.

Given the absence of a few dominant chains that explain how SOA generates economic potential, our research demonstrates that factors mediating the relations between SOA’s IS capabilities and benefits as well as between the contingency factors that moderate these effects [5] are important for understanding SOA’s economic potential. With respect to the former, we suggest that in a specific situation, the benefit argumentation for SOA needs to be explained via mediating variables. This calls for more research on the specific application scenarios and elements of our conceptual model’s connection layer. In addition, our data suggest that external and internal contingency factors [48, 51] influence the relevance of certain IS capabilities and their effect on SOA’s benefit in a specific environment. Such contingencies may, for example, include contextual, structural, or strategic factors that should be included in a comprehensive model [82].

While these aspects are not as specific as the propositions, we believe they are crucial to adequately capture the links we observed and to increase the explanatory power of research building on our work. To support future research, we aggregated our propositions and observations into a proposed research model based on the service-oriented architecture economic potential model (SOA‑ EPM) depicted in Figure 6.

This research model underpins that SOA is an IS architectural style with a potential to create IS capabilities that, in turn, support the realization of business benefits. Because our data have shown that some IS capabilities are more strongly linked to certain design principles than others, this has led us to associate them with the respective design principles.<sup>7</sup> Our theoretical and empirical investigation shows that SOA’s design principles are the source of increased IS capabilities and generate economic potential according to the benefits dimensions introduced earlier. The bold arrows in the center of Figure 6 depict the relations between these two aspects as described by Propositions 3 through 5. Further connections among the constructs are also present but, as of yet, are not as significant as the others suggested by our research propositions.

## Comparing the Results to Related Literature

In line with rec ent SOA pub lic ations, our research supports the versatility of SOA as an architectural paradigm. This implies that a simplistic calculation of SOA value is difficult [8, 58].

While our findings provide interesting insights into how SOA enhances IT capabilities, consequently creating economic potential, they also provide a basis for analyzing SOA’s commonalities and differences when compared to other IS innovations. For this purpose, we compare our findings to studies on ERP and EAI, which use Shang and Seddon’s framework [81]. From their analysis of ERP implementations, Karimi et al. [48] argue that in terms of (geographical and organizational) range and scope, increased ERP capabilities result in first-order ERP investments effects at the operational level. These first-order effects specifically point to process efficiency, effectiveness, and flexibility, which, in turn, may lead to second-order effects, such as improved profitability, earnings valuation, and competitiveness. While process improvements are also perceived as an important outcome of SOA implementations, it is evident that, compared to ERP systems’ cross-functional and integrated nature, SOA extends the organizational and geographical reach beyond a single organization’s scope to the wider value chain or ecosystem. It is, however, important to note that, contrary to ERP systems and other forms of enterprise systems, SOA is an IS architectural style. As such, it does not provide implementations of business functions that support specific business processes and, consequently, generate a defined set of business benefits. Consequently, the type and characteristics of the realized operational and strategic benefits are more diverse with regard to SOA than in the case of ERP systems. On the other hand, SOA has a much more important role to play with regard to IT infrastructure benefits. Khoumbati et al. [49] and Themistocleous [86] have investigated the benefits that integration technologies—notably, EAI—bring to an organization, mentioning benefits in all five benefit dimensions. It may be argued that, given that both concepts address integration abilities, there are analogies between EAI and SOA. Although our findings highlight SOA’s integration abilities, we find that it adds modularity, which, according to our empirical data, is the source of specific IS capabilities that are not provided by EAI.

![](/api/attachments/VT35T3KJ/fulltext/images/4a5c07b8f6cf81c87a1c49b9f7d35bfd8c019c72ff68fc2817eb6bd7d430dede.jpg)  
<sub>Model</sub> <sub>Based</sub> <sub>on</sub> <sub>the</sub> <sub>Service-Oriente</sub>d <sup>Architecture</sup> <sup>Economic</sup> <sup>Potential</sup> <sup>M</sup>

In comparison to prior SOA research, interesting insights also arise with regard to the relevance of the three design principles. In our analysis, modularity is perceived as the most dominant principle in the case material, whereas SOA literature highlights the availability of more open (Internet) standards and loose coupling as its most important new characteristic and its main differentiator in respect of earlier component-based software approaches [83, 91]. This disparity may be due to many companies struggling with the complexity of silo architectures and monolithic applications, which they are unable to integrate into and adapt to new business requirements. It is also interesting to note that another key argument of current SOA literature—namely, SOA’s capabilities to dynamically compose services [38, 93, 94]—is not yet regarded as a major factor in current SOA implementations.

## Limitations

While this is one of the first b road studies on SOA’s economic potential, its results cannot be interpreted without taking its limitations into account. The most important limitation is that our analysis relies on secondary data. This not only has implications with respect to the data quality but also imposes the problem that the data were originally collected for a different purpose. This poses the challenge of ensuring the external validity of the constructs used to describe the cause-and-effect chains on our model’s various layers. As applied in our work, the qualitative data analysis calls for an immersion in the materials used [18, 47]. In this context, we looked not only for single elements of our conceptual model but also for entire, logical cause-and-effect links. We consequently not only analyzed individual elements but also looked at the context of their use. This increased our understanding of how and why SOA was implemented, helping us correctly interpret an element and its use in the case material. This, along with our efforts to ensure interrater reliability, helped us improve the validity of the applied constructs.

Beyond this, the fact that press and company publications are generally not as thoroughly reviewed as scientific publications could be regarded as a limitation. We argue that journalistic publications are generally concerned with their reputation and that customers need to approve vendor or consultant publications. Shang and Seddon [81] have demonstrated that assuming that the latter results in a sufficient level of accuracy is adequate for such publications to be used in scientific analysis. On the other hand, company publications might over- or understate certain benefits. We presume that they will not mention benefits based on cause–effect chains that do not exist. Since no inference is made about the strength of a chain found in a case, we feel that potential over- and understatement does not adversely affect our data set.

A similar limitation may be observed with respect to missing chains. If a logical chain is not present in a text, we cannot make any inference about the reason for this.

In this case, the combination of elements (chain) was not explicit enough in the case description to be considered relevant by the raters, but we cannot judge whether the chain was truly missing or whether it was accidentally or intentionally omitted in the case description. An approach to address such potential bias would be the further analysis of the data set with respect to additional variables such as publication type, intended audience of the publication, firm size, or industry. The former two can help reduce bias by, for example, examining whether press or company publications produce significantly different sources of economic potential than scientific publications. The latter are valuable as they can inform future research, especially on the moderating variables discussed above.

The final limitation relates to data interpretation. In order to derive cause–effect links from SOA case descriptions, we carefully analyzed and interpreted the data, which means our approach is open to rater bias. As described earlier, we addressed this challenge by first carefully defining a conceptual model based on the literature to establish a common understanding of the concepts under consideration. Second, we conducted multiple iterations and the raters discussed the problems to ensure interrater reliability during the coding phase. Third, we split our case material into two random subsets to cross validate our findings as described in the paper’s section on the research design.

## Conclusion

## Contributions to Research

Giv en the lack of models to c larify the ec onomic potential of SOA, our research’s long-term aim is to establish a framework for understanding how the IS architectural paradigm SOA generates value on the business side. From our conceptual and exploratory work, we gained important insights into SOA’s sources of economic potential, which advance the understanding of SOA and can be helpful to future IS research. Thereby, we address the economics of service-oriented technology and management, which is one of the key research questions related to SOA [25].

First, we presented a conceptual model, the service-oriented architecture economic potential model (SOA‑ EPM), which is among the first attempts to systematically capture the complex relations that link SOA and its design principles with IS capabilities and the associated economic potential. We used three theoretical perspectives—that is, SOA as an architectural style, the resource-based view, and IS benefit frameworks—to develop causal links that explain SOA’s economic potential. Thus, our model anchors SOA research to prior work regarding IS effectiveness and value. Given that SOA is a novel field of research, the model improves the general understanding of how SOA as an architectural style differs from other IS innovations and how SOA creates benefits from the perspective of the adopting entity.

Second, and in light of the data gathered from 164 SOA case descriptions representing different industry settings, we offer an empirical basis that can stimulate a more detailed investigation of SOA. Our theoretical and empirical investigation reveals IT infrastructure benefits derived from SOA’s modularity as first-order effects of SOA implementations, and it also demonstrates that a more flexible and adaptable IS landscape generates second-order effects leading to operational and strategic benefits.

Third, we extend current SOA research by suggesting propositions and a research model regarding SOA’s economic potential. Our research model comprises the relevant constructs that explain how SOA constitutes economic potential in companies. It represents the SOA’s style in terms of design principles and IS capabilities and relates them to an SOA-specific set of benefit dimensions on the business side. The set of propositions we identified could be a starting point for future investigations into how SOA constitutes economic potential in companies. Therefore, our research model introduces constructs that refine and operationalize the logical reasoning for SOA’s economic potential. With the introduction of constructs and their relationships, an important basis is created that supports future quantitative research, especially by means of structural equation modeling.

## Opportunities for Future Research

From an academic perspective, this study adds to the emerging research stream of service science, management, and engineering [3]. More specifically, the suggested research model and propositions provide a conceptual framework and stimulate future empirically grounded studies on SOA’s economic value. Given the increasing number of companies adopting SOA, testing these propositions with a larger firm sample should produce additional insights into how SOA creates economic potential and how the understanding of these dynamics can inform IS decision makers. Our exploratory study reveals the essential elements, layers, and logical chains for an understanding of SOA’s economic potential, but we have not as yet arrived at firm conclusions regarding the strength of the relations—neither on the case level nor on the general level. Hence, we expect future research will investigate the actual effects of the relations that our research proposes.

Given the absence of a few dominant paths with regard to SOA benefits realization and its nature as an architectural style, more research is needed to identify the factors mediating the relations between SOA’s IS capabilities and benefits, as well as the contingency factors that moderate these effects. Prior research generally confirms that IS value and effectiveness are contingent on a larger number of complementary factors [9, 48, 51]. In the case of SOA, this might suggest that different industries emphasize different facets of the SOA paradigm. The cases we analyzed suggest a number of industry-specific preferences for SOA adoption. The banking industry strongly emphasizes the role of SOA in leveraging legacy applications and ultimately realizing better asset utilization and improving business–IT alignment. We found several examples from other industries—notably, telecommunications—that perceive SOA as an instrument to strengthen their distribution networks, thus creating a competitive advantage. Hence, a promising area of future research is the impact of contingencies—such as industry or competitive environment—and the investigation of factors that mediate the realization of SOA benefits—notably, complementary IT and organizational resources [51]—by means of subgroup analysis, as suggested by Sharma et al. [82].

The same is true for nontechnological aspects and, in particular, for complementary capabilities [9, 51] required for successful SOA implementations. In one of the cases analyzed, an IT executive maintains that SOA “is perhaps 20 percent [about] . . . technology, but the rest is all about business transformation” [68]. This quotation suggests that there are other variables with significant explanatory power regarding SOA’s economic potential. It is furthermore important that future research undertake a subgroup analysis, focusing specifically on organizational and transformational issues, to search for these contingent variables.

In addition to these opportunities for quantitative analysis of SOA’s economic potential, our study also revealed the need for more exploratory studies of some of the constructs involved. This particularly applies to the two IS capabilities reusability and flexibility, which are frequently cited in SOA cases but are not yet fully captured in scientific literature. While previous literature views reusability as reuse of code, our research suggests a broader interpretation of reusability, which takes into account that SOA realizes reuse by the (remote) invocation of services. Hence, future research needs to investigate how IS architectures [96] and business processes [61] should leverage the reusability of services in order to generate economic benefits. Similar opportunities arise for future research with regard to improving our understanding of how SOA enhances the flexibility of the IS architecture, thus creating value.

In light of these opportunities, we believe the SOA value research stream has great potential to help balance SOA’s technological and business-oriented considerations.

## Managerial Implications

Our research has allowed us to examine how practitioners believe SOA, as an emerging architectural paradigm, creates business benefits. The case material confirms the nature of SOA as an architectural style with the potential to create IS capabilities, but which does not generate business value in isolation. Therefore, prior to investment, the results of our research indicate that managers should carefully evaluate SOA and design an appropriate implementation strategy. Our conceptual model and the insights we gained provide IS managers with an instrument for assessing SOA’s economic potential and support them in defining or revising their approach to its implementation. In an increasingly dynamic environment, the ability to align IT and business is driven by the ability to adapt to changing circumstances—a challenge for many IS departments [31]. Our research suggests that SOA is an effective instrument to address these challenges and to form the required IS capabilities.

In contrast to the perception of many authors of recent practitioner publications, current SOA projects are clearly driven by IT departments and focus on IT infrastructure benefits. The potentials on the business side, such as more flexible business processes or improved external coordination, are currently less emphasized and are considered higher-level effects. Approaching an SOA’s capabilities from the business side might enable businesses to obtain economic potential beyond the technological realm. This is also in line with the quotation on business transformation discussed above [68]. The need to further exploit SOA’s dynamic capabilities implies that business units need to be more involved in IS landscapes’ future design.

Our research suggests that SOA is able to extend a firm’s IS capability in terms of both functional range and organizational reach. As external services can be integrated more easily, SOA has a significant potential to reduce vertical integration and improve interorganizational coordination. Managers should closely investigate how value-added services, such as financing solutions for car sales or third-party information services, can help their businesses to more easily and flexibly offer customers additional services. In addition, they should consider how potential synergies with business partners could help leverage other firm capabilities.

Despite its potentials, SOA also saddles management with a new and significant set of challenges. Beyond the discussion on the external sourcing of services with respect to issues of security, reliability, and the rating of services or service providers, the complexity of a distributed, modular IS architecture also needs to be managed in order to ensure that SOA’s benefits outweigh its costs.

## Notes

1. A full reference list of all the sources used is available from the authors on request.

2. Because one company or division of a company could be present in more than one literature source, some SOA implementations were analyzed multiple times. With the SOA implementation as the relevant unit of analysis, however, we decided to consolidate all case material on the company/division level. Hence, chains that were present more than once per company/division were taken into account only once.

3. The cases were equally distributed across the subsamples. However, because there is no fixed number of chains per case, the random assignment resulted in a different number of chains assigned to each subsample. Regarding the 547 chains in the data set, the split resulted in 282:265 chains in the two subsets.

4. Based on Table 4, the percentages are calculated as unweighted averages. For example, the 41 percent mentioned with regard to infrastructure benefits is calculated as follows: [(27/67) + (134/317) + (64/163)]/3 = 41 percent.

5. Based on Table 4, the percentages are calculated as unweighted averages. For example, the 56 percent mentioned with regard to modularity is calculated as follows: [(134/225) + (19/28) + (103/175) + (6/14) + (55/105)]/5 = 56 percent.

6. We used an agglomerative hierarchical cluster analysis using the single-linkage method.

7. We grouped IS capabilities based on the design principle with which they are most often connected. To do so, we used links accounting for more than 3 percent of the total number of links on the respective layer. The same logic was applied to the economic side, where elements with links greater than 3 percent were associated with the respective benefit dimensions. Elements with less than 3 percent were not included in the research model depicted above.

## Referenc es

1. Al-Naeem, T.; Rabhi, F.A.; Benatallah, B.; and Ray, P.K. Systematic approaches for designing B2B applications. International Journal of Electronic Commerce, 9, 2 (Winter 2004), 41–70.

2. Anderson, D.; Howell-Barber, H.; Hill, J.; Javed, N.; Lawler, J.; and Zheng, L. A study of Web services projects in the financial services industry. Information Systems Management, 22, 1 (Winter 2005), 66–76.

3. Bardhan, I.; Demirkan, H.; Kannan, P.K.; Kauffman, R.J.; and Sougstad, R. An interdisciplinary perspective on IT services management and service science. Journal of Management Information Systems, 26, 4 (Spring 2010), 13–64, this issue.

4. Barney, J.B. Resource-based theories of competitive advantage: A ten-year retrospective on the resource-based view. Journal of Management, 27, 6 (2001), 643–650.

5. Baron, R.M., and Kenny, D.A. The moderator–mediator variable distinction in social psychological research: Conceptual, strategic, and statistical considerations. Journal of Personality and Social Psychology, 51, 6 (December 1986), 1173–1182.

6. Barua, A.; Kriebel, C.H.; and Mukhopadhyay, T. Information technologies and business value: An analytic and empirical investigation. Information Systems Research, 6, 1 (March 1995), 3–23.

7. Baskerville, R.; Cavallari, M.; Hjort-Madsen, K.; Pries-Heje, J.; Sorrentino, M.; and Virili, F. Extensible architectures: The strategic value of service-oriented architecture in banking. In D. Bartmann, F. Rajola, J. Kallinikos, D. Avison, R. Winter, P. Ein-Dor, J. Becker, F. Bodendorf, and C. Weinhardt (eds.), Proceedings of the Thirteenth European Conference on Information Systems (ECIS 2005). Atlanta: Association for Information Systems, 2005, pp. 761–772.

8. Becker, A.; Buxmann, P.; and Widjaja, T. Value potential and challenges of service-oriented architectures—A user and vendor perspective. In S. Newell, E. Whitley, N. Pouloudi, J. Wareham, and L. Mathiassen (eds.), Proceedings of the Seventeenth European Conference on Information Systems (ECIS 2009). Atlanta: Association for Information Systems, 2009, pp. 616–628.

9. Bharadwaj, A.S. A resource-based perspective on information technology capability and firm performance: An empirical investigation. MIS Quarterly, 24, 1 (March 2000), 169–196.

10. Brown, A.W.; Johnston, S.; and Kelly, K. Using Service-Oriented Architecture and Component-Based Development to Build Web Service Applications. Santa Clara, CA: Rational Software Corporation, 2002.

11. Brown, A.W.; Delbaere, M.; Eeles, P.; Johnston, S.; and Weaver, R. Realizing serviceoriented solutions with the IBM rational software development platform. IBM Systems Journal, 44, 4 (2005), 727–752.

12. Brynjolfsson, E. The productivity paradox of information technology: Review and assessment. Communications of the ACM, 36, 12 (December 1993), 67–77.

13. Brynjolfsson, E., and Hitt, L.M. Paradox lost? Firm-level evidence on the returns to information systems spending. Management Science, 42, 4 (April 1996), 541–558.

14. Brynjolfsson, E., and Hitt, L.M. Beyond computation: Information technology, organizational transformation and business performance. Journal of Economic Perspectives, 14, 4 (Fall 2000), 23–48.

15. Cameron, K.S., and Whetten, D.A. Organizational Effectiveness: A Comparison of Multiple Models. New York: Academic Press, 1983.

16. Carr, N.G. IT doesn’t matter. Harvard Business Review, 81, 5 (May 2003), 41–49.

17. Chang, H.H. Technical and management perceptions of enterprise information system importance, implementation and benefits. Information Systems Journal, 16, 3 (July 2006), 263–292.

18. Choudhury, V., and Sabherwal, R. Portfolios of control in outsourced software development projects. Information Systems Research, 14, 3 (September 2003), 291–314.

19. Clemons, E.K.; Reddi, S.P.; and Row, M.C. The impact of information technology on the organization of economic activity: The “move to the middle” hypothesis. Journal of Management Information Systems, 10, 2 (Fall 1993), 9–35.

20. Davis, F.D. Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13, 3 (September 1989), 319–340.

21. Davis, F.D.; Bagozzi, R.P.; and Warshaw, P.R. User acceptance of computer technology: A comparison of two theoretical models. Management Science, 35, 8 (August 1989), 982–1003.

22. DeLone, W.H., and McLean, E.R. Information systems success: The quest for the dependent variable. Information Systems Research, 3, 1 (March 1992), 60–95.

23. DeLone, W.H., and McLean, E.R. The DeLone and McLean model of information systems success: A ten-year update. Journal of Management Information Systems, 19, 4 (Spring 2003), 9–30.

24. Demirkan, H., and Goul, M. AMCIS 2006 panel summary: Towards the service oriented enterprise vision: Bridging industry and academics. Communications of the AIS, 18, 26 (2006), 546–556.

25. Demirkan, H.; Kauffman, R.J.; Vayghan, J.A.; Fill, H.-G.; Karagiannis, D.; and Maglio, P.P. Service-oriented technology and management: Perspectives on research and practice for the coming decade. Electronic Commerce Research & Applications, 7, 4 (Winter 2008), 356–376.

26. Doherty, N.F., and Terry, M. The role of IS capabilities in delivering sustainable improvements to competitive positioning. Journal of Strategic Information Systems, 18, 2 (June 2009), 100–116.

27. Dostal, W.; Jeckle, M.; Melzer, I.; and Zengler, B. Service-Orientierte Architekturen mit Web Services [Service-Oriented Architecture Using Web Services]. Munich: Spektrum Akademischer Verlag, 2005.

28. Erl, T. Service-Oriented Architecture: Concepts, Technology, and Design. Upper Saddle River, NJ: Prentice Hall, 2005.

29. Fettke, P. State-of-the-art des state-of-the-art: Eine Untersuchung der Forschungsmethode: review innerhalb der Wirtschaftsinformatik [State-of-the-art of the state-of-the-art: A study of the research method review in the information systems discipline]. Wirtschaftsinformatik, 48, 4 (August 2006), 257–266.

30. Fielding, R.T. Architectural styles and the design of network-based software architectures. Ph.D. dissertation, University of California, Irvine, 2000.

31. Gallagher, K.P., and Worrell, J.L. Organizing IT to promote agility. Information Technology and Management, 9, 1 (March 2008), 71–88.

32. Gallivan, M.J.; Truex, D.P.; and Kvasny, L. Changing patterns in IT skill sets 1988–2003: A content analysis of classified advertising. ACM SIGMIS Database, 35, 3 (Summer 2004), 64–87.

33. Gefen, D., and Ragowsky, A. A multi-level approach to measuring the benefits of an ERP system in manufacturing firms. Information Systems Management, 22, 1 (Winter 2005), 18–25.

34. Gosain, S. Realizing the vision for Web services: Strategies for dealing with imperfect standards. Information Systems Frontiers, 9, 1 (March 2007), 53–67.

35. Grant, R.M. The resource-based theory of competitive advantage. California Management Review, 33, 3 (Spring 1991), 114–135.

36. Grant, R.M. Contemporary Strategy Analysis. Oxford: Blackwell, 1995.

37. Gregor, S. The nature of theory in information systems. MIS Quarterly, 30, 3 (September 2006), 611–642.

38. Hagel, J., and Brown, J.S. Your next IT strategy. Harvard Business Review, 79, 9 (October 2001), 105–113.

39. Hagen, C. Integrationsarchitektur der Credit Suisse [Integration architecture of Credit Suisse]. In S. Aier and M. Schönherr (eds.), Enterprise Application Integration: Flexibilisierung Komplexer Unternehmensarchitekturen [Enterprise Application Integration: Making Complex Enterprise Architectures Flexible]. Berlin: GITO Verlag, 2004, pp. 61–83.

40. Hau, T.; Ebert, N.; Hochstein, A.; and Brenner, W. Where to start with SOA: Criteria for selecting SOA projects. In R.H. Sprague (ed.), Proceedings of the Forty-First Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, 2008 (available at www.computer.org/plugins/dl/pdf/proceedings/hicss/2008/3075/00/30750314.pdf ?template=1&loginState=1&userData=anonymous-IP%253A%253A71.99.94.194).

41. Heffner, R. SOA adoption: Budgets don’t matter much. White Paper, Forrester Research, Cambridge, MA, 2008.

42. Heinrich, L.J. Informationsmanagement: Planung, Überwachung und Steuerung der Informationsinfrastruktur [Information Management: Planning, Controlling, and Steering the Information Infrastructure]. Munich: Oldenbourg, 2002.

43. Hitt, L.M.; Wu, D.J.; and Zhou, X. Investment in enterprise resource planning: Business impact and productivity measures. Journal of Management Information Systems, 19, 1 (Summer 2002), 71–98.

44. Holmqvist, M., and Pessi, K. Process integration and Web services. Scandinavian Journal of Information Systems, 16, Special Issue (2004), 117–144.

45. Huang, D., and Hu, Q. Integrating Web services with competitive strategies: A balanced scorecard approach. Communications of the AIS, 13, 6 (2004), 57–80.

46. Huhns, M.N., and Singh, M.P. Service-oriented computing: Key concepts and principles. IEEE Internet Computing, 9, 1 (January–February 2005), 75–81.

47. Kaplan, B., and Duchon, D. Combining qualitative and quantitative methods in information systems research: A case study. MIS Quarterly, 12, 4 (December 1988), 571–586.

48. Karimi, J.; Somers, T.M.; and Bhattacherjee, A. The impact of ERP implementation on business process outcomes: A factor-based study. Journal of Management Information Systems, 24, 1 (Summer 2007), 101–127.

49. Khoumbati, K.; Themistocleous, M.; and Irani, Z. Evaluating the adoption of enterprise application integration in health-care organizations. Journal of Management Information Systems, 22, 4 (Spring 2006), 69–108.

50. Kohli, R., and Devaraj, S. Measuring information technology payoff: A meta-analysis of structural variables in firm-level empirical research. Information Systems Research, 14, 2 (June 2003), 127–145.

51. Kohli, R., and Grover, V. Business value of IT: An essay on expanding research directions to keep up with the times. Journal of the AIS, 9, 1 (2008), 23–39.

52. Kossmann, D., and Leymann, F. Web services. Informatik Spektrum, 27, 2 (April 2004), 117–128.

53. Krafzig, D.; Banke, K.; and Slama, D. Enterprise SOA. Upper Saddle River, NJ: Prentice Hall, 2004.

54. Lagerström, R., and Öhrström, J. A framework for assessing business value of service oriented architectures. In L.-J. Zhang, W. van der Aalst, and P.C.K. Hung (eds.), Proceedings of the 2007 IEEE International Conference on Services Computing (SCC 2007). Los Alamitos, CA: IEEE Computer Society Press, 2007, pp. 670–671.

55. Legner, C., and Heutschi, R. SOA adoption in practice—Findings from early SOA implementations. In H. Österle, J. Schelp, and R. Winter (eds.), Proceedings of the Fifteenth European Conference on Information Systems (ECIS 2007). Atlanta: Association for Information Systems, 2007, pp. 1643–1654.

56. Legner, C., and Heutschi, R. Service-oriented architecture—From concept to implementation. Information Systems Journal, 2010, forthcoming.

57. Lim, B., and Wen, H.J. Web services: An analysis of the technology, its benefits, and implementation difficulties. Information Systems Management, 20, 2 (Spring 2003), 49–57.

58. Luthria, H., and Rabhi, F. Service oriented computing in practice—An agenda for research into the factors influencing the organizational adoption of service oriented architectures. Journal of Theoretical and Applied Electronic Commerce Research, 4, 1 (April 2009), 39–56.

59. Malone, T.W.; Yates, J.; and Benjamin, R.I. Electronic markets and electronic hierarchies. Communications of the ACM, 30, 6 (June 1987), 484–497.

60. March, S.; Hevner, A.R.; and Ram, S. Research commentary: An agenda for information technology research in heterogeneous and distributed environments. Information Systems Research, 11, 4 (December 2000), 327–341.

61. Markovic, I., and Pereira, A.C. Towards a formal framework for reuse in business process modeling. In A. ter Hofstede, B. Benatallah, and H.-Y. Paik (eds.), Business Process Management Workshops: Lecture Notes in Computer Science, vol. 4928. Berlin and Heidelberg: Springer, 2008, pp. 484–495.

62. Mata, F.J.; Fuerst, W.L.; and Barney, J.B. Information technology and sustained competitive advantage: A resource-based analysis. MIS Quarterly, 19, 4 (December 1995), 487–505.

63. McGovern, J.; Tyagi, S.; Stevens, M.; and Mathew, S. Service-oriented architecture. In J. McGovern, S. Tyagi, M. Stevens, and S. Mathew (eds.), Java Web Services Architecture. San Francisco: Morgan Kaufmann, 2003, pp. 35–63.

64. Melville, N.; Kraemer, K.; and Gurbaxani, V. Information technology and organizational performance: An integrative model of IT business value. MIS Quarterly, 28, 2 (June 2004), 283–322.

65. Merrifield, R.; Calhoun, J.; and Stevens, D. The next revolution in productivity. Harvard Business Review, 86, 6 (June 2008), 72–80.

66. Mukhopadhyay, T.; Rajiv, S.; and Srinivasan, K. Information technology impact on process output and quality. Management Science, 43, 12 (December 1997), 1645–1659.

67. Müller, B.; Viering, G.; Ahlemann, F.; and Riempp, G. Towards understanding the sources of the economic potential of service-oriented architecture: Findings from the automotive and banking industry. In H. Österle, J. Schelp, and R. Winter (eds.), Proceedings of the Fifteenth European Conference on Information Systems (ECIS 2007). Atlanta: Association for Information Systems, 2007, pp. 1608–1619.

68. Murray, J. Interview: BT cuts costs with service-oriented architecture. IT Week (August 11, 2006) (available at www.computing.co.uk/articles/print/2162201).

69. Newcomer, E., and Lomow, G. Understanding SOA with Web Services. Reading, MA: Addison-Wesley, 2004.

70. Papazoglou, M.P., and Georgakopoulos, D. Service-oriented computing. Communications of the ACM, 46, 10 (October 2003), 24–28.

71. Papazoglou, M.P., and van den Heuvel, W.-J. Service oriented architectures: Approaches, technologies and research issues. International Journal on Very Large Data Bases, 16, 3 (July 2007), 389–415.

72. Paré, G. Investigating information systems with positivist case study research. Communications of the AIS, 13, 18 (2004), 233–264.

73. Peppard, J., and Ward, J. Beyond strategic information systems: Towards an IS capability. Journal of Strategic Information Systems, 13, 2 (July 2004), 167–194.

74. Peppard, J.; Weill, P.; and Daniel, E. Managing the realization of business benefits from IT investments. MIS Quarterly Executive, 6, 1 (2007), 1–11.

75. Qian, T., and Hsing, C. Optimal strategies for a monopoly intermediary in the supply chain of complementary Web services. Journal of Management Information Systems, 23, 3 (Winter 2006–7), 275–307.

76. Rhee, S.-H.; Bae, H.; and Choi, Y. Enhancing the efficiency of supply chain processes through Web services. Information Systems Frontiers, 9, 1 (March 2007), 103–118.

77. Romano, N.C.; Donovan, C.; Chen, H.; and Nunamaker, J.F. A methodology for analyzing Web-based qualitative data. Journal of Management Information Systems, 19, 4 (Spring 2003), 213–246.

78. Saaty, T.L. The Analytic Hierarchy Process. New York: McGraw-Hill, 1980.

79. Sabherwal, R., and Sabherwal, S. Knowledge management using information technology: Determinants of short-term impact on firm value. Decision Sciences, 36, 4 (December 2005), 531–567.

80. Seddon, P.; Staples, S.; Patnayakuni, R.; and Bowtell, M. Dimensions of information systems success. Communications of the AIS, 2, 20 (1999), 1–61.

81. Shang, S., and Seddon, P.B. Assessing and managing the benefits of enterprise systems: The business manager’s perspective. Information Systems Journal, 12, 4 (October 2002), 271–299.

82. Sharma, S.; Durand, R.M.; and Gur-Arie, O. Identification and analysis of moderator variables. Journal of Marketing Research, 18, 3 (August 1981), 291–300.

83. Siedersleben, J. SOA revisited: Komponentenorientierung bei Systemlandschaften [SOA revisited: Component orientation by system landscape]. Wirtschaftsinformatik, 49, Special Issue (February 2007), 110–117.

84. Tafti, A.; Mithas, S.; and Krishnan, M.S. The effects of information technology and serviceoriented architectures on joint venture value. In Proceedings of the Twenty-Ninth International Conference on Information Systems (ICIS 2008). Atlanta: Association for Information Systems, 2008 (available at http://aisel.aisnet.org/icis2008/72/).

85. Tesch, R. Qualitative Research Analysis Types and Software Tools. New York: Falmer Press, 1990.

86. Themistocleous, M. Justifying the decisions for EAI implementations: A validated proposition of influential factors. Journal of Enterprise Information Management, 17, 2 (2004), 85–104.

87. Umapathy, K., and Purao, S. A theoretical investigation of the emerging standards for Web services. Information Systems Frontiers, 9, 1 (March 2007), 119–134.

88. Urbach, N.; Smolnik, S.; and Riempp, G. A methodological examination of empirical research on information systems success: 2003 to 2007. In Proceedings of the Fourteenth Americas Conference on Information Systems (AMCIS 2008). Atlanta: Association for Information Systems, 2008 (available at http://aisel.aisnet.org/amcis2008/7/).

89. Viering, G., and Müller, B. Economic Potential of Service-Oriented Architecture. Lohmar and Cologne: Josef Eul, 2007.

90. Webster, J., and Watson, R.T. Analyzing the past to prepare for the future: Writing a literature review. MIS Quarterly, 26, 2 (June 2002), xiii–xxiii.

91. Yang, J. Web service componentization. Communications of the ACM, 46, 10 (October 2003), 35–40.

92. Zencke, P., and Eichin, R. SAP Business ByDesign—die neue Mittelstandslösung der SAP [SAP Business ByDesign—The new midsize-enterprise solution of SAP ]. Wirtschaftsinformatik, 50, 1 (January 2008), 47–51.

93. Zhao, J.L., and Cheng, H.K. Web services and process management: A union of convenience or a new area of research? Decision Support Systems, 40, 1 (July 2005), 1–8.

94. Zhao, J.L.; Tanniru, M.; and Zhang, L.-J. Services computing as the foundation of enterprise agility: Overview of recent advances and introduction to the special issue. Information Systems Frontiers, 9, 1 (March 2007), 1–8.

95. Zhao, J.L.; Goul, M.; Purao, S.; Vitharana, P.; and Wang, H.J. Impact of service-centric computing on business and education. Communications of the AIS, 22, 16 (2008), 1–14.

96. Zimmermann, O.; Gschwind, T.; Küster, J.; Leymann, F.; and Schuster, N. Reusable architectural decision models for enterprise application development. In S. Overhage, C.A. Szyperski, R. Reussner, and J.A. Stafford (eds.), Proceedings of the Third International Conference on Quality of Software Architectures (QoSA 2007). Medford, MA: Springer, 2008, pp. 15–32.

![](/api/attachments/VT35T3KJ/fulltext/images/574fb696f59ad2e75499daea51bebee619cad6deb5c3fde59a3120abb839c94b.jpg)  
# Number of times this element was mentioned in the case material analzyed

Appendix Figure A1. Service-Oriented Architecture Economic Potential Model (SOA-EPM) Including the Analysis of Elements in the Cases
