---
otero_id: 8948
otero_key: "TQ3CWWKV"
title: "Requesting Distant Robotic Action: An Ontology for Naming and Action Identification for Planning on the Mars Exploration Rover Mission."
authors: "Roxana Wales; Valerie Shalin; Deborah Bass"
year: "2007"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00116"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 8 | Issue 2

Article 6

2-4-2007

# Requesting Distant Robotic Action: An Ontology for Naming and Action Identification for Planning on the Mars Exploration Rover Mission.

Roxana C. Wales

Valerie L. Shalin

Deborah S. Bass

Follow this and additional works at: https://aisel.aisnet.org/jais

# Journal of the Association for Information Systems JAIS

Requesting Distant Robotic Action: An Ontology for Naming and Action Identification for Planning on the Mars Exploration Rover Mission.

Roxana C. Wales
SAIC NASA Ames Research Center
rwales@google.com

Valerie L. Shalin
Wright State University

Deborah S. Bass
NASA Jet Propulsion Laboratory
California Institute of Technology

## Abstract:

This paper focuses on the development of a naming convention and the use of abbreviated names and a related ontology for science work and distant robotic action that comprise requests for a robotic rover during the NASA Mars Exploration Rover (MER) mission, run by the Jet Propulsion Laboratory (JPL). We demonstrate how abbreviated names and an associated ontology support sharing and identifying information among teams and software tools. An ontology of distant action must take into account a dynamic environment, changing in response to physical events and intentional actions, and reflect the influence of context on the meaning of action. The nascent domain of Martian tele-robotic science, in which specialists request work from a rover moving through a distant landscape, as well as the need to consider the interdisciplinary teams involved in completing that work, required an empirical approach. The formulation of this ontology used ethnographic methods and grounded theory to study human behavior and work practice with software tools.

Key Words: ethnography, grounded theory; domain model, work practice, distributed work, planning technology, knowledge elicitation.

<table><tr><td colspan="2">Requesting Distant Robotic Action: An Ontology for Naming and Action Identification for Planning on the Mars Exploration Rover Mission.</td></tr><tr><td colspan="2">IntroductionPeople frequently ask other people to do tasks that appear simple, yet, when analyzed, can be quite complex. A colleague says: “We need four copies of this,” and typically, other colleagues produce four copies of the document, because they understand the steps involved in copy-making. The success rate may change if the requests become more complex, e.g. asking for copies of multiple originals or making multiple requests concerning the same original. However, an abbreviated name will identify the task successfully, even though the execution is invariably more intricate than a simple one- sentence request implies.The success of such communication depends on the speaker and recipient having a set of shared concepts and concept labels. They must agree on the meaning of the relationship between copies and an original document as well as the word that labels this relation. Arriving at an agreement on the types of objects, attributes, and relations in a domain is challenging for a number of reasons. First, cooperating disciplines may define object classes differently. For example Bowker and Star (1999) describe differences in the taxonomy for diseases for early 20thcentury immigration officers and medical doctors, and even differences in the taxonomies across international immigration agencies. A second challenge lies in the evolution of domain knowledge, which at minimum will add distinctions over time. For instance, the numerous B vitamins started out as a single undifferentiated class until scientific work established specific functions and chemical structures for the various enumerated co-enzymes.The present paper concerns the relationship between domain models for humans and technology. In particular, we examine the models of geologists and their distant robotic extensions (rovers) operating on the surface of Mars during the 2003-2004 NASA Mars Exploration Rover (MER) mission, run by the Jet Propulsion Laboratory (JPL). Designers of technology recognize the domain model as a critical variable in software development, and the source of variability across programmers (Hadar and Soffer, 2006). Human Factors specialists know that the types of entities that technology incorporates can influence human comprehension of that technology. For example, in modern trajectory planning software for commercial aviation, discrepancies between a pilot’s stair-step model of descent including specific ground locations and a programmer’s curved model of descent challenges the pilot’s ability to understand and use this software (Degani and Weiner, 1997). We add the topic of ontology to the classification scheme for research on human interaction with information systems (Zhang and Li, 2005).Opportunities for mismatch between technology and human users are increasing as product lifecycle management and ubiquitous computing concerns rise. This paper focuses on the development of a naming convention that helped interdisciplinary teams identify tasks and collaborate on the development of science plans for MER rovers, i.e., computers that execute action in a physical environment. This domain involves high uncertainty, high variability, and time criticality, which correlate with the need for great flexibility (Gebauer and Schober, 2006). The naming convention is composed of two related constructs:Abbreviated namesrepresented the natural language referents used by scientists and engineers as they requested robotic action in the exploration of Mars.An emerging ontology for science work and distant robotic action created structure for the abbreviated names and carried information across different tools in the mission uplink process, ultimately mapping to the instrumentation system of the rovers.We present a case study on the development of a naming convention for requesting rover action on Mars. In devising a solution to a practical problem relative to the interaction between humans and technology, we encounter several domain properties that make our solution of theoretical relevance to the development of ontologies for computationally intensive work systems:The target user community had a high degree of participation in the design and testing of the rover technology. However, substantial engineering safety considerations dominated commanding, introducing the potential for discrepancy between the scientists’ and the rover’s models of action.</td></tr><tr><td colspan="2">Volume 8 Issue 2 Article 1</td></tr></table>

\- Robotic planetary surface exploration was a relatively nascent domain, lacking an established work practice to guide design and testing or initial execution. This required a flexible approach to constructing an ontology related to commanding.

\- Scientists and engineers needed semantics and labels not just for objects but also for higher-order work actions. This challenged the sufficiency of state changes alone to communicate the semantics of action (Georgeff and Lansky, 1986). It also required a representation of action at multiple levels of analysis (Sacerdoti, 1977).

\- The rover operated in and moved through a physical environment. This required external (extensional) semantics for action, more than the internal consistency and coherence that characterizes most attempts at ontology development.

While much contemporary work on ontologies focuses on computational search and pattern matching in a limited, symbolic domain (McGuinness, 2001), the role of context and human intention is critical for commanding robots in a dynamic world. Critics of computational linguistics (and computational models of mind) specifically note that natural language is contextualized (Dreyfus, 1979) and intentional (Searle, 2002), rather than an unambiguous, stand-alone construct for computational manipulation. In our case, the Martian environment provided this context, and the successful execution of intended action in that environment reflected the extensional semantics that grounds our ontology.

Consistent with the work of Carnap (1947) and Quine (1963), our use of the term “ontology” refers to the types of entities that exist, with a metaphysics (or explanation) of those entities in this domain emerging from the manner in which these entities map to the physical environment. A primary contribution of this paper lies in the ontology of action. Brachman (1979) identifies this sort of contribution as epistemological, as it offers examples of the types of entities involved. We make no claim to a complete inventory. While an inventory of individual primitives would provide a conceptual contribution, in the open-ended, context-dependent Martian domain, such an effort may be unattainable.

Because actions change the state of the world, differently ordered sequences of identically parameterized action can have different meanings. For example, moving the rover and then requesting a picture focused on a particular target results in a different image than does requesting a picture before driving. The mere passage of time also results in environmental changes (lighting), so that requesting a picture of a target at one time of day does not have the same outcome as an identical request at a different time of day. In this sense understanding/meaning equates to knowing how to perform an action that is dependent upon the context, with successful execution providing the ultimate evaluation. This feature of our domain distinguishes it from other domains with semantics based on symbolic relations. According to some philosophers (Dreyfus, 1979), the context sensitivity of named action, a characteristic of natural language, will not be explained solely by inter-relationships between symbols.

In established work domains, knowledge acquisition experts typically work with domain experts to translate existing knowledge into an ontology (Forsythe and Buchanan, 1989; Meyer, 1992; Noy and McGuiness). While the task of eliciting and formalizing important domain constructs and distinctions to create an ontology is never trivial, our research required another order of ontology development to accommodate the evolving expertise and the interdisciplinary nature of the work across both engineering and science.

This paper presents the empirical work supporting a grounded theory understanding of remote science work on Mars. Research to develop the naming convention took place over a three and a half year period covering the design and operations phases of the mission. The research resulted in five organizing principles for tele-science (e.g. remote planetary work or tele-medicine) or other remote, team-based work in dynamic environments. These principles can give structure to the development of a supporting ontology for the work.

1. Ontologies of work in information systems must contain both actions and objects to identify and represent all aspects of the work involved. The communication of work activities can be organized around a part-whole hierarchy, specifying high- and low-level action and high- and low-level objects.

2. Requests for science work are organized around higher order descriptors (what we call observations) that refer to and group the steps of the work. Identifiers for the work, consisting of abbreviated names and based on natural language, can facilitate information-sharing across teams.

3. An ontology of action must take into account a dynamic environment and reflect multiple concepts: changes in response to natural physical events, interactions with objects with their own changing state conditions, as well as constraints. It must reflect the influence of context on the meaning of intentional action.

4. In a dynamic environment, teams require semantics that are not just internally consistent within the software and can support action in a dynamic external environment, but can also adjust to users who are themselves changing, that is, learning, over time.

5. A set of formal, intentional, conceptual primitives is less relevant in our ontology because meaning goes beyond the intentional when executing action in a physical environment.

Similar to Schank (1975), our ontology distinguishes between objects (features and targets), actions (instrument and rover actions), and science work (observations and activities). The justification for these distinctions is the topic of this paper. In contrast to Schank, however, we elevate an essential part-whole relationship between types of objects. Rover objects (targets) become explicitly related to human scientists' objects (features). We only examine one facet of science work, called the observation, but elevate an essential part-whole relationship between observations and subordinate activities, which are more directly related to the rover's primitive actions. We also identify an entity called the plan, consisting of multiple observations. Figure 1 illustrates the resulting higher order components of the naming convention and the supporting ontology for MER science planning.

![](/api/attachments/TQ3CWWKV/fulltext/images/218ccca1ebd9acfbaae649774ed8e56ebc62ac0a51cd6f31baf208f82484883c.jpg)

Figure 1. The higher order components of the naming convention and supporting ontology for distant robotic action for MER.

We begin the paper with a description of our research method based on ethnography and grounded theory. The case study describes the MER mission planning and execution process; the analysis of the mission training and testing from which we derived a theoretical foundation for the naming convention and supporting ontology; and the results of the application of our theories drawn from the 2004 mission data itself.

## The Research Method

Consistent with the psychological literature (Behrend, 1995; Merriman and Tomasello, 1995), it was apparent that a standard, stable taxonomy would not address the need for an ontology of action, which requires a dynamic, flexible organization scheme. Only a participative and observational study in the domain could identify such a scheme. We participated in the formulation of the scheme in several ways. As researchers, we had to understand the work as it evolved from the earliest test and training exercises through surface operations on Mars. As mission participants, we had to identify, reflect on, and provide feedback on emerging constructs to the domain to support developing work and meet the demands of the mission timeline. The nascent domain and interdisciplinary nature of the work resulted in an empirical approach grounded in human behavior.

In the next section, we describe how we used ethnography and grounded theory to construct the emerging components of the naming convention.

## Ethnography and Human Centered Computing (HCC) at NASA

Ethnographic methods provide a number of data collection techniques that allow researchers to focus their attentions on a variety of social, cognitive, and technical perspectives that mirror the complexity of a domain (Bloomberg et al., 1993; Forsythe, 1999; Jordan, 1996; Nardi, 1996). Past ethnographic research has also focused on the elicitation of knowledge from existing situations of use (Forsythe and Buchanan, 1989; Meyer, 1992). NASA Ames researchers have used ethnographic methods since 1998 to understand scientific and technical work and do empirical requirements analysis for the development of new technology (Clancey, 2001, 2004; O'Neill and Wales, 1999; Shalin and McCraw, 2003; Shalin, 2005; Wales et al., 2001). Like action researchers (Lewin, 1946), Human Centered Computing (HCC) researchers work collaboratively with practitioners to solve problems through an iterative process including stages of in-situ data collection, analysis, and design. HCC research (including the present paper) assumes that all human activity is situated in a context (Suchman, 1987) and focuses on the cognitive and social systems, work practices, and technologies used in these activities. Our research followed the classic iterative cycles for qualitative research found in Spradley's (1980) ethnography - collecting data, creating an ethnographic record, analyzing and asking new questions - and in Lewin's (1946) action research - planning, acting, observing, and evaluating.

We came to call our work “mission ethnography,” because ethnographic data collection, analysis, assessment, and HCC recommendations had to be completed in time for tests and training sessions, software freeze dates, and landing dates without exception. Like the mission, we were on a timeline. Decisions would be made whether our recommendations were ready or not.

## Participant Observation and Development of a Grounded Theory

One of the authors was the MER Science Operations Systems Engineer and later the MER Deputy Science Team Chief. She had daily access and input to on-going mission design work. The other authors provided HCC work systems design recommendations and spent extended periods at JPL. We supported the design of science processes and trainings. Our tasks allowed us to act on our developing theories, feeding our findings into software design and processes in the years leading up to mission. Our team brought a cross-disciplinary perspective to the research, drawing on backgrounds in geology, systems engineering, cognitive science, and cultural psychology/anthropology.

Our recommendations were based on extensive observation and interaction with the target community during pre-mission events, tests, team meetings, and tele-cons. Our documentation included field notes and video-recordings. As badged members of the mission, we were able to move with flexibility, attending meetings and working with software designers. We presented and iterated on the developing naming convention, abbreviated names, and ontology with the science team. We helped train the team in the use of the ontological convention during the science team training “flight schools.”

Our analysis reflects a grounded theory approach. Grounded theory is “the discovery of theory from data systematically obtained from social research” (Glaser and Strauss, 1967, p.2) in which “the emerging theory points to the next steps” in the research as the work attempts to fill gaps in the theory and “answer research questions suggested by previous answers” (p.47). Our goal was to identify consistent conceptual and software representations that would support mission personnel in referencing and identifying distant robotic work.

To develop the grounded theory for the naming convention, we analyzed field notes, mission design documentation, and data from the science planning tool (SAP). We analyzed scholarly articles, communication exchanges, scientists' work practices and their scientific reasoning. We also assessed the software requirements and interfaces among mission technologies to address software needs, while supporting the work of the science team. After each test, we analyzed the data from the science planning tool (SAP) as well as from field notes, seeking cognitive, linguistic, and referential patterns to inform the theory.

![](/api/attachments/TQ3CWWKV/fulltext/images/930761cb21af2bf2c13270bd1e17e2a6032b6f8cb4cbdf2af70c7c2997db63a7.jpg)

During the mission, we took field notes, made video tapes of meetings and collected copies of planning print outs. Further, the mission planning and commanding process resulted in an accessible electronic record of work. This paper provides a qualitative analysis of those data.

The Case Study

The Case Study contains three major subsections:

\- The first section describes MER mission work in general and the use of a naming convention that is, in part, the product of our recommendations.

\- The second section describes the pre-mission collaborative research period (2001 -2003) during which we participated and worked with scientists and engineers in designing a surface operations process. In this period, we applied grounded theory to the problem of defining a naming convention and developing abbreviated names, and the related ontology.

\- The third section describes results from a period of mission surface operations (2004) as the scientists used the abbreviated names and ontology.

## MER Mission: Work Systems for the Tele-Robotic Exploration of Mars

This section covers the work of the mission participants during surface operations on Mars, including preliminary planning, planning tools, science plan integration, and the associated planning software in the ground data system. This post hoc description provides an implicit declaration of the ontology we articulate later in this paper. Several contextual factors influenced the MER work system. Unlike most space exploration missions, the sequence of actions to be executed depended on the results of immediately prior action, and therefore could not be specified in advance. This feature alone suggested the need for a highly flexible commanding process. In addition, scientists largely designed the instruments that the rover carried, based on bench-top instrumentation and previous space craft experience. However, the complete suite of tools does not exist in a single laboratory, so these scientists had little experience in the coordinated use of these instruments. In addition, there were limited opportunities to use the instrument suite outside the laboratory in field science. The result was limited understanding of how to guide the intended tele-robotic work practice for Martian science, emphasizing the need for flexibility.

While MER was a science-motivated mission, spacecraft health and safety were always a primary constraint in commanding. All conditional reasoning and decision making remained in the hands of human controllers, who translated requests for rover, action into a command language based on rover internal states. After controllers assessed the current state of the rover, commands operated rover devices or moved the rover but could not reference rover states in relation to the external environment. However, science focuses on the environment being explored as well as on the orientation and use of a device (e.g., that the robotic arm is touching a rock). One advantage of low level rover-state command language is that it provides maximal flexibility to construct virtually any unanticipated sequence of activities for orientation and rover use. Our ontology for tele-robotic action, however, bridges the external environment and the command-level internal states of the rover. This allows the rover to behave in a manner consistent with the external ontology even though that ontology is never represented in the rover itself. It compensates for the absence of an internal rover ontology for environmental objects, such as a rock. Further, because engineers, not scientists, are ultimately responsible for commanding the rover, the ontology allows scientists to articulate their requests to them in a consistent fashion including information about both the internal world of the rover (instrument, calibrations) and external objects (rocks).

The section below describes the MER mission process for developing science activity plans, which are requests for robotic action and are made up of lower level observations that contain subsets of activities. We suggest that the abbreviated names for these observations provide coherence across all planning phases.

## MER Science Planning Process

Each operational Martian day, called a “sol” (approximately 24 hrs and 39 min), the Science Team convenes in specialty-based Theme Groups to discuss the newly arriving data and decide what to plan for the next sol. Planning was complicated by thirteen available instruments located on three different parts of the rover: the rover’s body, mast, and robotic arm. [See Table A1. in the Appendix].

![](/api/attachments/TQ3CWWKV/fulltext/images/4ea247ba481484d2a756b5d07a9ad657cf81bc26e3045118a36cc95904926905.jpg)

In the first meeting of the sol, called the Science Context Meeting, scientists rough out a plan for the work of the rover based on the previous sol's rover work and updated information. Theme Groups then suggest and receive assignments for observation development. For example, the Soils and Physical Properties Group might develop an observation to examine the detailed morphology of a particular patch of soil. Later, the science team re-convenes to make adjustments to the plan, and then groups and individuals rework observations considering:

\- The type of sol being planned (e.g., traverse, approach towards a rock).

• The available resources (e.g., power, operating time)

\- Possible timing restrictions on when observations can take place.

\- Related events that will influence the observation (e.g., a communication event for data transmission)

• Engineering restrictions on the upcoming sol that will impact observations.

\- Options for reducing resource use by a particular observation (e.g., specifying adjustable parameter values)

Scientists use a naming convention and ontology to name the observation and convey appropriate information to other scientists as well as to other teams in the downstream planning process. For example, the science team might generate an observation to examine changes in the amount of registered sunlight over the course of a Martian sol. To accomplish this, the Pancam cameras will image the sun using solar filters at various times of day, to examine trends in atmospheric dust loading. The group names this observation Pancam\_Tau\_Anytime. "Pancam" refers to the instrument; "Tau" refers to the method of data collection and the analysis that will follow. "Anytime" indicates when the observation can be conducted.

As scientists used the instruments, it was clear that different kinds of use required different naming requirements, and the work itself suggested the names. Remote sensing instruments on the mast (those that gather images, spectroscopy data, etc. from locations distant from the rover) might specify work in a direction relative to the rover. An observation name such as Post-drive\_Navcam\_360 names a request for rover action using the nav (navigation) camera in a 360-degree circle around the rover at the end of a drive. Such an action does not require a feature as a focal point. Alternatively, an in-situ measurement (data collected by direct or close contact with a rover arm instrument on an object) might specify work on a particular object. For example, an in-situ measurement might be named Post-MB\_MI\_5position\_EICapitan, requesting the use of the MI (Microscopic Imager) camera to acquire five pictures on the rock El Capitan after the MB (Mössbauer) instrument has completed its measurement. As these examples illustrate, the classification of instruments determines the parameters that an action request requires. Elevating such classifications to standardize work practice was a major part of our contribution.

## MER Tools for Creating Science Observations

The science and engineering mission team was also responsible for translating observations into a language for programming the rover, with all of the correct parameterizations. Time was a precious resource in the mission. Failure to approve and command an activity plan in time to meet the Deep Space Network's transmission window meant the loss of a day's science. The need for agreed upon meanings in names and for the salient and consistent specifications of information as it flowed through different software applications was essential to mission success.

To facilitate the translation of purposeful action into rover language, the mission team used a series of software tools that translated the requests into several different representations. At the front end of the process, the science team used the Science Activity Planner (SAP) (Norris et al., 2005) software (Figure 2. and 3.)

<table><tr><td colspan="7">Observations Targets</td></tr><tr><td colspan="7">sol/054/post/bct/sci/sowg/sol_054_sowg_science_plan-merged.rml [sol-054]</td></tr><tr><td></td><td>Name</td><td>Uplink Priority</td><td>Duration (s)</td><td>Energy (Yt - h)</td><td>Critical Qdits</td><td>Purpose</td></tr><tr><td>Observation</td><td>PreDrive_Mudpie_IDD_work(Phys)</td><td>0</td><td>1,716.75</td><td>22.48</td><td>43,264.00</td><td>Part of our crater traverse systematic soil sur</td></tr><tr><td>SOE_NOTE</td><td>MB_Contract_Soil</td><td>0</td><td>0.00</td><td>0.00</td><td>0.00</td><td>to sense the location of the surface</td></tr><tr><td>APXS</td><td>short_APXS_Coconut</td><td>0</td><td>50.00</td><td>2.16</td><td>0.00</td><td>short integration on Coconut for information o</td></tr><tr><td>HAZCAM_FRONT</td><td>Verify_APXS_Position</td><td>0</td><td>57.22</td><td>0.18</td><td>10,816.00</td><td>Full frame stereo Hazcam capturing IDD work</td></tr><tr><td>MB</td><td>short_MB_Coconut</td><td>0</td><td>215.00</td><td>7.78</td><td>0.00</td><td>short integration on Coconut for mineralogical</td></tr><tr><td>HAZCAM_FRONT</td><td>Verify_MB_Position</td><td>0</td><td>57.22</td><td>0.18</td><td>10,816.00</td><td>Full frame stereo Hazcam capturing IDD work</td></tr><tr><td>MI</td><td>3pos_3bpp_Coconut</td><td>1</td><td>365.33</td><td>3.50</td><td>0.00</td><td>imaging of soils for grain morphology of the t</td></tr><tr><td>HAZCAM_FRONT</td><td>Verify_MI_Position_1</td><td>1</td><td>57.22</td><td>0.18</td><td>10,816.00</td><td>Full frame stereo Hazcam capturing IDD work</td></tr><tr><td>MI</td><td>5pos_3bpp_ChocolateChip</td><td>0</td><td>507.56</td><td>4.86</td><td>0.00</td><td>imaging of soils for grain morphology</td></tr><tr><td>HAZCAM_FRONT</td><td>Verify_MI_Position_2</td><td>0</td><td>57.22</td><td>0.18</td><td>10,816.00</td><td>Full frame stereo Hazcam capturing IDD work</td></tr><tr><td>IDD_STOW</td><td>STOW_IDD</td><td>0</td><td>300.00</td><td>2.71</td><td>0.00</td><td>stow IDD prior to drive</td></tr><tr><td>APXS</td><td>Load_5min_cycle_parameters</td><td>0</td><td>50.00</td><td>0.76</td><td>0.00</td><td></td></tr><tr><td>Observation</td><td>Pancam_ripple_mosaic (chem)</td><td>0</td><td>385.85</td><td>2.14</td><td>43,264.00</td><td>obtain red stereo mosaic of ripple field near</td></tr><tr><td>PANCAM_MOSAIC</td><td>Pancam_ripple_redmosaic_L2R2</td><td>0</td><td>294.63</td><td>1.63</td><td>32,448.00</td><td></td></tr><tr><td>PANCAM_SINGLE_POSITION</td><td>Pancam_ripple_cal_target_L2R2</td><td>0</td><td>91.22</td><td>0.51</td><td>10,816.00</td><td></td></tr><tr><td>Observation</td><td>Pancam_Mudpie_13F_Full_Frame (chem)</td><td>0</td><td>959.31</td><td>5.32</td><td>151,424.00</td><td>Pancam of Mudpie MI target; to be taken from</td></tr><tr><td>PANCAM_SINGLE_POSITION</td><td>Pancam_chocolatechip_quarter_L234567Rail</td><td>0</td><td>434.05</td><td>2.41</td><td>70,304.00</td><td></td></tr><tr><td>PANCAM_SINGLE_POSITION</td><td>Pancam_ripple_cal_target_L2R2</td><td>0</td><td>91.22</td><td>0.51</td><td>10,816.00</td><td></td></tr><tr><td>PANCAM_SINGLE_POSITION</td><td>Pancam_chocolatechip_cal_target_L234567Rail</td><td>0</td><td>434.05</td><td>2.41</td><td>70,304.00</td><td>13 filters, subframed for sweep magnet</td></tr><tr><td>Observation</td><td>Bounce_Drag Mark RemGen (chem)</td><td>2</td><td>1,220.10</td><td>6.57</td><td>140,608.00</td><td>Remote Sensing of smush and bounce marks</td></tr><tr><td>PANCAM_SINGLE_POSITION</td><td>Pancam_BounceDrag_quarter_L234567Rail</td><td>0</td><td>434.05</td><td>2.41</td><td>70,304.00</td><td>13-filter imaging of bounce and drag marks</td></tr><tr><td>PANCAM_SINGLE_POSITION</td><td>Pancam_BounceDrag_Caharger_L234567Rail</td><td>0</td><td>434.05</td><td>2.41</td><td>70,304.00</td><td></td></tr><tr><td>MTES_20_MRAD</td><td>MTES BounceDrag Raster</td><td>0</td><td>352.00</td><td>1.76</td><td>0.00</td><td></td></tr><tr><td>Observation</td><td>Drive Place Holder: backup from Mudpie (chem)</td><td>0</td><td>1,381.00</td><td>14.16</td><td>420,242.86</td><td>back up from Mudpie</td></tr><tr><td>ROVER_DRIVE</td><td>Back-up drive</td><td>0</td><td>1,381.00</td><td>14.16</td><td>420,242.86</td><td></td></tr><tr><td>Observation</td><td>Pancam_4F_backupstop (chem)</td><td>2</td><td>350.56</td><td>1.94</td><td>43,264.00</td><td></td></tr><tr><td>PANCAM_SINGLE_POSITION</td><td>Pancam_backupstop_R1267</td><td>2</td><td>194.44</td><td>1.08</td><td>21,632.00</td><td></td></tr><tr><td>PANCAM_SINGLE_POSITION</td><td>Pancam_backupstop_cal_target_R1267</td><td>2</td><td>156.12</td><td>0.87</td><td>21,632.00</td><td>4 filters, subframed for sweep magnet</td></tr><tr><td>Observation</td><td>Meringue_penuultimate_RemGen (chem)</td><td>1</td><td>1,210.56</td><td>6.29</td><td>2,205,312.00</td><td>Systematic Remote Sensing at drive stops.</td></tr><tr><td>PANCAM_SINGLE_POSITION</td><td>Pancam_Meringue_penuultimate_R1267</td><td>1</td><td>194.44</td><td>1.08</td><td>21,632.00</td><td></td></tr><tr><td>PANCAM_SINGLE_POSITION</td><td>Pancam_penuultimate_cal_target_R1267</td><td>1</td><td>156.12</td><td>0.87</td><td>21,632.00</td><td>4 filters, subframed for sweep magnet</td></tr><tr><td>PANCAM_SINGLE_POSITION</td><td>Pancam_Meringue_penuultimate_L4567R1</td><td>1</td><td>235.56</td><td>1.31</td><td>27,040.00</td><td></td></tr><tr><td>PANCAM_SINGLE_POSITION</td><td>Pancam_5F_cal_target_L4567R1</td><td>1</td><td>185.80</td><td>1.03</td><td>27,040.00</td><td>5 filters, subframed for sweep magnet</td></tr><tr><td>MTES_20_MRAD</td><td>Stop2_MTES Foreword look Work Volume</td><td>1</td><td>340.00</td><td>1.70</td><td>0.00</td><td></td></tr><tr><td>HAZCAM_FRONT</td><td>Front Haz from Penultimate Position</td><td>0</td><td>98.63</td><td>0.31</td><td>2,107,968.00</td><td>Hazcam from penultimate location</td></tr><tr><td>Observation</td><td>Drive Place Holder: To post-penultimate (chem)</td><td>0</td><td>1,676.90</td><td>15.08</td><td>15,132,754.86</td><td>Advance 0.35m to post-penultimate</td></tr><tr><td>Observation</td><td>Pancam_stop_13F Full Frame (chem)</td><td>0</td><td>998.49</td><td>5.54</td><td>140,608.00</td><td>Pancam of stop 2 work volume, to be taken f</td></tr><tr><td>Observation</td><td>Drive Place Holder: To Merrigue (chem)</td><td>0</td><td>1,578.27</td><td>14.77</td><td>13,024,786.86</td><td>Advance 0.5m to Merrigue</td></tr><tr><td>Observation</td><td>NavCam from Post Drive (chem)</td><td>0</td><td>361.90</td><td>1.88</td><td>12,664,032.00</td><td>acquire nav from stop at Coal 4 for pointing c</td></tr><tr><td>Observation</td><td>Mini-TES_Sky_Share_AND_Ground 1X (atm)</td><td>1</td><td>1,048.00</td><td>5.23</td><td>0.00</td><td>High Temporal Resolution survey of T(2), wa</td></tr><tr><td>Observation</td><td>PANCAM_Tau_anytime_01 (atm)</td><td>2</td><td>168.00</td><td>0.93</td><td>10,816.00</td><td>Quantify atmospheric optical depth in two ch</td></tr><tr><td>Observation</td><td>PANCAM_Tau_anytime_02 (atm)</td><td>3</td><td>168.00</td><td>0.93</td><td>10,816.00</td><td>Quantify atmospheric optical depth in two ch</td></tr><tr><td>Observation</td><td>Mini_TES_Elevation_Sky_AND_Ground_ODY_PM (atm)</td><td>3</td><td>977.00</td><td>4.88</td><td>0.00</td><td>Long term monitoring of atmospheric profile o</td></tr><tr><td>Observation</td><td>PMA_Sky_AND_Ground_AMS055 (atm)</td><td>3</td><td>1,145.00</td><td>5.81</td><td>10,816.00</td><td>Long term monitoring of atmospheric profile o</td></tr><tr><td>Observation</td><td>Mini-TES_Sky_Share_AND_Ground 2X(atm)</td><td>3</td><td>1,624.00</td><td>8.11</td><td>0.00</td><td>High Temporal Resolution survey of T(2), wa</td></tr><tr><td>Observation</td><td>Mini_Min-TES_Sky_AND_Ground_Anytime (atm)</td><td>3</td><td>509.00</td><td>2.54</td><td>0.00</td><td>Long term monitoring of atmospheric profile o</td></tr><tr><td>Observation</td><td>Trench_Goal4_Soil</td><td>1</td><td>2,400.00</td><td>26.67</td><td>8,808,038.40</td><td></td></tr></table>

Figure 2. Science Activity Planner (SAP) screen shot shows a science team science activity plan with the higher order observations. Open toggles on some observations show subordinate activities that instantiate the observation.

<table><tr><td>Observation</td><td>PreDrive_Mudpie_IDD_work (Phys)</td><td>0</td></tr><tr><td>SOE_NOTE</td><td>MB_Contact_Soil</td><td>0</td></tr><tr><td>APXS</td><td>short_APXS_Coconut</td><td>0</td></tr><tr><td>HAZCAM_FRONT</td><td>Verify_APXS_Position</td><td>0</td></tr><tr><td>MB</td><td>short_MB_Coconut</td><td>0</td></tr><tr><td>HAZCAM_FRONT</td><td>Verify_MB_Position</td><td>0</td></tr><tr><td>MI</td><td>3pos_3bpp_Coconut</td><td>1</td></tr><tr><td>HAZCAM_FRONT</td><td>Verify_MI_Position_1</td><td>1</td></tr><tr><td>MI</td><td>5pos_3bpp_ChocolateChip</td><td>0</td></tr><tr><td>HAZCAM_FRONT</td><td>Verify_MI_Position_2</td><td>0</td></tr><tr><td>IDD_STOW</td><td>STOW_IDD</td><td>0</td></tr><tr><td>APXS</td><td>Load_5min_cycle_parameters</td><td>0</td></tr><tr><td>Observation</td><td>Pancam_ripple_mosaic (chem)</td><td>0</td></tr><tr><td>PANCAM_MOSAIC</td><td>Pancam_ripple_redmosaic_L2R2</td><td>0</td></tr><tr><td>PANCAM_SINGLE_POSITION</td><td>Pancam_ripple_cal_target_L2R2</td><td>0</td></tr><tr><td>Observation</td><td>Pancam_Mudpie_13F_Full_Frame (chem)</td><td>0</td></tr><tr><td>PANCAM_SINGLE_POSITION</td><td>Pancam_chocolatechip_quarter_L234567Rall</td><td>0</td></tr></table>

Figure 3. A partial image of observations and activities in SAP

## The Science Plan: Integration, Planning, and Prioritization

After defining their observations in SAP, members of the Science Team meet again to discuss and finalize the Science Activity Plan, which is the complete set of requested observations and rover actions for the next sol.

The scientists:

\- Consider each science observation and its related activities in relation to the available rover resources - Make choices between possible plans, considering whether a certain observation must be completed prior to the execution of a second observation, or whether a given observation might have time-of-day constraints for temperatures or lighting.

\- Prioritize according to importance and ensure that the plan achieves the objectives for the sol.

\- Identify a rough planning timeline, and check the plan against a model that predicts the resources that will be consumed.

The observation name improves the efficiency of this work because it highlights important identifiers (such as instrument, method, and constraints) that inform decision making, planning and scheduling. Engineers would have preferred numeric identifiers; however, the ontology provides human-understandable, meaningful, concise and consistent information within the mission information system.

## Scheduling and Sequencing

Next, the engineering team works with MAPGEN software (Ai-Chang et al., 2004) that uses a spatial representation to schedule the labeled observations in relation to fixed events in the day (i.e. rover wake up time and communication windows). Labels identify the contents of observation and must fit within the scope and resolution of this display. (Figure 4). This scheduling process involves a somewhat higher fidelity resource model, resulting in the removal of low priority observations when they do not fit in the available time and power envelope.

![](/api/attachments/TQ3CWWKV/fulltext/images/409ac1f8f6f10437088cc7cdfd422a38c043b016e57f2b94eeb071d8c2facdb6.jpg)

Figure 4. Activity Plan Generator (MAPGEN/APGEN): Screen shots and magnified view of the interface that shows observations as they are “planned” into a timeline for execution. Colors indicate the priority level that scientists have assigned to each observation.

After generating the scheduled plan, an engineering and science team creates “sequences”, i.e., instructions in computer code that the rover can understand. Because the rover only understands its own states, human “translators” tell the rover precisely what to do. This special group of scientist-engineers, called PULs (Payload Uplink Leads), translates desired action into rover states. For example: a description to “Acquire MI image #1 of 7 @ 35mm” translates to “move the robotic arm to acquire the first of a stack of 7 microscopic imager images holding the MI on the IDD 35mm away from the rock or soil target.” This description gives enough information so that the PUL can instantiate a sequence template with 47 different parameters.

Each set of instructions uplinked to the rover and successfully executed by the spacecraft on Mars results in sets of data that require a filename. Engineers must monitor returned data in order to manage limited on board memory. They require unique names.

The current work system and the use of the naming convention described above evolved over a period of three years — perhaps a relatively long time for an engineering effort, but a rather short time for the evolution of a domain of work. In the following section, we relate how we arrived at the naming convention just described.

## Mission Ethnography, Pre-Mission Training Sessions and the Use of Grounded Theory in Developing a Naming Convention and an Ontology for Science Work and Distant Robotic Action

“Naming,” a conglomeration of related issues, was the underlying issue in our grounded theory research, in part because the mission did not initially recognize naming as key to the efficient planning and execution of science requests. We started with an initial identification of the problem: the absence of a meaningful naming convention. In the first test session, we worked through the deconstruction of that problem, and in later field tests identified categories (Strauss and Corbin, 1990) and a taxonomy (Spradley, 1980) that contributed to an emergent grounded theory relevant to a naming convention. We determined that we needed a naming convention that could work as natural language during the collaborative human process (abbreviated names) and one that could transition into an ontology for the identification of relatively precise and consistent identifiers in software and tools. The need was to support science requests, moving from science to engineering teams and eventually translating them into commands for the rover.

Below we describe some of the work of scientists and engineers during mission sponsored FIDO (Field Integrated Design and Operations) rover field tests in 2001 and 2002 and in later (2003) pre-mission operations readiness tests (ORTs) that contributed to the grounded theory development. These were tests prescribed by the mission to design and train mission participants in the work of Martian surface operations.

During these tests the grounded theory process involved repeated cycles in which we:

\- Gathered data relevant to what we saw as an emerging need for the mission - the ability to name and identify the parts of remote robotic work in making science requests;

\- Analyzed the data to contribute to the emerging grounded theory;

\- Made recommendations to the mission for abbreviated names and an ontology with a flexible syntax, semantics, and a description of the relationships between the categories of identifiers for referencing and naming science work;

\- Analyzed the resultant work practice during tests and training after our recommendations had been implemented; and

\- Developed new parts of the theory and made iterative recommendations over the pre-mission time period.

## 2001 Test: Identification of a Naming Problem

These early tests revealed the previously unrecognized need for a standardized, consistent naming convention that: was based in the elements of natural language discussion; was complex enough to identify parts of the work; and could represent scientific requests to downstream engineering teams and software tools. The absence of such a scheme made it difficult to trace the history of work, caused ambiguity in referencing, and excluded necessary information to support group understanding.

The major insight from the 2001 test data was that much of the naming confusion resulted from the use of a single target name to represent both the objects in the domain and the action on those objects. The target name was the single tag for work that was being done, yet that work involved pointing, referencing, and identifying action of the rover, and situating the work in the remote environment. The need to incorporate the instrument in the written/software name was not at first obvious, because scientists and engineers were using the instrument name in conversation, and the conversation was conveying information to a small group of participants in a confined space and time. Unlike transient military target points, the targets of scientific interest persist in the Martian environment and are relevant to later work. Request names must therefore distinguish state changes for those targets from the targets themselves and carry information for additional work or related work.

![](/api/attachments/TQ3CWWKV/fulltext/images/1d68f4795b08282688bd1b71423f9ad1443f8ece9ec0e217a0ce1cac3732ad64.jpg)

The science team created a variety of naming conventions. The problems they encountered motivated the research reported here. Table 1 incorporates issues identified during the early tests as well as the emergent theories that were grounded in analysis of that in-situ data.

## 2001 Findings

Based on the above realizations, we identified a premise in our theory that the naming convention and its related ontology must identify and convey information about both objects and action in the domain. Once we stated this premise, we also saw that there were different categories of objects (ex: features and targets) and different categories of action (ex. drive and instrument work) and that action categories implied the need for other identifiers. Names had to be unique and consistent, yet complex enough to support cross-referencing to more than one activity on an object.

## Cumulative Findings: Grounded Theory and Ontology Development

2001: Object-action distinction; feature-target distinction, categories of action distinction; whole-part relationships; names must be unique, consistent and human centered; group similar types of work

<table><tr><td colspan="3">Table 1. 2001 Test Events - Early Findings Related to the Problem of &quot;Naming&quot; and Emergent Concepts for Grounded Theory Development</td></tr><tr><td>Examples of Names and Referencing by Scientist</td><td>Related Issues</td><td>Emergent Theory: concepts for testing in 2002 tests</td></tr><tr><td>Use of descriptive names: Geometric Rock, White Rock</td><td>Meaningful, but multiple schemes developed; lacked systematicity.</td><td>Work requires a standardized, systematic naming convention</td></tr><tr><td>Use of ordered names (Alpha, Beta, Gamma); rover-centric # s</td><td>Carries an implicit order, but difficult to remember referents.</td><td>Names should have human-centered meaning</td></tr><tr><td>Names to describe the requesting group and the sol of work: Sol#_science theme group identifier_target#</td><td>Required renaming if different groups identified the same target. Required renaming to an &quot;official&quot; target name. Caused referencing confusion. Scientists had to keep elaborate notes on name changes.</td><td>Names must be consistent throughout the planning process</td></tr><tr><td>Use of theme names: Aaron, Ruth, Mantle (baseball theme)</td><td>Difficulty tracking and referencing because some targets were given new names on new solConfusion resulted over what work had been done on what targetsData were lost</td><td>Names must be unique and consistent yet complex enough to support cross-referencing</td></tr><tr><td>Verbal references implicitly group related activities</td><td>Difficulty keeping track of conceptual groupings because s/w does not support grouping</td><td>Related work needs to be grouped so it can be identified</td></tr><tr><td>References to a body of work by single target name. Ex: &quot;Ruth-like&quot;</td><td>Difficult to know if work was done on same rock. Some work will be related due to fact that it is done on a common geological feature</td><td>Must name rocks/soil as well as targets on the rock/soil</td></tr><tr><td>Informal conversation includes verbal identification of instrument names</td><td>Confusion as to what kind of work had been done, because the instrument was not included in formal name.</td><td>Names must explicitly identify both the object (target) and the action (instrument)</td></tr></table>

![](/api/attachments/TQ3CWWKV/fulltext/images/8d35b60b65d7fee6db8984fb9a6607d6e24eb4552a93960f312854f12bf38a8d.jpg)

## 2002 Test Findings and Ontology Development

Based on our findings in 2001, we began our grounded theory development for testing in 2002. We constructed a first taxonomy consisting of instruments, features, targets, observations, and activities; provided definitions for the constructs; and began to establish relationships between the parts of the taxonomy that included:

• Separating objects from actions by including instruments in the name as the representative of action.

\- Providing a way to differentiate between features and targets when referencing work.

\- Creating higher-level observations (to group individual activities with a common purpose).

## We recommended that:

## Target names:

\- Reflect a whole-part relationship with a feature, if possible, such that the feature represents the whole and the target represents the part (i.e., Feature=Shoe; Target=Heel). The expectation was that whole-part names establish relationships between target points as well as identify the relationship between multiple targets and a common feature.

## Observation names:

\- Identify the instrument as well as the feature name and a target.

\- Have a consistent syntax. Instrument should be identified first as the most consistent reference, then feature and then target. Instrument\_Feature\_Target. Example: Pancam\_Shoe\_Heel, identifying first the panorama camera instrument, pointing at the feature shoe, with the center image point on the target heel.

\- Indicate basic relationships between objects and actions, such as which instrument was used on which feature and target.

To reflect the way that scientists often described the work, we recommended that observation names could also indicate pointing to remote objects and pointing to more than one object. We recommended the use of “Survey,” drawn from science field use, for indicating such relationships.

As we analyzed the work of the science team from FIDO 2002, we understood that our research and recommendations had changed the developing work practice of the scientists. These appear in Table 2 under Implications on Work Practice. We recognized the need to identify features in the environment, reference rover instrumentation in the names, and develop systematic methods for tele-robotic exploration. As a result of our work on FIDO 2002 results, we expanded the parts of the ontology to include identifiers related to methods and constraints, helping to make intent visible in uplink tools and integral to later engineering decision making.

## Cumulative Findings: Grounded theory and Ontology Development

2001: Object-action distinction; feature-target distinction, categories of action distinction; names must be unique, consistent and human centered; group similar types of work

2002: Observation-activity distinction; whole-part relationships; include reference to rover instrumentation; development of systematic methods and constraints

## 2003 Pre-Mission Tests and Training Sessions

As we expanded the official taxonomy and continued our grounded theory analysis for testing in 2003, we defined increasingly complex relationships between observation, activity, feature, target, and instrument use.

Tables 3 and 4 give an overview of the developing theory and the findings we tested. They describe the parts of the ontology, their inter-relationships and the related scientific work practice implications. Some additional examples of the developing complexity in naming include:

\- A convention that differentiated between the use of a single instrument and multiple instruments in an observation [Table A 3]

\- The implications for work and naming when doing in-situ work with the rover's arm placed on rock or soil and for remote-sensing work, in which instruments were used to take measurements or images at a distance from the rover.

## Additional 2003 Findings Related to Ontology Development

Differentiating Between Activities

The initial mission design called for the scientists to simply choose activity types from a dictionary in the science planning software and populate their observations with formalized sets of information. The 2003 tests showed us that activities required additional differentiation for downstream teams to use in planning and commanding. $^{1}$

The syntax for naming an activity became

## Distinguishing parameter\_Target

At the observation level, the syntax represented the relationships between instrument, method, feature, and other identifiers. The first identifier was instrument and the last was feature.

Differentiating Between Observations

The syntax for naming an observation became

Instrument\_Method\_Other Identifier\_Feature

Multiple instrument observations had the following syntax

PMA\_Method\_Other Identifiers\_Feature

IDD\_Method\_Other Identifiers\_Feature

<table><tr><td colspan="4">Table 2. 2002 Test Events – Grounded Theory Development from 2001 tested in 2002 Related to Parts of the Ontology: Feature and Target Examples</td></tr><tr><td>Grounded Theory tested in 2002</td><td>Recommendation</td><td>Example</td><td>Implications of Theory on Work Practice</td></tr><tr><td>Actions and Objects: need to be identified separately</td><td>Names must contain both instrument and feature/target names</td><td>APXS_heel</td><td>Used instrument names explicitly, work and data became easier to reference unambiguously. Planning was more efficient.Time and training limits minimized software entries.</td></tr><tr><td>Features:are objects of interest in the terrain (cliff face, crater, hill)do not require associated actions may contain several targets.</td><td>Identify features and targets separately in the softwareFeatures can stand alone</td><td>Feature= shoeTarget= heel</td><td>Used distant features as directional reference points, in both s/w and in printed images. Reference to features in talk subsumed individual target references.Features became markers for planning and rover drives.Used feature name to reference entire body of data drawn from work on a feature as well as to refer to generalized target data from particular instruments.</td></tr><tr><td>Targets:serve as focal points for instrument activity/actionexist only as parts of identified featureswhole part relationship between features and targets</td><td>Identify targets and features separately in the softwareAssociate targets with a featureUse whole/part relationship to help in memory and referencing</td><td>Feature= shoeTarget= heel</td><td>Used target designation for fine pointing of instrument activityFound it hard to create names identifying whole/part relations for feature/target in short timeline.Often numbered targets as part of feature names, e.g., RIO_1, RIO_2 resulting in less distinctive names, required coordination to avoid repetition.Targets were sometimes named after an instrument, e.g., Min_1, Min_2 and the same name was used on different targets across sols.</td></tr></table>

<table><tr><td colspan="4">Table 3. 2003 Test Events – Grounded Theory Development from 2002 tested in 2003 Related to Parts of the Ontology: Observation and Activity Examples</td></tr><tr><td>Grounded Theory Tested in 2003</td><td>Recommendation</td><td>Example(s)</td><td>Implications of Theory on Work Practice</td></tr><tr><td>Activities are actions defining work of instruments and rover state.Activity types from dictionary are not unique enough to provide updated information across tools and teams.</td><td>Expand Activity names to convey information about requestsUse additional identifiers to make names unique</td><td>Pancam_8_filter</td><td>Information supported downstream planning as teams found it easier to distinguish between activities in the software</td></tr><tr><td>Observations are containers that combine activities with the same scientific purpose.Activities define the work of observations.</td><td>Group related activities under Observations in the software</td><td>See names in Figure 3</td><td>Hierarchy organized science work and planning as well as uplink planning by other teams</td></tr><tr><td>Observation names reflect different basic relationships between instrument and feature</td><td>Create identifiers that indicate these relationships, e.g., survey</td><td>Sky_survey_IPS_2EII(a spectral survey of 2 distinct elevations in the sky)</td><td>Accepted first in atmospheric use that was focused on remote work.Supported remote sensing referencing</td></tr></table>

<table><tr><td colspan="4">Table 4. 2003 Test Events - Grounded Theory Development from 2002 tested in 2003: Other Findings Related to Parts of the Ontology</td></tr><tr><td>Grounded Theory</td><td>Recommendation</td><td>Example(s)</td><td>Implications of Theory on Work Practice</td></tr><tr><td>Instruments have classes that reflect fundamental differences in instrument use and work.</td><td>Identify classes of instruments in names when doing certain types of grouped activities.</td><td>Remote-Sensing (PMA) In-Situ (IDD)</td><td>Instruments were used for different purposes and methods. This was important to identify in the name.</td></tr><tr><td>Observations cannot contain activities that cross instrument classes.</td><td>Cannot do remote sensing work and arm work in same observation</td><td>APXS_feature Pancam_feature</td><td>Concept was based in the logic of the work and the importance of identifying the individual location of sets of data collection.</td></tr><tr><td>In-situ science must distinguish between work on different features.</td><td>In-situ observations should include only one feature.</td><td>MI_Roadcut MI_Coconut</td><td>Rover movement and data collection context required separate identification of rover work events.</td></tr><tr><td>Methods correspond to stereotypical combinations of instruments, or special ways of using an instrument.</td><td>Make Method an identifier in the name. Describe emerging methods</td><td>Comparison, movie, quick look, blind Scratch</td><td>Provided semantics for sets of activities. Scientists began to use method names. (The identification of method names became apparent during training opportunities)</td></tr><tr><td>Learning is on-going. Constraints are central to planning.</td><td>Provide “Other Identifier” field in name to enter new descriptors or to develop constraints</td><td>Temporal: Afternoon Spatial: North, Long, Around</td><td>Provided additional opportunity to indicate explicit semantics.</td></tr><tr><td>Field of view and target pointing are conceptually different.</td><td>Name FOV pointing based on azimuth and elevation</td><td>Azimuth 30 degrees</td><td>Provided alternative approach to naming and identifying targets. Accommodated theme groups that did not need features---e.g., Atmospheric</td></tr></table>

<table><tr><td colspan="2">Table 5. Examples of Observation and Activity Naming</td></tr><tr><td>Observation Names: Examples</td><td>Meaning of the name</td></tr><tr><td>MI post rat Buffalo</td><td>Take a Microscopic Image of Buffalo, after using the Rock Abrasion tool</td></tr><tr><td>Mini-TES_Movie_30deg_Sky</td><td>Take several consecutive MiniTES measurements of the sky at a 30 degree elevation</td></tr><tr><td>IDD_Post Scratch_Plymouth Rock</td><td>Take several different kinds of in-situ measurements of Plymouth Rock, after scratching the rock with the RAT</td></tr><tr><td>Activity Names: Examples</td><td>Meaning of the name</td></tr><tr><td>Red single Pilgrim</td><td>Take a single frame image of the target pilgrim, using the red filter of the Pancam</td></tr><tr><td>5 filter vent_center</td><td>Take a Pancam image of the target vent_center using five filters.</td></tr></table>

As the science team worked, we began to see additional differentiations develop. Remote sensing observations, those that require pointing to and work on objects in the distance required separate referencing from In-situ observations, those that place the rover's instrument arm on a rock or soil patch.2 The cognitive differences between these two types of observation, as well as associated planning difficulties and the different configurations of the rover, made them separate types of science requests. These differences also led us to believe that the designations, "remote sensing" and "in-situ" (terms already used by the science team) should be the observation name identifiers for work using more than one instrument. The science team asked to use "IDD" and "PMA" as shorthand identifiers in the software for these two types of work. Those names referenced instruments located on the robotic arm Instrument Deployment Device (IDD) or on the Pancam Mast Assembly (PMA) (see Table 6). Method as an overall category became an increasingly important identifier at the observation level for the emergent ontology.

## Requirement for Flexibility

By the end of the training sessions, and based on our understanding of the increasing complexity needed to identify the work, we determined that a completely fixed naming convention would not support the multiple types of observations or define the complexity of the tele-robotic work. Nor would it accommodate learning and changes that we could already see taking place as the team discovered new ways to use the rover, created more sophisticated and new scientific methods, and dealt with changes in the environment and mission context, such as variations in the Deep Space Network communication cycles. Our final recommendation for the convention was an open invitation to scientists to enter what we came to call “other identifiers,” typically temporal or spatial constraints and pointing (e.g. 30 degrees).

While we had based our recommendations on grounded theory and had worked with the science team to develop the naming convention, the abbreviated names, and the ontology, we also knew that workers in a domain will often find work-arounds to tools and procedures that are inefficient. The test of the effectiveness of the naming convention and related ontology would be in the mission itself.

Cumulative Findings: Grounded Theory and Ontology Development

2001: Object-action distinction; feature-target distinction, categories of action distinction; names must be unique, consistent and human centered; group similar types of work

2002: Observation-activity distinction; whole-part relationships; include reference to rover instrumentation; development of systematic methods and constraints

2003: Concept of “other identifiers for flexibility; classification of instrument types (remote sensing and in-situ).

<table><tr><td colspan="3">Table 6: Remote Sensing Instruments and relationships between Instruments, Features and Targets</td></tr><tr><td># of Instruments</td><td>One Feature</td><td>Multiple Features</td></tr><tr><td rowspan="2">One Instrument(Use instrument or shorthand name)</td><td>Include feature namePancam_ShipsProw</td><td>Include one or two features and relation identifier or method for grouping featuresPancam_Surveyaround_ShipsProw</td></tr><tr><td>Include feature name and relation identifier or method for grouping associated targets with featureMiniTES_ShipsProw</td><td>Include one or two features and relation identifier or method for grouping associated targets with featuresMiniTES_Surveyaround_ShipsProw</td></tr><tr><td rowspan="2">Multiple Instruments(Use PMA instrument class name)</td><td>Include feature namePMA_postScratchSniff_ShipsProw</td><td>Include one or two features and relation identifier or method for grouping features with target namePMA_Surveyaround_ShipsProw</td></tr><tr><td>Include feature name and relation identifier or method for grouping associated targets with featurePMA_Surveyon_ShipsProw</td><td>Include one or two features and relation identifier or method for grouping associated targets with featuresPMA_Surveyfrom_ShipsProw to Boulder</td></tr></table>

## 2004 Mars Exploration Rover Mission: Work Practice, Naming and the Use of the Ontology

This section describes the results of a qualitative analysis of the science plan data and the work practice during the mission that began in January of 2004. It describes the use of constraints, the development of method, observations and activities, and the use of feature and targets within the actual mission context.

## Work Practice and Naming Development

Scientists adapted the naming convention as they gained experience with the operational environment and developed new methods of tele-robotic exploration. The basic ontology held through the mission, but some of the individual elements continued to develop. Specific examples of observation name development from mid mission to end of nominal mission in April of 2004 appear in Table 7 below and will be discussed here in the order of their appearance in the table.

## Temporal Constraints and Other Identifiers

The category of temporal constraints expanded dramatically, with the addition of a number of different subcategories. Specific (numeric) and general timing constraints appeared as proxies for changing temperature and lighting. The need also arose to indicate the absence of a temporal constraint (anytime). Temporal constraints also expressed synchronization with rover events to ensure that the data from two observations reflected the same underlying conditions (e.g., Post MB). While commanding respected these constraints, nowhere in the rover language were there pre-requisites for temperature, lighting or synchronous events. The ontology allowed scientists to express such relationships.

The science team adapted the syntax to the engineering context. Our formal ontology called for feature to always be identified at the end of the name. As time went on, however, scientists began to locate temporal constraints, not feature, at the end of the name. For example, scientists doing remote sensing (PMA) work placed temporal constraints at the end of the name in the early part of the mission: Pancam\_Tau\_Anytime. However, when the mission moved into an extended operations phase, the planning process became more standardized, and engineers began to use templates for pre-planning activity requests. Because the temporal constraints were key in this template planning, engineers requested that the science team place temporal constraints first in the observation name. So instead of Pancam\_Tau\_Anytime they wrote Anytime\_Pancam Tau,

<table><tr><td></td><td>Mid Mission</td><td>End of Nominal Mission</td></tr><tr><td>TemporalConstraints</td><td>13:30 LSTMiddayAnytimePost MBPrebrushSol 46PreMGSUltimate/penultimate/Antepenultimate</td><td>Before 14:30Post backupPlan A, IF Dist GT .085mOvernight sciencePre or Post ODY</td></tr><tr><td>Methods</td><td>Traverse clast surveyMini-MiniTESStutter step</td><td>Super clast surveyGround Stare3x1x255 Stares</td></tr><tr><td>Purposes</td><td>ReconTransient Temperature Doc</td><td>Dust Devil FinderPhobos Set</td></tr><tr><td>Features</td><td>Trex cheekSoilEjecta blanketIDD work volume</td><td>Crater floorHeatshield</td></tr></table>

## Method Development

Experience with the specific tool suite lead to the development of numerous specific methods of rover activity such as a scuff and go, brushing, mini-Mini-TES, and stutter step. The science team also named different ways to plan rover mobility, or "drive" as the table indicates. New method names were still appearing after 45 sols of operations. The ability to name clusters of activities with a single label lends support to the idea that observations were containers that rendered the work coherent and that the ontology helped frame the tele-robotic work of the science team. As we first saw during the field tests (Table 3), purpose continued to emerge in the observation names. Some of the purposes were primarily operations-relevant, such as reconnaissance or turning for communication. However, some of the purposes were scientific, such as documenting transient temperature.

## Feature Name Development

The use of features in the observation name also evolved with the mission. We had recommended that scientists use a whole/part relationship when identifying features and targets to help with information and knowledge management during Uplink discussions and in finding information in returned data. Whole/part relationships were used more consistently with the in-situ IDD instruments. We discuss this further when we turn to activity names and the use of targets. Here we note that target name, which was supposed to be an activity identifier, was sometimes elevated to the observation name to create specificity and distinctiveness.

## Activity Name Development

While mission activity names included temporal constraints (such as pre and post), constraints were not included with the regularity we observed in observation names. Activity names also acquired some method names, generally referring to parameter settings (i.e., cal for calibration). Purpose also crept in to activity names, to capture both operational and scientific rationale. The most prevalent descriptor on an activity functioned as both a method and a target. For example, when doing remote sensing pointing, as we had anticipated during earlier field trials, scientists increasingly used the FOV perspective, relying on azimuth and elevation numbers. Further, as we indicated earlier, features were less important in remote sensing, because the product of remote sensing is typically a region rather than a particular spot. Table 8 describes some of the additions to activity names that appeared during the mission.

<table><tr><td colspan="3">Table 8. Activity Name Highlights</td></tr><tr><td></td><td>Mid Mission</td><td>End of Nominal Mission</td></tr><tr><td>TemporalConstraints</td><td>16:10NighttimeMI preMBPost DriveUltimate/penultimate</td><td>DaytimePostgrind</td></tr><tr><td>Methods</td><td>Cal target filtersTriple PlayColor stereo</td><td>Cal plus sweep magnet1x1x50 Block</td></tr><tr><td>Purposes</td><td>For MTES overlayVerify placementMineralogyLayer Study</td><td>Document placementVerify position</td></tr><tr><td>Features andTargets</td><td>Cherry centerBelow SunRear view tracks</td><td>Target 1Placement 1Drive directionFilter magnets</td></tr></table>

We also saw the occasional use of numbers to identify targets. Over time, numbers are not always meaningful or unique, but within the context of a particular static situation, their use can seem an acceptable practice. Another variation in target naming work practice was of particular interest, however. Scientists sometimes had to identify several target points in the software before finding the exact spot for the placement of the RAT on a rock, because the placement on the rock had to be optimal for surface abrasion and yet within the reach of the rover arm. In this case, the team sometimes used numbers to identify various candidate targets. They might also use the feature name with the number to help keep the number in context, such as McKittrick\_1, McKittrick\_2. We suggest here that the science team found this the most expedient way to target a number of points at once, knowing that they would use only one in the end. Cumulative knowledge management of these two variations was not as serious an issue as it would have been if every target in the mission had been identified only by a number.

## Ontology and Observation Name Development

As the mission went on, observation names got longer. We believe this tendency correlated with the increased use and standardization of methods (Shalin V., in prep) and the indicated desire of the science team to make sure that important relevant information was obvious in the software at both the observation and activity levels. For example, in situations where scientists were requesting re-work on the same feature, they sometimes elevated the new target name to the observation level to make sure that others understood this was a request for new target work. Important parameters were also elevated to the observation level on occasion.

Examples of a longer name from later mission work are:

\- MTES Elevation Sky AND Ground ODY PM

\- Pancam Midway 1 4Fs (Four Filters on Soil)

\- PM ODY mini TES Elevation Sky AND Ground Beta Pancam Photometry Photometric Equator3

The naming convention for MER contained abbreviated names and an ontology for distant robotic action. Figure 5 represents the parts of the ontology that supported the work of creating and instantiating observations with specific examples from the MER mission. Figures 5 and Figure 1 together identify the high-level relationships between the parts of the ontology as they were used across teams for decision making, in uplink software tools for planning, and then honed into more explicit identifiers for commanding the rover.

In summary, by developing a grounded theory over several iterative cycles of mission testing, science work practice evolved. We came to understand the work of participating scientists and engineers, resulting in a naming convention of abbreviated names as well as a related ontology for scientific work. While developing the underlying theory, we were less concerned about the effect of our interventions from a research perspective than we were eager to improve the effectiveness of the mission itself. However, our positions did not allow us to enforce any recommendations if they had not solved existing problems. We suggest that the recommended ontology was adopted because it emerged through grounded theory analysis, was relevant to the work being done, and served the needs of the mission. Hadar and Soffer (2006, p. 586) suggest that the creation of useful tools to support practical tasks is key to the empirical evaluation of an ontology.

![](/api/attachments/TQ3CWWKV/fulltext/images/af73640e6f1fa865e97d6f9f5a9bfe3029cf7e8e76f161711a4b0ff6bb65e86a.jpg)

The “naming problem” first identified in early field tests was related both to the need to reference rover capabilities and the need for extended planning work across multiple tools that required multidisciplinary communication among human participants. All scientists, whether as individuals, small groups, or a whole team, used the emergent ontology to plan and coordinate work. The engineering team used the ontology to structure planning and trim scheduling to meet available resources.

Cumulative Findings: Grounded Theory and Ontology Development

2001: Object-action distinction; feature-target distinction, categories of action distinction; names must be unique, consistent and human centered; group similar types of work

2002: Observation-activity distinction; whole-part relationships; include reference to rover instrumentation; development of systematic methods and constraints

2003: Concept of “other identifiers for flexibility; classification of instrument types (remote sensing and in-situ)

2004 Mission: Explosion of use of temporal constraints; syntax reconfigured to incorporate meaning for engineering team

![](/api/attachments/TQ3CWWKV/fulltext/images/49f54affdc1613f80fa97c1a14ad10a96b6784cb741686007730030a2529b0b3.jpg)

![](/api/attachments/TQ3CWWKV/fulltext/images/3448d7bfbb921e1cf0d51b1891ca9c457f84260ed1a7169e506efa626f7f8d50.jpg)

## Conclusions

We believe the definition of the emerging ontology in this domain served several purposes. It provided procedural and work practice support and a shared language for interdisciplinary exchange. It established consistency for software representations. It incorporated referents to scientific work and allowed for the unique specification of requests for both the science and downstream engineering teams. Finally, the ontology captured shared conceptualizations and representations for the historical record. While we were working to support the remote work of the MER mission, similar ontological constructs could support other remote work such as tele-medicine.

Regarding ontology development we found:

1. Ontologies of work in information systems must contain both actions and objects to identify and represent all aspects of the work involved. These must represent the basic units of the action in the work system (e.g. method, instrument) in relation to the objects (e.g. features and targets) on which the work will be done.

2. Requests for science work are organized around higher order descriptors (what we call observations) that refer to and group the steps of the work. The lower order descriptors of the work (what we call activities) depend on the instrumentation, in this case of the rover. The observation and activity work descriptors were not explicit in the rover command language. The decoupling of these descriptors from rover code, however, allowed for flexibility in naming and the evolution of scientific work based on pervasive and continual learning.

When developing associated software in emerging domains, it is important to limit restrictions as much as possible until the nature of the work can be better understood. Eventually software fields can reflect pre-set taxonomies (such as instruments, constraints, and methods) that offer participants (in our case both scientists and engineers) the ability to view and flexibly reconfigure information most salient to their work. Increased formality can then capture and present information consistently across the various tools within a system.

3. An ontology of action must take into account a dynamic environment and reflect multiple concepts: changes in response to natural physical events, interactions with objects that have their own changing state conditions (terrain changes and moving robotic satellites), and constraints (time, before and after). It must reflect the influence of context on the meaning of intentional action. The appearance over time of temporal constraints in the expert work on MER acknowledges that names for action must be able to reflect a changing environment.

4. In a dynamic environment, teams require semantics that are not just internally consistent within the software and supportive of action in a dynamic external environment, but can also adjust to users who are themselves changing, that is learning, over time. When constructing an ontology for an emerging domain of action, the ontologist should expect dramatic, frequent revisions and have the capability to capture and support both incremental and revolutionary revisions over time. The addition of the open concept of “other identifier” in our naming convention helped the ontology adapt and support learning and change, even while the robotic technology remained stable.

This finding is consistent with past work in cognitive theory that acknowledges the role of new conceptualizations as a result of learning (Greeno, 1983): As leaning takes place, new conceptualizations will develop. It is also consistent with the understanding in current ontology development (McGuinness, 2001) that ontologies require extensibility, or the ability to adapt to user needs and projects.

5. A set of formal, intentional, conceptual primitives is less relevant in our ontology because meaning goes beyond the intentional when executing action in a physical environment. Additionally, in this environment human actors helped bridge the gaps between the external ontology, the internal rover command language, and the environmental context.

Context sensitivity and the absence of an intentional analysis challenges formal approaches to the construction and evaluation of an ontology typically applied to objects such as that developed by Zhang, Cao, Gu and Si (2004). Our novel problem domain demanded methods that fell outside the traditional ontologist's tool kit. We expect that our contribution, founded on less traditional methods, will extend the scholarly dialogue on ontology development in action domains.

Nevertheless, the motivation for ontology development is the need to share structured information [Musen, 1992; Gruber, 1993] that represents agreements about shared conceptualizations [Gruber, 1994]. The main driver behind our research and ontology development was the need to define, frame, and standardize shared conceptualizations (abstract models) of the work of Martian tele-robotic science in unambiguous representations.

The MER ontology and the associated abbreviated names exemplify the definitions for an ontology referred to by Gruber (1994) and Guarino and Giaretta (1995). That is, it is not so much a complete specification of shared conceptualizations as it is an incomplete or partial agreement or account of those conceptualizations. The fact that identifiers in this ontology changed as the work developed, responding to changes in the Martian environment as well as in the planning and uplink process, suggests that such an ontology in a dynamic environment can only be a partial account of shared conceptualizations.

While extensibility is crucial for any information technology, especially those concerning long term product lifecycle management and ubiquitous computing, we believe this research demonstrates that an ontology for executed action in a dynamic environment demands the greatest flexibility. More generally, we claim that ontological change is a key property of knowledge creation, crucial to the enduring usability of workplace technology (e.g., Li and Kettinger, 2006).

Regarding the use of abbreviated names for referencing work, we found:

1. Abbreviated names can be successful identifiers along with an associated ontology, as long as they contain consistent and systematic representations of the work to be done and draw on pre-identified parts of the ontology to create descriptions of the work being done.

2. Abbreviated names allow for natural language referencing and knowledge and information sharing during collaboration in a domain as well as for the translation of work from one set of experts to another across domains and software tools.

Regarding the relationship between work practice and an ontology for scientific work, we found:

As we used “mission” ethnography to understand work practice and gather data for our grounded theory research, we realized that we were not just identifying and formalizing shared conceptualizations salient to organizing and planning telerobotic work. We were also identifying and describing the work of the scientists themselves. The higher order abstractions in the ontology (observation, activity, feature, target, method, etc.) used for referencing robotic work also represented steps in the scientific work process (defining and instantiating scientific observation, defining parameters and constraints, and using methods) on the objects necessary to scientific work (features). Thus, they specify the inter-relationship between work practice and the categories of an ontology.

Regarding research in knowledge elicitation, we found:

The methodological focus of the work in ontology formation has been on the formalization of the relationships between objects. While we agree that object relations are important, we found that a greater focus on work process and work practice and consideration of how they are related to shared conceptualizations and expert knowledge enabled us to identify relevant ontological categories.

![](/api/attachments/TQ3CWWKV/fulltext/images/e5006de1a6378ff9d16928121fc693a607b9b29f290a6e077458d9190138cb65.jpg)

## Acknowledgements

We are grateful to the members of the MER Athena Science Team for their collaboration in developing the MER naming convention. Their feedback, insight and patience were invaluable. We are also grateful to many members of the JPL MER Development team for their feedback and comments and for administrative support from Jim Erickson, Steve Sqyures and John Callas. We wish to thank the NASA Ames Research Center for funding the research. Thanks also to Jay Trimble and Andy Mishkin for their support of our MER research, the SAP and MAPGEN teams for incorporating our suggestions and to Dan Berrios, Keri Carpenter and Zara Mirmalek for their valuable comments in formulating this work. We thank members of the Workplace Cognition group at Wright State University, especially Katherine Lippa and Ben Simpkins for their assistance with this manuscript. The manuscript reviewers and editors of this journal provided numerous suggestions that improved the quality of the product.

Clancey, W. J. (2001). "Field Science Ethnography: Methods for Systematic Observation on an Expedition." Field Methods, (13) 3, pp. 223-243.

## References

Ai-Chang, M., and J. Bressina, L. Charest, A. Chase, J. Hsu, A. Jonsson, B. Kanefsky, P., Morris, K Rajan, J. Yglesisa, B., Chafin, W., Dias, P. Maldaque (2004). MAPGEN: Mixed-Initiative Planning and Scheduling for the Mars Exploration Rover Mission. IEEE Intelligent Systems, vol. 19, no. 1, pp. 8-12,

Behrend, D.A. (1995). Processes Involved in the Initial Mapping of Verb Meanings. In M. tomasello and W.E. Merriman (Eds.) Beyond Names for Things (pp. 251-273). Hillsdale, NJ: Erlbaum

Bloomberg, J., and J. Giacomi, A. Mosher, and P. Swenton-Wall (1993).

"Ethnographic Field Methods and their Relation to Design", in Schuler and Namoida (eds.) Participatory Design: Perspectives on System Design. Lawrence Erlbaum: Hillsdale, NJ, pp. 123-155.

Brachman, R. (1979). On the Epistemological Status of Semantic Networks. In N. Findler (Ed.), Associative networks: Representation and Use of Knowledge by Computers. New York: Academic Press.

Bowker, G. and S. L. Star (1999). Sorting Things Out: Classification and Its Consequences. Cambridge, MA: Massachusetts Institute of Technology.

Carnap, R. (1947). Meaning and Necessity: A study in Semantics and Modal Logic. Chicago: University of Chicago Press.

Degani, A. and E. Wiener (1997). Procedures in Complex Systems: The Airline . IEEE Systems Man and Cybernetics Part A- Systems and Humans, 27(3), 302-312.

Dreyfus, H.L. (1979). What Computers Can't Do. 2nd. ed. New York:

Dreyfus, H.L. (1997). From Micro-worlds to Knowledge Representation: AI at an Impasse. In Mind design II: Philosophy, Psychology, Artificial Intelligence. J. Haugeland (ed.) Cambridge, MA: MIT Press.

Forsythe, D. E. (1999). "It's Just a Matter of Common Sense: Ethnography as Invisible Work", Computer Supported Cooperative Work 8: Kluwer:

Forsythe, D.E and B. G. Buchanan (1989). "Knowledge Acquisition for Expert Systems: Some Pitfalls and Suggestions", IEEE Transactions on Systems, Man and Cybernetics 19(3), pp. 435-442

Gebauer, J. and F. Schober (2006). Information System Flexibility and the Cost Efficiency of Business Processes. Journal of the Association for Information Systems, 7, 122-147.

Georgeff, M.P. and A.L. Lansky (1986). "Procedural Knowledge." Proceedings of the IEEE. 74 (10) pp. 1383-1398.

Glaser B and A. Strauss (1967). The Discovery of Grounded Theory: Strategies for Qualitative Research. New York: Aldine De Gruyter

Greeno, J.G. (1983). "Conceptual Entities," in D. Genter and A. Stevens (eds.) Mental Models, Hillsdale, NJ: LEA.

Gruber, T. (1993). "A Translation Approach to Portable Ontology Specification", Knowledge Acquisition (5), pp. 199-220.

Gruber, T. (1994). email communication, SRKB Mailing list, in Uschold, M and M. Gruninger (1996) "Ontologies: Principles, Methods and Applications", The Knowledge Engineering Review, 11, pp. 93-136.

Guarino, N. and P. Giaretta (1995). “Ontologies and Knowledge Bases: towards a terminological clarification”. In N. Mars, (ed) Towards Very Large Knowledge Bases; Knowledge Building and Knowledge Sharing, Amsterdam: IOS Press, pp.25-32.

Hadar, I. and Soffer, P. (2006). Variations in Conceptual Modeling: Classification and Ontological Analysis. Journal of the Association for Information Systems, 7(8), 568-592.

Jordan, B. (1996). "Ethnographic Workplace Studies and Computer Supported Cooperative Work", in D. Shapiro, M. Tauber and R. Traunmüller (eds.) The Design of Computer-Supported Cooperative Work and Groupware Systems (1996), North Holland/Elsevier Science: Amsterdam, pp. 17-42.

Lewin, K. (1946). "Action Research and Minority Problems". In Resolving Social Conflicts: Selected Papers on Group Dynamics by Kurt Lewin. K. Lewin (ed). New York: G.W. Harper and Brothers.

Li, Y. and W. J. Kettinger (2006). An evolutionary information-processing theory of knowledge creation. Journal of the Association for Information Systems, 7, 593-617.

McGuinness, D.L. (2000). "Conceptual Modeling for Distributed Ontology Environments," in Proceedings of The Eighth International Conference on Conceptual Structures Logical, Linguistic, and Computational Issues (ICCS 2000), Darmstadt, Germany, August 14-18.

McGuinness, D.L. (2001). "Ontologies Come of Age", in D. Fensel, J. Hendler, H. Lieberman, and W. Wahlster, (eds.) The Semantic Web: Why, What, and How, Cambridge: MIT Press.

![](/api/attachments/TQ3CWWKV/fulltext/images/67a262448b4b408b50c9a116400ba7762d18d5a2f3ecb9e3dc9b38f07a102527.jpg)

Merriman, W.E., and M Tomasellow (1995). Introduction: Verbs Are Words Too. In M. Tomasello and W.E. Merriman (Eds), Beyond Names for Things, (pp. 251-273). Hillsdale, NJ: Erlbaum.

Meyer, M. A. (1992). "How to Apply the Anthropological Technique of Participant Observation to Knowledge Acquisition for Expert Systems." IEEE Transactions on Systems, Man and Cybernetics 22 (5) pp.983-991.

Musen, M. (1992). "Dimensions of Knowledge Sharing and Reuse", Computers and Biomedical Research, 25 pp. 435-467.

Nardi, B. (1996). "The Use of Ethnographic Methods in Design and Evaluation" In M.G. Helander, T. Landauer, and P. Prabhu (eds). Handbook of Human-Computer Interaction II. Amsterdam: Elsevier

Norris, J., and M. Powell, M. Vona, P., Backes (2005). Mars Exploration Rover Operations and the Science Activity Planner. Proceedings of the 2005 IEEE

International Conference on Robotics and Automation, Barcelona, Spain, pp 4629-4634.

Proceedings of the Computer-Supported Collaborative Argumentation for Learning Communities Workshop. Palo Alto, CA. http://kmi.open.ac.uk/people/sbs/csca/cscl99/papers.html

Quine, W.V.O. (1963). From a Logical Point of View, New York: Harper.

Sacerdoti, E.D. (1977). A Structure for Plans and Behavior, New York: Elsevier.

Schank, R. (1975). Conceptual Information Processing. Amsterdam: North Holland.

Searle, J.R. (2002). The Rediscovery of Mind. Cambridge: MIT.

Searle, J.R. (2002). Consciousness and Language. Cambridge, UK: Cambridge University Press.

Shalin, V.L. (2005). The Roles of Humans and Computers in Distributed Planning for Complex, Dynamic Domains. To appear in Cognition, Technology and Work.

Shalin, V.L. (in prep). Development of Work Methods in Novel Tasks.

Shalin, V.L. and P. McCraw (2003). Representations for Distributed Planning. In E. Hollnagel (ed.) Handbook of Cognitive Task Design.) New Jersey: LEA. (pp. 701-725 Spradley, J. (1980). Participant Observation. Fort Worth: Holt, Rhinehart and Winston.

Strauss A. and J. Corbin (1990). Basics of Qualitative Research: Grounded Theory Procedures and Techniques, London: Sage.

Suchman, L. (1987). Plans and Situated Actions. Cambridge, UK: Cambridge University Press

Wales, R., J. O'Neill, and Z. Mirmalek (2002). "Ethnography, Customers and Negotiated Interactions at the Airport", in special issue on Human Centered

Computing at NASA. IEEE Intelligent Systems Journal 17(5), pp.15-23.

Zhan, C-X, C-G Cao, F. Gu, and J-X Si (2004). Domain Specific Formal Ontology of Archaeology and Its Application in Knowledge Acquisition and Analysis. Journal of Computer Science and Technology, 19(3), 290-301.

Zhang, P. and N. Li (2005). The Intellectual Development of Human-Computer Interaction Research: A critical assessment of the MIS literature (1990-2002). Journal of the Association for Information Systems, 6, 227-292.

<table><tr><td colspan="3">Table A1 Instrument Locations on the Rover</td></tr><tr><td>Type of Instrument and Location</td><td>Name</td><td>Definition</td></tr><tr><td>Engineering instruments on Rover body</td><td>Navcam</td><td>Navigational cameras</td></tr><tr><td></td><td>Hazcam</td><td>Hazard Avoidance cameras</td></tr><tr><td>Remote Sensing Instruments on Rover Mast</td><td>Pancam</td><td>High Resolution Panorama Cameras</td></tr><tr><td></td><td>MiniTES</td><td>Mini Thermal Emission Spectrometer</td></tr><tr><td>Instruments for Gathering In-situ Data on Instrument Deployment Device (IDD)</td><td>MI</td><td>Microscopic Imager camera</td></tr><tr><td></td><td>APXS</td><td>Alpha Particle Xray Spectrometer</td></tr><tr><td></td><td>MB</td><td>Mössbauer</td></tr><tr><td></td><td>RAT</td><td>Rock Abrasion Tool</td></tr></table>

<table><tr><td colspan="2">Table A2. Single and Multiple Instrument Observations</td></tr><tr><td>Observation Type</td><td>Name (shorthand)</td></tr><tr><td>Single Instrument</td><td>APXS, Hazcam (Haz), Mössbauer (MB), Microscopic Imager (MI), MiniTES, Navcam (Nav), Pancam, RAT, Rover</td></tr><tr><td>Multiple Instrument</td><td>Instrument Deploy Device (IDD) [in-situ] Pancam Mast Assembly (PMA) [remote sensing]</td></tr></table>

<table><tr><td colspan="3">Table A3. In-situ Instruments and relationship between Instruments, Features and Targets</td></tr><tr><td># of Inst.</td><td>One Feature</td><td>Multiple Features</td></tr><tr><td rowspan="2">One Inst.(Use instrument or shorthand name)</td><td>Include feature nameMB Boulder</td><td>(Not Possible)</td></tr><tr><td>Include feature name and relation or method for grouping unmentioned targets with featureMB_Sniff_Boulder</td><td>Include one or two feature names and relation or method for grouping unmentioned targets with featuresAPXS_comparison_Boulder_ShipsProw</td></tr><tr><td rowspan="2">Multiple Inst.(Use IDD instrument class name)</td><td>Include feature nameIDD_Boulder_</td><td>(Not Possible)</td></tr><tr><td>Include feature name and relation or method for grouping unmentioned targets with featureIDD_Survey_Boulder</td><td>(Separate Observations)</td></tr></table>

![](/api/attachments/TQ3CWWKV/fulltext/images/6bce670e4882681fada536e7ff713884870b1f9a6cc9f18c3e190222f2762c62.jpg)

<table><tr><td colspan="2">Appendix A: List of Acronyms</td></tr><tr><td>APXS</td><td>Alpha Particle X-ray Spectrometer</td></tr><tr><td>FIDO</td><td>Field Integrated Design and Operations</td></tr><tr><td>Hazcam</td><td>Hazard Avoidance Camera</td></tr><tr><td>IDD</td><td>Instrument Deployment Device</td></tr><tr><td>JPL</td><td>Jet Propulsion Laboratory</td></tr><tr><td>MB</td><td>Mössbauer Spectrometer</td></tr><tr><td>MER</td><td>Mars Exploration Rover</td></tr><tr><td>MI</td><td>Microscopic Imager</td></tr><tr><td>Mini-TES</td><td>Miniature Thermal Emission Spectrometer</td></tr><tr><td>MTES</td><td>Miniature Thermal Emission Spectrometer</td></tr><tr><td>Navcam</td><td>Navigational Camera</td></tr><tr><td>Pancam</td><td>Panoramic Camera</td></tr><tr><td>PMA</td><td>Pancam Mast Assembly</td></tr><tr><td>PUL</td><td>Payload Uplink Lead</td></tr><tr><td>RAT</td><td>Rock Abrasion Tool</td></tr><tr><td>SAP</td><td>Science Activity Planner</td></tr><tr><td>SOWG</td><td>Science Operations Working Group</td></tr></table>

## About the Authors

Roxana C. Wales, Ph.D., currently at Google, was a senior human-centered computing research scientist with SAIC at the NASA Ames Research Center when this work was done. As an ethnographer focused on work system design and evaluation, she is especially interested in revealing explicit as well as implicit information in technological settings that is essential for creating better work systems and supporting technology use within expert domains. At NASA, she also worked on projects in Mission Control at Johnson Space Center, for both the International Space Station and the Space Shuttle, and conducted a two and a half year study of airline and airport operations and delays.

Valerie L. Shalin Ph.D. is currently an Associate Professor in the Department of Psychology at Wright State University, and has held positions at SUNY Buffalo Department of Industrial Engineering and Honeywell Systems and Research Center. She has examined workplace cognition in aerospace systems, medicine and military domains, and has numerous journal articles, book chapters, and proceedings papers in the area of human workplace expertise and associated empirical and analytic methods to support the design and evaluation of workplace aiding and training technology.

Deborah S. Bass, Ph.D. currently works at the NASA Jet Propulsion Laboratory, where she was the Deputy Science Team Chief for the Mars Exploration Rover (MER) Project. Dr. Bass is now the Deputy Project Scientist for the 2007 Mars Lander, Phoenix. She received her PhD from the University of California at Los Angeles, and her science expertise focuses on Mars polar geology, with an emphasis on water transport in and out of the polar regions.

ISSN: 1536-9323

Editor

Kalle Lyytinen
Case Western Reserve University, USA

<table><tr><td colspan="4">Senior Editors</td></tr><tr><td>Izak Benbasat</td><td>University of British Columbia, Canada</td><td>Robert Fichman</td><td>Boston College, USA</td></tr><tr><td>Varun Grover</td><td>Clemson University, USA</td><td>Rudy Hirschheim</td><td>Louisiana State University, USA</td></tr><tr><td>Juhani livari</td><td>University of Oulu, Finland</td><td>Elena Karahanna</td><td>University of Georgia, USA</td></tr><tr><td>Robert Kauffman</td><td>University of Minnesota, USA</td><td>Frank Land</td><td>London School of Economics, UK</td></tr><tr><td>Bernard C.Y. Tan</td><td>National University of Singapore, Singapore</td><td>Yair Wand</td><td>University of British Columbia, Canada</td></tr><tr><td colspan="4">Editorial Board</td></tr><tr><td>Ritu Agarwal</td><td>University of Maryland, USA</td><td>Steve Alter</td><td>University of San Francisco, USA</td></tr><tr><td>Michael Barrett</td><td>University of Cambridge, UK</td><td>Cynthia Beath</td><td>University of Texas at Austin, USA</td></tr><tr><td>Anandhi S. Bharadwaj</td><td>Emory University, USA</td><td>Francois Bodart</td><td>University of Namur, Belgium</td></tr><tr><td>Marie-Claude Boudreau</td><td>University of Georgia, USA</td><td>Tung Bui</td><td>University of Hawaii, USA</td></tr><tr><td>Yolande E. Chan</td><td>Queen&#x27;s University, Canada</td><td>Dave Chatterjee</td><td>University of Georgia, USA</td></tr><tr><td>Roger H. L. Chiang</td><td>University of Cincinnati, USA</td><td>Wynne Chin</td><td>University of Houston, USA</td></tr><tr><td>Ellen Christiaanse</td><td>University of Amsterdam, Nederland</td><td>Guy G. Gable</td><td>Queensland University of Technology, Australia</td></tr><tr><td>Dennis Galletta</td><td>University of Pittsburg, USA</td><td>Hitotora Higashikuni</td><td>Tokyo University of Science, Japan</td></tr><tr><td>Matthew R. Jones</td><td>University of Cambridge, UK</td><td>Bill Kettinger</td><td>University of South Carolina, USA</td></tr><tr><td>Rajiv Kohli</td><td>Colleage of William and Mary, USA</td><td>Chidambaram Laku</td><td>University of Oklahoma, USA</td></tr><tr><td>Ho Geun Lee</td><td>Yonsei University, Korea</td><td>Jae-Nam Lee</td><td>Korea University</td></tr><tr><td>Kai H. Lim</td><td>City University of Hong Kong, Hong Kong</td><td>Mats Lundeberg</td><td>Stockholm School of Economics, Sweden</td></tr><tr><td>Ann Majchrzak</td><td>University of Southern California, USA</td><td>Ji-Ye Mao</td><td>Remnin University, China</td></tr><tr><td>Anne Massey</td><td>Indiana University, USA</td><td>Emmanuel Monod</td><td>Dauphine University, France</td></tr><tr><td>Eric Monteiro</td><td>Norwegian University of Science and Technology, Norway</td><td>Jonathan Palmer</td><td>College of William and Mary, USA</td></tr><tr><td>B. Jeffrey Parsons</td><td>Memorial University of Newfoundland, Canada</td><td>Paul Palou</td><td>University of California, Riverside, USA</td></tr><tr><td>Yves Pigneur</td><td>HEC, Lausanne, Switzerland</td><td>Nava Pliskin</td><td>Ben-Gurion University of the Negev, Israel</td></tr><tr><td>Jan Pries-Heje</td><td>Copenhagen Business School, Denmark</td><td>Dewan Rajiv</td><td>University of Rochester, USA</td></tr><tr><td>Sudha Ram</td><td>University of Arizona, USA</td><td>Balasubramaniam Ramesh</td><td>Georgia State University, USA</td></tr><tr><td>Suzanne Rivard</td><td>Ecole des Hautes Etudes Commerciales, Canada</td><td>Timo Saarinen</td><td>Helsinki School of Economics, Finland</td></tr><tr><td>Rajiv Sabherwal</td><td>University of Missouri, St. Louis, USA</td><td>Olivia Sheng</td><td>University of Utah, USA</td></tr><tr><td>Ananth Srinivasan</td><td>University of Auckland, New Zealand</td><td>Katherine Stewart</td><td>University of Maryland, USA</td></tr><tr><td>Kar Yan Tam</td><td>University of Science and Technology, Hong Kong</td><td>Dov Te&#x27;eni</td><td>Tel Aviv University, Israel</td></tr><tr><td>Viswanath Venkatesh</td><td>University of Arkansas, USA</td><td>Richard T. Watson</td><td>University of Georgia, USA</td></tr><tr><td>Bruce Weber</td><td>London Business School, UK</td><td>Richard Welke</td><td>Georgia State University, USA</td></tr><tr><td>Youngjin Yoo</td><td>Temple University, USA</td><td>Kevin Zhu</td><td>University of California at Irvine, USA</td></tr><tr><td colspan="4">Administrator</td></tr><tr><td>Eph McLean</td><td>AIS, Executive Director</td><td colspan="2">Georgia State University, USA</td></tr><tr><td>J. Peter Tinsley</td><td>Deputy Executive Director</td><td colspan="2">Association for Information Systems, USA</td></tr><tr><td>Reagan Ramsower</td><td>Publisher</td><td colspan="2">Baylor University</td></tr></table>
