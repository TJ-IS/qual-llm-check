---
otero_id: 11706
otero_key: "YNYJ599K"
title: "Decision support for improvisation in response to extreme events: Learning from the response to the 2001 World Trade Center attack"
authors: "David Mendonça"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.05.025"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support for improvisation in response to extreme events: Learning from the response to the 2001 World Trade Center attack

David Mendonc¸a<sup>\*</sup>

Information Systems Department, New Jersey Institute of Technology, 323 Martin Luther King, Jr. Blvd, Newark, NJ 07102, United States

Available online 5 July 2005

## Abstract

Extreme events such as natural or technological disasters challenge society’s capabilities for planning and response. While advanced technologies and modeling techniques continue to expand how society can limit and manage extreme events, flexibility and an ability to improvise remain crucial in responding to them. By analyzing a case from the response to the 2001 World Trade Center attack, this paper develops a set of requirements for computer-based systems intended to support improvisation in response to extreme events. The particular goal of this analysis is to identify methods for providing cognitive-level support for organizations in determining when and how to improvise. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Extreme events; Improvisation; Emergency response

## 1. Introduction

Due to their size, complexity and rarity, extreme events such as natural or technological disasters challenge society’s capabilities both for planning and response. While information technologies and advanced modeling techniques continue to expand how society can limit and manage extreme events [69], flexibility remains crucial to organizational resilience when responding to them [50,78]. The response to the 2001 World Trade Center attack offers numerous examples of how flexibility may contribute to the resilience of critical infrastructure systems:

subway maintenance workers joined the response effort to remove obstacles and lift and move heavy debris and wreckage [31]; police responded without the use of cellular phones and pagers [68]; and electric utility crews improvised a solution to widespread power outages [3]. Yet infrastructure systems and the organizations that manage them are now recognized as components of highly-coupled systems that increasingly rely on one another in order to deliver key services [60,63,80]. When such systems have physical or logical connections with each other–and must therefore work in concert to provide key services–they are said to be interdependent [83]. The above examples of impacted interdependent critical infrastructures suggest that, in order to improve resiliency, emergency response organizations need to maintain flexibility in order to address contingencies that have not been planned-for.

The focus of the present work is on using field data associated with the response to the 2001 World Trade Center attack in order to accomplish two goals: first, to identify cognitive-level issues involved in responding to extreme events, particularly those that impact interdependent critical infrastructures; second, to develop a set of requirements and challenges for computer-based systems intended to support cognition in extreme event decision making.

The need for real-time development and deployment of new procedures to address unplanned-for contingencies during the response to extreme events is first discussed, and improvisation is considered as one approach to addressing this need (Section 2). A case study from the response to the 2001 World Trade Center attack (Section 3) illustrates an observation made by Kreps [37] and reiterated by others [34,79]: that emergencies routinely create non-routine situations, and that responding organizations must plan for improvisation. A set of requirements is then presented for systems intended to provide cognitive-level support for extreme event decision making (Section 4). The paper concludes with a discussion of challenges to meeting these requirements along with a discussion of prospects for future work (Section 5).

## 2. Background

This section develops a scope of inquiry that will be used in analyzing the recovery of one interdependent infrastructure system following the 2001 World Trade Center attack.

## 2.1. Extreme event decision making

Extreme events may be regarded as events which are rare, uncertainty and potentially high and broad consequences [78]. Their rarity limits opportunities for learning about them and the circumstances that gave rise to them. Risk is present as possible largescale threats to life, property or the environment. Responding to an extreme event is likely to require multiple decision makers reasoning and making decisions about complex systems such as physical infrastructures [78]. Time pressure arises from factors such as a threat of building collapse or policy constraints on minimum response time.

As shown in Fig. 1, when decision makers at some time t are faced with a future deadline at T, every minute spent on planning is one less minute available for plan implementation. Simultaneously, the materiel and personnel resources available for responding to the event decrease, since they will typically have to be dispatched from one location to another, the result being that the number of possible plans involving these resources (i.e., the size of the search space) decreases. Over time, then, a greater extent of this space can be searched per unit of time. However, as a result of decreasing available resources and increasing complexity and risk, the problem of how to respond becomes more difficult. Indeed, both risk and time constraint contribute to the need for response personnel to <sup>b</sup>make do<sup>Q</sup> with resources that are or can be made available in time. As Fig. 1 suggests, then, <sup>b</sup>the chal lenges and consequences of extreme events are the joint product of an event, the community that is affected by the event, and the organizations involved in preparation and response<sup>Q</sup> [78]. Other studies [53] describe the social, organizational and community impacts of extreme events. The present work describes extreme event decision making in order to identify opportunities for supporting it with computer-based tools.

## 2.2. Organizational response to extreme events

The onset of an extreme event may result in the mobilization of an emergency response organization (ERO), defined as an assembly of individuals who work together to manage the response to an emergency [4]. An ERO may be comprised of individuals from within a single organization or of representatives from a number of organizations [61]. The Incident Command System (ICS) [9] is a decision making protocol for EROs that places a coordinator in the central role of facilitating team decision making. Systems such as ICS may be particularly appropriate in managing the response to impacts on interdependent infrastructures, since at least two organizations must coordinate in order to restore a service whose provision is dependent upon the infrastructures working in concert.

![](/api/attachments/YNYJ599K/fulltext/images/524e3f038ca87d08bf9807683a751b68b68e8276024a465c14be103042f1132e.jpg)  
Fig. 1. Decision situation for extreme events.

Managing an emergency usually includes monitoring operations during normal conditions, selecting an appropriate procedure when planned-for contingencies arise, and revisiting the appropriateness of these procedures as other potentially disruptive events occur [6,8]. Unplanned-for contingencies–events for which no planned-for procedure exists–create the need for the responding organization to develop and deploy new procedures in real-time. An unplanned-for contingency may have its genesis in numerous circumstances: an emergency situation may evolve so that implemented plans are no longer applicable [79]; it may be multi-faceted, requiring responding organizations to combine many plans in unexpected ways; it may occur concurrently with other situations, thus creating resource shortages or outages [79]; and, finally, it may require activities that are not immediately assignable to a particular organization [73].

## 2.3. The role of improvisation

One approach to addressing unplanned-for contingencies is improvisation. The need for skill in improvisation was emphasized for emergency management practitioners by Kreps [37]:

Without improvisation, emergency management loses flexibility in the face of changing conditions. Without preparedness, emergency management loses clarity and efficiency in meeting essential disaster-related demands. Equally importantly, improvisation and preparedness go hand in hand. One need not worry that preparedness will decrease the ability to improvise. On the contrary, even a modest effort to prepare enhances the ability to improvise.

To borrow a comparison from music–where improvisation is routinely <sup>b</sup>planned-for<sup>Q</sup>–improvisation in jazz is said to involve <sup>b</sup>reworking precomposed material and design in relation to unanticipated ideas conceived, shaped, and transformed under the specia conditions of performance, thereby adding unique features to every creation<sup>Q</sup> [5]. Improvisation is therefore in part a cognitive activity that requires creativity under time constraint in order to meet performance objectives. While improvising has been compared to <sup>b</sup>real-time composing<sup>Q</sup> [32], improvisation and composition differ in salient ways [56]. Composition refers to <sup>b</sup>the discontinuous process of creation and iteration (usually through notation) of musical ideas<sup>Q</sup> [72], and has its analog as planning in emergency response. Improvisation, by contrast, is a continuous and serial process [44]. Composing involves distributing musical elements (such as notes) over a score that is to be played serially: the composer may add to, delete or edit any part of the composition at any time before its performance. Performance of a composition involves interpreting and articulating a written or memorized score. Performance of an improvisation involves conceiving, articulating and remembering an unwritten, evolving score [5]. While a misplaced note in a composition can be erased and rewritten; a misplayed note in improvisation cannot. Errors in improvisation therefore <sup>b</sup>must be accepted as part of the irrevocable chain of acoustical events, and contextually justified after the fact by reinforcement or development<sup>Q</sup> [64]. The musician Steve Lacy was given 15 s to characterize the difference between composition and improvisation, and he replied <sup>b</sup>In fifteen seconds the difference between composition and improvisation is that in composition you have all the time you want to decide what to say in fifteen seconds, while in improvisation you have exactly fifteen seconds<sup>Q</sup> [1].

Implicit in this and other descriptions of improvisation [64–66,72,75] is the notion that a rough guide or framework is used to guide cognition in performance. In music, examples of such rough guides include an existing theme (such as a melody), a body of fragments (such as a few notes) or a newlyinvented theme. Sarath [72] and Pressing [65,66] refer to this guide as a referent, defined as an underlying format, such as <sup>b</sup>the harmonic-rhythmic framework of the composition<sup>Q</sup> played by the improviser [65]. Sloboda [75] speculates that the referent is a set of constraints that provide a <sup>b</sup>blueprint<sup>Q</sup> or <sup>b</sup>skeleton<sup>Q</sup> for the improvisation. In emergency response, the referent may be a standard operating procedure or a routine learned from experience which, given the occurrence of an unplanned-for contingency, forms the basis for a new course of action.

Researchers have suggested that different realizations may arise from the same referent. In jazz, a realization of a referent is that which is played based on the referent: in other words, the music itself. Berliner [5] has analyzed and found consistencies among different realizations of one referent (i.e., a well-known solo) over 46 years (pp. 576 ff.). In emergency response, a realization may be a set of actions that follow a modified standard operating procedure, as when police officers used alternative methods of communication during the response to the 2001 World Trade Center attack [68].

In emergency response, improvisation can be regarded as a two-stage process [46]. In the first stage, the responding organization recognizes either that no planned-for procedure applies to the current situation or that an appropriate planned-for procedure cannot be executed. In the process, <sup>b</sup>there can be errors of rigidly adhering to someone else’s plan as well as inappropriately departing from the plan<sup>Q</sup> [33]. An incorrect choice may therefore be defined as either (i) improvising when a planned-for procedure applies and is executable or (ii) failing to improvise when an appropriate planned-for procedure either cannot be found or cannot be executed. The other two possible choices (improvising when no planned-for procedure applies or can be executed; not improvising when a planned-for procedure does apply and can be executed) are correct choices, though of course no improvisation or planned-for procedure is guaranteed to have a desirable outcome.

At a cognitive level, the question of when to improvise during an extreme event may therefore be conceptualized as a problem in which the ability or likelihood of a decision maker to categorize the current situation correctly is influenced by a number of factors, such as penalties associated with making an incorrect choice and the likelihood that the response will succeed. Time pressure [42] and risk may also influence how the choice is made [76], in part by reducing the inclination to improvise given that the need exists to do so [86]. There is considerable evidence to suggest that decision makers enact strategies based on recognizing characteristics of past problems in the current one [33]. Indeed, a sobering conclusion of Weick’s [86] study of the response to the Mann Gulch forest fire is that groups under such conditions may force their conception of the emergency to fit one they know how to address—rather than to the one they need to address.

Once the need to improvise has been recognized, the second stage is the real-time development and deployment of new procedures. The referent may be a standard operating procedure or a routine learned from experience which, given the occurrence of an unplanned-for contingency, forms the basis for a new course of action. The improvisation may range from substitution to the construction of new procedures. In the case of substitution, the responding organization <sup>b</sup>mixes and matches<sup>Q</sup> existing procedures and/or the materiel used in them. At the other end of the spectrum, the organization must develop new procedures and possibly find new materiel for use in those procedures. An example of the former case (used by Emergency Services at the Port of Rotterdam, The Netherlands) is the use of a school bus instead of an ambulance corps for mass evacuation. An example of the latter case (used by the New South Wales, Australia, Fire Brigade) is the use of fire trucks to provide mobile showers following a chemical exposure.

Cognitively, then, the question of how to improvise may therefore be conceptualized as a search and assembly problem [57], which may be influenced by factors such as time available for planning, risk in the environment and the results of prior decisions.

## 2.4. Cognitive support for extreme event decision making

Research on how to provide cognitive-level support for decision making is needed [89], but rare [14]. One approach, taken elsewhere [38,39,43], is the integration of computational models of cognition into a decision support system. A computational model may be defined as <sup>b</sup>a model that describes a class of systems in terms of a set of operations on entities, where the operations can be described in computational terms<sup>Q</sup> [30,88]. A computational model of cognition (often called simply a cognitive model) may be described as a theory of human cognition that is executable on a computer [16,62]. Computational models of cognition have the potential to provide powerful means of supporting human cognitive processes [22,28,29,39], particularly when the task is characterized by uncertainty [54]. Yet for decision aids that employ these models to be effective, the design process will require the development of a detailed understanding of the appropriate cognitive processes [39]. Existing techniques for knowledge elicitation [19,20,35,81], coupled with data from field- [83] and laboratory-based [47] studies, may be useful in the development of such systems. The validity of laboratory- or simulation-based studies may be further improved with the use of materials such as the Federal Emergency Management Agency’s HAZUS database [77], the United States Fire Administration Technical Report Series (e.g., [71]) and case studies conducted by the Disaster Research Center [67]. Once such a model has been expressed in computer-executable code, it may be validated by (i) comparing the reasoning processes of the model to those of human subjects [57] or, in a setting where human and computer cooperate, (ii) evaluating whether the reasoning processes of the model and the decision makers are mutually and correctly understood [29].

One computational approach to improvisation is Hodges’ [25] Functional Ontology for Naive Mechanics (FONM), which extends research by Schank and Abelson [74] on how abstract or primitive actions can be combined into sequences called scripts. FONM is a hierarchical representation of mechanical devices (e.g., tools) and their functions that enables alternative devices to be specified when the device normally used for a task is unavailable.

A second approach follows from the theory of opportunistic planning [23,58], which states that human problem solving is incremental, in that it proceeds in stages, and opportunistic, in that problem solvers will suspend pursuit of some goals when more pressing needs (or promising opportunities) arise [12]. The model works by assembling a problem solution from the library of cognitive and behavioral processes contained within the system [24].

A third approach, based on research in improvisation outside the emergency response domain, provides a recommended decision to a group of human decision makers that is consistent with the group’s inferred referent [43,47]. A decision logic and domain ontology are used to infer the referent of a group of emergency response personnel and to support the generation of a realization of this referent. Given the occurrence of an unplanned-for contingency which blocks the use of some resources in the courses of action, the system provides recommendations concerning resources which might substitute for the unavailable resources.

Support for improvisation may be in the form of training before the event’s occurrence or provision of decision tools during response. Providing support before the event occurs is akin to planning for improvisation, an approach that has been advocated by a number of researchers [37,52,86,87]. Providing support for improvisation during extreme event response entails supporting tasks of recognizing and responding to unplanned-for contingencies. Since decision makers must realize that the current situation differs from the one that was planned-for, recognizing when to improvise requires problem finding [21]. Given the importance of time in making choices about whether or not to improvise, the decision aid should also support emergency managers in recognizing more quickly when it is necessary to improvise. Once the need to improvise is recognized, the system should support responding organizations in developing and deploying new courses of action.

A decision support system for improvisation may also take advantage of the likely structure of the responding organization. Under the Incident Command System protocol, for example, the system may interact with the coordinator, process event data and monitor planning and decision making processes. As a participant in improvisation, the system should provide guidance that is informed both by knowledge of the event and of the organization’s goals and preferences. Finally, given the complexity and difficulty of extreme event decision making, it may be advisable to include graphical tools for structuring how problems are defined [15,45] or how information about the emergency is presented [49].

## 2.5. Discussion

Prior research has proposed six properties of extreme events that are particularly important for decision making [78] and hence for decision support: rarity; uncertainty; high and broad consequences; complexity; time pressure; and multiple decision makers. These are now considered in the context of the preceding discussion in order to identify a preliminary set of opportunities for designers of decision support systems.

Rarity in event incidence limits opportunities for training for and learning from extreme events. Indeed, one observation from the preceding discussion is that it may be appropriate to provide training and tools for recognizing when and how to depart from planned-for procedures. Rarity also creates the need for divergent thinking, since the solution will likely need to be assembled from various sources. Time pressure forces a convergence of planning and execution [55], so that opportunities for analysis are limited [78]. It therefore creates a need for convergent thinking, so that a solution can be generated in a timely fashion. Tools for supporting both divergent and convergent thinking therefore need to be integrated so that decision makers can know when and how to alternate between the two types of thinking.

Uncertainty is present since both the incidence and evolution of an extreme event are difficult to predict. It is therefore vital that accurate and timely information be gathered about the event, and that opportunities be identified for supporting predictions about event impact and propagation. Extreme events have high and broad consequences, leading to the need to manage interdependencies among a wide range of physical and social systems. This may entail the use of tools to support interaction among (i) responding and affected organizations and individuals, (ii) physical infrastructures and (iii) the event itself. Event complexity arises in part due to the high and broad consequences of extreme events. It may also arise as a consequence of interdependencies among infrastructure systems [69]. Advanced models may be used to represent these systems, creating the possibility of using these models to manage complexity [69,83]. However, as discussed below, it must be recognized that complexity can create competing demands among multiple stakeholders for scarce resource.

Finally, multiple decision makers (e.g., representatives of impacted or responding organizations) may compete or negotiate while responding to the event. It may therefore be advisable to consider how decision support systems can support the management of proprietary information and shared resources. As a participant in improvisation, then, the model should provide guidance that is informed both by knowledge of the event and of the intentions of the organization. Table 1 summarizes this discussion.

The remainder of this paper is concerned with developing requirements for decision support systems in these areas of opportunity. Of particular focus is the question of what types of cognitivelevel support to provide for the tasks of determining when and how to improvise in response to an unplanned-for contingency. Studies based on field data offer opportunities for examining extreme event decision making in an environment characterized by complexity, uncertainty, risk and urgency [82], and therefore may be useful in developing and evaluating decision support for response activities. To this end, the following section reviews how one organization responded to an extreme event–the 2001 World Trade Center attack–in order to restore critical services following the occurrence of numerous unplanned-for contingencies. Decision making in the case is then analyzed in order to inform recommendations for the design of cognitively-grounded, computer-based systems to support decision making about when and how to improvise during the response to extreme events.

Opportunities for extreme event decision support systems

<table><tr><td>Extreme event property</td><td>DSS opportunity</td></tr><tr><td>Rarity</td><td>Support recognition of when and how to depart from planned-for procedures</td></tr><tr><td>Uncertainty</td><td>Support information seeking; support prediction about event propagation</td></tr><tr><td>High and broad consequences</td><td>Support interaction among society, physical infrastructures and response personnel</td></tr><tr><td>Complexity</td><td>Support interaction with models of complex systems</td></tr><tr><td>Time pressure</td><td>Reduce search time by supporting divergent and convergent thinking</td></tr><tr><td>Multiple decision makers</td><td>Support collaboration, negotiation and data sharing</td></tr></table>

## 3. Telecommunications restoration following the 2001 World Trade Center attack

## 3.1. Method

This research began with the identification of a preliminary set of incidents that resulted from the 2001 World Trade Center (WTC) attack that involved infrastructures regarded as critical by the U.S. government [63]. Incidents were identified by examining articles published in the popular press (e.g., New York Times and Wall Street Journal) in the 100-day period following the attack. Individuals within various responding organizations were then contacted and asked which of these or other incidents they would like to discuss. Personnel involved with the response then described their decision making using the method described below. In some cases, the interview data were supplemented with internal documents (such as after-action reports) and external documents (such as reports in the press and in academic journals). Approximately 30 personnel from both public and private organizations were interviewed.

A cognitive task analysis [18] method called the critical decision method [26,35] was used to elicit knowledge from study participants. The critical decision method (CDM) is a modified version of the critical incident technique [20] and, like other cognitive task analysis methods, is intended to reveal information about human knowledge and thinking processes during decision making, particularly during non-routine decision making [35]. It has been used in a wide variety of studies (see [26] for a review), including those intended to produce decision aids (see [90] for various examples). The method begins with the participant briefly recalling the incident, which is then recounted by the interviewer in order to ensure that it has been correctly understood. Decision points and a timeline of events are then discovered via direct questioning. An important product of this stage is the identification of points where (i) data were received or sensed, (ii) decisions were made or (iii) actions were taken. The interviewer then uses probe questions to investigate the <sup>b</sup>story behind the story<sup>Q</sup> [35], (i.e., the details about knowledge and thinking processes during the decision). Table 2 shows sample probe questions (from [26]).

<sup>b</sup>What if<sup>Q</sup> queries are next used to explore questions about how experts and novices might differ in approaching the decision, what were possible sources of error, and the like. The incident is then reviewed a fourth time, with the perspective shifting from actual experience to analysis. The interviewer poses hypothetical changes to incident and asks what might have happened under these hypothetical conditions.

One interviewer was responsible for conducting the interview. When possible (as in the case described below), interviews were audio- and videotaped. Otherwise, the other interviewer documented the interview subject’s responses. To complete the data collection, each participant was given a structured questionnaire concerning his/her professional training and background. A second questionnaire, adapted from work by Moorman et al. [51,55] on improvisation by organizations, was used to measure organizational improvisation, organizational memory and the evaluation of the response. At the conclusion of the interview, participants were free to ask the interviewers for more detail about the study and its objectives. An application of this method is now presented.

Table 2  
Sample CDM probe questions

<table><tr><td>Probe type</td><td>Probe content</td></tr><tr><td>Cues</td><td>What were you seeing, hearing, smelling?</td></tr><tr><td>Knowledge</td><td>What information did you use in making this decision and how was it obtained?</td></tr><tr><td>Analogues</td><td>Were you reminded of any previous experience?</td></tr><tr><td>Standard</td><td>Does this case fit a standard or typical scenario? Does it fit a scenario you were trained to deal with?</td></tr><tr><td>Goals</td><td>What were your specific goals and objectives at the time?</td></tr><tr><td>Options</td><td>What other courses of action were considered or were available?</td></tr><tr><td>Basis of choice</td><td>How was this option selected/other options rejected? What rule was being followed?</td></tr><tr><td>Experience</td><td>What specific training or experience was necessary or helpful in making this decision? What training, knowledge, or information might have helped?</td></tr><tr><td>Decision making</td><td>How much time pressure was involved in making this decision? How long did it take to actually make this decision?</td></tr></table>

## 3.2. Background

The WTC attack led to widespread utility outages in the lower Manhattan area. Further examination of the written and photographic record of the WTC attack suggests that infrastructure interdependencies impacted the flow of key or critical services in various ways [59]. The following case concerns the restoration of power at a key telecommunications center that was significantly impacted by the attack. The company that ran the center provided a variety of telecommunications services to lower Manhattan, some of which were provided by infrastructure at the center.

The case is based primarily on data from an audioand videotaped interview with a senior network operations manager from the company that ran the center. Supplementary materials such as after-action reports were provided by the company. The interview subject (<sup>b</sup>the manager<sup>Q</sup>) was well-experienced both in his field and in the company, having spent 30 years in the organization, six in his present position.

The loss of power impacted a major switching station, backup emergency 911 call routing and consumer telephone service, all located within the build ing housing the center. The task of the company was to restore power to the building and recommence telecommunications services as quickly as possible. Before recounting how this was done, the manager provided background on how power is normally obtained and managed at the building:<sup>1</sup>

<sup>b</sup>The equipment that provides telephone services runs on DC [direct current], so we provide 48 volt DC to all of the equipment that produces the revenue for the business.. . . We get 48 volt DC through two methods: we get commercial AC [alternating current] generated by the power company, . . . which works its way into the building series of transformers. We rectify that AC and produce DC. The DC then goes two ways: some of it trickle charges batteries that are always online, the remainder of it goes to power the equipment. The implication there is, if you fail to provide AC for a period of time, the charged batteries will operate the equipment for a period of time that we specify.<sup>Q</sup>

<sup>b</sup>The other way in which we provide AC, is if any commercial provider fails we have autostart generators that come online and provide the AC, which we then rectify to continue to charge batteries and run the equipment. So the implication in a commercial failure [is that] theoretically as long as you can run your generators–meaning get enough fuel–you can run for an extended period of time.<sup>Q</sup>

In the event of a commercial power failure, then, the standard operating procedure is to use the company’s own diesel fuel-powered generators in order to charge batteries and run equipment.

## 3.3. Event impact

One of the impacts associated with the collapse of the Twin Towers on 11 September was a fire at World Trade Center 7 (WTC7), which for reasons unrelated to this case was allowed to burn. Approximately 1 h before the collapse of WTC7, the two electric substations in the building were de-energized per request of the New York City Fire Department [59]. The collapse of WTC7 at 17:20 destroyed the substations, <sup>b</sup>and the cables coming into our building were likely crushed, severed, or otherwise damaged<sup>Q</sup>.

The standard operating procedure for restoring power could not be executed for a number of reasons, some involving emergent interdependencies with other critical infrastructure systems: <sup>b</sup>The reason [the standard operating procedure] didn’t work here was that there were water main breaks at the same time. So, [because] the generators are in the basement of our building they got flooded<sup>Q</sup>. Water also had entered the basement as a result of firefighting activities. A second contingency had arisen when debris from the collapse of WTC7 clogged the air intakes of one of the generators in the building. As a result, by about 17:30 there was <sup>b</sup>no commercial power, no generators operating, but equipment still operating normally on batteries<sup>Q</sup>.

The last call billed out of the building was at 22:21. The building was <sup>b</sup>totally dark at that point: batteries had been depleted, generators had failed, commercial power had failed, switching and transmission systems failed and we were down<sup>Q</sup>. Further complicating matters, the collapse of WTC7 had ripped open the side of the company’s building and poured dirt into it, <sup>b</sup>and that was with asbestos, and sheet rock, and who knows what else<sup>Q</sup>. The building’s air handling system had, however, been shut down earlier in the day, thus somewhat mitigating the effect of the debris.

In summary, the company concluded that no standard operating procedure for restoring power could be executed. By 17:30 on 11 September, no commercial power was available, no generators were operating, but equipment was still operating normally on batteries. By 22:21, following the collapse of WTC7, the batteries were depleted and none of the building’s telecommunications systems were operating.

## 3.4. Event response

The company’s priorities were to restore telecommunications services to Emergency Services and to the New York Stock Exchange. Establishment of this latter priority followed President Bush’s declaration that the New York Stock Exchange should reopen within 1 week of the attack. The level of time pressure arose not only from the need to restore services to the stock exchange and other critical infrastructures, but also from the company culture. When asked whether the level of time pressure changed over the first few days of the response, the manager stated that <sup>b</sup>it instantly went to intense and stayed that way. Remember you’re dealing with people who are genetically trained to never have a failure. So we measured and get paid on failures that run, minutes, seconds and sometimes hours at most. To be out of service for days is incomprehensible<sup>Q</sup>. When asked to contrast this degree of time pressure with that in prior events, he responded <sup>b</sup>there’s nothing in second place<sup>Q</sup>.

The need for power was immediately obvious and of primary importance: <sup>b</sup>this was a situation where until you could restore power you couldn’t go anywhere. I mean this, there’s no other branches on the tree, if there’s no power<sup>Q</sup>. The problem was <sup>b</sup>how to provide megawatts of generating capacity to one, charge batteries, and then two, once your batteries are starting to come online, then slowly start to place equipment online consistent with the power budget and determine the status of the equipment<sup>Q</sup>. Abiding by the power budget (in this case, about 4

MW) meant not trying to use more power than can be generated. <sup>b</sup>So, to the extent you had this much power you wanted to turn up this much electronics. They had more electronics that they wanted to turn up as we generated more power, which they’d go ahead and do. So it’s kind of staying in step with things. I mean, generating more power doesn’t serve any value<sup>Q</sup>. Smaller demands for power, as for pumps and spot lighting, were met with small portable generators. A decision was made to connect diesel fuel-powered portable generators to the building’s electrical system (see Fig. 2 for an example of a portable generator in use at another building). Other options were not considered. In fact, the decision to use diesel generators was made in a <sup>b</sup>split-second<sup>Q</sup>. Concurrent goals were to clean the environment and equipment: <sup>b</sup>the two activities that would be critical–and one ties to the other–[were that] we had to be able to clean the environment and the equipment, and then we’d be able to power it to assess its condition. The cleaning had to come a little ahead of the powering, because we couldn’t power the equipment in the dirty state because that would cause additional failures. And we’re not talking just dust here, we’re talking equipment that is now caked with stuff, so the danger you’d have is you could get a conductive path, and now you’re damaging equipment<sup>Q</sup>.

The standard procedure for connecting a generator to the building would likely have been to connect via the basement hookups and thus power the building. The hookups and switches located in the basement were clearly labeled with the names of the floors to which they pertained. However, the water and debris in the basement made this procedure unexecutable. A decision was then made to connect cable from the diesel generators directly to the floors which they were to power, but <sup>b</sup>there’s no good way of doing that, because it’s all hard wired in an elaborate system of switches<sup>Q</sup>. This decision was <sup>b</sup>one of those decisions that truly took milliseconds. I said, OK we have to get the building risers–meaning the hard-wired cables–cut them and splice cables from the street into the riser<sup>Q</sup>. The risers are cables within the building that are normally used to transmit power throughout the building. This solution required cutting those cables and attaching them to portable generators with between 1 and 2.5 MW capacity. The requirement was to <sup>b</sup>solve the problem as if there was no basement in the building, where all the equipment was located<sup>Q</sup>.

![](/api/attachments/YNYJ599K/fulltext/images/53f6065cae629aa1b66a9546449f97d9ae5101ec19e438bd0530f4bc825f3e6f.jpg)  
Fig. 2. Portable diesel-powered generator (photo courtesy of Jersey City, NJ Fire Department).

The task of connecting the cables required considerable care in order to ensure that cables were properly matched. <sup>b</sup>So you had cables coming down and you now had to cut them, not knowing for sure which was which. Then you took the cables from the street, bring them together, and you gotta make sure you get to the right one, and then you work that problem<sup>Q</sup>. This solution was accomplished incrementally: <sup>b</sup>what we were able to do is okay, get the third floor plant going, and get it running, get the sixth floor, you get the ninth floor. Or you get a piece of [floors] 3, 6 and 9, then you come back and beef it up<sup>Q</sup>. Generators were running by Friday, 14 September: <sup>b</sup>what we were then doing was turning up our equipment, and turning it on, and then once the power company was up and running, then we started to slowly do a transition to give more of the load to their side, and eventually take all of our generators offline and hold them in reserve for a failure of their system<sup>Q</sup>. With the transition to commercial power, the incident was essentially resolved, though the generators remained on stand-by and were periodically tested.

After recounting the company’s response, the manager re-emphasized the limited usefulness of plans during the response. He stated <sup>b</sup>if I’d had to go to anything other than my head or someone else’s it wouldn’t have worked. You don’t pull a binder off the shelf on this one. You certainly wouldn’t grab a laptop and go into something<sup>Q</sup>. Indeed, <sup>b</sup>no one to my knowledge went into a system quote unquote that gave them an answer in terms of what to do<sup>Q</sup>. The comments underscore the idea that plan-following and improvisation differ in fundamental ways. They also suggest that systems which can retrieve standard operating procedures from a database are not likely to be perceived as useful unless they can support decision makers in modifying these procedures to make them feasible and relevant to the goals of the response.

After the interview (about 1.5 h), the manager responded to questions (taken from [51]) on the degree of improvisation (questions 1 through 3) and the relevance of organizational memory (questions 4 through 7) in the case. As in [51], multiple questions were used for each construct in order to increase internal validity. A seven-point semantic scale was used for all questions. The questions and the responses are shown in Figs. 3 and 4. The responses to questions 1 through 3 suggest that the response was highly improvised. The responses to questions 4 through 7 suggest that standard approaches and procedures were not available but that prior knowledge and skills were highly relevant to the response. It may be concluded that, in the manager’s opinion, memory

## Rate the Action:

![](/api/attachments/YNYJ599K/fulltext/images/88ac57be57203e9c6adba2fa8f5905b47649cfccd20e350b4effdb47ca0df491.jpg)  
Fig. 3. Organizational improvisation.

![](/api/attachments/YNYJ599K/fulltext/images/fbebfdf8f8f85f8c712f76c4afa8139b5c7ce609302c99aa71d959046b6ab8ff.jpg)  
Fig. 4. Organizational memory.

based on procedures and standard approaches was not relevant, but that skills and some other forms of knowledge were very relevant. A key question, then, is how to identify relevant knowledge and convert it into procedures that can be executed using existing skills.

## 4. Discussion

Decision making in the case is now examined in order to identify requirements for systems to support improvised decision making.

## 4.1. Extreme event decision making

The properties of extreme events shown in Table 1 are all present in the case, as summarized in Table

3 (below). The rarity of the event is obvious but is emphasized by the responses to the questions on organizational improvisation and memory. Rarity was the product of a wide range of events, including debris intrusion, flooding and loss of power to the center. Site conditions made it difficult to access the site and therefore retrieve reliable information about the status of the building, situations that contributed to event uncertainty. The responses to questions 1–3 in Fig. 3 further enforce this view.

The consequences and complexity of the event were intertwined: many infrastructure systems were impacted, and there were numerous interdependencies among these systems (some of which emerged only during the event itself). An interdependency had been designed in which the telecommunications company depended on the power company for electric power. The New York Stock Exchange and various emergency services depended upon the company for telecommunications. In contrast to these designed interdependencies, two others emerged as a result of the attack. First, the proximity of the water supply to the building contributed to flooding in the basement when the water mains were shattered. Second, water from fire crews’ hoses also entered the basement.

Time pressure arose due to policy considerations (e.g., the need to restore power to critical services), but also from the organization’s culture, which was highly intolerant of service outages. Finally, multiple decision makers were involved since, over time, telecommunications and electric power personnel had to coordinate activities (e.g., when the power company restored services and generators were taken off-line).

Table 3  
Extreme event properties evident in case

<table><tr><td>Extreme event property</td><td>Examples from case</td></tr><tr><td>Rarity</td><td>Numerous unplanned-for contingencies blocked execution of standard operating procedure</td></tr><tr><td>Uncertainty</td><td>Coordination by feedback was necessary in restoring power</td></tr><tr><td>High and broad consequences</td><td>Critical services provided by Electric Power, Financial, Emergency Service and Telecommunications infrastructures were impacted</td></tr><tr><td>Complexity</td><td>Interdependencies were present among Electric Power, Financial, Emergency Service and Telecommunications infrastructures</td></tr><tr><td>Time pressure</td><td>Financial and Emergency Services, along with commercial and residential customers, were in immediate need of telecommunications service; organizational culture imposed additional time pressure</td></tr><tr><td>Multiple decision makers</td><td>Coordination was required among Telecommunications and Electric Power infrastructures, and with private contractors</td></tr></table>

Additionally, the company contracted work to various outside organizations (e.g., for cleanup of the building environment).

The remainder of this analysis focuses on developing requirements for systems to support response activities associated with event rarity, uncertainty, time pressure and the presence of multiple decision makers. Prospects for supporting activities associated with event complexity and consequences are being investigated by other researchers [69,83]. Possible approaches to evaluating the system are then proposed.

## 4.2. Implications for cognitively-grounded decision support

The framework of referent-based improvisation may be used to describe cognition as reflected in the interview, and hence to suggest design specifications for a model of that cognition. A triggering event (the power outage) resulted in an attempt to execute a particular procedure (in this case, to use the company’s generators and built-in wiring). The decision about when to improvise was informed by a number of factors (e.g., flooded auto-start generators, clogged air intakes, a collapsed WTC7). Some of these factors were identified <sup>b</sup>remotely<sup>Q</sup> (i.e., by watching television coverage of the impacted area); others were witnessed. Rapid assessment of the extent of the severity of these conditions was necessary. Indeed, the manager noted that a less-experienced person might have called for studies and investigations— but would soon have been replaced by a more-experienced person.

Decision support for recognizing when to depart from planned-for procedures must therefore support– and perhaps even encourage–the comparison of the current decision situation with past ones. Recent research on cognitive processes of categorization [13], as well as computational approaches to categorizing [48], may be used here. Case-based reasoning systems [84] and other systems which catalogue the set of planned-for situations or decision alternatives may also be used for this purpose [7]. A key issue, discussed previously, is that risk and time constraints may discourage decision makers from considering that the situation might not have been planned-for. Decision support should therefore be capable of providing alternative views of event-related data. The proliferation of sensor technologies is producing more and more detailed descriptions of extreme event-related phenomena and hence a larger pool of data from which to draw inferences. For example, remote sensing technologies were used extensively in response and recovery operations at Ground Zero following the World Trade Center attack.

Once the severity of these contingencies was assessed, the decision was made not to attempt to execute the procedure. An alternative procedure was then developed, in which portable generators and a different wiring configuration were used to provide power. The new procedure may be represented as a realization of this referent, since it entailed the modification of an existing procedure and the use of unplanned-for materiel. Recall that the standard operating procedure would have called for (1) the company’s own auto-start generators to be connected directly to (2) connectors in the basement, from which the power would be distributed via risers in the building. The procedure was modified by calling for (1V) portable generators to be connected to (2V) connectors that were constructed by splicing the wiring on various floors above the basement. In this sense, two materiel substitutions (1V for 1 and 2V for 2) were made, but procedural modifications were also required, since the building risers had to be modified in order to connect the ad hoc wiring to them. (A procedure was also added, since the cleaning crew was called in to clean the building environment.) Table 4 summarizes this sequence.

The referent (here, a standard operating procedure) is an action that is triggered by some condition but, due to some contingency, cannot be executed. The referent specifies one or more inputs that are acted upon by operators to produce one or more outputs. An improvisation based on this referent may be seen as involving any of the following modifications to the referent:

A referent-based improvisation

<table><tr><td>Decision element</td><td>Result</td></tr><tr><td>Rule</td><td>If power service is interrupted,</td></tr><tr><td>Referent</td><td>Use auto-start generators and connect to connectors in the basement.</td></tr><tr><td>Unplanned-for contingency</td><td>Generators out of service due to flooding and clogging of air intakes.</td></tr><tr><td>Realization</td><td>Use portable generators, install ad hoc wiring and connect to spliced lines on appropriate floors above the basement.</td></tr></table>

(i) the use of novel inputs for existing operators,

(ii) the use of existing inputs or operators to produce new outputs, or

(iii) the development of new operators.

Modification (i) may be considered improvisation by substitution, similar to improvisation as described in the work of Hodges [25] and Mendonc¸a and Wallace [43] and Webb et al. [85]; (ii) entails a type of mix-and-match procedure that is similar to solution by assembly in the Virtual Theater [24]; (iii) requires the decision maker to create new processes and to decide on which inputs and outputs are associated with it.

A summary of the requirements discussed in this section is presented in Table 5.

## 4.3. System evaluation

It has been hypothesized that, to be effective in supporting decision making, a cognitive model should be capable of interacting with human decision makers, either on an individual or group basis [17,40]. Following this design principle should lead to a model whose intentions, thought processes and recommendations follow from the encoded theory and can be explained to human decision makers. Evaluation of the impact of the decision support system in which the model is embedded may therefore consider (i) the degree of consistency between the actual emergency situation and the way it is perceived by the model and response personnel [10,11,36,70], (ii) the effectiveness and efficiency of the team’s decisions [27,47], (iii) human team members’ perceived satisfaction with the team’s decision processes and outcomes [2] and (iv) the degree to which the system’s reasoning processes are effectively communicated to the group [41].

Table 5  
Requirements for extreme event decision support systems

<table><tr><td>Cognitive activity</td><td>Requirements</td></tr><tr><td>Categorization</td><td>Recognize the occurrence of unplanned-for contingencies</td></tr><tr><td>Search</td><td>Retrieve or infer a referent that is appropriate for the situation</td></tr><tr><td>Assembly</td><td>Generate one or more new procedures that are derived from this referent</td></tr><tr><td>Constraint satisfaction</td><td>Ensure that new procedures can be executed in a timely fashion</td></tr><tr><td>Communication</td><td>Communicate and collaborate with human decision makers</td></tr><tr><td>Inference</td><td>Reason about interdependent physical systems and the models that represent them</td></tr></table>

## 5. Conclusions

Extreme events present responding organizations with complex, unprecedented situations having the potential for widespread catastrophic losses. To assist organizations in responding to extreme events, new decision models must be developed that can accommodate flexibility and creativity by these organizations. This need is particularly strong when organizations must develop and deploy new procedures in real time. Although improvisation has been offered as one approach to addressing this need, there is little guidance for researchers and developers on how to construct and evaluate computer-based systems to support improvisation. Accordingly, prior research as well as a case study from the response to the 2001 World Trade Center attack have been analyzed, leading to three main contributions: (i) articulation of the roles of cognition and improvisation in extreme event decision making (XEDM); (ii) identification of opportunities for supporting cognition in improvised XEDM; and (iii) generation of requirements that can help guide the extension of existing theories and technologies in order to address these opportunities.

Work in meeting these requirements stands to contribute to society’s understanding of how improvisation can be both trained-for and supported, thereby addressing the need for greater flexibility in respond ing to extreme events [78]. The involvement of practitioners throughout such research is likely to be vital for its success, validity and acceptability. Given the broad surge of scholarship in the areas of extreme events and improvisation, the results of work in this area could impact research and practitioner communities as well as society at large.

## Acknowledgement

This research was supported by U.S. National Science Foundation Grant CMS-0139306.

## References

[1] D. Bailey, Improvisation: Its Nature and Practice in Music, Da Capo Press, New York, 1992.

[2] J.E. Bailey, S.W. Pearson, Development of a tool for measuring and analyzing computer user satisfaction, Management Science 29 (5) (1983) 530– 545.

[3] N. Banerjee, Con Edison crews improvise as they rewire a truncated system, New York Times, vol. 1, The New York Times Company, New York, 2001, p. 14.

[4] S. Belardo, K.R. Karwan, W.A. Wallace, An Investigation of system design considerations for emergency management decision support, IEEE Transactions on Systems, Man, and Cybernetics 14 (6) (1984) 795– 804.

[5] P.F. Berliner, Thinking in Jazz, University of Chicago Press, Chicago, 1994.

[6] G.E.G. Beroggi, W.A. Wallace, Operational risk management: a new paradigm for decision making, IEEE Transactions on Systems, Man, and Cybernetics 24 (10) (1994) 1450–1457.

[7] G.E.G. Beroggi, W.A. Wallace, Operational Risk Management: The Integration of Decision, Communications, and Multimedia Technologies, Kluwer Academic Publishers, Boston, 1998.

[8] G.E.G. Beroggi, W.A. Wallace, Multi-expert operational risk management, IEEE Transactions on Systems, Man and Cybernetics. Part C, Applications and Reviews 30 (1) (2000) 32 – 44.

[9] G.A. Bigley, K.H. Roberts, The incident command system: high-reliability organizing for complex and volatile task environments, Academy of Management Journal 44 (6) (2001) 1281– 1299.

[10] J.A. Cannon-Bowers, E. Salas, S. Converse, Shared mental models in expert term decision making, in: N.J. Castellan Jr. (Ed.), Individual and Group Decision Making: Current Issues, Lawrence Erlbaum Associates Inc., Hillsdale, 1993, pp. 221– 246.

[11] K. Carley, M. Palmquist, Extracting, representing, and analyzing mental models, Social Forces 70 (3) (1992) 601–636.

[12] N. Carver, V. Lesser, Evolution of blackboard control architectures, Expert Systems with Applications 7 (1) (1994) 1 – 30.

[13] C.G. Cech, E.J. Shoben, Categorization processes in mental comparisons, Journal of Experimental Psychology. Learning, Memory, and Cognition 27 (3) (2001) 800– 816.

[14] J.Q. Chen, S.M. Lee, An exploratory cognitive DSS for strategic decision making, Decision Support Systems 36 (2003) 147– 160.

[15] K. Chopra, R. Rush, D. Mendonc¸a, W.A. Wallace, Acquiring and assessing knowledge from multiple experts using graphical representations, in: C.T. Leondes (Ed.), Knowledge Based Systems Techniques and Applications, vol. 1, Academic Press, San Diego, CA, 2000, pp. 293– 326.

[16] P. Cohen, Models of cognition, P.R. Cohen, E.A. Feigenbaum (Eds.), The Handbook of Artificial Intelligence, vol. 3, Addison-Wesley, Boston, 1989, pp. 1 –74.

[17] P.R. Cohen, H.J. Levesque, Teamwork, Nouˆs, Special Issue on Cognitive Science and Artificial Intelligence 25 (4) (1991) 487– 512.

[18] N.J. Cooke, Varieties of knowledge elicitation techniques, International Journal of Human-Computer Studies 41 (1994) 801– 849.

[19] B. Crandall, K. Getchell-Reiter, Critical decision method: a technique for eliciting concrete assessment indicators from the <sup>b</sup>intuition<sup>Q</sup> of NICU Nurses, Advances in Nursing Science 16 (1) (1993) 42 – 51.

[20] J.C. Flanagan, The critical incident technique, Psychological Bulletin 51 (1954) 327 – 358.

[21] R.B. Gallupe, G. DeSanctis, Computer-based support for group problem-finding: an experimental investigation, MIS Quarterly 12 (2) (1988) 277–296.

[22] C. Gonzalez, F.J. Lerch, C. Lebiere, Instance-based learning in dynamic decision making, Cognitive Science 27 (4) (2003) 561– 635.

[23] B. Hayes-Roth, F. Hayes-Roth, A cognitive model of planning, Cognitive Science 3 (1979) 275–310.

[24] B. Hayes-Roth, L. Brownston, R. van Gent, Multiagent collaboration in directed improvisation, First International Conference on Multi-Agent Systems, San Francisco, CA, 1995.

[25] J. Hodges, Naive mechanics, IEEE Expert (1992) 14– 27.

[26] R.R. Hoffman, B. Crandall, N. Shadbolt, Use of the critical decision method to elicit expert knowledge: a case study in the methodology of cognitive task analysis, Human Factors 40 (2) (1998) 254– 276.

[27] D.E. Howie, K.J. Vincente, Measures of operator performance in complex, dynamic microworlds: advancing the state of the art, Ergonomics 4 (1998) 485–500.

[28] P.M. Jones, J.L. Jacobs, Cooperative problem solving in human-machine systems: theory, models, and intelligent associate systems, IEEE Transactions on Systems, Man, and Cybernetics 30 (4) (2000) 397– 407.

[29] P.M. Jones, C.M. Mitchell, Human-computer cooperative problem solving: theory, design and evaluation of an intelligent associate system, IEEE Transactions on Systems, Man, and Cybernetics 25 (7) (1995) 1039– 1053.

[30] M. Kang, L.B. Waisel, W.A. Wallace, Team-Soar: a model for team decision making, in: M. Prietula, K. Carley, L. Glasser (Eds.), Simulating Organizations: Computational Models of Institutions and Groups, AAAI Press/The MIT Press, Menlo Park, CA, 1998, pp. 23–45.

[31] R. Kennedy, Heavy-duty lifters rushed from the tracks to the tower, New York Times (2001) A20 (New York).

[32] B. Kernfeld, The New Grove Dictionary of Jazz, vol. 1, Macmillan Press Ltd, New York, 1988.

[33] G.A. Klein, A recognition-primed decision (RPD) model of rapid decision making, in: G.A. Klein, J. Orasanu, R. Calderwood, C.E. Zsambok (Eds.), Decision Making in Action: Models and Methods, Ablex Publishing Corp, Norwood, NJ, 1993, pp. 138–147.

[34] G.A. Klein, Twenty questions: suggestions for research in naturalistic decision making, in: G.A. Klein, J. Orasanu, R. Calderwood, C.E. Zsambok (Eds.), Decision Making in Action, Ablex Publishing Corp, Norwood, NJ, 1993, pp. 389– 403.

[35] G. Klein, R. Calderwood, D. MacGregor, Critical decision method for eliciting knowledge, IEEE Transactions on Systems, Man, and Cybernetics 19 (1989) 462– 472.

[36] K. Kraiger, L. Wenzel, Conceptual development and empirical evaluation of measures of shared mental models as indicators of team effectiveness, in: M. Brannick, E. Salas, C. Prince (Eds.), Team Performance Assessment and Measurement, LEA Publishers, 1997, pp. 63– 85.

[37] G.A. Kreps, Organizing for emergency management, in: T.E. Drabek, G.J. Hoetmer (Eds.), Emergency Management: Principles and Practice for Local Governments, International City Management Association, Washington, DC, 1991, pp. 30–54.

[38] R. Krishnan, X. Li, D. Steier, L. Zhao, On heterogeneous database retrieval: a cognitively guided approach, Information Systems Research 12 (3) (2001) 286–301.

[39] F.J. Lerch, D.E. Harter, Cognitive support for real-time dy namic decision making, Information Systems Research 1 (2001) 63– 82.

[40] H.J. Levesque, P.R. Cohen, J.T.H. Nunes, On acting together, Proceedings of the National Conference on Artificial Intelli gence, 1990.

[41] M. Limayem, G. DeSanctis, Providing decisional guidance for multicriteria decision making in groups, Information Systems Research 11 (4) (2000) 386– 401.

[42] J.R. Marsden, R. Pakath, K. Wibowo, Decision making under time pressure with different information sources and performance-based financial incentives—Part 1, Decision Support Systems 34 (1) (2002) 75– 97.

[43] D. Mendonc¸a, W.A. Wallace, Development of a decision logic to support group improvisation, An Application to Emergency Response, Hawaii International Conference on System Sciences (HICSS-35), Big Island, HI, 2002.

[44] D. Mendonc¸a, W.A. Wallace, Cognition in jazz improvisation, An Exploratory Study, 26th Annual Meeting of the Cognitive Science Society, Chicago, IL, 2004.

[45] D. Mendonc¸a, R. Rush, W.A. Wallace, Timely knowledge elicitation from geographically separate, mobile experts during emergency response, Safety Science 35 (2000) 193– 208.

[46] D. Mendonc¸a, G.E.G. Beroggi, W.A. Wallace, Decision support for improvisation during emergency response operations, International Journal of Emergency Management 1 (1) (2001) 30– 38.

[47] D. Mendonc¸a, G.E.G. Beroggi, W.A. Wallace, Evaluating support for improvisation in simulated emergency scenarios, Hawaii International Conference on System Sciences (HICSS-36). Big Island. HL. 2003

[48] J.L. Mennis, D.J. Peuquet, L. Qian, A conceptual framework for incorporating cognitive principles into geographic database representation, International Journal of Geographic Information Science 14 (6) (2000) 501– 520.

[49] J.R.W. Merrick, J.R. van Dorp, T. Mazzuchi, J.R. Harrald, J.E. Spahn, M. Grabowski, The Prince William Sound risk assessment, Interfaces 32 (6) (2002) 25 – 40.

[50] D.S. Mileti, Disasters by Design: A Reassessment of Natural Hazards in the United States, Joseph Henry Press, Washington, DC, 1999.

[51] A. Miner, P. Bassoff, C. Moorman, Organizational improvisation and learning: a field study, Administrative Science Quarterly 46 (2001 (June)) 304 – 337.

[52] P.H. Mirvis, Practice improvisation, Organization Science 9 (5) (1998) 586 – 592.

[53] J.L. Monday, Beyond September 11th: An Account of Post-Disaster Research, Natural Hazards Research and Applications Information Center, University of Colorado, Boulder, CO, 2003.

[54] A.R. Montazemi, K.M. Gupta, On the effectiveness of cognitive feedback from an interface agent, OMEGA, International Journal of Management Science 25 (6) (1997) 643 – 658.

[55] C. Moorman, A.S. Miner, Organizational improvisation and organizational memory, Academy of Management Review 23 (4) (1998) 698– 723.

[56] B. Nettl, Thoughts on improvisation: a comparative approach, The Musical Quarterly 60 (1) (1974) 1 –17.

[57] A. Newell, J.C. Shaw, H.A. Simon, The processes of creative thinking, in: H.E. Gruber, G. Terrel, M. Wertheimer (Eds.), Contemporary Approaches to Creative Thinking, Atherton Press, New York, 1962, pp. 63– 119.

[58] H.P. Nii, Blackboard systems, in: A. Barr, P.R. Cohen, E.A. Feigenbaum (Eds.), The Handbook of Artificial Intelligence, vol. 4, Addison-Wesley, Boston, 1989, pp. 1 – 82.

[59] T.D. O’Rourke, A.J. Lembo, L.K. Nozick, Lessons learned from the World Trade Center disaster about critical utility systems, in: J.L. Monday (Ed.), Beyond September 11th: An Account of Post-Disaster Research, Natural Hazards Research and Applications Information Center, Boulder, CO, 2003, pp. 269– 290.

[60] J. Peerenboom, R. Fischer, R. Whitfield, Recovering from Disruptions of Interdependent Critical Infrastructures, Presentation to the CRIS/DRM/IIIT/NSF Workshop on <sup>b</sup>Mitigating the Vulnerability of Critical Infrastructures to Catastrophic Failures,<sup>Q</sup> Alexandria, VA, 20012003.

[61] R. Perry, Managing disaster response operations, in: T. Drabek, G. Hoetmer (Eds.), Emergency Management: Principles and Practice for Local Government, International City Management Association, Washington, 1991, pp. 201– 224.

[62] T.A. Polk, C.M. Seifert, Cognitive Modeling, The MIT Press, Cambridge, MA, 2002

[63] President’s Commission on Critical Infrastructure Protection, Critical Foundations: Protecting America’s Infrastructures: The Report of the President’s Commission on Critical Infrastructure Protection, United States Government Printing Office 040-000-00699-1, October (1997).

[64] J. Pressing, Cognitive processes in improvisation, in: R. Crozier, A. Chapman (Eds.), Cognitive Processes in the Perception of Art, North Holland, Amsterdam, 1984.

[65] J. Pressing, Improvisation: methods and models, in: J.A. Sloboda (Ed.), Generative Processes in Music, Clarendon Press, Oxford, 1988.

[66] J. Pressing, Psychological constraints on improvisational expertise and skill, in: B. Nettl, M. Russell (Eds.), In the Course

of Performance, University of Chicago Press, Chicago, 1998, pp. 47 – 67.

[67] E.L. Quarantelli, The disaster research center field studies of organizational behavior in the crisis time period of disasters, International Journal of Mass Emergencies and Disasters 15 (1) (1997) 47– 69.

[68] W.K. Rashbaum, Police officers swiftly show inventiveness during crisis, New York Times (2001) A7 (New York).

[69] S. Rinaldi, J. Peerenboom, T. Kelly, Complexities in identifying, understanding, and analyzing critical infrastructure interdependencies, IEEE Control Systems Magazine (2001 (December)) 11 – 25.

[70] W.B. Rouse, J.A. Cannon-Bowers, E. Salas, The role of mental models in team performance in complex systems, IEEE Transactions on Systems, Man, and Cybernetics 22 (6) (1992) 1296–1308

[71] J.G. Routley, Fire and Explosions at Rocket Fuel Plant Henderson, Nevada, U.S. Fire Administration, Emmitsburg, MD TR-021 (n.d.).

[72] E. Sarath, A new look at improvisation, Journal of Music Theory 40 (1) (1996) 1– 38.

[73] J. Scanlon, The role of EOCs in emergency management: a comparison of American and Canadian experience, International Journal of Mass Emergencies and Disasters 12 (1) (1994) 51–75.

[74] R. Schank, R. Abelson, Scripts, Plans, Goals, and Understanding, Lawrence Erlbaum, Hillsdale, NJ, 1977.

[75] J.A. Sloboda, The Musical Mind, Clarendon Press, Oxford, 1985.

[76] C. Smart, I. Vertinsky, Designs for crisis decision units, Administrative Science Quarterly 22 (1977) 640 – 657.

[77] D. Srinivasan, Battling hazards with a brand new tool, Planning (2003 (February)) 10–13.

[78] T.R. Stewart, A. Bostrom, Extreme Event Decision Making: Workshop Report, University at Albany, Albany, NY June, 2002.

[79] B.A. Turner, The role of flexibility and improvisation in emergency response, in: T. Horlick-Jones, A. Amendola, R. Casale (Eds.), Natural Risk and Civil Protection, E. & F. Spon, London, 1995, pp. 463– 475.

[80] U.S. General Accounting Office, Critical Infrastructure Protection, Washington, DC GAO-01-323, 12 September (2001).

[81] P. Venkataraman, D. Mendonc¸a, Using process data to populate ontologies, IEEE International Conference on Systems, Man and Cybernetics, Washington, DC, 2003.

[82] B. Vidaillet, Cognitive processes and decision making in a crisis situation: a case study, in: T.K. Lant, Z. Shapira (Eds.), Organizational Cognition: Computation and Interpretation, Lawrence Erlbaum Associates, Mahwah, NJ, 2001, pp. 241– 263.

[83] W.A. Wallace, D. Mendonc¸a, E. Lee, J. Mitchell, J. Chow, Managing disruptions to critical infrastructure interdependencies in the context of the 2001 World Trade Center attack, in: J.L. Monday (Ed.), Beyond September 11th: An Account of Post-Disaster Research, Natural Hazards Research and Applications Information Center, Boulder, CO, 2003, pp. 165 – 198.

[84] I. Watson, F. Marir, Case-based reasoning: a review, The Knowledge Engineering Review 9 (4) (1994) 327 – 354.

[85] G.R. Webb, M. Beverly, M. McMichael, J. Noon, T. Patterson, Role improvising under conditions of uncertainty, A Classification of Types, Preliminary Paper, vol. 289, University of Delaware, Newark, DE, 1998

[86] K.E. Weick, The collapse of sensemaking in organizations: the Mann Gulch disaster, Administrative Science Quarterly (1993 (Dec)) 628– 652.

[87] K.E. Weick, Improvisation as a mindset for organizational analysis, Organization Science 9 (5) (1998) 543 – 555.

[88] G.R. Yost, A. Newell, J.C. Shaw, H.A. Simon, A problem space approach to expert system specification, in: P.S. Rosenbloom, J.E. Laird, A. Newell (Eds.), The Soar Papers: Research on Integrated Intelligence, vol. 2, MIT Press, Cambridge, MA, 1993, pp. 982– 988.

[89] R.W. Zmud, Supporting senior executives through Decision Support Technologies: a review and directions for future research, in: E.R. McLean and H.G. Sol (Eds.), Decision Support Systems: A Decade in Perspective, North Holland, Amsterdam: Elsevier Science (1986).

[90] C.E. Zsambok, G. Klein, Naturalistic Decision Making, Lawrence Erlbaum, Mahwah, NJ, 1997.

![](/api/attachments/YNYJ599K/fulltext/images/d697577cf284c47b4845add1317fe2b94b5897d73e701c64c5230c6ca6626f85.jpg)  
David Mendonc¸a is an Assistant Professor in the Information Systems Department of the College of Computing Sciences at New Jersey Institute of Technology in Newark, NJ. He has a Ph.D. in Decision Sciences and Engineering Systems from Rensselaer Polytechnic Institute, an M.S. from Carnegie Mellon University and a B.A. from University of Massachusetts/ Amherst.
