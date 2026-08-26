---
otero_id: 17056
otero_key: "BTUVCFBK"
title: "Interaction of task and technology to support large groups"
authors: "Jay Nunamaker; Dong Vogel; Benn Konsynski"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90003-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Interaction of Task and Technology to Support Large Groups

Jay NUNAMAKER, Doug VOGEL

and Benn KONSYNSKI

University of Arizona, Department of MIS, Tucson, AZ 85721, USA

There are multiple, and occasionally conflicting, perspectives regarding what Group Support Systems are, what they should be, and what directions research related to them should take. The purpose of this paper is to focus on the factors involved in Group Support Systems, with particular attention to the ways in which these factors interact. A University of Arizona implementation of automated group decision support is described as an example of an established Group Support System, based upon a philosophy that recognizes the critical importance of environment, hardware and software to the successful operation of the system. Research conducted at University of Arizona facilities has involved experience with many groups brought together to address real problems. This research has resulted in identification of three interacting factors deemed to be essential to a successful Group Support System: user profile, task domain, and technology. Each of these is defined and its relationships with the others are described. Aspects of benefits to larger groups, task dynamics, interaction among group tasks and technology, multiple session benefits, integration of information technology and impacts upon group process also are explored. Multiple-methodological research approaches and opportunities for future research are addressed.

Keywords: Group Support Systems, GDSS, Task, Information Integration, Group Process Impact.

## Introduction

Group Support Systems intended to provide automated support for groups that are addressing complex questions are themselves complex. There are multiple, and occasionally conflicting, perspectives regarding what Group Support Systems are, what they should be, and what directions research should take as these systems mature and potentially become institutionalized in organizations. The term Group Support Systems has been chosen as one that encompasses aspects of group decision support systems (GDSS), decision rooms, decision conferences, computer supported conference rooms, teleconferencing, and electronically supported meetings. None of these other terms captures the extended domain that automated support for groups addresses.

Although examples of Group Support Systems have been reported in the literature (see Kraemer and King, 1988), the field is as yet not well developed, even as a concept. Furthermore, although we are starting to see examples of Group Support Systems in use, little attention has been given to issues of how they can be made operational and be institutionalized within organizations as integral components of existing organizational information systems. It is only in such an environment that they can achieve any long term impact. In addition, they must also provide a sufficient level of individual and group usefulness to justify extended organizational commitment.

Questions related to the complex nature of Group Support Systems can best be addressed by looking at the problem domain from several different, but complementary, perspectives. Maruyama (1987) uses the term multi-ocularity to describe this approach to achieving a complete and more holographic vision of Group Support Systems. As is true of all attempts to solve complex problems, no single research approach is sufficient.

An established Group Support System at the University of Arizona is described with particular

![](/api/attachments/BTUVCFBK/fulltext/images/aea319b25b1444472136664a580a2193303f81af1a2d4ad579b566feb611f189.jpg)

Jay. F. Nunamaker, Jr. is Head of the Department of Management Information Systems and is a Professor of Management Information Systems (MIS) and Computer Science at the University of Arizona. He received a PhD from Case Institute of Technology in systems engineering and operations research. He was an Associate Professor of Computer Science and Industrial Administration at Purdue University. Dr. Nunamaker joined the faculty at the University of Arizona in

1974 to develop the MIS program. He has authored numerous papers on group decision support systems, the automation of software construction, performance evaluation of computer systems, decision support systems for systems analysis and design, and has lectured throughout Europe, Russia, Asia, and South America. Dr. Nunamaker is Chairman of the Association for Computing Machinery (ACM) Curriculum Committee on Information Systems.

![](/api/attachments/BTUVCFBK/fulltext/images/3ddb92c376075610f327eabf27a49d3e59036c9b26060192d16626d99f500ded.jpg)

Douglas R. Vogel is an Assistant Professor of MIS. He has been involved with computers and computer systems in various capacities for over 20 years. He received his M.S. in Computer Science from U.C.L.A. in 1972 and his Ph.D. in MIS from the University of Minnesota in 1986 where he was also research coordinator for the MIS Research Center. His current research interests bridge the business and academic communities in addressing questions of the impact of management information systems on aspects of interpersonal communication, group decision making, and organizational productivity.

![](/api/attachments/BTUVCFBK/fulltext/images/b87d2d5c24baa9d998c5bcca73c5afea9aaf2242e2f91bfbd5187503bddbd59c.jpg)

Benn R. Konsynski is a visiting Professor at the University of Arizona, visiting the Harvard Business School on a multi-year appointment. Professor Konsynski completed his Ph.D. in Computer Science at Purdue University. His minor fields included Russian and Industrial Engineering. He has taught at the University of Arizona in the Management Information Systems Department in the College of Business and Public Administration. He has taught in the MBA program at

the Harvard Business School in the first year course on Management Information Systems and in the second year program on Knowledge Based Systems. His research interests include electronic data interchange and IOS (inter-organizational systems), knowledge-based systems, model management in decision making, CASE (Computer-Aided Software Engineering), data communications and distributed processing and group decision support systems. He has published in Communications of the ACM, Harvard Business Review, IEEE Transactions on Communications, MIS Quarterly, Journal of MIS, Data Communications, Decision Sciences, Decision Support Systems, Information Systems, and IEEE Transactions on Software Engineering. His research grants have involved work with National Science Foundation, Army Communications Command, Electrical Power Research Institute, U.S. Navy, International Business Machines, NCR and Digital Equipment Corporation. He worked with AT&T Marketing and Bell Labs on product market positioning.

attention to the ways in which user profile, task domain and technology interact. These key issues in making Group Support Systems operational are identified, based on accumulated experience in our laboratory settings. Aspects of larger group benefits, task dynamics, interaction of group tasks and technology, multiple session benefits, integration of information technology, and group process impact are discussed as are multi-methodological research findings and opportunities in each of these areas.

## Literature

The literature reviewed in this section is presented from five different perspectives on Group Support Systems that we have designated as systems-based, organizational, human communication, decision making, and management science (see fig. 1). Considering any single perspective presents an incomplete picture and, while these perspectives are neither exhaustive nor mutually exclusive, they collectively represent foundational components from which Group Support System research can progress soundly.

## Systems-Based

System concepts provide a useful framework for describing Group Support Systems, i.e., a set of elements operating together to accomplish an objective. These systems, by nature, are probabilistic rather than deterministic i.e., there is always some degree of unpredictability associated with the interaction between human and machine components. Group Support Systems are also open (as opposed to closed) in terms of environment interaction and the capability to be adapted to meet changing circumstances, as when it is seen that adjustments are needed or when equifinality occurs among groups addressing complex questions with varying degrees of efficiency and effectiveness.

Group Support Systems  
![](/api/attachments/BTUVCFBK/fulltext/images/cc39150f7d020b2251367a3e8cf717a0e14a6dc6a458197da0e32ee9179f05dc.jpg)

The literature on systems theory is varied and rich. Ackoff (1971) has even suggested a “system of system concepts.” Huber (1984a) has used systems theory as a basis for determining the nature of post-industrial society and the increased demands that this environment would impose on post-industrial organizations. We will restrict ourselves here to those aspects of the systems literature that specifically provide a framework for information systems. Toward that end, the work of Peter Checkland (1981) is particularly appropriate to Group Support Systems. Checkland’s Soft Systems Methodology (SSM) recognizes the ambiguities inherent in dealing with human interface issues while preserving the concepts of decomposition, coupling and cohesion that are essential to the development and evaluation of Group Support Systems, in which adaptation and evolution are ways of life.

An example of the application of systems thinking to Group Support Systems is illustrated by the development of automated support for stakeholder identification and assumption surfacing [Applegate (1986)]. This research was based on the work of Mason and Mitroff (1981) that focused on dialectical inquiry and impact analysis in conjunction with assumption surfacing and testing. Their work, in turn, reflected some of Churchman's considerations for the meaning of a system [Churchman (1968)]. A systems focus is exemplified in research on semantic inheritance networks, frames, and production rules [Kotteman and Konsynski (1984), McIntyre, Konsynski, and Nunamaker (1987)].

## Organizational

An organizational perspective of Group Support Systems includes the aspects of organizational theory, organizational development, and organizational behavior that are particularly relevant to supporting groups in organizational contexts. Issues of work groups and their tasks are especially important. Pava (1983) noted that members of knowledge-work groups often tend to form into discretionary coalitions around a task and that such coalitions are particularly fluid, with employees tending to join many coalitions that relate to specific production group environments. In one sense, Group Support Systems act as an “organizational memory” that retains a measure of continuity from session to session. The relationship between social and technical variables has been recognized as particularly important, dating back to the Tavistock studies (e.g., Trist and Banforth (1951) and, more recently, the work of Galbraith (1977)).

Of particular interest is research reported in the organizational behavior literature which focuses on group functioning and methods for improving group performance. Following a review of such research, Shaw (1981) concluded that groups produce more and better solutions to problems than do individuals, particularly on judgmental tasks, although differences in overall time required for solution are not consistently better for either individuals or groups. Issues of open discussion within groups, member attitudes, risk propensity, and “group think” [Janis (1972)] have been addressed. A number of suggestions for structuring group processes to accentuate group gains, or at least to minimize the probability of group losses, have been made. Among these are Brainstorming [Osborn (1957), Delphi (the Rand Corp), Nominal Group Technique (NGT), Van de Ven and Delbecq (1971)], and Social Judgement Analysis [Rohrbaugh (1981)].

Group Support Systems historically have provided automated support for group processes by using keyboards, computer screens, and electronic communications to replace pencils, paper, and manual passing of sheets of ideas. This remains essentially a manual approach that is analogous to early development of the automotive industry when engines were put into carriage frames, giving us “horseless carriages.” Today’s automobiles and transportation network have come a long way from the “horseless carriage” period. It remains to be seen what changes will take place in Group Support Systems as the relationship between groups and technology becomes better understood. The ultimate challenge is to integrate the best that both people and machines have to offer.

## Human Communication

A significant amount of recent research has taken a human communications perspective, focusing on the nature of the interpersonal and group communication support individuals in a group need in order to utilize automated group systems successfully. Research tasks typically have focused on qualitative text-oriented aspects that require group member judgment and interpersonal communication to arrive at a conclusion; little, if any, attention has been paid to providing participant input to resident decision models. The goal has been to provide automated support in a decision room environment [Gray, (1981)] that seeks to minimize group process and/or maximize group process gains [Huber (1982), Kraemer and King (1988)].

Examples of research results from these Group Support Systems include those reported by Lewis (1982), who concluded that GDSS support was superior both to no support and to structured paper-and-pencil support in terms of producing higher quality decisions, generating more alternatives, and reducing domination by single group members. Gallupe (1985) found that GDSS supported groups produced higher quality decisions, particularly in high-difficulty tasks. Turoff and Hiltz (1982), using a task that required a group to rank a set of alternatives, found that either a human leadership condition or a GDSS support condition resulted in a greater ability for the group to reach consensus, but, used in combination, leadership and GDSS canceled one another out. Watson (1987) has examined the impact of group size (3 or 4) and GDSS structure (none, manual structure, automated structured support) on aspects of decision maker confidence, member dominance, and satisfaction with a resource allocation task.

Overall, GDSS installations and associated research typically focus attention on aspects of the group process and interpersonal communication rather than on the possible impact of data external to the immediate group or management science models that might assist the group in the evaluation of alternative approaches to completing its task. Organizational implications and issues are rarely addressed, but there has been fairly broad emphasis on various aspects of generating, choosing, and negotiating [McGrath (1984)]. The end result is a focus on appreciation of group dynamics that provides a foundation for research that emphasizes the use of information collected in group sessions.

## Decision Making

Huber and McDaniel (1986) have suggested a “decision-making paradigm of organizational design,” arguing that “the nature of current and future organizational environments requires use of a design paradigm that responds to the increasing frequency and criticality of the decision-making process.” Decision making includes the sensing, exploration, and definition of problems or opportunities as well as the generation, evaluation, and selection of solutions. Numerous models of the decision making process in organizational contexts have been developed [e.g., Simon (1960), Cyert and March (1963), Pounds (1969)]. Although rational models have been most often the focus of Group Support Systems, political/competitive, “garbage can” [Cohen (1971)], and program models also exist.

Behavioral models of decision makers have been developed, too. In the classical economic model of the decision maker, rational behavior with complete information is presumed. In the administrative model [Simon (1960)] the decision maker is assumed not to be completely rational but rather to display bounded rationality in complex and only partially known environments. Achieving satisfaction is paramount. Group Support Systems simultaneously have an opportunity and a responsibility in these situations. On the one hand, a Group Support System provides the opportunity to bring a number of decision makers together to share information and perhaps cumulatively attain a more robust appreciation of the problem domain and possible solutions. On the other hand, a Group Support System must support individuals within the group and the group itself with appropriate data and flexibility to facilitate decision makers' exploration of alternatives, using their own heuristics.

An additional aspect of decision making that simultaneously presents an opportunity and a problem in Group Support Systems involves humans as information processors. Group Support Systems exhibit promise in terms of supplementing human limits on short term memory [Miller (1956), Newell and Simon (1972)] and handling probabilistic data [Wright (1980)]. In effect, in addition to assisting humans in managing the problem space and combating information overload, Group Support Systems also provide feedback. However, some individual differences and inherent biases possessed by human beings as information processors [Davis and Olson (1985)] make it more complicated to provide effective automated support, especially in terms of decision maker confidence and satisfaction with Group Support System capabilities.

## Management Science

A branch of contemporary Group Support Systems research that has its foundations in management science seems particularly concerned with group problems that typically involve assignment of quantitative values from group members as collective inputs to models which then help in arriving at a solution. Tasks tend to be of the “choosing” type [McGrath (1984)] as opposed to idea generation. Examples of GDSS of this type include multi-attribute value analysis [e.g., Atrium and Lax (1987)] or calculation of preferences [Shakum (1987)], both based on input collected in a group context. Other research [e.g., Bui et al. (1987)] has examined the impact of the physical distribution of group members on ability to provide effective model input. Optimization techniques, payoff matrices, utility curves, decision trees, ranking, weighting, game theory, and statistical inference are but a few of the methods available for deciding among alternatives.

Multi-criteria decision-making models are particularly relevant to Group Support Systems. Group members typically confront a broad spectrum of factors that are important considerations in arriving at a final decision. Choices may be either compensatory or noncompensatory [Minch and Sanders (1986)], reflecting the level of cognitive processing demanded by the decision maker. Additive and additive-difference models illustrate compensatory choice strategies [Wright and Barbour (1977)] where all information available to the decision maker is used and the search is exhaustive. Conjunctive, disjunctive, lexicographic ordering, and elimination-by-aspects models illustrate noncompensatory choice strategies where heuristics for selecting alternatives are used without having to process completely all of the dimensional information available to the decision-maker [Tversky (1972)].

Interestingly, relatively little attention seems to have been paid to the nature of the user interface between people and machines that makes it possible for individuals in a group to interact as they contribute, share, and deliberate. Interfaces employed in typical management science models have a single workstation through which the group's input is in some way recorded, rather than multiple workstations (one for each individual in the group). Multiple stations serve a number of communication oriented functions, including the capture of individual inputs which are consolidated and incorporated into a collective set of model inputs whereas the single workstation configuration eliminates many opportunities to let the group of users actively share in selecting and weighting the importance of model assumptions to reflect a particular organizational context.

## University of Arizona Implementation

At the University of Arizona, we have created two environments in which groups can interact to perform a variety of tasks using group support technology. Our first facility has been operational since March 1985. The second, completed in November 1987, reflects what we learned from the first. Hardware has evolved from terminals to early PC/LAN technology to token-ring based IBM Personal System 2s with extended audio/visual integration. Software has evolved from isolated stand-alone support to sophisticated network-based integrated support that benefits from user feedback and systematic empirical evaluation. University of Arizona software created for use in these laboratories is now installed in six academic institutions and one major multi-national company. Hundreds of group sessions on a variety of topics have been conducted by groups representing a wide spectrum of member characteristics. Particular emphasis has been placed on providing planning and decision-making support for business and community groups assembled to address complex organizational problems of their own choosing. Group size has varied from 4 to 48 participants. Facilitation has evolved from provision of technical support for hardware to meeting coordination that includes professionally skilled attention to group dynamics. Participants interact with a variety of automated tools to support individual and group planning, deliberation, and problem-solving. For example:

A Session Manager tool guides the facilitator or group leader in selection of the tools to be used in a session and generates an agenda. Default times and output reports are listed and may be modified at the group's discretion.

An Electronic Brainstorming tool supports idea generation, allowing group members to share comments on a specific question simultaneously and anonymously.

An Issue Analyzer tool helps group members identify and consolidate key focus items resulting from idea generation. Support is also provided for integrating external information to support identified focus items.

A Voting tool provides a variety of prioritizing methods including Likert scales, rank ordering, and multiple choice. All group members cast private ballots. Accumulated results are displayed.

A Topic Commenter tool supports idea solicitation and provision of additional details in conjunction with a list of topics. Each topic may have sub-topics. Participants enter, exchange, and review information on self-selected topics.

A Policy Formation tool supports the group in developing a policy statement or mission through iteration and group consensus.

An Organizational Infrastructure tool provides support for capturing characteristics of organizational data sets, information systems, and structure to provide a foundation for impact analysis.

A Stakeholder Identification and Assumption Surfacing tool is used to systematically evaluate the implications of a proposed policy or plan. Stakeholders' assumptions are identified, scaled, and graphically analyzed.

An Alternative Evaluator tool provides multi-criteria decision making support. A set of alternatives can be examined under flexibly weighted criteria to evaluate decision scenarios and trade-offs.

Plexsys Group Support System  
![](/api/attachments/BTUVCFBK/fulltext/images/c1d8193d5eb5af5c09428c90e8743e6a18599155d0d34dd0e33a8140e2957cfb.jpg)  
Fig. 2.

The organization of the tools to support group processes and tasks is made possible by the system architecture illustrated in fig. 2. The tools are selected and arranged to meet the specific needs of a particular user group in performing the task at hand. As shown in fig. 2, the output from the tools serves as input to a knowledge base that provides a mechanism for representing and storing the planning knowledge. A variety of knowledge representation techniques are employed including semantic inheritance networks, frames, and production rules [Kottemann and Konsynski (1983), McIntyre, Konsynski, and Nunamaker (1987)]. The knowledge base approach facilitates multiple planning and decision process representations. The representations can change dynamically as new knowledge is added to the system, while the knowledge base acts as an “organization memory” when groups return for additional sessions and new members or groups seek to build upon the output from previous sessions.

## University of Arizona Philosophy

Group Decision Support research at the University of Arizona is philosophically grounded in a belief that, because the study of Group Support Systems is so complex, it requires both the recognition of multiple factors and an appreciation of the importance of factor interaction. Our philoso-

# Group Support System Dimensions

User Profile Task Domain

Technology

Fig. 3.

phy is based upon what we have learned in working with more than 90 public and private organizations at two facilities where groups having as few as 4 or as many as 48 members receive electronic support as they meet to address complex problems.

Fig. 3 illustrates three factors that, within the external environment of an organization, typify Group Support Systems. These factors are user profile, task domain, and technology and each of them can, in turn, be decomposed to provide variables that more precisely describe an individual Group Support System. The intersections of the three factors represent different aspects of the human-machine interface.

The user profile dimension of a Group Support System addresses variables such as group size, composition, history, member proximity, and differences that characterize group members who address issues concurrently or distributed in time. Additional characteristics of individuals such as leadership behavior, communication apprehension, and individual decision styles should also be included, as should the nature of interpersonal communication between group members. Overall, this dimension must deal with the individual, interpersonal, and group dynamics represented by the human beings using a Group Support System.

The task domain includes the task on which the users are focusing and is influenced by the organizational context and culture within which they operate. Based on a review of the literature, McGrath (1984) has grouped tasks into four categories: generating, choosing, negotiating, and executing. He further subdivides generating into generating ideas and generating plans, choosing into solving problems with correct answers and deciding issues with no right answers, negotiating into resolving conflicts of viewpoint and resolving conflicts of interest, and executing into resolving conflicts of power and executing performance tasks. Most Group Support Systems provide automated support for generating, choosing, and negotiating tasks. “Executing” usually is supported only to a minor extent and then only if executing is loosely interpreted to encompass execution of cognitive as well as physical tasks.

Technology, the final dimension to be considered in Group Support Systems, focuses on the degree to which technology is actively employed in the group process, ranging from passive to active as it provides communication support, process structure, integration, and guidance. Communication support is passive, since its function is simply to provide channels of communication between group members. Process structure support is slightly more active, providing some structure to the group process in conjunction with particular tasks. At the next level of technology involvement, integration facilitates exchange of knowledge base information between various sub-phases of tasks and tools and recognition of exceptions. Guidance constitutes active involvement of the Group Support System in the decision process by means of artificial intelligence techniques.

Basic to the University of Arizona philosophy is recognition of the interactions among user profile, task, and technology. As illustrated in fig. 3, each primary factor influences (and is influenced by) additional considerations whenever it overlaps with other factors. The intersections of the three factors represent aspects of the human-machine interface. Technology and user profile interact because user characteristics, including comfort and familiarity with technology, must be considered in the design of an interface that will provide effective support. The technology and task dimensions interact because appropriate technological support must be a function of the task domain. User profile and task interact because individual and cumulative user knowledge of the task at hand will vary greatly. In combination, the three factors require that, to be effectively operational, a Group Support System must have a human-machine interface that provides appropriate technological support for the task at hand and is responsive to the user profile.

Specifically, our Group Support Systems research at the University of Arizona suggests that:

The needs of larger groups (i.e. eight or more persons) are an important concern. Working only with small groups (e.g., three of four persons) does not sufficiently explore system capabilities and implications.

Group Support System practice and research should recognize the interaction of group, task, and technological issues. Insufficient attention to this interaction leads to bogus conclusions.

Attention to integrating information generated at multiple sessions by means of knowledge base technology to create a “meeting memory” is an important consideration.

Automated support for groups tends to change the way people work together, e.g., in terms of average meeting size, methods of addressing a complex problem, and group dynamics.

Capacity to provide flexible support for a variety of tasks is crucial. The dynamic nature of group activities and subtasks within a primary task is a particularly important concern.

To achieve broadbased use and institutionalized status, Group Support System technology must be interconnected and integrated within broader organizational information systems.

The following sections of this paper will expand on the conclusions listed and will discuss their implications for the development and operation of Group Support Systems as well as opportunities for additional research.

## Findings

Through our efforts to make automated support for groups operational, we have discovered much at the University of Arizona about the nature of the interactions among people, technology, and tasks. Evaluation techniques including case studies [e.g., Vogel and Nunamaker (1987)], field studies [e.g., Applegate (1986)], and laboratory experiments [e.g., Jessup, Tansik, and Laase (1987),

A. Easton (1988), G. Easton (1988)] have been employed and the results obtained have contributed to our knowledge. The complex and multifaceted nature of Group Support Systems requires that a variety of efforts and methodologies be called upon to address the multitude of research questions that exist. Matching the appropriate approach and methodology to the particular question being addressed is therefore a key responsibility.

Our direct experience is based upon having worked with more than 90 public and private organizations in two specially designed facilities and hundreds of experimental sessions with student subjects. Feedback also has been received from other domestic and international institutions that use our software and from groups working at sites within a major multi-national corporation that are modeled upon the facility illustrated in fig. 2. The following sections on benefits for larger groups, task dynamics, interaction of group tasks and technology, multiple session benefits, integration of information technology, and group process impact summarize our findings and propose opportunities for additional research.

## Larger Group Benefits

In a traditional meeting environment, conversation proceeds sequentially, with one member speaking at a time and other group participants listening and thinking about what they will say if and when they have an opportunity. Group efficiency degrades with increased group size. Since automated support removes this constraint, automation makes it possible for every member of the group to contribute at the same time, i.e., human parallel processing is achieved. In traditional terms, it is as if everyone in the group is able to talk at once and still hear and reflect on everything that is being contributed. Furthermore, the automated support seems to facilitate organization of multiple conversations around streams of thought. The opportunity for multiple conversations also increases exponentially with group size, with an upper bound of $n(n-1)/2$ where “n” is the group size. Because a group of size 4 contends with only 6 potential conversation paths while a group of size 12 contends with 66 potential conversation paths, the ability of automated support to facilitate multiple conversations efficiently becomes increasingly apparent as group size in creases. Additionally, the ability to support multiple conversations allows a group to address a number of issues in a relatively simultaneous fashion without having the meeting led off-track on a single issue. Members can rapidly share information and educate each other in a non-threatening fashion. This, in turn, has a direct impact on user satisfaction. The end result is that automated support contributes to enhanced meeting effectiveness.

Group size, however, should be treated as a relative rather than an absolute characteristic. The extent of group member domain knowledge concerning the task at hand can easily result in having the “logical size” of a group be significantly different from the physical group size. Group member domain knowledge is the knowledge that an individual member has relative to the question before the group. Typically, a group member’s domain knowledge overlaps to some extent with that of other members because each possesses unique expertise, opinions, or experience as well as some common knowledge of task issues. The degree of overlap can vary significantly, however, as a function of cumulative group experience, culture, and the nature of the task. A physically large group from a common culture that has met repeatedly on a task may have a high degree of overlapping domain knowledge that results in the group being “logically” small. Conversely, a physically small multi-cultural group exhibits characteristics of a much larger group because its members have multiple and often conflicting perspectives, points of view, diverse knowledge domains, and opinions that make it “logically” large. Furthermore, as task complexity increases within a given physical group size and culture, the overlap between member knowledge domains tends to decrease as members are required to draw on a variety of experiences. Different tools and facilitation techniques are necessary to meet the needs of various types of groups. Group time spent on idea generation is not well used when there is a high degree of member domain knowledge overlap. Tools with a high degree of specificity or focus are less appropriate in early stages of deliberation by groups with widely dispersed domain knowledge. Our experience has shown that, ultimately, group “logical size” is a more important indicator of which tools can best meet a particular group’s needs than is “physical size.”

The variability inherent within groups of different sizes presents numerous research caveats and opportunities. To always use small groups of student subjects who have similar knowledge domains can only lead to conclusions about the impact and implications of Group Support Systems that may not be appropriate to ultimate organizational use. DeSanctis and Gallupe (1987, p. 603) state that “users must have extended experience with GDSS before the effectiveness or ineffectiveness of systems design can be fully assessed.” We concur. In our opinion, failure to use “seasoned” groups undertaking sufficiently complex tasks in realistic contexts with appropriate technological support has rendered suspect many empirical findings. We suggest that researchers should carefully consider the diverse aspects of groups, task, context, and technology that might confound study results and thereby adversely affect researcher ability to draw conclusions and compare results across studies.

## Task Dynamics

We often speak of tasks as falling into categories such as McGrath's (1984) circumplex of planning, creativity, intellective, decision-making, cognitive conflict, and mixed motive tasks. It is important, however, that we recognize the dynamic nature of group activities and subtasks within a primary task environment. For example, a planning task may also exhibit aspects of creativity, decision-making, and cognitive conflict or mixed motive subtasks. A decision-making task can have phases when creativity and cognitive conflict subtasks involve negotiation while group members seek better understanding of the nature and implications of alternatives, especially when they attempt to decide issues have no right answer. The subtasks of any overall task can vary substantially over time and be even further decomposed into subphases of activity as a group addresses a complex problem or question. Groups tend to work back and forth between various task types as they deal with different aspects of their primary focus. Thus a circumplex of tasks should not be viewed as merely a static representation within which problems can be neatly categorized but as a more dynamic means of assisting in the tracking of group activities within a general task arena. We have found different types of automated support tools to be appropriate for different activities so the tools must be flexible and inter-connected if they are to facilitate “seamless” integration of various foci. Integrative mechanisms and information repositories are essential for automated support “tool kits” that will provide maximum group support.

To achieve optimal Group Support System capabilities, researchers must undertake tasks that reflect complexity and ambiguity and include multiple subtasks that are characteristic of complex organizational problem environments. Unfortunately, research related to task issues has tended to focus on the impact of individual tools addressing a single task. For example, Gallupe (1985) evaluated the impact of a “choice supporting” tool under differences in problem complexity. Nunamaker, Applegate, and Konsynski (1987) examined the impact of a tool focusing on idea generation. Watson (1987) and Zigurs (1987) dealt with aspects of the impact of Group Support Systems using resource allocation tasks. However, research has only begun to either systematically explore the impact of using combinations of tools [G. Easton (1988)] or suggest rules for combining tools specifically to meet the needs of a particular group addressing a defined task, much less extended this exploration to more complex task domains.

There are additional research opportunities in the potential extension of the domain of Group Support System task coverage, particularly as constraints imposed on group processes by lack of technological support are removed. There are increasing numbers of opportunities to explore application of automated support in extended task domains. These include aspects of problem finding and exploration prior to identification of particular questions and evaluation of the impact of proposed policies or plans on the existing organizational structure. Particular attention should be given to the nature of information that will be required in conjunction with resolution of a task and how that information will be communicated and utilized by group members. Comparison of results achieved using automated and manual versions of two or more structured techniques may help identify indicators of Group Support System success and provide guidance for development of hybrid approaches that embody the best of manual and automated environments.

## Interaction of Group, Tasks and Technology

Successful operation of Group Support Systems depends heavily on the interaction of facility design, hardware, software, and facilitation with user profiles and task requirements. Facility design includes characteristics of the meeting room, lighting, and physical organization of the technology that together provide the environment in which the group decision making process takes place. Ignoring the importance of the setting may hinder or even prevent successful group decision making. Failure to provide sufficient hardware and powerful yet easily used software can lead to user dissatisfaction and inadequate conclusions. Interfaces should be flexible, recognizing differences in user “keyboard literacy” and familiarity with the way the support system functions.

Research addressing the implications of shifting and redistributing cognitive tasks from the user to the technological environment suggests that technological capability is being underutilized [Fjeldstad (1987)]. Research has also demonstrated that user interface and on-demand help are complicated issues that are important to successful system use [Smith (1988)]. The fragile nature of the group process dictates that the software used should not impose upon or frustrate users. Software should encourage user interaction through effective use of color, high resolution graphics, overlays, windowing, on demand help screens, and other features that help group members feel that they are receiving a measure of professional respect and at the same time gives them confidence in the system's support capabilities.

Research opportunities related to the human-machine interface include not only aspects of effective technological support for individual group members but also aspects of group feedback from cumulative member contributions. In addition to keyboards and screens as we know them, interface devices include alternative methods that can support human-machine interaction and present information in a “user friendly” manner. Frameworks for modeling user-computer interactions have been developed, and these suggest there are possibilities for developing a language for information presentation and elicitation in the user-computer dialogue process [Kuo (1985)]. From an expert systems perspective, there are research opportunities in the areas of embedding facilitator expertise and aspects of system usage experience in the knowledge base and of creating on-line process monitoring that would allow the Group Support System more effectively to assist groups.

## Multiple Session Benefits

Addressing a complex problem environment often requires multiple group sessions potentially involving different participants at various phases in the process. An important facet of automated support for groups lies in effectively and efficiently integrating results across sessions and organizational layers, using knowledge base technology. Continuity between sessions is important to ensure that the group “stays on track” relative to the broader nature of the problem and direction from top corporate levels. For example, information system strategies can be effectively and efficiently aligned to be truly supportive of organizational strategies. Multiple session support also facilitates integration of information across traditional organizational boundaries. An example is examination of corporate processes across different functional areas with a goal of streamlining complex activities.

Group Support Systems further provide a “meeting memory”. All comments are permanently recorded as they are made. Group members have opportunities to review the full discussion or areas of particular interest at their discretion, in either hardcopy or electronic format. Future group sessions can be started where previous sessions left off without the need to “backtrack” to bring new members up to speed. Of particular benefit is the ability of the group to recognize and respond quickly to changes in increasingly turbulent business climates based on an understanding of conditions and assumptions identified at previous group meetings. The probability of overlooked problems, misunderstandings, and incomplete appreciation of issue interrelationships can be minimized through effective use of information integrated from multiple sessions.

Provision of effective and efficient information integration between sessions and across groups is not easily accomplished, and this area offers many research opportunities. Being able quickly and effectively to link related information to make it useful to participants and facilitators remains a continuing challenge. Providing user access to information is complicated by the need to dynamically accommodate a wide variety of user needs and skills. Semantic browsing systems [Valacich, Vogel, and Nunamaker (1988)] offer just one approach to solving this problem. Finally, representation and presentation of information in a manner which illustrates the whole while preserving details of the parts [Tufte (1983)] is particularly relevant to the characteristically complex and “messy” nature of Group Support System information. Group member mental models need to be preserved within the broader and more comprehensive display of the bigger picture.

## Integration of Information Technology

The importance of interconnecting and integrating Group Support System technology within broader organizational information systems should not be underestimated. Group Support Systems cannot exist as isolated entities. As an integral part of the organizational information systems, Group Support Systems become institutionalized, a used and useful day-to-day reality rather than a curiosity or overhead item. Failure to integrate Group Support Systems into broader organizational information systems may preclude widespread organizational acceptance, thereby making it difficult to demonstrate return on investment and/or longevity of usefulness. Group Support Systems must be introduced in a fashion that encourages successful proliferation of their use, recognizing the complex interrelationships involved. To accomplish this, Group Support Systems must be flexible and evolutionary in nature so they can meet changing organizational needs.

Provision of individual as well as group support is an important facet of Group Support System flexibility and integration into organizational information systems. While they deliberate, group members should have access to organizational information external to the group. When such data are available and easily accessible, groups will be able to integrate external information to complement information generated extemporaneously by group members [Vogel (1988)]. Reduction of equivocality will then be accompanied by reduction of uncertainty and the Group Support System will become an aspect of the “organizational memory.” However, provision of effective access to external information is complicated by the need flexibly to support a wide range of user computer literacy and personal preferences. Houdeshel and Watson (1987), in discussing implementation of an Executive Information System, note that considerable flexibility is necessary to support various executive patterns and styles of use. This situation exists in intensified form when executives work in groups.

Research opportunities in this area extend beyond the individual and the group as units of analysis. On an organizational level, there are questions of the implications of the use of Group Support Systems to enhance organizational competitiveness. Experience with Group Support Systems may precipitate changes in the way we work. The opportunity exists to treat projects as units of analysis within which patterns of group sessions can be compared. Investigation of performance and productivity issues involves aspects of user, task, and technology that extend beyond single sessions. Application of artificial intelligence to acquire and integrate information internal and external to the group presents additional research opportunities. Systematic environmental scanning is but one of many examples.

## Group Process Impact

Historically, meeting size has been constrained by the need to convene in a face-to-face environment with little or no support for multiple conversations.

As many smaller meetings as necessary have been used to address complex problems, with different groups addressing various problem facets. Differences between groups are typically resolved by additional meetings with representatives from the various groups. Automated support removes these traditional meeting constraints because it promotes efficient information exchange and sharing, thus permitting group size to be increased without adversely affecting group efficiency. Because additional members can be simultaneously involved in reduction of equivocality among various perspectives and problem resolution group effectiveness is improved. Furthermore, the need for additional meetings to resolve inter-group differences is decreased and this increases overall project efficiency. Finally, in many cases, meetings need not be held in a face-to-face mode, thereby reducing travel and scheduling time. Overall, both the number and frequency of meetings are substantially cut, resulting in shorter project elapsed time without group member “burn-out.” The end result is a significant reduction in the total number of people hours expended to address and resolve complex questions. Individual, group, and organizational productivity are all enhanced.

The anonymous nature of automated support for group communication has a direct impact on conflict management. Numerous authors [e.g., Nunamaker, Applegate, and Konsynski (1987)] have noted that automated support tends to raise the potential for conflict within a group as members tend to enter challenging comments through the electronic medium without fear of personal recognition or retribution. This increased potential for conflict is offset, however, by the technology acting as a “buffer” on the receiving end. Recipients of conflict-inducing comments tend to give more reasoned consideration before responding than probably would occur in a face-to-face environment, where the potential for an argument to erupt would be high. Group members tend to focus more on content than on personalities, and the encouragement of group members to participate tends, overall, to result in a better shared sense of solution and “buy-in” of group members. Issues are surfaced and critically reviewed without group members having to “take a stand” prematurely. Group members find it easier to judge the merits of suggestions and adjust their own opinions, if appropriate, in a more personally detached frame of mind. The end result is a heightened sense of achievement and satisfaction with the outcome than might be achieved in a face-to-face meeting environment.

Research opportunities abound in the area of achieving a better understanding of the impact of Group Support Systems on group dynamics. It is important to recognize that it is not necessary to be constrained by technology or historical modes of operation and that it is possible to strive to go beyond examining that which currently exists. Studies related to meeting size provide but one example; the impact of size variations on different types of meetings has not been sufficiently explored. Another example is exploration of the effects of proximity. Decision rooms without walls are achievable with contemporary technology but the effects they may have on group process are, for the most part, unknown. Overall, Group Support Systems facilitate new forms of interaction as well as provide more efficient support for traditional forms of interaction that can help organizations cope with increased environmental uncertainty.

## Conclusion

As we begin to see a positive effect of Group Support Systems in organizational contexts their future shows great promise. Nevertheless, we are still in the “horseless carriage” phase of Group Support System functionality. Basically, we have done little more than insert a computer into traditional paper and pencil approaches. Still to be envisioned is a marriage between the best that technology has to offer and human capabilities that will effectively unite group and organizational needs. Not only time, research, and experience, but also attitudes that allow Group Support Systems to evolve gracefully will play important roles in development of the technology. We feel that the complex nature of Group Support Systems precludes examining their role based on a single methodological approach and/or a single perspective. If any single perspective is given too much authority, a distorted view of a complex phenomenon will result. On the other hand, approaching research from multiple perspectives will enrich our understanding and provide a solid foundation for future Group Support System research and development.

## References

Ackoff, R., Towards A System of System Concepts, Management Science, July, 1971, pp. 661–671.

Applegate, L., Idea Management in Organization Planning, Unpublished Doctoral Dissertation, University of Arizona, 1986.

Atrium, L. and Lax, D., Support and Analysis for International Commercial Debt Negotiations, Proceedings of the 31 Annual Meeting of the International Society for General Systems Research, Budapest, Hungary, June 1–5, 1987.

Bui, T. et al., Identifying Organizational Opportunities for GDSS Use: Some Experimental Evidence, Proceedings of the 7th International Conference on Decision Support Systems. June 8–11, 1987.

Checkland, P., Systems Thinking, Systems Practice, Wiley: New York, 1981.

Churchman, C.W., The Systems Approach, Delhi: New York, 1968.

Cohen, M., March, J. and Olsen, J., A Garbage Can Model of Organizational Choice, Administrative Science Quarterly, 16 (4), 1971, pp. 413–428.

Cyert. R. and March, J., A Behavioral Theory of the Firm, Prentice-Hall: Englewood Cliffs, NJ, 1963.

Davis, G. and Olson, M., Management Information Systems: Conceptual Foundations, Structure, and Development, 2nd edition, McGraw Hill: New York, 1985.

DeSanctis, G. and Gallupe, B., A Foundation for the Study of Group Decision Support Systems, Management Science, 33(5), May, 1987, pp. 589–609.

Easton, A., An Experimental Investigation of Automated versus Manual Support for Stakeholder Identification and Assumption Surfacing in Small Groups. Unpublished Doctoral Dissertation. University of Arizona, 1988.

Easton, G., Group Decision Support System versus Face-to-Face Communication for Collaborative Group Work: An Experimental Investigation, Unpublished Doctoral Dissertation, University of Arizona, 1988.

Fjeldstad, O., On the Reapportionment of Cognitive Responsibilities in Information Systems, Unpublished Doctoral Dissertation, University of Arizona, 1987.

Galbraith, J., Organization Design, Addison-Wesley: Reading, MA, 1977.

Gallupe, B., The Impact of Task Difficulty on the Use of a Group Decision Support System, Unpublished Doctoral Dissertation, University of Minnesota, 1985.

Gray, P. et al., The SMU Decision Room Project," Transactions of the First International Conference on Decision Support Systems, Atlanta, GA, June, 1981, pp. 122–129.

Hiltz, S. an Turoff, M., The Evolution of User Behavior in a Computerized Conferencing System, Communications of the ACM, 24 (11): 739, 1981.

Houdeshel, G and Watson, H., The Management Information and Decision Support (MIDS) System at Lockheed-Georgia, MIS Quarterly, March, 1986, pp. 127–140.

Huber, G., Group Decision Support Systems as Aids in the Use of Structured Group Management Techniques, DSS-82 Conference Proceedings, 1982, pp. 96–108.

Huber, G., The Nature and Design of Post-Industrial Organizations, Management Science, 30 (8), August, 1984, pp. 298–951.

Huber, G., Issues in the Design of Group Decision Support Systems, MIS Quarterly, September, 1984.

Huber G. and McDaniel, R., The Decision-Making Paradigm of Organizational Design, Management Science, 32 (5), May, 1986, pp. 572–589.

Janis, I., Victims of Groupthink: A Psychological Study of Foreign Policy Decisions and Fiascos, Houghton-Mifflin: Boston, MA, 1972.

Jessup, L.M., Tansik, D., and Laase, T.D., Group Problem solving in an automated environment: The effects of anonymity and proximity on group process and outcome with a group decision support system, Proceedings of the Academy of Management, Anaheim, CA, August, 1988.

Konsynski, B., Kottemann, J., Nunamaker, J., Stott, J., Plexsys-84: An Integrated Development Environment for Information Systems, Journal of Management Information Systems, 1 (3), 1984.

Kotteman, J. and Konsynski, B., Information Systems Planning and Development: Strategic Postures and Methodolo-

gies, Journal of Management Information Systems, 8 (3): 195, 1983.

Kraemer, K. and King, J., Computer-Based Systems for Cooperative Work and Group Decision Making, ACM Computing Surveys, 20 (2), June, 1988, pp. 115–146.

Kuo, Feng-Yang, An Architecture for Dialogue Management Support in Information Systems, Unpublished Doctoral Dissertation, University of Arizona, 1985.

Lewis, F., Facilitator: A Microcomputer Decision Support System for Small Groups, Unpublished Doctoral Dissertation, University of Louisville, 1982.

Maruyama, M., Communication Between Mindscape Types, in Decision Making About Decision Making, J. Van Gigch (editor), Abacus Press: Cambridge, MA, 1987.

Mason, R. and Mitroff, I., Challenging Strategic Planning Assumptions, John Wiley and Sons: New York, 1981.

McGrath, J., Groups: Interaction and Performance, Prentice-Hall: Englewood Cliffs, NJ, 1984.

McIntyre, S., Konsynski, B., Nunamaker, J., Automated Planning Environments: Knowledge Integration and Model Scripting, Journal of Management Information Systems, 1987.

Miller, G., The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capability for Processing Information, The Psychological Review, 63 (2), March, 1956, pp. 81–97.

Minch, P. and Sanders, G., Computerized Information Systems Supporting Multi-criteria Decision-making, Decision Sciences, Summer, 1986, pp. 395–413.

Newell, A. and Simon, H., Human Problem Solving, Prentice-Hall: Englewood Cliffs, NJ, 1972.

Nunamaker, J., Applegate, L., and Konsynski, B., Facilitating Group Creativity: Experience with a Group Decision Support System, Journal of Management Information Systems, Spring, 1987, pp. 5–19.

Osborn, A., Applied Imagination, (rev. ed.) Scribner's: New York, 1957.

Pava, C., Managing New Office Technology: An Organizational Strategy, Free Press: New York, 1983.

Pounds, W.F., The Process of Problem Finding, Sloan Management Review, 1 (20), Fall, 1969, pp. 1–19.

Rohrbaugh, J., Improving the Quality of Group Judgment: Social Judgment Analysis and the Nominal Group Technique, Organizational Behavior and Human Performance, 28, 1981, pp. 272–288.

Shaw, M.E., Group Dynamics: The Psychology of Small Group Behavior, third edition, McGraw-Hill: New York, 1981.

Shakum, M., Evolutionary Systems Design: Policy Making

Under Complexity and Group Decision Support Systems, Holden-Day, Inc.: Oakland, CA, 1987.

Simon, H., The New Science of Management of Decision, Harper and Row: New York, 1960.

Smith, T., Assessing the Usability of User Interfaces: Guidance and Online Help Features, Unpublished Doctoral Dissertation, University of Arizona, 1988.

Trist, E. and Banforth, K., Some Social and Psychological Consequences of the Longwall Method of Coal Getting, Human Relations, 4 (1), 1951, pp. 3–38.

Tufte, E., The Visual Display of Quantitative Information, Graphics Press: Cheshire, CN, 1983.

Turoff, M. and Hiltz, S., Computer Support for Group Versus Individual Decisions, IEEE Transactions on Communications, 1982, 30 (1), 82–90.

Tversky, A., Elimination by Aspects: A Theory of Choice, Psychological Review, 79, 1972, pp. 281–299.

Valacich, J., Vogel, D. and Nunamaker, J., A Semantic Guided Interface for Knowledge Base Supported GDSS, Transactions on Decision Support Systems, June, 1988.

Van de Ven, A. and Delbecq, A., Nominal Versus Interacting Group Processes for Committee Decision Making, Academy of Management Journal, 14, 1971, pp. 203–213.

Vogel, D., The Impact of "Messy" Data on Group Decision Making, Proceedings of the 21st Annual Hawaii International Conference on System Sciences, January 5–8, 1988.

Vogel, D. and Nunamaker, J., Health Service Group Use of Automated Planning Support, Administrative Radiology, September, 1988.

Vogel, D., Nunamaker, J., Applegate, L. and Konsynski, B., Group Decision Support Systems: Determinants of Success, Transactions on Decision Support Systems, June 8–11, 1987.

Watson, R., A Study of Group Decision Support System Use in Three and Four-person Groups for a Preference Allocation Decision, Unpublished Doctoral Dissertation, University of Minnesota, 1987.

Wright, W., Cognitive Information Processing Biases: Implications for Producers and Users of Financial Information, Decision Sciences, 11, 1980, pp. 284–298.

Wright, P. and Barbour, F., Phased Decision Strategies: Sequels to an Initial Screening, TIMS Studies in the Management Sciences, 6, 1977, pp. 91–109.

Zigurs, I., The Impact of Computer-Based Support on Influence Attempts and Patterns in Small Group Decision Making, Unpublished Doctoral Dissertation, University of Minnesota, 1987.
