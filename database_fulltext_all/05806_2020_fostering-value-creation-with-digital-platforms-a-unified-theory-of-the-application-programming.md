---
otero_id: 5806
otero_key: "NEWPV6BA"
title: "Fostering Value Creation with Digital Platforms: A Unified Theory of the Application Programming Interface Design"
authors: "Jochen Wulf; Ivo Blohm"
year: "2020"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2019.1705514"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Fostering Value Creation with Digital Platforms: A Unified Theory of the Application Programming Interface Design

Jochen Wulf & Ivo Blohm

To cite this article: Jochen Wulf & Ivo Blohm (2020) Fostering Value Creation with Digital Platforms: A Unified Theory of the Application Programming Interface Design, Journal of Management Information Systems, 37:1, 251-281, DOI: 10.1080/07421222.2019.1705514

To link to this article: https://doi.org/10.1080/07421222.2019.1705514

![](/api/attachments/NEWPV6BA/fulltext/images/fcc5bbfde233b4c961be398b1c77a0c9958c56e3f17a2a81819b29917d4df75a.jpg)

View supplementary material

![](/api/attachments/NEWPV6BA/fulltext/images/c06e10fefe4f2d11889e96f75236ae898c37a69a8b70dd94ee38857f0056336d.jpg)

Published online: 01 Mar 2020.

![](/api/attachments/NEWPV6BA/fulltext/images/e8d58fd7b41caede3a92f1ae8ae1cc34ba74e45f640c8cf23e50b28ddd5c9654.jpg)

Submit your article to this journal

![](/api/attachments/NEWPV6BA/fulltext/images/841d7258a3b85f853f0167b9e3a50c2b20e9a3bd57d73bed4c7166bf74777998.jpg)

View related articles

![](/api/attachments/NEWPV6BA/fulltext/images/03319416fcf227bf3970da431f69e09b296fe7687f78711308e81e18081795c9.jpg)

View Crossmark data

Check for updates

# Fostering Value Creation with Digital Platforms: A Uni<sup>fi</sup>ed Theory of the Application Programming Interface Design

Jochen Wulf and Ivo Blohm

Institute of Information Management, University of St.Gallen, St. Gallen, Switzerland

## ABSTRACT

While many <sup>fi</sup>rms in recent years have started to o<sup>f</sup>er public Application Programming Interfaces (APIs), <sup>fi</sup>rms struggle with shaping digital platform strategies that align API design with aspired business goals and the demands of external developers. We address the lack of theory that explains the performance impacts of three API archetypes (professional, mediation, and open asset services). We couple survey data from 152 API product managers with manually coded API design classi<sup>fi</sup>cations. With this data, we conduct cluster and regression analyses that reveal moderating e<sup>f</sup>ects of two value creation strategies (economies of scope in production and innovation) on the relationships between API archetype similarity and two API performance outcomes: return on investment and di<sup>f</sup>usion. We contribute to IS literature by developing a unifying theory that consolidates di<sup>f</sup>erent theoretical perspectives on API design, by extending current knowledge on the performance e<sup>f</sup>ects of API design, and by empirically studying the distinct circumstances under which digital platforms facilitate economies of scope in production or in innovation. Our results provide practical implications on how API providers can align API archetype choice with the value creation strategy and the API’s business objective.

## KEYWORDS

Application programming interface; boundary resource; digital platform; economies of scope; cluster analysis; API design

## Introduction

The growing number of publicly available Application Programming Interfaces (APIs) suggests that o<sup>f</sup>ering APIs today has become a common instrument of digital strategy [85]. The API directory ProgrammableWeb reported over 22,500 registered APIs in October 2019 and a <sup>fi</sup>ve-year consecutive growth rate of over 10 percent [85]. By now, successfully designed and managed APIs outperform traditional modes of service distribution (such as e-commerce websites) at well-known digital service providers such as Expedia, eBay, and Salesforce [51, 73].

The majority of API providers, however, struggles with designing successful APIs, because a solid technical solution does not su<sup>fi</sup>ce; rather, the API must align with the overall business objectives and the demands of third-party developers and end customers [11]. Considering that APIs transform entire industries by enabling agile service development, specialization, scalability, and leveraging network e<sup>f</sup>ects [73], many <sup>fi</sup>rms overlook the APIs’ signi<sup>fi</sup>cance for their strategic competitiveness [51]. The misalignment of an API’s design and its provider’s business objectives may be the consequence. For example, a lot of API providers adopt transaction-based pricing models [12]. However, establishing two-sided platforms by means of an API and attracting third-party developers requires paying out commissions to developers for each transaction as the case of Walgreen’s Photo Prints API demonstrates [3]. Furthermore, many API initiatives fail because of insu<sup>fi</sup>cient knowledge about the targeted segment of third-party developers [12]. Hence, APIs provide insu<sup>fi</sup>cient incentives for these developers or fail to align the API provider’s business interests with those of developers [3]. Lastly, focusing on APIs as a single channel for distributing software solutions may impose high implementation e<sup>f</sup>ort on software adopters [58]. Owing to these challenges, API providers require knowledge that supports the alignment of API design, their business goals, and the objectives of third-party developers.

The literature on digital platforms broadly considers APIs as boundary resources through which platform providers execute choices of platform architecture and governance [22, 38, 99-101]. Our literature synthesis yields three API archetypes with characteristic di<sup>f</sup>erences regarding the design of a platform’s partitioning, systems integration, decision rights, control, and pricing. Professional services provide access to cloud-based information technology (IT) resources, which providers traditionally distribute as installable software or make accessible via browser-based interfaces [7, 61, 106]. Mediation services o<sup>f</sup>er access to a two-sided platform’s resources based on which third-party developers design complementary service o<sup>f</sup>erings for the platform’s end customers [75, 79, 94]. Open asset services give free-of-charge access to organization-internal IT resources with low integration e<sup>f</sup>ort [48, 56, 64, 84].

We survey 152 API providers and investigate the interaction e<sup>f</sup>ects of API design and two value creation strategies — economies of scope in production and innovation — on API return on investment (ROI) and di<sup>f</sup>usion. We apply qualitative content analysis to these APIs in order to reveal API design choices that may in<sup>fl</sup>uence API performance. Applying cluster analysis, we verify the theoretically derived typology of professional, mediation, and open asset services. We show that one can distinguish these services by distinct API design characteristics. Furthermore, we conduct ordinal logistic and negative binomial regression analyses and show that API providers that align their APIs’ design with the intended platform-based value creation mechanism exhibit higher levels of API ROI and di<sup>f</sup>usion. Speci<sup>fi</sup>cally, we <sup>fi</sup>nd that API providers that follow the archetypical designs of professional or mediation services and that target economies of scope in production have higher levels of API ROI than others. API providers that choose an open asset services design and target economies of scope in innovation exhibit higher levels of API di<sup>f</sup>usion than others.

Our research contributes to closing three research gaps in the digital platforms literature. First, prior literature on API design is scattered and studies API design in disparate and isolated contexts. One group of authors considers APIs as distribution channels for cloud-based professional services [7, 25, 41, 106]. A second group studies APIs as boundary resources to multi-sided platforms [27, 37, 38, 75, 79]. A third group analyzes APIs in the context of open data [48, 56, 64, 84]. Considering the strategic role of APIs for platform providers [9] and that this disparate literature insu<sup>fi</sup>ciently explains how the breadth of possible API design choices relating to platform architecture and governance a<sup>f</sup>ects strategic API outcomes, Yoo et al. [108] call for a generalizable theory that explains API design choices and strategic consequences. Addressing this call, we provide a unifying perspective on the design of three API archetypes that explains API design and strategic API outcomes across these distinct literature streams. It is grounded in contemporary literature on platform architecture and governance [99, 100] and synthesizes prior API literature.

Second, prior API research does not study the design and outcomes of individual APIs but looks at an aggregate level at the set of APIs o<sup>f</sup>ered by a <sup>fi</sup>rm [9] and by a platform [8, 93, 101, 107]. These studies only allow limited implications on the design and performance e<sup>f</sup>ects at the level of individual APIs. They focus on a <sup>fi</sup>rm’s or platform’s general use of potentially multiple APIs and do not establish a direct relationship between the design of individual APIs and API performance. By choosing the API as unit of analysis, we provide novel theory regarding the distinct consequences of API-level design choices on API performance in terms of API ROI and di<sup>f</sup>usion.

Third, prior literature provides disconnected theories of how platforms facilitate value creation in platform-based ecosystems [36]. Some authors theorize on platform-based economies of scope in production [55, 71]. Other authors focus on economies of scope in innovation [1, 74]. An integrating theory that explains how APIs facilitate either or both value creation mechanisms is currently missing. Adopting a conceptualization that “sees platforms through an organizational lens” [36, p. 1240], we integrate these two perspectives and study simultaneously how APIs facilitate economies of scope in production and innovation.

In summary, our research addresses the lack of theory that interrelates di<sup>f</sup>erent API design choices, platform-based value creation mechanisms, and API-level performance. We develop a theoretical model that proposes how the interaction of API design with a platform provider’s targeted value creation mechanism a<sup>f</sup>ects an API’s ROI and di<sup>f</sup>usion. This paper proceeds as follows. In the theoretical foundations, we discuss prior research on digital platforms and APIs. Subsequently, we develop our hypotheses in the theory development section. We then present our research methodology and estimation approach, followed by the results section. After a discussion of the contributions, we end with limitations and potential avenues for future research.

## Theoretical Foundations

We de<sup>fi</sup>ne APIs as machine-readable interfaces that connect multiple applications, govern application interaction, and remove the need to know the inner workings of how an API’s functionality is provided [53]. While APIs may also regulate the communication on local machines, this study focuses on web services that provide remote access over the Internet [20]. We focus our analysis on the large API subgroup of public APIs that are accessible from outside of a company’s network [53, 85]. API providers openly communicate the speci<sup>fi</sup>cation of public APIs in order to promote APIs to the community of third-party developers. In the next subsections, we discuss how API design relates to the architecture and governance of digital platforms and prior research on API archetypes.

## Architecture and Governance of Digital Platforms

APIs represent boundary resources of digital platforms [22, 38]. Boundary resources are software tools that transfer design capability to developers [103] and allow platform owners to control the ecosystem that is formed by third-party developers [38]. Hence, boundary resources are regulations that control the arm’s-length relationship between a platform owner and application developers [38]. From a technological perspective, digital platforms consist of an extensible codebase for a core functionality that is shared by connected modules and interfaces such as APIs. Modules are software subsystems, that is, applications that third-party developers provide and that add functionality to the platform. APIs support the interoperation between platform core and modules [99]. One can distinguish platforms by design choices related to platform architecture and governance [99-101], which are executed through boundary resources such as APIs [22, 38, 86]. The information systems literature discusses several aspects related to API design (API characteristics) that have an impact on platform architecture and governance, which we summarize in Table 1 and discuss in the following.

Architecture has two main functions: (1) partitioning and (2) systems integration [100].

Partitioning refers to how platform-based functions are decomposed into relatively autonomous subsystems (i.e., modules). A trait of partitioning is platform span (i.e., the number of modules that is determined by the level of functional disaggregation) [90]. The scope of functionalities that a platform owner exposes via APIs is characteristic for the platform [8]. The API literature distinguishes between decomposition at the architectural level of application functionality or even <sup>fi</sup>ner disaggregation at the level of data or infrastructure access [108]. Accordingly, API functionality refers to providing complex information processing capabilities [107], that is, executing business processes [110], in contrast to making accessible lower-level resources, that is, data- and infrastructure-as -a-service [25, 46]. Partitioning not only applies to an API’s level of functional disaggregation, but also relates to the distribution of end customer-oriented functionality. APIs can be designed as a distribution channel that connects third-party developers with an API provider’s end customers [92]. APIs then provide end customer access that allows developers to exploit platform-based marketing resources [87] and to o<sup>f</sup>er value-added services to the platform’s installed end customer base [60].

Systems integration refers to how a platform provider interconnects with external developers. It is common to extend a software product by o<sup>f</sup>ering an API as an alternative access channel [76], because o<sup>f</sup>ering APIs facilitates the integration into customers’ systems landscapes [61]. We refer to such an API access to services that providers complementarily distribute as software products or via websites as multi-channel access. Furthermore, APIs can allow secure communication by using message encryption standards [42]. Security risks (e.g., data leakage) are among the most important barriers for adopting professional services [63]. The API trait security thus characterizes an API provider’s investments into function assurance by implementing encryption mechanisms.

API characteristics, de<sup>fi</sup>nitions, and guiding references.

<table><tr><td>Platform component</td><td>API element</td><td>Definition</td><td>Guiding references</td></tr><tr><td rowspan="2">Partitioning</td><td>Function</td><td>API carries out information processing task</td><td>[8, 107, 108]</td></tr><tr><td>End customer access</td><td>API links developers to end customers</td><td>[60, 87, 99]</td></tr><tr><td rowspan="2">Systems integration</td><td>Multi-channel access</td><td>Functionality or data is accessible through alternative channels</td><td>[61, 76]</td></tr><tr><td>Security</td><td>API supports data encryption (e.g., https)</td><td>[42, 63]</td></tr><tr><td>Decision rights</td><td>End customer relationship</td><td>API maintains own relationship with end customers</td><td>[9, 37, 99]</td></tr><tr><td>Control</td><td>User authorization</td><td>API supports user authentication (e.g., key or token based)</td><td>[42, 64]</td></tr><tr><td rowspan="3">Pricing</td><td>Subscription-based charging</td><td>API users are charged by subscription-oriented logic</td><td>[61, 76, 110]</td></tr><tr><td>Transaction-based charging</td><td>API users are charged by transaction-oriented logic</td><td>[61, 76, 110]</td></tr><tr><td>Revenue sharing</td><td>API provider shares revenues with developers</td><td>[54, 77, 79]</td></tr></table>

Notes: API = Application Programming Interface

Platform governance addresses (1) the allocation of decision rights, (2) the execution of control, and (3) a platform’s pricing policies [100].

The decision right to maintain the end customer relationship is a strategic component [92]. A platform owner can either keep this right or leave this to the external developer. API providers that keep the end customer relationship can steer API developers towards implementing services that are complementary to the API providers’ end customer-facing o<sup>f</sup>erings [9]. APIs then position third-party modules to <sup>fi</sup>ll holes in the API provider’s product line [37] or to innovate value-adding functionality to an API providers’ platform [99].

Regarding the execution of platform control, the process of granting permission for an activity represents a functional component in API speci<sup>fi</sup>cations [42]. Since APIs allow access to proprietary resources, API providers must protect their strategic assets and — at the same time — encourage developer innovation [99]. Authorization allows API providers to execute control [9]. Alternatively, API providers may go without authorization in order to decrease adoption barriers (e.g., in the case of open data) [64].

API providers execute platform pricing via two API features. APIs can serve as a direct source of revenue via charging [110]. Charging strategies may include transaction-based and subscription-based charges [76]. Alternatively, providers may o<sup>f</sup>er API access free-ofcharge and aim at non-monetary bene<sup>fi</sup>ts [29]. Furthermore, API providers can use revenue sharing to attract API developers with the goal to enrich an API provider’s product o<sup>f</sup>erings [54]. For example, the appropriation of value between providers and developers through revenue sharing represents a key success factor for o<sup>f</sup>ering a wide portfolio of services in mobile ecosystems [77, 79].

## Typology of Public APIs

A synthesis of API literature (see Supplemental Appendix A) suggests that API providers o<sup>f</sup>er three distinct services and that each of these API archetypes incorporates distinct API characteristics related to the design of API architecture and governance. We de<sup>fi</sup>ne these archetypes in Table 2.

## Professional Services

Professional services o<sup>f</sup>er infrastructure-, platform-, data-, or software-as-a-service. Via standardized interfaces, they facilitate the consumption of the API provider’s modularized o<sup>f</sup>erings [7, 106]. For example, mobile network operators o<sup>f</sup>er APIs that provide paid access to the telecommunication network’s functionalities such as telephony [41]. Professional services represent alternative channels to browser-based or o<sup>f</sup>-the-shelve software o<sup>f</sup>erings. For example, with the Cloud Datastore service, Google o<sup>f</sup>ers data-as -a-service via a browser-based editor and, alternatively, via the Cloud Datastore API [25].

API archetypes.

<table><tr><td>Archetype</td><td>Definition</td><td>Sources</td><td>Examples</td></tr><tr><td>Professional service</td><td>API provides access to cloud-based IT resources with direct or indirect charging that providers traditionally distribute as installable software or make accessible via browser-based interfaces.</td><td>[7, 29, 47, 61, 76, 106]</td><td>Amazon S3 API, SAP Anywhere API, Google Maps API, AccuWeather Forecast API, FedEx API, Expedia API</td></tr><tr><td>Mediation service</td><td>API offers access to a two-sided platform&#x27;s resources based on which third-party developers design complementary service offerings for the platform&#x27;s end customers.</td><td>[75, 79, 80, 87, 94]</td><td>Facebook Graph API, Twitter Direct Message API, Youtube Live Streaming API, Amazon Product Advertising API, LinkedIn API</td></tr><tr><td>Open asset service</td><td>API gives free-of-charge access to organization-internal IT resources with low integration effort.</td><td>[35, 48, 56, 64, 84]</td><td>New York Times API, DB Open Data API, BBC Nitro API, NBA Stats API, Github API</td></tr></table>

Notes: API = Application Programming Interface

Professional service providers generate direct revenue streams by charging for API consumption [29, 61, 76].

## Mediation Services

Mediation services expose platform resources to third-party developers, upon which thirdparty developers innovate end customer-facing services that are complementary to the platform’s end customer-oriented o<sup>f</sup>erings [94]. Mediation services provide, among others, business development, marketing, and resource bundling [87]. Providers of mediation services o<sup>f</sup>er incentives in order to subsidize third-party innovation. The Android API, for example, includes free API access to Google’s Android platform and is supplemented with revenue-sharing mechanisms via the Google Play store [79].

## Open Asset Services

Open asset services provide free-of-charge access to proprietary IT assets of a company [35, 48, 56]. Such o<sup>f</sup>erings include open access to data [48, 64], to infrastructure, or to applications [35]. While researchers usually discuss open asset services in non-commercial contexts [56, 65], pro<sup>fi</sup>t-oriented companies may equally o<sup>f</sup>er such services [48]. Open asset services encourage a provider’s interaction with the external developer community [65]. This is because o<sup>f</sup>ering free access to company-internal assets, removing technological access barriers such as user authentication restrictions, and providing generative and easy-to-integrate IT resources lowers the adoption barriers for external developers [84]. Furthermore, the use of standardized interfaces and well-de<sup>fi</sup>ned governance approaches establishes trust between the API provider and external developers [35]. The Github API, for example, o<sup>f</sup>ers free programmatical access to the version control system’s functionalities such as forking projects, sending pull requests, and monitoring development [72].

## Theory Development

We adopt Gawer’s [36] organization-centric conceptualization of digital platforms as meta-organizations. This conceptualization emphasizes a technological platform’s capacity to host inter-organizational service ecosystems [79]. In such platform-based ecosystems, value-adding activities of resource integration are provided by multiple actors and customers [66]. We distinguish two mechanisms of value creation in digital platforms discussed by Gawer [36] that are rooted in cost reductions owing to the joint value creation of platform participants in comparison to creating value separately: economies of scope in production and in innovation. We propose that value creation mechanisms in digital platforms and API design are interlinked, that is, we assume that distinct API archetypes <sup>fi</sup>t di<sup>f</sup>erent value creation mechanisms and target varying objectives. We depict the research model in Figure 1.

## API Return on Investment, Di<sup>f</sup>usion, and Value Creation Mechanisms

API providers may follow two di<sup>f</sup>erent objectives by o<sup>f</sup>ering APIs that are related to two major types of business objectives, value generation, and value appropriation [69]. They may aim at achieving a positive ROI by creating revenue streams (relating to value appropriation) and at reaching a high API di<sup>f</sup>usion level, which may stimulate innovation (relating to value generation) [38, 86]. ROI is commonly used to assess a new product’s performance [50]. Return on API investment describes the ratio between net pro<sup>fi</sup>t and costs resulting from investing in API development and operations. Many APIs directly target a positive ROI by charging for API consumption [61, 76] or by generating indirect revenue streams through an increased attractiveness of a core product [47]. The di<sup>f</sup>usion of a service generally includes awareness and adoption among potential customers [88]. API awareness characterizes the extent to which external developers gain information about the API and its attributes. Adoption entails the usage of an API by third-party developers. API di<sup>f</sup>usion provides non-monetary bene<sup>fi</sup>ts to API providers [29] and enhances the provider’s internal innovation capacities [16].

According to the contingency perspective of organizational strategy, there is no universally superior strategy, irrespective of the environmental or organizational context [102]. Companies must, therefore, align their internally oriented resource development with their externally oriented strategy [40]. We follow this notion and argue that a provider’s internal design of boundary resources (speci<sup>fi</sup>cally API design) must match its externally oriented ecosystem positioning (speci<sup>fi</sup>cally the targeted mechanisms of interorganizational value creation) in order to achieve positive outcomes. Inter-organizational value creation in platform-based ecosystems has its roots in di<sup>f</sup>erent economies of scope [36], which we refer to as value creation mechanisms. In the following, we develop a <sup>fi</sup>t-asmoderation perspective by conceptualizing the match between internal resources and the externally oriented strategy in a moderation model [102]. The <sup>fi</sup>t-as-moderation approach suggests that the interaction between the predictor and the moderator “is the primary determinant of the criterion variable.“ [102, p. 424]. Speci<sup>fi</sup>cally, we propose that the interaction of an API’s similarity to archetypical API designs and the levels to which API providers target value creation mechanisms a<sup>f</sup>ects API ROI and di<sup>f</sup>usion. Table 3 provides an overview of the constructs and de<sup>fi</sup>nitions of our research model.

![](/api/attachments/NEWPV6BA/fulltext/images/a9ce00160fd55af57f6bf5a1ca415c2cdde85babe017d04a629f80e73c7f41ec.jpg)  
Research model.

## Economies of Scope in Production

Economies of scope in production is a phenomenon in which the joint production of a product is less costly than producing the intermediate and the end product separately [78]. If two successive value creation stages are interlinked, vertically integrating these stages may allow for jointly optimized production [21, 34].

Targeting economies of scope in production owing to vertical integration leverages an API’s ROI for the professional service archetype, because professional services aim at facilitating the integration of the service provider’s o<sup>f</sup>erings into the API developers’ applications [7, 106]. The modularization of IT infrastructure allows for reusing IT assets in a <sup>fl</sup>exible manner [70] in inter-organizational service relationships, which is particularly valuable for service customers with highly customized and complex application landscapes [106]. The use of standardized interfaces facilitates the service integration in the course of customer’s application development projects, because software developers require less e<sup>f</sup>ort to familiarize with the service’s functionality and syntax [63]. The professional service’s <sup>fl</sup>exibility and integrability ultimately increase the attractiveness of a service provider’s o<sup>f</sup>erings. By creating novel revenue streams via direct or indirect charging mechanisms, while requiring relatively low investments, professional services implement a value appropriation mechanism and thus directly contribute to an API’s ROI. An exemplary professional service is Salesforce’s Analytics API. Salesforce traditionally is a browser-based software-as-a-service provider for CRM solutions. Salesforce’s Analytics API allows programmatic access to analytics features such as datasets and dashboards [2]. This API o<sup>f</sup>ers easy integrability into customer application landscapes and clearly communicated service-level agreements. It is bound to a subscription of Salesforce’s cloud product.

Constructs and de<sup>fi</sup>nitions.

<table><tr><td colspan="2">Construct</td><td>Definition</td><td>Sources</td></tr><tr><td colspan="2">Return on investment</td><td>The API&#x27;s return on investment relative to the company&#x27;s original objectives for the API.</td><td>[18, 68]</td></tr><tr><td colspan="2">Diffusion</td><td>Level of API awareness and adoption among third-party developers.</td><td>[88]</td></tr><tr><td colspan="2">Target level of value creation mechanism</td><td>Level to which an API provider targets a mechanism of inter-organizational value creation in a platform-based ecosystem.</td><td>[36]</td></tr><tr><td rowspan="2">Target level of ...</td><td>... economies of scope in production</td><td>The joint production of successive value creation stages is less costly than producing separately if they are tightly interlinked.</td><td>[21, 78]</td></tr><tr><td>... economies of scope in innovation</td><td>Jointly innovating on two products is cheaper than independent innovations on these two products.</td><td>[14, 74]</td></tr><tr><td colspan="2">Similarity to API archetype</td><td>Three measures that represent the similarity to the “average representative” of the three archetypes of API design (professional service, mediation service, and open asset service)</td><td>[35, 74, 79]</td></tr></table>

Notes: API = Application Programming Interface

In contrast to open asset services, that are o<sup>f</sup>ered free-of-charge and focus on value generation by spurring innovation via di<sup>f</sup>usion in the open development community [48], professional services include charging mechanisms and do not target wide accessibility among the external developer community (i.e., API di<sup>f</sup>usion). From the aforementioned argumentation, we conclude that there is a <sup>fi</sup>t between an API’s similarity to the professional service archetype and the target level of economies of scope in production with respect to achieving API ROI.

Hypothesis 1: The interaction of an API’s similarity to the professional service archetype and the target level of economies of scope in production is positively related to API return on investment.

Targeting economies of scope in production owing to vertical integration may further leverage API ROI for the mediation service archetype because this archetype is geared towards facilitating the integration of business development and marketing resources into third-party developers’ applications [87]. Platform providers, by o<sup>f</sup>ering mediation services, aim to generate novel or increased revenue streams with relatively low additional investments and thus target an increased ROI [80]. Mediation services are frequently provided to third-party developers free-of -charge, but with the goal to generate end customer revenues [94]. Compared to alternative boundary resources (such as browser-based user interfaces) that platform providers frequently o<sup>f</sup>er [38], API-based mediation services allow easy integrability into third-party applications and thus increase a platform’s overall attractiveness to application developers. This, in combination with a platform’s value appropriation mechanisms, such as collecting end customer fees or charges for targeted advertising, results in an increased ROI. Dropbox, for example, o<sup>f</sup>ers the Dropbox API which exposes standardized <sup>fi</sup>le management capabilities to third parties. Service providers, such as streamboxr, integrate with Dropbox’s API and thus free end customers from having to conduct <sup>fi</sup>le integration manually [19]. Third-party developers contribute to improving Dropbox’s end customer-facing o<sup>f</sup>erings. Higher end customer revenues lead to an increased ROI of the Dropbox API [23]. Consequently, we conclude that there is a <sup>fi</sup>t between an API’s similarity to the mediation service archetype and the target level of economies of scope in production with respect to achieving API ROI.

Hypothesis 2: The interaction of an API’s similarity to the mediation service archetype and the target level of economies of scope in production is positively related to API return on investment.

## Economies of Scope in Innovation

Economies of scope in innovation occur when jointly innovating on two products is cheaper than developing independent innovations on these two products [36, 74]. Innovating <sup>fi</sup>rms share IT resources in the presence of innovational complementarities that emerge in business-to-business relationships when a <sup>fi</sup>rm’s innovation increases the productivity of customers’ research and development investments [14].

Targeting economies of scope in innovation leverages the di<sup>f</sup>usion of open asset services because open asset services are geared towards stimulating generativity by providing free-of-charge access to core platform modules [38]. Generativity refers to the “capacity to produce unprompted change driven by large, varied, and uncoordinated audiences” [111, p. 1980]. Modularity spurs third parties’ innovativeness through experimentation [38, 74, 93]. Providing open asset services attracts external innovators, because of the low <sup>fi</sup>nancial cost and developmental e<sup>f</sup>ort that innovators require to establish and maintain interoperability [56, 101]. The open asset service’s generativity and modularity ultimately lead to API di<sup>f</sup>usion. Open asset services, in contrast to professional services, do not target ROI, because they focus on exploring novel modes of value generation through involving third-party developers rather than on value appropriation [16]. The New York Times Article Search API, for example, allows free search of articles from 1981 to today and returns headlines, abstracts, lead paragraphs, links to associated multimedia, and other article metadata [98]. This API, by attracting large interest in the open development community, has led to the development of diverse mashups, which may also stimulate innovations in the New York Times’ o<sup>f</sup>erings. Hence, we conclude that there is a <sup>fi</sup>t between an API’s similarity to the open asset service archetype and the target level of economies of scope in innovation with respect to achieving API di<sup>f</sup>usion.

Hypothesis 3: The interaction of an API’s similarity to the open asset service archetype and the target level of economies of scope in innovation is positively related to API difusion.

Targeting economies of scope in innovation may leverage API di<sup>f</sup>usion for mediation services because these services are geared towards facilitating open access to resources that link external developers to the platform’s end customers [87]. Exposing platform resources through mediation services may trigger third-party developer innovations of end customer-facing services that go beyond the API provider’s scope of imagination [24, 79, 96]. Platform providers, by o<sup>f</sup>ering mediation services, leverage economies of scope in innovation to broaden the scope of functionality o<sup>f</sup>ered by the platform [39]. Mediation services, to incentivize API di<sup>f</sup>usion, may involve the distribution of end customer revenues among the platform and third-party developers via revenue sharing mechanisms [80]. Innovating novel value propositions is important for attracting user crowds independent of the simultaneous implementation of value appropriation mechanisms [16]. Platforms may even focus on di<sup>f</sup>usion prior to implementing value appropriation mechanisms in later stages, because appropriating value may con<sup>fl</sup>ict attracting platform users [52]. The YouTube Data API, for example, is a mediation service that allows content providers to freely upload, update, and delete videos on the end-customer-facing YouTube platform. With this API, YouTube focused on attracting a large mass of content providers in an initial stage of the YouTube platform’s lifecycle and added value capture mechanisms (such as targeted advertising) in a later stage [16]. Thus, we conclude that there is a <sup>fi</sup>t between an API’s similarity to the mediation service archetype and the target level of economies of scope in innovation with respect to achieving API di<sup>f</sup>usion.

Hypothesis 4: The interaction of an API’s similarity to the mediation service archetype and the target level of economies of scope in innovation is positively related to API difusion.

## Research Methodology and Estimation Approach

We triangulate quantitative and qualitative data collection and analysis methods in order to investigate the interrelated e<sup>f</sup>ects of API design and targeted economies of scope on API ROI and di<sup>f</sup>usion across professional, mediation, and open asset services. First, we surveyed product managers at API providers that are listed in the Internet’s most complete public API directory ProgrammableWeb [29, 85, 109] in order to collect data on the API providers’ targeted value creation mechanisms as well as on API ROI. Second, we collected secondary data regarding the actual di<sup>f</sup>usion of these APIs among developers. Third, we applied qualitative content analysis to the documentations of APIs on which we gathered survey and secondary data. This analysis allowed us to collect data on the speci<sup>fi</sup>c API designs that API providers have implemented. In terms of data analysis, we combine cluster and regression analyses. We <sup>fi</sup>rst apply cluster analysis to the data from our content analysis in order to verify our typology of theoretically derived API archetypes and to develop a more <sup>fi</sup>ne-grained understanding of their dominant design characteristics. Second, we investigate the di<sup>f</sup>erential e<sup>f</sup>ects of economies of scope in production and innovation on API di<sup>f</sup>usion and ROI for the three archetypes of API design by applying ordinal logistic and negative binomial regression.

## Data Sources and Variables

## Survey Research: Value Creation Mechanisms, API Return on Investment, and Controls

We conducted a cross-sectional survey to collect complete response data from 185 product managers who represent di<sup>f</sup>erent API providers. The survey was online from May to July 2017 and targeted API product managers at for-pro<sup>fi</sup>t API providers that were responsible for the design of the APIs, the strategies pursued with the APIs, and the overall API operations. We mailed the survey to 2950 organizations that were listed on ProgrammableWeb. The response rate of our survey was 6.17 percent, which is comparable to similar studies that use nonpersonalized mailings [91]. In order to motivate respondents to participate, we provided access to an API industry study that reported preliminary results of our project. We sent two reminder e-mails to improve response rates. We considered 152 responses from for-pro<sup>fi</sup>t API providers for our study. Even though we explicitly targeted for-pro<sup>fi</sup>t API providers, we could not verify pro<sup>fi</sup>t orientation for the other responses in our qualitative API analysis. In order to ensure relevance and generalizability of our results, we targeted a broad range of di<sup>f</sup>erent industries. The API providers mainly o<sup>f</sup>ered services in regard to IT & Communication (41 percent), Education & Science (14 percent), Marketing & Media (10 percent), Wholesale & Retail (7 percent), or Leisure (5 percent). Most API providers resided in the USA (38 percent), Germany (12 percent), UK (9 percent), Switzerland (7 percent), and France (5 percent).

We undertook various measures for mitigating the risk of common method variance that is related to our survey-based measurement of value creation mechanisms and API <sup>fi</sup>nancial performance [81]. We provided a cover story for our questionnaire to emphasize that the independent and dependent variables are unconnected. Second, we developed simple structured questions and avoided ambiguous terms. Finally, we explicitly pointed out in our cover story that all answers would be anonymous and we would not establish a connection between answers and individuals. We checked the extent of common method variance by inspecting the correlation matrix (see Supplemental Appendix D). Common method bias is re<sup>fl</sup>ected by extremely high correlations above 0.9 or below −0.9 . However, in our study, the highest correlations among our survey variables are −0.24 and 0.41. In sum, these procedural remedies and the results from our correlation analysis give no indication of potential threats resulting from common method bias. We also checked for non-response bias [4]. In addition, we checked for di<sup>f</sup>erences in industries or company sizes. We found no signi<sup>fi</sup>cant di<sup>f</sup>erences and our data does not indicate nonresponse bias. Supplemental Appendix B provides an overview of the survey instrument.

As our study focuses on the API-level, we asked the repondents to indicate the API which they referred to in the survey. This information was then used to collect qualitative and secondary data about the APIs.

API Return on Investment. Whereas on the <sup>fi</sup>rm-level, ROI measures are widely available, our unique focus on the API level inhibits using objective <sup>fi</sup>nancial performance measures. Thus, we followed a long history of measuring pro<sup>fi</sup>tability of new products in the new product development literature. Following Cooper [18] and McNally et al. [68], we used a single-item measure for API ROI that captures the degree to which an API’s ROI meets the <sup>fi</sup>nancial goals of the API provider. Such subjective measures of <sup>fi</sup>nancial performance allow for a relative comparison of API’s <sup>fi</sup>nancial performance [68], because they avoid problems in comparing actual values for di<sup>f</sup>erent projects and products [17] and allow to account for the API provider’s speci<sup>fi</sup>c organizational goals that are associated with the APIs [5]. Furthermore, such relative measures help to capture the peculiarities of di<sup>f</sup>erent industries API providers operate in. Finally, subjective measures have been found to produce equally valid performance measurements in a variety of contexts when being compared against objective ones [26, 104].

According to Bergkvist and Rossiter [10], single-item measurements have similar validity as multi-item scales when the construct being measured is doubly concrete in the mind of the respondent. This means that both the object of the study (i.e., the respondent’s API provider) as well as its attribute (i.e., its <sup>fi</sup>nancial performance) are concrete such that they can be easily and uniformly imagined [83]. By contrast, constructs consisting of formed or abstract objects (e.g., all API providers in a given industry) and attributes (e.g., service quality or market orientation) would require a multi-item measurement. As our measure of API ROI re<sup>fl</sup>ects an overall assessment of <sup>fi</sup>nancial performance, it can be considered as being concrete [83]. The same is true for the respondents’ API provider. Thus, we consider our subjective single-item measure as being valid for our purpose.

Value Creation Mechanisms. Owing to the lack of survey-based measurements of Gawer’s [36] platform value creation mechanisms, we introduce self-developed measurements that capture the extends to which economies of scale in production and innovation describe a company’s API strategy. The measure for economies of scope in production comprises three <sup>fi</sup>ve-level Likert items that characterize the level to which an API facilitates the <sup>fl</sup>exible integration, adaptation, and deep integration of IT resources. The items are inspired by D’Aveni and Ravenscraft [21], Garcia et al. [34], and Gawer [36]. The instrument for economies of scope in innovation consists of three items that describe the extent to which APIs allow to tap the inventive capacities of the external developer community, to exploit the creative potential of external developers, and to enhance an API provider’s innovation capabilities. This instrument is informed by Bresnahan and Trajtenberg [14], Gawer [36], and Nambisan and Sawhney [74].

Controls. We included two API-level controls. We proxied the API’s quality of implementation by capturing the functional quality and service innovativeness of the API. Functional quality captures the degree to which an API o<sup>f</sup>ers unique features compared to, is clearly superior to, and is of higher quality than competing APIs [97]. Service innovativeness captures the degree to which an API is innovative in the speci<sup>fi</sup>c industry of the API provider [30]. The API provider-level control number of employees accounts for organizations of di<sup>f</sup>erent size, as an API might be more central for the overall business model of smaller organizations than larger organizations. We further included two respondent-level controls. The respondent’s years with the API provider and afiliation may potentially bias response behavior [81].

## Content Analysis and Cluster Analysis: Similarity to API Design Archetypes

Following a <sup>fi</sup>t-as-moderation perspective, we propose that APIs with di<sup>f</sup>erent design traits require distinct value creation strategies. While we collected data on value creation strategies by applying survey research, we followed a di<sup>f</sup>erent approach for investigating API design. First, we applied content analysis to the API websites and related information in order to collect data on API’s speci<sup>fi</sup>c design characteristics. Then, we applied cluster analysis to this data in order to reveal API design archetypes and verify the three theoretically derived API designs — professional, open asset, and mediation services. Finally, we measured the degree to which each API’s design followed these archetypes by measuring their similarity to these design archetypes.

API Designs Characteristics. In order to collect data on the speci<sup>fi</sup>c API designs, we applied content analysis to the corresponding API websites, the APIs’ technical documentation, as well as their terms of use. Based on the nine API design characteristics in Table 1, we developed a coding scheme that comprised de<sup>fi</sup>nitions of the API design characteristics, respective binary indicators (for existence and non-existence of an API characteristic), and coding examples. Using this coding scheme, we content analyzed all 152 APIs for which respondents returned a complete questionnaire. In order to ensure the reliability, two independent researchers coded all APIs. Using a coding template, the researchers had to provide evidence for why they have coded an API design characteristic in a certain way. The two researchers reached a Cohen’s Kappa of 0.82, which indicates excellent agreement [57]. Based on the coding templates, the coders discussed and resolved coding di<sup>f</sup>erences resulting in nine dichotomous variables per API. These variables indicate whether a certain API design characteristic has been implemented by an API provider or not (0 = no implementation, 1 = implementation).

API Design Archetypes. We identify archetypes of API design as cluster centroids by applying cluster analysis to the nine dichotomous API design characteristics. Cluster analysis groups entities such that the in-group variation is small in relation to intergroup variation [67]. By de<sup>fi</sup>ning distinctive variables (i.e., API design characteristics), cluster analysis groups entities (i.e., APIs) according to their reciprocal similarities describing natural groups [62]. In order to avoid idiosyncratic errors speci<sup>fi</sup>c to a certain clustering technique, we used di<sup>f</sup>erent cluster algorithms applying distinct distance metrics. As the primary goal of the cluster analysis was to identify archetypes of API design, we used four di<sup>f</sup>erent partitioning clustering approaches that create cluster centroids (i.e., average representatives for each cluster) that we conceptualize as archetypes. We used Spherical K-Means using Cosine distance [49], a numeric optimization approach using Jaccard distance [62], as well as K-Medians [62] and Partitioning Around Medoids [82] using Hamming distance. The idea of such algorithms is to randomly assign entities to a pre-de<sup>fi</sup>ned number of clusters (k) and then reassign entities iteratively to the centroids of these clusters. All these clustering approaches and distance measures are apt for dichotomous data. Determining an appropriate number of clusters, we used the Dunn-Index and Average Silhouette Values that measure the compactness of clusters while also taking into account their separation.

Similarity to API Design Archetypes. Finally, we measured the similarity of each API to the identi<sup>fi</sup>ed cluster centroids (i.e., API archetypes) for each clustering algorithm: (1) We determined the archetypical design for each cluster (i.e., the average representative). (2) We calculated the distance between each API and these archetypical implementations using the distance measures that were used for the clustering (e.g., for the Spherical K-Means clustering using Cosine distance, we used Cosine distance). (3) We transformed the obtained distance measures to similarity measures in order to increase the interpretability of our results. We scaled each distance measure by dividing it by its maximum value so that it ranges between 0 and 1. Then, we subtracted these scaled distance measures from 1.

## Secondary Data: API Di<sup>f</sup>usion

We follow Setia et al. [88] who conceptualize di<sup>f</sup>usion of open source software as awareness and adoption among developers. We collected data on API di<sup>f</sup>usion in three major developer communities: Github, Stack Overflow, and ProgrammableWeb. For adoption, we collected the number of publicly available software repositories that use the API and that were uploaded by third-party developers on Github. For measuring awareness, we retrieved the number of API-related comments within Stack Over<sup>fl</sup>ow as well as the number of followers of a given API on ProgrammableWeb. All these data were retrieved using the search mechanism provided by these communities using the API title and “API” as search terms (e.g., “clickmeter API”) in December 2018. These measures provide an objective measure of API di<sup>f</sup>usion and are apt for dealing with APIs in commercial and non-commercial settings.

## Results

## Construct Validation

In order to con<sup>fi</sup>rm validity and reliability of our survey-based measures, we applied exploratory and con<sup>fi</sup>rmatory factor analysis. The Measure of Sampling Adequacy was 0.75, indicating good applicability of exploratory factor analysis. We used the latent root criterion (Eigenvalues >1) for extracting <sup>fi</sup>ve factors that could be clearly interpreted. Alphas of at least 0.79 suggest good reliability of factors. Composite Reliabilities (CR) exceeded values of 0.5 and the Average Variance Explained (AVE) for each factor surpassed 0.5. Thus, convergent validity could be assumed [6]. The discriminant validity was checked by using the Fornell-Larcker criterion, which claims that a factor’s AVE should be higher than its squared correlation with every other factor [32]. Thus, discriminant validity could be assumed. Construct validation results are shown in Supplemental Appendix C.

Our three items measuring API di<sup>f</sup>usion represent count data. Standard techniques to factor analysis do not deal well with the discrete, non-negative nature of count data and might lead to biased results [105]. In order to extract an overarching API di<sup>f</sup>usion measure, we applied non-negative matrix factorization to our three API di<sup>f</sup>usion items. Non-negative matrix factorization is frequently applied to extract latent factors from count data [59, 89]. We followed Brunet et al. [15] and extracted one latent API di<sup>f</sup>usion factor that accounted for 62.7 percent of the three original item’s variances. We successfully validated the appropriateness of extracting a single API di<sup>f</sup>usion factor following the ideas of Frigyesi and Höglund [33].<sup>1</sup> We made sure that our results are robust regarding other approaches to non-negative matrix factorization algorithms. Supplemental Appendix D depicts means, standard deviations, minimum, and maximum values, as well as correlations of our variables. In all subsequent analyses, we used obtained factor scores as well as z-standardized scores.

## Validation of API Archetypes

Average Silhouette Values and Davies-Bouldin-Indices indicate a robust three cluster solution (see Supplemental Appendices E and F). Supplemental Appendix G exhibits that all clustering approaches produce similar results, that is, there is an average agreement of 92.3 percent between the di<sup>f</sup>erent clusterings. This agreement is backed by a contingency analysis. All $\chi ^ { 2 }$ tests are statistically signi<sup>fi</sup>cant $\left( \mathtt { p } < 0 . 0 1 \right)$ and an average Cramer V of 0.87 indicates a very high correlation between the nominal clusterings. We report results for the Spherical K-Means clustering using Cosine distance only. Based on our theoretical considerations, the implementation of API design characteristics re<sup>fl</sup>ects a conscious design decision of an API provider. Following this line of reasoning, Cosine distance is an asymmetrical distance measure and, thus, takes into account such conscious design decisions only [31]. By contrast, other applicable distance measures also take into account non-implemented API design characteristics for which we cannot infer conscious design. After validating the cluster structure, we report frequency distributions to characterize the API clusters (see Table 4). We calculate Cramer Vs to test whether or not the API design characteristics signi<sup>fi</sup>cantly di<sup>f</sup>er across the three clusters. We analyze global di<sup>f</sup>erences across all clusters and apply posthoc tests, comparing single clusters. In order to ensure that the analysis represents a realistic picture of API design characteristics, the assignment of APIs was manually veri<sup>fi</sup>ed for plausibility. We report cluster centroids (i.e., the API characteristics’ values for the three archetypes) and archetypical examples in Table 5.

Professional Services. APIs in the professional services cluster are characterized by a high probability of o<sup>f</sup>ering sophisticated information processing functionalities that go beyond the simple provision of data and for which API providers request transaction- and subscription-based charges. User authorization and security measures are also quite strongly associated with this cluster. This cluster can be well matched to the group of professional services [7, 61, 106]. Choosing the professional service archetype, API providers create an API that enables their clients to integrate the functionality of the API provider’s o<sup>f</sup>erings directly into the client’s existing information systems and the evolving business operations. These APIs are frequently built to leverage an already existing service or product of the API provider for which the API usually represents an alternative access channel. With a share of 67 percent, the professional service cluster is the biggest API cluster. As an archetypical example, Salesforce’s Analytics API o<sup>f</sup>ers programmatic access to analytics features [2].

Implementation of API design characteristics by API cluster as percentage.

<table><tr><td>API Design Characteristic</td><td>Professional Services (1)</td><td>Mediation Services (2)</td><td>Open Asset Services (3)</td><td>Cramer&#x27;s V</td><td>Group Comparisons</td></tr><tr><td>End Customer Access</td><td>0</td><td>66.67</td><td>4.35</td><td>0.76**</td><td>3-2**, 1-2**, 3-1</td></tr><tr><td>Multi-Channel Access</td><td>72.55</td><td>59.26</td><td>100</td><td>0.27**</td><td>3-2**, 1-2, 3-1**</td></tr><tr><td>End Customer Relationship</td><td>0.98</td><td>66.67</td><td>0</td><td>0.76**</td><td>3-2**, 1-2**, 3-1</td></tr><tr><td>Function</td><td>92.16</td><td>88.89</td><td>0</td><td>0.79**</td><td>3-2**, 1-2, 3-1**</td></tr><tr><td>Subscription-based Charge</td><td>97.06</td><td>11.11</td><td>0</td><td>0.91**</td><td>3-2, 1-2**, 3-1**</td></tr><tr><td>Transaction-based Charge</td><td>96.08</td><td>7.41</td><td>4.35</td><td>0.9**</td><td>3-2, 1-2**, 3-1**</td></tr><tr><td>User Authorization</td><td>98.04</td><td>100</td><td>65.22</td><td>0.48**</td><td>3-2**, 1-2, 3-1**</td></tr><tr><td>Security</td><td>68.63</td><td>74.07</td><td>21.74</td><td>0.36**</td><td>3-2**, 1-2, 3-1**</td></tr><tr><td>Revenue.sharing</td><td>0</td><td>18.52</td><td>0</td><td>0.4</td><td>3-2, 1-2**, 3-1</td></tr><tr><td>N (percent)</td><td>67.10</td><td>17.76</td><td>15.13</td><td></td><td></td></tr></table>

Notes: \*\*p < 0.01, \* < 0.05; API= Application Programming Interface

API archetypes and archetypical examples.

<table><tr><td rowspan="2">API Design Characteristic</td><td colspan="2">Professional Service</td><td colspan="2">Mediation Service</td><td colspan="2">Open Asset Service</td></tr><tr><td>A</td><td>Salesforce Analytics [2]</td><td>A</td><td>Dropbox [23]</td><td>A</td><td>New York Times Search [98]</td></tr><tr><td>Function</td><td>1</td><td>1: analytics functionality</td><td>1</td><td>1: file synchronization and storage functionality</td><td>0</td><td>0: retrieval of article data only</td></tr><tr><td>End customer access</td><td>0</td><td>0: no marketing of third-party apps to end customers</td><td>1</td><td>1: marketing for apps that integrate with Dropbox API</td><td>0</td><td>0: no marketing of third-party apps to end customers</td></tr><tr><td>Multi-channel access</td><td>1</td><td>1: alternative browser interface</td><td>1</td><td>1: browser-based access and desktop integration</td><td>1</td><td>1: browser-based access to articles</td></tr><tr><td>Security</td><td>1</td><td>1: HTTPS encryption</td><td>1</td><td>1: HTTPS encryption</td><td>0</td><td> $1^i$ : HTTPS encryption</td></tr><tr><td>End customer relationship</td><td>0</td><td>0: salesforce has no end customer relationship</td><td>1</td><td>1: third-party app customers require a salesforce subscription</td><td>0</td><td>0: third-party app customers don&#x27;t require NYT subscription</td></tr><tr><td>User authorization</td><td>1</td><td>1: authentication model (API Key, OAuth 2)</td><td>1</td><td>1: OAuth authentication</td><td>1</td><td>1: developer key required</td></tr><tr><td>Subscription-based charging</td><td>1</td><td>1: requires paid salesforce subscription</td><td>0</td><td>0: API use does not require a dropbox subscription</td><td>0</td><td>0: no charging</td></tr><tr><td>Transaction-based charging</td><td>1</td><td> $0^i$ : no charges per API call</td><td>0</td><td>0: no charges per API call</td><td>0</td><td>0: no charging</td></tr><tr><td>Revenue sharing</td><td>0</td><td>0: salesforce does not share revenues</td><td>0</td><td>0: dropbox does not share end customer revenues with app developers</td><td>0</td><td>0: NYT does not share end customer revenues with app developers</td></tr></table>

Notes: API = Application Programming Interface; A =Archetype; 1 = Implementation; 0 = No Implementation; i = Nonconformance with archetype

Mediation Services. APIs in the second cluster are characterized by providing developers access to end customers; the provider of a mediation service, however, entertains its own direct relationship with these end customers. APIs in this cluster most frequently engage in revenue sharing approaches and make strong use of user authorization. As for professional services, API providers o<sup>f</sup>er a broad range of functionalities that go beyond infrastructure and data access. Given these characteristics, this cluster matches well with the mediation service [75, 79, 94]. Based on extant information processing functionalities that mediation services provide, API developers can develop new service o<sup>f</sup>erings for the API providers’ end customers. This API cluster accounts for 18 percent in our sample. The Dropbox API, as an archetypical mediation service, allows app developers programmatic access to <sup>fi</sup>le synchronization and storage functionalities [23]. Dropbox provides marketing for apps that integrate with the Dropbox API on its website and requires app customers to have their own Dropbox subscription.

Open Asset Services. APIs in the third cluster are characterized by providing multichannel access to IT infrastructure or data resources, that is, the API re<sup>fl</sup>ects an alternative access option. API providers apply neither transaction-, nor subscription-based charges. Also, they o<sup>f</sup>er no revenue sharing options. Further, they show the lowest usage of user authorization and security options. Given these traits, APIs in this archetype match well open asset services[48, 56, 64, 84]. With low access barriers and their high versatility, such APIs are intended to involve the general public in approaches to open innovation. This API cluster accounts for 15 percent of all surveyed API providers. The New York Times Article Search API is an archetypical open asset service that o<sup>f</sup>ers free access to article data and metadata that is also available via the New York Times website [98].

## Hypothesis Test

In order to test our hypothesis, we again present results that are based on the Spherical K-Means clustering only. However, results are very consistent between the di<sup>f</sup>erent clustering approaches. API ROI re<sup>fl</sup>ects a single item that has been measured with a <sup>fi</sup>vepoint Likert scale. Thus, API ROI can be best described as being of ordinal nature such that ordinal logistic regression is an appropriate modeling choice [13, 43, 45]. Similarly, we apply negative binomial regression in order to account for the fact that the API di<sup>f</sup>usion measure relies on count data.

We <sup>fi</sup>rst test our API ROI hypotheses (Hypothesis 1 and Hypothesis 2). Ordinal logistic regression is a generalization of binary logistic regression and can accommodate dependent variables that consist of more than two ordinal levels by applying a cumulative logit model. A central pre-requisite of ordinal logistic regression is the proportional odds (also known as parallel regression) assumption that claims that the relationship between each pair of outcome categories of the dependent variable is the same [43]. We applied Brant’s [13] test in order to test this assumption. We yielded non-signi<sup>fi</sup>cant test statistics indicating that proportional odds can be assumed. We estimated the following regression:

Model 1: $\begin{array} { r } { \operatorname* { P r } ( A P I R O I \geq j | X ) = \frac { 1 } { 1 + \exp [ - \alpha j + X \beta ] } } \end{array}$ with

$X \beta = \alpha + \beta _ { 1 }$ Economies of Scope in Production $+ \beta _ { 2 }$ Similarity Mediation Archetype

<sub>þ</sub> β Similarity Professional Service Archetype

<sub>þ</sub> β Economies of Scope in Production x Similarity Mediation Archetype

þ $\beta _ { 5 }$ Economies of Scope in Production x Similarity Professional Service Archetype

$+ \beta _ { 6 } F u n c t i o n a l \ Q u a l i t y \ + \beta _ { 7 }$ Service Innovativeness $+ \beta _ { 8 }$ Employees API Provider

<sub>þ</sub> β Respondent Management Level $+ \beta _ { 1 0 }$ Respondent Years with API Provider

API ROI re<sup>fl</sup>ects the level of <sup>fi</sup>nancial goal attainment (1 = API ROI goals are not met at all; 5 = API ROI goals are completely met), X the vector of predictor variables, β the vector of estimated coe<sup>fi</sup>cients, α the intercepts, and j the number of ordinal response levels for API ROI. Consequently, $\operatorname* { P r } ( \mathrm { A P I } \ \mathrm { R O I } \geq \mathrm { j } \mid \mathrm { X } )$ is the probability that API ROI is higher or equal to the API ROI level j, conditional on the predictors X. We test model 1 in a stepwise fashion. We <sup>fi</sup>rst test for direct main e<sup>f</sup>ects excluding the interaction terms (model 1a). Then, we included the moderation e<sup>f</sup>ects in order to test our hypotheses (model 1b). Table 6 shows the results of the ordinal logistic regressions. Model 1a indicates that we cannot detect any signi<sup>fi</sup>cant main e<sup>f</sup>ect of economies of scope in production and the variables measuring the similarity to the design archetypes of professional/mediation services. Model 1b reveals positive interaction e<sup>f</sup>ects for economies of scope production and similarity to the professional service archetype $( \beta = 0 . 4 6 , \mathtt { p } \le 0 . 0 1 )$ as well as to the mediation archetype $( \beta = 0 . 3 9 , \mathrm { p } \le 0 . 0 5 )$

A likelihood ratio test reveals that $\mathrm { R } ^ { 2 }$ increases signi<sup>fi</sup>cantly $( \mathtt { p } \le 0 . 0 1 )$ from 0.25 to 0.30 when comparing the models with (model 1b) and without moderation e<sup>f</sup>ects (model 1a). The log odds (exponentiated beta coe<sup>fi</sup>cients) for both interaction e<sup>f</sup>ects are > 1, that is, indicating that API providers following a mediation or professional service design and targeting economies of scope in production have a higher API ROI than others. In order to better understand the results of these interaction e<sup>f</sup>ects, we evaluate how the predicted probabilities of the di<sup>f</sup>erent levels of API ROI change with varying degrees of similarity to

Ordinal logistic regression results.

<table><tr><td rowspan="2">Hypo-thesis</td><td rowspan="2">Variables</td><td colspan="2">Model 1a API ROI(main effects)</td><td colspan="2">Model 1b API ROI(full model)</td></tr><tr><td>Coefficients</td><td>Exp(β)(Odd Ratio)</td><td>Coefficients</td><td>Exp(β)(Odd Ratio)</td></tr><tr><td rowspan="4">H1</td><td>Economies of scope in production</td><td>0.20 (0.19)</td><td>1.23</td><td>0.23 (0.2)</td><td>1.26</td></tr><tr><td>Similarity professional service archetype</td><td>0.12 (0.16)</td><td>1.13</td><td>0.16 (0.17)</td><td>1.17</td></tr><tr><td>Similarity mediation archetype</td><td>-0.16 (0.16)</td><td>0.85</td><td>-0.23 (0.17)</td><td>0.79</td></tr><tr><td>Economies of scope in production * similarity professional service archetype</td><td></td><td></td><td>0.45** (0.18)</td><td>1.57</td></tr><tr><td rowspan="8">H2</td><td>Economies of scope in production * similarity mediation archetype</td><td></td><td></td><td>0.37* (0.18)</td><td>1.45</td></tr><tr><td>Functional quality</td><td>1.15** (0.23)</td><td>3.14</td><td>1.17** (0.24)</td><td>3.22</td></tr><tr><td>Service innovativeness</td><td>-0.08* (0.00)</td><td>0.66</td><td>-0.37 (0.20)</td><td>0.69</td></tr><tr><td>Employees API provider</td><td>-0.06 (0.13)</td><td>0.95</td><td>-0.07 (0.14)</td><td>0.93</td></tr><tr><td>Respondent API Affiliation</td><td>0.72 (0.47)</td><td>2.06</td><td>0.71 (0.48)</td><td>2.04</td></tr><tr><td>Respondent years API provider</td><td>0.01 (0.16)</td><td>1.01</td><td>-0.03 (0.16)</td><td>0.97</td></tr><tr><td>R2</td><td colspan="2">0.26</td><td colspan="2">0.30</td></tr><tr><td>Δ R2</td><td colspan="2"></td><td colspan="2">0.04*</td></tr></table>

Notes: \*\*p < 0.01, \* < 0.05; API = Application Programming Interface; ROI = Return on Investment; N = 152

Predicted probabilities for ordinal logistic regression.

<table><tr><td rowspan="2">Similarity to Design Archetype and Level of targeted economies of scope on production</td><td colspan="4">Cumulative Probability for Minimum Level of Goal Attainment for API ROI</td></tr><tr><td>Low</td><td>Moderate</td><td>High</td><td>Very high</td></tr><tr><td>High Similarity to Professional Service &amp; High levels of economies of scope in production</td><td>0.99</td><td>0.93</td><td>0.68</td><td>0.33</td></tr><tr><td>High Similarity to Professional Service &amp; Low levels of economies of scope in production</td><td>0.95</td><td>0.78</td><td>0.36</td><td>0.11</td></tr><tr><td>Low Similarity to Professional Service &amp; High levels of economies of scope in production</td><td>0.95</td><td>0.8</td><td>0.39</td><td>0.13</td></tr><tr><td>High Similarity to Mediation Service &amp; High levels of economies of scope in production</td><td>0.98</td><td>0.89</td><td>0.57</td><td>0.24</td></tr><tr><td>High Similarity to Mediation Service &amp; Low levels of economies of scope in production</td><td>0.93</td><td>0.72</td><td>0.29</td><td>0.08</td></tr><tr><td>Low Similarity to Mediation Service &amp; High levels of economies of scope in production</td><td>0.97</td><td>0.86</td><td>0.5</td><td>0.19</td></tr></table>

Notes: API = Application Programming Interface; ROI = Return on Investment

Negative binomial regression results.

<table><tr><td rowspan="2">Hypo-thesis</td><td rowspan="2">Variables</td><td colspan="2">Model 2a API Diffusion (main effects)</td><td colspan="2">Model 2b API Diffusion (full model)</td></tr><tr><td>Coefficients</td><td>Exp(β)</td><td>Coefficients</td><td>Exp(β)</td></tr><tr><td rowspan="4">H3</td><td>Economies of scope in innovation</td><td>-0.34 (0.26)</td><td>0.71</td><td>-0.32 (0.22)</td><td>0.72</td></tr><tr><td>Similarity to mediation archetype</td><td>-0.08 (0.23)</td><td>0.92</td><td>0.00 (0.19)</td><td>1.00</td></tr><tr><td>Similarity to open asset archetype</td><td>-0.22 (0.22)</td><td>0.80</td><td>-0.24 (0.19)</td><td>0.79</td></tr><tr><td>Economies of scope in innovation* similarity to open asset archetype</td><td></td><td></td><td>0.45* (0.22)</td><td>1.57</td></tr><tr><td rowspan="8">H4</td><td>Economies of scope in innovation* similarity to mediation archetype</td><td></td><td></td><td>0.07 (0.2)</td><td>1.08</td></tr><tr><td>Functional quality</td><td>0.29 (0.28)</td><td>1.33</td><td>0.29 (0.24)</td><td>1.33</td></tr><tr><td>Service innovativeness</td><td>0.01 (0.29)</td><td>1.01</td><td>-0.02 (0.24)</td><td>0.98</td></tr><tr><td>Employees API provider</td><td>0.35 (0.21)</td><td>1.42</td><td>0.36* (0.18)</td><td>1.43</td></tr><tr><td>Respondent API Affiliation</td><td>-1.19 (0.65)</td><td>0.30</td><td>-1.14 (0.63)</td><td>0.32</td></tr><tr><td>Respondent years API provider</td><td>-0.11 (0.22)</td><td>0.90</td><td>-0.07 (0.19)</td><td>0.94</td></tr><tr><td>R2</td><td colspan="2">0.25</td><td colspan="2">0.30</td></tr><tr><td>Δ R2</td><td colspan="2"></td><td colspan="2">0.05**</td></tr></table>

Notes: \*\*p < 0.01, \* < 0.05; API = Application Programming Interface; N = 152; Reported are standardized beta values; Standard errors in parentheses

the API design archetypes and economies of scope in production. Table 7 shows that API providers that simultaneously target economies of scope in production and follow a professional service or a mediation service design have higher probabilities of reaching high to very high levels of attaining their API ROI goals. For instance, API providers that follow professional service design and have reported high levels of economies of scope in production have a 68 percent chance of reaching high to very high level of goal attainment. By contrast, API providers that follow a professional service design without explicitly targeting economies of scope in production or vice versa have lower probabilities of reaching the same levels of goal attainment (36 percent and 39 percent). Thus, we <sup>fi</sup>nd support for our hypotheses 1 and 2.<sup>2</sup>

Testing our API di<sup>f</sup>usion hypotheses, we <sup>fi</sup>rst applied a chi-square test for dispersion and found our data to be overdispersed with $\mathrm { ~ p ~ } < 0 . 0 1$ [45]. We believe that this overdispersion (conditional variance of API di<sup>f</sup>usion is greater than its conditional mean) is caused by a distribution that is found in many online-contexts. Most APIs have a low to moderate di<sup>f</sup>usion and a handful of APIs show very high di<sup>f</sup>usion. In order to deal with this overdispersion, we tested a variety of alternatives including quasi-poisson, negative binomial, or zero-in<sup>fl</sup>ated regression models [45, 106]. However, likelihood ratio and deviance tests revealed that negative binomial regression best represents our data such that we have chosen this approach. Negative binomial regression models are based on logtransforming the conditional expectation of the dependent variable [97] (i.e., API di<sup>f</sup>usion). In greater detail, we have tested the following regression:

Model 2: log<sub>ð</sub>E<sub>ð</sub>API diffusion <sub>j</sub> X<sub>ÞÞ</sub>

$\mathit { \Theta } = \alpha \ + \ \beta _ { 1 }$ Economies of Scope in Innovation $+ \beta _ { 2 }$ Similarity Open Asset Archetype

十 $\beta _ { 3 }$ Similarity Mediation Archetype

$\beta _ { 4 }$ Economies of Scope in Innovation x Similarity Open Asset Archetype

þ $\beta _ { 5 }$ Economies of Scope in Innovation x Similarity Mediation Archetype

þ $\beta _ { 6 }$ Functional Quality <sub>þ</sub> β Service Innovativeness $+ \ \beta _ { 8 }$ Employees API Provider

十 $\beta _ { 9 }$ Respondent Management Level $+ ~ \beta _ { 1 0 }$ Respondent Years with API Provider r

API di<sup>f</sup>usion refers to the value of API di<sup>f</sup>usions and X to the vector of predictor variables. Thus, E(API di<sup>f</sup>usion | X) re<sup>fl</sup>ects the expected value of API di<sup>f</sup>usion given the predictor variables in the model [95]. Again, we test this equation in a stepwise fashion in order to disentangle main and interaction e<sup>f</sup>ects. Table 8 shows the negative binomial regression results. In model 2a, we <sup>fi</sup>nd no main e<sup>f</sup>ects of our API design measures and the targeted level of economies of scope in innovation. Model 2b shows that the interaction between economies of scope in innovation and similarity to the open asset archetype is signi<sup>fi</sup>cant $( \beta = 0 . 4 5 , \mathrm { p } < 0 . 0 5 )$ This interaction e<sup>f</sup>ect signi<sup>fi</sup>cantly increases $\mathrm { R } ^ { 2 }$ from 0.25 (model 2a) to 0.3 (model 2b) with $\mathtt { p < }$ 0.01. These results indicate that neither increasing the similarity to the open asset archetype nor following an economies of scope in innovation strategy is associated with a signi<sup>fi</sup>cant increase in API di<sup>f</sup>usion in isolation. The exponentiated beta coe<sup>fi</sup>cient for designing APIs according to the open asset archetype is 1, that is, striving towards open asset design alone has no positive or negative e<sup>f</sup>ect on API di<sup>f</sup>usion. By contrast, the exponentiated beta coe<sup>fi</sup>cient for the interaction term of similarity to the open asset design and economies of scope in innovation strategy is 1.57. This means that API providers that embark on economies of scope in innovation in conjecture with an open asset design increase the di<sup>f</sup>usion of their API by 57 percent when being compared to API providers that follow an open asset design only. We <sup>fi</sup>nd no support for the interaction between economies of scope in innovation and the similarity to the mediation archetype. Thus, we can support Hypothesis 3, while we have to reject Hypothesis $4 . ^ { 3 }$

Finally, we probe our moderation analyses through visual representations (Figure 2, 3, and 4). These plots support our <sup>fi</sup>t as moderation perspective showing that an alignment between API design archetypes and targeted economies of scope leads to superior API ROI and di<sup>f</sup>usion.

## Discussion

Our analysis of how a provider’s choice of API archetype interacts with its targeting of platform-based value creation mechanisms in in<sup>fl</sup>uencing API ROI and di<sup>f</sup>usion provides support for the theoretically derived hypothesis that the interaction of targeting economies

Marginal Means for Economies of Scope in Production and Similarity to Mediation Archetype Interaction  
![](/api/attachments/NEWPV6BA/fulltext/images/41067ce1d3774c06c6ea0f8a93b012ce157ba46738ac229e0eae74e4eb129a82.jpg)  
Economies of Scope in Innovation – Low – Moderate – High  
Interaction between economies of scope in production and similarity to professional services.

Marginal Means for Economies of Scope in Production and Similarity to Mediation Archetype Interaction  
![](/api/attachments/NEWPV6BA/fulltext/images/a8886cb575bd4b5da1e25a3e7f2f0bc11681bf32baefaac7d3edbe7218587de7.jpg)  
Economies of Scope in Innovation - Low - Moderate - High  
Interaction between economies of scope in production and similarity to mediation services.

Marginal Means for Economies of Scope in Innovation and Similarity to Open Asset Archetype Interaction  
![](/api/attachments/NEWPV6BA/fulltext/images/7f9fa1ccf0c8de21453e158d52cf917ab9b413b7bb7c626b099cb9701437fd70.jpg)  
Economies of Scope in Innovation – Low–Moderate - High

Interaction between economies of scope in innovation and similarity toopen asset.

of scope in production and an API’s similarity to the professional service archetype is positively related to API ROI (Hypothesis 1). Second, our results support our theoretical argumentation that the interaction of targeting economies of scope in production and an API’s similarity to the mediation archetype is also positively related to API ROI (Hypothesis 2). Third, our analysis shows that the interaction of targeting economies of scope in innovation and an API’s similarity to the open asset service archetype is positively related to API di<sup>f</sup>usion (Hypothesis 3). Our results do not provide support for the fourth hypothesis that the interaction of targeting economies of scope in innovation and an API’s similarity to the mediation service archetype is positively related to API di<sup>f</sup>usion (Hypothesis 4). A strategy that targets economies of innovation, thus, does not su<sup>fi</sup>ce for achieving high di<sup>f</sup>usion with APIs that are similar to the mediation service archetype.

This <sup>fi</sup>nding conforms with prior literature, which suggests that di<sup>f</sup>usion of mediation services requires careful coordination of cross-platform externalities and the execution of platform ignition strategies [28]. External developers will only become aware of and adopt a mediation service if it provides access to enough customers that external developers target [94], if there is complementarity between the API provider’s and the developer’s capabilities [52], and if there is an adequate level of platform governance [99].

## Theoretical Contributions

We provide three contributions to the literature on digital platforms. First, we develop a unifying theory that consolidates di<sup>f</sup>erent theoretical perspectives on API design and strategy. Prior literature on API design is scattered and discusses selective aspects of API design in disparate contexts. Some authors study APIs that provide marketing and distribution capabilities to third-party developers on two-sided platforms [e.g., 79]. This stream of literature focusses on an API’s ability to provide end customer access and to spur novel end-customer-facing value propositions from third parties. It produces theories with limited transferability to APIs on one-sided platforms that primarily focus on value appropriation. A second group of authors studies APIs that provide open data services [e.g., 56]. It focusses on an API’s ability to expose assets to external developers free of charge in order to achieve high API di<sup>f</sup>usion. The research results are not applicable to fee-based APIs that do not target API di<sup>f</sup>usion but API ROI. A third group of authors considers APIs as distribution channels for cloud-based professional services [e.g., 7]. This perspective focusses on fee-based o<sup>f</sup>erings to API developers and excludes indirect value appropriation mechanisms on two-sided markets. Considering that APIs represent key strategic resources of platform providers that determine a platform’s prosperity [9], a generalizable theory on API design is required [108] that integrates the disparate perspectives on API design and explains the strategic impact of design choices across these isolated contexts. Our unifying perspective on API design that is grounded in contemporary literature on platform architecture and governance [99, 100] synthesizes prior API literature. We di<sup>f</sup>erentiate between three API archetypes with archetypal design - professional services, moderation services and open asset services — and o<sup>f</sup>er a <sup>fi</sup>t-as-moderation perspective on the applicability of economies of scope in production and innovation to these API archetypes. In so doing, we respond to Yoo et al.’s [108] call for further research on the strategic role of design decisions regarding boundary resources for digital platforms.

As our second contribution, we choose the individual API as our focal unit of analysis and, thus, extend the knowledge on the performance e<sup>f</sup>ects of API design. Prior research studies the aggregate use of APIs and discovers positive performance e<sup>f</sup>ects of API adoption on the <sup>fi</sup>rm level [9] and on the platform level [8, 93, 101, 107]. Thus, prior empirical research studies sets of APIs o<sup>f</sup>ered by a <sup>fi</sup>rm or by a platform and look at the collective role of APIs for <sup>fi</sup>rm and platform performance, respectively. Firm-level and platform-level analyses do not allow a direct linkage between individual APIs (particularly API design characteristics) and their performance impacts. At the <sup>fi</sup>rm level, Benzell et al. [9] compare <sup>fi</sup>rm performance (market value, R&D expenditure, data breaches) before and after the <sup>fi</sup>rst introduction of APIs. They show that whether or not a <sup>fi</sup>rm adopts APIs predicts a substantial increase in a <sup>fi</sup>rm’s market value. At the platform level, Xue et al. [107], for example, study how developer’s adoption of APIs, which are o<sup>f</sup>ered by a platform, in<sup>fl</sup>uences their likelihood to continue developing new applications for this platform. They examine how the adoption of APIs generally in<sup>fl</sup>uences platform performance (in terms of the number of apps hosted by a platform). Benlian et al. [8], as a second example for a platform-level analysis, regard the scope of functionalities APIs collectively o<sup>f</sup>er as part of their operationalization of platform openness, and show a positive relationship of platform openness with a platform’s perceived usefulness and developer satisfaction. Because most platforms o<sup>f</sup>er multiple APIs and alternative boundary resources such as software development kits, these studies only allow limited implications on the design and performance e<sup>f</sup>ects at the level of individual APIs. We take into account di<sup>f</sup>erent architecture-related and governance-related design decisions that APIs incorporate and distinguish between three API archetypes of professional, mediation, and open asset services. We relate these API archetypes to API ROI and di<sup>f</sup>usion. Our results extend our knowledge regarding the distinct consequences of di<sup>f</sup>erent API-level design choices. We, thus, respond to de Reuver et al.’s [24] call for further research on platform boundary resources that creates direct platform design knowledge.

As our third contribution, we respond to Gawer’s [36] call for empirical e<sup>f</sup>orts to validate her proposed organization-theoretic platform perspective. We adopt Gawer’s [36] organization-theoretic conceptualization of platform-based ecosystems that allows us to empirically study two modes of ecosystem value creation simultaneously: economies of scope in production and innovation. With our moderation-as-<sup>fi</sup>t-perspective, we establish that the provider’s API design must match the targeted mechanism of interorganizational value creation and the business objective (ROI or API di<sup>f</sup>usion). Our results suggest that, depending on the design, APIs facilitate economies of scope in production or innovation. Moreover, the <sup>fi</sup>t of API design with value creation strategies determines whether value exploration targets (via API di<sup>f</sup>usion) or value appropriation targets (via ROI) are achievable.

## Practical Implications

Our results generate two practical implications. First, API providers are challenged with overlooking an API’s relevance for strategic competitiveness [51]. Our results show that API providers should carefully align API archetype choice with the value creation strategy and the superordinate business objective. O<sup>f</sup>ering professional services may result in a positive ROI if they improve a software solution’s integrability. Mediation services may increase direct or indirect revenues in case they facilitate the integration of platform resources, such as end customer marketing capabilities for third-party developers. Open asset services, in contrast to the other two API archetypes, do not focus on value appropriation but on value generation only. They may generate high levels of API di<sup>f</sup>usion if the API provider successfully involves third-party developers in joint innovation. Second, API providers have di<sup>fi</sup>culties in attracting third-party developers and in de<sup>fi</sup>ning appropriate approaches to value appropriation [3, 12]. We suggest that API providers should align approaches towards value generation and appropriation with the value creation strategy. Leveraging economies of scope in production legitimates transaction-based or subscription-based API pricing. The realization of economies of scope in innovation, on the contrary, is not linked to value appropriation, but is an e<sup>f</sup>ective instrument for attracting third-party developers.

## Limitations and Further Research

One should interpret the results cognizant of the following limitations that open up avenues for further research. First, owing to our focus on public Internet APIs, the results do not apply to private APIs or non-Internet APIs that local applications expose. Further research may apply our model to investigate non-Internet APIs in local applications. Second, our study is limited to APIs o<sup>f</sup>ered by for-pro<sup>fi</sup>t providers. Further research may adapt our research model to study APIs that non-pro<sup>fi</sup>t providers such as governmental institutions o<sup>f</sup>er. Third, we do not study the e<sup>f</sup>ects of simultaneously o<sup>f</sup>ering more than one API. An avenue for further research is to build on our theory and explore the interaction e<sup>f</sup>ects that result from o<sup>f</sup>ering multiple APIs. Fourth, we limit our conceptualization of economies of scope in production to linkage e<sup>f</sup>ects resulting from facilitating the vertical integration of provider and customer systems. We do not study production economies relating to horizontal bundling and the use of shared inputs in digital platforms, to which future research may attend. Fifth, apart from economies of scope in production, this research only studies economies of scope in innovation. Another area for further research is a focal study of mediation services and how API design aligns with economies of scale in demand, which will require a detailed analysis of cross-platform externalities. Sixth, our measurement approach is limited in that, while the set of analyzed API design elements is theoretically motivated, backed by a thorough synopsis of the available literature, and empirically veri<sup>fi</sup>ed, we do not claim exhaustiveness of API archetypes. Also, API ROI is the product manager’s perception rather than an objective measure. Moreover, we analyze the levels to which an API provider targets the value creation mechanisms and do not provide objective measures for economies of scope in production and in innovation. Further research may introduce other measurement approaches to extend our <sup>fi</sup>ndings. Seventh, our cross-sectional analyses only ascertain association, but not the causal relationships inherent in our theoretical arguments. A fruitful area of further research that may expand on our results deals with investigating longitudinally how a time-varying API strategy impacts a provider’s platform evolution.

## Conclusion

In spite of the rich literature on digital platforms, there is sparse knowledge on the design of APIs and on how to successfully align API design with an API provider’s contextual conditions. In this research, we developed and validated a theoretical model that explains how the choice of API design interacts with the levels to which an API provider targets di<sup>f</sup>erent value creation mechanisms and how this interaction a<sup>f</sup>ects API ROI and di<sup>f</sup>usion. We contribute to the IS literate an overarching theory of API design that uni<sup>fi</sup>es prior theoretical perspectives and that extends current knowledge on the performance e<sup>f</sup>ects of API design.

## Notes

1. The basic idea of Frigyesi and Höglund [33] is to investigate how well an extracted factor or a number of extracted factors can reproduce the initial items from which the factor(s) were formed. They suggest to calculate the residual errors for an increasing number of factors for a data set and a permuted version of that data set. If the residual errors calculated from the permuted data set have the same size as the residual errors from the original data set, nonnegative matrix factorization has captured all the “noise” within a data set such that the extracted factor(s) do not contain useful information. However, the factors in the original data set show considerably smaller residual errors than the factors extracted from the permuted data set. Di<sup>f</sup>erences are biggest for one single factor such that we conclude that this single factor captures the relevant information from the underlying items.

2. We also performed a robustness check in which we considered API ROI as interval-scaled data and applied ordinary least square regressions. Results are consistent and lead to identical implications.

3. We also performed a robustness test for verifying these results. In greater detail, we applied log transformation to the three items with an o<sup>f</sup>set of 1 [44] as well as applied exploratory and con<sup>fi</sup>rmatory factor analysis. The psychometrical properties of this latent API di<sup>f</sup>usion factor were excellent. All three items loaded unambiguously and signi<sup>fi</sup>cantly with p < 0.01 on that factor. Chronbach α was 0.86, the Average Variance Explained was 0.68, and the Composite Reliability was 0.86. Using the Fornell-Larcker-Criterion the factor was clearly distinguishable from the other ones. Testing Model 2 by means of ordinary least square regression, we found very consistent results that lead to the identical implications.

## Acknowledgements

The authors acknowledge the JMIS Editor-in-Chief and the anonymous reviewers for their valuable contributions during the review process.

## ORCID

Jochen Wulf http://orcid.org/0000-0001-5553-8850 Ivo Blohm http://orcid.org/0000-0003-2422-5952

## References

1. Adner, R.; and Kapoor, R. Value creation in innovation ecosystems: How the structure of technological interdependence a<sup>f</sup>ects <sup>fi</sup>rm performance in new technology generations. Strategic Management Journal, 31, 3 (2010), 306–333.

2. Analytics REST API developer guide. Salesforce, 2019. https://developer.salesforce.com/docs/atlas. en-us.bi\_dev\_guide\_rest.meta/bi\_dev\_guide\_rest/bi\_rest\_overview.htm (accessed October 8, 2019).

3. Anu<sup>f</sup>, E. Almost everyone is doing the API economy wrong. Techcrunch, 2016. https:// techcrunch.com/2016/03/21/almost-everyone-is-doing-the-api-economy-wrong/(accessed October 8, 2019).

4. Armstrong, S.T.; and Overton, T.S. Estimating non-response bias in mail surveys. Journal of Marketing Research, 14, 3 (1977), 396–402.

5. Baer, M.; and Frese, M. Innovation is not enough: Climates for initiative and psychological safety, process innovations, and <sup>fi</sup>rm performance. Journal of Organizational Behavior, 24, 1 (2003), 45–68.

6. Bagozzi, R.P.; and Yi, Y. On the evaluation of structural equatation models. Journal of the Academy of Marketing Sciences, 16, 1 (1988), 74–94.

7. Benlian, A.; Koufaris, M.; and Hess, T. Service quality in software-as-a-service: Developing the SaaS-Qual measure and examining its role in usage continuance. Journal of Management Information Systems, 28, 3 (2011), 85–126.

8. Benlian, A.; Hilkert, D.; and Hess, T. How open is this platform? The meaning and measurement of platform openness from the complementors’ perspective. Journal of Information Technology, 30, 3 (2015), 209–228.

9. Benzell, S.G.; LaGarda, G.; Hersh, J.; and Van Alstyne, M.W. The Paradox of Openness: Exposure vs. E<sup>fi</sup>ciency of APIs. Boston University, 2019. http://dx.doi.org/10.2139/ssrn. 3432591(accessed October 8, 2019).

10. Bergkvist, L.; and Rossiter, J.R. The predictive validity of multiple-item versus single-item measures of the same constructs. Journal of Marketing Research, 44, 2 (2007), 175–184.

11. Boyd, M. Making API decisions: Are you connecting business and technical interests? ProgrammableWeb, 2017. https://www.programmableweb.com/news/making-api-decisions-areyou-connecting-business-and-technical-interests/analysis/2017/09/27 (accessed October 8, 2019).

12. Boyd, M. How to pick the best business models for your APIs. ProgrammableWeb, 2017. https://www.programmableweb.com/news/how-to-pick-best-business-models-your-apis/ana lysis/2017/09/27. (accessed October 8, 2019).

13. Brant, R. Assessing proportionality in the proportional odds model for ordinal logistic regression. Biometrics, 46, 4 (1990), 1171–1178.

14. Bresnahan, T.F.; and Trajtenberg, M. General purpose technologies ‘engines of growth’? Journal of Econometrics, 65, 1 (1995), 83–108.

15. Brunet, J.-P.; Tamayo, P.; Golub, T.R.; and Mesirov, J.P. Metagenes and molecular pattern discovery using matrix factorization. Proceedings of the National Academy of Sciences, 101, 12 (2004), 4164–4169.

16. Chesbrough, H.W.; and Appleyard, M.M. Open innovation and strategy. California Management Review, 50, 1 (2007), 57–76.

17. Chryssochoidis, G.M.; and Wong, V. Customization of product technology and international new product success: Mediating e<sup>f</sup>ects of new product development and rollout timeliness. Journal of Product Innovation Management, 17, 4, 268–285.

18. Cooper, R.G. The dimensions of industrial new product success and failure. Journal of Marketing, 43, 3 (1979), 93–103.

19. Create Audio Playlists On Dropbox. Streamboxr, 2019. https://streamboxr.com/(accessed October 8, 2019).

20. Curbera, F.; Khalaf, R.; Mukhi, N.; Tai, S.; and Weerawarana, S. The next step in web services. Communications of the ACM, 46, 10 (2003), 29–34.

21. D’Aveni, R.A.; and Ravenscraft, D.J. Economies of integration versus bureaucracy costs: Does vertical integration improve perfoermance? Academy of Management Journal, 37, 5 (1994), 1167–1206.

22. Dal Bianco, V.; Myllarniemi, V.; Komssi, M.; and Raatikainen, M. The role of platform boundary resources in software ecosystems: A case study. IEEE/IFIP Conference on Software Architecture, Washington, DC, USA: IEEE Computer Society 2014, pp. 11–20.

23. DBX platform - Develop apps for 500 million Dropbox users. Dropbox, 2019. https://www. dropbox.com/developers (accessed October 8, 2019).

24. de Reuver, M.; Sørensen, C.; and Basole, R.C. The digital platform: A research agenda. Journal of Information Technology, 33, 2 (2017), 124–135.

25. Demirkan, H.; and Delen, D. Leveraging the capabilities of service-oriented decision support systems: Putting analytics and big data in cloud. Decision Support Systems, 55, 1 (2013), 412–421.

26. Dollinger, M.J.; and Golden, P.A. Interorganizational and collective strategies in small <sup>fi</sup>rms: Environmental e<sup>f</sup>ects and performance. Journal of Management, 18, 4 (1992), 695–715.

27. Eaton, B.; Elaluf-Calderwood, S.; Sorensen, C.; and Yoo, Y. Distributed tuning of boundary resources: The case of Apple’s iOS service system. MIS Quarterly, 39, 1 (2015), 217–243.

28. Evans, D.S.; and Schmalensee, R. Matchmakers: The New Economics of Multisided Platforms. Boston, MA, USA: Harvard Business Review Press, 2016.

29. Evans, P.C.; and Basole, R.C. Revealing the API ecosystem and enterprise strategy via visual analytics. Communations of the ACM, 59, 2 (2016), 26–28.

30. Fang, E. Customer participation and the trade-o<sup>f</sup> between new product innovativeness and speed to market. Journal of Marketing, 72, 4 (2008), 90–104.

31. Foreman, J.W. Data Smart: Using Data Science to Transform Information into Insight. Indianoplis, IN, USA: John Wiley & Sons, 2013.

32. Fornell, C.; and Larcker, D.F. Evaluating structural equation models with unobservable variables and measurement error. Journal of Marketing Research, 18, 2 (1981), 39–50.

33. Frigyesi, A.; and Höglund, M. Non-negative matrix factorization for the analysis of complex gene expression data: Identi<sup>fi</sup>cation of clinically relevant tumor subtypes. Cancer Informatics, 6(2008), 275–292.

34. Garcia, S.; Moreaux, M.; and Reynaud, A. Measuring economies of vertical integration in network industries: An application to the water sector. International Journal of Industrial Organization, 25, 4 (2007), 791–820.

35. Gawer, A.; and Henderson, R. Platform owner entry and innovation in complementary markets: Evidence from Intel. Journal of Economics & Management Strategy, 16, 1 (2007), 1–34.

36. Gawer, A. Bridging di<sup>f</sup>ering perspectives on technological platforms: Toward an integrative framework. Research Policy, 43, 7 (2014), 1239–1249.

37. Ghazawneh, A.; and Henfridsson, O. Micro-strategizing in platform ecosystems: A multiple case study. International Conference on Information Systems, Shanghai, China: Association for Information Systems, 2011, pp. 1–19.

38. Ghazawneh, A.; and Henfridsson, O. Balancing platform control and external contribution in third-party development: The boundary resources model. Information Systems Journal, 23, 2 (2013), 173–192.

39. Ghazawneh, A.; and Henfridsson, O. A paradigmatic analysis of digital application marketplaces. Journal of Information Technology, 30, 3 (2015), 198–208.

40. Ginsberg, A.; and Venkatraman, N. Contingency perspectives of organizational strategy: A critical review of the empirical research. Academy of Management Review, 10, 3 (1985), 421–434.

41. Gonçalves, V.; and Ballon, P. Adding value to the network: Mobile operators’ experiments with Software-as-a-Service and Platform-as-a-Service models. Telematics and Informatics, 28, 1 (2011), 12–21.

42. Gosain, S. Realizing the vision for web services: Strategies for dealing with imperfect standards. Information Systems Frontiers, 9, 1 (2007), 53–67.

43. Gunarathne, P.; Rui, H.; and Seidmann, A. Whose and what social media complaints have happier resolutions? Evidence from Twitter. Journal of Management Information Systems, 34, 2 (2017), 314–340.

44. Guo, J.; Zhang, W.; Fan, W.; and Li, W. Combining geographical and social in<sup>fl</sup>uences with deep learning for personalized point-of-interest recommendation. Journal of Management Information Systems, 35, 4 (2018), 1121–1153.

45. Harrell, F. Regression Modeling Strategies. Cham, Switzerland: Springer, 2015.

46. Hartmann, P.M.; Zaki, M.; Feldmann, N.; and Neely, A. Capturing value from big data - A taxonomy of data-driven business models used by start-up <sup>fi</sup>rms. International Journal of Operations & Production Management, 36, 10 (2016), 1382–1406.

47. Henfridsson, O.; and Bygstad, B. The generative mechanisms of digital infrastructure evolution. MIS Quarterly, 37, 3 (2013), 907–931.

48. Hjalmarsson, A.; Juell-Skielse, G.; Ayele, W.Y.; Rudmark, D.; and Johannesson, P. From contest to market entry: A longitudinal survey of innovation barriers constraining open data service development. European Conference on Information Systems, Münster, Germany: Association for Information Systems, 2015.

49. Hornik, K.; Feinerer, I.; Kober, M.; and Buchta, C. Spherical k-means clustering. Journal of Statistical Software, 50, 10 (2012), 1–22.

50. Im, S.; and Workman Jr, J.P. Market orientation, creativity, and new product performance in high-technology <sup>fi</sup>rms. Journal of Marketing, 68, 2 (2004), 114–132.

51. Iyer, B.; and Subramaniam, M. The strategic value of APIs. Harvard Business Review Digital Articles, 2015. https://hbr.org/2015/01/the-strategic-value-of-apis (accessed October 8, 2019).

52. Jacobides, M.G.; Cennamo, C.; and Gawer, A. Towards a theory of ecosystems. Strategic Management Journal, 39, 8 (2018), 2255–2276.

53. Jacobson, D.; Brail, G.; and Woods, D. APIs: A Strategy Guide. Sebastopol, CA, USA: O’Reilly, 2011.

54. Jansen, S.; Brinkkemper, S.; and Finkelstein, A. Business network management as a survival. In S. Jansen, S Brinkkemper, and A. Finkelstein (eds.), Software Ecosystems: Analyzing and Managing Business Networks in the Software Industry. Cheltenham, UK: Edward Alger Publishing, 2013, pp. 29–42.

55. Krishnan, V.; and Gupta, S. Appropriateness and impact of platform-based product development. Management Science, 47, 1 (2001), 52–68.

56. Kuk, G.; and Davies, T. The roles of agency and artifacts in assembling open data complementarities. International Conference on Information Systems, Shanghai, China: Association for Information Systems, 2011.

57. Landis, J.R.; and Koch, G.G. The measurement of observer agreement for categorical data. Biometrics, 33, 1 (1977), 159–174.

58. Lee, D. The API for absurdity. Techcrunch, 2016. https://techcrunch.com/2016/08/27/the-apifor-absurdity/(accessed October 8, 2019).

59. Lee, D.D.; and Seung, H.S. Algorithms for non-negative matrix factorization. Advances in Neural Information Processing Systems, Denver, CO, USA: Neural Information Processing Systems Foundation, 2001, pp. 556–562.

60. Lee, S.M.; Kim, T.; Noh, Y.; and Lee, B. Success factors of platform leadership in web 2.0 service business. Service Business, 4, 2 (2010), 89–103.

61. Legner, C. Do web services foster specialization? An analysis of commercial web service directories. International Conference on Wirtschaftsinformatik, Wien, Austria: Association for Information Systems, 2009, pp. 67–76.

62. Leisch, F. A toolbox for k-centroids cluster analysis. Computational Statistics & Data Analysis, 51, 2 (2006), 526–544.

63. Lin, A.; and Chen, N.-C. Cloud computing as an innovation: Percepetion, attitude, and adoption. International Journal of Information Management, 32, 6 (2012), 533–540.

64. Lindman, J.; Rossi, M.; and Tuunainen, V.K. Open data services: Research agenda. Hawaii International Conference on System Sciences, Wailea, HI, USA: IEEE Computer Society, 2013, pp. 1239–1246.

65. Lindman, J.; Kinnari, T.; and Rossi, M. Business roles in the emerging open-data ecosystem. IEEE Software, 33, 5 (2016), 54–59.

66. Lusch, R.F.; and Nambisan, S. Service innovation: A service-dominant logic perspective. MIS Quarterly, 39, 1 (2015), 155–175.

67. Malhotra, A.; Gosain, S.; and Sawy, O.A.E. Absorptive capacity con<sup>fi</sup>gurations in supply chains: Gearing for partner-enabled market knowledge creation. MIS Quarterly, 29, 1 (2005), 145–187.

68. McNally, R.C.; Akdeniz, M.B.; and Calantone, R.J. New product development processes and new product pro<sup>fi</sup>tability: Exploring the mediating role of speed to market and product quality. Journal of Product Innovation Management, 28, s1 (2011), 63–77.

69. Mizik, N.; and Jacobson, R. Trading O<sup>f</sup> Between Value Creation and Value Appropriation: The Financial Implications of Shifts in Strategic Emphasis. Journal of Marketing, 67, 1 (2003), 63–76.

70. Mueller, B.; Viering, G.; Legner, C.; and Riempp, G. Understanding the economic potential of service-oriented architecture. Journal of Management Information Systems, 26, 4 (2010), 145–180.

71. Mu<sup>f</sup>atto, M.; and Roveda, M. Product architecture and platforms: A conceptual framework. International Journal of Technology Management, 24, 1 (2002), 1–16.

72. Munaiah, N.; Kroh, S.; Cabrey, C.; and Nagappan, M. Curating GitHub for engineered software projects. Empirical Software Engineering, 22, 6 (2017), 3219–3253.

73. Murphy, M.; and Sloane, S. The rise of APIs. Techcrunch, 2016. https://techcrunch.com/2016/ 05/21/the-rise-of-apis/(accessed October 8, 2019).

74. Nambisan, S.; and Sawhney, M. Orchestration processes in network-centric innovation: Evidence from the <sup>fi</sup>eld. Academy of Management Perspectives, 25, 3 (2011), 40–57.

75. Niculescu, M.F.; Wu, D.; and Xu, L. Strategic intellectual property sharing: Competition on an open technology platform under network e<sup>f</sup>ects. Information Systems Research, 29, 2 (2018), 498–519.

76. Nüttgens, M.; and Iskender, D. Business models of service-oriented information systems - A strategic approach towards the commercialization of web services. Wirtschaftsinformatik, 50, 1 (2008), 31–38.

77. Oh, J.; Koh, B.; and Raghunathan, S. Value appropriation between the platform provider and app developers in mobile platform mediated networks. Journal of Information Technology, 30, 3 (2015), 245–259.

78. Panzar, J.C.; and Willig, R.D. Economies of scope. American Economic Review, 71, 2 (1981), 268–272.

79. Parker, G.; Van Alstyne, M.; and Jiang, X. Platform ecosystems: How developers invert the <sup>fi</sup>rm. MIS Quarterly, 41, 1 (2017), 255–266.

80. Parker, G.G.; and Van Alstyne, M.W. Two-sided network e<sup>f</sup>ects: A theory of information product design. Management Science, 51, 10 (2005), 1494–1504.

81. Podsako<sup>f</sup>, P.M.; MacKenzie, S.B.; Lee, J.-Y.; and Podsako<sup>f</sup>, N.P. Common method biases in behavioral research: A critical review of the literature and recommended remedies. Journal of Applied Psychology, 88, 5 (2003), 879–903.

82. Reynolds, A.P.; Richards, G.; de la Iglesia, B.; and Rayward-Smith, V.J. Clustering rules: A comparison of partitioning and hierarchical clustering algorithms. Journal of Mathematical Modelling and Algorithms, 5, 4 (2006), 475–504.

83. Rossiter, J.R. The C-OAR-SE procedure for scale development in marketing. International Journal of Research in Marketing, 19, 4 (2002), 305–335.

84. Rudmark, D. The practices of unpaid third-party developers – Implications for API design. Americas Conference on Information Systems, Chicago, IL, USA: Association for Information Systems, 2013.

85. Santos, W. APIs show faster growth rate in 2019 than previous years. ProgrammableWeb, 2019. https://www.programmableweb.com/news/apis-show-faster-growth-rate-2019-previous -years/research/2019/07/17. (accessed October 8, 2019).

86. Schreieck, M.; Wiesche, M.; and Krcmar, H. Design and governance of platform ecosystems - Key concepts and issues for future research. European Conference on Information Systems, Instanbul, Turkey: Association for Information Systems, 2016, pp. 1–20.

87. Selander, L.; Henfridsson, O.; and Svahn, F. Capability search and redeem across digital ecosystems. Journal of Information Technology, 28, 3 (2013), 183–197.

88. Setia, P.; Rajagopalan, B.; Sambamurthy, V.; and Calantone, R. How peripheral developers contribute to open-source software development. Information Systems Research, 23, 1 (2012), 144–163.

89. Shi, Z.; and Whinston, A.B. Network structure and observational learning: Evidence from a location-based social network. Journal of Management Information Systems, 30, 2 (2013), 185–212.

90. Simon, H.A. The architecture of complexity. Proceedings American Philosophical Society, 106, 6 (1962), 467–482.

91. Sivo, S.A.; Saunders, C.; Chang, Q.; and Jiang, J.J. How low should you go? Low response rates and the validity of inference in IS questionnaire research. Journal of the Association for Information Systems, 7, 1 (2006), 351–414.

92. Smedlund, A. Value cocreation in service platform business models. Service Science, 4, 1 (2012), 79–88.

93. Song, P.; Xue, L.; Zhang, C.; and Rai, A. APIs in software platform: Implications for innovation and imitation. International Conference on Information Systems, Seoul, Korea: Association for Information Systems, 2017, pp. 1–11.

94. Song, P.; Xue, L.; Rai, A.; and Zhang, C. The ecosystem of software platform: A study of asymmetric cross-side network e<sup>f</sup>ects and platform governance. MIS Quarterly, 42, 1 (2018), 121–142.

95. Stieglitz, S.; and Dang-Xuan, L. Emotions and information di<sup>f</sup>usion in social media - Sentiment of microblogs and sharing behavior. Journal of Management Information Systems, 29, 4 (2013), 217–248.

96. Svahn, F.; Mathiassen, L.; and Lindgren, R. Embracing digital innovation in incumbent <sup>fi</sup>rms: How Volvo Cars managed competing concerns. MIS Quarterly, 41, 1 (2017), 239–253.

97. Swink, M.; and Song, M. E<sup>f</sup>ects of marketing-manufacturing integration on new product development time and competitive advantage. Journal of Operations Management, 25, 1 (2007), 203–217.

98. The New York Times developer network. New York Times, 2019. https://developer.nytimes. com/. (accessed October 8, 2019).

99. Tiwana, A.; Konsynski, B.; and Bush, A.A. Platform evolution: Coevolution of platform architecture, governance, and environmental dynamics. Information Systems Research, 21, 4 (2010), 675–687.

100. Tiwana, A. Platform Ecosystems: Aligning Architecture, Governance, and Strategy. Waltham, MA, USA: Morgan Kaufmann, 2013.

101. Tiwana, A. Platform desertion by app developers. Journal of Management Information Systems, 32, 4 (2015), 40–77.

102. Venkatraman, N. The concept of <sup>fi</sup>t in strategy research: Towards verbal and statistical sorrespondence. Academy of Management Review, 14, 3 (1989), 423–444.

103. Von Hippel, E.; and Katz, R. Shifting innovation to users via toolkits. Management Science, 48, 7 (2002), 821–833.

104. Wall, T.D.; Michie, J.; Patterson, M.; Wood, S.J.; Sheehan, M.; Clegg, C.W.; and West, M. On the validity of subjective measures of company performance. Personnel Psychology, 57, 1 (2004), 95–118.

105. Wedel, M.; Böckenholt, U.; and Kamakura, W.A. Factor models for multivariate count data. Journal of Multivariate Analysis, 87, 2 (2003), 356–369.

106. Xin, M.; and Levina, N. Software-as-a-service model: Elaborating client-side adoption factors. International Conference on Information Systems, Paris, France: Association for Information Systems, 2008, pp. 1–12.

107. Xue, L.; Rai, A.; Song, P.; and Cheng, Z. Third-party developers’ adoption of APIs and their continued new app development in software platform: A competing risk analysis. Conference on Information Systems & Technology, Houston, TX, USA: INFORMS, 2017.

108. Yoo, Y.; Henfridsson, O.; and Lyytinen, K. The new organizing logic of digital innovation: An agenda for information systems research. Information Systems Research, 21, 4 (2010), 724–735.

109. Yu, S.; and Woodard, C.J. Innovation in the programmable web: Characterizing the mashup ecosystem. International Conference on Service-Oriented Computing, Sydney, Australia: Springer, 2008, pp. 136–147.

110. Zimmermann, S.; Müller, M.; and Heinrich, B. Exposing and selling the use of web services: An option to be considered in make-or-buy decision-making. Decision Support Systems, 89 (2016), 28–40.

111. Zittrain, J.L. The generative internet. Harvard Law Review, 119, 7 (2006), 1974–2040.

## About the Authors

Jochen Wulf (jochen.wulf@unisg.ch; corresponding author) is a lecturer at the Institute of Information Management, University of St.Gallen, Switzerland. He obtained a Ph.D. in Information Systems from the Technical University of Berlin, Germany. His research on datadriven services, consumer-centric information systems, and information technology (IT) service management has been published in such journals as Journal of Management Information Systems, Journal of Marketing, Journal of the Association for Information Systems, and Information Systems Journal. Dr. Wulf has several years of consulting experience in the areas of IT service management, digital consumer services, and business analytics. He was awarded a grant of the International Postdoctoral Fellowship program while being an assistant professor at the University of St.Gallen.

Ivo Blohm (ivo.blohm@unisg.ch) is an Assistant Professor for Data Science and Management at the Institute for Information Management at the University of St. Gallen. His research focuses on business analytics, crowdsourcing, and crowd work, as well as digital platforms. His work has appeared, among others, in such journals as Information Systems Research, Journal of Management Information Systems, and California Management Review.
