---
otero_id: 20839
otero_key: "77UV2NPY"
title: "An organizational decision support system for managing the DOE hazardous waste cleanup program"
authors: "Tarun K Sen; Laurence J Moore; Traci J Hess"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00066-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An organizational decision support system for managing the DOE hazardous waste cleanup program

Tarun K. Sen <sup>a,)</sup>, Laurence J. Moore <sup>b</sup>, Traci J. Hess <sup>c</sup>

<sup>a</sup> Department of Accounting and Information Systems, Pamplin College of Business, Virginia Tech., 7054 Haycock Road, Falls Church, VA22043, USA

<sup>b</sup> Department of Management Science and Information Technology, Pamplin College of Business, Virginia Tech, Blacksburg, VA24061, USA

<sup>c</sup> Department of Management Information Systems, College of Business Administration, UniÕersity of Central Florida, Orlando, FL32816-1400, USA

Accepted 24 February 2000

## Abstract

Organizational Decision Support Systems ODSS are a form of DSS that provide support for multiple decision-makingŽ . processes in an organization. These systems differ from other forms of DSS in that several functionally distinct decision-making tasks are supported. In this paper, we describe an ODSS, the EM50-ODSS, that was designed to support the Department of Energy’s DOE hazardous waste clean up efforts. The cleanup effort is to take place over a 30-year periodŽ . and the process must integrate the activities of academic institutions, consultants, outside contractors and the Office of Environmental Restoration and Waste Management EM , a subdivision of DOE. The Office of EM was formed to organizeŽ . and monitor the cleanup effort, apply available technology to waste problems and make investment decisions with regard to developing new technologies to address unmet waste resolution needs. A system was needed to integrate many resources from various divisions in DOE and outside parties and provide support for multiple decision-making processes within the different functional areas of EM. This system is described in terms of an ODSS taxonomy and framework. A description of the design issues involved in developing the EM-50 ODSS is provided. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: DSS; ODSS; MDSS; Hazardous waste; Environmental management; Environmental restoration; Taxonomy

## 1. Introduction

In August of 1989, the Department of Energy Ž . DOE published a revolving 5-year plan to bring DOE into compliance with environmental laws and clean up over 3700 hazardous and radioactive substance release sites. A new Office of Environmental Restoration and Waste Management EM was cre-Ž . ated for the purpose of carrying out the plan 4,5 .<sup>w</sup> <sup>x</sup> The issuance of the 5-year plan and the formation of the EM office were the DOE’s initial responses to public and governmental demands for environmental protection and restoration and for providing public access to information regarding these efforts. In the first 5-year plan, the DOE-EM made a commitment to attain compliance and complete the cleanup in 30 years at all sites connected to the DOE’s past, current and future nuclear programs 4 . The research<sup>w</sup> <sup>x</sup> and development R&D necessary to provide tech-Ž . nologies to enable the cleanup of hazardous waste was a fundamental aspect of this plan.

Information on technologies that are available for cleaning up hazardous waste, or technologies under development, was widely dispersed among the many organizations involved in such research. The DOE, private contractors, consultants, industrial partnerships, universities and national research laboratories all actively participate in the research and development activities to produce thousands of technologies related to hazardous waste cleanup. Prior to the formation of EM, the DOE’s need for clean up technologies at these sites was classified i.e., un-Ž available to the public information. Additionally,. this classified information was distributed among several different offices of the DOE. Essential to the success of EM’s 30-year commitment to cleanup hazardous waste was an information system that maintained data on technology needs and technology developments and supported decision making in matching these technologies to cleanup efforts in this inter-organizational, distributed environment.

Several characteristics of the requested information system brought about its designation as an Organizational Decision Support System ODSS . ODSSŽ . can be differentiated from other forms of DSS by the requirement that these systems support decisionmaking tasks in various functional areas and at various hierarchical levels within an organization 7,10 .<sup>w</sup> <sup>x</sup> The system being developed would need to provide decision-making support to users for the various functions within the DOE and for users external to the organization. These users include managers, team leaders and team members, supervisors within the DOE, researchers<sup>r</sup>contractors from industry and academia, and public stakeholders i.e., congress andŽ the general public . The use of technology to support . communication and coordination among multiple, distributed users was also a requirement of the system and a common trait of ODSS.

In this paper, we describe an ODSS, EM50-ODSS, that was designed and developed to support the DOE’s mandate for EM and discuss how this system can be classified within existing ODSS research. The EM50-ODSS was specifically designed to serve as a central data repository for hazardous waste needs and technologies, match needs with available technologies, identify gaps in the available technologies needed, prioritize hazardous waste research and development, and allocate funds within technology development portfolios. In the next section of this paper, Section 2, we provide some background information on the technologies, a taxonomy, and a framework described in the ODSS literature. We describe the problem domain of EM and its need for an ODSS in relation to the taxonomies and frameworks of ODSS in Section 3. The specific decision processes to be supported by the ODSS and the data model used are described in Sections 4 and 5, respectively. The prototype implementation is described in Section 6. We summarize the paper in Section 7 and identify some future research opportunities for ODSS in general and the EM50-ODSS.

## 2. Organizational decision support systems

ODSS have emerged in the past decade as a new class of decision support systems DSS that focus Ž . on organizational decision making. An ODSS is a DSS that supports multiple, functional areas in an organization instead of a single decision-maker or a group of centrally located decision-makers focused on one decision-making scenario. This category of DSS was initially set forth by some of the pioneers of DSS, including Hackathorn and Keen 9 and <sup>w</sup> <sup>x</sup> Huber 11 in the early 1980s. The groundwork laid <sup>w</sup> <sup>x</sup> by research on DSS 12,20 and group decision <sup>w</sup> <sup>x</sup> support systems GDSS 3,14 along with the de- Ž . <sup>w</sup> <sup>x</sup> creasing cost of hardware has made implementations of ODSS more feasible and commonplace. As a result, ODSS has become a significant stream of research and application over the past several years <sup>w</sup> <sup>x</sup>7,8,13,17 .

An ODSS can be distinguished from other types of DSS by its scope. Specific DSS or GDSS typically provide decision-making support for a task or activity within one functional unit of an organization <sup>w</sup> <sup>x</sup> 3,20 . An ODSS provides decision-making support for multiple tasks or activities that involve multiple functional units within an organization 6,7 . Unlike <sup>w</sup> <sup>x</sup> GDSS, where multiple users receive decision support concurrently in a common location, ODSS are typically implemented in a distributed environment where users can access and interact with the system from remote sites both independently and concurrently with other users.

## 2.1. An ODSS taxonomy

ODSS have been described by the information technologies they employ and the type of organizational structures they support. The types of technology implemented within an ODSS should be determined by the type of organizational structure that the ODSS was designed to support 8 . George et al. 8<sup>w x</sup> <sup>w x</sup> described three prominent trends in organizational change that would necessitate different ODSS architectures: 1 downsizing, 2 an emphasis on teams,Ž . Ž . and 3 outsourcing. In a downsizing environment, Ž . the reduction in workers and the number of hierarchical levels within the organization place more emphasis on intra-organizational communication, filtering and monitoring technologies. In an environment where workers complete tasks in teams, intra-team communication, coordination and decision making technologies would receive more emphasis. Interorganizational communication would be the fundamental technology employed in an outsourcing environment, where vital information is exchanged between the organization and outside contractors 8 .<sup>w</sup> <sup>x</sup>

A taxonomy of these organizational objectives and ODSS technology was initially set forth by George et al. 8 in the early 1990s. The importance <sup>w</sup> <sup>x</sup> of the technologies relative to the organizational strategy was also specified within the taxonomy. An extended version of this taxonomy is shown in Table 1. The original taxonomy included the first three organizational strategies shown as column headings in Table 1 downsizing, teams, and outsourcing andŽ . the first four technologies shown as row headings Žcommunication, coordination, decision making, and monitoring ..

A fifth technology, filtering, was also included by George et al. 8 . Filtering was described as technol- <sup>w</sup> <sup>x</sup> ogy that would ‘‘filter and summarize information, e.g., intelligent e-mail’’ 7, p. 122 . In the extended<sup>w</sup> <sup>x</sup> taxonomy shown in Table 1, filtering has been replaced with artificial intelligence to better represent the wide range of intelligent technologies that have appeared in the last decade. Intelligent mechanisms such as filtering have been applied to many domains, including email. Intelligent agents show particular promise as a means to filter, summarize, and automate information retrieval and other tasks within our complex computing environment.

A taxonomy of organizational objectives and ODSS technology extended from George et al. 8 Ž <sup>w</sup> <sup>x</sup>.

<table><tr><td rowspan="2">ODSS Technology</td><td colspan="4">Organizational Objective</td></tr><tr><td>Downsizing</td><td>Teams</td><td>Outsourcing</td><td>Inter-organizational Integration</td></tr><tr><td>Communication</td><td></td><td></td><td></td><td></td></tr><tr><td>Coordination</td><td></td><td></td><td></td><td></td></tr><tr><td>Decision Making</td><td></td><td></td><td></td><td></td></tr><tr><td>Monitoring</td><td></td><td></td><td></td><td></td></tr><tr><td>Artificial Intelligence for filtering/automation</td><td></td><td></td><td></td><td></td></tr><tr><td>Data/knowledge representation</td><td></td><td></td><td></td><td></td></tr><tr><td>Processing and presentation</td><td></td><td></td><td></td><td></td></tr><tr><td>Distributed Architectures</td><td></td><td></td><td></td><td></td></tr></table>

In a related paper, George 7 suggested two<sup>w</sup> <sup>x</sup> additional categories of technology to be included in the taxonomy, 1 data Ž . <sup>r</sup>knowledge representation and 2 processing and presentation technologies Ž . based upon his review of other research in the realm of ODSS. These two additional categories of technology have been incorporated into the extended taxonomy. The category of data<sup>r</sup>knowledge representation includes those technologies that support the storage of data and knowledge within the ODSS. The category of processing and presentation includes those technologies used for data processing and for presenting information to the user. Both of these categories were noted in the taxonomy as being key requirements for organizations with the objectives of downsizing and teams due to the crucial role of data and presentation in any information system. The technologies were both noted as having little direct benefit in organizations pursuing the strategy of outsourcing, as the storage of data<sup>r</sup>knowledge along with data processing and presentation would presumably be outsourced in such organizations.

As a result of our own efforts in designing and implementing an ODSS, we have suggested one additional technology, distributed architectures, and an additional organizational strategy, inter-organizational integration, that reflect some of the more recent trends in computing. Distributed architectures include those technologies that facilitate the distributed storage of data and<sup>r</sup>or the distributed<sup>r</sup>parallel processing of data. This includes the ubiquitous web technology also. Within the ODSS taxonomy, distributed architectures are noted as being a somewhat needed for organizations with the objective of using a team-based structure as teams would benefit from having the relevant data close at hand and from the flexibility provided by a tiered architecture. Organizations pursuing outsourcing and downsizing strategies would find a distributed architecture to be of little direct benefit as outsourcing organizations would not be addressing such issues in-house and downsizing organizations would have a reduced interest in distributed storage and processing.

The new organizational objective added to the taxonomy, inter-organizational integration, represents the strategy of seeking integration with other closely related organizations. Electronic integration in the form of EDI Electronic Data Interchange and Ž . extranets has become increasingly common in the last 5 years. Web-based applications provide another avenue for organizations seeking electronic integration with corporate partners. An organization pursuing such a strategy would find most forms of information technology essential for supporting a successful ODSS. All of the technologies included in the taxonomy, with the exception of monitoring, would be key requirements due to the number of distributed users seeking access to the ODSS through various mediums. The presence of multiple corporate cultures and processes would require increased communication and coordination. Artificial intelligence would be required to filter, summarize, and automate information retrieval for users accessing the large volume of information stored in such an ODSS. Monitoring, however, would not be an essential technology, as the ODSS would provide a comprehensive view of corporate goals and decision-making processes. Decision making support and the status of decision-making processes would be provided by the system.

## 2.2. A multiparticipant DSS architecture

Holsapple and Whinston 10 have developed a<sup>w</sup> <sup>x</sup> generic architecture for multiparticipant decision support systems MDSS . This framework is applica-Ž . ble to ODSS as these systems support multiple participants. As shown in Fig. 1, there are four components in a MDSS, a language system, a problem processing system, a knowledge system and a presentation system. Users would send requests to a MDSS through the language system and receive responses through the presentation system. The knowledge system provides storage for the various types of knowledge used by the system. The problem processing system processes requests received through the language system, often interacting with the knowledge system, and then generates a response

A Multiparticipant Decision Support System

![](/api/attachments/77UV2NPY/fulltext/images/2cd26e89ae1964e4ecffb34d21f985131f54dd1cddb244be03b6036b732b7092.jpg)  
Fig. 1. A generic MDSS architecture 10 . <sup>w</sup> <sup>x</sup>

that is sent back to the user through the presentation system.

This framework was used to guide the development of the EM50-ODSS. The use of public and private messages and public and private knowledge stores within the generic MDSS architecture was a crucial feature in our design of the EM50-ODSS. The multitude of users at various hierarchical levels within different organizations mandated the differentiation between public messages and knowledge and private messages and knowledge. The public aspects of the system were those messages and knowledge that all users could access. The private aspects of the system were those messages and knowledge that only some users could access. Semi-private messages and knowledge stores were also used in the system. Other aspects of the MDSS architecture, such as the facilitator and relational knowledge, were not used in designing the EM50-ODSS as such features were most useful in group decision support and negotiation support environments.

## 3. EM50-ODSS design framework

The ODSS described in this paper was designed to support a new organization that had been given an objective previously unassigned to any single function or division. The office of EM was a newly created organizational unit within the DOE and its mandate to achieve regulatory compliance and cleanup contaminated sites in 30 years was previously unspecified. Information and expertise on the topic of hazardous waste was distributed among many independent departments and organizations, and a significant percentage of the research and implementation of hazardous waste technology was performed by outside consultants, external contractors, and universities. The level of involvement needed between the EM program and the various outside entities, however, was much more collaborative and extensive than in a typical outsourcing arrangement. The new EM organization and the requested decision support provided an ideal scenario for the design and implementation of an ODSS.

## 3.1. DOE-EM background

DOE’s 5-year plan for EM focused on eliminating or reducing the risks of hazardous waste contamination to workers, the public, and the environment due to past nuclear programs. To achieve these goals, three functional areas were established within EM. The Office of Waste Operations was responsible for the treatment, storage and disposal of hazardous waste at active sites. The Office of Environmental Restoration was responsible for the clean up of inactive sites, which included 110 sites located in 32 states and 1 site in Puerto Rico 4 . The Office of<sup>w</sup> <sup>x</sup> Technology Development, known as EM-50, was responsible for research and development of new technologies to assist Waste Operations and Environmental Restoration. The DOE’s goals for reducing risk could only be met by applying existing technologies and developing new technologies for unmet needs.

The major thrust of the EM-50 program is the development of technologies to address problems related to hazardous waste sites. The EM program manages four categories of radioactive waste. 1Ž . High level waste HLW is highly radioactive. ItŽ . usually results from the reprocessing of spent nuclear fuel. High level waste needs careful handling from behind protective shielding. 2 Low level wasteŽ . Ž . LLW is used to classify any radioactive waste that is not high level. Low level waste is usually contaminated with small amounts of radioactivity. 3Ž . Transuranic waste is low level waste that contains man-made elements heavier than uranium. 4 Ura- Ž . nium mill tailings are by-products of mining uranium and occur naturally. Apart from these four categories of nuclear waste EM manages other mixed hazardous waste including sanitary waste.

The technology development program is divided into six major functional areas: a groundwater andŽ .

soils cleanup, b waste retrieval and processing, c Ž . Ž . waste minimization and avoidance, d infrastructure,Ž . Ž .e technology integration and environmental education development and f program management. In Ž . each of these areas new technologies need to be developed. For example, in the area of groundwater and soils cleanup, relevant technologies include innovative directional drilling technologies, different monitoring and characterization systems, thermal remediation techniques, etc.

Various new technologies are being developed by different organizations in industry, national research laboratories, universities, DOE contractors and others. Technology development projects can be at various stages ranging from basic research and exploratory development to demonstration and implementation of successful technologies. Technology investment decisions must be made by EM at each of the various stages of development. One of the ultimate goals for the ODSS was to assist EM in making these technology investment decisions at different stages. The technology development projects needed to be prioritized using criteria such as cost, potential hazards to workers, public, and the environment, and regulatory factors.

3.2. EM50-ODSS classification within the ODSS taxonomy

DOE’s 5-year plan for EM specified the development of technology investment ‘‘portfolios’’ through which technology development projects would be evaluated and funded. These portfolios corresponded to the four categories of hazardous waste, referred to as focus areas and would be managed by focus area teams comprised of staff from various divisions within EM. In relation to the ODSS taxonomy shown in Table 1, a project or team orientation, where specific workers are assigned to an individual project was required due to the technical nature of the work and the limited availability of experts. In light of this organizational strategy, the EM50-ODSS would need to utilize the various information technology categories as shown in the teams column of the ODSS taxonomy.

In addition to a team-based structure, EM also pursues the organizational goal of inter-organizational integration. The specifications for the EM50-

ODSS required it to support decision making external to the EM organization. The decision-makers external to EM included waste removal technology developers, public stakeholders, and DOE administrators supervising EM’s activities. Thus, the technology usage suggested by the ODSS taxonomy would be a combination of the team and interorganizational integration approaches.

In considering the specific needs of EM, all of the technologies shown in the taxonomy appeared to be key requirements with the exception of monitoring. Monitoring technology was not considered a requirement due to the comprehensive nature of the EM50- ODSS and its ability to support the various decision-makers interested in the operations of EM. With regard to the technology categories of filtering<sup>r</sup>automation through artificial intelligence and distributed architecture, the inter-organizational integration need key requirement for these technolo- Ž . gies was selected over the team perspective some- Ž what needed . The volume of information stored by. the ODSS influenced the decision to view filtering<sup>r</sup>automation as a key requirement rather than somewhat needed. The distributed nature of the decision-makers and the organizations involved influenced the decision to view distributed architecture as a key requirement rather than somewhat needed.

## 3.3. The EM50-ODSS architecture

The EM50-ODSS was designed using the MDSS architecture shown in Fig. 1. A revised view of this architecture showing the specific features of the EM50-ODSS is shown in Fig. 2. The users of the system include the employees of EM serving in various organizational roles, external users such as research scientists and technology development experts in industry, public policy stakeholders such as congress and the general public, and DOE administrators. The ODSS was designed to allow access to the system through the EM intranet or the Internet. Regardless of the communication medium used, decision support for the users would be provided through the query interface and<sup>r</sup>or a report generator based upon the level of access granted to the user. More details of the user interface are provided in Section 6.

![](/api/attachments/77UV2NPY/fulltext/images/65d7c9786b339adbca785643e13fb9040821f3e8392470dd077ae6944625bf0d.jpg)  
Fig. 2. The EM50-ODSS architecture an adaptation of the generic MDSS architecture 10 . Ž <sup>w</sup> <sup>x</sup>.

As shown in Fig. 2, public, semi-private, private messages are used with the language and presentation systems depending upon the user’s allowed access to the knowledge stored within the ODSS. For example, some aspects of the system should be accessible to the general public. Using web access, the public should be able to review the many sites under EM management and evaluate the cleanup efforts underway at these sites. Information regarding specific contracts, investment allocation details, and similar financial data would not be available to the general public. Information about the access to be given to specific users or types of users is stored in the knowledge system.

Other users, such as the EM site managers would be given read access to more of the knowledge in the ODSS, but would only be able to update information regarding the categorization of contamination problems at EM sites. Some of the messages sent and received by these users would be considered semiprivate as some but not all users have access to such messages. Similarly, members of focus area teams would be able to update information relating to the matching of cleanup technologies to contamination problems, but would not be able to update the categorization of such problems.

The problem processing sub-system performs the necessary processing for the various types of messages received from users and the responses filled by the knowledge system. Specific functions of this subsystem include query formulation and the use of filtering system to help narrow down searches for the user. The sub-system also supports navigational linkages that allow information from different domains to be connected after a user’s query is processed. The problem processing system collects and processes new knowledge acquired from technology experts and stores it in the database in accordance with the specified data model. This sub-system also supports the prioritization of new technologies developed in the future.

The initial design for the knowledge system of the ODSS includes a central database that stores private, public, and system knowledge. The knowledge contained in the database can be broadly classified into two categories: system knowledge and domain knowledge. System knowledge includes information on user roles, for example, the access allowed for a particular class of user. Rules, such as functions for rating the suitability of the various cleanup technologies and for allocating funds for cleaning up specific problems would also be stored as system knowledge. Domain knowledge includes both private and public knowledge relating to the decisions to be supported and was initially obtained from many different sources. Basic research, industries involved in technology development, EM site administrators, and public policy stakeholders all contributed to the initial collection of data stored in the ODSS knowledge system.

## 4. EM50 decision model

The general objective of the EM50-ODSS was to support EM in assigning existing or prospective technologies to contamination problems and to assist in prioritizing cleanup and research and development Ž . R & D efforts. Specific decision processes to be supported by the ODSS include 1 matching tech-Ž . nologies to problems, 2 prioritizing technologiesŽ . based upon problem criteria, 3 identifying unmetŽ . requirements, and 4 allocating funds to R & D pro- Ž . jects within technology investment portfolios. EM had adopted a technology investment decision model set forth by Paladino and Longsworth 16 to manage<sup>w</sup> <sup>x</sup> research and development efforts. The model was to be integrated with the various decision processes to align R&D efforts with technology needs. The Technology Investment Decision Model established technology investment portfolios for each of the four focus areas of contamination problems: 1 Subsur-Ž . face Contamination SCFA , 2 High Level Waste Ž . Ž . Tank Remediation High Level , 3 Mixed WasteŽ . Ž . Characterization, Treatment and Disposal MixedŽ Waste and 4 Decontamination and Decommission-. Ž . ing D & D 4,5,15 . Contamination problems at the Ž . <sup>w</sup> <sup>x</sup> DOE sites would be categorized into a focus area and would be prioritized to receive cleanup services based upon a portfolio evaluation process 15,16 .<sup>w</sup> <sup>x</sup> Problems, gaps and technologies would be prioritized with respect to health, safety and cost factors. This model would enable the efficient allocation of funds within each focus area and coordinate EM’s research and development with its cleanup efforts to ensure that all of the DOE’s 3700 contaminated sites are cleaned up within the 30-year time horizon initially envisioned.

The decision model shown in Fig. 3 depicts how the decision processes described above transcend several organizational levels and departments within EM. One specific function of the ODSS is to assist the project managers in the EM’s waste management division at the various installations across the country in categorizing the contamination that exists at a site. In this capacity, the ODSS is serving as a specific DSS for workers in a lower level of EM’s organizational hierarchy. Once the problem is categorized and recorded, the project manager uses the ODSS to specify a solution to the problem using pre-defined technical requirement categories. The user can then request the ODSS to display any available technologies that match the solution specified for the contamination problem. Matching technologies are ranked according to environmental protection, public health, worker health, regulatory compliance and cost factors. A technology suitability function TSF is used to determine the rankings, as Ž . shown in Eq. 1 below. This function 16 is aŽ . <sup>w</sup> <sup>x</sup> weighted function of cost, environmental protection, public safety and health, regulatory compliance, and worker health safety assessments obtained from experts.

$$
\begin{array}{r l} \mathrm{TSF} _ {\mathrm{t}} & = w _ {\mathrm{c}} (\text {Cost\_val}) _ {\mathrm{t}} + w _ {\mathrm{e}} (\text {Env\_prot\_val}) _ {\mathrm{t}} \\ & + w _ {\mathrm{p}} (\text {Pub\_health\_val}) _ {\mathrm{t}} \\ & + w _ {\mathrm{r}} (\text {Reg\_compl\_val}) _ {\mathrm{t}} \\ & + w _ {\mathrm{w}} (\text {Work\_Health\_saf\_val}) _ {\mathrm{t}} \end{array}\tag{1}
$$

The weights $( w _ { \mathrm { c } } , w _ { \mathrm { e } } , w _ { \mathrm { p } } , w _ { \mathrm { r } }$ , and $w _ { \mathrm { w } } )$ in the technology suitability function are provided by a committee consisting of various experts and stake holders and t denotes a specific technology. However, research into the use of the analytic hierarchy process AHP 19 to assist in the development of Ž . <sup>w</sup> <sup>x</sup> these weights is also underway. Although AHP provides a way to arrive at a meaningful set of weights, the process requires a large number of comparisons to be made by experts. The initial reaction of some of these experts was that they are unwilling to go through this process.

In the event that no available technologies match the solution specified, the ODSS can match the specified solution to technologies currently being developed. Technologies currently being developed can come from four sources: 1 R&D projectsŽ . within EM, 2 industry development, 3 basic sci-Ž . Ž . ence, or 4 other programs, and are ranked using theŽ . technology suitability function in Eq. 1 . In the Ž . event that there are no available technologies or technologies under development that match the desired solution for a contamination problem, the problem and its specified solution are classified as an unmet requirement.

![](/api/attachments/77UV2NPY/fulltext/images/3aa47b0339e0a9e15746ceb3e29e9dbcbaa7df92ec41f5b476218e460ee40508.jpg)  
Fig. 3. The EM50-ODSS decision model and the related decision processes.

The outputs from the project manager’s decision making process serve as inputs for other users of the ODSS. When solutions are matched to technologies under development, the rankings of these technologies for fund allocation purposes are changed. An investment suitability function ISF is used to rank Ž . the various technology developments within the four technology investment portfolios, as shown in Eq. Ž . 2 below. These rankings are used along with other criteria from the technology investment decision model to allocate funds within the portfolios. Focus area teams, which include staff from EM’s waste management, technology deployment and environmental restoration programs 15 , review the tech-<sup>w</sup> <sup>x</sup> nologies under development within their area and use these rankings in deciding how to allocate R&D funds among these technologies.

$$
\begin{array}{r l} \mathrm{ISF} _ {\mathrm{t}} & = \sum w _ {\mathrm{c}} (\text { Cost\_val }) _ {\mathrm{t}} + w _ {\mathrm{e}} (\text { Env\_prot\_val }) _ {\mathrm{t}} \\ & + w _ {\mathrm{p}} (\text { Pub\_health\_val }) _ {\mathrm{t}} \\ & + w _ {\mathrm{r}} (\text { Reg\_compl\_val }) _ {\mathrm{t}} \\ & + w _ {\mathrm{w}} (\text { Work\_Health\_saf\_val }) _ {\mathrm{t}} \end{array}\tag{2}
$$

Outputs from the project manager’s decision making process also serve as inputs to another focus area team’s decision making process. When specified so lutions are not matched to either available technologies or technologies under development, they become classified as unmet requirements. These unmet needs must be addressed for EM to achieve its mandate of cleaning up all contaminated sites within 30 years. Focus area teams use the ODSS to identify any unmet needs within their portfolio. The ODSS can also assist the teams in identifying sources to develop these technologies. Information on similar or related technologies developed by all types of sources is stored in the ODSS and can be retrieved based upon features in common with the specified solution.

A secondary objective of the EM50-ODSS was to provide decision-making support to constituents external to the EM organization: 1 EM’s partners inŽ . industry, science, and academics, 2 DOE adminis-Ž . trators, and 3 EM’s public stakeholders. EM’s part-Ž . ners in industry, science, and academics need access to the breadth of knowledge that encompasses EM’s mandate for restoration and need support for selecting technology contracts and researching new technologies. In addition, these partners are often sources for new knowledge to be stored in the ODSS. DOE administrators need access to the system and its decision support capabilities to evaluate the individual activities of EM and the overall effectiveness of the organization. Lastly, EM’s public stakeholders, the general public and congress, need access to the system to review the restoration status of the various contaminated sites all over the country.

## 5. Data model

In performing the requirements analysis for the system, we noted an unusual level of complexity in modeling the data requirements. Because EM was a relatively new organization, the data within the scope of the ODSS was distributed among numerous branches of the DOE, consultants, external contractors and universities. For example, the contamination problems for the subsurface contaminants focus area Ž . SCFA came from one source in an electronic format. This source had compiled the information from several other sources. The information on available technologies came from an independent source external to DOE. The technology requirements came from multiple sources, while basic science research came from another source external to DOE. Additionally, because the decision processes being modeled and supported within the ODSS were new and not established procedures, the relationships between the data entities were more difficult to determine.

The entity-relationship ER diagram shown inŽ . Fig. 4 depicts the data model for the ODSS. The diamonds shown on each line connecting the entities

![](/api/attachments/77UV2NPY/fulltext/images/fa33875891436e80c1493a7ebb13b83db68ecd16d44f84499cba179d514a9502.jpg)  
Fig. 4. The entity-relationship ER diagram for the EM50-ODSS.Ž .

in Fig. 4 represent relationships and are generally many-to-many relationships. The data entity, Problem, describes all of the contamination problems that have been identified by DOE sites. These problems can be categorized by their Contaminant and Hydrogeology characteristics as shown by these two data entities. Problems are addressed by a solution strategy which is represented by the Solution entity. The solutions can be addressed by pre-defined Technology Requirement Categories. These categories are described in more detail by the Tech\_reqmt\_description entity. The technology requirement categories are either met by available Industrial Technologies, or they result in Technology Gaps that need to be addressed. Technology gaps are addressed by DOE Projects, Industrial DeÕelopment Projects, Basic Science Projects, Other Programs, or are not addressed currently by any program and represent the Unmet Requirements entity. DOE projects result in Technology Task Plans TTPs , information regard-Ž . ing which is also included in the system. DOE projects also have yearly funding information related to it, as indicated by the entity Funding Year. The different R & D projects are assessed periodically during development by defined gate criteria 15<sup>w</sup> <sup>x</sup> from the technology investment decision model and are thus related to the entity, Gate-criteria.

Prior to implementation, the data was normalized to obtain a relational model. The relations were in Boyce–Codd Normal Form. The relational model yielded 36 relations which were set up as tables within a DBMS.

## 6. Implementation

The implementation plan for the EM50-ODSS consisted of two phases. In the first phase, the database and the portion of the system accessible from within EM were built. A fully functional prototype was implemented in Microsoft Access and Visual Basic for the first phase of the implementation due to the EM personnel’s familiarity with the application environment. The second phase of the implementation entailed upgrading the database to one that would support a distributed architecture and building the portions of the system accessible to users external to the EM. Computer-supported coordination technologies, including conferencing, could be included in the second phase to support communication in the ODSS’s distributed environment. The first phase of the implementation was completed and is described below.

The primary purpose of the EM50-ODSS was to assist various users in the DOE complex to assess the technologies being built or available to address contamination problems. Consequently, in developing the model for the EM50-ODSS we focused on two issues. We first identified problems and technologies related to waste management that existed in the DOE environment. The second issue dealt with the identification of internal and external entities that were involved in developing appropriate technologies related to waste management. This resulted in broadly classifying the entities into the following five categories.

Ž . 1 Problems: Contamination problems are recorded and reported from different DOE sites. These problems are broadly classified by field offices, installations, focus areas, and product lines. The overall objective of the EM50-ODSS is to address these problems through various technology development projects. As a preliminary step in achieving this objective, the EM50-ODSS integrates diverse data sources and builds and supports an enterprise wide data model.

Ž . 2 Available Technologies: Technologies that exist in industry today that may be able to address DOE’s waste problems are recorded. This information is collected by DOE, their contractors, consultants, etc. One of the objectives of the system is to catalog these technologies and attempt to match available technologies with waste problems.

Ž . 3 Technology Requirements: DOE analysts describe problems using a classification scheme that helps characterize problems in terms of technology requirements. These technology requirement categories are the road maps for technology development and are at the heart of the system, driving all potential technology development. Fig. 5 shows a sample of the technology requirement categories in the system.

Ž . 4 Gaps<sup>r</sup>Work Packages: Technology requirements are brought to fruition by developmental projects. When technology requirements have no associated developmental projects, gaps in technology development arise. These gaps result in unmet requirements that often have to be pursued aggressively depending upon predetermined priorities. A work package is a description of the unmet requirements and what needs to be done to remedy the situation.

<table><tr><td>Technology Reqmt. ID</td><td>Technology Requirement Category</td></tr><tr><td>3.1</td><td>Assessment</td></tr><tr><td>3.1.1</td><td>Subsurface Assessment</td></tr><tr><td>3.1.1.1</td><td>Hydrology</td></tr><tr><td>3.1.1.2</td><td>Geophysical</td></tr><tr><td>3.1.1.2.1</td><td>Subsurface Imaging</td></tr><tr><td>3.1.1.2.2</td><td>Surveying Techniques</td></tr><tr><td>3.1.1.2.3</td><td>Other Geophysical</td></tr><tr><td>3.1.1.3</td><td>Soil Characteristics</td></tr><tr><td>3.1.1.3.1</td><td>Lysimeters</td></tr><tr><td>3.1.1.3.2</td><td>Subsurface Imaging</td></tr><tr><td>3.1.1.3.3</td><td>Other soil characteristics measurements</td></tr><tr><td>3.1.10</td><td>Assessment-Other</td></tr><tr><td>3.1.2</td><td>Intrusive sampling/Buried objects</td></tr><tr><td>3.1.2.1</td><td>Ground penetrating radar</td></tr><tr><td>3.1.2.2</td><td>Other Electromagnetic</td></tr><tr><td>3.1.2.3</td><td>Radiological detection</td></tr><tr><td>3.1.3</td><td>Risk/Performance assessment</td></tr><tr><td>3.1.4</td><td>Monitoring</td></tr><tr><td>3.1.4.1</td><td>Dig-face</td></tr><tr><td>3.1.4.2</td><td>Assay/Stabilization</td></tr><tr><td>3.1.4.3</td><td>Air Monitoring</td></tr><tr><td>3.1.4.3.1</td><td>Organics</td></tr><tr><td>3.1.4.3.2</td><td>Radionuclides</td></tr><tr><td>3.1.4.3.3</td><td>Radiation</td></tr><tr><td>3.1.4.4</td><td>Geoprobes</td></tr><tr><td>3.1.4.5</td><td>Penetrometers</td></tr><tr><td>3.1.4.6</td><td>Assessment/Monitoring - Other</td></tr><tr><td>3.1.5</td><td>Metal,Radionuclide contamination assessment/characterization</td></tr><tr><td>3.1.6</td><td>DNAPL contamination assessment/characterization</td></tr><tr><td>3.1.6.1</td><td>Groundwater</td></tr><tr><td>3.1.6.2</td><td>Vadose zone</td></tr><tr><td>3.1.6.3</td><td>Fracture zones</td></tr></table>

Fig. 5. A sample of technology requirements in the EM50-ODSS.

Ž . 5 Projects: Projects in the DOE system are undertaken by different types of organizations, some internal and some external. Each focus area in the DOE system has its own projects called focus area projects. These projects are usually internally managed and monitored by the DOE complex. Some projects are related to basic scientific research. These are usually conducted at universities and national research laboratories. These projects are called basic science projects. Another category of projects is contracted out by the DOE to industry. These projects are called industrial programs. All of these projects, taken together, address DOE’s technology requirements.

## 6.1. User interface

The EM50-ODSS was designed for users with different decision making needs. The users are able to select their area of interest through sub-menus as shown in Fig. 6. The general categories of problems, technology requirements, available technologies, gaps<sup>r</sup>work packages and projects are the system entry points available to a user.

Some of the categories i.e., entities listed above,Ž . such as problems, have complex semantics. User interfaces that describe problems and other entities are designed in a modular fashion to provide ease of use as shown in Fig. 7. For example, detailed information regarding problems, like priorities, contacts, etc., can be displayed on other screens by drilling down through the problem interface. This modular approach to screen design was adopted for all primary entity screens: problems, available technologies, projects, gaps<sup>r</sup>work packages, and technology requirements.

![](/api/attachments/77UV2NPY/fulltext/images/cb7eb7817de89d33e43d0a5ca7c0b5bd8907d17aee0ba05319c1693089143ed6.jpg)  
Fig. 6. Decision support capabilities in EM50-ODSS.

## 6.2. Decision support capabilities

The decision support capabilities of the system are broadly divided into two categories, queries and decision support reports, as shown in Fig. 6. The queries module allows ad-hoc retrieval of information, whereas, the decision support reports module contains pre-defined reports geared towards specific decision-making tasks. All information stored in the system can be obtained using the Queries module if the user has been given the appropriate access.

## 6.2.1. Queries module

Users can retrieve information in several ways in the Queries module. Some examples of how information can be retrieved using the Queries module are listed below:

<sup>Ø</sup> Browse through all Problems, Technologies, Projects, etc. stored in the system.

<sup>Ø</sup> Retrieve Problems related to a certain focus area using filters. The use of filters allows a user to look at selected sets of the data.

<sup>Ø</sup> When a user is looking at a Problem, or a Technology Requirement, etc., the user can link to other parts of the database and retrieve information.

<sup>Ø</sup> Depending on what the user is looking at, context sensitive reports can be viewed or printed when using the Queries module.

The Queries module allows the user to select Problems, Technology Requirements, AÕailable Technologies, Gaps<sup>r</sup>Work Packages, or Projects as the starting point for information retrieval. Having selected one of these initial categories, filters may be used to narrow the search.

Filters are a critical component of the ODSS. These filters allow the user to create SQL queries that can be executed by the system to retrieve information without having to formulate the SQL themselves. Without the use of filter screens, formulation of complex queries would become an arduous task for the user. An example of a Technology Requirements filter is shown in Fig. 8, while the results are shown in Fig. 9.

![](/api/attachments/77UV2NPY/fulltext/images/ee2d876b1d0d56bfe4c746be14c21b1eefad0994b0b98d5577d2224a95b49bcf.jpg)  
Fig. 7. A problem data screen.

After having utilized various filters, the user arrives at the data screen that is desired, e.g., a particular problem, a particular available technology, a particular focus area project, etc. As shown in Fig. 7, the data screen includes a Link button. Links allow the user to link to any part of the database from the screen currently being displayed. For instance, if the user is looking at a problem in Rocky Flats, and wants to see if there are any aÕailable technologies linked with this problem, the user can click on the links button on this problem screen and choose the option AÕailable Technologies on the drop-down list of link options. This will take the user to any linked available technologies. Similarly, the user could go to any Focus Area Projects, Gaps<sup>r</sup>Work Packages, Technology Requirements, etc., linked with the problem currently being displayed on the screen. An example of the link options drop-down screen is shown in Fig. 10.

## 6.2.2. Decision support reports

This module supports the decision-making tasks for which the system was intended. The Decision Support Reports module allows the user to generate a number of reports from the database system in pre-defined formats. The primary purpose of these reports is to support decision-making concerning investments in technology development projects. The reports provide information related to matching problems to different components of the database, including available technologies, gaps, projects, unmet requirements, etc. The reports also assist the user in prioritizing projects with respect to different gaps being addressed.

![](/api/attachments/77UV2NPY/fulltext/images/ce57a9a73f52a092cbb53fa3300ce98ee5851115ab8aca1bfe63859191e84dba.jpg)  
Fig. 8. A technology requirements filter in the EM50-ODSS.

The interface for the Decision Support Reports module Fig. 11 allows the user to navigate aroundŽ . the report generating facility of the system. The user may choose from several general reports shown on the initial Decision Support Reports screen, or select more detailed reports, including gate criteria reports, contaminant<sup>r</sup>hydrogeology reports, etc. One such report, Gap<sup>r</sup>Work Packages and Projects by Prob lem, is shown in Fig. 12.

![](/api/attachments/77UV2NPY/fulltext/images/90f7293f9d7fc68fdecfece27c1408eec9c78cf3db890e07ab9e3c11791a6f40.jpg)  
Fig. 9. The results of a technology requirements filter.

![](/api/attachments/77UV2NPY/fulltext/images/6cb5f18cf09b69e8883322d12aeaeb558bc1caaa5864d91ddb62cb6b112d56a7.jpg)  
Fig. 10. An example of the links option drop-down box.

![](/api/attachments/77UV2NPY/fulltext/images/7388d2aa8ef9a0662bc7e61dfdf6a8a1db97965ac1258cb1c618433a38bf6263.jpg)  
Fig. 11. The menu for the Decision Support Reports sub-menu item.

## 6.3. Organizational decision support

Organizational decision support is provided through both the query and report modules of the system due to the variety of users with different decision-making tasks that are supported by the system. The standardized reports provided by the system demonstrate another aspect of organizational decision support. The content of these reports depicts the status of the overall organizational goal as it cuts across the functional units of EM. A view of the corporate decision model and processes supported by the system was provided in Fig. 3. The reports generated address the EM-50’s contamination problem assessment and strategic solution approaches. These reports provide the following information that is currently not available in an integrated fashion using the current systems of the DOE:

<sup>Ø</sup> contamination problems, their innovative solution approaches, and corresponding technology requirements for each field office.

<sup>Ø</sup> contamination problems, their corresponding technology requirements, and gap<sup>r</sup>work packages for each field office.

<sup>Ø</sup> technology requirements and available technologies for each problem.

<sup>Ø</sup> gaps<sup>r</sup>work packages and their corresponding focus area projects for each problem.

<sup>Ø</sup> projects currently addressing each gap<sup>r</sup>work package.

![](/api/attachments/77UV2NPY/fulltext/images/d28ee34baa40f5ae64b1d46eb5ebeb9047c09ac58444a6bc4a4402bd3c587627.jpg)  
Fig. 12. Example report generated from EM50-ODSS.

<sup>Ø</sup> gaps<sup>r</sup>work packages not being addressed currently.

## 6.3.1. Decision-making related to gate criteria

Gate-criteria are used to indicate stages of technology development related to environmental cleanup. Some examples of these stages are feasibility study, design, testing, etc. For the technology investment program, obtaining gate criteria progress on projects for which EM-50 technology investments have been made is critical for making future investment decisions. The EM-50 DSS can provide decision support information related to:

<sup>Ø</sup> gate criteria passed for each project basic sci- Ž ence, industry, focus area and other programs that is addressing a particular gap<sup>r</sup>work package ..

<sup>Ø</sup> gate criteria passed by each focus-area project.

<sup>Ø</sup> gate criteria passed and technology requirements addressed by each available technology.

## 6.3.2. Decision support related to matching hydrogeology and contaminants

Classifying problems and technologies by contaminant category and their hydrogeologic characteristics is very important for decision-makers attempting to match problems to available technologies. These reports help in the attempt to automate some of the matching process so that users do not toil with vast amounts of information. However, for this component of the decision support to be successful, rule-based information from experts is required. These are then organized in relational form and input into the system. This can be accomplished by breaking up ‘‘if–then’’ rules and classifying them as premises and conclusions. These can then be input into relational tables and operated upon by inference engines that are designed to work on them. For an example of this approach, see Ref. 1 . The following<sup>w</sup> <sup>x</sup> decision support capabilities can be obtained from this sub-system.

<sup>Ø</sup> problems and available technologies matched on the basis of contaminants and hydrogeologies.

<sup>Ø</sup> problems for a specific contaminant or hydrogeologic characteristic

<sup>Ø</sup> technologies for a specific contaminant or hydrogeologic characteristic.

## 6.3.3. Prioritization support:

This subsystem is a very critical aspect of the ODSS as it helps the decision-maker to prioritize investment in technology. The prioritizations, however, need to be developed with caution. Prioritization criteria are debatable and expert opinions on the criteria differ. Even, the most appropriate models developed can lack consensual support. Several prioritization reports based on multi-attribute utility Ž . MAU models were developed and implemented within the subsystem. MAU models were suggested, as they are simple to use and understand. They allow diverse information with different degrees of importance to be combined to together to prioritize alternatives 18 .<sup>w</sup> <sup>x</sup>

One of the problems in using the MAU models was the determination of the weights for the parameters involved. A suggested methodology for the determination of these weights is the Analytic Hierarchy Process AHP 19 . The use of AHP required Ž . <sup>w</sup> <sup>x</sup> several hundred comparisons of the decision parameters involved in arriving at the weights. Given the time constraints of the project, it was considered impractical to incorporate the MAU model as a part of the DSS at this time. It was left for future inclusion in the system.

## 7. Conclusion

An ODSS was designed and a prototype was implemented to support various decision-making functions within the DOE’s Office of Environmental Restoration and Waste Management and to support the external decision-making tasks of EM partners. The prototype was developed as a preliminary step towards achieving the following: 1 automated ac- Ž . cess to data previously distributed over numerous divisions and organizations, 2 design and supportŽ . for an enterprise-wide data model, 3 matching of Ž . technology needs to available resources, 4 identifi-Ž . cation of unmet technology needs, 5 monitoring ofŽ . ongoing technology development and 6 support forŽ . the allocation of investments in technology development. The domain of hazardous waste cleanup provided an ideal problem space for the deployment of an ODSS due to the need for integration of the decision-making tasks across various functional areas.

The web-based version of the system represents an ODSS that supports a virtual organization. The DOE-EM and the many outside organizations and research groups involved in hazard waste resolution form a virtual organization with unique integration and collaboration requirements. Virtual organizations are formed when different companies pool available resources to produce or develop a product or project. This form of inter-organization collaboration is not often found in industry, whereas other forms of inter-organization associations, such as outsourcing, are common. Thus, an ODSS implementation in a virtual organization, such as DOE-EM, provides a unique research opportunity.

This paper advanced the study of ODSS by providing both theoretical and applied contributions. An ODSS taxonomy of organizational strategies and technologies, initially set forth by George et al. 8 in<sup>w</sup> <sup>x</sup> 1992, was extended to accommodate inter-organizational integration, artificial intelligence and distributed architectures. Additional theoretical contributions include an analysis of the prototype system in terms of Holsapple and Whinston’s 10 MDSS<sup>w</sup> <sup>x</sup> architecture. From an applied perspective, the EM50-ODSS represents one of the few documented examples of ODSS. The EM50-ODSS is differentiated from previously documented ODSS by the complexity and inter-related decision activities of the system’s decision model and the organizational diversity of the system’s intended users.

Future research opportunities specific to the EM50-ODSS include the development of prioritization criteria for ranking purposes. The development of such prioritization criteria for the purpose of ranking investments in waste resolution technology is a very complex process. Obtaining a group consensus on the criteria developed proved to be extremely difficult. Future efforts to enhance the development and collection of such criteria could include transferring this technology to a distributed architecture with web interfaces and using a form of distributed GSS. A distributed GSS could provide the means to collect the necessary information and opinions from experts in different geographic locations and provide decision-making support to help drive the group to some agreement. More advanced prioritization methods such as AHP could potentially be implemented in such an environment.

One limitation of this paper is that it describes a prototype system and does not provide any insight on actual ODSS usage. Most documented ODSS examples have been similarly limited, and there has been very little published research on this topic. Future research that analyzes ODSS usage in terms of the Information System Success Model components system and information quality, information Ž use, user satisfaction, individual and organizational impact 2 is needed. The widespread adoption of. <sup>w</sup> <sup>x</sup> Enterprise Resource Planning ERP systems thatŽ . support inter-departmental decision-making activities could provide an ideal environment for this avenue of research.

Additional research opportunities for ODSS in general, include research on gaining and maintaining stakeholder approval for such systems. A project of this magnitude requires significant investments in technology and human resources and serves a multitude of diverse users. While the benefits of such an investment clearly exist, retaining the needed support from all of the relevant stakeholders can be quite a challenge. In the current scenario, the lack of an integrated decision support environment that provides information critical to developing waste management technology hampers the technology management process that EM has been mandated to undertake. Selecting a systems development methodology that accommodates the number and diversity of potential users is extremely important in such an environment. Research that suggests a methodology or certain methodological features to employ would be of great benefit to organizations attempting to design and build ODSS.

## Acknowledgements

This work was supported by the Waste Policy Institute with a grant from the U.S. Department of Energy, Morgantown Energy Technology Center, through cooperative agreement number DE-FC21- 91MC29467 with West Virginia University Research

Corporation and by the ASPIRES grant awarded by Virginia Polytechnic Institute and State University.

The authors would like to thank an anonymous reviewer whose comments and suggestions signifi cantly strengthened this paper.

## References

<sup>w</sup> <sup>x</sup> 1 R. Blanning, A relational framework for join implementation in model management systems, Decision Support Systems 1 Ž . Ž . 1 1985 69–82.

<sup>w</sup> <sup>x</sup> 2 W.H. DeLone, E.R. McLean, Information systems success: the quest for the dependent variable, Information Systems Research 3 1 1992 60–95.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 G. DeSanctis, B. Gallupe, A foundation for the study of group decision support systems, Management Science 33 5Ž . Ž . 1987 589–609.

<sup>w</sup> <sup>x</sup> 4 Environmental Restoration and Waste Management EMŽ . Program: An Introduction DOEŽ . <sup>r</sup>EM-0013P , U.S. Department of Energy–Office of Environmental Restoration and Waste Management 1991 .Ž .

<sup>w</sup> <sup>x</sup> 5 Environmental Restoration and Waste Management Five-Year Plan: Fiscal Years 1994–1998, U.S. Department of Energy– Office of Environmental Restoration and Waste Management Ž . 1993 .

<sup>w</sup> <sup>x</sup> 6 J. Fedorowicz, B. Konsynki, Organization support systems: bridging business and decision processes, Journal of Management Information Systems 8 4 1992 5–22. Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 J.F. George, The conceptualization and development of organizational decision support systems, Journal of Management Information Systems 8 3 1992 109–125.Ž . Ž .

<sup>w</sup> <sup>x</sup>8 J.F. George, J.F. Nunamaker, J. Valacich, ODSS: information technology for organizational change, Decision Support Systems 8 1992 307–315.Ž .

<sup>w</sup> <sup>x</sup> 9 R.D. Hackathorn, P.G. Keen, Organizational strategies for personal computing in decision support systems, MIS Quarterly 5 3 1981 21–27.Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 C.W. Holsapple, A.B. Whinston, Decision Support Systems: A Knowledge-Based Approach, West Publishing, St. Paul, MN, 1996.

<sup>w</sup> <sup>x</sup> 11 G.P. Huber, The nature of organizational decision making and the design of decision support systems, MIS Quarterly 5 Ž . Ž . 2 1981 1–10.

<sup>w</sup> <sup>x</sup> 12 P.G.W. Keen, M.S. Scott Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, MA, 1978.

<sup>w</sup> <sup>x</sup> 13 Y. Kim, H. Kim, J. Yoon, H. Ryu, Building an organizational decision support system for Korea telecom: a process redesign approach, Decision Support Systems 19 1997 Ž . 255–269.

<sup>w</sup> <sup>x</sup> 14 J.F. Nunamaker, A.R. Dennis, J.S. Valacich, D.R. Vogel, J.F. George, Electronic meeting systems to support group work, Communications of the ACM 34 7 1991 40–61.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 J. Paladino, Managing Technology for Deployment, U.S. Department of Energy–Office of Environmental Management-Office of Technology Development.

<sup>w</sup> <sup>x</sup> 16 J. Paladino, P. Longsworth, Maximizing R&D Investments in the Department of Energy’s Environmental Clean-Up Program, U.S. Department of Energy–Office of Environmental Management–Office of Technology Development.

<sup>w</sup> <sup>x</sup> 17 A.S. Philippakis, G.I. Green, An architecture for organization-wide decision support systems, Proceedings of the Ninth International Conference on Information Systems 1988Ž . 257–263.

<sup>w</sup> <sup>x</sup> 18 H. Raiffa, Decision Analysis, Addison-Wesley, New York, NY, 1968.

<sup>w</sup> <sup>x</sup> 19 T. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, NY, 1980.

<sup>w</sup> <sup>x</sup> 20 R.H. Sprague, E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

Tarun K. Sen is Professor of Accounting and Information Systems and co-Director of the Systems Integration Center at Virginia Tech. He got his undergraduate degree in Mechanical Engineering from IIT Kanpur; M.B.A. from IIM Bangalore; and Ph.D. in Management Information Systems from The University of Iowa. His research areas include database management systems, business intelligence systems, design of graphical user interfaces, knowledge management systems using model bases, design and development of decision support systems, data warehousing, design of e-business systems, graphical model management systems and the application of neural networks in financial modeling. He is widely published in these areas and has been engaged in several consulting, research, and professional development programs. He has published several journal articles that have appeared in journals like Management Science, IEEE Transactions on Systems Man and Cybernetics, Omega, The INFORMS Journal on Computing, Decision Support Systems, The Journal of Information Systems, BehaÕior and Information Technology, International Journal of Intelligent Systems in Accounting Finance and Management, and others.

Laurence J. Moore is the Bell Atlantic-Virginia Professor of Management Science and Information Technology in the Pamplin College of Business at Virginia Tech. Dr. Moore has published over 50 papers in journals and proceedings, including such journals as Management Science, Decision Sciences, Operations Research, IIE Transactions, Journal of the Operational Research Society, Computers and Operations Research, International Journal of Production Research, and the European Journal of Operational Research. Dr. Moore is coauthor of several books including Management Science Ž1st, 2nd, 3rd, 4th edn., W.C. Brown, Allyn & Bacon, Prentice-Hall ;. Ž GERT Modeling and Simulation Petrocelli<sup>r</sup>Charter ; and . Introduction to Decision Science Ž . Petrocelli<sup>r</sup>Charter , as well as two books of Proceedings. Dr. Moore’s research has focused on the development of optimization models for multicriteria decision analysis, network simulation modeling, and decision support systems. Dr. Moore is a member of INFORMS and the Decision Sciences Institute.

Traci J. Hess is an assistant professor in the Department of Management Information Systems at the University of Central Florida. Her research interests include decision support systems and software agents, and she has published in Decision Sciences. She received her Ph.D. in Management Science and Information Technology and an M.A. in Accounting Information Systems at Virginia Polytechnic Institute and State University. She is a member of the Association for Information Systems, the Decision Sciences Institute, and INFORMS.
