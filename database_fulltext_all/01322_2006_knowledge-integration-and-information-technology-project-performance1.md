---
otero_id: 1322
otero_key: "WRGHMWN3"
title: "Knowledge Integration and Information Technology Project Performance1"
authors: "Victoria L. Mitchell"
year: "2006"
journal: "MIS Quarterly"
doi: "10.2307/25148759"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Knowledge Integration and Information Technology Project Performance
Author(s): Victoria L. Mitchell
Source: MIS Quarterly, Vol. 30, No. 4 (Dec., 2006), pp. 919-939
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/25148759
Accessed: 26-09-2015 04:01 UTC

## REFERENCES

Linked references are available on JSTOR for this article:
http://www.jstor.org/stable/25148759?seq=1&cid=pdf-reference#references\_tab\_contents

You may need to log in to JSTOR to access the linked references.

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# KNOWLEDGE INTEGRATION AND INFORMATION TECHNOLOGY PROJECT PERFORMANCE $^{1}$

By: Victoria L. Mitchell
University of Calgary
Calgary, Alberta T2N 1N4
CANADA
mitchelv@ucalgary.ca

Keywords: IT performance, MIS management, knowledge management, management structure, integrative capabilities, dynamic capabilities, project delay

## Abstract

Successful product and process design depends on management's ability to integrate fragmented pockets of specialized knowledge. This integrative capability has important implications for large-scale information technology projects. This article examines the relationship between timely project completion and two dimensions of management's integrative capability: access to external knowledge and internal knowledge integration. Measures of these two dimensions are used to predict on-time project completion, where completion is a function of the duration of IT-related project delays. In a longitudinal study of 74 enterprise application integration projects in the medical sector, integrative capability was measured from the point of view of the CIO and a facility IT manager. Accounting for several project controls, our Cox regression results indicate both integrative dimensions significantly mitigate the duration of IT-related project delays, thus promoting timely project completion. The analysis also reveals the importance of taking management structure into consideration when studying IT phenomena in networked organizations.

## Introduction

Estimating completion dates for information technology projects and bringing them in on time is tricky business. In 2001, Standish Group reported 49 percent of IT projects exceeded time and cost estimates, with an average time overrun of 63 percent. In 2002, Forrester Research Inc. reported IT project completion rates—regardless of time and cost overruns—of 67 percent, rates that were down from 72 percent in 1999. These low completion rates are amplified for short-term projects: completion of short-term projects (lasting less than a year) slipped from 58 percent in 1999 to 51 percent in 2002 (Johnson 2003). In 2003, Hackett Group reported similar completion rates for IT projects, with time overruns ranging between 24 and 100 percent (Perks 2003). In 2005, the “State of the CIO Survey” reported systems integration and the enhancement of business processes as the top technology priority for chief information officers (Varon and Ware 2005). A particularly troublesome integration project is that of enterprise application integration (EAI).

EAI projects are generally large-scale, enterprise-wide IT initiatives connecting business processes across multiple facilities and IT platforms. EAI is a means of system integration where facilities pass data between multiple legacy and newer systems through a single messaging hub, rather than build custom interfaces to link each system. Using a message broker as the underlying data transport mechanism, EAI tools parse, duplicate, or transform the data to present it in the requisite format for each idiosyncratic application that needs to receive the data. Companies typically purchase a central module and the specific interfaces they need, then contract for custom programming to build interfaces for proprietary applications. In doing so, they increase the speed of data transfer, reap cost savings, and gain greater flexibility with their business processes (Slater 2002). EAI allows users to define business process rules and makes data integration subject to those rules. Thus, the integration of operational rules with technical knowledge is critical to EAI success.

The time it takes to complete a large-scale EAI project—and even whether the project is completed—depends on a number of factors including the size of the project, prior project experience, user involvement, and the degree to which the firm possesses a set of organizational capabilities. One such capability is management's integrative capability. Integrative capability refers to an ability to integrate knowledge within and across organizational boundaries (Henderson 1994). It is analogous to the concept of architectural competence, coined by Henderson and Cockburn (1994) in their study of knowledge transfer in the design of new pharmaceutical products. Both studies demonstrated that research and development project performance was related to an ability to import new external knowledge and synthesize existing internal knowledge. They found that higher project performance was associated with knowledge transfer mechanisms that actively encouraged the exchange of information across organizational units and across organizational boundaries. Thus, a proportion of the variance in project performance across firms is attributed to the acquisition and integration of specialized knowledge, particularly when that knowledge is tacit or proprietary (Leonard-Barton 1992; Teece et al. 1997).

The purpose of our study is to examine the relationship between management's integrative capability and one aspect of EAI project performance: on-time project completion. More specifically, we seek answers to two questions: Can management's integrative capability improve the probability of on-time project completion by reducing the duration of IT delays? If so, which integrative dimensions are most important for predicting timely project completion? In order to address these questions, we refine Henderson's (1994) integrative capability dimensions (access to external knowledge and internal knowledge integration) to reflect an IT context. We develop measures of these two dimensions, and use the resulting instrument with telephone interviews to collect data on 75 EAI projects from CIOs and facility IT managers in the medical sector. We measure the duration of IT delay impeding EAI project completion as the time between the scheduled project completion date and the actual completion date. After validating our measurement scales, we develop two sets of Cox regression models (one from the CIO perspective, the other from the IT manager perspective) to examine the effect of management's integrative capability on the timeliness of EAI project completion. Controlling for project size, user involvement, and prior project experience, our results conclusively show that integrative capability is inversely related to the duration of IT delay forestalling timely project completion. We find that each integrative dimension—access to external knowledge and internal knowledge integration—is a significant predictor of on-time project completion; however, the reliability of internal knowledge integration as a predictor of timeliness is stronger from the CIO perspective than the IT manager perspective. While our project controls were also reliable predictors, one control variable, the intensity of user involvement, was significant from the IT manger perspective but not from the CIO perspective.

In the next section we use prior literature, primarily in new product development, IS development, and knowledge management, to develop our theoretical framework in the context of EAI projects. Subsequently, we provide details of our methodology, including instrument development, data collection, and validation of our measurement scales. Then we describe our statistical methods and report our regression results. Next we discuss our results, insights gained, and limitations. We conclude with a summary of our study and its managerial implications.

## Background Literature

## The EAI Context

EAI initiatives are typically large-scale systems integration projects that join disparate IT platforms and business processes across multiple facilities. Unfortunately, integrating the mass and complexity of enterprise applications with an application program interface (API) remains problematic. Few application architectures have published APIs needed to access their internal functions, and even if standard APIs are published, data semantics pose another problem in that some data transformations are almost always required to ensure data fields have consistent definitions, especially with differing data formats that originate in the different business units. There are several forms that differ in style (the way integration occurs—data synchronization, straight-through processing, or composed programs), mode (the rate of integration—batch, near real-time or real-time), domain (where the integration process occurs—within a business unit, between two units in the same enterprise, or between enterprises), and endpoints (the source and target being integrated—people, databases, applications, or devices) (Altman and Altman 2004). Adding to the complexity, each enterprise has its own technologies and interfaces that must also be integrated. EAI manages such design complexity with middleware (i.e., interface engines and a messaging standard) to coordinate the movement and exchange of information between applications and business processes. Although the goal of straight-through transaction processing for “seamless” business operations can be obtained technically (Chuang and Fusco 2003), the greater difficulty lies in amassing the combination of business and technical knowledge to bring such projects to completion.

Managing the integration of disparate IT platforms and business processes across a network of different facilities is a formidable challenge. According to a recent guideline promulgated by the Association for Project Management, "Efficient project management requires effective delegation that allows decisions to be made at a level that is consistent with the organization's system for internal control" (APM 2004). Large-scale projects generally require a two-tier, federal management structure to govern IT activities where the corporate office, facility IT units, and line management assume varying degrees of responsibility (Brown and Magill 1994).

For EAI projects in a networked organization, centralized corporate control permits the standardization necessary for integration of an IT infrastructure across facilities, with decentralized control of software at the facility level to permit flexibility in its use (DeSanctis and Jackson 1994). This is in contrast to a centralized structure where all IT activities are managed at the corporate level, and a decentralized structure where facility IT managers assume responsibility for all IT activities with little corporate oversight (Sambamurthy and Zmud 1999). Studies in project management, systems development, and new product development generally support a federal management approach, reporting that the strongest determinant of project timeliness is a cross-functional team with a strong project leader backed by a senior management sponsor (e.g., Cooper and Kleinschmidt 1994; Gupta and Wilemon 1990).

## Theoretical Framework

We approach the problem of timely EAI project completion from a systems perspective. We conceptualize IT platforms as a set of interrelated components, which are largely software applications. Each component (application) has a core design of its own, and the linkages among components give rise to a system architecture that supports distinct business processes.

The distinction between the system as a whole (the IT platform) and the system in its parts (individual applications) is important for understanding the knowledge requirements for EAI and the role of management's integrative capability. EAI is a form of architectural innovation $^{2}$ in that the focal point of change occurs in the linkages among component applications, while leaving each application's core design intact (Henderson and Clark 1990). Implementation of an architectural innovation requires an understanding of these linkages and how they impact performance of the larger system (the corporate enterprise). This understanding is contingent on the ability to import and integrate requisite technical and operational knowledge. The extent to which these activities are enacted is indicative of management's integrative capability and together with essential project competencies (e.g., prior project experience and user involvement) they determine the likelihood of timely EAI project completion.

## EAI Project Completion

IT project performance embodies two dimensions: product performance and process performance (Barki et al. 2001). Product performance refers to the quality of the project outcome or effectiveness of the installed system. In contrast, process performance refers to the quality of the development process – most notably effective planning and efficient implementation. A key indicator of process performance is on-time project completion for a given budget and set of specifications. We define project completion as the point at which implementation has concluded. On-time project completion is influenced by a number of risk factors including project size, lack of top management support, waning user involvement, lack of functional knowledge, and poor project planning (Cleland 2002; Schmidt et al. 2001). These factors are elements of performance risk and execution risk. Performance risk refers to the likelihood that performance outcomes are estimated inaccurately (Nidumolu 1995). Execution risk refers to the probability that project outcomes will be unsatisfactory (Wallace and Keil 2004). While performance risk affects the allocation of time for project completion, execution risk affects the utilization of time, forestalling completion.

![](/api/attachments/WRGHMWN3/fulltext/images/a94ff83b68545b3a8be16f2c55b650127347839f6e714c5bb71a4c1d55017b75.jpg)  
Figure 1. Factors Affecting EAI Project Completion

Performance risk and execution risk reflect the knowledge deficits impeding process performance. Where knowledge deficits exist, incomplete information and know-how give rise to uncertainties (Argote 1982) that obscure prediction and execution. Performance risk and execution risk are lowered through the knowledge transfer mechanisms developed to alleviate technical and operational uncertainties that cause estimation errors and IT-related project delays. Hence timely project completion largely depends on the knowledge transfer mechanisms that facilitate the importation and synthesis of information and know-how to reduce the execution and performance risk affecting EAI design and delivery. Using internal and external knowledge transfer mechanisms, the acquisition and integration of this knowledge is embodied in management's integrative capability (depicted in Figure 1).

## Integrative Capability

Drawing from the resource-based literature, prior research on dynamic capabilities and combinative capabilities provides insight into the relationship between management's integrative capability and timely EAI project completion. Dynamic capability refers to an ability to integrate, build, and reconfigure internal and external knowledge to respond to environmental change (Teece et al. 1997; Zollo and Winter 2002). Relating dynamic capability to innovation success, Galunic and Eisenhardt's (2001) study of modular corporate forms found that management's ability (its dynamic capability) to reconfigure division charters (an architectural innovation) was a critical factor in producing new, productive assets in a dynamic market. Thomas (1996) reports in his longitudinal study of 200 industries that an industry's knowledge base, and management's ability to enact change based on that knowledge, was a key determinant of innovation success. Kogut and Zander (1992) coined the term combinative capability to represent the synthesis and application of new and existing knowledge culminating in innovation success. They view the firm as a repository of capabilities comprised of knowledge (information and know-how) - and the recombination of knowledge gives rise to new skills and routines for innovation. Grant (1996) refines our understanding of the relationship between knowledge and organizational capabilities by arguing that the integration of multiple types of knowledge is key to forming capabilities.

These studies extend the work of Lawrence and Lorsch (1967), who highlighted the need for intra-organizational coordination to align differentiated business units. Lawrence and Lorsch conceptualized integration as a “process of achieving unity of effort” (p. 4), and integrative capability as management’s ability to achieve that unity of effort. Where the locus of their integrative capability concept is internal integration, Verona’s (1999) synthesis of the competency literature identified a second type of integrative capability—external integration—that works in conjunction with internal integration to enhance project performance.

Using Henderson's (1994) definition in the context of these findings, we conceptualize integrative capability as a knowledge transfer competency with two dimensions: the ability to import external knowledge and the ability to synthesize internal knowledge. Recognizing that knowledge is largely tacit in nature, and difficult to codify and capture directly, we use the behavioral indicators access and integration as proxies for knowledge importation and synthesis. Access to external knowledge represents an external-to-internal transfer of knowledge, while internal knowledge integration captures an internal-to-internal transfer of knowledge. Amassing and synthesizing specialized knowledge from multiple sources is a pivotal factor in resolving the technical and operational uncertainties that impede timely project completion.

We recognize that knowledge integration originates with the activities of people (Amit and Schoemaker 1993). The integrative activities of a strong senior manager and local project managers have a positive effect on timely project completion (Plewa and Pliskin 1995; Verona 1999). For EAI projects that span a network of facilities overseen by a corporate office, the behavior of lead IT personnel captures the nature of a firm's knowledge transfer mechanisms. At the corporate level, the CIO's ability to access new knowledge and promote the integration of internal knowledge significantly influences the vision, planning, and implementation of an EAI project. At the facility level, the IT manager's acquisition of new knowledge and facilitation of internal knowledge integration affects the level of technical and operational knowledge needed to fulfill that vision. Next we explore each integrative dimension in more detail.

## Access to External Knowledge

Studies in new product development suggest external communication is strongly associated with project performance. For example, Nagarajan and Mitchell's (1998) study of technological change in the lithotripsy industry indicates that project success relies on the development and management of strong ties with external knowledge networks. Pennings and Harianto (1992) show that stronger technological networks have a greater ability to innovate. Ancona and Caldwell (1990, 1992) show that high-performing development teams carry out more external activities and show higher frequency of communication with external colleagues than low-performing development teams. These studies suggest that the act of importing new knowledge through external communication channels is an important factor in timely project completion.

To be of consequence, newly imported knowledge must be integrated into the decisions and actions of key personnel.

Senior managers play a powerful role in shaping a firm's technological capabilities through their decisions and actions (Pisano 1996). In the context of EAI, CIOs are charged with finding the right technology to advance their firm's strategic business goals (Swoyer 2003). They develop external communication channels to import new knowledge about technology, its impact, and its implementation. CIOs report that a large part of their leadership responsibility involves taking charge of high-profile strategic projects (CIO Magazine 2002) such as EAI. This involves communicating the project's vision and business impact to the executive team (and board), securing approval, then delivering that vision and impact on time and within budget.

The importation of new knowledge coupled with the recombination of existing knowledge provides CIOs with information that can be leveraged to improve their decision making and lower performance risk. Decision making is often compromised when executives fall victim to the planning fallacy, where benefits are overestimated and costs are underestimated. The result is an overly optimistic or bold forecast $^{3}$ (Kahneman and Lovallo 1993). Executives tend to frame their circumstance in the positive, where gains from a few successes outweigh losses from many failures (Kahneman and Tversky 1979). Anchoring on past successes leads to delusional optimism that distorts further analysis, and competitive pressure for limited resources perpetuates such distortions (Lovallo and Kahneman 2003). Unrealistic optimism about future events and outcomes is often coupled with an illusion of control, deepening the distortion from reality (Taylor and Brown 1988).

These cognitive biases are common when forecasting is based on an “inside view” of the project, where the focus is on a project plan and attempts are made to predict potential obstacles to project completion (Kahneman and Lovallo 1993). The inside view is an insular approach to forecasting where intuition and knowledge of the current project is used to forecast its rollout (Lovallo and Kahneman 2003). Bold forecasts are reduced when executives adopt an “outside view” or reference-class approach to outcomes estimation. This approach examines the experience of a reference class of similar projects, drafts a distribution of outcomes for the reference class, then positions the project within that distribution to assess likely outcomes (Lovallo and Kahneman 2003). In treating a project as an instance of a larger class of projects, the outside view avoids distortion related to the planning fallacy and optimistic bias.

On average, CIOs spend one day a week gathering information about emerging technologies, best practices, and high-level project management (CXO Systems 2003). They actively seek this knowledge through trade publications, seminars, vendor-sponsored technology briefings, and nurturing ties with outside IT professionals, particularly vendors and other CIOs (Blodgett 1998; Breshnahan 1996). CIO member organizations, such as the Society for Information Management and the College of Health Care Information Management Executives present an opportunity to network with peers and share best practices. These activities provide the means by which new knowledge can be incorporated in high-level decisions that ultimately affect duration estimates and the extent of IT-related project delays.

Where the CIO performs a boundary spanning function at the corporate level, the IT manager performs key boundary spanning activities at the facility level. Boundary spanning refers to the formal and informal communications an individual has with external entities it relies upon for information. Boundary spanning on the part of facility IT managers is an important mechanism by which development groups are linked to external sources of knowledge (Thomas-Hunt et al. 2003). These boundary spanners assume multiple roles to build and manage communication channels for knowledge transfer. Two of those roles are technical scout and task coordinator (Ancona and Caldwell 1990). As a technical scout, the IT manager gathers detailed information about the technology and its implementation. As a task coordinator, the IT manager develops and maintains lateral communications with relevant parties (i.e., users, vendors, and the development team) to coordinate and implement architectural change. These external knowledge transfer activities are aimed at enhancing the development team's expertise and improving the project management practices that mitigate execution risk.

As the lead IT member of a facility-specific project team, the IT manager is responsible for local project execution. Where knowledge deficits exist, information and know-how imported by the IT manager can alleviate many of the technological and operational uncertainties that forestall project completion. External sources of knowledge primarily consist of professional and operational outlets (Appleyard 1996), including professional associations, conferences, vendor-sponsored seminars, technical literature, and external peer networks. Managers who participate in external discipline-specific networks of knowledge increase the probability of timely project completion (Verona 1999). These activities provide the means for incorporating new knowledge in planning and implementation activities governed by IT managers. Thus, under a federal management structure, we hypothesize that

H1: The probability of on-time project completion is directly and positively related to the CIO's and IT manager's ability to access external knowledge.

## Internal Knowledge Integration

We use the term integration to refer to “the quality of the state of collaboration that exists among departments that are required to achieve unity of effort by the demands of the environment” (Lawrence and Lorsch 1967, p. 11). In the context of EAI projects, collaboration among IT personnel and operations personnel is required to achieve both IT platform integration and related work process integration. A fundamental activity of the development effort is to meld individually held information and know-how into a common stock of knowledge that can be applied to problem solving—in our case, EAI planning and implementation. The ability to integrate internally held knowledge requires a shared perspective of the problem, which permits existing knowledge to be combined and reformulated to produce new insights and solutions (Nonaka 1994; Okhuysen and Eisenhardt 2002).

The knowledge integration process involves social interactions among individuals using internal communication channels for knowledge transfer to arrive at a common perspective for problem solving. Where organizational units hold specialized knowledge, inter-unit linkages are the primary means of transferring that knowledge (e.g., Tasi 2001). Such knowledge transfer permits knowledge reuse, and the recombination of existing knowledge is an important antecedent of uncertainty resolution in organizational innovation (Marjchrzak et al. 2004; Terwiesch and Loch 1999).

For EAI projects, internal knowledge integration combines knowledge specific to the IT platform with knowledge of the operational routines it supports. An effective mechanism for achieving such integration is to coordinate the planning of interdependent IT and work process design strategies. Prior research in IT-enabled change indicates internal knowledge integration can be achieved when IT personnel are involved in work process planning and operational personnel are involved in IT planning (Boynton et al. 1994). Mutual consideration of IT and work process strengths and weaknesses allows the development team to identify information requirements for targeted work processes, predict what IT resources are needed to fulfill those requirements, and determine how best to deploy those IT resources to minimize IT-related project delays (Mitchell and Zmud 1999). The act of coordination is a knowledge integration process that facilitates a common understanding of project objectives and the means to reach those objectives, (Reich and Benbasat 1996).

A key result underlying this research is that the extensive coordination of interdependent strategies and individually held knowledge significantly improves the performance of large-scale IT projects.

Knowledge integration through joint planning relies on vertical and horizontal coordination mechanisms to facilitate knowledge transfer. Vertical coordination mechanisms utilize hierarchical relations to bring system users and IT personnel together (Nidumolu 1995), while horizontal coordination supplements hierarchical communication channels (Brown 1999). Typically, vertical coordination centers on the enabling activities of an authority figure, such as the policies and procedures a CIO adopts to involve functional and IT personnel in joint planning. Horizontal coordination mechanisms rely on lateral relations through personal and group communication channels to synthesize the knowledge held by system stakeholders, for example, an executive team and the CIO, system users and IT personnel (Enns et al. 2003; Pawlowski and Robey 2004; Van de Van et al. 1976). In their study of design structures and coordination at Texaco, DeSanctis and Jackson (1994) note that among the possible integration mechanisms available, cross-functional teams represent the most comprehensive structural approach to horizontal IT coordination.

Nidumolu's (1995) examination of the relationship between coordination mechanisms and performance of software development projects found the two mechanisms affect project performance differently. Vertical coordination had an indirect effect on performance by influencing execution risk and performance risk, while horizontal coordination had a positive and direct effect. This finding is in keeping with prior IS research where greater IT staff-user interaction reduces the technical and operational uncertainties surrounding development projects (Hunton and Beeler 1997). In the context of a federal management structure, this research suggests internal knowledge integration is a combined effort with the CIO responsible for the coordinated planning of loosely coupled units at the corporate level and the IT manager responsible for joint problem solving with cross-functional teams at the facility level. This reasoning leads to our second hypothesis.

H2: The probability of on-time project completion is directly and positively related to the CIO's and IT manager's ability to integrate internal knowledge.

Our hypotheses suggest that management's integrative capability is reflected in the perspectives of both the CIO and IT manager, which is consistent with the division of responsibilities in a federal management structure. To test these hypotheses, we develop two proportional hazard models, one for the CIO perspective ( $S_{1}$ ) and another for the IT manager perspective ( $S_{2}$ ). Theoretically, we expect agreement between the two integrative dimensions, as well as agreement between the two management perspectives.

## Controlling for Project Differences

This study is conducted at the project level of analysis—specifically, enterprise-wide projects that span multiple facilities. In addition to management's integrative capability, other factors known to influence timely project completion include project size, management's prior project experience, and level of user involvement. While lines of code, manpower, and budgets are common measures of a project's size, these measures are misleading relative to time overrun (Brooks 1995). Rather, the size and complexity of an EAI project is directly related to the number of interfaces needed. Where these interfaces tie together disparate applications across varying business processes spread among numerous facilities, execution risk increases, as does the likelihood of IT-related project delays. Thus, the more interfaces an EAI project entails, the less likely the project will be completed on time.

Another key factor affecting timely project completion is management's prior project experience (McFarlan 1981). Knowing how to acquire project support, project planning, and its implementation requires a set of knowledge structures for problem solving that is hard to articulate. Learning set theory (Harlow 1959) tells us that learning how to recognize important pieces of information and learning how to solve problems with that information is built up over many practice trials with related problems. As IT remains the primary job background for CIOs and IT managers (Varon 2002), they build a stock of tacit knowledge related to their prior project experience. A firm's ability to draw on this experience enhances project performance, such that higher levels of project experience lead to shorter IT-related project delays (Broadbent et al. 1999), and accumulated experience is positively associated with higher project performance (Iansiti 2000).

User involvement has long been considered a vital component of effective system development (McFarlan 1981). Although recently defined as a psychological state where a user ascribes importance to a system, traditionally user involvement has referred to user participation in the systems development process (Hartwick and Barki 1994). We use the broader, more traditional meaning of user involvement in this study. User involvement in an IT project provides a better understanding of work processes and related information requirements, more realistic user expectations about the system, less resistance to change, and greater user commitment to project success (Lucas 1974; Robey and Farrow 1982). As the scale and complexity of a project increases, so does the need for active user involvement (Tait and Vessey 1988), which raises the probability of on-time project completion.

## Methodology

## Instrument Development

Replicating Henderson and Cockburn's (1994) measures for architectural competence, Henderson's (1994) measures for integrative capability embody two integrative dimensions: access to external knowledge and internal knowledge integration. These measures were specific to research and development in the pharmaceutical industry and are not easily generalized to other industries. For example, the measures for access to external knowledge—that is, publication record, proximity to a university, and joint industry-university ventures—are less applicable outside an R&D context. Two of the four measures used for internal knowledge integration, global research effort and locus of research administration, are less applicable to an IT context. However, the other two measures, the use of cross-functional teams and centralized decision making for resource allocation, are more applicable.

In developing our measure of access to external knowledge, we emphasize external knowledge sources for IT professionals, while maintaining Henderson's concept of accessibility to new knowledge. Incorporating the concepts of boundary spanning and social networks highlighted in our literature review, we generated three items to represent access to external knowledge that affect systems development projects. These are questions 8, 9, and 10 in the survey instrument provided in the appendix.

To measure internal knowledge integration, we utilized relevant portions of two previously validated instruments. We adapted five items from Mitchell and Zmud's (1999) instrument on strategy coupling and two items from Reich and Benbasat's (1996) instrument on shared objectives to measure knowledge integration between IT personnel and clinicians. The five items adapted from Mitchell and Zmud's coupling instrument are questions 1 through 5 in our survey; the two items adapted from Reich and Benbasat's objectives instrument are questions 6 and 7 in the survey. All items were measured on a seven-point Likert scale and solicit information about the level of knowledge exchange at the project level of analysis. Because the projects in our sampling frame were large-scale EAI projects that spanned the entire organization, our internal knowledge integration measures were chosen to capture knowledge exchange within and across facilities, from the IT manager's perspective and from the CIO's perspective, respectively. Doing so allows for the identification of differences in perception related to management structure that in turn affect project performance.

Henderson and Cockburn also highlighted the importance of prior experience in accessing and assimilating new knowledge; however, they did not measure it. In a related paper analyzing underinvestment and incompetence in radical innovation, Henderson (1993) used cumulative years invested in the previous generation of an innovation as a proxy for prior experience at the organizational level. MacCormack et al. (2001) also used temporal measures in reference to “generational experience” where they measured prior experience with two or more generations of a technology. We incorporated the empirical definition of prior experience put forth by Henderson and by MacCormack et al., by capturing an individual’s years of past experience managing different types of projects related to enterprise-wide application integration across a networked organization. We developed an additive scale to capture prior project experience as a sum of project types (IT redesign, IT-enabled process redesign, and network integration) for which a respondent had several years experience. These questions are 11a, b, and c in the survey instrument.

A pilot study was conducted to evaluate the meaning, ordering, and representativeness of these scales. We sent the survey instrument to four corporate CIOs and related facility IT managers for review regarding intended issues and concepts. Upon receipt of completed surveys and comments, we interviewed the respondents by telephone to obtain further feedback and refined the instrumentation accordingly (Converse and Presser 1986; Stone 1978). We initially used closed-ended questions to measure several project control variables: number of interfaces, number of programmers involved, number of users involved, implementation horizon, and dollar amount allocated to the project's budget. Based on feedback from the pilot instrument, two of these objective measures were replaced with subjective measures using a Likert scale. A subjective measure for budget was created to facilitate a response to this item, as many CIOs are hesitant to provide actual figures. CIO's were asked to categorize the project's budget using a scale of 1 to 7, with 1 meaning extremely inadequate, 4 meaning adequate, and 7 meaning extremely adequate. Number of users involved was replaced with a subjective measure (intensity of user involvement) to capture the level of user participation. CIO's were asked to categorize level of user involvement using a scale of 1 to 7, with 1 meaning very low, 4 meaning moderate, and 7 meaning very high.

## Measuring the Dependent Variable

To represent our dependent variable (on-time project completion), we used the process performance measure time overrun, specifically focusing on IT-related project delays. In preimplementation phone interviews, respondents provided an estimated completion date for the project. In postimplementation phone interviews, respondents provided an actual completion date. When the actual completion date exceeded the target completion date, we queried respondents to identify the primary reason the project was delayed. Where project delays were primarily due to IT-related problems, respondents were asked to elaborate on the underlying reasons these problems occurred and how the situation was resolved. If projects were delayed for reasons other than IT problems they were excluded from this study. The telephone interview guides are provided in the appendix.

## Data Collection

Data collection took place between 1993 and 2003 as part of a larger research program on the impact of IT in health services. Although each EAI project was followed from startup to completion, this portion of the study focused on knowledge factors affecting timely project completion. The sampling frame consisted of 114 health networks that used HL7 compliant interface engines for application integration. HL7 is a messaging standard that dominates the medical sector. Health network refers to a multi-organizational conglomerate, typically comprised of 20 or more health care facilities. For example, New York Presbyterian Health Network is comprised of 156 facilities: 32 hospitals, 3 specialty institutions, 8 long term care facilities, 11 home health agencies, 97 satellite primary care centers, 12 physician groups, and 4 managed care entities. EAI projects were identified through professional associations, government offices, consulting agencies, and the popular press.

We contacted the CEO of each health network, briefly explained the study, and obtained the name of the CIO responsible for integrating applications across network facilities. CIOs were contacted by telephone, informed of the study, and asked to participate. Of the CIOs contacted, 28 declined to participate, 4 switched to ERP systems, and another 7 suspended EAI until the next (object-based) version of HL7 was released in 2002. The remaining 75 health networks used HL7 version 2.x as a messaging standard for EAI. Once agreement was obtained, we asked the CIO about project milestones and when the project was slated for implementation. We phoned again just prior to the implementation date to see if the project was on track. If so, we proceeded with the telephone interview to gather detailed information about IT (particularly EAI) planning. If not, we phoned again just prior to the revised start date.

At this point we also obtained information regarding our control variables (number of interfaces to be constructed, number of programmers involved, project budget, and implementation horizon). Next, we asked each CIO to identify an IT manager actively involved in managing the EAI project at the facility level. We then contacted facility IT managers to explain the nature of our study and obtain consent for their participation. After that, our survey instrument was distributed electronically and participants were asked to return the completed survey within 30 days. Those failing to return surveys were contacted during the subsequent quarter and the survey was conducted by telephone. As projects were completed, participants were interviewed by telephone to gather more information about user involvement (number and attitude), IT-related project delays, and resolution of the delays. Projects delayed for reasons outside the IT domain (e.g., awaiting next version of HL7, switched to ERP, redeployments of human and financial resources, etc.) were excluded from further analysis.

## Instrument Validation

We used principal components analysis with varimax rotation to validate the measurement scales for our integrative dimensions (access to external knowledge and internal knowledge integration) for both sets of respondents. The initial extraction suggests two principle constructs as each data set had just two eigenvalues that exceeded the 1.0 cutoff for significance. Table 1 suggests both convergent and discriminant validity for these constructs, as primary factor loadings exceed the 0.722 critical value for significance for all items (Stevens 1986, p. 344). There was a high degree of internal consistency among items as indicated by a Cronbach's alpha coefficient of 0.90 based on CIO responses and 0.88 based on IT manager responses (Stone 1978). Items 1 through 7 primarily loaded on the internal knowledge integration dimension and items 8, 9, and 10 primarily loaded on the access to external knowledge dimension. The resulting two-factor solution explained 85 percent percent of the variance in our CIO data and 75 percent of the variance in our IT manager data.

In addition to a count of prior project experience, we collected data on five control variables known to affect IT project outcomes. As indicated in Table 2, budget, implementation horizon, user involvement, and number of programmers were correlated, as were number of interfaces and programmers.

Table 1. PCA Results: Rotated Sum of Squares Loadings

<table><tr><td rowspan="2">Survey Item</td><td colspan="2">CIO Respondents</td><td colspan="2">IT Manager Respondents</td></tr><tr><td>Access to External Knowledge</td><td>Internal Knowledge Integration</td><td>Access to External Knowledge</td><td>Internal Knowledge Integration</td></tr><tr><td>IT plan supports redesign plan</td><td>.073</td><td>.945</td><td>.055</td><td>.799</td></tr><tr><td>Clinicians involved in IT plan</td><td>.160</td><td>.910</td><td>-.087</td><td>.877</td></tr><tr><td>Consider information needs</td><td>.120</td><td>.923</td><td>-.053</td><td>.907</td></tr><tr><td>IT assessment utilized</td><td>-.015</td><td>.915</td><td>-.198</td><td>.839</td></tr><tr><td>Assessed IT trends</td><td>.059</td><td>.940</td><td>.011</td><td>.871</td></tr><tr><td>IT aware of clinical objectives</td><td>.116</td><td>.899</td><td>-.063</td><td>.899</td></tr><tr><td>Clinicians aware IT objectives</td><td>-.014</td><td>.882</td><td>.050</td><td>.887</td></tr><tr><td>Professional Association</td><td>.919</td><td>.177</td><td>.776</td><td>.274</td></tr><tr><td>Workshops/Conferences</td><td>.917</td><td>.131</td><td>.808</td><td>.076</td></tr><tr><td>Journal Subscriptions</td><td>.929</td><td>-.093</td><td>.912</td><td>.071</td></tr><tr><td>Eigen values</td><td>2.488</td><td>6.061</td><td>2.145</td><td>5.325</td></tr><tr><td>% variance explained</td><td>26.112</td><td>59.371</td><td>21.859</td><td>53.251</td></tr></table>

Table 2. Correlation Among Project Control Variables

<table><tr><td></td><td>CIO Exp</td><td>ITM Exp</td><td>Interfaces</td><td>Budget</td><td>Horizon</td><td>Users</td><td>Programmers</td></tr><tr><td>CIO Experience</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ITM Experience</td><td>.206</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Interfaces</td><td>-.174</td><td>-.267</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>Budget</td><td>-.042</td><td>-.132</td><td>.161</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>Horizon</td><td>.117</td><td>.097</td><td>.150</td><td>.477*</td><td>1.00</td><td></td><td></td></tr><tr><td>User Involvement</td><td>.150</td><td>.017</td><td>-.078</td><td>.486*</td><td>.482*</td><td>1.00</td><td></td></tr><tr><td>Programmers</td><td>.014</td><td>-.113</td><td>.338*</td><td>.367*</td><td>.617*</td><td>.161</td><td>1.00</td></tr><tr><td>Facilities</td><td>.189</td><td>-.008</td><td>.433*</td><td>.355*</td><td>.661</td><td>.104</td><td>.356*</td></tr></table>

\*Significant at 0.01.

To minimize inflation of error terms, we limited our controls to three uncorrelated variables: number of interfaces, intensity of user involvement, and prior project experience. An examination of Z scores for our two integrative dimensions and three controls revealed an absence of univariate outliers, as none exceeded the suggested 3.29 cutoff value (Tabachnick and Fidell 2001). One multivariate outlier was identified (Cook's distance = 0.28064, Dffit = 1.37870) and removed, leaving 74 projects for analysis. Descriptive statistics are provided in Table 3.

## Statistical Methods and Results

## Statistical Methodology

In a duration analysis that uses Cox regression (one in a family of proportional hazard models), the probability associated with an outcome (called the dependent event) is based on an underlying time variable relative to a set of predictors. Data is collected regarding the dependent event and its time to occurrence, and then a count of the duration time relative to the predictor variables is used to calculate the probability of the dependent event occurring. In this study, collecting data on the scheduled and actual completion dates provided an objective measure for the duration of IT delay (our time variable) that was used to calculate the probability of on-time completion for finished projects (our dependent event) for a given set of predictors.

<table><tr><td colspan="5">Table 3. Descriptive Statistics</td></tr><tr><td>Variable</td><td>Minimum</td><td>Maximum</td><td>Mean</td><td>Std. Dev.</td></tr><tr><td>Interfaces</td><td>1.00</td><td>7.00</td><td>3.95</td><td>1.49</td></tr><tr><td>User Involvement</td><td>1.00</td><td>7.00</td><td>3.81</td><td>1.86</td></tr><tr><td>Dedicated Programmers</td><td>2.00</td><td>14.00</td><td>5.35</td><td>2.06</td></tr><tr><td>Implementation Horizon</td><td>1 mo (.08 yr)</td><td>4 years</td><td>2.2 year</td><td>0.95 years</td></tr><tr><td>Budget Category</td><td>3</td><td>4</td><td>3.42</td><td>0.50</td></tr><tr><td>Number of Facilities</td><td>5</td><td>178</td><td>61.67</td><td>5.62</td></tr><tr><td>CIO Project Experience</td><td>1.00</td><td>3.00</td><td>2.28</td><td>0.79</td></tr><tr><td>CIO External Access</td><td>-1.65</td><td>1.76</td><td>-.01</td><td>1.00</td></tr><tr><td>CIO Internal Integration</td><td>-1.61</td><td>1.53</td><td>-.02</td><td>1.00</td></tr><tr><td>IT mgr Project Experience</td><td>1.00</td><td>3.00</td><td>2.39</td><td>0.66</td></tr><tr><td>IT mgr External Access</td><td>-3.45</td><td>1.82</td><td>0.00</td><td>1.00</td></tr><tr><td>IT mgr Internal Integration</td><td>-2.96</td><td>1.40</td><td>0.00</td><td>1.00</td></tr><tr><td>Duration of IT Delay</td><td>.01 mo</td><td>23 mo</td><td>4 mo</td><td>4.83 mo</td></tr><tr><td>Project Duration</td><td>6 mo</td><td>84 mo</td><td>33 mo</td><td>21.97 mo</td></tr></table>

Traditional linear regression models do not lend themselves to the analysis of duration time relative to an outcome because the normality assumption for dependent residuals generally does not hold. Although linear regression is robust to deviations from normality, the distributions of time to an event are typically nonsymmetric and linear regression is not robust to these violations. Duration analysis removes the distributional assumption of time and uses the order of event occurrence to assess the influence of a set of predictors on the event (Cleves et al. 2004).

We use Cox regression, a duration analysis approach in which the functional form of the relationship between the predictor variables and the outcome variable need not be specified in order to fit a model to the data. This approach is preferred to other modeling approaches to describe the underlying time dependency of an event when distribution assumptions may not hold (Box-Steffensmeier and Jones 2004, p. 93). Cox regression is a proportional hazards (PH) regression technique used in survival analysis, event history analysis, reliability analysis, and other types of duration analysis where the outcome variable is time until the occurrence of an event (Kleinbaum and Klein 1996). This technique permits us to model on-time project completion (the dependent event) as a log-linear function of contingencies among our covariates: the integrative dimensions and our project controls. The time to project completion refers to the duration of IT-delays, which extends the implementation period. Estimating a PH model allows us to formulate a Cox regression equation without specifying an underlying distribution for the duration of IT-delay (Box-Steffensmeier and Zorn 1998). Through the sequential ordering of covariates, we can isolate the likelihood that our two integrative dimensions increases the likelihood of on-time project completion by reducing the duration of IT delay, accounting for project size, user involvement, and project experience.

## Model Specification

Our analysis is based on the following Cox PH model:

$$
h (t, X) = h _ {0} (t) \exp \left(\Sigma_ {p} \beta_ {i} x _ {i}\right)
$$

<table><tr><td colspan="5">Table 4. Grambsch and Therneau Test Results for Proportionality</td></tr><tr><td></td><td colspan="2">CIO</td><td colspan="2">IT Manager</td></tr><tr><td>PH Model</td><td> $S_{1\text{ controls}}$ </td><td> $S_{1\text{ full}}$ </td><td> $S_{2\text{ controls}}$ </td><td> $S_{2\text{ full}}$ </td></tr><tr><td>Global Test  $\chi^2$ </td><td>1.06</td><td>0.64</td><td>0.14</td><td>1.27</td></tr><tr><td>Prob &gt; $\chi^2$ </td><td>0.786</td><td>0.9861</td><td>0.9871</td><td>0.9382</td></tr><tr><td>Interfaces rho</td><td>0.003</td><td>-0.033</td><td>0.028</td><td>0.023</td></tr><tr><td> $\chi^2$ </td><td>0.00</td><td>0.07</td><td>0.06</td><td>0.04</td></tr><tr><td>Prob &gt; $\chi^2$ </td><td>0.9802</td><td>0.7986</td><td>0.8065</td><td>0.8456</td></tr><tr><td rowspan="3">User Involvement</td><td>-0.024</td><td>0.015</td><td>-0.004</td><td>0.040</td></tr><tr><td>0.04</td><td>0.02</td><td>0.00</td><td>0.12</td></tr><tr><td>0.8412</td><td>0.8955</td><td>0.9735</td><td>0.7290</td></tr><tr><td rowspan="3">Project Experience</td><td>-0.124</td><td>-0.080</td><td>-0.014</td><td>-0.003</td></tr><tr><td>1.03</td><td>0.46</td><td>0.02</td><td>0.00</td></tr><tr><td>0.3100</td><td>0.4967</td><td>0.8963</td><td>0.9789</td></tr><tr><td rowspan="3">Access to External Knowledge</td><td></td><td>-0.062</td><td></td><td>-0.087</td></tr><tr><td></td><td>0.32</td><td></td><td>0.64</td></tr><tr><td></td><td>0.5743</td><td></td><td>0.4252</td></tr><tr><td rowspan="3">Internal Knowledge Integration</td><td></td><td>-0.023</td><td></td><td>-0.079</td></tr><tr><td></td><td>0.04</td><td></td><td>0.41</td></tr><tr><td></td><td>0.8427</td><td></td><td>0.5237</td></tr></table>

where $h(t,X)$ is the hazard rate or likelihood that our event (project completion) will occur at time t given it is not complete at t-1 and depends on a set of explanatory covariates $X = (x_{1} \ldots x_{p})$ . The term $h_{0}(t)$ represents the baseline hazard function, and measures the likelihood of project completion at time t without the explanatory covariates. This baseline hazard function interacts with the expression $exp(\Sigma\beta_{i}x_{i})$ , which is independent of time, to incorporate the effects of the covariates. The term $x_{i}$ denotes an individual covariate, $\beta_{i}$ is the regression coefficient associated with that covariate, and p is the number of covariates in the model. In the context of EAI projects, we use this model to understand how our integrative dimensions affect the duration of IT delay impeding project completion, while controlling for project size, user involvement, and project experience.

The Cox PH model assumes the proportionality of hazards, wherein the relationship between project completion rates and duration of IT-delay remains constant across sets of covariates. Violation of proportionality signals that one or more covariates are time-dependent, and an alternative PH model should be specified. We used the Grambsch and Therneau (1994) tests of the proportional hazards assumption implemented in Stata 8.0 to assess the appropriateness of our model specification. First, we tested the null hypothesis that the regression slope for the global model was zero. A nonzero slope is an indication of a violation of the proportional hazard assumption. In our global tests, the likelihood chi-square ( $\chi^{2}$ ) statistic is calculated by comparing the deviance ( $-2 \times \log$ likelihood) of our Cox model, with all of the specified covariates, against a model with all covariates dropped. Table 4 shows that the global test chi-square statistic for the Cox models are insignificant, upholding the proportionality assumption.

Next, we tested for a nonzero slope in a generalized linear regression of scaled Schoenfeld residuals on functions of time for each covariate. These test results are also provided in Table 4. The chi-square statistic for each rho (Pearson product-moment correlation) is insignificant, indicating all covariates are time-independent in accordance with the proportional hazards assumption.

It has been shown that if the Cox regression model fits the data, then the true cumulative hazard function conditional on the covariate vector has an exponential distribution with a hazard rate of 1 (Cleves et al. 2004). Using Stata 8.0, we generated the Nelson–Aalen (N–A) cumulative hazard function and plotted it against the Cox–Snell (C–S) residuals. Comparing the jagged N–A line to the reference C–S line in

![](/api/attachments/WRGHMWN3/fulltext/images/1880acaf7a64d205aa6779a03ab442c0bb260603034bb466254d20710e535a48.jpg)

Figure 2 for the CIO model $S_{1full}$ and Figure 3 for the IT manager model $S_{2full}$ , we find that both models fit the data well. Some variability about the C-S reference line is to be expected, particularly in the right hand tail, due to the reduced sample as projects are completed (Cleves et al. 2004, p. 190).

## Regression Results

In all, 74 completed EAI projects were included in the analysis; thus there was no censored data. We developed two sets of Cox regression models to test our hypotheses. The first set of models (S $_{1}$ ) view management's integrative capability from the CIO's (corporate-level) perspective and the second set (S $_{2}$ ) from the IT manager's (facility-level) perspective. Table 5 provides the following Cox regression results: a likelihood ratio chi-square test for goodness of model fit, the change in log-likelihood as the regression model is expanded, the estimated coefficient ( $\beta$ ), the standard error of the estimated coefficient SE( $\beta$ ), the hazard ratio for a one unit change in the covariate $exp(\beta)$ , and a z-test statistic along with its p-value for the significance of the estimated coefficient. The z-test is sometimes referred to as Wald's test and is calculated as ( $\beta/SE$ ) $^{2}$ (Cleves et al. 2004, p. 125).

To determine whether management's integrative capability improves the probability of timely project completion by minimizing IT-delay (our first research question), we entered our covariates sequentially to isolate any improvement in predictability due to our competence dimensions. In our CIO models (S $_{1}$ ), project controls (number of interfaces, intensity of user involvement, and CIO project experience) were entered first in model S $_{1\ controls}$ , followed by the integrative capability dimensions (access to external knowledge and internal knowledge integration) in model S $_{1\ full}$ . As expected, project controls (S $_{1\ controls}$ ) alone influence the likelihood of completion. The difference in the log-likelihood ratios (Agresti 1990) between S $_{1\ controls}$ and S $_{1\ full}$ ( $\chi^{2} = 5.986$ , p = 0.050) indicates that after adjusting for our controls, together the competence dimensions have a significant effect on the probability of on-time project completion.

![](/api/attachments/WRGHMWN3/fulltext/images/843db0c08d06262a04d99096038a5bcc07b1cd4ffa3220238c76f4b069c60db2.jpg)  
Figure 3. IT Manager Model Goodness of Fit

In our IT manager model $(S_{2})$ , the control variable CIO project experience is replaced with IT manager project experience. This modified model for project controls $(S_{2\text{controls}})$ remains influential in predicting the likelihood of on-time project completion. The difference in the log-likelihood ratios between $S_{2\text{controls}}$ and $S_{2\text{full}}$ is also statistically significant ( $\chi^{2}=7.698, p=0.021$ ), suggesting that from the IT manager's perspective, together the competence dimensions influence project timeliness at the facility level as well. To learn how the individual dimensions behave we turn to our second research question and our two hypotheses.

## Predictors at the Corporate Level

We refer to the z-test statistic in Table 5 to determine which integrative dimensions are most important for predicting on-time project completion. At the corporate level, the CIO's access to external knowledge (z = 1.97, p = 0.049) and internal knowledge integration (z = 1.94, p = 0.053) in model $S_{1full}$ indicate both competence dimensions are reliable predictors of on-time project completion. An examination of regression coefficients ( $\beta$ ) reveals they have a positive effect on timely project completion. These results lend support to our two hypotheses from the perspective of the CIO.

<table><tr><td colspan="5">Table 5. Cox Regression Results</td></tr><tr><td></td><td colspan="2">CIO</td><td colspan="2">IT Manager</td></tr><tr><td>PH Model</td><td> $S_{1\text{ controls}}$ </td><td> $S_{1\text{ full}}$ </td><td> $S_{2\text{ controls}}$ </td><td> $S_{2\text{ full}}$ </td></tr><tr><td>Log-Likelihood Ratio  $\chi^{2\dagger}$ Change in LLR  $\chi^{2} (G^{2})$ </td><td>41.615***</td><td>48.188***5.986**</td><td>42.688***</td><td>48.062***7.698**</td></tr><tr><td>Interfaces z-statistic</td><td>-5.86***</td><td>-4.80***</td><td>-4.40***</td><td>-4.68***</td></tr><tr><td>HR</td><td>0.56</td><td>0.603</td><td>0.61</td><td>0.589</td></tr><tr><td>β(SE)</td><td>-0.583(0.099)</td><td>-0.507(0.105)</td><td>-0.487(0.111)</td><td>-0.530(0.113)</td></tr><tr><td>User Involvement</td><td>1.96**1.140.128(0.065)</td><td>1.401.1010.097(0.069)</td><td>2.26**1.160.148(0.065)</td><td>2.60***1.1950.178(0.068)</td></tr><tr><td>Project Experience</td><td>1.60*1.280.244(0.152)</td><td>1.90**1.3590.306(0.161)</td><td>1.71*1.480.391(0.229)</td><td>1.90**1.5710.452(0.238)</td></tr><tr><td>Access to External Knowledge</td><td></td><td>1.97**1.3230.280(0.142)</td><td></td><td>2.04**1.2360.266(0.130)</td></tr><tr><td>Internal Knowledge Integration</td><td></td><td>1.94**1.2890.254(0.131)</td><td></td><td>1.64*1.2190.198(0.121)</td></tr></table>

Significance levels \*.10, \*\*.05, \*\*\*.01  
\*Because Cox regression models are semi-parametric, the traditional $R^2$ is not an appropriate measure of model fit. Instead, the log-likelihood ratio $\chi^2$ is used.

To understand the extent of these effects, regression coefficients are exponentiated (e $^{\beta}$ ) into hazard ratios that are easier to interpret. Hazard ratios (HR) greater than 1 are interpreted as “a unit increase in X increases the likelihood of on-time project completion by Y%,” where Y = HR-1. Hazard ratios less than 1 are interpreted as “a unit increase in X decreases the likelihood of on-time project completion by Y%,” where Y = 1-HR. From the CIO perspective, the likelihood of on-time project completion increases by 32 percent for every unit increase in access to external knowledge, and increases by 29 percent for every unit increase in internal knowledge integration.

Two of the three project controls had a significant influence on timely project completion. The likelihood of on-time completion decreases by 40 percent for every (100) unit increase in the number of interfaces, and it increases by 36 percent with prior CIO experience. The intensity of user involvement was not a significant predictor at the corporate level.

## Predictors at the Facility Level

An IT manager's access to external knowledge (z = 2.04, p = 0.041) is also a strong predictor of on-time project completion. Coupled with strong CIO results for the same dimension, hypothesis H1 is fully supported. At the facility level, internal knowledge integration (z = 1.64, p = 0.10) is also a reliable predictor of project timeliness; however, its significance level is weaker than at the corporate level. Thus, our second hypothesis outlining a direct relationship between internal knowledge integration and project timeliness is significant or approaches significance when considering both managerial perspectives.

The regression coefficients indicate all covariates have a positive effect on timely completion, with the exception of interfaces, which has the expected negative effect. An examination of the hazard ratios shows the likelihood of on-time project completion increases by 24 percent for every unit increase in the IT manager's access to external knowledge, and roughly by the same amount, 22 percent, for every unit increase in internal knowledge integration.

Interestingly, the control variable, intensity of user involvement is a significant predictor of timely completion (z = 2.60, p = 0.009) at the facility level, while it is not at the corporate level. The other two controls are also reliable predictors from the IT manager's perspective. The probability of on-time completion increases by 19 percent with every unit increase in the intensity of user involvement, and it increases by 57 percent with accumulations in IT manager experience. These increases are offset by a 41 percent decrease in the likelihood of timely completion for every (100) unit increase in the number of interfaces required.

## Common Method Bias

To reduce common method variance, variance attributed to the measurement method rather than the constructs of interest, we separated the measurement of our dependent variable and predictor variables temporally and methodologically. Temporally, we collected data on our dependent and duration variables (project completion and IT-related delays) at different points in time than the data for our predictor variables. Methodologically, we used telephone interviews to gather data for our dependent and duration variables, and we used a survey instrument delivered electronically to gather data on the predictors. We conducted Harman's one-factor procedure to statistically test for the presence of common method variance among our variables. For each of the corporate and facility levels, the duration and predictor variables were entered into a factor analysis to see if all variables would load on a single factor and whether a single item would account for the majority of covariance (Podsakoff and Organ 1986). Multiple factors were obtained for both analyses with a relatively even distribution of covariance among items, indicating a lack of common method variance.

## Discussion and Limitations

Our study yielded four main findings. First, we find that management's access to external knowledge significantly increases the likelihood of on-time project completion. The strength of this relationship is strong for both sets of respondents, with a high degree of reliability, providing solid support for our first hypothesis. This finding reinforces earlier research on the expropriation of knowledge through social networks and its ease of transfer, but does so in the context of large-scale EAI projects in the medical sector. Boundary spanning utilizes social forums and publications to import knowledge that is largely codified in verbal form (Liebeskind et al. 1996). This finding also supports the argument that the degree to which knowledge is codifiable and conceptually related facilitates its absorption into the firm (Zander and Kogut 1995). In addition, it upholds the outside view of forecasting (Lovallo and Kahneman 2003), whereby management's ability to tap external sources of information impacts the quality of the reference class used for predicting EAI project outcomes.

Second, we find that management's ability to integrate internal knowledge also increases the probability of on-time completion. As an IT platform evolves and the breadth of technologies increases, more specialized knowledge is needed to develop and manage those technologies and dependent work processes. Through coordinated planning, knowledge specific to IT and organizational processes is pooled and synthesized into a common body of knowledge. The act of coordinated planning is a knowledge integration mechanism that facilitates a shared perspective of the project reducing the incidence and severity of impediments resulting in IT delay. Although coordinated planning is conducted at different management levels, a shared perspective may not exist between management levels.

As a predictor of on-time project completion, internal knowledge integration is more reliable at the corporate level than at the facility level. We attribute this difference to the span of management responsibility, which provides the CIO with a broader, enterprise-wide perspective and the IT manager with a narrower, facility-specific perspective. Considering our outcome variable is the timely completion of enterprise-wide projects, the knowledge integration capabilities for all constituent facilities as reflected from the CIO should better predict timely completion. Thus, in spite of the

CIO and IT manager perspectives being highly correlated (r = .931, p = .000), as are the matched survey items, the reliability of this dimension as a predictor of timeliness is stronger for the CIO than the IT manager. The CIO perspective is able to account for more of the total variance in IT-delay than the IT manager perspective. Additional research is needed to ascertain if the reverse holds for project outcomes confined to a single facility.

Third, we find that, taken together, the integrative dimensions are reliable predictors of project timeliness and good measures of management's integrative capability. Our Cox regression results show a high level of agreement between the integrative dimensions and across managerial perspectives. Our CIO results indicate the integrative dimensions have roughly equal weight (HR of 32 percent and 29 percent) in predicting on-time project completion. Our IT manager results show a closer weighting (HR of 24 percent and 22 percent), with slightly less impact than from the CIO perspective. This level of agreement provides confidence that the integrative capability concept as applied to product development is generalizable to systems development, and more specifically to EAI projects. We conclude that management's integrative capability can improve the probability of on-time project completion by reducing the duration of IT delay. Thus, our first research question is answered affirmatively.

Finally, we find that two of our three project controls are significant predictors of on-time completion and behave as expected. The exception is intensity of user involvement, which is a reliable predictor at the facility level but not the corporate level. We attribute this outcome to interaction patterns at each management level. Collocation puts the IT manager and system user in close proximity, and oversight of cross-functional teams provides the means to assess intensity of user involvement. CIOs interact primarily with the executive team and IT personnel, providing little exposure to the user community. Taken in conjunction with our earlier findings, accuracy in predicting the probability of on-time completion is enhanced when both perspectives are taken into consideration.

Our study's primary limitation is its potentially limited generalizability. We focused on large, complex EAI projects in the medical sector and our findings may be less applicable to smaller IT projects, smaller organizations, and other business sectors. The measurement scale developed is specific to an IT development environment and not readily applicable to other contexts. Generalizability may have been further compromised because of convenience sampling and the exclusion of on-going projects. Of the 28 firms that declined to participate, 11 didn't meet the criteria for inclusion in the study. While there are no differences in the characteristics of the 75 participating and 17 nonparticipating firms, the potential for sampling bias exists. Consequently, our findings are most relevant for completed EAI projects and we can offer no conclusions about on-going EAI projects. Given our proportional hazard models focus on integrative mechanisms in the context of a federal management structure, the model may not be applicable to centralized or decentralized approaches.

Our findings are limited to one measure of project performance: on-time project completion. Other important performance measures, such as adherence to budget, user satisfaction, and goal attainment, do not lend themselves to duration analysis, and therefore are not explored in this study. More research is needed to assess how management's integrative capability affects other performance measures, particularly in light of known project predictors unrelated to knowledge management.

Other research design limitations also exist. The smaller sample size limited our ability to use additional control variables to partition out influential effects that might be applicable to a greater variety of projects. The variety of development methodologies (e.g., the traditional SDLC, RAD, SCRUM, XP, and ASD) used for EAI precluded a meaningful measure of project team size. Thus a comparison of projects by team size was not undertaken. Additional research is needed to assess the effect of team size and development methodology on project performance. Finally, the measures for management's integrative capability appear psychometrically sound. However, additional refinement is always possible. For example, incorporating social indicators of coordination (e.g., those discussed by Reich and Benbasat 1996) would more fully represent internal knowledge integration at the facility level.

## Conclusions and Managerial Implications

The purpose of this study was to understand the relationship between management's integrative capability and one aspect of EAI project performance, on-time project completion. Our proportional hazards model validates the role of management's integrative capability in facilitating on-time project completion. After taking several controls into consideration, our PH models show that higher levels of integrative capability minimize IT delays through better prediction and execution, thereby promoting timely project completion. Amassing the requisite knowledge for reference-class forecasting and for resolving project uncertainties that impede implementation is a pivotal factor for EAI project success. In keeping with previous research on the role of dynamic, integrative, and combinative capabilities in new product development, our results confirm the importance of synthesizing knowledge from multiple sources to successfully manage the innovation process.

The partitioning of management's integrative capability into two integrative dimensions provides additional insight into its effect on timely project completion. In the absence of information about EAI or its impact on work processes, technical and operational uncertainties arise, resulting in IT delays that can be directly attributed to IT-related knowledge deficits in the prediction and execution of project outcomes. Our findings indicate that integrative dimension is a significant predictor of on-time project completion, and a key indicator of underutilized knowledge channels.

Methodologically we demonstrate how duration analysis can inform MIS research and we highlight the use of Cox regression as a reliable means of assessing risk factors related to the passage of time. Cox regression is one technique in a family of proportional hazard models that is suitable for samples with or without censored data. The refinement of Henderson and Clark's (1994) measurement scale provides a parsimonious and validated instrument for measuring a firm's integrative capabilities in an EAI context. In addition, our analysis reveals the importance of taking management structure into consideration when studying IT phenomena in networked organizations. Data collection confined to one level of management in a multitiered structure may provide misleading results.

A key feature of our study is that the measures we use for each of the integrative dimensions are answers to questions that can be obtained prior to project implementation, and thereby predict the likelihood of on-time completion in advance. This means our model can be directly used in practice. The literature suggests that firms can substantially reduce and prevent IT delays by cultivating management's integrative capability. Our proportional hazard model provides a means of determining whether an integrative capability requires further cultivation and our survey instrument provides a means of detecting particular integrative behaviors in need of attention.

Our survey instrument is short, simple to administer, and reliably captures a firm's ability to access and synthesize EAI relevant knowledge, two integrative capabilities affecting project timeliness. Acquisition and synthesis activities are profiled using a small set of indicators. A simple bivariate correlation of indicator values can pinpoint specific strengths and weaknesses in management's integrative capabilities. Once identified, any shortcomings can be addressed. Thus, taken together, these tools provide managers with an ability to determine the probability of on-time project completion prior to implementation and make necessary adjustments in knowledge acquisition and synthesis to reduce IT-related delays in advance.

Our study also suggests that important perceptual differences exist between managers at different levels, which should be taken into account when assessing integrative capabilities in organizations using a federal management structure. Because the CIO has a more holistic picture of coordinated planning, the CIO perspective is a better indicator of a firm's internal knowledge integration than an IT manager's perspective. However, it is the facility IT manager that is better able to gage the intensity of user involvement. Taking these factors into consideration will improve a firm's ability to bring large-scale EAI projects in on time.

## Acknowledgments

This paper has benefitted from the insightful comments and suggestions of the senior editor, associate editor, four reviewers, Al Dexter, Barrie Nault, and Peter Scherer. I also thank the Dean's Research Fund and the Informatics Research Centre at the University of Calgary for their generous support.

## References

Agresti, A. Categorical Data Analysis, Wiley, New York, 1990.

Altman, R., and Altman, G. “An Integration Primer,” Business Integration Journal, February 2004, pp. 57-59.

Amit, R., and Schoemaker, P. “Strategic Assets and Organizational Rents,” Strategic Management Journal (14:1), 1993, pp. 33-46.

Ancona, D., and Caldwell, D. “Bridging the Boundary,” Administrative Science Quarterly (37:4), 1992, pp. 634-666.

Ancona, D., and Caldwell, D. “Improving the Performance of New Product Teams,” Research Technology Management (33:2), 1990, pp. 25-29.

Appleyard, M. “Does Knowledge Flow? Interfirm Patterns in the Semiconductor Industry,” Strategic Management Journal (17) Winter 1996, pp. 137-154.

Argote, L. “Input Uncertainty and Organizational Coordination in Hospital Emergency Units,” Administrative Science Quarterly (27), 1982, pp. 420-434.

APM. “Directing Change: A Guide to Governance of Project Management,” Association for Project Management, High Wycombe, UK, 2004 (available at http://www.apm.org.uk/Governance2.asp).

Barki, H., Rivard, S., and Talbot, J. “An Integrative Contingency Model of Software Project Risk Management,” Journal of Management Information Systems (17:4), pp. 37-70.

Blodgett, M. “Hi, Technology!,” CIO Magazine, February 15, 1998 (available online at http://www.cio.com/archive/021598/cope.html).

Box-Steffensmeier, J., and Jones, B. Event History Modeling: A Guide for Social Scientists, Cambridge University Press, Cambridge, UK, 2004.

Box-Steffensmeier, J., and Zorn, C. “Duration Models and Proportional Hazards in Political Science,” American Journal of Political Science (45), October 2001, pp. 951-967.

Boynton, A., Zmud, R., and Jacobs, G. “The Influence of IT Management Practice on IT Use in Large Organizations,” MIS Quarterly (18:3), 1994, pp. 299-320.

Breshnahan, J. “Mixed Messages.” CIO Magazine (9:15), May 15, 1996 (available online at http://www.cio.com/archive/051596/mixed\_1.html).

Broadbent, M., Weill, P., and St. Clair, D. “The Implications of Information Technology Infrastructure for Business Process Redesign,” MIS Quarterly (23:2), 1999, pp. 159-182.

Brown, C. “Horizontal Mechanisms Under Differing IS Organization Contexts,” MIS Quarterly (23:3), 1999, pp. 421-448.

Brown, C., and Magill, S. “Alignment of the IS Function with the Enterprise: Toward a Model of Antecedents,” MIS Quarterly (18:4), 1994, pp. 371-403.

Brooks, F. The Mythical Man-Month, Addison-Wesley, Boston, 1995.

Chuang, P., and Fusco, G. “Integrating Data and Applications: Enterprise Application Integration,” Inews, University of California, Berkeley, October 1, 2003 (available online at http://istpub.berkeley.edu:4201/bcc/Fall2003/eai.html).

CIO Magazine. “The State of the CIO,” CIO Magazine, March 1, 2002 (available online at http://www.cio.com/archive/030102/intro.html).

Cleland, D. Project Management: Strategic Design and Implementation, McGraw-Hill, New York, 2002.

Cleves, M., Gould, W., and Guiterrez, R. An Introduction to Survival Analysis Using Stata, Stata Press, College Station, TX, 2004.

Converse, J., and Presser, S. Survey Questions: Handcrafting the Questionnaire, SAGE Publications, Newbury Park, CA, 1986.

Cooper, R., and Kleinschmidt, E. “Determinants of Timeliness in Product Development,” Journal of Product Innovation Management (11), 1994, pp. 381-396.

CXO Systems. “CIO Metrics and Decision-Making Survey Results,” Waltham, MA, 2003 (available online at www.cxosystems.com).

DeSanctis, G., and Jackson, B. “Coordination of Information Technology Management,” Journal of Management Information Systems (10:4), 1994, pp. 85-111.

Enns, H., Huff, S., and Higgins, C. “CIO Lateral Influence Behaviors: Gaining Peer Commitment to Strategic Information Systems,” MIS Quarterly (27:1), 2003, pp. 155-176.

Galunic, D., and Eisenhardt, K. “Architectural Innovation and Modular Corporate Forms,” Academy of Management Journal (44:6), 2001, pp. 1229-1250.

Grambsch, P., and Therneau, T. “Proportional Hazards Tests and Diagnostics Based on Weighted Residuals,” Biometrica (81:3), 1994, pp. 515-526.

Grant, R. “Prospering in Dynamically-Competitive Environments: Organizational Capability as Knowledge Integration,” Organization Science (7:4), 1996, pp. 375-387.

Gupta, A., and Wilemon, D. “Accelerating the Development of Technology-Based New Products,” California Management Review (32:2), 1990, pp. 24-44.

Harlow, H. F. “The Formation of Learning Sets,” Psychological Review (56), 1959, pp. 51-65.

Hartwick, J., and Barki, H. “Explaining the Role of User Participation in Information System Use,” Management Science (40:4), 1994, pp. 440-466.

Henderson, R. “The Evolution of Integrative Capability: Innovation in Cardiovascular Drug Discovery,” Industrial and Corporate Change (3:3), 1994, pp. 607-630.

Henderson, R. “Underinvestment and Incompetence as Responses to Radical Innovation: Evidence from the Photolithographic Alignment Equipment Industry,” Rand Journal of Economics (24:2), 1993, pp. 248-267.

Henderson, R., and Clark, K. “Architectural Innovation: The Reconfiguration of Existing Product Technologies and the Failure of Established Firms,” Administrative Science Quarterly (35), 1990, pp. 9-30.

Henderson, R., and Cockburn, I. “Measuring Competence? Exploring Firm Effects in Pharmaceutical Research,” Strategic Management Journal (15: Special Issue), Winter 1994, pp. 63-84.

Hunton, J., and Beeler, J. “Effects of User Participation in Systems Development: A Longitudinal Field Experiment,” MIS Quarterly (21:4), 1997, pp. 359-389.

Iansiti, M. “How the Incumbent Can Win: Managing Technological Transitions in the Semiconductor Industry,” Management Science (46:2), 2000, pp. 169-185.

Johnson, M. “Credibility Challenged,” Computerworld (37:20), May 19, 2003, p. 22.

Kahneman, D., and Lovallo, D. “Timid Choices and Bold Forecasts: A Cognitive Perspective on Risk Taking,” Management Science (39:1), 1993, pp. 17-31.

Kahneman, D., and Tversky, A. “Prospect Theory: An Analysis of Decision Under Risk,” Econometrica (47:2), 1979, pp. 263-290.

Kleinbaum, D., and Klein, M. Survival Analysis, Springer-Verlag, New York, 1996.

Kogut, B., and Zander, U. “Knowledge of the Firm, Combinative Capabilities and the Replication of Technology,” Organization Science (3:3), 1992, pp. 383-397.

Lawrence, P., and Lorsch, J. Organization and Environment, Harvard Business School Press, Boston, 1967.

Leonard-Barton, D. “Core Capabilities and Core Rigidities,” Strategic Management Journal (13:Special Issue), 1992, pp. 111-126.

Liebeskind, J., Oliver, A., Zucker, L., and Brewer, M. “Social Networks, Learning, and Flexibility: Sourcing Scientific Knowledge in New Biotechnology Firms,” Organization Science (7:4), 1996, pp. 428-443.

Lovallo, D., and Kahneman, D. “Delusions of Success: How Optimism Undermines Executives’ Decisions,” Harvard Business Review (81:7), 2003, pp. 56.

Lucas, H. “Systems Quality, User reactions, and the Use of Information Systems,” Management Informatics (3:4), 1974, pp. 207-212.

MacCormack, A., Verganti, R., and Iansiti, M. “Developing Products on ‘Internet Time’: The Anatomy of a Flexible Development Process,” Management Science (47:1), 2001, pp. 133-150.

Marjchrzak, A., Cooper, L., and Neece, O. “Knowledge Reuse for Innovation,” Management Science (50:2), 2004, pp. 174-188.

McFarlan, W. “Portfolio Approach to Information Systems,” Harvard Business Review (59:5), 1981, pp. 142-151.

Mitchell, V., and Zmud, R. “The Effects of Coupling IT and Work Process Strategies in Redesign Projects,” Organization Science (10:4), 1999, pp. 424-438.

Nagarajan, A., and Mitchell, W. “Evolutionary Diffusion: Internal and External Methods Used to Acquire Encompassing, Complementary, and Incremental Technological Changes in the Lithotripsy Industry,” Strategic Management Journal (19:11), 1998, pp. 1063-1078.

Nidumolu, S. “The Effect of Coordination and Uncertainty on Software Project Performance: Residual Performance Risk as an Intervening Variable,” Information Systems Research (6:3), 1995, pp. 191-210.

Nonaka, I. “A Dynamic Theory of Organizational Knowledge Creation,” Organization Science (5:1), 1994, pp. 14-37.

Okhuysen, G., and Eisenhardt, K. “Integrating Knowledge in Groups: How Formal Interventions Enable Flexibility,” Organization Science (13:4), 2002, pp. 370-386.

Pawlowski, S., and Robey, D. “Bridging User Organizations: Knowledge Brokering and the Work of Information Technology Professionals,” MIS Quarterly (28:4), 2004, pp. 645-673.

Pennings, J., and Harianto, F. “The Diffusion of Technological Innovation in the Commercial Banking Industry,” Strategic Management Journal (13:1), 1992, pp. 29-46.

Perks, M. “Best Practices for Software Development Projects,” Computerworld, September 29, 2003 (available online at http://www.computerworld.com/managementtopics/management/story/0,10801,85198,00.html?f=x247).

Pisano, G. “Learning-Before-Doing in the Development of New Process Technology,” Research Policy (25:7), 1996, pp. 1097-2020.

Plewa, J., and Pliskin, S. “Client/Server Everything,” CIO Magazine, July 1, 1995 (available online at http://www.cio.com/archive/070195/outlo.html).

Podsakoff, P. M., and Organ, D. W. “Self-Reports in Organizational Research: Problems and Prospects,” Journal of Management (12:4), 1986, pp. 531-544.

Reich, B. H., and Benbasat, I. “Measuring the Linkage Between Business and Information Technology Objectives,” MIS Quarterly (20:1), March 1996, pp. 55-81.

Robey, D., and Farrow, D. L. “User Involvement in Information System Development,” Management Science (28:1), 1982, pp. 73-85.

Sambamurthy, V., and Zmud, R. “Arrangements for Information Technology Governance: A Theory of Multiple Contingencies,” MIS Quarterly (23:2), 1999, pp. 261-290.

Schmidt, R., Lyytinen, K., Keil, M., and Cule, P. “Identifying Software Project Risks,” Journal of Management Information Systems (17:4), 2001, pp. 5-37.

Slater, D. “Middleware Demystified,” CIO Magazine, May 15, 2002 (available online at http://www.cio.com/archive/051500/middle.html).

Stevens, J. Applied Multivariate Statistics for the Social Sciences, Lawrence Erlbaum Associates, Publishers, Hillsdale, NJ, 1986.

Stone, E. Research Methods in Organizational Behavior, Scott, Foresman and Company, Glenview, IL, 1978.

Swoyer, S. “Successful Project Management: Best Practices of World-Class Companies,” Enterprise Systems Journal, June 24, 2003 (available online at http://www.esj.com/news/article.aspx?EditorialsID=596).

Tabachnick, B., and Fidell, L. Using Multivariate Statistics ( $4^{th}$ ed.), Allyn and Bacon, Needham Heights, MA, 2001.

Tait, P., and Vessey, I. “The Effect of User Involvement on Systems Success: A Contingency Approach,” MIS Quarterly (12:1), 1988, pp. 91-108.

Tasi, W. “Knowledge Transfer in Intraorganizational Networks: Effects of Network Position and Absorptive Capacity on Business Unit Innovation and Performance,” Academy of Management Journal (44:5), 2001, pp. 996-1004.

Taylor, S., and Brown, J. “Illusion and Well-Being,” Psychological Bulletin (103:2), 1988, pp. 193-210.

Teece, D., Pisano, G., and Shuen, A. “Dynamic Capabilities and Strategic Management,” Strategic Management Journal (18:7), 1997, pp. 509-533.

Terwiesch, C., and Loch, C. “Measuring the Effectiveness of Overlapping Development Activities,” Management Science (45:4), 1999, pp. 455-465.

Thomas, L. G. “The Two Faces of Competition: Dynamic Resourcefulness and the Hypercompetitive Shift,” Organization Science (7:3), 1996, pp. 221-243.

Thomas-Hunt, M., Ogden, T., and Neale, M. “Who’s Really Sharing: Effects of Social and Expert Status on Knowledge Exchange Within Groups,” Management Science (49:4), 2003, pp. 464-477.

Van de Ven, A., Delbecq, A., and Koenig, R. “Determinants of Coordination Modes Within Organizations,” American Sociological Review (41:2), 1976, pp. 322-338.

Varon, E. “The State of the CIO: Responsibilities,” CIO Magazine, March 1, 2002 (available online at http://www.cio.com/archive/030102/responsibilities.html).

Varon, E., and Ware, L. “The State of the CIO Around the World,” CIO Magazine, April 1, 2005 (available online at http://www.cio.com/archive/040105/stateofcio.pdf).

Verona, G. “A Resource Based View of Product Development,” Academy of Management Review (24:1), 1999, pp. 132-143.

Wallace, L., and Keil, M. “Software Project Risks and Their Affects on Outcomes,” Communications of the ACM (47:4), 2004, pp. 68-73.

Zander, U., and Kogut, B. “Knowledge and the Speed of the Transfer and Imitation of Organizational Capabilities: An Empirical Test,” Organization Science (6:1), 1995, pp. 76-92.

Zollo, M., and Winter, G. “Deliberate Learning and the Evolution of Dynamic Capabilities,” Organization Science (13:3), 2002, pp. 339-353.

## About the Author

Victoria L. Mitchell is an associate professor in the Haskayne School of Business at the University of Calgary. She has a Ph.D. in Information Systems, an MBA, and a B.S.N. from Florida State University, and a B.Sc. in Human Resource Development from Oakland University. Her research examines the use of information technology in networked organizations, and more generally the use of knowledge in high technology firms. She has been on faculty at The Ohio State University, the University of Washington, the University of California at Los Angeles, and North Carolina State University. Her research appears in Organization Science, Management Science, and Decision Sciences, among others outlets.

## Appendix

## Telephone Interview Guide

Conducted prior to project implementation.

Title of Health Network:

CIO:

Please describe the project: If not provided in the description we specifically ask about

IT project start date:

Projected completion date:

Number of facilities involved:

Number of interfaces to be constructed:

Number of programmers dedicated to those interfaces:

How long do you expect it will take to implement the project?

On a scale of 1 to 7, with 1 meaning extremely inadequate, 4 meaning adequate, and 7 meaning extremely adequate, how would you characterize the budget for this project?

Conducted shortly after project completion

Project's actual completion date:

If actual date is after estimated completion date, CIOs were asked

What was the primary reason for project delay?

If IT issues were the primary source of delay, CIOs were asked

In your opinion, what was the underlying cause of (IT issue)? Please elaborate.

How was the situation resolved?

On a scale of 1 to 7, with 1 meaning ery low, 4 meaning moderate, and 7 meaning very high, how would you characterize the level of user involvement for this project?

## Survey Instrument

Please indicate the extent to which you agree with the following statements.

Items measured on a seven-point Likert scale, $1 =$ strongly disagree, $4 =$ neutral, $7 =$ strongly agree

1. Clinical personnel are involved in IT planning.

2. The IT strategy supports the redesign strategy for our clinical processes.

3. The information needs of evolving clinical processes were considered when formulating the IT plan.

4. An assessment of IT strengths and limitations was utilized in the clinical redesign plan.

5. An assessment was made of relevant IT trends prior to implementing the redesign project.

6. Clinical managers are aware of IT objectives.

7. IT personnel are aware of clinical redesign objectives.

8. I am an active member of a professional association that kept me informed about changes in interface engines, messaging brokers, network integration and related project management issues.

9. I attended workshops and/or conferences on messaging standards, interface engines, network integration and project management issues prior to project implementation.

10. I subscribe to literature that kept me informed about new developments in application integration.

## Please circle all that apply.

11. Prior to implementing this project

a. I had several years experience managing IT platform redesign projects.

b. I had several years experience managing work process redesign that utilized IT.

c. I had several years experience managing network integration projects.
