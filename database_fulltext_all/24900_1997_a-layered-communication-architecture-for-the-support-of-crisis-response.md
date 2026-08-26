---
otero_id: 24900
otero_key: "CKR3WAG2"
title: "A Layered Communication Architecture for the Support of Crisis Response"
authors: "Joanne Hale"
year: "1997"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1997.11518160"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Layered Communication Architecture for the Support of Crisis Response

Joanne Hale

To cite this article: Joanne Hale (1997) A Layered Communication Architecture for the Support of Crisis Response, Journal of Management Information Systems, 14:1, 235-255, DOI: 10.1080/07421222.1997.11518160

To link to this article: http://dx.doi.org/10.1080/07421222.1997.11518160

![](/api/attachments/CKR3WAG2/fulltext/images/077a96de533e93f2b7b9053c9e54c9cb4502758ecd4079f4568e8a504ed1ca86.jpg)

Published online: 08 Dec 2015.

![](/api/attachments/CKR3WAG2/fulltext/images/975185b1fa79256f9849d10061d6f583e66edae5c12e775a1458e8fcd6ff1610.jpg)

Submit your article to this journal ↗

![](/api/attachments/CKR3WAG2/fulltext/images/4c023323d5f5ad60da5c9d4a41a2f9d030fdeed001e59c4b53d86040ea4b13f6.jpg)

Article views: 3

![](/api/attachments/CKR3WAG2/fulltext/images/9b8c10a7e8c8a128948680a20886e1af31f4d960f57d71175b1f4009250c2d50.jpg)

View related articles ↗

![](/api/attachments/CKR3WAG2/fulltext/images/5ee5b2de06fe98f76701417d0dd5d1b9650e663a389b77f7efac66dd8fdb674a.jpg)

Citing articles: 5 View citing articles ↗

# A Layered Communication Architecture for the Support of Crisis Response

JOANNE HALE

JOANNE HALE is an Assistant Professor of Management Information Systems at the University of Alabama. She holds a Ph.D. in MIS from Texas Tech University, as well as an M.A. in statistics and a B.S. in industrial engineering from the University of Missouri. Her research interests include information systems for the support of crisis management, component-based development and reuse, and small business IS strategy. Her previous research has appeared in IEEE Transactions on Systems, Man, and Cybernetics and the Journal of Systems Management.

ABSTRACT: Crises, situations characterized by high consequence, low probability, and short decision time, create a unique and threatening decision-making environment that must be conscientiously supported. The aim of this study is to derive a prescriptive architecture for crisis response systems, in particular, the role of communication and the characteristics of communication systems that are needed to connect the decision-making elements of crisis response.

The layered crisis communication architecture (CCA) detailed in this paper enumerates the communication functionality required of any crisis response system. To support the crisis-handling team adequately during crisis response, such systems must include the services of each of the described six layers: The base, or connectivity, layer interfaces with the ISO's OSI model to provide error-free end-to-end message transfer. The data-validation layer protects against incorrect data sources through gathering information to corroborate an incoming message. The filtering layer organizes and synthesizes messages to ensure that the crisis-handling team is presented with relevant data in a meaningful, usable form. The values layer interprets messages based on preestablished crisis priorities. The organizational memory layer provides decision makers with access to relevant data and knowledge bases. The group process layer supports the communication, coordination, and collaboration among the crisis-handling team members. To support crisis response adequately, these six layers of the CCA must be implemented as a single, cohesive whole.

Through the CCA, the study offers pragmatically sound principles for organizing crisis response systems and captures a comprehensive perspective of the crisis response process; that is, this work offers a system architecture. As an architecture, the model enumerates all the functions necessary to support crisis response communication effectively.

KEY WORDS AND PHRASES: crisis management systems, crisis response, communication architecture, information systems, organizational crises.

IN THE EARLY MORNING HOURS OF DECEMBER 3, 1984, at a Union Carbide pesticide plant in Bhopal, India, there was a fatal leak of a poisonous gas from an underground storage tank. Most of the victims died from suffocation, the gas attacking their lungs and blood streams. Within a matter of days, there were more than 2,000 deaths and more than 200,000 injuries, including permanent blindness to many [29]. Many of the killed or injured Bhopal residents thought that the Union Carbide plant manufactured "plant medicine" and thus had no fear of or preparation for such a devastating disaster [37]. An extremely simple, readily employed procedure, placing a wet cloth over the face, could have prevented countless deaths [16]. Tragically, the benefit of this elementary technique was not communicated to the residents of Bhopal.

## Motivation

In the complex, fast-paced business environment, a crisis management plan is only as good as the information system that supports it . . . as the business environment becomes more complex and the frequency of crises increases, crisis management systems will become a central part of strategic management. [19, p. 389]

BEFORE THIS PREDICTION CAN BE ATTAINED, MUCH MORE must be learned about the needed functionality of such systems. Investors in and developers of crisis management systems must be given relevant, understandable guidance regarding what system functionality will best facilitate their crisis decision makers.

## What Is an Organizational Crisis?

THIS STUDY RELIES ON THE DEFINITION OF A CRISIS as a situation characterized by [18, 19, 33, 41, 44]:

1. High consequence, or threat to one or more central goals;

2. Low probability of the events' occurrence; and

3. Little available time in which to make and act upon decisions.

Individually, each of these attributes places extreme demands on decision makers. When combined, however, they create a unique and threatening decision-making environment that must be conscientiously supported.

A crisis seems to occur, to the outsider at least, suddenly and without warning. Ideally, this is not true from the perspective of the crisis organization. Crisis management should be initiated prior to the moment when the crisis is actually triggered, with attempts to avoid and plan for potential crises. Correspondingly, organizational crisis management consists of five interdependent stages $[16]$ : mitigation, planning, warning, response, and recovery. Although all five stages are important, this study specifically addresses the unique decision support requirements of the response phase. It is during this phase that the crisis characteristic of short decision time surfaces, the response phase being characterized by a complex set of quickly occurring events $[9, 16, 43]$ . During this phase, punctuated by critical, stressful decision-making, many normal systems of operation fail $[9]$ . The traditional information system is of little use $[30]$ , and decisions are made in an almost random fashion $[23]$ .

## Information Systems and Crisis Management

WHILE “NEITHER A COMPLETE THEORY OF CRISES NOR A COMPLETE theory of organizational crisis management has been proposed to date” [37, p. 141], research has been conducted that is relevant to the study of crisis response decision support. Notable is Nunamaker, Weber, and Chen’s [35] model of organizational crisis management systems. Their model, shown in figure 1, serves as a framework within which the intention of this study may be better understood.

Figure 1 is based on three phases of crisis responsibility: precrisis activities (encompassing the planning and warning phases), crisis activities (representing the response phase), and postcrisis activities (corresponding to the recovery phase). $^{1}$ Most relevant to the study of crisis response support, the crisis activities (hereafter termed the crisis response system) are highlighted in figure 1 and reviewed subsequently. The intention of this study may be interpreted as investigating the functional requirements of Nunamaker et al.'s crisis response system.

At the heart of the crisis response system, an executive “crisis-handling team” directs crisis response efforts while being sequestered in a command center that provides the needed group communication and decision-making tools. The crisis-handling team is further supported by a set of expert systems, developed during the planning stage, which provides access to “detailed crisis plans, control knowledge in terms of tactics, empirically established relationships, propositional facts, and strategies for making use of factual and procedural knowledge” [35, p. 20]. The model further supports crisis response through the situation monitoring system. Using communication and database technologies, the monitoring system tracks the crisis, including critical factors identified during crisis planning, and reports ongoing events to the control center. The resource management system, through the use of database management technology, records and reports the availability and distribution of crisis resources.

Focusing on the functionality of the crisis response system $^{2}$ reveals descriptive studies that detail crisis response tools utilized by organizations. Overwhelmingly, these tools provide crisis response decision support through: access to computer-supported databases [2, 3, 4, 5, 52]; provision of quantitative decision models [2, 3, 4, 5, 18, 52]; or expert systems [18, 23, 51].

A significant shortcoming of this descriptive literature is its overwhelming focus on supporting specific foreseen crises. Given a specific foreseen crisis, decision makers may well benefit from structured expert systems, decision support systems, and quantitative models. However, every organization is potentially faced with a multitude of unforeseen crises $[34, 42]$ , for which quantitative decision models and expert systems would be useless, as they are necessarily built for a narrow problem domain.

Several researchers perceived the need to move beyond description to the development of prescriptive models of crisis response support $[40, 45, 48, 52]$ . However, the models are purely speculative, with no empirical validation of their recommendations. In addition, all but one $[40]$ prescribe a “toolbox” $[48, p. 95]$ of independent, fragmented solutions that actually may do more harm than good $[37]$ .

To produce information systems that effectively support crisis decision making, crisis response and its support must be viewed as a cohesive, purposeful whole. To date, the literature is devoid of this perspective. In response, this study's goal is to develop a model of crisis response support from such a perspective—namely, a prescriptive architecture for crisis response systems. True to the goals of an architecture, the developed model enumerates the functions necessary to support crisis response effectively, without needlessly constraining designers' implementation choices [24, 28].

![](/api/attachments/CKR3WAG2/fulltext/images/a020a7ca714161f91ac1c3a6d58cd6b0d34001459bd86e17e3e079d977ab308b.jpg)  
Figure 1. Model of a Crisis Management Environment Adapted from [35, p. 16]

## Methodology

DERIVATION OF THE PRESCRIPTIVE ARCHITECTURE FOR CRISIS RESPONSE systems has been a theory-building process. Although theory-building research methods have been less formally defined than theory-testing methods, tenets have been set forth to make such an effort more systematic [12, 15]. The study falls into the category of theory-building case studies, as detailed by Eisenhardt [15]. True to the approach, theoretical constructs and relationships are allowed to emerge inductively from empirical data. The benefits of this exploratory case study approach include:

\- An increased likelihood of generating novel theory, because the researcher's perspective is less prejudiced by a priori hypotheses;

\- A resultant theory that is more likely to have greater validity, because the researcher is immersed in the data.

## Analytic Process

Data for the study were obtained through extensive interviews with crisis decision makers and a review of numerous secondary data sources. Secondary data sources included published case studies of responses to five well-documented crises, including the Exxon Valdez oil spill and Union Carbide's Bhopal gas leak. In addition to analyzing these primary and secondary data, theory building was enhanced by theoretical insights gained from published research in related areas. The result is a model developed from the iterative movement among interview data, secondary data obtained from published crisis case studies and relevant literature bases, and the emerging theoretical concepts.

Throughout the process of theory development, the concepts and relationships that were suggested or supported by an interview or published case study were used to refine the questions asked of future data (both primary and secondary). Questions asked of both primary and secondary data probed difficulties faced by the crisis handling team during crisis response, how these difficulties were resolved, what support tools were made available to the team, the effectiveness of these tools, and support changes implemented as a result of the crisis.

True to the theory-building case study approach [15], research sites (representing sources of both primary and secondary data) were selected opportunistically as the theory emerged, in an effort to include a wide variety of crises. The primary unit of analysis is the crisis, not the technology. To focus on technology would confine theoretical discovery to those elements of crisis response already supported, rather than encouraging the full exploration of all needed support functionality.

## Personal Interviews

Personal interviews were conducted with twenty-five crisis decision makers representing thirteen firms and fifteen organizational crises. At least two crisis decision makers were interviewed at most sites. Participants were senior managers who had recently served as crisis-handling team members during major crisis response efforts. Each interview lasted one to five hours, with most lasting approximately two hours.

Written notes were taken during all interviews. $^{3}$ These notes were immediately transcribed by the researcher, then returned to the participants, who were asked to review the transcripts for accuracy and completeness. In some cases, gaps in the notes were filled. In others, statements were clarified, or errors were corrected. If significant changes were made, the corrected and completed notes were again returned to the participant for review. If later theory development deemed it necessary, interview participants were reinterviewed by telephone to clarify a point, expand on a theme, or fill in a hole left in the data or theory.

## Secondary Data

According to Strauss and Corbin [47], literature may be used as sources of primary data, to be analyzed as one would analyze interview or observational data. “Every book, every magazine article, represents at least one person who is equivalent to the anthropologist’s informant or the sociologist’s interviewee” [17, p. 163]. The use of published literature as data has several advantages: The literature is accessible, in consideration of the effort, cost, and speed of data gathering, and it provides an excellent range of comparison groups that otherwise might be unattainable [17]. In accordance with these suggestions, secondary data were obtained from published case and literature bases (including crisis management, high reliability organizations, failsafe systems, data communications, and organizational communication). As one would expect with interview or observational data, these secondary data were collected, analyzed, and incorporated into the developing theory.

Figure 2 shows the crises examined through primary and secondary data sources, categorized according to Shrivastava and Mitroff's [42] crisis typology. This typology classifies crises along two dimensions: (1) internal versus external triggering events; and (2) technical/economic versus human/social triggering events. The figure reveals the variety of crises that were examined during the theory-building process.

## Model Validation

To gather further evidence of the theory's validity, the study's results (discussed in the following sections) were reviewed with two practitioners who otherwise did not participate in the research. One was the founder and president of a small information systems consulting firm, the other a retired vice president who was in charge of crisis management for a large oil company and is now an active crisis management consultant. These two consultants reviewed the theory and both found it useful and understandable to an audience consisting of designers of and investors in crisis response systems.

Technical/Economic

<table><tr><td>NuclearNuclear gas leakChemicalPlant explosionElectronicPlant fireExxonValdez oil spillUnion CarbideBhopal gas leakProcter and GambleRely tampon crisis</td><td>UtilityPower outageFundsStock market crashOfficeEarthquakeDPEarthquakeSchoolTornadoElectronicsEarthquakeMetalHurricane</td></tr><tr><td>FarmExtortion attemptOfficeSexual harassment</td><td>InsurerCalifornia billChemcoKidnappingFarmEmployee arrestsKennedy administrationCuban missile crisisJohnson and JohnsonTylenol poisonings</td></tr></table>

Figure 2. Classification of Organizational Crises  
Adapted from [42, p. 7]. Cases examined through secondary data sources are shown in bold; others were examined through personal interviews.

## Initial Finding: Need for a Communication Perspective

AT THE BEGINNING OF DATA COLLECTION, THE RESEARCHER'S tacit expectation was that the evolving theory would explore and detail the functional characteristics of the tools supporting the crisis handling team, that is, the resource monitoring system, the situation monitoring system, and so on, as shown in figure 1. After only a few interviews with crisis decision makers, this task-driven perspective was submerged. It became clear from these initial interviews that the key obstacle to effective crisis response is the communication needed to access relevant data or expertise and to piece together an accurate, understandable picture of reality. Only after these obstacles are overcome can crisis response tasks be effectively performed. In response, the theoretical focus quickly shifted to the role of communication and the characteristics of communication systems needed to connect the decision-making elements of crisis response.

## A Layered Crisis Communication Architecture

THE RESULTING CRISIS COMMUNICATION ARCHITECTURE (CCA), presented here, prescribes the functionality required to support the effective response to organizational crises. As an architecture [8], the model enumerates all the functions necessary to support crisis communication adequately while it disregards the details of final construction, leaving enough freedom for further design and construction [8, 24, 28].

The CCA is depicted as a layered model that partitions communication functions into a vertical set of layers [46, 49]. Partitioning reduces model complexity and eases future design and construction by:

\- Ensuring that each layer performs a cohesive, or closely related, set of functions;

\- Allowing higher layers to rely upon the services provided by lower layers; and

\- Defining layers that are sufficiently loosely coupled to allow changes in one layer without affecting other layers [24, 46].

Each layer relies on the next lower layer to perform more primitive functions and provides a similar service to the next higher layer $[24, 46]$ . As one moves upward through the layers, the set of services provided by each layer is enhanced $[24]$ . Consequently, describing the layered CCA becomes a process of defining each functional layer, as well as the services provided by each layer to layer(s) above.

This section presents the CCA that prescribes the functionality required to support the effective establishment and utilization of communication links for crisis response. Figure 3 depicts the CCA and its correspondence to the Open Systems Interconnection (OSI) data communication model (see [11, 21]). The OSI model served as a valuable building block for the crisis communication model; the value of the OSI model is that it describes and structures all functions necessary for effective data communications. However, the OSI model lacks detail, particularly at the highest levels [39]. Therefore, the crisis communication model uses the functions provided by the OSI model, building on them to serve the communication requirements within the context of organizational crises. The crisis communication model is not intended to replace the OSI model, but to supplement it. The OSI model describes a number of communication services that are untouched by the crisis model. It should not be inferred from this exclusion that these services are unimportant within a crisis context. Rather, the purpose of this model is to detail those communication services that are most critical and often unavailable during crisis response. When mapped to the OSI model, the connectivity layer represents the services provided by the OSI's physical through presentation layers; the remaining layers of the CCA represent application processes (APs) [24, 39] within the OSI's application layer.

The CCA enumerates the functionality required of crisis response systems. To support the crisis-handling team adequately during crisis response, such systems must include the functions of each of the six layers. As an interface to the OSI model, the connectivity layer ensures that individual messages are received as they were sent. The data-validation layer protects against incorrect or incomplete data sources by searching for collaborative information that is appended to the original message. The filtering layer then groups messages pertaining to the same subject matter into message sets and presents them in priority order. The values layer interprets each message set based upon crisis priorities. The highest-level functions, organizational memory and group process, use annotated message sets as inputs to the decision-making process of the crisis-handling team. The organizational memory layer provides database access, and the group process layer supports the sharing and discussion of the resulting memory sets as well as message sets.

![](/api/attachments/CKR3WAG2/fulltext/images/e8f456caa6ac370c5ac025a43f2e03a5b047fcd9c12432cd037705fabe36b7d7.jpg)  
Figure 3. Crisis Communication Architecture

## Layer 1: Connectivity

Need for the most elemental service provided by the CCA is illustrated by the following interview excerpt:

On Labor Day evening, 1990, an unexpected tornado ripped a devastating path through the School campus. Many buildings were destroyed, and the entire campus was flooded. The tornado left the campus without electricity, and destroyed its telephone switching system. The security guard on duty went to the single remaining communication line, a pay telephone, to notify the college president of the damage. The guard never placed that call—he didn't have a quarter.

Thus, the most fundamental of all crisis communication requirements is an open, operable channel between the crisis-handling team, communication and decision support tools, the resource management system, the situation monitoring system, and other crisis stakeholders. Provision of this function is accomplished by the connectivity layer.

The connectivity layer provides the services of:

• End-to-end message transfer,

\- Error detection and correction.

Thus, through the connectivity layer, succeeding layers are guaranteed that individual messages are transmitted completely and correctly between sender and receiver. In providing these services, the connectivity layer serves as the interface between the OSI model and the CCA.

The CCA process model (shown in figure 4) depicts the information exchange between each of the six layers. The connectivity layers pass an individual message $(M_{i})$ to the data validation layer above.

## Layer 2: Data Validation

When provided with an error-free message by the connectivity layer, the data-validation layer encompasses the functions necessary to prevent the following scenario:

Approximately 8 months after the Bhopal tragedy, Union Carbide's Institute, West Virginia, plant suffered a toxic gas leak that sent 135 local residents to the hospital for treatment. For nearly a week, Union Carbide officials incorrectly believed and reported that the gas was a minor eye and lung irritant. Not until five days after the leak was it determined that, among the 23 hazardous gases that had escaped, two-thirds of the mixture was a toxin that attacks the nervous system [16].

If the hazardous nature of the gas leak had been known as the crisis unfolded in the first days, Union Carbide officials undoubtedly would have changed their chosen actions. Unfortunately, as this scenario illustrates, it is dangerously common to receive incorrect, incomplete, and inconsistent data during crisis response [43].

![](/api/attachments/CKR3WAG2/fulltext/images/167c91d0825d386c3e4074e5e211e8c0282250e32ad82803cbe0ed5aed79fe92.jpg)  
Figure 4. CCA Process Model

The connectivity layer provides a complete message, received as it was sent. The data-validation layer then attempts to authenticate the message content. This is accomplished through triangulation $[13, 53]$ —the reliance on multiple, independent sources to validate an event, fact, or conclusion $[7, 14]$ . Thus, the data-validation layer provides the filtering layer with a central message, annotated with supporting (or contradictory) material (shown as $MV_{i}$ in figure 4).

## Layer 3: Filtering

Provided with a substantiated message by the data validation layer, the filtering layer encompasses the functions necessary to prevent the following scenarios:

An unbelievable and grossly insensitive crisis management oversight occurred during the tragic Jalisco cheese deaths in southern California in the late spring of 1985. The contaminated cheese, purchased mainly by Hispanics, caused more than 30 deaths. A widely publicized poison center hot line, under the auspices of the Los Angeles County Medical Association, was flooded with more than 4,000 calls in three days. But the hot line was staffed with only English-speaking nurses, and the phones were jammed with calls from concerned, confused, scared, and angry Spanish-speaking callers, who could not be helped. [16, p. 60; emphasis in original]

[The control room at Three Mile Island] is seriously deficient under accident conditions. During the first few minutes of the accident, more than 100 alarms went off, and there was no system for suppressing the unimportant signals so that operators could concentrate on the significant alarms. Information was not presented in a clear and sufficiently understandable form. [25, p. 11; emphasis added]

As these two scenarios illustrate, complete, error-free, and validated messages are not enough to assure effective crisis communication. In both cases, the data presented to the stakeholders (the southern California public and the Three Mile Island operator) were complete and accurate. Nevertheless, in one case the data could not be understood. In the other case, data were not necessarily relevant to the tasks at hand; the critical data were masked by information overload.

To deal with these problems, filtering mechanisms are needed. The aim of the filtering layer is to present relevant data to the crisis-handling team in a meaningful, usable form. Without the functionality provided by the filtering layer, the reduction of uncertainty and equivocality is more cumbersome. Data that are misunderstood only increase confusion and, thus, equivocality. Further, the presentation of irrelevant data, at best, fails to decrease uncertainty. Alternatively, it may cause a decision maker to overlook important data. At worst, irrelevant data may actually increase equivocality by confusing a recipient who attempts to infer the data's significance. Processing these unnecessary and unintelligible messages serves dangerously to slow the process of crisis decision making, thus calling for the use of filtering mechanisms.

The data validation layer provides the filtering layer with numerous but unorganized messages, each annotated with collaborating and/or contradictory information. Using this input, the filtering layer provides the following services:

\- Screening incoming messages, diverting those that can be safely handled outside of the crisis-handling team;

\- Organizing related messages into cohesive, coherent message sets; and

\- Sorting message sets according to level of importance.

Through organized, prioritized message sets (shown in figure 4 as $MS_{j}$ ), the crisis-handling team is presented, not with fragments of data, but with a clear picture of ongoing events.

## Layer 4: Values

Provided a message set by the filtering layer, the values layer encompasses the functions necessary to replicate the decision-making support provided by Johnson and Johnson's credo during the Tylenol crisis, as noted by David R. Clare (corporate president):

There are probably as many emergency plans worked out and ready to go within our organization as there are in any other company that tries to prepare for unseen emergencies. But the events surrounding the Tylenol crisis were so atypical that we found ourselves improvising every step of the way. Crisis planning did not see us through this tragedy nearly as much as the sound business management philosophy that is embodied in our credo. It was the credo that prompted the decisions that enabled us to make the right early decisions that eventually led to the comeback phase. [6, p. 31]

James Burke, Johnson and Johnson chairman and CEO, described it this way:

Two things are clear to us. The first is that the value system, as articulated in the credo, now permeates the company in a way that could not have been possible without the crisis. The credo was tested—and it worked. [50, p. 10]

There were many Johnson and Johnson decision makers who stated unequivocally that, when they were forced to act in the dark during the Tylenol crisis, they looked to the credo for guidance. By doing so, they confirmed that actions taken were compatible with the first line of the credo: “We believe our first responsibility is to the doctors, nurses, and patients, to mothers and all others who use our products and services” [50, p. 10].

This layer of crisis communication support furnishes a central ingredient of the decision-making process—crisis response priorities. Organizational values, whether expressed implicitly or explicitly, have a great impact on the response choices made by a crisis-handling team. The proposal offered here is that the effectiveness of the decision-making process is significantly enhanced if these organizational values are made explicit and communicated clearly to crisis decision makers. Within the CCA, the values layer provides such services.

The filtering layer provides a set of interrelated messages. The values layer then analyzes each message set, mapping the contents of the message set against pre-established crisis priorities. Thus, the values layer serves subsequent layers by annotating message sets with interpretation and evaluation against critical crisis priorities (shown in figure 4 as $MSI_{k}$ ). The next two parallel layers of organizational memory and group process are used directly by the crisis-handling team in their crisis response decision making.

## Layer 5: Organizational Memory

Provided interpreted message sets by the values layer, the organizational memory layer, through a direct user interface, encompasses the functions necessary to prevent the following scenario:

During its Colombian hostage crisis, Chemco executives relied heavily on “three people in the trenches.” These three had been central players since the kidnapping took place. As a result, their knowledge and experience were irreplaceable; they barely took time to return home to sleep, shower, and return. So much stress was experienced by these three that two nearly divorced, and the third took an early medical retirement. In retrospect, a corporate executive concluded that perhaps a better strategy would have been to rotate the members of the response group, so that no one person’s experience was indispensable.

These “three people in the trenches” were indispensable because Chemco lacked pertinent organizational memory, lessons of relevant experiences that are maintained and accumulated despite the turnover of personnel and the passage of time $[31]$ . The tools contained in this, the organizational memory, layer ensure that such lessons are not lost and are available as input to crisis decision making.

At this functional layer, organizational memory is supported by recording experiences and aiding the retrieval of needed organizational memory. It is at the organizational memory layer that the traditional strength of information technology—information storage and retrieval—is most realized. Crisis planning often results in the recording of organizational memory to aid crisis response decision making. Typical memory supplements include: a personnel database, an inventory database, maps of corporate facilities and surrounding communities, a historical track record of past incidents, and a response resource database (containing information regarding nearby hospitals, fire stations, and so on). Of course, not all required data can be anticipated, but crisis response efforts will be eased by the needed data that are anticipated and recorded for ready access. To provide the crisis-handling team with an initial response model from which to begin, an additional memory aid often resulting from crisis planning is a set of task checklists. It is not presumed that crisis plans will be (or even can be) followed exactly, but they can provide a valuable starting point [37].

Several simple tools may be used by a crisis-handling team as short-term memory aids. Event logs may be extremely helpful in tracking the course of a crisis, preserving the organizational memory as the membership of the crisis-handling team shifts during crisis response. Event logs are often stored in computer-supported databases, but a simple alternative may be to keep the log on flip charts or on paper attached to the walls of the control room. An additional short-term memory aid is a whiteboard, ideally one whose contents can be readily copied onto paper.

Further supplements to organizational memory may be provided by knowledge stores containing valuable memories from previous crises experienced by both the focal organization and peer organizations. To preserve their experiences, an organization may create a database of the crises studied, with summaries of critical events, issues faced, and the names and telephone numbers of those involved. Photographs, video recordings, or tape recordings of a crisis, when available, can provide rich supplementary memory stored as nodes within a hypertext database. If these tools are not feasible, event logs, useful as short-term memory aids, may also be retained for use as memory aids during later crises (or later stages of the same crisis).

Through a direct user interface, tools at the organizational memory layer allow the crisis-handling team to access and search relevant knowledge and databases. The search results, sets of related memories (depicted in figure 4 as $MyS_{l}$ ), are then used as input to decision making, as supported by the parallel group process layer.

## Layer 6: Group Process

Provided with inputs of interpreted message sets and organizational memory sets, the crisis-handling team must make difficult response decisions such as those faced by Warren Anderson, chairman and CEO of Union Carbide:

Within 48 hours of initial reports of Union Carbide's Bhopal gas leak, Warren Anderson announced an immediate trip to India to personally direct the relief efforts. Warren had yet to speak to Union Carbide officials in India. He had not yet established whether or not he would be allowed to visit the plant. In fact, the Indian government had already threatened his arrest on arrival. [16, 38]

In retrospect, it is difficult to evaluate the expediency of Anderson's decision. Many applauded Anderson's evident concern and caring [38], while others believed that his trip "showed a lot of guts but not a lot of intelligence."⁴ There were certainly both risk and rewards to Anderson's immediate trip to Bhopal. On the positive side, such action showed that the corporation was concerned for public welfare, willing to take responsibility, and willing to take immediate action to aid the disaster's victims and their families. If Anderson had been allowed to visit the plant, he may have been able to obtain more accurate and up-to-date information. This was particularly important because of failings at the connectivity layer—there were reportedly only two telephone lines linking headquarters with the Bhopal plant [16]. Finally, the trip may have been a measure taken to head off lawsuits [16]. From the opposing viewpoint, the lack of connectivity between headquarters and Bhopal drastically reduced Anderson's ability to transmit directives from India back to the United States. In addition, there was a significant risk that Anderson would be arrested upon landing, which would severely curb his ability to act as a central crisis decision maker.⁵

No amount of hindsight can determine whether Anderson should have taken that trip, given the potential rewards and risks known to him at the time. However, there is evidence that insufficient constructive debate took place to air the pro's and con's of this action [16, 27, 38]. It is this constructive debate that is supported at the group process level.

Using the functionality of the group process layer, members of the crisis-handling team share interpreted message sets and organizational memories to build implicit and explicit models of crisis events and reach difficult response decisions (shown in figure 4 as $CM_{m}$ ). Applications encompassing this layer must, at a minimum, include the ability to transmit message and organizational memory sets, store such sets as persistent information (through the parallel organizational memory layer), and append comments to them. Building on this foundation, the group process layer must support the group coordination and decision-making activities necessary for the building and exploration of crisis models.

## Discussion

THE CONNECTIVITY, DATA VALIDATION, FILTERING, AND VALUES LAYERS of the CCA provide the conditions necessary for crisis decision making by ensuring that the crisis-handling team has ready access to valid, relevant messages appended with sufficient corroborating and evaluative information to allow a thorough understanding of ongoing crisis events. Given these facilitating conditions, the two highest parallel layers then are able to support crisis response directly. The organizational memory supports the crisis-handling team with access to knowledge and databases, while the parallel group process layer provides support for group communication and decision-making.

Through the CCA, this research offers pragmatically sound principles for organizing crisis response systems and captures a comprehensive view of the crisis response process; that is, this work offers a system architecture $[28]$ . “Architecture is the art of determining the needs of the user of a structure and then designing it to meet those needs as effectively as possible within the economic and technological constraints” $[10, p. 21]$ . As an architecture $[8]$ , the layered model enumerates all the functions necessary to support crisis communication linkages adequately, while disregarding the details of final construction, leaving enough freedom for further design and construction work $[8, 28]$ .

## Implications for Practice

The CCA provides both the investor and the builder with a standard against which crisis response tools should be measured. This research is not meant to suggest that traditional dedicated crisis response tools, such as decision support systems and expert systems, are to be avoided. However, the research does strongly demonstrate that such tools are only parts of the puzzle; they should be considered potential sources of organizational memory or problem understanding, rather than the entire solution.

A builder of crisis response tools should consciously target the layer(s) to be supported and know how to deliver that support to upper layers; a tool isolated from other layers is of no use to crisis stakeholders. The specific implementation of the crisis communication support model will vary considerably. $^{6}$ Layers may be combined in some implementations; a chosen tool may provide support at multiple layers or only a portion of one layer. Nonetheless, tool builders must realize that all functional layers are necessary to support crisis communication linkages adequately, and, in keeping with the layered approach, different tools may be incorporated into the layers but must work together as a cohesive whole. In evaluating a potential crisis response tool, an investor should determine what layers of support are encompassed by the tool, as well as what support layers are lacking and, consequently, must be provided through other means.

## Implementation of the CCA

As an architecture, the CCA enumerates the functions necessary to support crisis response effectively, without needlessly constraining designers' implementation choices [24, 28]. However, it is beneficial to examine the communication services prescribed by the CCA to determine the capability and promise of current technology in implementing the model. As previously discussed, it is critical to find technologies that are capable of implementing the CCA as a unified, cohesive whole rather than as a set of isolated tools.

Table 1. CCA Implementation Requirements

<table><tr><td>CCA layer</td><td>Services provided</td><td>Implementation requirements</td></tr><tr><td>Group process</td><td>Sharing of message and memory sets among CHT membersSupport for formulation of crisis models</td><td>Group communicationGroup collaborationGroup coordination</td></tr><tr><td>Organizational memory</td><td>Access to previous internal, external experiences relevant to crisis</td><td>Data, knowledge base searchAdaptive learning</td></tr><tr><td>Values</td><td>Interpretation and evaluation of message sets based on crisis priorities</td><td>Pattern recognition</td></tr><tr><td>Filtering</td><td>Organization of messages into message sets</td><td>Message classificationMessage organizationMessage synthesis</td></tr><tr><td>Data validation</td><td>Validated message</td><td>Data, knowledge base search</td></tr><tr><td>Connectivity</td><td>End-to-end message transfer</td><td>Synchronous and asynchronous transmission Multimedia</td></tr></table>

Table 1 summarizes the implementation requirements ensuing from each of the six layers of CCA support. To provide the connectivity service of end-to-end message transfer, a CCA-conforming system must support both synchronous and asynchronous transmission of messages in a number of media (text, voice, image, and video). At the data-validation layer, a CCA-conforming system must be capable of abstracting the core of a message and searching for corroborating information from independent sources, including other incoming messages, as well as related data and knowledge bases. To provide the filtering service of organizing individual messages into cohesive message sets, a CCA-conforming system must be capable of classifying messages according to content, synthesizing related messages into a single message, and organizing message sets according to priority. To provide the values-layer service of interpreting message sets based upon their impact on preestablished crisis priorities, a CCA-conforming system must be capable of recognizing a recurrent theme or issue present within a message set and mapping it to the priority set. The services of the organizational memory layer require a CCA-conforming system to provide user access to data and knowledge bases, and to allow these data and knowledge bases to incorporate the memories that emerge as the ongoing crisis unfolds. At the group process layer, a CCA-conforming system must provide the crisis-handling team with those tools necessary for the group's ongoing communication, collaboration, and coordination. This will necessarily include supporting group processes such as brainstorming, idea evaluation, and consensus building.

The class of information systems termed groupware is promising in its ability to provide a platform on which to implement the CCA. $^{7}$ Groupware is defined as the class of computer-based systems that are explicitly designed to support groups of people working together [22]. In particular, several groupware products (e.g., Lotus Notes and Microsoft Exchange) show considerable potential with regard to implementing the CCA as a unified, cohesive whole. Critical to their use as a CCA platform, these applications support [20, 32]:

\- Both asynchronous transmission of and simultaneous access to multimedia files;

\- Integration with external data sources, such as relational databases, image and video servers, and the Internet;

\- Message filtering and sorting through an integrated search engine; and

\- Shared databases, which provide groups with a common workspace through which collaboration is supported.

Future research efforts will include using such a comprehensive groupware tool to implement a prototype of the CCA, and testing its ability to support the decision-making efforts of the crisis-handling team.

## Conclusions

A NOTABLE CONTRIBUTION OF THIS RESEARCH IS THAT IT uncovers significant strengths and limitations of current literature. The bulk of related research activity offers task-level support of specific, foreseen crises (e.g., [2, 51, 52]). In contrast, the difficulties that emerged from this examination point to the need to support the personal and data communication necessary to respond to an organizational crisis; only after effective communication is achieved can crisis response tasks be performed. While these task-level support tools are certainly important, they are only as effective as the communication support system will allow. Thus, this research contributes to the literature by recognizing the need for a theory of crisis communication support.

This research develops relevant, understandable guidance regarding investment in and development of crisis response tools. This is attained through the crisis communication architecture (CCA), which provides both the investor and the builder with a standard against which crisis response tools should be measured. Through this layered model of crisis communication support, the research offers a system architecture $[28]$ , pragmatically sound principles for organizing crisis response systems, and a comprehensive view of the crisis response process.

Finally, crisis response is a complicated process that must take place under conditions of high uncertainty and equivocality. To avoid the development of isolated, fragmented support tools that may do more harm than good $[37]$ , crisis response must be viewed as a set of integrated activities driven to meet essential goals and facilitated through effective communication linkages.

## NOTES

Acknowledgment: The author thanks the Center for Telecommunications Management and the Exxon Company, U.S.A., for their sponsorship of this research.

1. The mitigation phase of crisis management is not addressed in Nunamaker, Weber, and Chen's model.

2. Several notable works, including the prescriptive work of Belardo and Harrald [1] and the descriptive work of O'Sullivan [36], are not discussed here because their focus is on the support of the crisis planning phase, rather than on the functionality of the crisis response system.

3. Audio recording of the interviews was considered but rejected due to concerns that the appearance of a recording device might cause some participants to be less than candid in discussing crisis response difficulties. As detailed in this section, steps were taken to ensure that interview transcripts were both accurate and complete.

4. This is a quotation from an unnamed executive of a rival chemical company to Kirkland [27].

5. In retrospect, this risk was partially realized. Anderson, along with other Union Carbide officials, was placed under house arrest [27].

6. The implementation of an architecture is defined as the specific logical structure chosen to make possible the functions laid out in the architecture [8].

7. The label groupware has been attached to numerous applications as diverse as electronic mail, computer conferencing, group calendaring/scheduling, and workflow management $[26]$ . However, these systems support group work only within a very narrow range of tasks and (generally) use only a single communication media. Therefore, this study considers as groupware only those applications that support group communication, coordination, and collaboration across a wide range of tasks and problem settings.

## REFERENCES

1. Belardo, S., and Harrald, J. A framework for the application of decision support systems to the problem of planning for catastrophic events. IEEE Transactions on Engineering Management, 39, 4 (1992), 400–411.

2. Belardo, S., and Karwan, K.K. The development of a disaster management support system through prototyping. Information and Management, 10, 2 (1986), 93–102.

3. Belardo, S.; Karwan, K.R.; and Wallace, W.A. DSS component design through field experimentation: an application to emergency management. In J.I. DeGross (ed.), Proceedings of the Third International Conference on Information Systems. Ann Arbor, MI: ICIS, 1982, pp. 93–106.

4. Belardo, S.; Karwan, K.R.; and Wallace, W.A. An investigation of system design considerations for emergency management decision support. IEEE Transactions of Systems, Man, and Cybernetics, SMC-14, 6 (1984), 795–804.

5. Belardo, S.; Karwan, K.R.; and Wallace, W.A. Managing the response to disasters using microcomputers. Interfaces, 14, 2 (1984), 29–39.

6. Berge, D. The First 24 Hours: A Comprehensive Guide to Successful Crisis Communications. Cambridge, MA: Basil Blackwell, 1990.

7. Bernstein, C., and Woodward, B. All the President's Men. New York: Simon and Schuster, 1974.

8. Blaauw, G.A. van. Computer architecture. Elektronische Rechenanlagen, 14, 4 (1972), 154–159.

9. Bouillette, J.R., and Quarantelli, E.R. Types of patterned variation in bureaucratic adaptations of organizational stress. Social Inquiry, 41 (1971), 39–45.

10. Brooks, F.P. Architectural philosophy. In W. Buchholz (ed.), Planning a Computer System. New York: McGraw-Hill, 1962, pp. 5–16.

19. Housel, T.J.; El Sawy, O.A.; and Donovan, P.F. Information systems for crisis manage-

11. CCITT. Reference Model of Open Systems Interconnection CCITT Application (CCITT Recommendation X.200). New York: CCITT, 1984.

12. Dougherty, D. Understanding new markets for new products. Strategic Management Journal, 11, 1 (1990), 59–78.

13. Douglas, J. Investigative Social Research. Newbury Park, CA: SAGE Publications, 1976.
14. Downs, A. Inside Bureaucracy. Boston: Little, Brown, 1967.

15. Eisenhardt, K.M. Building theories from case study research. Academy of Management Review, 14, 4 (1989), 532–550.

16. Fink, S.L. Crisis Management: Planning for the Inevitable. New York: American Management Association, 1986.

17. Glaser, B.G., and Strauss, A.L. The Discovery of Grounded Theory. Chicago: Aldine, 1967.

18. Hermann, C.F. Some consequences of crises which limit the viability of organizations. Administrative Science Quarterly, 8, 1 (1963) 61–82.

20. Informationweek. Exchange versus Notes. 569 (1996), 66–70.

21. International Standards Organization. OSI—Basic Reference Model (ISO Document #7498). New York: International Standards Organization, 1984.

22. Ishii, H.; Kobayashi, M.; and Arita, K. Iterative design of seamless collaboration media. Communications of the ACM, 37, 8 (1994), 83–97.

23. Isett, J.B. Decision support system design for crisis decision making: an experiment in automated support for crisis management. Ph.D. dissertation, University of Texas, Austin, 1987.

24. Jain, B.N., and Agrawala, A.K. Open System Interconnection: Its Architecture and Protocols, rev. ed. New York: McGraw-Hill, 1993.

25. Kemeny, J.G. Report of the President's Commission on the Accident at Three Mile Island. Washington, DC: U.S. Government Printing Office, 1979.

26. King, W.R. Strategic issues in groupware. Information Systems Management (Spring 1996), 73–75.

27. Kirkland, R.I., Jr. Union Carbide: coping with catastrophe. Fortune, 111, 1 (1985), 50.

28. Klir, G.J. Architecture of Systems Problem Solving. New York: Plenum Press, 1985.

29. Kuechle, D. Crisis management: an executive quagmire. Business Quarterly, 50, 1 (1985), 53–70.

30. Kupperman, R.; Wilcox, R.; and Smith, H. Crisis management: some opportunities. Science, 187, 4175, 404–410.

31. Levitt, B., and March, J.G. Chester I. Barnard and the intelligence of learning. In O.E. Williamson (ed.), Organization Theory: From Chester Barnard to the Present and Beyond. New York: Oxford University Press, 1990, pp. 11–37.

32. Lotus Development Corporation. White Paper—Lotus Notes. Cambridge, MA: Lotus, 1996. http://www.lotus.com.

33. Milburn, T.W. The management of crises. In C.F. Hermann (ed.), International Crises: Insights from Behavioral Research. New York: Free Press, 1972, pp. 259–277.

34. Mitroff, I.I.; Pauchant, T.C.; and Shrivastava, P. Crisis, disaster, catastrophe: are you ready? Security Management (February 1989), 101–108.

35. Nunamaker, J.F.; Weber, E.S.; and Chen, M. Organizational crisis management systems: planning for intelligent action. Journal of Management Information Systems, 5, 4 (1989), 7–32.

36. O'Sullivan, D. Management training software system simulates disaster situations. Chemical and Engineering News, 70, 38 (1992), 21–23.

37. Pauchant, T.C., and Mitroff, I.I. Transforming the Crisis-Prone Organization: Preventing Individual, Organizational, and Environmental Tragedies. San Francisco: Jossey-Bass, 1992.

38. Pinsdorf, M.K. Communicating When Your Company is under Siege: Surviving Public Crisis. Lexington, MA: Lexington Books, 1987.

39. Piscitello, D.M., and Chapin, A.L. Open Systems Networking: TCP/IP and OSI. Reading, MA: Addison-Wesley, 1993.

40. Rice, R.E. From adversity to diversity: applications of communication technology to crisis management. Advances in Telecommunications Management, 3 (1990), 91–112.

41. Robinson, J.A. Crisis: an appraisal of concepts and theories. In C.F. Hermann (ed.), International Crises: Insights from Behavioral Research. New York: Free Press, 1972, pp. 20–35.

42. Shrivastava, P., and Mitroff, I.I. Strategic management of corporate crises. Columbia Journal of World Business, 22 (1987), 5–11.

43. Shrivastava, P.; Mitroff, I.I.; Miller, D.; and Miglani, A. Understanding industrial crises. Journal of Management Studies, 25, 4 (1988), 285–303.

44. Siomkos, G., and Shrivastava, P. Responding to product liability crises. Long Range Planning, 26, 5, 72–79.

45. Smart, C., and Vertinsky, I. Design for crisis decision units. Administrative Science Quarterly, 22, 4 (1977), 640–657.

46. Stallings, W. Data and Computer Communications. New York: Macmillan, 1994.

47. Strauss, A.L., and Corbin, J. Basics of Qualitative Research: Grounded Theory Procedures and Techniques. Newbury Park, CA.: Sage Publications, 1990.

48. Stubbart, C.I. Improving the quality of crisis thinking. Columbia Journal of World Business, 22, 1 (1987), 89–99.

49. Tanenbaum, A.S. Computer Networks, 3d ed. Englewood Cliffs, NJ.: Prentice-Hall, 1996.

50. The Tylenol Comeback (special report). New Brunswick, NJ: Johnson and Johnson, 1983.

51. Vedder, E.G., and Mason, R.O. An expert system application for decision support in law enforcement. Decision Sciences, 18, 3 (1987), 400–414.

52. Wallace, W.A., and DeBalogh, F. Decision support systems for disaster management. Public Administration Review, 45 (1985), 134–146.

53. Webb, E.J.; Campbell, D.T.; Schwartz, R.D.; and Sechrest, L. Unobtrusive Measures. Chicago: Rand-McNally, 1965.
