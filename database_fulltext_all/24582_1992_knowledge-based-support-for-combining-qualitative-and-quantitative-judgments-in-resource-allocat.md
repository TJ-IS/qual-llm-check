---
otero_id: 24582
otero_key: "D4FBPB9Y"
title: "Knowledge-Based Support for Combining Qualitative and Quantitative Judgments in Resource Allocation Decisions"
authors: "Ritu Agarwal; Mohan R. Tanniru; Marcos Dacruz"
year: "1992"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1992.11517952"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge-Based Support for Combining Qualitative and Quantitative Judgments in Resource Allocation Decisions

Ritu Agarwal, Mohan R. Tanniru & Marcos Dacruz

To cite this article: Ritu Agarwal, Mohan R. Tanniru & Marcos Dacruz (1992) Knowledge-Based Support for Combining Qualitative and Quantitative Judgments in Resource Allocation Decisions, Journal of Management Information Systems, 9:1, 165-184, DOI: 10.1080/07421222.1992.11517952

To link to this article: http://dx.doi.org/10.1080/07421222.1992.11517952

![](/api/attachments/D4FBPB9Y/fulltext/images/a57695b17cfbab1c2affc0a4fa095b0ad1fe5a4a00095a5af4b96f9cb2638365.jpg)

Published online: 16 Dec 2015.

![](/api/attachments/D4FBPB9Y/fulltext/images/59d16bb63ac1f8a75e9e11b550e18007ab585e11dabe477f12cbba44cf9908b9.jpg)

Submit your article to this journal ↗

![](/api/attachments/D4FBPB9Y/fulltext/images/fbc15060e2b6b9b5028657ab59d6a420293fe8e52f021d71d8af27f454a4423e.jpg)

View related articles ↗

![](/api/attachments/D4FBPB9Y/fulltext/images/6ba2533ac944b263e5854b1fdb2288b78ee6c95cf153684a601890e71e7d74de.jpg)

Citing articles: 9 View citing articles ↗

# Knowledge-Based Support for Combining Qualitative and Quantitative Judgments in Resource Allocation Decisions

RITU AGARWAL, MOHAN R. TANNIRU, AND MARCOS DACRUZ

RITU AGARWAL is an Assistant Professor in the Department of MIS and Decision Sciences at the University of Dayton. She received her Ph.D. in MIS and her M.S. in computer science from Syracuse University. Professor Agarwal's publications have appeared or are forthcoming in Journal of Management Information Systems, Information and Management, OMEGA, Decision Support Systems, Knowledge-Based Systems, International Journal of Man–Machine Studies, Knowledge Acquisition, and elsewhere. She has presented papers at several national and international meetings. Her research interests are in knowledge acquisition, expert system development and validation, decision support systems, and group decision making.

MOHAN R. TANNIRU is an Associate Professor of MIS in the School of Management at Syracuse University. He received his Ph.D. in MIS from Northwestern University. He has published in a number of journals and presented papers at various meetings. Dr. Tanniru has consulted with several corporations in the area of expert and knowledge-based systems and technology management, including the Carrier Corporation, Bristol-Myers, and Tata Consultancy Services. His current research interests are in systems analysis and design, decision support systems, and expert systems.

MARCOS DACRUZ works in the Expert Systems area at Carrier–United Technologies Corporation and was involved in developing an expert system for configuring an air-handling unit. He has an M.B.A. degree from Syracuse University with a concentration in MIS and finance. Prior to joining the M.B.A. program, he worked with Andersen Consulting in Brazil.

ABSTRACT: The allocation of scarce resources to competing information systems project opportunities is a key activity performed by the MIS planning group. Performing this task typically involves consideration of both quantitative as well as qualitative aspects of projects. Research in human information processing and cognitive psychology suggests that decision makers are often subject to biases that tend to assign greater salience to quantitative as opposed to qualitative and intangible factors. To help overcome such biases and to provide flexible decision support to the project selection committee, a knowledge-based system has been developed. Knowledge captured in the system was extracted from industry practitioners responsible for the project selection decision. The system architecture represents an integration of database, modeling, and expert system capabilities. It supports both intelligence and design phases of project selection and can assess the impact of a selected portfolio on an organization's cash flow. The operation of the system is illustrated through an extended example.

KEY WORDS AND PHRASES: knowledge-based support, information systems projects, multi-criteria decision making, project selection, qualitative factors.

## 1. Introduction

THE DETERMINATION OF HOW A FIXED AMOUNT of resource is to be allocated among competing project opportunities is an important decision made at many levels of an organization. In the context of information systems, project selection is a key activity performed by the MIS planning group. Successful planning for the utilization of information technology is rapidly becoming a crucial determinant in an organization's long-term ability to survive and compete [18, 20, 23]. Specific tasks performed in MIS planning include both the identification of information systems that will support strategic and operational activities, as well as the effective allocation of limited resources to developing these systems.

Several methodologies for supporting either or both MIS planning tasks have been described in the literature. For example, Porter [22] identifies five forces of competition (buyers, sellers, competitors, substitutes, and new entrants) that affect the competitiveness of a firm, and indicates that information technology (IT) can play a strategic role in influencing these forces. Specifically, the effects of information technology on the value chain [21] can form the basis for generating alternative strategies in order to gain a competitive advantage. Strategies and objectives developed by an organization through such methods can be related to alternate information systems proposals using techniques such as strategic set transformation [15] and business systems planning [13].

We focus on the second aspect of the MIS planning exercise: that is, the selection of projects to be undertaken from a given pool of candidate projects. Criteria suggested as useful in prior research for evaluating competing systems proposals have ranged from strictly quantitative, measurable considerations such as net present value, return on investment, and payback period, to more qualitative, intangible factors, including project risk and the project's relationship with strategic needs and organizational culture [5, 8, 10, 16, 19]. Among the qualitative considerations, particular importance has been accorded to the risk dimension, which has been related to various system characteristics such as complexity, budget, development time, and newness of technology [8, 10]. Risk is also inherent if a particular system has a negative impact on one objective and a positive impact on another [28]. Further, although prior research has emphasized the significance of the political dimension in system prioritization [4, 6], no formal mechanisms have been provided to relate this dimension to systems that are proposed.

Despite the presence of qualitative factors being acknowledged, methodologies proposed for system prioritization have focused primarily on the quantitative attributes of projects. Most techniques that do attempt to incorporate nonquantitative dimensions do so along with other quantitative dimensions such as tangible costs and benefits. A questionable assumption underlying these procedures is that they regard decision makers in a normative light as idealized rational agents who are able to adequately assess and weigh the importance of various data in decision making. The methodologies fail to account for errors of judgment that can frequently lead to biased choice processes and an associated nonoptimal allocation of resources [11, 26]. Biases are particularly pervasive in multiattribute decision-making situations, where several disparate and incompatible aspects of each choice must be considered simultaneously.

Of particular salience to the problem of project selection is the consideration of both the quantitative and qualitative aspects of a project. Typically, in a situation where all aspects of a system are considered simultaneously, there can be a tendency to weigh the quantitative or concrete criteria (such as payback period, net present value, etc.) more heavily than qualitative and abstract criteria $[25]$ (such as congruence with strategic objectives, effect on productivity, etc.). Within MIS planning, this type of bias can result in a negative consequence in that the disproportionate influence wielded by the quantitative criteria could cause projects that are financially attractive but strategically less so to be assigned a higher priority. Further, given that project benefits in an IS context tend to be, more often than not, “soft” and intangible in nature, an explicit recognition of this bias is even more critical.

Current methods for the project selection decision suffer from some inherent limitations. Quantitative models such as internal rate of return (IRR) and net present value (NPV) are unable to incorporate qualitative criteria in their computations. To overcome this limitation, qualitative criteria are often reduced to numerical quantities and combined using some method of weighting and scoring using a multi-criteria decision-making (MCDM) model such as multi-attribute utility theory (MAUT) [9]. However, since qualitative judgments usually tend to be measured on different dimensions, the results of their combination using quantitative algorithms becomes difficult to interpret. Further, the information requirements of MCDM models often place a significant cognitive burden on decision makers who are required to supply a large number of values for model parameters [29].

In order to provide an adequate level of decision support for the project selection decision, mechanisms for the explicit capture and dissemination of qualitative judgments and past experience are required. Knowledge-based systems technology allows an organization to combine quantitative and qualitative considerations flexibly. This process is further facilitated by advances in connectivity that permit systems to access databases and external routines to obtain and manipulate quantitative data. An organization can, thus, still use traditional methods such as NPV or IRR for project evaluation, and, at the same time, assess the impact of such an evaluation on qualitative or subjective criteria.

Our research has focused on the development of a knowledge-based system that supports an integrated approach to project evaluation. It builds on recent interest in combining technologies to provide support for unstructured and judgmental decisions involving a multiplicity of objectives $[12, 27]$ . Prior work is extended and enhanced in two major ways: first, the system illustrates how disparate technologies can be successfully combined to provide flexible decision support, and, second, it incorporates the procedural or descriptive rationality of industry experts responsible for the project selection decision. The system allows for simultaneous or independent consideration of both subjective and objective criteria. It consists of a core knowledge base that contains rules considered relevant by MIS planning groups in their subjective evaluation of individual projects. These rules constitute both established organizational guidelines and directives, as well as personal heuristics that decision makers have developed over time. Further, meta-rules for ordering projects so that they may be considered incrementally are also included. The decision-making group or individual has the flexibility of choosing the class of criteria they wish to use to evaluate projects, while the system provides them with the option of combining criteria if they so desire.

The organization of this article is as follows: The next section discusses salient aspects of the project selection decision and describes the architecture of the knowledge-based support system. Sources of knowledge for the system are also identified. The third section details the operation of the system for a variety of decision scenarios. The last section concludes with some extensions to this research.

## 2. The Project Selection Decision

TRADITIONAL PROJECT SELECTION APPROACHES can be categorized as either value measurement or portfolio selection models. Value measurement approaches such as checklist models, scoring models, multi-attribute utility theory, and economic index models concentrate on the development of procedures for comparing and evaluating multi-attribute alternatives. Portfolio models generally attempt to optimize some value function subject to the fact that the organization is operating in a constrained environment. Linear and chance constrained programming models fall under this category. Several multi-attribute choice models are reviewed in [12] and [29]. Some limitations associated with such modeling approaches include:

\- inadequate treatment of multiple, often interrelated criteria;

\- inability to recognize and treat nonmonetary and qualitative aspects;

\- inability to facilitate, in a decision support mode, the testing of various assumptions and judgments implicitly or explicitly made in project prioritization;

\- restrictive assumptions such as independence among attributes; and

\- placement of high demands on decision makers in terms of both information requirements and complexity.

Viewing the project selection activity as a decision-making process [24], we note that the intelligence phase is concerned with gathering relevant knowledge about each candidate project and the criteria used to make a final decision; the design phase relates project characteristics to the various criteria; and the choice phase requires the use of an appraisal strategy to arrive at a final decision (a project portfolio). A lack of structure is typically evident in both design and choice phases. In the design phase, this unstructure may be caused by ill-defined or incomplete knowledge about relationships between project features and the criteria established, especially when these criteria depend on judgments related to a project's strategic role, complexity, risk, and the like. In the choice phase, a lack of structure is exhibited when the exact method (or appraisal strategy) that is used to select a project portfolio is unclear. Our goal is to address the potential lack of structure in these two phases by providing knowledge-based support for the design phase and decision support for the choice phase. All three decision-making phases, as they relate to the project selection decision, are discussed in detail below, along with the components of the system architecture developed to support them (figure 1).

## Intelligence Phase

We assume that the first step in the MIS planning process has already been completed, that is, that various candidate projects have been identified and their characteristics (objectively or subjectively measured) established by users or the corporate community. For example, objective measures such as NPV, Payback, or IRR may be calculated from the projected cash inflows/outflows associated with each project using standard computational models. In the system architecture, the computational models to estimate quantitative characteristics are stored in a model base. Other subjective information such as a user's assessment of a project's development time or the type of technology it uses is extracted directly from the user/system developer. These data are then stored in a database for subsequent manipulation. While we assume that the data are known prior to undertaking the project selection decision, the system does allow a user to evaluate the sensitivity of a recommended project portfolio to changes in these data values.

## Design Phase

The criteria used to make project selection decisions and their relationship to various project characteristics are typically very subjective, unless the decision is strictly based on quantitative considerations. Relationships may be composed of heuristics that an individual or an organization acquires over a period of time and can be highly domain- and organization-specific. As these relationships vary frequently, the support provided by the system should allow sufficient flexibility to modify and custom-tailor them to fit each case as needed. The heuristic nature of this knowledge and the flexibility needed to manipulate and modify such knowledge frequently requires the use of knowledge-based technology to support this phase.

A structured interviewing technique was used to gather information on the criteria and the relationships among these criteria relevant to the resource allocation decision. Over thirty industry experts responsible for resource allocation have participated in this study. The methodology of content analysis was applied to the interview transcripts to extract the experts' reasoning processes $[1, 2]$ . Content analysis is a data filtering technique that allows data generated by a communication (written, verbal, visual, etc.) to be transformed into a form that is conducive to subsequent analysis $[17]$ . Four content analytic schemes: one each for relationships, criteria, equivocal situations, and quantitative/qualitative categorization were used.

This part of the knowledge is subject to continual change or update and the support system should allow for modifications as needed. Updates to the knowledge may be caused by changes in the decision environment over time, changes in organizational philosophies, a change in the decision makers, and so on. As a matter of fact, the support system can be used to allow an individual or a group to make a decision independently of the system and subsequently compare it with what the system would have recommended based on the organizational expertise embedded in the knowledge base. The criteria (or parameters) and their dependencies are shown in the form of a network in figure 2 and will be used here to illustrate the selection process. These dependencies form a part of the knowledge-based component of the support system, which has hooks to model and databases to facilitate computation and storage of data values. The transfer of information from one subsystem to another is transparent to the user.

![](/api/attachments/D4FBPB9Y/fulltext/images/83e627fad0aa3ab607410889d10931f29835d0e5adfd8d8938b5d4229fe86503.jpg)  
Figure 1. Architecture of the Decision Support System

## Choice Phase

The project selection process exemplifies a multiple attribute decision-making problem, where one or more selections are made from a finite set of alternatives. Several models can be used to facilitate the choice process, and the choice of a specific model is usually based on factors such as: nature of information (ordinal, cardinal, etc.) used for comparison, and the type of comparison possible (pairwise comparison, preference proximity between alternatives, etc.) [29]. The architecture described here can be linked to any of the MADM models based on their suitability. The current architecture provides the following functionality to the decision-making unit (individual or group):

![](/api/attachments/D4FBPB9Y/fulltext/images/be44dbad59fc4cba976795ff7cd98af32e384a9d6691ddb9112d9e0882fb652d.jpg)  
Figure 2. Parameter Dependency Network

1. Users may request quantitative and qualitative ranks for each project independently or simultaneously. This will partly address the issue of information bias associated with concrete data discussed earlier.

2. Users may provide a set of rules to guide the integration of these independent ranks in order to evolve an overall rank. This facility allows the knowledge to become organization-specific and monitors its consistency or validity over time (this feature is illustrated subsequently).

3. Users may request a link to any multi-attribute model so that the data on various attributes can be properly weighted to arrive at a final decision, as determined by the multi-attribute model (the current system does not provide this facility).

4. Users may simply request that the projects be rank ordered on multiple-dimensions so she or he can use any type of data manipulation language, on an ad-hoc basis, to generate the needed prioritization. This facilitates the use of such a system in a group decision context for brainstorming and assumption testing.

5. Users can input their choice of projects and the system will list all the internally stored heuristics that are violated by this ranking. This type of ex-post analysis of the project selection process allows one group to compare their criteria against the a priori stored organizational knowledge and, possibly, alter either the knowledge stored or the choices made.

6. Users may provide a budgetary constraint or cash flow limitations, and the system provides the impact of a chosen system selection strategy on either of these factors. This is useful not only to determine the number of projects that can be effectively funded, but also to observe their impact on the development risk or funds flows, if the chosen systems are implemented in a different order.

The features described above are derived from our work with three different organizations (a government unit housed within the Department of Health and Social Services, a public utility, and a medical equipment manufacturer). The governmental unit that has participated in the study is responsible for billing and collecting for medical care and services provided at three state mental health institutions and three centers for the developmentally disabled. It has over thirty employees and serves 5,000 to 6,000 patients. The issue of separating qualitative and quantitative dimensions for systems planning was considered critical there as the unit has to serve several external clients with varied demands (often qualitative) and the influence of political factors is fairly dominant. A detailed study of this case and the outcome of the planning process is discussed elsewhere [3].

The use of multiple criteria models for selecting alternatives and studying their impact on budgetary constraints was addressed in a study undertaken with a major utility company in the Midwest as it attempted to look at computerizing its cash management operations. The organization here asked for a linkage between project selection decisions and the budgetary process, so that it can study the sensitivity of project selection to assumptions made about costs and risks. The results of this study are reported elsewhere $[14]$ .

The study with the medical equipment manufacturer $[10]$ surfaced the need to consider both ad-hoc ranking of projects by a steering committee and a testing of these rank orders against assumptions made in the past to see how consistent the decisions are over time. A knowledge-based approach to capturing the heuristics used in the past was considered critical in order to monitor consistency in decisions over time. The specifications for the system presented here are, thus, derived from our investigation of the project selection decision within several MIS organizations; the three organizations provided insights into the necessary functionality that such a system ought to provide, while the interviews with experts provided the specific knowledge captured in the system.

Models for estimating the quantitative characteristics of a project were developed and programmed in the Interactive Financial Planning System (IFPS) software. IFPS is a decision support system generator that allows for easy construction of quantitative models. Subjective criteria were captured in the form of rules in IBM's mainframe expert system shell, ES/E. The qualitative project data are stored in a database implemented using IBM's Structured Query Language/Data System (SQL/DS) software. The knowledge encapsulated in the expert system is used to synthesize the model and database information in order to arrive at project rankings on a variety of dimensions. The outcome of this procedure is stored in the SQL/DS database for further analysis and the IFPS model output is used to perform cash flow analysis.

The potential benefits to an organization obtainable through utilizing such a system can be numerous. First, the encapsulation of decision-making knowledge in an electronic medium enforces longitudinal consistency in decisions made. Second, decisions about a particular project portfolio can be explained and justified on the basis of the guidelines formalized as rules. Since such decisions are most likely made at many different levels of an organization, the potential utilization of the system can be high. The initial investment and the experience gained through system development can be transported to other levels relatively easily. The system provides an on-line memory of corporate knowledge as the firm's dynamics and priorities change. The rule-based programming environment provides for easy updates and changes to the knowledge captured. Finally, while the system is constructed primarily to obtain a rank ordering of projects, it is possible to assess the impacts on cash flows for a given portfolio.

## 3. The Knowledge-Based Support System

AS INDICATED EARLIER, IT IS ASSUMED that the number of projects and their characteristics (objective and subjective) are provided to the knowledge base for manipulation and analysis. Since the data used to build the model and databases are dependent on the heuristics an organization uses to make their selection, the knowledge base is discussed first. Figure 2 provides an outline of the criteria (parameters in the terminology of the expert systems shell) and their dependencies both at the parameter level as well as at the rule level (how each value for a parameter is established) in the form of a parameter dependency network. The overall rank of a project depends on a synthesis of both the qualitative and quantitative ranks established independently, and these, in turn, are dependent on other intermediate parameters such as risk and cost of capital.

The major subgoals of the project selection process, as depicted in the dependency network, are to obtain an overall qualitative and a quantitative rank for each project. The qualitative rank is dependent on five parameters: project risk, the political dimension, the strategic dimension, the philosophical dimension, and the extent to which the project satisfies the needs of a number of users (user needs). IS project selection (like many other resource allocation decisions) is frequently made against a backdrop of political considerations, such as the relative importance of the users or department who propose the project within the organization's formal or informal hierarchy. The political dimension attempts to capture this subjective assessment which can be a critical factor in obtaining support and commitment for the project once it has been selected $[4, 6]$ . The strategic dimension assesses the extent to which the project meets the strategic objectives of the organization. An organization's philosophy in performing its mission must be compatible with proposed project characteristics in order to generate greater corporate commitment, as measured by the philosophical dimension. For example, an organization that has historically been a technology follower might be less inclined to support leading-edge technology proposals. Further, projects that simultaneously satisfy the needs of a large number of users are “preferred” to those whose benefits are reaped by a limited number.

Project risk, in turn, is estimated as a function of the following project characteristics: (1) whether the project uses new technology with which the organization has no experience; (2) the complexity of the project in terms of the number of systems that need to be interfaced and processes that need to be automated (complexity); (3) the estimated development time required for the project; and (4) the degree to which the project exhibits a positive impact on one objective and a negative impact on another. As an example for the last parameter, a project may rank extremely high in terms of fulfilling a pressing objective of employee productivity, but may rank extremely low on an organizational policy of not laying off employees. In sum, the risk parameter attempts to assess the inverse of the extent to which the organization can be confident of obtaining the potential benefits identified for a project.

The quantitative rank of a project is obtained by evaluating the returns associated with it using internal rate of return and payback models, in conjunction with the cost of capital to the firm. In addition, the project category is also a consideration here, as it impacts the desired return on investment. The categories included in the knowledge base are new development, enhancement/maintenance to existing systems, mandatory projects (including audit-related projects), and research and development proposals. The cost of capital for the organization is determined by external economic conditions.

Notice that the knowledge extracted from the experts suggests that their subjective models of the resource allocation process are essentially compensatory in nature; that is, an implicit commensurability across attributes is seen to exist. The experts appeared to seek values for all project dimensions (the parameters in the network) prior to ranking them and arriving at a final portfolio.

While the parameters defined in the dependency network provide the overall dependency information, the rules described in Tables 1.1 through 1.5 provide a select set of heuristics incorporated in the current version of the knowledge base that guide the establishment of the values assumed by these parameters. An organization can choose to alter either the network (if they include other criteria in the project selection decision) or the rules that guide the establishment of their values to fit its constraints. Given the network, the knowledge-based environment requires that either the user provide the information on input parameters interactively, or that the data be obtained from a database or external procedures that establish these values. As indicated previously, most of the quantitative data such as payback and IRR come from a model base defined to compute these values based on projected cash flows associated with projects, while other information such as complexity, development time, and the like is obtained from a database. However, some information such as a project's relationship to corporate strategies or philosophical relationship of the project to the corporation's culture may be input by the steering committee (or user group) interactively when the system is being consulted. This allows for a greater discussion of the project among the group's participants in order to reach a consensus on the relationship of the project to these crucial dimensions.

The rest of this section will illustrate the operation of the system as it uses the knowledge acquired from resource allocation experts to support the project rank ordering process. The use of various features identified under the choice phase are illustrated to demonstrate their value in such a decision-making process. The characteristics of the projects under consideration are outlined in Table 2.

## 3.1. Consultation with the System

At the outset, the system uses project characteristics to rank-order the projects on quantitative and qualitative dimensions separately. In Table 3, projects are rank ordered on the quantitative dimension based on IRR (highest to lowest) and on the qualitative dimension according to the five separate dimensions. Each of these ranks can be presented in any order, allowing the steering committee to observe qualitative ranks prior to presenting the quantitative ranks, thus avoiding the issue of information bias associated with concrete data.

Table 1.1 Rules for Estimating Risk

<table><tr><td colspan="4">INPUT PARAMETERS</td><td>OUTPUT</td></tr><tr><td>new technology</td><td>complexity</td><td>development time</td><td>conflicting impact</td><td>risk</td></tr><tr><td rowspan="7">Y</td><td>H</td><td>-</td><td>Y</td><td>H</td></tr><tr><td>H</td><td>&lt;2</td><td>N</td><td>M</td></tr><tr><td>L</td><td>&lt;2</td><td>N</td><td>M</td></tr><tr><td>L</td><td>&gt;=2</td><td>N</td><td>M</td></tr><tr><td>M</td><td>&gt;=2</td><td>N</td><td>H</td></tr><tr><td>M</td><td>&lt;2</td><td>N</td><td>M</td></tr><tr><td>M</td><td>-</td><td>Y</td><td>H</td></tr><tr><td rowspan="8">N</td><td>H</td><td>&lt;2</td><td>N</td><td>M</td></tr><tr><td>H</td><td>&gt;=2</td><td>N</td><td>H</td></tr><tr><td>M/L</td><td>&lt;2</td><td>N</td><td>L</td></tr><tr><td>H</td><td>-</td><td>Y</td><td>H</td></tr><tr><td>M</td><td>&gt;=2</td><td>N</td><td>M</td></tr><tr><td>M</td><td>&gt;=2</td><td>Y</td><td>H</td></tr><tr><td>L</td><td>&gt;=2</td><td>N</td><td>L</td></tr><tr><td>L</td><td>&gt;=2</td><td>Y</td><td>M</td></tr></table>

Y=yes, N=no, H=high, M=medium, L=low

Table 1.2 Rules for Estimating Qualitative Risk

<table><tr><td colspan="5">INPUT PARAMETERS</td><td>OUTPUT</td></tr><tr><td>political dimension</td><td>risk</td><td>user needs</td><td>strategic dimension</td><td>philosophical dimension</td><td>Qualitative Rank</td></tr><tr><td>H/M</td><td>L</td><td>--</td><td>M/H</td><td>M/H</td><td>H</td></tr><tr><td>H</td><td>H</td><td>H</td><td>M/L</td><td>M/L</td><td>M</td></tr><tr><td>H/M</td><td>L</td><td>--</td><td>H</td><td>--</td><td>H</td></tr><tr><td>L</td><td>L</td><td>H</td><td>M/H</td><td>M/H</td><td>H</td></tr><tr><td>--</td><td>M</td><td>--</td><td>H</td><td>H</td><td>H</td></tr><tr><td>M</td><td>M/L</td><td>H</td><td>M/L</td><td>M/L</td><td>H</td></tr><tr><td>L</td><td>--</td><td>L/M</td><td>L</td><td>--</td><td>L</td></tr></table>

H=high, M=medium, L=low

As is evident in this table, the rank ordering of projects on each dimension is not the same and these differences must be reconciled in some manner to arrive at a consensus on which projects are critical for final implementation. In our prior discussion, we have shown how these multiple dimensions can be combined, heuristically, to arrive at a single rank on the overall qualitative dimension. These may be altered if the heuristics do not reflect changed corporate objectives. A cursory evaluation shows that certain projects such as “C” rank very high on the qualitative dimensions, but somewhat low on the quantitative dimension. On the other hand, project “G” is ranked high on the quantitative dimension, and low on the qualitative dimension. These types of conflicts have to be reconciled by management by challenging the assumptions made about the way projects were selected in the past. This ranking can be provided independently by the system (first the qualitative and then the quantitative) to allow for an objective assessment.

Table 1.3 Rules for Estimating Quantitative Risk

<table><tr><td colspan="3">INPUT PARAMETERS</td><td>OUTPUT</td></tr><tr><td>project category</td><td>IRR</td><td>payback</td><td>Quantitative Rank</td></tr><tr><td rowspan="3">new development</td><td>&gt;= c_o_c</td><td>&lt;= 3</td><td>H</td></tr><tr><td>&lt;= c_o_c &amp; &gt;= 15</td><td>&lt;= 3</td><td>M</td></tr><tr><td>&lt;= 15</td><td>or &gt;= 3</td><td>L</td></tr><tr><td rowspan="3">enhancement/ maintenance</td><td>&gt;= 15</td><td>&lt;= 5</td><td>H</td></tr><tr><td>&lt; 15</td><td>&lt;= 5</td><td>M</td></tr><tr><td>--</td><td>&gt;= 5</td><td>L</td></tr><tr><td>mandatory</td><td>--</td><td>--</td><td>H</td></tr><tr><td rowspan="3">research and development</td><td>&gt;= 20</td><td>&lt;= 8</td><td>H</td></tr><tr><td>&lt; 20</td><td>&lt;= 8</td><td>M</td></tr><tr><td>--</td><td>&gt; 8</td><td>L</td></tr></table>

c\_o\_c=cost of capital, H=high, M=medium, L=low

Table 1.4 Rules for Estimating Cost of Capital

<table><tr><td>INPUT PARAMETERS</td><td>OUTPUT</td></tr><tr><td>economy</td><td>cost of capital</td></tr><tr><td>stable</td><td>20 %</td></tr><tr><td>inflationary</td><td>25 %</td></tr><tr><td>deflationary</td><td>15 %</td></tr></table>

Table 1.5 Prespecified Budget Allocations

<table><tr><td>INPUT PARAMETERS</td><td>OUTPUT</td></tr><tr><td>project type</td><td>budget</td></tr><tr><td>research and development</td><td>&lt;= 5 %</td></tr><tr><td>high risk</td><td>&lt;= 10 %</td></tr></table>

Table 2 Characteristics of Projects Used for Consultation

<table><tr><td>Project</td><td>payback</td><td>IRR</td><td>new technology</td><td>complexity</td><td>development time</td><td>conflicting impact</td><td>project category</td><td>project description</td></tr><tr><td>A</td><td>3</td><td>22.1</td><td>N</td><td>M</td><td>2</td><td>N</td><td>new</td><td>order entry</td></tr><tr><td>B</td><td>2</td><td>9.5</td><td>N</td><td>L</td><td>1</td><td>N</td><td>maintenance</td><td>purchasing</td></tr><tr><td>C</td><td>4</td><td>10.7</td><td>N</td><td>L</td><td>1</td><td>N</td><td>new</td><td>invoicing</td></tr><tr><td>D</td><td>5</td><td>21.1</td><td>Y</td><td>H</td><td>3</td><td>N</td><td>research and development</td><td>sales forecasting</td></tr><tr><td>E</td><td>4</td><td>15.2</td><td>N</td><td>M</td><td>1</td><td>N</td><td>new</td><td>accounts receivable</td></tr><tr><td>F</td><td>4</td><td>16.6</td><td>Y</td><td>H</td><td>3</td><td>Y</td><td>new</td><td>production planning &amp; scheduling</td></tr><tr><td>G</td><td>1</td><td>25.0</td><td>N</td><td>L</td><td>1</td><td>N</td><td>maintenance</td><td>payroll</td></tr><tr><td>H</td><td>3</td><td>7.7</td><td>N</td><td>M</td><td>1</td><td>N</td><td>mandatory</td><td>personnel</td></tr><tr><td>I</td><td>2</td><td>20.8</td><td>N</td><td>M</td><td>3</td><td>N</td><td>new</td><td>general ledger</td></tr><tr><td>J</td><td>4</td><td>7.0</td><td>Y</td><td>H</td><td>3</td><td>Y</td><td>new</td><td>asset planning</td></tr></table>

Y=yes, N=no, H=high, M=medium, L=low

Table 3 Projects Ordered on Various Dimensions (Descending)

<table><tr><td rowspan="2">IRR</td><td colspan="5">Qualitative Dimensions *</td></tr><tr><td>strategic dimension</td><td>philosophical dimension</td><td>political dimension</td><td>user needs</td><td>risk</td></tr><tr><td>G</td><td>C</td><td></td><td>C</td><td></td><td>B</td></tr><tr><td>A</td><td>D</td><td>F</td><td></td><td>H</td><td>C</td></tr><tr><td>D</td><td>F</td><td>B</td><td>I</td><td>J</td><td>E</td></tr><tr><td>I</td><td>I</td><td>I</td><td>J</td><td>J</td><td>G</td></tr><tr><td>F</td><td>B</td><td>A</td><td>A</td><td>B</td><td>H</td></tr><tr><td>E</td><td>E</td><td>D</td><td>B</td><td>C</td><td>A</td></tr><tr><td>C</td><td>G</td><td>E</td><td>F</td><td>D</td><td>I</td></tr><tr><td>B</td><td>H</td><td>G</td><td>G</td><td>E</td><td>D</td></tr><tr><td>H</td><td>A</td><td>H</td><td>H</td><td>I</td><td>J</td></tr><tr><td>J</td><td>J</td><td>J</td><td>D</td><td>F</td><td>J</td></tr><tr><td></td><td></td><td></td><td>E</td><td></td><td>F</td></tr></table>

• bracketed items have equal ranks on particular dimension

## 3.2. Provide the Combined Rank based on Corporate Knowledge

At this time, corporate knowledge on the way qualitative ranks are to be combined can be input, or accessed from the existing knowledge base so that a single rank ordering of these projects is developed. Again, the case here uses the heuristics described in Tables 1.1 through 1.5 to generate such a combined rank and the system displays these ranks for management evaluation. Note that all these heuristics can be altered over time by management if such changes are considered appropriate. In Table 4, the combined rank is presented in two stages: combined rank using multiple qualitative dimensions, and combined overall rank using both the net qualitative rank and the quantitative rank.

Again, heuristics were used to combine the net qualitative rank with the net quantitative rank. The use of multi-attribute models is an alternate way to address the derivation of the combined rank; we discuss one such model next. However, steering committees, who are often given this responsibility, can simply use brainstorming sessions to poll individuals on the relative merit of each system, and force them to make trade-offs that are necessary between IRR and a project's importance on many intangible, qualitative dimensions. It is possible that these discussions may result in a reassessment of the project's characteristics, especially if the initial assessment of a project's relationship to various qualitative dimensions was established by the sponsoring user group. This type of procedure does allow for a preliminary identification of those projects that agree on both dimensions, thereby allowing the group to focus on those that exhibit a significant amount of disparity, such as projects "G" and "C".

## 3.3. Use of MADM Models for Generating Net Qualitative Rank

It is possible to translate the rank ordering on qualitative dimensions to a numerical scale and apply MADM models to generate a net numerical weight for each project. While many such models exist, one should be aware of the assumptions that are made in combining these weights before interpreting the cumulative weight associated with each project. The use of one such model (linear difference model) is shown in Table 5. The model is written and executed using a spreadsheet environment. The model assigns a weight of 3, 2, and 1 to qualitative and quantitative ranks of each project. (3 for “high,” 2 for “moderate,” and 1 for “low”) and uses the following algorithm to establish the preference structure among projects.

First, assign weights to qualrank and quanrank so that they sum to one (e.g., quanrank is 0.4 and qualrank is 0.6). Take each pair of projects and compute the weighted difference on both dimensions. For example, if the projects are as follows: Project “A”: qualrank = 3, quanrank = 2; Project “B”: qualrank = 2, quanrank = 1, then the preference structure between “A” and “B” is: $0.6(3-2) + 0.4(2-1) = 1.0$ . Since this number is positive, “A” is preferred to “B”. Similar pairwise comparisons are made to obtain the relative preference structure between projects; the results are summarized in Table 5.

This matrix of relative preference values is used to extract a consistent rank ordering. The rank ordering is as follows: (I,H), A, (C,F), B, (G,D), J,E. Projects in parentheses are of equal relative rank. This is not completely inconsistent with the result obtained using the heuristics, even though the relative preference among projects C,B,F,G,D is not brought to the surface when heuristics are used. Obviously, more complicated modeling procedures can be used to establish the relative ranking of these projects. For example, one can assign different utilities to each possible value of qualrank and quanrank (e.g., $u(3)=0.8$ , $u(2)=0.4$ , $u(1)=0.1$ ).

Table 4 Projects Ordered on Qualitative, Quantitative, and Net Ranks

<table><tr><td>Qualitative Ranks*</td><td>Quantitative Ranks*</td><td>Net (Overall) Rank*</td></tr><tr><td>A H C I F J B G D E</td><td>I H D G B A F E C J</td><td>H I A C B F G D J E</td></tr></table>

\* bracketed items have equal ranks on particular dimension

Table 5 Application of the MADM Model

<table><tr><td>Projects</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td></tr><tr><td>A</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B</td><td>0.6</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>C</td><td>0.4</td><td>-0.2</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>D</td><td>0.8</td><td>0.2</td><td>0.4</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>E</td><td>1.6</td><td>1.0</td><td>1.2</td><td>0.8</td><td>0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>F</td><td>0.4</td><td>-0.2</td><td>0</td><td>-0.4</td><td>-1.2</td><td>0</td><td></td><td></td><td></td><td></td></tr><tr><td>G</td><td>0.8</td><td>0.2</td><td>0.4</td><td>0</td><td>-0.8</td><td>0.4</td><td>0</td><td></td><td></td><td></td></tr><tr><td>H</td><td>-0.4</td><td>-1.0</td><td>-0.8</td><td>-1.2</td><td>-2.0</td><td>-0.8</td><td>-1.2</td><td>0</td><td></td><td></td></tr><tr><td>I</td><td>-0.4</td><td>-1.0</td><td>-0.8</td><td>-1.2</td><td>-2.0</td><td>-0.8</td><td>-1.2</td><td>0</td><td>0</td><td></td></tr><tr><td>J</td><td>1.0</td><td>0.4</td><td>0.6</td><td>0.2</td><td>-0.6</td><td>0.6</td><td>0.2</td><td>1.4</td><td>1.4</td><td>0</td></tr></table>

## 3.4. Sensitivity Analysis

The committee, if it chooses to alter the ranks of the projects on each dimension, may do so by allowing the characteristics of each project on each dimension to be presented independently and making decisions on their appropriateness. This step can take place before step 2 (for initial rank ordering) or after step 3 (for sensitivity analysis), thus allowing management to challenge the assumptions made in arriving at these rank orderings. One such analysis is shown in Table 6 when the organization decided to alter the characteristics of two projects, "G" and "H". It was determined that "G" was assigned a low user need and "H" was assigned a high user need. However, upon discussion, it was established that this assumption should be reversed (as payroll frequently affects many more employees, while the personnel system affects user needs only in the human resources division on a selective basis). This change in assumptions suddenly alters both the qualitative and quantitative ranks of the projects and, hence, the net rank.

Such sensitivity analysis can play an extremely useful role, especially in situations where user groups responsible for providing input on project characteristics have a different understanding of the semantics of the criteria used for evaluation, thus causing them to answer questions on a project's relationship to these criteria differently.

## 3.5. Ex-Post Analysis of Project Rankings

If projects are rank ordered differently, possibly by not using the system, then the committee can determine how these ranks compare with what the system may have recommended and why. This type of analysis is useful to determine if any corporate philosophies or policies are violated by the rank ordering and to challenge these, if required. Such a feature also allows the organization to ensure that there is some kind of longitudinal consistency in the way projects are funded or resource allocated across multiple units in the organization and over time. Some specific, nonsystem-dependent rankings of projects and the assumptions this rank ordering violates are presented in figure 3.

In this case, the rationale underlying project G's low qualitative rank is its “less than ideal” relationship to the political and philosophical dimensions, and its minimal impact on multiple user needs. It is only through such explicit reasoning that management can arrive at a consistent set of policies that take into consideration factors that are often intractable, and to validate them over time for their continued applicability.

## 3.6. Incremental Cash Flow Analysis

In some cases, a decision on a final portfolio based on project ranks may then be used to examine how their implementation affects the organization's funds flow. Since the projects take a certain amount of time, deciding which of these should be undertaken first may impact the level of funds required and level of funds currently available. Some of these decisions on implementation may be made based on their logical dependency, while others may be based on their impact on cash flows or risks. This type of analysis can be very useful in management decision making even if all of the chosen projects will be implemented eventually. Table 7 provides the net cash flows associated with each project under consideration.

Assume in this case that management has chosen to select the top three systems (A, H, and I). Then the investment plan results in the net funds flow shown in Table 8. Further assuming that all the chosen projects cannot be undertaken immediately, a strategy for implementing them can be formulated based on overall initial investment and the riskiness of each individual project. In Table 8, project A is a bit more risky than H and I. Hence, one can choose to build H first, then I, and then A. In which case, the funds flow situation will be different (assuming there is no dependency between these systems, and they start at different time periods). The change in funds flow is shown in Table 9. This type of staggering can also vary the net quantitative rank of these projects as the timing of the benefit stream may change, as is the case here.

Table 6 Effect on Ranks of Altering Assumptions

<table><tr><td></td><td>Net Qualitative</td><td>Net Quantitative</td><td>Net Overall</td></tr><tr><td colspan="4">Before</td></tr><tr><td>G</td><td>Low</td><td>High</td><td>3</td></tr><tr><td>H</td><td>High</td><td>High</td><td>5</td></tr><tr><td colspan="4">After</td></tr><tr><td>G</td><td>High</td><td>High</td><td>5</td></tr><tr><td>H</td><td>Low</td><td>High</td><td>3</td></tr><tr><td colspan="4">Management examined the quantitative rank ordering and wondered why some projects were not ranked higher on other dimensions as well. For example, Project G ranks extremely high on IRR, and the question raised is “why is G ranked low on qualitative dimensions?”</td></tr><tr><td rowspan="2">Rule 101</td><td>IF</td><td colspan="2">LOW risk;MODERATE on political dimension;LOW on meeting user needs;MODERATE on strategic dimension;LOW on philosophical dimension;</td></tr><tr><td>THEN</td><td colspan="2">LOW on net Qualitative dimension.</td></tr></table>

Figure 3. Assumptions Underlying Rank Ordering

Table 7 Cash Flows Associated with All Projects

<table><tr><td>Project</td><td>Year 0</td><td>Year 1</td><td>Year 2</td><td>Year 3</td><td>Year 4</td><td>Year 5</td></tr><tr><td>A</td><td>-10000</td><td>3500</td><td>3500</td><td>3500</td><td>3500</td><td>3500</td></tr><tr><td>B</td><td>-5000</td><td>3100</td><td>2600</td><td></td><td></td><td></td></tr><tr><td>C</td><td></td><td>-5000</td><td>1600</td><td>1600</td><td>1600</td><td>1600</td></tr><tr><td>D</td><td>-10000</td><td>0</td><td>0</td><td>0</td><td>0</td><td>26000</td></tr><tr><td>E</td><td>-2000</td><td>600</td><td>600</td><td>600</td><td>600</td><td>600</td></tr><tr><td>F</td><td></td><td>-5000</td><td></td><td></td><td>4500</td><td>4000</td></tr><tr><td>G</td><td>-10000</td><td>12500</td><td></td><td></td><td></td><td></td></tr><tr><td>H</td><td></td><td></td><td>-10000</td><td>3600</td><td>4000</td><td>4000</td></tr><tr><td>I</td><td></td><td>-8000</td><td>4500</td><td>3500</td><td>3300</td><td></td></tr><tr><td>J</td><td>-3000</td><td></td><td>1000</td><td>1200</td><td>1500</td><td></td></tr></table>

Further, if there are budgetary constraints on bringing these projects on board, then these can be formally introduced into the model so that only those project sequences that are amenable for implementation are extracted. For example, if there is a limit of \$5,000 in the current year for project implementation, then one can look at potentially initiating C, B, or F whose initial outlay is only about \$5,000, and they are next in line in terms of the overall rank. Such trade-offs based on budgetary considerations, while not always advisable due to the long-term nature of MIS projects, may sometimes be necessary to allow flexibility in the planning process.

## 4. Limitations and Extensions

DECISION-MAKING PROCESSES THAT REQUIRE a synthesis of both qualitative and quantitative factors often cannot be supported effectively using a single technology due to its limiting information processing characteristics. For example, many technologies that can effectively process numerical data are inadequate for processing subjective or qualitative data. Since many unstructured and semistructured decisions use information that is both quantitative and qualitative, there is a definite need to examine disparate technologies that can manage different information sets effectively, and yet be integrated to support the total decision. Such technology integration, however, cannot be undertaken without an understanding of the decision process characteristics that these technologies are intending to support. In this paper, the resource allocation decision (an unstructured decision) within the MIS planning activity was analyzed using knowledge acquisition techniques, and different technologies such as decision support, database, and knowledge-based were utilized appropriately to manipulate data, and integrated to support the entire decision process. The use of such an integrated, knowledge-based system was illustrated with the aid of an example.

The value to an organization of a system such as the one presented here is ultimately dependent on the specific manner in which it is utilized by a planning group. Clearly there is a potential for political maneuvering here in that individuals may manipulate data to reinforce their positions or predilections. While the system does provide facilities for assumption testing where committee members may challenge the data presented by a project proposer, the responsibility for controlling such manipulation rests with the entire group involved in project selection. Also, IS planning involves a far wider range of activities than those supported by the system. The emphasis of the system is on the narrow problem of project ranking; it does not address related and equally relevant issues such as communicating IT opportunities to top management, educating users and general management about IT, keeping pace with rapid technological developments, and so on.

The approach we have described is related to research focused on providing decision support to small groups. In supporting group decision making, the first and second levels of support have been identified as communication and model integration, while the third level of support is for the system to set the group's agenda and to direct group activity proactively [7]. Our system addresses the communication issue by providing common access to the project database and project rankings and the model integration issue by linking quantitative models with heuristics that represent the qualitative judgments of the steering committee. However, while supporting the various stages in the decision-making process, the system does not dictate the agenda or coordinate the stages in an a priori defined manner. Three research questions related to this final limitation are currently under investigation.

Table 8 Funds Flow Associated with Investment Plan

<table><tr><td>Project</td><td>Year 0</td><td>Year 1</td><td>Year 2</td><td>Year 3</td><td>Year 4</td><td>Year 5</td></tr><tr><td>A</td><td>-10000</td><td>3500</td><td>3500</td><td>3500</td><td>3500</td><td>3500</td></tr><tr><td>H</td><td></td><td></td><td>-10000</td><td>3600</td><td>4000</td><td>4000</td></tr><tr><td>I</td><td></td><td>-8000</td><td>4500</td><td>3500</td><td>3300</td><td></td></tr><tr><td></td><td>-10000</td><td>-4500</td><td>-2000</td><td>10600</td><td>10800</td><td>7500</td></tr></table>

Table 9 Effect of Altering Investment Plan on Cash Flow

<table><tr><td>Project</td><td>Year 0</td><td>Year 1</td><td>Year 2</td><td>Year 3</td><td>Year 4</td><td>Year 5</td><td>Year 6</td><td>Year 7</td></tr><tr><td>A</td><td></td><td></td><td>-10000</td><td>3500</td><td>3500</td><td>3500</td><td>3500</td><td>3500</td></tr><tr><td>H</td><td>-10000</td><td>3600</td><td>4000</td><td>4000</td><td></td><td></td><td></td><td></td></tr><tr><td>I</td><td></td><td>-8000</td><td>4500</td><td>3500</td><td>3300</td><td></td><td></td><td></td></tr><tr><td></td><td>-10000</td><td>-4400</td><td>-1500</td><td>11000</td><td>6800</td><td>3500</td><td>3500</td><td>3500</td></tr></table>

First, if it were desired to involve the system more actively in the resource allocation decision, what types of tasks might be assigned to it and what would its effect on the decision group be—that is, at what point would the system become a hindrance to group deliberations rather than help the decision-making process? Second, in what manner does the decision group deal with multiple dimensions when presented individually as opposed to providing a single rank that is derived with the help of heuristics or some type of multi-attribute decision-making model which, in essence, captures the utility of the group? Finally, how significant is the bias toward the concrete versus abstract data that are presented about the projects? While there is some evidence for such a bias, it would be useful to determine its significance empirically with the aid of such a system.

## REFERENCES

1. Agarwal, R., and Tanniru, M. Knowledge acquisition using structured interviewing: an empirical investigation. Journal of Management Information Systems, 7, 1 (Summer 1990), 123–140.

2. Agarwal, R., and Tanniru, M. Knowledge extraction using content analysis. Knowledge Acquisition, 3 (1991), 421–441.

3. Agarwal R.; Roberge, L.; and Tanniru, M. Qualitative factors in MIS planning: a multi-dimensional methodology for systems prioritization. Working Paper, Syracuse University, School of Management, 1991.

4. Cash, J.I.; McFarlan, F.W.; and McKenney, J.L. Information Systems Management: The Issues Facing Senior Executives. Homewood, IL: Irwin, 1988.

5. Davis G.B., and Wetherbe, J.C. Developing a long-range information architecture. Proceedings of the National Computer Conference, Anaheim, CA, May 1983.

6. Davis G.B., and Olson, M. Management Information Systems, 2d ed. New York: McGraw-Hill, 1985.

7. DeSanctis, G., and Gallupe, B.R. A foundation for the study of group decision support systems. Management Science, 33, 5 (1987), 589–609.

8. Drury, D.H. A survey of data processing steering committees. Information and Management, 9 (1985), 1–7.

9. Edwards, W., and Newman, J.R. Multi-Attribute Evaluation. Newbury Park, CA: Sage, 1982.

10. Fazolallahi, B. A framework for MIS planning. Ph.D. dissertation, Syracuse University, 1984.

11. Hogarth, R. Judgment and Choice: The Psychology of Decision. New York: Wiley, 1980.

12. Hong, I.B., and Vogel, D.R. Data and model management in a generalized MCDM-DSS. Decision Sciences, 22, 1 (Winter 1991), 1–25.

13. IBM. Business Information Systems—Information System Planning Guide GE20-0527-3, July 1981, 3d ed.

14. Jain, H.; Tanniru, M.; and Fazlollahi, B. MCDM approach for generating and evaluating alternatives in requirement analysis. Information Systems Research, 2, 3 (September 1991), 223–239.

15. King, W.R. Strategic planning for MIS. MIS Quarterly, 2, 1 (March 1978), 27–37.

16. Klein, G., and Beck, P.O. A decision aid for selecting among information system alternatives. MIS Quarterly, 11, 2 (June 1987), 177–185.

17. Krippendorf, K. Content Analysis: An Introduction to Its Methodology. Beverly Hills, CA: Sage, 1980.

18. Lederer, A.L., and Mendelow, A.L. Issues in information systems planning. Information and Management, 10 (1986), 245–254.

19. McFarlan, F.W. Portfolio approach to information systems. Harvard Business Review (September–October 1981), 142–150.

20. McFarlan, F.W. Information technology changes the way you compete. Harvard Business Review (May–June 1984), 98–103.

21. Porter, M.E., and Miller, V.E. How information gives you competitive advantage. Harvard Business Review (July–August 1985), 149–160.

22. Porter, M.E. Strategy: Techniques for Analyzing Industries and Competitors. New York: Free Press, 1980.

23. Rackoff, N.; Wiseman, C.; and Ulrich, W.A. Information systems for competitive advantage: implementation of a planning process. MIS Quarterly, 9, 4 (December 1985), 285–294.

24. Simon, H.A. The Shape of Automation for Men and Management. New York: Harper and Row, 1965.

25. Slovic, P. From Shakespeare to Simon: speculations—and some evidence—about man's ability to process information. Oregon Research Institute Monograph, 12, 12 (April 1972).

26. Slovic, P.; Fischhoff, B.; and Lichtenstein, S. Response mode, framing, and information-processing effects in risk assessment. In D.E. Bell, H. Raiffa, and A. Tversky, eds., Decision Making. New York: Cambridge University Press, 1988.

27. Van Dyck, E., and Smith, D.G. R&D portfolio selection by using qualitative pairwise comparisons. OMEGA: The International Journal of Management Science, 18, 6 (1990), 583–594.

28. Vitale, M.R. The growing risks of information systems success. MIS Quarterly, 10, 4 (December 1986), 327–334.

29. Zeleny, M. Multiple Criteria Decision Making. New York: McGraw-Hill, 1982.
