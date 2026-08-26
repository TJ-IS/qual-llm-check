---
otero_id: 21153
otero_key: "XB4PPXNY"
title: "Intelligent delivery of military lessons learned"
authors: "Rosina O. Weber; David W. Aha"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00122-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Intelligent delivery of military lessons learned

Rosina O. Weber <sup>a,</sup>\*, David W. Aha <sup>b</sup>

<sup>a</sup>College of Information Science and Technology, Drexel University, 3141 Chesnut Street, Philadelphia, PA 19104, USA <sup>b</sup>Navy Center for Applied Research in Artificial Intelligence, Naval Research Laboratory (Code 5515), Washington, DC 20375, USA

## Abstract

Lessons learned systems (LLS) are a common knowledge management (KM) initiative among the American government agencies (e.g., Department of Defense (DOD), Department of Energy (DOE), NASA). An effective lessons learned (LL) process can substantially improve decision processes, thus representing an essential chapter in a knowledge-sharing digital government. Unfortunately, these systems typically fail to deliver lessons when and where they are needed. In this paper, we introduce, describe, and empirically evaluate the monitored distribution (MD) approach for the active delivery of lessons learned. Our results show that this just-in-time information delivery approach, embedded in a decision support system (DSS) for plan authoring, significantly improved plan execution performance measures. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Knowledge management; Lessons learned systems; Just-in-time knowledge; Case-based reasoning; Noncombatant evacuation operations

## 1. Introduction

Lessons learned systems (LLS) are knowledge management (KM) initiatives structured over a repository of lessons learned (LL). Lessons learned are knowledge artifacts that convey experiential knowledge that is applicable to a task, decision, or process such that, when reused, this knowledge positively impacts an organization’s results. For this reason, LLS are ubiquitous in governmental organizations that need to leverage knowledge, such as the Department of Defense (DOD), where military operations may risk human lives, the Department of Energy (DOE), where accident prevention is a major concern, and space agencies (e.g., American space agency (NASA), European space agency (ESA), Japanese space agencies (NASDA)) due to their potential for incurring costly mission failures.

A potential problem that the digital government needs to face originates from the abundance of information resulting from the digitization of government processes. Organizing all this digital information may not suffice if there are not enough intelligent minds available to use that information. Thus, knowledge sources for using digitized information and supporting decision-making are needed in the service of the government’s goals. The answer to this problem lies in using effective KM processes that can help humans make decisions by providing the right applicable knowledge when and where there are processes and valuable information.

An example of abundant and idle digital information available in the government is the Navy Lessons Learned System (NLLS [23]) repository, with approximately $3 5 , 0 0 0 ^ { 1 }$ lessons learned. The NLLS lacks effective methods for delivering these lessons to potential users to support military decision-making processes. This has been referred to as the lesson distribution gap [5]. In this paper, we propose the monitored distribution (MD) solution to bridge this gap, extending our work in Ref. [5] and detailing the delivery of military lessons in continuation of our research on intelligent lessons learned systems, which began with the publication of a survey [37].

The applicability of the MD approach is not limited to military lessons. Our evaluation indicates that this approach has the potential to improve the quality of targeted processes (and decisions) by pushing validated experiential knowledge when and where it is applicable (at the time of decision making). The use of a repository to improve knowledge sharing is appropriate depending on the nature and structure of an organization. For example, large hierarchical organizations might benefit because their members may not have the opportunity to easily interact. Likewise, knowledge sharing could benefit organizations (e.g., military) that cannot employ automatic methods to incorporate new and experiential knowledge into their doctrine. Also, organizations in rapidly changing fields (e.g., ones that rely on innovation and high technology), or whose knowledge is used infrequently [27] or is highly variable (e.g., military operations are repeated in different countries and circumstances), may benefit. Finally, knowledge sharing is crucial for organizations in which sharing a single experience can save lives (e.g., the DOD). For all organizations that fit into one or more of these cases, it is important to use a knowledge repository to support sharing and leveraging of experiential knowledge.

In Section 2, we describe LLS in the context of knowledge management initiatives. Section 3 then concerns the nature of the lessons learned process (LLP) with respect to general knowledge processes. Section 4 details definitions of, representations for, and examples of LL. In Section 5, we describe the lesson distribution gap. We explain our proposed solution, monitored distribution, and exemplify it in Section 6. In Section 7, we evaluate the proposed MD approach in the context of a decision support tool for planning military missions. In Section 8, we describe related methods for active lesson delivery, and we conclude with a description of future goals.

## 2. Knowledge management initiatives

A study published in 1998 [9] identified three types of KM initiatives. The first, knowledge repositories, are technologically motivated because they usually start with the purchase of software to store the repository. A second initiative focuses on knowledge access and transfer; it attempts to connect members who are in need of knowledge to the ones who possess the desired knowledge. Third, the knowledge environment type refers to initiatives that attempt to change behavior towards knowledge, treating it as a capital asset. In the remainder of this paper, we focus on the first type, knowledge repositories.

## 2.1. Knowledge repositories

KM initiatives that focus on knowledge repositories represent a category of organizational KM systems that interleave a knowledge repository with an organization’s members, as sketched in Fig. 1. In these types of KM systems, the central unit is a repository of knowledge artifacts [15] that is collected from (internal or external) organizational sources and distributed back to them. These KM systems can vary based on the type of knowledge artifact stored, the scope and nature of the topic described, and the orientation [37].

![](/api/attachments/XB4PPXNY/fulltext/images/c9bfe0390c6edf04a217ddac5693f80dbd863cb57e66cc8e0c12280f7563c6a1.jpg)  
Fig. 1. Knowledge repository initiatives manage a repository of an organization’s knowledge artifacts.

Knowledge artifacts can be lessons learned, best practices, alerts, videos, and so forth. For example, best practices are usually industry-oriented because they describe successful complete processes as benchmarks. In contrast, lessons learned are usually organization oriented: They can either be successes or failures and are applicable to tasks or decisions within organizational processes. Alert systems [28] are industry oriented, where alerts originate from failures (i.e., defective parts).

## 2.2. Lessons learned systems

Based on the explanation above, lessons learned systems are knowledge repository initiatives that store lessons learned. Lessons learned systems, which were surveyed in Ref. [37], are organization-oriented initiatives that were primarily developed by groups whose goals include preventing the recurrence of situations that caused fatalities and high costs. These include Department of Defense initiatives, where lessons learned systems have been developed for each of the services, the Department of Energy, whose Society for Effective Lessons Learned Sharing (SELLS) grass-roots organization holds workshops twice annually and has more than 100 members [30], and space agencies from the USA, Europe, and Japan [20,28]. Fig. 2 lists some organizations that employ LLS.

## 3. Knowledge processes

Knowledge processes have been identified as specific methodologies for representing the organizational learning cycle of different types of KM initiatives [21]. For example, in Ref. [31], a knowledge process is defined to include subprocesses concerning knowledge creation, knowledge import, knowledge capture, knowledge retrieval and access, and knowledge use. In Ref. [33], a summary of knowledge processes distinguishes four basic subprocesses: developing new knowledge, securing new and existing knowledge, distributing knowledge, and combining available knowledge. Basically, they all specify the flow of knowledge among different organizational entities that convey knowledge artifacts throughout an organization in service of its goals.

## 3.1. Lessons learned process

A LLP is an instance of a knowledge process for lessons learned repositories that supports their leveraging and sharing. A LLP exclusive to the construction industry has been described in Ref. [12]. Based on this previous work, our survey in Ref. [37] focused on governmental organizations and used a widely adopted definition for lessons learned (see Section 4.1) to describe a five-part LLP: collect, verify, store, distribute, and reuse.

A military LLP (Fig. 3) typically involves a lessons learned center whose members are responsible for populating the repository. Because lessons originate from experiences, they are collected from military personnel who have lived the experiences while engaging in military missions. Lessons obtained by the collect subprocess are submitted to subject matter experts to undergo a verification subprocess that, according to the definition of lessons, requires them to be correct (see Section 4.1). The store subprocess then inserts verified lessons into the LL repository, from which they are disseminated to military personnel through distribution methods. Hence, prospective users can reuse these lessons in military exercises and missions in which they engage.

![](/api/attachments/XB4PPXNY/fulltext/images/333d46f131440510b153b6bc93cbcf396885b725c54c7fab4b536a9193791477.jpg)  
Fig. 2. Some organizations that have developed LLS.

![](/api/attachments/XB4PPXNY/fulltext/images/86e060522001591bad2021c6c09baf6cc9fd56a233afd102dc39c27684249a8e.jpg)  
Fig. 3. A military lesson learned process.

## 3.2. Case-based reasoning (CBR) process

Knowledge processes in intelligent systems are also intended to support knowledge methodologies. Among these, the CBR cycle (Fig. 4) [1] has several commonalities with the military LLP, in that both involve the acquisition and reuse of knowledge artifacts.

The CBR cycle’s subprocesses are RETRIEVE, REUSE, REVISE, and RETAIN. These four subprocesses are directly analogous to the subprocesses in the military LLP. RETRIEVE involves retrieving cases from a ‘‘case base’’, which is analogous to distributing lessons from a lesson repository. Both the CBR and LL processes include an element of REUSE to apply retrieved/distributed artifacts to a new problem. In the REVISE subprocess, we find their main distinction: In CBR, revision searches for possible corrections to improve the reuse of a knowledge artifact that can be RETAINed while, in the military LLP, lessons are verified after collection from military personnel so that they can be stored in the lessons repository. In the military LLP, any adaptation to improve knowledge reuse is normally not stored; knowledge derives from experience and it is input in the cycle exclusively via collection.

The commonalities between the CBR and LL processes have also been the focus of an AAAI Workshop [4]. Among this workshop’s conclusions is the suggestion of using theoretical guidelines from the CBR literature to support LL processes. In Section 4, we present the lessons learned artifact and use CBR theory to structure its representation.

![](/api/attachments/XB4PPXNY/fulltext/images/df87eb5f01f16723c83f454886fa5ad195c9c7ab64cafbc06dda543b612833d0.jpg)  
Fig. 4. The CBR cycle proposed in Ref. [1].

## 4. Lessons learned

## 4.1. Definition

Among many proposed definitions for lessons learned, we adopt the one given in Ref. [29]:

A lesson learned is a knowledge [artifact] or understanding gained by experience. The experience may be positive, as in a successful test or mission, or negative, as in a mishap or failure. Successes are also considered sources of lessons learned. A lesson must be significant in that it has a real or assumed impact on operations; valid in that is factually and technically correct; and applicable in that it identifies a specific design, process, or decision that reduces or eliminates the potential for failures and mishaps, or reinforces a positive result.

This definition implies a set of requirements for lessons specified through the phrases knowledge, experience, impact on operations, technically correct, and applicable. These phrases conform to the structure of a LLP (e.g., the need for a subprocess to verify lessons for correctness, and a reuse subprocess to apply lessons). Furthermore, this definition also suggests relevant components to include in a computable representation for lessons.

## 4.2. Lessons learned representation

We use the commonalities between LL and CBR processes to define a LL representation that can potentially improve the overall LLP. Based on the definition of lessons learned, we need a representation of experiential knowledge that is applicable, correct, and can be used to positively impact operations. Because it is experiential knowledge, and due to the commonalities between LL and CBR processes, we consider a case representation for lessons. This case representation has to be designed such that it promotes the retrieval of lessons based on their applicability. In Section 5.4, we explain problems with distribution methods that emphasize why lessons should be distributed based on their applicability. The other problem that we address with lesson representations is their ease of interpretation.

Table 1  
The selected representation for lessons learned

<table><tr><td colspan="2">The selected representation for lessons learned</td></tr><tr><td>Indexing elements (problem)</td><td>Applicable taskPreconditions</td></tr><tr><td>Reuse elements (solution)</td><td>Lesson suggestionRationale</td></tr></table>

Table 2  
Example lesson from NLLS [23] on assigning air traffic controllers

<table><tr><td>Applicable task</td><td>Action: Assign air traffic controllers.Mission type: NEOUJTL task: Provide for movement services in theater of operations.</td></tr><tr><td>Preconditions</td><td>A civilian airport is used for military air traffic.</td></tr><tr><td>Lesson suggestion</td><td>Assign military air traffic controllers.</td></tr><tr><td>Rationale</td><td>Type: FailureWhat? Military traffic overloaded civilian controllers.Why? The rapid build-up of military flight operations at Mactan International Airport, Cebu quickly overloaded the civilian host nation controllers.</td></tr></table>

In a simplified view of case representation, a case has two primary components: a problem and a solution (Table 1). The case’s problem describes the state of the world when the case occurred, while the case’s solution prescribes how to solve that problem [35]. In the CBR cycle, the problem portion is used to index and guide retrieval, while the case solution is the portion that is reused to solve each new problem. Therefore, we organize the elements considered in the LL definition, focusing on ease of interpretation and the desire to retrieve lessons according to their applicability. This yields a representation for lessons, shown in Table 1, whose objective is to provide an applicable lesson representation.

Tables 2, 3 and 4 show examples of different types of lessons in diverse domains.<sup>2</sup> Table 2 is an example from NLLS [23]. It is a typical military lesson, where the impact is on avoiding mission failure. Table 3 is an example from the Best Buy repository [18]; it is a typical example of a private organization’s lesson, where the potential impact is on avoiding or reducing costs. Table 4 is an example from a Project Hanford Lessons Learned repository [11], typical of DOE laboratories, where the lesson’s potential impact is on avoiding accidents.

Table 3  
Example lesson from Best Buy [18] on installing custom stereo speakers

<table><tr><td>Applicable task</td><td>Installing custom stereo speakers.</td></tr><tr><td>Preconditions</td><td>The car is the Porsche Boxster.</td></tr><tr><td>Lesson suggestion</td><td>Make sure you distinguish the wires leading to the speakers from the wires leading to the side airbag.</td></tr><tr><td>Rationale</td><td>Somebody has cut the wrong wire because they look alike and the airbag went off with explosive force. This means spending several thousand dollars to replace the airbag in addition to be a potential hazard.</td></tr></table>

By indexing lessons directly with the task (i.e., the task, decision, or process) to which they are applicable we promote a retrieval based on applicability. The second element, preconditions, refers to state conditions that distinguish when the lesson is applicable. The reuse portion consists of a lesson suggestion, which captures what was learned through experience that should be repeated or avoided. Finally, the rationale gives the prospective user a justification by stating how this lesson was learned.

All these elements consist of a set of features. For example, the applicable task is described in terms of the final activity or action, but it must also indicate the process for which it is a component. The example applicable task in Table 2 is described in terms of a task (i.e., Assign air traffic controllers), but this action can be performed in many different missions. Therefore, the description also includes the mission type (NEO missions are described in Section 7.2) and the task in Universal Joint Task List<sup>3</sup> (UJTL).

The lesson rationale also consists of a set of subfields (i.e., type, what, and why). The rationale type distinguishes three possible origins of a lesson: success, failure, and advice. The second subfield is a description of what happened; and the third summarizes the cause. The examples in Tables 2 and 4 illustrate the rationale.

Table 4  
Example lesson on replacing headlights

<table><tr><td>Applicable task</td><td>Exchanging the headlight in the hood of a vehicle.</td></tr><tr><td>Preconditions</td><td>The headlight is located near the hood where the battery is.</td></tr><tr><td>Lesson suggestion</td><td>Remove any metallic jewelry when exchanging the part.</td></tr><tr><td>Rationale</td><td>Type: FailureWhat? Someone exchanged the headlight without removing his watch and received 3rd degree burns.Why? The person overlooked safety procedures and did not remove the jewelry. Then, one side of his watch contacted the positive terminal of the battery and the other side grounded against the chassis causing the burns.</td></tr></table>

## 5. The lesson distribution gap

The lesson distribution gap refers to the difficulty of transmitting lessons between a lessons learned repository and its prospective users. In this section, we describe methods for lesson delivery with respect to these users, enumerate problems with these methods, and deduce the characteristics of a method to bridge this gap.

## 5.1. Lesson distribution methods

The LLP presented in Section 3.1 consists of five subprocesses (i.e., collect, verify, store, distribute, and reuse). Different services use distinct methods to implement these subprocesses. Both deployed and research examples of these methods were surveyed in [37]. Our scope is limited to distribution methods that we group into two delivery styles, called push and pull, between a user and a source.<sup>4</sup> These methods for information delivery concern the traffic between the user and the information source. This traffic varies based on the number, size, and orientation of the messages delivered [8].

## 5.2. Pull

Pull methods leave all the burden of search to the user, who must completely devote his or her attention to the source and, therefore, will only capture desired information. Examples of pull methods are library and web searches. The most traditional pull method for disseminating lessons is a passive distribution approach in which users search for lessons using a standalone repository or bulletins.

## 5.3. Push

Push methods attempt to relieve the burden on the users by either taking the initiative to disseminate information or by allowing the user to direct attention and resources to efforts other than the information source. In broadcasting, lessons are pushed to all the members of an organization through bulletins without being solicited. In active casting, lessons are broadcasted to potential users via a dedicated list server in an attempt to anticipate a user’s needs. This method relies on the expected need of knowledge based on the roles of individuals. Recently, some LL centers have begun using information-gathering tools (e.g., web crawlers, spiders) that, given a user’s query, can search for and push relevant lessons to that user. Information gathering methods can quickly perform searches that, when using other search engines, may require a period ranging from three days to several weeks [8]. They can also update their results autonomously.

An alternative method is possible when lessons are abstract and general. General lessons do not depend on many preconditions to be applicable to some tasks or can be applied to a category of tasks [38]. In this case, these lessons can be incorporated into an organization’s body of knowledge (e.g., military doctrine). Doctrine is delivered to military personnel by many methods (e.g., training). Once incorporated into doctrine, they are no longer considered to be experiential lessons.

## 5.4. Problems with lesson distribution methods

Although push methods offer the advantage of allowing the user to devote attention to other concerns, these methods still suffer from some of the problems that confound traditional pull methods:

 Distribution is divorced from targeted organizational processes.

 Users may not know or be reminded of the repository, as they need to access a standalone tool to search for lessons. Also, users may not be convinced of the potential utility of lessons.

 Users may not have the time or skills to retrieve and interpret textual lessons.

 Users may not be able to apply lessons successfully.

Together, these problems greatly limit the utility of push methods that exist as standalone tools, divorced from the organizational processes targeted by the lessons. We elaborate on the implications in Section 5.5.

## 5.5. The gap

The problems listed in Section 5.4 indicate the existence of a gap [5] between a lesson repository and the processes targeted by these lessons, as illustrated in Fig. 5.

In order to bridge this gap, we must address each of the problems listed above. This requires merging the repository with the organizational process(es) targeted by its lessons. This eliminates the need for users to be reminded of the lessons because they do not need to access a standalone tool to search for lessons.

Merging the contexts of the lesson repository and the organizational processes does not eliminate all the problems with current distribution methods. We also need a distribution approach that is tightly integrated to the applicable processes so that knowledge is distributed not only where but also when it is needed. This requires adopting active methods [37] (i.e., methods that deliver content autonomously without any solicitation), which have some requirements. For example, users must be engaged in targeted processes using a software tool that supports decision-making. Consequently, one must identify what the best mo ment is to deliver lessons. In our work, these moments occur during mission planning, in which we assume that the prospective users are using a software tool for authoring plans. This tool provides a context for detailing and recording plans, and also defining and allocating resources. Thus, it also provides opportunities for the timely reminding of pertinent strategies and lessons.

![](/api/attachments/XB4PPXNY/fulltext/images/1dde9f92a6675134bc137b78ab003a51849fe1618dcae040dd7cafe10c3332e1.jpg)  
Fig. 5. The lesson distribution gap.

Another issue with active methods is that they are intrusive and annoying if they distribute knowledge that is not applicable. The MD [5] approach, which we detail in Section 6, represents lessons as cases, thus providing a retrieval capability that is based on lesson applicability to improve retrieval precision.

In summary, the MD approach has the following benefits:

 Distribution takes place in the context of targeted organizational processes.

 Distribution is tightly integrated with the targeted organizational processes.

 Users need not know or be reminded of the repository to use lessons, nor require lesson retrieval skills.

 Users can assess the potential utility of lessons by analyzing the lesson’s rationale.

 Users do not need significant additional time to retrieve lessons.

 Lesson interpretation is facilitated as lessons are displayed with all relevant attributes.

 Because lessons are integrated with the targeted processes, interfaces can be developed with the MD approach to allow users to execute lesson suggestions.

## 6. Monitored distribution

We implemented the MD approach in the Active Lesson Delivery System (ALDS) [5], which can be integrated as a module of a decision support system (DSS) to distribute lessons when and where they are needed in a just-in-time knowledge delivery fashion [7]. This requires indexing lessons by the decisions, tasks, and processes known to the DSS.

Potentially, ALDS can be integrated with any DSS. The requirements for the integration are that the DSS has a flexible architecture and that the decision/task/ process and state conditions that determine decisionmaking are explicitly represented (i.e., so that an applicability oriented retrieval process can be used to distribute lessons).

## 6.1. Architecture

Fig. 6 displays a simplified sketch of a DSS with an embedded monitored distribution approach, ALDS. In this sketch, the inputs of the DSS are state conditions and the current task or decision that the user is engaged. The DSS output is not affected by ALDS. ALDS keeps track of the state conditions input by the user and uses them plus the current task to assess their similarity to recorded lessons stored in the lesson base. If a lesson is considered to be sufficiently similar to the current situation and applies to the current task, then ALDS considers it to be applicable. Applicable lessons are displayed to the user as an additional output of the system. The lesson is displayed, with all its components (see Fig. 7), so that the user can make an informed decision regarding its reuse, thus helping to achieve the organization’s goals.

![](/api/attachments/XB4PPXNY/fulltext/images/243f2239f122fe0ac46f17888b0880f0d758334d62e313360c8258b525db2e1c.jpg)  
Fig. 6. An architecture for integrating monitored distribution in a decision support system.

Given that the decisions and state conditions in a DSS are explicitly represented, a MD module can be integrated by representing lessons in the same representation format as decisions and conditions. A similarity assessment subprocess tracks the current decision and state conditions to obtain a similarity score that, by comparing with a threshold, establishes whether a given lesson is sufficiently similar and, therefore, applicable.

![](/api/attachments/XB4PPXNY/fulltext/images/d55fdee3fac1ff90723012bbc9827e8227e683b30927959e43566abac98d3117.jpg)  
Fig. 7. Active lesson delivery in HICAP using monitored distribution.

## 6.2. Example

We have integrated ALDS, our implementation of the MD approach, with HICAP<sup>5</sup> [22], a plan authoring tool suite that helps its user to construct a hierarchical plan. Initially, HICAP presents a Hierarchical Task Network (HTN) consisting of the main tasks that comprise the mission (based on doctrine). Users interact with HICAP by iteratively refining a HTN through task decompositions to build a desired plan. During task decomposition, HICAP asks users about state conditions, and ALDS compares these conditions with the states described in each lesson for the currently selected task. Lessons are indexed with tasks in HICAP’s task hierarchy. Although HICAP can be used in any hierarchical planning domain, we focus here on mission planning for NEOs (Section 7.2).

Fig. 7 illustrates the active delivery of lessons in HICAP. Because the displayed lesson’s task matches the user’s selected (active) task, and its preconditions match those in the current state, it was brought to the user’s attention. Its suggestion involves substituting a new task named Assign high visibility to air wing. At the bottom of the lesson, there is an Apply button that, if selected, automatically implements the lesson’s suggestion (i.e., replacing the currently selected task with the lesson’s suggested task).

## 7. Empirical evaluation

The problem that we propose to solve with the monitored distribution approach (e.g., as implemented in ALDS/HICAP) is to bridge the gap between lessons and their prospective users, who are engaged in military operations whose results (i.e., measures of effectiveness) can be potentially improved by applying experiential knowledge. With this purpose in mind, we embedded ALDS in HICAP, which is a

DSS that generates plans. We want to test whether the use of MD can positively impact the performance measures of plans authored using HICAP.

## 7.1. Hypothesis

Our hypothesis is that using lessons will improve plan quality (i.e., using lessons collected by the military services can improve the quality of actual plans that embed tasks described in these lessons). The plans generated in our experiment concern noncombatant evacuation operations (NEOs). We introduce NEOs in Section 7.2. We measure plan quality using domain-specific (used for real NEOs) measures of effectiveness (e.g., plan duration, casualty rates).

## 7.2. Noncombatant evacuation operations

Noncombatant evacuation operations are military operations for evacuating endangered noncombatants to a safe haven. The danger can originate from political instability or because of a natural disaster that threatens lives of American citizens who are living abroad. These operations are joint operations—they usually involve at least two or more military services (e.g., Navy, Marine Corps).

If a NEO order is given (e.g., through the request of a USA ambassador), then the operational forces involved gather at an assembly point. This is when they learn about the need for a NEO, the location, and the size of force allocated for the mission. At the assembly point, the commanders define a location for the mission headquarters. They refine the plan by determining locations for the intermediate staging base and the safe haven. The primary goal of a NEO is to safely transfer the evacuees from the NEO site to the safe haven. A simplification of a NEO plan is depicted in Fig. 8.

## 7.3. Methodology

The plans generated in HICAP, and the lessons employed, refer to NEOs. In order to evaluate the quality of the resulting plans, we implemented a nondeterministic NEO plan executor. For our evaluation, we generated 100 plans with and 100 plans without lessons. To account for the nondeterministic aspects of the plan executor, we executed each set of plans ten times to estimate average performance measures and their standard deviations.

![](/api/attachments/XB4PPXNY/fulltext/images/df73fd8e843ceff213c86b76550dad438b630ad4c428dad33b3e22dd6be0d5c5.jpg)  
Fig. 8. A simplified abstraction of a NEO plan.<sup>6</sup>

## 7.3.1. Simulated users

Because HICAP is an evolving prototype that has not yet been tested in military exercises, we have not yet tested the MD approach with military planners. Instead, we developed a simulated user to respond consistently while choosing task decompositions and to generate plans using HICAP both with and without lessons in an unbiased fashion. When ALDS detects a matching lesson, the simulated user always applies the lesson suggestion.

Had we chosen to use real rather than simulated users, we would then have to track their lesson usage because some users would use the lessons while others would not. Thus, by using simulated users, we have simplified the interpretation of the results; we know exactly why the results for the second set of experiments were better—because the lessons were used (i.e., we varied only one independent variable).

## 7.3.2. Selecting lessons

We used 13 actual lessons drawn from the NLLS [23] in the experiment. Ideally, the lessons included in this evaluation should be drawn randomly from among the entire NLLS. However, our objective is only a proof of concept to show that using some actual lessons can yield improvements when executing the result of the decision support process (i.e., the generated plan). Thus, our selection of these specific 13 lessons simply allowed us to draw a comparison between (a) testing the system without lessons vs. (b) testing the system when some lessons are available and would be used during plan authoring. Therefore, it was imperative that selected lessons referred to tasks that were part of the plans whose quality we could assess with domain-specific measures.

We have started our selection by choosing a subset of lessons, which were returned by the NLLS text retrieval tool when we used the keyword ‘‘NEO’’. The number of lessons retrieved containing the keyword NEO from the Sep 1998 repository of unclassified active (i.e., less than 2 years old) lessons collected by the Navy was 57. The second step was to remove all lessons that were either completely useless (i.e., because they did not comprise real lessons) or did not address NEO related tasks. The result is the final set of 13 lessons. In sum, these 13 were selected because (1) they concerned tasks performed during NEO missions and (2) they are actual lessons collected and stored in NLLS. The experimental results would not have differed had we included all 35,000 lessons because only these 13 would have been used.

Next, we converted these 13 lessons from their original text format into a case representation that matches HICAP’s lesson representation. After preparing these lessons, we then prepared HICAP to build plans that included the lessons’ applicable tasks and to interact with simulated users. Two lessons from the 13 lessons used in the experiment are displayed in Tables 5 and 6.

## 7.3.3. Dependent variables

Our plan executor simulates the execution of a NEO plan and records (1) their total duration, (2) their duration until medical assistance becomes available, and (3) their casualty rates for evacuees, friendly forces, and enemies. These evaluation measures were chosen from military doctrine [32].

We have focused on keeping all independent variables constant except the independent variable of interest (i.e., whether or not lessons are used). In particular, we kept constant the (simulated) user, who acted the same in both experiments (i.e., it always applied lessons, but was given lessons only in the first set of 100 plans).

Table 5  
A lesson from NLLS on assigning security elements

<table><tr><td>Applicable task</td><td>Assign security element.</td></tr><tr><td>Preconditions</td><td>There are hundreds or more evacuees as to justify a security effort.</td></tr><tr><td>Lesson suggestion</td><td>Recommend that explosive ordnance disposal (EOD) personnel are utilized in security element.</td></tr><tr><td>Rationale</td><td>Type: SuccessWhat? Ten EOD personnel were employed in a force protection role and assisted USS Nassau security teams.Why? They have identified and investigated suspect items brought aboard by evacuees.</td></tr></table>

Table 6

<table><tr><td colspan="2">Lesson from NLLS on establishing a liaison team</td></tr><tr><td>Applicable task</td><td>Action: Set up Liaison team.Mission type: NEOUJTL task: Communicate operational information</td></tr><tr><td>Preconditions</td><td>There are representatives of different branches assigned to participate in the mission.</td></tr><tr><td>Lesson suggestion</td><td>Assign representatives of all forces to plan.</td></tr><tr><td>Rationale</td><td>Lack of representatives prevents good communication causing delays and miscommunication.</td></tr></table>

## 7.3.4. NEO plan executor

The NEO plans that we created consisted of 30 variables, of which 12 are random (i.e., their values were assigned randomly according to a uniform distribution) variables that describe the planning scenario’s initial state. These variables include: existence of an airport in each of the segments, weather conditions, number of evacuees, terrain conditions, availability of helicopters, hostility level, size of force, and so forth.

When creating a plan, simulated users must make decisions on 18 variables that describe the length of the generated plans. These 18 variables have two to four possible values. More precisely, six have three possible values, four have four possible values, and eight have two possible values, which, together, yield a space of 47,775,744 possible plans. These decisions refer to aspects such as which route and transportation mode to use in each segment (e.g., helicopter, armored vehicle), the amount of medical inventory to allocate, and the assignment of particular experts (e.g., communications, explosive ordnance disposal).

For this experiment, we constructed a nondeterministic NEO plan executor that models uncertainties from the NEO domain. The executor simulates the execution of the NEO plans according to its five segments (see Fig. 8) using domain knowledge. For example, the chances of enemy attack increase when evacuees are transported via land transportation modes. There are also probabilities associated with helicopter and airplane crashes, where helicopter crashes are more likely when weather conditions include very strong winds.

The executor finds values for the measures based on the combination of random variables, user’s decisions, and random effects. Suppose for a given transportation segment that the random variable weather has the value strong winds, the user’s decision for transportation mode is helicopter, and the random effect results in a crash. Then the casualty rate increases in proportion to the number of evacuees and friendly forces that were transported in each helicopter that crashed.

## 7.4. Results

As summarized in Table 7, the MD approach implemented in ALDS/HICAP using lessons substantially improved plan quality (i.e., plan execution performance measures), namely it reduced execution time and casualty rates. More generally, this improvement indicates that MD can potentially improve the decision-making quality produced when embedding it to a decision support system. MD can augment a DSS so that it delivers timely, relevant, and applicable experiential knowledge.

We used two kinds of performance measures. Durations were measured for total duration, with a reduction of 18%; and duration until medical assistance became available, which also reduced an average of 18%. The other category of measures concerned casualties. The most significant reduction was observed in casualties among friendly forces with 30% decrease. Casualties among evacuees indicated a reduction of 24%. The variation for casualties among enemies was negative, indicating an increase.

Average plan execution results for simulated NEO plans authored using HICAP

<table><tr><td></td><td>Without lessons</td><td>With lessons</td><td>% Reduction with lessons</td></tr><tr><td>Mean duration (hr)a</td><td>39h50</td><td>32h48</td><td>18</td></tr><tr><td>Standard deviation (hr)a</td><td>16h51</td><td>16h12</td><td>-</td></tr><tr><td>Mean duration until medical assistance (hr)</td><td>29h37</td><td>24h13</td><td>18</td></tr><tr><td>Standard deviation (hr)</td><td>11h13</td><td>10h26</td><td>-</td></tr><tr><td colspan="4">Mean % casualties:</td></tr><tr><td>Evacuees</td><td>11.48</td><td>8.69</td><td>24</td></tr><tr><td>Friendly forces</td><td>9.41</td><td>6.57</td><td>30</td></tr><tr><td>Enemies</td><td>3.08</td><td>3.14</td><td>-2</td></tr></table>

A brief examination of the results (i.e., the first run for each of the 100 plans), using a standard Student’s t test, revealed significant differences for both overall duration ( p<0.1, t=1.60, df=99) and duration until medical assistance arrived ( p<0.1, t =1.39). All of the lessons were applicable in the generated plans, and, when lessons were used, approximately three were used per plan.

These results favorably corroborate our hypothesis that the MD approach can generate better plans for realistic problem domains. However, the experimental conditions were designed so that the authored plans all provided some application opportunities for the available lessons. In addition, the simulated HICAP user was designed to apply all delivered lessons. Although this artificially increased the frequency of lesson use, similar improvements should occur whenever a user decides to apply a relevant, high-impact lesson, especially for domains where safety issues and speed are paramount to success.

The capabilities of certain learning algorithms can be evaluated by varying data set characteristics to determine when certain learning algorithms can be expected to perform well (e.g., Ref. [3]). Similarly, we plan to characterize the set of experimental conditions for which MD can use lessons to significantly improve plan evaluation performance measures.

## 8. Related work

Recently, researchers and practitioners have displayed an increased interest in exploring alternative methods to reach users with the right information, at the right place, at the right time, in the right format, right level of specificity, and so on. The processoriented approach that we propose to distribute applicable knowledge when and where it is needed in the context of decision support systems has been inspired and influenced by related work that varies along several dimensions. In this section, we discuss three forms of active distribution of objects to users that vary in their content (e.g., knowledge, information, instructions) and activation style (i.e., active, proactive, reactive). We do not intend this to be complete, but, instead, we briefly summarize some alternatives that can be explored in active distribution methods.

## 8.1. Distribution of knowledge in context

Three methods have been identified for knowledge delivery in context: active, reactive, and proactive [37]. The MD approach is an active method for lesson delivery. By monitoring targeted decision-making processes, these systems can automatically notify users of potentially relevant lessons whenever they are applicable.

The Air Campaign Planning Advisor (ACPA) [16] is composed of a web-based ASK system linked to a performance support tool through a model-based task tracking system. The goal of this integration is to prompt the user with relevant planning knowledge whenever needed. Monitoring the progress and the problems encountered by the user triggers ACPA. It supports two modes of dissemination: proactive and reactive. ACPA responds when a user asks for help (reactive) and when the system identifies potential problems in a user’s evolving plan (proactive) that can be addressed by a relevant story. These stories are stored as related sets of video clips (and associated text) that have been recorded by domain experts. The proactive method is not limited to knowledge about the current task, but it also embeds instructions (in the form of stories) that may bring relevant knowledge to users that concern the overall planning task.

In the active delivery of lessons in the MD approach, we use information from the targeted DSS to collect current state conditions. When there is a lesson applicable to an activity (e.g., task, decision) that the user is currently addressing and there are not sufficient conditions to justify lesson applicability, HICAP’s conversational case retrieval engine could ask the user for the state of unknown variables to assess the similarity between the current conditions and a potentially applicable lesson. Knowledge of the contextual business process is also used in the KnowMore project [2] to retrieve information from an organizational knowledge base. In Ref. [27], the authors propose different perspectives of active dissemination based on the user’s individual features (e.g., expertise level).

## 8.2. Active distribution of information and instructions

The active delivery of information about a current task, when the task is being performed to support overall process performance, is the basis of a category of systems named electronic performance support systems (EPSS) [7,13]. One important motivation of EPSS is to minimize training needs for using computer systems (e.g., by embedding training procedures). This is exemplified in MicrosoftR Excel [7].

From the perspective of active information retrieval, the basic strategy is to build a user’s model to track a user’s actions, goals, and needs. Budzik and Hammond [6] highlight the importance of identifying the user’s context to create better queries and, subsequently, to obtain better results. They attempt to anticipate a user’s needs by observing their interaction with everyday applications, and by building queries from the observed context. The information delivered in Ref. [6] originates from Internet information sources. One important conclusion about just-in-time delivery of information described in Ref. [26] suggests that users, indeed, use more information when exposed to active delivery.

Active dissemination of instructions is being investigated by researchers on help systems as illustrated by a series of three special issues on intelligent help systems for UNIX [14]. For example, Virou et al. [34] argue that an active help system has advantages compared with passive methods because the active approach knows the user’s goals. They propose that active methods, in order to track each user’s goals and actions, require a user model. The active delivery of instructions is named learning on demand in Ref. [39].

## 9. Discussion, conclusions, and next steps

## 9.1. Discussion

It seems inescapable to avoid discussing the distinction between information and knowledge, which has been addressed extensively by other authors (e.g., Refs. [10,17,24,25]). For the purpose of our work and to distinguish the type of knowledge delivered by the MD approach, we refer to knowledge as the strategies that humans apply to information to make decisions. Therefore, knowledge must be applicable and can be learned.

The primary reason for the utility of the MD approach concerns the distinction between information and knowledge. When one overlooks this distinction, MD may seem similar to MicrosoftR Office Assistant (Fig. 9) (e.g., Clippit), which, in contrast, distributes information and general knowledge in the format of instructions. For example, when the MicrosoftR Office Assistant activates a message such as the one shown on the right side of Fig. 9, the content refers to the specific topic of communication, which is the only commonality between the message and the current user’s activity. In this example, the instruction was activated only because the word communication was present in the user’s slide. While a lesson’s definition suggests that each may communicate a single experience, the example on the left side of Fig. 9 consists of two nonrelated instructions. The last sentence associates a task (i.e., create a new slide) with a suggestion (click New Slide on the Insert menu). The latter consists of knowledge to be learned, but it is too general to be disseminated actively, it is not integrated with the user’s decision-making process, and it does not have the potential to significantly impact the operation.

Training and help systems face the problem of overwhelming users with knowledge and information. This happens because keyword search strategies have low retrieval precision and are not integrated with their targeted decision processes. However, this is not a concern in our active lesson delivery approach because, as lessons are disseminated in the context of a decision support system, they can be retrieved according to their applicability (i.e., a lesson is disseminated only when it is applicable to the current task).

Active and proactive methods risk being intrusive and can potentially decrease a process’ performance rather than improve it. Intrusive methods require good precision to avoid disseminating knowledge when it is not needed. Our strategy to prevent this from happening is to tightly integrate the knowledge to its applicable processes so that knowledge artifacts are shared only in the context of their targeted processes where they are applicable. However, a lesson’s applicability is determined not only by the step in the decision process; the lesson’s preconditions must also be checked to verify its applicability. Retrieval precision rates may be improved by collecting preconditions during previous system usage by expert users, assuming that they are good at identifying relevant preconditions. In addition, we plan to compare the utility of different similarity measures, according to their efficiency and precision, and implement the most promising versions in ALDS.

The downside of tightly integrating lessons to applicable processes is the knowledge modeling required. We expect to compensate this by reducing the effort involved with lesson verification. As long as lessons are represented in a structured format and are indexed by their applicable processes, verification can be partially automated.

## 9.2. Conclusions

One conclusion of our work is that delivery of knowledge requires tight integration with the processes to which the knowledge is applicable. This integration will facilitate effectiveness because knowledge delivered will be immediately useful, thus reducing the chances of useless interruptions. A tight integration requires flexible process structures because knowledge is naturally dynamic and will require adaptations that may become infeasible in rigid architectures. This topic was the focus of the Workshop on Process-Oriented Knowledge Management [36] at the Fourth International Conference on Case-Based Reasoning. In that workshop, most speakers discussed the characteristics of architectures where knowledge is to be distributed, and they were unanimous in concluding these must be flexible.

![](/api/attachments/XB4PPXNY/fulltext/images/e51b78bd692d9c293014a903e7348f3e359abb5f1c9f589dddd1bb54f11dee8e.jpg)  
Fig. 9. Messages from MicrosoftR Office Assistant.

Another conclusion is that knowledge modeling is required to implement case retrieval and index lessons according to their applicability, thus permitting a tight integration with the targeted processes. The lesson here for the digital government is to use a flexible design when creating digital libraries, which should simplify the knowledge modeling effort (e.g., by using semiautomated modeling methods).

Knowledge modeling can be viewed as a powerful approach for converting information into knowledge. In NLLS, the current database with 35,000 textual lessons represents a huge collection of information. Once this information is processed and the reusable strategies are characterized, this collection can then be more easily applied in decision-making contexts.

## 9.3. Next steps

The first requirement to implement the MD approach is the knowledge modeling effort needed to index lessons by their applicability to targeted (sub)processes. Because there are approximately 35,000 textual lessons stored in the NLLS, one of the alternatives is to investigate methods for converting these lessons into cases (e.g., using textual CBR [19] methods). Another alternative is to investigate a collection tool (to replace the currently deployed collection tool) that directly converts collected lessons into the desired format [38].

The immediate capability that knowledge modeling will provide is to support an automatic (or semiautomatic) verification method. From this point, it is possible to also use reasoning methods to assist with decision support. This will permit experiential knowledge to be integrated and delivered to organizational processes when it is useful. Modeling will also assist with detecting experiential knowledge that has become outdated or useless, allowing it to be eliminated.

We want to extend MD’s implementation to different information systems (e.g., enterprise resource systems); and to different knowledge artifacts (e.g., best practices). Eventually, we can explore the dissemination of experiential knowledge together with training knowledge. In terms of evaluating the MD approach, we plan to perform an experiment with human subjects so that they can decide whether to apply delivered lessons during military planning efforts. Our evaluation of monitored distribution with simulated users, who applied every retrieved lesson, demonstrates the potential improvement in decision quality when augmenting a DSS with MD, allowing lessons to be delivered when and where they are needed.

## Acknowledgements

This research was supported by a contract provided by the Office of Naval Research. The authors would like to thank He´ctor Mun˜oz-Avila for his work in coding the knowledge base in HICAP and the simulated users for the experiment, as well as his support and advice on formatting lessons and designing the simulator. Thanks also to Andre´ Becker Testa for his help on the figures. Thanks to our reviewers for their comments, which helped us to significantly improve this article.

## References

[1] A. Aamodt, E. Plaza, Case-based reasoning: foundational issues, methodological variations, and system approaches, AI Commun. 7 (1) (1994) 39 – 59.

[2] A. Abecker, A. Bernardi, K. Hinkelmann, O. Kuehn, M. Sintek, Context-aware, proactive delivery of task-specific information: the know more project, Inf. Syst. Front. 2 (3/4) (2000) 253– 276.

[3] D.W. Aha, Generalizing case studies: a case study, Proceedings of the Ninth International Conference on Machine Learning, Aberdeen, Morgan Kaufmann, San Francisco, CA, 1992, pp. 1– 10.

[4] D.W. Aha, R. Weber (Eds.), Intelligent Lessons Learned Systems: Papers from the AAAI Workshop, AAAI Press, Menlo Park, CA, 2000, Technical Report WS-00-03.

[5] D.W. Aha, R. Weber, H. Mun˜oz-Avila, L.A. Breslow, K.M. Gupta, Lesson distribution gap, in: Proceedings of the IJCAI,

Seattle, WA, vol. 2, AAAI Press, Menlo Park, CA, 2001, pp.987– 992.

[6] J. Budzik, K.J. Hammond, User interactions with everyday applications as context for just-in-time information access, Proceedings of Intelligent User Interfaces, New Orleans, LA, ACM Press, New York, NY, USA, 2000, pp. 44 – 51.

[7] K. Cole, O. Fischer, P. Saltzman, Just-in-time knowledge delivery, Commun. ACM 40 (7) (1997) 49 – 53.

[8] G. Cybenko, B. Brewington, The foundations of information push and pull, in: G. Cybenko, D.P. O’Leary, J. Rissanen (Eds.), The Mathematics of Information Coding, Extraction, and Distribution, vol. 107, Springer-Verlag, New York, NY, 1999.

[9] T.H. Davenport, L. Prusak, Working Knowledge: How Organizations Manage What They Know, Harvard Business School Press, Boston, MA, 1998.

[10] P. Drucker, Post-Capitalist Society, Harper Collins, New York, 1993.

[11] M. Eby, Employee Burned While Changing Personal Vehicle Headlamp, Project Hanford Lessons Learned, Department of Energy, Jan. 2001, http://www.hanford.gov/lessons/sitell/ll01/ 2001-02.htm.

[12] D. Fisher, S. Deshpande, J. Livingston, Modeling the Lessons Learned Process, University of New Mexico, Albuquerque, NM, 1998, Department of Civil Engineering Research Report 123-11.

[13] G. Gery, Electronic Performance Support Systems: How and Why to Remake the Workplace Through Strategic Application of Technology, Gery Performance Press, Tolland, MA, 1991.

[14] S.J. Hegner, P. Mc Kevitt, P. Norvig, R. Wilensky (Eds.), Intelligent Help Systems for UNIX, Artificial Intelligence Review, vol. 14, Kluwer, Netherlands, 2000, pp. 1 – 4.

[15] C.W. Holsapple, K.D. Joshi, Decis. Support Syst. 31 (2001) 39–54.

[16] C. Johnson, L. Birnbaum, R. Bareiss, T. Hinrichs, War stories: harnessing organizational memories to support task performance, Intell.: New Visions AI Pract. 11 (1) (2000) 17 – 31.

[17] B. Kogut, U. Zander, Knowledge of the firm, combinative capabilities, and the replication of technology, Organ. Sci. 3 (1992) 383– 397.

[18] P. Williams (Ed.), Learning from Mistakes: Knowledge Management Magazine, Bizmedia Ltd., London, UK, Apr. 2001, p. 40.

[19] M. Lenz, K. Ashley (Eds.), Textual Case-Based Reasoning: Papers from the AAAI-98 Workshop, AAAI Press, Menlo Park, CA, 1998, Technical Report, WS-98-12.

[20] J. Liebowitz, Information Technology Management: A Knowledge Repository, CRC Press, Boca Raton, FL, 1999.

[21] J. Liebowitz, Knowledge Management Handbook, CRC Press, Boca Raton, FL, 1999.

[22] H. Mun˜oz-Avila, D.W. Aha, L.A. Breslow, D. Nau, HICAP: an interactive case-based planning architecture and its application to NEOs, Proceedings of the Eleventh Conference on Innovative Applications of Artificial Intelligence, AAAI Press, Orlando, FL, 1999, pp. 870 – 875.

[23] Navy Lessons Learned System, Navy Warfare Development Command, Navy Lessons Learned Database, Feb. 2001 [http://

www.nwdc.navy.mil/Command/NavyLessonsLearned/default. asp].

[24] I. Nonaka, H. Takeuchi, The Knowledge-Creating Company, Oxford University Press, Oxford, 1995.

[25] M. Polanyi, The Tacit Dimension, Doubleday, Garden City, NY, 1966.

[26] B.J. Rhodes, P. Maes, Just-in-time information retrieval agents, IBM Syst. J. 39 (3 and 4) (2000) 685 – 704.

[27] U. Reimer, A. Margelisch, M. Staudt, A knowledge-based approach to support business processes, Proceedings of the AAAI 2000 Spring Symposium Series: Bringing Knowledge to Business Processes, Stanford, CA, AAAI Press, Menlo Park, CA, Mar. 2000, TR (SS-00-03).

[28] P. Secchi (Ed.), Proceedings of Alerts and LL: An Effective Way to Prevent Failures and Problems, ESTEC, Noordwijk, The Netherlands, Sep. 1999, Technical Report WPP-167.

[29] P. Secchi, R. Ciaschi, D. Spence, A concept for an ESA lessons learned system, in: P. Secchi (Ed.), Proceedings of Alerts and LL: An Effective Way to Prevent Failures and Problems, ESTEC, Noordwijk, The Netherlands, Sep. 1999, pp. 57 – 61, Technical Report WPP-167.

[30] SELLS, Proceedings of the SELLS Fall Meeting, Fall, 2000, hhttp://tis.eh.doe.gov/ll/proceedings/proceedings1000.htmi.

[31] S. Staab, R. Studer, H.P. Schnurr, Y. Sure, Knowledge processes and ontologies, IEEE Intell. Syst. 16 (1) (Jan./Feb. 2001) 26 – 34.

[32] Universal Naval Task List (UNTL), OPNAVINST 3500.38, Navy Modeling and Simulation Office, Arlington, VA, Sep. 1996.

[33] G. van Heijst, R. van der Spek, E. Kruizinga, Organizing corporate memories, in: R. Dieng, J. Vanwelkenhuysen (Eds.), KAW’96, Special Track on Corporate Memory and Enterprise Modeling, Nov. 1996.

[34] M. Virou, J. Jones, M. Millington, Virtues and problems of an active help system for UNIX, in: S.J. Hegner, P. Mc Kevitt, P. Norvig, R. Wilensky (Eds.), Artificial Intelligence Review, vol. 14, Kluwer, The Netherlands, 2000, pp. 23 – 42.

[35] I. Watson, Applying Case-Based Reasoning: Techniques for Enterprise Systems, Morgan Kaufmann Publishers, San Francisco, CA, 1997.

[36] R. Weber, C.G. von Wangenheim (Eds.), Case-Based Reasoning: Papers from the ICCBR-2001 Workshop Program, Naval Research Laboratory, Navy Center for Applied Research in Artificial Intelligence, Washington, DC, Jul. 2001, Technical Note AIC-01-003.

[37] R. Weber, D.W. Aha, I. Becerra-Fernandez, Intelligent lessons learned systems, Int. J. Expert Syst. Res. Appl. 20 (1) (Jan. 2001) 17–34.

[38] R. Weber, L. Breslow, N. Sandhu, On the technological, human, and managerial issues in sharing organizational lessons, Proceedings of the Fourteenth Annual Conference of the International Florida Artificial Intelligence Research Society, AAAI Press, Menlo Park, CA, 2001, pp. 334–338.

[39] Y. Ye, G. Fischer, Information delivery in support of learning reusable software components in demand, Proceedings of the 2002 International Conference on Intelligent User Interfaces, ACM Press, New York, NY, 2002, pp. 159 – 166.

![](/api/attachments/XB4PPXNY/fulltext/images/2435612b40f44fd1332f13dda2a00d6be7f47dbf74f192193b16bb85ce69ca1e.jpg)

Dr. Rosina Weber is an Assistant Professor in the College of Information Science and Technology at Drexel University (Philadelphia, PA). She holds a Bachelors degree in Business Administration (1988), a Masters in Operations Research (1994) and a Doctorate in Production Engineering (1998) from the Federal University of Santa Catarina (Brazil). She also has 5 years of industry experience mostly in corporate finance. Her topics of interest include

Case-Based Reasoning, Fuzzy Set Theory, and Information Extraction applied to Knowledge Management systems in Finance, Law, Military, and Health Sciences. Copies of papers, abstracts, demos, and slides are available at http://www.pages.drexel.edu/\~rw37/. Dr. Weber worked for 2 years at the Navy Center for Applied Research in Artificial Intelligence (NCARAI), a branch of the Naval Research Laboratory (in Washington, DC), as a member of the Intelligent Decision Aids Group, during which time her work was funded by ONR and the University of Wyoming. Together with Dr. Aha, they have organized a AAAI 2000 workshop on Intelligent Lessons Learned Systems and recently published a survey on lessons learned systems.

Dr. David W. Aha leads the Intelligent Decision Aids Group at the Naval Research Laboratory’s Navy Center for Applied Research in Artificial Intelligence. This group’s projects have recently focused on mixed-initiative planning, case-based reasoning, knowledge management (intelligent lessons learned systems), and machine learning. He has (co)organized several meetings related to these areas, is an Action Editor for the Machine Learning journal, and is on the Review Board for Applied Intelligence, where his coedited special issue on Interactive CBR was recently published. The IDA Group’s current focus includes IPATS, an integrated plan authoring tool suite that integrates hierarchical AI planning techniques in project planning tools using graphical user interfaces for creating operational plans. For more information, please see www.aic.nrl. navy.mil/\~aha/ida.
