---
otero_id: 25068
otero_key: "KM6K9UYU"
title: "Integration in Electronic Exchange Environments"
authors: ""
year: "2000"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2000.11045630"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Integration in Electronic Exchange Environments

Gregory E. Truman

To cite this article: Gregory E. Truman (2000) Integration in Electronic Exchange Environments, Journal of Management Information Systems, 17:1, 209-244

To link to this article: http://dx.doi.org/10.1080/07421222.2000.11045630

![](/api/attachments/KM6K9UYU/fulltext/images/1aea3926b1e9fc809aec87741cad4b062997a5a8ccdc2951b5a45fc9eb1eb670.jpg)

Published online: 09 Jan 2015.

![](/api/attachments/KM6K9UYU/fulltext/images/ab40e2d7110f9dfbcd8b4613f24b2c8e8ce485ad32727f15bfd781331f2baac8.jpg)

Submit your article to this journal

![](/api/attachments/KM6K9UYU/fulltext/images/c502d1325719f11b78e0862fa8a56907cae21a6f85e490cfeebf9f8f1e5f0aeb.jpg)

Article views: 7

![](/api/attachments/KM6K9UYU/fulltext/images/f98b1dacfa8c3bc917bea1b27de6d2874b33d65456a3cea024d043a3a4d081b1.jpg)

View related articles

# Integration in Electronic Exchange Environments

GREGORY E. TRUMAN

GREGORY E. TRUMAN is an Assistant Professor of Information Systems at the Schools of Business at Fordham University in New York City, where he teaches both graduate and undergraduate courses in information systems. He earned his Ph.D. in Information Systems from the Stern School of Business at New York University. Professor Truman has published articles in Communications of the ACM, MIS Quarterly, Journal of Organizational Computing and Electronic Commerce, and the International Journal of Electronic Commerce. He is a member of INFORMS, ACM, and AIS. Professor Truman’s research interests center on electronic exchange systems, electronic integration, and systems performance.

ABSTRACT: Provided the increasing prevalence of electronic exchange environments—including propriety electronic data interchange (EDI) and some Internetbased EDI (e-commerce) systems—we argue that management’s decision-making focus vis-à-vis electronic data interchange (EDI) assumes a tactical disposition rather than a strategic one. We offer that the formulation and execution of tactics may be organized around the general question of how to effectively integrate EDI with internal systems, since this appears to be crucial for obtaining the expected perfor mance advantages. We distinguish between two integration concepts, including the integration between the EDI systems and internal systems (interface integration), and the integration among the internal systems (internal integration). Based on theory and literature, we propose that interface integration is favorably related to perfor mance outcomes, and that interface integration and internal integration are posi tively related. Using data from the Group Insurance industry, we obtain supportive findings. We conclude that tactical EDI planning should centrally focus on interface integration regardless of how intensively management plans to use EDI. We further conclude that management may want to consider internal integration as a risk factor during EDI implementation, because the ability to establish high inter face integration may be inhibited or advanced by low or high internal integration, respectively.

KEY WORDS AND PHRASES: e-commerce, electronic data interchange (EDI), electronic integration, health care information systems, interorganizational information systems, information systems performance

THE INTERNET’S EMERGENCE AS A STANDARDIZED GLOBAL DATA NETWORK has cre ated clear incentives for organizations to use a variety of electronic exchange systems, which may be collectively referred to as electronic commerce (e-commerce). Specific instances of e-commerce applications are now found in any functional area, in both large and small organizations, in virtually all industries, and in practically all coun tries. Moreover, although e-commerce currently supports a small proportion of overall economic activity, before long a majority of economic activity will likely be supported by e-commerce due to the manifold advantages that are believed to follow. On the whole then, furthering a general understanding of electronic exchange systems may yield benefit to those who represent broad, diverse, and expansive business interests.

Zwass [112] employs a hierarchical conceptualization of e-commerce as consisting of three metalevels: infrastructure, services, and products and structures. Within the services level are several messaging and transmission services, which include electronic data interchange (EDI). While EDI may be generally defined as interorganizational systems that support business-to-business electronic exchange, e-commerce may be broadly characterized as the means by which organizations share information, exchange transactions, and coordinate processes over telecommunication networks with other organizations and consumers. E-commerce practices among organizations are frequently referred to as business-to-business e-commerce (indus trial sector), and e-commerce practices between organizations and consumers are commonly referred to as business-to-consumer e-commerce (retail sector). As a pre cursor to e-commerce in the industrial sector, EDI has assumed a significant role in the evolution of current-day e-commerce practices. Consequently, we take the view that the cumulative research on EDI is germane to the application of e-commerce in the industrial sector, but that the application of e-commerce in the retail sector introduces a host of issues and implications that are unrelated to EDI (e.g., implications regarding consumers’ incentives for using e-commerce applications [9] or consumers’ assessment of the value of products purchased over the Internet [54]). Because the greater share of existing e-commerce applications, and expected growth in new ones, is in the industrial sector [26, 38, 99, 100], EDI research is relevant to a majority of e-commerce practices.<sup>1</sup>

Developments surrounding e-commerce have technically redefined EDI. This re definition manifests largely in the replacement of proprietary communication protocols by the TCP/IP communication protocol, which effects greater standardization for exchange purposes. The greater standardization increases the use potential of EDI, which suggests that organizations of different industries, sizes, and countries will increasingly rely on electronic means to transact data [4, 33]. This argument is consistent with the assertion of Benjamin et al. [11] that the competitive emphasis behind EDI use has shifted, albeit gradually, from one of competitive advantage to one of competitive necessity. Thus, we assume that EDI will become even more ubiquitous, primarily in the form of e-commerce applications.

The empirical research that has examined antecedents to EDI use has found that, while many organizations voluntarily implement EDI for strategic or operational advantages, some organizations find EDI systems imposed on them by their trading partners [14, 15, 42, 48, 64, 86, 88, 95, 111]. For example, Premkumar and Ramamurthy [86] found that trading partners’ competitive pressure and exercised power are sig nificant discriminators between proactive and reactive organizations, and characteristic of reactive organizations’motives for adopting EDI. Additionally, Iacovou et al. [48] found that small organizations tend be reactive, in that EDI is often imposed on them by their larger trading partners. Others have suggested that trust plays a signifi cant role, with proactive and reactive organizations having a comparatively high and low degree of trust in their trading partners, respectively [42, 110]. Thus, we assume that a significant number of organizations have EDI imposed on them by their trad ing partners.

Provided these assumptions, we suggest that the decision emphasis regarding EDI implementation has shifted in a comparative sense. In the past the decision regarding whether and to what extent to implement EDI has been management’s dominant concern, while today the decision regarding how to implement EDI is comparatively more important. Viewed in this light, management’s decision-making focus vis-à-vis EDI assumes a tactical disposition rather than a strategic one. Moreover, provided that e-commerce subsumes EDI, understanding how EDI implementation tactics re late to expected performance advantages may offer useful guidance to IS managers in an era marked by the rapid development and increasingly commonplace nature of e commerce. Thus, in the context of EDI and from an organizational perspective, we offer that the formulation and execution of tactics may be organized around two gen eral questions: (1) how to effectively deploy EDI, and (2) how to effectively integrate EDI with internal systems. We focus on the second question here.<sup>2</sup>

We conceptually and empirically distinguish between two integration concepts: (1) the integration of EDI with internal systems, and (2) the integration among the internal systems. Based on existing theory and literature, we argue that organizations vary on these integration concepts, which may affect the realization of expected EDI per formance advantages. Although these integration concepts have been distinguished in the literature, they have not been empirically assessed in the same study. We have two specific research objectives here. The first objective is to theoretically discuss and empirically examine the relationship between EDI’s integration with internal sys tems and performance outcomes. The second objective is to theoretically discuss and empirically examine the relationship between the two integration concepts.

## Research Context

NUMEROUS THEORETICAL AND CONCEPTUAL FRAMEWORKS have been proposed to distinguish among types of EDI [3, 7, 22, 37, 45, 65], and most draw heavily from Williamson’s [108] theoretical work on governance structures. Although EDI in prac tice may elude strict characterization as theoretical “pure forms” of any conceptualization—including that of Williamson’s governance structures [45]—the theoretical “pure forms” nonetheless offer a useful starting point for two reasons. First, the cumulative research heavily draws from this theoretical work, so it is useful to understand how this study compares and contrasts to previous ones. Second, since the theoretical implications of EDI will vary according to and be bounded by the type of EDI under consideration, any subsequent discussion and generalization of conclusions must be limited to like EDI systems.

We define EDI as information systems that exchange structured data between dissimilar applications of two organizations [48]. An EDI system requires a sponsor— one or several organizations that assume the primary responsibility for its development, maintenance, and operation. The sponsor is typically one user of the EDI system as well. Far greater in number are organizations that use the EDI system, but perform no sponsoring role. These organizations may be called participants. Although Lee et al. [63] recently found empirical support for participants’ realization of performance benefits, Nygaard-Andersen and Bjørn-Andersen [77] noted earlier that the research community has been comparatively less attentive to the participant’s perspective, which we adopt here. In addition, the EDI that is studied here has evolved into supporting both ex ante and ex post transaction support functions, as defined by Bakos [3]. There fore we characterize the EDI as a hybrid form. Finally, because this EDI system em ploys national ANSI X.12 standards, it is best characterized as multilateral, as defined by Bakos [3] and Choudhury [22]. In sum, our findings may generalize to other EDI systems of this hybrid, multilateral type.

Our research setting is the insurance industry, which consists of two segments that we refer to as Group Insurance and Personal Insurance. We offer that these segments are substantively different in several ways,<sup>3</sup> a view that is consistent with Venkatraman and Zaheer [106] and industry training literature [47]. More specifically, our research setting is the Group Insurance industry, while previous studies have been set in the Personal Insurance industry [40, 75, 78, 106, 110].

## Theoretical Considerations

A SIGNIFICANT SHARE OF THE RESEARCH ON EDI PERFORMANCE IMPACTS has been couched in terms of strategic advantages, and informs many strategic issues related to EDI. These studies have drawn from Williamson’s [108] transaction cost theory [5, 14, 37, 41, 65, 79], Porter’s [83] industry structure framework [14, 19, 20, 24, 53, 80, 85], and Porter’s [84] value added chain perspective [14, 17, 24, 41, 85], among others. However, our interest lies in tactical issues, which warrant a different theoretical perspective. More specifically, we require a theoretical perspective that in forms about integration issues.

Because our unit of analysis is the organization and EDI occupies an interorganizational role, we assume that each organization is part of an open system of other organizations that collectively makeup its environment. Moreover, as part of that system, each organization must exchange information and resources with its environment. These exchange tasks are performed by specialized boundary-spanning roles, which interface with trading partners. We also assume that the organization consists of subunits that are task-specialized and require coordination. Because the information processing model of the organization incorporates these assumptions in a reasonably comprehensive way, we draw from it.

## Organizations as Information Processing Entities

The open systems perspective views the organization as an entity that requires exchange with its environment in order to sustain its survival [94]. Among various conceptions of the environment [31], Meyer and Scott [70] view it as possessing an institutional and a technical dimension.<sup>4</sup> Dill [29] was among the first to refer to the technical dimension as the firm’s task environment, which mostly consists of suppliers, competitors and customers. Aldrich and Mindlin [2] identify two “currencies” of exchange with the task environment including resources and information. They argue that information exchange requirements present uncertainty problems, which the or ganization must manage. Although technology and environmental characteristics sys tematically affect uncertainty levels associated with the task environment [29, 81, 101], it is generally accepted that all organizations confront some uncertainty related to its task environment.

Tushman and Nadler [104] recognize task environment uncertainty, and two additional uncertainty sources when provided the assumption that an organization may consist of subunits. They identify uncertainty stemming from inter-subunit task interdependence and from subunit task characteristics. Although we do not debate the validity of a tripartite conceptual framework, the uncertainty associated with subunit task characteristics is not germane to our study.<sup>5</sup> Thus, we conceptually distinguish between two uncertainty sources: (1) uncertainty from exchange with the task environment—external uncertainty, and (2) uncertainty from interdependent tasks be tween organizational subunits—internal uncertainty

External uncertainty may manifest in the random and unpredictable nature of interorganizational exchange relationships, such as trading partners’ aberrant ac tions and behaviors. Because these actions and behaviors are outside the organization’s control, specialized boundary-spanning roles are established to decouple the organization’s internal processes from external disturbances. A primary objective in the design of boundary-spanning roles is to manage coordination between an organization and its trading partners. In today’s typical computing envi ronment, EDI is increasingly used to promote, advance, and strengthen coordination between organizations.

With regards to internal uncertainty, we assume that an organization’s subunits are task-specialized. Because most business processes span multiple subunits, inter-subunit task interdependence invariably occurs. Thompson [101] conceptually distinguishes among three types of task interdependence, including pooled, sequential, and reciprocal, which give rise to internal uncertainty in varying degrees. Random and unpredictable events in one subunit may disrupt the process flow, result in idle resources, or give rise to error in another subunit. In order to mitigate these and other adverse consequences, an organization designs coordinating mechanisms in order to manage task interdependence between subunits. In today’s typical computing environment, internal systems are used to promote, advance, and strengthen coordination between subunits.

In sum, an organization strives to enhance coordination among task-specialized organizational subunits and with other organizations of its task environment. In the most general sense, coordination is argued to lead to improved organization perfor mance [61]. Among alternative coordinating mechanisms, information systems may be used to expand an organization’s overall processing capacity in order to effect higher coordination levels [34]. One means to establish greater capacity is to raise the information systems’ integration levels. Although the merits of integration should be critically assessed—for there are costs as well as benefits [36]—it is generally ac cepted that integration will lead to enhanced coordination, with attending perfor mance advantages.

## The Role of Integration in Electronic Exchange Environments

We are interested in two integration concepts that have been treated as conceptually distinct and theoretically relevant in the context of EDI [41, 68, 96, 98]. One concept is the level of integration between the EDI and internal systems, which we call inter face integration. On a conceptual level, interface integration refers to the level, de gree or amount of integration between an EDI system and an internal system—that is, at the “boundary” between the organization and its task environment. The other concept is the level of integration among the internal systems, which we call internal integration. Internal integration refers to the level, degree, or amount of integration among the internal systems. Previous research suggests that interface integration [21, 30, 41, 55, 64, 68, 73, 87, 88, 89, 90, 96, 98] and internal integration [41, 43, 68, 96, 98] may be associated with EDI performance benefits. While the role of interface integration has been empirically explored in this context [55, 90, 96], internal integration has not.

For the purpose of discourse, we offer a conceptual view of EDI as a technology cluster. Presented in Rogers’s [93] work on innovation, a technology cluster “consists of one or more distinguishable elements of technology that are perceived as being closely interrelated” (p. 226). We find that EDI consists of a “bundle” of multiple functionally interrelated transaction types in practice [30], where a collection of transaction types may be implemented in order to provide an organization with cross functional EDI capability [30, 73] or broad transaction-based communication ability [74]. Moreover, when two functionally interrelated transaction types have been imple mented, the possibility of gaining cross-functional efficiencies arises [51, 64, 67]. Although the implementation of a single transaction type may occur with attending benefit, a typical implementation process begins with one transaction type, followed by successive implementation of functionally interrelated transaction types [98]. Thus, we argue that EDI may be usefully characterized as a technology cluster.

In characterizing EDI as a technology cluster, we and others observe that EDI use has several conceptually distinct facets [7, 51, 67, 79]. Massetti and Zmud [67] present four facets, which they refer to as breadth, volume, diversity, and depth. From the participant’s perspective, breadth is defined as the number of EDI trading partners that are using a given transaction type. Volume is defined as the percentage of data exchange that is conducted via EDI for a given transaction type, while diversity is defined as the number of transaction types a participant has implemented. Finally, depth is defined as a characterization of the EDI-facilitated connection between two organizations, where shallow (deep) depth is suggestive of loosely (tightly) coupled business processes. Massetti and Zmud [67] conclude that the four facets offer a robust, rich, and comprehensive conceptualization of EDI use, and others have drawn from their conceptualization for operationalizing EDI use [43].

Our EDI use construct incorporates Massetti and Zmud’s notion of volume and diversity, while their notion of depth is incorporated into our integration construct.<sup>6</sup> In order to derive our variables, we require measures on multiple functionally interre lated transaction types. Five transaction types that subscribe to ANSI X.25 standards in the Group Insurance industry constitute our technology cluster: ANSI #270, #834, #835, #837, and #839. (Brief descriptions of the transaction types’ data content are provided in the appendix.) These transaction types are functionally interrelated in that each is involved with the administration of payment for medical services by the Group Insurers. By including multiple functionally interrelated transaction types in conceptualizing EDI use, our study contrasts with previous ones that operationalize EDI use through one dichotomous measure on a single transaction type [18, 55, 74, 88, 90, 96, 106].

## Interface Integration

According to Aldrich and Herker [1], boundary-spanning roles perform the dual func tions of information processing and external representation. The information processing function’s objective is to interpret, filter, store, summarize, and route information into and out of the organization in order to promote coordination with its task environment.<sup>7</sup> March and Simon [66] identify programming and feedback as two general ways to facilitate coordination. Van De Ven et al. [105] extend on March and Simon’s work by specifying three modes of coordination, including an impersonal mode (pro gramming) and personal and group modes (feedback). They characterize the imper sonal mode as coordination by preestablished plans and schedules, formalized rules, policies and procedures, and information and communication systems. In contrast, the personal and group modes promote coordination through mutual adjustment mecha nisms, such as vertical and horizontal communication and scheduled and unscheduled meetings. The former is comparatively routine, formal, and programmed, while the latter is comparatively nonroutine, informal, and ad hoc. Brown [16] similarly distinguishes boundary-spanning roles through his concept of coding process—character ized as controlling the variety and amount of interorganizational information flows, which he defines on the basis of distinguishing between mechanical and human trans mission modes. These conceptual distinctions strongly parallel Hickson’s [44] conceptual bifurcation of role expectations, which he offered as a means to unify the existing body of organization theory. Hickson argues that a vein running through many organization theories rests on the degree of role prescriptions—highly specified role prescriptions versus widely ranged legitimate discretion.

We apply a similar theoretical distinction to boundary-spanning roles. That is, we take the view that a boundary-spanning role’s coordination modes may be similarly characterized as either routine, formal, and programmed (mechanical coordination mode) or nonroutine, informal, and ad hoc (human coordination mode). When considering the collection of tasks for any boundary-spanning role, we may assume that each boundary-spanning role uses both coordination modes. Thus, the issue is not one of exclusive reliance on one coordination mode, but rather the comparative de gree of emphasis placed on each coordination mode during boundary-spanning role design. Moreover, the concurrency of mechanical and human coordination mode raises an interesting issue in today’s computing environment, where electronic exchange is pervasive if not dominant. As electronic exchange represents an increasing share of total exchange, there may be an increasing comparative emphasis placed on mechanical coordination modes over human coordination modes. In sum, there is a probable shift away from widely ranged legitimate discretion and toward highly speci fied role prescriptions. Therefore, greater uniformity and consistency in the boundary roles’conduct should result, which should weigh favorably for performance outcomes.

This argument is consistent with some empirical findings. For example, Riggins and Mukhopadhyay [90] determined that participants’ level of integration was sig nificantly associated with the sponsor’s ability to realize an expected reduction in message (transaction)-handling errors, suggesting that the sponsor’s realized EDI ad vantages are interdependent with how trading partners choose to implement EDI. Srinivasan et al. [96] found that EDI’s integration with internal systems was associ ated with lower shipping discrepancies. Interestingly, they found a pronounced effect for exchange relationships that are characterized as complex. Thus the empirical evi dence is consistent with others’ view that suboptimal interface integration restrains expected EDI performance advantages [22, 41, 48, 77, 86, 87, 90, 96, 98, 110].

During implementation of electronic exchange systems, organizations must con vert human coordination modes into mechanical coordination modes. For example, rather than relying on human procedure to transcribe data from an external source document into an internal database, computer programs map data elements between external and internal formats. In addition, various control procedures are automated through computer programs rather than performed through human activity [39, 76]. Human coordination modes may consist of decision rules, manual procedures, and policies that guide task execution. The conversion to mechanical coordination modes requires that these decision rules, manual procedures, and policies be prescribed as computer programs [97]. This is a complex endeavor. Moreover, the implementation of electronic exchange systems is subject to a myriad of technical, financial, and organizational constraints in practice. Thus, we assume that the complexity and constraints cause organizations to vary in their ability to implement interface integration as they replace human coordination modes with mechanical ones.

Because we assume that EDI is ubiquitous and may be imposed on organizations, we view management’s use of EDI as inevitable and not wholly controllable. Consequently, we deem any decisions regarding EDI use (intensity) as extraneous. How ever, provided that earlier findings show an observed relationship between EDI use and performance outcomes [18, 55, 74, 88, 106], we relegate EDI use as a control variable in order to more precisely isolate the association between interface integration and performance outcomes.

In summary, we take the view that a boundary-spanning role concurrently relies on routine, formal, and programmed (mechanical coordination mode) and nonroutine, informal, and ad hoc (human coordination mode) coordination modes. The relative reliance on mechanical and human coordination modes is a critical boundary-spanning role design issue. As EDI represents an increasing share of total exchange, there is likely to be an increasing comparative reliance on mechanical coordination modes over human ones, when the technical, financial, and organizational constraints are effectively managed. If high interface integration is established, then greater unifor mity and consistency in the boundary roles’ conduct should result and weigh favor ably for performance outcomes. Thus, we submit the following general proposition, and follow with more specific derivations of it.

Proposition 1: Interface integration and performance outcomes are significantly associated, after controlling for EDI use intensity.

Performance Outcomes. Some conceptual works have suggested that EDI may lead to favorable performance outcomes in terms of operational procedure or strategic position [13, 53, 67, 73, 78, 79, 95, 98]. However, any strategic advantage may be short-lived, since EDI becomes a competitive necessity after it diffuses widely within an industry [11]. Moreover, in many industries EDI is deliberately employed in a cooperative or collaborative manner, rather than a competitive one [22, 28, 57, 59, 92]. Among these industries is healthcare [24], which interfaces with the Group In surance industry as defined here [89]. Where EDI implementation proceeds in a cooperative or collaborative manner, it is less likely that firms will use the technology to improve their competitive position vis-à-vis their trading partners. Instead, they are more likely to focus on improving operational procedures for the betterment of all involved [109]. Thus we focus on performance outcomes that are related to opera tional procedures, which may be characterized as efficiency-related or effectiveness related [51, 69, 106].

Our efficiency-related performance outcome variables are a ratio of input over output units. As in any industry, input units may be conceptually divided into capital and labor. In a service industry like Group Insurance, we expect that capital input unit consist largely of investments in information technology. Regarding labor input units, we may conceptually distinguish between the administrative labor that is involved in the organization’s operations, and the managerial or professional labor that is in volved in planning and control decisions. A substitution effect of capital for adminis trative labor occurs when EDI is implemented to supplant manual tasks such as data entry and error detection. In the Group Insurance industry, for example, the data entry task for electronic claims may be alleviated altogether by shifting this task to the healthcare provider. Also, claim adjudication may be more fully automated by com puter programs that apply adjudication decision rules to, and generate payment disbursements for, electronic claims. Because EDI may create a substitution effect for administrative labor inputs under conditions of high interface integration, we would expect to find a negative association between interface integration and administrative employees [77].

Proposition 1a: Interface integration and administrative employees are signifi cantly negatively associated, after controlling for EDI use intensity.

Regarding the impacts on professional labor, we note that EDI is expected to lead to quality improvements in data and data handling abilities [55, 89, 97]. This premise is grounded in recognition that electronic data can be processed faster and more accurately for informational purposes. More specifically, in characterizing processing as moving, verifying, formatting, or synthesizing activities, we argue that processing activities can be performed faster and more accurately when EDI is implemented with high interface integration. EDI data that flow seamlessly into internal systems will require less time to get the data into an accessible and verifiable state or useable form and format. Consequently, professional employees may spend less time and effort in processing data into useful information for decision-making purposes. Thus, we would expect to find a negative association between interface integration and professional employees.

Proposition 1b: Interface integration and professional employees are signifi cantly negatively associated, after controlling for EDI use intensity.

Our characterization of effectiveness-related outcomes is related to customers’per ceptions of service quality, such as how fast or accurately a Group Insurer performs its processes. Because EDI is generally accepted to speed up cycle times and lessen the vulnerability to error [30, 50, 79, 95, 97], we may expect that EDI will lead to improvements in service quality. For example, the provider or member may perceive greater effectiveness if fewer claims are paid in error or if fewer days are required to pay a claim. Thus we would expect to find a negative association between interface integration and claim error rate or claim payment time.

Proposition 1c: Interface integration and claim error rate are significantly nega tively associated, after controlling for EDI use intensity.

Proposition 1d: Interface integration and claim payment time are significantl negatively associated, after controlling for EDI use intensity.

## Internal Integration

Several researchers have suggested that internal systems integration may be related to effective EDI use [17, 41, 43, 48, 68, 96]. Among the first to suggest this, Hart and Estrin [41] stated:

We also found that effective use of computer networks for exchanging informa tion between firms is related to the extent of internal computing integration within firms. (p. 372) (italics ours)

McGee [68] was a second early observer, and he wrote:

If change is limited strictly to what occurs at the interface (increased interface integration), we have not obtained any higher level of inter-organizational integration than was present without the technology. (p. 188)

Moreover, Srinivasan et al. [96] suggested that internal integration may be an im portant control variable in EDI empirical studies in order to more precisely isolate performance impacts. They stated that internal integration “remains a source of unobserved heterogeneity” (p. 1295). Implicit in their suggestion for improving methodological rigor is some conjecture regarding internal integration’s influence on EDI performance impacts. Finally, arguing that EDI efficiency advantages are directly related to trading partners’ internal integration, Hart and Saunders [43] write:

Without [internal] integration, the potential efficiencies related to shortening the time required to exchange information are substantially reduced because slower conventional information-processing capacities have to be maintained once the information reaches the other firm. (p. 92)

These observations beg the question of how internal systems integration may af fect performance outcomes related to EDI. We proceed to address this question through inductive reasoning. We first identify three functionally interdependent sub units that are common to Group Insurers, and a (business) process that requires co ordination activity among them. Next, we compare and contrast how this process may occur in an electronic exchange environment under conditions of low and high internal integration.

The three subunits are enrollment, eligibility, and claims administration, which makeup a Group Insurer’s customer administration area. These subunits are generally organized as autonomous areas, and there exists substantive task interdependence for some business processes. Because these subunits have task interdependence, they require coordination and have data sharing requirements. Thus, each subunit is de pendent on its own and others’ internal systems, although each internal system is controlled through policy and procedure by one subunit. Regarding the five transac tion types, each is linked with at least one subunit’s internal systems, and the collective forms the core of interorganizational transaction processing for the customer administration area’s subunits.

The business process that we use for inductive reasoning is claim adjudication. The claim adjudication process begins with a treatment episode between a group member and a provider. Subsequently, the treatment episode generates a claim transaction, which must be adjudicated in order to determine payment disbursements. The payment disbursements are computed from data that originate from all subunits—from claims administration for data about the claim, including the date of treatment episode and the specific medical services rendered; from enrollment for data about the group member’s enrollment standing, including enrollment status at time of treatment episode and the group member’s annual deductible limit and cumulative deductible amount; from eligibility for data about the coverage terms, including identification of the kinds and amounts of specific medical procedures covered under the group plan’s contract. Thus, the claim adjudication process patently requires coordination among all three subunits, and underscores their data sharing requirements.

Figure 1 illustrates a Group Insurer that operates under conditions of low internal integration. In this scenario, the internal systems inhere design features that retard, mitigate, and reduce coordinating potential. For example, the format of shared data items may vary, or different coding schemes for the same datum (field) could be employed. Or, differences in the timing of transactional records for master record update may cause data discrepancies. These are just three examples among many that give rise to design differences among internal systems in practice. On a con ceptual level, these design differences lead to added coordination costs that work ers incur as they perform interdependent tasks pursuant to collective process execution.

Figure 1 also illustrates the transmission of data between the organization and its task environment via EDI. These data are initially stored on some magnetic device.<sup>8</sup> Subsequently, the data are merged into the internal systems by a boundary-spanning role, which consists of mechanical coordination modes and human coordination modes. We assume that the organization attempts to use mechanical coordination modes to the extent that such procedures are technically, financially, and organizationally fea sible. Under assumptions of low internal integration, however, the boundary-spanning roles must be tailored or specialized for each subunit’s internal systems.

Figure 2 illustrates a Group Insurer that operates under conditions of high internal integration. In this scenario, we assume that the internal systems inhere design fea tures that promote, advance, and further coordinating potential. For example, the data may be uniform in content and meaning across all internal systems. In this scenario, the boundary-spanning roles require less tailoring or specializing to each subunit’s internal systems, yielding a relatively unitary and standardized boundary-spanning role for all subunits. Assuming that an organization has limited resources to implement EDI, and noting the fact that implementing highly integrated EDI is expensive [15, 48, 77, 90], we stress an important, yet uncomplicated, logical conclusion—the specification, design, and programming of one boundary-spanning role with a com parative emphasis on mechanical coordination modes may yield higher interface in tegration than would the specification, design, and programming of three. Although we do not preclude the possibility that an organization with low internal integration may successfully implement highly integrated EDI systems, we argue that this is less likely from a conceptual perspective.

In summary, some support the view that internal systems integration plays a role for realizing performance outcomes related to EDI. However, the issue remains largely the by-product of exploratory case studies and anecdotes. Through inductive reasoning, we compare and contrast process performance and EDI implementation under conditions of low and high internal integration in order to elucidate the internal systems’ role in an electronic exchange environment. We argue that high internal integration may create a propensity to establish high interface integration, because fewer specialized boundary-spanning roles need to be (re)designed upon EDI introduction. This may be particularly so in light of the facts that attaining high interface integration is expensive, and that organizations are generally resource-constrained. Thus, we submit the following proposition:

![](/api/attachments/KM6K9UYU/fulltext/images/08fed49d9ea1f19e5d888171cc4959a472cb2948409720807a658624d9eda33d.jpg)  
Figure 1. Low Internal Integration

![](/api/attachments/KM6K9UYU/fulltext/images/adafc64fcacf4a346e7d3d2f99251ce39f5f5ead3d31c0e6410ab5c3aef2382e.jpg)  
Figure 2. High Internal Integration

Proposition 2: Internal integration and interface integration are positively associated.

## Method

WE DISCUSS METHODOLOGICAL CONCERNS in three sections, including variables, data sources, and reliability and validity test results.

## Variables

We address EDI use intensity and interface integration first, followed by internal integration and performance outcomes. Table 1 shows a summary of all variables.

## EDI Use Intensity and Interface Integration Variables

Preliminary interviews with informed subjects and pretesting indicated that respondents’ assessment of EDI use intensity and interface integration would be most accurate at the transaction type level, because the planning and control of EDI projects are organized by transaction type. Moreover, others have suggested that EDI use inten sity and interface integration may vary across transaction types within an organization [73], which is consistent with other empirical data [88]. Therefore, we concluded that the data for EDI use intensity and interface integration should be collected for each transaction type. We aggregate across the transaction types to operationalize EDI use intensity and interface integration of the technology cluster at the subunit level of analysis.

EDI Use Intensity Variable. We identified our five transaction types from industry literature and through survey instrument pretest. Respondents were instructed to indicate the percentage of data exchange volume facilitated by each transaction type— referred to as electronic exchange volume. To derive the technology cluster variable for EDI volume, we compute the average electronic exchange volume across the five transaction types. For the technology cluster variable for EDI diversity, we count the number of transaction types with electronic exchange volumes greater than or equal to 1 percent. Refer to Table 2 for several hypothetical examples.

Interface Integration Variable. For interface integration, we collected two Likertscale measures for each transaction type. The first measure is a narrow or partial characterization, and asked the respondent to characterize how the data are merged with internal systems’ data in terms of manual versus automated procedure. The second measure is a broad or global characterization, and asked for respondents general assessment of interface integration. The technology cluster variable for in terface integration is computed by averaging the second measure across the five transaction types.

## Internal Integration Variable

In measuring internal integration, we conceptually distinguish between the level of integration among the internal systems within each subunit and between each pairwise combination of subunits. Provided that three subunits are included here, this yields three within-subunit measures and three between-subunits measures, rendering six measures in total. (Refer to Figure 3.)

Table 1. Variable Summary

<table><tr><td rowspan="2">Variable</td><td colspan="2">Reliability</td><td>Validity</td></tr><tr><td>Cronbach&#x27;s α</td><td>Items</td><td>Pearson&#x27;s r</td></tr><tr><td colspan="4">EDI Use Intensity</td></tr><tr><td>EDI Volume: Percentage of total exchange volume for the technology cluster</td><td>Objective Measure</td><td></td><td>0.27b</td></tr><tr><td>EDI Diversity: Count of the implemented transaction types for the technology cluster</td><td>Objective Measure</td><td></td><td>0.63**b</td></tr><tr><td colspan="4">Integration</td></tr><tr><td colspan="4">Interface Integration: The level of integration between each transaction type of the technology cluster and internal systems of specified subunits</td></tr><tr><td>ANSI #270</td><td>0.36a</td><td>2</td><td>—</td></tr><tr><td>ANSI #834</td><td>0.70a</td><td>2</td><td>—</td></tr><tr><td>ANSI #835</td><td>0.92a</td><td>2</td><td>—</td></tr><tr><td>ANSI #837</td><td>0.94a</td><td>2</td><td>—</td></tr><tr><td>ANSI #839</td><td>0.64a</td><td>2</td><td>—</td></tr><tr><td rowspan="4">Internal Integration: The level of integration among the internal systems of specified subunits</td><td rowspan="4">0.93a</td><td rowspan="4">6</td><td>0.61**c</td></tr><tr><td>0.48**c</td></tr><tr><td>0.24c</td></tr><tr><td>0.40**c</td></tr><tr><td colspan="4">Performance Outcomes</td></tr><tr><td>Professional Employees (Unadjusted): Number of FTE professional employees</td><td>Objective Measure</td><td></td><td>0.80**b</td></tr><tr><td>Administrative Employees (Unadjusted): Number of FTE administrative employees</td><td>Objective Measure</td><td></td><td>0.44**b</td></tr><tr><td>Claim Error Rate: Percentage of claims in error</td><td>Objective Measure</td><td></td><td>—</td></tr><tr><td>Claim Payment Time: The average number of days to process a claim</td><td>Objective Measure</td><td></td><td>0.82**d</td></tr><tr><td colspan="4">Organization Size</td></tr><tr><td>Premium Income: Annual premium income in millions of dollars</td><td>Objective Measure</td><td></td><td>0.99**d</td></tr><tr><td colspan="4">aInter-Item Reliability Test</td></tr><tr><td colspan="4">bConvergent Validity Test (correlation between respective measure and premium income measure)</td></tr><tr><td colspan="4">cConvergent Validity Test (correlation between respective measure and criterion measure)</td></tr><tr><td colspan="4">dConvergent Validity Test (correlation between respective measure and secondary data measure) **p&lt;0.01; *p&lt;0.05</td></tr></table>

Table 2. Technology Cluster Variables

<table><tr><td rowspan="2">Organizations</td><td colspan="5">Electronic Exchange Volume Measures</td><td colspan="2">Technology Cluster Variables</td></tr><tr><td>ANSI #270</td><td>ANSI #834</td><td>ANSI #835</td><td>ANSI #837</td><td>ANSI #839</td><td>EDI Volume</td><td>EDI Diversity</td></tr><tr><td>1</td><td>5%</td><td>5%</td><td>10%</td><td>0%</td><td>0%</td><td>20/5=4%</td><td>3</td></tr><tr><td>2</td><td>10%</td><td>10%</td><td>15%</td><td>15%</td><td>10%</td><td>60/5=12%</td><td>5</td></tr><tr><td>3</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0/5=0%</td><td>0</td></tr><tr><td>4</td><td>10%</td><td>10%</td><td>10%</td><td>10%</td><td>0%</td><td>40/5=8%</td><td>4</td></tr><tr><td colspan="6">Survey Data</td><td colspan="2">Aggregate Data</td></tr></table>

![](/api/attachments/KM6K9UYU/fulltext/images/5356f002ae2741a82832d099f0f65961d479c9e60369f2a8d796ba51c0a2d580.jpg)  
Figure 3. Internal Integration

Each of these measures is a difference score derived from two percentage-scale (ratio) items. The two items required the respondent to indicate the ideal (i.e., normative) and actual amount of integrated data elements as a percentage of all data elements. We define internal integration as 100 minus the absolute value of the difference between the ideal and actual figures. More formally,

$$
\text { Internal   Integration } = 1 0 0 - | \text { Ideal } - \text { Actual } |
$$

Thus the internal integration measure is a relative assessment sensitive to the theoretical notion that there are benefits and costs associated with internal integration [36].<sup>9</sup> We compute the average of the six internal integration measures to yield one internal integration variable at the subunit level of analysis.

## Performance Outcome Variables

Our efficiency measures include the number of professional full-time equivalent employees (Professional Employees) and administrative full-time equivalent em ployees (Administrative Employees). These measures are computed as a percentage of total employees, which was collected as a nominal figure. The percentage figures show respondents’ assessment of the proportion of total employees who perform professional and administrative roles.<sup>10</sup> We adjust Professional Employees and Ad ministrative Employees for organization size effects by dividing by annual premium income, producing Professional Employees (Adjusted) and Administrative Employees (Adjusted).

Our effectiveness measures include the percentage of claims in error (Claim Error Rate) and the time between claim receipt and claim payment disbursement (Claim Payment Time). The claim error rate is the amount of claim processing exceptions as a percentage of all claims processed, while claim payment time is the average numbe of days to process a claim.

## Data Sources

Primary and secondary data are used in this study, and all data are from the latter half of 1993. Primary data were collected through a survey instrument, which was distributed to 66 Group Insurance companies. Forty-eight organizations returned the sur vey, which represents a 73 percent response rate. The survey instrument is organized into three sections, including measures on EDI (Section 1), internal systems (Section 2), and performance outcomes (Section 3). Different respondents were asked to fill out each section in order to avoid the methodological problem of common-response bias [56], and we attempted to secure informed respondents, as suggested by Huber and Power [46]. Thus typical respondents included EDI project leaders (Section 1), IS subunit managers (Section 2), and customer administration area managers (Sec tion 3). Secondary data were obtained from LOMA<sup>11</sup> on some performance outcome measures. These data serve to conduct predictive validity tests, or to augment the primary data set. LOMA data have been used in previous studies [10, 40].

## Reliability and Validity

We address reliability tests for the integration variables first, and we follow with a discussion of validity tests. Table 1 shows a summary of reliability and validity test results.

## Reliability

For each transaction type, we collected a partial and a global assessment of interface integration. We computed Cronbach’s alpha on each pair. Two satisfied the 0.80 threshold level (#835, #837), but three did not (#834, #270, #839). Thus the reliability of these measures is suspect, and suggests that the notion of interface integration is a multidimensional concept of which the first measure captures only part. For lack of alternative measures, we chose the global measure for data analyses since this measure’s phrasing is more comprehensive in its characterization of the underlying construct. The six measures for relative internal integration are deemed reliable, with a 0.93 Cronbach a value.

## Validity

Validity assessment may proceed on qualitative (content validity) and quantitative (convergent validity) levels. Content validity may be established by verifying that the measures are representative of the variables. In order to establish content validity, we interviewed five current and former employees from different Group Insurers and two LOMA employees from the Group industry liaison role. The objectives were twofold: (1) to confirm that widely used transaction types were included, and (2) to confirm that the performance outcomes should be affected by EDI use.

The interviewees agreed that these five transaction types are significant in terms of prevailing usage patterns. Regarding the EDI’s causal influence on organization performance, we focused on direct rather than indirect effects. Although information technology has been credited for having both direct and indirect effects on organization performance [8, 64], indirect effects are generally operationalized through ag gregate performance measures, which may be overwhelmed by other factors [32, 106]. This requires control variables as part of the research design in order to more reliably detect causal relationships [74]. Provided that our research design included an organization unit of analysis coupled with survey methodology, a design imperative was to maintain a reasonable survey length. In order to lessen the need for control variables, we chose performance variables that are representative of direct effects. The interviewees agreed that these performance outcome variables should be directly affected by these five transaction types.

Convergent validity may be demonstrated through a measure’s association with other conceptually related measures that come from the same or a different study. Convergent validity may be tested through bivariate correlation analyses [56]. There fore we use Pearson’s correlation coefficient, since we have continuous scale mea sures (see Table 1).

Large organizations are typically early movers in the adoption of new technologies— a finding that has been consistently found for many innovations [93]. Thus we believe that large organizations are more likely to have implemented more transaction types and at greater electronic exchange volumes—patterns consistently found in other studies [6, 18, 60, 64, 107]. Consequently, we may expect to find that organization size<sup>12</sup> is positively correlated with EDI volume and EDI diversity. We would also expect that the number of professional and administrative employees would be positively related to organization size. We found that three of these four variables are positively correlated with premium income at the $p < 0 . 0 1$ significance level, which offers evidence of convergent validity for these three variables. Only EDI volume was not significantly re lated to premium income, although the association is in the expected direction.

We used four criterion measures (CM) to test for convergent validity of the internal integration variable. Presented below, these criterion measures were designed according to reasonable expectations that they are conceptually related to internal integration. Using a seven-point Likert scale, the respondent was asked to indicate the level of agreement to the following statements.

CM1: Data must be rekeyed, as it used and reused by different employees of customer administration.

CM2: The same data are often inconsistent in terms of format and meaning across different application systems of customer administration.

CM3: For at least some data fields, there are data standards imposed and en forced across most of the customer administration’s application systems.

CM4: A high percentage of all data fields residing in the customer administration’s application systems is assigned data standards.

Criterion measures 1 and 2 are reverse-coded to control for common-response bias, and are linearly transformed in order to provide expected positive correlation be tween each criterion measure and internal integration. We found that three criterion measures converged with the internal integration variable at $p < 0 . 0 1$ , which offers support for the validity of our internal integration variable.

Finally, using secondary data from LOMA, we found that our claim payment time variable converged with theirs at $p < 0 . 0 1$ . Although we have no secondary data nor alternative measure for claim error rate, it is noteworthy that it is positively associated with claim payment time at $p < 0 . 0 1$ . Claim errors as defined here will likely lead to delay in payment of claims.

## Results

THE MEAN, STANDARD DEVIATION, AND NUMBER OF CASES (n) for each variable are shown in Table 3. The varying n results from either no EDI use in the case of interface integration, or missing values in the case of the performance outcome variables. Missing values occur from either an inability to ascertain the data or an unwillingness to share confidential data. First-order correlations among all variables are shown in Table 4.

Thirteen organizations had zero electronic exchange volume on all five transaction types. Therefore we evaluate these organizations as zero on the EDI volume and diversity variables, since these are ratio-scale measures. For interface integration, which uses a subjective ordinal scale, no EDI use rendered any measurement of interface integration meaningless. Thus those organizations that use no EDI are excluded for testing the propositions.

## Proposition 1

Using hierarchical regression models for testing Proposition 1, we entered EDI volume and EDI diversity first, followed by interface integration. The $\mathbf { R } ^ { 2 } \Delta \mathbf { R } ^ { 2 } .$ , and the standardized coefficients (b ) are reported in Table 5. One of the $\mathbf { R } ^ { 2 } \Delta$ values for interface integration is significant at $p < 0 . 0 5$ , and a second at $p < 0 . 1 0 . ^ { 1 3 }$ Interface integration is significantly negatively related with administrative employees (adjusted) at $p < 0 . 0 5$ after controlling for EDI use intensity (Proposition 1a). This result shows that higher interface integration is associated with lower administrative employee staff ing at constant levels of EDI use. Also, interface integration is significantly negatively related with professional employees (adjusted) at $p < 0 . 1 0$ after controlling for EDI use intensity (Proposition 1b). This result shows that higher interface integration is associated with lower professional employee staffing at constant levels of EDI use. Interface integration accounts for 12 percent of the variance in Administrative Em ployees (Adjusted), and 11 percent of the variance in Professional Employees (Ad justed). Altogether, EDI use intensity and interface integration account for 23 percent of the variance in Administrative Employees (Adjusted), and 12 percent of the vari ance in Professional Employees (Adjusted). No significant results obtains for the claim error rate and claim payment time variables (Propositions 1c and 1d).

Table 3. Univariate Statistics

<table><tr><td>Variable</td><td>Mean</td><td>Standard Deviation</td><td>Number of Cases</td></tr><tr><td colspan="4">EDI Use Intensity</td></tr><tr><td>EDI Volume (%)</td><td>5.7</td><td>7.5</td><td>48</td></tr><tr><td>EDI Diversity (range: 0–5)</td><td>1.6</td><td>1.4</td><td>48</td></tr><tr><td colspan="4">Integration</td></tr><tr><td>Interface Integration (7-point Likert scale)</td><td>5.3</td><td>1.7</td><td>35</td></tr><tr><td>Internal Integration (%)</td><td>72.7</td><td>25.0</td><td>48</td></tr><tr><td colspan="4">Performance Outcomes</td></tr><tr><td>Professional Employees (Adjusted)</td><td>0.7</td><td>0.7</td><td>43</td></tr><tr><td>Administrative Employees (Adjusted)</td><td>1.0</td><td>1.4</td><td>43</td></tr><tr><td>Claim Error Rate (%)</td><td>2.6</td><td>1.9</td><td>28</td></tr><tr><td>Claim Payment Time (days)</td><td>12.1</td><td>14.8</td><td>35</td></tr><tr><td colspan="4">Organization Size</td></tr><tr><td>Premium Income (millions of U.S. dollars)</td><td>2024.4</td><td>3987.4</td><td>48</td></tr></table>

## Proposition 2

## Proposition 1

Table 4 reveals that the interface integration and internal integration variables are positively related a $p < 0 . 0 1$ . This result shows that as the integration between the EDI and internal systems increases, so does the integration among the internal systems. Thus, Proposition 2 is supported. Common-response bias is relegated as inconsequential here for two reasons. First, multiple respondents were relied on to provide data for each case. In most cases, an EDI project manager provided interface integration data and an IS subunit manager provided internal integration data. Second, different mea surement methods and scales were used for the two integration variables.

## Discussion

We organize our discussion by proposition.

We found mixed support for Proposition 1. Of the four performance outcome vari ables, Administrative Employees and Professional Employees are significantly related to interface integration after controlling for EDI use intensity. The direction of the significant findings is consistent with earlier theoretical arguments, which suggest that interface integration should be negatively associated with administrative and professional employees. Moreover, provided that EDI is generally transactional in nature, we would expect that EDI use intensity and interface integration would ac count for a larger share of the variance in administrative employees (23 percent) than in professional employees (12 percent). Our findings are consistent with this argu ment.<sup>14</sup>

Table 4. Bivariate Statistics

<table><tr><td>Variable</td><td>EDI Volume</td><td>EDI Diversity</td><td>Interface Integration</td><td>Internal Integration</td><td>Professional Employees (Adjusted)</td><td>Administrative Employees (Adjusted)</td><td>Claim Error Rate</td><td>Claim Payment Time</td></tr><tr><td>EDI Volume</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EDI Diversity</td><td>0.65**</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Interface Integration</td><td>-0.02</td><td>0.09</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Internal Integration</td><td>0.07</td><td>0.00</td><td>0.44**</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>Professional Employees</td><td>0.01</td><td>-0.01</td><td>-0.33</td><td>-0.01</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>Administrative Employees</td><td>0.15</td><td>-0.04</td><td>-0.37*</td><td>-0.04</td><td>0.53**</td><td>1.00</td><td></td><td></td></tr><tr><td>Claim Error Rate</td><td>-0.02</td><td>0.19</td><td>0.33</td><td>0.21</td><td>-0.27</td><td>-0.18</td><td>1.00</td><td></td></tr><tr><td>Claim Payment Time</td><td>0.08</td><td>0.17</td><td>0.15</td><td>0.01</td><td>-0.13</td><td>-0.09</td><td>0.75**</td><td>1.00</td></tr><tr><td>Premium Income</td><td>0.27</td><td>0.63**</td><td>0.05</td><td>-0.12</td><td>-0.09</td><td>-0.18</td><td>0.09</td><td>0.07</td></tr><tr><td colspan="9">**p&lt;0.01; *p&lt;0.05</td></tr></table>

Table 5. Multivariate Statistics

<table><tr><td>Proposition</td><td>Dependent Variable</td><td>Independent Variables</td><td> $R^2\Delta$ (Significance Level)</td><td> $R^2$ </td><td>Standardized Coefficient β</td></tr><tr><td rowspan="2">1a</td><td rowspan="2">Administrative Employees (Adjusted)</td><td>EDI Use Intensity (Control Variables)</td><td>0.11 (0.18)</td><td>0.11</td><td>0.25 (EDI Volume)</td></tr><tr><td>Interface Integration</td><td>0.12 (0.05)*</td><td>0.23</td><td>-0.34 (EDI Diversity)</td></tr><tr><td rowspan="2">1b</td><td rowspan="2">Professional Employees (Adjusted)</td><td>EDI Use Intensity (Control Variables)</td><td>0.01 (0.86)</td><td>0.01</td><td>0.01 (EDI Volume)</td></tr><tr><td>Interface Integration</td><td>0.11 (0.07)#</td><td>0.12</td><td>-0.08 (EDI Diversity)</td></tr><tr><td rowspan="2">1c</td><td rowspan="2">Claim Error Rate</td><td>EDI Use Intensity (Control Variables)</td><td>0.05 (0.58)</td><td>0.05</td><td>-0.07 (EDI Volume)</td></tr><tr><td>Interface Integration</td><td>0.09 (0.15)</td><td>0.14</td><td>0.19 (EDI Diversity)</td></tr><tr><td rowspan="2">1d</td><td rowspan="2">Claim Payment Time</td><td>EDI Use Intensity (Control Variables)</td><td>0.10 (0.24)</td><td>0.10</td><td>-0.02 (EDI Volume)</td></tr><tr><td>Interface Integration</td><td>0.01 (0.63)</td><td>0.11</td><td>0.31 (EDI Diversity)</td></tr><tr><td colspan="6">** p&lt;0.01; * p&lt;0.05; # p&lt;0.10</td></tr></table>

These findings suggest that, at constant levels of EDI use intensity, integrated data flows between EDI and internal systems may yield some labor displacement effects. Thus these findings provide moderate support for the premise that interface integration is an important consideration during EDI implementation, which offers additional empirical support for previous theoretical and conceptual works. Consequently, it may be advisable that management’s tactical disposition lend keen at tention to how well the EDI and internal systems are integrated, regardless of how intensively the organization uses (or plans to use) EDI. This finding is significant for two reasons.

First, it argues against a stage model approach to EDI implementation as observed by some, where each successive stage is characterized by increasing levels of interface integration [48, 58, 98]. For example, Swatman et al. [98] present a descriptive model that shows organizations progressing through four stages of EDI implementation. At the first stage virtually no integration exists upon initial EDI adoption, while the last stage is characterized as highly integrated or tightly coupled application-level linkage. Many organizations begin with low interface integra tion levels and proceed through successive stages characterized by increasing integration levels. Even though the stage model approach is not intended as prescriptive, its prescriptive use has not been precluded. Our findings suggest that the stage model should not be accepted as a prescriptive framework, and that organizations may want to implement highly integrated EDI systems at the onset of their use.

Second, because the integration of EDI with internal systems is complex and costly, and has implications for trading partners’ performance advantages [43, 90], planning is critically important for guiding EDI implementation. However, Bjørn-Andersen and Krcmar [13] found that the amount and kind of planning efforts vary across organizations. Others have intimated that EDI implementation occurs with no, little, or only marginal planning effort [49, 51, 98]. Where planning does occur, Stern and Kauffman [97] suggest that greater satisfaction outcomes obtain when the business side, as well as technical side, is represented during planning efforts. Thus, under conditions of technical complexity, financial burden, and interorganizational process interdependence, the importance of tactical planning with broad functional representation becomes paramount. These findings suggest that tactical planning may beneficially focus on the means by which high interface integration will be obtained. Although integrating EDI with internal systems may be intuitively obvious, it nonetheless guards against overly optimistic and simplistic statements, which ostensibly suggest that greater EDI use will impact performance outcomes by ignoring interface design issues altogether [11, 88]. Our findings suggest that interface design issues should not be ignored or disregarded, but rather included as a centra aspect of EDI planning.

Although we believe that our theoretical arguments regarding claim error rate and claim payment are valid, we offer an explanation for the unsupportive findings. Existing literature suggests that organizations may experience significant learning effects when implementing EDI [63, 72, 90]. In addition, Hart and Saunders [42] remark that task complexity may cause interface integration to vary considerably, while Mackay [64] mentioned that inconsistent operating procedures across trading partners rendered the integration of EDI with internal systems even more difficult. Because the claims adjudication process is complex and (probably) nonuniform in execution, the complete and accurate modeling of manual decision rules may remain elusive prior to EDI implementation. Thus dyadic trading partners may have to pursue joint cooperative and corrective action, which may take on an iterative nature over time as problems continually emerge.<sup>15</sup> This view is consistent with Ring and Van De Ven’s [91] more general analytic perspective, which characterizes interorganizational relationship development as a long-term and cyclic process that must mediate inevitable conflict and changing expectations. Consequently, any organization should expect to engage in a long-term and cyclic process with trading partners as they proceed with EDI implementation.

Because organizations may experience postimplementation learning effects, we may aptly characterize EDI implementation as a refining period during which complications with new automated decision rules are detected and corrected [71]. On a con ceptual level, as the human coordination modes are supplanted by mechanical ones, improvements in the effectiveness and efficiency of error detection and correction may be attainable due to the advantages that computer programs and electronic data offer over human procedure and paper-based data. Drawing on Zuboff’s [111] notion of “informatting,” we argue that the computer programs that are the mechanical coordination modes allow for expanded monitoring and auditing capabilities within rea sonable cost-effective bounds vis-à-vis the alternative human coordination modes. This expansion may include invocation of additional or enhancement to existing data integrity constraints exercised at the boundary, creating long-run improvements in processing abilities compared to what could be attained through exclusive reliance on human procedure and paper-based data alone.

Thus, although we continue to believe that reductions in claim error rates and claim payment times are practically attainable in this industry, it may be that our data collection coincided with a period of short-term performance degradation. In the long run, these performance advantages may be forthcoming as well, and may exact improvements beyond what could be obtained through exclusive reliance on human procedure alone. This argument is consistent with Chatfield and Bjørn-Andersen’s [21] suggestion that “Over time, as [EDI] became more fully integrated with internal IT . . . JAL learned new capabilities by which it shared proprietary and strategic information and knowledge” (p. 31) (italics ours).

## Proposition 2

We found support for Proposition 2. Interface integration and internal integration are significantly and positively related. Besides the theoretical explanation provided ear lier, other supportive explanations came forward during followup interviews with respondents. First, because data standard imposition is a necessary condition for EDI adoption, an organization may concurrently adopt the EDI (external) data standard as its own internal data standard. This removes much of the need for translation as data move between the EDI and internal systems. This explanation resonates with Kreuwels’s [58] suggestion that, in discussing EDI’s structural impacts, internal systems development effort should be guided by consideration of electronic inter organizational exchange requirements so as to minimize translation needs. Because political forces may prevail against internal integration as a goal unto itself [36], EDI implementation may act to propel internal integration to the extent that internal data standards can be institutionalized only through external data standard adoption.

A second explanation is that the relationship between interface integration and internal integration may be spurious in that other factors affect both. For example, IS managers, who acknowledge the benefits of and strive for internal integration, may be predisposed to strive for interface integration. In addition, the IS staff’s skills and knowledge, which are gained through increasing internal integration, may be applicable to enhancing interface integration, or vice versa. Therefore IS staff’s learning gained through one set of efforts may be readily applied to a second set when both are directed toward the same objective—enhancing integration.

Regarding its tactical disposition, IS management may want to carefully evaluate internal integration before or at the onset of EDI implementation. In light of Riggins and Mukhopadhyay’s [90] suggestion that research might beneficially identify EDI risk factors, we suggest that internal integration may qualify as one. If high internal integration exists, then management is made aware of a relative proclivity to estab lish high interface integration. Since only one boundary role is required, optimal resource allocation may be reduced and high performance expectations may be set. On the other hand, low internal integration may render high interface integration to be elusive. Resources may need to be dispersed across several boundary roles, internal systems may need to be redesigned before or concurrent to EDI implementation, or both. Regardless of the tactics decided on, optimal resource allocation may need to be expanded and performance expectations may need to be appropriately tempered.

## Propositions 1 and 2

The collective findings suggest that high internal integration may create a propensity for implementing high interface integration, and that interface integration may effect greater administrative labor efficiencies. Thus there may be an indirect rela tionship between internal integration and administrative labor, as well as an assumed direct relationship, when EDI is introduced into an organization’s computing envi ronment. Although our methods do not provide the means to conclusively show an indirect relationship, our results are consistent with the presence of one. Assuming that an indirect relationship exists, we find that the tactical arguments for promoting EDI use with high interface integration and for advancing internal integration be come intertwined. That is, attaining high internal integration may be warranted in consideration of future EDI use; concomitantly, current EDI use with low interface integration may offer a motivating rationale for enhancing internal integration. However, we offer this position with tempered advocacy, since the integration variables’ temporal causal order on a descriptive level remains an outstanding issue.

## Research Contributions and Limitations

Interestingly, arguments for advancing EDI implementation or internal integration begin to intersect with incentives for proceeding with enterprise-wide resource planning (ERP), strategic data planning (SDP), or business process redesign (BPR). ERP [25, 27] and SDP [35, 62] move an organization toward an organization-wide data architecture. An organization-wide data architecture has several implications, including the implementation of data standards, which effects a higher state of internal integration. Enhancing internal integration is often a difficult and elusive goal, how ever. For example, after finding SDP efforts lacking in some organizations, Goodhue et al. [35] propose that “data integration must be critical to the strategic goals of the organization, as perceived by top management” (p. 22). Provided the possible tendency to view IS strictly in operational terms and not as a strategic tool, however, senior management may be disinclined to commit resources for enhancing internal integration. However, to the extent that SDP or ERP is embraced as a strategic objec tive by senior management, then internal integration as a tactical goal assumes stat ure. Consequently, IS management’s arguments for proceeding with internal integration initiatives may carry greater force.

Regarding BPR, Clark and Stoddard [23] showed that both process and technology innovations are critical for obtaining dramatic performance improvements, while either alone provide only marginal performance improvement. Clark and Stoddard conclude that both technology and process innovations are essential for dramatic improvements, although rational decision-making may cause process innovation to succeed technology innovation in order to reduce potential resistance to change [11]. Even though Clark and Stoddard’s process innovation construct is not specifi cally related to our integration variables, in the context of EDI as BPR enabler, interface and internal integration often do assume prominent roles in process innovation. Thus we argue that to introduce EDI without concern for the integration issue is akin to pursuing the technology innovation without the complementary pro cess innovation.

WE BEGIN WITH A DISCUSSION OF RESEARCH CONTRIBUTIONS AND EXTENSIONS, and follow with identification of several limitations related to this study.

## Research Contributions and Extensions

We have offered theoretical elaboration on, and have demonstrated some empirical support for, a positive association between interface integration and performance outcomes at constant levels of EDI use intensity. Although some have suggested that analytic frameworks on EDI planning and implementation may differ contingent on the industry setting [24], in empirical research we would hope to replicate findings across industry settings. Thus, because other empirical studies have provided similar results in manufacturing settings and our setting is a service industry, we have added to the cumulative research on the hybrid, multilateral EDI type by replicating find ings in a substantively different research setting.

We have offered theoretical elaboration on, and have demonstrated empirical sup port for, a positive association between interface integration and internal integration. Previous empirical support has been largely limited to anecdotes, while some re searchers have been more rigorous by using the case study method [41, 68, 96]. Al though useful for theory generation and refinement, case study methods do not facilitate theory confirmation. Using survey methods, our study contributes by testing a proposition that remained empirically unconfirmed.

There are several possibilities for research extension. First, establishing any temporal causal order between interface and internal integration variables would be useful to practitioners. Since there are plausible explanations for either causal order, as re vealed in our discussion above, an empirical study that uses a longitudinal design would be beneficial toward gaining a fuller understanding of this complex relationship. Second, the possibility that interface integration may mediate the relationship between internal integration and performance outcomes remains an outstanding em pirical issue. An attempt to more fully elucidate the relationships among EDI use intensity, integration, and performance outcome variables might offer management additional understanding for formulating effective tactical plans.

Third, testing for interaction effects between EDI use intensity and integration on these or other performance outcome variables may provide useful insight into the prac tical aspects of managing EDI implementation. For example, detecting significant in teraction effects may offer greater weight to earlier suggestions regarding optimal resource allocation and performance expectation management. Finally, and in consideration for the Internet’s growing influence on organizations’ information technology infrastructure and application portfolio, it may be interesting to examine how to most effectively change over from EDI applications that use proprietary communication protocols to those that use the TCP/IP communications protocol. There are many aspects to this problem. Whether enhancement to existing EDI applications or their re tirement with introduction of new Internet-based EDI applications offers the most effective means is one of the general, though nonetheless important, aspects to address.

## Limitations

This study uses a cross-sectional design. Thus, the temporal causal order of inter face and internal integration is inconclusive. Although we suggest that an assess ment of internal integration may prudently precede EDI implementation, we offer this suggestion based on broader consideration of the qualitative research addressing this issue. We cannot prescribe—based solely on the empirical data presented here—that an assessment of internal integration should necessarily precede EDI’s introduction.

The cross-sectional design also leaves open the possibility for lagged effects between integration and performance outcomes. Moreover, to the extent they exist, lagged effects may be interpreted through two plausible explanations. For example, we emphasize that higher levels of interface integration may lead to greater performance outcomes (at constant levels of EDI use), because this explanation is consistent with what theory would predict. However, an alternative explanation, which is also consistent with our results, is equally plausible: It may be that greater performance outcomes free up or result in more resources, which may be (re)directed into creating greater integration levels.

The EDI use variables’ mean values are low, suggesting that EDI was not intensively used at the time of data collection, which is similar to other empirical data from the early 1990s [6, 15, 43, 51, 107]. These data suggest an embryonic state of EDI implementation, and possibly a highly fluid situation with respect to EDI perfor mance impacts. Thus, while we did have significant findings in the expected direction, it may be that performance outcomes are fully evident only after adaptation ha more fully played out.

We address the generalizability of these findings at three levels. First, our sample is limited to those Group Insurers that are members of LOMA. Although there is no evidence that LOMA members differ from all Group Insurers [40], without conclusive empirical support indicating otherwise it is not possible to rule out a selection bias among the companies of our sample. On a second level, we may address cross-industry generalizability. Our view of EDI as a technology cluster requires identification of multiple functionally related transaction types, which are specific to the Group Insur ance industry. If these findings are generalizable to other industries, one should be able to replicate them in other industries. This necessarily requires the identification of an altogether different set of transaction types, however. Although a theoretical argument for similar findings in different industries can be made, whether the practical implications of selecting an altogether different set of transaction types might affect the find ings remains to be seen. Thus, generalizing these findings to other industries should be exercised with caution. Finally, the generalizability issue may be raised at a third level. We stated earlier that a careful identification of EDI type is essential in order to prop erly bound the generalizability of these results, and we recommend that this study’s findings not be generalized beyond the hybrid, multilateral EDI type.

Although the general research question that we address is how to effectively integrate EDI with internal systems, we treat this question in a conceptual vein. We do not intend nor attempt to offer prescriptive guidance for enhancing interface or internal integration, which may require specialization by industry, application, or platform [49]. Thus our conclusions address the question in a general, but nonetheless widely applicable, sense.

## Conclusion

ALTHOUGH OUR FINDINGS, DISCUSSIONS, AND CONCLUSIONS ARE PRESENTED in an EDI context, we extend them to e-commerce as applied in the industrial sector. Because e-commerce applications occur in nearly all functional areas, industries, organization sizes, and locations today, and their use is growing, this paper is relevant to a broad, diverse, and expansive set of business interests. We offer the conclusions to those who represent these interests and confront the challenge of managing their organization’s information technology infrastructure and application portfolio in an environment distinguished by a standardized global data network—the Internet.

First, we conclude that management should actively incorporate and emphasize interface design issues during EDI planning. More specifically, tactical planning should centrally focus on interface integration at the beginning of EDI implementation, thereby departing from the stage-model approach that describes how organizations typically implement EDI in practice. Second, we conclude that management may want to con sider internal integration as a risk factor during EDI implementation. This suggests that management might prudently assess internal integration before proceeding with EDI implementation, because the ability to establish high interface integration may be inhibited or advanced by low or high internal integration, respectively. In either case anticipation of the propensity to implement EDI with high interface integration may inform several planning decisions, including those related to resource allocation and performance expectation management.

Acknowledgments: The author wishes to thank Hank Lucas, Jon Turner, and Jack Baroudi for their helpful comments throughout the conduct of this research project. In addition, Jim Huffman of LOMA deserves recognition for his support during data collection.

## NOTES

1. In many cases we use the term EDI in lieu of e-commerce because our empirical data specifically pertain to EDI applications.

2. The first question is addressed in Truman [102].

3. We contrast the Group Insurance and Personal Insurance industries on four criteria that reveal substantive differences. First, Group Insurance includes primarily medical, disability, and dental insurance services, whereas Personal Insurance includes primarily life, home, and auto insurance services. Thus the product content is different. Second, although some insurance companies offer both Group and Personal Insurance services, the share of premium income generated by each varies widely across insurance companies. Moreover, some insurance companies offer either Group or Personal Insurance services. Thus the producers are different. Third, all insurance services are distributed through agents, who may be classified as either exclusive agents or brokerage agents. Group Insurance is typically distributed through exclusive agents, while Personal Insurance is typically distributed through brokerage agents. Consequently, the distribution channels are different. Fourth, Group Insurance services are contracted by private corporations and public entities to cover their employees. In contrast, Personal Insurance services are contracted directly by individuals. Thus the contractors (or consumers) are different. Collectively, these differences in terms of product content, producers, distribution channel, and consumers offer evidence of markedly different industries. Therefore we argue that the “insurance industry” is not an adequately precise characterization as a single industry, and we suggest that there are two insurance-related industries.

4. The technical dimension includes those environmental entities that engage the organization in exchange activities in order to enhance its economic viability. The institutional dimension includes those environmental entities that contribute to an organization’s legitimacy in order to enhance its social and political viability.

5. We collected data from the same subunit across all organizations, therefore there is no variance in subunit task characteristics.

6. We suggest that breadth and volume are two operationalizationsof a like facet—reflecting the participant’s penetration of electronic exchange with its task environment. The breadth and volume measures would be highly correlated, thus the value of importing both breadth and volume facets into an empirical study is conceivably negligible. Consequently, breadth is not incorporated here as a measured component of EDI use.

7. The external representation function relates to how an organization responds to environmental influences.

8. Many organizations design controls in order to monitor these transmissions, and to de rive operational or business activity measures of a transactional nature in some cases.

9. The theoretical underpinnings for and practical implications of using a relative measurement method for internal integration are presented in Truman [103].

10. The number and variety of job titles across organizations rendered specification of “professional” and “administrative” roles problematic.

11. Life Office Management Association (LOMA) provides research, education, and consulting services to the Group and Personal Insurance industries.

12. We use premium income as a surrogate for organization size. We are confident that our premium income measure is valid, because it converges with secondary data from LOMA at p < 0.01. These secondary data are collected by LOMA as part of a routine and continuing research program.

13. Due to the organization unit of analysis and a moderate sample size, we use a liberal significance level of p < 0.10.

14. The R<sup>2</sup> figures should be interpreted with caution because of multicolinearity between the EDI volume and EDI diversity variables. They are positively correlated at $\mathsf { p } < 0 . 0 1$ 1, thus the R<sup>2</sup> figures are inflated. However, our point rests on the comparison of these R<sup>2</sup> values, not their magnitude.

15. For example, NEIC—a third-party EDI service provider in the Group Insurance industry, conducts a certification program whereby a trading partner’s data are continually monitored and reviewed for the purpose of improving data integrity. Intended as temporary, a certification period starts when a trading partner joins NEIC’s network. However, the certification period varies greatly, which suggests variation in trading partners’ ability to transmit error-free data. Moreover, the certification period may restart if data integrity significantly degrades.

## REFERENCES

1. Aldrich, H.E., and Herker, D. Boundary spanning roles and organization structure. Acad emy of Management Review, 2 (April 1977), 217–230.

2. Aldrich, H.E., and Mindlin, S. Uncertainty and dependence: two perspectives on envi ronment. Organizations and Environment. Beverly Hills, CA: Sage Publications, Inc., 1978.

3. Bakos, J.Y. Information links and electronic marketplaces: the role of interorganizationa information systems in vertical markets. Journal of Management Information Systems, 8, 2 (Fall 1991), 31–52.

4. Bakos, J.Y., and Nault, B.R. Ownership and investment in electronic networks. Information Systems Research, 8, 4 (December 1997), 321–341.

5. Bakos, J.Y., and Treacy, M.E. Information technology and corporate strategy: a research perspective. MIS Quarterly, 10, 2 (June 1986), 107–119.

6. Banerjee, S., and Golhar, D.Y. Electronic data interchange: characteristics of users and nonusers. Information and Management, 26 (1994), 65–74.

7. Barrett, S., and Konsynski, B. Inter-organization information sharing systems. MIS Quarterly, Special Issue (1982), 93–105.

8. Barua, A.; Kriebel, C.H.; and Mukhopadhyay, T. Information technologies and business value: an analytic and empirical investigation. Information Systems Research, 6, 1 (March 1995), 3–23.

9. Bellman, S.; Lohse, G.L.; and Johnson, E.J. Predictors of online buying behavior. Com munications of the ACM, 42, 12 (December 1999), 32–38.

10. Bender, D.H. Financial impact of information processing. Journal of Management Infor mation Systems, 3, 2 (Fall 1986), 232–238.

11. Benjamin, R.I.; De Long, D.W.; and Scott-Morton, M.S. Electronic data interchange: how much competitive advantage? Long Range Planning, 23, 1 (1990), 29–40.

12. Bergeron, F., and Raymond, L. The advantages of electronic data interchange. Database (Fall 1992), 19–31.

13. Bjørn-Andersen, N., and Krcmar, H. Looking back—a cross-analysis of 14 EDI cases. In H. Krcmar, N. Bjørn-Andersen, and R. O’Callaghan (eds.), EDI in Europe. Chichester, UK: John Wiley & Sons, 1995.

14. Blili, S., and Raymond, L. Information technology: Threats and opportunities for small and medium-sized enterprises. International Journal of Information Management, 13 (December 1993), 439–448.

15. Bouchard, L. Decision criteria in the adoption of EDI. Proceedings of the Fourteenth International Conference on Information Systems, Orlando, Florida, December 1993.

16. Brown, W.B. Systems, boundaries, and information flow. Academy of Management Jour nal, 9 (1966), pp. 318–327.

17. Bytheway, A., and Braganza, A. Corporate information, EDI and logistics. Logistics Information Management, 5, 4 (1992), 10–18.

18. Carter, J.R., and Fredendall, L.D. The dollars and sense of electronic data interchange. Production and Inventory Management Journal, 2 (1990), 22–25.

19. Cash, J.I. Information systems: an information society opportunity or threat? The Information Society, 3, 3 (1985), 199–228.

20. Cash, J.I., and Konsynski, B.R. IS redraws competitive boundaries. Harvard Business Review (March–April 1985), 134–142.

21. Chatfield, T.A., and Bjørn-Andersen, N. The impact of IOS-enabled business process change on business outcomes. Journal of Management Information Systems, 14, 1 (Summer 1997), 13–40.

22. Choudhury, V. Strategic choices in the development of interorganizational information systems. Information Systems Research, 8, 1 (March 1997), 1–24.

23. Clark, T.H., and Stoddard, D.B. Interorganizational business process redesign: merging technological and process innovation. Journal of Management Information Systems, 13, 2 (Fal 1996), 9–28.

24. Clarke, R. A contingency model of EDI’s impact on industry sectors. Journal of Strategic Information Systems, 1, 3 (1992), 143–151.

25. Claymon, D. SAP’s worldview. Red Herring (November 1998), 6–10.

26. Cohn, L.; Brady, D.; and Welch, D. B2B: the hottest net bet yet? Business Week (January 17, 2000), 36–37.

27. Davenport, T.H. Putting the enterprise into the enterprise system. Harvard Business Review (July–August 1998), 121–131.

28. Dearing, B. The strategic benefits of EDI. Journal of Business Strategy (January–February 1990), 4–6.

29. Dill, W.R. Environment as an influence on managerial autonomy. Administrative Science Quarterly, 2 (March 1958), 409–443.

30. Emmelhainz, M.A. EDI: A Total Management Guide. New York: Van Nostrand Reinhold, 1990.

31. Fahey, L., and Narayanan, V.K. Conceptual overview: macroenvironmental analysis for strategic management. In Macroenvironmental Analysis, 1986, pp. 10–36.

32. Floyd, S.W., and Wooldridge, B. Path analysis of the relationship between competitive strategy, information technology, and financial performance. Journal of Management Information Systems, 7, 1 (Summer 1990), 47–64.

33. Fulk, J., and DeSanctis, G. Electronic communication and changing organizational forms. Organization Science, 6, 4 (July–August 1995), 337–348.

34. Galbraith, J.R. Organization Design. Reading, MA: Addison-Wesley, 1977.

35. Goodhue, D.L.; Kirsch, L.J.; Quillard, J.A.; and Wybo, M.D. Strategic data planning: lessons from the field. MIS Quarterly, 16, 1 (March 1992), 11–34.

36. Goodhue, D.L.; Wybo, M.D.; and Kirsch, L.J. The impact of data integration on the costs and benefits of information systems. MIS Quarterly, 16, 3 (September 1992), 293–310.

37. Gurbaxani, V., and Whang, S. The impact of information systems on organizations and markets. Communications of the ACM, 34, 1 (January 1991), 60–73.

38. Hansell, S. Keeping track of e-commerce. New York Times Special Report, September 22, 1999.

39. Hansen, J.V., and Hill, N.C. Control and audit of electronic data interchange. MIS Quarterly, 13, 4 (1989), 403–413.

40. Harris, S.E., and Katz, J.L. Organizational performance and information technology investment intensity in the insurance industry. Organization Science, 2, 3 (August 1991), 263–295.

41. Hart, P., and Estrin, D. Inter-organization networks, computer integration, and shifts in interdependence: the case of the semiconductor industry. ACM Transactions on Information Systems, 9, 4 (October 1991), 370–398.

42. Hart, P.J., and Saunders, C.S. Power and trust: critical factors in the adoption and use of electronic data interchange. Organization Science, 8, 1 (January–February 1997), 23–42.

43. Hart, P.J., and Saunders, C.S. Emerging electronic partnerships: antecedents and dimensions of EDI use from the suppliers’ perspective. Journal of Management Information Systems, 14, 4 (Spring 1998), 87–111.

44. Hickson, D. A convergence in organization theory. Administrative Science Quarterly, 2 (1966), 224–237.

45. Holand, C., and Lockett, A.G. Mixed mode network structures: the strategic use of electronic communication by organizations. Organization Science, 8, 5 (September–October 1997), 475–488.

46. Huber, G.P., and Power, D.J. Retrospective reports of strategic level managers: guidelines for increasing their accuracy. Strategic Management Journal, 5 (1985), 171–180.

47. Huggins, K., and Land, R.D. Operations of Life and Health Insurance Companies, 2d ed. Atlanta: Life Office Management Association, 1992.

48. Iacovou, C.L.; Benbasat, I.; and Dexter, A.S. Electronic data interchange and small organizations: adoption and impact of technology. MIS Quarterly, 19, 4 (December 1995), 465–485.

49. Jackson, G. Choosing a platform for EDI. EDI World (April 1994), 30–32.

50. Jelassi, T., and Figon, O. Competing through EDI at Brun Passot: achievements in France and ambitions for the single European market. MIS Quarterly, 18, 4 (December 1994), 337– 352.

51. Johnson, D.A.; Allen, B.J.; and Crum, M.R. The state of EDI usage in the motor carrier industry. Journal of Business Logistics, 13, 2 (1992), 43–68.

52. Johnston, H.R., and Carrico, S.R. Developing capabilities to use information strategi cally. MIS Quarterly, 12, 2 (June 1988), 153–165.

53. Johnston, H.R., and Vitale, M.R. Creating competitive advantage with interorganizationa information systems. MIS Quarterly, 12, 2 (June 1988), 153–165.

54. Keeney, R.L. The value of Internet commerce to the customer. Management Science, 45, 4 (April 1999), 533–542.

55. Kekre, S., and Mukhopadhyay, T. Impacts of electronic data interchange on quality improvement and inventory reduction programs. International Journal of Production Economics, 28 (1992), 265–282.

56. Kerlinger, F.N. Foundations of Behavioral Research, 3d ed. Chicago: Holt, Rinehart and Winston, 1986.

57. Konsynski, B., and McFarlan, W. Information partnerships—shared data, shared scale. Harvard Business Review (September–October 1990), 114–120.

58. Kreuwels, M.A. Electronic data interchange: An introduction and examples of its structural impact. Production Planning and Control, 3, 4 (1992), 381–392.

59. Kumar, K., and Van Dissel, H.G. Sustainable collaboration: Managing conflict and cooperation in interorganizational systems. MIS Quarterly, 20, 3 (September 1996), 279–300.

60. La Londe, B.J., and Emmelhainz, M.A. Electronic purchase order interchange. Journal of Purchasing and Materials Management (Fall 1985), 2–9.

61. Lawrence, P.R., and Lorsch, J.W. Organization and Environment: Managing Differentiation and Integration. Boston: Harvard Business School Press, 1967.

62. Lederer, A.L., and Sethi, V. Critical dimensions of strategic information systems plan ning. Decision Sciences, 22, 1 (Winter 1991), 104–119.

63. Lee, H.G.; Clark, T.; and Tam, K.Y. Research report: can EDI benefit adopters? Information Systems Research, 10, 2 (June 1999), 186–195.

64. Mackay, D.R. The impact of EDI on the components sector of the Australian automotive industry. Journal of Strategic Information Systems, 2, 3 (September 1993), 243–263.

65. Malone, T.W.; Yates, J.; and Benjamin, R.I. Electronic markets and electronic hierarchies. Communications of the ACM (June 1987), 484–497.

66. March, J.G., and Simon, H.A. Organizations. New York: John Wiley & Sons, 1958

tions: strategies and illustrative examples. MIS Quarterly, 20, 3 (September 1996), 331– 345.

68. McGee, J.V., Jr. Implementing Systems Across Boundaries: Dynamics of Information Technology and Integration.Ph.D. dissertation, Harvard University, 1991.

69. Meier, J., and Chismar, W.G. A formal model of the introduction of a vertical EDI system. Proceedings of the Hawaii International Conference on System Sciences, Koloa, Hawaii, January 1991.

70. Meyer, J.W., and Scott, W.R. Organizational Environments: Ritual and Rationality. Beverly Hills, CA: Sage Publications, Inc., 1983.

71. Monczka, R.M., and Carter, J.R. Implementing electronic data interchange. Journal of Purchasing and Materials Management (Summer 1988), 1–9.

72. Moynihan, J.J., and Kathryn, N. CHIN provides vital healthcare linkages. Healthcare Financial Management (January 1994), 59–64.

73. Mukhopadhyay, T. Assessing the economic impacts of electronic data interchange technology. In R.D. Banker, R.J. Kauffman, and M.A. Mahmood (eds.), Strategic Information Technology Management: Perspectives on Organizational Growth and Competitive Advantage. Harrisburg, PA: Idea Group Publishing, 1993, pp. 241–264.

74. Mukhopadhyay, T.; Kekre, S.; and Kalathur, S. Business value of information technol ogy: a study of electronic data interchange. MIS Quarterly, 19, 2 (June 1995), 137–156.

75. Nidumolu, S.R. The impact of interorganizational systems on the form and climate of sellerbuyer relationships: A structural equations modeling approach. Proceedings of the Tenth Interna tional Conference on Information Systems, Boston, December 1989, pp. 289–304.

76. Norris, D.M., and Waples, E. Control of Electronic Data Interchange Systems. Journal of Systems Management (March 1989), 21–25.

77. Nygaard-Andersen, S., and Bjørn-Andersen, N. To join or not to join: a framework for evaluating electronic data interchange systems. Journal of Strategic Information Systems, 3, 3 (September 1994), 191–210.

78. O’Callaghan, R.; Kaufmann, P.J.; and Konsynski, B.R. Adoption correlate and share effects of electronic data interchange systems in marketing channels. Journal of Marketing, 56 (April 1992), 45–56.

79. O’Callaghan, R., and Turner, J.A. Electronic data interchange—concepts and issues. In H. Krcmar, N. Bjørn-Andersen, and R. O’Callaghan (eds.), EDI in Europe. Chichester, UK: John Wiley & Sons, 1995.

80. Parsons, G.L. Information technology: a new competitive weapon. Sloan Management Review (Fall 1983), 3–14.

81. Pfeffer, J., and Salancik, G.R. The External Control of Organizations: A Resource Dependence Perspective. New York: Harper & Row Publishers, 1978.

82. Pinsonneault, A., and Kraemer, K.L. Middle management downsizing: an empirical investigation of the impact of information technology. Management Science, 43, 5 (May 1997), 659–679.

83. Porter, M.E. Competitive Strategy: Techniques for Analyzing Industries and Competitors, New York: Free Press, 1980.

84. Porter, M.E. Competitive Advantage. New York: Free Press, 1985.

85. Porter, M.E., and Miller, V.E. How information gives you competitive advantage. Harvard Business Review (July–August 1985), 149–160.

86. Premkumar, G., and Ramamurthy, K. The role of interorganizationaland organizational factors on the decision mode for adoption of interorganizational systems. Decision Sciences, 26, 3 (May–June 1995), 303–336.

87. Ramamurthy, K.; Premkumar, G.; and Crum, M.R. Organizational and interorganizational determinants of EDI diffusion and organizational performance: a causal model. Journal of Organizational Computing and Electronic Commerce, 9, 4 (1999), 253–285.

88. Raymond, L.; and Bergeron, F. EDI Success in small and medium-sized enterprises: a field study. Journal of Organizational Computing and Electronic Commerce, 6, 2 (1996), 161–172.

Krcmar, N. Bjørn-Andersen, and R. O’Callaghan (eds.), EDI in Europe. Chichester, UK: John Wiley & Sons, 1995.

90. Riggins, F.J., and Mukhopadhyay, T. Interdependent benefits from interorganizationa systems. Journal of Management Information Systems, 11, 2 (Fall 1994), 37–57.

91. Ring, P.S., and Van De Ven, A.H. Developmental processes of cooperative interorganizationalrelationships. Academy of Management Review, 19, 1 (1994), 90–118.

92. Rockart, J.F., and Short, J.E. Information technology in the 1990s: managing organizational interdependence. Sloan Management Review, 30, 2 (Winter 1989), 7–18.

93. Rogers, E.M. Diffusion of Innovations, 3d ed. New York: The Free Press, 1983.

94. Scott, W.R. Organizations: Rational, Natural and Open Systems. Englewood Cliffs, NJ: Prentice-Hall, 1987.

95. Senn, J.A. Electronic data interchange: the elements of implementation. Information Systems Management (Winter 1992), 45–53.

96. Srinivasan, K.; Kekre, S.; and Mukhopadhyay, T. Impact of electronic data interchange technology on JIT shipments. Management Science, 40, 10 (October 1994), 1291–1304.

97. Stern, L.W., and Kauffman, P.J. Electronic data interchange in selected consumer goods industries: An interorganizationalperspective. In R. Buzzell (ed.), Marketing in an Electronic Age. Boston: Harvard Business School Press, 1985.

98. Swatman, P.M.C.; Swatman, P.A.; and Fowler, D.C. A model of EDI integration and strategic business reengineering. Journal of Strategic Information Systems, 3, 1 (1994), 41–60.

99. Tedeschi, B. The Net’s real business happens .com to .com. New York Times, April 19, 1999.

100. Tedeschi, B. E-commerce report. New York Times, January 24, 2000.

101. Thompson, J.D. Organizations in Action. New York: McGraw-Hill Publishers, 1967.

102. Truman, G.E. An empirical appraisal of EDI implementation strategies. International Journal of Electronic Commerce, 2, 4 (Summer 1998), 43–70.

103. Truman, G.E. A discrepancy-basedmeasurement approach for data integration. Journal of Organizational Computing and Electronic Commerce, 8, 3 (1998), 169–193.

104. Tushman, M., and Nadler, D. Information processing as an integrating concept in organizational design. Academy of Management Review, 3 (July 1978), 613–624.

105. Van De Ven, A.; Delbecq, A.; and Koenig, R. Determinants of coordination modes within organizations. American Sociological Review, 41 (1976), 322–338.

106. Venkatraman, N., and Zaheer, A. Electronic integration and strategic advantage: a quasiexperimental study in the insurance industry. Information Systems Research, 1, 4 (December 1990), 377–393.

107. Vlosky, R.; Smith, P.M.; and Wilson, D.T. Electronic data interchange implementation strategies: a case study. Journal of Business and Industrial Marketing, 9, 4 (1994), 5–18.

108. Williamson, O.E. The Economic Institutions of Capitalism. New York: The Free Press, 1985.

109. Wrigley, C.D.; Wagenaar, R.W.; and Clarke, R.A. Electronic data interchange in international trade: frameworks for the strategic analysis of ocean port communities. Journal of Strategic Information Systems, 3, 3 (1994), 211–234.

110. Zaheer, A., and Venkatraman, N. Determinants of electronic integration in the insurance industry: an empirical test. Management Science, 40, 5 (May 1994), 549–566.

111. Zuboff, S. In the Age of the Smart Machine: The Future of Work and Power. New York: Basic Books, 1988.

112. Zwass, V. Electronic commerce: Structures and Issues. International Journal of Electronic Commerce, 1, 1 (Fall 1996), 3–23.

## Appendix

The ANSI Transaction Types

 ANSI 270: Includes data on pending provider services and member’s Group plan identification. These data are used to determine the eligibility of provider services according to the coverage terms of the Group plan. Coverage terms refer to the set of medical services that are fully or partially covered and reimbursable by the insurer to the provider. The coverage terms are uniform for all members within a Group plan, but the reimbursable amounts may vary according to other individual attributes, for example, paid cumulative annual deductible, coinsurance factors, etc. We refer to these data as eligibility data. The use of ANSI 270 (eligibility request) implies the use of ANSI 271 (eligibility response). Thus they are paired transaction types forming a bidirectional data flow between provider and insurer.

 ANSI 834: Identifies current members of a Group policy. Included in this transaction type are the member’s name, address, and demographic information such as age, marital status, dependents, etc. We refer to these data as enrollment data.

 ANSI 835: Includes data that may be classified into two parts—payment and advice. The payment specifies the reimbursable amount and the appropriate financial intermediary identification numbers. The advice specifies the outcome of the claim adjudication process that determines the reimbursable amount. The two parts are similar to a check and check stub of a payroll system, where the check specifies the pay period’s net payment along with financial intermediary information, and the check stub details the gross payment and deductions from which the net payment is computed. We refer to these data as claim payment data.

 ANSI 837: Includes data on one or more medical services or procedures rendered to the member by a provider. Medical supplies may also be included when used in the course of treatment procedure. Identification of member, member’s plan, provider, medical procedures, and associated service dates are included in this transaction type. We refer to these data as claim data.

 ANSI 839: Includes data regarding the status of a claim as it proceeds through the claim adjudication process. Lengthy and complex, the claim adjudication process involves successive stages lasting over several weeks. Providers, members, and insurers either require or want information regarding the claim adjudication process in order to take timely remedial action. We refer to these data as claim status data.
