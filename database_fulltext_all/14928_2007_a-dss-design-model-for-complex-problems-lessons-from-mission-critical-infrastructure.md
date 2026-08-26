---
otero_id: 14928
otero_key: "THX5Z32S"
title: "A DSS Design Model for complex problems: Lessons from mission critical infrastructure"
authors: "Robb Klashner; Sameh Sabet"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.05.027"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A DSS Design Model for complex problems: Lessons from mission critical infrastructure

Robb Klashner <sup>a,\*</sup>, Sameh Sabet <sup>a,b</sup>

<sup>a</sup>Information Systems Department, New Jersey Institute of Technology, Newark, NJ 07102-1982, United States <sup>b</sup>Tyco Telecommunications, 250 Industrial Way West, Eatontown, NJ 07724, United States

Available online 27 June 2006

## Abstract

This paper presents a new DSS Design Model for complex, mission critical decision-making situations and its technical, conceptual, and partial empirical evaluation. The new model was derived from conceptual design research and through a deep qualitative field research study at an electric power utility control center—a typical arena for <sup>b</sup>wicked<sup>Q</sup> problems. The model suggests an iterative process of theory, simulation, and decision-making interactions. The DSS Design Model is validated using a tool instantiation, microgrid mini-case, and current research of a KMDSS for telecommunications. Main findings suggest that broader and more integrated approaches are necessary to design DSS for complex domains.

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Decision support systems; Design; Wicked decisions; Electricity; Infrastructure; Complex adaptive systems; Knowledge management

## 1. Introduction

There are numerous <sup>b</sup>Decisions<sup>Q</sup> associated with the development of Decision Support Systems (DSS). DSS developers are encumbered by the same domain constraints and complexities that disrupt other software development life cycles (SDLC). Software engineering has increasingly brought more rigor to the SDLC with methodologies formalized as programming languages and built software systems.

However, with the explosion of software utilization in every facet of society, the degree of difficulty and complexity inherent in software design has presented problems for software engineers. They are now attacking <sup>b</sup>wicked<sup>Q</sup> [79] real-world problems within Software Architecture research, which uses the architectural metaphor from systems theorists [85], hardware development, and information systems (IS) research [107].

DSS research can benefit from the progress in Software Architecture research. During the early years of DSS research, design choices were intuitively understood in most cases because of the straightforward nature of the stakeholder criteria (e.g., requirements) and the decision in question. However, stakeholder decisions have become highly subjective due to increased problem complexity [66] and convoluted contextual situations arising from rapidly evolving domain constraints. These domain changes have altered the nature of <sup>b</sup>Support<sup>Q</sup> because the interaction for which the DSS is created is no longer a simple relationship, but a multifaceted one because decision-makers must engage in <sup>b</sup>solving various semi- to ill-structured problems involving multiple attributes, objectives and goals<sup>Q</sup> [66]. One can infer from these developments that DSS design is no longer intuitive or deterministic.

These developments may indicate that the historic DSS design predisposition for deterministic SDLC approaches are frustrating the use of nondeterministic design activities. Therefore, in order for DSS designers to meet the <sup>b</sup>wicked<sup>Q</sup> [79] problem challenge, a more comprehensive <sup>b</sup>Systems<sup>Q</sup> design approach is needed to address the nondeterministic complexities arising from today’s real-world decision-making requirements. Although both software engineers and DSS designers can make progress on this class of problems by hypothesizing about the solutions, it is also logical to first extract intricate details about the problems from specific domains where we know they exist. This strategy is a logical step for DSS designers.

This paper presents a new DSS Design Model to address domain complexities leading to <sup>b</sup>wicked<sup>Q</sup> problems. We contend prescriptive life cycle approaches must be augmented with descriptive approaches to utilize the model for process adaptation to domainspecific constraints. These constraints were derived from data acquired from a field study in the electric power industry – a mission critical infrastructure with real-time domain constraints – and during the subsequent software architecture tool development.

Although this new DSS Design Model appears simple and straightforward, it can exhibit both combinatorial and inherent complexity due in part to our theoretical framework that incorporates morphogenic principles, described later. Thus, based on this theoretical foundation, the model reflectively and concurrently informs its own evolution, thereby directly impacting the design of the proposed DSS under development. A great deal of the model’s complexity comes from the necessity to incorporate a multidisciplinary set of theories and methodological approaches in order to address all the stakeholders and constraints involved in a <sup>b</sup>wicked<sup>Q</sup> problem. The logic behind the model will primarily be presented in the context of designing systems that are used to support electric power grid dispatch and control functions in a large US utility.

The paper also presents an overview of how the model is currently being applied to another mission critical infrastructure design effort to show its generalizability to other domains where DSS plays a key role in daily operations. The remainder of the paper is organized into the following sections. In Section 2, the theoretical background for this work is presented including limitations of classic DSS design approaches; DSS design issues for complex domains such as the electric power industry; SDLC constraints; and theoretical integration using a Complex Adaptive Systems (CAS) theoretical framework. In Section 3, we discuss the research methodology that is a blending of various research streams with respect to decision-making used in the new DSS Design Model. In Section 4, we present the DSS Design Model with its primary relationships and interactive phases. In Section 5, we discuss how we have validated the new DSS Design Model through a software architecture tool development, a mini-case from a second electric power field site, and an empirical study of a Knowledge Management DSS development for global telecommunication network fault analysis research, which is currently underway. In Section 6, we provide our conclusions.

## 2. Theoretical background

Decisions have become more complex because the solution sets are dynamic and reflect the changing nature of domains. In addition, the <sup>b</sup>process of elaboration and refinement of the issues, alternatives, and decision criteria itself is an important component of the problem<sup>Q</sup> [95]. This emerging paradigm negated the historical DSS design approaches that depended upon deterministic problems with quantifiable constraint sets [8,20].

## 2.1. Limitations of classic DSS design approaches

Context and process largely determine resulting software and decisions [54,95]. The software engineering (SE) community widely concurs design decision-making controls the resulting product, or <sup>b</sup>software processes are software too<sup>Q</sup> [71]. Thus, as decision facilitating software, next generation DSS can play a significant role in decision-making if their designers factor in real-world complexities with a broader view of process interactions [21]. The DSS of the past addressed narrowly defined problems reflecting well-defined technological borders, organizational roles, and less dynamic markets. Power summarizes Little’s <sup>b</sup>criteria for designing models and systems to support. . .<sup>Q</sup> from 1970, which include <sup>b</sup>ease of control, simplicity, and completeness of relevant detail<sup>Q</sup> [78]. Thus, in most cases, those early DSS designs could be intuitively understood; i.e., they were easy, simple, and complete. The primary reason for the lack of complexity was the straightforward nature of the stakeholder criteria and the actual decision in question. The organizations were almost as complex then as they are now, but the expectations on technology were not as high in the past. Today, however, clear delineation of boundaries is disappearing resulting in convoluted problems [20]. These developments are exacerbated by a growing dependence on Information and Communication Technologies (ICT). Specifically, the individualistic nature of software and information systems designs has been replaced by designs that tightly couple resources through network capabilities.

ICT have historically been used to extend control over technological resources beyond typical human capabilities (i.e., in space, time, or scale). DSS supported this extended capability to conceptualize, analyze, and adjust resources in order to solve problems. Often, only a small number of individuals control organizational resources using technology (e.g., electric power grid dispatch centers). Tightly coupled strategic approaches overlap functionality and the control of resources (including DSS) with integrated ICT designs. Resources not collocated with the controlling individuals must be managed using ICT. Their efforts and accomplishments are instrumental to overall organizational strategy and specific tactical cases. Thus, ICT provided strategic advantages that were integrated into the business plans and operations – i.e., the daily decision-making processes – effectively making ICT a necessary aspect of these processes that DSS analysts must now factor into their designs. As markets evolved, strategists used ICT to facilitate agility. Short-term mergers, extended supply chains, and rapid integration efforts were all facilitated by ICT. Ecommerce markets emerged based entirely on ICT functionality. These market developments changed the conventional nature of brick-and-mortar businesses including their boundaries and standard operating procedures.

Integrating DSS with ICT capabilities in light of information-rich domain dynamics [95] creates a richer design and will provide needed capabilities for agility in decision-making. These capabilities will better address the <sup>b</sup>wicked<sup>Q</sup> aspects and problems [20,79] associated with complex decision-making due to ever changing domain constraints. The utilization of new DSS designs should be done in the field where the constraints of the domain are salient, e.g., realworld strategic planning [20] or recommending individuals possessing the appropriate expertise [62]. Real-world field problems facilitate requirements elicitation, analysis, and design [21,33] activities that have tangible correlation with emerging <sup>b</sup>wicked<sup>Q</sup> problems [79].

## 2.2. DSS design issues for complex domains: the case of electric power industry

The electric power industry has spent over 100 years learning about electric power faults [41]. Yet, we still have rolling blackouts [91] because the domain is so complex that experimental tests cannot ever be devised to find and prevent all faults. The electric power industry in North America has created an infrastructure spanning thousands of miles [13,41]. This infrastructure is tightly coupled with a <sup>b</sup>complex<sup>Q</sup> of ICT that forms their integrated information infrastructure (I<sup>3</sup>) [52,53]. They communicate over a private telecommunications network that is typically triply redundant (e.g., fiber, microwave, and radio). In the USA, there are approximately 9000 electric power busses. Data retrieved from the domain through Supervisory Control and Data Acquisition (SCADA) [6,52,102] are transmitted to command and control locations every 2–4 s from ubiquitous locations throughout the geographical area, which can span 50,000 square miles with millions of residents. These data are used by Automatic Generation Control (AGC) and other software systems to dynamically adjust the generation–transmission–distribution process for reliability and optimal economic dispatch during periods of stability. But, nearly any significant perturbation will render these automatic tools nearly useless (or worse if faulty information is not detected) [52,91].

Grid dispatch control centers (GDCC) have operators familiar with the domain-specific constraints. They have intuitively guided utilities for decades past faulty conditions in both the physical electric power grid and their information infrastructure. These human operators cannot (and should not) be automated out of the electric power production process because of the life and death nature of this infrastructural service, because this industry is the largest one in the US [13,42]; it is literally the lifeblood of the country. Mission critical operations such as infrastructure control should always have humans in the loop to solve the uncommon, nondeterministic, and unexpected problems. But they need integrated support when making time-sensitive decisions that have overloaded them (and their DSS) with information.

Historically, IS analysts creating a variety of DSS in the electric power domain needed to be concerned with a limited set of software requirements arising from various institutional (e.g., Federal Energy Regulatory Commission (FERC)), organizational, and operational constraints or very narrow economic principles associated with their form of a vertically integrated monopoly. During the last 15 years in the US, deregulation of the electric power industry has necessitated the use of other economic or strategic theories and concepts such as market power in order to create advanced DSS [23,72,82,94]. These electric power domain changes have increased the crosscutting effects (e.g., contradictory Federal and State laws regulating ICT design in a suboptimal manner) [52,53] necessitating new frameworks for the design of DSS to mitigate these <sup>b</sup>wicked<sup>Q</sup> problems [79]. By definition, <sup>b</sup>wicked<sup>Q</sup> problems do not have solutions, only best possible resolutions [79].

The electric power industry fosters the creation of wicked problems. GDCC operational decisions must be made based on large quantities of data (e.g., SCADA). Generally speaking, raw data are gathered in order to generate usable information [6], which is slightly different than knowledge [66,95]. IS can obviously process the huge volume of domain data, but <sup>b</sup>only a fraction of the needed information exists on computers; the vast majority of a firm’s intellectual assets exist as knowledge in the minds of its employees<sup>Q</sup> [66]. Thus, expert operators must still interpret the information. For example, electric power grid operators often abandon their DSS during grid state changes to intuitively understand the nuances of the infrastructure because of their years of experience. These nuances cannot easily be captured in lines of software code.

Compounding their problems are doubt and risk arising from the ICT and DSS currently in place. Individual mechanistic or rudimentary computational components within the electric power grid act in a deterministic manner so that DSS can be designed to leverage their predictability [6]. However, even when rudimentary components are configured in a large system, they produce undesired or unexpected behavior such as harmonics, which oftentimes cannot be attributed to the root cause. Field data indicate that prior to the large West Coast blackout on August 10, 1996, operators observed unusual harmonic readings on the grid, but they were unable to pinpoint the cause [52]. The type of complexity associated with large structures of components is very common (but exacerbated) in large software systems [74] built from thousands of individual modules, subprograms, and objects.

Researchers have been unsuccessful in finding a foolproof method for testing these large software systems. Unfortunately, this lack of assurance increases the complexity further for electric power grid command and control because of their dependency on ICT and DSS. Nevertheless, the trend in the electric power industry is to continue advancing ICT to address new domain constraints [6] created by deregulation. However, these problems may be a result of both social and technical (i.e., sociotechnical) design decisions [53]. For example, the recent US Northeast 2003 blackout was to a large degree propagated by incorrect decision-making arising from a dependency on ICT. The following quotes are from transcriptions of the relevant grid dispatch control centers’ audio files obtained by and for the House Committee’s investigation of the blackout [91]:

## [Approximately 15:07 August 14, 2003]

First Energy/Jerry Snickey: We have no clue. Our computer is giving us fits too. We don’t even know the status of some of the stuff around us. A0822duanEJ1.pdf pp. 33, lines 3–5

MISO/Don Hunter: I called you guys like 10 minutes ago, and I thought you were figuring out what was going on there. A0822duanEJ1.pdf pp. 33, lines 23–25

First Energy/Jerry Snickey: Well, we’re trying to. Our computer is not happy. It’s not cooperating either. A0822duanEJ1.pdf pp. 34, lines 1–3.

These operators must make life and death splitsecond decisions based on their intimate knowledge of the DSS and intuition as to which information source is correct and reliable as seen in the transcripts [91]. Generally speaking, as with any emergency response system, a DSS that is <sup>b</sup>not used on a regular basis before an emergency will never be of use in an actual emergency<sup>Q</sup> [100], indicating a coevolutionary approach to design is needed. If electric power systems are designed to evolve and grow in parallel with the operator’s knowledge capital, intuitive capabilities DSS features can facilitate the dynamic parsing and reintegration of large volumes of knowledge [40,66].

Another primary constraint on the design of DSS is the current grid disposition. Our field investigations determined that the electric power operations have <sup>b</sup>states<sup>Q</sup> [52]. To a large degree, electric power grid states (e.g., blackout state) predetermine the actions of individuals in all circumstances. For example, when the state of the infrastructure system changes, operators are beset with contradicting information as seen in the empirical data just quoted [91], their limited human capacity [54] to process the volume may overwhelm them [38].

A new generation of DSS can ultimately counteract a great deal of the complexity associated with this sort of wicked problem. DSS designed to be adaptive will facilitate knowledge capture and reuse for overwhelmed operators. To be adaptive, there must exist a direct connection to the domain <sup>b</sup>variety<sup>Q</sup> causing the confusion. Field research is necessary to capture these real-world complexities associated with design. Prior requirements engineering research has indicated the importance of maintaining real-world research activities [33,34,43]. Adaptation also infers nondeterministic design processes because deterministic processes are less likely and capable of recognizing and responding to domain state changes. We assert that the lack of adaptation to nondeterministic domain variety is a limitation in classic DSS design approaches that is reflected in the Systems Development Life Cycles (SDLC) used to conceptualize the design process. We examine the SDLC to draw out these conflicts in order to further substantiate the existence of these limitations.

## 2.3. Systems Development Life Cycles (SDLC)

<sup>b</sup>So the rational model of the design process, that is generally taught in our engineering textbooks (such as Pahl and Beitz, 1984) is dead wrong and seriously misleading. . .In software, we must exorcise the waterfall model in favor of co-evolutionary models<sup>Q</sup>. [emphasis added] F. P. Brooks [14].

An SDLC that prescribes behaviors will predetermine the evolution of the design process. These approaches do not match the nondeterministic nature of the <sup>b</sup>wicked<sup>Q</sup> problems we seek to address. Also, the process leading to design is where many of the complexities of the artifact are teased apart. Later life cycle steps, such as testing, implementation, deployment, are natural extensions of the earlier decisions. The SDLC must be understood in order to appreciate the emphasis on software process [71], because <sup>b</sup>Good decisions result from sound process. . .<sup>Q</sup> [54, pp, 392]. Decision-makers typically define the problem both in terms of a solution within the process design and in terms of a certain SDLC model [11,12]. Therefore, a strong correlation exists between what software process is chosen for the design of DSS and the resulting decision support quality. In other words, the decision of how to conceptualize the system’s evolution largely determines the success of the DSS.

An SDLC can be modeled prescriptively or descriptively [21,81]. Typical software or IS development life cycles are prescriptive, such as the popular Rational Unified Process (RUP) [46]. DSS Kleindorfer et al. classify (i.e., in their (Figure 1.1) DSS as one of the deterministic or prescriptive decision science approaches [54]. Hevner et al. assert that DSS design is generally prescriptive, <sup>b</sup>. . .within the context of <sup>d</sup>IS design theories.<sup>T</sup> Such theories prescribe. . .methods. . .instantiation. . .models. Such prescriptive theories must be evaluated. . .<sup>Q</sup> [37].

Choosing a prescriptive SDLC model, however, often produces negative results. It is a well-known and documented fact [86] that critical decisions made in the prescriptive requirements phase have serious and ongoing repercussions throughout the SDLC. Osterweil asserts, <sup>b</sup>there should be no presumption that process code must be overly prescriptive, authoritarian, or intolerable either <sup>Q</sup> [71]. Therefore, we concur with Scacchi, who said, <sup>b</sup>This, of course, should raise concern for the relative validity and robustness of such [prescriptive] life cycle models<sup>Q</sup> [emphasis added] [81]. Besides, <sup>b</sup>sound prescription should be based on careful description<sup>Q</sup> [54, pp. 388].

Descriptive models (i.e., not generally as in [98]) are utilized in an ongoing process improvement approach that is designed to first capture, and then articulate the historical software development in a domain [10,49,87]. This knowledge is leveraged to improve upon the SDLC. Design activities for DSS are intrinsically tied to nondeterministic elements arising from domain constraints and humans [21] in the decision-making process. Thus, future approaches that consider nondeterministic human aspects of the design and decision-making will strengthen the resulting domain analysis.

The electric power industry has standard operating procedures, but their SDLC processes were nevertheless undergoing dramatic evolution due to the nondeterministic social factors associated with the rapidly changing deregulatory environment [67]. Prescriptive models did not adapt well at the GDCC field site because their internal organizational processes were dynamically evolving in response to domain changes arising from Federal and State deregulation of the electric power industry [67,94]. Thus, as with [9], political maneuvers outweighed sound design deci sions during this turbulent transition. This observation from the field demonstrates that qualitative data must be used to limit the combinatorial possibilities because certain aspects of the existing legacy processes are not quickly, economically, or easily replaced with <sup>b</sup>ideal<sup>Q</sup> prescriptive approaches. Symbiotic relationships between the built infrastructure, knowledge workers, and existing software/information systems preclude broad prescriptive models. Custom theoretical frameworks that are derived from the field assist DSS research by guiding decision-makers to a variety of applicable theories and methods. The following section presents the theoretical underpinning that emerged during the descriptive analysis of the GDCC SDLC.

## 2.4. The integration of theoretical perspectives

This research is essentially premised on concepts from design research, various qualitative theoretical and methodological approaches, and Complex Adaptive Systems (CAS) theory. We will very briefly examine key aspects of each to highlight their relevance. The IS community has a clarification of what represents design research (http://www.isworld.org Researchdesign/drisISworld.htm) [101], with which we philosophically concur. We shall, however, scrutinize some design principles, conjectures, and beliefs in order to re-examine these precepts so that some degree of freedom is introduced into this discussion. Instead of making the argument in our own words, we will make some key points by quoting some notable scholars who recently attended a NSF sponsored Science of Design workshop:

1. <sup>b</sup>It is a fact that uncertain and open-ended processes require radically different institutions, organizations and incentives from deterministic processes: the factory approach will not work for designs<sup>Q</sup>. Baldwin [1].

2. <sup>b</sup>A science of software design, then, must be about radical, not about normal, design<sup>Q</sup>. Jackson [45].

3. <sup>b</sup>By its very nature, design involves the integration of information from a heterogeneous collection of knowledge sources each provided by a particular stakeholder with a particular interest in the outcome<sup>Q</sup>. Easterbrook [27].

4. <sup>b</sup>Large, complex systems are hard to evolve without undermining their dependability. Often change is disproportionately costly,. . . I believe that system architectures are pivotal in meeting the above challenge. . . First, dependability properties tend to be emergent, and are much more readily modeled and controlled at an architectural level<sup>Q</sup>. McDermid [61].

We have already partially addressed point #1 above in our discussion of the SDLC, and will introduce nondeterministic aspects of our DSS Design Model in a later section. In point #2, Jackson is referring to design activities that extend beyond the boundaries of the known approaches and existing knowledge in order to meet the new demands of the user or domain. Earlier, McDermid made a similar point by encouraging requirements engineers to go against their <sup>b</sup>orthodox<sup>Q</sup> beliefs [60]. Generally speaking, many still consider qualitative social research to be radical or unorthodox.

Qualitative theory and methods, such as Grounded theory or ethnography, generate large amounts of nonstandard data. Grounded theoretical analysis [30] can be a way of handling these problems. Grounded theory facilitates the understanding of previously unnoticed sociotechnical relations surrounding a group task or activity (e.g., dispatching of electricity). Grounded theory can play a significant role in mission critical domains (such as medical diagnostic) using DSS. For instance, researchers have noted difficulties due to the lack of theoretical guidance, <sup>b</sup>Unfortunately, there is no theory available to guide the selection of the best model<sup>Q</sup>. [58]. We discuss the relevance of ethnography later in this paper.

Point #3 draws out two key aspects relevant to this research. Qualitative approaches are more apt to discover stakeholder agendas. Specifically, <sup>b</sup>Grounded theories take concepts built covertly into any descriptive account, make them visible, examine them, and produce adequate definitions for them<sup>Q</sup> [99]. Their agendas can make normal development processes meaningless because their requirements are not authentic, which is demonstrated later in a mini-case. Easterbrook also emphasizes the need for integration, a key cause of systemic complexity.

McDermid summarizes several other interwoven concepts in Point #4 – size, complexity, evolution, architecture, and emergent properties – that we have focused our research on up to this point. Our unorthodox domain has necessitated design research utilizing the aforementioned qualitative approaches in conjunction with software architectures. Software architecture research [46,52,75,93,97] and IS architecture research [107] abstract away lower level details of software code to focus on major barriers to success or the reuse of component–connector configurations at a high level. These high-level abstractions reduce some, but not all forms of complexity.

The aforementioned challenges drew us to a theoretically grounded Complex Adaptive Systems framework [15] developed as an <sup>b</sup>integrationist<sup>Q</sup> research paradigm [17]. Buckley’s framework was premised on distinct concepts he gleaned from General Systems research and other disciplines. At times, the concepts are synonymous with the current software architecture meaning. The <sup>b</sup>modern systems theorists<sup>Q</sup> from the 1950s and 1960s had tightly coupled the concepts of organization, information, and communication. The environment can be viewed as a <sup>b</sup>set<sup>Q</sup> or <sup>b</sup>ensemble<sup>Q</sup> of elements, states, or events that are to some degree distinguishably different and are generally regarded as <sup>b</sup>variety<sup>Q</sup> [15]. Buckley extended those specific organizational concepts to assert that CAS elements were almost entirely linked by the intercommunication of information.

All known domain entities exist in a state of <sup>b</sup>organized complexity<sup>Q</sup> [15, pp, 38] <sup>b</sup>by a complex net of relations<sup>Q</sup> that conceptually lies between two opposites represented by two ideal organizing constructs: <sup>b</sup>organized simplicity. . .is a complex of relatively unchanging components<sup>Q</sup>; and <sup>b</sup>chaotic complexity<sup>Q</sup> refers to <sup>b</sup>a vast number of components that do not have to be specifically identified and whose interactions can be described<sup>Q</sup>. Buckley also asserted that there are relatively stable spatial, causal, and/or temporal relations between <sup>b</sup>elements or events<sup>Q</sup> considered to be <sup>b</sup>constraints.<sup>Q</sup> Chaotic complexity is the complete lack of constraint and organized simplicity is the presence of maximum constraint. Buckley [16] connects these organizational concepts to a distinct type of information theory.

The conversion of theoretical variety into information includes recognizing and selecting a subset of the variety, then <sup>b</sup>mapping<sup>Q</sup> the environmental variety and constraints into its own organized structure and/or information. This process is basically communication of the original variety and its associated constraints in a manner that remains somewhat invariant between transmitting and receiving elements. However, Buckley also introduces an abstract model of morphogenesis that indicates that two isomorphic systems will not deterministically evolve to the same future state because the occurrence of any particular event within a set of constraints is governed by probabilities. Constraints interact within the context of sensitivity/tension, organization, and contingency to morphogenically evolve the system to another state or <sup>b</sup>level<sup>Q</sup> that is determined by the successful mapping of variety to information or knowledge.

Reuse of Buckley’s research is possible because CAS utilizes concepts such as components, information, events, constraints, and relations that are consistent with many software and IS architecture methods. The fundamental ability to evolve the DSS Design Model based on the domain variety as interpreted by the current systemic model state reflects one of the tenets of the CAS theoretical framework. Thus, the mapping of CAS concepts into DSS design enables designers to modify existing multidisciplinary theories within the integrationist paradigm as Buckley intended.

## 3. Research methodology

We have sought to gain a thorough understand of ICT use in mission critical infrastructure by utilizing deep qualitative methods in conjunction with design research principles. This research strategy was not chosen a priori but was a morphogenic and evolutionary process as the data were collected and analyzed. A qualitative, field-based study enabled us to explore the effects of institutional forces such as the deregulation of the vertically integrated electric power industry. We were especially interested in observing what role ICT played in the inevitable emergent processes. To our knowledge, no other prior studies have concurrently explored the wide spectrum of technical and social factors in a context of command and control of a major utility. These factors have shaped our research design. The literature guided us in our consideration of potentially important aspects as we observed emergent behavior at our field site and throughout their industry.

## 3.1. Methods for DSS design

The preceding sections have all pointed to a confluence of constraints arising from multiple stakeholders with varying agendas. These constraints merge to create pressure on DSS designers. We needed representational sufficiency when discussing the domain and the variety of constraints. Typically, electric power planning approaches [89] merely abstract the domain details away by focusing on special set of circumstances to arrive at requirements. However, to properly understand crosscutting effects, data collection and analysis methods that map domain variety into useful information must be used. Qualitative methods often seem less rigorous than quantitative methods (e.g., semi-structured interviews vs. surveys), but when applied systematically are more formal and effective than ad hoc or informal analysis, which is often used by practicing system analysts [50,105].

Generally speaking, several qualitative methodologies have been explicitly developed to determine a more accurate picture beneath the visible organizational processes. The combined emerging and dynamic picture can often not conform to <sup>b</sup>rational<sup>Q</sup> actor expectations [14,84]. This indicates a need for new research approaches. For example, empirical studies have examined usage of Computer-aided Software Engineering (CASE) tools with the Grounded Theory research approach to study the organizations’ experiences in terms of processes of incremental or radical organizational change [70]. Their findings were then used to develop a theoretical framework for conceptualizing the organizational issues around the adoption and use of these tools. Our research synthesized a methodological framework that was necessary to address emergent phenomenon present in the field data. The resulting synthesized DSS Design Model (presented later) is a derivative of the framework and the field data [52]. It utilizes approaches from various research disciplines such as Software Engineering (SE), Information Systems (IS), and sociology for data collection.

Requirements capture is an integral part of most SDLC. As shown earlier, decisions about prescriptive SDLC approaches map directly and in a deterministic fashion to design decisions. Therefore, we have incorporated descriptive methods into our DSS Design Model starting with the requirements component of the SDLC. Requirement engineering (RE) has been drawn to empirical data [35,36]. Understanding the real-world has been a priority in RE for over 20 years [33,34,43,47]. The interest is due in part to the irreplaceable domain expert in system design [2]. Realistic scenarios, goal-oriented requirements, and use-cases are methods used by engineers to formalize the domain data [2,24,34,47,50,55, 90,103] that all factor into this research design. Empirical data are the only way to accurately understand the <sup>b</sup>why<sup>Q</sup> [35,36,105,106] behind irrational stakeholder behavior in mission critical infrastructure domains because of the widely varying activities leading to software requirements. In addition, every domain – especially mission critical domains – has a body of <sup>b</sup>knowledge<sup>Q</sup> used to <sup>b</sup>interpret and understand that world<sup>Q</sup> [33,44]. This <sup>b</sup>shared understanding<sup>Q</sup> [73] become <sup>b</sup>domain models, or ontologies<sup>Q</sup> [92] that regularize the terminology, a pragmatic extension to most ontological research today.

The research began with ethnographic methods that have been used for requirements gathering [31,48,49,87] because they effectively elicit the necessary domain knowledge from experts. The data captured from ethnographic methods are useful for scenario, goal-oriented, and use-case research. These qualitative research approaches were synthesized [52] in order to capture as much of the domain intricacies [21] as possible in conjunction with other relevant concepts. The original research extended that synthesized utility to software architectures [4,28,52,55, 68,75,83,92,93,96,97]. We propose the synthesis of this research is applicable for DSS design research with modifications.

## 3.2. Site selection

The field site for this research effort was initially a Grid Dispatch Control Center (GDCC) of a major West Coast utility. The system analysts at GDCC were required to design information systems based on numerous constraints arising from different stakeholder groups, e.g., FERC, State Public Utility Commission, and other organizations. Their constraints were often contradictory, which put the system analyst in the position of having to interpret many ambiguous or contradictory policy documents in order to arrive at an equitable solution to be embedded in the software. The GDCC management was interested in gaining a clearer picture of the design process to facilitate interorganizational negotiations with the Independent System Operator established by California state law AB1890.

## 3.3. Data collection

The electric power grid system (including its ICT) is constantly undergoing a morphogenic process. Since legacy IS and software are common in most mission critical infrastructure, a data-driven approach using the methods detailed below will provide a view of system variety, component behaviors, and interactions. Data were collected at different locations and levels through a variety of methods: semi-structured and unstructured interviews; reviews of company and industry documentation; observation of operations and organizational activities; participation in IEEE standards making activities associated with the industry. This triangulation through several theoretical perspectives of various techniques of data collection provided multiple perspectives to identify emerging phenomena.

The first author started with ethnographic methods such as observation in order to carefully describe the domain without contamination from informant opinions. Thus, the observations were taken from an uninformed perspective. This approach facilitates the discovery of information that informants often take for granted or have integrated within their subconscious specific activities associated with daily work habits. Also, when planned software upgrades or unexpected events occurred (e.g., disturbance in the grid system), the observer was allowed to remain in the GDCC. All grid dispatch personnel on both 12-h shifts were observed randomly throughout the field study, but this was later augmented with impromptu and semiformal extended interviews.

These initial semi-structured, then unstructured, and later impromptu interviews were conducted with a cross-section of the grid dispatch informants to gather data about the impacts from deregulation; their duties; the technology they had used and were now being forced to utilize; and the organization as a whole. These interviews provided information about the general operation of the GDCC, an operator’s role as a member of the GDCC team, and important insights these skilled individuals had about the industry in general. Support staff outside the main GDCC was also interviewed to get other perspectives.

Informants included all supervisors, upper management, IS analysts who designed and developed GDCC software to support the GDCC operators; electric power marketers and forecasters who interacted with the GDCC operators in planning processes; management; and accountants who monitored the result of the operations for discrepancies. At least one individual from each control center duty station was semi-formally interviewed, which totaled 30 h of taped interviews (see [53] for actual data such as recordings of interviews). The field data collected were analyzed to determine constraint–resource associations and determine critical relationships. In addition, sporadic observations, conversations, and interviews were conducted with operators acting in the marketing function and support staff such as accountants or forecasters.

Pointers to additional materials such as Standard Operating Procedures, Federal and State Law, organizational tariffs, etc. were given to the researcher during the interactions with the informants. These additional materials provided a quantifiable baseline in this domain but did not represent how things were necessarily implemented or run. These ideal structures and models inform us of the industry’s <sup>b</sup>shared understanding<sup>Q</sup> [52,95] in the same way Weber’s ideal organization [104] can be leveraged to understand how real organizations work. The ideal structure must be compared with field data for a clearer view of the critical relationships.

This research is premised on the knowledge that the <sup>b</sup>system<sup>Q</sup> under design suffers from numerous crosscutting effects [52]. Field data regarding the activities of individuals from the GDCC and general electric power industry will play a vital role in DSS design in this domain. However, the appropriate research methods must be applied to extract the relevant information for humans intuitively grappling with the wicked infrastructural problems. Without these data, the design of DSS will lack real-world relevance and will not seize the opportunity to move onto the next generation of problems–solutions fostered by agile markets, mergers, and integrated technological solutions.

## 3.4. General decision-making approaches

Based on these data, a model was developed and applied to a software architecture design and development tool suite [52]. The emerging model evolved based on the data and repeatedly applying some basic tenets of SE and IS analysis and design methods. The model needed to be iterative and incremental, i.e., concurrently modifying model, domain analysis, and tool design based on new data. Iteration allows for analysis either with prior results based on the same theoretical baseline or differing theoretical perspectives. The incremental nature of the model is nothing new to decision-making since [54] noted it as both <sup>b</sup>incrementalism<sup>Q</sup> [57] amounting to successive limited comparisons, and <sup>b</sup>local search<sup>Q</sup> [22] that is simplistic reactionist managing. The model should reflect the decision elements summarized by [54] (presented in the Table 1) and juxtaposed to traditional SE and IS analysis and design to draw out their similarities. The five elements indicated in Table 1 are integrated throughout the DSS Design Model (presented later).

Table 1  
Elements highlight areas and issues in design decision-making

<table><tr><td colspan="2">From Kleindorfer [54]</td><td>From SE and IS</td></tr><tr><td>Decision elements</td><td>Decision sciences</td><td>Historical analysis and design</td></tr><tr><td>Problem finding</td><td>What is the real problem?</td><td>What is the actual problem domain?</td></tr><tr><td>Institutional arrangements</td><td>Stakeholder analysis to measure their goals, views, objectives, constraints, and agendas</td><td>Stakeholder and user analysis to determine the real requirements</td></tr><tr><td>Information gathering</td><td>Both objective and subjective facts, assumptions, and values</td><td>Circumscribe application and problem domain</td></tr><tr><td>Choice process</td><td>What approaches to choices should be considered?</td><td>Are the requirements valid and verifiable?</td></tr><tr><td>Implementation</td><td>Specific approach using feedback, legitimization, and control through accounting</td><td>Traceability and model checking between process stages</td></tr></table>

## 4. DSS Design Model

Designer researchers and practitioners can utilize this new DSS Design Model framework to develop a sense of systemic <sup>b</sup>trajectory<sup>Q</sup> [41,42] associated with these implementations that evolve over decades. This understanding is necessary to address wicked problems [79] arising from domain constraints not typically a concern of designers [52,53]. The research process we followed was based on the theoretical and methodological framework presented earlier. The systemic considerations when developing this model are a reflection of these approaches. We have generalized the research process as a model while simultaneously validating and evolving it (see Discussion). The five decision elements (Table 1) are integrated throughout the DSS Design Model, but are most heavily concentrated around and within the theory and analysis component (shown later). A unified graphical representation (Fig. 4) of the DSS Design Model is shown at the end of this section.

Conventional infrastructure (e.g., electric power, telecommunications) generates data from the physical urban infrastructure and the ICT that is utilized in the operations and accounting of the built infrastructure (Figs. 1 and 4). These two legacy systems should be modeled as separate but tightly coupled components (i.e., represented in the image by them touching in a stacked formation) to demonstrate the strong dependency between them. A great deal of the morphogenic evolution is a direct result of symbiotic relationships that exist between the system domain component and the information infrastructure component, which must be considered separately, but simultaneously during data collection.

![](/api/attachments/THX5Z32S/fulltext/images/404ac3300c2bcac3952f74d2903e7cce91faa89694b51f76f314ce732d2b1519.jpg)  
Fig. 1. The real-world; ICT supporting urban infrastructure.

![](/api/attachments/THX5Z32S/fulltext/images/67c6a2921d36bdf1a4129dffa89a2686a7191ae74a6f3ac1caf6637802741557.jpg)  
Fig. 2. Multiple data feeds into theory and analysis with feedback to the domain. Synchronous data or information exchange (Box #1) between entities.

The research model has three primary interactions with auxiliary feedback loops that are necessary based on the underlying CAS theoretical framework. The applied theoretical constructs (e.g., descriptive approaches such as ethnography or Grounded theory) determine initial incremental steps through the model, but later increments are guided by the inherent feedback loops. The incremental relationships in the model components allow testing of theoretical conjectures without jeopardizing the actual operation of the infrastructure, thus satisfying a fundamental constraint from the domain. Also, the increments create temporal milestones. This process necessitates the utilization of a nondeterministic and descriptive SDLC. The combination of these conceptual constructs provides a great deal of intellectual leverage over the process, but also greatly increases the complexity of the seemingly simple DSS Design Model.

The remainder of the model consists of the following components: theory and analysis, simulation, decision/design. Two-headed arrows between model components (Figs. 2–4) indicate an interaction leading to information exchange in both directions. The dotted line indicates an interaction that can be a real-time synchronous exchange of information. We will use the interactions between the DSS Design Model components to discuss these components and model specifics, i.e., data–theory interaction; simulation–theory interaction; decision/design interaction.

![](/api/attachments/THX5Z32S/fulltext/images/19e11141aba385b7a4577ae1082099f0700f61f01dfdb848efb995a366ca9171.jpg)  
Fig. 3. Simulation: the added component interacts with theory and analysis (Box #2)

![](/api/attachments/THX5Z32S/fulltext/images/6069b607fcf774b76e19caa24be1b57454b48a329b26d9e644f560ea9c029d64.jpg)  
Fig. 4. DSS Design Model. This visual representation infers both iteration and incremental activities, but no predetermined pattern is inferred— only a general morphogenic process contained within the CAS theoretical framework.

## 4.1. Phase I: data–theory interaction

The research is driven by the available data. Qualitative techniques (e.g., ethnographic methods) were used because of the lack of experience of the researcher and the deep domain knowledge of the informants. This dichotomy facilitates good data collection using ethnographic methods. Based on field data in the electric power industry, it became obvious that a conceptual framework (with the associated technical mechanisms) was needed to utilize numerous theoretical constructs due to the variety of data in the domain. Also, many qualitative methods (e.g., ethnomethodology [32]) do not scale well, so there must be an underlying theoretical motivation for different data collection and analysis approaches during subsequent iterations through the model.

Our DSS Design Model incorporates an introspective analysis that maps well into the future DSS research agenda proposed by Nemati et al. [66]. Specifically, they said, <sup>b</sup>one research area of DSS becomes the development of a set of theoretical foundations upon which to build future development and applications<sup>Q</sup>. They went on to further specify the combining of theoretical perspectives, such as <sup>b</sup>Gestalt theory of insight [39 [sic]] combined with Newell and Simon’s [46 [sic]] theory<sup>Q</sup> or <sup>b</sup>Cognitive dissonance and Perkin’s [51 [sic]] theory of understanding<sup>Q</sup>, to achieve <sup>b</sup>a solid foundation for new knowledge generation<sup>Q</sup> [66]. In our DSS Design Model, if the introspective analysis indicates the necessity to use a different theory, it is integrated within the CAS framework and data collection resumes.

The relation between the theory component and domain (Fig. 2) is maintained to continuously integrate emerging data and update the theory (e.g., if a Grounded theoretic approach is utilized [70]). The real-time synchronous exchange of information (represented by the dotted line and Box #1) can result in an immediate evolution of ideas, concepts, and viewpoints is possible, e.g., analysts/theoreticians or practitioners meeting with domain experts to exchange ideas. Two other data feeds influence the choice of theory.

A direct feedback arrow (curved arrow on top of Figs. 2 and 4) from the information infrastructure indicates a purely technical data feed from the specific DSS or general IS (e.g., integration testing). Based on the CAS theoretical framework, we assert SDLC activities that are normally after design (e.g., testing, deployment, maintenance) are not independent, but a natural morphogenic outcome of the design activity. Thus, the single feedback arrow from the information architecture component captures the necessary data for design from these concurrent or later SDLC activities. More recent agile SDLC configurations (e.g., eXtreme Programming [5]) have radically rearranged the order of activities such that testing is before design, which means the testing becomes an aspect of the theoretical analysis from a software engineering perspective (e.g., software engineering) and the simulation of component-based techniques are applied. The second data feed into the theory and analysis are from the simulation component described in the next subsection.

## 4.2. Phase II: simulation–theory interaction

The integrated theories (i.e., in theory component) at any particular increment during an iteration of the DSS Design Model dictates many aspects of the overall model execution. Obviously, the choice of theories should be predicated on the research goals, existence of prior collected data, and results from previous theoretical analysis, all of which may or may not be consistent with the current theoretical component. Since the type of data collection and analysis techniques are mandated by the theory, it is only logical these same constraints will guide the simulation design. The basic CAS tenets of integration and morphogenesis through interpretation of domain variety captured in feedback mechanisms factor heavily into the DSS Design Model capability to oscillate somewhere between the conceptual opposites of organized complexity and chaotic complexity, e.g., to a lesser degree, but somewhat analogous to prescriptive and descriptive SDLC.

The morphogenetic approach utilized in this research resulted in the modification of the design model itself through the addition of the simulation component to the model (Figs. 3 and 4). Decisionmaking processes often employ some sort of critical abstraction akin to simulation to reduce the information overload most humans suffer with in mission critical domains. For example, the California Energy Commission has a large contingent of analysts that use data in mathematical models and simulations in order to advise policy decision-makers. Although simulation is one of the common three modeling paradigms (i.e., linear programming, simulation, and spreadsheet models) [66], the field data indicated that it needed to take an even more prominent role due to the mission critical nature of build infrastructure and their dependence on simulation.

Simulation is still used for information infrastructure modeling, but with a more expanded role than typically ascribed to it. The simulation referred to in this case can be of the traditional type [56] or a type modified to hide simulation complexity from a particular stakeholder group [7], wherein the simulation output is analyzed (i.e., Fig. 3, Box #2 input arrowhead to theory/analysis component). The utilization of domain-specific knowledge in [7] has similarities with this DSS Design Model. Typically, the GDCC simulation resulted in an evolutionary prototype [86] similar to that used in [64] for software architecture modeling, which demonstrates another aspect of the technical feasibility of the theoretical synthesis underlying the DSS Design Model.

The simulation and theoretical components leverage the flexibility provided by modern software engineering and software architectures techniques to integrate theoretically grounded assertions with the data feed. Emerging technologies are used to dynamically replace and integrate computational components within systems. Thus, from a fundamental inception of the DSS, the design incrementally becomes more like the real-world artifact. To make the transition theoretically sound, we have leveraged a holistic simulation theory developed by Zeigler during the General Systems Theory era, but evolved to its current capability [108]. One reason for the choice of Zeigler theory was its natural overlap with the CAS theoretical framework such as the shared morphogenic properties and componentbased approach to modeling. However, the transition from simulation theory (e.g., Zeigler) to componentbased prototype creates a need to change theoretical perspectives. In addition, some design recommendations from the simulation or software component architecture may be self-evident for use in the decision process, i.e., not requiring theoretically based analysis) resulting in a decision/design feedback for the human actors described next.

## 4.3. Phase III: decision/design interaction

The cumulative effect of the theoretical analysis and/or simulation can combine to dynamically influence the design decision-making process (Fig. 4, Box #3). Decision-makers such as IS analysts, software engineers, project managers, and other primary stakeholders interpret these inputs based on their <sup>b</sup>shared understanding<sup>Q</sup> [52,95] of the relevant domain resource constraints. Thus, the combination of theory and simulation will inevitably impact the decisions, but only to the degree that it does not violate the decision-makers’ shared understanding of the design goals.

These decisions may be made in real-time as the various stakeholders observe the prototype as it is time-spliced into the working infrastructure as observed at the GDCC. By choosing different time increments, their subjective impression of the design will be altered in a nondeterministic manner because the data are live and random based on the electric power customer base. For example, if a high-power transmission line goes offline due to an airplane accident while the prototype is running, the software may crash bringing down the entire system leaving a lasting impression that may kill the development project. As noted earlier in the theoretical background, this systemic behavior is the nature of real-world design and, more generally, of wicked problems. The design decisions impact the built information infrastructure (i.e., Fig. 4, Box #4) that needs to be factored into a systemic model.

Newly integrated design decisions immediately impact the symbiotic relation between the information infrastructure and the domain thereby completing the first full iteration since the general iterative flow of data shown in Fig. 4 is counterclockwise. Note, however, depending on the data, the theory or theories utilized, and the type(s) of simulation/prototypes developed there may be an undetermined number of incremental steps in any particular iteration through the entire DSS Design Model.

## 5. Discussion

<sup>b</sup>Indeed, it is precisely in the exploration of <sup>T</sup>wicked problems<sup>d</sup> for which conflicting or sparse theoretical bases exist that design research excels (March and Smith, 1995; Carroll and Kellogg, 1989)<sup>Q</sup>. V. Vaish navi and W. Kuechler [101].

A basic disconnect exists between the theoretical framework used by the electric power industry architects and the IS designers who actually built the grid information infrastructure. The mismatch between their theories and reality demonstrates the need for DSS designers to pursue more comprehensive approaches in order to correctly match or address the domain constraints that greatly contribute to the evolution of the system.

The DSS Design Model takes a step toward correcting the mismatch between theory and design practice. We discuss how the model was validated through three separate activities: a software architecture tool development; a microgrid design case; and our current field work in the mission critical telecommunications domain where we are designing a Knowledge Management DSS (KMDSS) for network operators to use in alarm correlation.

## 5.1. Reduction of mismatches

The DSS Design Model presented here seeks to reduce the theory–design mismatch by tightly coupling the theoretical aspects of DSS design into the SDLC and implemented process. Our motivation for this approach was domain instances. The FERC made deregulatory decisions regarding the electric power industry based on several different groups of powerful lobbyists, committees, and political bodies. For example, the FERC made many of the specific design decisions [67] based on <sup>b</sup>What<sup>Q</sup> and <sup>b</sup>How<sup>Q</sup> panels of industry experts. It is interesting to note the strong correlation with the traditional requirements engineering what–how rule of thumb [86]. Primary economic arguments came from the Energy Power Research Institute (EPRI), the public at large, or economists [26,69,82].

Economists utilized various theoretical frameworks, such as Game Theory and Cournot–Nash Equilibrium, to arrive at suggestions that deregulators largely followed. Often, the economic arguments were combined with other research disciplines to adapt their theories to empirical data. For instance, after observing certain market behavior, EPRI researchers [19] presented an economic market making argument leveraging Kirchoff’s laws of electric power flow by developing an engineering–economic model of the electric power network [94]. Local grid operations personnel, in contrast to these economic arguments, utilized ICT developed by IS analysts based more on a shared understanding of the electric power industry and a heuristic approach that was more in line with how their people made decisions. Thus, the electric power deregulation debacle in California resulted in part from this paradigm mismatch in DSS design that was directly tied to theoretical assumptions and expectations not matching the ICT designs and implementations in the field.

## 5.2. The ArckBuilder case

The DSS Design Model described earlier was utilized as the basis from which to concurrently evolve a specific instance of a software architecture tool suite (ArckBuilder) [52]. The ArckBuilder implementation encourages a particular architectural process. ArckBuilder is presented here as an example of how design research concepts and the results from qualitative methods can be integrated into tool environments in the future within the CAS theoretical framework.

Each domain resource has a set of behavioral constraints (e.g., specifications) that are captured in the resource service proxy, i.e., in a service-oriented architectural style similar to [3]. As noted by [63], components can be evolved by modifying a subset of the <sup>b</sup>component’s properties, e.g., interface, behavior, or implementation<sup>Q</sup>. ArckBuilder understands and classifies those features of an architectural description that are placed in property lists. Thus, architecture constructed using service proxies must adapt to resource constraints using the properties associated with these proxies. The existence of these proxies within the domain guides and, where necessary, restrains the crosscutting influence by various stakeholder demands.

There are three ArckBuilder components that have the following functionality: Harvester gathers resources from the web; CARESA (Computer-aided Requirements Engineering with Software Architectures) component addresses evolution, requirements negotiation, and stylistic constraints; and CASA (Computer-aided Software Architecture) is a canvas type of interface for design, technical collaboration, and stylistic views.

The Harvester component gathers resource proxies from the dispersed domain (e.g., electric power industry). These proxies are connected to live or simulated resources. Since the proxies are strongly typed interfaces, they can be categorized within the overall domain classification called a <sup>b</sup>catalog<sup>Q</sup> [52]. The CARESA component is a use-case based interface that is the front end for a tuple space (e.g., Linda [76]). Stakeholders using the CARESA interface enumerate constraints that are then transformed into strongly typed objects within the space. Requirements engineers, system analysts, and/or software architects act as the mediators to guide the constraint negotiations. Their expertise emerges through this process.

The CASA component is the heart of the Arck-Builder suite because it uses the Harvester and CARESA components in the design process. An up-to-date catalog is downloaded from the Harvester server whenever the software architect needs a revision. The service proxies are used in the canvas area of the tool to construct system architectures that combine all types of resources. After computationally combining and instantiating the new component, it appears in the canvas. Different components are combined using first-class architectural connectors, which themselves are derived from services (e.g., telecommunication infrastructure for a distributed system). The entire architecture can then be exported as an executable file that dynamically simulates the aggregated service behavior.

ArckBuilder makes use of a strongly typed programming language to maintain <sup>b</sup>shared understanding<sup>Q</sup> consistent, which is necessary as indicated by the data. The tool has been presented in a cursory manner to demonstrate that it is possible to complete the process from qualitative data acquisition to design, and then to a finished instantiated software architecture environment. Also, designing in the architectural context with trusted components greatly obfuscates or eradicates traditional SDLC stages. Once the essential design decisions arising from the theory and analysis are complete, the other activities such as testing, implementation, and deployment occur in a nondeterministic manner.

DSS projects utilizing the DSS Design Model to achieve similar functionality as the ArckBuilder design would provide the capability to mix and match computational components derived from varying theoretical perspectives in order to juxtapose the results and guide decision-making. Utilizing the varying apertures of differing theoretical lenses, architectural component/connector replacement and reuse provides something new for decision-makers—the ability to dynamically juxtapose service offerings concurrently with real-world observations of infrastructural behavior in a design context.

## 5.3. Microgrid EMS-DSS analysis mini-case

The DSS Design Model was conceptually validated in a project described by the following minicase. We were investigating the representational sufficiency of the model with analytical and field data entirely separate from the original field site location. The following subsections correlate with the various DSS Design Model components that were incrementally, concurrently, and iteratively put into operation in the field. An advanced energy management system (EMS) DSS was needed to support a commercial park’s coordinated electricity marketplace. The EMS-DSS project was not completed due to killer issues associated with high-level requirements [8,9] (explained later), but the DSS Design Model was introspectively evolved and its use during this process will demonstrate the flexibility in the model. Some specific constraints will be discussed below to elaborate the domain.

## 5.3.1. Domain-information infrastructure component: commercial park niche market

Regulators were trying to decrease the cost of electricity for customers. Organizations were responding to pressures and incentives created by deregulation. Skyrocketing prices in California dramatized the emerging competitive market. California’s high-tech industry is reflected in its load configuration that demands high-quality electricity. Evolving the common centralized distribution paradigm into a market by utilizing an ICT augmented microgrid is a logical, but controversial, outcome of deregulation. There were numerous policies and laws that contradicted each other. In addition, contradicting hypothesis could be deduced using economic policies associated with deregulation, microgrid economics [39], and interconnection standards (i.e., IEEE P1547 at that time). Policy makers (e.g., California and FERC regulators; Department of Energy) were DER supporters.

Commercial parks specializing in niche markets providing power quality and/or special pricing arrangements to high-tech tenants could meet these new market demands. Parks have several potential market offerings because they can act as value added reseller of <sup>b</sup>ancillary services<sup>Q</sup> [51,72,94] necessary in the deregulated market. Tenants can outsource power problems to park owners or their consulting firms. These arrangements essentially redefine historical control relationships creating service economies.

The <sup>b</sup>microgrid<sup>Q</sup> (i.e., microcosm of the normal grid) is a fundamental component in an experimental commercial park planned as a 200-acre, 2.4 million square foot joint venture. The park design utilized a microgrid that consisted of Distributed Energy Resources (DER), i.e., combined heat, cooling and power (CHP), fuel cells, micro-turbine generators, and photovoltaics, power storage facilities, and intelligent network devices. The design combined the microgrid with ICT to create niche services that would result in an internal electric power marketplace.

## 5.3.2. Theory/analysis component: stakeholder data

The CAS theoretical premises used in this case were the same as before. Initially, we conjectured most of the integration work would be technical and would be relying on mechanical, civil, and other engineering approaches. However, the inclusion of economic theory was inevitable, but later iterations of the model revealed an electricity auction marketplace would be necessary with its associated theory [18,29]. As the project progressed, it also became apparent that the utilities utilized the interconnection standards to maintain control over what DER could be used—even equipment entirely on private property needed their approval. The study of standards theories [25] was necessary because of the prominent role the interconnection issue assumed. Trust theories were under consideration because of the inevitable situation where marketplace competitors should change to collaborators due to a disruptive microgrid state change event. Also, requirements regarding interconnection and dynamic architecture configuration management capabilities were determined from stakeholders. The theories guided data collection and requirements analysis, but did not completely alleviate conflicting requirements, which fostered extensive complexity.

The data collection methods in this case were similar to those used earlier, but with no observation because the project was primarily conceptual. Data collection began with the academic engineers to discern the technical constraints and requirements associated with DER. Other park stakeholders were included as we iterated through the model. The politicalization of the microgrid project necessitated data collection from the California Energy Commission and Department of Energy. Policy makers suggested that processes controlled by utilities (i.e., the DER interconnection) created market barriers by artificially inflating integration costs. Policy theory also created contradictions with electric power engineering methods. Thus, both streams of data were relevant. Utility representatives were interviewed since it represented a major constraint in the project. Data were gathered from DER vendor specifications and personnel who were involved in their software engineering projects. The first author participated in the IEEE interconnection standardization process, which included documentation and meetings with all stakeholders present, to collect data. The engineers provided DER prototype operational data and we collaboratively developed simulations discussed next.

## 5.3.3. Simulation component: triangulating the behaviors

We utilized three general types of simulations in order to determine the behavior of the domain-specific resources. The academic engineers and their graduate students were currently utilizing hand-coded simulations to model the various DER devices. The simulation data were compared to the DER prototypes in the laboratory and verified to be accurate. The second type of simulations was generated from commercial packages (e.g., Simulink by MathWorks) and were utilized to model common electric power and mechanical engineering devices, which were assembled into larger components (e.g., as part of the interconnection). The third type of simulation was a serviceoriented one developed as part of ArckBuilder (see prior subsection) to model the entire commercial park and microgrid. Each resource owner (e.g., DER) would have to develop a service proxy that could then be assembled into an ArckBuilder model. The service proxy to represent one of the other simulations or a real-world artifact. Since the proxies were written in Java and represented live services, they could all be instantiated as Java objects and executed simultaneously.

The DSS Design Model guided our decisions as to which services to create and how to design them based on theories pertaining to domain constraints such as markets or auctions. Each theory was instructive about how to represent a resource as a service. Future work was discussed where we were going to use Game theory or Trust theories to determine how much data to collect or provide through the service proxies, which were entirely different considerations from software or mechanical engineering.

## 5.3.4. Decision/design component: multiple stakeholder agendas

EMS-DSS designers must make the decision as to what theoretical perspectives to base future prototypes upon—a wicked problem given the contradictions in theory and data. The flexibility of component services architectures partially offsets these decision complexities. The design of the experimental park facility that was suggested to the stakeholders and agreed upon enabled the leveraging of service architectures. The EMS-DSS design provided the capability to connect the components into microgrid systems. This approach provides maximum flexibility for architectural variety of microgrids in order to test various market scenarios.

The natural gas, electrical microgrid, and computational infrastructures had to accommodate DER in cooperation with local gas and electric utilities. The eventual park design provided:

1. Various alternative distribution options such as a premium power circuit.

2. A context dependent bridge between networks with interlocking capabilities.

3. Unified constant–frequency integration control devices [109].

4. Multiple electric power network designs (radial or network).

5. Multi-point power quality monitoring such as power flow, or harmonics.

## 5.3.5. Postmortem of the EMS-DSS: need to develop foresight with theory

The microgrid project was more narrowly defined than the initial case because the academic engineers and policy makers wanted DER to succeed in the park. However, it was no less <sup>b</sup>wicked<sup>Q</sup> due to unrevealed agendas. System failures are often linked to undiscovered <sup>b</sup>killer requirements<sup>Q</sup> [8,9] that are inherently obfuscated because they are entangled in the domain details. <sup>b</sup>High-level requirements<sup>Q</sup> [8,9], on the other hand, focus on other aspects of the process to determine killer issues, such as political drivers.

We were unable to solve these high-level requirements problems as described next.

The utility was a mandatory stakeholder due to the legacy policies. Their behavior was inconsistent with their own SOP, which indicated they were treating the park in a special manner, possibly due to the market threat an independent park running their own microgrid represented. One instance of an artificial barrier is electric power network data collection. They insisted the utility would install the data collection devices, but refused to put in enough devices to facilitate the accurate architectural reconfiguration of the microgrid by the EMS-DSS. Also, we discovered late in the SDLC that the DER vendors were competing with each other to develop proprietary EMS-DSS of their own. Thus, they would not share interface information necessary to build the appropriate service proxies. The inevitable result was the project stalled and the park owner, although already putting in additional built infrastructure for the experiment, lost incentive to continue because of the economic downturn changed their agenda too.

These types of deviant behavior can be addressed with the appropriate sociological theory but is not easily teased out a priori even when killer requirements are suspected. Although the CAS theoretical framework and the DSS Design Model enable multiple theory utilization, it will take further research to determine how to combine and compare theoretical perspectives, especially when the results are contradictory. We discuss current research next, which is intended to further validate our past work in the electric power industry.

## 5.4. A KMDSS for telecomm network operators

Strategic planning promises to become even more complex in the future, as the Internet and telecommunications technology will allow more organizations to become global in nature, and suppliers, producers and customers will become more closely connected throughout the world. J. Courtney [20; Section 2.2, pp. 20 (i.e., pp. 4 of 22)].

We are currently using the DSS Design Model for a semi-automated fault diagnosis system [65]: the Alarm Correlation Tool (ACT). These types of systems have traditionally assisted operators in maintaining global optical telecommunications networks from command and controls centers, but with narrow applicability and limited success. ACT must be integrated with current ICT deployed in the global network to provide <sup>b</sup>clearer<sup>Q</sup> solutions to network faults than is currently available. The tool must be designed using a global, sociotechnical, and geopolitical awareness [80]. Due to the application of the DSS Design Model, we have determined that the ACT must be designed as a KM augmented DSS [80].

## 5.4.1. Domain-information infrastructure component: tracking faults around the globe

A Network Management System (NMS) monitors the global optical network domain we are examining. The field environment forces significant constraints on the design of the system. The global optical networks in question are mission critical and provide vital aspects of national security. Node-tonode communications used by multiple instances of the ACT are facilitated via the network management Data Communications Network (DCN). Finally, the ACT must be designed to work at the various levels of hierarchical reporting schemas available in the network. This hierarchy is based on the principle that a central Network Management Center (NMC) has overall coordination responsibility for the entire global network, i.e., the operation of every node. Thus, inter-node activities are monitored and coordinated through the NMC. This constraint implies that the ACT must function at a local jurisdiction within a node while still supporting overall network end-to-end fault diagnosis at the NMC level: i.e., a requirement not met by prior industry tools.

The operators of these networks who will use ACT are comprised of loosely coupled, inter-organizational, virtual teams distributed in various geopolitical domains. These users must coordinate their efforts and share knowledge premised on the emerging technical and social state of affairs within the context of each nation’s security. Also, members of the teams vary greatly in experience, prior knowledge, and the diagnosis process they have adopted.

## 5.4.2. Theory/analysis component

An extensive review of the various correlation algorithms available in the literature is provided by [65]. The initial iterations of the DSS Design Model were largely influenced by traditional DSS design theory [77,78,88,40] because of the existence of a well-defined application domain. However, after following the model’s guidelines, a different set of problems was identified. The data collection and analysis from domain feedback showed that there was a need to address: the geopolitical aspects in the domain; knowledge capture; knowledge transfer between command and control centers; a wide variety of users. The existing DSS theories we were using did not address these challenging demands. During a subsequent iteration, we have explored aspects of the Emergent Knowledge Processes theoretical perspective [59] because it has several principles we are finding useful, such as the emergent nature of knowledge sharing and dealing with <sup>b</sup>naı¨ve<sup>Q</sup> users given the unpredictability of the global user base for the ACT. A rigorous, multiple field site evaluation of the ACT prototypes will generate empirical data in future iterations of the DSS Design Model.

Data were collected for use with rule-based correlation algorithms that were the first attempt at an ACT design solution. Further analysis by domain experts showed that determining all rules covering all possible fault scenarios would prove prohibitive. Subsequent DSS Design model iterations demonstrated a model-based approach appeared to capture most common scenarios, while rules could be integrated into the design in order to capture the more extraneous scenarios. During future iterations, we will juxtapose theories regarding correlation algorithms with other relevant theories to perform data analysis.

The ACT is intended to integrate with the currently deployed NMS. Therefore, the ACT must interface to the local NMS to retrieve both fault data and network topology models. Every network node runs an instance of the ACT. As local engineers gain experience, they will theoretically be able to capture this knowledge in the form of updated models and/or rules in the system. An instance of ACT will distribute these data and knowledge to other nodes, where other ACT instances are running. Finally, at the NMC, a <sup>b</sup>higher-level<sup>Q</sup> ACT must be able to integrate root causes determined by each node’s ACT to create end-to-end root cause analysis.

## 5.4.3. Simulation component: merging prototypes with existing applications

It is imperative to simulate the behavior of the correlation algorithms and specific fault scenarios to verify that the tool is operating properly. Simulation is necessary because the ACT operates on real-time alarm data retrieved from the NMS that exhibit characteristic, uncharacteristic, and false positive behavior. Telecommunications suppliers in industry have progressively developed complex transmission and equipment simulators that provide a basis for testing theories and hypotheses as necessary. These commercial simulators can be interchanged as complete components per the DSS Design Model. The simulators can be exchanged in parallel with the various algorithms in the ACT prototypes to better understand the optimal configuration.

## 5.4.4. Decision/design component: extending their ability to share knowledge

The first iteration of the design model resulted in a simple correlator system to assist in local diagnosis; i.e., it did not include knowledge management techniques in the design. The next iteration included the use of rule-based correlation only. Through simulations and domain expert feedback, it was determined that a model-based addition would allow for capturing more scenarios with less user effort or cognitive load. However, field data indicated management of knowledge to be an important factor in daily operations. Therefore, next iteration introduced a KM design aspect that allowed for sharing of acquired knowledge. The current design iteration is a modular, hierarchical alarm correlation system. We are also working on the new requirement to provide knowledge sharing across the entire network. This latest design activity requires the exploration of theories of knowledge to inform our existing kernel theories. The CAS theoretical framework facilitates this integration because it separates the concepts of data and information, thereby lending itself to knowledge theories.

By utilizing this new DSS Design Model, we have evolved the ACT design while investigating the appropriate algorithms and architectural combinations to deploy in the system. We are able to analyze various algorithms and use simulation techniques to verify their proper behavior. Furthermore, by taking into account the domain constraints as well as the existing ICT infrastructure, the design was augmented to allow for more successful integration in the field. In addition, we are able to progressively integrate more appropriate theories for design of the ACT KMDSS.

## 6. Conclusion

The new DSS Design Model presented in this paper has evolved over time to address the <sup>b</sup>wicked<sup>Q</sup> design problem we became aware of during our initial field study in the complex, mission critical electric power industry. The model reflects a long process of data collection and validation within a Complex Adaptive Systems (CAS) theoretical framework that itself proposes the integrated use of numerous theories and approaches. Utilizing the CAS framework has resulted in a multidimensional approach to design research that leverages theoretical concepts, ranging from deep qualitative methods to software engineering practices, in various complimenting ways. This paper has explained the model using following contexts: conceptual rigor, technical instantiation, minicase study, and ongoing empirical evaluation. Using this model in an adaptive manner should experientially lead researchers to a new understanding of what DSS design must become.

The new DSS Design Model suggests future design processes will be evolutionary and iteratively encompass dynamic theory–simulation–and decisionmaking interactions. Although simple in appearance, when the DSS Design Model is understood within the CAS framework, it assumes a dynamic complexity that no prescriptive software development life cycle (SDLC) or process is capable of mastering. The new DSS Design Model is conceptually a multithreaded configuration with dynamic runtime behavior playing out in concurrent operations. So far, we have only been able to instantiate this new DSS Design Model using software architecture research techniques that have the capability for stylistic adaptation to domain-specific complexity. Another advantage of including software architecture methods is that we were then able to analyze DSS prototype behavior and interactions based on various theoretical perspectives through component services. Therefore, we have instantiated a multi-theoretic process with certain basic similarities to the approach suggested by Nemati et al. [66].

The new DSS Design Model was devised during a period of great upheaval associated with electric power industry deregulation spurred on by increasing sociotechnical dependencies on Internet technologies [53]. To further validate the model and test its general applicability to other mission critical infrastructure, we are conducting a more narrowly focused development of a KMDSS for use in global telecommunications fault correlation.

## Acknowledgements

The authors wish to especially thank John L. King, Dean of the School of Information, University of Michigan, for his support and many insights including, but not limited too, the very essence of the design model presented in this paper. We would like to acknowledge and thank Professor Jerry Fjermestad for his insights and recommendations. Also, we are very grateful to the anonymous reviewers for their guidance.

## References

[1] C.Y. Baldwin, What can the social sciences gain from the science of design? in: K. Sullivan (Ed.), NSF Workshop on the Science of Design: Software and Software-Intensive Systems, NSF, Airlie Center, VA, 2003, p. 2.

[2] R. Banach, M. Poppleton, Retrenching partial requirements into system definitions: a simple feature interaction case study, Requirements Engineering 8 (4) (2003 November) 266– 288.

[3] L. Baresi, R. Heckel, S. Tho¨ne, D. Varro´, Modeling and validation of service-oriented architectures: application vs. style, Proceedings of the 9th European Software Engineering Conference and 10th ACM SIGSOFT Foundations of Software Engineering, ACM, Helsinki, Finland, 2003, pp. 68– 77.

[4] L. Bass, P. Clements, R. Kazman, Software Architecture in Practice, Addison-Wesley, Reading, MA, 1998, p. 452.

[5] K. Beck, M. Fowler, Planning Extreme Programming, Addison-Wesley Publishing Co, Reading, MA, 2000, p. 160.

[6] M. Begovic, D. Novosel, M. Milisavljevic, Trends in power system protection and control, Decision Support Systems 30 (2001) 269–278.

[7] R. Belz, P. Mertens, Combining knowledge-based systems and simulation to solve rescheduling problems, Decision Support Systems 17 (2) (1996 May) 141– 157.

[8] M. Bergman, J. King, K. Lyytinen, Large scale requirements analysis as heterogeneous engineering, in: C. Floyd, R. Klischewski (Eds.), Social Thinking—Software Practice, MIT Press, Cambridge, MA, 2000.

[9] M. Bergman, J.L. King, K. Lyytinen, Large scale requirements analysis revisited: the need for understanding the political ecology of requirements engineering, Requirements Engineering 7 (3) (2002) 152– 171.

[10] D.M. Berman, J.T. O’Connor, Who Owns the Sun: People, Politics, and the Struggle for a Solar Economy, Chelsea Green Pub. Co, White River Junction, VT, 1996, p. 331.

[11] B. Boehm, A Spiral model of software development and enhancement, IEEE Computer 21 (5) (1988 May) 61 – 72.

[12] B.W. Boehm, P.N. Papaccio, Understanding and controlling software costs, IEEE Transactions on Software Engineering 14 (10) (1988) 1462– 1477.

[13] T.J. Brennan, A Shock to the System: Restructuring America’s Electricity Industry, Resources for the Future, Washing ton, DC, 1996, p. 138.

[14] F.P. Brooks, Is there a design of design? in: K. Sullivan (Ed.), NSF Workshop on the Science of Design: Software and Software-Intensive Systems, NSF, Airlie Center, VA, 2003, p. 2.

[15] W.F. Buckley, Sociology and Modern Systems Theory, Pren tice-Hall, Englewood Cliffs, NJ, 1967, p. 227.

[16] W.F. Buckley, Society—A Complex Adaptive System: Essays in Social Theory, Gordon and Breach, Australia, 1998, p. 312.

[17] G. Burrell, G. Morgan, Sociological Paradigms and Organisational Analysis: Elements of the Sociology of Corporate Life, Heinemann, London, 1979, p. 432.

[18] J.B. Bushnell, S.S. Oren, Internal auctions for the efficient sourcing of intermediate products, Journal of Operations Management 12 (3,4) (1995) 311– 320.

[19] H. Chao, S. Peck, A market mechanism for electric power transmission, Journal of Regulatory Economics 10 (1996) 25–59.

[20] J.F. Courtney, Decision making and knowledge management in inquiring organizations: toward a new decision-making paradigm for DSS, Decision Support Systems 31 (1) (2001 May) 17– 38.

[21] B. Curtis, H. Krasner, N. Iscoe, A field study of the software design process for large systems, Communications of the ACM 31 (11) (1988 November) 1268– 1287.

[22] R. Cyert, J. March, A Behavioral Theory of the Firm, Prentice-Hall, Englewood Cliffs, NJ, 1963, p. 252.

[23] A. Dandekar, E. Perry, Barriers to effective process architecture—an experience report, Software Process Improvement and Practice 2 (1) (1996 March) 13 – 20.

[24] A. Dardenne, A. van Lamsweerde, S. Fickas, Goal-directed requirements acquisition, Science of Computer Programming 20 (1993) 3– 50.

[25] P.A. David, W.E. Steinmueller, Standards, trade and competition in the emerging global information infrastructure environment, Telecommunications Policy 20 (1996) 817.

[26] M.J. Denton, S.J. Rassenti, V.L. Smith, S.R. Backerman, Market power in a deregulated electrical industry, Decision Support Systems 30 (2001) 357– 381.

[27] S. Easterbrook, Model management and inconsistency in software design, in: K. Sullivan (Ed.), NSF Workshop on the Science of Design: Software and Software-Intensive Systems, NSF, Airlie Center, VA, 2003, p. 2.

[28] R.T. Fielding, R.N. Taylor, Principled design of the modern web architecture, Proceedings of the 22nd International Conference on Software Engineering, Limerick, Ireland, 2000.

[29] D. Friedman, J. Rust, The Double Auction Market: Institutions, Theories, and Evidence, Addison-Wesley Pub. Co, Reading, MA, 1993, p. 429.

[30] B.G. Glaser, A.L. Strauss, Discovery of Grounded Theory: Strategies for Qualitative Research, Aldine de Gruyter, 1967, p. 271.

[31] J.A. Goguen, Formality and informality in requirements engineering, Proceedings of the Fourth International Conference on Requirements Engineering, IEEE Computer Society, 1996, pp. 102–108.

[32] J. Goguen, An introduction to algebraic semiotics, with applications to user interface design, in: C.L. Nehaniv (Ed.), Computation for Metaphors, Analogy, and Agents, Springer, New York, NY, 1999, pp. 242– 291.

[33] S.J. Greenspan, J. Mylopoulos, A. Borgida, Capturing more world knowledge in the requirements specification, Proceedings of the Sixth International Conferences of Software Engineering, 1982, pp. 225–234.

[34] S.J. Greenspan, J. Mylopoulos, A. Borgida, On formal requirements modeling. Languages: RML Revisited, Proceedings of the International Conferences of Software Engineering, 1994, pp. 225–234.

[35] M. Haglind, L. Johansson, M. Rantzer, Experiences integrating requirements engineering and business analysis an empirical study of operations and management system procurement, International Conference on Requirements Engineering (ICRE ’98), IEEE, Colorado Springs, CO, 1998, p. 108.

[36] J.D. Herbsleb, A. Mockus, Formulation and preliminary test of an empirical theory of coordination in software engineering, Proceedings of the 9th European Software Engineering Conference and 10th ACM SIGSOFT Foundations of Software Engineering, Helsinki, Finland, 2003.

[37] A. Hevner, S. March, J. Park, S. Ram, Design science in information systems research, MIS Quarterly 28 (1) (2004 March) 75–105.

[38] S.R. Hiltz, M. Turoff, Structuring computer-mediated communication systems to avoid information overload, Communications of the ACM 28 (7) (1985 July) 680– 689.

[39] T.E. Hoff, H.J. Wenger, C. Herig, J. Robert, W. Shaw, Distributed generation and micro-grids, Proceedings of the 18th Annual North American Conference of the US Association for Energy Economics, San Francisco, CA, 1997.

[40] C.W. Holsapple, Knowledge management support of decision making, Decision Support Systems 31 (1) (2001 May) 1– 3.

[41] T.P. Hughes, Networks of Power: Electrification in Western society, 1880–1930, Johns Hopkins University Press, Baltimore, 1983, p. 474.

[42] T.P. Hughes, Edison and electric light, in: D. MacKenzie, J. Wajcman (Eds.), The Social Shaping of Technology, Open University Press, Bristol, PA, 1992, pp. 39 – 53.

[43] M. Jackson, System Development, Prentice-Hall, Englewood Cliffs, NJ, 1983, p. 418.

[44] M. Jackson, Software Requirements and Specifications: A Lexicon of Practice, Principles and Prejudices, ACM Press/ Addison-Wesley Publishing Co., New York, NY, 1995, p. 264.

[45] M. Jackson, A science of software design? in: K. Sullivan (Ed.), NSF Workshop on the Science of Design: Software and Software-Intensive Systems, NSF, Airlie Center, VA, 2003, p. 2.

[46] I. Jacobson, G. Booch, J. Rumbaugh, The Unified Software Development Process, Addison-Wesley, New York, NY, USA, 1999, p. 463.

[47] M. Jarke, J. Bubenko, C. Rolland, A. Sutcliffe, Y. Vassiliou, Theories underlying requirements engineering: an overview of NATURE at Genesis, Proceedings of the IEEE Symposium on Requirements Engineering, RE’93, San Diego, California, 1993.

[48] M. Jirotka, Tutorial on video supported ethnography for requirements analysis, International Conference on Requirements Engineering (ICRE), Colorado Springs, CO, 1998.

[49] M. Jirotka, J. Goguen, Requirements Engineering: Social and Technical Issues, Academic Press, London, 1994, p. 296.

[50] H. Kaindl, S. Brinkkemper, J.A.J. Bubenko, B. Farbey, S.J. Greenspan, C.L. Heitmeyer, J.C.S.d.P. Leite, N.R. Mead, J. Mylopoulos, J. Siddiqi, Requirements engineering and technology transfer: obstacles, incentives and improvement agenda, Requirements Engineering 7 (2002) 113– 123.

[51] A. Keyhani, A. Kian, J.C. Jr., M.A. Simaan, Market monitoring and control of ancillary services, Decision Support Systems 30 (2001) 255–267.

[52] R. Klashner, Using Architecture Style to Design and Evolve Complex Integrated Information Infrastructure, Information and Computer Science, University of California, Irvine, CA, 2002, p. 228.

[53] R. Klashner, ICT and the deregulation of the electric power industry: a story of an architect’s new tool, Journal of Digital Information (JoDI), To appear in a Special issue on Social Aspects of Digital Information in Perspective, 2004.

[54] P.R. Kleindorfer, H.G. Kunreuther, P.J.H. Schoemaker, Decision Sciences, Cambridge University Press, 1993, p. 484.

[55] P.B. Kruchten, The 4+1 view model of architecture, IEEE Software 12 (1995) 42.

[56] A.M. Law, W.D. Kelton, Simulation Modeling and Analysis, McGraw-Hill, Boston, 2000, p. 760.

[57] C.E. Lindblom, The science of muddling through, Public Administration Review 19 (1959) 79– 88.

[58] P. Mangiameli, D. West, R. Rampal, Model selection for medical diagnosis decision support systems, Decision Support Systems 36 (3) (2004 Jan) 247–259.

[59] M.L. Markus, A. Majchrzak, L. Gasser, A design theory for systems that support emergent knowledge processes, MIS Quarterly 26 (3) (2002 September) 179– 212.

[60] J.A. McDermid, Requirements analysis: orthodoxy, fundamentalism, and heresy, in: M. Jirotka, J. Goguen (Eds.),

Requirements Engineering: Social and Technical Issues, Academic Press, London, 1994, p. 296.

[61] J. McDermid, Science of software design: architectures for evolvable, dependable systems, in: K. Sullivan (Ed.), NSF Workshop on the Science of Design: Software and Software-Intensive Systems, NSF, Airlie Center, VA, 2003, p. 2.

[62] D.W. McDonald, Supporting nuance in groupware design, Moving from Naturalistic Expertise Location to Expertise Recommendation, Information and Computer Science, University of California, Irvine, CA, 2000.

[63] N. Medvidovic, R.N. Taylor, A classification and comparison framework for software architecture description languages, IEEE Transactions on Software Engineering 26 (1) (2000) 70–93.

[64] N. Medvidovic, D.S. Rosenblum, R.N. Taylor, A language and environment for architecture-based software development and evolution, Proceedings of the 21st International Conference on Software Engineering (ICSE’99), Los Angeles, CA, 1999, pp. 44–53.

[65] D.M. Meira, A Model for alarm correlation in telecommunications networks, Computer Science, Institute of Exact Sciences (ICEx) of the Federal University of Minas Gerais, Belo Horizonte, Brazil, 1997, p. 149.

[66] H.R. Nemati, D.M. Steiger, L.S. Iyer, R.T. Herschel, Knowledge warehouse: an architectural integration of knowledge management, decision support, artificial intelligence and data warehousing, Decision Support Systems 33 (2002) 143– 161.

[67] Open access same-time information system and standards of conduct, In Federal Energy Regulatory Commission OASIS NOPR 889, RM95-9-000, (1996) 145.

[68] P. Oreizy, M.M. Gorlick, R.N. Taylor, D. Heimbigner, G. Johnson, N. Medvidovic, A. Quilici, D.S. Rosenblum, A.L. Wolf, An architecture-based approach to self-adaptive software, IEEE Intelligent Systems 14 (1999) 54–62.

[69] S.S. Oren, Economic inefficiency of passive transmission rights in congested electricity systems with competitive generation, Energy Journal 18 (1) (1997) 63– 83.

[70] W.J. Orlikowski, CASE tools as organizational change: investigating incremental and radical changes in systems development, MIS Quarterly 17 (3) (1993) 309– 340.

[71] L.J. Osterweil, Software processes are software too, revisited: an invited talk on the most influential paper of ICSE 9, 19th International Conference on Software Engineering, ACM Press, Boston, MA, 1997, pp. 540– 548.

[72] T.J. Overbye, J.D. Weber, K.J. Patten, Analysis and visualization of market power in electric power systems, Decision Support Systems 30 (2001) 229– 241.

[73] C. Pahl, M. Casey, Ontology support for web service processes, Proceedings of the 9th European Software Engineering Conference and 10th ACM SIGSOFT Foundations of Software Engineering, Helsinki, Finland, 2003, pp. 208– 216.

[74] D.E. Perry, Software evolution and <sup>b</sup>light <sup>Q</sup> semantics, Proceedings of the 21st International Conference on Software Engineering, Los Angeles, CA, IEEE Computer Society Press, 1999, pp. 587– 590.

[75] D.E. Perry, A.L. Wolf, Foundations for the study of software architecture, ACM SIGSOFT Software Engineering Notes 17 (4) (1992 October).

[76] G.P. Picco, A.L. Murphy, G.-C. Roman, LIME: Linda meets mobility, Proceedings of the 21st International Conference on Software Engineering, Los Angeles, CA USA, 1999, pp. 368–377.

[77] D. Power, Building knowledge-driven DSS and mining data, Decision Support Systems, HyperBook, 2000.

[78] D.J., Power, A brief history of decision support systems, accessed in 02/18/04, 2004, DSSResources.COM, Electronic source: http://DSSResources.COM/history/dsshistory.html.

[79] H.W. Rittel, J., M.M. Webber, Dilemmas in a general theory of planning, Policy Sciences 4 (1973) 155 – 169.

[80] S.A. Sabet, R. Klashner, Helping network managers meet service demands using DSS, The Proceedings of the Special Interest Group on Decision Support, Knowledge and Data Management (SIGDSS) Workshop held in conjunction with the International Conference on Information Systems (ICIS’03), Seattle, WA, 2003.

[81] W. Scacchi, Process models in software engineering, in: J.J. Marciniak (Ed.), Encyclopedia of Software Engineering, John Wiley and Sons, New York, NY, 2001.

[82] R.E. Schuler, Analytic and experimentally derived estimates of market power in deregulated electricity systems: policy implications for the management and institutional evolution of the industry, Decision Support Systems 30 (2001) 341–355.

[83] M. Shaw, D. Garlan, Software Architecture: Perspectives on an Emerging Discipline, Prentice Hall, Upper Saddle River, NJ, 1996, p. 242.

[84] H.A. Simon, Models of Bounded Rationality, MIT Press, Cambridge, MA, 1982

[85] H.A. Simon, The Sciences of the Artificial, MIT Press, Cambridge, MA, 1994.

[86] I. Sommerville, Software Engineering, Addison-Wesley Pub. Co, 2000, p. 693.

[87] I. Sommerville, T. Rodden, P. Sawyer, R. Bentley, M. Twidale, Integrating ethnography into the requirements engineering process, RE’93, San Diego CA, 1994.

[88] R.H. Sprague, A framework for the development of decision support systems, MIS Quarterly 4 (4) (1980) 1 – 26.

[89] R.L. Sullivan, Power System Planning, McGraw-Hill, New York, NY, 1977, p. 324.

[90] A.G. Sutcliffe, N.A.M. Maiden, S. Minocha, D. Manuel, Supporting scenario-based requirements engineering, IEEE Transactions on Software Engineering 24 (12) (1998 Decem ber) 1072–1088.

[91] W.J. Tauzin, August 14th Transcript of Midwest ISO control center from 1:00 to 5:00 pm Eastern Time. H.C.o.E.a, Commerce House of Representatives, Washington, DC, 2003, p. 650.

[92] R.N. Taylor, W. Tracz, L. Coglianese, Software Development using Domain-Specific Software Architectures, A Curriculum Module in the SEI style, University of California, Irvine, 1994.

[93] R.N. Taylor, N. Medvidovic, K.M. Anderson, E.J. Whitehead Jr., J.E. Robbins, K.A. Nies, P. Oreizy, D.L. Dubrow, A component- and message-based architectural style for GUI software, IEEE Transactions on Software Engineering 22 (6) (1996 June) 390–406.

[94] R.J. Thomas, Restructuring the electric power business—a marriage of power engineering and market economics, Decision Support Systems 30 (3) (2001) 227 – 228.

[95] A. Tiwana, B. Ramesh, A design knowledge management system to support collaborative information product evolution, Decision Support Systems 31 (2) (2001 June) 241– 262.

[96] W. Tracz, Confessions of a Used Program Salesman: Institutionalizing Software Reuse, Addison-Wesley Pub. Co, Reading, MA, 1995, p. 233.

[97] W. Tracz, L. Coglianese, P. Young, A domain-specific software architecture engineering process outline, ACM Software Engineering Notes (1993 April) 40– 49.

[98] E. Turban, Decision Support Systems and Intelligent Systems, Prentice-Hall Inc., Upper Saddle River, NJ, 1998, p. 890.

[99] B.A. Turner, The use of Grounded theory for the qualitative analysis of organizational behaviour, Journal of Management Studies 20 (3) (1983) 333– 348.

[100] M. Turoff, M. Chumer, B.V.d. Walle, X. Yao, The design of a dynamic emergency response management information system (DERMIS), Journal of Information Technology Theory and Application To appear, 2004.

[101] V. Vaishnavi, W. Kuechler, Design research in information systems, accessed in January 20, 2004, Electronic source: http://www.isworld.org/Researchdesign/drisISworld. htm, 2004.

[102] Z.A. Vale, M.F. Fernandes, C. Rosado, A. Marques, et al., Better KBS for real-time applications in power system control centers: the experience of SPARSE project, Computers in Industry 37 (2) (1998) 97– 111.

[103] A. van Lamsweerde, Requirements engineering in the year 00: a research perspective, Proceedings of the 22nd International Conference on Software Engineering, Limerick, Ireland, 2000.

[104] M. Weber, Max Weber on Law in Economy and Society, translated by E. Shils and M. Rheinstein, Simon and Schuster, New York, NY, 1968.

[105] E.S.K. Yu, Towards modelling and reasoning support for early-phase requirements engineering, The Proceedings of 3rd IEEE International Symposium on Requirements Engineering, 1997, pp. 226–235.

[106] E.S.K. Yu, J. Mylopoulos, Towards modelling strategic actor relationships for information systems development—with examples from business process reengineering, Proceedings of the 4th Workshop on Information Technologies and Systems, WITS’94, Vancouver, BC, 1994.

[107] J.A. Zachman, A framework for information system architecture, IBM Systems Journal 26 (3) (1987) 454–470.

[108] B. Zeigler, T. Kim, H. Praehofer, Theory of Modeling and Simulation, Academic Press, 2000, p. 510.

[109] L. Zhou, K.M. Smedley, Unified constant–frequency integration control of active power filters, IEEE Applied Power Electronics Conference, 2000, pp. 406–412.

![](/api/attachments/THX5Z32S/fulltext/images/3839e8725c4a580d8b2a668bab506e981370cc1f36a10bb829ad63025da3a4dd.jpg)

Robb Klashner is an Assistant Professor in the Information Systems Department, College of Computing Sciences, at the New Jersey Institute of Technology. He has a PhD in Information and Computer Science from the University of California Irvine. His current research interests include decision support systems, design of emergency response systems, theoretically grounded analysis and design, mission critical infrastructure, integrated informa-

tion infrastructure, software architecture design tool environments, software engineering, and requirements acquisition using qualitative methods.

![](/api/attachments/THX5Z32S/fulltext/images/ada31e8df7868b26d9a5f4132d3c984efe172e6ebded9714b68ad65d4254ab0e.jpg)

Sameh Sabet is a Distinguished Member of Technical Staff at Tyco Telecommunications Laboratories. He is also an adjunct professor at NJIT where he teaches requirements engineering. He is a PhD candidate in Information Systems at NJIT. Previously, he was the Director of Network Systems Development for TyCom Labs. He has over 10 years of experience in IT as well as software design, development and real-time embedded systems design for

Network Management Systems in the telecommunications industry. His current research interests span augmenting alarm correlation with emerging decision support systems and knowledge management research.
