---
otero_id: 8338
otero_key: "R6AMEZPR"
title: "Delineating ‘Pervasiveness’ in Pervasive Information Systems: A Taxonomical Framework and Design Implications"
authors: "Panos E Kourouthanassis; George M Giaglis; Dimitrios C Karaiskos"
year: "2010"
journal: "Journal of Information Technology"
doi: "10.1057/jit.2009.6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research article

# Delineating ‘pervasiveness’ in pervasive information systems: a taxonomical framework and design implications

Panos E Kourouthanassis, George M Giaglis, Dimitrios C Karaiskos

Department of Management Science and Technology, Athens University of Business and Economics, Athens, Greece

Correspondence:

PE Kourouthanassis, Department of Management Science and Technology, Athens University of Business and Economics, Athens, Greece.

Tel: þ 3 02 1082 03855;

Fax: þ 3 02 1082 03682;

E-mail: pkour@aueb.gr

## Abstract

Pervasive Information Systems (IS) exemplify a paradigm where Information Technology is embedded in the physical environment, capable of accommodating user needs and wants when desired. Pervasive IS differ from IS that are based on the desktop paradigm in that they encompass a complex, dynamic environment composed of multiple artifacts, capable of perceiving contextual information and supporting user mobility. Building on the novel properties of pervasive IS, we propose a taxonomical framework assessing the level of ‘pervasiveness’ in a given information system. The framework consists of three interweaving dimensions, namely ubiquity (encompassing mobility and heterogeneity), diffusion (encompassing invisibility and interactivity) and contextual awareness. The framework may be employed either to prospectively inform the design of pervasive IS (by pointing towards pertinent design considerations) or to retrospectively assess the pervasiveness of a system and identify improvement opportunities. We demonstrate both uses, firstly by discussing design priorities for ex ante IS evaluation and secondly by showcasing ex post assessments of a domestic and a corporate pervasive IS. Journal of Information Technology (2010) 25, 273–287. doi:10.1057/jit.2009.6;

Published online 20 July 2010

Keywords: pervasive information systems; design considerations; mobility; context-awareness; invisibility; assessment framework

## Introduction

C <sup>omputing</sup> <sup>is</sup> <sup>becoming</sup> <sup>increasingly</sup> <sup>nomadic,</sup> <sup>pervasive,</sup>and, ultimately, ubiquitous. New technologies, such as and, ultimately, ubiquitous. New technologies, such as ad hoc wireless sensors (Hsin and Liu, 2006), ZigBee (Geer, 2005), wireless mesh networks (Akyildiz et al., 2005), and smart dust micro-sensors (Boukerche et al., 2006), with the support of broadband networks (Sawyer et al., 2003), enable the provision of applications in the physical space beyond the confinements imposed by the desktop computer. Birnbaum (1997) positioned such systems within the Information Systems (IS) discipline paradigm by defining a new class of IS, called Pervasive Information Systems.

Pervasive IS may support both personal and business activities. Kourouthanassis and Giaglis (2008b) provide a taxonomy of pervasive IS and their features by identifying four pertinent application types: personal, domestic, corporate, and public:

\- Personal pervasive IS rely on wearable hardware elements to provide a fully functional computing experience wherever the user might be. Typical examples include biomedical monitoring systems (Jafari et al., 2005), human detection systems (Smith et al., 2005), and remote plant operation systems (Najjar et al., 1997).

\- Domestic pervasive IS automate tasks that otherwise require human supervision in the household (e.g. heating and lightning control, monitoring the home inventory, and so on). Typical examples include MIT’s Home of the Future initiative (Intille, 2002) and the Aware Home (Kidd et al., 1999).

\- Corporate pervasive IS support enterprise-wide activities, such as supply chain management [e.g. warehouse and logistics management (Prater et al., 2005)], workforce management [e.g. sales force automation (Alt and Puschmann, 2005) and office support (Churchill et al., 2003)], and customer relationship management (Fano and Gershman, 2002; Kourouthanassis, 2004).

\- Public pervasive IS craft interactive environments in public places. Examples include wireless museum guides (Hsi and Fait, 2005) and mobile information devices in hospitals (Liszka et al., 2004) to name but a few popular applications.

Designing such pervasive environments presents novel challenges compared to the design of traditional, desktopbased, IS. The pervasive space introduces a multiplicity of engineering, social, organizational, and application-specific challenges that need to be addressed during the design process. In effect, over the past few years, pervasive IS urged an independent research stream within the IS discipline in which design is considered as one of the most important research activities [c.f. (Abowd and Mynatt, 2000; Abowd et al., 2002; Lyytinen and Yoo, 2002a b; Roussos, 2003; Lyytinen et al., 2004; Streitz et al., 2005)]. Within this stream of research, emphasis is given to detecting design challenges that need to be addressed during the development of pervasive IS. These challenges stem from the novel features of pervasive IS, both in terms of interactivity between users and the system and the level and mechanics of infrastructural support, which motivate researchers to devise new tools, methods, or practices that streamline and facilitate the design process.

There are usually two alternative prevailing viewpoints regarding the design of pervasive IS:

\- The first viewpoint suggests that the design of pervasive IS should be studied horizontally. Underlying this assertion lies the assumption that all pervasive IS instances share common design challenges, therefore they all require common design considerations. These considerations may holistically encompass the entire class of pervasive IS [e.g. in the form of design theories for pervasive IS (Kourouthanassis and Giaglis, 2006)] or they may focus on a single design dimension only, such as engineering design (Estrin et al., 2002; Want and Perring, 2005), interaction design (Thackara, 2001; Abowd et al., 2002), or social design (Langheinrich, 2001; Beckwith, 2003).

\- The second viewpoint suggests that the design of pervasive IS should be studied vertically, depending on their application domain. Along this line, researchers have formulated principles governing the design of domestic pervasive IS (Intille, 2002; Rodden and Benford, 2003), wearable pervasive IS (Smailagic and Siewiorek, 2002), and public pervasive IS (Kostakos and O’Neill, 2004), to name but a few examination areas.

Both viewpoints assume that the proposed design principles and corresponding design solutions may be applied to all pervasive IS that fall under their investigation lenses. These design principles are usually tailored to the challenges imposed by the pervasive nature of each IS class. Nevertheless, it is not necessarily true that all pervasive IS share the same level of ‘pervasiveness’. In effect, it might be misleading to distinguish between only two extremes: ‘pervasive’ and ‘non-pervasive’ IS. Most pervasive systems will vary on their degree of ‘pervasiveness’, whether the latter is defined as the level of support by pervasive technologies or the degree to which a system enables a time- and space-agnostic user experience. For example, a pervasive warehouse management system (McKelvin et al., 2005) might require less support for perceiving environmental stimuli compared to a pervasive customer relationship management system (Cumby et al., 2005)

aspiring to assist customers during their shopping. Although both may be classified under the corporate pervasive IS class, design choices are logically expected to differ between them.

Framing the determinant factors of pervasiveness has recently been a debatable topic for the IS community. Lyytinen and Yoo (2002a) described the pervasiveness degree of an IS type as a combination of its level of mobility and its level of information technology (IT) embeddedness into the physical space. The same authors have later added digital convergence, assessing IT artifact heterogeneity in a pervasive environment (Lyytinen and Yoo, 2002b). Building on this work, Junglas and Watson (2006) have proposed four constructs that collectively characterize IS pervasiveness: ubiquity, uniqueness, universality, and unison. Such efforts are however limited to the identification of appropriate factors, without discussing their implications to the design and implementation of a pervasive IS.

This article aims at advancing the IS community’s thinking towards defining design theories for pervasive IS by providing a first and important step towards this direction: defining ‘pervasiveness’ and assessing its implications on pervasive IS design choices. To this end, we propose a framework delineating the dimensions of pervasiveness for any given IS. The following section presents the novel properties of pervasive IS and aggregates their emerging design challenges. Pervasiveness in pervasive IS: A consolidated framework section presents the proposed framework and discusses how it may be applied during the initial stages of the design process to propose pertinent design considerations (Using the framework to perform ex ante evaluations of pervasive IS section) and as an assessment tool in a deployed pervasive IS to identify prospective improvement fields (Using the framework to perform ex post assessments of pervasive IS section). The final section concludes the article by summarizing our contribution and discussing future research directions.

## Pervasive IS: Theoretical background and design challenges

A pervasive environment is likely to be manifested by multiple heterogeneous IT artifacts, ranging from laptops and mobile phones to smart sensors and information appliances. These interconnected artifacts may be diffused in their surrounding environment, working together to sense, process, store, and communicate information to ubiquitously and unobtrusively support user tasks and activities. The novel characteristics of pervasive IS can be summarized to the following:

## Extension of traditional computing boundaries

Pervasive IS represent the third wave of computing where, ultimately, every person interacts with many computers or computerized artifacts (Weiser, 1993). This characteristic expands the design canvas for the system architect. Whereas in desktop environments the designer needs to include as much as possible of the physical space to the virtual world (implying the hardware and software), the ubiquitous nature of pervasive IS brings in an additional factor during the design process: efficient manipulation of the existing physical architecture in terms of smoothly embedding the supporting infrastructure of the pervasive system. Satyanarayanan (2001) characterized this blending of the physical with the virtual as ‘effective use of smart spaces’. Moreover, the system users are transformed from stationary to nomadic, while the environment senses their actions and responds accordingly. As Weiser (1994) stated ‘the [computing] world is no [longer] the desktop’. Instead, the physical world becomes the desktop as buildings, places, and infrastructures are augmented with IT crafting dynamic interactive environments.

## Invisibility and unobtrusiveness

Hiding the IT infrastructure and making it an indistinguishable part of the environment surfaces a notion of living with IT rather than simply using it. We therefore need to distinguish among physical invisibility, referring to the gradual disappearance of IT into the physical space, and cognitive invisibility, referring to a change in human mentality in accepting IT as granted, part of their lifeworld. Researchers have named this notion calm technology (Weiser and Brown, 1998) or slow technology (Hallnas and Redstrom, 2001). Moreover, opposed to a desktop environment where the user is always actively involved with the system, pervasive IS may be capable of supporting implicit users that may not even be aware that such a system exists.

## Context awareness

One of the most important novel characteristics that pervasive IS introduce is the notion of context awareness. By understanding the properties of context, designers of pervasive IS will be able to choose what information to use and provide insights into the types of data that need to be supported and the abstractions and mechanisms required to support context-aware computing. Contextual awareness also implies that sensing artifacts should be able to effectively communicate the information they collect and process as well as trigger events they deem necessary to support pervasive IS users. Opposed to desktop-based systems where the user initiates the interaction with the system, pervasive IS are always active, continuously collecting contextual information, and pro-acting (rather than re-acting) to the needs and demands of the users.

## Multi-modal interaction

As pervasive IS deal with non-traditional computing devices, the desktop should be considered as just ‘another access device’. Consequently, conventional HCI design methods and interaction schemes may be inappropriate for pervasive IS because the physical interactions between users and the system will, most certainly, not resemble the prevailing keyboard/mouse/display paradigm. In effect, pervasive IS may simulate the way that humans interact with the physical world. Abowd and Mynatt (2000) argue that as humans speak, gesture, and use writing utensils to communicate with other humans and alter physical artifacts, such actions can and should be used as explicit or implicit input to pervasive IS. Burkey (2000) argues that the next step in this progression refers to environmental interfaces, where the environment is the interface and the user exists in it. Eventually, human–computer interaction will be transformed to artifact-to-artifact interaction and human-to-human interaction. Thus, apart from solely physical interactions with the system, pervasive IS may also incorporate elements of ambient interactions with devices, objects, or displays from the physical space (Dodgson, 2005; Maes, 2005).

## Heterogeneity of pervasive artifacts

A pervasive environment is likely to be manifested by diverse IT artifacts that differ in terms of size, shape, and functionality. The diversity and plurality of pervasive artifacts poses new challenges for information delivery applications in this environment. To meet the demands in this heterogeneous environment, it is necessary for the information to be customized or tailored according to user preferences, client capabilities, and network characteristics (Held et al., 2002). As such, pervasive IS usually incorporate an adaptation mechanism that can accommodate all different types of adaptations between different formats. Several such mechanisms have already been proposed in the literature [e.g. (Mohan et al., 1999; Ponnekanti et al., 2001; Gajos and Weld, 2004; Hirschfeld and Kawamura, 2004; Cao et al., 2005)] providing the system designer with the option to select the most appropriate for the specific system requirements.

The points above might induce the perception that pervasive IS, and consequently their design, are primarily an HCI-related research stream. We argue that this is not the case for the following reasons:

\- First, the operation of a pervasive system requires the development of supporting infrastructures that are capable of managing a complex environment consisting of heterogeneous devices, diverse information requirements, and multiple users. Therefore, the design of pervasive IS should also be influenced by principles and ideas stemming from such research fields as operating systems, software engineering, and information modeling to name but a few popular IS research areas.

\- Second, pervasive IS are purposeful systems; they may be deployed in domestic, corporate, or public spaces providing a particular type of functionality with humans being the direct or indirect beneficiaries of their functionality. As a result, the design of a pervasive IS should also be directed by the requirements, opportunities, and limitations of the application domain as well as the requirements raised by the system’s prospective stakeholders (users and system owners).

Each novel characteristic raises one or more design challenges that should be addressed during the development of pervasive IS. Table 1 aggregates the most important of these challenges and proposes pertinent design solutions for each. A more detailed presentation of pervasive IS design challenges is available in Kourouthanassis and Giaglis (2008a).

A pervasive system is likely to face one or more of these design challenges. However, their weight and importance is dependent on a number of factors that determine the requirements of the application domain for pervasiveness support. For example, the design of a pervasive system supporting corporate employees might need to emphasize on aspects related to increased mobility and interactivity, while the design of a pervasive museum guide might focus on elements related to the perception and management of contextual information and effective placement of the pervasive artifacts to the physical space. Therefore, we posit that designers of pervasive systems might benefit from a consolidated framework that prioritizes each design challenge and facilitates the process of selecting pertinent design solutions.

<table><tr><td>Novel characteristic</td><td>Design challenge</td><td>Candidate design solution</td></tr><tr><td rowspan="3">Extension of traditional computing boundaries</td><td>Increased mobility and continuous connectivity.</td><td>Provision of connectivity and mobility support within the boundaries of the system by employing multiple wireless/mobile networks.</td></tr><tr><td>Quality-of-service and wireless networks management.</td><td>QoS management centrally, through the pervasive middleware, based on established methods or models [e.g. QADA (Matinlassi et al., 2002)]. Implementation of middleware platforms managing network handovers.</td></tr><tr><td>Support for secure wireless information exchange.</td><td>Wireless encryption techniques and protocols (e.g. WEP). Auditing mechanisms preventing unauthorized access and use of any system component.</td></tr><tr><td rowspan="2">Invisibility and unobtrusiveness</td><td>Smooth embedment of pervasive artifacts in the physical space.</td><td>Augmentation of everyday life objects with computing capabilities [e.g. (Kawsar et al., 2005; Maes, 2005)].</td></tr><tr><td>Concealment of pervasive artifacts from users&#x27; consciousness.</td><td>Design for emotions by incorporating aesthetical attributes to the pervasive artifacts (Hallnas and Redstrom, 2002). Design information-augmented architectural spaces which incorporate multi-functional IT artifacts that are highly integrated among them (Travi, 2001).</td></tr><tr><td rowspan="4">Context-awareness</td><td>Location aware computing.</td><td>Selection of an appropriate mechanism to identify current user location [e.g. (Fox et al., 2003; Ni et al., 2004)]. Zeimpekis et al. (2007) provide a taxonomy of available location identification technologies based on the application area (indoor vs outdoor).</td></tr><tr><td>Perception and communication of contextual information.</td><td>Design of architectures supporting and coordinating wireless sensor networks.</td></tr><tr><td>Uniform context representation and coordinated communication among the system components.</td><td>Implementation of context toolkits or architectures that use a common representation format for contextual information, and coordinate/manage contextual information among the system components [e.g. MARS (Cabri et al., 2002) and Context Shadow (Jonsson, 2002)].</td></tr><tr><td>Implementation of privacy management schemes.</td><td>Design of context toolkits/solutions taking into account established privacy-by-design pervasive IS principles [e.g. (Langheinrich, 2001, 2002)].</td></tr><tr><td rowspan="2">Multi-modal interaction</td><td>Support for multiple concurrent interaction modalities.</td><td>Design of centralized or distributed schemes capable of handling conventional or more natural interaction schemes.</td></tr><tr><td>Adaptation of information resources to the capabilities of the access device or interaction modality.</td><td>Provision of adaptation mechanisms that generate user interfaces based on knowledge of the capabilities of the target display [e.g. PUC (Nichols et al., 2004) and SUPPLE (Gajos and Weld, 2004)]. These adaptation mechanisms may be incorporated in a middleware platform.</td></tr><tr><td rowspan="2">Heterogeneity of pervasive artifacts</td><td>Support for coordination and communication among heterogeneous devices, IT artifacts, and system components.</td><td>Centralized and coordinated artifacts and system components management through meta-models or abstractions incorporated in middleware solutions [e.g. Gaia (Roman et al., 2002b) and Aura (Sousa and Garlan, 2002)]. Such support may be provided through the deployment of pervasive middleware software.</td></tr><tr><td>Dynamic discovery and registration of new IT artifacts.</td><td>Dynamic wireless discovery schemes that utilize established communication and connection protocols such as Universal Plug-and-Play (UpnP) (Jeronimo and Weast, 2003) and Apple&#x27;s Bonjour (Apple, 2006). Development of standards supporting universal user interface development and user interface remoting.</td></tr></table>

## Pervasiveness in pervasive IS: A consolidated framework

The proposed framework attempts to capture the required level of support by pervasive technologies for a given application environment. In effect, as argued in the Introduction section of the article, it is not true that all instances of pervasive systems would share the same design requirements. We propose that pervasive IS should be perceived as a continuum among three examination dimensions that determine the degree of ‘pervasiveness’ for any pervasive system: diffusion, ubiquity, and context awareness:

\- Diffusion assesses the extent to which the system consists of hidden components in the physical space and the extent to which interaction is performed through natural interfaces. Hence, diffusion can be further decomposed into the elements of invisibility and interactivity.

\- Ubiquity assesses the system’s capability of providing users with continuous access to information resources irrespective of their location within the system’s boundaries and the system’s capability of providing its services through multiple access devices. Hence, ubiquity can be further decomposed into the elements of mobility and heterogeneity.

\- Context awareness assesses the system’s capability of perceiving contextual information regarding the user, the system, and the environment to dynamically and proactively adapt its functionality accordingly.

Figure 1 illustrates the five detailed dimensions of pervasiveness for a fully pervasive IS instance.

The framework has been conceived as a scorecard tool that features a set of measurable perspectives that collectively determine the degree of pervasiveness for any pervasive IS. Each perspective, or pervasiveness dimension, is associated with a specific value that may help designers devise an appropriate development strategy for that particular dimension based on its weight and importance. In essence, the proposed framework helps designers calibrate their design strategy by allocating priorities based on the inherent application-specific requirements. Table 2 provides definitions for each dimension of the framework, identifies the value ranges per dimension, and suggests indicative criteria that may be employed to rate each dimension.

![](/api/attachments/R6AMEZPR/fulltext/images/e0274c7be18057ea2b751c7c151907486669a78f63a61a72ada963ff07bec20f.jpg)  
Figure 1 A framework for assessing the degree of pervasiveness for pervasive IS.

In practice, the framework may be applied to perform two distinct types of assessment in a pervasive environment. During an a priori (or ex ante) evaluation, the framework may be employed to assess the pervasiveness requirements of a pervasive environment and to extrapolate pertinent design considerations. Pervasiveness requirements may be collected by following any requirements engineering method. During an a posteriori (or ex post) assessment, the framework may be applied to assess the pervasiveness of an IS instance and identify areas of improvement. In this context, designers may evaluate the design choices of the pervasive IS in question under the five dimensions of the framework and determine improvements based on design best practices of other similar pervasive IS instantiations. Moreover, designers may evaluate whether the design choices of a deployed pervasive IS meet the actual requirements for pervasiveness support of the application domain. In this particular assessment type, designers may compare the a priori and a posteriori assessments of a pervasive IS and spot deviations between the targeted and the implemented design choices.

Scoring of each dimension may be performed either objectively of perceptually. An objective allocation of scores on each dimension suggests that designers evaluate the pervasive system based on the classification criteria per dimension. Hence, a pervasive system that supports multiple access devises and incorporates many sensor technologies may be considered as more heterogeneous compared to a system that exhibits fewer instances. Conversely, a perceptual allocation of scores on each dimension requires the development of a psychometric instrument that provides scales for each pervasiveness dimension. Such an instrument may comprise of a questionnaire assessing each pervasiveness dimension based on specific items. The system users or designers, depending on the evaluation type, will consist of the target sample. A preliminary work towards this objective is available in Karaiskos et al. (2009) who have developed specific constructs with measurement items assessing each pervasiveness dimension.

The following sections discuss both approaches regarding the applicability and utility of the proposed framework:

## Using the framework to perform ex ante evaluations of pervasive IS

During the a priori evaluation of a pervasive IS the designer may apply the proposed framework to capture the requirements for pervasive support for the given application domain. The design options vary depending on the examined dimension of the framework. The following paragraphs discuss the available design strategies per dimension:

Table 2 Determining dimensions for the pervasive nature of pervasive IS

<table><tr><td>Pervasiveness dimension</td><td>Definition</td><td>Value ranges</td><td>Indicative classification criteria</td></tr><tr><td colspan="4">Ubiquity</td></tr><tr><td>Mobility</td><td>The extent to which the system provides users with access to information resources irrespective of their location within the system&#x27;s boundaries.</td><td>Localized to mobile</td><td>Degree of coverage by wireless or mobile network.Quality-of-service (QoS) at the wireless network&#x27;s edges.</td></tr><tr><td>Heterogeneity</td><td>The system&#x27;s ability to provide its functionality to diverse device types and IT artifacts within its environment.</td><td>Homogeneous to heterogeneous</td><td>Number and diversity of access devices.Support for multiple operation systems types.Support for diverse sensor technologies.Degree of integration among device types and IT artifacts.Degree of coordination among device types and IT artifacts.</td></tr><tr><td colspan="4">Diffusion</td></tr><tr><td>Interactivity</td><td>The system&#x27;s capability of providing alternative means of interaction with its resources.</td><td>Uni-modal interaction to multi-modal interaction</td><td>Number and types of interaction modalities.Support for interactions through natural interfaces (tangible, speech-based, and so on).</td></tr><tr><td>Invisibility</td><td>The degree to which the system enables the disappearance of IT resources from user consciousness, promoting minimal user distraction.</td><td>Conspicuous to invisible</td><td>Usability of interaction modalities and perceived distraction for users.Degree of artifact embedment to the physical space.Degree of conformance to the existing physical architecture/degree of changes evoked to the existing physical architecture.</td></tr><tr><td>Contextual awareness</td><td>The system&#x27;s capability of perceiving, managing, and communicating contextual information (user-related, systemic, or environmental) and dynamically adapting its functionality based on contextual changes. Also implies the degree to which the system automatically triggers an action or event based on contextual stimuli to fulfill user needs.</td><td>Context-agnostic to context-conscious</td><td>Variety of supported contextual information.Degree of processing and communication of the perceived contextual information.Support for cumulative and temporal processing of contextual information.Degree of adaptation to contextual changes.Number of tasks and activities fulfilled without user exhortation.</td></tr></table>

## Dimension 1: Mobility

Pervasive networks represent the backbone infrastructure of any pervasive system supporting mobility within its boundaries. Luff and Heath (1998) identify three types of mobility requirements for pervasive systems: micro mobility, local mobility, and remote mobility. Micro mobility supports interactions that relate to our bodily experience. Local mobility involves interactions within individuals and artifacts within a given space. Finally, remote mobility supports synchronous and asynchronous communications among people in distant locations. In any case, the degree of mobility for pervasive IS is application-dependent. For example, individuals performing maintenance operations in a factory using a wearable computer might require very short-range coverage, whereas users of a smart museum guide [exhibiting functionality similar to the prescriptions of Cheverst et al. (2000)] might require increased support for mobility within the premises of the museum. Designers of pervasive IS might select among the following types of networks and corresponding technologies to support mobility within the system’s boundaries:

\- Wireless Personal Area Networks (WPANs) aim to connect different devices (sensors, actuators, Personal Digital Assistant (PDAs), and so on) that a user carries or wears. Ashok and Agrawal (2003) characterize PANs as ‘on-body networks’ mainly because of their capability to support wearable computing applications. The most common PANs wireless technologies are Infrared (IrDA) (Ashok and Agrawal, 2003), Bluetooth (Buttery and Sago, 2003), and ZigBee (Schindler, 2004).

\- Wireless Local Area Networks (WLANs) are capable of supporting medium-range connections among different devices. They constitute the de facto substitute of wired Ethernet connections especially in terms of interconnecting indoor environments. The most common WLAN technologies are the IEEE 802.11 family of protocols and HiperLAN2 (Lenzini and Mingozzi, 2001).

\- Wireless Metropolitan Area Networks (WMANs) provide LAN-like services, but in a wider coverage extent, such as an entire city. They aim to provide inexpensive broadband access to nomadic or stationary users acting as a replacement of conventional wired last-mile access systems. Common WMAN technologies are IEEE 802.16 or WiMAX (Hoymann, 2005), and Terrestrial Trunked Radio system (Dunlop et al., 1999).

\- Wireless Wide Area Networks (WWANs) support remote connectivity among individuals and corporate systems through mainly cellular (mobile) networks such as GPRS and UMTS.

The application requirements for mobility should instruct designers to select the most appropriate solution. Pervasive systems that require a higher degree of mobility within their boundaries might oblige designers to select a combination of network technologies that provide extended geographical coverage, such as multiple WLANs or a WMAN. In this case, designers should also devise mechanisms to support the efficient management and coordination of the deployed networks. The design of highly mobile systems might require the development of a middleware platform handling all network connections, whereas the design of more localized systems might meet connectivity requirements on an ad hoc basis. Finally, security should be viewed as a horizontal design challenge for any pervasive IS irrespective of their mobility requirements. Security challenges for pervasive environments refer to system/service availability (denial of service, signal jamming), authentication and authorization, access control, secure service discovery, and trust management. Each networking technology proposes its own encryption protocol that aims to secure as much as possible the wireless infrastructure. A short list of available encryption techniques for wireless networks can be collec tively found in Hu et al. (2005). Along the same line, Haque and Ahamed (Haque and Ahamed, 2006) provide a thorough literature review on the existing technologies and practices regarding security management in pervasive spaces.

## Dimension 2: Interactivity

Highly interactive systems might require the deployment of multi-modal interaction schemes that combine a combination of conventional and more natural interface modalities such as human motion and gestures [e.g. (Wexelblat, 1995; Quek et al., 2002; Ward et al., 2002; Benford et al., 2005)], speech [e.g. (Oviatt et al., 2000; Lemon and Gruenstein, 2004)], and tangible or graspable interfaces [e.g. (Plowman and Luckin, 2004; Ullmer et al., 2005)]. The Interactive Workspaces Project is a representative example of a highly interactive pervasive system that augments a dedicated meeting space with large displays, wireless or multi-modal devices, and seamless mobile appliance integration (Johanson et al., 2002). On the opposite, systems with fewer interactivity requirements might allow designers to select an interaction modality that uses a single modality type to provide access to the system’s resources. Of course, interaction in pervasive IS should not assume a uniform range of human perception and motor skills. The design of pervasive interactions should be fully adaptable to the capabilities and sensoral/motor skills of the expected system users. This is particularly true for people that are not familiar with IT or people with disabilities, which may lack the necessary skills to explicitly interact with the system. For these cases, the system should implicitly infer the desired request of the user and proactively trigger an action. Providing system feedback acknowledging or requesting confirmation for a user action that was not comprehended correctly (Lai et al., 2002) or handling errors in the form of a toolkit supporting interface designers (Mankoff et al., 2000) might minimize system misuse and enhance overall accessibility. Still, pervasive IS environments might require self-organizing and selfadaptive capabilities to cope with dynamically changing context environments such as computing contexts and user contexts. These would require the development of interaction approaches that support spontaneous services created on the fly by mobiles or wireless devices that interact by ad hoc connections. The two dominant approaches that appear on pervasive IS literature coping with this challenge are the

Adaptive Services to Client Paradigm and the Spontaneous Service Emergence Paradigm (Bakhouya and Gaber, 2007).

## Dimension 3: Heterogeneity

The multiplicity, diversity and dynamic nature of IT artifacts in a pervasive environment require an integration mechanism that will ensure their efficient communication and management. The development of middleware software is the solution most commonly followed. To meet the emerging requirements of pervasive systems, various software architectures have been proposed: Sahara (Merino, 2005), M-Echo (Raj et al., 2005), TOTA (Mamei and Zambonelli, 2005), Allia (Ratsimor et al., 2004), Middle-Where (Ranganathan et al., 2004), and GAIA (Roman et al., 2002a) are just a few examples. These architectures identify an ‘execution support layer’ that encapsulates the functions of middleware for pervasive applications. Raatikainen et al. (2002) have summarized the architectural qualities that a pervasive middleware should incorporate into the following: adaptability and modifiability, availability and performance, and security. Rasheed et al. (2002) extend these qualities by incorporating also the technical properties of: device discovery; configuration, management and control; Quality-of-service (QoS) and policy management. In all cases, the middleware should provide the necessary support for the application developer in an intuitive and accessible programming model (Biegel and Cahill, 2008). Systems with increased heterogeneity requirements might need the full functionality of the pervasive middleware, whereas systems with limited heterogeneity requirements might enable designers to develop more simplified middleware solutions that incorporate only part of the full-fledged middleware functionality.

At the same time, the heterogeneity of pervasive devices calls for the development of new standards supporting universal interaction among the diverse system components. The existing efforts on this field can be categorized into two groups: universal user interface languages and user interface remoting. The first category refers to the development of abstract user interface descriptions and methods for dynamic service discovery. The second category aims at specifying service discovery frameworks supporting device interoperability using user interface presentation protocols to remote devices. There are multiple technologies enabling universal interaction. The W3C Composite Capabilities/Preferences Profile is one attempt to define a vocabulary capable of describing delivery context (Kiss, 2007). Additional universal interaction technologies include the International Committee for Information Technology Standards Universal Remote Console (INCITS/V2 URC) (LaPlant et al., 2004), the User Interface Markup Language (Helms and Abrams, 2008), the Extensible Interface Markup Language, and the UPnP Remote User Interface standard.

## Dimension 4: Contextual awareness

Designing for contextual awareness implies that a pervasive IS should be capable of perceiving relevant information of its environment, processing it, and adapting to changes in the environment taking into account both historical and current data. Another issue with context-aware pervasive IS is their ability to deal with ambiguity. Dey and Mankoff (2005) proposed a mechanism that enables mediation to imperfectly sensed context. The complexity of the design solution might be instructed by assessing the desired degree for contextual awareness for the application in question. Indicatively, designers may give priorities to the available contextual information of the application domain and propose a scalable architectural solution. For example, designers of MIT’s Home of the Future have considered user location and identity as the most important contextual factors and they have specified the system’s architecture (in terms of sensing artifacts and supporting coordination and management infrastructure) accordingly (Intille, 2002).

## Dimension 5: Invisibility

Designers should devise appropriate means to ensure that IS resources and artifacts are ‘gracefully’ embedded in the physical space. This smooth integration does not suggest that IT should be completely invisible to the system users. On the contrary, we follow Redstrom’s (2001) considerations that pervasive technology should be governed by meaningful presence, promoting unobtrusiveness. Invisibility poses a dilemma. On the one hand, it is desirable to hide the infrastructure of computer technology from its users, because that might just make the pervasive IS easier to use and comprehend. On the other hand, completely obliterating IT may cause frustrations in the form of perceived system exclusion (Kostakos and O’Neill, 2004). Therefore, invisibility should be treated differently; instead of limiting the design effort in hiding pervasive technology from the physical space, we should also focus on hiding the pervasive technology from user consciousness allowing users to interact with the system at an almost subconscious level. Thus, the challenge is to design pervasive IS in such a way that users perceive them as part of the environment. Universal design principles (Story et al., 1998) may be applied to create remembrances allowing for system usage with the minimal distraction. The desired degree of invisibility may dictate the placement of IT artifacts in the pervasive environment and the selected model for user– system interaction. Highly invisible pervasive systems are likely to embed computing capabilities to everyday life objects (Bohn et al., 2003; Kawsar et al., 2005), promote the use of information appliances (Roussos, 2003), and adopt a more natural way of interacting with the system (through speech or gestures) (Abowd et al., 2002). More conspicuous pervasive systems might promote the design of more explicit ways of interacting with the system through stationary IT artifacts (e.g. infokiosks) or mobile IT artifacts that have a clear functionality for their users [e.g. Personal Shopping Assistants (PSA)].

## Using the framework to perform ex post assessments of pervasive IS

The proposed framework may also be applied to assess the current degree of pervasiveness support for an already deployed pervasive system and help designers identify opportunities for further improvement. To demonstrate the applicability of the framework we selected two large-scale pervasive IS that have been considered as reference examples in their field:

\- METRO’s Future Store Initiative, which examines the applicability of the framework in a corporate environment.

\- MIT’s House\_n, which showcases how the framework may be employed to assess the level of support by pervasive technologies in the household.

## METRO’s Future Store Initiative

In 2003, the German retailer METRO unveiled the ‘Future Store’, a converted traditional supermarket embedded with pervasive technologies aiming to make shopping easier and more comfortable for shoppers. The initiative is a joint operation of Metro with IBM, SAP, Intel, T-Systems, and over 60 research and industrial partners. The future store is located in Rheinberg, Germany, and since 2003 it has attracted more than 20,000 international visitors.

From a functional perspective, the Future Store initiative offers a variety of pervasive applications. Shoppers may use a shopping cart equipped with a Tablet PC enabling them to scan the barcodes of items they select and presenting them with valuable information. A wireless network ensures the unobtrusive communication with the backend system accessing the product catalog and active promotional plans while self-service checkouts make payments automatic. The technologies and applications employed include (METRO Future Store, 2006):

\- PSA consisting of a small computer attached to the shopping trolley that facilitates individual shopping. Shoppers scan the products by using an embedded barcode scanner and all respective information is instantly presented in the computer’s display screen. Shoppers initiate their shopping session with the PSA by using their personalized loyalty card (entitled ‘Extra Future Card’). PSA also displays indications of active promotions and special offers while provides also a navigation system enabling fast orientation and instant product location finding within the store.

\- Information Terminals located in strategic places in the store allowing shoppers to scan a product and receive information comprising of ingredients, recipes, alternative, or other meaningful product-related information.

\- Electronic Advertising Displays comprising of flat screens that are efficiently placed in the store highlighting current offers and promotions or playing short video sequences of product advertisements.

\- Self-checkouts Systems: Shoppers can manage the checkout process themselves as the total price of the products scanned with the PSA is transmitted to the checkout system via radio signals. Shoppers can pay with cash or credit card at the cashier. For those shoppers that are not interested in using the PSA system, METRO also provides independent self-checkout systems placed near the cashiers. These checkout systems have embedded an Radio Frequency Identification (RFID) reader, which may transparently scan and identify the RFID labels of all products that shoppers have picked up for purchasing.

\- Intelligent Scales facilitating the weighting process of fruits and vegetables.

\- Electronic Shelf Labels that dynamically display pricerelated information per product.

The METRO Future Store initiative represents probably the most successful corporate pervasive IS example. The supermarket chain subcontracted the Boston Consulting Group, a consultant company, to perform annual field studies assessing (i) the extent to which the deployed applications in the shop floor enhance the traditional shopping experience; and (ii) shoppers’ perceived acceptance of the technologies involved. According to the latest results, published in April 2005, 85% of the customers visiting the supermarket in Rheinberg always use at least one system feature. Smart scales are the preferred method of interacting with the system, whereas infokiosks are second runners. It should be noted that the pervasive IS acceptance by older customers has grown from 16% in July 2003 to 27% in April 2005. At the same time, the rate of new customers has steadily increased during the period 2003–2005 by 30% per year. In terms of perceived acceptance and effect to the traditional shopping experience, over 90% of the respondents in each annual survey indicated that the technology solutions have been useful and supportive during their shopping trip, contributing to a more streamlined and entertaining shopping experience.

The design of METRO Future Store paid significant attention to the provision of user friendly and easy to learn interaction modalities. In particular, the system uses the shopping cart as the main interaction medium. However, to accommodate for the different shopper expectations and fears against IT, the designers also devised a variety of ways to interact with the system in the form of infokiosks, intelligent scales, dynamic price labels, and self-checkout systems. By that means, shoppers may still flavor from the system benefits and receive a streamlined and pleasant shopping experience. The system components and pervasive artifacts are coordinated by middleware software. Because multiple vendors participate in the project, the pervasive IS environment encompasses several middleware platforms each supporting a particular system feature.

Table 3 provides the a posteriori assessment of METRO Future Store Initiative by evaluating the current architectural and functional design of the system.

Figure 2 provides a schematic representation regarding the degree of pervasiveness for the METRO Future Store. The scores are based on the a posterior evaluation of the system and are based on the analysis that follows. In principle, the functionality and architectural elements of the system follow the same design principles considered by related systems, which are commonly known as PSA [e.g. (Asthana et al., 1994; Menczer et al., 2002; Shekar et al., 2003; Zhu et al., 2004; Cumby et al., 2005)]. Our analysis on the five examination dimensions of the framework suggests that designers may strehgthen the degree of pervasiveness for the Future Store Initiative on several directions. For example, designers might develop additional interaction modalities with the system resources that compliment the existing ones. Enhancing the interactivity of the system by incorporating RFID scanning to the shopping cart represents such a design strategy. The benefits of RFID technology compared to barcodes can be summarized to (a) transparent data capturing for the shopper (no line-ofsight is required between the tag and the reader); and

282  
Table 3 A posteriori assessment of METRO Future Store Initiative

<table><tr><td>Dimension</td><td>Assessment</td><td>Current design choices</td></tr><tr><td>Degree of mobility</td><td>(Highly) mobile</td><td>Full wireless coverage (using IEEE 802.11) throughout the entire supermarket space.</td></tr><tr><td>Degree of interactivity</td><td>Uni-modal interaction</td><td>Shoppers may interact on a one-to-one basis with each access device. No multi-modal interaction elements are supported by the system.</td></tr><tr><td>Degree of heterogeneity</td><td>Relatively heterogeneous</td><td>The system supports a variety of pervasive devices and artifacts supporting its smooth operation.Devices range from the Table PC that is embedded on top of the shopping cart to PDAs, smart shelves, intelligent scales, and smart checkout systems. A middleware capable of coordinating communications between the back-end systems and the pervasive devices supports this requirement.</td></tr><tr><td>Degree of contextual awareness</td><td>Relatively high contextual awareness</td><td>Electronic shelf labels dynamically change the price of products based on predefined conditions. Personalized promotions pop-up on the Personal Shopping Assistant based on the current contents of the cart and shoppers&#x27; individual preferences. Electronic advertising displays present promotional videos based on ambient information.</td></tr><tr><td>Degree of invisibility</td><td>Mostly conspicuous</td><td>All interaction elements are fully visible to increase their accessibility by shoppers (shopping cart, intelligent scales, and so on). Supporting infrastructure has been installed so that it does not infer with shoppers.</td></tr></table>

![](/api/attachments/R6AMEZPR/fulltext/images/1b16d2df1ee17fd82a34936f7f3c133902070e8d1d201d2eca6d1825e7fde288.jpg)  
Figure 2 Framework’s scores regarding the degree of pervasiveness for METRO Future Store.

(b) efficient operation in hostile environments (excessive dust, moisture, dirt, and so on), which ensures that the RFtag will be read even in extreme conditions (Smith and Konsynski, 2003; Pramataris et al., 2004; Prater et al., 2005). Kourouthanassis and Roussos (2003) discuss the implementation of a smart shopping cart, which uses RFID technology as the main interaction modality with the system. In all cases, the appropriate design policies on each pervasiveness dimension of the framework will be subject to the constraints, opportunities, and unique requirements of the application domain.

## MIT’s House\_n Initiative

House\_n is an umbrella project that investigates how pervasive computing technologies may be applied to better meet the opportunities and challenges of future homes. The project is led by MIT’s Department of Architecture. Several industrial and academic partners also participate in the project. The House\_n Initiative embraces several diverse micro-projects aspiring to design and evaluate smart home applications and services. The Open Source Building Alliance micro-project aims at devising the necessary IT artifacts for demonstration purposes. Areas of investigation include ambient assisted living (modular heating, lightning, and air-conditioning), health and safety management (biometric monitoring, fire, and intruder detection), and networked information appliances (Larson and Intille, 2003). To investigate the behavior of residents when using the aforementioned portfolio of pervasive application and services within their home environment, a ‘living laboratory’ residential home research facility, called PlaceLab, has been constructed in July 2004 in an urban neighborhood near MIT (Intille et al., 2006).

Volunteer participants live in PlaceLab for a specific time of period and share their experiences of using smart home pervasive computing technologies. The research facility resembles a normal apartment consisting of a dining area, living room, kitchen, bedrooms, baths, and an office area, all augmented with IT. To date, three pilot studies have been executed in PlaceLab, each assessing the extent to which IT can adequately support everyday activities of humans in their household. A methodological discussion of these studies, and some preliminary results, are provided in Intille et al. (2006).

From a functional and architectural perspective, everyday objects and appliances have been augmented with sensors and actuators, supporting a user-friendly and easyto-learn interface. Middleware software ensures the proper communication and coordination of all pervasive artifacts. At the same time, the smart home uses just-in-time persuasive user interfaces. These interfaces detect ‘pointof-decision’ contexts using wireless sensors and use this information to extrapolate the current behavior and state of residents. Context-sensitive measurements trigger the system to proactively support ambient assisted living activities (such as switching off the lights when the resident exits a room) or generate health messages for external curators (in case of accidents or other health-related problems).

Table 4 provides the a posteriori assessment of the MIT House\_n Initiative. Similar to the case of METRO’s Future Store, emphasis has been paid to the functional and architectural properties of the system. A diagrammatical representation is illustrated in Figure 3. As in the case of

Metro’s Future Store, the scores are based on the analysis of the architectural and functional design choices of the system.

The application of the framework reveals that the MIT House\_n Initiative provides almost ubiquitous support within its boundaries and paves little ground for significant improvement at least taking into account the present capabilities of pervasive technologies. The limited support for mobility may not be considered as a design drawback because of the inherent characteristics of domestic pervasive systems (different functionality and support should be provided at each room of the household) [c.f. (Crabtree et al., 2002b; Park et al., 2003; Rodden and Benford, 2003; Callaghan et al., 2008)]. Nevertheless, designers might enhance the degree of interactivity and heterogeneity by embodying additional novel interactive elements that have been proposed in pervasive IS literature [e.g. dynamically changing picture frames based on the preferences of the person currently in the room (Crabtree et al., 2002a)].

## Discussion

Advances in information and communication technologies have made it possible to realize a vision in which the computing and interaction boundaries of IS are expanded beyond the desktop space and into the physical environment.

Table 4 A posteriori assessment of MIT House\_n Initiative

<table><tr><td>Dimension</td><td>Assessment</td><td>Current design choices</td></tr><tr><td>Degree of mobility</td><td>Relatively localized</td><td>The system&#x27;s available options, and consequent functionality, are closely associated with the locale of each user, therefore the system provides limited mobility support.</td></tr><tr><td>Degree of interactivity</td><td>Multi-modal interaction</td><td>Residents interact with the system through multiple input modalities that are embedded in the physical space. Interactions take place through ambient interfaces, everyday objects, and IT-augmented home appliances enhancing natural interaction with the system.</td></tr><tr><td>Degree of heterogeneity</td><td>(Highly) heterogeneous</td><td>The system supports a variety of pervasive devices and artifacts that are integrated in everyday objects and information appliances. A middleware capable of coordinating communications between the back-end systems and the pervasive devices supports this requirement.</td></tr><tr><td>Degree of contextual awareness</td><td>(High) contextual cognition</td><td>Wireless sensors provide a variety of proactive operations based on contextual information, which refers to residents&#x27; identity, current location, health-related data, and current activity.</td></tr><tr><td>Degree of invisibility</td><td>Relatively invisible</td><td>All pervasive artifacts have been discreetly integrated into cabinetry, appliances, furnishings, and fixtures. For example, switch sensors are embedded in the wood of walls or ceiling; movement detection sensors have been placed on objects of interest such as chairs or sofas; emitters have been scattered throughout cabinets, and so on.</td></tr></table>

![](/api/attachments/R6AMEZPR/fulltext/images/71c2b36d0e26c443360d8564f47f1531876f2b542c96b4169f04cfefe171c6b7.jpg)  
Figure 3 Framework’s scores regarding the degree of pervasiveness for MIT House\_n Initiative.

This vision is commonly referred to as Pervasive IS and supports new forms of services, organizations, and strategies based on anytime and anyplace computing. In essence, the term pervasive IS characterizes a class of IS that is broadly accessible, increasingly available, and constantly present, aspiring to support user wants and needs proactively.

Pervasive IS will be a fertile source of challenging research problems in the near future. Solving these problems will require IS scholars to fuse seemingly independent research areas (e.g. human–computer interaction, distributed systems, operating systems, and software engineering to name but a few) and to revisit long-standing IS design assumptions and theories. Because IS scholarship is in part about clarity and precision, we need to develop a more common understanding of the core aspects that define ‘pervasiveness’ in these IS types. The IS community has already started investigating the challenges that govern the design of pervasive IS. Nevertheless, these efforts are highly fragmented, adopting a rather myopic investigation lens, and providing an authoritarian design viewpoint by contemplating that the proposed design considerations under each perspective may uniformly apply to all pervasive IS types.

Our research seeks to initiate a scholarly debate on the design of pervasive IS by proposing an integrated and consolidated framework that allows researchers to study the properties of a prospective or existing IS instance and assess its pervasiveness. Our framework considers five dimensions defining pervasiveness. Each dimension examines a unique perspective along which IS are currently evolving. The framework may be employed for both a posteriori and a priori assessments of IS evaluating their pervasiveness degree based on existing or desired design choices. We contend that advances in these five areas will inevitably influence existing IS design theories, many of which have been developed during the eras of mainframe or desktop-based personal computing when IT was highly localized and aimed at primarily supporting organizational goals. With a deeper understanding of the fundamental drivers of IS progress, we might need to revisit some of these theories. We posit that the proposed framework provides an initial step towards this direction by not only providing a means of understanding the potential of pervasive technologies, but also by serving as an instrument for identifying stakeholder needs and evaluating potential business benefits for a prospective or existing IS instance. A psychometric instrument that formally provides scores for each pervasiveness dimension has also been developed in a subsequent work (Karaiskos et al., 2009).

We recognize that there is still ample scope for improving and extending the framework proposed in this article into a fully fledged design theory for pervasive IS. Such theory, further to its inherent scholarly value, will provide guidance to practitioners by demonstrating how traditional IS design methods need to be modified to support the development of pervasive IS. In most cases, traditional IS design approaches provide designers with little guidance about what to do and how to do it. In new and emerging IS areas (such as pervasive IS), the existing knowledge base is often insufficient for design purposes and designers must rely on intuition, experience, and trialand-error methods. A design theory for pervasive IS may codify and systematize current and emerging knowledge and development practices in the pervasive IS domain to enhance the efficacy of the design process.

## References

Abowd, G.D. and Mynatt, E.D. (2000). Charting Past, Present, and Future Research in Ubiquitous Computing, ACM Transactions on Computer-Human Interaction.7: 29-58

Abowd, G.D., Mynatt, E.D. and Rodden, T. (2002). The Human Experience, IEEE Pervasive Computing 1: 48–57.

Akyildiz, I.F., Wang, X. and Wang, W. (2005). Wireless Mesh Networks: A survey, Computer Networks 47: 445–487.

Alt, R. and Puschmann, T. (2005). Developing Customer Process Orientation: The case of Pharma Corp, Business Process Management Journal 11: 297–315.

Apple (2006). Networking: Bonjour, [www document], http://developer .apple.com/networking/bonjour/index.html (accessed 15th July 2009).

Ashok, R.L. and Agrawal, D.P. (2003). Next-generation Wearable Networks, IEEE Computer 36: 31–39.

Asthana, R., Cravatts, M. and Krzyzanowski, P. (1994). An Indoor Wireless System for Personalized Shopping Assistance, IEEE Workshop on Mobile Computing Systems and Applications; Santa Cruz, California: IEEE Computer Society Press.

Bakhouya, M. and Gaber, J. (2007). Service Composition Approaches for Ubiquitous and Pervasive Computing Environments: A survey, in E. Li and S.T. Yuan (eds.) Agent Systems in Electronic Business, Hershey, PA: IGI Publishing.

Beckwith, R. (2003). Designing for Ubiquity: The perception of privacy, IEEE Pervasive Computing 2: 40–46.

Benford, S., Schna¨delbach, H., Koleva, B., Anastasi, R., Greenhalgh, C., Rodden, T., Green, J., Ghali, A., Pridmore, T., Gaver, B., Boucher, A., Walker, B., Pennington, S., Schmidt, A., Gellersen, H. and Steed, A. (2005). Expected, Sensed, and Desired: A framework for designing sensing-based interaction, ACM Transactions on Computer-Human Interaction 12: 3–30.

Biegel, G. and Cahill, V. (2008). Requirements for Middleware for Pervasive Information Systems, in P. Kourouthanassis and G.M. Giaglis (eds.) Pervasive Information Systems, M.E. Sharpe, 86–102.

Birnbaum, J. (1997). Pervasive Information Systems, Communications of the ACM 40: 40–41.

Bohn, J., Coroama, V., Langheinrich, M., Mattern, F. and Rohs, M. (2003). Disappearing Computers Everywhere Living in a World of Smart Everyday Objects, New Media, Technology and Everyday Life in Europe Conference (London, UK), [www document], http://www.lse.ac.uk/collections/EMTEL Conference/papers/Bohn.pdf.

Boukerche, A., Chatzigiannakis, I. and Nikoletseas, S. (2006). A New Energy Efficient and Fault-tolerant Protocol for Data Propagation in Smart Dust Networks Using Varying Transmission Range, Computer Communications 29: 477–489.

Burkey, C. (2000). Environmental Interfaces: HomeLab, Conference on Human Factors in Computing Systems; the Hague, the Netherlands: ACM Press.

Buttery, S. and Sago, A. (2003). Future Applications of Bluetooth, BT Technology Journal 21: 48–55.

Cabri, G., Leonardi, L. and Zambonelli, F. (2002). Engineering Mobile Agent Applications via Context-dependent Coordination, IEEE Transactions on Software Engineering 28: 1039–1055.

Callaghan, V., Chin, J., Zamudio, V., Clarke, G., Shahi, A. and Gardner, M. (2008). Domestic Pervasive Information Systems: End-user programming of digital homes, in P. Kourouthanassis and G.M. Giaglis (eds.) Pervasive Information Systems, M.E. Sharpe, 150–164.

Cao, J., Xing, N., Chan, A.T.S., Feng, Y. and Jin, B. (2005). Service Adaptation using Fuzzy Theory in Context-aware Mobile Computing Middleware, 11th IEEE International Conference on Embedded and Real-time Computing Systems and Applications, Hong Kong: IEEE Press.

Cheverst, K., Davies, N., Mitchell, K., Friday, A. and Efstratiou, C. (2000). Developing a Context-aware Electronic Tourist Guide: Some issues and experiences, T. Turner and G. Szwillus (eds.) ACM SIGCHI Conference on human factors in computing systems, pp. 17–24. New York: ACM Press.

Churchill, E.F., Nelson, L. and Denoue, L. (2003). Multimedia Fliers: in M. Huysman, E. Wenger and V. Wulf (eds.) Information sharing with digital community bulletin boards, in M. Huysman, E.Wenger and V. Wulf (eds.), Communities and Technologies, Amsterdam, the Netherlands: Kluwer, pp. 97–117.

Crabtree, A., Hemmings, T. and Rodden, T. (2002a). Coordinate Displays in the Home, ACM Conference on Computer Supported Cooperative Work; New Orleans: ACM Press.

Crabtree, A., Hemmings, T. and Rodden, T. (2002b). Pattern-based Support for Interactive Design in Domestic Settings, Symposium on Designing Interactive Systems; London, UK: ACM Press.

Cumby, C., Fano, A., Ghani, R. and Krema, M. (2005). Building Intelligent Shopping Assistants using Individual Consumer Models, 10th International Conference on Intelligent User Interfaces; San Diego, California, USA: ACM Press.

Dodgson, N.A. (2005). Autostereoscopic 3D Displays, IEEE Computer 38: 31–36.

Dey, A. and Mankoff, J. (2005). Designing Mediation for Context-aware Applications, Communications of the ACM 12: 53–80.

Dunlop, J., Girma, D. and Irvine, J. (1999). Digital Mobile Communications and the TETRA System, New York: Wiley.

Estrin, D., Culler, D., Pister, K. and Sukhatme, G. (2002). Connecting the Physical World with Pervasive Networks, IEEE Pervasive Computing 1: 59–69.

Fano, A. and Gershman, A. (2002). The Future of Business Services in the Age of Ubiquitous Computing, Communications of the ACM 45: 83–87.

Fox, D., Hightower, J., Liao, L., Schulz, D. and Borriello, G. (2003). Bayesian Filtering for Location Estimation, IEEE Pervasive Computing 2: 24–33.

Gajos, K. and Weld, D. (2004). SUPPLE: Automatically generating user interfaces in J. Vanderdonckt, N.J. Nunes and C. Rich (eds.) 9th Internationa Conference on Intelligent User Interfaces (IUI) 2004, Funcha, Portugal, New York: ACM Press, pp. 93–100

Geer, D. (2005). Users Make a Beeline for ZigBee Sensor Technology, IEEE Computer 38: 16–19.

Hallnas, L. and Redstrom, J. (2001). Slow Technology – Designing for reflection, Personal and Ubiquitous Computing 5: 201–212.

Hallnas, L. and Redstrom, J. (2002). From Use to Presence: On the expressions and aesthetics of everyday computational things, ACM Transactions on Computer-Human Interaction 9: 106–124.

Haque, M. and Ahamed, S.I. (2006). Security in Pervasive Computing: Current status and open issues, International Journal of Network Security 3: 203–214.

Held, A., Buchholz, S. and Schill, A. (2002). Modeling of Context Information for Pervasive Computing Applications, in N. Callaos, G. Whymark and W. Lesso (eds.) IEEE Proceedings of the 6th World Multiconference on Systemics, Cybernetics and Informatics (SC12002) Orlando, FL, USA: IEEE Press.

Helms, J. and Abrams, M. (2008). Retrospective on UI Description Languages, Based on Eight Years’ Experience with the User Interface Markup Language (UIML), International Journal of Web Engineering and Technology 4: 138–162.

Hirschfeld, R. and Kawamura, K. (2004). Dynamic Service Adaptation, 24th International Conference on Distributed Computing Systems, Hachioj Tokyo, Japan: IEEE Press, 290–297.

Hoymann, C. (2005). Analysis and Performance Evaluation of the OFDM-based Metropolitan Area Network IEEE 802.16, Computer Networks 49: 341–363.

Hsi, S. and Fait, H. (2005). RFID Enhances Visitors’ Museum Experience at the Exploratorium, Communications of the ACM 48: 60–65.

Hsin, C. and Liu, M. (2006). Self-monitoring of Wireless Sensor Networks, Computer Communications 29: 462–476.

Hu, W.C., Lee, C.W. and Kou, W. (eds.) (2005). Advances in Security and Payment Methods for Mobile Commerce, Hershet, PA: Idea Group Publishing.

Intille, S.S. (2002). Designing a Home of the Future, IEEE Pervasive Computing 1: 76–82.

Intille, S.S., Larson, K., Munguia Tapia, E., Beaudin, J., Kaushik, P., Nawyn, J. and Rockinson, R. (2006). Using a Live-in Laboratory for Ubiquitous Computing Research, in K.P. Fishkin, B. Schiele, P. Nixon and A. Quigley (eds.) 4th International Conference on Pervasive Computing: Dublin, Ireland: Springer-Verlag.

Jafari, R., Dabiri, F., Brisk, P. and Sarrafzadeh, M. (2005). Adaptive and Fault Tolerant Medical Vest for Life-critical Medical Monitoring, in L.M. Liebrock, (ed.) ACM symposium on Applied Computing, Santa Fe, New Mexico: ACM Press, 272–279.

Jeronimo, M. and Weast, J. (2003). UPnP Design by Example: A software designer’s guide to universal plug and play, Hillsboro, TX: Intel Press.

Johanson, B., Fox, A. and Winograd, T. (2002). The Interactive Workspaces Project: Experiences with ubiquitous computing rooms, IEEE Pervasive Computing 1: 67–74.

Jonsson, M. (2002). Context Shadow: An infrastructure for context aware computing, 3rd Workshop on Artificial Intelligence in Mobile Systems (AIMS) in conjunction with ECAI 2002 (Lyon, France), Seattle, WA.

Junglas, I.A. and Watson, R.T. (2006). The U-Constructs: Four information drives, Communications of the AIS 17: 2–43.

Kawsar, F., Fujinami, K. and Nakajima, T. (2005). Augmenting Everyday Life with Sentient Artefacts, in G. Bailly, and J.L. Crowley (eds). Smart Objects and Ambient Intelligence Conference Grenoble, France, NY: ACM Press, pp. 141–146.

Kidd, C.D., Orr, R., Abowd, G.D., Atkeson, C., Essa, I., Macintyre, B., Mynatt, E.D., Starner, T. and Newstetter, W. (1999). The Aware Home: A living laboratory for ubiquitous computing research, Second International Workshop on Cooperative Buildings; Berlin: Springer-Verlag.

Kiss, C. (ed.) (2007). Composite Capability/Preference Profiles (CC/PP): Structure and vocabularies 2.0. [www document], http://www.w3.org/TR/ 2007/WD-CCPP-struct-vocab2-20070430/.

Kostakos, V. and O’Neill, E. (2004). Designing Pervasive Systems for Society, in A. Ferscha and F. Mattern (eds.) Second International Conference on Pervasive Computing, Vienna, Austria, Heidelberg: Springer, Berlin.

Kourouthanassis, P. (2004). Can Technology Make Shopping Fun? ECR Journal 3: 37–44.

Kourouthanassis, P. and Giaglis, G.M. (2006). A Design Theory for Pervasive Information Systems, in S.K. Moste´faoui, Z. Maamar and G.M. Giaglis (eds.): 3rd International Workshop on Ubiquitous Computing Paphos, Cyprus, INSTICC Press.

Kourouthanassis, P. and Giaglis, G.M. (2008a). The Design Challenge of Pervasive Information Systems, in P. Kourouthanassis and G.M. Giaglis (eds.) Pervasive Information Systems, NY: M.E. Sharpe, 29–85.

Kourouthanassis, P. and Roussos, G. (2003). Developing Consumer-friendly Pervasive Retail Systems, IEEE Pervasive Computing 2: 32–39.

Kourouthanassis, P.E. and Giaglis, G.M. (eds.) (2008b). Pervasive Information Systems, New York: M.E. Sharpe Inc.

Lai, J., Mitchell, S., Viveros, M. and Wood, D. (2002). Ubiquitous Access to Unified Messaging: A study of usability and the use of pervasive computing, International Journal of Human-Computer Interaction 14: 385–404.

Langheinrich, M. (2001). Privacy by Design – Principles of privacy-aware ubiquitous systems, in G.D. Abowd, B. Brummitt and S.A.N. Shafer (eds.) UBICOMP 2001, Berlin, Heidelberg: Springer-Verlag.

Langheinrich, M. (2002). A Privacy Awareness System for Ubiquitous Computing Environments, in G. Borriello and L.E. Holmquist (eds.) 4th International Conference on Ubiquitous Computing, UBICOMP, Springer-Verlag, 237–245.

Laplant, B., Trewin, S., Zimmermann, G. and Vanderheiden, G. (2004). The Universal Remote Console: A universal access bus for pervasive computing, IEEE Pervasive Computing 3: 76–80.

Larson, K. and Intille, S.S. (2003). MIT Open Source Building Alliance: A house\_n initiative, Cambridge, MA: Massachussets Institute of Technology.

Lemon, O. and Gruenstein, A. (2004). Multithreaded Context for Robust Conversational Interfaces: Context-sensitive speech recognition and interpretation of corrective fragments, ACM Transactions on Computer-Human Interaction 11: 241–267.

Lenzini, L. and Mingozzi, E. (2001). Performance Evaluation of Capacity Request and Allocation Mechanisms for HiperLAN2 Wireless LANs, Computer Networks 37: 5–15.

Liszka, K.J., Mackin, M.A., Lichter, M.J., York, D.W., Pillai, D. and Rosenbaum, D.S. (2004). Keeping a Beat on the Heart, IEEE Pervasive Computing 3: 42–49.

Luff, P. and Heath, C. (1998). Mobility in Collaboration, in S. Poltrock and J. Grudin (eds.) CSCW’98, Seattle, WA, NY: ACM Press, 305–314.

Lyytinen, K. and Yoo, Y. (2002a). Issues and Challenges in Ubiquitous Computing, Communications of the ACM 45: 63–65.

Lyytinen, K. and Yoo, Y. (2002b). The Next Wave of Nomadic Computing: A research agenda for information systems research, Information Systems Research 13: 377–388.

Lyytinen, K., Yoo, Y., Varshney, U., Ackerman, M.S., Davis, G., Avital, M., Robey, D., Sawyer, S. and Sorensen, C. (2004). Surfing the Next Wave: Design and implementation challenges of ubiquitous computing environments, Communications of the Association for Information Systems 13: 697–716.

Maes, P. (2005). Attentive Objects: Enriching people’s natural interactions with everyday objects, ACM Interactions 12: 45–48.

Mamei, M. and Zambonelli, F. (2005). Programming Stigmergic Coordination with the TOTA Middleware, 4th International Joint Conference on Autonomous Agents and Multiagent Systems; the Netherlands: ACM Press.

Mankoff, J., Abowd, G.D. and Hudson, S.E. (2000). OOPS: A toolkit supporting mediation techniques for resolving ambiguity in recognition-based interfaces, Computer and Graphics 24: 819–834.

Merino, A.S., Matsunaga, Y., Shah, M., Suzuki, T. and Katz, R.H. (2005). Secure Authentication–System for Public WLAN Roaming, Mobile Networks and Applications, 10: 355–370.

Matinlassi, M., Niemela¨, E. and Dobrica, L. (2002). Quality-driven Architecture Design and Quality Analysis Method – A revolutionary initiation approach to product line architecture, Espoo, Finland: VTT Publications.

Mckelvin, M.L., Williams, M.L. and Berry, N.M. (2005). Integrated Radio Frequency Identification and Wireless Sensor Network Architecture for Automated Inventory Management and Tracking Applications, Conference on Diversity in Computing, Albuquerque, New Mexico, USA, NY: ACM Press, 44–47.

Menczer, F., Street, W.N., Vishwakarma, N., Monge, A.E. and Jakobsson, M. (2002). IntelliShopper: A proactive, personal, private shopping assistant, International Conference on Autonomous Agents; Rome, Italy: ACM Press.

Metro Future Store (2006). METRO Group Future Store Initiative, Rheinberg, Germany.

Mohan, R., Smith, J. and Li, C.S. (1999). Adapting Multimedia Internet Content For Universal Access, JEEE Transactions on Multimedia 1: 104-114.

Najjar, L., Thompson, J.C. and Ockerman, J.J. (1997). A Wearable Computer for Quality Assurance in a Food-processing Plant, 1st International Symposium on Wearable Computers; Los Alamitos, California: IEEE Press.

Ni, L.M., Liu, Y., Lau, Y.C. and Patil, A.P. (2004). LANDMARC: Indoor location sensing using active RFID, Wireless Networks 10: 701–710.

Nichols, J., Myers, B.A. and Litwack, K. (2004). Improving Automatic Interface Generation with Smart Templates, 9th Intelligent User Interfaces (IUI) Conference, Funchal, Portugal, NY: ACM Press, 286–288.

Oviatt, S., Cohen, P., Wu, L., Vergo, J., Duncan, L., Suhm, B., Bers, J., Holzman, T., Winograd, T., Landay, J., Larson, J. and Ferro, D. (2000). Designing the User Interface for Multimodal Speech and Pen-based Gesture Applications: State-of-the-art systems and future research directions, Human-Computer Interaction 15: 263–322.

Park, S.H., Won, S.H., Lee, J.B. and Kim, S.W. (2003). Smart Home – Digitally engineered domestic life, IEEE Personal and Ubiquitous Computing 7: 189–196.

Plowman, L. and Luckin, R. (2004). Interactivity, Interfaces, and Smart Toys, IEEE Computer 37: 98–100.

Ponnekanti, S.R., Lee, B., Fox, A., Hanrahan, P. and Winograd, T. (2001). I-Crafter: A service framework for ubiquitous computing environments, in G.D. Abowd, B. Brummitt and S. Shafer (eds.) UBICOMP2001, Georgia, Atlanta, Berlin, Heidelberg: Springer-Verlag, 56–75.

Pramataris K. Doukidis G.L. and Kourouthanassis P.E. (2004) Towards Smarter Supply and Demand Chain Collaboration Practices Enabled by RFID Technology, in P. Vervest, E. Van Heck, K. Preiss and L.F. Pau (eds.) Smart Business Networks, Berlin, Heidelberg: Springer-Verlag, 197–210.

Prater, E., Frazier, G.V. and Reyes, P.M. (2005). Future Impacts of RFID on E-supply Chains in Grocery Retailing, Supply Chain Management: An International Journal 10: 134–142.

Quek, F., Mcneill, D., Bryll, R., Duncan, S., Ma, X.F., Kirbas, C., Mccullough, K.E. and Ansari, R. (2002). Multimodal Human Discourse: Gesture and speech, ACM Transactions on Computer-Human Interaction 9: 171–193.

Raatikainen, K., Christensen, H.B. and Nakajima, T. (2002). Application Requirements for Middleware for Mobile and Pervasive Systems, Mobile Computing and Communications Review 6: 16–24.

Raj, H., Schwan, K. and Nathuji, R. (2005). M-ECho: A middleware for morphable data-streaming in pervasive systems, Seattle, Washington: USENIX Association.

Ranganathan, A., Al-Muhtadi, J., Chetan, S., Campbell, R. and Mickunas, M.D. (2004). MiddleWhere: A middleware for location awareness in ubiquitous computing applications, 5th ACM/IFIP/USENIX International Conference on Middleware (Toronto, Canada); New York: Springer-Verlag Inc.

Rasheed, Y., Edwards, J. and Tai, C. (2002). Home Interoperability Framework for the Digital Home, INTEL Technology Journal 6: 5–16.

Ratsimor, O., Chakraborty, D., Joshi, A., Finin, T. and Yesha, Y. (2004). Service Discovery in Agent-based Pervasive Computing Environments, Mobile Networks and Applications 9: 679–692.

Redstrom, J. (2001). Designing Everyday Computational Things, Goteborg, Sweden: Department of Informatics, Goteborg University.

Rodden, T. and Benford, S. (2003). The Evolution of Buildings and Implications for the Design of Ubiquitous Domestic Environments, in G. Cockton and P. Korhonen (eds.) Conference on Human Factors in Computing Systems, Ft. Lauderdale, Florida, USA: ACM Press.

Roman, M., Hess, C., Cerqueira, R., Ranganathan, A., Campbell, R.H. and Nahrstedt, K. (2002a). Gaia: A middleware platform for active spaces, Mobile Computing and Communications Review 6: 65–67.

Roman, M., Hess, C., Cerqueira, R., Ranganathan, A., Campbell, R.H. and Nahrstedt, K. (2002b). A Middleware Infrastructure for Active Spaces, JEEE Pervasive Computing 1: 74–83.

Roussos, G. (2003). Appliance Design for Pervasive Computing, IEEE Pervasive Computing 2: 75–77.

Satyanarayanan, M. (2001). Pervasive Computing: Visions and challenges, IEEE Personal Communications 8: 10–17.

Sawyer, S., Allen, J.P. and Lee, H. (2003). Broadband and Mobile Opportunities: A socio-technical perspective, Journal of Information Technology 18: 121–137.

Schindler, E. (2004). The Buzz in the Background, netWorker 8: 24–29.

Shekar, S., Nair, P. and Helal, A.S. (2003). iGrocer – A ubiquitous and pervasive smart grocery shopping system, in G.B. Lamond, H. Haddad, G.A. Papadoupoulos and P. Panda, ACM Symposium on Applied Computing Melbourne, Florida, USA, NY: ACM Press, 645–652.

Smailagic, A. and Siewiorek, D. (2002). Application Design for Wearable and Context-aware Computers, IEEE Pervasive Computing 1: 20–29.

Smith, H. and Konsynski, B. (2003). Developments In Practice X: Radio Frequency Identification (RFID) – An internet for physical objects, Communications of the Association for Information Systems 12: 301–311.

Smith, J.R., Fishkin, K., Jiang, B., Mamishev, A., Philipose, M., Rea, A.D., Roy, R. and Sundara-Rajan, K. (2005). RFID-based Techniques for Human-activity Detection, Communications of the ACM 48: 39–44.

Sousa, J.P. and Garlan, G. (2002). Aura: An architectural framework for user mobility in ubiquitous computing environments, in J. Bosch, M. Gentleman, C. Hofmeister and J. Kuusela (eds.) 3rd Working IEEE/IFIP Conference on Software Architecture; the Netherlands: Kluwer Academic Publishers, 29–43.

Story, M.F., Mueller, J.L. and Mace, R.L. (1998). The Universal Design File: Designing for people of all ages and abilities, The Center for Universal Design, NC State University.

Streitz, N., Magerkurth, C., Prante, T. and Rocker, C. (2005). From Information Design to Experience Design: Smart artefacts and the disappearing computer, ACM Interactions 12: 21–25.

Thackara, J. (2001). The Design Challenge of Pervasive Computing, Interactions, (May–June) 8: 46–52.

Travi, V. (2001). Advanced Technologies: Building in the computer age, Basel, Switzerland: Birkhauser Verlag AG.

Ullmer, B., Ishii, H. and Jacob, R.J.K. (2005). Token+Constraint Systems for Tangible Interaction with Digital Information, ACM Transactions on Computer-Human Interaction 12: 81–118.

Want, R. and Perring, T. (2005). System Challenges for Ubiquitous & Pervasive Computing, in G.C., Roman, W. Grisworld and B. Nuseibeh, 27th

International Conference on Software Engineering St. Louis, MO, USA, NY: ACM Press, 9–14.

Ward, D.J., Blackwell, A.F. and Mackay, D.J.C. (2002). Dasher: A gesture-driven data entry interface for mobile computing, Human-Computer Interaction 17: 199–228.

Weiser, M. (1993). Some Computer Science Issues in Ubiquitous Computing, Communications of the ACM 36: 75–84.

Weiser, M. (1994). The World is not a Desktop, ACM Interactions 1: 7–8.

Weiser, M. and Brown, J.S. (1998). The Coming Age of Calm Technology, in P.J. Denning and R. Metcalfe (eds.), Beyond Calculation – The next fifty years of computing, Heidelberg, Germany, Springer-Verlag, pp. 75–86.

Wexelblat, A. (1995). An Approach to Natural Gesture in Virtual Environments, ACM Transactions on Computer-Human Interaction 2: 179–200.

Zeimpekis, V., Kourouthanassis, P.E. and M., G.G. (2007). Mobile and Wireless Positioning Technologies, in P. Bellavista (ed.) Telecommunication Systems and Technologies, EOLSS Publishers Co Ltd.

Zhu, W., Owen, C.B., Li, H. and Lee, J.H. (2004). Personalized In-store E-commerce with the PromoPad: An augmented reality shopping assistant, East Lansing, Michigan, USA: Michigan State University.

## About the authors

Dr. Panos E Kourouthanassis (pkour@aueb.gr) is Senior Research Officer in the ISTLAB Wireless Research Center of the Athens University of Economics and Business (AUEB), Greece. His main research interests lie in the areas of eBusiness (emphasizing on mobile and wireless applications and services), pervasive and ubiquitous computing, software engineering, and information systems design. He is coeditor of a volume on Pervasive Information Systems. He is also member of the executive board of the AIS special interest group on Mobile and Ubiquitous Information Systems (SIGMUBIS).

Dr. George M Giaglis (giaglis@aueb.gr) is Associate Professor of eBusiness at the Athens University of Economics and Business (AUEB) and Director of the ISTLab Wireless Research Center (http://istlab.dmst.aueb.gr/wrc/). He has published more than 100 articles in leading journals and international conferences in the areas of electronic and mobile business, business process modeling and simulation, and IS evaluation. He has served as Secretary of the International Conference on Mobile Business (ICMB) and is a cofounder of the AIS special interest group on Mobile and Ubiquitous Information Systems (SIGMUBIS) and coeditor of two books on Pervasive Information Systems.

Dimitrios C Karaiskos (dimkar@aueb.gr) is a doctoral student at the Department of Management Science and Technology at the Athens University of Economics and Business, Greece. His main interests lie in the areas of pervasive and ubiquitous computing and information systems acceptance. He is also a researcher in the ISTLAB Wireless Research Center of the Athens University of Economics and Business (AUEB), Greece.
